from utils.input_reader import read_file


def largest_joltage(banks: str) -> int:
    largest = float("-inf")
    n = len(banks)
    for i in range(n):
        for j in range(i + 1, n):
            largest = max(largest, int(banks[i] + banks[j]))
    return largest


def part_one(data: str):
    output = 0
    for banks in data.splitlines():
        output += largest_joltage(banks)

    return output


def part_two(data: str):
    output = 0
    NUM_BATTERIES = 12
    for banks in data.splitlines():
        banks = banks.strip()
        n = len(banks)
        discards = n - NUM_BATTERIES  # allowed number of remaining discards
        batteries_on = []
        for c in banks:
            while batteries_on and int(batteries_on[-1]) < int(c) and discards > 0:
                batteries_on.pop()
                discards -= 1
            batteries_on.append(c)
        output += int(''.join(batteries_on[:NUM_BATTERIES]))
    return output


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total output joltage: {part_one(file)}")
    print(f"New total output joltage: {part_two(file)}")
