import unittest
from solution import *

class Test(unittest.TestCase):
    def setUp(self):
        self.file = read_file("input.txt")

    def testPart1(self):
        self.assertEqual(159833790, sum_multiplications(self.file))

    def testPart2(self):
        self.assertEqual(89349241, sum_enabled_multiplications(self.file))


if __name__ == "__main__":
    unittest.main()
