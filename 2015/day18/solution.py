def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_grid(raw_input: str) -> list:
    grid = []
    for line in raw_input.split("\n"):
        grid.append(list(line))
    return grid


def next_step(grid: list, corner_on=False) -> list:
    # Previous light ON stays on when 2 or 3 neighbours are on, otherwise turns off
    # Previous light OFF turns on when exactly 3 neighbours are on, otherwise stays off
    R = len(grid)
    C = len(grid[0])
    next_state = [['' for _ in range(C)] for _ in range(R)]

    if corner_on:
        grid[0][0] = grid[0][C - 1] = grid[R - 1][0] = grid[R - 1][C - 1] = "#"

    def count_neighbour_lights(_r: int, _c: int) -> int:
        count = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = _r + dr, _c + dc
            if 0 <= nr < R and 0 <= nc < C:
                count += 1 if grid[nr][nc] == "#" else 0
        return count

    for r in range(R):
        for c in range(C):
            n = count_neighbour_lights(r, c)
            if grid[r][c] == "#":
                next_state[r][c] = "#" if n == 2 or n == 3 else "."
            else:
                next_state[r][c] = "#" if n == 3 else "."

    if corner_on:
        next_state[0][0] = next_state[0][C - 1] = next_state[R - 1][0] = next_state[R - 1][C - 1] = "#"

    return next_state


def count_lights(raw_input: str, steps: int, corner_on=False) -> int:
    grid = parse_grid(raw_input)
    for i in range(steps):
        new_state = next_step(grid, corner_on)
        grid = new_state
    return sum(row.count("#") for row in grid)


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"Number of lights on after 100 steps: {count_lights(input, 100)}")
    print(f"Number of lights on after 100 steps with stuck corner lights: {count_lights(input, 100, True)}")
