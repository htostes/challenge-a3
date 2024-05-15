from typing import Optional
import mlflow.sklearn

import schemas


def get(model_path: dict) -> Optional[schemas.Model]:
    """Search for model in source and retrieve model estimator.

    Args:
        model_path (str): Path from model to load

    Returns:
        Optional[schemas.Model]: Schema from model that contains model estimator if found.
    """
    model = mlflow.sklearn.load_model(model_path)
    if model:
        return schemas.Model(**model)