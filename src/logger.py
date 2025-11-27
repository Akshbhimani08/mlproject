# src/logger.py
import logging
import logging.handlers
import os
import sys
from datetime import datetime
from pathlib import Path

# path relative to project root
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / LOG_FILE_NAME

def get_logger():
    """
    Return a configured logger instance. Use this in modules like:
        from src.logger import logger
        logger.info("...")
    """
    logging.basicConfig(
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger("ml_project")

# Create module-level logger for convenient import
logger = get_logger()

if __name__ == "__main__":
    from src.exception import CustomException
    try:
        a = 1 / 0
    except Exception as e:
        # log the original exception with traceback
        logging.error("Divide by zero error", exc_info=True)
        # raise an instance of CustomException with the original exception and sys
        raise CustomException(e,sys)

