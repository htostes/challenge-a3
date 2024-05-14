from typing import Optional, Union

import schemas
from core.security import verify_password


def get(db: dict, username: str) -> Optional[schemas.User]:
    """Search for user in database and retrieve email and hased password.

    Args:
        db (dict): Connection with database
        username (str): User name to search

    Returns:
        Optional[schemas.UserInDB]: Schema from user that contains hashed password if found.
    """
    user = db.get(username, None)
    if user:
        return schemas.UserInDB(**user)


def authenticate_user(
    db: dict, username: str, password: str
) -> Union[schemas.User, bool]:
    """Checks if hashed password found in database matchs password in args.

    Args:
        db (dict): Connection with database
        username (str): User name to search
        password (str): Raw password from user

    Returns:
        Union[schemas.User, bool]: Schema from user.
    """
    user = get(db, username)
    if not user:
        return False
    if verify_password(password, user.hashed_password):
        return user
    else:
        return False
