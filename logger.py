import logging
from config.settings import LOGGING_FILENAME, LOGGING_LEVEL

def get_logger(name):
    logging.basicConfig(filename=LOGGING_FILENAME, filemode='a', level=LOGGING_LEVEL)
    return logging.getLogger(name)
