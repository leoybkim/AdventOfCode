import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")
        self.test_file3 = read_file("inputs/test3.txt")
        self.test_file4 = read_file("inputs/test4.txt")

    def testPart1(self):
        pass

    def testPart2(self):
        pass

    def testPart1Example(self):
        self.assertEqual(12, calculate_string(self.test_file1))

    def testPart2Example(self):
        self.assertEqual(11, calculate_string(self.test_file2))

    def testPart3Example(self):
        self.assertEqual(6, calculate_string(self.test_file3))

    def testPart4Example(self):
        self.assertEqual(8, calculate_string(self.test_file4))


if __name__ == "__main__":
    unittest.main()
