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
from TwitterFeedProcessingMethods import clsTwitterFeedProcessingMethods


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

    # Parse user content
    lstUsers, dctUserRelations = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)

    if (not lstUsers):
        logging.error("No users. Exit!")
        return

    # Read the tweet.txt file
    acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile(sys.argv[2])

    # Parse tweet content
    lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

    if (not lstTweets):
        logging.error("No tweets. Exit!")
        return

    # Create the desired twitter simulation feed
    acDisplayFeed = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

    # Display the twitter simulation feed
    print(acDisplayFeed)


if __name__ == "__main__":
    vMain()