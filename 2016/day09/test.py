import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")

    def testPart1(self):
        self.assertEqual(152851, decompressed_length(self.input_file))

    def testPart2(self):
        self.assertEqual(11797310782, decompressed_length(self.input_file, part2=True))

    def testPart1Example1(self):
        self.assertEqual(6, decompressed_length("ADVENT"))

    def testPart1Example2(self):
        self.assertEqual(7, decompressed_length("A(1x5)BC"))

    def testPart1Example3(self):
        self.assertEqual(9, decompressed_length("(3x3)XYZ"))

    def testPart1Example4(self):
        self.assertEqual(11, decompressed_length("A(2x2)BCD(2x2)EFG"))

    def testPart1Example5(self):
        self.assertEqual(6, decompressed_length("(6x1)(1x3)A"))

    def testPart1Example6(self):
        self.assertEqual(18, decompressed_length("X(8x2)(3x3)ABCY"))

    def testPart2Example1(self):
        self.assertEqual(9, decompressed_length("(3x3)XYZ", part2=True))

    def testPart2Example2(self):
        self.assertEqual(20, decompressed_length("X(8x2)(3x3)ABCY", part2=True))

    def testPart2Example3(self):
        self.assertEqual(241920, decompressed_length("(27x12)(20x12)(13x14)(7x10)(1x12)A", part2=True))

    def testPart2Example4(self):
        self.assertEqual(445,
                         decompressed_length("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", part2=True))


if __name__ == "__main__":
    unittest.main()
