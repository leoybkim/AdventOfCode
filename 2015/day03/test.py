import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file1 = read_file("inputs/test1.txt", __file__)
        self.test_file2 = read_file("inputs/test2.txt", __file__)

    def testPart1(self):
        self.assertEqual(2081, count_houses(self.input_file))

    def testPart2(self):
        self.assertEqual(2341, count_houses(self.input_file, robo=True))

    def testPart1Example1(self):
        self.assertEqual(4, count_houses(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(2, count_houses(self.test_file2))

    def testPart2Example1(self):
        self.assertEqual(3, count_houses(self.test_file1, robo=True))

    def testPart2Example2(self):
        self.assertEqual(11, count_houses(self.test_file2, robo=True))


if __name__ == "__main__":
    unittest.main()
