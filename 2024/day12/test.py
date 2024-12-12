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
        self.assertEqual(1344578, total_price(self.input_file))

    def testPart2(self):
        self.assertEqual(0, total_price(self.input_file))

    def testPart1Example1(self):
        self.assertEqual(140, total_price(self.test_file1))

    def testPart1Example2(self):
        self.assertEqual(772, total_price(self.test_file2))

    def testPart1Example3(self):
        self.assertEqual(1930, total_price(self.test_file3))

    def testPart2Example1(self):
        self.assertEqual(80, total_price(self.test_file1))

    def testPart2Example2(self):
        self.assertEqual(436, total_price(self.test_file2))

    def testPart2Example3(self):
        self.assertEqual(1206, total_price(self.test_file3))

    def testPart2Example4(self):
        self.assertEqual(236, total_price(self.test_file4))

    def testPart2Example5(self):
        self.assertEqual(368, total_price(self.test_file5))

if __name__ == "__main__":
    unittest.main()
