from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[List[str]]]:
    schematics = []
    for chunk in raw_data.split("\n\n"):
        schematic = []
        for line in chunk.split("\n"):
            schematic.append(list(line))
        schematics.append(schematic)
    return schematics


def find_pairs(raw_input: str) -> int:
    schematics = format_data(raw_input)
    return 0


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of unique lock/key pairs fit without overlapping: {find_pairs(file)}")
