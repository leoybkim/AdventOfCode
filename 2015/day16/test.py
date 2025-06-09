import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")

    def testPart1(self):
        self.assertEqual(103, find_aunt_sue(self.input_file))

    def testPart2(self):
        self.assertEqual(405, find_aunt_sue(self.input_file, True))


if __name__ == "__main__":
    unittest.main()
