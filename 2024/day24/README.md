# Day 24

[adventofcode.com/2024/day/24](https://adventofcode.com/2024/day/24)

## Adders
Adders are a circuit designed to perform the arithmetic addition of two binary numbers.

### Half Adder
The half adder sums two single digit binary numbers to produce a sum and a carry.
The sum is calculated by an XOR gate and the carry is calculated by an AND gate.
```
  Sum = A XOR B
Carry = A AND B
```

### Full Adder
Full adder can be constructed using two half adders. Each "carry out" from the previous adder becomes the "carry in" of the current adder.
The second half adder sums the "carry in" and the "sum" produced by the first half adder. Using multiple full adders, we can construct a circuit to add N-bit numbers.
```
      Sum = A XOR B XOR Carry_in
Carry_out = (A AND B) OR (Carry_in AND (A XOR B)) 
```