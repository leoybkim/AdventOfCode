import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)

    def testPart1(self):
        self.assertEqual(91, find_min_gold_required(self.input_file))

    def testPart2(self):
        self.assertEqual(158, find_min_gold_required(self.input_file, True))


if __name__ == "__main__":
    unittest.main()
