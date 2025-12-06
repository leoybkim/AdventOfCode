import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file = read_file("inputs/test.txt", __file__)

    def testPart1(self):
        self.assertEqual(1399, count_cheats(self.input_file, saved_time=100))

    def testPart2(self):
        self.assertEqual(994807, count_cheats(self.input_file, saved_time=100, cheat_time=20))

    def testPart1Example1(self):
        self.assertEqual(1, count_cheats(self.test_file, saved_time=64))

    def testPart1Example2(self):
        self.assertEqual(2, count_cheats(self.test_file, saved_time=40))

    def testPart1Example3(self):
        self.assertEqual(8, count_cheats(self.test_file, saved_time=12))

    def testPart1Example4(self):
        self.assertEqual(44, count_cheats(self.test_file, saved_time=2))

    def testPart2Example1(self):
        self.assertEqual(3, count_cheats(self.test_file, saved_time=76, cheat_time=20))

    def testPart2Example2(self):
        self.assertEqual(7, count_cheats(self.test_file, saved_time=74, cheat_time=20))

    def testPart2Example3(self):
        self.assertEqual(29, count_cheats(self.test_file, saved_time=72, cheat_time=20))

    def testPart2Example4(self):
        self.assertEqual(285, count_cheats(self.test_file, saved_time=50, cheat_time=20))


if __name__ == "__main__":
    unittest.main()
