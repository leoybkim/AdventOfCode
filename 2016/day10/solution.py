import functools
import re
from collections import defaultdict, deque

from utils.input_reader import read_file


def parse_instructions(raw_input: str) -> tuple[list, dict]:
    value_assignments = []
    bots = defaultdict(dict)
    for line in raw_input.split("\n"):

        if line[:5] == "value":
            match = re.match(r"value (\d+) goes to bot (\d+)", line)
            if match:
                value_assignments.append((int(match.group(2)), int(match.group(1))))  # (bot, value)
        else:
            match = re.match(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)", line)
            if match:
                # (low-recipient type, low-recipient id, high-recipient type, high-recipient id)
                bots[int(match.group(1))]["instruction"] = (match.group(2),
                                                            int(match.group(3)),
                                                            match.group(4),
                                                            int(match.group(5)))

    return value_assignments, bots


def find_bot(raw_input: str, chip1: int, chip2: int) -> int:
    chips = frozenset([chip1, chip2])
    bot_chips = defaultdict(list)
    value_assignments, bots = parse_instructions(raw_input)
    queue = deque()

    for bot, value in value_assignments:
        bot_chips[bot].append(value)
        if len(bot_chips[bot]) == 2:
            queue.append(bot)

    while queue:
        bot = queue.popleft()
        if frozenset(bot_chips[bot]) == chips:
            return bot

        # run instructions assigned to the bot
        if bot in bots:
            lower = min(bot_chips[bot])
            higher = max(bot_chips[bot])
            low_recipient_type, low_recipient, high_recipient_type, high_recipient = bots[bot]["instruction"]
            if low_recipient_type == "bot":
                bot_chips[low_recipient].append(lower)
            if high_recipient_type == "bot":
                bot_chips[high_recipient].append(higher)
            if len(bot_chips[low_recipient]) == 2:
                queue.append(low_recipient)
            if len(bot_chips[high_recipient]) == 2:
                queue.append(high_recipient)

    return -1


def output_product(raw_input: str, outputs: list) -> int:
    bot_chips = defaultdict(list)
    output_chips = {}
    value_assignments, bots = parse_instructions(raw_input)
    queue = deque()

    for bot, value in value_assignments:
        bot_chips[bot].append(value)
        if len(bot_chips[bot]) == 2:
            queue.append(bot)

    while queue:
        bot = queue.popleft()

        # run instructions assigned to the bot
        if bot in bots:
            lower = min(bot_chips[bot])
            higher = max(bot_chips[bot])
            low_recipient_type, low_recipient, high_recipient_type, high_recipient = bots[bot]["instruction"]
            if low_recipient_type == "bot":
                bot_chips[low_recipient].append(lower)
            else:
                output_chips[low_recipient] = lower
            if high_recipient_type == "bot":
                bot_chips[high_recipient].append(higher)
            else:
                output_chips[high_recipient] = higher

            if len(bot_chips[low_recipient]) == 2:
                queue.append(low_recipient)
            if len(bot_chips[high_recipient]) == 2:
                queue.append(high_recipient)

    return functools.reduce(lambda x, y: x * y, map(lambda output: output_chips[output], outputs))


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Bot responsible for comparing value 61 and value 17 microchips: bot #{find_bot(file, chip1=61, chip2=17)}")
    print(f"The product of the outputs 0, 1, 2 is: {output_product(file, [0, 1, 2])}")
