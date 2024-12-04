from dataclasses import dataclass
from pathlib import Path

# Creating fields to extract the zipfile, unzip the zipfile, and store it in some paths 
@dataclass # 
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path 