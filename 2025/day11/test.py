import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test1_file = read_file("inputs/test1.txt", __file__)
        self.test2_file = read_file("inputs/test2.txt", __file__)

    def testPart1(self):
        self.assertEqual(566, part_one(self.input_file))

    def testPart2(self):
        self.assertEqual(331837854931968, part_two(self.input_file))

    def testPart1Example(self):
        self.assertEqual(5, part_one(self.test1_file))

    def testPart2Example(self):
        self.assertEqual(2, part_two(self.test2_file))


if __name__ == "__main__":
    unittest.main()
