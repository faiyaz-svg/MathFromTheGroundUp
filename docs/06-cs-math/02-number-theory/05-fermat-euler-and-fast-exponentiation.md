# Fermat, Euler and fast exponentiation

After this lesson you can prove Fermat's little theorem and Euler's theorem, compute Euler's phi function from a factorization, reduce huge exponents mod $n$, compute $a^e \bmod n$ with about $\log_2 e$ squarings, and explain why Fermat primality tests can be fooled.

Before this: [modular inverses and the Chinese remainder theorem](04-modular-inverses-and-chinese-remainder-theorem.md) (units, cancellation, the Chinese remainder theorem), [primes and unique factorization](03-primes-and-unique-factorization.md) and [divisibility and modular arithmetic](01-divisibility-and-modular-arithmetic.md) (computing with congruences).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Compute $3^{6} \bmod 7$ and $5^{12} \bmod 13$.
2. How many integers from 1 to 20 are coprime to 20?
3. About how many multiplications does it take to compute $a^{1000000}$ if you multiply $a$ by itself repeatedly? About how many if you square cleverly?

<details class="solution" markdown>
<summary>Answers</summary>

1. $3^6 = 729 = 104 \cdot 7 + 1$, so the first is 1. The second is also 1: by the theorem below, $a^{p-1} \equiv 1 \pmod p$ for a prime $p$ and $p \nmid a$, here $p = 13$. Direct check: $5^2 = 25 \equiv -1$, so $5^{12} = (5^2)^6 \equiv (-1)^6 = 1$.
2. Eight: 1, 3, 7, 9, 11, 13, 17 and 19. They are the numbers with no factor 2 or 5, and $20 \cdot \frac{1}{2} \cdot \frac{4}{5} = 8$.
3. Repeated multiplication takes 999,999 multiplications. Squaring takes about 20 squarings plus a few more multiplications, since $2^{20} = 1{,}048{,}576$ is just above $10^6$.

</details>

## The idea

Powers mod $n$ repeat. Take the powers of 3 mod 7: $3, 2, 6, 4, 5, 1$, then $3, 2, 6, \dots$ again. After six steps we are back at 1, and the cycle repeats forever. The same happens for 2 mod 7 with the shorter cycle $2, 4, 1$. In every case the cycle length divides 6, which is $7 - 1$. Fermat's little theorem says that this is no accident: for a prime $p$, the sixth power here is $p - 1$ and $a^{p-1} \equiv 1$ whenever $p \nmid a$.

This gives two tools. The first is exponent reduction: if you know $a^k \equiv 1$, then $a^{e}$ depends only on $e \bmod k$, so $3^{1000} \bmod 7$ is $3^{1000 \bmod 6} = 3^4$. The second is a primality filter: if $a^{n-1} \not\equiv 1 \pmod n$ for some $a$ coprime to $n$, then $n$ is not prime. For composite moduli the exponent $p - 1$ is replaced by Euler's $\varphi(n)$, the number of residues coprime to $n$.

The other half of the lesson is a computing question. A power like $a^e \bmod n$ with $e$ having 600 digits cannot be done by multiplying $e$ times, and it cannot be done by computing $a^e$ and reducing at the end (the number has more digits than there are atoms in the universe). Reducing after every multiplication keeps the numbers small, and squaring repeatedly cuts the number of multiplications from $e$ to about $2\log_2 e$. This is what makes RSA practical.

## Definitions

**Euler's phi function**, also called the totient function, is $\varphi(n)$ for $n \ge 1$, the number of integers $k$ with $1 \le k \le n$ and $\gcd(k, n) = 1$. In plain words, it counts the residues mod $n$ that are coprime to $n$. By the units theorem (Theorem 1 of the last lesson) these are exactly the units mod $n$, so $\varphi(n)$ is the number of units. For example $\varphi(12) = 4$ (the numbers 1, 5, 7, 11), $\varphi(p) = p - 1$ for a prime $p$, and $\varphi(1) = 1$.

A **reduced residue system** mod $n$ is a list of $\varphi(n)$ integers, one from each residue class coprime to $n$, for example $1, 3, 7, 9$ mod 10. In plain words, it is the list of units, written once each.

**Fast exponentiation**, or square-and-multiply, computes $a^e \bmod n$ using the binary digits of $e$. The **binary expansion** of $e \ge 1$ is $e = b_0 + 2b_1 + 4b_2 + \dots + 2^{L-1} b_{L-1}$ with each $b_i \in \{0, 1\}$ and $b_{L-1} = 1$; the length $L = \lfloor \log_2 e \rfloor + 1$ is the number of bits (the [number bases lesson](../01-number-representation/01-number-bases-and-conversions.md) has the conversion).

## How to do it

### Fermat's little theorem

*Theorem 1 (Fermat's little theorem).* Let $p$ be a prime and $a$ an integer with $p \nmid a$. Then

$$
a^{p-1} \equiv 1 \pmod p.
$$

Equivalently, $a^p \equiv a \pmod p$ for every integer $a$.

What we know: every nonzero residue mod $p$ is a unit, so we can cancel (Corollary 2 of the last lesson). What we want: the power of $a$. The plan: multiply the list $1, 2, \dots, p - 1$ by $a$, show that the products are the same list in a different order, and compare the products of the two lists.

*Proof.* Consider the $p - 1$ numbers $a, 2a, 3a, \dots, (p - 1)a$. None is $\equiv 0 \pmod p$, since $p \nmid a$ and $p \nmid i$ for $1 \le i \le p-1$ (Euclid's lemma). They are also distinct mod $p$: if $ia \equiv ja$ with $1 \le i, j \le p - 1$, then cancelling the unit $a$ gives $i \equiv j$, and so $i = j$. So these $p - 1$ numbers are $p - 1$ different nonzero residues, and there are only $p - 1$ nonzero residues. Hence they are $1, 2, \dots, p - 1$ in some order. Multiplying them all together,

$$
a \cdot 2a \cdots (p-1)a \equiv 1 \cdot 2 \cdots (p-1) \pmod p,
$$

that is, $a^{p-1} (p-1)! \equiv (p-1)! \pmod p$. The number $(p-1)!$ is a product of units, so it is a unit (Practice 7 of the last lesson), and we can cancel it: $a^{p-1} \equiv 1$. For the second form, multiply by $a$; and if $p \mid a$, both sides of $a^p \equiv a$ are $\equiv 0$. $\blacksquare$

Look back: the proof used only that the multiplication-by-$a$ map shuffles the nonzero residues without losing any. For $a = 3$ and $p = 7$:

| $i$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $3i \bmod 7$ | 3 | 6 | 2 | 5 | 1 | 4 |

The bottom row is 1 to 6 in a new order, and the product of the top row, 720, is $\equiv 6$ mod 7, the same as the product of the bottom row. So $3^6 \cdot 720 \equiv 720$, and $3^6 \equiv 1$. For a composite modulus such as 6, the argument breaks at the first step (not all of $1, \dots, 5$ are units), and $a^5 \equiv 1 \pmod 6$ is false for $a = 2$, $3$ or $4$.

### Euler's phi from the factorization

*Theorem 2.* (a) For a prime $p$ and $e \ge 1$, $\varphi(p^e) = p^e - p^{e-1} = p^{e-1}(p - 1)$. (b) If $\gcd(m, n) = 1$, then $\varphi(mn) = \varphi(m)\,\varphi(n)$.

*Proof.* (a) A number is coprime to $p^e$ unless it is a multiple of $p$ (the only prime divisor of $p^e$ is $p$). Among $1, \dots, p^e$ the multiples of $p$ are $p, 2p, \dots, p^{e-1} \cdot p$, which is $p^{e-1}$ numbers. The rest, $p^e - p^{e-1}$, are coprime.

(b) By the Chinese remainder theorem, the map $x \mapsto (x \bmod m,\ x \bmod n)$ from $\{0, \dots, mn - 1\}$ to pairs is a one-to-one correspondence. We claim $\gcd(x, mn) = 1$ exactly when $\gcd(x, m) = 1$ and $\gcd(x, n) = 1$. If a prime divides $x$ and $mn$, then by Euclid's lemma it divides $m$ or $n$, so it divides $x$ and $m$, or $x$ and $n$; the converse is clear. Also $\gcd(x, m) = \gcd(x \bmod m, m)$ by Euclid's algorithm. So the numbers coprime to $mn$ correspond to pairs (coprime to $m$, coprime to $n$), and there are $\varphi(m)\varphi(n)$ such pairs. $\blacksquare$

Combining the two with the factorization $n = p_1^{e_1} \cdots p_k^{e_k}$ (the prime powers are pairwise coprime):

$$
\varphi(n) = \prod_{i=1}^{k} p_i^{e_i - 1}(p_i - 1) = n \prod_{i=1}^{k} \left(1 - \frac{1}{p_i}\right).
$$

Examples: $\varphi(360) = \varphi(2^3)\varphi(3^2)\varphi(5) = 4 \cdot 6 \cdot 4 = 96$, and for two distinct primes $\varphi(pq) = (p - 1)(q - 1)$. For example $\varphi(77) = 6 \cdot 10 = 60$. Note that computing $\varphi(n)$ takes the factorization of $n$, and with $n = pq$ it is no easier than factoring (see RSA cryptography<!-- link: 06-rsa-cryptography.md -->).

### Euler's theorem

*Theorem 3 (Euler's theorem).* If $n \ge 1$ and $\gcd(a, n) = 1$, then $a^{\varphi(n)} \equiv 1 \pmod n$.

What we know: the units mod $n$ are closed under products and can be cancelled. What we want: the same shuffling argument as Fermat's. The plan: replace $1, \dots, p-1$ by a reduced residue system.

*Proof.* Let $r_1, \dots, r_k$ with $k = \varphi(n)$ be a reduced residue system mod $n$. The numbers $ar_1, \dots, ar_k$ are units (a product of units), and they are distinct mod $n$ (if $ar_i \equiv ar_j$, cancel the unit $a$). So they are $k$ different residues coprime to $n$, and there are exactly $k$ of those, which means they are $r_1, \dots, r_k$ in some order. Multiplying, $a^k r_1 \cdots r_k \equiv r_1 \cdots r_k$. The product $r_1 \cdots r_k$ is a unit, so cancel it: $a^k \equiv 1$. $\blacksquare$

Look back: with $n = p$ prime, $\varphi(p) = p - 1$ and this is Fermat's theorem. For $n = 10$ and $a = 3$: the units are $1, 3, 7, 9$, and $3 \cdot (1, 3, 7, 9) = (3, 9, 21, 27) \equiv (3, 9, 1, 7)$, a rearrangement. So $3^4 = 81 \equiv 1 \pmod{10}$.

### Reducing exponents

*Corollary 4.* If $\gcd(a, n) = 1$ and $e \equiv f \pmod{\varphi(n)}$ with $e, f \ge 0$, then $a^e \equiv a^f \pmod n$. In particular $a^e \equiv a^{e \bmod \varphi(n)}$.

*Proof.* Say $e \ge f$, so $e = f + k\varphi(n)$ with $k \ge 0$. Then $a^e = a^f (a^{\varphi(n)})^k \equiv a^f \cdot 1^k = a^f$. $\blacksquare$

To compute $a^e \bmod n$ for a huge $e$ with $\gcd(a, n) = 1$:

1. Compute $\varphi(n)$ from the factorization of $n$.
2. Replace $e$ by $e \bmod \varphi(n)$.
3. Compute the smaller power (by hand or by fast exponentiation).
4. Check by a second route, such as the cycle of small powers.

<div class="warning" markdown>

Watch out at step 2: the exponent is reduced mod $\varphi(n)$, not mod $n$. For $3^{14} \bmod 7$, we have $\varphi(7) = 6$ and $14 \bmod 6 = 2$, so the answer is $3^2 = 9 \equiv 2$. Reducing the exponent mod 7 instead gives $3^{14 \bmod 7} = 3^0 = 1$, which is wrong. Check: `pow(3, 14, 7)` is 2.

</div>

The condition $\gcd(a, n) = 1$ matters. For $n = 8$ and $a = 2$, $\varphi(8) = 4$, and $2^5 = 32 \equiv 0 \pmod 8$, but $2^{5 \bmod 4} = 2^1 = 2$.

### Fast exponentiation

Computing $a^e \bmod n$ by the binary digits of $e$:

1. Set `result` $= 1$ and `base` $= a \bmod n$.
2. While $e > 0$: if $e$ is odd, replace `result` by `result` $\times$ `base` $\bmod n$.
3. Replace `base` by `base` $\times$ `base` $\bmod n$, and replace $e$ by $\lfloor e / 2 \rfloor$.
4. When $e = 0$, the answer is `result`.
5. Check with a small case or a second method.

*Theorem 5.* The algorithm returns $a^e \bmod n$ and makes at most $2L$ multiplications mod $n$, where $L = \lfloor \log_2 e \rfloor + 1$ is the number of bits of $e$.

What we know: the binary expansion of $e$. What we want: correctness and the count. The plan: show that the squarings produce $a^{2^i}$, that the algorithm multiplies in exactly those with $b_i = 1$, and count the loop.

*Proof.* In round $i$ (starting at $i = 0$), `base` holds $a^{2^i}$ mod $n$: it starts as $a^{2^0}$, and squaring $a^{2^i}$ gives $a^{2^{i+1}}$. Also round $i$ looks at the lowest bit of the current $e$, which is $b_i$, because halving drops one bit each round. So `result` is multiplied by $a^{2^i}$ exactly when $b_i = 1$. After the last round,

$$
\texttt{result} \equiv \prod_{i:\, b_i = 1} a^{2^i} = a^{\sum b_i 2^i} = a^e \pmod n.
$$

The loop runs once per bit, $L$ times, and each round has at most one multiplication into `result` and one squaring. So at most $2L$ multiplications. $\blacksquare$

Look back: a second way to see correctness is the invariant "`result` $\cdot$ `base`$^{e} \equiv a^{e_0}$", where $e_0$ is the original exponent and $e$ the current one. It holds at the start (`result` $= 1$, `base` $= a$). If $e$ is odd, `result`$\cdot$`base` times (`base`$^2$)$^{(e-1)/2}$ is the same product, and if $e$ is even, `result` times (`base`$^2$)$^{e/2}$ is. When $e = 0$ the invariant says `result` $\equiv a^{e_0}$. This is the proof style of invariants and algorithm correctness<!-- link: ../04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->.

A sample count: $e = 10^6$ has 20 bits, since $2^{19} = 524{,}288 \le 10^6 < 2^{20}$, so at most 40 multiplications instead of 999,999. For a 2048-bit exponent, at most 4096.

### Fermat tests and Carmichael numbers

Fermat's theorem gives a test that finds composites without factoring them. If $\gcd(a, n) = 1$ and $a^{n-1} \not\equiv 1 \pmod n$, then $n$ is composite: if $n$ were prime, the theorem would force $a^{n-1} \equiv 1$. Such an $a$ is a **Fermat witness** for $n$. For $n = 91$ the base 2 is a witness, since $2^{90} \equiv 64 \pmod{91}$, and so 91 is composite (as $91 = 7 \cdot 13$) even though we have not found a factor.

The converse is false. If $a^{n-1} \equiv 1$, the number $n$ may still be composite. For $n = 341 = 11 \cdot 31$ we have $2^{340} \equiv 1 \pmod{341}$, so base 2 is fooled, but $3^{340} \equiv 56 \pmod{341}$ gives away that 341 is composite. A worse case is $n = 561 = 3 \cdot 11 \cdot 17$. A **Carmichael number** is a composite number $n$ with $a^{n-1} \equiv 1 \pmod n$ for every $a$ coprime to $n$. The number 561 is the smallest.

*Theorem 6.* The number 561 is a Carmichael number.

*Proof.* We have $560 = 2 \cdot 280 = 10 \cdot 56 = 16 \cdot 35$. Let $\gcd(a, 561) = 1$, so $a$ is not divisible by 3, 11 or 17. By Fermat, $a^2 \equiv 1 \pmod 3$, $a^{10} \equiv 1 \pmod{11}$ and $a^{16} \equiv 1 \pmod{17}$. Raising to the powers 280, 56 and 35, we get $a^{560} \equiv 1$ modulo each of 3, 11 and 17. These moduli are pairwise coprime with product 561, so by the uniqueness part of the Chinese remainder theorem, $a^{560} \equiv 1 \pmod{561}$. $\blacksquare$

The test still fails on 561 only for bases that share a factor with 561 (3, 6, 9, 11, 12, ...), and a random base almost never does. There are infinitely many Carmichael numbers (Alford, Granville and Pomerance, 1994); the first few are 561, 1105, 1729, 2465, 2821 and 6601. The **Miller-Rabin test** repairs the problem: it examines the square roots of 1 on the way to $a^{n-1}$, and for each composite $n$ at least three quarters of the bases give it away. In practice a few dozen random bases reduce the error below any threshold you want. This is how large primes are found for RSA<!-- link: 06-rsa-cryptography.md -->, and it is stated here without proof.

## Worked examples

<div class="example" markdown>

### Example 1: a huge power mod 10

Find the last digit of $7^{222}$, which is $7^{222} \bmod 10$.

Step 1: $10 = 2 \cdot 5$, so $\varphi(10) = 1 \cdot 4 = 4$, and $\gcd(7, 10) = 1$. Step 2: $222 = 55 \cdot 4 + 2$, so $222 \bmod 4 = 2$. Step 3: $7^2 = 49 \equiv 9 \pmod{10}$.

So the last digit of $7^{222}$ is 9.

Check: the powers of 7 mod 10 are $7, 9, 3, 1, 7, 9, 3, 1, \dots$ with period 4, and the 222nd power is in the second position of a cycle, which is 9. Python: `pow(7, 222, 10)` is 9.

</div>

<div class="example" markdown>

### Example 2: square-and-multiply for $5^{13} \bmod 23$

Since $13 = 1101_2$ (that is $8 + 4 + 1$), there are 4 rounds. Follow the steps: in each round, multiply into `result` if $e$ is odd (step 2), then square `base` and halve $e$ (step 3).

| Round | $e$ | bit | `result` before | `base` before | `result` after |
|---|---|---|---|---|---|
| 0 | 13 | 1 | 1 | 5 | 5 |
| 1 | 6 | 0 | 5 | $5^2 = 25 \equiv 2$ | 5 |
| 2 | 3 | 1 | 5 | $2^2 = 4$ | $5 \cdot 4 = 20$ |
| 3 | 1 | 1 | 20 | $4^2 = 16$ | $20 \cdot 16 = 320 \equiv 21$ |

So $5^{13} \equiv 21 \pmod{23}$, using 7 multiplications (3 into `result`, and 4 squarings, the last of which is not needed).

Check by Fermat: $5^{22} \equiv 1$, so $5^{13} \cdot 5^{9} \equiv 1$. Directly, $5^{13} = 1{,}220{,}703{,}125 = 53{,}074{,}048 \cdot 23 + 21$. Python's `pow(5, 13, 23)` is 21.

</div>

<div class="example" markdown>

### Example 3: a Carmichael number in the trace

Compute $7^{560} \bmod 561$. Here $560 = 1000110000_2$ has 10 bits, 3 of them 1. The table shows `base` before the squaring in each round, so it holds $7^{2^i} \bmod 561$.

| Round $i$ | bit $b_i$ | `base` $= 7^{2^i} \bmod 561$ | `result` after |
|---|---|---|---|
| 0 | 0 | 7 | 1 |
| 1 | 0 | 49 | 1 |
| 2 | 0 | 157 | 1 |
| 3 | 0 | 526 | 1 |
| 4 | 1 | 103 | 103 |
| 5 | 1 | 511 | $103 \cdot 511 \equiv 460$ |
| 6 | 0 | 256 | 460 |
| 7 | 0 | 460 | 460 |
| 8 | 0 | 103 | 460 |
| 9 | 1 | 511 | $460 \cdot 511 \equiv 1$ |

The answer is $7^{560} \equiv 1 \pmod{561}$, as Theorem 6 says, although 561 is composite. It took 3 multiplications into the result and 9 useful squarings (the loop does a tenth that is not needed).

Check: the base 3 shares a factor with 561, and `pow(3, 560, 561)` is 375, not 1.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Find the last two digits of $7^{2026}$, that is, $7^{2026} \bmod 100$. Start: $100 = 2^2 \cdot 5^2$, so $\varphi(100) = \varphi(4)\varphi(25) = 2 \cdot 20 = 40$. Finish: reduce the exponent mod 40, compute the small power and check.

<details class="solution" markdown>
<summary>Finish</summary>

Since $2026 = 50 \cdot 40 + 26$, we need $7^{26} \bmod 100$. Using $7^2 = 49$, $7^4 = 2401 \equiv 1 \pmod{100}$, and $26 = 4 \cdot 6 + 2$, we get $7^{26} \equiv 7^2 = 49$. The last two digits are 49.

Check: since $7^4 \equiv 1 \pmod{100}$ directly, $2026 = 4 \cdot 506 + 2$ gives $7^{2026} \equiv 7^2 = 49$ as well. Python's `pow(7, 2026, 100)` is 49.

</details>

</div>

## Edge cases and common mistakes

The mistake of reducing the exponent mod $n$ instead of mod $\varphi(n)$ is flagged above at step 2.

<div class="warning" markdown>

Watch out for using Fermat's theorem when $p \mid a$. Then $a^{p-1} \equiv 0$, not 1. The form $a^p \equiv a$ covers every integer $a$.

</div>

<div class="warning" markdown>

Watch out for reducing the exponent when $\gcd(a, n) > 1$. With $n = 8$ and $a = 2$: $2^5 \equiv 0$ but $2^{5 \bmod 4} = 2$. Euler's theorem needs the base to be a unit.

</div>

<div class="warning" markdown>

Watch out for trusting "$a^{n-1} \equiv 1$" as proof of primality. It is only evidence. A single base can be fooled (341 for base 2), and Carmichael numbers fool every coprime base.

</div>

In code, do not write `a**e % n` for large numbers: it builds the huge number $a^e$ first. Python's three-argument `pow(a, e, n)` reduces at each step. A negative exponent works too, `pow(a, -1, n)`, as the inverse. For $e = 0$ the answer is 1 (also when $a \equiv 0$), and for $n = 1$ every answer is 0.

## Tricks and shortcuts

- Find the cycle first. Mod 7 the powers of 2 are $2, 4, 1$, so $2^e$ only depends on $e \bmod 3$. The cycle length always divides $\varphi(n)$, and it can be shorter, so a cycle found by hand is the better tool.
- For a prime modulus, $a^{p-2}$ is the inverse of $a$. For example, mod 13, $5^{11} \equiv 8$ and $5 \cdot 8 = 40 = 3 \cdot 13 + 1$. This is the quickest way to code an inverse when $p$ is known to be prime.
- Use $-1$: if $a \equiv -1$, then $a^e \equiv (-1)^e$ is $\pm 1$ by the parity of $e$. For example $12^{99} \equiv (-1)^{99} = -1 \pmod{13}$.
- To square-and-multiply by hand, write $e$ in binary first, then list $a, a^2, a^4, \dots$ mod $n$ and multiply the ones that correspond to the 1 bits.
- Count bits to estimate cost: $\log_2 e$ is the number of squarings.

## In code

The first function is the loop of Theorem 5. `phi` is the product formula, and the test functions check the lesson's claims on finite ranges (evidence, not proof).

<details class="code" markdown>
<summary>In code</summary>

```python
from math import gcd

def power_mod(a, e, n):
    """Square-and-multiply. Same result as Python's pow(a, e, n)."""
    result, base = 1, a % n
    while e > 0:
        if e & 1:                       # lowest bit of e is 1
            result = result * base % n
        base = base * base % n          # base is a^(2^i) in round i
        e >>= 1                         # drop the lowest bit
    return result % n

def phi(n):
    """Euler's phi from the factorization (trial division)."""
    result, m, p = n, n, 2
    while p * p <= m:
        if m % p == 0:
            while m % p == 0:
                m //= p
            result -= result // p       # multiply by (1 - 1/p)
        p += 1
    if m > 1:
        result -= result // m
    return result

print(power_mod(5, 13, 23), pow(5, 13, 23), power_mod(7, 560, 561))   # 21 21 1
print(phi(12), phi(77), phi(360), phi(3233))                          # 4 60 96 3120
print(pow(7, 222, 10), pow(7, 2026, 100), pow(3, 1000, 7))            # 9 49 4
print(all(pow(a, phi(n), n) == 1
          for n in range(2, 300) for a in range(1, n) if gcd(a, n) == 1))   # True

def fermat_passes(n, a):
    return pow(a, n - 1, n) == 1

print(fermat_passes(91, 2), fermat_passes(341, 2), fermat_passes(341, 3))  # False True False
carmichael = [n for n in range(3, 3000)
              if any(n % d == 0 for d in range(2, n))                      # composite
              and all(pow(a, n - 1, n) == 1 for a in range(2, n) if gcd(a, n) == 1)]
print(carmichael)                                                          # [561, 1105, 1729, 2465, 2821]
print(pow(3, 10**18, 10**9 + 7))     # 246336683, computed at once from a 60-bit exponent
```

</details>

## FAQ

### Why is it called Fermat's "little" theorem?

To tell it from Fermat's last theorem, the famous claim about $x^n + y^n = z^n$. Pierre de Fermat stated the little theorem in a letter in 1640 without proof, and Euler published the first proof in 1736 and the generalization to composite moduli later.

### Does the exponent $p - 1$ have to be the smallest one that works?

No. For $p = 7$ the number 2 satisfies $2^3 \equiv 1$, so the smallest exponent is 3, a divisor of 6. The theorem gives an exponent that works for every base. The smallest one for a given base always divides it, which is why exponents can be reduced mod $p - 1$.

### Why is square-and-multiply not just a trick for small cases?

The point is the growth rate: the work is proportional to the number of bits of $e$, not to $e$ itself. A 2048-bit exponent needs about 4,000 multiplications of 2048-bit numbers, which a laptop does in a fraction of a second, whereas $e$ itself is about $10^{616}$.

### If Carmichael numbers exist, can a Fermat test be trusted at all?

Used with several random bases it still catches nearly every composite, because a Carmichael number is fooled only by bases that share a factor with it, and those are rare among large numbers. But a determined adversary can pick a Carmichael number on purpose, which is why serious libraries use the Miller-Rabin test.

## Practice

### Warm-up

1\. Compute $\varphi(20)$, $\varphi(45)$ and $\varphi(100)$ with the formula, and list the units mod 20 to check the first.

<details class="solution" markdown>
<summary>Solution</summary>

$20 = 2^2 \cdot 5$, so $\varphi(20) = 2 \cdot 4 = 8$. $45 = 3^2 \cdot 5$, so $\varphi(45) = 6 \cdot 4 = 24$. $100 = 2^2 \cdot 5^2$, so $\varphi(100) = 2 \cdot 20 = 40$.

The units mod 20 are the numbers with no factor 2 or 5: 1, 3, 7, 9, 11, 13, 17, 19, which is 8 of them.

Check: $\varphi(n) = n\prod(1 - \frac{1}{p})$ gives $20 \cdot \frac{1}{2} \cdot \frac{4}{5} = 8$ and $45 \cdot \frac{2}{3} \cdot \frac{4}{5} = 24$.

</details>

2\. Find $2^{100} \bmod 7$.

<details class="solution" markdown>
<summary>Solution</summary>

By Fermat, $2^6 \equiv 1 \pmod 7$, and $100 = 16 \cdot 6 + 4$, so $2^{100} \equiv 2^4 = 16 \equiv 2$.

Check: the powers of 2 mod 7 cycle $2, 4, 1$ with period 3, and $100 = 33 \cdot 3 + 1$, so the first position of the cycle, 2. Python agrees.

</details>

3\. Why does $5^{96} \equiv 1 \pmod{97}$ without any computation?

<details class="solution" markdown>
<summary>Solution</summary>

The number 97 is prime (no prime up to 9 divides it) and $97 \nmid 5$. Fermat's little theorem gives $5^{97 - 1} = 5^{96} \equiv 1 \pmod{97}$.

Check: `pow(5, 96, 97)` is 1.

</details>

### Standard

4\. Find the last two digits of $3^{1000}$.

<details class="solution" markdown>
<summary>Solution</summary>

Since $\gcd(3, 100) = 1$ and $\varphi(100) = 40$, and $1000 = 25 \cdot 40$, we get $3^{1000} \equiv 1 \pmod{100}$. The last two digits are 01.

Check: `pow(3, 1000, 100)` is 1.

</details>

5\. Use square-and-multiply to compute $3^{45} \bmod 1000$. Write the bits of 45 and the table of squares.

<details class="solution" markdown>
<summary>Solution</summary>

Since $45 = 101101_2 = 32 + 8 + 4 + 1$, we need $3^1, 3^4, 3^8, 3^{32}$. The repeated squares mod 1000 are $3^1 = 3$, $3^2 = 9$, $3^4 = 81$, $3^8 = 6561 \equiv 561$, $3^{16} = 561^2 = 314{,}721 \equiv 721$, $3^{32} = 721^2 = 519{,}841 \equiv 841$. Multiply the ones for the 1 bits:

$$
3 \cdot 81 = 243, \qquad 243 \cdot 561 = 136{,}323 \equiv 323, \qquad 323 \cdot 841 = 271{,}643 \equiv 643.
$$

So $3^{45} \equiv 643 \pmod{1000}$.

Check: Python's `pow(3, 45, 1000)` is 643.

</details>

6\. This one reviews [modular inverses](04-modular-inverses-and-chinese-remainder-theorem.md). Find the inverse of 5 mod 13 two ways: with Fermat's theorem and with the extended Euclidean algorithm.

<details class="solution" markdown>
<summary>Solution</summary>

By Fermat, $5^{12} \equiv 1$, so $5 \cdot 5^{11} \equiv 1$ and the inverse is $5^{11} \bmod 13$. Squaring: $5^2 = 25 \equiv 12 \equiv -1$, so $5^{10} \equiv (-1)^5 = -1$ and $5^{11} \equiv -5 \equiv 8$.

By Euclid: $13 = 2 \cdot 5 + 3$, $5 = 1 \cdot 3 + 2$, $3 = 1 \cdot 2 + 1$. Back: $1 = 3 - 2 = 3 - (5 - 3) = 2 \cdot 3 - 5 = 2(13 - 2 \cdot 5) - 5 = 2 \cdot 13 - 5 \cdot 5$. So the inverse is $-5 \equiv 8$.

Check: $5 \cdot 8 = 40 = 3 \cdot 13 + 1$. Both methods give 8.

</details>

### Challenge

7\. Prove Wilson's theorem: for a prime $p$, $(p - 1)! \equiv -1 \pmod p$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: each of $1, \dots, p-1$ has a unique inverse in the same range. What we want: the product of all of them. The plan: pair each number with its inverse, so the products of the pairs are 1, and look at which numbers are their own inverse.

*Proof.* For $p = 2$, $1! = 1 \equiv -1$. Let $p \ge 3$. A number $a$ is its own inverse when $a^2 \equiv 1$, that is $p \mid (a - 1)(a + 1)$. By Euclid's lemma, $p \mid a - 1$ or $p \mid a + 1$, so $a = 1$ or $a = p - 1$ among $1, \dots, p - 1$. Every other number in $2, \dots, p - 2$ has an inverse different from itself, also in $2, \dots, p-2$ (the inverse of $a$ is not 1 or $p-1$, since those have inverses 1 and $p - 1$). So $2, \dots, p-2$ splits into pairs $\{a, a^{-1}\}$ with product 1. Then $(p-1)! = 1 \cdot (p - 1) \cdot \prod(\text{pairs}) \equiv p - 1 \equiv -1$. $\blacksquare$

Check: $10! = 3{,}628{,}800 \equiv 10 \pmod{11}$ and $6! = 720 \equiv 6 \pmod 7$. For the composite 6, $5! = 120 \equiv 0$, not $-1$.

</details>

8\. Show that 1105 is a Carmichael number. (Hint: $1105 = 5 \cdot 13 \cdot 17$, and check that $4$, $12$ and $16$ divide $1104$.)

<details class="solution" markdown>
<summary>Solution</summary>

We have $1104 = 4 \cdot 276 = 12 \cdot 92 = 16 \cdot 69$. Let $\gcd(a, 1105) = 1$, so $a$ is not divisible by 5, 13 or 17. By Fermat, $a^4 \equiv 1 \pmod 5$, $a^{12} \equiv 1 \pmod{13}$ and $a^{16} \equiv 1 \pmod{17}$. Raising to the powers 276, 92 and 69 gives $a^{1104} \equiv 1$ modulo each of 5, 13 and 17. These are pairwise coprime with product 1105, so by the Chinese remainder theorem $a^{1104} \equiv 1 \pmod{1105}$. And 1105 is composite. $\square$

Check: Python finds no coprime base $a < 1105$ with $a^{1104} \not\equiv 1$. The same argument works for $561$ (Theorem 6): the key is that each $p - 1$ divides $n - 1$.

</details>

## Where this shows up

- The next lesson, RSA cryptography<!-- link: 06-rsa-cryptography.md -->, is Euler's theorem plus fast exponentiation: encryption and decryption are $m^e \bmod n$ and $c^d \bmod n$, and they work because $ed \equiv 1 \pmod{\varphi(n)}$.
- Hash functions, pseudorandom generators and Diffie-Hellman key exchange all compute $g^x \bmod p$ with square-and-multiply. The same repeated-squaring idea computes Fibonacci numbers through matrix powers, and the recursion `fast_pow` in the [strong induction lesson](../../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md) is this algorithm written recursively.
- The shape "work proportional to $\log e$" is the first example of an exponential speed-up from repeated halving, the same pattern as binary search in asymptotic notation<!-- link: ../04-sums-recurrences-and-algorithms/04-asymptotic-notation.md -->.
