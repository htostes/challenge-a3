import crud, schemas
from typing import List
from api import deps
from fastapi import APIRouter, Depends, Request
from core.config import settings
from core.security import LIMITER
import numpy as np


router = APIRouter()


@router.get(
    "/",
    description="""
        Retireve all available models
    """,
)
@LIMITER.limit(f"{settings.REQUEST_LIMIT_PER_MINUTE}/minute")
def models(
    request: Request,
    current_user: schemas.User = Depends(deps.get_current_user),
) -> List[schemas.Model]:
    """Endpoint to list all available models

    Args:
        request (Request): Request object for standarization.
        current_user (schemas.User, optional): For authentication. Defaults to Depends(deps.get_current_user).

    Returns:
        list: List of available models
    """
    models_list = crud.model.list_all()
    if models_list:
        return models_list
    else:
        return {"message": "No models found."}


# Here could be by /models/{id}, but then would be needed to estabilish
# which output and input schema belongs to which model.
# Then, for simplicity Im going to make static
@router.post(
    "/iris",
    description="""
        Predict endpoint for the model iris.
    """,
)
@LIMITER.limit(f"{settings.REQUEST_LIMIT_PER_MINUTE}/minute")
def iris_predict(
    request: Request,
    inputs: List[schemas.InputIris],
    current_user: schemas.User = Depends(deps.get_current_user),
) -> List[schemas.OutputIris]:
    """Predict endpoint for the iris model

    Args:
        request (Request): Request object for standarization.
        inputs (List[schemas.InputIris]): List of inputs to predict iris class.
        current_user (schemas.User, optional): For authentication. Defaults to Depends(deps.get_current_user).

    Returns:
        List[schemas.OutputIris]: List of the iris classes
    """
    model = crud.model.get("iris")
    transformed_input = np.array(
        [
            [
                input.sepal_length,
                input.sepal_width,
                input.petal_length,
                input.petal_width,
            ]
            for input in inputs
        ]
    )
    np_arr_predict = model.estimator.predict(transformed_input)
    response = [schemas.OutputIris(classification=output) for output in np_arr_predict]
    return response
