# Exponents and order of operations

After this lesson you can work out powers of negative numbers and fractions, and evaluate an expression with brackets, exponents and the four operations in the standard order, the same way a calculator or Python does.

Before this: [powers of ten](../../01-elementary/14-powers-of-ten.md), [integer arithmetic and sign rules](02-integer-arithmetic-and-sign-rules.md) and [rational number arithmetic](03-rational-number-arithmetic.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $(-2)^4$, $-2^4$ and $(-2)^3$.
2. Work out $20 - 12 \div 4 \times 2$.
3. Work out $\dfrac{6 - 3^2}{-3} + 2 \times (1 - 4)^2$.

<details class="solution" markdown>
<summary>Answers</summary>

1. 16, $-16$ and $-8$. In $-2^4$ the exponent belongs to the 2 alone, so it means $-(2^4)$.
2. 14. Divide and multiply from left to right, $12 \div 4 = 3$ and $3 \times 2 = 6$, and then $20 - 6 = 14$.
3. 19. The numerator is $6 - 9 = -3$, and $-3 \div (-3) = 1$. Then $(1 - 4)^2 = (-3)^2 = 9$, and $2 \times 9 = 18$. Finally $1 + 18 = 19$.

</details>

## The idea

A café sells coffee for \$3 and muffins for \$2 each. You buy a coffee and 4 muffins, and the cashier keys in $3 + 4 \times 2$. Working from left to right gives $7 \times 2 = 14$, but your bill is \$11: the 4 muffins at \$2 are one amount, $4 \times 2 = 8$, which is added to the coffee. The standard reading, multiplication before addition, gives $3 + 8 = 11$, which is what the expression is meant to say.

An expression has a single value only if everyone agrees which operation comes first. The order of operations is that agreement. It is a convention, chosen so that the most common expressions need the fewest brackets. In $3 + 4 \times 2$, and in algebra's $3x^2 + 2x$, the products and powers are the pieces being added, so they are worked out first. When you want something else, brackets override the order: $(3 + 4) \times 2 = 14$.

Exponents rank above multiplication for the same reason that multiplication ranks above addition. A product is a repeated sum, and a power is a repeated product, so $2 \times 3^2$ means 2 times the square of 3, which is $2 \times 9 = 18$.

## Definitions

[Powers of ten](../../01-elementary/14-powers-of-ten.md) defined a power for every base: for a number $b$ and a positive integer $n$, the power $b^n$ is the product of $n$ copies of $b$, where $b$ is the base and $n$ is the exponent. This lesson lets the base be negative or a fraction:

$$
(-3)^2 = (-3) \times (-3) = 9, \qquad \left(\frac{2}{3}\right)^3 = \frac{2}{3} \times \frac{2}{3} \times \frac{2}{3} = \frac{8}{27}.
$$

As before, $b^1 = b$, and $b^0 = 1$ for every number $b \ne 0$.

The **square** of a number $b$ is $b^2$, read "$b$ squared", and its **cube** is $b^3$, read "$b$ cubed". The names come from the area of a square and the volume of a cube ([geometry basics](../../01-elementary/16-geometry-basics-area-perimeter-volume.md)). The perfect squares 0, 1, 4, 9, 16, ... from [multiplication and times tables](../../01-elementary/03-multiplication-and-times-tables.md) are the squares of integers, and they are never negative, since $(-4)^2 = 16$ as well. The **perfect cubes** are the cubes of integers, and they include negative numbers: $\ldots, -27, -8, -1, 0, 1, 8, 27, \ldots$

**Grouping symbols** mark part of an expression to be worked out as a single number. They are round brackets $(\ )$, square brackets $[\ ]$, braces $\{\ \}$, the fraction bar, absolute value bars and the square root sign $\sqrt{\ }$. In Canada round brackets are usually just called brackets; American books call them parentheses.

The **order of operations** is the convention that says which operation to do first:

1. Grouping symbols, starting with the innermost pair.
2. Exponents.
3. Multiplication and division, from left to right.
4. Addition and subtraction, from left to right.

In Canada the memory aid is BEDMAS: brackets, exponents, division and multiplication, addition and subtraction. In the United States it is PEMDAS, with P for parentheses and the M and D swapped, and British books say BODMAS or BIDMAS. All of them describe the same order. In each name the two letters in a pair have equal rank, so neither "DM" nor "MD" means "do this one first".

A minus sign that takes an opposite, as in $-3^2$, ranks with multiplication, because $-a$ means $(-1) \times a$ (Practice problem 7 of [integer arithmetic](02-integer-arithmetic-and-sign-rules.md#practice) proves this). So it comes after exponents: $-3^2 = -(3^2) = -9$. To square $-3$ itself, write $(-3)^2 = 9$.

When exponents are stacked, as in $2^{3^2}$, the raised part is worked out first, from the top down: $2^{3^2} = 2^{(3^2)} = 2^9 = 512$.

## How to do it

1. Work inside grouping symbols first, starting with the innermost pair. A fraction bar groups its whole numerator and its whole denominator, and absolute value bars group what is between them.
2. Work out the powers. The base is only the number or bracket that the exponent is attached to: in $2 \times 5^2$ the base is 5, in $-3^2$ it is 3, and in $(-3)^2$ it is $-3$.
3. Multiply and divide from left to right, in the order the operations appear.
4. Add and subtract from left to right.
5. Check: write the expression again with every bracket the order adds, or type it into Python with the same brackets.

For Step 2, the sign of a power of a negative number depends only on the exponent. The factors pair up as in the counting rule from the last two lessons, so an even power of a negative number is positive and an odd power is negative. In particular, $(-1)^n$ is 1 when $n$ is even and $-1$ when $n$ is odd.

### Why left to right matters

Take $8 \div 4 \div 2$. Left to right, $8 \div 4 = 2$ and $2 \div 2 = 1$. Working from the right instead gives $8 \div (4 \div 2) = 8 \div 2 = 4$, a different answer. In the same way, $10 - 4 + 3$ is $6 + 3 = 9$ from left to right, while doing the addition first gives $10 - 7 = 3$.

The direction matters because division and subtraction are not associative ([properties of operations](../../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division)): moving the brackets changes the answer. Rewriting removes the problem. As $10 + (-4) + 3$, the second expression is all additions, and as $8 \times \frac{1}{4} \times \frac{1}{2}$, the first is all multiplications, so each can be done in whatever order you like. They still come to 9 and 1.

### Nested brackets and the fraction bar

With brackets inside brackets, work from the inside out:

$$
2 \times [3 + (5 - 8)^2] = 2 \times [3 + (-3)^2] = 2 \times [3 + 9] = 2 \times 12 = 24.
$$

Square brackets and braces mean exactly what round brackets mean. They only make the pairs easier to match by eye.

A fraction bar is a grouping symbol that doesn't look like one. In $\dfrac{12 + 6}{3 + 6}$ the bar says to work out the whole numerator and the whole denominator first, which gives $\frac{18}{9} = 2$. Typed on one line into a calculator or a program, the expression needs brackets: `(12 + 6) / (3 + 6)`. Without them, `12 + 6 / 3 + 6` means $12 + 2 + 6 = 20$.

### Calculators, spreadsheets and code

Python follows the order in this lesson. Its `**` operator is done before a minus sign on its left, so `-3**2` is $-9$, as the In code box below shows. Other tools differ in the one place where this order is easy to get wrong, a minus sign in front of a power.

In Excel, negation ranks above exponents, so `=-3^2` gives 9; Microsoft lists the ranks on its [operator precedence page](https://support.microsoft.com/en-us/excel/calculation-operators-and-precedence-in-excel). To get $-9$ in Excel, write `=-(3^2)`. JavaScript refuses to choose: `-3 ** 2` is a syntax error, and you have to write `(-3) ** 2` or `-(3 ** 2)` ([MDN's page on the error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unparenthesized_unary_expr_lhs_exponentiation)).

Calculators differ too. Test one with $3 + 4 \times 2$: a calculator that follows the order of operations shows 11, and one that works each operation as you press it shows 14. Whatever the tool, brackets around a negative base, and around every numerator and denominator, give the answer you meant.

## Worked examples

<div class="example" markdown>

### Example 1: all four steps

Work out $5 - 2 \times (3 - 7)^2 \div 4$.

Step 1: the only grouping symbols are the brackets, and inside them $3 - 7 = -4$. The expression is now $5 - 2 \times (-4)^2 \div 4$.

Step 2: the exponent is attached to the bracket, so the base is $-4$. An even power of a negative number is positive: $(-4)^2 = 16$. The expression is now $5 - 2 \times 16 \div 4$.

<div class="warning" markdown>

Watch out at Step 2: keep the brackets around $-4$ when you copy the line. Writing $-4^2$ instead turns the square into $-16$, and the calculation then gives $5 - 2 \times (-16) \div 4 = 5 + 8 = 13$, which is wrong.

</div>

Step 3: multiply and divide from left to right. First $2 \times 16 = 32$, then $32 \div 4 = 8$. The expression is now $5 - 8$.

Step 4: $5 - 8 = -3$.

Step 5: with every bracket written in, the expression is $5 - \bigl((2 \times (3 - 7)^2) \div 4\bigr)$, which is $5 - ((2 \times 16) \div 4) = 5 - 8$. Python agrees: `5 - 2 * (3 - 7)**2 / 4` gives `-3.0`.

</div>

<div class="example" markdown>

### Example 2: powers and signs

- (a) $-2^4 = -(2 \times 2 \times 2 \times 2) = -16$. The base is 2, and the minus sign comes after the power.
- (b) $(-2)^4 = 16$. Four negative factors, an even number, give a positive product.
- (c) $(-2)^5 = -32$. Five negative factors, an odd number, give a negative product.
- (d) $-(-2)^4 = -16$. The power is 16, and its opposite is $-16$.
- (e) $\left(-\frac{1}{2}\right)^3 = -\frac{1}{8}$. Three negative factors, and $\frac{1 \times 1 \times 1}{2 \times 2 \times 2} = \frac{1}{8}$.
- (f) $(-0.1)^2 = 0.01$. The square of a number between $-1$ and 1 is smaller in absolute value than the number itself.

Check (e) one factor at a time: $\left(-\frac{1}{2}\right) \times \left(-\frac{1}{2}\right) = \frac{1}{4}$, and $\frac{1}{4} \times \left(-\frac{1}{2}\right) = -\frac{1}{8}$.

</div>

<div class="example" markdown>

### Example 3: a fraction bar and nested brackets

Work out $\dfrac{4^2 - 2 \times 5}{3 - 3^2} + [6 - (2 - 5)]$.

The fraction bar and the square brackets are grouping symbols, so Step 1 works out each one first, following Steps 2 to 4 inside it.

- Numerator: the power first, $4^2 = 16$, then the product, $2 \times 5 = 10$, then $16 - 10 = 6$.
- Denominator: $3^2 = 9$, then $3 - 9 = -6$.
- The fraction is $6 \div (-6) = -1$.
- Square brackets: the inner pair first, $2 - 5 = -3$, then $6 - (-3) = 6 + 3 = 9$.

Finally, $-1 + 9 = 8$.

Check in Python, with brackets around the numerator and the denominator: `(4**2 - 2*5) / (3 - 3**2) + (6 - (2 - 5))` gives `8.0`.

</div>

<div class="example" markdown>

### Example 4: absolute value bars (finish it yourself)

Work out $\lvert 3 - 5^2 \rvert - 4 \times (-2)^3 \div 8$.

Step 1: inside the bars, the power comes first, so $3 - 25 = -22$, and $\lvert -22 \rvert = 22$.

Step 2: $(-2)^3 = -8$, since three negative factors give a negative product.

The expression is now $22 - 4 \times (-8) \div 8$. Finish Steps 3 and 4, and check your answer.

<details class="solution" markdown>
<summary>Finish</summary>

Step 3, from left to right: $4 \times (-8) = -32$, then $-32 \div 8 = -4$. Step 4: $22 - (-4) = 22 + 4 = 26$.

Check: Python's `abs(3 - 5**2) - 4 * (-2)**3 / 8` gives `26.0`.

</details>

</div>

## Edge cases and common mistakes

Dropping the brackets around a negative base is flagged in Example 1. Here are the others.

<div class="warning" markdown>

Watch out: $-3^2$ is $-9$, not 9. The exponent is attached to the 3, and the minus sign is applied afterwards. Only $(-3)^2$ squares the negative number. The same goes for every even power: $-5^4 = -625$, while $(-5)^4 = 625$.

</div>

<div class="warning" markdown>

Watch out: an exponent doesn't split over a sum. For example, $(3 + 4)^2 = 7^2 = 49$, but $3^2 + 4^2 = 9 + 16 = 25$. Multiplying out $(3 + 4) \times (3 + 4)$ with the distributive property gives $9 + 12 + 12 + 16 = 49$, and the two middle products are what $3^2 + 4^2$ leaves out. The general version, $(a + b)^2 = a^2 + 2ab + b^2$, is in [polynomial arithmetic](../../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md). An exponent does split over a product, $(2 \times 3)^2 = 36 = 2^2 \times 3^2$, which is one of the [exponent rules](../04-powers-roots-and-real-numbers/01-exponent-rules.md).

</div>

<div class="warning" markdown>

Watch out: multiplication doesn't come before division, and addition doesn't come before subtraction. In $8 \div 2 \times 4$, left to right gives $4 \times 4 = 16$. Multiplying first gives $8 \div 8 = 1$, which is wrong. BEDMAS lists D before M and PEMDAS lists M before D, and both mean "these two together, left to right".

</div>

<div class="warning" markdown>

Watch out for the base of a power. In $2 \times 3^2$ only the 3 is squared, so the value is 18, not $6^2 = 36$. In $\left(\frac{2}{3}\right)^2$ the whole fraction is squared, giving $\frac{4}{9}$, while in $\frac{2^2}{3}$ only the numerator is, giving $\frac{4}{3}$.

</div>

The exponent is a count, not a factor, as in [powers of ten](../../01-elementary/14-powers-of-ten.md#edge-cases-and-common-mistakes): $3^4 = 3 \times 3 \times 3 \times 3 = 81$, not $3 \times 4 = 12$.

Zero needs care. For every positive integer $n$, $0^n = 0$. For every $b \ne 0$, $b^0 = 1$, so $(-7)^0 = 1$, while $-7^0 = -(7^0) = -1$. The expression $0^0$ is left undefined in this lesson; Python gives `0**0` as 1, and the question comes back in [exponent rules](../04-powers-roots-and-real-numbers/01-exponent-rules.md).

Squaring doesn't always make a number bigger. For a number between 0 and 1 the square is smaller, as in $0.5^2 = 0.25$. For a negative number the square is positive, so it is bigger than the number: $(-0.5)^2 = 0.25 > -0.5$.

## Tricks and shortcuts

These powers come up often enough to know by heart. The last column is the one a CS course uses most, since $2^n$ counts the values that fit in $n$ bits ([number bases and conversions](../../06-cs-math/01-number-representation/01-number-bases-and-conversions.md)).

| $n$ | $n^2$ | $n^3$ | $2^n$ |
|---|---|---|---|
| 1 | 1 | 1 | 2 |
| 2 | 4 | 8 | 4 |
| 3 | 9 | 27 | 8 |
| 4 | 16 | 64 | 16 |
| 5 | 25 | 125 | 32 |
| 6 | 36 | 216 | 64 |
| 7 | 49 | 343 | 128 |
| 8 | 64 | 512 | 256 |
| 9 | 81 | 729 | 512 |
| 10 | 100 | 1000 | 1024 |

The squares from 11 to 15 are 121, 144, 169, 196 and 225.

To square a number that ends in 5, multiply the digits in front of the 5 by one more than themselves and write 25 after the result. For $35^2$, work out $3 \times 4 = 12$ and write 25 after it: 1225. Similarly $65^2 = 4225$, since $6 \times 7 = 42$. It works because $(10a + 5)^2 = 100a^2 + 100a + 25 = 100a(a + 1) + 25$, by the distributive property used twice.

To check a long calculation, write it out again with every bracket that the order of operations adds. If the fully bracketed version reads the way you meant, the calculation was set up right.

The sign of a power of a negative number depends only on whether the exponent is even or odd, so decide the sign first and then work out the power of the absolute value: $(-3)^5 = -(3^5) = -243$.

## In code

Python's `**` operator is done before a minus sign on its left, so `-3**2` is $-9$, matching the order in this lesson.

<details class="code" markdown>
<summary>In code</summary>

```python
print(-3**2, (-3)**2)          # -9 9
print(-3**2 == -9)             # True
print(2**3**2, (2**3)**2)      # 512 64
print(2**-1)                   # 0.5
print(8 / 4 / 2, 10 - 4 + 3)   # 1.0 9
print(12 + 6 / 3 + 6, (12 + 6) / (3 + 6))  # 20.0 2.0
```

A minus sign on the right of `**` belongs to the exponent, so `2**-1` is $2^{-1} = \frac{1}{2}$, a preview of negative exponents. Stacked powers group from the right, so `2**3**2` is `2**9`. The operators `/` and `-` work from left to right, giving 1 and 9, and `/` always gives a float. The last line shows that a fraction typed on one line needs brackets around its numerator and its denominator.

</details>

## FAQ

### Is the order of operations a theorem?

No, it is a convention, like driving on the right side of the road. Another order would work if everyone used it, but common expressions would need more brackets. Compare the sign rules from [integer arithmetic and sign rules](02-integer-arithmetic-and-sign-rules.md): those are forced by the distributive property, and no other choice is possible. The order of operations is chosen; the value of $(-3) \times (-4)$ is not.

### Does a product written without a times sign come first?

By the rules in this lesson, no. A product written side by side, such as $2(1 + 2)$, has the same rank as every other multiplication. So $6 \div 2(1 + 2)$ is $6 \div 2 \times 3$, which is $3 \times 3 = 9$ from left to right. Some people and some calculators treat a product without a sign as a single unit, and they get $6 \div 6 = 1$. Since careful readers disagree, the expression is badly written, not a puzzle with a hidden answer. Write $\frac{6}{2}(1 + 2)$ or $\frac{6}{2(1 + 2)}$, whichever you mean. [Variables and expressions](../03-expressions-equations-inequalities/01-variables-and-expressions.md#how-should-i-read-a-division-followed-by-brackets) gives the same advice for $1/2x$.

### Why is a nonzero number to the power 0 equal to 1?

Read a list of powers from the top down. Each line divides the one above it by the base, and the exponent drops by 1: $2^3 = 8$, $2^2 = 4$, $2^1 = 2$. One more division by 2 gives $2^0 = 1$. The same pattern works for every nonzero base, which is why $b^0 = 1$ is the definition; [powers of ten](../../01-elementary/14-powers-of-ten.md#zero-and-negative-exponents) shows it for base 10.

## Practice

### Warm-up

1\. Work out (a) $5^3$, (b) $(-5)^2$, (c) $-5^2$, (d) $\left(\frac{3}{4}\right)^2$, (e) $(-1)^7$ and (f) $0.2^3$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $5 \times 5 \times 5 = 125$.
- (b) $(-5) \times (-5) = 25$.
- (c) The base is 5, so $-(5^2) = -25$.
- (d) $\frac{3 \times 3}{4 \times 4} = \frac{9}{16}$.
- (e) An odd power of $-1$: $-1$.
- (f) $0.2 \times 0.2 \times 0.2 = 0.008$: the digits are $2 \times 2 \times 2 = 8$, with $1 + 1 + 1 = 3$ decimal places.

Check (f) with fractions: $\left(\frac{1}{5}\right)^3 = \frac{1}{125}$, and $1 \div 125 = 0.008$.

</details>

2\. Work out (a) $18 - 6 \div 3$, (b) $18 \div 6 \times 3$, (c) $18 - 6 + 3$ and (d) $2 + 3 \times 4^2$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Division first: $6 \div 3 = 2$, and $18 - 2 = 16$.
- (b) Left to right: $18 \div 6 = 3$, then $3 \times 3 = 9$.
- (c) Left to right: $18 - 6 = 12$, then $12 + 3 = 15$.
- (d) The power first, $4^2 = 16$, then $3 \times 16 = 48$, then $2 + 48 = 50$.

Check with full brackets: $18 - (6 \div 3)$, $(18 \div 6) \times 3$, $(18 - 6) + 3$ and $2 + (3 \times (4^2))$.

</details>

3\. Put brackets into $2 + 6 \times 5 - 1$ to make it equal (a) 39, (b) 26 and (c) 32. What is its value with no brackets?

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $(2 + 6) \times 5 - 1 = 40 - 1 = 39$.
- (b) $2 + 6 \times (5 - 1) = 2 + 24 = 26$.
- (c) $(2 + 6) \times (5 - 1) = 8 \times 4 = 32$.

With no brackets, the multiplication comes first: $2 + 30 - 1 = 31$.

Check: each version gives a different value, which is why the brackets have to be written whenever the intended order isn't the standard one.

</details>

### Standard

4\. Work out (a) $3 \times [10 - (4 - 6)^2]$, (b) $\dfrac{-2 \times 3^2 + 6}{(-2)^2 - 1}$ and (c) $-4^2 \div 8 \times (-3)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Inner brackets: $4 - 6 = -2$, and $(-2)^2 = 4$. Square brackets: $10 - 4 = 6$. Then $3 \times 6 = 18$.

(b) Numerator: $3^2 = 9$, $-2 \times 9 = -18$, and $-18 + 6 = -12$. Denominator: $(-2)^2 = 4$, and $4 - 1 = 3$. The value is $-12 \div 3 = -4$.

(c) The power first, with base 4: $-4^2 = -16$. Then from left to right, $-16 \div 8 = -2$ and $-2 \times (-3) = 6$.

Check in Python: `3 * (10 - (4 - 6)**2)` gives `18`, `(-2 * 3**2 + 6) / ((-2)**2 - 1)` gives `-4.0`, and `-4**2 / 8 * (-3)` gives `6.0`.

</details>

5\. Predict what Python prints for each line, then check: (a) `-2**4`, (b) `(-2)**4`, (c) `30 / 5 / 3`, (d) `2 + 3 * 4**2 / 8`. (e) Type $\dfrac{5 + 7}{2 \times 3}$ as one line of Python, and say what `5 + 7 / 2 * 3` gives instead.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The power before the minus sign: $-(2^4)$, so `-16`.
- (b) The bracket makes $-2$ the base: `16`.
- (c) Left to right: $30 \div 5 = 6$, then $6 \div 3 = 2$, printed as `2.0` because `/` gives a float.
- (d) The power first, $4^2 = 16$, then from left to right $3 \times 16 = 48$ and $48 \div 8 = 6$, then $2 + 6$: `8.0`.
- (e) Bracket the numerator and the denominator: `(5 + 7) / (2 * 3)`, which gives `2.0`. Without brackets, `5 + 7 / 2 * 3` is $5 + (7 \div 2) \times 3 = 5 + 10.5 = 15.5$.

Check: running the five lines prints `-16`, `16`, `2.0`, `8.0`, and `2.0` and `15.5` for (e).

</details>

6\. You invest \$500 at 4% interest a year, and the interest is added to the balance at the end of each year. After 3 years the balance is $500 \times 1.04^3$ dollars. (a) Work out the balance to the cent. (b) A classmate types $(500 \times 1.04)^3$ instead. What does that compute, and why is it wrong?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The power first: $1.04^2 = 1.0816$ and $1.04^3 = 1.0816 \times 1.04 = 1.124864$. Then $500 \times 1.124864 = 562.432$, so the balance is \$562.43.

(b) It computes $520^3 = 140{,}608{,}000$, the cube of the balance after one year. The exponent should apply only to the growth factor 1.04, since each year multiplies the balance by 1.04 once. Cubing the dollar amount has no meaning, and the size check shows it: \$500 can't grow into \$140 million in three years at 4%.

Check (a) year by year: $500 \times 1.04 = 520$, then $520 \times 1.04 = 540.80$, then $540.80 \times 1.04 = 562.432$.

</details>

### Challenge

7\. Use the theorem and the lemma from [integer arithmetic and sign rules](02-integer-arithmetic-and-sign-rules.md#why-a-negative-times-a-negative-is-positive) to prove that for every number $a$, (a) $(-a)^2 = a^2$ and (b) $(-a)^3 = -a^3$. Then (c) explain why $-a^2$ is never positive.

<details class="solution" markdown>
<summary>Solution</summary>

We know the theorem $(-a) \times (-b) = a \times b$ and the lemma $a \times (-b) = -(a \times b)$, both for all numbers. We want the two identities for every $a$. The plan is to write each power as a product and apply the two results.

(a) By the definition of a square and the theorem with $b = a$,

$$
(-a)^2 = (-a) \times (-a) = a \times a = a^2.
$$

(b) Group the first two factors, then use part (a) and the lemma:

$$
\begin{aligned}
(-a)^3 &= \bigl((-a) \times (-a)\bigr) \times (-a) && \text{definition of a cube} \\
&= a^2 \times (-a) && \text{part (a)} \\
&= -(a^2 \times a) && \text{lemma} \\
&= -a^3 && \text{definition of a cube}
\end{aligned}
$$

(c) First, $a^2 \ge 0$ for every $a$. If $a$ is positive or negative, $a^2 = a \times a$ is a product of two numbers with the same sign, which is positive by the sign rules; if $a = 0$, then $a^2 = 0$. The expression $-a^2$ means $-(a^2)$, the opposite of a number that is positive or 0, so it is negative or 0, never positive.

Look back: the same steps, repeated, show that $(-a)^n = a^n$ for every even $n$ and $(-a)^n = -a^n$ for every odd $n$. Proving that for every $n$ at once takes mathematical induction<!-- link: ../../04-proofs-and-logic/05-induction/01-mathematical-induction.md -->. Check with $a = 2$: $(-2)^2 = 4 = 2^2$, and $(-2)^3 = -8 = -(2^3)$.

</details>

8\. This one reviews [powers of ten](../../01-elementary/14-powers-of-ten.md) and expanded form. Work out (a) $3 \times 10^2 + 4 \times 10^1 + 7 \times 10^0$, (b) $2 \times 10^{-1} + 5 \times 10^{-2}$ and (c) $1 \times 2^3 + 0 \times 2^2 + 1 \times 2^1 + 1 \times 2^0$. Then say why these expressions need no brackets.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The powers first: $10^2 = 100$, $10^1 = 10$ and $10^0 = 1$. The products are 300, 40 and 7, and the sum is 347.

(b) $10^{-1} = 0.1$ and $10^{-2} = 0.01$, so the products are 0.2 and 0.05, and the sum is 0.25.

(c) The powers are 8, 4, 2 and 1, the products are 8, 0, 2 and 1, and the sum is 11. This is the binary numeral $1011_2$ written out, as in [number bases and conversions](../../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

No brackets are needed because the order of operations already does what expanded form means: each power is worked out, then each digit is multiplied by its power, and only then are the pieces added.

Check: 347 is 3 hundreds, 4 tens and 7 ones; 0.25 is 2 tenths and 5 hundredths; and in Python, `0b1011` is `11`.

</details>

## Where this shows up

- [Exponent rules](../04-powers-roots-and-real-numbers/01-exponent-rules.md) and [scientific notation](../04-powers-roots-and-real-numbers/02-scientific-notation.md) build on powers. [Variables and expressions](../03-expressions-equations-inequalities/01-variables-and-expressions.md) evaluates expressions such as $3x^2 - 5x$ by putting in a number and following this order, and a negative value needs brackets: for $x = -2$, the first term is $3 \times (-2)^2 = 12$.
- Every programming language has a precedence table, and a parser uses it to turn a line of code into a tree of operations. Context-free grammars and pushdown automata<!-- link: ../../06-cs-math/06-theory-of-computation/03-context-free-grammars-and-pushdown-automata.md --> shows how a grammar builds the order of operations into its rules.
- Compound interest<!-- link: ../../08-financial-math/02-interest-and-growth/02-compound-interest.md --> uses the formula from Practice problem 6, a starting amount times $(1 + r)^n$, where the exponent applies to the growth factor alone.
