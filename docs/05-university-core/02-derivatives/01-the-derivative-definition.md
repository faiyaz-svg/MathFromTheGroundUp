# The derivative definition

After this lesson you can compute a derivative from the limit definition, write the equation of a tangent line, read $f'(a)$ as an instantaneous rate of change with units, say where and why a derivative fails to exist, and estimate a derivative numerically in code.

Before this: [reading function graphs](../../03-high-school/03-functions/02-reading-function-graphs.md) (average rate of change and secant lines), [slope and linear equations](../../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md), and [limits, intuition and limit laws](../01-limits-and-continuity/01-limits-intuition-and-limit-laws.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For $f(x) = x^2 - 3x$, simplify $\frac{f(2 + h) - f(2)}{h}$ and take the limit as $h \to 0$.
2. Is $g(x) = \lvert x - 2 \rvert$ differentiable at $x = 2$? Give the reason in terms of slopes.
3. A ball's height in metres after $t$ seconds is $s(t) = 20t - 5t^2$. Use the definition to find its velocity at $t = 1$, with units.

<details class="solution" markdown>
<summary>Answers</summary>

1. Expand: $f(2 + h) = 4 + 4h + h^2 - 6 - 3h = -2 + h + h^2$ and $f(2) = -2$. So the quotient is $\frac{h + h^2}{h} = 1 + h$, which tends to 1. So $f'(2) = 1$.
2. No. To the right of 2 the graph is the line $y = x - 2$, with slope $1$, and to the left it is $y = 2 - x$, with slope $-1$. The two one-sided slopes differ, so the limit of the difference quotient doesn't exist.
3. The quotient is $\frac{s(1 + h) - s(1)}{h} = \frac{20h - 5(2h + h^2)}{h} = 10 - 5h$, which tends to 10. The velocity at $t = 1$ is $10$ m/s (still going up).

</details>

## The idea

A car's trip computer says it covered 90 km in the last hour, so the average speed was 90 km/h. The speedometer says 112 km/h right now. These are different numbers, and the second one is harder to define, because "right now" is a single instant, and in a single instant the car covers no distance and no time passes. The way out is the one you already used for average rates: take a short stretch of time, compute distance over time, and make the stretch shorter and shorter.

Try it with the cost curve from [reading function graphs](../../03-high-school/03-functions/02-reading-function-graphs.md), $C(q) = 1000 + 10q + 0.05q^2$ dollars to make $q$ widgets. That lesson found an average of \$15 more per widget from 0 to 100 widgets, and \$25 from 100 to 200. What does one more widget cost when you are already making 100? Look at the average over $[100, 100 + h]$. Since $C(100) = 2500$ and $C(100 + h) = 2500 + 20h + 0.05h^2$, the average is

$$
\frac{C(100 + h) - C(100)}{h} = \frac{20h + 0.05h^2}{h} = 20 + 0.05h.
$$

| Interval | $h$ | Average cost per extra widget |
|---|---|---|
| $[100, 200]$ | $100$ | \$25.00 |
| $[100, 110]$ | $10$ | \$20.50 |
| $[100, 101]$ | $1$ | \$20.05 |
| $[100, 100.1]$ | $0.1$ | \$20.005 |

As the interval shrinks, the average settles on \$20. That number is the cost of the next widget at output 100, and it is what the rest of this lesson calls a derivative.

On the graph, each average is the slope of a secant line through the point $P$ at $q = 100$ and a second point on the curve. As the second point slides toward $P$, the secant swings round and settles into one limiting line, which just grazes the curve at $P$. That line is the tangent line, and its slope is the derivative. The figure shows it for $y = x^2$ at $P = (1, 1)$, where the secant slopes 4, 3 and 2.5 are heading for 2.

![The parabola y = x squared with the point (1, 1) marked. Three secant lines through (1, 1) are drawn: a red one through the point at h = 2 with slope 4, an orange one at h = 1 with slope 3, and a blue one at h = 0.5 with slope 2.5. A thicker green tangent line through (1, 1) has slope 2 and lies below all three secants to the right of the point.](../../assets/figures/05-university-core/the-derivative-definition-secants.svg)

There is a second way to say it. Zoom in on a smooth curve at one point, and it looks more and more like a straight line. The slope of that line is the derivative. At a corner, no amount of zooming gives a straight line, and the derivative doesn't exist there. Both pictures lead to the same definition.

## Definitions

Let $f$ be a function defined on an open interval around $a$. For $h \ne 0$, the **difference quotient** of $f$ at $a$ is

$$
\frac{f(a + h) - f(a)}{h},
$$

which is the slope of the secant line through $(a, f(a))$ and $(a + h, f(a + h))$. In plain words, it is the average rate of change of $f$ from $a$ to $a + h$. The number $h$ may be negative, in which case the second point is to the left of $a$ and the formula still gives a secant slope.

The **derivative** of $f$ at $a$ is the limit of the difference quotient as $h$ approaches 0:

$$
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h},
$$

when this limit exists, as a real number. In that case $f$ is **differentiable** at $a$. If the limit doesn't exist, or is $\infty$ or $-\infty$, then $f$ is not differentiable at $a$. In plain words, $f'(a)$ is the number the secant slopes settle on as the second point closes in on the first. The same limit can be written with $x$ in place of $a + h$:

$$
f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}.
$$

This form is handy when the algebra is easier with a factor like $x - a$, for example $x^3 - a^3$.

The **tangent line** to the graph of $f$ at the point $(a, f(a))$ is the line through that point with slope $f'(a)$, so its equation is

$$
y = f(a) + f'(a)\,(x - a).
$$

In plain words, the tangent line is the best straight-line copy of the curve near $a$. Notice that this is a definition and not "the line that touches the curve once": a line can touch a curve at one point and not be a tangent, and a tangent can cross the curve (see the FAQ).

The **derivative function** $f'$ assigns to each $x$ where $f$ is differentiable the number $f'(x)$:

$$
f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}.
$$

Its domain is the set of $x$ where the limit exists, which can be smaller than the domain of $f$. The word "derivative" covers both the number $f'(a)$ and the function $f'$; the context tells you which. A function is differentiable on an interval when it is differentiable at every point of it.

There are several notations, and a calculus text uses all of them.

| Notation | Read as | Notes |
|---|---|---|
| $f'(x)$ | "$f$ prime of $x$" | Lagrange's notation, short and common |
| $\dfrac{dy}{dx}$ | "$d y$ by $d x$" | Leibniz's notation, for $y = f(x)$; keeps the variable visible |
| $\dfrac{d}{dx} f(x)$ | "d by d x of $f$" | the derivative as an operation applied to an expression |
| $\left.\dfrac{dy}{dx}\right\rvert_{x=a}$ | "$dy\,dx$ at $x$ equals $a$" | the derivative evaluated at one point, same as $f'(a)$ |

The symbol $\frac{dy}{dx}$ comes from writing the difference quotient as $\frac{\Delta y}{\Delta x}$, with $\Delta$ meaning "change in", and then letting the changes shrink. For now treat $\frac{dy}{dx}$ as one symbol and not as a fraction; the [chain rule](03-chain-rule-implicit-and-inverse-derivatives.md) is where it starts to behave like one.

Finally, the **instantaneous rate of change** of $f$ at $a$ is $f'(a)$. Its units are the units of $f(x)$ per unit of $x$. If $s(t)$ is a position in metres and $t$ is in seconds, then $s'(t)$ is a velocity in metres per second. If $C(q)$ is a cost in dollars and $q$ counts widgets, then $C'(q)$ is in dollars per widget and is called the **marginal cost**: the cost of producing one more unit at output $q$, to a good approximation. A positive derivative means the quantity is increasing at that point, and a negative derivative means it is decreasing.

For a line $f(x) = mx + b$ the difference quotient is $\frac{m(x + h) + b - mx - b}{h} = m$, so $f'(x) = m$ for every $x$. The derivative is a generalization of the slope of a line, and the tangent to a line is the line itself.

## How to do it

### Computing a derivative from the definition

1. Write the difference quotient $\frac{f(x + h) - f(x)}{h}$, replacing $x$ by $x + h$ in every place it appears and putting the new input in brackets.
2. Simplify until the $h$ in the denominator cancels. The usual moves are to expand a power, to combine fractions over a common denominator, or to multiply top and bottom by a conjugate when there is a square root.
3. Take the limit as $h \to 0$. After the cancellation, the expression is continuous at $h = 0$, so this means putting $h = 0$ in what is left.
4. State the answer as a function of $x$, and say where it holds (for example, $x > 0$).
5. Check by computing the difference quotient for a small $h$, such as $0.001$, at one value of $x$.

Watch out for Step 3. If you put $h = 0$ before the cancellation, you get $\frac{0}{0}$, which has no value. Cancelling the $h$ first is the whole point of the algebra in Step 2.

### Writing a tangent line

1. Find the point: compute $f(a)$.
2. Find the slope: compute $f'(a)$, with the steps above.
3. Substitute into $y = f(a) + f'(a)(x - a)$ and simplify if needed.
4. Check that the line passes through $(a, f(a))$, and that its slope has the sign the graph suggests.

### Where a derivative does not exist

The derivative at $a$ asks for one number, and four things can prevent it. The figure shows each at $x = 0$.

![Four small graphs, each with a red dot at the origin. A V-shaped graph of absolute value of x, labelled corner. The graph of x to the two-thirds, which has a sharp point pointing down at the origin, labelled cusp. The graph of the cube root of x, which is steep at the origin, with a dashed vertical red line through the origin, labelled vertical tangent. A step graph that is 0 for x less than 0 and 1 for x at least 0, labelled jump.](../../assets/figures/05-university-core/the-derivative-definition-failures.svg)

A **corner** is a point where the two one-sided slopes are different finite numbers, as for $\lvert x \rvert$ at 0. A two-sided limit exists exactly when both one-sided limits exist and are equal. So the derivative exists exactly when the slope from the right, $\lim_{h \to 0^+}$, equals the slope from the left, $\lim_{h \to 0^-}$.

A **cusp** is a sharp point where the one-sided slopes go off to infinity with opposite signs. For $f(x) = x^{2/3}$ at 0 the difference quotient is $\frac{h^{2/3}}{h} = h^{-1/3}$, which tends to $+\infty$ from the right and $-\infty$ from the left.

A **vertical tangent** is a point where the curve is smooth but the tangent line is vertical, so its slope would be infinite. For $f(x) = x^{1/3}$ (the real cube root) the quotient is $\frac{h^{1/3}}{h} = h^{-2/3}$, which tends to $+\infty$ from both sides. The limit is $\infty$, which is not a real number, so $f'(0)$ doesn't exist even though the graph has a perfectly good tangent line, the $y$-axis.

A **discontinuity** is a jump, a hole or an asymptote at $a$. There a derivative can't exist, and the theorem below explains why.

A fifth way is wild oscillation. The function $x \sin\frac{1}{x}$, with value 0 at $x = 0$, is continuous there, but its difference quotient at 0 is $\sin\frac{1}{h}$, which swings between $-1$ and $1$ forever as $h \to 0$ and has no limit. In practice, corners, cusps, vertical tangents and jumps are the cases you will meet.

### Differentiable implies continuous

A function is continuous at $a$ when $\lim_{x \to a} f(x) = f(a)$, which can also be written $\lim_{h \to 0} f(a + h) = f(a)$ (see [continuity, asymptotes and the IVT](../01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md)).

*Theorem.* If $f$ is differentiable at $a$, then $f$ is continuous at $a$.

We know that the limit $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$ exists as a real number. We want to show that $f(a + h)$ tends to $f(a)$. The plan is to write the change $f(a + h) - f(a)$ as the difference quotient times $h$, and use the limit law for products.

*Proof.* For $h \ne 0$,

$$
f(a + h) - f(a) = \frac{f(a + h) - f(a)}{h} \cdot h.
$$

As $h \to 0$ the first factor tends to $f'(a)$ and the second factor tends to 0. The limit of a product is the product of the limits when both exist, so $\lim_{h \to 0} \bigl(f(a + h) - f(a)\bigr) = f'(a) \cdot 0 = 0$. Adding $f(a)$, we get $\lim_{h \to 0} f(a + h) = f(a)$, so $f$ is continuous at $a$. $\blacksquare$

Look back: the proof used nothing about $f$ except the existence of the derivative. The converse is false: $\lvert x \rvert$ is continuous at 0 and not differentiable there. The contrapositive is useful, though. If $f$ is not continuous at $a$, it is not differentiable at $a$, so a jump rules out a derivative without any computation. Continuity is the weaker condition. A continuous graph can be drawn without lifting the pen, and a differentiable graph must also be smooth.

## Worked examples

<div class="example" markdown>

### Example 1: the derivative of $x^2$

Find $f'(x)$ for $f(x) = x^2$, then the tangent line at $x = 3$.

Step 1: the difference quotient has $x + h$ in brackets:

$$
\frac{(x + h)^2 - x^2}{h}.
$$

Step 2: expand $(x + h)^2 = x^2 + 2xh + h^2$. The $x^2$ terms cancel, and every term left on top has a factor of $h$:

$$
\frac{x^2 + 2xh + h^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h.
$$

Watch out: $(x + h)^2$ is not $x^2 + h^2$. Leaving out the middle term $2xh$ gives a quotient of $\frac{h^2}{h} = h$ and a derivative of 0, which is wrong for a parabola that slopes up on one side of its vertex.

Step 3: now put $h = 0$:

$$
\lim_{h \to 0} (2x + h) = 2x.
$$

Step 4: so $f'(x) = 2x$ for every real $x$. The slope is negative to the left of the vertex, zero at $x = 0$ and positive to the right, which is how a parabola behaves.

For the tangent line at $x = 3$: $f(3) = 9$ and $f'(3) = 6$, so $y = 9 + 6(x - 3) = 6x - 9$.

Step 5, the check: at $x = 3$ with $h = 0.001$, the quotient is $\frac{3.001^2 - 9}{0.001} = 6.001$, close to 6. The tangent line passes through $(3, 9)$, since $6 \cdot 3 - 9 = 9$. The figure at the start shows the same limit at $x = 1$, where $f'(1) = 2$ and the secant slopes were $2 + h$ for $h = 2, 1, 0.5$.

</div>

<div class="example" markdown>

### Example 2: $\frac{1}{x}$ and $\sqrt{x}$

First $f(x) = \frac{1}{x}$, for $x \ne 0$. The quotient has a fraction on top, so combine it over a common denominator:

$$
\frac{\frac{1}{x + h} - \frac{1}{x}}{h} = \frac{1}{h} \cdot \frac{x - (x + h)}{x(x + h)} = \frac{1}{h} \cdot \frac{-h}{x(x + h)} = \frac{-1}{x(x + h)}.
$$

Putting $h = 0$ gives $f'(x) = -\frac{1}{x^2}$. This is negative everywhere, which matches the graph: both branches of $\frac{1}{x}$ go downhill as you move right. At $x = 2$ the slope is $-\frac{1}{4}$, and the tangent line through $\left(2, \frac{1}{2}\right)$ is $y = \frac{1}{2} - \frac{1}{4}(x - 2) = 1 - \frac{x}{4}$.

Now $f(x) = \sqrt{x}$, for $x > 0$. A square root on top is cleared by multiplying top and bottom by the conjugate, $\sqrt{x + h} + \sqrt{x}$, which turns the top into a difference of squares:

$$
\frac{\sqrt{x + h} - \sqrt{x}}{h} \cdot \frac{\sqrt{x + h} + \sqrt{x}}{\sqrt{x + h} + \sqrt{x}} = \frac{(x + h) - x}{h\left(\sqrt{x + h} + \sqrt{x}\right)} = \frac{1}{\sqrt{x + h} + \sqrt{x}}.
$$

Putting $h = 0$ gives $f'(x) = \frac{1}{2\sqrt{x}}$ for $x > 0$. The slope is large near 0 and gets smaller for large $x$, as the graph of $\sqrt{x}$ flattens out. At $x = 0$ the quotient is $\frac{1}{\sqrt{h}}$, which tends to $\infty$ from the right: a vertical tangent, and no derivative.

Check: for $\sqrt{x}$ at $x = 4$ the answer is $\frac{1}{2 \cdot 2} = 0.25$, and the quotients for $h = 1, 0.1, 0.01$ are $0.2361$, $0.2485$ and $0.2498$, closing in on $0.25$. For $\frac{1}{x}$ at $x = 2$ with $h = 0.01$: $\frac{1/2.01 - 1/2}{0.01} = -0.24876$, close to $-\frac{1}{4}$.

</div>

<div class="example" markdown>

### Example 3: a corner, done properly

Show that $f(x) = \lvert x \rvert$ is not differentiable at 0, and find $f'(x)$ everywhere else.

At $a = 0$ the quotient is $\frac{\lvert h \rvert - 0}{h} = \frac{\lvert h \rvert}{h}$. For $h > 0$ it equals $\frac{h}{h} = 1$, and for $h < 0$ it equals $\frac{-h}{h} = -1$. So the limit from the right is 1 and the limit from the left is $-1$. They differ, so the limit doesn't exist, and $f'(0)$ doesn't exist.

At $a = 2$, take $h$ so small that $2 + h > 0$ (any $\lvert h \rvert < 2$). Then $\lvert 2 + h \rvert = 2 + h$, and the quotient is $\frac{(2 + h) - 2}{h} = 1$ for all such $h$. So $f'(2) = 1$. The same argument at any $a > 0$ gives 1, and at any $a < 0$ the absolute value is $-x$ near $a$, giving $-1$:

$$
f'(x) = \begin{cases} 1 & x > 0, \\ -1 & x < 0. \end{cases}
$$

Check: the graph is the line $y = x$ for $x > 0$ and $y = -x$ for $x < 0$, with slopes 1 and $-1$. The derivative function $f'$ is a step with a jump at 0, and its domain leaves out $x = 0$, so it is smaller than the domain of $f$.

</div>

<div class="example" markdown>

### Example 4: marginal cost with units

For $C(q) = 1000 + 10q + 0.05q^2$ dollars, find $C'(q)$ from the definition and interpret $C'(100)$ and $C'(0)$.

Step 1: the quotient is $\frac{C(q + h) - C(q)}{h}$. Expand $C(q + h) = 1000 + 10q + 10h + 0.05\left(q^2 + 2qh + h^2\right)$.

Step 2: subtract $C(q)$. The constant, the $10q$ and the $0.05q^2$ cancel, leaving $10h + 0.1qh + 0.05h^2$, and dividing by $h$ gives $10 + 0.1q + 0.05h$.

Step 3: put $h = 0$: $C'(q) = 10 + 0.1q$ dollars per widget.

So $C'(100) = 20$: at an output of 100 widgets, one more widget costs about \$20, which agrees with the table in the idea section. And $C'(0) = 10$: in this model the first widget costs about \$10 in materials and labour, with the \$1,000 fixed cost not entering the marginal cost at all, because the derivative of a constant is 0. The marginal cost rises by \$0.10 for every widget made, which is why the graph curves upward.

Check: the exact extra cost of the 101st widget is $C(101) - C(100) = 2520.05 - 2500 = 20.05$, within a nickel of the \$20 derivative. The marginal cost is a good estimate of the next unit's cost, but not exactly equal to it, because the slope changes along the way.

</div>

<div class="example" markdown>

### Example 5: velocity of a ball (finish it yourself)

The height of a ball is $s(t) = 20t - 5t^2$ metres at time $t$ seconds. Find its velocity $s'(t)$ for every $t$.

Step 1: $s(t + h) = 20(t + h) - 5(t + h)^2$, where $h$ is now a small time step. Step 2: subtract $s(t)$ and expand. The terms $20t$ and $-5t^2$ cancel, leaving $20h - 10th - 5h^2$. Dividing by $h$ gives the quotient $20 - 10t - 5h$.

Now do Step 3, state $s'(t)$, find the velocity at $t = 0$, $t = 2$ and $t = 3$, say what the sign means at each, and check one value with a small $h$.

<details class="solution" markdown>
<summary>Finish</summary>

Step 3: as $h \to 0$ the quotient tends to $20 - 10t$, so $s'(t) = 20 - 10t$ metres per second.

At $t = 0$ the velocity is $20$ m/s, upward. At $t = 2$ it is $0$ m/s: the ball is at the top of its flight, momentarily at rest. At $t = 3$ it is $-10$ m/s, and the minus sign means the ball is moving downward.

Check: at $t = 1$, with $h = 0.001$, the quotient is $20 - 10 - 0.005 = 9.995$, close to $s'(1) = 10$, the answer from the quick check. The top of the flight at $t = 2$ matches the height formula too: $s(t) = 5t(4 - t)$ has its maximum halfway between its zeros 0 and 4.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: substituting $h = 0$ too early. In $\frac{(x + h)^2 - x^2}{h}$, putting $h = 0$ gives $\frac{0}{0}$. A limit is about what happens as $h$ gets close to 0, not at 0, so you must simplify first. If the $h$ in the denominator is still there after your algebra, you aren't done.

</div>

<div class="warning" markdown>

Watch out: a derivative at a point and a derivative of a constant are different things. For $f(x) = x^2$, the number $f(3) = 9$ is a constant, and its derivative is 0. But $f'(3) = 6$ means "find $f'(x) = 2x$, then put in $x = 3$". Differentiate first, then substitute. Substituting first and then differentiating gives 0, which is wrong.

</div>

<div class="warning" markdown>

Watch out: continuous does not mean differentiable. The graph of $\lvert x \rvert$ has no gaps, and it has no tangent line at 0. The implication goes the other way, as the theorem says: differentiable implies continuous.

</div>

<div class="warning" markdown>

Watch out for the units of a derivative. If $s$ is in metres and $t$ in seconds, then $s'$ is in metres per second, "per unit of the input". A derivative of 20 "dollars" is incomplete: say \$20 per widget. And the sign belongs to the answer: $-10$ m/s means moving the other way, which is different from 10 m/s.

</div>

When the limit is $\infty$ or $-\infty$, there is no derivative, even though the picture may show a clean vertical tangent. The definition asks for a real number. Calculus texts sometimes say "the derivative is infinite" informally, and what they mean is the vertical-tangent case.

A derivative can also exist at only one side of a domain. For $f(x) = \sqrt{x}$ on $[0, \infty)$ the function has no points left of 0, so the two-sided limit at $x = 0$ can't be formed. Texts handle the endpoint with a one-sided derivative, which here would be $\infty$. This book takes derivatives at interior points.

## Tricks and shortcuts

The algebra for Step 2 depends on the type of function, and recognizing the type saves time.

| Function contains | Move in Step 2 | Example |
|---|---|---|
| a power $x^n$ | expand $(x + h)^n$ with the binomial theorem; all terms except the first have a factor of $h$ | $(x + h)^2$ |
| a fraction with $x$ below | combine over the common denominator $x(x + h)$ | $\frac{1}{x}$ |
| a square root | multiply top and bottom by the conjugate | $\sqrt{x}$ |
| a difference like $x^3 - a^3$ | use the form with $x \to a$ and factor out $x - a$ | $x^3$ at $a$ |

For the last row: $\frac{x^3 - a^3}{x - a} = x^2 + xa + a^2$, which tends to $3a^2$ as $x \to a$. So the derivative of $x^3$ is $3x^2$, found without expanding $(x + h)^3$.

Two quick sanity checks apply to every answer. First, the sign of $f'$ must match the graph: positive where $f$ climbs, negative where it falls, zero at the top of a smooth hill. Second, a polynomial's derivative has a lower degree, and a derivative that is bigger than the function by a lot is usually a mistake.

The zoom-in test is a fast way to decide whether a derivative exists from a graph. Zoom in on the point in your mind. If the curve flattens into a line, there is a derivative. If it stays a V, a point or a step, there isn't one.

## In code

A computer can estimate a derivative with a small $h$, which is useful for checking a hand calculation. There are two standard quotients. The forward difference is $\frac{f(x + h) - f(x)}{h}$, the definition with $h$ held small. The central difference is $\frac{f(x + h) - f(x - h)}{2h}$, which looks at both sides of $x$. The central version is more accurate, because the errors from the two sides mostly cancel. (Practice problem 7 shows that for a differentiable function it still tends to $f'(x)$.) For smooth functions, the error of the forward difference is roughly proportional to $h$, and that of the central difference to $h^2$. The reason comes from Taylor series, in [Power series and Taylor series](../05-sequences-and-series/04-power-series-and-taylor-series.md).

It would be natural to make $h$ as small as possible, and that fails. A computer stores numbers with about 16 significant digits (see [floating point basics](../../06-cs-math/01-number-representation/04-floating-point-basics.md)). When $h$ is tiny, $f(x + h)$ and $f(x)$ agree in nearly all their digits, and their difference keeps only a few correct ones. Dividing by $h$ then magnifies that rounding error, so it grows like $\frac{10^{-16}}{h}$ as $h$ shrinks, while the error from the formula itself shrinks. The total error is a V: it falls as $h$ decreases and then climbs again. For the forward difference the best $h$ is about $10^{-8}$, and for the central difference about $10^{-5}$ or $10^{-6}$.

![A log-log graph of the error in estimating the derivative of e to the x at x = 1 against the step size h from 1e-16 to 1. The forward difference in orange falls with slope 1 down to about 7e-9 at h near 1e-8, then rises in a jagged line toward 1 as h shrinks to 1e-16. The central difference in blue falls faster, with slope 2, to about 6e-11 near h = 1e-5, then rises raggedly too. Annotations mark the rounding error region on the left and the best forward step.](../../assets/figures/05-university-core/the-derivative-definition-numerical.svg)

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def forward(f, x, h):
    return (f(x + h) - f(x)) / h

def central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# The derivative of e^x at x = 1 is e, so the exact error is easy to measure.
for h in [1e-1, 1e-3, 1e-5, 1e-8, 1e-11, 1e-14]:
    ef = abs(forward(math.exp, 1, h) - math.e)
    ec = abs(central(math.exp, 1, h) - math.e)
    print(f"{h:.0e}  {ef:.1e}  {ec:.1e}")
# 1e-01  1.4e-01  4.5e-03
# 1e-03  1.4e-03  4.5e-07
# 1e-05  1.4e-05  5.9e-11
# 1e-08  6.6e-09  6.6e-09
# 1e-11  3.3e-05  1.0e-05
# 1e-14  9.3e-03  9.3e-03

# At a corner the one-sided slopes disagree, and the central difference hides it.
print(forward(abs, 0, 1e-6), forward(abs, 0, -1e-6), central(abs, 0, 1e-6))  # 1.0 -1.0 0.0

# Marginal cost at q = 100 for C(q) = 1000 + 10q + 0.05q^2 (exact value 20).
C = lambda q: 1000 + 10 * q + 0.05 * q**2
print(round(central(C, 100, 1e-3), 6))  # 20.0
```

The table shows the V: from $h = 10^{-1}$ down to $10^{-5}$ the central error drops by a factor of 100 for every factor of 10 in $h$, the signature of an error proportional to $h^2$, and then rounding error takes over. The corner line is a warning. The central difference of $\lvert x \rvert$ at 0 is exactly 0, a number that is not the derivative, because the derivative doesn't exist there. A numerical estimate can't tell you whether a derivative exists. It only estimates the number when you already know it does.

</details>

## FAQ

### Why can't I just put $h = 0$ into the difference quotient?

Because the quotient is $\frac{0}{0}$ at $h = 0$, which has no value. The limit asks what the quotient approaches as $h$ gets close to 0 without ever equalling 0. Algebra turns the quotient into an expression, like $2x + h$, that agrees with it for every $h \ne 0$ and is fine at $h = 0$. The limit of the original is the value of the new expression at 0.

### Is $\frac{dy}{dx}$ a fraction?

It is a limit of fractions, $\frac{\Delta y}{\Delta x}$, and it is written as one symbol for the derivative. It acts like a fraction in many formulas, such as the [chain rule](03-chain-rule-implicit-and-inverse-derivatives.md), which is why Leibniz's notation is so convenient. But in this course the safe reading is "the derivative of $y$ with respect to $x$", and you shouldn't cancel the $d$'s as if they were numbers.

### Is the tangent line the line that touches the curve at one point?

No. For a circle that works, and that is where the word comes from, but it fails in general. The line $y = 0$ is the tangent to $y = x^3$ at the origin, and it crosses the curve there, from below to above. The line $y = 1$ is tangent to $y = \sin x$ at $x = \frac{\pi}{2}$ and touches the curve again at $x = \frac{\pi}{2} + 2\pi$ and at every other peak. A vertical line meets the parabola $y = x^2$ at only one point and is not a tangent. The definition by the limit of secant slopes is the one that works.

### If $f'(a) = 0$, is the function constant near $a$?

No. The derivative at one point says only that the tangent line is horizontal there. For $f(x) = x^2$, we have $f'(0) = 0$, and the function is not constant near 0. A function whose derivative is 0 on a whole interval is constant on it, and that is a theorem proved in [The mean value theorem and extrema](../03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md).

## Practice

### Warm-up

1\. For $f(x) = x^2 + 4x$, use the definition to find $f'(x)$. Then write the equation of the tangent line at $x = 3$.

<details class="solution" markdown>
<summary>Solution</summary>

The quotient is $\frac{(x + h)^2 + 4(x + h) - x^2 - 4x}{h} = \frac{2xh + h^2 + 4h}{h} = 2x + 4 + h$. Letting $h \to 0$ gives $f'(x) = 2x + 4$.

At $x = 3$: $f(3) = 9 + 12 = 21$ and $f'(3) = 10$. The tangent line is $y = 21 + 10(x - 3) = 10x - 9$.

Check: the line passes through $(3, 21)$, since $10 \cdot 3 - 9 = 21$. With $h = 0.001$ at $x = 3$ the quotient is $\frac{f(3.001) - f(3)}{0.001} = 10.001$, close to 10.

</details>

2\. Which of these are differentiable at 0, and why: (a) $x^2$, (b) $\lvert x \rvert$, (c) $x^{1/3}$, (d) the step function that is 0 for $x < 0$ and 1 for $x \ge 0$?

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Differentiable. By Example 1, $f'(0) = 2 \cdot 0 = 0$.
- (b) Not differentiable: a corner, with one-sided slopes $1$ and $-1$.
- (c) Not differentiable: a vertical tangent. The quotient $h^{-2/3}$ tends to $\infty$.
- (d) Not differentiable: the function has a jump at 0, so it isn't continuous there, and differentiable implies continuous.

Check with the zoom-in test: only the parabola flattens into a line when you zoom in at the origin.

</details>

3\. A store's total revenue is $R(t)$ dollars after $t$ hours of a sale. What do (a) $R'(5) = 120$ and (b) $R'(8) = -15$ mean, with units? Could (b) happen?

<details class="solution" markdown>
<summary>Solution</summary>

(a) At 5 hours into the sale, total revenue is growing at the rate of \$120 per hour. In the next hour it increases by about \$120.

(b) At 8 hours total revenue is falling at \$15 per hour. This can't happen if revenue is a running total of sales, since a running total never decreases. It could happen if $R$ means something else, such as revenue in the current hour, or if refunds are subtracted from the total.

Check: both answers carry units of dollars per hour, "output units per input unit".

</details>

### Standard

4\. Use the definition to find the derivative of $f(x) = \frac{1}{x + 1}$ for $x \ne -1$, and the tangent line at $x = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

Combine over a common denominator:

$$
\frac{\frac{1}{x + h + 1} - \frac{1}{x + 1}}{h} = \frac{1}{h} \cdot \frac{(x + 1) - (x + h + 1)}{(x + h + 1)(x + 1)} = \frac{-1}{(x + h + 1)(x + 1)}.
$$

Letting $h \to 0$ gives $f'(x) = -\frac{1}{(x + 1)^2}$.

At $x = 1$: $f(1) = \frac{1}{2}$ and $f'(1) = -\frac{1}{4}$. The tangent line is $y = \frac{1}{2} - \frac{1}{4}(x - 1) = \frac{3}{4} - \frac{x}{4}$.

Check: with $h = 0.001$ at $x = 1$, the quotient is $\frac{1/2.001 - 1/2}{0.001} = -0.24988$, close to $-0.25$. The graph of $\frac{1}{x + 1}$ is $\frac{1}{x}$ shifted left by 1, so its slope at $x = 1$ should equal the slope of $\frac{1}{x}$ at $x = 2$, which is $-\frac{1}{4}$ by Example 2.

</details>

5\. Let $f(x) = x^2$ for $x \le 1$ and $f(x) = 3x - 2$ for $x > 1$. (a) Show that $f$ is continuous at 1. (b) Find the slope from the left and from the right at $x = 1$. (c) Is $f$ differentiable at 1? (d) Which constant should replace 3 so that the function is differentiable at 1?

<details class="solution" markdown>
<summary>Solution</summary>

(a) From the left, $x^2 \to 1$. From the right, $3x - 2 \to 1$. Also $f(1) = 1$. So the limit equals the value and $f$ is continuous at 1.

(b) From the left, for $h < 0$ the quotient is $\frac{(1 + h)^2 - 1}{h} = 2 + h \to 2$. From the right, for $h > 0$ it is $\frac{3(1 + h) - 2 - 1}{h} = \frac{3h}{h} = 3$. The slopes are 2 and 3.

(c) No, since $2 \ne 3$. The graph has a corner at $(1, 1)$, though it is continuous.

(d) The right branch must pass through $(1, 1)$ with slope 2: $y = 1 + 2(x - 1) = 2x - 1$. So $f(x) = 2x - 1$ for $x > 1$ gives a function that is differentiable at 1, with $f'(1) = 2$.

Check: with $2x - 1$, the right-hand quotient is $\frac{2(1 + h) - 1 - 1}{h} = 2$, which matches the left-hand limit of 2.

</details>

6\. (Reviews [reading function graphs](../../03-high-school/03-functions/02-reading-function-graphs.md).) For $f(x) = x^2 - 4x$, the quick check of that lesson found an average rate of change of 1 from $x = 1$ to $x = 4$. (a) Find the average rate of change from $x = 2$ to $x = 2 + h$, simplified, and use it to find $f'(2)$. (b) Find $f'(x)$ and the point where the tangent line has slope 1. (c) Is that point between 1 and 4? What does the secant slope 1 have to do with it?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $f(2) = -4$, and $f(2 + h) = 4 + 4h + h^2 - 8 - 4h = -4 + h^2$. The average rate is $\frac{h^2}{h} = h$, so $f'(2) = \lim_{h \to 0} h = 0$. The tangent at $x = 2$ is horizontal, at the vertex.

(b) The same steps at a general $x$ give $\frac{(x + h)^2 - 4(x + h) - x^2 + 4x}{h} = 2x - 4 + h$, so $f'(x) = 2x - 4$. Solving $2x - 4 = 1$ gives $x = 2.5$.

(c) Yes, $2.5$ lies between 1 and 4. The tangent at $x = 2.5$ is parallel to the secant from $x = 1$ to $x = 4$. For every smooth curve there is such a point somewhere between the endpoints, a fact called the mean value theorem and proved in [The mean value theorem and extrema](../03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md).

Check: $f'(2.5) = 5 - 4 = 1$. The vertex of $x^2 - 4x$ is at $x = 2$, where $2 \cdot 2 - 4 = 0$, as found in (a).

</details>

### Challenge

7\. (a) Prove that if $f$ is differentiable at $a$, then $\lim_{h \to 0} \frac{f(a + h) - f(a - h)}{2h} = f'(a)$. (b) Show that the converse fails: for $f(x) = \lvert x \rvert$ the limit in (a) exists at $a = 0$, but $f'(0)$ doesn't.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Split the numerator at $f(a)$:

$$
\frac{f(a + h) - f(a - h)}{2h} = \frac{1}{2}\left[\frac{f(a + h) - f(a)}{h} + \frac{f(a - h) - f(a)}{-h}\right].
$$

As $h \to 0$ the first fraction tends to $f'(a)$. The second is the difference quotient with $-h$ in the place of $h$, and $-h \to 0$ too, so it also tends to $f'(a)$. The limit is $\frac{1}{2}\left(f'(a) + f'(a)\right) = f'(a)$.

(b) For $f(x) = \lvert x \rvert$ at 0, the expression is $\frac{\lvert h \rvert - \lvert -h \rvert}{2h} = 0$ for every $h \ne 0$, so the limit is 0. But Example 3 showed that $f'(0)$ doesn't exist.

Check: for $f(x) = x^2$ at $a = 3$, $\frac{(3 + h)^2 - (3 - h)^2}{2h} = \frac{12h}{2h} = 6 = f'(3)$.

</details>

8\. Let $f(x) = x\lvert x \rvert$. (a) Use the definition to show that $f'(0)$ exists and find it. (b) Find $f'(x)$ for $x \ne 0$ by writing $f$ without absolute value on each side. (c) Is $f'$ continuous at 0?

<details class="solution" markdown>
<summary>Solution</summary>

(a) At 0 the quotient is $\frac{h\lvert h \rvert - 0}{h} = \lvert h \rvert$, which tends to 0 from both sides. So $f'(0) = 0$, even though $f$ contains an absolute value.

(b) For $x > 0$ we have $f(x) = x^2$, so $f'(x) = 2x$. For $x < 0$ we have $f(x) = -x^2$, whose quotient $\frac{-(x + h)^2 + x^2}{h} = -2x - h$ gives $f'(x) = -2x$. So $f'(x) = 2\lvert x \rvert$ for all $x$, including 0.

(c) Yes: $2\lvert x \rvert \to 0 = f'(0)$ as $x \to 0$. The function is smooth at 0, though the absolute value in its formula suggests a corner. Its derivative $2\lvert x \rvert$, however, has a corner at 0, so $f'$ itself is not differentiable there.

Check: $f(0.001) = 0.000001$, so the slope of the secant from 0 is $0.001$, close to 0.

</details>

## Where this shows up

- The next lesson, [differentiation rules](02-differentiation-rules.md), builds shortcuts so that you never need the limit again for ordinary functions. The applications chapter uses the derivative for marginal analysis, linear approximation, and finding maxima and minima ([rates of change and marginal analysis](../03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md)).
- In computer science, the same difference quotient checks the gradients of a machine-learning model: a numerical gradient check compares the formula's answer with a central difference. Floating-point rounding is why the step can't be too small.
- In economics, marginal cost, marginal revenue and marginal utility are all derivatives ([marginal analysis with derivatives](../../07-economics-math/03-firms-and-consumers/01-marginal-analysis-with-derivatives.md)). A tangent line to a curve is also the best linear model near a point, the idea behind [Linear approximation and L'Hopital's rule](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md).
