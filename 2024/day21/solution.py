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


def dijkstra(grid: List[List[str]], init: tuple[int, int], goal: tuple[int, int]) -> List[List[str]]:
    """
    Dijkstra's algorithm to find the shortest path between two cells where turning is discouraged
    ">^^", "^>^" and "^^>" all move to the same position but  "^>^" requires pressing more button when proxied
    @param grid: Map
    @param init: Initial cell coordinate
    @param goal: Goal cell coordinate
    @return: Directional symbols that creates shortest path from initial cell to goal cell
    """
    directions = [(-1, 0, "^", 0), (1, 0, "v", 0), (0, -1, "<", 100), (0, 1, ">", 100)]
    best_cost = float("inf")
    R, C = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]
    costs = [[[best_cost for _ in range(4)] for _ in range(C)] for _ in range(R)]
    init_r, init_c = init
    pq = [(0, init_r, init_c, -1, [])]  # cost, row, column, direction, path
    costs[init_r][init_c][-1] = 0
    best_paths = []

    def in_bound(r: int, c: int) -> bool:
        return 0 <= r < R and 0 <= c < C

    while pq:
        cur_cost, cur_r, cur_c, cur_dir, cur_path = heapq.heappop(pq)

        # Keep track of best paths
        if (cur_r, cur_c) == goal:
            if cur_cost <= best_cost:
                best_cost = cur_cost
                best_paths.append(cur_path)

        visited[cur_r][cur_c][cur_dir] = True

        for i, (dr, dc, symbol, dir_cost) in enumerate(directions):
            nr, nc = cur_r + dr, cur_c + dc
            if in_bound(nr, nc) and not visited[nr][nc][i] and grid[nr][nc] is not None:
                new_cost = cur_cost + (1 if cur_dir == i else 1001) + dir_cost  # Discourage turning
                if new_cost < costs[nr][nc][i]:
                    costs[nr][nc][i] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc, i, cur_path + [symbol]))
                elif new_cost == costs[nr][nc][i]:
                    heapq.heappush(pq, (new_cost, nr, nc, i, cur_path + [symbol]))
    return best_paths


def find_coord(grid: List[List[str]], c: str) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == c:
                return i, j


def directional_keypad_paths(parent_paths):
    directional_keypad = [[None, "^", "A"], ["<", "v", ">"]]
    best_paths = []
    for path in parent_paths:
        init = find_coord(directional_keypad, "A")  # Start at Button A
        temp_best_paths = None
        for c in path:
            goal = find_coord(directional_keypad, c)
            temp_paths = dijkstra(directional_keypad, init, goal)
            init = goal
            for p in temp_paths:
                p.append("A")

            # Append the next path found to the existing paths
            if temp_best_paths is None:
                temp_best_paths = temp_paths
            else:
                new_paths = []
                for tbp in temp_best_paths:
                    for tp in temp_paths:
                        new_paths.append(tbp + tp)
                temp_best_paths = new_paths

        best_paths += temp_best_paths

    # Find the shortest paths
    min_path_length = float("inf")
    for path in best_paths:
        min_path_length = min(min_path_length, len(path))

    best_paths = [path for path in best_paths if len(path) <= min_path_length]
    return best_paths


def shortest_sequence(code: str, count: int) -> int:
    numeric_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]

    # numeric keypad to directional keypad
    init = find_coord(numeric_keypad, "A")  # Start at Button A
    best_paths = None
    for c in code:
        goal = find_coord(numeric_keypad, c)
        temp_paths = dijkstra(numeric_keypad, init, goal)
        init = goal
        for p in temp_paths:
            p.append("A")

        # Append the next path found to the existing paths
        if best_paths is None:
            best_paths = temp_paths
        else:
            new_paths = []
            for bp in best_paths:
                for tp in temp_paths:
                    new_paths.append(bp + tp)
            best_paths = new_paths

    # Find the shortest paths
    min_path_length = float("inf")
    for path in best_paths:
        min_path_length = min(min_path_length, len(path))
    best_paths = [path for path in best_paths if len(path) <= min_path_length]

    while count > 0:
        print(count)
        best_directional_keypad_paths = directional_keypad_paths(best_paths)
        best_paths = best_directional_keypad_paths
        count -= 1

    return min(len(path) for path in best_paths)


def total_complexities(raw_input: str, count: int) -> int:
    codes = format_data(raw_input)

    total = 0
    for code in codes:
        total += shortest_sequence(code, count) * int(code.split("A")[0])
    return total


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    # print(f"Sum of the complexities: {total_complexities(file, count=2)}")
    print(f"Sum of the complexities: {total_complexities(file, count=25)}")
