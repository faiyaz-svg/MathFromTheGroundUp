# Multivariable optimization and Lagrange multipliers

After this lesson you can find and classify the critical points of a function of two variables with the Hessian, find the absolute maximum and minimum on a closed region, use Lagrange multipliers to optimize under a constraint, solve utility maximization and cost minimization with Cobb-Douglas functions, and say what the multiplier means in economics.

Before this: [partial derivatives and the gradient](02-partial-derivatives-and-the-gradient.md), [optimization](../03-applications-of-derivatives/05-optimization.md) and [eigenvalues and eigenvectors](../06-linear-algebra/08-eigenvalues-and-eigenvectors.md) (the symmetric-matrix part).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find the critical point of $f(x, y) = x^2 - xy + y^2 - 3y$, and say whether it is a minimum, a maximum or a saddle.
2. Use Lagrange multipliers to maximize $xy$ subject to $x + y = 10$.
3. At a critical point, $f_{xx} = 2$, $f_{yy} = 3$ and $f_{xy} = 5$. What is it?

<details class="solution" markdown>
<summary>Answers</summary>

1. $f_x = 2x - y = 0$ and $f_y = -x + 2y - 3 = 0$. The first gives $y = 2x$, and the second then gives $3x = 3$, so the point is $(1, 2)$. The second derivatives are $f_{xx} = 2$, $f_{yy} = 2$ and $f_{xy} = -1$, so $D = 4 - 1 = 3 > 0$ with $f_{xx} > 0$: a minimum, with value $f(1, 2) = -3$.
2. $\nabla(xy) = (y, x)$ and the constraint has gradient $(1, 1)$, so $y = \lambda$ and $x = \lambda$. Then $x = y = 5$ and the product is $25$.
3. $D = f_{xx}f_{yy} - f_{xy}^2 = 6 - 25 = -19 < 0$, so it is a saddle point.

</details>

## The idea

In one variable the best point of a smooth function is where the derivative is zero (or at an end of the interval). With two variables there is more room: from a point you can move in every direction, and the point is flat only if the slope is zero in all of them. That is the condition $\nabla f = \mathbf{0}$, both partial derivatives zero. Flat doesn't mean best: a mountain pass is flat and is the bottom of the pass in one direction and the top in the other, a saddle. To tell the cases apart you look at the curvature in every direction, and the lesson on eigenvalues is what organizes that: the curvature is a symmetric matrix, and its eigenvalues are the curvatures along its principal directions.

Most real problems add a constraint. A consumer maximizes satisfaction, but only among the bundles they can afford. A firm minimizes cost, but only among the input mixes that make a required output. The constraint takes away the freedom to move in every direction: you must stay on a curve. The picture that solves such problems is in the figure below. At the best point on the budget line, the line just touches a level curve of the objective, because at a crossing you could slide along the line to a higher level curve. At a touching point the two curves have the same tangent, so by the last lesson their gradients point the same way: one is a multiple of the other. That multiple is the Lagrange multiplier, and in economics it has a meaning of its own.

![Left, the circle x squared plus y squared equals 5 with parallel grey and red lines x plus 2y equal to a constant. The red line x plus 2y equals 5 touches the circle at (1, 2), where the gradient of f, (1, 2), and the gradient of g, (2, 4), point the same way. The point (1, 2) is marked as the maximum, 5, and (minus 1, minus 2) as the minimum, minus 5. Right, the budget line 2x plus 3y equals 120 from (60, 0) to (0, 40) touches the green curve U = 24 at the bundle (24, 24). The curve U = 15 is below the line and U = 33 above it.](../../assets/figures/05-university-core/multivariable-optimization-and-lagrange-multipliers-lagrange.svg)

## Definitions

A point $\mathbf{a}$ in the domain of $f$ is a **critical point** if $\nabla f(\mathbf{a}) = \mathbf{0}$ (or if $\nabla f$ doesn't exist there). The function has a **local maximum** at $\mathbf{a}$ if $f(\mathbf{x}) \le f(\mathbf{a})$ for all $\mathbf{x}$ near $\mathbf{a}$, a **local minimum** if $f(\mathbf{x}) \ge f(\mathbf{a})$ for all $\mathbf{x}$ near $\mathbf{a}$, and a **saddle point** if $\mathbf{a}$ is a critical point where $f$ takes both larger and smaller values arbitrarily close to $\mathbf{a}$. In plain words, a critical point is a flat spot, and it is a peak, a pit or a pass.

The **Hessian** of $f$ at a point is the matrix of second partial derivatives,

$$
H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix},
$$

and its determinant is $D = f_{xx}f_{yy} - f_{xy}^2$ (the entries $f_{xy}$ and $f_{yx}$ are equal when the second partials are continuous). In plain words, the Hessian is the several-variable version of $f''$: it says how the slope itself changes as you move.

In a **constrained optimization problem** you maximize or minimize an **objective function** $f(x, y)$ over the points satisfying a **constraint** $g(x, y) = c$. The **Lagrange multiplier** is a number $\lambda$ with $\nabla f = \lambda\nabla g$ at the best point. The **Lagrangian** is the function $\mathcal{L}(x, y, \lambda) = f(x, y) - \lambda\bigl(g(x, y) - c\bigr)$, whose three partial derivatives set to zero are exactly the equations $\nabla f = \lambda\nabla g$ and $g = c$.

In economics, **utility maximization** means choosing the bundle $(x, y)$ with the highest utility $U(x, y)$ subject to the **budget constraint** $p_xx + p_yy = m$, where $p_x$ and $p_y$ are prices and $m$ is income. **Cost minimization** means choosing inputs $(K, L)$ with the lowest cost $p_KK + p_LL$ subject to making a required output, $f(K, L) = \bar{Q}$.

## How to do it

### Unconstrained problems: the second derivative test

1. Compute $f_x$ and $f_y$, set both to $0$, and solve the two equations together. Each solution is a critical point.
2. Compute $f_{xx}$, $f_{yy}$ and $f_{xy}$ and evaluate them at each critical point.
3. Compute $D = f_{xx}f_{yy} - f_{xy}^2$ and apply the test below.
4. Check by evaluating $f$ at nearby points, or by comparing with a simpler version of the problem.

*Theorem 1 (second derivative test).* Let $f$ have continuous second partial derivatives near a critical point $\mathbf{a}$, and let $D$ be the determinant of the Hessian at $\mathbf{a}$. If $D > 0$ and $f_{xx} > 0$, then $\mathbf{a}$ is a local minimum. If $D > 0$ and $f_{xx} < 0$, it is a local maximum. If $D < 0$, it is a saddle point. If $D = 0$, the test gives no information.

What we know: the lesson on eigenvalues, where a symmetric matrix $H$ has two real eigenvalues $\lambda_1$ and $\lambda_2$ and two perpendicular eigenvectors, with $\lambda_1\lambda_2 = \det H$. We also use the second-order Taylor expansion of a function of two variables, stated without proof: near a critical point (where the first-order terms vanish),

$$
f(\mathbf{a} + \mathbf{h}) = f(\mathbf{a}) + \tfrac{1}{2}\,\mathbf{h}^TH\mathbf{h} + \text{error},
$$

with an error much smaller than $\lVert \mathbf{h} \rVert^2$. What we want: the sign of $\mathbf{h}^TH\mathbf{h}$ for every direction $\mathbf{h}$. The plan: rotate to the eigenvector axes, where $\mathbf{h}^TH\mathbf{h}$ is a sum of two terms with the signs of the eigenvalues.

*Proof.* The Hessian is symmetric, so by the spectral theorem of the eigenvalue lesson it has perpendicular unit eigenvectors $\mathbf{q}_1$ and $\mathbf{q}_2$ with eigenvalues $\lambda_1$ and $\lambda_2$. Write $\mathbf{h} = u\mathbf{q}_1 + v\mathbf{q}_2$. Then $\mathbf{h}^TH\mathbf{h} = \lambda_1u^2 + \lambda_2v^2$ and $\lVert \mathbf{h} \rVert^2 = u^2 + v^2$. Also $D = \lambda_1\lambda_2$, so $D > 0$ means that the eigenvalues have the same sign, and $D < 0$ means opposite signs.

If $D > 0$, the number $f_{xx} = \mathbf{e}_1^TH\mathbf{e}_1$ (with $\mathbf{e}_1 = (1, 0)$) is a combination $\lambda_1c^2 + \lambda_2s^2$ of the eigenvalues with weights $c^2 + s^2 = 1$, so it has their common sign. If both eigenvalues are positive, then $\mathbf{h}^TH\mathbf{h} \ge \min(\lambda_1, \lambda_2)\lVert \mathbf{h} \rVert^2$, a positive multiple of $\lVert \mathbf{h} \rVert^2$ that beats the error for small $\mathbf{h}$, so $f(\mathbf{a} + \mathbf{h}) > f(\mathbf{a})$ near $\mathbf{a}$: a local minimum. If both are negative, the same argument gives a local maximum. If $D < 0$, say $\lambda_1 > 0 > \lambda_2$, then moving along $\mathbf{q}_1$ raises $f$ and moving along $\mathbf{q}_2$ lowers it, so there is a saddle. For $D = 0$, an eigenvalue is $0$ and the quadratic term says nothing in that direction. $\blacksquare$

Look back: behind the test is a statement about eigenvalues. Both positive is a bowl, both negative is a dome, opposite signs is a saddle. The functions $x^4 + y^4$ and $-x^4 - y^4$ both have $H = 0$ at the origin, one a minimum and the other a maximum, which is why $D = 0$ gives nothing. For three or more variables the test is the same in terms of eigenvalues: all positive means a local minimum, all negative a local maximum, and mixed signs a saddle.

![Contours of f(x, y) = x cubed plus y cubed minus 3xy. The blue level curve f = 0 forms a loop through the origin, where it crosses itself, and the origin is marked in red as a saddle point. Inside the loop, small dashed ellipses close in on the point (1, 1), marked in green as a minimum with f = minus 1. Contours outside the loop open away.](../../assets/figures/05-university-core/multivariable-optimization-and-lagrange-multipliers-critical.svg)

### Absolute extrema on a closed bounded region

Local extrema say how $f$ behaves nearby. The best point over a whole region may be on its edge. The tool is the *extreme value theorem* (stated): a continuous function on a closed, bounded region has an absolute maximum and an absolute minimum. The method extends the closed interval method of the one-variable lesson.

1. Find the critical points inside the region.
2. Find the extreme values of $f$ on the boundary. Parametrize each edge so that it is a one-variable problem, or use Lagrange multipliers, and include the corners.
3. Compare the values of $f$ at all the candidates. The largest is the absolute maximum and the smallest is the absolute minimum.

### Constrained problems: Lagrange multipliers

*Theorem 2 (Lagrange).* Let $f$ and $g$ have continuous partial derivatives. Suppose $f$ has a local maximum or minimum at $\mathbf{a}$ among the points with $g(\mathbf{x}) = c$, and $\nabla g(\mathbf{a}) \ne \mathbf{0}$. Then there is a number $\lambda$ with $\nabla f(\mathbf{a}) = \lambda\nabla g(\mathbf{a})$.

What we know: the gradient is perpendicular to level curves (Theorem 3 of the last lesson), and the constraint is a level curve of $g$. What we want: $\nabla f$ is a multiple of $\nabla g$. The plan, for two variables: because $\nabla g \ne \mathbf{0}$, the constraint curve is a smooth curve near $\mathbf{a}$ (this is the implicit function theorem, stated). Walk along it and apply the one-variable test to $f$ restricted to the curve.

*Proof (two variables).* Let $\mathbf{r}(t)$ be a smooth path along the constraint curve with $\mathbf{r}(0) = \mathbf{a}$ and $\mathbf{r}'(0) \ne \mathbf{0}$. The function $h(t) = f(\mathbf{r}(t))$ of one variable has a local extremum at $t = 0$, so $h'(0) = 0$. By the chain rule, $h'(0) = \nabla f(\mathbf{a}) \cdot \mathbf{r}'(0) = 0$. On the other hand $g(\mathbf{r}(t)) = c$ for all $t$, so differentiating gives $\nabla g(\mathbf{a}) \cdot \mathbf{r}'(0) = 0$. In the plane, the vectors perpendicular to the nonzero vector $\mathbf{r}'(0)$ form a line. Both $\nabla f(\mathbf{a})$ and $\nabla g(\mathbf{a})$ lie on that line, and $\nabla g(\mathbf{a}) \ne \mathbf{0}$, so $\nabla f(\mathbf{a})$ is a multiple $\lambda\nabla g(\mathbf{a})$. $\blacksquare$

Look back: the proof is the picture. Both gradients are perpendicular to the same tangent direction, so they are parallel. The assumption $\nabla g \ne \mathbf{0}$ matters, and the cusp in the edge cases below shows what goes wrong without it. For three variables the same proof works with the path in the tangent plane of the constraint surface, and with several constraints $g_1 = c_1$, $g_2 = c_2$ there is one multiplier for each: $\nabla f = \lambda_1\nabla g_1 + \lambda_2\nabla g_2$.

The method:

1. Write the objective $f$ and the constraint as $g(x, y) = c$.
2. Write the equations $f_x = \lambda g_x$, $f_y = \lambda g_y$ and $g(x, y) = c$: three equations in the three unknowns $x$, $y$ and $\lambda$.
3. Solve. A good way is to divide the first two equations to eliminate $\lambda$ (watch for a variable that could be $0$), solve the resulting relation between $x$ and $y$, and substitute into the constraint.
4. List every solution, together with the points where $\nabla g = \mathbf{0}$ and the endpoints of the constraint curve if it has any.
5. Evaluate $f$ at each candidate and compare. If the constraint set is closed and bounded, the largest and smallest values are the maximum and the minimum.
6. Check: the constraint holds at the answer, and nearby points on the constraint give a worse value.

### The multiplier in economics

In the utility problem, the equation $\nabla U = \lambda\mathbf{p}$ with $\mathbf{p} = (p_x, p_y)$ says

$$
\frac{U_x}{p_x} = \frac{U_y}{p_y} = \lambda, \qquad\text{equivalently}\qquad \frac{U_x}{U_y} = \frac{p_x}{p_y}.
$$

In plain words, at the best bundle the extra utility per dollar is the same for both goods, and the ratio of marginal utilities (the marginal rate of substitution, the slope of the indifference curve) equals the price ratio, the slope of the budget line. If the extra utility per dollar were higher for good $x$, moving a dollar from $y$ to $x$ would raise utility.

The number $\lambda$ is the **marginal utility of income**: how much the best attainable utility rises per extra dollar of income. The reason is short. If income rises by a small amount $dm$, the best bundle moves by $(dx, dy)$ with $p_x\,dx + p_y\,dy = dm$, and the utility changes by

$$
dU = U_x\,dx + U_y\,dy = \lambda(p_x\,dx + p_y\,dy) = \lambda\,dm.
$$

This is a first-order argument, and the full statement (the envelope theorem) is a result of an economics course, though Example 4 checks it directly. The same argument applies to cost minimization. There $\nabla C = \lambda\nabla f$ and $\lambda$ is the **marginal cost** of the output, the extra cost of one more unit of the required output $\bar{Q}$.

For Cobb-Douglas utility $U = x^ay^{1-a}$ with $0 < a < 1$, solving the conditions gives $p_xx = am$ and $p_yy = (1 - a)m$: the consumer spends the fixed share $a$ of income on $x$ and $1 - a$ on $y$, whatever the prices. Example 4 shows the steps with numbers.

## Worked examples

<div class="example" markdown>

### Example 1: classify the critical points

Find and classify the critical points of $f(x, y) = x^3 + y^3 - 3xy$.

Step 1: $f_x = 3x^2 - 3y = 0$ gives $y = x^2$, and $f_y = 3y^2 - 3x = 0$ gives $x = y^2$. Substituting, $x = (x^2)^2 = x^4$, so $x(x^3 - 1) = 0$ and $x = 0$ or $x = 1$ (the only real roots). The critical points are $(0, 0)$ and $(1, 1)$.

Step 2: the second derivatives are $f_{xx} = 6x$, $f_{yy} = 6y$ and $f_{xy} = -3$.

Step 3: at $(0, 0)$, $D = 0 \cdot 0 - 9 = -9 < 0$, a saddle. At $(1, 1)$, $D = 36 - 9 = 27 > 0$ and $f_{xx} = 6 > 0$, a local minimum with $f(1, 1) = -1$.

Step 4, the check: $f(0.1, 0.1) = -0.028$ is below $f(0, 0) = 0$ and $f(0.1, -0.1) = 0.03$ is above it, which is a saddle. And $f(1.1, 1.1) = -0.968$ is above $-1$. In terms of eigenvalues, the Hessian at $(1, 1)$ is $\begin{pmatrix} 6 & -3 \\ -3 & 6 \end{pmatrix}$ with eigenvalues $3$ and $9$, both positive, and at the origin $\begin{pmatrix} 0 & -3 \\ -3 & 0 \end{pmatrix}$ has eigenvalues $3$ and $-3$. The minimum is only local: $f(x, 0) = x^3$ goes to $-\infty$.

</div>

<div class="example" markdown>

### Example 2: absolute extrema on a triangle

Find the absolute maximum and minimum of $f(x, y) = x^2 - 2x + y^2 - 2y$ on the triangle with vertices $(0, 0)$, $(3, 0)$ and $(0, 3)$.

Interior: $f_x = 2x - 2 = 0$ and $f_y = 2y - 2 = 0$ give $(1, 1)$, which is inside (since $1 + 1 < 3$), with $f = -2$.

Bottom edge, $y = 0$ and $0 \le x \le 3$: $f = x^2 - 2x$, which has its minimum $-1$ at $x = 1$ and endpoint values $f(0, 0) = 0$ and $f(3, 0) = 3$. The left edge $x = 0$ is the same by symmetry: minimum $-1$ at $(0, 1)$, and $f(0, 3) = 3$.

Slanted edge, $y = 3 - x$: $f = x^2 - 2x + (3 - x)^2 - 2(3 - x) = 2x^2 - 6x + 3$, which has its minimum at $x = 1.5$ with $f = -1.5$, and endpoint values $3$ and $3$.

Compare: the candidates are $-2$, $-1$, $-1$, $-1.5$, $0$, $3$ and $3$. The absolute maximum is $3$, at the corners $(3, 0)$ and $(0, 3)$, and the absolute minimum is $-2$ at $(1, 1)$.

Check: $f$ is the squared distance from $(1, 1)$ minus 2, since $f = (x - 1)^2 + (y - 1)^2 - 2$. The nearest point of the triangle to $(1, 1)$ is $(1, 1)$ itself, and the farthest corner is $(3, 0)$ or $(0, 3)$ at squared distance $5$, so $f$ ranges from $-2$ to $3$.

</div>

<div class="example" markdown>

### Example 3: the geometry of a Lagrange problem

Maximize and minimize $f(x, y) = x + 2y$ on the circle $x^2 + y^2 = 5$.

Step 1 and 2: $g = x^2 + y^2$ and $c = 5$. Then $\nabla f = (1, 2)$ and $\nabla g = (2x, 2y)$, so $1 = 2\lambda x$ and $2 = 2\lambda y$.

Step 3: dividing the second equation by the first (the first shows that $x \ne 0$) gives $\frac{y}{x} = 2$, so $y = 2x$. The constraint becomes $x^2 + 4x^2 = 5$, so $x = \pm 1$.

Steps 4 and 5: the candidates are $(1, 2)$ with $f = 5$ and $\lambda = \frac{1}{2}$, and $(-1, -2)$ with $f = -5$ and $\lambda = -\frac{1}{2}$. The circle is closed and bounded and $\nabla g = \mathbf{0}$ only at the origin, which is not on it, so the maximum is $5$ at $(1, 2)$ and the minimum is $-5$ at $(-1, -2)$.

Step 6, the check: the numerical walk around the circle in the "In code" section finds the same maximum. In the figure, the line $x + 2y = 5$ touches the circle at $(1, 2)$, and $\nabla f = (1, 2)$ is half of $\nabla g = (2, 4)$. The Cauchy-Schwarz bound agrees: $x + 2y = (1, 2) \cdot (x, y) \le \sqrt{5}\sqrt{5} = 5$.

</div>

<div class="example" markdown>

### Example 4: utility maximization

A consumer has utility $U(x, y) = x^{0.4}y^{0.6}$, faces the prices $p_x = \$2$ and $p_y = \$3$, and has an income of \$120. Find the best bundle, and what the multiplier means.

Step 1 and 2: maximize $U$ subject to $2x + 3y = 120$. The conditions are $U_x = 2\lambda$ and $U_y = 3\lambda$, with $U_x = 0.4\frac{U}{x}$ and $U_y = 0.6\frac{U}{y}$.

Step 3: dividing, $\frac{U_x}{U_y} = \frac{0.4y}{0.6x} = \frac{2}{3}$. Cross-multiplying, $1.2y = 1.2x$, so $y = x$. The budget becomes $2x + 3x = 120$, so $x = y = 24$.

Step 4 and 5: the bundle is $(24, 24)$ with utility $U = 24^{0.4}\cdot 24^{0.6} = 24$. (The axes give $U = 0$, and the constraint set is bounded, so the interior solution is the maximum.) The consumer spends $2 \cdot 24 = \$48$, which is 40% of the income, on $x$ and \$72, which is 60%, on $y$.

The multiplier: $U_x = 0.4 \cdot \frac{24}{24} = 0.4$, so $\lambda = \frac{0.4}{2} = 0.2$. The check with $y$ agrees: $U_y = 0.6$ and $\frac{0.6}{3} = 0.2$. With income $m$ the same steps give $x = y = \frac{m}{5}$ and $U = \frac{m}{5}$, so the best utility rises by $0.2$ per extra dollar, which is $\lambda$: an extra dollar of income, \$121 instead of \$120, gives $U = 24.2$.

Step 6, the check on the constraint: $2(24) + 3(24) = 120$. Nearby affordable bundles do worse: $(30, 20)$ costs $60 + 60 = 120$ and gives $30^{0.4}20^{0.6} \approx 23.52$, and $\left(20, \frac{80}{3}\right)$ gives $20^{0.4}\left(\frac{80}{3}\right)^{0.6} \approx 23.77$. Both are below $24$.

</div>

<div class="example" markdown>

### Example 5: cost minimization

A hypothetical firm makes output with $Q = K^{0.3}L^{0.7}$. Capital costs \$3 a unit and labour costs \$7 an hour. What is the cheapest way to make $Q = 100$, and what is the marginal cost?

The objective is $C = 3K + 7L$ and the constraint is $K^{0.3}L^{0.7} = 100$. The conditions $\nabla C = \lambda\nabla Q$ are $3 = \lambda \cdot 0.3\frac{Q}{K}$ and $7 = \lambda \cdot 0.7\frac{Q}{L}$. With $Q = 100$ they give $K = 10\lambda$ and $L = 10\lambda$, so $K = L$. The constraint then reads $K^{0.3}K^{0.7} = K = 100$, so $K = L = 100$, $\lambda = 10$ and the cost is $3 \cdot 100 + 7 \cdot 100 = \$1000$.

Check on the marginal cost: for a general output $Q$ the same steps give $K = L = Q$ and cost $10Q$, so one more unit of output costs \$10 more, which is $\lambda$. The numerical search in the "In code" section gives \$1000 for $Q = 100$ and an extra \$10 for $Q = 101$. The figure shows the tangency: the isocost line $3K + 7L = 1000$ touches the isoquant at $(100, 100)$, and the line for cost 800 misses it, while the line for cost 1300 crosses it twice and is not the cheapest.

![The curved isoquant K to the 0.3 times L to the 0.7 equals 100 in green, falling steeply on the left and flattening on the right. Three straight isocost lines of slope minus 3 over 7: cost 800 below the curve, cost 1000 in red touching the curve at (100, 100), and cost 1300 above it, crossing it twice. The point (100, 100) is marked as the cheapest way.](../../assets/figures/05-university-core/multivariable-optimization-and-lagrange-multipliers-cost.svg)

At the tangency the isoquant slope $-\frac{Q_K}{Q_L} = -\frac{3}{7}$ equals the slope of the isocost line, $-\frac{p_K}{p_L}$. In words, the firm hires inputs until the extra output per dollar is the same for both.

</div>

<div class="example" markdown>

### Example 6: a least-squares check

For the points $(1, 2)$, $(2, 3)$ and $(3, 5)$ the sum of squared errors of the line $y = w_0 + w_1x$ is $S(w_0, w_1) = \sum(w_0 + w_1x_i - y_i)^2$. Show that its critical point is the least-squares line and that it is a minimum.

Step 1: $S_{w_0} = 2\sum(w_0 + w_1x_i - y_i) = 6w_0 + 12w_1 - 20$ and $S_{w_1} = 2\sum x_i(w_0 + w_1x_i - y_i) = 12w_0 + 28w_1 - 46$. Setting both to $0$ gives $3w_0 + 6w_1 = 10$ and $6w_0 + 14w_1 = 23$. Subtracting twice the first from the second, $2w_1 = 3$, so $w_1 = 1.5$ and $w_0 = \frac{1}{3}$.

Step 2: the Hessian is $\begin{pmatrix} 6 & 12 \\ 12 & 28 \end{pmatrix}$ and $D = 168 - 144 = 24 > 0$ with $S_{w_0w_0} = 6 > 0$, so the critical point is a local minimum. Its eigenvalues are $0.72$ and $33.28$, both positive.

Check: these are the normal equations $A^TA\mathbf{w} = A^T\mathbf{y}$ of [orthogonality, projections and least squares](../06-linear-algebra/07-orthogonality-projections-and-least-squares.md) with $A^TA = \begin{pmatrix} 3 & 6 \\ 6 & 14 \end{pmatrix}$, and the Hessian is $2A^TA$. The Hessian doesn't depend on $\mathbf{w}$, so the surface is a single bowl and the local minimum is the absolute minimum. The same bowl is the one that gradient descent runs on in the last lesson.

</div>

<div class="example" markdown>

### Example 7: a budget problem (finish it yourself)

A consumer maximizes $U(x, y) = xy$ subject to the budget $2x + 5y = 100$. The conditions are $y = 2\lambda$ and $x = 5\lambda$.

Substitute them into the budget to find $\lambda$, then $x$, $y$ and the utility, and check that $\lambda$ is the marginal utility of income.

<details class="solution" markdown>
<summary>Finish</summary>

The budget gives $2(5\lambda) + 5(2\lambda) = 20\lambda = 100$, so $\lambda = 5$, $x = 25$, $y = 10$ and $U = 250$.

Check: with income $m$ the same steps give $20\lambda = m$, $x = \frac{m}{4}$, $y = \frac{m}{10}$ and $U = \frac{m^2}{40}$, so $\frac{dU}{dm} = \frac{m}{20} = 5$ at $m = 100$, which is $\lambda$. Also $\frac{U_x}{p_x} = \frac{10}{2} = 5$ and $\frac{U_y}{p_y} = \frac{25}{5} = 5$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: $D = 0$ means the test is silent, not that the point is a saddle. At the origin both $x^4 + y^4$ (a minimum) and $x^3 + y^3$ (neither, since $f(t, 0) = t^3$ changes sign) have $D = 0$. Look at the function's values near the point.

</div>

<div class="warning" markdown>

Watch out: forgetting the boundary. A function on a closed region can have its best value on the edge with no critical point there at all. In Example 2 the maximum is at corners that are not critical points. Check the interior, then every edge and corner.

</div>

<div class="warning" markdown>

Watch out: the condition $\nabla g \ne \mathbf{0}$. Minimize $f(x, y) = x$ on the curve $y^2 = x^3$. The curve has a cusp at the origin, and the smallest value of $x$ on it is $0$, at the origin. But there $\nabla g = (-3x^2, 2y) = (0, 0)$, and no number $\lambda$ makes $\nabla f = (1, 0)$ equal to $\lambda(0, 0)$. The method misses this minimum. Always list the points where $\nabla g = \mathbf{0}$ as extra candidates.

</div>

<div class="warning" markdown>

Watch out: dividing by a variable that could be zero. Dividing the equation $1 = 2\lambda x$ by $x$ is only allowed if $x \ne 0$, and in Example 3 the equation itself shows that $x \ne 0$. In other problems $x = 0$ can be a solution that the division loses. Check the case $x = 0$ separately.

</div>

<div class="warning" markdown>

Watch out: stopping at the critical point of the Lagrangian without comparing values. The equations give all candidates, including both the maximum and the minimum (Example 3 has both). Evaluate $f$ at each. Also, the equations don't say which is which: the sign of $\lambda$ doesn't tell you either.

</div>

<div class="warning" markdown>

Watch out: a local minimum is not an absolute minimum. In Example 1 the point $(1, 1)$ is a local minimum of a function with no lower bound. For an absolute claim, use a closed bounded region, or a convexity argument like the one in Example 6.

</div>

## Tricks and shortcuts

If the constraint is easy to solve for one variable, substitute and use one-variable calculus instead. For the budget $2x + 3y = 120$, put $y = \frac{120 - 2x}{3}$ into $U$ and differentiate. Lagrange multipliers are for constraints that can't be solved so easily, and for getting the multiplier.

For a two-good problem the answer is the tangency condition (the ratio of marginal values equals the ratio of prices) plus the constraint. You can write this down at once, without the multiplier: $\frac{U_x}{U_y} = \frac{p_x}{p_y}$ and $p_xx + p_yy = m$. For Cobb-Douglas utility skip even that, and use the spending shares: a fraction $a$ of income goes to $x$.

For a $2 \times 2$ Hessian, $D = f_{xx}f_{yy} - f_{xy}^2$ and the trace $f_{xx} + f_{yy}$ tell you the eigenvalues' signs: $D > 0$ and trace $> 0$ means both positive. A fast saddle test is $f_{xx}f_{yy} < f_{xy}^2$.

To check a candidate on a constraint, move a little along the constraint curve in each direction and see that $f$ gets worse. This is the numerical check of Example 3 and Example 4.

## In code

The Hessian classification of Example 1 with eigenvalues, a brute-force search along the constraint for Examples 3 to 5 (which confirms the multipliers as the change in the best value), and the normal equations of Example 6.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

# Classify the critical points of f = x^3 + y^3 - 3xy with the Hessian.
def hessian(x, y):
    return np.array([[6 * x, -3], [-3, 6 * y]])

for point in [(0, 0), (1, 1)]:
    H = hessian(*point)
    print(point, np.round(np.linalg.eigvalsh(H), 4), round(np.linalg.det(H), 4))
# (0, 0) [-3.  3.] -9.0
# (1, 1) [3. 9.] 27.0

# Maximize f = x + 2y on the circle x^2 + y^2 = 5 by walking around the circle.
t = np.linspace(0, 2 * np.pi, 1_000_001)
x, y = np.sqrt(5) * np.cos(t), np.sqrt(5) * np.sin(t)
i = np.argmax(x + 2 * y)
print(round(x[i], 3), round(y[i], 3), round((x + 2 * y)[i], 4))
# 1.0 2.0 5.0

# Utility x^0.4 y^0.6 on the budget line 2x + 3y = m: search along the line.
def best_utility(m):
    xs = np.linspace(0.001, m / 2 - 0.001, 400_001)
    ys = (m - 2 * xs) / 3
    u = xs ** 0.4 * ys ** 0.6
    i = np.argmax(u)
    return xs[i], ys[i], u[i]

x1, y1, u1 = best_utility(120)
print(round(x1, 2), round(y1, 2), round(u1, 4))
# 24.0 24.0 24.0
print(round(best_utility(121)[2] - u1, 4))
# 0.2

# Cheapest way to make Q = K^0.3 L^0.7 = 100 at input prices 3 and 7.
K = np.linspace(1, 1000, 1_000_000)
L = (100 / K ** 0.3) ** (1 / 0.7)
c = 3 * K + 7 * L
i = np.argmin(c)
print(round(K[i], 1), round(L[i], 1), round(c[i], 2))
# 100.0 100.0 1000.0
Lq = (101 / K ** 0.3) ** (1 / 0.7)
print(round((3 * K + 7 * Lq).min() - c[i], 3))
# 10.0

# A least-squares line: set both partial derivatives of the sum of squares to 0.
X = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)
yv = np.array([2, 3, 5], dtype=float)
H = 2 * X.T @ X
w = np.linalg.solve(H, 2 * X.T @ yv)
print(np.round(w, 4), np.round(np.linalg.eigvalsh(H), 4))
# [0.3333 1.5   ] [ 0.7212 33.2788]
```

The extra \$1 of income raises the best utility by $0.2$, and the extra unit of output costs an extra \$10. These are the multipliers, found by brute force and not by the Lagrange equations.

</details>

## FAQ

### Why does the best point on a constraint have parallel gradients?

If the gradients weren't parallel, the level curve of $f$ would cross the constraint curve there, and sliding along the constraint to one side of the crossing would raise $f$ while sliding to the other side would lower it. So the point couldn't be a maximum or a minimum. At the best point the level curve of $f$ touches the constraint and has the same tangent, and since a gradient is perpendicular to the tangent of its level curve, the gradients point along the same line.

### What does a multiplier of zero mean?

That the constraint isn't really limiting: the best point of the objective already satisfies it, so relaxing it by a little changes nothing. For example, maximizing $-(x - 1)^2 - (y - 1)^2$ subject to $x + y = 2$ gives the point $(1, 1)$, which is the unconstrained maximum, and the multiplier is $0$. In economics, a multiplier of zero is a budget that a satiated consumer doesn't need.

### Can I use Lagrange multipliers with an inequality constraint?

Yes, in a more general form (the Karush-Kuhn-Tucker conditions), where the multiplier is not allowed to be negative and is zero when the constraint isn't binding. This book stays with equality constraints. For a budget $p_xx + p_yy \le m$ with a utility that always increases with more goods, the consumer spends everything, so the constraint can be treated as an equation.

### Why are the Hessian and the eigenvalues connected?

Because the Hessian is a symmetric matrix, and a symmetric matrix is a stretch along perpendicular axes (the spectral theorem). The curvature of $f$ in a direction is how much the matrix stretches that direction, and the eigenvalues are the stretch factors along the special axes. "Bowl" means the matrix stretches every direction by a positive amount.

## Practice

### Warm-up

1\. Find and classify the critical point of $f(x, y) = x^2 + y^2 - 4x + 6y$, and give the value of $f$ there.

<details class="solution" markdown>
<summary>Solution</summary>

$f_x = 2x - 4 = 0$ and $f_y = 2y + 6 = 0$ give $(2, -3)$. Then $f_{xx} = 2$, $f_{yy} = 2$, $f_{xy} = 0$, so $D = 4 > 0$ with $f_{xx} > 0$: a local minimum, and in fact the absolute one since $f = (x - 2)^2 + (y + 3)^2 - 13$. The value is $f(2, -3) = -13$.

Check: completing the squares gives the same value $-13$ and shows that the bowl is a paraboloid with its lowest point at $(2, -3)$.

</details>

2\. Find and classify the critical points of $f(x, y) = x^3 - 3x + y^2$.

<details class="solution" markdown>
<summary>Solution</summary>

$f_x = 3x^2 - 3 = 0$ gives $x = \pm 1$, and $f_y = 2y = 0$ gives $y = 0$. The critical points are $(1, 0)$ and $(-1, 0)$. The second derivatives are $f_{xx} = 6x$, $f_{yy} = 2$ and $f_{xy} = 0$, so $D = 12x$. At $(1, 0)$, $D = 12 > 0$ and $f_{xx} = 6 > 0$, a local minimum with $f = -2$. At $(-1, 0)$, $D = -12 < 0$, a saddle with $f = 2$.

Check: along the $x$-axis $f = x^3 - 3x$ has a local minimum at $x = 1$ and a local maximum at $x = -1$, and in the $y$ direction it is the upward parabola $y^2$. At $(-1, 0)$ it goes up in one direction and down in the other, a saddle.

</details>

3\. Minimize $x^2 + y^2$ subject to $x + y = 4$ using a Lagrange multiplier.

<details class="solution" markdown>
<summary>Solution</summary>

$\nabla f = (2x, 2y) = \lambda(1, 1)$, so $x = y = \frac{\lambda}{2}$. The constraint gives $2x = 4$, so $x = y = 2$, $\lambda = 4$ and the minimum value is $8$.

Check: by substituting $y = 4 - x$, $f = x^2 + (4 - x)^2 = 2x^2 - 8x + 16$ has its minimum at $x = 2$, with $f = 8 - 16 + 16 = 8$. Also $\sqrt{8} = 2\sqrt{2}$ is the distance from the origin to the line $x + y = 4$.

</details>

### Standard

4\. A consumer with utility $U = \sqrt{xy}$ has an income of \$80, with $p_x = \$4$ and $p_y = \$1$. Find the best bundle, the utility, and the multiplier, and check that the multiplier is the marginal utility of income.

<details class="solution" markdown>
<summary>Solution</summary>

The tangency condition is $\frac{U_x}{U_y} = \frac{y}{x} = \frac{p_x}{p_y} = 4$, so $y = 4x$. The budget $4x + y = 80$ becomes $8x = 80$, so $x = 10$ and $y = 40$. The utility is $\sqrt{400} = 20$. The multiplier is $\lambda = \frac{U_x}{p_x} = \frac{0.5\sqrt{y/x}}{4} = \frac{0.5 \cdot 2}{4} = 0.25$.

Check: with income $m$ the same steps give $x = \frac{m}{8}$, $y = \frac{m}{2}$ and $U = \sqrt{\frac{m^2}{16}} = \frac{m}{4}$, so $\frac{dU}{dm} = 0.25 = \lambda$. The spending shares are $\frac{40}{80} = 50\%$ on each good, as for $U = x^{0.5}y^{0.5}$.

</details>

5\. A firm makes $Q = \sqrt{KL}$ with input prices $p_K = \$4$ and $p_L = \$9$. Find the cheapest inputs for $Q = 60$ and the marginal cost.

<details class="solution" markdown>
<summary>Solution</summary>

The tangency condition is $\frac{Q_L}{Q_K} = \frac{K}{L} = \frac{p_L}{p_K} = \frac{9}{4}$, so $K = 2.25L$. The constraint $\sqrt{2.25L \cdot L} = 1.5L = 60$ gives $L = 40$ and $K = 90$. The cost is $4 \cdot 90 + 9 \cdot 40 = 360 + 360 = \$720$. The multiplier is $\lambda = \frac{p_K}{Q_K} = \frac{4}{0.5\sqrt{L/K}} = \frac{4}{0.5 \cdot \frac{2}{3}} = 12$.

Check: for any output $Q$ the same steps give a cost of $2\sqrt{p_Kp_L}\,Q = 12Q$, which is \$720 at $Q = 60$, and the marginal cost is \$12 per unit, equal to $\lambda$.

</details>

6\. Find the absolute maximum and minimum of $f(x, y) = xy$ on the disc $x^2 + y^2 \le 2$.

<details class="solution" markdown>
<summary>Solution</summary>

Interior: $\nabla f = (y, x) = \mathbf{0}$ at $(0, 0)$, with $f = 0$. Boundary $x^2 + y^2 = 2$: the conditions $y = 2\lambda x$ and $x = 2\lambda y$ give $x = 4\lambda^2x$. Since $x = 0$ would force $y = 0$, which is not on the circle, $\lambda = \pm\frac{1}{2}$, so $y = \pm x$. The points are $(1, 1)$ and $(-1, -1)$ with $f = 1$, and $(1, -1)$ and $(-1, 1)$ with $f = -1$. The absolute maximum is $1$ and the absolute minimum is $-1$.

Check: on the circle, $2xy \le x^2 + y^2 = 2$ because $(x - y)^2 \ge 0$, so $xy \le 1$, with equality when $x = y$. Similarly $(x + y)^2 \ge 0$ gives $xy \ge -1$.

</details>

### Challenge

7\. (a) Minimize $x^2 + y^2 + z^2$ subject to $x + 2y + 2z = 9$ with a Lagrange multiplier. (b) For a vector $\mathbf{a} \ne \mathbf{0}$ and a number $b$, show that the point of the plane $\mathbf{a} \cdot \mathbf{x} = b$ closest to the origin is $\frac{b}{\lVert \mathbf{a} \rVert^2}\mathbf{a}$, with the squared distance $\frac{b^2}{\lVert \mathbf{a} \rVert^2}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\nabla f = (2x, 2y, 2z) = \lambda(1, 2, 2)$, so $x = \frac{\lambda}{2}$, $y = \lambda$, $z = \lambda$. The constraint gives $\frac{\lambda}{2} + 2\lambda + 2\lambda = \frac{9\lambda}{2} = 9$, so $\lambda = 2$ and the point is $(1, 2, 2)$, with minimum value $1 + 4 + 4 = 9$.

(b) The condition $2\mathbf{x} = \lambda\mathbf{a}$ gives $\mathbf{x} = \frac{\lambda}{2}\mathbf{a}$. The constraint gives $\frac{\lambda}{2}\lVert \mathbf{a} \rVert^2 = b$, so $\frac{\lambda}{2} = \frac{b}{\lVert \mathbf{a} \rVert^2}$ and $\mathbf{x} = \frac{b}{\lVert \mathbf{a} \rVert^2}\mathbf{a}$, with $\lVert \mathbf{x} \rVert^2 = \frac{b^2}{\lVert \mathbf{a} \rVert^4}\lVert \mathbf{a} \rVert^2 = \frac{b^2}{\lVert \mathbf{a} \rVert^2}$. This is the minimum because the quantity is a convex bowl, and the constraint set is a plane. Part (a) is the case $\mathbf{a} = (1, 2, 2)$, $b = 9$, $\lVert \mathbf{a} \rVert^2 = 9$.

Check with the Cauchy-Schwarz inequality: $b = \mathbf{a} \cdot \mathbf{x} \le \lVert \mathbf{a} \rVert\lVert \mathbf{x} \rVert$ gives $\lVert \mathbf{x} \rVert^2 \ge \frac{b^2}{\lVert \mathbf{a} \rVert^2}$, with equality for $\mathbf{x}$ a multiple of $\mathbf{a}$. The distance from the origin to the plane in (a) is $\sqrt{9} = 3$, which is $\frac{9}{\sqrt{9}}$, matching the distance formula of [parametric, polar and 3D coordinates](01-parametric-polar-and-3d-coordinates.md).

</details>

8\. (Reviews [optimization](../03-applications-of-derivatives/05-optimization.md).) A firm sells two products with the profit function $P(x, y) = 60x + 48y - 3x^2 - 2y^2 - 2xy$ thousand dollars, where $x$ and $y$ are the quantities in thousands. Find the profit-maximizing quantities and the maximum profit, and show that it is a maximum.

<details class="solution" markdown>
<summary>Solution</summary>

The marginal profits are $P_x = 60 - 6x - 2y$ and $P_y = 48 - 4y - 2x$. Setting both to $0$, the second gives $x = 24 - 2y$. Substituting into the first, $60 - 6(24 - 2y) - 2y = -84 + 10y = 0$, so $y = 8.4$ and $x = 7.2$. The profit is $P = 432 + 403.2 - 155.52 - 141.12 - 120.96 = 417.6$, that is \$417,600.

The second derivatives are $P_{xx} = -6$, $P_{yy} = -4$ and $P_{xy} = -2$, so $D = 24 - 4 = 20 > 0$ with $P_{xx} < 0$: a local maximum. The Hessian has the same negative-definite sign everywhere, so $P$ is a dome and this is the absolute maximum.

Check: $P(7, 8.4) = 420 + 403.2 - 147 - 141.12 - 117.6 = 417.48$, below $417.6$. This is the two-variable version of "marginal revenue equals marginal cost" for each product.

</details>

## Where this shows up

- The next lesson, [double integrals](04-double-integrals.md), integrates functions of two variables. In the rest of this book, utility maximization and cost minimization are worked out in Lagrange multipliers, utility and cost minimization<!-- link: ../../07-economics-math/03-firms-and-consumers/05-lagrange-multipliers-utility-and-cost-minimization.md --> and production and cost functions<!-- link: ../../07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md -->, using the method of this lesson.
- In CS, constrained optimization is the core of support vector machines, resource allocation and the dual form of linear programs, and the Hessian's eigenvalues decide whether a point found by training is a minimum or a saddle. Least squares is the unconstrained case of Example 6, and [regression and econometrics intuition](../../07-economics-math/04-more-tools/03-regression-and-econometrics-intuition.md) applies it to data.
- In economics, the multiplier $\lambda$ is a shadow price: the value of relaxing a constraint by one unit. The same idea prices a unit of income (marginal utility of income) and a unit of output (marginal cost).
