TOTAL_TICKS = 100
START_POSITION = 50


def part_one(input_file_path: str):
    dial = START_POSITION
    zeros = 0

    with open(input_file_path, "r") as input_file:
        for line in input_file:
            direction, n = line[0], int(line[1:])
            if direction == "L":
                n *= -1
            dial += n
            zeros += dial % TOTAL_TICKS == 0
        return zeros


def part_two(input_file_path: str):
    dial = START_POSITION
    zeros = 0
    with open(input_file_path, "r") as input_file:
        for line in input_file:
            direction, n = line[0], int(line[1:])
            if direction == "L":
                n *= -1
            at_zero = dial == 0
            laps, dial = divmod(dial + n, TOTAL_TICKS)
            zeros += abs(laps)
            if n < 0:
                zeros += (dial == 0) - at_zero
        return zeros


if __name__ == "__main__":
    file = "inputs/input.txt"
    print(f"Actual password is: {part_one(file)}")
    print(f"Actual password with new protocol is: {part_two(file)}")
