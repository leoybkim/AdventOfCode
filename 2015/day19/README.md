# Day 19

[adventofcode.com/2015/day/19](https://adventofcode.com/2015/day/19)

Part 2 is something else. I think I *could* go down a rabbit hole learning the CYK algorithm or happily settle for a
greedy approach.

## Method 1: Shortcut

Note that the number of steps to build the molecule is related to the number of atoms in the final string.
In a simple grammar where every rule is in the form of `A -> BC`.
Then one atom becomes two atoms except for the very first step where you must start with `e -> X`.
So the total steps become `atoms - 1`.

Total atoms can be found with atom names starting with an upper case: `c.isupper() for c in molecule`.
Atoms `Rn` and `Ar` are special terminal atoms (at least for my puzzle input, and not a general solution) where they
only appear on the right side of the grammar equations.
Also, they always appear in pairs, surrounding other atoms. This means that for every grammar rule that generates these
pairs, you must subtract two steps because they don't generate any more atoms.
Additionally, `Y` atom also only appear on the right side of the equation.

## Method 2: Beam Search

Next, we can work backward from the target molecule down to `e` using breadth first search.
On each level of search, generate all possible next states from the current set of strings through reduction.
The runtime of BFS is `O(V + E)` where `V` is the number of vertices in the graph and `E` is the number of edges.
The issue with vanilla BFS is that the number of possible "molecules" (states) you can generate could be enormous.
The grammar rules allow for molecules to grow in complexity and length without a bound, the search space could be
infinite.
Therefore, you can set some limit to the number of states/molecules to queue on each search level.
This is a heuristic search and is not a general solution. This method may not find the correct answer for certain
inputs.

## Method 3: Context-Free Grammar[[1]](#1) Parsing Algorithm

The replacement rules in the puzzle are basically a collection of CFG production rules.
Context-free grammar is the second lowest level in the Chomsky hierarchy; more complex and flexible than Regular
grammars but simpler and more restrictive than Context-sensitive grammars.
Context-free grammar rules include any rules allowed by Regular grammars.

The basic idea behind the parsing algorithm is to determine if a given input string (target molecule from puzzle input)
can be derived by the grammar rules.
Finding the minimum steps to derive is the goal of this problem. For a grammar in CNF (Chompsky Normal Form), if a string has length $n$, any
derivation of string from any non-terminal will contain exactly $2n - 1$ steps. This is because each terminal
production $A -> a$ consumes one non-terminal and produces one terminal. Each binary production $A -> BC$ consumes one non-terminal and produces two non-terminal.
The total number of grammar rules applied to go from the start symbol to the string would be $n - 1 \; (binary \;rules) + n \; (terminal \;rules) = 2n - 1$.
But this is *if* the grammar is provided in CNF. The puzzle is asking for minimum steps took from the given input grammar rules which is in CFG but not necessarily in CNF.

TODO: come back to this puzzle, backreference might be possible?

### Regular Grammar [[2]](#2)

- ${W}$ is non-terminal and ${a,b}$ are terminals
- start variable $S$, $S = W$
- $
  Rules = \begin{cases}
  W \rightarrow a\\
  W \rightarrow b\\
  W \rightarrow aW\\
  W \rightarrow bW\\
  \end{cases}
  $
- left-hand side must be non-terminal and the right-side can at most have one terminal, or one terminal followed by a
  non-terminal.

### Context-Free Grammar

In addition to any rules allowed by Regular Grammars, CFG also allows:

- $A \rightarrow \alpha$
- $\alpha$ is a string of terminals and/or non-terminals, or empty.

Each production rule defines how to replace the variable/non-terminal regardless of the context.
And you apply this until there are no more variables left. The final result will be all terminal strings.
There is also a start variable (in our case `e`) to define the starting point.

### CYK Algorithm [[3]](#3)

- The grammar must be in Chomsky Normal Form (CNF)

#### Chomsky Normal Form (CNF) [[4]](#4)

- every production rule must be in the form of:
    - $A \rightarrow BC$ or $A \rightarrow a$ or $S \rightarrow \epsilon$
    - $A, B, C$ are any variables, and $a$ is any terminal
    - $B, C$ must not be the start variable
    - $S \rightarrow \epsilon$ is allowed if $S$ is the start variable ($\epsilon$ denotes empty string)
- every CFG can be transformed into CNF in 5 steps (order matters!):
    - **START**: eliminate the start variable from the right-hand sides
    - **TERM**: eliminate right-hand sides with both variables and terminals
    - **BIN**: eliminate right-hand sides with more than 2 variables
    - **DEL**: eliminate all $\epsilon$ rules ($A \rightarrow \epsilon$) not involving the start variable
    - **UNIT**: eliminate all unit rules ($A \rightarrow B$)

Based on our puzzle input, **START** has already been done. The starting variable `e` is only on the left-hand side of
the equation.

For **TERM**, the production rules must be in the form of $A \rightarrow BC$ or $A \rightarrow a$. You cannot mix
non-terminal and terminal together like $A \rightarrow aB$. For every terminal symbol that appears on the right-hand
side of a production rule along with other symbols (either other terminals or non-terminals), you introduce a new
non-terminal symbol and a new production rule. Based on my puzzle input, I have `Ar`, `Rn` and `Y` which are terminal
symbols that appear with other terminal and non-terminal symbols. I'll create new production rule for each and replace
them.
For example $W \rightarrow Ar$, $X \rightarrow Rn$, $Y \rightarrow Z$. So one of the production
rule $Ca \rightarrow SiRnFYFAr$ will now become $Ca \rightarrow SiXFZFW$.

Next step, **BIN** ensures that any production rule whose right-hand side consists only non-terminal
symbols has exactly _two_ non-terminal symbols.
For any production rule where there are more than two non-terminals on the right-hand side, you must introduce new
non-terminal symbols to break down the right-hand side into a sequence of binary pairs. For instance, if you have a rule
$A \rightarrow B_1B_2B_3...B_k \; where \; k < 2$

1. create a new non-terminal $N_1$, and a new rule $N_1 \rightarrow B_2B_3...B_k$
2. update the original rule: $A \rightarrow B_1N_1$ to make only contain two non-terminals on the RHS
3. repeat process until $N_1 \rightarrow B_2B_3...B_k$ has no more than two non-terminals on the RHS
    - create $N_2$, and rule $N_2 \rightarrow B_3...B_k$
    - update $N_1 \rightarrow B_2N_2$

In the **DEL** step we eliminate all $\epsilon$ rules ($A \rightarrow \epsilon$) not involving the start variable.
This step is not necessary for my puzzle input as I don't have any production rules that create nullable non-terminals.
But if there were such rules, you would eliminate them and also update other production rules to omit the nullable
non-terminals from the RHS.
For example, if the grammar rules are as follows:

- $S \rightarrow ABC$
- $A \rightarrow a$
- $B \rightarrow \epsilon$
- $C \rightarrow \epsilon$
- $C \rightarrow c$

We would identify non-terminal $\{B, C\}$ as nullable non-terminals and remove them from other production rules such
as $S \rightarrow ABC$. So the new production rule would become $S \rightarrow A$ in case $C$ is nullable
or $S \rightarrow AC$ in case it is $c$. And $A \rightarrow a$ and $C \rightarrow c$ would remain.

Final **UNIT** step eliminates unit production rules of the form $A \rightarrow B$ where both $A$ and $B$ are
non-terminal symbols. The CNF form only allows rules in the form of $A \rightarrow BC$ (two non-terminals on RHS)
or $A \rightarrow a$ (single termina on RHS). So a rule like $A \rightarrow B$ violates this form because it only
renames
a non-terminal without contributing to the derivation of terminal or a binary structure. So to do this, we create a new
production rule for every $B$ generating a terminal.
For example, if $A \rightarrow B$ and $B \rightarrow b$, then now $A \rightarrow b$ and $B \rightarrow b$.
And $A \rightarrow B$ can now be removed.

#### CYK Algorithm

Now that we have CFG in CNF, we can implement the CYK algorithm.
If our puzzle input (final target molecule string) $w$ is of length $n$:

- if $w$ is $\epsilon$, then there exists a rule $S \rightarrow \epsilon$
- if $w$ length of 1 can be derived from a variable $A$, then there exists a rule $A \rightarrow w$
- if $w$ length $\ge 2$ can be derived from variable A, then there exists a rule $A \rightarrow BC$ such that
    - $B$ derives the substring $w_{front}$
    - $C$ derives the substring $w_{back}$
    - where $w = w_{front} + w_{back}$

You can also work your way up from the bottom to parse a sentence. If you are trying to figure out if a whole sentence
is grammatically correct, CYK algorithm can approach this by first figuring out if small parts of the sentence (atoms
and molecules, in the case our puzzle) are grammatically correct.
Then it uses that information to figure out if slightly larger parts are correct, and so on, until it covers the entire
sentence.

If $w$ is of length $n$, $w = \sigma_1\sigma_2...\sigma_n$

- create CYK/DP table of $n \times n$ cells where `dp[i][j]` stores a set of variables that can generate the
  substring $\sigma_i\sigma_{i+1}...\sigma_n \; (i \le j)$
- if $w$ is empty, if $S \rightarrow \epsilon$ exists then return `True` else `False`
- For `i = 1 ... n`:
    - for each variable $A$: If $A \rightarrow \sigma_i$ exists, then insert $A$ into `dp[i][j]`
- For `l = 2 ... n`:
    - For `i = 1 ...(N - l + 1):`
        - Let `j = i + 1 - 1`; For `k = i ... (j -1)`:
            - For each rule $A \rightarrow BC$: If `dp[i][k]` contains $B$ and
              `dp[k+1][j]` contains $C$, then insert $A$ into `dp[i][j]`
- If `dp[1][n]` contains $S$ return `True` else `False`

#### References

<a id="1">[1]</a> Context-free grammar [https://en.wikipedia.org/wiki/Context-free_grammar](https://en.wikipedia.org/wiki/Context-free_grammar)\
<a id="1">[2]</a> Regular grammar [https://en.wikipedia.org/wiki/Regular_grammar](https://en.wikipedia.org/wiki/Regular_grammar)\
<a id="1">[3]</a> CYK algorithm [https://en.wikipedia.org/wiki/CYK_algorithm](https://en.wikipedia.org/wiki/CYK_algorithm)\
<a id="1">[4]</a> Chomsky normal form [https://en.wikipedia.org/wiki/Chomsky_normal_form](https://en.wikipedia.org/wiki/Chomsky_normal_form)