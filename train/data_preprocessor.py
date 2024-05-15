from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from config_loader import ConfigFileLoader


def build_pipeline_rf(
    params: dict = None, 
    seed: int = None,
    config_file_path: str = None,
) -> Pipeline:

    if seed is None:
        seed = ConfigFileLoader(config_file_path).get_seed()
        
    if params is None:
        params = ConfigFileLoader(config_file_path).get_params()
        
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('random_forest', RandomForestClassifier(random_state=seed, **params))
    ])
    return pipeline