import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test1_file = read_file("inputs/test1.txt")

    def testPart1(self):
        self.assertEqual(9132360, find_code(self.input_file))  # 28836990

    def testPart1Example1(self):
        self.assertEqual(18749137, find_code(self.test1_file))


if __name__ == "__main__":
    unittest.main()
