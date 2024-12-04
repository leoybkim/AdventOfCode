import unittest
from solution import *

class Test(unittest.TestCase):
    def setUp(self):
        self.filename = "input.txt"

    def testPart1(self):
        self.assertEqual(236, num_safe_reports(self.filename))

    def testPart2(self):
        self.assertEqual(308, num_safe_reports(self.filename, dampener=1))


if __name__ == "__main__":
    unittest.main()
