from typing import Optional
import httpx
import logging

from fastapi import APIRouter, Request, Response, status
from openai.types import Model as OAIModel
from openai.pagination import SyncPage
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from gpustack.api.exceptions import (
    BadRequestException,
    InvalidException,
    NotFoundException,
    OpenAIAPIError,
    OpenAIAPIErrorResponse,
    ServiceUnavailableException,
)
from gpustack.api.responses import StreamingResponseWithStatusCode
from gpustack.http_proxy.load_balancer import LoadBalancer
from gpustack.schemas.models import Model, ModelInstance, ModelInstanceStateEnum
from gpustack.server.deps import SessionDep

router = APIRouter()

logger = logging.getLogger(__name__)

load_balancer = LoadBalancer()


@router.get("/models")
async def list_models(
    session: SessionDep,
    embedding_only: Optional[bool] = None,
    reranker: Optional[bool] = None,
):
    statement = select(Model).where(Model.ready_replicas > 0)

    if embedding_only is not None:
        statement = statement.where(Model.embedding_only == embedding_only)

    if reranker is not None:
        statement = statement.where(Model.reranker == reranker)

    models = (await session.exec(statement)).all()
    result = SyncPage[OAIModel](data=[], object="list")
    for model in models:
        result.data.append(
            OAIModel(
                id=model.name,
                object="model",
                created=int(model.created_at.timestamp()),
                owned_by="gpustack",
            )
        )
    return result


@router.post("/chat/completions")
async def chat_completions(session: SessionDep, request: Request):
    return await proxy_request_by_model(request, session, "chat/completions")


@router.post("/completions")
async def completions(session: SessionDep, request: Request):
    return await proxy_request_by_model(request, session, "completions")


@router.post("/embeddings")
async def embeddings(session: SessionDep, request: Request):
    return await proxy_request_by_model(request, session, "embeddings")


async def proxy_request_by_model(  # noqa: C901
    request: Request, session: SessionDep, endpoint: str
):
    """
    Proxy the request to the model instance that is running the model specified in the
    request body.
    """

    try:
        body = await request.json()
    except Exception as e:
        raise BadRequestException(
            message=f"We could not parse the JSON body of your request: {e}",
            is_openai_exception=True,
        )

    model_name = body.get("model")
    if not model_name:
        raise InvalidException(
            message="Missing 'model' field",
            is_openai_exception=True,
        )

    model = await Model.one_by_field(session=session, field="name", value=model_name)
    if not model:
        raise NotFoundException(
            message="Model not found",
            is_openai_exception=True,
        )

    stream = body.get("stream", False)

    request.state.model = model
    request.state.stream = stream

    instance = await get_running_instance(session, model.id)

    url = f"http://{instance.worker_ip}:{instance.port}/v1/{endpoint}"
    logger.debug(f"proxying to {url}")

    headers = filter_headers(request.headers)

    timeout = 120

    try:
        if stream:
            if "stream_options" not in body:
                # Defaults to include usage.
                # TODO Record usage without client awareness.
                body["stream_options"] = {"include_usage": True}

            async def stream_generator():
                try:
                    async with httpx.AsyncClient() as client:
                        async with client.stream(
                            method=request.method,
                            url=url,
                            headers=headers,
                            json=body,
                            timeout=timeout,
                        ) as resp:
                            async for chunk in resp.aiter_text():
                                yield chunk, resp.status_code
                except httpx.RequestError:
                    error_response = OpenAIAPIErrorResponse(
                        error=OpenAIAPIError(
                            message="Service unavailable. Please retry your requests after a brief wait.",
                            code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            type="ServiceUnavailable",
                        ),
                    )
                    yield error_response.model_dump_json(), status.HTTP_503_SERVICE_UNAVAILABLE
                except Exception as e:
                    error_response = OpenAIAPIErrorResponse(
                        error=OpenAIAPIError(
                            message=f"Internal server error: {e}",
                            code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            type="InternalServerError",
                        ),
                    )
                    yield error_response.model_dump_json(), status.HTTP_500_INTERNAL_SERVER_ERROR

            return StreamingResponseWithStatusCode(
                stream_generator(), media_type="text/event-stream"
            )
        else:
            async with httpx.AsyncClient() as client:
                resp = await client.request(
                    method=request.method,
                    url=url,
                    headers=headers,
                    json=body,
                    timeout=timeout,
                )
                return Response(
                    status_code=resp.status_code,
                    headers=dict(resp.headers),
                    content=resp.content,
                )
    except Exception as e:
        raise ServiceUnavailableException(
            message=f"An unexpected error occurred: {e}",
            is_openai_exception=True,
        )


def filter_headers(headers):
    return {
        key: value
        for key, value in headers.items()
        if key.lower() != "content-length" and key.lower() != "host"
    }


async def get_running_instance(session: AsyncSession, model_id: int):
    model_instances = await ModelInstance.all_by_field(
        session=session, field="model_id", value=model_id
    )
    running_instances = [
        inst for inst in model_instances if inst.state == ModelInstanceStateEnum.RUNNING
    ]
    if not running_instances:
        raise ServiceUnavailableException(
            message="No running instances available",
            is_openai_exception=True,
        )
    return await load_balancer.get_instance(running_instances)
