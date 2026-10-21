# Derivatives

The derivative as a limit of slopes, the rules that make it fast to compute, and the chain rule with its consequences.

1. [The derivative definition](01-the-derivative-definition.md)
2. [Differentiation rules](02-differentiation-rules.md)
3. [Chain rule, implicit and inverse derivatives](03-chain-rule-implicit-and-inverse-derivatives.md)

## Cheat sheet

### The derivative definition

The difference quotient $\frac{f(a + h) - f(a)}{h}$ is the slope of a secant line. The derivative is its limit as $h \to 0$:

$$
f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h} = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}.
$$

The tangent line at $(a, f(a))$ is $y = f(a) + f'(a)(x - a)$. The number $f'(a)$ is the instantaneous rate of change, in units of $f$ per unit of $x$.

| Notation | Meaning |
|---|---|
| $f'(x)$, $\dfrac{dy}{dx}$, $\dfrac{d}{dx}f(x)$ | the derivative function |
| $f'(a)$, $\left.\dfrac{dy}{dx}\right\rvert_{x=a}$ | the derivative at one point |

To compute from the definition: write the quotient, simplify until the $h$ in the denominator cancels (expand, common denominator, or conjugate), then put $h = 0$.

A derivative fails to exist at a corner (different one-sided slopes, as for $\lvert x \rvert$ at 0), a cusp, a vertical tangent (limit is $\pm\infty$), and a discontinuity. Differentiable implies continuous, and the converse is false.

Numerically, the central difference $\frac{f(x + h) - f(x - h)}{2h}$ beats the forward difference. A step near $10^{-5}$ works well in double precision; a smaller $h$ lets rounding error grow like $\frac{10^{-16}}{h}$.

Main mistakes:

- Putting $h = 0$ before cancelling, which gives $\frac{0}{0}$.
- Writing $(x + h)^2$ as $x^2 + h^2$.
- Treating continuous as differentiable.
- Differentiating $f(a)$, a constant, instead of evaluating $f'$ at $a$.
- Dropping the units or the sign of a rate.

### Differentiation rules

| Rule | Formula |
|---|---|
| constant | $(c)' = 0$ |
| power | $(x^n)' = n x^{n-1}$ for every real $n$ ($x > 0$ if $n$ is not an integer) |
| constant multiple, sum | $(cf)' = cf'$, $(f \pm g)' = f' \pm g'$ |
| product | $(fg)' = f'g + fg'$ |
| quotient | $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$ |

The power rule for positive integers comes from the binomial theorem: only the term $n x^{n-1}h$ survives after dividing by $h$. The product rule comes from adding and subtracting $f(x + h)g(x)$ and uses continuity of $f$.

Higher derivatives: $f'' = (f')'$, and $f^{(n)}$ is the $n$-th. Velocity is $s'$ and acceleration is $s''$. Marginal revenue is $R'(q)$, and $R = qp(q)$ gives $R' = p + qp'$.

Tricks: rewrite roots and reciprocals as powers and split single-term denominators before differentiating; the derivatives of $\sin$ go around a cycle of four; functions starting with "co" get a minus sign.

Main mistakes:

- Using $(fg)' = f'g'$. For $x \cdot x$ it gives 1, not $2x$.
- Swapping the numerator order in the quotient rule.
- Using the power rule on $b^x$, or the exponential rule on $x^n$.
- Differentiating a constant like $\pi^2$ as if it varied.
- Using degrees: the derivative of $\sin x$ is $\cos x$ only in radians.

### Chain rule, implicit and inverse derivatives

The chain rule: $(f \circ g)'(x) = f'(g(x))\,g'(x)$, or $\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}$. Differentiate the outside and leave the inside, then multiply by the derivative of the inside, layer by layer. For linear inside functions, $\frac{d}{dx}f(kx + c) = kf'(kx + c)$.

Implicit differentiation: differentiate both sides with respect to $x$, attach $\frac{dy}{dx}$ to every term with $y$, then solve. For $x^2 + y^2 = 25$, $\frac{dy}{dx} = -\frac{x}{y}$. The point must be on the curve.

Inverse rule: $\left(f^{-1}\right)'(b) = \frac{1}{f'(a)}$ where $f(a) = b$ and $f'(a) \ne 0$. Reflecting in $y = x$ turns slope $m$ into slope $\frac{1}{m}$.

Logarithmic differentiation: take $\ln$ of both sides, differentiate, multiply by $y$. It handles $x^x$ and long products. For $y = x^x$, $y' = x^x(\ln x + 1)$.

Related rates: differentiate the relating equation with respect to $t$.

### Derivative table

| $f(x)$ | $f'(x)$ | Valid for |
|---|---|---|
| $x^n$ | $n x^{n-1}$ | real $n$, with $x > 0$ unless $n$ is an integer |
| $e^x$ | $e^x$ | all $x$ |
| $b^x$ | $b^x \ln b$ | $b > 0$ |
| $\ln x$ | $\dfrac{1}{x}$ | $x > 0$ |
| $\ln\lvert x \rvert$ | $\dfrac{1}{x}$ | $x \ne 0$ |
| $\log_b x$ | $\dfrac{1}{x \ln b}$ | $x > 0$ |
| $\sin x$ | $\cos x$ | all $x$ |
| $\cos x$ | $-\sin x$ | all $x$ |
| $\tan x$ | $\sec^2 x$ | $\cos x \ne 0$ |
| $\sec x$ | $\sec x \tan x$ | $\cos x \ne 0$ |
| $\csc x$ | $-\csc x \cot x$ | $\sin x \ne 0$ |
| $\cot x$ | $-\csc^2 x$ | $\sin x \ne 0$ |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1 - x^2}}$ | $-1 < x < 1$ |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1 - x^2}}$ | $-1 < x < 1$ |
| $\arctan x$ | $\dfrac{1}{1 + x^2}$ | all $x$ |

With an inner function $u$, multiply each row by $u'$: for example $\frac{d}{dx}e^u = u'e^u$ and $\frac{d}{dx}\ln u = \frac{u'}{u}$.

Main mistakes:

- Forgetting the inner factor: $\frac{d}{dx}\sin(x^2)$ is $2x\cos(x^2)$.
- Dropping $\frac{dy}{dx}$ on a $y$ term in implicit differentiation.
- Using the slope of $f$ at $b$ instead of at $a$ in the inverse rule.
- Mixing up $b^x$ (variable in the exponent) and $x^b$ (variable in the base).
