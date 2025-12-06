import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test1_file = read_file("inputs/test1.txt", __file__)
        self.test2_file = read_file("inputs/test2.txt", __file__)

    def testPart1(self):
        self.assertEqual(1824, find_min_mana_required(self.input_file))

    def testPart2(self):
        self.assertEqual(1937, find_min_mana_required(self.input_file, hard=True))

    def testPart1Example1(self):
        self.assertEqual(226, find_min_mana_required(self.test1_file, hp=10, mana=250))

    def testPart1Example2(self):
        self.assertEqual(641, find_min_mana_required(self.test2_file, hp=10, mana=250))


if __name__ == "__main__":
    unittest.main()
