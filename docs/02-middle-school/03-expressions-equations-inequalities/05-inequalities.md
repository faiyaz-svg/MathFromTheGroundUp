# Inequalities

After this lesson you can read and write inequalities, graph a solution set on a number line, solve a linear inequality (reversing the sign when you multiply or divide by a negative number, and knowing why), and turn phrases such as "at least" and "at most" into symbols.

Before this: [multi-step equations](04-multi-step-equations.md), and [negative numbers and absolute value](../01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md) for the number line.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $3x - 5 \le 10$, and describe its graph on a number line.
2. Solve $4 - 2x > 10$.
3. A ride costs \$3 plus \$1.50 per kilometre, and you have \$24. How far can you go?

<details class="solution" markdown>
<summary>Answers</summary>

1. $x \le 5$. Add 5 to get $3x \le 15$, then divide by 3. The graph is a closed dot at 5 with the line shaded to the left.
2. $x < -3$. Subtract 4 to get $-2x > 6$, then divide by $-2$ and reverse the sign.
3. At most 14 km. With $d$ the distance in kilometres, $3 + 1.50d \le 24$, so $1.50d \le 21$ and $d \le 14$.

</details>

## The idea

A trip to a museum costs \$15 for parking plus \$9 for each ticket, and the group has \$60. How many tickets can it buy? With $n$ tickets the cost is $15 + 9n$ dollars, and the cost must be at most 60:

$$
15 + 9n \le 60.
$$

The same steps as for an equation work here. Subtract 15 from both sides to get $9n \le 45$, and divide by 9 to get $n \le 5$. The answer is not one number: the group can buy 0, 1, 2, 3, 4 or 5 tickets. An inequality usually has a whole range of solutions, and solving it means describing that range.

Most of the equation rules carry over unchanged, with one exception. Start from $2 < 3$, which is true, and multiply both sides by $-1$. The results are $-2$ and $-3$, and on the number line $-3$ is to the left of $-2$:

```text
<---+-----+-----+-----+-----+-----+-----+--->
   -3    -2    -1     0     1     2     3
```

So $-2 > -3$: multiplying by $-1$ reversed the order. Think of money. Owing \$2 is better than owing \$3, even though \$2 is less than \$3. Multiplying by $-1$ reflects every number across 0, and a reflection swaps left and right, so the smaller number becomes the larger one (the mirror from [negative numbers and absolute value](../01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md)). That is why an inequality reverses when you multiply or divide both sides by a negative number.

## Definitions

An **inequality** is a statement that compares two expressions with one of the symbols in this table.

| Symbol | Read as | Example of a true statement |
|---|---|---|
| $<$ | is less than | $-3 < -2$ |
| $\le$ | is less than or equal to | $4 \le 4$ |
| $>$ | is greater than | $0 > -1$ |
| $\ge$ | is greater than or equal to | $7 \ge 2$ |
| $\ne$ | is not equal to | $2 + 2 \ne 5$ |

For numbers $a$ and $b$, the statement $a < b$ means that $b - a$ is positive. On the number line, $a$ lies to the left of $b$. The statement $a \le b$ means that $a < b$ or $a = b$, and $a > b$ means the same as $b < a$. For example, $-3 < -2$ because $-2 - (-3) = 1$, which is positive.

A **strict inequality** uses $<$ or $>$ and leaves out the case of equality, so $5 < 5$ is false. A non-strict inequality uses $\le$ or $\ge$ and allows it, so $5 \le 5$ is true. The symbol $\ne$ appears in this book mostly in conditions such as "for $x \ne 0$", and the solving in this lesson uses the other four.

As with equations, a solution of an inequality in one variable is a value that makes it true, and the solution set is the set of all solutions. Two inequalities with the same solution set are equivalent. The solution set of $x \le 5$ contains 5, $-12$ and $4.99$, but not $5.01$.

On a number line, a solution set such as $x \le 5$ is drawn as a dot at the boundary number with the line shaded toward the solutions. An **open dot** at the boundary means the boundary number is not included, which goes with $<$ and $>$. A **closed dot**, filled in, means it is included, which goes with $\le$ and $\ge$. In the text pictures in this lesson, `o` is an open dot, `*` is a closed dot, and `=` marks the shading.

## How to do it

### The rules for inequalities

*Theorem.* Let $a$, $b$ and $c$ be numbers with $a < b$.

1. Then $a + c < b + c$.
2. If $c > 0$, then $ac < bc$.
3. If $c < 0$, then $ac > bc$.

The same rules hold with $\le$ in place of $<$, and then with $\ge$ in place of $>$ in rule 3. Subtracting $c$ is adding $-c$, and dividing by $c$ is multiplying by $\frac{1}{c}$, which has the same sign as $c$, so the three rules cover all four operations.

We know that $a < b$ means $b - a$ is positive, and the sign rules from [integer arithmetic and sign rules](../01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md): the product of two positive numbers is positive. We want to compare two new numbers, and by the definition that means finding the sign of their difference. The plan is to write each difference as a product of numbers whose signs we know.

*Proof.* For rule 1, the difference is $(b + c) - (a + c) = b - a$, which is positive, so $a + c < b + c$.

For rule 2, the difference is $bc - ac = (b - a)c$. Both $b - a$ and $c$ are positive, so the product is positive, and $ac < bc$.

For rule 3, take the difference the other way round:

$$
ac - bc = (a - b)c = (b - a)(-c).
$$

Here $b - a$ is positive, and $-c$ is positive because $c$ is negative. So $ac - bc$ is positive, which means $bc < ac$, that is, $ac > bc$.

Look back: the only place the sign of $c$ mattered was in rules 2 and 3, and the reversal in rule 3 comes from the factor $-c$. With $a = 2$, $b = 3$ and $c = -1$, rule 3 says $-2 > -3$, the example from [The idea](#the-idea). Multiplying by $c = 0$ is excluded from both rules: it turns $2 < 3$ into $0 < 0$, which is false. Equations never needed a rule like rule 3, because an equality has no direction to reverse.

### Solving a linear inequality

1. Simplify each side as for an equation: clear fractions by multiplying by the LCD, which is positive, expand brackets and combine like terms.
2. Gather the variable terms on one side and the constants on the other, by adding or subtracting the same term on both sides. Neither step changes the direction of the symbol.
3. Divide both sides by the coefficient of the variable. If it is positive, keep the symbol. If it is negative, reverse it: $<$ becomes $>$, $\le$ becomes $\ge$, and the other way round.
4. Write the answer with the variable on the left. If you finish with $5 > x$, read it from right to left as $x < 5$; that is the same statement, not a step that changes it.
5. Graph the solution set: a dot at the boundary number, open for $<$ or $>$ and closed for $\le$ or $\ge$, with the line shaded toward the solutions.
6. Check two things. The boundary number should make the two sides equal. A test number from the shaded part should make the original inequality true, and one from the unshaded part should make it false.

### Words for inequalities

| Words | Symbol | Example | Inequality |
|---|---|---|---|
| at least, no less than, a minimum of | $\ge$ | you need at least 67 marks | $x \ge 67$ |
| at most, no more than, a maximum of | $\le$ | the load is at most 1,000 kg | $x \le 1000$ |
| more than, greater than, over | $>$ | the trip takes more than 3 hours | $t > 3$ |
| less than, fewer than, under | $<$ | the class has fewer than 30 students | $n < 30$ |

The first two rows include the boundary: if you need at least 67 marks, then 67 itself is enough. The last two leave it out.

### Compound inequalities, a preview

A **compound inequality** is two inequalities joined by "and" or "or". The statement $-2 < x \le 5$ means "$-2 < x$ and $x \le 5$", so it describes the numbers between $-2$ and 5, with 5 included and $-2$ left out:

```text
          o=========================================*
<---+-----+-----+-----+-----+-----+-----+-----+-----+-----+--->
   -3    -2    -1     0     1     2     3     4     5     6
```

The statement "$x < -1$ or $x \ge 3$" describes two separate pieces of the line, one going left from $-1$ and one going right from 3. To solve a "between" inequality such as $-3 \le 2x + 1 < 7$, do the same thing to all three parts. Subtracting 1 gives $-4 \le 2x < 6$, and dividing by 2 gives $-2 \le x < 3$. Dividing all three parts by a negative number reverses both symbols, as Practice problem 7 shows. The full treatment, with interval notation such as $[-2, 3)$, is in [compound inequalities and interval notation](../../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md).

## Worked examples

<div class="example" markdown>

### Example 1: dividing by a negative number

Solve $5 - 3x \le 17$, graph the solution set, and check it.

Step 1: each side is already simplified.

Step 2: subtract 5 from both sides. Subtracting never changes the direction:

$$
-3x \le 12.
$$

Step 3: the coefficient of $x$ is $-3$, which is negative. Dividing both sides by $-3$ reverses the symbol, so $\le$ becomes $\ge$:

$$
x \ge \frac{12}{-3}, \quad \text{that is,} \quad x \ge -4.
$$

<div class="warning" markdown>

Watch out: this is the step where the reversal happens, and forgetting it gives $x \le -4$, the exact opposite set apart from the boundary. The test number in Step 6 catches it: $x = -5$ satisfies $x \le -4$, but $5 - 3(-5) = 20$, and $20 \le 17$ is false.

</div>

Step 4: the variable is on the left, so the answer is $x \ge -4$.

Step 5: the symbol $\ge$ includes the boundary, so draw a closed dot at $-4$ and shade to the right:

```text
                *=================================>
<---+-----+-----+-----+-----+-----+-----+-----+--->
   -6    -5    -4    -3    -2    -1     0     1
```

Step 6: at the boundary, $5 - 3(-4) = 5 + 12 = 17$, so the two sides are equal, as they should be. At the test number 0, from the shaded part, $5 - 0 = 5$, and $5 \le 17$ is true. At $-5$, from the unshaded part, the left side is 20, and $20 \le 17$ is false. Both tests agree with the graph.

</div>

<div class="example" markdown>

### Example 2: fractions and the variable on both sides

Solve $\frac{x}{3} - 2 > \frac{x + 1}{2}$.

Step 1: the LCD of 3 and 2 is 6, a positive number, so multiplying by it keeps the symbol. Multiply every term by 6, keeping the brackets around $x + 1$:

$$
2x - 12 > 3(x + 1), \quad \text{so} \quad 2x - 12 > 3x + 3.
$$

Step 2: the larger coefficient, 3, is on the right, so gather the variable there. Subtract $2x$ from both sides, then subtract 3:

$$
-12 > x + 3, \quad \text{so} \quad -15 > x.
$$

Step 3: the coefficient of $x$ is already 1, so nothing is divided and nothing is reversed.

Step 4: read $-15 > x$ from right to left: $x < -15$. The graph has an open dot at $-15$, shaded to the left:

```text
<=====================o
<---+-----+-----+-----+-----+-----+-----+--->
  -18   -17   -16   -15   -14   -13   -12
```

Gathering on the left would also work. Subtracting $3x$ gives $-x - 12 > 3$, then $-x > 15$, and dividing by $-1$ reverses the symbol: $x < -15$, the same answer.

Check: at $x = -15$ the left side is $-5 - 2 = -7$ and the right side is $\frac{-14}{2} = -7$, so the boundary makes the sides equal. At $x = -18$ the left side is $-6 - 2 = -8$ and the right side is $\frac{-17}{2} = -8.5$, and $-8 > -8.5$ is true.

</div>

<div class="example" markdown>

### Example 3: no solution, and every number

Solve (a) $3x + 1 < 3x - 2$ and (b) $2(x + 1) \ge 2x$.

(a) Subtract $3x$ from both sides: $1 < -2$. The variable is gone, and the statement left over is false. It is false whatever $x$ is, so there is no solution, and the solution set is empty. In words: the left side is always 3 more than the right side, so it is never less.

(b) Expand: $2x + 2 \ge 2x$. Subtract $2x$: $2 \ge 0$, which is true. It is true whatever $x$ is, so every number is a solution, and the graph shades the whole line. Check at $x = -10$: the left side is $-18$, the right side is $-20$, and $-18 \ge -20$ is true.

These are the same two special cases as in [multi-step equations](04-multi-step-equations.md#the-three-possible-outcomes): when the variable terms cancel, a false statement means no solution and a true statement means every number.

</div>

<div class="example" markdown>

### Example 4: the mark you need (finish it yourself)

Your course grade is the average of four tests, and you need an average of at least 70. You scored 64, 78 and 71 on the first three. What do you need on the fourth?

Let $x$ be the mark on the fourth test, out of 100. "At least 70" means $\ge 70$, so

$$
\frac{64 + 78 + 71 + x}{4} \ge 70.
$$

Step 1: add the known marks, $64 + 78 + 71 = 213$, and multiply both sides by 4, which is positive:

$$
213 + x \ge 280.
$$

Now finish Steps 2 to 6: solve, describe the graph, and check the boundary.

<details class="solution" markdown>
<summary>Finish</summary>

Step 2: subtract 213 from both sides, which gives $x \ge 67$. Steps 3 and 4: the coefficient is 1 and the variable is on the left, so the answer is $x \ge 67$. You need at least 67 on the fourth test.

Step 5: a closed dot at 67, shaded to the right. Since a test is marked out of 100, the useful part of the solution set runs from 67 to 100.

Step 6: with exactly 67, the average is $\frac{213 + 67}{4} = \frac{280}{4} = 70$, which meets "at least 70". With 66 it would be $\frac{279}{4} = 69.75$, which falls short.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: dividing by a negative number reverses the symbol. From $-2x < 6$, dividing by $-2$ gives $x > -3$, not $x < -3$. Test $x = 0$, which satisfies $x > -3$: the original says $0 < 6$, which is true. This is also on the [common mistakes](../../reference/common-mistakes.md#not-flipping-an-inequality-after-multiplying-by-a-negative) page.

</div>

<div class="warning" markdown>

Watch out: a negative number elsewhere in the inequality doesn't reverse anything. Only multiplying or dividing both sides by a negative number does. From $3x < -12$, dividing by the positive number 3 gives $x < -4$, and from $x - 4 < -6$, adding 4 gives $x < -2$. Neither needs a reversal, even though both contain negatives.

</div>

<div class="warning" markdown>

Watch out: the dot must match the symbol. "At least 67" includes 67, so the dot at 67 is closed; "more than 3 hours" leaves 3 out, so the dot at 3 is open. When an answer ends as $5 > x$, the solutions are the numbers less than 5, so the shading goes left, even though the 5 is written first.

</div>

Checking only the boundary is not enough. The boundary number makes the two sides equal whether or not you reversed the symbol, so it can't catch a missing reversal. Always try one test number from the shaded part as well.

When the variable counts whole things, round in the direction the inequality allows, not to the nearest whole number. If $n \le 38.75$ boxes fit in an elevator, then 38 boxes fit and 39 don't. If you need $t \ge 42.9$ hours of work, then you need 43 hours. Practice problems 6 and 8 have both cases.

Multiplying both sides by an expression that contains the variable is a trap, because you don't know its sign, so you don't know whether to reverse. For example, $\frac{1}{x} < 2$ is not the same as $1 < 2x$: the number $x = -1$ satisfies the first, since $-1 < 2$, but not the second. Inequalities of that kind are solved by cases in [polynomial and rational inequalities](../../03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md).

A chain such as $3 < x > 5$ is not a compound inequality and has no standard meaning. A chain is written with both symbols pointing the same way, as in $3 < x < 5$, so that it reads as one stretch of the number line.

## Tricks and shortcuts

Keep the coefficient positive and you never have to reverse. Gather the variable on the side where its coefficient is larger, as in Example 2, and Step 3 always divides by a positive number. The reversal rule is still needed when the coefficient is negative from the start, as in Example 1, unless you add $3x$ to both sides first.

When the variable is on the left, the tip of the symbol points the way to shade. In $x < 2$ the tip of $<$ points left, and the solutions are to the left of 2; in $x \ge -4$ the tip of $\ge$ points right, and the solutions are to the right of $-4$.

Choose 0 as the test number whenever 0 is not the boundary, because the arithmetic is easiest. In Example 1 the test at 0 took one line.

## In code

Sympy's `solveset` solves inequalities and returns the solution set as an interval. The last lines show the compound inequality from Practice problem 7 as the intersection of two solution sets, since "and" asks for the numbers in both.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import symbols, solveset, S

x = symbols("x")
print(solveset(5 - 3*x <= 17, x, S.Reals))              # Interval(-4, oo)
print(solveset(x/3 - 2 > (x + 1)/2, x, S.Reals))        # Interval.open(-oo, -15)
print(solveset(3*x + 1 < 3*x - 2, x, S.Reals))          # EmptySet
print(solveset(2*(x + 1) >= 2*x, x, S.Reals))           # Reals

print([n for n in range(-10, 11) if 5 - 3*n <= 17])     # the integers from -4 to 10

left = solveset(-5 < 3 - 2*x, x, S.Reals)
right = solveset(3 - 2*x <= 9, x, S.Reals)
print(left.intersect(right))                            # Interval.Ropen(-3, 4)
```

`oo` is sympy's symbol for infinity, so `Interval(-4, oo)` is every number from $-4$ up, with $-4$ included. `Interval.open` leaves out both ends, and `Interval.Ropen(-3, 4)` includes $-3$ and leaves out 4 (the right end is open). Python itself also writes compound inequalities as chains: `0 <= i < len(a)` is true exactly when `i` is a valid index of the list `a`.

</details>

## FAQ

### Why does multiplying by a negative reverse the symbol when subtracting a negative doesn't?

Adding or subtracting a number slides the whole number line left or right, and a slide keeps every number in the same order. Subtracting $-4$ is adding 4, which is a slide, so nothing reverses. Multiplying by a negative number reflects the line across 0 (and also stretches it), and a reflection swaps left and right. Rule 1 and rule 3 of the theorem are these two pictures written in symbols.

### Is "at most 5" the same as "less than 6"?

For whole numbers, yes: both describe $5, 4, 3, \dots$ and the negative integers. For real numbers, no. The number 5.5 satisfies $x < 6$ but not $x \le 5$. When the variable counts tickets or people the two are interchangeable, but in algebra the variable can be any real number unless the problem says otherwise, so keep the symbol and the boundary you found.

### Is 0 positive?

No, 0 is neither positive nor negative. A positive number satisfies $x > 0$, which leaves 0 out, and a non-negative number satisfies $x \ge 0$, which lets it in. University definitions lean on the difference: "for every integer $n \ge 1$" and "for every integer $n > 0$" describe the same integers, but "for every real $x > 0$" and "for every real $x \ge 0$" do not, since only the second includes 0.

## Practice

### Warm-up

1\. True or false: (a) $-7 < -2$, (b) $-4 \ge -4$, (c) $3 \le -3$, (d) $-0.5 < -0.25$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) True: $-2 - (-7) = 5$, which is positive, so $-7$ is to the left of $-2$.
- (b) True: $\ge$ allows equality, and $-4 = -4$.
- (c) False: 3 is to the right of $-3$.
- (d) True: $-0.25 - (-0.5) = 0.25$, which is positive. Owing half a dollar is worse than owing a quarter.

</details>

2\. (a) Graph $x > -1$. (b) Write "all numbers that are at most 4" as an inequality, and graph it.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The symbol $>$ leaves out the boundary, so draw an open dot at $-1$ and shade to the right:

```text
                o===========================>
<---+-----+-----+-----+-----+-----+-----+--->
   -3    -2    -1     0     1     2     3
```

(b) "At most 4" means $x \le 4$. Draw a closed dot at 4 and shade to the left:

```text
<===========================*
<---+-----+-----+-----+-----+-----+-----+--->
    0     1     2     3     4     5     6
```

Check with test numbers: 0 is shaded in (a), and $0 > -1$ is true; 4 is shaded in (b), and $4 \le 4$ is true, while 5 is not shaded, and $5 \le 4$ is false.

</details>

3\. Solve (a) $x + 7 < 3$ and (b) $-5x \ge 20$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Subtract 7 from both sides: $x < -4$. Subtracting never reverses the symbol.

(b) Divide both sides by $-5$, which is negative, so reverse the symbol: $x \le -4$.

Check (a) at $-5$: $-5 + 7 = 2$, and $2 < 3$ is true. Check (b) at $-5$: $-5(-5) = 25$, and $25 \ge 20$ is true; at 0, $0 \ge 20$ is false, as it should be, since 0 is not in the solution set.

</details>

### Standard

4\. Solve $7 - 4x > 3x + 21$, graph the solution set, and check it.

<details class="solution" markdown>
<summary>Solution</summary>

The larger coefficient of $x$ is on the right ($3 > -4$), so gather there. Add $4x$ to both sides: $7 > 7x + 21$. Subtract 21: $-14 > 7x$. Divide by 7, which is positive: $-2 > x$. Read from right to left, the answer is $x < -2$.

The graph has an open dot at $-2$, shaded to the left:

```text
<=====================o
<---+-----+-----+-----+-----+-----+-----+--->
   -5    -4    -3    -2    -1     0     1
```

Check: at the boundary $-2$, the left side is $7 + 8 = 15$ and the right side is $-6 + 21 = 15$. At the test number $-3$, the left side is 19 and the right side is 12, and $19 > 12$ is true. At 0, $7 > 21$ is false.

</details>

5\. Solve $\frac{2x - 3}{5} \le \frac{x}{2} + 1$.

<details class="solution" markdown>
<summary>Solution</summary>

The LCD of 5 and 2 is 10. Multiply every term by 10, which is positive: $2(2x - 3) \le 5x + 10$. Expand: $4x - 6 \le 5x + 10$. Gather on the right, where the coefficient is larger. Subtract $4x$: $-6 \le x + 10$. Subtract 10: $-16 \le x$. So $x \ge -16$.

Check: at the boundary, the left side is $\frac{-32 - 3}{5} = -7$ and the right side is $-8 + 1 = -7$. At the test number 0, the left side is $-\frac{3}{5}$ and the right side is 1, and $-\frac{3}{5} \le 1$ is true.

</details>

6\. An elevator can carry at most 1,000 kg. The operator weighs 70 kg and rides with boxes of 24 kg each. How many boxes can go in one trip?

<details class="solution" markdown>
<summary>Solution</summary>

Let $n$ be the number of boxes. The load is $70 + 24n$ kilograms, and "at most 1,000" means $\le 1000$:

$$
70 + 24n \le 1000.
$$

Subtract 70: $24n \le 930$. Divide by 24: $n \le 38.75$. The number of boxes is a whole number, and 38.75 rounds to 39, but 39 boxes would break the limit, so round down: at most 38 boxes.

Check: 38 boxes give $70 + 24 \times 38 = 70 + 912 = 982$ kg, which is within the limit, and 39 boxes give $70 + 936 = 1006$ kg, which is over.

</details>

### Challenge

7\. Solve the compound inequality $-5 < 3 - 2x \le 9$, and graph the solution set.

<details class="solution" markdown>
<summary>Solution</summary>

Do the same thing to all three parts. Subtract 3:

$$
-8 < -2x \le 6.
$$

Divide all three parts by $-2$. The number is negative, so both symbols reverse:

$$
4 > x \ge -3.
$$

Read from right to left, this is $-3 \le x < 4$: the numbers from $-3$ to 4, with $-3$ included and 4 left out.

```text
          *=========================================o
<---+-----+-----+-----+-----+-----+-----+-----+-----+-----+--->
   -4    -3    -2    -1     0     1     2     3     4     5
```

Check the ends. At $x = -3$ the middle expression is $3 + 6 = 9$, and $-5 < 9 \le 9$ is true, so $-3$ belongs. At $x = 4$ it is $3 - 8 = -5$, and $-5 < -5$ is false, so 4 does not. At the test number 0 it is 3, and $-5 < 3 \le 9$ is true.

</details>

8\. This one reviews [percents](../02-ratios-rates-percents/03-percents.md). You have \$50, and the notebooks you want cost \$6.50 each before 13% HST. How many can you buy?

<details class="solution" markdown>
<summary>Solution</summary>

Let $n$ be the number of notebooks. Before tax they cost $6.50n$ dollars, and adding 13% HST multiplies that by 1.13. The total must be at most \$50:

$$
1.13 \times 6.50n \le 50, \quad \text{that is,} \quad 7.345n \le 50.
$$

Divide by 7.345, which is positive: $n \le 6.807\ldots$ The number of notebooks is a whole number no bigger than 6.807, so you can buy at most 6.

Check: 6 notebooks cost $6 \times 6.50 = 39$ dollars before tax and $1.13 \times 39 = 44.07$ with tax, which is under \$50. Seven cost $1.13 \times 45.50 = 51.415$, about \$51.42, which is over.

</details>

## Where this shows up

- [Compound inequalities and interval notation](../../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md) finishes the preview above, [absolute value equations and inequalities](../../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md) solves statements such as $\lvert x - 3 \rvert < 2$, and [two-variable inequalities and feasible regions](../../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md) shades regions of the plane. In economics, a budget is an inequality in two variables: spending on two goods must be at most your income (utility and indifference curves<!-- link: ../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md -->).
- University definitions are full of inequalities. Big O notation says that $f(n) \le c\,g(n)$ for every $n \ge n_0$ (asymptotic notation<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md -->), and the definition of a limit asks for $\lvert f(x) - L \rvert < \varepsilon$ (the epsilon-delta definition<!-- link: ../../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md -->). Proofs about them use the three rules in this lesson, step by step.
- In code, bounds checks and loop conditions are inequalities: a loop `for i in range(n)` runs exactly for the integers with $0 \le i < n$, and the off-by-one bugs come from mixing up $<$ and $\le$.
