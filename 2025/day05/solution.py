from utils.input_reader import read_file


def parse_file(data: str) -> tuple[list, list]:
    ranges = []
    ids = []
    range_mode = True
    for line in data.splitlines():
        if line.strip() == "":
            range_mode = False
            continue
        if range_mode:
            s, e = map(int, line.split("-"))
            ranges.append((s, e))
        else:
            ids.append(int(line.strip()))

    return ranges, ids


def merge_ranges(ranges: list) -> list:
    ranges.sort(key=lambda x: x[0])
    merged = [[ranges[0][0], ranges[0][1]]]  # convert tuples to list, because they will need to be modified

    for s, e, in ranges[1:]:
        prev_s, prev_e = merged[-1]
        if s <= prev_e:
            merged[-1][1] = max(prev_e, e)
        else:
            merged.append([s, e])
    return merged


def part_one(data: str):
    count = 0
    ranges, ids = parse_file(data)
    for v in ids:
        for s, e in ranges:
            if s <= v <= e:
                count += 1
                break
    return count


def part_two(data: str):
    count = 0
    ranges, _ = parse_file(data)
    ranges = merge_ranges(ranges)
    for s, e in ranges:
        count += (e - s) + 1
    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of fresh ingredients: {part_one(file)}")
    print(f"Number of all fresh ingredients in range: {part_two(file)}")
