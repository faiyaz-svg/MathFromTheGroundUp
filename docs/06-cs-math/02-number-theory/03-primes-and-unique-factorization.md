# Primes and unique factorization

After this lesson you can prove that there are infinitely many primes, prove Euclid's lemma and the fundamental theorem of arithmetic, justify why trial division and the sieve of Eratosthenes work, and say what the prime number theorem tells you about how many primes there are.

Before this: [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md) (the facts, without proofs), [GCD and Euclid's algorithm](02-gcd-and-euclids-algorithm.md) (Bezout's identity), [proof by contradiction](../../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md) and [strong induction and well-ordering](../../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Which primes do you need to test to decide whether 391 is prime?
2. A student says: "$2 \cdot 3 \cdot 5 \cdot 7 + 1 = 211$ is prime, so Euclid's proof builds a new prime each time." Is the claim true for $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1$?
3. If a prime $p$ divides $ab$, must it divide $a$ or $b$? Must the number 6 divide $a$ or $b$ if it divides $ab$?

<details class="solution" markdown>
<summary>Answers</summary>

1. Since $19^2 = 361 \le 391 < 400 = 20^2$, test the primes up to 19: 2, 3, 5, 7, 11, 13, 17 and 19. The prime 17 divides it, because $391 = 17 \cdot 23$, so 391 is composite.
2. No. The number $30{,}031 = 59 \cdot 509$ is composite. The proof only says that some prime outside the list divides it, and here there are two.
3. A prime must (this is Euclid's lemma, proved below). The number 6 need not: $6 \mid 3 \cdot 4$ but $6 \nmid 3$ and $6 \nmid 4$.

</details>

## The idea

The [factors lesson](../../01-elementary/08-factors-multiples-and-primes.md) says that every whole number above 1 is a product of primes, in only one way. That is easy to believe after factoring a few numbers, and it is false in some number systems that look very much like the integers. In the numbers $a + b\sqrt{-5}$ with $a$ and $b$ integers, $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$, and none of the four factors can be split further. So uniqueness is a theorem about the integers, and it needs a proof.

The proof has a single key ingredient: if a prime divides a product, it divides one of the factors. That sounds like part of the definition of a prime, but the definition says something else (a prime has no divisors but 1 and itself). Bezout's identity from the last lesson is the bridge between the two statements.

Once uniqueness is in place, a number is completely described by the list of exponents of its primes, and divisibility, gcd and lcm become comparisons of lists. The cost is that finding the list is hard. Trial division works for small numbers, a sieve finds all the primes up to a limit, and for numbers with hundreds of digits nothing known works in reasonable time. That gap is where cryptography begins.

## Definitions

An integer $p$ is **prime** if $p > 1$ and the only positive divisors of $p$ are 1 and $p$. An integer $n > 1$ that is not prime is **composite**. In plain words, a composite number splits into a product $n = ab$ with $1 < a, b < n$. The numbers 0 and 1 are neither.

A **prime factorization** of $n > 1$ is a way of writing $n = p_1 p_2 \cdots p_r$ with each $p_i$ prime (repeats allowed; $r = 1$ is allowed). Two factorizations are the **same** if they differ only in the order of the factors. The **standard form** lists the distinct primes in increasing order with exponents:

$$
n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}, \qquad p_1 < p_2 < \dots < p_k,\quad e_i \ge 1.
$$

For example $360 = 2^3 \cdot 3^2 \cdot 5$. The **exponent** $e_i$ says how many times $p_i$ appears.

The prime-counting function $\pi(x)$ is the number of primes that are at most $x$. For example $\pi(10) = 4$ (the primes 2, 3, 5, 7) and $\pi(100) = 25$.

## How to do it

### Every number has a prime divisor

*Theorem 1.* Every integer $n > 1$ has a prime divisor.

What we know: well-ordering. What we want: a prime that divides $n$. The plan: take the smallest divisor of $n$ that is bigger than 1, and show it is prime.

*Proof.* The set of divisors of $n$ that are greater than 1 is nonempty, since it contains $n$. Let $d$ be its least element. If $d$ were not prime, it would have a divisor $e$ with $1 < e < d$, and then $e \mid d$ and $d \mid n$ give $e \mid n$ by transitivity, contradicting the choice of $d$. So $d$ is prime. $\blacksquare$

### There are infinitely many primes

*Theorem 2 (Euclid).* There are infinitely many primes.

What we know: Theorem 1. What we want: no finite list holds all the primes. The plan is a [proof by contradiction](../../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md): given any finite list of primes, build a number that has a prime divisor not on the list.

*Proof.* Suppose the primes were $p_1, p_2, \dots, p_k$, a complete finite list. Let $N = p_1 p_2 \cdots p_k + 1$. Since $N > 1$, Theorem 1 gives a prime $q$ with $q \mid N$. By assumption $q = p_i$ for some $i$. Then $q$ divides $p_1 \cdots p_k$ and $q$ divides $N$, so $q$ divides their difference $N - p_1 \cdots p_k = 1$. But a prime is bigger than 1 and can't divide 1. This contradiction shows that no finite list contains every prime. $\blacksquare$

Look back: the proof does not say that $N$ is prime, only that a prime outside the list divides it. For the list 2, 3, 5, 7, 11, 13 we get $N = 30{,}031 = 59 \cdot 509$. Both factors are new primes.

### Euclid's lemma

*Theorem 3 (Euclid's lemma).* Let $p$ be a prime and $a$, $b$ integers. If $p \mid ab$, then $p \mid a$ or $p \mid b$.

What we know: Bezout's identity (Theorem 6 of the last lesson) and the coprime lemma. What we want: $p$ divides at least one factor. The plan: if $p$ does not divide $a$, then $p$ and $a$ are coprime, so the coprime lemma finishes it.

*Proof.* Suppose $p \mid ab$ and $p \nmid a$. The only positive divisors of $p$ are 1 and $p$, and $p$ does not divide $a$, so $\gcd(p, a) = 1$. Bezout gives integers $x$ and $y$ with $px + ay = 1$. Multiply by $b$: $b = pbx + aby$. The prime $p$ divides $pbx$, and it divides $aby = y(ab)$ because $p \mid ab$. So $p$ divides the sum $b$. $\blacksquare$

Look back: this is Lemma 8 of the last lesson with $a = p$ in the role of the divisor. Primality was used exactly once, to turn "$p \nmid a$" into "$\gcd(p, a) = 1$". For 6 the step fails: $6 \nmid 3$, but $\gcd(6, 3) = 3 \ne 1$.

*Corollary 4.* If a prime $p$ divides a product $a_1 a_2 \cdots a_k$, then $p$ divides some $a_i$. In particular, if $p$ divides a product of primes $q_1 \cdots q_k$, then $p = q_j$ for some $j$.

*Proof.* Induction on $k$. For $k = 1$ there is nothing to prove. If $p \mid (a_1 \cdots a_{k-1}) \cdot a_k$, then Theorem 3 gives $p \mid a_1 \cdots a_{k-1}$, to which the hypothesis applies, or $p \mid a_k$. For the second sentence, $p \mid q_j$ for some $j$, and the only divisor of the prime $q_j$ that exceeds 1 is $q_j$ itself, so $p = q_j$. $\blacksquare$

### The fundamental theorem of arithmetic

*Theorem 5 (fundamental theorem of arithmetic).* Every integer $n > 1$ can be written as a product of primes, and the factorization is unique apart from the order of the factors.

We prove existence and uniqueness separately.

*Existence.* The proof is the one in the [strong induction lesson](../../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md), repeated here in short. Suppose every integer $j$ with $2 \le j \le k$ is a product of primes, and consider $k + 1$. If it is prime, it is a product of one prime. Otherwise $k + 1 = ab$ with $2 \le a, b \le k$, and both $a$ and $b$ are products of primes by the hypothesis, so their product is too. The base case $n = 2$ is prime. $\blacksquare$

*Uniqueness.* What we know: Corollary 4. What we want: if $p_1 \cdots p_r = q_1 \cdots q_s$ with every $p_i$ and $q_j$ prime, then $r = s$ and the $q$'s are the $p$'s in some order. The plan: induction on $r$. Take the last $p$, use Corollary 4 to find the $q$ that equals it, cancel both, and apply the hypothesis to what is left.

*Proof.* For $r = 1$: $p_1 = q_1 \cdots q_s$. Then $q_1$ divides the prime $p_1$ and exceeds 1, so $q_1 = p_1$. If $s \ge 2$, cancelling gives $1 = q_2 \cdots q_s$, impossible since each $q_j \ge 2$. So $s = 1$ and the two factorizations are the same.

Now let $r \ge 2$ and suppose uniqueness holds for products of $r - 1$ primes. Given $p_1 \cdots p_r = q_1 \cdots q_s$, the prime $p_r$ divides the right side, so by Corollary 4 $p_r = q_j$ for some $j$. Reorder the $q$'s so that $j = s$. Cancelling $p_r = q_s$ from both sides gives $p_1 \cdots p_{r-1} = q_1 \cdots q_{s-1}$. The left side is at least 2, so the right side is not an empty product, and $s - 1 \ge 1$. By the hypothesis $r - 1 = s - 1$ and the $q_1, \dots, q_{s-1}$ are the $p_1, \dots, p_{r-1}$ in some order. So $r = s$ and the two factorizations agree. $\blacksquare$

Look back: all the work in uniqueness is done by Euclid's lemma. In the numbers $a + b\sqrt{-5}$ from the start of the lesson, the factors 2 and 3 can't be split further but don't satisfy Euclid's lemma ($2 \mid (1 + \sqrt{-5})(1 - \sqrt{-5}) = 6$, yet 2 divides neither factor), and uniqueness fails with them.

In plain words, a number is the same thing as its list of prime exponents. Multiplying numbers adds the exponent lists, and $a \mid b$ exactly when every exponent of $a$ is at most the matching exponent of $b$. That is why the factors lesson's rule works: $\gcd$ takes the smaller exponent of each prime and lcm takes the larger, with an exponent of 0 for a prime that is missing. The number of positive divisors of $p_1^{e_1} \cdots p_k^{e_k}$ is $(e_1 + 1)(e_2 + 1) \cdots (e_k + 1)$, since each divisor picks an exponent from $0$ to $e_i$ independently. For $360 = 2^3 \cdot 3^2 \cdot 5$ that is $4 \cdot 3 \cdot 2 = 24$.

### Trial division

To test whether $n$ is prime, you only need to look at divisors up to $\sqrt{n}$.

*Theorem 6.* If $n > 1$ is composite, then $n$ has a prime divisor $p$ with $p \le \sqrt{n}$.

What we know: $n = ab$ with $1 < a \le b < n$, and Theorem 1. What we want: a small prime divisor. The plan: the smaller factor is at most $\sqrt{n}$, and any prime divisor of it divides $n$.

*Proof.* Write $n = ab$ with $1 < a \le b$. Then $a^2 \le ab = n$, so $a \le \sqrt{n}$. By Theorem 1, $a$ has a prime divisor $p$, and $p \le a \le \sqrt{n}$ by [Theorem 1(c)](01-divisibility-and-modular-arithmetic.md). Since $p \mid a$ and $a \mid n$, we have $p \mid n$. $\blacksquare$

So to test $n$:

1. Compute $m = \lfloor \sqrt{n} \rfloor$.
2. For each prime $p \le m$ (or, simpler, for each $d = 2, 3, \dots, m$), check whether $p \mid n$.
3. If one divides, $n$ is composite, and that divisor starts a factorization. If none does, $n$ is prime.
4. To factor $n$ fully, divide out each prime found and repeat on the quotient, stopping at the square root of the quotient.

The cost is at most $\sqrt{n}$ divisions. For a 64-bit number that is up to $2^{32} \approx 4.3 \times 10^9$, which takes seconds. For a 1024-bit number it is $2^{512}$, far beyond any computer. Trial division is an exponential-time algorithm in the number of digits, whereas Euclid's algorithm is linear in the number of digits.

### The sieve of Eratosthenes

To list all primes up to $n$, a sieve avoids testing each number separately.

1. Write the numbers $2, 3, \dots, n$ and mark them all as possibly prime.
2. Take the smallest number $p$ not crossed out. It is prime.
3. Cross out $p^2, p^2 + p, p^2 + 2p, \dots$ up to $n$.
4. Repeat steps 2 and 3. Stop when $p^2 > n$. The numbers not crossed out are the primes up to $n$.

*Theorem 7.* The sieve crosses out exactly the composite numbers up to $n$.

*Proof.* Every crossed-out number is a multiple $mp$ of a prime $p$ with $m \ge p$, so it is composite. Conversely, let $c \le n$ be composite and let $p$ be its smallest prime divisor. Write $c = pm$ with $m > 1$. Every prime divisor of $m$ also divides $c$, so it is at least $p$, and therefore $m \ge p$. Then $p^2 \le pm = c \le n$, so $p \le \sqrt{n}$. A prime is never crossed out, so the sieve does reach $p$ and processes it, and $c = pm$ is among the multiples it crosses out, since $c \ge p^2$. $\blacksquare$

The sieve starts at $p^2$ in step 3 because the smaller multiples, $2p, 3p, \dots, (p-1)p$, each have a smaller prime factor and are already gone. For $n = 50$ the stopping rule means the primes 2, 3, 5 and 7:

| Prime $p$ | New numbers crossed out | Count |
|---|---|---|
| 2 | 4, 6, 8, ..., 50 | 24 |
| 3 | 9, 15, 21, 27, 33, 39, 45 | 7 |
| 5 | 25, 35 | 2 |
| 7 | 49 | 1 |

There are 49 numbers from 2 to 50 and $24 + 7 + 2 + 1 = 34$ are crossed out, leaving 15: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43 and 47. The sieve takes about $n \log \log n$ steps, which is nearly linear, and it needs memory for $n$ flags. It lists every prime to $10^7$ in a fraction of a second, but it can't test one huge number.

### How many primes are there?

Theorem 2 says $\pi(x)$ grows without bound. The **prime number theorem** says how fast. It states, without proof here, that

$$
\pi(x) \approx \frac{x}{\ln x} \quad\text{for large } x,
$$

in the sense that the ratio of the two sides gets closer to 1. It was proved independently by Hadamard and de la Vallée Poussin in 1896, and the proof uses complex analysis. Computed values show the pattern:

| $x$ | $\pi(x)$ | $x / \ln x$ (rounded) | ratio |
|---|---|---|---|
| $10^3$ | 168 | 145 | 1.16 |
| $10^4$ | 1,229 | 1,086 | 1.13 |
| $10^5$ | 9,592 | 8,686 | 1.10 |
| $10^6$ | 78,498 | 72,382 | 1.08 |
| $10^7$ | 664,579 | 620,421 | 1.07 |

In plain words, a random number near $x$ is prime with probability about $\frac{1}{\ln x}$. For a 1024-bit number that is about $\frac{1}{710}$, or about $\frac{1}{355}$ if you only try odd numbers. That is why RSA<!-- link: 06-rsa-cryptography.md --> can find a large prime by picking random odd numbers and testing each one: it expects to try a few hundred.

## Worked examples

<div class="example" markdown>

### Example 1: factoring 123,456 by trial division

Step 1: $\lfloor \sqrt{123456} \rfloor = 351$, so divisors up to 351 may be needed. Step 2: divide by 2 as often as possible. We get $123456 = 2 \cdot 61728 = 2^2 \cdot 30864 = 2^3 \cdot 15432 = 2^4 \cdot 7716 = 2^5 \cdot 3858 = 2^6 \cdot 1929$, and 1929 is odd.

Step 3: try 3. The digit sum of 1929 is 21, so $3 \mid 1929$, and $1929 = 3 \cdot 643$. Now the number left is 643, and by step 4 we stop at $\lfloor \sqrt{643} \rfloor = 25$. The primes up to 25 are 2, 3, 5, 7, 11, 13, 17, 19 and 23, and none divides 643 (the remainders are 1, 1, 3, 6, 5, 6, 14, 16 and 22 respectively). So 643 is prime.

Result: $123456 = 2^6 \cdot 3 \cdot 643$. By uniqueness, this is the only factorization.

Check: $64 \cdot 3 = 192$ and $192 \cdot 643 = 123{,}456$. The number of divisors is $(6 + 1)(1 + 1)(1 + 1) = 28$.

</div>

<div class="example" markdown>

### Example 2: using Euclid's lemma

Show that if a prime $p$ divides $a^2$, then $p \mid a$. Then explain why $\sqrt{2}$ cannot be a fraction.

By Euclid's lemma with $b = a$, $p \mid a \cdot a$ gives $p \mid a$ or $p \mid a$, so $p \mid a$.

Suppose $\sqrt{2} = \frac{m}{n}$ in lowest terms, so $m^2 = 2n^2$. Then $2 \mid m^2$, so $2 \mid m$ by what we just showed. Write $m = 2k$: $4k^2 = 2n^2$ and $n^2 = 2k^2$, so $2 \mid n$ too. Then 2 divides both $m$ and $n$, contradicting lowest terms.

Check: the contradiction rests on Euclid's lemma. For the non-prime 4, "$4 \mid m^2$ implies $4 \mid m$" is false: $4 \mid 6^2 = 36$ but $4 \nmid 6$.

</div>

<div class="example" markdown>

### Example 3: the sieve up to 30

Write 2 to 30. Take 2, a prime, and cross out 4, 6, 8, ..., 30. The next number left is 3, so cross out 9, 15, 21, 27 (the other multiples, 6, 12, 18, 24 and 30, are gone). The next is 5, and $5^2 = 25$, so cross out 25. The next is 7, and $7^2 = 49 > 30$, so stop.

The survivors are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.

Check: $\pi(30) = 10$, and the only composites up to 30 whose smallest prime factor is above $\sqrt{30} \approx 5.5$ would be products of two primes at least 7, which are at least 49.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Is 487 prime? The first step is done: $22^2 = 484 \le 487 < 529 = 23^2$, so only primes up to 22 need testing, namely 2, 3, 5, 7, 11, 13, 17 and 19. Test 2, 3 and 5 by the digit rules, then test 7, 11, 13, 17 and 19 by division, and decide.

<details class="solution" markdown>
<summary>Finish</summary>

The number is odd, its digit sum is 19 (not a multiple of 3), and it does not end in 0 or 5. Division: $487 = 69 \cdot 7 + 4$, $487 = 44 \cdot 11 + 3$, $487 = 37 \cdot 13 + 6$, $487 = 28 \cdot 17 + 11$ and $487 = 25 \cdot 19 + 12$. No prime up to 22 divides 487, so by Theorem 6 it is prime.

Check: Python's `sympy.isprime(487)` is True, and `factor(487)` from the code section returns `[487]`.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for taking the stopping point too early. For $n = 49$, $\sqrt{49} = 7$ exactly, and $7 \cdot 7 = 49$. A test that stops at primes below 7 misses it. The rule is $p \le \sqrt{n}$, with equality allowed.

</div>

<div class="warning" markdown>

Watch out for assuming that Euclid's proof builds primes. The number $p_1 \cdots p_k + 1$ is not always prime (30,031 is not). The proof shows that some prime outside the list divides it, not that it is the next prime or that it is prime itself.

</div>

<div class="warning" markdown>

Watch out for using Euclid's lemma on a composite number. From $6 \mid 3 \cdot 4$ you can't conclude $6 \mid 3$ or $6 \mid 4$. The lemma needs $p$ to be prime. The same goes for the cancellation shortcut "$p \mid ab$, so $p \mid a$ or $p \mid b$" in a proof: check the first word of the sentence.

</div>

The number 1 is not prime, and that is not a convention of taste: if 1 were prime, then $6 = 2 \cdot 3 = 1 \cdot 2 \cdot 3 = 1 \cdot 1 \cdot 2 \cdot 3$ would be different factorizations and uniqueness would be false. The number 2 is prime, and it is the only even prime. A prime factorization of $n = 1$ is the empty product, and this is why products of zero primes equal 1.

## Tricks and shortcuts

- After testing 2 and 3, a prime must be of the form $6k \pm 1$ (Practice 6), so trial division can skip multiples of 2 and 3 and test only 5, 7, 11, 13, 17, 19, 23, ... That removes two thirds of the divisions.
- A number whose digit sum is a multiple of 3, or that ends in an even digit or in 5, is quickly ruled out. These are the [divisibility rules](../../01-elementary/06-division-facts-and-remainders.md#divisibility-rules), now proved by the congruence rules of divisibility and modular arithmetic<!-- link: 01-divisibility-and-modular-arithmetic.md -->.
- To check that two numbers are coprime you do not need their factorizations: use Euclid's algorithm. To factor, you do.
- To estimate how many primes a range holds, use $\frac{1}{\ln x}$ per number. Between $10^6$ and $2 \times 10^6$ the estimate is about $10^6 / \ln(1.5 \times 10^6) \approx 70{,}000$; the true count is 70,435.

## In code

The code is trial division, the sieve, and the checks of this lesson on finite ranges (evidence, not proof).

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def factor(n):
    """Trial division: the prime factors of n > 1 in increasing order."""
    out, d = [], 2
    while d * d <= n:             # stop when d exceeds the square root of what is left
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)             # what is left is prime
    return out

def primes_up_to(n):
    """Sieve of Eratosthenes."""
    flags = [True] * (n + 1)
    flags[0:2] = [False, False]
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            for m in range(p * p, n + 1, p):
                flags[m] = False
    return [k for k in range(n + 1) if flags[k]]

print(factor(123456), factor(9991), factor(30031))   # [2, 2, 2, 2, 2, 2, 3, 643] [97, 103] [59, 509]
print(primes_up_to(50))        # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ps = primes_up_to(10**6)
print(len(ps), round(10**6 / math.log(10**6)))       # 78498 72382
print(all(p % 6 in (1, 5) for p in ps if p > 3))     # True
print(math.prod(factor(123456)) == 123456)           # True
```

</details>

## FAQ

### Why is 1 not a prime, when it has no divisors other than 1 and itself?

Because it would break uniqueness: every factorization could carry any number of extra 1s. The definition "bigger than 1 with only two positive divisors" is chosen so that the fundamental theorem is true as stated. Nothing is lost, since multiplying by 1 changes nothing.

### Isn't "a prime divides a product only if it divides a factor" just the definition of prime?

It is a different property. The definition says a prime has no divisors but 1 and itself. Euclid's lemma says it can't hide inside a product. In the integers the two are equivalent, and proving it takes Bezout's identity. In other number systems they come apart, as in the $\sqrt{-5}$ example, and the second property is the one that makes unique factorization work (it is the definition of a prime element in abstract algebra).

### If factoring is so hard, why is testing for primality easy?

Because primality can be certified without finding a factor, using facts like Fermat's little theorem<!-- link: 05-fermat-euler-and-fast-exponentiation.md -->. There are fast randomized primality tests, and in 2002 Agrawal, Kayal and Saxena gave a deterministic polynomial-time test. For factoring, no polynomial-time algorithm is known for an ordinary computer.

### Do the primes follow any pattern?

They are very regular on average, as the prime number theorem shows, and very irregular up close. Gaps between consecutive primes can be as small as 2 (the pairs 11 and 13, 17 and 19) or as large as you like. Whether there are infinitely many pairs 2 apart (twin primes) is an open problem.

## Practice

### Warm-up

1\. Decide whether each number is prime, and say which primes you tested: 221, 391, 487.

<details class="solution" markdown>
<summary>Solution</summary>

For 221, $14^2 = 196 \le 221 < 225 = 15^2$, so test 2, 3, 5, 7, 11 and 13. The prime 13 divides it: $221 = 13 \cdot 17$. Composite.

For 391, test the primes up to 19. We have $391 = 17 \cdot 23$, so it is composite (2, 3, 5, 7, 11 and 13 fail first).

For 487, test the primes up to 22; none divides it (Example 4), so it is prime.

Check: $13 \cdot 17 = 221$, $17 \cdot 23 = 391$, and `sympy.isprime(487)` is True.

</details>

2\. Use the sieve to list the primes up to 60. Which primes did you use to cross out numbers?

<details class="solution" markdown>
<summary>Solution</summary>

Since $7^2 = 49 \le 60 < 121 = 11^2$, the sieve uses 2, 3, 5 and 7. It crosses out the multiples of 2; then 9, 15, 21, 27, 33, 39, 45, 51, 57; then 25, 35, 55; then 49.

The survivors are 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 and 59.

Check: there are 17 of them, and $\pi(60) = 17$ (the 15 primes below 50 plus 53 and 59).

</details>

3\. Write 360 and 2,520 in standard form. Use the exponents to find their GCD and LCM.

<details class="solution" markdown>
<summary>Solution</summary>

$360 = 2^3 \cdot 3^2 \cdot 5$ and $2520 = 2^3 \cdot 3^2 \cdot 5 \cdot 7$. The GCD takes the smaller exponent of each prime: $2^3 \cdot 3^2 \cdot 5 \cdot 7^0 = 360$. The LCM takes the larger: $2^3 \cdot 3^2 \cdot 5 \cdot 7 = 2520$.

Check: $360 \mid 2520$ since $2520 = 7 \cdot 360$, so the GCD is the smaller number and the LCM is the larger.

</details>

### Standard

4\. Factor 9,991 by trial division. Which primes do you test, and where do you stop?

<details class="solution" markdown>
<summary>Solution</summary>

Since $99^2 = 9801 \le 9991 < 10000 = 100^2$, we would test primes up to 97. Testing in order, none of 2, 3, 5, 7, 11, ..., 89 divides it, but $9991 = 97 \cdot 103$. As $97 \cdot 103 = (100 - 3)(100 + 3) = 10000 - 9$, this can also be seen as a difference of squares. Both factors are prime: 97 is prime, and 103 is prime since $10^2 = 100 \le 103 < 121$ and none of 2, 3, 5, 7 divides it.

Check: $97 \cdot 103 = 9991$.

</details>

5\. Prove that a positive integer is a perfect square if and only if every exponent in its standard form is even. Use it to decide whether 360 and 7,056 are squares.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: uniqueness of factorization. What we want: both directions. The plan: square a factorization for one direction, and compare factorizations for the other.

*Proof.* If $n = m^2$ and $m = p_1^{f_1} \cdots p_k^{f_k}$, then $n = p_1^{2f_1} \cdots p_k^{2f_k}$, which has even exponents. Conversely, if $n = p_1^{2g_1} \cdots p_k^{2g_k}$, then $n = (p_1^{g_1} \cdots p_k^{g_k})^2$. By uniqueness, the exponents of $n$ don't depend on how we found its factorization, so the statement "all even" is well defined for $n$. $\blacksquare$

Now $360 = 2^3 \cdot 3^2 \cdot 5$ has odd exponents 3 and 1, so it is not a square. And $7056 = 2^4 \cdot 3^2 \cdot 7^2$ has even exponents, so it is a square: $7056 = 84^2$.

Check: $19^2 = 361 \ne 360$, and $84 \cdot 84 = 7056$.

</details>

6\. This one reviews [divisibility and modular arithmetic](01-divisibility-and-modular-arithmetic.md). Prove that every prime $p > 3$ satisfies $p \equiv 1$ or $p \equiv 5 \pmod 6$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $p \bmod 6$ is one of 0, 1, 2, 3, 4, 5. What we want: it is 1 or 5. The plan: rule out the other four by showing they give a divisor of $p$ other than 1 and $p$.

*Proof.* If $p \equiv 0, 2$ or $4 \pmod 6$, then $p$ is even, so $2 \mid p$, which is impossible for a prime above 3 (a prime with $2 \mid p$ equals 2). If $p \equiv 3 \pmod 6$, then $p = 6k + 3 = 3(2k + 1)$, so $3 \mid p$, which is impossible for a prime above 3. That leaves 1 and 5. $\blacksquare$

Check: 5, 7, 11, 13, 17, 19, 23 leave remainders 5, 1, 5, 1, 5, 1, 5 mod 6. The converse is false: $25 \equiv 1$ and is not prime.

</details>

### Challenge

7\. Prove that there are infinitely many primes of the form $4k + 3$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Theorem 1, and that a product of numbers $\equiv 1 \pmod 4$ is $\equiv 1 \pmod 4$ (Theorem 6 of the last lesson). What we want: no finite list of primes $\equiv 3 \pmod 4$ is complete. The plan: copy Euclid's proof with a number that is $\equiv 3$.

*Proof.* Suppose $p_1, \dots, p_k$ were all the primes $\equiv 3 \pmod 4$. Let $N = 4 p_1 \cdots p_k - 1$. Then $N \equiv -1 \equiv 3 \pmod 4$, and $N$ is odd. Write $N$ as a product of primes (Theorem 5). All of them are odd, so each is $\equiv 1$ or $\equiv 3 \pmod 4$. If all were $\equiv 1$, their product would be $\equiv 1$, not 3. So some prime factor $q$ of $N$ is $\equiv 3 \pmod 4$, which means $q = p_i$ for some $i$. Then $q$ divides $4p_1 \cdots p_k$ and $N$, so $q$ divides the difference, which is 1. This contradiction proves the claim. $\blacksquare$

Check: with the list $\{3\}$, $N = 4 \cdot 3 - 1 = 11$, a new prime $\equiv 3$. With $\{3, 7\}$, $N = 83$, again a new prime $\equiv 3 \pmod 4$.

</details>

8\. In the set $E = \{2, 4, 6, 8, \dots\}$ of positive even numbers, call a number "even-prime" if it is not the product of two numbers in $E$. Show that 2, 6, 10 and 30 are even-prime, and that $60 = 6 \cdot 10 = 2 \cdot 30$ is two different factorizations into even-primes. What does this say about the proof of the fundamental theorem?

<details class="solution" markdown>
<summary>Solution</summary>

A product of two numbers in $E$ is a multiple of 4. The numbers 2, 6, 10 and 30 are not multiples of 4 (each is $\equiv 2 \pmod 4$), so none is a product of two members of $E$, and each is even-prime. Then $6 \cdot 10 = 60 = 2 \cdot 30$, and the two lists $\{6, 10\}$ and $\{2, 30\}$ are different.

So existence of factorization holds in $E$ (the existence proof only splits numbers into smaller ones), but uniqueness fails. Uniqueness needs more than "can't be split further": it needs Euclid's lemma, the statement that an unsplittable number dividing a product divides a factor. Here 6 divides $2 \cdot 30 = 60$ (as $60 = 6 \cdot 10$ and $10 \in E$), yet 6 does not divide 2 or 30 inside $E$, because $30 / 6 = 5$ is not in $E$. The proof for the integers works because Bezout's identity gives the lemma there.

Check: $6 \cdot 10 = 60$ and $2 \cdot 30 = 60$.

</details>

## Where this shows up

- The next lesson, modular inverses and the Chinese remainder theorem<!-- link: 04-modular-inverses-and-chinese-remainder-theorem.md -->, uses coprimality and the prime factorization of the modulus, and Euler's phi function in Fermat, Euler and fast exponentiation<!-- link: 05-fermat-euler-and-fast-exponentiation.md --> is computed from the factorization.
- RSA cryptography<!-- link: 06-rsa-cryptography.md --> rests on the gap between the two halves of this lesson: finding large primes is easy (the density from the prime number theorem and fast primality tests), while recovering the two primes from their product is not known to be.
- Hash table sizes are often chosen prime so that `key % size` spreads keys evenly, and prime factorization shows up in counting divisors and in the counting lessons<!-- link: ../03-counting-and-discrete-probability/01-counting-rules.md -->.
