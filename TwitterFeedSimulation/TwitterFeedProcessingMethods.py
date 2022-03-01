"""
The Twitter Feed Processing class contains methods that is responsible for handling twitter user follow relations,
tweets and the resultant output feed.

"""
import logging
from pathlib import Path
import re


class clsTwitterFeedProcessingMethods():
    """
    Contains all methods to process twitter user relations, tweets and create desired output twitter simulated feed.
    """

    @staticmethod
    def acReadFile(acFilePathPar: str):
        """ Method to read an ascii file.

            Parameters:
                acFilePathPar (str): The file path.

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
        """ Method to parse user text.

            Parameters:
                acUserContent (str): User content as in user.txt.

            Returns:
                tplUsers(dctUserRelations, lstAllUsers)
                    dctUserRelations (dictionary): {user(str): user and all users current user follows (list of strings)}.
                    example: {'Ward': ['Ward', 'Martin', 'Alan']}.
                    lstAllUsers (list): [all users alphabetically sorted (str)].

        """
        acRegexUserNameFormat = '^[a-zA-Z0-9_]+$'  # Use this regex format to test for a valid username
        dctUserRelations = {}
        lstAllUsers = []
        tplUsers = (dctUserRelations, lstAllUsers)

        # If User Content is empty
        if (not acUserContent):
            return(tplUsers)

        # Go through each line in text file
        for acLine in acUserContent.splitlines():
            acUserLine = acLine.replace(',', '').split()

            # Do some checks to confirm that the input user file is in a format we expect
            # i.e 'Each line of a well-formed user file contains a user, followed by the word 'follows' and then a comma separated list of users they follow.

            # Check that there are more than 3 arguments(i.e one user before 'follows' and atleast one user after) in each line of user.txt
            if (len(acUserLine) < 3):
                logging.error("There are not enough arguments (minimum 3 arguments required) in one of the lines of user.txt. User.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            if (acUserLine.count('follows') > 1):
                logging.error("The word 'follows' appears more than once in one of the lines of user.txt. User.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            if (acUserLine.count('follows') < 1):
                logging.error("The word 'follows' is missing in one of the lines of user.txt. User.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            if (acUserLine[1] != str("follows")):
                logging.error("The word 'follows' is not in the expected position in one of the lines of user.txt. User.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            acUserLine.remove('follows')

            # Create dictionary of users and who they follow : i.e {user : all users current user follows including current user}
            acUser = acUserLine[0]
            acUserAndRelations = acUserLine[:]
            dctUserRelations[(acUser)] = acUserAndRelations

            # Create list of all users
            lstAllUsers.append(acUserLine)

        # Flatten the List Structure into one List of All Users
        lstAllUsers = [item for sublist in lstAllUsers for item in sublist]

        # Remove Duplicate Users
        lstAllUsers = list(dict.fromkeys(lstAllUsers))

        # Check that user names are alpha-numeric with the exception of an underscore character
        for acUserName in lstAllUsers:
            if (re.match(acRegexUserNameFormat, acUserName) is None):
                logging.error("Invalid user name %s in one of the lines of user.txt. User.txt is invalid.", acUserName)
                tplUsers = ({}, [])
                return (tplUsers)

        # Sort List of Users into alphabetical order
        lstAllUsers = sorted(lstAllUsers)

        tplUsers = (dctUserRelations, lstAllUsers)

        return(tplUsers)

    @staticmethod
    def lstParseTweets(acTweetContent: str):
        """ Method to parse tweet text.

            Parameters:
                acTweetContent (str): Tweet content as in tweet.txt.

            Returns:
                lstTweets (list): List containing [user (str): tweet (str)].

        """
        lstTweets = []

        # If Tweet Content is empty
        if (not acTweetContent):
            return(lstTweets)

        for acLine in acTweetContent.splitlines():
            acLineUserAndTweet = acLine.replace('\n', '').split('> ')
            lstTweets.append(acLineUserAndTweet)

        return (lstTweets)

    @staticmethod
    def acCreateFeedFromUserRelationsAndTweets(lstUsers: list, dctUserRelations: dict, lstTweets: list):
        """ Method to produce twitter feed given the users and their tweets.

            Parameters:
                lstUsers (list): List of all users in string format, alphabetically sorted.
                dctUserRelations (dict): Dictionary of all users and the users they follow in string format.
                lstTweets (list): List of all users and what they tweeted in string format.

            Returns:
                acResultantSimulationFeed (str) : Desired Simulation Feed.

        """
        acResultantSimulationFeed = ""

        # If dictionary of user relations is empty
        if (not dctUserRelations):
            return (acResultantSimulationFeed)

        # If list of users and their tweets is empty
        if (not lstTweets):
            return (acResultantSimulationFeed)

        # If list of all users is empty
        if (not lstUsers):
            return (acResultantSimulationFeed)

        '''
        Go through alphabetically ordered list and then check if the user follows any other users
        by checking if the user matches the dictionary key. Then go through the list of users and tweets
        and if any of the users in the user relations dictionary has tweeted something, add to the resultant
        twitter simulation feed. Note: Tweeter refers to the user that has posted a tweet.
        '''

        for acCurrentUser in lstUsers:
            acResultantSimulationFeed += f'{acCurrentUser}\n'

            if acCurrentUser in dctUserRelations.keys():
                for acTweet in lstTweets:
                    acTweeter = acTweet[0]
                    if acTweeter in dctUserRelations[acCurrentUser]:
                        acResultantSimulationFeed += f'\t@{acTweeter}: {acTweet[1]}\n'

        return (acResultantSimulationFeed)
