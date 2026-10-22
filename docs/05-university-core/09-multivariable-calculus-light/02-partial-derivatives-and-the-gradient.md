# Partial derivatives and the gradient

After this lesson you can compute partial derivatives, write the tangent plane and use it to approximate a function, apply the chain rule along a path, compute a gradient and a directional derivative, explain why the gradient points uphill and is perpendicular to level curves, find the marginal products of a Cobb-Douglas production function, and run gradient descent on a function of several variables.

Before this: [linear approximation](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md), [the chain rule](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md), [optimization](../03-applications-of-derivatives/05-optimization.md) and [vectors, dot product and span](../06-linear-algebra/01-vectors-dot-product-and-span.md). Contour maps are in [parametric, polar and 3D coordinates](01-parametric-polar-and-3d-coordinates.md), the optional lesson before this one.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For $f(x, y) = x^2y + 3y$, find $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ at the point $(1, 2)$.
2. For $f(x, y) = x^2 + y^2$ at $(3, 4)$, find the vector $(f_x, f_y)$, the direction in which $f$ increases fastest and how fast it increases that way.
3. For $f(x, y) = xy$ at $(2, 1)$, find the rate of change of $f$ in the direction $\frac{1}{5}(3, 4)$.

<details class="solution" markdown>
<summary>Answers</summary>

1. Treat $y$ as a constant for $\frac{\partial f}{\partial x} = 2xy$, which is $4$ at $(1, 2)$. Treat $x$ as a constant for $\frac{\partial f}{\partial y} = x^2 + 3$, which is $4$.
2. The vector is $(2x, 2y) = (6, 8)$. The function increases fastest in the direction $\frac{1}{10}(6, 8) = (0.6, 0.8)$, at the rate $\lVert (6, 8) \rVert = 10$.
3. The vector $(f_x, f_y) = (y, x) = (1, 2)$ at $(2, 1)$. The rate in the unit direction $\frac{1}{5}(3, 4)$ is the dot product $\frac{3 + 8}{5} = 2.2$.

</details>

## The idea

Most quantities depend on several things at once. The output of a factory depends on its capital and its labour. The height of a hill depends on where you stand, east-west and north-south. The error of a model depends on all its parameters. In each case the one-variable question "how fast does this change?" splits into many questions: how fast as you move east, as you move north, as you move in any direction at all.

The first step is to change one input at a time. Fix the position north-south, walk east, and measure the slope: that is a partial derivative. Do it for each input and you have a list of slopes, one per input. The list turns out to be a vector, the gradient, and it answers the question about every direction at once. A hiker who wants to climb as steeply as possible walks along the gradient, and a hiker who wants to stay at the same height walks at a right angle to it. Both facts are proved in this lesson, and the first one is a direct use of the Cauchy-Schwarz inequality from the linear algebra chapter.

![The hill f(x, y) = 4 minus x squared minus 2 y squared drawn as grey contour ellipses with green gradient arrows. Every arrow points inward toward the peak at the origin, is longer where the contours are closer together, and crosses the contour at a right angle. At the point (1, 1) a red arrow marks the gradient (minus 2, minus 4), and a dashed blue line marks the contour direction (2, minus 1), at a right angle to it.](../../assets/figures/05-university-core/partial-derivatives-and-the-gradient-gradient.svg)

For economics, the partial derivatives of a production function are the marginal products, and the gradient says how output responds when inputs change. For machine learning, the negative gradient of the loss is the direction in which to adjust the parameters, and repeating that step is gradient descent, the several-variable version of the lesson on [optimization](../03-applications-of-derivatives/05-optimization.md#gradient-descent-in-one-variable).

## Definitions

A **function of two variables** assigns a number $f(x, y)$ to each point $(x, y)$ of a region of the plane. More generally, a function of $n$ variables takes a point of $\mathbb{R}^n$ to a number, and everything below carries over with more coordinates.

The **limit** $\lim_{(x, y) \to (a, b)} f(x, y) = L$ means that $f(x, y)$ gets as close as we like to $L$ when $(x, y)$ is close enough to $(a, b)$ and not equal to it. In the language of [epsilon and delta](../01-limits-and-continuity/02-epsilon-delta-definition.md): for every $\varepsilon > 0$ there is a $\delta > 0$ such that $\lvert f(x, y) - L \rvert < \varepsilon$ whenever $0 < \sqrt{(x - a)^2 + (y - b)^2} < \delta$. In plain words, the same limit has to come out along every route to the point. The function $f$ is **continuous** at $(a, b)$ if the limit exists and equals $f(a, b)$.

The **partial derivative** of $f$ with respect to $x$ at $(a, b)$ is

$$
\frac{\partial f}{\partial x}(a, b) = f_x(a, b) = \lim_{h \to 0}\frac{f(a + h, b) - f(a, b)}{h},
$$

and the partial derivative with respect to $y$ is $f_y(a, b) = \lim_{k \to 0}\frac{f(a, b + k) - f(a, b)}{k}$. In plain words, hold the other variable fixed and differentiate as in one variable. Geometrically $f_x(a, b)$ is the slope of the surface in the $x$-direction at the point above $(a, b)$, the slope of the slice through the surface by the plane $y = b$. The symbol $\partial$ is a rounded $d$, used to say that other variables are being held fixed.

The **gradient** of $f$ is the vector of its partial derivatives,

$$
\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right),
$$

read "del $f$" or "grad $f$". For $n$ variables, $\nabla f = (f_{x_1}, \dots, f_{x_n})$. In plain words, it is the list of all the slopes along the coordinate axes, packed into one vector that lives in the input space, the plane of $(x, y)$, and not on the surface.

For a unit vector $\mathbf{u}$ (a vector of length 1), the **directional derivative** of $f$ at $\mathbf{a}$ in the direction $\mathbf{u}$ is

$$
D_{\mathbf{u}}f(\mathbf{a}) = \lim_{h \to 0}\frac{f(\mathbf{a} + h\mathbf{u}) - f(\mathbf{a})}{h}.
$$

In plain words, it is the rate of change of $f$ per unit distance when you walk from $\mathbf{a}$ in the direction $\mathbf{u}$. Taking $\mathbf{u} = (1, 0)$ gives $f_x$, and $\mathbf{u} = (0, 1)$ gives $f_y$.

In economics, a **production function** $Q = f(K, L)$ gives the output $Q$ from capital $K$ and labour $L$. The **marginal product** of capital is $\frac{\partial Q}{\partial K}$ and of labour is $\frac{\partial Q}{\partial L}$: the extra output from one more unit of that input with the other input held fixed. The **Cobb-Douglas** function is $Q = AK^{\alpha}L^{\beta}$ with constants $A > 0$, $\alpha > 0$ and $\beta > 0$. The one-variable version of marginal analysis is in [rates of change and marginal analysis](../03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md).

## How to do it

### Computing partial derivatives

1. To find $f_x$, treat $y$ as a constant and differentiate with respect to $x$ using the usual rules (power, product, chain). To find $f_y$, treat $x$ as a constant.
2. Substitute the point, if one is given.
3. Check one of them against a one-variable derivative: for $f_x(a, b)$, differentiate the single-variable function $g(x) = f(x, b)$ at $x = a$.

For $f_{xy}$ and $f_{yx}$ the order matters in the notation but, for every function in this book, not in the result. This is *Clairaut's theorem*, stated without proof: if $f_{xy}$ and $f_{yx}$ are continuous near a point, they are equal there. It is a useful check on a hand computation.

### A limit that fails, and one that works

Limits in two variables are harder than in one because there are infinitely many routes to the point. Consider $f(x, y) = \frac{xy}{x^2 + y^2}$ for $(x, y) \ne (0, 0)$, with $f(0, 0) = 0$. Along the line $y = mx$, for $x \ne 0$,

$$
f(x, mx) = \frac{mx^2}{x^2 + m^2x^2} = \frac{m}{1 + m^2}.
$$

This doesn't depend on $x$, so the limit along each line is its own number: $0$ for $m = 0$, $\frac{1}{2}$ for $m = 1$, $-\frac{1}{2}$ for $m = -1$. Two routes with different limits mean that the limit doesn't exist, so $f$ is not continuous at the origin even though $f(0, 0)$ is defined.

![Left, five lines through the origin: the x-axis, the y-axis, y = x and y = minus x, labelled with the value that f takes along each, 0, 0, one half and minus one half. Right, the curve m over 1 plus m squared against the slope m, which rises from minus one half at m = minus 1, through 0 at m = 0, to one half at m = 1, and fades to 0 for large positive and negative m.](../../assets/figures/05-university-core/partial-derivatives-and-the-gradient-limit.svg)

Notice the odd feature: both partial derivatives exist at the origin, because $f(x, 0) = 0$ and $f(0, y) = 0$ give $f_x(0, 0) = f_y(0, 0) = 0$. The partials only look along the two axes. So the existence of partial derivatives is weaker than continuity, a point that has no one-variable counterpart.

To prove that a limit does exist you can't check every route, since there are too many. You bound the function instead. For $g(x, y) = \frac{x^2y}{x^2 + y^2}$, we have $\frac{x^2}{x^2 + y^2} \le 1$, so $\lvert g(x, y) \rvert \le \lvert y \rvert$, which tends to $0$. By the squeeze theorem $\lim_{(x, y) \to (0, 0)} g(x, y) = 0$.

Sums, products, quotients (with nonzero denominator) and compositions of continuous functions are continuous, so every function built from polynomials, exponentials, logarithms and trig functions is continuous wherever it is defined. That covers the functions in the rest of the book, and trouble only arises where a denominator is $0$.

### The tangent plane and linear approximation

For a function of one variable, the tangent line at $a$ is $y = f(a) + f'(a)(x - a)$. For two variables, the **tangent plane** to the surface $z = f(x, y)$ at $(a, b)$ is

$$
z = f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b).
$$

It is the plane through the point $(a, b, f(a, b))$ that has the right slope in the $x$-direction and the right slope in the $y$-direction. The theorem that makes it useful is stated without proof: if $f_x$ and $f_y$ are continuous near $(a, b)$, then the plane is a good approximation, in the sense that

$$
f(a + h, b + k) = f(a, b) + f_x(a, b)\,h + f_y(a, b)\,k + \text{error},
$$

where the error is small compared with $\sqrt{h^2 + k^2}$. So for small steps $\Delta f \approx f_x\,\Delta x + f_y\,\Delta y$: each partial derivative tells how much each input contributes, and the contributions add. In vector form, $f(\mathbf{a} + \mathbf{h}) \approx f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot \mathbf{h}$.

### The chain rule along a path

Suppose a point moves along a path $\mathbf{r}(t) = (x(t), y(t))$ and $f$ has continuous partial derivatives. Then the value $f(x(t), y(t))$ is a function of $t$ alone, and

$$
\frac{d}{dt}f(x(t), y(t)) = f_x\,x'(t) + f_y\,y'(t) = \nabla f \cdot \mathbf{r}'(t).
$$

The reason is the linear approximation. In a short time $\Delta t$ the point moves by $\Delta x \approx x'\,\Delta t$ and $\Delta y \approx y'\,\Delta t$, so $\Delta f \approx f_x\,\Delta x + f_y\,\Delta y \approx (f_x x' + f_y y')\,\Delta t$, and dividing by $\Delta t$ gives the formula. In plain words, the rate at which the altitude changes along a walk is the gradient dotted with the velocity.

### The gradient and the directions

*Theorem 1.* If $f$ has continuous partial derivatives near $\mathbf{a}$ and $\mathbf{u}$ is a unit vector, then $D_{\mathbf{u}}f(\mathbf{a}) = \nabla f(\mathbf{a}) \cdot \mathbf{u}$.

What we know: the chain rule along a path. What we want: the directional derivative as a dot product. The plan: the walk $\mathbf{r}(h) = \mathbf{a} + h\mathbf{u}$ has velocity $\mathbf{u}$, and the directional derivative is the derivative of $f$ along that walk at $h = 0$.

*Proof.* By definition $D_{\mathbf{u}}f(\mathbf{a}) = \frac{d}{dh}f(\mathbf{a} + h\mathbf{u})\big|_{h = 0}$. The path $\mathbf{r}(h) = \mathbf{a} + h\mathbf{u}$ has $\mathbf{r}'(h) = \mathbf{u}$, so the chain rule gives $\nabla f(\mathbf{r}(0)) \cdot \mathbf{u} = \nabla f(\mathbf{a}) \cdot \mathbf{u}$. $\blacksquare$

Look back: the directional derivative in every direction is known from the two numbers $f_x$ and $f_y$. If you forget to make $\mathbf{u}$ a unit vector, the answer is too big by the factor $\lVert \mathbf{u} \rVert$.

*Theorem 2 (steepest ascent).* Suppose $\nabla f(\mathbf{a}) \ne \mathbf{0}$. Among all unit vectors $\mathbf{u}$, the directional derivative $D_{\mathbf{u}}f(\mathbf{a})$ is largest for $\mathbf{u} = \frac{\nabla f(\mathbf{a})}{\lVert \nabla f(\mathbf{a}) \rVert}$, and the largest value is $\lVert \nabla f(\mathbf{a}) \rVert$. It is smallest, $-\lVert \nabla f(\mathbf{a}) \rVert$, for the opposite direction, and it is $0$ for the directions perpendicular to $\nabla f(\mathbf{a})$.

What we know: Theorem 1, and the Cauchy-Schwarz inequality $\lvert \mathbf{v} \cdot \mathbf{u} \rvert \le \lVert \mathbf{v} \rVert\,\lVert \mathbf{u} \rVert$ with equality exactly when one vector is a multiple of the other, from [vectors, dot product and span](../06-linear-algebra/01-vectors-dot-product-and-span.md#measuring-the-cauchy-schwarz-inequality). What we want: the maximum of a dot product over unit vectors. The plan: bound the dot product with Cauchy-Schwarz and find where the bound is reached.

*Proof.* Write $\mathbf{g} = \nabla f(\mathbf{a})$. For a unit vector $\mathbf{u}$, Theorem 1 and Cauchy-Schwarz give $D_{\mathbf{u}}f = \mathbf{g} \cdot \mathbf{u} \le \lVert \mathbf{g} \rVert\,\lVert \mathbf{u} \rVert = \lVert \mathbf{g} \rVert$. The bound is reached by $\mathbf{u} = \frac{\mathbf{g}}{\lVert \mathbf{g} \rVert}$, which is a unit vector, because $\mathbf{g} \cdot \frac{\mathbf{g}}{\lVert \mathbf{g} \rVert} = \lVert \mathbf{g} \rVert$. By the equality case of Cauchy-Schwarz no other unit vector reaches it: equality needs $\mathbf{u}$ to be a multiple of $\mathbf{g}$, and a unit multiple with a positive dot product is only $\frac{\mathbf{g}}{\lVert \mathbf{g} \rVert}$. The same argument applied to $-\mathbf{g}$ gives the smallest value $-\lVert \mathbf{g} \rVert$. If $\mathbf{u} \perp \mathbf{g}$ the dot product is $0$ by definition. $\blacksquare$

Look back: the angle form says the same thing. With $\theta$ the angle between $\mathbf{g}$ and $\mathbf{u}$, $D_{\mathbf{u}}f = \lVert \mathbf{g} \rVert\cos\theta$, which is largest at $\theta = 0$. The proof by Cauchy-Schwarz works in any number of variables, where there is no picture of an angle, and that is why the book proved the inequality for $\mathbb{R}^n$ first.

*Theorem 3 (the gradient is perpendicular to level curves).* Let $f$ have continuous partial derivatives and let $\mathbf{r}(t)$ be a smooth path in the level curve $f(x, y) = c$. Then $\nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t) = 0$, so the gradient is perpendicular to the tangent of the level curve.

What we know: along the path $f$ always equals $c$. What we want: a dot product equal to $0$. The plan: differentiate the constant with the chain rule.

*Proof.* Since $f(\mathbf{r}(t)) = c$ for every $t$, the derivative with respect to $t$ is $0$. By the chain rule along a path, that derivative is $\nabla f \cdot \mathbf{r}'(t)$. $\blacksquare$

Look back: the result agrees with Theorem 2. Moving along a level curve doesn't change $f$, so the rate is $0$, and the direction of the largest rate has to be at a right angle to the level curve. It also gives the slope of a level curve. The tangent direction is perpendicular to $(f_x, f_y)$, so it is $(f_y, -f_x)$ and the slope is

$$
\frac{dy}{dx} = -\frac{f_x}{f_y} \qquad (f_y \ne 0),
$$

which is what implicit differentiation of $f(x, y) = c$ gives: $f_x + f_y\frac{dy}{dx} = 0$.

### Marginal products and the Cobb-Douglas function

For $Q = AK^{\alpha}L^{\beta}$ the partial derivatives are $\frac{\partial Q}{\partial K} = \alpha AK^{\alpha - 1}L^{\beta} = \alpha\frac{Q}{K}$ and $\frac{\partial Q}{\partial L} = \beta\frac{Q}{L}$. Three facts follow.

First, if $0 < \alpha < 1$ then $\frac{\partial^2 Q}{\partial K^2} = \alpha(\alpha - 1)AK^{\alpha - 2}L^{\beta} < 0$, so the marginal product of capital falls as capital grows with labour fixed. This is *diminishing marginal returns*. Second, scaling both inputs by $s > 0$ gives $A(sK)^{\alpha}(sL)^{\beta} = s^{\alpha + \beta}Q$, so if $\alpha + \beta = 1$ doubling both inputs doubles output (constant returns to scale), and if $\alpha + \beta > 1$ it more than doubles it. Third, the quantity $\frac{K}{Q}\frac{\partial Q}{\partial K} = \alpha$ is the percent change in output per 1% change in capital for small changes, so the exponent is the output elasticity of capital.

The isoquant of $Q$ is a level curve, and by Theorem 3 its slope is $\frac{dL}{dK} = -\frac{Q_K}{Q_L}$, the amount of labour that can replace one unit of capital at the same output. Economists call the size of this slope the *marginal rate of technical substitution*.

### Gradient descent in several variables

To minimize a function $f$ of several variables, start at a point $\mathbf{w}_0$ and repeat

$$
\mathbf{w}_{n+1} = \mathbf{w}_n - \eta\,\nabla f(\mathbf{w}_n),
$$

with a learning rate $\eta > 0$. This is the update of the [one-variable lesson](../03-applications-of-derivatives/05-optimization.md#gradient-descent-in-one-variable), with the gradient for the slope. By Theorem 2, $-\nabla f$ is the direction in which $f$ decreases fastest, so each step is the best direction for a small step. For a bowl $f(x, y) = x^2 + 5y^2$ the gradient is $(2x, 10y)$ and the update is $x \leftarrow (1 - 2\eta)x$, $y \leftarrow (1 - 10\eta)y$. Each coordinate is a one-variable problem with its own factor, and the step must make both factors have absolute value below 1, so $\eta < \frac{2}{10} = 0.2$. The steep direction ($y$, with curvature 10) sets the limit, and the shallow direction ($x$, curvature 2) sets the speed. The best choice has $1 - 2\eta = -(1 - 10\eta)$, which is $\eta = \frac{1}{6}$, with both factors of size $\frac{2}{3}$.

![Contours of f(x, y) = x squared plus 5 y squared, long ellipses along the x-axis, with two descent paths starting from (4, 1.5). The red path, with learning rate 0.18, zigzags across the valley from side to side while closing in on the minimum at the origin. The green path, with learning rate 0.05, slides smoothly toward the x-axis and then creeps along it toward the minimum, and after 25 steps it is still at about x = 0.3.](../../assets/figures/05-university-core/partial-derivatives-and-the-gradient-descent.svg)

The numbers 2 and 10 are the eigenvalues of the matrix of second derivatives, $\begin{pmatrix} 2 & 0 \\ 0 & 10 \end{pmatrix}$. In general the rule of thumb of the one-variable lesson becomes: the learning rate must stay below $\frac{2}{L}$, where $L$ is the largest eigenvalue of that matrix, the Hessian of the next lesson. A bowl that is much steeper in one direction than in another, like this one (with ratio 5 here, and ratios of thousands in real problems), forces a small step and makes the progress along the shallow direction slow.

## Worked examples

<div class="example" markdown>

### Example 1: partial derivatives and a check

Find $f_x$, $f_y$ and the mixed partials of $f(x, y) = x^2e^y + y\ln x$ for $x > 0$, and evaluate the first partials at $(1, 0)$.

Step 1: holding $y$ fixed, $x^2e^y$ has derivative $2xe^y$ and $y\ln x$ has derivative $\frac{y}{x}$, so $f_x = 2xe^y + \frac{y}{x}$. Holding $x$ fixed, $x^2e^y$ has derivative $x^2e^y$ and $y\ln x$ has derivative $\ln x$, so $f_y = x^2e^y + \ln x$.

Step 2: at $(1, 0)$, $f_x = 2 \cdot 1 \cdot 1 + 0 = 2$ and $f_y = 1 \cdot 1 + 0 = 1$.

Step 3: the check with a one-variable function. At $y = 0$ we have $g(x) = f(x, 0) = x^2$, and $g'(1) = 2$, which is $f_x(1, 0)$. At $x = 1$ we have $h(y) = f(1, y) = e^y$, and $h'(0) = 1$, which is $f_y(1, 0)$.

The mixed partials are $f_{xy} = \frac{\partial}{\partial y}\left(2xe^y + \frac{y}{x}\right) = 2xe^y + \frac{1}{x}$ and $f_{yx} = \frac{\partial}{\partial x}\left(x^2e^y + \ln x\right) = 2xe^y + \frac{1}{x}$. They agree, as Clairaut's theorem says they should.

</div>

<div class="example" markdown>

### Example 2: tangent plane, estimate and a chain rule

Let $f(x, y) = \sqrt{x^2 + y^2}$, the distance from the origin. Estimate $f(3.02, 3.97)$ with the tangent plane at $(3, 4)$. Then find the rate of change of $f$ along the path $\mathbf{r}(t) = (3 + t, 4 - 2t)$ at $t = 0$.

At $(3, 4)$ we have $f = 5$, $f_x = \frac{x}{\sqrt{x^2 + y^2}} = \frac{3}{5}$ and $f_y = \frac{4}{5}$. The tangent plane is $z = 5 + 0.6(x - 3) + 0.8(y - 4)$. At $(3.02, 3.97)$ the steps are $h = 0.02$ and $k = -0.03$, so $f \approx 5 + 0.6(0.02) + 0.8(-0.03) = 5 + 0.012 - 0.024 = 4.988$.

Check: the exact value is $\sqrt{9.1204 + 15.7609} = \sqrt{24.8813} \approx 4.98811$, so the estimate is off by about $0.0001$.

For the path, $\mathbf{r}'(t) = (1, -2)$, so $\frac{d}{dt}f(\mathbf{r}(t)) = \nabla f \cdot \mathbf{r}' = 0.6 \cdot 1 + 0.8 \cdot (-2) = -1$. In words, a walker leaving $(3, 4)$ with velocity $(1, -2)$ gets closer to the origin at rate $1$. Direct check: $f(\mathbf{r}(t))^2 = (3 + t)^2 + (4 - 2t)^2 = 25 - 10t + 5t^2$, so $2f\,f' = -10 + 10t$ and at $t = 0$, $f' = \frac{-10}{2 \cdot 5} = -1$.

</div>

<div class="example" markdown>

### Example 3: the steepest way up a hill

The height of a hill is $f(x, y) = 4 - x^2 - 2y^2$, the surface of the contour figure. A hiker stands at $(1, 1)$. Find the steepest direction up and its slope, the direction to walk to stay level, and the slope toward the point $(3, 2)$.

Step 1: $\nabla f = (-2x, -4y) = (-2, -4)$ at $(1, 1)$, with length $\sqrt{4 + 16} = \sqrt{20} \approx 4.472$.

Step 2: by Theorem 2 the steepest ascent is along $\frac{(-2, -4)}{\sqrt{20}} = \frac{(-1, -2)}{\sqrt{5}}$, at the slope $\sqrt{20} \approx 4.47$ metres of height per metre walked. This is toward the peak, as it should be.

Step 3: the level directions are the unit vectors perpendicular to $(-2, -4)$, which are $\pm\frac{(2, -1)}{\sqrt{5}}$: the dot product $-4 + 4 = 0$. The slope there is $0$. This is the dashed blue line in the figure.

Step 4: the direction toward $(3, 2)$ is $(2, 1)$, with length $\sqrt{5}$, so $\mathbf{u} = \frac{(2, 1)}{\sqrt{5}}$ and $D_{\mathbf{u}}f = \frac{-4 - 4}{\sqrt{5}} = -\frac{8}{\sqrt{5}} \approx -3.578$. The hiker goes downhill, which makes sense: the height at $(3, 2)$ is $4 - 9 - 8 = -13$, far below the height $1$ at $(1, 1)$.

Check: a small step of $10^{-6}$ in that direction changes $f$ by about $-3.5777 \times 10^{-6}$ (the "In code" section runs it). The number $-3.578$ is between $-\sqrt{20} = -4.472$ and $\sqrt{20}$, as any directional derivative must be.

</div>

<div class="example" markdown>

### Example 4: marginal products

A hypothetical firm has the production function $Q = 10K^{0.3}L^{0.7}$ with $K$ units of capital and $L$ hours of labour. Find the marginal products at $K = L = 100$, the effect of doubling both inputs, and the slope of the isoquant.

At $K = L = 100$ the output is $Q = 10 \cdot 100^{0.3} \cdot 100^{0.7} = 10 \cdot 100 = 1000$. The marginal products are $Q_K = 0.3\frac{Q}{K} = 0.3 \cdot 10 = 3$ and $Q_L = 0.7\frac{Q}{L} = 7$. One more unit of capital adds about 3 units of output, and one more hour of labour adds about 7.

Check against a real change: $Q(101, 100) = 1002.99$, so the actual gain from one more unit of capital is $2.99$. The marginal product $3$ is the rate at the point, and the actual gain is slightly smaller because returns diminish.

Doubling both inputs gives $Q(200, 200) = 10 \cdot 200 = 2000$, double, because $0.3 + 0.7 = 1$ (constant returns to scale). The isoquant through $(100, 100)$ has slope $-\frac{Q_K}{Q_L} = -\frac{3}{7} \approx -0.43$: to give up one unit of capital and keep output at 1000, the firm needs about $\frac{3}{7}$ of an hour more labour.

</div>

<div class="example" markdown>

### Example 5: gradient descent on a stretched bowl

Run gradient descent on $f(x, y) = x^2 + 5y^2$ from $(4, 1.5)$ with $\eta = 0.18$, and then say which learning rates converge.

The gradient is $(2x, 10y)$ and the update is $x \leftarrow (1 - 0.36)x = 0.64x$ and $y \leftarrow (1 - 1.8)y = -0.8y$. The steps are

| Step | $x$ | $y$ | $f(x, y)$ |
|---|---|---|---|
| 0 | 4 | 1.5 | 27.25 |
| 1 | 2.56 | $-1.2$ | 13.7536 |
| 2 | 1.6384 | 0.96 | 7.2924 |
| 3 | 1.0486 | $-0.768$ | 4.0486 |

The $x$ coordinate shrinks smoothly by the factor $0.64$ and the $y$ coordinate flips sign each time while shrinking by $0.8$: that is the zigzag in the figure. The value of $f$ goes down at every step.

In general $x$ needs $\lvert 1 - 2\eta \rvert < 1$ and $y$ needs $\lvert 1 - 10\eta \rvert < 1$, so the method converges exactly when $0 < \eta < 0.2$. At $\eta = 0.2$ the $y$ factor is $-1$, and $y$ bounces between $1.5$ and $-1.5$ forever. At $\eta = 0.21$ the factor is $-1.1$ and $y$ grows (after 30 steps $y \approx 26.17$). The best rate is $\eta = \frac{1}{6}$, which makes both factors $\pm\frac{2}{3}$.

Check: after step 1, $f = 2.56^2 + 5(1.2)^2 = 6.5536 + 7.2 = 13.7536$, in the table. The table starts at $f = 16 + 11.25 = 27.25$.

</div>

<div class="example" markdown>

### Example 6: one step of gradient descent for a line fit (finish it yourself)

A line $y = w_0 + w_1x$ is fitted to the points $(1, 2)$, $(2, 3)$ and $(3, 5)$ by minimizing the mean squared error

$$
E(w_0, w_1) = \frac{1}{3}\sum_{i=1}^{3}\left(w_0 + w_1x_i - y_i\right)^2.
$$

The partial derivatives are $\frac{\partial E}{\partial w_0} = \frac{2}{3}\sum(w_0 + w_1x_i - y_i)$ and $\frac{\partial E}{\partial w_1} = \frac{2}{3}\sum x_i(w_0 + w_1x_i - y_i)$. Find the gradient at $(w_0, w_1) = (0, 0)$, and take one step with $\eta = 0.05$.

<details class="solution" markdown>
<summary>Finish</summary>

At $(0, 0)$ each residual is $-y_i$, so $\frac{\partial E}{\partial w_0} = \frac{2}{3}(-2 - 3 - 5) = -\frac{20}{3} \approx -6.667$ and $\frac{\partial E}{\partial w_1} = \frac{2}{3}(-2 - 6 - 15) = -\frac{46}{3} \approx -15.333$. The step is $(0, 0) - 0.05\,(-6.667, -15.333) = (0.3333, 0.7667)$.

Check: the error goes from $E(0, 0) = \frac{4 + 9 + 25}{3} = 12.667$ to $E(0.3333, 0.7667) = \frac{(1.1 - 2)^2 + (1.8667 - 3)^2 + (2.6333 - 5)^2}{3} = \frac{0.81 + 1.2844 + 5.6011}{3} = 2.565$, a big drop. Run to the end, the weights reach $(0.3333, 1.5)$, the least-squares line of [orthogonality, projections and least squares](../06-linear-algebra/07-orthogonality-projections-and-least-squares.md).

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: forgetting that "constant" means constant. In $f_x$ for $f = x^2y$ the factor $y$ stays as it is and the derivative is $2xy$, not $2x$ and not $2xy + x^2$. The second term would be $x^2\frac{dy}{dx}$, which is $0$ only because $y$ is held fixed. If a variable depends on another (as in a path), the chain rule adds that term.

</div>

<div class="warning" markdown>

Watch out: the existence of $f_x$ and $f_y$ doesn't make a function continuous or differentiable. The function $\frac{xy}{x^2 + y^2}$ has both partials at the origin and no limit there. The tangent plane and the chain rule need continuous partial derivatives near the point, which every function you meet in this book has.

</div>

<div class="warning" markdown>

Watch out: directional derivatives need a unit vector. For the direction $(3, 4)$ the vector to use is $\left(\frac{3}{5}, \frac{4}{5}\right)$, and $\nabla f \cdot (3, 4)$ is five times too large. In Example 3 the direction $(2, 1)$ was divided by $\sqrt{5}$ for this reason.

</div>

<div class="warning" markdown>

Watch out: the gradient lives in the input plane. It is a vector in the plane of $(x, y)$ that points uphill on the contour map, not an arrow along the surface. Its length is a slope (height per distance), but its direction is a direction of the map. Also, going down needs the minus sign: gradient ascent adds $\eta\nabla f$ and gradient descent subtracts it.

</div>

<div class="warning" markdown>

Watch out: the slope of a level curve is $-\frac{f_x}{f_y}$, with the minus sign and with $f_x$ on top. For $f = \sqrt{xy}$ at $(2, 2)$, $f_x = f_y$, so the slope is $-1$. Writing $+\frac{f_x}{f_y}$ gives $+1$, which is the slope of the line $y = x$, perpendicular to the contour and parallel to the gradient.

</div>

<div class="warning" markdown>

Watch out: at a point where $\nabla f = \mathbf{0}$ there is no steepest direction. All directional derivatives are $0$ there. Such a point is a critical point, the subject of the next lesson, and gradient descent stops there (and might stop at a maximum or a saddle).

</div>

## Tricks and shortcuts

To check a partial derivative by hand, change the input by a tiny amount and compare: if $f_x(a, b) = 2$ then $f(a + 0.001, b) - f(a, b)$ should be about $0.002$. The "In code" section turns this into a function that checks any gradient, which is also how machine-learning code tests its derivatives.

The tangent line to a level curve at $(a, b)$ is quick to write down with the gradient: $f_x(a, b)(x - a) + f_y(a, b)(y - b) = 0$. For the hill at $(1, 1)$ that is $-2(x - 1) - 4(y - 1) = 0$, or $y = 1.5 - 0.5x$, the dashed blue line of the figure (slope $-\frac{1}{2}$, which is the direction $(2, -1)$).

For a Cobb-Douglas function, take logs. $\ln Q = \ln A + \alpha\ln K + \beta\ln L$ is linear in $\ln K$ and $\ln L$, so the exponents are the elasticities and the marginal products are $\alpha\frac{Q}{K}$ and $\beta\frac{Q}{L}$ without differentiating the power.

## In code

A central-difference gradient (the check for a hand computation), the directional derivative and marginal products from it, gradient descent with five learning rates on $x^2 + 5y^2$, and gradient descent for the line fit of Example 6.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

def num_grad(f, p, h=1e-6):
    """Central-difference gradient of f at the point p."""
    p = np.asarray(p, dtype=float)
    g = np.zeros_like(p)
    for i in range(len(p)):
        e = np.zeros_like(p)
        e[i] = h
        g[i] = (f(p + e) - f(p - e)) / (2 * h)
    return g

hill = lambda p: 4 - p[0] ** 2 - 2 * p[1] ** 2
g = num_grad(hill, [1, 1])
print(g.round(4), round(np.linalg.norm(g), 4))
# [-2. -4.] 4.4721
u = np.array([2, 1]) / np.sqrt(5)
print(round(g @ u, 4))
# -3.5777

# Marginal products of Q = 10 K^0.3 L^0.7 at (100, 100).
Q = lambda p: 10 * p[0] ** 0.3 * p[1] ** 0.7
print(num_grad(Q, [100, 100]).round(4), round(Q([100, 100]), 4))
# [3. 7.] 1000.0

# Gradient descent on f(x, y) = x^2 + 5 y^2 from (4, 1.5).
grad = lambda p: np.array([2 * p[0], 10 * p[1]])
for eta in (0.05, 1 / 6, 0.18, 0.2, 0.21):
    p = np.array([4.0, 1.5])
    for _ in range(30):
        p = p - eta * grad(p)
    print(round(eta, 4), round(p[0], 5), round(p[1], 5), round(p[0] ** 2 + 5 * p[1] ** 2, 4))
# 0.05 0.16956 0.0 0.0288
# 0.1667 2e-05 1e-05 0.0
# 0.18 1e-05 0.00186 0.0
# 0.2 0.0 1.5 11.25
# 0.21 0.0 26.1741 3425.4184

# Least squares by gradient descent: fit y = w0 + w1 x to (1,2), (2,3), (3,5).
X = np.array([[1, 1], [1, 2], [1, 3]], dtype=float)
y = np.array([2, 3, 5], dtype=float)
w = np.zeros(2)
for step in range(1, 1001):
    w = w - 0.05 * (2 / 3) * X.T @ (X @ w - y)
    if step in (1, 10, 100, 1000):
        print(step, np.round(w, 4))
# 1 [0.3333 0.7667]
# 10 [0.5756 1.3929]
# 100 [0.415  1.4641]
# 1000 [0.3333 1.5   ]
print(np.round(np.linalg.lstsq(X, y, rcond=None)[0], 4))
# [0.3333 1.5   ]
```

The first three rates converge (the slowest, $\eta = 0.05$, is still at $x \approx 0.17$ after 30 steps), the rate $\eta = 0.2$ leaves $y$ stuck at $1.5$ in absolute value, and $\eta = 0.21$ makes it grow. For the line fit, the learning rate is limited by the largest eigenvalue of the Hessian (about $11.09$), so it must be below $\frac{2}{11.09} \approx 0.18$, and the small eigenvalue (about $0.24$) is why 100 steps are not enough.

</details>

## FAQ

### Why is the gradient a vector and not just a list of numbers?

Because it answers a geometric question. The directional derivative in any direction is the dot product of the gradient with that direction, and the direction of the largest slope is the gradient's own direction. Both facts are statements about vectors, and they would be nonsense for an arbitrary list. In machine learning the gradient of a loss with a million parameters is a vector of length a million, and it is used the same way.

### What if the partial derivatives exist but the function isn't differentiable?

Then the tangent plane isn't a good approximation, and the formula $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$ can fail. The example $\frac{xy}{x^2 + y^2}$ above is one. In practice, functions built from the usual formulas have continuous partials away from trouble spots such as zero denominators and corners, and the theorems of this lesson hold. Where a function has a corner (such as $\lvert x \rvert + \lvert y \rvert$ at the origin), there is no gradient, and optimization code uses a "subgradient" instead.

### Why does gradient descent zigzag?

Because the gradient is perpendicular to the level curve and points straight across the valley, not along it. In a long narrow valley, the steepest direction at the side points mostly across the valley floor, so the step overshoots the floor and lands on the other side, while the slow progress along the valley is the small component. A smaller learning rate stops the zigzag but slows everything. Methods such as momentum and Adam are fixes for this, and they are the subject of a machine-learning course.

### Is a partial derivative a rate of change in the usual sense?

Yes, with a condition: the other variables are held fixed. If they can't be held fixed (a firm that raises its capital also hires more labour), the full change comes from the chain rule, which adds one term per variable.

## Practice

### Warm-up

1\. Find $f_x$ and $f_y$ for $f(x, y) = x^3y^2 - 4xy + \sin y$, and evaluate both at $(2, 0)$.

<details class="solution" markdown>
<summary>Solution</summary>

Holding $y$ fixed: $f_x = 3x^2y^2 - 4y$. Holding $x$ fixed: $f_y = 2x^3y - 4x + \cos y$. At $(2, 0)$: $f_x = 0 - 0 = 0$ and $f_y = 0 - 8 + 1 = -7$.

Check: $f(x, 0) = 0$ for all $x$, so $f_x(2, 0) = 0$. And $f(2, y) = 8y^2 - 8y + \sin y$ has derivative $16y - 8 + \cos y = -7$ at $y = 0$.

</details>

2\. Find the gradient of $f(x, y, z) = x^2 + 2yz - z^3$ at $(1, 2, -1)$.

<details class="solution" markdown>
<summary>Solution</summary>

$\nabla f = (2x, 2z, 2y - 3z^2)$. At $(1, 2, -1)$ this is $(2, -2, 4 - 3) = (2, -2, 1)$.

Check: increasing $x$ by $0.001$ changes $f$ by about $0.002 = 2 \cdot 0.001$; $f(1.001, 2, -1) - f(1, 2, -1) = 1.002001 - 1 = 0.002001$.

</details>

3\. Find the tangent plane to $z = x^2 + y^2$ at $(1, 2)$ and use it to estimate $f(1.1, 1.9)$.

<details class="solution" markdown>
<summary>Solution</summary>

At $(1, 2)$: $f = 5$, $f_x = 2x = 2$ and $f_y = 2y = 4$. The plane is $z = 5 + 2(x - 1) + 4(y - 2)$. At $(1.1, 1.9)$: $z = 5 + 0.2 - 0.4 = 4.8$.

Check: the exact value is $1.21 + 3.61 = 4.82$, so the estimate is off by $0.02$, which is the size of $h^2 + k^2 = 0.02$, the part the plane ignores.

</details>

### Standard

4\. Find the directional derivative of $f(x, y) = x^2y$ at $(2, 1)$ in the direction of $(1, -1)$. In which direction is $f$ increasing fastest at that point, and at what rate?

<details class="solution" markdown>
<summary>Solution</summary>

$\nabla f = (2xy, x^2) = (4, 4)$ at $(2, 1)$. The unit vector is $\mathbf{u} = \frac{(1, -1)}{\sqrt{2}}$, so $D_{\mathbf{u}}f = \frac{4 - 4}{\sqrt{2}} = 0$. The fastest increase is along $\frac{(4, 4)}{\sqrt{32}} = \frac{(1, 1)}{\sqrt{2}}$, at the rate $\lVert (4, 4) \rVert = 4\sqrt{2} \approx 5.657$.

Check: $(1, -1)$ is perpendicular to $(4, 4)$, so the contour through $(2, 1)$ runs in that direction and the rate is $0$. Numerically, the contour $x^2y = 4$ passes through $(2, 1)$ and $(2.1, 0.907)$, a step of $(0.1, -0.093)$, nearly along $(1, -1)$.

</details>

5\. A path is $\mathbf{r}(t) = (\cos t, \sin t)$ and $f(x, y) = x^2 + 3xy$. Use the chain rule to find $\frac{d}{dt}f(\mathbf{r}(t))$ at $t = \frac{\pi}{4}$, and check by substituting first.

<details class="solution" markdown>
<summary>Solution</summary>

$\nabla f = (2x + 3y, 3x)$. At $t = \frac{\pi}{4}$ the point is $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ and $\mathbf{r}' = (-\sin t, \cos t) = \left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$. So $\nabla f = \left(\frac{5}{\sqrt{2}}, \frac{3}{\sqrt{2}}\right)$ and the derivative is $\frac{5}{\sqrt{2}} \cdot \left(-\frac{1}{\sqrt{2}}\right) + \frac{3}{\sqrt{2}} \cdot \frac{1}{\sqrt{2}} = -\frac{5}{2} + \frac{3}{2} = -1$.

Check: $f(\mathbf{r}(t)) = \cos^2 t + 3\cos t\sin t$, whose derivative is $-2\cos t\sin t + 3(\cos^2 t - \sin^2 t)$. At $t = \frac{\pi}{4}$ this is $-2 \cdot \frac{1}{2} + 3 \cdot 0 = -1$.

</details>

6\. A hypothetical firm has $Q = 20K^{0.4}L^{0.6}$. At $K = 32$ and $L = 243$, find $Q_K$ and $Q_L$ (using $32^{0.4} = 4$ and $243^{0.6} = 27$), and the slope of the isoquant there. Does the marginal product of labour rise or fall as $L$ grows?

<details class="solution" markdown>
<summary>Solution</summary>

$Q = 20 \cdot 4 \cdot 27 = 2160$. Then $Q_K = 0.4\frac{Q}{K} = \frac{0.4 \cdot 2160}{32} = 27$ and $Q_L = 0.6\frac{Q}{L} = \frac{0.6 \cdot 2160}{243} = \frac{1296}{243} = 5.333$. The slope of the isoquant is $-\frac{Q_K}{Q_L} = -\frac{27}{5.333} = -5.0625$. For the last part, $Q_{LL} = 0.6(0.6 - 1)\frac{Q}{L^2} < 0$, so the marginal product of labour falls as $L$ grows.

Check: $-\frac{Q_K}{Q_L} = -\frac{0.4}{0.6}\cdot\frac{L}{K} = -\frac{2}{3} \cdot \frac{243}{32} = -5.0625$, in agreement.

</details>

### Challenge

7\. Let $f(x, y) = x^2 - y^2$. (a) Find the directions $\mathbf{u}$ at $(1, 1)$ for which $D_{\mathbf{u}}f = 0$, and describe the level curve through $(1, 1)$. (b) Show by Theorem 3 that $\nabla f$ is perpendicular to the level curve at every point, by parametrizing the level curve $x^2 - y^2 = 1$ as $(\cosh t, \sinh t)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\nabla f = (2x, -2y) = (2, -2)$ at $(1, 1)$. The unit vectors with zero dot product are $\pm\frac{(1, 1)}{\sqrt{2}}$. The level curve through $(1, 1)$ is $x^2 - y^2 = 0$, the pair of lines $y = x$ and $y = -x$, and the direction $(1, 1)$ runs along the first line. The two lines cross at the origin, where $\nabla f = \mathbf{0}$, so Theorem 3 says nothing about that point.

(b) On the curve $x^2 - y^2 = 1$ the path $\mathbf{r}(t) = (\cosh t, \sinh t)$ has $\cosh^2 t - \sinh^2 t = 1$. The gradient there is $(2\cosh t, -2\sinh t)$ and $\mathbf{r}' = (\sinh t, \cosh t)$. The dot product is $2\cosh t\sinh t - 2\sinh t\cosh t = 0$.

Check at $t = 0$: the point is $(1, 0)$, the gradient is $(2, 0)$ and the tangent is $(0, 1)$, which are perpendicular.

</details>

8\. (Reviews [optimization](../03-applications-of-derivatives/05-optimization.md).) For $f(x, y) = (x - 1)^2 + 4(y + 2)^2$, show that gradient descent satisfies $x_{n+1} - 1 = (1 - 2\eta)(x_n - 1)$ and $y_{n+1} + 2 = (1 - 8\eta)(y_n + 2)$, and find the learning rates that converge and the best one.

<details class="solution" markdown>
<summary>Solution</summary>

The gradient is $(2(x - 1), 8(y + 2))$. The update $x_{n+1} = x_n - 2\eta(x_n - 1)$ gives $x_{n+1} - 1 = (1 - 2\eta)(x_n - 1)$, and $y_{n+1} = y_n - 8\eta(y_n + 2)$ gives $y_{n+1} + 2 = (1 - 8\eta)(y_n + 2)$. The method converges to $(1, -2)$ when both factors have absolute value below 1: $0 < \eta < 1$ for the first and $0 < \eta < \frac{1}{4}$ for the second, so the condition is $0 < \eta < \frac{1}{4}$. The best rate balances $1 - 2\eta = -(1 - 8\eta)$, so $\eta = \frac{1}{5}$, with both factors of size $0.6$.

Check: with $\eta = 0.2$ the factors are $1 - 0.4 = 0.6$ and $1 - 1.6 = -0.6$. In general the best rate is $\frac{2}{\lambda_{\min} + \lambda_{\max}} = \frac{2}{2 + 8} = 0.2$, where the eigenvalues of the Hessian are $2$ and $8$.

</details>

## Where this shows up

- The next lesson, [multivariable optimization and Lagrange multipliers](03-multivariable-optimization-and-lagrange-multipliers.md), sets the gradient equal to $\mathbf{0}$ to find the highest and lowest points, and uses Theorem 3 to explain Lagrange multipliers: at the best point on a constraint, two level curves touch, so their gradients are parallel. The optional lesson on [double integrals](04-double-integrals.md) adds up a function of two variables instead of differentiating it.
- In CS, every neural network and every logistic or linear regression is trained by gradient descent or a variant, and backpropagation is the chain rule along a path of computations. A numerical gradient check is a standard test for such code. The lesson on [correlation and linear regression](../08-statistics/04-correlation-and-linear-regression.md) finds the least-squares line from the normal equations, which are the partial derivatives of the sum of squared errors set to $0$ (Example 6 of the next lesson shows this).
- In economics, marginal products, marginal utilities and the marginal rate of substitution are partial derivatives, and production functions such as Cobb-Douglas are covered in production and cost functions<!-- link: ../../07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md --> and utility and indifference curves<!-- link: ../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md -->.
