# The mean value theorem and extrema

After this lesson you can find the absolute maximum and minimum of a continuous function on a closed interval, state and prove Fermat's theorem, Rolle's theorem and the mean value theorem, and use them to prove that a derivative of zero means constant, that a positive derivative means increasing, and that inequalities such as $\lvert \sin a - \sin b \rvert \le \lvert a - b \rvert$ hold.

Before this: [the derivative definition](../02-derivatives/01-the-derivative-definition.md), [differentiation rules](../02-derivatives/02-differentiation-rules.md), [continuity, asymptotes and the IVT](../01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md) and [linear approximation and L'Hopital's rule](02-linear-approximation-and-lhopitals-rule.md). For the proof style, see [direct proof](../../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find the absolute maximum and minimum of $f(x) = x^3 - 3x$ on $[0, 2]$.
2. Find the number $c$ that the mean value theorem promises for $f(x) = \sqrt{x}$ on $[1, 9]$.
3. Why can't the mean value theorem be used for $f(x) = \lvert x \rvert$ on $[-1, 2]$?

<details class="solution" markdown>
<summary>Answers</summary>

1. $f'(x) = 3x^2 - 3 = 0$ at $x = 1$ (and $x = -1$, outside the interval). The values are $f(0) = 0$, $f(1) = -2$ and $f(2) = 2$. The maximum is 2, at $x = 2$, and the minimum is $-2$, at $x = 1$.
2. The slope of the chord is $\frac{3 - 1}{9 - 1} = \frac{1}{4}$. Solve $f'(c) = \frac{1}{2\sqrt{c}} = \frac{1}{4}$: $\sqrt{c} = 2$, so $c = 4$.
3. The chord slope is $\frac{2 - 1}{2 - (-1)} = \frac{1}{3}$, but $f'(x)$ is $-1$ or $1$ wherever it exists, never $\frac{1}{3}$. The theorem needs $f$ to be differentiable on the whole open interval, and $\lvert x \rvert$ has a corner at 0.

</details>

## The idea

A driver covers 100 km in exactly one hour. The average speed is 100 km/h. Is there a moment at which the speedometer reads exactly 100? The speed might have been 80 for half the trip and 120 for the other half, jumping between the two, but a car's speed can't jump: it passes through every value in between. So it was 100 at some moment. This is the mean value theorem in disguise, and the picture is a curve with a chord (the line through its end points) and a tangent line that is parallel to the chord.

Now a simpler picture. You walk a trail that starts and ends at the same elevation, and the trail has no cliffs or sudden corners. Somewhere on the walk you were at a highest point or a lowest point, and there the trail is level. That is Rolle's theorem, and the level spot is a point where the derivative is zero.

The two pictures are one idea in two forms, and the second is the special case of the first with a horizontal chord. The first half of the lesson turns it into theorems with proofs. The second half uses them: a function with zero derivative must be constant, a function with positive derivative must be increasing, and a bound on the derivative gives a bound on the function. These are the facts that make the curve sketching and optimization in the next lessons legitimate and not just plausible.

## Definitions

Let $f$ be a function with domain $D$. The function has an **absolute maximum** at $c \in D$ if $f(c) \ge f(x)$ for every $x \in D$, and an **absolute minimum** at $c$ if $f(c) \le f(x)$ for every $x \in D$. The number $f(c)$ is the maximum value or minimum value. In plain words, an absolute maximum is the highest point of the whole graph over $D$, and an absolute minimum is the lowest.

The function has a **local maximum** at $c$ if $f(c) \ge f(x)$ for all $x$ in some open interval around $c$ (within $D$), and a **local minimum** if $f(c) \le f(x)$ for all $x$ near $c$ in that sense. In plain words, a local maximum is a hilltop: the highest point in its neighbourhood, even if a higher hill is elsewhere. An **extremum** is a maximum or a minimum, and **extreme values** are their values.

A number $c$ in the domain of $f$ is a **critical point** of $f$ if $f'(c) = 0$ or $f'(c)$ does not exist. In plain words, a critical point is a place where the tangent line is horizontal, or where there is no tangent line (a corner or a cusp). The figure shows three critical points at $x = 0$, and only two of them are extrema.

![Three small graphs, each with a red dot at the origin. The graph of x squared has a horizontal tangent at the dot and a local minimum there. The graph of x cubed has a horizontal tangent at the dot but no extremum, since it rises through the dot. The graph of the absolute value of x has a corner at the dot, where the derivative does not exist, and a local minimum there.](../../assets/figures/05-university-core/mean-value-theorem-and-extrema-critical-points.svg)

The **extreme value theorem** says: if $f$ is continuous on a closed interval $[a, b]$, then $f$ has an absolute maximum and an absolute minimum on $[a, b]$. In plain words, a continuous function on a closed interval attains a highest and a lowest value. The proof depends on the completeness of the real numbers, the same property behind the intermediate value theorem, and is given in a first course in analysis. Here it is used without proof, and both conditions matter, as the figure shows.

![Three small graphs. The first is the graph of f(x) = x on the open interval from 0 to 1, with open circles at both ends, which has no maximum and no minimum. The second is the graph of 1 over x on the interval from 0 to 1, including 1 but not 0, which climbs without bound as x approaches 0 and so has no maximum. The third is a graph that rises along the line y = x from 0 to just below 1 at x equal to 1, and then jumps down to 0 and stays there until x equals 2, so the values come close to 1 without reaching it and there is no maximum.](../../assets/figures/05-university-core/mean-value-theorem-and-extrema-evt-fails.svg)

**Rolle's theorem.** If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$ and $f(a) = f(b)$, then there is a number $c \in (a, b)$ with $f'(c) = 0$.

**The mean value theorem (MVT).** If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then there is a number $c \in (a, b)$ with

$$
f'(c) = \frac{f(b) - f(a)}{b - a}.
$$

In plain words, somewhere between $a$ and $b$ the tangent line is parallel to the chord from $(a, f(a))$ to $(b, f(b))$, and the instantaneous rate of change equals the average rate of change. The conditions are the same in both theorems: continuous at the ends, differentiable inside. The figure shows both on one curve, where the MVT has two such numbers $c$.

![Two panels showing the graph of f(x) = x cubed over 3 minus 2 x squared plus 3x plus 1. On the left, the interval from 0 to 3 has f equal to 1 at both ends, and the horizontal tangent line at x equal to 1 touches the top of the hump, illustrating Rolle's theorem. On the right, the interval from 0 to 4 has a chord of slope one third, and two tangent lines parallel to it touch the curve near x equal to 0.85 and x equal to 3.15.](../../assets/figures/05-university-core/mean-value-theorem-and-extrema-rolle-and-mvt.svg)

## How to do it

### Finding absolute extrema on a closed interval

1. Check that $f$ is continuous on $[a, b]$. The extreme value theorem then guarantees that the maximum and the minimum exist.
2. Find the critical points of $f$ in the open interval $(a, b)$: solve $f'(x) = 0$ and find where $f'(x)$ doesn't exist but $f$ does.
3. Evaluate $f$ at each critical point and at both endpoints $a$ and $b$.
4. The largest of these values is the absolute maximum and the smallest is the absolute minimum. Say where each occurs.
5. Check against a sketch or a table of values.

The reason Step 3 is enough is the next theorem: an extremum in the interior can only occur at a critical point, and the other possibility is an endpoint.

### Fermat's theorem

*Theorem (Fermat).* If $f$ has a local maximum or a local minimum at an interior point $c$, and $f'(c)$ exists, then $f'(c) = 0$.

We know that $f(c) \ge f(x)$ for all $x$ near $c$ (the case of a local maximum), and that the limit $f'(c) = \lim_{h \to 0}\frac{f(c + h) - f(c)}{h}$ exists. We want to show that this limit is 0. The plan is to look at the one-sided limits of the difference quotient: from the right it is at most 0 and from the left it is at least 0, so the common value is 0.

*Proof.* Take $\delta > 0$ such that $f(x) \le f(c)$ whenever $\lvert x - c \rvert < \delta$. Then $f(c + h) - f(c) \le 0$ for every $h$ with $\lvert h \rvert < \delta$.

For $0 < h < \delta$ the quotient $\frac{f(c + h) - f(c)}{h}$ has a numerator at most 0 and a positive denominator, so it is at most 0. Letting $h \to 0^+$ gives $f'(c) \le 0$.

For $-\delta < h < 0$ the numerator is at most 0 and the denominator is negative, so the quotient is at least 0. Letting $h \to 0^-$ gives $f'(c) \ge 0$.

Both hold, so $f'(c) = 0$. For a local minimum, apply the argument to $-f$, which has a local maximum at $c$ and the derivative $-f'(c)$. $\blacksquare$

Look back at what the theorem doesn't say. It says that a local extremum at $c$ forces $f'(c) = 0$ if the derivative exists, and not the reverse: $x^3$ has $f'(0) = 0$ and no extremum (see the figure). Fermat's theorem is a filter, and the critical points are the candidates that survive it.

### Rolle's theorem

*Theorem (Rolle).* If $f$ is continuous on $[a, b]$, differentiable on $(a, b)$ and $f(a) = f(b)$, then $f'(c) = 0$ for some $c \in (a, b)$.

We know the three conditions. We want a point where the derivative is 0. The plan is to find an interior extremum with the extreme value theorem and then apply Fermat's theorem.

*Proof.* By the extreme value theorem, $f$ has an absolute maximum value $M$ and an absolute minimum value $m$ on $[a, b]$. There are two cases.

If $M = m$, then $f$ is constant, so $f'(x) = 0$ for every $x \in (a, b)$, and any $c$ works.

If $M \ne m$, then at least one of $M$ and $m$ is different from the common value $f(a) = f(b)$. Suppose $M \ne f(a)$. Then the maximum is not attained at $a$ or at $b$, so it is attained at some $c \in (a, b)$. That point is a local maximum, and $f$ is differentiable at $c$, so $f'(c) = 0$ by Fermat's theorem. If instead $m \ne f(a)$, the same argument works with the minimum. $\blacksquare$

Look back at where each hypothesis was used. Continuity gave the extremum, the equal end values pushed it into the interior, and differentiability let Fermat's theorem apply. Remove any one and the theorem fails: $f(x) = \lvert x \rvert$ on $[-1, 1]$ has equal end values but a corner, $f(x) = x$ on $[0, 1)$ with $f(1) = 0$ has a jump, and $f(x) = x$ on $[0, 1]$ has different end values.

### The mean value theorem

*Theorem (MVT).* If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then $f'(c) = \frac{f(b) - f(a)}{b - a}$ for some $c \in (a, b)$.

We know the same two conditions as Rolle's theorem, but no condition on the end values. We want a point where the tangent is parallel to the chord. The plan is to subtract the chord from $f$, which leaves a function with equal end values, and then apply Rolle's theorem.

*Proof.* Let $m = \frac{f(b) - f(a)}{b - a}$, the slope of the chord, and define

$$
h(x) = f(x) - f(a) - m(x - a).
$$

This is $f$ minus the chord line, so it measures the vertical gap between the curve and the chord. It is continuous on $[a, b]$ and differentiable on $(a, b)$, since $f$ is and the line is. Also $h(a) = 0$ and $h(b) = f(b) - f(a) - m(b - a) = 0$ by the choice of $m$. By Rolle's theorem there is $c \in (a, b)$ with $h'(c) = 0$. Since $h'(x) = f'(x) - m$, this gives $f'(c) = m$. $\blacksquare$

Look back at the idea: tilting the picture until the chord is horizontal turns the MVT into Rolle's theorem. The theorem says that $c$ exists, and not where it is or whether it is unique: in the figure there are two.

### What the mean value theorem gives you

Every use of the MVT has the same shape. Take two points $x < y$ in an interval, apply the theorem on $[x, y]$ to get $f(y) - f(x) = f'(c)(y - x)$ for some $c$ between them, and read off what the sign or size of $f'(c)$ tells you.

*Theorem (zero derivative).* If $f'(x) = 0$ for every $x$ in an interval $I$, then $f$ is constant on $I$.

We know $f'$ is 0 everywhere on $I$. We want $f(x) = f(y)$ for every pair of points. The plan is to apply the MVT on the interval between the two points.

*Proof.* Take any $x < y$ in $I$. Then $f$ is differentiable on $[x, y] \subseteq I$, so it is continuous there, and the MVT gives $c \in (x, y)$ with $f(y) - f(x) = f'(c)(y - x) = 0 \cdot (y - x) = 0$. So $f(y) = f(x)$. $\blacksquare$

*Corollary.* If $f'(x) = g'(x)$ for every $x$ in an interval, then $f - g$ is constant there, since $(f - g)' = 0$. In plain words, two functions with the same derivative differ by a constant. This is why an antiderivative is determined only up to "$+ C$" ([the fundamental theorem of calculus](../04-integrals/02-fundamental-theorem-of-calculus.md) uses it).

*Theorem (sign of the derivative).* Let $f$ be continuous on an interval $I$ and differentiable at every interior point. If $f'(x) > 0$ for all interior $x$, then $f$ is strictly increasing on $I$, which means $f(x) < f(y)$ whenever $x < y$. If $f'(x) \ge 0$ for all interior $x$, then $f$ is nondecreasing, $f(x) \le f(y)$ whenever $x < y$. The same with the inequalities reversed gives decreasing.

*Proof.* Take $x < y$ in $I$. The MVT gives $c \in (x, y)$ with $f(y) - f(x) = f'(c)(y - x)$. Since $y - x > 0$, the sign of $f(y) - f(x)$ is the sign of $f'(c)$: positive if $f' > 0$ everywhere, and not negative if $f' \ge 0$ everywhere. $\blacksquare$

Look back at two points. The theorem is about an interval: $f(x) = -\frac{1}{x}$ has $f'(x) = \frac{1}{x^2} > 0$ at every point of its domain, but $f(-1) = 1$ and $f(1) = -1$, so it is not increasing on the whole domain, which is two intervals. And the converse of the strict statement is false: $x^3$ is strictly increasing with $f'(0) = 0$. (For differentiable $f$, "$f$ nondecreasing" does imply $f' \ge 0$, since every difference quotient is then at least 0.)

### Inequalities from the mean value theorem

The MVT turns a bound on a derivative into a bound on a function. If $\lvert f'(t) \rvert \le K$ between $x$ and $y$, then $\lvert f(y) - f(x) \rvert = \lvert f'(c) \rvert\,\lvert y - x \rvert \le K\lvert y - x \rvert$.

*Theorem.* For all real $a$ and $b$, $\lvert \sin a - \sin b \rvert \le \lvert a - b \rvert$.

*Proof.* If $a = b$ both sides are 0. Otherwise the MVT for $\sin$ on the interval between $a$ and $b$ gives $c$ with $\sin b - \sin a = (\cos c)(b - a)$. Since $\lvert \cos c \rvert \le 1$, the result follows. $\blacksquare$

With $b = 0$ this says $\lvert \sin a \rvert \le \lvert a \rvert$, the fact that the graph of $\sin x$ stays inside the lines $y = \pm x$.

*Theorem.* $e^x > 1 + x$ for every real $x \ne 0$.

*Proof.* Take $x > 0$. The MVT for $e^t$ on $[0, x]$ gives $c \in (0, x)$ with $e^x - 1 = e^c \cdot x$. Since $c > 0$, $e^c > 1$, so $e^x - 1 > x$. Take $x < 0$. The MVT on $[x, 0]$ gives $c \in (x, 0)$ with $1 - e^x = e^c(0 - x) = -e^c x$, so $e^x = 1 + e^c x$. Since $c < 0$, $e^c < 1$, and multiplying by $x < 0$ reverses the inequality: $e^c x > x$. So $e^x > 1 + x$. $\blacksquare$

The tangent line to $e^x$ at 0 is $y = 1 + x$, so this says that the curve lies above its tangent line there. [Concavity and curve sketching](04-concavity-and-curve-sketching.md) shows that this happens for every convex function.

### Cauchy's mean value theorem

This version compares two functions, and it is the tool behind L'Hopital's rule and the error bound that follow.

*Theorem (Cauchy).* If $f$ and $g$ are continuous on $[a, b]$ and differentiable on $(a, b)$, and $g'(x) \ne 0$ for every $x \in (a, b)$, then $g(b) \ne g(a)$ and there is a number $c \in (a, b)$ with

$$
\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(c)}{g'(c)}.
$$

*Proof.* If $g(b) = g(a)$, Rolle's theorem would give a point where $g' = 0$, which is excluded. So $g(b) \ne g(a)$, and we may define $K = \frac{f(b) - f(a)}{g(b) - g(a)}$ and

$$
h(x) = f(x) - f(a) - K\bigl(g(x) - g(a)\bigr).
$$

Then $h(a) = 0$, and $h(b) = (f(b) - f(a)) - K(g(b) - g(a)) = 0$. Rolle's theorem gives $c \in (a, b)$ with $h'(c) = f'(c) - Kg'(c) = 0$, and so $\frac{f'(c)}{g'(c)} = K$. $\blacksquare$

With $g(x) = x$ this is the ordinary MVT.

### The error of a tangent line approximation

[Linear approximation and L'Hopital's rule](02-linear-approximation-and-lhopitals-rule.md) claimed that the error of the tangent line is about $\frac{1}{2}f''(a)(x - a)^2$. Here is the exact statement.

*Theorem.* Let $f$ be twice differentiable on an interval containing $a$ and $x$, with $x > a$ (the case $x < a$ is the same). Then there is a number $d$ between $a$ and $x$ with

$$
f(x) = f(a) + f'(a)(x - a) + \frac{1}{2}f''(d)(x - a)^2.
$$

So if $\lvert f''(t) \rvert \le M$ for all $t$ between $a$ and $x$, then $\lvert f(x) - L(x) \rvert \le \frac{M}{2}(x - a)^2$, where $L$ is the linearization at $a$.

We know that $f''$ exists, so $f'$ is differentiable and the error function can be differentiated twice. We want the error written with $f''$ at some unknown point. The plan is to apply Cauchy's theorem to the error and to $(t - a)^2$, and then the ordinary MVT to $f'$.

*Proof.* Let $E(t) = f(t) - f(a) - f'(a)(t - a)$, the error of the tangent line, and $G(t) = (t - a)^2$. Then $E(a) = G(a) = 0$, and $G'(t) = 2(t - a) \ne 0$ for $t \in (a, x)$. Cauchy's theorem on $[a, x]$ gives $c \in (a, x)$ with

$$
\frac{E(x)}{G(x)} = \frac{E(x) - E(a)}{G(x) - G(a)} = \frac{E'(c)}{G'(c)} = \frac{f'(c) - f'(a)}{2(c - a)}.
$$

Now the MVT for $f'$ on $[a, c]$ gives $d \in (a, c)$ with $f'(c) - f'(a) = f''(d)(c - a)$. So $\frac{E(x)}{(x - a)^2} = \frac{f''(d)}{2}$, which is the formula. The bound follows from $\lvert f''(d) \rvert \le M$. $\blacksquare$

Look back at the formula. It says that the tangent line's error is a second derivative, taken somewhere between $a$ and $x$, times $\frac{(x - a)^2}{2}$. Where $f'' > 0$ the error $f - L$ is positive, so the curve is above its tangent line. For $\sqrt{4.1}$ the second derivative is $-\frac{1}{4}t^{-3/2}$, which is $-0.03125$ at $t = 4$ and $-0.03011$ at $t = 4.1$. The true error is $f(4.1) - L(4.1) = -0.000154$, and $\frac{1}{2}f''(d)(0.1)^2$ matches it when $f''(d) = -0.0309$, which happens at $d \approx 4.03$, inside $(4, 4.1)$ as the theorem says.

### L'Hopital's rule, proved

The case $\frac{0}{0}$ of the rule at a finite point follows from Cauchy's theorem.

*Theorem.* Let $f$ and $g$ be differentiable on $(a, b)$ with $g'(x) \ne 0$ there, and $f(x) \to 0$ and $g(x) \to 0$ as $x \to a^+$. If $\frac{f'(x)}{g'(x)} \to L$ as $x \to a^+$, where $L$ is a real number or $\pm\infty$, then $\frac{f(x)}{g(x)} \to L$ as $x \to a^+$.

*Proof.* Define $f(a) = g(a) = 0$. This makes $f$ and $g$ continuous on $[a, x]$ for each $x \in (a, b)$, and they are differentiable on $(a, x)$. Cauchy's theorem on $[a, x]$ gives $c_x \in (a, x)$ with

$$
\frac{f(x)}{g(x)} = \frac{f(x) - f(a)}{g(x) - g(a)} = \frac{f'(c_x)}{g'(c_x)}.
$$

As $x \to a^+$, the number $c_x$ is squeezed between $a$ and $x$, so $c_x \to a^+$, and $\frac{f'(c_x)}{g'(c_x)} \to L$. So $\frac{f(x)}{g(x)} \to L$. $\blacksquare$

The left-hand limit is the same with the interval $[x, a]$, and the two together give the two-sided rule. The cases $x \to \infty$ and $\frac{\infty}{\infty}$ need extra steps, and are in any analysis text.

## Worked examples

<div class="example" markdown>

### Example 1: absolute extrema on a closed interval

Find the absolute maximum and minimum of $f(x) = x^3 - 3x^2 + 1$ on $[-0.5, 3.5]$.

Step 1: $f$ is a polynomial, so it is continuous, and the extreme value theorem applies.

Step 2: $f'(x) = 3x^2 - 6x = 3x(x - 2)$ is defined everywhere and is zero at $x = 0$ and $x = 2$. Both are in $(-0.5, 3.5)$.

Step 3: evaluate at the two critical points and the two endpoints:

| $x$ | $-0.5$ | $0$ | $2$ | $3.5$ |
|---|---|---|---|---|
| $f(x)$ | $0.125$ | $1$ | $-3$ | $7.125$ |

Step 4: the absolute maximum is $7.125$, at the endpoint $x = 3.5$, and the absolute minimum is $-3$, at the critical point $x = 2$. The critical point $x = 0$ is a local maximum but not an absolute one.

![The graph of x cubed minus 3 x squared plus 1 on the interval from minus 0.5 to 3.5. A blue dot at x equal to 0 is labelled local max, value 1. A red dot at x equal to 2 is labelled absolute min, value minus 3. A red dot at the right end, x equal to 3.5, is labelled absolute max, value 7.125, and an orange dot at the left end is labelled endpoint, value 0.125.](../../assets/figures/05-university-core/mean-value-theorem-and-extrema-extrema.svg)

Check: the graph in the figure agrees, and a grid of 100,000 values on the interval (in the code below) finds the same two points. Without the endpoint check the answer would be wrong: $x = 0$ looks like the maximum, but the function goes on rising to $7.125$.

</div>

<div class="example" markdown>

### Example 2: finding the number the MVT promises

Find $c$ for $f(x) = x^3$ on $[0, 2]$, and check the hypotheses.

The function is a polynomial, so it is continuous on $[0, 2]$ and differentiable on $(0, 2)$. The chord slope is $\frac{8 - 0}{2 - 0} = 4$. Solve $f'(c) = 3c^2 = 4$, so $c = \pm\frac{2}{\sqrt{3}}$, and only $c = \frac{2}{\sqrt{3}} \approx 1.1547$ is in $(0, 2)$.

Check: $f'(1.1547) = 3 \cdot 1.3333 = 4$, which is the chord slope. A function that fails the hypotheses can fail the conclusion: $f(x) = \frac{1}{x}$ on $[-1, 1]$ has chord slope $\frac{1 - (-1)}{1 - (-1)} = 1$, but $f'(x) = -\frac{1}{x^2}$ is never positive, because $f$ is not even defined at 0.

</div>

<div class="example" markdown>

### Example 3: exactly one root

Show that $2x + \cos x = 0$ has exactly one real solution.

Let $f(x) = 2x + \cos x$. Existence first: $f(-1) = -2 + 0.540 < 0$ and $f(0) = 1 > 0$, and $f$ is continuous, so by the intermediate value theorem there is a root in $(-1, 0)$.

Uniqueness: suppose there were two roots $r_1 < r_2$. Then $f(r_1) = f(r_2) = 0$, and Rolle's theorem would give $c$ between them with $f'(c) = 0$. But $f'(x) = 2 - \sin x \ge 1$ for every $x$, so $f'$ is never 0. That is a contradiction, so there is only one root.

Check: bisection finds the root at $x \approx -0.4502$, and $2(-0.4502) + \cos(-0.4502) = -0.9004 + 0.9004 = 0$. Because $f' > 0$ everywhere, the function is increasing, which is also why it can cross the axis only once.

</div>

<div class="example" markdown>

### Example 4: a critical point where the derivative does not exist

Find the absolute extrema of $f(x) = x^{2/3}$ on $[-1, 8]$.

The function is continuous. For $x \ne 0$, $f'(x) = \frac{2}{3}x^{-1/3}$, which is never 0. At $x = 0$ the derivative doesn't exist (the graph has a cusp, as in [the derivative definition](../02-derivatives/01-the-derivative-definition.md)), but $0$ is in the domain, so it is a critical point.

The values are $f(-1) = 1$, $f(0) = 0$ and $f(8) = 4$. The absolute maximum is 4, at $x = 8$, and the absolute minimum is 0, at the cusp $x = 0$.

Check: $x^{2/3} \ge 0$ for all $x$, so 0 is certainly the minimum. Solving $f'(x) = 0$ alone would have found no candidates at all, which is why the second half of the definition of critical point matters.

</div>

<div class="example" markdown>

### Example 5: absolute extrema (finish it yourself)

Find the absolute maximum and minimum of $f(x) = x + \frac{4}{x}$ on $[1, 5]$.

The function is continuous on $[1, 5]$, because $0$ is outside the interval. Its derivative is $f'(x) = 1 - \frac{4}{x^2}$.

<details class="solution" markdown>
<summary>Finish</summary>

Set $f'(x) = 0$: $x^2 = 4$, so $x = 2$ (the root $-2$ is outside the interval). The derivative exists on all of $[1, 5]$.

The values are $f(1) = 5$, $f(2) = 4$ and $f(5) = 5.8$. The absolute maximum is $5.8$, at $x = 5$, and the absolute minimum is $4$, at $x = 2$.

Check: $f'(x) < 0$ for $1 \le x < 2$ and $f'(x) > 0$ for $x > 2$, so $f$ falls to $x = 2$ and rises after it, which agrees with the three values.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: skipping the endpoints. On a closed interval the maximum and minimum often sit at an end. In Example 1 the maximum is at $x = 3.5$, and the interior critical points never reach it.

</div>

<div class="warning" markdown>

Watch out: believing that $f'(c) = 0$ means an extremum. It is only a candidate. $f(x) = x^3$ has $f'(0) = 0$ and rises straight through it. Test the candidate with values on both sides, or with the tests in [concavity and curve sketching](04-concavity-and-curve-sketching.md).

</div>

<div class="warning" markdown>

Watch out: forgetting critical points where $f'$ doesn't exist. $\lvert x \rvert$ has its minimum at 0 and $x^{2/3}$ has its minimum at 0, and in each case $f'(0)$ doesn't exist, so solving $f'(x) = 0$ finds nothing.

</div>

<div class="warning" markdown>

Watch out: using the mean value theorem without checking its two conditions. Differentiable on the open interval and continuous on the closed interval are both required. $\lvert x \rvert$ on $[-1, 2]$ fails the first, and a function with a jump fails the second.

</div>

<div class="warning" markdown>

Watch out: treating the MVT as a way to find $c$ or to say it is unique. It only says that some $c$ exists. In the figure there are two, and for a function such as $f(x) = x$ every point works.

</div>

<div class="warning" markdown>

Watch out: applying "positive derivative means increasing" to a set that isn't an interval. $f(x) = -\frac{1}{x}$ has a positive derivative at every point of its domain, but $f(-1) = 1 > f(1) = -1$. The domain is two intervals, and the function increases on each of them separately.

</div>

## Tricks and shortcuts

When asked for the extrema of a continuous function on a closed interval, write the candidates in a table, one column for each endpoint and critical point. It makes it hard to forget an endpoint.

For an absolute extremum on an interval that isn't closed, the closed interval method doesn't apply directly. Check the limits at the missing ends (does $f$ go to $\infty$, or settle on a value?), and then compare with the critical points. [Optimization](05-optimization.md) uses this.

To prove "at most one root", use Rolle's theorem: two roots would force a zero of $f'$ between them. To prove "at least one root", use the intermediate value theorem. Together they prove "exactly one", as in Example 3.

To prove an inequality about a function, apply the MVT to it between the two points and bound the derivative at the unknown point $c$.

## In code

The first part runs the closed interval method on Example 1 and checks it against a fine grid. The second finds the MVT number for $x^3$ by bisection. The third checks $\lvert \sin a - \sin b \rvert \le \lvert a - b \rvert$ on random pairs and looks at the largest ratio.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import random

f = lambda x: x**3 - 3 * x**2 + 1
a, b = -0.5, 3.5

# Closed interval method: endpoints and critical points (f'(x) = 0 at x = 0 and x = 2).
candidates = [a, 0.0, 2.0, b]
for x in candidates:
    print(x, f(x))
print("max", max(candidates, key=f), "min", min(candidates, key=f))
# -0.5 0.125
# 0.0 1.0
# 2.0 -3.0
# 3.5 7.125
# max 3.5 min 2.0

# A brute-force check on a fine grid.
n = 100_000
xs = [a + (b - a) * i / n for i in range(n + 1)]
print(round(max(xs, key=f), 4), round(min(xs, key=f), 4))
# 3.5 2.0

# Mean value theorem for g(x) = x**3 on [0, 2]: find c with g'(c) = chord slope.
g = lambda x: x**3
gp = lambda x: 3 * x**2
lo, hi = 0.0, 2.0
slope = (g(hi) - g(lo)) / (hi - lo)
for _ in range(60):
    mid = (lo + hi) / 2
    if gp(mid) < slope:
        lo = mid
    else:
        hi = mid
print(slope, round(lo, 6), round(2 / math.sqrt(3), 6))
# 4.0 1.154701 1.154701

# |sin a - sin b| / |a - b| never exceeds 1.
random.seed(1)
worst = max(
    abs(math.sin(p) - math.sin(q)) / abs(p - q)
    for p, q in ((random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(10_000))
)
print(round(worst, 4))
# 0.9995
```

The grid agrees with the candidates, the bisection finds $\frac{2}{\sqrt{3}}$, and the largest ratio is just under 1, as the theorem predicts. A test like this never proves the inequality, but it would catch a wrong claim quickly.

</details>

## FAQ

### Why prove the mean value theorem when the picture already convinces me?

Because the pictures that convince you are pictures of nice functions, and a theorem has to hold for every function that meets its conditions, including ones that nobody can draw. The proof also shows exactly what is needed: the same statement is false for functions with a corner, a jump or a gap in the domain, and the proof says where each assumption was used. In the same way, "a function with zero derivative is constant" looks plain on a graph, but it is the MVT that proves it, and the proof is what lets you use it for an integral.

### Does the mean value theorem work for functions on the rational numbers, or only the real numbers?

Only for the real numbers. The proof uses the extreme value theorem, which depends on the real number line having no gaps. If you work only with rational numbers, $f(x) = x^3$ on $[0, 2]$ needs $c = \frac{2}{\sqrt{3}}$, which is irrational, so no rational $c$ exists. Over the rationals the MVT can fail.

### What is the difference between a critical point and an extremum?

A critical point is a candidate, defined by the derivative: it is where $f'$ is 0 or doesn't exist. An extremum is a fact about values: it is where $f$ is highest or lowest nearby (local) or everywhere (absolute). Every interior extremum is a critical point (Fermat's theorem plus the corner and cusp cases), but a critical point may be neither, as for $x^3$ at 0.

### Is the number $c$ in the MVT the midpoint of the interval?

Not usually. For $f(x) = \sqrt{x}$ on $[1, 9]$ the number is $c = 4$, and the midpoint is 5. For a quadratic function $f(x) = px^2 + qx + r$ it is the midpoint exactly, because $f'$ is a line and the chord slope is the value of $f'$ at the midpoint. This is the midpoint trick from [rates of change and marginal analysis](01-rates-of-change-and-marginal-analysis.md).

## Practice

### Warm-up

1\. Find the absolute maximum and minimum of $f(x) = x^2 - 4x + 5$ on $[0, 5]$.

<details class="solution" markdown>
<summary>Solution</summary>

$f'(x) = 2x - 4 = 0$ at $x = 2$. The values are $f(0) = 5$, $f(2) = 1$ and $f(5) = 10$. The maximum is 10, at $x = 5$, and the minimum is 1, at $x = 2$.

Check: $f(x) = (x - 2)^2 + 1$, so the vertex $(2, 1)$ is the lowest point, and the farthest end from $x = 2$ is $x = 5$, which gives the highest.

</details>

2\. Check the hypotheses of Rolle's theorem for $f(x) = x^3 - x$ on $[-1, 1]$, and find every $c$ that it gives.

<details class="solution" markdown>
<summary>Solution</summary>

$f$ is a polynomial, so it is continuous and differentiable, and $f(-1) = 0 = f(1)$. Then $f'(x) = 3x^2 - 1 = 0$ gives $x = \pm\frac{1}{\sqrt{3}} \approx \pm 0.577$, and both are in $(-1, 1)$.

Check: $f'(0.5774) = 3(0.3333) - 1 = 0$.

</details>

3\. True or false, with an example or a reason: (a) if $f'(c) = 0$, then $f$ has a local extremum at $c$; (b) if $f$ has a local minimum at $c$, then $f'(c) = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) False. $f(x) = x^3$ has $f'(0) = 0$ but is increasing through 0.

(b) False as stated. $f(x) = \lvert x \rvert$ has a local minimum at 0 and $f'(0)$ doesn't exist. It is true if $f'(c)$ exists, which is Fermat's theorem.

Check: both counterexamples are in the figure of critical points.

</details>

### Standard

4\. Use the mean value theorem to prove that $\ln(1 + x) < x$ for every $x > 0$.

<details class="solution" markdown>
<summary>Solution</summary>

Let $f(t) = \ln(1 + t)$ on $[0, x]$. It is continuous and differentiable, with $f'(t) = \frac{1}{1 + t}$. The MVT gives $c \in (0, x)$ with $\ln(1 + x) - \ln 1 = \frac{1}{1 + c}\cdot x$. Since $c > 0$, $\frac{1}{1 + c} < 1$, so $\ln(1 + x) < x$.

Check: for $x = 0.5$, $\ln 1.5 = 0.405 < 0.5$.

</details>

5\. Show that $x^3 + 3x - 5 = 0$ has exactly one real root, and say between which integers it lies.

<details class="solution" markdown>
<summary>Solution</summary>

Let $f(x) = x^3 + 3x - 5$. Then $f(1) = -1 < 0$ and $f(2) = 9 > 0$, and $f$ is continuous, so there is a root in $(1, 2)$ by the intermediate value theorem. Also $f'(x) = 3x^2 + 3 \ge 3 > 0$, so $f$ is strictly increasing and cannot have two roots (two roots would force $f'(c) = 0$ by Rolle's theorem).

Check: the root is $x \approx 1.1542$, and $1.1542^3 + 3(1.1542) - 5 = 1.5376 + 3.4626 - 5 = 0.0002$, which is 0 to rounding.

</details>

6\. Find the absolute extrema of $f(x) = \lvert x^2 - 1 \rvert$ on $[-2, 2]$.

<details class="solution" markdown>
<summary>Solution</summary>

The function is continuous. It equals $x^2 - 1$ for $\lvert x \rvert \ge 1$ and $1 - x^2$ for $\lvert x \rvert < 1$. Its derivative is $2x$ for $\lvert x \rvert > 1$, $-2x$ for $\lvert x \rvert < 1$, and doesn't exist at $x = \pm 1$ (a corner: at each of $x = -1$ and $x = 1$ the slope is $-2$ just to the left and $2$ just to the right). So the critical points are $x = 0$ (where $f' = 0$) and $x = \pm 1$.

The values are $f(-2) = 3$, $f(-1) = 0$, $f(0) = 1$, $f(1) = 0$ and $f(2) = 3$. The maximum is 3, at $x = \pm 2$, and the minimum is 0, at $x = \pm 1$.

Check: $f \ge 0$ always, and $f(\pm 1) = 0$, so 0 is the minimum. The largest of $x^2 - 1$ on $[-2, 2]$ is at the ends, $3$.

</details>

### Challenge

7\. Prove that if $f$ is differentiable on an interval $I$ and $f'(x) \ne 0$ for all $x \in I$, then $f$ is one-to-one on $I$. Then show that $f(x) = x^5 + x^3 + x$ has an inverse function on $\mathbb{R}$.

<details class="solution" markdown>
<summary>Solution</summary>

Suppose, for contradiction, that $f(x_1) = f(x_2)$ with $x_1 < x_2$ in $I$. Then $f$ is continuous on $[x_1, x_2]$ and differentiable on $(x_1, x_2)$, with equal values at the ends, so Rolle's theorem gives $c \in (x_1, x_2)$ with $f'(c) = 0$. This contradicts the assumption. So $f(x_1) \ne f(x_2)$ whenever $x_1 \ne x_2$.

For $f(x) = x^5 + x^3 + x$ the derivative is $5x^4 + 3x^2 + 1 \ge 1 > 0$ for every $x$, so $f$ is one-to-one on $\mathbb{R}$. A one-to-one function has an inverse defined on its range. Here the range is all of $\mathbb{R}$, since $f$ is continuous and $f(x) \to \pm\infty$ as $x \to \pm\infty$, so the inverse is defined for every real number.

Check: $f(0) = 0$, $f(1) = 3$ and $f(-1) = -3$, increasing as expected.

</details>

8\. (Reviews [continuity, asymptotes and the IVT](../01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md).) Show that $\cos x = x$ has exactly one real solution, and that it lies in $(0, 1)$.

<details class="solution" markdown>
<summary>Solution</summary>

Let $f(x) = \cos x - x$. It is continuous, with $f(0) = 1 > 0$ and $f(1) = \cos 1 - 1 = -0.4597 < 0$, so the intermediate value theorem gives a root in $(0, 1)$.

For uniqueness inside $(0, 1)$: there $\sin x > 0$, so $f'(x) = -\sin x - 1 < -1 < 0$. Two roots in $(0, 1)$ would give a zero of $f'$ between them by Rolle's theorem, which is impossible. For roots outside $(0, 1)$: if $x \ge 1$ then $\cos x \le 1 \le x$ with $\cos x < x$ because $\cos 1 < 1$, so $f(x) < 0$. If $-1 \le x \le 0$ then $\cos x \ge \cos 1 > 0$ and $-x \ge 0$, so $f(x) > 0$. If $x < -1$ then $\cos x \ge -1$ and $-x > 1$, so $f(x) > 0$. So there are no roots outside $(0, 1)$, and exactly one inside.

Check: the root is $x = 0.7390851\ldots$, the same number that Newton's method found in [linear approximation and L'Hopital's rule](02-linear-approximation-and-lhopitals-rule.md).

</details>

## Where this shows up

- The next lesson, [concavity and curve sketching](04-concavity-and-curve-sketching.md), builds the first derivative test on the sign-of-the-derivative theorem, and [optimization](05-optimization.md) uses the closed interval method on word problems.
- In CS, a bound on a derivative is a bound on how fast a function can change, called a Lipschitz constant: if $\lvert f'(x) \rvert \le K$ then $\lvert f(a) - f(b) \rvert \le K\lvert a - b \rvert$, which follows from the MVT. Step-size bounds for gradient descent and error bounds for numerical methods are built this way. Bisection works because of the intermediate value theorem, and the error formula for a tangent line above is the starting point for the convergence proof of Newton's method.
- In economics, the sign-of-the-derivative theorem is how marginal analysis reads the direction of change: if marginal cost is positive on an interval, then total cost is increasing there, with no need to look at the graph ([marginal analysis with derivatives](../../07-economics-math/03-firms-and-consumers/01-marginal-analysis-with-derivatives.md)).
