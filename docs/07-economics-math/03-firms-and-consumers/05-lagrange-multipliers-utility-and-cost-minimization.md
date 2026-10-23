# Lagrange multipliers, utility and cost minimization

After this lesson you can solve the Cobb-Douglas consumer's problem in general, write the demand functions and say what the multiplier means, solve the dual problem of minimizing expenditure or cost, use the envelope theorem, split a price change into substitution and income effects with numbers, and tell when the Lagrange method gives a wrong answer because the best bundle is at a corner.

Before this: [utility and indifference curves](04-utility-and-indifference-curves.md), [production and cost functions](02-production-and-cost-functions.md) and [multivariable optimization and Lagrange multipliers](../../05-university-core/09-multivariable-calculus-light/03-multivariable-optimization-and-lagrange-multipliers.md). That lesson solved one utility example and one cost example with numbers. This lesson solves the whole family at once and goes on to the dual problem.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A consumer has $U = x^{0.3}y^{0.7}$, income \$100, and prices $p_x = \$5$ and $p_y = \$2$. How much of each good do they buy?
2. For $U = xy$ with income 80 and prices 2 and 4, the best bundle is $(20, 10)$ with $U = 200$. Find the multiplier $\lambda$ from $\frac{U_x}{p_x}$.
3. A firm needs output $Q = \sqrt{KL}$ at the least cost with $r = \$4$ and $w = \$4$. What is the ratio $\frac{K}{L}$ it chooses?

<details class="solution" markdown>
<summary>Answers</summary>

1. The shares of income are 30% and 70%: $x = \frac{0.3 \cdot 100}{5} = 6$ and $y = \frac{0.7 \cdot 100}{2} = 35$.
2. $U_x = y = 10$, so $\lambda = \frac{10}{2} = 5$. (Check: $\frac{U_y}{p_y} = \frac{20}{4} = 5$.)
3. The MRTS is $\frac{K}{L}$ and it must equal $\frac{w}{r} = 1$, so $K = L$.

</details>

## The idea

The last lesson found the best bundle by drawing: the indifference curve touches the budget line. Lagrange's method does the same thing with algebra, and it does it for any prices and any income at once. Solve it once with letters and you have the demand functions, formulas that say how much a consumer buys at every price and income. For the Cobb-Douglas family the answer is simple enough to remember: spend a fixed fraction of income on each good.

The multiplier $\lambda$ that comes out of the method is a by-product with an economic meaning: the extra utility from one more dollar. That meaning is a special case of a general result, the envelope theorem, which says that the way the best value of a problem changes with a parameter doesn't depend on how the best point itself moves. It is why economists can skip a lot of algebra.

Every maximization problem has a mirror image. The consumer who maximizes utility for a budget could instead minimize spending to reach a target utility, and the firm that picks inputs for the least cost is solving that second kind of problem. The two problems give related answers, and the difference between them is how economists split a price change into a substitution effect and an income effect. Finally, the method assumes that the best point is in the interior with a tangency. When it isn't, the equations still have a solution, and it is wrong, so the lesson ends by saying how to notice.

## Definitions

In the **utility maximization problem** the consumer chooses $(x, y)$ to maximize $U(x, y)$ subject to $p_xx + p_yy = m$. The solution as a function of the prices and income, $x^*(p_x, p_y, m)$ and $y^*(p_x, p_y, m)$, is the **Marshallian demand** (or ordinary demand). The best utility, $V(p_x, p_y, m) = U(x^*, y^*)$, is the **indirect utility function**.

In the **expenditure minimization problem** the consumer chooses $(x, y)$ to minimize $p_xx + p_yy$ subject to $U(x, y) = \bar{u}$. The solution $h_x(p_x, p_y, \bar{u})$ and $h_y(p_x, p_y, \bar{u})$ is the **Hicksian demand** (or compensated demand), and the least spending, $e(p_x, p_y, \bar{u}) = p_xh_x + p_yh_y$, is the **expenditure function**. In plain words, Marshallian demand answers "what do I buy with this much money?", and Hicksian demand answers "what is the cheapest way to be this well off?".

The firm's version is the **cost minimization problem**: choose $(K, L)$ to minimize $rK + wL$ subject to $f(K, L) = Q$. Its solution $K(r, w, Q)$ and $L(r, w, Q)$ is the pair of **conditional factor demands** (conditional on the output $Q$), and the least cost is the cost function $C(r, w, Q)$.

The **Lagrangian** of a problem to optimize $f(\mathbf{x}, \theta)$ subject to $g(\mathbf{x}, \theta) = 0$ is $\mathcal{L} = f - \lambda g$, where $\theta$ stands for the parameters (prices, income, output). The multiplier is the number $\lambda$ at the solution with $\nabla_{\mathbf{x}} f = \lambda\nabla_{\mathbf{x}} g$.

## How to do it

### Utility maximization for Cobb-Douglas

*Theorem 1.* Let $U = x^ay^b$ with $a, b > 0$, and let prices and income be positive. The unique best bundle with $x, y > 0$ on the budget line $p_xx + p_yy = m$ is

$$
x^* = \frac{a}{a + b}\cdot\frac{m}{p_x}, \qquad y^* = \frac{b}{a + b}\cdot\frac{m}{p_y},
$$

so the consumer spends the fraction $\frac{a}{a + b}$ of income on $x$ and $\frac{b}{a + b}$ on $y$, and the multiplier is $\lambda = \frac{(a + b)\,U^*}{m}$.

What we know: the conditions $U_x = \lambda p_x$, $U_y = \lambda p_y$ and the budget, from the multivariable lesson. What we want: $x$, $y$ and $\lambda$ in terms of the parameters. The plan is to multiply the first two conditions by $x$ and $y$ to get the spending on each good in terms of $\lambda$, then use the budget.

*Proof.* For $U = x^ay^b$ we have $U_x = \frac{aU}{x}$ and $U_y = \frac{bU}{y}$. The conditions become $\frac{aU}{x} = \lambda p_x$ and $\frac{bU}{y} = \lambda p_y$. Multiply the first by $x$ and the second by $y$: $p_xx = \frac{aU}{\lambda}$ and $p_yy = \frac{bU}{\lambda}$. Add and use the budget: $m = \frac{(a + b)U}{\lambda}$, so $\lambda = \frac{(a + b)U}{m}$. Then $p_xx = \frac{aU}{\lambda} = \frac{a\,m}{a + b}$ and $p_yy = \frac{b\,m}{a + b}$, which gives the formulas. The point is the maximum: the budget line is bounded, the utility is $0$ on the axes and positive in between, so the best point is interior, and it is the only solution of the conditions. $\blacksquare$

Look back at the result. The shares $\frac{a}{a + b}$ and $\frac{b}{a + b}$ don't depend on prices or income, which makes the demand for $x$ proportional to income and inversely proportional to its own price, with no effect from the price of $y$. Only the ratio of the exponents matters: $U = xy^2$ and $U = x^{0.5}y$ have the same shares, $\frac{1}{3}$ and $\frac{2}{3}$. This is Theorem 1 of the last lesson again, since $x^{0.5}y = \sqrt{xy^2}$.

### The multiplier and the envelope theorem

*Theorem 2 (envelope theorem).* Let $V(\theta) = \max f(\mathbf{x}, \theta)$ subject to $g(\mathbf{x}, \theta) = 0$, let the solution $\mathbf{x}^*(\theta)$ be differentiable with multiplier $\lambda$, and let $f$ and $g$ be differentiable. Then

$$
\frac{dV}{d\theta} = \frac{\partial\mathcal{L}}{\partial\theta}\bigg|_{\mathbf{x}^*} = \frac{\partial f}{\partial\theta} - \lambda\frac{\partial g}{\partial\theta}.
$$

What we know: $V(\theta) = f(\mathbf{x}^*(\theta), \theta)$, the constraint holds for every $\theta$, and the first-order condition $\nabla_{\mathbf{x}} f = \lambda\nabla_{\mathbf{x}} g$ holds at the solution. What we want: the derivative of $V$. The plan is the chain rule, then using the constraint to cancel the terms that contain how the solution moves.

*Proof.* The chain rule gives $\frac{dV}{d\theta} = \nabla_{\mathbf{x}} f\cdot\frac{d\mathbf{x}^*}{d\theta} + \frac{\partial f}{\partial\theta}$. Differentiating the identity $g(\mathbf{x}^*(\theta), \theta) = 0$ gives $\nabla_{\mathbf{x}} g\cdot\frac{d\mathbf{x}^*}{d\theta} + \frac{\partial g}{\partial\theta} = 0$. By the first-order condition $\nabla_{\mathbf{x}} f\cdot\frac{d\mathbf{x}^*}{d\theta} = \lambda\nabla_{\mathbf{x}} g\cdot\frac{d\mathbf{x}^*}{d\theta} = -\lambda\frac{\partial g}{\partial\theta}$. Substituting, $\frac{dV}{d\theta} = \frac{\partial f}{\partial\theta} - \lambda\frac{\partial g}{\partial\theta}$. $\blacksquare$

Look back: the proof says that the best point shifts a bit when $\theta$ changes, but a small shift of a point that is already best costs nothing to first order, apart from what the constraint does. For the consumer, write the constraint as $g = p_xx + p_yy - m$. With $\theta = m$ we get $\frac{\partial V}{\partial m} = \lambda$, the marginal utility of income. With $\theta = p_x$ we get $\frac{\partial V}{\partial p_x} = -\lambda x^*$: a rise in $p_x$ by one dollar costs the consumer $x^*$ dollars, worth $\lambda$ utility each. For the firm, $\theta = Q$ with $g = Q - f$ gives $\frac{\partial C}{\partial Q} = \lambda$, so the multiplier is the marginal cost, and $\theta = r$ gives $\frac{\partial C}{\partial r} = K^*$.

The multiplier depends on how utility is labelled. If $U$ is replaced by $g(U)$, the demands don't change (lesson 4), but $\lambda$ is multiplied by $g'(U)$. So $\lambda$ is a number in the units of the utility function and is not itself observable, while the demand functions are.

### Expenditure minimization and Hicksian demand

*Theorem 3.* For $U = x^ay^b$ and the target utility $\bar{u}$, the cheapest bundle on the indifference curve is

$$
h_x = \bar{u}^{\frac{1}{a + b}}\left(\frac{a\,p_y}{b\,p_x}\right)^{\frac{b}{a + b}}, \qquad h_y = \bar{u}^{\frac{1}{a + b}}\left(\frac{b\,p_x}{a\,p_y}\right)^{\frac{a}{a + b}},
$$

and the expenditure function is $e = (a + b)\,\bar{u}^{\frac{1}{a + b}}\left(\frac{p_x}{a}\right)^{\frac{a}{a + b}}\left(\frac{p_y}{b}\right)^{\frac{b}{a + b}}$.

What we know: the problem has the same tangency condition as before, with the roles of the objective and the constraint swapped. What we want: the bundle on the curve $x^ay^b = \bar{u}$ with the lowest cost. The plan is to use the Lagrangian $p_xx + p_yy - \mu(x^ay^b - \bar{u})$, get the ratio of $y$ to $x$, and substitute into the constraint.

*Proof.* The conditions are $p_x = \mu\frac{a\bar{u}}{x}$ and $p_y = \mu\frac{b\bar{u}}{y}$, so $p_xx = \mu a\bar{u}$ and $p_yy = \mu b\bar{u}$. Dividing, $\frac{p_xx}{a} = \frac{p_yy}{b}$, so $y = \frac{b\,p_x}{a\,p_y}x$. The constraint becomes $\bar{u} = x^a\left(\frac{b\,p_x}{a\,p_y}\right)^bx^b$, so $x^{a + b} = \bar{u}\left(\frac{a\,p_y}{b\,p_x}\right)^b$, which gives $h_x$. Then $h_y = \frac{b\,p_x}{a\,p_y}h_x$ gives $h_y$ after simplifying, and $e = p_xh_x + p_yh_y$ simplifies to the stated form. $\blacksquare$

Look back: the tangency is the same equation as in the utility problem, $\frac{U_x}{U_y} = \frac{p_x}{p_y}$, because both problems look for the point where an indifference curve and a budget line touch. The two problems are duals. If you spend the least amount $e$ needed to reach $\bar{u}$, the best you can do with the income $m = e$ is $\bar{u}$ again: $e\bigl(p, V(p, m)\bigr) = m$ and $V\bigl(p, e(p, \bar{u})\bigr) = \bar{u}$. In particular, $h(p, V(p, m)) = x^*(p, m)$: the two demands agree at matching utility and income. The multiplier $\mu$ is the marginal cost of utility, $\frac{\partial e}{\partial\bar{u}}$.

For a firm, the same proof with $f = K^\alpha L^\beta$ gives the conditional factor demands

$$
K = Q^{\frac{1}{\alpha + \beta}}\left(\frac{\alpha\,w}{\beta\,r}\right)^{\frac{\beta}{\alpha + \beta}}, \qquad L = Q^{\frac{1}{\alpha + \beta}}\left(\frac{\beta\,r}{\alpha\,w}\right)^{\frac{\alpha}{\alpha + \beta}},
$$

and the cost function $C = (\alpha + \beta)\,Q^{\frac{1}{\alpha + \beta}}\left(\frac{r}{\alpha}\right)^{\frac{\alpha}{\alpha + \beta}}\left(\frac{w}{\beta}\right)^{\frac{\beta}{\alpha + \beta}}$. It is proportional to $Q^{1/(\alpha + \beta)}$, matching Theorem 4 of [production and cost functions](02-production-and-cost-functions.md).

### Substitution and income effects

When the price of $x$ rises, the consumer buys less $x$ for two reasons: $x$ is dearer relative to $y$ (a substitution effect), and the consumer is poorer (an income effect). The Hicks decomposition measures the first with Hicksian demand: it holds utility fixed at the old level and lets only the relative price change.

1. Find the old best bundle $x_0$ and the old utility $u_0$.
2. Find the new Marshallian demand $x_1$ at the new prices and the old income.
3. Find the Hicksian demand $h_x(p^{new}, u_0)$, the cheapest way to get the old utility at the new prices. The substitution effect is $h_x - x_0$.
4. The income effect is $x_1 - h_x$. The total is $x_1 - x_0$, the sum of the two.

*Theorem 4 (Slutsky equation).* For the demand $x(p_x, m)$ and the Hicksian demand $h_x(p_x, u)$,

$$
\frac{\partial x}{\partial p_x} = \frac{\partial h_x}{\partial p_x} - x\,\frac{\partial x}{\partial m}.
$$

What we know: $x\bigl(p_x, e(p_x, u)\bigr) = h_x(p_x, u)$, because the compensated and ordinary demands agree when income is exactly the expenditure needed for $u$, and $\frac{\partial e}{\partial p_x} = h_x$ (the envelope theorem applied to expenditure minimization). What we want: the slope of ordinary demand in terms of the other two. The plan is to differentiate the identity with respect to $p_x$.

*Proof.* Differentiating $x\bigl(p_x, e(p_x, u)\bigr) = h_x(p_x, u)$ with respect to $p_x$ by the chain rule gives $\frac{\partial x}{\partial p_x} + \frac{\partial x}{\partial m}\cdot\frac{\partial e}{\partial p_x} = \frac{\partial h_x}{\partial p_x}$. Replace $\frac{\partial e}{\partial p_x}$ with $h_x = x$ at the point and rearrange. $\blacksquare$

Look back: the first term of the Slutsky equation is the substitution effect (always negative or zero for a price rise) and the second is the income effect, $-x\frac{\partial x}{\partial m}$, which is negative for a normal good, where more income means more demand. Example 4 computes both with numbers.

### When the method fails

The conditions $\nabla U = \lambda\nabla g$ are necessary only for an interior point with $x, y > 0$, differentiable $U$ and $\nabla g \ne \mathbf{0}$. Three things go wrong.

- The solution has a negative quantity. Then the real answer is a corner with that good at zero, where the tangency condition fails (it holds only as an inequality).
- The preferences have a kink (perfect complements), where the derivative doesn't exist.
- The second-order condition fails (non-convex preferences), so a tangency point is a minimum along the budget line.

The usual rule: solve the equations, then check that $x, y \ge 0$; if one is negative, set it to 0 and see whether the remaining good takes all the income, and compare the utility with the other candidates.

## Worked examples

<div class="example" markdown>

### Example 1: Cobb-Douglas demand with exponents that don't add to 1

A consumer has $U = x^{0.5}y^{1.5}$ (made up), income \$200, and prices $p_x = \$2$, $p_y = \$5$. Find the best bundle, the utility and the multiplier.

Step 1: the exponents are $a = 0.5$ and $b = 1.5$, so $a + b = 2$, and the shares are $\frac{a}{a + b} = 0.25$ and $\frac{b}{a + b} = 0.75$.

Step 2: spending on $x$ is $0.25 \cdot 200 = 50$, so $x^* = \frac{50}{2} = 25$. Spending on $y$ is $0.75 \cdot 200 = 150$, so $y^* = \frac{150}{5} = 30$.

Step 3: the utility is $U^* = 25^{0.5}\cdot 30^{1.5} = 5 \cdot 164.32 \approx 821.58$. The multiplier is $\lambda = \frac{(a + b)U^*}{m} = \frac{2 \cdot 821.58}{200} \approx 8.216$.

Check: the first-order conditions agree: $\frac{U_x}{p_x} = \frac{0.5U/x}{2} = \frac{0.5 \cdot 821.58/25}{2} \approx 8.216$ and $\frac{U_y}{p_y} = \frac{1.5 \cdot 821.58/30}{5} \approx 8.216$. Nearby bundles on the budget line do worse: $(20, 32)$ gives $809.5$ and $(30, 28)$ gives $811.5$, both below $821.6$.

</div>

<div class="example" markdown>

### Example 2: demand functions and the meaning of the multiplier

Take the consumer of lesson 4, $U = xy^2$ with $p_x = \$3$, $p_y = \$2$ and $m = \$90$ (made up). Find the demand functions, the multiplier, and check the envelope theorem.

By Theorem 1 with $a = 1$ and $b = 2$, $x^* = \frac{m}{3p_x}$ and $y^* = \frac{2m}{3p_y}$. At the given numbers, $x^* = 10$ and $y^* = 30$, and $U^* = 9000$. Doubling $p_x$ to \$6 halves the demand for $x$ to 5, and leaves $y^* = 30$ unchanged.

The multiplier is $\lambda = \frac{(a + b)U^*}{m} = \frac{3 \cdot 9000}{90} = 300$ utility units per dollar. The indirect utility is $V = \frac{4}{27}\cdot\frac{m^3}{p_xp_y^2}$, so $\frac{\partial V}{\partial m} = \frac{3V}{m} = 300$, equal to $\lambda$. Also $\frac{\partial V}{\partial p_x} = -\frac{V}{p_x} = -3000$, and $-\lambda x^* = -300 \cdot 10 = -3000$.

Relabelling changes $\lambda$ but not the demand. Take $W = \ln U = \ln x + 2\ln y$. The demand is the same, since the shares are $\frac{1}{3}$ and $\frac{2}{3}$, but now the multiplier is $\frac{(a + b)}{m} = \frac{3}{90} = \frac{1}{30}$, which is $\frac{300}{9000}$, the old $\lambda$ divided by $U$.

Check: the real gain from one more dollar is $V(91) - V(90) = \frac{91^3}{81} - 9000 \approx 303.3$, close to the rate $\lambda = 300$ (the rate at the point, and utility is convex in income here).

</div>

<div class="example" markdown>

### Example 3: cost minimization and conditional factor demands

A firm has $Q = K^{1/4}L^{1/4}$ with $r = \$2$ and $w = \$8$ (made up; the exponents add to $\frac{1}{2}$, so returns to scale are decreasing). Find the cheapest inputs for $Q$, the cost function, and the marginal cost.

Step 1: the tangency is $MRTS = \frac{\beta}{\alpha}\frac{K}{L} = \frac{K}{L} = \frac{w}{r} = 4$, so $K = 4L$.

Step 2: the output constraint is $(KL)^{1/4} = Q$, so $KL = Q^4$. With $K = 4L$ this is $4L^2 = Q^4$, so $L = \frac{Q^2}{2}$ and $K = 2Q^2$. (These agree with the general formulas, with $\alpha + \beta = \frac{1}{2}$.)

Step 3: the cost is $C(Q) = 2 \cdot 2Q^2 + 8 \cdot \frac{Q^2}{2} = 4Q^2 + 4Q^2 = 8Q^2$, and the marginal cost is $C'(Q) = 16Q$, rising: decreasing returns to scale.

For $Q = 3$: $K = 18$, $L = 4.5$, $C = 72$ and $MC = 48$. The multiplier from $r = \lambda\frac{\partial Q}{\partial K} = \lambda\frac{\alpha Q}{K}$ is $\lambda = \frac{rK}{\alpha Q} = \frac{2 \cdot 18}{0.25 \cdot 3} = 48$, the marginal cost, as Theorem 2 says. And $\frac{\partial C}{\partial r} = Q^2\sqrt{w/r} = 18 = K$.

Check: $(18 \cdot 4.5)^{1/4} = 81^{1/4} = 3$ and $2 \cdot 18 + 8 \cdot 4.5 = 72$. A nearby input mix for the same output costs more: $K = 9$ and $L = 9$ gives $(81)^{1/4} = 3$ at the cost $18 + 72 = 90$.

</div>

<div class="example" markdown>

### Example 4: Hicksian demand and the Slutsky decomposition

A consumer has $U = \sqrt{xy}$ (made up), income \$100 and the price $p_y = \$1$. The price of $x$ rises from \$1 to \$4. Split the change in the demand for $x$ into the substitution and income effects.

Step 1: the old demand is $x_0 = \frac{m}{2p_x} = 50$ and $y_0 = 50$, with $u_0 = \sqrt{2500} = 50$.

Step 2: the new demand at $p_x = 4$ with the old income is $x_1 = \frac{100}{2 \cdot 4} = 12.5$. The total change is $12.5 - 50 = -37.5$.

Step 3: Hicksian demand at the new prices and the old utility. By Theorem 3 with $a = b = \frac{1}{2}$, $h_x = u_0\sqrt{\frac{p_y}{p_x}} = 50 \cdot \frac{1}{2} = 25$ and $h_y = u_0\sqrt{\frac{p_x}{p_y}} = 100$. The cost is $4 \cdot 25 + 100 = 200$: to be as well off as before at the new prices the consumer would need \$200, not \$100. The substitution effect is $25 - 50 = -25$.

Step 4: the income effect is $12.5 - 25 = -12.5$, the fall in demand from being left with \$100 and not \$200. The total is $-25 + (-12.5) = -37.5$.

So two thirds of the fall is substitution and one third is income. The slope version at the old point gives the same split: $\frac{\partial x}{\partial p_x} = -\frac{m}{2p_x^2} = -50$, $\frac{\partial h_x}{\partial p_x} = -\frac{1}{2}u_0p_x^{-3/2} = -25$ and $-x\frac{\partial x}{\partial m} = -50 \cdot \frac{1}{2} = -25$, which sum to $-50$ as Theorem 4 says.

Check: the Marshallian demand at the new prices with the compensating income \$200 is $\frac{200}{8} = 25 = h_x$, as the duality predicts. And the utility at $(25, 100)$ is $\sqrt{2500} = 50$, the old level.

</div>

<div class="example" markdown>

### Example 5: a corner where the Lagrange method gives the wrong answer

A consumer has $U = 4\sqrt{x} + y$ (made up) with $p_x = p_y = \$1$. Find the best bundle for the incomes $m = 10$ and $m = 3$.

The conditions give $\frac{U_x}{U_y} = \frac{2/\sqrt{x}}{1} = \frac{p_x}{p_y} = 1$, so $\sqrt{x} = 2$ and $x = 4$, and the budget gives $y = m - 4$.

For $m = 10$, $y = 6$. The bundle $(4, 6)$ is interior, and $U = 8 + 6 = 14$. Good.

For $m = 3$, the method gives $y = -1$, which is impossible. The real answer is a corner: spend everything on $x$, so $(3, 0)$ with $U = 4\sqrt{3} \approx 6.93$. At the corner, the utility per dollar of $x$ is $\frac{U_x}{p_x} = \frac{2}{\sqrt{3}} \approx 1.155$, above $\frac{U_y}{p_y} = 1$, so the consumer would like to move spending from $y$ to $x$ but has no $y$ to give up.

Check: nearby affordable bundles are worse: $(2.5, 0.5)$ gives $4\sqrt{2.5} + 0.5 \approx 6.82$ and $(2, 1)$ gives $4\sqrt{2} + 1 \approx 6.66$, both below $6.93$.

For non-convex preferences, such as $U = x^2 + y^2$ with $p_x = p_y = 1$ and $m = 10$, the equations give $x = y = 5$ with $U = 50$, but the corner $(10, 0)$ gives $U = 100$. The tangency is the worst point on the line.

</div>

<div class="example" markdown>

### Example 6: expenditure minimization (finish it yourself)

A consumer has $U = xy$ with $p_x = \$4$ and $p_y = \$6$. Find the cheapest bundle that gives $U = 150$. The tangency condition is $\frac{y}{x} = \frac{4}{6}$.

Use it with the constraint to find the bundle and the expenditure, then compare with the budget problem for the income of \$120.

<details class="solution" markdown>
<summary>Finish</summary>

$y = \frac{2x}{3}$, and $xy = \frac{2x^2}{3} = 150$ gives $x^2 = 225$, so $x = 15$ and $y = 10$. The expenditure is $4 \cdot 15 + 6 \cdot 10 = 120$.

This is the dual of the lesson 4 problem (Example 5 there): with income \$120 the best bundle was $(15, 10)$ with $U = 150$. Spending the least to reach 150 costs \$120, and spending \$120 reaches at most 150.

Check: a different bundle with $U = 150$, such as $(10, 15)$, costs $40 + 90 = 130 > 120$, and $(20, 7.5)$ costs $80 + 45 = 125 > 120$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: reading $\lambda$ as an observable number. The multiplier depends on how the utility is labelled: in Example 2 it is 300 for $U = xy^2$ and $\frac{1}{30}$ for $\ln U$, for the same consumer making the same choices. The marginal utility of income has a meaning only together with the utility function you chose. Demand, shares and the MRS are the same for every labelling.

</div>

<div class="warning" markdown>

Watch out: using the Lagrange solution without checking the signs. If the method returns a negative $x$ or $y$, as in Example 5 with $m = 3$, the answer is invalid, and the best bundle is at a corner. Always read the solution back: are both quantities non-negative, and does the budget hold?

</div>

<div class="warning" markdown>

Watch out: assuming that the exponents have to add to 1. Theorem 1 holds for every positive $a$ and $b$, and the shares are $\frac{a}{a + b}$ and $\frac{b}{a + b}$. Writing the share of $x$ as $a$ gives the wrong answer for $U = x^{0.5}y^{1.5}$ (a share of 0.5 instead of 0.25).

</div>

<div class="warning" markdown>

Watch out: mixing up Marshallian and Hicksian demand. Marshallian demand holds income fixed, and utility changes with the price. Hicksian demand holds utility fixed, and the income needed changes. The two coincide only at the starting prices. The substitution effect is always measured along the Hicksian demand, and in Example 4 using the wrong one would give $12.5 - 50$ for the substitution effect and no income effect.

</div>

<div class="warning" markdown>

Watch out: applying the envelope theorem to the wrong constraint form. The formula $\frac{dV}{d\theta} = \frac{\partial\mathcal{L}}{\partial\theta}$ uses the Lagrangian $f - \lambda g$ with the constraint written as $g = 0$. If the constraint is $p_xx + p_yy = m$ then $g = p_xx + p_yy - m$, so $\frac{\partial g}{\partial m} = -1$ and $\frac{\partial V}{\partial m} = +\lambda$. Writing the constraint as $m - p_xx - p_yy$ flips the sign of the multiplier, so keep one convention throughout a problem.

</div>

Two edge cases are worth knowing. When the multiplier is zero, the constraint isn't binding: the consumer is satiated and would not spend more income even if they had it. And when the second-order condition fails (Example 5, non-convex), $\lambda$ and the bundle can be perfectly well defined and still describe a minimum.

## Tricks and shortcuts

For Cobb-Douglas utility skip the Lagrangian: the shares are $\frac{a}{a + b}$ and $\frac{b}{a + b}$ of income, and then $x^* = \frac{\text{share}\cdot m}{p_x}$. If you want $\lambda$ as well, $\lambda = \frac{U_x}{p_x}$ at the answer.

For the cost function of a Cobb-Douglas firm, find the cost of one unit of output, $C(1)$, and use $C(Q) = C(1)Q^{1/(\alpha + \beta)}$. For $\alpha + \beta = 1$ the whole cost function is $C(1)\,Q$ with $C(1) = \left(\frac{r}{\alpha}\right)^\alpha\left(\frac{w}{\beta}\right)^\beta$.

To split a price change, find the Hicksian demand at the new prices first (the cost of the old utility at the new prices is a useful number to compute), then subtract. The substitution effect is the first step, and the income effect is what is left.

To check any answer to a constrained problem, move along the constraint a little in each direction and confirm that the objective is lower. This catches both corners and minima.

## In code

Sympy solves the Cobb-Douglas problem with letters and confirms the envelope results. The numeric part computes the Slutsky split and the corner case, searching along the budget line.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import sympy as sp

x, y, lam = sp.symbols("x y lam", positive=True)
a, b, px, py, m = sp.symbols("a b p_x p_y m", positive=True)

# Cobb-Douglas with letters
U = x**a * y**b
L = U - lam * (px * x + py * y - m)
sol = sp.solve([sp.diff(L, x), sp.diff(L, y), px * x + py * y - m], [x, y, lam], dict=True)[0]
print(sp.simplify(sol[x]), sp.simplify(sol[y]))
# a*m/(p_x*(a + b)) b*m/(p_y*(a + b))

# Example 2: the envelope results for U = x y^2
V = sp.Rational(4, 27) * m**3 / (px * py**2)
at = {m: 90, px: 3, py: 2}
print(sp.diff(V, m).subs(at), sp.diff(V, px).subs(at), V.subs(at))
# 300 -3000 9000

# Example 4: Slutsky split for U = sqrt(xy), m = 100, p_y = 1, p_x from 1 to 4
x0 = 100 / (2 * 1)
x1 = 100 / (2 * 4)
u0 = np.sqrt(x0 * 50)
hx = u0 * np.sqrt(1 / 4)
print(x0, x1, hx, hx - x0, x1 - hx)
# 50.0 12.5 25.0 -25.0 -12.5

# Example 5: a search along the budget line shows the corner for m = 3
def best(m_):
    xs = np.linspace(0, m_, 300_001)
    u = 4 * np.sqrt(xs) + (m_ - xs)
    i = np.argmax(u)
    return round(float(xs[i]), 3), round(float(m_ - xs[i]), 3), round(float(u[i]), 3)

print(best(10))
print(best(3))
# (4.0, 6.0, 14.0)
# (3.0, 0.0, 6.928)
```

The search finds the interior answer when income is 10 and the corner when it is 3, which the equations of Example 5 would have missed.

</details>

## FAQ

### Why is the multiplier the marginal utility of income?

By the envelope theorem. The best utility is $V(m)$, and a dollar more of income relaxes the constraint by one dollar. The proof of Theorem 2 shows that the effect on $V$ is $\lambda$ per dollar, whatever the consumer does with it. A small change in how the money is spent has no first-order effect, because the consumer was already spending optimally.

### Why does the consumer spend a constant share of income with Cobb-Douglas utility?

The price effects cancel. When $p_x$ rises, the consumer buys less $x$, but each unit costs more, and for Cobb-Douglas these two effects exactly offset, so the spending $p_xx = \frac{a\,m}{a + b}$ doesn't change. Real data show shares that do move with prices, which is one reason economists look at other utility functions.

### Is the substitution effect always negative?

Yes: Hicksian demand slopes down in its own price, since the cheapest way to reach a utility level moves away from a good whose price has risen. The income effect can have either sign. For an inferior good (demand falls when income rises) the income effect is positive for a price rise, and if it is larger than the substitution effect the total is positive, a Giffen good, which is rare.

### Do I need the dual problem if I can solve the primal?

For most exam questions the primal gives all you need. The dual matters when the question is about compensation: how much extra income would make the consumer as well off after a price rise, or what a price change is worth in dollars. It also gives the cost function of a firm, since cost minimization is the dual problem of production.

## Practice

### Warm-up

1\. A consumer has $U = x^{0.3}y^{0.7}$, income \$100 and prices $p_x = \$5$ and $p_y = \$2$. Find the best bundle and write the utility to two decimals.

<details class="solution" markdown>
<summary>Solution</summary>

The shares are $0.3$ and $0.7$. Then $x = \frac{0.3 \cdot 100}{5} = 6$ and $y = \frac{0.7 \cdot 100}{2} = 35$. The utility is $6^{0.3}\cdot 35^{0.7} \approx 20.62$.

Check: the budget is $30 + 70 = 100$, and the tangency $\frac{U_x}{U_y} = \frac{0.3y}{0.7x} = \frac{0.3 \cdot 35}{0.7 \cdot 6} = 2.5 = \frac{5}{2}$.

</details>

2\. For $U = xy$ with income \$80 and prices $p_x = \$2$, $p_y = \$4$, find the best bundle, the utility and $\lambda$ from Theorem 1, and check $\lambda = \frac{U_x}{p_x}$.

<details class="solution" markdown>
<summary>Solution</summary>

With $a = b = 1$, $x = \frac{80}{2 \cdot 2} = 20$ and $y = \frac{80}{2 \cdot 4} = 10$. The utility is 200. Then $\lambda = \frac{(a + b)U}{m} = \frac{2 \cdot 200}{80} = 5$.

Check: $U_x = y = 10$, so $\frac{U_x}{p_x} = 5$, and $\frac{U_y}{p_y} = \frac{20}{4} = 5$.

</details>

3\. A consumer has $U = x^2y$. Write the demand for each good as a function of $p_x$, $p_y$ and $m$. What happens to the demand for $y$ when $p_x$ doubles?

<details class="solution" markdown>
<summary>Solution</summary>

With $a = 2$ and $b = 1$ the shares are $\frac{2}{3}$ and $\frac{1}{3}$, so $x = \frac{2m}{3p_x}$ and $y = \frac{m}{3p_y}$. The demand for $y$ doesn't depend on $p_x$, so it is unchanged when $p_x$ doubles. The demand for $x$ halves.

Check: the budget is $p_x\cdot\frac{2m}{3p_x} + p_y\cdot\frac{m}{3p_y} = \frac{2m}{3} + \frac{m}{3} = m$.

</details>

### Standard

4\. For $U = xy$ the indirect utility is $V = \frac{m^2}{4p_xp_y}$. At $m = 80$, $p_x = 2$, $p_y = 4$, verify the envelope theorem for $p_x$: compute $\frac{\partial V}{\partial p_x}$ and compare it with $-\lambda x^*$.

<details class="solution" markdown>
<summary>Solution</summary>

$V = \frac{6400}{32} = 200$. $\frac{\partial V}{\partial p_x} = -\frac{m^2}{4p_x^2p_y} = -\frac{V}{p_x} = -100$. From problem 2, $\lambda = 5$ and $x^* = 20$, so $-\lambda x^* = -100$.

Check: the two agree. Also $\frac{\partial V}{\partial m} = \frac{m}{2p_xp_y} = 5 = \lambda$.

</details>

5\. A firm has $Q = K^{1/3}L^{2/3}$ with $r = \$3$ and $w = \$4$. Find the cost-minimizing inputs for $Q = 10$, the total cost, and the cost function $C(Q)$.

<details class="solution" markdown>
<summary>Solution</summary>

The tangency is $\frac{\beta}{\alpha}\frac{K}{L} = \frac{2K}{L} = \frac{w}{r} = \frac{4}{3}$, so $K = \frac{2}{3}L$. The constraint is $K^{1/3}L^{2/3} = \left(\frac{2}{3}\right)^{1/3}L = Q$, so $L = 1.5^{1/3}Q \approx 1.1447Q$ and $K \approx 0.7631Q$. For $Q = 10$: $L \approx 11.45$ and $K \approx 7.63$. The cost is $3 \cdot 7.63 + 4 \cdot 11.45 \approx 68.68$. With constant returns, $C(Q) = 6.868Q$, exactly $324^{1/3}Q$.

Check: the formula $C = (\alpha + \beta)Q\left(\frac{r}{\alpha}\right)^\alpha\left(\frac{w}{\beta}\right)^\beta = Q \cdot 9^{1/3} \cdot 6^{2/3} = 324^{1/3}Q \approx 6.868Q$, and the output $7.63^{1/3} \cdot 11.45^{2/3} \approx 10.0$.

</details>

6\. A consumer has $U = \sqrt{xy}$, income \$120 and $p_y = \$1$. The price of $x$ rises from \$2 to \$8. Find the substitution and income effects on the demand for $x$.

<details class="solution" markdown>
<summary>Solution</summary>

Old: $x_0 = \frac{120}{2 \cdot 2} = 30$, $y_0 = 60$, $u_0 = \sqrt{1800} \approx 42.43$. New Marshallian demand: $x_1 = \frac{120}{2 \cdot 8} = 7.5$. Hicksian demand at $p_x = 8$: $h_x = u_0\sqrt{\frac{1}{8}} = 15$ (and $h_y = 120$, with a cost of $8 \cdot 15 + 120 = 240$). The substitution effect is $15 - 30 = -15$, the income effect is $7.5 - 15 = -7.5$, and the total is $-22.5$.

Check: $x_1 - x_0 = 7.5 - 30 = -22.5 = -15 - 7.5$. The compensated income \$240 would buy $\frac{240}{16} = 15 = h_x$.

</details>

### Challenge

7\. A consumer has $U = 4\sqrt{x} + y$ with $p_x = 1$ and $p_y = 2$. (a) Find the income at which the tangency bundle stops being feasible. (b) Find the demand for $x$ and $y$ for $m = 30$ and $m = 10$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The tangency is $\frac{2/\sqrt{x}}{1} = \frac{1}{2}$, so $\sqrt{x} = 4$ and $x = 16$. It costs $16$, so it is feasible with $y \ge 0$ exactly when $m \ge 16$.

(b) For $m = 30$: $x = 16$ and $y = \frac{30 - 16}{2} = 7$, with $U = 16 + 7 = 23$. For $m = 10$ the tangency would need $y < 0$, so the answer is the corner $x = 10$, $y = 0$, with $U = 4\sqrt{10} \approx 12.65$.

Check: at the corner, $\frac{U_x}{p_x} = \frac{2}{\sqrt{10}} \approx 0.632$ and $\frac{U_y}{p_y} = \frac{1}{2} = 0.5$: the consumer would put more into $x$ if they could. The bundle $(9, 0.5)$ costs $9 + 1 = 10$ and gives $12 + 0.5 = 12.5 < 12.65$.

</details>

8\. (Reviews [optimization](../../05-university-core/03-applications-of-derivatives/05-optimization.md).) Maximize $U = xy$ subject to $2x + 3y = 120$ by substituting for $y$ and using one-variable calculus. Then find $\lambda$ and check it against the Lagrange conditions.

<details class="solution" markdown>
<summary>Solution</summary>

From the budget, $y = \frac{120 - 2x}{3}$, so $U(x) = \frac{x(120 - 2x)}{3}$ and $U'(x) = \frac{120 - 4x}{3} = 0$ gives $x = 30$, $y = 20$ and $U = 600$. Also $U'' = -\frac{4}{3} < 0$, so it is a maximum.

The Lagrange conditions give $\lambda = \frac{U_x}{p_x} = \frac{y}{2} = 10$ and $\frac{U_y}{p_y} = \frac{x}{3} = 10$.

Check: Theorem 1 gives $\lambda = \frac{(a + b)U}{m} = \frac{2 \cdot 600}{120} = 10$, and the shares are one half each: $2 \cdot 30 = 60 = \frac{120}{2}$.

</details>

## Where this shows up

- This is the last lesson of the chapter, and the [chapter cheat sheet](index.md) collects its formulas. The rest of the economics folder uses other tools: [present value, NPV and bond prices](../04-more-tools/01-present-value-npv-and-bond-prices.md) and [game theory and Nash equilibrium](../04-more-tools/04-game-theory-and-nash-equilibrium.md), where best responses like the Cournot reaction functions come back.
- Economics: Marshallian demand is the demand curve of a first course, Hicksian demand is how welfare changes are measured in dollars (compensating and equivalent variation), and the Slutsky equation explains why a Giffen good is possible. The multiplier on a resource constraint is its shadow price.
- CS: support vector machines are trained by a constrained optimization whose multipliers pick out the support vectors, and the envelope theorem is the idea behind sensitivity analysis for linear programs, where the dual variables give the value of one more unit of a resource.
