import re
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List:
    robots = []
    parser = re.compile(r"p=(\d+),(\d+)\sv=(-?\d+),(-?\d+)")
    for line in raw_data.split("\n"):
        m = parser.match(line)
        robot = {
            "position": (int(m.group(1)), int(m.group(2))),
            "velocity": (int(m.group(3)), int(m.group(4)))
        }
        robots.append(robot)
    return robots


def safety_factor(raw_input: str, W=101, H=103, seconds=100) -> int:
    robots = format_data(raw_input)

    m_W = W // 2
    m_H = H // 2
    q1 = q2 = q3 = q4 = 0

    # Update robot positions
    for robot in robots:
        robot["position"] = ((robot["position"][0] + seconds * robot["velocity"][0]) % W,
                             (robot["position"][1] + seconds * robot["velocity"][1]) % H)
        q1 += 0 <= robot["position"][0] < m_W and 0 <= robot["position"][1] < m_H
        q2 += m_W < robot["position"][0] < W and 0 <= robot["position"][1] < m_H
        q3 += 0 <= robot["position"][0] < m_W and m_H < robot["position"][1] < H
        q4 += m_W < robot["position"][0] < W and m_H < robot["position"][1] < H
    return q1 * q2 * q3 * q4


def find_tree(raw_input: str, W=101, H=103, seconds=100) -> int:
    robots = format_data(raw_input)

    for s in range(1, seconds):
        grid = [["." for _ in range(W)] for _ in range(H)]
        for robot in robots:
            robot["position"] = ((robot["position"][0] + robot["velocity"][0]) % W,
                                 (robot["position"][1] + robot["velocity"][1]) % H)
            grid[robot["position"][1]][robot["position"][0]] = "@"

        # Print the grid
        if any("@@@@@@@@@@@@@@@@@@" in "".join(row) for row in grid):
            for row in range(H):
                print("".join(grid[row]))
            return s


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Safety factor after 100 seconds: {safety_factor(file)}")
    print(f"Find Christmas tree: {find_tree(file, seconds=20000)}")
