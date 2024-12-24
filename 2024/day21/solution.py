import heapq
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[str]:
    codes = []
    for line in raw_data.split("\n"):
        codes.append(line.strip())
    return codes


def dijkstra(grid: List[List[str]], init: tuple[int, int], goal: tuple[int, int]) -> List[str]:
    """
    Dijkstra's algorithm to find the shortest path between two cells where turning is discouraged
    @param grid: Map
    @param init: Initial cell coordinate
    @param goal: Goal cell coordinate
    @return: Directional symbols that creates shortest path from initial cell to goal cell
    """
    directions = [(-1, 0, "^"), (1, 0, "v"), (0, -1, "<"), (0, 1, ">")]
    R, C = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]
    costs = [[[float('inf') for _ in range(4)] for _ in range(C)] for _ in range(R)]
    init_r, init_c = init
    pq = [(0, init_r, init_c, 3, [])]  # cost, row, column, direction, path
    costs[init_r][init_c][3] = 0

    def in_bound(r: int, c: int) -> bool:
        return 0 <= r < R and 0 <= c < C

    while pq:
        cur_cost, cur_r, cur_c, cur_dir, cur_path = heapq.heappop(pq)

        if (cur_r, cur_c) == goal:
            return cur_path

        visited[cur_r][cur_c][cur_dir] = True

        for i, (dr, dc, symbol) in enumerate(directions):
            nr, nc = cur_r + dr, cur_c + dc
            if in_bound(nr, nc) and not visited[nr][nc][i] and grid[nr][nc] is not None:
                new_cost = cur_cost + (1 if cur_dir == i else 1001)  # Discourage turning
                if new_cost < costs[nr][nc][i]:
                    costs[nr][nc][i] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc, i, cur_path + [symbol]))


def find_coord(grid: List[List[str]], c: str) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                return i, j


def shortest_sequence(code: str) -> int:
    numeric_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
    directional_keypad = [[None, "^", "A"], ["<", "v", ">"]]

    # numeric keypad to directional keypad
    init = find_coord(numeric_keypad, "A")  # Start at Button A
    path = []
    for c in code:
        goal = find_coord(numeric_keypad, c)
        path += dijkstra(numeric_keypad, init, goal) + ["A"]
        init = goal

    # directional keypad to robot 1 directional keypad
    init = find_coord(directional_keypad, "A")  # Start at Button A
    robot1_path = []
    for c in path:
        goal = find_coord(directional_keypad, c)
        robot1_path += dijkstra(directional_keypad, init, goal) + ["A"]
        init = goal

    # robot 1 directional keypad to robot 2 directional keypad
    init = find_coord(directional_keypad, "A")  # Start at Button A
    robot2_path = []
    for c in robot1_path:
        goal = find_coord(directional_keypad, c)
        robot2_path += dijkstra(directional_keypad, init, goal) + ["A"]
        init = goal

    return len(robot2_path)


def total_complexities(raw_input: str) -> int:
    codes = format_data(raw_input)

    total = 0
    for code in codes:
        total += shortest_sequence(code) * int(code.split("A")[0])
    return total


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Sum of the complexities: {total_complexities(file)}")
