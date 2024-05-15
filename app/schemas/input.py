from pydantic import BaseModel


class InputIris(BaseModel):
    """Class that references input from model iris schema.

    Args:
        BaseModel (pydantic.BaseModel): BaseModel for the schema
    """

    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float