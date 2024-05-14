from app.api.api import api_router
from app.core.security import LIMITER
from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded


app = FastAPI()
app.state.limiter = LIMITER
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.include_router(api_router)
