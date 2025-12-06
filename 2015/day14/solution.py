from re import match
from typing import List

from utils.input_reader import read_file


def parse_info(raw_input: str) -> List[tuple[str, int, int, int]]:
    """
    Returns the parsed information from the raindeer stats
    :param raw_input: raw paragraph that contains all the raindeer stats
    :return: list of individual raindeer stat in a tuple (name, speed, duration, rest)
    """
    stats = []
    pattern = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    for line in raw_input.split("\n"):
        m = match(pattern, line)
        deer = m.group(1)
        speed = m.group(2)
        duration = m.group(3)
        rest = m.group(4)
        stats.append((deer, int(speed), int(duration), int(rest)))
    return stats


def winning_raindeer_distance(raw_input: str, seconds: int) -> int:
    stats = parse_info(raw_input)
    max_distance = float("-inf")
    for stat in stats:
        _, speed, duration, rest = stat
        distance = 0
        while seconds > 0:
            seconds -= duration
            distance += speed * duration
            seconds -= rest
        max_distance = max(max_distance, distance)
    return max_distance


def calculate_distance(seconds: int, speed: int, duration: int, rest: int) -> int:
    period = duration + rest
    if seconds <= duration:
        return seconds * speed
    else:
        quotient = seconds // period
        remainder = seconds - (quotient * period)
        if remainder > duration:
            return (quotient + 1) * speed * duration
        else:
            return (quotient * speed * duration) + (speed * remainder)


def winning_raindeer_points(raw_input: str, seconds: int) -> int:
    stats = parse_info(raw_input)
    deers = {
        name: [speed, duration, rest, 0] for name, speed, duration, rest in stats
    }  # [speed, duration, rest, points]
    max_distance = float("-inf")
    leads = set()  # multiple reindeer can tie the lead
    s = 0
    while s < seconds:
        s += 1
        for deer, [speed, duration, rest, _] in deers.items():
            distance = calculate_distance(s, speed, duration, rest)
            if not leads:
                leads.add(deer)
            elif distance > max_distance:
                leads = {deer}
            elif distance == max_distance:
                leads.add(deer)
            max_distance = max(max_distance, distance)

        for lead in leads:
            deers[lead][3] += 1  # add point to the leading reindeer(s)

        points = []
        for lead in leads:
            points.append(deers[lead][3])

    return max(deers[deer][3] for deer in deers)  # max point


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Winning raindeer distance after 2503 seconds: {winning_raindeer_distance(file, 2503)}")
    print(f"Winning raindeer points after 2503 seconds: {winning_raindeer_points(file, 2503)}")
