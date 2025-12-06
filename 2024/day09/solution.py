from collections import defaultdict
from typing import List

from utils.input_reader import read_file


def format_data(raw_data: str) -> str:
    return raw_data.strip()


def checksum(raw_file: str, whole=False) -> int:
    s = 0
    translated = translate(format_data(raw_file))
    rearranged = rearrange(translated, whole=whole)
    for i, c in enumerate(rearranged):
        if c != ".":
            s += i * int(c)

    return s


def translate(data: str) -> List[str]:
    results = []
    ID = 0
    for i in range(len(data)):
        if i == 0 or i % 2 == 0:  # Iterate in two character chunks
            results += [str(ID)] * int(data[i])  # First char represents file block size
            if i + 1 < len(data):
                results += ["."] * int(data[i + 1])  # Second character represents free space.
            ID += 1
    return results


def create_lookup(data: List[str]) -> defaultdict:
    """
    Generate lookup table where key is the ID number of the file that holds information of its location in the system.
    Values: {"fileblock": tuple(start, end), "free_space": tuple(start, end)}
    @param data: Translated disk map
    @return: Look up table
    """
    lookup = defaultdict(lambda: defaultdict(tuple))
    fileblock_s = fileblock_e = free_space_s = free_space_e = 0
    prev_ID = None
    ID = None
    for i, c in enumerate(data):
        if c.isnumeric():
            if ID and ID != c and not lookup[ID]["fileblock"]:
                lookup[ID]["fileblock"] = (fileblock_s, fileblock_e)
                lookup[ID]["free_space"] = (-1, -1)
                fileblock_s = i
                prev_ID = ID
            if prev_ID and not lookup[prev_ID]["free_space"]:
                lookup[prev_ID]["free_space"] = (free_space_s, free_space_e)
            ID = c
            fileblock_e = i  # Keep updating end of fileblock index
            free_space_s = i + 1  # Anticipate the start of next free space index
        else:
            if not lookup[ID]["fileblock"]:
                lookup[ID]["fileblock"] = (fileblock_s, fileblock_e)
            free_space_e = i  # Keep updating end of free space index
            fileblock_s = i + 1  # Anticipate the start of next fileblock index
            prev_ID = ID
    # Handle last insert
    if not lookup[ID]["fileblock"]:
        lookup[ID]["fileblock"] = (fileblock_s, fileblock_e)
    if not lookup[ID]["free_space"]:
        lookup[ID]["free_space"] = (fileblock_e + 1, len(data) - 1) if fileblock_e + 1 <= len(data) - 1 else (-1, -1)
    return lookup


def rearrange(data: List[str], whole) -> List[str]:
    if whole:
        lookup = create_lookup(data)  # Dictionaries will guarantee insertion order
        keys = list(lookup.keys())
        for k in keys[:0:-1]:
            size = (lookup[k]["fileblock"][1] - lookup[k]["fileblock"][0]) + 1
            for m in keys[:int(k)]:
                free_space = (lookup[m]["free_space"][1] - lookup[m]["free_space"][0]) + 1
                space = free_space if lookup[m]["free_space"] != (-1, -1) else 0
                if space == size:
                    data[lookup[m]["free_space"][0]:lookup[m]["free_space"][1] + 1] = [k] * size
                    data[lookup[k]["fileblock"][0]:lookup[k]["fileblock"][1] + 1] = ["."] * size
                    lookup[m]["free_space"] = (-1, -1)
                    break
                if space > size:
                    new_free_space_s = lookup[m]["free_space"][0] + size
                    data[lookup[m]["free_space"][0]:new_free_space_s] = [k] * size
                    lookup[m]["free_space"] = (new_free_space_s, lookup[m]["free_space"][1])
                    data[lookup[k]["fileblock"][0]:lookup[k]["fileblock"][1] + 1] = ["."] * size
                    break
        return data

    else:
        i = 0
        j = len(data) - 1
        while i < j:
            if data[i] == "." and data[j] != ".":
                data[i], data[j] = data[j], data[i]  # Swap positions
            if data[i] != ".":
                i += 1
            if data[j] == ".":
                j -= 1

    return data


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Filesystem checksum: {checksum(file)}")
    print(f"Filesystem checksum rearranging whole file: {checksum(file, whole=True)}")
