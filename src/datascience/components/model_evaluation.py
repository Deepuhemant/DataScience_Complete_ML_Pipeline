# Import required libraries
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
from src.datascience.entity.config_entity import ModelEvaluationConfig
import mlflow
from pathlib import Path
import json
from src.datascience.utils.common import save_json
import os
import dagshub

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        # Initialize DagsHub with authentication
        dagshub.init(repo_owner='DeepuHemant', 
                     repo_name='DataScience_Complete_ML_Pipeline', 
                     mlflow=True)
        
        # Alternative: Use dagshub.auth
        dagshub.auth.add_app_token(token='65e2450193707a8901e9b601e765263b90687496')  # Update with new token!
        
        # Load test data and model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # Prepare test data
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Set MLflow tracking URI
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        
        # Start MLflow run
        with mlflow.start_run():
            # Make predictions
            predicted_qualities = model.predict(test_x)

            # Calculate metrics
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            # Save metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log parameters and metrics to MLflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)
            
            print("\n" + "="*60)
            print("✅ MODEL EVALUATION COMPLETED SUCCESSFULLY!")
            print("="*60)
            print(f"📊 Metrics:")
            print(f"   RMSE: {rmse:.4f}")
            print(f"   MAE:  {mae:.4f}")
            print(f"   R2:   {r2:.4f}")
            print("="*60)
            print(f"💾 Metrics saved to: {self.config.metric_file_name}")
            print(f"🔗 View MLflow run at: https://dagshub.com/DeepuHemant/DataScience_Complete_ML_Pipeline.mlflow")
            print("="*60)
