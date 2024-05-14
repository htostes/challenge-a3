from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_pipeline_rf(n_estimators) -> Pipeline:

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('random_forest', RandomForestClassifier(n_estimators=n_estimators))
    ])
    return pipeline