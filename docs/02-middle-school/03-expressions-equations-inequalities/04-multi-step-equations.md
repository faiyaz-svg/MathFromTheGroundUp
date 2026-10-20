# Multi-step equations

After this lesson you can solve linear equations with brackets, fractions and the variable on both sides, recognize an equation that has no solution or that every number solves, and explain why dividing both sides by an expression that might be 0 can lose a solution.

Before this: [one- and two-step equations](03-one-and-two-step-equations.md), [equivalent expressions](02-equivalent-expressions.md), and [adding and subtracting fractions](../../01-elementary/10-adding-and-subtracting-fractions.md) for the least common denominator.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $5x - 4 = 2x + 11$.
2. Solve $\frac{x}{3} + \frac{x - 1}{4} = 2$.
3. How many solutions does $2(x + 3) = 2x + 5$ have?

<details class="solution" markdown>
<summary>Answers</summary>

1. $x = 5$. Subtract $2x$ to get $3x - 4 = 11$, then $3x = 15$. Check: $25 - 4 = 21$ and $10 + 11 = 21$.
2. $x = \frac{27}{7}$. Multiply both sides by 12 to get $4x + 3(x - 1) = 24$, so $7x - 3 = 24$ and $7x = 27$.
3. None. Expanding gives $2x + 6 = 2x + 5$, and subtracting $2x$ leaves $6 = 5$, which is false for every $x$.

</details>

## The idea

The car-share company from [variables and expressions](01-variables-and-expressions.md) charges \$5 to unlock and \$0.40 a minute. A rival charges \$2 to unlock and \$0.55 a minute. For a trip of $t$ minutes the costs are $5 + 0.40t$ and $2 + 0.55t$ dollars, and a few values show that neither is always cheaper:

| Minutes $t$ | First company, $5 + 0.40t$ | Rival, $2 + 0.55t$ |
|---|---|---|
| $10$ | $9.00$ | $7.50$ |
| $20$ | $13.00$ | $13.00$ |
| $30$ | $17.00$ | $18.50$ |

The rival is cheaper for short trips and dearer for long ones, and the two cost the same at some trip length. To find it without guessing, set the costs equal:

$$
5 + 0.40t = 2 + 0.55t.
$$

The unknown now appears on both sides. Subtract $0.40t$ from both sides, which leaves $5 = 2 + 0.15t$. That is a two-step equation: subtract 2 to get $3 = 0.15t$, and divide by $0.15$ to get $t = 20$. The costs match for a 20-minute trip, as the table shows.

Every equation in this lesson goes the same way. Tidy each side with the moves from [equivalent expressions](02-equivalent-expressions.md), gather the variable on one side with the both-sides moves from [one- and two-step equations](03-one-and-two-step-equations.md), and finish as before. Something new can happen in the gathering step, though. If the two companies charged the same rate per minute, the $t$ terms would cancel, and what remained would decide everything: different unlock fees would mean the costs never match, and equal ones would mean they always do.

## Definitions

A **linear equation** in one variable $x$ is an equation that can be rearranged, by expanding, combining like terms and doing the same operation to both sides, into the form $ax = b$ for some numbers $a$ and $b$.

In plain words, once the brackets are expanded, the variable appears only to the first power: never squared, never in a denominator, never under a root. The equations $3(x - 1) = 5x + \frac{x}{2}$ and $5 + 0.40t = 2 + 0.55t$ are linear, while $x^2 = 3x$ and $\frac{1}{x} = 2$ are not. Some books also require $a \ne 0$ in the definition; this lesson allows $a = 0$ so that it can treat every outcome together.

**Clearing fractions** means multiplying both sides of an equation by a common denominator of all its fractions, usually the least common denominator (LCD), so that no fractions remain. It is the both-sides rule with $c$ equal to the LCD, which is not 0, so the new equation has the same solutions.

An equation with no solution has an empty solution set, written $\emptyset$, the set with no elements ([sets and set operations](../../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md)). An equation that every number solves is an identity, as defined in [equivalent expressions](02-equivalent-expressions.md#definitions).

## How to do it

### A strategy for every linear equation

1. Clear fractions: multiply both sides by the LCD of all the denominators. Multiply every term, including the terms without fractions. Clear decimals the same way, by multiplying by 10 or 100.
2. Expand every bracket with the distributive property, minding the sign in front.
3. Combine like terms on each side.
4. Gather the variable terms on one side and the constant terms on the other, by adding or subtracting the same term on both sides. Gathering on the side whose variable term has the larger coefficient keeps the coefficient positive.
5. Divide both sides by the coefficient of the variable. If the variable terms cancelled in Step 4, there is nothing to divide by; read the result with the theorem below.
6. Check by substituting into the original equation, working out each side separately.

Steps 1 to 3 change the expressions on each side into equivalent expressions, and Steps 4 and 5 change the equation into an equivalent equation. Either way the solutions are kept, so the method never loses or adds a solution, provided you never divide by something that could be 0.

### The three possible outcomes

*Theorem.* Let $a$ and $b$ be numbers. The equation $ax = b$ has

1. exactly one solution, $x = \frac{b}{a}$, if $a \ne 0$,
2. no solution, if $a = 0$ and $b \ne 0$,
3. every number as a solution, if $a = 0$ and $b = 0$.

We know the both-sides theorem from [one- and two-step equations](03-one-and-two-step-equations.md#why-the-same-operation-on-both-sides-keeps-the-solutions) and the zero property, $0 \cdot x = 0$ for every $x$. We want the solution set of $ax = b$ in every case. The plan is a proof by cases: either $a \ne 0$ or $a = 0$, and proving the result in each case covers every possibility (proof by cases and WLOG<!-- link: ../../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md -->).

*Proof.* Suppose first that $a \ne 0$. Then dividing both sides by $a$ is allowed, and it gives the equivalent equation $x = \frac{b}{a}$. Its only solution is $\frac{b}{a}$, so the same is true of $ax = b$.

Now suppose $a = 0$. The equation reads $0 \cdot x = b$, and since $0 \cdot x = 0$ for every $x$, it says $0 = b$, whatever $x$ is. If $b \ne 0$, that statement is false for every $x$, so there is no solution. If $b = 0$, it is $0 = 0$, which is true for every $x$, so every number is a solution.

Look back: in practice you never write $0x = b$. You see the variable terms cancel in Step 4 and a statement with no variable left over. A false statement, such as $6 = 5$, means no solution; a true statement, such as $0 = 0$ or $2 = 2$, means every number is a solution. Since every linear equation can be brought to the form $ax = b$, a linear equation has exactly one solution, none or infinitely many. It never has exactly two.

### Dividing by an expression that might be zero

Solve $5x = 3x$. Dividing both sides by $x$ gives $5 = 3$, which is false and suggests that there is no solution. But $x = 0$ works: $5 \cdot 0 = 3 \cdot 0$ says $0 = 0$, which is true.

The division went wrong because dividing by $x$ is allowed only when $x \ne 0$. The step assumed, without saying so, that $x$ is not 0, and that assumption threw away the one solution. The safe way gathers the terms instead: subtract $3x$ from both sides to get $2x = 0$, and divide by the number 2 to get $x = 0$.

The rule is to divide both sides only by a number you know is not 0. If you want to divide by an expression that contains the variable, split into two cases, one where the expression is 0 and one where it isn't, and solve each. The same trap returns with $x^2 = 3x$, where dividing by $x$ gives $x = 3$ and loses $x = 0$ ([solving quadratic equations](../../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md)). Multiplying both sides by an expression that might be 0 has the opposite danger: it can add solutions that the original equation doesn't have ([rational and radical equations](../../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md)).

## Worked examples

<div class="example" markdown>

### Example 1: brackets and the variable on both sides

Solve $4(x - 3) - (2x - 5) = 3(x + 1) - 14$.

Step 1: there are no fractions.

Step 2: expand. On the left, $4(x - 3) = 4x - 12$, and the minus sign in front of the second bracket changes both of its signs: $-(2x - 5) = -2x + 5$. On the right, $3(x + 1) = 3x + 3$:

$$
4x - 12 - 2x + 5 = 3x + 3 - 14.
$$

Step 3: combine like terms on each side. The left side is $2x - 7$ and the right side is $3x - 11$:

$$
2x - 7 = 3x - 11.
$$

Step 4: the larger coefficient, 3, is on the right, so gather the variable there. Subtract $2x$ from both sides, then add 11 to both sides:

$$
\begin{aligned}
-7 &= x - 11 && \text{subtract } 2x \text{ from both sides} \\
4 &= x && \text{add 11 to both sides}
\end{aligned}
$$

Step 5: the coefficient of $x$ is already 1, so the solution is $x = 4$.

Step 6: check in the original equation. The left side is $4(4 - 3) - (8 - 5) = 4 - 3 = 1$, and the right side is $3(5) - 14 = 15 - 14 = 1$. Both sides are 1.

</div>

<div class="example" markdown>

### Example 2: clearing fractions

Solve $\frac{x + 2}{3} - \frac{x}{4} = \frac{1}{2}$.

Step 1: the denominators are 3, 4 and 2, and their LCD is 12. Multiply every term on both sides by 12:

$$
12 \cdot \frac{x + 2}{3} - 12 \cdot \frac{x}{4} = 12 \cdot \frac{1}{2}.
$$

Since $12 \div 3 = 4$, $12 \div 4 = 3$ and $12 \div 2 = 6$, this is

$$
4(x + 2) - 3x = 6.
$$

<div class="warning" markdown>

Watch out: keep the brackets around a numerator with two terms. The 4 multiplies the whole numerator $x + 2$, so it is $4(x + 2) = 4x + 8$. Writing $4x + 2$ multiplies only the $x$ and gives the wrong answer $x = 4$.

</div>

Steps 2 and 3: expand and combine, $4x + 8 - 3x = 6$, so $x + 8 = 6$.

Steps 4 and 5: subtract 8 from both sides, and $x = -2$.

Step 6: in the original, the left side is $\frac{-2 + 2}{3} - \frac{-2}{4} = 0 + \frac{1}{2} = \frac{1}{2}$, which is the right side.

</div>

<div class="example" markdown>

### Example 3: no solution, and every number

Solve (a) $3(x + 2) - x = 2x + 5$ and (b) $4(x - 1) + 6 = 2(2x + 1)$.

(a) Expanding and combining gives $2x + 6 = 2x + 5$. Subtract $2x$ from both sides: $6 = 5$. The variable is gone and the statement left is false, so by the theorem there is no solution. The solution set is $\emptyset$. Check one value anyway: at $x = 0$, the left side is 6 and the right side is 5.

(b) Expanding and combining gives $4x + 2 = 4x + 2$. Subtract $4x$ from both sides: $2 = 2$. The statement is true and no variable is left, so every number is a solution, and the equation is an identity. Check two values: at $x = 0$ both sides are 2, and at $x = 10$ both sides are 42.

In both parts the two sides had the same coefficient of $x$ after Step 3. That is the sign to look for: the constants then decide between no solution and every number.

</div>

<div class="example" markdown>

### Example 4: two fractions set equal (finish it yourself)

Solve $\frac{2x - 1}{5} = \frac{x + 4}{3}$.

Step 1: the LCD of 5 and 3 is 15. Multiplying both sides by 15 gives $3(2x - 1) = 5(x + 4)$.

Step 2: expanding gives $6x - 3 = 5x + 20$.

Step 3: each side is already combined.

Now do Steps 4 and 5, and check the answer in the original equation.

<details class="solution" markdown>
<summary>Finish</summary>

Step 4: the larger coefficient, 6, is on the left. Subtract $5x$ from both sides to get $x - 3 = 20$, then add 3 to both sides to get $x = 23$.

Step 5: the coefficient is 1, so $x = 23$.

Step 6: the left side is $\frac{46 - 1}{5} = \frac{45}{5} = 9$, and the right side is $\frac{23 + 4}{3} = \frac{27}{3} = 9$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: clearing fractions multiplies every term, including the ones without a fraction. In $\frac{x}{2} + 3 = 5$, multiplying by 2 gives $x + 6 = 10$, so $x = 4$. Writing $x + 3 = 10$ leaves the 3 unmultiplied and gives $x = 7$, and the check fails: $\frac{7}{2} + 3 = 6.5$, not 5.

</div>

<div class="warning" markdown>

Watch out for a subtracted fraction with a sum on top. In $\frac{x}{3} - \frac{x - 1}{4} = 2$, multiplying by 12 turns the second term into $-3(x - 1) = -3x + 3$. Writing $-3x - 1$ changes one sign and forgets to multiply the other term. The fraction bar groups like brackets, so keep the brackets until you expand.

</div>

<div class="warning" markdown>

Watch out: three different answers sound alike. "The solution is 0" means one solution, the number 0, as in $5x = 3x$. "No solution" means the solution set is empty, as in $6 = 5$. "Every number is a solution" means the equation is an identity, as in $0 = 0$. Reaching $0 = 0$ does not mean $x = 0$.

</div>

When you gather terms, subtract the term from both sides; don't move it across and keep its sign. From $2x - 7 = 5x + 8$, subtracting $5x$ from both sides gives $-3x - 7 = 8$, then $-3x = 15$ and $x = -5$. Moving the $5x$ to the left without changing its sign gives $7x - 7 = 8$, which leads to the wrong answer $x = \frac{15}{7}$. Check: $2(-5) - 7 = -17$ and $5(-5) + 8 = -17$.

Untidy solutions such as $x = \frac{27}{7}$ are common, and a check with fractions is still possible: substitute and work with fractions rather than rounded decimals, as in Practice problem 5.

## Tricks and shortcuts

Gather the variable on the side with the larger coefficient, as in Examples 1 and 4. The coefficient then stays positive, and you never divide by a negative number. The habit pays off in [inequalities](05-inequalities.md), where dividing by a negative flips the sign.

Spot the special cases early. If, after Step 3, both sides have the same coefficient of $x$, the answer is either no solution or every number, and comparing the constants tells you which. In $7x + 2 = 7x - 9$ the constants differ, so there is no solution.

Cross-multiplying is clearing fractions in one move. For $\frac{a}{b} = \frac{c}{d}$, multiplying both sides by $bd$ gives $ad = bc$, and that is the rule from [proportional relationships](../02-ratios-rates-percents/02-proportional-relationships.md). It works only when each side is a single fraction, as in Example 4, and not when a side has two terms, as in Example 2.

## In code

Sympy's `solveset` returns the solution set itself, so it distinguishes the three outcomes. Its older function `solve` returns an empty list both when there is no solution and when every number is one.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import symbols, Eq, solve, solveset, S

x = symbols("x")
one = Eq(4*(x - 3) - (2*x - 5), 3*(x + 1) - 14)   # Example 1
no_sol = Eq(3*(x + 2) - x, 2*x + 5)               # Example 3(a)
every = Eq(4*(x - 1) + 6, 2*(2*x + 1))            # Example 3(b)

for eq in [one, no_sol, every]:
    print(solveset(eq, x, S.Reals), solve(eq, x))
# {4} [4]
# EmptySet []
# Reals []
```

`S.Reals` tells `solveset` to look for real solutions, and `Reals` in the output is the set of all real numbers. Sympy expands both sides of `every` to $4x + 2$ as soon as the equation is built, so `every` is already the value `True` before it is solved.

</details>

## FAQ

### Is "no solution" the same as "the solution is 0"?

No. The equation $2x = 0$ has a solution, the number 0, and its solution set is $\{0\}$. The equation $2x + 1 = 2x$ has no solution, and its solution set is $\emptyset$. Substitution tells them apart: 0 makes $2x = 0$ true, but no number makes $2x + 1 = 2x$ true, because the left side is always 1 more than the right.

### Where does the "proof" that 2 equals 1 go wrong?

Here is the argument. Let $x$ and $y$ be equal numbers. Then $2x - 2y = x - y$, since both sides are 0. Factoring each side gives $2(x - y) = 1(x - y)$, and dividing both sides by $x - y$ gives $2 = 1$. Every step is valid except the last: since $x = y$, the expression $x - y$ is 0, and the last step divides by 0. It is the trap from [dividing by an expression that might be zero](#dividing-by-an-expression-that-might-be-zero), in disguise.

### Does it matter which side I gather the variable on?

Not for the answer. Gathering on either side produces equivalent equations, so both routes reach the same solution. In Example 1, gathering on the left gives $-x - 7 = -11$, then $-x = -4$ and $x = 4$, the same as before with one more sign to handle. The side with the larger coefficient is just the route with fewer negatives.

## Practice

### Warm-up

1\. Solve $7x + 3 = 4x - 9$.

<details class="solution" markdown>
<summary>Solution</summary>

Subtract $4x$ from both sides: $3x + 3 = -9$. Subtract 3: $3x = -12$. Divide by 3: $x = -4$.

Check: the left side is $7(-4) + 3 = -25$, and the right side is $4(-4) - 9 = -25$.

</details>

2\. Solve $2(x - 5) = 3x + 1$.

<details class="solution" markdown>
<summary>Solution</summary>

Expand: $2x - 10 = 3x + 1$. The larger coefficient is on the right, so subtract $2x$ from both sides: $-10 = x + 1$. Subtract 1: $x = -11$.

Check: the left side is $2(-11 - 5) = 2(-16) = -32$, and the right side is $3(-11) + 1 = -32$.

</details>

3\. Solve $\frac{x}{2} + \frac{x}{3} = 10$.

<details class="solution" markdown>
<summary>Solution</summary>

The LCD of 2 and 3 is 6. Multiply every term by 6: $3x + 2x = 60$. Combine: $5x = 60$. Divide by 5: $x = 12$.

Check: $\frac{12}{2} + \frac{12}{3} = 6 + 4 = 10$.

</details>

### Standard

4\. Solve $5 - 2(3 - x) = 4(x + 1) - 3$.

<details class="solution" markdown>
<summary>Solution</summary>

Expand with the multiplier $-2$ on the left: $5 - 6 + 2x$, which is $2x - 1$. On the right, $4x + 4 - 3 = 4x + 1$. So $2x - 1 = 4x + 1$.

Gather on the right, where the coefficient is larger. Subtract $2x$: $-1 = 2x + 1$. Subtract 1: $-2 = 2x$. Divide by 2: $x = -1$.

Check: the left side is $5 - 2(3 - (-1)) = 5 - 8 = -3$, and the right side is $4(0) - 3 = -3$.

</details>

5\. Solve $\frac{3x - 1}{4} - \frac{x + 2}{6} = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

The LCD of 4 and 6 is 12. Multiply every term by 12, keeping brackets around the numerators: $3(3x - 1) - 2(x + 2) = 12$. Expand: $9x - 3 - 2x - 4 = 12$. Combine: $7x - 7 = 12$. Add 7: $7x = 19$. Divide by 7: $x = \frac{19}{7}$.

Check with fractions. First, $3x - 1 = \frac{57}{7} - \frac{7}{7} = \frac{50}{7}$, so the first term is $\frac{50}{7} \div 4 = \frac{50}{28} = \frac{25}{14}$. Next, $x + 2 = \frac{19}{7} + \frac{14}{7} = \frac{33}{7}$, so the second term is $\frac{33}{7} \div 6 = \frac{33}{42} = \frac{11}{14}$. Then $\frac{25}{14} - \frac{11}{14} = \frac{14}{14} = 1$, the right side.

</details>

6\. Decide how many solutions each equation has, and find them: (a) $3(2x - 1) = 6x - 3$, (b) $5x - (2x + 4) = 3(x - 1)$, (c) $2(x + 4) = 8 - x$. (d) For which number $k$ is $3(x + k) = 3x + 12$ an identity, and what happens for every other $k$?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Expanding gives $6x - 3 = 6x - 3$, and subtracting $6x$ leaves $-3 = -3$, which is true. Every number is a solution: the equation is an identity.

(b) The left side is $5x - 2x - 4 = 3x - 4$, and the right side is $3x - 3$. Subtracting $3x$ leaves $-4 = -3$, which is false. There is no solution.

(c) Expanding gives $2x + 8 = 8 - x$. Add $x$ to both sides: $3x + 8 = 8$. Subtract 8: $3x = 0$. Divide by 3: $x = 0$. There is exactly one solution, the number 0.

(d) Expanding gives $3x + 3k = 3x + 12$, and subtracting $3x$ leaves $3k = 12$. If $k = 4$ this is $12 = 12$, true, so the equation is an identity. For every other $k$ it is false, so the equation has no solution.

Check: (a) at $x = 1$ both sides are 3. (b) At $x = 0$ the left side is $-4$ and the right side is $-3$. (c) At $x = 0$ both sides are 8. (d) With $k = 4$, at $x = 1$ both sides are 15; with $k = 5$, at $x = 1$ the left side is 18 and the right side is 15.

</details>

### Challenge

7\. One print shop charges \$18 to set up a job plus \$0.35 a page. Another charges \$6 to set up plus \$0.50 a page. (a) For how many pages do the two cost the same? (b) Which shop is cheaper for a 100-page job, and by how much?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Let $n$ be the number of pages. The costs in dollars are $18 + 0.35n$ and $6 + 0.50n$, so set them equal:

$$
18 + 0.35n = 6 + 0.50n.
$$

Clear the decimals by multiplying both sides by 100: $1800 + 35n = 600 + 50n$. Gather on the right, where the coefficient is larger: subtract $35n$ to get $1800 = 600 + 15n$, then subtract 600 to get $1200 = 15n$, so $n = 80$. The two shops cost the same for 80 pages.

(b) At 100 pages the first shop costs $18 + 35 = 53$ dollars and the second costs $6 + 50 = 56$ dollars. The first shop is cheaper by \$3. That fits the equation: past 80 pages, the lower price per page outweighs the higher set-up fee.

Check (a): at 80 pages, $18 + 0.35 \times 80 = 18 + 28 = 46$ and $6 + 0.50 \times 80 = 6 + 40 = 46$.

</details>

8\. This one reviews [percents](../02-ratios-rates-percents/03-percents.md). A store raises a price by 20%, then takes \$12 off. The result is 90% of the original price. What was the original price?

<details class="solution" markdown>
<summary>Solution</summary>

Let $p$ be the original price in dollars. Raising it by 20% gives $1.2p$, taking \$12 off gives $1.2p - 12$, and 90% of the original is $0.9p$. So

$$
1.2p - 12 = 0.9p.
$$

Multiply both sides by 10 to clear the decimals: $12p - 120 = 9p$. Subtract $9p$: $3p - 120 = 0$. Add 120: $3p = 120$. Divide by 3: $p = 40$. The original price was \$40.

Check with the words: 20% more than \$40 is \$48, and \$12 off leaves \$36, while 90% of \$40 is $0.9 \times 40 = 36$.

</details>

## Where this shows up

- The next lesson, [inequalities](05-inequalities.md), follows the same six steps with one new rule.
- [Systems of linear equations](../05-linear-relationships-and-functions/04-systems-of-linear-equations.md) are solved by turning two equations into one multi-step equation, and the three outcomes of the theorem return there as lines that cross once, never or everywhere. In linear algebra they become the three outcomes of Gaussian elimination (systems and Gaussian elimination<!-- link: ../../05-university-core/06-linear-algebra/02-systems-and-gaussian-elimination.md -->).
- In economics, a firm with \$500 of fixed costs, a cost of \$7 per unit and a price of \$12 per unit breaks even when revenue equals cost, $12n = 500 + 7n$, which gives $n = 100$ units. Setting supply equal to demand is the same move (supply and demand equilibrium algebra<!-- link: ../../07-economics-math/02-markets/03-supply-and-demand-equilibrium-algebra.md -->).
