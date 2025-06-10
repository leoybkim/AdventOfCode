import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(1061, count_lights(self.input_file, 100))

    def testPart2(self):
        self.assertEqual(1006, count_lights(self.input_file, 100, True))

    def testPart1Example(self):
        self.assertEqual(4, count_lights(self.test_file, 4))

    def testPart2Example(self):
        self.assertEqual(17, count_lights(self.test_file, 5, True))


if __name__ == "__main__":
    unittest.main()
