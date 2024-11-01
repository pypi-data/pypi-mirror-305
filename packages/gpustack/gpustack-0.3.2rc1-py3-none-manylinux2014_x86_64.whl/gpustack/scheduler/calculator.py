import asyncio
from enum import Enum
import logging
from pathlib import Path
import subprocess
from dataclasses import dataclass
from typing import List, Optional
from dataclasses_json import dataclass_json


from gpustack.config.config import get_global_config
from gpustack.schemas.models import Model, ModelInstance, SourceEnum
from gpustack.utils.compat_importlib import pkg_resources
from gpustack.utils.hub import match_hugging_face_files, match_model_scope_file_paths
from gpustack.utils import platform

logger = logging.getLogger(__name__)
fetch_file_timeout_in_seconds = 5


class GPUOffloadEnum(str, Enum):
    Full = "full"
    Partial = "partial"
    Disable = "disable"


@dataclass_json
@dataclass
class layerMemoryEstimate:
    uma: int
    nonuma: int
    handleLayers: Optional[int]


@dataclass_json
@dataclass
class memoryEstimate:
    offloadLayers: int
    fullOffloaded: bool
    ram: layerMemoryEstimate
    vrams: List[layerMemoryEstimate]


@dataclass_json
@dataclass
class estimate:
    items: List[memoryEstimate]
    contextSize: int
    architecture: str
    embeddingOnly: bool
    distributable: bool
    reranking: bool


@dataclass_json
@dataclass
class modelResoruceClaim:
    estimate: estimate


@dataclass
class ModelInstanceResourceClaim:
    model_instance: ModelInstance
    resource_claim_estimate: estimate

    # overwrite the hash to use in uniquequeue
    def __hash__(self):
        return self.model_instance.id

    # compare the model instance id
    def __eq__(self, other):
        if isinstance(other, ModelInstanceResourceClaim):
            return self.model_instance.id == other.model_instance.id
        return False


async def _gguf_parser_command(
    model: Model, offload: GPUOffloadEnum = GPUOffloadEnum.Full, **kwargs
):
    command = "gguf-parser"
    if platform.system() == "windows":
        command += ".exe"

    command_path = pkg_resources.files("gpustack.third_party.bin.gguf-parser").joinpath(
        command
    )
    execuable_command = [
        command_path,
        "--ctx-size",
        "8192",
        "--in-max-ctx-size",
        "--skip-tokenizer",
        "--skip-architecture",
        "--skip-metadata",
        "--cache-expiration",
        "168h0m0s",
        "--no-mmap",
        "--json",
    ]

    cache_dir = kwargs.get("cache_dir")
    if cache_dir:
        execuable_command.append("--cache-path")
        execuable_command.append(cache_dir)

    if offload == GPUOffloadEnum.Full:
        execuable_command.append("--gpu-layers")
        execuable_command.append("-1")
    elif offload == GPUOffloadEnum.Partial:
        execuable_command.append("--gpu-layers-step")
        execuable_command.append("1")
    elif offload == GPUOffloadEnum.Disable:
        execuable_command.append("--gpu-layers")
        execuable_command.append("0")

    tensor_split = kwargs.get("tensor_split")
    if tensor_split:
        tensor_split_str = ",".join(
            [str(int(i / (1024 * 1024))) for i in tensor_split]
        )  # convert to MiB to prevent overflow
        execuable_command.append("--tensor-split")
        execuable_command.append(tensor_split_str)

    rpc = kwargs.get("rpc")
    if rpc:
        rpc_str = ",".join([v for v in rpc])
        execuable_command.append("--rpc")
        execuable_command.append(rpc_str)

    source_args = await _gguf_parser_command_args_from_source(model, **kwargs)
    execuable_command.extend(source_args)
    return execuable_command


async def calculate_model_resource_claim(
    model_instance: ModelInstance,
    model: Model,
    offload: GPUOffloadEnum = GPUOffloadEnum.Full,
    **kwargs,
) -> ModelInstanceResourceClaim:
    """
    Calculate the resource claim of the model instance.
    Args:
        model_instance: Model instance to calculate the resource claim for.
        model: Model to calculate the resource claim for.
    """

    logger.info(f"Calculating resource claim for model instance {model_instance.name}")

    command = await _gguf_parser_command(model, offload, **kwargs)
    try:
        process = await asyncio.create_subprocess_exec(
            *command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            raise subprocess.CalledProcessError(
                process.returncode, command, output=stdout, stderr=stderr
            )

        cmd_output = stdout.decode()
        claim = modelResoruceClaim.from_json(cmd_output)

        if offload == GPUOffloadEnum.Full:
            logger.info(
                f"Calculated resource claim for full offload model instance {model_instance.name}, "
                f"claim: {claim.estimate.items[0]}"
            )
        elif offload == GPUOffloadEnum.Partial:
            logger.info(
                f"Calculated resource claim for partial offloading model instance {model_instance.name}, "
                f"least claim: {claim.estimate.items[1]}, "
                f"most claim: {claim.estimate.items[len(claim.estimate.items) - 2]}"
            )
        elif offload == GPUOffloadEnum.Disable:
            logger.info(
                f"Calculated resource claim for disabled offloading model instance {model_instance.name}, "
                f"claim: {claim.estimate.items[0]}"
            )

        return ModelInstanceResourceClaim(model_instance, claim.estimate)

    except subprocess.CalledProcessError as e:
        raise Exception(
            f"Failed to execution {command}, error: {e}, ",
            f"stderr: {e.stderr.decode()}, ",
            f"stdout: {e.stdout.decode()}",
        )
    except Exception as e:
        raise Exception(
            f"Failed to parse the output of {command}, error: {e}",
        )


async def _gguf_parser_command_args_from_source(  # noqa: C901
    model: Model, **kwargs
) -> List[str]:
    """
    Get the model url based on the model source.
    Args:
        model: Model to get the url for.
    """

    if model.source not in [
        SourceEnum.OLLAMA_LIBRARY,
        SourceEnum.HUGGING_FACE,
        SourceEnum.MODEL_SCOPE,
    ]:
        raise ValueError(f"Unsupported source: {model.source}")

    try:
        if model.source == SourceEnum.OLLAMA_LIBRARY:
            args = ["-ol-model", model.ollama_library_model_name]
            ol_base_url = kwargs.get("ollama_library_base_url")
            if ol_base_url:
                args.extend(["-ol-base-url", ol_base_url])
            return args
        elif model.source == SourceEnum.HUGGING_FACE:
            args = ["-hf-repo", model.huggingface_repo_id]
            if model.huggingface_filename:
                model_filename = await asyncio.wait_for(
                    asyncio.to_thread(
                        hf_model_filename,
                        model.huggingface_repo_id,
                        model.huggingface_filename,
                    ),
                    timeout=fetch_file_timeout_in_seconds,
                )
                args.extend(["-hf-file", model_filename])

            global_config = get_global_config()
            if global_config.huggingface_token:
                args.extend(["-hf-token", global_config.huggingface_token])

            return args
        elif model.source == SourceEnum.MODEL_SCOPE:
            file_path = await asyncio.wait_for(
                asyncio.to_thread(
                    model_scope_file_path,
                    model.model_scope_model_id,
                    model.model_scope_file_path,
                ),
                timeout=fetch_file_timeout_in_seconds,
            )
        return ["-ms-repo", model.model_scope_model_id, "-ms-file", file_path]
    except asyncio.TimeoutError:
        raise Exception(f"Timeout when getting the file for model {model.name}")
    except Exception as e:
        raise Exception(f"Failed to get the file for model {model.name}, error: {e}")


def hf_model_filename(repo_id: str, filename: Optional[str] = None) -> str | None:
    if filename is None:
        return None
    else:
        matching_files = match_hugging_face_files(repo_id, filename)
        if len(matching_files) == 0:
            raise ValueError(f"File {filename} not found in {repo_id}")

        filename = Path(matching_files[0]).name
        return filename


def model_scope_file_path(model_id: str, file_path: str) -> str:
    file_paths = match_model_scope_file_paths(model_id, file_path)
    if len(file_paths) == 0:
        raise ValueError(f"File {file_path} not found in {model_id}")
    return file_paths[0]
