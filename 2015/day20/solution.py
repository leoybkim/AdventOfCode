def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def find_lowest_house_number(raw_input: str) -> int:
    goal = int(raw_input)
    MAX_HOUSE_NUMBER = 1_000_000  # arbitrary upper bound
    presents = [0] * (MAX_HOUSE_NUMBER + 1)

    for elf_i in range(1, MAX_HOUSE_NUMBER + 1):
        for house_i in range(elf_i, MAX_HOUSE_NUMBER + 1, elf_i):
            # start at elf_i: elf can't visit a house with a lower number than its own
            # step by elf_i: elf delivers presents to every ith house
            presents[house_i] += elf_i * 10

    for i in range(1, MAX_HOUSE_NUMBER + 1):
        if presents[i] >= goal:
            return i
    return None


def find_lowest_house_number2(raw_input: str) -> int:
    goal = int(raw_input)
    MAX_HOUSE_NUMBER = 1_000_000  # arbitrary upper bound
    presents = [0] * (MAX_HOUSE_NUMBER + 1)

    for elf_i in range(1, MAX_HOUSE_NUMBER + 1):
        count = 0
        for house_i in range(elf_i, MAX_HOUSE_NUMBER + 1, elf_i):
            # start at elf_i: elf can't visit a house with a lower number than its own
            # step by elf_i: elf delivers presents to every ith house
            count += 1
            if count <= 50:
                presents[house_i] += elf_i * 11
            else:
                # elf_i has already visited 50 houses, no further check required for this elf
                break

    for i in range(1, MAX_HOUSE_NUMBER + 1):
        if presents[i] >= goal:
            return i
    return None


if __name__ == "__main__":
    input = read_file("inputs/input.txt")
    print(f"Lowest house number of the house to get as least as many presents: {find_lowest_house_number(input)}")
    print(f"Lowest house number with new rules: {find_lowest_house_number2(input)}")
