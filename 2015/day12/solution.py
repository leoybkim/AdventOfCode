import json

from utils.input_reader import read_file


def parse_list(array: list, total: int, exclude_red=False) -> int:
    _total = total
    for item in array:
        if isinstance(item, list):
            total += parse_list(item, _total, exclude_red)
        elif isinstance(item, dict):
            if not exclude_red or not contains_red(item):
                total += parse_dict(item, _total, exclude_red)
        elif isinstance(item, int):
            total += item
    return total


def parse_dict(d: dict, total: int, exclude_red=False) -> int:
    _total = total
    for value in d.values():
        if isinstance(value, list):
            total += parse_list(value, _total, exclude_red)
        elif isinstance(value, dict):
            if not exclude_red or not contains_red(value):
                total += parse_dict(value, _total, exclude_red)
        elif isinstance(value, int):
            total += value
    return total


def contains_red(d: dict) -> bool:
    for k, v in d.items():
        if v == "red":
            return True
    return False


def sum_all_numbers(json_string: str, exclude_red=False) -> int:
    obj = json.loads(json_string)
    total = 0

    if isinstance(obj, list):
        total += parse_list(obj, 0, exclude_red)
    elif isinstance(obj, dict):
        if not exclude_red or not contains_red(obj):
            total += parse_dict(obj, 0, exclude_red)
    elif isinstance(obj, int):
        total += obj

    return total


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Sum of all numbers in the JSON document: {sum_all_numbers(file)}")
    print(f"Sum of all numbers in the JSON document, excluding key 'red': {sum_all_numbers(file, True)}")
