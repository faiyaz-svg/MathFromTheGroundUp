# Sequences, series and counting

Lists of numbers defined by a rule, their sums, and the counting methods that explain the binomial theorem.

1. [Sequences and recursion](01-sequences-and-recursion.md)
2. [Summation notation and series](02-summation-notation-and-series.md)
3. [Counting: permutations and combinations](03-counting-permutations-combinations.md)
4. [The binomial theorem](04-binomial-theorem.md)

## Cheat sheet

### Sequences and recursion

A sequence is a function on $\mathbb{N}$, written $a_n$ for the term with index $n$. This book starts at index 0. An explicit formula gives $a_n$ from $n$. A recurrence gives the initial conditions plus a rule for the next term, and it needs as many initial conditions as the number of terms it looks back.

| Type | Defining rule | Explicit formula | Example |
|---|---|---|---|
| arithmetic | $a_{n+1} = a_n + d$ | $a_n = a_0 + nd$ | $2, 7, 12, \dots$ has $a_n = 2 + 5n$ |
| geometric | $a_{n+1} = r\,a_n$ | $a_n = a_0 r^n$ | $100 \cdot 1.02^n$ for a 2% yearly balance |
| Fibonacci | $F_{n+2} = F_{n+1} + F_n$ | $F_0 = 0$, $F_1 = 1$ | $0, 1, 1, 2, 3, 5, 8, \dots$ |

- From two terms $a_m$ and $a_n$: $d = \frac{a_n - a_m}{n - m}$, and $r^{n-m} = \frac{a_n}{a_m}$ (two answers $\pm r$ when $n - m$ is even).
- Terms from $a_m$ to $a_n$ number $n - m + 1$.
- To find a formula for a recurrence: compute six terms, spot the pattern, test it, then prove it by induction (check the start, and show that the formula for $n$ gives the formula for $n + 1$). Example: $h_0 = 0$, $h_{n+1} = 2h_n + 1$ gives $h_n = 2^n - 1$.
- A loan balance is $B_{n+1} = (1 + r)B_n - \text{PMT}$, with $r$ the rate per period.
- In code, a recurrence is a loop (`b = (1 + r) * b - pmt`) or a recursive function. Plain recursion for Fibonacci repeats work and makes 21,891 calls for $F_{20}$.

Main mistakes:

- Treating a pattern as a proof: $1, 2, 4, 8, 16, 31$ counts regions of a circle.
- Off-by-one errors from starting at index 0 or 1.
- Mixing up $2n$ and $2^n$. Check both the differences and the ratios.
- Writing a recurrence without its initial conditions.

### Summation notation and series

$\sum_{k=m}^{n} a_k = a_m + \cdots + a_n$ has $n - m + 1$ terms, and an empty sum is 0. The index is a placeholder.

| Sum | Value |
|---|---|
| $\sum_{k=m}^{n} c$ | $(n - m + 1)\,c$ |
| $\sum_{k=1}^{n} k$ | $\frac{n(n+1)}{2}$ |
| $\sum_{k=1}^{n} k^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $\sum_{k=1}^{n} k^3$ | $\left(\frac{n(n+1)}{2}\right)^2$ |
| arithmetic, $n$ terms | $n \cdot \frac{\text{first} + \text{last}}{2}$ |
| geometric, $n$ terms, $r \ne 1$ | $a\,\frac{1 - r^n}{1 - r}$ |
| infinite geometric, $\lvert r \rvert < 1$ | $\frac{a}{1 - r}$ |

- Rules: linearity ($\sum (a_k + b_k)$ splits, constants come out), splitting at any point, and shifting the index (change the bounds with it). A telescoping sum $\sum (b_{k+1} - b_k)$ equals $b_{n+1} - b_m$.
- Proofs: pair the sum with its reverse (arithmetic), subtract $rS$ from $S$ (geometric), telescope $(k+1)^3 - k^3$ (squares).
- A repeating block of $b$ digits is the block over $10^b - 1$: $0.\overline{36} = \frac{36}{99} = \frac{4}{11}$. Also $0.\overline{9} = 1$.
- The sum $1 + 2 + \cdots + n$ is the step count of a nested loop, about $\frac{n^2}{2}$, so $O(n^2)$. A dynamic array that doubles copies fewer than $n$ items in total.
- Regular deposits $D$ at rate $r$ per period for $n$ periods are worth $D\,\frac{(1+r)^n - 1}{r}$. A loan balance is $B_n = (1+r)^n B_0 - \text{PMT}\,\frac{(1+r)^n - 1}{r}$.

Main mistakes:

- Using $n - m$ for the number of terms, or the last exponent $n - 1$ in the geometric formula (the exponent is the number of terms).
- Using $\frac{n(n+1)}{2}$ when the sum doesn't start at 1.
- Using $\frac{a}{1 - r}$ when $\lvert r \rvert \ge 1$.
- Writing $\sum a_k b_k = \left(\sum a_k\right)\left(\sum b_k\right)$.

### Counting: permutations and combinations

| Rule | Statement |
|---|---|
| sum rule | cases with no overlap: add the counts |
| product rule | stages, with a fixed number of options at each: multiply |
| lists of length $k$ from $n$ symbols | $n^k$ |
| subsets of an $n$-set | $2^n$ |

| Order matters? | Repeats? | Count |
|---|---|---|
| yes | yes | $n^k$ |
| yes | no | $P(n, k) = \frac{n!}{(n-k)!}$ |
| no | no | $\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$ |
| no | yes | $\binom{n+k-1}{k}$ (stated, not proved) |

- $0! = 1$. Also $\binom{n}{0} = \binom{n}{n} = 1$, $\binom{n}{k} = \binom{n}{n-k}$, and $\binom{n}{k} = 0$ for $k > n$.
- Dividing by $k!$ removes order, because each subset appears in $k!$ ordered lists.
- Repeated letters: $\frac{n!}{n_1!\,n_2!\cdots n_m!}$. BANANA gives $\frac{6!}{3!\,2!} = 60$.
- Restrictions: subtract the complement ("at least one" is the total minus "none"), fill the restricted position first, and glue items that must stay together.
- A random secret with $N$ equally likely values has $\log_2 N$ bits: a 4-digit PIN is 13.3 bits, and 8 characters from 62 is 47.6 bits.
- With equally likely outcomes, $P(A) = \frac{\lvert A \rvert}{\lvert S \rvert}$. Lotto 6/49 has $\binom{49}{6} = 13{,}983{,}816$ tickets.

Main mistakes:

- Using $P$ when order doesn't matter (overcounts by $k!$).
- Counting a case twice, as when picking "Ana or Ben first".
- Adding when the stages should multiply, or the reverse.
- Counting the sample space with order and the event without it.

### The binomial theorem

$$
(a+b)^n = \sum_{k=0}^{n} \binom{n}{k}\, a^{n-k} b^k.
$$

It has $n + 1$ terms, the exponents of $a$ and $b$ add to $n$, and the coefficient is the number of ways to choose which $k$ brackets give a $b$.

- Pascal's rule: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$, because a $k$-subset either contains a chosen element or doesn't. Row $n$ of the triangle is built from row $n - 1$, and row 0 is 1.
- Row sums: $\sum_k \binom{n}{k} = 2^n$ (subsets sorted by size), and $\sum_k (-1)^k\binom{n}{k} = 0$ for $n \ge 1$.
- To expand: put $a$ and $b$ in brackets with their signs, write the coefficients, and simplify. For one term, write the general term, solve for $k$ from the exponent, and evaluate. If $k$ isn't a whole number from 0 to $n$, the coefficient is 0.
- Coin flips: $P(k \text{ heads in } n \text{ fair flips}) = \binom{n}{k} / 2^n$. Row 10 gives $1, 10, 45, 120, 210, 252, \dots$ over 1024.
- Approximation: $(1 + x)^n \approx 1 + nx$ when $nx$ is small, and $(1+x)^n \ge 1 + nx$ for $x \ge 0$. With the next term, $1 + nx + \binom{n}{2}x^2$. Then $r^n \to 0$ for $\lvert r \rvert < 1$.
- Check an expansion by putting in a simple value such as $x = 1$.

Main mistakes:

- $(a+b)^n = a^n + b^n$. The mixed terms are missing.
- Not raising the coefficient: $(2x)^4 = 16x^4$.
- Dropping the alternating signs of $(a - b)^n$.
- Starting the row at $k = 1$ instead of $k = 0$.
- Using $1 + nx$ when $nx$ is not small: $1.05^{10}$ is $1.629$, not $1.5$.
