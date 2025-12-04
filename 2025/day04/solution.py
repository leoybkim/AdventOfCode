def parse_file(input_file_path: str) -> list[list[str]]:
    grid = []
    with (open(input_file_path, "r") as input_file):
        for line in input_file:
            grid.append(list(line.strip()))
    return grid


def can_access(x: int, y: int, grid: list[list[str]]) -> bool:
    # loop through 8 adjacent positions
    roll_count = 0
    adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in adj:
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
            roll_count += grid[x + dx][y + dy] == "@"
            if roll_count >= 4:
                return False
    return True


def part_one(input_file_path: str):
    output = 0
    grid = parse_file(input_file_path)

    R, C = len(grid), len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "@":
                output += can_access(r, c, grid)
    return output


def part_two(input_file_path: str):
    grid = parse_file(input_file_path)

    R, C = len(grid), len(grid[0])
    remove_count = 0
    can_remove = True
    while can_remove:
        can_remove = False
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "@":
                    if can_access(r, c, grid):
                        grid[r][c] = "x"  # removed
                        remove_count += 1
                        can_remove = True
    return remove_count


if __name__ == "__main__":
    file = "inputs/input.txt"
    print(f"Number of rolls of paper can be accessed by forklift: {part_one(file)}")
    print(f"Number of rolls of paper can be removed by Elves and forklifts: {part_one(file)}")
