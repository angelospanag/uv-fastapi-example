import uuid

import structlog
from fastapi import Depends, FastAPI, Request, Response

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users

app = FastAPI()
logger = structlog.get_logger()


@app.middleware("http")
async def logger_middleware(request: Request, call_next):
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(
        path=request.url.path,
        method=request.method,
        client_host=request.client.host,
        request_id=str(uuid.uuid4()),
    )
    response = await call_next(request)

    structlog.contextvars.bind_contextvars(
        status_code=response.status_code,
    )

    # Exclude /healthcheck endpoint from producing logs
    if request.url.path != "/healthcheck":
        if 400 <= response.status_code < 500:
            logger.warn("Client error")
        elif response.status_code >= 500:
            logger.error("Server error")
        else:
            logger.info("OK")

    return response


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/healthcheck")
async def healthcheck():
    return Response()


@app.get("/", dependencies=[Depends(get_query_token)])
async def root():
    logger.info("In root path")
    return {"message": "Hello Bigger Applications!"}
