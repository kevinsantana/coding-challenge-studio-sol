from fastapi import APIRouter

from valid_password.api.v1.endpoints import healthcheck, check_rules


v1 = APIRouter()

v1.include_router(healthcheck.router, tags=["healthcheck"])
v1.include_router(check_rules.router, tags=["rules"])
