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

    # Choose a name for log file
    acUnitTestLogFileName = 'UnitTestReport.log'

    # Start and configure the Logger
    objUnitTestLogger = clsLogger()
    objUnitTestLogger.vConfigureLogger(acUnitTestLogFileName)

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
        acTestReportOutput += "Unit Test 003 : [Invalid Input] [User.txt: No newline, 'follows' appears multiple times]"

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
        acTestReportOutput += "Unit Test 004 : [Invalid Input] [User.txt: Missing 'follows']"

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
        acTestReportOutput += "Unit Test 005 : [Invalid Input] [User.txt: Extra user before 'follows']"

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
        acTestReportOutput += "Unit Test 006 : [Invalid Input] [User.txt: No user after 'follows']"

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
        acTestReportOutput += "Unit Test 007 : [Invalid Input] [User.txt: Non-alphanumeric chars in username]"

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
        acTestReportOutput += "Unit Test 008 : [Valid Input] [User.txt: Underscores and numbers in username]"

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
        acTestReportOutput += "Unit Test 009 : [Invalid Input] [Tweet.txt:  Tweet Post > 140 chars]"

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
        acTestReportOutput += "Unit Test 010 : [Invalid Input] [Tweet.txt: More than 1 user, invalid username]"

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

        if (bAllTestsPassed is True):
            logging.info("All unit test passed")
        else:
            logging.info("One or more unit tests failed")

        tplReturn = (bAllTestsPassed, acTestReportOutput)

        return(tplReturn)
 
        # '''
        # ====================================================================================================
        # Unit Test : Users after the word 'follows' are not comma seperated in one of the lines in user.txt TODO
        # ====================================================================================================
        # '''
        # acTestReportOutput += "Unit Test : [Invalid Input] [User.txt: User list not comma seperated]"

        # acUserFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/TODO_001/user.txt')
        # acTweetFileContent = clsTwitterFeedProcessingMethods.acReadFile('./UnitTests/TODO_001/tweet.txt')

        # acCorrectResult = ""

        # (dctUserRelations, lstUsers) = clsTwitterFeedProcessingMethods.tplParseUsers(acUserFileContent)
        # lstTweets = clsTwitterFeedProcessingMethods.lstParseTweets(acTweetFileContent)

        # acProducedResult = clsTwitterFeedProcessingMethods.acCreateFeedFromUserRelationsAndTweets(lstUsers, dctUserRelations, lstTweets)

        # try:
        #     self.assertEqual(acProducedResult, acCorrectResult)
        #     bUnitTestReturn = True
        #     acTestReportOutput += "\t\t\tPASS ---- with feedback returned: 'Success'\n"
        # except Exception as E:
        #     bUnitTestReturn = False
        #     acTestReportOutput += "\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        # bAllTestsPassed &= bUnitTestReturn
