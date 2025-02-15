import inspect
import logging
import os

import pytest


@pytest.mark.usefixtures("setup_teardown")
class Base:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        current_folder = os.path.dirname(os.path.abspath(__file__))
        log_path = os.path.join(current_folder, "../", 'logs')
        # Check whether the specified path exists or not
        isExist = os.path.exists(log_path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(log_path)
            print("logs directory is created!")
            # log_file = open("logfile.log", "w+")
        final_log_path = os.path.join(current_folder, "../", 'logs', 'logfile.log')
        filehandler = logging.FileHandler(final_log_path)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger


