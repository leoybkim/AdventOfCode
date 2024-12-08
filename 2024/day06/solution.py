import copy
from collections import defaultdict
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[str]]:
    layout = []
    for line in raw_data.split():
        layout.append(list(line))
    return layout


class Map:
    def __init__(self, raw_input):
        self.layout = format_data(raw_input)
        self.guard_format = [">", "v", "<", "^"]
        self.path = []
        self.visited = defaultdict(int)
        self.is_cycle = False
        self.start_r, self.start_c, self.start_o = self.init_starting_position()

    def init_starting_position(self):
        cur_r, cur_c, orientation = None, None, None
        for r in range(len(self.layout)):
            for c in range(len(self.layout[0])):
                if self.layout[r][c] in self.guard_format:
                    orientation = self.guard_format.index(self.layout[r][c])
                    cur_r = r
                    cur_c = c

        return cur_r, cur_c, orientation

    def row_count(self):
        return len(self.layout)

    def column_count(self):
        return len(self.layout[0])

    def set(self, r, c, o, value):
        self.layout[r][c] = value

        # Check if this cell has been visited before with the same orientation more than once
        if self.visited[(r, c, o)] > 1:
            self.is_cycle = True
        self.visited[(r, c, o)] += 1

    def get(self, r, c):
        return self.layout[r][c]

    def get_starting_position(self):
        return self.start_r, self.start_c, self.start_o


def walk(m: Map):
    R, C = m.row_count(), m.column_count()
    cur_r, cur_c, orientation = m.get_starting_position()
    out_of_bound = False

    while not out_of_bound and not m.is_cycle:
        m.set(cur_r, cur_c, orientation, "X")
        next_r = cur_r
        next_c = cur_c
        if m.guard_format[orientation] == ">":
            next_c += 1
        if m.guard_format[orientation] == "v":
            next_r += 1
        if m.guard_format[orientation] == "<":
            next_c -= 1
        if m.guard_format[orientation] == "^":
            next_r -= 1

        if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
            out_of_bound = True
        elif m.get(next_r, next_c) == "#":
            orientation += 1
            orientation %= len(m.guard_format)
        else:
            cur_r, cur_c = next_r, next_c


def num_guard_positions(raw_file: str) -> int:
    m = Map(raw_file)
    walk(m)
    positions = 0
    for r in range(m.row_count()):
        for c in range(m.column_count()):
            if m.get(r, c) == "X":
                positions += 1
    return positions


def num_obstruction_positions(raw_file: str) -> int:
    """
    Follow the X in the map.
    For every position in the path, try to place obstruction ahead and check if that creates a cycle.
    Cycle happens when same path is repeated more than once.
    This can be deduced when two cells in the grid is repeated in same sequence.
    """
    m = Map(raw_file)

    R, C = m.row_count(), m.column_count()
    cur_r, cur_c, orientation = m.get_starting_position()
    out_of_bound = False
    obstruction_pos = set()

    while not out_of_bound:
        m_clone = copy.deepcopy(m)  # Create a copy of the current map
        next_r = cur_r
        next_c = cur_c
        if m.guard_format[orientation] == ">":
            next_c += 1
        if m.guard_format[orientation] == "v":
            next_r += 1
        if m.guard_format[orientation] == "<":
            next_c -= 1
        if m.guard_format[orientation] == "^":
            next_r -= 1

        if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
            out_of_bound = True
        elif m.get(next_r, next_c) == "#":
            orientation += 1
            orientation %= len(m.guard_format)
        else:
            m_clone.set(next_r, next_c, orientation, "#")  # Set up a potential obstruction
            walk(m_clone)  # Test the path with new obstruction
            if m_clone.is_cycle:
                obstruction_pos.add((next_r, next_c))
            cur_r, cur_c = next_r, next_c

    return len(obstruction_pos)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of distinct position of the guard: {num_guard_positions(file)}")
    print(f"Number of distinct position of the obstruction: {num_obstruction_positions(file)}")
