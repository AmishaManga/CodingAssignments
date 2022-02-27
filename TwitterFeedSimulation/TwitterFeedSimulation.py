"""
Author: Amisha Manga
Date: 28/02/2022
This is the coding solution to the Twitter Feed Coding Assignment

Usage:

Please ensure the correct path to the input text files are provided.

$ python TwitterFeedSimulation.py user.txt tweet.txt

Assumptions:

TODO

"""
import sys
import logging
from pathlib import Path
from Logger import clsLogger


def vMain():
    """
    This is the main method of the Twitter Feed Simulation program.

    Parameters:

    Returns:
    """

    # Start and configure the Logger
    objClsLogger = clsLogger()
    objClsLogger.vConfigureLogger()

    if (len(sys.argv) != 3):
        print('Please pass two command line arguments')
        print('Example:')
        print('')
        print('$ python TwitterFeedSimulation.py user.txt tweet.txt')
        print('')
        return

    objPathUserTxt = Path(sys.argv[1])
    objPathTweetTxt = Path(sys.argv[2])

    # Verify if the file exists
    if (objPathUserTxt.exists() is False):
        logging.error('File %s does not exist', sys.argv[1])
        return

    # Verify if the file exists
    if (objPathTweetTxt.exists() is False):
        logging.error('File %s does not exist', sys.argv[2])
        return

    # Verify the filename is correct
    if (objPathUserTxt.name != 'user.txt'):
        logging.error("The first parameter file should be called user.txt")
        return

    # Verify the filename is correct
    if (objPathTweetTxt.name != 'tweet.txt'):
        logging.error("The second parameter file should be called tweet.txt")
        return



if __name__ == "__main__":
    vMain()