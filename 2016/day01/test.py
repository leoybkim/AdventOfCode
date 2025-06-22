import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(288, find_distance(self.input_file))

    def testPart2(self):
        self.assertEqual(10, find_visited_location(self.input_file))

    def testPart2Example1(self):
        self.assertEqual(4, find_visited_location(self.test_file))


if __name__ == "__main__":
    unittest.main()
