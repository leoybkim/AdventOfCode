import copy
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str, large: bool) -> (List[List[str]], List[str]):
    """
    Read input and returns the map and robot movement directions parsed from the file.
    If large box mode, widen the map by replacing the legends with corresponding characters of double length.
    @param raw_data: Input file
    @param large: Large box mode
    @return: Map and robot directions
    """
    grid_str, moves_str = raw_data.split("\n\n")
    grid = []
    moves = []
    for line in grid_str.split():
        if large:
            temp = []
            for c in list(line):
                if c == "#":
                    temp += ["#", "#"]
                elif c == "O":
                    temp += ["[", "]"]
                elif c == ".":
                    temp += [".", "."]
                elif c == "@":
                    temp += ["@", "."]
            grid.append(temp)
        else:
            grid.append(list(line))

    for line in moves_str.split():
        moves += (list(line))
    return grid, moves


def robot_coordinate(grid: List[List[str]]) -> tuple[int, int]:
    """
    Returns the current coordinate of the robot indicated with "@"
    @param grid: Map
    @return: (row, column) coordinate of the Robot
    """
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                return r, c


def recursive_push(grid: List[List[str]], row: int, boxes: tuple[int, int], dr: int, prev: tuple[int, int] | None,
                   prev_row: List[str] | None, edge: str) -> bool:
    """
    Returns True if the boxes can be pushed at the current level
    @param grid: Temporary working copy of the map
    @param row: Current row
    @param boxes: Start and end indices of the boxes
    @param dr: Vertical direction of the robots movement
    @param prev: Start and end indices of the previous boxes
    @param prev_row: Copy of the previous row
    @param edge: "[" or "]" edge of the box being pushed
    @return: True if the boxes can be pushed, False otherwise
    """
    s, e = boxes
    temp_prev_row = grid[row].copy()
    if any(grid[row + dr][i] == "#" for i in range(s, e + 1)):
        # Wall is blocking some of the boxes, cannot push
        return False

    # Find next row of boxes, if any
    ns = ne = None
    if grid[row + dr][s] == "]":
        ns = s - 1
    else:
        for i in range(s, e + 1):
            if grid[row + dr][i] == "[":
                ns = i
                break

    if grid[row + dr][e] == "[":
        ne = e + 1
    else:
        for i in range(e, s - 1, -1):
            if grid[row + dr][i] == "]":
                ne = i
                break

    if prev is None:
        # If first iteration, replace the box position with robot and a clear space next to it
        grid[row][s:e + 1] = ["@", "."] if edge == "[" else [".", "@"]
        if edge == "[":
            grid[row - dr][s] = "."
        else:
            grid[row - dr][e] = "."
    else:
        # For all iteration > 1, replace the current rows of boxes with the previous rows of box
        # Calculate where the free space should be placed, if any, depending on the positional difference from two rows
        ps, pe = prev
        grid[row][min(ps, s):max(pe, e) + 1] = (["."] * ((ps - s) if ps > s else 0) +
                                                prev_row[ps:pe + 1] +
                                                ["."] * ((e - pe) if pe < e else 0))
    if ns is None and ne is None:
        # If there are no more boxes ahead of the current ones, do the final push and exit recursion
        grid[row + dr][s:e + 1] = temp_prev_row[s:e + 1]
        return True
    else:
        # If there are more boxes to push, continue recursion
        return recursive_push(grid, row + dr, (ns, ne), dr, (s, e), temp_prev_row, edge)


def push_boxes(grid: List[List[str]], robot: tuple[int, int], d: tuple[int, int], large: bool) -> bool:
    """
    Push the boxes by 1 cell in direction of the robots movement originating from the current position.
    When pushing larger boxes, push all boxes in the chain that are consecutively affected.
    Prevent the push if any box in the chain is blocked by a wall.
    @param grid: Map
    @param robot: Current coordinate of the robot
    @param d: Direction of the robots movement (r, c)
    @param large: Larger box mode
    @return: True if boxes were pushed, False otherwise
    """
    rr, rc = robot
    dr, dc = d
    edge = grid[rr + dr][rc]  # "0" or "[" or "]"
    s = rc - (edge == "]")
    e = rc + (edge == "[")
    if dr != 0:
        # Check if enough space vertically above or below the boxes before reaching the wall
        for r in range(rr + dr, (len(grid) - 1) if dr == 1 else 0, dr):
            if grid[r][rc] == "#":
                return False
            if grid[r][rc] == ".":
                # Shift all the boxes in the column one cell vertically in the direction
                if large:
                    # Create a copy of the current map and attempt to push boxes recursively for each row
                    # If all rows of boxes can be pushed, reassigned the edited map to the current map
                    # Otherwise, toss the temp map
                    temp = copy.deepcopy(grid)
                    if recursive_push(temp, rr + dr, (s, e), dr, None, None, edge):
                        grid.clear()
                        grid.extend(temp)
                        return True
                    else:
                        return False
                else:
                    if dr == -1:
                        for i in range(r, rr - 1):
                            grid[i][rc] = grid[i + 1][rc]
                    elif dr == 1:
                        for i in range(r, rr + 1, -1):
                            grid[i][rc] = grid[i - 1][rc]

                return True
    elif dc != 0:
        # Check if enough space horizontally left or right of the boxes before reaching the wall
        for c in range(rc + dc, (len(grid[0]) - 1) if dc == 1 else 0, dc):
            if grid[rr][c] == "#":
                return False
            if grid[rr][c] == ".":
                # Shift all the boxes in the row one cell horizontally in the direction
                if dc == -1:
                    grid[rr][c:rc] = grid[rr][c + 1:rc] + ["."]
                elif dc == 1:
                    grid[rr][rc + 1:c + 1] = ["."] + grid[rr][rc + 1:c]
                return True
    return False


def move_robot(grid: List[List[str]], moves: List[str], large: bool):
    """
    Moves the robot as indicated in the direction while pushing boxes
    @param grid: Map
    @param moves: Direction of robot movements
    @param large: Large box mode
    """
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
            elif grid[nr][nc] in ["O", "[", "]"]:
                box = grid[nr][nc]
                # Box, check if boxes can be pushed and move
                if push_boxes(grid, (rr, rc), coord[move], large):
                    if move == "^" or move == "v":
                        if box == "[":
                            grid[nr][nc + 1] = "."
                        if box == "]":
                            grid[nr][nc - 1] = "."
                    grid[rr][rc], grid[nr][nc] = ".", "@"
                    rr, rc = nr, nc
            else:
                grid[rr][rc], grid[nr][nc] = ".", "@"
                rr, rc = nr, nc


def sum_gps_coordinates(raw_input: str, large=False) -> int:
    """
    Returns the sum of all boxes' GPS coordinates.
    GPS coordinate of a box is equal to 100 x y coordinate + x coordinate where top left corner of the map is (0,0).
    @param raw_input: Input file
    @param large: Large box mode
    @return: Sum of all boxes' GPS coordinates
    """
    grid, moves = format_data(raw_input, large)
    move_robot(grid, moves, large)
    s = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == ("[" if large else "O"):
                s += (100 * r + c)

    return s


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Sum of all boxes' GPS coordinates: {sum_gps_coordinates(file)}")
    print(f"Sum of all boxes' GPS coordinates in scaled-up warehouse: {sum_gps_coordinates(file, large=True)}")
