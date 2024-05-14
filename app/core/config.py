import secrets

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Class that has all global configurations for this project.

    Args:
        BaseSettings (pydantic.BaseSettings): Class base for settings
    """

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    # 60 min * 24h * 1d = 1 dia
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 1
    REQUEST_LIMIT_PER_MINUTE: int = 15


settings = Settings()
