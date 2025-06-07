from itertools import permutations
from re import match
from typing import List


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_info(raw_input: str) -> List[tuple[str, str, int]]:
    """
    Returns the parsed information from the happiness
    :param raw_input: raw paragraph that contains all the happiness change rule
    :return: list of individual rule in a tuple where the first two values contain the names of people sitting next to each other.
    The third value represents the happiness change from the first person from the result of seating arrangement.
    """
    rules = []
    pattern = r"(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)."
    for line in raw_input.split("\n"):
        m = match(pattern, line)
        name1 = m.group(1)
        name2 = m.group(4)
        operation = m.group(2)  # lose or gain
        units = m.group(3)
        rules.append((name1, name2, -int(units) if operation == "lose" else int(units)))
    return rules


def happiness_change(raw_input: str, include_self=False) -> int:
    rules = parse_info(raw_input)
    attendees = set()  # unique individuals participating in the seating arrangement
    for rule in rules:
        attendees.add(rule[0])
        attendees.add(rule[1])

    if include_self:
        me = "Leo"
        for attendee in attendees:
            rules.append((attendee, me, 0))
            rules.append((me, attendee, 0))
        attendees.add(me)

    attendees_list = list(attendees)
    attendees_map = {name: i for i, name in enumerate(attendees_list)}
    rule_map = [[None for _ in attendees_list] for _ in attendees_list]
    for rule in rules:
        i = attendees_map[rule[0]]
        j = attendees_map[rule[1]]
        rule_map[i][j] = rule[2]

    max_happiness = float("-inf")
    seatings = []
    for perm in permutations(attendees_list[1:]):
        seatings.append([attendees_list[0]] + list(perm))

    for seating in seatings:
        happiness = 0
        for i, name in enumerate(seating):
            if i == len(seating) - 1:
                happiness += rule_map[attendees_map[seating[i]]][attendees_map[seating[0]]]
                happiness += rule_map[attendees_map[seating[i]]][attendees_map[seating[i - 1]]]
            else:
                happiness += rule_map[attendees_map[seating[i]]][attendees_map[seating[i + 1]]]
                happiness += rule_map[attendees_map[seating[i]]][attendees_map[seating[i - 1]]]
        max_happiness = max(happiness, max_happiness)

    return max_happiness


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"Total happiness for optimal seating arrangement: {happiness_change(input)}")
    print(f"Total happiness for optimal seating arrangement including yourself: {happiness_change(input, True)}")
