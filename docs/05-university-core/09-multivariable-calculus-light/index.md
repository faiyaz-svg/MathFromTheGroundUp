# Multivariable calculus (light)

The working tools of calculus for functions of two or more variables: partial derivatives and the gradient, optimization with and without constraints, and double integrals. Lessons 1 and 4 are optional.

1. [Parametric, polar and 3D coordinates](01-parametric-polar-and-3d-coordinates.md) (optional)
2. [Partial derivatives and the gradient](02-partial-derivatives-and-the-gradient.md)
3. [Multivariable optimization and Lagrange multipliers](03-multivariable-optimization-and-lagrange-multipliers.md)
4. [Double integrals](04-double-integrals.md) (optional)

## Cheat sheet

### Parametric, polar and 3D coordinates

| Idea | Rule |
|---|---|
| parametric curve | $(x(t), y(t))$; velocity $(x', y')$, speed $\sqrt{x'^2 + y'^2}$ |
| slope of a parametric curve | $\dfrac{dy}{dx} = \dfrac{y'(t)}{x'(t)}$ when $x'(t) \ne 0$ |
| length of a path | $\int_a^b \sqrt{x'^2 + y'^2}\,dt$ |
| polar to Cartesian | $x = r\cos\theta$, $y = r\sin\theta$ |
| Cartesian to polar | $r = \sqrt{x^2 + y^2}$; pick $\theta$ in the right quadrant (`atan2(y, x)`) |
| area in polar form | $A = \frac{1}{2}\int_\alpha^\beta r^2\,d\theta$ |
| distance in $\mathbb{R}^3$ | $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$ |
| sphere | $(x - a)^2 + (y - b)^2 + (z - c)^2 = R^2$ |
| plane | $ax + by + cz = d$, normal vector $(a, b, c)$ |
| distance from a point to a plane | $\dfrac{\lvert aq_1 + bq_2 + cq_3 - d \rvert}{\sqrt{a^2 + b^2 + c^2}}$ |
| level curve | $f(x, y) = c$; a contour map shows several |

The circle $r = 2a\cos\theta$ has centre $(a, 0)$ and radius $a$. The cardioid $r = 1 + \cos\theta$ has area $\frac{3\pi}{2}$.

The main mistakes: taking $\theta = \arctan\frac{y}{x}$ without checking the quadrant, mixing up $\frac{dy}{dt}$ and $\frac{dy}{dx}$, leaving out the $\frac{1}{2}$ in the polar area, and using a $\theta$ range that traces the curve twice.

### Partial derivatives and the gradient

| Idea | Rule |
|---|---|
| partial derivative | $f_x$: differentiate in $x$ with $y$ held constant |
| gradient | $\nabla f = (f_x, f_y)$, a vector in the input plane |
| tangent plane at $(a, b)$ | $z = f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b)$ |
| linear approximation | $\Delta f \approx f_x\,\Delta x + f_y\,\Delta y$ |
| chain rule along a path | $\dfrac{d}{dt}f(\mathbf{r}(t)) = \nabla f \cdot \mathbf{r}'(t)$ |
| directional derivative | $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$ for a unit vector $\mathbf{u}$ |
| steepest ascent | direction $\frac{\nabla f}{\lVert \nabla f \rVert}$, rate $\lVert \nabla f \rVert$ |
| level curves | $\nabla f$ is perpendicular to them; slope of a level curve is $-\dfrac{f_x}{f_y}$ |
| gradient descent | $\mathbf{w} \leftarrow \mathbf{w} - \eta\,\nabla f(\mathbf{w})$ |

Clairaut: $f_{xy} = f_{yx}$ when the second partials are continuous. A limit in two variables must agree along every route to the point: for $\frac{xy}{x^2 + y^2}$ the limit along $y = mx$ is $\frac{m}{1 + m^2}$, so there is no limit at the origin, although both partials exist there.

For $Q = AK^{\alpha}L^{\beta}$: $Q_K = \alpha\frac{Q}{K}$ and $Q_L = \beta\frac{Q}{L}$, returns to scale are $\alpha + \beta$, and the isoquant has slope $-\frac{Q_K}{Q_L}$. Gradient descent on $x^2 + 5y^2$ needs $\eta < 0.2$ ($2$ over the largest curvature), and the best rate is $\frac{1}{6}$.

The main mistakes: a non-unit direction vector, a wrong sign on the slope of a level curve, subtracting instead of adding in ascent versus descent, and believing that existing partial derivatives mean continuity.

### Multivariable optimization and Lagrange multipliers

| Idea | Rule |
|---|---|
| critical point | $\nabla f = \mathbf{0}$ |
| Hessian | $H = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{xy} & f_{yy} \end{pmatrix}$, $D = f_{xx}f_{yy} - f_{xy}^2$ |
| second derivative test | $D > 0$, $f_{xx} > 0$: minimum; $D > 0$, $f_{xx} < 0$: maximum; $D < 0$: saddle; $D = 0$: no information |
| in terms of eigenvalues | both positive: minimum; both negative: maximum; opposite signs: saddle |
| absolute extrema on a closed bounded region | compare $f$ at interior critical points and the extreme values on the boundary |
| Lagrange | at an extremum of $f$ on $g = c$ with $\nabla g \ne \mathbf{0}$: $\nabla f = \lambda\nabla g$ |
| utility maximization | $\dfrac{U_x}{p_x} = \dfrac{U_y}{p_y} = \lambda$ and $p_xx + p_yy = m$ |
| cost minimization | $\dfrac{p_K}{Q_K} = \dfrac{p_L}{Q_L} = \lambda$ and $Q(K, L) = \bar{Q}$ |
| meaning of $\lambda$ | marginal utility of income, or marginal cost of output |

Cobb-Douglas utility $x^ay^{1 - a}$ spends the share $a$ of income $m$ on $x$: $p_xx = am$. Example: $U = x^{0.4}y^{0.6}$, prices \$2 and \$3, income \$120 gives $(24, 24)$, $U = 24$, $\lambda = 0.2$. Example: $Q = K^{0.3}L^{0.7} = 100$ at prices \$3 and \$7 gives $K = L = 100$, cost \$1,000, marginal cost \$10. The least-squares line is the critical point of the sum of squared errors, and its Hessian $2A^TA$ is positive definite.

The main mistakes: reading $D = 0$ as a saddle, forgetting the boundary and the points where $\nabla g = \mathbf{0}$ (the cusp $y^2 = x^3$), dividing by a variable that may be zero, and stopping at the Lagrange equations without comparing the values of $f$.

### Double integrals

| Idea | Rule |
|---|---|
| double integral | $\iint_R f\,dA$, the volume under $z = f(x, y)$ over $R$; $\iint_R 1\,dA$ is the area |
| Fubini (rectangle) | $\int_a^b\int_c^d f\,dy\,dx = \int_c^d\int_a^b f\,dx\,dy$ |
| type I region | $a \le x \le b$, $g_1(x) \le y \le g_2(x)$; inner $dy$ |
| type II region | $c \le y \le d$, $h_1(y) \le x \le h_2(y)$; inner $dx$ |
| polar coordinates | $\iint f\,dA = \iint f(r\cos\theta, r\sin\theta)\,r\,dr\,d\theta$ |
| change of variables | $dA = \lvert \det J \rvert\,du\,dv$; for polar, $\det J = r$ |
| average value | $\dfrac{1}{\text{area}(R)}\iint_R f\,dA$ |

Set-up steps: sketch the region, choose the order, write the inner limits from one strip, integrate the inner integral and then the outer, and check with $f = 1$ or with the other order. If the inner integral has no antiderivative, as for $e^{y^2}$ in $dy$, change the order: $\int_0^1\int_x^1 e^{y^2}\,dy\,dx = \int_0^1\int_0^y e^{y^2}\,dx\,dy = \frac{e - 1}{2}$.

The Gaussian integral: squaring $I = \int_{-\infty}^{\infty}e^{-x^2}\,dx$ gives $\int_0^{2\pi}\int_0^\infty e^{-r^2}r\,dr\,d\theta = \pi$, so $I = \sqrt{\pi}$, and $\int e^{-z^2/2}\,dz = \sqrt{2\pi}$. The distance of a standard normal point from the origin has $P(R \le \rho) = 1 - e^{-\rho^2/2}$.

For a joint density: probabilities are $\iint_R f\,dA$, the density of $X$ is $\int f\,dy$, and $E[g(X, Y)] = \iint g\,f\,dA$. Example: $f = 8xy$ on $0 \le y \le x \le 1$ has $P(X + Y \le 1) = \frac{1}{6}$ and $E[X] = \frac{4}{5}$. Volumes: the paraboloid cap $4 - x^2 - y^2$ over $r \le 2$ has volume $8\pi$, and a sphere has $\frac{4}{3}\pi R^3$.

The main mistakes: forgetting the factor $r$ in polar coordinates, swapping the order without drawing the region, and putting the inner variable in the outer limits.
