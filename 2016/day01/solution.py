import re
from collections import defaultdict


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_instructions(raw_input: str) -> list:
    instructions = []
    for i in raw_input.split(","):
        match = re.match(r"([RL])(\d+)", i.strip())
        if match:
            instructions.append((match.group(1), int(match.group(2))))

    return instructions


def find_distance(raw_input: str) -> int:
    instructions = parse_instructions(raw_input)
    orientation = ["N", "E", "S", "W"]
    orientation_idx = 0
    x = y = 0  # starting position

    for instruction in instructions:
        direction, move = instruction
        # when instructed to turn right, orientation increments one index
        # when instructed to move left, orientation decrements one index
        # use modulo 4 to calculate increment/decrement to avoid going out of bounds
        next_orientation_idx = (orientation_idx + 1) % 4 if direction == "R" else (orientation_idx - 1) % 4
        match orientation[next_orientation_idx]:
            case "N":
                y += move
            case "E":
                x += move
            case "S":
                y -= move
            case "W":
                x -= move
        orientation_idx = next_orientation_idx
    return abs(x) + abs(y)


def find_visited_location(raw_input: str) -> int:
    instructions = parse_instructions(raw_input)
    orientation = ["N", "E", "S", "W"]
    orientation_idx = 0
    x = y = 0  # starting position
    visited = defaultdict(bool)
    visited[(x, y)] = True

    def travel_x(cur_x, cur_y, next_x):
        if cur_x < next_x:
            for _x in range(cur_x + 1, next_x + 1):
                if visited[(_x, cur_y)]:
                    return _x, cur_y
                visited[(_x, cur_y)] = True

        if cur_x > next_x:
            for _x in range(cur_x - 1, next_x - 1, -1):
                if visited[(_x, cur_y)]:
                    return _x, cur_y
                visited[(_x, cur_y)] = True

        return None, None

    def travel_y(cur_x, cur_y, next_y):
        if cur_y < next_y:
            for _y in range(cur_y + 1, next_y + 1):
                if visited[(cur_x, _y)]:
                    return cur_x, _y
                visited[(cur_x, _y)] = True

        if cur_y > next_y:
            for _y in range(cur_y - 1, next_y - 1, -1):
                if visited[(cur_x, _y)]:
                    return cur_x, _y
                visited[(cur_x, _y)] = True

        return None, None

    _x = _y = None
    for instruction in instructions:
        direction, move = instruction
        # when instructed to turn right, orientation increments one index
        # when instructed to move left, orientation decrements one index
        # use modulo 4 to calculate increment/decrement to avoid going out of bounds
        next_orientation_idx = (orientation_idx + 1) % 4 if direction == "R" else (orientation_idx - 1) % 4
        match orientation[next_orientation_idx]:
            case "N":
                _x, _y = travel_y(x, y, y + move)
                y += move
            case "E":
                _x, _y = travel_x(x, y, x + move)
                x += move
            case "S":
                _x, _y = travel_y(x, y, y - move)
                y -= move
            case "W":
                _x, _y = travel_x(x, y, x - move)
                x -= move
        if _x is not None and _y is not None:
            return abs(_x) + abs(_y)
        orientation_idx = next_orientation_idx
    return -1  # not found visited location


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Easter Bunny HQ is {find_distance(file)} blocks away.")
    print(f"First location you visit twice is {find_visited_location(file)} blocks away.")
