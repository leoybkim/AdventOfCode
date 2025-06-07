import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")

    def testPart1(self):
        self.assertEqual(733, happiness_change(self.input_file))

    def testPart2(self):
        self.assertEqual(725, happiness_change(self.input_file, True))

    def testPart1Example1(self):
        self.assertEqual(330, happiness_change(self.test_file1))


if __name__ == "__main__":
    unittest.main()
