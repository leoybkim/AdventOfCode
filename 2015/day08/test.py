import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")
        self.test_file3 = read_file("inputs/test3.txt")
        self.test_file4 = read_file("inputs/test4.txt")
        self.test_file5 = read_file("inputs/test5.txt")

    def testPart1(self):
        self.assertEqual(1371, calculate_string(self.input_file))

    def testPart2(self):
        self.assertEqual(2117, calculate_string(self.input_file, new=True))

    def testPart1Example1(self):
        self.assertEqual(12, calculate_string(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(11, calculate_string(self.test_file2))

    def testPart1Example3(self):
        self.assertEqual(6, calculate_string(self.test_file3))

    def testPart1Example4(self):
        self.assertEqual(8, calculate_string(self.test_file4))

    def testPart1Exampl5(self):
        self.assertEqual(9, calculate_string(self.test_file5))


if __name__ == "__main__":
    unittest.main()
