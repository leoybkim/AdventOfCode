import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from solution import part_one, part_two


class Test(unittest.TestCase):
    def setUp(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.input_file = os.path.join(base_dir, "inputs", "input.txt")
        self.test_file = os.path.join(base_dir, "inputs", "test.txt")

    def testPart1(self):
        self.assertEqual(992, part_one(self.input_file))

    def testPart2(self):
        self.assertEqual(6133, part_two(self.input_file))

    def testPart1Example(self):
        self.assertEqual(3, part_one(self.test_file))

    def testPart2Example(self):
        self.assertEqual(6, part_two(self.test_file))


if __name__ == "__main__":
    unittest.main()
