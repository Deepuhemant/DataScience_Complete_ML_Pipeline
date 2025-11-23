import os
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import (DataValidationConfig)


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    
    def validate_all_columns(self) -> bool:
        """
        Validates if all required columns exist in the dataset
        """
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            # Check if all columns from data exist in schema
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w', encoding='utf-8') as f:
                        f.write(f"Column Validation Status: {validation_status}\n")
                        f.write(f"Missing column in schema: {col}\n")
                    logger.error(f"Column '{col}' not found in schema")
                    return validation_status
            
            # All columns exist
            validation_status = True
            with open(self.config.STATUS_FILE, 'w', encoding='utf-8') as f:
                f.write(f"Column Validation Status: {validation_status}\n")
            
            logger.info("All columns validated successfully")
            return validation_status
            
        except Exception as e:
            raise e


    def validate_all_dtypes(self) -> bool:
        """
        Validates if all column datatypes match the schema
        """
        try:
            validation_status = None
            
            # Read the data
            data = pd.read_csv(self.config.unzip_data_dir)
            
            # Get actual datatypes from CSV
            actual_dtypes = data.dtypes
            
            # Get expected datatypes from schema
            expected_schema = self.config.all_schema
            
            # Open file in append mode to add dtype validation results
            with open(self.config.STATUS_FILE, 'a', encoding='utf-8') as f:
                f.write(f"\n{'='*50}\n")
                f.write(f"Datatype Validation:\n")
                f.write(f"{'='*50}\n")
            
            # Compare each column's datatype
            mismatches = []
            for col in data.columns:
                actual_dtype = str(actual_dtypes[col])
                expected_dtype = str(expected_schema[col])
                
                if actual_dtype != expected_dtype:
                    mismatch_msg = f"  [X] {col}: Expected '{expected_dtype}', Got '{actual_dtype}'"
                    mismatches.append(mismatch_msg)
                    logger.warning(mismatch_msg)
            
            # Write results
            if len(mismatches) > 0:
                validation_status = False
                with open(self.config.STATUS_FILE, 'a', encoding='utf-8') as f:
                    f.write(f"Datatype Validation Status: {validation_status}\n")
                    f.write(f"Mismatches Found:\n")
                    for mismatch in mismatches:
                        f.write(f"{mismatch}\n")
                logger.error(f"Found {len(mismatches)} datatype mismatches")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, 'a', encoding='utf-8') as f:
                    f.write(f"Datatype Validation Status: {validation_status}\n")
                    f.write(f"[OK] All datatypes match the schema!\n")
                logger.info("All datatypes validated successfully")
            
            return validation_status
            
        except Exception as e:
            raise e
