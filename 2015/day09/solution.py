from collections import defaultdict
from itertools import combinations
from re import match
from typing import List


def read_file(file_path: str) -> str:
    with open(file_path) as input_file:
        return input_file.read()


def format_data(raw_input: str) -> list[tuple]:
    data = []
    pattern = r"([a-zA-Z]+)\sto\s([a-zA-Z]+)\s=\s(\d+)"
    for line in raw_input.split("\n"):
        m = match(pattern, line)
        data.append(m.groups())
    return data


def adjacency_map(data: list) -> dict:
    """
    Create an adjacency list representation using a map.
    Outer dictionary key is the starting city, the inner keys are the destination cities,
    and the values are the traveling distance between those cities.
    @param data: Tuple of (A, B, distance) where A is the starting city, B is the destination and the distance
    @return: Adjacency list representation of the graph
    """
    adj = defaultdict(dict)
    for A, B, distance in data:
        adj[A][B] = int(distance)
        adj[B][A] = int(distance)
    return adj


def find_unique_cities(data: list) -> list[str]:
    cities = []
    for A, B, distance in data:
        if A not in cities:
            cities.append(A)
        if B not in cities:
            cities.append(B)
    return cities


def find_shortest_distance(raw_input: str) -> int:
    data = format_data(raw_input)
    adj = adjacency_map(data)
    cities = find_unique_cities(data)

    n = len(cities)
    idx_to_city = {idx: city for idx, city in enumerate(cities)}
    city_to_idx = {city: idx for idx, city in enumerate(cities)}

    # enumerate the cities and the distance between the two is stored on the 2D matrix
    distances = [[float("inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = adj[idx_to_city[i]][idx_to_city[j]] if i != j else 0

    min_distances = []  # minimum distances found for each starting city
    for city in cities:
        min_distances.append(modified_Held_Karp_algorithm(city_to_idx[city], distances))

    return min(min_distances)


def find_longest_distance(raw_input: str) -> int:
    data = format_data(raw_input)
    adj = adjacency_map(data)
    cities = find_unique_cities(data)

    n = len(cities)
    idx_to_city = {idx: city for idx, city in enumerate(cities)}
    city_to_idx = {city: idx for idx, city in enumerate(cities)}

    # enumerate the cities and the distance between the two is stored on the 2D matrix
    distances = [[float("-inf") for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = adj[idx_to_city[i]][idx_to_city[j]] if i != j else 0

    max_distances = []  # minimum distances found for each starting city
    for city in cities:
        max_distances.append(modified_Held_Karp_algorithm(city_to_idx[city], distances, inverse=True))

    return max(max_distances)


def modified_Held_Karp_algorithm(s_idx: int, distances: List[List[int]], inverse=False) -> int:
    """
    Modified Held Karp algorithm for finding the minimum cost of visiting all cities exactly once given a starting city.
    :param s_idx: starting city index
    :param distances: adjacency matrix
    :param inverse: parameter to change the heuristics from min cost to max cost
    :return: Hamiltonian path cost starting from city i and ending at any city.
    """
    n = len(distances)  # total number of cities

    # dp variable stores intermediate costs of g(S, k)
    # which represents the minimum costs of a path that starts at city s_idx,
    # visits all cities in the set S exactly once, and ends at city k.
    # S is a subset of cities, and k is one of the cities in subset S.
    dp = {}

    # Base case
    # cost of traveling to each neighbouring city from the starting city
    for k in range(n):
        if s_idx != k:
            # store the cost of the distance in the form of g({k}, k) = d(s_idx, k)
            # 1 << k, which equals integer value of 2^k, later can be interpreted in binary form for bit masking
            dp[(1 << k, k)] = (distances[s_idx][k], s_idx)

    # Iterative calculations
    # increase the subset size s from 2 to (n - 1) and store the intermediate costs in dp
    for s in range(2, n):
        # generate all permutations of the city subset of size s
        # exclude the starting city from becoming part of the subset
        for subset in combinations([i for i in range(n) if i != s_idx], s):
            # add bit masking for all cities in this subset using bitwise OR
            subset_mask = 0
            for city in subset:
                subset_mask |= 1 << city

            # find the lowest cost to get to this subset
            for k in subset:
                # create a new bit mask representing subset without the ending city k
                # bitwise XOR is used to toggle off the bit if exists in both masks
                prev_mask = subset_mask ^ (1 << k)
                path = []
                for m in subset:
                    if m != k:
                        # check if subproblem has been solved before, and use that value
                        if (prev_mask, m) in dp:
                            cost = dp[(prev_mask, m)][0] + distances[m][k]
                            path.append((cost, m))
                if path:
                    dp[(subset_mask, k)] = max(path) if inverse else min(path)

    # final bitmask is used to query the dynamic programming table for all cities visited excluding the starting city
    final_mask = ((1 << n) - 1) ^ (1 << s_idx)
    min_cost = float("-inf") if inverse else float("inf")

    # calculate optimal cost
    for k in range(n):
        if k != s_idx:
            if (final_mask, k) in dp:
                cost = dp[(final_mask, k)][0]
                min_cost = max(min_cost, cost) if inverse else min(min_cost, cost)
    return min_cost


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Distance of the shortest route: {find_shortest_distance(file)}")
    print(f"Distance of the shortest route: {find_longest_distance(file)}")
