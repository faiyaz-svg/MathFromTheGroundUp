# GCD and Euclid's algorithm

After this lesson you can find a greatest common divisor with Euclid's algorithm and a trace table, prove that the algorithm is correct and fast, write the GCD as a combination $ax + by$ with the extended algorithm, and compute the least common multiple from it.

Before this: [divisibility and modular arithmetic](01-divisibility-and-modular-arithmetic.md) (the division algorithm and congruences), [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md) (the GCF found by factoring), [direct proof](../../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md) and [strong induction and well-ordering](../../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find $\gcd(252, 198)$ using only divisions with remainder.
2. What are $\gcd(0, 7)$ and $\gcd(-12, 18)$?
3. Find $\operatorname{lcm}(18, 48)$.

<details class="solution" markdown>
<summary>Answers</summary>

1. We have $252 = 1 \cdot 198 + 54$, then $198 = 3 \cdot 54 + 36$, then $54 = 1 \cdot 36 + 18$, then $36 = 2 \cdot 18 + 0$. The last nonzero remainder is $\gcd(252, 198) = 18$.
2. Every integer divides 0, so the common divisors of 0 and 7 are the divisors of 7, and $\gcd(0, 7) = 7$. The divisors of $-12$ and 12 are the same, so $\gcd(-12, 18) = \gcd(12, 18) = 6$.
3. Since $\gcd(18, 48) = 6$, the least common multiple is $\frac{18}{6} \cdot 48 = 3 \cdot 48 = 144$. Check: $144 = 8 \cdot 18 = 3 \cdot 48$.

</details>

## The idea

The [factors lesson](../../01-elementary/08-factors-multiples-and-primes.md) finds the greatest common factor of two numbers by writing both as products of primes. That works for 84 and 360. It does not work for two numbers with 300 digits each, because no one knows how to factor numbers that size quickly. Yet a computer finds the GCD of two such numbers in a few milliseconds. The method it uses is over 2,000 years old and needs no factoring.

Picture a $1071 \times 462$ rectangle, and cut off the biggest squares you can. Two squares of side 462 fit, leaving a $147 \times 462$ strip. In that strip three squares of side 147 fit, leaving a $147 \times 21$ strip. In that strip seven squares of side 21 fit exactly, with nothing left. The side of the last square, 21, is the GCD. Every cut is a division with remainder, and the remainder is the leftover strip.

The reason this works is a simple fact about the leftover. Any number that divides both sides of a rectangle also divides the strip that remains after cutting off whole squares. So the common divisors of the big rectangle are the common divisors of the smaller one, and the GCD never changes while the numbers shrink. The proof, a speed analysis, and a useful by-product (the GCD can always be written as $ax + by$) are the content of the lesson.

## Definitions

### Greatest common divisor

Let $a$ and $b$ be integers that are not both 0. A **common divisor** of $a$ and $b$ is an integer that divides both. The **greatest common divisor**, written $\gcd(a, b)$, is the largest common divisor.

In plain words, it is the biggest number that goes into both. It exists because 1 is a common divisor, and by [divisibility Theorem 1(c)](01-divisibility-and-modular-arithmetic.md) a common divisor of a nonzero number can't exceed that number in absolute value. The factors lesson called it the greatest common factor; "GCD" is the name in number theory and in code (`math.gcd`).

A few cases follow at once. Divisors ignore signs, so $\gcd(a, b) = \gcd(\lvert a \rvert, \lvert b \rvert)$. Since every integer divides 0, we have $\gcd(a, 0) = \lvert a \rvert$ for $a \ne 0$. The value $\gcd(0, 0)$ is undefined, because every integer divides 0 and there is no largest. Python's `math.gcd(0, 0)` returns 0 by convention.

Integers $a$ and $b$ are **coprime**, or relatively prime, if $\gcd(a, b) = 1$. For example 8 and 15 are coprime although neither is prime.

### Least common multiple

For nonzero integers $a$ and $b$, the **least common multiple**, written $\operatorname{lcm}(a, b)$, is the smallest positive integer that both $a$ and $b$ divide. For 18 and 48 it is 144.

### Linear combination

A **linear combination** of $a$ and $b$ is a number $ax + by$ with $x$ and $y$ integers. The numbers $x$ and $y$ are the coefficients. For example $1071 \cdot (-3) + 462 \cdot 7 = 21$.

## How to do it

### Euclid's algorithm

To find $\gcd(a, b)$ for integers $a \ge b > 0$:

1. If $b = 0$, stop: the answer is $a$. (With $b > 0$, go on.)
2. Divide: write $a = qb + r$ with $0 \le r < b$.
3. Replace the pair $(a, b)$ by $(b, r)$.
4. Repeat from step 1. When a remainder is 0, the answer is the divisor you just used, which is the last nonzero remainder.
5. Check: the answer divides both original numbers.

If $a < b$, step 2 gives $q = 0$ and $r = a$, so the pair is just swapped, and nothing special is needed. A trace table lists one row per division.

| Step | $a$ | $b$ | $q$ | $r$ |
|---|---|---|---|---|
| 1 | 1071 | 462 | 2 | 147 |
| 2 | 462 | 147 | 3 | 21 |
| 3 | 147 | 21 | 7 | 0 |

The last nonzero remainder is 21, so $\gcd(1071, 462) = 21$. In code it is two lines: `while b: a, b = b, a % b`.

### Why it works

*Theorem 1.* Let $a$ and $b$ be integers with $b > 0$, and let $a = qb + r$ with $0 \le r < b$. Then $\gcd(a, b) = \gcd(b, r)$.

What we know: the division algorithm gives $r = a - qb$. What we want: the two pairs have the same greatest common divisor. The plan: show that the two pairs have exactly the same common divisors, so the largest is the same.

*Proof.* Suppose $d \mid a$ and $d \mid b$. Then $d$ divides $a - qb = r$ by [Theorem 1(b)](01-divisibility-and-modular-arithmetic.md), so $d$ is a common divisor of $b$ and $r$. Conversely, suppose $d \mid b$ and $d \mid r$. Then $d$ divides $qb + r = a$, so $d$ is a common divisor of $a$ and $b$. The two pairs therefore have the same set of common divisors, and so the same largest one. (If $r = 0$, the second pair is $(b, 0)$, and the set is the divisors of $b$.) $\blacksquare$

Look back: nothing was assumed about the size of $q$, so the same proof shows $\gcd(a, b) = \gcd(a - b, b)$ and $\gcd(a, b) = \gcd(a - 7b, b)$. Euclid's algorithm applies the biggest possible subtraction at once.

*Theorem 2.* For $a \ge b > 0$, Euclid's algorithm stops after finitely many divisions, and its answer is $\gcd(a, b)$.

*Proof.* The successive remainders form a strictly decreasing sequence of nonnegative integers, $b > r_1 > r_2 > \dots \ge 0$, so by well-ordering the sequence reaches 0 after at most $b$ divisions. At every step Theorem 1 says the gcd of the current pair equals the gcd of the previous pair. This is the invariant: "$\gcd(a, b)$ of the current pair equals the gcd of the original pair". It holds at the start and after each step. When the pair is $(g, 0)$, the invariant says the original gcd is $\gcd(g, 0) = g$. $\blacksquare$

The same argument, phrased as a loop invariant, is the model for the proofs in [invariants and algorithm correctness](../04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md).

### How fast it is

The bound $b$ on the number of divisions is far too weak. In the table above, 462 would allow 462 divisions, and the algorithm used 3.

*Theorem 3.* Let $r_0 = a$ and $r_1 = b$ be positive integers with $a \ge b$, and let $r_2, r_3, \dots$ be the successive remainders. If $r_{i+1} > 0$, then $r_{i+2} < \frac{1}{2} r_i$.

What we know: $r_i = q\, r_{i+1} + r_{i+2}$ with $q \ge 1$ and $0 \le r_{i+2} < r_{i+1}$. What we want: the remainder two steps later is less than half of $r_i$. The plan: split into two cases by the size of $r_{i+1}$.

*Proof.* If $r_{i+1} \le \frac{1}{2} r_i$, then $r_{i+2} < r_{i+1} \le \frac{1}{2} r_i$. If $r_{i+1} > \frac{1}{2} r_i$, then $q = 1$ (two copies of $r_{i+1}$ would exceed $r_i$), so $r_{i+2} = r_i - r_{i+1} < r_i - \frac{1}{2} r_i = \frac{1}{2} r_i$. $\blacksquare$

*Corollary 4.* Euclid's algorithm on $a \ge b > 0$ makes at most $2 \log_2 b + 2$ divisions.

*Proof.* Suppose the algorithm makes $k$ divisions, so the remainders $r_1, \dots, r_k$ are all at least 1 and $r_{k+1} = 0$. Applying Theorem 3 over and over gives $r_{1+2j} < b / 2^j$ whenever $j \ge 1$ and $1 + 2j \le k$. Let $m = 1 + 2j$ be the largest odd index with $m \le k$, so $k \le m + 1$. Since $r_m \ge 1$, either $j = 0$ or $1 \le r_m < b/2^j$; in both cases $2^j \le b$, so $j \le \log_2 b$. Therefore $k \le m + 1 = 2j + 2 \le 2 \log_2 b + 2$. $\blacksquare$

The count is in terms of $\log_2 b$, which is about the number of bits of $b$. So the work grows in proportion to the number of digits, not to the size of the number. In big O terms ([asymptotic notation](../04-sums-recurrences-and-algorithms/04-asymptotic-notation.md)), it is $O(\log b)$ divisions. Trial division for the same job takes about $\sqrt{b}$ steps, and for a 100-digit $b$ that is $10^{50}$.

A sharper statement says what the worst case looks like. Recall the Fibonacci numbers $F_1 = F_2 = 1$ and $F_{n+2} = F_{n+1} + F_n$ ([sequences and recursion](../../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md)).

*Theorem 5 (Lamé).* If Euclid's algorithm on $a > b \ge 1$ makes exactly $k$ divisions, then $b \ge F_{k+1}$ and $a \ge F_{k+2}$.

What we know: the definition of the Fibonacci numbers. What we want: a lower bound on the inputs in terms of the number of divisions. The plan: induction on $k$, using that after one division the algorithm is running on $(b, r)$ with one fewer division.

*Proof.* For $k = 1$: $b \ge 1 = F_2$, and $a > b$ gives $a \ge 2 = F_3$. Now suppose the claim holds for $k$, and the algorithm on $a > b$ makes $k + 1$ divisions. After the first division $a = qb + r$ it runs on $(b, r)$ with $b > r \ge 1$, making $k$ divisions, so $r \ge F_{k+1}$ and $b \ge F_{k+2}$. Since $q \ge 1$, we get $a = qb + r \ge b + r \ge F_{k+2} + F_{k+1} = F_{k+3}$. This is the claim for $k + 1$. $\blacksquare$

Look back: the inputs $(F_{k+2}, F_{k+1})$ meet the bound exactly, since each division has $q = 1$ (the pair (13, 8) is the example at the end of the lesson). Consecutive Fibonacci numbers are the worst case. Since $F_n \ge \left(\tfrac{3}{2}\right)^{n-2}$ for $n \ge 2$ (Practice 7 of the strong induction lesson), a $b$ below $10^{100}$ needs at most 568 divisions. The true worst case for 100 digits, using Fibonacci numbers, is about 480.

### Bezout's identity

*Theorem 6 (Bezout's identity).* Let $a$ and $b$ be integers, not both 0, and let $g = \gcd(a, b)$. Then there are integers $x$ and $y$ with

$$
ax + by = g.
$$

What we know: well-ordering and the division algorithm. What we want: the GCD is a linear combination. The plan: take the smallest positive linear combination, and show that it divides both $a$ and $b$ and is divisible by $g$.

*Proof.* Let $S = \{ax + by : x, y \in \mathbb{Z},\ ax + by > 0\}$. It is nonempty, since $a \cdot a + b \cdot b > 0$. By well-ordering it has a least element $s = ax_0 + by_0$. Divide: $a = qs + r$ with $0 \le r < s$. Then $r = a - q(ax_0 + by_0) = a(1 - qx_0) + b(-qy_0)$ is a linear combination too. Since $r < s$ and $s$ is the least positive one, $r$ is not positive, so $r = 0$ and $s \mid a$. The same argument shows $s \mid b$.

So $s$ is a common divisor, and $s \le g$. On the other hand $g \mid a$ and $g \mid b$, so $g$ divides $ax_0 + by_0 = s$, and $g \le s$ because $s > 0$. Hence $s = g$. $\blacksquare$

Look back: the proof is a smallest-counterexample argument in disguise, and it says nothing about how to find $x$ and $y$. The extended algorithm below does that. Three consequences are used in the rest of the chapter.

*Corollary 7.* (a) Every common divisor of $a$ and $b$ divides $\gcd(a, b)$. (b) $\gcd(a, b) = 1$ if and only if $ax + by = 1$ for some integers $x$ and $y$.

*Proof.* (a) A common divisor $d$ divides $ax + by = g$ by Theorem 1(b) of the previous lesson. (b) If $\gcd(a, b) = 1$, Theorem 6 gives $x$ and $y$. Conversely, if $ax + by = 1$, then each common divisor of $a$ and $b$ divides 1, so the only ones are $\pm 1$. $\blacksquare$

*Lemma 8 (coprime lemma).* If $\gcd(a, b) = 1$ and $a \mid bc$, then $a \mid c$.

*Proof.* Write $1 = ax + by$. Multiply by $c$: $c = acx + bcy$. Now $a$ divides $acx$, and $a$ divides $bcy$ because $a \mid bc$. So $a$ divides their sum $c$. $\blacksquare$

In plain words, a number that shares no factor with $b$ can only divide a product $bc$ by dividing $c$. The next lesson uses this for primes.

### The extended Euclidean algorithm

To find $x$ and $y$ with $ax + by = \gcd(a, b)$, run Euclid's algorithm and then substitute backwards.

1. Run Euclid's algorithm, keeping every division line.
2. Solve the line whose remainder is the GCD (the next-to-last line) for the GCD.
3. Replace the newest remainder in that equation using the line above it, so that the GCD is written with the two numbers from that line.
4. Repeat step 3 up the list until only $a$ and $b$ remain. Collect terms in each of them every time, and don't multiply out a bracket until you must.
5. Check: compute $ax + by$.

For 1071 and 462, the lines are $1071 = 2 \cdot 462 + 147$ and $462 = 3 \cdot 147 + 21$. Solve the second for 21, replace 147 by $1071 - 2 \cdot 462$, and collect:

$$
\begin{aligned}
21 &= 462 - 3 \cdot 147 \\
&= 462 - 3\,(1071 - 2 \cdot 462) \\
&= 7 \cdot 462 - 3 \cdot 1071.
\end{aligned}
$$

So $x = -3$ and $y = 7$. Check: $-3213 + 3234 = 21$.

The forward form of the same computation is easier to program, and to check. Keep two extra columns, $s_i$ and $t_i$, with the claim that every remainder satisfies $r_i = s_i a + t_i b$. Start with $r_0 = a$ ($s_0 = 1$, $t_0 = 0$) and $r_1 = b$ ($s_1 = 0$, $t_1 = 1$). Row $i$ divides $r_{i-2}$ by $r_{i-1}$ to get the quotient $q_i$, and then $r_i = r_{i-2} - q_i r_{i-1}$. Apply the same update to $s$ and $t$: $s_i = s_{i-2} - q_i s_{i-1}$ and $t_i = t_{i-2} - q_i t_{i-1}$.

| $i$ | $r_i$ | $q_i$ | $s_i$ | $t_i$ |
|---|---|---|---|---|
| 0 | 1071 | | 1 | 0 |
| 1 | 462 | | 0 | 1 |
| 2 | 147 | 2 | 1 | $-2$ |
| 3 | 21 | 3 | $-3$ | 7 |

Every row satisfies $r_i = s_i a + t_i b$. Rows 0 and 1 do, and a row is built from two earlier rows by the same subtraction on all three columns, so by induction on $i$ the claim holds for every row. The row of the last nonzero remainder gives $21 = (-3)(1071) + (7)(462)$. One more row (with $q = 7$) gives $r = 0$ and $(s, t) = (22, -51)$, which tells how to shift the answer, as the edge cases below explain.

### The least common multiple

*Theorem 9.* For positive integers $a$ and $b$, $\operatorname{lcm}(a, b) = \dfrac{ab}{\gcd(a, b)}$. Also, every common multiple of $a$ and $b$ is a multiple of $\operatorname{lcm}(a, b)$.

What we know: Lemma 8. What we want: a formula, and a description of all common multiples. The plan: divide out the GCD so the two numbers become coprime, then use the coprime lemma on a common multiple.

*Proof.* Let $g = \gcd(a, b)$ and write $a = ga'$ and $b = gb'$. Then $\gcd(a', b') = 1$: a common divisor $d$ of $a'$ and $b'$ gives a common divisor $dg$ of $a$ and $b$, so $dg \le g$ and $d \le 1$.

Put $L = ab/g = ga'b'$. It is a common multiple, since $L = a \cdot b' = b \cdot a'$. Now let $m$ be any common multiple. Write $m = ak = ga'k$. Since $b \mid m$, we have $gb' \mid ga'k$, so $b' \mid a'k$. By Lemma 8, $b' \mid k$, say $k = b'j$. Then $m = ga'b'j = Lj$. So every common multiple is a multiple of $L$, and the smallest positive one is $L$ itself. $\blacksquare$

Look back: the elementary lesson stated $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = ab$ and proved it by prime exponents; this proof avoids factoring entirely. To compute an lcm, divide first and multiply second: $\frac{a}{g} \cdot b$ keeps the intermediate number small. Check: $\operatorname{lcm}(18, 48) = \frac{18}{6} \cdot 48 = 144$.

## Worked examples

<div class="example" markdown>

### Example 1: a trace table for $\gcd(1071, 462)$

Step 1: $b = 462$ is not 0, so we go on. Step 2: divide 1071 by 462. Two copies of 462 make 924, and $1071 - 924 = 147$, so $1071 = 2 \cdot 462 + 147$ with $q = 2$ and $r = 147$. Step 3: the new pair is $(462, 147)$.

Step 4, repeating: $462 = 3 \cdot 147 + 21$ gives the pair $(147, 21)$, and $147 = 7 \cdot 21 + 0$ gives remainder 0. The trace table at the top of the section holds all three rows. The last nonzero remainder is 21.

Step 5, the check: $1071 = 51 \cdot 21$ and $462 = 22 \cdot 21$, so 21 divides both. It is the greatest, since $51 = 3 \cdot 17$ and $22 = 2 \cdot 11$ share no factor. As a second check, the factors lesson's method gives $1071 = 3^2 \cdot 7 \cdot 17$ and $462 = 2 \cdot 3 \cdot 7 \cdot 11$, and the shared part is $3 \cdot 7 = 21$.

</div>

<div class="example" markdown>

### Example 2: back-substitution for 240 and 46

The divisions are

$$
\begin{aligned}
240 &= 5 \cdot 46 + 10 \\
46 &= 4 \cdot 10 + 6 \\
10 &= 1 \cdot 6 + 4 \\
6 &= 1 \cdot 4 + 2 \\
4 &= 2 \cdot 2 + 0
\end{aligned}
$$

so $\gcd(240, 46) = 2$. Now substitute upward from the line with remainder 2. Each step replaces the newest remainder using the line above it:

$$
\begin{aligned}
2 &= 6 - 1 \cdot 4 \\
&= 6 - (10 - 6) = 2 \cdot 6 - 10 \\
&= 2\,(46 - 4 \cdot 10) - 10 = 2 \cdot 46 - 9 \cdot 10 \\
&= 2 \cdot 46 - 9\,(240 - 5 \cdot 46) = 47 \cdot 46 - 9 \cdot 240.
\end{aligned}
$$

So $x = -9$ and $y = 47$ in $240x + 46y = 2$.

Check: $47 \cdot 46 = 2162$ and $9 \cdot 240 = 2160$, and $2162 - 2160 = 2$.

<div class="warning" markdown>

Watch out at step 4 of the extended algorithm: in the second line above, $6 - (10 - 6)$ has the number 6 twice. Collect them to get $2 \cdot 6 - 10$ before substituting for 6 again. Substituting for both 6s separately is not wrong but doubles the work.

</div>

</div>

<div class="example" markdown>

### Example 3: edge cases

The pair $(84, 360)$ has $a < b$. The first division is $84 = 0 \cdot 360 + 84$, which swaps the pair to $(360, 84)$. Then $360 = 4 \cdot 84 + 24$, $84 = 3 \cdot 24 + 12$ and $24 = 2 \cdot 12 + 0$, so $\gcd(84, 360) = 12$.

When one number divides the other, one division finishes it: $1001 = 11 \cdot 91 + 0$, so $\gcd(1001, 91) = 91$. And for a pair like $(17, 0)$, step 1 stops at once with answer 17.

Consecutive integers are coprime. For $(n + 1, n)$, the division is $n + 1 = 1 \cdot n + 1$, so the pair becomes $(n, 1)$, and $n = n \cdot 1 + 0$ gives GCD 1. For example $\gcd(101, 100) = 1$.

Check: Python's `math.gcd` gives 12, 91, 17 and 1 for the four pairs.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Find $x$ and $y$ with $119x + 35y = \gcd(119, 35)$. The divisions are

$$
\begin{aligned}
119 &= 3 \cdot 35 + 14 \\
35 &= 2 \cdot 14 + 7 \\
14 &= 2 \cdot 7 + 0
\end{aligned}
$$

so the GCD is 7, and the first substitution gives $7 = 35 - 2 \cdot 14$. Finish: replace 14 using the first line, collect terms and check.

<details class="solution" markdown>
<summary>Finish</summary>

Replace $14 = 119 - 3 \cdot 35$:

$$
7 = 35 - 2\,(119 - 3 \cdot 35) = 7 \cdot 35 - 2 \cdot 119.
$$

So $x = -2$ and $y = 7$.

Check: $119 \cdot (-2) + 35 \cdot 7 = -238 + 245 = 7$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for answering 0. The algorithm stops when a remainder is 0, but the answer is the divisor in that last division, the previous remainder. In the trace of $(1071, 462)$ the final remainder is 0 and the answer is 21.

</div>

<div class="warning" markdown>

Watch out for treating Bezout's coefficients as unique. If $ax + by = g$, then for every integer $k$ also

$$
a\left(x + k\frac{b}{g}\right) + b\left(y - k\frac{a}{g}\right) = g,
$$

because the $k$ terms cancel: $k\frac{ab}{g} - k\frac{ab}{g} = 0$. For 1071 and 462 we have $\frac{b}{g} = 22$ and $\frac{a}{g} = 51$, so $(x, y) = (19, -44)$ works too: $1071 \cdot 19 - 462 \cdot 44 = 20{,}349 - 20{,}328 = 21$. The pair the algorithm gives is one of them, usually the smallest in size.

</div>

<div class="warning" markdown>

Watch out for reading Bezout as "any target can be reached". The combinations $ax + by$ are exactly the multiples of $g$. For $119x + 35y$ the values 7, 14 and $-21$ are reachable and 10 is not. The equation $ax + by = c$ has integer solutions if and only if $\gcd(a, b) \mid c$, which is the test used for [linear congruences](04-modular-inverses-and-chinese-remainder-theorem.md).

</div>

A version of the algorithm that subtracts instead of dividing is correct but slow: for $(10^9, 1)$ it makes a billion subtractions where division makes one. The speed in Corollary 4 depends on using the full quotient.

## Tricks and shortcuts

- Subtracting a multiple never changes the GCD, so you can simplify before dividing: $\gcd(1001, 91)$ is $\gcd(1001 - 11 \cdot 91, 91) = \gcd(0, 91)$. Spotting an easy multiple saves a row.
- The gcd of a list is built one pair at a time: $\gcd(a, b, c) = \gcd(\gcd(a, b), c)$. In Python, `math.gcd(a, b, c)` accepts several arguments.
- For Mersenne-style numbers, $\gcd(2^a - 1, 2^b - 1) = 2^{\gcd(a, b)} - 1$. For example $\gcd(2^{12} - 1, 2^{18} - 1) = 2^6 - 1 = 63$. This is a fact to use, not one proved here.
- To reduce a fraction $\frac{a}{b}$ to lowest terms, divide both by $\gcd(a, b)$. It is how `fractions.Fraction` works, and with Euclid's algorithm it never needs a factorization.

## In code

The first function is Euclid's algorithm, the second the forward extended table, and the last lines check the identities of this lesson.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import random

def gcd(a, b):
    """Euclid's algorithm. Python's % keeps the remainder nonnegative for b > 0."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def egcd(a, b):
    """Extended Euclid: return (g, x, y) with a*x + b*y == g == gcd(a, b)."""
    x0, y0, x1, y1 = 1, 0, 0, 1          # a = 1*a + 0*b and b = 0*a + 1*b
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def lcm(a, b):
    return a // gcd(a, b) * b            # divide first to keep the numbers small

print(gcd(1071, 462), gcd(84, 360), gcd(-12, 18), gcd(17, 0))   # 21 12 6 17
print(egcd(1071, 462), egcd(240, 46))        # (21, -3, 7) (2, -9, 47)
print(lcm(18, 48), math.lcm(18, 48))         # 144 144

random.seed(7)
a = random.randrange(10**99, 10**100)
b = random.randrange(10**99, 10**100)
g, x, y = egcd(a, b)
print(g == math.gcd(a, b), a * x + b * y == g)   # True True

steps = 0
while b:                                     # count the divisions
    a, b = b, a % b
    steps += 1
print(steps)                                 # 184
```

</details>

The last line shows two random 100-digit numbers finishing in 184 divisions, well under the bound of 568, and instantly.

## FAQ

### Why does Euclid's algorithm always stop?

Each remainder is smaller than the one before and none is negative, so the sequence of remainders can't go on forever. This is the well-ordering principle at work (Theorem 2). It also shows why the order $r < b$ in the division algorithm matters: with a bigger remainder allowed, the numbers might not shrink.

### Why is Euclid's algorithm fast when factoring is slow?

Each division at least halves the size every two steps (Theorem 3), so the number of steps is proportional to the number of digits. Factoring has no known method with that property. The gap between the two problems is what [RSA cryptography](06-rsa-cryptography.md) relies on.

### Why would I want the numbers $x$ and $y$?

Because they give inverses. If $\gcd(a, n) = 1$ and $ax + ny = 1$, then reducing mod $n$ gives $ax \equiv 1 \pmod n$, so $x$ is a multiplicative inverse of $a$ mod $n$. Computing inverses is the main use of the extended algorithm ([modular inverses and the Chinese remainder theorem](04-modular-inverses-and-chinese-remainder-theorem.md)), and it is how an RSA private key is found.

### Does the order of the two inputs matter?

Not for the answer. If $a < b$, the first division swaps them, as in Example 3. In the extended algorithm the coefficients $x$ and $y$ swap with them, so keep track of which belongs to which number.

## Practice

### Warm-up

1\. Use Euclid's algorithm to find $\gcd(1001, 429)$, and write the trace table.

<details class="solution" markdown>
<summary>Solution</summary>

| Step | $a$ | $b$ | $q$ | $r$ |
|---|---|---|---|---|
| 1 | 1001 | 429 | 2 | 143 |
| 2 | 429 | 143 | 3 | 0 |

The last nonzero remainder is 143, so $\gcd(1001, 429) = 143$.

Check: $1001 = 7 \cdot 143$ and $429 = 3 \cdot 143$, and 7 and 3 share no factor but 1. By primes, $1001 = 7 \cdot 11 \cdot 13$ and $429 = 3 \cdot 11 \cdot 13$, which share $11 \cdot 13 = 143$.

</details>

2\. Which of these pairs are coprime? (a) 35 and 64. (b) 91 and 143. (c) 221 and 247.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $64 = 1 \cdot 35 + 29$, $35 = 1 \cdot 29 + 6$, $29 = 4 \cdot 6 + 5$, $6 = 1 \cdot 5 + 1$, $5 = 5 \cdot 1 + 0$. The GCD is 1, so they are coprime.

(b) $143 = 1 \cdot 91 + 52$, $91 = 1 \cdot 52 + 39$, $52 = 1 \cdot 39 + 13$, $39 = 3 \cdot 13 + 0$. The GCD is 13, so they are not coprime.

(c) $247 = 1 \cdot 221 + 26$, $221 = 8 \cdot 26 + 13$, $26 = 2 \cdot 13 + 0$. The GCD is 13, so they are not coprime.

Check: $91 = 7 \cdot 13$ and $143 = 11 \cdot 13$; $221 = 13 \cdot 17$ and $247 = 13 \cdot 19$; and 35 and 64 share no prime factor ($5 \cdot 7$ against $2^6$).

</details>

3\. Find $\operatorname{lcm}(126, 210)$ using the GCD.

<details class="solution" markdown>
<summary>Solution</summary>

Euclid: $210 = 1 \cdot 126 + 84$, $126 = 1 \cdot 84 + 42$, $84 = 2 \cdot 42 + 0$, so $\gcd = 42$. Then $\operatorname{lcm} = \frac{126}{42} \cdot 210 = 3 \cdot 210 = 630$.

Check: $630 = 5 \cdot 126 = 3 \cdot 210$, and $42 \cdot 630 = 26{,}460 = 126 \cdot 210$.

</details>

### Standard

4\. Find integers $x$ and $y$ with $1769x + 551y = \gcd(1769, 551)$.

<details class="solution" markdown>
<summary>Solution</summary>

Divide: $1769 = 3 \cdot 551 + 116$, $551 = 4 \cdot 116 + 87$, $116 = 1 \cdot 87 + 29$, $87 = 3 \cdot 29 + 0$. So the GCD is 29. Substituting upward:

$$
\begin{aligned}
29 &= 116 - 87 \\
&= 116 - (551 - 4 \cdot 116) = 5 \cdot 116 - 551 \\
&= 5\,(1769 - 3 \cdot 551) - 551 = 5 \cdot 1769 - 16 \cdot 551.
\end{aligned}
$$

So $x = 5$ and $y = -16$.

Check: $5 \cdot 1769 = 8845$ and $16 \cdot 551 = 8816$, and $8845 - 8816 = 29$.

</details>

5\. Prove that $\gcd(n, n + 1) = 1$ for every positive integer $n$, and that $\gcd(n, n + 2)$ is 1 or 2.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: a common divisor divides every combination of the two numbers. What we want: the possible values of the GCD. The plan: let $d$ be a common divisor, and see what it must divide.

*Proof.* Let $d$ divide both $n$ and $n + 1$. Then $d \mid (n + 1) - n = 1$, so $d = \pm 1$ and the GCD is 1. For $n$ and $n + 2$, a common divisor $d$ divides $(n + 2) - n = 2$, so $d \in \{\pm 1, \pm 2\}$ and the GCD is 1 or 2. $\blacksquare$

Check: $\gcd(9, 11) = 1$ and $\gcd(8, 10) = 2$. The GCD is 2 exactly when $n$ is even, because then 2 divides both.

</details>

6\. How many divisions does Euclid's algorithm make on $(6765, 4181)$? What is the smallest pair $a > b \ge 1$ that needs 5 divisions?

<details class="solution" markdown>
<summary>Solution</summary>

These are consecutive Fibonacci numbers, $F_{20} = 6765$ and $F_{19} = 4181$. Every quotient is 1 until the last: $6765 = 1 \cdot 4181 + 2584$, $4181 = 1 \cdot 2584 + 1597$, and so on down the Fibonacci numbers to $3 = 1 \cdot 2 + 1$ and $2 = 2 \cdot 1 + 0$. By Theorem 5 with $a = F_{k+2}$, we have $k + 2 = 20$ and $k = 18$ divisions.

For 5 divisions, Theorem 5 says $b \ge F_6 = 8$ and $a \ge F_7 = 13$, and the pair $(13, 8)$ meets both bounds. Its divisions are $13 = 1 \cdot 8 + 5$, $8 = 1 \cdot 5 + 3$, $5 = 1 \cdot 3 + 2$, $3 = 1 \cdot 2 + 1$, $2 = 2 \cdot 1 + 0$, which is five.

Check: the halving bound for 4181 is $2\log_2 4181 + 2 \approx 26.1$, and 18 is below it.

</details>

### Challenge

7\. Prove that if $\gcd(a, b) = 1$, $a \mid c$ and $b \mid c$, then $ab \mid c$. Why does it fail without $\gcd(a, b) = 1$?

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Lemma 8. What we want: $ab \mid c$. The plan: write $c = ak$, and show $b \mid k$.

*Proof.* Since $a \mid c$, write $c = ak$. Since $b \mid c$, we have $b \mid ak$. As $\gcd(a, b) = 1$, Lemma 8 (with the roles of the letters changed) gives $b \mid k$, say $k = bj$. Then $c = abj$, so $ab \mid c$. $\blacksquare$

Without coprimality it can fail: $4 \mid 12$ and $6 \mid 12$ but $24 \nmid 12$. Here $\gcd(4, 6) = 2$, and what is true is $\operatorname{lcm}(4, 6) = 12 \mid 12$.

Check: with $a = 3$ and $b = 5$, the numbers divisible by both are the multiples of 15, as expected.

</details>

8\. This one reviews the [factors lesson](../../01-elementary/08-factors-multiples-and-primes.md). Find $\gcd(84, 360)$ both by prime factorization and by Euclid's algorithm, then write the GCD as $84x + 360y$.

<details class="solution" markdown>
<summary>Solution</summary>

By primes, $84 = 2^2 \cdot 3 \cdot 7$ and $360 = 2^3 \cdot 3^2 \cdot 5$, and the smaller exponents give $2^2 \cdot 3 = 12$.

By Euclid, $360 = 4 \cdot 84 + 24$, $84 = 3 \cdot 24 + 12$, $24 = 2 \cdot 12 + 0$, so the GCD is 12, in agreement.

Back-substitution: $12 = 84 - 3 \cdot 24 = 84 - 3\,(360 - 4 \cdot 84) = 13 \cdot 84 - 3 \cdot 360$. So $x = 13$ and $y = -3$.

Check: $13 \cdot 84 = 1092$ and $3 \cdot 360 = 1080$, and $1092 - 1080 = 12$.

</details>

## Where this shows up

- The next lesson, [primes and unique factorization](03-primes-and-unique-factorization.md), proves Euclid's lemma from Bezout's identity and uses it to show factorization is unique.
- Modular inverses, the Chinese remainder theorem and every RSA private key rely on the extended algorithm ([modular inverses and the Chinese remainder theorem](04-modular-inverses-and-chinese-remainder-theorem.md)).
- The analysis of Euclid's algorithm is a standard example of running time in terms of the number of digits, in [asymptotic notation](../04-sums-recurrences-and-algorithms/04-asymptotic-notation.md), and a standard loop invariant in [invariants and algorithm correctness](../04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md).
