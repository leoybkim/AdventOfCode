def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def format_data(raw_input: str) -> list[str]:
    data = []
    for line in raw_input.split("\n"):
        data.append(line)
    return data


def num_char_in_memory(line: str) -> int:
    length = len(line) - 2  # Subtract outer quotes
    count = length
    for i in range(1, length):
        c = line[i]
        if i <= length - 1 and line[i] == "\\" and (line[i + 1] == "\\" or line[i + 1] == '"'):
            if i <= length - 2 and (line[i + 2] == "x" or line[i + 2] == '"'):
                continue
            count -= 1  # Subtract escaping for slash or quote character
        elif i <= length - 3 and line[i:i + 2] == "\\x":
            count -= 3  # \x0A represents one ASCII code
    return count


def calculate_string(raw_input: str) -> int:
    data = format_data(raw_input)
    total = 0

    for d in data:
        total += len(d)
        total -= num_char_in_memory(d)

    return total


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total number of characters of code for string literals minus "
          f"total number of characters in memory for the value of string: {calculate_string(file)}")
