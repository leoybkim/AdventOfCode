from collections import deque
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[tuple]:
    corrupted = []
    for line in raw_data.split("\n"):
        corrupted.append(tuple(map(lambda s: int(s.strip()), reversed(line.split(",")))))
    return corrupted


def generate_maze(R: int, C: int, corrupted: List[tuple]) -> List[List[str]]:
    """
    Generate a maze with R rows, C columns and obstacles on the corrupted cells
    @param R: Number of rows
    @param C: Number of columns
    @param corrupted: List of corrupted cells
    @return: Generated maze matrix
    """
    maze = [["." for _ in range(C)] for _ in range(R)]
    for r, c in corrupted:
        maze[r][c] = "#"
    return maze


def bst(maze: List[List[str]]) -> int | None:
    """
    Simple BST maze solver where init is (0,0) and goal is (R-1, C-1)
    @param maze: Map of the maze
    @return: Return the minimum number of steps needed to reach the exit
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # down, up, left, right
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    costs = [[float("inf") for _ in range(len(maze[0]))] for _ in range(len(maze))]
    queue = deque([(0, 0, 0)])  # (cost, row, column)

    costs[0][0] = 0

    def in_bound(row: int, column: int) -> bool:
        return 0 <= row < len(maze) and 0 <= column < len(maze[0])

    while queue:
        # FIFO
        cur_cost, cur_r, cur_c = queue.popleft()

        # Maze is solved; exit
        if (cur_r, cur_c) == (len(maze) - 1, len(maze[0]) - 1):
            return cur_cost

        visited[cur_r][cur_c] = True

        for i, (dr, dc) in enumerate(directions):
            nr, nc = cur_r + dr, cur_c + dc
            if in_bound(nr, nc) and not visited[nr][nc] and maze[nr][nc] == ".":
                new_cost = cur_cost + 1
                if new_cost < costs[nr][nc]:
                    costs[nr][nc] = new_cost
                    queue.append((new_cost, nr, nc))
    return None


def solve_maze(raw_file: str, R=71, C=71, I=1024, most_corrupted=False) -> int | tuple:
    corrupted = format_data(raw_file)
    if most_corrupted:
        i = len(corrupted)
        maze = generate_maze(R, C, corrupted[:i])
        while bst(maze) is None:
            i -= 1
            maze = generate_maze(R, C, corrupted[:i])

        last_corrupted = corrupted[i]
        return tuple(reversed(last_corrupted))
    else:
        return bst(generate_maze(R, C, corrupted[:I]))


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Value of the program output: {solve_maze(file)}")
    print(f"Coordinate of the first byte that will prevent reaching exit: {solve_maze(file, most_corrupted=True)}")
