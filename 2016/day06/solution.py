import collections

from utils.input_reader import read_file


def corrected_message(raw_input: str, part2=False) -> str:
    messages = raw_input.split("\n")
    # transpose the rows to columns
    col_messages = [list(col) for col in zip(*messages)]
    correct = []
    for col in col_messages:
        c = sorted(collections.Counter(col).items(), key=lambda item: (item[1] if part2 else -item[1], item[0]))[0][0]
        correct.append(c)

    return "".join(correct)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"The error-corrected version of the message is {corrected_message(file)}")
    print(f"The original message using new decoding methodology is {corrected_message(file, part2=True)}")
