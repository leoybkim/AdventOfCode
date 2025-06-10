# Day 17

[adventofcode.com/2015/day/17](https://adventofcode.com/2015/day/17)

This puzzle is a variation of a subset sum problem [[1]](#1) where instead of just checking if *any* subset sums to the target, you need to **count all subsets** that sum to the target.

The recurrence relation of the problem can be expressed as follows:

- Let $C = [c_1, c_2, ..., c_N]$ be the list of container sizes, where $N$ is the total number of containers
- $T$ be the target volume

Define $dp[i][j]$ as the number of ways to achieve a sum of $j$ using only the first $i$ containers ($c_1, c_2, ..., c_i$).

$$
dp[i][j] = \begin{cases}
dp[i-1][j] & \text{if } j < c_i \\
dp[i-1][j] + dp[i-1][j - c_i] & \text{if } j \ge c_i
\end{cases}
$$

Case 1: $j < c_i$
- current container size $c_i$ is greater than the target sum $j$. Therefore, the number of ways to make sum $j$ using the first $i$ containers is simply the number of way to make sum $j$ using the first $i-1$ containers.

Case 2: $j \ge c_i$
- current container can potentially be included
- 2 options:
  - don't include the current container $c_i$: 
    - the number of ways to achieve sum $j$ without using $c_i$
    - $dp[i-1][j]$
  - include the current container $c_i$: 
    - if $c_i$ is included, then need to achieve the remaining sum of $j-c_i$ using the first $i-1$ containers
    - $dp[i-1][j - c_i]$
- total ways to achieve sum $j$ is the sum of these two options. 

Base cases:
- $dp[0][0] = 1$
  - There is only one way to achieve a sum of 0 using zero containers
- $dp[0][j] = 0 for j > 0$
  - There are zero ways to achieve any sum using zero containers
  
The final solution will be the value of $dp[N][T]$.

#### References

<a id="1">[1]</a> Subset sum problem [https://en.wikipedia.org/wiki/Subset_sum_problem](https://en.wikipedia.org/wiki/Subset_sum_problem)
