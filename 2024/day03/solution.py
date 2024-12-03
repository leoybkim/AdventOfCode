import re


def sum_multiplications(data: str) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    return sum(int(x) * int(y) for x, y in matches)

def sum_disabled_multiplications(data: str) -> int:
    disabled_pattern = r"don't\(\)([\s\S]+?)do\(\)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    disabled_matches = re.findall(disabled_pattern, data)

    matches = []
    for line in disabled_matches:
        matches += re.findall(pattern, line)
    return sum(int(x) * int(y) for x, y in matches)

def read_file(input_file_path: str) -> str:
    return open(input_file_path).read()

if __name__ == "__main__":
    file = read_file("input.txt")
    print(f"Sum of all multiplications: {sum_multiplications(file)}")
    print(f"Sum of all enabled multiplications: {sum_multiplications(file) - sum_disabled_multiplications(file)}")
