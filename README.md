# Diabetes Prediction Project

## Project Overview
This project aims to predict diabetes status using health indicators from a dataset. It implements a complete ML pipeline with components for data ingestion, validation, transformation, training, evaluation, and deployment using Flask for a web interface. Additionally, the project is integrated with a CI/CD pipeline and deployed on AWS using Docker.

## Key Components

### Data Ingestion
**Purpose**: Downloads the dataset from the given source and extracts necessary files for further processing.  
**Files**:
- `data_ingestion.py`: Handles downloading and extracting the dataset.  
- `dvc.yaml`: Contains the data pipeline configuration.  
**Output**: Data is stored in the `artifacts/data_ingestion/` folder.

### Data Validation
**Purpose**: Validates that the dataset contains the required columns and follows the defined schema.  
**Files**:
- `data_validation.py`: Checks if all required columns are present in the dataset.  
**Output**: Validation status is saved in `artifacts/data_validation/status.txt`.

### Data Transformation
**Purpose**: Splits the dataset into training and testing datasets.  
**Files**:
- `data_transformation.py`: Splits the dataset into training and testing sets.  
**Output**: Transformed data is saved in `artifacts/data_transformation/`.

### Model Training
**Purpose**: Trains an ElasticNet regression model on the transformed dataset.  
**Files**:
- `model_trainer.py`: Handles training and saving the model.  
**Output**: The trained model is saved as `model.joblib` in `artifacts/model_trainer/`.

### Model Evaluation
**Purpose**: Evaluates the trained model using test data.  
**Files**:
- `model_evaluation.py`: Loads the model and computes evaluation metrics such as RMSE, MAE, and R-squared.  
**Output**: Evaluation metrics are saved in `artifacts/model_evaluation/metrics.json`.

### Prediction Pipeline
**Purpose**: Processes input data and returns predictions for diabetes risk.  
**Files**:
- `prediction.py`: Loads the trained model and makes predictions.

### API Deployment
**Purpose**: Deploys the trained model as a REST API for predictions.  
**Files**:
- `app.py`: Contains Flask routes for training and prediction.  

### Notebooks
Contains Jupyter notebooks for experimentation and analysis:
- `01_data_ingestion.ipynb`
- `02_data_validation.ipynb`
- `03_data_transformation.ipynb`
- `04_model_trainer.ipynb`
- `05_model_evaluation.ipynb`
- `experiment.ipynb`
- `trials.ipynb`

## Docker Setup

The project uses Docker to containerize the application for consistent deployments and easier distribution.

- **Dockerfile**: Defines the environment and dependencies for running the application.
  
  The `Dockerfile` builds an image with the required dependencies, including Python, the required libraries, and the web application. It uses the `requirements.txt` to install dependencies and sets up the application to run on port `8080`.

  ### Building and Running Docker Container
  ```bash
  # Build the Docker image
  docker build -t diabetes-prediction .

  # Run the Docker container
  docker run -p 8080:8080 diabetes-prediction


**Note**: Make sure Docker is installed and running on your local machine

## CI/CD Deployment
The project includes a CI/CD pipeline using GitHub Actions to automate testing, building, and deployment processes on AWS.

- Continuous Integration: The CI/CD pipeline checks for code linting and runs unit tests whenever code is pushed to the repository's main branch.
- Continuous Delivery: The pipeline builds a Docker image and pushes it to Amazon ECR (Elastic Container Registry).
- Continuous Deployment: The pipeline deploys the Docker container on an AWS EC2 instance using a self-hosted runner or an ECS service.


## GitHub Actions Workflow
**CI/CD Configuration**: The .github/workflows/cicd.yaml file defines the pipeline, including stages for integration, build, push, and deployment.                                                                                   
**AWS Integration**: The pipeline is configured to authenticate with AWS using secrets (AWS_ACCESS_KEY_ID and       
**AWS_SECRET_ACCESS_KEY)** and deploys the container using Amazon ECR and ECS or an EC2 instance with Docker.

## AWS Deployment
- Amazon ECR: Used to store Docker images for deployment.
- Amazon ECS/EC2: Used to deploy the Docker containers to the cloud.

## Prerequisites
- AWS account with configured IAM roles and permissions.
- GitHub repository with required secrets set up (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, - ECR_REPOSITORY_NAME).
- Docker and AWS CLI installed locally.


## CI/CD Workflow
- Continuous Integration: Lints the code and runs unit tests on each push to the main branch.
- Build and Push Docker Image: Builds the Docker image and pushes it to Amazon ECR.
- Deploy Docker Container: Pulls the latest Docker image from ECR and deploys it on an EC2 instance or ECS service.

