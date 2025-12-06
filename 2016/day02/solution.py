from utils.input_reader import read_file


def parse_instructions(raw_input: str) -> list:
    instructions = []
    for line in raw_input.split("\n"):
        instructions.append(list(line))
    return instructions


def bathroom_code(raw_input: str, part2=False) -> str:
    instructions = parse_instructions(raw_input)

    if part2:
        keypad = [[None, None, "1", None, None],
                  [None, "2", "3", "4", None],
                  ["5", "6", "7", "8", "9"],
                  [None, "A", "B", "C", None],
                  [None, None, "D", None, None]]
        # the starting button is "5"
        r = 2
        c = 0
    else:
        keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        r = c = 1  # the starting button is "5"

    code = []

    direction = {
        "U": (-1, 0),
        "L": (0, -1),
        "R": (0, 1),
        "D": (1, 0)
    }

    def valid_move(_r, _c, dr, dc):
        return 0 <= _r + dr < len(keypad) and 0 <= _c + dc < len(keypad[0]) and keypad[_r + dr][_c + dc] is not None

    for instruction in instructions:
        for step in instruction:
            if valid_move(r, c, direction[step][0], direction[step][1]):
                r += direction[step][0]
                c += direction[step][1]

        # Press the corresponding button at the end of following each line of instructions
        code.append(keypad[r][c])

    return "".join(code)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Bathroom code is: {bathroom_code(file)}")
    print(f"Bathroom code is: {bathroom_code(file, part2=True)}")
