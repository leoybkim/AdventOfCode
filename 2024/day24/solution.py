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


def full_adder(n: int, wires: dict, ops: dict) -> list | None:
    """
    Full adder operation
          sum = X XOR Y XOR carry_in
    carry_out = (X AND Y) OR (carry_in AND (X XOR Y))

    Performs addition of binary number and verifies if operation logic is valid.
    @param n: Length of the binary number being operated
    @param wires: Wire values
    @param ops: Operations
    @return: Return pair of wires that must be swapped if operation is invalid
    """
    c_in = None
    c_in_str = None
    c_out_str = None

    for i in range(n):
        n_str = str(i).zfill(2)
        x_str = "x" + n_str
        y_str = "y" + n_str
        z_str = "z" + n_str
        x = wires[x_str] if x_str in wires else 0
        y = wires[y_str] if y_str in wires else 0
        z = wires[z_str]

        # Bit calculations
        s = x ^ y
        tmp = x ^ y
        if c_in is not None:
            s ^= c_in
            tmp &= c_in
        c_out = (x & y) | tmp

        # Find corresponding operations
        if c_in is None:
            """
            Half adder: 2 operation steps
            1) X XOR Y   --> Sum
            2) X AND Y   --> Carry
            """
            for k, v in ops.items():
                if set(v["eq"][0:3]) == {x_str, "AND", y_str}:
                    c_out_str = k
        else:
            """
            Full adder: 5 operation steps
            After analyzing the full adder operation, each full adder goes through the following steps
            0) xN   XOR   yN   ->  A                 xN XOR yN
            1)  A   XOR  c_in  -> zN    --> Sum      xN XOR yN XOR carry_in
            2) xN   AND   yN   ->  C                 xN AND yN
            3)  A   AND  c_in  ->  D                 carry_in AND (xN XOR yN)
            4)  D    OR    C   ->  E    --> Carry   (carry_in AND (xN XOR yN)) or (xN OR yN)

            There are 5 choose 2 (nCr where n=5, r =2) combinations of error pairs, which equals to total 10 cases.
            """
            A = None
            eq = [None] * 5
            for k, v in ops.items():
                if c_in_str in v["eq"][0:3] and v["eq"][1] == "XOR":
                    if k == z_str:
                        # Operation 1) is valid if key is zN
                        A = v["eq"][0] if v["eq"][0] != c_in_str else v["eq"][2]
                        eq[1] = v
                    else:
                        # It is trivial that 1) must be swapped with an operation that holds zN as key
                        return [k, z_str]  # Accounts for 4 cases: 1) and [0), 2), 3), or 4)]
                if c_in_str in v["eq"][0:3] and v["eq"][1] == "AND":
                    eq[3] = v  # Validity of 3) is uncertain at this point

            for k, v in ops.items():
                if set(v["eq"][0:3]) == {x_str, "XOR", y_str}:
                    if k == A:
                        # Operation 0) is valid if key is A (it is guaranteed to have found A by this stage)
                        eq[0] = v
                    else:
                        # It is trivial that 0) must be swapped with an operation that holds A as key
                        return [k, A]  # Accounts for 3 cases: 0) and [2), 3) or 4)]
                if set(v["eq"][0:3]) == {x_str, "AND", y_str}:
                    eq[2] = v  # Validity of 2) is uncertain at this point

            for k, v in ops.items():
                if set(v["eq"][0:3]) == {eq[2]["eq"][3], "OR", eq[3]["eq"][3]}:
                    # Operation 4) is valid if C and D is in the equation (by this stage)
                    eq[4] = v
                    c_out_str = k  # E; by this stage all 5 operations are valid
                elif eq[2]["eq"][3] in set(v["eq"][0:3]) and v["eq"][1] == "OR":
                    # Operation 2) is valid and Operation 3) is invalid
                    return [k, eq[3]["eq"][3]]  # Need to swap 3) and 4)
                elif eq[3]["eq"][3] in set(v["eq"][0:3]) and v["eq"][1] == "OR":
                    # Operation 2) is invalid and Operation 3) is valid
                    return [k, eq[2]["eq"][3]]  # Need to swap 2) and 4)

            # Final case; check if 2) and 3) needs to be swapped
            if eq[3]["value"] == (x & y) and eq[3]["value"] != ((x ^ y) & c_in):
                return [eq[2]["eq"][3], eq[3]["eq"][3]]

        if z != s:
            # Error in expected bit value
            raise ValueError(f"There was an error in the calculation at bit position: {i}")
        else:
            if i < n - 1:
                c_in = c_out  # Next carry
                c_in_str = c_out_str


def calculate(operand1: int, operator: str, operand2: int) -> int:
    match operator:
        case "AND":
            return operand1 & operand2
        case "OR":
            return operand1 | operand2
        case "XOR":
            return operand1 ^ operand2


def cascade_update(key: str, wires: dict, ops: dict):
    """
    Upon swapping of the results, more equations may need to the updated if that swapped results is an input to another operation.
    @param key: Updated wire
    @param wires: Wire values
    @param ops: Operations
    """
    for k, v in ops.items():
        if key == v["eq"][0] or key == v["eq"][2]:
            new_val = calculate(wires[v["eq"][0]], v["eq"][1], wires[v["eq"][2]])
            if v["eq"][3] != new_val:
                ops[k]["value"] = new_val
                wires[k] = new_val
                cascade_update(k, wires, ops)  # Recursively update the output affected by the input change


def swap_operations(k1: str, k2: str, wires: dict, ops: dict):
    """
    Swap the results from the two operations and cascade the update.
    @param k1: Wire that stores the result of the first operation
    @param k2: Wire that stores the result of the second operation
    @param wires: Wire values
    @param ops: Operations
    """
    wires[k1], wires[k2] = wires[k2], wires[k1]
    ops[k1]["eq"][3], ops[k2]["eq"][3] = ops[k2]["eq"][3], ops[k1]["eq"][3]
    ops[k1], ops[k2] = ops[k2], ops[k1]
    cascade_update(k1, wires, ops)
    cascade_update(k2, wires, ops)


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
        # Find the 4 swapped pairs
        for _ in range(4):
            k1, k2 = full_adder(n, wires, ops)
            swapped_wires += [k1, k2]
            swap_operations(k1, k2, wires, ops)

        swapped_wires.sort()
        return ",".join(swapped_wires)
    else:
        binary_str = "".join(str(wire[1]) for wire in z_wires)
        return int(binary_str, 2)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Decimal number output on wires starting with z: {output(file)}")
    print(f"Output of the sorted wires name: {output(file, adder=True)}")
