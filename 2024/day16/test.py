import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(111480, solve_maze(self.input_file))

    def testPart2(self):
        pass

    def testPart1Example1(self):
        self.assertEqual(7036, solve_maze(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(11048, solve_maze(self.test_file2))

    def testPart2Example1(self):
        pass

    def testPart2Example2(self):
        pass


if __name__ == "__main__":
    unittest.main()