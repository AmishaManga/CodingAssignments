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
        acTestReport += str("Module: Twitter Feed\n")
        acTestReport += str("Date: %s\n" % (objDatetime.strftime("%Y-%m-%d %H:%M:%S")))
        acTestReport += str("\n")
        acTestReport += str("****** Running Unit Tests ******\n")
        acTestReport += str("\n")

        tplTestResult = self.tplTestAssert()
        bAllTestsPassed &= tplTestResult[0]
        acTestReport += tplTestResult[1]

        if (bAllTestsPassed is True):
            logging.info("All unit test passed")
        else:
            logging.info("One or more unit test failed")

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
        Unit Test 001 : Expected Behavior with provided input
        '''
        acTestReportOutput += "Unit Test 001 : [Expected Behaviour] (Provided inputs)"

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
            acTestReportOutput += "\t\t\t\tPASS ---- with feedback returned: 'Success'\n"
        except Exception as E:
            bUnitTestReturn = False
            acTestReportOutput += "\t\t\t\tFAILED ---- with feedback returned: 'Failed'\n"

        bAllTestsPassed &= bUnitTestReturn

        tplReturn = (bAllTestsPassed, acTestReportOutput)

        return(tplReturn)
