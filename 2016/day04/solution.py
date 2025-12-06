import collections
import re

from utils.input_reader import read_file


def parse_rooms(raw_input: str) -> list:
    rooms = []
    for line in raw_input.split("\n"):
        match = re.match(r"([a-z-]+?)-(\d+)\[(\w+)\]", line)
        if match:
            name = match.group(1)
            id = match.group(2)
            checksum = match.group(3)
            rooms.append((name, int(id), checksum))
    return rooms


def is_real_room(name, checksum) -> bool:
    counts = collections.Counter(name)
    del counts["-"]
    # sort by descending order of count, and ascending alphabetical order
    sorted_top_five = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:5]
    return "".join(map(lambda item: item[0], sorted_top_five)) == checksum


def decrypted_room_name(encrypted_name, id) -> str:
    decrypted = []
    unicode_start = ord("a")
    for c in encrypted_name:
        if c == "-":
            decrypted.append(" ")
        else:
            shifted = (ord(c) - unicode_start + id) % 26 + unicode_start
            decrypted.append(chr(shifted))
    return "".join(decrypted)


def sum_real_room_ids(raw_input: str) -> int:
    rooms = parse_rooms(raw_input)
    sum_ids = 0
    for room in rooms:
        sum_ids += room[1] if is_real_room(room[0], room[2]) else 0
    return sum_ids


def find_north_pole_room(raw_input: str) -> int:
    rooms = parse_rooms(raw_input)
    for room in rooms:
        if decrypted_room_name(room[0], room[1]) == "northpole object storage":
            return room[1]
    return -1


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Sum of the sector IDs of the real room is: {sum_real_room_ids(file)}")
    print(f"The sector ID of the room where North Pole objecst are stored: {find_north_pole_room(file)}")
