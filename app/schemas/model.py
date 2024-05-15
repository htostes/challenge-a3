from pydantic import BaseModel, BaseSettings
from sklearn.base import BaseEstimator


class Model(BaseModel):
    """Class that references model schema.

    Args:
        BaseModel (pydantic.BaseModel): BaseModel for the schema
    """

    estimator: 'BaseEstimator'
    
    class Config:
        arbitrary_types_allowed = True