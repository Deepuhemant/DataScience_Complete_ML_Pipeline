from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_validation import DataValidation
from src.datascience import logger


STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            
            # Step 1: Validate column names
            column_status = data_validation.validate_all_columns()  # ← First validation
            
            # Step 2: Validate datatypes
            dtype_status = data_validation.validate_all_dtypes()  # ← HERE! Second validation
            
            # Overall validation
            if column_status and dtype_status:
                print("🎉 ALL VALIDATIONS PASSED! 🎉")
            else:
                print("⚠️ SOME VALIDATIONS FAILED")
                
        except Exception as e:
            raise e



if __name__ == "__main__":
    try: 
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e