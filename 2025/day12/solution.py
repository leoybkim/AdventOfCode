from utils.input_reader import read_file


def parse_data(data: str) -> tuple[list[list], list[tuple]]:
    lines = data.splitlines()
    presents = []
    for i in range(0, 30, 5):
        presents.append([list(lines[i + 1]), list(lines[i + 2]), list(lines[i + 3])])

    regions = []
    for j in range(30, len(lines)):
        shape, quantity = lines[j].split(":")
        regions.append((tuple(map(int, shape.split("x"))), list(map(int, quantity.strip().split()))))
    return presents, regions


def can_fit(r: tuple, presents) -> bool:
    x, y = r[0]
    quantities = r[1]
    total = x * y
    temp = 0
    for i, q in enumerate(quantities):
        if q > 0:
            filled = sum(row.count("#") for row in presents[i])
            temp += q * filled
    return temp < total * 0.85


def part_one(data: str) -> int:
    count = 0
    presents, regions = parse_data(data)
    for region in regions:
        count += can_fit(region, presents)
    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of regions that can fit all presents listed: {part_one(file)}")
