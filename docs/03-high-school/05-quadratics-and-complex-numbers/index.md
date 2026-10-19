# Quadratics and complex numbers

Parabolas and their three forms, four ways to solve a quadratic equation, and the complex numbers that give every quadratic its solutions.

1. [Quadratic functions and graphs](01-quadratic-functions-and-graphs.md)
2. [Solving quadratic equations](02-solving-quadratic-equations.md)
3. [Complex numbers](03-complex-numbers.md)

## Cheat sheet

### Quadratic functions and graphs

A quadratic function is $f(x) = ax^2 + bx + c$ with $a \ne 0$. Its graph is a parabola that opens up when $a > 0$ and down when $a < 0$, and a larger $\lvert a \rvert$ makes it narrower.

| Form | Written as | Read off |
|---|---|---|
| standard | $ax^2 + bx + c$ | $y$-intercept $c$; axis $x = -\frac{b}{2a}$ |
| vertex | $a(x - h)^2 + k$ | vertex $(h, k)$; axis $x = h$ |
| factored | $a(x - r)(x - s)$ | $x$-intercepts $r$, $s$; axis $x = \frac{r + s}{2}$ |

- Vertex: $h = -\frac{b}{2a}$ and $k = f(h)$. The value $k$ is the minimum if $a > 0$ and the maximum if $a < 0$.
- Completing the square: $ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right)$. Factor $a$ out of the $x^2$ and $x$ terms, add and subtract the square of half the coefficient, and remember that the subtracted number leaves the bracket multiplied by $a$.
- The mirror image of the $y$-intercept $(0, c)$ is $(2h, c)$. The axis is halfway between any two points at the same height.
- Finding an equation: vertex and a point use vertex form; two intercepts and a point use factored form; then solve for $a$.
- Maximum and minimum problems: write the quantity as a function of one variable, note the allowed values, find the vertex, and check the end of the range if the vertex is not allowed.
- Revenue is $R = p \cdot q$. With linear demand the best price is halfway between 0 and the price where $q = 0$. With $q = 800 - 20p$ subscribers, that is $p = 20$ dollars.
- Fence against a wall with 100 m: width 25 m, length 50 m, area 1250 square metres.
- For values one step apart, the change in the change is $2a$.

Main mistakes:

- Reading $2(x + 3)^2 - 8$ as having its vertex at $x = 3$. It is at $-3$.
- Subtracting only 4 instead of $2 \cdot 4$ when completing the square with $a = 2$.
- Giving $-\frac{b}{2a}$ as the maximum value. It is where the maximum happens.
- Ignoring the allowed values, such as a wall that is too short or a negative price.

### Solving quadratic equations

Standard form is $ax^2 + bx + c = 0$. The discriminant is $D = b^2 - 4ac$.

| Equation looks like | Method |
|---|---|
| $ax^2 = k$ or $(x - h)^2 = k$ | square roots: $x = h \pm \sqrt{k}$ |
| no constant term | factor out $x$: $x = 0$ or $x = -\frac{b}{a}$ |
| small integers, or $D$ a perfect square | factoring and the zero-product property |
| anything else | the quadratic formula |
| you also want the vertex | completing the square |

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

| Discriminant | Real solutions | Graph |
|---|---|---|
| $D > 0$ | two | crosses the $x$-axis twice |
| $D = 0$ | one, $-\frac{b}{2a}$ | touches the axis at the vertex |
| $D < 0$ | none | misses the axis |

- Solutions add to $-\frac{b}{a}$ and multiply to $\frac{c}{a}$. Use this as a check.
- If $a + b + c = 0$, then $x = 1$ is a solution and the other is $\frac{c}{a}$.
- With integer coefficients, $D$ a perfect square means the quadratic factors; $ac < 0$ forces $D > 0$.
- Word problems: reject solutions that don't fit, such as a negative length or a time before the start.
- In code, the stable form uses $q = -\frac{1}{2}\left(b + \operatorname{sign}(b)\sqrt{D}\right)$ and the roots $\frac{q}{a}$ and $\frac{c}{q}$, which avoids cancellation when $b^2 \gg 4ac$.

Main mistakes:

- Dividing by $x$ and losing the solution $x = 0$.
- Using the zero-product property when the right side isn't 0.
- Sign errors with $-b$ and $-4ac$ when $b$ or $c$ is negative.
- Cancelling the 2 against only one term in $\frac{4 \pm 2\sqrt{3}}{2}$.
- Forgetting the $\pm$, or forgetting to rearrange to standard form first.

### Complex numbers

The imaginary unit has $i^2 = -1$. A complex number is $z = a + bi$ with real part $a$ and imaginary part $b$ (a real number). It is plotted as the point $(a, b)$.

| Task | Rule | Example |
|---|---|---|
| add, subtract | combine real and imaginary parts | $(3 + i) - (5 - 4i) = -2 + 5i$ |
| multiply | expand, replace $i^2$ by $-1$ | $(2 - 3i)(4 + i) = 11 - 10i$ |
| conjugate | $\overline{a + bi} = a - bi$ | $\overline{-3 + 4i} = -3 - 4i$ |
| modulus | $\lvert z \rvert = \sqrt{a^2 + b^2}$ | $\lvert 3 + 4i \rvert = 5$ |
| divide | multiply top and bottom by the conjugate of the bottom | $\frac{7 + i}{3 - 4i} = \frac{17 + 31i}{25}$ |
| powers of $i$ | $i^n = i^{n \bmod 4}$: $1, i, -1, -i$ | $i^{2026} = -1$ |

- $z\overline{z} = \lvert z \rvert^2$, $\overline{zw} = \overline{z}\,\overline{w}$ and $\lvert zw \rvert = \lvert z \rvert\lvert w \rvert$.
- Multiplying by $i$ turns the point a quarter turn counter-clockwise: $(a, b) \to (-b, a)$.
- If $D < 0$, the solutions are $-\frac{b}{2a} \pm \frac{\sqrt{-D}}{2a}\,i$, a conjugate pair. From vertex form, $h \pm i\sqrt{\frac{k}{a}}$.
- Real polynomials have non-real zeros in conjugate pairs. Every polynomial of degree $n$ has $n$ complex zeros, counting repeats.
- Python: `3 + 4j`, `abs(z)`, `z.conjugate()`, `cmath.sqrt(-4)` is `2j`, and `math.sqrt(-4)` raises an error.

Main mistakes:

- Forgetting $i^2 = -1$ in a product: $(2 + 3i)^2 = -5 + 12i$.
- Using $\sqrt{a}\sqrt{b} = \sqrt{ab}$ for negative numbers: $\sqrt{-4}\sqrt{-9} = -6$.
- Writing $\lvert 3 + 4i \rvert = 7$, or calling $4i$ the imaginary part.
- Changing the wrong sign when taking a conjugate.
- Trying to order complex numbers: $i > 0$ and $i < 0$ are both false.
