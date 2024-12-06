from typing import List


def read_file(input_file_path: str) -> str:
    with  open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[str]]:
    layout = []
    for line in raw_data.split():
        layout.append(list(line))
    return layout


def num_distinct_positions(raw_input: str) -> int:
    layout = format_data(raw_input)
    guard_format = [">", "v", "<", "^"]
    R = len(layout)
    C = len(layout[0])
    cur_r = None
    cur_c = None
    orientation = None
    for r in range(R):
        for c in range(C):
            if layout[r][c] in guard_format:
                orientation = guard_format.index(layout[r][c])
                cur_r = r
                cur_c = c
    num = 0
    out_of_bound = False
    while not out_of_bound:
        layout[cur_r][cur_c] = "X"
        next_r = cur_r
        next_c = cur_c
        if guard_format[orientation] == ">":
            next_c += 1
        if guard_format[orientation] == "v":
            next_r += 1
        if guard_format[orientation] == "<":
            next_c -= 1
        if guard_format[orientation] == "^":
            next_r -= 1

        if next_r < 0 or next_c < 0 or next_r >= R or next_c >= C:
            out_of_bound = True
        elif layout[next_r][next_c] == "#":
            orientation += 1
            orientation %= 4
        else:
            cur_r, cur_c = next_r, next_c

    for r in range(R):
        for c in range(C):
            if layout[r][c] == "X":
                num += 1
    return num


if __name__ == "__main__":
    file = read_file("input.txt")
    print(f"Number of distinct position of the guard: {num_distinct_positions(file)}")
