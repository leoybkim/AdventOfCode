import heapq
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[str]]:
    maze = []
    for line in raw_data.split("\n"):
        maze.append(list(line))
    return maze


def dijkstra(maze: List[List[str]], init: tuple[int, int], goal: tuple[int, int]) -> int:
    """
    Return the lowest score possible for solving the maze.
    Each step forward adds 1 score and a turn adds additional 1000 score.
    @param maze: Map of the maze
    @param init: Coordinate of the starting cell
    @param goal: Coordinate of the destination cell
    @return: Return the lowest score if the maze can be solved, otherwise return -1
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # down, up, left, right
    visited = [[[False for _ in range(4)] for _ in range(len(maze[0]))] for _ in range(len(maze))]  # dir, r, c
    distances = [[[float("inf") for _ in range(4)] for _ in range(len(maze[0]))] for _ in range(len(maze))]  # dir, r, c
    r, c = init
    pq = [(0, r, c, directions[3])]  # (cost, row, column, direction) Start facing east

    distances[r][c][3] = 0

    def in_bound(row: int, column: int) -> bool:
        return 0 <= row < len(maze) and 0 <= column < len(maze[0])

    while pq:
        # Pop and return smallest item from heap, maintaining the heap invariant
        cur_cost, cur_r, cur_c, cur_dir = heapq.heappop(pq)

        # Maze is solved, return the cost
        if (cur_r, cur_c) == goal:
            return cur_cost

        visited[cur_r][cur_c][directions.index(cur_dir)] = True

        for i, (dr, dc) in enumerate(directions):
            nr, nc = cur_r + dr, cur_c + dc
            if in_bound(nr, nc) and not visited[nr][nc][i] and maze[nr][nc] == "." or maze[nr][nc] == "E":
                new_cost = cur_cost + (1 if cur_dir == (dr, dc) else 1001)
                if new_cost < distances[nr][nc][i]:
                    distances[nr][nc][i] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc, (dr, dc)))
    return -1


def solve_maze(raw_file: str) -> int:
    maze = format_data(raw_file)
    start = end = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == "S":
                start = (r, c)
            if maze[r][c] == "E":
                end = (r, c)

    return dijkstra(maze, start, end)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Lowest score possible: {solve_maze(file)}")
