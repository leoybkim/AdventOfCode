def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def format_input(input_file: str) -> list:
    dimensions = []
    for line in input_file.split("\n"):
        dimensions.append(list(map(int, line.split("x"))))  # l x w x h
    return dimensions


def calculate_wrapping_paper(raw_input: str) -> int:
    dimensions = format_input(raw_input)
    sqft = 0
    for l, w, h in dimensions:
        min_side = min(l * w, w * h, l * h)
        sqft += min_side + 2 * l * w + 2 * w * h + 2 * l * h
    return sqft


def calculate_ribbon_length(raw_input: str) -> int:
    dimensions = format_input(raw_input)
    ft = 0
    for l, w, h in dimensions:
        min_perimeter = min(2 * (l + w), 2 * (w + h), 2 * (l + h))
        ft += min_perimeter + l * w * h
    return ft


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total sqft of wrapping paper: {calculate_wrapping_paper(file)}")
    print(f"Total feet of ribbon: {calculate_ribbon_length(file)}")
