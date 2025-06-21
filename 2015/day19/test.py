import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(576, distinct_molecules(self.input_file))

    def testPart2(self):
        self.assertEqual(207, generate_molecule(self.input_file))

    def testPart1Example(self):
        self.assertEqual(4, distinct_molecules(self.test_file1))

    def testPart2Example(self):
        self.assertEqual(6, generate_molecule(self.test_file2))


if __name__ == "__main__":
    unittest.main()
