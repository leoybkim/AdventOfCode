import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)

    def testPart1(self):
        self.assertEqual(307, get_register_b(self.input_file))

    def testPart2(self):
        self.assertEqual(160, get_register_b(self.input_file, reg_a=1))


if __name__ == "__main__":
    unittest.main()
