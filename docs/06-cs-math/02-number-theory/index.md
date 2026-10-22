# Number theory

Divisibility, remainders and primes, and the chain of results that leads from Euclid's algorithm to RSA encryption.

1. [Divisibility and modular arithmetic](01-divisibility-and-modular-arithmetic.md)
2. [GCD and Euclid's algorithm](02-gcd-and-euclids-algorithm.md)
3. [Primes and unique factorization](03-primes-and-unique-factorization.md)
4. [Modular inverses and the Chinese remainder theorem](04-modular-inverses-and-chinese-remainder-theorem.md)
5. [Fermat, Euler and fast exponentiation](05-fermat-euler-and-fast-exponentiation.md)
6. [RSA cryptography](06-rsa-cryptography.md)

## Cheat sheet

### Divisibility and modular arithmetic

The statement $a \mid b$ means $b = ak$ for some integer $k$. The division algorithm: for $d > 0$ there are unique $q, r$ with $n = qd + r$ and $0 \le r < d$, and $n \bmod d = r$. Congruence $a \equiv b \pmod n$ means $n \mid a - b$, which holds exactly when $a$ and $b$ leave the same remainder.

| Fact | Statement |
|---|---|
| Divides is transitive | $a \mid b$ and $b \mid c$ give $a \mid c$ |
| Linear combinations | $a \mid b$ and $a \mid c$ give $a \mid bx + cy$ |
| Size | $a \mid b$ and $b \ne 0$ give $\lvert a \rvert \le \lvert b \rvert$ |
| Arithmetic | $a \equiv b$, $c \equiv d$ give $a \pm c \equiv b \pm d$ and $ac \equiv bd$ |
| Powers | $a \equiv b$ gives $a^k \equiv b^k$ for $k \ge 0$ |
| Digits | $n \equiv$ digit sum mod 9 (and mod 3); alternating digit sum mod 11 |

- Reduce before you compute, and use $\pm 1$ when you can: $6 \equiv -1 \pmod 7$.
- Python's `%` gives a result with the sign of the divisor, so `-17 % 5` is 3. C, C++, Java, JavaScript and Rust truncate, so `-17 % 5` is $-2$.
- Check digits: ISBN-10 needs $10d_1 + 9d_2 + \dots + 1 \cdot d_{10} \equiv 0 \pmod{11}$. Luhn doubles every second digit from the right (subtract 9 if above 9) and needs a total $\equiv 0 \pmod{10}$.

Main mistakes:

- Writing $17 \bmod 5 = 7$. The operator gives a number from 0 to 4; the relation $17 \equiv 7 \pmod 5$ is true.
- Cancelling a common factor: $6 \cdot 2 \equiv 6 \cdot 4 \pmod{12}$ but $2 \not\equiv 4$.
- Reducing the exponent mod $n$ in $a^e \bmod n$.
- Trusting a negative `%` result in a hash table index.

### GCD and Euclid's algorithm

$\gcd(a, b)$ is the largest common divisor, $\gcd(a, 0) = \lvert a \rvert$, and $\gcd(a, b) = \gcd(b, a \bmod b)$. Repeat the division until the remainder is 0; the last nonzero remainder is the GCD.

| Step | $a$ | $b$ | $q$ | $r$ |
|---|---|---|---|---|
| 1 | 1071 | 462 | 2 | 147 |
| 2 | 462 | 147 | 3 | 21 |
| 3 | 147 | 21 | 7 | 0 |

- The algorithm makes at most $2\log_2 b + 2$ divisions (every two steps halve the remainder). Consecutive Fibonacci numbers are the worst case (Lamé).
- Bezout: $ax + by = \gcd(a, b)$ for some integers $x, y$. The extended algorithm finds them by back-substitution or with a table. For 1071 and 462: $21 = (-3)(1071) + 7 \cdot 462$.
- Consequences: $\gcd(a, b) = 1$ exactly when $ax + by = 1$ is solvable; if $\gcd(a, b) = 1$ and $a \mid bc$ then $a \mid c$.
- $\operatorname{lcm}(a, b) = \frac{a}{\gcd(a, b)} \cdot b$.

Main mistakes:

- Answering 0 instead of the last nonzero remainder.
- Treating Bezout's $x$ and $y$ as unique; they can be shifted by $\frac{b}{g}$ and $\frac{a}{g}$.
- Expecting $ax + by = c$ to be solvable for every $c$; it is solvable exactly when $\gcd(a, b) \mid c$.

### Primes and unique factorization

A prime is an integer above 1 with no positive divisors except 1 and itself.

- Every $n > 1$ has a prime divisor, and there are infinitely many primes (Euclid: $p_1 \cdots p_k + 1$ has a prime divisor outside the list).
- Euclid's lemma: if a prime $p \mid ab$, then $p \mid a$ or $p \mid b$. It fails for composite moduli: $6 \mid 3 \cdot 4$.
- Fundamental theorem of arithmetic: every $n > 1$ is a product of primes in exactly one way up to order. Existence by strong induction, uniqueness by Euclid's lemma.
- Exponent lists: GCD takes the smaller exponent, lcm the larger, and the number of divisors of $p_1^{e_1} \cdots p_k^{e_k}$ is $(e_1 + 1) \cdots (e_k + 1)$.
- Trial division: a composite $n$ has a prime divisor $p \le \sqrt{n}$, so test primes up to $\sqrt{n}$ (equality allowed).
- Sieve of Eratosthenes: cross out multiples of each prime $p$ starting at $p^2$, stop when $p^2 > n$. For $n = 50$ it leaves 15 primes.
- Prime number theorem: $\pi(x) \approx \frac{x}{\ln x}$, so a random number near $x$ is prime with probability about $\frac{1}{\ln x}$. About 1 in 710 numbers near $2^{1024}$.

Main mistakes:

- Calling 1 prime, or stopping trial division before $\sqrt{n}$.
- Thinking $p_1 \cdots p_k + 1$ is always prime (it is $30{,}031 = 59 \cdot 509$ for the first six primes).
- Applying Euclid's lemma to a modulus that is not prime.

### Modular inverses and the Chinese remainder theorem

An inverse of $a$ mod $n$ is $b$ with $ab \equiv 1$. It exists exactly when $\gcd(a, n) = 1$, and it is unique mod $n$. Find it with the extended Euclidean algorithm or `pow(a, -1, n)`. Mod 40, the inverse of 7 is 23.

- Cancellation: if $\gcd(c, n) = 1$ and $cb \equiv cb'$, then $b \equiv b'$. Modulo a prime, every nonzero residue has an inverse.
- Linear congruence $ax \equiv b \pmod n$ with $g = \gcd(a, n)$: no solution if $g \nmid b$; otherwise exactly $g$ solutions mod $n$, namely $x_0 + k\frac{n}{g}$ where $x_0$ solves $\frac{a}{g}x \equiv \frac{b}{g} \pmod{\frac{n}{g}}$.
- Chinese remainder theorem: for pairwise coprime $m_i$ with product $M$, the system $x \equiv a_i \pmod{m_i}$ has a solution, unique mod $M$: $x = \sum a_i M_i y_i$ with $M_i = M/m_i$ and $y_i = M_i^{-1} \bmod m_i$.
- Two congruences: $x = a_1 + m_1 t$ with $t \equiv (a_2 - a_1)\,m_1^{-1} \pmod{m_2}$. Example: $x \equiv 2, 3, 2$ mod $3, 5, 7$ gives $x \equiv 23 \pmod{105}$.

Main mistakes:

- Dividing in $\mathbb{Z}_n$ as if every number had a reciprocal.
- Using the Chinese remainder theorem when the moduli share a factor.
- Stating one solution of $ax \equiv b$ when there are $g$ of them.

### Fermat, Euler and fast exponentiation

- Fermat: for a prime $p$ and $p \nmid a$, $a^{p-1} \equiv 1 \pmod p$; for every $a$, $a^p \equiv a$. Proof: $a, 2a, \dots, (p-1)a$ is $1, \dots, p-1$ reordered.
- Euler's phi: $\varphi(n)$ counts $1 \le k \le n$ coprime to $n$. $\varphi(p^e) = p^{e-1}(p-1)$, $\varphi(mn) = \varphi(m)\varphi(n)$ for coprime $m, n$, so $\varphi(n) = n \prod (1 - \frac{1}{p})$. Examples: $\varphi(12) = 4$, $\varphi(360) = 96$, $\varphi(pq) = (p-1)(q-1)$.
- Euler: $\gcd(a, n) = 1$ gives $a^{\varphi(n)} \equiv 1 \pmod n$. Reduce exponents mod $\varphi(n)$, never mod $n$, and only when $a$ is coprime to $n$.
- Square-and-multiply: `result = 1`; while $e > 0$, multiply `result` by `base` if $e$ is odd, square `base`, halve $e$. At most $2L$ multiplications for an $L$-bit exponent. Python: `pow(a, e, n)`.
- Fermat test: if $\gcd(a, n) = 1$ and $a^{n-1} \not\equiv 1 \pmod n$, then $n$ is composite. Carmichael numbers (561, 1105, 1729, ...) pass for every coprime base; Miller-Rabin is the repair.

Main mistakes:

- Using $a^{p-1} \equiv 1$ when $p \mid a$ (then it is 0).
- Computing `a**e % n` for large $e$ instead of `pow(a, e, n)`.
- Trusting a passed Fermat test as proof of primality.

### RSA cryptography

| Step | What happens | Toy example |
|---|---|---|
| Choose primes | $p \ne q$ | $7, 11$ |
| Modulus | $n = pq$ | $77$ |
| Totient | $\varphi(n) = (p-1)(q-1)$ | $60$ |
| Public exponent | $\gcd(e, \varphi(n)) = 1$ | $e = 13$ |
| Private exponent | $d = e^{-1} \bmod \varphi(n)$ | $d = 37$ |
| Encrypt | $c = m^e \bmod n$ | $5 \to 26$ |
| Decrypt | $m = c^d \bmod n$ | $26 \to 5$ |

- Correctness: $ed = 1 + k\varphi(n)$, so $m^{ed} \equiv m$ mod $p$ and mod $q$ (Fermat, including $p \mid m$), and the Chinese remainder theorem combines them.
- Knowing $\varphi(n)$ gives the factors: $p + q = n - \varphi(n) + 1$ and $pq = n$.
- Security is an assumption: no fast factoring algorithm is known for ordinary computers, but none is proved impossible. Keys are at least 2048 bits (NIST SP 800-131A Rev 2).
- Textbook RSA is deterministic, malleable ($E(m_1)E(m_2) = E(m_1 m_2)$), and leaks small messages with small $e$. Real systems use padding (OAEP, PSS) and encrypt only a short symmetric key.

Main mistakes:

- Computing $d$ mod $n$ instead of mod $\varphi(n)$.
- Using $p = q$ or primes that are close together.
- Encrypting a message $m \ge n$.
- Treating the toy code as safe: use a vetted library for anything real.
