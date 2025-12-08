import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(52668, part_one(self.input_file, 1000))

    def testPart2(self):
        self.assertEqual(1474050600, part_two(self.input_file))

    def testPart1Example(self):
        self.assertEqual(40, part_one(self.test_file, 10))

    def testPart2Example(self):
        self.assertEqual(25272, part_two(self.test_file))


if __name__ == "__main__":
    unittest.main()
