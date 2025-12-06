# Day 13

[adventofcode.com/2015/day/13](https://adventofcode.com/2015/day/13)

## Notes

To calculate the cost from all possible seating arrangements in a circular setup, we need to iterate through unique
circular permutations.
This means we only account for the relative positions of people sitting next to each other, eliminating redundant
arrangements that occur from rotation.
There can be $n$ possible rotation, so dividing $n!$ by $n$, the final number of permutations will be $(n-1)!$.
In other words, to generate these unique positions, we can simply fix one person's position as the head of the table.
Then you only need to calculate the linear permutations of the remaining $n-1$ people to fill the other seats.
Each of these linear arrangements, when appended with the fixed person's position at the beginning or at the end,
represents a unique circular seating arrangement.