import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.file = read_file("input.txt")

    def testPart1(self):
        self.assertEqual(5713, sum_correct_ordered_middle_pages(self.file))

    def testPart2(self):
        self.assertEqual(5180, sum_incorrect_ordered_middle_pages_after_reordering(self.file))

    def testPart1Example(self):
        test_file = read_file("test.txt")
        self.assertEqual(143, sum_correct_ordered_middle_pages(test_file))

    def testPart2Example(self):
        test_file = read_file("test.txt")
        self.assertEqual(123, sum_incorrect_ordered_middle_pages_after_reordering(test_file))


if __name__ == "__main__":
    unittest.main()
