# Sums and closed forms

After this lesson you can find a closed form for a sum by the perturbation method or by telescoping, bound a sum between two integrals, show that the harmonic numbers grow like $\ln n$, swap the order of a double sum, and turn a nested loop into a sum and then into a count.

Before this: [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md), [mathematical induction](../../04-proofs-and-logic/05-induction/01-mathematical-induction.md) and [Riemann sums and the definite integral](../../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Evaluate $\sum_{k=1}^{99} \frac{1}{k(k+1)}$. (Hint: $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$.)
2. How many times does `count += 1` run when $n = 10$?

    ```python
    for i in range(n):
        for j in range(i, n):
            count += 1
    ```

3. Use $\ln 1000 \approx 6.908$ to guess the size of $1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{1000}$ to within 1.

<details class="solution" markdown>
<summary>Answers</summary>

1. Each term is $\frac{1}{k} - \frac{1}{k+1}$, so the terms cancel in pairs and only the first and last survive: $1 - \frac{1}{100} = \frac{99}{100}$.
2. The inner loop runs $n - i$ times, so the count is $10 + 9 + \cdots + 1 = 55$, which is $\frac{n(n+1)}{2}$.
3. The sum is about $\ln 1000$ plus something below 1. The exact value is $7.485\ldots$, so a good guess is "a bit more than 7".

</details>

## The idea

The cost of a loop is a sum. If the inner loop of a double loop runs $i$ times on pass $i$, the total number of steps is $1 + 2 + \cdots + n$. If a loop halves a number each time and does work proportional to the number, the total is $n + \frac{n}{2} + \frac{n}{4} + \cdots$. The previous lessons gave formulas for the sums that come up most: arithmetic, geometric, and the sums of $k$, $k^2$ and $k^3$.

This lesson is about what to do when the sum in front of you is not on that list. There are three moves. You can find an exact formula, a **closed form**, by a method that works for a whole family of sums. You can skip the exact formula and trap the sum between two integrals, which is often all an algorithm analysis needs. Or you can change the order in which you add, which turns a hard sum into an easy one.

The most useful sum without a closed form is $1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}$. It appears in the average cost of quicksort, in a loop that visits multiples, and in the coupon collector problem. We will not find a formula for it, but we will pin it down: it grows like $\ln n$, slowly but without limit.

## Definitions

A **closed form** for a sum $S_n = \sum_{k=0}^{n} a_k$ is an expression for $S_n$ in terms of $n$ that uses a fixed number of operations, whatever $n$ is: powers, products, quotients and sums of a fixed size, with no summation sign and no "$\cdots$". For example, $\frac{n(n+1)}{2}$ is a closed form for $1 + 2 + \cdots + n$.

In plain words, a closed form is a formula you can evaluate in a few steps, where the sum itself takes $n$ steps. "Fixed number of operations" is a judgement call; a power such as $2^n$ counts as one operation, and a sum with $n$ terms does not.

The **$n$-th harmonic number** is

$$
H_n = \sum_{k=1}^{n} \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n}.
$$

In plain words, $H_n$ is the total of the reciprocals of the first $n$ positive integers. A few values: $H_1 = 1$, $H_2 = 1.5$, $H_3 = 1.8333\ldots$ and $H_{10} = 2.929\ldots$. There is no simpler formula for $H_n$ in terms of $n$; the symbol $H_n$ is itself the standard name for it.

A **double sum** is a sum of sums, written $\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij}$. The inner sum is worked out first for each fixed $i$, and the outer sum adds the results. In plain words, it adds up a table of numbers row by row.

We write $f(n) \sim g(n)$, read "$f$ is **asymptotically equal** to $g$", when $\dfrac{f(n)}{g(n)} \to 1$ as $n \to \infty$. In plain words, the two functions are close in relative terms: the ratio gets as near to 1 as you like. For example, $n^2 + n \sim n^2$, because $\frac{n^2 + n}{n^2} = 1 + \frac{1}{n} \to 1$. Note that $\sim$ does not mean the difference is small: $n^2 + n$ and $n^2$ differ by $n$, which grows.

A sequence $(a_k)$ is **nondecreasing** if $a_k \le a_{k+1}$ for every $k$, and **nonincreasing** if $a_k \ge a_{k+1}$ for every $k$. The same words describe a function $f$ on an interval: $f$ is nondecreasing if $x \le y$ implies $f(x) \le f(y)$. The function $\frac{1}{x}$ is nonincreasing for $x > 0$ and $\ln x$ is nondecreasing.

## How to do it

### The sums you already have

The table collects the closed forms from [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md) and from the induction lessons. Every method below reduces a new sum to these.

| Sum | Closed form |
|---|---|
| $\sum_{k=1}^{n} 1$ | $n$ |
| $\sum_{k=1}^{n} k$ | $\frac{n(n+1)}{2}$ |
| $\sum_{k=1}^{n} k^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $\sum_{k=1}^{n} k^3$ | $\left(\frac{n(n+1)}{2}\right)^2$ |
| $\sum_{k=0}^{n} r^k$, for $r \ne 1$ | $\frac{r^{n+1} - 1}{r - 1}$ |
| $\sum_{k=0}^{\infty} r^k$, for $\lvert r \rvert < 1$ | $\frac{1}{1 - r}$ |

For a sum of an arithmetic sequence, "the number of terms times the average of the first and last" is the fastest form. For a geometric sum, remember it as "last term times $r$, minus first term, over $r - 1$". With $r = 2$ this is $1 + 2 + 4 + \cdots + 2^n = 2^{n+1} - 1$, the largest number with $n + 1$ bits.

### The perturbation method

The geometric proof in the earlier lesson multiplies the sum by $r$ and subtracts. The **perturbation method** does the same thing in a form that also works for sums that aren't geometric. The idea is to write the sum of $n + 2$ terms in two ways, and to let the sum $S_n$ show up on both sides so you can solve for it.

1. Name the sum: $S_n = \sum_{k=0}^{n} a_k$.
2. Write the sum $a_0 + a_1 + \cdots + a_{n+1}$ two ways. Peeling off the last term gives $S_n + a_{n+1}$. Peeling off the first term gives $a_0 + \sum_{k=0}^{n} a_{k+1}$. So $S_n + a_{n+1} = a_0 + \sum_{k=0}^{n} a_{k+1}$.
3. Rewrite $a_{k+1}$ using the pattern of $a_k$, until the right-hand sum is made of $S_n$ and sums you already know.
4. Solve the equation for $S_n$.
5. Check $n = 0$, $1$ and $2$ by hand. If you want a proof, confirm the formula by induction.

Why it works: both sides add the same $n + 2$ numbers, so they are equal, and this holds for every sequence. The method only pays off when step 3 brings $S_n$ back.

<div class="warning" markdown>

Watch out at step 4: sometimes $S_n$ cancels from both sides and you are left with a true statement like $0 = 0$, or with a formula for a simpler sum. That is not a failure of the algebra. It means the perturbation used the wrong power. To get $\sum k^2$, perturb $\sum k^3$, and to get $\sum k^3$, perturb $\sum k^4$.

</div>

### Telescoping

A sum **telescopes** when the terms cancel in pairs. If you can write the summand as a difference $g(k+1) - g(k)$, then

$$
\sum_{k=m}^{n} \bigl(g(k+1) - g(k)\bigr) = g(n+1) - g(m),
$$

which is proved in the earlier lesson by shifting one of the two sums. The method:

1. Rewrite the summand as $g(k+1) - g(k)$ for some function $g$. For a fraction, use partial fractions: $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$. For a product of consecutive factors, use a "falling product": $k(k+1)(k+2)$ is a difference of $(k-1)k(k+1)(k+2)$ and $k(k+1)(k+2)(k+3)$, up to a constant.
2. Add. Everything cancels except $g(n+1)$ and $g(m)$.
3. Check with $n = m$ (one term) and one more value.

Telescoping gives the sum of squares in two lines. Since $k^2 = k(k+1) - k$ and $k(k+1) = \frac{1}{3}\bigl[k(k+1)(k+2) - (k-1)k(k+1)\bigr]$, the first part telescopes:

$$
\sum_{k=1}^{n} k(k+1) = \frac{n(n+1)(n+2)}{3}, \qquad \text{so} \qquad \sum_{k=1}^{n} k^2 = \frac{n(n+1)(n+2)}{3} - \frac{n(n+1)}{2} = \frac{n(n+1)(2n+1)}{6}.
$$

(The first term of the telescoping sum, $g(1) = 0 \cdot 1 \cdot 2 = 0$, vanishes.) This is a third proof of the sum of squares, after the telescoping of cubes and the induction proof.

### Harmonic numbers and the integral bound

*Theorem.* For every integer $n \ge 1$,

$$
\ln(n+1) \le H_n \le 1 + \ln n.
$$

So $H_n \sim \ln n$.

We know that $\int_k^{k+1} \frac{dx}{x} = \ln(k+1) - \ln k$ and that $\frac{1}{x}$ is nonincreasing, so on the interval from $k$ to $k + 1$ the function is never above $\frac{1}{k}$ and never below $\frac{1}{k+1}$. We want to trap $H_n$ between logarithms. The plan is to compare each term $\frac{1}{k}$ with the area under the curve over a width-1 interval, and add up.

*Proof.* The interval $[k, k+1]$ has width 1, and on it $\frac{1}{k+1} \le \frac{1}{x} \le \frac{1}{k}$. Integrating over the interval, the area under $\frac{1}{x}$ lies between the areas of the lower and upper rectangles:

$$
\frac{1}{k+1} \le \int_k^{k+1} \frac{dx}{x} \le \frac{1}{k}.
$$

For the lower bound on $H_n$, add the right inequality for $k = 1, \dots, n$. The integrals join into one: $\sum_{k=1}^{n} \int_k^{k+1} \frac{dx}{x} = \int_1^{n+1} \frac{dx}{x} = \ln(n+1)$. So $\ln(n+1) \le H_n$.

For the upper bound, add the left inequality for $k = 1, \dots, n-1$. The left sides add to $\frac{1}{2} + \cdots + \frac{1}{n} = H_n - 1$, and the integrals join into $\int_1^n \frac{dx}{x} = \ln n$. So $H_n - 1 \le \ln n$.

Finally, divide the two bounds by $\ln n$: $\frac{\ln(n+1)}{\ln n} \le \frac{H_n}{\ln n} \le \frac{1}{\ln n} + 1$. Both ends tend to 1 (since $\ln(n+1) = \ln n + \ln(1 + \frac{1}{n})$ and the last term tends to 0), so by the squeeze theorem $\frac{H_n}{\ln n} \to 1$. $\blacksquare$

Look back: the figure shows the two bounds as two sets of rectangles, here for $n = 7$. On the left, the rectangles of height $\frac{1}{k}$ stick out above the curve, and their total area $H_7$ is more than the area $\ln 8$ under the curve. On the right, the rectangles of height $\frac{1}{k+1}$ sit under the curve, and their total area $H_8 - 1$ is less than the area under the curve from 1 to 8. The extra "$1+$" in the upper bound is the first rectangle, which has to be dropped so that the rest fit under the curve.

![Two graphs of y = 1 over x from x = 1 to x = 8. On the left, seven rectangles of width 1 with heights 1, 1/2, up to 1/7 stand on the intervals from k to k+1 and reach up to the curve at their left corners, so they stick out above it; their total area is H_7, and the area under the curve from 1 to 8 is ln 8. On the right, seven rectangles have heights 1/2, 1/3, up to 1/8 and sit under the curve; their total area is H_8 minus 1.](../../assets/figures/06-cs-math/sums-and-closed-forms-harmonic.svg)

| $n$ | $\ln(n+1)$ | $H_n$ | $1 + \ln n$ | $H_n - \ln n$ |
|---|---|---|---|---|
| 10 | 2.398 | 2.929 | 3.303 | 0.626 |
| 100 | 4.615 | 5.187 | 5.605 | 0.582 |
| 1,000 | 6.909 | 7.485 | 7.908 | 0.578 |
| 1,000,000 | 13.816 | 14.393 | 14.816 | 0.577 |

The last column suggests that $H_n - \ln n$ settles near $0.5772$, which is true (Euler's constant) but needs calculus beyond this book to prove. The bounds alone say the difference is between 0 and 1.

Two consequences matter. The harmonic numbers never stop growing: since $H_n \ge \ln(n+1)$, they pass any number you choose, though slowly. To pass 10 you need $n = 12{,}367$ terms. And $\ln n$ is a good everyday estimate: $H_n \approx \ln n + 0.58$.

### Bounding a sum by integrals

The argument for $H_n$ works for any monotonic function. Each term $f(k)$ is the area of a rectangle of width 1, and a monotonic $f$ keeps that rectangle on one side of the curve.

*Theorem.* Let $m \le n$ be integers and let $f$ be defined on the interval $[m-1, n+1]$.

- If $f$ is nondecreasing, then $\displaystyle\int_{m-1}^{n} f(x)\,dx \le \sum_{k=m}^{n} f(k) \le \int_{m}^{n+1} f(x)\,dx$.
- If $f$ is nonincreasing, then $\displaystyle\int_{m}^{n+1} f(x)\,dx \le \sum_{k=m}^{n} f(k) \le \int_{m-1}^{n} f(x)\,dx$.

*Proof.* Suppose $f$ is nondecreasing. On the interval $[k-1, k]$ the function is at most $f(k)$, so $\int_{k-1}^{k} f \le f(k)$. On $[k, k+1]$ it is at least $f(k)$, so $f(k) \le \int_{k}^{k+1} f$. Add the first inequality for $k = m, \dots, n$ and the second likewise; the integrals join into single integrals. The nonincreasing case reverses both inequalities. $\blacksquare$

The method, for a sum of a positive monotonic function:

1. Decide whether $f$ is nondecreasing or nonincreasing on the range of the sum.
2. Write the two integrals from the theorem, with the endpoints in the right places.
3. Evaluate the integrals. For a nondecreasing $f$ the two bounds differ by at most $f(n+1) - f(m-1)$ (the same quantity, reversed, for a nonincreasing $f$), so the sum is pinned down to within about one large term.
4. Check the bounds with a small $n$ against the actual sum.

<div class="warning" markdown>

Watch out at step 2: the endpoints are different for the two bounds, and they flip when the direction of $f$ flips. A common slip is to use $\int_1^n$ for both bounds. With $f(x) = x^2$ and $n = 100$ the two correct integrals are $\int_0^{100} x^2\,dx = 333{,}333$ and $\int_1^{101} x^2\,dx = 343{,}433$, and the true sum $338{,}350$ lies between them. Using $\int_1^{100} x^2\,dx \approx 333{,}333$ as an upper bound would claim that the sum is at most 333,333, which is false.

</div>

## Worked examples

<div class="example" markdown>

### Example 1: a sum that is not on the list, by perturbation

Find a closed form for $S_n = \sum_{k=0}^{n} k\,2^k$.

Step 1: name the sum: $S_n = 0 + 2 + 8 + 24 + \cdots + n\,2^n$.

Step 2: here $a_k = k\,2^k$, so $a_0 = 0$ and $a_{n+1} = (n+1)2^{n+1}$. Writing the $n + 2$ term sum two ways gives

$$
S_n + (n+1)2^{n+1} = \sum_{k=0}^{n} (k+1)\,2^{k+1}.
$$

Step 3: pull the factor 2 out of the right side and split $k + 1$ into two parts. The part with $k$ is $S_n$ again, and the part with 1 is a geometric sum:

$$
\sum_{k=0}^{n} (k+1)\,2^{k+1} = 2\sum_{k=0}^{n} k\,2^k + 2\sum_{k=0}^{n} 2^k = 2S_n + 2\bigl(2^{n+1} - 1\bigr).
$$

Step 4: put the two sides together and solve. From $S_n + (n+1)2^{n+1} = 2S_n + 2^{n+2} - 2$ we get

$$
S_n = (n+1)2^{n+1} - 2^{n+2} + 2 = (n-1)\,2^{n+1} + 2.
$$

Step 5, the check: $n = 0$ gives $(-1) \cdot 2 + 2 = 0$, which is the sum $0$. For $n = 1$ the formula gives $0 + 2 = 2$, and the sum is $0 + 2 = 2$. For $n = 3$ the sum is $0 + 2 + 8 + 24 = 34$ and the formula gives $2 \cdot 16 + 2 = 34$.

</div>

<div class="example" markdown>

### Example 2: telescoping

Find $\sum_{k=1}^{n} \frac{1}{k(k+2)}$.

Step 1: partial fractions give $\frac{1}{k(k+2)} = \frac{1}{2}\left(\frac{1}{k} - \frac{1}{k+2}\right)$. The two parts are two steps apart, so the cancelling is every other term and two terms survive at each end.

Step 2: write out the first few terms of $\frac{1}{2}\left(\frac{1}{k} - \frac{1}{k+2}\right)$ for $k = 1, 2, 3, 4, \dots$ inside the bracket: $\left(1 - \frac{1}{3}\right) + \left(\frac{1}{2} - \frac{1}{4}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \cdots$. The $-\frac{1}{3}$ cancels the next-but-one $+\frac{1}{3}$, and so on. What is left is the first two positive terms and the last two negative ones:

$$
\sum_{k=1}^{n} \frac{1}{k(k+2)} = \frac{1}{2}\left(1 + \frac{1}{2} - \frac{1}{n+1} - \frac{1}{n+2}\right).
$$

Step 3, the check: $n = 1$ gives $\frac{1}{2}\left(\frac{3}{2} - \frac{1}{2} - \frac{1}{3}\right) = \frac{1}{3}$, and the sum is $\frac{1}{1 \cdot 3} = \frac{1}{3}$. For $n = 2$ the sum is $\frac{1}{3} + \frac{1}{8} = \frac{11}{24}$, and the formula gives $\frac{1}{2}\left(\frac{3}{2} - \frac{1}{3} - \frac{1}{4}\right) = \frac{1}{2} \cdot \frac{11}{12} = \frac{11}{24}$.

As $n$ grows the formula approaches $\frac{3}{4}$, so the infinite series $\sum_{k=1}^{\infty} \frac{1}{k(k+2)}$ converges to $\frac{3}{4}$.

</div>

<div class="example" markdown>

### Example 3: counting the steps of nested loops

Find the number of times `work()` is called, as a function of $n$.

```python
for i in range(n):                  # loop A
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            work()

i = n                               # loop B
while i >= 1:
    for j in range(i):
        work()
    i //= 2
```

For loop A, the innermost loop runs $n - 1 - j$ times, and the middle loop adds that up over $j$. The number of calls is $\sum_{i=0}^{n-1} \sum_{j=i+1}^{n-1} (n - 1 - j)$. The inner double sum counts the pairs $j < k$ among the $n - 1 - i$ values after $i$, which is $\frac{(n-1-i)(n-2-i)}{2}$. Adding over $i$ and writing $m = n - 1 - i$, which runs from $n - 1$ down to 0:

$$
\sum_{m=0}^{n-1} \frac{m(m-1)}{2} = \frac{1}{2}\sum_{m=1}^{n-1} (m-1)m = \frac{1}{2} \cdot \frac{(n-2)(n-1)n}{3} = \frac{n(n-1)(n-2)}{6}.
$$

This used $\sum_{m=1}^{N}(m-1)m = \frac{(N-1)N(N+1)}{3}$ with $N = n - 1$, from the telescoping above. It is the number of ways to choose 3 of $n$ positions in increasing order, which the lesson on [permutations and combinations](../03-counting-and-discrete-probability/02-permutations-and-combinations.md) writes $\binom{n}{3}$. For $n = 5$ the loops visit $(i, j, k)$ = (0,1,2), (0,1,3), (0,1,4), (0,2,3), (0,2,4), (0,3,4), (1,2,3), (1,2,4), (1,3,4), (2,3,4): 10 triples, and $\frac{5 \cdot 4 \cdot 3}{6} = 10$.

For loop B, $i$ takes the values $n, \lfloor n/2 \rfloor, \lfloor n/4 \rfloor, \dots, 1$ and the inner loop runs $i$ times. If $n = 2^t$ the total is the geometric sum $2^t + 2^{t-1} + \cdots + 1 = 2^{t+1} - 1 = 2n - 1$. For $n = 1024$ that is 2,047. For other $n$ each term is rounded down, so the total is at most $n \sum_{s \ge 0} 2^{-s} = 2n$. The loop is linear, not $n \lg n$: the number of passes is $\lg n$, but most of the work is in the first pass.

</div>

<div class="example" markdown>

### Example 4: a loop with harmonic cost

How many times does the body run?

```python
total = 0
for i in range(1, n + 1):
    j = i
    while j <= n:
        total += 1
        j += i
```

For a fixed $i$, the variable $j$ takes the values $i, 2i, 3i, \dots$ up to $n$, so the body runs $\lfloor n/i \rfloor$ times. The total is $S = \sum_{i=1}^{n} \lfloor n/i \rfloor$. Each floor is within 1 below $\frac{n}{i}$, so $\frac{n}{i} - 1 < \lfloor n/i \rfloor \le \frac{n}{i}$. Adding over $i$:

$$
n H_n - n < S \le n H_n.
$$

By the harmonic bound, $S$ is between about $n \ln n - n$ and $n \ln n + n$. For $n = 100$ the bounds are $418.7 < S \le 518.7$, and the loop really runs $S = 482$ times. For $n = 1000$ the loop runs 7,069 times and the bounds are $6485 < S \le 7486$. A simple sieve of Eratosthenes has this shape: it crosses off the multiples of each number $i$ in turn. (The usual sieve runs only for prime $i$ and starts at $i^2$, which is cheaper, about $n \ln \ln n$ steps.)

Check: the number $S$ counts pairs $(i, j)$ with $i$ dividing $j$ and $j \le n$. Counting by $j$ instead of $i$ gives $\sum_{j=1}^{n} d(j)$, the total number of divisors. For $n = 4$: the divisor counts of $1, 2, 3, 4$ are $1, 2, 2, 3$, total 8, and $\lfloor 4/1 \rfloor + \lfloor 4/2 \rfloor + \lfloor 4/3 \rfloor + \lfloor 4/4 \rfloor = 4 + 2 + 1 + 1 = 8$.

</div>

<div class="example" markdown>

### Example 5: bounds for $\ln n!$

Since $\ln n! = \sum_{k=2}^{n} \ln k$ (the term $\ln 1$ is 0) and $\ln x$ is nondecreasing, the integral bounds with $m = 2$ give

$$
\int_1^{n} \ln x\,dx \le \ln n! \le \int_2^{n+1} \ln x\,dx \le \int_1^{n+1} \ln x\,dx.
$$

The last step holds because $\ln x \ge 0$ on $[1, 2]$. An antiderivative of $\ln x$ is $x \ln x - x$; check by differentiating, which gives $\ln x + 1 - 1 = \ln x$. Evaluating,

$$
n \ln n - n + 1 \le \ln n! \le (n+1)\ln(n+1) - n.
$$

For $n = 10$, $\ln 10! = 15.104$ and the bounds are $14.026$ and $16.377$. For $n = 100$ the value is $363.74$ and the bounds are $361.52$ and $366.13$. So $\ln n! \sim n \ln n$.

This is the counting argument for sorting. To pick the right one of the $n!$ orderings of $n$ items by yes-or-no comparisons, you need at least $\lceil \lg n! \rceil$ questions, and $\lg n! = \frac{\ln n!}{\ln 2}$ grows like $n \lg n$. For $n = 10$ that is $\lceil 21.79 \rceil = 22$ comparisons at least. [Asymptotic notation](04-asymptotic-notation.md) uses this bound.

Check: $10! = 3{,}628{,}800$ and $\ln 3{,}628{,}800 = 15.104$.

</div>

<div class="example" markdown>

### Example 6: $\sum k\,3^k$ (finish it yourself)

Use the perturbation method to find $S_n = \sum_{k=0}^{n} k\,3^k$. The first steps are done.

Step 2: $S_n + (n+1)3^{n+1} = \sum_{k=0}^{n} (k+1)3^{k+1}$.

Step 3: the right side is $3\sum k\,3^k + 3\sum 3^k = 3S_n + 3 \cdot \frac{3^{n+1} - 1}{2}$.

Solve for $S_n$ and check with $n = 0, 1, 2$.

<details class="solution" markdown>
<summary>Finish</summary>

Step 4: from $S_n + (n+1)3^{n+1} = 3S_n + \frac{3}{2}\left(3^{n+1} - 1\right)$ we get

$$
2S_n = (n+1)3^{n+1} - \frac{3^{n+2} - 3}{2} = \frac{(2n+2)3^{n+1} - 3 \cdot 3^{n+1} + 3}{2} = \frac{(2n-1)3^{n+1} + 3}{2},
$$

so $S_n = \frac{(2n-1)\,3^{n+1} + 3}{4}$.

Step 5, the check: $n = 0$ gives $\frac{-3 + 3}{4} = 0$. $n = 1$ gives $\frac{9 + 3}{4} = 3$, and the sum is $0 + 3 = 3$. $n = 2$ gives $\frac{81 + 3}{4} = 21$, and the sum is $0 + 3 + 18 = 21$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out when you swap the order of a triangular double sum without changing the bounds. In $\sum_{i=1}^{n} \sum_{j=1}^{i} a_{ij}$ the inner bound depends on $i$. Swapping the two sigmas and keeping the bounds gives nonsense. The pairs are $1 \le j \le i \le n$, and reading them by columns gives $\sum_{j=1}^{n} \sum_{i=j}^{n} a_{ij}$. For a grid whose bounds don't depend on each other, such as $\sum_{i=1}^{m} \sum_{j=1}^{n}$, you can swap freely.

</div>

<div class="warning" markdown>

Watch out for the number of terms in a loop sum. `for j in range(i, n)` runs $n - i$ times, not $n - i + 1$, because `range` stops before its upper end. `range(1, n + 1)` runs $n$ times. Write the loop as a sum with the exact bounds, then count the terms as (last $-$ first $+ 1$) before using a formula.

</div>

<div class="warning" markdown>

Watch out for treating $H_n$ as $\ln n$. The bounds say $H_n$ is within 1 of $\ln n$, and in fact about $0.58$ above it. For a statement about growth, $H_n \sim \ln n$ is right. For an exact count, such as the work of the loop in Example 4, the extra $0.58\,n$ is part of the answer. It does not matter for large $n$ but does for $n = 100$.

</div>

<div class="warning" markdown>

Watch out for a closed form that was only tested on one value. A formula can match at $n = 1$ and fail everywhere else. Test at $n = 0$ (the empty sum is 0), $n = 1$, $n = 2$ and one larger value. Two cubic polynomials that agree at four values are the same polynomial, so if you expect a cubic, four matching values are strong evidence, and a proof by induction settles it.

</div>

Some small cases. An empty sum is 0, so the formulas in this lesson should give 0 at the lower end: $S_0$ for $\sum_{k=0}^{n}$ may be one term, and $\sum_{k=1}^{0}$ is empty. The harmonic bound needs $n \ge 1$, since $\ln 0$ is not defined. When the summand can be negative the integral bounds don't apply as stated; split the sum into the positive and negative parts first.

## Tricks and shortcuts

- A closed form for a sum of $k^p$ is a polynomial in $n$ of degree $p + 1$, so you can find it from $p + 2$ values: fit a polynomial through the values at $n = 0, 1, \dots$, then prove it by induction. For $\sum k$, the values $0, 1, 3$ fit $\frac{n^2 + n}{2}$.
- A difference test: a formula $F(n)$ is right for $\sum_{k=1}^{n} a_k$ exactly when $F(0) = 0$ and $F(n) - F(n-1) = a_n$ for every $n$. For $F(n) = (n-1)2^{n+1} + 2$ in Example 1 (with $F(0) = 0$): $F(n) - F(n-1) = (n-1)2^{n+1} - (n-2)2^n = 2^n(2n - 2 - n + 2) = n\,2^n$. That is the induction step in one line.
- To estimate a sum before computing it, replace it by an integral. $\sum_{k=1}^{n} k^2 \approx \int_0^n x^2\,dx = \frac{n^3}{3}$, which is the leading term of the closed form. The error is of lower order.
- Sums with a doubling or halving index are geometric, so they are dominated by their largest term: $1 + 2 + 4 + \cdots + 2^t < 2 \cdot 2^t$.
- $\sum_{k=1}^{n} \ln k = \ln(n!)$, so sums of logarithms are logarithms of products. Example 5 uses it.

## In code

The first part checks the closed forms with exact arithmetic. The second part shows $H_n$ between its bounds and the loop count of Example 4.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
from fractions import Fraction

# closed forms, checked for every n from 0 to 19
for n in range(20):
    assert sum(k * 2**k for k in range(n + 1)) == (n - 1) * 2**(n + 1) + 2
    assert 4 * sum(k * 3**k for k in range(n + 1)) == (2 * n - 1) * 3**(n + 1) + 3
for n in range(1, 20):
    left = sum(Fraction(1, k * (k + 2)) for k in range(1, n + 1))
    right = Fraction(1, 2) * (Fraction(3, 2) - Fraction(1, n + 1) - Fraction(1, n + 2))
    assert left == right
print("closed forms agree")                       # closed forms agree

def H(n):
    return sum(1 / k for k in range(1, n + 1))

for n in (10, 100, 1000):
    print(n, round(math.log(n + 1), 3), round(H(n), 3), round(1 + math.log(n), 3))
# 10 2.398 2.929 3.303
# 100 4.615 5.187 5.605
# 1000 6.909 7.485 7.908

def steps(n):                                      # Example 4, counted
    total = 0
    for i in range(1, n + 1):
        j = i
        while j <= n:
            total += 1
            j += i
    return total

n = 100
print(steps(n), sum(n // i for i in range(1, n + 1)))   # 482 482
print(round(n * H(n) - n, 1), round(n * H(n), 1))       # 418.7 518.7

t, k = 0, 0                                        # when does H pass 10?
while t <= 10:
    k += 1
    t += 1 / k
print(k)                                           # 12367
```

The `assert` lines test the formulas at 20 values each, which is evidence and not a proof; the induction or perturbation argument is what makes them true for every $n$.

</details>

## FAQ

### Why does a logarithm show up in a sum of fractions?

Because $\ln$ is defined as the area under $\frac{1}{x}$, and a sum of $\frac{1}{k}$ is an estimate of that area by rectangles. Where the terms $\frac{1}{k}$ shrink slowly, the sum has to behave like the integral, which is $\ln n$. The same comparison with $\frac{1}{x^2}$ gives something different: $\int_1^n \frac{dx}{x^2} = 1 - \frac{1}{n} < 1$, so $\sum_{k=1}^{n} \frac{1}{k^2} \le 2 - \frac{1}{n}$ stays bounded. Terms $\frac{1}{k}$ add up to something unbounded and terms $\frac{1}{k^2}$ don't.

### Why isn't there a closed form for $H_n$?

There is no formula built from a fixed number of the usual operations that equals $H_n$ for every $n$, although proving that takes more algebra than this book uses. In practice it doesn't matter: the bounds $\ln(n+1) \le H_n \le 1 + \ln n$ are accurate enough for algorithm analysis, and the exact value is cheap to compute by a loop.

### How do I know which method to try?

Look at the shape. A power times a geometric term, such as $k^2 2^k$, suggests perturbation. A fraction of consecutive factors, such as $\frac{1}{k(k+1)}$, suggests telescoping. A polynomial in $k$ is a combination of the table sums. A function like $\frac{1}{k}$ or $\ln k$ that has no closed form suggests integral bounds. If a double sum has an awkward inner bound, try swapping the order.

### Does the integral bound work for $\sum \sqrt{k}$ and $\sum \ln k$?

Yes, since both functions are nondecreasing for $x \ge 1$. Practice problem 5 does $\sum \sqrt{k}$, and Example 5 does $\ln k$.

### Why do the bounds in Example 5 start the sum at 2?

Because the theorem needs the function defined on $[m-1, n+1]$, and $\ln x$ is not defined at 0. The term $\ln 1$ is 0, so dropping it from the sum changes nothing, and starting at $m = 2$ keeps the integrals on $[1, n+1]$.

## Practice

### Warm-up

1\. Evaluate (a) $\sum_{k=0}^{10} 3 \cdot 2^k$ and (b) $\sum_{k=1}^{50} (2k - 1)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) A geometric sum with first term 3, ratio 2 and 11 terms: $3 \cdot (2^{11} - 1) = 3 \cdot 2047 = 6141$.

(b) The sum of the first $n$ odd numbers is $n^2$ (from linearity: $2 \cdot \frac{n(n+1)}{2} - n = n^2$), so the answer is $50^2 = 2500$.

Check: (a) the largest term is $3 \cdot 1024 = 3072$, and the sum should be a little under twice that, which 6141 is. (b) The average of the first and last terms is $\frac{1 + 99}{2} = 50$, times 50 terms.

</details>

2\. Evaluate $\sum_{k=2}^{10} \frac{1}{k^2 - 1}$ by telescoping.

<details class="solution" markdown>
<summary>Solution</summary>

Since $k^2 - 1 = (k-1)(k+1)$, partial fractions give $\frac{1}{k^2-1} = \frac{1}{2}\left(\frac{1}{k-1} - \frac{1}{k+1}\right)$. Writing out the terms from $k = 2$ to $10$, the values $\frac{1}{3}, \dots, \frac{1}{9}$ cancel, and what is left is

$$
\frac{1}{2}\left(1 + \frac{1}{2} - \frac{1}{10} - \frac{1}{11}\right) = \frac{1}{2} \cdot \frac{165 - 11 - 10}{110} = \frac{1}{2} \cdot \frac{144}{110} = \frac{36}{55}.
$$

Check: the first term is $\frac{1}{3} = 0.3333$, and the sum of all nine terms in Python with `Fraction` is exactly $\frac{36}{55} \approx 0.6545$.

</details>

3\. How many times does `count += 1` run, as a formula in $n$, in each loop? Give the number for $n = 6$.

```python
for i in range(n):                    # (a)
    for j in range(i):
        count += 1

for i in range(1, n + 1):             # (b)
    for j in range(i, n + 1):
        count += 1
```

<details class="solution" markdown>
<summary>Solution</summary>

(a) The inner loop runs $i$ times, for $i = 0, 1, \dots, n-1$: $0 + 1 + \cdots + (n-1) = \frac{n(n-1)}{2}$. For $n = 6$ that is 15.

(b) The inner loop runs $n - i + 1$ times, for $i = 1, \dots, n$: $n + (n-1) + \cdots + 1 = \frac{n(n+1)}{2}$. For $n = 6$ that is 21.

Check: counting by hand for $n = 6$ in (a) gives $0 + 1 + 2 + 3 + 4 + 5 = 15$, and in (b) $6 + 5 + 4 + 3 + 2 + 1 = 21$.

</details>

### Standard

4\. Prove that $\sum_{k=1}^{n} k(k+1)(k+2) = \frac{n(n+1)(n+2)(n+3)}{4}$ by telescoping, and evaluate it for $n = 10$.

<details class="solution" markdown>
<summary>Solution</summary>

Let $g(k) = (k-1)k(k+1)(k+2)$. Then $g(k+1) - g(k) = k(k+1)(k+2)(k+3) - (k-1)k(k+1)(k+2) = k(k+1)(k+2)\bigl[(k+3) - (k-1)\bigr] = 4k(k+1)(k+2)$.

So $k(k+1)(k+2) = \frac{1}{4}\bigl(g(k+1) - g(k)\bigr)$, and the sum telescopes to $\frac{1}{4}\bigl(g(n+1) - g(1)\bigr)$. Since $g(1) = 0$ and $g(n+1) = n(n+1)(n+2)(n+3)$, the sum is $\frac{n(n+1)(n+2)(n+3)}{4}$.

For $n = 10$: $\frac{10 \cdot 11 \cdot 12 \cdot 13}{4} = \frac{17160}{4} = 4290$.

Check with $n = 2$: $1 \cdot 2 \cdot 3 + 2 \cdot 3 \cdot 4 = 6 + 24 = 30$, and $\frac{2 \cdot 3 \cdot 4 \cdot 5}{4} = 30$.

</details>

5\. (a) Bound $\sum_{k=1}^{100} \sqrt{k}$ between two integrals. (b) How far apart are the bounds, and how close is the true value, $671.46$?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The function $\sqrt{x}$ is nondecreasing, so with $m = 1$ and $n = 100$: $\int_0^{100} \sqrt{x}\,dx \le \sum_{k=1}^{100} \sqrt{k} \le \int_1^{101} \sqrt{x}\,dx$. An antiderivative of $\sqrt{x}$ is $\frac{2}{3}x^{3/2}$, so the lower bound is $\frac{2}{3} \cdot 1000 = 666.67$ and the upper bound is $\frac{2}{3}\bigl(101^{3/2} - 1\bigr) = \frac{2}{3}(1015.04 - 1) = 676.02$.

(b) The gap is about 9.4, below the bound $f(101) - f(0) = \sqrt{101} \approx 10.05$ from the method, and the true value 671.46 lies inside it, close to the middle.

Check: $666.67 \le 671.46 \le 676.02$.

</details>

6\. A loop does `for i in range(1, n + 1): for j in range(i, n + 1, i): count += 1` with $n = 100$. Find the exact count, and use the harmonic bound to check it.

<details class="solution" markdown>
<summary>Solution</summary>

For a fixed $i$, the variable $j$ takes the values $i, 2i, \dots$ up to $n$, so the inner loop runs $\lfloor 100/i \rfloor$ times. The count is $\sum_{i=1}^{100} \lfloor 100/i \rfloor$. The first terms are $100, 50, 33, 25, 20, 16, 14, 12, 11, 10, \dots$ and the sum of all 100 terms is 482.

The harmonic bound says $nH_n - n < \text{count} \le nH_n$. With $H_{100} = 5.1874$ this is $418.7 < \text{count} \le 518.7$.

Check: $418.7 < 482 \le 518.7$.

</details>

### Challenge

7\. Prove that $\sum_{k=1}^{n} H_k = (n+1)H_n - n$ by writing it as a double sum and swapping the order.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $H_k = \sum_{j=1}^{k} \frac{1}{j}$. What we want: a formula for $\sum_{k=1}^{n} H_k$. The plan: write it as a sum over the pairs $1 \le j \le k \le n$, then add column by column.

$$
\sum_{k=1}^{n} H_k = \sum_{k=1}^{n} \sum_{j=1}^{k} \frac{1}{j} = \sum_{j=1}^{n} \sum_{k=j}^{n} \frac{1}{j}.
$$

The pairs are the same on both sides: $j$ runs from 1 to $n$, and for each $j$, $k$ runs from $j$ to $n$. The inner summand $\frac{1}{j}$ doesn't depend on $k$, and the inner sum has $n - j + 1$ terms, so

$$
\sum_{j=1}^{n} \frac{n - j + 1}{j} = (n+1)\sum_{j=1}^{n} \frac{1}{j} - \sum_{j=1}^{n} \frac{j}{j} = (n+1)H_n - n.
$$

Check with $n = 3$: $H_1 + H_2 + H_3 = 1 + 1.5 + 1.8333 = 4.3333$, and $4 H_3 - 3 = 4 \cdot 1.8333 - 3 = 4.3333$.

</details>

8\. (Reviews [mathematical induction](../../04-proofs-and-logic/05-induction/01-mathematical-induction.md).) Prove that $\sum_{k=1}^{n} k \cdot k! = (n+1)! - 1$ for every $n \ge 1$, once by telescoping and once by induction.

<details class="solution" markdown>
<summary>Solution</summary>

Telescoping: $k \cdot k! = (k+1)\,k! - k! = (k+1)! - k!$. So the sum is $\sum_{k=1}^{n} \bigl((k+1)! - k!\bigr) = (n+1)! - 1! = (n+1)! - 1$.

Induction: for $n = 1$ the left side is $1 \cdot 1! = 1$ and the right side is $2! - 1 = 1$. Suppose the formula holds for $n = j$. Then

$$
\sum_{k=1}^{j+1} k \cdot k! = (j+1)! - 1 + (j+1)(j+1)! = (j+1)!\,\bigl(1 + (j+1)\bigr) - 1 = (j+2)! - 1,
$$

which is the formula for $j + 1$. By induction it holds for every $n \ge 1$.

Check: $n = 3$ gives $1 + 4 + 18 = 23$, and $4! - 1 = 23$.

</details>

## Where this shows up

- The next lesson, [recurrences](02-recurrences.md), solves a recurrence by unrolling it, and the result is always a sum like the ones here. [Asymptotic notation](04-asymptotic-notation.md) gives the language for saying "this sum grows like $n \ln n$" without the exact formula.
- Algorithm analysis: the average number of comparisons in quicksort and the cost of a simple sieve of Eratosthenes each contain $H_n$. In probability, the coupon collector problem (how many random draws to see all $n$ kinds) has expected value $n H_n$; see [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md) for expected values.
- The geometric sum is the engine of finance: [annuities and geometric series](../../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md) is the same sum with an interest rate in the ratio.
