from typing import Optional, List
import mlflow.sklearn

import schemas


# This could be a table in a database or a yml file with all available models, ids and path to retrieve.
__ALL_MODELS = {
    "iris": {
        "path": "/app/models/iris"
    }
}


def get(name: str) -> Optional[schemas.ModelIn]:
    """Search for model in source and retrieve model estimator.

    Args:
        model_path (str): Path from model to load

    Returns:
        Optional[schemas.Model]: Schema from model that contains model estimator if found.
    """
    # This could be retrieved by id. The ids can be listed with the next method
    model = mlflow.sklearn.load_model(__ALL_MODELS[name]["path"])
    if model:
        model_dict = {
            "name": name,
            "estimator": model
        }
        return schemas.ModelIn(**model_dict)
    
def list_all() -> List[schemas.Model]:
    return [schemas.Model(name=model_name) for model_name in __ALL_MODELS.keys()]