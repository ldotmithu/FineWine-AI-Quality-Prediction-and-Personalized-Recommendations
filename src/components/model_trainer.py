from src.Config.config_entity import ModelTrainerConfig
from src import logging
from sklearn.ensemble import RandomForestClassifier
import numpy as np 
from src.Utility.common import Create_Folder,Read_Yaml
from src.constant.constant_config import *
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import joblib,os


class ModelTrainer:
    def __init__(self):
        self.trainer = ModelTrainerConfig()
        self.perams = Read_Yaml(PARAMS_PATH)['Model']
            
        Create_Folder(self.trainer.root_dir)
    
    def initiate_model_training(self):
        train_data = np.load(self.trainer.train_data_path)
        
        train_data_input_feature = train_data[:,:-1]
        train_data_target_feature = train_data[:,-1] 
          
    
        rfc = RandomForestClassifier(n_estimators= self.perams.get('n_estimators'),
                                     max_features = self.perams.get('max_features'),
                                     max_depth = self.perams.get('max_depth'))
        
        rfc.fit(train_data_input_feature,train_data_target_feature)
        print(rfc.score(train_data_input_feature,train_data_target_feature))
        
        joblib.dump(rfc,os.path.join(self.trainer.root_dir,self.trainer.model_path))
        logging.info("save the model.pkl")       