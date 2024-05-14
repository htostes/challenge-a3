from typing import Union

from pydantic import BaseModel


class Token(BaseModel):
    """Class that references token schema.

    Args:
        BaseModel (pydantic.BaseModel): BaseModel for the schema
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Class that references token payload schema.

    Args:
        BaseModel (pydantic.BaseModel): BaseModel for the schema
    """

    username: Union[str, None] = None
