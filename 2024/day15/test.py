import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")
        self.test_file3 = read_file("inputs/test3.txt")

    def testPart1(self):
        self.assertEqual(1415498, sum_gps_coordinates(self.input_file))

    def testPart2(self):
        self.assertEqual(1432898, sum_gps_coordinates(self.input_file, large=True))

    def testPart1Example1(self):
        self.assertEqual(10092, sum_gps_coordinates(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(2028, sum_gps_coordinates(self.test_file2))

    def testPart2Example1(self):
        self.assertEqual(618, sum_gps_coordinates(self.test_file3, large=True))

    def testPart2Example2(self):
        self.assertEqual(9021, sum_gps_coordinates(self.test_file1, large=True))


if __name__ == "__main__":
    unittest.main()
