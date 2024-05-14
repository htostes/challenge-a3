from api.endpoints.v1 import token
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(token.router, tags=["token"])
