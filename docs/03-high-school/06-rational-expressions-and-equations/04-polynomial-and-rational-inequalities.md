# Polynomial and rational inequalities

After this lesson you can solve polynomial and rational inequalities with a sign chart, write the answer in interval notation, and use the method to answer questions such as when a profit is positive or when the average cost is below a target.

Before this: [compound inequalities and interval notation](../01-algebra-foundations/03-compound-inequalities-and-interval-notation.md), [factoring polynomials](../04-radicals-and-polynomials/03-factoring-polynomials.md), [polynomial functions and graphs](../04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md) and [rational expressions](01-rational-expressions.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $(x + 3)(x - 1)(x - 4) \le 0$ and write the answer in interval notation.
2. Solve $\dfrac{x + 1}{x - 2} \ge 0$.
3. Solve $\dfrac{3}{x - 2} \ge 1$. Why is it wrong to start by multiplying both sides by $x - 2$?

<details class="solution" markdown>
<summary>Answers</summary>

1. The zeros are $-3$, $1$ and $4$. The signs on the four intervals, from left to right, are $-, +, -, +$, and the zeros are included because of the $\le$. The answer is $(-\infty, -3] \cup [1, 4]$.
2. The critical numbers are $-1$ (numerator) and $2$ (denominator). The signs are $+, -, +$. The zero $-1$ is included and the value $2$ never is, so the answer is $(-\infty, -1] \cup (2, \infty)$.
3. Move everything to one side: $\frac{3}{x - 2} - 1 = \frac{5 - x}{x - 2} \ge 0$. The critical numbers are 2 and 5 and the signs are $-, +, -$, so the answer is $(2, 5]$. Multiplying by $x - 2$ is wrong because $x - 2$ is positive for some $x$ and negative for others, so you don't know whether to flip the inequality.

</details>

## The idea

A business makes $q$ units a day and its profit in dollars is $P(q) = -q^2 + 120q - 2000$. The question a manager asks is not "when is the profit exactly 0?" but "for which quantities is the profit positive?" The first question has the answers $q = 20$ and $q = 100$, the break-even points, found by factoring $-(q - 20)(q - 100)$. The second needs more: the profit is 0 at those two numbers, and in between, at $q = 60$, it is $P(60) = 1600$, which is positive. Outside, at $q = 10$ or $q = 120$, it is negative. So the profit is positive exactly when $20 < q < 100$.

That reasoning works for any polynomial. The graph of a polynomial has no jumps, so it cannot go from above the axis to below it without crossing the axis at a zero. Between two neighbouring zeros the sign stays the same, and one test number tells you the sign for the whole stretch. A rational expression has a second way to change sign, because it can jump at a zero of the denominator, where it is undefined. So the places to mark are the zeros of the top and the zeros of the bottom.

This is the sign chart from [polynomial functions and graphs](../04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#sketching-a-graph-from-the-factored-form), used now as a solving tool. The skill is the same every time: get 0 on one side, factor, mark the critical numbers, test one number in each interval, and read off the answer.

## Definitions

A **polynomial inequality** is an inequality that can be written as $p(x) > 0$, with $p$ a polynomial and with $>$ replaced by $<$, $\ge$ or $\le$ if needed. A **rational inequality** is one that can be written the same way with a rational expression $\frac{p(x)}{q(x)}$ in place of $p(x)$. In plain words, it is a question about the sign of a polynomial or a fraction of polynomials, once everything has been moved to one side.

A **critical number** of such an inequality is a real number that is a zero of the numerator or a zero of the denominator, after everything has been combined into one fraction and factored. In plain words, the critical numbers are the only places where the sign of the expression can change, or where it is not defined. A **sign chart** is a number line marked at the critical numbers, with the sign of the expression written on each interval between them.

The answer to an inequality is a set of real numbers, written in [interval notation](../01-algebra-foundations/03-compound-inequalities-and-interval-notation.md#definitions) with $\cup$ joining separate pieces. The rule for endpoints is short. A zero of the numerator makes the whole expression 0, so it is included for $\ge$ and $\le$ and excluded for $>$ and $<$. A zero of the denominator makes the expression undefined, so it is never included, whatever the symbol.

### Why one test number is enough

*Theorem (sign constancy).* Let $p$ and $q$ be polynomials and let $I$ be an interval of real numbers that contains no zero of $p$ and no zero of $q$. Then the expression $\frac{p(x)}{q(x)}$ has the same sign for every $x$ in $I$, and it is never 0 or undefined there.

We know that the graph of a polynomial has no jumps, so if a polynomial has opposite signs at two numbers, it has a zero between them (fact 2 in [what the graph must do](../04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#what-the-graph-must-do)). We want to show that the quotient cannot change sign inside $I$. The plan is to apply that fact to $p$ and to $q$ separately.

*Proof.* Suppose $p$ had a positive value at one number of $I$ and a negative value at another. Then $p$ would have a zero between them, which is also in $I$, and that contradicts the assumption. So $p$ has one sign on all of $I$, and it is never 0. The same argument applies to $q$. The quotient of two numbers of fixed signs has a fixed sign: positive if the signs of $p$ and $q$ agree, negative if they differ. $\blacksquare$

Look back: the proof used only that polynomials have no jumps. The expression changes sign only at critical numbers, and whether it does depends on the factor. A factor $(x - r)^k$ changes sign at $r$ when $k$ is odd, and keeps its sign when $k$ is even, as in the [multiplicity rule](../04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#crossing-and-touching). This holds for a factor in the denominator as well.

## How to do it

### Solving a polynomial inequality

1. Move every term to one side, so that the other side is 0. If you divide or multiply by a negative number, flip the inequality.
2. Factor the polynomial completely.
3. Find the zeros. They are the critical numbers. Mark them on a number line in order.
4. Find the sign of the polynomial on each interval. Either test one number from each interval, or note the sign at the right end (the sign of the leading coefficient) and flip it at each critical number that comes from an odd power, moving left.
5. Pick the intervals that match the inequality: positive for $> 0$ and $\ge 0$, negative for $< 0$ and $\le 0$.
6. For $\ge$ and $\le$, include the zeros, as single points or as closed ends. For $>$ and $<$, leave them out.
7. Write the answer in interval notation, and check one number from inside the answer and one from outside in the original inequality.

### Solving a rational inequality

1. Move every term to one side, so that the other side is 0. Do not multiply by the denominator.
2. Combine the terms into a single fraction with the LCD ([adding and subtracting](01-rational-expressions.md#adding-and-subtracting)), then factor the numerator and the denominator.
3. The critical numbers are the zeros of the numerator and the zeros of the denominator. Mark all of them.
4. Make the sign chart as in Step 4 above.
5. Pick the intervals that match the inequality. Include a zero of the numerator only for $\ge$ and $\le$. Never include a zero of the denominator.
6. Write the answer in interval notation and check one number from each kind of interval.

### Why not multiply by the denominator

To solve $\frac{3}{x - 2} \ge 1$ you could try to multiply both sides by $x - 2$. But multiplying an inequality by a positive number keeps its direction and multiplying by a negative number flips it, and here you don't know which one $x - 2$ is. A correct version splits into two cases. If $x - 2 > 0$, so that $x > 2$, the direction stays and $3 \ge x - 2$, so $x \le 5$. Together with $x > 2$ that gives $2 < x \le 5$. If $x - 2 < 0$, so that $x < 2$, the direction flips and $3 \le x - 2$, so $x \ge 5$. That contradicts $x < 2$, so there is nothing from this case. The solution is $(2, 5]$.

The sign chart gets the same answer in one pass: $\frac{3}{x - 2} - 1 = \frac{5 - x}{x - 2} \ge 0$, with critical numbers 2 and 5. If you multiplied by $x - 2$ without splitting, you would get $x \le 5$, and that answer includes $x = 0$, where $\frac{3}{-2} = -1.5$ is not at least 1.

## Worked examples

<div class="example" markdown>

### Example 1: a cubic

Solve $x^3 - x^2 - 6x > 0$.

Step 1: the right side is already 0.

Step 2: factor. Take out $x$: $x(x^2 - x - 6)$, and $x^2 - x - 6 = (x - 3)(x + 2)$. So the inequality is $x(x - 3)(x + 2) > 0$.

Step 3: the critical numbers are $-2$, $0$ and $3$.

Step 4: test one number in each of the four intervals.

| Interval | Test number | $x$ | $x - 3$ | $x + 2$ | Product |
|---|---|---|---|---|---|
| $x < -2$ | $-3$ | $-$ | $-$ | $-$ | $-$ |
| $-2 < x < 0$ | $-1$ | $-$ | $-$ | $+$ | $+$ |
| $0 < x < 3$ | $1$ | $+$ | $-$ | $+$ | $-$ |
| $x > 3$ | $4$ | $+$ | $+$ | $+$ | $+$ |

Step 5 and 6: we want the positive intervals, and the inequality is strict, so the zeros stay out. The answer is $(-2, 0) \cup (3, \infty)$.

Step 7: check inside and outside. At $x = -1$ the value is $-1 - 1 + 6 = 4 > 0$, and at $x = 4$ it is $64 - 16 - 24 = 24 > 0$. At $x = -3$ it is $-27 - 9 + 18 = -18$, and at $x = 1$ it is $1 - 1 - 6 = -6$, so neither of those is in the answer.

The shortcut also works: the leading coefficient is positive, so the sign is $+$ at the far right, and it flips at each of $3$, $0$ and $-2$, because each power is 1. That gives $+, -, +, -$ from right to left, matching the table.

</div>

<div class="example" markdown>

### Example 2: a rational inequality with four critical numbers

Solve $\dfrac{x^2 - x - 6}{x^2 - 1} \ge 0$.

Step 1 and 2: the right side is 0 and there is one fraction already. Factor: $\frac{(x - 3)(x + 2)}{(x - 1)(x + 1)} \ge 0$.

Step 3: the zeros of the numerator are $3$ and $-2$. The zeros of the denominator are $1$ and $-1$. So the critical numbers, in order, are $-2, -1, 1, 3$.

Step 4: the sign chart. Each row is a factor, and the last row is the quotient.

| Interval | $x - 3$ | $x + 2$ | $x - 1$ | $x + 1$ | Quotient |
|---|---|---|---|---|---|
| $x < -2$ | $-$ | $-$ | $-$ | $-$ | $+$ |
| $-2 < x < -1$ | $-$ | $+$ | $-$ | $-$ | $-$ |
| $-1 < x < 1$ | $-$ | $+$ | $-$ | $+$ | $+$ |
| $1 < x < 3$ | $-$ | $+$ | $+$ | $+$ | $-$ |
| $x > 3$ | $+$ | $+$ | $+$ | $+$ | $+$ |

![A number line with critical numbers minus 2, minus 1, 1 and 3. Four rows of signs show the factors x minus 3, x plus 2, x minus 1 and x plus 1 on each of the five intervals, and a row below the line shows the quotient signs plus, minus, plus, minus, plus. A green bar marks the solution: a closed dot at minus 2 with the line to its left, an open interval from minus 1 to 1 with open dots, and a closed dot at 3 with the line to its right.](../../assets/figures/03-high-school/polynomial-and-rational-inequalities-sign-chart.svg)

Step 5 and 6: pick the $+$ intervals. The zeros of the numerator, $-2$ and $3$, are included because of the $\ge$. The zeros of the denominator, $-1$ and $1$, are excluded. The answer is

$$
(-\infty, -2] \cup (-1, 1) \cup [3, \infty).
$$

Step 7: check one number from each interval in the original. At $x = -3$: $\frac{9 + 3 - 6}{9 - 1} = \frac{6}{8} > 0$. At $x = 0$: $\frac{-6}{-1} = 6 > 0$. At $x = 4$: $\frac{16 - 4 - 6}{16 - 1} = \frac{6}{15} > 0$. At $x = -1.5$: $\frac{2.25 + 1.5 - 6}{2.25 - 1} = \frac{-2.25}{1.25} < 0$, and at $x = 2$: $\frac{4 - 2 - 6}{4 - 1} = -\frac{4}{3} < 0$, so those two intervals are out.

<div class="warning" markdown>

Watch out at Step 5: an answer like $[-2, 3]$ is the classic slip. The chart alternates, so the answer has three separate pieces, and it must be written with $\cup$.

</div>

</div>

<div class="example" markdown>

### Example 3: when is the profit positive

A business has the profit $P(q) = -q^2 + 120q - 2000$ dollars per day from $q$ units. (a) For which $q$ is the profit positive? (b) For which $q$ is it at least \$1,200?

(a) We need $-q^2 + 120q - 2000 > 0$. The leading coefficient is negative, so multiply both sides by $-1$ and flip the inequality: $q^2 - 120q + 2000 < 0$. Factor: the numbers $-20$ and $-100$ have product 2000 and sum $-120$, so $(q - 20)(q - 100) < 0$. The critical numbers are 20 and 100. The product of two factors is negative when they have opposite signs: that is between the zeros. So the profit is positive for $20 < q < 100$, which is $(20, 100)$.

(b) We need $-q^2 + 120q - 2000 \ge 1200$, so $-q^2 + 120q - 3200 \ge 0$, and after multiplying by $-1$: $q^2 - 120q + 3200 \le 0$. Factor: $(q - 40)(q - 80) \le 0$. Between the zeros the product is negative, and the zeros are included, so $[40, 80]$.

Check: $P(60) = -3600 + 7200 - 2000 = 1600$, which is positive and at least 1200. $P(20) = 0$ and $P(100) = 0$ are the break-even points, which are not in the answer to (a). $P(40) = -1600 + 4800 - 2000 = 1200$ and $P(80) = -6400 + 9600 - 2000 = 1200$, so both ends of (b) are included. $P(30) = -900 + 3600 - 2000 = 700$ is positive but below 1200, so it is in (a) and not in (b).

</div>

<div class="example" markdown>

### Example 4: average cost below a target (finish it yourself)

The cost of making $q$ units is $C(q) = 5000 + 12q$ dollars, so the average cost is $\overline{C}(q) = \frac{5000}{q} + 12$ for $q > 0$ ([rational functions and asymptotes](02-rational-functions-and-asymptotes.md#models)). For what quantities is the average cost at most \$15?

Step 1: move everything to one side: $\frac{5000}{q} + 12 - 15 \le 0$, that is $\frac{5000}{q} - 3 \le 0$.

Step 2: combine: $\frac{5000 - 3q}{q} \le 0$.

Step 3: the critical numbers are $q = 0$ (denominator, never included) and $q = \frac{5000}{3} \approx 1666.7$ (numerator).

Now make the sign chart, remember that $q > 0$ in this problem, and give the answer both as an interval and as a whole number of units.

<details class="solution" markdown>
<summary>Finish</summary>

The signs of $\frac{5000 - 3q}{q}$: for $q < 0$ the top is positive and the bottom is negative, so the quotient is negative. For $0 < q < \frac{5000}{3}$ both are positive, so the quotient is positive. For $q > \frac{5000}{3}$ the top is negative and the bottom is positive, so it is negative again.

We want $\le 0$, so the quotient is negative or zero. With $q > 0$ the answer is $q \ge \frac{5000}{3}$, that is $\left[\frac{5000}{3}, \infty\right)$. The numerator's zero is included because of the $\le$.

Units are whole, so the company needs at least 1,667 units. Check: $\overline{C}(1667) = \frac{5000}{1667} + 12 \approx 14.9994$, which is at most 15, and $\overline{C}(1666) = \frac{5000}{1666} + 12 \approx 15.0012$, which is just over.

![The graph of average cost, 5000 over q plus 12, falling toward a dashed line at 12 dollars. A dashed horizontal line marks the target of 15 dollars. The curve crosses it at q equal to about 1666.7, and the region to the right of that point is shaded to show average cost at most 15 dollars.](../../assets/figures/03-high-school/polynomial-and-rational-inequalities-average-cost-target.svg)

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: multiplying by an expression of unknown sign. In $\frac{x}{x - 1} > 2$, multiplying by $x - 1$ gives $x > 2x - 2$, so $x < 2$. But $x = 0$ is in that answer and $\frac{0}{-1} = 0$ is not greater than 2. The correct solution is $\frac{x}{x - 1} - 2 = \frac{2 - x}{x - 1} > 0$, which is $(1, 2)$. Always get 0 on one side and compare signs.

</div>

<div class="warning" markdown>

Watch out: forgetting to flip. Dividing or multiplying by a negative number reverses the inequality. In Example 3, $-q^2 + 120q - 2000 > 0$ becomes $q^2 - 120q + 2000 < 0$. A quick check settles it: the correct answer must contain $q = 60$, where the profit is positive, and the flipped version $q < 20$ or $q > 100$ does not.

</div>

<div class="warning" markdown>

Watch out: a hole is still excluded. Solve $\frac{x^2 - 4}{x - 2} \ge 0$. The fraction reduces to $x + 2$ for $x \ne 2$, and $x + 2 \ge 0$ means $x \ge -2$. But $x = 2$ is not in the domain, so the answer is $[-2, 2) \cup (2, \infty)$. The factor $x - 2$ cancels in the sign but not in the domain.

</div>

<div class="warning" markdown>

Watch out: a repeated factor does not change the sign. Solve $(x + 2)(x - 1)^2(x - 3) \ge 0$. The zeros are $-2$, $1$ (power 2) and $3$. The signs from left to right are $+, -, -, +$: no flip at $x = 1$. The answer includes all the zeros: $(-\infty, -2] \cup \{1\} \cup [3, \infty)$. The single point $x = 1$ appears because the expression is exactly 0 there. For the strict inequality $> 0$ the answer is $(-\infty, -2) \cup (3, \infty)$, with 1 left out.

</div>

Some inequalities have no solution or every number as a solution. The inequality $x^2 + 1 > 0$ is true for every real $x$, so the answer is $(-\infty, \infty)$. The inequality $x^2 < 0$ has no solution, and $x^2 \le 0$ has the one solution $x = 0$. An inequality $(x - 3)^2 > 0$ is true for every real number except 3, so its answer is $(-\infty, 3) \cup (3, \infty)$. A quadratic with no real zeros has the same sign everywhere, so a single test number decides it.

If the numerator and denominator both contain only factors that never change sign, such as $\frac{x^2 + 1}{x^2 + 4}$, the expression is positive everywhere and there are no critical numbers to find.

## Tricks and shortcuts

Start at the right end. For large positive $x$ the sign of the whole expression is the sign of the ratio of the leading coefficients of the numerator and the denominator. Move left across each critical number, flipping the sign when the factor has an odd power and keeping it when the power is even. One test number at the end confirms the pattern.

For a quadratic, use the picture. When $a > 0$ the parabola $ax^2 + bx + c$ opens up, so it is negative between its two zeros and positive outside them: $(x - r)(x - s) < 0$ means between $r$ and $s$, and $> 0$ means outside. When $a < 0$ the picture flips.

To combine "and" with a rational inequality, as in a compound inequality, solve each piece and intersect the answers; for "or", take the union ([compound inequalities](../01-algebra-foundations/03-compound-inequalities-and-interval-notation.md)). Practice problem 8 does this.

## In code

SymPy solves an inequality in one variable exactly. A numeric scan with exact fractions is the sign chart done by machine: test one number from each interval.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction
from sympy import symbols, solve_univariate_inequality

x = symbols("x", real=True)

expr = (x**2 - x - 6) / (x**2 - 1)
print(solve_univariate_inequality(expr >= 0, x, relational=False))
# Union(Interval(-oo, -2), Interval.open(-1, 1), Interval(3, oo))

print(solve_univariate_inequality(3/(x - 2) >= 1, x, relational=False))
# Interval.Lopen(2, 5)

def f(t):
    return Fraction(t*t - t - 6, t*t - 1)

tests = [-3, Fraction(-3, 2), 0, 2, 4]        # one number from each interval
print([f(t) > 0 for t in tests])              # [True, False, True, False, True]
```

The first two answers match Example 2 and the Quick check. The list at the end is the sign chart: the quotient is positive on the first, third and fifth intervals. SymPy reports the endpoints of the answer as open or closed using the same rules as this lesson.

</details>

## FAQ

### Why can the sign change only at a critical number?

A fraction of polynomials is positive, negative, 0 or undefined, and to go from positive to negative it has to pass through 0 or through an undefined point, since polynomial graphs have no jumps. The zeros of the numerator are where it equals 0, and the zeros of the denominator are where it is undefined. That is the sign constancy theorem above.

### Why is a zero of the denominator never part of the answer, even for $\le$?

Because the expression is not defined there, so the inequality is neither true nor false at that number. A $\le$ allows equality with 0, and the expression never equals 0 at a number where it is undefined. In the answer, such an endpoint always gets a parenthesis.

### What if I cannot factor the numerator?

Find its zeros another way, with the quadratic formula or a numerical method ([solving quadratic equations](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md)), and use those decimal or exact numbers as critical numbers. If the polynomial has no real zeros, such as $x^2 + 1$, it has one sign everywhere, and you can drop it from the chart after checking that sign with one number.

### Can I solve this from a graph instead?

Yes. The inequality $f(x) > 0$ is the question of where the graph of $f$ is above the $x$-axis, and $f(x) > g(x)$ is where one graph is above the other. A sketch from [rational functions and asymptotes](02-rational-functions-and-asymptotes.md) shows the answer, and the sign chart is the exact version. If the critical numbers are close together, the chart is more reliable than a sketch.

## Practice

### Warm-up

1\. Solve and write the answer in interval notation: (a) $(x - 1)(x + 4) > 0$, (b) $x^2 - 9 \le 0$, (c) $x^2 + 4 > 0$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The zeros are $-4$ and $1$. The parabola opens up, so the product is positive outside the zeros: $(-\infty, -4) \cup (1, \infty)$.
- (b) $x^2 - 9 = (x - 3)(x + 3)$, negative between $-3$ and $3$, and 0 at the ends, which are included: $[-3, 3]$.
- (c) $x^2 + 4 \ge 4$ for every real $x$, so it is always positive: $(-\infty, \infty)$.

Check: (a) at $x = 2$: $1 \cdot 6 = 6 > 0$ and at $x = 0$: $-4 < 0$. (b) at $x = 0$: $-9 \le 0$, and at $x = 4$: $7 > 0$. (c) at $x = 0$: $4 > 0$.

</details>

2\. Solve (a) $\dfrac{x + 1}{x - 3} < 0$ and (b) $\dfrac{x - 2}{x + 5} \ge 0$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The critical numbers are $-1$ and $3$, and the signs are $+, -, +$. We want negative, and both ends are excluded because of the strict inequality (and 3 is a denominator zero): $(-1, 3)$.

(b) The critical numbers are $-5$ (denominator) and $2$ (numerator). The signs are $+, -, +$. We want $\ge 0$: the positive intervals, with $2$ included and $-5$ excluded: $(-\infty, -5) \cup [2, \infty)$.

Check: (a) at $x = 0$: $\frac{1}{-3} < 0$ yes, and at $x = 4$: $\frac{5}{1} > 0$, so 4 is out. (b) at $x = 2$: $0 \ge 0$ yes, at $x = 0$: $\frac{-2}{5} < 0$, so 0 is out, and at $x = -6$: $\frac{-8}{-1} = 8 \ge 0$, so $-6$ is in.

</details>

3\. Solve $x^3 - 4x \ge 0$.

<details class="solution" markdown>
<summary>Solution</summary>

Factor: $x(x - 2)(x + 2) \ge 0$. The critical numbers are $-2$, $0$ and $2$. The sign at the far right is $+$, and it flips at each, so from left to right the signs are $-, +, -, +$. We want $\ge 0$, so we take the positive intervals and include the zeros: $[-2, 0] \cup [2, \infty)$.

Check: at $x = -1$: $-1 + 4 = 3 \ge 0$, in. At $x = 1$: $1 - 4 = -3$, out. At $x = 3$: $27 - 12 = 15$, in. At $x = -3$: $-27 + 12 = -15$, out.

</details>

### Standard

4\. Solve $\dfrac{2x}{x + 1} \le 1$.

<details class="solution" markdown>
<summary>Solution</summary>

Move 1 to the left and combine: $\frac{2x - (x + 1)}{x + 1} = \frac{x - 1}{x + 1} \le 0$. The critical numbers are $-1$ (denominator) and $1$ (numerator). The signs are $+, -, +$. We want negative or zero: between them, with 1 included and $-1$ excluded. The answer is $(-1, 1]$.

Check: at $x = 0$: $0 \le 1$, yes. At $x = 1$: $\frac{2}{2} = 1 \le 1$, yes. At $x = -2$: $\frac{-4}{-1} = 4$, not at most 1, so $-2$ is out. At $x = 3$: $\frac{6}{4} = 1.5$, out.

</details>

5\. Solve $\dfrac{1}{x - 1} \ge \dfrac{1}{x + 2}$.

<details class="solution" markdown>
<summary>Solution</summary>

Move one term and use the LCD $(x - 1)(x + 2)$: $\frac{(x + 2) - (x - 1)}{(x - 1)(x + 2)} = \frac{3}{(x - 1)(x + 2)} \ge 0$. The numerator is the constant 3, which is never 0, so the only critical numbers are $-2$ and $1$, both from the denominator, and neither is included. The quotient is positive when the two factors have the same sign: $x < -2$ or $x > 1$. The answer is $(-\infty, -2) \cup (1, \infty)$.

Check: $x = 2$: $1 \ge \frac{1}{4}$, yes. $x = -3$: $-\frac{1}{4} \ge -1$, yes. $x = 0$: $-1 \ge \frac{1}{2}$, no.

</details>

6\. A company's daily profit is $P(q) = -2q^2 + 140q - 2400$ dollars. (a) For which $q$ is the profit positive? (b) Can the profit reach \$100?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Divide by $-2$ and flip: $q^2 - 70q + 1200 < 0$. Factor: $(q - 30)(q - 40) < 0$, so the profit is positive for $30 < q < 40$.

(b) Complete the square: $P(q) = -2(q^2 - 70q) - 2400 = -2(q - 35)^2 + 2450 - 2400 = -2(q - 35)^2 + 50$. Since $(q - 35)^2 \ge 0$, we get $P(q) \le 50$, so the profit never reaches \$100. The best profit is \$50, at $q = 35$.

Check: $P(35) = -2450 + 4900 - 2400 = 50$. Also $P(30) = -1800 + 4200 - 2400 = 0$ and $P(40) = -3200 + 5600 - 2400 = 0$.

</details>

### Challenge

7\. (a) Solve $\dfrac{x}{x - 1} > 2$. (b) Explain what goes wrong if you multiply both sides by $x - 1$ and solve $x > 2(x - 1)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Move 2 to the left: $\frac{x - 2(x - 1)}{x - 1} = \frac{2 - x}{x - 1} > 0$. The critical numbers are 1 and 2. For $x < 1$ the top is positive and the bottom is negative, so the quotient is negative. For $1 < x < 2$ both are positive, so the quotient is positive. For $x > 2$ the top is negative and the bottom is positive, so it is negative. The answer is $(1, 2)$.

(b) Multiplying by $x - 1$ gives $x > 2x - 2$, so $x < 2$. That treats $x - 1$ as positive and it isn't always. The result $x < 2$ includes numbers below 1 such as $x = 0$, where $\frac{0}{-1} = 0$ is not greater than 2. Under the assumption $x - 1 > 0$, $x < 2$ is correct and gives $1 < x < 2$. For $x - 1 < 0$ the inequality should flip, giving $x > 2$, which contradicts $x < 1$ and gives nothing.

Check (a): $x = 1.5$: $\frac{1.5}{0.5} = 3 > 2$. $x = 3$: $\frac{3}{2} = 1.5$, not greater than 2. $x = 0$: $0$, not greater than 2.

</details>

8\. (Reviews [compound inequalities](../01-algebra-foundations/03-compound-inequalities-and-interval-notation.md).) Solve $1 < \dfrac{x + 3}{x - 1} \le 3$.

<details class="solution" markdown>
<summary>Solution</summary>

This means "$\frac{x + 3}{x - 1} > 1$ and $\frac{x + 3}{x - 1} \le 3$", so intersect the two solution sets.

First piece: $\frac{x + 3}{x - 1} - 1 = \frac{4}{x - 1} > 0$, which holds for $x > 1$. Second piece: $\frac{x + 3}{x - 1} - 3 = \frac{6 - 2x}{x - 1} \le 0$. The critical numbers are 1 (denominator) and 3 (numerator). The signs are $-, +, -$, so the second set is $(-\infty, 1) \cup [3, \infty)$.

The intersection of $(1, \infty)$ with $(-\infty, 1) \cup [3, \infty)$ is $[3, \infty)$.

Check: $x = 3$: $\frac{6}{2} = 3$, which is in $(1, 3]$. $x = 5$: $\frac{8}{4} = 2$, in. $x = 2$: $\frac{5}{1} = 5$, which is above 3, so out. $x = 0$: $\frac{3}{-1} = -3$, below 1, so out.

</details>

## Where this shows up

- Calculus asks the same question of derivatives: a function is increasing where its derivative is positive, so finding where it rises or falls is a sign chart of the derivative (the mean value theorem and extrema<!-- link: ../../05-university-core/03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md -->). Domains of functions with roots and logarithms, and intervals of convergence for series, are also inequalities of this kind.
- In computer science, deciding when one running time beats another is a polynomial inequality. For example, $n^2 > 100n$ factors as $n(n - 100) > 0$, which is true for $n > 100$ when $n > 0$: that is the crossover point in asymptotic notation<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md -->.
- In economics, break-even and profitable ranges are polynomial inequalities, as in Example 3, and a target for average cost is a rational inequality, as in Example 4 (production and cost functions<!-- link: ../../07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md -->). The domain of a logarithm is also an inequality, since its argument must be positive, which comes back in [exponential and logarithmic equations](../07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md).
