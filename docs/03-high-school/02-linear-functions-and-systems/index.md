# Linear functions and systems

Lines in every form, systems of linear equations in two and three unknowns, and linear inequalities with their feasible regions.

1. [Forms of linear equations](01-forms-of-linear-equations.md)
2. [Systems of linear equations](02-systems-of-linear-equations.md)
3. [Two-variable inequalities and feasible regions](03-two-variable-inequalities-and-feasible-regions.md)

## Cheat sheet

### Forms of linear equations

| Form | Equation | Shows | Use when |
|---|---|---|---|
| slope-intercept | $y = mx + b$ | slope, $y$-intercept | you know a rate and a starting value |
| point-slope | $y - y_1 = m(x - x_1)$ | slope, one point | you know a point and the slope |
| standard | $Ax + By = C$ | both intercepts | two quantities have a fixed total, or the line may be vertical |

- Standard-form convention: $A$, $B$, $C$ integers with no common factor, and $A \ge 0$. For $B \ne 0$ the slope is $-\frac{A}{B}$ and the $y$-intercept is $\frac{C}{B}$. The $x$-intercept is $\frac{C}{A}$.
- Horizontal: $y = k$, slope 0. Vertical: $x = h$, no slope and no slope-intercept form.
- Parallel lines have equal slopes. Perpendicular non-vertical lines have slopes with $m_1 m_2 = -1$, so the second slope is $-\frac{1}{m_1}$. The proof turns the line a quarter turn: $(1, m)$ goes to $(-m, 1)$.
- Through $(x_0, y_0)$: parallel to $Ax + By = C$ is $Ax + By = Ax_0 + By_0$, and perpendicular is $Bx - Ay = Bx_0 - Ay_0$.
- Through two points, $A = y_2 - y_1$, $B = x_1 - x_2$ and $C = Ax_1 + By_1$.
- A linear model has a unit on each variable. The slope is a rate (dollars per year) and the intercept is the starting value. State where the model applies.

Main mistakes:

- Reading the slope of $2x + 3y = 12$ as $\frac{2}{3}$. It is $-\frac{2}{3}$.
- Writing $m(x - 2)$ for the point $(-2, 5)$. It is $m(x + 2)$.
- Flipping only or negating only for a perpendicular slope.
- Multiplying only some terms when clearing fractions.
- Looking for a slope of a vertical line.

### Systems of linear equations

The three elementary operations keep the solutions: swap two equations, multiply one by a nonzero number, add a multiple of one equation to another. Each can be undone, which is why the new system is equivalent.

For $a_1x + b_1y = c_1$ and $a_2x + b_2y = c_2$, let $D = a_1b_2 - a_2b_1$.

| Result | Meaning | Solutions |
|---|---|---|
| $D \ne 0$ | different slopes | one: $x = \frac{c_1b_2 - c_2b_1}{D}$, $y = \frac{a_1c_2 - a_2c_1}{D}$ |
| $D = 0$, elimination leaves $0 = c$ with $c \ne 0$ | parallel | none |
| $D = 0$, elimination leaves $0 = 0$ | same line | infinitely many |

- Three unknowns: remove the same unknown from two pairs of equations, solve the remaining two equations, back-substitute, and check all three originals. A false statement $0 = c$ means no solution. $0 = 0$ means a redundant equation and a free unknown.
- A system never has exactly two solutions. Fewer equations than unknowns never gives exactly one.
- The augmented matrix holds the numbers only. Row operations are the elementary operations, and the goal is a staircase of zeros (Gaussian elimination).
- Equilibrium: set $Q_d = Q_s$. For $Q_d = 150 - 10P$ and $Q_s = 30 + 20P$, $P = 4$ and $Q = 110$.
- Mixture: one equation for the total amount and one for the amount of the active ingredient, with percents as decimals.

Main mistakes:

- Reading $0 = 0$ as "no solution" or as "all unknowns are 0".
- Removing different unknowns in the two moves of a three-unknown system.
- A sign slip when subtracting equations. Check in the original equations.
- Setting prices equal instead of quantities in a supply and demand problem.

### Two-variable inequalities and feasible regions

To graph $Ax + By \le C$ (or $<$, $>$, $\ge$):

1. Draw the line $Ax + By = C$, dashed for $<$ and $>$, solid for $\le$ and $\ge$.
2. Test a point off the line, usually $(0, 0)$.
3. Shade the side where the test is true.

When $y$ is alone, $y > mx + b$ is above the line and $y < mx + b$ is below it. Dividing by a negative number reverses the symbol.

- The feasible region is the overlap of all the shaded half-planes. A corner point is a crossing of two boundary lines that satisfies every other constraint. Solve each pair of boundary equations to get the exact corner.
- Linear program: name the variables, write the constraints and $x \ge 0$, $y \ge 0$, write the objective, find the corners, compute the objective at each, pick the best, and answer with units.
- For a bounded region, the maximum and the minimum of $P = ax + by$ are at corners. The proof slides from any point to the boundary and then along an edge to a corner, since $P$ is a weighted average along a segment.
- Lines of equal value have slope $-\frac{a}{b}$. The best corner depends on how that slope compares with the slopes of the nearby boundary lines.
- Two best corners tie along their whole edge. An unbounded region may have no maximum. An empty region means the constraints conflict (infeasible).
- Budget constraint: $p_xx + p_yy \le I$ with $x, y \ge 0$. Intercepts are $\frac{I}{p_x}$ and $\frac{I}{p_y}$, and the slope $-\frac{p_x}{p_y}$ is the opportunity cost of one more $x$. More income shifts the line parallel. A price change pivots it about the other intercept.

Main mistakes:

- Shading by the look of the symbol instead of with a test point.
- Using $(0, 0)$ as a test point when the line passes through it.
- Calling every crossing of two boundary lines a corner. It must satisfy the other constraints.
- Drawing a solid line for a strict inequality.
- Rounding a corner to whole numbers without checking the constraints.
