from collections import defaultdict
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[str]]:
    grid = []
    for line in raw_data.split("\n"):
        grid.append(list(line))
    return grid


def find_perimeter(r: int, c: int, grid: List[List[str]], perimeter: dict):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != grid[r][c]:
                perimeter[dr, dc].append((r, c))
        else:
            perimeter[dr, dc].append((r, c))


def dfs(r: int, c: int, grid: List[List[str]], plant: str,
        area: List[tuple], perimeter: dict, visited: List[List[bool]]):
    if not visited[r][c]:
        visited[r][c] = True
        area.append((r, c))
        find_perimeter(r, c, grid, perimeter)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not visited[nr][nc] and grid[nr][nc] == plant:
                dfs(nr, nc, grid, plant, area, perimeter, visited)


def count_sides(perimeter: dict) -> int:
    sides = 0
    for (nr, nc) in perimeter:
        cells = sorted(perimeter[(nr, nc)])
        if nc == 0:
            # Top or bottom side checks
            sr = None
            sc = None
            for cell in cells:
                if sr != cell[0]:
                    sr = cell[0]
                    sides += 1  # different row
                elif sc is not None and abs(cell[1] - sc) > 1:
                    sides += 1  # gaps
                sc = cell[1]
        cells = sorted(perimeter[(nr, nc)], key=lambda point: (point[1], point[0]))
        if nr == 0:
            # Left or right side checks
            sr = None
            sc = None
            for cell in cells:
                if sc != cell[1]:
                    sc = cell[1]
                    sides += 1  # different column
                elif sr is not None and abs(cell[0] - sr) > 1:
                    sides += 1  # gaps
                sr = cell[0]
    return sides


def total_price(raw_file: str, discount=False) -> int:
    grid = format_data(raw_file)
    R = len(grid)
    C = len(grid[0])

    visited = [[False for _ in range(C)] for _ in range(R)]
    price = 0
    for r in range(R):
        for c in range(C):
            if not visited[r][c]:
                area = []
                perimeter = defaultdict(list)
                plant = grid[r][c]
                dfs(r, c, grid, plant, area, perimeter, visited)
                if discount:
                    price += len(area) * count_sides(perimeter)
                else:
                    price += len(area) * sum(len(side) for side in perimeter.values())

    return price


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total price of fencing all regions (using perimeters): {total_price(file)}")
    print(f"Total price of fencing all regions (using number of sides): {total_price(file, discount=True)}")
