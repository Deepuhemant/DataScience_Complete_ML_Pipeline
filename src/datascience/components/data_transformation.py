import os
from src.datascience import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from src.datascience.entity.config_entity import ( DataTransformationConfig)

class DataTransformation:
    def __init__(self, config : DataTransformationConfig):
        self.config = config

## You can add different different data transformation techniques such as standardscaler, tsne and many more


    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        # split the data into training and testing sets
        train , test = train_test_split(data, test_size=0.20)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)        