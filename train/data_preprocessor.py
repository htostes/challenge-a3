from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from config_loader import ConfigFileLoader


def build_pipeline_rf(
    params: dict = None,
    seed: int = None,
    config_file_path: str = None,
) -> Pipeline:
    """Build scikit learn pipeline for the model. Every preprocessing step should be here

    Args:
        params (dict, optional): params to pass to the model. Defaults to None.
        seed (int, optional): sedd, for randomness. Defaults to None.
        config_file_path (str, optional): path for a config file, if none is passed uses the default one in config.yaml. Defaults to None.

    Returns:
        Pipeline: scikit learn pipeline ready to be fitted.
    """
    if seed is None:
        seed = ConfigFileLoader(config_file_path).get_seed()

    if params is None:
        params = ConfigFileLoader(config_file_path).get_params()

    pipeline = Pipeline(
        [
            ("scaler", StandardScaler()),
            ("random_forest", RandomForestClassifier(random_state=seed, **params)),
        ]
    )
    return pipeline
