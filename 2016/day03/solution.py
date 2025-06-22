def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def parse_instructions(raw_input: str, part2=False) -> list:
    instructions = []
    if part2:
        col1 = []
        col2 = []
        col3 = []
        for line in raw_input.split("\n"):
            nums = list(map(int, line.split()))
            col1.append(nums[0])
            col2.append(nums[1])
            col3.append(nums[2])

        for i in range(0, len(col1), 3):
            instructions.append([col1[i], col1[i + 1], col1[i + 2]])
            instructions.append([col2[i], col2[i + 1], col2[i + 2]])
            instructions.append([col3[i], col3[i + 1], col3[i + 2]])
    else:
        for line in raw_input.split("\n"):
            instructions.append(tuple(map(int, line.split())))
    return instructions


def valid_triangle(item: tuple[int, int, int]) -> bool:
    # in a valid triangle, the sum of any two sides must be larger than the remaining side
    return item[0] + item[1] > item[2] and item[1] + item[2] > item[0] and item[0] + item[2] > item[1]


def possible_triangles(raw_input: str, part2=False) -> int:
    if part2:
        items = parse_instructions(raw_input, part2=True)
    else:
        items = parse_instructions(raw_input)
    count = 0
    for item in items:
        count += 1 if valid_triangle(item) else 0

    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"There are {possible_triangles(file)} possible triangles")
    print(f"There are {possible_triangles(file, part2=True)} possible triangles with vertical specification")
