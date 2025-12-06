import re

from utils.input_reader import read_file


def parse_instructions(raw_input: str) -> list:
    instructions = []
    for line in raw_input.split("\n"):
        if line[:4] == "rect":
            match = re.match(r"rect (\d+)x(\d+)", line)
            instructions.append(("rect", int(match.group(1)), int(match.group(2))))
        elif len(line) >= 10:
            if line[:10] == "rotate row":
                match = re.match(r"rotate row y=(\d+) by (\d+)", line)
                instructions.append(("rotate row", int(match.group(1)), int(match.group(2))))
            elif line[:10] == "rotate col":
                match = re.match(r"rotate column x=(\d+) by (\d+)", line)
                instructions.append(("rotate column", int(match.group(1)), int(match.group(2))))
    return instructions


def rect(screen: list[list[int]], col: int, row: int):
    R = len(screen)
    C = len(screen[0])
    for r in range(R):
        for c in range(C):
            if 0 <= r < row and 0 <= c < col:
                screen[r][c] = 1


def rotate_row(screen: list[list[int]], row: int, shift: int):
    C = len(screen[0])
    new_row = [None] * C
    for c in range(C):
        new_row[(c + shift) % C] = screen[row][c]
    screen[row] = new_row


def rotate_column(screen: list[list[int]], col: int, shift: int):
    R = len(screen)
    C = len(screen[0])
    transposed = list(zip(*screen))
    new_column = [None] * R
    for r in range(R):
        new_column[(r + shift) % R] = transposed[col][r]

    for r in range(R):
        for c in range(C):
            if c == col:
                screen[r][c] = new_column[r]


def num_lit_pixels(raw_input: str, row=6, col=50) -> int:
    instructions = parse_instructions(raw_input)
    screen = [[0] * col for _ in range(row)]
    for instruction in instructions:
        match instruction[0]:
            case "rect":
                rect(screen, instruction[1], instruction[2])
            case "rotate row":
                rotate_row(screen, instruction[1], instruction[2])
            case "rotate column":
                rotate_column(screen, instruction[1], instruction[2])
    for row in screen:
        row_chars = ["@" if cell == 1 else " " for cell in row]
        print("".join(row_chars))
    return sum(light for row in screen for light in row)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of pixels that should be lit: {num_lit_pixels(file)}")
