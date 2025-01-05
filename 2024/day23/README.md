# Day 23

[adventofcode.com/2024/day/23](https://adventofcode.com/2024/day/23)

## Clique

A clique is a subset of vertices in a graph where every part of vertices in the subset is directly connected by an edge.
In other words, it is a group of vertices where each one is connected to every other vertices in that group.

The first part of the puzzle is finding a clique of a given size (in this case, 3). The second part of the puzzle is finding the largest clique.
This is a NP-complete problem, where brute-force approach may work for small graphs, but a heuristic algorithms like Bron-Kerbosch [[1]](#1) may be needed for larger graphs.

```
algorithm BronKerbosch1(R, P, X) is
    if P and X are both empty then
        report R as a maximal clique
    for each vertex v in P do
        BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        P := P \ {v}
        X := X ⋃ {v}
```

#### References
<a id="1">[1]</a> Bron–Kerbosch algorithm [https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm](https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm)