from fastapi import APIRouter

from valid_password.api.v1.endpoints import healthcheck


v1 = APIRouter()

v1.include_router(healthcheck.router, prefix="/health", tags=["healthcheck"])
