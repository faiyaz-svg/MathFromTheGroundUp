# Limits and continuity

What "gets close to" means for a function: limits and how to compute them, the epsilon-delta definition, and continuity with its two big theorems.

1. [Limits, intuition and limit laws](01-limits-intuition-and-limit-laws.md)
2. [The epsilon-delta definition](02-epsilon-delta-definition.md)
3. [Continuity, asymptotes and the IVT](03-continuity-asymptotes-and-ivt.md)

## Cheat sheet

### Limits, intuition and limit laws

The limit $\lim_{x \to a} f(x) = L$ says $f(x)$ gets as close to $L$ as you like when $x$ is close enough to $a$ and $x \ne a$. It ignores $f(a)$. The two-sided limit exists exactly when both one-sided limits exist and are equal.

| Way a limit fails | Example at 0 |
|---|---|
| jump (one-sided limits differ) | $\frac{\lvert x \rvert}{x}$ |
| blow-up (written $\pm\infty$) | $\frac{1}{x^2}$, and $\frac{1}{x}$ with opposite signs on the sides |
| oscillation | $\sin\frac{1}{x}$ |

Limit laws (when the limits of the pieces exist): the limit of a sum, difference, constant multiple, product, power and root is the same operation on the limits, and for a quotient the bottom limit must not be 0. Polynomials and rational functions (with nonzero denominator) are found by substitution.

| Situation | Move |
|---|---|
| $\frac{0}{0}$ with polynomials | factor and cancel the common factor |
| $\frac{0}{0}$ with a square root | multiply by the conjugate |
| $\frac{0}{0}$ with fractions on top | common denominator |
| sine or cosine | reach $\frac{\sin u}{u}$; $\lim_{x \to 0} \frac{\sin x}{x} = 1$ (radians), $\lim_{x \to 0} \frac{1 - \cos x}{x} = 0$ |
| trapped between two functions with the same limit | squeeze theorem |
| $\frac{c}{0}$ with $c \ne 0$ | blow-up; check the sign on each side |
| $x \to \pm\infty$, rational function | divide by the highest power of $x$ in the denominator |

- A horizontal asymptote $y = L$ means $\lim_{x \to \pm\infty} f(x) = L$ at one end or both. A vertical asymptote $x = a$ means an infinite one-sided limit at $a$.
- $\sqrt{x^2} = \lvert x \rvert$, so a root can give opposite limits at $+\infty$ and $-\infty$.

Main mistakes:

- Reading the limit as the value: $\frac{x^2 - 1}{x - 1}$ has limit 2 at 1 and no value there.
- Treating $\frac{0}{0}$ as 0, 1 or "no limit". It means more work is needed.
- Using a limit law when a piece has no limit.
- Trusting a table on an oscillating function.
- Using $\infty$ as a number ($\infty - \infty$ is undetermined).
- Using degrees in the $\frac{\sin x}{x}$ limit.

### The epsilon-delta definition

$$
\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0\ \exists \delta > 0\ \forall x\ \bigl(0 < \lvert x - a \rvert < \delta \Rightarrow \lvert f(x) - L \rvert < \varepsilon\bigr).
$$

The challenger picks $\varepsilon$ (output tolerance), you answer with $\delta$ (input tolerance), the challenger picks any $x$ in the window other than $a$. $\delta$ may depend on $\varepsilon$, never on $x$.

Proof recipe:

1. Scratch work backwards: simplify $\lvert f(x) - L \rvert$ until a factor $\lvert x - a \rvert$ appears.
2. If the other factor depends on $x$, promise $\delta \le 1$ and bound it on that window by a number $K$.
3. Take $\delta = \min\left(1, \frac{\varepsilon}{K}\right)$ (just $\frac{\varepsilon}{K}$ if $K$ was a constant already).
4. Write forwards: let $\varepsilon > 0$, take $\delta$, suppose $0 < \lvert x - a \rvert < \delta$, conclude $< \varepsilon$.
5. Test one number.

| Limit | $\delta$ |
|---|---|
| $\lim_{x \to a}(mx + b) = ma + b$ | $\frac{\varepsilon}{\lvert m \rvert}$ |
| $\lim_{x \to 3} x^2 = 9$ | $\min\left(1, \frac{\varepsilon}{7}\right)$ |
| $\lim_{x \to 1}(x^2 + x) = 2$ | $\min\left(1, \frac{\varepsilon}{4}\right)$ |
| $\lim_{x \to 4}\sqrt{x} = 2$ | $\min(4, 2\varepsilon)$ |
| $\lim_{x \to 2}\frac{1}{x} = \frac{1}{2}$ | $\min(1, 2\varepsilon)$ |

- Sum law: use $\frac{\varepsilon}{2}$ for each piece and $\delta = \min(\delta_1, \delta_2)$, then the triangle inequality.
- To disprove, negate: $\exists \varepsilon\ \forall \delta\ \exists x\ (0 < \lvert x - a \rvert < \delta \wedge \lvert f(x) - L \rvert \ge \varepsilon)$. For a jump of size $s$, take $\varepsilon = \frac{s}{2}$.
- Sequences: $a_n \to L$ means $\forall \varepsilon\ \exists N\ \forall n \ge N\ (\lvert a_n - L \rvert < \varepsilon)$. Two input sequences closing in on $a$ with different output limits show that the limit does not exist.

Main mistakes:

- Giving $\delta$ for one $\varepsilon$ instead of a rule for every $\varepsilon$.
- Letting $\delta$ depend on $x$.
- Writing the scratch work as the proof.
- Testing $x = a$ in a check.
- Flipping only some quantifiers when negating.

### Continuity, asymptotes and the IVT

$f$ is continuous at $a$ when $f(a)$ is defined, $\lim_{x \to a} f(x)$ exists, and the two are equal. Equivalently, $\forall \varepsilon\ \exists \delta\ \forall x\ (\lvert x - a \rvert < \delta \Rightarrow \lvert f(x) - f(a) \rvert < \varepsilon)$, with no "$0 <$".

| Discontinuity | What happens | Repair |
|---|---|---|
| removable | finite limit, value missing or different | redefine $f(a)$ |
| jump | two different finite one-sided limits | none |
| infinite | an infinite one-sided limit (vertical asymptote) | none |

- Continuous on its domain: polynomials, rational functions, roots, $\lvert x \rvert$, $b^x$, $\log_b x$, sine, cosine, tangent. Sums, products, quotients (bottom nonzero) and compositions of continuous functions are continuous.
- If $\lim g(x) = b$ and $f$ is continuous at $b$, then $\lim f(g(x)) = f(b)$.
- A piecewise function needs checking only at the breaks: left limit, right limit and value all equal.
- Slant asymptote $y = mx + b$: $m = \lim \frac{f(x)}{x}$, then $b = \lim (f(x) - mx)$. A graph can cross a horizontal or slant asymptote, never a vertical one.
- IVT: $f$ continuous on $[a, b]$ and $N$ strictly between $f(a)$ and $f(b)$ gives a $c$ in $(a, b)$ with $f(c) = N$. It needs completeness: it fails over the rationals ($x^2 - 2$).
- Root existence: a sign change of a continuous function means a zero. To solve $f = h$, apply it to $f - h$. An odd-degree polynomial has a real zero.
- Bisection: keep the half with a sign change; after $k$ steps the width is $\frac{b - a}{2^k}$, so $\lceil \log_2 \frac{b - a}{w} \rceil$ steps reach width $w$.
- EVT: a continuous function on a closed interval $[a, b]$ has a maximum and a minimum.

Main mistakes:

- Calling a function with a hole continuous at the hole.
- Using the IVT without continuity on the whole closed interval ($\frac{1}{x}$ on $[-1, 1]$).
- Reading the IVT backwards: taking every value does not make a function continuous.
- Reading the IVT as "exactly one solution".
- Forgetting that the EVT needs a closed interval.
