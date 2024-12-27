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
            "eq": [m.group(1), m.group(2), m.group(3), m.group(4)]
        }

    return wires, ops


def full_adder(n: int, wires: dict) -> int | None:
    """
    Full adder operation
          sum = X XOR Y XOR carry_in
    carry_out = (X AND Y) OR (carry_in AND (X XOR Y))
    """
    c_in = None
    for i in range(n):
        n_str = str(i).zfill(2)
        x_str = "x" + n_str
        y_str = "y" + n_str
        z_str = "z" + n_str
        x = wires[x_str] if x_str in wires else 0
        y = wires[y_str] if y_str in wires else 0
        z = wires[z_str]

        s = x ^ y
        tmp = x ^ y
        if c_in is not None:
            s ^= c_in
            tmp &= c_in
        c_out = (x & y) | tmp

        if z != s:
            return i  # Error in expected bit value
        else:
            if i < n - 1:
                c_in = c_out  # Next carry
    return None


def calculate(operand1: int, operator: str, operand2: int) -> int:
    match operator:
        case "AND":
            return operand1 & operand2
        case "OR":
            return operand1 | operand2
        case "XOR":
            return operand1 ^ operand2


def update_wires(wires: dict, ops: dict, swapped):
    wires[swapped[0]], wires[swapped[1]] = wires[swapped[1]], wires[swapped[0]]

    has_change = True
    while has_change:
        for k, v in ops.items():
            has_change = False
            if swapped[0] == v["eq"][0] or swapped[0] == v["eq"][2]:
                new_val0 = calculate(wires[v["eq"][0]], v["eq"][1], wires[v["eq"][2]])
                if v["value"] != new_val0:
                    has_change = True
                    v["value"] = new_val0
                    wires[k] = v["value"]
                    swapped[0] = k
            if swapped[1] == v["eq"][0] or swapped[1] == v["eq"][2]:
                new_val1 = calculate(wires[v["eq"][0]], v["eq"][1], wires[v["eq"][2]])
                if v["value"] != new_val1:
                    has_change = True
                    v["value"] = new_val1
                    wires[k] = v["value"]
                    swapped[1] = k
    # for k, v in ops.items():
    #     if v["eq"][0] in wires and v["eq"][2] in wires:
    #         v["value"] = calculate(wires[v["eq"][0]], v["eq"][1], wires[v["eq"][2]])
    #         wires[k] = v["value"]



def swap_operations(i: int, ops: dict) -> list:
    """
    After analyzing the full adder operation, each full adder goes through the following steps
    1) xN   XOR   yN   ->  A                 xN XOR yN
    2)  A   XOR  c_in  -> zN    --> Sum      xN XOR yN XOR carry_in
    3) xN   AND   yN   ->  C                 xN AND yN
    4)  A   AND  c_in  ->  D                 carry_in AND (xN XOR yN)
    5)  D    OR    C   ->  E    --> Carry   (carry_in AND (xN XOR yN)) or (xN OR yN)

    There are 5 choose 2 (nCr where n=5, r =2) combinations of error pairs, which equals to total 10 cases.
    However, switching 3) and 4) doesn't change the overall results, so this case can be ignored.
    So only 9 final cases needs to be considered.
    """

    def swap(k1, k2) -> list:
        ops[k1]["eq"][3], ops[k2]["eq"][3] = ops[k2]["eq"][3], ops[k1]["eq"][3]
        ops[k1], ops[k2] = ops[k2], ops[k1]
        return [k1, k2]

    operations = [None] * 5  # Store operations and an indicator for error in the resulting wire
    n_str = str(i).zfill(2)

    for k, v in ops.items():
        tmp = set(v["eq"][0:3])
        if tmp == {"x" + n_str, "XOR", "y" + n_str}:
            operations[0] = v  # 1) xN XOR yN -> A
            if v["eq"][3][0] == "z":
                for _k, _v in ops.items():
                    if _k == "z" + n_str:
                        return swap(k, _k)  # Swap 1) and 2)

        if tmp == {"x" + n_str, "AND", "y" + n_str}:
            operations[2] = v  # 3) xN AND yN -> C
            if v["eq"][3][0] == "z":
                for _k, _v in ops.items():
                    if _k == "z" + n_str:
                        return swap(k, _k)  # Swap 2) and 3)

    # Found operation 1) and 3), but results are not guaranteed to be correct
    if ops["z" + n_str]["eq"][1] == "OR":
        operations[4] = ops["z" + n_str]  # 5) D OR C -> E
        A = operations[0]["eq"][3]  # Need to swap 2) and 5), so can assume 1) is correct
        for _k, _v in ops.items():
            tmp = set(_v["eq"][0:3])
            if A in tmp and "XOR" in tmp:
                return swap("z" + n_str, _k)  # Swap 2) and 5)

    if ops["z" + n_str]["eq"][1] == "AND":
        operations[3] = ops["z" + n_str]  # 4) A AND c_in -> D
        for _k, _v in ops.items():
            tmp = set(_v["eq"][0:3])
            if tmp == {ops["z" + n_str]["eq"][0], "XOR", ops["z" + n_str]["eq"][2]}:
                return swap("z" + n_str, _k)  # Swap 2) and 4)

    if ops["z" + n_str]["eq"][1] == "XOR" and ops["z" + n_str]["eq"][0][0] not in ["x", "y"]:
        operations[1] = ops["z" + n_str]  # 2) A XOR c_in -> zN
        if operations[0]["eq"][3] not in ops["z" + n_str]["eq"]: # 1) is incorrect and must be swapped
            for _k, _v in ops.items():
                if _v["eq"][1] == "OR" and operations[0]["eq"][3] in _v["eq"]:
                    return swap(operations[0]["eq"][3], operations[2]["eq"][3])  # Swap 1) and 3)
            return swap(operations[0]["eq"][3], operations[3]["eq"][3])  # Swap 1) and 4)

    # if operations[4]["eq"][3] in operations[1]["eq"] and operations[0]["eq"][3] not in operations[1]["eq"]:
    #     return swap(operations[0]["eq"][3], operations[4]["eq"][3])  # Swap 1) and 5)
    #
    # if operations[3]["eq"][3] not in operations[4]["eq"] and operations[4]["eq"][3] in operations[4]["eq"]:
    #     return swap(operations[3]["eq"][3], operations[4]["eq"][3])  # Swap 4) and 5)
    #
    # if operations[2]["eq"][3] not in operations[4]["eq"] and operations[4]["eq"][3] not in operations[4]["eq"]:
    #     return swap(operations[2]["eq"][3], operations[4]["eq"][3])  # Swap 3) and 5)
    #

def output(raw_input: str, adder=False) -> int | str:
    wires, ops = format_data(raw_input)
    z_wires = []

    while any(op["value"] is None for op in ops.values()):
        for k, v in ops.items():
            if v["eq"][0] in wires and v["eq"][2] in wires:
                v["value"] = calculate(wires[v["eq"][0]], v["eq"][1], wires[v["eq"][2]])
                wires[k] = v["value"]

    for k, v in wires.items():
        if k[0] == "z":
            z_wires.append((k, v))
    z_wires.sort(key=lambda wire: wire[0], reverse=True)
    n = len(z_wires)

    if adder:
        swapped_wires = []
        error_index = full_adder(n, wires)
        while error_index is not None or len(swapped_wires) >= 8:
            error_index = full_adder(n, wires)
            swapped = swap_operations(error_index, ops)
            update_wires(wires, ops, swapped)
        swapped_wires.sort()
        return ",".join(swapped_wires)
    else:
        binary_str = "".join(str(wire[1]) for wire in z_wires)
        return int(binary_str, 2)


if __name__ == "__main__":
    file = read_file("inputs/omg3.txt")
    print(f"Decimal number output on wires starting with z: {output(file)}")
    # print(f"Output of the sorted wires name: {output(file, adder=True)}")
