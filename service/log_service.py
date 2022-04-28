"""This functions will handle the log of the system"""
import logging
from constants import C_LOG_FILE_NAME, C_LOG_DATE_MASK
import datetime

# TODO create a page to handle the log file
def log(msg):
    logging.basicConfig(filename=C_LOG_FILE_NAME+"_" + C_LOG_DATE_MASK.format(datetime.datetime.now()) + ".log",
                        format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    logging.log(level=logging.INFO, msg=msg)


def log_database(msg):
    logging.basicConfig(filename=C_LOG_FILE_NAME+"_" + C_LOG_DATE_MASK.format(datetime.datetime.now()) + ".log",
                        format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S',
                        level=logging.INFO)
    logging.log(level=logging.INFO, msg=msg)

