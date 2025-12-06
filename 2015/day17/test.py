import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(4372, count_combinations(self.input_file, 150))

    def testPart2(self):
        self.assertEqual(4, count_minimum_combinations(self.input_file, 150))

    def testPart1Example(self):
        self.assertEqual(4, count_combinations(self.test_file, 25))

    def testPart2Example(self):
        self.assertEqual(3, count_minimum_combinations(self.test_file, 25))


if __name__ == "__main__":
    unittest.main()
