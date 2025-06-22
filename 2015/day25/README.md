# Day 25

[adventofcode.com/2015/day/25](https://adventofcode.com/2015/day/25)

#### Generating the Kth Code

If `next_code = (previous_code * 252533) % 33554393`, \
then

- `c1 = (c0 * M) % N`
- `c2 = (c1 * M) % N = ((c0 * M) % N * M) % N = (c0 * M^2) % N`
- `c1 = (c0 * M) % N = ((c0 * M^2) % N * M) % N = (c0 * M^3) % N`
- ...
- `ck = (c0 * M^k) % N`

#### Determine K

This is the tricky part involving the diagonal filling.

|    |    |    |    | 15 |
|----|----|----|----|----|
|    |    |    | 14 |    |
|    |    | 13 |    |    |
|    | 12 |    |    |    |
| 11 |    |    |    |    |

The diagonal filling starts from the bottom left to top right.\
The first diagonal is of length 1: `[1]`\
The second diagonal is of length 2: `[2, 3]`\
The third diagonal is of length 3: `[4, 5, 6]`\
The fourth diagonal is of length 4: `[7, 8, 9, 10]`\
The fifth diagonal is of length 5: `[11, 12, 13, 14, 15]`\
...\
The `n`th diagonal is of length n: `[x for x in range(((n - 1) * n // 2) + 1, (((n - 1) * n // 2) + n) + 1)]`

The number of elements before a given diagonal is the sum of numbers from `1` to `d - 1`, which is equal to the
triangular number: `((d - 1) * d) // 2`.

The diagonal number `n` is equal to `row + column - 1` on a 1-index table.

So the `K` based on `row` and `column` will first need to determine the diagonal `n`. Then within the numbers in the
diagonal list, K will be at the `column`th position.

For example, `K` will be `14` at `row=2` and `column=4` in the above table. `n = 2 + 4 - 1 = 5`. Diagonals are `[x for x in range((4 * 5 // 2) + 1, ((4 * 5 // 2) + n) + 1)] = [11, 12, 13, 14, 15]`. And `diagonal[column=4] = 14`.  