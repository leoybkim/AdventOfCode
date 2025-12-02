def is_invalid(n: int) -> bool:
    s = str(n)
    l = len(s)
    if l % 2 == 1:
        return False
    else:
        m = l // 2
        if s[0:m] == s[m:]:
            return True
    return False


def is_invalid2(n: str) -> bool:
    # Nice little trick found on https://codegolf.stackexchange.com/questions/37851/string-prototype-isrepeated/37855#37855
    s = str(n)
    doubled_s = s + s

    # Slice the doubled string, removing the first and last characters.
    # This creates a window of all possible cyclic shifts of s, excluding s itself.
    sliced_s = doubled_s[1:-1]

    # If s is present in the sliced string, it means the original string is periodic.
    return s in sliced_s


def part_one(input_file_path: str):
    sum_invalids = 0
    with (open(input_file_path, "r") as input_file):
        for line in input_file:
            for r in line.split(","):
                s, e = map(int, r.split("-"))
                for n in range(s, e + 1):
                    sum_invalids += n if is_invalid(n) else 0

    return sum_invalids


def part_two(input_file_path: str):
    sum_invalids = 0
    with (open(input_file_path, "r") as input_file):
        for line in input_file:
            for r in line.split(","):
                s, e = map(int, r.split("-"))
                for n in range(s, e + 1):
                    sum_invalids += n if is_invalid2(n) else 0

    return sum_invalids


if __name__ == "__main__":
    file = "inputs/input.txt"
    print(f"Sum of invalid IDs: {part_one(file)}")
    print(f"Sum of invalid IDs with new rules: {part_two(file)}")
