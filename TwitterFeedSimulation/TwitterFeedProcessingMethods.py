"""
The Twitter Feed Processing class contains methods that is responsible for handling twitter user follow relations,
tweets and the resultant output feed.

"""
import logging
from pathlib import Path


class clsTwitterFeedProcessingMethods():
    """
    Contains all methods to process twitter user relations, tweets and create desired output twitter simulated feed.
    """

    @staticmethod
    def acReadFile(acFilePathPar: str):
        """ Method to read an ascii file

            Parameters:
                acFilePathPar (str): The file path

            Returns:
                acFileContent (str): The contents inside the file.

        """
        acFileContent = ""

        try:
            objPathFile = Path(acFilePathPar)
            acFileContent = objPathFile.read_text(encoding='ascii')
        except Exception as E:
            logging.error(str(E))
            return("")

        return(acFileContent)

    @staticmethod
    def tplParseUsers(acUserContent: str):
        """ Method to parse user text

            Parameters:
                acUserContent (str): User content as in user.txt

            Returns:
                tplUsers(dctUserRelations, lstAllUsers)
                dctUserRelations (dictionary): {user(str): user and all users current user follows (list of strings)}
                lstAllUsers (list): [all users alphabetically sorted (str)]

        """
        dctUserRelations = {}
        lstAllUsers = []
        tplUsers = (dctUserRelations, lstAllUsers)

        return (tplUsers)

    @staticmethod
    def lstParseTweets(acTweetContent: str):
        """ Method to parse tweet text

            Parameters:
                acTweetContent (str): Tweet content as in tweet.txt

            Returns:
                lstTweets (list): List containing [user (str): tweet (str)]

        """
        lstTweets = []

        return (lstTweets)

    @staticmethod
    def acCreateFeedFromUserRelationsAndTweets(lstUsers: list, dctUserRelations: dict, lstTweets: list):
        """ Method to produce twitter feed given the users and their tweets

            Parameters:
                lstUsers (list): List of all users in string format, alphabetically sorted
                dctUserRelations (dict): Dictionary of all users and the users they follow in string format
                lstTweets (list): List of all users and what they tweeted in string format

            Returns:
                acResultantSimulationFeed (str) : Desired Simulation Feed

        """
        acResultantSimulationFeed = ""

        return (acResultantSimulationFeed)
