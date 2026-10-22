# Applications of integrals

After this lesson you can set up and evaluate an integral for the area between two curves, the average value of a function, the volume of a solid of revolution, consumer and producer surplus, the present value of a continuous income stream, the Gini coefficient of a Lorenz curve, and the expected value of a continuous random variable.

Before this: [the fundamental theorem of calculus](02-fundamental-theorem-of-calculus.md), [u-substitution](03-u-substitution.md), [integration by parts and trig integrals](04-integration-by-parts-and-trig-integrals.md) and [partial fractions and improper integrals](05-partial-fractions-and-improper-integrals.md). The volume formulas also use the [area of a circle](../../02-middle-school/06-geometry/02-area-and-circles.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find the area of the region between $y = x$ and $y = x^2$ for $0 \le x \le 1$.
2. Find the average value of $f(x) = x^2$ on $[0, 3]$.
3. The region under $y = \sqrt{x}$ from $x = 0$ to $x = 4$ is turned about the $x$-axis. Find the volume of the solid it sweeps out.

<details class="solution" markdown>
<summary>Answers</summary>

1. On $[0, 1]$ the line is above the parabola, so the area is $\int_0^1\left(x - x^2\right)dx = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$.
2. The average value is $\frac{1}{3 - 0}\int_0^3 x^2\,dx = \frac{1}{3}\cdot 9 = 3$.
3. Each slice perpendicular to the axis is a disc of radius $\sqrt{x}$ and area $\pi x$, so the volume is $\int_0^4 \pi x\,dx = \pi\cdot\frac{16}{2} = 8\pi$.

</details>

## The idea

The last five lessons built tools for computing integrals. This one is about setting them up. Almost every use of the integral follows one recipe: cut the problem into thin slices, find the contribution of one slice by treating the varying quantity as constant across it, add the slices, and let the slices get thin. The sum becomes an integral. The quantity differs from problem to problem (an area of a strip, a volume of a disc, the money received in a short time), and the recipe stays the same.

The recipe gives the integral before any antiderivative is found. For the area between two curves, a thin vertical strip at $x$ has height (top curve minus bottom curve) and width $dx$, so its area is $\bigl(f(x) - g(x)\bigr)\,dx$, and the total is the integral of that. For the volume of a solid, a thin slab at $x$ has the area of the cross-section and a thickness $dx$. For a stream of income, the money arriving in a short time $dt$ is the rate times $dt$, discounted for how long you wait. The figure below shows the first of these set-ups, and the sections after it show the others.

![Left, the region between the line y = x and the parabola y = x squared from 0 to 1 is shaded, with a vertical strip of height x minus x squared marked at x = 0.6, and the area is 1 over 6. Right, the region between sine x and cosine x from pi over 4 to 5 pi over 4 is shaded, with area 2 root 2.](../../assets/figures/05-university-core/applications-of-integrals-between.svg)

Three quantities in this lesson are the same operation on different objects. The average of something over an interval is its total divided by the length, the volume of something thick is the integral of its cross-sectional area, and the expected value of a random quantity is its average with each value weighted by how likely it is.

## Definitions

Let $f$ and $g$ be continuous on $[a, b]$ with $f(x) \ge g(x)$. The **area between the curves** is

$$
A = \int_a^b \bigl(f(x) - g(x)\bigr)\,dx.
$$

In plain words, integrate the top curve minus the bottom curve. If the curves cross, split the interval at the crossing points and in each part use top minus bottom, or integrate $\lvert f - g \rvert$. If the region is described more easily with $y$ as the variable, with a right curve $x = h(y)$ and a left curve $x = k(y)$, then $A = \int_c^d \bigl(h(y) - k(y)\bigr)\,dy$.

The **average value** of $f$ on $[a, b]$ is

$$
f_{\text{avg}} = \frac{1}{b - a}\int_a^b f(x)\,dx.
$$

In plain words, it is the height of the rectangle on $[a, b]$ with the same area as the region under the graph. For a constant $f$, it is that constant.

A solid has **cross-sectional area** $A(x)$ if the plane perpendicular to the $x$-axis at $x$ cuts the solid in a region of area $A(x)$. The **volume by slicing** is

$$
V = \int_a^b A(x)\,dx.
$$

A **solid of revolution** is the solid swept out when a region under a curve $y = f(x)$ is turned about the $x$-axis. Its cross-sections are discs of radius $f(x)$, so $A(x) = \pi f(x)^2$ and

$$
V = \pi\int_a^b f(x)^2\,dx \qquad \text{(the disc method).}
$$

If the region lies between two curves $f(x) \ge g(x) \ge 0$, the cross-sections are rings with area $\pi\bigl(f(x)^2 - g(x)^2\bigr)$ (the **washer method**). In plain words, add up thin discs, each with its own radius.

In economics, take a market with an inverse demand function $D(q)$, the price at which buyers will take $q$ units, and an inverse supply function $S(q)$, the price at which sellers will provide $q$ units. At the equilibrium quantity $q^*$ and price $p^* = D(q^*) = S(q^*)$, the **consumer surplus** is $\int_0^{q^*}\bigl(D(q) - p^*\bigr)\,dq$ and the **producer surplus** is $\int_0^{q^*}\bigl(p^* - S(q)\bigr)\,dq$. In plain words, consumer surplus is the total amount by which buyers' willingness to pay exceeds the price they pay, and producer surplus is the total amount by which the price exceeds sellers' minimum prices. Both are areas between a curve and the horizontal line at the market price.

For a continuous income stream of $R(t)$ dollars per year and a continuously compounded discount rate $r$, the **present value** over $T$ years is

$$
\text{PV} = \int_0^T R(t)\,e^{-rt}\,dt.
$$

In plain words, the money received in a short time $dt$ around $t$ is $R(t)\,dt$, and it is worth $e^{-rt}$ times as much today, so the present value is the sum of these discounted amounts.

A **Lorenz curve** is a graph of $y = L(x)$, where $L(x)$ is the fraction of a country's total income that goes to the poorest fraction $x$ of the population. It satisfies $L(0) = 0$, $L(1) = 1$, $L$ is increasing, and $L(x) \le x$. The line $y = x$ is the line of perfect equality. The **Gini coefficient** is

$$
G = \frac{\text{area between the line } y = x \text{ and the curve}}{\text{area under the line } y = x} = 2\int_0^1\bigl(x - L(x)\bigr)\,dx = 1 - 2\int_0^1 L(x)\,dx.
$$

In plain words, $G = 0$ means perfect equality, and $G$ near 1 means one person holds almost everything.

If $X$ is a continuous random variable with density $f$ (see [partial fractions and improper integrals](05-partial-fractions-and-improper-integrals.md)), its **expected value** is

$$
E[X] = \int_{-\infty}^{\infty}x\,f(x)\,dx.
$$

In plain words, it is the average of the possible values, each weighted by its density. Compare the discrete case, $E[X] = \sum x\,P(X = x)$, with the sum turned into an integral.

## How to do it

### Setting up an integral from a slice

1. Draw the region or solid and choose a direction to slice. Choose the variable ($x$ or $y$ or $t$) that makes a slice a simple shape.
2. Describe one slice: its length, area or amount, as a function of its position, and its thickness $dx$.
3. Write the integral of (amount of a slice) over the range of positions. Check the units: the units of the answer are the units of the slice's amount times the units of $dx$ summed, as in dollars per year times years.
4. Evaluate with the tools of the earlier lessons.
5. Check against a shape you know, an estimate, or a numerical sum.

### Area between curves

Find where the curves meet by solving $f(x) = g(x)$, and decide which is on top in each piece. For $y = x$ and $y = x^2$ the curves meet where $x = x^2$, that is, at $x = 0$ and $x = 1$, and the line is above the parabola in between (test $x = \frac{1}{2}$: $\frac{1}{2} > \frac{1}{4}$). The area is $\int_0^1\left(x - x^2\right)dx = \frac{1}{6}$.

When the top and bottom curves swap, split. For $\sin x$ and $\cos x$ on $\left[0, 2\pi\right]$ the curves meet at $x = \frac{\pi}{4}$ and $x = \frac{5\pi}{4}$ (where $\tan x = 1$). Between those points $\sin x \ge \cos x$, so the enclosed region has area $\int_{\pi/4}^{5\pi/4}(\sin x - \cos x)\,dx = \bigl[-\cos x - \sin x\bigr]_{\pi/4}^{5\pi/4} = \sqrt{2} + \sqrt{2} = 2\sqrt{2}$, as in the right panel of the figure above.

### The average value and the mean value theorem for integrals

*Theorem 1 (mean value theorem for integrals).* If $f$ is continuous on $[a, b]$, there is a number $c$ in $[a, b]$ with

$$
f(c) = \frac{1}{b - a}\int_a^b f(x)\,dx, \qquad \text{that is,} \qquad \int_a^b f(x)\,dx = f(c)\,(b - a).
$$

In plain words, a continuous function actually takes its average value somewhere. The rectangle with height $f(c)$ has the same area as the region under the curve.

We know the extreme value theorem and the intermediate value theorem for continuous functions on a closed interval (from [continuity, asymptotes and the IVT](../01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md)), and the comparison property of integrals. We want a point where $f$ equals its average. The plan is to trap the average between the smallest and largest values of $f$, and then use the intermediate value theorem to hit it.

*Proof.* By the extreme value theorem, $f$ has a smallest value $m$ and a largest value $M$ on $[a, b]$, so $m \le f(x) \le M$ for every $x$. By the comparison and constant rules, $m(b - a) \le \int_a^b f \le M(b - a)$. Dividing by $b - a > 0$ gives $m \le f_{\text{avg}} \le M$. The values $m$ and $M$ are both attained by $f$, and by the intermediate value theorem $f$ takes every value between them, so $f(c) = f_{\text{avg}}$ for some $c$ in $[a, b]$. $\blacksquare$

Look back: it is the integral version of the [mean value theorem](../03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md). Apply the derivative version to an antiderivative $F$ of $f$: $F(b) - F(a) = F'(c)(b - a) = f(c)(b - a)$, and the fundamental theorem says the left side is $\int_a^b f$. For $f(x) = x^2$ on $[0, 3]$ the average is 3, and $c^2 = 3$ gives $c = \sqrt{3} \approx 1.73$, a point in the interval. Continuity is needed: a function with a jump may never equal its average.

### Volumes

For the disc method, the solid has a circular cross-section at each $x$, so $V = \pi\int_a^b f(x)^2\,dx$. A sphere of radius $r$ is the region under $y = \sqrt{r^2 - x^2}$ from $-r$ to $r$ turned about the axis:

$$
V = \pi\int_{-r}^{r}\left(r^2 - x^2\right)dx = \pi\left[r^2x - \frac{x^3}{3}\right]_{-r}^{r} = \pi\left(2r^3 - \frac{2r^3}{3}\right) = \frac{4}{3}\pi r^3.
$$

This is the formula for the volume of a sphere from [volume and surface area](../../02-middle-school/06-geometry/03-volume-and-surface-area.md), now with a reason. A cone of radius $R$ and height $H$ is the region under $y = \frac{R}{H}x$ from 0 to $H$ turned about the axis, and $V = \pi\int_0^H\frac{R^2}{H^2}x^2\,dx = \frac{\pi R^2H}{3}$. The washer method subtracts: for the region between $y = x$ and $y = x^2$ turned about the $x$-axis, $V = \pi\int_0^1\left(x^2 - x^4\right)dx = \pi\left(\frac{1}{3} - \frac{1}{5}\right) = \frac{2\pi}{15}$.

## Worked examples

<div class="example" markdown>

### Example 1: area between a parabola and a line

Find the area enclosed by the parabola $x = y^2$ and the line $y = x - 2$.

Step 1: the curves meet where $x = y^2$ and $y = x - 2$, so $y = y^2 - 2$, that is, $y^2 - y - 2 = 0$, so $(y - 2)(y + 1) = 0$. The points are $y = 2$ (with $x = 4$) and $y = -1$ (with $x = 1$).

Step 2: slicing with vertical strips would need two different pieces, because the lower boundary changes at $x = 1$. Slice horizontally instead, with $y$ as the variable. At height $y$ the region runs from the parabola $x = y^2$ on the left to the line $x = y + 2$ on the right.

Step 3: the area is

$$
\int_{-1}^{2}\bigl((y + 2) - y^2\bigr)\,dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_{-1}^{2} = \left(2 + 4 - \frac{8}{3}\right) - \left(\frac{1}{2} - 2 + \frac{1}{3}\right) = \frac{10}{3} + \frac{7}{6} = \frac{9}{2}.
$$

Check: the region fits inside the rectangle $1 \le x \le 4$, $-1 \le y \le 2$, which has area $3 \cdot 3 = 9$, and $\frac{9}{2}$ is a plausible fraction of it. With vertical strips the same area comes out as $\int_0^1 2\sqrt{x}\,dx + \int_1^4\left(\sqrt{x} - (x - 2)\right)dx = \frac{4}{3} + \frac{19}{6} = \frac{9}{2}$.

</div>

<div class="example" markdown>

### Example 2: average value

Find the average of $\sin^2 x$ over $[0, \pi]$, and the average of the marginal cost $20 - 0.02q$ dollars per unit over $q$ from 100 to 300.

For the first, from the last lessons $\int_0^\pi\sin^2 x\,dx = \frac{\pi}{2}$, so the average is $\frac{\pi/2}{\pi} = \frac{1}{2}$. For the second, $\int_{100}^{300}(20 - 0.02q)\,dq = 3200$ (the extra cost from Example 3 of the [fundamental theorem lesson](02-fundamental-theorem-of-calculus.md)), and the interval has length 200, so the average marginal cost is $\frac{3200}{200} = 16$ dollars per unit.

Check: the first average lies between the least value 0 and the greatest value 1 of $\sin^2 x$, and by symmetry $\sin^2$ and $\cos^2$ share the total of 1, so $\frac{1}{2}$ is right. For the second, the marginal cost is linear from \$18 at $q = 100$ to \$14 at $q = 300$, so its average is the midpoint \$16, and the value $c$ where $20 - 0.02c = 16$ is $c = 200$, in the interval.

</div>

<div class="example" markdown>

### Example 3: volumes by discs

Find the volume of the solid made by turning the region under $y = \sqrt{x}$ for $0 \le x \le 4$ about the $x$-axis.

A slice at $x$ is a disc of radius $\sqrt{x}$ and thickness $dx$, so its volume is $\pi\left(\sqrt{x}\right)^2dx = \pi x\,dx$.

$$
V = \int_0^4\pi x\,dx = \pi\left[\frac{x^2}{2}\right]_0^4 = 8\pi \approx 25.13.
$$

![The region under y equals the square root of x from 0 to 4, and its mirror image below the axis, shaded green. A thin orange disc at x = 2.4 has radius root x, drawn as a vertical ellipse, and its volume is pi x dx. The solid's end face at x = 4 is a larger ellipse. The total volume is 8 pi.](../../assets/figures/05-university-core/applications-of-integrals-revolve.svg)

Check: the solid is inside the cylinder of radius 2 and length 4, which has volume $\pi\cdot 4\cdot 4 = 16\pi$, and the answer $8\pi$ is exactly half of it. A numerical sum of the disc areas $\pi x$ with 100,000 slices gives $25.1327$.

</div>

<div class="example" markdown>

### Example 4: consumer and producer surplus

In a market (hypothetical numbers), the inverse demand is $D(q) = 100 - 2q$ and the inverse supply is $S(q) = 20 + 0.1q^2$, with $q$ in thousands of units and prices in dollars. Find the equilibrium and both surpluses.

Equilibrium: $D(q) = S(q)$ gives $100 - 2q = 20 + 0.1q^2$, so $0.1q^2 + 2q - 80 = 0$ and $q^2 + 20q - 800 = 0$, so $(q - 20)(q + 40) = 0$. Only $q^* = 20$ is positive, and $p^* = D(20) = 60$.

Consumer surplus: $\int_0^{20}(100 - 2q - 60)\,dq = \int_0^{20}(40 - 2q)\,dq = \bigl[40q - q^2\bigr]_0^{20} = 800 - 400 = 400$.

Producer surplus: $\int_0^{20}\left(60 - 20 - 0.1q^2\right)dq = \left[40q - \frac{0.1q^3}{3}\right]_0^{20} = 800 - \frac{800}{3} = \frac{1600}{3} \approx 533.3$.

![A supply and demand graph with quantity in thousands of units on the horizontal axis and price in dollars on the vertical axis. A falling blue demand line and a rising orange supply curve cross at q = 20, p = 60. The area between the demand line and the price line p = 60 is shaded blue and labelled consumer surplus 400. The area between the price line and the supply curve is shaded orange and labelled producer surplus about 533.3.](../../assets/figures/05-university-core/applications-of-integrals-surplus.svg)

The units: surplus is dollars per unit times thousands of units, so the surpluses are about \$400 thousand and \$533.3 thousand. Total surplus is $\frac{2800}{3} \approx 933.3$ thousand dollars.

Check: the consumer surplus is a triangle with base 20 and height $100 - 60 = 40$, so its area is $\frac{1}{2}\cdot 20\cdot 40 = 400$. The producer surplus is less than the rectangle $20\cdot 40 = 800$ and more than the triangle with the same base and height 40 (400), since the supply curve bends upward, and $533.3$ fits.

</div>

<div class="example" markdown>

### Example 5: present value of an income stream

A project is expected to pay \$50,000 a year, spread evenly over 10 years. With a continuous discount rate of 4% a year (a hypothetical rate), what is it worth today? What if the stream never ended?

Here $R(t) = 50{,}000$ is constant, $r = 0.04$ and $T = 10$:

$$
\text{PV} = \int_0^{10}50000\,e^{-0.04t}\,dt = 50000\left[\frac{e^{-0.04t}}{-0.04}\right]_0^{10} = \frac{50000}{0.04}\left(1 - e^{-0.4}\right) = 1{,}250{,}000 \cdot 0.32968 \approx \$412{,}100.
$$

If the stream never ends, take $T \to \infty$: $\int_0^\infty 50000\,e^{-0.04t}\,dt = \frac{50000}{0.04} = \$1{,}250{,}000$, an improper integral that converges because $e^{-0.04t}$ decays. This is a **perpetuity**, a stream with no end date, with value $\frac{R}{r}$.

Check: the undiscounted total over 10 years is \$500,000, and discounting lowers it, to \$412,100. The perpetuity's value \$1,250,000 is more than the 10-year value, as it should be since it adds more payments, but it is finite: the first 10 years contribute about a third of it. A numerical sum of $R(t)e^{-rt}$ over 100,000 slices gives \$412,099.94. For a stream that grows at 2% a year, $R(t) = 50000\,e^{0.02t}$, the integrand becomes $50000\,e^{-0.02t}$ and the value is $\frac{50000}{0.02}\left(1 - e^{-0.2}\right) \approx \$453{,}173$.

</div>

<div class="example" markdown>

### Example 6: a Gini coefficient

A country's Lorenz curve is $L(x) = x^2$ (hypothetical). Find the Gini coefficient and say what the curve says about the poorest half. Then estimate $G$ from the quintile data below, where the poorest 20% of households have 5% of income, the next 20% have 10%, then 15%, 25% and 45% (also hypothetical).

For the curve, $G = 1 - 2\int_0^1 x^2\,dx = 1 - 2\cdot\frac{1}{3} = \frac{1}{3}$. At $x = \frac{1}{2}$ the curve gives $L = \frac{1}{4}$: the poorest half of the population has 25% of the income.

![A square graph with the share of the population, poorest first, on the horizontal axis and the share of total income on the vertical axis. A dashed diagonal is the line of equality. The curve y equals x squared lies below it. The area between the diagonal and the curve is shaded red and labelled A, and the area under the curve is shaded blue and labelled B. A dotted line marks that at x = 0.5 the curve is at 0.25.](../../assets/figures/05-university-core/applications-of-integrals-lorenz.svg)

In the figure the Gini coefficient is the area $A$ between the diagonal and the curve, divided by the area $A + B = \frac{1}{2}$ under the diagonal, which is $2A$.

For the data, the Lorenz curve passes through $(0, 0)$ and then $(0.2, 0.05)$, $(0.4, 0.15)$, $(0.6, 0.30)$, $(0.8, 0.55)$ and $(1, 1)$, where each height is the running total of the shares. Join the points with straight lines, so that the area under the curve is a trapezoid sum with width 0.2:

$$
\int_0^1 L \approx 0.2\left(\frac{0}{2} + 0.05 + 0.15 + 0.30 + 0.55 + \frac{1}{2}\right) = 0.2\cdot 1.55 = 0.31, \qquad G \approx 1 - 2\cdot 0.31 = 0.38.
$$

Check: with perfect equality, $L(x) = x$, $\int_0^1 L = \frac{1}{2}$ and $G = 0$, and if one person held everything $L$ would be 0 until $x = 1$, giving $G = 1$. Both estimates, $\frac{1}{3}$ and $0.38$, lie between. Straight lines between the quintile points lie above the true curve (the Lorenz curve is convex), so the true Gini is a little more than $0.38$.

</div>

<div class="example" markdown>

### Example 7: expected value (finish it yourself)

A random variable $X$ has density $f(x) = 2x$ on $[0, 1]$ and $0$ elsewhere (it is a density, since $\int_0^1 2x\,dx = 1$). Find $E[X]$. Then, for the exponential density $\lambda e^{-\lambda x}$ on $[0, \infty)$, set up $E[X] = \int_0^\infty x\,\lambda e^{-\lambda x}\,dx$ and use parts with $u = x$ and $dv = \lambda e^{-\lambda x}\,dx$, so $v = -e^{-\lambda x}$. Finish the integral and check.

<details class="solution" markdown>
<summary>Finish</summary>

First density: $E[X] = \int_0^1 x\cdot 2x\,dx = \int_0^1 2x^2\,dx = \frac{2}{3}$. The values are weighted toward the right end, where the density is larger, so the mean is above the midpoint $\frac{1}{2}$.

Exponential: with parts, $\int_0^b x\,\lambda e^{-\lambda x}\,dx = \bigl[-x\,e^{-\lambda x}\bigr]_0^b + \int_0^b e^{-\lambda x}\,dx = -b\,e^{-\lambda b} + \frac{1 - e^{-\lambda b}}{\lambda}$. As $b \to \infty$, $b\,e^{-\lambda b} \to 0$ and $e^{-\lambda b} \to 0$, so $E[X] = \frac{1}{\lambda}$.

Check: for $\lambda = 0.5$ the mean wait is 2 seconds, which matches the earlier lesson, where the median was $1.386$, below the mean. For $\lambda = 1$ the integral is the $\int_0^\infty x\,e^{-x}\,dx = 1$ found before. Also the units are consistent: the rate $\lambda$ is per second, and $\frac{1}{\lambda}$ is in seconds.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: top minus bottom, in that order, and only between the crossing points. If you subtract the other way you get a negative area. If the curves cross inside the interval and you integrate $f - g$ over the whole interval, the regions where $g$ is on top count as negative and cancel part of the area. For $\sin x - \cos x$ over $[0, 2\pi]$ the integral is 0, but the area between the two curves over that interval is $4\sqrt{2}$.

</div>

<div class="warning" markdown>

Watch out: square the radius before integrating, not after. The disc method uses $\pi\int f(x)^2\,dx$ and not $\pi\left(\int f\,dx\right)^2$. For $f(x) = \sqrt{x}$ on $[0, 4]$ the second would give $\pi\left(\frac{16}{3}\right)^2$, which is wrong, while $\pi\int_0^4 x\,dx = 8\pi$ is right. In the washer method, square each radius separately: $f^2 - g^2$ and not $(f - g)^2$.

</div>

<div class="warning" markdown>

Watch out: the average of a function is not the average of its endpoints, except for a linear function. For $f(x) = x^2$ on $[0, 3]$ the endpoint average is $\frac{0 + 9}{2} = 4.5$, but the average value is 3, because the function spends more of the interval at low values. For a linear function the two agree, as in Example 2.

</div>

<div class="warning" markdown>

Watch out: keep the units and the discounting honest in money problems. The integral $\int R(t)e^{-rt}\,dt$ needs $r$ as a continuous rate. A quoted annual rate of 4% compounded yearly is not $r = 0.04$ for the continuous formula, and the conversion is $r = \ln 1.04 \approx 0.0392$. The two rates give slightly different present values. Surpluses are areas in (price times quantity), so check that the axes' units match what you are measuring.

</div>

An integral can set up a quantity in the wrong order of dimensions. The volume of a solid is an integral of area, a length squared, so the answer has units of length cubed. If an integral of a length gives a "volume", the set-up has lost a dimension. Dimensional analysis is a fast check on every set-up in this lesson.

The disc method assumes the region touches the axis of rotation along its whole length. If it doesn't, use the washer method, with an outer and an inner radius, and don't forget the hole.

## Tricks and shortcuts

Symmetry halves the work. For a region symmetric about the $y$-axis, double the integral over $[0, b]$. For a solid of revolution of a function that is even, the volume is $2\pi\int_0^b f^2\,dx$, as for the sphere.

The integral of the average value is the same as the integral of the function: $\int_a^b f_{\text{avg}}\,dx = \int_a^b f\,dx$, so if you know the total and the length you know the average, and if you know the average and the length you know the total. That gives a quick estimate: the average of a function on an interval is between its smallest and largest values.

The Gini coefficient from a few points is a trapezoid sum, as in Example 6, and the same trapezoid rule works on any table of data: write the cumulative shares, apply the rule, double and subtract from 1. The errors are in one direction, because a convex curve lies below its chords.

For a surplus triangle with a linear curve, skip the integral: consumer surplus is $\frac{1}{2}\times\text{quantity}\times(\text{choke price} - p^*)$, where the choke price is the price at which demand falls to zero (here 100). In Example 4 this is $\frac{1}{2}\cdot 20\cdot 40 = 400$.

## In code

A few lines of numerical integration check every set-up in this lesson. The function `integral` is the midpoint sum from earlier. Each result can be compared with the exact value worked out above.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def integral(f, a, b, n=100000):
    dx = (b - a) / n
    return dx * sum(f(a + (k + 0.5) * dx) for k in range(n))

# Area between y = x and y = x^2: 1/6.
print(round(integral(lambda x: x - x * x, 0, 1), 5), round(1 / 6, 5))
# 0.16667 0.16667

# Volume of the solid of revolution of sqrt(x) on [0, 4]: 8*pi.
print(round(integral(lambda x: math.pi * x, 0, 4), 4), round(8 * math.pi, 4))
# 25.1327 25.1327

# Surpluses: D(q) = 100 - 2q, S(q) = 20 + 0.1 q^2, equilibrium q = 20, p = 60.
cs = integral(lambda q: (100 - 2 * q) - 60, 0, 20)
ps = integral(lambda q: 60 - (20 + 0.1 * q * q), 0, 20)
print(round(cs, 2), round(ps, 2))
# 400.0 533.33

# Present value of 50,000 a year for 10 years at a continuous 4%.
pv = integral(lambda t: 50000 * math.exp(-0.04 * t), 0, 10)
print(round(pv, 2), round(50000 / 0.04 * (1 - math.exp(-0.4)), 2))
# 412099.94 412099.94

# Gini from quintile shares (trapezoid rule on the Lorenz curve).
shares = [0.05, 0.10, 0.15, 0.25, 0.45]
L = [0.0]
for s in shares:
    L.append(L[-1] + s)
area = 0.2 * (L[0] / 2 + sum(L[1:-1]) + L[-1] / 2)
print(round(1 - 2 * area, 2))
# 0.38

# Expected value of the exponential density with rate 0.5 (the tail past 60 is negligible).
lam = 0.5
print(round(integral(lambda x: x * lam * math.exp(-lam * x), 0, 60), 4), 1 / lam)
# 2.0 2.0
```

</details>

## FAQ

### Why does the volume formula integrate area and not length?

Because volume is built from slabs, and a slab's volume is its cross-sectional area times its thickness. The one-dimensional pieces of an area integral are lengths times thickness, and the two-dimensional pieces of a volume integral are areas times thickness. If you integrate a length you get an area, and if you integrate an area you get a volume. Cavalieri's principle says the same: two solids with equal cross-sectional areas at every height have equal volumes.

### Why is consumer surplus an area?

Take the buyers in order of how much they would pay. The first unit goes to the buyer willing to pay $D(1)$ (in a continuous model, $D(q)$ at quantity $q$), the next to a buyer willing to pay a little less, and so on, but every buyer pays the same market price $p^*$. The gain of the buyer of unit $q$ is $D(q) - p^*$, and the integral adds these gains for every unit up to $q^*$. The picture is the area above the price line and below the demand curve.

### Is a continuous income stream realistic?

It is an approximation that gives clean formulas. A salary paid every two weeks is close to continuous compared with a 10-year horizon, and the formula $\frac{R}{r}\left(1 - e^{-rT}\right)$ agrees closely with the sum of the discrete payments. For a few large payments, the discrete formulas of the finance chapters (present and future value<!-- link: ../../08-financial-math/03-time-value-of-money/01-present-and-future-value.md -->) are better. The two are linked: the sum of a geometric series becomes an integral of an exponential as the payments get more frequent.

### What does the Gini coefficient measure, and what does it hide?

It measures how far the Lorenz curve bends away from the line of equality, as a single number between 0 and 1. It hides where the inequality is: two different Lorenz curves can have the same Gini coefficient, one with a very rich top 1% and the other with a poor bottom 20%. Compare the whole curve when the shape matters.

## Practice

### Warm-up

1\. Find the area between $y = x^2$ and $y = 8 - x^2$.

<details class="solution" markdown>
<summary>Solution</summary>

The curves meet where $x^2 = 8 - x^2$, so $x^2 = 4$ and $x = \pm 2$. Between those points $8 - x^2 \ge x^2$ (test $x = 0$: $8 > 0$). The area is $\int_{-2}^{2}\left(8 - 2x^2\right)dx = 2\int_0^2\left(8 - 2x^2\right)dx = 2\left[8x - \frac{2x^3}{3}\right]_0^2 = 2\left(16 - \frac{16}{3}\right) = \frac{64}{3}$.

Check: the region fits in a rectangle $4$ wide and $8$ high, with area 32, and $\frac{64}{3} = 21.3$ is two thirds of it, a plausible share for a region between two parabolas.

</details>

2\. Find the average value of $f(x) = \sqrt{x}$ on $[0, 9]$, and find a point $c$ where $f$ takes that value.

<details class="solution" markdown>
<summary>Solution</summary>

The integral is $\int_0^9\sqrt{x}\,dx = \frac{2}{3}\cdot 27 = 18$, so the average is $\frac{18}{9} = 2$. Then $\sqrt{c} = 2$ gives $c = 4$, which is in $[0, 9]$.

Check: the average 2 lies between the least value 0 and the greatest value 3. It is above the endpoint average $\frac{0 + 3}{2} = 1.5$, because $\sqrt{x}$ is concave: it climbs quickly at first and spends most of the interval at heights near 3.

</details>

3\. A cone has base radius 3 and height 5. Use the disc method to find its volume, and compare with $\frac{1}{3}\pi R^2H$.

<details class="solution" markdown>
<summary>Solution</summary>

Turn the region under $y = \frac{3}{5}x$ for $0 \le x \le 5$ about the $x$-axis. Then $V = \pi\int_0^5\frac{9}{25}x^2\,dx = \pi\cdot\frac{9}{25}\cdot\frac{125}{3} = 15\pi$.

Check: $\frac{1}{3}\pi R^2H = \frac{1}{3}\pi\cdot 9\cdot 5 = 15\pi$, the same.

</details>

### Standard

4\. Find the area enclosed by $y = \sqrt{x}$, $y = 0$ and the line $y = x - 2$.

<details class="solution" markdown>
<summary>Solution</summary>

The curve and the line meet where $\sqrt{x} = x - 2$, so $x = (x - 2)^2$, which gives $x^2 - 5x + 4 = 0$, so $x = 1$ or $x = 4$. Only $x = 4$ works in the original equation ($\sqrt{1} = 1 \ne -1$), so the meeting point is $(4, 2)$. The line meets the axis at $x = 2$. Slice horizontally: at height $y$ from 0 to 2, the region runs from the curve $x = y^2$ on the left to the line $x = y + 2$ on the right. The area is $\int_0^2\bigl(y + 2 - y^2\bigr)\,dy = \left[\frac{y^2}{2} + 2y - \frac{y^3}{3}\right]_0^2 = 2 + 4 - \frac{8}{3} = \frac{10}{3}$.

Check: with vertical strips, the area is $\int_0^2\sqrt{x}\,dx + \int_2^4\bigl(\sqrt{x} - (x - 2)\bigr)\,dx = \frac{2}{3}2^{3/2} + \left[\frac{2}{3}x^{3/2} - \frac{x^2}{2} + 2x\right]_2^4$, which is $1.8856 + (5.3333 - 8 + 8) - (1.8856 - 2 + 4) = 1.8856 + 5.3333 - 3.8856 = 3.3333$, which is $\frac{10}{3}$.

</details>

5\. In a market, inverse demand is $D(q) = 90 - q$ and inverse supply is $S(q) = 10 + q$ ($q$ in thousands of units, dollars per unit; hypothetical numbers). Find the equilibrium, and the consumer and producer surplus.

<details class="solution" markdown>
<summary>Solution</summary>

Setting $90 - q = 10 + q$ gives $q^* = 40$ and $p^* = 50$. Consumer surplus: $\int_0^{40}(90 - q - 50)\,dq = \int_0^{40}(40 - q)\,dq = 1600 - 800 = 800$. Producer surplus: $\int_0^{40}(50 - 10 - q)\,dq = 800$ as well. So each is \$800 thousand and the total is \$1.6 million.

Check: both are triangles with base 40 and height 40, so each has area $\frac{1}{2}\cdot 40\cdot 40 = 800$.

</details>

6\. (Reviews [the fundamental theorem of calculus](02-fundamental-theorem-of-calculus.md).) A tank is filled at a rate of $r(t) = 6 - 0.5t$ litres per minute for $0 \le t \le 10$ minutes. (a) How much water enters? (b) What is the average flow rate, and at what time does the flow equal its average? (c) Show that the amount in the tank, starting empty, is $V(t) = 6t - 0.25t^2$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\int_0^{10}(6 - 0.5t)\,dt = \bigl[6t - 0.25t^2\bigr]_0^{10} = 60 - 25 = 35$ litres.

(b) The average is $\frac{35}{10} = 3.5$ litres per minute. The flow equals it when $6 - 0.5t = 3.5$, so $t = 5$. The flow is linear, so the average is the value at the middle of the interval.

(c) $V(t) = \int_0^t(6 - 0.5s)\,ds = 6t - 0.25t^2$, with $V(0) = 0$. By part 1 of the fundamental theorem, $V'(t) = 6 - 0.5t = r(t)$.

Check: $V(10) = 60 - 25 = 35$, which agrees with (a). The flow is positive over the whole interval ($r(10) = 1 > 0$), so the volume is increasing throughout.

</details>

### Challenge

7\. The region between $y = x$ and $y = x^2$ is turned about the $x$-axis (washers), and about the line $y = 1$. Find both volumes.

<details class="solution" markdown>
<summary>Solution</summary>

About the $x$-axis, the outer radius is $x$ and the inner radius is $x^2$: $V = \pi\int_0^1\left(x^2 - x^4\right)dx = \pi\left(\frac{1}{3} - \frac{1}{5}\right) = \frac{2\pi}{15}$.

About the line $y = 1$, a point at height $y$ is at distance $1 - y$ from the axis. The line $y = x$ is nearer to the axis than the parabola $y = x^2$ is (since $x \ge x^2$ means $1 - x \le 1 - x^2$), so the outer radius is $1 - x^2$ and the inner radius is $1 - x$:

$$
V = \pi\int_0^1\left[\left(1 - x^2\right)^2 - (1 - x)^2\right]dx = \pi\int_0^1\left(x^4 - 3x^2 + 2x\right)dx = \pi\left(\frac{1}{5} - 1 + 1\right) = \frac{\pi}{5}.
$$

Check: $\left(1 - x^2\right)^2 - (1 - x)^2 = 1 - 2x^2 + x^4 - 1 + 2x - x^2 = x^4 - 3x^2 + 2x$. A numerical sum of the two integrands gives $0.4189 = \frac{2\pi}{15}$ and $0.6283 = \frac{\pi}{5}$.

</details>

8\. A Lorenz curve is $L(x) = x^p$ for a constant $p > 1$. (a) Show that $G = \frac{p - 1}{p + 1}$. (b) Find $p$ so that $G = 0.4$, and say what share of income the poorest half receives.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $G = 1 - 2\int_0^1 x^p\,dx = 1 - \frac{2}{p + 1} = \frac{p - 1}{p + 1}$.

(b) Solve $\frac{p - 1}{p + 1} = 0.4$: $p - 1 = 0.4p + 0.4$, so $0.6p = 1.4$ and $p = \frac{7}{3} \approx 2.333$. The poorest half receives $L(0.5) = 0.5^{7/3} \approx 0.198$, about 19.8% of income.

Check: for $p = 2$ the formula gives $\frac{1}{3}$, as in Example 6, and for $p = 3$ it gives $\frac{1}{2}$. The value $p = \frac{7}{3}$ lies between 2 and 3, so $G = 0.4$ lies between $\frac{1}{3}$ and $\frac{1}{2}$, as it should. As $p \to 1$ the curve approaches the line of equality and $G \to 0$.

</details>

## Where this shows up

- In the rest of this folder, expected values and densities are the core of probability ([continuous random variables and the normal distribution](../07-probability/04-continuous-random-variables-and-the-normal.md)), and volumes and areas become double integrals ([double integrals](../09-multivariable-calculus-light/04-double-integrals.md)).
- In CS, the expected value of a continuous random variable is how average-case running times and expected losses are computed when inputs are drawn from a density. The slice-and-sum method is how a graphics program finds the volume of a mesh, and the Riemann sums of the first lesson are how a numerical integrator does all of the examples above.
- In economics and finance, surplus and the present value of income streams are integrals you meet in intermediate economics courses (surplus and market interventions<!-- link: ../../07-economics-math/02-markets/04-surplus-and-market-interventions.md -->, [present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md)), and the Gini coefficient is the standard summary of a Lorenz curve in studies of income inequality.
