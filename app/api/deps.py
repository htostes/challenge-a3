import crud, schemas
from core.config import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db() -> dict:
    """Creates a database session.

    Yields:
        Dict: Database in dictionary format
    """
    fake_db = {
        "test_user": {
            "username": "test_user",
            "hashed_password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
        }
    }
    return fake_db


def get_current_user(
    db: dict = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> schemas.User:
    """Validates token and get user and company from payload.

    Args:
        db (dict, optional): Connection with database. Defaults to Depends(get_db).
        token (str, optional): Access token. Defaults to Depends(oauth2_scheme).

    Raises:
        credentials_exception: In case user or company data is None
        credentials_exception: In case jwt couldn't be decoded
        credentials_exception: In case user of payload couldn't be founded in database

    Returns:
        schemas.User: User found in access token payload
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("user")
        if username is None:
            raise credentials_exception
        token_data = schemas.token.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.user.get(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
