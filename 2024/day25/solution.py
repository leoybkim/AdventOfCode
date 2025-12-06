from itertools import product

from utils.input_reader import read_file


def format_data(raw_data: str) -> tuple[list[list[list[str]]], list[list[list[str]]]]:
    keys, locks = [], []
    for chunk in raw_data.split("\n\n"):
        schematic = []
        for line in chunk.split("\n"):
            schematic.append(list(line))
        if chunk[0][0] == "#":
            locks.append(schematic)
        else:
            keys.append(schematic)
    return keys, locks


def converter(schematic: list[list[str]]) -> list[int]:
    height = []
    if schematic[0][0] == "#":
        # lock height
        for column in range(len(schematic[0])):
            height.append(sum(1 for row in schematic[1:] if row[column] == "#"))
    else:
        # key height
        for column in range(len(schematic[0])):
            height.append(sum(1 for row in schematic[1:len(schematic) - 1] if row[column] == "#"))
    return height


def count_pairs(raw_input: str) -> int:
    keys, locks = format_data(raw_input)
    count = 0
    for lock, key in product(locks, keys):
        lock_height = converter(lock)
        key_height = converter(key)
        count += 1
        for i in range(len(lock_height)):
            if lock_height[i] + key_height[i] > 5:
                count -= 1
                break
    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of unique lock/key pairs fit without overlapping: {count_pairs(file)}")
