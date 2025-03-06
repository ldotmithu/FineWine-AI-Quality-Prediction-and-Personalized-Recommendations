from src.Pipeline.Stages_of_Pipeline import (DataIngestionPipeline,DataValidationPipeline,DataTransformPipeline,
                                             ModelTrainPipeline)

from src import logging

try:
    logging.info(">>>>>>Data Ingestion>>>>>>>")
    ingestion = DataIngestionPipeline()
    ingestion.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 

try:
    logging.info(">>>>>>Data Valiadtion>>>>>>>")
    validation = DataValidationPipeline()
    validation.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 

try:
    logging.info(">>>>>>Data Transform>>>>>>>")
    transform = DataTransformPipeline()
    transform.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 

try:
    logging.info(">>>>>>Model Trainer >>>>>>>")
    trainer = ModelTrainPipeline()
    trainer.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 