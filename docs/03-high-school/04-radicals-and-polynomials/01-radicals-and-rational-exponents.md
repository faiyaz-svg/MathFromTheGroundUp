# Radicals and rational exponents

After this lesson you can evaluate and simplify $n$-th roots and rational powers such as $27^{2/3}$, add and multiply radicals, rationalize a denominator (including one like $\frac{1}{\sqrt{3} - 1}$), and compute an average growth rate with a root.

Before this: [exponent rules](../../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md), [roots, irrational numbers and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md) and [equivalent expressions](../../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Evaluate $27^{2/3}$ and $16^{-3/4}$.
2. Simplify $\sqrt{18x^4y^3}$, where $y \ge 0$.
3. Write $\dfrac{1}{\sqrt{3} - 1}$ with no radical in the denominator.

<details class="solution" markdown>
<summary>Answers</summary>

1. $27^{2/3} = (\sqrt[3]{27})^2 = 3^2 = 9$, and $16^{-3/4} = \dfrac{1}{(\sqrt[4]{16})^3} = \dfrac{1}{2^3} = \dfrac{1}{8}$.
2. $3x^2y\sqrt{2y}$. The radicand is $2 \cdot 3^2 \cdot x^4 \cdot y^3$, so $3$, $x^2$ and $y$ come out of the root, and $2y$ stays in.
3. Multiply the top and bottom by $\sqrt{3} + 1$, the conjugate of the denominator: $\dfrac{\sqrt{3} + 1}{(\sqrt{3})^2 - 1^2} = \dfrac{\sqrt{3} + 1}{2}$.

</details>

## The idea

You put \$1,000 in an account that grows by the same factor $f$ every year. After three years it holds \$1,331. Each year multiplies the balance by $f$, so $f \cdot f \cdot f = 1.331$. Since $1.1^3 = 1.331$, the factor is $f = 1.1$, a 10% raise each year. Finding $f$ undid a cube, so it was a cube root: $f = \sqrt[3]{1.331}$.

Now ask a stranger question. By what factor does the balance grow in half a year? Call that factor $g$. Two half-years make one year, so $g \cdot g = 1.1$, which says $g = \sqrt{1.1} \approx 1.0488$. After $t$ years the balance is multiplied by $1.1^t$, and half a year is $t = \frac{1}{2}$. So the number $1.1^{1/2}$ ought to be the number that squares to 1.1, which is $g$.

The exponent rules you already know say what a fractional exponent has to mean: if $(1.1^{1/2})^2 = 1.1^{(1/2) \cdot 2} = 1.1^1$ is going to hold, then $1.1^{1/2}$ is a square root of 1.1. Roots and fractional powers are the same thing written two ways. The exponent form is better for calculating with the exponent rules, and the radical form is better for reading off a value. Moving between them, and cleaning up expressions that contain roots, is the skill this lesson builds.

## Definitions

Let $n$ be an integer with $n \ge 2$. An **$n$-th root** of a number $a$ is a number $b$ with $b^n = a$. The integer $n$ is the **index** of the root. For $n = 2$ and $n = 3$ these are the square roots and cube roots from the [last chapter](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#definitions). The real $n$-th roots of a number depend on whether $n$ is odd or even:

| Index $n$ | Number $a$ | Real $n$-th roots of $a$ | Example |
|---|---|---|---|
| odd | any real number | exactly one | $-8$ has one cube root, $-2$ |
| even | $a > 0$ | two, a positive one and its negative | 16 has the 4th roots $2$ and $-2$ |
| even | $a = 0$ | one, namely 0 | the only square root of 0 is 0 |
| even | $a < 0$ | none | $-16$ has no real 4th root |

The last row holds because an even power of a real number is never negative.

The **principal $n$-th root** of $a$, written $\sqrt[n]{a}$, is the one real $n$-th root when $n$ is odd, and the non-negative one when $n$ is even and $a \ge 0$. The symbol $\sqrt{a}$ is short for $\sqrt[2]{a}$. In plain words, $\sqrt[n]{a}$ is one number, and it is negative only when $n$ is odd and $a$ is negative. So $\sqrt[4]{16} = 2$, never $-2$, and $\sqrt[3]{-27} = -3$. The expression $\sqrt[4]{-16}$ has no value among the real numbers.

A **rational exponent** is an exponent that is a fraction $\frac{m}{n}$ of integers with $n \ge 2$. For a base $a > 0$, a power with a rational exponent is defined by

$$
a^{1/n} = \sqrt[n]{a}, \qquad a^{m/n} = \left(\sqrt[n]{a}\right)^m = \sqrt[n]{a^m}.
$$

In plain words, the denominator of the exponent is the index of the root, and the numerator is an ordinary power. So $8^{2/3}$ means "take the cube root of 8, then square it", which is $2^2 = 4$. A negative exponent still means a reciprocal: $a^{-m/n} = \dfrac{1}{a^{m/n}}$. For $a = 0$ the value $0^{m/n}$ is 0 when $m > 0$ and undefined when $m < 0$. For a negative base the definition is used only when $n$ is odd and the fraction $\frac{m}{n}$ is in lowest terms; the section on [edge cases](#edge-cases-and-common-mistakes) shows what goes wrong otherwise.

With these definitions, all five [laws of exponents](../../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md#definitions) hold for every positive base and every rational exponent. Reading three of them as statements about radicals gives the rules for working with roots. For $n$ even, they hold when $a \ge 0$ and $b \ge 0$ (and $b > 0$ in the quotient); for $n$ odd, they hold for all real $a$ and $b$.

| Rule | In radicals | From the exponent law |
|---|---|---|
| product | $\sqrt[n]{ab} = \sqrt[n]{a}\,\sqrt[n]{b}$ | $(ab)^{1/n} = a^{1/n}b^{1/n}$ |
| quotient | $\sqrt[n]{\dfrac{a}{b}} = \dfrac{\sqrt[n]{a}}{\sqrt[n]{b}}$ | $\left(\dfrac{a}{b}\right)^{1/n} = \dfrac{a^{1/n}}{b^{1/n}}$ |
| root of a root | $\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$ | $\left(a^{1/n}\right)^{1/m} = a^{1/(mn)}$ |

One more fact is the reason absolute values appear below. For every real number $a$,

$$
\sqrt[n]{a^n} = \begin{cases} a & \text{if } n \text{ is odd,} \\ \lvert a \rvert & \text{if } n \text{ is even.} \end{cases}
$$

For example, $\sqrt[3]{(-2)^3} = \sqrt[3]{-8} = -2$, while $\sqrt[4]{(-2)^4} = \sqrt[4]{16} = 2 = \lvert -2 \rvert$. An even power erases the sign, and the principal root never gives it back. This is the same fact as $\sqrt{a^2} = \lvert a \rvert$ from the last chapter.

A radical expression is in **simplest radical form** when three things hold: no factor of the radicand is a perfect $n$-th power other than 1, no factor in the radicand has an exponent of $n$ or more, and no radical remains in a denominator. The third condition is done by **rationalizing the denominator**: multiplying the top and bottom of a fraction by the same nonzero number so that the new denominator has no radical. When the denominator is a sum or difference with a square root, such as $\sqrt{3} - 1$, the multiplier is its **conjugate**, the same two terms with the sign between them flipped: $\sqrt{3} + 1$. The product of conjugates is a difference of squares,

$$
(a - b)(a + b) = a^2 - ab + ba - b^2 = a^2 - b^2,
$$

so if $a$ or $b$ is a square root, squaring it removes the radical.

The picture shows why the index decides which numbers have roots. Taking an $n$-th root undoes the $n$-th power, so the graph of $y = x^{1/n}$ is the graph of $y = x^n$ reflected in the line $y = x$. A square is never negative, so only numbers $x \ge 0$ have a square root. A cube keeps the sign, so every number $x$ has a cube root.

![Two panels. Left: y equals x squared for x from 0 to about 2.2 and its mirror image y equals x to the one half, which exists only for x at least 0, both meeting the dashed line y equals x at 0 and 1. Right: y equals x cubed and its mirror image y equals x to the one third, which passes through the negative numbers, meeting the dashed line y equals x at minus 1, 0 and 1.](../../assets/figures/03-high-school/radicals-and-rational-exponents-roots-and-powers.svg)

## How to do it

### Why the exponent rules force these definitions

Here is a theorem that says why the definition of $a^{1/n}$ is not a choice. We know the power of a power rule, $(a^p)^q = a^{pq}$, for integer exponents. We want to find out what $a^{1/n}$ has to be, for $a > 0$, if the same rule is to keep working for a fractional exponent. The plan is to apply the rule with $p = \frac{1}{n}$ and $q = n$.

*Theorem.* Let $a > 0$ and let $n \ge 2$ be an integer. If $(a^p)^q = a^{pq}$ holds for $p = \frac{1}{n}$ and $q = n$, then $a^{1/n}$ is a positive $n$-th root of $a$. There is exactly one such number, $\sqrt[n]{a}$, so $a^{1/n} = \sqrt[n]{a}$.

*Proof.* The rule gives $\left(a^{1/n}\right)^n = a^{(1/n) \cdot n} = a^1 = a$. So $a^{1/n}$ is an $n$-th root of $a$, and we also want it positive, since powers of a positive number should be positive. A positive $n$-th root exists because the real number line has no gaps (the axioms are in [real numbers, axioms and set notation](../01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md)). It is unique: if $0 < b < c$, then multiplying the inequality $b < c$ by itself $n$ times gives $b^n < c^n$, so two different positive numbers never have the same $n$-th power. $\blacksquare$

The same rule gives the meaning of $a^{m/n}$. With $p = \frac{1}{n}$ and $q = m$, we get $a^{m/n} = \left(a^{1/n}\right)^m = \left(\sqrt[n]{a}\right)^m$. With $p = m$ and $q = \frac{1}{n}$, we get $a^{m/n} = (a^m)^{1/n} = \sqrt[n]{a^m}$. The two forms are the same number, because $\left(\sqrt[n]{a}\right)^m$ is positive and its $n$-th power is $\left(\left(\sqrt[n]{a}\right)^n\right)^m = a^m$, so it is the positive $n$-th root of $a^m$.

Look back: nothing in the argument depended on a particular $a$ or $n$. Every fractional exponent has exactly one value that keeps the exponent rules true, so the notation $a^{1/n}$ follows from the rules. The same reasoning is how irrational exponents such as $2^{\sqrt{2}}$ get a meaning, by squeezing them between rational exponents (the FAQ comes back to this).

### Evaluating a rational power

1. Write the exponent as a fraction $\frac{m}{n}$ in lowest terms, with $n > 0$.
2. If $m$ is negative, take the reciprocal of the base and make $m$ positive.
3. Take the $n$-th root of the base first, then raise the result to the power $m$. Doing the root first keeps the numbers small.
4. Check by undoing it: raise your answer to the power $\frac{n}{m}$ (or to $-\frac{n}{m}$ if you flipped the base), and you should get the original base.

### Simplifying a radical with variables

1. Break the radicand into factors: prime factors for the number, and each variable with its exponent.
2. For each factor $p^k$ under an index $n$, divide: $k = qn + r$ with $0 \le r < n$. Then $p^q$ comes out of the root and $p^r$ stays.
3. Decide on absolute values. If $n$ is even, the part that comes out of the root for a variable $x$ is $\lvert x \rvert^q$. That is just $x^q$ when $q$ is even, and $\lvert x^q \rvert$ when $q$ is odd. Drop the bars when the problem says $x \ge 0$, and when the radicand itself forces $x \ge 0$. For $n$ odd there are no bars.
4. Multiply what came out, and write what stayed in a single radical.
5. Check by raising your answer to the index, and by trying a value, including a negative one if bars are in play.

### Adding, subtracting and multiplying radicals

Radicals add like the like terms in [equivalent expressions](../../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md): they must have the same index and the same radicand, and then the distributive property combines the coefficients. Simplify each radical first, because radicals that look different sometimes have the same radicand underneath:

$$
\sqrt{75} - 2\sqrt{12} + \sqrt{27} = 5\sqrt{3} - 4\sqrt{3} + 3\sqrt{3} = 4\sqrt{3}.
$$

To multiply, use the distributive property on every pair of terms and the product rule on every pair of radicals. For example,

$$
(2\sqrt{3} - \sqrt{5})(\sqrt{3} + 2\sqrt{5}) = 2 \cdot 3 + 4\sqrt{15} - \sqrt{15} - 2 \cdot 5 = -4 + 3\sqrt{15}.
$$

When two radicals have different indices, rewrite them with rational exponents so that the exponent rules apply: $\sqrt{2} \cdot \sqrt[3]{2} = 2^{1/2} \cdot 2^{1/3} = 2^{5/6} = \sqrt[6]{2^5} = \sqrt[6]{32}$.

### Rationalizing a denominator

1. Simplify the denominator and the numerator first. For instance, $\frac{2}{\sqrt{8}} = \frac{2}{2\sqrt{2}} = \frac{1}{\sqrt{2}}$.
2. If the denominator is a single square root $\sqrt{b}$, multiply the top and bottom by $\sqrt{b}$, since $\sqrt{b} \cdot \sqrt{b} = b$.
3. If it is a single $n$-th root with $n > 2$, multiply by whatever makes the radicand a perfect $n$-th power. For $\sqrt[3]{2}$ that is $\sqrt[3]{4}$, since $\sqrt[3]{2} \cdot \sqrt[3]{4} = \sqrt[3]{8} = 2$.
4. If it is a sum or difference containing a square root, multiply the top and bottom by its conjugate. The new denominator is a difference of squares.
5. Multiply out, simplify, and check with a calculator: the decimal value must not have changed.

Both the top and the bottom get multiplied, so the fraction is multiplied by $\frac{\sqrt{b}}{\sqrt{b}}$, which is 1.

## Worked examples

<div class="example" markdown>

### Example 1: a negative fractional exponent

Evaluate $\left(\dfrac{27}{8}\right)^{-2/3}$.

Step 1: the exponent $-\frac{2}{3}$ is already in lowest terms, so $m = -2$ and $n = 3$.

<div class="warning" markdown>

Watch out at Step 1: the 3 is the index of the root, not something to divide by. Writing $27^{2/3} = \frac{27^2}{3}$ is a common slip. The correct reading is "cube root, then square".

</div>

Step 2: the exponent is negative, so take the reciprocal of the base:

$$
\left(\frac{27}{8}\right)^{-2/3} = \left(\frac{8}{27}\right)^{2/3}.
$$

Step 3: take the cube root first. Since $2^3 = 8$ and $3^3 = 27$, the cube root of $\frac{8}{27}$ is $\frac{2}{3}$. Then square it:

$$
\left(\frac{8}{27}\right)^{2/3} = \left(\frac{2}{3}\right)^2 = \frac{4}{9}.
$$

Step 4: check by undoing it. We flipped the base, so raise the answer to $-\frac{3}{2}$: $\left(\frac{4}{9}\right)^{-3/2} = \left(\frac{9}{4}\right)^{3/2} = \left(\frac{3}{2}\right)^3 = \frac{27}{8}$, the original base.

</div>

<div class="example" markdown>

### Example 2: variables, and when absolute values are needed

Simplify $\sqrt{50x^6y^3}$, and then $\sqrt[3]{54x^7}$.

For the square root, Step 1 gives the factors $50 = 2 \cdot 5^2$, $x^6$ and $y^3$. Step 2, with index 2: $5^2$ gives a 5 outside and nothing inside. The power $x^6$ has $6 = 3 \cdot 2 + 0$, so $x^3$ comes out and nothing stays. The power $y^3$ has $3 = 1 \cdot 2 + 1$, so one $y$ comes out and one stays. The 2 stays in too.

Step 3: the index is even, and $x^3$ is an odd power, so it needs bars: $\lvert x^3 \rvert$. For $y$, the radicand $50x^6y^3$ can only be at least 0 if $y \ge 0$, so no bars are needed on $y$. Step 4:

$$
\sqrt{50x^6y^3} = 5\lvert x^3 \rvert\, y\sqrt{2y}.
$$

Step 5: try $x = -1$ and $y = 2$. The left side is $\sqrt{50 \cdot 1 \cdot 8} = \sqrt{400} = 20$, and the right side is $5 \cdot 1 \cdot 2 \cdot \sqrt{4} = 20$. Without the bars the right side would be $-20$, which is why the value $x = -1$ is the useful test.

For the cube root, the index is odd, so there are no bars. The number $54 = 27 \cdot 2 = 3^3 \cdot 2$ gives a 3 outside and a 2 inside. The power $x^7$ has $7 = 2 \cdot 3 + 1$, so $x^2$ comes out and one $x$ stays:

$$
\sqrt[3]{54x^7} = 3x^2\sqrt[3]{2x}.
$$

Check with $x = -2$: the left side is $\sqrt[3]{54 \cdot (-128)} = \sqrt[3]{-6912} \approx -19.05$, and the right side is $3 \cdot 4 \cdot \sqrt[3]{-4} \approx 12 \cdot (-1.587) = -19.05$.

</div>

<div class="example" markdown>

### Example 3: rationalizing with a conjugate

Write $\dfrac{1}{\sqrt{3} - 1}$ and $\dfrac{6}{\sqrt{5} + \sqrt{2}}$ without radicals in the denominators.

For the first, the denominator is a difference, so by Step 4 multiply the top and bottom by the conjugate $\sqrt{3} + 1$:

$$
\frac{1}{\sqrt{3} - 1} \cdot \frac{\sqrt{3} + 1}{\sqrt{3} + 1} = \frac{\sqrt{3} + 1}{(\sqrt{3})^2 - 1^2} = \frac{\sqrt{3} + 1}{3 - 1} = \frac{\sqrt{3} + 1}{2}.
$$

Check with decimals: $\frac{1}{1.7321 - 1} = 1.3660$ and $\frac{1.7321 + 1}{2} = 1.3660$.

For the second, the conjugate of $\sqrt{5} + \sqrt{2}$ is $\sqrt{5} - \sqrt{2}$:

$$
\frac{6}{\sqrt{5} + \sqrt{2}} \cdot \frac{\sqrt{5} - \sqrt{2}}{\sqrt{5} - \sqrt{2}} = \frac{6(\sqrt{5} - \sqrt{2})}{5 - 2} = 2(\sqrt{5} - \sqrt{2}) = 2\sqrt{5} - 2\sqrt{2}.
$$

Both of the radicals in the answer are fine; the rule only asks for none in the denominator. Check: $\frac{6}{2.2361 + 1.4142} = 1.6437$ and $2(2.2361 - 1.4142) = 1.6437$.

<div class="warning" markdown>

Watch out: multiplying by $\sqrt{3} - 1$ again, the same sign as the denominator, doesn't remove the radical. The product $(\sqrt{3} - 1)^2 = 4 - 2\sqrt{3}$ still has one. The flipped sign is what cancels the middle terms.

</div>

When the top is a binomial too, nothing changes. For $\dfrac{2 + \sqrt{3}}{2 - \sqrt{3}}$, multiply by $2 + \sqrt{3}$ on both levels: the bottom becomes $4 - 3 = 1$ and the top becomes $(2 + \sqrt{3})^2 = 7 + 4\sqrt{3}$, which is about 13.93, matching $\frac{3.732}{0.268}$.

</div>

<div class="example" markdown>

### Example 4: an average growth rate (finish it yourself)

A portfolio is worth \$10,000 at the start and \$14,000 five years later. What constant yearly growth rate would produce the same result?

Let $f$ be the yearly growth factor, so the value is multiplied by $f$ each year. After five years the value is $10{,}000 f^5$, so

$$
10{,}000 f^5 = 14{,}000, \qquad f^5 = 1.4, \qquad f = 1.4^{1/5}.
$$

A calculator gives $f \approx 1.0696$. Now turn $f$ into a percent rate, and check your answer by growing \$10,000 for five years at that rate.

<details class="solution" markdown>
<summary>Finish</summary>

The rate is $r = f - 1 \approx 0.0696$, which is about 6.96% per year.

Check: $1.0696^5 \approx 1.39993$, so \$10,000 grows to about \$13,999, which is \$14,000 up to the rounding of $f$. With the unrounded factor the match is exact, since $(1.4^{1/5})^5 = 1.4$.

The tempting shortcut is to split the 40% total growth over 5 years and get 8% a year. That is too high: $1.08^5 \approx 1.4693$, which grows \$10,000 to about \$14,693. Growth compounds, so the right "average" is the fifth root of the total growth factor.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: $\sqrt{x^2}$ is $\lvert x \rvert$, not $x$. With $x = -3$, $\sqrt{(-3)^2} = \sqrt{9} = 3$, not $-3$. The root of a square is only equal to $x$ when $x \ge 0$. The same goes for every even index: $\sqrt[4]{x^4} = \lvert x \rvert$.

</div>

<div class="warning" markdown>

Watch out: a root of a sum is not the sum of the roots. The expression $\sqrt{x^2 + 9}$ is not $x + 3$: at $x = 4$ the left side is $\sqrt{25} = 5$ and the right side is 7. The product rule, $\sqrt{ab} = \sqrt{a}\sqrt{b}$, has no version for addition. For the same reason, $\sqrt{2} + \sqrt{3} \ne \sqrt{5}$, and $\sqrt{2} + \sqrt{2} = 2\sqrt{2}$, not $\sqrt{4}$.

</div>

<div class="warning" markdown>

Watch out for negative bases with fractional exponents. The exponents $\frac{1}{3}$ and $\frac{2}{6}$ are equal. With the first, $(-8)^{1/3} = \sqrt[3]{-8} = -2$. With the second, the form $\sqrt[6]{(-8)^2} = \sqrt[6]{64}$ is $2$. One exponent would give two answers, so the rules can't hold for negative bases and fractional exponents together. That is why a negative base is allowed only with an odd index and the exponent in lowest terms, and why many courses avoid negative bases with fractional exponents altogether.

</div>

<div class="warning" markdown>

Watch out: an even root of a negative number is not a real number. The expression $\sqrt{-4}$ is not $-2$ (since $(-2)^2 = 4$, not $-4$) and not $2$. It has no value among the real numbers, and the [complex numbers](../05-quadratics-and-complex-numbers/03-complex-numbers.md) are the extension that gives it one. An answer that needs the square root of a negative number means "no real solution" until then.

</div>

Rationalizing multiplies the top and the bottom by the same thing. Multiplying only the bottom by $\sqrt{3}$ changes the value of the fraction by a factor of $\sqrt{3}$.

A root that is an untidy decimal is not a mistake. The answer $\sqrt{5} + 1$ is exact, and $3.236$ is an approximation of it. Leave the radical in until the last line if the answer feeds a later step, so rounding errors don't pile up.

## Tricks and shortcuts

To simplify a radical with a big number, factor the number into primes and divide each exponent by the index. The quotient comes out and the remainder stays. For $\sqrt[3]{432}$: $432 = 2^4 \cdot 3^3$. The 3s give $3^{3/3} = 3$ outside. The 2s give $2^4 = 2^{3} \cdot 2$, so a 2 comes out and a 2 stays in. The answer is $3 \cdot 2 \cdot \sqrt[3]{2} = 6\sqrt[3]{2}$.

Knowing the perfect powers by sight makes roots fast. These come up all the time:

| Powers | Values |
|---|---|
| squares of 1 to 15 | 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225 |
| cubes of 1 to 10 | 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000 |
| fourth powers of 1 to 5 | 1, 16, 81, 256, 625 |
| powers of 2 | 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 |

For a quick size check, a root of a number bigger than 1 is smaller than the number but still bigger than 1, and the bigger the index, the closer to 1: $\sqrt{1.4} \approx 1.18$, $\sqrt[5]{1.4} \approx 1.07$. When $a$ is less than 1, the root is larger than $a$.

Read $x^{a/b}$ aloud as "the $b$-th root of $x$, to the power $a$". Saying it that way keeps the denominator in the root and the numerator in the power.

## In code

Python's `**` operator accepts fractional exponents, but it works with floating-point approximations, and for a negative base it returns a complex number. The last lines show why rationalizing still matters: subtracting two nearly equal square roots loses digits, while the conjugate form doesn't.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

print(27 ** (2 / 3))              # 8.999999999999998, not exactly 9
print(math.cbrt(27) ** 2)         # 9.0
print((-8) ** (1 / 3))            # (1.0000000000000002+1.7320508075688772j)
print(math.cbrt(-8))              # -2.0
print((14000 / 10000) ** (1 / 5) - 1)   # 0.0696103757250688

x = 10**12
print(math.sqrt(x + 1) - math.sqrt(x))        # 5.00003807246685e-07
print(1 / (math.sqrt(x + 1) + math.sqrt(x)))  # 4.999999999998749e-07
```

The fractional power `27 ** (2 / 3)` is computed from the float `2 / 3`, which is not exactly two thirds, so the result is off in the last digit; the function `math.cbrt` (Python 3.11 and later) takes the cube root directly. For a negative base, `**` returns the principal complex cube root, not the real one; `math.cbrt(-8)` returns the real root $-2$. The last two lines compute the same number, since $\sqrt{x + 1} - \sqrt{x} = \frac{1}{\sqrt{x + 1} + \sqrt{x}}$, the second form being the one after rationalizing. The true value is $4.99999999999875 \times 10^{-7}$ (rounded). The subtraction gets only about 5 correct digits, because it subtracts two numbers near $10^6$ that agree in their first 13 digits. The conjugate form is correct to about 15 digits. Floating-point basics<!-- link: ../../06-cs-math/01-number-representation/04-floating-point-basics.md --> explains where such errors come from.

</details>

## FAQ

### Why rationalize the denominator, when a calculator doesn't care?

Mostly for a standard form. Two expressions are easy to compare, add and check when they are written the same way, and a denominator with no radical makes it easy to see that $\frac{1}{\sqrt{3} - 1}$ and $\frac{\sqrt{3} + 1}{2}$ are the same number. Before calculators, dividing by $1.7321 - 1$ by hand was much harder than dividing by 2. A modern reason is numerical: as the last section showed, the rationalized form can be more accurate in floating-point arithmetic. Some courses no longer require it, but it is still the expected form on many exams, and the conjugate trick comes back in limits and in complex numbers.

### What does an irrational exponent such as 2 to the power square root of 2 mean?

It is the number that the values $2^{1.4}$, $2^{1.41}$, $2^{1.414}$, and so on get closer and closer to. Each of those has a rational exponent, so each is a root of a power: $2^{1.4} = \sqrt[5]{2^7}$. The exponent rules still hold for the limit. [Exponential functions and growth](../07-exponentials-and-logarithms/01-exponential-functions-and-growth.md) uses this to define $b^x$ for every real $x$.

### Python says the cube root of $-8$ is complex. Is $-2$ wrong?

No. The number $-8$ has three cube roots among the complex numbers, namely $-2$ and $1 \pm \sqrt{3}\,i$, and $-2$ is the real one. Python computes `(-8) ** (1/3)` with a formula that picks the "principal" complex root, $1 + \sqrt{3}\,i$, and you can check that $(1 + \sqrt{3}\,i)^3 = -8$ once you know [complex numbers](../05-quadratics-and-complex-numbers/03-complex-numbers.md). In a real-number course, $\sqrt[3]{-8}$ means $-2$, and in code you ask for it with `math.cbrt`.

### Is the $n$-th root the only way to undo a power?

For the power function $x \mapsto x^n$ on the positive numbers, yes. The root is its inverse, as the reflection picture shows. For other situations the inverse is a different function: to undo $2^x$ you need a logarithm, which is the topic of [logarithms](../07-exponentials-and-logarithms/02-logarithms.md).

## Practice

### Warm-up

1\. Evaluate (a) $\sqrt[3]{-125}$, (b) $16^{3/4}$, (c) $9^{-1/2}$ and (d) $\left(\frac{1}{4}\right)^{-3/2}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $(-5)^3 = -125$, so the cube root is $-5$.
- (b) The fourth root of 16 is 2, and $2^3 = 8$.
- (c) Reciprocal first: $9^{-1/2} = \frac{1}{9^{1/2}} = \frac{1}{3}$.
- (d) Flip the base: $\left(\frac{1}{4}\right)^{-3/2} = 4^{3/2} = (\sqrt{4})^3 = 2^3 = 8$.

Check by undoing each one: $(-5)^3 = -125$; $8^{4/3} = (\sqrt[3]{8})^4 = 16$; $\left(\frac{1}{3}\right)^{-2} = 9$; and $8^{-2/3} = \frac{1}{4}$, so raising $\frac{1}{4}$ to $-\frac{3}{2}$ gives back 8.

</details>

2\. Write (a) $x^{3/5}$ in radical form, and write (b) $\sqrt[4]{y^3}$, (c) $\dfrac{1}{\sqrt[3]{z}}$ and (d) $\sqrt{x}\,\sqrt[3]{x}$ with rational exponents, as a single power where possible.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The denominator is the index and the numerator is the power: $\sqrt[5]{x^3}$.
- (b) $y^{3/4}$.
- (c) A reciprocal makes the exponent negative: $\dfrac{1}{z^{1/3}} = z^{-1/3}$.
- (d) Add the exponents: $x^{1/2} \cdot x^{1/3} = x^{1/2 + 1/3} = x^{5/6}$.

Check (d) with $x = 64$: $\sqrt{64} \cdot \sqrt[3]{64} = 8 \cdot 4 = 32$, and $64^{5/6} = (\sqrt[6]{64})^5 = 2^5 = 32$.

</details>

3\. Simplify (a) $\sqrt{200}$, (b) $\sqrt[3]{81}$, (c) $\sqrt{x^{10}}$ and (d) $\sqrt[4]{16x^8}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $200 = 100 \cdot 2$, so $\sqrt{200} = 10\sqrt{2}$.
- (b) $81 = 27 \cdot 3$, so $\sqrt[3]{81} = 3\sqrt[3]{3}$.
- (c) The exponent 10 divided by the index 2 is 5, which is odd, so the bars stay: $\sqrt{x^{10}} = \lvert x^5 \rvert$.
- (d) $16 = 2^4$ and $x^8 = (x^2)^4$, so $\sqrt[4]{16x^8} = 2x^2$. Here $q = 2$ is even, so no bars are needed ($x^2 \ge 0$ already).

Check: $(10\sqrt{2})^2 = 200$; $(3\sqrt[3]{3})^3 = 27 \cdot 3 = 81$; for (c) at $x = -1$, $\sqrt{1} = 1 = \lvert (-1)^5 \rvert$; $(2x^2)^4 = 16x^8$.

</details>

### Standard

4\. Simplify (a) $3\sqrt{20} - \sqrt{45} + \sqrt{5}$, (b) $(\sqrt{7} + 2)(\sqrt{7} - 2)$ and (c) $(3 + \sqrt{2})^2$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Simplify each radical: $\sqrt{20} = 2\sqrt{5}$ and $\sqrt{45} = 3\sqrt{5}$. So the sum is $6\sqrt{5} - 3\sqrt{5} + \sqrt{5} = 4\sqrt{5}$.

(b) These are conjugates, so the product is a difference of squares: $7 - 4 = 3$.

(c) $(3 + \sqrt{2})^2 = 9 + 2 \cdot 3\sqrt{2} + 2 = 11 + 6\sqrt{2}$. The middle term is easy to forget; the square of a sum is not the sum of the squares.

Check with decimals: (a) $3(4.4721) - 6.7082 + 2.2361 = 8.9443$, and $4\sqrt{5} = 8.9443$. (c) $(3 + 1.4142)^2 = 19.485$, and $11 + 6(1.4142) = 19.485$.

</details>

5\. Rationalize the denominator: (a) $\dfrac{5}{2\sqrt{3}}$, (b) $\dfrac{4}{\sqrt{7} - \sqrt{3}}$ and (c) $\dfrac{2}{\sqrt[3]{4}}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Multiply the top and bottom by $\sqrt{3}$: $\dfrac{5\sqrt{3}}{2 \cdot 3} = \dfrac{5\sqrt{3}}{6}$.

(b) Multiply by the conjugate $\sqrt{7} + \sqrt{3}$: the bottom becomes $7 - 3 = 4$, so the fraction is $\dfrac{4(\sqrt{7} + \sqrt{3})}{4} = \sqrt{7} + \sqrt{3}$.

(c) Multiply the top and bottom by $\sqrt[3]{2}$, since $\sqrt[3]{4} \cdot \sqrt[3]{2} = \sqrt[3]{8} = 2$: the result is $\dfrac{2\sqrt[3]{2}}{2} = \sqrt[3]{2}$.

Check with decimals: (a) $\frac{5}{3.4641} = 1.4434$ and $\frac{5(1.7321)}{6} = 1.4434$. (b) $\frac{4}{2.6458 - 1.7321} = 4.3778$ and $2.6458 + 1.7321 = 4.3778$. (c) $\frac{2}{1.5874} = 1.2599$ and $\sqrt[3]{2} = 1.2599$.

</details>

6\. (a) An investment grows from \$8,000 to \$12,000 in 4 years. Find the constant yearly growth rate. (b) An account pays an effective annual rate of 6%. What monthly rate $r$ gives the same yearly growth, so that $(1 + r)^{12} = 1.06$? Is it 0.5%?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The yearly factor $f$ satisfies $8000 f^4 = 12000$, so $f^4 = 1.5$ and $f = 1.5^{1/4} \approx 1.1067$. The rate is about 10.67% per year.

(b) Take the 12th root: $1 + r = 1.06^{1/12} \approx 1.004868$, so $r \approx 0.4868\%$ per month. It is not 0.5%, which is $6\% \div 12$: twelve months at 0.5% compound to $1.005^{12} \approx 1.0617$, a yearly growth of about 6.17%, which is more than 6%.

Check: (a) $8000 \times 1.1067^4 \approx 8000 \times 1.50010 \approx 12{,}001$, which is \$12,000 up to rounding. (b) $1.004868^{12} \approx 1.0600$.

</details>

### Challenge

7\. (a) Solve $x^{2/3} = 9$. (b) Solve $x^{3/2} = 8$. (c) Why would raising both sides of (a) to the power $\frac{3}{2}$ miss one of the answers?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Since $x^{2/3} = (\sqrt[3]{x})^2$, the equation says $(\sqrt[3]{x})^2 = 9$, so $\sqrt[3]{x} = 3$ or $\sqrt[3]{x} = -3$. Cube both sides of each: $x = 27$ or $x = -27$.

(b) The expression $x^{3/2} = (\sqrt{x})^3$ needs $x \ge 0$. Then $(\sqrt{x})^3 = 8$ gives $\sqrt{x} = 2$, so $x = 4$. There is no second answer, because a negative $x$ has no square root.

(c) Raising both sides of $x^{2/3} = 9$ to $\frac{3}{2}$ gives $\left(x^{2/3}\right)^{3/2} = 9^{3/2} = 27$, and it is tempting to write $x = 27$ and stop. But the left side is not $x$ when $x$ is negative. With $u = \sqrt[3]{x}$, we have $x^{2/3} = u^2$ and $\left(u^2\right)^{3/2} = \left(\sqrt{u^2}\right)^3 = \lvert u \rvert^3 = \lvert x \rvert$. So the step really says $\lvert x \rvert = 27$, which allows both $27$ and $-27$. The power of a power rule $(x^{p})^{q} = x^{pq}$ is only guaranteed for a positive $x$.

Check: $27^{2/3} = 9$ and $(-27)^{2/3} = (-3)^2 = 9$. For (b), $4^{3/2} = 8$.

</details>

8\. (Reviews [roots, irrational numbers and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).) Prove that $\sqrt[3]{2}$ is irrational. First prove that if $n^3$ is even then $n$ is even, then imitate the proof for $\sqrt{2}$ (a [proof by contradiction](../../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md)).

<details class="solution" markdown>
<summary>Solution</summary>

*Lemma.* If $n$ is an integer and $n^3$ is even, then $n$ is even.

*Proof of the lemma.* Suppose $n$ is odd, so $n = 2k + 1$ for an integer $k$. Then $n^3 = 8k^3 + 12k^2 + 6k + 1 = 2(4k^3 + 6k^2 + 3k) + 1$, which is odd. So an odd $n$ has an odd cube, and if $n^3$ is even then $n$ is even. $\blacksquare$

*Theorem.* The number $\sqrt[3]{2}$ is irrational.

*Proof.* We know the definition of rational, and that a fraction can be written in simplest form. We want to show that no fraction equals $\sqrt[3]{2}$. Suppose, to get a contradiction, that $\sqrt[3]{2} = \frac{a}{b}$ with integers $a$ and $b \ne 0$ with no common factor other than 1. Cubing gives $2 = \frac{a^3}{b^3}$, so $a^3 = 2b^3$. Then $a^3$ is even, so by the lemma $a$ is even: $a = 2k$. Substituting, $8k^3 = 2b^3$, so $b^3 = 4k^3$, which is even, and the lemma says $b$ is even. Now $a$ and $b$ are both even, so they have the common factor 2, which contradicts the choice of the fraction in simplest form. So $\sqrt[3]{2}$ is irrational. $\blacksquare$

Look back and check: the argument depends on 2 not being a perfect cube. For $\sqrt[3]{8} = 2$, which is rational, the same steps give $a^3 = 8b^3$, so $a = 2k$ gives $8k^3 = 8b^3$ and $b^3 = k^3$, and no parity conclusion about $b$ follows, so no contradiction appears. The decimal value $\sqrt[3]{2} = 1.2599\ldots$ agrees with the claim that no fraction fits exactly.

</details>

## Where this shows up

- The next lesson, [polynomial arithmetic](02-polynomial-arithmetic.md), starts from the exponents here: a polynomial only has whole-number exponents, and $\sqrt{x} = x^{1/2}$ is not one. [Solving quadratic equations](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md) uses $\pm\sqrt{\ }$ in the quadratic formula, and [rational and radical equations](../06-rational-expressions-and-equations/03-rational-and-radical-equations.md) solves equations such as $\sqrt{x + 2} = x$ by squaring both sides.
- In CS, trial division tests whether $n$ is prime using only the divisors up to $\sqrt{n}$, so it takes about $n^{1/2}$ steps instead of $n$. Distance and vector length are square roots of sums of squares ([vectors in the plane](../10-vectors-and-matrices/01-vectors-in-the-plane.md)).
- In finance and economics, an average growth rate over $n$ periods is $\left(\frac{\text{end}}{\text{start}}\right)^{1/n} - 1$, which is the formula in Example 4 (compound interest<!-- link: ../../08-financial-math/02-interest-and-growth/02-compound-interest.md --> and growth rates and CAGR<!-- link: ../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md -->).
