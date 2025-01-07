def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def format_data(raw_input: str) -> list[str]:
    data = []
    for line in raw_input.split("\n"):
        data.append(line)
    return data


def num_char_in_memory(line: str) -> int:
    repeat = True
    s = 0
    while repeat:
        repeat = False
        for i in range(s, len(line)):
            if i <= len(line) - 2 and line[i] == "\\" and (line[i + 1] == "\\" or line[i + 1] == '"'):
                # If '\\' or '\"' , remove the first slash and evaluate again
                line = line[0:i] + line[i + 1:]
                repeat = True
                s = i + 1
                break
            elif i <= len(line) - 4 and line[i:i + 2] == "\\x" and line[i + 2:i + 4].isalnum():
                # if '\x0A' ASCII representation, remove three of the 4 literal characters
                line = line[0:i] + line[i + 3:]
                repeat = True
                s = i + 1
                break

    return len(line) - 2


def num_char_in_new_encoding(line: str) -> int:
    special = 0
    for c in line:
        if c == '"' or c == "\\":
            special += 1
    return len(line) + special + 2


def calculate_string(raw_input: str, new=False) -> int:
    data = format_data(raw_input)
    total = 0

    if new:
        for d in data:
            total += num_char_in_new_encoding(d)
            total -= len(d)
    else:
        for d in data:
            total += len(d)
            total -= num_char_in_memory(d)

    return total


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Total number of characters of code for string literals minus "
          f"total number of characters in memory for the value of string: {calculate_string(file)}")

    print(f"Total number of characters new encoded string minus "
          f"total number of characters of code in each original string literal: {calculate_string(file, new=True)}")
