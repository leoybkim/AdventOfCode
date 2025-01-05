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


def bron_kerbosch(R: set, P: set, X: set, graph: dict, largest_clique: set):
    """
    Bron-Kerbosch recursive function modified to find the largest maximal clique.
    @param R: Set of vertices in the current clique
    @param P: Set of vertices that can potentially be added to the clique
    @param X: Set of vertices that have already been considered
    @param graph: The graph represented as a dictionary {vertex: set of neighbors}
    @param largest_clique: Set of vertices in the largest maximal clique
    """
    if not P and not X:
        if len(R) > len(largest_clique):
            largest_clique.clear()
            largest_clique.update(R)

    # Loop over a copy of P to avoid modifying it during iteration
    for v in P.copy():
        bron_kerbosch(R.union({v}), P.intersection(graph[v]), X.intersection(graph[v]), graph, largest_clique)
        P.remove(v)
        X.add(v)


def build_network_graph(raw_input: str) -> dict:
    connections = format_data(raw_input)
    network = defaultdict(set)
    for link1, link2 in connections:
        network[link1].add(link2)
        network[link2].add(link1)
    return network


def lan_party_search(raw_input: str) -> int:
    network = build_network_graph(raw_input)
    parties = find_parties(network)

    count = 0
    for party in parties:
        count += any("t" == v[0] for v in party)
    return count


def lan_party_password(raw_input: str) -> str:
    network = build_network_graph(raw_input)
    largest_clique = set()
    bron_kerbosch(set(), set(network.keys()), set(), network, largest_clique)
    sorted_clique = sorted(list(largest_clique))
    return ",".join(sorted_clique)


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of LAN Party with at least one computer with a name that starts with t: {lan_party_search(file)}")
    print(f"Password to get into the LAN party: {lan_party_password(file)}")
