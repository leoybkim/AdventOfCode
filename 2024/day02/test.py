import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = "inputs/input.txt"
        self.test_file = "inputs/test.txt"

    def testPart1(self):
        self.assertEqual(236, num_safe_reports(self.input_file))

    def testPart2(self):
        self.assertEqual(308, num_safe_reports(self.input_file, dampener=1))

    def testPart1Example(self):
        self.assertEqual(2, num_safe_reports(self.test_file))

    def testPart2Example(self):
        self.assertEqual(4, num_safe_reports(self.test_file, dampener=1))


if __name__ == "__main__":
    unittest.main()
