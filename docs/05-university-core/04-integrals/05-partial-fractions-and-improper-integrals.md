# Partial fractions and improper integrals

After this lesson you can integrate a rational function by splitting it into partial fractions, evaluate integrals over an infinite interval or with an unbounded integrand as limits, decide when $\int_1^\infty \frac{dx}{x^p}$ converges, compare an integral with a simpler one, and use an improper integral to check that a probability density has total area 1.

Before this: [u-substitution](03-u-substitution.md), [polynomial division and the remainder theorem](../../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md), [rational expressions](../../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md) and [limits at infinity](../01-limits-and-continuity/01-limits-intuition-and-limit-laws.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find $A$ and $B$ with $\dfrac{3x + 5}{(x - 1)(x + 2)} = \dfrac{A}{x - 1} + \dfrac{B}{x + 2}$.
2. Evaluate $\displaystyle\int_1^\infty \frac{dx}{x^2}$.
3. Does $\displaystyle\int_1^\infty \frac{dx}{x}$ converge?

<details class="solution" markdown>
<summary>Answers</summary>

1. Multiply by $(x - 1)(x + 2)$: $3x + 5 = A(x + 2) + B(x - 1)$. At $x = 1$: $8 = 3A$, so $A = \frac{8}{3}$. At $x = -2$: $-1 = -3B$, so $B = \frac{1}{3}$.
2. The integral up to $b$ is $\int_1^b x^{-2}\,dx = 1 - \frac{1}{b}$, which tends to 1 as $b \to \infty$. The integral is 1.
3. No. $\int_1^b \frac{dx}{x} = \ln b$, which grows without bound as $b \to \infty$.

</details>

## The idea

Add two fractions: $\frac{1}{x - 1} + \frac{1}{x + 2} = \frac{(x + 2) + (x - 1)}{(x - 1)(x + 2)} = \frac{2x + 1}{(x - 1)(x + 2)}$. The sum has a single denominator that is a product, and it looks harder to integrate than either piece. But each piece, $\frac{1}{x - 1}$ and $\frac{1}{x + 2}$, integrates to a logarithm. So if you can run the addition backward, taking $\frac{2x + 1}{(x - 1)(x + 2)}$ and splitting it into the two pieces it came from, then a hard-looking integral becomes two easy ones. That is partial fractions, the common-denominator step of [rational expressions](../../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md) in reverse.

The second half of the lesson is about a different difficulty: an interval that never ends, such as the area under $\frac{1}{x^2}$ for all $x \ge 1$, or a function that blows up inside the interval, such as $\frac{1}{\sqrt{x}}$ near 0. The area can still be a finite number. The figure shows the two cases that decide almost everything: $\frac{1}{x^2}$ has finite area from 1 to infinity, and $\frac{1}{x}$, which falls only a little more slowly, has infinite area.

![Two graphs side by side, both from x = 1 to x = 10 with the area under the curve shaded. On the left, y = 1 over x squared in green: the area from 1 to b is 1 minus 1 over b and tends to 1. On the right, y = 1 over x in red: the area from 1 to b is the natural log of b and grows without bound.](../../assets/figures/05-university-core/partial-fractions-and-improper-integrals-p-test.svg)

An integral of this kind is a limit of ordinary integrals, so nothing new is needed except the limit. The last use is a preview of probability: a probability density is a function whose total area is 1, and checking that takes an improper integral.

## Definitions

A **rational function** is a quotient $\frac{P(x)}{Q(x)}$ of two polynomials. It is **proper** if the degree of $P$ is less than the degree of $Q$, and improper otherwise. A quadratic $x^2 + bx + c$ is **irreducible** if it has no real roots, that is, if $b^2 - 4c < 0$. In plain words, it can't be factored into real linear factors, like $x^2 + 4$.

The **partial fraction decomposition** of a proper rational function is its expression as a sum of simpler fractions, one family for each factor of the denominator: for a repeated linear factor $(x - a)^k$ the terms $\frac{A_1}{x - a} + \cdots + \frac{A_k}{(x - a)^k}$, and for a repeated irreducible quadratic factor $\left(x^2 + bx + c\right)^k$ the terms $\frac{B_1x + C_1}{x^2 + bx + c} + \cdots + \frac{B_kx + C_k}{\left(x^2 + bx + c\right)^k}$. In plain words, every factor of the denominator, including each power of a repeated factor, gets its own term, and a linear factor gets a constant on top while a quadratic factor gets a linear expression on top.

An **improper integral** is an integral over an unbounded interval, or of a function that is unbounded near an endpoint, defined as a limit of ordinary integrals. For an infinite upper limit,

$$
\int_a^\infty f(x)\,dx = \lim_{b \to \infty}\int_a^b f(x)\,dx,
$$

and similarly $\int_{-\infty}^b f$ is the limit of $\int_t^b f$ as $t \to -\infty$. For $f$ continuous on $[a, b)$ but unbounded as $x \to b^-$,

$$
\int_a^b f(x)\,dx = \lim_{t \to b^-}\int_a^t f(x)\,dx,
$$

and a similar limit from the right handles a problem at $a$. If the limit exists as a finite number, the improper integral **converges** to it. Otherwise it **diverges**. For $\int_{-\infty}^{\infty} f$, or an integral with a problem at an interior point $c$, split at a point and require both pieces to converge. In plain words, an improper integral is the area up to a moving endpoint, and we ask whether the area settles down as the endpoint moves out to infinity or in to the trouble spot.

A **probability density function** (density, for short) is a function $f \ge 0$ with $\int_{-\infty}^{\infty} f(x)\,dx = 1$. The probability that a random value falls between $a$ and $b$ is $\int_a^b f(x)\,dx$. In plain words, the density's graph has total area 1, and the area over an interval is its probability.

## How to do it

### Partial fractions

1. If the degree of the numerator is at least the degree of the denominator, divide first, as in [polynomial division](../../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md). This gives a polynomial plus a proper fraction, and only the proper fraction needs decomposing.
2. Factor the denominator completely into linear factors and irreducible quadratics.
3. Write the form: one term for each factor, with unknown constants on top as in the definition. Use $\frac{A}{x - a}$ for a linear factor and $\frac{Bx + C}{x^2 + bx + c}$ for an irreducible quadratic, and one term for each power of a repeated factor.
4. Multiply both sides by the denominator, so that there are no fractions. Find the constants by substituting convenient values of $x$ (the roots of the factors) and by comparing coefficients of powers of $x$ for what is left.
5. Integrate term by term. Use $\int \frac{A}{x - a}\,dx = A\ln\lvert x - a \rvert$, $\int \frac{A}{(x - a)^k}\,dx = \frac{A(x - a)^{1-k}}{1 - k}$ for $k \ge 2$, and for a quadratic term split it into a multiple of the derivative of the denominator (a logarithm) and a constant over a sum of squares (an arctangent after completing the square).
6. Check by putting the sum back over a common denominator, or by comparing both sides at one value of $x$.

*Theorem 1 (distinct linear factors).* Let $P$ be a polynomial of degree less than $n$, and let $Q(x) = (x - a_1)(x - a_2)\cdots(x - a_n)$ with the numbers $a_i$ all different. Then

$$
\frac{P(x)}{Q(x)} = \sum_{i=1}^{n}\frac{A_i}{x - a_i}, \qquad A_i = \frac{P(a_i)}{Q'(a_i)}.
$$

In plain words, the constant for the factor $x - a_i$ is the numerator evaluated at $a_i$, divided by what is left of the denominator after covering up that factor and putting in $x = a_i$. This is the "cover-up" shortcut.

We know that a nonzero polynomial of degree at most $m$ has at most $m$ roots (a consequence of the factor theorem from the [remainder theorem lesson](../../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md)), and the product rule. We want to show that the sum of fractions equals $\frac{P}{Q}$. The plan is to build a polynomial from the proposed constants, show that it takes the same values as $P$ at $n$ points, and conclude that it equals $P$.

*Proof.* Let $Q_i(x) = \frac{Q(x)}{x - a_i}$, the product of all the factors except the $i$-th. It is a polynomial of degree $n - 1$, and $Q_i(a_j) = 0$ for $j \ne i$, since $x - a_j$ is one of its factors. By the product rule applied to $Q(x) = (x - a_i)Q_i(x)$, we have $Q'(x) = Q_i(x) + (x - a_i)Q_i'(x)$, so $Q'(a_i) = Q_i(a_i)$, which is nonzero because the $a$'s are distinct. Define $L(x) = \sum_{i}A_i\,Q_i(x)$ with $A_i = \frac{P(a_i)}{Q'(a_i)}$. At $x = a_j$ every term but one vanishes, so $L(a_j) = A_j\,Q_j(a_j) = \frac{P(a_j)}{Q'(a_j)}Q'(a_j) = P(a_j)$. So $P - L$ has degree at most $n - 1$ and has $n$ roots $a_1, \dots, a_n$, which forces $P - L = 0$. Hence $P = L$, and dividing by $Q$ gives $\frac{P}{Q} = \sum_i\frac{A_i\,Q_i}{Q} = \sum_i\frac{A_i}{x - a_i}$. $\blacksquare$

Look back: the proof is Lagrange interpolation in disguise. It explains why the substitution trick works: putting $x = a_i$ in the cleared equation kills every term except one. For repeated factors and irreducible quadratics the same form exists and is unique, a fact from algebra that this book accepts. The cover-up shortcut gives only the highest-power coefficient of a repeated factor, so the other coefficients come from other values of $x$ or from comparing coefficients, as in Example 2.

### Improper integrals

1. Identify the problem: an infinite limit, or a point where the integrand is unbounded. If the problem is inside the interval, split there.
2. Replace the problem by a variable ($b$ for $\infty$, $t$ for a bad endpoint), and find the ordinary integral over the shorter interval, usually by the fundamental theorem.
3. Take the limit of the result as the variable tends to the problem. Don't substitute $\infty$ into the antiderivative, since $\infty$ is not a number.
4. If the limit is finite, the integral converges to it. If the limit is infinite or doesn't exist, it diverges.

*Theorem 2 (the $p$ test).* For $p$ a real number:

- $\displaystyle\int_1^\infty\frac{dx}{x^p}$ converges when $p > 1$, with value $\dfrac{1}{p - 1}$, and diverges when $p \le 1$.
- $\displaystyle\int_0^1\frac{dx}{x^p}$ converges when $p < 1$, with value $\dfrac{1}{1 - p}$, and diverges when $p \ge 1$.

We know the power rule for antiderivatives and the behaviour of $b^{s}$ as $b \to \infty$: it tends to 0 for $s < 0$ and to infinity for $s > 0$. We want to find which exponents give a finite limit. The plan is to compute the integral to a moving endpoint, and take the limit separately for $p = 1$ and $p \ne 1$.

*Proof.* For the first integral and $p \ne 1$, $\int_1^b x^{-p}\,dx = \frac{b^{1-p} - 1}{1 - p}$. If $p > 1$ the exponent $1 - p$ is negative, $b^{1-p} \to 0$, and the limit is $\frac{-1}{1 - p} = \frac{1}{p - 1}$. If $p < 1$ the exponent is positive, $b^{1-p} \to \infty$, and the integral diverges. If $p = 1$, $\int_1^b\frac{dx}{x} = \ln b \to \infty$, which diverges. For the second integral and $p \ne 1$, $\int_t^1 x^{-p}\,dx = \frac{1 - t^{1-p}}{1 - p}$. If $p < 1$, then $t^{1-p} \to 0$ as $t \to 0^+$ and the limit is $\frac{1}{1 - p}$. If $p > 1$, then $t^{1-p} \to \infty$ and the integral diverges. If $p = 1$, $\int_t^1\frac{dx}{x} = -\ln t \to \infty$. $\blacksquare$

Look back: the borderline is $p = 1$ and it diverges both times. The two cases have opposite thresholds, because near infinity a bigger $p$ makes the tail smaller, and near 0 a bigger $p$ makes the spike taller. A way to remember: $\frac{1}{x^p}$ with $p > 1$ is "small at infinity", and with $p < 1$ is "small at 0". The other end of each interval is harmless, since $x^{-p}$ is continuous on $[1, b]$ and on $[t, 1]$. The thresholds are the same ones used for infinite series in [convergence tests](../05-sequences-and-series/03-convergence-tests.md).

*Theorem 3 (comparison).* Suppose $0 \le f(x) \le g(x)$ for $x \ge a$, and both are continuous. If $\int_a^\infty g$ converges, then $\int_a^\infty f$ converges and is at most $\int_a^\infty g$. If $\int_a^\infty f$ diverges, then $\int_a^\infty g$ diverges.

In plain words, a function squeezed under a convergent one has finite area, and a function above a divergent one has infinite area. The reason is that $\int_a^b f$ never decreases as $b$ grows (since $f \ge 0$) and is bounded by $\int_a^\infty g$, and a non-decreasing function bounded above has a limit, a fact about the real numbers that this book accepts. The same statement holds for integrals with a bad endpoint.

## Worked examples

<div class="example" markdown>

### Example 1: distinct linear factors

Find $\int\frac{3x + 5}{(x - 1)(x + 2)}\,dx$.

Step 1: the numerator has degree 1 and the denominator has degree 2, so the fraction is proper. Step 2: the denominator is already factored, with two different linear factors. Step 3: $\frac{3x + 5}{(x - 1)(x + 2)} = \frac{A}{x - 1} + \frac{B}{x + 2}$. Step 4: clear the denominators, $3x + 5 = A(x + 2) + B(x - 1)$. At $x = 1$, $8 = 3A$, so $A = \frac{8}{3}$. At $x = -2$, $-1 = -3B$, so $B = \frac{1}{3}$. (The cover-up rule agrees: $A = \frac{P(1)}{Q'(1)} = \frac{8}{3}$, since $Q'(x) = 2x + 1$.) Step 5:

$$
\int\left(\frac{8/3}{x - 1} + \frac{1/3}{x + 2}\right)dx = \frac{8}{3}\ln\lvert x - 1 \rvert + \frac{1}{3}\ln\lvert x + 2 \rvert + C.
$$

Step 6, the check: at $x = 0$ the original fraction is $\frac{5}{(-1)(2)} = -2.5$, and the decomposition gives $\frac{8/3}{-1} + \frac{1/3}{2} = -\frac{8}{3} + \frac{1}{6} = -2.5$. Also the coefficients of the logs, $\frac{8}{3}$ and $\frac{1}{3}$, add to 3, the leading coefficient of the numerator, which is the behaviour of the fraction for large $x$, close to $\frac{3}{x}$.

</div>

<div class="example" markdown>

### Example 2: a repeated factor

Find $\int\frac{dx}{(x - 1)^2(x + 1)}$.

The denominator has the factor $(x - 1)$ twice, so the form needs both powers: $\frac{1}{(x - 1)^2(x + 1)} = \frac{A}{x - 1} + \frac{B}{(x - 1)^2} + \frac{C}{x + 1}$. Clearing denominators, $1 = A(x - 1)(x + 1) + B(x + 1) + C(x - 1)^2$.

At $x = 1$: $1 = 2B$, so $B = \frac{1}{2}$. At $x = -1$: $1 = 4C$, so $C = \frac{1}{4}$. These are the two values that kill terms. For $A$, compare the coefficients of $x^2$ on both sides: $0 = A + C$, so $A = -\frac{1}{4}$. Then

$$
\int\left(-\frac{1/4}{x - 1} + \frac{1/2}{(x - 1)^2} + \frac{1/4}{x + 1}\right)dx = -\frac{1}{4}\ln\lvert x - 1 \rvert - \frac{1}{2(x - 1)} + \frac{1}{4}\ln\lvert x + 1 \rvert + C.
$$

Check: at $x = 2$ the fraction is $\frac{1}{1 \cdot 3} = \frac{1}{3}$, and the decomposition gives $-\frac{1}{4} + \frac{1}{2} + \frac{1}{12} = \frac{-3 + 6 + 1}{12} = \frac{1}{3}$. The antiderivative of the repeated term used $\int (x - 1)^{-2}\,dx = -(x - 1)^{-1}$, which has no logarithm: a repeated factor adds a power term and not a new log.

</div>

<div class="example" markdown>

### Example 3: an irreducible quadratic

Find $\int\frac{3x + 2}{(x + 1)\left(x^2 + 4\right)}\,dx$.

The quadratic $x^2 + 4$ has no real roots, so the form is $\frac{3x + 2}{(x + 1)(x^2 + 4)} = \frac{A}{x + 1} + \frac{Bx + C}{x^2 + 4}$. Clear the denominators: $3x + 2 = A\left(x^2 + 4\right) + (Bx + C)(x + 1)$. At $x = -1$: $-1 = 5A$, so $A = -\frac{1}{5}$. Compare the coefficients of $x^2$: $0 = A + B$, so $B = \frac{1}{5}$. Compare the constant terms: $2 = 4A + C$, so $C = 2 + \frac{4}{5} = \frac{14}{5}$.

Split the quadratic term into a log part and an arctangent part: $\frac{(1/5)x + 14/5}{x^2 + 4} = \frac{1}{10}\cdot\frac{2x}{x^2 + 4} + \frac{14}{5}\cdot\frac{1}{x^2 + 4}$. With $\int\frac{2x}{x^2 + 4}\,dx = \ln\left(x^2 + 4\right)$ and $\int\frac{dx}{x^2 + 4} = \frac{1}{2}\arctan\frac{x}{2}$,

$$
\int\frac{3x + 2}{(x + 1)(x^2 + 4)}\,dx = -\frac{1}{5}\ln\lvert x + 1 \rvert + \frac{1}{10}\ln\left(x^2 + 4\right) + \frac{7}{5}\arctan\frac{x}{2} + C.
$$

Check: the coefficient of $x$ in the numerator, 3, must equal the $x$-coefficient of the expanded right side, $B + C = \frac{1}{5} + \frac{14}{5} = 3$. And at $x = 0$ the fraction is $\frac{2}{1 \cdot 4} = 0.5$, while the decomposition gives $-\frac{1}{5} + \frac{14/5}{4} = -0.2 + 0.7 = 0.5$.

</div>

<div class="example" markdown>

### Example 4: an infinite interval, with partial fractions

Evaluate $\int_1^\infty\frac{dx}{x(x + 1)}$.

Decompose: $\frac{1}{x(x + 1)} = \frac{1}{x} - \frac{1}{x + 1}$ (at $x = 0$: $A = 1$; at $x = -1$: $B = -1$). Then, with the limit replacing $\infty$,

$$
\int_1^b\left(\frac{1}{x} - \frac{1}{x + 1}\right)dx = \Bigl[\ln x - \ln(x + 1)\Bigr]_1^b = \ln\frac{b}{b + 1} - \ln\frac{1}{2} = \ln\frac{2b}{b + 1}.
$$

As $b \to \infty$, $\frac{2b}{b + 1} \to 2$, so the integral converges to $\ln 2 \approx 0.6931$.

Check: the integrand is positive, so the integral to $b$ should increase with $b$: for $b = 10$ it is $\ln\frac{20}{11} = 0.598$, for $b = 100$ it is $0.683$, and for $b = 10{,}000$ it is $0.69305$, approaching $0.69315$. Compare with the $p$ test: the integrand is less than $\frac{1}{x^2}$ for $x \ge 1$, and $\int_1^\infty\frac{dx}{x^2} = 1$, so convergence was expected, and the value $0.69$ is below 1, as the comparison says.

Notice what is happening in the integrand $\frac{1}{x} - \frac{1}{x + 1}$: each piece alone diverges, since $\int_1^\infty\frac{dx}{x}$ is infinite, and the difference converges. Always take the limit of the whole expression and not of the pieces.

</div>

<div class="example" markdown>

### Example 5: an unbounded integrand and a trap

Evaluate $\int_0^1\ln x\,dx$ and decide whether $\int_{-1}^{1}\frac{dx}{x}$ converges.

The function $\ln x$ is unbounded near 0, so use a limit from the right: $\int_t^1\ln x\,dx = \bigl[x\ln x - x\bigr]_t^1 = -1 - (t\ln t - t)$. As $t \to 0^+$, $t \to 0$ and $t\ln t \to 0$ (by the limit $\lim_{t \to 0^+}t\ln t = 0$, which is [L'Hopital's rule](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md) applied to $\frac{\ln t}{1/t}$). So the integral converges to $-1$.

For $\int_{-1}^{1}\frac{dx}{x}$, the problem is at the interior point 0, so split: $\int_{-1}^{0}\frac{dx}{x} + \int_{0}^{1}\frac{dx}{x}$. The second piece is the case $p = 1$ of the $p$ test and diverges, so the whole integral diverges, even though the function is odd and the areas on the two sides look as if they should cancel. Both sides are infinite, and $\infty - \infty$ is not 0. The symmetric formula $\lim_{\varepsilon \to 0^+}\left(\int_{-1}^{-\varepsilon} + \int_{\varepsilon}^{1}\right) = 0$ is a different quantity (the principal value) and isn't the integral.

Check: $\ln x$ is negative on $(0, 1)$, so a negative answer is right, and $-1$ is the negative of $\int_0^1\ln\frac{1}{x}\,dx$, an area that is finite because $\ln\frac{1}{x}$ grows more slowly than any $\frac{1}{x^p}$ with $p > 0$.

</div>

<div class="example" markdown>

### Example 6: the exponential density

A waiting time $X$ (in seconds) for the next request at a server has density $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$, and $f(x) = 0$ for $x < 0$, with rate $\lambda = 0.5$ per second (a hypothetical value). Check that the total area is 1, and find $P(X > 3)$ and $P(1 < X < 3)$.

Total area: $\int_0^b 0.5\,e^{-0.5x}\,dx = \bigl[-e^{-0.5x}\bigr]_0^b = 1 - e^{-0.5b}$, which tends to 1 as $b \to \infty$. So $f$ is a density. (The left half, $x < 0$, adds 0.)

Then $P(X > 3) = \int_3^\infty 0.5\,e^{-0.5x}\,dx = \lim_{b \to \infty}\bigl(e^{-1.5} - e^{-0.5b}\bigr) = e^{-1.5} \approx 0.2231$. And $P(1 < X < 3) = \int_1^3 0.5\,e^{-0.5x}\,dx = e^{-0.5} - e^{-1.5} \approx 0.6065 - 0.2231 = 0.3834$.

Check: in general $P(X > t) = e^{-\lambda t}$, which equals 1 at $t = 0$ (every waiting time is positive) and falls towards 0. The probabilities $P(X \le 1) = 0.3935$, $P(1 < X < 3) = 0.3834$ and $P(X > 3) = 0.2231$ add to 1.

</div>

<div class="example" markdown>

### Example 7: a limit at infinity with parts (finish it yourself)

Evaluate $\int_0^\infty x\,e^{-x}\,dx$. Integration by parts with $u = x$ and $dv = e^{-x}\,dx$ gives the antiderivative $-(x + 1)e^{-x}$ (check it by differentiating). Evaluate from 0 to $b$, and take the limit as $b \to \infty$, using $\lim_{b \to \infty}b\,e^{-b} = 0$.

<details class="solution" markdown>
<summary>Finish</summary>

The integral up to $b$ is $\int_0^b x\,e^{-x}\,dx = \bigl[-(x + 1)e^{-x}\bigr]_0^b = -(b + 1)e^{-b} + 1$. As $b \to \infty$, both $b\,e^{-b}$ and $e^{-b}$ tend to 0 (the first by [L'Hopital's rule](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md) on $\frac{b}{e^b}$, since an exponential beats a power). So the integral converges to $1$.

Check: the antiderivative's derivative is $-e^{-x} + (x + 1)e^{-x} = x\,e^{-x}$. A numerical sum of $x\,e^{-x}$ on $[0, 40]$ with 100,000 rectangles gives $1.0000$. This is also the mean $\frac{1}{\lambda}$ of the exponential density with $\lambda = 1$, which the next lesson derives for every $\lambda$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: divide first when the fraction is improper. The form $\frac{A}{x - 1} + \frac{B}{x + 1}$ can't produce $\frac{x^2 + 1}{x^2 - 1}$, because for large $x$ that form tends to 0 while the fraction tends to 1. Do the division, $\frac{x^2 + 1}{x^2 - 1} = 1 + \frac{2}{x^2 - 1}$, and decompose the remainder.

</div>

<div class="warning" markdown>

Watch out: a repeated factor needs a term for each power. For $(x - 1)^2$ the form is $\frac{A}{x - 1} + \frac{B}{(x - 1)^2}$, and with only $\frac{A}{(x - 1)^2}$ the system of equations has no solution. A quadratic factor needs a linear numerator, $Bx + C$ and not just $B$.

</div>

<div class="warning" markdown>

Watch out: never substitute $\infty$ into an antiderivative. Write the limit. The antiderivative $-\frac{1}{x}$ of $\frac{1}{x^2}$ at "infinity" is $0$ only because $\lim_{b \to \infty}\left(-\frac{1}{b}\right) = 0$, and the step must be written down, especially when the answer is a difference of two terms that each go to infinity, as in Example 4.

</div>

<div class="warning" markdown>

Watch out: the integrand tending to 0 does not make an infinite integral converge. The function $\frac{1}{x}$ tends to 0 and its integral from 1 to infinity diverges. The $p$ test says how fast is fast enough: faster than $\frac{1}{x}$. And the thresholds for the two types of improper integral go in opposite directions: $\int_1^\infty\frac{dx}{x^p}$ needs $p > 1$, $\int_0^1\frac{dx}{x^p}$ needs $p < 1$.

</div>

Finite area under an infinite curve is not a paradox. Under $\frac{1}{x^2}$ from 1 to infinity the area is 1, in the same way that $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots = 1$ is a sum of infinitely many positive terms with a finite total. The boundary of what gives a finite total is the same: $\frac{1}{x}$ and the harmonic series both diverge.

For $\int_{-\infty}^{\infty}$ you may not use $\lim_{R \to \infty}\int_{-R}^{R}$ as the definition. With $f(x) = x$ the symmetric integral is $0$ for every $R$, but $\int_0^\infty x\,dx$ diverges, so $\int_{-\infty}^{\infty}x\,dx$ does too. Split at a point and require both halves to converge.

## Tricks and shortcuts

For distinct linear factors use cover-up: to find the constant over $(x - a)$, cover that factor with your finger in the original fraction and put $x = a$ into what is left. In $\frac{3x + 5}{(x - 1)(x + 2)}$, cover $(x - 1)$ and evaluate $\frac{3x + 5}{x + 2}$ at 1 to get $\frac{8}{3}$. This is Theorem 1.

A difference of squares in the denominator is a common case: $\frac{1}{x^2 - a^2} = \frac{1}{2a}\left(\frac{1}{x - a} - \frac{1}{x + a}\right)$, so $\int\frac{dx}{x^2 - a^2} = \frac{1}{2a}\ln\left\lvert\frac{x - a}{x + a}\right\rvert + C$. For $a = 2$, $\frac{1}{x^2 - 4} = \frac{1}{4}\left(\frac{1}{x - 2} - \frac{1}{x + 2}\right)$.

Comparison is the quickest way to decide convergence without finding the antiderivative. Compare with a $p$-integral: for large $x$, $\frac{1}{x^2 + x}$ is less than $\frac{1}{x^2}$, so $\int_1^\infty\frac{dx}{x^2 + x}$ converges. A function that looks like $\frac{1}{x^p}$ for large $x$ converges exactly when $p > 1$. Check the estimate before computing, since a divergent integral gives a "limit" of infinity that is easy to miss when you substitute without thinking.

To check any partial fraction decomposition, add the pieces back up, or compare at one value of $x$ that isn't a root of the denominator (Examples 1 to 3).

## In code

The partial sums of an improper integral show convergence or divergence. For $\int_1^b\frac{dx}{x^2} = 1 - \frac{1}{b}$ the integral settles near 1, and for $\int_1^b\frac{dx}{x} = \ln b$ it keeps growing, slowly. The code also checks Example 4 and the exponential density, using exact antiderivatives so that the loop runs fast.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

# Areas up to b: 1/x^2 settles down, 1/x keeps growing (slowly).
print("       b   int 1/x^2   int 1/x")
for b in (10, 1_000, 100_000, 10_000_000):
    print(f"{b:8d}   {1 - 1 / b:.6f}   {math.log(b):.4f}")
#        b   int 1/x^2   int 1/x
#       10   0.900000   2.3026
#     1000   0.999000   6.9078
#   100000   0.999990   11.5129
# 10000000   1.000000   16.1181

# Example 4: the integral of 1/(x(x+1)) from 1 to b is ln(2b/(b+1)), tending to ln 2.
for b in (10, 100, 10_000):
    print(b, round(math.log(2 * b / (b + 1)), 5))
print(round(math.log(2), 5))
# 10 0.59784
# 100 0.6832
# 10000 0.69305
# 0.69315

# Example 6: exponential density with rate 0.5.
lam = 0.5
tail = lambda t: math.exp(-lam * t)          # P(X > t)
print(round(tail(3), 4), round(tail(1) - tail(3), 4), round(tail(0), 4))
# 0.2231 0.3834 1.0
```

</details>

After ten million units the area under $\frac{1}{x}$ is only $16.1$, and it still doesn't level off. This is why a numerical estimate alone can't prove divergence, and why the limit has to be taken by algebra.

## FAQ

### Why do we need the form $Bx + C$ over an irreducible quadratic?

Because the numerator of a fraction can have one degree less than its denominator and still be a general polynomial of that degree. A quadratic denominator allows a linear numerator, $Bx + C$. With a constant alone there are not enough unknowns to match every numerator. For a linear denominator, a numerator of degree 0 is a constant, so $A$ alone is enough. In general the unknown constants in the form number exactly the degree of the denominator, which matches the unknown coefficients of a numerator of lower degree.

### Does every rational function have a partial fraction decomposition?

Yes, over the real numbers, if you allow irreducible quadratics. Every real polynomial factors into real linear factors and irreducible real quadratics, and then the decomposition exists and is unique. Finding the factorization is the hard part, and for degree 5 and higher there is no general formula for the roots, but for textbook problems the factors are given or easy.

### How can an infinite region have finite area?

The region is infinitely long but is also getting thin. Under $\frac{1}{x^2}$ from 1 to infinity, the strip between $x = n$ and $x = n + 1$ has area less than $\frac{1}{n^2}$, and these areas add up to a finite number. The result depends on how fast the height shrinks, which is what the $p$ test measures. For $\frac{1}{x}$ the strips shrink too slowly, and their areas, about $\frac{1}{n}$, add up like the harmonic series.

### Is the integral of a probability density always 1?

For a density, yes, by definition: the probability that $X$ takes some value is 1. This is the reason for the normalising constants in the formulas, such as the $\lambda$ in $\lambda e^{-\lambda x}$ and the $\frac{1}{\sqrt{2\pi}}$ in the standard normal density $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}$. The normal density needs $\int_{-\infty}^{\infty}e^{-x^2/2}\,dx = \sqrt{2\pi}$, a value that can't be found with the techniques of this chapter, and is found in a multivariable calculus course by using a double integral.

## Practice

### Warm-up

1\. Decompose and integrate: (a) $\frac{x + 7}{(x + 1)(x - 2)}$ and (b) $\frac{1}{x^2 - 4}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\frac{x + 7}{(x + 1)(x - 2)} = \frac{A}{x + 1} + \frac{B}{x - 2}$, so $x + 7 = A(x - 2) + B(x + 1)$. At $x = 2$: $9 = 3B$, so $B = 3$. At $x = -1$: $6 = -3A$, so $A = -2$. The integral is $-2\ln\lvert x + 1 \rvert + 3\ln\lvert x - 2 \rvert + C$.

(b) $\frac{1}{(x - 2)(x + 2)} = \frac{A}{x - 2} + \frac{B}{x + 2}$, so $1 = A(x + 2) + B(x - 2)$. At $x = 2$: $A = \frac{1}{4}$. At $x = -2$: $B = -\frac{1}{4}$. The integral is $\frac{1}{4}\ln\left\lvert\frac{x - 2}{x + 2}\right\rvert + C$.

Check (a) at $x = 0$: the fraction is $\frac{7}{-2} = -3.5$, and $\frac{-2}{1} + \frac{3}{-2} = -2 - 1.5 = -3.5$. Check (b) at $x = 0$: the fraction is $-\frac{1}{4}$, and $\frac{1/4}{-2} + \frac{-1/4}{2} = -\frac{1}{8} - \frac{1}{8} = -\frac{1}{4}$.

</details>

2\. Evaluate or show divergence: (a) $\int_1^\infty x^{-3}\,dx$, (b) $\int_0^4\frac{dx}{\sqrt{x}}$ and (c) $\int_1^\infty\frac{dx}{\sqrt{x}}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The $p$ test with $p = 3$: $\frac{1}{3 - 1} = \frac{1}{2}$. (b) The singularity is at 0 with $p = \frac{1}{2} < 1$, so it converges: $\int_t^4 x^{-1/2}\,dx = 2\sqrt{4} - 2\sqrt{t} = 4 - 2\sqrt{t} \to 4$. (c) With $p = \frac{1}{2} \le 1$ at infinity, $\int_1^b x^{-1/2}\,dx = 2\sqrt{b} - 2 \to \infty$, so it diverges.

Check (a): $\int_1^b x^{-3}\,dx = \frac{1}{2}\left(1 - b^{-2}\right)$, which is $0.495$ for $b = 10$ and approaches $\frac{1}{2}$. Check (c): at $b = 10^6$ the value is $1998$ and still growing.

</details>

3\. Evaluate if convergent: (a) $\int_0^\infty e^{-2x}\,dx$, (b) $\int_{-\infty}^{0}e^{x}\,dx$ and (c) $\int_0^\infty\cos x\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\int_0^b e^{-2x}\,dx = \frac{1 - e^{-2b}}{2} \to \frac{1}{2}$. (b) $\int_t^0 e^x\,dx = 1 - e^t \to 1$ as $t \to -\infty$. (c) $\int_0^b\cos x\,dx = \sin b$, which oscillates between $-1$ and 1 and has no limit, so the integral diverges. It is not infinite, it just doesn't settle.

Check (a): the integrand starts at 2 and falls quickly, so an area of $\frac{1}{2}$ is plausible. (b) is the same picture reflected. For (c), $\sin b$ at $b = \frac{\pi}{2}$ is 1 and at $b = \frac{3\pi}{2}$ is $-1$.

</details>

### Standard

4\. Find $\int\frac{x^3 + 2}{x^2 - 1}\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

The degree of the numerator exceeds that of the denominator, so divide first: $x^3 + 2 = x\left(x^2 - 1\right) + (x + 2)$, so $\frac{x^3 + 2}{x^2 - 1} = x + \frac{x + 2}{(x - 1)(x + 1)}$. Decompose the remainder, $\frac{x + 2}{(x - 1)(x + 1)} = \frac{A}{x - 1} + \frac{B}{x + 1}$. At $x = 1$: $3 = 2A$, so $A = \frac{3}{2}$. At $x = -1$: $1 = -2B$, so $B = -\frac{1}{2}$. Then

$$
\int\left(x + \frac{3/2}{x - 1} - \frac{1/2}{x + 1}\right)dx = \frac{x^2}{2} + \frac{3}{2}\ln\lvert x - 1 \rvert - \frac{1}{2}\ln\lvert x + 1 \rvert + C.
$$

Check: at $x = 2$ the original is $\frac{10}{3} = 3.3333$, and the pieces give $2 + \frac{3}{2} - \frac{1}{6} = 3.3333$.

</details>

5\. Find $\int\frac{dx}{x\left(x^2 + 1\right)}$ and then evaluate $\int_1^\infty\frac{dx}{x\left(x^2 + 1\right)}$.

<details class="solution" markdown>
<summary>Solution</summary>

Write $\frac{1}{x(x^2 + 1)} = \frac{A}{x} + \frac{Bx + C}{x^2 + 1}$. Clearing, $1 = A\left(x^2 + 1\right) + (Bx + C)x$. At $x = 0$: $A = 1$. The $x^2$ terms give $0 = A + B$, so $B = -1$, and the $x$ terms give $0 = C$. So the fraction is $\frac{1}{x} - \frac{x}{x^2 + 1}$ and

$$
\int\frac{dx}{x(x^2 + 1)} = \ln\lvert x \rvert - \frac{1}{2}\ln\left(x^2 + 1\right) + C = \ln\frac{\lvert x \rvert}{\sqrt{x^2 + 1}} + C.
$$

For the improper integral, $\bigl[\ln\frac{x}{\sqrt{x^2 + 1}}\bigr]_1^b = \ln\frac{b}{\sqrt{b^2 + 1}} - \ln\frac{1}{\sqrt{2}}$. As $b \to \infty$, $\frac{b}{\sqrt{b^2 + 1}} \to 1$ and the first log tends to 0. So the value is $\ln\sqrt{2} = \frac{1}{2}\ln 2 \approx 0.3466$.

Check: the integrand is less than $\frac{1}{x^3}$ for $x \ge 1$, and $\int_1^\infty x^{-3}\,dx = \frac{1}{2}$, so the value should be below $0.5$, and it is.

</details>

6\. (Reviews [polynomial division](../../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md).) Divide to evaluate $\int\frac{x^2 + 1}{x + 1}\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

Dividing $x^2 + 1$ by $x + 1$: the quotient is $x - 1$ and the remainder is 2, since $(x + 1)(x - 1) + 2 = x^2 + 1$. So $\frac{x^2 + 1}{x + 1} = x - 1 + \frac{2}{x + 1}$, and the integral is $\frac{x^2}{2} - x + 2\ln\lvert x + 1 \rvert + C$.

Check: the remainder 2 is the value of $x^2 + 1$ at $x = -1$, as the remainder theorem says. Differentiating the answer gives $x - 1 + \frac{2}{x + 1}$, which is the quotient plus the remainder over the divisor.

</details>

### Challenge

7\. Decide whether each converges, by comparison with a $p$-integral: (a) $\int_1^\infty\frac{2 + \sin x}{x^2}\,dx$ and (b) $\int_2^\infty\frac{dx}{\sqrt{x^2 - 1}}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Since $-1 \le \sin x \le 1$, we have $0 < \frac{2 + \sin x}{x^2} \le \frac{3}{x^2}$. The integral $\int_1^\infty\frac{3}{x^2}\,dx = 3$ converges, so by comparison the integral in (a) converges, and its value is at most 3.

(b) For $x \ge 2$, $\sqrt{x^2 - 1} < x$, so $\frac{1}{\sqrt{x^2 - 1}} > \frac{1}{x}$. The integral $\int_2^\infty\frac{dx}{x}$ diverges ($p = 1$), so by comparison the integral in (b) diverges.

Check: (a) the value is between $\int_1^\infty\frac{dx}{x^2} = 1$ and 3, and a numerical value is about $2.504$. For (b), the integral to $b$ is $\ln\left(b + \sqrt{b^2 - 1}\right) - \ln\left(2 + \sqrt{3}\right)$, which grows like $\ln 2b$ and not toward a limit.

</details>

8\. For the exponential density $f(x) = \lambda e^{-\lambda x}$ with $\lambda = 0.5$, find the median $m$, the value with $P(X > m) = \frac{1}{2}$. Compare it with the mean $\frac{1}{\lambda} = 2$ (derived in the next lesson).

<details class="solution" markdown>
<summary>Solution</summary>

We know $P(X > t) = e^{-\lambda t}$ from the integral over $[t, \infty)$. Set $e^{-0.5m} = \frac{1}{2}$. Taking logs, $-0.5m = -\ln 2$, so $m = 2\ln 2 \approx 1.386$.

The median 1.386 is below the mean 2. The density has a long right tail, so a few large waiting times pull the mean above the median, and half the waits are shorter than 1.386 s even though the average wait is 2 s.

Check: $e^{-0.5 \cdot 1.386} = e^{-0.693} = 0.5$. And $P(X > 2) = e^{-1} = 0.368$, so fewer than half of the waits exceed the mean, which agrees with the median being below it.

</details>

## Where this shows up

- The last lesson of the chapter, [applications of integrals](06-applications-of-integrals.md), uses improper integrals for expected values of continuous variables and for the present value of a payment stream that never ends. [Convergence tests](../05-sequences-and-series/03-convergence-tests.md) uses the $p$ test again, through the integral test for infinite series.
- In CS, the logistic function $\sigma(z) = \frac{1}{1 + e^{-z}}$ satisfies $\frac{d\sigma}{dz} = \sigma(1 - \sigma)$, so $\int\frac{dp}{p(1 - p)} = z$, and the partial fractions $\frac{1}{p(1 - p)} = \frac{1}{p} + \frac{1}{1 - p}$ give $\ln\frac{p}{1 - p} = z$, the inverse of the sigmoid, called the logit and used in logistic regression. Heavy-tailed distributions in networks and algorithms are those whose densities fall like $\frac{1}{x^p}$ with $p$ not much above 1, where the $p$ test decides whether the mean exists. The same decomposition idea is how rational generating functions are expanded in the analysis of recurrences.
- In probability and economics, densities integrate to 1 over an infinite range (continuous random variables and the normal distribution<!-- link: ../07-probability/04-continuous-random-variables-and-the-normal.md -->), and a perpetuity, a payment stream with no end date, has a finite present value for the same reason $\int_0^\infty e^{-rt}\,dt$ converges (present value, NPV and bond prices<!-- link: ../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md -->).
