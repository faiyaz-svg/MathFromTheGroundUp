# CS math diagnostic

This quiz covers the 32 lessons of the CS math folder: two questions on each lesson, 64 in all. None of the lessons is optional. Take it without notes, and write every answer down before you look at the answers. A calculator is allowed, and a computer is not. Most questions take one to three minutes, so plan on four or five sittings rather than one. Every question here is a small version of something its lesson teaches, and none asks for a full proof.

Mark each answer right, wrong or guessed. A guess counts as wrong, even when it turns out right. Then do only the lessons behind the questions you marked wrong or guessed; the answer table names the lesson for each one. Several questions ask for a reason, and an answer without its reason counts as wrong. All data in the questions are made up (hypothetical).

## Number representation

1\. Convert $10110110_2$ to decimal and to hexadecimal, and convert $213$ to binary.

2\. Convert $0.6875$ to binary, and convert $100$ to base 7.

3\. How many bits are needed to give each of 1000 items its own label? Find the entropy of a source with three outcomes of probabilities $\frac{1}{2}$, $\frac{1}{4}$ and $\frac{1}{4}$.

4\. Find the entropy of a coin with $P(\text{heads}) = 0.9$ to three decimal places. Why is it below 1 bit?

5\. In 8-bit two's complement, write $-45$, and find the value of $10010110$.

6\. Add $100 + 50$ in 8-bit two's complement. Give the 8-bit result and its value, and say whether overflow happened.

7\. Decode the binary32 float with hex pattern `40490000` (1 sign bit, 8 exponent bits with bias 127, 23 fraction bits).

8\. In Python, what do `0.1 + 0.2 == 0.3` and `2.0**53 + 1 == 2.0**53` give, and why?

9\. Find $1100_2 \mathbin{\&} 1010_2$, $1100_2 \mid 1010_2$ and $1100_2 \oplus 1010_2$ in binary, and find $13 \ll 2$ and $200 \gg 3$.

10\. For $x = 10100101_2$, write the result of setting bit 3, of clearing bit 2 and of testing bit 5 (bit 0 is the rightmost). Then find $44 \mathbin{\&} 43$ and say what `x & (x - 1)` does in general.

11\. Simplify $AB + AB' + A'B$ with Boolean algebra, and write the negation of "$A$ and not $B$" with De Morgan's law.

12\. Build NOT from NAND gates alone. Give the sum and carry outputs of a half adder, and the sum and carry of a full adder with inputs $1, 1, 1$.

## Number theory

13\. Find $-17 \bmod 5$, and find $123456 \bmod 9$ without long division.

14\. Find the last digit of $7^{2026}$.

15\. Use Euclid's algorithm to find $\gcd(1071, 462)$, showing each step.

16\. Find integers $x$ and $y$ with $240x + 46y = \gcd(240, 46)$.

17\. Factor $360$ into primes and count its positive divisors.

18\. Is $391$ prime? Up to what bound must you test divisors? Give the prime factorization if it is composite.

19\. Find the inverse of $7$ modulo $26$. Does $6$ have an inverse modulo $15$?

20\. Find the $x$ with $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$ and $x \equiv 2 \pmod 7$, and say modulo what it is unique.

21\. Use Fermat's little theorem to find $3^{100} \bmod 7$.

22\. Find $\varphi(36)$, and compute $3^{13} \bmod 50$ by repeated squaring, using the binary form of 13.

23\. Take the toy RSA primes $p = 5$ and $q = 11$ with $e = 3$. Find $n$, $\varphi(n)$ and the private exponent $d$.

24\. With the key of the previous question, encrypt $m = 9$ and decrypt the result. Which numbers are public?

## Counting and discrete probability

25\. A licence plate has 3 letters followed by 3 digits. How many plates are there?

26\. How many 8-bit strings start with 1 or end with 0? How many 4-letter strings from 26 lowercase letters have no repeated letter?

27\. How many distinct arrangements of the letters of LEVEL are there?

28\. A committee of 3 is chosen from 10 people. How many committees are there, and how many are there if two particular people refuse to serve together?

29\. Find the coefficient of $x^3$ in $(2x + 1)^5$.

30\. Evaluate $\sum_{k=0}^{6} \binom{6}{k} 2^k$, and check Pascal's rule on $\binom{7}{3}$. Give the committee argument for the rule in one sentence.

31\. How many integers from 1 to 100 are divisible by 2, 3 or 5?

32\. How many cards must you draw from a standard deck to be sure of two of the same suit? Among 100 people, what is the largest number that must share a birth month, at least?

33\. Two fair dice are rolled. Find $P(\text{sum is } 8)$ and $P(\text{sum is } 8 \mid \text{first die is } 3)$.

34\. A fair die is rolled 4 times. Find the probability of at least one six, and the expected number of sixes.

## Sums, recurrences and algorithms

35\. Evaluate $\sum_{k=1}^{100} k$ and $\sum_{k=0}^{9} 3 \cdot 2^k$.

36\. Evaluate $\sum_{k=1}^{20} k^2$ and $\sum_{k=0}^{\infty} \left(\frac{1}{3}\right)^k$.

37\. Solve $a_n = 2a_{n-1} + 1$ with $a_0 = 0$ by finding a closed form, and give $a_{10}$.

38\. Solve $a_n = a_{n-1} + 6a_{n-2}$ with $a_0 = 1$ and $a_1 = 2$. Give a closed form and $a_5$.

39\. A loop starts with `s = 0, i = 0` and repeats `i += 1; s += 2*i - 1` while `i < n`. State a loop invariant and what it proves when the loop ends.

40\. Binary search runs on a sorted array of 1000 items. State the invariant that makes it correct, and the most comparisons it can need.

41\. Order from slowest-growing to fastest-growing: $n^2$, $2^n$, $\log n$, $n \log n$, $n$.

42\. Show $3n^2 + 10n + 5 = O(n^2)$ by giving constants $c$ and $n_0$. Is $2^{n+1} = O(2^n)$? Is $2^{2n} = O(2^n)$?

43\. Use the master theorem on (a) $T(n) = 2T(n/2) + n$, (b) $T(n) = 4T(n/2) + n$ and (c) $T(n) = T(n/2) + 1$.

44\. Use the master theorem on $T(n) = 3T(n/2) + n^2$. Then solve $T(n) = 2T(n/2) + n$ exactly for $n = 1024$ with $T(1) = 0$.

## Graphs

45\. A simple graph has 5 vertices with degrees $3, 3, 2, 2, 2$. How many edges does it have? Can a simple graph have degrees $3, 3, 2, 2, 1$? How many edges does $K_7$ have?

46\. A graph on vertices 1 to 4 has edges 12, 23, 13 and 34. Write its adjacency matrix $A$ and find the number of walks of length 2 from vertex 1 to vertex 3.

47\. A graph has edges AB, AC, BD, CD, DE, EF and CF. Run breadth-first search from A and give the distance to every vertex.

48\. A connected graph has 10 vertices and 12 edges. How many edges must be deleted to get a spanning tree? A tree has 8 leaves and every other vertex has degree 3. How many vertices does it have?

49\. Is $C_5$ bipartite? Is $C_6$? Give the chromatic number of $C_5$, $C_6$ and $K_4$.

50\. A connected planar graph has 6 vertices and 9 edges. How many faces does it have? Why is $K_5$ not planar?

## Theory of computation

51\. A DFA reads a binary number left to right with states $r_0, r_1, r_2$, moving from $r$ to $(2r + b) \bmod 3$ on bit $b$. It starts and accepts at $r_0$. Does it accept $1100$? Does it accept $1011$? What does it test?

52\. An NFA has states $q_0, q_1, q_2$. State $q_0$ loops on 0 and 1, $q_0 \xrightarrow{0} q_1$, $q_1 \xrightarrow{1} q_2$, and $q_2$ accepts. Does it accept $1101$? $0110$? At most how many states can the subset construction give?

53\. Write a regular expression for strings over $\{a, b\}$ with exactly one $a$, and one for strings that end in $ab$.

54\. True or false, with a reason: the pumping lemma can prove that a language is regular. Then say where the pumped part $y$ lies for $0^p1^p$, and why pumping leaves the language $\{0^n 1^n\}$.

55\. Write a grammar for balanced parentheses and derive `(())` from it.

56\. A PDA for $\{0^n 1^n\}$ pushes a symbol for each 0 and pops one for each 1. How many symbols are on the stack after reading $0001$? Which of $\{a^n b^n\}$, $\{a^n b^n c^n\}$ and $\{ww^R\}$ are context-free?

57\. A one-state Turing machine reads a cell, writes the flipped bit (0 becomes 1, 1 becomes 0), moves right, and accepts on the first blank. What is on the tape at the end for input $1011$?

58\. State the Church-Turing thesis. Why is it a thesis and not a theorem? Does a multi-tape machine decide more languages than a single-tape machine?

59\. Which are decidable: (a) whether a given DFA accepts a given string, (b) whether a given DFA accepts some string, (c) whether a given program halts on a given input?

60\. In the proof that the halting problem is undecidable, a program $D$ runs a supposed decider $H$ on $(P, P)$ and does the opposite of the answer. What happens when $D$ runs on its own code?

61\. If $A \le_m B$ and $B$ is decidable, what follows about $A$? If $A$ is undecidable, what follows about $B$?

62\. Use Rice's theorem to decide whether "the language of machine $M$ is empty" is decidable, and say why "$M$ has at least 5 states" is not covered by it.

63\. For the SUBSET-SUM instance $\{3, 34, 4, 12, 5, 2\}$ with target 9, give a certificate and say why this shows the problem is in NP.

64\. Define NP-complete in one sentence. What would follow if a polynomial-time algorithm for 3-SAT were found?

## Answers

<details class="solution" markdown>
<summary>Answers</summary>

| Question | Answer | Working | Study |
|---|---|---|---|
| 1 | 182; B6 (hex); $11010101_2$ | $128 + 32 + 16 + 4 + 2 = 182$, and the nibbles 1011 and 0110 are B and 6. For 213: $128 + 64 + 16 + 4 + 1$. | [Number bases and conversions](01-number-representation/01-number-bases-and-conversions.md) |
| 2 | $0.1011_2$; $202_7$ | $0.6875 \cdot 16 = 11 = 1011_2$, so the fraction is $0.1011$. And $100 = 2 \cdot 49 + 0 \cdot 7 + 2$. | [Number bases and conversions](01-number-representation/01-number-bases-and-conversions.md) |
| 3 | 10 bits; 1.5 bits | $2^{9} = 512 < 1000 \le 1024 = 2^{10}$. The entropy is $\frac{1}{2}(1) + \frac{1}{4}(2) + \frac{1}{4}(2)$. | [Bits and information](01-number-representation/02-bits-and-information.md) |
| 4 | About 0.469 bits; the outcome is predictable | $-0.9\log_2 0.9 - 0.1\log_2 0.1 = 0.137 + 0.332$. Heads is usually the outcome, so each flip carries less surprise on average. | [Bits and information](01-number-representation/02-bits-and-information.md) |
| 5 | $11010011$; $-106$ | $45 = 00101101$; flip the bits and add 1. And $10010110 = 150 - 256$. | [Binary arithmetic and two's complement](01-number-representation/03-binary-arithmetic-and-twos-complement.md) |
| 6 | $10010110$; $-106$; overflow | $100 + 50 = 150$ is above the largest value 127. Two positive numbers gave a negative result. | [Binary arithmetic and two's complement](01-number-representation/03-binary-arithmetic-and-twos-complement.md) |
| 7 | $3.140625$ | The sign is 0 and the exponent field is 128, so $e = 1$. The fraction is $0.5 + 0.0625 + 0.0078125 = 0.5703125$, so the value is $1.5703125 \cdot 2$. | [Floating point basics](01-number-representation/04-floating-point-basics.md) |
| 8 | False; True | $0.1$, $0.2$ and $0.3$ have no exact binary form, so the sums differ by rounding. Above $2^{53}$ a double cannot hold every integer, and $2^{53} + 1$ rounds back to $2^{53}$. | [Floating point basics](01-number-representation/04-floating-point-basics.md) |
| 9 | $1000_2$, $1110_2$, $0110_2$; 52; 25 | Compare bit by bit. Shifting left by 2 multiplies by 4, and $200 \gg 3$ is $\lfloor 200 / 8 \rfloor$. | [Bitwise operations and masks](01-number-representation/05-bitwise-operations-and-masks.md) |
| 10 | $10101101_2$; $10100001_2$; bit 5 is set; 40; it clears the lowest set bit | Use OR with $1 \ll 3$, AND with the complement of $1 \ll 2$, and AND with $1 \ll 5$. And $101100 \mathbin{\&} 101011 = 101000$. A power of two gives 0. | [Bitwise operations and masks](01-number-representation/05-bitwise-operations-and-masks.md) |
| 11 | $A + B$; $\lnot A \lor B$ | $AB + AB' = A$, then $A + A'B = A + B$. De Morgan gives $\lnot(A \land \lnot B) = \lnot A \lor B$. | [Boolean algebra and logic gates](01-number-representation/06-boolean-algebra-and-logic-gates.md) |
| 12 | $\lnot A = A \text{ NAND } A$; half adder: sum $= A \oplus B$, carry $= A \land B$; full adder: sum 1, carry 1 | A NAND with both inputs equal is a NOT. For the full adder, $1 + 1 + 1 = 3 = 11_2$. | [Boolean algebra and logic gates](01-number-representation/06-boolean-algebra-and-logic-gates.md) |
| 13 | 3; 3 | $-17 = -4 \cdot 5 + 3$. A number is congruent to its digit sum mod 9, and $1+2+3+4+5+6 = 21$, so $21 \bmod 9 = 3$. | [Divisibility and modular arithmetic](02-number-theory/01-divisibility-and-modular-arithmetic.md) |
| 14 | 9 | The last digits of powers of 7 cycle 7, 9, 3, 1 with period 4, and $2026 \bmod 4 = 2$. | [Divisibility and modular arithmetic](02-number-theory/01-divisibility-and-modular-arithmetic.md) |
| 15 | 21 | $1071 = 2 \cdot 462 + 147$, $462 = 3 \cdot 147 + 21$, $147 = 7 \cdot 21 + 0$. | [GCD and Euclid's algorithm](02-number-theory/02-gcd-and-euclids-algorithm.md) |
| 16 | $x = -9$, $y = 47$ (gcd 2) | $240 = 5 \cdot 46 + 10$, $46 = 4 \cdot 10 + 6$, $10 = 6 + 4$, $6 = 4 + 2$. Back-substituting gives $2 = -9 \cdot 240 + 47 \cdot 46$. | [GCD and Euclid's algorithm](02-number-theory/02-gcd-and-euclids-algorithm.md) |
| 17 | $2^3 \cdot 3^2 \cdot 5$; 24 divisors | Add 1 to each exponent and multiply: $4 \cdot 3 \cdot 2$. | [Primes and unique factorization](02-number-theory/03-primes-and-unique-factorization.md) |
| 18 | Composite, $391 = 17 \cdot 23$; test primes up to 19 | A composite number has a prime factor at most $\sqrt{391} \approx 19.8$. | [Primes and unique factorization](02-number-theory/03-primes-and-unique-factorization.md) |
| 19 | 15; no | $7 \cdot 15 = 105 = 4 \cdot 26 + 1$. And $\gcd(6, 15) = 3$ is not 1, so no inverse exists. | [Modular inverses and the Chinese remainder theorem](02-number-theory/04-modular-inverses-and-chinese-remainder-theorem.md) |
| 20 | $x = 23$, unique modulo 105 | $23 = 7 \cdot 3 + 2 = 4 \cdot 5 + 3 = 3 \cdot 7 + 2$. The moduli are pairwise coprime and $3 \cdot 5 \cdot 7 = 105$. | [Modular inverses and the Chinese remainder theorem](02-number-theory/04-modular-inverses-and-chinese-remainder-theorem.md) |
| 21 | 4 | $3^6 \equiv 1 \pmod 7$ and $100 = 16 \cdot 6 + 4$, so $3^{100} \equiv 3^4 = 81 \equiv 4$. | [Fermat, Euler and fast exponentiation](02-number-theory/05-fermat-euler-and-fast-exponentiation.md) |
| 22 | 12; 23 | $\varphi(36) = 36 \cdot \frac{1}{2} \cdot \frac{2}{3}$. With $13 = 1101_2$: $3^2 = 9$, $3^4 = 81 \equiv 31$, $3^8 \equiv 961 \equiv 11$, and $3^{13} = 3^8 \cdot 3^4 \cdot 3 \equiv 11 \cdot 31 \cdot 3 \equiv 23$. | [Fermat, Euler and fast exponentiation](02-number-theory/05-fermat-euler-and-fast-exponentiation.md) |
| 23 | $n = 55$, $\varphi(n) = 40$, $d = 27$ | $\varphi(55) = 4 \cdot 10$. Then $3 \cdot 27 = 81 = 2 \cdot 40 + 1$. | [RSA cryptography](02-number-theory/06-rsa-cryptography.md) |
| 24 | $c = 14$; decrypts to 9; public: $n = 55$ and $e = 3$ | $9^3 = 729 = 13 \cdot 55 + 14$, and $14^{27} \equiv 9 \pmod{55}$. The numbers $p$, $q$, $\varphi(n)$ and $d$ stay private. | [RSA cryptography](02-number-theory/06-rsa-cryptography.md) |
| 25 | $17{,}576{,}000$ | $26^3 \cdot 10^3$ by the product rule. | [Counting rules](03-counting-and-discrete-probability/01-counting-rules.md) |
| 26 | 192; $358{,}800$ | Start with 1: 128. End with 0: 128. Both: 64. So $128 + 128 - 64$. And $26 \cdot 25 \cdot 24 \cdot 23$. | [Counting rules](03-counting-and-discrete-probability/01-counting-rules.md) |
| 27 | 30 | $\frac{5!}{2!\,2!}$, since L and E each appear twice. | [Permutations and combinations](03-counting-and-discrete-probability/02-permutations-and-combinations.md) |
| 28 | 120; 112 | $\binom{10}{3}$. Committees holding both people: $\binom{8}{1} = 8$, so $120 - 8$. | [Permutations and combinations](03-counting-and-discrete-probability/02-permutations-and-combinations.md) |
| 29 | 80 | The term is $\binom{5}{3}(2x)^3 \cdot 1^2 = 10 \cdot 8x^3$. | [The binomial theorem and combinatorial proofs](03-counting-and-discrete-probability/03-binomial-theorem-and-combinatorial-proofs.md) |
| 30 | 729; $35 = 15 + 20$ | The sum is $(1 + 2)^6 = 3^6$. Pascal: $\binom{6}{2} + \binom{6}{3}$. A committee of 3 from 7 either includes a chosen person (pick 2 from the other 6) or does not (pick 3 from the other 6). | [The binomial theorem and combinatorial proofs](03-counting-and-discrete-probability/03-binomial-theorem-and-combinatorial-proofs.md) |
| 31 | 74 | $50 + 33 + 20 - 16 - 10 - 6 + 3$. | [Inclusion-exclusion and the pigeonhole principle](03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md) |
| 32 | 5; 9 | Four suits can each hold one card, so the fifth card forces a match. And $\lceil 100 / 12 \rceil = 9$. | [Inclusion-exclusion and the pigeonhole principle](03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md) |
| 33 | $\frac{5}{36}$; $\frac{1}{6}$ | The pairs are (2,6), (3,5), (4,4), (5,3), (6,2). With a first die 3, only a second die 5 works, out of 6. | [Discrete probability](03-counting-and-discrete-probability/05-discrete-probability.md) |
| 34 | $\frac{671}{1296} \approx 0.518$; $\frac{2}{3}$ | $1 - \left(\frac{5}{6}\right)^4$. By linearity the expected count is $4 \cdot \frac{1}{6}$. | [Discrete probability](03-counting-and-discrete-probability/05-discrete-probability.md) |
| 35 | 5050; 3069 | $\frac{100 \cdot 101}{2}$, and $3(2^{10} - 1)$. | [Sums and closed forms](04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md) |
| 36 | 2870; $\frac{3}{2}$ | $\frac{20 \cdot 21 \cdot 41}{6} = 2870$, and $\frac{1}{1 - \frac{1}{3}}$. | [Sums and closed forms](04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md) |
| 37 | $a_n = 2^n - 1$; $a_{10} = 1023$ | Add 1 to both sides: $a_n + 1 = 2(a_{n-1} + 1)$ with $a_0 + 1 = 1$. | [Recurrences](04-sums-recurrences-and-algorithms/02-recurrences.md) |
| 38 | $a_n = \frac{4}{5}3^n + \frac{1}{5}(-2)^n$; 188 | The roots of $r^2 = r + 6$ are 3 and $-2$. Then $A + B = 1$ and $3A - 2B = 2$. The terms are 1, 2, 8, 20, 68, 188. | [Recurrences](04-sums-recurrences-and-algorithms/02-recurrences.md) |
| 39 | $s = i^2$ after each pass; at the end $i = n$, so $s = n^2$ | Initially $0 = 0^2$, and each pass adds $2(i+1) - 1$ to $i^2$ to give $(i+1)^2$. | [Invariants and algorithm correctness](04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md) |
| 40 | If the target is present, it lies in $a[lo..hi]$; 10 comparisons | Each step halves the range. $\lfloor \log_2 1000 \rfloor + 1 = 10$. | [Invariants and algorithm correctness](04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md) |
| 41 | $\log n$, $n$, $n \log n$, $n^2$, $2^n$ | Logarithms grow slower than any power, and exponentials beat every polynomial. | [Asymptotic notation](04-sums-recurrences-and-algorithms/04-asymptotic-notation.md) |
| 42 | $c = 4$, $n_0 = 11$; yes; no | $3n^2 + 10n + 5 \le 4n^2$ exactly when $n^2 - 10n - 5 \ge 0$, true for $n \ge 11$. And $2^{n+1} = 2 \cdot 2^n$, but $2^{2n} = 2^n \cdot 2^n$ is not bounded by a constant times $2^n$. | [Asymptotic notation](04-sums-recurrences-and-algorithms/04-asymptotic-notation.md) |
| 43 | (a) $\Theta(n \log n)$; (b) $\Theta(n^2)$; (c) $\Theta(\log n)$ | Compare $n^{\log_b a}$ with $f(n)$: (a) $n^1$ ties with $n$; (b) $n^2$ beats $n$; (c) $n^0 = 1$ ties with 1. | [Divide and conquer and the master theorem](04-sums-recurrences-and-algorithms/05-divide-and-conquer-and-master-theorem.md) |
| 44 | $\Theta(n^2)$; 10240 | Here $n^{\log_2 3} \approx n^{1.58}$ is smaller than $n^2$, and the regularity condition holds. The exact solution is $n \log_2 n = 1024 \cdot 10$. | [Divide and conquer and the master theorem](04-sums-recurrences-and-algorithms/05-divide-and-conquer-and-master-theorem.md) |
| 45 | 6 edges; no; 21 | The degree sum 12 is twice the edges. The sum $3+3+2+2+1 = 11$ is odd. And $\binom{7}{2} = 21$. | [Graph basics](05-graphs/01-graph-basics.md) |
| 46 | One walk | Row 1 of $A$ is $(0,1,1,0)$ and column 3 is $(1,1,0,1)$, so the dot product is 1, through vertex 2. | [Graph basics](05-graphs/01-graph-basics.md) |
| 47 | A 0, B 1, C 1, D 2, F 2, E 3 | The neighbours of A are B and C, then D (from B) and F (from C), then E. | [Paths, connectivity and trees](05-graphs/02-paths-connectivity-and-trees.md) |
| 48 | 3; 14 | A spanning tree has 9 edges, and $12 - 9 = 3$. With 8 leaves and $k$ internal vertices, the degree sum is $8 + 3k = 2(8 + k - 1)$, so $k = 6$. | [Paths, connectivity and trees](05-graphs/02-paths-connectivity-and-trees.md) |
| 49 | No; yes; 3, 2, 4 | $C_5$ has an odd cycle. $C_6$ alternates two colours. $K_4$ needs four colours since all vertices are adjacent. | [Bipartite graphs, colouring and planar graphs](05-graphs/03-bipartite-coloring-and-planar-graphs.md) |
| 50 | 5 faces; $E = 10 > 3V - 6 = 9$ | Euler's formula gives $6 - 9 + F = 2$. A simple planar graph with $V \ge 3$ has at most $3V - 6$ edges. | [Bipartite graphs, colouring and planar graphs](05-graphs/03-bipartite-coloring-and-planar-graphs.md) |
| 51 | Yes; no; whether the number is divisible by 3 | $1100_2 = 12$ ends at $r_0$, and $1011_2 = 11$ ends at $r_2$. The state is the remainder mod 3. | [Finite automata: DFA and NFA](06-theory-of-computation/01-finite-automata-dfa-and-nfa.md) |
| 52 | Yes; no; 8 | $1101$ ends in 01, and $0110$ ends in 10. The subset construction has at most $2^3$ states. | [Finite automata: DFA and NFA](06-theory-of-computation/01-finite-automata-dfa-and-nfa.md) |
| 53 | $b^* a b^*$; $(a \cup b)^* ab$ | After the single $a$ only $b$s are allowed. For the second, anything may come before the final $ab$. | [Regular expressions and the pumping lemma](06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md) |
| 54 | False; $y$ is all 0s, so $xy^2z$ has more 0s than 1s | The lemma is only a necessary condition for regular languages, so it can show non-regularity but never regularity. The first $p$ symbols of $0^p1^p$ are 0s. | [Regular expressions and the pumping lemma](06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md) |
| 55 | $S \to (S)S \mid \varepsilon$; $S \Rightarrow (S)S \Rightarrow ((S)S)S \Rightarrow (()S)S \Rightarrow (())S \Rightarrow (())$ | Each pair of parentheses wraps a balanced string and is followed by another. Other correct grammars exist. | [Context-free grammars and pushdown automata](06-theory-of-computation/03-context-free-grammars-and-pushdown-automata.md) |
| 56 | 2 symbols; $\{a^n b^n\}$ and $\{ww^R\}$ | After $000$ there are three symbols, and the 1 pops one. The language $\{a^n b^n c^n\}$ needs two comparisons and a single stack cannot do both. | [Context-free grammars and pushdown automata](06-theory-of-computation/03-context-free-grammars-and-pushdown-automata.md) |
| 57 | $0100$ | Flip each bit in turn: $1 \to 0$, $0 \to 1$, $1 \to 0$, $1 \to 0$. | [Turing machines and the Church-Turing thesis](06-theory-of-computation/04-turing-machines-and-church-turing-thesis.md) |
| 58 | Anything computable by an algorithm is computable by a Turing machine; no | "Algorithm" is an informal idea, so it cannot be proved equal to a formal model. A multi-tape machine can be simulated by a single-tape one, so it decides the same languages. | [Turing machines and the Church-Turing thesis](06-theory-of-computation/04-turing-machines-and-church-turing-thesis.md) |
| 59 | (a) and (b) are decidable; (c) is not | For a DFA, run it or search for a reachable accepting state. The halting problem is undecidable. | [Decidability and the halting problem](06-theory-of-computation/05-decidability-and-the-halting-problem.md) |
| 60 | $D(D)$ halts exactly when it does not halt, a contradiction | If $H$ says $D$ halts on $D$, then $D$ loops. If $H$ says it loops, then $D$ halts. So no such $H$ exists. | [Decidability and the halting problem](06-theory-of-computation/05-decidability-and-the-halting-problem.md) |
| 61 | $A$ is decidable; $B$ is undecidable | Decide $A$ by converting the input and running the decider for $B$. The second is the contrapositive. | [Reductions and undecidability](06-theory-of-computation/06-reductions-and-undecidability.md) |
| 62 | Undecidable; it is about the machine's description, not its language | The property "language is empty" is non-trivial and depends only on the language. A property of how many states a machine has depends on the machine itself. | [Reductions and undecidability](06-theory-of-computation/06-reductions-and-undecidability.md) |
| 63 | $\{4, 5\}$ (or $\{3, 4, 2\}$); a verifier checks it in polynomial time | The sum $4 + 5 = 9$ is a quick check that the numbers come from the set and add to the target. | [P, NP and NP-completeness](06-theory-of-computation/07-p-np-and-np-completeness.md) |
| 64 | A problem in NP to which every problem in NP reduces in polynomial time; $P = NP$ | Every NP problem reduces to 3-SAT, so a fast algorithm for 3-SAT would solve all of them fast. | [P, NP and NP-completeness](06-theory-of-computation/07-p-np-and-np-completeness.md) |

</details>

## What to do next

List the lessons behind every question you marked wrong or guessed, and do them in order, since later lessons build on earlier ones. Start each lesson with its quick check: if you get all three right, go straight to its practice problems. Use the chapter cheat sheets to review, such as [number theory](02-number-theory/index.md#cheat-sheet), [counting](03-counting-and-discrete-probability/index.md#cheat-sheet) or [graphs](05-graphs/index.md#cheat-sheet), and take this diagnostic again a few weeks after you finish the lessons, as [how to study](../00-start-here/how-to-study.md#use-the-diagnostics-well) recommends. If you missed nothing, or when you finish, go on to [economics math](../07-economics-math/index.md).
