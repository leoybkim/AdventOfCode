# Day 23

[adventofcode.com/2024/day/23](https://adventofcode.com/2024/day/23)

## Find cycle in undirected graphs

An undirected graph has a cycle if a depth first search (DFS) finds a visited vertex again.
If we want to find a sets of three vertices where each vertex is connected to the other 2 vertex, we can exit the DFS early at depth of 3.
And at which point if the last vertex can connect back to the first vertex, we have found the set.
