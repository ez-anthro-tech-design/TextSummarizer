import os
import urllib.request as request 
import zipfile 
from src.textSummarizer.logging import logger 

from src.textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 
    
    def download_file(self):  # Download the file 
        if not os.path.exists(self.config.local_data_file):  # If the file does not exist, retrieve it from the URL 
            try:
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file,
                )
                logger.info("File is downloaded successfully.")
            except Exception as e:
                logger.error(f"Error downloading the file: {e}")
        else:
            logger.info("File already exists.")
    
    def extract_zip_file(self):  # Unzip the file
        """
        Extracts the zip file into the data directory.
        Function returns None.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file to {unzip_path}.")
        except zipfile.BadZipFile:
            logger.error(f"Error: The file {self.config.local_data_file} is not a valid ZIP file.")
        except FileNotFoundError:
            logger.error(f"Error: The file {self.config.local_data_file} was not found.")
        except Exception as e:
            logger.error(f"An error occurred while extracting the zip file: {e}")