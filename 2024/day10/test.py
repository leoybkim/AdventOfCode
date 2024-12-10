import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")
        self.test_file3 = read_file("inputs/test3.txt")
        self.test_file4 = read_file("inputs/test4.txt")
        self.test_file5 = read_file("inputs/test5.txt")
        self.test_file6 = read_file("inputs/test6.txt")
        self.test_file7 = read_file("inputs/test7.txt")

    def testPart1(self):
        self.assertEqual(552, sum_trailhead_scores(self.input_file))

    def testPart2(self):
        self.assertEqual(1225, sum_trailhead_scores(self.input_file, ratings=True))

    def testPart1Example1(self):
        self.assertEqual(1, sum_trailhead_scores(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(2, sum_trailhead_scores(self.test_file2))

    def testPart1Example3(self):
        self.assertEqual(4, sum_trailhead_scores(self.test_file3))

    def testPart1Example4(self):
        self.assertEqual(3, sum_trailhead_scores(self.test_file4))

    def testPart1Example5(self):
        self.assertEqual(36, sum_trailhead_scores(self.test_file5))

    def testPart2Example1(self):
        self.assertEqual(3, sum_trailhead_scores(self.test_file6, ratings=True))

    def testPart2Example2(self):
        self.assertEqual(13, sum_trailhead_scores(self.test_file3, ratings=True))

    def testPart2Example3(self):
        self.assertEqual(227, sum_trailhead_scores(self.test_file7, ratings=True))

    def testPart2Example4(self):
        self.assertEqual(81, sum_trailhead_scores(self.test_file5, ratings=True))


if __name__ == "__main__":
    unittest.main()
