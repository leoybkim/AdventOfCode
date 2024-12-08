from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[int]]:
    equations = []
    for line in raw_data.split("\n"):
        parts = line.split(":")
        test = int(parts[0])
        inputs = list(map(int, parts[1].split()))
        equations.append([test, inputs])
    return equations


def generate(operators: List[List[str]], loop: int, allow_concat: bool) -> List[List[str]]:
    if loop > 0:
        new_operators = []
        if len(operators) == 0:
            new_operators.append(["+"])
            new_operators.append(["*"])
            if allow_concat:
                new_operators.append(["||"])
        else:
            for item in operators:
                new_operators.append(item + ["+"])
                new_operators.append(item + ["*"])
                if allow_concat:
                    new_operators.append(item + ["||"])
        return generate(new_operators, loop - 1, allow_concat)
    else:
        return operators


def is_solvable(test: List, allow_concat: bool) -> bool:
    value = test[0]
    numbers = test[1]
    n = len(numbers) - 1  # Available position for operators
    operations = generate([], n, allow_concat)
    for operation in operations:
        result = numbers[0]
        for i, op in enumerate(operation):
            if op == "+":
                result += numbers[i + 1]
            if op == "*":
                result *= numbers[i + 1]
            if op == "||":
                result = int(str(result) + str(numbers[i + 1]))
        if value == result:
            return True
    return False


def total_calibration(raw_file: str, allow_concat: bool = False) -> int:
    tests = format_data(raw_file)
    result = 0
    for test in tests:
        if is_solvable(test, allow_concat):
            result += test[0]
    return result


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total calibration result: {total_calibration(file)}")
    print(f"Total calibration result: {total_calibration(file, allow_concat=True)}")
