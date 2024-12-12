from collections import Counter
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[int]:
    return list(map(int, raw_data.split()))


def num_stones(raw_input: str, blink: int) -> int:
    stones = format_data(raw_input)
    return count_stones(stones, blink)


def count_stones(stones: List[int], blink: int) -> int:
    counter = Counter(stones)
    for i in range(blink):
        temp_counter = Counter()
        for stone, count in counter.items():
            stone_str = str(stone)
            l = len(stone_str)
            if stone == 0:
                temp_counter[1] += count
            elif l % 2 == 0:
                one, two = stone_str[:l // 2], stone_str[l // 2:]
                temp_counter[int(one)] += count
                temp_counter[int(two)] += count
            else:
                temp_counter[stone * 2024] += count
        counter = temp_counter
    return sum(counter.values())


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of stones after blinking 25 times: {num_stones(file, blink=25)}")
    print(f"Number of stones after blinking 75 times: {num_stones(file, blink=75)}")
