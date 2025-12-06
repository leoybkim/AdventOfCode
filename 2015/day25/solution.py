from re import match

from utils.input_reader import read_file


def parse_instruction(raw_input: str) -> tuple[int, int]:
    pattern = r".*?row\s(\d+),\scolumn\s(\d+)"
    m = match(pattern, raw_input)
    return int(m.group(1)), int(m.group(2))


def gen_kth_code(first_code: int, k: int) -> int:
    """
    If next_code = (previous_code * 252533) % 33554393, then
    c1 = (c0 * M) % N
    c2 = (c1 * M) % N = ((c0 * M) % N * M) % N = (c0 * M^2) % N
    c1 = (c0 * M) % N = ((c0 * M^2) % N * M) % N = (c0 * M^3) % N
    ...
    ck = (c0 * M^k) % N
    """
    # return (first_code * 252533 ** k) % 33554393
    return int((first_code * pow(252533, k, 33554393)) % 33554393)


def find_code(raw_input: str) -> int:
    r, c = parse_instruction(raw_input)
    first_code = 20151125
    k = find_k(r, c)
    return gen_kth_code(first_code, k)


def find_k(r: int, c: int) -> int:
    """
    The number of elements before a given diagonal is the sum of numbers from 1 to d-1,
    which is equal to the triangular number: ((d - 1) * d) // 2
    The n-th diagonal is of length n: [x for x in range(((n - 1) * n // 2) + 1, (((n - 1) * n // 2) + n) + 1)]
    The diagonal number n is equal to (row + column - 1) on a 1-index table.
    So the K based on row and column will first need to determine the diagonal n.
    Then within the numbers in the diagonal list, K will be at the column-th position.
    :param r: row 1-index
    :param c: column 1-index
    :return: K, the order in which value at [r,c] was inserted through diagonal filling
    """
    n = r + c - 1
    triangular_number = (n - 1) * n // 2
    return [x for x in range(triangular_number + 1, triangular_number + n + 1)][c - 1] - 1


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"The CODE: {find_code(file)}")
