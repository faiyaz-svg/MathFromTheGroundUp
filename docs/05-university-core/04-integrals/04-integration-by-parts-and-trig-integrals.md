# Integration by parts and trig integrals

After this lesson you can integrate a product with integration by parts (including repeated parts and the loop trick), choose which factor to differentiate, integrate powers of sine and cosine with the half-angle identities, and use a trigonometric substitution on $\sqrt{a^2 - x^2}$.

Before this: [u-substitution](03-u-substitution.md), [the fundamental theorem of calculus](02-fundamental-theorem-of-calculus.md), [differentiation rules](../02-derivatives/02-differentiation-rules.md) for the product rule, and [trig identities](../../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md) for the double-angle formulas.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find $\displaystyle\int x\cos x\,dx$. Differentiate your answer to check it.
2. Find $\displaystyle\int \sin^2 x\,dx$ by rewriting $\sin^2 x$ with the double-angle formula $\cos 2x = 1 - 2\sin^2 x$.
3. Evaluate $\displaystyle\int_1^e \ln x\,dx$.

<details class="solution" markdown>
<summary>Answers</summary>

1. Try $x\sin x$: its derivative is $\sin x + x\cos x$, which is $x\cos x$ plus an extra $\sin x$. Subtract an antiderivative of $\sin x$ to cancel it: the answer is $x\sin x + \cos x + C$, and its derivative is $\sin x + x\cos x - \sin x = x\cos x$.
2. Solving the identity for $\sin^2 x$ gives $\sin^2 x = \frac{1 - \cos 2x}{2}$. So the integral is $\frac{x}{2} - \frac{\sin 2x}{4} + C$.
3. Parts with $u = \ln x$ and $dv = dx$ gives $\int \ln x\,dx = x\ln x - x + C$. So $\bigl[x\ln x - x\bigr]_1^e = (e - e) - (0 - 1) = 1$.

</details>

## The idea

Try to find $\int x\,e^x\,dx$. Substitution doesn't help: the inside $x$ has derivative 1, which isn't a factor of the integrand. But guessing does. The function $x\,e^x$ is almost the derivative of $x\,e^x$ itself. By the product rule, $\frac{d}{dx}\left(x\,e^x\right) = e^x + x\,e^x$, which is the integrand plus an extra $e^x$. So subtract an antiderivative of the extra $e^x$:

$$
\int x\,e^x\,dx = x\,e^x - \int e^x\,dx = x\,e^x - e^x + C.
$$

The derivative of $(x - 1)e^x$ is $e^x + (x - 1)e^x = x\,e^x$, so the answer is right. What you did was run the product rule backward. The product rule says that the derivative of a product is the sum of two terms, so if you know an antiderivative of one of the terms, you know one of the other. This is integration by parts, and it turns a hard integral $\int u\,v'\,dx$ into a (hopefully easier) integral $\int u'\,v\,dx$.

The lesson has a second half, about integrals of trig functions. Powers of sine and cosine have no single formula, but they can be done by two moves: if one of the powers is odd, peel off one factor and use substitution, and if both are even, use the double-angle identities from the trig lessons to lower the power. Then, a third idea, trigonometric substitution, uses $x = \sin\theta$ to remove a square root of $1 - x^2$. The area of a quarter of a unit circle, $\frac{\pi}{4}$, comes out of it, which is a check you can do without calculus.

## Definitions

The **integration by parts** formula says that for functions $u$ and $v$ with continuous derivatives on an interval,

$$
\int u\,dv = u\,v - \int v\,du,
$$

where $dv = v'\,dx$ and $du = u'\,dx$. In terms of functions of $x$, this is $\int u(x)\,v'(x)\,dx = u(x)\,v(x) - \int u'(x)\,v(x)\,dx$. For a definite integral, the product $u\,v$ is evaluated at the limits:

$$
\int_a^b u\,v'\,dx = \Bigl[u\,v\Bigr]_a^b - \int_a^b u'\,v\,dx.
$$

In plain words, to integrate a product, choose one factor $u$ to differentiate and the rest $dv$ to integrate, and then the answer is $u\,v$ minus the integral of $v\,du$.

The **LIATE rule** is a heuristic for choosing $u$. Rank the types of function in the order Logarithmic, Inverse trig, Algebraic (powers of $x$ and polynomials), Trig, Exponential, and take $u$ to be the factor of the earliest type. In plain words, differentiate the factor that gets simpler under differentiation (logs and inverse trig functions turn into algebraic functions) and integrate the factor that stays about as hard (exponentials and trig functions go in circles). The rule is a guide and not a theorem, and the examples show when it needs help.

The **tabular method** is a shorthand for repeating integration by parts when $u$ is a polynomial. It is described below.

The **half-angle identities** are

$$
\sin^2 x = \frac{1 - \cos 2x}{2}, \qquad \cos^2 x = \frac{1 + \cos 2x}{2}.
$$

They are the double-angle formulas $\cos 2x = 1 - 2\sin^2 x$ and $\cos 2x = 2\cos^2 x - 1$ solved for the square. In plain words, they trade a squared trig function for a plain cosine of twice the angle, which can be integrated.

A **trigonometric substitution** is a substitution $x = a\sin\theta$, $x = a\tan\theta$ or $x = a\sec\theta$ chosen to turn a square root of a quadratic into a trig function.

## How to do it

### Integration by parts

1. Look at the integrand as a product of two factors. If one factor is a log or an inverse trig function, or if a power of $x$ would disappear after differentiating, that factor is a candidate for $u$. Use LIATE.
2. Put $u$ = the chosen factor and $dv$ = the rest, including $dx$. Compute $du = u'\,dx$ and $v = \int dv$. Use any antiderivative $v$, and leave out the constant.
3. Write $u\,v - \int v\,du$.
4. Check that the new integral $\int v\,du$ is simpler. If it is harder, go back to Step 2 and swap the roles, or try another method.
5. Evaluate the remaining integral, and add $+C$.
6. Check by differentiating, and for a definite integral, don't forget to evaluate the $u\,v$ term at both limits.

*Theorem (integration by parts).* If $u$ and $v$ have continuous derivatives on $[a, b]$, then $\displaystyle\int_a^b u\,v'\,dx = \bigl[u\,v\bigr]_a^b - \int_a^b u'\,v\,dx$.

We know the product rule and the fundamental theorem of calculus. We want to move the derivative from $v$ to $u$ inside an integral. The plan is to integrate the product rule over $[a, b]$ and solve for the integral we want.

*Proof.* By the product rule, $(u\,v)' = u'\,v + u\,v'$. All three functions are continuous, so we can integrate both sides over $[a, b]$:

$$
\int_a^b (u\,v)'\,dx = \int_a^b u'\,v\,dx + \int_a^b u\,v'\,dx.
$$

By part 2 of the fundamental theorem, the left side is $\bigl[u\,v\bigr]_a^b$. Solving for the last integral gives the formula. $\blacksquare$

Look back: the formula is the product rule rearranged, and nothing else. The indefinite version is the same argument without limits. The proof also shows what to look for: parts helps when $\int u'\,v\,dx$ is easier than $\int u\,v'\,dx$. It moves the difficulty from one integral to another, and it only pays when the new one is easier.

Which factor should be $u$? For $\int x\ln x\,dx$ try both. With $u = \ln x$ and $dv = x\,dx$: $du = \frac{dx}{x}$ and $v = \frac{x^2}{2}$, so the new integral is $\int \frac{x^2}{2}\cdot\frac{1}{x}\,dx = \int \frac{x}{2}\,dx$, which is easy. With $u = x$ and $dv = \ln x\,dx$ you would need $v = x\ln x - x$ first, which already uses parts, and the new integral $\int \bigl(x\ln x - x\bigr)\,dx$ is harder than the one you started with. LIATE picks the first choice because the logarithm comes first in the list.

### Repeated parts, the loop trick and the tabular method

If $u$ is a power of $x$ times something simple, parts lowers the power by 1 each time, so apply it repeatedly. For $\int x^2e^x\,dx$:

$$
\int x^2 e^x\,dx = x^2 e^x - 2\int x\,e^x\,dx = x^2 e^x - 2\left(x\,e^x - e^x\right) + C = \left(x^2 - 2x + 2\right)e^x + C.
$$

The tabular method does this bookkeeping in a table. Put $u$ and its successive derivatives in the first column until you reach 0, put $dv$ and its successive antiderivatives in the second column, and then multiply along the diagonals with alternating signs, starting with plus.

| Sign | Derivatives of $x^2$ | Antiderivatives of $e^x$ |
|---|---|---|
| $+$ | $x^2$ | $e^x$ |
| $-$ | $2x$ | $e^x$ |
| $+$ | $2$ | $e^x$ |
| $-$ | $0$ | $e^x$ |

The answer is the sum of products along the diagonals: $x^2 e^x - 2x\,e^x + 2e^x$. Each diagonal is one application of parts, and the zero in the last row means the leftover integral is $\int 0\,dx = 0$. The method works when one factor is a polynomial and the other can be integrated again and again ($e^{ax}$, $\sin ax$, $\cos ax$).

Some integrals come back to themselves. For $I = \int e^x\sin x\,dx$, parts with $u = \sin x$ and $dv = e^x\,dx$ gives $I = e^x\sin x - \int e^x\cos x\,dx$. Apply parts again to the new integral, with $u = \cos x$ and $dv = e^x\,dx$:

$$
\int e^x\cos x\,dx = e^x\cos x + \int e^x\sin x\,dx = e^x\cos x + I.
$$

Substituting back, $I = e^x\sin x - e^x\cos x - I$. This is an equation for $I$, and it has no integral left on the right except $I$ itself. Move $I$ to the left and divide by 2:

$$
I = \int e^x\sin x\,dx = \frac{e^x(\sin x - \cos x)}{2} + C.
$$

The trick requires keeping the same choice of $u$ (a trig function both times, or an exponential both times). If you swap roles in the second step, the two applications cancel and you get $I = I$, which tells you nothing. The constant $C$ is added at the end, since the equation $I = \ldots - I$ is between specific antiderivatives.

### Powers of sine and cosine

To integrate $\sin^m x\cos^n x$:

1. If $n$ is odd, peel off one $\cos x$ and write the remaining even power of cosine in terms of sine, using $\cos^2 x = 1 - \sin^2 x$. Then substitute $u = \sin x$, so that $du = \cos x\,dx$.
2. If $m$ is odd, peel off one $\sin x$, write the even power of sine as $1 - \cos^2 x$, and substitute $u = \cos x$, so that $du = -\sin x\,dx$.
3. If both are even, use the half-angle identities to lower the powers. A product $\sin^2 x\cos^2 x$ is easier with $\sin x\cos x = \frac{1}{2}\sin 2x$ first.

The two basic cases are

$$
\int \sin^2 x\,dx = \frac{x}{2} - \frac{\sin 2x}{4} + C, \qquad \int \cos^2 x\,dx = \frac{x}{2} + \frac{\sin 2x}{4} + C.
$$

Over a whole period the oscillating term returns to 0, so $\int_0^{2\pi}\sin^2 x\,dx = \pi$, and the average value of $\sin^2 x$ over a period is $\frac{\pi}{2\pi} = \frac{1}{2}$. That is the reason that $\sin^2 x$ and $\cos^2 x$ are each "half" in average, a fact used in alternating current and in Fourier analysis.

### Trigonometric substitution

When the integrand contains $\sqrt{a^2 - x^2}$, put $x = a\sin\theta$ with $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$. Then $dx = a\cos\theta\,d\theta$ and

$$
\sqrt{a^2 - x^2} = \sqrt{a^2 - a^2\sin^2\theta} = a\sqrt{\cos^2\theta} = a\cos\theta,
$$

where the absolute value $\lvert\cos\theta\rvert$ equals $\cos\theta$ because $\cos\theta \ge 0$ on that range of $\theta$. The two other standard cases follow the same pattern.

| The integrand contains | Substitution | The root becomes | Identity used |
|---|---|---|---|
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$ | $a\cos\theta$ | $1 - \sin^2\theta = \cos^2\theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a\tan\theta$ | $a\sec\theta$ | $1 + \tan^2\theta = \sec^2\theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a\sec\theta$ | $a\tan\theta$ | $\sec^2\theta - 1 = \tan^2\theta$ |

This lesson uses only the first one. It is the substitution rule with $g(\theta) = a\sin\theta$ and the roles of $x$ and $u$ exchanged, so the same rule applies: the limits change with the substitution, and the final answer is turned back to $x$ using a right triangle or the inverse trig function.

## Worked examples

<div class="example" markdown>

### Example 1: a polynomial times an exponential

Find $\int x\,e^x\,dx$ and then $\int_0^1 x\,e^x\,dx$.

Step 1: the integrand is a product of $x$ (algebraic) and $e^x$ (exponential). LIATE puts the algebraic factor first, and differentiating $x$ gives 1, which is simpler.

Step 2: $u = x$ and $dv = e^x\,dx$. Then $du = dx$ and $v = e^x$.

Step 3: $\int x\,e^x\,dx = x\,e^x - \int e^x\,dx$.

Step 4: the new integral $\int e^x\,dx$ is simpler, as hoped.

Step 5: $= x\,e^x - e^x + C = (x - 1)e^x + C$.

Step 6, the check: $\frac{d}{dx}\bigl[(x - 1)e^x\bigr] = e^x + (x - 1)e^x = x\,e^x$. For the definite integral, $\bigl[(x - 1)e^x\bigr]_0^1 = 0 - (-1) = 1$, and a trapezoid sum of $x\,e^x$ on $[0, 1]$ is $1.0000$. Watch out for the sign when evaluating at 0: $(0 - 1)e^0 = -1$, and subtracting it adds 1.

</div>

<div class="example" markdown>

### Example 2: logarithms and inverse trig functions

Find $\int \ln x\,dx$ and $\int \arctan x\,dx$.

There is only one visible factor in each, but the integrand can be written as $\ln x \cdot 1$ and $\arctan x \cdot 1$. LIATE puts the log and the inverse trig function first, so each is $u$, and $dv = dx$. For the logarithm, $du = \frac{dx}{x}$ and $v = x$:

$$
\int \ln x\,dx = x\ln x - \int x\cdot\frac{1}{x}\,dx = x\ln x - x + C.
$$

For the arctangent, $du = \frac{dx}{1 + x^2}$ and $v = x$:

$$
\int \arctan x\,dx = x\arctan x - \int \frac{x}{1 + x^2}\,dx.
$$

The last integral is a substitution: with $w = 1 + x^2$, $x\,dx = \frac{1}{2}\,dw$ and $\int \frac{x}{1 + x^2}\,dx = \frac{1}{2}\ln\left(1 + x^2\right)$. So $\int \arctan x\,dx = x\arctan x - \frac{1}{2}\ln\left(1 + x^2\right) + C$.

Check: the derivative of $x\ln x - x$ is $\ln x + 1 - 1 = \ln x$. The derivative of $x\arctan x - \frac{1}{2}\ln\left(1 + x^2\right)$ is $\arctan x + \frac{x}{1 + x^2} - \frac{x}{1 + x^2} = \arctan x$. Also $\int_0^1\arctan x\,dx = \frac{\pi}{4} - \frac{\ln 2}{2} \approx 0.4388$, and the area under a curve that rises from 0 to $\frac{\pi}{4} = 0.785$ over a width of 1, bending down, is plausibly a bit over half of $0.785$.

</div>

<div class="example" markdown>

### Example 3: repeated parts and the tabular method

Find $\int x^2\sin x\,dx$.

The factor $x^2$ is algebraic and goes first. Use the table, with derivatives of $x^2$ on the left and antiderivatives of $\sin x$ on the right.

| Sign | Derivatives of $x^2$ | Antiderivatives of $\sin x$ |
|---|---|---|
| $+$ | $x^2$ | $-\cos x$ |
| $-$ | $2x$ | $-\sin x$ |
| $+$ | $2$ | $\cos x$ |
| $-$ | $0$ | $\sin x$ |

The diagonal products with signs are $+x^2(-\cos x) - 2x(-\sin x) + 2\cos x$, so

$$
\int x^2\sin x\,dx = -x^2\cos x + 2x\sin x + 2\cos x + C.
$$

Check: differentiating, $-2x\cos x + x^2\sin x + 2\sin x + 2x\cos x - 2\sin x = x^2\sin x$.

</div>

<div class="example" markdown>

### Example 4: the loop

Evaluate $\int_0^{\pi} e^x\sin x\,dx$.

From the section above, an antiderivative is $\frac{e^x(\sin x - \cos x)}{2}$. Then

$$
\int_0^{\pi}e^x\sin x\,dx = \left[\frac{e^x(\sin x - \cos x)}{2}\right]_0^{\pi} = \frac{e^{\pi}(0 + 1)}{2} - \frac{1\cdot(0 - 1)}{2} = \frac{e^{\pi} + 1}{2} \approx 12.0703.
$$

Check: $e^\pi = 23.14$, so the answer is $12.07$. The integrand rises with $e^x$ and is mostly large where $\sin x$ is large (it peaks near $x = 2.36$ at about $e^{2.36}\cdot 0.7 = 7.4$), so an area of about 12 over a width of $\pi$ is plausible. A midpoint sum with 100,000 rectangles gives $12.0703$.

</div>

<div class="example" markdown>

### Example 5: powers of sine and cosine

Find $\int \sin^3 x\,dx$, $\int_0^{\pi}\sin^2 x\,dx$ and $\int \sin^2 x\cos^2 x\,dx$.

The first has an odd power of sine. Peel off one $\sin x$ and write $\sin^2 x = 1 - \cos^2 x$: $\int \bigl(1 - \cos^2 x\bigr)\sin x\,dx$. Let $u = \cos x$, so $du = -\sin x\,dx$ and the integral is $-\int \bigl(1 - u^2\bigr)\,du = -u + \frac{u^3}{3} + C = -\cos x + \frac{\cos^3 x}{3} + C$.

The second has an even power, so use the half-angle identity: $\int_0^{\pi}\frac{1 - \cos 2x}{2}\,dx = \left[\frac{x}{2} - \frac{\sin 2x}{4}\right]_0^{\pi} = \frac{\pi}{2}$.

The third has both powers even. Use $\sin x\cos x = \frac{\sin 2x}{2}$, so $\sin^2 x\cos^2 x = \frac{\sin^2 2x}{4} = \frac{1 - \cos 4x}{8}$. Then $\int \frac{1 - \cos 4x}{8}\,dx = \frac{x}{8} - \frac{\sin 4x}{32} + C$.

Check: the derivative of the first answer is $\sin x - \cos^2 x\sin x = \sin x\left(1 - \cos^2 x\right) = \sin^3 x$. The second is the area under $\sin^2$ over half a period, and since $\sin^2$ averages $\frac{1}{2}$ over $[0, \pi]$, the area is $\frac{\pi}{2} = 1.5708$. The derivative of the third is $\frac{1}{8} - \frac{\cos 4x}{8} = \sin^2 x\cos^2 x$.

</div>

<div class="example" markdown>

### Example 6: a quarter circle from a trig substitution

Evaluate $\int_0^1\sqrt{1 - x^2}\,dx$ and compare with geometry.

The graph of $y = \sqrt{1 - x^2}$ is the upper half of the unit circle, so the region under it from 0 to 1 is a quarter of the unit disc, with area $\frac{1}{4}\pi\cdot 1^2 = \frac{\pi}{4}$. Now do it with calculus. Let $x = \sin\theta$, so $dx = \cos\theta\,d\theta$ and $\sqrt{1 - x^2} = \cos\theta$ (with $\theta$ the angle from the vertical axis, as in the figure). The limits become $\theta = 0$ at $x = 0$ and $\theta = \frac{\pi}{2}$ at $x = 1$. Then

$$
\int_0^1\sqrt{1 - x^2}\,dx = \int_0^{\pi/2}\cos^2\theta\,d\theta = \int_0^{\pi/2}\frac{1 + \cos 2\theta}{2}\,d\theta = \left[\frac{\theta}{2} + \frac{\sin 2\theta}{4}\right]_0^{\pi/2} = \frac{\pi}{4}.
$$

![The quarter of the unit disc under the graph of y equals the square root of 1 minus x squared, from x = 0 to x = 1, shaded green. A radius from the origin to a point on the arc makes an angle theta with the vertical axis. The horizontal coordinate of the point is sine theta, equal to x, and the vertical coordinate is cosine theta, equal to the height of the curve. The area is pi over 4.](../../assets/figures/05-university-core/integration-by-parts-and-trig-integrals-quarter.svg)

The two answers agree, which is a check on the substitution. Going back to $x$ for the indefinite integral: $\theta = \arcsin x$ and $\sin\theta\cos\theta = x\sqrt{1 - x^2}$, so $\int\sqrt{1 - x^2}\,dx = \frac{1}{2}\arcsin x + \frac{1}{2}x\sqrt{1 - x^2} + C$. Differentiating gives $\frac{1}{2\sqrt{1 - x^2}} + \frac{1}{2}\sqrt{1 - x^2} - \frac{x^2}{2\sqrt{1 - x^2}} = \frac{1 + \left(1 - x^2\right) - x^2}{2\sqrt{1 - x^2}} = \sqrt{1 - x^2}$.

The same substitution with $x = a\sin\theta$ gives the area of a disc of radius $a$: $4\int_0^a\sqrt{a^2 - x^2}\,dx = \pi a^2$, as it should.

</div>

<div class="example" markdown>

### Example 7: choosing the right method (finish it yourself)

Evaluate $\int_0^{\pi}x\sin x\,dx$. By LIATE, $x$ is the algebraic factor and $\sin x$ is the trig factor, so take $u = x$ and $dv = \sin x\,dx$. Write down $du$ and $v$, apply the formula for a definite integral, evaluate the boundary term, finish the integral and check.

<details class="solution" markdown>
<summary>Finish</summary>

With $du = dx$ and $v = -\cos x$:

$$
\int_0^{\pi}x\sin x\,dx = \Bigl[-x\cos x\Bigr]_0^{\pi} + \int_0^{\pi}\cos x\,dx = \bigl(-\pi\cos\pi + 0\bigr) + \bigl[\sin x\bigr]_0^{\pi} = \pi + 0 = \pi.
$$

Check: the antiderivative is $-x\cos x + \sin x$, whose derivative is $-\cos x + x\sin x + \cos x = x\sin x$. The integrand is $x\sin x$, an arch of height about 1.8 near $x = 2$ over a width of $\pi$, and an area of $\pi = 3.14$ is plausible: the arch is about as large as a triangle with base $\pi$ and height 2.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the choice of $u$ can make the integral harder. For $\int x\,e^{x^2}\,dx$, parts with $u = x$ and $dv = e^{x^2}\,dx$ needs $v = \int e^{x^2}\,dx$, which has no elementary form. Substitution is the right method there. Before using parts, check whether a substitution already works, and use parts when $dv$ can be integrated in closed form.

</div>

<div class="warning" markdown>

Watch out: the minus sign and the $u\,v$ term. The formula is $u\,v - \int v\,du$, not $u\,v + \int v\,du$, and not $\int u\,dv = u\,v$. In Example 1, writing $x\,e^x + \int e^x\,dx = x\,e^x + e^x$ gives a function whose derivative is $x\,e^x + 2e^x$. A fast check is to differentiate. For definite integrals, the boundary term $\bigl[u\,v\bigr]_a^b$ is easy to forget.

</div>

<div class="warning" markdown>

Watch out: in the loop trick, keep the same type of function as $u$ both times. If $u = \sin x$ in the first step and $u = e^x$ in the second, the second step undoes the first and the equation says $I = I$. And don't divide by 2 before moving $I$ across: $I = F - I$ gives $2I = F$, so $I = \frac{F}{2}$.

</div>

<div class="warning" markdown>

Watch out: $\int \sin^2 x\,dx$ is not $\frac{\sin^3 x}{3}$. That would be right if $\cos x$ were also in the integrand (a substitution), but it isn't. The check is to differentiate: $\frac{d}{dx}\frac{\sin^3 x}{3} = \sin^2 x\cos x$, which has an extra factor. For $\sin^2 x$ alone, use the half-angle identity.

</div>

In a trig substitution, the step $\sqrt{\cos^2\theta} = \cos\theta$ uses a range for $\theta$ on which cosine is not negative. With $x = \sin\theta$ for $-1 \le x \le 1$ the angle $\theta = \arcsin x$ lies in $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, so it is fine. If you choose another range, the root becomes $\lvert\cos\theta\rvert$, and the sign matters.

Parts needs both factors to have continuous derivatives on the interval. For $\int_0^1\ln x\,dx$, the function $\ln x$ is not defined at 0 and the integral is improper (it converges to $-1$, by [partial fractions and improper integrals](05-partial-fractions-and-improper-integrals.md)). Always check the interval before evaluating a boundary term like $x\ln x$ at 0.

## Tricks and shortcuts

Use the tabular method whenever one factor is a polynomial and the other is $e^{ax}$, $\sin ax$ or $\cos ax$, since you never need to decide a step at a time. For $\int x^3 e^{2x}\,dx$, the table has four rows, and the answer comes out as $e^{2x}\left(\frac{x^3}{2} - \frac{3x^2}{4} + \frac{3x}{4} - \frac{3}{8}\right) + C$. A polynomial of degree $n$ needs $n + 1$ rows.

Check by differentiating, always. A parts answer is a product, so the derivative uses the product rule, and the terms should cancel in pairs to leave the original integrand. When they don't, the sign is usually wrong.

Learn $\int \ln x\,dx = x\ln x - x + C$ and $\int \arctan x\,dx$ as results. Both come from parts with $dv = dx$, and the trick generalises: if an integrand is a function whose derivative is simpler (a log, an inverse trig function), write it as the function times 1 and use parts.

For odd powers, the peel-off trick turns every $\sin^{2k+1}x$ into a polynomial in $\cos x$ times $\sin x$. For $\int\sin^5 x\,dx$, the integrand is $\bigl(1 - \cos^2 x\bigr)^2\sin x$, and with $u = \cos x$ the answer is $-\cos x + \frac{2}{3}\cos^3 x - \frac{1}{5}\cos^5 x + C$.

## In code

The loop trick and the trig substitution can both be checked by comparing closed forms with a midpoint sum. The last part shows something about numerical rules: the midpoint error for $\int_0^1\sqrt{1 - x^2}\,dx = \frac{\pi}{4}$ falls like $n^{-3/2}$, much slower than the $n^{-2}$ for smooth functions, because the graph has a vertical tangent at $x = 1$.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def midpoint(f, a, b, n=100000):
    dx = (b - a) / n
    return dx * sum(f(a + (k + 0.5) * dx) for k in range(n))

# The loop trick: the integral of e^x sin x from 0 to pi.
print(round(midpoint(lambda x: math.exp(x) * math.sin(x), 0, math.pi), 4),
      round((math.exp(math.pi) + 1) / 2, 4))
# 12.0703 12.0703

# Integration by parts: the integral of x sin x from 0 to pi is pi.
print(round(midpoint(lambda x: x * math.sin(x), 0, math.pi), 4), round(math.pi, 4))
# 3.1416 3.1416

# A quarter of the unit disc, and how the error shrinks with n.
for n in (100, 10000, 1000000):
    err = abs(midpoint(lambda x: math.sqrt(1 - x * x), 0, 1, n) - math.pi / 4)
    print(n, f"{err:.2e}")
# 100 8.61e-05
# 10000 8.61e-08
# 1000000 8.61e-11
```

</details>

Multiplying $n$ by 100 divides the error by 1000, which is $100^{3/2}$, and not by 10,000, which is what a smooth function would give. A change of variables like $x = \sin\theta$ before summing would remove the problem.

## FAQ

### How do I know when to use parts and not substitution?

Substitution works when the integrand has the form $f(g(x))\,g'(x)$: a function and the derivative of its inside. Parts works when the integrand is a product of two unrelated pieces, such as $x\,e^x$ or $x\sin x$, where neither piece is the derivative of the other's inside. Try substitution first because it is quicker, and use parts when it leaves an $x$ behind. Many integrals need both, as $\int\arctan x\,dx$ does.

### Why does LIATE work?

It ranks functions by how much they simplify under differentiation, against how much they change under integration. A logarithm or inverse trig function is hard to integrate, but its derivative is algebraic, so it should be $u$. A polynomial gets simpler when differentiated. An exponential or a sine or cosine is as easy to integrate as to differentiate, so it makes a good $dv$. It is only a heuristic. For $\int x^2\ln x\,dx$ it works, and for $\int e^x\sin x\,dx$ it picks $u = \sin x$, though $u = e^x$ works just as well.

### Why don't I need $+C$ when I find $v$?

Because any constant in $v$ drops out. If you use $v + c$ in place of $v$, the formula gives $u(v + c) - \int(v + c)\,du = u\,v + c\,u - \int v\,du - c\,u$, and the $c\,u$ terms cancel. Choose the simplest $v$.

### Why do the half-angle identities give $\frac{1}{2}$ on average?

Because $\sin^2 x + \cos^2 x = 1$ and the two curves are shifted copies of each other, so over a full period each takes half of the total. The integral shows it: $\int_0^{2\pi}\sin^2 x\,dx = \int_0^{2\pi}\frac{1 - \cos 2x}{2}\,dx = \pi$, because $\cos 2x$ spends as much time positive as negative and integrates to 0 over a period. The average is $\pi$ divided by the length $2\pi$.

## Practice

### Warm-up

1\. Find (a) $\int x\cos x\,dx$, (b) $\int x\,e^{2x}\,dx$ and (c) $\int x\ln x\,dx$ for $x > 0$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $u = x$, $dv = \cos x\,dx$, so $du = dx$ and $v = \sin x$: $x\sin x - \int\sin x\,dx = x\sin x + \cos x + C$.

(b) $u = x$, $dv = e^{2x}\,dx$, so $v = \frac{e^{2x}}{2}$: $\frac{x\,e^{2x}}{2} - \int\frac{e^{2x}}{2}\,dx = \frac{x\,e^{2x}}{2} - \frac{e^{2x}}{4} + C = \left(\frac{x}{2} - \frac{1}{4}\right)e^{2x} + C$.

(c) $u = \ln x$, $dv = x\,dx$, so $du = \frac{dx}{x}$ and $v = \frac{x^2}{2}$: $\frac{x^2}{2}\ln x - \int\frac{x}{2}\,dx = \frac{x^2}{2}\ln x - \frac{x^2}{4} + C$.

Check by differentiating: (a) $\sin x + x\cos x - \sin x = x\cos x$. (b) $\frac{e^{2x}}{2} + x\,e^{2x} - \frac{e^{2x}}{2} = x\,e^{2x}$. (c) $x\ln x + \frac{x}{2} - \frac{x}{2} = x\ln x$.

</details>

2\. Evaluate (a) $\int_0^{\pi/2}\cos^3 x\,dx$ and (b) $\int\cos^2(3x)\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Peel off one $\cos x$: $\int\bigl(1 - \sin^2 x\bigr)\cos x\,dx$, and $u = \sin x$ gives $\int_0^1\bigl(1 - u^2\bigr)\,du = 1 - \frac{1}{3} = \frac{2}{3}$, with the limits changing to $u = 0$ and $u = 1$.

(b) Use the half-angle identity with $2x$ replaced by $6x$: $\cos^2(3x) = \frac{1 + \cos 6x}{2}$. The integral is $\frac{x}{2} + \frac{\sin 6x}{12} + C$.

Check: (a) the integrand starts at 1, ends at 0, and falls; a value of $\frac{2}{3}$ over a width of $\frac{\pi}{2} = 1.57$ is plausible (it is below $\int_0^{\pi/2}\cos x\,dx = 1$, as it should be, since $\cos^3 x \le \cos x$). For (b), the derivative is $\frac{1}{2} + \frac{\cos 6x}{2} = \cos^2(3x)$.

</details>

3\. For each integral, say which factor LIATE chooses as $u$ and which method you would try first: (a) $\int x^2\sin x\,dx$, (b) $\int\arcsin x\,dx$, (c) $\int x\,e^{x^2}\,dx$, (d) $\int x^5\ln x\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $u = x^2$ (algebraic before trig), and repeated parts, or the tabular method.

(b) $u = \arcsin x$ (inverse trig) and $dv = dx$, then a substitution for $\int\frac{x}{\sqrt{1 - x^2}}\,dx$.

(c) Here substitution is better: $w = x^2$ and $x\,dx = \frac{1}{2}\,dw$. Parts would want $\int e^{x^2}\,dx$, which has no elementary form.

(d) $u = \ln x$ (logarithm first) and $dv = x^5\,dx$, so the answer is $\frac{x^6}{6}\ln x - \frac{x^6}{36} + C$.

Check (d): the derivative is $x^5\ln x + \frac{x^5}{6} - \frac{x^5}{6} = x^5\ln x$.

</details>

### Standard

4\. Find $\int x^2\sin x\,dx$ by repeated parts (not the table) and compare with the answer in Example 3.

<details class="solution" markdown>
<summary>Solution</summary>

First pass: $u = x^2$, $dv = \sin x\,dx$, so $du = 2x\,dx$ and $v = -\cos x$:

$$
\int x^2\sin x\,dx = -x^2\cos x + 2\int x\cos x\,dx.
$$

Second pass on $\int x\cos x\,dx$: $u = x$, $dv = \cos x\,dx$, so this is $x\sin x + \cos x$ (Problem 1a). Then $\int x^2\sin x\,dx = -x^2\cos x + 2x\sin x + 2\cos x + C$, the same as the table gave.

Check: at $x = \pi$ the antiderivative is $\pi^2 - 2 = 7.87$ and at 0 it is 2, so $\int_0^\pi x^2\sin x\,dx = \pi^2 - 4 = 5.87$, and a midpoint sum gives $5.8696$.

</details>

5\. Evaluate $\int_0^1\arctan x\,dx$ and give a decimal.

<details class="solution" markdown>
<summary>Solution</summary>

By Example 2, an antiderivative is $x\arctan x - \frac{1}{2}\ln\left(1 + x^2\right)$. At $x = 1$: $\frac{\pi}{4} - \frac{1}{2}\ln 2$. At $x = 0$: 0. So the integral is $\frac{\pi}{4} - \frac{\ln 2}{2} \approx 0.7854 - 0.3466 = 0.4388$.

Check: a midpoint sum with 100,000 rectangles gives $0.438825$.

</details>

6\. (Reviews [differentiation rules](../02-derivatives/02-differentiation-rules.md).) Find constants $A$ and $B$ so that $\frac{d}{dx}\bigl[(Ax + B)e^{2x}\bigr] = x\,e^{2x}$. Compare the result with Problem 1b.

<details class="solution" markdown>
<summary>Solution</summary>

By the product rule, $\frac{d}{dx}\bigl[(Ax + B)e^{2x}\bigr] = A\,e^{2x} + 2(Ax + B)e^{2x} = (2Ax + A + 2B)e^{2x}$. We need this to equal $x\,e^{2x}$, so $2A = 1$ and $A + 2B = 0$. Then $A = \frac{1}{2}$ and $B = -\frac{1}{4}$.

This is the antiderivative $\left(\frac{x}{2} - \frac{1}{4}\right)e^{2x}$ found by parts in Problem 1b. Parts is the same product rule, organised so that you don't need to guess.

Check: at $x = 1$ the derivative is $\left(1 + \frac{1}{2} - \frac{1}{2}\right)e^2 = e^2$, which equals $1\cdot e^2$.

</details>

### Challenge

7\. Let $I_n = \int_0^{\pi/2}\sin^n x\,dx$. Use parts to show that $I_n = \frac{n - 1}{n}I_{n-2}$ for $n \ge 2$, and find $I_6$.

<details class="solution" markdown>
<summary>Solution</summary>

Write $\sin^n x = \sin^{n-1}x\cdot\sin x$ and take $u = \sin^{n-1}x$, $dv = \sin x\,dx$, so $du = (n - 1)\sin^{n-2}x\cos x\,dx$ and $v = -\cos x$. Then

$$
I_n = \bigl[-\sin^{n-1}x\cos x\bigr]_0^{\pi/2} + (n - 1)\int_0^{\pi/2}\sin^{n-2}x\cos^2 x\,dx.
$$

The boundary term is 0 at both ends (for $n \ge 2$, $\sin 0 = 0$ at the lower limit and $\cos\frac{\pi}{2} = 0$ at the upper). Use $\cos^2 x = 1 - \sin^2 x$ in the last integral: it becomes $I_{n-2} - I_n$. So $I_n = (n - 1)(I_{n-2} - I_n)$, which gives $n\,I_n = (n - 1)I_{n-2}$, as claimed.

Start from $I_0 = \frac{\pi}{2}$. Then $I_2 = \frac{1}{2}\cdot\frac{\pi}{2} = \frac{\pi}{4}$, $I_4 = \frac{3}{4}\cdot\frac{\pi}{4} = \frac{3\pi}{16}$, and $I_6 = \frac{5}{6}\cdot\frac{3\pi}{16} = \frac{5\pi}{32} \approx 0.4909$.

Check: $I_2 = \frac{\pi}{4}$ agrees with the half-angle computation $\left[\frac{x}{2} - \frac{\sin 2x}{4}\right]_0^{\pi/2} = \frac{\pi}{4}$, and a midpoint sum for $I_6$ gives $0.4909$.

</details>

8\. Find the area of the ellipse $\frac{x^2}{9} + \frac{y^2}{4} = 1$ with a trig substitution.

<details class="solution" markdown>
<summary>Solution</summary>

The upper half of the ellipse is $y = \frac{2}{3}\sqrt{9 - x^2}$, and by symmetry the area is 4 times the area of the quarter in the first quadrant: $4\int_0^3\frac{2}{3}\sqrt{9 - x^2}\,dx$.

Let $x = 3\sin\theta$, so $dx = 3\cos\theta\,d\theta$, $\sqrt{9 - x^2} = 3\cos\theta$, and the limits are $\theta = 0$ and $\theta = \frac{\pi}{2}$. Then $\int_0^3\sqrt{9 - x^2}\,dx = \int_0^{\pi/2}9\cos^2\theta\,d\theta = 9\cdot\frac{\pi}{4} = \frac{9\pi}{4}$, using the result of Example 6. So the area is $4\cdot\frac{2}{3}\cdot\frac{9\pi}{4} = 6\pi \approx 18.85$.

Check: the formula for an ellipse with semi-axes $a$ and $b$ is $\pi ab = \pi\cdot 3\cdot 2 = 6\pi$. The ellipse contains the circle of radius 2 (area $4\pi = 12.57$) and sits inside the circle of radius 3 (area $9\pi = 28.27$), and $18.85$ is between those.

</details>

## Where this shows up

- The next lesson, [partial fractions and improper integrals](05-partial-fractions-and-improper-integrals.md), uses parts to show that $\int_0^\infty x\,e^{-x}\,dx = 1$ once improper integrals are defined, and [applications of integrals](06-applications-of-integrals.md) uses it for the mean of the exponential distribution. Trig integrals also give the average of $\sin^2$ over a period and the area of a disc and an ellipse.
- In CS and engineering, the orthogonality of sines and cosines, $\int_0^{2\pi}\sin(mx)\sin(nx)\,dx = 0$ for $m \ne n$, is proved with these identities and underlies Fourier series, audio compression and the FFT. Parts is also how the factorial turns up as an integral, in the gamma function.
- In probability and economics, expected values of continuous variables such as $\int x\,\lambda e^{-\lambda x}\,dx$ need parts ([continuous random variables and the normal distribution](../07-probability/04-continuous-random-variables-and-the-normal.md)), and so do present values of a growing income stream.
