import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) -> tuple[str, str]:
        logging.info("Entered the data ingestion method/component")
        try:
            project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            data_path = os.path.join(project_root, "notebook", "data", "stud.csv")

            logging.info(f"Reading dataset from: {data_path}")
            df = pd.read_csv(data_path)
            logging.info(f"Dataset shape: {df.shape}")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at: {self.ingestion_config.raw_data_path}")

            logging.info("Performing train-test split")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f"Train data saved at: {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved at: {self.ingestion_config.test_data_path}")

            logging.info("Data ingestion completed successfully")
            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as ex:
            raise CustomException(ex, sys)
