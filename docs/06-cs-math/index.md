# CS math

Number representation, number theory, counting, recurrences and algorithm analysis, graphs, and the theory of computation.

Before this folder: Proofs and logic, plus the probability chapter of the university core for discrete probability.

## How to use this folder

Each chapter has its own cheat sheet (the links are below), and each lesson starts with a quick check, so you can test yourself before reading it. If you already know a chapter, read its cheat sheet and do only the lessons whose quick check you miss. The chapters build in order: number representation and number theory first, then counting, then sums and recurrences, then graphs, then the theory of computation, which leans on the proof techniques of the earlier folder.

The [Anki deck for this folder](../downloads/anki/06-cs-math.apkg) holds the base conversions, two's complement and floating point facts, modular arithmetic and Euclid's algorithm, the counting formulas, the closed forms and recurrence methods, the graph theorems, and the definitions of the machine models and complexity classes, including pairs that are easy to confuse, such as a trail and a path, recognizable and decidable, and NP-hard and NP-complete. In Anki desktop choose File, then Import, and [Anki decks](../00-start-here/index.md#anki-decks) covers phones.

## Fast path for a CS student

If you are short on time, these lessons carry the most weight in courses on proofs, algorithms and the theory of computation. They are listed in reading order, so each one only needs the ones above it.

| Lesson | Where it comes back |
|---|---|
| [Binary arithmetic and two's complement](01-number-representation/03-binary-arithmetic-and-twos-complement.md) | integer overflow bugs, and what `int` really means in C, Java and Rust |
| [Divisibility and modular arithmetic](02-number-theory/01-divisibility-and-modular-arithmetic.md) | hash tables, checksums and every cryptography course |
| [GCD and Euclid's algorithm](02-number-theory/02-gcd-and-euclids-algorithm.md) | the first algorithm with a proof of correctness and a running time |
| [Fermat, Euler and fast exponentiation](02-number-theory/05-fermat-euler-and-fast-exponentiation.md) | [RSA](02-number-theory/06-rsa-cryptography.md), primality tests and repeated squaring |
| [Counting rules](03-counting-and-discrete-probability/01-counting-rules.md) | counting the cases of an algorithm, and sizes of search spaces |
| [Permutations and combinations](03-counting-and-discrete-probability/02-permutations-and-combinations.md) | brute-force costs such as $n!$ and $2^n$, and the binomial distribution |
| [Discrete probability](03-counting-and-discrete-probability/05-discrete-probability.md) | randomized algorithms, hashing and expected running time |
| [Sums and closed forms](04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md) | the cost of nested loops |
| [Recurrences](04-sums-recurrences-and-algorithms/02-recurrences.md) | the running time of recursive algorithms |
| [Invariants and algorithm correctness](04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md) | proving a loop correct, and finding bugs in binary search |
| [Asymptotic notation](04-sums-recurrences-and-algorithms/04-asymptotic-notation.md) | every statement of the form "this algorithm is $O(n \log n)$" |
| [Divide and conquer and the master theorem](04-sums-recurrences-and-algorithms/05-divide-and-conquer-and-master-theorem.md) | merge sort, quicksort, fast multiplication and binary search |
| [Graph basics](05-graphs/01-graph-basics.md) | data structures for graphs, and the handshake lemma |
| [Paths, connectivity and trees](05-graphs/02-paths-connectivity-and-trees.md) | BFS, spanning trees and Kruskal's algorithm |
| [Finite automata: DFA and NFA](06-theory-of-computation/01-finite-automata-dfa-and-nfa.md) | lexers, regular expression engines and protocol state machines |
| [Regular expressions and the pumping lemma](06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md) | proving a language is not regular |
| [Context-free grammars and pushdown automata](06-theory-of-computation/03-context-free-grammars-and-pushdown-automata.md) | parsers and the syntax of programming languages |
| [Turing machines and the Church-Turing thesis](06-theory-of-computation/04-turing-machines-and-church-turing-thesis.md) | the definition of "algorithm" used in the rest of the theory |
| [Decidability and the halting problem](06-theory-of-computation/05-decidability-and-the-halting-problem.md) | the diagonal argument, and why no tool finds every bug |
| [Reductions and undecidability](06-theory-of-computation/06-reductions-and-undecidability.md) | the template for every hardness proof |
| [P, NP and NP-completeness](06-theory-of-computation/07-p-np-and-np-completeness.md) | recognizing a hard problem, and the polynomial-time reductions of an algorithms course |

The lessons not in the table can wait. Come back to floating point when a numerical bug appears, to bitwise operations and Boolean algebra before a computer architecture course, to primes and modular inverses before RSA, to inclusion-exclusion when a counting problem has overlapping cases, and to bipartite graphs, colouring and planar graphs when a course reaches matchings or graph colouring.

## Cheat sheet

Each chapter has a cheat sheet with the rules, tables and common mistakes of its lessons. This is the map.

- [Number representation](01-number-representation/index.md#cheat-sheet) covers base conversions, bits and entropy, two's complement and overflow, floating point, bitwise masks and Boolean algebra.
- [Number theory](02-number-theory/index.md#cheat-sheet) covers divisibility and congruences, Euclid's algorithm and Bezout, unique factorization, modular inverses and the Chinese remainder theorem, Fermat and Euler, and RSA.
- [Counting and discrete probability](03-counting-and-discrete-probability/index.md#cheat-sheet) covers the counting rules, permutations and combinations, the binomial theorem, inclusion-exclusion, the pigeonhole principle and discrete probability.
- [Sums, recurrences and algorithms](04-sums-recurrences-and-algorithms/index.md#cheat-sheet) covers closed forms, solving recurrences, loop invariants, asymptotic notation and the master theorem.
- [Graphs](05-graphs/index.md#cheat-sheet) covers degrees and isomorphism, paths and trees, BFS and spanning trees, bipartite graphs and matchings, colouring and planar graphs.
- [Theory of computation](06-theory-of-computation/index.md#cheat-sheet) covers automata, regular expressions, grammars, Turing machines, decidability, reductions and NP-completeness.

The results used most often in later courses are below in short form.

| Topic | The result to keep |
|---|---|
| positional notation | $d_k \dots d_0$ in base $b$ means $\sum d_i b^i$ |
| bits | $n$ bits hold $2^n$ values, and $N$ values need $\lceil \log_2 N \rceil$ bits |
| two's complement | $n$ bits give $-2^{n-1}$ to $2^{n-1} - 1$, and $-x$ is flip the bits and add 1 |
| Euclid | $\gcd(a, b) = \gcd(b, a \bmod b)$, and $ax + by = \gcd(a, b)$ has a solution |
| subsets | an $n$-set has $2^n$ subsets and $\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$ of size $k$ |
| inclusion-exclusion | $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$ |
| geometric sum | $\sum_{k=0}^{n} r^k = \frac{r^{n+1} - 1}{r - 1}$ for $r \ne 1$ |
| loop cost | $\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$, so a triangular double loop is $\Theta(n^2)$ |
| characteristic equation | $a_n = c_1 a_{n-1} + c_2 a_{n-2}$ gives $r^2 = c_1 r + c_2$ |
| handshake | $\sum_v \deg(v) = 2\lvert E \rvert$ |
| tree | $n$ vertices, connected with $n - 1$ edges |
| Euler circuit | connected with every degree even |
| planar | $V - E + F = 2$, and $E \le 3V - 6$ |
| pumping lemma | $s = xyz$ with $xy^i z \in A$, $\lvert y \rvert > 0$, $\lvert xy \rvert \le p$ |
| reduction | $A \le_m B$ and $B$ decidable give $A$ decidable |
| NP-complete | in NP and every NP problem reduces to it in polynomial time |

<!-- lessons:start -->
## Lessons

### 1. [Number representation](01-number-representation/index.md)

1. [Number bases and conversions](01-number-representation/01-number-bases-and-conversions.md)
2. [Bits and information](01-number-representation/02-bits-and-information.md)
3. [Binary arithmetic and two's complement](01-number-representation/03-binary-arithmetic-and-twos-complement.md)
4. [Floating point basics](01-number-representation/04-floating-point-basics.md)
5. [Bitwise operations and masks](01-number-representation/05-bitwise-operations-and-masks.md)
6. [Boolean algebra and logic gates](01-number-representation/06-boolean-algebra-and-logic-gates.md)

### 2. [Number theory](02-number-theory/index.md)

1. [Divisibility and modular arithmetic](02-number-theory/01-divisibility-and-modular-arithmetic.md)
2. [GCD and Euclid's algorithm](02-number-theory/02-gcd-and-euclids-algorithm.md)
3. [Primes and unique factorization](02-number-theory/03-primes-and-unique-factorization.md)
4. [Modular inverses and the Chinese remainder theorem](02-number-theory/04-modular-inverses-and-chinese-remainder-theorem.md)
5. [Fermat, Euler and fast exponentiation](02-number-theory/05-fermat-euler-and-fast-exponentiation.md)
6. [RSA cryptography](02-number-theory/06-rsa-cryptography.md)

### 3. [Counting and discrete probability](03-counting-and-discrete-probability/index.md)

1. [Counting rules](03-counting-and-discrete-probability/01-counting-rules.md)
2. [Permutations and combinations](03-counting-and-discrete-probability/02-permutations-and-combinations.md)
3. [The binomial theorem and combinatorial proofs](03-counting-and-discrete-probability/03-binomial-theorem-and-combinatorial-proofs.md)
4. [Inclusion-exclusion and the pigeonhole principle](03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md)
5. [Discrete probability](03-counting-and-discrete-probability/05-discrete-probability.md)

### 4. [Sums, recurrences and algorithms](04-sums-recurrences-and-algorithms/index.md)

1. [Sums and closed forms](04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md)
2. [Recurrences](04-sums-recurrences-and-algorithms/02-recurrences.md)
3. [Invariants and algorithm correctness](04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md)
4. [Asymptotic notation](04-sums-recurrences-and-algorithms/04-asymptotic-notation.md)
5. [Divide and conquer and the master theorem](04-sums-recurrences-and-algorithms/05-divide-and-conquer-and-master-theorem.md)

### 5. [Graphs](05-graphs/index.md)

1. [Graph basics](05-graphs/01-graph-basics.md)
2. [Paths, connectivity and trees](05-graphs/02-paths-connectivity-and-trees.md)
3. [Bipartite graphs, colouring and planar graphs](05-graphs/03-bipartite-coloring-and-planar-graphs.md)

### 6. [Theory of computation](06-theory-of-computation/index.md)

1. [Finite automata: DFA and NFA](06-theory-of-computation/01-finite-automata-dfa-and-nfa.md)
2. [Regular expressions and the pumping lemma](06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md)
3. [Context-free grammars and pushdown automata](06-theory-of-computation/03-context-free-grammars-and-pushdown-automata.md)
4. [Turing machines and the Church-Turing thesis](06-theory-of-computation/04-turing-machines-and-church-turing-thesis.md)
5. [Decidability and the halting problem](06-theory-of-computation/05-decidability-and-the-halting-problem.md)
6. [Reductions and undecidability](06-theory-of-computation/06-reductions-and-undecidability.md)
7. [P, NP and NP-completeness](06-theory-of-computation/07-p-np-and-np-completeness.md)

<!-- lessons:end -->
