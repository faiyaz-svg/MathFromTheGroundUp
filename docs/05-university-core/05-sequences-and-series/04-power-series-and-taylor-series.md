# Power series and Taylor series

After this lesson you can find the radius and interval of convergence of a power series, build the Taylor polynomial of a function, write the Taylor series of $e^x$, $\sin x$, $\cos x$, $\frac{1}{1 - x}$ and $\ln(1 + x)$, bound the error of a Taylor polynomial with the Lagrange remainder, differentiate and integrate a series term by term, and explain how a computer evaluates $e^x$.

Before this: [convergence tests](03-convergence-tests.md) (the ratio test and the alternating series error bound), [infinite series basics](02-infinite-series-basics.md), [linear approximation and L'Hopital's rule](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md) and [the mean value theorem and extrema](../03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write the degree 2 Taylor polynomial of $e^x$ at $0$ and use it to estimate $e^{0.1}$.
2. For which $x$ does $\displaystyle\sum_{k=0}^{\infty}\left(\frac{x}{2}\right)^k$ converge, and what is its sum?
3. Does $\displaystyle\sum_{k=0}^{\infty}\frac{1}{k!}$ converge?

<details class="solution" markdown>
<summary>Answers</summary>

1. Every derivative of $e^x$ is $e^x$, which is 1 at $x = 0$, so $T_2(x) = 1 + x + \frac{x^2}{2}$. Then $e^{0.1} \approx 1 + 0.1 + 0.005 = 1.105$. (The true value is $1.10517$.)
2. It is a geometric series with ratio $\frac{x}{2}$, so it converges exactly when $\left\lvert\frac{x}{2}\right\rvert < 1$, that is, $-2 < x < 2$, and the sum is $\frac{1}{1 - x/2} = \frac{2}{2 - x}$.
3. Yes. The ratio of consecutive terms is $\frac{1/(k+1)!}{1/k!} = \frac{1}{k + 1} \to 0 < 1$, so the ratio test gives convergence. The sum is $e$.

</details>

## The idea

Your calculator can compute $e^{0.1}$ and $\sin 0.1$, but a processor can only add and multiply. Somewhere inside there must be an algorithm that turns a function into additions and multiplications, which means a polynomial. The question is which polynomial, and how accurate.

The linearization from the earlier lesson is the first answer: near $x = a$, replace $f$ by the line $f(a) + f'(a)(x - a)$, which matches $f$ in value and in slope. To do better, match the curvature as well with a quadratic, then the rate of change of curvature with a cubic, and so on. Each extra term pins down one more derivative at $a$. The result is the Taylor polynomial, and its error shrinks quickly near $a$. For $e^x$ and $\sin x$ the error goes to 0 for every $x$ as the degree grows, and the polynomials become an infinite series that equals the function.

The two figures show it. In the first, the polynomials $T_1, T_2, T_3, T_4$ for $e^x$ hug the curve near 0 and peel away as $x$ moves out, with each higher degree staying close for longer. In the second, the polynomials for $\sin x$ of degree 1, 3, 5, 7 and 9 follow the sine wave for longer and longer stretches.

![The graph of e to the x from x equals negative 3 to 3 in thick dark gray, with the Taylor polynomials of degree 1 in red, 2 in orange, 3 in blue and 4 in green. All five curves meet at the point (0, 1) and are close to each other near zero. For positive x the higher degree curves lie closer to e to the x, and at x equals 3 the values are about 4, 8.5, 13, 16.4 and 20.1.](../../assets/figures/05-university-core/power-series-and-taylor-series-exp-polynomials.svg)

![The graph of sine from negative 2 pi to 2 pi in thick dark gray, with the Taylor polynomials of degree 1, 3, 5, 7 and 9 at 0. The degree 1 polynomial is a straight line. The higher degree curves follow the sine wave over a wider and wider interval around 0 before bending away sharply.](../../assets/figures/05-university-core/power-series-and-taylor-series-sin-polynomials.svg)

A series of the form $\sum c_k x^k$ is also a function of $x$, defined wherever it converges. The geometric series $\sum x^k = \frac{1}{1 - x}$ is the model: it is a polynomial of infinite degree that agrees with the function only for $-1 < x < 1$. The third figure shows what that means. The partial sums follow $\frac{1}{1 - x}$ inside the shaded band and fly away outside it, even to the left, where $\frac{1}{1 - x}$ itself is perfectly well behaved.

![The graph of 1 over (1 minus x) for x from about negative 1.9 to 0.93, in thick dark gray, with the partial sums of degree 2 in red, degree 4 in orange and degree 8 in blue. A green band marks the interval from negative 1 to 1. Inside the band the partial sums, especially degree 8, stay close to the curve. To the left of negative 1 the partial sums turn upward and move away from the curve, with the degree 8 curve shooting up the steepest.](../../assets/figures/05-university-core/power-series-and-taylor-series-geometric-radius.svg)

This lesson makes these ideas precise: how far out a series converges (the radius), which polynomial approximates a function (Taylor), how big the error is (the remainder), and what you can do with the result.

## Definitions

A **power series** centred at $a$ is a series of the form

$$
\sum_{k=0}^{\infty}c_k(x - a)^k = c_0 + c_1(x - a) + c_2(x - a)^2 + \cdots,
$$

where $c_0, c_1, \dots$ are constants called the coefficients. For each $x$ it is an ordinary series of numbers. In plain words, a power series is a polynomial with infinitely many terms, and the question is for which $x$ it adds up to something.

The set of $x$ where the series converges is its **interval of convergence**. It always contains the centre $a$ (at $x = a$ every term except $c_0$ is 0). The **radius of convergence** is the number $R$ with $0 \le R \le \infty$ such that the series converges for $\lvert x - a \rvert < R$ and diverges for $\lvert x - a \rvert > R$. In plain words, the interval of convergence is centred at $a$ and reaches $R$ to each side, and what happens exactly at the two endpoints $a \pm R$ has to be checked separately.

Let $f$ have $n$ derivatives at $a$. The **Taylor polynomial** of degree $n$ of $f$ at $a$ is

$$
T_n(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x - a)^k = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x - a)^n.
$$

When $f$ has derivatives of every order at $a$, the **Taylor series** of $f$ at $a$ is the power series $\sum_{k=0}^{\infty}\frac{f^{(k)}(a)}{k!}(x - a)^k$. A Taylor series at $a = 0$ is also called a **Maclaurin series**. The **remainder** is $R_n(x) = f(x) - T_n(x)$, the error of the Taylor polynomial. In plain words, the Taylor polynomial is the polynomial of degree at most $n$ that has the same value and the same first $n$ derivatives as $f$ at $a$, and the remainder is how far off it is at $x$. The linearization $L(x)$ of the earlier lesson is $T_1$.

## How to do it

### The radius of convergence

1. Write the general term of the series, including the powers of $x - a$.
2. Compute $\rho = \lim_{k \to \infty}\left\lvert\frac{c_{k+1}}{c_k}\right\rvert$, if the limit exists. Equivalently, apply the ratio test to the whole term and solve $\lvert x - a \rvert\,\rho < 1$.
3. The radius is $R = \frac{1}{\rho}$, with $R = \infty$ if $\rho = 0$ and $R = 0$ if $\rho = \infty$.
4. Test each endpoint $x = a \pm R$ separately with another test, since the ratio test says nothing when the ratio is exactly 1.
5. State the interval: for each endpoint, open if the series diverges there and closed if it converges.

*Theorem 1.* If $\left\lvert\frac{c_{k+1}}{c_k}\right\rvert \to \rho$, then the power series $\sum c_k(x - a)^k$ converges absolutely for $\lvert x - a \rvert < \frac{1}{\rho}$ and diverges for $\lvert x - a \rvert > \frac{1}{\rho}$.

We know the ratio test for series of numbers. We want to read the radius off the coefficients. The plan is to apply the ratio test to the terms $t_k = c_k(x - a)^k$ with $x$ fixed.

*Proof.* The ratio of consecutive terms is $\left\lvert\frac{t_{k+1}}{t_k}\right\rvert = \left\lvert\frac{c_{k+1}}{c_k}\right\rvert\lvert x - a \rvert \to \rho\lvert x - a \rvert$. By the ratio test the series converges absolutely when $\rho\lvert x - a \rvert < 1$, which is $\lvert x - a \rvert < \frac{1}{\rho}$, and diverges when $\rho\lvert x - a \rvert > 1$. If $\rho = 0$ the limit is $0 < 1$ for every $x$, so the series converges everywhere. $\blacksquare$

Look back: the geometric series has $c_k = 1$, so $\rho = 1$ and $R = 1$, matching the figure. The same test applies to $\sum\frac{x^k}{k!}$, where $\rho = \lim\frac{1}{k + 1} = 0$ and $R = \infty$. A power series with gaps, such as $\sum\frac{x^{2k+1}}{(2k+1)!}$, has $c_k = 0$ for every other power, and the ratio of coefficients is undefined. In that case apply the ratio test to the full term $\left\lvert\frac{x^{2k+3}}{(2k+3)!}\cdot\frac{(2k+1)!}{x^{2k+1}}\right\rvert = \frac{x^2}{(2k+2)(2k+3)} \to 0$.

### Taylor polynomials

1. Compute $f(a), f'(a), f''(a), \dots, f^{(n)}(a)$.
2. Divide the $k$-th derivative value by $k!$. These are the coefficients.
3. Write $T_n(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x - a)^k$.
4. To estimate $f(x)$, evaluate $T_n(x)$, and bound the error with the Lagrange remainder below.

Why divide by $k!$? Suppose we want a polynomial $p(x) = c_0 + c_1(x - a) + c_2(x - a)^2 + \cdots + c_n(x - a)^n$ with $p^{(k)}(a) = f^{(k)}(a)$ for $k = 0, 1, \dots, n$. Differentiating $k$ times, every term with a lower power than $(x - a)^k$ disappears, and every term with a higher power still has a factor of $(x - a)$ left, which is 0 at $x = a$. What remains is the derivative of $c_k(x - a)^k$, which is $k!\,c_k$. So $p^{(k)}(a) = k!\,c_k$, and matching derivatives forces $c_k = \frac{f^{(k)}(a)}{k!}$. The Taylor polynomial is the only polynomial of degree at most $n$ with the matching property.

### The remainder

*Theorem 2 (Taylor's theorem with the Lagrange remainder).* Suppose $f$ has $n + 1$ continuous derivatives on an interval containing $a$ and $x$. Then there is a number $c$ between $a$ and $x$ such that

$$
R_n(x) = \frac{f^{(n+1)}(c)}{(n + 1)!}(x - a)^{n+1}.
$$

In particular, if $\lvert f^{(n+1)}(t) \rvert \le M$ for every $t$ between $a$ and $x$, then

$$
\lvert R_n(x) \rvert \le \frac{M\lvert x - a \rvert^{n+1}}{(n + 1)!}.
$$

We state this without a full proof. For $n = 0$ the statement is $f(x) - f(a) = f'(c)(x - a)$, which is the mean value theorem, and for $n = 1$ it is the error formula for the tangent line in [the mean value theorem lesson](../03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md#the-error-of-a-tangent-line-approximation). The general case is proved by applying Rolle's theorem $n + 1$ times to a function that measures the difference between $f$ and its Taylor polynomial. In plain words, the error looks like the next term of the series, except that the derivative is evaluated at some unknown point $c$ between $a$ and $x$ instead of at $a$.

Look back: the second statement is the useful one. It needs a bound $M$ on the next derivative over the whole interval from $a$ to $x$, not just at the endpoints, and it gives an error bound with no unknown $c$. The bound has the shape $\frac{M\,h^{n+1}}{(n+1)!}$ with $h = \lvert x - a \rvert$, so a small $h$ and a large $n$ both help.

A Taylor series equals the function at $x$ exactly when $R_n(x) \to 0$ as $n \to \infty$, since $R_n(x) = f(x) - T_n(x)$ and $T_n(x)$ is the partial sum.

### The standard series

*Theorem 3.* The following hold, with the stated radius of convergence $R$.

| Function | Series at 0 | $R$ | Interval |
|---|---|---|---|
| $e^x$ | $\displaystyle\sum_{k=0}^{\infty}\frac{x^k}{k!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$ | $\infty$ | all $x$ |
| $\sin x$ | $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k+1}}{(2k + 1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ | $\infty$ | all $x$ |
| $\cos x$ | $\displaystyle\sum_{k=0}^{\infty}\frac{(-1)^kx^{2k}}{(2k)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$ | $\infty$ | all $x$ |
| $\dfrac{1}{1 - x}$ | $\displaystyle\sum_{k=0}^{\infty}x^k = 1 + x + x^2 + \cdots$ | 1 | $(-1, 1)$ |
| $\ln(1 + x)$ | $\displaystyle\sum_{k=1}^{\infty}\frac{(-1)^{k-1}x^k}{k} = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ | 1 | $(-1, 1]$ |

We know the Lagrange bound from Theorem 2, and $\frac{b^n}{n!} \to 0$ for every constant $b$ ([growth orders](01-sequences-and-their-limits.md#growth-orders)). We want $R_n(x) \to 0$ in each case. The plan is to find $M$ for each function and use that growth fact.

*Proof for $e^x$, $\sin x$ and $\cos x$.* For $e^x$ every derivative is $e^x$, which is 1 at 0, so the coefficients are $\frac{1}{k!}$. For $x$ fixed, every $t$ between 0 and $x$ has $e^t \le e^{\lvert x \rvert}$, so $\lvert R_n(x) \rvert \le e^{\lvert x \rvert}\frac{\lvert x \rvert^{n+1}}{(n + 1)!} \to 0$, since $\frac{\lvert x \rvert^{n}}{n!} \to 0$. For $\sin x$ the derivatives cycle $\cos x, -\sin x, -\cos x, \sin x$, so at 0 they take the values $0, 1, 0, -1, \dots$, which gives the odd powers with alternating signs. All derivatives of $\sin$ and $\cos$ are at most 1 in absolute value, so $\lvert R_n(x) \rvert \le \frac{\lvert x \rvert^{n+1}}{(n + 1)!} \to 0$. The same argument works for $\cos x$, whose values at 0 are $1, 0, -1, 0, \dots$. In each case the ratio test confirms $R = \infty$. $\blacksquare$

*Proof for $\frac{1}{1 - x}$ and $\ln(1 + x)$.* The first is the geometric series (Theorem 1 of [infinite series basics](02-infinite-series-basics.md)), with $R = 1$. For the second, integrate the geometric series for $\frac{1}{1 + t} = \sum(-t)^k$ term by term from 0 to $x$, which is allowed inside the radius (Theorem 4 below). This gives $\ln(1 + x) = \sum_{k=0}^{\infty}\frac{(-1)^kx^{k+1}}{k + 1}$ for $-1 < x < 1$, the series in the table. At $x = 1$ the series is the alternating harmonic series, which converges by the alternating series test. To see that its sum is $\ln 2$ and not just something near it, use the Lagrange remainder at $x = 1$: the derivatives of $\ln(1 + t)$ satisfy $\left\lvert f^{(n+1)}(t) \right\rvert = \frac{n!}{(1 + t)^{n+1}} \le n!$ for $0 \le t \le 1$, so $\lvert R_n(1) \rvert \le \frac{n!}{(n + 1)!} = \frac{1}{n + 1} \to 0$. At $x = -1$ the series is $-\sum\frac{1}{k}$, which diverges. $\blacksquare$

Look back: five functions are enough for most work, because new series come from old ones by substituting, adding, multiplying, differentiating and integrating. The pattern in the table is also worth seeing: $e^x$ has all the powers with positive signs, $\sin x$ and $\cos x$ split them into odd and even and put in the alternating signs. The series for $\ln(1 + x)$ has radius 1 because $\ln(1 + x)$ has a trouble spot at $x = -1$, but the series for $\frac{1}{1 + x^2}$ has radius 1 too, though that function is smooth for all real $x$: its trouble spots are at the complex numbers $x = \pm i$, which are at distance 1 from the centre.

### Differentiating and integrating series

*Theorem 4 (term-by-term calculus).* Suppose $f(x) = \sum_{k=0}^{\infty}c_k(x - a)^k$ has radius of convergence $R > 0$. Then on $\lvert x - a \rvert < R$ the function $f$ is differentiable, and

$$
f'(x) = \sum_{k=1}^{\infty}k\,c_k(x - a)^{k-1}, \qquad \int f(x)\,dx = C + \sum_{k=0}^{\infty}\frac{c_k}{k + 1}(x - a)^{k+1}.
$$

Both new series have the same radius of convergence $R$, although the behaviour at the endpoints can change.

This is stated without proof; it is proved in a real analysis course by comparing with a geometric series. In plain words, inside its radius, a power series behaves like a polynomial of infinite degree: you can differentiate and integrate each term separately. This is false for general series of functions, so it is a real property of power series.

Examples of its use:

- Differentiating $e^x = \sum\frac{x^k}{k!}$ gives $\sum_{k\ge1}\frac{kx^{k-1}}{k!} = \sum_{k\ge1}\frac{x^{k-1}}{(k-1)!} = e^x$, which checks that the series is consistent with $\frac{d}{dx}e^x = e^x$.
- Differentiating $\frac{1}{1 - x} = \sum x^k$ gives $\frac{1}{(1 - x)^2} = \sum_{k=1}^{\infty}kx^{k-1}$ for $\lvert x \rvert < 1$. With $x = 1 - p$ this gives $\sum_{k \ge 1}k(1 - p)^{k-1} = \frac{1}{p^2}$, so the expected number of trials until a success with probability $p$ is $E[T] = \sum_{k \ge 1} k\,p(1 - p)^{k-1} = p \cdot \frac{1}{p^2} = \frac{1}{p}$. This is the answer found in [infinite series basics](02-infinite-series-basics.md#worked-examples) by a different route.
- Integrating $\frac{1}{1 + t^2} = \sum(-1)^kt^{2k}$ from 0 to $x$ gives $\arctan x = \sum_{k=0}^{\infty}\frac{(-1)^kx^{2k+1}}{2k + 1}$ for $\lvert x \rvert < 1$. This also holds at $x = 1$, which gives $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \cdots$, though it converges too slowly to compute $\pi$ well: 1,000 terms give 3.1406.

### Where computers use this

A library function for $e^x$ can't sum an infinite series, but it can sum a short polynomial if $x$ is small. The standard trick is range reduction. Write $x = m\ln 2 + r$ where $m$ is a whole number and $\lvert r \rvert \le \frac{\ln 2}{2} \approx 0.3466$. Then $e^x = 2^m e^r$. The factor $2^m$ is a shift of the exponent field of a binary floating-point number, which is cheap, and $e^r$ comes from a polynomial in $r$. With $\lvert r \rvert \le 0.3466$ the Lagrange bound for the degree 13 Taylor polynomial is below $6 \times 10^{-18}$, smaller than the rounding error of double precision (about $1.1 \times 10^{-16}$). Real libraries typically use polynomials fitted to minimize the worst-case error (so a lower degree is enough), but the Taylor polynomial is the baseline idea and it explains why the reduction step exists: the Taylor error depends on how far from the centre you are.

For small angles, $\sin\theta \approx \theta$ and $\cos\theta \approx 1 - \frac{\theta^2}{2}$ are the first terms of the series, and the error bound $\frac{\lvert\theta\rvert^3}{6}$ (for $\sin$) says how small $\theta$ must be. For $\theta = 5^\circ = 0.08727$ radians, $\sin\theta = 0.08716$, so the approximation is off by about 0.13%. This is the small-angle approximation used for pendulums and in optics.

The same series extends to complex numbers. Put $x = i\theta$ in the series for $e^x$, where $i^2 = -1$, so that the powers of $i$ cycle $1, i, -1, -i$:

$$
e^{i\theta} = \sum_{k=0}^{\infty}\frac{(i\theta)^k}{k!} = \left(1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} - \cdots\right) + i\left(\theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \cdots\right) = \cos\theta + i\sin\theta.
$$

The series for $e^z$ converges for every complex $z$ (the ratio test uses $\lvert z \rvert$), so this is a legitimate computation, and the real and imaginary parts are the series for $\cos\theta$ and $\sin\theta$. The result, Euler's formula, says that $e^{i\theta}$ is the point at angle $\theta$ on the unit circle, and $\theta = \pi$ gives $e^{i\pi} = -1$. It is the reason multiplication of complex numbers adds angles, previewed in [complex numbers](../../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md), and it is the basis of the Fourier transform used in signal processing.

## Worked examples

<div class="example" markdown>

### Example 1: a Taylor polynomial and its error

Find the degree 2 Taylor polynomial of $f(x) = \sqrt{x}$ at $a = 4$, use it to estimate $\sqrt{4.1}$, and bound the error.

Step 1: compute the derivatives at 4. $f(x) = x^{1/2}$ gives $f(4) = 2$. Then $f'(x) = \frac{1}{2}x^{-1/2}$, so $f'(4) = \frac{1}{4}$. Next $f''(x) = -\frac{1}{4}x^{-3/2}$, so $f''(4) = -\frac{1}{4\cdot 8} = -\frac{1}{32}$.

Step 2: divide by $k!$. The coefficients are $2$, $\frac{1}{4}$ and $\frac{-1/32}{2} = -\frac{1}{64}$.

Step 3: $T_2(x) = 2 + \frac{x - 4}{4} - \frac{(x - 4)^2}{64}$. The first two terms are the linearization from the earlier lesson, and the last term is the correction for curvature.

Estimate: $T_2(4.1) = 2 + 0.025 - \frac{0.01}{64} = 2.025 - 0.000156 = 2.024844$.

Step 4, error: $f'''(x) = \frac{3}{8}x^{-5/2}$, which is positive and decreasing, so on $[4, 4.1]$ its largest value is $f'''(4) = \frac{3}{8\cdot 32} = 0.011719$. So $\lvert R_2(4.1) \rvert \le \frac{0.011719}{3!}(0.1)^3 = 1.95 \times 10^{-6}$.

Check: the true value is $\sqrt{4.1} = 2.0248457$, and the actual error is $1.92 \times 10^{-6}$, inside the bound. The linearization alone had error $0.00015$, so one more term made the estimate about 80 times better.

</div>

<div class="example" markdown>

### Example 2: radius and interval of convergence

Find the interval of convergence of $\displaystyle\sum_{k=1}^{\infty}\frac{(x - 2)^k}{k\,3^k}$.

Step 1: the term is $t_k = \frac{(x - 2)^k}{k\,3^k}$, centre $a = 2$.

Step 2: the ratio of consecutive terms is $\left\lvert\frac{(x - 2)^{k+1}}{(k + 1)3^{k+1}}\cdot\frac{k\,3^k}{(x - 2)^k}\right\rvert = \frac{k}{k + 1}\cdot\frac{\lvert x - 2 \rvert}{3} \to \frac{\lvert x - 2 \rvert}{3}$.

Step 3: the series converges when $\frac{\lvert x - 2 \rvert}{3} < 1$, so $R = 3$ and the open interval is $-1 < x < 5$.

Step 4, endpoints. At $x = 5$ the series is $\sum\frac{3^k}{k\,3^k} = \sum\frac{1}{k}$, which diverges. At $x = -1$ it is $\sum\frac{(-3)^k}{k\,3^k} = \sum\frac{(-1)^k}{k}$, which converges by the alternating series test.

Step 5: the interval of convergence is $[-1, 5)$.

Check: at $x = 1$ the series is $\sum\frac{(-1/3)^k}{k}$. Replacing $x$ by $-u$ in the series for $\ln(1 + x)$ and negating gives $\sum\frac{u^k}{k} = -\ln(1 - u)$ for $\lvert u \rvert < 1$, so with $u = -\frac{1}{3}$ the sum should be $-\ln\frac{4}{3} = -0.28768$. A numerical sum of 100 terms also gives $-0.28768$.

</div>

<div class="example" markdown>

### Example 3: computing $e$ to six decimal places

How many terms of $e = \sum\frac{1}{k!}$ guarantee an error below $10^{-6}$?

Use $f(x) = e^x$ at $a = 0$ and $x = 1$. Every derivative is $e^t \le e < 3$ on $[0, 1]$, so $\lvert R_n(1) \rvert \le \frac{3}{(n + 1)!}$. We need $\frac{3}{(n + 1)!} < 10^{-6}$. For $n = 8$, $\frac{3}{9!} = 8.3 \times 10^{-6}$, which is too big. For $n = 9$, $\frac{3}{10!} = 8.3 \times 10^{-7}$, which works.

So $T_9(1) = 1 + 1 + \frac{1}{2} + \frac{1}{6} + \cdots + \frac{1}{362880} = 2.718281526\ldots$ is within $10^{-6}$ of $e$.

Check: $e = 2.718281828\ldots$, so the actual error is $3.0 \times 10^{-7}$, inside the bound $8.3 \times 10^{-7}$. The bound used $e < 3$. To avoid going in a circle, note that $e = T_9(1) + R_9(1) \le T_9(1) + \frac{e}{10!}$, so $e \le \frac{T_9(1)}{1 - 1/10!} < 2.72 < 3$.

</div>

<div class="example" markdown>

### Example 4: $\sin 0.1$ by hand

Estimate $\sin 0.1$ with the series, and bound the error.

The terms are $0.1 - \frac{0.1^3}{3!} + \frac{0.1^5}{5!} - \cdots$. Take $T_3(0.1) = 0.1 - \frac{0.001}{6} = 0.0998333$. The next term in the series is $\frac{0.1^5}{120} = 8.3 \times 10^{-8}$. By the Lagrange bound with $n = 4$ (note $T_4 = T_3$ for $\sin$, because the degree 4 coefficient is 0) and $M = 1$, $\lvert R_4(0.1) \rvert \le \frac{0.1^5}{5!} = 8.3 \times 10^{-8}$.

Check: $\sin 0.1 = 0.0998334166\ldots$, and the difference from $T_3(0.1)$ is $8.33 \times 10^{-8}$, essentially equal to the bound. The series for $\sin 0.1$ is alternating with decreasing terms, so the alternating series bound gives the same answer. Using $T_3$ instead of $T_1$ ($0.1$ itself) improves the accuracy from $1.7 \times 10^{-4}$ to $8 \times 10^{-8}$.

</div>

<div class="example" markdown>

### Example 5: an integral with no elementary antiderivative

Estimate $\displaystyle\int_0^1 e^{-x^2}\,dx$ (the area under the bell curve, which matters for continuous random variables and the normal distribution<!-- link: ../07-probability/04-continuous-random-variables-and-the-normal.md -->).

Substitute $t = -x^2$ in the series for $e^t$: $e^{-x^2} = \sum_{k=0}^{\infty}\frac{(-1)^kx^{2k}}{k!} = 1 - x^2 + \frac{x^4}{2} - \frac{x^6}{6} + \cdots$, valid for all $x$. Integrate term by term from 0 to 1 (Theorem 4):

$$
\int_0^1 e^{-x^2}\,dx = \sum_{k=0}^{\infty}\frac{(-1)^k}{k!\,(2k + 1)} = 1 - \frac{1}{3} + \frac{1}{10} - \frac{1}{42} + \frac{1}{216} - \cdots.
$$

The series alternates, the sizes $\frac{1}{k!(2k + 1)}$ decrease to 0, so the error is at most the first omitted term. Five terms give $1 - 0.33333 + 0.1 - 0.02381 + 0.00463 = 0.74749$, with error at most $\frac{1}{11 \cdot 120} = \frac{1}{1320} = 0.00076$.

Check: the true value is $0.746824$, and the difference $0.00066$ is below $0.00076$. This is a sum of areas we can compute exactly, for a function with no formula for its antiderivative.

</div>

<div class="example" markdown>

### Example 6: finish it yourself

Estimate $\cos 0.2$ using $T_2(x) = 1 - \frac{x^2}{2}$, and bound the error using the Lagrange remainder with $n = 3$.

The estimate is $T_2(0.2) = 1 - \frac{0.04}{2} = 0.98$. For the bound, $T_3 = T_2$ for cosine because the $x^3$ coefficient is 0, and $f^{(4)}(t) = \cos t$ has $\lvert f^{(4)}(t) \rvert \le 1$.

<details class="solution" markdown>
<summary>Finish</summary>

By Theorem 2 with $n = 3$ and $M = 1$, $\lvert R_3(0.2) \rvert \le \frac{0.2^4}{4!} = \frac{0.0016}{24} = 6.7 \times 10^{-5}$. So $\cos 0.2$ lies within $0.000067$ of $0.98$, that is, in $[0.979933, 0.980067]$.

Check: $\cos 0.2 = 0.9800666$, so the actual error is $6.66 \times 10^{-5}$, just inside the bound, and the true value is at the top of the interval, as expected, since the next term $+\frac{x^4}{24}$ is positive.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the Taylor polynomial is accurate near the centre and can be terrible far away. At $x = -3$, the polynomial $T_4$ for $e^x$ gives $1.375$ while $e^{-3} = 0.0498$. The Lagrange bound grows with $\lvert x - a \rvert^{n+1}$. The figures show the polynomials peeling away from the curve as $x$ moves away from 0.

</div>

<div class="warning" markdown>

Watch out: a series can converge without converging to the function. The function $f(x) = e^{-1/x^2}$ with $f(0) = 0$ has every derivative equal to 0 at $x = 0$, so its Taylor series at 0 is $0 + 0 + 0 + \cdots$, which converges everywhere to 0, but $f(x) > 0$ for $x \ne 0$. Convergence of the series is not enough. The remainder $R_n(x)$ must tend to 0, as in the proof for $e^x$.

</div>

<div class="warning" markdown>

Watch out: the ratio test gives the radius but not the endpoints. At $x = a \pm R$ the ratio is exactly 1 and the test says nothing. Test the endpoints separately, as in Example 2, where one endpoint converged and the other didn't.

</div>

<div class="warning" markdown>

Watch out: the formula $\ln(1 + x) = x - \frac{x^2}{2} + \cdots$ is only for $-1 < x \le 1$. For $x = 2$ the terms $\frac{(-1)^{k-1}2^k}{k}$ grow without bound, so the series diverges even though $\ln 3$ exists. A series equals its function only inside its interval of convergence.

</div>

<div class="warning" markdown>

Watch out: don't forget $k!$ in the coefficients. The coefficient of $(x - a)^k$ is $\frac{f^{(k)}(a)}{k!}$, not $f^{(k)}(a)$. A check: for $e^x$ at 0 all derivatives are 1, so the coefficients must be $\frac{1}{k!}$, and a missing factorial would make the series the geometric series.

</div>

<div class="warning" markdown>

Watch out: bound the derivative on the whole interval between $a$ and $x$, not at one end. In Example 1 the third derivative is largest at $x = 4$ because it decreases, so the bound used $f'''(4)$. For a derivative that increases, the largest value is at $x$, and using $f'''(a)$ would underestimate the error.

</div>

## Tricks and shortcuts

New series come from old ones. Substituting $x \to -x^2$ in $e^x$ gives the series for $e^{-x^2}$ (Example 5), substituting $x \to 2x$ in $\sin x$ gives $\sin 2x = 2x - \frac{8x^3}{6} + \cdots$, and multiplying $e^x$ by $x$ shifts every power up by one. Always check that the new variable stays inside the radius.

Four values worth knowing near 0: $e^x \approx 1 + x$, $\sin x \approx x$, $\cos x \approx 1 - \frac{x^2}{2}$ and $\ln(1 + x) \approx x - \frac{x^2}{2}$. In economics, $\ln(1 + g) \approx g$ means a log difference is approximately a percent change, so $\ln 1.05 = 0.04879$ is close to 0.05, and one more term gives $0.05 - \frac{0.0025}{2} = 0.04875$ (growth rates and CAGR<!-- link: ../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md -->).

The binomial series generalizes the binomial theorem to any exponent $\alpha$: $(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha - 1)}{2!}x^2 + \cdots$ for $\lvert x \rvert < 1$. For $\alpha = \frac{1}{2}$ it gives $\sqrt{1 + x} \approx 1 + \frac{x}{2} - \frac{x^2}{8}$, so $\sqrt{1.04} \approx 1 + 0.02 - 0.0002 = 1.0198$, and the true value is $1.019804$.

The series for $e^x$ with $x = r$ also explains continuous compounding: $\left(1 + \frac{r}{n}\right)^n \to e^r$ as $n \to \infty$ (continuous compounding and e<!-- link: ../../08-financial-math/02-interest-and-growth/04-continuous-compounding-and-e.md -->).

## In code

The code builds $e^x$ the way a library might: reduce the argument, then sum a degree 13 polynomial. It also checks the error bounds from this lesson.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def my_exp(x, degree=13):
    m = round(x / math.log(2))        # x = m ln 2 + r with |r| <= ln 2 / 2
    r = x - m * math.log(2)
    total, term = 0.0, 1.0
    for k in range(degree + 1):       # Taylor polynomial of e^r, built term by term
        total += term
        term *= r / (k + 1)
    return math.ldexp(total, m)       # multiply by 2^m

for x in (0.5, 10, -3.7):
    print(x, my_exp(x), math.exp(x))
# 0.5 1.648721270700128 1.6487212707001282
# 10 22026.465794806725 22026.465794806718
# -3.7 0.02472352647033939 0.024723526470339388

# Error bounds from the lesson.
print(sum(1 / math.factorial(k) for k in range(10)))   # T_9(1), the estimate of e
# 2.7182815255731922
print(math.e - sum(1 / math.factorial(k) for k in range(10)), 3 / math.factorial(10))
# 3.0288585284310443e-07 8.267195767195768e-07

print(math.sin(0.1) - (0.1 - 0.1**3 / 6), 0.1**5 / 120)
# 8.331349481138783e-08 8.333333333333335e-08

# Integral of exp(-x^2) from 0 to 1 from the series.
print(sum((-1) ** k / (math.factorial(k) * (2 * k + 1)) for k in range(5)))
# 0.7474867724867725
print(sum((-1) ** k / (math.factorial(k) * (2 * k + 1)) for k in range(30)))
# 0.7468241328124271
```

</details>

## FAQ

### Why do the Taylor series of $\sin x$ and $\cos x$ work for every $x$, even $x = 1000$?

Because the factorial in the denominator beats any power of $x$ eventually: $\frac{1000^n}{n!} \to 0$. But for $x = 1000$ you need a very large $n$ before the terms start shrinking (they grow up to around $n = 1000$), so the series converges but is useless numerically. That is why libraries first reduce the angle with the periodicity $\sin(x + 2\pi) = \sin x$ and evaluate a polynomial only for small arguments.

### What is the difference between the Taylor polynomial and the Taylor series?

The polynomial $T_n$ is a finite sum, defined for any function with $n$ derivatives, and it always exists. The series is the limit as $n \to \infty$, and it may converge only for some $x$ and may not equal the function. The remainder $R_n(x) = f(x) - T_n(x)$ links them: the series equals $f(x)$ exactly when $R_n(x) \to 0$.

### Why does the radius of $\ln(1 + x)$ stop at 1 and not somewhere else?

The function has a singularity at $x = -1$, where $\ln(1 + x)$ is undefined, and a power series can't converge on a disc that contains a singularity of the function. The radius is the distance from the centre to the nearest trouble spot, counting complex numbers. That is why $\frac{1}{1 + x^2}$ has radius 1 although it has no problem on the real line: it has poles at $\pm i$.

### Is a power series just a polynomial that doesn't stop?

Almost. Inside the radius it can be differentiated and integrated termwise, added and multiplied like a polynomial. But infinite sums have limits that finite ones don't, and the two things that can go wrong (convergence only on an interval, and a series that converges to the wrong function) don't happen for polynomials.

## Practice

### Warm-up

1\. Find the Taylor polynomial of degree 3 of $f(x) = \ln(1 + x)$ at $a = 0$, using derivatives, and compare with the series in Theorem 3.

<details class="solution" markdown>
<summary>Solution</summary>

$f(x) = \ln(1 + x)$, $f'(x) = \frac{1}{1 + x}$, $f''(x) = -\frac{1}{(1 + x)^2}$, $f'''(x) = \frac{2}{(1 + x)^3}$. At 0 the values are $0, 1, -1, 2$. Dividing by $k!$ gives the coefficients $0, 1, -\frac{1}{2}, \frac{2}{6} = \frac{1}{3}$. So $T_3(x) = x - \frac{x^2}{2} + \frac{x^3}{3}$, which are the first three terms of the series.

Check: $T_3(0.05) = 0.05 - 0.00125 + 0.0000417 = 0.048792$, and $\ln 1.05 = 0.048790$.

</details>

2\. Find the radius of convergence of $\displaystyle\sum_{k=0}^{\infty}\frac{k!\,x^k}{3^k}$.

<details class="solution" markdown>
<summary>Solution</summary>

The ratio of consecutive terms is $\frac{(k + 1)!\,\lvert x \rvert^{k+1}}{3^{k+1}}\cdot\frac{3^k}{k!\,\lvert x \rvert^k} = \frac{(k + 1)\lvert x \rvert}{3}$, which tends to $\infty$ for every $x \ne 0$. So the series diverges for every $x \ne 0$, and $R = 0$: it converges only at the centre $x = 0$.

Check: at $x = 1$ the terms $\frac{k!}{3^k}$ are $0.33, 0.22, 0.22, 0.30, \dots$ and eventually grow without bound, so the series diverges by the $n$-th term test.

</details>

3\. Write out the first four nonzero terms of the series for $x^2\cos(x)$ and the first three of $\frac{1}{1 + x}$.

<details class="solution" markdown>
<summary>Solution</summary>

Multiplying the series $\cos x = 1 - \frac{x^2}{2} + \frac{x^4}{24} - \frac{x^6}{720} + \cdots$ by $x^2$ gives $x^2 - \frac{x^4}{2} + \frac{x^6}{24} - \frac{x^8}{720} + \cdots$. For $\frac{1}{1 + x}$, substitute $x \to -x$ in the geometric series: $1 - x + x^2 - \cdots$.

Check: at $x = 0.1$, $\frac{1}{1.1} = 0.90909$ and $1 - 0.1 + 0.01 = 0.91$, close, and the next term $-0.001$ moves it to $0.909$.

</details>

### Standard

4\. Find the interval of convergence of $\displaystyle\sum_{k=1}^{\infty}\frac{x^k}{k^2}$.

<details class="solution" markdown>
<summary>Solution</summary>

The ratio of consecutive terms is $\frac{\lvert x \rvert^{k+1}}{(k + 1)^2}\cdot\frac{k^2}{\lvert x \rvert^k} = \left(\frac{k}{k + 1}\right)^2\lvert x \rvert \to \lvert x \rvert$, so $R = 1$. At $x = 1$ the series is $\sum\frac{1}{k^2}$, which converges ($p = 2$). At $x = -1$ it is $\sum\frac{(-1)^k}{k^2}$, which converges absolutely. The interval is $[-1, 1]$.

Check: at $x = 1$ the sum is $\frac{\pi^2}{6} = 1.645$, and at $x = 0.5$ it is $0.5 + 0.0625 + 0.0139 + 0.0039 + \cdots \approx 0.5822$.

</details>

5\. Use $T_3(x)$ for $e^x$ at 0 to estimate $e^{0.5}$, and bound the error with the Lagrange remainder. Compare with the actual error.

<details class="solution" markdown>
<summary>Solution</summary>

$T_3(0.5) = 1 + 0.5 + \frac{0.25}{2} + \frac{0.125}{6} = 1.64583$. For the remainder, $f^{(4)}(t) = e^t \le e^{0.5} < 2$ on $[0, 0.5]$ (since $e^{0.5} < 1.7$, so 2 is a safe bound), so $\lvert R_3(0.5) \rvert \le \frac{2\cdot 0.5^4}{24} = 0.0052$.

Check: $e^{0.5} = 1.64872$, so the actual error is $0.00289$, inside the bound $0.0052$.

</details>

6\. Approximate $\displaystyle\int_0^{0.5}\frac{\sin x}{x}\,dx$ using the first three nonzero terms of the series for $\frac{\sin x}{x}$, and bound the error.

<details class="solution" markdown>
<summary>Solution</summary>

$\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \frac{x^6}{5040} + \cdots$. Integrating from 0 to 0.5: $\int_0^{0.5} = 0.5 - \frac{0.5^3}{18} + \frac{0.5^5}{600} - \cdots = 0.5 - 0.0069444 + 0.0000521 = 0.4931076$. The series alternates with decreasing terms, so the error is at most the next term $\frac{0.5^7}{7\cdot 5040} = 2.2 \times 10^{-7}$.

Check: the exact value (the sine integral at 0.5) is $0.4931074$, so the actual error is $2.2 \times 10^{-7}$, inside the bound.

</details>

### Challenge

7\. Show that $\displaystyle\sum_{k=0}^{\infty}\frac{k + 1}{2^k} = 4$ by differentiating a geometric series. Then use it to find the expected number of tosses of a fair coin until the first head.

<details class="solution" markdown>
<summary>Solution</summary>

From $\sum_{k=0}^{\infty}x^k = \frac{1}{1 - x}$ for $\lvert x \rvert < 1$, differentiating term by term gives $\sum_{k=1}^{\infty}kx^{k-1} = \sum_{k=0}^{\infty}(k + 1)x^k = \frac{1}{(1 - x)^2}$. At $x = \frac{1}{2}$ this is $\frac{1}{(1/2)^2} = 4$. So $\sum\frac{k + 1}{2^k} = 4$.

For the coin, the first head on toss $k$ has probability $\left(\frac{1}{2}\right)^k$, so $E[T] = \sum_{k=1}^{\infty}\frac{k}{2^k} = \frac{1}{2}\sum_{k=1}^{\infty}k\left(\frac{1}{2}\right)^{k-1} = \frac{1}{2}\cdot 4 = 2$.

Check: the formula $\frac{1}{p}$ with $p = \frac{1}{2}$ gives 2, and the partial sums of $\sum\frac{k}{2^k}$ are $0.5, 1, 1.375, 1.625, \dots$ climbing toward 2.

</details>

8\. (Reviews [linear approximation and L'Hopital's rule](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md).) Use Taylor series to evaluate $\displaystyle\lim_{x \to 0}\frac{e^x - 1 - x}{x^2}$ and $\displaystyle\lim_{x \to 0}\frac{\sin x - x}{x^3}$, and compare with L'Hopital's rule.

<details class="solution" markdown>
<summary>Solution</summary>

For the first limit, $e^x - 1 - x = \frac{x^2}{2} + \frac{x^3}{6} + \cdots$, so $\frac{e^x - 1 - x}{x^2} = \frac{1}{2} + \frac{x}{6} + \cdots \to \frac{1}{2}$. For the second, $\sin x - x = -\frac{x^3}{6} + \frac{x^5}{120} - \cdots$, so $\frac{\sin x - x}{x^3} = -\frac{1}{6} + \frac{x^2}{120} - \cdots \to -\frac{1}{6}$.

L'Hopital's rule gives the same answers after two applications in the first case ($\frac{e^x - 1}{2x}$, then $\frac{e^x}{2} \to \frac{1}{2}$) and three in the second. The series method sees every cancellation at once.

Check: at $x = 0.01$, $\frac{e^x - 1 - x}{x^2} = 0.50167$ and $\frac{\sin x - x}{x^3} = -0.16667$.

</details>

## Where this shows up

- Later calculus and analysis courses use Taylor series to define functions (the exponential and trigonometric functions can be defined by their series) and to prove results such as the central limit theorem. In the multivariable lessons, the second-order Taylor polynomial is what makes the Hessian test for maxima and minima work (multivariable optimization and Lagrange multipliers<!-- link: ../09-multivariable-calculus-light/03-multivariable-optimization-and-lagrange-multipliers.md -->).
- In CS, Taylor polynomials are how floating-point libraries compute $e^x$, $\ln x$, $\sin x$ and $\cos x$ (floating point basics<!-- link: ../../06-cs-math/01-number-representation/04-floating-point-basics.md -->), and an optimization step of gradient descent or of Newton's method minimizes the first or the second order Taylor approximation of the loss.
- In economics and finance, $\ln(1 + g) \approx g$ turns growth rates into log differences, and the second-order term of a bond's price in the interest rate is its convexity (present value, NPV and bond prices<!-- link: ../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md -->).
