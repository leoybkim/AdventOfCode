from utils.input_reader import read_file


def parse_data(data: str) -> list:
    points = []
    for line in data.splitlines():
        points.append(tuple(map(int, line.split(","))))
    return points


def area(a: tuple, b: tuple) -> int:
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)


def part_one(data: str):
    points = parse_data(data)  # tuple(column, row) of red carpet locations
    max_area = float('-inf')

    n = len(points)
    for i in range(n - 1):
        for j in range(i + 1, n):
            max_area = max(max_area, area(points[i], points[j]))

    return max_area


def draw_line(grid: list[list[str]], a: tuple, b: tuple):
    # The line will always be horizontal or vertical, never diagonal
    if a[0] == b[0]:
        # horizontal
        if a[1] < b[1]:
            # draw downwards
            for i in range(a[1], b[1] + 1):
                grid[i][a[0]] = "#"
        else:
            # draw upwards
            for i in range(a[1], b[1] - 1, -1):
                grid[i][a[0]] = "#"
    else:
        # horizontal
        if a[0] < b[0]:
            # draw to the right
            for i in range(a[0], b[0] + 1):
                grid[a[1]][i] = "#"
        else:
            # draw to the left
            for i in range(a[0], b[0] - 1, -1):
                grid[a[1]][i] = "#"


def dfs(grid: list[list[str]], start: tuple[int, int]):
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Up, Down
    r, c = start
    R = len(grid)
    C = len(grid[0])
    grid[r][c] = "x"
    for dr, dc in dir:
        if 0 <= r + dr < R and 0 <= c + dc < C:
            if grid[r + dr][c + dc] != "#" and grid[r + dr][c + dc] != "x":
                # if not boundary and not visited yet
                dfs(grid, (r + dr, c + dc))


def flood_fill(grid: list[list[str]]):
    # try 4 corners in order
    R = len(grid)
    C = len(grid[0])

    if grid[0][0] != "#":
        dfs(grid, (0, 0))
    elif grid[0][C - 1] != "#":
        dfs(grid, (0, C - 1))
    elif grid[R - 1][0] != "#":
        dfs(grid, (R - 1, 0))
    elif grid[R - 1][C - 1] != "#":
        dfs(grid, (R - 1, C - 1))
    else:
        # the grid is the boundary
        return


def in_boundary(grid: list[list[str]], a: tuple, b: tuple) -> bool:
    for c in range(min(a[0], b[0]), max(a[0], b[0])):
        for r in range(min(a[1], b[1]), max(a[1], b[1])):
            if grid[r][c] == "x":
                return False
    return True

def part_two(data: str) -> int:
    points = parse_data(data)  # tuple(column, row) of red carpet locations
    max_area = float('-inf')
    n = len(points)
    R = max(points, key=lambda loc: loc[1])[1] + 1
    C = max(points, key=lambda loc: loc[0])[0] + 1
    print(R, C)
    grid = [["." for _ in range(C)] for _ in range(R)]

    print("Building the boundary")
    # Build the boundary
    start_p = points[0]
    for i in range(1, n):
        next_p = points[i]
        draw_line(grid, start_p, next_p)
        start_p = next_p

    # Complete the loop
    draw_line(grid, points[-1], points[0])
    print("Completed the loop")

    # Flood fill the outer area because it is easier to determine the outside than the inside
    flood_fill(grid)
    print("Filled grid")

    # with open("output.txt", "w") as test:
    #     for line in grid:
    #         test.write(str(line) + "\n")

    # Loop through rectangles and see if it fits in the boundary, keep the largest area
    for i in range(n - 1):
        for j in range(i + 1, n):
            if in_boundary(grid, points[i], points[j]):
                max_area = max(max_area, area(points[i], points[j]))

    return max_area


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Largest area of the rectangle: {part_one(file)}")
    print(f"Largest area of the rectangle using only red and green tiles: {part_two(file)}")
