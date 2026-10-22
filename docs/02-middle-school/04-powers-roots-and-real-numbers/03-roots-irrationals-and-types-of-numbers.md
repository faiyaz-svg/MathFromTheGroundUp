# Roots, irrational numbers and types of numbers

After this lesson you can find, simplify and estimate square roots and cube roots, explain why $\sqrt{2}$ is not a fraction, and say which of the sets $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$ a number belongs to.

Before this: [exponent rules](01-exponent-rules.md), [rational number arithmetic](../01-integers-and-rational-numbers/03-rational-number-arithmetic.md) and [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Simplify $\sqrt{72}$ and $\sqrt{50} + \sqrt{18}$.
2. Between which two consecutive integers is $\sqrt{90}$? Estimate it to one decimal place.
3. Which of $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$ contain $-3$? Which contain $\sqrt{9}$, and which contain $\sqrt{2}$?

<details class="solution" markdown>
<summary>Answers</summary>

1. $6\sqrt{2}$ and $8\sqrt{2}$. Since $72 = 36 \times 2$, $\sqrt{72} = 6\sqrt{2}$; and $\sqrt{50} + \sqrt{18} = 5\sqrt{2} + 3\sqrt{2}$.
2. Between 9 and 10, since $81 < 90 < 100$. It is about 9.5: $9.5^2 = 90.25$, a little over 90, and $9.4^2 = 88.36$ is further away.
3. $-3$ is in $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$. $\sqrt{9} = 3$ is in all four. $\sqrt{2}$ is only in $\mathbb{R}$, because it is irrational.

</details>

## The idea

A square room has an area of $49 \text{ m}^2$. How long is each wall? You want a number whose square is 49, and $7^2 = 49$, so the walls are 7 m. Finding a side from an area undoes squaring, and that is what a square root does.

Now make the room $50 \text{ m}^2$. The side is a little more than 7 m, since $7.07^2 = 49.98$ and $7.08^2 = 50.13$. Trying more decimal places gets closer, $7.0710678\ldots$, but no decimal you write down squares to exactly 50, and no fraction does either. The side has a definite length, which you could mark on a tape measure, yet it is not a rational number.

That is the second half of this lesson. The rational numbers from the last chapter leave gaps in the number line, and numbers such as $\sqrt{2}$ and $\pi$ sit in those gaps. Putting the rational and irrational numbers together gives the real numbers, the full number line.

## Definitions

### Square roots and cube roots

A **square root** of a number $a$ is a number whose square is $a$. Every positive number has two square roots, one positive and one negative: both 7 and $-7$ are square roots of 49, since $7^2 = (-7)^2 = 49$. The only square root of 0 is 0. A negative number has no real square root, because the square of every real number is 0 or positive.

For $a \ge 0$, the **principal square root** $\sqrt{a}$ is the square root that is not negative. So $\sqrt{49} = 7$, never $-7$, and the negative root is written $-\sqrt{49}$. The symbol $\sqrt{\ }$ is the **radical sign**, and the number under it is the **radicand**.

In plain words, $\sqrt{a}$ answers "what non-negative number squared gives $a$?" It is one number, and it is never negative. When both roots are wanted, as in solving $x^2 = 49$, write $x = \pm 7$ or "$x = 7$ or $x = -7$".

A **cube root** of $a$, written $\sqrt[3]{a}$, is the number whose cube is $a$. Every real number has exactly one real cube root, including negative numbers, since an odd power keeps the sign: $\sqrt[3]{8} = 2$ and $\sqrt[3]{-8} = -2$, because $(-2)^3 = -8$.

Two facts about the principal root follow from these definitions. First, for $a \ge 0$, $(\sqrt{a})^2 = a$, since that is what $\sqrt{a}$ was defined to do. Second, for every real number $a$,

$$
\sqrt{a^2} = \lvert a \rvert.
$$

For example, $\sqrt{(-5)^2} = \sqrt{25} = 5 = \lvert -5 \rvert$. Squaring loses the sign, and the principal root always returns the non-negative one, so the result is the absolute value ([negative numbers and absolute value](../01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md)).

### Rules for products and quotients

For $a \ge 0$ and $b \ge 0$,

$$
\sqrt{ab} = \sqrt{a}\,\sqrt{b}, \qquad \text{and if } b > 0, \qquad \sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}.
$$

Here is why the first one holds. By the power of a product rule, $(\sqrt{a}\sqrt{b})^2 = (\sqrt{a})^2 (\sqrt{b})^2 = ab$, so $\sqrt{a}\sqrt{b}$ is a square root of $ab$. It is not negative, because it is a product of two numbers that are not negative. So it is the principal square root, $\sqrt{ab}$. The rule for quotients has the same proof with a fraction.

There is no rule like this for sums: $\sqrt{a + b}$ is not $\sqrt{a} + \sqrt{b}$ in general. For example, $\sqrt{9 + 16} = \sqrt{25} = 5$, while $\sqrt{9} + \sqrt{16} = 3 + 4 = 7$.

A root is in **simplest radical form** when the radicand has no perfect square factor other than 1, and there is no root in a denominator. So $6\sqrt{2}$ is in simplest radical form, while $\sqrt{72}$ is not, because 72 has the factor 36.

### Rational and irrational numbers

An **irrational number** is a real number that is not rational: it can't be written as $\frac{a}{b}$ with $a$ and $b$ integers and $b \ne 0$.

In plain words, no fraction of integers equals it exactly, though fractions can come as close as you like. This lesson proves that $\sqrt{2}$ is irrational. The number $\pi$, the circumference of a circle divided by its diameter ([area and circles](../06-geometry/02-area-and-circles.md)), is irrational too, but its proof needs calculus, so this book doesn't give it. The familiar values $3.14$ and $\frac{22}{7} = 3.142857\ldots$ are rational approximations of $\pi = 3.14159265\ldots$, not its value.

The decimal expansion tells the two kinds apart. [Rational number arithmetic](../01-integers-and-rational-numbers/03-rational-number-arithmetic.md#terminating-and-repeating-decimals) showed that every fraction's decimal terminates or repeats, and that every repeating decimal can be turned back into a fraction. Together these say:

$$
\text{a real number is rational exactly when its decimal expansion terminates or repeats.}
$$

So an irrational number has a decimal expansion that never ends and never settles into a repeating block, such as $\sqrt{2} = 1.41421356\ldots$ or $0.101001000100001\ldots$, where each run of zeros is one longer than the last.

### The real numbers and their subsets

The **real numbers** are all the numbers on the number line, rational and irrational. Each one has a decimal expansion, and each decimal expansion names a real number. The set of real numbers is written $\mathbb{R}$. A careful definition from axioms comes in [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md).

The **natural numbers** are the counting numbers starting from 0: $\mathbb{N} = \{0, 1, 2, 3, \ldots\}$. Many books start at 1 instead, so check the definition in whatever you read ([symbols and notation](../../reference/symbols-and-notation.md#number-sets)).

With the [integers](../01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md) $\mathbb{Z}$ and the rational numbers $\mathbb{Q}$, the four sets sit inside each other:

$$
\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}.
$$

The symbol $\subseteq$ means "is a subset of": every element of the set on the left is also an element of the set on the right. Every natural number is an integer, every integer $n$ is the fraction $\frac{n}{1}$, and every rational number is a point on the number line. The irrational numbers are the real numbers outside $\mathbb{Q}$. In the figure, each set is drawn inside the next, and the irrational numbers fill the part of $\mathbb{R}$ outside $\mathbb{Q}$:

![Nested rectangles: the natural numbers 0, 7 and the square root of 9 inside the integers, which add -3 and -12, inside the rational numbers, which add 0.5, -2/3, 0.3 repeating and 22/7, inside the real numbers. The irrational numbers, the square root of 2, pi and minus the square root of 5, are in the real numbers outside the rational numbers.](../../assets/figures/02-middle-school/roots-irrationals-and-types-of-numbers-number-sets.svg)

## How to do it

### Simplifying a square root

1. Factor the radicand. Look for the largest perfect square that divides it (try 4, 9, 16, 25, 36, 49, 64, 81, 100), or write its prime factorization.
2. Write the radicand as a perfect square times what is left: $72 = 36 \times 2$. With a prime factorization, each pair of equal primes is a perfect square: $72 = 2^2 \times 3^2 \times 2$.
3. Use $\sqrt{ab} = \sqrt{a}\sqrt{b}$ to take the root of the perfect square: $\sqrt{36 \times 2} = 6\sqrt{2}$.
4. Check that the number left under the root has no perfect square factor. If it has one, repeat.
5. Check by squaring: $(6\sqrt{2})^2 = 36 \times 2 = 72$.

Roots with the same radicand combine like the like terms in [equivalent expressions](../03-expressions-equations-inequalities/02-equivalent-expressions.md): $5\sqrt{2} + 3\sqrt{2} = 8\sqrt{2}$, by the distributive property. Roots with different radicands, such as $\sqrt{2} + \sqrt{3}$, don't combine, unless simplifying them first gives the same radicand.

### Estimating a square root

1. Find the perfect squares just below and just above the radicand. For $\sqrt{40}$: $36 < 40 < 49$.
2. Take their roots. The answer is between them: $6 < \sqrt{40} < 7$.
3. Refine. A good first guess is $n + \frac{d}{2n}$, where $n^2$ is the perfect square just below and $d$ is how far the radicand is above it. For $\sqrt{40}$, $n = 6$ and $d = 4$, so the guess is $6 + \frac{4}{12} \approx 6.33$.
4. Check by squaring, and adjust: $6.33^2 = 40.07$, a little too big, so try $6.32^2 = 39.94$.

The guess in Step 3 comes from $(n + h)^2 = n^2 + 2nh + h^2$. When $h$ is small, $h^2$ is tiny, so $n^2 + 2nh \approx n^2 + d$, which gives $h \approx \frac{d}{2n}$. It always comes out a little too big, because it ignores the $h^2$.

### Proving that the square root of 2 is irrational

We know the definition of a rational number, and that every fraction can be written in simplest form, with numerator and denominator sharing no factor other than 1 ([fractions and equivalent fractions](../../01-elementary/09-fractions-and-equivalent-fractions.md)). We want to show that no fraction of integers equals $\sqrt{2}$.

This is a [proof by contradiction](../../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md). We can't check every fraction one by one, since there are infinitely many. So we assume the opposite, that $\sqrt{2}$ is a fraction, and follow that assumption step by step until it says something impossible. An assumption that leads to something impossible must be false.

First, one fact about even numbers. An integer $n$ is even when $n = 2k$ for some integer $k$, and odd when $n = 2k + 1$.

*Lemma.* If $n$ is an integer and $n^2$ is even, then $n$ is even.

*Proof.* Every integer is even or odd, so it is enough to show that $n$ can't be odd. If $n$ were odd, $n = 2k + 1$ for some integer $k$, and then

$$
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,
$$

which is odd. But $n^2$ is even, so $n$ is not odd, and therefore $n$ is even. $\blacksquare$

*Theorem.* The number $\sqrt{2}$ is irrational.

*Proof.* Suppose, to get a contradiction, that $\sqrt{2}$ is rational. Then $\sqrt{2} = \frac{a}{b}$ for some integers $a$ and $b$ with $b \ne 0$, and we can choose the fraction in simplest form, so that $a$ and $b$ have no common factor other than 1.

Square both sides: $2 = \frac{a^2}{b^2}$. Multiplying both sides by $b^2$ gives

$$
a^2 = 2b^2.
$$

So $a^2$ is 2 times an integer, which means $a^2$ is even. By the lemma, $a$ is even, so $a = 2k$ for some integer $k$. Put that into the equation:

$$
(2k)^2 = 2b^2, \quad \text{so} \quad 4k^2 = 2b^2, \quad \text{so} \quad b^2 = 2k^2.
$$

Now $b^2$ is even, and by the lemma again, $b$ is even. So $a$ and $b$ are both even, which means 2 is a common factor of $a$ and $b$. That contradicts our choice of the fraction in simplest form. So the assumption was false, and $\sqrt{2}$ is irrational. $\blacksquare$

Look back. The contradiction came from the fact that $a^2 = 2b^2$ forces both $a$ and $b$ to be even, again and again: a fraction for $\sqrt{2}$ could always be reduced further, and no fraction can be reduced forever. The same idea shows that $\sqrt{3}$, $\sqrt{5}$ and in fact $\sqrt{n}$ for every natural number $n$ that is not a perfect square are irrational, using prime factorizations instead of even and odd (primes and unique factorization<!-- link: ../../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md -->).

## Worked examples

<div class="example" markdown>

### Example 1: simplifying the square root of 180

Simplify $\sqrt{180}$, and find its value to two decimal places.

Step 1: try the perfect squares. 180 is divisible by 4, since $180 = 4 \times 45$, and by 9, since $180 = 9 \times 20$, so it is also divisible by 36: $180 = 36 \times 5$. The prime factorization shows the same thing: $180 = 2^2 \times 3^2 \times 5$.

Step 2: the pairs $2^2$ and $3^2$ make the perfect square $2^2 \times 3^2 = 36$, so $180 = 36 \times 5$.

Step 3: take the root of the perfect square:

$$
\sqrt{180} = \sqrt{36 \times 5} = \sqrt{36}\,\sqrt{5} = 6\sqrt{5}.
$$

Step 4: 5 is prime, so it has no perfect square factor, and $6\sqrt{5}$ is in simplest radical form.

<div class="warning" markdown>

Watch out at Step 1: a smaller perfect square also works, but leaves more to do. Using 4 gives $\sqrt{180} = 2\sqrt{45}$, and 45 still has the factor 9, so Step 4 sends you back: $2\sqrt{45} = 2 \times 3\sqrt{5} = 6\sqrt{5}$. Stopping at $2\sqrt{45}$ is the common slip.

</div>

Step 5: check by squaring, $(6\sqrt{5})^2 = 36 \times 5 = 180$. For the value, $\sqrt{5} \approx 2.2361$, so $6\sqrt{5} \approx 13.42$. That fits the estimate method: $13^2 = 169 < 180 < 196 = 14^2$, and $13 + \frac{11}{26} \approx 13.42$.

</div>

<div class="example" markdown>

### Example 2: estimating the square root of 40

Estimate $\sqrt{40}$ to two decimal places without a calculator.

Steps 1 and 2: $36 < 40 < 49$, so $6 < \sqrt{40} < 7$. Step 3: with $n = 6$ and $d = 4$, the guess is $6 + \frac{4}{12} = 6.333\ldots$ Step 4: square nearby values with two decimal places:

$$
6.32^2 = 39.9424, \qquad 6.33^2 = 40.0689.
$$

So $\sqrt{40}$ is between 6.32 and 6.33. It is closer to 6.32, since 40 is $0.0576$ above $6.32^2$ but $0.0689$ below $6.33^2$. To two decimal places, $\sqrt{40} \approx 6.32$. (A calculator gives $6.3246$.)

Check another way: $\sqrt{40} = 2\sqrt{10}$, and $\sqrt{10} \approx 3.162$ gives $6.324$.

</div>

<div class="example" markdown>

### Example 3: signs and roots

Work out (a) $\sqrt{(-6)^2}$, (b) $\sqrt[3]{-64}$, (c) $-\sqrt{16}$, and (d) say what $\sqrt{-16}$ is.

- (a) Brackets first: $(-6)^2 = 36$, and $\sqrt{36} = 6$. The answer is 6, which is $\lvert -6 \rvert$, not $-6$.
- (b) $(-4)^3 = -64$, so $\sqrt[3]{-64} = -4$. Cube roots of negative numbers are negative.
- (c) The minus sign is outside the root: $-\sqrt{16} = -4$.
- (d) No real number squares to $-16$, so $\sqrt{-16}$ is not a real number. [Complex numbers](../../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md) give it a meaning, $4i$, later.

Check (b): $(-4) \times (-4) \times (-4) = 16 \times (-4) = -64$.

</div>

<div class="example" markdown>

### Example 4: adding roots (finish it yourself)

Simplify $\sqrt{12} + \sqrt{27} - \sqrt{48}$.

The radicands differ, so first simplify each root. The largest perfect squares are 4, 9 and 16:

$$
\sqrt{12} = \sqrt{4 \times 3} = 2\sqrt{3}, \qquad \sqrt{27} = \sqrt{9 \times 3} = 3\sqrt{3}, \qquad \sqrt{48} = \sqrt{16 \times 3} = 4\sqrt{3}.
$$

All three now have radicand 3. Combine them as like terms, and check the answer with decimals.

<details class="solution" markdown>
<summary>Finish</summary>

$2\sqrt{3} + 3\sqrt{3} - 4\sqrt{3} = (2 + 3 - 4)\sqrt{3} = \sqrt{3}$.

Check: $\sqrt{12} \approx 3.464$, $\sqrt{27} \approx 5.196$ and $\sqrt{48} \approx 6.928$, so the expression is about $3.464 + 5.196 - 6.928 = 1.732$, and $\sqrt{3} \approx 1.732$.

</details>

</div>

## Edge cases and common mistakes

Stopping before a root is fully simplified is flagged in Example 1. Here are the others.

<div class="warning" markdown>

Watch out: $\sqrt{a + b}$ is not $\sqrt{a} + \sqrt{b}$. With $a = 9$ and $b = 16$, the first is 5 and the second is 7. A root splits over a product, $\sqrt{9 \times 16} = 3 \times 4 = 12$, but not over a sum, for the same reason that a power doesn't split over a sum ([exponent rules](01-exponent-rules.md#edge-cases-and-common-mistakes)). The same goes for differences: $\sqrt{25 - 9} = 4$, not $5 - 3 = 2$.

</div>

<div class="warning" markdown>

Watch out: $\sqrt{9}$ is 3, not $\pm 3$. The equation $x^2 = 9$ has two solutions, 3 and $-3$, but the symbol $\sqrt{9}$ names one number, the principal root. Writing $\sqrt{9} = \pm 3$ would make $\sqrt{9}$ two numbers at once, and then $\sqrt{9} + 1$ would have no single value.

</div>

<div class="warning" markdown>

Watch out: $\sqrt{x^2} = x$ is only true when $x \ge 0$. For $x = -5$, $\sqrt{(-5)^2} = 5$, not $-5$. The rule that works for every $x$ is $\sqrt{x^2} = \lvert x \rvert$. The other order, $(\sqrt{x})^2 = x$, makes sense only for $x \ge 0$, since $\sqrt{x}$ isn't a real number when $x < 0$.

</div>

<div class="warning" markdown>

Watch out: $2\sqrt{3}$ means $2 \times \sqrt{3}$, which is about 3.46, while $\sqrt{2 \times 3} = \sqrt{6}$ is about 2.45. To move a number under a root, square it first: $2\sqrt{3} = \sqrt{4}\sqrt{3} = \sqrt{12}$.

</div>

Sums and products of irrational numbers can be rational: $\sqrt{2} + (-\sqrt{2}) = 0$, and $\sqrt{2} \times \sqrt{2} = 2$. So "irrational plus irrational" has no fixed type. A rational number plus an irrational one is always irrational, which Practice problem 7 proves.

A calculator can't settle whether a number is rational. It shows about ten digits, and every finite list of digits is a terminating decimal. The display $\sqrt{2} \approx 1.414213562$ is a rational approximation; the proof above is what shows that $\sqrt{2}$ itself is irrational.

Zero has one square root, 0. Every natural number has a square root in $\mathbb{R}$, but it is a natural number only when the number is a perfect square: $\sqrt{9}$ is in $\mathbb{N}$, while $\sqrt{8} = 2\sqrt{2}$ is irrational.

Here is where some boundary cases land. A number belongs to every set to the right of the first one that contains it.

| Number | $\mathbb{N}$ | $\mathbb{Z}$ | $\mathbb{Q}$ | $\mathbb{R}$ | Reason |
|---|---|---|---|---|---|
| $0$ | yes | yes | yes | yes | in $\mathbb{N}$ in this book; $0 = \frac{0}{1}$ |
| $-3$ | no | yes | yes | yes | negative, so not a natural number |
| $0.5$ | no | no | yes | yes | $0.5 = \frac{1}{2}$, not a whole number |
| $\sqrt{9}$ | yes | yes | yes | yes | $\sqrt{9} = 3$; the root sign doesn't make it irrational |
| $0.\overline{9}$ | yes | yes | yes | yes | $0.\overline{9} = 1$ |
| $\frac{22}{7}$ | no | no | yes | yes | a fraction of integers, close to $\pi$ but not equal |
| $\sqrt{2}$ | no | no | no | yes | proved irrational above |
| $\pi$ | no | no | no | yes | irrational |
| $\sqrt{-4}$ | no | no | no | no | not a real number |

## Tricks and shortcuts

Know the perfect squares up to $20^2 = 400$. The ones from $11^2$ to $15^2$ are in the last lesson; the rest are $16^2 = 256$, $17^2 = 289$, $18^2 = 324$, $19^2 = 361$ and $20^2 = 400$. They make Step 1 of simplifying and estimating quick.

A perfect square ends in 0, 1, 4, 5, 6 or 9, because the last digit of $n^2$ depends only on the last digit of $n$, and $0^2, 1^2, \ldots, 9^2$ end in 0, 1, 4, 9, 6, 5, 6, 9, 4, 1. So 1,000,002 and 2,743 are not perfect squares, and their roots are irrational.

Square roots of powers of ten and powers of 2 halve the exponent: $\sqrt{10^6} = 10^3$ and $\sqrt{2^{20}} = 2^{10} = 1024$. This is the power of a power rule run backwards, since $(10^3)^2 = 10^6$. For an odd exponent, borrow one power first: $\sqrt{10^5} = \sqrt{10} \times 10^2 \approx 316$.

The estimate $\sqrt{n^2 + d} \approx n + \frac{d}{2n}$ from Step 3 is very good when $d$ is small compared with $n^2$: $\sqrt{50} \approx 7 + \frac{1}{14} = 7.0714$, and the true value is $7.0711$.

To decide which of two roots is bigger, compare their squares: $3\sqrt{5} = \sqrt{45}$ and $4\sqrt{3} = \sqrt{48}$, so $4\sqrt{3}$ is bigger.

## In code

Python's `math` module has square and cube roots, and an exact integer square root that avoids floats.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

print(math.sqrt(72), 6 * math.sqrt(2))   # 8.48528137423857 8.485281374238571
print(math.sqrt(2) ** 2)                 # 2.0000000000000004
print(math.isqrt(72), math.isqrt(81))    # 8 9
n = 1_000_002
print(math.isqrt(n) ** 2 == n)           # False: not a perfect square
print(math.cbrt(-8))                     # -2.0
print((-8) ** (1 / 3))                   # (1.0000000000000002+1.7320508075688772j)
```

The first two lines show that a float can only approximate $\sqrt{2}$: the two values of $\sqrt{72}$ differ in the last digit, and squaring `math.sqrt(2)` misses 2. `math.isqrt` returns the largest integer whose square is at most `n`, exactly, so it is the safe way to test for a perfect square. The last line is a trap: raising a negative number to the float power `1/3` gives a complex number, not the real cube root, so use `math.cbrt` (Python 3.11 and later). `math.sqrt(-4)` raises a `ValueError`.

</details>

## FAQ

### Why is the square root of 9 only 3, when -3 squared is also 9?

So that $\sqrt{9}$ names one number. A symbol that stood for two numbers would make expressions such as $\sqrt{9} + 1$ ambiguous. The convention picks the non-negative root, and the other root is still available as $-\sqrt{9}$. When an equation has two solutions, the $\pm$ sign lists both: $x^2 = 9$ gives $x = \pm\sqrt{9} = \pm 3$.

### Is 0 a natural number?

In this book, yes: $\mathbb{N} = \{0, 1, 2, \ldots\}$, which is the usual choice in logic and computer science (array indices and the sizes of sets start at 0). Many number theory and calculus books start at 1. Neither is wrong, so read each book's definition. When it matters, $\mathbb{Z}^+$ for $\{1, 2, 3, \ldots\}$ avoids the question.

### Are there more irrational numbers than rational ones?

Yes, in a precise sense. The rational numbers can be listed in a single infinite sequence, and the real numbers can't, so most real numbers are irrational even though the irrational numbers you meet by name are few. [Cardinality and countability](../../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md) proves both facts.

### If the square root of 2 is irrational, how can it be a length?

Draw a square with sides of 1 m. Its diagonal is a real segment you can measure, and [the Pythagorean theorem](../06-geometry/04-pythagorean-theorem.md) shows that its length squared is $1^2 + 1^2 = 2$, so the diagonal is $\sqrt{2}$ m long. Being irrational is a fact about how a number can be written (not as a fraction of integers), not about whether it exists.

## Practice

### Warm-up

1\. Work out (a) $\sqrt{144}$, (b) $\sqrt{0.25}$, (c) $\sqrt[3]{-125}$, (d) $\sqrt{(-7)^2}$, (e) $-\sqrt{49}$ and (f) $\sqrt{\frac{9}{64}}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $12^2 = 144$, so 12.
- (b) $0.5^2 = 0.25$, so 0.5.
- (c) $(-5)^3 = -125$, so $-5$.
- (d) $\sqrt{49} = 7$, which is $\lvert -7 \rvert$.
- (e) The minus sign is outside: $-7$.
- (f) Root of a quotient: $\frac{\sqrt{9}}{\sqrt{64}} = \frac{3}{8}$.

Check (f): $\left(\frac{3}{8}\right)^2 = \frac{9}{64}$.

</details>

2\. Write in simplest radical form: (a) $\sqrt{48}$, (b) $\sqrt{200}$, (c) $\sqrt{45}$, (d) $\sqrt{98}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $48 = 16 \times 3$, so $4\sqrt{3}$.
- (b) $200 = 100 \times 2$, so $10\sqrt{2}$.
- (c) $45 = 9 \times 5$, so $3\sqrt{5}$.
- (d) $98 = 49 \times 2$, so $7\sqrt{2}$.

Check by squaring: $16 \times 3 = 48$, $100 \times 2 = 200$, $9 \times 5 = 45$ and $49 \times 2 = 98$.

</details>

3\. For each number, name the smallest of $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$ and $\mathbb{R}$ that contains it, or say that it is irrational: $-7$, $\frac{3}{4}$, $\sqrt{16}$, $\sqrt{5}$, $0.\overline{12}$, $-\sqrt{25}$.

<details class="solution" markdown>
<summary>Solution</summary>

- $-7$: $\mathbb{Z}$, since it is a negative integer.
- $\frac{3}{4}$: $\mathbb{Q}$.
- $\sqrt{16} = 4$: $\mathbb{N}$.
- $\sqrt{5}$: irrational, since 5 is not a perfect square, so its smallest set is $\mathbb{R}$.
- $0.\overline{12}$: it repeats, so it is rational, $\frac{12}{99} = \frac{4}{33}$; $\mathbb{Q}$.
- $-\sqrt{25} = -5$: $\mathbb{Z}$.

Check $0.\overline{12}$: $4 \div 33 = 0.121212\ldots$

</details>

### Standard

4\. Without a calculator, estimate to one decimal place: (a) $\sqrt{30}$, (b) $\sqrt{130}$. Show the squaring that confirms each answer.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $25 < 30 < 36$, so $5 < \sqrt{30} < 6$. The guess is $5 + \frac{5}{10} = 5.5$, and it is a little too big, as always. Check: $5.5^2 = 30.25$ and $5.4^2 = 29.16$. 30 is $0.25$ from $30.25$ and $0.84$ from $29.16$, so $\sqrt{30} \approx 5.5$.

(b) $121 < 130 < 144$, so $11 < \sqrt{130} < 12$. The guess is $11 + \frac{9}{22} \approx 11.41$. Check: $11.4^2 = 129.96$ and $11.5^2 = 132.25$, so $\sqrt{130} \approx 11.4$.

A calculator gives $5.477$ and $11.402$.

</details>

5\. Simplify: (a) $3\sqrt{12} + \sqrt{75}$, (b) $\sqrt{8} \times \sqrt{18}$, (c) $\dfrac{\sqrt{50}}{\sqrt{2}}$. Then (d) work out $\sqrt{16 + 9}$ and $\sqrt{16} + \sqrt{9}$, and say which rule (d) shows.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $3\sqrt{12} = 3 \times 2\sqrt{3} = 6\sqrt{3}$ and $\sqrt{75} = 5\sqrt{3}$, so the sum is $11\sqrt{3}$.

(b) $\sqrt{8}\sqrt{18} = \sqrt{144} = 12$. The product of two irrational numbers is rational here.

(c) $\sqrt{\frac{50}{2}} = \sqrt{25} = 5$.

(d) $\sqrt{25} = 5$, while $3 + 4 = 7$. A root doesn't split over a sum.

Check (a): $3 \times 3.4641 + 8.6603 = 19.0526$, and $11 \times 1.7321 = 19.053$.

</details>

6\. (a) A square garden has an area of $200 \text{ m}^2$. Find its side length exactly and to the nearest centimetre, and the length of fence needed to go around it. (b) A square image has 4,194,304 pixels. How many pixels wide is it?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The side is $\sqrt{200} = 10\sqrt{2}$ m, which is about 14.14 m. The fence is 4 sides: $40\sqrt{2} \approx 56.57$ m. If you round up to buy whole metres, that is 57 m.

(b) $4{,}194{,}304 = 2^{22}$, so the width is $\sqrt{2^{22}} = 2^{11} = 2048$ pixels. Halving the exponent works because $(2^{11})^2 = 2^{22}$.

Check: $14.14^2 = 199.94$, close to 200, and $2048^2 = 4{,}194{,}304$.

</details>

### Challenge

7\. Prove that if $r$ is rational and $x$ is irrational, then $r + x$ is irrational. Use it to show that $3 + \sqrt{2}$ is irrational. Then give two irrational numbers whose sum is rational.

<details class="solution" markdown>
<summary>Solution</summary>

We know that sums and differences of rational numbers are rational (a difference of two fractions of integers is again a fraction of integers). We want $r + x$ to be irrational. This is a proof by contradiction: assume $r + x$ is rational and show that $x$ would then be rational too.

*Proof.* Suppose, to get a contradiction, that $s = r + x$ is rational. Then $x = s - r$ is a difference of two rational numbers, so $x$ is rational. That contradicts the hypothesis that $x$ is irrational. So $r + x$ is irrational. $\blacksquare$

With $r = 3$ and $x = \sqrt{2}$, which is irrational by the theorem in this lesson, $3 + \sqrt{2}$ is irrational.

For the last part, $\sqrt{2}$ and $-\sqrt{2}$ are both irrational (if $-\sqrt{2}$ were rational, so would be its opposite), and their sum is $0$, which is rational. Another pair is $1 + \sqrt{2}$ and $1 - \sqrt{2}$, with sum 2.

Look back: the proof never used anything special about $\sqrt{2}$, only that rational numbers are closed under subtraction. Check the example numerically: $3 + \sqrt{2} = 4.41421356\ldots$, whose digits are those of $\sqrt{2}$ shifted, so they don't repeat either.

</details>

8\. This one reviews repeating decimals from [rational number arithmetic](../01-integers-and-rational-numbers/03-rational-number-arithmetic.md#turning-a-repeating-decimal-into-a-fraction). Write each repeating decimal as a fraction, take the square root, and write the answer as a fraction and as a decimal: (a) $\sqrt{0.\overline{4}}$, (b) $\sqrt{0.\overline{1}}$, (c) $\sqrt{0.\overline{9}}$.

<details class="solution" markdown>
<summary>Solution</summary>

A one-digit repeating block is that digit over 9.

- (a) $0.\overline{4} = \frac{4}{9}$, so the root is $\frac{\sqrt{4}}{\sqrt{9}} = \frac{2}{3} = 0.\overline{6}$.
- (b) $0.\overline{1} = \frac{1}{9}$, so the root is $\frac{1}{3} = 0.\overline{3}$.
- (c) $0.\overline{9} = \frac{9}{9} = 1$, so the root is 1.

All three answers are rational, because each radicand is a perfect square over a perfect square.

Check (a): $0.6667^2 = 0.4445$, close to $0.4444$.

</details>

## Where this shows up

- [The Pythagorean theorem](../06-geometry/04-pythagorean-theorem.md) finds lengths with square roots, and the distance between two points is a square root of a sum of squares. [Radicals and rational exponents](../../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md) writes $\sqrt{a}$ as $a^{1/2}$, and [solving quadratic equations](../../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md) uses both square roots at once, $\pm\sqrt{\ }$.
- The proof by contradiction here is the model for many proofs in [proof by contradiction](../../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md), and the sets $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}$ are the default domains of every university course.
- In statistics the standard deviation is the square root of an average of squares ([descriptive statistics and study design](../../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md)). In code, a float stores a rational approximation of $\sqrt{2}$, which is why `math.sqrt(2) ** 2` misses 2 (floating point basics<!-- link: ../../06-cs-math/01-number-representation/04-floating-point-basics.md -->).
