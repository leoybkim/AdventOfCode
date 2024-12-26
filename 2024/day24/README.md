# Day 24

[adventofcode.com/2024/day/24](https://adventofcode.com/2024/day/24)

## Adders
Adders are a circuit designed to perform the arithmetic addition of two binary numbers.

### Half adder
The half adder sums two single digit binary numbers to produce a sum and a carry.
The sum is calculated by an XOR gate and the carry is calculated by an AND gate.
```
  Sum = A XOR B
Carry = A AND B
```

### Full Adder
The full adder can handle multi digit addition of two binary numbers. It addresses an additional input "carry in", which allows handling the carry form a previous bit's addition.
```
      Sum = A XOR B XOR Carry_in
Carry_out = (A AND B) OR (Carry_in AND (A XOR B)) 
```

#### Ripple Carry Adder
The ripple carry adder creates a circuit using multiple full adders to add N-bit numbers. 
Each "carry out" from the previous adder becomes the "carry in" of the current adder. 
