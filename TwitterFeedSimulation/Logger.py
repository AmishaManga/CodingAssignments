"""
The Logger is responsible for managing the logging. Detailed and thorough levels of logging is very important when debugging the program,
especially if it is to be deployed on a production system. 

"""

import logging
from logging.handlers import RotatingFileHandler
import time

class clsLogger():
    """
    Logger Class
    """
    def __init__(self):
        self.objLogger = None
        self.objLogFormatter = None
        self.objLoggingRotatingFileHandler = None

        # This log format follows the logging standard
        # Insert the module name in its correct place
        self.acLoggingFormat = "%(asctime)s,%(msecs)03d,%(levelname)s,%(filename)s,%(lineno)d,%(funcName)s,%(message)s"
        self.acLoggingDateFormat = "%Y,%m,%d,%H,%M,%S"
        
    def vConfigureLogger(self):
        """ This function which configures the Log Manager

        Parameters:
        TODO
            acFileName (str) : Name of Log file

        Returns:
            None
        """

        # Get the logger instance and set level to debug
        self.objLogger = logging.getLogger()  
        self.objLogger.setLevel(logging.DEBUG)

        self.objLogFormatter = logging.Formatter(self.acLoggingFormat, self.acLoggingDateFormat)

        # Set up the logger to use UTC time instead of local time - this is to follow the logging standard
        #logging.Formatter.converter = time.gmtime

        # When we log to file
        self.objLoggingRotatingFileHandler = logging.handlers.RotatingFileHandler(filename="logging.log")
        self.objLoggingRotatingFileHandler.setLevel(logging.DEBUG)
        self.objLoggingRotatingFileHandler.setFormatter(self.objLogFormatter)
        self.objLogger.addHandler(self.objLoggingRotatingFileHandler)

        return
