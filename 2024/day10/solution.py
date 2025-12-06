from typing import List

from utils.input_reader import read_file


def format_data(raw_data: str) -> List[List[str]]:
    grid = []
    for line in raw_data.split("\n"):
        grid.append(list(line))
    return grid


def dfs_score(r, c, grid, visited, ratings=False) -> int:
    visited[r][c] = not ratings
    if grid[r][c] == 9:
        return 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    score = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not visited[nr][nc]:
            if grid[nr][nc] == grid[r][c] + 1:
                score += dfs_score(nr, nc, grid, visited, ratings=ratings)

    return score


def sum_trailhead_scores(raw_file: str, ratings=False) -> int:
    grid = format_data(raw_file)
    scores = 0
    trailheads = []
    R = len(grid)
    C = len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c].isnumeric():
                grid[r][c] = int(grid[r][c])
                if grid[r][c] == 0:
                    trailheads.append((r, c))
            else:
                grid[r][c] = None

    for trailhead in trailheads:
        visited = [[False for _ in range(C)] for _ in range(R)]
        scores += dfs_score(trailhead[0], trailhead[1], grid, visited, ratings)
    return scores


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Sum of scores of al trailheads: {sum_trailhead_scores(file)}")
    print(f"Sum of ratings of al trailheads: {sum_trailhead_scores(file, ratings=True)}")
