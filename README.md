# Diabetes Prediction Project

## Project Overview
This project aims to predict diabetes status using health indicators from a dataset. It implements a complete ML pipeline with components for data ingestion, validation, transformation, training, evaluation, and deployment using Flask for a web interface.

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

## Project Structure

- `.github/workflows/cicd.yaml`: GitHub Actions configuration for CI/CD.
- `artifacts/`: Folder containing data ingestion, transformation, and model-related files.
- `config/`: Contains the YAML configuration files (`config.yaml`, `params.yaml`, `schema.yaml`).
- `src/ML/`: Main source code containing the components and pipeline.
- `static/`: Contains static assets like CSS, JavaScript, and images.
- `templates/`: Contains HTML templates for the web interface.
- `app.py`: Flask application file.
- `main.py`: Script to execute the entire training pipeline.
- `requirements.txt`: Python dependencies.

## Installation

### Prerequisites
- Python 3.8+
- Docker (if you want to use Docker)
- AWS CLI and AWS account (for cloud-based deployments)

### Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction.git
   cd diabetes-prediction
