from typing import List


def read_file(input_file_path: str) -> str:
    with  open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[List[str]]:
    data = []
    for line in raw_data.split():
        data.append(list(line))
    return data


def count_xmas(data: List[List[str]]) -> int:
    """
    Crossword search for "XMAS"
    Allow forward, backward and diagonal search
    :param data: Crossword board
    :return: Number of times "XMAS" appears in the crossword
    """
    count = 0

    # Horizontal forward and backward search
    for r in data:
        count += "".join(r).count("XMAS") + "".join(r).count("SAMX")

    # Transpose the grid for vertical search
    data_t = [list(x) for x in zip(*data)]
    for r in data_t:
        count += "".join(r).count("XMAS") + "".join(r).count("SAMX")

    # Prep for diagonal search by shifting each row with padding, then transposing for vertical search
    # Diagonal left (top-bottom)
    l = len(data[0])
    d_data = []
    for i, r in enumerate(data):
        d_data.append(["." for _ in range(i)] + r + ["." for _ in range(l - 1 - i)])
    d_data_t = [list(x) for x in zip(*d_data)]
    for r in d_data_t:
        count += "".join(r).count("XMAS") + "".join(r).count("SAMX")

    # Prep for opposite diagonal search by shifting in reverse order with padding, then transposing for vertical search
    d_data_r = []
    for i, r in enumerate(data):
        d_data_r.append(["." for _ in range(l - 1 - i)] + r + ["." for _ in range(i)])
    d_data_r_t = [list(x) for x in zip(*d_data_r)]
    for r in d_data_r_t:
        count += "".join(r).count("XMAS") + "".join(r).count("SAMX")

    return count


def count_x_mas(data: List[List[str]]) -> int:
    pass


if __name__ == "__main__":
    file = read_file("input.txt")
    letters = format_data(file)
    print(f"Number of times XMAS appear: {count_xmas(letters)}")
    print(f"Number of times X-MAS appear: {count_x_mas(letters)}")
