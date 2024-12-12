import unittest
from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file1 = read_file("inputs/test1.txt")
        self.test_file2 = read_file("inputs/test2.txt")

    def testPart1(self):
        self.assertEqual(233875, num_stones(self.input_file, blink=25))

    def testPart2(self):
        self.assertEqual(277444936413293, num_stones(self.input_file, blink=75))

    def testPart1Example1(self):
        self.assertEqual(len([1, 2024, 1, 0, 9, 9, 2021976]), num_stones(self.test_file1, blink=1))

    def testPart1Example2(self):
        self.assertEqual(len([253000, 1, 7]), num_stones(self.test_file2, blink=1))

    def testPart1Example3(self):
        self.assertEqual(len([253, 0, 2024, 14168]), num_stones(self.test_file2, blink=2))

    def testPart1Example4(self):
        self.assertEqual(len([512072, 1, 20, 24, 28676032]), num_stones(self.test_file2, blink=3))

    def testPart1Example5(self):
        self.assertEqual(len([512, 72, 2024, 2, 0, 2, 4, 2867, 6032]), num_stones(self.test_file2, blink=4))

    def testPart1Example6(self):
        self.assertEqual(len([1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32]),
                         num_stones(self.test_file2, blink=5))

    def testPart1Example7(self):
        self.assertEqual(
            len([2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2]),
            num_stones(self.test_file2, blink=6))

    def testPart1Example8(self):
        self.assertEqual(55312, num_stones(self.test_file2, blink=25))


if __name__ == "__main__":
    unittest.main()
