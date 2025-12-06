import unittest

from .solution import *


class Test(unittest.TestCase):
    def setUp(self):
        self.input_file = read_file("inputs/input.txt", __file__)
        self.test_file1 = read_file("inputs/test1.txt", __file__)
        self.test_file2 = read_file("inputs/test2.txt", __file__)

    def testPart1(self):
        self.assertEqual("7,0,3,1,2,6,3,7,1", program_output(self.input_file))

    def testPart2(self):
        self.assertEqual(109020013201563, program_output(self.input_file, quine=True))

    def testPart1Example1(self):
        self.assertEqual("4,6,3,5,6,3,5,2,1,0", program_output(self.test_file1))

    def testPart1Example2(self):
        register = {"A": 0, "B": 0, "C": 9}
        program = [2, 6]
        comp = Computer(register, program)
        comp.compute()
        self.assertEqual(1, comp.registers["B"])

    def testPart1Example3(self):
        register = {"A": 10, "B": 0, "C": 0}
        program = [5, 0, 5, 1, 5, 4]
        comp = Computer(register, program)
        self.assertEqual([0, 1, 2], comp.compute())

    def testPart1Example4(self):
        register = {"A": 2024, "B": 0, "C": 0}
        program = [0, 1, 5, 4, 3, 0]
        comp = Computer(register, program)
        self.assertEqual([4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0], comp.compute())
        self.assertEqual(0, comp.registers["A"])

    def testPart1Example5(self):
        register = {"A": 0, "B": 29, "C": 0}
        program = [1, 7]
        comp = Computer(register, program)
        comp.compute()
        self.assertEqual(26, comp.registers["B"])

    def testPart1Example6(self):
        register = {"A": 0, "B": 2024, "C": 43690}
        program = [4, 0]
        comp = Computer(register, program)
        comp.compute()
        self.assertEqual(44354, comp.registers["B"])

    def testPart2Example1(self):
        self.assertEqual(117440, program_output(self.test_file2, quine=True))


if __name__ == "__main__":
    unittest.main()
