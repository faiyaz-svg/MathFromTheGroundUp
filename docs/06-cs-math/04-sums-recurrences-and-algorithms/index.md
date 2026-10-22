# Sums, recurrences and algorithms

The math behind algorithm analysis: closed forms for sums, solving recurrences, proving loops correct, asymptotic notation and divide and conquer.

1. [Sums and closed forms](01-sums-and-closed-forms.md)
2. [Recurrences](02-recurrences.md)
3. [Invariants and algorithm correctness](03-invariants-and-algorithm-correctness.md)
4. [Asymptotic notation](04-asymptotic-notation.md)
5. [Divide and conquer and the master theorem](05-divide-and-conquer-and-master-theorem.md)

## Cheat sheet

### Sums and closed forms

| Sum | Closed form |
|---|---|
| $\sum_{k=1}^{n} k$ | $\frac{n(n+1)}{2}$ |
| $\sum_{k=1}^{n} k^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $\sum_{k=1}^{n} k^3$ | $\left(\frac{n(n+1)}{2}\right)^2$ |
| $\sum_{k=0}^{n} r^k$, $r \ne 1$ | $\frac{r^{n+1} - 1}{r - 1}$ |
| $\sum_{k=0}^{n} k\,2^k$ | $(n-1)2^{n+1} + 2$ |
| $\sum_{k=1}^{n} \frac{1}{k(k+1)}$ | $1 - \frac{1}{n+1}$ |
| $\sum_{k=1}^{n} H_k$ | $(n+1)H_n - n$ |

- Perturbation: write $S_n + a_{n+1} = a_0 + \sum_{k=0}^{n} a_{k+1}$, rewrite the right side so $S_n$ appears, and solve.
- Telescoping: write the summand as $g(k+1) - g(k)$ (partial fractions, or falling products), and the sum is $g(n+1) - g(m)$.
- Harmonic numbers: $\ln(n+1) \le H_n \le 1 + \ln n$, so $H_n \sim \ln n$. $H_n$ passes 10 at $n = 12{,}367$.
- Integral bounds for a nondecreasing $f$: $\int_{m-1}^{n} f \le \sum_{k=m}^{n} f(k) \le \int_m^{n+1} f$. For a nonincreasing $f$ the integrals swap sides.
- $\ln n!$ lies between $n \ln n - n + 1$ and $(n+1)\ln(n+1) - n$.
- Swap a triangular double sum by changing the bounds: $\sum_{i=1}^{n}\sum_{j=1}^{i} = \sum_{j=1}^{n}\sum_{i=j}^{n}$.
- A nested loop is a sum: `range(i, n)` runs $n - i$ times. Halving loops are geometric and cost about $2n$ in total.

Main mistakes:

- Using the same endpoints for both integral bounds, or the wrong ones for a decreasing $f$.
- Swapping a triangular double sum without changing the bounds.
- Treating $H_n$ as exactly $\ln n$ (it is about $\ln n + 0.58$).
- Checking a closed form at one value. Check $n = 0$, 1, 2 and one more.

### Recurrences

| Type | Method |
|---|---|
| $T(n) = T(n-1) + f(n)$ | unroll: $T(n) = T(0) + \sum f(k)$ |
| $T(n) = 2T(n-1) + 1$ (Hanoi) | $T(n) = 2^n T(0) + 2^n - 1$ |
| $a_n = c_1 a_{n-1} + c_2 a_{n-2}$ | characteristic equation $r^2 = c_1 r + c_2$ |
| distinct roots $r_1, r_2$ | $a_n = A\,r_1^n + B\,r_2^n$ |
| double root $r$ | $a_n = (A + Bn)\,r^n$ |
| nonhomogeneous $+\,g(n)$ | $a_n = p_n + h_n$, with a guessed particular solution $p_n$ |

- Fit the constants to the initial values last, after adding the particular solution.
- Guesses for $p_n$: a constant for constant $g$, a polynomial of the same degree for a polynomial $g$, $C s^n$ for $g = s^n$. Multiply by $n$ if the guess already solves the homogeneous part.
- Fibonacci: $F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}$ with $\varphi = \frac{1+\sqrt{5}}{2}$ and $\psi = \frac{1-\sqrt{5}}{2}$, and $F_n$ is the integer nearest $\varphi^n/\sqrt{5}$. In floating point this fails from $n = 71$.
- Calls of the plain recursive Fibonacci: $C(n) = 2F_{n+1} - 1$, which is 21,891 for $n = 20$.
- Loan balance: $B_n = (1+r)^n B_0 - \text{PMT}\cdot\frac{(1+r)^n - 1}{r}$.
- Cassini: $F_{n+1}F_{n-1} - F_n^2 = (-1)^n$.

Main mistakes:

- Writing $r^2 + c_1 r + c_2$ for the characteristic equation (the correct one is $r^2 - c_1 r - c_2$).
- Using $A\,r^n$ alone for a double root.
- Fitting initial values to the homogeneous part only.
- Applying the characteristic equation to $T(n) = 2T(n/2) + n$, which isn't of that form.

### Invariants and algorithm correctness

- Specification: precondition (what the caller gives) and postcondition (what the algorithm promises). Correct means partially correct and terminating.
- Loop invariant: true before the first test (initialization), kept true by a pass that starts with it true and the guard true (maintenance), and, with "not guard", it implies the postcondition when the loop stops.
- Termination: a variant, a natural number that strictly decreases each pass ($n - i$, $\text{hi} - \text{lo}$, $b$ in Euclid).
- Finding an invariant: replace the end value in the postcondition by the progress variable ("the part seen so far").
- State machine: an invariant true at the start and preserved by every transition holds in every reachable state. It proves a state is unreachable, never that it is reachable.

| Algorithm | Invariant |
|---|---|
| maximum of a list | `m` is the largest of `a[0:i]` |
| insertion sort | `a[0:i]` holds the original first $i$ items, sorted |
| binary search (half-open) | everything before `lo` is $< x$, everything from `hi` on is $\ge x$ |
| Euclid | $\gcd(a, b)$ never changes |
| fast power | $\text{result} \cdot \text{base}^e = x^n$ |

- 15-puzzle: $I + R$ is even, where $I$ is the number of inversions and $R$ the blank's row from the top. For the 8-puzzle, $I$ alone is even.
- Jugs of size $s$ and $t$ only hold multiples of $\gcd(s, t)$.

Main mistakes:

- Claiming the invariant in the middle of the body.
- An invariant too weak to give the postcondition, or too specific to be preserved.
- Proving only partial correctness (no variant).
- Binary search bugs: `hi = len(a) - 1` with `while lo < hi`, `lo = mid` with no `+ 1`, and `(lo + hi) // 2` overflowing in fixed-width integers.

### Asymptotic notation

| Notation | Meaning | Definition |
|---|---|---|
| $f = O(g)$ | at most | some $c > 0$ and $n_0$ give $f(n) \le c\,g(n)$ for every $n \ge n_0$ |
| $f = \Omega(g)$ | at least | some $c > 0$ and $n_0$ give $f(n) \ge c\,g(n)$ for every $n \ge n_0$ |
| $f = \Theta(g)$ | same rate | both of the above |
| $f = o(g)$ | strictly slower | for every $c > 0$, $f(n) < c\,g(n)$ eventually |

- Limit test with $L = \lim f/g$: $L = 0$ gives $o$, $0 < L < \infty$ gives $\Theta$, $L = \infty$ gives $\omega$.
- A polynomial of degree $d$ with positive leading coefficient is $\Theta(n^d)$.
- Order: $1 \ll \lg n \ll n^p \ll n \lg n \ll n^2 \ll n^k \ll b^n \ll n! \ll n^n$, with $p < 1$ and $b > 1$. $\lg n! = \Theta(n \lg n)$.
- The base of a logarithm doesn't matter, the base of an exponential does: $2^n \ll 3^n$.
- Analysing code: sequence adds, nested loops multiply (or sum, if the bounds depend on the loop variable), recursion gives a recurrence.
- Doubling test: $T(2n)/T(n)$ near 2 means linear, 4 means quadratic, 8 means cubic.

Main mistakes:

- Reading $O$ as a tight bound or as a lower bound ("at least $O(n^2)$").
- Reading "$=$" as symmetric: $O(n) = O(n^2)$ is true left to right only.
- Hiding a growing number of terms in a constant: $\sum_{i \le n} i$ is not $O(n)$.
- Dropping the base of an exponential, or comparing at small $n$.
- Claiming $\Theta$ for an algorithm without saying the case (best, worst, average).

### Divide and conquer and the master theorem

$T(n) = a\,T(n/b) + f(n)$, with $p = \log_b a$ the critical exponent, $n^p$ the number of leaves.

| Case | Condition | Result |
|---|---|---|
| 1 | $f(n) = O(n^{p - \varepsilon})$ | $\Theta(n^p)$ |
| 2 | $f(n) = \Theta(n^p)$ | $\Theta(n^p \lg n)$ |
| 3 | $f(n) = \Omega(n^{p + \varepsilon})$ and $a f(n/b) \le c f(n)$, $c < 1$ | $\Theta(f(n))$ |

| Algorithm | Recurrence | Result |
|---|---|---|
| binary search | $T(n/2) + 1$ | $\Theta(\lg n)$ |
| merge sort | $2T(n/2) + n$ | $\Theta(n \lg n)$ |
| Karatsuba | $3T(n/2) + n$ | $\Theta(n^{\lg 3})$, $\lg 3 \approx 1.585$ |
| block matrix multiply | $8T(n/2) + n^2$ | $\Theta(n^3)$ |
| Strassen | $7T(n/2) + n^2$ | $\Theta(n^{\lg 7})$, $\lg 7 \approx 2.807$ |

- Recursion tree: level $i$ costs $a^i f(n/b^i)$ and there are $\log_b n + 1$ levels. A geometric series with ratio above 1, equal to 1 or below 1 gives cases 1, 2 and 3.
- Gaps: $2T(n/2) + n/\lg n$ is $\Theta(n \lg\lg n)$ (a harmonic sum of level costs), and $2T(n/2) + n\lg n$ is $\Theta(n \lg^2 n)$.
- Unequal pieces such as $T(n/3) + T(2n/3) + n$ are $\Theta(n \lg n)$ by the tree.
- Substitution: assume $T(m) \le c\,g(m)$ for smaller $m$, push it through the recurrence, and check the base cases by hand. For $n \lg n$ the base cases are $n = 2, 3$, since $1 \cdot \lg 1 = 0$.
- If the bound doesn't close, subtract a lower-order term: prove $T(n) \le 2n - 1$, not $T(n) \le cn$.

Main mistakes:

- $\log_a b$ for $\log_b a$.
- Treating $n \lg n$ as polynomially larger than $n$.
- Skipping the regularity check in case 3.
- A substitution proof that ends with $(c + 1)n$ and calls it $O(n)$.
