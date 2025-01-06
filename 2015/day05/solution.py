def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def format_data(raw_input: str) -> list[str]:
    data = []
    for line in raw_input.split("\n"):
        data.append(line)
    return data


def count_nice_strings(raw_input: str, new_rule=False) -> int:
    data = format_data(raw_input)
    vowels = "aeiou"
    count = 0

    def has_3_vowels(s: str) -> bool:
        v_count = 0
        for c in s:
            if c in vowels:
                v_count += 1
            if v_count == 3:
                return True
        return False

    def has_combo(s: str) -> bool:
        prev = s[0]
        for c in s[1:]:
            if c == prev:
                return True
            prev = c
        return False

    def has_forbidden(s: str) -> bool:
        forbidden = ["ab", "cd", "pq", "xy"]
        for w in forbidden:
            if w in s:
                return True
        return False

    def has_pair_without_overlap(s: str):
        for i in range(len(s) - 1):
            pair = s[i:i + 2]
            if i >= 4 and pair in s[0:i - 1] or pair in s[i + 2:]:
                return True
            elif pair in s[i + 2:]:
                return True
        return False

    def has_sandwich(s: str):
        for i in range(len(s) - 2):
            if s[i] == s[i + 2]:
                return True
        return False

    for s in data:
        if new_rule:
            count += has_pair_without_overlap(s) and has_sandwich(s)
        else:
            count += has_3_vowels(s) and has_combo(s) and not has_forbidden(s)
    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of 'nice' strings: {count_nice_strings(file)}")
    print(f"Number of 'nice' strings under new rules: {count_nice_strings(file, new_rule=True)}")
