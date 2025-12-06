import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(776160, find_lowest_house_number(self.input_file))

    def testPart2(self):
        self.assertEqual(786240, find_lowest_house_number2(self.input_file))

    def testPart1Example(self):
        self.assertEqual(8, find_lowest_house_number(self.test_file))


if __name__ == "__main__":
    unittest.main()
