# Linear approximation and L'Hopital's rule

After this lesson you can estimate a function value with its tangent line and say how big the error is, use Newton's method to solve an equation (and know when it fails), evaluate indeterminate limits with L'Hopital's rule, and rank growth rates such as $\ln x$, $x^p$ and $e^x$.

Before this: [the derivative definition](../02-derivatives/01-the-derivative-definition.md), [differentiation rules](../02-derivatives/02-differentiation-rules.md), [chain rule, implicit and inverse derivatives](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md) and [rates of change and marginal analysis](01-rates-of-change-and-marginal-analysis.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Use the tangent line to $f(x) = \sqrt{x}$ at $x = 4$ to estimate $\sqrt{4.1}$.
2. Find $\lim_{x \to 0} \frac{e^{3x} - 1}{x}$.
3. Do one step of Newton's method for $x^2 - 2 = 0$ starting from $x_0 = 1.5$.

<details class="solution" markdown>
<summary>Answers</summary>

1. $f(4) = 2$ and $f'(x) = \frac{1}{2\sqrt{x}}$, so $f'(4) = \frac{1}{4}$. Then $\sqrt{4.1} \approx 2 + \frac{1}{4}(0.1) = 2.025$.
2. The limit has the form $\frac{0}{0}$. Differentiate top and bottom: $\frac{3e^{3x}}{1} \to 3$. So the limit is 3.
3. $x_1 = x_0 - \frac{f(x_0)}{f'(x_0)} = 1.5 - \frac{0.25}{3} = \frac{17}{12} \approx 1.41667$.

</details>

## The idea

Your calculator gives $\sqrt{4.1}$ instantly, but suppose it didn't. You know that $\sqrt{4} = 2$, and 4.1 is a little more than 4. How much more is the square root? The function $\sqrt{x}$ is climbing at the rate $f'(4) = \frac{1}{4}$ at $x = 4$, so a step of 0.1 should add about $\frac{1}{4} \cdot 0.1 = 0.025$. That gives 2.025. The true value is 2.02485, so the estimate is off by about 0.00015.

This is the idea of **linear approximation**: near a point, a smooth curve is almost its tangent line, so replace the curve by the line. A line is easy to evaluate and to solve, and the derivative is the only thing needed to build it. This lesson uses that single idea three times.

First, to estimate values and errors, as above. Second, to solve equations: if $f(x) = 0$ is hard, replace $f$ by its tangent line at a guess, solve the line's equation (it is a linear equation, so easy), and take the answer as the next guess. This is Newton's method. Third, to find limits that look like $\frac{0}{0}$: near $a$, $f(x) \approx f'(a)(x - a)$ and $g(x) \approx g'(a)(x - a)$, so $\frac{f(x)}{g(x)}$ behaves like $\frac{f'(a)}{g'(a)}$ and the troublesome factor $x - a$ cancels. This is L'Hopital's rule.

The last part of the lesson compares how fast functions grow, which is a limit at infinity of the same kind, and which is the language of algorithm analysis.

## Definitions

Let $f$ be differentiable at $a$. The **linearization** of $f$ at $a$ is the function

$$
L(x) = f(a) + f'(a)(x - a).
$$

Its graph is the tangent line at $(a, f(a))$. In plain words, $L$ is the straight-line function that matches $f$ in value and in slope at $a$, and $f(x) \approx L(x)$ for $x$ near $a$. The point $a$ is the base point, chosen so that $f(a)$ and $f'(a)$ are easy to compute.

The **differential** is a way to write the same thing with changes. Let $dx$ be a small change in $x$, which is just a number, equal to $\Delta x$. Then

$$
dy = f'(x)\,dx \qquad\text{and}\qquad \Delta y = f(x + dx) - f(x).
$$

In plain words, $\Delta y$ is the true change in $f$ over a step of $dx$ (the change along the curve), $dy$ is the change in the tangent line over the same step, and $\Delta y \approx dy$ when $dx$ is small. This is the approximation $C(q + 1) - C(q) \approx C'(q)$ from [rates of change and marginal analysis](01-rates-of-change-and-marginal-analysis.md), with $dx = 1$.

The word "best" in "best linear approximation" has a precise meaning. Write the error of the line through $(a, f(a))$ with slope $m$ as $e_m(x) = f(x) - f(a) - m(x - a)$. Every such line has error $e_m(x) \to 0$ as $x \to a$, because every such line passes through $(a, f(a))$. The tangent line is the only one for which the error vanishes faster than the distance:

$$
\lim_{x \to a} \frac{e_m(x)}{x - a} = 0 \quad\text{exactly when}\quad m = f'(a).
$$

To see this, note that $\frac{e_m(x)}{x - a} = \frac{f(x) - f(a)}{x - a} - m$. As $x \to a$ the first term tends to $f'(a)$, so the whole expression tends to $f'(a) - m$, which is 0 if and only if $m = f'(a)$. In plain words, the derivative is the one slope that makes the error small even compared with the step, and a line with any other slope is worse by a fixed fraction of the step.

An **indeterminate form** is a limit of a quotient, product, difference or power in which the limits of the parts don't decide the answer. The forms are $\frac{0}{0}$, $\frac{\infty}{\infty}$, $0 \cdot \infty$, $\infty - \infty$, $1^\infty$, $0^0$ and $\infty^0$. In plain words, $\frac{0}{0}$ can be 0, 1, 5 or $\infty$, depending on how fast the top and bottom go to 0: $\frac{x^2}{x}$, $\frac{x}{x}$, $\frac{5x}{x}$ and $\frac{x}{x^2}$ all have the form $\frac{0}{0}$ at $x = 0$, and their limits are 0, 1, 5 and no limit. The limit laws give no help, and the form has to be changed or investigated.

**L'Hopital's rule** is the following theorem. Suppose $f$ and $g$ are differentiable near $a$, except possibly at $a$, with $g'(x) \ne 0$ near $a$ for $x \ne a$, and that $\lim_{x \to a} \frac{f(x)}{g(x)}$ has the form $\frac{0}{0}$ or $\frac{\pm\infty}{\pm\infty}$. If $\lim_{x \to a} \frac{f'(x)}{g'(x)}$ exists, as a real number or as $\pm\infty$, then

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}.
$$

The same holds for one-sided limits, and for $x \to \infty$ or $x \to -\infty$. In plain words, when a quotient is stuck at $\frac{0}{0}$ or $\frac{\infty}{\infty}$, differentiate the top and the bottom separately (not with the quotient rule), and look at the new quotient.

For functions $f$ and $g$ defined for large $x$, write $f \ll g$ and say "$g$ grows faster than $f$" when

$$
\lim_{x \to \infty} \frac{f(x)}{g(x)} = 0.
$$

In plain words, $g$ eventually dwarfs $f$: the ratio shrinks to nothing. The CS version of this is the little-$o$ of [asymptotic notation](../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md).

## How to do it

### Estimating with a tangent line

1. Pick a base point $a$ near the input $x$, where $f(a)$ and $f'(a)$ are easy (for $\sqrt{4.1}$, take $a = 4$).
2. Compute $f(a)$ and $f'(a)$.
3. Write $L(x) = f(a) + f'(a)(x - a)$ and evaluate it at $x$.
4. Estimate the error. Informally, the error is about $\frac{1}{2}f''(a)(x - a)^2$, and its sign says which way the estimate errs: where $f'' > 0$ the curve bends up, away from the tangent, and the line underestimates, and where $f'' < 0$ the line overestimates.
5. Check with a calculator or code, and compare the error with the estimate in Step 4.

The size of the error has a clean statement. It is proved in [the mean value theorem and extrema](03-mean-value-theorem-and-extrema.md#the-error-of-a-tangent-line-approximation), and it is the first case of Taylor's theorem ([power series and Taylor series](../05-sequences-and-series/04-power-series-and-taylor-series.md)): if $\lvert f''(t) \rvert \le M$ for all $t$ between $a$ and $x$, then

$$
\lvert f(x) - L(x) \rvert \le \frac{M}{2}(x - a)^2.
$$

The key feature is the square: halving the distance from $a$ quarters the error.

The linearizations at $a = 0$ of the common functions are the ones worth knowing by heart. The angle is in radians.

| Function | Linearization at 0 | Why |
|---|---|---|
| $\sin x$ | $x$ | $f(0) = 0$, $f'(0) = \cos 0 = 1$ |
| $\cos x$ | $1$ | $f(0) = 1$, $f'(0) = -\sin 0 = 0$ |
| $\tan x$ | $x$ | $f(0) = 0$, $f'(0) = \sec^2 0 = 1$ |
| $e^x$ | $1 + x$ | $f(0) = f'(0) = 1$ |
| $\ln(1 + x)$ | $x$ | $f(0) = 0$, $f'(0) = \frac{1}{1 + 0} = 1$ |
| $(1 + x)^k$ | $1 + kx$ | $f(0) = 1$, $f'(0) = k$ |

### Newton's method

To solve $f(x) = 0$ with a differentiable $f$:

1. Make a guess $x_0$, near the root if you can (a graph helps).
2. Draw the tangent line at $(x_0, f(x_0))$: $y = f(x_0) + f'(x_0)(x - x_0)$. Where it crosses the $x$-axis is the next guess $x_1$. Setting $y = 0$ and solving gives $x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}$.
3. Repeat with the new guess: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$.
4. Stop when the step $\lvert x_{n+1} - x_n \rvert$ is smaller than the accuracy you want, and check by evaluating $f(x_{n+1})$.

The figure shows the first steps for $x^2 - 2 = 0$ from $x_0 = 2$. Each tangent line is close to the curve, so its zero is close to the curve's zero.

![The parabola y = x squared minus 2 for x from 1.15 to 2.3. A red tangent line at x equals 2 crosses the horizontal axis at x equals 1.5, where an orange tangent line starts, and that one crosses at about 1.4167, labelled x2. Dashed vertical segments join each guess on the axis to the curve.](../../assets/figures/05-university-core/linear-approximation-and-lhopitals-rule-newton.svg)

For $f(x) = x^2 - 2$ the update is $x_{n+1} = x_n - \frac{x_n^2 - 2}{2x_n} = \frac{1}{2}\left(x_n + \frac{2}{x_n}\right)$, the average of $x_n$ and $\frac{2}{x_n}$. Starting from $x_0 = 1$:

| $n$ | $x_n$ | Error $x_n - \sqrt{2}$ |
|---|---|---|
| 0 | 1 | $-0.41$ |
| 1 | 1.5 | $0.086$ |
| 2 | 1.4166667 | $0.0025$ |
| 3 | 1.4142157 | $0.0000021$ |
| 4 | 1.41421356237469 | $0.0000000000016$ |

The error is roughly squared at each step. For this function there is an exact formula: subtract $\sqrt{2}$ from the update to get

$$
x_{n+1} - \sqrt{2} = \frac{x_n^2 - 2\sqrt{2}x_n + 2}{2x_n} = \frac{(x_n - \sqrt{2})^2}{2x_n}.
$$

When $x_n$ is near 1.4 the denominator is about 2.8, so an error of 0.0025 becomes about $\frac{0.0025^2}{2.83} = 0.0000022$. The number of correct digits roughly doubles at each step, which is called quadratic convergence and is why Newton's method is fast. In general it behaves like this whenever $f'$ at the root is not 0, and the standard proof uses the second-derivative error bound for a tangent line.

Newton's method can fail, and the figure shows two ways.

![Two panels. On the left, the curve y = x cubed minus 2x plus 2 with two tangent lines: the tangent at x equals 0 hits the axis at x equals 1, and the tangent at x equals 1 hits the axis back at 0, so the guesses cycle between 0 and 1 forever. On the right, the graph of the cube root of x with tangent lines at x equals 1, minus 2 and 4, each landing farther from the root at 0 than the last.](../../assets/figures/05-university-core/linear-approximation-and-lhopitals-rule-newton-fails.svg)

- A flat tangent: if $f'(x_n) = 0$ the tangent never reaches the axis and the formula divides by 0. For $x^2 - 2$ starting at $x_0 = 0$, this happens at once.
- A cycle: for $f(x) = x^3 - 2x + 2$ from $x_0 = 0$ the guesses are $0, 1, 0, 1, \ldots$ forever, although the equation has a root near $-1.769$.
- Divergence: for $f(x) = \sqrt[3]{x}$ the iteration is $x_{n+1} = x_n - \frac{x_n^{1/3}}{\frac{1}{3}x_n^{-2/3}} = -2x_n$, so the guesses $1, -2, 4, -8, \ldots$ run away from the root at 0.
- A surprising root: for $f(x) = x^3 - x$ with roots $-1$, $0$ and $1$, the start $x_0 = 0.5$ jumps to $-1$, which is not the nearest root. The start $x_0 = 0.45$ bounces to $-10.2$ by the third step and takes about a dozen steps to settle on $-1$. Near a point where $f'$ is small, one step can send the guess far away.
- Slow convergence: at a double root, as for $(x - 1)^2$, each step only halves the error, so the quadratic speed is lost.

### L'Hopital's rule

1. Substitute the limit value. If the result is a number, you're done: the limit laws apply. If it is $\frac{0}{0}$ or $\frac{\infty}{\infty}$, go on.
2. Differentiate the top and the bottom separately.
3. Find the limit of the new quotient. If it exists (or is $\pm\infty$), that is the answer.
4. If the new quotient is again $\frac{0}{0}$ or $\frac{\infty}{\infty}$, repeat Step 2.
5. For the other indeterminate forms, first rewrite them as a quotient (see below), and then apply Steps 1 to 4.
6. Check with a table of values near the limit point.

Two conditions are easy to forget, and each has a counterexample.

The form must be indeterminate. Take $\lim_{x \to 0} \frac{x + 1}{x + 2} = \frac{1}{2}$. If you differentiate anyway, you get $\frac{1}{1} = 1$, which is wrong.

The limit of the new quotient must exist. Take $\lim_{x \to \infty} \frac{x + \sin x}{x}$. This is $\frac{\infty}{\infty}$ and the true limit is 1, since the quotient is $1 + \frac{\sin x}{x}$ and $\frac{\sin x}{x} \to 0$ by the squeeze theorem. The quotient of the derivatives is $\frac{1 + \cos x}{1} = 1 + \cos x$, which oscillates between 0 and 2 and has no limit. The rule says nothing when the limit of the new quotient doesn't exist, and the original limit may still exist.

#### Why the rule works

The simplest case has a full proof. Suppose $f$ and $g$ are differentiable at $a$, with $f(a) = g(a) = 0$ and $g'(a) \ne 0$. For $x$ close to $a$ with $x \ne a$, the difference quotient $\frac{g(x)}{x - a} = \frac{g(x) - g(a)}{x - a}$ is close to $g'(a) \ne 0$, so $g(x) \ne 0$ there, and

$$
\frac{f(x)}{g(x)} = \frac{f(x)/(x - a)}{g(x)/(x - a)} = \frac{\frac{f(x) - f(a)}{x - a}}{\frac{g(x) - g(a)}{x - a}} \longrightarrow \frac{f'(a)}{g'(a)}
$$

by the limit law for quotients. This is the picture from the idea section, made exact: the common factor $x - a$ cancels. If $f'$ and $g'$ are also continuous at $a$, then $\frac{f'(x)}{g'(x)} \to \frac{f'(a)}{g'(a)}$ too, so the limit of the new quotient agrees. The general case, where $f'(a)$ and $g'(a)$ may not exist or are both 0, needs a theorem that comes in [the mean value theorem and extrema](03-mean-value-theorem-and-extrema.md#lhopitals-rule-proved), where the $\frac{0}{0}$ case is proved. The $\frac{\infty}{\infty}$ case is proved the same way in a longer argument that textbooks give in full.

### The other indeterminate forms

Each of these is turned into a quotient so that L'Hopital's rule applies.

| Form | Method | Example |
|---|---|---|
| $0 \cdot \infty$ | write $uv$ as $\frac{u}{1/v}$ | $x \ln x$ as $x \to 0^+$ |
| $\infty - \infty$ | combine into one fraction | $\frac{1}{x} - \frac{1}{\sin x}$ as $x \to 0$ |
| $1^\infty$, $0^0$, $\infty^0$ | take $\ln$ of $y = f^g$ to get $g \ln f$, a $0 \cdot \infty$ form, then use $y = e^{\ln y}$ | $\left(1 + \frac{1}{x}\right)^x$ as $x \to \infty$ |

The last example gives the number $e$. Let $y = \left(1 + \frac{1}{x}\right)^x$, which has the form $1^\infty$ as $x \to \infty$. Then $\ln y = x\ln\left(1 + \frac{1}{x}\right) = \frac{\ln(1 + 1/x)}{1/x}$, which is $\frac{0}{0}$. Differentiate top and bottom with respect to $x$:

$$
\frac{\frac{1}{1 + 1/x}\cdot\left(-\frac{1}{x^2}\right)}{-\frac{1}{x^2}} = \frac{1}{1 + 1/x} \longrightarrow 1.
$$

So $\ln y \to 1$, and since $e^t$ is continuous, $y = e^{\ln y} \to e^1 = e$. The high-school lesson on [exponential functions and growth](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md) accepted this limit from a table of values, and this argument proves it. The same steps with $\frac{r}{x}$ in place of $\frac{1}{x}$ give $\left(1 + \frac{r}{x}\right)^x \to e^r$, which is continuous compounding at the rate $r$.

### Growth rates

*Theorem.* For every $p > 0$ and every $b > 1$,

$$
\ln x \ll x^p \ll b^x, \qquad\text{that is,}\qquad \lim_{x \to \infty} \frac{\ln x}{x^p} = 0 \quad\text{and}\quad \lim_{x \to \infty} \frac{x^p}{b^x} = 0.
$$

We know that all three functions tend to $\infty$, and that L'Hopital's rule applies to $\frac{\infty}{\infty}$. We want the two limits to be 0. The plan is to apply the rule to $\frac{\ln x}{x^p}$ once, and to $\frac{x^n}{e^x}$ with a whole number $n$ repeatedly, and then reduce the general case to these.

*Proof.* First, $\frac{\ln x}{x^p}$ is $\frac{\infty}{\infty}$, and $\frac{1/x}{px^{p-1}} = \frac{1}{px^p} \to 0$. By L'Hopital's rule, $\frac{\ln x}{x^p} \to 0$.

Next, for a whole number $n \ge 1$, apply the rule $n$ times to $\frac{x^n}{e^x}$. Each time the top loses one power and the bottom stays $e^x$, reaching $\frac{n!}{e^x} \to 0$. For a real $p > 0$ pick a whole number $n \ge p$. For $x \ge 1$ we have $0 < x^p \le x^n$, so $0 < \frac{x^p}{e^x} \le \frac{x^n}{e^x} \to 0$, and the squeeze theorem gives $\frac{x^p}{e^x} \to 0$.

Finally, for a base $b > 1$ write $b^x = e^{(\ln b)x}$ and let $u = (\ln b)x$, which tends to $\infty$ as $x$ does. Then $\frac{x^p}{b^x} = (\ln b)^{-p}\frac{u^p}{e^u} \to 0$. $\blacksquare$

Look back at what the theorem does not say. It says "eventually", and eventually can be far away. The figure shows both ratios rising before they fall.

![Two panels. On the left, the ratio of ln x to the square root of x, which rises to a peak of about 0.74 at x equal to e squared, about 7.4, and then falls slowly, still about 0.26 at x equal to 600. On the right, the ratio of x to the fifth power to e to the x, which peaks at about 21 at x equal to 5, falls below 1 near x equal to 13, and drops towards 0.](../../assets/figures/05-university-core/linear-approximation-and-lhopitals-rule-growth.svg)

| $x$ | $\dfrac{\ln x}{\sqrt{x}}$ | $\dfrac{x^3}{e^x}$ |
|---|---|---|
| 10 | $0.728$ | $0.0454$ |
| 100 | $0.461$ | $3.7 \times 10^{-38}$ |
| 1,000 | $0.218$ | essentially 0 |
| 1,000,000 | $0.0138$ | essentially 0 |

Logarithms are slow to be overtaken by roots (a million inputs before the ratio is about 1%), and exponentials overtake every power almost at once.

## Worked examples

<div class="example" markdown>

### Example 1: estimating a square root

Estimate $\sqrt{4.1}$ and bound the error.

Step 1: the base point is $a = 4$, because $\sqrt{4} = 2$ exactly and 4.1 is close.

Step 2: $f(x) = \sqrt{x}$, so $f(4) = 2$, and $f'(x) = \frac{1}{2}x^{-1/2}$ gives $f'(4) = \frac{1}{4}$.

Step 3: $L(x) = 2 + \frac{1}{4}(x - 4)$, so $L(4.1) = 2 + 0.025 = 2.025$.

Step 4: $f''(x) = -\frac{1}{4}x^{-3/2}$, which is negative, so the curve bends down and the tangent line is above the curve: the estimate is too large. Between 4 and 4.1 we have $\lvert f''(t) \rvert \le \frac{1}{4}\cdot 4^{-3/2} = \frac{1}{32}$, so the error is at most $\frac{1}{2}\cdot\frac{1}{32}\cdot 0.1^2 = 0.00015625$.

Check: $\sqrt{4.1} = 2.0248457\ldots$, so the true error is $2.025 - 2.0248457 = 0.000154$. It is positive, as Step 4 predicted (the estimate is too large), and it is below the bound 0.000156. The answer is $2.025$, correct to within 0.00016.

</div>

<div class="example" markdown>

### Example 2: sin(0.1) and when the line is not enough

Estimate $\sin(0.1)$, with 0.1 in radians, and estimate $1.03^{10}$.

For the sine, the base point is $a = 0$, and $L(x) = x$ from the table. So $\sin(0.1) \approx 0.1$. The true value is $0.0998334$, and the error is $0.0001666$. The line has an error much smaller than the bound $\frac{M}{2}x^2 = \frac{1}{2}(0.01) = 0.005$ suggests, because $f''(0) = -\sin 0 = 0$: the curve is almost straight at 0 and the first correction is of third order, $\frac{x^3}{6} = 0.0001667$.

For $1.03^{10}$ use $(1 + x)^k \approx 1 + kx$ with $x = 0.03$ and $k = 10$. This gives $1.3$. The true value is $1.3439$, and the estimate is 3% too low. The second derivative of $(1 + x)^{10}$ is $90(1 + x)^8$, which is about 90, so the error is about $\frac{1}{2} \cdot 90 \cdot 0.03^2 = 0.0405$, close to the true error $0.0439$.

The lesson from the second estimate: the linearization is good when the step is small compared with how fast the slope changes. Here $kx = 0.3$ is not small. The second derivative tells you before you compute whether to trust the line.

Check: both true values from a calculator are $0.0998334$ and $1.3439164$, and the error sizes follow the second-derivative estimates.

</div>

<div class="example" markdown>

### Example 3: errors in a measurement

A sphere's radius is measured as 10 cm, with a possible error of 0.1 cm. Estimate the error in the volume $V = \frac{4}{3}\pi r^3$.

The differential is $dV = V'(r)\,dr = 4\pi r^2\,dr = 4\pi \cdot 100 \cdot 0.1 = 40\pi \approx 125.7$ cm$^3$. The volume itself is $V = \frac{4}{3}\pi \cdot 1000 \approx 4188.8$ cm$^3$, so the relative error is $\frac{dV}{V} = \frac{125.7}{4188.8} = 3\%$. It is three times the 1% relative error of the radius, because $\frac{dV}{V} = 3\frac{dr}{r}$ for $V \propto r^3$.

Check: the true change is $\frac{4}{3}\pi(10.1^3 - 10^3) = 126.9$ cm$^3$, within about 1% of the estimate. For a power $x^n$ the relative error is always $n$ times that of $x$, which is why measuring a radius precisely matters more for a volume than for a length.

</div>

<div class="example" markdown>

### Example 4: Newton's method for cos x = x

Solve $\cos x = x$. A graph of $\cos x$ and $x$ shows them meeting once, between 0 and 1, so take $x_0 = 1$.

Let $f(x) = \cos x - x$, so $f'(x) = -\sin x - 1$. Then

$$
x_1 = 1 - \frac{\cos 1 - 1}{-\sin 1 - 1} = 1 - \frac{-0.4597}{-1.8415} = 0.75036.
$$

The next steps are $x_2 = 0.7391129$, $x_3 = 0.7390851334$ and $x_4 = 0.7390851332$. The differences between steps are 0.25, 0.011, 0.000028 and 0.0000000002, which are roughly squared each time.

Check: $\cos(0.7390851332) = 0.7390851332$ to ten places. The root is $0.7390851332\ldots$, and four steps gave ten digits.

</div>

<div class="example" markdown>

### Example 5: several limits with L'Hopital's rule

(a) $\lim_{x \to 0} \frac{e^x - 1 - x}{x^2}$. The form is $\frac{0}{0}$. Differentiate: $\frac{e^x - 1}{2x}$, which is $\frac{0}{0}$ again. Differentiate again: $\frac{e^x}{2} \to \frac{1}{2}$. The limit is $\frac{1}{2}$.

(b) $\lim_{x \to 0^+} x\ln x$. The form is $0 \cdot (-\infty)$. Write it as $\frac{\ln x}{1/x}$, which is $\frac{-\infty}{\infty}$. Differentiate: $\frac{1/x}{-1/x^2} = -x \to 0$. The limit is 0, so $x$ beats $\ln x$ at 0: the logarithm blows up, but more slowly than $x$ shrinks.

(c) $\lim_{x \to 0}\left(\frac{1}{x} - \frac{1}{\sin x}\right)$. The form is $\infty - \infty$. Combine: $\frac{\sin x - x}{x\sin x}$, which is $\frac{0}{0}$. Differentiate: $\frac{\cos x - 1}{\sin x + x\cos x}$, still $\frac{0}{0}$. Differentiate again: $\frac{-\sin x}{2\cos x - x\sin x} \to \frac{0}{2} = 0$. The limit is 0.

Check by table: at $x = 0.01$, (a) gives $0.50167$, (b) gives $-0.0461$, and (c) gives $-0.00167$. Each is near its limit and heads towards it as $x$ shrinks.

</div>

<div class="example" markdown>

### Example 6: a power limit (finish it yourself)

Find $\lim_{x \to 0^+} x^x$. This has the form $0^0$. Let $y = x^x$, so $\ln y = x\ln x$. From Example 5(b), $x\ln x \to 0$ as $x \to 0^+$.

Now find the limit of $y$ itself.

<details class="solution" markdown>
<summary>Finish</summary>

Since $\ln y \to 0$ and $e^t$ is continuous, $y = e^{\ln y} \to e^0 = 1$. So $\lim_{x \to 0^+} x^x = 1$.

Check: $0.01^{0.01} = e^{0.01\ln 0.01} = e^{-0.0461} = 0.955$, and $0.0001^{0.0001} = e^{-0.00092} = 0.9991$. The values rise towards 1.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: using a linearization far from the base point. $L(x) = x$ for $\sin x$ gives $\sin(1) \approx 1$, and the true value is $0.841$. The estimate is only good for small $x$.

</div>

<div class="warning" markdown>

Watch out: degrees. The statement $\sin x \approx x$ is for $x$ in radians. In degrees, $\sin 5^\circ \approx 0.0872$ and not 5. Convert first: $5^\circ = \frac{5\pi}{180} = 0.0873$ radians.

</div>

<div class="warning" markdown>

Watch out: applying L'Hopital's rule when the form isn't indeterminate. $\lim_{x \to 0}\frac{x + 1}{x + 2}$ is $\frac{1}{2}$, and differentiating top and bottom gives 1.

</div>

<div class="warning" markdown>

Watch out: using the quotient rule on $\frac{f}{g}$ in L'Hopital's rule. The rule differentiates the top and the bottom separately: the new quotient is $\frac{f'}{g'}$, and not $\left(\frac{f}{g}\right)'$.

</div>

<div class="warning" markdown>

Watch out: concluding that the limit doesn't exist when the limit of $\frac{f'}{g'}$ doesn't. The rule gives no answer in that case. $\frac{x + \sin x}{x} \to 1$ although $\frac{1 + \cos x}{1}$ has no limit.

</div>

<div class="warning" markdown>

Watch out: treating $1^\infty$ as 1, or $0 \cdot \infty$ as 0. In $\left(1 + \frac{1}{x}\right)^x$ the base tends to 1 but the exponent tends to $\infty$, and the limit is $e$, not 1.

</div>

<div class="warning" markdown>

Watch out: Newton's method returns a number even when it hasn't found a root. Always check $f(x_n)$ is near 0, and watch for the step size not shrinking.

</div>

## Tricks and shortcuts

Think of $\sin x \approx x$, $e^x \approx 1 + x$, $\ln(1 + x) \approx x$ and $(1 + x)^k \approx 1 + kx$ as the four facts to remember. With them you can estimate $\sqrt{1.04} = (1 + 0.04)^{1/2} \approx 1.02$ and $\ln 1.05 \approx 0.05$ in your head (the true values are 1.0198 and 0.0488).

Percent changes combine through the exponent: if $x$ rises by 2% then $x^3$ rises by about 6%, and $\sqrt{x}$ by about 1%. The reason is $(1 + 0.02)^k \approx 1 + 0.02k$.

L'Hopital's rule is often the slow way to a limit. For a quotient of polynomials as $x \to \infty$, divide by the highest power. Using the rule to show that $\frac{\sin x}{x} \to 1$ is circular, because the derivative of $\sin x$ was found with that very limit.

For Newton's method, the number of correct digits doubles, so stop when two steps agree to the accuracy you need. A starting guess with one correct digit gives 2, 4, 8, 16 digits in four steps, which is about double precision.

## In code

A short Newton function with a tolerance, an iteration limit and a check for a zero slope, run on the examples above, and then the linear approximations against their true values.

<details class="code" markdown>
<summary>In code</summary>

```python
import math


def newton(f, df, x0, tol=1e-12, max_iter=50):
    """Newton's method. Returns (root, number of steps)."""
    x = x0
    for i in range(1, max_iter + 1):
        slope = df(x)
        if slope == 0:
            raise ZeroDivisionError(f"slope is 0 at x = {x}")
        step = f(x) / slope
        x -= step
        if abs(step) < tol:
            return x, i
    raise RuntimeError("no convergence in max_iter steps")


root, steps = newton(lambda x: x * x - 2, lambda x: 2 * x, 1.0)
print(root, steps)
# 1.414213562373095 6

root, steps = newton(lambda x: math.cos(x) - x, lambda x: -math.sin(x) - 1, 1.0)
print(round(root, 10), steps)
# 0.7390851332 5

for x0 in (0.0, 1.0):
    try:
        print(newton(lambda x: x**3 - 2 * x + 2, lambda x: 3 * x * x - 2, x0))
    except RuntimeError as err:
        print("x0 =", x0, "->", err)
# x0 = 0.0 -> no convergence in max_iter steps
# x0 = 1.0 -> no convergence in max_iter steps

try:
    newton(lambda x: x * x - 2, lambda x: 2 * x, 0.0)
except ZeroDivisionError as err:
    print(err)
# slope is 0 at x = 0.0

# Linear approximations against the true values: estimate, true, estimate - true.
for name, approx, true in [
    ("sqrt(4.1)", 2 + 0.1 / 4, math.sqrt(4.1)),
    ("sin(0.1)", 0.1, math.sin(0.1)),
    ("ln(1.05)", 0.05, math.log(1.05)),
    ("1.03**10", 1 + 10 * 0.03, 1.03**10),
]:
    print(name, round(approx, 6), round(true, 6), round(approx - true, 6))
# sqrt(4.1) 2.025 2.024846 0.000154
# sin(0.1) 0.1 0.099833 0.000167
# ln(1.05) 0.05 0.04879 0.00121
# 1.03**10 1.3 1.343916 -0.043916
```

The function stops with an error, and does not return a wrong number, when the iteration cycles or the slope is zero. The signs of the last column match the second derivative: the estimate is too large where $f'' < 0$ ($\sqrt{x}$, $\sin x$ at positive $x$, $\ln(1 + x)$) and too small where $f'' > 0$ ($(1 + x)^{10}$).

</details>

## FAQ

### Why does the tangent line give the best approximation, and not a secant line?

A line through $(a, f(a))$ with any slope $m \ne f'(a)$, a secant included, has an error of about $(f'(a) - m)(x - a)$, which is a fixed fraction of the distance from $a$. The tangent is the limit of the secants, and it is the one line whose error shrinks faster than the distance to $a$, as the formula in the definitions shows. If you need a good approximation over a whole interval and not near one point, a line through the two ends of the interval often has a smaller worst-case error, and the tool is interpolation.

### Why can't I use L'Hopital's rule on $\frac{5}{x}$ as $x \to 0$?

The top tends to 5, not to 0 or $\infty$, so the form isn't indeterminate. The limit laws already say that a quotient with a top tending to 5 and a bottom tending to 0 has no finite limit: from the right it tends to $+\infty$ and from the left to $-\infty$. Differentiating gives $\frac{0}{1} = 0$, which is wrong.

### What if L'Hopital's rule keeps giving $\frac{0}{0}$ forever?

Then the rule is the wrong tool. A standard example is $\lim_{x \to 0}\frac{e^{-1/x^2}}{x}$: each differentiation makes the expression more complicated, with more powers of $\frac{1}{x}$, and never leaves the form $\frac{0}{0}$. Substitute $t = \frac{1}{x}$ instead and the quotient becomes $te^{-t^2}$ as $t \to \infty$, which tends to 0 by the growth-rate theorem. The limit is 0, because the exponential decays faster than any power of $x$ grows.

### Why use Newton's method when bisection is simpler?

Bisection needs a sign change and always works, and it gains one binary digit per step. Newton's method needs the derivative and a good start, and it doubles the number of correct digits per step. Fifty bisection steps give about 15 digits, and Newton's method needs about 5. Programs often use a safe method to get close and then Newton's method to finish.

## Practice

### Warm-up

1\. Find the linearization of $f(x) = \ln x$ at $a = 1$, use it to estimate $\ln 1.05$, and say whether the estimate is too large or too small.

<details class="solution" markdown>
<summary>Solution</summary>

$f(1) = 0$ and $f'(1) = 1$, so $L(x) = x - 1$ and $\ln 1.05 \approx 0.05$. Since $f''(x) = -\frac{1}{x^2} < 0$, the curve bends down and the tangent line is above it, so the estimate is too large.

Check: $\ln 1.05 = 0.04879$, so the estimate is too large by $0.00121$, close to $\frac{1}{2}\lvert f''(1) \rvert (0.05)^2 = 0.00125$.

</details>

2\. Find $\lim_{x \to 0}\frac{1 - \cos x}{x^2}$.

<details class="solution" markdown>
<summary>Solution</summary>

The form is $\frac{0}{0}$. Differentiate: $\frac{\sin x}{2x}$, again $\frac{0}{0}$. Differentiate again: $\frac{\cos x}{2} \to \frac{1}{2}$. The limit is $\frac{1}{2}$.

Check: at $x = 0.1$ the quotient is $\frac{1 - 0.995004}{0.01} = 0.49958$.

</details>

3\. Do one step of Newton's method for $x^3 = 2$, starting from $x_0 = 1.5$.

<details class="solution" markdown>
<summary>Solution</summary>

Let $f(x) = x^3 - 2$, with $f'(x) = 3x^2$. Then $x_1 = 1.5 - \frac{3.375 - 2}{6.75} = 1.5 - 0.2037 = 1.2963$.

Check: $\sqrt[3]{2} = 1.2599$, so the guess moved from error $0.24$ to error $0.036$.

</details>

### Standard

4\. Estimate $\sqrt[3]{8.1}$ with a linearization at $a = 8$. Bound the error with $\frac{M}{2}(x - a)^2$, where $M$ bounds $\lvert f'' \rvert$ on $[8, 8.1]$.

<details class="solution" markdown>
<summary>Solution</summary>

$f(x) = x^{1/3}$, $f(8) = 2$ and $f'(x) = \frac{1}{3}x^{-2/3}$, so $f'(8) = \frac{1}{12}$. Then $\sqrt[3]{8.1} \approx 2 + \frac{0.1}{12} = 2.008333$.

$f''(x) = -\frac{2}{9}x^{-5/3}$, and on $[8, 8.1]$ its size is at most $\frac{2}{9}\cdot 8^{-5/3} = \frac{2}{9 \cdot 32} = 0.006944$. So the error is at most $\frac{0.006944}{2} \cdot 0.01 = 0.0000347$.

Check: $\sqrt[3]{8.1} = 2.0082989$, so the true error is $0.0000345$, just inside the bound.

</details>

5\. Find (a) $\lim_{x \to 0}\frac{x - \sin x}{x^3}$, (b) $\lim_{x \to 0^+} x^2\ln x$, (c) $\lim_{x \to \infty}\left(1 + \frac{3}{x}\right)^x$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The form is $\frac{0}{0}$. Differentiate: $\frac{1 - \cos x}{3x^2}$, still $\frac{0}{0}$. Differentiate again: $\frac{\sin x}{6x}$, still $\frac{0}{0}$. Once more: $\frac{\cos x}{6} \to \frac{1}{6}$.

(b) The form is $0 \cdot (-\infty)$. Write $\frac{\ln x}{x^{-2}}$, which is $\frac{-\infty}{\infty}$. Differentiate: $\frac{1/x}{-2x^{-3}} = -\frac{x^2}{2} \to 0$.

(c) The form is $1^\infty$. With $y$ the expression, $\ln y = x\ln\left(1 + \frac{3}{x}\right) = \frac{\ln(1 + 3/x)}{1/x}$, which is $\frac{0}{0}$. Differentiate: $\frac{\frac{1}{1 + 3/x}\cdot\left(-\frac{3}{x^2}\right)}{-\frac{1}{x^2}} = \frac{3}{1 + 3/x} \to 3$. So $y \to e^3 \approx 20.09$.

Check: at $x = 0.1$, (a) gives $0.16658$; (b) at $x = 0.01$ gives $-0.00046$; (c) at $x = 10^6$ gives $20.0854$, and $e^3 = 20.0855$.

</details>

6\. Use Newton's method for $x^3 - 2x - 5 = 0$ starting from $x_0 = 2$. Compute $x_1$, $x_2$ and $x_3$.

<details class="solution" markdown>
<summary>Solution</summary>

$f(x) = x^3 - 2x - 5$ and $f'(x) = 3x^2 - 2$. At $x_0 = 2$: $f = 8 - 4 - 5 = -1$ and $f' = 10$, so $x_1 = 2 + 0.1 = 2.1$. At $x_1 = 2.1$: $f = 9.261 - 4.2 - 5 = 0.061$ and $f' = 11.23$, so $x_2 = 2.1 - 0.005432 = 2.094568$. Then $x_3 = 2.0945515$.

Check: $f(2.0945515) \approx 0$, since $2.0945515^3 = 9.18910\ldots$ and $2 \cdot 2.0945515 + 5 = 9.18910\ldots$. The errors shrink from $0.0054$ to $0.000017$ to $0.0000000002$.

</details>

### Challenge

7\. Newton's method for $f(x) = x^2 - a$, with $a > 0$, is $x_{n+1} = \frac{1}{2}\left(x_n + \frac{a}{x_n}\right)$. Show that $x_{n+1} - \sqrt{a} = \frac{(x_n - \sqrt{a})^2}{2x_n}$, and deduce that for $x_0 > 0$ every later guess is at least $\sqrt{a}$. Apply it to $a = 10$ with $x_0 = 3$.

<details class="solution" markdown>
<summary>Solution</summary>

Subtract $\sqrt{a}$: $x_{n+1} - \sqrt{a} = \frac{x_n^2 + a - 2\sqrt{a}x_n}{2x_n} = \frac{(x_n - \sqrt{a})^2}{2x_n}$, using $a = (\sqrt{a})^2$ to complete the square.

If $x_n > 0$ the right side is not negative, so $x_{n+1} \ge \sqrt{a}$. In particular $x_{n+1} > 0$, so the argument repeats: for every $n \ge 1$, $x_n \ge \sqrt{a}$.

For $a = 10$, $\sqrt{10} = 3.16227766$. With $x_0 = 3$: $x_1 = 3.166667$ (error $0.0044$), $x_2 = 3.162281$ (error $0.0000030$), $x_3 = 3.16227766017$ (error $0.0000000000015$). Each error is about the square of the one before divided by $2\sqrt{10} \approx 6.3$: $\frac{0.0044^2}{6.3} = 0.0000031$.

Check: the guess $x_0 = 3$ is below $\sqrt{10}$, and $x_1$ is above it, as the argument says.

</details>

8\. (Reviews [exponential functions and growth](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md).) A balance of \$1,000 earns 5% a year for 10 years, compounded $n$ times a year, so it becomes $1000\left(1 + \frac{0.05}{n}\right)^{10n}$. (a) Compute it for $n = 1$, $n = 12$ and $n = 365$. (b) Use the limit $\left(1 + \frac{r}{x}\right)^x \to e^r$ to find the value for continuous compounding. (c) How much does continuous compounding add to monthly compounding?

<details class="solution" markdown>
<summary>Solution</summary>

(a) For $n = 1$ the balance is $1000 \cdot 1.05^{10}$, which is \$1,628.89. For $n = 12$ it is $1000\left(1 + \frac{0.05}{12}\right)^{120}$, which is \$1,647.01. For $n = 365$ it is \$1,648.66.

(b) Write $\left(1 + \frac{0.05}{n}\right)^{10n} = \left(1 + \frac{0.5}{10n}\right)^{10n}$, which is $\left(1 + \frac{r}{x}\right)^x$ with $r = 0.5$ and $x = 10n$. As $n \to \infty$ this tends to $e^{0.5}$, so the balance tends to $1000e^{0.5}$, which is \$1,648.72.

(c) The difference is $1648.72 - 1647.01 = 1.71$ dollars, about \$1.71.

Check: the values $1628.89$, $1647.01$, $1648.66$ rise towards $1648.72$ and never pass it.

</details>

## Where this shows up

- The next lesson, [the mean value theorem and extrema](03-mean-value-theorem-and-extrema.md), proves the error bound for linear approximation and the $\frac{0}{0}$ case of L'Hopital's rule. [Optimization](05-optimization.md) mentions Newton's method for finding a critical point, since $f'(x) = 0$ is itself an equation.
- In CS, Newton's method is a standard way to compute square roots and reciprocals, and its multi-variable version is used to solve systems of equations and in optimizers. The comparison $\ln x \ll x^p \ll b^x$ is why logarithmic algorithms beat polynomial ones and polynomial ones beat exponential ones ([asymptotic notation](../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md)). Linear approximation is also the first term of the Taylor series ([power series and Taylor series](../05-sequences-and-series/04-power-series-and-taylor-series.md)).
- In economics and finance, the percent change in a quantity is approximately the change in its logarithm, which is $\ln(1 + x) \approx x$ in disguise (growth rates and CAGR<!-- link: ../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md -->). The change in a bond's price after a small change in its interest rate is estimated with a linearization ([present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md)).
