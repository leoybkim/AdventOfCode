import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(5713, sum_correct_ordered_middle_pages(self.input_file))

    def testPart2(self):
        self.assertEqual(5180, sum_incorrect_ordered_middle_pages_after_reordering(self.input_file))

    def testPart1Example(self):
        self.assertEqual(143, sum_correct_ordered_middle_pages(self.test_file))

    def testPart2Example(self):
        self.assertEqual(123, sum_incorrect_ordered_middle_pages_after_reordering(self.test_file))


if __name__ == "__main__":
    unittest.main()
