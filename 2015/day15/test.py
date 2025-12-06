import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file1 = read_file("inputs/test1.txt", __file__)

    def testPart1(self):
        self.assertEqual(13882464, highest_scoring_cookie(self.input_file))

    def testPart2(self):
        self.assertEqual(11171160, highest_scoring_cookie(self.input_file, True))

    def testPart1Example1(self):
        self.assertEqual(62842880, highest_scoring_cookie(self.test_file1))

    def testPart2Example1(self):
        self.assertEqual(57600000, highest_scoring_cookie(self.test_file1, True))


if __name__ == "__main__":
    unittest.main()
