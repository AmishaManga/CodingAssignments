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

        Do some checks to confirm that the input user file is in a format we expect
        i.e 'Each line of a well-formed user file contains a user, followed by the word 'follows' and then a comma separated list of users they follow.'

        e.g. Jane follows John, Doe and Jack

            Parameters:
                acUserContent (str): User content as in user.txt.

            Returns:
                tplUsers(dctUserRelations, lstAllUsers)
                    dctUserRelations (dictionary): {user(str): user and all users current user follows (list of strings)}.
                        example: {'Jane': ['Jane', 'John', 'Doe', 'Jack']}.
                    lstAllUsers (list): [all users alphabetically sorted (str)].
                        example: ['Doe', 'Jack', 'Jane', 'John']

        """
        acRegexUserNameFormat = '^[a-zA-Z0-9_]+$'  # Use this regex format to test for a valid username
        dctUserRelations = {}
        lstAllUsers = []
        tplUsers = (dctUserRelations, lstAllUsers)

        # If User Content is empty
        if (not acUserContent):
            return(tplUsers)

        # Go through each line in user file
        for acLine in acUserContent.splitlines():
            intCommaCount = int(acLine.count(','))
            lstUserLine = acLine.replace(',', '').split()

            # Check that there are more than 3 parameters(i.e one user before 'follows' and atleast one user after) in each line of user.txt
            if (len(lstUserLine) < 3):
                logging.error("There are not enough parameters (minimum 3 parameters required) in one of the lines of user.txt. user.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            # Check that the word 'follows' does not appear more than once in each line of user.txt
            if (lstUserLine.count('follows') > 1):
                logging.error("The word 'follows' appears more than once in one of the lines of user.txt. user.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            # Check that the word follows appears once in each line of user.txt
            if (lstUserLine.count('follows') < 1):
                logging.error("The word 'follows' is missing in one of the lines of user.txt. user.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            # Check that the word follows appears where we expect, i.e one whitespace after first listed user in each line of user.txt
            if (lstUserLine[1] != str("follows")):
                logging.error("The word 'follows' is not in the expected position in one of the lines of user.txt. user.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            lstUserLine.remove('follows')

            if (len(lstUserLine) != (intCommaCount + 2)):
                logging.error("The list of users after the word 'follows' is not comma seperated in one of the lines of user.txt. user.txt is invalid.")
                tplUsers = ({}, [])
                return (tplUsers)

            # Create dictionary of users and who they follow : i.e {user : all users current user follows including current user}
            acUser = lstUserLine[0]
            acUserAndRelations = lstUserLine[:]
            dctUserRelations[(acUser)] = acUserAndRelations

            # Create list of all users
            lstAllUsers.append(lstUserLine)

        # Flatten the List Structure into one List of All Users
        lstAllUsers = [item for sublist in lstAllUsers for item in sublist]

        # Remove Duplicate Users
        lstAllUsers = list(dict.fromkeys(lstAllUsers))

        # Check that user names are alpha-numeric with the exception of an underscore character
        for acUserName in lstAllUsers:
            if (re.match(acRegexUserNameFormat, acUserName) is None):
                logging.error("Invalid user name '%s' in one of the lines of user.txt. user.txt is invalid.", acUserName)
                tplUsers = ({}, [])
                return (tplUsers)

        # Sort List of Users into alphabetical order
        lstAllUsers = sorted(lstAllUsers)

        tplUsers = (dctUserRelations, lstAllUsers)

        return(tplUsers)

    @staticmethod
    def lstParseTweets(acTweetContent: str):
        """ Method to parse tweet text.

        Do some checks to confirm that the input tweet file is in a format we expect
        i.e 'Lines of the tweet file contain a user, followed by greater than, space and then a tweet that may be at most 140 characters in length.'

        e.g. Jane> I love sunflowers.

            Parameters:
                acTweetContent (str): Tweet content as in tweet.txt.

            Returns:
                lstTweets (list): List containing [user (str): tweet (str)].
                    example: ['Jane', 'I love sunflowers.']

        """
        lstTweets = []
        acRegexUserNameFormat = '^[a-zA-Z0-9_]+$'  # Use this regex format to test for a valid username

        # If Tweet Content is empty
        if (not acTweetContent):
            return(lstTweets)

        # Go through each line in tweet file
        for acLine in acTweetContent.splitlines():
            # TODO is there even a > in the string
            intCountGreaterThanOccurance = acLine.count('>')
            lstLineUserAndTweet = acLine.replace('\n', '').split('> ')

            # Check that there is one user parameter and one tweet parameter
            if (len(lstLineUserAndTweet) < 2):
                logging.error("Incorrect number of parameters in one of the lines of tweet.txt. tweet.txt is invalid.")
                lstTweets = []
                return(lstTweets)

            acTweeter = lstLineUserAndTweet[0]
            acTweet = lstLineUserAndTweet[1]

            # Check that user name is alpha-numeric with the exception of an underscore character
            if (re.match(acRegexUserNameFormat, acTweeter) is None):
                logging.error("Invalid user name '%s' in one of the lines of tweet.txt. tweet.txt is invalid.", acTweeter)
                lstTweets = []
                return(lstTweets)

            # Check that the length of the characters in the tweet is not more than 140 characters
            if (len(acTweet) > 140):
                logging.error("The length of the tweet is greater than 140 characters in one of the lines of tweet.txt. tweet.txt is invalid.")
                lstTweets = []
                return(lstTweets)

            lstTweets.append(lstLineUserAndTweet)

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
