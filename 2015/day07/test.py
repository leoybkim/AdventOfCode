import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")

    def testPart1(self):
        self.assertEqual(46065, find_signal_a(self.input_file))

    def testPart2(self):
        self.assertEqual(14134, find_signal_a(self.input_file, override=True))


if __name__ == "__main__":
    unittest.main()
