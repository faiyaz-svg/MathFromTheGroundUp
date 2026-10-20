# Factoring polynomials

After this lesson you can factor a polynomial completely over the integers (common factors, grouping, trinomials, differences of squares, sums and differences of cubes), check the result by expanding, solve polynomial equations with the zero-product property, and recognize a polynomial that doesn't factor.

Before this: [polynomial arithmetic](02-polynomial-arithmetic.md) and [factoring out the GCF](../../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#factoring-out-the-gcf).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Factor $6x^2 - 15x$.
2. Factor $x^2 + 5x - 24$.
3. Solve $x^2 = 7x - 12$.

<details class="solution" markdown>
<summary>Answers</summary>

1. $3x(2x - 5)$. The GCF of $6x^2$ and $15x$ is $3x$, and expanding gives back $6x^2 - 15x$.
2. $(x - 3)(x + 8)$. You need two numbers with product $-24$ and sum $5$, and $-3$ and $8$ work.
3. $x = 3$ or $x = 4$. Move everything to one side: $x^2 - 7x + 12 = 0$, which factors as $(x - 3)(x - 4) = 0$. A product is zero only if a factor is zero.

</details>

## The idea

A rectangular patio has an area of $x^2 + 7x + 12$ square metres, and you want to know what its side lengths could be. The garden picture from [polynomial arithmetic](02-polynomial-arithmetic.md#the-idea) runs backwards. An $x$ by $x$ square, plus some strips that are $x$ wide, plus a block of unit squares: if the strips are $3$ and $4$ long, the unit block is $3 \times 4 = 12$ squares, and the whole thing is a rectangle with sides $x + 3$ and $x + 4$. Check: $(x + 3)(x + 4) = x^2 + 4x + 3x + 12 = x^2 + 7x + 12$.

Factoring is expanding in reverse. Expanding a product is a mechanical job, because the distributive property tells you every step. Factoring is a search: you have to find the factors. The special products and a few patterns tell you where to look, and the final check, expanding, always tells you whether you found them.

The reason to look is that a factored form shows something an expanded form hides. The polynomial $x^2 - 7x + 12$ doesn't show when it is zero. The factored form $(x - 3)(x - 4)$ does, since a product of numbers is zero only when one of the numbers is zero, and that happens at $x = 3$ and at $x = 4$. Finding where a polynomial is zero, which is solving an equation, is the main use of factoring. It is also how you find the zeros of a polynomial to draw its graph, and how you cancel common factors in a fraction.

## Definitions

To **factor** a polynomial is to write it as a product of polynomials of lower degree (or of a number and a polynomial), and each polynomial in the product is a **factor**. We usually factor over the integers, which means that every factor must have integer coefficients. So $x^2 - 9 = (x - 3)(x + 3)$ is a factorization, while $x^2 - 2 = (x - \sqrt{2})(x + \sqrt{2})$ is not one over the integers, since $\sqrt{2}$ is not an integer.

A polynomial is **prime over the integers** if it has degree at least 1, its coefficients have no common factor other than $1$ and $-1$, and it can't be written as a product of two polynomials of lower positive degree with integer coefficients. For example, $x + 3$, $x^2 + 4$ and $x^2 - 2$ are prime over the integers. A polynomial is **factored completely** over the integers when it is written as an integer times a product of polynomials that are prime over the integers.

In plain words, you are done factoring when no factor can be split again and no number is left that every term shares. The polynomial $2x^2 - 8 = 2(x^2 - 4)$ is not done, because $x^2 - 4$ splits again. It is done as $2(x - 2)(x + 2)$. Which polynomials count as prime depends on the number system. Over the real numbers, $x^2 - 2$ splits and $x^2 + 4$ doesn't, and over the [complex numbers](../05-quadratics-and-complex-numbers/03-complex-numbers.md) every polynomial of degree 2 or more splits.

### Zero-product property

The property that makes factoring useful for solving equations is this theorem.

*Theorem (zero-product property).* If $a$ and $b$ are real numbers and $ab = 0$, then $a = 0$ or $b = 0$.

We know the properties of arithmetic: every nonzero number has a reciprocal, and every number times 0 is 0. We want to show that at least one of $a$ and $b$ is 0. The plan is to assume that the first one isn't 0, and show that the second one must be.

*Proof.* Suppose $ab = 0$ and $a \ne 0$. Multiply both sides by $\frac{1}{a}$, which exists because $a \ne 0$:

$$
\frac{1}{a}(ab) = \frac{1}{a} \cdot 0 = 0.
$$

By the associative property, the left side is $\left(\frac{1}{a} \cdot a\right) b = 1 \cdot b = b$. So $b = 0$. $\blacksquare$

Look back: the proof used a reciprocal, so it needs a number system where nonzero numbers can be divided. It can fail elsewhere. In arithmetic mod 6, $2 \cdot 3 = 6 \equiv 0$ although neither factor is 0 (divisibility and modular arithmetic<!-- link: ../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->). The theorem extends to any number of factors: a product of real numbers is zero if and only if at least one factor is zero. Taking the other side, a product of nonzero numbers is never zero, which is the fact that [polynomial arithmetic](02-polynomial-arithmetic.md#definitions) used to show that the leading coefficient of a product can't vanish.

### The factoring identities

These are the special products from [polynomial arithmetic](02-polynomial-arithmetic.md#definitions), read from right to left, with the two cube identities added. They hold for all numbers and expressions $a$ and $b$.

| Name | Identity | Example |
|---|---|---|
| difference of squares | $a^2 - b^2 = (a - b)(a + b)$ | $x^2 - 49 = (x - 7)(x + 7)$ |
| perfect-square trinomial | $a^2 + 2ab + b^2 = (a + b)^2$ | $x^2 + 10x + 25 = (x + 5)^2$ |
| perfect-square trinomial | $a^2 - 2ab + b^2 = (a - b)^2$ | $4x^2 - 12x + 9 = (2x - 3)^2$ |
| sum of cubes | $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$ | $x^3 + 27 = (x + 3)(x^2 - 3x + 9)$ |
| difference of cubes | $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$ | $8x^3 - 125 = (2x - 5)(4x^2 + 10x + 25)$ |

In plain words, a difference of two squares splits into the difference and the sum of the two roots. A trinomial whose first and last terms are squares and whose middle term is twice the product of their roots is itself a square. A sum or a difference of cubes splits into a binomial and a trinomial. The signs in the cube formulas follow a pattern: the binomial has the same sign as the original, the trinomial's middle sign is the opposite, and its last sign is always plus.

The cube identities are checked by expanding the right side. For the sum of cubes:

$$
(a + b)(a^2 - ab + b^2) = a^3 - a^2b + ab^2 + a^2b - ab^2 + b^3 = a^3 + b^3,
$$

because the four middle terms cancel in pairs. Replacing $b$ by $-b$ gives the difference of cubes. A sum of squares, $a^2 + b^2$, has no such identity: it is prime over the reals.

The difference of squares also has a picture proof. A square of side $a$ with a $b$ by $b$ corner cut out has area $a^2 - b^2$. The remaining L-shape is two rectangles, $A$ and $B$. Turn $B$ on its side and move it next to $A$, and the two pieces form one rectangle with sides $a + b$ and $a - b$:

![On the left, a square of side a with a b by b corner removed, leaving a rectangle A of width a and height a minus b below a rectangle B of width a minus b and height b. On the right, B turned on its side and placed beside A, making one rectangle of width a plus b and height a minus b.](../../assets/figures/03-high-school/factoring-polynomials-difference-of-squares.svg)

The picture works for positive $a > b$. The algebra, $(a - b)(a + b) = a^2 - ab + ba - b^2 = a^2 - b^2$, works for all numbers.

## How to do it

### The factoring checklist

Work through these steps in order, every time.

1. Take out the greatest common factor of all the terms. If the leading coefficient is negative, take out its negative as well, so the polynomial inside the brackets starts with a positive term.
2. Count the terms of what is left. With two terms, look for a difference of squares, a sum of cubes or a difference of cubes. With three terms, check for a perfect-square trinomial, and otherwise use one of the trinomial methods below. With four terms, try grouping.
3. Factor each factor again. A difference of squares can contain another difference of squares, as in $x^4 - 16$. Stop only when every factor is prime.
4. Check by expanding the factors. You must get the original polynomial back. A quick second check is to put in $x = 2$ and compare the two values.

If no step works, the polynomial may be prime over the integers.

### Trinomials with leading coefficient 1

To factor $x^2 + bx + c$, look for integers $r$ and $s$ with product $c$ and sum $b$, and then write $(x + r)(x + s)$. The reason comes from expanding:

$$
(x + r)(x + s) = x^2 + (r + s)x + rs,
$$

so the middle coefficient is the sum $r + s$ and the constant term is the product $rs$.

1. List the pairs of integers whose product is $c$. The signs follow from $c$ and $b$:

| If the constant $c$ is | then $r$ and $s$ | so |
|---|---|---|
| positive | have the same sign, the sign of $b$ | their sizes add up to $\lvert b \rvert$ |
| negative | have opposite signs | the one with the bigger size has the sign of $b$, and the sizes differ by $\lvert b \rvert$ |

2. Find the pair whose sum is $b$.
3. Write $(x + r)(x + s)$ and expand to check.

For example, in $x^2 - 3x - 28$ the constant is negative, so the signs are opposite, and the bigger number is negative because $b = -3$. The pairs with product 28 are $1, 28$ and $2, 14$ and $4, 7$, and the sizes must differ by 3, which is $4$ and $7$. So $r = -7$ and $s = 4$, and $x^2 - 3x - 28 = (x - 7)(x + 4)$.

### Trinomials with leading coefficient other than 1: the ac method

For $ax^2 + bx + c$ with $a \ne 1$, look for integers $m$ and $n$ with $mn = ac$ and $m + n = b$.

1. Take out any common factor, then multiply $a$ and $c$.
2. Find integers $m$ and $n$ with product $ac$ and sum $b$.
3. Split the middle term: $ax^2 + mx + nx + c$.
4. Factor the first two terms and the last two terms separately, taking out the GCF of each pair. The brackets that remain must match.
5. Take out the matching bracket, and check by expanding.

The reason it works is the expansion of $(px + q)(rx + s) = prx^2 + (ps + qr)x + qs$. The two middle pieces $ps$ and $qr$ add to $b$, and they multiply to $pqrs$, which is the product of the first and last coefficients, $ac$. So $m$ and $n$ are exactly $ps$ and $qr$, and the grouping in Step 4 recovers the two factors. If no integer pair $m, n$ has the right product and sum, the trinomial is prime over the integers.

### Factoring by grouping

A four-term polynomial sometimes splits into two pairs that share a bracket.

1. Group the terms in pairs.
2. Take out the GCF of each pair, and watch the signs: for a pair like $-9x - 18$, take out $-9$.
3. If the same bracket appears in both pairs, take it out as a common factor. If the brackets don't match, change the order of the terms, or change the sign you took out.
4. Factor what remains, and check by expanding.

For example, $x^3 + 2x^2 - 9x - 18$ groups as $x^2(x + 2) - 9(x + 2)$, so it is $(x + 2)(x^2 - 9) = (x + 2)(x - 3)(x + 3)$.

### Solving a polynomial equation by factoring

1. Move every term to one side, so that the other side is 0. The zero-product property needs a product equal to 0, and no other number works.
2. Factor the polynomial completely.
3. Set each factor equal to 0.
4. Solve each of the simple equations. The solutions are the zeros, or roots, of the polynomial.
5. Check each solution in the original equation.

## Worked examples

<div class="example" markdown>

### Example 1: a full factoring, using the checklist

Factor $2x^4 - 32$ completely.

Step 1: both terms have the common factor 2, so $2x^4 - 32 = 2(x^4 - 16)$.

Step 2: what is left has two terms. Since $x^4 = (x^2)^2$ and $16 = 4^2$, it is a difference of squares with $a = x^2$ and $b = 4$:

$$
2(x^4 - 16) = 2(x^2 - 4)(x^2 + 4).
$$

<div class="warning" markdown>

Watch out at Step 3: stopping here is the common slip. The factor $x^2 - 4$ is itself a difference of squares, so the factoring isn't complete.

</div>

Step 3: factor each factor again. The first is $x^2 - 4 = (x - 2)(x + 2)$. The second, $x^2 + 4$, is a sum of squares, which is prime. So

$$
2x^4 - 32 = 2(x - 2)(x + 2)(x^2 + 4).
$$

Step 4: check by expanding. First $(x - 2)(x + 2) = x^2 - 4$. Then $(x^2 - 4)(x^2 + 4) = x^4 - 16$, and the factor 2 gives $2x^4 - 32$. As a second check, put in $x = 3$: the original is $2 \cdot 81 - 32 = 130$, and the factors give $2 \cdot 1 \cdot 5 \cdot 13 = 130$.

</div>

<div class="example" markdown>

### Example 2: the ac method

Factor $6x^2 + 7x - 3$.

Step 1: there is no common factor, and $ac = 6 \cdot (-3) = -18$.

Step 2: we need integers $m$ and $n$ with product $-18$ and sum $7$. The product is negative, so they have opposite signs, and the bigger one is positive because $7 > 0$. The pairs with product 18 are $1, 18$ and $2, 9$ and $3, 6$, and the sizes must differ by 7, which is $9$ and $2$. So $m = 9$ and $n = -2$.

Step 3: split the middle term, $6x^2 + 9x - 2x - 3$.

Step 4: take the GCF out of each pair: $3x(2x + 3) - 1(2x + 3)$. Both brackets are $2x + 3$, so they match.

Step 5: the common bracket comes out, and we get $(2x + 3)(3x - 1)$.

Check by expanding: $(2x + 3)(3x - 1) = 6x^2 - 2x + 9x - 3 = 6x^2 + 7x - 3$. The check also catches a wrong order: $(2x - 3)(3x + 1)$ gives the middle term $-7x$.

</div>

<div class="example" markdown>

### Example 3: grouping, and zero on one side

Solve $x^3 - 4x^2 = 9x - 36$.

First, zero on one side. Move the right side over: $x^3 - 4x^2 - 9x + 36 = 0$. Four terms, so try grouping: $x^2(x - 4) - 9(x - 4) = 0$. The brackets match, so $(x - 4)(x^2 - 9) = 0$, and $x^2 - 9$ is a difference of squares:

$$
(x - 4)(x - 3)(x + 3) = 0.
$$

By the zero-product property, $x - 4 = 0$, $x - 3 = 0$ or $x + 3 = 0$, so $x = 4$, $x = 3$ or $x = -3$.

Check each in the original equation. At $x = 4$ both sides are 0. At $x = 3$ the left side is $27 - 36 = -9$ and the right side is $27 - 36 = -9$. At $x = -3$ the left side is $-27 - 36 = -63$ and the right side is $-27 - 36 = -63$.

<div class="warning" markdown>

Watch out: it is tempting to divide both sides of $x^3 - 4x^2 = 9x - 36$ by $x - 4$ to "cancel" a factor. That divides by 0 when $x = 4$ and loses that solution. Move everything to one side and factor instead.

</div>

</div>

<div class="example" markdown>

### Example 4: an untidy answer (finish it yourself)

Solve $2x^2 = 5x + 12$.

Step 1: move everything to one side: $2x^2 - 5x - 12 = 0$. Step 2: here $ac = -24$ and $b = -5$, so we need $m + n = -5$ and $mn = -24$. The numbers $-8$ and $3$ work. Split the middle term: $2x^2 - 8x + 3x - 12 = 0$.

Now group, factor, apply the zero-product property, and check both solutions.

<details class="solution" markdown>
<summary>Finish</summary>

Group: $2x(x - 4) + 3(x - 4) = 0$, which is $(x - 4)(2x + 3) = 0$. So $x - 4 = 0$ or $2x + 3 = 0$, giving $x = 4$ or $x = -\frac{3}{2}$. A fraction is a fine solution.

Check: at $x = 4$, $2 \cdot 16 = 32$ and $5 \cdot 4 + 12 = 32$. At $x = -\frac{3}{2}$, $2 \cdot \frac{9}{4} = \frac{9}{2}$ and $5 \cdot \left(-\frac{3}{2}\right) + 12 = -\frac{15}{2} + 12 = \frac{9}{2}$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a sum of squares doesn't factor over the real numbers. The expression $x^2 + 9$ is not $(x + 3)^2$, since $(x + 3)^2 = x^2 + 6x + 9$ has a middle term. It also has no real zeros, because $x^2 + 9 \ge 9$ for every real $x$, and a real factor $(x - c)$ would give a zero at $x = c$. The difference of squares is different: $x^2 - 9$ factors because the minus sign makes the middle terms cancel.

</div>

<div class="warning" markdown>

Watch out for the zero-product trap. For $x(x - 3) = 10$, it is wrong to say "$x = 10$ or $x - 3 = 10$". A product equal to 10 doesn't force either factor to be 10: $2 \cdot 5$, $1 \cdot 10$ and $0.5 \cdot 20$ all work. Move the 10 over, and factor $x^2 - 3x - 10 = (x - 5)(x + 2) = 0$, which gives $x = 5$ or $x = -2$. Check $x = 5$: $5 \cdot 2 = 10$. Check $x = -2$: $-2 \cdot (-5) = 10$.

</div>

<div class="warning" markdown>

Watch out: dividing both sides by a variable loses a solution. From $x^2 = 5x$, dividing by $x$ gives only $x = 5$. But $x^2 - 5x = x(x - 5) = 0$ gives $x = 0$ and $x = 5$, and $0$ really is a solution: $0^2 = 5 \cdot 0$.

</div>

<div class="warning" markdown>

Watch out when factoring a perfect-square trinomial. The middle term has to be twice the product of the two roots. The trinomial $x^2 + 6x + 9$ is $(x + 3)^2$, since $2 \cdot 3 = 6$. But $x^2 + 6x + 10$ is not a square, and $x^2 + 9x + 9$ isn't either; try them in the trinomial method instead.

</div>

Not factoring completely is the most common reason for a lost mark. After each step, ask whether any factor is a difference of squares, a difference or sum of cubes, or has a common factor left. The second factor in a sum or difference of cubes doesn't split further over the integers: $x^2 - 3x + 9$ has $b^2 - 4ac = 9 - 36 < 0$.

Don't write $(x + 3)^3$ for $x^3 + 27$. The expansion $(x + 3)^3 = x^3 + 9x^2 + 27x + 27$ has two middle terms that the sum of cubes doesn't.

A leading negative coefficient is handled by taking out $-1$: $-x^2 + 5x - 6 = -(x^2 - 5x + 6) = -(x - 2)(x - 3)$. Different-looking answers can agree, since $(2 - x)(3 - x) = (x - 2)(x - 3)$, because two sign changes cancel.

Some polynomials don't factor over the integers: $x^2 + x + 1$ and $x^2 - 2$ are prime. Finding no pair $r, s$ is not a failure of the method, and it tells you something true about the polynomial. The next trick tests for it without searching.

## Tricks and shortcuts

A quadratic $ax^2 + bx + c$ with integer coefficients factors over the integers exactly when $b^2 - 4ac$ is a perfect square (0, 1, 4, 9, 16, and so on). The quantity $b^2 - 4ac$ is the discriminant, which [the quadratic formula](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md) in the next chapter explains. For $6x^2 + 7x - 3$, $7^2 + 72 = 121 = 11^2$, so it factors. For $x^2 + x + 1$, $1 - 4 = -3$ is not a square, and for $x^2 - 2$, $0 + 8 = 8$ is not a square, so neither factors.

Compare values at $x = 1$ to check a factoring in seconds. The value of a polynomial at $x = 1$ is the sum of its coefficients, and it has to equal the product of the factors' values at $x = 1$. For $6x^2 + 7x - 3 = (2x + 3)(3x - 1)$: $6 + 7 - 3 = 10$ and $5 \cdot 2 = 10$.

A difference of squares can factor whole numbers. Since $899 = 900 - 1 = 30^2 - 1^2$, we get $899 = 29 \cdot 31$. And $8051 = 8100 - 49 = 90^2 - 7^2 = 83 \cdot 97$. This idea, looking for $N = a^2 - b^2$, is Fermat's factoring method, which works best when the two factors are close together.

When $a$ and $c$ are big, list only the pairs that could give the right sign and size. To factor $x^2 + bx + c$ with $c > 0$, you only need pairs whose sum has size $\lvert b \rvert$, so the pair is found as soon as you see it.

## In code

A short loop does the pair search for $x^2 + bx + c$, and the library SymPy factors any polynomial and shows what "prime over a number system" means. SymPy comes with the scientific Python distributions, or install it with `pip install sympy`.

<details class="code" markdown>
<summary>In code</summary>

```python
def find_pair(b, c):
    """Integers r, s with r * s == c and r + s == b, or None."""
    for r in range(-abs(c), abs(c) + 1):
        if r != 0 and c % r == 0:
            s = c // r
            if r + s == b:
                return (r, s)
    return None

print(find_pair(5, -24))    # (-3, 8), so x^2 + 5x - 24 = (x - 3)(x + 8)
print(find_pair(-7, 12))    # (-4, -3), so x^2 - 7x + 12 = (x - 4)(x - 3)
print(find_pair(1, 1))      # None, so x^2 + x + 1 has no integer factors

from sympy import symbols, factor, expand, sqrt, I

x = symbols("x")
print(factor(2 * x**4 - 32))                 # 2*(x - 2)*(x + 2)*(x**2 + 4)
print(factor(x**2 + 9))                      # x**2 + 9
print(factor(x**2 + 9, extension=I))         # (x - 3*I)*(x + 3*I)
print(factor(x**2 - 2))                      # x**2 - 2
print(factor(x**2 - 2, extension=sqrt(2)))   # (x - sqrt(2))*(x + sqrt(2))
print(expand((x - 2) * (x + 2) * (x**2 + 4)) == x**4 - 16)   # True
```

The function `find_pair` tries every divisor $r$ of $c$ and keeps the one with the right sum. It returns `None` when no integer pair exists, which means the trinomial is prime over the integers. In the SymPy lines, `factor` works over the integers by default, so it leaves $x^2 + 9$ and $x^2 - 2$ alone. Asking for an extension of the number system, the complex numbers with `I` or the real numbers that include $\sqrt{2}$, lets them split. The last line is the check from Example 1, done by `expand`.

</details>

## FAQ

### Why can't $x^2 + 9$ be factored?

Over the real numbers, a factorization would give a real zero, and $x^2 + 9$ is at least 9 for every real $x$. Over the complex numbers it does factor, as $(x - 3i)(x + 3i)$, where $i^2 = -1$ ([complex numbers](../05-quadratics-and-complex-numbers/03-complex-numbers.md)). So "doesn't factor" always means "doesn't factor over this number system". Over the integers, which is what this lesson uses, the answer is also no.

### Why does the zero-product property need the zero?

Because zero is the only number with that behaviour. Many different pairs multiply to 10, so $ab = 10$ says almost nothing about $a$ or $b$. But if $ab = 0$, the proof above shows that one of them is 0. That is why the first step of solving by factoring is to get 0 on one side.

### Is the factorization unique?

Up to order and constants, yes. The polynomial $x^2 - 5x + 6$ can be written $(x - 2)(x - 3)$, or $(x - 3)(x - 2)$, or $(2 - x)(3 - x)$, or $(2x - 4)\left(\frac{1}{2}x - \frac{3}{2}\right)$, but these differ only in order and in constants moved around. With whole-number factors that are prime, the factorization is unique, in the same way that every whole number has one prime factorization ([factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md)). The proof for polynomials is in a university algebra course.

### What do I do if a polynomial won't factor, but I need its zeros?

Use another method. For a quadratic, the quadratic formula gives the zeros even when the polynomial doesn't factor over the integers ([solving quadratic equations](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md)). For higher degrees, [the rational root theorem](04-polynomial-division-and-remainder-theorem.md#the-rational-root-theorem) finds the rational zeros, and numerical methods find the others.

## Practice

### Warm-up

1\. Factor out the GCF: (a) $12x^3 - 18x^2$, (b) $4x^2y - 10xy^2$ and (c) $-6x^2 + 9x$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The GCF of 12 and 18 is 6, and the smallest power of $x$ is $x^2$: $6x^2(2x - 3)$.
- (b) The GCF is $2xy$: $2xy(2x - 5y)$.
- (c) The leading coefficient is negative, so take out $-3x$: $-3x(2x - 3)$.

Check by expanding: $6x^2 \cdot 2x = 12x^3$ and $6x^2 \cdot (-3) = -18x^2$; $2xy \cdot 2x = 4x^2y$ and $2xy \cdot (-5y) = -10xy^2$; $-3x \cdot 2x = -6x^2$ and $-3x \cdot (-3) = 9x$.

</details>

2\. Factor (a) $x^2 + 9x + 20$, (b) $x^2 - 3x - 28$ and (c) $x^2 - 10x + 25$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Product 20 and sum 9: $4$ and $5$. So $(x + 4)(x + 5)$.
- (b) Product $-28$ and sum $-3$: $-7$ and $4$. So $(x - 7)(x + 4)$.
- (c) Product 25 and sum $-10$: $-5$ and $-5$. So $(x - 5)^2$, a perfect-square trinomial.

Check: (a) $x^2 + 5x + 4x + 20$. (b) $x^2 + 4x - 7x - 28$. (c) $x^2 - 5x - 5x + 25$. Each middle term combines to the original.

</details>

3\. Factor (a) $49x^2 - 16$, (b) $9x^2 + 30x + 25$ and (c) $x^2 + 16$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) A difference of squares, $(7x)^2 - 4^2$: $(7x - 4)(7x + 4)$.
- (b) The first and last terms are $(3x)^2$ and $5^2$, and the middle term is $2 \cdot 3x \cdot 5 = 30x$, so it is $(3x + 5)^2$.
- (c) A sum of squares, which is prime: it can't be factored over the integers or the real numbers.

Check: $(7x - 4)(7x + 4) = 49x^2 - 28x + 28x - 16$. And $(3x + 5)^2 = 9x^2 + 30x + 25$. For (c), $x^2 + 16 \ge 16$ has no real zero, so there is no real factor.

</details>

### Standard

4\. Factor (a) $2x^2 + 11x + 12$, (b) $6x^2 - x - 12$ and (c) $5x^2 + x - 4$ with the ac method.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $ac = 24$ and $b = 11$, so $m = 3$ and $n = 8$. Then $2x^2 + 3x + 8x + 12 = x(2x + 3) + 4(2x + 3) = (2x + 3)(x + 4)$.

(b) $ac = -72$ and $b = -1$, so $m = -9$ and $n = 8$. Then $6x^2 - 9x + 8x - 12 = 3x(2x - 3) + 4(2x - 3) = (2x - 3)(3x + 4)$.

(c) $ac = -20$ and $b = 1$, so $m = 5$ and $n = -4$. Then $5x^2 + 5x - 4x - 4 = 5x(x + 1) - 4(x + 1) = (x + 1)(5x - 4)$.

Check by expanding: (a) $2x^2 + 8x + 3x + 12$, (b) $6x^2 + 8x - 9x - 12$, (c) $5x^2 - 4x + 5x - 4$. The middle terms are $11x$, $-x$ and $x$, as required.

</details>

5\. Factor completely: (a) $x^3 - 8$, (b) $27x^3 + 64$, (c) $3x^4 - 48$ and (d) $x^3 + 3x^2 - 4x - 12$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) A difference of cubes with $a = x$ and $b = 2$: $(x - 2)(x^2 + 2x + 4)$.
- (b) A sum of cubes with $a = 3x$ and $b = 4$: $(3x + 4)(9x^2 - 12x + 16)$.
- (c) Take out 3, then use differences of squares twice: $3(x^4 - 16) = 3(x^2 - 4)(x^2 + 4) = 3(x - 2)(x + 2)(x^2 + 4)$.
- (d) Group: $x^2(x + 3) - 4(x + 3) = (x + 3)(x^2 - 4) = (x + 3)(x - 2)(x + 2)$.

Check at $x = 1$ (the sum of the coefficients must equal the product of the factors' values): (a) $1 - 8 = -7$ and $(-1)(7) = -7$. (b) $27 + 64 = 91$ and $7 \cdot 13 = 91$. (c) $3 - 48 = -45$ and $3(-1)(3)(5) = -45$. (d) $1 + 3 - 4 - 12 = -12$ and $4 \cdot (-1) \cdot 3 = -12$.

</details>

6\. (a) Solve $x^2 + x = 12$. (b) Solve $3x^2 = 12x$. (c) A shop makes a profit of $P(q) = -q^2 + 8q - 12$ thousand dollars when it sells $q$ hundred units. Find the break-even quantities, where $P = 0$, and say for which $q$ the profit is positive.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Move the 12: $x^2 + x - 12 = 0$, so $(x + 4)(x - 3) = 0$ and $x = -4$ or $x = 3$.

(b) $3x^2 - 12x = 3x(x - 4) = 0$, so $x = 0$ or $x = 4$. Dividing by $3x$ at the start would lose $x = 0$.

(c) Take out $-1$: $P(q) = -(q^2 - 8q + 12) = -(q - 2)(q - 6)$. So $P = 0$ at $q = 2$ and $q = 6$, which is 200 and 600 units. The expression $-(q - 2)(q - 6)$ is positive when $(q - 2)(q - 6)$ is negative, which happens when the two factors have opposite signs: $q > 2$ and $q < 6$. So the profit is positive for $2 < q < 6$, between 200 and 600 units.

Check: (a) $(-4)^2 + (-4) = 12$ and $3^2 + 3 = 12$. (b) $3 \cdot 16 = 48 = 12 \cdot 4$. (c) $P(4) = -16 + 32 - 12 = 4 > 0$, and $P(1) = -1 + 8 - 12 = -5$ is negative, as expected outside the interval.

</details>

### Challenge

7\. Show that $x^4 + 4$ factors over the integers, even though it has no real zeros. Hint: add and subtract $4x^2$ to make a difference of squares.

<details class="solution" markdown>
<summary>Solution</summary>

The hint gives $x^4 + 4 = x^4 + 4x^2 + 4 - 4x^2$. The first three terms are a perfect-square trinomial, $(x^2 + 2)^2$, and $4x^2 = (2x)^2$, so we have a difference of squares:

$$
x^4 + 4 = (x^2 + 2)^2 - (2x)^2 = (x^2 + 2 - 2x)(x^2 + 2 + 2x) = (x^2 - 2x + 2)(x^2 + 2x + 2).
$$

Each factor is prime over the integers: $b^2 - 4ac = 4 - 8 = -4$, which is negative, so neither has a real zero. And $x^4 + 4 \ge 4$ has no real zero either, which agrees.

Check by expanding: $(x^2 + 2)^2 - 4x^2 = x^4 + 4x^2 + 4 - 4x^2 = x^4 + 4$. At $x = 1$: $5$ equals $1 \cdot 5$.

The lesson is that having no zeros doesn't mean a polynomial is prime. The polynomial $x^4 + 4$ has no real zero and still splits into two quadratics.

</details>

8\. (Reviews [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md).) Show that $n^3 - n$ is divisible by 6 for every integer $n$.

<details class="solution" markdown>
<summary>Solution</summary>

We know how to factor, and that $6 = 2 \cdot 3$ with 2 and 3 having no common factor. We want to show that 6 divides $n^3 - n$. The plan is to factor and look at the factors as consecutive integers.

Factor: $n^3 - n = n(n^2 - 1) = (n - 1)n(n + 1)$. These are three consecutive integers. Among any two consecutive integers, one is even, so the product is divisible by 2. Among any three consecutive integers, exactly one is a multiple of 3, because the remainders mod 3 of $n - 1$, $n$, $n + 1$ run through 0, 1, 2 in some order. So the product is divisible by 3. A number divisible by both 2 and 3 is divisible by 6, since 2 and 3 share no factor.

Look back: the factoring turned a statement about a cube into a statement about three neighbours, where divisibility is easy to see.

Check: $n = 5$ gives $120 = 6 \cdot 20$; $n = 2$ gives $6$; $n = 0$ gives $0$; and $n = -3$ gives $-27 + 3 = -24 = 6 \cdot (-4)$.

</details>

## Where this shows up

- The next lesson, [polynomial division and the remainder theorem](04-polynomial-division-and-remainder-theorem.md), finds factors of higher-degree polynomials when no pattern shows them. Factoring also cancels common factors in [rational expressions](../06-rational-expressions-and-equations/01-rational-expressions.md), finds the sign of a product in [polynomial and rational inequalities](../06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md), and resolves the $\frac{0}{0}$ limits in limits, intuition and limit laws<!-- link: ../../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md -->.
- In linear algebra, the eigenvalues of a matrix are the zeros of its characteristic polynomial, found by factoring (eigenvalues and eigenvectors<!-- link: ../../05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md -->). Computer algebra systems factor polynomials quickly, but no fast method is known for factoring large integers, which is what RSA encryption relies on; the difference-of-squares trick above is the oldest method for the integers.
- In economics, solving profit equal to zero gives the break-even quantities, as in Practice problem 6, and the sign of a factored profit shows where a firm earns money.
