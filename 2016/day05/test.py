import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual("f97c354d", find_password(self.input_file))

    def testPart2(self):
        self.assertEqual("863dde27", find_password2(self.input_file))

    def testPart1Example(self):
        self.assertEqual("18f47a30", find_password(self.test_file))

    def testPart2Example(self):
        self.assertEqual("05ace8e3", find_password2(self.test_file))


if __name__ == "__main__":
    unittest.main()
