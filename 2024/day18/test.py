import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(374, solve_maze(self.input_file))

    def testPart2(self):
        self.assertEqual((30, 12), solve_maze(self.input_file, most_corrupted=True))

    def testPart1Example1(self):
        self.assertEqual(22, solve_maze(self.test_file, R=7, C=7, I=12))

    def testPart2Example1(self):
        self.assertEqual((6, 1), solve_maze(self.test_file, R=7, C=7, I=12, most_corrupted=True))


if __name__ == "__main__":
    unittest.main()
