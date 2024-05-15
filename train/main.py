from data_loader import load_raw_data_from_url
from data_preprocessor import build_pipeline_rf
from data_splitter import split_raw_data_train_test
from model_trainer import train_pipeline


url = r"https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

header = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "class",
]

data = load_raw_data_from_url(url, header)

pipeline = build_pipeline_rf()

X_train, X_test, Y_train, Y_test = split_raw_data_train_test(data, y_name="class")

train_pipeline(
    pipeline=pipeline,
    X_train=X_train,
    X_test=X_test,
    Y_train=Y_train,
    Y_test=Y_test,
    experiment_name="iris_model",
)
