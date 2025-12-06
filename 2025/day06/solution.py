import math
from itertools import zip_longest

from utils.input_reader import read_file


def parsed_data(data: str) -> tuple[list, str]:
    homework = data.splitlines()
    variables = homework[:len(homework) - 1]
    operators = homework[-1]
    return variables, operators


def part_one(data: str) -> int:
    variables, operators = parsed_data(data)
    variables = [list(map(int, temp.split())) for temp in variables]
    pivoted = list(zip(*variables))
    answers = []
    for i, ops in enumerate(operators.split()):
        if ops == "*":
            answers.append(math.prod(list(map(int, pivoted[i]))))
        elif ops == "+":
            answers.append(sum(list(map(int, pivoted[i]))))

    return sum(answers)


def calculate_group(op: str, nums: list) -> int:
    if not nums:
        return 0
    if op == "*":
        return math.prod(nums)
    elif op == "+":
        return sum(nums)
    return 0


def part_two(data: str) -> int:
    variables, operators = parsed_data(data)
    pivoted = list(zip_longest(*variables, fillvalue=""))
    max_length = max(len(v) for v in variables)
    operators = operators.ljust(max_length)  # match the operation to the longest number

    answers = []
    current_op = None
    accumulated = []
    for i in range(len(operators)):
        num_str = "".join(pivoted[i])
        if not num_str.strip():
            continue
        if operators[i] == "*" or operators[i] == "+":
            if not current_op:
                current_op = operators[i]
            else:
                answers.append(calculate_group(current_op, accumulated))
                current_op = operators[i]
                accumulated = []
        accumulated.append(int(num_str))

    # handle last accumulated numbers
    if current_op:
        answers.append(calculate_group(current_op, accumulated))

    return sum(answers)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Grand total of answers: {part_one(file)}")
    print(f"Grand total of answers reading right-to-left by column: {part_two(file)}")
