import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.file = read_file("input.txt")

    def testPart1(self):
        self.assertEqual(1985268524462, total_calibration(self.file))

    def testPart2(self):
        self.assertEqual(150077710195188, total_calibration(self.file, allow_concat=True))

    def testPart1Example(self):
        test_file = read_file("test.txt")
        self.assertEqual(3749, total_calibration(test_file))

    def testPart2Example(self):
        test_file = read_file("test.txt")
        self.assertEqual(11387, total_calibration(test_file, allow_concat=True))


if __name__ == "__main__":
    unittest.main()
