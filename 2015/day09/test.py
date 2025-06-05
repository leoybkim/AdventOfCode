import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(207, find_shortest_distance(self.input_file))

    def testPart2(self):
        self.assertEqual(804, find_longest_distance(self.input_file))

    def testPart1Example1(self):
        self.assertEqual(605, find_shortest_distance(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(841, find_shortest_distance(self.test_file2))

    def testPart2Example1(self):
        self.assertEqual(982, find_longest_distance(self.test_file1))

    def testPart2Example2(self):
        self.assertEqual(1282, find_longest_distance(self.test_file2))

if __name__ == "__main__":
    unittest.main()
