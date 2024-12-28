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


def dfs(graph: dict, vertex: str, party: list, visited: dict) -> list | None:
    visited[vertex] = True
    if len(party) == 3:
        # Found LAN Party
        return party if vertex == party[0] else None
    party.append(vertex)
    for v in graph[vertex]:
        if not visited[v] or (v == party[0] and len(party) == 3):
            dfs(graph, v, party, visited)


def lan_party_search(raw_input: str) -> int:
    connections = format_data(raw_input)

    network = defaultdict(set)
    for link1, link2 in connections:
        network[link1].add(link2)
        network[link2].add(link1)
    for v in network:
        parties = []
        visited = {computer: False for computer in network}
        party = dfs(network, v, [], visited)
        if party is not None:
            parties.append(party)

    count = 0
    for party in parties:
        count += any("t" in v for v in party)
    return 0


if __name__ == "__main__":
    file = read_file("inputs/input.txt")
    print(f"Number of LAN Party with at least one computer with a name that starts with t: {lan_party_search(file)}")
