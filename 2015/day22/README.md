# Day 22

[adventofcode.com/2015/day/22](https://adventofcode.com/2015/day/22)

A chance to write OOP in AoC? :godmode:

Unlike Day 21, which involved making a single set of choices at the beginning with a deterministic outcome, Day 22
choices are dynamic and continuous.
This is finding the "shortest path" problem. Each possible state in the game can be considered as a node in a graph.
Casting a spell against the boss's move can be considered as the edges or path from one game state to another.
The edge weights can be represented with the mana cost to cast the spell. And since we want to find the minimum mana
cost, we are effectively searching for the shortest path. 