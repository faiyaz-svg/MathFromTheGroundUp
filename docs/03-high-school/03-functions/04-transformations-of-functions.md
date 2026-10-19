# Transformations of functions

After this lesson you can sketch the graph of $y = a\,f(b(x - h)) + k$ from the graph of $y = f(x)$, read the shifts, stretches and reflections off an equation, explain why horizontal changes seem to act backwards, and apply the rules to $x^2$, $\lvert x \rvert$ and $\sqrt{x}$.

Before this: [reading function graphs](02-reading-function-graphs.md), [piecewise, absolute value and step functions](03-piecewise-absolute-value-and-step-functions.md), and [transformations, congruence and similarity](../../02-middle-school/06-geometry/05-transformations-congruence-similarity.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Describe how the graph of $y = (x + 4)^2 - 5$ comes from the graph of $y = x^2$, and give its vertex.
2. The graph of $y = f(x)$ passes through $(2, 6)$. Name a point on the graph of $y = f(x - 3) + 1$ and a point on the graph of $y = -f(x)$.
3. What is the domain of $y = \sqrt{-x}$, and how does its graph come from the graph of $y = \sqrt{x}$?

<details class="solution" markdown>
<summary>Answers</summary>

1. Shift the parabola 4 units left and 5 units down. The vertex $(0, 0)$ moves to $(-4, -5)$.
2. For $f(x - 3) + 1$, the point moves 3 right and 1 up, to $(5, 7)$. For $-f(x)$, the height flips sign: $(2, -6)$.
3. The root needs $-x \ge 0$, so $x \le 0$ and the domain is $(-\infty, 0]$. The graph is the reflection of $y = \sqrt{x}$ in the $y$-axis.

</details>

## The idea

Suppose an app's traffic in Toronto follows a daily curve $T(t)$, where $t$ is the time on the Eastern clock. Vancouver follows the same pattern, but on its own clock, which is 3 hours behind. When the Eastern clock reads $t$, Vancouver's clock reads $t - 3$, so the Vancouver traffic at Eastern time $t$ is $T(t - 3)$. The Vancouver peak happens 3 hours later on the Eastern clock, so the graph slides to the right by 3, and the formula has a minus sign. The sign looks backwards, and the reason is that the formula describes what is done to the input, while the graph shows what happens to the picture.

This is the whole subject. A few small changes to a formula, adding a number, multiplying by a number, or flipping a sign, either inside the brackets or outside, move, stretch or flip the graph in predictable ways. If you know the graph of one function, you know a whole family of them. A parabola anywhere on the plane, opening up or down, wide or narrow, is the graph of $x^2$ moved around.

Changes made outside the brackets, to the output, act the way you would guess. Changes made inside, to the input, act the opposite way. The lesson explains why, so that you don't have to memorize which way each one goes.

## Definitions

Let $f$ be a function. The functions below are built from it. The numbers $h$ and $k$ are shifts, and $a$ and $b$ are nonzero scale factors.

A **vertical shift** replaces $f(x)$ by $f(x) + k$: the graph moves up by $k$ if $k > 0$ and down by $\lvert k \rvert$ if $k < 0$. A **horizontal shift** replaces $f(x)$ by $f(x - h)$: the graph moves right by $h$ if $h > 0$ and left by $\lvert h \rvert$ if $h < 0$. In plain words, the number outside moves the graph up or down. The number inside moves it right or left, in the direction opposite to its sign: $f(x - 3)$ moves right and $f(x + 3)$ moves left.

A **vertical stretch or compression** replaces $f(x)$ by $a\,f(x)$ with $a > 0$. The graph is stretched away from the $x$-axis by the factor $a$ if $a > 1$, and compressed toward it if $0 < a < 1$. A **horizontal stretch or compression** replaces $f(x)$ by $f(bx)$ with $b > 0$. The graph is compressed toward the $y$-axis by the factor $b$ if $b > 1$, and stretched away from it if $0 < b < 1$. Again the inside change acts backwards: multiplying the input by 2 makes the graph half as wide.

A **reflection in the $x$-axis** replaces $f(x)$ by $-f(x)$, which flips every height. A **reflection in the $y$-axis** replaces $f(x)$ by $f(-x)$, which swaps the left and right sides. In plain words, a minus sign outside flips the graph upside down, and a minus sign inside flips it left to right.

Together these make the general form

$$
g(x) = a\,f\bigl(b(x - h)\bigr) + k.
$$

A negative $a$ includes a reflection in the $x$-axis along with the stretch by $\lvert a \rvert$, and a negative $b$ includes a reflection in the $y$-axis along with the compression by $\lvert b \rvert$. The function $f$ is the **parent function**, and $g$ is a transformation of it.

![Two panels showing y = x squared in gray. On the left, the same parabola shifted up 2 (x squared plus 2, green) and down 3 (x squared minus 3, orange). On the right, the parabola shifted right 2 (x minus 2, squared, green) with its vertex at (2, 0), and left 3 (x plus 3, squared, orange) with its vertex at (-3, 0).](../../assets/figures/03-high-school/transformations-of-functions-shifts.svg)

## How to do it

### Why the inside acts backwards

This is a theorem about points. It says where each point of the parent graph goes.

*Theorem.* Let $g(x) = a\,f\bigl(b(x - h)\bigr) + k$ with $b \ne 0$. A point $(u, v)$ is on the graph of $f$ exactly when the point

$$
\left(h + \frac{u}{b},\ av + k\right)
$$

is on the graph of $g$.

We know the definitions of $f$ and $g$, and that the graph of a function is the set of points $(x, \text{output})$ for inputs $x$ in the domain. We want a rule that takes each point of the parent graph to a point of the new graph, and that reaches every point of the new graph. The plan is to choose the new $x$ so that the inside of $f$ becomes exactly $u$.

*Proof.* Suppose $(u, v)$ is on the graph of $f$, so $v = f(u)$. Put $x = h + \frac{u}{b}$. Then $b(x - h) = b \cdot \frac{u}{b} = u$, so $g(x) = a\,f(u) + k = av + k$. So the point $\left(h + \frac{u}{b}, av + k\right)$ is on the graph of $g$. Conversely, if $x$ is in the domain of $g$, then $u = b(x - h)$ is in the domain of $f$, the point $(u, f(u))$ is on the graph of $f$, and by the same calculation it goes to $(x, g(x))$. So every point of the graph of $g$ comes from a point of the graph of $f$. $\blacksquare$

Looking back: the point rule says what the graph does. Horizontally, $x = h + \frac{u}{b}$ divides every old $x$-coordinate by $b$ and then adds $h$. The formula $b(x - h)$ did the reverse to the input: subtract $h$, then multiply by $b$. The graph undoes what the formula does to $x$, and in the opposite order. That is the backwards behaviour. Vertically, $av + k$ multiplies by $a$ and then adds $k$, the same operations in the same order as in the formula, so the outside acts as you would guess.

Two special cases tell you the rules of the table. With $b = 1$ and $a = 1$: $(u, v) \mapsto (u + h, v + k)$, a shift. With $h = k = 0$ and $b = -1$: $(u, v) \mapsto (-u, v)$, a reflection in the $y$-axis. This is the translation rule from [transformations, congruence and similarity](../../02-middle-school/06-geometry/05-transformations-congruence-similarity.md): the same movement of points, written there as a rule on points and here as a change in the equation.

| Change to $f(x)$ | What happens to a point $(u, v)$ | Effect on the graph |
|---|---|---|
| $f(x) + k$ | $(u, v + k)$ | up $k$ (down if $k < 0$) |
| $f(x - h)$ | $(u + h, v)$ | right $h$ (left if $h < 0$) |
| $a\,f(x)$, $a > 0$ | $(u, av)$ | vertical stretch by $a$ |
| $f(bx)$, $b > 0$ | $\left(\frac{u}{b}, v\right)$ | horizontal compression by $b$ |
| $-f(x)$ | $(u, -v)$ | reflection in the $x$-axis |
| $f(-x)$ | $(-u, v)$ | reflection in the $y$-axis |

### Sketching a transformed graph

1. Name the parent function $f$ and write the target in the form $a\,f(b(x - h)) + k$. If $b$ has a number added to it inside, factor $b$ out first: $f(2x - 6)$ becomes $f(2(x - 3))$, with $b = 2$ and $h = 3$.
2. List 3 to 5 key points of the parent graph, such as a vertex, intercepts and a point on each side.
3. Move each key point with the rule $(u, v) \mapsto \left(h + \frac{u}{b},\ av + k\right)$. Do the horizontal part, dividing by $b$ and then adding $h$, and the vertical part, multiplying by $a$ and then adding $k$.
4. Plot the images and join them with the shape of the parent graph. Pay attention to the end behaviour and any endpoints.
5. Read off the new domain and range. The domain is the old domain moved by the horizontal rule, and the range by the vertical rule.
6. Check by evaluating $g$ at one or two $x$-values and confirming that the points lie on your sketch.

### The order of transformations

Horizontal and vertical changes don't interfere with each other: you can do any horizontal change before or after any vertical one. The order matters only among changes in the same direction. Vertically, $2f(x) + 3$ stretches and then shifts, and it is not the same as $2\bigl(f(x) + 3\bigr) = 2f(x) + 6$, which shifts and then stretches. Horizontally, a reflection and a shift in either order give different graphs. By the theorem, the standard form $a\,f(b(x - h)) + k$ corresponds to: scale and reflect first, then shift.

### The three parents

For $x^2$, the form $a(x - h)^2 + k$ is the vertex form of a parabola. Its vertex is $(h, k)$, it opens up if $a > 0$ and down if $a < 0$, and it is narrower for a larger $\lvert a \rvert$. [Quadratic functions and graphs](../05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md) builds on this.

For $\lvert x \rvert$, the form $a\lvert x - h \rvert + k$ is a V with its corner at $(h, k)$ and slopes $\pm a$.

For $\sqrt{x}$, the form $a\sqrt{b(x - h)} + k$ starts at $(h, k)$ and heads right if $b > 0$ or left if $b < 0$. Its domain is $x \ge h$ if $b > 0$, and $x \le h$ if $b < 0$.

![Four curves around the origin, with the points (1, 1), (-1, 1), (1, -1) and (-1, -1) marked. The square root of x is in the first quadrant, minus the square root of x in the fourth, the square root of minus x in the second, and minus the square root of minus x in the third.](../../assets/figures/03-high-school/transformations-of-functions-reflections.svg)

For a parent such as $x^2$, $\lvert x \rvert$ or $\sqrt{x}$, a horizontal change can look the same as a vertical one: $\sqrt{4x} = 2\sqrt{x}$. This happens because these functions turn multiplication into multiplication. A parent with a more interesting shape tells them apart, as the cubic does in the figure below, where $f(x) = x^3 - 3x$ from [reading function graphs](02-reading-function-graphs.md) is used. The vertical stretch $2f(x)$ keeps the zeros where they are and doubles the heights. The horizontal compression $f(2x)$ moves the zeros toward the $y$-axis, and the domain $[-2, 2]$ shrinks to $[-1, 1]$.

![Two panels for the cubic f(x) = x cubed minus 3x on the interval from -2 to 2, shown in gray. On the left, 2 f(x) in green has the same zeros but peaks at height 4, and one half f(x) in orange peaks at height 1. On the right, f(2x) in green is squeezed into the interval from -1 to 1, and f(x/2) in orange is stretched across the interval from -4 to 4.](../../assets/figures/03-high-school/transformations-of-functions-scaling.svg)

## Worked examples

<div class="example" markdown>

### Example 1: four transformations of the square root

Sketch $g(x) = -2\sqrt{x + 3} + 1$ and find its domain and range.

Step 1: the parent is $f(x) = \sqrt{x}$. Write $x + 3$ as $x - (-3)$, so $h = -3$, with $b = 1$, $a = -2$ and $k = 1$. In words: shift left 3, stretch vertically by 2, reflect in the $x$-axis, and shift up 1.

Step 2: key points of $\sqrt{x}$ with easy values: $(0, 0)$, $(1, 1)$, $(4, 2)$ and $(9, 3)$.

Step 3: apply $(u, v) \mapsto (-3 + u,\ -2v + 1)$:

| Parent point | New point |
|---|---|
| $(0, 0)$ | $(-3, 1)$ |
| $(1, 1)$ | $(-2, -1)$ |
| $(4, 2)$ | $(1, -3)$ |
| $(9, 3)$ | $(6, -5)$ |

Step 4: plot these and draw the square-root shape through them. The graph starts at $(-3, 1)$, the image of the starting point, and falls toward the right, because the reflection turned the rising curve upside down.

![The gray dashed graph of the square root of x with the points (0, 0), (1, 1), (4, 2) and (9, 3), and in green the graph of minus 2 times the square root of (x plus 3) plus 1, through (-3, 1), (-2, -1), (1, -3) and (6, -5), with thin arrows from each parent point to its image.](../../assets/figures/03-high-school/transformations-of-functions-steps.svg)

Step 5: the parent has domain $[0, \infty)$ and range $[0, \infty)$. Shifting left 3 makes the domain $[-3, \infty)$. The range goes through $v \mapsto -2v + 1$: the outputs $v \ge 0$ become $-2v + 1 \le 1$, so the range is $(-\infty, 1]$.

Step 6: check with numbers. $g(1) = -2\sqrt{4} + 1 = -3$ and $g(6) = -2\sqrt{9} + 1 = -5$, both on the sketch.

</div>

<div class="example" markdown>

### Example 2: factoring out the scale

Describe the graph of $g(x) = \lvert 2x - 6 \rvert - 1$ in terms of $y = \lvert x \rvert$.

By Step 1, $2x - 6$ must be written as $2(x - 3)$, so $b = 2$ and $h = 3$, with $a = 1$ and $k = -1$. The graph is compressed horizontally by 2, shifted right 3 (not 6), and shifted down 1. The point rule gives the corner $(0, 0) \mapsto (3 + 0, -1) = (3, -1)$, and the point $(1, 1) \mapsto (3.5, 0)$, and $(-1, 1) \mapsto (2.5, 0)$. So the zeros are $x = 2.5$ and $x = 3.5$.

Here is a second way to see it. Since $\lvert 2(x - 3) \rvert = 2\lvert x - 3 \rvert$, the same function is $g(x) = 2\lvert x - 3 \rvert - 1$: a vertical stretch by 2, right 3, down 1. A V compressed horizontally by 2 is the same as a V stretched vertically by 2, because a V has no scale: its slopes just double.

Check: $g(4) = \lvert 8 - 6 \rvert - 1 = 1$, and the other form gives $2 \cdot 1 - 1 = 1$. Also $g(2.5) = \lvert -1 \rvert - 1 = 0$.

<div class="warning" markdown>

Watch out: reading $\lvert 2x - 6 \rvert$ as a shift of 6 is the usual mistake. A shift is the number subtracted from $x$ itself, so the 2 must come out of the bracket first. The corner is at $x = 3$, where $2x - 6 = 0$.

</div>

</div>

<div class="example" markdown>

### Example 3: reflect then shift, or shift then reflect

Start with $f(x) = \sqrt{x}$. Find the equation after (A) reflecting in the $y$-axis and then shifting right 2, and (B) shifting right 2 and then reflecting in the $y$-axis.

For (A), the reflection gives $\sqrt{-x}$. Now shifting right 2 replaces $x$ by $x - 2$ everywhere, including inside the minus sign: $\sqrt{-(x - 2)} = \sqrt{2 - x}$. The domain is $x \le 2$.

For (B), the shift gives $\sqrt{x - 2}$. Reflecting replaces $x$ by $-x$: $\sqrt{-x - 2}$. The domain needs $-x - 2 \ge 0$, so $x \le -2$.

The two graphs are different. Track the starting point $(0, 0)$: in (A) the reflection leaves it at $(0, 0)$ and the shift sends it to $(2, 0)$, while in (B) the shift sends it to $(2, 0)$ and the reflection to $(-2, 0)$.

![Three curves on one grid. The gray dashed curve is the square root of x, starting at the origin and going right. The green curve is the square root of (2 minus x), starting at (2, 0) and going left. The orange curve is the square root of (minus x minus 2), starting at (-2, 0) and going left.](../../assets/figures/03-high-school/transformations-of-functions-order.svg)

Check: in (A) the point $(1, 1)$ goes to $(-1, 1)$ and then to $(1, 1)$, and $\sqrt{2 - 1} = 1$. In (B) it goes to $(3, 1)$ and then to $(-3, 1)$, and $\sqrt{-(-3) - 2} = \sqrt{1} = 1$. Both images satisfy their formulas.

</div>

<div class="example" markdown>

### Example 4: reading a transformed parabola (finish it yourself)

Describe $g(x) = -\frac{1}{2}(x - 1)^2 + 4$ in terms of $y = x^2$, then find its vertex, its range, its $y$-intercept and its $x$-intercepts.

The form $a f(b(x - h)) + k$ has $a = -\frac{1}{2}$, $h = 1$ and $k = 4$. The graph is the parabola $y = x^2$ compressed vertically by $\frac{1}{2}$, flipped upside down, and moved right 1 and up 4. The vertex $(0, 0)$ goes to $(1, 4)$, and the parabola opens downward, so the range is $(-\infty, 4]$.

Now find the $y$-intercept and the $x$-intercepts, and check them.

<details class="solution" markdown>
<summary>Finish</summary>

The $y$-intercept is $g(0) = -\frac{1}{2}(1) + 4 = 3.5$, so $(0, 3.5)$.

For the $x$-intercepts, solve $-\frac{1}{2}(x - 1)^2 + 4 = 0$. Then $(x - 1)^2 = 8$, so $x - 1 = \pm\sqrt{8} = \pm 2\sqrt{2}$ and $x = 1 \pm 2\sqrt{2}$, about $3.83$ and $-1.83$. The answers are not whole numbers, and that is fine.

Check: $g(3) = -\frac{1}{2}(4) + 4 = 2$ is positive, and $g(4) = -\frac{1}{2}(9) + 4 = -0.5$ is negative, so the graph crosses zero between 3 and 4, as $3.83$ requires. Also $g(1 + 2\sqrt{2}) = -\frac{1}{2}(8) + 4 = 0$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: $f(x + 2)$ moves the graph left, not right. The graph undoes the formula: to get the old output you need $x + 2$ to equal the old input, so $x$ must be 2 less. A check with one point settles it: for $f(x) = x^2$, the zero of $f(x + 2) = (x + 2)^2$ is at $x = -2$.

</div>

<div class="warning" markdown>

Watch out: $f(2x)$ is compressed, not stretched. A graph that reaches a height at $x = 4$ reaches it at $x = 2$ after the change, because the formula doubles the input before $f$ sees it. A stretch needs $b < 1$, as in $f(\frac{x}{2})$.

</div>

<div class="warning" markdown>

Watch out: $-f(x)$ and $f(-x)$ are different. For $\sqrt{x}$, the first is $-\sqrt{x}$, hanging below the $x$-axis, and the second is $\sqrt{-x}$, extending to the left. They agree only when the function has the right symmetry: for an odd function they are the same graph, since $f(-x) = -f(x)$, and for an even function $f(-x)$ is the original graph.

</div>

<div class="warning" markdown>

Watch out: don't shift by the number you see before $x$. In $f(3x - 6)$ the shift is 2, not 6, and in $f(\frac{x}{2} + 1)$ the shift is $-2$, since $\frac{x}{2} + 1 = \frac{1}{2}(x + 2)$. Factor out the number multiplying $x$ first.

</div>

A stretch or compression never moves a point on the axis it works from. The vertical scale $a\,f(x)$ keeps the zeros fixed, and the horizontal scale $f(bx)$ keeps the $y$-intercept $(0, f(0))$ fixed. Reflections keep the points on their mirror axis fixed too.

A scale factor of 0 or a $b$ of 0 isn't a transformation at all. It flattens the graph to the $x$-axis or collapses it to a vertical line, which is not the graph of a function. That is why $a$ and $b$ are required to be nonzero.

Domain and range follow the transformations: a horizontal shift moves the domain, a horizontal scale divides the domain's endpoints by $b$, and the vertical changes act on the range the same way. For $f(2x)$ with domain $[-2, 2]$, the new domain is $[-1, 1]$.

## Tricks and shortcuts

Track the parent's most recognizable point, such as the vertex of $x^2$ or the corner of $\lvert x \rvert$ and $\sqrt{x}$. After a transformation it sits at $(h, k)$ in vertex form, and the rest of the graph hangs off it in the shape of the parent.

To get $h$ without sign errors, ask what input makes the inside of $f$ equal to 0. For $(x + 2)^2$ the input is $-2$, so the vertex is at $x = -2$.

To check a sketch, evaluate $g$ at the $x$-value of one key point. If the value matches the $y$-coordinate you computed with the point rule, the horizontal and vertical parts agree.

To compare the widths of parabolas, use $a$ in $a(x - h)^2 + k$: for the same height above the vertex, $y - k = a(x - h)^2$ gives $\lvert x - h \rvert = \sqrt{(y - k)/a}$, so a larger $\lvert a \rvert$ means a narrower parabola.

## In code

Transformations of a function are functions that take a function and return a new one. The code builds the general form and checks the point rule from the theorem on Example 1.

<details class="code" markdown>
<summary>In code</summary>

```python
from math import sqrt

def transform(f, a=1, b=1, h=0, k=0):
    return lambda x: a * f(b * (x - h)) + k

g = transform(sqrt, a=-2, h=-3, k=1)     # -2*sqrt(x + 3) + 1
print(g(1), g(6))                        # -3.0 -5.0

for u, v in [(0, 0), (1, 1), (4, 2), (9, 3)]:
    x = -3 + u / 1                       # h + u/b
    y = -2 * v + 1                       # a*v + k
    print((u, v), "->", (x, y), g(x) == y)
# (0, 0) -> (-3.0, 1) True
# (1, 1) -> (-2.0, -1) True
# (4, 2) -> (1.0, -3) True
# (9, 3) -> (6.0, -5) True

shifted_then_flipped = lambda x: sqrt(-x - 2)
flipped_then_shifted = lambda x: sqrt(2 - x)
print(shifted_then_flipped(-6), flipped_then_shifted(-2))   # 2.0 2.0
```

The function `transform` returns a new function, and shows the order in the formula: it multiplies by $b$ after subtracting $h$, so the input is shifted first and scaled second, while the graph does the reverse. The loop confirms that each parent point lands on the new graph. The last two lines evaluate Example 3: the two orders are different functions, with different domains, and they happen to agree here only because the two inputs, $-6$ and $-2$, were chosen to give the same output.

</details>

## FAQ

### Why does a minus sign inside move the graph to the right?

Because $f(x - h)$ at $x = c + h$ equals $f(c)$, the value the parent has at $c$. The new graph reaches the parent's height at $c$ only after you have moved $h$ further right. In the time-zone story, a clock 3 hours behind sees the same event 3 hours later on your clock.

### Does the order really matter if I only shift and stretch?

For changes in different directions, no: a vertical change and a horizontal change commute. For two changes in the same direction, yes. Stretching by 2 and then shifting up 3 gives $2f(x) + 3$, but shifting up 3 and then stretching by 2 gives $2f(x) + 6$. When the equation is in the standard form, the order is built in: scale and reflect first, then shift.

### What about a transformation like $f(x^2)$ or $f(\lvert x \rvert)$?

Those change the shape of the graph rather than moving or scaling it, so they are not in this family. The replacement $f(\lvert x \rvert)$ copies the right half of the graph onto the left side, and $\lvert f(x) \rvert$ flips every part below the axis upward. Both are useful, and neither is a shift, stretch or reflection.

### Can I turn any parabola into $y = x^2$ this way?

Every parabola $y = ax^2 + bx + c$ with $a \ne 0$ is $y = x^2$ stretched, possibly flipped, and shifted, by completing the square. For example, $x^2 + 6x + 11 = (x + 3)^2 + 2$ is $x^2$ moved left 3 and up 2. Practice problem 7 does two more.

## Practice

### Warm-up

1\. Describe each graph in terms of its parent, and give the key point: (a) $y = (x + 4)^2 - 5$, (b) $y = -\lvert x - 2 \rvert$, (c) $y = \sqrt{x} + 3$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The parent is $x^2$: left 4 and down 5. The vertex moves from $(0, 0)$ to $(-4, -5)$.
- (b) The parent is $\lvert x \rvert$: right 2 and reflected in the $x$-axis, so it is an upside-down V with its corner at $(2, 0)$.
- (c) The parent is $\sqrt{x}$: up 3. The starting point moves from $(0, 0)$ to $(0, 3)$, and the range is $[3, \infty)$.

Check (a): the inside is 0 at $x = -4$, where $y = -5$. Check (b): $y = -\lvert 2 - 2 \rvert = 0$ at $x = 2$, and every other output is negative.

</details>

2\. The graph of $f$ passes through $(-2, 3)$, $(0, 1)$ and $(4, -2)$. Find the images of these points on (a) $g(x) = 2f(x - 1) + 3$ and (b) $h(x) = f(2x)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Here $a = 2$, $b = 1$, $h = 1$ and $k = 3$, so $(u, v) \mapsto (1 + u,\ 2v + 3)$. The points go to $(-1, 9)$, $(1, 5)$ and $(5, -1)$.

(b) Here $b = 2$, so $(u, v) \mapsto \left(\frac{u}{2}, v\right)$. The points go to $(-1, 3)$, $(0, 1)$ and $(2, -2)$.

Check (a): $g(1) = 2f(0) + 3 = 2(1) + 3 = 5$. Check (b): $h(2) = f(4) = -2$.

</details>

3\. Write the equation of the graph of $y = \lvert x \rvert$ after it is shifted left 2, reflected in the $x$-axis, and shifted up 5.

<details class="solution" markdown>
<summary>Solution</summary>

Shifting left 2 gives $\lvert x + 2 \rvert$. Reflecting in the $x$-axis gives $-\lvert x + 2 \rvert$. Shifting up 5 gives $y = -\lvert x + 2 \rvert + 5$.

Check: the corner $(0, 0)$ moves to $(-2, 5)$. At $x = -2$ the equation gives $-0 + 5 = 5$, and the graph is an upside-down V, so 5 is the maximum.

</details>

### Standard

4\. Show that $y = \sqrt{4x + 8}$ is a transformation of $y = \sqrt{x}$ in two ways, and find its domain.

<details class="solution" markdown>
<summary>Solution</summary>

Factor out the 4: $\sqrt{4x + 8} = \sqrt{4(x + 2)}$. So $b = 4$ and $h = -2$: a horizontal compression by 4, shifted left 2. The point rule $(u, v) \mapsto (-2 + \frac{u}{4}, v)$ sends $(0, 0)$, $(1, 1)$ and $(4, 2)$ to $(-2, 0)$, $(-1.75, 1)$ and $(-1, 2)$.

Also $\sqrt{4(x + 2)} = \sqrt{4}\sqrt{x + 2} = 2\sqrt{x + 2}$, a vertical stretch by 2 and a shift left 2.

The domain needs $4x + 8 \ge 0$, so $x \ge -2$, which is $[-2, \infty)$.

Check: at $x = -1$, $\sqrt{4(-1) + 8} = 2$, and $2\sqrt{-1 + 2} = 2$.

</details>

5\. Complete the square to describe $y = x^2 - 4x + 1$ as a transformation of $y = x^2$. Give the vertex, the range and the $x$-intercepts.

<details class="solution" markdown>
<summary>Solution</summary>

$x^2 - 4x + 1 = (x^2 - 4x + 4) - 4 + 1 = (x - 2)^2 - 3$. So the parabola is $y = x^2$ moved right 2 and down 3. The vertex is $(2, -3)$, and the range is $[-3, \infty)$.

For the $x$-intercepts, $(x - 2)^2 = 3$ gives $x = 2 \pm \sqrt{3}$, about $3.73$ and $0.27$.

Check: expanding $(x - 2)^2 - 3$ gives $x^2 - 4x + 4 - 3 = x^2 - 4x + 1$. The $y$-intercept is $1$ both ways.

</details>

6\. Let $f(x) = \sqrt{x}$. Find the equations that stretch the graph vertically by 3 and then shift it up 2, and that shift it up 2 and then stretch it by 3. Where does the point $(4, 2)$ go in each case?

<details class="solution" markdown>
<summary>Solution</summary>

Stretch then shift: $y = 3\sqrt{x} + 2$. The point $(4, 2)$ goes to $(4, 3 \cdot 2 + 2) = (4, 8)$.

Shift then stretch: $y = 3\bigl(\sqrt{x} + 2\bigr) = 3\sqrt{x} + 6$. The point goes to $(4, 3 \cdot 2 + 6) = (4, 12)$, since it moves to height 4 and then to height 12.

The graphs differ by 4 units everywhere, since the shift of 2 was multiplied by 3 in the second case.

Check: $3(2 + 2) = 12$ and $3(2) + 2 = 8$.

</details>

### Challenge

7\. Describe each as a transformation of $y = x^2$ by completing the square, and check by expanding: (a) $y = x^2 + 6x + 11$, (b) $y = 2x^2 - 8x + 5$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $x^2 + 6x + 11 = (x^2 + 6x + 9) + 2 = (x + 3)^2 + 2$: left 3 and up 2, with vertex $(-3, 2)$.

(b) Factor the 2 out of the first two terms: $2x^2 - 8x + 5 = 2(x^2 - 4x) + 5 = 2\bigl((x - 2)^2 - 4\bigr) + 5 = 2(x - 2)^2 - 3$. So it is a vertical stretch by 2, right 2 and down 3, with vertex $(2, -3)$.

Check by expanding: $(x + 3)^2 + 2 = x^2 + 6x + 9 + 2 = x^2 + 6x + 11$, and $2(x - 2)^2 - 3 = 2x^2 - 8x + 8 - 3 = 2x^2 - 8x + 5$.

</details>

8\. (Reviews [slope and linear equations](../../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md).) The temperature graph $T(t)$ in [reading function graphs](02-reading-function-graphs.md) is in degrees Celsius. To redraw it in Fahrenheit, use $F(t) = 1.8\,T(t) + 32$. (a) Which transformations is that? (b) Where does the point $(15, 2)$ go? (c) Where does the dashed freezing line $y = 0$ go? (d) Does the time of the warmest moment change?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $a = 1.8$ and $k = 32$: a vertical stretch by 1.8, then a shift up 32.

(b) $(15, 2) \mapsto (15, 1.8 \cdot 2 + 32) = (15, 35.6)$.

(c) Every point at height 0 goes to height $1.8 \cdot 0 + 32 = 32$, so the freezing line moves to $y = 32$.

(d) No. The transformation acts only on the output, so every point keeps its $x$-coordinate and the warmest moment is still at 15:00.

Check: the coldest point $(3, -10)$ goes to $(3, -18 + 32) = (3, 14)$, below the new freezing line at 32, as $-10$ °C is below freezing.

</details>

## Where this shows up

- The next lesson, [composition and inverse functions](05-composition-and-inverse-functions.md), builds new functions by chaining. A transformation is a composition: $g = a \cdot f(b(x - h)) + k$ is $f$ with simple linear functions applied to its input and output. [Quadratic functions and graphs](../05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md) uses vertex form, and graphs of trig functions<!-- link: ../09-trigonometry/03-graphs-of-trig-functions.md --> need amplitude, period and phase shift, which are $a$, $b$ and $h$ for sine and cosine.
- In computer graphics, a shift, scale or flip of an image is the same kind of rule on coordinates, written with matrices (matrix basics<!-- link: ../10-vectors-and-matrices/02-matrix-basics.md -->). Normalizing data, subtracting a mean and dividing by a standard deviation, is a shift and a scale.
- In economics, a change in income moves a demand curve sideways, while a tax added to a price moves a supply curve up (supply and demand equilibrium algebra<!-- link: ../../07-economics-math/02-markets/03-supply-and-demand-equilibrium-algebra.md -->).
