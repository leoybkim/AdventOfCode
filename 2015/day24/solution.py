import math
from itertools import combinations


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def quantum_entanglement(raw_input: str, groups=3) -> int:
    packages = list(map(int, raw_input.split("\n")))
    total_weight = sum(packages)
    group_weight = total_weight // groups
    min_QE = float("inf")

    for i in range(1, len(packages)):
        for combination in combinations(packages, i):
            if sum(combination) == group_weight:
                QE = math.prod(combination)
                return min(min_QE, QE)
    return min_QE


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"The quantum entanglement of the first group of packages for 3 groups: {quantum_entanglement(input)}")
    print(f"The quantum entanglement of the first group of packages for 4 groups : {quantum_entanglement(input, groups=4)}")
