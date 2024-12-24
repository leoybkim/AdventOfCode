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


def bfs(maze: List[List[str]], init: tuple[int, int], goal: tuple[int, int]) -> tuple[int, List[tuple[int, int]]]:
    """
    BFS maze solver
    @param maze: Map of the maze
    @param init: Coordinate of the starting cell
    @param goal: Coordinate of the destination cell
    @return: Return the minimum number of steps needed to reach the exit
    """
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # down, up, left, right
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    costs = [[float("inf") for _ in range(len(maze[0]))] for _ in range(len(maze))]
    init_r, init_c = init
    queue = deque([(0, init_r, init_c, [init])])  # (cost, row, column, path)
    costs[init_r][init_c] = 0

    def in_bound(row: int, column: int) -> bool:
        return 0 <= row < len(maze) and 0 <= column < len(maze[0])

    while queue:
        # FIFO
        cur_cost, cur_r, cur_c, cur_path = queue.popleft()

        # Maze is solved; exit
        if (cur_r, cur_c) == goal:
            return cur_cost, cur_path

        visited[cur_r][cur_c] = True

        for i, (dr, dc) in enumerate(DIRECTIONS):
            nr, nc = cur_r + dr, cur_c + dc
            if in_bound(nr, nc) and not visited[nr][nc] and (maze[nr][nc] == "." or maze[nr][nc] == "E"):
                new_cost = cur_cost + 1
                if new_cost < costs[nr][nc]:
                    costs[nr][nc] = new_cost
                    queue.append((new_cost, nr, nc, cur_path + [(nr, nc)]))


def count_cheats(raw_file: str, saved_time: int, cheat_time=2) -> int:
    maze = format_data(raw_file)
    start = end = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "S":
                start = (r, c)
            if maze[r][c] == "E":
                end = (r, c)

    best_cost, best_path = bfs(maze, start, end)
    count = 0
    path_length = len(best_path)
    # For any two points on the best path, check if they can be shortcutted through cheating
    for i in range(path_length):
        for j in range(i):
            c1, c2 = best_path[i], best_path[j]
            original_dist = i - j  # Shortest distance between the 2 cells on the proper path on maze
            manhattan_dist = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])  # Shortest manhattan distance between the 2 cells
            # Check if the two points can be met at a shorter distance with the limit of cheat time
            if manhattan_dist <= cheat_time:
                # Check if the new path is able to save more than desired amount of time
                count += original_dist - manhattan_dist >= saved_time

    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of cheats that saves 100 ps (2 ps cheat time): {count_cheats(file, saved_time=100)}")
    print(f"Number of cheats that saves 100 ps (20 ps cheat time): {count_cheats(file, saved_time=100, cheat_time=20)}")
