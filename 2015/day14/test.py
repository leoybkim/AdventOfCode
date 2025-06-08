import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")

    def testPart1(self):
        self.assertEqual(2660, winning_raindeer_distance(self.input_file, 2503))

    def testPart2(self):
        self.assertEqual(1256, winning_raindeer_points(self.input_file, 2503))

    def testPart1Example1(self):
        self.assertEqual(1120, winning_raindeer_distance(self.test_file1, 1000))

    def testPart2Example1(self):
        self.assertEqual(689, winning_raindeer_points(self.test_file1, 1000))


if __name__ == "__main__":
    unittest.main()
