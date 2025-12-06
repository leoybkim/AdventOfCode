import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(4722948564882, part_one(self.input_file))

    def testPart2(self):
        self.assertEqual(9581313737063, part_two(self.input_file))

    def testPart1Example(self):
        self.assertEqual(4277556, part_one(self.test_file))

    def testPart2Example(self):
        self.assertEqual(3263827, part_two(self.test_file))


if __name__ == "__main__":
    unittest.main()
