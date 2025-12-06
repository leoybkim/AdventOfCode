import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(128, num_lit_pixels(self.input_file))

    def testPart2(self):
        self.assertEqual(6, num_lit_pixels(self.test_file, row=3, col=7))


if __name__ == "__main__":
    unittest.main()
