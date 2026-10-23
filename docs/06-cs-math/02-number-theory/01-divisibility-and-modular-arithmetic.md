# Divisibility and modular arithmetic

After this lesson you can prove the basic facts about divisibility, find the quotient and remainder for any integer (negatives included), compute with congruences by reducing first, and use them for day-of-week and check-digit problems.

Before this: [long division](../../01-elementary/07-long-division.md), [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md), [definitions, theorems, lemmas and corollaries](../../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md) (the definition of divides) and [equivalence relations and partitions](../../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find $1{,}001 \bmod 7$ and $-17 \bmod 5$.
2. What is the last digit of $7^{100}$?
3. If today is Wednesday, what day of the week is it 100 days from now?

<details class="solution" markdown>
<summary>Answers</summary>

1. Since $1{,}001 = 143 \cdot 7 + 0$, the first answer is 0. Since $-17 = (-4) \cdot 5 + 3$, the second is 3, not $-2$.
2. The last digit is the remainder mod 10. We have $7^2 = 49 \equiv -1 \pmod{10}$, so $7^4 \equiv 1$, and $7^{100} = (7^4)^{25} \equiv 1$. The last digit is 1.
3. Since $100 = 14 \cdot 7 + 2$, the answer is 2 days after Wednesday: Friday.

</details>

## The idea

A clock shows 9. Five hours later it shows 2, not 14. On a clock face, 14 and 2 are the same position, and so are 26, 38 and $-10$. Only the remainder after dividing by 12 matters. The days of the week do the same with 7: 100 days from now is 2 days from now, because 98 of them are 14 whole weeks.

Computers are full of this wrapping. A 32-bit counter that passes $2^{32} - 1$ starts again at 0. A hash table with 8 buckets sends a key to bucket `h % 8`. A credit card number carries a last digit chosen so that a weighted sum of all the digits leaves remainder 0 when divided by 10, which catches most typing mistakes.

This lesson makes the wrapping exact. We first prove the facts about "divides" that everything else uses, then prove the division algorithm for every integer, including negative ones, which the [long division](../../01-elementary/07-long-division.md) lesson left for here. Then we define congruence and show that you can add, subtract and multiply while reducing at any point you like. Division is the one operation that does not carry over so easily; that is the subject of [modular inverses and the Chinese remainder theorem](04-modular-inverses-and-chinese-remainder-theorem.md).

## Definitions

### Divides

For integers $a$ and $b$, we say that $a$ **divides** $b$, and write $a \mid b$, if $b = ak$ for some integer $k$. We also say that $a$ is a **divisor** or factor of $b$, and that $b$ is a multiple of $a$. The notation $a \nmid b$ means that $a$ does not divide $b$.

In plain words, $b$ is a multiple of $a$. So $3 \mid 12$ since $12 = 3 \cdot 4$, and $5 \nmid 12$. By this definition every integer divides 0, because $0 = a \cdot 0$, and 0 divides only 0. The statement $a \mid b$ is true or false; it is not a number, and writing "$3 \mid 12 = 4$" mixes the two.

### Quotient and remainder

The **division algorithm** says that for integers $n$ and $d$ with $d > 0$ there are unique integers $q$ and $r$ with

$$
n = qd + r \quad\text{and}\quad 0 \le r < d.
$$

The integer $q$ is the **quotient** and $r$ the **remainder**. The theorem is proved below for every integer $n$. In plain words, $d$ fits into $n$ a whole number $q$ of times and leaves $r$, which is too small to hold another $d$. For $n = -17$ and $d = 5$ we get $q = -4$ and $r = 3$, since $-17 = (-4) \cdot 5 + 3$.

The quotient is $q = \lfloor n/d \rfloor$, the fraction rounded down. The **mod operator** gives the remainder: $n \bmod d = r$. It is a number from $0$ to $d - 1$. Python writes `n // d` and `n % d`.

### Congruence

Let $n \ge 1$ be an integer, called the **modulus**. Integers $a$ and $b$ are **congruent modulo $n$**, written

$$
a \equiv b \pmod{n},
$$

if $n \mid a - b$. In plain words, $a$ and $b$ differ by a multiple of $n$, which turns out to mean that they leave the same remainder (Theorem 4). For example $17 \equiv 2 \pmod 5$ since $5 \mid 15$, and also $17 \equiv 7$ and $17 \equiv -3 \pmod 5$.

### The operator and the relation

Mod as an operator and congruence as a relation are different kinds of object, and the notation looks alike.

| | $a \bmod n$ | $a \equiv b \pmod{n}$ |
|---|---|---|
| What it is | a number, from 0 to $n - 1$ | a statement, true or false |
| Example | $17 \bmod 5 = 2$ | $17 \equiv 7 \pmod 5$ is true |
| Python | `17 % 5` | `(17 - 7) % 5 == 0` |

The two connect by Theorem 4: $a \equiv b \pmod n$ exactly when $a \bmod n = b \bmod n$. Note that $17 \equiv 7 \pmod 5$ is true while $17 \bmod 5 = 7$ is false.

## How to do it

### Facts about divides

*Theorem 1.* Let $a$, $b$ and $c$ be integers.

- (a) If $a \mid b$ and $b \mid c$, then $a \mid c$.
- (b) If $a \mid b$ and $a \mid c$, then $a \mid bx + cy$ for all integers $x$ and $y$.
- (c) If $a \mid b$ and $b \ne 0$, then $\lvert a \rvert \le \lvert b \rvert$.
- (d) If $a \mid b$ and $b \mid a$, then $a = b$ or $a = -b$.

Parts (a) and (b) are also in the [definitions lesson](../../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md); the proofs are short enough to repeat. We know only the definition of divides. We want four conclusions, and the plan is to write each hypothesis as an equation and compute.

*Proof.* (a) Write $b = aj$ and $c = bk$ for integers $j$ and $k$. Then $c = (aj)k = a(jk)$, and $jk$ is an integer.

(b) Write $b = aj$ and $c = ak$. Then $bx + cy = a(jx + ky)$, and $jx + ky$ is an integer.

(c) Write $b = ak$. Since $b \ne 0$, we have $k \ne 0$, so $\lvert k \rvert \ge 1$ because $k$ is an integer. Then $\lvert b \rvert = \lvert a \rvert \lvert k \rvert \ge \lvert a \rvert$.

(d) If $a = 0$, then $0 \mid b$ forces $b = 0$, and $a = b$. Otherwise $a$ and $b$ are both nonzero (if $b = 0$, then $b \mid a$ forces $a = 0$). By (c) applied twice, $\lvert a \rvert \le \lvert b \rvert$ and $\lvert b \rvert \le \lvert a \rvert$, so $\lvert a \rvert = \lvert b \rvert$. $\blacksquare$

Look back: part (c) is the one that gives divisibility its size limit. A nonzero number has only finitely many divisors, none bigger than itself in absolute value. Check with numbers: $3 \mid 12$ and $3 \mid 21$, so $3 \mid 12 \cdot 5 + 21 \cdot (-2) = 18$.

*Corollary 2.* If $d > 0$, $d \mid m$ and $\lvert m \rvert < d$, then $m = 0$.

*Proof.* If $m \ne 0$, then part (c) gives $d \le \lvert m \rvert < d$, which is impossible. $\blacksquare$

In plain words, the only multiple of $d$ that is closer to 0 than $d$ is 0 itself. This is what makes remainders unique.

### The division algorithm for every integer

*Theorem 3 (division algorithm).* Let $n$ and $d$ be integers with $d > 0$. Then there exist integers $q$ and $r$ with $n = qd + r$ and $0 \le r < d$, and the pair $(q, r)$ is unique.

What we know: well-ordering, which says every nonempty set of natural numbers has a least element ([strong induction and well-ordering](../../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md)), and Corollary 2. What we want: existence and uniqueness. The plan: for existence, collect the nonnegative numbers of the form $n - dq$ and take the smallest, which must be less than $d$. For uniqueness, subtract two proposed answers and apply Corollary 2.

*Proof.* Existence. Let $S = \{n - dq : q \in \mathbb{Z} \text{ and } n - dq \ge 0\}$. The set $S$ is nonempty: taking $q = -\lvert n \rvert$ gives $n + d\lvert n \rvert \ge n + \lvert n \rvert \ge 0$, using $d \ge 1$. By well-ordering, $S$ has a least element $r = n - dq$ for some integer $q$. Then $n = qd + r$ and $r \ge 0$. If $r \ge d$, then $r - d = n - d(q + 1)$ would be a smaller element of $S$, which is impossible. So $r < d$.

Uniqueness. Suppose $n = qd + r = q'd + r'$ with $0 \le r, r' < d$. Then $d(q - q') = r' - r$, so $d \mid r' - r$. Since $-d < r' - r < d$, Corollary 2 gives $r' - r = 0$. So $r = r'$, and then $d(q - q') = 0$ gives $q = q'$ because $d \ne 0$. $\blacksquare$

Look back: the condition $0 \le r < d$ is doing the work in both halves. The proof never used the sign of $n$, so negative numbers are covered. Check: $n = -17$ and $d = 5$ give $S = \{3, 8, 13, \dots\}$ from $q = -4, -5, -6, \dots$, whose least element is $3$, so $r = 3$ and $q = -4$.

### Congruence and remainders

*Theorem 4.* For integers $a$, $b$ and $n \ge 1$, we have $a \equiv b \pmod n$ if and only if $a$ and $b$ leave the same remainder when divided by $n$.

What we know: $a = q_1 n + r_1$ and $b = q_2 n + r_2$ with $0 \le r_1, r_2 < n$. What we want: $n \mid a - b$ exactly when $r_1 = r_2$. The plan: subtract the two equations.

*Proof.* Subtracting gives $a - b = n(q_1 - q_2) + (r_1 - r_2)$. If $r_1 = r_2$, then $a - b = n(q_1 - q_2)$, so $n \mid a - b$. Conversely, if $n \mid a - b$, then $n$ divides $(a - b) - n(q_1 - q_2) = r_1 - r_2$ by Theorem 1(b). Since $-n < r_1 - r_2 < n$, Corollary 2 gives $r_1 - r_2 = 0$. $\blacksquare$

*Theorem 5.* Congruence modulo $n$ is an equivalence relation on $\mathbb{Z}$.

*Proof.* Reflexive: $n \mid a - a = 0$. Symmetric: if $n \mid a - b$, then $n \mid -(a - b) = b - a$. Transitive: if $n \mid a - b$ and $n \mid b - c$, then $n$ divides their sum $a - c$ by Theorem 1(b). $\blacksquare$

Another proof: by Theorem 4, $a \sim b$ means $f(a) = f(b)$ for the function $f(x) = x \bmod n$, and any relation of that form is an equivalence relation (the kernel of a function, in the [equivalence relations lesson](../../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md)). The equivalence classes are the **residue classes** $[0], [1], \dots, [n - 1]$, where $[r] = \{r + nk : k \in \mathbb{Z}\}$. Every integer lies in exactly one of them, namely the class of its remainder. The set of these $n$ classes is written $\mathbb{Z}_n$.

*Theorem 6 (arithmetic with congruences).* If $a \equiv b \pmod n$ and $c \equiv d \pmod n$, then

$$
a + c \equiv b + d, \qquad a - c \equiv b - d, \qquad ac \equiv bd \pmod n.
$$

What we know: $a = b + nj$ and $c = d + nk$ for integers $j$ and $k$. What we want: the three differences are multiples of $n$. The plan: substitute and factor out $n$.

*Proof.* The sum is $a + c = (b + d) + n(j + k)$ and the difference is $a - c = (b - d) + n(j - k)$. For the product,

$$
ac = (b + nj)(d + nk) = bd + n(bk + dj + njk),
$$

and the bracket is an integer. So $n$ divides $ac - bd$. $\blacksquare$

Look back: nothing here needed the numbers to be small or positive. The next result is what makes the theorem useful.

*Corollary 7.* If $a \equiv b \pmod n$, then $a^k \equiv b^k \pmod n$ for every integer $k \ge 0$. So any expression built from integers with $+$, $-$ and $\times$ and whole-number powers has the same remainder mod $n$ if you replace each integer by one congruent to it.

*Proof.* For $k = 0$ both sides are 1. If $a^k \equiv b^k$, then multiplying by $a \equiv b$ with the product rule gives $a^{k+1} \equiv b^{k+1}$. This is induction on $k$. The second sentence is Theorem 6 applied one operation at a time. $\blacksquare$

In plain words, you may reduce at any stage. Theorem 6 is also the reason arithmetic on residue classes makes sense: the class of $a + c$ depends only on the classes of $a$ and $c$, not on which representatives you chose (the idea of being well-defined, from [functions and well-definedness](../../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md)).

### Computing with congruences

1. Replace each number by a congruent one that is small. The remainder from 0 to $n - 1$ is standard, but a negative number such as $-1$ is often smaller: $6 \equiv -1 \pmod 7$.
2. Do the additions, subtractions and multiplications on the small numbers. For a power, use Corollary 7 to raise the small number.
3. Reduce the result to the range 0 to $n - 1$.
4. Check by working one piece a different way, or by comparing with the full-size computation if it is small enough to do.

Only the base of a power is reduced. The exponent follows different rules, which come in [Fermat, Euler and fast exponentiation](05-fermat-euler-and-fast-exponentiation.md).

<div class="warning" markdown>

Watch out at step 2: you cannot divide both sides of a congruence by a common factor. We have $6 \cdot 2 \equiv 6 \cdot 4 \pmod{12}$, since both sides are $\equiv 0$, yet $2 \not\equiv 4 \pmod{12}$. Multiplication is allowed because Theorem 6 proves it; cancelling a factor needs a separate condition (the factor must be invertible), covered in the next lessons.

</div>

### Negative numbers and programming languages

Our definition gives remainders in $0, \dots, d - 1$ always. Languages disagree about what `%` does when a number is negative, because there are two natural ways to round the quotient. Python rounds it down (floor division), which matches the division algorithm. C (since C99), C++, Java, JavaScript and Rust truncate it towards 0, so the remainder takes the sign of the dividend.

| $n$ | $d$ | Python `n // d` | Python `n % d` | C `n / d` | C `n % d` |
|---|---|---|---|---|---|
| 17 | 5 | 3 | 2 | 3 | 2 |
| $-17$ | 5 | $-4$ | 3 | $-3$ | $-2$ |
| 17 | $-5$ | $-4$ | $-3$ | $-3$ | 2 |

In both families `(n / d) * d + n % d == n` holds, so each is a consistent division algorithm; they differ in which pair $(q, r)$ they choose. Python's remainder takes the sign of the divisor, so with $d > 0$ it is always the remainder in this lesson. To get a nonnegative remainder in C-style languages, use `((n % d) + d) % d`.

<div class="warning" markdown>

Watch out when you map a hash to a bucket: `hash % buckets` can be negative in Java or C when the hash is negative, which is an out-of-range index. The common fix `Math.abs(hash) % buckets` still fails for one input in Java, because `Math.abs` of the most negative 32-bit integer, $-2^{31}$, is itself negative. Use `Math.floorMod(hash, buckets)`.

</div>

### Two rules for digits

*Theorem 8.* Let $n = d_k d_{k-1} \dots d_1 d_0$ be written in decimal. Then $n \equiv d_0 + d_1 + \dots + d_k \pmod 9$, and the same holds mod 3. Also $n \equiv d_0 - d_1 + d_2 - \dots + (-1)^k d_k \pmod{11}$.

*Proof.* Since $10 \equiv 1 \pmod 9$, Corollary 7 gives $10^i \equiv 1$ for every $i \ge 0$. So $n = \sum d_i 10^i \equiv \sum d_i \cdot 1 \pmod 9$. Since $3 \mid 9$, a difference that is a multiple of 9 is also a multiple of 3, so the same congruence holds mod 3. For 11, use $10 \equiv -1 \pmod{11}$, so $10^i \equiv (-1)^i$. $\blacksquare$

These are the divisibility tests for 3, 9 and 11 from the [division facts lesson](../../01-elementary/06-division-facts-and-remainders.md#divisibility-rules), now with a reason. Casting out nines uses the first rule as a check on arithmetic: a product's digit sum, reduced mod 9, must equal the product of the factors' digit sums, reduced mod 9.

### Check digits

An identification number can carry a digit that is determined by the others, so that a typing mistake is likely to break the rule. The **ISBN-10** of a book has ten symbols $d_1 d_2 \dots d_{10}$, where $d_{10}$ may be the symbol X, standing for 10. The rule is

$$
10 d_1 + 9 d_2 + 8 d_3 + \dots + 2 d_9 + 1 \cdot d_{10} \equiv 0 \pmod{11}.
$$

To find the check digit $d_{10}$ from the first nine, compute the weighted sum $s$ of the nine digits and solve $s + d_{10} \equiv 0$, that is $d_{10} \equiv -s \pmod{11}$. For 0-306-40615-?, the weighted sum is

$$
10 \cdot 0 + 9 \cdot 3 + 8 \cdot 0 + 7 \cdot 6 + 6 \cdot 4 + 5 \cdot 0 + 4 \cdot 6 + 3 \cdot 1 + 2 \cdot 5 = 130,
$$

and $130 = 11 \cdot 11 + 9$, so $d_{10} \equiv -9 \equiv 2 \pmod{11}$. The ISBN is 0-306-40615-2. The full sum with $d_{10}$ is $132 = 12 \cdot 11$.

Why does the rule catch an error in one digit? If $d_i$ is replaced by a different digit, the sum changes by $w \cdot e$, where $w$ is the weight (from 1 to 10) and $e$ is the change (nonzero, at most 10 in absolute value). The new sum is a multiple of 11 only if $11 \mid we$. Since 11 is prime, $11 \mid we$ would force $11 \mid w$ or $11 \mid e$ (Euclid's lemma, proved in [primes and unique factorization](03-primes-and-unique-factorization.md)), and neither is possible. That is why the modulus is 11, not 10: with a modulus like 10, a weight of 2 or 5 can hide an error.

The **Luhn algorithm** protects credit card numbers, and many other identification numbers, and uses modulus 10. Starting from the rightmost digit, double every second digit (the second from the right, the fourth, and so on); if doubling gives a number above 9, subtract 9. Add everything. The number is valid when the total is a multiple of 10. For 79927398713, the doubled digits are $1 \to 2$, $8 \to 16 \to 7$, $3 \to 6$, $2 \to 4$ and $9 \to 18 \to 9$, and the total is $70$, so the number is valid. Luhn catches every single-digit error and most swaps of two neighbouring digits, but not the swap 09 and 90.

## Worked examples

<div class="example" markdown>

### Example 1: reducing before computing

Find the remainder of $4871 \cdot 3092 + 6^{15}$ when divided by 7. The number is about $4.7 \times 10^{11}$, so we will not compute it in full.

Step 1: reduce each piece. Since $4871 = 695 \cdot 7 + 6$, we have $4871 \equiv 6$. Since $3092 = 441 \cdot 7 + 5$, we have $3092 \equiv 5$. And $6 \equiv -1$, so $6^{15} \equiv (-1)^{15} = -1$.

Step 2: compute with the small numbers. $4871 \cdot 3092 \equiv 6 \cdot 5 = 30$, so the whole expression is $\equiv 30 + (-1) = 29$.

Step 3: reduce. $29 = 4 \cdot 7 + 1$, so the remainder is 1.

Check: the pieces separately are $4871 \cdot 3092 \bmod 7 = 2$ (since $30 = 4 \cdot 7 + 2$) and $6^{15} \bmod 7 = 6$ (since $-1 \equiv 6$), and $2 + 6 = 8 \equiv 1$. Python agrees: `(4871 * 3092 + 6**15) % 7` is 1.

<div class="warning" markdown>

Watch out at step 1: the exponent 15 stayed as it is. Reducing it, for example replacing $6^{15}$ by $6^{15 \bmod 7} = 6^1$, would be a different computation. It happens to give 6 here, which is the right residue of $6^{15}$, but only by luck.

</div>

</div>

<div class="example" markdown>

### Example 2: the day of the week

January 1, 2026 is a Thursday. What day of the week is December 25, 2026?

December 25 is the 359th day of 2026, so it is $358$ days after January 1. Number the days Monday $= 0$ to Sunday $= 6$, so Thursday is 3. Then the day number is $3 + 358 = 361 \pmod 7$, and $361 = 51 \cdot 7 + 4$. Day 4 is Friday.

Check: $358 = 51 \cdot 7 + 1$, so it is 51 whole weeks and one day after a Thursday, which is a Friday. Python's `datetime.date(2026, 12, 25).strftime("%A")` gives Friday.

</div>

<div class="example" markdown>

### Example 3: a negative number in two languages

Find $-45 \div 7$ in the sense of the division algorithm, and say what C would print for `-45 % 7`.

The multiples of 7 near $-45$ are $-49$ and $-42$. The division algorithm needs $0 \le r < 7$, so we take the multiple on the low side: $-45 = (-7) \cdot 7 + 4$, with $q = -7$ and $r = 4$. This is what Python's `-45 // 7` and `-45 % 7` give.

C cuts the quotient towards 0. The real quotient is $-6.43$, which C turns into $-6$, and then $-45 = (-6) \cdot 7 + (-3)$, so `-45 % 7` is $-3$.

Check: both pairs rebuild $-45$, since $(-7)(7) + 4 = -45$ and $(-6)(7) - 3 = -45$. The two remainders differ by 7, the divisor, as they must.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Find the check digit of the ISBN-10 0-19-853453-?. The weighted sum of the nine digits is done:

$$
10 \cdot 0 + 9 \cdot 1 + 8 \cdot 9 + 7 \cdot 8 + 6 \cdot 5 + 5 \cdot 3 + 4 \cdot 4 + 3 \cdot 5 + 2 \cdot 3 = 219.
$$

Finish: reduce 219 mod 11, solve for $d_{10}$ and check.

<details class="solution" markdown>
<summary>Finish</summary>

Since $219 = 19 \cdot 11 + 10$, we have $s \equiv 10$, so $d_{10} \equiv -10 \equiv 1 \pmod{11}$. The ISBN is 0-19-853453-1.

Check: the full weighted sum is $219 + 1 = 220 = 20 \cdot 11$. A remainder of $s \equiv 1$ would need $d_{10} = 10$, written X, since $-1 \equiv 10$.

</details>

</div>

## Edge cases and common mistakes

The mistake of cancelling a common factor is flagged above, next to Theorem 6, and the one about reducing exponents is flagged in Example 1. These are the others.

<div class="warning" markdown>

Watch out for mixing the operator and the relation. The statement $17 \equiv 7 \pmod 5$ is true, and $17 \bmod 5 = 7$ is false because a remainder mod 5 is at most 4. Write $\equiv$ when two numbers differ by a multiple of $n$, and $\bmod$ when you want the standard remainder.

</div>

<div class="warning" markdown>

Watch out for a negative remainder. In the division algorithm, $-17 = (-3) \cdot 5 - 2$ has $r = -2$, which fails $0 \le r < 5$. The correct pair is $q = -4$ and $r = 3$. The mistake is the same as the one C makes by default, so check which convention your language uses before you rely on `%`.

</div>

The modulus must be at least 1. Modulo 1, every two integers are congruent, since $1 \mid x$ for all $x$, and there is only one residue class. Modulo 0 would mean $0 \mid a - b$, that is $a = b$, and `5 % 0` raises an error in Python. Congruence modulo $-n$ means the same as modulo $n$, so only $n \ge 1$ is ever written.

## Tricks and shortcuts

- Look for $\pm 1$. In arithmetic mod 7, $6 \equiv -1$, $8 \equiv 1$ and $13 \equiv -1$, so $6^{99} \equiv -1$ and $8^{1000} \equiv 1$. In mod 9 and mod 11, the digit rules of Theorem 8 are the same idea.
- The last digit of a number is its remainder mod 10, and the last two digits are its remainder mod 100. Since $4 \mid 100$, a number is divisible by 4 exactly when its last two digits are: $n = 100m + t$ with $t$ the last two digits, and $4 \mid 100m$.
- For a power of 2 as the modulus, the remainder is the low bits: $n \bmod 2^k$ is `n & (2**k - 1)`, the bit masks of [bitwise operations and masks](../01-number-representation/05-bitwise-operations-and-masks.md).
- Powers cycle. The powers of 2 mod 7 are $1, 2, 4, 1, 2, 4, \dots$, with period 3, and the powers of 10 mod 11 alternate $1, -1, 1, -1, \dots$. Find the cycle, then reduce the exponent by its length. Why a cycle exists, and how long it can be, is the subject of [Fermat, Euler and fast exponentiation](05-fermat-euler-and-fast-exponentiation.md).

## In code

The code is the lesson in miniature. The first part is the division algorithm in Python's convention and the C convention, the second is reduce-before-compute, and the last is the two check-digit rules.

<details class="code" markdown>
<summary>In code</summary>

```python
import datetime

def divide(n, d):
    """Division algorithm for d > 0: unique q, r with n = q*d + r and 0 <= r < d."""
    q, r = n // d, n % d       # Python floors the quotient, so r is already in range
    assert n == q * d + r and 0 <= r < d
    return q, r

def c_mod(a, n):
    """What a % n gives in C, Java and JavaScript: the sign follows a."""
    r = abs(a) % abs(n)
    return r if a >= 0 else -r

print(divide(83, 9), divide(-83, 9), divide(-5, 12))   # (9, 2) (-10, 7) (-1, 7)
print(-17 % 5, -17 // 5, 17 % -5)                      # 3 -4 -3
print(c_mod(-17, 5), c_mod(17, -5), c_mod(-45, 7))     # -2 2 -3

# Reduce before computing (Example 1)
print((4871 * 3092 + 6**15) % 7)                       # 1
print((4871 % 7 * (3092 % 7) + (-1) ** 15) % 7)        # 1
print(pow(7, 100, 10))                                 # 1

# Digit rule for 9 (Theorem 8) and the day of the week (Example 2)
print(1234567 % 9, sum(map(int, "1234567")) % 9)       # 1 1
print(datetime.date(2026, 12, 25).strftime("%A"))      # Friday

def isbn10_valid(s):
    digits = [10 if c in "Xx" else int(c) for c in s if c not in "- "]
    return sum(w * d for w, d in zip(range(10, 0, -1), digits)) % 11 == 0

def luhn_valid(s):
    total = 0
    for i, ch in enumerate(reversed(s)):
        d = int(ch)
        if i % 2 == 1:                 # every second digit from the right
            d = 2 * d - 9 if d > 4 else 2 * d
        total += d
    return total % 10 == 0

print(isbn10_valid("0-306-40615-2"), isbn10_valid("0-306-40651-2"))   # True False
print(luhn_valid("79927398713"), luhn_valid("79927398710"))           # True False
```

</details>

The line `2 * d - 9 if d > 4 else 2 * d` is the "subtract 9 if above 9" step, since $2d > 9$ exactly when $d \ge 5$.

## FAQ

### Why is the remainder never negative, when $-17 = (-3) \cdot 5 - 2$ is also true?

Both equations are true; only one has a remainder in the required range. Requiring $0 \le r < d$ is what makes the pair unique (Theorem 3). Without it you could add $d$ to $r$ and subtract 1 from $q$ forever. The choice also makes each integer belong to exactly one of the classes $[0], \dots, [n-1]$.

### What is the difference between $=$ and $\equiv$?

Equal numbers are the same number. Congruent numbers are different numbers that the modulus can't tell apart. Equality implies congruence for every modulus, but $17 \equiv 2 \pmod 5$ and $17 \ne 2$. Replacing a number by a congruent one is legal only inside a congruence, not inside an equation.

### Why can't I divide a congruence by a number?

Division would need a number to multiply by that undoes the first multiplication, an inverse. Mod 12 the product $6 \cdot 2$ and $6 \cdot 4$ are both 0, so dividing by 6 would turn $0 \equiv 0$ into $2 \equiv 4$. Some numbers do have inverses mod $n$ (mod 7, $3 \cdot 5 \equiv 1$), and exactly which ones is answered in [modular inverses and the Chinese remainder theorem](04-modular-inverses-and-chinese-remainder-theorem.md).

### Do I need to know both versions of `%`?

Yes if you read or write code in more than one language, and in particular for hashing, circular buffers and anything with wrap-around indexes. Python's matches the math in this lesson. In C-style languages, test with a negative input before you trust a `%` expression.

## Practice

### Warm-up

1\. Find the quotient $q$ and remainder $r$ with $n = qd + r$ and $0 \le r < d$ for (a) $n = 83$, $d = 9$, (b) $n = -83$, $d = 9$, (c) $n = 5$, $d = 12$, (d) $n = -5$, $d = 12$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $83 = 9 \cdot 9 + 2$, so $q = 9$ and $r = 2$.

(b) The multiple of 9 just below $-83$ is $-90$, so $-83 = (-10) \cdot 9 + 7$, with $q = -10$ and $r = 7$.

(c) Twelve does not fit into 5, so $5 = 0 \cdot 12 + 5$ with $q = 0$ and $r = 5$.

(d) The multiple of 12 just below $-5$ is $-12$, so $-5 = (-1) \cdot 12 + 7$, with $q = -1$ and $r = 7$.

Check: $81 + 2 = 83$, $-90 + 7 = -83$, $0 + 5 = 5$ and $-12 + 7 = -5$. All four remainders are in range.

</details>

2\. Decide whether each statement is true. (a) $38 \equiv 14 \pmod{12}$. (b) $-8 \equiv 13 \pmod 7$. (c) $100 \equiv 3 \pmod 7$. (d) $17 \equiv -17 \pmod{34}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) True: $38 - 14 = 24 = 2 \cdot 12$. (b) True: $-8 - 13 = -21 = -3 \cdot 7$. (c) False: $100 - 3 = 97 = 13 \cdot 7 + 6$, which leaves remainder 6. (d) True: $17 - (-17) = 34$.

Check with remainders: 38 and 14 both leave 2 mod 12; $-8$ and 13 both leave 6 mod 7; 100 leaves 2 and 3 leaves 3 mod 7; 17 and $-17$ both leave 17 mod 34.

</details>

3\. Use reduction to find (a) $2^{10} \bmod 7$, (b) $38 \cdot 47 \bmod 7$, (c) $123 \cdot 457 \bmod 10$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Since $2^3 = 8 \equiv 1 \pmod 7$, we get $2^{10} = (2^3)^3 \cdot 2 \equiv 2$.

(b) Since $38 \equiv 3$ and $47 \equiv 5$, the product is $\equiv 15 \equiv 1$.

(c) The last digits are 3 and 7, and $3 \cdot 7 = 21$, so the remainder mod 10 is 1.

Check: $2^{10} = 1024 = 146 \cdot 7 + 2$, $38 \cdot 47 = 1786 = 255 \cdot 7 + 1$ and $123 \cdot 457 = 56{,}211$.

</details>

### Standard

4\. Prove that $n^2 \bmod 4$ is 0 or 1 for every integer $n$. Deduce that a sum of two squares of integers never leaves remainder 3 when divided by 4, and that 2027 is not a sum of two squares.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: every integer is congruent mod 4 to one of $0, 1, 2, 3$, and Corollary 7. What we want: the possible values of $n^2 \bmod 4$. The plan: square each of the four residues.

*Proof.* Since $n \equiv r \pmod 4$ for some $r \in \{0, 1, 2, 3\}$, Corollary 7 gives $n^2 \equiv r^2$. The squares of 0, 1, 2, 3 are 0, 1, 4, 9, which are congruent to 0, 1, 0, 1 mod 4. So $n^2 \bmod 4 \in \{0, 1\}$.

For $x^2 + y^2$, the possible remainders are the sums $0 + 0 = 0$, $0 + 1 = 1$ and $1 + 1 = 2$. None is 3. Since $2027 = 506 \cdot 4 + 3$, it leaves remainder 3 and is not a sum of two squares. $\blacksquare$

Check: $2027 \bmod 4 = 3$, and a computer search over $x, y \le 45$ finds no pair with $x^2 + y^2 = 2027$.

</details>

5\. Is the card number 4111 1111 1111 1111 valid under the Luhn algorithm? What about 4111 1111 1111 1121?

<details class="solution" markdown>
<summary>Solution</summary>

Number the digits from the right, starting at 0. The digits in odd positions (the 2nd, 4th, ..., 16th from the right) are doubled. For 4111 1111 1111 1111, reading from the left, the 16 digits are 4, then fifteen 1s. The odd positions from the right are the 1st, 3rd, ..., 15th digits from the left, which are 4 and then seven 1s. Doubling gives 8 and seven 2s, a total of 22. The even positions are the eight remaining 1s, total 8. The sum is $22 + 8 = 30$, a multiple of 10, so the number is valid.

For 4111 1111 1111 1121, the second-last digit is 2 and sits in an odd position (the 2nd from the right), so it is doubled to 4 where a 1 was doubled to 2 before. The sum rises by 2 to 32, which is not a multiple of 10, so that number is invalid.

Check: `luhn_valid("4111111111111111")` is True and `luhn_valid("4111111111111121")` is False. The second has a single changed digit, which Luhn always catches.

</details>

6\. In an ISBN-10, two neighbouring digits $x$ and $y$ are swapped, with $x \ne y$. Prove that the check always fails.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the weights of neighbouring positions differ by 1. What we want: the weighted sum changes by a number that is not a multiple of 11. The plan: compute the change.

*Proof.* Let $x$ sit at weight $w + 1$ and $y$ at weight $w$ (with $1 \le w \le 9$). Before the swap their contribution is $(w + 1)x + wy$, and after it is $(w + 1)y + wx$. The change is the difference of the two, which is $y - x$. Each symbol is between 0 and 10, so $0 < \lvert y - x \rvert \le 10 < 11$. By Corollary 2, $11 \nmid y - x$. A valid number had a sum $\equiv 0$, and the new sum is $\equiv y - x \not\equiv 0 \pmod{11}$. So the check fails. $\blacksquare$

Check with 0-306-40615-2: swapping the 1 (weight 3) and the 5 (weight 2) gives 0-306-40651-2, whose sum is $132 + (5 - 1) = 136 = 12 \cdot 11 + 4$. That is not a multiple of 11, and `isbn10_valid` returns False.

</details>

### Challenge

7\. (a) Show that every six-digit number of the form $abcabc$ (such as 217,217) is divisible by 7, 11 and 13. (b) Since $1001 = 7 \cdot 11 \cdot 13$ and $1000 \equiv -1 \pmod{1001}$, a number is congruent mod 1001 to its three-digit groups taken alternately added and subtracted from the right. Use this to test whether 5,217,331 is divisible by 7, by 11 and by 13.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The number is $abc \cdot 1000 + abc = abc \cdot 1001$, and $1001 = 7 \cdot 11 \cdot 13$. So each of 7, 11 and 13 divides it. For 217,217: $217 \cdot 1001 = 217{,}217$.

(b) Write $5{,}217{,}331 = 331 + 217 \cdot 1000 + 5 \cdot 1000^2$. Since $1000 \equiv -1$ mod 1001, Corollary 7 gives $1000^2 \equiv 1$, so the number is $\equiv 331 - 217 + 5 = 119 \pmod{1001}$. Because 7, 11 and 13 all divide 1001, the number has the same remainder as 119 mod each of them. We have $119 = 17 \cdot 7$, so 7 divides it. Mod 11, $119 = 10 \cdot 11 + 9$, which is not 0. Mod 13, $119 = 9 \cdot 13 + 2$, which is not 0.

So 5,217,331 is divisible by 7 but not by 11 or 13.

Check: $5{,}217{,}331 = 7 \cdot 745{,}333$.

</details>

8\. This one reviews [long division](../../01-elementary/07-long-division.md). (a) Divide 2,705 by 13 by long division and write the answer as $n = qd + r$. (b) Find $-2{,}705 \bmod 13$ from your answer, without a second long division.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Thirteen goes into 27 twice with 1 left. Bring down 0 to make 10, which 13 goes into 0 times. Bring down 5 to make 105, which 13 goes into 8 times ($8 \cdot 13 = 104$) with 1 left. So $2{,}705 = 208 \cdot 13 + 1$.

(b) Negating gives $-2{,}705 = (-208) \cdot 13 - 1$, with a remainder of $-1$, which is out of range. Add and subtract 13: $-2{,}705 = (-209) \cdot 13 + 12$. So $q = -209$ and $r = 12$.

Check: $-209 \cdot 13 = -2{,}717$, and $-2{,}717 + 12 = -2{,}705$. Also $2{,}705 \equiv 1$ means $-2{,}705 \equiv -1 \equiv 12 \pmod{13}$.

</details>

## Where this shows up

- The next lesson, [GCD and Euclid's algorithm](02-gcd-and-euclids-algorithm.md), runs the division algorithm repeatedly, and the rest of the chapter builds arithmetic mod $n$ into [RSA cryptography](06-rsa-cryptography.md).
- Wrap-around arithmetic is how fixed-width integers behave: [two's complement](../01-number-representation/03-binary-arithmetic-and-twos-complement.md) computes mod $2^{32}$ or $2^{64}$, and hash tables, circular buffers, calendars and cron schedules all reduce mod something.
- Congruence is the main example of an equivalence relation in [equivalence relations and partitions](../../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md), and the first step to the abstract algebra courses that follow discrete math.
