# Polynomial division and the remainder theorem

After this lesson you can divide one polynomial by another with long division and with synthetic division, use the remainder theorem and the factor theorem to test for zeros, list the possible rational zeros of a polynomial with the rational root theorem, and find all the zeros of a cubic.

Before this: [factoring polynomials](03-factoring-polynomials.md), [polynomial arithmetic](02-polynomial-arithmetic.md) and [long division](../../01-elementary/07-long-division.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Divide $x^2 + 7x + 12$ by $x + 3$.
2. Without dividing, find the remainder when $p(x) = 2x^3 - 5x^2 + x - 4$ is divided by $x + 2$.
3. Is $x - 2$ a factor of $x^3 - 7x + 6$?

<details class="solution" markdown>
<summary>Answers</summary>

1. The quotient is $x + 4$ and the remainder is 0, since $(x + 3)(x + 4) = x^2 + 7x + 12$.
2. The remainder is $p(-2) = -16 - 20 - 2 - 4 = -42$. Dividing by $x + 2 = x - (-2)$ means $c = -2$.
3. Yes. At $x = 2$ the value is $8 - 14 + 6 = 0$, and a zero value means $x - 2$ is a factor.

</details>

## The idea

Divide 156 by 12. Long division gives 13, with nothing left over, because $12 \times 13 = 156$. Now write the same numbers as polynomials in $x$ with $x = 10$: $156$ is $x^2 + 5x + 6$, $12$ is $x + 2$, and $13$ is $x + 3$. The polynomial division $(x^2 + 5x + 6) \div (x + 2) = x + 3$ is the same calculation with the carrying removed. Long division of polynomials works like the long division of numbers, one term of the quotient at a time, from the highest power down.

The new thing is a question that has no counterpart for whole numbers: is a number $c$ a zero of a polynomial $p$? You could substitute $c$ and compute. But dividing $p(x)$ by $x - c$ gives a quotient and a remainder, and the remainder turns out to be exactly $p(c)$. So division tests a zero, and when the remainder is 0 the quotient is the rest of the polynomial, one degree lower. That is how a cubic, which has no formula you can do in your head, is cut down to a quadratic you can factor.

## Definitions

The **division algorithm for polynomials** is the polynomial version of the theorem in [long division](../../01-elementary/07-long-division.md#definitions).

*Theorem.* Let $p(x)$ and $d(x)$ be polynomials with real coefficients, with $d(x)$ not the zero polynomial. Then there are unique polynomials $q(x)$ and $r(x)$ with

$$
p(x) = q(x)\,d(x) + r(x), \qquad \text{where } r(x) = 0 \text{ or } \deg r < \deg d.
$$

The polynomial $p$ is the **dividend**, $d$ is the **divisor**, $q$ is the **quotient** and $r$ is the **remainder**. In plain words, the divisor fits into the dividend $q$ times, and what is left over is too small, in degree, to hold another copy of the divisor. When $r = 0$ we say that $d$ **divides** $p$, or that $d$ is a factor of $p$.

For integers the condition was $0 \le r < d$, a remainder smaller than the divisor. Here "smaller" means lower in degree. A divisor of degree 1, such as $x - c$, always leaves a remainder that is a constant. The coefficients have to come from a number system where you can divide, such as the real numbers, because each step divides by the leading coefficient of $d$.

We know that the degree of a product is the sum of the degrees ([polynomial arithmetic](02-polynomial-arithmetic.md#definitions)). We want to show that $q$ and $r$ exist, and that there is only one pair. The plan: for existence, subtract off one term of the quotient at a time, which lowers the degree, and repeat. For uniqueness, compare two answers and look at degrees.

*Proof of existence.* Use strong induction on the degree of $p$ (if $p = 0$, take $q = r = 0$). Let $m = \deg d$ with leading coefficient $b$. If $p$ has degree less than $m$, take $q = 0$ and $r = p$. Otherwise $p$ has degree $n \ge m$ and leading coefficient $a$. Let $t(x) = \frac{a}{b}x^{n-m}$. Then $t\,d$ has the same leading term $ax^n$ as $p$, so $p_1 = p - t\,d$ has degree less than $n$ (or is 0). By the induction hypothesis, $p_1 = q_1 d + r_1$ with $r_1 = 0$ or $\deg r_1 < m$. Then $p = (q_1 + t)d + r_1$, which is the form we want.

*Proof of uniqueness.* Suppose $qd + r = q'd + r'$, with both remainders of degree below $\deg d$ (or 0). Then $(q - q')d = r' - r$. If $q \ne q'$, the left side has degree $\deg(q - q') + \deg d \ge \deg d$, but the right side is 0 or has degree below $\deg d$, a contradiction. So $q = q'$, and then $r = r'$. $\blacksquare$

Look back: the existence proof is the long division algorithm. Each pass takes $t$, the next term of the quotient, and subtracts $t\,d$ from what is left. Uniqueness is why the condition on the degree of $r$ matters; without it, many pairs would work (Practice problem 8).

Two theorems tell you what the remainder is when the divisor is linear.

*Remainder theorem.* When a polynomial $p(x)$ is divided by $x - c$, the remainder is the number $p(c)$.

*Proof.* The division algorithm gives $p(x) = q(x)(x - c) + r$, where $r$ is a constant, since its degree is below 1. Put $x = c$: $p(c) = q(c) \cdot 0 + r = r$. $\blacksquare$

*Factor theorem.* The polynomial $x - c$ is a factor of $p(x)$ if and only if $p(c) = 0$.

This is the remainder theorem with $r = 0$: the remainder is zero exactly when $p(c) = 0$. A number $c$ with $p(c) = 0$ is a **zero** (or root) of $p$. In plain words, finding a zero of a polynomial is the same as finding a linear factor.

A corollary will be used in the next lesson and when fitting curves: *a nonzero polynomial of degree $n$ has at most $n$ zeros.* To see why, suppose $c_1, \ldots, c_k$ are distinct zeros of $p$. By the factor theorem $p(x) = (x - c_1)p_1(x)$. For each other zero $c_j$, $0 = (c_j - c_1)p_1(c_j)$ and $c_j - c_1 \ne 0$, so $p_1(c_j) = 0$ by the zero-product property. Repeating, $p$ has the factor $(x - c_1)(x - c_2)\cdots(x - c_k)$, a polynomial of degree $k$, and since the degree of a product is the sum, $k \le n$. This also shows that two polynomials of degree at most $n$ that agree at $n + 1$ different numbers are equal: their difference has degree at most $n$ and too many zeros, so it is the zero polynomial.

### The rational root theorem

*Theorem (rational root theorem).* Let $p(x) = a_nx^n + \cdots + a_1x + a_0$ have integer coefficients with $a_n \ne 0$ and $a_0 \ne 0$. If a fraction $\frac{r}{s}$ in lowest terms is a zero of $p$, then $r$ divides $a_0$ and $s$ divides $a_n$.

We know the definition of a zero and that $r$ and $s$ share no factor other than 1. We want to show that $r \mid a_0$ and $s \mid a_n$. The plan is to clear the fractions and look at which terms $r$ and $s$ divide.

*Proof.* Put $x = \frac{r}{s}$ into $p(x) = 0$ and multiply by $s^n$:

$$
a_nr^n + a_{n-1}r^{n-1}s + \cdots + a_1rs^{n-1} + a_0s^n = 0.
$$

Every term except the last has a factor $r$, so $r$ divides $a_0s^n$. The numbers $r$ and $s$ share no prime factor, so no prime in $r$ divides $s^n$, and all of $r$ must divide $a_0$ (unique prime factorization, from [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md)). In the same way every term except the first has a factor $s$, so $s$ divides $a_nr^n$, and therefore $s$ divides $a_n$. $\blacksquare$

Look back: the theorem gives a short list of candidates, not a guarantee. It says that a rational zero has to be of the form $\frac{\text{factor of } a_0}{\text{factor of } a_n}$, and each candidate still has to be tested. If $a_n = 1$, every rational zero is an integer that divides $a_0$.

## How to do it

### Polynomial long division

1. Write the dividend and the divisor in standard form. Put in a term with coefficient 0 for each missing power in the dividend, so the columns line up.
2. Divide the leading term of the dividend by the leading term of the divisor. The result is the next term of the quotient.
3. Multiply the whole divisor by that term, and write the product under the dividend.
4. Subtract, changing the sign of every term of the product. The leading terms cancel.
5. The difference is the new dividend. Repeat from Step 2 until its degree is less than the degree of the divisor.
6. Read the quotient and the remainder. Check that $q(x)\,d(x) + r(x) = p(x)$.

### Synthetic division

Synthetic division is a shortcut for dividing by $x - c$. It keeps only the coefficients.

1. Write $c$ for the divisor $x - c$. For $x + 2$, $c = -2$. Write the coefficients of $p$ in order, with 0 for any missing power.
2. Bring down the first coefficient.
3. Multiply the number you just wrote by $c$, write the product under the next coefficient, and add them. Repeat to the end.
4. The last number is the remainder, which is $p(c)$. The other numbers are the coefficients of the quotient, starting one degree below $p$.

Why it works: this is Horner's method from [polynomial arithmetic](02-polynomial-arithmetic.md#evaluating-a-polynomial-with-horners-method). Each number written is $b_k = b_{k+1}c + a_k$, the running value in Horner's method at $x = c$. The last one is $p(c)$, the remainder, and the earlier ones are the coefficients of $q$. Evaluating a polynomial and dividing it by $x - c$ are the same calculation.

### Finding all the zeros of a polynomial with integer coefficients

1. If $a_0 = 0$, take out the power of $x$ you can. Then $x = 0$ is a zero.
2. List the candidates $\pm\frac{r}{s}$, with $r$ a factor of the constant term and $s$ a factor of the leading coefficient.
3. Test candidates with synthetic division, simplest first ($\pm 1$, $\pm 2$). A zero remainder means a zero.
4. Replace $p$ by the quotient, which has one degree less, and repeat on it. Candidates that failed for $p$ don't need to be tested again, except to find repeated zeros.
5. When a quadratic is left, factor it or use [the quadratic formula](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md).
6. Check by multiplying the factors back, or by substituting each zero.

If no candidate works, $p$ has no rational zeros. For example, the candidates for $x^3 - 2$ are $\pm 1$ and $\pm 2$, and the values are $-1$, $-3$, $6$ and $-10$. None is 0, so the equation $x^3 = 2$ has no rational solution: $\sqrt[3]{2}$ is irrational, the result of Practice problem 8 in [radicals and rational exponents](01-radicals-and-rational-exponents.md#practice) proved a second way.

## Worked examples

<div class="example" markdown>

### Example 1: long division with a missing term

Divide $6x^3 - 7x^2 + 4$ by $2x - 1$.

Step 1: the dividend has no $x$ term, so write it as $6x^3 - 7x^2 + 0x + 4$.

Step 2: divide the leading terms, $\frac{6x^3}{2x} = 3x^2$. That is the first term of the quotient. Step 3: multiply, $3x^2(2x - 1) = 6x^3 - 3x^2$. Step 4: subtract. The $x^3$ terms cancel, and $-7x^2 - (-3x^2) = -4x^2$, so what is left is $-4x^2 + 0x + 4$.

Step 5, second pass: $\frac{-4x^2}{2x} = -2x$. Multiply: $-2x(2x - 1) = -4x^2 + 2x$. Subtract: the $x^2$ terms cancel, and $0x - 2x = -2x$, leaving $-2x + 4$.

Third pass: $\frac{-2x}{2x} = -1$. Multiply: $-1(2x - 1) = -2x + 1$. Subtract: $4 - 1 = 3$. This has degree 0, less than the degree 1 of the divisor, so we stop.

$$
\begin{array}{rcl}
6x^3 - 7x^2 + 0x + 4 & & \\
\underline{-\,(6x^3 - 3x^2)} & \leftarrow & 3x^2(2x - 1) \\
-4x^2 + 0x + 4 & & \\
\underline{-\,(-4x^2 + 2x)} & \leftarrow & -2x(2x - 1) \\
-2x + 4 & & \\
\underline{-\,(-2x + 1)} & \leftarrow & -1(2x - 1) \\
3 & \leftarrow & \text{remainder}
\end{array}
$$

Step 6: the quotient is $3x^2 - 2x - 1$ and the remainder is 3. Check: $(2x - 1)(3x^2 - 2x - 1) = 6x^3 - 4x^2 - 2x - 3x^2 + 2x + 1 = 6x^3 - 7x^2 + 1$, and adding the remainder 3 gives $6x^3 - 7x^2 + 4$.

<div class="warning" markdown>

Watch out at Step 4: subtracting a polynomial changes every sign. Writing $-7x^2 - 3x^2 = -10x^2$ forgets that the product was subtracted. Putting the product in brackets with a minus sign in front, as above, keeps the signs straight.

</div>

By the remainder theorem for a non-monic divisor, the remainder is $p\left(\frac{1}{2}\right) = \frac{6}{8} - \frac{7}{4} + 4 = 3$, since $2x - 1 = 2\left(x - \frac{1}{2}\right)$ and $x = \frac{1}{2}$ makes the divisor 0. That agrees.

</div>

<div class="example" markdown>

### Example 2: synthetic division

Divide $x^3 + 2x^2 - 5x + 7$ by $x - 2$.

Step 1: $c = 2$, and the coefficients are $1, 2, -5, 7$. Step 2: bring down the 1. Step 3: multiply by 2 and add to the next coefficient: $2 + 2 \cdot 1 = 4$. Then $-5 + 2 \cdot 4 = 3$. Then $7 + 2 \cdot 3 = 13$.

| | $1$ | $2$ | $-5$ | $7$ |
|---|---|---|---|---|
| $c = 2$ | | $2$ | $8$ | $6$ |
| | $1$ | $4$ | $3$ | $13$ |

Step 4: the last number, 13, is the remainder, and the others are the quotient $x^2 + 4x + 3$. So $x^3 + 2x^2 - 5x + 7 = (x - 2)(x^2 + 4x + 3) + 13$.

Check with the remainder theorem: $p(2) = 8 + 8 - 10 + 7 = 13$. Check by expanding: $(x - 2)(x^2 + 4x + 3) = x^3 + 4x^2 + 3x - 2x^2 - 8x - 6 = x^3 + 2x^2 - 5x - 6$, and adding 13 gives $x^3 + 2x^2 - 5x + 7$.

<div class="warning" markdown>

Watch out: for $x + 2$ the number to use is $c = -2$, not 2. The divisor is $x - c$, so $x + 2 = x - (-2)$.

</div>

</div>

<div class="example" markdown>

### Example 3: all the zeros of a cubic

Find all the zeros of $p(x) = 2x^3 - 3x^2 - 11x + 6$.

Step 2: the constant term 6 has factors $1, 2, 3, 6$ and the leading coefficient 2 has factors $1, 2$. The candidates are $\pm 1, \pm 2, \pm 3, \pm 6, \pm\frac{1}{2}, \pm\frac{3}{2}$.

Step 3: test the simple ones. $p(1) = 2 - 3 - 11 + 6 = -6$, $p(-1) = -2 - 3 + 11 + 6 = 12$ and $p(2) = 16 - 12 - 22 + 6 = -12$ are not 0. But $p(-2) = -16 - 12 + 22 + 6 = 0$, so $-2$ is a zero and $x + 2$ is a factor.

Step 4: divide by $x + 2$ with $c = -2$ and coefficients $2, -3, -11, 6$:

| | $2$ | $-3$ | $-11$ | $6$ |
|---|---|---|---|---|
| $c = -2$ | | $-4$ | $14$ | $-6$ |
| | $2$ | $-7$ | $3$ | $0$ |

The remainder is 0, as it should be, and $p(x) = (x + 2)(2x^2 - 7x + 3)$.

Step 5: factor the quadratic with the ac method. The product $2 \cdot 3 = 6$ and sum $-7$ give $-1$ and $-6$, so $2x^2 - x - 6x + 3 = x(2x - 1) - 3(2x - 1) = (2x - 1)(x - 3)$. Then $p(x) = (x + 2)(2x - 1)(x - 3)$, and the zeros are $x = -2$, $x = \frac{1}{2}$ and $x = 3$. Both $\frac{1}{2}$ and $3$ were on the candidate list.

Step 6: check by substituting. $p(3) = 54 - 27 - 33 + 6 = 0$ and $p\left(\frac{1}{2}\right) = \frac{1}{4} - \frac{3}{4} - \frac{11}{2} + 6 = 0$.

</div>

<div class="example" markdown>

### Example 4: a cubic with one rational zero (finish it yourself)

Find all the zeros of $p(x) = 3x^3 + x^2 - 12x - 4$.

The candidates are $\pm\frac{\{1, 2, 4\}}{\{1, 3\}}$. Testing $x = -2$ gives $-24 + 4 + 24 - 4 = 0$, so $-2$ is a zero. Divide by $x + 2$ with $c = -2$ and the coefficients $3, 1, -12, -4$: bring down 3, then $1 + (-2)(3) = -5$, then $-12 + (-2)(-5) = -2$, then $-4 + (-2)(-2) = 0$. The quotient is $3x^2 - 5x - 2$.

Now factor the quadratic, list all the zeros, and check them.

<details class="solution" markdown>
<summary>Finish</summary>

For $3x^2 - 5x - 2$, $ac = -6$ and $b = -5$, so $m = -6$ and $n = 1$: $3x^2 - 6x + x - 2 = 3x(x - 2) + (x - 2) = (x - 2)(3x + 1)$. So $p(x) = (x + 2)(x - 2)(3x + 1)$ and the zeros are $-2$, $2$ and $-\frac{1}{3}$.

Check: $p(2) = 24 + 4 - 24 - 4 = 0$ and $p\left(-\frac{1}{3}\right) = -\frac{1}{9} + \frac{1}{9} + 4 - 4 = 0$. Also $\frac{-1}{3}$ was on the list: $r = 1$ divides 4 and $s = 3$ divides 3.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: leaving out a missing power. Dividing $x^3 - 1$ by $x - 1$ with the coefficients $1, -1$ puts the columns out of line. Write $x^3 + 0x^2 + 0x - 1$, with coefficients $1, 0, 0, -1$, and the synthetic division gives $1, 1, 1$ with remainder 0, so $x^3 - 1 = (x - 1)(x^2 + x + 1)$.

</div>

<div class="warning" markdown>

Watch out: synthetic division only works for divisors of the form $x - c$ with leading coefficient 1. To divide by $2x - 1$, use long division, or divide by $x - \frac{1}{2}$ and then divide the quotient by 2.

</div>

<div class="warning" markdown>

Watch out for the sign of $c$. The remainder of $p(x)$ on division by $x + 3$ is $p(-3)$, not $p(3)$. Check the sign by asking which value of $x$ makes the divisor 0.

</div>

The rational root theorem lists candidates only. In Example 3, 9 of the 12 candidates are not zeros. A polynomial with integer coefficients can also have zeros that are not rational, such as $1 \pm \sqrt{2}$ for $x^3 - 3x^2 + x + 1$. Here $x = 1$ is a zero, the quotient is $x^2 - 2x - 1$, and the quadratic formula gives the other two.

A remainder of 0 is the good case: the divisor is a factor. A nonzero remainder is not an error. In Example 2 the remainder 13 says that $x - 2$ is not a factor, and 13 is the value of $p(2)$.

If the constant term is 0, the polynomial has the factor $x$. In $x^3 - 7x^2 + 6x = x(x - 1)(x - 6)$, take out $x$ first. The rational root theorem requires $a_0 \ne 0$.

A zero can repeat. For $p(x) = (x - 1)^2(x + 2)$, dividing by $x - 1$ leaves $(x - 1)(x + 2)$, which has zero remainder at 1 again. After finding a zero, test it on the quotient before moving on.

## Tricks and shortcuts

To test whether $c$ is a zero, use synthetic division instead of substituting, because it gives you the quotient for free if the answer is yes. For a simple $c$ such as $\pm 1$, substituting is just as fast: $p(1)$ is the sum of the coefficients, and $p(-1)$ is the alternating sum.

When there are many candidates, narrow them with the signs. If all the coefficients are positive, there are no positive zeros, since a sum of positive numbers can't be 0. If the signs alternate, there are no negative zeros.

The remainder theorem finds the remainder without dividing, and it lets you find an unknown coefficient. If $x + 1$ is a factor of $x^3 + kx^2 - x + 6$, then $p(-1) = -1 + k + 1 + 6 = k + 6 = 0$, so $k = -6$.

The sum of the zeros and their product are in the coefficients. For a cubic $x^3 + bx^2 + cx + d$ with zeros $z_1, z_2, z_3$, the product $(x - z_1)(x - z_2)(x - z_3)$ expands to a constant term $-z_1z_2z_3$, so the zeros multiply to $-d$. In Example 3 the zeros of the monic version $x^3 - 1.5x^2 - 5.5x + 3$ multiply to $(-2)(0.5)(3) = -3 = -d$. It is a quick check on a list of zeros.

## In code

Synthetic division is Horner's method that keeps its intermediate values. The function below returns the quotient and the remainder for a coefficient list written from the highest power down, and a loop tests the rational root candidates.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction
from itertools import product

def synthetic(coeffs, c):
    """Divide by (x - c). Coefficients go from the highest power down."""
    out = [coeffs[0]]
    for a in coeffs[1:]:
        out.append(a + out[-1] * c)
    return out[:-1], out[-1]          # quotient coefficients, remainder

print(synthetic([1, 2, -5, 7], 2))            # ([1, 4, 3], 13)
print(synthetic([2, -3, -11, 6], -2))         # ([2, -7, 3], 0)

def divisors(n):
    return [d for d in range(1, abs(n) + 1) if n % d == 0]

def rational_zeros(coeffs):
    a_n, a_0 = coeffs[0], coeffs[-1]
    found = set()
    for r, s in product(divisors(a_0), divisors(a_n)):
        for sign in (1, -1):
            c = Fraction(sign * r, s)
            if synthetic(coeffs, c)[1] == 0:
                found.add(c)
    return sorted(found)

print(rational_zeros([2, -3, -11, 6]))        # [Fraction(-2, 1), Fraction(1, 2), Fraction(3, 1)]
print(rational_zeros([1, 0, 0, -2]))          # [], so x^3 - 2 has no rational zero
```

The first line reproduces Example 2: the quotient is $x^2 + 4x + 3$ and the remainder is 13. The second line is the table from Example 3. The function `rational_zeros` builds every candidate $\pm\frac{r}{s}$ from the divisors of the constant term and the leading coefficient and keeps the ones with remainder 0. It uses `Fraction` so that the test is exact, since floating-point arithmetic could turn a zero remainder into a tiny nonzero number. The empty list for $x^3 - 2$ is the proof, in code, that $\sqrt[3]{2}$ is irrational.

</details>

## FAQ

### Why does the remainder have to be lower in degree than the divisor?

It is what makes the answer unique, as for whole numbers, where $47 = 8 \times 5 + 7$ is true but the remainder 7 still holds another 5. With polynomials, $x^2 + 1 = x(x + 1) + (1 - x)$ is true, but the remainder $1 - x$ has the same degree as the divisor and could be divided again. The degree condition says the division is finished.

### Why is synthetic division allowed to drop the $x$'s?

Because the position in the list already records the power. Each coefficient sits in a column that stands for one power of $x$, just as the digits in a long division sit in columns for ones, tens and hundreds. Dropping the $x$'s changes nothing as long as the columns stay lined up, which is why missing powers must be written as 0.

### Does every polynomial have a zero?

Not among the real numbers: $x^2 + 1$ has none. Among the complex numbers, every polynomial of degree at least 1 has a zero, which is the fundamental theorem of algebra, and then the factor theorem splits off a linear factor again and again until the polynomial is a product of $n$ linear factors. [Complex numbers](../05-quadratics-and-complex-numbers/03-complex-numbers.md) is where the zeros of $x^2 + 1$ come from.

### Can I always find the zeros of a cubic this way?

Only the rational ones, and only if there is at least one. A cubic always has at least one real zero ([the next lesson](05-polynomial-functions-and-graphs.md#what-the-graph-must-do) shows why), but it needn't be rational, as in $x^3 - 2$. Then you use a numerical method such as bisection (next lesson) or the general formula for cubics, which is long and rarely used.

## Practice

### Warm-up

1\. Divide (a) $x^2 + 7x + 12$ by $x + 3$ and (b) $x^3 - 1$ by $x - 1$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Divide $x^2$ by $x$ to get $x$. Subtract $x(x + 3) = x^2 + 3x$, leaving $4x + 12$. Divide $4x$ by $x$ to get 4, and subtract $4(x + 3) = 4x + 12$, leaving 0. The quotient is $x + 4$ and the remainder is 0.

(b) With $c = 1$ and coefficients $1, 0, 0, -1$: bring down 1, then $0 + 1 = 1$, then $0 + 1 = 1$, then $-1 + 1 = 0$. The quotient is $x^2 + x + 1$ with remainder 0.

Check: $(x + 3)(x + 4) = x^2 + 7x + 12$, and $(x - 1)(x^2 + x + 1) = x^3 - 1$ (a difference of cubes).

</details>

2\. Use the remainder theorem to find the remainder when $p(x) = 2x^3 - 5x^2 + x - 4$ is divided by $x + 2$. Then divide to check.

<details class="solution" markdown>
<summary>Solution</summary>

Since $x + 2 = x - (-2)$, the remainder is $p(-2) = 2(-8) - 5(4) + (-2) - 4 = -16 - 20 - 2 - 4 = -42$.

Synthetic division with $c = -2$ and coefficients $2, -5, 1, -4$: bring down 2, then $-5 + (-2)(2) = -9$, then $1 + (-2)(-9) = 19$, then $-4 + (-2)(19) = -42$. The remainder is $-42$, and the quotient is $2x^2 - 9x + 19$.

Check: $(x + 2)(2x^2 - 9x + 19) - 42 = 2x^3 - 9x^2 + 19x + 4x^2 - 18x + 38 - 42 = 2x^3 - 5x^2 + x - 4$.

</details>

3\. Show that $x - 2$ is a factor of $x^3 - 7x + 6$, and factor the polynomial completely.

<details class="solution" markdown>
<summary>Solution</summary>

$p(2) = 8 - 14 + 6 = 0$, so $x - 2$ is a factor. Synthetic division with $c = 2$ and the coefficients $1, 0, -7, 6$: $1$, then $0 + 2 = 2$, then $-7 + 4 = -3$, then $6 - 6 = 0$. The quotient is $x^2 + 2x - 3 = (x + 3)(x - 1)$, so $p(x) = (x - 2)(x - 1)(x + 3)$.

Check: the zeros $2$, $1$ and $-3$ give $8 - 14 + 6 = 0$, $1 - 7 + 6 = 0$ and $-27 + 21 + 6 = 0$.

</details>

### Standard

4\. Divide $x^4 + x^3 + 2x - 3$ by $x^2 + x + 1$ with long division. State the quotient and the remainder.

<details class="solution" markdown>
<summary>Solution</summary>

Write the dividend as $x^4 + x^3 + 0x^2 + 2x - 3$. First, $\frac{x^4}{x^2} = x^2$, and $x^2(x^2 + x + 1) = x^4 + x^3 + x^2$. Subtract: $-x^2 + 2x - 3$. Next, $\frac{-x^2}{x^2} = -1$, and $-1(x^2 + x + 1) = -x^2 - x - 1$. Subtract: $2x - (-x) = 3x$ and $-3 - (-1) = -2$, leaving $3x - 2$. This has degree 1, less than 2, so we stop. The quotient is $x^2 - 1$ and the remainder is $3x - 2$.

Check: $(x^2 - 1)(x^2 + x + 1) = x^4 + x^3 + x^2 - x^2 - x - 1 = x^4 + x^3 - x - 1$, and adding $3x - 2$ gives $x^4 + x^3 + 2x - 3$.

</details>

5\. Find all the zeros of $6x^3 + 11x^2 - 3x - 2$.

<details class="solution" markdown>
<summary>Solution</summary>

The constant term $-2$ has factors $1, 2$, and the leading coefficient 6 has factors $1, 2, 3, 6$, so the candidates are $\pm1, \pm2, \pm\frac{1}{2}, \pm\frac{1}{3}, \pm\frac{2}{3}, \pm\frac{1}{6}$. Test: $p(1) = 12$, $p(-1) = -6 + 11 + 3 - 2 = 6$, $p(2) = 48 + 44 - 6 - 2 = 84$, and $p(-2) = -48 + 44 + 6 - 2 = 0$. So $-2$ is a zero. Synthetic division with $c = -2$ and the coefficients $6, 11, -3, -2$: $6$, then $11 - 12 = -1$, then $-3 + 2 = -1$, then $-2 + 2 = 0$. The quotient is $6x^2 - x - 1$, and $ac = -6$, $b = -1$ gives $m = -3$, $n = 2$: $6x^2 - 3x + 2x - 1 = 3x(2x - 1) + (2x - 1) = (2x - 1)(3x + 1)$.

So $p(x) = (x + 2)(2x - 1)(3x + 1)$ and the zeros are $-2$, $\frac{1}{2}$ and $-\frac{1}{3}$.

Check: expanding $(2x - 1)(3x + 1) = 6x^2 - x - 1$, and $(x + 2)(6x^2 - x - 1) = 6x^3 + 11x^2 - 3x - 2$.

</details>

6\. Find the value of $k$ that makes $x + 1$ a factor of $x^3 + kx^2 - x + 6$, and factor the polynomial for that $k$.

<details class="solution" markdown>
<summary>Solution</summary>

By the factor theorem, $p(-1) = 0$: $-1 + k + 1 + 6 = k + 6 = 0$, so $k = -6$. Then $p(x) = x^3 - 6x^2 - x + 6$. Grouping, $x^2(x - 6) - (x - 6) = (x - 6)(x^2 - 1) = (x - 6)(x - 1)(x + 1)$.

Check: $p(-1) = -1 - 6 + 1 + 6 = 0$, and the zeros $6, 1, -1$ all work: $p(6) = 216 - 216 - 6 + 6 = 0$ and $p(1) = 1 - 6 - 1 + 6 = 0$.

</details>

### Challenge

7\. A polynomial $p$ leaves remainder 5 when divided by $x - 1$ and remainder 11 when divided by $x - 2$. What is the remainder when $p$ is divided by $(x - 1)(x - 2)$?

<details class="solution" markdown>
<summary>Solution</summary>

By the remainder theorem, $p(1) = 5$ and $p(2) = 11$. The divisor $(x - 1)(x - 2)$ has degree 2, so the remainder has degree at most 1: $r(x) = ax + b$. The division algorithm says $p(x) = q(x)(x - 1)(x - 2) + ax + b$. Put in $x = 1$ and $x = 2$, where the first term vanishes: $a + b = 5$ and $2a + b = 11$. Subtracting gives $a = 6$ and then $b = -1$. The remainder is $6x - 1$.

Check: $r(1) = 5$ and $r(2) = 11$. One polynomial with these remainders is $p(x) = 6x - 1$ itself, which has remainder $6x - 1$ on division by any quadratic.

</details>

8\. (Reviews [long division](../../01-elementary/07-long-division.md).) Divide $p(x) = x^2 + 1$ by $d(x) = x + 1$. (a) Find the quotient and the remainder from the division algorithm. (b) Find two other pairs $q$ and $r$ with $p = qd + r$ whose remainder has degree 1 or more. (c) Why does the algorithm exclude them?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $x^2 \div x = x$, and $x(x + 1) = x^2 + x$ leaves $-x + 1$. Then $-x \div x = -1$, and $-1(x + 1) = -x - 1$ leaves $2$. So $q = x - 1$ and $r = 2$. By the remainder theorem, $p(-1) = 2$.

(b) Take $q = x$ and $r = 1 - x$: $x(x + 1) + 1 - x = x^2 + 1$. Or take $q = x - 2$ and $r = x + 3$: $(x - 2)(x + 1) + x + 3 = x^2 - x - 2 + x + 3 = x^2 + 1$.

(c) Both remainders have degree 1, which is not less than $\deg d = 1$, so another multiple of $d$ can still be taken out of them. This is the same as $47 = 8 \times 5 + 7$ in the integer algorithm: it is true, but the remainder 7 is too big. The condition on the degree makes the pair unique.

Check: $(x - 1)(x + 1) + 2 = x^2 - 1 + 2 = x^2 + 1$.

</details>

## Where this shows up

- The next lesson, [polynomial functions and graphs](05-polynomial-functions-and-graphs.md), uses the zeros and factors found here to sketch graphs. [Rational expressions](../06-rational-expressions-and-equations/01-rational-expressions.md) divides polynomials again to find the slanted asymptote of a rational function, and [partial fractions](../../05-university-core/04-integrals/05-partial-fractions-and-improper-integrals.md) uses polynomial long division in calculus.
- In CS, a CRC checksum is the remainder of a long division of polynomials whose coefficients are bits (arithmetic mod 2), and polynomial hashing evaluates a polynomial with Horner's method.
- In linear algebra, finding the eigenvalues of a 3 by 3 matrix means finding the zeros of a cubic, which is done with the rational root theorem and synthetic division ([eigenvalues and eigenvectors](../../05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md)).
