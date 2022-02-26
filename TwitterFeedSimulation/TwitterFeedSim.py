"""
Author: Amisha Manga
Date: 26/02/2022
This is the coding solution to the Twitter Feed Coding Assignment

Usage: 

TODO

Assumptions:

TODO

"""
import logging
from Logger import clsLogger

def vMain():

    # Start the Logger 
    objClsLogger = clsLogger()
    objClsLogger.vConfigureLogger()

    logging.info("Logger set up correctly!")



if __name__ == "__main__":
    vMain()