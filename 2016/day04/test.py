import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(173787, sum_real_room_ids(self.input_file))

    def testPart2(self):
        self.assertEqual(548, find_north_pole_room(self.input_file))

    def testPart1Example(self):
        self.assertEqual(1514, sum_real_room_ids(self.test_file))


if __name__ == "__main__":
    unittest.main()
