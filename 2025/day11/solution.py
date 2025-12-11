from collections import defaultdict
from functools import lru_cache

from utils.input_reader import read_file

YOU = "you"
OUT = "out"
SVR = "svr"
DAC = "dac"
FFT = "fft"


def parse_data(data: str) -> dict:
    path = defaultdict(list)
    for line in data.splitlines():
        items = line.split()
        items[0] = items[0][:-1]
        path[items[0]] += items[1:]
    return path


def part_one(data: str) -> int:
    path = parse_data(data)

    def dfs(label: str) -> int:
        if label == OUT:
            return 1
        total = 0
        for next_label in path[label]:
            total += dfs(next_label)
        return total

    return dfs(YOU)


def part_two(data: str) -> int:
    path = parse_data(data)

    # Memoize the combination of input (label, has_dac, has_fft)
    @lru_cache(maxsize=None)
    def dfs(label: str, has_dac: bool, has_fft: bool) -> int:
        has_dac = has_dac or (label == DAC)
        has_fft = has_fft or (label == FFT)
        if label == OUT:
            return 1 if (has_dac and has_fft) else 0
        total = 0
        for next_label in path[label]:
            total += dfs(next_label, has_dac, has_fft)
        return total

    return dfs(SVR, False, False)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of different paths from 'you' to 'out': {part_one(file)}")
    print(f"Number of different paths from 'svr' to 'out' while also visiting both 'dac' and 'fft': {part_two(file)}")
