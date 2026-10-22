# Parametric, polar and 3D coordinates

This lesson is optional. Read it if parametric curves, polar coordinates or three-dimensional pictures are new to you, and skip to [partial derivatives and the gradient](02-partial-derivatives-and-the-gradient.md) if they are not.

After this lesson you can describe a curve by a parameter and find its velocity and slope, convert between polar and Cartesian coordinates, find an area in polar form, measure distances and write planes and spheres in three dimensions, and read a surface $z = f(x, y)$ as a contour map.

Before this: [the chain rule](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md), [radians and the unit circle](../../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md) and [vectors in the plane](../../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md). The area formula uses [applications of integrals](../04-integrals/06-applications-of-integrals.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A curve is given by $x = t^2$ and $y = t^3$. Find $\frac{dy}{dx}$ at $t = 1$.
2. Convert the polar point $(r, \theta) = \left(4, \frac{2\pi}{3}\right)$ to Cartesian coordinates.
3. Find the distance between the points $(1, 2, 3)$ and $(4, -2, 15)$.

<details class="solution" markdown>
<summary>Answers</summary>

1. Divide the rates of change: $\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{3t^2}{2t} = \frac{3t}{2}$, which is $\frac{3}{2}$ at $t = 1$.
2. $x = 4\cos\frac{2\pi}{3} = -2$ and $y = 4\sin\frac{2\pi}{3} = 2\sqrt{3} \approx 3.464$.
3. The differences are $(3, -4, 12)$, so the distance is $\sqrt{9 + 16 + 144} = 13$.

</details>

## The idea

A ball is thrown across a field. Its path is a curve, but a curve in the plane doesn't say when the ball is where. If you record the horizontal position $x = 20t$ metres and the height $y = 15t - 4.9t^2$ metres at each time $t$ in seconds, you have the whole story: the path, the speed and the landing time. Each of $x$ and $y$ is a function of the third variable $t$, the **parameter**, and the pair $(x(t), y(t))$ traces out the curve.

Two other descriptions of the plane come up all the time. Polar coordinates give a point by its distance from the origin and the angle of its direction, and they make circles, spirals and petals into one-line equations. Three-dimensional coordinates add a height, so that a function of two variables $z = f(x, y)$ becomes a surface, such as a hill whose height depends on where you stand. A surface is hard to draw. A contour map, the one a hiker carries, shows the same hill with curves joining points of equal height.

![The path of a thrown ball, x = 20t and y = 15t minus 4.9 t squared, with red velocity arrows at t = 0, 1, 2 and 3 seconds. The arrows lean up at the start, run level at the top near t = 1.53, and point down at the end. The ball lands at t about 3.06 and x about 61.2 metres.](../../assets/figures/05-university-core/parametric-polar-and-3d-coordinates-projectile.svg)

This lesson sets up the three tools. The next lesson uses them: a gradient is a vector that lives on the contour map of a surface, and the path of a hiker or of a learning algorithm is a parametric curve.

## Definitions

A **parametric curve** in the plane is a pair of functions $x = x(t)$ and $y = y(t)$ of a parameter $t$ in an interval. The point $(x(t), y(t))$ is the position at parameter $t$. In plain words, the parameter is a clock, and the curve is where the point goes as the clock runs. Many parameters give one curve: $x = \cos t$, $y = \sin t$ for $0 \le t \le 2\pi$ is the unit circle traced once, and $x = \cos 2t$, $y = \sin 2t$ traces it twice as fast.

The **velocity** at $t$ is the vector $\mathbf{v}(t) = (x'(t), y'(t))$ of the derivatives, and the **speed** is its length $\sqrt{x'(t)^2 + y'(t)^2}$. In plain words, velocity says which way the point is moving and how fast, and speed is just the how fast. The velocity vector is tangent to the curve, and when $x'(t) \ne 0$ the slope of the curve is

$$
\frac{dy}{dx} = \frac{dy/dt}{dx/dt}.
$$

**Polar coordinates** describe a point $P$ other than the origin by $(r, \theta)$, where $r > 0$ is the distance from the origin to $P$ and $\theta$ is the angle from the positive $x$-axis to the ray through $P$, counterclockwise. The origin is $r = 0$ with any angle. The conversion formulas are

$$
x = r\cos\theta, \qquad y = r\sin\theta, \qquad r = \sqrt{x^2 + y^2}, \qquad \tan\theta = \frac{y}{x}.
$$

In plain words, $r$ and $\theta$ are the length and direction of the vector $(x, y)$. A polar curve $r = f(\theta)$ is the set of points whose distance from the origin is given by the angle. A negative $r$ is allowed in this notation, and it means to go the opposite way: $(-2, \theta)$ is the same point as $(2, \theta + \pi)$.

Three-dimensional space is $\mathbb{R}^3$, the set of points $(x, y, z)$, as in [vectors, dot product and span](../06-linear-algebra/01-vectors-dot-product-and-span.md). The distance between $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$ is $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$, so the **sphere** of radius $R$ centred at $(a, b, c)$ is $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$. A **plane** is the set of points satisfying $ax + by + cz = d$ with $(a, b, c) \ne \mathbf{0}$, and $\mathbf{n} = (a, b, c)$ is a vector perpendicular to it, a **normal vector**. In plain words, a plane is every point $\mathbf{x}$ whose dot product with $\mathbf{n}$ is a fixed number.

A **function of two variables** $f(x, y)$ assigns a number to each point of a region of the plane, and its **graph** is the **surface** $z = f(x, y)$ in $\mathbb{R}^3$. A **level curve** of $f$ is the set of points $(x, y)$ where $f(x, y) = c$ for a constant $c$, and a **contour map** is a picture of several level curves for equally spaced values of $c$. In plain words, a level curve is the slice of the surface at height $c$, seen from above.

## How to do it

### Slope and velocity of a parametric curve

1. Differentiate each coordinate: $x'(t)$ and $y'(t)$. These two numbers are the velocity.
2. For a slope, divide: $\frac{dy}{dx} = \frac{y'(t)}{x'(t)}$ at the value of $t$ you need. This is the chain rule: $y'(t) = \frac{dy}{dx}\cdot x'(t)$.
3. If $x'(t) = 0$ and $y'(t) \ne 0$, the tangent is vertical. If both are 0, the point is momentarily at rest and the slope needs more work.
4. To get the equation in $x$ and $y$ alone, eliminate $t$ if you can, for example with $\cos^2 t + \sin^2 t = 1$.
5. Check with a point: at that $t$, is the slope what the picture shows?

The length travelled between $t = a$ and $t = b$ is the integral of the speed, $\int_a^b \sqrt{x'(t)^2 + y'(t)^2}\,dt$. This is the same idea as in [applications of integrals](../04-integrals/06-applications-of-integrals.md): add up speed times a short time.

### Polar and Cartesian

1. To go from polar to Cartesian, compute $x = r\cos\theta$ and $y = r\sin\theta$.
2. To go the other way, compute $r = \sqrt{x^2 + y^2}$.
3. Choose $\theta$ in the right quadrant. The equation $\tan\theta = \frac{y}{x}$ has two solutions in $[0, 2\pi)$, and only one points toward $(x, y)$. Look at the signs of $x$ and $y$ first, or use `atan2(y, x)` in code.
4. Check by converting back.

### Area in polar coordinates

A thin sector of the plane with angle $d\theta$ and radius $r$ is almost a triangle with base $r\,d\theta$ and height $r$, so its area is $\frac{1}{2}r^2\,d\theta$. The area swept by $r = f(\theta)$ for $\alpha \le \theta \le \beta$ is the sum of these slivers:

$$
A = \frac{1}{2}\int_\alpha^\beta r^2\,d\theta.
$$

The formula needs the curve to sweep each part of the region once as $\theta$ goes from $\alpha$ to $\beta$. For $r = 1 + \cos\theta$ that is $0 \le \theta \le 2\pi$.

![Left, a point in polar form (r, theta) and in Cartesian form (x, y), with the right triangle whose legs are r cos theta and r sin theta. Right, the heart-shaped curve r = 1 + cos theta, called a cardioid, with a thin red sector marked as a sliver of area one half r squared d theta. The area of the whole curve is 3 pi over 2.](../../assets/figures/05-university-core/parametric-polar-and-3d-coordinates-polar.svg)

The optional lesson on [double integrals](04-double-integrals.md) explains where the factor $r$ in polar integrals comes from. For now, the slivers are enough.

### Planes, distances and level curves

To write the plane through a point $P_0$ with normal vector $\mathbf{n}$, use the fact that $\mathbf{x}$ is on the plane exactly when $\mathbf{x} - P_0$ is perpendicular to $\mathbf{n}$, that is, $\mathbf{n} \cdot (\mathbf{x} - P_0) = 0$. Expanding gives $\mathbf{n} \cdot \mathbf{x} = \mathbf{n} \cdot P_0$, the form $ax + by + cz = d$.

The distance from a point $Q$ to the plane $ax + by + cz = d$ is the length of the shadow of $Q - P_0$ on the normal direction. In symbols, with $\mathbf{n} = (a, b, c)$,

$$
\text{distance} = \frac{\lvert \mathbf{n} \cdot (Q - P_0) \rvert}{\lVert \mathbf{n} \rVert} = \frac{\lvert aq_1 + bq_2 + cq_3 - d \rvert}{\sqrt{a^2 + b^2 + c^2}}.
$$

To read a surface, sketch its level curves. Setting $f(x, y) = c$ for a few values of $c$ gives the contour map. Curves that are close together mean a steep surface, and curves far apart mean a gentle one. The figure shows the hill $z = 4 - x^2 - 2y^2$ and its contours: each contour is an ellipse, because $x^2 + 2y^2 = 4 - c$.

![Left, the surface z = 4 minus x squared minus 2 y squared, a hill with peak 4 at the origin, with the level curves at heights 1, 2 and 3 drawn on it in red and projected onto the floor. Right, the contour map of the same function: nested ellipses labelled z = 0, 1, 2 and 3 around the peak at the origin, wider along the x-axis than along the y-axis.](../../assets/figures/05-university-core/parametric-polar-and-3d-coordinates-surface.svg)

## Worked examples

<div class="example" markdown>

### Example 1: a thrown ball

A ball's position is $x = 20t$, $y = 15t - 4.9t^2$ (metres, seconds, from the ground at the origin). Find the velocity and speed at $t = 1$, the slope of the path there, the highest point and where the ball lands.

Step 1: the derivatives are $x'(t) = 20$ and $y'(t) = 15 - 9.8t$. At $t = 1$ the velocity is $(20, 5.2)$ and the speed is $\sqrt{400 + 27.04} \approx 20.66$ metres per second.

Step 2: the slope at $t = 1$ is $\frac{5.2}{20} = 0.26$.

Step 3: $x'(t) = 20$ is never 0, so the tangent is never vertical. The ball is at its highest where the slope is 0, that is where $y'(t) = 15 - 9.8t = 0$, so $t = \frac{15}{9.8} \approx 1.531$. Then $y = 15(1.531) - 4.9(1.531)^2 \approx 11.48$ metres.

Step 4: the ball lands when $y = 0$: $t(15 - 4.9t) = 0$ gives $t = 0$ (the throw) and $t = \frac{15}{4.9} \approx 3.061$. Then $x = 20 \cdot 3.061 \approx 61.22$ metres.

Step 5: the check uses the speed at landing. The velocity is $(20, 15 - 9.8 \cdot 3.061) = (20, -15)$, so the speed is $\sqrt{400 + 225} = 25$. At $t = 0$ the velocity is $(20, 15)$ and the speed is also $\sqrt{400 + 225} = 25$. This model has no air resistance, so the ball lands as fast as it left.

</div>

<div class="example" markdown>

### Example 2: an ellipse by a parameter

The curve $x = 3\cos t$, $y = 2\sin t$ for $0 \le t \le 2\pi$ is an ellipse. Eliminate $t$, and find the slope at $t = \frac{\pi}{4}$.

From $\cos t = \frac{x}{3}$ and $\sin t = \frac{y}{2}$ and $\cos^2 t + \sin^2 t = 1$, we get $\frac{x^2}{9} + \frac{y^2}{4} = 1$. The derivatives are $x'(t) = -3\sin t$ and $y'(t) = 2\cos t$, so $\frac{dy}{dx} = -\frac{2\cos t}{3\sin t} = -\frac{2}{3}\cot t$. At $t = \frac{\pi}{4}$ the cotangent is 1, so the slope is $-\frac{2}{3}$. The point is $\left(\frac{3}{\sqrt{2}}, \sqrt{2}\right) \approx (2.121, 1.414)$.

Check: differentiating $\frac{x^2}{9} + \frac{y^2}{4} = 1$ implicitly gives $\frac{2x}{9} + \frac{2y}{4}\frac{dy}{dx} = 0$, so $\frac{dy}{dx} = -\frac{4x}{9y} = -\frac{4 \cdot 2.121}{9 \cdot 1.414} = -0.667$, in agreement.

</div>

<div class="example" markdown>

### Example 3: converting points and finding a polar area

Convert $(x, y) = (-1, 1)$ to polar form. Then find the area enclosed by the cardioid $r = 1 + \cos\theta$.

For the point, $r = \sqrt{1 + 1} = \sqrt{2}$. The equation $\tan\theta = \frac{1}{-1} = -1$ has solutions $\frac{3\pi}{4}$ and $\frac{7\pi}{4}$. The point has $x < 0$ and $y > 0$, so it is in the second quadrant, and $\theta = \frac{3\pi}{4}$. The answer $\theta = -\frac{\pi}{4}$ that a calculator's $\arctan(-1)$ returns points into the fourth quadrant, to $(1, -1)$.

For the area, with $r^2 = 1 + 2\cos\theta + \cos^2\theta$ and $\cos^2\theta = \frac{1 + \cos 2\theta}{2}$,

$$
A = \frac{1}{2}\int_0^{2\pi}\left(\frac{3}{2} + 2\cos\theta + \frac{1}{2}\cos 2\theta\right)d\theta = \frac{1}{2}\cdot\frac{3}{2}\cdot 2\pi = \frac{3\pi}{2} \approx 4.712,
$$

because the cosine terms integrate to 0 over a full period.

Check: the cardioid fits inside the circle of radius 2 (area $4\pi \approx 12.57$) and the value $4.712$ is well below that. A sharper check is numerical: the midpoint sum in the "In code" section gives $4.7124$.

</div>

<div class="example" markdown>

### Example 4: a plane, a distance and a hill

Find the plane through the points $(1, 0, 0)$, $(0, 2, 0)$ and $(0, 0, 3)$, and its distance from the origin.

A plane through points on the three axes with intercepts 1, 2 and 3 is $\frac{x}{1} + \frac{y}{2} + \frac{z}{3} = 1$. Multiplying by 6 clears the fractions: $6x + 3y + 2z = 6$. All three points satisfy it: $6$, $6$ and $6$. The normal vector is $(6, 3, 2)$ with length $\sqrt{36 + 9 + 4} = 7$.

The origin gives $6 \cdot 0 + 3 \cdot 0 + 2 \cdot 0 - 6 = -6$, so the distance is $\frac{6}{7} \approx 0.857$.

For the hill $z = 4 - x^2 - 2y^2$, the level curve at height $c$ is $x^2 + 2y^2 = 4 - c$. At $c = 2$ it is $x^2 + 2y^2 = 2$, which crosses the $x$-axis at $x = \pm\sqrt{2} \approx \pm 1.414$ and the $y$-axis at $y = \pm 1$. Hikers who stay on this contour keep walking at height 2.

Check: the foot of the perpendicular from the origin is $\frac{6}{49}(6, 3, 2)$, since $6x + 3y + 2z = 6$ at that point gives $\frac{6}{49} \cdot 49 = 6$. Its length is $\frac{6}{49} \cdot 7 = \frac{6}{7}$.

</div>

<div class="example" markdown>

### Example 5: the area inside a circle in polar form (finish it yourself)

The polar curve $r = 2\cos\theta$ is a circle through the origin. For $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$ the radius $r$ is nonnegative, and the point sweeps the circle once. Find the area from the formula $\frac{1}{2}\int r^2\,d\theta$.

The set-up is $A = \frac{1}{2}\int_{-\pi/2}^{\pi/2}4\cos^2\theta\,d\theta$. Replace $\cos^2\theta$ using the identity $\frac{1 + \cos 2\theta}{2}$, integrate, and check the answer against the area of a circle.

<details class="solution" markdown>
<summary>Finish</summary>

With $\cos^2\theta = \frac{1 + \cos 2\theta}{2}$, the integrand is $\frac{1}{2} \cdot 4\cos^2\theta = 1 + \cos 2\theta$, so

$$
A = \int_{-\pi/2}^{\pi/2}(1 + \cos 2\theta)\,d\theta = \left[\theta + \frac{1}{2}\sin 2\theta\right]_{-\pi/2}^{\pi/2} = \pi + 0 = \pi.
$$

Check: in Cartesian form, $x = r\cos\theta = 2\cos^2\theta$ and $y = 2\sin\theta\cos\theta$ give $(x - 1)^2 + y^2 = 1$, a circle of radius 1 and area $\pi$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: taking $\theta = \arctan\frac{y}{x}$ without looking at the quadrant. The points $(1, 1)$ and $(-1, -1)$ have the same ratio $\frac{y}{x} = 1$ and different directions, $45^\circ$ and $225^\circ$. The arctangent returns an angle between $-90^\circ$ and $90^\circ$, so it can never put a point in the left half of the plane. Check the signs of $x$ and $y$, or use `atan2`.

</div>

<div class="warning" markdown>

Watch out: confusing $\frac{dy}{dt}$ with $\frac{dy}{dx}$. The first is how fast the height changes per second, and the second is the slope of the path. At $t = 1$ in Example 1, $\frac{dy}{dt} = 5.2$ metres per second and the slope is $\frac{dy}{dx} = 0.26$, a rise of 0.26 metres per metre. Neither is the speed.

</div>

<div class="warning" markdown>

Watch out: speed is the length of the velocity vector, not the derivative of either coordinate. A point on the circle $x = 5\cos 2t$, $y = 5\sin 2t$ has velocity $(-10\sin 2t, 10\cos 2t)$ and constant speed 10, even though each coordinate's rate of change goes up and down.

</div>

<div class="warning" markdown>

Watch out: using $\int r\,d\theta$ for area, or $\int r^2\,d\theta$ without the $\frac{1}{2}$. The sliver is a thin triangle, so its area has the $\frac{1}{2}$ of a triangle and the square of $r$ (a length times a length).

</div>

<div class="warning" markdown>

Watch out: the interval of $\theta$ must trace the curve once. For $r = 2\cos\theta$, using $0 \le \theta \le 2\pi$ would go around the circle twice, and $r$ would be negative for half of that range. Integrating $\frac{1}{2}\int_0^{2\pi}4\cos^2\theta\,d\theta$ gives $2\pi$, double the true area. Sketch the curve, or find where it returns to its start.

</div>

<div class="warning" markdown>

Watch out: a level curve is a curve in the $xy$-plane, not a curve on the surface. The contour $x^2 + 2y^2 = 2$ lives at $z = 0$ on the floor, and the matching curve on the surface is the same ellipse lifted to height $z = 2$. Different level curves of one function never cross, because a point has only one value of $f$.

</div>

A parametric curve can also stop. The curve $x = t^2$, $y = t^3$ has $x'(0) = y'(0) = 0$, so the point is at rest at the origin when $t = 0$, and the quotient $\frac{y'}{x'}$ is $\frac{0}{0}$ there. After cancelling $t$, the slope formula $\frac{3t}{2}$ tends to $0$ as $t \to 0$, and the curve has a cusp at the origin with a horizontal tangent line. The quotient can't be used directly at such a point, so take the limit.

## Tricks and shortcuts

For a circle through the origin, the polar equation is short. The circle $r = 2a\cos\theta$ has centre $(a, 0)$ and radius $a$, and $r = 2a\sin\theta$ has centre $(0, a)$. The substitution $x = r\cos\theta$ shows why: multiplying $r = 2a\cos\theta$ by $r$ gives $r^2 = 2ar\cos\theta$, which is $x^2 + y^2 = 2ax$.

Spot symmetry before integrating a polar area. The cardioid is symmetric about the $x$-axis, so its area is twice the area of the top half: $2 \cdot \frac{1}{2}\int_0^{\pi}(1 + \cos\theta)^2\,d\theta = \frac{3\pi}{2}$, the same as the integral over the full turn.

To find a normal vector from three points $A$, $B$, $C$, you need a vector perpendicular to both $B - A$ and $C - A$. For intercept points on the axes, skip that and use the intercept form $\frac{x}{p} + \frac{y}{q} + \frac{z}{s} = 1$ from Example 4.

## In code

A conversion pair that handles quadrants, the projectile from Example 1, its path length (the integral of the speed) and the area of the cardioid by a midpoint sum.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import numpy as np

def to_polar(x, y):
    return math.hypot(x, y), math.atan2(y, x)

def to_cartesian(r, theta):
    return r * math.cos(theta), r * math.sin(theta)

r, th = to_polar(-1, 1)
print(round(r, 4), round(math.degrees(th), 1))
# 1.4142 135.0
print([round(v, 4) for v in to_cartesian(4, 2 * math.pi / 3)])
# [-2.0, 3.4641]

# The projectile x = 20 t, y = 15 t - 4.9 t^2.
t_land = 15 / 4.9
print(round(t_land, 4), round(20 * t_land, 2))
# 3.0612 61.22
t = np.linspace(0, t_land, 100001)
vx, vy = np.full_like(t, 20.0), 15 - 9.8 * t
speed = np.hypot(vx, vy)
print(round(speed[0], 3), round(speed[-1], 3))
# 25.0 25.0

# Length of the path = integral of speed dt (trapezoid rule).
length = np.sum((speed[1:] + speed[:-1]) / 2 * np.diff(t))
print(round(length, 2))
# 66.56

# Area of the cardioid r = 1 + cos(theta): 1/2 * integral of r^2 (midpoint rule).
n = 100000
theta = (np.arange(n) + 0.5) * 2 * np.pi / n
area = 0.5 * np.sum((1 + np.cos(theta)) ** 2) * 2 * np.pi / n
print(round(area, 4), round(3 * math.pi / 2, 4))
# 4.7124 4.7124
```

`atan2(y, x)` takes both coordinates and returns the angle in the correct quadrant, in $(-\pi, \pi]$, which is what the arctangent of a ratio can't do. The path is about 66.56 m long, a little more than the 61.22 m it covers horizontally, because it also goes up and down.

</details>

## FAQ

### Why use a parameter instead of writing $y$ as a function of $x$?

Some curves are not graphs of functions. A circle fails the vertical line test, and a path that crosses itself would need several values of $y$ for one $x$. A parameter handles all of these, and it also records timing, which is the information in a velocity. When the curve is a function graph, $x = t$ and $y = f(t)$ is the special case.

### Can a point have more than one polar form?

Yes. Adding $2\pi$ to $\theta$ gives the same point, and so does a negative $r$ with $\theta$ shifted by $\pi$. The origin has $r = 0$ and every angle. So $(2, \frac{\pi}{3})$, $(2, \frac{7\pi}{3})$ and $(-2, \frac{4\pi}{3})$ are one point. Cartesian coordinates have no such freedom, and that is why converting to polar needs a choice, usually $r \ge 0$ and $0 \le \theta < 2\pi$.

### Why does the $\frac{1}{2}$ appear in the polar area but not in the Cartesian one?

In Cartesian coordinates the slice is a thin rectangle of height $f(x)$ and width $dx$. In polar coordinates the slice is a thin wedge that comes to a point at the origin, and its area is that of a triangle. Wedges and rectangles are different shapes, and the $\frac{1}{2}$ is the triangle's $\frac{1}{2} \times \text{base} \times \text{height}$.

### Do I need to draw three-dimensional surfaces by hand?

No. The skill that carries over is reading level curves: where the contours are close, the surface is steep, and a closed contour around a point means a peak or a pit. Software draws the surface, and you read the contour map.

## Practice

### Warm-up

1\. Convert $(-3, 3\sqrt{3})$ to polar form with $r > 0$ and $0 \le \theta < 2\pi$, and convert $\left(2, \frac{\pi}{6}\right)$ to Cartesian form.

<details class="solution" markdown>
<summary>Solution</summary>

For the first point, $r = \sqrt{9 + 27} = 6$. The point has $x < 0$ and $y > 0$, so it is in the second quadrant. The reference angle has $\tan = \sqrt{3}$, which is $\frac{\pi}{3}$, so $\theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$.

For the second, $x = 2\cos\frac{\pi}{6} = \sqrt{3}$ and $y = 2\sin\frac{\pi}{6} = 1$.

Check: $6\cos\frac{2\pi}{3} = -3$ and $6\sin\frac{2\pi}{3} = 3\sqrt{3}$, which is the starting point.

</details>

2\. A curve is $x = 2t + 1$, $y = t^2 - 3$. Write $y$ in terms of $x$, and find the slope and the tangent line at $t = 2$.

<details class="solution" markdown>
<summary>Solution</summary>

From $x = 2t + 1$ we get $t = \frac{x - 1}{2}$, so $y = \frac{(x - 1)^2}{4} - 3$. The slope is $\frac{dy}{dx} = \frac{2t}{2} = t$, which is 2 at $t = 2$. The point is $(5, 1)$, so the tangent line is $y - 1 = 2(x - 5)$, that is, $y = 2x - 9$.

Check: from $y = \frac{(x-1)^2}{4} - 3$, $\frac{dy}{dx} = \frac{x - 1}{2} = 2$ at $x = 5$, and $y(5) = 4 - 3 = 1$.

</details>

3\. Find the distance between $(2, -1, 0)$ and $(5, 3, 12)$, and decide whether the point $(3, 0, 4)$ is inside, on or outside the sphere with centre $(1, -2, 3)$ and radius 4.

<details class="solution" markdown>
<summary>Solution</summary>

The differences are $(3, 4, 12)$, so the distance is $\sqrt{9 + 16 + 144} = 13$. For the sphere, the distance from $(3, 0, 4)$ to the centre is $\sqrt{(3 - 1)^2 + (0 + 2)^2 + (4 - 3)^2} = \sqrt{4 + 4 + 1} = 3$, which is less than the radius 4, so the point is inside.

Check: $(x - 1)^2 + (y + 2)^2 + (z - 3)^2 = 9 < 16 = 4^2$ for the point.

</details>

### Standard

4\. A point moves with $x = 5\cos 2t$, $y = 5\sin 2t$. Find its speed, and show that its velocity is perpendicular to its position vector at every time.

<details class="solution" markdown>
<summary>Solution</summary>

The velocity is $(-10\sin 2t, 10\cos 2t)$, so the speed is $\sqrt{100\sin^2 2t + 100\cos^2 2t} = 10$. The dot product of position and velocity is $5\cos 2t \cdot (-10\sin 2t) + 5\sin 2t \cdot 10\cos 2t = -50\sin 2t\cos 2t + 50\sin 2t\cos 2t = 0$.

So the point goes around a circle of radius 5 at constant speed 10, and the velocity is tangent to the circle, perpendicular to the radius.

Check: the circle has circumference $10\pi$, and at speed 10 a trip around takes $\pi$ seconds. The parameter $2t$ goes from 0 to $2\pi$ over $t \in [0, \pi]$, which agrees.

</details>

5\. Find the area enclosed by the four-petal rose $r = \cos 2\theta$, $0 \le \theta \le 2\pi$, and the area inside the circle $r = 3\sin\theta$.

<details class="solution" markdown>
<summary>Solution</summary>

For the rose, $A = \frac{1}{2}\int_0^{2\pi}\cos^2 2\theta\,d\theta = \frac{1}{2}\int_0^{2\pi}\frac{1 + \cos 4\theta}{2}\,d\theta = \frac{1}{2}\cdot\frac{2\pi}{2} = \frac{\pi}{2}$.

For the circle $r = 3\sin\theta$, the curve is traced once for $0 \le \theta \le \pi$: $A = \frac{1}{2}\int_0^{\pi}9\sin^2\theta\,d\theta = \frac{9}{2}\cdot\frac{\pi}{2} = \frac{9\pi}{4}$.

Check: the second curve is a circle of diameter 3 (it reaches $r = 3$ at $\theta = \frac{\pi}{2}$), so its area is $\pi\left(\frac{3}{2}\right)^2 = \frac{9\pi}{4}$. The rose fits inside the unit circle, whose area is $\pi$, and $\frac{\pi}{2} < \pi$.

</details>

6\. Describe the level curves of $f(x, y) = \sqrt{xy}$ for $x, y > 0$. Which of the points $(1, 4)$, $(2, 2)$, $(8, 0.5)$ and $(4, 4)$ lie on the same level curve? What is the slope of the level curve through $(2, 2)$ at that point?

<details class="solution" markdown>
<summary>Solution</summary>

The level curve $\sqrt{xy} = c$ is $xy = c^2$, that is, $y = \frac{c^2}{x}$, a hyperbola branch in the first quadrant. The values are $f(1, 4) = 2$, $f(2, 2) = 2$, $f(8, 0.5) = 2$ and $f(4, 4) = 4$, so the first three lie on the level curve $c = 2$, which is $y = \frac{4}{x}$, and $(4, 4)$ is on $c = 4$.

At $(2, 2)$ the slope of $y = \frac{4}{x}$ is $-\frac{4}{x^2} = -1$.

Check: $2 \cdot 2 = 4 = c^2$ for $c = 2$, and a slope of $-1$ fits the picture, since the curve is symmetric about the line $y = x$ and crosses it at $(2, 2)$.

</details>

### Challenge

7\. The cycloid, the path of a point on a rolling wheel of radius 1, is $x = t - \sin t$, $y = 1 - \cos t$. (a) Find $\frac{dy}{dx}$, and the slope at $t = \frac{\pi}{2}$. (b) Where is the slope 0, and where is the tangent vertical? (c) Find the area under one arch, $0 \le t \le 2\pi$, using $\int y\,dx = \int y\,x'(t)\,dt$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $x'(t) = 1 - \cos t$ and $y'(t) = \sin t$, so $\frac{dy}{dx} = \frac{\sin t}{1 - \cos t}$. At $t = \frac{\pi}{2}$ it is $\frac{1}{1 - 0} = 1$.

(b) The slope is 0 when $\sin t = 0$ and $1 - \cos t \ne 0$, so at $t = \pi$, the top of the arch, where $y = 2$. At $t = 0$ and $t = 2\pi$ both $x'$ and $y'$ are 0: the point touches the ground and stops for an instant. By the half-angle identities $\frac{\sin t}{1 - \cos t} = \cot\frac{t}{2}$, which tends to $+\infty$ as $t \to 0^+$, so the arch leaves the ground along a vertical tangent. The tangent is never vertical anywhere else, since $x'(t) = 0$ only at those points.

(c) $A = \int_0^{2\pi}(1 - \cos t)(1 - \cos t)\,dt = \int_0^{2\pi}(1 - 2\cos t + \cos^2 t)\,dt = 2\pi - 0 + \pi = 3\pi$.

Check: the arch is $2\pi \approx 6.28$ wide and 2 tall, a rectangle of area $4\pi$, and $3\pi$ is three-quarters of that, which looks right for an arch that is wide at the bottom. The area is 3 times the area $\pi$ of the wheel, a famous result.

</details>

8\. (Reviews [the chain rule](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md).) Find the slope $\frac{dy}{dx}$ of the cardioid $r = 1 + \cos\theta$ at $\theta = \frac{\pi}{2}$. Hint: write $x = r\cos\theta$ and $y = r\sin\theta$ with $r = 1 + \cos\theta$, so that $\theta$ is a parameter.

<details class="solution" markdown>
<summary>Solution</summary>

Treat $\theta$ as the parameter: $x = (1 + \cos\theta)\cos\theta$ and $y = (1 + \cos\theta)\sin\theta$. By the product and chain rules,

$$
\frac{dx}{d\theta} = -\sin\theta\cos\theta - (1 + \cos\theta)\sin\theta, \qquad \frac{dy}{d\theta} = -\sin^2\theta + (1 + \cos\theta)\cos\theta.
$$

At $\theta = \frac{\pi}{2}$: $\frac{dx}{d\theta} = 0 - 1 \cdot 1 = -1$ and $\frac{dy}{d\theta} = -1 + 0 = -1$. So $\frac{dy}{dx} = \frac{-1}{-1} = 1$. The point is $(0, 1)$.

Check with two nearby points: at $\theta = \frac{\pi}{2} \mp 0.001$ the curve is at about $(0.001001, 1.001000)$ and $(-0.000999, 0.999000)$, and the slope between them is $\frac{-0.002}{-0.002} \approx 1$.

</details>

## Where this shows up

- The next lesson, [partial derivatives and the gradient](02-partial-derivatives-and-the-gradient.md), differentiates functions of two variables. Its main picture is the contour map of this lesson with arrows drawn on it, and its chain rule is the chain rule for a parametric path. The lesson on [double integrals](04-double-integrals.md) uses polar coordinates and the area sliver of this lesson.
- In CS, parametric curves are how graphics and animation describe motion and shapes (Bezier curves are parametric), and polar coordinates appear in robotics and signal processing. Contour plots are how a loss function with two parameters is shown.
- In economics, indifference curves and isoquants are level curves of a utility or production function (utility and indifference curves<!-- link: ../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md -->), and a budget is a plane or a line with a normal vector given by the prices.
