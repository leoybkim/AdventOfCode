import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(13004408787, sum_secrets(self.input_file, iteration=2000))

    def testPart2(self):
        self.assertEqual(1455, most_bananas(self.input_file, iteration=2000))

    def testPart1Example1(self):
        self.assertEqual(37327623, sum_secrets(self.test_file1, iteration=2000))

    def testPart2Example1(self):
        self.assertEqual(23, most_bananas(self.test_file2, iteration=2000))


if __name__ == "__main__":
    unittest.main()
