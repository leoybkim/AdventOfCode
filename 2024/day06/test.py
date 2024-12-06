import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.file = read_file("input.txt")

    def testPart1(self):
        self.assertEqual(5131, num_distinct_positions(self.file))

    def testPart1Example(self):
        test_file = read_file("test.txt")
        self.assertEqual(41, num_distinct_positions(test_file))


if __name__ == "__main__":
    unittest.main()
