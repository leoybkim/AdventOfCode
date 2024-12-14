# Day 13
[adventofcode.com/2024/day/13](https://adventofcode.com/2024/day/13)

## Notes
The puzzle statement can be simplified into solving a linear equations with the smallest positive integers. So to solve this problem, we need to determine 1) if the linear equation has possible integer solutions, and 2) find the smallest positive integer solution. 

For the first part of the requirement.
Given a linear equation with two variables where $x$ and $y$ are variables and $a$, $b$, and $c$ are constants:
$$ax +by = c$$
We can use the Bézout's lemma[[1]](#1) below to determine if there exists an integer solution.

>Let a and b be integers with greatest common divisor d. Then there exist integers x and y such that ax + by = d. Moreover, the integers of the form az + bt are exactly the multiples of d.

For example, for a solution to exist in the following equation:

$$94x + 22y  = 8400$$

The $gcd(94, 22)$ must divide $8400$. The $gcd(94, 22) = 2$ and because 2 can divide 8400, there exists an integer solution to this equation.


#### References
<a id="1">[1]</a> Bézout's identity [https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity)