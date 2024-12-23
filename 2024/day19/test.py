import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(306, possible_designs(self.input_file))

    def testPart2(self):
        self.assertEqual(604622004681855, possible_designs(self.input_file, count_combinations=True))

    def testPart1Example1(self):
        self.assertEqual(6, possible_designs(self.test_file))

    def testPart2Example1(self):
        self.assertEqual(16, possible_designs(self.test_file, count_combinations=True))


if __name__ == "__main__":
    unittest.main()
