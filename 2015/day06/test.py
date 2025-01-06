import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")
        self.test_file3 = read_file("inputs/test3.txt")

    def testPart1(self):
        self.assertEqual(400410, count_lit_light(self.input_file))

    def testPart2(self):
        self.assertEqual(15343601, count_lit_light(self.input_file, brightness=True))

    def testPart1Example1(self):
        self.assertEqual(1000000, count_lit_light(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(1000, count_lit_light(self.test_file2))

    def testPart1Example3(self):
        self.assertEqual(999996, count_lit_light(self.test_file3))


if __name__ == "__main__":
    unittest.main()
