# Day 16

[adventofcode.com/2024/day/16](https://adventofcode.com/2024/day/16)

## Dijkstra!

Process of exploring a graph in Dijkstra's algorithm is structurally similar to BFS (Breadth First Search) because both algorithms explore nodes level by level.
The key difference in Dijkstra's algorithm is that the edges between the nodes have varying weights.

In this puzzle, a straight move costs less than a turn move, and this difference is represented by edge weights.
While BFS considers all moves as equal, Dijkstra's algorithm accounts for the cost of each move in a weighted graph.

As a result, instead of using a FIFO queue like BFS, Dijkstra uses a priority queue, typically implemented with a min-heap.
This ensures that the algorithm always explores the node with the minimum accumulated cost at each step to guide it towards the optimal path.