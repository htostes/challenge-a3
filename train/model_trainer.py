import mlflow
import mlflow.sklearn
import sklearn.metrics
from sklearn.pipeline import Pipeline


def train_pipeline(pipeline: Pipeline, X_train, Y_train, X_test, Y_test, experiment_name):

    mlflow.set_experiment(experiment_name)
    with mlflow.start_run() as run:
        # Train the model
        pipeline.fit(X_train, Y_train)

        # Evaluate the model
        class_list = pipeline.classes_.tolist()
        Y_test_encoded = [class_list.index(y) for y in Y_test]
        Y_predicted = pipeline.predict(X_test)
        Y_predicted_encoded = [class_list.index(y) for y in Y_predicted]
            
        accuracy_score = sklearn.metrics.accuracy_score(Y_test_encoded, Y_predicted_encoded)
        mlflow.log_metric("accuracy_score", accuracy_score)
        
        f1_score = sklearn.metrics.f1_score(Y_test_encoded, Y_predicted_encoded, average='weighted')
        mlflow.log_metric("f1_score", f1_score)

        # Save the model
        mlflow.sklearn.save_model(
            sk_model=pipeline, path="artifacts",
        )