"""
Author: Amisha Manga
Date: 28/02/2022
This is the coding solution to the Twitter Feed Coding Assignment

Usage:

Please ensure the correct path to the input text files are provided.

$ python TwitterFeedSimulation.py user.txt tweet.txt

For Unit Tests:

$ python TwitterFeedSimulation.py

Assumptions:

TODO

"""
import sys
import logging
from pathlib import Path
from Logger import clsLogger
from TwitterFeedProcessingMethods import clsTwitterFeedProcessingMethods
from UnitTests.UnitTests import clsUnitTesting


def vMain():
    """This is the main method of the Twitter Feed Simulation program.

    Parameters:

    Returns:
    """

    if (len(sys.argv) != 3):
        print('Please pass two command line arguments')
        print('Example:')
        print('')
        print('$ python TwitterFeedSimulation.py user.txt tweet.txt')
        print('')
        print('Run unit tests and produce report:')
        print('')

        objClsUnitTesting = clsUnitTesting()

        # If we passed in the unit-test option as an argument then run the unit tests and exit
        if (objClsUnitTesting.bMainTestMethod() is True):
            logging.info("All unit tests passed")
        else:
            logging.info("One or more unit tests failed")
        logging.info("Exit!")
        return

    # Choose a name for log file
    acLogFileName = 'Logging.log'

    # Enabled logging to console, set to  True for Debugging
    bLogToConsole = True

    # Start and configure the Logger
    objClsLogger = clsLogger()
    objClsLogger.vConfigureLogger(acLogFileName, bLogToConsole)

    objPathUserTxt = Path(sys.argv[1])
    objPathTweetTxt = Path(sys.argv[2])

    # Verify if the user.txt file exists
    if (objPathUserTxt.exists() is False):
        logging.error('File %s does not exist', sys.argv[1])
        return

    # Verify if the tweet.txt file exists
    if (objPathTweetTxt.exists() is False):
        logging.error('File %s does not exist', sys.argv[2])
        return

    # Verify the filename user.txt is correct
    if (objPathUserTxt.name != 'user.txt'):
        logging.error("The first parameter file should be called user.txt")
        return

    # Verify the filename tweet.txt is correct
    if (objPathTweetTxt.name != 'tweet.txt'):
        logging.error("The second parameter file should be called tweet.txt")
        return

    # Read the user.txt file
    acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile(sys.argv[1])

    if (not acUserFileContent):
        logging.error("user.txt file has no contents. Exit!")
        return

    # Parse user content
    (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)

    if (not lstUsers):
        logging.error("user.txt is not valid. Exit!")
        return

    # Read the tweet.txt file
    acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile(sys.argv[2])

    # If tweet.txt has no contents, process user list if valid
    if (not acTweetFileContent):
        logging.info("tweet.txt file has no contents, processing list of users")
        acDisplayFeed = clsTwitterFeedProcessingMethods.acCreateFeedFromUserList(lstUsers)

    else:
        # Parse tweet content
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        if (not lstTweets):
            logging.error("tweet.txt is not valid. Exit!")
            return

        # Create the desired twitter simulation feed
        acDisplayFeed = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

    # Display the twitter simulation feed
    print(acDisplayFeed)


if __name__ == "__main__":
    vMain()
