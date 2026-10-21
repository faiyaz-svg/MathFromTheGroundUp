# Rational expressions

After this lesson you can find the values a rational expression is not allowed to take, simplify it by cancelling common factors, and add, subtract, multiply and divide rational expressions, including complex fractions, without losing track of the excluded values.

Before this: [factoring polynomials](../04-radicals-and-polynomials/03-factoring-polynomials.md), [adding and subtracting fractions](../../01-elementary/10-adding-and-subtracting-fractions.md) and [rational number arithmetic](../../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Simplify $\dfrac{x^2 - 9}{x^2 + x - 6}$ and state every value of $x$ that is excluded.
2. Write $\dfrac{1}{x - 1} + \dfrac{1}{x + 1}$ as one fraction.
3. Simplify $\dfrac{x^2 - 4}{x + 3} \div \dfrac{x + 2}{x^2 - 9}$ and state the excluded values.

<details class="solution" markdown>
<summary>Answers</summary>

1. Factor: $\frac{(x - 3)(x + 3)}{(x + 3)(x - 2)} = \frac{x - 3}{x - 2}$, with $x \ne -3$ and $x \ne 2$. The value $-3$ stays excluded even though its factor cancelled.
2. The common denominator is $(x - 1)(x + 1)$, so the sum is $\frac{(x + 1) + (x - 1)}{(x - 1)(x + 1)} = \frac{2x}{x^2 - 1}$, with $x \ne \pm 1$.
3. Multiply by the reciprocal: $\frac{(x - 2)(x + 2)}{x + 3} \cdot \frac{(x - 3)(x + 3)}{x + 2} = (x - 2)(x - 3)$. The excluded values are $-3$ (a denominator), $3$ (a denominator in the second fraction) and $-2$ (the divisor is 0 there), so $x \ne -3, -2, 3$.

</details>

## The idea

Take the fraction $\frac{12}{18}$. Both numbers contain the factors 2 and 3, since $12 = 2 \cdot 2 \cdot 3$ and $18 = 2 \cdot 3 \cdot 3$. Cancel the common factors $2 \cdot 3$ and what is left is $\frac{2}{3}$. Nothing about this needs the numbers to be integers: it needs only that the top and bottom are written as products and that you cancel a factor, not a piece of a sum. The same method works when the top and bottom are polynomials, which you can now factor.

Suppose a small business pays \$5,000 in fixed costs and \$12 for each unit it makes. Making $q$ units costs $5000 + 12q$ dollars, so the cost per unit is $\frac{5000 + 12q}{q}$. That is a fraction of two polynomials in $q$, and it is only meaningful for $q \ne 0$, because a business that makes no units has no cost per unit. Fractions like this one are called rational expressions, after "ratio", and the whole chapter is about them: their graphs, the equations they make and the inequalities they make.

Everything in this lesson is fraction arithmetic from elementary school with one extra duty. Before you cancel anything, the bottom of each fraction has to be factored. And every value of the variable that makes a bottom 0 has to be remembered, because dividing by zero is not allowed, and a simplified answer must not allow what the original did not.

## Definitions

A **rational expression** is a fraction $\frac{p(x)}{q(x)}$ in which $p(x)$ and $q(x)$ are polynomials and $q(x)$ is not the zero polynomial. In plain words, it is to polynomials what a fraction of integers is to integers. The expressions $\frac{3}{x - 2}$, $\frac{x^2 - 9}{x^2 + x - 6}$ and $x + 1$ (which is $\frac{x + 1}{1}$) are all rational expressions, while $\frac{\sqrt{x}}{x}$ is not, because the numerator is not a polynomial.

The **domain** of a rational expression is the set of real numbers $x$ for which the denominator is not 0. A value of $x$ that makes a denominator 0 is an **excluded value**. In plain words, the domain is everything you may substitute, and the excluded values are the inputs where the expression has no meaning. For $\frac{x^2 - 9}{x^2 + x - 6}$ the denominator is $(x + 3)(x - 2)$, which is 0 at $x = -3$ and at $x = 2$, so the domain is every real number except $-3$ and $2$. This is the natural domain from [what is a function](../03-functions/01-what-is-a-function.md#how-to-do-it), applied to a quotient. Some denominators have no real zero, such as $x^2 + 4$, and then nothing is excluded.

Two rational expressions are **equivalent** when they have the same value at every real number where both are defined. A rational expression is in **lowest terms** (also called simplified) when its numerator and denominator have no common factor of degree 1 or more. In plain words, equivalent expressions give the same number for each allowed $x$, and lowest terms means there is nothing left to cancel. You may write $\frac{x^2 - 1}{x - 1} = x + 1$ only together with the condition $x \ne 1$, since the left side is undefined at 1 and the right side is 2 there.

The **least common denominator** (LCD) of several rational expressions is the lowest-degree polynomial that every denominator divides. To build it, factor each denominator completely and take every different factor once, to the highest power in which it appears in any single denominator. In plain words, it is the least common multiple from the [factors and multiples lesson](../../01-elementary/08-factors-multiples-and-primes.md), with polynomials in place of integers. For $2x$ and $3x^2$ the LCD is $6x^2$: the numbers 2 and 3 give 6, and the powers of $x$ give $x^2$.

A **complex fraction** is a fraction whose numerator, denominator or both contain fractions, such as $\dfrac{1 + \frac{1}{x}}{1 - \frac{1}{x^2}}$.

### Why a common factor can be cancelled

*Theorem (cancellation).* Let $a$, $b$ and $c$ be polynomials, with $b$ and $c$ not the zero polynomial. For every real number $x$ where $b(x)c(x) \ne 0$,

$$
\frac{a(x)\,c(x)}{b(x)\,c(x)} = \frac{a(x)}{b(x)}.
$$

We know that for numbers $A$, $B$ and $C$ with $B \ne 0$ and $C \ne 0$, $\frac{AC}{BC} = \frac{A}{B}$ (equivalent fractions, from [fractions and equivalent fractions](../../01-elementary/09-fractions-and-equivalent-fractions.md)). We want the same statement with polynomials. The plan is to pick one real number $x$ and turn the polynomials into numbers.

*Proof.* Fix a real $x$ with $b(x)c(x) \ne 0$. A product is 0 only if one of its factors is 0, so $b(x) \ne 0$ and $c(x) \ne 0$. Now $A = a(x)$, $B = b(x)$ and $C = c(x)$ are numbers that satisfy the conditions of the fact about numbers, so $\frac{a(x)c(x)}{b(x)c(x)} = \frac{a(x)}{b(x)}$. Since $x$ was any such number, the two sides are equal for every $x$ where the left side is defined. $\blacksquare$

Look back: the proof shows exactly what the rule needs, a common factor that multiplies the whole top and the whole bottom. It also shows why the excluded values stay. At a zero of $c$ the left side is undefined, but the right side may not be, so the two expressions are equal only on the domain of the left side.

## How to do it

### Simplifying a rational expression

1. Factor the numerator and the denominator completely, using the [factoring checklist](../04-radicals-and-polynomials/03-factoring-polynomials.md#the-factoring-checklist).
2. Write down the excluded values: the real zeros of every denominator in the original expression, before anything is cancelled.
3. Cancel each factor that appears in both the numerator and the denominator. A factor $(a - b)$ and a factor $(b - a)$ cancel to $-1$, because $b - a = -(a - b)$.
4. Write what is left, with the excluded values from Step 2 beside it.
5. Check by substituting a number that is not excluded into the original and the result. The two values must agree.

The rule in Step 3 is the one most often broken. You may cancel factors, which are things multiplied, and never terms, which are things added. In $\frac{x + 3}{3}$ the 3 on top is a term, so the expression does not simplify to $x + 1$: at $x = 3$ the first is $\frac{6}{3} = 2$ and the second is 4.

### Multiplying and dividing

1. Factor every numerator and every denominator.
2. To divide, replace the division by multiplication by the reciprocal of the divisor. Note that the divisor's own numerator is also an excluded value, since you cannot divide by 0.
3. Cancel factors that appear anywhere on top with factors that appear anywhere on the bottom, as in multiplying fractions of numbers ([multiplying and dividing fractions](../../01-elementary/11-multiplying-and-dividing-fractions.md)).
4. Multiply what remains, and state the excluded values from all the original denominators and the divisor.
5. Check with a test number.

### Adding and subtracting

1. Factor the denominators completely and build the LCD.
2. Rewrite each fraction with the LCD as its denominator. Multiply the top and the bottom of each fraction by the factors the LCD has and its denominator is missing.
3. Add or subtract the numerators. When subtracting, put the whole second numerator in brackets so the minus sign reaches every term.
4. Simplify the new numerator, then factor it. Cancel anything the numerator and the LCD share.
5. Write the excluded values from the original denominators, and check with a test number.

### Simplifying a complex fraction

There are two methods, and each works for every complex fraction.

1. Method A: combine the numerator into one fraction, combine the denominator into one fraction, and then divide, as in the steps above.
2. Method B: find the LCD of all the small fractions inside, multiply the whole numerator and the whole denominator by it, and simplify. Multiplying the top and the bottom by the same nonzero polynomial does not change the value.
3. Either way, the excluded values include the zeros of every inner denominator, and also the zeros of the main denominator of the complex fraction.

## Worked examples

<div class="example" markdown>

### Example 1: simplifying, and what stays excluded

Simplify $\dfrac{3x^2 - 12}{x^2 - x - 6}$.

Step 1: factor. The numerator has a common factor 3 and then a difference of squares: $3x^2 - 12 = 3(x^2 - 4) = 3(x - 2)(x + 2)$. The denominator is a trinomial with leading coefficient 1, and the pair $-3$ and $2$ has product $-6$ and sum $-1$, so $x^2 - x - 6 = (x - 3)(x + 2)$.

Step 2: the denominator $(x - 3)(x + 2)$ is 0 at $x = 3$ and at $x = -2$. Both are excluded, even though one of the factors is about to cancel.

Step 3: the factor $x + 2$ is on top and on bottom. The 3 on top is a constant multiplying the whole numerator, and there is no 3 in the denominator to cancel it with: the factor $x - 3$ is a different thing. So

$$
\frac{3(x - 2)(x + 2)}{(x - 3)(x + 2)} = \frac{3(x - 2)}{x - 3}.
$$

Step 4: the answer is $\frac{3(x - 2)}{x - 3}$ for $x \ne 3$ and $x \ne -2$. At $x = -2$ the simplified expression gives $\frac{3(-4)}{-5} = \frac{12}{5}$, but the original is $\frac{0}{0}$ there, so the equal sign does not hold at $-2$.

Step 5: check at $x = 5$. The original is $\frac{3 \cdot 25 - 12}{25 - 5 - 6} = \frac{63}{14} = \frac{9}{2}$, and the simplified form is $\frac{3 \cdot 3}{2} = \frac{9}{2}$. At $x = -4$ both give $\frac{18}{7}$.

<div class="warning" markdown>

Watch out at Step 3: you cannot cancel the 3 against the $-3$ inside $x - 3$, and you cannot cancel the $x$ in $3x - 6$ with the $x$ in $x - 3$. Each of those is a term inside a sum. Only whole factors cancel.

</div>

</div>

<div class="example" markdown>

### Example 2: multiplying and dividing in one problem

Simplify $\dfrac{x^2 - x - 6}{x^2 - 1} \cdot \dfrac{x^2 + 2x + 1}{x^2 - 9}$.

Factor everything (Step 1 of the multiplying steps): $x^2 - x - 6 = (x - 3)(x + 2)$, $x^2 - 1 = (x - 1)(x + 1)$, $x^2 + 2x + 1 = (x + 1)^2$ and $x^2 - 9 = (x - 3)(x + 3)$. So the product is

$$
\frac{(x - 3)(x + 2)}{(x - 1)(x + 1)} \cdot \frac{(x + 1)^2}{(x - 3)(x + 3)}.
$$

The excluded values come from the original denominators: $x \ne 1$, $x \ne -1$, $x \ne 3$ and $x \ne -3$. Cancel $x - 3$ from top and bottom, and cancel one $x + 1$ from the $(x + 1)^2$ against the $x + 1$ in the first denominator:

$$
\frac{(x + 2)(x + 1)}{(x - 1)(x + 3)}.
$$

Check at $x = 2$: the original is $\frac{4 - 2 - 6}{4 - 1} \cdot \frac{4 + 4 + 1}{4 - 9} = \frac{-4}{3} \cdot \frac{9}{-5} = \frac{12}{5}$, and the result is $\frac{4 \cdot 3}{1 \cdot 5} = \frac{12}{5}$.

Now a division: if the second fraction were the divisor, you would flip it and the excluded values would also include the zeros of its numerator, $x^2 + 2x + 1 = 0$, which is $x = -1$ (already on the list).

</div>

<div class="example" markdown>

### Example 3: adding with denominators that share a factor

Write $\dfrac{x}{x^2 - x - 6} + \dfrac{1}{x^2 - 9}$ as one fraction.

Step 1: factor the denominators: $x^2 - x - 6 = (x - 3)(x + 2)$ and $x^2 - 9 = (x - 3)(x + 3)$. The factor $x - 3$ is shared, so it appears once in the LCD, which is $(x - 3)(x + 2)(x + 3)$.

Step 2: the first denominator is missing $x + 3$ and the second is missing $x + 2$:

$$
\frac{x(x + 3)}{(x - 3)(x + 2)(x + 3)} + \frac{x + 2}{(x - 3)(x + 3)(x + 2)}.
$$

Step 3: add the numerators, $x(x + 3) + (x + 2) = x^2 + 3x + x + 2 = x^2 + 4x + 2$.

Step 4: the numerator does not factor over the integers (the pairs with product 2 have sums $\pm 3$, not 4), so nothing cancels. An answer that doesn't simplify is a fine answer:

$$
\frac{x^2 + 4x + 2}{(x - 3)(x + 2)(x + 3)}, \qquad x \ne 3,\ -2,\ -3.
$$

Check at $x = 1$: the original is $\frac{1}{-6} + \frac{1}{-8} = -\frac{4}{24} - \frac{3}{24} = -\frac{7}{24}$, and the result is $\frac{7}{(-2)(3)(4)} = -\frac{7}{24}$.

<div class="warning" markdown>

Watch out: adding the denominators is the classic slip. $\frac{1}{x - 1} + \frac{1}{x + 1}$ is not $\frac{2}{2x}$. As with $\frac{1}{2} + \frac{1}{3} \ne \frac{2}{5}$, fractions need a common denominator first, and only the numerators are added.

</div>

</div>

<div class="example" markdown>

### Example 4: a complex fraction (finish it yourself)

Simplify $\dfrac{1 + \frac{1}{x}}{1 - \frac{1}{x^2}}$ using Method B.

The inner denominators are $x$ and $x^2$, so the LCD is $x^2$. Multiply the whole top and the whole bottom by $x^2$:

$$
\frac{x^2\left(1 + \frac{1}{x}\right)}{x^2\left(1 - \frac{1}{x^2}\right)} = \frac{x^2 + x}{x^2 - 1}.
$$

Now factor, cancel, and state the excluded values. They come from the inner denominators ($x \ne 0$) and from the main denominator being 0.

<details class="solution" markdown>
<summary>Finish</summary>

Factor: $\frac{x(x + 1)}{(x - 1)(x + 1)} = \frac{x}{x - 1}$.

The main denominator $1 - \frac{1}{x^2}$ is 0 when $x^2 = 1$, so $x = \pm 1$. Together with $x \ne 0$ the excluded values are $x \ne 0, 1, -1$. Notice that 0 is excluded even though the final answer $\frac{x}{x - 1}$ allows it, because the original expression contains $\frac{1}{x}$.

Check at $x = 2$: the original is $\frac{1 + \frac{1}{2}}{1 - \frac{1}{4}} = \frac{3/2}{3/4} = 2$, and $\frac{x}{x - 1} = \frac{2}{1} = 2$. At $x = 3$: $\frac{4/3}{8/9} = \frac{3}{2}$ and $\frac{3}{2}$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for cancelling terms. $\frac{x^2 + 4}{x^2 + 2}$ does not simplify to $\frac{4}{2}$, and $\frac{x + 5}{x}$ does not become 5. Substitute $x = 1$ to see it: $\frac{5}{3}$ is not 2, and $\frac{6}{1}$ is not 5. Cancel only when the top and the whole bottom are both products, so that the common piece is a factor of each.

</div>

<div class="warning" markdown>

Watch out for losing an excluded value. After cancelling $x + 2$ in Example 1, the answer $\frac{3(x - 2)}{x - 3}$ seems to say only $x \ne 3$. But the original expression is not defined at $x = -2$, and a rewritten expression should be equal to it only where it was defined. Write the exclusions from the original denominators, before cancelling, next to the answer. This matters most when you solve equations in the [next lessons](03-rational-and-radical-equations.md).

</div>

<div class="warning" markdown>

Watch out for the sign trap with $a - b$ and $b - a$. They are opposites, so $\frac{x - 5}{5 - x} = -1$ for $x \ne 5$, not $1$. Check with $x = 7$: $\frac{2}{-2} = -1$. Likewise, $\frac{5}{x - 2} + \frac{3}{2 - x}$ can be written with the denominator $x - 2$ by turning the second fraction into $\frac{-3}{x - 2}$, giving $\frac{2}{x - 2}$. Doing this avoids a bigger LCD.

</div>

<div class="warning" markdown>

Watch out when subtracting. In $\frac{x}{x + 1} - \frac{x - 3}{x + 1}$ the numerator is $x - (x - 3) = 3$. Without the brackets you would write $x - x - 3 = -3$, which has the wrong sign. Put the second numerator in brackets, as in Step 3 of the adding steps, so that the minus sign reaches both terms. The answer is $\frac{3}{x + 1}$, and at $x = 1$ it checks: $\frac{1}{2} - \frac{-2}{2} = \frac{3}{2}$, and $\frac{3}{1 + 1} = \frac{3}{2}$.

</div>

A rational expression can have no excluded values (the denominator $x^2 + 1$ is never 0), one excluded value, or many. It can also be simplified all the way to a polynomial, as with $\frac{x^2 - 4}{x - 2} = x + 2$ for $x \ne 2$. When the degree of the top is the same as or bigger than the degree of the bottom, the expression is called improper, and polynomial division rewrites it as a polynomial plus a proper fraction: $\frac{x^2 + 1}{x - 1} = x + 1 + \frac{2}{x - 1}$. The next lesson uses this form.

The value 0 in the numerator is not an excluded value. The expression $\frac{x - 3}{x + 1}$ is 0 at $x = 3$ and that is a perfectly good output. Only a zero of the denominator is a problem.

## Tricks and shortcuts

Test with a number. After any simplification, substitute a number that is not excluded into the original and into the answer. Two different values mean there is an error. One matching value does not prove the answer is right, but a second test number makes a wrong answer very unlikely.

To find the LCD fast, write each denominator as a product of its prime factors with exponents and take the biggest exponent of each. For $x^2 - 4x + 4 = (x - 2)^2$ and $x^2 - 4 = (x - 2)(x + 2)$, the LCD is $(x - 2)^2(x + 2)$. It is not $(x - 2)^3(x + 2)$: the shared factor $x - 2$ is counted at the larger of its powers, once.

When the denominators have no common factor, the LCD is their product, and the sum has a pattern you can use directly:

$$
\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}.
$$

The pattern is true for polynomials just as for integers.

## In code

SymPy simplifies rational expressions and shows how an excluded value behaves: the original expression is undefined at $x = -2$, but the simplified one has a value. The last two lines combine fractions and rewrite an improper fraction with polynomial division.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction
from sympy import symbols, factor, together, apart

x = symbols("x")
expr = (3*x**2 - 12) / (x**2 - x - 6)
simple = factor(expr)
print(simple)                           # 3*(x - 2)/(x - 3)
print(expr.subs(x, -2), simple.subs(x, -2))   # nan 12/5
print(expr.subs(x, 3), simple.subs(x, 3))     # zoo zoo

def original(t):
    return Fraction(3*t**2 - 12, t**2 - t - 6)

def reduced(t):
    return Fraction(3*(t - 2), t - 3)

print([original(t) == reduced(t) for t in (-4, 0, 1, 5, 10)])   # all True

print(factor(together(x/(x**2 - x - 6) + 1/(x**2 - 9))))
# (x**2 + 4*x + 2)/((x - 3)*(x + 2)*(x + 3))
print(apart((x**3 - 2*x**2 + x + 5)/(x - 2)))   # x**2 + 1 + 7/(x - 2)
```

SymPy's `nan` is "not a number", the result of $\frac{0}{0}$, and `zoo` is its name for a division by zero (complex infinity). The Python `Fraction` type keeps the arithmetic exact, so `==` compares real values and not rounded ones. The function `original` would raise an error at $t = 3$ or $t = -2$, which is the same warning that the excluded values give on paper.

</details>

## FAQ

### Why do we keep the excluded values after cancelling?

Because the original expression is a different function from the cancelled one. The function $\frac{x^2 - 1}{x - 1}$ has no value at $x = 1$, while $x + 1$ has the value 2 there. Their graphs are the same line except for one missing point. The next lesson draws that missing point as a hole, and it matters again in [rational and radical equations](03-rational-and-radical-equations.md), where a solution at an excluded value must be thrown out.

### Is $\frac{x}{x}$ equal to 1?

For every $x \ne 0$, yes. At $x = 0$ the expression is undefined, so it isn't equal to 1 there. This is why the theorem above is stated for $x$ with $b(x)c(x) \ne 0$ and not for every $x$.

### Why can't I cancel the $x$ in $\frac{x + 2}{x}$?

Cancelling means dividing the top and the bottom by the same nonzero thing. Dividing the bottom, $x$, by $x$ gives 1. But dividing the top, $x + 2$, by $x$ divides every term, and gives $1 + \frac{2}{x}$, not 2. That is the rule $\frac{a + b}{c} = \frac{a}{c} + \frac{b}{c}$. So $\frac{x + 2}{x} = 1 + \frac{2}{x}$ is true, but it is a different form of the same expression and not a simpler one.

### Do I always have to find the least common denominator?

Any common denominator works, since the answer can be simplified at the end, but a bigger one means bigger numbers and more cancelling. The LCD keeps the algebra short. With denominators $x^2 - 9$ and $x - 3$, using the product $(x^2 - 9)(x - 3)$ gives a common factor to cancel at the end, while the LCD $x^2 - 9$ gives it right away.

## Practice

### Warm-up

1\. Find the excluded values of (a) $\dfrac{5}{x - 4}$, (b) $\dfrac{x + 1}{x^2 - 25}$ and (c) $\dfrac{x}{x^2 + 4}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The denominator is 0 at $x = 4$, so $x \ne 4$.
- (b) $x^2 - 25 = (x - 5)(x + 5)$ is 0 at $x = 5$ and $x = -5$, so $x \ne \pm 5$. The numerator being 0 at $x = -1$ is not a problem.
- (c) $x^2 + 4 \ge 4$ for every real $x$, so the denominator is never 0 and nothing is excluded.

Check: substitute each excluded value into its denominator: $4 - 4 = 0$, $25 - 25 = 0$ and $(-5)^2 - 25 = 0$.

</details>

2\. Simplify and state the excluded values: (a) $\dfrac{4x^2 - 12x}{8x}$, (b) $\dfrac{x^2 - 25}{x^2 + 5x}$, (c) $\dfrac{x - 5}{5 - x}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Factor the numerator: $4x(x - 3)$. Then $\frac{4x(x - 3)}{8x} = \frac{x - 3}{2}$, with $x \ne 0$.
- (b) $\frac{(x - 5)(x + 5)}{x(x + 5)} = \frac{x - 5}{x}$, with $x \ne 0$ and $x \ne -5$.
- (c) Since $5 - x = -(x - 5)$, the fraction is $-1$, with $x \ne 5$.

Check at $x = 2$ for (a): $\frac{16 - 24}{16} = -\frac{1}{2}$ and $\frac{2 - 3}{2} = -\frac{1}{2}$. At $x = 3$ for (b): $\frac{-16}{24} = -\frac{2}{3}$ and $\frac{3 - 5}{3} = -\frac{2}{3}$. At $x = 7$ for (c): $\frac{2}{-2} = -1$.

</details>

3\. Write $\dfrac{3}{2x} - \dfrac{5}{3x^2}$ as one fraction.

<details class="solution" markdown>
<summary>Solution</summary>

The denominators are $2x$ and $3x^2$. The LCD takes the biggest power of each factor: $6x^2$. Then

$$
\frac{3}{2x} = \frac{3 \cdot 3x}{6x^2} = \frac{9x}{6x^2}, \qquad \frac{5}{3x^2} = \frac{5 \cdot 2}{6x^2} = \frac{10}{6x^2},
$$

so the difference is $\frac{9x - 10}{6x^2}$, with $x \ne 0$. The numerator does not factor with the denominator, so this is in lowest terms.

Check at $x = 2$: $\frac{3}{4} - \frac{5}{12} = \frac{9}{12} - \frac{5}{12} = \frac{1}{3}$, and $\frac{18 - 10}{24} = \frac{8}{24} = \frac{1}{3}$.

</details>

### Standard

4\. Simplify $\dfrac{x^2 - 2x - 8}{x^2 - 9} \div \dfrac{x^2 + 2x}{x^2 + 3x}$ and state every excluded value.

<details class="solution" markdown>
<summary>Solution</summary>

Factor everything: $\frac{(x - 4)(x + 2)}{(x - 3)(x + 3)} \div \frac{x(x + 2)}{x(x + 3)}$. Flip the divisor and multiply:

$$
\frac{(x - 4)(x + 2)}{(x - 3)(x + 3)} \cdot \frac{x(x + 3)}{x(x + 2)} = \frac{x - 4}{x - 3}.
$$

The excluded values: the first denominator is 0 at $x = \pm 3$, the second denominator is 0 at $x = 0$ and $x = -3$, and the divisor is 0 where its numerator is, at $x = 0$ and $x = -2$. So $x \ne -3, -2, 0, 3$.

Check at $x = 1$: $\frac{1 - 2 - 8}{1 - 9} = \frac{9}{8}$ and $\frac{1 + 2}{1 + 3} = \frac{3}{4}$, so the quotient is $\frac{9}{8} \cdot \frac{4}{3} = \frac{3}{2}$. The answer gives $\frac{1 - 4}{1 - 3} = \frac{3}{2}$.

</details>

5\. Simplify $\dfrac{2x}{x^2 - 4} - \dfrac{1}{x + 2}$.

<details class="solution" markdown>
<summary>Solution</summary>

The denominators are $(x - 2)(x + 2)$ and $x + 2$, so the LCD is $(x - 2)(x + 2)$. Rewrite the second fraction as $\frac{x - 2}{(x - 2)(x + 2)}$ and subtract, with brackets:

$$
\frac{2x - (x - 2)}{(x - 2)(x + 2)} = \frac{x + 2}{(x - 2)(x + 2)} = \frac{1}{x - 2}.
$$

The excluded values are $x \ne 2$ and $x \ne -2$. Even though the answer allows $-2$, the original does not.

Check at $x = 1$: $\frac{2}{-3} - \frac{1}{3} = -1$, and $\frac{1}{1 - 2} = -1$.

</details>

6\. Simplify the complex fraction $\dfrac{x - \frac{4}{x}}{1 - \frac{2}{x}}$ and state the excluded values.

<details class="solution" markdown>
<summary>Solution</summary>

The only inner denominator is $x$, so multiply the top and the bottom by $x$:

$$
\frac{x^2 - 4}{x - 2} = \frac{(x - 2)(x + 2)}{x - 2} = x + 2.
$$

The excluded values are $x \ne 0$ (inner denominator) and $x \ne 2$ (the main denominator $1 - \frac{2}{x}$ is 0 when $x = 2$).

Check at $x = 4$: $\frac{4 - 1}{1 - \frac{1}{2}} = \frac{3}{1/2} = 6$, and $4 + 2 = 6$.

</details>

### Challenge

7\. Find numbers $A$ and $B$ so that $\dfrac{5x + 1}{(x - 1)(x + 2)} = \dfrac{A}{x - 1} + \dfrac{B}{x + 2}$ for every allowed $x$.

<details class="solution" markdown>
<summary>Solution</summary>

Add the right side over the LCD: $\frac{A(x + 2) + B(x - 1)}{(x - 1)(x + 2)}$. The denominators are the same, so the numerators must be equal for every $x$:

$$
5x + 1 = A(x + 2) + B(x - 1).
$$

Substitute $x = 1$, which kills the $B$ term: $6 = 3A$, so $A = 2$. Substitute $x = -2$, which kills the $A$ term: $-9 = -3B$, so $B = 3$.

Check: $\frac{2}{x - 1} + \frac{3}{x + 2} = \frac{2(x + 2) + 3(x - 1)}{(x - 1)(x + 2)} = \frac{5x + 1}{(x - 1)(x + 2)}$. At $x = 2$: the left side is $\frac{11}{4}$, and $2 + \frac{3}{4} = \frac{11}{4}$.

</details>

8\. (Reviews [polynomial division](../04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md).) Divide to write $\dfrac{x^3 - 2x^2 + x + 5}{x - 2}$ as a polynomial plus a fraction whose numerator is a constant.

<details class="solution" markdown>
<summary>Solution</summary>

Use synthetic division with $c = 2$ and the coefficients $1, -2, 1, 5$. Bring down 1. Then $1 \cdot 2 = 2$ and $-2 + 2 = 0$. Then $0 \cdot 2 = 0$ and $1 + 0 = 1$. Then $1 \cdot 2 = 2$ and $5 + 2 = 7$. The quotient is $x^2 + 0x + 1$ and the remainder is 7, so

$$
\frac{x^3 - 2x^2 + x + 5}{x - 2} = x^2 + 1 + \frac{7}{x - 2}, \qquad x \ne 2.
$$

Check at $x = 12$: the left side is $\frac{1728 - 288 + 12 + 5}{10} = \frac{1457}{10} = 145.7$, and the right side is $144 + 1 + 0.7 = 145.7$. The remainder 7 also equals $p(2) = 8 - 8 + 2 + 5 = 7$, as the remainder theorem says.

</details>

## Where this shows up

- The next lesson, [rational functions and asymptotes](02-rational-functions-and-asymptotes.md), graphs $\frac{p(x)}{q(x)}$: an excluded value that cancels becomes a hole, and one that does not becomes a vertical asymptote. After that, [rational and radical equations](03-rational-and-radical-equations.md) clears fractions with the LCD, and [polynomial and rational inequalities](04-polynomial-and-rational-inequalities.md) uses the factored form to find where an expression is positive.
- In calculus, the same factor-and-cancel step resolves limits that look like $\frac{0}{0}$ ([limits, intuition and limit laws](../../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md)), and the identity in Practice problem 7, called partial fractions, is used to integrate rational functions ([partial fractions and improper integrals](../../05-university-core/04-integrals/05-partial-fractions-and-improper-integrals.md)).
- In computer science, comparing the running times of two algorithms is often a question about a ratio of polynomials in the input size $n$, and which one wins for large $n$ depends on the leading terms (asymptotic notation<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md -->). In economics, average cost, $\frac{C(q)}{q}$, is a rational expression in the quantity $q$ (production and cost functions<!-- link: ../../07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md -->).
