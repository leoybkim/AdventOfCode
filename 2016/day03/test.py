import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)

    def testPart1(self):
        self.assertEqual(869, possible_triangles(self.input_file))

    def testPart2(self):
        self.assertEqual(1544, possible_triangles(self.input_file, part2=True))


if __name__ == "__main__":
    unittest.main()
