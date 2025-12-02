# 😻 Wine Quality Prediction - Complete ML Pipeline

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![MLflow](https://img.shields.io/badge/tracking-MLflow-0194E3.svg)](https://mlflow.org/)
[![Scikit-learn](https://img.shields.io/badge/ML-scikit--learn-F7931E.svg)](https://scikit-learn.org/)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-yellow.svg)](https://opensource.org/licenses/GPL-3.0)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

An end-to-end Machine Learning pipeline for predicting wine quality from physicochemical properties. Features modular architecture, MLflow experiment tracking, Flask web interface, and Docker deployment.

## 🌿 Overview

This project demonstrates a production-ready ML pipeline following industry best practices for predicting wine quality. It includes:
- Complete data ingestion to deployment workflow
- MLflow and DagsHub integration for experiment tracking
- Interactive Flask web UI for real-time predictions
- Docker containerization for easy deployment
- Comprehensive Jupyter notebooks for research and analysis

**Key Highlights:**
- ✅ End-to-end ML pipeline (data ingestion → evaluation → deployment)
- ✅ Modular and scalable architecture
- ✅ MLflow & DagsHub integration for experiment tracking
- ✅ Interactive web UI for predictions
- ✅ Docker support for containerized deployment
- ✅ Comprehensive research notebooks
- ✅ Production-ready code structure

## ✨ Features

### Core Pipeline Components
1. **Data Ingestion** - Automated data loading and initial processing
2. **Data Validation** - Schema validation and data quality checks
3. **Data Transformation** - Feature engineering and preprocessing
4. **Model Training** - Scikit-learn model training with hyperparameter tuning
5. **Model Evaluation** - Performance metrics tracking with MLflow

### Web Interface
- Beautiful Flask-based UI for predictions
- Train button for model retraining
- Real-time prediction form
- Interactive visualization

### Additional Features
- Experiment Tracking with MLflow integration
- Configuration Management (YAML-based configs)
- Comprehensive research notebooks
- Docker support for containerized deployment
- DagsHub integration for remote tracking

## 📁 Project Structure

```
DataScience_Complete_ML_Pipeline/
├── .github/workflows/          # CI/CD workflows
├── config/                     # Configuration files
│   ├── config.yaml             # Project configurations
│   ├── params.yaml             # Model parameters
│   └── schema.yaml             # Data schema
├── research/                   # Jupyter notebooks
│   ├── data_ingestion.ipynb
│   ├── data_validation.ipynb
│   ├── data_transformation.ipynb
│   ├── model_trainer.ipynb
│   ├── model_evaluation.ipynb
│   └── research.ipynb
├── src/datascience/            # Main source code
│   ├── components/              # Pipeline components
│   ├── config/                 # Configuration manager
│   ├── constants/              # Constants
│   ├── entity/                 # Data entities
│   ├── pipeline/               # Training & prediction
│   └── utils/                  # Utility functions
├── static/                     # Static files for web UI
├── templates/                  # HTML templates
├── mlruns/                     # MLflow tracking data
├── app.py                      # Flask web application
├── main.py                     # Training script
├── requirements.txt            # Dependencies
├── setup.py                    # Package setup
├── Dockerfile                  # Docker configuration
└── README.md                   # This file
```

## 🔧 Tech Stack

| Category | Technologies |
|----------|---------------|
| **Language** | Python 3.8+ |
| **ML Framework** | scikit-learn |
| **Experiment Tracking** | MLflow, DagsHub |
| **Web Framework** | Flask, Flask-CORS |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib |
| **Configuration** | PyYAML, python-box |
| **Development** | Jupyter Notebook |
| **Containerization** | Docker |
| **Version Control** | Git, GitHub |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git
- (Optional) Docker

### Installation

**Step 1: Clone Repository**
```bash
git clone https://github.com/Deepuhemant/DataScience_Complete_ML_Pipeline.git
cd DataScience_Complete_ML_Pipeline
```

**Step 2: Create Virtual Environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Install Package**
```bash
pip install -e .
```

## 📤 Usage Guide

### 1. Train the Model

Run the complete training pipeline:
```bash
python main.py
```

This executes all pipeline stages:
- Data Ingestion
- Data Validation
- Data Transformation
- Model Training
- Model Evaluation

### 2. Start the Web Application

Launch the Flask web interface:
```bash
python app.py
```

Access the application at: `http://localhost:8080`

### 3. Make Predictions

The web interface provides:
- **Train Button**: Trigger model training from the UI
- **Prediction Form**: Input wine properties to get quality predictions

**Input Features (11 total):**
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol Content

**Output:** Wine quality score (0-10 scale)

## 📊 ML Pipeline Workflow

### Pipeline Steps:
1. **Data Ingestion** → Load wine quality dataset
2. **Data Validation** → Validate against schema.yaml
3. **Data Transformation** → Feature engineering and preprocessing
4. **Model Training** → Train ML models with scikit-learn
5. **Model Evaluation** → Evaluate and log metrics to MLflow
6. **Deployment** → Serve via Flask web interface

## 📊 MLflow Tracking

This project uses **MLflow** integrated with **DagsHub** for comprehensive experiment tracking.

### View Experiments
```bash
mlflow ui
```

Open `http://localhost:5000` to view:
- Model parameters
- Performance metrics (RMSE, MAE, R²)
- Artifacts and models
- Experiment comparisons
- Training history

### Tracked Metrics
- **RMSE** (Root Mean Square Error)
- **MAE** (Mean Absolute Error)
- **R² Score** (Coefficient of Determination)
- **Model Parameters**
- **Hyperparameters**

## 📚 Development Workflow

For adding new features or modifications:

1. Update `config/config.yaml` with new configurations
2. Update `config/schema.yaml` for data validation rules
3. Update `config/params.yaml` for model hyperparameters
4. Update entity in `src/datascience/entity/`
5. Update configuration manager in `src/datascience/config/`
6. Update components in `src/datascience/components/`
7. Update pipeline in `src/datascience/pipeline/`
8. Update `main.py` to include new pipeline stages

## 🛣 Docker Deployment

### Build Docker Image
```bash
docker build -t wine-quality-predictor .
```

### Run Container
```bash
docker run -p 8080:8080 wine-quality-predictor
```

Access at: `http://localhost:8080`

## 📊 Model Performance

Typical performance metrics:
- **RMSE**: 0.5-0.7
- **MAE**: 0.4-0.6
- **R² Score**: 0.45-0.65

*Note: Performance varies based on hyperparameters and data split.*

## 🛡 Troubleshooting

### Common Issues

**Module not found error**
```bash
pip install -e .
```

**Port 8080 already in use**
```bash
# Change port in app.py or use:
python -m flask run --port 5000
```

**MLflow UI not loading**
```bash
# Ensure MLflow is installed:
pip install mlflow
# Then start UI:
mlflow ui
```

## 🌟 Future Enhancements

- [ ] Model ensemble techniques
- [ ] Hyperparameter optimization (Optuna, Ray Tune)
- [ ] Feature selection automation
- [ ] API endpoint for programmatic access
- [ ] Real-time model monitoring
- [ ] A/B testing framework
- [ ] Advanced visualization dashboard
- [ ] Model explainability (SHAP, LIME)
- [ ] Automated model selection
- [ ] Performance benchmarking

## 👋 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

## 📧 Support & Contact

**Author:** Deepuhemant

**Repository:** [DataScience_Complete_ML_Pipeline](https://github.com/Deepuhemant/DataScience_Complete_ML_Pipeline)

For issues or questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review logs in console output
3. Open an [issue on GitHub](https://github.com/Deepuhemant/DataScience_Complete_ML_Pipeline/issues)

## 🙏 Acknowledgments

- [Scikit-learn](https://scikit-learn.org/) for ML algorithms
- [MLflow](https://mlflow.org/) for experiment tracking
- [Flask](https://flask.palletsprojects.com/) for web framework
- [DagsHub](https://dagshub.com/) for MLflow hosting
- [Wine Quality Dataset](https://archive.ics.uci.edu/ml/datasets/wine+quality) for data

## 📌 Portfolio Note

This is a production-ready project demonstrating expertise in:
- End-to-end ML pipeline development
- MLflow experiment tracking and management
- Flask web application development
- Data validation and error handling
- Configuration management
- Docker containerization
- Professional software engineering practices
- Model evaluation and metrics tracking

---

**⭐ If you find this project helpful, please give it a star! ⭐**

**Made with ❤️ using Scikit-learn, MLflow, and Flask**

*Last updated: 2025*
