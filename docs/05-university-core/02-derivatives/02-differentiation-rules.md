# Differentiation rules

After this lesson you can differentiate polynomials, powers, products, quotients, $e^x$, $\sin x$ and $\cos x$ without going back to the limit, prove each rule from the definition, find higher derivatives, and check an answer numerically.

Before this: [the derivative definition](01-the-derivative-definition.md) and [the binomial theorem](../../03-high-school/11-sequences-series-and-counting/04-binomial-theorem.md). The sine and cosine rules also use [trig identities](../../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md) and the limit $\lim_{x \to 0} \frac{\sin x}{x} = 1$ from [limits, intuition and limit laws](../01-limits-and-continuity/01-limits-intuition-and-limit-laws.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Differentiate $f(x) = 4x^3 - 5x + 2$.
2. Differentiate $g(x) = x^2 e^x$.
3. Differentiate $h(x) = \dfrac{\sin x}{x}$.

<details class="solution" markdown>
<summary>Answers</summary>

1. Apply the power rule to each term and drop the constant: $f'(x) = 12x^2 - 5$.
2. Product rule: $g'(x) = 2x \cdot e^x + x^2 \cdot e^x = (x^2 + 2x)e^x$.
3. Quotient rule: $h'(x) = \dfrac{x\cos x - \sin x \cdot 1}{x^2}$.

</details>

## The idea

The last lesson took a page of algebra per function: $x^2$, $\frac{1}{x}$, $\sqrt{x}$. Put the answers side by side and a pattern shows.

| $f(x)$ | $x$ | $x^2$ | $x^3$ | $\dfrac{1}{x} = x^{-1}$ | $\sqrt{x} = x^{1/2}$ |
|---|---|---|---|---|---|
| $f'(x)$ | $1$ | $2x$ | $3x^2$ | $-x^{-2}$ | $\frac{1}{2}x^{-1/2}$ |

Every column is $x^n$ becoming $n x^{n-1}$: the exponent comes down in front and then drops by 1. That is the power rule. Once you trust it, you never need the limit for a power again, the same way you stop adding repeatedly once you know the times tables.

The goal of this lesson is a small toolkit with the same effect on every function you can build from a few pieces. There are rules for building a function from simpler ones, namely sums, constant multiples, products and quotients, and there are a few basic derivatives to start from: powers, $e^x$, $\sin x$ and $\cos x$. Together they cover most of what a first course differentiates. The chain rule in the next lesson adds the last building operation, composition.

Each rule is proved here from the definition, since a university course expects it and since the proofs show why a rule has its shape. The product rule is the one most people get wrong, so it comes with a picture: the area of a rectangle whose two sides are both changing.

## Definitions

The **second derivative** of $f$ is the derivative of the derivative, written $f''(x)$, $\frac{d^2 y}{dx^2}$ or $\frac{d}{dx}\left(\frac{dy}{dx}\right)$. The **third derivative** is $f'''$, and in general the **$n$-th derivative** is $f^{(n)}$, found by differentiating $n$ times. In plain words, the second derivative is the rate of change of the rate of change. For $f(x) = x^3$ we have $f' = 3x^2$, $f'' = 6x$, $f''' = 6$, and $f^{(4)} = 0$.

If $s(t)$ is the position of an object on a line at time $t$, then its **velocity** is $v(t) = s'(t)$ and its **acceleration** is $a(t) = v'(t) = s''(t)$. In plain words, velocity is how fast the position changes and acceleration is how fast the velocity changes. The units are metres per second and metres per second squared.

If $R(q)$ is the revenue from selling $q$ units, then the **marginal revenue** is $R'(q)$: the extra revenue from selling one more unit at output $q$, to a good approximation. In plain words, it is the marginal cost idea from the last lesson, on the income side.

Here are the rules, stated for functions $f$ and $g$ differentiable at $x$ and a constant $c$. Each is proved below.

| Rule | Statement |
|---|---|
| constant | $\dfrac{d}{dx}(c) = 0$ |
| power | $\dfrac{d}{dx}\left(x^n\right) = n x^{n-1}$ |
| constant multiple | $\dfrac{d}{dx}\bigl(c f(x)\bigr) = c f'(x)$ |
| sum and difference | $\dfrac{d}{dx}\bigl(f(x) \pm g(x)\bigr) = f'(x) \pm g'(x)$ |
| product | $\dfrac{d}{dx}\bigl(f(x) g(x)\bigr) = f'(x) g(x) + f(x) g'(x)$ |
| reciprocal | $\dfrac{d}{dx}\left(\dfrac{1}{g(x)}\right) = -\dfrac{g'(x)}{g(x)^2}$ when $g(x) \ne 0$ |
| quotient | $\dfrac{d}{dx}\left(\dfrac{f(x)}{g(x)}\right) = \dfrac{f'(x) g(x) - f(x) g'(x)}{g(x)^2}$ when $g(x) \ne 0$ |
| exponential | $\dfrac{d}{dx}\left(e^x\right) = e^x$ |
| sine and cosine | $\dfrac{d}{dx}(\sin x) = \cos x$ and $\dfrac{d}{dx}(\cos x) = -\sin x$, with $x$ in radians |

In plain words: a constant has no slope; sums and constants pass through the derivative; a product is differentiated one factor at a time; and $e^x$ is its own derivative.

## How to do it

### The simple rules

*Theorem (constant, constant multiple, sum).* For constants $c$ and functions $f$, $g$ differentiable at $x$: $(c)' = 0$, $(cf)' = cf'$ and $(f \pm g)' = f' \pm g'$.

*Proof.* For the constant function, every difference quotient is $\frac{c - c}{h} = 0$, so the limit is 0. For the others, use the limit laws, which say that a limit of a constant multiple or of a sum is the constant multiple or the sum of the limits when those limits exist:

$$
\frac{c f(x + h) - c f(x)}{h} = c \cdot \frac{f(x + h) - f(x)}{h} \to c f'(x),
$$

$$
\frac{\bigl(f(x + h) \pm g(x + h)\bigr) - \bigl(f(x) \pm g(x)\bigr)}{h} = \frac{f(x + h) - f(x)}{h} \pm \frac{g(x + h) - g(x)}{h} \to f'(x) \pm g'(x). \quad \blacksquare
$$

These two rules together say that differentiation is linear: $(af + bg)' = af' + bg'$, so you can differentiate a polynomial one term at a time.

### The power rule

*Theorem (power rule for positive integers).* For every integer $n \ge 1$, $\dfrac{d}{dx}\left(x^n\right) = n x^{n-1}$.

We know the definition of the derivative and the binomial theorem from [the binomial theorem](../../03-high-school/11-sequences-series-and-counting/04-binomial-theorem.md). We want the limit of $\frac{(x + h)^n - x^n}{h}$. The plan is to expand $(x + h)^n$, and notice that after subtracting $x^n$ every term has a factor of $h$.

*Proof.* By the binomial theorem,

$$
(x + h)^n = x^n + n x^{n-1} h + \binom{n}{2} x^{n-2} h^2 + \cdots + h^n = x^n + n x^{n-1} h + h^2 Q(x, h),
$$

where $Q(x, h) = \sum_{k=2}^{n} \binom{n}{k} x^{n-k} h^{k-2}$ is a polynomial in $h$ (an empty sum, which is 0, when $n = 1$). Subtract $x^n$ and divide by $h$:

$$
\frac{(x + h)^n - x^n}{h} = n x^{n-1} + h\,Q(x, h).
$$

As $h \to 0$, the term $h\,Q(x, h)$ tends to 0, because $Q$ is a polynomial in $h$ and so stays bounded near $h = 0$. The limit is $n x^{n-1}$. $\blacksquare$

Look back: the proof says where the rule comes from. Of all the terms of $(x + h)^n$, only the second, $\binom{n}{1} x^{n-1} h$, survives after dividing by $h$, and its coefficient $\binom{n}{1} = n$ is the exponent that comes down. The rule also holds for other exponents. For negative integers it follows from the reciprocal rule below, and the [next lesson](03-chain-rule-implicit-and-inverse-derivatives.md) extends it to every real exponent, so $\frac{d}{dx}\sqrt{x} = \frac{1}{2}x^{-1/2}$ and $\frac{d}{dx}x^{\pi} = \pi x^{\pi - 1}$ are fair to use from now on, for $x > 0$.

### The product rule

*Theorem (product rule).* If $f$ and $g$ are differentiable at $x$, then $fg$ is, and $(fg)' = f'g + fg'$.

The picture comes first. Let $u = f(x)$ and $v = g(x)$ be the sides of a rectangle, so the area is $uv$. Nudge $x$ by a small $h$, which grows $u$ by $\Delta u$ and $v$ by $\Delta v$. The area gains three pieces: a strip $v\,\Delta u$ along one side, a strip $u\,\Delta v$ along the other, and a small corner $\Delta u\,\Delta v$.

![A rectangle of width u and height v, shaded gray. A green strip of width delta u runs down its right side, area v times delta u. A blue strip of height delta v runs along its top, area u times delta v. A small red square at the top right corner has area delta u times delta v.](../../assets/figures/05-university-core/differentiation-rules-product-rectangle.svg)

Divide the gain by $h$. The strips give $v\frac{\Delta u}{h}$ and $u\frac{\Delta v}{h}$, which tend to $v u'$ and $u v'$. The corner gives $\Delta u \cdot \frac{\Delta v}{h}$, which tends to $0 \cdot v' = 0$, because $\Delta u$ shrinks to 0 while $\frac{\Delta v}{h}$ settles to a number. So the corner drops out, and $(uv)' = u'v + uv'$. The proof below says the same in symbols.

We know that $f$ and $g$ are differentiable at $x$, so by [the continuity theorem](01-the-derivative-definition.md#differentiable-implies-continuous) they are continuous at $x$. We want the limit of $\frac{f(x + h)g(x + h) - f(x)g(x)}{h}$. The plan is to add and subtract the term $f(x + h)g(x)$ in the numerator, which splits the change into the two strips of the picture.

*Proof.* Write

$$
\frac{f(x + h)g(x + h) - f(x)g(x)}{h} = f(x + h)\,\frac{g(x + h) - g(x)}{h} + g(x)\,\frac{f(x + h) - f(x)}{h}.
$$

(Expanding the right side, the term $f(x + h)g(x)$ appears once with each sign, so the two sides agree.) Let $h \to 0$. The fraction in the first term tends to $g'(x)$. The factor $f(x + h)$ tends to $f(x)$, because $f$ is continuous at $x$. In the second term, $g(x)$ is a constant and the fraction tends to $f'(x)$. By the limit laws for products and sums the whole expression tends to $f(x)g'(x) + g(x)f'(x)$. $\blacksquare$

Look back: the proof used continuity of $f$ at $x$, which came from the theorem in the last lesson. In words, the rule says "the derivative of the first times the second, plus the first times the derivative of the second". Watch out that $(fg)' \ne f'g'$: with $f = g = x$, the product is $x^2$, whose derivative is $2x$, while $f'g' = 1$.

### The reciprocal and quotient rules

*Theorem (reciprocal rule).* If $g$ is differentiable at $x$ and $g(x) \ne 0$, then $\left(\dfrac{1}{g}\right)' = -\dfrac{g'}{g^2}$ at $x$.

We know $g$ is continuous at $x$ and $g(x) \ne 0$, so $g(x + h) \ne 0$ for small $h$. We want the limit of $\frac{1/g(x + h) - 1/g(x)}{h}$. The plan is to combine the fractions over $g(x)g(x + h)$.

*Proof.* Combining over a common denominator,

$$
\frac{\frac{1}{g(x + h)} - \frac{1}{g(x)}}{h} = \frac{g(x) - g(x + h)}{h\,g(x)g(x + h)} = -\frac{g(x + h) - g(x)}{h} \cdot \frac{1}{g(x)g(x + h)}.
$$

As $h \to 0$ the first fraction tends to $g'(x)$, and $g(x + h) \to g(x)$ by continuity, so the second factor tends to $\frac{1}{g(x)^2}$. The limit is $-\frac{g'(x)}{g(x)^2}$. $\blacksquare$

For a negative integer $-n$, write $x^{-n} = \frac{1}{x^n}$ and use the reciprocal rule with $g = x^n$: the derivative is $-\frac{n x^{n-1}}{x^{2n}} = -n x^{-n-1}$. So the power rule holds for negative integers too. For example, $\frac{d}{dx} x^{-2} = -2x^{-3}$.

*Theorem (quotient rule).* If $f$ and $g$ are differentiable at $x$ and $g(x) \ne 0$, then $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$.

*Proof.* Write $\frac{f}{g} = f \cdot \frac{1}{g}$ and apply the product rule and then the reciprocal rule:

$$
\left(f \cdot \frac{1}{g}\right)' = f' \cdot \frac{1}{g} + f \cdot \left(-\frac{g'}{g^2}\right) = \frac{f'g - fg'}{g^2}. \quad \blacksquare
$$

The memory aid is "low d-high minus high d-low, over low squared", where $g$ is "low" and $f$ is "high". The order in the numerator matters, because swapping it flips the sign.

### The derivative of $e^x$

This is where the definition of $e$ comes in. In [exponential functions and growth](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#the-number-e), $e$ is the limit of $\left(1 + \frac{1}{m}\right)^m$ as $m \to \infty$. We use it in the form for a real variable $t$ that shrinks to 0, where $m = \frac{1}{t}$:

$$
\lim_{t \to 0} (1 + t)^{1/t} = e.
$$

The table below shows it numerically. Proving that the limit exists from both sides is a task for a course in analysis, and this book accepts it, as the exponentials lesson does.

| $t$ | $0.1$ | $0.01$ | $0.001$ | $-0.001$ | $-0.01$ |
|---|---|---|---|---|---|
| $(1 + t)^{1/t}$ | $2.5937$ | $2.7048$ | $2.7169$ | $2.7196$ | $2.7320$ |

*Lemma.* $\displaystyle\lim_{h \to 0} \frac{e^h - 1}{h} = 1$.

We know the limit above, that $\ln$ is continuous with $\ln e = 1$, and the power law of logarithms. We want the limit of $\frac{e^h - 1}{h}$. The plan is to substitute $t = e^h - 1$, which turns the expression into one about $(1 + t)^{1/t}$.

*Proof.* For $h \ne 0$ put $t = e^h - 1$. Then $t \ne 0$, and $t \to 0$ as $h \to 0$, because $e^h$ is continuous and $e^0 = 1$. Since $e^h = 1 + t$, we have $h = \ln(1 + t)$. So

$$
\frac{e^h - 1}{h} = \frac{t}{\ln(1 + t)} = \frac{1}{\frac{1}{t}\ln(1 + t)} = \frac{1}{\ln\left((1 + t)^{1/t}\right)}.
$$

As $t \to 0$, $(1 + t)^{1/t} \to e$, and $\ln$ is continuous at $e$, so the denominator tends to $\ln e = 1$. The quotient tends to 1. $\blacksquare$

*Theorem.* $\dfrac{d}{dx}\left(e^x\right) = e^x$.

*Proof.* By the law of exponents, $e^{x + h} = e^x e^h$, so

$$
\frac{e^{x + h} - e^x}{h} = e^x \cdot \frac{e^h - 1}{h} \to e^x \cdot 1 = e^x,
$$

using the lemma. $\blacksquare$

Look back: the number $e$ is the base for which the slope of $b^x$ at $x = 0$ is exactly 1. The slope of $2^x$ at 0 is about 0.693 and that of $3^x$ is about 1.099, and $e \approx 2.718$ sits between them. The proof shows that every exponential is a constant times itself, $\frac{d}{dx}b^x = b^x \cdot \lim_{h \to 0}\frac{b^h - 1}{h}$, and $e$ makes the constant 1. That is why calculus uses $e$: the function whose rate of change equals its own value is the model for continuous growth. See the differential equation $y' = y$ in [First-order differential equations](../10-differential-equations-light/01-first-order-differential-equations.md).

### The derivatives of $\sin x$ and $\cos x$

The picture first. In the figure, the top panel shows tangent lines to $y = \sin x$ at five points, and the bottom panel plots the slopes of those lines. The slope is 1 at $x = 0$, 0 at the top of the first hump, $-1$ where the curve falls through the axis at $x = \pi$, and so on. The slopes trace out the cosine curve.

![Two stacked graphs over x from 0 to 2 pi. The top shows y = sin x in green with orange tangent lines at x = 0, pi over 2, pi, 3 pi over 2 and 2 pi. The bottom shows y = cos x in blue with orange dots at the same five x-values, labelled slope 1, slope 0, slope minus 1, slope 0 and slope 1, the slopes of the tangent lines above.](../../assets/figures/05-university-core/differentiation-rules-sine-and-slope.svg)

*Lemma.* $\displaystyle\lim_{h \to 0} \frac{\cos h - 1}{h} = 0$.

We know the limit $\lim_{h \to 0} \frac{\sin h}{h} = 1$ from the limits chapter, and that $\sin h \to 0$ and $\cos h \to 1$. We want the limit of $\frac{\cos h - 1}{h}$. The plan is to multiply top and bottom by $\cos h + 1$ and use $\sin^2 h + \cos^2 h = 1$.

*Proof.* For small $h \ne 0$, $\cos h + 1 \ne 0$, and

$$
\frac{\cos h - 1}{h} \cdot \frac{\cos h + 1}{\cos h + 1} = \frac{\cos^2 h - 1}{h(\cos h + 1)} = \frac{-\sin^2 h}{h(\cos h + 1)} = -\frac{\sin h}{h} \cdot \frac{\sin h}{\cos h + 1}.
$$

As $h \to 0$ this tends to $-1 \cdot \frac{0}{2} = 0$. $\blacksquare$

*Theorem.* $\dfrac{d}{dx}(\sin x) = \cos x$ and $\dfrac{d}{dx}(\cos x) = -\sin x$, for $x$ in radians.

*Proof.* The sum formula $\sin(x + h) = \sin x \cos h + \cos x \sin h$ gives

$$
\frac{\sin(x + h) - \sin x}{h} = \sin x \cdot \frac{\cos h - 1}{h} + \cos x \cdot \frac{\sin h}{h} \to \sin x \cdot 0 + \cos x \cdot 1 = \cos x.
$$

Likewise $\cos(x + h) = \cos x \cos h - \sin x \sin h$ gives

$$
\frac{\cos(x + h) - \cos x}{h} = \cos x \cdot \frac{\cos h - 1}{h} - \sin x \cdot \frac{\sin h}{h} \to \cos x \cdot 0 - \sin x \cdot 1 = -\sin x. \quad \blacksquare
$$

Look back: the proof used the radian measure in exactly one place, the limit $\frac{\sin h}{h} \to 1$, which is true only when $h$ is an angle in radians (the arc length on the unit circle). In degrees the limit would be $\frac{\pi}{180}$, and every formula would carry that extra factor. This is why calculus uses radians.

The quotient rule gives the other four trig derivatives. For $\tan x = \frac{\sin x}{\cos x}$:

$$
\frac{d}{dx}\tan x = \frac{\cos x \cdot \cos x - \sin x \cdot (-\sin x)}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x} = \sec^2 x.
$$

The same method gives $\frac{d}{dx}\sec x = \sec x \tan x$, $\frac{d}{dx}\csc x = -\csc x \cot x$ and $\frac{d}{dx}\cot x = -\csc^2 x$ (Practice problem 5 asks for one of them).

### Differentiating an expression

1. Rewrite first. Turn roots and reciprocals into powers ($\sqrt[3]{x} = x^{1/3}$, $\frac{1}{x^2} = x^{-2}$), and split a fraction with a single term below, such as $\frac{x^2 + 3x}{x} = x + 3$.
2. Find the outermost operation: a sum or difference, a constant multiple, a product, or a quotient. A function of a function, such as $\sin(x^2)$, needs the next lesson.
3. Apply the matching rule, and differentiate each piece with the basic derivatives.
4. Simplify: collect terms, and factor out common factors such as $e^x$.
5. Check. At one value of $x$, compare your formula with a central difference (see [In code](#in-code)), or test whether its sign matches the graph.

## Worked examples

<div class="example" markdown>

### Example 1: sums, constants and powers

Differentiate $f(x) = 3x^4 - \dfrac{2}{x^2} + 5\sqrt{x} + 7$.

Step 1: rewrite with powers: $f(x) = 3x^4 - 2x^{-2} + 5x^{1/2} + 7$.

Step 2: the outermost operation is a sum, with constant multiples inside it. Step 3: differentiate term by term. The power rule gives $3 \cdot 4x^3 = 12x^3$, then $-2 \cdot (-2)x^{-3} = 4x^{-3}$, then $5 \cdot \frac{1}{2}x^{-1/2} = \frac{5}{2}x^{-1/2}$, and the constant 7 gives 0.

Step 4: $f'(x) = 12x^3 + 4x^{-3} + \frac{5}{2}x^{-1/2} = 12x^3 + \dfrac{4}{x^3} + \dfrac{5}{2\sqrt{x}}$.

Watch out for the signs and the exponent in the second term: the exponent $-2$ comes down as a factor and multiplies the $-2$ in front, so the sign becomes $+$, and the exponent becomes $-2 - 1 = -3$, not $-1$.

Step 5, the check at $x = 4$: the formula gives $12 \cdot 64 + \frac{4}{64} + \frac{5}{4} = 768 + 0.0625 + 1.25 = 769.3125$. A central difference with $h = 10^{-5}$ gives $769.3125$ as well.

</div>

<div class="example" markdown>

### Example 2: product and quotient

(a) Differentiate $g(x) = x^3 \sin x$. The outermost operation is a product, with $f = x^3$ and $g = \sin x$:

$$
g'(x) = 3x^2 \sin x + x^3 \cos x = x^2(3\sin x + x\cos x).
$$

(b) Differentiate $h(x) = \dfrac{3x + 1}{x^2 + 2}$. The numerator is "high" and the denominator is "low":

$$
h'(x) = \frac{3(x^2 + 2) - (3x + 1)(2x)}{(x^2 + 2)^2} = \frac{3x^2 + 6 - 6x^2 - 2x}{(x^2 + 2)^2} = \frac{-3x^2 - 2x + 6}{(x^2 + 2)^2}.
$$

Check (b) at $x = 1$: the formula gives $\frac{-3 - 2 + 6}{9} = \frac{1}{9} = 0.1111\ldots$, and the difference quotient $\frac{h(1.001) - h(1)}{0.001}$ is about $0.1106$, and the central difference matches $\frac{1}{9}$ to nine places. The sign makes sense too: the function $h$ rises from $h(0) = 0.5$ to a peak near $x = 1.12$, where the numerator $-3x^2 - 2x + 6$ crosses zero.

</div>

<div class="example" markdown>

### Example 3: a tangent that is horizontal

Where does the graph of $f(x) = x\,e^x$ have a horizontal tangent line?

A horizontal tangent has slope 0, so we solve $f'(x) = 0$. The product rule gives $f'(x) = 1 \cdot e^x + x \cdot e^x = e^x(1 + x)$. The factor $e^x$ is never 0, so $f'(x) = 0$ only when $1 + x = 0$, that is, at $x = -1$. The point is $\left(-1, -\frac{1}{e}\right)$, about $(-1, -0.368)$.

Check: $f'(x) < 0$ for $x < -1$ and $f'(x) > 0$ for $x > -1$, so the function falls and then rises, and the point is the lowest point of the graph. As a numerical test, $f(-1.1) = -0.3662$ and $f(-0.9) = -0.3659$ are both above $f(-1) = -0.3679$.

</div>

<div class="example" markdown>

### Example 4: marginal revenue

A seller finds that $q$ units sell at the price $p(q) = 100 - 2q$ dollars each, for $0 \le q \le 50$. Find the marginal revenue at $q = 10$, and compare it with the actual revenue gain from the 11th unit.

The revenue is price times quantity, a product: $R(q) = q\,p(q) = 100q - 2q^2$. By the product rule, $R'(q) = p(q) + q\,p'(q) = (100 - 2q) + q(-2) = 100 - 4q$. At $q = 10$ the marginal revenue is $100 - 40 = 60$ dollars per unit.

The product rule shows what the number means: $p = 80$ is the price of the extra unit, and $q\,p' = 10 \cdot (-2) = -20$ is the loss from the price drop on the 10 units already selling. The extra unit adds 80 and the lower price takes back 20.

Check: $R(10) = 1000 - 200 = 800$ and $R(11) = 1100 - 242 = 858$, so the actual gain is \$58. The derivative \$60 is close but not equal, because the price keeps falling during the extra unit. Also $R'(q) = 0$ at $q = 25$, where the revenue is $R(25) = 1250$, its largest value. Past that point selling more lowers revenue.

</div>

<div class="example" markdown>

### Example 5: velocity and acceleration (finish it yourself)

A particle moves along a line with position $s(t) = t^3 - 6t^2 + 9t$ metres, for $t \ge 0$ seconds. Then $v(t) = s'(t) = 3t^2 - 12t + 9 = 3(t - 1)(t - 3)$ by the sum and power rules.

Now find the acceleration $a(t)$, the times when the particle is at rest, the particle's position and acceleration at those times, and its velocity at $t = 0$ and $t = 2$. Say in words what is happening at each.

<details class="solution" markdown>
<summary>Finish</summary>

The acceleration is $a(t) = v'(t) = 6t - 12$ metres per second squared.

The particle is at rest when $v(t) = 0$, so at $t = 1$ and $t = 3$. At $t = 1$: $s(1) = 1 - 6 + 9 = 4$ and $a(1) = -6$, so it is 4 m from the start, turning around, with the acceleration pointing back. At $t = 3$: $s(3) = 27 - 54 + 27 = 0$ and $a(3) = 6$, so it is back at the start, turning around again.

The velocity at $t = 0$ is $v(0) = 9$ m/s, forward. At $t = 2$ it is $v(2) = 12 - 24 + 9 = -3$ m/s, so it is moving backward between $t = 1$ and $t = 3$.

Check: $v$ is positive before 1, negative between 1 and 3, positive after 3, so $s$ rises from 0 to 4, falls back to 0 and then rises again. That matches $s(0) = 0$, $s(1) = 4$ and $s(3) = 0$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the derivative of a product is not the product of the derivatives. For $x^2 e^x$ the true derivative is $(x^2 + 2x)e^x$, which at $x = 1$ is $3e \approx 8.155$. Multiplying the derivatives gives $2x \cdot e^x = 2e \approx 5.437$ at $x = 1$, and a numerical check catches the difference at once. The same applies to quotients: $\left(\frac{f}{g}\right)' \ne \frac{f'}{g'}$.

</div>

<div class="warning" markdown>

Watch out: the quotient rule has a minus sign and an order. The numerator is $f'g - fg'$, the derivative of the top times the bottom first. Writing $fg' - f'g$ gives the answer with the wrong sign. A fast test is to take $f = 1$: then $\left(\frac{1}{g}\right)' = \frac{-g'}{g^2}$, which has a minus sign and no $f'$ term.

</div>

<div class="warning" markdown>

Watch out: the power rule is for a variable base and a constant exponent. The function $x^2$ is a power and has derivative $2x$. The function $2^x$ is an exponential, with the variable in the exponent, and its derivative is not $x \cdot 2^{x-1}$. In the same way, $\frac{d}{dx}e^x = e^x$, not $x e^{x-1}$. The rule for $b^x$ comes in the next lesson.

</div>

<div class="warning" markdown>

Watch out: a constant has derivative 0 even when it looks like a function. The numbers $\pi^2$, $e^3$ and $\sin 1$ are all constants, so $\frac{d}{dx}\left(\pi^2\right) = 0$, not $2\pi$. In contrast, $x^\pi$ has a variable base, so its derivative is $\pi x^{\pi - 1}$.

</div>

<div class="warning" markdown>

Watch out: $\frac{d}{dx}\cos x = -\sin x$ has a minus sign and $\frac{d}{dx}\sin x = \cos x$ does not. The figure checks the sign: the sine falls between $x = \frac{\pi}{2}$ and $x = \frac{3\pi}{2}$, so its derivative is negative there, and $\cos x$ is negative there. For the cosine, a minus sign in front of $\sin x$ is right because the cosine falls just after $x = 0$, where $\sin x$ is positive. These formulas hold in radians only.

</div>

Differentiate the simplest form of an expression. The function $\frac{x^2 + 3x}{x}$ can be done with the quotient rule, but it equals $x + 3$ for $x \ne 0$, with derivative 1. The two answers agree, and the second route is shorter and has fewer chances for a slip.

Every rule in this lesson assumes that $f$ and $g$ are differentiable at $x$. If one of them isn't, the rule says nothing. For example, $\lvert x \rvert$ has no derivative at 0, so the product rule can't be used on $x\lvert x \rvert$ there. The product is still differentiable at 0, with derivative 0, but you have to use the definition to see it (Practice problem 8 of the last lesson).

## Tricks and shortcuts

Rewrite before differentiating. A quotient with a single term below, such as $\frac{3x^2 - 5x + 1}{x}$, becomes $3x - 5 + x^{-1}$, which is differentiated one term at a time to give $3 - x^{-2}$. A product that can be multiplied out, such as $(x^2 + 1)(x^3 - x) = x^5 - x$, is easier to expand than to differentiate by the product rule, and the two methods are a good check on each other: the product rule gives $2x(x^3 - x) + (x^2 + 1)(3x^2 - 1) = 5x^4 - 1$, and so does $\frac{d}{dx}(x^5 - x)$.

The product rule extends to more factors: differentiate one factor at a time and keep the others. For three factors, $(fgh)' = f'gh + fg'h + fgh'$.

For the trig functions, the derivatives go around a cycle of four: $\sin x \to \cos x \to -\sin x \to -\cos x \to \sin x$. So the fourth derivative of $\sin x$ is $\sin x$ again, and the 100th derivative is $\sin x$, since 100 is a multiple of 4. Also the functions that begin with "co" have the minus sign: $\cos$, $\cot$, $\csc$.

Higher derivatives of a polynomial are easy to read off: $\frac{d^n}{dx^n}x^n = n!$, a constant, and every derivative after that is 0.

| $f(x)$ | $f'$ | $f''$ | $f'''$ | $f^{(4)}$ |
|---|---|---|---|---|
| $x^4$ | $4x^3$ | $12x^2$ | $24x$ | $24$ |
| $\sin x$ | $\cos x$ | $-\sin x$ | $-\cos x$ | $\sin x$ |
| $e^x$ | $e^x$ | $e^x$ | $e^x$ | $e^x$ |

## In code

The best check of a derivative is a numerical one: a central difference at a few points, compared with your formula. If they agree to five or six digits at several points, the formula is almost certainly right. A wrong formula fails at once, as the last check below shows. The step $h = 10^{-5}$ is a good default, for the reasons in the previous lesson.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def central(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def check(f, df, points):
    for a in points:
        print(f"x = {a}: formula {df(a):.6f}, numerical {central(f, a):.6f}")

# Product rule: (x^2 e^x)' = (x^2 + 2x) e^x
check(lambda x: x**2 * math.exp(x), lambda x: (x**2 + 2 * x) * math.exp(x), [0.5, 1, 2])
# x = 0.5: formula 2.060902, numerical 2.060902
# x = 1: formula 8.154845, numerical 8.154845
# x = 2: formula 59.112449, numerical 59.112449

# Quotient rule: (sin x / x)' = (x cos x - sin x) / x^2
check(lambda x: math.sin(x) / x, lambda x: (x * math.cos(x) - math.sin(x)) / x**2, [1, 2, 3])
# x = 1: formula -0.301169, numerical -0.301169
# x = 2: formula -0.435398, numerical -0.435398
# x = 3: formula -0.345677, numerical -0.345677

# A wrong "derivative", the product of the two derivatives, fails the check.
check(lambda x: x**2 * math.exp(x), lambda x: 2 * x * math.exp(x), [1])
# x = 1: formula 5.436564, numerical 8.154845

# Radians matter: the slope of sin at 0 is 1 in radians but pi/180 in degrees.
print(central(math.sin, 0), central(lambda deg: math.sin(math.radians(deg)), 0))
# 0.9999999999833332 0.01745329251994321
```

A computer algebra system differentiates symbolically. The library SymPy returns a formula you can compare with yours, and it is a good way to check your algebra, though the central difference is the check that doesn't depend on the same rules you used.

```python
import sympy as sp

x = sp.symbols("x")
print(sp.diff(x**2 * sp.exp(x), x))   # x**2*exp(x) + 2*x*exp(x)
print(sp.diff(sp.sin(x) / x, x))      # cos(x)/x - sin(x)/x**2
```

</details>

## FAQ

### Why isn't the derivative of a product the product of the derivatives?

Because the pieces of the change don't work that way. In the rectangle picture, the area $uv$ grows by two strips, $v\,\Delta u$ and $u\,\Delta v$, and each strip involves one side's change and the other side's size. The product $u'v'$ would multiply two rates of change, which has the wrong units. If $x$ is time in seconds and $u$ and $v$ are lengths in metres, then $uv$ is in square metres and $(uv)'$ is in square metres per second, while $u'v'$ is in square metres per second squared.

### Why does the power rule work for fractions and negative exponents?

For negative integers it comes from the reciprocal rule, as shown above. For fractions, the case $x^{1/2}$ was done by hand in the last lesson, and every rational exponent follows from the chain rule or implicit differentiation, and every real exponent from logarithmic differentiation, all in the next lesson. The formula $\frac{d}{dx}x^n = nx^{n-1}$ stays the same; only the proof changes.

### Why is $e$ special, when any base gives an exponential function?

All exponential functions $b^x$ have a derivative that is a constant multiple of themselves. For $b = e$ the constant is 1, so the derivative is $e^x$ with no extra factor. For other bases the factor is $\ln b$ (the next lesson shows this), which is about $0.693$ for $b = 2$. Every exponential can be written as $e^{kx}$ for some $k$, so using $e$ puts all of the awkwardness into one number $k$, the continuous growth rate.

### Why does calculus insist on radians?

The derivative of $\sin x$ is $\cos x$ only when $x$ is in radians, because the limit $\frac{\sin h}{h} \to 1$ holds only for radians: a small angle $h$ has a sine almost equal to $h$ exactly when the angle is measured as arc length on the unit circle. In degrees, the derivative of $\sin x^\circ$ is $\frac{\pi}{180}\cos x^\circ$, as the code above shows.

## Practice

### Warm-up

1\. Differentiate: (a) $7x^5 - 3x^2 + 9$, (b) $4\sqrt{x} - \dfrac{6}{x^3} + \pi^2$, (c) $(x^2 + 1)(x^3 - x)$, both by the product rule and by multiplying out first.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Term by term: $35x^4 - 6x$.

(b) Rewrite as $4x^{1/2} - 6x^{-3} + \pi^2$. Then the derivative is $2x^{-1/2} + 18x^{-4} + 0 = \dfrac{2}{\sqrt{x}} + \dfrac{18}{x^4}$. The constant $\pi^2$ goes to 0, and $-6 \cdot (-3) = +18$.

(c) Product rule: $2x(x^3 - x) + (x^2 + 1)(3x^2 - 1) = 2x^4 - 2x^2 + 3x^4 - x^2 + 3x^2 - 1 = 5x^4 - 1$. Multiplying out first: $(x^2 + 1)(x^3 - x) = x^5 - x$, with derivative $5x^4 - 1$.

Check (c) at $x = 1$: both give 4. For (b) at $x = 4$: $\frac{2}{2} + \frac{18}{256} = 1.0703$, and a central difference with $h = 10^{-5}$ gives the same.

</details>

2\. Differentiate: (a) $3\sin x - 2\cos x + e^x$, (b) $\dfrac{e^x}{x}$, (c) $x^2\cos x$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $3\cos x + 2\sin x + e^x$, since the derivative of $-2\cos x$ is $-2 \cdot (-\sin x) = 2\sin x$.

(b) Quotient rule with high $= e^x$ and low $= x$: $\dfrac{e^x \cdot x - e^x \cdot 1}{x^2} = \dfrac{e^x(x - 1)}{x^2}$.

(c) Product rule: $2x\cos x + x^2(-\sin x) = 2x\cos x - x^2\sin x$.

Check: (a) at $x = 0$ gives $3 + 0 + 1 = 4$. (b) at $x = 1$ gives 0, and indeed $\frac{e^x}{x}$ has its lowest point at $x = 1$ (for $x > 0$). (c) at $x = \pi$ gives $-2\pi \approx -6.283$, which agrees with a central difference.

</details>

3\. A particle has position $s(t) = t^2 - 4t + 1$ metres at time $t$ seconds. Find its velocity and acceleration, and when it is at rest.

<details class="solution" markdown>
<summary>Solution</summary>

The velocity is $v(t) = s'(t) = 2t - 4$ m/s, and the acceleration is $a(t) = v'(t) = 2$ m/s$^2$. It is at rest when $2t - 4 = 0$, so at $t = 2$, where $s(2) = 4 - 8 + 1 = -3$.

Check: $s$ is an upward parabola, so it has its lowest point at the rest time $t = 2$, and a constant acceleration of 2 matches its constant curvature.

</details>

### Standard

4\. Find every point on the graph of $y = x^3 - 3x^2 + 2$ where the tangent line is horizontal, and write the equation of the tangent line at each.

<details class="solution" markdown>
<summary>Solution</summary>

$y' = 3x^2 - 6x = 3x(x - 2)$, which is 0 at $x = 0$ and $x = 2$. At $x = 0$ the height is $y = 2$, and at $x = 2$ it is $y = 8 - 12 + 2 = -2$. The horizontal tangent lines are $y = 2$ and $y = -2$.

Check: $y'$ changes from positive to negative at $x = 0$ (a peak) and from negative to positive at $x = 2$ (a valley), so the graph rises, falls and rises again, as a cubic with a positive leading coefficient does.

</details>

5\. (a) Differentiate $f(x) = \dfrac{\sin x}{1 + \cos x}$ and simplify. (b) Use the quotient rule to show that $\dfrac{d}{dx}\cot x = -\csc^2 x$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The quotient rule gives

$$
f'(x) = \frac{\cos x(1 + \cos x) - \sin x(-\sin x)}{(1 + \cos x)^2} = \frac{\cos x + \cos^2 x + \sin^2 x}{(1 + \cos x)^2} = \frac{\cos x + 1}{(1 + \cos x)^2} = \frac{1}{1 + \cos x}.
$$

(b) Write $\cot x = \frac{\cos x}{\sin x}$. Then

$$
\frac{d}{dx}\cot x = \frac{-\sin x \cdot \sin x - \cos x \cdot \cos x}{\sin^2 x} = \frac{-(\sin^2 x + \cos^2 x)}{\sin^2 x} = -\frac{1}{\sin^2 x} = -\csc^2 x.
$$

Check (a) at $x = \frac{\pi}{2}$: the formula gives $\frac{1}{1 + 0} = 1$, and a central difference of $\frac{\sin x}{1 + \cos x}$ at $\frac{\pi}{2}$ is $1.0000$.

</details>

6\. A firm sells $q$ units at the price $p(q) = 200 - 0.5q$ dollars, and its cost is $C(q) = 500 + 20q + 0.1q^2$ dollars. (a) Find the marginal revenue $R'(q)$ and the marginal cost $C'(q)$. (b) The profit is $P = R - C$. Find $P'(q)$ and the output where $P'(q) = 0$. (c) Check that profit at that output beats the profit one unit lower and one unit higher.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $R(q) = q\,p(q) = 200q - 0.5q^2$, so $R'(q) = 200 - q$. Also $C'(q) = 20 + 0.2q$.

(b) By the difference rule, $P'(q) = R'(q) - C'(q) = 200 - q - 20 - 0.2q = 180 - 1.2q$. Setting this to 0 gives $q = 150$: marginal revenue equals marginal cost, $200 - 150 = 50 = 20 + 30$.

(c) $P(q) = R(q) - C(q) = -0.6q^2 + 180q - 500$. Then $P(150) = 13{,}000$, $P(149) = 12{,}999.40$ and $P(151) = 12{,}999.40$. So the profit at 150 units, \$13,000, is the largest of the three.

Check: $R(150) = 30000 - 11250 = 18750$ and $C(150) = 500 + 3000 + 2250 = 5750$, so $P(150) = 13000$. Setting marginal revenue equal to marginal cost is the first step of profit maximization, which [Optimization](../03-applications-of-derivatives/05-optimization.md) develops properly.

</details>

### Challenge

7\. Prove that $\dfrac{d}{dx}x^n = nx^{n-1}$ for every integer $n \ge 1$ using only the product rule, the derivative $\frac{d}{dx}x = 1$ and induction on $n$. (This is a second proof of the power rule.)

<details class="solution" markdown>
<summary>Solution</summary>

Let $S(n)$ be the statement $\frac{d}{dx}x^n = nx^{n-1}$.

Base case: $S(1)$ says $\frac{d}{dx}x = 1 \cdot x^0 = 1$, which is true because the difference quotient of $x$ is $\frac{(x + h) - x}{h} = 1$.

Inductive step: assume $S(n)$ for some $n \ge 1$. Write $x^{n+1} = x \cdot x^n$ and use the product rule:

$$
\frac{d}{dx}\left(x \cdot x^n\right) = 1 \cdot x^n + x \cdot n x^{n-1} = x^n + n x^n = (n + 1)x^n.
$$

This is $S(n + 1)$. By induction, $S(n)$ holds for every integer $n \ge 1$.

Check with $n = 3$: the inductive step from $n = 2$ gives $x^2 + x \cdot 2x = 3x^2$.

</details>

8\. (Reviews [the binomial theorem](../../03-high-school/11-sequences-series-and-counting/04-binomial-theorem.md).) (a) Expand $(x + h)^5$ with the binomial theorem, and find $\frac{d}{dx}x^5$ from the definition. (b) Show that $(fg)'' = f''g + 2f'g' + fg''$. (c) Find the pattern of the coefficients in $(fg)'''$, and test it with $f = g = x^2$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The coefficients in row 5 of Pascal's triangle are $1, 5, 10, 10, 5, 1$, so $(x + h)^5 = x^5 + 5x^4h + 10x^3h^2 + 10x^2h^3 + 5xh^4 + h^5$. Subtracting $x^5$ and dividing by $h$ gives $5x^4 + 10x^3h + 10x^2h^2 + 5xh^3 + h^4$, which tends to $5x^4$ as $h \to 0$.

(b) $(fg)' = f'g + fg'$. Differentiate each term with the product rule: $(f'g)' = f''g + f'g'$ and $(fg')' = f'g' + fg''$. Adding, $(fg)'' = f''g + 2f'g' + fg''$.

(c) The coefficients $1, 2, 1$ are row 2 of Pascal's triangle, so the guess for the next case is row 3: $(fg)''' = f'''g + 3f''g' + 3f'g'' + fg'''$. For $f = g = x^2$: $f = x^2$, $f' = 2x$, $f'' = 2$, $f''' = 0$, so the formula gives $0 + 3 \cdot 2 \cdot 2x + 3 \cdot 2x \cdot 2 + 0 = 24x$. Also $fg = x^4$ has third derivative $24x$.

Check: the same pattern holds for every order (it is called the Leibniz rule), and for $x^2 \cdot x^2$ the check above agrees.

</details>

## Where this shows up

- The next lesson, [chain rule, implicit and inverse derivatives](03-chain-rule-implicit-and-inverse-derivatives.md), adds composition and the derivatives of $\ln x$, $b^x$ and the inverse trig functions. The applications chapter uses these rules to find maxima and minima ([Optimization](../03-applications-of-derivatives/05-optimization.md)).
- In economics, marginal revenue, marginal cost and profit maximization all use the product, sum and power rules (marginal analysis with derivatives<!-- link: ../../07-economics-math/03-firms-and-consumers/01-marginal-analysis-with-derivatives.md -->).
- In CS, automatic differentiation in machine-learning libraries applies exactly these rules mechanically to every operation in a program, which is why a model can report its gradient to floating-point accuracy. The functions $e^x$, $\sin x$ and $\cos x$ solve the equations $y' = y$ and $y'' = -y$, the building blocks of differential equations ([First-order differential equations](../10-differential-equations-light/01-first-order-differential-equations.md)).
