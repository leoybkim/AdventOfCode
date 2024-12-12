from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[str]]:
    grid = []
    for line in raw_data.split("\n"):
        grid.append(list(line))
    return grid


def find_perimeter(r, c, grid):
    perimeter = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != grid[r][c]:
                perimeter += 1
        else:
            perimeter += 1

    return perimeter


def dfs(r, c, grid, plant, group, visited):
    if not visited[r][c]:
        visited[r][c] = True
        group.append((r, c))
        perimeter = find_perimeter(r, c, grid)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not visited[nr][nc] and grid[nr][nc] == plant:
                perimeter += dfs(nr, nc, grid, plant, group, visited)
        return perimeter
    else:
        return 0


def total_price(raw_file: str, discount=False) -> int:
    grid = format_data(raw_file)
    R = len(grid)
    C = len(grid[0])

    visited = [[False for _ in range(C)] for _ in range(R)]
    price = 0

    for r in range(R):
        for c in range(C):
            if not visited[r][c]:
                group = []
                plant = grid[r][c]
                if not discount:
                    perimeter = dfs(r, c, grid, plant, group, visited)
                    price += len(group) * perimeter
                else:
                    pass
    return price


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total price of fencing all regions (using perimeters): {total_price(file)}")
    print(f"Total price of fencing all regions (using number of sides): {total_price(file, discount=True)}")
