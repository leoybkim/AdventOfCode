import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test1_file = read_file("inputs/test1.txt")
        self.test2_file = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(1415498, sum_gps_coordinates(self.input_file))

    def testPart2(self):
        pass

    def testPart1Example1(self):
        self.assertEqual(10092, sum_gps_coordinates(self.test1_file))

    def testPart1Example2(self):
        self.assertEqual(2028, sum_gps_coordinates(self.test2_file))

if __name__ == "__main__":
    unittest.main()
