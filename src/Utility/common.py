from pathlib import Path
from src import logging
import os 
import yaml
import numpy as np 
import json

def Create_Folder(file_path):
    try:
        os.makedirs(file_path,exist_ok=True)
        logging.info(f"{file_path} Created")
    except  Exception as e:
        raise e     
    
def Read_Yaml(File_path):
    try:
        with open(File_path,'r') as f:
            file= yaml.safe_load(f)
            logging.info(f"{File_path} Read the yaml")
            return file
            
    except Exception as e:
        raise e 
        
def check_xls_occur(dir_path):
    files = os.listdir(dir_path)
    csv_file = [file for file in files if file.endswith(".csv")] 
    if len(csv_file) == 1:
            return csv_file[0]
    elif len(csv_file) == 0:
        logging.error("Don't have any csv files")
        return None
    else:
        logging.error("Multipule csv files are there")
        return None  
    
def save_object(file_path,obj):
    try:
        with open(file_path,'w') as f:
            metrics =json.dump(obj,f)      
            logging.info(f'save the {file_path}')
            return metrics
    except Exception as e:
        raise e      
    