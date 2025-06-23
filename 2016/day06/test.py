import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual("qoclwvah", corrected_message(self.input_file))

    def testPart2(self):
        self.assertEqual("ryrgviuv", corrected_message(self.input_file, part2=True))

    def testPart1Example(self):
        self.assertEqual("easter", corrected_message(self.test_file))

    def testPart2Example(self):
        self.assertEqual("advent", corrected_message(self.test_file, part2=True))


if __name__ == "__main__":
    unittest.main()
