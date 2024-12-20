def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> tuple:
    register_str, program_str = raw_data.split("\n\n")
    registers = {}
    for r in register_str.split("\n"):
        i = r.index(":")
        registers[r[i - 1]] = int(r[i + 1:].strip())
    return registers, list(map(int, map(str.strip, program_str.split(":")[1].split(","))))


class Computer:
    def __init__(self, registers, program):
        self.registers = registers
        self.program = program
        self.pointer = 0
        self.output = []

    def combo_operand(self, operand: int) -> int:
        if operand in [0, 1, 2, 3]:
            return operand
        elif operand == 4:
            return self.registers["A"]
        elif operand == 5:
            return self.registers["B"]
        elif operand == 6:
            return self.registers["C"]
        elif operand == 7:
            raise ValueError("7 is reserved operand")

    def run_instructions(self, opcode: int, operand: int):
        if opcode == 0:
            # adv instruction performs division;
            # numerator: A register, denominator: 2^(combo operand)
            # result of division is truncated to an integer and then written to the A register
            self.registers["A"] = self.registers["A"] >> self.combo_operand(operand)
        elif opcode == 1:
            # bxl instruction calculates the bitwise XOR of register B and the instruction's literal operand;
            # result is stored to register B
            self.registers["B"] = self.registers["B"] ^ operand
        elif opcode == 2:
            # bst instruction calculates the value of combo operand modulo 8 (thereby keeping only its lowest 3 bits)
            # result is stored to register B
            self.registers["B"] = self.combo_operand(operand) % 8
        elif opcode == 3:
            # jnz instruction does nothing if A register is 0;
            # if A register is not 0, it jumps by setting the instruction pointer to the value of its literal operand
            if self.registers["A"] != 0:
                self.pointer = operand
        elif opcode == 4:
            # bxc instruction calculates the bitwise XOR of register B and register C
            # result is stored in register B (legacy reasons: reads the operand but ignores it)
            self.registers["B"] = self.registers["B"] ^ self.registers["C"]
        elif opcode == 5:
            # out instruction calculates the value of its combo operand modulo 8 and outputs that value
            self.output.append(self.combo_operand(operand) % 8)
        elif opcode == 6:
            # bdv instruction works exactly like adv instruction but store result in B register
            self.registers["B"] = self.registers["A"] >> self.combo_operand(operand)
        elif opcode == 7:
            # cdv instruction works exactly like adv instruction but store result in C register
            self.registers["C"] = self.registers["A"] >> self.combo_operand(operand)

    def compute(self):
        while self.pointer <= len(self.program) - 2:
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            self.run_instructions(opcode, operand)
            if opcode != 3 or self.pointer != operand:
                self.pointer += 2
        return ",".join(map(str, self.output))


def program_output(raw_input: str) -> str:
    registers, program = format_data(raw_input)
    computer = Computer(registers, program)
    return computer.compute()


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Value of the program output: {program_output(file)}")
