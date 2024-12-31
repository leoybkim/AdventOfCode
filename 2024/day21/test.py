import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(162740, total_complexities(self.input_file, count=2))

    def testPart2(self):
        self.assertEqual(203640915832208, total_complexities(self.input_file, count=25))

    def testPart1Example1(self):
        self.assertEqual(126384, total_complexities(self.test_file, count=2))


if __name__ == "__main__":
    unittest.main()
