import unittest
import os
from Logger import Logger

class LoggerTest(unittest.TestCase):
    def test_init(self):
        dir = os.getcwd()
        logger = Logger(dir)
        #self.assertEqual("E://Projects//Python//Logger", logger.loc)
        return logger

    def test_Error(self):
        logger = self.test_init()
        msg = 'Testing Error function'
        logger.write('Error', msg)



if __name__ == '__main__':
    test = LoggerTest()
    test.test_Error()
