import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(19605500130, part_one(self.input_file))

    def testPart2(self):
        self.assertEqual(36862281418, part_two(self.input_file))

    def testPart1Example(self):
        self.assertEqual(1227775554, part_one(self.test_file))

    def testPart2Example(self):
        self.assertEqual(4174379265, part_two(self.test_file))


if __name__ == "__main__":
    unittest.main()
