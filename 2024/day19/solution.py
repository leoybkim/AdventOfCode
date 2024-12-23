def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> tuple:
    pattern_str, designs_str = raw_data.split("\n\n")
    patterns = {}
    for pattern in pattern_str.split(","):
        l = len(pattern.strip())
        patterns[pattern.strip()] = l
    designs = []
    for design in designs_str.split("\n"):
        design = design.strip()
        designs.append(design)
    return patterns, designs


def clean_patterns(patterns: dict) -> dict:
    """
    Remove redundant patterns.
    Redundant patterns are multi-colour patterns that are only composed of single patterns that are also available.
    @param patterns: Initial patterns
    @return: Cleaned patterns
    """
    clean = {}
    for pattern, length in patterns.items():
        if length == 1 or not all(char in patterns for char in pattern):
            clean[pattern] = length
    return clean


def possible_designs(raw_input: str, count_combinations=False) -> int:
    patterns, designs = format_data(raw_input)
    if not count_combinations:
        patterns = clean_patterns(patterns)

    counter = 0
    combinations = 0
    for design in designs:
        # Dynamic Programming:
        # Check if the substrings of each design string can be built using the patterns
        # Memoize the answers to the sub problems iteratively until we find solution to the final design string
        n = len(design)
        dp = [0] * (n + 1)  # Init DP array where results of the sub problems can be cached
        dp[0] = 1  # Base case for empty string

        # Iterate through the index of the design string, check if substring ending at each position can be formed
        for i in range(1, n + 1):
            for pat in patterns:
                # Check if some portion of the next substring can be formed using the pattern
                if len(pat) <= i and dp[i - len(pat)] > 0 and design[i - len(pat):i] == pat:
                    dp[i] += dp[i - len(pat)]

        counter += dp[n] > 0
        combinations += dp[n]
    return combinations if count_combinations else counter


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of possible designs: {possible_designs(file)}")
    print(f"Number of different ways to make each possible designs: {possible_designs(file, count_combinations=True)}")
