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
        self.test_file6 = read_file("inputs/test6.txt")

    def testPart1(self):
        self.assertEqual(191164, sum_all_numbers(self.input_file))

    def testPart2(self):
        self.assertEqual(87842, sum_all_numbers(self.input_file, True))

    def testPart1Example1(self):
        self.assertEqual(12, sum_all_numbers(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(6, sum_all_numbers(self.test_file2))

    def testPart1Example3(self):
        self.assertEqual(0, sum_all_numbers(self.test_file3))

    def testPart1Example4(self):
        self.assertEqual(4, sum_all_numbers(self.test_file4, True))

    def testPart1Example5(self):
        self.assertEqual(0, sum_all_numbers(self.test_file5, True))

    def testPart1Example6(self):
        self.assertEqual(6, sum_all_numbers(self.test_file6, True))


if __name__ == "__main__":
    unittest.main()
