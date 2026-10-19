# Equivalent expressions

After this lesson you can expand brackets and factor out a greatest common factor with the distributive property, combine like terms, name the property behind each step, and decide whether two expressions are equivalent.

Before this: [variables and expressions](01-variables-and-expressions.md), [properties of operations](../../01-elementary/04-properties-of-operations.md), and [integer arithmetic and sign rules](../01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Simplify $3(2x - 5) - 4x + 7$.
2. Factor the greatest common factor out of $12x - 18$.
3. Is $-(x - 4)$ equivalent to $-x - 4$? Give a reason.

<details class="solution" markdown>
<summary>Answers</summary>

1. $2x - 8$. Expand to $6x - 15 - 4x + 7$, then combine: $6x - 4x = 2x$ and $-15 + 7 = -8$.
2. $6(2x - 3)$. The GCF of 12 and 18 is 6, and expanding gives back $12x - 18$.
3. No. At $x = 0$ the first is $-(0 - 4) = 4$ and the second is $-4$. The minus sign multiplies both terms, so $-(x - 4) = -x + 4$.

</details>

## The idea

Two classmates write the cost of $n$ concert tickets at \$45 each plus a \$5 fee per ticket. One writes $45n + 5n$ and the other writes $50n$. The expressions look different, but they give the same cost for every number of tickets: 1 ticket costs \$50 either way, 4 tickets cost \$200, and 37 tickets cost \$1,850. They are two names for the same rule.

Rewriting an expression into a more useful form, without changing its value for any number, is most of what algebra does. The rewriting uses the properties from [properties of operations](../../01-elementary/04-properties-of-operations.md), and each step can be justified by naming the property it uses.

The hard part is the phrase "for every number". Trying a few values is a good way to catch mistakes, but it can't prove that two expressions always agree. Compare $x^2 + 2$ and $3x$:

| $x$ | $x^2 + 2$ | $3x$ |
|---|---|---|
| $1$ | $3$ | $3$ |
| $2$ | $6$ | $6$ |
| $3$ | $11$ | $9$ |

They agree at 1 and at 2, but they differ at 3, so they are not equivalent. A single value where two expressions differ settles the question, but agreeing at a handful of values settles nothing.

## Definitions

Two expressions are **equivalent** if they have the same value for every value of their variables. When an expression has no value for some numbers, as $\frac{1}{x}$ has none at $x = 0$, the comparison is made only where both expressions are defined.

In plain words, equivalent expressions give the same output for every input. The expressions $45n + 5n$ and $50n$ are equivalent; $x^2 + 2$ and $3x$ are not, since they differ at $x = 3$.

An **identity** is an equation that is true for every value of its variables. Saying that two expressions are equivalent is the same as saying that the equation between them is an identity. So $45n + 5n = 50n$ is an identity, while $x^2 + 2 = 3x$ is not, because it is false at $x = 3$. An identity is an equation you never need to solve, since every number already works.

To **expand** a product is to multiply it out into a sum of terms with the distributive property, as in $3(x + 4) = 3x + 12$. To **factor** an expression is to go the other way and write it as a product, as in $3x + 12 = 3(x + 4)$. Expanding removes brackets and factoring puts them in.

The greatest common factor (GCF) of the terms of an expression is the GCF of their coefficients ([factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md)) times each variable that appears in every term. Each variable gets the smallest power it has in any of the terms, so the GCF of $12x^2$ and $18x$ is $6x$.

To **simplify** an expression is to rewrite it as an equivalent expression with no brackets left to expand and no like terms left to combine. For example, $3(x + 4) - 2x$ simplifies to $x + 12$. When a question asks for factored form instead, the brackets stay.

### The properties behind each step

Every rewrite in this lesson uses one of these rules. Each holds for all numbers $a$, $b$ and $c$, and the letters may stand for whole expressions, such as $a = 2x$.

| Property | Rule | Example |
|---|---|---|
| distributive property | $a(b + c) = ab + ac$ and $(a + b)c = ac + bc$ | $3(x + 4) = 3x + 12$ |
| commutative property of addition | $a + b = b + a$ | $5 + 2x = 2x + 5$ |
| associative property of addition | $(a + b) + c = a + (b + c)$ | $(x + 3) + 4 = x + 7$ |
| commutative property of multiplication | $ab = ba$ | $x \cdot 4 = 4x$ |
| associative property of multiplication | $(ab)c = a(bc)$ | $3(2x) = (3 \cdot 2)x = 6x$ |
| identity properties | $a + 0 = a$ and $1a = a$ | $1x = x$ |
| inverse property of addition | $a + (-a) = 0$ | $3x + (-3x) = 0$ |
| inverse property of multiplication | $a \cdot \frac{1}{a} = 1$, for $a \ne 0$ | $\frac{1}{2} \cdot 2x = 1x$ |
| definition of subtraction | $a - b = a + (-b)$ | $5x - 3 = 5x + (-3)$ |
| multiplying by $-1$ | $(-1)a = -a$ | $(-1)(x - 3) = -(x - 3)$ |

The second form of the distributive property, with the multiplier on the right, is the theorem proved in [properties of operations](../../01-elementary/04-properties-of-operations.md#naming-the-property-behind-each-step). The inverse properties are new here. They say that each number has an opposite, which adds to it to give 0, and each nonzero number has a reciprocal, which multiplies it to give 1.

Two rules you will use on almost every line follow from the table. Combining like terms is the distributive property read from right to left:

$$
ax + bx = (a + b)x, \quad \text{so} \quad 3x + 5x = 8x.
$$

A minus sign in front of brackets is a factor of $-1$, and the distributive property sends it to every term inside:

$$
-(a - b) = (-1)(a - b) = (-1)a + (-1)(-b) = -a + b.
$$

So a minus sign in front of brackets changes the sign of every term inside, however many there are: $-(2x - 5 + y) = -2x + 5 - y$.

## How to do it

### Simplifying an expression

1. Expand every bracket. Multiply the number in front, with its sign, by every term inside. A minus sign in front of brackets is a factor of $-1$.
2. Find the like terms: the $x^2$ terms, the $x$ terms, the constant terms, and so on.
3. Group the like terms together (commutative and associative properties of addition).
4. Combine each group by adding the coefficients (distributive property, read from right to left).
5. Write the result with the highest power first and the constant term last.
6. Check by evaluating the original and the result at one or two values other than 0 and 1.

### Factoring out the GCF

1. Find the GCF of the coefficients, and each variable that appears in every term, to its smallest power.
2. Divide each term by the GCF. The quotients go inside the brackets, one for each term.
3. Write the GCF in front of the brackets.
4. Check by expanding: you must get the original expression back, and the terms inside the brackets must have no common factor left.

When the first term is negative, it is usual to factor out the negative of the GCF, so that the bracket starts with a positive term: $-6x - 9 = -3(2x + 3)$.

### Naming the reason for each step

In a proof, each step must follow from the one before by a rule you can name. A two-column table puts each step on the left and its reason on the right, so a gap in the reasoning is easy to spot.

We know the properties in the table above. We want to show that $3(x + 4) - 2x$ is equivalent to $x + 12$, that is, that $3(x + 4) - 2x = x + 12$ for every number $x$. The plan is to expand, bring the two $x$ terms together and combine them.

| Step | Reason |
|---|---|
| $3(x + 4) - 2x = (3x + 12) - 2x$ | distributive property, and $3 \cdot 4 = 12$ |
| $\qquad = (3x + 12) + (-2x)$ | definition of subtraction |
| $\qquad = 3x + (-2x) + 12$ | commutative and associative properties of addition |
| $\qquad = (3 + (-2))x + 12$ | distributive property, read from right to left |
| $\qquad = 1x + 12$ | arithmetic: $3 + (-2) = 1$ |
| $\qquad = x + 12$ | identity property of multiplication |

Look back: no step used a particular value of $x$, so the equation holds for every $x$, and it is an identity. With practice you will merge several rows into one line, as the worked examples below do, but each merged line still rests on rules like these. University proofs are written in sentences rather than tables; direct proof<!-- link: ../../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md --> shows how.

### Testing whether two expressions are equivalent

1. Evaluate both expressions at a value or two other than 0 and 1. If they differ at some value, they are not equivalent, and that value is a counterexample, the one case that sinks a claim about every number ([properties of operations](../../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division)). You are done.
2. If they agree, simplify both, giving the property for each step. If you reach the same expression from both, they are equivalent, and the steps are the proof.
3. If the two simplified forms are different, keep testing values until you find one where they differ. That value proves they are not equivalent.

## Worked examples

<div class="example" markdown>

### Example 1: simplifying with a subtracted bracket

Simplify $5(2x - 3) - 3(x - 4)$.

Step 1: expand each bracket. In the first, $5 \cdot 2x = 10x$ and $5 \cdot (-3) = -15$. In the second, the multiplier is $-3$, with its sign, so $(-3) \cdot x = -3x$ and $(-3) \cdot (-4) = 12$:

$$
5(2x - 3) - 3(x - 4) = 10x - 15 - 3x + 12.
$$

<div class="warning" markdown>

Watch out: this is where the classic slip happens. Writing $-3(x - 4) = -3x - 12$ multiplies the $-4$ by $3$ instead of by $-3$. A negative times a negative is positive, so the last term is $+12$.

</div>

Step 2: the like terms are $10x$ and $-3x$, and the constants $-15$ and $12$.

Steps 3 and 4: group and combine, with the reason beside each line:

$$
\begin{aligned}
10x - 15 - 3x + 12 &= (10x - 3x) + (-15 + 12) && \text{commutative and associative properties} \\
&= (10 - 3)x + (-3) && \text{distributive property, right to left} \\
&= 7x - 3.
\end{aligned}
$$

Step 5: the answer $7x - 3$ already has the $x$ term first.

Step 6: check at $x = 2$. The original is $5(4 - 3) - 3(2 - 4) = 5 + 6 = 11$, and the answer is $7 \cdot 2 - 3 = 11$. The slip from the warning would give $7x - 27$, which is $-13$ at $x = 2$, so the check would catch it.

</div>

<div class="example" markdown>

### Example 2: factoring out the GCF

Factor (a) $18x^2 - 12x + 6$, (b) $15xy - 10x$ and (c) $-4x - 10$.

(a) The GCF of 18, 12 and 6 is 6. The last term has no $x$, so no variable goes in the GCF (Step 1). Dividing each term by 6 gives $3x^2$, $-2x$ and $1$ (Step 2), so

$$
18x^2 - 12x + 6 = 6(3x^2 - 2x + 1).
$$

The 1 must stay. The last term, 6, is $6 \cdot 1$, and without the 1 the brackets would hold only two terms where there were three.

(b) The GCF of 15 and 10 is 5. Both terms contain $x$, but only one contains $y$, so the GCF is $5x$. Dividing gives $15xy \div 5x = 3y$ and $-10x \div 5x = -2$, so $15xy - 10x = 5x(3y - 2)$.

(c) The first term is negative, so factor out $-2$. Dividing gives $-4x \div (-2) = 2x$ and $-10 \div (-2) = 5$, so $-4x - 10 = -2(2x + 5)$.

Check each by expanding (Step 4). For instance, $5x \cdot 3y - 5x \cdot 2 = 15xy - 10x$, and $(-2)(2x) + (-2)(5) = -4x - 10$. None of the three brackets has a common factor left.

</div>

<div class="example" markdown>

### Example 3: three pairs, three verdicts

Decide whether each pair is equivalent: (a) $2(x - 1) + 4$ and $2x + 2$, (b) $\frac{x}{2} + \frac{x}{3}$ and $\frac{2x}{5}$, (c) $(x + 3)^2$ and $x^2 + 9$.

(a) Test $x = 3$: both give 8. They agree, so try to prove it. Expanding the first gives $2x - 2 + 4$ (distributive property), which is $2x + 2$. The two are equivalent.

(b) Test $x = 6$: the first gives $3 + 2 = 5$, while the second gives $\frac{12}{5} = 2.4$. They differ, so they are not equivalent, and $x = 6$ is a counterexample. The second expression adds the numerators and the denominators, the mistake from [adding and subtracting fractions](../../01-elementary/10-adding-and-subtracting-fractions.md#edge-cases-and-common-mistakes). Combining like terms gives the right sum, $\frac{1}{2}x + \frac{1}{3}x = \frac{5}{6}x$, which is 5 at $x = 6$.

(c) Test $x = 1$: the first gives $4^2 = 16$ and the second gives $1 + 9 = 10$, so they are not equivalent. A counterexample settles this before you know how to expand a square (the expansion, $x^2 + 6x + 9$, is in polynomial arithmetic<!-- link: ../../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md -->). At $x = 0$ both expressions are 9, which is why Step 1 avoids 0.

</div>

<div class="example" markdown>

### Example 4: an answer with no variable (finish it yourself)

Simplify $\frac{1}{2}(4x - 6) - \frac{2}{3}(3x + 9)$.

Step 1: expand. The first bracket gives $\frac{1}{2} \cdot 4x = 2x$ and $\frac{1}{2} \cdot (-6) = -3$. The multiplier of the second is $-\frac{2}{3}$, sign included, so it gives $-\frac{2}{3} \cdot 3x = -2x$ and $-\frac{2}{3} \cdot 9 = -6$:

$$
\frac{1}{2}(4x - 6) - \frac{2}{3}(3x + 9) = 2x - 3 - 2x - 6.
$$

Now find and combine the like terms (Steps 2 to 5), and check the result at two values (Step 6).

<details class="solution" markdown>
<summary>Finish</summary>

The like terms are $2x$ and $-2x$, and $-3$ and $-6$. Combining gives $(2 - 2)x + (-3 - 6) = 0x - 9$, and $0x = 0$, so the expression simplifies to $-9$.

The answer has no $x$ in it, and that is fine: the expression has the value $-9$ whatever $x$ is. Check at $x = 3$: $\frac{1}{2}(6) - \frac{2}{3}(18) = 3 - 12 = -9$. At $x = -3$: $\frac{1}{2}(-18) - \frac{2}{3}(0) = -9 - 0 = -9$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the minus sign in front of brackets. Writing $-(x - 3) = -x - 3$ changes the sign of the first term only. The minus sign is a factor of $-1$ that multiplies both terms, so $-(x - 3) = -x + 3$. Test at $x = 0$: the original is $-(-3) = 3$, the right version gives 3, and the wrong one gives $-3$. This is also on the [common mistakes](../../reference/common-mistakes.md#subtracting-only-the-first-term-in-brackets) page.

</div>

<div class="warning" markdown>

Watch out: the multiplier reaches every term inside the brackets. Writing $2(x + 3) = 2x + 3$ multiplies only the $x$. The right expansion is $2x + 6$; at $x = 4$ the original is $2 \cdot 7 = 14$, and $2x + 3$ gives only 11.

</div>

<div class="warning" markdown>

Watch out: only like terms combine. The expression $3x + 2$ is already simplified, and writing it as $5x$ is wrong: at $x = 2$ the first is 8 and the second is 10. In the same way, $x^2 + x$ is neither $x^3$ nor $2x^2$; at $x = 2$ it is 6, while both of those are 8. (At $x = 1$, $x^2 + x$ and $2x^2$ are both 2, so 1 would hide the slip.)

</div>

<div class="warning" markdown>

Watch out: the distributive property spreads a multiplication over a sum, never over a product. Writing $2(xy) = (2x)(2y)$ doubles twice. The right value is $2xy$, by the associative property; at $x = 3$ and $y = 5$ it is 30, while $(2x)(2y)$ is 60.

</div>

A partial GCF gives an equivalent expression but not the fully factored one: $12x - 18 = 2(6x - 9)$ is true, but $6x - 9$ still has the common factor 3, and the full answer is $6(2x - 3)$.

Dividing a sum by a number divides every term, because dividing by 2 is multiplying by $\frac{1}{2}$ and the distributive property applies. So $\frac{6x + 4}{2} = 3x + 2$. The slip $\frac{6x + 4}{2} = 3x + 4$ divides only the first term.

When a variable sits in a denominator, equivalence holds only where both expressions are defined. The expressions $\frac{2x}{x}$ and $2$ agree at every $x \ne 0$, but at $x = 0$ the first has no value, so the true statement is "$\frac{2x}{x} = 2$ for $x \ne 0$". That condition matters when dividing by a variable can lose a solution ([multi-step equations](04-multi-step-equations.md#dividing-by-an-expression-that-might-be-zero)).

## Tricks and shortcuts

Draw a rectangle. The product $3(x + 4)$ is the area of a rectangle 3 wide and $x + 4$ long, and cutting it at the $x$ mark gives two pieces with areas $3x$ and 12:

```text
         x          4
    +----------+--------+
  3 |    3x    |   12   |
    +----------+--------+
```

Expanding reads the areas off the side lengths, and factoring finds the side lengths from the areas: the common side is the GCF.

Carry the sign with the number when you distribute. Read $5 - 3(x - 4)$ as $5 + (-3)(x - 4)$, then multiply $-3$ by each term. Most sign errors come from distributing a 3 and attaching the minus sign afterwards.

Factored form shows things that expanded form hides. The expression $6(2x - 3)$ is a multiple of 6 for every integer $x$, which $12x - 18$ doesn't show at a glance, and in high school the factored form of a polynomial shows where it equals 0 (factoring polynomials<!-- link: ../../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md -->).

## In code

Sympy expands and factors exactly, and it can test equivalence: two polynomials are equivalent exactly when their difference expands to 0.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import symbols, expand, factor

x = symbols("x")
print(expand(5*(2*x - 3) - 3*(x - 4)))    # 7*x - 3
print(factor(18*x**2 - 12*x + 6))         # 6*(3*x**2 - 2*x + 1)
print(expand(-(x - 3)))                   # 3 - x

print(expand((2*(x - 1) + 4) - (2*x + 2)))                # 0: equivalent
print(expand((x**2 + 2) - 3*x))                           # x**2 - 3*x + 2: not 0
print([(x**2 + 2 - 3*x).subs(x, v) for v in [1, 2, 3]])   # [0, 0, 2]
```

The last line finds the counterexample $x = 3$ from [The idea](#the-idea). For polynomials, `expand` puts every expression into one standard form, so comparing standard forms settles equivalence. Once functions such as sine and exponentials are allowed, no algorithm can decide equivalence in every case; that is Richardson's theorem (1968), and it is why sympy's `simplify` can fail to reduce an expression that equals 0 (decidability and the halting problem<!-- link: ../../06-cs-math/06-theory-of-computation/05-decidability-and-the-halting-problem.md -->).

</details>

## FAQ

### Why isn't checking a few values enough?

An equivalence is a claim about infinitely many values, and checking some of them leaves the rest unchecked: $x^2 + 2$ and $3x$ agree twice and still differ. There is one special case worth knowing. Expressions of the form $ax + b$ graph as straight lines (slope and linear equations<!-- link: ../05-linear-relationships-and-functions/02-slope-and-linear-equations.md -->), and two different lines cross at most once, so two such expressions that agree at two different values are equivalent. More generally, two polynomials of degree at most $n$ that agree at $n + 1$ different values are equivalent (polynomial functions and graphs<!-- link: ../../03-high-school/04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md -->). Since $x^2 + 2$ has degree 2, two agreements were not enough.

### Is simplifying the same as solving?

No. Simplifying turns an expression into an equivalent expression, and solving finds the values that make an equation true. "Solve $2x + 3$" has no meaning, since an expression is not a statement that can be true or false. The two meet in the next lessons, where you simplify each side of an equation before you solve it.
## Practice

### Warm-up

1\. Expand: (a) $4(x + 5)$, (b) $-2(3x - 7)$, (c) $-(5 - x)$, (d) $\frac{1}{3}(6x + 9)$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $4 \cdot x + 4 \cdot 5 = 4x + 20$.
- (b) $(-2)(3x) + (-2)(-7) = -6x + 14$.
- (c) $(-1)(5) + (-1)(-x) = -5 + x$, which is $x - 5$ with the $x$ term first.
- (d) $\frac{1}{3} \cdot 6x + \frac{1}{3} \cdot 9 = 2x + 3$.

Check at $x = 2$: (b) gives $-2(-1) = 2$ and $-12 + 14 = 2$, and (c) gives $-(3) = -3$ and $2 - 5 = -3$. Parts (a) and (d) check the same way, with 28 and 7.

</details>

2\. Simplify $7x - 3 + 2x^2 - 5x + 8 - x^2$.

<details class="solution" markdown>
<summary>Solution</summary>

Group the like terms: the $x^2$ terms are $2x^2 - x^2 = x^2$, the $x$ terms are $7x - 5x = 2x$, and the constants are $-3 + 8 = 5$. Highest power first, the answer is $x^2 + 2x + 5$.

Check at $x = 2$: the original is $14 - 3 + 8 - 10 + 8 - 4 = 13$, and the answer is $4 + 4 + 5 = 13$.

</details>

3\. Factor out the GCF: (a) $8x + 12$, (b) $15x^2 - 10x$, (c) $-6x - 9$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The GCF is 4: $8x + 12 = 4(2x + 3)$.
- (b) The GCF of 15 and 10 is 5, and both terms contain $x$ (the smallest power is $x^1$), so the GCF is $5x$: $15x^2 - 10x = 5x(3x - 2)$.
- (c) The first term is negative, so factor out $-3$: $-6x - 9 = -3(2x + 3)$.

Check by expanding: $4 \cdot 2x + 4 \cdot 3 = 8x + 12$; $5x \cdot 3x - 5x \cdot 2 = 15x^2 - 10x$; $(-3)(2x) + (-3)(3) = -6x - 9$.

</details>

### Standard

4\. Simplify $6 - 2(3x - 4) + 5x$.

<details class="solution" markdown>
<summary>Solution</summary>

Expand with the multiplier $-2$: $(-2)(3x) = -6x$ and $(-2)(-4) = 8$. So the expression is $6 - 6x + 8 + 5x$. Combine the $x$ terms, $-6x + 5x = -x$, and the constants, $6 + 8 = 14$. The answer is $-x + 14$, which can also be written $14 - x$.

Check at $x = 3$: the original is $6 - 2(5) + 15 = 11$, and $14 - 3 = 11$.

</details>

5\. Practice problem 7 of [variables and expressions](01-variables-and-expressions.md#practice) turned a number trick into the expression $\frac{2n + 6}{2} - n$, which came out as 3 for three different numbers. Prove that it equals 3 for every number $n$, with a two-column table of steps and reasons.

<details class="solution" markdown>
<summary>Solution</summary>

We know the properties from this lesson. We want $\frac{2n + 6}{2} - n = 3$ for every number $n$. The plan is to divide each term by 2, then let the $n$ and the $-n$ cancel.

| Step | Reason |
|---|---|
| $\frac{2n + 6}{2} - n = \frac{1}{2}(2n + 6) - n$ | dividing by 2 is multiplying by $\frac{1}{2}$ |
| $\qquad = \frac{1}{2} \cdot 2n + \frac{1}{2} \cdot 6 - n$ | distributive property |
| $\qquad = 1n + 3 - n$ | associative property of multiplication, inverse property of multiplication, and $\frac{1}{2} \cdot 6 = 3$ |
| $\qquad = n + 3 + (-n)$ | identity property of multiplication, definition of subtraction |
| $\qquad = n + (-n) + 3$ | commutative and associative properties of addition |
| $\qquad = 0 + 3$ | inverse property of addition |
| $\qquad = 3$ | identity property of addition |

Look back: no step used a particular value of $n$, so the trick gives 3 for every starting number. The three examples suggested it, and the proof shows it.

Check with a new number, $n = 100$: $\frac{206}{2} - 100 = 103 - 100 = 3$.

</details>

6\. For each pair, prove that the expressions are equivalent or give a counterexample: (a) $3(x + 2) - x$ and $2x + 6$, (b) $\frac{x + 6}{2}$ and $x + 3$, (c) $2(xy)$ and $(2x)(2y)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Equivalent. Expanding gives $3x + 6 - x$ (distributive property), and combining like terms gives $(3 - 1)x + 6 = 2x + 6$ (distributive property, right to left).

(b) Not equivalent. At $x = 2$ the first is $\frac{8}{2} = 4$ and the second is 5. The division applies to both terms of the numerator: $\frac{x + 6}{2} = \frac{x}{2} + 3$.

(c) Not equivalent. At $x = 3$ and $y = 5$ the first is $2 \cdot 15 = 30$ and the second is $6 \cdot 10 = 60$. In fact $(2x)(2y) = 4xy$, by the associative and commutative properties.

Check (a) at $x = 5$: $3 \cdot 7 - 5 = 16$ and $10 + 6 = 16$.

</details>

### Challenge

7\. (a) Prove that the sum of three consecutive integers is always a multiple of 3. (b) Is the sum of four consecutive integers always a multiple of 4? Prove it or give a counterexample.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Let $k$ be the smallest of the three integers. Then the other two are $k + 1$ and $k + 2$, and their sum is

$$
k + (k + 1) + (k + 2) = 3k + 3 = 3(k + 1),
$$

by combining like terms and factoring out 3. Since $k + 1$ is an integer, the sum is a multiple of 3, and no particular $k$ was used, so this holds for every three consecutive integers.

(b) No. Take 1, 2, 3 and 4: the sum is 10, which is not a multiple of 4. The algebra shows why: $k + (k + 1) + (k + 2) + (k + 3) = 4k + 6 = 4(k + 1) + 2$, so the sum always leaves a remainder of 2 when divided by 4.

Check: (a) with $k = 7$, the sum $7 + 8 + 9 = 24$ is $3 \cdot 8$, and $k + 1 = 8$. (b) With $k = 1$, $4(2) + 2 = 10$.

</details>

8\. This one reviews [percents](../02-ratios-rates-percents/03-percents.md). (a) A store raises a price $p$ by 25%, then puts the item on sale at 20% off the new price. Write the final price as an expression, simplify it, and decide whether it is equivalent to $p$. (b) Do the same for a 20% increase followed by 20% off.

<details class="solution" markdown>
<summary>Solution</summary>

A 25% increase multiplies the price by 1.25, and 20% off leaves 80% of it, which multiplies by 0.80.

(a) The final price is $0.80(1.25p)$. By the associative property, this is $(0.80 \cdot 1.25)p = 1p = p$. So the final price is equivalent to $p$: the item ends where it started, for every price.

(b) The final price is $0.80(1.20p) = (0.80 \cdot 1.20)p = 0.96p$. This is not equivalent to $p$. At $p = 100$ it gives 96, so the item ends 4% cheaper than it started.

Check (a) at $p = 40$: a 25% increase gives 50, and 20% off 50 gives 40. Check (b) at $p = 100$: a 20% increase gives 120, and 20% off 120 gives 96.

</details>

## Where this shows up

- Every step of solving an equation replaces one side with an equivalent expression or one equation with an equivalent equation, starting in the next lesson, [one- and two-step equations](03-one-and-two-step-equations.md).
- A chain of equalities with a reason for each link is the shape of many university proofs, such as proofs of trigonometric identities and of formulas for sums (direct proof<!-- link: ../../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md -->). Disproving a claim with one value is counterexamples and disproof<!-- link: ../../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md -->.
- Compilers rewrite expressions to make code faster, such as `x*2 + x*3` into `x*5`, and each rewrite must be equivalent for every input. Floating-point numbers break some of the properties, so GCC won't regroup floating-point sums unless a flag such as `-ffast-math` allows it (floating point basics<!-- link: ../../06-cs-math/01-number-representation/04-floating-point-basics.md -->).
