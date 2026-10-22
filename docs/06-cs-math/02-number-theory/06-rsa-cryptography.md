# RSA cryptography

After this lesson you can generate an RSA key pair from two primes, encrypt and decrypt a number by hand with square-and-multiply, prove that decryption undoes encryption, and explain what the security of RSA rests on and why the bare textbook version is not safe to use.

Before this: [Fermat, Euler and fast exponentiation](05-fermat-euler-and-fast-exponentiation.md), [modular inverses and the Chinese remainder theorem](04-modular-inverses-and-chinese-remainder-theorem.md) and [primes and unique factorization](03-primes-and-unique-factorization.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. What is $\varphi(35)$?
2. Find the inverse of 5 mod 24.
3. With $n = 35$, compute $2^5 \bmod 35$ and then raise the result to the 5th power mod 35.

<details class="solution" markdown>
<summary>Answers</summary>

1. Since $35 = 5 \cdot 7$ with distinct primes, $\varphi(35) = 4 \cdot 6 = 24$.
2. Since $5 \cdot 5 = 25 \equiv 1 \pmod{24}$, the inverse is 5.
3. $2^5 = 32$. Then $32 \equiv -3 \pmod{35}$, so $32^5 \equiv (-3)^5 = -243 = -243 + 245 = 2$. Raising to the 5th power twice brought us back to 2, because $5 \cdot 5 = 25 \equiv 1 \pmod{24}$. That is the whole mechanism of RSA in miniature.

</details>

## The idea

To send a secret with an ordinary lock, two people must first share a key, and sharing it needs a secret channel, which is the problem you were trying to solve. In 1977 Rivest, Shamir and Adleman published a way around it: a lock that anyone can snap shut, but only one person can open. You publish a **public key**, a pair of numbers that lets anyone scramble a message to you. You keep a **private key**, a third number, which unscrambles it. Learning the private key from the public one must be too hard to do.

The scrambling is exponentiation. Pick a modulus $n$ and an exponent $e$, and turn a message $m$ (a number below $n$) into $m^e \bmod n$. Anyone can do this, and by fast exponentiation it is quick. To undo it, raise to a second exponent $d$ that satisfies $ed \equiv 1$ in the right sense. Euler's theorem says exactly when raising to the power $ed$ gives back the original. Finding $d$ requires $\varphi(n)$, and finding $\varphi(n)$ requires the factors of $n$. If $n$ is the product of two huge primes, then multiplying them was easy and factoring the product is not known to be.

So the scheme is a **trapdoor** function: easy in one direction, hard to reverse for anyone who lacks a secret (the primes), and easy again with the secret. The previous five lessons are the ingredients: the Euclidean algorithm for $d$, Euler's theorem for correctness, fast exponentiation for speed, the Chinese remainder theorem for a faster decryption and for the general proof, and the primes lesson for the hardness assumption.

## Definitions

An **RSA key pair** consists of the following numbers. Let $p$ and $q$ be two distinct primes and $n = pq$, the **modulus**. Let $e$ be an integer with $1 < e < \varphi(n)$ and $\gcd(e, \varphi(n)) = 1$, the **public exponent**, and let $d$ be an inverse of $e$ mod $\varphi(n)$, the **private exponent**. The **public key** is $(n, e)$ and the **private key** is $d$ (together with $p$ and $q$).

A **message** is an integer $m$ with $0 \le m < n$. **Encryption** produces the **ciphertext** $c = m^e \bmod n$, and **decryption** computes $c^d \bmod n$. In plain words, you encrypt with the public numbers and decrypt with the secret one.

The **factoring problem** is: given $n = pq$ with $p$ and $q$ large primes, find $p$ and $q$. The security of RSA is believed, not proved, to depend on its difficulty. The **key size** of RSA is the number of bits of $n$.

## How to do it

### Generating a key pair

1. Choose two distinct large primes $p$ and $q$ at random. Pick random odd numbers of the right size and test each one for primality (the Miller-Rabin test; by the prime number theorem about one in 355 odd 1024-bit numbers is prime, so a few hundred tries are expected).
2. Compute the modulus $n = pq$.
3. Compute $\varphi(n) = (p - 1)(q - 1)$.
4. Choose $e$ with $\gcd(e, \varphi(n)) = 1$. A common choice is $e = 65537 = 2^{16} + 1$, which has only two 1 bits and so needs only 17 multiplications to apply.
5. Compute $d = e^{-1} \bmod \varphi(n)$ with the extended Euclidean algorithm.
6. Publish $(n, e)$. Keep $d$ secret, and keep or destroy $p$, $q$ and $\varphi(n)$ (anyone who has them can get $d$).

Many libraries use $\lambda(n) = \operatorname{lcm}(p - 1, q - 1)$ in steps 3 and 5 in place of $\varphi(n)$. That also works (Practice 7) and gives a smaller $d$.

### Encrypting and decrypting

To encrypt a message $m$ with $0 \le m < n$: compute $c = m^e \bmod n$ with square-and-multiply. To decrypt: compute $c^d \bmod n$ the same way. If the factors are known, the decryption can be done separately mod $p$ and mod $q$ with exponents $d \bmod (p - 1)$ and $d \bmod (q - 1)$ and the two answers combined by the Chinese remainder theorem. That is what the examples below do by hand, and it is the usual way to do it in software.

### Why decryption works

*Theorem 1 (RSA correctness).* Let $p \ne q$ be primes, $n = pq$, and let $e$ and $d$ be positive integers with $ed \equiv 1 \pmod{(p-1)(q-1)}$. Then for every integer $m$ with $0 \le m < n$,

$$
(m^e)^d \equiv m \pmod n.
$$

What we know: Euler's and Fermat's theorems, and that $ed = 1 + k(p-1)(q-1)$ for some integer $k \ge 0$. What we want: the congruence for all $m$, including $m$ that share a factor with $n$. The plan: first the easy case $\gcd(m, n) = 1$ by Euler. Then, for every $m$, prove the congruence mod $p$ and mod $q$ separately and combine with the Chinese remainder theorem.

*Proof.* Write $ed = 1 + k\varphi(n)$ with $\varphi(n) = (p-1)(q-1)$.

Case 1: $\gcd(m, n) = 1$. By Euler's theorem $m^{\varphi(n)} \equiv 1 \pmod n$, so

$$
m^{ed} = m \cdot \left(m^{\varphi(n)}\right)^k \equiv m \cdot 1^k = m \pmod n.
$$

Case 2: any $m$. Look at the prime $p$. If $p \mid m$, then both $m^{ed}$ and $m$ are $\equiv 0 \pmod p$. If $p \nmid m$, then Fermat's theorem gives $m^{p-1} \equiv 1 \pmod p$, and $ed - 1 = k(p-1)(q-1)$ is a multiple of $p - 1$, so $m^{ed} = m \cdot (m^{p-1})^{k(q-1)} \equiv m \pmod p$. In both cases $p \mid m^{ed} - m$. The same argument with $q$ gives $q \mid m^{ed} - m$. Since $p$ and $q$ are distinct primes, they are coprime, so $pq = n$ divides $m^{ed} - m$ (the second part of Lemma 4 in the last lesson). $\blacksquare$

Look back: Case 2 includes Case 1, and it is the one to remember, because it also covers the (rare) messages that share a factor with $n$. The congruence $(m^e)^d \equiv m \pmod n$ together with $0 \le m < n$ and $0 \le c^d \bmod n < n$ says the decrypted value is exactly $m$, not just congruent to it. The condition $ed \equiv 1 \pmod{\varphi(n)}$ is the only place $d$ enters.

### Why the secret stays secret

An attacker has $n$, $e$ and a ciphertext $c$. To decrypt, they need $d$, and $d$ is the inverse of $e$ mod $\varphi(n)$. Computing $\varphi(n)$ is as hard as factoring $n$:

*Theorem 2.* Given $n = pq$ and $\varphi(n)$, one can find $p$ and $q$ with a few arithmetic steps.

*Proof.* We have $\varphi(n) = pq - p - q + 1$, so $p + q = n - \varphi(n) + 1$. Then $p$ and $q$ are the two roots of $x^2 - (p + q)x + n = 0$, which the quadratic formula finds. $\blacksquare$

For $n = 77$ and $\varphi = 60$: $p + q = 77 - 60 + 1 = 18$, and $x^2 - 18x + 77 = (x - 7)(x - 11)$. So whoever learns $\varphi(n)$ learns the factors, and it is believed that no shortcut avoids factoring. (It is also known that $d$ itself reveals the factors, though the argument is longer.)

What is known about the difficulty of factoring, plainly stated:

- The best algorithm known for large general numbers is the general number field sieve, which takes sub-exponential time: far faster than trial division, but not polynomial in the number of digits. No polynomial-time factoring algorithm is known for an ordinary computer, and nobody has proved that none exists.
- In 2020 a team factored the 829-bit number RSA-250, using about 2,700 core-years of computing ([integer factoring records](https://members.loria.fr/PZimmermann/records/factor.html), by Paul Zimmermann; check the page for newer records). Key sizes in use are far larger: NIST's guidance (Special Publication 800-131A, Revision 2) requires RSA moduli of at least 2048 bits.
- Factoring is not known to be NP-complete (P, NP and NP-completeness<!-- link: ../06-theory-of-computation/07-p-np-and-np-completeness.md -->), so a proof that $\mathrm{P} \ne \mathrm{NP}$ would not by itself show that factoring is hard.
- Shor's algorithm (1994) factors in polynomial time on a quantum computer. No quantum computer large enough to break real RSA keys is known to exist, and NIST has standardized post-quantum replacements for the public-key schemes that Shor's algorithm would break.
- Nobody has proved that breaking RSA requires factoring. The claim that RSA is secure is an assumption (the RSA problem is hard), and nothing here is a proof of it.

### Why textbook RSA is not enough

The scheme above, applied directly to a message, is called textbook RSA. It is correct, and it is not secure as a way to send messages. The weaknesses are known and easy to demonstrate with toy numbers.

- It is deterministic. The same message always gives the same ciphertext, so an eavesdropper who suspects the message is "yes" or "no" encrypts both with the public key and compares.
- It is malleable. Since $(m_1 m_2)^e = m_1^e m_2^e$, anyone can turn the ciphertext of $m$ into the ciphertext of $2m$ by multiplying by $2^e \bmod n$, without knowing $m$ or $d$.
- Small messages leak. If $m^e < n$, there is no reduction mod $n$, and the attacker just takes an ordinary $e$-th root of $c$. With $e = 3$ this happens for any $m$ below $\sqrt[3]{n}$.
- Messages must be below $n$, and there is no built-in way to handle longer data.

The fixes are padding and hybrid use. A padding scheme such as RSA-OAEP (specified in PKCS #1) adds fresh randomness and a structure that the decryptor checks, which removes the first three problems. In practice RSA encrypts only a short random key, and a symmetric cipher such as AES encrypts the actual data with that key. Signatures reverse the roles ($s = h^d \bmod n$ for a hash $h$ of the message, checked by $s^e \equiv h$) and use their own padding, such as RSA-PSS. Padded RSA with large keys is widely used, and its security rests on assumptions and careful design, not on a proof. The rule in practice: use a vetted library with the recommended padding, never your own implementation.

## Worked examples

<div class="example" markdown>

### Example 1: generating a toy key pair

Take $p = 7$ and $q = 11$. Step 2: $n = 77$. Step 3: $\varphi(77) = 6 \cdot 10 = 60$. Step 4: choose $e = 13$; since $13$ is prime and does not divide 60, $\gcd(13, 60) = 1$.

Step 5: Euclid on 60 and 13: $60 = 4 \cdot 13 + 8$, $13 = 1 \cdot 8 + 5$, $8 = 1 \cdot 5 + 3$, $5 = 1 \cdot 3 + 2$, $3 = 1 \cdot 2 + 1$. Back-substitute:

$$
\begin{aligned}
1 &= 3 - 2 = 3 - (5 - 3) = 2 \cdot 3 - 5 \\
&= 2\,(8 - 5) - 5 = 2 \cdot 8 - 3 \cdot 5 \\
&= 2 \cdot 8 - 3\,(13 - 8) = 5 \cdot 8 - 3 \cdot 13 \\
&= 5\,(60 - 4 \cdot 13) - 3 \cdot 13 = 5 \cdot 60 - 23 \cdot 13.
\end{aligned}
$$

So $13 \cdot (-23) \equiv 1 \pmod{60}$, and $d = -23 + 60 = 37$.

Check: $13 \cdot 37 = 481 = 8 \cdot 60 + 1$. The public key is $(77, 13)$ and the private exponent is $d = 37$.

</div>

<div class="example" markdown>

### Example 2: encrypting $m = 5$

Compute $5^{13} \bmod 77$ with square-and-multiply. Since $13 = 8 + 4 + 1$, we need $5^1$, $5^4$ and $5^8$. The repeated squares are $5^2 = 25$, $5^4 = 625 = 8 \cdot 77 + 9 \equiv 9$ and $5^8 \equiv 9^2 = 81 \equiv 4$. Multiply the three:

$$
5^{13} \equiv 5^8 \cdot 5^4 \cdot 5 \equiv 4 \cdot 9 \cdot 5 = 180 = 2 \cdot 77 + 26 \equiv 26.
$$

So the ciphertext is $c = 26$.

Check: `pow(5, 13, 77)` is 26, and the exact value $5^{13} = 1{,}220{,}703{,}125$ leaves remainder 26 when divided by 77.

</div>

<div class="example" markdown>

### Example 3: decrypting $c = 26$ using the factors

Step 1: reduce the ciphertext and exponent. Mod 7, $26 \equiv 5$, and $d = 37$ reduces mod $p - 1 = 6$ to $37 \equiv 1$. Mod 11, $26 \equiv 4$, and $37 \bmod 10 = 7$.

Step 2: exponentiate. Mod 7, $5^{1} = 5$. Mod 11, $4^7$: we have $4^2 = 16 \equiv 5$ and $4^4 \equiv 25 \equiv 3$, so $4^7 = 4^4 \cdot 4^2 \cdot 4 \equiv 3 \cdot 5 \cdot 4 = 60 \equiv 5$.

Step 3: combine with the Chinese remainder theorem. The number is $\equiv 5$ mod 7 and $\equiv 5$ mod 11, so it is 5 mod 77.

Decryption recovered $m = 5$. Check: `pow(26, 37, 77)` is 5, the direct computation without the factors.

</div>

<div class="example" markdown>

### Example 4: a message that shares a factor with $n$

Take $m = 14 = 2 \cdot 7$, so $\gcd(14, 77) = 7$ and Euler's theorem does not apply. Encrypting, $14^{13} \bmod 77$: mod 7 the base is 0, so $c \equiv 0 \pmod 7$, and mod 11 we have $14 \equiv 3$ and $3^{13} \equiv 3^{3} = 27 \equiv 5$ (since $13 \bmod 10 = 3$). The number that is $0$ mod 7 and $5$ mod 11 is $49$, so $c = 49$.

Decrypting, mod 7 we get $c \equiv 0$ and so $0^{37} = 0$. Mod 11 we get $49 \equiv 5$, and $5^{7}$: $5^2 = 25 \equiv 3$, $5^4 \equiv 9$, so $5^7 = 5^4 \cdot 5^2 \cdot 5 \equiv 9 \cdot 3 \cdot 5 = 135 \equiv 3$. The number that is $0$ mod 7 and $3$ mod 11 is 14.

So $m = 14$ comes back, as Case 2 of the proof promised. Check: `pow(49, 37, 77)` is 14.

</div>

<div class="example" markdown>

### Example 5: finish it yourself

Encrypt $m = 2$ with the key above, and decrypt. Encryption is done: $2^{13} = 8192 = 106 \cdot 77 + 30$, so $c = 30$. Start decrypting: mod 7, $30 \equiv 2$, and with the exponent $37 \bmod 6 = 1$ we get $2^1 = 2$. Finish the part mod 11, combine and check.

<details class="solution" markdown>
<summary>Finish</summary>

Mod 11, $30 \equiv 8$ and the exponent is $37 \bmod 10 = 7$. Compute $8^2 = 64 \equiv 9$, $8^4 \equiv 81 \equiv 4$, so $8^7 = 8^4 \cdot 8^2 \cdot 8 \equiv 4 \cdot 9 \cdot 8 = 288 = 26 \cdot 11 + 2 \equiv 2$.

The number is $\equiv 2$ mod 7 and $\equiv 2$ mod 11, so it is 2 mod 77. We recovered $m = 2$.

Check: `pow(30, 37, 77)` is 2.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for messages that are too big. Encryption works on integers $0 \le m < n$. A message $m \ge n$ is reduced mod $n$ before it is encrypted and comes back as $m \bmod n$, so information is lost. Longer data has to be split into blocks, or (better) encrypted with a symmetric cipher using an RSA-encrypted key.

</div>

<div class="warning" markdown>

Watch out for choosing $p$ and $q$ carelessly. If $p = q$, then $n = p^2$ and $\sqrt{n}$ reveals $p$. If $p$ and $q$ are close, Fermat's factoring method (write $n = a^2 - b^2$, starting from $a = \lceil\sqrt n\rceil$) finds them fast. If the random number generator is weak, two users can end up sharing a prime, and the GCD of their two moduli (Euclid's algorithm) reveals it.

</div>

<div class="warning" markdown>

Watch out for reusing $\varphi$ and $d$ with the wrong modulus. The exponents $e$ and $d$ are inverses mod $\varphi(n)$, not mod $n$. Reducing $d$ mod $n$ or computing $e^{-1} \bmod n$ gives a number that does not decrypt.

</div>

Some messages are unchanged by encryption. For any key, $m = 0$, $m = 1$ and $m = n - 1$ map to themselves, since $e$ is odd (it is coprime to the even number $\varphi(n)$) and $(-1)^e = -1$. For the toy key, $m = 76$ encrypts to 76. There can be other fixed points: for the toy key, $m = 33$ also encrypts to 33, while 5 and 14 do not. A padded scheme avoids these cases, which is one reason raw messages should not be encrypted directly.

## Tricks and shortcuts

- Decrypt by pieces: reduce $c$ mod $p$ and mod $q$, reduce $d$ mod $p - 1$ and $q - 1$, exponentiate small numbers, and combine by the Chinese remainder theorem (Examples 3 to 5). By hand this keeps the numbers small, and in software it is faster than one big exponentiation.
- Choose $e = 65537$ for real keys: it is prime, has two 1 bits, and applying it needs 17 multiplications. Choose $e = 3$ only in toy examples, since it makes the small-message weakness worse.
- To check a key pair quickly, test one message: $m = 2$ or $m = 3$ should survive a round trip.
- In hand examples pick $p$ and $q$ so that $\varphi(n)$ has an easy inverse for $e$, such as $e = 3$ when $3 \nmid \varphi(n)$.

## In code

The toy key from Examples 1 to 4, then a key from random 64-bit primes (Miller-Rabin with random bases), then the weaknesses of textbook RSA on the key $n = 3233$. This is a classroom sketch and is not safe to use.

<details class="code" markdown>
<summary>In code</summary>

```python
import random
from math import gcd, isqrt

# The toy key from Example 1
p, q, e = 7, 11, 13
n, phi = p * q, (p - 1) * (q - 1)
d = pow(e, -1, phi)
print(n, phi, d)                                   # 77 60 37
print(pow(5, e, n), pow(26, d, n))                 # 26 5
print(pow(14, e, n), pow(49, d, n))                # 49 14
print(all(pow(pow(m, e, n), d, n) == m for m in range(n)))   # True: every message works

def decrypt_crt(c, d, p, q):
    """Decrypt mod p and mod q separately, then combine with the CRT."""
    mp = pow(c % p, d % (p - 1), p)
    mq = pow(c % q, d % (q - 1), q)
    return (mp * q * pow(q, -1, p) + mq * p * pow(p, -1, q)) % (p * q)

print(decrypt_crt(26, d, p, q), decrypt_crt(49, d, p, q))   # 5 14

def is_probable_prime(k, rounds=20):
    """Miller-Rabin test."""
    if k < 4:
        return k in (2, 3)
    if k % 2 == 0:
        return False
    r, s = 0, k - 1
    while s % 2 == 0:
        r, s = r + 1, s // 2
    for _ in range(rounds):
        a = random.randrange(2, k - 1)
        x = pow(a, s, k)
        if x in (1, k - 1):
            continue
        for _ in range(r - 1):
            x = x * x % k
            if x == k - 1:
                break
        else:
            return False
    return True

random.seed(1)
def random_prime(bits):
    while True:
        k = random.getrandbits(bits) | (1 << (bits - 1)) | 1    # right length, odd
        if is_probable_prime(k):
            return k

P, Q = random_prime(64), random_prime(64)
N, PHI = P * Q, (P - 1) * (Q - 1)
E = 65537
D = pow(E, -1, PHI)
M = 123456789012345678901234567890
print(P != Q, gcd(E, PHI) == 1, N.bit_length() >= 127)       # True True True
print(pow(pow(M, E, N), D, N) == M)                           # True

# Knowing phi(n) gives the factors (Theorem 2)
s = N - PHI + 1
r = isqrt(s * s - 4 * N)
print(sorted([(s - r) // 2, (s + r) // 2]) == sorted([P, Q]))  # True

# Weaknesses of textbook RSA on n = 3233, e = 17, d = 2753 (p = 61, q = 53)
n, e, d = 3233, 17, 2753
c = pow(65, e, n)
print(c, pow(c, d, n))                                        # 2790 65
c2 = c * pow(2, e, n) % n                                     # a ciphertext made without d
print(pow(c2, d, n))                                          # 130, which is 2 * 65
print(pow(65, e, n) == pow(65, e, n))                         # True: deterministic
print(pow(10, 3, n))                                          # 1000: with e = 3, no reduction
```

</details>

## FAQ

### Why do we need both $p$ and $q$ to be prime, and not just $n$ hard to factor?

The proof of correctness and the formula $\varphi(n) = (p-1)(q-1)$ both use that $n$ is a product of exactly two distinct primes. With other shapes of $n$ the formula for $\varphi$ changes, and $n$ with small factors is easy to split. Using two primes of about the same size is the standard way to make the factoring problem hard.

### Is the private key really needed if I know the factors?

The factors are enough: from $p$ and $q$ you compute $\varphi(n)$ and then $d = e^{-1} \bmod \varphi(n)$. So the factors are the real secret, and the private key is a convenient form of it. That is also why leaking $p$, $q$ or $\varphi(n)$ is as bad as leaking $d$.

### If RSA is slow, why not use it for everything?

Each operation is an exponentiation with a 2048-bit (or larger) modulus, and it is thousands of times slower than a symmetric cipher such as AES. So RSA is used for a small secret (a key, or a hash to sign), and a fast symmetric cipher handles the bulk data.

### Does a bigger prime always mean a safer key?

Larger $n$ makes factoring slower by a lot (the sieve's running time grows faster than any polynomial in the number of digits, so doubling the bits adds far more than double the work), at the price of slower encryption and decryption, which grow roughly with the cube of the bit length. So key sizes are chosen to match a target security level, and they are raised over time as factoring records improve and computers get faster.

## Practice

### Warm-up

1\. Take $p = 5$, $q = 11$ and $e = 3$. Find $n$, $\varphi(n)$ and $d$, and encrypt $m = 9$.

<details class="solution" markdown>
<summary>Solution</summary>

$n = 55$ and $\varphi(55) = 4 \cdot 10 = 40$. Since $\gcd(3, 40) = 1$, $e = 3$ is allowed. The inverse of 3 mod 40 is 27, because $3 \cdot 27 = 81 = 2 \cdot 40 + 1$. So $d = 27$.

Encrypting: $9^3 = 729 = 13 \cdot 55 + 14$, so $c = 14$.

Check: $14^{27} \bmod 55 = 9$ (in Python, `pow(14, 27, 55)`), so decryption returns the message.

</details>

2\. Which of $e = 3, 4, 5, 7, 9$ can be used as a public exponent when $\varphi(n) = 40$?

<details class="solution" markdown>
<summary>Solution</summary>

An exponent is allowed when $\gcd(e, 40) = 1$, so that it has an inverse mod 40. We have $\gcd(3, 40) = 1$, $\gcd(4, 40) = 4$, $\gcd(5, 40) = 5$, $\gcd(7, 40) = 1$ and $\gcd(9, 40) = 1$. So 3, 7 and 9 work, and 4 and 5 don't.

Check: $40 = 2^3 \cdot 5$, so an exponent is usable exactly when it is odd and not a multiple of 5.

</details>

3\. For $n = 15$ ($p = 3$, $q = 5$), $e = 3$: find $d$, encrypt $m = 7$ and decrypt.

<details class="solution" markdown>
<summary>Solution</summary>

$\varphi(15) = 2 \cdot 4 = 8$, and $3 \cdot 3 = 9 \equiv 1 \pmod 8$, so $d = 3$. Encrypting, $7^3 = 343 = 22 \cdot 15 + 13$, so $c = 13$. Decrypting, $13^3 = 2197 = 146 \cdot 15 + 7$, so we get 7 back.

Check: $ed = 9 = 1 + 8$, as $ed \equiv 1 \pmod{\varphi(n)}$ requires.

</details>

### Standard

4\. An eavesdropper sees the public key $(n, e) = (33, 3)$ and the ciphertext $c = 3$. Break it.

<details class="solution" markdown>
<summary>Solution</summary>

Factor: $33 = 3 \cdot 11$, so $\varphi(33) = 2 \cdot 10 = 20$. The inverse of 3 mod 20 is 7, since $3 \cdot 7 = 21 \equiv 1$. So $d = 7$ and $m = 3^7 \bmod 33$. Compute $3^7 = 2187 = 66 \cdot 33 + 9$, so $m = 9$.

Check: $9^3 = 729 = 22 \cdot 33 + 3$, which is the ciphertext 3. Real keys are safe because the factoring step cannot be done.

</details>

5\. Using Theorem 2, recover the primes from $n = 3233$ and $\varphi(n) = 3120$.

<details class="solution" markdown>
<summary>Solution</summary>

$p + q = n - \varphi(n) + 1 = 3233 - 3120 + 1 = 114$ and $pq = 3233$. The primes are the roots of $x^2 - 114x + 3233 = 0$. The discriminant is $114^2 - 4 \cdot 3233 = 12{,}996 - 12{,}932 = 64$, with square root 8. So $x = \frac{114 \pm 8}{2}$, which gives 53 and 61.

Check: $53 \cdot 61 = 3233$ and $52 \cdot 60 = 3120$.

</details>

6\. Show that RSA encryption satisfies $E(m_1)\,E(m_2) \equiv E(m_1 m_2) \pmod n$, and check it with $n = 77$, $e = 13$, $m_1 = 5$, $m_2 = 3$. What attack does it allow?

<details class="solution" markdown>
<summary>Solution</summary>

*Proof.* $E(m_1)E(m_2) = m_1^e m_2^e = (m_1 m_2)^e = E(m_1 m_2)$ mod $n$, by the power rule for products.

Numbers: $E(5) = 26$, $E(3) = 3^{13} \bmod 77 = 38$, and $26 \cdot 38 = 988 = 12 \cdot 77 + 64$, so the product is 64. And $E(15) = 15^{13} \bmod 77 = 64$.

The attack: given a ciphertext $c = E(m)$, an attacker multiplies by $E(2)$ and sends $c \cdot E(2) \bmod n$, which decrypts to $2m$, without ever learning $m$. Padding schemes check a structure that this breaks.

Check: `pow(15, 13, 77)` is 64.

</details>

### Challenge

7\. Prove that Theorem 1 still holds if $ed \equiv 1 \pmod{\operatorname{lcm}(p-1, q-1)}$. Find the smaller $d$ for $n = 77$, $e = 13$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Case 2 of the proof needed only that $ed - 1$ is a multiple of $p - 1$ and of $q - 1$. What we want: the same with the lcm. The plan: a multiple of $\operatorname{lcm}(p-1, q-1)$ is a multiple of both.

*Proof.* If $ed - 1$ is a multiple of $\operatorname{lcm}(p-1, q-1)$, then it is a multiple of $p - 1$ and of $q - 1$. The proof of Case 2 then goes through unchanged: for $p \nmid m$, $m^{ed} = m \cdot (m^{p-1})^{(ed-1)/(p-1)} \equiv m \pmod p$, and the same for $q$. $\blacksquare$

For $n = 77$: $\operatorname{lcm}(6, 10) = 30$, and $13 \cdot 7 = 91 = 3 \cdot 30 + 1$, so $d' = 7$ works, instead of $d = 37$. Check: $26^7 \bmod 77 = 5$, the original message.

</details>

8\. This one reviews [fast exponentiation](05-fermat-euler-and-fast-exponentiation.md). How many modular multiplications does square-and-multiply need for $m^{65537} \bmod n$? About how many for a 2048-bit private exponent?

<details class="solution" markdown>
<summary>Solution</summary>

Since $65537 = 2^{16} + 1 = 10000000000000001_2$, it has 17 bits. Squaring $m$ sixteen times gives $m^{2^{16}}$, and one more multiplication by $m$ gives $m^{65537}$, so 17 multiplications.

A 2048-bit exponent has at most 2048 squarings and 2048 multiplications, about 4096 at most, and about 3072 for a typical exponent where half the bits are 1 (2048 squarings plus about 1024 multiplications).

Check: Theorem 5 of the last lesson bounds the count by $2L$ with $L = 17$ and $L = 2048$.

</details>

## Where this shows up

- Secure web traffic, signed software updates and SSH keys all use RSA or the related discrete-logarithm schemes, with the key sizes and padding described above. The same number theory (primes, inverses, exponentiation mod $n$) is behind Diffie-Hellman key exchange.
- The hardness assumption connects to P, NP and NP-completeness<!-- link: ../06-theory-of-computation/07-p-np-and-np-completeness.md -->: RSA is secure only if factoring has no fast algorithm, and that question is open.
- Within this chapter, every lesson is used: divisibility and congruences for the arithmetic, Euclid's algorithm for $d$, primes for key generation and the hardness assumption, the Chinese remainder theorem for the proof and for fast decryption, and Fermat and Euler for correctness.
