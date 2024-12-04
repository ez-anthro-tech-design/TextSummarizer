from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories

from src.textSummarizer.entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH): #path initiated before ANY module 
        self.config = read_yaml(config_path) # read the YAML file path
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
# basic setup before starting any module 
    def get_data_ingestion_config(self) -> DataIngestionConfig: # read all the configurations specified in config.yaml 
        config=self.config.data_ingestion # reading data from data_ingestion in config.yaml 
        create_directories([config.root_dir])

        data_ingestion_config=DataIngestionConfig( # return all values from DataIngestionConfig
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
