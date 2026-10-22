# Modular inverses and the Chinese remainder theorem

After this lesson you can decide when a number has an inverse mod $n$ and find it, solve any linear congruence $ax \equiv b \pmod n$ (no solution, one or several), and solve a system of congruences with the Chinese remainder theorem.

Before this: [divisibility and modular arithmetic](01-divisibility-and-modular-arithmetic.md), [GCD and Euclid's algorithm](02-gcd-and-euclids-algorithm.md) (Bezout's identity and the extended algorithm) and [primes and unique factorization](03-primes-and-unique-factorization.md) (Euclid's lemma).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find an inverse of 3 mod 11, that is, a number $b$ with $3b \equiv 1 \pmod{11}$.
2. Does $6x \equiv 4 \pmod{10}$ have a solution? How many solutions are there between 0 and 9?
3. Find a number $x$ with $x \equiv 2 \pmod 3$ and $x \equiv 3 \pmod 5$.

<details class="solution" markdown>
<summary>Answers</summary>

1. Since $3 \cdot 4 = 12 \equiv 1$, the number 4 is an inverse.
2. Yes. Testing $x = 0, \dots, 9$ gives $6x \bmod 10 = 0, 6, 2, 8, 4, 0, 6, 2, 8, 4$, so $x = 4$ and $x = 9$ work: two solutions.
3. The numbers that are $\equiv 3 \pmod 5$ are 3, 8, 13, ..., and 8 is also $\equiv 2 \pmod 3$. So $x = 8$ (and every number $8 + 15k$).

</details>

## The idea

In ordinary arithmetic, to solve $3x = 12$ you divide by 3, which means multiplying by $\frac{1}{3}$, the number with $3 \cdot \frac{1}{3} = 1$. Modular arithmetic has no fractions, but sometimes there is a whole number that plays the same role. Mod 11, the number 4 undoes multiplication by 3, because $3 \cdot 4 \equiv 1$. So $3x \equiv 5 \pmod{11}$ gives $x \equiv 4 \cdot 5 = 20 \equiv 9$.

Sometimes there is no such number. Mod 10, multiplying by 6 sends 0 to 0, 1 to 6, 2 to 2, 3 to 8, 4 to 4, 5 to 0, and so on: only the even numbers ever come out, and each is hit twice. Nothing can undo that. Multiplying by 3 mod 10 sends 0, 1, 2, ..., 9 to 0, 3, 6, 9, 2, 5, 8, 1, 4, 7, so every number is hit exactly once, and the shuffle can be reversed.

The first half of the lesson says exactly when the shuffle can be reversed (when $\gcd(a, n) = 1$), how to find the reversal, and what to do when it can't. The second half is the Chinese remainder theorem: if you know a number's remainders mod several pairwise coprime numbers, you know the number mod their product. A Chinese text of the 3rd to 5th century, the *Sunzi Suanjing*, poses it as a puzzle about counting soldiers by threes, fives and sevens. In computing it means that arithmetic with a huge modulus can be split into arithmetic with several small ones.

## Definitions

Let $n \ge 1$. We write $\mathbb{Z}_n$ for the residues $0, 1, \dots, n - 1$ with addition and multiplication mod $n$ (the classes of the [equivalence relations lesson](../../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md), named by their remainders).

An **inverse** of $a$ mod $n$ is an integer $b$ with $ab \equiv 1 \pmod n$. We write it $a^{-1}$ when the modulus is clear. A **unit** mod $n$ is a residue that has an inverse. In plain words, $b$ undoes multiplication by $a$: multiplying $ax \equiv c$ through by $b$ gives $x \equiv bc$. Mod 11 the number 3 is a unit with inverse 4. The notation $a^{-1}$ is not the fraction $\frac{1}{a}$, which isn't an integer, and it is only defined when the inverse exists.

A **linear congruence** is an equation $ax \equiv b \pmod n$ in the unknown $x$. A **system** of congruences is several of them at once, such as $x \equiv 2 \pmod 3$ and $x \equiv 3 \pmod 5$. Moduli $m_1, \dots, m_k$ are **pairwise coprime** if $\gcd(m_i, m_j) = 1$ whenever $i \ne j$. For example 3, 5 and 7 are pairwise coprime, and 4, 9 and 25 are, but 4, 6 and 9 are not (since $\gcd(4, 6) = 2$).

## How to do it

### When does an inverse exist?

*Theorem 1.* Let $n \ge 1$ and let $a$ be an integer. Then $a$ has an inverse mod $n$ if and only if $\gcd(a, n) = 1$.

What we know: Bezout's identity and its corollary (Corollary 7 of the GCD lesson). What we want: both directions. The plan: an inverse gives a combination equal to 1, and a combination equal to 1 gives an inverse.

*Proof.* Suppose $ab \equiv 1 \pmod n$. Then $n \mid ab - 1$, so $ab - 1 = nk$ for an integer $k$, and $ab + n(-k) = 1$. A common divisor of $a$ and $n$ divides this combination, so it divides 1, and $\gcd(a, n) = 1$.

Conversely, suppose $\gcd(a, n) = 1$. By Bezout, $ax + ny = 1$ for some integers $x$ and $y$. Then $ax - 1 = -ny$ is a multiple of $n$, so $ax \equiv 1 \pmod n$, and $x$ is an inverse. $\blacksquare$

Look back: the proof is Bezout's identity read mod $n$, and it shows how to find the inverse, because $x$ is the coefficient the extended Euclidean algorithm produces. Check: mod 10, the numbers 1, 3, 7, 9 are coprime to 10, and the inverse pairs are $1 \cdot 1$, $3 \cdot 7 = 21$ and $9 \cdot 9 = 81$, all $\equiv 1$. The numbers 2, 4, 5, 6, 8 have no inverse.

*Corollary 2.* (a) An inverse mod $n$ is unique mod $n$: if $b$ and $b'$ are both inverses of $a$, then $b \equiv b'$. (b) If $p$ is prime, every residue $1, 2, \dots, p - 1$ has an inverse mod $p$. (c) If $\gcd(c, n) = 1$ and $cb \equiv cb' \pmod n$, then $b \equiv b' \pmod n$.

*Proof.* (a) $b \equiv b(ab') = (ba)b' \equiv b'$, using the congruence rules. (b) A prime $p$ has no divisors except 1 and $p$, so $\gcd(a, p) = 1$ for $1 \le a \le p - 1$. (c) Multiply both sides by an inverse of $c$. $\blacksquare$

In plain words, modulo a prime every nonzero residue can be divided by, so $\mathbb{Z}_p$ has all four operations (this is what "field" means in algebra courses). Part (c) is the cancellation rule that was missing in the last lesson: you may cancel a factor only when it is coprime to the modulus.

### Finding an inverse

1. Check that $\gcd(a, n) = 1$ with Euclid's algorithm on $n$ and $a$ (the trace table). If the GCD is more than 1, stop: there is no inverse.
2. Use back-substitution (or the forward table) to write $1 = ax + ny$.
3. The inverse is $x$ reduced mod $n$. A negative $x$ is fine as an answer, but add $n$ to get the standard residue.
4. Check by multiplying $a$ by your answer and reducing mod $n$.

In Python, `pow(a, -1, n)` does all four steps, and raises `ValueError` if the inverse doesn't exist.

### Solving $ax \equiv b$

*Theorem 3.* Let $g = \gcd(a, n)$. The congruence $ax \equiv b \pmod n$ has a solution if and only if $g \mid b$. When it does, it has exactly $g$ solutions between $0$ and $n - 1$. They are all congruent mod $n/g$, so they can be written $x \equiv x_0 + k \cdot \frac{n}{g} \pmod n$ for $k = 0, 1, \dots, g - 1$, where $x_0$ is the solution of the reduced congruence

$$
\frac{a}{g}\, x \equiv \frac{b}{g} \pmod{\frac{n}{g}}.
$$

What we know: Theorem 1, and that $x$ solves $ax \equiv b$ exactly when $n \mid ax - b$. What we want: the test, and the solutions. The plan: show that a solution forces $g \mid b$, then divide everything by $g$ to land on a case where the coefficient is invertible.

*Proof.* If $x$ is a solution, then $ax - b = nk$ for some integer $k$, so $b = ax - nk$ is a combination of $a$ and $n$, divisible by $g$. So a solution forces $g \mid b$.

Now suppose $g \mid b$. Write $a = ga'$, $b = gb'$ and $n = gn'$. Then $n \mid ax - b$ means $gn' \mid g(a'x - b')$, which says $n' \mid a'x - b'$. That is the reduced congruence $a'x \equiv b' \pmod{n'}$. Since $\gcd(a', n') = 1$ (as in the proof of Theorem 9 of the GCD lesson), Theorem 1 gives an inverse of $a'$ mod $n'$, and the reduced congruence has exactly one solution class mod $n'$, namely $x \equiv x_0 = b' (a')^{-1} \pmod{n'}$. The integers from $0$ to $n - 1$ in this class are $x_0 + kn'$ for $k = 0, \dots, g - 1$, which is $g$ numbers, because $n = gn'$. $\blacksquare$

Look back: when $g = 1$ the theorem says that there is exactly one solution, $x \equiv a^{-1} b$. The case of no solution is as important: $6x \equiv 5 \pmod 9$ has $g = 3$ and $3 \nmid 5$, so no solution exists. As steps:

1. Compute $g = \gcd(a, n)$.
2. If $g \nmid b$, there is no solution. Stop.
3. Divide $a$, $b$ and $n$ by $g$.
4. Find the inverse of $a' = a/g$ mod $n' = n/g$, and set $x_0 = b'(a')^{-1} \bmod n'$.
5. The solutions mod $n$ are $x_0, x_0 + n', \dots, x_0 + (g-1)n'$.
6. Check each in the original congruence.

### The Chinese remainder theorem

We need a fact about pairwise coprime numbers.

*Lemma 4.* If $m_1, \dots, m_k$ are pairwise coprime, then for each $i$ the number $M_i = M / m_i$ (the product of all the other moduli) is coprime to $m_i$. Also, if every $m_i$ divides an integer $c$, then the product $M = m_1 \cdots m_k$ divides $c$.

*Proof.* Suppose a prime $p$ divided both $M_i$ and $m_i$. By Euclid's lemma (Corollary 4 of the primes lesson), $p$ divides some $m_j$ with $j \ne i$, so $p$ is a common divisor of $m_i$ and $m_j$, contradicting $\gcd(m_i, m_j) = 1$. So $M_i$ and $m_i$ have no prime divisor in common, so their GCD is 1 (a GCD above 1 would have a prime divisor by Theorem 1 of the primes lesson).

For the second claim, use induction on $k$. For $k = 1$ it is trivial. Suppose $m_1 \cdots m_{k-1}$ divides $c$ and $m_k$ divides $c$, and write $c = m_1 \cdots m_{k-1} \cdot t$. The first part, applied to the moduli $m_1, \dots, m_k$ (with $i = k$), says $m_1 \cdots m_{k-1}$ is coprime to $m_k$. Since $m_k$ divides $(m_1 \cdots m_{k-1}) \cdot t$, the coprime lemma gives $m_k \mid t$, so $M \mid c$. $\blacksquare$

*Theorem 5 (Chinese remainder theorem).* Let $m_1, \dots, m_k$ be pairwise coprime, $M = m_1 m_2 \cdots m_k$, and let $a_1, \dots, a_k$ be any integers. Then the system

$$
x \equiv a_1 \pmod{m_1}, \quad x \equiv a_2 \pmod{m_2}, \quad \dots, \quad x \equiv a_k \pmod{m_k}
$$

has a solution, and the solution is unique mod $M$: any two solutions are congruent mod $M$.

What we know: Theorem 1 and Lemma 4. What we want: existence, by an explicit formula, and uniqueness mod $M$. The plan: build, for each $i$, a number that is $1$ mod $m_i$ and $0$ mod every other modulus, then add up the pieces weighted by the $a_i$.

*Proof.* Existence. For each $i$ let $M_i = M/m_i$. By Lemma 4, $\gcd(M_i, m_i) = 1$, so by Theorem 1 there is $y_i$ with $M_i y_i \equiv 1 \pmod{m_i}$. Put

$$
x = a_1 M_1 y_1 + a_2 M_2 y_2 + \dots + a_k M_k y_k.
$$

Fix $j$. For $i \ne j$, the modulus $m_j$ divides $M_i$, since $m_j$ is one of the factors of $M_i$, so the term $a_i M_i y_i \equiv 0 \pmod{m_j}$. The remaining term is $a_j M_j y_j \equiv a_j \cdot 1 = a_j \pmod{m_j}$. So $x \equiv a_j \pmod{m_j}$ for every $j$.

Uniqueness. If $x$ and $x'$ are both solutions, then $x - x' \equiv a_j - a_j = 0 \pmod{m_j}$ for every $j$, so every $m_j$ divides $x - x'$. By Lemma 4, $M \mid x - x'$, so $x \equiv x' \pmod M$. $\blacksquare$

Look back: the proof is a recipe. The number $e_i = M_i y_i$ is $1$ mod $m_i$ and $0$ mod each other modulus, and $x$ is a weighted sum $\sum a_i e_i$, like an interpolation formula. To use it:

1. Compute $M$ and each $M_i = M / m_i$.
2. Find $y_i = M_i^{-1} \bmod m_i$ (reduce $M_i$ mod $m_i$ first to keep numbers small).
3. Compute $x = \sum a_i M_i y_i$ and reduce mod $M$.
4. Check $x \bmod m_i = a_i$ for each $i$.

For two congruences there is a shorter route. Write $x = a_1 + m_1 t$. The second congruence says $a_1 + m_1 t \equiv a_2 \pmod{m_2}$, which is a linear congruence in $t$ with solution $t \equiv (a_2 - a_1)\, m_1^{-1} \pmod{m_2}$. Then $x = a_1 + m_1 t$ for that $t$.

A consequence: the map $x \mapsto (x \bmod m_1, \dots, x \bmod m_k)$ from $\mathbb{Z}_M$ to the list of remainders is a one-to-one correspondence (the theorem says every list is hit, and by exactly one residue mod $M$). The correspondence respects addition and multiplication: the remainders of $x + y$ and $xy$ are the sums and products of the remainders, taken mod each $m_i$ separately. So arithmetic mod $M$ can be done mod each small $m_i$ and put back together at the end.

When the moduli are not coprime, the system may or may not be solvable. For two moduli, it is solvable exactly when $a_1 \equiv a_2 \pmod{\gcd(m_1, m_2)}$, and then the solution is unique mod $\operatorname{lcm}(m_1, m_2)$. For example, $x \equiv 1 \pmod 4$ and $x \equiv 3 \pmod 6$ is solvable ($x = 9$, unique mod 12), while $x \equiv 1 \pmod 4$ and $x \equiv 2 \pmod 6$ is not, because the first forces $x$ to be odd and the second forces it to be even.

## Worked examples

<div class="example" markdown>

### Example 1: the inverse of 7 mod 40

Step 1: Euclid's algorithm on 40 and 7 gives $40 = 5 \cdot 7 + 5$, then $7 = 1 \cdot 5 + 2$, then $5 = 2 \cdot 2 + 1$, then $2 = 2 \cdot 1 + 0$. The GCD is 1, so the inverse exists.

Step 2: back-substitute from the line with remainder 1:

$$
\begin{aligned}
1 &= 5 - 2 \cdot 2 \\
&= 5 - 2\,(7 - 5) = 3 \cdot 5 - 2 \cdot 7 \\
&= 3\,(40 - 5 \cdot 7) - 2 \cdot 7 = 3 \cdot 40 - 17 \cdot 7.
\end{aligned}
$$

So $7 \cdot (-17) \equiv 1 \pmod{40}$. Step 3: reduce, $-17 + 40 = 23$.

Step 4, the check: $7 \cdot 23 = 161 = 4 \cdot 40 + 1$. The inverse of 7 mod 40 is 23, and `pow(7, -1, 40)` gives 23.

Use it: $7x \equiv 3 \pmod{40}$ gives $x \equiv 23 \cdot 3 = 69 \equiv 29$. Check: $7 \cdot 29 = 203 = 5 \cdot 40 + 3$.

<div class="warning" markdown>

Watch out at step 3: the coefficient $-17$ is a correct inverse, but if you leave it negative and later multiply and reduce, a negative remainder can slip into an answer. Reduce to the standard range 0 to $n - 1$ as the last step.

</div>

</div>

<div class="example" markdown>

### Example 2: three linear congruences

Solve (a) $6x \equiv 4 \pmod{10}$, (b) $6x \equiv 5 \pmod 9$, (c) $12x \equiv 18 \pmod{30}$.

(a) Step 1: $g = \gcd(6, 10) = 2$. Step 2: $2 \mid 4$, so there are solutions. Step 3: divide by 2 to get $3x \equiv 2 \pmod 5$. Step 4: the inverse of 3 mod 5 is 2 (since $3 \cdot 2 = 6 \equiv 1$), so $x_0 = 2 \cdot 2 = 4$. Step 5: the solutions mod 10 are $4$ and $4 + 5 = 9$.

(b) $g = \gcd(6, 9) = 3$ and $3 \nmid 5$. No solution.

(c) $g = \gcd(12, 30) = 6$ and $6 \mid 18$. Dividing by 6 gives $2x \equiv 3 \pmod 5$. The inverse of 2 mod 5 is 3, so $x_0 = 3 \cdot 3 = 9 \equiv 4$. The six solutions mod 30 are $4, 9, 14, 19, 24, 29$.

Check: $6 \cdot 4 = 24 \equiv 4$ and $6 \cdot 9 = 54 \equiv 4 \pmod{10}$. For (b), $6x \bmod 9$ takes only the values 0, 3, 6, never 5. For (c), $12 \cdot 4 = 48 = 30 + 18$ and $12 \cdot 9 = 108 = 3 \cdot 30 + 18$.

</div>

<div class="example" markdown>

### Example 3: the soldiers puzzle

Solve $x \equiv 2 \pmod 3$, $x \equiv 3 \pmod 5$ and $x \equiv 2 \pmod 7$.

Step 1: the moduli are pairwise coprime, $M = 105$, and $M_1 = 35$, $M_2 = 21$, $M_3 = 15$. Step 2: find the inverses of each $M_i$ mod $m_i$, reducing first.

| $i$ | $m_i$ | $a_i$ | $M_i$ | $M_i \bmod m_i$ | $y_i$ | $a_i M_i y_i$ |
|---|---|---|---|---|---|---|
| 1 | 3 | 2 | 35 | 2 | 2 | 140 |
| 2 | 5 | 3 | 21 | 1 | 1 | 63 |
| 3 | 7 | 2 | 15 | 1 | 1 | 30 |

Here $y_1 = 2$ because $2 \cdot 2 = 4 \equiv 1 \pmod 3$. Step 3: the sum is $140 + 63 + 30 = 233$, and $233 - 2 \cdot 105 = 23$. So $x \equiv 23 \pmod{105}$.

Check: $23 = 7 \cdot 3 + 2$, $23 = 4 \cdot 5 + 3$ and $23 = 3 \cdot 7 + 2$. The smallest positive solution is 23, and the others are $23 + 105k$.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Solve $x \equiv 3 \pmod 8$ and $x \equiv 5 \pmod{11}$ with the two-congruence route. Start: write $x = 3 + 8t$. The second congruence becomes $3 + 8t \equiv 5 \pmod{11}$, that is $8t \equiv 2 \pmod{11}$. Finish: find the inverse of 8 mod 11, solve for $t$, find $x$ and check.

<details class="solution" markdown>
<summary>Finish</summary>

Since $8 \cdot 7 = 56 = 5 \cdot 11 + 1$, the inverse of 8 mod 11 is 7. So $t \equiv 7 \cdot 2 = 14 \equiv 3 \pmod{11}$, and $x = 3 + 8 \cdot 3 = 27$. The solution is $x \equiv 27 \pmod{88}$.

Check: $27 = 3 \cdot 8 + 3$ and $27 = 2 \cdot 11 + 5$. Using the general formula with $M_1 = 11$, $y_1 = 3$, $M_2 = 8$ and $y_2 = 7$ gives $3 \cdot 11 \cdot 3 + 5 \cdot 8 \cdot 7 = 99 + 280 = 379 = 4 \cdot 88 + 27$, the same.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for cancelling without checking. From $6 \cdot 2 \equiv 6 \cdot 4 \pmod{12}$ you can't cancel the 6, since $\gcd(6, 12) = 6$. What is true is the weaker $2 \equiv 4 \pmod{12/6}$, that is, mod 2. In general $ca \equiv cb \pmod n$ gives $a \equiv b \pmod{n / \gcd(c, n)}$ (divide $n \mid c(a - b)$ by $g = \gcd(c, n)$ to get $\frac{n}{g} \mid \frac{c}{g}(a - b)$, then use the coprime lemma).

</div>

<div class="warning" markdown>

Watch out for dividing as if the numbers were real. To solve $3x \equiv 4 \pmod 7$, writing $x = \frac{4}{3}$ is wrong. Multiply by the inverse instead: $3^{-1} = 5$, so $x \equiv 5 \cdot 4 = 20 \equiv 6$. Check: $3 \cdot 6 = 18 \equiv 4$.

</div>

<div class="warning" markdown>

Watch out for the Chinese remainder theorem with moduli that share a factor. The system $x \equiv 1 \pmod 4$, $x \equiv 2 \pmod 6$ has no solution, and the formula would divide by a non-unit. Check pairwise coprimality first; if it fails, use the compatibility test above.

</div>

A congruence $ax \equiv b$ with $g > 1$ and $g \mid b$ has several solutions, and a complete answer lists all $g$ of them mod $n$, or states them as one class mod $n/g$. The modulus 1 is degenerate (everything is congruent), and $a \equiv 0$ is a unit only mod 1.

## Tricks and shortcuts

- Test small inverses by hand: look for a multiple of $a$ that is one more than a multiple of $n$. For $a = 7$ and $n = 40$, the multiples $7, 14, 21, \dots$ reach 161 at the 23rd, since $161 = 4 \cdot 40 + 1$.
- Special inverses: $1^{-1} = 1$, $(-1)^{-1} = -1$, and $2^{-1} = \frac{n+1}{2}$ for odd $n$ (check: $2 \cdot \frac{n+1}{2} = n + 1 \equiv 1$).
- For two congruences, the shortcut $x = a_1 + m_1 \cdot \big((a_2 - a_1)\, m_1^{-1} \bmod m_2\big)$ needs only one inverse. For $x \equiv 3 \pmod 8$ and $x \equiv 5 \pmod{11}$: $(5 - 3)\cdot 7 = 14 \equiv 3$, so $x = 3 + 8 \cdot 3 = 27$.
- With three or more moduli, merge two at a time: solve the first two to get one congruence mod $m_1 m_2$, then merge that with the third.
- Mod a prime $p$, Fermat's little theorem gives the inverse as $a^{p-2}$ ([Fermat, Euler and fast exponentiation](05-fermat-euler-and-fast-exponentiation.md)), which is simplest to code when $p$ is known to be prime.

## In code

The three functions are Theorems 1, 3 and 5 written out. Python's built-in `pow(a, -1, n)` is the same inverse.

<details class="code" markdown>
<summary>In code</summary>

```python
from math import gcd

def egcd(a, b):
    """Return (g, x, y) with a*x + b*y == g == gcd(a, b)."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q, r = divmod(a, b)
        a, b = b, r
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, n):
    g, x, _ = egcd(a % n, n)
    if g != 1:
        raise ValueError(f"{a} has no inverse mod {n}")
    return x % n                         # reduce to the range 0..n-1

def solve_linear(a, b, n):
    """All solutions x in 0..n-1 of a*x = b (mod n)."""
    g = gcd(a, n)
    if b % g != 0:
        return []                        # no solution
    a2, b2, n2 = a // g, b // g, n // g
    x0 = (b2 * modinv(a2, n2)) % n2
    return [x0 + k * n2 for k in range(g)]

def crt(residues, moduli):
    """Solve x = a_i (mod m_i) for pairwise coprime moduli; return x in 0..M-1."""
    M = 1
    for m in moduli:
        M *= m
    x = 0
    for a, m in zip(residues, moduli):
        Mi = M // m
        x += a * Mi * modinv(Mi, m)
    return x % M

print(modinv(7, 40), pow(7, -1, 40), modinv(17, 3120))        # 23 23 2753
print(solve_linear(6, 4, 10), solve_linear(6, 5, 9), solve_linear(12, 18, 30))
# [4, 9] [] [4, 9, 14, 19, 24, 29]
print(crt([2, 3, 2], [3, 5, 7]), crt([3, 5], [8, 11]))        # 23 27
print(crt([1, 2, 3], [4, 9, 25]))                             # 353

try:
    modinv(6, 9)
except ValueError as e:
    print(e)                                                  # 6 has no inverse mod 9
```

</details>

## FAQ

### Why can't I always divide in modular arithmetic?

Division by $a$ means undoing multiplication by $a$, which requires that multiplication by $a$ be a one-to-one shuffle of the residues. If $\gcd(a, n) = g > 1$, then multiplication by $a$ only produces multiples of $g$ and hits some of them more than once, so the information is lost and no inverse can bring it back. Modulo a prime this never happens to a nonzero residue.

### Is the modular inverse the same as a reciprocal?

It plays the same role ($a \cdot a^{-1} \equiv 1$), but it is a different number. Mod 7 the inverse of 3 is 5, not $\frac{1}{3}$. If you read "$\frac{1}{3} \bmod 7$" as "the number whose product with 3 is 1", you get 5, and that is the only sensible meaning of a fraction mod $n$.

### Why do the moduli in the Chinese remainder theorem have to be coprime?

Coprimality is used twice: to get the inverses $y_i$ in the existence proof (Lemma 4 makes $M_i$ coprime to $m_i$), and to make $M$ divide $x - x'$ in the uniqueness proof. If $\gcd(m_1, m_2) > 1$, the two congruences each carry information about the shared factor, and they can contradict each other, as in the example above.

### Why is this useful when I can just compute with the big number?

Because the small pieces are cheaper and can run independently. Multiplication takes more than twice as long when the numbers are twice as long, so two multiplications with half-size moduli cost less than one with the full-size modulus. RSA decryption uses exactly this split ([RSA cryptography](06-rsa-cryptography.md)).

## Practice

### Warm-up

1\. Which of 4, 5, 6, 7 and 9 have an inverse mod 15? Find the inverse of each that does.

<details class="solution" markdown>
<summary>Solution</summary>

The GCDs with 15 are $\gcd(4, 15) = 1$, $\gcd(5, 15) = 5$, $\gcd(6, 15) = 3$, $\gcd(7, 15) = 1$ and $\gcd(9, 15) = 3$. So only 4 and 7 are units.

Looking for a multiple of 4 that is one more than a multiple of 15: $4 \cdot 4 = 16 = 15 + 1$, so the inverse of 4 is 4. For 7: $7 \cdot 13 = 91 = 6 \cdot 15 + 1$, so the inverse of 7 is 13.

Check: `pow(4, -1, 15)` is 4 and `pow(7, -1, 15)` is 13.

</details>

2\. Solve $3x \equiv 4 \pmod 7$ and $5x \equiv 1 \pmod{12}$.

<details class="solution" markdown>
<summary>Solution</summary>

Mod 7, the inverse of 3 is 5 (since $3 \cdot 5 = 15 \equiv 1$), so $x \equiv 5 \cdot 4 = 20 \equiv 6$.

Mod 12, $5 \cdot 5 = 25 \equiv 1$, so 5 is its own inverse, and $x \equiv 5 \cdot 1 = 5$.

Check: $3 \cdot 6 = 18 = 2 \cdot 7 + 4$ and $5 \cdot 5 = 25 = 2 \cdot 12 + 1$.

</details>

3\. Does $4x \equiv 6 \pmod{10}$ have a solution? Does $4x \equiv 5 \pmod{10}$?

<details class="solution" markdown>
<summary>Solution</summary>

For both, $g = \gcd(4, 10) = 2$. Since $2 \mid 6$, the first has solutions: $2x \equiv 3 \pmod 5$ gives $x \equiv 3 \cdot 3 = 9 \equiv 4 \pmod 5$, so $x = 4$ and $x = 9$. Since $2 \nmid 5$, the second has none.

Check: $4 \cdot 4 = 16 \equiv 6$ and $4 \cdot 9 = 36 \equiv 6 \pmod{10}$, while $4x \bmod 10$ is always even and so never 5.

</details>

### Standard

4\. Find the inverse of 17 mod 3120. (This is the number $d$ in the RSA example of the last lesson of the chapter.)

<details class="solution" markdown>
<summary>Solution</summary>

Euclid: $3120 = 183 \cdot 17 + 9$ (since $183 \cdot 17 = 3111$), $17 = 1 \cdot 9 + 8$, $9 = 1 \cdot 8 + 1$. Back-substitute:

$$
\begin{aligned}
1 &= 9 - 8 = 9 - (17 - 9) = 2 \cdot 9 - 17 \\
&= 2\,(3120 - 183 \cdot 17) - 17 = 2 \cdot 3120 - 367 \cdot 17.
\end{aligned}
$$

So $17 \cdot (-367) \equiv 1$, and $-367 + 3120 = 2753$.

Check: $17 \cdot 2753 = 46{,}801 = 15 \cdot 3120 + 1$.

</details>

5\. Solve $15x \equiv 9 \pmod{21}$. Give all solutions between 0 and 20.

<details class="solution" markdown>
<summary>Solution</summary>

Here $g = \gcd(15, 21) = 3$ and $3 \mid 9$. Dividing by 3 gives $5x \equiv 3 \pmod 7$. The inverse of 5 mod 7 is 3, so $x_0 = 3 \cdot 3 = 9 \equiv 2$. The three solutions are $2$, $2 + 7 = 9$ and $2 + 14 = 16$.

Check: $15 \cdot 2 = 30 = 21 + 9$, $15 \cdot 9 = 135 = 6 \cdot 21 + 9$ and $15 \cdot 16 = 240 = 11 \cdot 21 + 9$.

</details>

6\. Solve $x \equiv 1 \pmod 3$, $x \equiv 2 \pmod 4$ and $x \equiv 3 \pmod 5$.

<details class="solution" markdown>
<summary>Solution</summary>

The moduli are pairwise coprime and $M = 60$, so $M_1 = 20$, $M_2 = 15$, $M_3 = 12$. Reduce: $20 \equiv 2 \pmod 3$ with inverse 2; $15 \equiv 3 \pmod 4$ with inverse 3 (as $3 \cdot 3 = 9 \equiv 1$); $12 \equiv 2 \pmod 5$ with inverse 3. Then

$$
x = 1 \cdot 20 \cdot 2 + 2 \cdot 15 \cdot 3 + 3 \cdot 12 \cdot 3 = 40 + 90 + 108 = 238 = 3 \cdot 60 + 58.
$$

So $x \equiv 58 \pmod{60}$.

Check: $58 = 19 \cdot 3 + 1$, $58 = 14 \cdot 4 + 2$ and $58 = 11 \cdot 5 + 3$.

</details>

### Challenge

7\. Prove that the product of two units mod $n$ is a unit, and that if $a$ is a unit then so is $a^{-1}$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $a$ and $c$ have inverses $b$ and $d$. What we want: inverses for $ac$ and for $b$. The plan: guess the inverse and multiply.

*Proof.* If $ab \equiv 1$ and $cd \equiv 1$, then $(ac)(bd) = (ab)(cd) \equiv 1 \cdot 1 = 1$ by the congruence rules, so $bd$ is an inverse of $ac$. And $ab \equiv 1$ also says $b \cdot a \equiv 1$, so $a$ is an inverse of $b$, which makes $b$ a unit. $\blacksquare$

Check: mod 15, the units 4 and 7 have inverses 4 and 13. Their product is $28 \equiv 13$, and the claimed inverse is $4 \cdot 13 = 52 \equiv 7$. Indeed $13 \cdot 7 = 91 = 6 \cdot 15 + 1$.

</details>

8\. A hash table has 12 slots, numbered 0 to 11, and uses open addressing with the probe sequence $h, h + s, h + 2s, \dots$ taken mod 12, where the step $s$ is fixed. For which steps $s$ does a probe sequence visit every slot? This reviews arithmetic mod $n$ from [divisibility and modular arithmetic](01-divisibility-and-modular-arithmetic.md).

<details class="solution" markdown>
<summary>Solution</summary>

What we want: the steps $s$ for which $h + is \bmod 12$, for $i = 0, \dots, 11$, takes all 12 values. The plan: the values are distinct exactly when $is \equiv js$ forces $i \equiv j$, which is when $s$ can be cancelled.

If $\gcd(s, 12) = 1$, then $s$ is a unit, and $is \equiv js$ gives $i \equiv j$ (cancellation, Corollary 2(c)), so the 12 probes are distinct and cover every slot. If $g = \gcd(s, 12) > 1$, then $i = 12/g$ gives $is = 12 \cdot (s/g) \equiv 0$, the same as $i = 0$, so the sequence repeats after $12/g$ probes and misses slots.

So the good steps are $s = 1, 5, 7, 11$. For $s = 5$ from $h = 0$ the slots are 0, 5, 10, 3, 8, 1, 6, 11, 4, 9, 2, 7, all 12. For $s = 4$ they are 0, 4, 8, 0, ..., only 3 distinct slots.

Check: this is the same condition as in Theorem 1, and why table sizes are often prime (every step in $1, \dots, p - 1$ then works).

</details>

## Where this shows up

- The next lesson, [Fermat, Euler and fast exponentiation](05-fermat-euler-and-fast-exponentiation.md), counts the units mod $n$ (Euler's phi) and uses the cancellation rule to prove Fermat's little theorem.
- In [RSA cryptography](06-rsa-cryptography.md), the private key is an inverse (Practice 4 computes one), and decryption can be speeded up with the Chinese remainder theorem.
- Units mod 26 are what make the affine cipher $x \mapsto ax + b$ reversible, and in [matrix algebra and inverses](../../05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md) the same question returns for matrices: an inverse exists exactly when one number (the determinant) is nonzero for real matrices, or a unit for matrices mod $n$.
