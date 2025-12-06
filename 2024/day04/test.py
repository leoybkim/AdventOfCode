import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file1_1 = read_file("inputs/test1-1.txt", __file__)
        self.test_file1_2 = read_file("inputs/test1-2.txt", __file__)
        self.test_file2 = read_file("inputs/test2.txt", __file__)

    def testPart1(self):
        self.assertEqual(2336, count_xmas(format_data(self.input_file)))

    def testPart2(self):
        self.assertEqual(1831, count_x_mas(format_data(self.input_file)))

    def testPart1Example1(self):
        self.assertEqual(4, count_xmas(format_data(self.test_file1_1)))

    def testPart1Example2(self):
        self.assertEqual(18, count_xmas(format_data(self.test_file1_2)))

    def testPart2Example1(self):
        self.assertEqual(9, count_x_mas(format_data(self.test_file2)))


if __name__ == "__main__":
    unittest.main()
