import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(210587128, safety_factor(self.input_file))

    def testPart2(self):
        self.assertEqual(7286, find_tree(self.input_file, seconds=10000))

    def testPart1Example(self):
        self.assertEqual(12, safety_factor(self.test_file, W=11, H=7))


if __name__ == "__main__":
    unittest.main()
