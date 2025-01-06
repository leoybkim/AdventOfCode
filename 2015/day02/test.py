import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(1588178, calculate_wrapping_paper(self.input_file))

    def testPart2(self):
        self.assertEqual(3783758, calculate_ribbon_length(self.input_file))

    def testPart1Example(self):
        self.assertEqual(58, calculate_wrapping_paper(self.test_file))

    def testPart2Example(self):
        self.assertEqual(34, calculate_ribbon_length(self.test_file))


if __name__ == "__main__":
    unittest.main()
