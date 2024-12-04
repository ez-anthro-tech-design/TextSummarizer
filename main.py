from h11 import Data
from src.textSummarizer.logging import logger 
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.components import data_ingestion



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e 
