from flask import Flask, render_template, request, jsonify
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline
import subprocess
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/train", methods=["POST"])
def training():
    """Trigger model training"""
    try:
        # Run the training pipeline
        result = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True,
            timeout=600  # 10 minutes timeout
        )
        
        if result.returncode == 0:
            return jsonify({
                "status": "success",
                "message": "Model training completed successfully! ✅",
                "details": "You can now make predictions."
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Training failed ❌",
                "details": result.stderr
            }), 500
            
    except subprocess.TimeoutExpired:
        return jsonify({
            "status": "error",
            "message": "Training timeout ⏱️",
            "details": "Training took too long. Please try again."
        }), 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Training error ❌",
            "details": str(e)
        }), 500

@app.route("/predict", methods=["POST", "GET"])
def predict():
    """Handle prediction requests"""
    if request.method == "POST":
        try:
            # Get form data
            fixed_acidity = float(request.form["fixed_acidity"])
            volatile_acidity = float(request.form["volatile_acidity"])
            citric_acid = float(request.form["citric_acid"])
            residual_sugar = float(request.form["residual_sugar"])
            chlorides = float(request.form["chlorides"])
            free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
            total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
            density = float(request.form["density"])
            pH = float(request.form["pH"])
            sulphates = float(request.form["sulphates"])
            alcohol = float(request.form["alcohol"])
            
            # Create input data array
            data = [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol
            ]
            
            # Convert to numpy array and reshape
            data = np.array(data).reshape(1, -1)
            
            # Create prediction pipeline and predict
            try:
                prediction_pipeline = PredictionPipeline()
                prediction = prediction_pipeline.predict(data)
                
                # Round prediction to nearest integer
                prediction_value = round(float(prediction[0]))
                
                # Ensure prediction is within valid range (0-10)
                prediction_value = max(0, min(10, prediction_value))
                
                # Render template with prediction
                return render_template("index.html", prediction=prediction_value)
                
            except FileNotFoundError:
                return render_template("index.html", 
                                     error="Model not found! Please train the model first using the 'Start Training' button above.")
            
        except ValueError as ve:
            return render_template("index.html", 
                                 error=f"Invalid input: {str(ve)}. Please enter valid numbers.")
        except Exception as e:
            return render_template("index.html", 
                                 error=f"Prediction error: {str(e)}")
    
    # GET request - just show the form
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
