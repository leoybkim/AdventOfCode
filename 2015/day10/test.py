import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")
        self.test_file = read_file("inputs/test.txt")

    def testPart1(self):
        self.assertEqual(329356, look_and_say(self.input_file, 40))

    def testPart2(self):
        self.assertEqual(329356, look_and_say(self.input_file, 50))

    def testPart1Example(self):
        self.assertEqual(6, look_and_say(self.test_file, 5))


if __name__ == "__main__":
    unittest.main()
