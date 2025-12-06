from typing import List

from utils.input_reader import read_file


def format_data(raw_data: str) -> tuple:
    register_str, program_str = raw_data.split("\n\n")
    registers = {}
    for r in register_str.split("\n"):
        i = r.index(":")
        registers[r[i - 1]] = int(r[i + 1:].strip())
    return registers, list(map(int, map(str.strip, program_str.split(":")[1].split(","))))


class Computer:
    def __init__(self, registers: dict, program: List[int]):
        self.registers = registers
        self.program = program
        self.pointer = 0
        self.output = []

    def combo_operand(self, operand: int) -> int:
        match operand:
            case 0 | 1 | 2 | 3:
                return operand
            case 4:
                return self.registers["A"]
            case 5:
                return self.registers["B"]
            case 6:
                return self.registers["C"]
            case 7:
                raise ValueError("7 is reserved operand")

    def run_instructions(self, opcode: int, operand: int):
        match opcode:
            case 0:
                self.registers["A"] = self.registers["A"] >> self.combo_operand(operand)
            case 1:
                self.registers["B"] = self.registers["B"] ^ operand
            case 2:
                self.registers["B"] = self.combo_operand(operand) % 8
            case 3:
                if self.registers["A"] != 0:
                    self.pointer = operand
            case 4:
                self.registers["B"] = self.registers["B"] ^ self.registers["C"]
            case 5:
                self.output.append(self.combo_operand(operand) % 8)
            case 6:
                self.registers["B"] = self.registers["A"] >> self.combo_operand(operand)
            case 7:
                self.registers["C"] = self.registers["A"] >> self.combo_operand(operand)

    def compute(self):
        while self.pointer <= len(self.program) - 2:
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            self.run_instructions(opcode, operand)
            if opcode != 3 or self.pointer != operand:
                self.pointer += 2
        self.pointer = 0
        return self.output


def program_output(raw_input: str, quine=False) -> str | int:
    registers, program = format_data(raw_input)
    computer = Computer(registers, program)
    if quine:
        return find_init_value(0, 0, registers, program)
    else:
        output = computer.compute()
        return ",".join(map(str, output))


def find_init_value(a: int, i: int, registers: dict, program: List[int]) -> int | None:
    """
    Reverse engineer the computer program to find the register A value that outputs an exact copy of the input program.
    After analysing the program behaviour, I noticed that the lowest 3 bits of A are discarded after each iteration.
    Once A reaches 0, the program halts.
    I also noticed that the output at each iteration is also based on these lowest 3 bits of A.
    So initially, I loop through potential values of A that produces the output of the last iteration.
    The loop only needs to range upto 7 because 3 bits can only express values from 0 to 7.
    After I find a potential value of A that can generate the last output, I bit shift left by 3 (multiply 8), creating space for the next 3 bits to be explored through DFS.
    I also increment the number of outputs that needs to be matched at each depth of the search until all outputs are matched.
    @param a: Potential register A value
    @param i: Suffix index that matches the input program
    @param registers: Input registers
    @param program: Input program
    @return: Quine Register A
    """
    registers["A"] = a
    computer = Computer(registers, program)
    output = computer.compute()
    # print(f"a: {a} bin(a): {bin(a)} - output after running: {output}")

    # Base case
    if output == program:
        return a

    # Explore initial values or if output matches suffix of the program
    if i == 0 or output == program[-i:]:
        # Explore all possible values from 0 through 7:
        for j in range(8):
            new_a = (a << 3) + j
            new_i = i + 1
            tmp = find_init_value(new_a, new_i, registers, program)
            if tmp:
                return tmp
    return None


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Value of the program output: {program_output(file)}")
    print(f"Lowest positive register A that causes the program to copy itself: {program_output(file, quine=True)}")
