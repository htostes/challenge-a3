from pydantic import BaseModel


class User(BaseModel):
    """Class that references user schema.

    Args:
        BaseModel (pydantic.BaseModel): BaseModel for the schema
    """

    username: str


class UserInDB(User):
    """Class that extends from User to define schema for user to fetch password in db.

    Args:
        User (pydantic.BaseModel): BaseModel from User for this schema
    """

    hashed_password: str
