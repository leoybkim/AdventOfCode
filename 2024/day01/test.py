import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(2285373, find_total_distance(self.input_file))

    def testPart2(self):
        self.assertEqual(21142653, find_similarity_score(self.input_file))

    def testPart1Example(self):
        self.assertEqual(11, find_total_distance(self.test_file))

    def testPart2Example(self):
        self.assertEqual(31, find_similarity_score(self.test_file))


if __name__ == "__main__":
    unittest.main()
