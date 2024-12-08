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


def total_nodes(raw_file: str, loop=False) -> int:
    layout = format_data(raw_file)
    R = len(layout)
    C = len(layout[0])
    antennas = defaultdict(list)
    for r in range(R):
        for c in range(C):
            if layout[r][c].isalnum():
                antennas[layout[r][c]].append((r, c))

    unique_nodes = set()
    for x in antennas:
        cells = antennas[x]
        pairs = set()
        for i in range(len(cells)):
            if loop:
                unique_nodes.add(cells[i])  # Part 2: Include antennas as nodes
            for j in range(i + 1, len(cells)):
                pairs.add((cells[i], cells[j]))

        for pair in pairs:
            nodes = find_nodes(pair[0], pair[1], R, C, loop)
            unique_nodes.update(nodes)  # Update the set, adding elements from the List of nodes
    return len(unique_nodes)


def find_nodes(p1: tuple[int, int], p2: tuple[int, int], R: int, C: int, loop: bool) -> List[tuple[int, int]]:
    p1y, p1x = p1
    p2y, p2x = p2
    a = (p1y - p2y) / (p1x - p2x)  # slope
    x_diff = abs(p1x - p2x)
    y_diff = abs(p1y - p2y)
    nodes = []

    l1 = True
    l2 = True

    if a >= 0:
        if p1y > p2y:
            while p1y + y_diff < R and p1x + x_diff < C and l1:
                nodes.append((p1y + y_diff, p1x + x_diff))
                p1y += y_diff
                p1x += x_diff
                l1 = loop
            while p2y - y_diff >= 0 and p2x - x_diff >= 0 and l2:
                nodes.append((p2y - y_diff, p2x - x_diff))
                p2y -= y_diff
                p2x -= x_diff
                l2 = loop
        else:
            while p1y - y_diff >= 0 and p1x - x_diff >= 0 and l1:
                nodes.append((p1y - y_diff, p1x - x_diff))
                p1y -= y_diff
                p1x -= x_diff
                l1 = loop
            while p2y + y_diff < R and p2x + x_diff < C and l2:
                nodes.append((p2y + y_diff, p2x + x_diff))
                p2y += y_diff
                p2x += x_diff
                l2 = loop
    else:
        if p1y > p2y:
            while p1y + y_diff < R and p1x - x_diff >= 0 and l1:
                nodes.append((p1y + y_diff, p1x - x_diff))
                p1y += y_diff
                p1x -= x_diff
                l1 = loop
            while p2y - y_diff >= 0 and p2x + x_diff < C and l2:
                nodes.append((p2y - y_diff, p2x + x_diff))
                p2y -= y_diff
                p2x += x_diff
                l2 = loop
        else:
            while p1y - y_diff >= 0 and p1x + x_diff < C and l1:
                nodes.append((p1y - y_diff, p1x + x_diff))
                p1y -= y_diff
                p1x += x_diff
                l1 = loop
            while p2y + y_diff < R and p2x - x_diff >= 0 and l2:
                nodes.append((p2y + y_diff, p2x - x_diff))
                p2y += y_diff
                p2x -= x_diff
                l2 = loop

    return nodes


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of unique locations containing antinodes: {total_nodes(file)}")
    print(f"Number of unique locations containing antinodes extended: {total_nodes(file, loop=True)}")