# Summation notation and series

After this lesson you can read and write sigma notation, use its rules, find the sum of an arithmetic or a geometric series (and of an infinite geometric series when $\lvert r \rvert < 1$), prove those formulas, and use them to count the steps of a nested loop, value regular deposits and write a repeating decimal as a fraction.

Before this: [sequences and recursion](01-sequences-and-recursion.md), [exponent rules](../../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md) and [polynomial arithmetic](../04-radicals-and-polynomials/02-polynomial-arithmetic.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Evaluate $\sum_{k=1}^{5} (2k + 1)$.
2. Find $3 + 7 + 11 + \cdots + 99$.
3. Find $\sum_{k=0}^{9} 2 \cdot 3^k$.

<details class="solution" markdown>
<summary>Answers</summary>

1. The terms are $3, 5, 7, 9, 11$, and they add to 35.
2. The numbers go up by 4, so there are $\frac{99 - 3}{4} + 1 = 25$ terms. The average of the first and last is $\frac{3 + 99}{2} = 51$, so the sum is $25 \cdot 51 = 1275$.
3. A geometric series with first term 2, ratio 3 and 10 terms: $2 \cdot \frac{3^{10} - 1}{3 - 1} = 3^{10} - 1 = 59048$.

</details>

## The idea

A program has two nested loops. The outer loop runs $i$ from 1 to $n$, and for each $i$ the inner loop runs $j$ from 1 to $i$, doing one unit of work each time. The inner loop does 1 unit of work when $i = 1$, 2 units when $i = 2$, and $i$ units in general. The total work is

$$
1 + 2 + 3 + \cdots + n.
$$

For $n = 100$ the total is 5050, which is far more than the 100 of a single loop and about half of the $100 \times 100 = 10{,}000$ of a full square grid. Counting the work of a loop is the same problem as adding up a sequence, and the cost of an algorithm often comes down to a sum of this kind.

Writing out "$1 + 2 + 3 + \cdots + n$" is clumsy, and the three dots hide a pattern that a reader must guess. Sigma notation states the pattern exactly. Once the notation is clear, the lesson has two jobs: find short formulas for the sums that come up again and again, and prove them. The sum of the numbers 1 to $n$, the sum of the terms of a geometric sequence, and the sum of squares each get a formula, and each formula has an argument that explains why it is true.

## Definitions

Let $m$ and $n$ be integers with $n \ge m - 1$, and let $a_m, a_{m+1}, \dots, a_n$ be numbers. The **sum** written in **sigma notation** is

$$
\sum_{k=m}^{n} a_k = a_m + a_{m+1} + \cdots + a_n.
$$

The symbol $\Sigma$ is the capital Greek letter sigma, and it means "add up". The letter $k$ is the **index of summation**, the number $m$ is the **lower bound**, the number $n$ is the **upper bound**, and $a_k$ is the **summand**. In plain words, let $k$ take each whole-number value from $m$ up to $n$, work out $a_k$ for each, and add the results.

The sum has $n - m + 1$ terms, so $\sum_{k=3}^{7}$ has 5. When $n = m - 1$ there are no terms, and the **empty sum** is defined to be 0. This is the sum a loop produces if it runs zero times. Formally, the definition is a recurrence: the sum with no terms is 0, and adding one more term to a sum of terms $m$ to $n$ gives the sum of terms $m$ to $n + 1$,

$$
\sum_{k=m}^{m-1} a_k = 0, \qquad \sum_{k=m}^{n+1} a_k = \sum_{k=m}^{n} a_k + a_{n+1}.
$$

The recurrence is exactly the code `total = 0` followed by `total += a(k)` for each $k$ in turn.

The index is a placeholder. The sums $\sum_{k=1}^{3} k$ and $\sum_{j=1}^{3} j$ are the same number, 6, because the letter only names the position in the list, like a loop variable. A letter that already means something in the formula, such as the upper bound $n$, can't also be the index.

A **series** is a sum of the terms of a sequence. The **partial sum** $S_n$ of a sequence $(a_k)$ is the sum of its first terms, $S_n = \sum_{k=0}^{n} a_k$ when the sequence starts at index 0. An **arithmetic series** is a sum of the terms of an arithmetic sequence, and a **geometric series** is a sum of the terms of a geometric sequence. Both are defined in [sequences and recursion](01-sequences-and-recursion.md).

There is a matching notation for products. For $n \ge m - 1$,

$$
\prod_{k=m}^{n} a_k = a_m a_{m+1} \cdots a_n,
$$

where the **empty product** (no factors) is 1. For example, $\prod_{k=1}^{4} k = 1 \cdot 2 \cdot 3 \cdot 4 = 24$, which is $4!$ in the [counting lesson](03-counting-permutations-combinations.md).

## How to do it

### The rules for sums

*Theorem.* Let $(a_k)$ and $(b_k)$ be sequences, let $c$ be a constant that doesn't depend on $k$, and let $m - 1 \le p \le n$ and $s$ be integers. Then:

- (linearity) $\sum_{k=m}^{n} (a_k + b_k) = \sum_{k=m}^{n} a_k + \sum_{k=m}^{n} b_k$ and $\sum_{k=m}^{n} c\,a_k = c \sum_{k=m}^{n} a_k$,
- (constant) $\sum_{k=m}^{n} c = (n - m + 1)\,c$,
- (splitting) $\sum_{k=m}^{n} a_k = \sum_{k=m}^{p} a_k + \sum_{k=p+1}^{n} a_k$,
- (shifting) $\sum_{k=m}^{n} a_k = \sum_{j=m+s}^{n+s} a_{j-s}$.

In plain words: a sum of sums splits, a constant factor comes out, a constant summand counts the terms, a sum can be cut in two at any point, and the index can be renumbered as long as the bounds move with it.

*Proof.* Each rule says that two ways of writing out a list give the same total, and finite sums can be regrouped freely because addition is commutative and associative.

For the first rule, write out the left side: $(a_m + b_m) + (a_{m+1} + b_{m+1}) + \cdots + (a_n + b_n)$. Regrouping gives $(a_m + \cdots + a_n) + (b_m + \cdots + b_n)$, the right side. For the second, the distributive property gives $c(a_m + \cdots + a_n) = ca_m + \cdots + ca_n$. For the constant rule, the sum has $n - m + 1$ terms and each is $c$. For splitting, the terms $a_m, \dots, a_p$ come first and the terms $a_{p+1}, \dots, a_n$ come after, with none left out and none repeated. For shifting, put $j = k + s$. As $k$ runs from $m$ to $n$, $j$ runs from $m + s$ to $n + s$, and the summand $a_k$ is $a_{j-s}$, so both sides list the same terms $a_m, \dots, a_n$. (A fully formal version uses induction on $n$ with the recurrence in the definition.) $\blacksquare$

Look back: the rules are the reason that sigma notation is useful. They let you turn a complicated sum into simple pieces, and the shifting rule is the one that fixes the bounds so that a known formula applies. Two things look like rules and are not: in general $\sum a_k b_k \ne \left(\sum a_k\right)\left(\sum b_k\right)$ and $\sum a_k^2 \ne \left(\sum a_k\right)^2$. With $a_k = b_k = k$ and $k$ from 1 to 2, the first gives $1 + 4 = 5$ against $3 \cdot 3 = 9$.

### Evaluating a sum

1. Identify the index, the bounds and the summand, and count the terms, $n - m + 1$.
2. If there are only a few terms, list them and add. Otherwise, use the rules to break the summand into pieces of three kinds: a constant, a multiple of $k$ (or $k^2$), or a power $r^k$.
3. Use the formula for each piece (the table below). If the bounds of a formula don't match yours, split or shift: $\sum_{k=m}^{n} k = \sum_{k=1}^{n} k - \sum_{k=1}^{m-1} k$.
4. Combine the pieces.
5. Check with a small case: replace $n$ by 2 or 3 and add the terms by hand, or compute the sum with a few lines of code.

| Sum | Value | Where it is proved |
|---|---|---|
| $\sum_{k=1}^{n} 1$ | $n$ | constant rule |
| $\sum_{k=1}^{n} k$ | $\frac{n(n+1)}{2}$ | Gauss's pairing, below |
| $\sum_{k=1}^{n} k^2$ | $\frac{n(n+1)(2n+1)}{6}$ | telescoping, below |
| $\sum_{k=1}^{n} k^3$ | $\left(\frac{n(n+1)}{2}\right)^2$ | Practice problem 8 |
| $\sum_{k=0}^{n-1} r^k$, for $r \ne 1$ | $\frac{1 - r^n}{1 - r}$ | shift and subtract, below |

### The sum of the first $n$ whole numbers

*Theorem.* For every integer $n \ge 1$,

$$
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}.
$$

We know the sigma rules. We want a formula for $1 + 2 + \cdots + n$. The plan is to write the sum twice, once forwards and once backwards, and add the two copies column by column, so that every column has the same total.

*Proof.* Let $S = \sum_{k=1}^{n} k$. Writing the terms in the opposite order gives the same sum:

$$
\begin{aligned}
S &= 1 + 2 + 3 + \cdots + (n-1) + n \\
S &= n + (n-1) + (n-2) + \cdots + 2 + 1
\end{aligned}
$$

Adding the two lines term by term, each column adds up to $n + 1$, and there are $n$ columns, so $2S = n(n+1)$. In sigma notation this is a use of the rules. The backwards sum is $\sum_{k=1}^{n} (n + 1 - k)$, which equals $S$ by the shifting rule (put $j = n + 1 - k$). So

$$
2S = \sum_{k=1}^{n} k + \sum_{k=1}^{n} (n + 1 - k) = \sum_{k=1}^{n} (n + 1) = n(n+1),
$$

by linearity and the constant rule. Dividing by 2 gives $S = \frac{n(n+1)}{2}$. $\blacksquare$

Look back: the pairing shows why the formula is "the number of terms times the average of the first and last", since the average of 1 and $n$ is $\frac{n+1}{2}$. The same argument handles any arithmetic series. If $a_k = a_0 + kd$ and the series has $n$ terms, $k = 0, \dots, n - 1$, then by linearity

$$
\sum_{k=0}^{n-1} (a_0 + kd) = n\,a_0 + d \sum_{k=0}^{n-1} k = n\,a_0 + d\,\frac{(n-1)n}{2} = \frac{n}{2}\bigl(a_0 + (a_0 + (n-1)d)\bigr).
$$

Here the middle step uses the theorem, with $n - 1$ in place of $n$ (the term $k = 0$ adds nothing). The right side says: the sum is $\frac{n}{2}$ times (first term plus last term).

### The geometric series

*Theorem.* For a number $r \ne 1$, a number $a$, and an integer $n \ge 1$,

$$
\sum_{k=0}^{n-1} a r^k = a\,\frac{1 - r^n}{1 - r}.
$$

If $r = 1$, every term is $a$ and the sum is $na$.

We know the sum has $n$ terms, with exponents $0$ to $n - 1$. We want a formula that doesn't need the $n$ terms to be added. The plan is to multiply the sum by $r$, which slides every term one place along, and subtract: almost everything cancels.

*Proof.* Let $S = a + ar + ar^2 + \cdots + ar^{n-1}$. Multiplying by $r$ gives

$$
rS = ar + ar^2 + \cdots + ar^{n-1} + ar^n.
$$

The two lists share the terms $ar, ar^2, \dots, ar^{n-1}$. Subtracting, those cancel, and only the first term of $S$ and the last term of $rS$ remain:

$$
S - rS = a - ar^n, \qquad \text{that is,} \qquad (1 - r)S = a(1 - r^n).
$$

Since $r \ne 1$, we can divide by $1 - r$, which gives the formula. In sigma notation, $rS = \sum_{k=0}^{n-1} ar^{k+1} = \sum_{k=1}^{n} ar^k$ by the shifting rule, and splitting off the first term of $S$ and the last term of $rS$ leaves the common middle $\sum_{k=1}^{n-1} ar^k$ to cancel. $\blacksquare$

Look back: the same idea is behind the factoring identity $1 - r^n = (1 - r)(1 + r + \cdots + r^{n-1})$ from [polynomial arithmetic](../04-radicals-and-polynomials/02-polynomial-arithmetic.md), where $n = 2$ is the difference of squares. When $r > 1$ it is more comfortable to write the formula as $a\,\frac{r^n - 1}{r - 1}$, which is the same number with the top and bottom both multiplied by $-1$. The number of terms is $n$, which is the exponent in the formula, and not the last exponent $n - 1$.

### The infinite geometric series

Suppose $\lvert r \rvert < 1$. The partial sum after $n$ terms is $S_n = a\,\frac{1 - r^n}{1 - r}$. The only part that changes with $n$ is $r^n$, and for $\lvert r \rvert < 1$ the power $r^n$ gets closer to 0 as $n$ grows: $0.9^{10} \approx 0.35$, $0.9^{50} \approx 0.005$ and $0.9^{100} \approx 0.00003$. So $S_n$ gets closer and closer to $\frac{a}{1 - r}$.

An **infinite series** $\sum_{k=0}^{\infty} a_k$ means the number that the partial sums $S_n$ approach as $n$ grows without bound, when there is such a number. In that case the series **converges** to that number, and otherwise it **diverges**. (The word "approach" is left informal here. Sequences and their limits<!-- link: ../../05-university-core/05-sequences-and-series/01-sequences-and-their-limits.md --> and infinite series basics<!-- link: ../../05-university-core/05-sequences-and-series/02-infinite-series-basics.md --> make it precise.) For the geometric series, we get:

$$
\sum_{k=0}^{\infty} a r^k = \frac{a}{1 - r} \qquad \text{for } \lvert r \rvert < 1.
$$

When $\lvert r \rvert \ge 1$ and $a \ne 0$ the terms $ar^k$ don't shrink toward 0, and the partial sums keep growing, or keep jumping around, so the series diverges. In particular the formula never applies to $1 + 2 + 4 + 8 + \cdots$, even though $\frac{1}{1 - 2} = -1$ is a number you can compute.

For example, the series $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$ has $a = \frac{1}{2}$ and $r = \frac{1}{2}$, so the sum is $\frac{1/2}{1 - 1/2} = 1$. The partial sums $\frac{1}{2}, \frac{3}{4}, \frac{7}{8}, \dots$ are $1 - \frac{1}{2^n}$, and they approach 1 without reaching it. The fact that $r^n \to 0$ for $\lvert r \rvert < 1$ has a short proof, which is a use of the [binomial theorem](04-binomial-theorem.md#why-powers-of-a-small-ratio-shrink).

### Telescoping, and the sum of squares

A **telescoping sum** is one where consecutive terms cancel. If $b_k$ is any sequence, then

$$
\sum_{k=m}^{n} (b_{k+1} - b_k) = b_{n+1} - b_m.
$$

To see why, split the sum by linearity into $\sum_{k=m}^{n} b_{k+1} - \sum_{k=m}^{n} b_k$. By the shifting rule the first is $\sum_{j=m+1}^{n+1} b_j$, so the two sums share every term from $b_{m+1}$ to $b_n$, and only $b_{n+1}$ and $-b_m$ are left.

*Theorem.* For every integer $n \ge 1$,

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}.
$$

We know the telescoping rule and the sum of $k$. We want a formula for the sum of squares. The plan is to telescope $(k+1)^3 - k^3$, which contains $k^2$ when it is expanded, and solve for the sum of squares.

*Proof.* Expanding the cube, $(k+1)^3 - k^3 = 3k^2 + 3k + 1$. Sum both sides from $k = 1$ to $n$. The left side telescopes to $(n+1)^3 - 1$. By linearity, the right side is $3\sum k^2 + 3\sum k + n$, and $\sum k = \frac{n(n+1)}{2}$ by the previous theorem. So

$$
3\sum_{k=1}^{n} k^2 = (n+1)^3 - 1 - \frac{3n(n+1)}{2} - n.
$$

Now $(n+1)^3 - (n+1) = (n+1)\bigl((n+1)^2 - 1\bigr) = n(n+1)(n+2)$, so the right side is $n(n+1)(n+2) - \frac{3n(n+1)}{2} = n(n+1)\left(n + 2 - \frac{3}{2}\right) = \frac{n(n+1)(2n+1)}{2}$. Dividing by 3 gives the theorem. $\blacksquare$

Look back: the pattern works for every power. To get $\sum k^3$, telescope $(k+1)^4 - k^4$, which brings in the sum of squares and the sum of $k$ you already have. Each power needs the formulas for the lower powers first, and Practice problem 8 does the cube.

## Worked examples

<div class="example" markdown>

### Example 1: a sum with a shifted index

Evaluate $\sum_{k=2}^{6} (3k - 1)$ by listing, by the rules, and by shifting the index.

Step 1: the index is $k$, the bounds are 2 and 6, the summand is $3k - 1$, and there are $6 - 2 + 1 = 5$ terms.

Step 2, listing: the terms are $5, 8, 11, 14, 17$, which add to 55.

Step 2, rules: split the summand by linearity, $\sum_{k=2}^{6} (3k - 1) = 3\sum_{k=2}^{6} k - \sum_{k=2}^{6} 1$. The second sum is $5 \cdot 1 = 5$ (five terms). Step 3: the first sum starts at 2, not 1, so use $\sum_{k=2}^{6} k = \sum_{k=1}^{6} k - 1 = 21 - 1 = 20$. Step 4: combine, $3 \cdot 20 - 5 = 55$.

Step 3, shifting: put $j = k - 2$, so $k = j + 2$ and $j$ runs from 0 to 4. The summand becomes $3(j+2) - 1 = 3j + 5$, and

$$
\sum_{j=0}^{4} (3j + 5) = 3 \cdot (0 + 1 + 2 + 3 + 4) + 5 \cdot 5 = 30 + 25 = 55.
$$

Step 5: all three methods give 55, which is the check. The terms form an arithmetic sequence with first term 5 and last term 17, so a fourth check is the count times the average of the ends, $5 \cdot \frac{5 + 17}{2} = 55$.

</div>

<div class="example" markdown>

### Example 2: an arithmetic series

Find $3 + 7 + 11 + \cdots + 99$.

The terms are $a_k = 3 + 4k$. To find how many there are, solve $3 + 4k = 99$, which gives $k = 24$, so $k$ runs from 0 to 24 and there are 25 terms. By the arithmetic series formula, the sum is the number of terms times the average of the first and last:

$$
25 \cdot \frac{3 + 99}{2} = 25 \cdot 51 = 1275.
$$

Check with the other form of the formula, $n\,a_0 + d\,\frac{(n-1)n}{2}$ with $n = 25$: $25 \cdot 3 + 4 \cdot \frac{24 \cdot 25}{2} = 75 + 1200 = 1275$. Pairing also works: $3 + 99$, $7 + 95$ and so on all give 102, there are 12 pairs, and the middle term 51 is left over: $12 \cdot 102 + 51 = 1275$.

</div>

<div class="example" markdown>

### Example 3: the cost of nested loops

How many times does the line `count += 1` run in each loop, as a function of $n$?

```python
count = 0
for i in range(1, n + 1):          # loop A
    for j in range(1, i + 1):
        count += 1

count = 0
for i in range(n):                 # loop B
    for j in range(i + 1, n):
        count += 1
```

Loop A is the example from the start of the lesson. The inner loop runs $i$ times, so the total is $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$. For $n = 1000$ that is 500,500 steps.

In loop B the inner loop runs for $j = i+1, \dots, n-1$, which is $n - 1 - i$ times. As $i$ goes from 0 to $n - 1$, this takes the values $n - 1, n - 2, \dots, 0$. The total is $(n-1) + (n-2) + \cdots + 0 = \sum_{k=0}^{n-1} k = \frac{(n-1)n}{2}$ (the previous theorem, with $n - 1$ in place of $n$). For $n = 1000$ that is 499,500, which is the number of pairs of distinct items in a list of 1000, the work done by a loop that compares every pair.

Both counts equal $\frac{n^2}{2}$ plus a term that grows only like $n$. So doubling $n$ from 1000 to 2000 raises loop A from 500,500 to 2,001,000, about four times as many. This is the sense in which these loops are $O(n^2)$: the growth rate is quadratic, whatever the constant $\frac{1}{2}$. Asymptotic notation<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md --> makes that precise.

Check: for $n = 4$, loop A runs $1 + 2 + 3 + 4 = 10$ times and $\frac{4 \cdot 5}{2} = 10$. Loop B runs $3 + 2 + 1 + 0 = 6$ times, and $\frac{3 \cdot 4}{2} = 6$.

</div>

<div class="example" markdown>

### Example 4: a repeating decimal as a fraction

Write $0.363636\ldots = 0.\overline{36}$ as a fraction.

The decimal is a sum of the blocks 36 hundredths, 36 ten-thousandths, and so on:

$$
0.\overline{36} = 0.36 + 0.0036 + 0.000036 + \cdots = \sum_{k=0}^{\infty} 0.36 \cdot (0.01)^k.
$$

This is an infinite geometric series with $a = 0.36$ and $r = 0.01$, and $\lvert r \rvert < 1$, so the sum is

$$
\frac{a}{1 - r} = \frac{0.36}{0.99} = \frac{36}{99} = \frac{4}{11}.
$$

The fraction $\frac{36}{99}$ simplifies by dividing top and bottom by their common factor 9.

Check: $4 \div 11 = 0.363636\ldots$ by long division. Also, the first partial sums $0.36$, $0.3636$ and $0.363636$ approach $\frac{4}{11} = 0.36363636\ldots$ from below.

</div>

<div class="example" markdown>

### Example 5: regular deposits (finish it yourself)

You deposit \$200 at the end of each month for 10 years. Suppose, as an illustration and not as a quoted rate, that the account earns 6% a year, credited monthly, which is $r = 0.005$ per month. How much is in the account right after the last deposit?

The deposit made at the end of month $j$ (for $j = 1, \dots, 120$) then earns interest for $120 - j$ months, so it grows to $200(1.005)^{120 - j}$. The total is

$$
\text{FV} = \sum_{j=1}^{120} 200\,(1.005)^{120-j} = 200\,\bigl(1 + 1.005 + 1.005^2 + \cdots + 1.005^{119}\bigr).
$$

(The last deposit earns no interest, which is the term 1, and the first deposit earns 119 months of interest.) The bracket is a geometric series with $a = 1$, ratio $1.005$ and $n = 120$ terms. Use the geometric series formula to write FV as a single expression, then compute it with a calculator and find how much of it is interest.

<details class="solution" markdown>
<summary>Finish</summary>

The sum is $\frac{1.005^{120} - 1}{1.005 - 1} = \frac{1.005^{120} - 1}{0.005}$, so

$$
\text{FV} = 200 \cdot \frac{1.005^{120} - 1}{0.005}.
$$

Since $1.005^{120} \approx 1.819397$, the bracket is $\frac{0.819397}{0.005} \approx 163.879$ and $\text{FV} \approx 200 \cdot 163.879 = 32{,}775.87$. The account holds about \$32,775.87. You deposited $200 \cdot 120 = 24{,}000$ dollars, so the interest is $32{,}775.87 - 24{,}000 = 8{,}775.87$, about \$8,775.87.

Check: adding the 120 deposits' growth one at a time in code gives the same \$32,775.87. The size also makes sense: without any interest the total would be \$24,000, and the account has gained about 37% on top of that.

</details>

The same algebra explains the loan balance from the last lesson. Writing $B_{n+1} = (1 + r)B_n - \text{PMT}$ as a sum shows that

$$
B_n = (1 + r)^n B_0 - \text{PMT}\cdot\frac{(1 + r)^n - 1}{r}.
$$

You can check it by induction: it gives $B_0$ at $n = 0$, and multiplying the formula for $B_n$ by $1 + r$ and subtracting PMT gives the formula for $B_{n+1}$, because $(1+r)\frac{(1+r)^n - 1}{r} + 1 = \frac{(1+r)^{n+1} - 1}{r}$. For the \$1,000 loan at 1% a month with \$100 payments it gives $B_4 = 634.56$ and $B_{10} = 58.40$, as in the table in the code of the last lesson. The finance lessons on annuities and geometric series<!-- link: ../../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md --> and the loan amortization formula<!-- link: ../../08-financial-math/03-time-value-of-money/03-loan-amortization-formula.md --> build on exactly this.

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the number of terms. The sum $\sum_{k=m}^{n}$ has $n - m + 1$ terms, not $n - m$. So $\sum_{k=3}^{7} 4 = 5 \cdot 4 = 20$, and $\sum_{k=1}^{n} 1 = n$. The geometric formula $\frac{1 - r^n}{1 - r}$ has the number of terms as its exponent: $\sum_{k=0}^{9} 2^k$ has 10 terms, so it is $\frac{1 - 2^{10}}{1 - 2} = 1023$, and writing $2^9$ in the formula gives 511, which is wrong.

</div>

<div class="warning" markdown>

Watch out when the lower bound isn't 1 or 0. The formula $\frac{n(n+1)}{2}$ assumes the sum starts at $k = 1$, so $\sum_{k=5}^{20} k$ is not $\frac{20 \cdot 21}{2} = 210$. Subtract the part you don't want: $210 - \sum_{k=1}^{4} k = 210 - 10 = 200$. Check by the average rule: 16 terms with ends 5 and 20 give $16 \cdot \frac{25}{2} = 200$.

</div>

<div class="warning" markdown>

Watch out: the infinite formula needs $\lvert r \rvert < 1$. The series $1 + 2 + 4 + 8 + \cdots$ doesn't equal $\frac{1}{1 - 2} = -1$; its partial sums $1, 3, 7, 15, \dots$ grow without bound. A series with $r = -1$, such as $1 - 1 + 1 - 1 + \cdots$, has partial sums $1, 0, 1, 0, \dots$ and doesn't settle on any number either.

</div>

<div class="warning" markdown>

Watch out: a sum of products is not a product of sums. $\sum_{k=1}^{3} k \cdot k = 14$, but $\left(\sum_{k=1}^{3} k\right)\left(\sum_{k=1}^{3} k\right) = 36$. And $\sum_{k=1}^{n} (k + 1)^2$ is not $\left(\sum_{k=1}^{n} k + 1\right)^2$. Expand the summand first, then use linearity.

</div>

A constant doesn't need the index. $\sum_{k=1}^{n} 5$ is $5n$, and $\sum_{k=1}^{n} x$ is $nx$ when $x$ doesn't depend on $k$. A sum with one term is just that term: $\sum_{k=4}^{4} a_k = a_4$. A sum with the upper bound below $m - 1$ is not defined by this lesson.

## Tricks and shortcuts

For any arithmetic series the quickest formula is "number of terms times the average of the first and last". The first step is to count the terms: (last $-$ first) $\div$ $d$ $+ 1$. For $5 + 8 + 11 + \cdots + 62$ there are $\frac{62 - 5}{3} + 1 = 20$ terms and the sum is $20 \cdot \frac{67}{2} = 670$.

The sum of the first $n$ odd numbers is $n^2$. By the rules, $\sum_{k=1}^{n} (2k - 1) = 2 \cdot \frac{n(n+1)}{2} - n = n^2$. So $1 + 3 + 5 + 7 + 9 = 25$, and the same number counts the dots in a square grid built by adding an L-shaped border of $2k - 1$ dots at each step.

For a geometric series, test the formula with $n = 1$ and $n = 2$ before trusting it. With one term the sum is $a$, since $a\frac{1 - r}{1 - r} = a$. With two terms it is $a(1 + r)$, since $1 - r^2 = (1 - r)(1 + r)$.

A decimal that repeats a block of $b$ digits is the block over $10^b - 1$: $0.\overline{36} = \frac{36}{99}$ and $0.\overline{7} = \frac{7}{9}$. This is the geometric formula with $a$ equal to the block as a decimal and $r = 10^{-b}$.

## In code

Sums of sequences are one-liners, and a simple counter confirms a loop's cost against the formula. The last lines show that the partial sums of $\sum \left(\frac{1}{2}\right)^k$ approach 2 and that the deposit formula agrees with adding the deposits up.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction

n = 100
print(sum(range(1, n + 1)), n * (n + 1) // 2)    # 5050 5050

def nested_steps(n):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            count += 1
    return count

print(nested_steps(100), nested_steps(200))      # 5050 20100

def geometric_sum(a, r, n):                      # n terms, r != 1
    return a * (1 - r**n) / (1 - r)

print(geometric_sum(2, 3, 10))                   # 59048.0
for n in (5, 10, 20, 40):
    print(n, geometric_sum(1, 0.5, n))
# 5 1.9375
# 10 1.998046875
# 20 1.9999980926513672
# 40 1.999999999998181

def future_value(deposit, rate, n):
    return deposit * ((1 + rate)**n - 1) / rate

print(round(future_value(200, 0.005, 120), 2))                          # 32775.87
print(round(sum(200 * 1.005**(120 - j) for j in range(1, 121)), 2))     # 32775.87

x = Fraction(36, 100) / (1 - Fraction(1, 100))   # a / (1 - r), computed exactly
print(x)                                         # 4/11
```

`Fraction` keeps the repeating-decimal calculation exact, so `4/11` appears with no rounding. The geometric sums are floats, so the last digits of the last line differ slightly from 2.

</details>

## FAQ

### Why is $0.999\ldots$ equal to 1?

Because $0.\overline{9}$ means the infinite series $0.9 + 0.09 + 0.009 + \cdots$, with $a = 0.9$ and $r = 0.1$. Its sum is $\frac{0.9}{1 - 0.1} = \frac{0.9}{0.9} = 1$. The partial sums are $0.9, 0.99, 0.999, \dots$, and the gap between each of them and 1 is $0.1^n$, which shrinks below any size you choose. There is no number between $0.999\ldots$ and 1, so they are the same number written two ways, just as $\frac{1}{2}$ and $\frac{2}{4}$ are.

### Why is the exponent $n$ and not $n - 1$ in the geometric formula?

Because the sum has $n$ terms, $a, ar, \dots, ar^{n-1}$, and the shifted copy $rS$ ends with $ar^n$. After subtracting, the leftover term is $ar^n$, with exponent $n$. A quick test: with $n = 1$ the sum is just $a$, and the formula gives $a\frac{1 - r^1}{1 - r} = a$. With $n - 1$ in place of $n$ you would get $a\frac{1 - r^0}{1 - r} = 0$.

### Is there a formula for $\sum k^p$ for every power $p$?

Yes. For each whole number $p$, $\sum_{k=1}^{n} k^p$ equals a polynomial in $n$ of degree $p + 1$. The telescoping method above finds them one at a time, each using the earlier ones. The general rule is named after Faulhaber, and you rarely need beyond $p = 3$.

### Can I swap the order of a double sum?

For finite sums, yes: $\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} = \sum_{j=1}^{n} \sum_{i=1}^{m} a_{ij}$, since both add up the same grid of numbers. It is no longer free when the inner bounds depend on the outer index, as in loop A, where $j$ runs up to $i$. Then you swap by rewriting the bounds, which is the same as reading the table of $(i, j)$ pairs by columns instead of rows.

## Practice

### Warm-up

1\. Evaluate (a) $\sum_{k=1}^{4} k^2$, (b) $\sum_{k=0}^{3} (2k - 3)$, (c) $\sum_{k=1}^{6} 7$ and (d) $\sum_{k=5}^{4} k$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $1 + 4 + 9 + 16 = 30$.
- (b) The terms are $-3, -1, 1, 3$ and they add to 0.
- (c) There are 6 terms of 7, so $6 \cdot 7 = 42$.
- (d) The upper bound is one below the lower bound, so the sum is empty and equals 0.

Check (a) with the formula: $\frac{4 \cdot 5 \cdot 9}{6} = 30$. Check (b) by pairing $-3$ with $3$ and $-1$ with $1$.

</details>

2\. Find the sum of the arithmetic series $4 + 9 + 14 + \cdots + 104$.

<details class="solution" markdown>
<summary>Solution</summary>

The difference is 5. The number of terms is $\frac{104 - 4}{5} + 1 = 21$. The sum is the number of terms times the average of the first and last: $21 \cdot \frac{4 + 104}{2} = 21 \cdot 54 = 1134$.

Check with the other formula, $n\,a_0 + d\,\frac{(n-1)n}{2}$: $21 \cdot 4 + 5 \cdot \frac{20 \cdot 21}{2} = 84 + 1050 = 1134$.

</details>

3\. Find (a) $\sum_{k=0}^{7} 5 \cdot 2^k$ and (b) $\sum_{k=0}^{\infty} 4 \left(\frac{1}{3}\right)^k$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) A geometric series with $a = 5$, $r = 2$ and 8 terms: $5 \cdot \frac{2^8 - 1}{2 - 1} = 5 \cdot 255 = 1275$.

(b) An infinite geometric series with $a = 4$ and $r = \frac{1}{3}$, and $\lvert r \rvert < 1$: $\frac{4}{1 - 1/3} = \frac{4}{2/3} = 6$.

Check (a): the terms are $5, 10, 20, 40, 80, 160, 320, 640$, which add to 1275. Check (b): the partial sums are $4, 5.33, 5.78, 5.93, \dots$ and they approach 6.

</details>

### Standard

4\. Use the rules and formulas to evaluate (a) $\sum_{k=1}^{20} (k^2 - 3k)$ and (b) $\sum_{k=3}^{10} (2k + 1)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) By linearity, $\sum k^2 - 3\sum k$. With $n = 20$: $\sum_{k=1}^{20} k^2 = \frac{20 \cdot 21 \cdot 41}{6} = 2870$ and $\sum_{k=1}^{20} k = \frac{20 \cdot 21}{2} = 210$. So the answer is $2870 - 3 \cdot 210 = 2240$.

(b) The sum starts at 3, so subtract the first two terms of a sum from 1. Using $\sum_{k=1}^{10} (2k + 1) = 2 \cdot 55 + 10 = 120$ and $\sum_{k=1}^{2} (2k + 1) = 3 + 5 = 8$, the answer is $120 - 8 = 112$.

Check: (b) lists as $7 + 9 + 11 + 13 + 15 + 17 + 19 + 21 = 112$, and 8 terms with ends 7 and 21 give $8 \cdot 14 = 112$. For (a), Python's `sum(k**2 - 3*k for k in range(1, 21))` is 2240.

</details>

5\. A dynamic array starts with room for 1 item, and whenever it is full it allocates twice the room and copies every item across. You append 1024 items. (a) How many item copies happen in total? (b) Compare with 1024, and say what that means for the cost of one append.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The array is full, and gets copied, when it holds $1, 2, 4, 8, \dots, 512$ items. That is one copy of each size $2^k$ for $k = 0, \dots, 9$, so the total is the geometric series

$$
\sum_{k=0}^{9} 2^k = \frac{2^{10} - 1}{2 - 1} = 1023.
$$

(b) There are 1023 copies for 1024 appends, less than one extra copy per append. In general the copies for $n$ appends total less than $n$, so the average cost of an append, counting the occasional expensive copy, is a constant. This is the idea behind "amortized constant time" for appending to a dynamic array. Real implementations grow by other factors than 2, and any constant factor above 1 works the same way.

Check: $1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256 + 512 = 1023$. Note that $1023 = 2^{10} - 1$, one less than the final size.

</details>

6\. Write each as a fraction in lowest terms: (a) $0.\overline{27}$ and (b) $2.1\overline{6}$ (the 6 repeats).

<details class="solution" markdown>
<summary>Solution</summary>

(a) The block 27 has two digits, so $r = 0.01$ and $a = 0.27$: $\frac{0.27}{0.99} = \frac{27}{99} = \frac{3}{11}$.

(b) Split off the part that doesn't repeat: $2.1\overline{6} = 2.1 + 0.0\overline{6}$. The repeating part is $0.06 + 0.006 + \cdots$, with $a = 0.06$ and $r = 0.1$: $\frac{0.06}{0.9} = \frac{6}{90} = \frac{1}{15}$. So the number is $2 + \frac{1}{10} + \frac{1}{15} = 2 + \frac{3}{30} + \frac{2}{30} = 2 + \frac{5}{30} = 2 + \frac{1}{6} = \frac{13}{6}$.

Check: $3 \div 11 = 0.2727\ldots$ and $13 \div 6 = 2.1666\ldots$.

</details>

### Challenge

7\. (Reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).) A salary starts at \$60,000 in year 1 and rises by 3% every year. (a) Write the salary in year $k$ and the total earned in the first $n$ years as a sum, and find a formula for the total. (b) What is the total after 10 years? (c) In which year does the total first pass \$1,000,000?

<details class="solution" markdown>
<summary>Solution</summary>

(a) A 3% rise multiplies by 1.03, so the salary in year $k$ is $60000 \cdot 1.03^{k-1}$ (year 1 is the first term). The total over $n$ years is the geometric series

$$
\sum_{k=1}^{n} 60000 \cdot 1.03^{k-1} = 60000 \cdot \frac{1.03^n - 1}{0.03}.
$$

(b) With $n = 10$: $1.03^{10} \approx 1.343916$, so the total is $60000 \cdot \frac{0.343916}{0.03} \approx 687{,}832.76$, about \$687,833.

(c) We need $60000 \cdot \frac{1.03^n - 1}{0.03} > 1{,}000{,}000$, which is $1.03^n - 1 > 0.5$, that is, $1.03^n > 1.5$. Trying values (or using logarithms, as in [exponential and logarithmic equations](../07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md)): $1.03^{13} \approx 1.4685$, which is below 1.5, and $1.03^{14} \approx 1.5126$, which is above. So the total first passes \$1,000,000 in year 14. After 13 years it is \$937,067, and after 14 years \$1,025,179.

Check: add the salaries directly in Python, `sum(60000 * 1.03**(k - 1) for k in range(1, 15))`, which gives 1025179.45.

</details>

8\. Prove that $\sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2$ by telescoping $(k+1)^4 - k^4$.

<details class="solution" markdown>
<summary>Solution</summary>

We know the formulas for $\sum k^2$, $\sum k$ and $\sum 1$, and the telescoping rule. We want $\sum k^3$. The plan is the same as for squares.

Expand: $(k+1)^4 - k^4 = 4k^3 + 6k^2 + 4k + 1$. Sum from $k = 1$ to $n$. The left side telescopes to $(n+1)^4 - 1$. The right side is, by linearity, $4\sum k^3 + 6\sum k^2 + 4\sum k + n$. So

$$
4\sum_{k=1}^{n} k^3 = (n+1)^4 - 1 - n(n+1)(2n+1) - 2n(n+1) - n.
$$

Here $6\sum k^2 = n(n+1)(2n+1)$ and $4\sum k = 2n(n+1)$. Now $(n+1)^4 - 1 - n = (n+1)^4 - (n+1) = (n+1)\bigl((n+1)^3 - 1\bigr) = (n+1)\,n\,(n^2 + 3n + 3)$. Factoring $n(n+1)$ out of every term:

$$
4\sum k^3 = n(n+1)\bigl[(n^2 + 3n + 3) - (2n+1) - 2\bigr] = n(n+1)(n^2 + n) = n^2(n+1)^2.
$$

Dividing by 4 gives $\sum_{k=1}^{n} k^3 = \frac{n^2(n+1)^2}{4} = \left(\frac{n(n+1)}{2}\right)^2$. $\blacksquare$

Check with $n = 4$: $1 + 8 + 27 + 64 = 100$, and $\left(\frac{4 \cdot 5}{2}\right)^2 = 10^2 = 100$. The result says the sum of the first $n$ cubes is the square of the sum of the first $n$ numbers.

</details>

## Where this shows up

- The next two lessons use sums to count: [permutations and combinations](03-counting-permutations-combinations.md) adds up cases, and the [binomial theorem](04-binomial-theorem.md) is a sum with a count in every term. Proofs of formulas like the ones here are practice for [mathematical induction](../../04-proofs-and-logic/05-induction/01-mathematical-induction.md).
- Algorithm analysis is mostly sums: counting loop steps (sums and closed forms<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md -->), the cost of a divide-and-conquer algorithm and the amortized cost of a dynamic array are all arithmetic or geometric series.
- In finance, the future value of regular deposits is a geometric series, and so are the present value of an annuity and the balance of a loan (annuities and geometric series<!-- link: ../../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md -->). In economics, the spending multiplier is an infinite geometric series with ratio equal to the share of income that gets spent again (multipliers and the AD-AS model<!-- link: ../../07-economics-math/04-more-tools/02-multipliers-and-the-ad-as-model.md -->).
