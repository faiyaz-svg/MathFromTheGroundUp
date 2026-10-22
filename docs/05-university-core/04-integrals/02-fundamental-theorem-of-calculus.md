# The fundamental theorem of calculus

After this lesson you can define and differentiate an accumulation function, state and prove both parts of the fundamental theorem of calculus, find antiderivatives of the basic functions, evaluate definite integrals by subtraction, and turn a rate (a marginal cost, a velocity) into a total.

Before this: [Riemann sums and the definite integral](01-riemann-sums-and-the-definite-integral.md), [differentiation rules](../02-derivatives/02-differentiation-rules.md), [the chain rule](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md) and [the mean value theorem](../03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md), which the proof of part 2 uses. The proof of part 1 uses the [extreme value theorem](../01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#the-extreme-value-theorem).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find $\dfrac{d}{dx}\displaystyle\int_1^x \sin\left(t^2\right)dt$.
2. Evaluate $\displaystyle\int_1^4 \sqrt{x}\,dx$.
3. A firm's marginal cost is $4 + 0.02q$ dollars per unit at output $q$. How much does production cost rise when output goes from 100 to 200 units?

<details class="solution" markdown>
<summary>Answers</summary>

1. The derivative of an integral with respect to its upper limit gives back the integrand evaluated at the limit: $\sin\left(x^2\right)$.
2. An antiderivative of $x^{1/2}$ is $\frac{2}{3}x^{3/2}$, so the integral is $\frac{2}{3}\left(4^{3/2} - 1^{3/2}\right) = \frac{2}{3}(8 - 1) = \frac{14}{3}$.
3. The rise in cost is the integral of marginal cost: $\int_{100}^{200}(4 + 0.02q)\,dq = \left[4q + 0.01q^2\right]_{100}^{200} = (800 + 400) - (400 + 100) = 700$ dollars.

</details>

## The idea

Water flows into a tank at a rate of $r(t)$ litres per minute, and $V(t)$ is the volume in the tank at time $t$. The rate of change of the volume is the flow rate: $V'(t) = r(t)$. That is a statement about derivatives. Now ask how much water came in between $t = a$ and $t = b$. You can read the volume at both times and subtract, which gives $V(b) - V(a)$. Or you can chop the time into small pieces, multiply the flow rate on each piece by its duration, and add. In the limit that is the integral $\int_a^b r(t)\,dt$. Both methods measure the same water, so

$$
\int_a^b r(t)\,dt = V(b) - V(a), \qquad \text{where } V' = r.
$$

This is the fundamental theorem of calculus. It says that finding the area under a curve, a limit of sums, is the same job as undoing a derivative. To integrate $r$, find a function $V$ whose derivative is $r$, and subtract two values of it. The last lesson took a limit of $n$ rectangle areas, with a sum formula, to get $\int_0^1 x^2\,dx = \frac{1}{3}$. The theorem gets it in one line: $x^3$ has derivative $3x^2$, so $\frac{x^3}{3}$ has derivative $x^2$, and the integral is $\frac{1^3}{3} - \frac{0^3}{3} = \frac{1}{3}$.

The theorem has two parts, and they say two different things. Part 1 says that if you build a function by accumulating area, $F(x) = \int_a^x f(t)\,dt$, then the slope of $F$ at $x$ is the height of $f$ at $x$. In the figure, the top graph is $f(t) = \sin t$ and the bottom graph is the area accumulated so far. The area function rises while $f$ is positive and falls while $f$ is negative, and it is flat at the top where $f$ crosses zero.

![Two graphs sharing the horizontal axis from 0 to 2 pi. The top graph is f of t equals sine t, with the area from 0 to x shaded in green at x = 2.2. The bottom graph is the accumulated area F of x equals 1 minus cosine x, rising from 0 to a peak of 2 at pi, where f crosses zero, then falling back to 0 at 2 pi. The point at x = 2.2 on the bottom graph has height 1.59, equal to the shaded area above.](../../assets/figures/05-university-core/fundamental-theorem-of-calculus-accumulation.svg)

Part 2 is the shortcut for computing a definite integral: subtract the values of any antiderivative at the two ends. Part 1 is the reason that antiderivatives exist, and part 2 is how you use them.

A discrete version is familiar to programmers. If $P_n = a_1 + \cdots + a_n$ is a running total (a prefix sum), then $a_n = P_n - P_{n-1}$, and the sum of the terms from $m + 1$ to $n$ is $P_n - P_m$. Prefix sums play the part of $F$, differences play the part of the derivative, and the sum of a range is a subtraction at the two ends. The telescoping sums in [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md) are the same fact.

## Definitions

Let $f$ be continuous on an interval and let $a$ be a number in the interval. The **accumulation function** of $f$ starting at $a$ is

$$
F(x) = \int_a^x f(t)\,dt.
$$

In plain words, $F(x)$ is the signed area under $f$ from the fixed starting point $a$ to the moving point $x$. The letter $t$ is the dummy variable, so that $x$ can be the upper limit. Changing the starting point $a$ changes $F$ by a constant, since $\int_{a'}^x f = \int_{a'}^a f + \int_a^x f$.

An **antiderivative** of $f$ on an interval is a function $F$ with $F'(x) = f(x)$ for every $x$ in the interval. In plain words, it is a function whose slope is $f$. For $f(x) = 2x$, the functions $x^2$, $x^2 + 5$ and $x^2 - 100$ are all antiderivatives. The **indefinite integral** of $f$ is the whole family of antiderivatives,

$$
\int f(x)\,dx = F(x) + C,
$$

where $F$ is one antiderivative and $C$ is an arbitrary constant, the **constant of integration**. The indefinite integral is a family of functions, and the definite integral $\int_a^b f(x)\,dx$ is a number. The shared symbol is deliberate and is explained by the theorem below.

The **evaluation bracket** is the notation $\bigl[F(x)\bigr]_a^b = F(b) - F(a)$. In plain words, put in the upper limit, put in the lower limit, and subtract.

The **net change** of a quantity $Q(x)$ over $[a, b]$ is $Q(b) - Q(a)$. The word "net" signals that increases and decreases are added with their signs.

## How to do it

### The two parts of the theorem

*Theorem 1 (fundamental theorem of calculus, part 1).* Let $f$ be continuous on $[a, b]$, and let $F(x) = \int_a^x f(t)\,dt$. Then $F$ is continuous on $[a, b]$, differentiable on $(a, b)$, and

$$
F'(x) = f(x) \quad \text{for every } x \text{ in } (a, b).
$$

In plain words, the derivative of the accumulated area is the height of the curve at the moving edge.

The picture first. Move the right edge from $x$ to $x + h$. The area gains a thin strip, shown in orange in the figure. If the strip is narrow, $f$ barely changes across it, so the strip is nearly a rectangle with height $f(x)$ and width $h$. Its area $F(x + h) - F(x)$ is about $f(x)\,h$, and so $\frac{F(x + h) - F(x)}{h}$ is about $f(x)$. The proof makes "about" precise by trapping the strip between a tallest and a shortest rectangle.

![The graph of a curve y = f of t. The area under it up to x is shaded green and labelled F of x. A narrow orange strip between x and x plus h is the new area F of x plus h minus F of x. Two dashed lines across the strip mark the lowest height f of c one and the highest height f of c two of the curve over the strip.](../../assets/figures/05-university-core/fundamental-theorem-of-calculus-strip.svg)

We know the integral's properties (additivity, comparison and the constant rule from the last lesson) and the extreme value theorem: a continuous function on a closed interval has a smallest and a largest value. We want the limit of the difference quotient of $F$ at $x$. The plan is to write the numerator as one integral over the strip, bound it between the smallest and largest rectangle on the strip, and let continuity squeeze both bounds to $f(x)$.

*Proof.* Fix $x$ in $(a, b)$. Take $h > 0$ small enough that $x + h \le b$. By additivity, $F(x + h) - F(x) = \int_x^{x+h} f(t)\,dt$. By the extreme value theorem, $f$ has a smallest value $f(c_1)$ and a largest value $f(c_2)$ on $[x, x + h]$, with $c_1$ and $c_2$ in that interval. Then $f(c_1) \le f(t) \le f(c_2)$ for every $t$ in the strip, and the comparison and constant rules give

$$
f(c_1)\,h \le \int_x^{x+h} f(t)\,dt \le f(c_2)\,h.
$$

Divide by $h > 0$:

$$
f(c_1) \le \frac{F(x + h) - F(x)}{h} \le f(c_2).
$$

As $h \to 0^+$, both $c_1$ and $c_2$ are trapped in $[x, x + h]$ and so tend to $x$. Since $f$ is continuous at $x$, $f(c_1) \to f(x)$ and $f(c_2) \to f(x)$. By the squeeze theorem, the right-hand limit of the difference quotient is $f(x)$. For $h < 0$ the same argument works on the interval $[x + h, x]$, because $\frac{F(x + h) - F(x)}{h} = \frac{1}{-h}\int_{x+h}^{x} f(t)\,dt$ is again a quotient of an integral over the strip by the width of the strip. So the two one-sided limits agree and $F'(x) = f(x)$. Differentiability gives continuity of $F$ on $(a, b)$, and the same bounds with $h \to 0$ show that $F$ is continuous at $a$ and $b$ as well. $\blacksquare$

Look back: the difference quotient is the average height of $f$ over the strip, and continuity says the average height approaches the height at one point. Continuity is needed. If $f$ jumps at $x$, the average over a strip containing the jump doesn't approach $f(x)$ from both sides, and $F$ has a corner there (Practice problem 7).

*Theorem 2 (fundamental theorem of calculus, part 2).* Let $f$ be continuous on $[a, b]$ and let $F$ be any antiderivative of $f$ on $[a, b]$. Then

$$
\int_a^b f(x)\,dx = F(b) - F(a).
$$

In plain words, to integrate a continuous function, find any antiderivative and subtract its values at the two ends. It doesn't matter which antiderivative you pick, because a different choice adds the same constant to $F(b)$ and $F(a)$, and it cancels in the difference.

We know that $F' = f$ on the interval, that $f$ is continuous and so integrable (Theorem 1 of the last lesson), and the mean value theorem: if $F$ is continuous on $[x_{k-1}, x_k]$ and differentiable inside, then $\frac{F(x_k) - F(x_{k-1})}{x_k - x_{k-1}} = F'(c)$ for some $c$ strictly between. We want $F(b) - F(a)$ in terms of the integral. The plan is to cut $[a, b]$ into $n$ pieces, write $F(b) - F(a)$ as a telescoping sum of the changes over the pieces, use the mean value theorem to turn each change into a rectangle area, and recognise a Riemann sum.

*Proof.* Cut $[a, b]$ into $n$ equal pieces with endpoints $x_0 = a, x_1, \dots, x_n = b$ and width $\Delta x = \frac{b - a}{n}$. The sum of the changes of $F$ over the pieces telescopes:

$$
F(b) - F(a) = \sum_{k=1}^{n}\bigl(F(x_k) - F(x_{k-1})\bigr).
$$

On each piece, the mean value theorem gives a number $c_k$ between $x_{k-1}$ and $x_k$ with $F(x_k) - F(x_{k-1}) = F'(c_k)\,\Delta x = f(c_k)\,\Delta x$. So

$$
F(b) - F(a) = \sum_{k=1}^{n} f(c_k)\,\Delta x.
$$

The right side is a Riemann sum for $f$ on $[a, b]$ with sample points $c_k$. The left side doesn't depend on $n$. Let $n \to \infty$: the right side tends to $\int_a^b f(x)\,dx$, because $f$ is integrable and the limit is the same for every choice of sample points. A quantity that equals the same number for every $n$ is equal to its limit, so $F(b) - F(a) = \int_a^b f(x)\,dx$. $\blacksquare$

Look back: the mean value theorem picks, on each piece, the one sample point where the rectangle has exactly the right area, so every Riemann sum in this list is exact. We never found the points $c_k$, and we didn't have to, since the theorem only needs that they exist. There is a second proof from part 1. The function $G(x) = \int_a^x f(t)\,dt$ is an antiderivative of $f$ by part 1, and two antiderivatives of $f$ on an interval differ by a constant (below), so $F(x) = G(x) + C$, and $F(b) - F(a) = G(b) - G(a) = \int_a^b f - 0$.

The second proof uses a fact that explains the $+C$.

*Theorem 3.* If $F$ and $G$ are antiderivatives of $f$ on an interval, then $F(x) - G(x)$ is constant on that interval.

*Proof.* The function $F - G$ has derivative $f - f = 0$ everywhere on the interval. By the mean value theorem, for any two points $p < q$ in the interval, $(F - G)(q) - (F - G)(p) = (F - G)'(c)(q - p) = 0$, so $F - G$ takes the same value at every pair of points, which means it is constant. $\blacksquare$

So once you have found one antiderivative, you have found all of them: add a constant. The fine print is "on an interval". The function $\frac{1}{x}$ has antiderivative $\ln\lvert x \rvert + C_1$ on $x > 0$ and $\ln\lvert x \rvert + C_2$ on $x < 0$, and the two constants need not be equal, since the domain has a gap at 0.

### Finding antiderivatives

Reading the derivative table of the [derivatives chapter](../02-derivatives/index.md#derivative-table) backward gives the basic antiderivatives. To check any row, differentiate the right side.

| $f(x)$ | $\displaystyle\int f(x)\,dx$ | Valid for |
|---|---|---|
| $x^n$ | $\dfrac{x^{n+1}}{n+1} + C$ | $n \ne -1$, and $x > 0$ unless $n$ is a non-negative integer |
| $\dfrac{1}{x}$ | $\ln\lvert x \rvert + C$ | $x \ne 0$, on each side separately |
| $e^x$ | $e^x + C$ | all $x$ |
| $b^x$ | $\dfrac{b^x}{\ln b} + C$ | $b > 0$, $b \ne 1$ |
| $\sin x$ | $-\cos x + C$ | all $x$ |
| $\cos x$ | $\sin x + C$ | all $x$ |
| $\sec^2 x$ | $\tan x + C$ | $\cos x \ne 0$ |
| $\csc^2 x$ | $-\cot x + C$ | $\sin x \ne 0$ |
| $\sec x \tan x$ | $\sec x + C$ | $\cos x \ne 0$ |
| $\csc x \cot x$ | $-\csc x + C$ | $\sin x \ne 0$ |
| $\dfrac{1}{\sqrt{1 - x^2}}$ | $\arcsin x + C$ | $-1 < x < 1$ |
| $\dfrac{1}{1 + x^2}$ | $\arctan x + C$ | all $x$ |

Three rules extend the table. Antidifferentiation is linear: $\int \bigl(af(x) + bg(x)\bigr)dx = a\int f(x)\,dx + b\int g(x)\,dx$, because differentiation is. There is no product or quotient rule for integrals, and an expression like $\frac{x + 1}{x^2}$ should be rewritten as $\frac{1}{x} + \frac{1}{x^2}$ before integrating. And if $\int f(x)\,dx = F(x) + C$, then for constants $a \ne 0$ and $b$,

$$
\int f(ax + b)\,dx = \frac{1}{a}F(ax + b) + C,
$$

which you can check with the chain rule: the derivative of the right side is $\frac{1}{a}F'(ax + b) \cdot a = f(ax + b)$. So $\int e^{3x}\,dx = \frac{e^{3x}}{3} + C$ and $\int \cos(5x - 1)\,dx = \frac{\sin(5x - 1)}{5} + C$.

### Evaluating a definite integral

1. Check that $f$ is continuous on $[a, b]$, with no break, blow-up or hole between the limits.
2. Rewrite $f$ as a sum of terms in the table: expand products, split fractions, use powers for roots.
3. Find an antiderivative $F$. Leave out $+C$, because it cancels.
4. Compute $F(b) - F(a)$. Put the upper limit first, and keep brackets around negative values.
5. Check the sign and size against a picture or a rough estimate, or against a trapezoid sum.

### Rates and totals

*Theorem 4 (net change).* If $Q$ has a continuous derivative on $[a, b]$, then $\displaystyle\int_a^b Q'(x)\,dx = Q(b) - Q(a)$.

This is part 2 with $F = Q$, and it is the most used form of the theorem. The integral of a rate of change is the net change of the quantity. Two cases from earlier lessons:

- If $v(t) = s'(t)$ is velocity, then $\int_a^b v(t)\,dt = s(b) - s(a)$ is the displacement. The distance travelled is $\int_a^b \lvert v(t) \rvert\,dt$.
- If $C(q)$ is the cost of producing $q$ units, its derivative $C'(q)$ is the marginal cost, and $\int_{q_1}^{q_2} C'(q)\,dq = C(q_2) - C(q_1)$ is the extra cost of raising output from $q_1$ to $q_2$. Fixed costs are in $C(q_1)$ and in $C(q_2)$ alike, so they cancel, and marginal cost alone gives the extra cost. The same holds for revenue: since $R(0) = 0$, the revenue from selling $q$ units is $R(q) = \int_0^q R'(s)\,ds$, the integral of marginal revenue. For the marginal cost and revenue side of this, see [rates of change and marginal analysis](../03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md).

The units follow the same rule as before: dollars per unit times units is dollars.

### Differentiating an integral with a variable limit

If the upper limit is a function $g(x)$ and not just $x$, part 1 and the chain rule combine. Write $F(u) = \int_a^u f(t)\,dt$, so that the accumulation up to $g(x)$ is $F(g(x))$. Then

$$
\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = F'(g(x))\,g'(x) = f(g(x))\,g'(x).
$$

If the variable is the lower limit, swap the limits and change the sign: $\frac{d}{dx}\int_x^b f(t)\,dt = -f(x)$. The lower limit $a$ in the first formula doesn't appear in the answer. It changes $F$ only by a constant.

## Worked examples

<div class="example" markdown>

### Example 1: a definite integral by subtraction

Evaluate $\int_1^4 \left(3x^2 - 2x + 1\right)dx$.

Step 1: the integrand is a polynomial, so it is continuous everywhere. Step 2: it is already a sum of powers of $x$ (the last term is $1 = x^0$). Step 3: by the power rule and linearity, an antiderivative is $F(x) = x^3 - x^2 + x$. Check it: $F'(x) = 3x^2 - 2x + 1$. Step 4:

$$
F(4) - F(1) = (64 - 16 + 4) - (1 - 1 + 1) = 52 - 1 = 51.
$$

Step 5, the check: the integrand is 2 at $x = 1$ and 41 at $x = 4$, and it rises over a width of 3, so an answer in the tens is plausible. A trapezoid sum with $n = 1000$ gives $51.00001$.

In bracket form the whole computation is $\bigl[x^3 - x^2 + x\bigr]_1^4 = 52 - 1 = 51$. Watch out: a mistake that costs marks is subtracting in the wrong order, $F(1) - F(4) = -51$. The upper limit comes first.

</div>

<div class="example" markdown>

### Example 2: differentiating with a variable limit

Find $\dfrac{d}{dx}\displaystyle\int_0^{x^2}\cos\left(t^2\right)dt$.

The integrand $\cos\left(t^2\right)$ has no elementary antiderivative, and we don't need one. The upper limit is $g(x) = x^2$, with $g'(x) = 2x$. By the formula above,

$$
\frac{d}{dx}\int_0^{x^2}\cos\left(t^2\right)dt = \cos\left(\left(x^2\right)^2\right)\cdot 2x = 2x\cos\left(x^4\right).
$$

Check numerically at $x = 0.9$: the formula gives $1.8\cos(0.6561) = 1.8 \cdot 0.7924 = 1.4263$. A central difference with step $10^{-5}$ of the integral, evaluated by a midpoint sum with 20,000 rectangles, gives $1.42628$.

</div>

<div class="example" markdown>

### Example 3: cost from marginal cost

A bakery's marginal cost at output $q$ loaves a day is $20 - 0.02q$ dollars per loaf (hypothetical numbers), and its fixed cost is \$500 a day. How much more does it cost to raise output from 100 to 300 loaves, and what is the total cost at 300 loaves?

The extra cost is the integral of marginal cost:

$$
\int_{100}^{300}(20 - 0.02q)\,dq = \bigl[20q - 0.01q^2\bigr]_{100}^{300} = (6000 - 900) - (2000 - 100) = 5100 - 1900 = 3200.
$$

So the cost rises by \$3,200. The total cost function is $C(q) = 500 + 20q - 0.01q^2$, since its derivative is the marginal cost and $C(0) = 500$. At 300 loaves $C(300) = 500 + 6000 - 900 = 5600$, and $C(100) = 2400$.

Check: $5600 - 2400 = 3200$, so the fixed cost cancels. Also, marginal cost falls from \$18 at $q = 100$ to \$14 at $q = 300$, so the average over those 200 loaves is \$16 (the function is linear), and $16 \cdot 200 = 3200$.

</div>

<div class="example" markdown>

### Example 4: when the theorem does not apply

A student computes $\int_{-1}^{1}\frac{1}{x^2}\,dx$ with the antiderivative $-\frac{1}{x}$ and gets $\left[-\frac{1}{x}\right]_{-1}^{1} = -1 - 1 = -2$. Why is this wrong?

The integrand $\frac{1}{x^2}$ is positive everywhere, so a result of $-2$ can't be an area. The mistake is in Step 1 of the method. The function $\frac{1}{x^2}$ is not continuous on $[-1, 1]$. It is undefined at 0 and grows without bound near it, so it isn't integrable in the sense of the last lesson, and Theorem 2 needs a continuous integrand. The antiderivative $-\frac{1}{x}$ also isn't continuous on the interval. The correct statement is that the area under $\frac{1}{x^2}$ near 0 is infinite: the integral from $\varepsilon$ to 1 is $\frac{1}{\varepsilon} - 1$, which grows without bound as $\varepsilon \to 0^+$. This is an improper integral, treated in [partial fractions and improper integrals](05-partial-fractions-and-improper-integrals.md).

The same trap appears with $\int_0^{\pi}\sec^2 x\,dx$. The antiderivative $\tan x$ gives $\tan\pi - \tan 0 = 0$ for a positive integrand, but $\sec^2 x$ blows up at $x = \frac{\pi}{2}$.

Check: the fix is to look for breaks before subtracting. On $[1, 2]$, where $\frac{1}{x^2}$ is continuous, the method works: $\left[-\frac{1}{x}\right]_1^2 = -\frac{1}{2} + 1 = \frac{1}{2}$, and a trapezoid sum gives $0.5000$.

</div>

<div class="example" markdown>

### Example 5: displacement and distance (finish it yourself)

A particle on a line has velocity $v(t) = t^2 - 4t + 3$ metres per second for $0 \le t \le 4$. Find its displacement and the total distance it travels. The velocity factors as $v(t) = (t - 1)(t - 3)$, so it changes sign at $t = 1$ and $t = 3$, and an antiderivative is $s(t) = \frac{t^3}{3} - 2t^2 + 3t$. Compute the displacement from $s(4) - s(0)$, then the three signed integrals over $[0, 1]$, $[1, 3]$ and $[3, 4]$, and use them for the distance.

<details class="solution" markdown>
<summary>Finish</summary>

The displacement is $s(4) - s(0) = \frac{64}{3} - 32 + 12 - 0 = \frac{4}{3}$ m. For the pieces: $s(1) = \frac{1}{3} - 2 + 3 = \frac{4}{3}$, $s(3) = 9 - 18 + 9 = 0$, and $s(4) = \frac{4}{3}$. So the integrals are $s(1) - s(0) = \frac{4}{3}$, then $s(3) - s(1) = -\frac{4}{3}$, then $s(4) - s(3) = \frac{4}{3}$. The particle moves forward $\frac{4}{3}$ m, back $\frac{4}{3}$ m, and forward $\frac{4}{3}$ m. The distance is the sum of the absolute values, $3 \cdot \frac{4}{3} = 4$ m.

Check: the signed pieces add up, $\frac{4}{3} - \frac{4}{3} + \frac{4}{3} = \frac{4}{3}$, the displacement. A midpoint sum of $\lvert v \rvert$ with 10,000 rectangles gives $4.0000$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the theorem needs a continuous integrand on the whole interval. Example 4 is the standard failure, and it gives a negative "area" for a positive function. Before subtracting, scan the interval for a division by zero, a logarithm of 0, or a tangent at $\frac{\pi}{2}$.

</div>

<div class="warning" markdown>

Watch out: don't write $+C$ in a definite integral, and don't forget it in an indefinite one. In $\int_1^4 f = F(4) - F(1)$ the constant cancels. In $\int f(x)\,dx$ the answer is a family, and "$x^2$" alone is not the full answer: it is one member. The constant matters when you need a particular function, as when a total cost has to equal the fixed cost at $q = 0$.

</div>

<div class="warning" markdown>

Watch out: the power rule for antiderivatives fails at $n = -1$. The formula $\frac{x^{n+1}}{n+1}$ divides by 0, and the integral of $\frac{1}{x}$ is $\ln\lvert x \rvert + C$, not "$\frac{x^0}{0}$". For the other powers, raise the power by 1 and then divide by the new power: $\int x^3\,dx = \frac{x^4}{4} + C$, not $4x^4$.

</div>

<div class="warning" markdown>

Watch out: $\frac{d}{dx}\int_a^{g(x)} f(t)\,dt$ is $f(g(x))\,g'(x)$, and the factor $g'(x)$ is the one students drop. In Example 2 the answer is $2x\cos\left(x^4\right)$, and without $2x$ the answer would be wrong whenever $g$ isn't the identity. The check is to try $f = 1$: $\frac{d}{dx}\int_0^{x^2}1\,dt = \frac{d}{dx}x^2 = 2x$.

</div>

The accumulation function is defined with a fixed starting point. If the lower limit also depends on $x$, split the integral at a constant: $\int_{h(x)}^{g(x)} f = \int_{c}^{g(x)} f - \int_{c}^{h(x)} f$, and apply the rule to each part.

An antiderivative can be a function you can't write with the usual functions. The continuous function $e^{-x^2}$ has an accumulation function $\int_0^x e^{-t^2}\,dt$ by part 1, and it has no formula in terms of polynomials, exponentials, logarithms and trig functions. This isn't a failure of the method, since part 1 guarantees that $F$ exists. It is where functions like the error function come from.

## Tricks and shortcuts

Check an antiderivative by differentiating it. It takes ten seconds and catches nearly every error. For $\int x\cos x\,dx$, the guess $x\sin x$ has derivative $\sin x + x\cos x$, which is not $x\cos x$, so the guess is wrong (the right answer is in the lesson on [integration by parts](04-integration-by-parts-and-trig-integrals.md)).

Use the linear-inside rule instead of a substitution when the inside is $ax + b$: $\int \sqrt{2x + 7}\,dx = \frac{1}{2}\cdot\frac{2}{3}(2x + 7)^{3/2} = \frac{1}{3}(2x + 7)^{3/2} + C$. For anything with a nonlinear inside, wait for the [next lesson](03-u-substitution.md).

Rewrite before integrating. Roots and reciprocals become powers, $\frac{x^2 + 1}{x}$ becomes $x + \frac{1}{x}$, and a product like $(x + 1)^2$ is expanded. A shortcut for a quick sign and size check on a definite integral is the bounding rule: the integral lies between (smallest value of $f$)$\,\times\,(b - a)$ and (largest value of $f$)$\,\times\,(b - a)$. For Example 1 on $[1, 4]$, the bounds are $2 \cdot 3 = 6$ and $41 \cdot 3 = 123$, and 51 fits.

## In code

The first lines check part 2: a formula for an antiderivative and a trapezoid sum give the same number. Then the accumulation function of $\sin$ is built numerically, and its slope is compared with the integrand, which is part 1. The last lines are the discrete version, a prefix sum.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def trapezoid(f, a, b, n=1000):
    dx = (b - a) / n
    return dx * (f(a) / 2 + sum(f(a + k * dx) for k in range(1, n)) + f(b) / 2)

# Part 2: a number from a formula agrees with a number from a sum.
f = lambda x: 3 * x**2 - 2 * x + 1
F = lambda x: x**3 - x**2 + x        # an antiderivative of f
print(F(4) - F(1), round(trapezoid(f, 1, 4), 4))
# 51 51.0

# Part 1: the accumulation function of sin, computed as a sum,
# is 1 - cos x, and its slope at x is sin x.
def accumulate(f, a, x, n=2000):
    return trapezoid(f, a, x, n)

x, h = 2.2, 1e-4
print(round(accumulate(math.sin, 0, x), 6), round(1 - math.cos(x), 6))
# 1.588501 1.588501
slope = (accumulate(math.sin, 0, x + h) - accumulate(math.sin, 0, x - h)) / (2 * h)
print(round(slope, 6), round(math.sin(x), 6))
# 0.808496 0.808496

# The discrete version: a prefix sum, and the sum of a range as a subtraction.
a = [2 * k + 1 for k in range(1, 11)]          # a_1, ..., a_10
prefix = [0]
for term in a:
    prefix.append(prefix[-1] + term)           # prefix[n] = a_1 + ... + a_n
print(prefix[10] - prefix[3], sum(a[3:10]))
# 105 105
```

</details>

## FAQ

### Why does the constant $C$ vanish in a definite integral?

Because a definite integral uses the difference $F(b) - F(a)$, and a different antiderivative $F + C$ gives $(F(b) + C) - (F(a) + C)$, which is the same number. Theorem 3 says every antiderivative is $F + C$ for some $C$, so every choice gives the same answer. That is why you can drop $C$ in Step 3 of the method.

### Is the integral the opposite of the derivative?

Nearly. Part 1 says that integrating and then differentiating returns the original function: $\frac{d}{dx}\int_a^x f = f$. Part 2 says that differentiating and then integrating returns the original function up to a constant: $\int_a^x F' = F(x) - F(a)$. The two operations undo each other, with the starting value $F(a)$ as the only information the derivative forgets. That is the same as saying that a derivative doesn't know the constant.

### Does every continuous function have an antiderivative I can write down?

It has an antiderivative, by part 1, but you may not be able to write it with the familiar functions. The functions $e^{-x^2}$, $\frac{\sin x}{x}$ and $\sqrt{1 + x^3}$ are examples. Differentiation always stays inside the familiar functions, and integration doesn't. This is why the later lessons are a toolbox of techniques (substitution, parts, partial fractions) and why numerical integration matters.

### What goes wrong if $f$ has a jump?

Part 1 fails at the jump. If $f(t) = 1$ for $t < 1$ and $f(t) = 2$ for $t \ge 1$, then $F(x) = \int_0^x f$ equals $x$ for $x \le 1$ and $2x - 1$ for $x \ge 1$. The function $F$ is continuous, since the area changes smoothly, but its slope jumps from 1 to 2 at $x = 1$, so $F'(1)$ doesn't exist. A step in the rate makes a corner in the total.

## Practice

### Warm-up

1\. Evaluate (a) $\int_0^2\left(x^3 - 2x + 5\right)dx$, (b) $\int_0^{\pi}\sin x\,dx$ and (c) $\int_0^1 e^{2x}\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) An antiderivative is $\frac{x^4}{4} - x^2 + 5x$. At 2 it is $4 - 4 + 10 = 10$, and at 0 it is 0, so the integral is 10.

(b) $\bigl[-\cos x\bigr]_0^{\pi} = -\cos\pi + \cos 0 = 1 + 1 = 2$.

(c) By the linear-inside rule an antiderivative is $\frac{e^{2x}}{2}$, so the integral is $\frac{e^2 - 1}{2} \approx 3.1945$.

Check: (b) is the area of one arch of the sine curve, which is 2, a bit less than the $\pi \cdot 1 = 3.14$ of the rectangle around it. For (c), the integrand rises from 1 to $e^2 = 7.39$ over a width of 1, and 3.19 is a plausible average. A trapezoid sum with $n = 1000$ confirms (a) $10.0000$ and (c) $3.1945$.

</details>

2\. Find the derivative: (a) $F(x) = \int_1^x \sqrt{1 + t^4}\,dt$, (b) $G(x) = \int_x^3 te^t\,dt$, (c) $H(x) = \int_0^{x^3}\sin t\,dt$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) By part 1, $F'(x) = \sqrt{1 + x^4}$.

(b) The variable is the lower limit, so swap the limits and change the sign: $G(x) = -\int_3^x te^t\,dt$, and $G'(x) = -xe^x$.

(c) The upper limit is $x^3$, so by the chain-rule form, $H'(x) = \sin\left(x^3\right) \cdot 3x^2$.

Check (c): $H(x) = \bigl[-\cos t\bigr]_0^{x^3} = 1 - \cos\left(x^3\right)$, whose derivative is $\sin\left(x^3\right) \cdot 3x^2$.

</details>

3\. Find each indefinite integral and check by differentiating: (a) $\int\left(4x^3 - \frac{1}{x} + e^x\right)dx$ for $x > 0$, (b) $\int\left(\sec^2 x + 2\cos x\right)dx$, (c) $\int\frac{3}{1 + x^2}\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $x^4 - \ln x + e^x + C$. (b) $\tan x + 2\sin x + C$. (c) $3\arctan x + C$.

Check: the derivative of (a) is $4x^3 - \frac{1}{x} + e^x$. The derivative of (b) is $\sec^2 x + 2\cos x$. The derivative of (c) is $\frac{3}{1 + x^2}$.

</details>

### Standard

4\. Evaluate (a) $\int_1^5 \frac{1}{x}\,dx$, (b) $\int_0^1 \frac{1}{1 + x^2}\,dx$ and (c) $\int_1^4\left(\sqrt{x} + \frac{1}{\sqrt{x}}\right)dx$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\bigl[\ln x\bigr]_1^5 = \ln 5 - 0 \approx 1.6094$.

(b) $\bigl[\arctan x\bigr]_0^1 = \frac{\pi}{4} - 0 = \frac{\pi}{4} \approx 0.7854$.

(c) Write the integrand as $x^{1/2} + x^{-1/2}$, with antiderivative $\frac{2}{3}x^{3/2} + 2x^{1/2}$. At 4 it is $\frac{16}{3} + 4 = \frac{28}{3}$, and at 1 it is $\frac{2}{3} + 2 = \frac{8}{3}$, so the integral is $\frac{20}{3}$.

Check: (b) is the area under a curve that falls from 1 to $\frac{1}{2}$ over a width of 1, so it should be between 0.5 and 1, and $0.785$ is. (c): the integrand ranges from 2 at $x = 1$ to $2.5$ at $x = 4$ and dips to 2 in between, over a width of 3, so $\frac{20}{3} = 6.67$ is between 6 and 7.5.

</details>

5\. A firm's marginal revenue is $R'(q) = 80 - 0.4q$ dollars per unit (hypothetical numbers) and $R(0) = 0$. (a) Find the revenue from the first 50 units. (b) Find $R(q)$ in general and the output at which revenue is largest. (c) What price does the firm charge per unit at that output?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\int_0^{50}(80 - 0.4q)\,dq = \bigl[80q - 0.2q^2\bigr]_0^{50} = 4000 - 500 = 3500$ dollars.

(b) $R(q) = \int_0^q(80 - 0.4s)\,ds = 80q - 0.2q^2$, using $s$ as the dummy variable. Revenue is largest where the marginal revenue is 0, which is $80 - 0.4q = 0$, so $q = 200$, and $R(200) = 16000 - 8000 = 8000$ dollars.

(c) Revenue is price times quantity, so $p = \frac{R(q)}{q} = 80 - 0.2q$, which at $q = 200$ is \$40.

Check: $200 \cdot 40 = 8000$. Also $R(50) = 4000 - 500 = 3500$, which agrees with (a), and $R'(q)$ is positive for $q < 200$ and negative after, so 200 is a maximum.

</details>

6\. (Reviews [the chain rule](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md).) Let $F(x) = \int_0^{\sin x}\frac{dt}{\sqrt{1 - t^2}}$ for $-\frac{\pi}{2} < x < \frac{\pi}{2}$. Find $F'(x)$ using the chain-rule form of part 1, and then find a formula for $F(x)$ by integrating.

<details class="solution" markdown>
<summary>Solution</summary>

With $g(x) = \sin x$, $F'(x) = \frac{1}{\sqrt{1 - \sin^2 x}}\cdot\cos x = \frac{\cos x}{\sqrt{\cos^2 x}} = \frac{\cos x}{\cos x} = 1$, because $\cos x > 0$ on this interval.

By integrating, $F(x) = \bigl[\arcsin t\bigr]_0^{\sin x} = \arcsin(\sin x) - 0 = x$ on this interval.

Check: the derivative of $x$ is 1, so the two answers agree. Note the role of the interval: on $\left(\frac{\pi}{2}, \frac{3\pi}{2}\right)$, $\cos x < 0$, the quotient is $-1$, and $\arcsin(\sin x) = \pi - x$, with derivative $-1$.

</details>

### Challenge

7\. Let $f(t) = 1$ for $t < 1$ and $f(t) = 2$ for $t \ge 1$. Find $F(x) = \int_0^x f(t)\,dt$ for $0 \le x \le 3$ and show that $F$ is continuous but not differentiable at $x = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

For $0 \le x \le 1$, the region is a rectangle of height 1, so $F(x) = x$. For $x \ge 1$, add the area from 1 to $x$, a rectangle of height 2: $F(x) = 1 + 2(x - 1) = 2x - 1$.

Both formulas give $F(1) = 1$, so $F$ is continuous at 1. The slope from the left is 1 and the slope from the right is 2. The one-sided derivatives differ, so $F'(1)$ doesn't exist, a corner like $\lvert x \rvert$ at 0.

Check: away from 1, $F' = f$ as part 1 says, since $F' = 1$ on $(0, 1)$ and $F' = 2$ on $(1, 3)$. The theorem fails only at the jump of $f$, as it must, because $f$ is not continuous there.

</details>

8\. A program keeps prefix sums $P_n = a_1 + a_2 + \cdots + a_n$ of the sequence $a_k = 2k + 1$. (a) Find a formula for $P_n$. (b) Use it to find $a_4 + a_5 + \cdots + a_{10}$ as a subtraction, as the fundamental theorem does. (c) Which statement here matches part 1, and which matches part 2?

<details class="solution" markdown>
<summary>Solution</summary>

(a) By the rules for sums, $P_n = 2\cdot\frac{n(n+1)}{2} + n = n^2 + 2n$.

(b) The terms from $a_4$ to $a_{10}$ are $P_{10} - P_3 = (100 + 20) - (9 + 6) = 120 - 15 = 105$.

(c) The statement $a_n = P_n - P_{n-1}$ is the discrete part 1: the change in the running total is the new term, like $F' = f$. Check: $P_n - P_{n-1} = n^2 + 2n - (n-1)^2 - 2(n-1) = 2n + 1$. The range sum $\sum_{k=m+1}^{n} a_k = P_n - P_m$ is the discrete part 2: a sum over a range is a difference of the running total at the ends.

Check (b) directly: $9 + 11 + 13 + 15 + 17 + 19 + 21 = 105$, seven terms with ends 9 and 21 and average 15.

</details>

## Where this shows up

- The rest of this chapter is a toolbox for finding antiderivatives: [u-substitution](03-u-substitution.md) runs the chain rule backward, and [integration by parts](04-integration-by-parts-and-trig-integrals.md) runs the product rule backward. [Applications of integrals](06-applications-of-integrals.md) uses the net change theorem for areas, averages and totals.
- In CS, prefix sums answer range-sum queries in constant time by the same subtraction, and a cumulative distribution function is an accumulation function of a probability density ([continuous random variables and the normal distribution](../07-probability/04-continuous-random-variables-and-the-normal.md)). Numerical integrators and ODE solvers rely on $F(b) - F(a)$ being a sum of small changes.
- In economics, total cost, total revenue and consumer surplus are integrals of marginal quantities ([surplus and market interventions](../../07-economics-math/02-markets/04-surplus-and-market-interventions.md)), and in physics the displacement is the integral of the velocity, as here.
