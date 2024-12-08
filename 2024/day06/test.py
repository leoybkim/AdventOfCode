import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(5131, num_guard_positions(self.input_file))

    def testPart2(self):
        self.assertEqual(1784, num_obstruction_positions(self.input_file))

    def testPart1Example(self):
        self.assertEqual(41, num_guard_positions(self.test_file))

    def testPart2Example(self):
        self.assertEqual(6, num_obstruction_positions(self.test_file))


if __name__ == "__main__":
    unittest.main()
