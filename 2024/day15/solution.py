from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str, large: bool) -> (List[List[str]], List[str]):
    grid_str, moves_str = raw_data.split("\n\n")
    grid = []
    moves = []
    for line in grid_str.split():
        if large:
            temp = []
            for c in list(line):
                if c == "#":
                    temp.append("##")
                elif c == "O":
                    temp.append("[]")
                elif c == ".":
                    temp.append("..")
                elif c == "@":
                    temp.append("@.")
            grid.append(temp)
        else:
            grid.append(list(line))

    for line in moves_str.split():
        moves += (list(line))
    return grid, moves


def robot_coordinate(grid: List[List[str]]) -> tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return r, c


def push_boxes(grid: List[List[str]], robot: tuple[int, int], d: tuple[int, int]) -> bool:
    """
    Push the boxes by 1 cell in direction of the robots movement originating from the current position.
    @param grid: Map
    @param robot: Current coordinate of the robot
    @param d: Direction of the robots movement (r, c)
    @return: True if boxes were pushed, False otherwise
    """
    if d[0] == -1:
        # Check if enough space vertically above the boxes before reaching the wall
        for r in range(robot[0] - 1, 0, -1):
            if grid[r][robot[1]] == "#":
                return False
            if grid[r][robot[1]] == ".":
                # Swap the position of the first box and the first available space
                grid[r][robot[1]], grid[robot[0] - 1][robot[1]] = grid[robot[0] - 1][robot[1]], grid[r][robot[1]]
                return True
    elif d[0] == 1:
        # Check if enough space vertically below the boxes before reaching the wall
        for r in range(robot[0] + 1, len(grid) - 1, 1):
            if grid[r][robot[1]] == "#":
                return False
            if grid[r][robot[1]] == ".":
                # Swap the position of the first box and the first available space
                grid[r][robot[1]], grid[robot[0] + 1][robot[1]] = grid[robot[0] + 1][robot[1]], grid[r][robot[1]]
                return True
    elif d[1] == -1:
        # Check if enough space horizontally left of the boxes before reaching the wall
        for c in range(robot[1] - 1, 0, -1):
            if grid[robot[0]][c] == "#":
                return False
            if grid[robot[0]][c] == ".":
                # Swap the position of the first box and the first available space
                grid[robot[0]][c], grid[robot[0]][robot[1] - 1] = grid[robot[0]][robot[1] - 1], grid[robot[0]][c]
                return True
    elif d[1] == 1:
        # Check if enough space horizontally right of the boxes before reaching the wall
        for c in range(robot[1] + 1, len(grid[0]) - 1, 1):
            if grid[robot[0]][c] == "#":
                return False
            if grid[robot[0]][c] == ".":
                # Swap the position of the first box and the first available space
                grid[robot[0]][c], grid[robot[0]][robot[1] + 1] = grid[robot[0]][robot[1] + 1], grid[robot[0]][c]
                return True

    return False


def move_robot(grid: List[List[str]], moves: List[str]):
    coord = {
        "<": (0, -1),
        "^": (-1, 0),
        ">": (0, 1),
        "v": (1, 0)
    }
    rr, rc = robot_coordinate(grid)
    for move in moves:
        nr, nc = rr + coord[move][0], rc + coord[move][1]
        if 0 < nr < len(grid) - 1 and 0 < nc < len(grid[0]) - 1:  # Borders are surrounded by walls of 1 cell depth
            if grid[nr][nc] == "#":
                continue  # Wall, do nothing
            elif grid[nr][nc] == "O":
                # Box, check if boxes can be pushed and move
                if push_boxes(grid, (rr, rc), coord[move]):
                    grid[rr][rc], grid[nr][nc] = ".", "@"
                    rr, rc = nr, nc
            else:
                grid[rr][rc], grid[nr][nc] = ".", "@"
                rr, rc = nr, nc


def sum_gps_coordinates(raw_input: str, large=False) -> int:
    grid, moves = format_data(raw_input, large)
    move_robot(grid, moves)
    s = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                s += (100 * r + c)
    return s


if __name__ == "__main__":
    file = read_file("inputs/test2.txt")
    print(f"Sum of all boxes' GPS coordinates: {sum_gps_coordinates(file)}")
    print(f"Sum of all boxes' GPS coordinates in scaled-up warehouse: {sum_gps_coordinates(file, large=True)}")
