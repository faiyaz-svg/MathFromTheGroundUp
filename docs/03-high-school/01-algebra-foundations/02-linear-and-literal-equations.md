# Linear and literal equations

After this lesson you can solve any linear equation in one variable quickly, solve a formula for any one of its letters, say when each step is allowed (dividing only by expressions known to be nonzero), and check the result by substitution.

Before this: [multi-step equations](../../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md) and [real numbers, axioms and set notation](01-real-numbers-axioms-and-set-notation.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $3(2x - 5) - 4(x - 1) = 7 - (x + 2)$.
2. Solve $A = P(1 + rt)$ for $t$. For which values of $P$ and $r$ is your answer valid?
3. Solve $y = mx + b$ for $x$, and say what happens when $m = 0$.

<details class="solution" markdown>
<summary>Answers</summary>

1. $x = \frac{16}{3}$. The left side expands to $2x - 11$ and the right side to $5 - x$, so $3x = 16$. Check: $2 \cdot \frac{16}{3} - 11 = -\frac{1}{3}$ and $5 - \frac{16}{3} = -\frac{1}{3}$.
2. $t = \frac{A - P}{Pr}$, valid when $P \ne 0$ and $r \ne 0$. Divide by $P$, subtract 1, divide by $r$.
3. $x = \frac{y - b}{m}$, valid when $m \ne 0$. If $m = 0$ the equation says $y = b$, which is true for every $x$ when $y = b$ and for no $x$ otherwise.

</details>

## The idea

You put \$2,000 into an account that pays 3% simple interest a year. After $t$ years it holds $A = 2000(1 + 0.03t)$ dollars. To find when it reaches \$2,150 you solve $2150 = 2000(1 + 0.03t)$, a multi-step equation, and get $t = 2.5$ years. Now suppose you want the same answer for \$3,000 at 2.5%, then for \$500 at 4%, and so on down a column of a spreadsheet. Redoing the algebra each time is wasteful. Solve the formula once, for $t$, and each case becomes one substitution.

A formula such as $A = P(1 + rt)$ is an equation whose numbers are replaced by letters. Solving it for $t$ uses the same rules as solving $2150 = 2000(1 + 0.03t)$, because the letters $A$, $P$ and $r$ stand for numbers that haven't been chosen yet. Two things are new. The answer is an expression, such as $\frac{A - P}{Pr}$, not a single number. And since the other letters could take any value, a step such as "divide by $P$" works only when $P \ne 0$. A good answer says so.

The same skill turns a formula around. The temperature formula $C = \frac{5}{9}(F - 32)$ converts Fahrenheit to Celsius. If your oven thermometer reads in Celsius and the recipe is in Fahrenheit, you want the formula with $F$ alone on one side.

## Definitions

A **formula** is an equation that relates several quantities, each written as a letter, such as $A = P(1 + rt)$ or $y = mx + b$. An equation whose quantities are letters, with several unknowns in it, is also called a **literal equation**.

To **solve a literal equation for a letter** (the **target letter**) means to write an equivalent equation of the form

$$
\text{target letter} = \text{an expression that doesn't contain the target letter}.
$$

In plain words, you get the target alone on one side, with everything else on the other. For example, $x = \frac{y - b}{m}$ solves $y = mx + b$ for $x$: the right side has no $x$ in it.

The solved form isn't always equivalent to the original for every value of the other letters. The equation $y = mx + b$ and the equation $x = \frac{y - b}{m}$ say the same thing when $m \ne 0$, and when $m = 0$ the second isn't even defined. A **restriction** is a condition on the other letters, such as $m \ne 0$, under which the solved form and the original have the same solutions. Solving a literal equation means finding the expression and stating the restrictions.

A linear equation in one variable $x$ is an equation that can be brought into the form $ax = b$, as defined in [multi-step equations](../../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#definitions). Every equation in this lesson is linear in its target letter, meaning the target appears only to the first power after expanding brackets. In $A = P(1 + rt)$ the equation is linear in $t$, in $P$ and in $r$, though it isn't linear in all three together, since the product $Prt$ has three letters multiplied.

## How to do it

### Solving a linear equation quickly

1. Clear fractions and decimals. Multiply every term on both sides by the least common denominator, or by 10 or 100 for decimals. The multiplier is a nonzero number, so no solution is lost.
2. Expand the brackets. A minus sign in front of a bracket changes every sign inside it.
3. Combine like terms on each side.
4. Collect the variable terms on one side, by subtracting the smaller variable term from both sides, and the constants on the other.
5. Divide both sides by the coefficient of the variable. If the variable cancelled instead, a false statement means no solution and a true statement means every number is a solution.
6. Check in the original equation, evaluating each side separately.

When the variable appears only once, you can skip the expanding and work from the outside in. To solve $3(2x - 5) = 21$, divide both sides by 3 first, since the whole left side is 3 times a bracket: $2x - 5 = 7$, so $2x = 12$ and $x = 6$.

The general equation $ax + b = cx + d$ has a shortcut. It gives the three outcomes of the multi-step lesson in one statement.

*Theorem.* Let $a$, $b$, $c$ and $d$ be numbers. The equation $ax + b = cx + d$ has

1. exactly one solution, $x = \frac{d - b}{a - c}$, if $a \ne c$,
2. no solution, if $a = c$ and $b \ne d$,
3. every number as a solution, if $a = c$ and $b = d$.

We know the both-sides theorem from [one- and two-step equations](../../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#why-the-same-operation-on-both-sides-keeps-the-solutions), the distributive property, and the three outcomes of $kx = m$ from [multi-step equations](../../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#the-three-possible-outcomes). We want the solutions of $ax + b = cx + d$ in every case. The plan is to turn it into an equation of the form $kx = m$ and read off the three outcomes.

*Proof.* Subtract $cx + b$ from both sides. This keeps the solutions, and it gives $ax - cx = d - b$. The distributive property read from right to left turns the left side into $(a - c)x$, so the equation is $(a - c)x = d - b$. This has the form $kx = m$ with $k = a - c$ and $m = d - b$. The three outcomes of that equation are exactly the three cases: one solution $x = \frac{m}{k}$ when $k \ne 0$, none when $k = 0$ and $m \ne 0$, and every number when $k = 0$ and $m = 0$. $\blacksquare$

Look back: the proof is the strategy of the multi-step lesson with letters in place of numbers. Check the formula on $5x + 4 = 3x + 10$: it gives $x = \frac{10 - 4}{5 - 3} = 3$, and both sides are 19 at $x = 3$. The case $a = c$ is the one that needs care. It says that when the coefficients of $x$ match on both sides, the constants decide everything.

### Solving a formula for one letter

1. Mark the target letter. From here on, treat every other letter as a number whose value you don't know yet.
2. Clear fractions. Multiply both sides by the common denominator, and note that it must not be 0.
3. If the target appears once, undo the operations around it in the reverse of the order they were applied to it. The last operation applied is the first one undone.
4. If the target appears in more than one term, expand, gather all the terms with the target on one side and everything else on the other, and factor the target out (the distributive property, right to left).
5. Divide both sides by the coefficient of the target, and write the restriction that the coefficient is not 0. If the coefficient can be 0, solve that case separately: the equation then has no solution or every number as a solution, as in the theorem above.
6. Check with numbers. Choose values for the other letters, solve the resulting numeric equation directly, and compare it with your formula. Then substitute the formula back into the original and simplify.

Step 3 is the "peeling" habit. In $A = P(1 + rt)$, the target $t$ is first multiplied by $r$, then added to 1, then multiplied by $P$. Undo the multiplication by $P$ first (divide), then the addition of 1 (subtract), then the multiplication by $r$ (divide).

## Worked examples

<div class="example" markdown>

### Example 1: simple interest solved for time

Solve $A = P(1 + rt)$ for $t$, then use the result to find how long \$2,000 takes to grow to \$2,150 at 3% simple interest a year.

Step 1: the target is $t$. The other letters, $A$, $P$ and $r$, are treated as numbers.

Step 2: there are no fractions.

Step 3: the target appears once. The last operation applied to $t$ was multiplying by $P$, so divide both sides by $P$, which is allowed when $P \ne 0$:

$$
\frac{A}{P} = 1 + rt.
$$

Subtract 1 from both sides:

$$
\frac{A}{P} - 1 = rt.
$$

Divide both sides by $r$, which is allowed when $r \ne 0$:

$$
t = \frac{\frac{A}{P} - 1}{r}.
$$

Step 5: the coefficient of $t$ was $Pr$, and we divided by $P$ and by $r$, so the restrictions are $P \ne 0$ and $r \ne 0$. The result is solved, but a fraction inside a fraction is awkward. Multiply the top and bottom by $P$ (allowed, since $P \ne 0$), which gives

$$
t = \frac{A - P}{Pr}, \qquad P \ne 0,\ r \ne 0.
$$

Now the numbers: $A = 2150$, $P = 2000$ and $r = 0.03$ (the 3% written as a decimal):

$$
t = \frac{2150 - 2000}{2000 \times 0.03} = \frac{150}{60} = 2.5.
$$

So it takes 2.5 years.

Step 6: substitute into the original formula. $2000\,(1 + 0.03 \times 2.5) = 2000 \times 1.075 = 2150$, which is $A$. For a check on the formula itself, with $P = 100$, $r = 0.05$ and $t = 2$ we get $A = 110$, and the solved form gives $\frac{110 - 100}{100 \times 0.05} = \frac{10}{5} = 2$.

</div>

<div class="example" markdown>

### Example 2: market equilibrium solved for price

In a market, the quantity demanded at price $p$ is $Q = a - bp$ and the quantity supplied is $Q = c + dp$, where $a$, $b$, $c$ and $d$ are fixed numbers. The market clears at the price where the two quantities are equal. Solve for that price, then find it for demand $Q = 100 - 2p$ and supply $Q = 10 + p$.

Set the quantities equal: $a - bp = c + dp$. The target $p$ appears on both sides, so Step 4 applies. Collect the $p$ terms on the right and the other terms on the left. Add $bp$ and subtract $c$ on both sides:

$$
a - c = bp + dp.
$$

Factor $p$ out of the right side, which is the distributive property read from right to left:

$$
a - c = (b + d)\,p.
$$

Step 5: divide by $b + d$, which requires $b + d \ne 0$:

$$
p = \frac{a - c}{b + d}, \qquad b + d \ne 0.
$$

In economics $b$ and $d$ are positive, since demand falls and supply rises as the price rises, so $b + d$ is positive and the restriction holds. If $b + d = 0$ the two lines have the same slope, and by the theorem there is either no equilibrium or every price is one.

With $a = 100$, $b = 2$, $c = 10$ and $d = 1$: $p = \frac{100 - 10}{2 + 1} = 30$. The quantity is $Q = 100 - 2(30) = 40$.

Check: the supply at 30 is $10 + 30 = 40$, which matches the demand.

</div>

<div class="example" markdown>

### Example 3: when the coefficient could be zero

(a) Solve $y = mx + b$ for $x$. Subtract $b$ from both sides to get $y - b = mx$, then divide by $m$:

$$
x = \frac{y - b}{m}, \qquad m \ne 0.
$$

What if $m = 0$? The equation is $y = b$, with no $x$ left in it. If $y$ happens to equal $b$, every $x$ works. If not, no $x$ does. A horizontal line has the same $y$ at every $x$, so a given $y$ doesn't identify one $x$.

(b) Solve $3x + 4 = 3x + 9$ and $3x + 4 = 3x + 4$ with the theorem. In both, $a = c = 3$. In the first $b = 4 \ne d = 9$, so there is no solution: subtracting $3x$ leaves $4 = 9$. In the second $b = d = 4$, so every number is a solution: subtracting $3x$ leaves $4 = 4$.

Check (a) with $m = 2$, $b = 1$ and $y = 7$: $x = \frac{7 - 1}{2} = 3$, and $2 \cdot 3 + 1 = 7$. Check (b) at $x = 0$: the first equation has the sides 4 and 9, and the second has 4 and 4.

</div>

<div class="example" markdown>

### Example 4: Celsius and Fahrenheit (finish it yourself)

Solve $C = \frac{5}{9}(F - 32)$ for $F$.

Step 1: the target is $F$.

Step 2: clear the fraction by multiplying both sides by 9, which is not 0:

$$
9C = 5(F - 32).
$$

Step 3: the target is inside the bracket, which is multiplied by 5. Divide both sides by 5:

$$
\frac{9C}{5} = F - 32.
$$

Now finish: get $F$ alone, and check your formula with $C = 100$, which should give the boiling point of water, 212.

<details class="solution" markdown>
<summary>Finish</summary>

Add 32 to both sides:

$$
F = \frac{9C}{5} + 32.
$$

No division by a letter happened, so there are no restrictions.

Check: $C = 100$ gives $F = 180 + 32 = 212$. Also $C = 0$ gives 32, the freezing point, and $C = 37$ gives $66.6 + 32 = 98.6$, normal body temperature. The two scales agree at $-40$: $F = \frac{9}{5}(-40) + 32 = -72 + 32 = -40$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: don't divide only one term. From $A = P + Prt$ it is tempting to write $t = \frac{A - P}{r}$, forgetting the $P$ in $Prt$. With the numbers of Example 1 that gives $\frac{150}{0.03} = 5000$ years instead of 2.5. The coefficient of $t$ is the whole product $Pr$, so divide by all of it: $t = \frac{A - P}{Pr}$.

</div>

<div class="warning" markdown>

Watch out: undo the operations in the right order. For $C = \frac{5}{9}(F - 32)$, the formula $F = \frac{9}{5}C - 32$ subtracts instead of adding, and $F = \frac{9}{5}(C + 32)$ adds before multiplying. Both fail the check: for $C = 100$ they give 148 and 237.6, not 212.

</div>

<div class="warning" markdown>

Watch out: a quotient doesn't cancel across a sum. The expression $\frac{A - P}{P}$ is $\frac{A}{P} - 1$, not $A - 1$. With $A = 150$ and $P = 100$ the first is 0.5 and the second is 149. Cancel only a factor that multiplies the whole numerator and the whole denominator.

</div>

<div class="warning" markdown>

Watch out for the target on both sides. The line $x = \frac{c - bx}{a}$ isn't solved, because $x$ still appears on the right. Multiply out, move every $x$ term to one side, factor, and divide: from $ax = c - bx$ you get $(a + b)x = c$, so $x = \frac{c}{a + b}$ when $a + b \ne 0$.

</div>

The restrictions matter most when a letter could be 0. Solving $A = P(1 + rt)$ for $r$ gives $r = \frac{A - P}{Pt}$, which needs $P \ne 0$ and $t \ne 0$. If $t = 0$, no time passes, the formula says $A = P$ whatever $r$ is, and no rate can be recovered. A solved form is a statement about the cases it covers, not about the others.

Check the units and the way a percent is written before you substitute. A rate of 3% goes in as 0.03, and if the rate is per year, $t$ must be in years: 18 months is 1.5 years. A mismatch gives a wrong answer that no algebra will catch.

Equivalent answers can look different. The answers $t = \frac{A - P}{Pr}$ and $t = \frac{1}{r}\left(\frac{A}{P} - 1\right)$ are the same, since multiplying out the second gives $\frac{A}{Pr} - \frac{1}{r}$, which is the first with the fraction split. If your answer differs from a key, test both with the same numbers before deciding that one is wrong.

## Tricks and shortcuts

Check the units. In $t = \frac{A - P}{Pr}$, the top is dollars, and the bottom is dollars times "per year", so the whole is in years, as a time should be. A formula with the wrong units can't be right.

Pick numbers that make the original formula easy, and test your answer on them. For $A = P(1 + rt)$, take $P = 100$, $r = 0.05$ and $t = 2$, so that $A = 110$. If your formula for $r$ is correct, it should return 0.05 when you put in $A = 110$, $P = 100$ and $t = 2$.

When the target is in a denominator, a swap often finishes the job. From $a = \frac{k}{x}$ with $x \ne 0$, multiplying by $x$ gives $ax = k$, and then $x = \frac{k}{a}$ when $a \ne 0$. For a pixel's position in an image stored row by row, the index is $i = rw + c$, with row $r$, width $w$ and column $c$. Solving for $c$ gives $c = i - rw$, and solving for $r$ gives $r = \frac{i - c}{w}$ for $w \ne 0$.

For the fast version of a plain linear equation, check the coefficient of $x$ on each side first. If they match, don't solve: compare the constants. If they differ, the formula $\frac{d - b}{a - c}$ from the theorem is one line.

## In code

A computer algebra system solves a formula for any letter, but it doesn't report the restrictions. This code finds all three solved forms of $A = P(1 + rt)$, checks them, and then guards the restrictions by hand.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import symbols, Eq, solve, simplify

A, P, r, t = symbols("A P r t")
formula = Eq(A, P * (1 + r * t))

for letter in (t, P, r):
    print(letter, solve(formula, letter))
# t [(A - P)/(P*r)]
# P [A/(r*t + 1)]
# r [(A - P)/(P*t)]

# Substitute the solution for t back into the formula: the difference should be 0.
t_solved = solve(formula, t)[0]
print(simplify(P * (1 + r * t_solved) - A))   # 0

def years_to_reach(A, P, r):
    if P == 0 or r == 0:
        raise ValueError("the formula needs P != 0 and r != 0")
    return (A - P) / (P * r)

print(years_to_reach(2150, 2000, 0.03))       # 2.5
```

The `solve` calls print one expression each, but none of them mentions that $P$ and $r$ must be nonzero, so the function adds those checks. The function returns `2.5`, as in Example 1.

</details>

## FAQ

### Why do I have to say that $P \ne 0$? A principal is never 0.

In a real situation it usually isn't, and then the restriction is automatic. In mathematics, a formula is an equation about letters, and the equation $A = P(1 + rt)$ makes perfect sense for $P = 0$ (it says $A = 0$). The solved form $t = \frac{A - P}{Pr}$ doesn't make sense there, so the two equations are not equivalent for every $P$. Stating the restriction tells the reader exactly where the solved form can be trusted.

### What if the target letter is squared or under a root?

Then the equation isn't linear in that letter, and the steps here are not enough. For $A = \pi r^2$ solved for $r$, you divide by $\pi$ and then take a square root, which gives two candidates, $\pm\sqrt{A/\pi}$, and a sign to decide from the context. Quadratics and radicals are the next big topics: [solving quadratic equations](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md) and [radicals and rational exponents](../04-radicals-and-polynomials/01-radicals-and-rational-exponents.md).

### How is solving for $x$ related to inverse functions?

Writing $y = mx + b$ and solving for $x$ is exactly how you find the inverse of the function $f(x) = mx + b$: swap the roles of input and output. You get $f^{-1}(y) = \frac{y - b}{m}$, which exists only when $m \ne 0$. The same method works for other functions that undo cleanly, and [composition and inverse functions](../03-functions/05-composition-and-inverse-functions.md) develops it.

### Is $x = \frac{y - b}{m}$ the same as $x = \frac{y}{m} - \frac{b}{m}$?

Yes, both are correct. Splitting a fraction with a sum on top is allowed because dividing a sum by $m$ divides each term by $m$ (the distributive property again). The unsplit form is shorter to write, and the split form is easier to read as "slope and intercept", so both are common.

## Practice

### Warm-up

1\. Solve $4(x - 2) = 2x + 10$.

<details class="solution" markdown>
<summary>Solution</summary>

Expand: $4x - 8 = 2x + 10$. Subtract $2x$ from both sides: $2x - 8 = 10$. Add 8: $2x = 18$. Divide by 2: $x = 9$.

Check: the left side is $4(9 - 2) = 28$, and the right side is $2 \cdot 9 + 10 = 28$.

</details>

2\. Solve $I = Prt$ for $r$, stating the restrictions. Then find the rate when \$90 of simple interest is earned on \$1,500 in 2 years.

<details class="solution" markdown>
<summary>Solution</summary>

The target $r$ appears once, multiplied by $Pt$. Divide both sides by $Pt$:

$$
r = \frac{I}{Pt}, \qquad P \ne 0,\ t \ne 0.
$$

With $I = 90$, $P = 1500$ and $t = 2$: $r = \frac{90}{1500 \times 2} = \frac{90}{3000} = 0.03$, so 3% a year.

Check: $1500 \times 0.03 \times 2 = 90$.

</details>

3\. Solve $y = mx + b$ for $m$, stating the restriction. Then find the slope of the line with $y$-intercept 1 that passes through the point $(2, 7)$.

<details class="solution" markdown>
<summary>Solution</summary>

Subtract $b$ from both sides: $y - b = mx$. Divide by $x$:

$$
m = \frac{y - b}{x}, \qquad x \ne 0.
$$

The intercept is $b = 1$, and the point gives $x = 2$ and $y = 7$, so $m = \frac{7 - 1}{2} = 3$.

Check: $3 \cdot 2 + 1 = 7$, so the line $y = 3x + 1$ does pass through $(2, 7)$.

</details>

### Standard

4\. Solve $\frac{x + 3}{4} - \frac{2x - 1}{6} = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

The LCD of 4 and 6 is 12. Multiply every term by 12, keeping brackets around the numerators: $3(x + 3) - 2(2x - 1) = 12$. Expand, minding the minus sign: $3x + 9 - 4x + 2 = 12$. Combine: $-x + 11 = 12$. Subtract 11: $-x = 1$, so $x = -1$.

Check: the left side is $\frac{-1 + 3}{4} - \frac{-2 - 1}{6} = \frac{2}{4} + \frac{3}{6} = \frac{1}{2} + \frac{1}{2} = 1$.

</details>

5\. A business sells at price $p$ per unit, pays $v$ per unit to make it, and has a one-time set-up cost $s$. Selling $q$ units gives profit $y = (p - v)q - s$. (a) Solve for $q$, stating the restriction. (b) For $p = 12$, $v = 7$ and $s = 500$, how many units give a profit of 0 (the break-even point)? (c) What does the restriction mean?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The target $q$ appears once. Add $s$ to both sides: $y + s = (p - v)q$. Divide by $p - v$:

$$
q = \frac{y + s}{p - v}, \qquad p \ne v.
$$

(b) Put in $y = 0$: $q = \frac{0 + 500}{12 - 7} = \frac{500}{5} = 100$ units.

(c) The number $p - v$ is the profit on each unit. If $p = v$, each unit earns nothing, so no number of units changes the profit from $-s$, and the profit never reaches 0 (unless $s = 0$).

Check: $(12 - 7) \cdot 100 - 500 = 0$.

</details>

6\. You want \$5,000 after 4 years at 3% simple interest a year. (a) Solve $A = P(1 + rt)$ for $P$, stating the restriction. (b) How much do you need to deposit, to the nearest cent, so that you have at least \$5,000?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The target $P$ appears once, multiplied by $1 + rt$. Divide both sides by $1 + rt$:

$$
P = \frac{A}{1 + rt}, \qquad 1 + rt \ne 0.
$$

For a positive rate and time, $1 + rt$ is at least 1, so the restriction always holds in this setting.

(b) $P = \frac{5000}{1 + 0.03 \times 4} = \frac{5000}{1.12} = 4464.2857\ldots$. You need at least this much, so round up: \$4,464.29.

Check: $4464.29 \times 1.12 = 5000.0048$, which is at least 5000, while $4464.28 \times 1.12 = 4999.9936$ falls short.

</details>

### Challenge

7\. Solve $\frac{x}{a} + \frac{x}{b} = 1$ for $x$, where $a \ne 0$ and $b \ne 0$. Find every case, including the one where the formula breaks. (This is the form of the lens equation in physics and of the combined resistance of two parallel resistors.)

<details class="solution" markdown>
<summary>Solution</summary>

We know that $a \ne 0$ and $b \ne 0$, so $ab \ne 0$. Multiply every term by $ab$: $bx + ax = ab$. Factor the target out of the left side: $(a + b)x = ab$.

If $a + b \ne 0$, divide by $a + b$:

$$
x = \frac{ab}{a + b}.
$$

If $a + b = 0$, then $b = -a$, and the equation $(a + b)x = ab$ reads $0 \cdot x = -a^2$. Since $a \ne 0$, $-a^2 \ne 0$, so there is no solution. In the original, the left side is $\frac{x}{a} - \frac{x}{a} = 0$, which never equals 1.

Check: with $a = 3$ and $b = 6$, the formula gives $x = \frac{18}{9} = 2$, and $\frac{2}{3} + \frac{2}{6} = 1$. With $a = 3$ and $b = -3$ there is no solution, as shown.

</details>

8\. This one reviews [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md). A seller sets the price $P$ from the cost $C$ and the margin $g$ (the profit as a fraction of the price) by $P = \frac{C}{1 - g}$. (a) Solve for $g$, stating the restriction. (b) Check that a cost of \$100 and a price of \$150 give a margin of one third. (c) What price gives a 40% margin on a cost of \$72?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Multiply both sides by $1 - g$ (which must not be 0): $P(1 - g) = C$. Divide by $P$, with $P \ne 0$: $1 - g = \frac{C}{P}$. Subtract 1 and change signs, or write directly:

$$
g = 1 - \frac{C}{P} = \frac{P - C}{P}, \qquad P \ne 0.
$$

(b) $g = \frac{150 - 100}{150} = \frac{50}{150} = \frac{1}{3}$, about 33.3%, so a 50% markup is a 33.3% margin, as in the percent change lesson.

(c) With $g = 0.4$ and $C = 72$: $P = \frac{72}{1 - 0.4} = \frac{72}{0.6} = 120$, so \$120.

Check: the margin at \$120 is $\frac{120 - 72}{120} = \frac{48}{120} = 0.4$.

</details>

## Where this shows up

- The next chapter starts from [forms of linear equations](../02-linear-functions-and-systems/01-forms-of-linear-equations.md), which are one line written in different ways, and converting between them is the skill of this lesson. [Systems of linear equations](../02-linear-functions-and-systems/02-systems-of-linear-equations.md) are solved by substitution: solve one equation for a letter, then put it into the other.
- In economics, equilibrium is "set two expressions equal and solve for the price", as in Example 2 ([supply and demand equilibrium algebra](../../07-economics-math/02-markets/03-supply-and-demand-equilibrium-algebra.md)). In finance, every interest and loan formula is solved for whichever letter you don't know: simple interest<!-- link: ../../08-financial-math/02-interest-and-growth/01-simple-interest.md --> uses the formula from Example 1, and the later formulas are solved the same way.
- In programming, inverting an index formula, such as turning `i = r * w + c` into row and column, is the same solve-for-a-letter step.
