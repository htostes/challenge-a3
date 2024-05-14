import hashlib
from datetime import datetime, timedelta

from app.core.config import settings
from jose import jwt
from slowapi import Limiter
from slowapi.util import get_remote_address

LIMITER: Limiter = Limiter(key_func=get_remote_address)


def get_password_hash(password: str) -> str:
    """Transform raw password string in hashed password.

    Args:
        password (str): Raw password string

    Returns:
        str: Hashed password
    """
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compares password that comes in request with found in database.

    Args:
        plain_password (str): Raw password that comes in request
        hashed_password (str): Hashed password found in database

    Returns:
        bool: True if passwords matchs, False otherwise
    """
    return get_password_hash(plain_password) == hashed_password


def create_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
) -> str:
    """Creates jwt  to access other endpoints based on
    data (payload) and expires_delta (expiration time).

    Args:
        data (dict): Payload to put in jwt
        expires_delta (timedelta, optional): Expiration time to jwt. Defaults to timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES).

    Returns:
        str: Access token
    """
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
