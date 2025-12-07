from utils.input_reader import read_file


def parse_data(data: str):
    grid = []
    for line in data.splitlines():
        grid.append(list(line))
    return grid


def part_one(data: str) -> int:
    grid = parse_data(data)
    num_cols = len(grid)

    beams = [0] * num_cols
    beams[grid[0].index("S")] = 1

    split_count = 0

    for row in grid[1:]:
        for i in range(num_cols):
            if beams[i] > 0 and row[i] == "^":
                # split the beam!
                split_count += 1
                beams[i] = 0
                if i > 0:
                    beams[i - 1] = 1
                if i < num_cols - 1:
                    beams[i + 1] = 1
            else:
                continue

    return split_count


def part_two(data: str) -> int:
    grid = parse_data(data)
    num_cols = len(grid)

    beams = [0] * num_cols
    beams[grid[0].index("S")] = 1

    for row in grid[1:]:
        for i in range(num_cols):
            if beams[i] > 0 and row[i] == "^":
                # split the beam!
                prev_v = beams[i]
                beams[i] = 0
                if i > 0:
                    beams[i - 1] += prev_v
                if i < num_cols - 1:
                    beams[i + 1] += prev_v
            else:
                continue

    return sum(beams)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total number of splits: {part_one(file)}")
    print(f"Total timelines: {part_two(file)}")
