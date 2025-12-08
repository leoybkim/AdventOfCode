import heapq
import math

from utils.input_reader import read_file


def distance(a: tuple, b: tuple) -> float:
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)


def part_one(data: str, connections: int):
    positions = []
    shortest = []

    # Check n*(n-1)/2 connections

    for line in data.splitlines():
        positions.append(tuple(map(int, line.split(","))))

    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            if len(shortest) < connections:
                heapq.heappush(shortest, (-distance(positions[i], positions[j]), positions[i], positions[j]))
            else:
                heapq.heappushpop(shortest, (-distance(positions[i], positions[j]), positions[i], positions[j]))

    # Found N connections that are the closest to together
    group_id = 0
    group_lookup = dict()
    group_member_lookup = dict()
    while shortest:
        dist, a, b = heapq.heappop(shortest)
        # first check if a or b is already in a group
        # if both are in a group but in a different group, merge the two groups
        if a in group_lookup and b in group_lookup and group_lookup[a] != group_lookup[b]:
            other_group_id = group_lookup[b]

            # update all other members in the other group as well
            for member in group_member_lookup[other_group_id]:
                group_lookup[member] = group_lookup[a]
                group_member_lookup[group_lookup[a]].append(member)

            # remove the other group
            del group_member_lookup[other_group_id]

        # If either one is in a group, assign the other in the same group
        elif a in group_lookup and b not in group_lookup:
            group_lookup[b] = group_lookup[a]
            group_member_lookup[group_lookup[a]].append(b)
        elif b in group_lookup and a not in group_lookup:
            group_lookup[a] = group_lookup[b]
            group_member_lookup[group_lookup[b]].append(a)

        elif a not in group_lookup and b not in group_lookup:
            # if both not in group, generate a group id and place them in that group
            group_id += 1
            group_member_lookup[group_id] = [a, b]
            group_lookup[a] = group_id
            group_lookup[b] = group_id

    # shortest N connections are all in a group now
    # find the largest group
    group_sizes = [len(members) for members in group_member_lookup.values()]
    top_3_groups = sorted(group_sizes, reverse=True)[:3]
    return math.prod(top_3_groups)


def part_two(data: str) -> int:
    positions = []
    shortest = []

    for line in data.splitlines():
        positions.append(tuple(map(int, line.split(","))))

    for i in range(len(positions) - 1):
        for j in range(i + 1, len(positions)):
            heapq.heappush(shortest, (distance(positions[i], positions[j]), positions[i], positions[j]))

    group_id = 0
    group_lookup = dict()
    group_member_lookup = dict()
    while shortest:
        dist, a, b = heapq.heappop(shortest)
        # first check if a or b is already in a group
        # if both are in a group but in a different group, merge the two groups
        if a in group_lookup and b in group_lookup and group_lookup[a] != group_lookup[b]:
            other_group_id = group_lookup[b]

            # update all other members in the other group as well
            for member in group_member_lookup[other_group_id]:
                group_lookup[member] = group_lookup[a]
                group_member_lookup[group_lookup[a]].append(member)

            # remove the other group
            del group_member_lookup[other_group_id]

        # If either one is in a group, assign the other in the same group
        elif a in group_lookup and b not in group_lookup:
            group_lookup[b] = group_lookup[a]
            group_member_lookup[group_lookup[a]].append(b)
        elif b in group_lookup and a not in group_lookup:
            group_lookup[a] = group_lookup[b]
            group_member_lookup[group_lookup[b]].append(a)

        elif a not in group_lookup and b not in group_lookup:
            # if both not in group, generate a group id and place them in that group
            group_id += 1
            group_member_lookup[group_id] = [a, b]
            group_lookup[a] = group_id
            group_lookup[b] = group_id

        if len(group_member_lookup) == 1 and len(list(group_member_lookup.values())[0]) == len(positions):
            return a[0] * b[0]

    return 0


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Product of three largest circuits: {part_one(file, 1000)}")
    print(f"Product of the X coordinates of the last two junction boxes: {part_two(file)}")
