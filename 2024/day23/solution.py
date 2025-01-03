from collections import defaultdict
from typing import List


def read_file(input_file_path: str) -> str:
    with open(input_file_path) as input_file:
        return input_file.read()


def format_data(raw_data: str) -> List[tuple[str, str]]:
    connections = []
    for line in raw_data.split("\n"):
        c1, c2 = line.split('-')
        connections.append((c1, c2))
    return connections


def find_parties(network):
    parties = set()

    for v in network:
        neighbours = list(network[v])
        # Check each pair of neighbours
        for i in range(len(neighbours)):
            for j in range(i + 1, len(neighbours)):
                n1 = neighbours[i]
                n2 = neighbours[j]

                # Party if there's an edge between the two neighbours
                if n2 in network[n1]:
                    party = frozenset([v, n1, n2])  # To avoid permutations
                    parties.add(party)

    return parties


def lan_party_search(raw_input: str) -> int:
    connections = format_data(raw_input)
    network = defaultdict(set)
    for link1, link2 in connections:
        network[link1].add(link2)
        network[link2].add(link1)

    parties = find_parties(network)

    count = 0
    for party in parties:
        count += any("t" == v[0] for v in party)
    return count


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of LAN Party with at least one computer with a name that starts with t: {lan_party_search(file)}")
