# Absolute value equations and inequalities

After this lesson you can solve equations and inequalities that have the variable inside absolute value bars, write the answers as points, intervals or unions of intervals, handle the cases where the other side is zero or negative, reject extraneous solutions, and turn a tolerance such as $25 \pm 0.05$ mm into an inequality.

Before this: [negative numbers and absolute value](../../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md) and [compound inequalities and interval notation](03-compound-inequalities-and-interval-notation.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $\lvert 2x - 3 \rvert = 7$.
2. Write the solution set of $\lvert x - 4 \rvert < 3$ as an interval.
3. Solve $\lvert 3x + 1 \rvert \ge 8$ and write the answer in interval notation.

<details class="solution" markdown>
<summary>Answers</summary>

1. $x = 5$ or $x = -2$. Solve $2x - 3 = 7$ and $2x - 3 = -7$. Check: $\lvert 7 \rvert = 7$ and $\lvert -7 \rvert = 7$.
2. $(1, 7)$. The numbers within 3 of 4 are the ones between $4 - 3 = 1$ and $4 + 3 = 7$.
3. $(-\infty, -3] \cup \left[\frac{7}{3}, \infty\right)$. The cases are $3x + 1 \ge 8$, which gives $x \ge \frac{7}{3}$, and $3x + 1 \le -8$, which gives $x \le -3$.

</details>

## The idea

A shaft is machined to a length of $25 \pm 0.05$ mm. The part passes inspection if its length $L$ is within 0.05 mm of 25, in either direction. "Within 0.05 of 25" says that the distance from $L$ to 25 is at most 0.05, and from [negative numbers and absolute value](../../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md) that distance is $\lvert L - 25 \rvert$. So the test is

$$
\lvert L - 25 \rvert \le 0.05.
$$

The same shape appears in economics. As of 2026, the Bank of Canada aims to keep inflation at the 2% midpoint of a control range of 1% to 3% (source: the Bank of Canada's page on [inflation](https://www.bankofcanada.ca/core-functions/monetary-policy/inflation/), which says the framework is up for renewal in 2026). An inflation rate $i$, in percent, is inside the range when $\lvert i - 2 \rvert \le 1$.

A picture explains the whole lesson. Take the centre 3 and the distance 2. The numbers at distance exactly 2 from 3 are the two points 1 and 5. The numbers closer than 2 fill the stretch between them. The numbers farther than 2 are the two rays outside:

![Three number lines from 0 to 6. The first marks closed dots at 1 and 5 for absolute value of x minus 3 equals 2, with arrows showing that each is a distance of 2 from the centre 3. The second shades the stretch between open dots at 1 and 5, labelled absolute value of x minus 3 less than 2 and the interval (1, 5). The third shades the two rays outside open dots at 1 and 5, labelled absolute value of x minus 3 greater than 2 and the union of the intervals from minus infinity to 1 and from 5 to infinity.](../../assets/figures/03-high-school/absolute-value-equations-and-inequalities-distance.svg)

So "equals" gives two points, "less than" gives the middle, and "greater than" gives the outside. The algebra in this lesson gets the same answers when the inside is more complicated, such as $\lvert 2x - 3 \rvert$ or $\lvert 5 - 2x \rvert$.

Closeness is the idea behind limits in calculus. "The values $f(x)$ get close to $L$" is made exact with the statement $\lvert f(x) - L \rvert < \varepsilon$, and that is what the epsilon-delta definition<!-- link: ../../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md --> will use. Practice problem 7 is a first taste.

## Definitions

The absolute value of a number $x$ is $\lvert x \rvert = x$ if $x \ge 0$ and $\lvert x \rvert = -x$ if $x < 0$, the distance from $x$ to 0. The **distance** between $x$ and a number $a$ is $\lvert x - a \rvert$. Two facts from the earlier lesson are used constantly here: $\lvert u \rvert \ge 0$ for every number $u$, and $\lvert u \rvert = 0$ only for $u = 0$.

For a number $a$ and a positive number $r$, the interval $(a - r, a + r)$ has **centre** $a$ and **radius** $r$. The centre is the midpoint, and the radius is the distance from the centre to each end. So $(1, 5)$ has centre 3 and radius 2.

In plain words, $\lvert x - a \rvert < r$ says that $x$ is within $r$ of $a$, which is the same as saying that $x$ lies in the interval with centre $a$ and radius $r$.

A quantity has **tolerance** $t$ around a nominal value $a$, written $a \pm t$, when the acceptable values $x$ are those with $\lvert x - a \rvert \le t$. The acceptable values form the closed interval $[a - t, a + t]$. A tolerance can also be given as a percent of the nominal value: a resistor labelled 330 ohms with a 5% tolerance has $t = 0.05 \times 330 = 16.5$ ohms.

An **absolute value equation** or **absolute value inequality** is an equation or inequality in which the variable appears inside absolute value bars. An **extraneous solution** is a number that comes out of the solving steps but doesn't satisfy the original equation. It is not a mistake in arithmetic. It appears because a step, such as splitting into cases, allows more than the original equation does.

## How to do it

### The three basic forms

The picture suggests three rules. Here they are with a proof.

*Theorem.* Let $a$ be a real number and $r > 0$. For every real number $x$:

1. $\lvert x - a \rvert = r$ exactly when $x = a - r$ or $x = a + r$.
2. $\lvert x - a \rvert < r$ exactly when $a - r < x < a + r$.
3. $\lvert x - a \rvert > r$ exactly when $x < a - r$ or $x > a + r$.

The same holds with $\le$ in (2) and $\ge$ in (3), and then the endpoints $a - r$ and $a + r$ are included.

We know the definition of absolute value by cases, and the rules for inequalities (adding a number keeps the direction, and multiplying by $-1$ reverses it). We want each statement for every $x$. The plan is a proof by cases on the sign of $u = x - a$. In each case the bars disappear, and each statement becomes an ordinary inequality in $u$.

*Proof.* Put $u = x - a$.

If $u \ge 0$, then $\lvert u \rvert = u$. The three statements become $u = r$, $u < r$ and $u > r$.

If $u < 0$, then $\lvert u \rvert = -u$. The statement $-u = r$ means $u = -r$. The statement $-u < r$ means $u > -r$, because multiplying by $-1$ reverses the symbol. The statement $-u > r$ means $u < -r$.

Now collect the two cases for each statement.

1. The solutions are $u = r$ (case $u \ge 0$) or $u = -r$ (case $u < 0$). Both cases fit their conditions, since $r > 0$ and $-r < 0$. Adding $a$ gives $x = a + r$ or $x = a - r$.
2. The first case gives $0 \le u < r$ and the second gives $-r < u < 0$. Together they say $-r < u < r$, the two pieces joining at $u = 0$. Adding $a$ gives $a - r < x < a + r$.
3. The first case gives $u > r$, and the condition $u \ge 0$ then holds automatically because $r > 0$. The second gives $u < -r$, and $u < 0$ holds automatically. So $u > r$ or $u < -r$, and adding $a$ gives $x > a + r$ or $x < a - r$. $\blacksquare$

Look back: the proof used $r > 0$ so that each case condition fits. The next section says what happens when $r$ is 0 or negative. With $a = 3$ and $r = 2$ the theorem gives $x = 1$ or $5$, the interval $(1, 5)$, and the two outside rays, the pictures above. The mnemonic is "less than means between (and), greater than means outside (or)", as in [compound inequalities and interval notation](03-compound-inequalities-and-interval-notation.md): in (3), the statement is the "not between" case of the theorem there.

### When the other side is zero or negative

Replace the inside $x - a$ by any expression $u$, and the number $r$ by any number $c$. For $c > 0$ the theorem still works with $u$ in place of $x - a$, so the three rows below follow. For $c \le 0$, use the fact that $\lvert u \rvert \ge 0$ and $\lvert u \rvert = 0$ only when $u = 0$.

| Statement | $c > 0$ | $c = 0$ | $c < 0$ |
|---|---|---|---|
| $\lvert u \rvert = c$ | $u = c$ or $u = -c$ | $u = 0$ | no solution |
| $\lvert u \rvert < c$ | $-c < u < c$ | no solution | no solution |
| $\lvert u \rvert \le c$ | $-c \le u \le c$ | $u = 0$ | no solution |
| $\lvert u \rvert > c$ | $u < -c$ or $u > c$ | every $u$ except $u = 0$ | every $u$ |
| $\lvert u \rvert \ge c$ | $u \le -c$ or $u \ge c$ | every $u$ | every $u$ |

The graph of $y = \lvert 2x - 3 \rvert$ shows the three cases for an equation. A horizontal line at height $c = 7$ meets it twice, the line at $c = 0$ touches it once at the point of the V, and the line at $c = -2$ never meets it:

![The graph of y equals the absolute value of 2x minus 3, a V with its point at (1.5, 0). A dashed horizontal line at c = 7 crosses it at x = -2 and x = 5. A dashed line at c = 0 touches it at x = 1.5. A dashed line at c = -2 is below the whole graph and is labelled no solution.](../../assets/figures/03-high-school/absolute-value-equations-and-inequalities-cases-graph.svg)

### Solving an absolute value equation

1. Isolate the absolute value. Undo the additions and multiplications outside the bars, so that the equation reads $\lvert u \rvert = c$.
2. Look at $c$. If $c < 0$, there is no solution, so stop. If $c = 0$, solve $u = 0$.
3. If $c > 0$, write the two equations $u = c$ and $u = -c$, and solve each.
4. Check every answer in the original equation. This is required when the other side contains the variable, as in $\lvert x - 3 \rvert = 2x$.

When the other side contains the variable, split on the sign of the inside instead. If $u \ge 0$ the bars are $u$, and if $u < 0$ they are $-u$. Solve each case, and keep only the answers that satisfy the condition of their case (Example 4).

### Solving an absolute value inequality

1. Isolate the absolute value, as in Step 1 above. If you multiply or divide by a negative number, reverse the symbol.
2. Use the table: for $c > 0$, "less than" gives a chain and "greater than" gives an "or". For $c \le 0$, read the answer from the table.
3. Solve the resulting compound inequality for $x$, with the rules from [compound inequalities and interval notation](03-compound-inequalities-and-interval-notation.md).
4. Write the answer in interval notation.
5. Check a number from inside, a number from the gap or outside, and each endpoint.

## Worked examples

<div class="example" markdown>

### Example 1: an equation with something outside the bars

Solve $2\lvert 3x - 1 \rvert + 5 = 13$.

Step 1: isolate the absolute value. Subtract 5 from both sides to get $2\lvert 3x - 1 \rvert = 8$, then divide by 2:

$$
\lvert 3x - 1 \rvert = 4.
$$

Step 2: $c = 4$ is positive, so there are two equations.

Step 3: solve each. From $3x - 1 = 4$, $3x = 5$, so $x = \frac{5}{3}$. From $3x - 1 = -4$, $3x = -3$, so $x = -1$. The answer $\frac{5}{3}$ is untidy, and that is fine.

Step 4: check both in the original equation. At $x = \frac{5}{3}$, $3x - 1 = 4$, so the left side is $2 \cdot 4 + 5 = 13$. At $x = -1$, $3x - 1 = -4$, so $\lvert -4 \rvert = 4$ and the left side is again 13.

The two solutions sit on either side of the point where the inside is 0, which is $x = \frac{1}{3}$. Their average is $\frac{1}{2}\left(\frac{5}{3} + (-1)\right) = \frac{1}{3}$. That is a quick check, since the solutions of $\lvert u \rvert = c$ are always symmetric about the point where $u = 0$.

</div>

<div class="example" markdown>

### Example 2: tolerance, and a harder inequality

(a) A shaft has length $25 \pm 0.05$ mm. Find the passing lengths, and say which of 24.94, 25.02, 25.05 and 25.07 mm pass.

The condition is $\lvert L - 25 \rvert \le 0.05$. By the theorem with $\le$, this is $24.95 \le L \le 25.05$, the interval $[24.95, 25.05]$. The centre is 25 and the radius is 0.05. The failing lengths are $\lvert L - 25 \rvert > 0.05$, which is $(-\infty, 24.95) \cup (25.05, \infty)$.

![A number line from 24.90 to 25.10 mm with the accepted interval from 24.95 to 25.05 shaded, closed dots at both ends, and arrows showing a distance of 0.05 on each side of 25.00. A second line marks four measured parts: 24.94 as an open red dot, 25.02 as a closed green dot, 25.05 as a closed green dot and 25.07 as an open red dot.](../../assets/figures/03-high-school/absolute-value-equations-and-inequalities-tolerance.svg)

Test each part by its distance from 25. The part at 24.94 is 0.06 away, which is more than 0.05, so it fails. The part at 25.02 is 0.02 away and passes. The part at 25.05 is exactly 0.05 away, and the inequality allows equality, so it passes. The part at 25.07 is 0.07 away and fails.

(b) Solve $\lvert 5 - 2x \rvert \ge 3$.

The value 3 is positive and the symbol is $\ge$, so the answer is an "or": $5 - 2x \ge 3$ or $5 - 2x \le -3$. From the first, $-2x \ge -2$, and dividing by $-2$ reverses the symbol: $x \le 1$. From the second, $-2x \le -8$, so $x \ge 4$. The answer is $(-\infty, 1] \cup [4, \infty)$.

Check: at the endpoint 1, $\lvert 5 - 2 \rvert = 3 \ge 3$ is true, and at 4, $\lvert 5 - 8 \rvert = 3 \ge 3$ is true. The gap number 2 gives $\lvert 1 \rvert = 1 \ge 3$, which is false, and the outside number 0 gives $5 \ge 3$, which is true. Distance form agrees: $\lvert 5 - 2x \rvert = 2\lvert x - \frac{5}{2} \rvert$, so the condition says $x$ is at least $\frac{3}{2}$ from $\frac{5}{2}$, and $\frac{5}{2} \pm \frac{3}{2}$ are 1 and 4.

</div>

<div class="example" markdown>

### Example 3: zero and negative values on the other side

Solve each statement.

- (a) $\lvert x + 3 \rvert = -2$. A distance can't be negative, so there is no solution.
- (b) $\lvert 4x - 1 \rvert = 0$. Only $4x - 1 = 0$ works, so $x = \frac{1}{4}$, one solution.
- (c) $\lvert x \rvert < 0$ has no solution, and $\lvert x \rvert \le 0$ has the single solution $x = 0$.
- (d) $\lvert x - 2 \rvert > -1$. Every absolute value is at least 0, which is above $-1$, so every real number is a solution: $(-\infty, \infty)$.
- (e) $\lvert x \rvert > 0$ is true for every $x$ except 0: $(-\infty, 0) \cup (0, \infty)$.

Check (a) by trying a number: at $x = -1$, $\lvert -1 + 3 \rvert = 2$, not $-2$. Check (d) at $x = 2$, the point where the bars give 0: $0 > -1$ is true. Check (e) at $x = 0$: $0 > 0$ is false, so 0 is correctly left out.

<div class="warning" markdown>

Watch out: don't turn $\lvert x + 3 \rvert = -2$ into $x + 3 = \pm 2$ without looking at the sign of the right side. The two numbers $-1$ and $-5$ that this gives are both wrong: $\lvert -1 + 3 \rvert = 2$ and $\lvert -5 + 3 \rvert = 2$, not $-2$. The right side decides first, and a negative one ends the problem.

</div>

</div>

<div class="example" markdown>

### Example 4: an extraneous solution (finish it yourself)

Solve $\lvert x - 3 \rvert = 2x$.

The right side contains the variable, so split on the sign of the inside, $x - 3$.

If $x \ge 3$, then $\lvert x - 3 \rvert = x - 3$, and the equation is $x - 3 = 2x$. That gives $x = -3$. But this case required $x \ge 3$, and $-3$ is not, so it is rejected.

If $x < 3$, then $\lvert x - 3 \rvert = -(x - 3) = 3 - x$, and the equation is $3 - x = 2x$.

![The graphs of y equals the absolute value of x minus 3, in blue, and y equals 2x, in orange. They cross once, at the green point x = 1, y = 2. A dashed red line at x = minus 3 joins the points (-3, 6) on the blue graph and (-3, -6) on the orange line, labelled not equal.](../../assets/figures/03-high-school/absolute-value-equations-and-inequalities-extraneous.svg)

Now finish: solve this equation, check that the answer satisfies $x < 3$, and check it in the original equation. Then check $x = -3$ in the original and say why it fails.

<details class="solution" markdown>
<summary>Finish</summary>

From $3 - x = 2x$ we get $3 = 3x$, so $x = 1$. This satisfies $x < 3$, so it is accepted. In the original equation, the left side is $\lvert 1 - 3 \rvert = 2$ and the right side is $2 \cdot 1 = 2$. The only solution is $x = 1$.

The rejected candidate $x = -3$ is extraneous. In the original, the left side is $\lvert -3 - 3 \rvert = 6$ and the right side is $2(-3) = -6$, so the sides differ. It appeared because the equation $x - 3 = 2x$ ignores the condition $x \ge 3$ that made the bars disappear. In the figure, the two graphs are 12 apart at $x = -3$ and cross only at $x = 1$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: isolate the absolute value before you split. For $\lvert x - 1 \rvert + 3 = 7$, writing $x - 1 + 3 = \pm 7$ gives $x = 5$ or $x = -9$. The second is wrong: $\lvert -9 - 1 \rvert + 3 = 13$, not 7. The correct first step gives $\lvert x - 1 \rvert = 4$, so $x = 5$ or $x = -3$.

</div>

<div class="warning" markdown>

Watch out: split by changing the sign of the other side, not the sign of $x$. The equation $\lvert x - 3 \rvert = 5$ means $x - 3 = 5$ or $x - 3 = -5$, so $x = 8$ or $x = -2$. Writing $x + 3 = 5$ for the second case gives $x = 2$, and $\lvert 2 - 3 \rvert = 1$, not 5.

</div>

<div class="warning" markdown>

Watch out: don't mix up "and" and "or". The inequality $\lvert x - 3 \rvert < 2$ is the chain $1 < x < 5$, and the "or" form $x < 1$ or $x > 5$ is its opposite. Test the centre, $x = 3$: $\lvert 0 \rvert < 2$ is true, so 3 must be in the answer, and only the chain contains it.

</div>

<div class="warning" markdown>

Watch out: absolute value bars don't distribute over a sum. The expression $\lvert x + 3 \rvert$ is not $\lvert x \rvert + 3$, and $\lvert a + b \rvert$ is not $\lvert a \rvert + \lvert b \rvert$ in general. With $a = 3$ and $b = -5$, $\lvert 3 + (-5) \rvert = 2$ but $\lvert 3 \rvert + \lvert -5 \rvert = 8$. In general $\lvert a + b \rvert \le \lvert a \rvert + \lvert b \rvert$, the triangle inequality, with equality only when $a$ and $b$ have the same sign (or one is 0).

</div>

Check when the variable is on both sides. If you only solve the two linear equations, as in Example 4, you can get an answer that fails. For a number on the right side, no check is needed beyond Step 4, but an expression with the variable always needs one.

For inequalities, a division by a negative number inside the chain reverses both symbols. For example, $\lvert 3 - x \rvert < 4$ becomes $-4 < 3 - x < 4$. Subtracting 3 gives $-7 < -x < 1$, and multiplying by $-1$ gives $7 > x > -1$, so the answer is $(-1, 7)$. A check: the centre of $\lvert x - 3 \rvert < 4$ is 3, and $3 \pm 4$ are $-1$ and 7.

When you write $-r < x - a < r$, remember to add $a$ to all three parts. Forgetting this gives $(-r, r)$, which is the answer only when $a = 0$.

## Tricks and shortcuts

Read $\lvert x - a \rvert < r$ aloud as "$x$ is within $r$ of $a$", and write $(a - r, a + r)$ at once. So $\lvert x - 25 \rvert \le 0.05$ is $[24.95, 25.05]$ with no algebra.

Factor the coefficient of $x$ out of the bars. Since $\lvert ab \rvert = \lvert a \rvert \lvert b \rvert$, we have $\lvert 2x - 6 \rvert = 2\lvert x - 3 \rvert$. The inequality $\lvert 2x - 6 \rvert < 4$ becomes $\lvert x - 3 \rvert < 2$, which is $(1, 5)$.

To go the other way, from an interval to an absolute value inequality, use the midpoint and the half-length. The interval from $p$ to $q$ has centre $\frac{p + q}{2}$ and radius $\frac{q - p}{2}$. The interval $[2, 8]$ has centre 5 and radius 3, so it is $\lvert x - 5 \rvert \le 3$.

When two absolute values are equal, $\lvert u \rvert = \lvert v \rvert$, the two numbers are the same distance from 0, so they are equal or opposite: $u = v$ or $u = -v$. For example, $\lvert x - 1 \rvert = \lvert 2x + 3 \rvert$ gives $x - 1 = 2x + 3$, so $x = -4$, or $x - 1 = -(2x + 3)$, so $x = -\frac{2}{3}$. Check at $-4$: $\lvert -5 \rvert = \lvert -5 \rvert$. Check at $-\frac{2}{3}$: both sides are $\frac{5}{3}$.

For a percent tolerance, find the radius first. A 330 ohm resistor with a 5% tolerance has radius $0.05 \times 330 = 16.5$, so the accepted values are $[313.5, 346.5]$.

## In code

A tolerance test is an absolute value inequality, and floating-point numbers make the endpoints tricky. The lines below show the problem and two fixes, then use sympy to solve the examples exactly.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
from decimal import Decimal
from sympy import symbols, Eq, Abs, Rational, solveset, S

print(abs(25.05 - 25))                      # 0.05000000000000071
print(abs(25.05 - 25) <= 0.05)              # False, though 25.05 should pass
print(abs(Decimal("25.05") - Decimal("25")) <= Decimal("0.05"))   # True
print(abs(25.05 - 25) <= 0.05 + 1e-9)       # True, with a little slack
print(math.isclose(25.05, 25, abs_tol=0.05 + 1e-9))               # True

x = symbols("x", real=True)
print(solveset(Eq(2 * Abs(3 * x - 1) + 5, 13), x, S.Reals))      # {-1, 5/3}
print(solveset(Abs(x - 25) <= Rational(1, 20), x, S.Reals))      # Interval(499/20, 501/20)
print(solveset(Abs(5 - 2 * x) >= 3, x, S.Reals))                 # Union(Interval(-oo, 1), Interval(4, oo))
print(solveset(Eq(Abs(x - 3), 2 * x), x, S.Reals))               # {1}
```

The float $25.05 - 25$ is stored as $0.05000000000000071$, slightly more than 0.05, so the exact-looking test fails for a part that is right on the boundary. Exact decimal arithmetic or a small slack fixes it, and `math.isclose` with an absolute tolerance does the same job in one call. The sympy lines return exact sets: $\frac{499}{20} = 24.95$ and $\frac{501}{20} = 25.05$, and the equation from Example 4 returns only $\{1\}$, with the extraneous $-3$ already discarded.

</details>

## FAQ

### Why does "less than" give an "and" and "greater than" give an "or"?

Distance gives the reason. Being closer than $r$ to $a$ means being on the right side of $a - r$ and on the left side of $a + r$ at once, so both conditions hold: an "and", which is the stretch between. Being farther than $r$ from $a$ can happen on either side, so one condition is enough: an "or", which is the two rays outside.

### Can I solve by squaring both sides?

Sometimes. Since $\lvert u \rvert^2 = u^2$, the equation $\lvert u \rvert = \lvert v \rvert$ is equivalent to $u^2 = v^2$, and that gives the same two cases after factoring. For an inequality like $\lvert 2x - 1 \rvert < 3$, squaring to $(2x - 1)^2 < 9$ is valid but needs quadratic inequalities, which come later in [polynomial and rational inequalities](../06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md). The case method here is simpler.

### Why is the distance between two points $\lvert x - a \rvert$ and not just $x - a$?

A difference can be negative, and a distance can't. The number $x - a$ tells you the direction as well as the size: it is negative when $x$ is to the left of $a$. Taking the absolute value keeps the size and drops the direction. It is also why $\lvert x - a \rvert = \lvert a - x \rvert$. In the plane the distance formula has a square root, and on a line it reduces to the same thing, since $\sqrt{(x - a)^2} = \lvert x - a \rvert$ by [roots, irrational numbers and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#square-roots-and-cube-roots).

### What if the equation has no absolute value signs left after I isolate it, or the bars are around a constant?

Then it is not really an absolute value equation. If the bars surround only numbers, such as $\lvert 3 - 8 \rvert$, evaluate them first. If the variable cancels, as in $\lvert x \rvert - \lvert x \rvert = 0$, treat the result like any statement with no variable: true means every number works, false means none does.

## Practice

### Warm-up

1\. Solve (a) $\lvert x \rvert = 9$, (b) $\lvert x - 4 \rvert = 9$, (c) $\lvert x + 4 \rvert = 0$ and (d) $\lvert x - 4 \rvert = -9$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $x = 9$ or $x = -9$.
- (b) $x - 4 = 9$ gives $x = 13$, and $x - 4 = -9$ gives $x = -5$.
- (c) Only $x + 4 = 0$ works, so $x = -4$.
- (d) The right side is negative and a distance is not, so there is no solution.

Check (b): $\lvert 13 - 4 \rvert = 9$ and $\lvert -5 - 4 \rvert = 9$.

</details>

2\. Write each as an absolute value inequality and solve it. (a) $x$ is within 3 of 10. (b) $x$ is at least 3 away from 10. (c) Write the interval $[2, 8]$ in the form $\lvert x - c \rvert \le r$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $\lvert x - 10 \rvert \le 3$, which is $[7, 13]$.
- (b) $\lvert x - 10 \rvert \ge 3$, which is $(-\infty, 7] \cup [13, \infty)$.
- (c) The centre is $\frac{2 + 8}{2} = 5$ and the radius is $\frac{8 - 2}{2} = 3$, so $\lvert x - 5 \rvert \le 3$.

Check (c): $\lvert 2 - 5 \rvert = 3$ and $\lvert 8 - 5 \rvert = 3$, so both ends are included, and the centre 5 gives $0 \le 3$.

</details>

3\. Solve $\lvert 2x + 1 \rvert < 7$ and write the answer in interval notation.

<details class="solution" markdown>
<summary>Solution</summary>

Write the chain $-7 < 2x + 1 < 7$. Subtract 1 from all three parts: $-8 < 2x < 6$. Divide by 2: $-4 < x < 3$. The answer is $(-4, 3)$.

Check: the endpoint $-4$ gives $\lvert -7 \rvert = 7 < 7$, which is false, and 3 gives $\lvert 7 \rvert = 7 < 7$, which is false, so both are correctly excluded. The test number 0 gives $1 < 7$, which is true.

</details>

### Standard

4\. Solve $3\lvert x - 2 \rvert + 4 \ge 13$ and write the answer in interval notation.

<details class="solution" markdown>
<summary>Solution</summary>

Subtract 4: $3\lvert x - 2 \rvert \ge 9$. Divide by 3: $\lvert x - 2 \rvert \ge 3$. This says $x$ is at least 3 from 2, so $x \le -1$ or $x \ge 5$. The answer is $(-\infty, -1] \cup [5, \infty)$.

Check: at $x = 5$, $3 \cdot 3 + 4 = 13 \ge 13$ is true. At $x = -1$, $3 \cdot 3 + 4 = 13$, true. At the gap number 2, $0 + 4 = 4 \ge 13$ is false.

</details>

5\. Solve $\lvert 3x - 2 \rvert = \lvert x + 6 \rvert$.

<details class="solution" markdown>
<summary>Solution</summary>

The two expressions are equal or opposite. Equal: $3x - 2 = x + 6$, so $2x = 8$ and $x = 4$. Opposite: $3x - 2 = -(x + 6) = -x - 6$, so $4x = -4$ and $x = -1$.

Check: at $x = 4$, $\lvert 10 \rvert = \lvert 10 \rvert$. At $x = -1$, $\lvert -5 \rvert = \lvert 5 \rvert$.

</details>

6\. A resistor is labelled 330 ohms with a 5% tolerance. (a) Find the interval of acceptable values $R$ and write it as $\lvert R - 330 \rvert \le t$. (b) Which of 312, 320, 340 and 347 ohms are acceptable?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The radius is $t = 0.05 \times 330 = 16.5$. The condition is $\lvert R - 330 \rvert \le 16.5$, which is $313.5 \le R \le 346.5$, the interval $[313.5, 346.5]$.

(b) Compare each distance from 330 with 16.5: 312 is 18 away, so it fails. 320 is 10 away and passes. 340 is 10 away and passes. 347 is 17 away, so it fails.

Check: $330 - 16.5 = 313.5$ and $330 + 16.5 = 346.5$. The values 312 and 347 are outside this interval, and 320 and 340 are inside.

</details>

### Challenge

7\. This is a first look at the epsilon-delta definition<!-- link: ../../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md -->. (a) Show that $\lvert 3x - 6 \rvert < 0.3$ is the same as $\lvert x - 2 \rvert < 0.1$. (b) For a general number $\varepsilon > 0$, find a number $\delta > 0$ such that $\lvert x - 2 \rvert < \delta$ guarantees $\lvert 3x - 6 \rvert < \varepsilon$. (c) Find the largest $\delta$ that keeps $\lvert 4x - 12 \rvert < 0.2$ whenever $\lvert x - 3 \rvert < \delta$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Factor the 3 out of the bars: $\lvert 3x - 6 \rvert = 3\lvert x - 2 \rvert$. So $3\lvert x - 2 \rvert < 0.3$, and dividing by 3 gives $\lvert x - 2 \rvert < 0.1$. Each step can be reversed, so the two inequalities say the same thing.

(b) We know that $\lvert 3x - 6 \rvert = 3\lvert x - 2 \rvert$, and we want it below $\varepsilon$. The plan is to work backwards from $3\lvert x - 2 \rvert < \varepsilon$. That is the same as $\lvert x - 2 \rvert < \frac{\varepsilon}{3}$, so take $\delta = \frac{\varepsilon}{3}$. Then $\lvert x - 2 \rvert < \delta$ gives $\lvert 3x - 6 \rvert = 3\lvert x - 2 \rvert < 3\delta = \varepsilon$. With $\varepsilon = 0.3$, this is $\delta = 0.1$, as in (a).

(c) $\lvert 4x - 12 \rvert = 4\lvert x - 3 \rvert < 0.2$ means $\lvert x - 3 \rvert < 0.05$, so the largest $\delta$ is 0.05. Any larger $\delta$ lets in a number such as $x = 3.06$, which has $\lvert 4 \cdot 3.06 - 12 \rvert = 0.24$, not below 0.2.

Check (b) with numbers: take $\varepsilon = 0.3$ and $x = 2.09$, which is within $\delta = 0.1$ of 2. Then $\lvert 3 \cdot 2.09 - 6 \rvert = 0.27 < 0.3$. For $x = 2.11$, outside the $\delta$ range, we get $0.33$.

</details>

8\. This one reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md). A forecast says revenue will be \$2.4 million, with a margin of error of 7.5% of the forecast. (a) Write the acceptable revenues $R$, in millions of dollars, as an absolute value inequality and as an interval. (b) Is a revenue of \$2.6 million within the margin? (c) By what percent of the forecast does \$2.6 million differ from it?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The radius is $0.075 \times 2.4 = 0.18$ million. The condition is $\lvert R - 2.4 \rvert \le 0.18$, which is $2.22 \le R \le 2.58$, so $[2.22, 2.58]$.

(b) The distance is $\lvert 2.6 - 2.4 \rvert = 0.2$, which is more than 0.18, so \$2.6 million is outside the margin.

(c) The percent is taken of the forecast, since the question says "of the forecast", so the whole is 2.4. The difference is 0.2, and $0.2 \div 2.4 = 0.0833\ldots$, about 8.3%.

Check: 7.5% of 2.4 is 0.18, and 8.3% is more than 7.5%, consistent with (b).

</details>

## Where this shows up

- The next chapter's [piecewise, absolute value and step functions](../03-functions/03-piecewise-absolute-value-and-step-functions.md) graphs $y = \lvert x \rvert$, a V with its point at the origin, and shifts and stretches it. Solving $\lvert 2x - 3 \rvert = 7$ is finding where the V crosses a horizontal line.
- The epsilon-delta definition<!-- link: ../../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md --> writes "close" as $\lvert x - a \rvert < \delta$ and $\lvert f(x) - L \rvert < \varepsilon$, as in Practice problem 7. A confidence interval is "estimate plus or minus a margin", which is $\lvert \mu - \bar{x} \rvert \le m$ (confidence intervals<!-- link: ../../05-university-core/08-statistics/02-confidence-intervals.md -->).
- In computing, comparing floats means testing $\lvert a - b \rvert \le \text{tolerance}$, and a numerical method such as Newton's method stops when the change is smaller than a tolerance. In economics, a target band such as the Bank of Canada's 1% to 3% is a tolerance around 2%.
