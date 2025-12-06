from re import match

from utils.input_reader import read_file

# Message on ticker tape
hints = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def parse_info(raw_input: str) -> dict:
    """
    Returns the parsed information about each aunt Sue
    :param raw_input: contains description for each aunt Sue
    :return: list of aunt Sue properties in a dictionary
    """
    aunts = {}
    pattern = r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)"
    for line in raw_input.split("\n"):
        m = match(pattern, line)
        aunts[m.group(1)] = {
            m.group(2): int(m.group(3)),
            m.group(4): int(m.group(5)),
            m.group(6): int(m.group(7))
        }
    return aunts


def find_aunt_sue(raw_input: str, adjust_readings=False) -> int:
    aunts = parse_info(raw_input)
    for n in aunts:
        candidate = True
        for feature, value in aunts[n].items():
            if feature in hints:
                if adjust_readings:
                    if ((feature in ["cats", "trees"] and hints[feature] >= value) or
                            (feature in ["pomeranians", "goldfish"] and hints[feature] <= value) or
                            (feature not in ["cats", "trees", "pomeranians", "goldfish"] and hints[feature] != value)):
                        candidate = False
                        break
                else:
                    if hints[feature] != value:
                        candidate = False
                        break
        if candidate:
            return int(n)
    return None


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Aunt Sue # that got you the gift is: {find_aunt_sue(file)}")
    print(f"Aunt Sue # that got you the gift after adjusting for bad readings: {find_aunt_sue(file, True)}")
