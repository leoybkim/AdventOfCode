from collections import deque
from re import match


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def format_data(raw_input: str) -> list[str]:
    data = []
    for line in raw_input.split("\n"):
        data.append(line)
    return data


def calculate(operand1: int, operator: str, operand2: int = None) -> int:
    match operator:
        case "AND":
            return operand1 & operand2
        case "OR":
            return operand1 | operand2
        case "NOT":
            return (2 ** 16 - 1) - operand1
        case "LSHIFT":
            return operand1 << operand2
        case "RSHIFT":
            return operand1 >> operand2


def run_circuit(instructions: list) -> int:
    pattern = r"(\d+|[a-z]+)?\s*(AND|OR|LSHIFT|RSHIFT|NOT)?\s*(\d+|[a-z]+)?\s*->\s([a-z]+)"
    wires = {}
    q = deque(instructions)
    while q:
        l = q.popleft()  # FIFO
        m = match(pattern, l)
        operand1, operator, operand2, result = m.groups()
        processed = False

        # operand -> wire
        if operand2 is None and operator is None:
            if operand1.isdigit():
                wires[result] = int(operand1)  # Assign output to wire
                processed = True
            elif operand1 in wires:
                wires[result] = wires[operand1]
                processed = True

        # NOT operand -> wire
        elif operand1 is None:
            if operand2.isdigit():
                wires[result] = ~int(operand2)
                processed = True
            elif operand2 in wires:
                wires[result] = calculate(wires[operand2], operator)
                processed = True

        # operand1 operator operand2 -> wire
        else:
            op1 = int(operand1) if operand1.isdigit() else wires[operand1] if operand1 in wires else None
            op2 = int(operand2) if operand2.isdigit() else wires[operand2] if operand2 in wires else None
            if op1 is not None and op2 is not None:
                wires[result] = calculate(op1, operator, op2)
                processed = True

        if not processed:
            q.append(l)  # Push it back to the queue and process it later

        if "a" in wires:
            return wires["a"]


def find_signal_a(raw_input: str, override=False) -> int:
    instructions = format_data(raw_input)
    signal_a = run_circuit(instructions)

    if override:
        for i, instruction in enumerate(instructions):
            if instruction[-4:] == "-> b":
                instructions[i] = f"{signal_a} -> b"
        signal_a = run_circuit(instructions)

    return signal_a


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Signal provided to wire a: {find_signal_a(file)}")
    print(f"New signal provided to wire a after overriding b: {find_signal_a(file, override=True)}")
