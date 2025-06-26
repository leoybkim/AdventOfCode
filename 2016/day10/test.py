import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(181, find_bot(self.input_file, 61, 17))

    def testPart2(self):
        self.assertEqual(12567, output_product(self.input_file, [0, 1, 2]))

    def testPart1Example1(self):
        self.assertEqual(2, find_bot(self.test_file, 5, 2))


if __name__ == "__main__":
    unittest.main()
