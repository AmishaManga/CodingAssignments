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
            (bool): Flag indicating if the tests passed

        """
        bAllTestsPassed = bool(True)
        acTestReport = ""

        tplTestResult = self.tplTestAssert()
        bAllTestsPassed &= tplTestResult[0]
        acTestReport += tplTestResult[1]

        objDatetime = datetime.datetime.now()
        acTestReport = str("\n")
        acTestReport += str("Module: Twitter Feed\n")
        acTestReport += str("Date: %s\n" % (objDatetime.strftime("%Y-%m-%d %H:%M:%S")))
        acTestReport += str("\n")
        acTestReport += str("****** Running Unit Tests ******\n")
        acTestReport += str("\n")

        return(bAllTestsPassed)

    def tplTestAssert(self) -> bool:
        """ This is a public static method which does some autogen tests.

        Args:

        Returns:
            tuple:
              * (bool) Boolean value which indicates if the method was successful or not.
              * (str) String which contains test report output as text

        Raises:
            Raises no exceptions
        """
        acTestReportOutput = str("")
        bAllTestPassed = bool(True)
        tplReturn = (bAllTestPassed, acTestReportOutput)

        tplReturn = (bAllTestPassed, acTestReportOutput)
        return(tplReturn)
