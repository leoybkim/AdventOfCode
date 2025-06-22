import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual("19636", bathroom_code(self.input_file))

    def testPart2(self):
        self.assertEqual("3CC43", bathroom_code(self.input_file, part2=True))

    def testPart1Example(self):
        self.assertEqual("1985", bathroom_code(self.test_file))

    def testPart2Example(self):
        self.assertEqual("5DB3", bathroom_code(self.test_file, part2=True))


if __name__ == "__main__":
    unittest.main()
