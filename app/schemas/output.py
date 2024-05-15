from pydantic import BaseModel


class OutputIris(BaseModel):
    """Class that references output from model iris schema.

    Args:
        BaseModel (pydantic.BaseModel): BaseModel for the schema
    """

    classification: str
