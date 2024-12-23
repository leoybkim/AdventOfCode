import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(1399, count_cheats(self.input_file, time=100))

    def testPart2(self):
        pass

    def testPart1Example1(self):
        self.assertEqual(1, count_cheats(self.test_file, time=64))

    def testPart1Example2(self):
        self.assertEqual(2, count_cheats(self.test_file, time=40))

    def testPart1Example3(self):
        self.assertEqual(8, count_cheats(self.test_file, time=12))

    def testPart1Example4(self):
        self.assertEqual(44, count_cheats(self.test_file, time=2))


if __name__ == "__main__":
    unittest.main()
