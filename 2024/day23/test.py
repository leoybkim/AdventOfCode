import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        pass

    def testPart2(self):
        pass

    def testPart1Example1(self):
        self.assertEqual(7, lan_party_search(self.test_file))

    def testPart2Example1(self):
        pass


if __name__ == "__main__":
    unittest.main()
