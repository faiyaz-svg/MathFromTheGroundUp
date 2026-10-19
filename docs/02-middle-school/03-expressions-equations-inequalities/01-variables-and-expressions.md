# Variables and expressions

After this lesson you can name the terms, coefficients and constant term of an expression, evaluate an expression by substituting numbers (negative ones included), and turn a phrase such as "5 less than twice a number" into an expression.

Before this: [properties of operations](../../01-elementary/04-properties-of-operations.md), [integer arithmetic and sign rules](../01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md), and [exponents and order of operations](../01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Name the terms of $4x^2 - x + 7$, the coefficient of each term that contains $x$, and the constant term.
2. Evaluate $3x^2 - 2x$ when $x = -4$.
3. Write "7 less than three times a number $n$" as an expression.

<details class="solution" markdown>
<summary>Answers</summary>

1. The terms are $4x^2$, $-x$ and $7$. The coefficients are $4$ and $-1$, since $-x$ means $-1 \cdot x$, and the constant term is 7.
2. Put the value in brackets: $3(-4)^2 - 2(-4) = 3 \cdot 16 + 8 = 56$.
3. $3n - 7$. Check with $n = 10$: three times 10 is 30, 7 less is 23, and $3 \cdot 10 - 7 = 23$.

</details>

## The idea

A car-share service charges \$5 to unlock a car and \$0.40 for each minute you drive. A 20-minute trip costs $5 + 0.40 \times 20 = 13$ dollars, and a 45-minute trip costs $5 + 0.40 \times 45 = 23$ dollars. The calculation has the same shape every time; only the number of minutes changes.

Instead of writing the calculation out for each trip, give the number of minutes a name, say $t$, and write the rule once:

$$
\text{cost in dollars} = 5 + 0.40t.
$$

Here $0.40t$ means $0.40$ times $t$. The letter $t$ is a name for a number. For a 20-minute trip you replace $t$ with 20, and for a 45-minute trip you replace it with 45.

A letter can name a number in two ways. In the rule above, $t$ varies: it stands for whichever trip you have in mind, and the rule works for all of them. In the question "your trip cost \$17, so how long was it?", the letter $t$ is an unknown, one particular number we haven't found yet. (It is 30, since $5 + 0.40 \times 30 = 17$.) Algebra handles both kinds with the same rules, so one letter can do either job.

If you program, a variable in code is a close cousin, with one difference. In code, `t = t + 1` is a command that changes the value stored in `t`. In math a letter keeps one value throughout a problem, so the equation $t = t + 1$ claims that some number equals one more than itself, and that is false for every number. The `=` in code assigns a value, while the $=$ in math states that two things are equal.

## Definitions

A **variable** is a symbol, usually a letter, that stands for a number. The number may be unknown (one value that we want to find), or it may range over a set of values (every possible number of minutes).

In plain words, a variable is a name for a number. The rules $5 + 0.40t$ and $5 + 0.40m$ say the same thing, because the letter is only a label. Pick one that reminds you what it stands for, such as $t$ for time.

An **expression** is a combination of numbers, variables and operations, possibly with brackets, that gives a number once every variable is replaced by a number. Three examples are $5 + 0.40t$, $3x^2 - 2x$ and $\frac{n + 1}{2}$. An expression has no equals sign.

An equation, by contrast, says that two expressions are equal, as in $5 + 0.40t = 17$. An expression names a number, while an equation is a sentence that is true or false. The expression $5 + 0.40t$ has the value 13 when $t = 20$, and the equation $5 + 0.40t = 17$ is true when $t = 30$ and false for every other $t$. You evaluate or simplify an expression, and you solve an equation; equations start in [one- and two-step equations](03-one-and-two-step-equations.md).

A **term** of an expression is one of the parts that are added together. Subtracting a number is the same as adding its opposite, so each term carries the sign in front of it. For example, $4x^2 - x + 7$ is $4x^2 + (-x) + 7$, and its terms are $4x^2$, $-x$ and $7$.

The **coefficient** of a term is its number factor, the number that multiplies the variable part. The coefficient of $4x^2$ is 4, and the coefficient of $-x$ is $-1$, because $-x = -1 \cdot x$. A coefficient can be a fraction: $\frac{x}{3} = \frac{1}{3}x$, so its coefficient is $\frac{1}{3}$.

A **constant term** is a term with no variable, such as the 7 in $4x^2 - x + 7$. Its value stays the same whatever the variable is. The word "constant" also names a letter that stands for a fixed number: in $ax + b$, the letters $a$ and $b$ are constants and $x$ is the variable. This book uses $a$, $b$ and $c$ that way (see [symbols and notation](../../reference/symbols-and-notation.md#one-letter-one-meaning-in-this-book)).

**Like terms** are terms with the same variables, each raised to the same power. Only their coefficients may differ. So $3x^2$ and $-5x^2$ are like terms, and so are $2xy$ and $7yx$, since $yx = xy$. But $3x^2$ and $3x$ are not like terms, and neither are $4x$ and $4y$. In plain words, like terms count the same kind of thing, the way 3 apples and 5 apples do. The next lesson combines them into one term.

To **evaluate** an expression is to replace each variable with a given number and work out the value. Replacing a variable with a number, or with another expression, is called **substitution**. For example, evaluating $5 + 0.40t$ at $t = 20$ gives 13.

### How multiplication is written

Algebra drops the $\times$ sign, which looks too much like the letter $x$. A number times a letter, or a letter times a letter, is written side by side, and this is called **implied multiplication**: $3x$ means $3 \cdot x$, $xy$ means $x \cdot y$, and $2(x + 1)$ means $2 \cdot (x + 1)$. The raised dot $\cdot$ means "times" wherever side by side would be misread, such as between two numbers, since $3 \cdot 4$ is 12 while $34$ is thirty-four.

A few more habits go with it. The number comes first ($3x$, never $x3$). A coefficient of 1 isn't written, so $x$ means $1x$ and $-x$ means $-1x$. Division is usually a fraction bar, $\frac{x}{4}$ instead of $x \div 4$. An exponent applies only to what is right before it. This table shows each habit, with the value it gives when $x = 2$ and $y = 5$:

| Written | Means | Value when $x = 2$ and $y = 5$ |
|---|---|---|
| $3x$ | $3 \cdot x$ | $6$ |
| $xy$ | $x \cdot y$ | $10$ |
| $2(x + y)$ | $2 \cdot (x + y)$ | $14$ |
| $3x^2$ | $3 \cdot (x^2)$ | $12$ |
| $(3x)^2$ | $(3 \cdot x)^2$ | $36$ |
| $-x^2$ | $-(x^2)$ | $-4$ |
| $\frac{x + y}{2}$ | $(x + y) \div 2$ | $3.5$ |

The fraction bar groups like brackets: everything above it is divided by everything below it.

## How to do it

### Reading an expression

1. Split the expression into terms at each $+$ or $-$ sign that is not inside brackets, a fraction or an exponent. Each term keeps the sign in front of it.
2. In each term, the number in front of the variables is the coefficient. A term written $x$ has coefficient 1, and $-x$ has coefficient $-1$.
3. A term with no variable is a constant term.
4. Like terms have the same letters with the same exponents. Compare the letters and exponents, never the coefficients.

### Evaluating an expression

1. Write the expression again with an empty pair of brackets in place of each variable.
2. Put each value into its brackets. Negative numbers and fractions must go in brackets, and brackets around a positive whole number do no harm.
3. Work out the value in the order of operations: brackets, then exponents, then multiplication and division from left to right, then addition and subtraction from left to right.
4. Check: work it out again a different way, or check the sign and the size of the answer.

### Writing an expression from words

1. Choose a letter for the unknown number, and say in words what it stands for.
2. Translate the phrase one piece at a time, using the table below.
3. Put brackets around a sum or difference that is multiplied, divided or raised to a power as a whole.
4. Check by choosing a number, such as 10, and working out both the phrase in words and your expression. They must agree.

| Words | Operation | Example | Expression |
|---|---|---|---|
| sum, plus, more than, increased by | addition | 4 more than $n$ | $n + 4$ |
| difference, minus, decreased by | subtraction | $n$ decreased by 4 | $n - 4$ |
| less than, subtracted from | subtraction, in reverse order | 4 less than $n$ | $n - 4$ |
| product, times, twice, of (after a fraction or percent) | multiplication | twice $n$ | $2n$ |
| quotient, divided by, per | division | the quotient of $n$ and 4 | $\frac{n}{4}$ |
| square of, squared, cubed | power | the square of $n$ | $n^2$ |

The "less than" row is the one that trips people up. The phrase "4 less than $n$" starts from $n$ and takes 4 away, so it is $n - 4$, even though the 4 is said first. "4 subtracted from $n$" works the same way. In "the difference of $n$ and 4", the order is as written: $n - 4$.

## Worked examples

<div class="example" markdown>

### Example 1: evaluating with a negative value

Evaluate $2x^2 - 3xy + y$ when $x = -3$ and $y = 4$.

Step 1: write the expression with empty brackets in place of the variables:

$$
2(\ \ )^2 - 3(\ \ )(\ \ ) + (\ \ ).
$$

Step 2: put $-3$ in each bracket that held $x$, and 4 in each bracket that held $y$:

$$
2(-3)^2 - 3(-3)(4) + (4).
$$

<div class="warning" markdown>

Watch out: without the brackets, the first term would read $2 \cdot -3^2$. Exponents come before negation, so $-3^2$ means $-(3^2) = -9$, and the term would come out as $-18$ instead of $18$. The bracket tells you that the whole number $-3$ is squared.

</div>

Step 3: exponents first, so $(-3)^2 = 9$. Then the multiplications: $2 \cdot 9 = 18$ and $3 \cdot (-3) \cdot 4 = -36$. Subtracting $-36$ is the same as adding 36:

$$
\begin{aligned}
2(-3)^2 - 3(-3)(4) + 4 &= 18 - (-36) + 4 \\
&= 18 + 36 + 4 \\
&= 58.
\end{aligned}
$$

Step 4: check the signs before trusting the number. The term $2x^2$ is positive for every nonzero $x$. With $x$ negative and $y$ positive, the product $xy$ is negative, so $-3xy$ is positive. And $y = 4$ is positive. All three terms are positive, so the value must be positive, and the three term values 18, 36 and 4 add to 58. The [In code](#in-code) box gets the same answer by computer.

</div>

<div class="example" markdown>

### Example 2: four phrases with the same words

Write each phrase as an expression in $n$: (a) 5 less than twice a number, (b) twice the sum of a number and 5, (c) the sum of twice a number and 5, and (d) 5 subtracted from the quotient of a number and 3.

- (a) Twice the number is $2n$, and 5 less than that is $2n - 5$. The reversed order, $5 - 2n$, is the classic slip.
- (b) The sum is $n + 5$, and twice the whole sum is $2(n + 5)$. Step 3 calls for the brackets.
- (c) Twice the number is $2n$, and the sum with 5 is $2n + 5$.
- (d) The quotient is $\frac{n}{3}$, and 5 subtracted from it is $\frac{n}{3} - 5$.

Check with $n = 12$, chosen so that (d) divides evenly. In (a), twice 12 is 24 and 5 less is 19, and $2 \cdot 12 - 5 = 19$, while the reversed $5 - 2 \cdot 12 = -19$ fails. In (b), the sum is 17 and twice it is 34, and $2(12 + 5) = 34$. In (c), $2 \cdot 12 + 5 = 29$. In (d), $12 \div 3 = 4$ and $4 - 5 = -1$. Phrases (b) and (c) use the same words in a different order and give 34 and 29, so the brackets matter.

</div>

<div class="example" markdown>

### Example 3: coefficients hidden by the notation

Name the terms, coefficients and constant term of $x^2 - \frac{x}{3} - 4xy + 9 - y$.

Splitting at each sign (Step 1) gives five terms: $x^2$, $-\frac{x}{3}$, $-4xy$, $9$ and $-y$. The coefficients are 1 (nothing written means 1), $-\frac{1}{3}$ (since $\frac{x}{3} = \frac{1}{3}x$), $-4$ and $-1$. The constant term is 9. No two terms are like terms: $x^2$ and $x$ have different exponents, and $xy$ has a different set of letters from both $x$ and $y$.

Now compare $6x - 2x^2 + x - 8 + 3x^2$. Its like terms are $6x$ and $x$, and also $-2x^2$ and $3x^2$. The constant $-8$ has no partner.

Brackets and fraction bars hide signs from Step 1. The expression $2(x + 1) - 5$ has two terms, $2(x + 1)$ and $-5$, because the $+$ inside the brackets doesn't split the expression. The same goes for $\frac{x + 1}{2}$, which is one term as written.

Check by rewriting the first expression as a sum: $1x^2 + \left(-\frac{1}{3}\right)x + (-4)xy + 9 + (-1)y$. The five numbers in front of the letters, and the 9, are the coefficients and the constant term listed above.

</div>

<div class="example" markdown>

### Example 4: a phone bill (finish it yourself)

A phone plan costs \$35 a month for up to 20 GB of data, plus \$7.50 for each GB over 20. Write the cost for a month in which you use $g$ GB, where $g$ is at least 20, and evaluate it for $g = 23.5$.

Step 1: let $g$ be the number of GB used in the month. The GB over 20 are $g - 20$.

Step 2 and Step 3: each GB over 20 costs \$7.50, so the extra charge is $7.50(g - 20)$. The brackets are needed because the whole difference is multiplied. The monthly cost in dollars is

$$
35 + 7.50(g - 20).
$$

To evaluate it at $g = 23.5$, substitute:

$$
35 + 7.50(23.5 - 20).
$$

Now work out the value with the order of operations, and check it.

<details class="solution" markdown>
<summary>Finish</summary>

Brackets first: $23.5 - 20 = 3.5$. Then multiply, $7.50 \times 3.5 = 26.25$, and add, $35 + 26.25 = 61.25$. The bill is \$61.25.

Check: 3 extra GB cost $3 \times 7.50 = 22.50$ dollars and the half GB costs \$3.75, so the extra charge is \$26.25, as above. At $g = 20$ the expression gives $35 + 7.50 \cdot 0 = 35$, the base price, as it should. Without the brackets you would get $35 + 7.50 \cdot 23.5 - 20 = 191.25$, which is far too much.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the square of a substituted negative. With $x = -5$, the three expressions $x^2$, $-x^2$ and $(-x)^2$ give

$$
(-5)^2 = 25, \qquad -(-5)^2 = -25, \qquad (-(-5))^2 = 5^2 = 25.
$$

Writing $-5^2$ for $x^2$ gives $-25$, which is wrong; Python agrees with the rule, since `-5**2` is `-25`. The [common mistakes](../../reference/common-mistakes.md#squaring-a-negative-number-without-brackets) page has this one too.

</div>

<div class="warning" markdown>

Watch out: implied multiplication needs a sign once numbers go in. The term $3x$ at $x = 4$ is $3(4) = 12$, not 34, and $xy$ at $x = 2$ and $y = 7$ is $2 \cdot 7 = 14$, not 27. The empty brackets of Step 1 prevent this.

</div>

<div class="warning" markdown>

Watch out: $2x$ and $x^2$ are different. The first is $x + x$ and the second is $x \cdot x$. At $x = 3$ they are 6 and 9. They happen to agree at $x = 0$ and $x = 2$, so a check with one of those values can hide the slip.

</div>

A minus sign in front of a variable doesn't make the value negative. The expression $-x$ is the opposite of $x$, so at $x = -6$ it is $-(-6) = 6$, a positive number. Read $-x$ as "the opposite of $x$" rather than "negative $x$" and the sign takes care of itself.

An expression can have no value for some numbers. In $\frac{1}{x - 2}$, putting in $x = 2$ gives $\frac{1}{0}$, and division by zero is undefined ([division facts and remainders](../../01-elementary/06-division-facts-and-remainders.md#edge-cases-and-common-mistakes)). The expression has a value for every other $x$, which is often written "for $x \ne 2$".

Within one expression, the same letter means the same number every time it appears. In $x + 2x$, both copies of $x$ get the same value. Different letters may stand for different numbers or for the same number, so $x + y$ at $x = 3$ and $y = 3$ is a perfectly good 6.

## Tricks and shortcuts

Test with numbers that aren't special. The values 0 and 1 hide mistakes, because $1^2 = 1$ and $0$ times anything is $0$. A value such as 3, 10 or $-2$ catches far more slips.

Check the sign before you check the number, as in Example 1. If every term is positive, a negative answer means an arithmetic slip, and you know before you redo the arithmetic.

To see how a quantity changes, evaluate the expression at evenly spaced values and make a table. The car-share cost $5 + 0.40t$ at 10, 20, 30 and 40 minutes is 9, 13, 17 and 21 dollars. Each extra 10 minutes adds $0.40 \times 10 = 4$ dollars, the coefficient times the step. This steady change is the slope of [slope and linear equations](../05-linear-relationships-and-functions/02-slope-and-linear-equations.md).

## In code

Substituting by hand is like replacing text, and replacing text without brackets makes the $-3^2$ mistake. These lines evaluate Example 1 with sympy, which substitutes values, and then by replacing text in a string and running it with Python's `eval`.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import symbols

x, y = symbols("x y")
expr = 2*x**2 - 3*x*y + y
print(expr.subs({x: -3, y: 4}))                 # 58

text = "2*x**2 - 3*x*y + y"
no_brackets = text.replace("x", "-3").replace("y", "4")
print(no_brackets, "=", eval(no_brackets))      # 2*-3**2 - 3*-3*4 + 4 = 22
with_brackets = text.replace("x", "(-3)").replace("y", "(4)")
print(with_brackets, "=", eval(with_brackets))  # 2*(-3)**2 - 3*(-3)*(4) + (4) = 58
```

The `subs` method puts in $-3$ as a number, so the brackets come for free. The text version without brackets reads `-3**2` as $-(3^2)$ and gets 22. C programmers meet the same bug in macros: `#define SQUARE(x) x*x` turns `SQUARE(a + 1)` into `a + 1*a + 1`, which is $2a + 1$, so macros are written with brackets around every argument, as `((x)*(x))`.

</details>

## FAQ

### Why use letters at all?

A letter lets you write a rule once and use it for every value, as the car-share rule does. It also lets you say something about every number at the same time. The statement "for every number $x$, $2(x + 3) = 2x + 6$" covers infinitely many arithmetic facts in one line, and proving statements of that kind is what the [next lesson](02-equivalent-expressions.md) starts and the proofs folder finishes.

### How should I read a division followed by brackets?

By the rules in [exponents and order of operations](../01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#does-a-product-written-without-a-times-sign-come-first), implied multiplication has the same rank as division, so $6 \div 2(1 + 2)$ is $6 \div 2 \cdot 3 = 9$, worked from left to right. Some calculators treat a side-by-side product as one unit and give 1 instead, so in practice the expression is ambiguous. Algebra meets the same problem in $1/2x$. By the rules it means $\frac{1}{2} \cdot x$, but plenty of people read it as $\frac{1}{2x}$. Write $\frac{1}{2}x$ or $\frac{1}{2x}$, whichever you mean, and nobody has to guess.

### Does it matter which letter I use?

Not for the math. The expressions $3t + 1$ and $3x + 1$ describe the same rule, and renaming the letter everywhere changes nothing. What matters is consistency: inside one problem a letter keeps one meaning, and this book gives most letters a default job ($n$ for counts, $t$ for time, $x$ for an unknown real number) so that solutions are easier to read.

## Practice

### Warm-up

1\. For $6y^2 - y + \frac{y}{2} - 10$, name the terms, the coefficient of each term that contains $y$, the constant term, and the like terms.

<details class="solution" markdown>
<summary>Solution</summary>

The terms are $6y^2$, $-y$, $\frac{y}{2}$ and $-10$. The coefficients are 6, $-1$ and $\frac{1}{2}$, since $\frac{y}{2} = \frac{1}{2}y$. The constant term is $-10$, sign included. The like terms are $-y$ and $\frac{y}{2}$: both are $y$ to the first power. The term $6y^2$ has a different exponent.

Check by rewriting as a sum: $6y^2 + (-1)y + \frac{1}{2}y + (-10)$.

</details>

2\. Evaluate $5 - 2x$ when (a) $x = 3$, (b) $x = -3$ and (c) $x = \frac{1}{2}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $5 - 2(3) = 5 - 6 = -1$.
- (b) $5 - 2(-3) = 5 + 6 = 11$.
- (c) $5 - 2\left(\frac{1}{2}\right) = 5 - 1 = 4$.

Check: each time $x$ goes up by 1, the value goes down by 2. Going from $x = -3$ to $x = 3$ is 6 steps up, so the value should fall by 12, and $11 - 12 = -1$ matches (a).

</details>

3\. Write each phrase as an expression in $n$: (a) 8 more than a number, (b) 6 times a number, decreased by 1, (c) 3 less than the square of a number, (d) the sum of a number and 4, divided by 2.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $n + 8$.
- (b) $6n - 1$.
- (c) $n^2 - 3$. "Less than" reverses the order, so it is not $3 - n^2$.
- (d) $\frac{n + 4}{2}$. The whole sum is divided, so the fraction bar covers both terms.

Check with $n = 10$: (a) 18, (b) $60 - 1 = 59$, (c) $100 - 3 = 97$, (d) $14 \div 2 = 7$. Each matches the phrase worked out in words.

</details>

### Standard

4\. Evaluate $\dfrac{2x - y}{x^2 + y}$ when $x = -3$ and $y = 4$. Then, keeping $x = -3$, find the value of $y$ for which the expression has no value.

<details class="solution" markdown>
<summary>Solution</summary>

Substitute with brackets. The numerator is $2(-3) - (4) = -6 - 4 = -10$, and the denominator is $(-3)^2 + (4) = 9 + 4 = 13$. So the value is $-\frac{10}{13}$. The answer is a negative fraction, and that is fine.

With $x = -3$, the denominator is $9 + y$, which is 0 when $y = -9$. Division by zero is undefined, so the expression has no value at $y = -9$.

Check: as decimals, $-10 \div 13 \approx -0.769$, and a negative numerator over a positive denominator gives a negative value. For the second part, $(-3)^2 + (-9) = 9 - 9 = 0$.

</details>

5\. Concert tickets cost \$45 each, plus a \$6.50 service fee per ticket, plus one \$4 fee per order. Write an expression for the cost of $n$ tickets bought in one order, find the cost of 4 tickets, and name the like terms in your expression.

<details class="solution" markdown>
<summary>Solution</summary>

Let $n$ be the number of tickets. The ticket prices are $45n$, the service fees are $6.50n$, and the order fee is 4, so the cost in dollars is

$$
45n + 6.50n + 4.
$$

For 4 tickets: $45(4) + 6.50(4) + 4 = 180 + 26 + 4 = 210$, so \$210.00. The like terms are $45n$ and $6.50n$; both are a number times $n$. The next lesson combines them into $51.50n$.

Check: each ticket really costs $45 + 6.50 = 51.50$ dollars, and $4 \times 51.50 + 4 = 206 + 4 = 210$.

</details>

6\. Write (a) three times the difference of a number and 7, and (b) the difference of three times a number and 7, as expressions in $n$. Evaluate both at $n = 10$ and at $n = -2$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The difference is $n - 7$, and three times the whole difference is $3(n - 7)$. At $n = 10$ it is $3(3) = 9$, and at $n = -2$ it is $3(-9) = -27$.

(b) Three times the number is $3n$, and the difference with 7 is $3n - 7$. At $n = 10$ it is $30 - 7 = 23$, and at $n = -2$ it is $-6 - 7 = -13$.

Check: the two expressions differ by 14 both times, since $23 - 9 = 14$ and $-13 - (-27) = 14$. That is no accident. Multiplying out $3(n - 7)$ gives $3n - 21$, which is 14 less than $3n - 7$ for every $n$, and the [next lesson](02-equivalent-expressions.md) shows how to see this.

</details>

### Challenge

7\. Here is a number trick: think of a number, double it, add 6, divide by 2, then subtract the number you started with. Write the trick as one expression in $n$, building it one instruction at a time, and evaluate it for $n = 5$, $n = -8$ and $n = \frac{1}{3}$. What do you notice?

<details class="solution" markdown>
<summary>Solution</summary>

Build it one instruction at a time. Doubling gives $2n$, and adding 6 gives $2n + 6$. Dividing by 2 divides the whole sum, so it is $\frac{2n + 6}{2}$. Subtracting the starting number gives

$$
\frac{2n + 6}{2} - n.
$$

At $n = 5$: $\frac{10 + 6}{2} - 5 = 8 - 5 = 3$.

At $n = -8$: $\frac{-16 + 6}{2} - (-8) = \frac{-10}{2} + 8 = -5 + 8 = 3$.

At $n = \frac{1}{3}$: $\frac{\frac{2}{3} + 6}{2} - \frac{1}{3} = \frac{20}{3} \div 2 - \frac{1}{3} = \frac{10}{3} - \frac{1}{3} = 3$.

The answer is 3 every time. Three examples can't prove that it is always 3, but they make it a good guess, and Practice problem 5 of [equivalent expressions](02-equivalent-expressions.md#practice) proves it.

Check $n = 5$ in words: double 5 is 10, add 6 is 16, half of 16 is 8, and $8 - 5 = 3$.

</details>

8\. This one reviews [adding and subtracting fractions](../../01-elementary/10-adding-and-subtracting-fractions.md) and [multiplying and dividing fractions](../../01-elementary/11-multiplying-and-dividing-fractions.md). Evaluate $\frac{x}{3} - \frac{y}{4}$ when $x = \frac{1}{2}$ and $y = -\frac{2}{3}$.

<details class="solution" markdown>
<summary>Solution</summary>

Substitute with brackets: $\frac{x}{3}$ becomes $\left(\frac{1}{2}\right) \div 3 = \frac{1}{2} \times \frac{1}{3} = \frac{1}{6}$, and $\frac{y}{4}$ becomes $\left(-\frac{2}{3}\right) \div 4 = -\frac{2}{12} = -\frac{1}{6}$. Then

$$
\frac{1}{6} - \left(-\frac{1}{6}\right) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}.
$$

Check with decimals: $0.5 \div 3 \approx 0.1667$ and $-0.6667 \div 4 \approx -0.1667$, and $0.1667 - (-0.1667) \approx 0.3333$, which is about $\frac{1}{3}$.

</details>

## Where this shows up

- The next lesson, [equivalent expressions](02-equivalent-expressions.md), rewrites an expression without changing its value for any number, and [one- and two-step equations](03-one-and-two-step-equations.md) finds the value of an unknown.
- Economics writes costs the same way as the car-share fare: a fixed part plus a part per unit. A firm with \$500 of fixed costs and \$12 of cost per unit has total cost $500 + 12n$ for $n$ units (production and cost functions<!-- link: ../../07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md -->).
- In code, a function parameter is a variable in the "varies" sense: `def cost(t): return 5 + 0.40 * t` is the car-share expression with a name. Substituting an expression for a variable, brackets and all, comes back in function notation such as $f(x + h)$ ([introduction to functions](../05-linear-relationships-and-functions/03-intro-to-functions.md)).
