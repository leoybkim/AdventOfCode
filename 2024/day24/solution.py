import re


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> tuple[dict, dict]:
    wire_str, op_str = raw_data.split("\n\n")
    wires = {}
    for line in wire_str.split("\n"):
        name, value = line.split(":")
        wires[name] = int(value.strip())

    ops = {}
    pattern = r"^([A-Za-z0-9]{3}) ([A-Za-z0-9]{2,3}) ([A-Za-z0-9]{3}) -> ([A-Za-z0-9]{3})$"
    for op in op_str.split("\n"):
        m = re.match(pattern, op)
        ops[m.group(4)] = {
            "value": None,
            "equation": (m.group(1), m.group(2), m.group(3), m.group(4))
        }

    return wires, ops

def recalculate(operand: str, ops: dict, wires: dict):
    for k, v in ops.items():
        if v["equation"][0] == operand or v["equation"][2]:
            old_value = v["value"]
            v["value"] = calculate(wires[v["equation"][0]], v["equation"][1], wires[v["equation"][2]])
            if v["value"] != old_value:
                recalculate(k, ops, wires)


def calculate(operand1: int, operator: str, operand2: int) -> int:
    match operator:
        case "AND":
            return operand1 & operand2
        case "OR":
            return operand1 | operand2
        case "XOR":
            return operand1 ^ operand2


def output(raw_input: str, adder=False) -> int | str:
    wires, ops = format_data(raw_input)
    while any(op["value"] is None for op in ops.values()):
        for k, v in ops.items():
            if v["equation"][0] in wires and v["equation"][2] in wires:
                v["value"] = calculate(wires[v["equation"][0]], v["equation"][1], wires[v["equation"][2]])
                wires[k] = v["value"]

    x_wires = []
    y_wires = []
    z_wires = []
    for k, v in wires.items():
        if k[0] == "x":
            x_wires.append((k, v))
        elif k[0] == "y":
            y_wires.append((k, v))
        elif k[0] == "z":
            z_wires.append((k, v))
    x_wires.sort(key=lambda wire: wire[0], reverse=True)
    y_wires.sort(key=lambda wire: wire[0], reverse=True)
    z_wires.sort(key=lambda wire: wire[0], reverse=True)

    if adder:
        x_str = "".join(str(wire[1]) for wire in x_wires)
        y_str = "".join(str(wire[1]) for wire in y_wires)
        z_str = "".join(str(wire[1]) for wire in z_wires)
        print(f"x:  {x_str} int: {int(x_str, 2)}")
        print(f"y:  {y_str} int: {int(y_str, 2)}")
        print(f"z: {z_str} int: {int(z_str, 2)}")
        print(f"Expected sum of {int(x_str, 2)} +  {int(y_str, 2)} = {int(x_str, 2) + int(y_str, 2)}")
        print(f"Binary representation of the sum is {bin(int(x_str, 2) + int(y_str, 2))}")

        need_swap = []

        """
        Full adder operation
              sum = X XOR Y XOR carry_in
        carry_out = (X AND Y) OR (carry_in AND (X XOR Y)) 
        """
        c_in = None
        for i in range(len(z_wires)):
            n_str = str(i).zfill(2)
            _z = wires["z" + n_str]
            _x = wires["x" + n_str] if ("x" + n_str) in wires else 0
            _y = wires["y" + n_str] if ("y" + n_str) in wires else 0

            print(f"Operation {n_str}: c_in: {c_in}; x: {_x}; y: {_y}")
            s = _x ^ _y
            _c_out = _x ^ _y
            if c_in is not None:
                s ^= c_in
                _c_out &= c_in
            c_out = (_x & _y) | _c_out

            if _z != s:
                print(i)
                need_swap.append("z" + n_str)
                wires["z" + n_str] = wires["z" + n_str] ^ 1 # Flip value
                ops["z" + n_str]["value"] = ops["z" + n_str]["value"] ^ 1
                recalculate("z" + n_str, ops, wires)  # Recursively fix the calculations
            print(f"z value: {_z}; actual sum: {s}; next carry: {c_out}")


        return ""
    else:
        binary_str = "".join(str(wire[1]) for wire in z_wires)
        return int(binary_str, 2)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    # print(f"Decimal number output on wires starting with z: {output(file)}")
    print(f"Output of the sorted wires name: {output(file, adder=True)}")
