import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file1 = read_file("inputs/test1.txt", __file__)
        self.test_file2 = read_file("inputs/test2.txt", __file__)
        self.test_file3 = read_file("inputs/test3.txt", __file__)
        self.test_file4 = read_file("inputs/test4.txt", __file__)

    def testPart1(self):
        self.assertEqual(6337367222422, checksum(self.input_file))

    def testPart2(self):
        self.assertEqual(6361380647183, checksum(self.input_file, whole=True))

    def testPart1Example1(self):
        translated = translate(self.test_file1)
        rearranged = rearrange(translated, whole=False)
        self.assertEqual(list("0099811188827773336446555566.............."), rearranged)
        self.assertEqual(1928, checksum(self.test_file1))

    def testPart1Example2(self):
        translated = translate(self.test_file2)
        rearranged = rearrange(translated, whole=False)
        self.assertEqual(list("022111222......"), rearranged)
        self.assertEqual(60, checksum(self.test_file2))

    def testPart1Example3(self):
        translated = translate(self.test_file3)
        rearranged = rearrange(translated, whole=False)
        self.assertEqual(list("0099811188827773336446555566..............."), rearranged)
        self.assertEqual(1928, checksum(self.test_file3))

    def testPart2Example1(self):
        translated = translate(self.test_file1)
        rearranged = rearrange(translated, whole=True)
        self.assertEqual(list("00992111777.44.333....5555.6666.....8888.."), rearranged)
        self.assertEqual(2858, checksum(self.test_file1, whole=True))

    def testPart2Example2(self):
        translated = translate(self.test_file2)
        rearranged = rearrange(translated, whole=True)
        self.assertEqual(list("0..111....22222"), rearranged)
        self.assertEqual(132, checksum(self.test_file2, whole=True))

    def testPart2Example3(self):
        translated = translate(self.test_file3)
        rearranged = rearrange(translated, whole=True)
        self.assertEqual(list("00992111777.44.333....5555.6666.....8888..."), rearranged)
        self.assertEqual(2858, checksum(self.test_file3, whole=True))

    def testPart2Example4(self):
        self.assertEqual(222, checksum(self.test_file4, whole=True))


if __name__ == "__main__":
    unittest.main()
