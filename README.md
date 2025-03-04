# house-price-prediction-model
MLOps project for house price prediction

# MLOps Pipeline for House Price Prediction

This project demonstrates an MLOps pipeline for a house price prediction model using **Linear Regression**. The pipeline involves model training, deployment, containerization, orchestration, CI/CD automation, and monitoring. The project uses the following tech stack:

- **Machine Learning**: Python, Scikit-learn, Pandas
- **Model Deployment**: Flask API
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus, Grafana

## Project Overview

This project builds an MLOps pipeline to predict house prices based on features like square footage, number of bedrooms, and more. The pipeline covers the following steps:
1. **Data Preprocessing and Model Training** using Python and Scikit-learn.
2. **Model Deployment** via Flask API.
3. **Containerization** using Docker.
4. **Kubernetes Deployment** for scalability.
5. **CI/CD** with GitHub Actions for automated builds and deployments.
6. **Monitoring** with Prometheus and Grafana.

## Folder Structure

## Input

To get a prediction from the model, send a POST request to the /predict endpoint with a JSON payload containing the features.
Example:

curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"features": [2100, 3, 2]}'

Where:
features is an array representing the input features (e.g., square footage, number of bedrooms, number of bathrooms).

## Output

The response will contain the predicted house price.
{
  "predicted_price": 350000.0
}
