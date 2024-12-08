import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(159833790, sum_multiplications(self.input_file))

    def testPart2(self):
        self.assertEqual(89349241, sum_enabled_multiplications(self.input_file))

    def testPart1Example(self):
        self.assertEqual(161, sum_multiplications(self.test_file1))

    def testPart2Example(self):
        self.assertEqual(48, sum_enabled_multiplications(self.test_file2))


if __name__ == "__main__":
    unittest.main()
