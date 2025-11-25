from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline 
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline 
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline 
from src.datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

class DataIngestion:

    try: 
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e 
    

STAGE_NAME = "Data Validation Stage"

class DataValidation:

    try: 
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.initiate_data_validation()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e 
    

STAGE_NAME = "Data Transformation Stage"

class Transformation:
    
    try: 
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        transformation_pipeline = DataTransformationTrainingPipeline()
        transformation_pipeline.initiate_data_transformation()
        logger.info(f">>>> *** stage {STAGE_NAME} completed SUCCESSFULLY *** <<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "Model Training  Stage"

class ModelTrainer:
    try: 
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        model_training_pipeline = ModelTrainerTrainingPipeline()
        model_training_pipeline.initiate_model_training()
        logger.info(f">>>> *** stage {STAGE_NAME} completed SUCCESSFULLY *** <<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Evaluation  Stage"

class ModelEvaluation:
    try: 
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
        model_evaluation_pipeline.initiate_model_evaluation()
        logger.info(f">>>> *** stage {STAGE_NAME} completed SUCCESSFULLY *** <<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e