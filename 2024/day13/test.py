import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")
        self.offset = 10000000000000

    def testPart1(self):
        self.assertEqual(29877, calculate_tokens(self.input_file))

    def testPart2(self):
        self.assertEqual(99423413811305, calculate_tokens(self.input_file, offset=self.offset))

    def testPart1Example1(self):
        self.assertEqual(480, calculate_tokens(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(0, calculate_tokens(self.test_file2))

    def testPart2Example1(self):
        self.assertEqual(875318608908, calculate_tokens(self.test_file1, offset=self.offset))


if __name__ == "__main__":
    unittest.main()
