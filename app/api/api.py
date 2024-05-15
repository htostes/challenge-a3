from api.endpoints.v1 import token, models
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(token.router, tags=["token"])
api_router.include_router(models.router, prefix="/models", tags=["models"])
