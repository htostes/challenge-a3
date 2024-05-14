import crud, schemas
from api import deps
from core import security
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from core.config import settings

router = APIRouter()


@router.post("/token", response_model=schemas.Token)
@security.LIMITER.limit(f"{settings.REQUEST_LIMIT_PER_MINUTE}/minute")
async def login_for_access_token(
    request: Request,
    db: dict = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
) -> dict:
    """Endpoint to get access token for user in form_data.

    Args:
        db (dict, optional): Connection with database. Defaults to Depends(deps.get_db).
        form_data (OAuth2PasswordRequestForm, optional): Form with user and password. Defaults to Depends().

    Raises:
        HTTPException: In case username or password is incorrect

    Returns:
        dict: Dictionary with access token and token type
    """
    user = crud.user.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(
        data={"user": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}
