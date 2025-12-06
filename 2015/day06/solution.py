from re import match

from utils.input_reader import read_file


def format_data(raw_input: str) -> list[tuple]:
    data = []
    pattern = r"(turn on|turn off|toggle)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)"
    for line in raw_input.split("\n"):
        m = match(pattern, line)
        operation = m.group(1)
        x1, y1, x2, y2 = map(int, m.groups()[1:])
        data.append((operation, (x1, y1), (x2, y2)))
    return data


def count_lit_light(raw_input: str, brightness=False) -> int:
    data = format_data(raw_input)
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for operation, start, end in data:
        for r in range(start[0], end[0] + 1):
            for c in range(start[1], end[1] + 1):
                if brightness:
                    if operation == "turn on":
                        lights[r][c] += 1
                    elif operation == "turn off":
                        if lights[r][c] > 0:
                            lights[r][c] -= 1
                    elif operation == "toggle":
                        lights[r][c] += 2
                else:
                    if operation == "turn on":
                        lights[r][c] = 1
                    elif operation == "turn off":
                        lights[r][c] = 0
                    elif operation == "toggle":
                        lights[r][c] = 0 if lights[r][c] else 1
    return sum(light for row in lights for light in row)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of lit lights: {count_lit_light(file)}")
    print(f"Total brightness of the lights: {count_lit_light(file, brightness=True)}")
