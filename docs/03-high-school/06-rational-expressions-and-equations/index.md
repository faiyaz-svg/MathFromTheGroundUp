# Rational expressions and equations

Fractions of polynomials: simplifying and combining them, graphing them with asymptotes, solving equations with fractions and roots, and solving inequalities with a sign chart.

1. [Rational expressions](01-rational-expressions.md)
2. [Rational functions and asymptotes](02-rational-functions-and-asymptotes.md)
3. [Rational and radical equations](03-rational-and-radical-equations.md)
4. [Polynomial and rational inequalities](04-polynomial-and-rational-inequalities.md)

## Cheat sheet

### Rational expressions

A rational expression is $\frac{p(x)}{q(x)}$ with $p$ and $q$ polynomials and $q \ne 0$. Its domain is every real $x$ with $q(x) \ne 0$. Cancelling needs a common factor of the whole top and the whole bottom: for $b(x)c(x) \ne 0$, $\frac{a\,c}{b\,c} = \frac{a}{b}$.

| Task | Method | Example |
|---|---|---|
| Simplify | factor everything, list excluded values from the original denominator, cancel factors | $\frac{3x^2 - 12}{x^2 - x - 6} = \frac{3(x - 2)}{x - 3}$, $x \ne 3, -2$ |
| Multiply | factor, cancel across the top and bottom, multiply what is left | $\frac{x - 3}{x - 1} \cdot \frac{x + 1}{x - 3} = \frac{x + 1}{x - 1}$ |
| Divide | multiply by the reciprocal, and also exclude the zeros of the divisor | $\frac{x - 2}{x + 3} \div \frac{x + 2}{x + 3}$ needs $x \ne -3, -2$ |
| Add or subtract | factor the denominators, build the LCD, rewrite, combine numerators (brackets on the second) | $\frac{2x}{x^2 - 4} - \frac{1}{x + 2} = \frac{1}{x - 2}$ |
| Complex fraction | multiply the top and bottom by the LCD of the small fractions | $\frac{1 + 1/x}{1 - 1/x^2} = \frac{x}{x - 1}$, $x \ne 0, \pm 1$ |

- LCD: every different factor once, at its highest power. $(x - 2)^2$ and $x^2 - 4$ give $(x - 2)^2(x + 2)$.
- $b - a = -(a - b)$, so $\frac{x - 5}{5 - x} = -1$ for $x \ne 5$.
- Improper fraction: divide. $\frac{x^3 - 2x^2 + x + 5}{x - 2} = x^2 + 1 + \frac{7}{x - 2}$.

Main mistakes:

- Cancelling terms: $\frac{x + 3}{3}$ is not $x + 1$ (try $x = 3$).
- Losing an excluded value after a factor cancels.
- Adding denominators: $\frac{1}{x - 1} + \frac{1}{x + 1}$ is not $\frac{2}{2x}$.
- Dropping the minus sign when subtracting a numerator with two terms.

### Rational functions and asymptotes

For $f = \frac{p}{q}$ in lowest terms, with $\deg p = n$ and $\deg q = m$:

| Feature | Rule |
|---|---|
| Vertical asymptote | $x = a$ where $q(a) = 0$ in lowest terms (the numerator is not 0 there) |
| Hole | a factor $(x - a)$ that cancels; the height is the reduced function at $a$ |
| $n < m$ | horizontal asymptote $y = 0$ |
| $n = m$ | horizontal asymptote $y = \frac{\text{leading coefficient of } p}{\text{leading coefficient of } q}$ |
| $n = m + 1$ | slant asymptote $y = Q(x)$, the quotient from dividing $p$ by $q$ |
| $n \ge m + 2$ | neither |
| Intercepts | $x$-intercepts are the zeros of the reduced numerator, $y$-intercept is $f(0)$ |

- Sketch: factor and cancel, mark holes and asymptotes, find intercepts, make a sign chart, draw each piece.
- Near a vertical asymptote the sign flips if the factor has an odd power and stays if the power is even ($\frac{1}{x}$ against $\frac{1}{x^2}$).
- The reciprocal family: $\frac{a}{x - h} + k$ has asymptotes $x = h$ and $y = k$. Divide to put $\frac{2x + 1}{x - 3}$ into this form: $2 + \frac{7}{x - 3}$.
- Average cost $\frac{F + vq}{q} = \frac{F}{q} + v$ falls toward the marginal cost $v$ and never reaches it.

Main mistakes:

- Calling a cancelled factor an asymptote. Cancel first.
- Writing $y = 0$ for equal degrees. It is the ratio of the leading coefficients.
- Thinking a graph can't cross a horizontal asymptote. It can, at a finite $x$. It can never cross a vertical one.

### Rational and radical equations

| Type | Steps | Danger |
|---|---|---|
| Rational | list excluded values, multiply every term by the LCD, solve, reject excluded values | multiplying by the LCD can add a zero of the LCD |
| Radical | isolate one radical, raise both sides to the index, repeat, solve, check every answer | squaring adds the solutions of $A = -B$ |
| Rational exponent | undo the numerator ($\pm$ if it is even), then the root; or substitute $u = x^{1/n}$ | for an even denominator, $x \ge 0$ |

- $A^2 = B^2$ exactly when $A = B$ or $A = -B$. Odd powers add nothing.
- $\sqrt{\cdots} = E$ needs $E \ge 0$, which removes many false answers early.
- Cross-multiply only when each side is a single fraction.
- Work: rate is $\frac{1}{\text{time}}$, and rates add. Two workers: $t = \frac{ab}{a + b}$.
- Current: speeds $v + c$ and $v - c$, time is distance over speed, and $v > c$.
- Equal distances at speeds $a$ and $b$: average speed is the harmonic mean $\frac{2ab}{a + b}$, which is at most $\frac{a + b}{2}$. At 60 and 40 it is 48.

Main mistakes:

- Skipping the check of a radical equation.
- Squaring a sum term by term.
- Forgetting to multiply a whole-number term by the LCD.
- Dividing both sides by $x - 3$ and losing the solution $x = 3$.
- Averaging two speeds that cover the same distance.

### Polynomial and rational inequalities

1. Get 0 on one side (no multiplying by the denominator). Combine into one fraction and factor.
2. Critical numbers: zeros of the numerator and of the denominator.
3. Sign chart: one test number per interval, or start from the right end and flip at each odd power.
4. Choose the intervals. Include a zero of the numerator only for $\ge$ and $\le$. Never include a zero of the denominator.
5. Write the answer in interval notation and test one number inside and one outside.

| Inequality | Answer |
|---|---|
| $(x - r)(x - s) < 0$, with $r < s$ | $(r, s)$ |
| $(x - r)(x - s) > 0$ | $(-\infty, r) \cup (s, \infty)$ |
| $\frac{x - 4}{x + 3} \le 0$ | $(-3, 4]$ |
| $(x - 3)^2 > 0$ | every real number except 3 |
| $(x + 2)(x - 1)^2(x - 3) \ge 0$ | $(-\infty, -2] \cup \{1\} \cup [3, \infty)$ |

- An even power doesn't change the sign, but its zero still counts as a solution for $\ge$ and $\le$.
- A hole is excluded: $\frac{x^2 - 4}{x - 2} \ge 0$ gives $[-2, 2) \cup (2, \infty)$.
- Dividing or multiplying by a negative number flips the inequality.
- Applications: profit $> 0$ between the break-even quantities, and average cost $\le$ a target is $\frac{F}{q} + v \le T$, so $q \ge \frac{F}{T - v}$.

Main mistakes:

- Multiplying by $x - 1$ in $\frac{x}{x - 1} > 2$ without splitting into cases.
- Writing one interval, such as $[-2, 3]$, when the chart alternates and the answer has several pieces.
- Including a zero of the denominator.
- Forgetting to flip when dividing by $-1$.
