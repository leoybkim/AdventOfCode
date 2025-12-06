from typing import List

from utils.input_reader import read_file


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
    """
    Search for Pattern

    M.S      M.M      S.M       S.S
    .A.  or  .A.  or  .A.   or  .A.
    M.S      S.S      S.M       M.M

    If the board size is MxN, iterate through (M-1)x(N-1) space and map if the 3x3 surrounding matches any of the 4
    :param data: Crossword board
    """
    count = 0
    m = len(data)
    n = len(data[0])
    for r in range(1, m - 1):
        for c in range(1, n - 1):
            if data[r][c] == "A":
                case1 = [(-1, -1, "M"), (-1, 1, "S"), (1, -1, "M"), (1, 1, "S")]
                case2 = [(-1, -1, "M"), (-1, 1, "M"), (1, -1, "S"), (1, 1, "S")]
                case3 = [(-1, -1, "S"), (-1, 1, "M"), (1, -1, "S"), (1, 1, "M")]
                case4 = [(-1, -1, "S"), (-1, 1, "S"), (1, -1, "M"), (1, 1, "M")]
                count += (match_patterns(data, r, c, case1) or
                          match_patterns(data, r, c, case2) or
                          match_patterns(data, r, c, case3) or
                          match_patterns(data, r, c, case4))
    return count


def match_patterns(grid: List[List[str]], r: int, c: int, conditions: List[tuple[int, int, str]]) -> bool:
    """
    Check if given conditions match the pattern in the grid
    :param grid: Crossword board
    :param r: row index
    :param c: column index
    :param conditions: a list of tuples containing (row offset, column offset, expected value)
    :return: True if all conditions are met, otherwise False
    """
    for i, j, pattern in conditions:
        if grid[r + i][c + j] != pattern:
            return False
    return True


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    letters = format_data(file)
    print(f"Number of times XMAS appear: {count_xmas(letters)}")
    print(f"Number of times X-MAS appear: {count_x_mas(letters)}")
