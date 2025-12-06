import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file1 = read_file("inputs/test1.txt", __file__)
        self.test_file2 = read_file("inputs/test2.txt", __file__)

    def testPart1(self):
        self.assertEqual(282749, find_number(self.input_file))

    def testPart2(self):
        self.assertEqual(9962624, find_number(self.input_file, zeros=6))

    def testPart1Example1(self):
        self.assertEqual(609043, find_number(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(1048970, find_number(self.test_file2))


if __name__ == "__main__":
    unittest.main()
