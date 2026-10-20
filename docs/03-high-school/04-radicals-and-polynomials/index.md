# Radicals and polynomials

Roots and fractional powers, then polynomials: arithmetic, factoring, division, zeros and graphs.

1. [Radicals and rational exponents](01-radicals-and-rational-exponents.md)
2. [Polynomial arithmetic](02-polynomial-arithmetic.md)
3. [Factoring polynomials](03-factoring-polynomials.md)
4. [Polynomial division and the remainder theorem](04-polynomial-division-and-remainder-theorem.md)
5. [Polynomial functions and graphs](05-polynomial-functions-and-graphs.md)

## Cheat sheet

### Radicals and rational exponents

An $n$-th root of $a$ is a number $b$ with $b^n = a$. The principal root $\sqrt[n]{a}$ is the real root for odd $n$, and the non-negative root for even $n$ and $a \ge 0$. An even root of a negative number is not real.

| Expression | Meaning | Example |
|---|---|---|
| $a^{1/n}$ | $\sqrt[n]{a}$ | $64^{1/3} = 4$ |
| $a^{m/n}$ | $\left(\sqrt[n]{a}\right)^m$, root first | $27^{2/3} = 9$ |
| $a^{-m/n}$ | $\dfrac{1}{a^{m/n}}$ | $16^{-3/4} = \dfrac{1}{8}$ |
| $\sqrt[n]{a^n}$ | $a$ for odd $n$, $\lvert a \rvert$ for even $n$ | $\sqrt{(-3)^2} = 3$ |

- Product and quotient rules: $\sqrt[n]{ab} = \sqrt[n]{a}\sqrt[n]{b}$ and $\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}$ (for even $n$, with $a, b \ge 0$). There is no rule for a sum.
- To simplify, divide each exponent in the radicand by the index: the quotient comes out and the remainder stays. For $\sqrt{50x^6y^3}$ with $y \ge 0$ the answer is $5\lvert x^3 \rvert y\sqrt{2y}$.
- Only radicals with the same index and radicand add: $\sqrt{75} - 2\sqrt{12} + \sqrt{27} = 4\sqrt{3}$.
- Rationalize $\frac{a}{\sqrt{b}}$ by multiplying top and bottom by $\sqrt{b}$. For $\frac{1}{\sqrt{3} - 1}$, multiply by the conjugate $\sqrt{3} + 1$ to get $\frac{\sqrt{3} + 1}{2}$.
- Average growth rate over $n$ periods: $\left(\frac{\text{end}}{\text{start}}\right)^{1/n} - 1$.

Main mistakes:

- Writing $\sqrt{x^2} = x$. It is $\lvert x \rvert$.
- Splitting a sum: $\sqrt{x^2 + 9} \ne x + 3$.
- Reading $8^{2/3}$ as $\frac{8^2}{3}$. The denominator is the index.
- Using a negative base with a fractional exponent that isn't in lowest terms with an odd denominator.

### Polynomial arithmetic

A polynomial in standard form is $a_nx^n + \cdots + a_1x + a_0$ with $a_n \ne 0$: degree $n$, leading coefficient $a_n$, constant term $a_0$. Exponents are whole numbers, so $\sqrt{x}$ and $\frac{1}{x}$ are not polynomials.

| Special product | Result |
|---|---|
| $(a + b)^2$ | $a^2 + 2ab + b^2$ |
| $(a - b)^2$ | $a^2 - 2ab + b^2$ |
| $(a + b)(a - b)$ | $a^2 - b^2$ |
| $(a + b)^3$ | $a^3 + 3a^2b + 3ab^2 + b^3$ |

- Add or subtract by combining like terms. Subtracting changes the sign of every term of the second polynomial.
- Multiply by distributing every term, or with a box. Multiply coefficients and add exponents.
- $\deg(pq) = \deg p + \deg q$. The degree of a sum is at most the larger degree.
- Checks: the value at $x = 1$ is the sum of the coefficients, and values at $x = 2$ multiply.
- Horner's method: $2x^3 - 6x^2 + 2x - 1 = ((2x - 6)x + 2)x - 1$, with $n$ multiplications for degree $n$.

Main mistakes: $(a + b)^2 \ne a^2 + b^2$; forgetting to flip every sign when subtracting; adding exponents when adding like terms ($x^2 + x^2 = 2x^2$, not $x^4$).

### Factoring polynomials

Checklist: (1) take out the GCF, and a $-1$ if the leading coefficient is negative; (2) count terms; (3) factor each factor again; (4) check by expanding.

| Terms | Look for |
|---|---|
| 2 | $a^2 - b^2 = (a - b)(a + b)$; $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$ |
| 3 | $a^2 \pm 2ab + b^2 = (a \pm b)^2$; $x^2 + bx + c = (x + r)(x + s)$ with $rs = c$, $r + s = b$ |
| 3, $a \ne 1$ | ac method: $mn = ac$, $m + n = b$, split $bx$, group |
| 4 | grouping |

- Zero-product property: $ab = 0$ means $a = 0$ or $b = 0$. To solve by factoring, get 0 on one side first.
- A sum of squares doesn't factor over the reals. Over the integers, $ax^2 + bx + c$ factors exactly when $b^2 - 4ac$ is a perfect square.

Main mistakes: stopping before every factor is prime; solving $x(x - 3) = 10$ as $x = 10$ or $x - 3 = 10$; dividing by a variable and losing the solution $0$; writing $(x + 3)^3$ for $x^3 + 27$.

### Polynomial division and the remainder theorem

Division algorithm: $p(x) = q(x)d(x) + r(x)$ with $r = 0$ or $\deg r < \deg d$, and $q$ and $r$ unique.

- Long division: divide leading terms, multiply, subtract (change every sign), repeat. Write 0 for missing powers.
- Synthetic division by $x - c$: bring down the first coefficient, then multiply by $c$ and add. The last number is the remainder. It is Horner's method.
- Remainder theorem: dividing by $x - c$ leaves $p(c)$. Factor theorem: $x - c$ divides $p$ exactly when $p(c) = 0$. A nonzero polynomial of degree $n$ has at most $n$ zeros.
- Rational root theorem: if integer-coefficient $p$ has a zero $\frac{r}{s}$ in lowest terms, then $r$ divides $a_0$ and $s$ divides $a_n$.
- All zeros of a cubic: list candidates, find one with synthetic division, factor the quadratic that is left. Example: $2x^3 - 3x^2 - 11x + 6 = (x + 2)(2x - 1)(x - 3)$.

Main mistakes: using $c = 2$ for the divisor $x + 2$ (it is $-2$); synthetic division with a divisor like $2x - 1$; leaving out the zero for a missing power; treating the candidate list as a list of zeros.

### Polynomial functions and graphs

| Leading term | Left end | Right end |
|---|---|---|
| even degree, $a_n > 0$ | up | up |
| even degree, $a_n < 0$ | down | down |
| odd degree, $a_n > 0$ | down | up |
| odd degree, $a_n < 0$ | up | down |

- A zero of odd multiplicity is a crossing, and one of even multiplicity is a touch. Higher multiplicity flattens the graph.
- At most $n$ zeros and at most $n - 1$ turning points. An odd degree always has a real zero.
- A sign change of $f$ between $a$ and $b$ means a zero in between (intermediate value idea). Bisection halves the interval each time.
- Sketch: end behaviour, zeros and multiplicities, $y$-intercept $a_0$, signs on the intervals, smooth curve.
- $n + 1$ points determine a unique polynomial of degree at most $n$. A high-degree fit through noisy points predicts badly outside the data.

Main mistakes: confusing the leading coefficient with the $y$-intercept; drawing corners; crossing at an even-multiplicity zero; concluding there is no zero because $f(a)$ and $f(b)$ have the same sign.
