# Exponent rules

After this lesson you can multiply, divide and raise powers by working with their exponents, use zero and negative exponents, and simplify expressions such as $\dfrac{(2x^3)^4}{8x^5}$ without writing out every factor.

Before this: [exponents and order of operations](../01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md), [powers of ten](../../01-elementary/14-powers-of-ten.md) and [equivalent expressions](../03-expressions-equations-inequalities/02-equivalent-expressions.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write each as a single power: $x^4 \cdot x^7$, $\dfrac{5^9}{5^6}$ and $(2^3)^4$.
2. Work out $4^{-2}$, $\left(\frac{2}{3}\right)^{-3}$ and $(-5)^0$.
3. Simplify $\dfrac{(2a^3 b)^2}{4a^8}$, with positive exponents only. Assume $a \ne 0$.

<details class="solution" markdown>
<summary>Answers</summary>

1. $x^{11}$, $5^3$ and $2^{12}$. Add the exponents to multiply, subtract them to divide, and multiply them for a power of a power.
2. $\frac{1}{16}$, $\frac{27}{8}$ and 1. A negative exponent takes the reciprocal: $4^{-2} = \frac{1}{4^2}$, and $\left(\frac{2}{3}\right)^{-3} = \left(\frac{3}{2}\right)^3$.
3. $\dfrac{b^2}{a^2}$. The numerator is $4a^6 b^2$, and $\frac{4a^6 b^2}{4a^8} = a^{6 - 8} b^2 = a^{-2} b^2$.

</details>

## The idea

A byte has 8 bits, so it can hold $2^8 = 256$ different values. Two bytes side by side give 256 choices for the first byte and 256 for the second, so they hold $2^8 \times 2^8$ values. Written out, that is eight 2s multiplied together, times eight more:

$$
2^8 \times 2^8 = \underbrace{2 \times \cdots \times 2}_{8 \text{ factors}} \times \underbrace{2 \times \cdots \times 2}_{8 \text{ factors}} = 2^{16} = 65{,}536.
$$

You didn't need to multiply 256 by 256 to get the power. You only had to count the 2s, and counting factors is adding exponents. The answer also fits what you know about bits: two bytes are 16 bits, and 16 bits hold $2^{16}$ values.

Every exponent rule in this lesson comes from the same move: write the powers out as factors, count, and write the count as a new exponent. Then we ask what $2^0$ and $2^{-3}$ should mean so that the rules keep working, and that question gives the definitions of zero and negative exponents.

## Definitions

Recall from [exponents and order of operations](../01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#definitions) that for a number $a$ and a positive integer $n$, the power $a^n$ is the product of $n$ copies of the base $a$. Two more definitions extend this to every integer exponent.

For every number $a \ne 0$, the **zero exponent** gives

$$
a^0 = 1.
$$

For every number $a \ne 0$ and every positive integer $n$, a **negative exponent** means a reciprocal:

$$
a^{-n} = \frac{1}{a^n}.
$$

In plain words, a negative exponent says how many times to divide by the base, starting from 1. So $2^{-3} = \frac{1}{2 \times 2 \times 2} = \frac{1}{8}$, which is a small positive number, not a negative one. The exponent $-1$ gives the plain reciprocal, $a^{-1} = \frac{1}{a}$, the same reciprocal used to divide fractions ([multiplying and dividing fractions](../../01-elementary/11-multiplying-and-dividing-fractions.md)).

The **laws of exponents**, also called the exponent rules, are the five identities below. They hold for all nonzero numbers $a$ and $b$ and all integers $m$ and $n$:

| Rule | Identity | Example |
|---|---|---|
| product | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^4 = 2^7$ |
| quotient | $\dfrac{a^m}{a^n} = a^{m-n}$ | $\dfrac{3^6}{3^2} = 3^4$ |
| power of a power | $(a^m)^n = a^{mn}$ | $(5^2)^3 = 5^6$ |
| power of a product | $(ab)^n = a^n b^n$ | $(2x)^3 = 8x^3$ |
| power of a quotient | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ | $\left(\dfrac{2}{3}\right)^2 = \dfrac{4}{9}$ |

In plain words: multiplying powers of the same base adds the exponents, dividing subtracts them, a power of a power multiplies them, and an exponent outside a product or a quotient goes onto each piece inside. The first three need the same base. The last two need the same exponent.

The dot $\cdot$ means multiplication, as in [variables and expressions](../03-expressions-equations-inequalities/01-variables-and-expressions.md). When the base is a letter, the rules hold for every nonzero value of the letter, which is why this lesson assumes that letters in a denominator or under a negative exponent are not 0.

## How to do it

### Why each rule is true

Take the exponents to be positive integers first, so that every power is a list of factors.

The product rule: $a^m \cdot a^n$ is $m$ copies of $a$ followed by $n$ more copies, which is $m + n$ copies. For example, $a^2 \cdot a^3 = (a \cdot a)(a \cdot a \cdot a) = a^5$.

The quotient rule, when $m > n$: write $\frac{a^m}{a^n}$ as a fraction with $m$ factors on top and $n$ below. Each factor below cancels one on top, which leaves $m - n$ factors:

$$
\frac{a^5}{a^2} = \frac{\cancel{a} \cdot \cancel{a} \cdot a \cdot a \cdot a}{\cancel{a} \cdot \cancel{a}} = a^3.
$$

The power of a power: $(a^m)^n$ is $n$ copies of $a^m$, and each copy is $m$ factors of $a$, so there are $n$ groups of $m$ factors, which is $mn$ factors. For example, $(a^2)^3 = a^2 \cdot a^2 \cdot a^2 = a^{2+2+2} = a^6$.

The power of a product: $(ab)^n$ is $n$ copies of $ab$. Multiplication can be done in any order ([properties of operations](../../01-elementary/04-properties-of-operations.md)), so collect the factors $a$ at the front and the factors $b$ at the back:

$$
(ab)^3 = (ab)(ab)(ab) = (a \cdot a \cdot a)(b \cdot b \cdot b) = a^3 b^3.
$$

The power of a quotient works the same way, because fractions multiply straight across: $\left(\frac{a}{b}\right)^3 = \frac{a}{b} \cdot \frac{a}{b} \cdot \frac{a}{b} = \frac{a \cdot a \cdot a}{b \cdot b \cdot b} = \frac{a^3}{b^3}$.

### Why a to the power 0 is 1

Now use the quotient rule with $m = n$. On one side, a nonzero number divided by itself is 1, so $\frac{a^3}{a^3} = 1$. On the other side, the rule says $\frac{a^3}{a^3} = a^{3-3} = a^0$. If the quotient rule is to keep working when the exponents are equal, $a^0$ has to be 1. That is why the definition says $a^0 = 1$: it is the only value that keeps the rules true, and it matches the pattern in [powers of ten](../../01-elementary/14-powers-of-ten.md#zero-and-negative-exponents), where each line divides the one above by 10.

### Why a negative exponent is a reciprocal

Use the quotient rule with $m < n$. Writing out the factors, two cancel and three are left below:

$$
\frac{a^2}{a^5} = \frac{\cancel{a} \cdot \cancel{a}}{\cancel{a} \cdot \cancel{a} \cdot a \cdot a \cdot a} = \frac{1}{a^3}.
$$

The rule says $\frac{a^2}{a^5} = a^{2-5} = a^{-3}$. So the rule keeps working only if $a^{-3} = \frac{1}{a^3}$, which is the definition. With these two definitions, all five rules hold for every integer exponent, positive, negative or zero. Practice problem 7 checks one of the new cases.

### What about 0 to the power 0

The argument for $a^0 = 1$ divided $a^3$ by itself, and when $a = 0$ that is $\frac{0}{0}$, which is undefined. So the argument says nothing about $0^0$. Two patterns also pull in different directions: $0^1 = 0^2 = 0^3 = 0$ suggests $0^0 = 0$, while $5^0 = 2^0 = 0.1^0 = 1$ suggests $0^0 = 1$.

So in arithmetic $0^0$ is left undefined, as the last lesson said. In calculus it is called an indeterminate form, because a limit that looks like $0^0$ can come out to different values ([linear approximation and L'Hopital's rule](../../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md)). Counting, polynomials and most programming languages use the convention $0^0 = 1$ instead, because it makes their formulas work without exceptions: $n^k$ counts the strings of length $k$ made from $n$ symbols, and there is exactly one string of length 0, the empty string, even when $n = 0$. Python follows that convention, so `0**0` is `1`.

Negative powers of 0 are undefined in every setting: $0^{-1}$ would be $\frac{1}{0}$.

### Simplifying an expression with exponents

1. Expand each bracket raised to a power. Use the power of a product or quotient to put the exponent on every factor inside, and the power of a power for factors that already have an exponent. A number in the bracket gets the exponent too: $(2x^3)^4 = 2^4 x^{12}$.
2. Collect each base. Within a product, add the exponents of the same base; for a base on the top and the bottom of a fraction, subtract the bottom exponent from the top one.
3. Work out the number parts with ordinary arithmetic, and simplify any fraction.
4. Tidy the exponents. Replace $a^0$ with 1, and if the question asks for positive exponents, rewrite $a^{-n}$ as $\frac{1}{a^n}$, which moves the factor across the fraction bar.
5. Check by putting a small value such as $x = 2$ into the original expression and into your answer. Avoid 0 and 1, which hide wrong exponents ($1^7 = 1^3$).

## Worked examples

<div class="example" markdown>

### Example 1: a bracket, a negative exponent and a fraction

Simplify $\dfrac{(2x^3)^4 \cdot x^{-2}}{8x^5}$, where $x \ne 0$.

Step 1: the only bracket with an exponent is $(2x^3)^4$. The exponent 4 goes onto both factors inside, the 2 and the $x^3$ (power of a product). Then $(x^3)^4 = x^{12}$ (power of a power):

$$
(2x^3)^4 = 2^4 \cdot (x^3)^4 = 16x^{12}.
$$

<div class="warning" markdown>

Watch out at Step 1: the 2 inside the bracket is raised to the power 4 as well. Writing $(2x^3)^4 = 2x^{12}$ forgets it, and so does $8x^{12}$, which multiplies 2 by 4 instead of raising it to the 4th power.

</div>

Step 2: in the numerator, $x^{12} \cdot x^{-2} = x^{12 + (-2)} = x^{10}$ (product rule). The expression is now $\dfrac{16x^{10}}{8x^5}$. The base $x$ is on the top and the bottom, so subtract: $\dfrac{x^{10}}{x^5} = x^{10-5} = x^5$ (quotient rule).

Step 3: the number parts give $\frac{16}{8} = 2$.

Step 4: every exponent is already positive, so the answer is $2x^5$.

Step 5: check with $x = 2$. The original is $\dfrac{(2 \cdot 8)^4 \cdot \frac{1}{4}}{8 \cdot 32} = \dfrac{65536 \div 4}{256} = \dfrac{16384}{256} = 64$, and the answer gives $2 \cdot 2^5 = 64$. They agree.

</div>

<div class="example" markdown>

### Example 2: different bases with the same exponent

Work out $\dfrac{6^5}{2^5 \cdot 3^3}$ without a calculator.

The bases 6, 2 and 3 are all different, so the product and quotient rules don't apply yet. Split the 6 instead, with the power of a product: $6^5 = (2 \cdot 3)^5 = 2^5 \cdot 3^5$. Now each base appears on the top and the bottom:

$$
\frac{2^5 \cdot 3^5}{2^5 \cdot 3^3} = 2^{5-5} \cdot 3^{5-3} = 2^0 \cdot 3^2 = 1 \cdot 9 = 9.
$$

Check: $6^5 = 7776$, and $2^5 \cdot 3^3 = 32 \cdot 27 = 864$, and $7776 \div 864 = 9$.

</div>

<div class="example" markdown>

### Example 3: negative exponents, signs and sums

Work out (a) $\left(\frac{2}{5}\right)^{-2}$, (b) $(-3)^{-3}$, (c) $-3^{-2}$ and (d) $2^{-1} + 2^{-2}$.

- (a) The reciprocal of $\left(\frac{2}{5}\right)^2 = \frac{4}{25}$ is $\frac{25}{4}$. A shortcut: a negative exponent on a fraction flips the fraction, so $\left(\frac{2}{5}\right)^{-2} = \left(\frac{5}{2}\right)^2 = \frac{25}{4}$.
- (b) $(-3)^{-3} = \frac{1}{(-3)^3} = \frac{1}{-27} = -\frac{1}{27}$. The base is negative and the power is odd, so the answer is negative. The minus sign in the exponent did not cause that; the minus sign in the base did.
- (c) The exponent belongs to the 3 alone, as in the last lesson: $-3^{-2} = -\frac{1}{3^2} = -\frac{1}{9}$.
- (d) No rule combines a sum of powers, so work out each one: $\frac{1}{2} + \frac{1}{4} = \frac{3}{4}$.

Check (d): $2^{-3} = \frac{1}{8}$, which is not $\frac{3}{4}$, so writing $2^{-1} + 2^{-2} = 2^{-3}$ would have been wrong.

</div>

<div class="example" markdown>

### Example 4: growth forward and back in time (finish it yourself)

A savings account grows by 5% a year, so each year multiplies the balance by 1.05 ([percent change](../02-ratios-rates-percents/04-percent-change-and-applications.md#several-changes-in-a-row)). Today it holds \$2,000. Its balance 6 years from now is $2000 \cdot 1.05^6$, and its balance 2 years ago was $2000 \cdot 1.05^{-2}$, since going back a year divides by 1.05.

By what factor does the balance grow between 2 years ago and 6 years from now? Divide the later balance by the earlier one; the 2000s cancel, which leaves $\dfrac{1.05^6}{1.05^{-2}}$. Write this as a single power and work it out to four decimal places.

<details class="solution" markdown>
<summary>Finish</summary>

The quotient rule gives $1.05^{6 - (-2)} = 1.05^8$, and $1.05^8 \approx 1.4775$. That makes sense: from 2 years ago to 6 years from now is 8 years of growth.

Check: the two balances are $2000 \cdot 1.05^6 \approx 2680.19$ and $2000 \cdot 1.05^{-2} \approx 1814.06$, and $2680.19 \div 1814.06 \approx 1.4775$.

</details>

</div>

## Edge cases and common mistakes

Forgetting to raise the number inside a bracket is flagged in Example 1. Here are the others.

<div class="warning" markdown>

Watch out: an exponent doesn't split over a sum. $(a + b)^2$ is not $a^2 + b^2$. With $a = 3$ and $b = 4$, $(3 + 4)^2 = 49$ while $3^2 + 4^2 = 25$. The power of a product rule is about $(ab)^n$, a product inside the bracket; for a sum, multiply out $(a + b)(a + b)$ instead, which gives $a^2 + 2ab + b^2$ ([polynomial arithmetic](../../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md)).

</div>

<div class="warning" markdown>

Watch out: multiplying powers adds the exponents; it doesn't multiply them. $a^m \cdot a^n$ is $a^{m+n}$, not $a^{mn}$. For example, $2^3 \cdot 2^4 = 8 \cdot 16 = 128 = 2^7$, while $2^{12} = 4096$. Multiplying the exponents is the rule for a power of a power, $(2^3)^4 = 2^{12}$. If you are unsure which, write out the factors of a small case.

</div>

<div class="warning" markdown>

Watch out: $-2^4$ is $-16$ and $(-2)^4$ is 16. The rules in this lesson apply to the base the exponent is attached to, which in $-2^4$ is 2. So $-2^4 \cdot 2^3 = -(2^4 \cdot 2^3) = -2^7 = -128$, and the minus sign comes along unchanged.

</div>

<div class="warning" markdown>

Watch out: powers with different bases and different exponents don't combine. In $2^3 \cdot 3^2$ the bases differ, so the product rule doesn't apply, and the exponents differ, so the power of a product doesn't either. Work it out instead: $8 \cdot 9 = 72$. Writing $6^5$ (multiply bases, add exponents) gives 7776, and $6^6$ is even further off. When the exponents match, the bases can combine: $2^3 \cdot 3^3 = 6^3 = 216$.

</div>

<div class="warning" markdown>

Watch out: a coefficient is not part of the base. $3 \cdot 2^4$ is $3 \cdot 16 = 48$, not $6^4 = 1296$. In the same way, $2x^{-1}$ means $2 \cdot \frac{1}{x} = \frac{2}{x}$, while $(2x)^{-1} = \frac{1}{2x}$. Only the base the exponent touches moves across the fraction bar.

</div>

Sums of powers also stay as they are: $2^3 + 2^4 = 8 + 16 = 24$, which is not $2^7$. The one exception is a sum of equal powers, which is a multiplication in disguise: $2^3 + 2^3 = 2 \cdot 2^3 = 2^4$.

A negative exponent never makes a number negative. $5^{-2} = \frac{1}{25}$, which is positive. The sign of a power depends only on the base: a positive base gives a positive power for every integer exponent.

Zero bases need care. For positive $n$, $0^n = 0$; $0^0$ is undefined in arithmetic and is 1 by convention in counting and in code; $0^{-n}$ is undefined. Expressions with letters inherit this, so $x^0 = 1$ is true only for $x \ne 0$.

## Tricks and shortcuts

Powers of 2 come up in every computing course, and $2^{10} = 1024$ is close to $10^3$. The power of a power rule turns that into quick estimates: $2^{20} = (2^{10})^2 \approx 10^6$ and $2^{30} = (2^{10})^3 \approx 10^9$. So 20 bits can hold about a million values, and 30 bits about a billion.

| Bits $n$ | Values $2^n$ | About |
|---|---|---|
| 8 | 256 | |
| 10 | 1,024 | $10^3$ |
| 16 | 65,536 | $6.6 \times 10^4$ |
| 20 | 1,048,576 | $10^6$ |
| 32 | 4,294,967,296 | $4.3 \times 10^9$ |
| 64 | 18,446,744,073,709,551,616 | $1.8 \times 10^{19}$ |

For a power that isn't a multiple of 10, split off the remainder with the product rule: $2^{32} = 2^{30} \cdot 2^2 \approx 4 \times 10^9$. The product rule also says that one more bit doubles the count, since $2^{n+1} = 2 \cdot 2^n$. This is why 32-bit IPv4 addresses, about 4.3 billion of them, ran short, and why IPv6 moved to 128 bits instead of 33 or 40: that gives $2^{128} \div 2^{32} = 2^{96}$ times as many addresses.

A negative exponent on a fraction flips it: $\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n$. So $\left(\frac{3}{4}\right)^{-2} = \frac{16}{9}$ in one step.

To move a factor across a fraction bar, change the sign of its exponent: $\dfrac{x^{-3}}{y^{-2}} = \dfrac{y^2}{x^3}$. This is the definition of a negative exponent used twice. It works for factors only, never for terms that are added: $\dfrac{1}{x^{-1} + 1}$ is not $x + 1$.

Repeated growth uses the same rules. If prices rise by a rate $r$ each year, $n$ years multiply them by $(1 + r)^n$, and the product rule splits the time: 3 years then 7 years is $(1 + r)^3 (1 + r)^7 = (1 + r)^{10}$. Going back $n$ years divides by $(1 + r)^n$, which is multiplying by $(1 + r)^{-n}$.

## In code

Python's `**` follows the rules in this lesson. With integers it gives exact answers, and a negative exponent gives a float (or an exact fraction with `Fraction`).

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction

print(2**3 * 2**4 == 2**7, (2**3)**4 == 2**12)   # True True
print(2**-3, Fraction(2, 5)**-2)                  # 0.125 25/4
print(0**0, 5**0, -2**4, (-2)**4)                 # 1 1 -16 16
print((3 + 4)**2, 3**2 + 4**2)                    # 49 25
print(2**10, 2**32, 2**128 // 2**32 == 2**96)     # 1024 4294967296 True
print(round(1.05**6 / 1.05**-2, 4))               # 1.4775
```

The third line shows the convention `0**0 == 1` and that `-2**4` is $-(2^4)$, as on paper. The fifth line uses `//`, integer division, so the comparison stays exact; Python's integers have no size limit, which is why `2**128` causes no trouble. Asking for `0**-1` raises a `ZeroDivisionError`, since it would be $\frac{1}{0}$.

</details>

## FAQ

### Why isn't a to the power 0 equal to 0?

Because the exponent counts factors, not the size of the result. Zero factors of $a$ means nothing has been multiplied in yet, and the starting point for multiplying is 1, in the same way that a sum with no terms is 0 and a product with no terms is 1 ([symbols and notation](../../reference/symbols-and-notation.md#sums-and-products)). The quotient rule forces the same answer: $\frac{a^3}{a^3}$ is 1, and the rule says it is $a^0$.

### Is a power of a power the same as a stacked power?

No. Brackets on the left mean the power of a power, $(2^3)^2 = 8^2 = 64 = 2^6$. Without brackets, a stacked power is worked from the top down, as in the last lesson: $2^{3^2} = 2^9 = 512$. The two agree only in special cases, so write the brackets you mean.

### What about exponents that are fractions, such as 2 to the power one half?

The rules decide that too. If $2^{1/2}$ is to obey the power of a power rule, then $(2^{1/2})^2 = 2^1 = 2$, so $2^{1/2}$ has to be a number whose square is 2, which is $\sqrt{2}$. Square roots come in [roots, irrational numbers and types of numbers](03-roots-irrationals-and-types-of-numbers.md), and fractional exponents in general in [radicals and rational exponents](../../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md).

### Do the rules work for negative bases?

Yes, for every integer exponent, as long as the base is not 0: $(-2)^3 \cdot (-2)^2 = (-8)(4) = -32 = (-2)^5$. Keep the brackets around a negative base on every line, since $(-2)^5$ and $-2^5$ happen to agree but $(-2)^4$ and $-2^4$ don't. With fractional exponents, negative bases cause real trouble, which the radicals lesson takes up.

## Practice

### Warm-up

1\. Write each as a single power: (a) $3^4 \cdot 3^5$, (b) $\dfrac{10^7}{10^3}$, (c) $(5^2)^3$, (d) $2^3 \cdot 2^{-5}$, (e) $\dfrac{x^2}{x^6}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Same base, multiplying: add the exponents, $3^{4+5} = 3^9$.
- (b) Same base, dividing: subtract, $10^{7-3} = 10^4$.
- (c) Power of a power: multiply, $5^{2 \cdot 3} = 5^6$.
- (d) Add the exponents: $2^{3 + (-5)} = 2^{-2}$, which is $\frac{1}{4}$.
- (e) Subtract: $x^{2-6} = x^{-4}$, or $\frac{1}{x^4}$.

Check (d) with factors: $8 \cdot \frac{1}{32} = \frac{8}{32} = \frac{1}{4}$, and $2^{-2} = \frac{1}{4}$.

</details>

2\. Work out (a) $7^0$, (b) $10^{-3}$, (c) $2^{-5}$, (d) $\left(\frac{1}{3}\right)^{-2}$, (e) $-4^0$ and (f) $(-4)^{-1}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Every nonzero number to the power 0 is 1.
- (b) $\frac{1}{10^3} = \frac{1}{1000} = 0.001$.
- (c) $\frac{1}{2^5} = \frac{1}{32}$.
- (d) Flip the fraction: $3^2 = 9$.
- (e) The exponent belongs to the 4, so $-(4^0) = -1$.
- (f) $\frac{1}{-4} = -\frac{1}{4}$.

Check (d) from the definition: $\left(\frac{1}{3}\right)^{-2} = \frac{1}{(1/3)^2} = \frac{1}{1/9} = 9$.

</details>

3\. True or false? Give a reason or a counterexample. (a) $2^3 \cdot 2^4 = 4^7$. (b) $(x^2)^3 = x^5$. (c) $(2x)^3 = 8x^3$. (d) $3^2 + 3^2 + 3^2 = 3^3$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) False. The base stays 2: $2^3 \cdot 2^4 = 2^7 = 128$, while $4^7 = 16{,}384$.
- (b) False. A power of a power multiplies the exponents, so $(x^2)^3 = x^6$. At $x = 2$, $(2^2)^3 = 64$ and $2^5 = 32$.
- (c) True, by the power of a product: $2^3 x^3 = 8x^3$.
- (d) True. Three equal terms are $3 \cdot 3^2 = 3^1 \cdot 3^2 = 3^3$. Check: $9 + 9 + 9 = 27$.

</details>

### Standard

4\. Simplify, writing answers with positive exponents only. Assume no letter is 0. (a) $(4a^2 b^3)(-3ab^5)$, (b) $(-2x^3 y)^4$, (c) $\dfrac{15m^4 n^{-2}}{5m^6 n}$, (d) $\left(\dfrac{x^2}{3y}\right)^{-3}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Multiply the numbers, $4 \cdot (-3) = -12$, then add exponents base by base ($a$ alone is $a^1$): $-12a^{2+1} b^{3+5} = -12a^3 b^8$.

(b) Every factor in the bracket gets the 4: $(-2)^4 (x^3)^4 y^4 = 16x^{12} y^4$. The power is even, so the sign is positive.

(c) Numbers: $\frac{15}{5} = 3$. Then $m^{4-6} = m^{-2}$ and $n^{-2-1} = n^{-3}$. Moving both negative powers below the bar gives $\dfrac{3}{m^2 n^3}$.

(d) Flip the fraction first: $\left(\dfrac{3y}{x^2}\right)^3 = \dfrac{3^3 y^3}{(x^2)^3} = \dfrac{27y^3}{x^6}$.

Check (c) with $m = 2$ and $n = 2$: the original is $\frac{15 \cdot 16 \cdot \frac{1}{4}}{5 \cdot 64 \cdot 2} = \frac{60}{640} = \frac{3}{32}$, and the answer is $\frac{3}{4 \cdot 8} = \frac{3}{32}$.

</details>

5\. (a) How many different values can 16 bits hold? (b) How many times as many values can 32 bits hold as 16 bits? Answer as a power of 2 and as a number. (c) Estimate $2^{40}$ as a power of ten, using $2^{10} \approx 10^3$, and compare with the exact value 1,099,511,627,776.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Each bit doubles the count, so $2^{16} = 65{,}536$ values.

(b) Divide: $\frac{2^{32}}{2^{16}} = 2^{16} = 65{,}536$ times as many. Doubling the number of bits squares the number of values, since $2^{32} = (2^{16})^2$.

(c) $2^{40} = (2^{10})^4 \approx (10^3)^4 = 10^{12}$. The exact value is about $1.0995 \times 10^{12}$, so the estimate is about 9% low, because each of the four factors 1024 is 2.4% bigger than 1000 and the errors multiply.

Check (c): $1.024^4 \approx 1.0995$.

</details>

6\. Prices rise 2.5% a year. (a) Write the factor by which prices rise over 4 years followed by 6 more years as a single power, and work it out to four decimal places. (b) An item costs \$40 today. What did it cost 3 years ago, to the cent?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Each year multiplies prices by 1.025, so the factor is $1.025^4 \cdot 1.025^6 = 1.025^{10} \approx 1.2801$. Prices rise about 28%, not 25%, because each year's rise is taken on a bigger price.

(b) Going back 3 years divides by $1.025^3$: $40 \cdot 1.025^{-3} = \frac{40}{1.025^3} = \frac{40}{1.076890625} \approx 37.144$, so about \$37.14.

Check (b) forwards: $37.144 \cdot 1.025^3 \approx 40.00$.

</details>

### Challenge

7\. The proofs in this lesson used positive exponents. Show that the product rule also holds when one exponent is negative: for $a \ne 0$ and positive integers $m$ and $k$ with $m > k$, prove that $a^m \cdot a^{-k} = a^{m-k}$. Then check it with $a = 3$, $m = 5$ and $k = 2$.

<details class="solution" markdown>
<summary>Solution</summary>

We know the definition $a^{-k} = \frac{1}{a^k}$ and the quotient rule for positive exponents with the top one bigger. We want $a^m \cdot a^{-k} = a^{m + (-k)} = a^{m-k}$. The plan is to replace the negative power by its definition and turn the product into a quotient.

*Proof.* By the definition of a negative exponent,

$$
a^m \cdot a^{-k} = a^m \cdot \frac{1}{a^k} = \frac{a^m}{a^k}.
$$

Here $m$ and $k$ are positive integers with $m > k$, so the quotient rule proved by cancelling factors applies, and $\frac{a^m}{a^k} = a^{m-k}$.

Look back: the cases $m = k$ and $m < k$ work the same way, using $a^0 = 1$ and the reciprocal definition. Check: $3^5 \cdot 3^{-2} = 243 \cdot \frac{1}{9} = 27$, and $3^{5-2} = 3^3 = 27$.

</details>

8\. This one reviews [rational number arithmetic](../01-integers-and-rational-numbers/03-rational-number-arithmetic.md). Work out $\dfrac{2^{-1} + 3^{-1}}{6^{-1}}$. Then explain what is wrong with writing the numerator as $5^{-1}$.

<details class="solution" markdown>
<summary>Solution</summary>

Write each negative power as a fraction: the numerator is $\frac{1}{2} + \frac{1}{3}$. Over the common denominator 6, that is $\frac{3}{6} + \frac{2}{6} = \frac{5}{6}$. The denominator is $6^{-1} = \frac{1}{6}$. Dividing by $\frac{1}{6}$ is multiplying by 6, so the value is $\frac{5}{6} \cdot 6 = 5$.

Writing $2^{-1} + 3^{-1} = 5^{-1}$ adds the bases, which no rule allows. It would claim $\frac{1}{2} + \frac{1}{3} = \frac{1}{5}$, the "add the denominators" mistake from [adding and subtracting fractions](../../01-elementary/10-adding-and-subtracting-fractions.md). The sum $\frac{5}{6}$ is bigger than $\frac{1}{2}$, while $\frac{1}{5}$ is smaller, so the size check catches it.

Check: $(0.5 + 0.3333) \div 0.16667 \approx 5.0$.

</details>

## Where this shows up

- [Scientific notation](02-scientific-notation.md) multiplies and divides huge and tiny numbers with the product and quotient rules for base 10. Fractional exponents and roots follow in [roots, irrational numbers and types of numbers](03-roots-irrationals-and-types-of-numbers.md) and [radicals and rational exponents](../../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md), and the [logarithm properties](../../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md) are these rules read backwards.
- In CS, $2^n$ counts what $n$ bits can hold ([bits and information](../../06-cs-math/01-number-representation/02-bits-and-information.md)), and algorithm analysis uses facts such as $2^{n+1} = 2 \cdot 2^n$ and $4^n = (2^n)^2$ all the time ([asymptotic notation](../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md)).
- In finance, $(1 + r)^n$ moves money forward $n$ periods and $(1 + r)^{-n}$ moves it back, which is the whole idea of compound interest<!-- link: ../../08-financial-math/02-interest-and-growth/02-compound-interest.md --> and present and future value<!-- link: ../../08-financial-math/03-time-value-of-money/01-present-and-future-value.md -->.
