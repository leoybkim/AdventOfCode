import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.file = read_file("input.txt")
        self.letters = format_data(self.file)

    def testPart1(self):
        self.assertEqual(2336, count_xmas(self.letters))

    def testPart2(self):
        self.assertEqual(1831, count_x_mas(self.letters))

    def testPart1Example1(self):
        test_file = read_file("test-part1-1.txt")
        test_data = format_data(test_file)
        self.assertEqual(4, count_xmas(test_data))

    def testPart1Example2(self):
        test_file = read_file("test-part1-2.txt")
        test_data = format_data(test_file)
        self.assertEqual(18, count_xmas(test_data))

    def testPart2Example1(self):
        test_file = read_file("test-part2.txt")
        test_data = format_data(test_file)
        self.assertEqual(9, count_x_mas(test_data))


if __name__ == "__main__":
    unittest.main()
