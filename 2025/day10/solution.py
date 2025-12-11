import re
from collections import deque

from utils.input_reader import read_file


class Requirement:
    def __init__(self, light: str, buttons: list[tuple[int, ...]], joltage: list[int]):
        self.light = light
        self.buttons = buttons
        self.joltage = joltage


def parse_data(data: str) -> list[Requirement]:
    reqs = []
    pattern = re.compile(
        r"^\[(?P<light>[.#]+)]\s+(?P<buttons>(?:\(\d+(?:,\d+)*\)\s*)+)\s+\{(?P<joltage>\d+(?:,\d+)*)}\s*$")
    for line in data.splitlines():
        m = pattern.match(line)
        light = m.group("light")
        temp_buttons = re.findall(r"\(([^)]*)\)", m.group("buttons"))
        buttons = [tuple(int(x) for x in part.split(",") if x) for part in temp_buttons]
        joltage = [int(x) for x in m.group("joltage").split(",")]
        reqs.append(Requirement(light, buttons, joltage))
    return reqs


def light_str_to_mask(s: str) -> int:
    # bitmask '.' as 0 and '#' as 1
    mask = 0
    n = len(s)
    for i, c in enumerate(s):
        if c == "#":
            mask |= 1 << (n - 1 - i)
    return mask


def buttons_to_mask(buttons: tuple[int, ...], n: int) -> int:
    mask = 0
    for button in buttons:
        mask |= 1 << (n - 1 - button)
    return mask


def min_presses(target_mask: int, button_masks: list[int]) -> int:
    # Finds the minimum number of button presses to reach the target mask using BFS

    # Total # of possible states: 2^(mask length)
    total_states = 1 << max(target_mask.bit_length(), max((m.bit_length() for m in button_masks), default=0))
    visited = [False] * total_states

    # Initialize the BFS queue with the starting state and the number of presses
    q = deque([(0, 0)])
    visited[0] = True
    while q:
        state, press = q.popleft()
        for button_mask in button_masks:
            # Calculate the next state by applying XOR with the button mask which flips the state of the light by toggling
            next_state = state ^ button_mask
            if not visited[next_state]:
                if next_state == target_mask:
                    return press + 1
                visited[next_state] = True
                q.append((next_state, press + 1))

    # Should never reach here
    return -1


def light_count_press(req: Requirement) -> int:
    n = len(req.light)
    target_mask = light_str_to_mask(req.light)
    button_masks = [buttons_to_mask(buttons, n) for buttons in req.buttons]
    presses = min_presses(target_mask, button_masks)
    return presses


def joltage_count_press(req: Requirement) -> int:
    ...


def part_one(data: str):
    reqs: list[Requirement] = parse_data(data)
    presses = 0
    for req in reqs:
        presses += light_count_press(req)
    return presses


def part_two(data: str):
    reqs: list[Requirement] = parse_data(data)
    presses = 0
    for req in reqs:
        presses += joltage_count_press(req)
    return presses


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Fewest button presses required to configure the light: {part_one(file)}")
    print(f"Fewest button presses required to configure the joltage: {part_two(file)}")
