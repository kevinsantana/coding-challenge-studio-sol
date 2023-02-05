import sys
import time
import urllib3
from uuid import uuid1
from datetime import datetime

from loguru import logger
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from valid_password import __version__
from valid_password.api.v1.api import v1
from valid_password.exceptions import BaseException


urllib3.disable_warnings()

logger.add(sys.stdout, colorize=True)
logger.level("REQUEST RECEIVED", no=38, color="<yellow>")
logger.level("REQUEST FINISHED", no=39, color="<yellow>")
logger.level("EXCEPTION", no=38, color="<red>")


def include_router(app: FastAPI):
    app.include_router(v1, prefix="/v1")


def load_exceptions(app: FastAPI):
    @app.exception_handler(BaseException)
    async def valid_password_exception_handler(
        request: Request, exception: BaseException
    ):  # pragma: no cover
        return JSONResponse(
            status_code=exception.status,
            content={
                "timestamp": str(datetime.now()),
                "status": exception.status,
                "error": exception.error,
                "message": exception.message,
                "method": request.method,
                "path": request.url.path,
                "error_details": exception.error_details,
            },
        )


def http_middleware(app: FastAPI):
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):  # pragma: no cover
        requets_id = uuid1()

        logger.log(
            "REQUEST RECEIVED",
            f"[{request.method}] ID: {requets_id} - IP: {request.client.host}"
            + f" - ENDPOINT: {request.url.path}",
        )

        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        logger.log(
            "REQUEST FINISHED",
            f"[{request.method}] ID: {requets_id} - IP: {request.client.host}"
            + f" - ENDPOINT: {request.url.path} - TEMPO: {process_time}",
        )
        response.headers["X-Process-Time"] = str(process_time)
        return response


def start_application():
    app = FastAPI(
        title="VALID-PASSWORD-API",
        version=__version__,
        docs_url="/v1/docs",
    )
    include_router(app)
    load_exceptions(app)
    http_middleware(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_credentials=True,
        allow_headers=["*"],
    )
    return app
