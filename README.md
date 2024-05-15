# Challenge-a3

## The problem

The Iris database is widely used in the machine community learning and is composed of measurements of four characteristics of iris flowers
(sepal length, sepal width, petal length and
petal) of three different species of iris (Iris setosa, Iris versicolor and Iris virginica).
Your goal is to build a machine learning model that is capable of
classify flowers into one of three species based on these characteristics. The database is available via the following url
https://archive.ics.uci.edu/dataset/53/iris. The dataset contains 3 classes of
50 instances each, where each class refers to a type of iris plant. One
class is linearly separable from the other 2.
The goal of this challenge is to create a classification model and make it
available for use by other applications. Choosing the Iris database
is due to its simplicity, since the more generic the implementation of the
availability structure, the greater the capacity for reuse for other
models.
The focus of the evaluation will not be the quality metrics of the generated model, but
rather the good practices used and tools chosen.
Your solution must receive some parameters from the user and return the
desired information in a format that is easy to process by the system.

## Tasks

For the purposes of this exercise you must carry out the following activities:
- Create a pipeline written in Python for model training and evaluation
- Develop an API in Python that uses the trained model. The API must receive 4 parameters:
  - sepal length
  - sepal width
  - petal length
  - petal width
- The API must perform the feature engineering process and return the prediction result..

The choice of technologies is free for the candidate.

## 1. Deliverables

- API Python code
- Codes must be delivered to a Git repository.
- Instructions on how to reproduce the pipeline
- Instructions on how to start the API

## 2. Rating criteria

For the test we will evaluate the following characteristics:

- Clean code
- Environmental reproducibility
- Efficiency

## Instructions

1. First you need to build the image to train the model, for this go to the root of the project and run this command:
  - docker build train/ -t challenge-train

2. Run a container from this image and mount a volume to save the resulting model:
  - docker run -v $PWD/model:/app/artifacts -p 5000:5000 challenge-train

3. Make sure a folder named "model" with a file named "model.pkl" is created

4. Now, go to another terminal and build the image for the API:
  - docker build app/ -t challenge-api

5. Run a container from this image and mount a volume to load the resulting model in the API:
  - docker run -v $PWD/model:/app/models/iris -p 8000:8000 challenge-api

6. Now in your local port 8000 is the API and in the port 5000 is the mlflow tracking server if you want to see details from the model.

7. In the API, you can use the swagger for the test in http://localhost:8000/docs.

8. There you will need to authorize to access the endpoints, for this you can use the green button **Authorize**.

9. The only user valid is the test one. 
  - username: test_user
  - password: password

10. Now you can access the other endpoints.
  - See the /models/ for all available models;
  - See /models/iris to predict in iris model;
  - In the swagger you can see the details and how are the objects.
