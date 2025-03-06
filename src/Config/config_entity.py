import os 
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir:Path = "artifacts/data_ingestion"
    URL:str = "https://github.com/ldotmithu/Dataset/raw/refs/heads/main/winequality-red.zip"
    local_data_path:Path = "artifacts/data_ingestion/data.zip"
    unzip_dir:Path = "artifacts/data_ingestion"