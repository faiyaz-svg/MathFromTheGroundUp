# Applications of derivatives

Derivatives as rates, linear approximation and L'Hopital's rule, the mean value theorem, curve sketching, and optimization.

1. [Rates of change and marginal analysis](01-rates-of-change-and-marginal-analysis.md)
2. [Linear approximation and L'Hopital's rule](02-linear-approximation-and-lhopitals-rule.md)
3. [The mean value theorem and extrema](03-mean-value-theorem-and-extrema.md)
4. [Concavity and curve sketching](04-concavity-and-curve-sketching.md)
5. [Optimization](05-optimization.md)

## Cheat sheet

### Rates of change and marginal analysis

The derivative $\frac{dy}{dx}$ is a rate with units "units of $y$ per unit of $x$"; a negative sign means $y$ is falling.

Related rates: draw, name the varying quantities, write one equation that connects them (keep the numbers of the instant out), differentiate with respect to $t$, then substitute and solve. Check sign and units.

| Name | Formula | Meaning |
|---|---|---|
| marginal cost | $C'(q)$ | cost of the next unit, $C(q + 1) - C(q) \approx C'(q)$ |
| marginal revenue | $R'(q) = p + q\,p'(q)$ for $R = q\,p(q)$ | extra revenue from the next unit |
| marginal profit | $P'(q) = R'(q) - C'(q)$ | extra profit from the next unit |
| average cost | $A(q) = \frac{C(q)}{q}$ | cost per unit overall |

For a quadratic the exact change over a step of 1 equals the derivative at the midpoint.

Average against marginal cost: $A'(q) = \frac{C'(q) - A(q)}{q}$. Average cost falls while $C' < A$, rises while $C' > A$, and at an interior minimum $C' = A$. For $C = F + vq + aq^2$ the minimum is at $q = \sqrt{F/a}$ with $A = v + 2\sqrt{aF}$.

Elasticity of demand $E = \frac{dq}{dp}\cdot\frac{p}{q}$ is about the percent change in quantity per 1% rise in price. Then $\frac{dR}{dp} = q(1 + E)$: a price rise raises revenue when $-1 < E < 0$.

Main mistakes:

- Substituting the instant's numbers before differentiating.
- Losing the sign of a rate for a falling quantity.
- Mixing units (minutes with seconds, metres with centimetres).
- Using average cost as the cost of the next unit.

### Linear approximation and L'Hopital's rule

Linearization at $a$: $L(x) = f(a) + f'(a)(x - a)$. The differential is $dy = f'(x)\,dx$, and $\Delta y \approx dy$. The error is $\frac{1}{2}f''(d)(x - a)^2$ for some $d$ between $a$ and $x$, so it is at most $\frac{M}{2}(x - a)^2$ when $\lvert f'' \rvert \le M$. Where $f'' > 0$ the tangent line underestimates, and where $f'' < 0$ it overestimates.

| Function | Near 0 |
|---|---|
| $\sin x$ | $x$ (radians) |
| $\cos x$ | $1$ |
| $e^x$ | $1 + x$ |
| $\ln(1 + x)$ | $x$ |
| $(1 + x)^k$ | $1 + kx$ |

Newton's method: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$. The correct digits roughly double each step near a simple root. It fails when $f'(x_n) = 0$, when it cycles ($x^3 - 2x + 2$ from 0), when it diverges ($\sqrt[3]{x}$), or when it lands on an unexpected root. Check $f(x_n)$ at the end.

L'Hopital's rule: if $\frac{f}{g}$ has the form $\frac{0}{0}$ or $\frac{\infty}{\infty}$ and $\frac{f'}{g'}$ has a limit (finite or $\pm\infty$), the two limits agree. Differentiate top and bottom separately.

| Form | What to do |
|---|---|
| $0 \cdot \infty$ | write as a quotient, $uv = \frac{u}{1/v}$ |
| $\infty - \infty$ | combine into one fraction |
| $1^\infty$, $0^0$, $\infty^0$ | take $\ln$, find the limit of the exponent times $\ln$ of the base, then exponentiate |

Key limits: $\left(1 + \frac{r}{x}\right)^x \to e^r$, $x\ln x \to 0$ as $x \to 0^+$. Growth rates: for $p > 0$ and $b > 1$, $\ln x \ll x^p \ll b^x$, but only eventually.

Main mistakes:

- Using L'Hopital's rule when the form isn't indeterminate.
- Applying the quotient rule instead of differentiating top and bottom.
- Concluding "no limit" because $\frac{f'}{g'}$ has none ($\frac{x + \sin x}{x} \to 1$).
- Treating $1^\infty$ as 1.
- Using degrees in $\sin x \approx x$.

### The mean value theorem and extrema

| Idea | Statement |
|---|---|
| critical point | $f'(c) = 0$ or $f'(c)$ doesn't exist ($c$ in the domain) |
| extreme value theorem | continuous on $[a, b]$ implies a maximum and a minimum exist |
| Fermat | a local extremum at an interior point where $f'$ exists has $f'(c) = 0$ |
| Rolle | continuous on $[a, b]$, differentiable on $(a, b)$, $f(a) = f(b)$ implies $f'(c) = 0$ for some $c$ |
| MVT | same hypotheses without the equal ends: $f'(c) = \frac{f(b) - f(a)}{b - a}$ for some $c$ |

Closed interval method: list the endpoints and the critical points, evaluate $f$ at each, and take the largest and smallest.

Consequences of the MVT: $f' = 0$ on an interval means $f$ is constant. $f' > 0$ means increasing, $f' \ge 0$ nondecreasing, $f' < 0$ decreasing. Equal derivatives mean the functions differ by a constant. A bound $\lvert f' \rvert \le K$ gives $\lvert f(a) - f(b) \rvert \le K\lvert a - b \rvert$, so $\lvert \sin a - \sin b \rvert \le \lvert a - b \rvert$, and $e^x > 1 + x$ for $x \ne 0$.

Proofs: Fermat from the signs of the one-sided difference quotients; Rolle from the extreme value theorem and Fermat; the MVT from Rolle applied to $f$ minus the chord.

Main mistakes:

- Skipping the endpoints.
- Thinking $f'(c) = 0$ guarantees an extremum ($x^3$).
- Forgetting critical points where $f'$ doesn't exist ($\lvert x \rvert$, $x^{2/3}$).
- Using the MVT without checking continuity and differentiability.
- Applying "$f' > 0$ means increasing" across a gap in the domain.

### Concavity and curve sketching

| Test | Conclusion |
|---|---|
| $f'' > 0$ on an interval | concave up (a cup, above its tangent lines) |
| $f'' < 0$ on an interval | concave down (a cap) |
| $f''$ changes sign at $c$ | inflection point |
| $f'$ goes $+$ to $-$ at $c$ | local maximum |
| $f'$ goes $-$ to $+$ at $c$ | local minimum |
| $f'(c) = 0$ and $f''(c) > 0$ ($< 0$) | local minimum (maximum); no information if $f''(c) = 0$ |

Sketching checklist: domain, intercepts, symmetry, asymptotes (vertical, horizontal, slant), sign chart of $f'$, local extrema, sign chart of $f''$, inflection points, then plot the key points and join them. Divide a rational function first to find its slant asymptote.

Convexity: if $f'' \ge 0$ on an interval, the graph lies above every tangent line, the chords lie above the graph, and any critical point is an absolute minimum. Diminishing returns means $f'' < 0$ (concave production), and rising marginal cost means $C'' > 0$ (convex cost).

Main mistakes:

- Calling every zero of $f''$ an inflection point ($x^4$).
- Using the second derivative test when $f''(c) = 0$.
- Confusing increasing with concave up.
- Running a sign chart across an asymptote.

### Optimization

Method: draw and name the variables, write the objective, use the constraint to leave one variable, find the feasible interval, find the critical points, compare (closed interval method, or the first or second derivative test or convexity on an open interval), and answer with units.

| Problem | Result |
|---|---|
| fence on three sides, length $L$ | $x = \frac{L}{4}$ each side, $y = \frac{L}{2}$ along the river (200 m: 50 by 100, area 5000) |
| box from a $30 \times 20$ sheet | cut $x \approx 3.92$ cm, volume $\approx 1056$ cm$^3$ |
| can of volume $V$, least surface | $h = 2r$, $r^3 = \frac{V}{2\pi}$ |
| can with ends twice as costly | $h = 4r$ |
| closest point on a curve | minimize the squared distance |
| profit | $R'(q) = C'(q)$ with $P''(q) < 0$ |

If the best interior point is outside the feasible interval, the best feasible point is an endpoint.

Gradient descent in one variable: $w_{n+1} = w_n - \eta f'(w_n)$. For $f(w) = a(w - w^*)^2 + k$ the distance to $w^*$ is multiplied by $1 - 2a\eta$ each step, so it converges exactly when $0 < \eta < \frac{1}{a}$. A learning rate that is too large oscillates or diverges, and for a non-convex $f$ the result depends on the starting point.

Main mistakes:

- Differentiating with two variables still in the objective.
- Using a critical point that is outside the feasible interval.
- Skipping the endpoints.
- Forgetting the last step of the question (the dimensions, the units, the square root of a squared distance).
- Setting $R' = C'$ without checking that it is a maximum.
