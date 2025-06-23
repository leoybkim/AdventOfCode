import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test1_file = read_file("inputs/test1.txt")
        self.test2_file = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(110, support_TLS_count(self.input_file))

    def testPart2(self):
        self.assertEqual(242, support_SSL_count(self.input_file))

    def testPart1Example(self):
        self.assertEqual(2, support_TLS_count(self.test1_file))

    def testPart2Example(self):
        self.assertEqual(3, support_SSL_count(self.test2_file))


if __name__ == "__main__":
    unittest.main()
