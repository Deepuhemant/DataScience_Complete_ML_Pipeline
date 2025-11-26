import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model_path = Path("artifacts/model_trainer/model.joblib")
        self.model = self.load_model()
    
    def load_model(self):
        """Load the trained model"""
        try:
            model = joblib.load(self.model_path)
            return model
        except Exception as e:
            raise Exception(f"Error loading model: {str(e)}")
    
    def predict(self, data):
        """
        Make prediction on input data
        
        Args:
            data: numpy array of shape (1, 11) containing:
                  [fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                   chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density,
                   pH, sulphates, alcohol]
        
        Returns:
            prediction: Predicted wine quality score
        """
        try:
            prediction = self.model.predict(data)
            return prediction
        except Exception as e:
            raise Exception(f"Error making prediction: {str(e)}")
