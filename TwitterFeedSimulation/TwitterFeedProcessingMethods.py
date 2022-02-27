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
                    example: {'Ward': ['Ward', 'Martin', 'Alan']}
                lstAllUsers (list): [all users alphabetically sorted (str)]

        """
        dctUserRelations = {}
        lstAllUsers = []    
        tplUsers = (dctUserRelations, lstAllUsers)

        # If User Content is empty
        if (not acUserContent):
            return(tplUsers)

        # Go through each line in text file
        for acLine in acUserContent.splitlines():
            acUserLine = acLine.replace(',', '').split()
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

        # Sort List of Users into alphabetical order
        lstAllUsers = sorted(lstAllUsers)

        return(dctUserRelations, lstAllUsers)

    @staticmethod
    def lstParseTweets(acTweetContent: str):
        """ Method to parse tweet text

            Parameters:
                acTweetContent (str): Tweet content as in tweet.txt

            Returns:
                lstTweets (list): List containing [user (str): tweet (str)]

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
        """ Method to produce twitter feed given the users and their tweets

            Parameters:
                lstUsers (list): List of all users in string format, alphabetically sorted
                dctUserRelations (dict): Dictionary of all users and the users they follow in string format
                lstTweets (list): List of all users and what they tweeted in string format

            Returns:
                acResultantSimulationFeed (str) : Desired Simulation Feed

        """
        acResultantSimulationFeed = ""

        for acUser in lstUsers:
            print(acUser)
            # is user in dictionary key:
            if acUser in dctUserRelations.keys():
                for acTweet in lstTweets:
                    acTweeter = acTweet[0]
                    # if user in list of users
                    if acTweeter in dctUserRelations[acUser]:
                        print(acTweet)

        return (acResultantSimulationFeed)
