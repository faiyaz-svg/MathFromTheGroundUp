# Double integrals

This lesson is optional. Read it if you want to see where the normal distribution's constant comes from, or how joint probability densities are used. The rest of the book doesn't depend on it, apart from that one proof.

After this lesson you can set up and evaluate a double integral as a volume, change the order of integration, use polar coordinates with the factor $r\,dr\,d\theta$, evaluate the Gaussian integral $\int_{-\infty}^{\infty}e^{-x^2}\,dx = \sqrt{\pi}$, and compute probabilities and expected values from a joint density.

Before this: [applications of integrals](../04-integrals/06-applications-of-integrals.md), [partial derivatives and the gradient](02-partial-derivatives-and-the-gradient.md), [parametric, polar and 3D coordinates](01-parametric-polar-and-3d-coordinates.md) and [determinants](../06-linear-algebra/06-determinants.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Evaluate $\int_0^3\int_0^2 xy\,dx\,dy$.
2. Evaluate $\int_0^1\int_0^x (x + y)\,dy\,dx$.
3. Find the area of the disc $x^2 + y^2 \le 4$ as an integral in polar coordinates.

<details class="solution" markdown>
<summary>Answers</summary>

1. The inner integral is $\int_0^2 xy\,dx = y\cdot\frac{x^2}{2}\Big|_0^2 = 2y$, and then $\int_0^3 2y\,dy = 9$.
2. The inner integral is $\int_0^x (x + y)\,dy = x^2 + \frac{x^2}{2} = \frac{3x^2}{2}$, and then $\int_0^1\frac{3x^2}{2}\,dx = \frac{1}{2}$.
3. $\int_0^{2\pi}\int_0^2 r\,dr\,d\theta = 2\pi \cdot 2 = 4\pi$, which is $\pi r^2$ for $r = 2$.

</details>

## The idea

The integral of a function of one variable is the area under a curve, built by cutting the interval into thin strips and adding. A function of two variables $f(x, y) \ge 0$ is the height of a surface above the plane, and the integral should be the volume under the surface. The idea is the same one with one more dimension. Cut the region of the plane into small rectangles of area $\Delta A$, build a thin column on each with the height of the surface at some point of the rectangle, and add up the volumes of the columns. As the rectangles shrink the sum approaches a number, the double integral.

Adding the columns in a clever order turns the problem into two ordinary integrals. Add up the columns along one strip first, to get the cross-sectional area of a slice of the solid. Then add up the slices. This is the volume-by-slices idea of [applications of integrals](../04-integrals/06-applications-of-integrals.md), and it is called an iterated integral. The skill of the lesson is the set-up: sketching the region, choosing the order, and writing the limits. Sometimes the order matters a lot. An integral that has no formula in one order can be easy in the other.

Many regions are round. For these, rectangles are the wrong shapes, and polar coordinates give better ones: small pieces of rings. The area of such a piece involves a factor $r$ that is easy to forget and easy to explain. Polar coordinates also solve a famous problem. The function $e^{-x^2}$ has no antiderivative in terms of the usual functions, yet the integral over the whole line has an exact value, $\sqrt{\pi}$, and the proof is a double integral.

![The triangle with vertices (0, 0), (0, 1) and (1, 1), bounded by x = 0, y = 1 and y = x, sliced two ways. On the left, vertical red strips run from the line y = x up to y = 1, so the inner integral is over y from x to 1 and the outer one over x from 0 to 1. On the right, horizontal blue strips run from x = 0 to the line y = x, so the inner integral is over x from 0 to y and the outer one over y from 0 to 1.](../../assets/figures/05-university-core/double-integrals-region.svg)

## Definitions

Let $R$ be a closed, bounded region of the plane and $f$ a function on $R$. Cut $R$ into small rectangles of area $\Delta A_i$, choose a point $(x_i, y_i)$ in each, and form the Riemann sum $\sum f(x_i, y_i)\,\Delta A_i$. The **double integral** of $f$ over $R$ is the limit of these sums as the rectangles shrink, if the limit exists,

$$
\iint_R f(x, y)\,dA = \lim\sum f(x_i, y_i)\,\Delta A_i.
$$

It exists for every continuous $f$ on a region with a reasonable boundary. In plain words, it is the signed volume between the surface $z = f(x, y)$ and the plane $z = 0$ over $R$, with volume below the plane counted as negative. When $f = 1$ the sum is the area of $R$, so $\iint_R 1\,dA = \text{area}(R)$.

The **average value** of $f$ on $R$ is $\frac{1}{\text{area}(R)}\iint_R f\,dA$, as in the one-variable lesson.

An **iterated integral** is a pair of one-variable integrals done one after the other. For the rectangle $R = [a, b] \times [c, d]$ the two orders are

$$
\int_a^b\left(\int_c^d f(x, y)\,dy\right)dx \qquad\text{and}\qquad \int_c^d\left(\int_a^b f(x, y)\,dx\right)dy.
$$

In plain words, the inner integral treats the other variable as a constant, as in a partial derivative, and leaves a function of the outer variable.

A region of **type I** is $a \le x \le b$ with $g_1(x) \le y \le g_2(x)$: between two curves, described by vertical strips. A region of **type II** is $c \le y \le d$ with $h_1(y) \le x \le h_2(y)$, described by horizontal strips.

In polar coordinates a **polar rectangle** is $\{r_1 \le r \le r_2,\ \theta_1 \le \theta \le \theta_2\}$, a piece of a ring.

A **joint probability density** of two random variables $X$ and $Y$ is a function $f(x, y) \ge 0$ with $\iint f\,dA = 1$ over the plane, such that $P\bigl((X, Y) \in R\bigr) = \iint_R f\,dA$. In plain words, probabilities are volumes under the density surface.

## How to do it

### Iterated integrals and Fubini's theorem

*Fubini's theorem* (stated without proof): if $f$ is continuous on the rectangle $R = [a, b] \times [c, d]$, then both iterated integrals exist and equal the double integral, so they equal each other:

$$
\iint_R f\,dA = \int_a^b\int_c^d f(x, y)\,dy\,dx = \int_c^d\int_a^b f(x, y)\,dx\,dy.
$$

The idea behind it is the slicing argument: for each $x$, the inner integral is the area of the slice of the solid at $x$, and the outer integral adds the slices. Cutting the other way gives the other order, and both count the same volume. For type I and type II regions the theorem still holds with the inner limits depending on the outer variable.

### Setting up a double integral

1. Sketch the region $R$. Mark the curves that bound it and where they cross.
2. Choose an order. Vertical strips (inner $dy$) suit a region described by $y$ between two curves. Horizontal strips (inner $dx$) suit one described by $x$ between two curves. Prefer the order in which the inner integral has an antiderivative and the limits need no splitting.
3. Write the limits. The outer variable has constant limits, the full range of the region. The inner variable has limits that are functions of the outer variable (or constants), found by drawing one strip.
4. Integrate the inner integral, holding the outer variable constant, and then the outer integral.
5. Check. Replace $f$ by $1$ and see whether you get the area. Estimate the answer from the area of $R$ times a typical value of $f$. If possible, do the other order.

### Changing the order of integration

For a type I region, draw the region and re-describe it as type II. For the triangle in the figure, vertical strips give $0 \le x \le 1$ and $x \le y \le 1$. Horizontal strips give $0 \le y \le 1$ and $0 \le x \le y$. So

$$
\int_0^1\int_x^1 f\,dy\,dx = \int_0^1\int_0^y f\,dx\,dy.
$$

The limits are found from the picture and not by solving formulas, and the picture is what stops the usual mistakes.

### Polar coordinates and the factor $r$

*Theorem 1 (area in polar coordinates).* If $R$ is the region $\alpha \le \theta \le \beta$, $r_1(\theta) \le r \le r_2(\theta)$, then

$$
\iint_R f(x, y)\,dA = \int_\alpha^\beta\int_{r_1(\theta)}^{r_2(\theta)} f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta.
$$

What we know: a polar rectangle with $\Delta r$ and $\Delta\theta$ small. What we want: its area. The plan: it is almost an ordinary rectangle, and we find its two sides.

*Proof sketch.* The piece between the rings $r$ and $r + \Delta r$ and the rays $\theta$ and $\theta + \Delta\theta$ has a radial side of length $\Delta r$ and an arc side of length about $r\,\Delta\theta$ (an arc of angle $\Delta\theta$ on a circle of radius $r$). It is nearly a rectangle, so $\Delta A \approx r\,\Delta r\,\Delta\theta$. Replacing $dA$ by $r\,dr\,d\theta$ in the limit of the Riemann sums gives the formula. $\blacksquare$

Look back: the factor $r$ is the reason that a polar integral is not just $f\,dr\,d\theta$. The pieces far from the origin are bigger than those near it, for the same $\Delta r$ and $\Delta\theta$. The area of a disc checks it: $\int_0^{2\pi}\int_0^a r\,dr\,d\theta = \pi a^2$.

![A quarter of the plane drawn with polar grid lines, circles r = 1, 2 and 3 and rays every 15 degrees. One small patch between two circles and two rays is shaded red. Its radial side is labelled dr, its arc side labelled r d theta, and the patch labelled with its area, approximately r dr d theta.](../../assets/figures/05-university-core/double-integrals-polar.svg)

The factor $r$ is also a determinant. The change of variables $x = r\cos\theta$, $y = r\sin\theta$ has the matrix of partial derivatives

$$
J = \begin{pmatrix} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\[2pt] \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} \end{pmatrix} = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix}, \qquad \det J = r\cos^2\theta + r\sin^2\theta = r.
$$

A small rectangle $\Delta r \times \Delta\theta$ is sent by the map to a piece that is, to first order, the image of the rectangle under the linear map $J$. By the [determinants lesson](../06-linear-algebra/06-determinants.md), a linear map scales areas by $\lvert \det \rvert$, so the piece has area $\lvert \det J \rvert\,\Delta r\,\Delta\theta = r\,\Delta r\,\Delta\theta$. In general, for a change of variables $x = x(u, v)$, $y = y(u, v)$ the double integral becomes $\iint f\,\lvert \det J \rvert\,du\,dv$ (stated). The number $\lvert \det J \rvert$ is called the **Jacobian**.

### The Gaussian integral

*Theorem 2.* $\displaystyle\int_{-\infty}^{\infty}e^{-x^2}\,dx = \sqrt{\pi}$.

What we know: the integral $I = \int_{-\infty}^{\infty}e^{-x^2}\,dx$ is a positive number (the integrand is positive), and the integrals of the chapter on integrals can't find it, because $e^{-x^2}$ has no elementary antiderivative. What we want: its value. The plan, which looks odd until it works, is to square it. The product of two copies of the integral is a double integral over the whole plane, and in the plane the function $e^{-x^2 - y^2}$ depends only on the distance from the origin, which is what polar coordinates are for.

*Proof.* Using $y$ as the variable in the second copy and Fubini's theorem (for improper integrals of a positive function),

$$
I^2 = \int_{-\infty}^{\infty}e^{-x^2}\,dx\int_{-\infty}^{\infty}e^{-y^2}\,dy = \iint_{\mathbb{R}^2}e^{-(x^2 + y^2)}\,dA.
$$

In polar coordinates the whole plane is $0 \le \theta \le 2\pi$, $0 \le r < \infty$, and $x^2 + y^2 = r^2$, so by Theorem 1

$$
I^2 = \int_0^{2\pi}\int_0^\infty e^{-r^2}\,r\,dr\,d\theta = 2\pi\int_0^\infty e^{-r^2}\,r\,dr.
$$

With the substitution $u = r^2$, $du = 2r\,dr$, the last integral is $\frac{1}{2}\int_0^\infty e^{-u}\,du = \frac{1}{2}$. So $I^2 = 2\pi \cdot \frac{1}{2} = \pi$, and since $I > 0$, $I = \sqrt{\pi}$. $\blacksquare$

Look back: the factor $r$ from the polar area is exactly what makes $e^{-r^2}r$ integrable by substitution. Without it the proof would fail, and the problem in the plane is easier than the problem on the line. Check: the numerical value is $\sqrt{\pi} \approx 1.7725$, and a midpoint sum of $e^{-x^2}$ gives the same (the code below).

*Consequence.* The substitution $z = \sqrt{2}\,x$ turns the theorem into $\int_{-\infty}^{\infty}e^{-z^2/2}\,dz = \sqrt{2\pi}$. This is the fact that the normal density

$$
\frac{1}{\sqrt{2\pi}}e^{-z^2/2}
$$

has total area 1, which [continuous random variables and the normal distribution](../07-probability/04-continuous-random-variables-and-the-normal.md) used without proof.

![Two three-dimensional surfaces. On the left, the cap z = 4 minus x squared minus y squared over the disc of radius 2 in the plane, a smooth dome of height 4 whose volume is 8 pi. On the right, the bell z = e to the minus (x squared plus y squared), a tall narrow peak of height 1 over the plane whose volume is pi.](../../assets/figures/05-university-core/double-integrals-solids.svg)

### Joint densities

For a joint density $f(x, y)$ of $X$ and $Y$:

- the probability of an event is the integral of $f$ over the region of the plane where it happens,
- the density of $X$ alone is found by integrating out $y$, $f_X(x) = \int f(x, y)\,dy$, and likewise for $Y$,
- the expected value of a function is $E[g(X, Y)] = \iint g(x, y)\,f(x, y)\,dA$, in particular $E[X] = \iint xf\,dA$,
- $X$ and $Y$ are independent exactly when $f(x, y) = f_X(x)f_Y(y)$.

The lesson on [joint distributions, covariance and sums](../07-probability/05-joint-distributions-covariance-and-sums.md) uses these facts.

## Worked examples

<div class="example" markdown>

### Example 1: a double integral over a rectangle, in both orders

Find the volume under $z = x^2y$ over the rectangle $0 \le x \le 2$, $1 \le y \le 3$.

Step 1 and 2: the region is a rectangle, so either order works. Take $dx$ first.

Step 3 and 4: the inner integral, with $y$ held constant, is $\int_0^2 x^2y\,dx = y\cdot\frac{8}{3}$. Then the outer integral is $\int_1^3\frac{8y}{3}\,dy = \frac{8}{3}\cdot\frac{9 - 1}{2} = \frac{32}{3}$.

Step 5, the check in the other order: the inner integral $\int_1^3 x^2y\,dy = x^2\cdot\frac{9 - 1}{2} = 4x^2$, and $\int_0^2 4x^2\,dx = \frac{32}{3}$, the same. A second check by averages: the average of $x^2$ on $[0, 2]$ is $\frac{4}{3}$ and the average of $y$ on $[1, 3]$ is $2$, and for a product these multiply, so the integral is $4 \cdot \frac{4}{3} \cdot 2 = \frac{32}{3}$, where $4$ is the area of the rectangle. In general, for $g(x)h(y)$ over a rectangle the double integral is the product of the two one-variable integrals, here $\frac{8}{3} \cdot 4$.

</div>

<div class="example" markdown>

### Example 2: an integral that needs the order changed

Evaluate $\displaystyle\int_0^1\int_x^1 e^{y^2}\,dy\,dx$.

The inner integral $\int e^{y^2}\,dy$ has no elementary antiderivative, so the iterated integral can't be done as written. The limits describe the triangle $0 \le x \le 1$, $x \le y \le 1$, which is the triangle of the first figure. In the other order the same region is $0 \le y \le 1$, $0 \le x \le y$, so

$$
\int_0^1\int_x^1 e^{y^2}\,dy\,dx = \int_0^1\int_0^y e^{y^2}\,dx\,dy = \int_0^1 y\,e^{y^2}\,dy = \frac{1}{2}\left(e - 1\right) \approx 0.8591.
$$

The inner integral is $\int_0^y e^{y^2}\,dx = y\,e^{y^2}$ because $e^{y^2}$ is a constant with respect to $x$. The outer integral uses $u = y^2$.

Check: the triangle has area $\frac{1}{2}$, and $e^{y^2}$ ranges from $1$ to $e \approx 2.72$ over it, so the answer lies between $0.5$ and $1.36$, and $0.86$ does. The numerical midpoint sum below gives $0.8591$.

</div>

<div class="example" markdown>

### Example 3: a volume in polar coordinates

Find the volume under $z = 4 - x^2 - y^2$ and above the disc $x^2 + y^2 \le 4$.

In polar coordinates the surface is $z = 4 - r^2$ and the disc is $0 \le r \le 2$, $0 \le \theta \le 2\pi$. By Theorem 1,

$$
V = \int_0^{2\pi}\int_0^2 (4 - r^2)\,r\,dr\,d\theta = 2\pi\left[2r^2 - \frac{r^4}{4}\right]_0^2 = 2\pi(8 - 4) = 8\pi \approx 25.13.
$$

Check: the solid is a dome of height 4 over a disc of area $4\pi$. A cylinder of the same base and height has volume $16\pi$, and a cone has $\frac{16\pi}{3}$. The paraboloid's volume $8\pi$ is exactly half the cylinder, and between the cone and the cylinder, as it should be. The numerical grid sum below gives $25.13$.

</div>

<div class="example" markdown>

### Example 4: the distance of a random point from the origin

Let $X$ and $Y$ be independent standard normal variables, so the joint density is the product $\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\cdot\frac{1}{\sqrt{2\pi}}e^{-y^2/2} = \frac{1}{2\pi}e^{-(x^2 + y^2)/2}$. Find the probability that the point $(X, Y)$ is within distance $\rho$ of the origin.

The region is the disc $r \le \rho$. In polar coordinates

$$
P = \int_0^{2\pi}\int_0^\rho \frac{1}{2\pi}e^{-r^2/2}\,r\,dr\,d\theta = \int_0^\rho e^{-r^2/2}\,r\,dr = 1 - e^{-\rho^2/2}.
$$

With $\rho \to \infty$ this tends to 1, confirming that the density has total area 1. For $\rho = 1$ the probability is $1 - e^{-1/2} \approx 0.3935$, and the median distance is where $1 - e^{-\rho^2/2} = \frac{1}{2}$, so $\rho = \sqrt{2\ln 2} \approx 1.1774$.

Check: a simulation with a million points (below, with a fixed seed) finds $0.393$ of them within distance 1. Also, the probability that each coordinate is in $[-1, 1]$ is $0.6827^2 = 0.466$, the probability for the square, and the disc inside the square has smaller probability, $0.3935$.

</div>

<div class="example" markdown>

### Example 5: a joint density

The joint density of $X$ and $Y$ is $f(x, y) = 8xy$ on the triangle $0 \le y \le x \le 1$ and $0$ elsewhere. Check that it is a density, then find $P(X + Y \le 1)$, the density of $X$ and $E[X]$.

Total: $\int_0^1\int_0^x 8xy\,dy\,dx = \int_0^1 8x\cdot\frac{x^2}{2}\,dx = \int_0^1 4x^3\,dx = 1$. So $f$ is a density. The inner integral is also the density of $X$: $f_X(x) = \int_0^x 8xy\,dy = 4x^3$ for $0 \le x \le 1$.

For $P(X + Y \le 1)$, the region is the part of the triangle below the line $y = 1 - x$. For $0 \le x \le \frac{1}{2}$ the line is above $y = x$, so $y$ runs from $0$ to $x$. For $\frac{1}{2} \le x \le 1$ the line is lower, so $y$ runs from $0$ to $1 - x$. Then

$$
P = \int_0^{1/2}4x^3\,dx + \int_{1/2}^1 4x(1 - x)^2\,dx = \frac{1}{16} + \frac{5}{48} = \frac{1}{6}.
$$

For the expected value, $E[X] = \int_0^1 x\cdot 4x^3\,dx = \frac{4}{5}$. The same value comes from the double integral $\int_0^1\int_0^x x\cdot 8xy\,dy\,dx = \int_0^1 4x^4\,dx = \frac{4}{5}$.

Check: the density $8xy$ is largest near $(1, 1)$, so a value of $E[X]$ near 1, such as $0.8$, is believable. The event $X + Y \le 1$ stays near the origin where the density is small, so a probability of $\frac{1}{6}$ is plausible. The grid sum below gives $1.0$ and $0.1667$.

</div>

<div class="example" markdown>

### Example 6: change the order and finish (finish it yourself)

Evaluate $\displaystyle\int_0^2\int_{x/2}^1 e^{y^2}\,dy\,dx$ by changing the order.

The region is $0 \le x \le 2$ and $\frac{x}{2} \le y \le 1$, a triangle with vertices $(0, 0)$, $(0, 1)$ and $(2, 1)$. Horizontal strips run from $x = 0$ to the line $y = \frac{x}{2}$, that is $x = 2y$, for $0 \le y \le 1$.

<details class="solution" markdown>
<summary>Finish</summary>

$$
\int_0^1\int_0^{2y}e^{y^2}\,dx\,dy = \int_0^1 2y\,e^{y^2}\,dy = \left[e^{y^2}\right]_0^1 = e - 1 \approx 1.718.
$$

Check: the triangle has area $\frac{1}{2} \cdot 2 \cdot 1 = 1$, and $e^{y^2}$ is between $1$ and $e$, so the integral should be between $1$ and $2.72$. It is also exactly twice Example 2's answer, $2 \cdot 0.8591 = 1.718$, because the triangle is twice as wide (the same height and a base of 2 instead of 1).

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: limits in the wrong places. The outer limits must be numbers, and the inner limits may use the outer variable but never the inner one. In $\int_0^1\int_x^1 \dots\,dy\,dx$ the inner limits $x$ and $1$ are fine, because $x$ is the outer variable. A limit such as $\int_0^y\int_0^1\dots\,dy\,dx$ is nonsense, since the answer of a finished integral can't still depend on the variable it was integrated over.

</div>

<div class="warning" markdown>

Watch out: changing the order without drawing the region. Swapping the numbers $0, 1, x, 1$ to get $\int_x^1\int_0^1$ is not the same region. Sketch, draw one strip in the new direction, and read off the new limits (Example 2).

</div>

<div class="warning" markdown>

Watch out: forgetting the $r$ in polar coordinates. Computing $\int_0^{2\pi}\int_0^a 1\,dr\,d\theta$ gives $2\pi a$, the circumference, and not the area $\pi a^2$. Every polar double integral has $r\,dr\,d\theta$.

</div>

<div class="warning" markdown>

Watch out: the polar ranges. For the disc, $0 \le \theta \le 2\pi$ and $0 \le r \le a$. For a disc that is not centred at the origin, such as the one bounded by $r = 2\cos\theta$ (the circle through the origin of the first lesson), $\theta$ runs only over $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$ and $r$ from $0$ to $2\cos\theta$. Sketch the region and find where a ray from the origin enters and leaves it.

</div>

<div class="warning" markdown>

Watch out: a negative integrand gives a negative contribution. The double integral is a signed volume, like a signed area. For the area or total mass, integrate a positive function, and for the volume of a solid that goes below the plane, split the region at the curve where $f = 0$.

</div>

The theorems need some care at infinity. Fubini's theorem and the polar substitution were used in the Gaussian proof on a positive function over the whole plane, which is safe because a positive function can be integrated in any order. For a function that changes sign, an improper double integral needs checking before the order is swapped.

## Tricks and shortcuts

If $f(x, y) = g(x)h(y)$ and the region is a rectangle, the double integral is the product $\int g\,dx \cdot \int h\,dy$. Example 1 is of this kind.

Use symmetry. For a region symmetric about the $y$-axis and a function with $f(-x, y) = f(x, y)$, integrate over the right half and double. For an odd function ($f(-x, y) = -f(x, y)$) the integral over a symmetric region is $0$.

Pick polar coordinates when the region is a disc, a sector or a ring, or when the integrand depends on $x^2 + y^2$. Staying in Cartesian coordinates would turn the limits into square roots.

A quick check for any region integral: the integral lies between $\text{area} \times \min f$ and $\text{area} \times \max f$.

## In code

A midpoint sum is a double integral in code. It checks Examples 2, 3 and 5, the Gaussian integral of Theorem 2, and the simulation of Example 4. (Cell centres exactly on an edge of a region count for half, which removes a bias from the edge.)

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import numpy as np

# A midpoint sum over an n-by-n grid of cells on the unit square. A cell centre exactly
# on the edge of the region counts for half.
n = 2000
h = 1 / n
mid = (np.arange(n) + 0.5) * h
X, Y = np.meshgrid(mid, mid)

def weight(gap):
    """1 where gap > 0, one half where gap == 0, 0 where gap < 0."""
    return np.where(gap > 1e-12, 1.0, np.where(gap > -1e-12, 0.5, 0.0))

# The integral of e^(y^2) over the triangle 0 <= x <= y <= 1 (exact: (e - 1)/2).
print(round(np.sum(np.exp(Y**2) * weight(Y - X)) * h * h, 4), round((math.e - 1) / 2, 4))
# 0.8591 0.8591

# The density f(x, y) = 8xy on 0 <= y <= x <= 1: total and P(X + Y <= 1).
f = 8 * X * Y * weight(X - Y)
print(round(np.sum(f) * h * h, 4), round(np.sum(f * weight(1 - X - Y)) * h * h, 4))
# 1.0 0.1667

# Volume under z = 4 - x^2 - y^2 over the disc r <= 2 (exact: 8 pi), on a grid of cells.
m = 4000
g = (np.arange(m) + 0.5) * 4 / m - 2
GX, GY = np.meshgrid(g, g)
r2 = GX**2 + GY**2
vol = np.sum((4 - r2)[r2 <= 4]) * (4 / m) ** 2
print(round(vol, 2), round(8 * math.pi, 2))
# 25.13 25.13

# The Gaussian integral: (integral of e^(-x^2))^2 should be pi.
x = np.linspace(-10, 10, 2_000_001)
I = np.sum(np.exp(-x**2)) * (x[1] - x[0])
print(round(I**2, 6), round(math.pi, 6))
# 3.141593 3.141593

# Two independent standard normals: P(distance from the origin <= 1), exact 1 - e^(-1/2).
rng = np.random.default_rng(0)
pts = rng.standard_normal((1_000_000, 2))
print(round(np.mean(np.hypot(pts[:, 0], pts[:, 1]) <= 1), 3), round(1 - math.exp(-0.5), 3))
# 0.393 0.393
```

The squared one-variable sum equals $\pi$ to six places, which is the numerical face of Theorem 2.

</details>

## FAQ

### Why does the order of integration not matter?

For a continuous function on a rectangle (and on the usual regions), both orders compute the same volume, cut into slices in two different directions. That is Fubini's theorem. What does matter is the effort: one order can have an inner integral you can't do, as in Example 2.

### Why is the area element $r\,dr\,d\theta$ and not $dr\,d\theta$?

Because $\Delta\theta$ is an angle and not a length. A step of $\Delta\theta$ moves you along an arc of length $r\,\Delta\theta$, longer for larger $r$. The patch with sides $\Delta r$ and $r\,\Delta\theta$ has area $r\,\Delta r\,\Delta\theta$. The determinant of the change of variables, $\det J = r$, says the same thing.

### How can the integral of $e^{-x^2}$ be known exactly if it has no antiderivative?

Having no antiderivative made of elementary functions only means that no formula for $\int_a^b e^{-x^2}\,dx$ exists in terms of the usual functions for general $a$ and $b$. The integral over the whole line is a different thing, a single number, and the trick of squaring it and using symmetry in the plane finds it exactly. The same function's integral from $0$ to $x$ is the error function, which software computes numerically.

### Is the double integral the same as two single integrals?

Only when the integrand is a product of a function of $x$ and a function of $y$ and the region is a rectangle. In general the inner integral depends on the outer variable, and you can't separate them.

## Practice

### Warm-up

1\. Evaluate $\iint_R (x + 2y)\,dA$ over $R = [0, 1] \times [0, 2]$, in both orders.

<details class="solution" markdown>
<summary>Solution</summary>

With $dy$ first, $\int_0^2 (x + 2y)\,dy = 2x + 4$, and $\int_0^1 (2x + 4)\,dx = 1 + 4 = 5$. With $dx$ first, $\int_0^1 (x + 2y)\,dx = \frac{1}{2} + 2y$, and $\int_0^2\left(\frac{1}{2} + 2y\right)dy = 1 + 4 = 5$.

Check: the two orders agree, and the average of $x + 2y$ over the rectangle (area 2) is $\frac{5}{2} = 2.5$, which is its value at the centre $(0.5, 1)$: $0.5 + 2 = 2.5$.

</details>

2\. Find $\iint_R xy\,dA$ over the region between $y = x^2$ and $y = x$ for $0 \le x \le 1$.

<details class="solution" markdown>
<summary>Solution</summary>

On $[0, 1]$ the line $y = x$ is above $y = x^2$, so $y$ runs from $x^2$ to $x$. Then $\int_{x^2}^x xy\,dy = x\cdot\frac{x^2 - x^4}{2}$, and $\int_0^1\frac{x^3 - x^5}{2}\,dx = \frac{1}{2}\left(\frac{1}{4} - \frac{1}{6}\right) = \frac{1}{24}$.

Check: the area of the region is $\int_0^1 (x - x^2)\,dx = \frac{1}{6}$, and $xy$ is between $0$ and $1$ there (about $\frac{1}{4}$ at most, near the middle), so $\frac{1}{24} = \frac{1}{6} \cdot \frac{1}{4}$ is in the right range.

</details>

3\. Change the order and evaluate $\displaystyle\int_0^2\int_x^2 e^{-y^2}\,dy\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

The region is $0 \le x \le 2$, $x \le y \le 2$, the triangle under $y = 2$ and above $y = x$. In the other order, $0 \le y \le 2$ and $0 \le x \le y$, so the integral is $\int_0^2\int_0^y e^{-y^2}\,dx\,dy = \int_0^2 y\,e^{-y^2}\,dy = \left[-\frac{1}{2}e^{-y^2}\right]_0^2 = \frac{1 - e^{-4}}{2} \approx 0.4908$.

Check: the triangle has area $2$ and $e^{-y^2}$ is close to $0$ for most of the triangle ($y > 1$ has $e^{-y^2} < 0.37$), so a value below $1$ is expected. It is also just under $\int_0^\infty y\,e^{-y^2}\,dy = \frac{1}{2}$, as it should be.

</details>

### Standard

4\. (a) Integrate $x^2 + y^2$ over the disc $r \le 3$. (b) Find the area of the ring $1 \le r \le 2$ with an integral.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\int_0^{2\pi}\int_0^3 r^2\cdot r\,dr\,d\theta = 2\pi\cdot\frac{3^4}{4} = \frac{81\pi}{2} \approx 127.2$.

(b) $\int_0^{2\pi}\int_1^2 r\,dr\,d\theta = 2\pi\cdot\frac{4 - 1}{2} = 3\pi$.

Check: (b) is $\pi \cdot 2^2 - \pi \cdot 1^2 = 3\pi$. For (a), the average of $x^2 + y^2 = r^2$ over a disc of radius $3$ is $\frac{81\pi/2}{9\pi} = 4.5$, which is $\frac{R^2}{2}$ for $R = 3$, between $0$ and the largest value $9$.

</details>

5\. Use a double integral in polar coordinates to find the volume of a sphere of radius $R$, as twice the volume under the hemisphere $z = \sqrt{R^2 - x^2 - y^2}$.

<details class="solution" markdown>
<summary>Solution</summary>

Over the disc $r \le R$ the hemisphere has height $\sqrt{R^2 - r^2}$. The volume under it is

$$
\int_0^{2\pi}\int_0^R\sqrt{R^2 - r^2}\,r\,dr\,d\theta = 2\pi\left[-\frac{1}{3}\left(R^2 - r^2\right)^{3/2}\right]_0^R = 2\pi\cdot\frac{R^3}{3} = \frac{2\pi R^3}{3}.
$$

The sphere has twice this volume, $\frac{4}{3}\pi R^3$.

Check: this is the formula for the volume of a sphere. For $R = 1$ the hemisphere has volume $\frac{2\pi}{3} \approx 2.094$, between the cone of the same base and height ($\frac{\pi}{3}$) and the cylinder ($\pi$).

</details>

6\. Let $X$ and $Y$ be independent with the joint density $f(x, y) = e^{-x - y}$ for $x, y \ge 0$. Find $P(X < Y)$ and $P(X + Y \le 1)$.

<details class="solution" markdown>
<summary>Solution</summary>

For $P(X < Y)$ the region is $0 \le x < y$: $\int_0^\infty\int_x^\infty e^{-x-y}\,dy\,dx = \int_0^\infty e^{-x}\cdot e^{-x}\,dx = \frac{1}{2}$. For $P(X + Y \le 1)$ the region is $0 \le x \le 1$, $0 \le y \le 1 - x$: $\int_0^1 e^{-x}\left(1 - e^{-(1 - x)}\right)dx = \int_0^1 \left(e^{-x} - e^{-1}\right)dx = (1 - e^{-1}) - e^{-1} = 1 - \frac{2}{e} \approx 0.2642$.

Check: $P(X < Y) = \frac{1}{2}$ by symmetry (the density is symmetric in $x$ and $y$ and ties have probability $0$). For the second, the triangle $x + y \le 1$ has area $\frac{1}{2}$ and the density is between $e^{-1} \approx 0.37$ and $1$ on it, so the probability is between $0.18$ and $0.5$, and $0.26$ fits.

</details>

### Challenge

7\. (a) Show that $\int_{-\infty}^{\infty}e^{-x^2/(2\sigma^2)}\,dx = \sigma\sqrt{2\pi}$ for $\sigma > 0$, so that $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x - \mu)^2/(2\sigma^2)}$ has total area 1. (b) Show that a standard normal variable has variance 1, that is, $\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}z^2e^{-z^2/2}\,dz = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Substitute $x = \sigma z$, so $dx = \sigma\,dz$. The integral is $\sigma\int_{-\infty}^\infty e^{-z^2/2}\,dz = \sigma\sqrt{2\pi}$ by the consequence of Theorem 2. The shift by $\mu$ doesn't change the area of a function over the whole line, so the density has total area $\frac{\sigma\sqrt{2\pi}}{\sigma\sqrt{2\pi}} = 1$.

(b) Integrate by parts with $u = z$ and $dv = z\,e^{-z^2/2}\,dz$, so that $v = -e^{-z^2/2}$:

$$
\int_{-\infty}^\infty z\cdot z\,e^{-z^2/2}\,dz = \left[-z\,e^{-z^2/2}\right]_{-\infty}^{\infty} + \int_{-\infty}^\infty e^{-z^2/2}\,dz = 0 + \sqrt{2\pi}.
$$

The boundary term is $0$ because $z\,e^{-z^2/2} \to 0$ at both ends. Dividing by $\sqrt{2\pi}$ gives $1$.

Check: since the mean is $0$ (the integrand $z\,e^{-z^2/2}$ is odd), the variance is $E[Z^2] - 0 = 1$, as the standard normal should have.

</details>

8\. (Reviews [determinants](../06-linear-algebra/06-determinants.md).) The parallelogram $P$ with vertices $(0, 0)$, $(2, 1)$, $(3, 4)$ and $(1, 3)$ is the image of the unit square under $x = 2u + v$, $y = u + 3v$. Find the Jacobian of the map, the area of $P$, and $\iint_P x\,dA$.

<details class="solution" markdown>
<summary>Solution</summary>

The matrix of partial derivatives is $\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ with determinant $6 - 1 = 5$, so the Jacobian is $5$ and the area of $P$ is $5 \cdot 1 = 5$. For the integral, $\iint_P x\,dA = \int_0^1\int_0^1 (2u + v)\cdot 5\,du\,dv = 5\left(2\cdot\frac{1}{2} + \frac{1}{2}\right) = \frac{15}{2}$.

Check: the integral of $x$ is the area times the average $x$ over $P$. The centre of the parallelogram is the average of its vertices, $x = \frac{0 + 2 + 3 + 1}{4} = 1.5$, and $5 \cdot 1.5 = 7.5$.

</details>

## Where this shows up

- The lesson on [joint distributions, covariance and sums](../07-probability/05-joint-distributions-covariance-and-sums.md) uses joint densities, and the proof of the normal curve's constant in [continuous random variables and the normal distribution](../07-probability/04-continuous-random-variables-and-the-normal.md) is Theorem 2 here.
- In CS, double integrals appear in image processing (a blur is an integral against a Gaussian), in graphics (area and volume), and in probabilistic machine learning, where the Gaussian integral is the reason that Gaussian models have closed forms.
- In economics, a double integral adds a quantity over a population that varies in two ways, such as total consumer surplus over a distribution of income and preferences, or the expected value of a function of two uncertain variables.
