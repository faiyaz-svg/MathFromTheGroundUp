# One- and two-step equations

After this lesson you can solve equations such as $3x + 11 = 2$ and $\frac{2}{3}x - 4 = 6$ by undoing operations, explain why doing the same thing to both sides keeps the solutions, check a solution by substitution, and set up an equation from a word problem.

Before this: [variables and expressions](01-variables-and-expressions.md), [equivalent expressions](02-equivalent-expressions.md), [integer arithmetic and sign rules](../01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md), and [multiplying and dividing fractions](../../01-elementary/11-multiplying-and-dividing-fractions.md) for reciprocals.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $x - 8 = -3$.
2. Solve $-4x + 9 = 21$.
3. A taxi charges \$4.25 plus \$1.80 per kilometre, and your ride cost \$22.25. How far did you go?

<details class="solution" markdown>
<summary>Answers</summary>

1. $x = 5$. Add 8 to both sides. Check: $5 - 8 = -3$.
2. $x = -3$. Subtract 9 to get $-4x = 12$, then divide by $-4$. Check: $-4(-3) + 9 = 12 + 9 = 21$.
3. 10 km. With $d$ the distance in kilometres, $1.80d + 4.25 = 22.25$, so $1.80d = 18$ and $d = 10$. Check: $1.80 \times 10 + 4.25 = 22.25$.

</details>

## The idea

Picture a pan balance. On the left pan sit three identical bags of rice and a 2 kg weight; on the right pan sit weights totalling 14 kg, and the pans are level. How heavy is one bag? Take the 2 kg weight off the left pan and 2 kg off the right pan, and the pans stay level: three bags balance 12 kg. Now split each side into three equal parts, and one bag balances 4 kg.

In symbols, with $x$ for the mass of one bag in kilograms, the balance says $3x + 2 = 14$. Removing 2 kg from both pans gives $3x = 12$, and taking a third of both sides gives $x = 4$. The pans stay level as long as you do the same thing to both sides, and that is the whole method.

A second way to see it: the expression $3x + 2$ is a recipe that starts with $x$, multiplies by 3, then adds 2. To get back to $x$, undo the steps in reverse order, the way you take off your shoes before your socks. Subtract 2, then divide by 3.

The balance picture stops working for negative numbers, since no bag weighs $-3$ kg, and it can't show dividing by a negative. The algebra has no such limit. The rest of this lesson states the rule exactly, proves that it never loses or adds a solution, and uses it with fractions and negatives.

## Definitions

An **equation** is a statement that two expressions are equal, such as $3x + 2 = 14$. The expression before the equals sign is the left side and the one after it is the right side.

A **solution** of an equation in one variable is a value of the variable that makes the equation true. To **solve** an equation is to find all of its solutions, and the set of all of them is the **solution set**. The number 4 is a solution of $3x + 2 = 14$, because $3(4) + 2 = 14$ is true; the number 5 is not, because $3(5) + 2 = 17$, and $17 \ne 14$. The solution set is $\{4\}$, the set whose only element is 4.

In plain words, an equation asks a question ("which numbers make this true?") and its solution set is the complete answer. Most equations in this lesson have exactly one solution, but the next lesson meets equations with none and equations that every number solves.

**Inverse operations** are operations that undo each other. Adding $c$ and subtracting $c$ are inverses, and so are multiplying by $c$ and dividing by $c$, provided $c \ne 0$. For example, $7 + 5 - 5 = 7$ and $7 \times 5 \div 5 = 7$.

Two equations are **equivalent equations** when they have the same solution set. The equations $3x + 2 = 14$, $3x = 12$ and $x = 4$ are equivalent, since each has the solution set $\{4\}$. Solving an equation means replacing it with equivalent equations until one of them says that $x$ equals some number, and then the solution can be read off.

## How to do it

### Why the same operation on both sides keeps the solutions

Write an equation as $L = R$, where $L$ is the expression on the left and $R$ the expression on the right.

*Theorem.* Let $c$ be a number.

1. The equations $L = R$ and $L + c = R + c$ have the same solutions.
2. If $c \ne 0$, the equations $L = R$ and $cL = cR$ have the same solutions.

We know that two equal numbers stay equal when you do the same thing to both: if $u = v$, then $u + c = v + c$ and $cu = cv$, because each side is the same number to begin with. We want more than that. A step that only kept the old solutions could still add new ones, so we need every solution of each equation to solve the other. The plan is to show that each step can be undone.

*Proof.* For part 1, take a solution of $L = R$. At that value of the variable, $L$ and $R$ are the same number, so $L + c$ and $R + c$ are the same number, and the value solves $L + c = R + c$. Now go back: take a solution of $L + c = R + c$, and add $-c$ to both sides. Since $c + (-c) = 0$ (the inverse property of addition), this gives $L = R$ at that value. So the two equations have exactly the same solutions.

Part 2 is the same argument with multiplication. A solution of $L = R$ solves $cL = cR$. For the way back, multiply both sides of $cL = cR$ by $\frac{1}{c}$; since $\frac{1}{c} \cdot c = 1$ (the inverse property of multiplication), this gives $L = R$. The number $\frac{1}{c}$ exists because $c \ne 0$.

Look back: subtracting $c$ is adding $-c$, and dividing by $c$ is multiplying by $\frac{1}{c}$, so the theorem covers all four operations. The condition $c \ne 0$ is needed. Multiplying both sides of $x = 2$ by 0 gives $0 = 0$, which every number satisfies, so the new equation has solutions the old one lacked, and there is no way back, because 0 has no reciprocal.

### Solving a one- or two-step equation

1. If a side has brackets or like terms, simplify it first, as in [equivalent expressions](02-equivalent-expressions.md).
2. Read what has been done to the variable, in order. In $3x + 11$, the variable was multiplied by 3 and then 11 was added.
3. Undo those operations in reverse order, doing each one to both sides: first undo the addition or subtraction, then the multiplication or division.
4. Stop when the variable stands alone on one side. The other side is the solution.
5. Check: substitute the solution into the original equation, and work out each side separately. They must be equal.

A one-step equation needs one pass through Step 3, and a two-step equation needs two.

### Writing an equation from a word problem

1. Choose a letter for the unknown and write down what it stands for, with units: "let $n$ be the number of months".
2. Write the other quantities in the problem in terms of that letter.
3. Find the two things the problem says are equal, and write them as an equation.
4. Solve the equation.
5. Check the answer against the words of the problem as well as against your equation, and give it in a sentence with units. Make sure it makes sense: a number of tickets is a whole number, and a length is not negative.

## Worked examples

<div class="example" markdown>

### Example 1: a two-step equation with a negative answer

Solve $3x + 11 = 2$.

Step 1: each side is already simplified.

Step 2: the variable was multiplied by 3, then 11 was added.

Step 3: undo the last operation first. Subtract 11 from both sides:

$$
\begin{aligned}
3x + 11 - 11 &= 2 - 11 && \text{subtract 11 from both sides} \\
3x &= -9.
\end{aligned}
$$

Then undo the multiplication. Divide both sides by 3:

$$
\begin{aligned}
\frac{3x}{3} &= \frac{-9}{3} && \text{divide both sides by 3} \\
x &= -3.
\end{aligned}
$$

<div class="warning" markdown>

Watch out: dividing first also works, as long as you divide every term. Dividing both sides by 3 gives $x + \frac{11}{3} = \frac{2}{3}$, and then $x = \frac{2}{3} - \frac{11}{3} = -3$, the same answer with more fractions. Writing $x + 11 = \frac{2}{3}$ divides only one term of the left side, and it gives the wrong answer $x = -\frac{31}{3}$.

</div>

Step 4: the variable is alone, so the solution is $x = -3$, and the solution set is $\{-3\}$. A negative solution is fine.

Step 5: check in the original equation. The left side is $3(-3) + 11 = -9 + 11 = 2$, and the right side is 2. They match.

</div>

<div class="example" markdown>

### Example 2: a fraction as the coefficient

Solve $\frac{2}{3}x - 4 = 6$.

The variable was multiplied by $\frac{2}{3}$, then 4 was subtracted (Step 2). Undo the subtraction by adding 4 to both sides, which gives $\frac{2}{3}x = 10$.

To undo multiplying by $\frac{2}{3}$, divide by $\frac{2}{3}$, which is the same as multiplying by its reciprocal $\frac{3}{2}$. Since $\frac{3}{2} \cdot \frac{2}{3} = 1$, the left side becomes $1x = x$:

$$
x = \frac{3}{2} \cdot 10 = 15.
$$

Multiplying both sides by $\frac{2}{3}$ instead is a common slip. It gives $\frac{4}{9}x = \frac{20}{3}$, which is true but no closer to the answer.

Check: $\frac{2}{3} \cdot 15 = 10$ and $10 - 4 = 6$, which is the right side.

</div>

<div class="example" markdown>

### Example 3: a minus sign on the variable, and the variable on the right

Solve (a) $12 - x = 20$ and (b) $-5 = \frac{x}{4} + 2$.

(a) Subtract 12 from both sides to get $-x = 8$. This is not solved yet, because $-x$ means $-1 \cdot x$; it says the opposite of $x$ is 8. Divide both sides by $-1$ (or multiply by $-1$, which is the same thing) to get $x = -8$.

Check: $12 - (-8) = 12 + 8 = 20$.

(b) The variable is on the right, which changes nothing: an equation $a = b$ says the same thing as $b = a$. Subtract 2 from both sides to get $-7 = \frac{x}{4}$, then multiply both sides by 4 to get $-28 = x$, which you can write as $x = -28$.

Check: $\frac{-28}{4} + 2 = -7 + 2 = -5$, which is the left side.

</div>

<div class="example" markdown>

### Example 4: a gym membership (finish it yourself)

A gym charges a \$49 sign-up fee and \$22 a month. So far you have paid \$247 in total. How many months have you been a member?

Step 1: let $n$ be the number of months.

Step 2: the monthly fees come to $22n$ dollars, and the sign-up fee adds 49.

Step 3: the total paid is \$247, so

$$
22n + 49 = 247.
$$

Step 4, first pass: subtract 49 from both sides, which gives $22n = 198$.

Now finish Step 4, and check the answer against the words of the problem (Step 5).

<details class="solution" markdown>
<summary>Finish</summary>

Divide both sides by 22: $n = \frac{198}{22} = 9$. You have been a member for 9 months.

Check with the words: 9 months at \$22 is \$198, and adding the \$49 sign-up fee gives \$247, the amount paid. The answer is a whole number of months, as it should be.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: an operation done to one side only breaks the balance. From $x + 5 = 12$, subtracting 5 on the left alone gives $x = 12$, and the check fails: $12 + 5 = 17$, not 12. Subtract from both sides, $x = 12 - 5 = 7$, and the check passes.

</div>

<div class="warning" markdown>

Watch out: $-x = 8$ is one step short. It says $x$ is the opposite of 8, so $x = -8$. The check catches the slip: in Example 3, $x = 8$ would give $12 - 8 = 4$, not 20.

</div>

<div class="warning" markdown>

Watch out when the equation subtracts a negative. Rewrite $x - (-4) = -2$ as $x + 4 = -2$ first, then subtract 4 from both sides to get $x = -6$. Treating the two minus signs as one and adding 4 gives $x = 2$, and $2 - (-4) = 6$, not $-2$.

</div>

<div class="warning" markdown>

Watch out: check in the original equation, not in a later line. If a slip turned $3x + 11 = 2$ into $3x = 9$, then $x = 3$ checks perfectly in $3x = 9$, and the error survives. Only the original equation can catch a mistake made on the way.

</div>

Untidy solutions are normal. The equation $3x = 1$ has the solution $x = \frac{1}{3}$, and that is the answer. Don't round it to 0.33 unless the question asks for a decimal, since $3 \times 0.33 = 0.99$, and the rounded number is not a solution.

Two operations are not allowed on both sides. Dividing by 0 is undefined, and multiplying by 0 turns every equation into $0 = 0$, as the look back after the theorem showed. An equation such as $0x = 5$ can't be solved by dividing by the coefficient; it has no solution at all, since $0x$ is 0 for every $x$. The next lesson sorts out these cases ([multi-step equations](04-multi-step-equations.md)).

A word problem can produce a solution that doesn't fit the situation, such as $-3$ tickets or $2.5$ people. That doesn't mean the algebra failed. It means the setup is wrong or the situation has no answer, so reread the problem before you report a number.

## Tricks and shortcuts

For a two-step equation with small numbers, think backwards in your head. For $3x + 2 = 14$, ask "what plus 2 is 14?" (12), then "3 times what is 12?" (4). This is Step 3 without writing it down, and it is a quick way to check a written answer.

Two patterns come up often enough to remember. For $\frac{x}{a} = b$ with $a \ne 0$, the solution is $x = ab$: from $\frac{x}{4} = -7$ you get $x = -28$. For $\frac{a}{b}x = c$ with $a$ and $b$ nonzero, multiply by the reciprocal: $x = \frac{b}{a} \cdot c$, as in Example 2.

When the coefficient is negative, divide by it with its sign. From $-4x = 12$, divide by $-4$ and get $x = -3$ in one step, rather than dividing by 4 and fixing the sign afterwards.

## In code

Sympy's `solve` returns the list of solutions. The second and third lines show why the fraction $\frac{2}{3}$ should be entered as `Rational(2, 3)`: plain Python turns `2/3` into a float before sympy sees it, and the answer comes back as a float too.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import symbols, Eq, solve, Rational

x = symbols("x")
print(solve(Eq(3*x + 11, 2), x))                # [-3]
print(solve(Eq(Rational(2, 3)*x - 4, 6), x))    # [15]
print(solve(Eq(2/3*x - 4, 6), x))               # [15.0000000000000]
print(solve(Eq(12 - x, 20), x))                 # [-8]
print((3*x + 11).subs(x, -3) == 2)              # True: the check in Step 5
```

`Eq(left, right)` builds the equation, since a single `=` in Python means assignment. The last line is the check: substitute the solution into the left side and compare with the right.

</details>

## FAQ

### Can I move a term to the other side and change its sign?

Yes, as long as you know what the shortcut stands for. "Move the $+11$ across and it becomes $-11$" is a quick way to say "subtract 11 from both sides". The shortcut only works for a term that is added or subtracted. A coefficient that multiplies is undone by dividing, so $3x = 12$ gives $x = \frac{12}{3} = 4$, never $x = 12 - 3$ or $x = -\frac{12}{3}$. If you are unsure, write the operation on both sides.

### Why is the answer sometimes written as a set?

The question "which numbers make this true?" can have one answer, several or none, and a set records all the cases in one notation. The solution set of $3x + 11 = 2$ is $\{-3\}$. The equation $x^2 = 9$ has the solution set $\{-3, 3\}$, and the next lesson meets an equation whose solution set is empty. Writing "$x = -3$" is fine when there is exactly one solution, which is the case for every equation in this lesson that has a solution at all.

### Why do I need to check if I followed the rules?

Because the rules guarantee the method, not your arithmetic. Each step produces an equivalent equation only if you carry it out correctly, and one sign slip produces a different equation with a different solution. Substituting into the original equation takes a few seconds and catches the slip, which is also why exams that give part marks reward it.

## Practice

### Warm-up

1\. Solve (a) $x + 9 = 4$, (b) $-6x = 42$ and (c) $\frac{x}{3} = -2$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Subtract 9 from both sides: $x = 4 - 9 = -5$.
- (b) Divide both sides by $-6$: $x = \frac{42}{-6} = -7$.
- (c) Multiply both sides by 3: $x = -6$.

Check: $-5 + 9 = 4$, $-6(-7) = 42$ and $\frac{-6}{3} = -2$.

</details>

2\. Without solving, decide whether each value is a solution of $5 - 3x = 11$: (a) $x = -2$, (b) $x = 2$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $5 - 3(-2) = 5 + 6 = 11$, which matches the right side, so $-2$ is a solution.

(b) $5 - 3(2) = 5 - 6 = -1$, and $-1 \ne 11$, so 2 is not a solution.

Check by solving: subtract 5 to get $-3x = 6$, and divide by $-3$ to get $x = -2$. The solution set is $\{-2\}$, which agrees with both parts.

</details>

3\. Solve (a) $4x - 9 = 15$ and (b) $5x + 2 = 4$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Add 9 to both sides: $4x = 24$. Divide by 4: $x = 6$.

(b) Subtract 2 from both sides: $5x = 2$. Divide by 5: $x = \frac{2}{5}$. The answer is a fraction, and that is fine.

Check: $4(6) - 9 = 24 - 9 = 15$, and $5 \cdot \frac{2}{5} + 2 = 2 + 2 = 4$.

</details>

### Standard

4\. Solve $\frac{3}{4}x + 5 = -1$.

<details class="solution" markdown>
<summary>Solution</summary>

Subtract 5 from both sides: $\frac{3}{4}x = -6$. Multiply both sides by the reciprocal $\frac{4}{3}$:

$$
x = \frac{4}{3} \cdot (-6) = -\frac{24}{3} = -8.
$$

Check: $\frac{3}{4} \cdot (-8) = -6$, and $-6 + 5 = -1$, which is the right side.

</details>

5\. Solve $7 - \frac{x}{2} = 10$.

<details class="solution" markdown>
<summary>Solution</summary>

Subtract 7 from both sides: $-\frac{x}{2} = 3$. The left side is $-\frac{1}{2}x$, so multiply both sides by its reciprocal, $-2$:

$$
x = (-2)(3) = -6.
$$

Check: $7 - \frac{-6}{2} = 7 - (-3) = 10$.

</details>

6\. A part-time job pays \$18 an hour, plus a \$40 bonus for each shift you work. How many hours must one shift last for you to earn \$310 from it? Write an equation, solve it and check.

<details class="solution" markdown>
<summary>Solution</summary>

Let $t$ be the length of the shift in hours. The hourly pay is $18t$ dollars, and the bonus adds 40, so

$$
18t + 40 = 310.
$$

Subtract 40 from both sides: $18t = 270$. Divide by 18: $t = 15$. The shift must last 15 hours.

Check with the words: 15 hours at \$18 is \$270, and the \$40 bonus brings it to \$310. (A 15-hour shift is long, but the algebra answers the question that was asked.)

</details>

### Challenge

7\. The Celsius temperature for a Fahrenheit reading $F$ is $\frac{5}{9}(F - 32)$, from [measurement and unit conversion](../../01-elementary/15-measurement-and-unit-conversion.md). (a) Which Fahrenheit reading is 37°C, normal body temperature? (b) Which is $-10$°C?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The equation is $\frac{5}{9}(F - 32) = 37$. The last operation done to $F$ was multiplying by $\frac{5}{9}$, so undo it first: multiply both sides by $\frac{9}{5}$, which gives $F - 32 = \frac{9}{5} \cdot 37 = 66.6$. Then add 32: $F = 98.6$. So 37°C is 98.6°F.

(b) The equation is $\frac{5}{9}(F - 32) = -10$. Multiply both sides by $\frac{9}{5}$: $F - 32 = -18$. Add 32: $F = 14$. So $-10$°C is 14°F.

Notice the order of Step 3: in $\frac{5}{9}(F - 32)$, the subtraction happens first and the multiplication last, so the multiplication is undone first.

Check: $\frac{5}{9}(98.6 - 32) = \frac{5}{9} \cdot 66.6 = 37$, and $\frac{5}{9}(14 - 32) = \frac{5}{9}(-18) = -10$.

</details>

8\. This one reviews [percents](../02-ratios-rates-percents/03-percents.md). You use a \$10 coupon on a jacket, and 13% HST is charged on the price after the coupon. You pay \$62.15. What was the jacket's price before the coupon?

<details class="solution" markdown>
<summary>Solution</summary>

Let $p$ be the price in dollars before the coupon. After the coupon it is $p - 10$, and adding 13% HST multiplies that by 1.13, so

$$
1.13(p - 10) = 62.15.
$$

The last operation done to $p$ was multiplying by 1.13, so divide both sides by 1.13 first: $p - 10 = 55$. Then add 10: $p = 65$. The jacket was \$65.

Check with the words: \$65 minus the \$10 coupon is \$55, and $1.13 \times 55 = 62.15$, the amount paid.

</details>

## Where this shows up

- The next lesson, [multi-step equations](04-multi-step-equations.md), puts the variable on both sides and adds brackets and fractions, and [linear and literal equations](../../03-high-school/01-algebra-foundations/02-linear-and-literal-equations.md) solves formulas for one letter in terms of the others.
- Undoing operations in reverse order is how an inverse function is built: if $f$ multiplies by 3 and then adds 11, its inverse subtracts 11 and then divides by 3 ([composition and inverse functions](../../03-high-school/03-functions/05-composition-and-inverse-functions.md)). In code, an array of 4-byte integers that starts at memory address 1000 stores element $i$ at address $1000 + 4i$; the element at address 1048 is found by solving $1000 + 4i = 1048$, which gives $i = 12$.
- In economics, if $200 - 40p$ cups of coffee sell each day at a price of $p$ dollars, the price at which 60 cups sell solves $200 - 40p = 60$, so $p = 3.5$ dollars. Setting quantities equal like this is the start of supply and demand equilibrium algebra<!-- link: ../../07-economics-math/02-markets/03-supply-and-demand-equilibrium-algebra.md -->.
