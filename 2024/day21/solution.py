from functools import lru_cache
from typing import List

from utils.input_reader import read_file

NUMERIC_KEYPAD = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "#": (3, 0), "0": (3, 1), "A": (3, 2)
}

DIRECTIONAL_KEYPAD = {
    "#": (0, 0), "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2),
}


def format_data(raw_data: str) -> List[str]:
    codes = []
    for line in raw_data.split("\n"):
        codes.append(line.strip())
    return codes


def generate_shortest_path(keypad) -> dict:
    """
    Generate a lookup for shortest path between all the keys.
    It is best to avoid turning as much as possible to find the shortest path.
    Prioritize the movements in the order of L, D, U, R
    @param keypad: Keypad controller grid
    @return: Best path between all the keys
    """
    shortest_path = {}
    for k1, (r1, c1) in keypad.items():
        if k1 != "#":
            for k2, (r2, c2) in keypad.items():
                if k2 != "#":
                    L = "<" * (c1 - c2)
                    D = "v" * (r2 - r1)
                    U = "^" * (r1 - r2)
                    R = ">" * (c2 - c1)
                    if (r1, c2) == keypad["#"] or (r2, c1) == keypad["#"]:
                        # Switch around the order of horizontal and vertical moves if path goes out of boundary
                        shortest_path[(k1, k2)] = R + D + U + L + "A"
                    else:
                        shortest_path[(k1, k2)] = L + D + U + R + "A"
    return shortest_path


NUMERIC_KEYPAD_PATH = generate_shortest_path(NUMERIC_KEYPAD)
DIRECTIONAL_KEYPAD_PATH = generate_shortest_path(DIRECTIONAL_KEYPAD)


@lru_cache
def shortest_sequence(code: str, count: int, numeric_keypad: bool) -> int:
    while count > 0:
        keypad = NUMERIC_KEYPAD_PATH if numeric_keypad else DIRECTIONAL_KEYPAD_PATH
        total = 0
        start = "A"
        for key in code:
            total += shortest_sequence(keypad[start, key], count if numeric_keypad else count - 1, numeric_keypad=False)
            start = key
        return total
    return len(code)


def total_complexities(raw_input: str, count: int) -> int:
    codes = format_data(raw_input)
    total = 0
    for code in codes:
        total += shortest_sequence(code, count, numeric_keypad=True) * int(code.split("A")[0])
    return total


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Sum of the complexities: {total_complexities(file, count=2)}")
    print(f"Sum of the complexities: {total_complexities(file, count=25)}")
