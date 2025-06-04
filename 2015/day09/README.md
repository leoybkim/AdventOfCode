# Day 9

[adventofcode.com/2015/day/9](https://adventofcode.com/2015/day/9)

## Travelling salesman problem
> Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city? [[1]](#1)
 
TSP is considered NP-hard problem and there exists many approximation algorithms and heuristic algorithms.

A brute force solution of trying all permutations to find the most optimal route would run in $O(n!)$ which may only be practical for small number of vertices like this puzzle input (8 cities).
Better alternative using the dynamic programming technique is the Bellman-Held-Karp algorithm [[2]](#2), which can find a guaranteed optimal solution in exponential time complexity of $O(n^{2}2^{n})$.

```
function algorithm TSP (G, n) is
    for k := 2 to n do
        g({k}, k) := d(1, k)
    end for

    for s := 2 to n−1 do
        for all S ⊆ {2, ..., n}, |S| = s do
            for all k ∈ S do
                g(S, k) := min m≠k,m∈S [g(S\{k}, m) + d(m, k)]
            end for
        end for
    end for

    opt := min k≠1 [g({2, 3, ..., n}, k) + d(k, 1)]
    return (opt)
end function
```

- `G`: represents the graph of cities, where edges have weights representing distances
- `n`: total number of cities
- `d(i, j)`: distance between city `i` and city `j`
- `s`: represents the size of the subset `S`, number of intermediate cities visited in addition to *city 1* and the last city `k`
- `g(S, k)`: represents the minimum cost of a path that starts at *city 1*, visits all cities in the set `S` exactly once, and ends at city `k`
  - `S`: a subset of cities that have been visited. The *city 1* is considered the starting point and isn't explicitly part of `S` in the `g` function arguments
  - `k`: the last city visited in the path represented by `g(S, k)`. `k` must be an element of `S`.

#### 1. Base case:

```
for k := 2 to n do
    g({k}, k) := d(1, k)
end for
```
- this loop initializes the base case of our dynamic programming table.
- `s = 1` to start at *city 1*, visit only one other city `k`, and end at `k`.
- `g({k}, k)` is the minimum cost to start at *city 1*, visit only city `k`, and end at city `k`. Which is simply the direct distance from *city 1* to `k`, `d(1, k)`

#### 2. Iterative calculations:
- the outer loop `for s := 2 to n−1 do` iterates through increasing sizes of subsets `S`. Start from `s = 2` because `s = 1` was handled at initialization stage. Go up to `n - 1` because the final step will consider all cities except *city 1*.
- the middle loop `for all S ⊆ {2, ..., n}, |S| = s do` considers all possible subsets `S` that contain `s` number of cities excluding *city 1*
- the inner loop `for all k ∈ S do` calculates `g(S, k)` for each subset `S` and city `k` within that subset.
  - `g(S, k) := min m≠k,m∈S [g(S\{k}, m) + d(m, k)]` is the recurrence relation
    - to find the minimum cost to visit all cities in `S` and end at `k`, consider all possible previous cities `m` in the path
    - `m` must be in `S` but not be `k`
    - `g(S\{k}, m)` represents the minimum cost to start at *city 1*, visit all cities in `S` except `k`, and end at city `m`. This has been already calculated in previous iterations.
    - `d(m, k)` is the additional cost to travel from previous city `m` to city `k`
    - take the minimum of `g(S\{k}, m) + d(m, k)` over all possible `m`

#### 3. Find the optimal path
- after computing all `g(S, k)` values, we can find the optimal path
- `g({2, 3, ..., n}, k)` represents the minimum cost path that starts at *city 1*, visits all other cities and end at city `k`
- `d(k, 1)` is the cost to return from the last city `k` back to the starting *city 1*
- iterate through all possible last cities `k` where `k` is not *city 1*, calculate the cost and take the minimum.


In the original TSP, the salesman must return to the starting city after visiting every other city, resulting in a Hamiltonian cycle [[3]](#3).
The optimal path is independent of the starting point because the cycle is symmetric. Rotating the cycle does not change the total cost.

However, the key difference in this puzzle from the TSP is that the puzzle does *not* require the salesman to return back to the original city at the end.
It is actually more correct to categorize it as the Hamiltonian path problem, which is a problem that requires finding a path that visits every vertex in the graph exactly once.
Which means that the choice of the starting city does matter. So the modified algorithm must consider all possible starting points to find the optimal cost.

The run time can be improved with more complex algorithms such as Monte Carlo algorithm $O(1.657^{n})$, or a SAT solver

#### References
<a id="1">[1]</a> Travelling salesman problem [https://en.wikipedia.org/wiki/Travelling_salesman_problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)\
<a id="2">[2]</a> Held–Karp algorithm [https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm](https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm)\
<a id="3">[3]</a> Hamiltonian cycle [https://en.wikipedia.org/wiki/Hamiltonian_path](https://en.wikipedia.org/wiki/Hamiltonian_path)