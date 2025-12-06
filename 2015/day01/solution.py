from utils.input_reader import read_file


def santa_floor(input_file: str) -> int:
    floor = 0
    for c in input_file:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return floor


def santa_basement(input_file: str) -> int:
    floor = 0
    for i, c in enumerate(input_file):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

        if floor == -1:
            return i + 1


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Santa is on floor: {santa_floor(file)}")
    print(f"Santa will enter the basement on position: {santa_basement(file)}")
