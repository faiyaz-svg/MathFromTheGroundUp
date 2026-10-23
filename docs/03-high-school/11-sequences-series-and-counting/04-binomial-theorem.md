# The binomial theorem

After this lesson you can expand $(a+b)^n$ with the binomial theorem or Pascal's triangle, find one term or coefficient without expanding everything, prove Pascal's rule and the binomial theorem by counting, show that the entries of a row add to $2^n$, approximate $(1+x)^n$ for small $x$, and find the probabilities of coin-flip counts.

Before this: [counting: permutations and combinations](03-counting-permutations-combinations.md) and [polynomial arithmetic](../04-radicals-and-polynomials/02-polynomial-arithmetic.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Expand $(x+2)^3$.
2. What is the coefficient of $x^2y^3$ in $(x+y)^5$?
3. Without a calculator, estimate $1.002^{50}$ using the first two terms of the binomial expansion.

<details class="solution" markdown>
<summary>Answers</summary>

1. The coefficients of the cube of a binomial are $1, 3, 3, 1$, so $(x+2)^3 = x^3 + 3x^2 \cdot 2 + 3x \cdot 2^2 + 2^3 = x^3 + 6x^2 + 12x + 8$.
2. It is $\binom{5}{2} = \binom{5}{3} = 10$.
3. Write $1.002 = 1 + 0.002$. The first two terms of $(1+x)^{50}$ are $1 + 50x = 1 + 50 \cdot 0.002 = 1.1$. (The exact value is 1.10506.)

</details>

## The idea

[Polynomial arithmetic](../04-radicals-and-polynomials/02-polynomial-arithmetic.md) found that

$$
(a+b)^2 = a^2 + 2ab + b^2, \qquad (a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3,
$$

and left a question open: where do the coefficients $1, 2, 1$ and $1, 3, 3, 1$ come from, and what are they for the fifth or tenth power? Multiplying out ten brackets by hand is not a plan.

Look at $(a+b)^3 = (a+b)(a+b)(a+b)$ and ask how a term such as $ab^2$ arises. Multiplying out means taking one term, $a$ or $b$, from each of the three brackets and multiplying the choices. The product $ab^2$ appears when $b$ is taken from two of the brackets and $a$ from the third. There are 3 ways to pick which bracket gives the $a$, so the term appears 3 times and the coefficient is 3. In general, the coefficient of $a^{n-k}b^k$ in $(a+b)^n$ is the number of ways to choose which $k$ of the $n$ brackets give a $b$. That is a counting problem, and it is exactly what $\binom{n}{k}$ counts. The rest of the lesson is this one observation, written carefully, and what follows from it.

## Definitions

**Pascal's triangle** is the triangular array whose row $n$, for $n = 0, 1, 2, \dots$, lists the binomial coefficients $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}$ from the previous lesson. In plain words, it is a pyramid of numbers with 1s down both sides, where each inside entry is the sum of the two entries just above it. Rows and positions both start at 0.

```
n=0                   1
n=1                 1   1
n=2               1   2   1
n=3             1   3   3   1
n=4           1   4   6   4   1
n=5         1   5  10  10   5   1
n=6       1   6  15  20  15   6   1
n=7     1   7  21  35  35  21   7   1
```

In row 5, for instance, the entry in position 2 is $\binom{5}{2} = 10$, and it is the sum of the entries $4$ and $6$ above it, which are $\binom{4}{1}$ and $\binom{4}{2}$. That observation is Pascal's rule, stated and proved below.

The **binomial theorem** is the formula for the expansion of a power of a sum of two terms, called a binomial:

$$
(a+b)^n = \sum_{k=0}^{n} \binom{n}{k}\, a^{n-k} b^k.
$$

In plain words, the expansion has $n + 1$ terms. The exponent of $a$ counts down from $n$ to 0, the exponent of $b$ counts up from 0 to $n$, the two exponents always add to $n$, and the coefficient of the term with $b^k$ is the entry in position $k$ of row $n$ of Pascal's triangle. The terms are written out as

$$
(a+b)^n = \binom{n}{0}a^n + \binom{n}{1}a^{n-1}b + \binom{n}{2}a^{n-2}b^2 + \cdots + \binom{n}{n}b^n.
$$

## How to do it

### Pascal's rule

*Theorem (Pascal's rule).* For integers $n \ge 2$ and $1 \le k \le n - 1$,

$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}.
$$

We know that $\binom{n}{k}$ counts the $k$-element subsets of an $n$-element set. We want to relate it to counts for a set with one element fewer. The plan is to single out one element and split the subsets into two cases, depending on whether they contain it.

*Proof by counting.* Let $S$ be a set of $n$ elements, and pick one element $z$ of $S$. Each $k$-element subset of $S$ either contains $z$ or doesn't, and not both.

If it contains $z$, the other $k - 1$ elements are chosen from the $n - 1$ elements of $S$ other than $z$: $\binom{n-1}{k-1}$ subsets. If it doesn't contain $z$, all $k$ elements are chosen from those $n - 1$ elements: $\binom{n-1}{k}$ subsets. The two cases don't overlap, so by the sum rule the total is $\binom{n-1}{k-1} + \binom{n-1}{k}$. The total is also $\binom{n}{k}$, since these are all the $k$-element subsets of $S$. $\blacksquare$

*Proof by algebra.* Write both terms on the right with the factorial formula and use the common factor $\frac{(n-1)!}{k!\,(n-k)!}$:

$$
\frac{(n-1)!}{(k-1)!\,(n-k)!} + \frac{(n-1)!}{k!\,(n-1-k)!} = \frac{(n-1)!}{k!\,(n-k)!}\bigl[k + (n-k)\bigr] = \frac{n!}{k!\,(n-k)!}.
$$

The first fraction was multiplied top and bottom by $k$, using $k! = k\,(k-1)!$, and the second by $n - k$, using $(n-k)! = (n-k)\,(n-1-k)!$. $\blacksquare$

Look back: the counting proof says why the rule is true, and the algebraic proof says that it is. The rule is what lets you build Pascal's triangle one row at a time with only additions, and it is the same kind of step as the recurrences of [sequences and recursion](01-sequences-and-recursion.md): each row is computed from the one before.

### The binomial theorem

*Theorem (binomial theorem).* For every integer $n \ge 0$ and all numbers $a$ and $b$,

$$
(a+b)^n = \sum_{k=0}^{n} \binom{n}{k}\, a^{n-k} b^k.
$$

We know the distributive property and that $\binom{n}{k}$ counts the $k$-element subsets of an $n$-element set. We want the coefficient of $a^{n-k}b^k$ after $(a+b)^n$ is multiplied out. The plan is to say exactly what multiplying out does, and count.

*Proof.* Write $(a+b)^n$ as a product of $n$ brackets, $(a+b)(a+b)\cdots(a+b)$, and number the brackets $1, 2, \dots, n$. By the distributive property, the product equals the sum of all the products obtained by choosing one term, $a$ or $b$, from each bracket and multiplying the $n$ choices together. There are $2^n$ such choices, one for each way of deciding, bracket by bracket, between $a$ and $b$.

Each choice is determined by the set $T$ of brackets from which $b$ was chosen, and the other $n - |T|$ brackets give $a$. If $|T| = k$, the product of the choices is $a^{n-k}b^k$ (the order of multiplication doesn't matter). For a fixed $k$, the number of sets $T$ with $k$ elements is $\binom{n}{k}$, so the term $a^{n-k}b^k$ occurs exactly $\binom{n}{k}$ times in the sum. Collecting these like terms gives the coefficient $\binom{n}{k}$, and adding over $k = 0, 1, \dots, n$ gives the theorem. $\blacksquare$

Look back: with $n = 3$ the proof says the 8 choices fall into groups of $1, 3, 3, 1$ by how many times $b$ is chosen, which matches $a^3 + 3a^2b + 3ab^2 + b^3$. The proof used only the distributive property and the fact that $a$ and $b$ commute, so it works for any two numbers, and for polynomials in place of $a$ and $b$. Practice problem 7 gives a second proof by induction, which uses Pascal's rule.

### Expanding a binomial

1. Identify $a$ and $b$ with their signs and coefficients, and put each in brackets: for $(2x - 3)^4$, $a = 2x$ and $b = -3$.
2. Write out the $n + 1$ coefficients $\binom{n}{k}$ for $k = 0, \dots, n$, from Pascal's triangle or the formula.
3. Write each term as $\binom{n}{k}\, a^{n-k}\, b^k$. The exponents of $a$ go down from $n$ to 0, and those of $b$ go up from 0 to $n$.
4. Simplify each term: work out the powers of numbers inside the brackets, and keep track of signs. A negative $b$ makes the signs alternate.
5. Check: there should be $n + 1$ terms, and substituting a simple value (such as $x = 1$) into the original and the expansion should give the same number.

### Finding one term or one coefficient

1. Write the general term, $\binom{n}{k}\, a^{n-k}\, b^k$, with $a$ and $b$ in brackets.
2. Simplify the general term so that the power of $x$ is visible, usually something like $x^{c - dk}$.
3. Set the exponent equal to the one you want (0 for the constant term) and solve for $k$. It must be a whole number from 0 to $n$; if it isn't, the coefficient is 0.
4. Evaluate that one term, with its sign.
5. Check that the exponent of $x$ in your answer is the one asked for.

### Row sums and subsets

*Theorem.* For every integer $n \ge 0$, $\sum_{k=0}^{n} \binom{n}{k} = 2^n$. For $n \ge 1$, $\sum_{k=0}^{n} (-1)^k\binom{n}{k} = 0$.

*Proof.* In the binomial theorem put $a = b = 1$: $2^n = (1+1)^n = \sum_{k=0}^{n} \binom{n}{k}\, 1^{n-k}\, 1^k$. For the second, put $a = 1$ and $b = -1$: $0^n = (1 + (-1))^n = \sum_{k=0}^{n} \binom{n}{k}(-1)^k$, and $0^n = 0$ when $n \ge 1$. $\blacksquare$

Here is the counting meaning of the first. A set with $n$ elements has $2^n$ subsets (each element is in or out), and sorting the subsets by size, $\binom{n}{k}$ of them have size $k$. Adding up the sizes' counts must give the total. The second says that, for $n \ge 1$, there are as many subsets of even size as of odd size, namely $2^{n-1}$ of each. Moving the negative terms to the other side of the equation shows this: the entries in even positions in a row add up to the entries in odd positions.

### Approximating a power near 1

Put $a = 1$ and $b = x$ in the binomial theorem:

$$
(1 + x)^n = 1 + nx + \binom{n}{2}x^2 + \binom{n}{3}x^3 + \cdots + x^n.
$$

When $x$ is small, the powers $x^2, x^3, \dots$ are much smaller still, so the first two terms are a good estimate: $(1+x)^n \approx 1 + nx$. The error is mainly the next term, $\binom{n}{2}x^2$. For $x \ge 0$ every term in the expansion is non-negative, so dropping terms can only make the sum smaller. That proves the following inequality.

*Theorem (Bernoulli's inequality).* For every real $x \ge 0$ and every integer $n \ge 0$, $(1 + x)^n \ge 1 + nx$.

The next table compares the exact value with one-term and two-term estimates:

| $x$ | $n$ | exact $(1+x)^n$ | $1 + nx$ | $1 + nx + \binom{n}{2}x^2$ | $nx$ |
|---|---|---|---|---|---|
| $0.005$ | $12$ | $1.061678$ | $1.06$ | $1.06165$ | $0.06$ |
| $0.002$ | $50$ | $1.105061$ | $1.1$ | $1.1049$ | $0.1$ |
| $0.05$ | $10$ | $1.628895$ | $1.5$ | $1.6125$ | $0.5$ |

The first-order estimate works when $nx$ is small, not when $x$ is small: with $n x = 0.06$ it is off by about 0.16%, with $nx = 0.1$ by about 0.5%, and with $nx = 0.5$ by about 8%. The estimate also works for negative $x$: $0.995^{12} \approx 1 - 12 \cdot 0.005 = 0.94$, and the exact value is $0.94162$. The first row is a compound-interest fact. An account paying 0.5% per month grows by a factor of $1.005^{12} = 1.0617$ over a year, a bit more than the 6% you get by multiplying 0.5% by 12. The extra 0.17% is the second term $\binom{12}{2}(0.005)^2 = 0.00165$: interest earning interest. The difference between the 6% rate and the 6.17% growth is the topic of [APR, APY and the effective annual rate](../../08-financial-math/02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md).

### Why powers of a small ratio shrink

This section fills the gap left in [summation notation and series](02-summation-notation-and-series.md), which used the fact that $r^n$ gets close to 0 when $\lvert r \rvert < 1$.

First take $0 < r < 1$. Then $r = \frac{1}{1+h}$ for the positive number $h = \frac{1}{r} - 1$. By Bernoulli's inequality, $(1+h)^n \ge 1 + nh$, so

$$
0 < r^n = \frac{1}{(1+h)^n} \le \frac{1}{1 + nh} < \frac{1}{nh}.
$$

The right side shrinks below any target you choose once $n$ is large enough: for a target $\varepsilon > 0$, every $n > \frac{1}{h\varepsilon}$ works. So $r^n$ is as close to 0 as you like for large $n$. For $-1 < r < 0$, apply this to $\lvert r \rvert$, since $\lvert r^n \rvert = \lvert r \rvert^n$. For $r = 0.9$, we get $h = \frac{1}{9}$ and $0.9^n < \frac{9}{n}$, a crude bound (the truth at $n = 100$ is 0.00003 against the bound 0.09), but enough to see that $0.9^n \to 0$.

### Coin flips

A fair coin is flipped $n$ times. The $2^n$ sequences of heads and tails are equally likely, and the number of sequences with exactly $k$ heads is $\binom{n}{k}$, because such a sequence is determined by which $k$ of the $n$ flips are heads. So, using the counting form of probability from [basic probability](../../02-middle-school/07-statistics-and-probability/02-basic-probability.md),

$$
P(\text{exactly } k \text{ heads in } n \text{ flips}) = \frac{\binom{n}{k}}{2^n}.
$$

The row-sum theorem says these probabilities, for $k = 0, \dots, n$, add up to $\frac{2^n}{2^n} = 1$, as they must. For a coin that lands heads with probability $p$, each sequence with $k$ heads has probability $p^k(1-p)^{n-k}$, so the probability of exactly $k$ heads is $\binom{n}{k}p^k(1-p)^{n-k}$, and the binomial theorem with $a = 1 - p$ and $b = p$ shows these add to $(1 - p + p)^n = 1$. These are the probabilities of the binomial distribution (see [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md)).

## Worked examples

<div class="example" markdown>

### Example 1: expanding a binomial with a coefficient and a negative

Expand $(2x - 3)^4$.

Step 1: $a = 2x$, $b = -3$, $n = 4$.

Step 2: row 4 of Pascal's triangle is $1, 4, 6, 4, 1$.

Step 3 and 4: write each term $\binom{4}{k}(2x)^{4-k}(-3)^k$ and simplify. Raise the whole bracket $2x$ to its power, which includes the 2:

| $k$ | term | simplified |
|---|---|---|
| 0 | $1 \cdot (2x)^4 \cdot 1$ | $16x^4$ |
| 1 | $4 \cdot (2x)^3 \cdot (-3)$ | $4 \cdot 8x^3 \cdot (-3) = -96x^3$ |
| 2 | $6 \cdot (2x)^2 \cdot 9$ | $6 \cdot 4x^2 \cdot 9 = 216x^2$ |
| 3 | $4 \cdot (2x) \cdot (-27)$ | $-216x$ |
| 4 | $1 \cdot 1 \cdot 81$ | $81$ |

So $(2x - 3)^4 = 16x^4 - 96x^3 + 216x^2 - 216x + 81$. The signs alternate because $b$ is negative.

Step 5: there are 5 terms, as there should be for $n = 4$. Substitute $x = 1$: the left side is $(2 - 3)^4 = 1$, and the right side is $16 - 96 + 216 - 216 + 81 = 1$. Also substitute $x = 2$: the left is $(4-3)^4 = 1$ and the right is $256 - 768 + 864 - 432 + 81 = 1$.

</div>

<div class="example" markdown>

### Example 2: one coefficient

Find the coefficient of $x^8$ in $\left(x^2 - \frac{1}{x}\right)^{10}$.

Step 1: the general term, with $a = x^2$ and $b = -x^{-1}$, is

$$
\binom{10}{k}(x^2)^{10-k}\left(-x^{-1}\right)^k.
$$

Step 2: simplify the powers: $(x^2)^{10-k} = x^{20-2k}$ and $(-x^{-1})^k = (-1)^k x^{-k}$, so the term is $\binom{10}{k}(-1)^k x^{20-3k}$.

Step 3: set $20 - 3k = 8$, so $k = 4$, a whole number from 0 to 10.

Step 4: the term has coefficient $\binom{10}{4}(-1)^4 = 210$.

So the coefficient is 210. Check: the exponent is $20 - 12 = 8$, and the sign is positive because $k$ is even. If the question had asked for the coefficient of $x^7$, then $20 - 3k = 7$ would give $k = \frac{13}{3}$, not a whole number, so the coefficient of $x^7$ is 0.

</div>

<div class="example" markdown>

### Example 3: toggles and subsets

A settings panel has 8 independent on/off toggles. (a) How many configurations are there? (b) How many have exactly 3 toggles on? (c) How many have an even number on?

(a) Each toggle is on or off, so there are $2^8 = 256$ configurations. This is the row sum $\sum_{k=0}^{8} \binom{8}{k}$ for row 8.

(b) A configuration with three toggles on is a 3-element subset of the 8 toggles: $\binom{8}{3} = 56$.

(c) For $n = 8$ the alternating sum is 0, so the even-size subsets and the odd-size subsets are equal in number, each half of 256: 128.

Check (c) by adding the even entries of row 8: $\binom{8}{0} + \binom{8}{2} + \binom{8}{4} + \binom{8}{6} + \binom{8}{8} = 1 + 28 + 70 + 28 + 1 = 128$. Note that the "no toggles on" configuration, the empty subset, is included in the even count. The row 8 entries $1, 8, 28, 56, 70, 56, 28, 8, 1$ add to 256.

</div>

<div class="example" markdown>

### Example 4: ten coin flips

A fair coin is flipped 10 times. Find the probability of (a) exactly 5 heads, (b) 7 or more heads, (c) between 4 and 6 heads, inclusive.

Row 10 of Pascal's triangle is $1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1$, and its entries add to $2^{10} = 1024$.

(a) $\frac{\binom{10}{5}}{1024} = \frac{252}{1024} \approx 0.246$.

(b) Add the counts for 7, 8, 9 and 10 heads: $120 + 45 + 10 + 1 = 176$, so the probability is $\frac{176}{1024} = \frac{11}{64} \approx 0.172$.

(c) Add the counts for 4, 5 and 6 heads: $210 + 252 + 210 = 672$, so the probability is $\frac{672}{1024} = \frac{21}{32} \approx 0.656$.

Check: by symmetry, 7 or more heads is as likely as 3 or fewer, and the two groups together with the middle range 4 to 6 must cover everything: $176 + 176 + 672 = 1024$.

</div>

<div class="example" markdown>

### Example 5: a monthly rate over a year (finish it yourself)

An account pays 0.4% per month, so after a year the balance is multiplied by $1.004^{12}$. Estimate this factor with the first three terms of the binomial expansion, then compare with the exact value 1.04907.

The first two terms are $1 + 12 \cdot 0.004 = 1.048$. The third term is $\binom{12}{2}(0.004)^2$. Work it out, add it, and compare the estimate with the exact value.

<details class="solution" markdown>
<summary>Finish</summary>

$\binom{12}{2} = 66$ and $(0.004)^2 = 0.000016$, so the third term is $66 \cdot 0.000016 = 0.001056$. The three-term estimate is $1.048 + 0.001056 = 1.049056$.

The exact value is $1.004^{12} = 1.049070\ldots$, so the three-term estimate is off by about $0.000014$, and the two-term estimate $1.048$ was off by about $0.0011$. The next term, $\binom{12}{3}(0.004)^3 = 220 \cdot 0.000000064 = 0.0000141$, accounts for the remaining gap.

Check: adding that fourth term gives $1.049056 + 0.0000141 = 1.0490701$, which agrees with the exact value to six decimal places. The year's growth is 4.907%, a little over the 4.8% you get by multiplying 0.4% by 12.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: $(a+b)^n$ is not $a^n + b^n$. Take $a = 1$, $b = 2$ and $n = 2$: $(1 + 2)^2 = 9$, but $1 + 4 = 5$. The missing term is the middle one, $2ab = 4$. In the binomial theorem the terms with both $a$ and $b$ are the ones that this mistake leaves out.

</div>

<div class="warning" markdown>

Watch out when $a$ or $b$ has a coefficient or a sign. In $(2x - 3)^4$ the first term is $(2x)^4 = 16x^4$, not $2x^4$: the 2 is part of $a$ and gets raised to the power. And $b = -3$, so $b^3 = -27$ and $b^4 = +81$. Putting $a$ and $b$ in brackets, as in Step 1, prevents both slips.

</div>

<div class="warning" markdown>

Watch out for off-by-one errors. Row 0 of Pascal's triangle is $1$, so row $n$ has $n + 1$ entries, and $(a+b)^n$ has $n + 1$ terms. The first term has $k = 0$. A frequent slip is reading the entries of row $n$ as $\binom{n}{1}, \dots, \binom{n}{n}$, which skips the first 1 and shifts every coefficient.

</div>

<div class="warning" markdown>

Watch out: $(1+x)^n \approx 1 + nx$ needs the product $nx$ to be small, and a small $x$ alone is not enough. For $x = 0.05$ and $n = 10$ the estimate is $1.5$ and the true value is $1.629$, a miss of about 8%. If $nx$ is not well below 1, include the $\binom{n}{2}x^2$ term, or compute the power directly.

</div>

The case $n = 0$ is allowed: $(a+b)^0 = 1 = \binom{0}{0}a^0b^0$. Coefficients can be huge even for modest $n$: the middle entry of row 30 is $\binom{30}{15} = 155{,}117{,}520$. Finally, the theorem as stated is for whole-number exponents; $(a+b)^{-1}$ and $(a+b)^{1/2}$ need the infinite versions of calculus (see the FAQ).

## Tricks and shortcuts

Build a row from the previous one when you need a few rows: write 1, add neighbours, write 1. For one entry in a big row, use the ratio $\binom{n}{k+1} = \binom{n}{k}\cdot\frac{n-k}{k+1}$, which follows from the factorial formula. Starting from $\binom{10}{0} = 1$ it gives $1, 10, 45, 120, 210, 252$ by multiplying by $\frac{10}{1}, \frac{9}{2}, \frac{8}{3}, \frac{7}{4}, \frac{6}{5}$. Then use symmetry, $\binom{n}{k} = \binom{n}{n-k}$, for the other half of the row.

The first rows are the digits of the powers of 11 until a carry happens: $11^2 = 121$, $11^3 = 1331$ and $11^4 = 14641$. From $11^5 = 161051$ on, the entries (10 and more) overlap in the same decimal place and the digits no longer match. This works because $11 = 10 + 1$ and $11^n = \sum \binom{n}{k}10^{n-k}$.

Test any expansion by setting the variable to 1 and comparing both sides, as in Example 1. For $(a - b)^n$, replace $b$ with $-b$ in the theorem: the signs alternate, and setting $a = b$ gives 0.

Mental estimates of growth use $(1+x)^n \approx 1 + nx$: 3% for 3 years is about 9%, true value 9.27%. At 2% for 5 years, about 10%, true value 10.4%.

## In code

The recurrence of Pascal's rule builds the triangle, `math.comb` checks it, and a loop compares exact powers with the first-order estimate.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def pascal(rows):
    row = [1]
    triangle = [row]
    for _ in range(rows - 1):
        # Pascal's rule: each inside entry is the sum of the two above it
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        triangle.append(row)
    return triangle

tri = pascal(9)
print(tri[8])                                    # [1, 8, 28, 56, 70, 56, 28, 8, 1]
print(all(tri[n][k] == math.comb(n, k)
          for n in range(9) for k in range(n + 1)))   # True
print([sum(row) for row in tri])                 # [1, 2, 4, 8, 16, 32, 64, 128, 256]

n = 10
probs = [math.comb(n, k) / 2**n for k in range(n + 1)]
print(round(probs[5], 4), round(sum(probs), 4))  # 0.2461 1.0

for x, m in [(0.005, 12), (0.002, 50), (0.05, 10)]:
    exact, estimate = (1 + x)**m, 1 + m * x
    print(m * x, round(exact, 6), estimate)
# 0.06 1.061678 1.06
# 0.1 1.105061 1.1
# 0.5 1.628895 1.5
```

The row sums are the powers of 2, the probabilities of the coin-flip counts add up to 1, and the estimate $1 + nx$ gets worse as $nx$ grows. The last column of the table above and the three printed lines agree.

</details>

## FAQ

### Does the binomial theorem work when the exponent is not a whole number?

In a different form, yes. For a real exponent $\alpha$ and $\lvert x \rvert < 1$, $(1+x)^\alpha$ equals an infinite sum $1 + \alpha x + \frac{\alpha(\alpha-1)}{2}x^2 + \cdots$, where the coefficients are built from the product form of $\binom{n}{k}$. It is why $(1+x)^{1/2} \approx 1 + \frac{x}{2}$ for small $x$: the first-order estimate holds for every exponent. The infinite version is part of [power series and Taylor series](../../05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md).

### Why are the rows of Pascal's triangle symmetric?

Because $\binom{n}{k} = \binom{n}{n-k}$, and the counting reason is that choosing the $k$ brackets that give a $b$ is the same as choosing the $n - k$ brackets that give an $a$. In the theorem it shows as the symmetry between $a$ and $b$: $(a+b)^n = (b+a)^n$.

### Is there a version for three or more terms?

Yes. In $(a+b+c)^n$ the coefficient of $a^ib^jc^k$, where $i + j + k = n$, is $\frac{n!}{i!\,j!\,k!}$, the repeated-letters count from the previous lesson. The proof is the same: choose $a$, $b$ or $c$ from each of the $n$ brackets, and count the ways that give $i$ choices of $a$, $j$ of $b$ and $k$ of $c$. This is the multinomial theorem.

### Does it work for matrices?

Only when the two matrices commute. The proof uses $ab = ba$ to group the products. For matrices $A$ and $B$ with $AB \ne BA$, already $(A+B)^2 = A^2 + AB + BA + B^2$ is not $A^2 + 2AB + B^2$. When $AB = BA$ the theorem holds as stated.

## Practice

### Warm-up

1\. Write row 7 of Pascal's triangle from row 6, using Pascal's rule, and check that its entries add to $2^7$.

<details class="solution" markdown>
<summary>Solution</summary>

Row 6 is $1, 6, 15, 20, 15, 6, 1$. Write 1, then add each pair of neighbours, then write 1. The sums are $1 + 6 = 7$, $6 + 15 = 21$, $15 + 20 = 35$, $20 + 15 = 35$, $15 + 6 = 21$ and $6 + 1 = 7$. The row is $1, 7, 21, 35, 35, 21, 7, 1$.

The sum is $1 + 7 + 21 + 35 + 35 + 21 + 7 + 1 = 128 = 2^7$.

Check: $\binom{7}{3} = \frac{7 \cdot 6 \cdot 5}{6} = 35$, which matches the middle entries, and the row is symmetric.

</details>

2\. Expand $(x + 3)^4$.

<details class="solution" markdown>
<summary>Solution</summary>

Row 4 is $1, 4, 6, 4, 1$. The terms are $\binom{4}{k}x^{4-k}3^k$:

$$
x^4 + 4x^3 \cdot 3 + 6x^2 \cdot 9 + 4x \cdot 27 + 81 = x^4 + 12x^3 + 54x^2 + 108x + 81.
$$

Check at $x = 1$: $(1 + 3)^4 = 256$ and $1 + 12 + 54 + 108 + 81 = 256$.

</details>

3\. Find (a) the coefficient of $x^3$ in $(1 + x)^8$, (b) the coefficient of $x^2y^5$ in $(x + y)^7$, and (c) the sum of the coefficients of $(1 + x)^{10}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The coefficient of $x^3$ is $\binom{8}{3} = 56$.
- (b) The exponents add to 7, and the coefficient is $\binom{7}{2} = \binom{7}{5} = 21$.
- (c) Put $x = 1$: the sum of the coefficients is $(1+1)^{10} = 1024$, which is the row sum.

Check (a) against row 8 of the triangle: $1, 8, 28, 56, \dots$, where position 3 holds 56.

</details>

### Standard

4\. Expand $(3x - 2y)^3$.

<details class="solution" markdown>
<summary>Solution</summary>

Take $a = 3x$ and $b = -2y$. Row 3 is $1, 3, 3, 1$:

$$
(3x)^3 + 3(3x)^2(-2y) + 3(3x)(-2y)^2 + (-2y)^3 = 27x^3 - 54x^2y + 36xy^2 - 8y^3.
$$

Check at $x = y = 1$: $(3 - 2)^3 = 1$ and $27 - 54 + 36 - 8 = 1$.

</details>

5\. Find (a) the coefficient of $x^4$ in $(2x + 1)^7$ and (b) the constant term of $\left(x + \frac{2}{x}\right)^6$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) With $a = 2x$ and $b = 1$, the term with $x^4$ is the one with $a^4$. Then $b$ has the power $k = 7 - 4 = 3$, and the term is $\binom{7}{3}(2x)^4 \cdot 1^3 = 35 \cdot 16x^4 = 560x^4$. The coefficient is 560.

(b) The general term is $\binom{6}{k}x^{6-k}\left(\frac{2}{x}\right)^k = \binom{6}{k}2^k x^{6-2k}$. The constant term needs $6 - 2k = 0$, so $k = 3$: $\binom{6}{3}2^3 = 20 \cdot 8 = 160$.

Check (a): $\binom{7}{3} = \binom{7}{4} = 35$ by symmetry, and $2^4 = 16$, so the coefficient is $35 \cdot 16 = 560$ whichever way you count. Check (b): when $k = 3$, $x^3 \cdot \frac{8}{x^3} = 8$, and $20 \cdot 8 = 160$.

</details>

6\. A fair coin is flipped 12 times. Find the probability of (a) exactly 4 heads and (b) at least 10 heads.

<details class="solution" markdown>
<summary>Solution</summary>

There are $2^{12} = 4096$ equally likely sequences.

(a) $\binom{12}{4} = 495$, so the probability is $\frac{495}{4096} \approx 0.1208$.

(b) At least 10 heads means 10, 11 or 12: $\binom{12}{10} + \binom{12}{11} + \binom{12}{12} = 66 + 12 + 1 = 79$, so the probability is $\frac{79}{4096} \approx 0.0193$.

Check: by symmetry (heads and tails swap), the probability of at least 10 heads equals the probability of at most 2 heads, $\binom{12}{0} + \binom{12}{1} + \binom{12}{2} = 1 + 12 + 66 = 79$.

</details>

### Challenge

7\. Prove the binomial theorem by induction on $n$, using Pascal's rule.

<details class="solution" markdown>
<summary>Solution</summary>

Let $P(n)$ be the statement $(a+b)^n = \sum_{k=0}^{n} \binom{n}{k}a^{n-k}b^k$.

Base case: for $n = 0$ both sides are 1, since $\binom{0}{0}a^0b^0 = 1$.

Step: assume $P(n)$ for some $n \ge 0$. Multiply by $(a+b)$:

$$
(a+b)^{n+1} = a\sum_{k=0}^{n} \binom{n}{k}a^{n-k}b^k + b\sum_{k=0}^{n} \binom{n}{k}a^{n-k}b^k = \sum_{k=0}^{n} \binom{n}{k}a^{n+1-k}b^k + \sum_{k=0}^{n} \binom{n}{k}a^{n-k}b^{k+1}.
$$

In the second sum put $j = k + 1$ (the shifting rule), which gives $\sum_{j=1}^{n+1} \binom{n}{j-1}a^{n+1-j}b^j$. Rename $k$ to $j$ in the first sum. The term $j = 0$ appears only in the first sum, as $a^{n+1}$. The term $j = n+1$ appears only in the second, as $b^{n+1}$. For $1 \le j \le n$ both sums contribute, and the coefficient of $a^{n+1-j}b^j$ is $\binom{n}{j} + \binom{n}{j-1} = \binom{n+1}{j}$ by Pascal's rule. Since $\binom{n+1}{0} = \binom{n+1}{n+1} = 1$ as well, the total is $\sum_{j=0}^{n+1} \binom{n+1}{j}a^{n+1-j}b^j$, which is $P(n+1)$.

So $P(0)$ holds, and $P(n)$ implies $P(n+1)$: the theorem holds for every $n$. $\blacksquare$

Check with $n = 1$ going to $n = 2$: $(a+b)(a+b) = a^2 + ab + ba + b^2$, and the middle coefficient is $\binom{1}{1} + \binom{1}{0} = 2 = \binom{2}{1}$.

</details>

8\. (Reviews [exponent rules](../../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md) and growth by a percent.) An investment grows 7% a year. (a) Use Bernoulli's inequality to show that it doubles in 15 years or fewer. (b) Use a calculator to find the first whole year in which the value is at least double, and compare it with the bound from (a).

<details class="solution" markdown>
<summary>Solution</summary>

(a) After $n$ years the value is multiplied by $1.07^n$. By Bernoulli's inequality, $1.07^n \ge 1 + 0.07n$. This is at least 2 when $0.07n \ge 1$, that is, $n \ge \frac{1}{0.07} \approx 14.29$. So with $n = 15$ the value has at least doubled: $1.07^{15} \ge 1 + 1.05 = 2.05$.

(b) Directly, $1.07^{10} = 1.967$, which is below 2, and $1.07^{11} = 2.105$, which is above. So the investment first passes double in year 11. The bound of 15 years is safe but loose, because Bernoulli's inequality ignores the interest earning interest.

Check: the exact doubling time is $\frac{\ln 2}{\ln 1.07} \approx 10.24$ years ([logarithms](../07-exponentials-and-logarithms/02-logarithms.md)), consistent with year 11 being the first whole year past double. The rule of 72 gives $72 \div 7 \approx 10.3$ years.

</details>

## Where this shows up

- The previous lesson, [counting](03-counting-permutations-combinations.md), is where $\binom{n}{k}$ comes from, and Pascal's rule connects it to the recurrences of [sequences and recursion](01-sequences-and-recursion.md). [The binomial theorem and combinatorial proofs](../../06-cs-math/03-counting-and-discrete-probability/03-binomial-theorem-and-combinatorial-proofs.md) goes further with identities proved by double counting.
- In probability and statistics, the binomial distribution has probabilities $\binom{n}{k}p^k(1-p)^{n-k}$ for the number of successes in $n$ independent trials. Calculus uses $(1+x)^n \approx 1 + nx$ as an early example in [linear approximation and L'Hopital's rule](../../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md).
- In finance, $(1 + r)^n \approx 1 + nr$ is the gap between simple and compound interest for small rates, as in [simple interest](../../08-financial-math/02-interest-and-growth/01-simple-interest.md) against [compound interest](../../08-financial-math/02-interest-and-growth/02-compound-interest.md). In CS, $2^n$ counts subsets and bit strings, so the row-sum theorem says that the subsets of an $n$-element set, sorted by size, are counted by row $n$.
