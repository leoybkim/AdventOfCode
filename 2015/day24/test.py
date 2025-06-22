import unittest

from solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt")

    def testPart1(self):
        self.assertEqual(11846773891, quantum_entanglement(self.input_file))

    def testPart2(self):
        self.assertEqual(80393059, quantum_entanglement(self.input_file, groups=4))


if __name__ == "__main__":
    unittest.main()
