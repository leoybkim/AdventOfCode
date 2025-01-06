import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")

    def testPart1(self):
        self.assertEqual(280, santa_floor(self.input_file))

    def testPart2(self):
        self.assertEqual(1797, santa_basement(self.input_file))


if __name__ == "__main__":
    unittest.main()
