import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(238, count_nice_strings(self.input_file))

    def testPart2(self):
        self.assertEqual(69, count_nice_strings(self.input_file, new_rule=True))

    def testPart2Example(self):
        self.assertEqual(2, count_nice_strings(self.test_file, new_rule=True))


if __name__ == "__main__":
    unittest.main()
