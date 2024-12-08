import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")
        self.test_file3 = read_file("inputs/test3.txt")
        self.test_file4 = read_file("inputs/test4.txt")
        self.test_file5 = read_file("inputs/test5.txt")

    def testPart1(self):
        self.assertEqual(293, total_nodes(self.input_file))

    def testPart2(self):
        self.assertEqual(934, total_nodes(self.input_file, loop=True))

    def testPart1Example1(self):
        self.assertEqual(14, total_nodes(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(2, total_nodes(self.test_file2))

    def testPart1Example3(self):
        self.assertEqual(4, total_nodes(self.test_file3))

    def testPart1Example4(self):
        self.assertEqual(4, total_nodes(self.test_file4))

    def testPart2Example1(self):
        self.assertEqual(9, total_nodes(self.test_file5, loop=True))

    def testPart2Example2(self):
        self.assertEqual(34, total_nodes(self.test_file1, loop=True))


if __name__ == "__main__":
    unittest.main()
