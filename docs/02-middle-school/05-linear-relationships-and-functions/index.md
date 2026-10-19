# Linear relationships and functions

Points in the plane, straight lines and their slopes, functions and $f(x)$ notation, and finding where two lines cross.

1. [The coordinate plane](01-coordinate-plane.md)
2. [Slope and linear equations](02-slope-and-linear-equations.md)
3. [Introduction to functions](03-intro-to-functions.md)
4. [Systems of linear equations](04-systems-of-linear-equations.md)

## Cheat sheet

### The coordinate plane

The $x$-axis runs across (positive to the right) and the $y$-axis runs up (positive upward); they cross at the origin $(0, 0)$. A point is an ordered pair $(x, y)$: go $x$ across, then $y$ up. Order matters, so $(2, 5) \ne (5, 2)$.

| Region | Signs | Example |
|---|---|---|
| quadrant I | $(+, +)$ | $(3, 2)$ |
| quadrant II | $(-, +)$ | $(-3, 3)$ |
| quadrant III | $(-, -)$ | $(-4, -1)$ |
| quadrant IV | $(+, -)$ | $(2, -3)$ |
| $x$-axis | $y = 0$ | $(-6, 0)$ |
| $y$-axis | $x = 0$ | $(0, 4.5)$ |

The quadrants are numbered counterclockwise from the top right. Points on an axis are in no quadrant.

| Task | Rule | Example |
|---|---|---|
| horizontal distance (same $y$) | $\lvert x_2 - x_1 \rvert$ | $(-3, 2)$ to $(4, 2)$ is 7 |
| vertical distance (same $x$) | $\lvert y_2 - y_1 \rvert$ | $(4, 2)$ to $(4, -1)$ is 3 |
| reflect in the $x$-axis | $(a, b)$ becomes $(a, -b)$ | $(3, 2)$ becomes $(3, -2)$ |
| reflect in the $y$-axis | $(a, b)$ becomes $(-a, b)$ | $(3, 2)$ becomes $(-3, 2)$ |
| reflect in both axes | $(a, b)$ becomes $(-a, -b)$ | $(3, 2)$ becomes $(-3, -2)$ |

- The axis you reflect in keeps its coordinate; the other coordinate changes sign.
- To read a real graph, check the labels, the units and the value of one grid step first. Say "about" when you read between grid lines.

Main mistakes:

- Plotting $(y, x)$ instead of $(x, y)$.
- Putting $(0, 5)$ on the $x$-axis. A zero $x$-coordinate puts the point on the $y$-axis.
- Changing the wrong sign in a reflection.
- Computing $4 - 3$ for the distance from $-3$ to 4. It is $4 - (-3) = 7$.

### Slope and linear equations

The slope of the line through $(x_1, y_1)$ and $(x_2, y_2)$, with $x_1 \ne x_2$, is

$$
m = \frac{\text{rise}}{\text{run}} = \frac{y_2 - y_1}{x_2 - x_1} = \frac{\Delta y}{\Delta x}.
$$

Every pair of points on a line gives the same slope. With units, the slope is a rate of change: units of $y$ per unit of $x$ (the taxi's slope is \$2 per km).

| Slope | Line | Equation |
|---|---|---|
| positive | rises to the right | $y = mx + b$, $m > 0$ |
| negative | falls to the right | $y = mx + b$, $m < 0$ |
| zero | horizontal | $y = b$ |
| undefined | vertical | $x = a$ |

Slope-intercept form is $y = mx + b$, where $m$ is the slope and $(0, b)$ is the $y$-intercept. Point-slope form is $y - y_1 = m(x - x_1)$. A proportional relationship $y = kx$ is the case $b = 0$, with slope $k$.

| Task | Method | Example |
|---|---|---|
| graph $y = mx + b$ | plot $(0, b)$, then move run across and rise up | $y = -\frac{3}{2}x + 3$: $(0, 3)$, $(2, 0)$, $(4, -3)$ |
| line through two points | find $m$, put one point in $y = mx + b$, solve for $b$, check the other point | $(-1, 7)$ and $(3, -1)$ give $y = -2x + 5$ |
| $y$-intercept | set $x = 0$ | $y = 4x - 6$ gives $(0, -6)$ |
| $x$-intercept | set $y = 0$ and solve | $y = 4x - 6$ gives $(1.5, 0)$ |
| a table | slope between neighbouring rows must be constant | days 1, 3, 4, 7 and costs 85, 155, 190, 295 give $y = 35x + 50$ |

- Cover-up for intercepts: in $2x + 3y = 12$, setting $y = 0$ gives $x = 6$ and setting $x = 0$ gives $y = 4$.
- Parallel lines have equal slopes. Perpendicular lines (neither vertical) have slopes that multiply to $-1$, such as $2$ and $-\frac{1}{2}$.

Main mistakes:

- Subtracting in different orders on top and bottom, which flips the sign.
- Run over rise. The change in $y$ goes on top.
- Reading $b$ from an equation not solved for $y$: $2x + 3y = 12$ is $y = -\frac{2}{3}x + 4$, so $b = 4$, not 12.
- Mixing up zero slope (horizontal) and undefined slope (vertical).
- Judging slope by eye when the two axes have different scales.

### Introduction to functions

A function assigns to each input exactly one output. The domain is the set of allowed inputs and the range is the set of outputs that occur. The notation $f(x)$, "$f$ of $x$", is the output of $f$ at the input $x$, not $f$ times $x$.

| Given | It is a function when |
|---|---|
| a list or table | no input appears with two different outputs |
| a mapping diagram | each input sends out exactly one arrow |
| a graph | every vertical line meets it at most once (vertical line test) |
| an equation | each $x$ gives one $y$; $y^2 = x$ fails, since $x = 4$ gives $y = \pm 2$ |

| Task | Method | Example |
|---|---|---|
| evaluate $f(a)$ | write empty brackets, put the whole input in each, simplify | $g(x) = 2x^2 - 3x + 1$: $g(-2) = 2(4) + 6 + 1 = 15$ |
| solve $f(x) = c$ | solve the equation for $x$ | $3x + 5 = 50$ gives $x = 15$ |
| domain | remove inputs that divide by 0 or root a negative; keep inputs that make sense | $\frac{12}{x - 3}$: every number except 3 |
| linear or not | linear means $f(x) = mx + b$; with equal input steps the output differences are constant | $x^2$ has differences $-3, -1, 1, 3$: nonlinear |

- Many inputs may share an output; one input may not have two outputs.
- A function whose domain is whole numbers (tickets, pizzas) graphs as separate points. Don't join them.
- A program function with side effects, or one that uses randomness, can give different outputs for the same input, so it is not a math function. A pure function is.

Main mistakes:

- Writing $-2^2$ for the square of the input $-2$. It is $(-2)^2 = 4$.
- Treating $f(x + 2)$ as $f(x) + 2$. With $f(x) = x^2$, $f(3) = 9$ but $f(1) + 2 = 3$.
- Using a horizontal line test to decide whether a graph is a function.
- Calling a relation a function because some inputs have one output. Every input must.

### Systems of linear equations

A solution of a system is a pair $(x, y)$ that makes every equation true at once: a point on both lines.

| Method | Steps | Best when |
|---|---|---|
| graphing | graph both lines, read the crossing, check it | you want a picture or an estimate |
| substitution | solve one equation for a variable, substitute into the other, solve, back-substitute | a variable has coefficient 1 or $-1$, or is already alone |
| elimination | multiply so one variable has opposite coefficients, add, solve, back-substitute | no coefficient is 1 |

Always check the pair in both original equations.

| Lines | Solutions | Algebra ends with |
|---|---|---|
| different slopes | exactly one | a value for each unknown |
| parallel (same slope, different intercepts) | none | a false statement such as $0 = 1$ |
| the same line | infinitely many | a true statement such as $0 = 0$ |

- Compare slopes first to know which case to expect.
- Break-even: set cost equal to revenue. Cost $600 + 4x$ and revenue $19x$ meet at $x = 40$, where both are \$760.
- Two plans: set the two cost lines equal. \$30 + \$5/GB and \$45 + \$2/GB cost the same at 5 GB, \$55.
- Mixtures: one equation counts amounts ($x + y = 12$ kg), the other counts value ($18x + 30y = 12 \times 26$).

Main mistakes:

- Checking only one equation.
- Multiplying an equation without multiplying its constant.
- Sign errors when subtracting equations. Multiplying by $-1$ and adding avoids them.
- Stopping after one unknown. The answer is a pair.
- Reading $0 = 0$ as the solution $(0, 0)$, or as "no solution". It means infinitely many.
