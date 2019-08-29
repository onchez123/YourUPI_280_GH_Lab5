import unittest
from logger import Logger

class Target(object):
    def __init__(self, text = None):
        self.__text = text

    def set_text(self, input_text):
        self.__text = input_text

    def get_text(self):
        return self.__text

class LoggerTest(unittest.TestCase):

    def test_info(self):
        t1 = Target()
        log1 = Logger(t1.set_text)
        log1.info("Information")
        self.assertEqual("[INFO] Information", t1.get_text(), "Test failed")

    def test_error(self):
        t2 = Target()
        log2 = Logger(t2.set_text)
        log2.error("Error")
        self.assertEqual("[WARNING] Error", t2.get_text(), "Test failed")

if __name__ == '__main__':
    unittest.main()

        
