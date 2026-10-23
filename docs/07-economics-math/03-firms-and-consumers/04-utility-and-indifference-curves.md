# Utility and indifference curves

After this lesson you can describe preferences with a utility function and indifference curves, prove that only the ranking of utility numbers matters, derive the marginal rate of substitution as a ratio of marginal utilities, draw a budget line, find the best bundle where the two touch, and recognize the cases (perfect substitutes and complements) where a tangency is the wrong answer.

Before this: [marginal analysis with derivatives](01-marginal-analysis-with-derivatives.md), [partial derivatives and the gradient](../../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md) and [chain rule, implicit and inverse derivatives](../../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For $U(x, y) = xy$, find the ratio $\frac{U_x}{U_y}$ at the bundle $(4, 9)$.
2. Goods $x$ and $y$ cost \$2 and \$4 and the income is \$40. Where does the budget line cross each axis, and what is its slope?
3. Does $V(x, y) = \ln x + \ln y$ rank bundles the same way as $U(x, y) = xy$ for $x, y > 0$? Why?

<details class="solution" markdown>
<summary>Answers</summary>

1. $U_x = y = 9$ and $U_y = x = 4$, so the ratio is $\frac{9}{4} = 2.25$.
2. It crosses the $x$-axis at $\frac{40}{2} = 20$ and the $y$-axis at $\frac{40}{4} = 10$, with slope $-\frac{2}{4} = -\frac{1}{2}$.
3. Yes. $V = \ln U$, and the logarithm is strictly increasing, so a bundle has the higher $V$ exactly when it has the higher $U$. For example $(2, 8)$ has $U = 16$ and $(4, 3)$ has $U = 12$, and $\ln 16 > \ln 12$ too.

</details>

## The idea

Ask someone whether they prefer a bundle of 3 restaurant meals and 10 streaming-hours a month to 5 meals and 4 hours, and they can usually answer. Ask them to say how many "units of happiness" each gives, and the question is odd. Economists build on the first kind of statement. Preferences are rankings of bundles, and a utility function is a convenient way to write a ranking: a number for each bundle, with a higher number for a bundle that is better.

Because only the ranking matters, many different formulas describe the same person. This is not a nuisance. It tells you what in the model is real (the shape of the indifference curves, the trade-off rate) and what is a choice of units (the size of the utility numbers). The trade-off rate is the marginal rate of substitution, the number of $y$ a person will give up for one more $x$ and stay equally happy. It comes out as a ratio of marginal utilities, and the ratio doesn't change if you relabel the utility numbers.

The consumer's problem then has a picture. The budget line shows which bundles are affordable, the indifference curves show which are equally good, and the best affordable bundle is where an indifference curve just touches the budget line. In the usual case that point is a tangency, so the slopes match: the trade-off rate in the person's head equals the trade-off rate in the shops. The cases in the last section show that the tangency rule has exceptions.

## Definitions

A **bundle** is a pair $(x, y)$ of quantities of two goods, each at least 0. A consumer's preferences are a ranking of bundles, written $A \succsim B$ for "$A$ is at least as good as $B$". They are **complete** if for every two bundles one of $A \succsim B$ or $B \succsim A$ holds, and **transitive** if $A \succsim B$ and $B \succsim C$ imply $A \succsim C$. They are **monotone** if a bundle with more of one good and no less of the other is strictly better.

A **utility function** $U(x, y)$ represents the preferences if $U(A) \ge U(B)$ exactly when $A \succsim B$. The numbers have only an ordering meaning (the utility is **ordinal**): a bundle with $U = 20$ is better than one with $U = 10$, but not "twice as good". The **marginal utility** of $x$ is $U_x = \frac{\partial U}{\partial x}$, and of $y$ is $U_y$. In plain words, it is the extra utility from a little more of that good, with the other held fixed.

An **indifference curve** is a level curve $U(x, y) = \bar{u}$, the set of bundles that are equally good. The **marginal rate of substitution** (MRS) is the amount of $y$ the consumer gives up for one more unit of $x$ along an indifference curve:

$$
MRS = -\frac{dy}{dx}\bigg|_{U \text{ fixed}}.
$$

In plain words, it is the slope of the indifference curve, made positive. Preferences are **convex** if averages of equally good bundles are at least as good: for $A \sim B$ and $0 < t < 1$, the bundle $tA + (1 - t)B$ is at least as good. On a graph, the set of bundles at least as good as a given one lies on or above its indifference curve and has no dent in it.

Given the prices $p_x$ and $p_y$ and the income $m$, the **budget line** is $p_xx + p_yy = m$ and the **budget set** is the bundles with $p_xx + p_yy \le m$. Two goods are **perfect substitutes** if the consumer is willing to swap them at a constant rate, as in $U = ax + by$. They are **perfect complements** if they are used together in a fixed ratio, as in $U = \min(x, y)$: a left shoe is worth nothing without a right shoe.

## How to do it

### Ordinal utility

*Theorem 1.* Let $U$ represent preferences and let $g$ be a strictly increasing function. Then $V(x, y) = g\bigl(U(x, y)\bigr)$ represents the same preferences. In particular, for every set of bundles that can be chosen from, $V$ and $U$ have the same best bundles.

What we know: $g$ is strictly increasing, so $a < b$ implies $g(a) < g(b)$. What we want: $V(A) \ge V(B)$ exactly when $U(A) \ge U(B)$. The plan is to prove each direction, using the contrapositive for the second.

*Proof.* If $U(A) \ge U(B)$ then $g(U(A)) \ge g(U(B))$, because $g$ doesn't decrease anywhere, so $V(A) \ge V(B)$. Conversely, suppose $U(A) < U(B)$. Then $g(U(A)) < g(U(B))$, so $V(A) < V(B)$. Taking the contrapositive, $V(A) \ge V(B)$ implies $U(A) \ge U(B)$. So the two functions order every pair of bundles in the same way. A best bundle in a set is one that no other bundle in the set beats, and that depends only on the ordering. $\blacksquare$

Look back: the proof is a statement that relabelling doesn't change a ranking, as when you change a class's marks from out of 50 to out of 100. This is why $xy$, $\ln x + \ln y$ and $(xy)^2$ all describe one consumer for $x, y > 0$. The proof also says what can't be read off a utility function: the differences between utility numbers. Whether going from 10 to 20 "is bigger" than going from 20 to 25 depends on the label $g$.

### The marginal rate of substitution

*Theorem 2.* If $U$ has continuous partial derivatives with $U_y \ne 0$, then along an indifference curve

$$
MRS = \frac{U_x}{U_y}.
$$

If $V = g(U)$ with $g' > 0$, the ratio computed from $V$ is the same.

What we know: along the curve $U(x, y) = \bar{u}$, with $y$ a function of $x$, the value of $U$ stays constant. What we want: $-\frac{dy}{dx}$. The plan is implicit differentiation, as in the earlier lesson.

*Proof.* Differentiate $U\bigl(x, y(x)\bigr) = \bar{u}$ with respect to $x$ using the chain rule: $U_x + U_y\frac{dy}{dx} = 0$. Solving, $\frac{dy}{dx} = -\frac{U_x}{U_y}$, so $MRS = \frac{U_x}{U_y}$. For $V = g(U)$, the chain rule gives $V_x = g'(U)\,U_x$ and $V_y = g'(U)\,U_y$, so $\frac{V_x}{V_y} = \frac{g'(U)\,U_x}{g'(U)\,U_y} = \frac{U_x}{U_y}$, since $g'(U) > 0$ cancels. $\blacksquare$

Look back: the first part says, in words, that to stay on the same level you must give up utility $U_y$ per unit of $y$ to make up for gaining $U_x$ per unit of $x$, so one unit of $x$ buys $\frac{U_x}{U_y}$ units of $y$. The second part is Theorem 1 at work on slopes: the marginal utilities themselves change under relabelling, but their ratio doesn't.

### Diminishing MRS and convexity

For most preferences the MRS falls as you move along an indifference curve towards more $x$. The consumer with many meals and few hours of streaming will give up several meals for one more hour, and the consumer with few meals will give up few. That is the case where the curves bow towards the origin.

*Theorem 3.* For $U = x^ay^b$ with $a, b > 0$ and $x, y > 0$, the indifference curve $U = \bar{u}$ is the graph of $y = \bar{u}^{1/b}x^{-a/b}$, with $MRS = \frac{a}{b}\cdot\frac{y}{x}$. The MRS falls as $x$ rises along the curve, and the curve is convex ($y'' > 0$).

*Proof.* From $x^ay^b = \bar{u}$ we get $y = \bar{u}^{1/b}x^{-a/b}$. Then $y' = -\frac{a}{b}\bar{u}^{1/b}x^{-a/b - 1} < 0$ and $y'' = \frac{a}{b}\left(\frac{a}{b} + 1\right)\bar{u}^{1/b}x^{-a/b - 2} > 0$, so the curve falls and is convex. By Theorem 2, $MRS = \frac{ax^{a-1}y^b}{bx^ay^{b-1}} = \frac{a}{b}\cdot\frac{y}{x}$. Along the curve $y$ falls and $x$ rises, so $\frac{y}{x}$ falls and so does the MRS. $\blacksquare$

Look back: convexity of the curves is about the MRS falling, which is an ordinal property. It is not the same as diminishing marginal utility. The function $V = (xy)^2$ has increasing marginal utilities in $x$ (since $V_x = 2xy^2$ grows with $x$) and exactly the same indifference curves, which are convex. So diminishing marginal utility is not needed for convex indifference curves.

### The budget line and the tangency

The budget line $p_xx + p_yy = m$ solves to $y = \frac{m}{p_y} - \frac{p_x}{p_y}x$: it has the intercepts $\frac{m}{p_x}$ and $\frac{m}{p_y}$ and the slope $-\frac{p_x}{p_y}$. Raising income moves the line out in parallel. Raising the price of $x$ swings the line in around the $y$-intercept.

*Theorem 4.* Suppose $U$ is differentiable with $U_x, U_y > 0$, and a bundle $(x^*, y^*)$ with $x^*, y^* > 0$ maximizes $U$ on the budget line. Then

$$
\frac{U_x}{U_y} = \frac{p_x}{p_y}, \qquad\text{that is,}\qquad MRS = \frac{p_x}{p_y}.
$$

What we know: the consumer can move along the budget line, changing $x$ by $dx$ and $y$ by $dy$ with $p_x\,dx + p_y\,dy = 0$. What we want: the condition under which no such move helps. The plan is to compute the change in utility along the line and see when it is zero.

*Proof.* On the budget line, $dy = -\frac{p_x}{p_y}dx$. A small move changes utility by $dU = U_x\,dx + U_y\,dy = U_x\,dx - U_y\frac{p_x}{p_y}dx = U_y\left(\frac{U_x}{U_y} - \frac{p_x}{p_y}\right)dx$. If $MRS > \frac{p_x}{p_y}$, then raising $x$ ($dx > 0$) makes $dU > 0$, and if $MRS < \frac{p_x}{p_y}$, then lowering $x$ does, so neither can hold at a maximum. Hence $MRS = \frac{p_x}{p_y}$. $\blacksquare$

Look back at the meaning. The MRS is the rate at which the consumer is willing to swap $y$ for $x$, and the price ratio is the rate at which the market lets them. If the consumer would give up 2 units of $y$ for one $x$ but the market asks only 1.5, they gain by buying $x$. They stop when the two rates agree. The condition is necessary; with convex preferences (as in Theorem 3) it is also sufficient, and the point is the global best. With two unknowns, the tangency condition and the budget equation are two equations that give the bundle.

### Where the tangency fails

If $U = ax + by$ with $a, b > 0$, the MRS is the constant $\frac{a}{b}$ and the indifference curves are straight lines. The computation of $dU$ above gives $dU = U_y\left(\frac{a}{b} - \frac{p_x}{p_y}\right)dx$ with a sign that does not depend on the bundle. So if $\frac{a}{b} > \frac{p_x}{p_y}$ the consumer buys only $x$, if $\frac{a}{b} < \frac{p_x}{p_y}$ only $y$, and if the two are equal every bundle on the budget line is best. The answer is a corner, and the tangency condition has no solution with both goods positive.

For $U = \min(x, y)$ the indifference curves are right angles with the kink on the line $y = x$, and there is no MRS at the kink. If a bundle has $x > y$, some of the $x$ adds nothing, and the money spent on it could buy more of both goods. So the best bundle has $x = y$, and with the budget it gives $x = y = \frac{m}{p_x + p_y}$.

## Worked examples

<div class="example" markdown>

### Example 1: the MRS along an indifference curve

A consumer has $U(x, y) = xy$, where $x$ is restaurant meals and $y$ is hours of streaming in a month (made up). Find the MRS at several bundles on the indifference curve $U = 36$, and show that relabelling doesn't change it.

Step 1: the curve is $y = \frac{36}{x}$, and $U_x = y$, $U_y = x$, so by Theorem 2 the MRS is $\frac{y}{x}$. (This is Theorem 3 with $a = b = 1$.)

Step 2: at the bundles on the curve:

| Bundle $(x, y)$ | $U$ | MRS $= \frac{y}{x}$ |
|---|---|---|
| $(4, 9)$ | 36 | $\frac{9}{4} = 2.25$ |
| $(6, 6)$ | 36 | $1$ |
| $(9, 4)$ | 36 | $\frac{4}{9} \approx 0.44$ |

Step 3: moving towards more $x$, the MRS falls from 2.25 to 0.44. The consumer with 4 meals would give up 2.25 hours of streaming for one more meal, and the one with 9 meals would give up only 0.44 hours.

Step 4: relabel. For $V = \ln x + \ln y$, $V_x = \frac{1}{x}$ and $V_y = \frac{1}{y}$, so $\frac{V_x}{V_y} = \frac{y}{x}$. For $W = (xy)^2$, $W_x = 2xy^2$ and $W_y = 2x^2y$, so $\frac{W_x}{W_y} = \frac{y}{x}$. The same.

Check: the slope of $y = \frac{36}{x}$ is $-\frac{36}{x^2}$, which at $x = 4$ is $-2.25$ and at $x = 9$ is $-0.44$. The negatives of these are the MRS values.

</div>

<div class="example" markdown>

### Example 2: the best bundle with a tangency

A consumer has $U = xy^2$ (made up), prices $p_x = \$3$ and $p_y = \$2$, and an income of \$90. Find the best bundle.

Step 1: the budget line is $3x + 2y = 90$, with intercepts 30 and 45.

Step 2: the MRS is $\frac{U_x}{U_y} = \frac{y^2}{2xy} = \frac{y}{2x}$, and the price ratio is $\frac{3}{2}$.

Step 3: set them equal: $\frac{y}{2x} = \frac{3}{2}$, so $y = 3x$.

Step 4: put this into the budget: $3x + 2(3x) = 9x = 90$, so $x = 10$ and $y = 30$. The utility is $U = 10 \cdot 900 = 9000$.

The first panel of the figure shows the tangency. The consumer spends $3 \cdot 10 = 30$ dollars on $x$, which is one third of the income, and \$60 on $y$, two thirds. These are the shares $\frac{a}{a + b} = \frac{1}{3}$ and $\frac{b}{a + b} = \frac{2}{3}$ for $U = x^ay^b$ with $a = 1$ and $b = 2$, which lesson 5 proves in general.

![Three panels. Left: the budget line 3x plus 2y equals 90 and three indifference curves for U equal to 6000, 9000 and 12000; the middle curve touches the budget line at the bundle (10, 30), marked as the best bundle, with the lower curve inside the budget set and the upper curve out of reach. Middle: perfect substitutes with U equal to x plus 2y and the budget line x plus 3y equals 60; the indifference curves are parallel straight lines flatter than the budget line, and the best bundle is the corner (60, 0). Right: perfect complements with U equal to the minimum of x and y; the indifference curves are right angles with corners on the line y equals x, and the budget line 4x plus 2y equals 60 passes through the kink (10, 10).](../../assets/figures/07-economics-math/utility-and-indifference-curves-three-cases.svg)

Check: the budget holds, $30 + 60 = 90$. Other affordable bundles do worse: $(12, 27)$ gives $12 \cdot 729 = 8748$, $(8, 33)$ gives $8 \cdot 1089 = 8712$, and $(9, 31.5)$ gives $8930.25$. A fine search along the line finds the maximum at $(10, 30)$.

</div>

<div class="example" markdown>

### Example 3: perfect substitutes and a corner

A consumer treats two brands of tea as perfect substitutes, with $U = x + 2y$ (made up): one box of $y$ is worth two boxes of $x$. Prices are $p_x = \$1$ and $p_y = \$3$, and the income is \$60. What do they buy, and what changes if $p_y$ falls?

The MRS is $\frac{U_x}{U_y} = \frac{1}{2}$ everywhere, while the price ratio is $\frac{1}{3}$. Since $MRS > \frac{p_x}{p_y}$, good $x$ is the better buy: it gives $1$ unit of utility per dollar, against $\frac{2}{3}$ for $y$. The consumer spends everything on $x$ and buys the corner $(60, 0)$ with $U = 60$.

If instead they bought only $y$ they would get $(0, 20)$ and $U = 40$, and a mix such as $(30, 10)$ gives $30 + 20 = 50$. The best bundle is the corner.

If $p_y$ falls to \$2, then the price ratio is $\frac{1}{2}$, equal to the MRS. Now every bundle on the line $x + 2y = 60$ gives $U = 60$, and the consumer is indifferent among them. If $p_y$ falls to \$1.50 the ratio is $\frac{2}{3}$, which is above $\frac{1}{2}$, so only $y$ is bought: $y = 40$ and $U = 80$, against $60$ for the corner of $x$.

Check: the best choice follows the cheaper source of utility per dollar. At $p_y = 1.50$, $y$ gives $\frac{2}{1.5} = 1.33$ per dollar against 1 for $x$, so $y$ wins. The demand for each good jumps from 0 to everything as the price crosses the threshold $p_y = 2$, which differs from the smooth change in Example 2.

</div>

<div class="example" markdown>

### Example 4: perfect complements

A consumer uses laptops and chargers in the ratio 1 to 1, with $U = \min(x, y)$ (made up). The prices are $p_x = \$4$ and $p_y = \$2$, and the income is \$60. How much of each do they buy, and what happens if the price of $y$ doubles?

There is no point in a bundle with $x \ne y$, so the choice is on the line $y = x$. Then $4x + 2x = 6x = 60$ and $x = y = 10$, with $U = 10$. One "package" of a laptop and a charger costs $p_x + p_y = 6$ dollars, and the income buys $\frac{60}{6} = 10$ of them.

If $p_y$ doubles to \$4, a package costs \$8 and the consumer buys $\frac{60}{8} = 7.5$ of each. The price of $y$ changed the demand for $x$, which wasn't so in Example 2 (there the demand for $x$ was $\frac{m}{3p_x}$, independent of $p_y$). If instead $p_x$ falls to \$2, a package costs \$4 and the consumer buys 15 of each.

Check: $4 \cdot 10 + 2 \cdot 10 = 60$. A nearby bundle such as $(12, 6)$ costs $48 + 12 = 60$ and gives $\min(12, 6) = 6 < 10$, and $(8, 14)$ costs $32 + 28 = 60$ and gives $8 < 10$. The kink is the best point, though no line is tangent there.

</div>

<div class="example" markdown>

### Example 5: tangency with other prices (finish it yourself)

A consumer with $U = xy$ has income \$120 and the prices $p_x = \$4$ and $p_y = \$6$. The budget line has intercepts 30 and 20. The MRS is $\frac{y}{x}$ and the price ratio is $\frac{4}{6} = \frac{2}{3}$.

Set them equal and use the budget to find the best bundle and its utility. What share of income goes to each good?

<details class="solution" markdown>
<summary>Finish</summary>

$\frac{y}{x} = \frac{2}{3}$ gives $y = \frac{2x}{3}$. The budget $4x + 6y = 4x + 4x = 8x = 120$ gives $x = 15$ and $y = 10$. The utility is $U = 150$. The spending is $4 \cdot 15 = 60$ on $x$ and $6 \cdot 10 = 60$ on $y$: half of the income on each, as for $U = x^{0.5}y^{0.5}$.

Check: $60 + 60 = 120$, and the neighbours $(18, 8)$ and $(12, 12)$ also cost $72 + 48 = 120$ and $48 + 72 = 120$ and give $144$ and $144$, both below 150.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: reading utility numbers as amounts of happiness. A utility of 20 against 10 says the first bundle is better, not that it is twice as good, and the choices don't change if you replace $U$ with $U^2$ or $\ln U$. Any question whose answer changes under a relabelling, such as "is the third unit worth twice the second?", can't be answered from ordinal preferences.

</div>

<div class="warning" markdown>

Watch out: inverting the MRS. The MRS of $x$ for $y$ is $\frac{U_x}{U_y}$, with the marginal utility of the good on the horizontal axis on top. The tangency is $\frac{U_x}{U_y} = \frac{p_x}{p_y}$, the same order on both sides. Writing $\frac{U_x}{U_y} = \frac{p_y}{p_x}$ gives the wrong bundle, and a quick check is that you should buy more of the good with the lower price.

</div>

<div class="warning" markdown>

Watch out: using the tangency when the preferences have a corner or a kink. For $U = x + 2y$ and $U = \min(x, y)$ there is no solution of $MRS = \frac{p_x}{p_y}$ with the best bundle. Check the shape of the indifference curves first: a straight line means a corner or an indifferent line, a right angle means the kink.

</div>

<div class="warning" markdown>

Watch out: confusing diminishing marginal utility with a diminishing MRS. The MRS falls along an indifference curve for the convex preferences of Theorem 3, whether or not each marginal utility falls. The statement "the more meals I have, the less I value another" is about $U_x$, and the statement about curves is about $\frac{U_x}{U_y}$.

</div>

<div class="warning" markdown>

Watch out: a tangency that is the worst point instead of the best. If the indifference curves bow away from the origin (non-convex preferences, as for $U = x^2 + y^2$), the point where a curve touches the budget line is a minimum along the line, and the best bundle is at a corner. Theorem 4 gives a necessary condition. Check the shape or compare utilities at the corners.

</div>

Two edge cases come up. If the budget line has a good that costs nothing, the budget set is unbounded, and "buy the most" has no answer: the model assumes all prices are positive. And if the preferences aren't monotone (a good that is bad, such as noise, or a bundle that is too much of a good thing), then spending the whole income is not always best, and the budget line is not the constraint to use.

## Tricks and shortcuts

For $U = x^ay^b$, write the MRS at once: $\frac{a}{b}\cdot\frac{y}{x}$. The tangency gives $y = \frac{b}{a}\cdot\frac{p_x}{p_y}x$, and the answer is fixed shares of income: $\frac{a}{a + b}$ on $x$ and $\frac{b}{a + b}$ on $y$ (Example 2, shares one third and two thirds).

To compare utility per dollar, divide each marginal utility by its price. For linear utility, the larger ratio wins everything. The tangency condition is the same statement for smooth curves: $\frac{U_x}{p_x} = \frac{U_y}{p_y}$.

For perfect complements, think in packages. The package costs the sum of the prices, and the consumer buys $\frac{m}{p_x + p_y}$ of them. For $\min(x, 2y)$ a package is two units of $x$ with one of $y$, costing $2p_x + p_y$.

To check that a tangency is a maximum and not a minimum, evaluate utility on two bundles on the budget line on either side of it, as in the check of Example 2.

## In code

Sympy checks that the MRS doesn't change under relabelling, solves the tangency of Example 2, and a grid search along the budget line confirms the best bundle for each of the three cases.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
import sympy as sp

x, y = sp.symbols("x y", positive=True)

# The MRS is the same for U, ln U and U squared
for V in (x * y, sp.log(x * y), (x * y) ** 2):
    print(sp.simplify(sp.diff(V, x) / sp.diff(V, y)))
# y/x
# y/x
# y/x

# Example 2: U = x y^2 with 3x + 2y = 90
U = x * y**2
mrs = sp.simplify(sp.diff(U, x) / sp.diff(U, y))
sol = sp.solve([sp.Eq(mrs, sp.Rational(3, 2)), sp.Eq(3 * x + 2 * y, 90)], [x, y])
print(sol, U.subs(sol))
# {x: 10, y: 30} 9000

# A search along each budget line
def best(u, px, py, m):
    xs = np.linspace(0, m / px, 600_001)
    ys = (m - px * xs) / py
    i = np.argmax(u(xs, ys))
    return round(float(xs[i]), 2), round(float(ys[i]), 2)

print(best(lambda a, b: a * b**2, 3, 2, 90))
# (10.0, 30.0)
print(best(lambda a, b: a + 2 * b, 1, 3, 60))
# (60.0, 0.0)
print(best(lambda a, b: np.minimum(a, b), 4, 2, 60))
# (10.0, 10.0)
```

The search finds the same bundles as the algebra, including the corner for substitutes and the kink for complements. The derivative method would find only the first.

</details>

## FAQ

### Why is ordinal utility enough?

Because choices depend only on which bundle ranks higher, and a ranking is all the choices reveal. Theorem 1 shows that nothing in the choices changes when the utility is relabelled, so the extra content of cardinal numbers (how much better) would be a claim that no observed choice could check. Ordinal utility makes fewer assumptions and gives the same demand curves.

### Can I compare my utility with someone else's?

Not with this model. The numbers have meaning only within one person's ranking, and two people's utility numbers have no common scale. That is why welfare questions are phrased in money (surplus) or in terms of everybody being better off, and not by adding up utilities.

### Why must indifference curves be convex?

They need not be, but convex curves are the standard case because they mean that people like variety: a mix of two bundles is at least as good as either. Convexity also ensures that the tangency is the best point and that demand responds smoothly to prices. Non-convex preferences give corners and jumps in demand.

### What if more is not better?

Then the monotone assumption fails, and the solution changes. If a good is a "bad" (pollution, noise), the indifference curves slope upward. If the consumer has a favourite bundle (a bliss point), indifference curves are closed loops around it, and they might not spend all of their income. The budget line is the constraint only when the consumer wants more.

## Practice

### Warm-up

1\. For $U = x^2y$, find $U_x$, $U_y$ and the MRS at $(3, 4)$.

<details class="solution" markdown>
<summary>Solution</summary>

$U_x = 2xy = 24$ and $U_y = x^2 = 9$ at $(3, 4)$. The MRS is $\frac{24}{9} = \frac{8}{3} \approx 2.67$. In general $MRS = \frac{2xy}{x^2} = \frac{2y}{x}$, which is $\frac{8}{3}$ at $(3, 4)$.

Check: this is Theorem 3 with $a = 2$, $b = 1$, giving $\frac{a}{b}\cdot\frac{y}{x} = \frac{2 \cdot 4}{3}$.

</details>

2\. Prices are $p_x = \$5$ and $p_y = \$10$, and income is \$100. Where does the budget line cross the axes, what is its slope, and which of $(10, 5)$, $(12, 4)$ and $(8, 7)$ are affordable and on the line?

<details class="solution" markdown>
<summary>Solution</summary>

The intercepts are $\frac{100}{5} = 20$ and $\frac{100}{10} = 10$, and the slope is $-\frac{5}{10} = -\frac{1}{2}$. The costs are $5 \cdot 10 + 10 \cdot 5 = 100$, $5 \cdot 12 + 10 \cdot 4 = 100$ and $5 \cdot 8 + 10 \cdot 7 = 110$. So $(10, 5)$ and $(12, 4)$ are affordable and on the line, and $(8, 7)$ is not affordable.

Check: moving from $(10, 5)$ to $(12, 4)$ gives up 1 unit of $y$ for 2 more units of $x$, which is the slope $-\frac{1}{2}$.

</details>

3\. Which of these represent the same preferences as $U = xy$ on $x, y > 0$? (a) $x^2y^2$, (b) $x + y$, (c) $3xy + 7$, (d) $-\frac{1}{xy}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $x^2y^2 = U^2$, and squaring is increasing for $U > 0$: yes. (c) $3U + 7$ is an increasing function of $U$: yes. (d) $-\frac{1}{U}$ is increasing for $U > 0$: yes. (b) $x + y$ is not a function of $U$ alone: $(1, 9)$ has $U = 9$ and $(4, 4)$ has $U = 16$, so $(4, 4)$ is preferred under $U$, but $x + y$ is 10 for the first and 8 for the second, which reverses the ranking. So no.

Check: a single counterexample is enough to rule out (b), and Theorem 1 covers the others.

</details>

### Standard

4\. A consumer has $U = x^{0.5}y^{0.5}$, prices $p_x = \$1$, $p_y = \$4$ and income \$80. Find the best bundle and the utility, and check the tangency.

<details class="solution" markdown>
<summary>Solution</summary>

$MRS = \frac{y}{x}$ and the price ratio is $\frac{1}{4}$, so $y = \frac{x}{4}$, or $x = 4y$. The budget $x + 4y = 4y + 4y = 8y = 80$ gives $y = 10$ and $x = 40$. The utility is $\sqrt{400} = 20$.

Check: $\frac{y}{x} = \frac{10}{40} = \frac{1}{4} = \frac{p_x}{p_y}$, and $40 + 40 = 80$. Half the income goes to each good, as for equal exponents.

</details>

5\. A consumer has $U = 3x + y$ and income \$30, with $p_y = \$1$. Find the best bundle when $p_x = \$2$, and the price of $x$ at which the choice switches.

<details class="solution" markdown>
<summary>Solution</summary>

The MRS is $\frac{3}{1} = 3$ and the price ratio is $2$. Since $3 > 2$ the consumer buys only $x$: $x = 15$, $y = 0$, $U = 45$. The alternative, only $y$, gives $U = 30$. The choice switches where the price ratio equals 3, at $p_x = \$3$. There the two goods give the same utility per dollar, and every bundle on the budget line gives $U = 30$. Above \$3 the consumer buys only $y$.

Check: at $p_x = 3$, the all-$x$ bundle is $x = 10$ with $U = 30$, equal to the all-$y$ bundle's 30. At $p_x = 4$, all $x$ gives $U = 3 \cdot 7.5 = 22.5 < 30$.

</details>

6\. A consumer has $U = \min(x, 2y)$, prices $p_x = \$3$ and $p_y = \$6$ and income \$120. Find the best bundle.

<details class="solution" markdown>
<summary>Solution</summary>

The best bundle has $x = 2y$. Then $3(2y) + 6y = 12y = 120$ gives $y = 10$ and $x = 20$, with $U = \min(20, 20) = 20$.

Check: $3 \cdot 20 + 6 \cdot 10 = 120$. A package of two $x$ and one $y$ costs \$12, so \$120 buys 10 packages. The bundle $(24, 8)$ costs $72 + 48 = 120$ and gives $\min(24, 16) = 16 < 20$.

</details>

### Challenge

7\. For the quasi-linear utility $U = \sqrt{x} + y$ (with $x, y \ge 0$), (a) show that the indifference curve $\sqrt{x} + y = \bar{u}$ is convex and find the MRS; (b) with $p_x = p_y = 1$ and income 10, find the tangency bundle and check that it is affordable with $y > 0$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The curve is $y = \bar{u} - \sqrt{x}$, with $y' = -\frac{1}{2\sqrt{x}}$ and $y'' = \frac{1}{4}x^{-3/2} > 0$, so it is convex. The MRS is $\frac{U_x}{U_y} = \frac{1/(2\sqrt{x})}{1} = \frac{1}{2\sqrt{x}}$, which falls as $x$ rises.

(b) The tangency $\frac{1}{2\sqrt{x}} = \frac{p_x}{p_y} = 1$ gives $\sqrt{x} = \frac{1}{2}$ and $x = \frac{1}{4}$. Then the budget gives $y = 10 - 0.25 = 9.75$, which is positive, so the solution is interior. The utility is $0.5 + 9.75 = 10.25$.

Check: the demand for $x$ doesn't depend on income as long as $y > 0$, since $x = \frac{1}{4}$ for any income above 0.25. If the income were 0.2 the tangency would need $y = -0.05$, which is impossible, and the answer would be the corner $(0.2, 0)$. Lesson 5 returns to this.

</details>

8\. (Reviews [chain rule, implicit and inverse derivatives](../../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md).) The indifference curve of $U = xy^2$ through $(1, 6)$ is $xy^2 = 36$. Find $\frac{dy}{dx}$ at $(1, 6)$ by implicit differentiation, and compare it with $-\frac{U_x}{U_y}$.

<details class="solution" markdown>
<summary>Solution</summary>

Differentiating $xy^2 = 36$ with respect to $x$: $y^2 + 2xy\frac{dy}{dx} = 0$, so $\frac{dy}{dx} = -\frac{y}{2x} = -\frac{6}{2} = -3$. The ratio is $\frac{U_x}{U_y} = \frac{y^2}{2xy} = \frac{y}{2x} = 3$, so $-\frac{U_x}{U_y} = -3$.

Check: solving for $y = \frac{6}{\sqrt{x}}$ gives $y' = -\frac{3}{x^{3/2}} = -3$ at $x = 1$.

</details>

## Where this shows up

- The next lesson, [Lagrange multipliers, utility and cost minimization](05-lagrange-multipliers-utility-and-cost-minimization.md), solves the tangency problem in general with a multiplier, finds the demand functions and handles the corners. The convex isoquants of [production and cost functions](02-production-and-cost-functions.md) have the same shape as the indifference curves here.
- Economics: demand curves, income and substitution effects, and consumer surplus are all built from the consumer's best bundle. Choices under risk use expected utility, where the shape of $U$ matters beyond its ranking, and a concave $U$ means risk aversion.
- CS: ranking and recommendation systems often learn a score per item that is used only to order the items, which is ordinal in the sense of Theorem 1: any increasing transformation of the scores gives the same ranking.
