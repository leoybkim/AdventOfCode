from re import match


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_instructions(raw_input: str) -> list:
    instructions = []
    for line in raw_input.split("\n"):
        pattern = r"(\w+)\s([a-z])?(?:(?:,\s|\s?)([+-]?\d+))?$"
        m = match(pattern, line)
        operation = m.groups()[0]
        register = m.groups()[1]
        value = int(m.groups()[2]) if m.groups()[2] else None
        instructions.append((operation, register, value))
    return instructions


class Computah:
    def __init__(self, reg_a, reg_b, instruction_ptr):
        self.reg_a = reg_a
        self.reg_b = reg_b
        self.instruction_ptr = instruction_ptr  # instruction pointer

    def hlf(self, register):
        if register == "a":
            self.reg_a //= 2
        if register == "b":
            self.reg_b //= 2
        self.instruction_ptr += 1

    def tpl(self, register):
        if register == "a":
            self.reg_a *= 3
        if register == "b":
            self.reg_b *= 3
        self.instruction_ptr += 1

    def inc(self, register):
        if register == "a":
            self.reg_a += 1
        if register == "b":
            self.reg_b += 1
        self.instruction_ptr += 1

    def jmp(self, value):
        self.instruction_ptr += value

    def jie(self, register, value):
        if (register == "a" and self.reg_a % 2 == 0) or (register == "b" and self.reg_b % 2 == 0):
            self.instruction_ptr += value
        else:
            self.instruction_ptr += 1

    def jio(self, register, value):
        if (register == "a" and self.reg_a == 1) or (register == "b" and self.reg_b == 1):
            self.instruction_ptr += value
        else:
            self.instruction_ptr += 1


def operate(computer, operator, register, value):
    match operator:
        case "hlf":
            computer.hlf(register)
        case "tpl":
            computer.tpl(register)
        case "inc":
            computer.inc(register)
        case "jmp":
            computer.jmp(value)
        case "jie":
            computer.jie(register, value)
        case "jio":
            computer.jio(register, value)


def get_register_b(raw_input: str, reg_a=0) -> int:
    instructions = parse_instructions(raw_input)
    computer = Computah(reg_a, 0, 0)
    while 0 <= computer.instruction_ptr < len(instructions):
        operator, register, value = instructions[computer.instruction_ptr]
        operate(computer, operator, register, value)
    return computer.reg_b


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"The value in register b when program finishes executing: {get_register_b(input)}")
    print(f"The value in register b when program finishes executing if register a starts as 1: {get_register_b(input, reg_a=1)}")
