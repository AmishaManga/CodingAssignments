"""
The Unit Testing class is responsible for all unit tests performed on the twitter simulation feed program.

"""
import unittest
import datetime
import logging
import sys
sys.path.append("../")
from Logger import clsLogger
from TwitterFeedProcessingMethods import clsTwitterFeedProcessingMethods


class clsUnitTesting(unittest.TestCase):
    """ This is the unit test class responsible for handling unit tests for the twitter simulation feed program.
    """
    def __init__(self):
        super(clsUnitTesting, self).__init__()
        # Choose a name for log file
        self.acUnitTestLogFileName = 'UnitTestReport.log'

        # Enabled logging to console
        self.bLogToConsole = True

        # Start and configure the Logger
        self.objUnitTestLogger = clsLogger()
        self.objUnitTestLogger.vConfigureLogger(self.acUnitTestLogFileName, self.bLogToConsole)

    def bMainTestMethod(self):
        """ This is the main testing method.

        Parameters:

        Returns:
            bAllTestsPassed (bool): Flag indicating if the tests passed.

        """
        bAllTestsPassed = bool(True)
        acTestReport = ""

        objDatetime = datetime.datetime.now()
        acTestReport = str("\n\n")
        acTestReport += str("Module: Twitter Simulation Feed\n")
        acTestReport += str("Date: %s\n" % (objDatetime.strftime("%Y-%m-%d %H:%M:%S")))
        acTestReport += str("\n")
        acTestReport += str("****** Running Unit Tests ******\n")
        acTestReport += str("\n")

        tplTestResult = self.tplTestAssert()
        bAllTestsPassed &= tplTestResult[0]
        acTestReport += tplTestResult[1]

        if (bAllTestsPassed is True):
            logging.info("All unit tests passed")
        else:
            logging.info("One or more unit tests failed")

        acTestReport += "\n"

        logging.info(acTestReport)

        return(bAllTestsPassed)

    def tplTestAssert(self) -> bool:
        """ This is a method which does some unit tests.

        Parameters:

        Returns:
            tplReturn (tpl): (bAllTestsPassed, acTestReportOutput)
                bAllTestsPassed (bool): Boolean value which indicates if the method was successful or not.
                acTestReportOutput (str): String which contains test report output as text

        """
        acTestReportOutput = str("")
        bAllTestsPassed = bool(True)
        bUnitTestReturn = bool(False)
        tplReturn = (bAllTestsPassed, acTestReportOutput)

        '''
        ====================================================================================================
        Unit Test 001 : Expected Behavior with provided input
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 001 : [Valid Input]   [Provided inputs]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/001/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/001/tweet.txt')

        acCorrectResult = '''Alan
\t@Alan: If you have a procedure with 10 parameters, you probably missed some.
\t@Alan: Random numbers should not be generated with a method chosen at random.
Martin
Ward
\t@Alan: If you have a procedure with 10 parameters, you probably missed some.
\t@Ward: There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.
\t@Alan: Random numbers should not be generated with a method chosen at random.
'''

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 002 : Empty input files
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 002 : [Invalid Input] [Empty input files]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/002/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/002/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 003 : No newline character between lines, and 'follows' appears multiple times in user.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 003 : [Invalid Input] [user.txt: No newline, 'follows' appears multiple times]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/003/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/003/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 004 : The word 'follows' is absent in one of the lines in user.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 004 : [Invalid Input] [user.txt: Missing 'follows']"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/004/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/004/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 005 : Extra user before the word 'follows' in one of the lines in user.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 005 : [Invalid Input] [user.txt: Extra user before 'follows']"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/005/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/005/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 006 : No user,users after the word 'follows' in one of the lines in user.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 006 : [Invalid Input] [user.txt: No user after 'follows']"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/006/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/006/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 007 : Non-alpha numeric characters in usernames in user.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 007 : [Invalid Input] [user.txt: Non-alphanumeric chars in username]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/007/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/007/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 008 : Usernames with underscores and numbers
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 008 : [Valid Input]   [user.txt: Underscores and numbers in username]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/008/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/008/tweet.txt')

        acCorrectResult = '''Alan
\t@Alan: If you have a procedure with 10 parameters, you probably missed some.
\t@Alan: Random numbers should not be generated with a method chosen at random.
Martin_01
Ward
\t@Alan: If you have a procedure with 10 parameters, you probably missed some.
\t@Ward: There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.
\t@Alan: Random numbers should not be generated with a method chosen at random.
'''
        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 009 : Tweet post longer than 140 characters
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 009 : [Invalid Input] [tweet.txt:  Tweet Post > 140 chars]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/009/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/009/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 010 : More than one user before '>'
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 010 : [Invalid Input] [tweet.txt: More than 1 user, invalid username]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/010/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/010/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 011 : List of tweets but no users
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 011 : [Invalid Input] [Tweets but no users in users.txt]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/011/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/011/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 012 : List of users but no tweets
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 012 : [Invalid Input] [Users but no tweets in tweets.txt]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/012/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/012/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 013 : Non-ascii character in tweets.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 013 : [Invalid Input] [tweets.txt: Non-ascii characters]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/013/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/013/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 014: Users after the word 'follows' are not comma seperated in one of the lines in user.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 014 : [Invalid Input] [user.txt: User list not comma seperated]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/014/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/014/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 015: Missing '>' in tweet.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 015 : [Invalid Input] [tweet.txt: Missing '>']"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/015/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/015/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 016: More than 1 '>' in line in tweet.txt
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 016 : [Invalid Input] [tweet.txt: More than 1 '>' in line]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/016/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/016/tweet.txt')

        acCorrectResult = ""

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 017: Users in tweet.txt which are not in user.txt are not processed. Also handling whitespaces
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 017 : [Valid Input]   [Users in tweet.txt not in user.txt, whitespaces]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/017/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/017/tweet.txt')

        acCorrectResult = '''Alan
\t@Alan:           lots of spaces   you probably missed some.
\t@Alan: Random numbers should not be generated with a method chosen at random.
Martin
Ward
\t@Alan:           lots of spaces   you probably missed some.
\t@Ward: There are only two hard things in Computer Science: cache invalidation, naming things and off-by-1 errors.
\t@Alan: Random numbers should not be generated with a method chosen at random.
'''

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        '''
        ====================================================================================================
        Unit Test 018: Empty tweet.txt file, valid user.txt file
        ====================================================================================================
        '''
        acTestReportOutput += "Unit Test 018 : [Valid Input]   [Valid users.txt file, Empty tweet.txt file]"

        acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/018/user.txt')
        acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/018/tweet.txt')

        acCorrectResult = '''Alan
Martin
Ward
'''

        (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserList(lstUsers)

        try:
            self.assertEqual(acProducedResult, acCorrectResult)
            bUnitTestReturn = True
            acTestReportOutput += "\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        if (bAllTestsPassed is True):
            logging.info("All unit tests passed")
        else:
            logging.info("One or more unit tests failed")

        tplReturn = (bAllTestsPassed, acTestReportOutput)

        return(tplReturn)
