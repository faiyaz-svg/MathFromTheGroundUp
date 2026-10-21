# Integrals

The integral as a limit of sums, its link to the derivative, the techniques for finding antiderivatives, and the main applications.

1. [Riemann sums and the definite integral](01-riemann-sums-and-the-definite-integral.md)
2. [The fundamental theorem of calculus](02-fundamental-theorem-of-calculus.md)
3. [U-substitution](03-u-substitution.md)
4. [Integration by parts and trig integrals](04-integration-by-parts-and-trig-integrals.md)
5. [Partial fractions and improper integrals](05-partial-fractions-and-improper-integrals.md)
6. [Applications of integrals](06-applications-of-integrals.md)

## Cheat sheet

### Riemann sums and the definite integral

With $\Delta x = \frac{b - a}{n}$ and sample points $x_k^*$ in each subinterval, the Riemann sum is $\sum_{k=1}^{n} f(x_k^*)\,\Delta x$, and the definite integral is its limit as $n \to \infty$:

$$
\int_a^b f(x)\,dx = \lim_{n \to \infty}\sum_{k=1}^{n} f(x_k^*)\,\Delta x.
$$

| Rule | Sample point | Error shrinks like |
|---|---|---|
| left, right | left or right end | $\frac{1}{n}$ |
| midpoint | middle | $\frac{1}{n^2}$ |
| trapezoid | average of left and right sums | $\frac{1}{n^2}$ (about twice the midpoint error, opposite sign) |

For an increasing $f$, $L_n \le \int \le R_n$ and $R_n - L_n = \Delta x\,(f(b) - f(a))$. Continuous functions are integrable. The integral is signed area: above the axis counts positive, below counts negative. Properties: constants and sums pass through, $\int_b^a = -\int_a^b$, $\int_a^c = \int_a^b + \int_b^c$, and $f \le g$ gives $\int f \le \int g$. Velocity gives displacement $\int v\,dt$, and distance $\int \lvert v \rvert\,dt$.

Main mistakes:

- Calling signed area "area" (the integral of $\sin$ over a full period is 0).
- Using $\Delta x = b - a$ instead of $\frac{b - a}{n}$, or counting $n + 1$ points in a left or right sum.
- Treating $\int fg$ as $\int f \cdot \int g$.

### The fundamental theorem of calculus

Part 1: if $f$ is continuous and $F(x) = \int_a^x f(t)\,dt$, then $F'(x) = f(x)$. With a variable limit, $\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f(g(x))\,g'(x)$.

Part 2: if $F' = f$ on $[a, b]$ with $f$ continuous, then $\int_a^b f(x)\,dx = F(b) - F(a) = \bigl[F\bigr]_a^b$. Any two antiderivatives differ by a constant, so $\int f\,dx = F + C$, and $C$ cancels in a definite integral. The integral of a rate is a net change: $\int_a^b Q'(x)\,dx = Q(b) - Q(a)$, so marginal cost integrates to extra cost and marginal revenue to revenue.

Steps: check that $f$ is continuous on $[a, b]$, rewrite the integrand as table terms, find $F$, compute $F(b) - F(a)$ with the upper limit first, and check the size.

Main mistakes:

- Using the theorem across a break: $\int_{-1}^{1}\frac{dx}{x^2}$ is not $-2$.
- Subtracting in the wrong order, or writing $+C$ in a definite integral.
- Using $\frac{x^{n+1}}{n+1}$ at $n = -1$.
- Dropping the factor $g'(x)$ in $\frac{d}{dx}\int_a^{g(x)}$.

### U-substitution

It runs the chain rule backward: $\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$ with $u = g(x)$, $du = g'(x)\,dx$. For a definite integral the limits become $g(a)$ and $g(b)$:

$$
\int_a^b f(g(x))\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du.
$$

Choose $u$ as the inside of the messiest part whose derivative is also present: a power or root, an exponent, the argument of a trig function, a denominator whose derivative is on top ($\int\frac{h'}{h} = \ln\lvert h \rvert$), or $\ln x$ with $\frac{1}{x}$. If an $x$ is left over, solve $u = g(x)$ for it. For a linear inside, $\int f(ax + b)\,dx = \frac{1}{a}F(ax + b) + C$. Always check by differentiating.

Main mistakes:

- Leaving $x$ in the integral, or forgetting that $dx$ changes.
- Using $x$-limits on a $u$-integral.
- Pulling a variable factor outside the integral.
- Dropping the absolute value in $\ln\lvert u \rvert$.

### Integration by parts and trig integrals

Parts is the product rule backward: $\int u\,dv = uv - \int v\,du$, and $\int_a^b u\,v'\,dx = \bigl[uv\bigr]_a^b - \int_a^b u'\,v\,dx$. Choose $u$ by LIATE (Logarithmic, Inverse trig, Algebraic, Trig, Exponential), so that $\int v\,du$ is simpler. Repeat for polynomials, using the tabular method (derivatives down one column, antiderivatives down the other, alternating signs). If the integral returns to itself, as for $\int e^x\sin x\,dx$, solve for it: $I = \frac{e^x(\sin x - \cos x)}{2} + C$. Use $dv = dx$ for $\ln x$ and inverse trig functions.

| Integrand | Move |
|---|---|
| $\sin^m x\cos^n x$, $n$ odd | peel off $\cos x$, use $\cos^2 = 1 - \sin^2$, set $u = \sin x$ |
| $\sin^m x\cos^n x$, $m$ odd | peel off $\sin x$, use $\sin^2 = 1 - \cos^2$, set $u = \cos x$ |
| both even | $\sin^2 x = \frac{1 - \cos 2x}{2}$, $\cos^2 x = \frac{1 + \cos 2x}{2}$ |
| $\sqrt{a^2 - x^2}$ | $x = a\sin\theta$, root becomes $a\cos\theta$ |

For example, $\int_0^1\sqrt{1 - x^2}\,dx = \int_0^{\pi/2}\cos^2\theta\,d\theta = \frac{\pi}{4}$, a quarter of the unit disc.

Main mistakes:

- Sign errors: the formula is $uv - \int v\,du$.
- Choosing $u$ so that $v$ needs another hard integral.
- Writing $\int\sin^2 x\,dx = \frac{\sin^3 x}{3}$.
- Swapping the choice of $u$ halfway through the loop trick.

### Partial fractions and improper integrals

For a proper rational function, factor the denominator and write one term per factor and per power of a repeated factor: $\frac{A}{x - a}$, then $\frac{A_1}{x - a} + \frac{A_2}{(x - a)^2}$ for a repeat, and $\frac{Bx + C}{x^2 + bx + c}$ for an irreducible quadratic. Clear denominators and use roots and coefficients. For distinct linear factors, cover-up gives $A_i = \frac{P(a_i)}{Q'(a_i)}$. Divide first if the fraction is improper. Integrate to logs, powers and arctangents.

An improper integral is a limit: $\int_a^\infty f = \lim_{b \to \infty}\int_a^b f$, and for an unbounded integrand $\int_a^b f = \lim_{t \to b^-}\int_a^t f$. Split at an interior trouble point and require both halves to converge. The $p$ test:

| Integral | Converges when | Value |
|---|---|---|
| $\displaystyle\int_1^\infty x^{-p}\,dx$ | $p > 1$ | $\frac{1}{p - 1}$ |
| $\displaystyle\int_0^1 x^{-p}\,dx$ | $p < 1$ | $\frac{1}{1 - p}$ |

Comparison: if $0 \le f \le g$ and $\int g$ converges, then $\int f$ converges. A density has $\int_{-\infty}^{\infty} f = 1$, as for $\lambda e^{-\lambda x}$ on $[0, \infty)$, where $P(X > t) = e^{-\lambda t}$.

Main mistakes:

- Skipping the division step for an improper fraction.
- Leaving out a term for a power of a repeated factor.
- Substituting $\infty$ instead of taking a limit.
- Thinking an integrand that tends to 0 must have a finite integral ($\frac{1}{x}$ does not).

### Applications of integrals

| Quantity | Formula |
|---|---|
| area between curves | $\int_a^b (\text{top} - \text{bottom})\,dx$ |
| average value | $\frac{1}{b - a}\int_a^b f\,dx$ (and $f(c)$ equals it for some $c$) |
| volume by slicing | $\int_a^b A(x)\,dx$ |
| discs, washers | $\pi\int f^2\,dx$, $\ \pi\int (f^2 - g^2)\,dx$ |
| consumer surplus | $\int_0^{q^*}(D(q) - p^*)\,dq$ |
| producer surplus | $\int_0^{q^*}(p^* - S(q))\,dq$ |
| present value of a stream | $\int_0^T R(t)\,e^{-rt}\,dt$, and $\frac{R}{r}$ for a perpetuity |
| Gini coefficient | $1 - 2\int_0^1 L(x)\,dx$ |
| expected value | $\int x\,f(x)\,dx$ |

The recipe is to slice, find the amount in one slice, add, and integrate. If curves cross, split the interval. Slice with $y$ as the variable when that gives one formula. Check units, and check against a known shape (a triangle, a cylinder).

Main mistakes:

- Subtracting bottom minus top, or integrating across a crossing.
- Squaring after integrating in the disc method, or using $(f - g)^2$ for a washer.
- Using the average of the endpoints as the average value of a curved function.
- Using a yearly compounded rate as the continuous rate $r$ (use $r = \ln(1 + i)$).

### Antiderivative table

| $f(x)$ | $\displaystyle\int f(x)\,dx$ | Valid for |
|---|---|---|
| $x^n$ | $\dfrac{x^{n+1}}{n+1} + C$ | $n \ne -1$ |
| $\dfrac{1}{x}$ | $\ln\lvert x \rvert + C$ | $x \ne 0$, each side separately |
| $e^x$ | $e^x + C$ | all $x$ |
| $b^x$ | $\dfrac{b^x}{\ln b} + C$ | $b > 0$, $b \ne 1$ |
| $\sin x$ | $-\cos x + C$ | all $x$ |
| $\cos x$ | $\sin x + C$ | all $x$ |
| $\tan x$ | $-\ln\lvert\cos x\rvert + C$ | $\cos x \ne 0$ |
| $\cot x$ | $\ln\lvert\sin x\rvert + C$ | $\sin x \ne 0$ |
| $\sec x$ | $\ln\lvert\sec x + \tan x\rvert + C$ | $\cos x \ne 0$ |
| $\sec^2 x$ | $\tan x + C$ | $\cos x \ne 0$ |
| $\csc^2 x$ | $-\cot x + C$ | $\sin x \ne 0$ |
| $\sec x\tan x$ | $\sec x + C$ | $\cos x \ne 0$ |
| $\csc x\cot x$ | $-\csc x + C$ | $\sin x \ne 0$ |
| $\dfrac{1}{\sqrt{1 - x^2}}$ | $\arcsin x + C$ | $-1 < x < 1$ |
| $\dfrac{1}{1 + x^2}$ | $\arctan x + C$ | all $x$ |
| $\dfrac{1}{x^2 + a^2}$ | $\dfrac{1}{a}\arctan\dfrac{x}{a} + C$ | $a \ne 0$ |
| $\dfrac{1}{x^2 - a^2}$ | $\dfrac{1}{2a}\ln\left\lvert\dfrac{x - a}{x + a}\right\rvert + C$ | $x \ne \pm a$ |
| $\ln x$ | $x\ln x - x + C$ | $x > 0$ |
| $\arctan x$ | $x\arctan x - \frac{1}{2}\ln\left(1 + x^2\right) + C$ | all $x$ |
| $\sin^2 x$ | $\dfrac{x}{2} - \dfrac{\sin 2x}{4} + C$ | all $x$ |
| $\cos^2 x$ | $\dfrac{x}{2} + \dfrac{\sin 2x}{4} + C$ | all $x$ |
| $\sqrt{1 - x^2}$ | $\dfrac{1}{2}\left(\arcsin x + x\sqrt{1 - x^2}\right) + C$ | $-1 \le x \le 1$ |

With a linear inside, $\int f(ax + b)\,dx = \frac{1}{a}F(ax + b) + C$. Any answer can be checked by differentiating it.
