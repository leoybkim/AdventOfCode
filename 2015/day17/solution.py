from itertools import combinations

from utils.input_reader import read_file


def count_combinations(raw_input: str, target: int) -> int:
    containers = list(map(int, raw_input.split("\n")))
    n = len(containers)
    # init DP table
    # dp[i][j] tracks number of ways to achieve sum "j" using the first "i" containers
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # base case
    for i in range(1, n + 1):
        container_size = containers[i - 1]
        for j in range(target + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= container_size:
                dp[i][j] += dp[i - 1][j - container_size]

    return dp[n][target]


def count_minimum_combinations(raw_input: str, target: int) -> int:
    containers = list(map(int, raw_input.split("\n")))
    min_count = 0

    # using itertools combinations function, generate all possible combinations of containers in increasing set size k
    # if sum of the set found matches the target, this k will be the smallest set size.
    for k in range(1, len(containers) + 1):
        for c in combinations(containers, k):
            if sum(c) == target:
                min_count += 1
        if min_count > 0:
            break
    return min_count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of different combinations of containers: {count_combinations(file, 150)}")
    print(
        f"Number of different combinations of using minimum number of containers: {count_minimum_combinations(file, 150)}")
