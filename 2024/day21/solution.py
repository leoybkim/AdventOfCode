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


def shortest_sequence(code: str) -> int:
    numeric_keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [None, "0", "A"]]
    directional_keypad = [[None, "^", "A"], ["<", "v", ">"]]

    # Step 1
    # numeric keypad to directional keypad
    init = find_coord(numeric_keypad, "A")  # Start at Button A
    best_numpad_paths = None
    for c in code:
        goal = find_coord(numeric_keypad, c)
        temp_paths = dijkstra(numeric_keypad, init, goal)
        init = goal
        for p in temp_paths:
            p.append("A")

        # Append the next path found to the existing paths
        if best_numpad_paths is None:
            best_numpad_paths = temp_paths
        else:
            new_paths = []
            for bp in best_numpad_paths:
                for tp in temp_paths:
                    new_paths.append(bp + tp)
            best_numpad_paths = new_paths

    # Find the shortest paths
    min_path_length = float("inf")
    for path in best_numpad_paths:
        min_path_length = min(min_path_length, len(path))
    best_numpad_paths = [path for path in best_numpad_paths if len(path) <= min_path_length]

    # Step 2
    # directional keypad to robot 1 directional keypad
    best_robot1_paths = []
    for path in best_numpad_paths:
        init = find_coord(directional_keypad, "A")  # Start at Button A
        temp_best_robot1_paths = None
        for c in path:
            goal = find_coord(directional_keypad, c)
            temp_paths = dijkstra(directional_keypad, init, goal)
            init = goal
            for p in temp_paths:
                p.append("A")

            # Append the next path found to the existing paths
            if temp_best_robot1_paths is None:
                temp_best_robot1_paths = temp_paths
            else:
                new_paths = []
                for bp in temp_best_robot1_paths:
                    for tp in temp_paths:
                        new_paths.append(bp + tp)
                temp_best_robot1_paths = new_paths

        best_robot1_paths += temp_best_robot1_paths

    # Find the shortest paths
    min_path_length = float("inf")
    for robot1_path in best_robot1_paths:
        min_path_length = min(min_path_length, len(robot1_path))

    best_robot1_paths = [path for path in best_robot1_paths if len(path) <= min_path_length]

    # Step 3
    # robot 1 directional keypad to robot 2 directional keypad
    best_robot2_paths = []
    for path in best_robot1_paths:
        init = find_coord(directional_keypad, "A")  # Start at Button A
        temp_best_robot2_paths = None
        for c in path:
            goal = find_coord(directional_keypad, c)
            temp_paths = dijkstra(directional_keypad, init, goal)
            init = goal
            for p in temp_paths:
                p.append("A")

            # Append the next path found to the existing paths
            if temp_best_robot2_paths is None:
                temp_best_robot2_paths = temp_paths
            else:
                new_paths = []
                for bp in temp_best_robot2_paths:
                    for tp in temp_paths:
                        new_paths.append(bp + tp)
                temp_best_robot2_paths = new_paths

        best_robot2_paths += temp_best_robot2_paths

    # Find the shortest paths
    min_path_length = float("inf")
    for robot2_path in best_robot2_paths:
        min_path_length = min(min_path_length, len(robot2_path))

    return min_path_length


def total_complexities(raw_input: str) -> int:
    codes = format_data(raw_input)

    total = 0
    for code in codes:
        total += shortest_sequence(code) * int(code.split("A")[0])
    return total


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Sum of the complexities: {total_complexities(file)}")
