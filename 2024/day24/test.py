import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(36902370467952, output(self.input_file))

    def testPart2(self):
        pass

    def testPart1Example1(self):
        self.assertEqual(4, output(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(2024, output(self.test_file2))


if __name__ == "__main__":
    unittest.main()
