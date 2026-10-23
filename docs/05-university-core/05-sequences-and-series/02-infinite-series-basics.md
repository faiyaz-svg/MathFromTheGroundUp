# Infinite series basics

After this lesson you can say what it means to add infinitely many numbers, decide when a geometric series converges and find its sum, evaluate telescoping series, show that the harmonic series diverges, use the $n$-th term test correctly, and recognize when rearranging terms is unsafe.

Before this: [sequences and their limits](01-sequences-and-their-limits.md), [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md) (sigma notation and the finite geometric sum) and [limits at infinity](../01-limits-and-continuity/01-limits-intuition-and-limit-laws.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find the partial sums $S_1, S_2, S_3$ of $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$ and guess the sum.
2. Find $3 + 1 + \frac{1}{3} + \frac{1}{9} + \cdots$.
3. Does $\displaystyle\sum_{k=1}^{\infty} \frac{k}{k + 1}$ converge?

<details class="solution" markdown>
<summary>Answers</summary>

1. $S_1 = \frac{1}{2}$, $S_2 = \frac{3}{4}$, $S_3 = \frac{7}{8}$. They are $1 - \frac{1}{2^n}$, so the sum is 1.
2. This is geometric with first term 3 and ratio $\frac{1}{3}$, so the sum is $\frac{3}{1 - 1/3} = \frac{9}{2}$.
3. No. The terms $\frac{k}{k + 1}$ tend to 1, not 0, so adding them forever can't settle down. This is the $n$-th term test.

</details>

## The idea

A walker crosses a 1 km path. The first half takes 30 minutes at 1 km/h. The next quarter takes 15 minutes, the next eighth takes 7.5 minutes, and so on, each leg taking half as long as the one before. Zeno's puzzle is that the walker needs infinitely many legs, so surely never arrives. But the times add up as $\frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$ hours, and the walker arrives after exactly one hour.

The sum of infinitely many numbers is not defined by "adding them all up", because that never finishes. It is defined by the partial sums: add the first $n$ terms, then watch what happens as $n$ grows. If the partial sums settle on a number, that number is the sum. If they don't, the series has no sum. The left panel of the figure shows the partial sums of $\frac{1}{2} + \frac{1}{4} + \cdots$ settling on 1, and the right panel shows the partial sums of $1 + \frac{1}{2} + \frac{1}{3} + \cdots$, which look as if they might settle but never do.

![Two panels. Left: the partial sums of one half plus one quarter plus one eighth and so on, plotted as green dots for n from 1 to 10, rising toward the dashed line at 1. Right: the partial sums of 1 plus one half plus one third and so on, plotted as a red staircase for n up to 100, rising slowly and passing the dashed line at 5 when n equals 83, with no sign of levelling off.](../../assets/figures/05-university-core/infinite-series-basics-partial-sums.svg)

The first series can also be seen as area. Cut a unit square in half, then cut one half in half, and keep cutting the remaining piece. The pieces have areas $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \dots$ and fill the square, so they total 1.

![A unit square cut into a left half labelled 1/2, then the right half cut into a bottom quarter labelled 1/4, then the top-right quarter cut into a left eighth labelled 1/8, a bottom-right sixteenth labelled 1/16, and smaller pieces ending in an ellipsis. The caption below reads area 1 in total.](../../assets/figures/05-university-core/infinite-series-basics-geometric-square.svg)

This lesson sets up the definition, handles the series where the partial sums can be found exactly (geometric and telescoping), and proves that the terms shrinking is not enough for convergence. The next lesson gives tests for the series where the partial sums can't be found.

## Definitions

An **infinite series** is an expression $\sum_{k=m}^{\infty} a_k$ built from a sequence $(a_k)$, where $m$ is the first index (usually 0 or 1). Its **partial sums** are $S_n = \sum_{k=m}^{n} a_k = a_m + a_{m+1} + \cdots + a_n$. The series **converges** to $S$ if the sequence of partial sums converges to $S$, that is, if $S_n \to S$ in the epsilon-N sense of the last lesson. We then write $\sum_{k=m}^{\infty} a_k = S$ and call $S$ the **sum** of the series. If $(S_n)$ does not converge, the series **diverges**. In plain words, the sum is the number the running totals approach, if there is one.

The notation $\sum a_k$ stands for two different things, and context says which. It is the series (the process), and when the series converges it is also the number $S$. The statement "$\sum a_k$ converges" is a claim about a limit that may or may not exist, so it must be proved. Dropping the starting index, $\sum a_k$, is common when the index doesn't matter.

A **geometric series** is a series $\sum_{k=0}^{\infty} a r^k = a + ar + ar^2 + \cdots$, with first term $a$ and common ratio $r$. A **telescoping series** is one whose partial sums collapse because consecutive terms cancel, as in $\sum (b_k - b_{k+1})$. The **harmonic series** is $\sum_{k=1}^{\infty} \frac{1}{k} = 1 + \frac{1}{2} + \frac{1}{3} + \cdots$, and its partial sums are the **harmonic numbers** $H_n = 1 + \frac{1}{2} + \cdots + \frac{1}{n}$.

Three facts follow from the definition and the limit laws of sequences, since $S_n$ is a sequence.

- If $\sum a_k = A$ and $\sum b_k = B$, then $\sum (a_k + b_k) = A + B$ and $\sum c\,a_k = cA$ for each constant $c$. The partial sums of the combined series are the combined partial sums.
- Changing, adding or deleting finitely many terms does not change whether the series converges (it may change the sum). The partial sums from some point on differ by a constant.
- The **tail** $\sum_{k=n+1}^{\infty} a_k$ of a convergent series tends to 0 as $n \to \infty$, because it equals $S - S_n$.

## How to do it

### Deciding a series

1. If you can find a formula for the partial sum $S_n$, take its limit as $n \to \infty$. This works for geometric series and for telescoping series.
2. If $a_k$ does not tend to 0, the series diverges by the $n$-th term test below. Check this first, because it is quick.
3. If $a_k \to 0$ and there is no formula for $S_n$, the question is open. Use a convergence test (comparison, integral, ratio and so on), which is the subject of the next lesson, [convergence tests](03-convergence-tests.md).
4. Before moving terms around or splitting a sum, check that the series converges absolutely (or that the splitting is into convergent pieces).

### The geometric series

*Theorem 1.* For $a \ne 0$, the series $\sum_{k=0}^{\infty} a r^k$ converges if and only if $\lvert r \rvert < 1$, and then

$$
\sum_{k=0}^{\infty} a r^k = \frac{a}{1 - r}.
$$

We know the finite formula $S_n = a\,\frac{1 - r^{n+1}}{1 - r}$ for $r \ne 1$ (there are $n + 1$ terms, with exponents 0 to $n$), from the high-school lesson, and that $r^n \to 0$ when $\lvert r \rvert < 1$ ([Theorem 3 of the last lesson](01-sequences-and-their-limits.md#proving-a-limit-from-the-definition)). We want to know when $S_n$ has a limit. The plan is to read it off the formula when $\lvert r \rvert < 1$, and to use the $n$-th term test when $\lvert r \rvert \ge 1$.

*Proof.* Suppose $\lvert r \rvert < 1$. Then $r^{n+1} \to 0$, so $S_n = \frac{a}{1 - r}\left(1 - r^{n+1}\right) \to \frac{a}{1 - r}$ by the limit laws. Now suppose $\lvert r \rvert \ge 1$. Then $\lvert a r^k \rvert = \lvert a \rvert \lvert r \rvert^k \ge \lvert a \rvert > 0$ for every $k$, so the terms do not tend to 0, and the series diverges by Theorem 3 below. $\blacksquare$

Look back: the first term is $a$, the term at $k = 0$. For a series that starts at $k = 1$, such as $\frac{1}{2} + \frac{1}{4} + \cdots = \sum_{k=1}^{\infty}\left(\frac{1}{2}\right)^k$, the first term is $\frac{1}{2}$, so the sum is $\frac{1/2}{1 - 1/2} = 1$. A useful way to remember the formula is $\frac{\text{first term}}{1 - \text{ratio}}$. The formula $\frac{a}{1 - r}$ is a number for every $r \ne 1$, but it is the sum only when $\lvert r \rvert < 1$. The series $1 + 2 + 4 + 8 + \cdots$ diverges even though $\frac{1}{1 - 2} = -1$.

### Telescoping series

*Theorem 2.* If $b_k \to B$, then $\displaystyle\sum_{k=1}^{\infty} (b_k - b_{k+1}) = b_1 - B$. If $(b_k)$ has no limit, the series diverges.

We know the finite telescoping sum $\sum_{k=1}^{n}(b_k - b_{k+1}) = b_1 - b_{n+1}$ from the high-school lesson. We want the limit of the partial sums. The plan is to write $S_n$ using that formula and apply the limit.

*Proof.* The partial sum is $S_n = (b_1 - b_2) + (b_2 - b_3) + \cdots + (b_n - b_{n+1}) = b_1 - b_{n+1}$, since each middle term appears once with each sign. If $b_{n+1} \to B$, then $S_n \to b_1 - B$. If $S_n$ had a limit $S$, then $b_{n+1} = b_1 - S_n$ would too, so $(b_k)$ having no limit forces the series to diverge. $\blacksquare$

Look back: the proof is the whole method, which is to write the term as a difference, cancel, and take a limit. Telescoping can diverge: $\ln\left(1 + \frac{1}{k}\right) = \ln(k + 1) - \ln k$, so the partial sum is $\ln(n + 1)$, which tends to infinity. For fractions, partial fractions (see [partial fractions and improper integrals](../04-integrals/05-partial-fractions-and-improper-integrals.md)) produce the difference. For example, $\frac{1}{k(k + 1)} = \frac{1}{k} - \frac{1}{k + 1}$, so $\sum_{k=1}^{\infty}\frac{1}{k(k + 1)} = 1 - 0 = 1$.

### The $n$-th term test

*Theorem 3 ($n$-th term test).* If $\sum a_k$ converges, then $a_k \to 0$. Equivalently, if $a_k$ does not tend to 0, then $\sum a_k$ diverges.

We know the series converges, so $S_n \to S$. We want $a_n \to 0$. The plan is to write the term as a difference of two consecutive partial sums.

*Proof.* For $n \ge m + 1$, $a_n = S_n - S_{n-1}$. Both $S_n$ and $S_{n-1}$ tend to $S$ (the second is the same sequence shifted by one), so by the difference law $a_n \to S - S = 0$. $\blacksquare$

Look back: this is a test for divergence only. The converse is false, and the next theorem is the standard counterexample. If the terms tend to 0 the test says nothing, and you need another method.

### The harmonic series diverges

*Theorem 4.* The harmonic series $\sum_{k=1}^{\infty}\frac{1}{k}$ diverges. More precisely, $H_{2^m} \ge 1 + \frac{m}{2}$ for every whole number $m \ge 0$.

We know the terms $\frac{1}{k}$ tend to 0, so the $n$-th term test is silent. We want the partial sums to be unbounded. The plan is to group the terms in blocks of lengths $1, 2, 4, 8, \dots$ and show that each block adds up to at least $\frac{1}{2}$, so infinitely many blocks add up to infinity. The grouping picture is the figure: five blocks of bars, each block shaded in one colour.

![A bar chart of the terms 1/k for k from 1 to 16, with bar heights 1, 1/2, 1/3, 1/4 and so on down to 1/16. The bars are coloured in blocks: k equals 1 in dark gray, k equals 2 in blue, k from 3 to 4 in green, k from 5 to 8 in orange, and k from 9 to 16 in red. Labels over the blocks say that 1/3 plus 1/4 is more than 1/2, 1/5 plus up to 1/8 is more than 1/2, and 1/9 plus up to 1/16 is more than 1/2.](../../assets/figures/05-university-core/infinite-series-basics-harmonic-grouping.svg)

*Proof.* Group the terms after the first two as

$$
1 + \frac{1}{2} + \underbrace{\left(\frac{1}{3} + \frac{1}{4}\right)}_{2\text{ terms}} + \underbrace{\left(\frac{1}{5} + \cdots + \frac{1}{8}\right)}_{4\text{ terms}} + \underbrace{\left(\frac{1}{9} + \cdots + \frac{1}{16}\right)}_{8\text{ terms}} + \cdots.
$$

The block from $\frac{1}{2^{j-1} + 1}$ to $\frac{1}{2^j}$ has $2^{j-1}$ terms, and each term is at least the last one, $\frac{1}{2^j}$. So the block sums to at least $2^{j-1}\cdot\frac{1}{2^j} = \frac{1}{2}$. The partial sum $H_{2^m}$ is $1$ plus the first $m$ blocks (the block for $j = 1$ is the single term $\frac{1}{2}$, which also equals $\frac{1}{2}$), so $H_{2^m} \ge 1 + m \cdot \frac{1}{2}$. This is unbounded. Since $H_n$ is increasing, an unbounded increasing sequence has no limit (a convergent sequence is bounded), so the series diverges. $\blacksquare$

Look back: the proof doesn't compute $H_n$. It shows $H_n$ is bigger than something that grows. It also shows how slowly: to push $H_n$ past 10 takes $n = 12{,}367$ terms, and past 5 takes 83. Each extra unit costs about $e \approx 2.7$ times as many terms as the last, as the next lesson shows with $H_n \approx \ln n$.

### Rearranging terms

A finite sum doesn't care about order. An infinite series can. The alternating harmonic series $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$ converges (next lesson), and its sum is $\ln 2 \approx 0.6931$ (this is proved in [power series and Taylor series](04-power-series-and-taylor-series.md)). Now take the same terms in a different order: two positive terms, then one negative term.

$$
1 + \frac{1}{3} - \frac{1}{2} + \frac{1}{5} + \frac{1}{7} - \frac{1}{4} + \frac{1}{9} + \frac{1}{11} - \frac{1}{6} + \cdots
$$

Every term of the original series appears exactly once. But the sum of the new series is $\frac{3}{2}\ln 2 \approx 1.0397$, which is 50% larger. The extra positive terms are used up faster than the negative ones. You can check this numerically with two million groups, which gives 1.03972.

The general fact is the Riemann rearrangement theorem, stated here without proof. If a series converges but the series of absolute values $\sum \lvert a_k \rvert$ diverges (the series is **conditionally convergent**), then for every real number $T$ there is a rearrangement of the terms whose sum is $T$, and there are rearrangements that diverge. If $\sum \lvert a_k \rvert$ converges (the series is **absolutely convergent**), every rearrangement converges to the same sum. In plain words, absolute convergence means that the positive terms and the negative terms each have a finite total, so the order can't matter. The test for it is in [convergence tests](03-convergence-tests.md).

This is the reason for step 4 of the method. Splitting a sum into positive and negative parts, regrouping, swapping the order of a double sum and rearranging terms are all safe for absolutely convergent series and unsafe in general.

## Worked examples

<div class="example" markdown>

### Example 1: a geometric series, split into two

Find $\displaystyle\sum_{k=1}^{\infty}\frac{2^k + 3^k}{6^k}$.

Step 1: no formula for $S_n$ is visible, but the term splits: $\frac{2^k + 3^k}{6^k} = \left(\frac{1}{3}\right)^k + \left(\frac{1}{2}\right)^k$. Each is a geometric series with ratio of absolute value below 1, so each converges (Theorem 1), and the sum law lets us add them.

Step 2: the first series starts at $k = 1$ with first term $\frac{1}{3}$ and ratio $\frac{1}{3}$, so its sum is $\frac{1/3}{1 - 1/3} = \frac{1}{2}$. The second has first term $\frac{1}{2}$ and ratio $\frac{1}{2}$, so its sum is $1$. The total is $\frac{1}{2} + 1 = \frac{3}{2}$.

Check: the first ten terms add to $0.49999 + 0.99902 \approx 1.4990$, and the sum of 200 terms is 1.5 to many decimals. The splitting is allowed here because both pieces converge. Watch out for starting at $k = 1$ and using $a = 1$ in the formula, which gives $\frac{1}{1 - 1/3} = \frac{3}{2}$ for the first series, an error of exactly the missing $k = 0$ term.

</div>

<div class="example" markdown>

### Example 2: a telescoping series

Find $\displaystyle\sum_{k=1}^{\infty}\frac{1}{k(k + 2)}$.

Partial fractions give $\frac{1}{k(k + 2)} = \frac{1}{2}\left(\frac{1}{k} - \frac{1}{k + 2}\right)$. The terms don't cancel with their immediate neighbours; they cancel two places along:

$$
S_n = \frac{1}{2}\left[\left(1 - \frac{1}{3}\right) + \left(\frac{1}{2} - \frac{1}{4}\right) + \left(\frac{1}{3} - \frac{1}{5}\right) + \cdots + \left(\frac{1}{n} - \frac{1}{n + 2}\right)\right].
$$

The $-\frac{1}{3}$ cancels with the $+\frac{1}{3}$ in the third bracket, and so on. What survives is the first two positive terms and the last two negative ones, so $S_n = \frac{1}{2}\left(1 + \frac{1}{2} - \frac{1}{n + 1} - \frac{1}{n + 2}\right)$. As $n \to \infty$, the last two terms tend to 0, so the sum is $\frac{1}{2}\cdot\frac{3}{2} = \frac{3}{4}$.

Check: $S_5 = \frac{1}{2}\left(\frac{3}{2} - \frac{1}{6} - \frac{1}{7}\right) = \frac{25}{42}$, and adding the five terms $\frac{1}{3} + \frac{1}{8} + \frac{1}{15} + \frac{1}{24} + \frac{1}{35}$ also gives $\frac{25}{42} \approx 0.595$, which is below the limit $0.75$ and rising toward it.

</div>

<div class="example" markdown>

### Example 3: the $n$-th term test

Decide whether $\displaystyle\sum_{k=1}^{\infty}\frac{k}{2k + 1}$ converges, and whether $\displaystyle\sum_{k=1}^{\infty}\frac{1}{k^2}$ is decided by the same test.

For the first, $\frac{k}{2k + 1} = \frac{1}{2 + 1/k} \to \frac{1}{2} \ne 0$, so the series diverges by Theorem 3. Intuitively, it adds numbers near $\frac{1}{2}$ forever.

For the second, $\frac{1}{k^2} \to 0$, so the $n$-th term test says nothing. The series happens to converge (next lesson), but the test can't tell. Compare the harmonic series, with terms $\frac{1}{k} \to 0$, which diverges.

Check: the partial sums of the first series are $\frac{1}{3}, \frac{1}{3} + \frac{2}{5}, \dots$, and each new term is at least $\frac{1}{3}$, so $S_n \ge \frac{n}{3}$, which is unbounded.

</div>

<div class="example" markdown>

### Example 4: expected number of trials

A process succeeds with probability $p$ on each independent trial, and $T$ is the number of trials up to and including the first success. For a fair die and "success = roll a six", $p = \frac{1}{6}$. What is the expected value of $T$?

The event $T > k$ means the first $k$ trials all fail, so $P(T > k) = (1 - p)^k$ for $k = 0, 1, 2, \dots$. A count can be written as a sum of indicators: $T = \sum_{k=0}^{\infty}[T > k]$, because the number of $k \ge 0$ with $T > k$ is exactly $T$. Taking expected values term by term (allowed here because all terms are non-negative),

$$
E[T] = \sum_{k=0}^{\infty} P(T > k) = \sum_{k=0}^{\infty}(1 - p)^k = \frac{1}{1 - (1 - p)} = \frac{1}{p}.
$$

For $p = \frac{1}{6}$ the expected number of rolls is $6$. The series converges because the ratio $1 - p$ has absolute value below 1.

Check: the direct sum $\sum k\,p(1 - p)^{k-1}$ with $p = \frac{1}{6}$, computed to 2000 terms, equals 6.0000, in agreement. The same series prices a retry loop in code: if a randomized step succeeds with probability $p$, you expect to run it $\frac{1}{p}$ times. A hash-table probe in open addressing at load factor $\alpha$ fails with probability $\alpha$ on each try, so the expected number of probes in a standard model (uniform hashing, as in Cormen et al., *Introduction to Algorithms*) is at most $\frac{1}{1 - \alpha}$, which is 10 at $\alpha = 0.9$. The expected value is treated fully in [discrete random variables](../07-probability/03-discrete-random-variables.md).

</div>

<div class="example" markdown>

### Example 5: a perpetuity and the money multiplier

A perpetuity pays \$100 at the end of each year forever. With a discount rate of 5% a year, a payment $k$ years away is worth $\frac{100}{1.05^k}$ today, so the present value is

$$
\sum_{k=1}^{\infty}\frac{100}{1.05^k} = \frac{100/1.05}{1 - 1/1.05} = \frac{100}{0.05} = \$2{,}000.
$$

The first term is $\frac{100}{1.05}$ and the ratio is $\frac{1}{1.05} < 1$. The rule "payment divided by rate" is this series. (All figures here are hypothetical.)

In the textbook money multiplier model, banks keep a fraction $\rho$ of every deposit as reserves and lend the rest, and every loan is redeposited. A \$1,000 deposit with $\rho = 0.10$ creates deposits of $1000 + 900 + 810 + \cdots$, a geometric series with ratio $0.9$:

$$
\sum_{k=0}^{\infty} 1000\,(0.9)^k = \frac{1000}{1 - 0.9} = \$10{,}000.
$$

The multiplier is $\frac{1}{\rho} = 10$. This is a simplified textbook model with hypothetical numbers, and [multipliers and the AD-AS model](../../07-economics-math/04-more-tools/02-multipliers-and-the-ad-as-model.md) discusses what it leaves out. Time-value formulas for loans and savings use finite versions of the same series ([annuities and geometric series](../../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md), [present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md)).

Check: the first 3,000 terms of the perpetuity sum to \$2,000.00, and the first 500 terms of the multiplier sum to \$10,000.00.

</div>

<div class="example" markdown>

### Example 6: finish it yourself

A growing perpetuity pays \$100 at the end of year 1, and each payment is 2% larger than the one before: \$100, \$102, \$104.04, and so on. The discount rate is 5%. Write the present value as a geometric series and find it.

The payment at the end of year $k$ is $100\cdot 1.02^{k-1}$, and its present value is $\frac{100\cdot 1.02^{k-1}}{1.05^k}$. The first term ($k = 1$) is $\frac{100}{1.05}$, and the ratio of consecutive terms is $\frac{1.02}{1.05}$.

<details class="solution" markdown>
<summary>Finish</summary>

The ratio $\frac{1.02}{1.05} \approx 0.9714$ has absolute value below 1, so the series converges to

$$
\frac{100/1.05}{1 - 1.02/1.05} = \frac{100/1.05}{0.03/1.05} = \frac{100}{0.03} \approx \$3{,}333.33.
$$

The rule is "first payment divided by (rate minus growth rate)".

Check: summing the first 3,000 terms numerically gives \$3,333.33. If the growth rate were 5% or more the ratio would be at least 1 and the present value would be infinite, so the formula needs growth below the discount rate.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: terms tending to 0 does not make a series converge. The harmonic series has $\frac{1}{k} \to 0$ and diverges. The $n$-th term test can prove divergence and can never prove convergence.

</div>

<div class="warning" markdown>

Watch out: don't use $\frac{a}{1 - r}$ when $\lvert r \rvert \ge 1$. The formula gives $1 + 2 + 4 + \cdots = -1$, which is nonsense for a sum of positive numbers. Check $\lvert r \rvert < 1$ before using the formula.

</div>

<div class="warning" markdown>

Watch out: the sum of $\sum_{k=1}^{\infty}\left(\frac{1}{2}\right)^k$ is 1, not 2. The formula $\frac{a}{1 - r}$ uses the first term, which is $\frac{1}{2}$ here. Using $a = 1$ adds a phantom term at $k = 0$.

</div>

<div class="warning" markdown>

Watch out: the limit of $S_n$ is the sum, not the limit of $a_n$. For $\sum \frac{1}{2^k}$ the terms tend to 0 and the sum is 1.

</div>

<div class="warning" markdown>

Watch out: splitting $\sum (a_k + b_k)$ into $\sum a_k + \sum b_k$ needs both pieces to converge. The series $\sum (1 - 1) = 0 + 0 + \cdots$ converges to 0, but you can't write it as $\sum 1 - \sum 1$ because each piece diverges. Similarly, $(1 - 1) + (1 - 1) + \cdots = 0$ while $1 - (1 - 1) - (1 - 1) - \cdots = 1$, so inserting parentheses into a divergent series changes the answer.

</div>

## Tricks and shortcuts

A geometric series is first term over one minus the ratio, so for $\frac{4}{5} + \frac{4}{25} + \frac{4}{125} + \cdots$ the first term is $\frac{4}{5}$, the ratio is $\frac{1}{5}$, and the sum is $\frac{4/5}{4/5} = 1$. To find the ratio, divide any term by the one before it.

A repeating decimal is a geometric series: $0.\overline{36} = \frac{36}{100} + \frac{36}{10000} + \cdots = \frac{36/100}{1 - 1/100} = \frac{36}{99} = \frac{4}{11}$.

For a fraction $\frac{1}{k(k + c)}$, try the partial fraction $\frac{1}{c}\left(\frac{1}{k} - \frac{1}{k + c}\right)$. The surviving terms are the first $c$ terms of $\frac{1}{k}$, so the infinite sum is $\frac{1}{c}\left(1 + \frac{1}{2} + \cdots + \frac{1}{c}\right) = \frac{H_c}{c}$. For $c = 2$ this is $\frac{1}{2}\cdot\frac{3}{2} = \frac{3}{4}$, matching Example 2.

## In code

The code finds how many terms the harmonic series needs to pass 10, and checks the geometric, telescoping and rearranged sums from this lesson.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

# Geometric: sum of 100 / 1.05^k (k >= 1) approaches 100 / 0.05 = 2000.
print(round(sum(100 / 1.05**k for k in range(1, 3000)), 4))
# 2000.0

# Telescoping: sum of 1 / (k (k + 2)) approaches 3/4.
print(round(sum(1 / (k * (k + 2)) for k in range(1, 100000)), 5))
# 0.74999

# Harmonic numbers: how many terms to pass 5, and to pass 10?
total, n = 0.0, 0
for target in (5, 10):
    while total < target:
        n += 1
        total += 1 / n
    print(target, n, round(total, 4))
# 5 83 5.0021
# 10 12367 10.0

# Rearranged alternating harmonic series: two positive terms, one negative.
s, p, q = 0.0, 1, 2
for _ in range(2_000_000):
    s += 1 / p + 1 / (p + 2) - 1 / q
    p += 4
    q += 2
print(round(s, 5), round(1.5 * math.log(2), 5), round(math.log(2), 5))
# 1.03972 1.03972 0.69315
```

</details>

## FAQ

### How can infinitely many positive numbers have a finite sum?

Because the pieces shrink fast enough. The unit square in the figure is cut into infinitely many pieces, each with positive area, and the total is the area of the square. What can't happen is that the sum exceeds the whole. Whether a series of positive terms is finite depends on how fast the terms shrink, and the borderline sits at the harmonic series, where they shrink too slowly.

### Is $0.999\ldots$ really equal to 1?

Yes. The decimal $0.999\ldots$ means the series $\frac{9}{10} + \frac{9}{100} + \cdots$, which is geometric with first term $\frac{9}{10}$ and ratio $\frac{1}{10}$. The sum is $\frac{9/10}{1 - 1/10} = 1$. The partial sums $0.9, 0.99, 0.999, \dots$ get within any $\varepsilon$ of 1, so the limit of the partial sums, which is what the infinite decimal means, is 1.

### Why define the sum as a limit instead of just "adding them all"?

Adding infinitely many numbers one at a time never finishes, so some definition is required, and the limit of partial sums is the one that agrees with finite sums and with the area picture. It has costs: it depends on the order of the terms, as the rearrangement example shows.

### If the harmonic series diverges so slowly, does it matter?

Yes, in two ways. Mathematically, divergent is divergent: for any ceiling you name, there is an $n$ past it. In computing, $H_n$ grows like $\ln n$ (next lesson), so for $n = 10^6$ the value is only about 14.4. That small growth is what makes things like expected-time analyses of randomized algorithms come out as $n\log n$ and not $n^2$.

## Practice

### Warm-up

1\. Find $\displaystyle\sum_{k=0}^{\infty} 5\left(\frac{2}{3}\right)^k$.

<details class="solution" markdown>
<summary>Solution</summary>

The first term is $5$ and the ratio is $\frac{2}{3}$, which has absolute value below 1. The sum is $\frac{5}{1 - 2/3} = 15$.

Check: the partial sums $5, 8.33, 10.56, \dots$ rise toward 15. After 40 terms the sum is $15\left(1 - \left(\frac{2}{3}\right)^{40}\right) \approx 15.000$.

</details>

2\. Does $\displaystyle\sum_{k=1}^{\infty}\frac{k^2}{k^2 + 1}$ converge?

<details class="solution" markdown>
<summary>Solution</summary>

The terms tend to $\frac{1}{1 + 1/k^2} \to 1$, not 0. By the $n$-th term test the series diverges.

Check: each term is at least $\frac{1}{2}$ (at $k = 1$ it is exactly $\frac{1}{2}$), so $S_n \ge \frac{n}{2}$, which is unbounded.

</details>

3\. Write $0.\overline{27} = 0.272727\ldots$ as a series and find the fraction.

<details class="solution" markdown>
<summary>Solution</summary>

$0.\overline{27} = \frac{27}{100} + \frac{27}{10000} + \cdots$, a geometric series with first term $\frac{27}{100}$ and ratio $\frac{1}{100}$. The sum is $\frac{27/100}{1 - 1/100} = \frac{27}{99} = \frac{3}{11}$.

Check: $\frac{3}{11} = 0.272727\ldots$ by long division.

</details>

### Standard

4\. Find $\displaystyle\sum_{k=1}^{\infty}\frac{1}{k(k + 3)}$.

<details class="solution" markdown>
<summary>Solution</summary>

Partial fractions: $\frac{1}{k(k + 3)} = \frac{1}{3}\left(\frac{1}{k} - \frac{1}{k + 3}\right)$. In the partial sum, each $-\frac{1}{k + 3}$ cancels the $+\frac{1}{k + 3}$ that appears three terms later, so what survives is $S_n = \frac{1}{3}\left(1 + \frac{1}{2} + \frac{1}{3} - \frac{1}{n + 1} - \frac{1}{n + 2} - \frac{1}{n + 3}\right)$. As $n \to \infty$ the last three terms tend to 0, so the sum is $\frac{1}{3}\cdot\frac{11}{6} = \frac{11}{18}$.

Check: this is $\frac{H_3}{3}$ as in the shortcut. Numerically, $\sum_{k=1}^{10^5}\frac{1}{k(k + 3)} \approx 0.61111$, and $\frac{11}{18} = 0.61111$.

</details>

5\. A wheel of ten equally likely slots has one winning slot. You spin until you win. (a) What is the expected number of spins? (b) What is the probability that it takes more than 20 spins?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Here $p = \frac{1}{10}$, so $E[T] = \frac{1}{p} = 10$ spins, from Example 4.

(b) $T > 20$ means the first 20 spins all lose, with probability $0.9^{20} \approx 0.1216$, about 12%.

Check: $0.9^{20} = 0.12158$. The sum of all tail probabilities $\sum_{k \ge 0} 0.9^k = 10$ agrees with (a).

</details>

6\. A perpetuity pays \$250 at the end of each year forever, and the discount rate is 4% a year (hypothetical numbers). Find its present value. Then find the present value of the same payments if the first \$250 arrives today and the rest at the ends of later years.

<details class="solution" markdown>
<summary>Solution</summary>

The payments at the end of years 1, 2, 3, ... have present value $\sum_{k=1}^{\infty}\frac{250}{1.04^k} = \frac{250}{0.04} = \$6{,}250$.

If a payment of \$250 also arrives today, it adds its own worth, \$250, so the total is $6250 + 250 = \$6{,}500$. As a geometric series starting at $k = 0$, $\frac{250}{1 - 1/1.04} = \frac{250 \cdot 1.04}{0.04} = \$6{,}500$.

Check: $6{,}250 \cdot 1.04 = 6{,}500$, since each payment is one year closer.

</details>

### Challenge

7\. Prove that $\displaystyle\sum_{k=1}^{\infty}\ln\left(1 + \frac{1}{k}\right)$ diverges even though its terms tend to 0. Then use it to show that the series $\sum \ln\left(1 - \frac{1}{(k + 1)^2}\right)$ converges and find its sum.

<details class="solution" markdown>
<summary>Solution</summary>

Since $\ln\left(1 + \frac{1}{k}\right) = \ln\frac{k + 1}{k} = \ln(k + 1) - \ln k$, the partial sum is $S_n = \ln(n + 1) - \ln 1 = \ln(n + 1) \to \infty$. The terms $\ln\left(1 + \frac{1}{k}\right) \to \ln 1 = 0$.

For the second series, $1 - \frac{1}{(k + 1)^2} = \frac{k(k + 2)}{(k + 1)^2}$, so the term is $\ln k + \ln(k + 2) - 2\ln(k + 1) = \left(\ln(k + 2) - \ln(k + 1)\right) - \left(\ln(k + 1) - \ln k\right)$. This is $b_{k+1} - b_k$ with $b_k = \ln(k + 1) - \ln k = \ln\left(1 + \frac{1}{k}\right)$. The partial sum from $k = 1$ to $n$ telescopes to $b_{n+1} - b_1 = \ln\left(1 + \frac{1}{n + 1}\right) - \ln 2 \to -\ln 2$. The series converges to $-\ln 2 \approx -0.6931$.

Check: the first term is $\ln\frac{3}{4} = -0.2877$ and the second is $\ln\frac{8}{9} = -0.1178$, and the partial sum through $k = 10$ is $\ln\frac{12}{11} - \ln 2 \approx -0.6061$, moving toward $-0.6931$.

</details>

8\. (Reviews [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md).) The finite formula gives $\sum_{k=0}^{n-1} ar^k = a\frac{1 - r^n}{1 - r}$. Use it to explain why the infinite series with $r = -1$ and $a = 1$, $1 - 1 + 1 - 1 + \cdots$, diverges, by listing the partial sums, and say which of the lesson's tests shows it.

<details class="solution" markdown>
<summary>Solution</summary>

With $r = -1$ the formula gives $S_n = \frac{1 - (-1)^n}{2}$, which is 1 when $n$ is odd and 0 when $n$ is even (here $S_n$ is the sum of the first $n$ terms). The partial sums are $1, 0, 1, 0, \dots$, an oscillating sequence with no limit (Theorem 4 of the last lesson), so the series diverges. The $n$-th term test also shows it: the terms $(-1)^k$ do not tend to 0.

Check: $S_1 = 1$, $S_2 = 1 - 1 = 0$, $S_3 = 1$, matching $\frac{1 - (-1)^n}{2}$.

</details>

## Where this shows up

- The next lesson gives tests for deciding convergence without a formula for the partial sums ([convergence tests](03-convergence-tests.md)), and the lesson after it turns series into functions ([power series and Taylor series](04-power-series-and-taylor-series.md)).
- In CS, closed forms for sums are the working tool of algorithm analysis ([sums and closed forms](../../06-cs-math/04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md)), and the geometric series $\sum (1 - p)^k = \frac{1}{p}$ is the expected cost of every "retry until success" loop ([discrete random variables](../07-probability/03-discrete-random-variables.md)).
- In economics and finance, perpetuities, bond prices and the multiplier are geometric series ([present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md), [annuities and geometric series](../../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md)).
