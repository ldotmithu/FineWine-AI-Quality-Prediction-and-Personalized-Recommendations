import os 
from src  import logging

def Create_Folder(path):
    try:
        logging.info(f"{path}folder created")
        os.makedirs(path,exist_ok=True)
    except Exception as e:
        raise e     
    