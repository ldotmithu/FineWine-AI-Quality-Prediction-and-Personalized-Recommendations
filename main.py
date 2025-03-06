from src.Pipeline.Stages_of_Pipeline import DataIngestionPipeline,DataValidationPipeline

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
    ingestion = DataValidationPipeline()
    ingestion.main()
    logging.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e:
    raise e 