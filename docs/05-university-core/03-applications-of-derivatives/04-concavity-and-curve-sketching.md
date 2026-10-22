# Concavity and curve sketching

After this lesson you can classify critical points with the first and second derivative tests, find where a graph is concave up or down and where it has inflection points, sketch a function from its derivatives with a full checklist, and explain why convexity makes optimization easy and why concavity models diminishing returns.

Before this: [the mean value theorem and extrema](03-mean-value-theorem-and-extrema.md) (critical points and the sign-of-the-derivative theorem), [differentiation rules](../02-derivatives/02-differentiation-rules.md), and [rational functions and asymptotes](../../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For $f(x) = x^3 - 12x$, find where $f$ is increasing and where it has local extrema.
2. For $f(x) = x^4 - 6x^2$, where is $f$ concave up?
3. Use the second derivative test on $f(x) = x + \frac{1}{x}$ at its critical point for $x > 0$.

<details class="solution" markdown>
<summary>Answers</summary>

1. $f'(x) = 3x^2 - 12 = 3(x - 2)(x + 2)$ is positive for $x < -2$ and $x > 2$, and negative between. So $f$ is increasing on $(-\infty, -2)$ and $(2, \infty)$, with a local maximum $f(-2) = 16$ and a local minimum $f(2) = -16$.
2. $f''(x) = 12x^2 - 12 = 12(x - 1)(x + 1)$ is positive when $\lvert x \rvert > 1$. So $f$ is concave up on $(-\infty, -1)$ and $(1, \infty)$.
3. $f'(x) = 1 - \frac{1}{x^2} = 0$ at $x = 1$, and $f''(x) = \frac{2}{x^3}$ gives $f''(1) = 2 > 0$, so $x = 1$ is a local minimum, with $f(1) = 2$.

</details>

## The idea

Knowing where a function rises and falls says where its hills and valleys are, but not how the graph bends between them. Two roads can climb at the same overall rate, and one is a steady slope while the other starts steep and flattens out. The first derivative tells you the steepness at each point. The second derivative, the rate of change of the steepness, tells you whether the road is getting steeper or flatter.

A graph that curves upward, like a cup, has slopes that increase as you move to the right: the tangent line tilts further and further anticlockwise. A graph that curves downward, like a cap, has slopes that decrease. The point where the bending changes direction is an inflection point, and there the tangent line crosses the curve. The figure shows the three situations.

![Three small graphs. The first is the parabola y = x squared with three tangent lines at x equal to minus 1.2, 0 and 1.2, whose slopes minus 2.4, 0 and 2.4 increase; all the tangent lines lie below the curve, and the label says concave up. The second is the parabola y = minus x squared with the same three tangent lines, whose slopes decrease, all lying above the curve, labelled concave down. The third is the graph of x cubed, concave down for negative x and concave up for positive x, with the horizontal tangent at the origin crossing the curve, labelled inflection.](../../assets/figures/05-university-core/concavity-and-curve-sketching-concavity.svg)

With the first and second derivatives you can find every hill, valley and change of bend, and then draw a graph that has the correct shape between the plotted points. The same two derivatives answer questions in economics and machine learning. Is the extra output from one more worker rising or falling? Is the loss function a bowl with one bottom, or a landscape with many?

## Definitions

Let $f$ be differentiable on an open interval $I$. The graph of $f$ is **concave up** on $I$ if $f'$ is increasing on $I$, and **concave down** on $I$ if $f'$ is decreasing on $I$. In plain words, concave up means the slope grows as $x$ grows, so the curve bends like a cup and lies above its tangent lines. Concave down means the slope shrinks, so the curve bends like a cap and lies below its tangent lines.

An **inflection point** is a point $(c, f(c))$ on the graph at which $f$ is continuous and the concavity changes, from up to down or from down to up. In plain words, it is where the bend switches direction, and the tangent line there (if there is one) crosses the curve.

The **concavity test** says: if $f''(x) > 0$ for all $x$ in $I$, then $f$ is concave up on $I$, and if $f''(x) < 0$ for all $x$ in $I$, then $f$ is concave down on $I$. This follows from the sign-of-the-derivative theorem of the last lesson applied to $f'$: a positive derivative of $f'$ means $f'$ is increasing.

The **first derivative test** says: let $c$ be a critical point of a function $f$ that is continuous at $c$ and differentiable on an interval around $c$, except possibly at $c$.

- If $f'$ changes from positive to negative at $c$ (positive just to the left, negative just to the right), then $f$ has a local maximum at $c$.
- If $f'$ changes from negative to positive at $c$, then $f$ has a local minimum at $c$.
- If $f'$ has the same sign on both sides of $c$, then $f$ has no local extremum at $c$.

In plain words, going left to right, a maximum is where the graph stops rising and starts falling, and a minimum is the reverse.

The **second derivative test** says: suppose $f'(c) = 0$ and $f''(c)$ exists. If $f''(c) > 0$ then $f$ has a local minimum at $c$, and if $f''(c) < 0$ then $f$ has a local maximum at $c$. If $f''(c) = 0$ the test says nothing. In plain words, at a flat spot, a cup shape means a valley and a cap shape means a hill.

A function $f$ is **convex** on an interval $I$ if its graph lies on or below every chord: for all $x, y$ in $I$ and every $t$ with $0 \le t \le 1$,

$$
f\bigl(tx + (1 - t)y\bigr) \le t f(x) + (1 - t) f(y).
$$

It is **concave** if the inequality is reversed. In plain words, a convex function is one that bends upward everywhere (a function with a bowl-shaped graph), and the right side is the height of the chord above the point $tx + (1 - t)y$. For a twice-differentiable function, convex on $I$ is the same as $f'' \ge 0$ on $I$. The theorem below proves the direction that is used in practice: $f'' \ge 0$ implies convex.

## How to do it

### Classifying a critical point

1. Differentiate and find the critical points ($f' = 0$, or $f'$ doesn't exist but $f$ does).
2. Make a sign chart for $f'$: pick one test number in each interval between critical points (and asymptotes), and record the sign of $f'$.
3. Read the first derivative test from the chart: positive then negative is a local maximum, negative then positive is a local minimum, no change is neither.
4. If $f'(c) = 0$ and $f''$ is easy, use the second derivative test as a shortcut. If $f''(c) = 0$, or $f'(c)$ doesn't exist, return to the sign chart.
5. Compute the value $f(c)$ for each extremum, and check against a few values of $f$.

### Finding concavity and inflection points

1. Compute $f''$ and find where $f''(x) = 0$ or $f''(x)$ doesn't exist (and $f$ is defined).
2. Make a sign chart for $f''$ on the intervals these points cut out.
3. Where $f'' > 0$ the graph is concave up, and where $f'' < 0$ it is concave down.
4. A point where the sign of $f''$ changes (and $f$ is continuous) is an inflection point. Write down $f(c)$. A zero of $f''$ where the sign doesn't change is not an inflection point.

### Proofs of the two tests

*Theorem (first derivative test, local maximum).* If $f$ is continuous at $c$, $f'(x) > 0$ for $x$ in some interval $(c - \delta, c)$ and $f'(x) < 0$ for $x$ in $(c, c + \delta)$, then $f$ has a local maximum at $c$.

We know the sign of $f'$ on each side, and that $f$ is continuous at $c$. We want $f(x) \le f(c)$ for $x$ near $c$. The plan is to use the sign-of-the-derivative theorem on each side, including the endpoint $c$.

*Proof.* On $(c - \delta, c]$ the function $f$ is continuous (at $c$ by assumption, and elsewhere because it is differentiable), and $f' > 0$ in the interior $(c - \delta, c)$. By the sign-of-the-derivative theorem $f$ is increasing on $(c - \delta, c]$, so $f(x) < f(c)$ for $x \in (c - \delta, c)$. On $[c, c + \delta)$ similarly $f' < 0$ in the interior, so $f$ is decreasing there and $f(x) < f(c)$ for $x \in (c, c + \delta)$. So $f(x) \le f(c)$ on the whole interval around $c$. $\blacksquare$

The local minimum case follows by applying this to $-f$, and the "no change" case is similar: $f$ is strictly increasing (or decreasing) through $c$.

*Theorem (second derivative test).* Suppose $f'(c) = 0$ and $f''(c)$ exists. If $f''(c) > 0$, then $f$ has a local minimum at $c$. If $f''(c) < 0$, it has a local maximum at $c$.

We know $f'(c) = 0$ and that the limit defining $f''(c)$ exists and is positive (in the first case). We want a local minimum, and the plan is to show that $f'$ changes from negative to positive at $c$, and use the first derivative test.

*Proof.* Suppose $f''(c) > 0$. Because $f'(c) = 0$,

$$
f''(c) = \lim_{x \to c}\frac{f'(x) - f'(c)}{x - c} = \lim_{x \to c}\frac{f'(x)}{x - c} > 0.
$$

A limit that is positive means the quotient is positive for every $x \ne c$ close enough to $c$. For such $x < c$ the denominator $x - c$ is negative, so $f'(x) < 0$. For such $x > c$ the denominator is positive, so $f'(x) > 0$. So $f'$ changes from negative to positive at $c$. Also $f$ is continuous at $c$, since $f'(c)$ exists. By the first derivative test, $f$ has a local minimum at $c$. The case $f''(c) < 0$ is the same with every inequality reversed. $\blacksquare$

Look back at the case the theorem leaves out. If $f''(c) = 0$, the limit above is 0 and says nothing about signs. All three of $f(x) = x^4$ (a minimum), $f(x) = -x^4$ (a maximum) and $f(x) = x^3$ (neither) have $f'(0) = 0$ and $f''(0) = 0$, so the second derivative test must be silent. The first derivative test decides each.

### A sketching checklist

1. Domain: where is $f$ defined? Break the line at any gaps.
2. Intercepts: $f(0)$ for the $y$-intercept, and the solutions of $f(x) = 0$ for the $x$-intercepts when they are easy to find.
3. Symmetry: even ($f(-x) = f(x)$, mirror in the $y$-axis), odd ($f(-x) = -f(x)$, turns into itself under rotation by $180^\circ$ about the origin) or periodic. Symmetry halves the work.
4. Asymptotes: vertical asymptotes where a denominator is 0 (check the one-sided limits for the signs), and horizontal or slant asymptotes from the limits as $x \to \pm\infty$ (see [continuity, asymptotes and the IVT](../01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md)).
5. First derivative: critical points, and the sign chart of $f'$ for the increasing and decreasing intervals.
6. Local extrema: from the sign chart (first derivative test), with their values.
7. Second derivative: the sign chart of $f''$ for concavity, and the inflection points with their values.
8. Plot the key points (intercepts, extrema, inflection points), draw the asymptotes as dashed lines, and join the points with curves that have the right direction and bend on each interval.
9. Check against two or three computed values, or a graphing tool.

### Convexity, optimization and economics

The next theorem is why convexity matters in optimization: for a convex function, a flat spot is automatically the global minimum.

*Theorem.* Let $f$ be twice differentiable on an interval $I$ with $f''(x) \ge 0$ for all $x \in I$. Then:

- (a) the graph lies on or above each tangent line: $f(x) \ge f(c) + f'(c)(x - c)$ for all $x, c \in I$;
- (b) $f$ is convex on $I$;
- (c) if $f'(c) = 0$ for some $c \in I$, then $f(c)$ is the absolute minimum of $f$ on $I$.

We know that $f'$ is nondecreasing (from $f'' \ge 0$ and the sign-of-the-derivative theorem). For (a) we want the vertical gap between the curve and the tangent line to be never negative. The plan is to study the gap as a function, whose derivative has a known sign on each side of $c$. Then (b) and (c) follow from (a).

*Proof of (a).* Fix $c$ and let $g(x) = f(x) - f(c) - f'(c)(x - c)$, the gap. Then $g(c) = 0$ and $g'(x) = f'(x) - f'(c)$. Since $f'$ is nondecreasing, $g'(x) \ge 0$ for $x > c$ and $g'(x) \le 0$ for $x < c$. By the sign-of-the-derivative theorem, $g$ is nondecreasing to the right of $c$ and nonincreasing to the left of $c$, so $g(x) \ge g(c) = 0$ on both sides.

*Proof of (b).* Take $x, y \in I$, $0 \le t \le 1$, and $z = tx + (1 - t)y$, which is in $I$. Apply (a) at $c = z$ twice: $f(x) \ge f(z) + f'(z)(x - z)$ and $f(y) \ge f(z) + f'(z)(y - z)$. Multiply the first by $t$ and the second by $1 - t$ and add. The tangent terms combine to $f'(z)\bigl(tx + (1 - t)y - z\bigr) = 0$, so $tf(x) + (1 - t)f(y) \ge f(z)$.

*Proof of (c).* If $f'(c) = 0$, then (a) reads $f(x) \ge f(c)$ for all $x \in I$. $\blacksquare$

Look back at part (c). It does what the second derivative test can't: it says that the minimum is absolute and not just local, and that no other valley can be lower. If $f'' > 0$ everywhere on $I$, the minimum point is also the only one.

In economics, concavity and convexity are the mathematical form of diminishing and increasing marginal effects. If output is a function of labour, $Q = f(L)$, then $f'(L)$ is the marginal product of labour, the extra output from one more worker. The **law of diminishing marginal returns** says that beyond some point $f'$ falls, which means $f'' < 0$ and the production curve is concave. In the same way, a total cost curve $C(q)$ with a rising marginal cost has $C'' > 0$, so it is convex, and a utility function with diminishing marginal utility is concave.

![Two panels. On the left, the graph of Q = 20 times the square root of L, a rising curve that bends downward (concave), with two tangent lines: at L = 4 the slope is 5 and at L = 16 the slope is 2.5. On the right, the marginal product 10 divided by the square root of L, which falls steadily as L increases.](../../assets/figures/05-university-core/concavity-and-curve-sketching-diminishing-returns.svg)

In machine learning, the squared-error loss of a linear model is a convex function of the parameters, so any minimum that gradient descent reaches is the global minimum. The loss of a neural network is not convex, and it has many local minima and flat regions, which is why training it is harder to guarantee (see [optimization](05-optimization.md)).

## Worked examples

<div class="example" markdown>

### Example 1: classifying critical points and finding the bend

Analyse $f(x) = 2x^3 - 9x^2 + 12x$: its critical points, concavity and inflection point.

Step 1: $f'(x) = 6x^2 - 18x + 12 = 6(x - 1)(x - 2)$, which is defined everywhere and is zero at $x = 1$ and $x = 2$.

Step 2: the sign chart. Test numbers: $f'(0) = 12 > 0$, $f'(1.5) = 6(0.5)(-0.5) = -1.5 < 0$ and $f'(3) = 6(2)(1) = 12 > 0$. So $f$ is increasing on $(-\infty, 1)$, decreasing on $(1, 2)$ and increasing on $(2, \infty)$.

Step 3: $f'$ goes from positive to negative at $x = 1$, a local maximum, with $f(1) = 5$. It goes from negative to positive at $x = 2$, a local minimum, with $f(2) = 4$.

Step 4: the shortcut. $f''(x) = 12x - 18$, so $f''(1) = -6 < 0$ (maximum) and $f''(2) = 6 > 0$ (minimum), in agreement.

Concavity: $f''(x) = 0$ at $x = 1.5$, with $f'' < 0$ for $x < 1.5$ and $f'' > 0$ for $x > 1.5$. So $f$ is concave down on $(-\infty, 1.5)$, concave up on $(1.5, \infty)$, with an inflection point at $(1.5, 4.5)$.

Check: the inflection value is $f(1.5) = 6.75 - 20.25 + 18 = 4.5$, halfway between $f(1) = 5$ and $f(2) = 4$, which fits a cubic that is symmetric about its inflection point. Plotting a few values confirms the hill at $x = 1$ and the valley at $x = 2$.

</div>

<div class="example" markdown>

### Example 2: a sketch where the second derivative test fails

Sketch $f(x) = x^4 - 4x^3 = x^3(x - 4)$.

Domain: all real numbers. Intercepts: $f(0) = 0$, and $f(x) = 0$ at $x = 0$ and $x = 4$. Symmetry: none. Asymptotes: none, since $f(x) \to +\infty$ as $x \to \pm\infty$ (the leading term $x^4$ dominates).

First derivative: $f'(x) = 4x^3 - 12x^2 = 4x^2(x - 3)$, zero at $x = 0$ and $x = 3$. Second derivative: $f''(x) = 12x^2 - 24x = 12x(x - 2)$, zero at $x = 0$ and $x = 2$.

| Interval | $f'$ | $f$ | $f''$ | Shape |
|---|---|---|---|---|
| $(-\infty, 0)$ | $-$ | decreasing | $+$ | concave up |
| $(0, 2)$ | $-$ | decreasing | $-$ | concave down |
| $(2, 3)$ | $-$ | decreasing | $+$ | concave up |
| $(3, \infty)$ | $+$ | increasing | $+$ | concave up |

At $x = 3$ the sign of $f'$ goes from $-$ to $+$, so there is a local (and, as the table shows, absolute) minimum $f(3) = -27$. At $x = 0$ the derivative is zero but it doesn't change sign (it is negative on both sides), so there is no extremum, and $f''(0) = 0$, so the second derivative test could not have told you. Instead, $f''$ changes sign at $0$ and at $2$, so both are inflection points: $(0, 0)$, where the tangent is horizontal, and $(2, -16)$.

![The graph of y = x to the fourth minus 4 x cubed. It comes down from the upper left, flattens at the origin where a blue dot marks an inflection point with a horizontal tangent, keeps falling, passes a second blue inflection point at (2, minus 16), reaches a red minimum at (3, minus 27), and then rises steeply through (4, 0).](../../assets/figures/05-university-core/concavity-and-curve-sketching-quartic.svg)

Check: $f(2) = 16 - 32 = -16$ and $f(3) = 81 - 108 = -27$, the graph is below zero between 0 and 4 and above it elsewhere (the sign of $x^3(x - 4)$), and the code below finds the sign changes of $f'$ at 3 and of $f''$ at 0 and 2.

</div>

<div class="example" markdown>

### Example 3: a rational function with a slant asymptote

Sketch $f(x) = \frac{x^2}{x - 1}$.

Domain: $x \ne 1$. Intercepts: $f(0) = 0$, and $f(x) = 0$ only at $x = 0$. Symmetry: none ($f(-x) = \frac{x^2}{-x - 1}$ is neither $f(x)$ nor $-f(x)$).

Asymptotes: at $x = 1$ the numerator is 1 and the denominator tends to 0, so $f \to +\infty$ as $x \to 1^+$ and $f \to -\infty$ as $x \to 1^-$. A vertical asymptote at $x = 1$. By polynomial division (see [rational functions and asymptotes](../../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md)), $f(x) = x + 1 + \frac{1}{x - 1}$. The last term tends to 0 as $x \to \pm\infty$, so $y = x + 1$ is a slant asymptote, and the curve lies above it for $x > 1$ and below it for $x < 1$.

First derivative: $f'(x) = 1 - \frac{1}{(x - 1)^2} = \frac{x(x - 2)}{(x - 1)^2}$, zero at $x = 0$ and $x = 2$. Second derivative: $f''(x) = \frac{2}{(x - 1)^3}$, never zero.

| Interval | $f'$ | $f$ | $f''$ | Shape |
|---|---|---|---|---|
| $(-\infty, 0)$ | $+$ | increasing | $-$ | concave down |
| $(0, 1)$ | $-$ | decreasing | $-$ | concave down |
| $(1, 2)$ | $-$ | decreasing | $+$ | concave up |
| $(2, \infty)$ | $+$ | increasing | $+$ | concave up |

So $x = 0$ is a local maximum with $f(0) = 0$ and $x = 2$ is a local minimum with $f(2) = 4$. The second derivative test agrees: $f''(0) = -2 < 0$ and $f''(2) = 2 > 0$. There is no inflection point: $f''$ changes sign at $x = 1$, but $f$ is not defined there, so concavity changes across the asymptote and not at a point of the graph.

![The graph of y = x squared over x minus 1, drawn as two pieces separated by the dashed vertical line x = 1 and hugging the dashed slant line y = x + 1. The left piece rises from the lower left, reaches a red local maximum at the origin, and then plunges to minus infinity at x = 1. The right piece comes down from plus infinity at x = 1, reaches a red local minimum at (2, 4), and then climbs along the slant line.](../../assets/figures/05-university-core/concavity-and-curve-sketching-rational.svg)

Check: $f(2) = \frac{4}{1} = 4$, $f(3) = 4.5$ (just above $y = 3 + 1 = 4$, as the sign of $\frac{1}{x - 1}$ says), and $f(-1) = \frac{1}{-2} = -0.5$ (below $y = 0$, the asymptote's value at $-1$, as predicted).

</div>

<div class="example" markdown>

### Example 4: x times e to the minus x

Sketch $f(x) = xe^{-x}$.

Domain: all real numbers. Intercept: $f(0) = 0$, and $f(x) = 0$ only at $x = 0$ because $e^{-x} > 0$. Sign: $f > 0$ for $x > 0$ and $f < 0$ for $x < 0$.

Asymptotes: as $x \to \infty$, $xe^{-x} = \frac{x}{e^x} \to 0$ by the growth-rate theorem of [linear approximation and L'Hopital's rule](02-linear-approximation-and-lhopitals-rule.md), so $y = 0$ is a horizontal asymptote on the right, and $f > 0$ there. As $x \to -\infty$, $x \to -\infty$ and $e^{-x} \to \infty$, so $f \to -\infty$, with no asymptote.

First derivative, by the product rule: $f'(x) = e^{-x} - xe^{-x} = (1 - x)e^{-x}$, which is positive for $x < 1$, zero at $x = 1$ and negative for $x > 1$. So $f$ increases up to $x = 1$ and decreases after it. Local (and absolute) maximum $f(1) = \frac{1}{e} \approx 0.368$.

Second derivative: $f''(x) = -e^{-x} - (1 - x)e^{-x} = (x - 2)e^{-x}$, which is negative for $x < 2$, zero at $x = 2$ and positive for $x > 2$. So $f$ is concave down on $(-\infty, 2)$ and concave up on $(2, \infty)$, with an inflection point at $\left(2, \frac{2}{e^2}\right) \approx (2, 0.271)$, where the slope is $f'(2) = -e^{-2} \approx -0.135$.

![The graph of y = x times e to the minus x. It rises steeply from far below at the left through the origin, reaches a red maximum at (1, 1 over e), passes a blue inflection point at (2, 2 over e squared), and then decreases slowly towards the horizontal axis, which is a dashed asymptote on the right.](../../assets/figures/05-university-core/concavity-and-curve-sketching-x-exp.svg)

Check: $f(1) = 0.3679$, $f(2) = 0.2707$, $f(3) = 0.1494$, $f(6) = 0.0149$, falling towards 0 on the right. The graph falls fastest around the inflection point, and the numbers show it: the drops are $0.097$ (from 1 to 2), $0.121$ (from 2 to 3) and $0.076$ (from 3 to 4).

</div>

<div class="example" markdown>

### Example 5: classify and bend (finish it yourself)

For $f(x) = x^3 - 3x^2$, find the critical points and classify them, and find the inflection point. The derivatives are $f'(x) = 3x^2 - 6x = 3x(x - 2)$ and $f''(x) = 6x - 6$.

<details class="solution" markdown>
<summary>Finish</summary>

The critical points are $x = 0$ and $x = 2$. Then $f''(0) = -6 < 0$, a local maximum with $f(0) = 0$, and $f''(2) = 6 > 0$, a local minimum with $f(2) = 8 - 12 = -4$.

The second derivative is zero at $x = 1$, negative before and positive after, so there is an inflection point at $(1, f(1)) = (1, -2)$.

Check: the sign chart of $f'$ is $+$, $-$, $+$ across $x = 0$ and $x = 2$, in agreement. The inflection point is the midpoint of the two extrema, $\left(\frac{0 + 2}{2}, \frac{0 + (-4)}{2}\right) = (1, -2)$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: "$f''(c) = 0$ means an inflection point". It is a candidate only. $f(x) = x^4$ has $f''(0) = 0$ and is concave up on both sides, so there is no inflection point. The sign of $f''$ must change.

</div>

<div class="warning" markdown>

Watch out: using the second derivative test when $f''(c) = 0$ or when $f'(c)$ doesn't exist. The test is silent for $x^4$, $-x^4$ and $x^3$, and for corners such as $\lvert x \rvert$. Use the sign chart of $f'$.

</div>

<div class="warning" markdown>

Watch out: an inflection point can occur where $f''$ doesn't exist. $f(x) = x^{1/3}$ has $f''(x) = -\frac{2}{9}x^{-5/3}$, undefined at 0, but $f$ is concave up for $x < 0$ and concave down for $x > 0$, so $(0, 0)$ is an inflection point with a vertical tangent.

</div>

<div class="warning" markdown>

Watch out: confusing "increasing" with "concave up". A function can be decreasing and concave up (the left part of $x^2$), or increasing and concave down ($\sqrt{x}$). The first derivative controls the direction and the second controls the bend.

</div>

<div class="warning" markdown>

Watch out: running a sign chart across a vertical asymptote or a gap in the domain. In Example 3 the intervals $(0, 1)$ and $(1, 2)$ are separate: $f'$ keeps its sign across $x = 1$ there, but $f$ is not defined at 1, and the sign-of-the-derivative theorem applies on each interval separately.

</div>

<div class="warning" markdown>

Watch out: calling a local extremum "the" maximum. A sign chart finds local extrema. For an absolute extremum, compare values, check the ends of the domain and the limits at infinity, as in [the mean value theorem and extrema](03-mean-value-theorem-and-extrema.md).

</div>

## Tricks and shortcuts

A cubic $ax^3 + bx^2 + cx + d$ has exactly one inflection point, at $x = -\frac{b}{3a}$, and it is symmetric about that point. When it has two critical points, the inflection point is halfway between them (Practice 7).

Remember the shapes: $f'' > 0$ is a cup (a smile), $f'' < 0$ is a cap (a frown). A minimum with $f'' > 0$ is the bottom of a cup, and a maximum with $f'' < 0$ is the top of a cap.

For a rational function, divide first. The quotient gives the asymptote and the remainder tells which side the curve is on, as in $x + 1 + \frac{1}{x - 1}$.

Check the ends first. The behaviour as $x \to \pm\infty$ and near any vertical asymptote tells you roughly what the whole graph looks like before you compute a derivative, and it catches sign errors later.

## In code

The slope and the concavity can be estimated numerically, and sign changes of each are found by scanning a grid. For $f(x) = x^4 - 4x^3$ this finds the single extremum at $x = 3$ and the two inflection points at 0 and 2, and shows the slope near $x = 0$ not changing sign.

<details class="code" markdown>
<summary>In code</summary>

```python
def f(x):
    return x**4 - 4 * x**3


def d1(x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)


def d2(x, h=1e-4):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2


# Find where the slope changes sign, and where the concavity changes sign.
def sign_changes(g, lo, hi, n=4000):
    xs = [lo + (hi - lo) * i / n for i in range(n + 1)]
    out = []
    for a, b in zip(xs, xs[1:]):
        if g(a) * g(b) < 0:
            out.append(round((a + b) / 2, 2) + 0.0)
    return out


print("slope changes sign at", sign_changes(d1, -2, 5))
print("concavity changes sign at", sign_changes(d2, -2, 5))
# slope changes sign at [3.0]
# concavity changes sign at [0.0, 2.0]

# x = 0 is a critical point where the slope does not change sign: no extremum.
for x in (-0.5, -0.1, 0.1, 0.5):
    print(x, round(d1(x), 4))
# -0.5 -3.5
# -0.1 -0.124
# 0.1 -0.116
# 0.5 -2.5
print(round(d2(3), 3), round(d2(0.0001), 3))
# 36.0 -0.002
```

The slope is negative on both sides of $x = 0$, so there is no extremum there, although $f'(0) = 0$. At $x = 3$ the second difference is 36, which matches $f''(3) = 12 \cdot 3 \cdot 1 = 36$.

</details>

## FAQ

### Why is "concave up" a cup and not a cap?

It is a convention: concave up means the graph curves in the direction of increasing $y$, like a cup that holds water, and concave down curves the other way. Some books say "convex" for concave up and "concave" for concave down, and in economics "convex" has other meanings too (convex preferences and convex sets), so check which one a text means. The test with $f''$ is the same either way: positive means up.

### Can a point be both a critical point and an inflection point?

Yes. At $x = 0$ for $f(x) = x^4 - 4x^3$ the tangent is horizontal ($f'(0) = 0$) and the concavity changes, so it is both. The first derivative test says it is not an extremum, because $f'$ is negative on both sides. Such a point is a flat inflection, like $x^3$ at 0.

### Why does the second derivative test need $f'(c) = 0$?

Because it detects the shape at a flat spot. If $f'(c) \ne 0$ the point is on a slope and is not an extremum whatever the sign of $f''(c)$: a cup shape on a slope is just a curve rising or falling. The second derivative tells you which way the graph bends only once you know that the tangent is level.

### Why does convexity make optimization easy?

For a convex function, the tangent line at every point is below the graph. At a point with a flat tangent the tangent line is horizontal, so the whole graph is on or above that height, which makes the point a global minimum. There are no other valleys to get stuck in. This is the content of part (c) of the theorem. For a non-convex function, a flat tangent only shows a local minimum, and the search for the global one is much harder.

## Practice

### Warm-up

1\. Find the intervals where $f(x) = x^3 - 12x$ is increasing and decreasing, and its local extrema.

<details class="solution" markdown>
<summary>Solution</summary>

$f'(x) = 3x^2 - 12 = 3(x - 2)(x + 2)$, zero at $x = \pm 2$. The sign is $+$ on $(-\infty, -2)$, $-$ on $(-2, 2)$ and $+$ on $(2, \infty)$. So $f$ increases on $(-\infty, -2)$ and $(2, \infty)$ and decreases on $(-2, 2)$. There is a local maximum $f(-2) = -8 + 24 = 16$ and a local minimum $f(2) = 8 - 24 = -16$.

Check: $f''(x) = 6x$ gives $f''(-2) = -12 < 0$ (maximum) and $f''(2) = 12 > 0$ (minimum).

</details>

2\. Find the intervals of concavity and the inflection points of $f(x) = x^4 - 6x^2$.

<details class="solution" markdown>
<summary>Solution</summary>

$f''(x) = 12x^2 - 12 = 12(x - 1)(x + 1)$, zero at $x = \pm 1$. It is positive for $x < -1$ and $x > 1$, and negative on $(-1, 1)$. So $f$ is concave up on $(-\infty, -1)$ and $(1, \infty)$ and concave down on $(-1, 1)$. The sign changes at both zeros, so the inflection points are $(-1, -5)$ and $(1, -5)$.

Check: $f(\pm 1) = 1 - 6 = -5$, and the function is even, so the two points mirror each other.

</details>

3\. Use the second derivative test to classify the critical point of $f(x) = x + \frac{1}{x}$ for $x > 0$, and say what convexity tells you about it.

<details class="solution" markdown>
<summary>Solution</summary>

$f'(x) = 1 - \frac{1}{x^2} = 0$ gives $x = 1$ (for $x > 0$). $f''(x) = \frac{2}{x^3}$, so $f''(1) = 2 > 0$: a local minimum with $f(1) = 2$. Since $f''(x) > 0$ for every $x > 0$, $f$ is convex on $(0, \infty)$, so by part (c) of the theorem the minimum is absolute: $x + \frac{1}{x} \ge 2$ for every $x > 0$.

Check: $f(2) = 2.5$ and $f(0.5) = 2.5$, both above 2.

</details>

### Standard

4\. Analyse $f(x) = \frac{1}{1 + x^2}$: symmetry, asymptote, the maximum, and the inflection points.

<details class="solution" markdown>
<summary>Solution</summary>

The function is even, defined for all $x$, positive, with $f(x) \to 0$ as $x \to \pm\infty$ (horizontal asymptote $y = 0$). $f'(x) = -\frac{2x}{(1 + x^2)^2}$ is positive for $x < 0$ and negative for $x > 0$, so $f$ has its maximum $f(0) = 1$. $f''(x) = \frac{2(3x^2 - 1)}{(1 + x^2)^3}$ is zero at $x = \pm\frac{1}{\sqrt{3}} \approx \pm 0.577$, positive for $\lvert x \rvert > \frac{1}{\sqrt{3}}$ and negative inside. So the graph is a bell: concave down near the peak and concave up in the tails, with inflection points at $\left(\pm\frac{1}{\sqrt{3}}, \frac{3}{4}\right)$.

Check: $f\left(\frac{1}{\sqrt{3}}\right) = \frac{1}{1 + 1/3} = \frac{3}{4}$.

</details>

5\. Sketch $f(x) = \frac{\ln x}{x}$ for $x > 0$. Find the limits at the ends of the domain, the maximum, and the inflection point.

<details class="solution" markdown>
<summary>Solution</summary>

Limits: as $x \to 0^+$, the numerator tends to $-\infty$ and the denominator to $0^+$, so $f \to -\infty$ (a vertical asymptote at $x = 0$). As $x \to \infty$, $f \to 0$ by the growth-rate theorem ($\ln x \ll x$), with $f > 0$ for $x > 1$. The only intercept is $f(1) = 0$.

$f'(x) = \frac{1 - \ln x}{x^2}$ is positive for $x < e$ and negative for $x > e$, so the maximum is $f(e) = \frac{1}{e} \approx 0.368$. $f''(x) = \frac{2\ln x - 3}{x^3}$ is negative for $x < e^{3/2}$ and positive after, so the inflection point is at $x = e^{3/2} \approx 4.482$, with $f = \frac{3/2}{e^{3/2}} \approx 0.335$.

Check: $f(1) = 0$, $f(e) = 0.368$, $f(4.482) = 0.335$ and $f(10) = 0.230$, a rise to $x = e$ and a slow decline after it.

</details>

6\. A total cost function is $C(q) = q^3 - 6q^2 + 15q$ dollars for $q \ge 0$. Show that the marginal cost has its minimum at $q = 2$, where $C$ has an inflection point, and give the economic meaning.

<details class="solution" markdown>
<summary>Solution</summary>

$C'(q) = 3q^2 - 12q + 15$ is the marginal cost, and $C''(q) = 6q - 12$. The marginal cost $C'$ has derivative $C''$, which is negative for $q < 2$ and positive for $q > 2$, so $C'$ falls until $q = 2$ and rises after it, with its minimum $C'(2) = 12 - 24 + 15 = 3$. At $q = 2$ the concavity of $C$ changes from down to up, an inflection point, with $C(2) = 8 - 24 + 30 = 14$.

In words: up to 2 units, each extra unit is cheaper than the last (for example, workers learn the job), and after 2 each extra unit costs more (the equipment gets crowded). The total cost is concave, then convex.

Check: $C'(1) = 6$, $C'(2) = 3$ and $C'(3) = 6$, with the least value at 2.

</details>

### Challenge

7\. Show that the cubic $f(x) = ax^3 + bx^2 + cx + d$ with $a \ne 0$ has exactly one inflection point, at $x = -\frac{b}{3a}$, and that if it has two critical points, the inflection point is halfway between them.

<details class="solution" markdown>
<summary>Solution</summary>

$f''(x) = 6ax + 2b$ is a line with nonzero slope, so it has exactly one zero, at $x = -\frac{b}{3a}$, and it changes sign there. So there is exactly one inflection point.

The critical points are the roots of $f'(x) = 3ax^2 + 2bx + c$. If there are two roots $r_1$ and $r_2$, their sum is $-\frac{2b}{3a}$ (by the sum of roots of a quadratic), so their average is $-\frac{b}{3a}$, which is the inflection point.

Check: for $f(x) = x^3 - 3x^2$, $a = 1$ and $b = -3$ give $-\frac{b}{3a} = 1$, and the critical points $0$ and $2$ have average 1, matching Example 5.

</details>

8\. (Reviews [rational functions and asymptotes](../../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md).) For $f(x) = \frac{2x^2 + 3x}{x + 1}$, use polynomial division to find the asymptotes, then show that $f$ has no local extrema.

<details class="solution" markdown>
<summary>Solution</summary>

Division gives $2x^2 + 3x = (x + 1)(2x + 1) - 1$, so $f(x) = 2x + 1 - \frac{1}{x + 1}$. The vertical asymptote is $x = -1$, and the slant asymptote is $y = 2x + 1$, since $\frac{1}{x + 1} \to 0$ as $x \to \pm\infty$.

Then $f'(x) = 2 + \frac{1}{(x + 1)^2} \ge 2 > 0$ wherever $f$ is defined, so $f'$ is never 0 and never changes sign. There are no critical points, so no local extrema. The function is increasing on $(-\infty, -1)$ and on $(-1, \infty)$. Also $f''(x) = -\frac{2}{(x + 1)^3}$, which is positive for $x < -1$ and negative for $x > -1$.

Check: $f(1) = \frac{5}{2} = 2.5$ and $2(1) + 1 - \frac{1}{2} = 2.5$.

</details>

## Where this shows up

- The next lesson, [optimization](05-optimization.md), uses these tests to decide whether a critical point of a word problem is the best choice, and uses convexity to avoid checking every candidate. The chapter's cheat sheet collects the sketching checklist.
- In economics, concave production and utility functions model diminishing returns, and convex cost curves model rising marginal cost (production and cost functions<!-- link: ../../07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md -->, utility and indifference curves<!-- link: ../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md -->).
- In CS, convex loss functions are the ones that gradient descent is sure to minimize, and the second derivative test becomes a test on a matrix of second derivatives for functions of several variables ([multivariable optimization and Lagrange multipliers](../09-multivariable-calculus-light/03-multivariable-optimization-and-lagrange-multipliers.md)). Sketching a function's growth is also the first step in comparing algorithms' running times.
