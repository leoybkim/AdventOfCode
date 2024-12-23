from collections import deque
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[str]]:
    maze = []
    for line in raw_data.split("\n"):
        maze.append(list(line))
    return maze


def in_bound(row: int, column: int, R: int, C: int) -> bool:
    return 0 <= row < R and 0 <= column < C


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # down, up, left, right


def find_cheat_cells(maze: List[List[str]]) -> List[tuple]:
    """
    Find cells in the maze that are worth exploring for cheats.
    Wall cells that are touching at least 2 walkable paths should be explored.
    @param maze: Init maze
    @return: Cheat cell coordinates
    """
    cells = []
    R, C = len(maze), len(maze[0])
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "#":
                path_count = 0
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if in_bound(nr, nc, R, C) and (maze[nr][nc] in [".", "S", "E"]):
                        path_count += 1
                if path_count >= 2:
                    cells.append((r, c))
    return cells


def bst(maze: List[List[str]], init: tuple[int, int], goal: tuple[int, int]) -> int | None:
    """
    BST maze solver
    @param maze: Map of the maze
    @param init: Coordinate of the starting cell
    @param goal: Coordinate of the destination cell
    @return: Return the minimum number of steps needed to reach the exit
    """
    R, C = len(maze), len(maze[0])
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    costs = [[float("inf") for _ in range(len(maze[0]))] for _ in range(len(maze))]
    init_r, init_c = init
    queue = deque([(0, init_r, init_c)])  # (cost, row, column)
    costs[init_r][init_c] = 0

    while queue:
        # FIFO
        cur_cost, cur_r, cur_c = queue.popleft()

        # Maze is solved; exit
        if (cur_r, cur_c) == goal:
            return cur_cost

        visited[cur_r][cur_c] = True

        for i, (dr, dc) in enumerate(DIRECTIONS):
            nr, nc = cur_r + dr, cur_c + dc
            if in_bound(nr, nc, R, C) and not visited[nr][nc] and (maze[nr][nc] == "." or maze[nr][nc] == "E"):
                new_cost = cur_cost + 1
                if new_cost < costs[nr][nc]:
                    costs[nr][nc] = new_cost
                    queue.append((new_cost, nr, nc))
    return None


def count_cheats(raw_file: str, time: int) -> int:
    maze = format_data(raw_file)
    start = end = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "S":
                start = (r, c)
            if maze[r][c] == "E":
                end = (r, c)

    best_cost = bst(maze, start, end)
    cheat_cells = find_cheat_cells(maze)

    count = 0
    for cell in cheat_cells:
        maze[cell[0]][cell[1]] = "."
        cheat_cost = bst(maze, start, end)
        maze[cell[0]][cell[1]] = "#"
        count += best_cost - cheat_cost >= time

    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of cheats that will save 100 picoseconds: {count_cheats(file, time=100)}")
