# The law of large numbers and the CLT

After this lesson you can find the mean and variance of a sample mean, prove Markov's and Chebyshev's inequalities and the weak law of large numbers, state the central limit theorem and use it (including the normal approximation to the binomial), compute how the error of a Monte Carlo estimate shrinks, and explain why the gambler's fallacy is a fallacy.

Before this: [discrete random variables](03-discrete-random-variables.md), [continuous random variables and the normal distribution](04-continuous-random-variables-and-the-normal.md) and [joint distributions, covariance and sums](05-joint-distributions-covariance-and-sums.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A random variable has mean 50 and standard deviation 5. Use Chebyshev's inequality to bound $P(\lvert X - 50 \rvert \ge 15)$.
2. You roll a fair die 100 times. What is the standard deviation of the average of the 100 rolls?
3. You estimate a probability by a simulation of $n$ independent trials, and the standard deviation of each trial's 0-or-1 result is at most $\frac{1}{2}$. How large must $n$ be for the standard deviation of the estimate to be at most 0.005?

<details class="solution" markdown>
<summary>Answers</summary>

1. The deviation 15 is $k = 3$ standard deviations, so the bound is $\frac{1}{k^2} = \frac{1}{9} \approx 0.111$.
2. One roll has $\sigma = \sqrt{\frac{35}{12}} \approx 1.708$, so the average of 100 rolls has standard deviation $\frac{1.708}{\sqrt{100}} \approx 0.171$.
3. The estimate is an average, with standard deviation $\frac{\sigma}{\sqrt{n}} \le \frac{0.5}{\sqrt{n}}$. We need $\frac{0.5}{\sqrt{n}} \le 0.005$, so $\sqrt{n} \ge 100$ and $n \ge 10{,}000$.

</details>

## The idea

Roll a die once and you get 1 to 6 with no way to predict it. Roll it 100 times and average: the result is almost always between 3.2 and 3.8. Roll it 10,000 times and it is between 3.45 and 3.55. The randomness of the individual rolls doesn't go away, but it averages out, and the average becomes more and more predictable. This is the most useful fact about randomness: totals and averages of many independent pieces behave in a regular way, even though the pieces don't.

There are two statements of this regularity. The first, the law of large numbers, says where the average ends up: at the mean $\mu$ of a single piece. The second, the central limit theorem, says how it gets there: the leftover error is shaped like a bell curve, and its size shrinks like $\frac{1}{\sqrt{n}}$. The figure below shows four runs of the average of die rolls. Each wanders widely at first and then settles at 3.5, inside a band that narrows with the number of rolls.

![Four coloured lines showing the running average of die rolls against the number of rolls from 1 to 5,000 on a logarithmic axis. They start far apart, from 1 to 6, and all converge to the dashed line at 3.5. A gray band, 3.5 plus or minus 2 sigma over root n, narrows around the line and contains the runs.](../../assets/figures/05-university-core/law-of-large-numbers-and-clt-running-average.svg)

The band is the key. The average of $n$ rolls usually sits within about $\frac{2\sigma}{\sqrt{n}}$ of the mean, so to cut the error in half you need four times as many rolls. That square root is the price of precision in polling, in measurement and in simulation, and it is derived in this lesson.

## Definitions

Random variables $X_1, X_2, \dots, X_n$ are **independent and identically distributed**, or **i.i.d.**, if they are independent and all have the same distribution. Think of $n$ independent repetitions of the same experiment. Write $\mu$ for their common mean and $\sigma^2$ for their common variance. The **sample mean** is

$$
\bar{X}_n = \frac{X_1 + X_2 + \cdots + X_n}{n}.
$$

In plain words, it is the ordinary average of the $n$ results, now seen as a random variable, because different repetitions of the whole experiment give different averages. The **standard error** of the sample mean is its standard deviation, $\frac{\sigma}{\sqrt{n}}$, as the first theorem shows.

*Theorem 1 (mean and variance of the sample mean).* If $X_1, \dots, X_n$ are i.i.d. with mean $\mu$ and variance $\sigma^2$, then

$$
E[\bar{X}_n] = \mu, \qquad \operatorname{Var}(\bar{X}_n) = \frac{\sigma^2}{n}.
$$

We know linearity of expectation, the scaling rule $\operatorname{Var}(aX) = a^2\operatorname{Var}(X)$, and that variances of independent variables add. We want the mean and variance of the average. The plan is to write $\bar{X}_n$ as $\frac{1}{n}$ times the sum.

*Proof.* By linearity, $E[\bar{X}_n] = \frac{1}{n}\sum_{i=1}^{n}E[X_i] = \frac{1}{n}\cdot n\mu = \mu$. By independence, $\operatorname{Var}\left(\sum_i X_i\right) = \sum_i\operatorname{Var}(X_i) = n\sigma^2$, and by the scaling rule with $a = \frac{1}{n}$,

$$
\operatorname{Var}(\bar{X}_n) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}. \qquad \blacksquare
$$

Look back: the average is on target (its mean is $\mu$) and its spread shrinks like $\frac{1}{\sqrt{n}}$. The standard deviation of the total $S_n = X_1 + \cdots + X_n$ is $\sigma\sqrt{n}$, which grows, but more slowly than the total itself, whose mean is $n\mu$. Averages get better with $n$ because the total grows like $n$ and its noise grows like $\sqrt{n}$. The proof used independence in one place, the variance of the sum: with correlated terms the variance of the average would not shrink to 0.

Two inequalities bound how far a random variable can be from its mean, knowing only its mean or its variance. They are blunt, and that is what makes them useful: they need no assumption about the shape of the distribution.

*Theorem 2 (Markov's inequality).* If $X \ge 0$ and $a > 0$, then

$$
P(X \ge a) \le \frac{E[X]}{a}.
$$

We know that expectation preserves inequalities between random variables ($Y \le Z$ everywhere implies $E[Y] \le E[Z]$) and that $E[I_A] = P(A)$. We want to bound a tail probability by the mean. The plan is to compare $X$ with $a$ times an indicator.

*Proof.* Let $A = \{X \ge a\}$. For every outcome, $a\,I_A \le X$: if the outcome is in $A$, the left side is $a$ and $X \ge a$, and if it is not in $A$, the left side is 0 and $X \ge 0$. Taking expectations, $a\,P(A) = E[a\,I_A] \le E[X]$. Divide by $a$. $\blacksquare$

Look back: a nonnegative variable with a small mean can't be large very often. If the average response time is 200 ms, then $P(X \ge 1000) \le \frac{200}{1000} = 0.2$: at most one request in five takes 5 times the average. The condition $X \ge 0$ is needed, and the bound is far from sharp for well-behaved distributions: for an exponential variable with mean 2 and $a = 10$, Markov gives 0.2 and the true value is $e^{-5} = 0.0067$.

*Theorem 3 (Chebyshev's inequality).* If $X$ has mean $\mu$ and variance $\sigma^2$, then for every $\varepsilon > 0$,

$$
P\bigl(\lvert X - \mu \rvert \ge \varepsilon\bigr) \le \frac{\sigma^2}{\varepsilon^2}.
$$

Equivalently, $P(\lvert X - \mu \rvert \ge k\sigma) \le \frac{1}{k^2}$ for $k > 0$.

We know Markov's inequality. We want a bound on the distance from the mean. The plan is to apply Markov's inequality to the nonnegative variable $(X - \mu)^2$.

*Proof.* The events $\{\lvert X - \mu \rvert \ge \varepsilon\}$ and $\{(X - \mu)^2 \ge \varepsilon^2\}$ are the same event. By Markov's inequality applied to $(X - \mu)^2 \ge 0$ with $a = \varepsilon^2$,

$$
P\bigl((X - \mu)^2 \ge \varepsilon^2\bigr) \le \frac{E\bigl[(X - \mu)^2\bigr]}{\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2}.
$$

Taking $\varepsilon = k\sigma$ gives the second form. $\blacksquare$

Look back: at most $\frac{1}{4}$ of the probability can be two or more standard deviations from the mean, and at most $\frac{1}{9}$ three or more, for every distribution with a finite variance. For a normal variable the true values are 0.0455 and 0.0027, so Chebyshev is generous, but it holds for every distribution, including ones you know nothing about. Practice problem 7 shows the bound can't be improved without more information.

*Theorem 4 (weak law of large numbers).* If $X_1, X_2, \dots$ are i.i.d. with mean $\mu$ and finite variance $\sigma^2$, then for every $\varepsilon > 0$,

$$
\lim_{n \to \infty}P\bigl(\lvert \bar{X}_n - \mu \rvert \ge \varepsilon\bigr) = 0.
$$

We know Theorem 1 and Chebyshev's inequality. We want the chance of a deviation of size $\varepsilon$ to go to 0. The plan is to apply Chebyshev's inequality to $\bar{X}_n$.

*Proof.* By Theorem 1, $\bar{X}_n$ has mean $\mu$ and variance $\frac{\sigma^2}{n}$. Chebyshev's inequality gives

$$
P\bigl(\lvert \bar{X}_n - \mu \rvert \ge \varepsilon\bigr) \le \frac{\sigma^2/n}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2}.
$$

For fixed $\varepsilon$ and $\sigma$, the right side tends to 0 as $n \to \infty$, and the probability on the left is non-negative, so it tends to 0 too. $\blacksquare$

Look back: the proof gives more than the statement: it gives a number, $\frac{\sigma^2}{n\varepsilon^2}$, for each $n$. The statement is called "weak" because it is about the probability of a deviation at one large $n$; the strong law says that, with probability 1, the whole sequence of averages converges to $\mu$. That one needs a longer proof and this book states it without one. The law also holds without a finite variance, as long as the mean exists, but not with the elementary proof above.

The LLN says that the average ends up at $\mu$. The next theorem describes the shape of the error. It is stated without proof here, because the standard proof uses moment generating functions or characteristic functions.

*Theorem 5 (central limit theorem).* Let $X_1, X_2, \dots$ be i.i.d. with mean $\mu$ and finite variance $\sigma^2 > 0$, and let $Z_n = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}}$. Then for every real number $z$,

$$
\lim_{n \to \infty}P(Z_n \le z) = \Phi(z).
$$

In plain words, the standardized average has approximately the standard normal distribution when $n$ is large, whatever the distribution of the individual $X_i$ (as long as the variance is finite). The variable $Z_n$ is the sample mean with its mean subtracted and its standard deviation divided out (Theorem 1), so its mean is 0 and its variance is 1 for every $n$. The theorem says that its whole shape approaches the bell curve. Equivalently, the sum $S_n$ is approximately $N(n\mu, n\sigma^2)$ and the average is approximately $N\left(\mu, \frac{\sigma^2}{n}\right)$.

The figure shows it. The top row is the standardized average of $n = 1, 2, 5, 30$ dice, with the standard normal density drawn over each, and the bottom row is the same for exponential variables, whose distribution is strongly skewed. The dice get close almost at once because a die is already symmetric. The exponential takes longer, because of the skew: at $n = 10$ the right tail is still visibly heavier than the normal curve, and by $n = 50$ the match is good.

![Two rows of four histograms with the standard normal curve drawn over each. Top row, standardized averages of 1, 2, 5 and 30 dice: a flat block, a pointed hill, then close matches to the curve. Bottom row, standardized averages of 1, 2, 10 and 50 exponential variables: a sharply skewed shape at n equal to 1, then progressively more symmetric shapes, close to the curve at n equal to 50.](../../assets/figures/05-university-core/law-of-large-numbers-and-clt-clt.svg)

## How to do it

### Using the central limit theorem

1. Identify the sum or average, check that the terms are independent and have the same distribution (or at least similar small contributions), and find $\mu$ and $\sigma$ of one term.
2. Find the mean and standard deviation of the quantity: for the sum, $n\mu$ and $\sigma\sqrt{n}$. For the average, $\mu$ and $\frac{\sigma}{\sqrt{n}}$.
3. Standardize with $z = \frac{\text{value} - \text{mean}}{\text{standard deviation}}$, and find the probability from $\Phi$ ([the normal lesson](04-continuous-random-variables-and-the-normal.md#finding-normal-probabilities)).
4. For counts that take integer values (sums of integers), apply the continuity correction: treat the integer $k$ as the interval from $k - \frac{1}{2}$ to $k + \frac{1}{2}$.
5. Check that $n$ is large enough for the shape of the individual terms. A skewed or heavy-tailed term needs more terms than a symmetric one, and a common rule of thumb for a binomial is $np \ge 10$ and $nq \ge 10$. These are rules of thumb and not theorems.
6. If you need a guarantee rather than an approximation, use Chebyshev's bound instead, which is weaker and needs no conditions beyond a finite variance.

### The normal approximation to the binomial

A binomial variable $X \sim \text{Bin}(n, p)$ is a sum of $n$ i.i.d. Bernoulli variables with mean $p$ and variance $pq$, so by the central limit theorem, for large $n$,

$$
X \approx N(np,\ npq).
$$

With the continuity correction, $P(X \ge k) \approx 1 - \Phi\!\left(\frac{k - \frac{1}{2} - np}{\sqrt{npq}}\right)$ and $P(X \le k) \approx \Phi\!\left(\frac{k + \frac{1}{2} - np}{\sqrt{npq}}\right)$. The correction matters: the exact binomial PMF is a set of bars of width 1 centred at the integers, and the normal curve should be integrated over the bar, which runs half a unit beyond the integer on each side.

## Worked examples

<div class="example" markdown>

### Example 1: the average of 100 dice, and how loose Chebyshev is

You roll a fair die 100 times. Find the mean and standard deviation of the average, bound the probability that it differs from 3.5 by 0.5 or more with Chebyshev's inequality, and compare with the central limit theorem.

Step 1: the rolls are i.i.d. with $\mu = 3.5$ and $\sigma^2 = \frac{35}{12}$. Step 2: by Theorem 1, $E[\bar{X}] = 3.5$ and $\operatorname{Var}(\bar{X}) = \frac{35/12}{100} = 0.02917$, so the standard error is $0.1708$.

For Chebyshev, take $\varepsilon = 0.5$: $P(\lvert\bar{X} - 3.5\rvert \ge 0.5) \le \frac{0.02917}{0.25} = 0.1167$. This is a guarantee, valid whatever the distribution.

By the central limit theorem, $\bar{X}$ is approximately $N(3.5, 0.1708^2)$, and $0.5$ is $\frac{0.5}{0.1708} = 2.93$ standard errors, so the probability is about $2\bigl(1 - \Phi(2.93)\bigr) = 0.0034$.

Step 5: the two answers are far apart, as they should be: one is a ceiling that holds for every distribution and the other is an approximation for this one. A simulation of 20,000 averages of 100 rolls gives a frequency of 0.004, close to the central limit answer and well under Chebyshev's ceiling (see [In code](#in-code)). The simulated standard deviation, 0.1705, matches $0.1708$.

</div>

<div class="example" markdown>

### Example 2: normal approximation to a binomial

A fair coin is flipped 100 times. Estimate the probability of at least 60 heads, and compare with the exact value.

Step 1: $X \sim \text{Bin}(100, 0.5)$ has mean $np = 50$ and variance $npq = 25$, so $\sigma = 5$. Step 2: with the continuity correction, $P(X \ge 60)$ is the area to the right of $59.5$, with z-score $\frac{59.5 - 50}{5} = 1.9$. So $P(X \ge 60) \approx 1 - \Phi(1.9) = 1 - 0.9713 = 0.0287$.

Step 3: the exact value is $\sum_{k=60}^{100}\binom{100}{k}\left(\frac{1}{2}\right)^{100} = 0.0284$. The approximation is within 0.0003. Without the correction, the z-score is $\frac{60 - 50}{5} = 2$ and the answer is $1 - \Phi(2) = 0.0228$, 20% too small, because it leaves out half of the bar at 60.

Check: the conditions $np = 50 \ge 10$ and $nq = 50 \ge 10$ hold. A second case, with $n = 1000$ flips: $P(X \le 480)$ has $\sigma = \sqrt{250} = 15.81$ and the z-score $\frac{480.5 - 500}{15.81} = -1.23$, so the approximation is $0.1087$, the same as the exact value to 4 decimals.

</div>

<div class="example" markdown>

### Example 3: how many people to ask in a poll

A poll will estimate the share $p$ of voters who support a proposal. Each person asked is an independent yes-or-no draw (an idealization: real polls have other sources of error). How many people must be asked so that, with probability about 95%, the sample proportion is within 0.03 of the true $p$?

Step 1: the sample proportion $\hat{p}$ is the sample mean of Bernoulli variables, so $E[\hat{p}] = p$ and the standard error is $\sqrt{\frac{pq}{n}}$. Step 2: by the central limit theorem, $\hat{p}$ is approximately normal, and $P(\lvert\hat{p} - p\rvert < 1.96\sqrt{pq/n}) \approx 0.95$, because $P(\lvert Z \rvert < 1.96) = 0.95$.

Step 3: we need $1.96\sqrt{\frac{pq}{n}} \le 0.03$. The value of $p$ is unknown, but $pq \le \frac{1}{4}$ with equality at $p = \frac{1}{2}$, so the worst case is $\sqrt{pq} = 0.5$, and

$$
n \ge \left(\frac{1.96 \cdot 0.5}{0.03}\right)^2 = 1067.1.
$$

So ask 1,068 people. This is where the familiar "about 1,000 people, give or take 3 percentage points" comes from.

Check: for $n = 1068$ the standard error is $\frac{0.5}{\sqrt{1068}} = 0.0153$, and $1.96 \cdot 0.0153 = 0.0300$. To halve the margin of error to 0.015 you need four times as many people, about 4,270, which is the $\frac{1}{\sqrt{n}}$ price of precision.

</div>

<div class="example" markdown>

### Example 4: Monte Carlo error (finish it yourself)

In [the first lesson](01-sample-spaces-events-and-axioms.md) we estimated $\pi$ by throwing random points at the unit square and counting the share that land inside the quarter disc, then multiplying by 4. Each point is a Bernoulli trial with $p = \frac{\pi}{4}$, so the estimate is $4\hat{p}$. How many points are needed for an error of at most 0.001, with probability about 95%?

Step 1: the standard deviation of a single trial is $\sqrt{p(1 - p)} = \sqrt{0.7854 \cdot 0.2146} = 0.4105$, and multiplying by 4, the standard deviation of one term of the estimate is $\sigma = 4 \cdot 0.4105 = 1.642$. Step 2: the standard error of the estimate after $n$ points is $\frac{1.642}{\sqrt{n}}$. Step 3: with probability about 95% the error is at most $1.96 \cdot \frac{1.642}{\sqrt{n}}$.

Set this equal to 0.001 and solve for $n$.

<details class="solution" markdown>
<summary>Finish</summary>

$\sqrt{n} = \frac{1.96 \cdot 1.642}{0.001} = 3218.7$, so $n = 3218.7^2 \approx 10.4$ million points. For an error of 0.01 the same formula gives about 103,600 points, 100 times fewer, as one more digit of accuracy costs 100 times as many samples.

Check: the figure below shows the average error for various $n$, from simulations. At $n = 10^4$ the average error is 0.0136 in the simulation in [In code](#in-code), against $\frac{1.642\sqrt{2/\pi}}{\sqrt{n}} = 0.0131$ from the theory (the factor $\sqrt{2/\pi}$ converts a standard deviation to an average absolute error for a normal variable). The 100,000-point simulation of the first lesson was off by 0.013. The standard error at that $n$ is $\frac{1.642}{\sqrt{100{,}000}} = 0.0052$, so that run was about 2.5 standard errors off, a somewhat unlucky run (about 1 run in 80 is that far or further).

</details>

</div>

![A log-log plot of the average error of the estimate of pi against the number of random points, from 100 to 10 million. The simulated points lie on a straight line of slope minus one half, falling from about 0.13 to about 0.0004, and a dashed gray line with the 1 over root n shape lies on top of it.](../../assets/figures/05-university-core/law-of-large-numbers-and-clt-monte-carlo.svg)

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the gambler's fallacy. A fair coin has shown five heads in a row. The law of large numbers does not make tails "due". The flips are independent, so the next flip is heads with probability $\frac{1}{2}$, as it always was. The average of the first $n$ flips tends to $\frac{1}{2}$ because the early excess of heads is swamped by the many later flips and not because it is corrected: if after 5 flips there are 5 heads, then after 10,000 more flips we expect about 5,005 heads out of 10,005, a share of 0.5002, with the excess of 5 heads still there, only diluted. In a simulation of 2 million flips, among the 61,840 flips that followed five heads in a row, 49.96% were heads.

</div>

<div class="warning" markdown>

Watch out: the law of large numbers is about averages, not counts. The average of $n$ flips approaches $\frac{1}{2}$, but the count of heads minus $\frac{n}{2}$ does not approach 0: its standard deviation is $\frac{\sqrt{n}}{2}$, which grows. After 1,000 flips the typical gap is about $\frac{\sqrt{1000}}{2} = 15.8$ heads, and after 10,000 flips it is about 50. The gap grows in absolute terms and shrinks in relative terms, from 1.6% of the flips at $n = 1000$ to 0.5% at $n = 10{,}000$.

</div>

<div class="warning" markdown>

Watch out: the central limit theorem is about the distribution of the average, not about the data. The individual values don't become normal when you collect more of them, and a histogram of 10,000 exponential waiting times is still skewed. What becomes normal is the distribution of the average (or the sum) of many of them, over repeated experiments.

</div>

<div class="warning" markdown>

Watch out: the theorems have conditions. Independence is needed: for correlated errors, the variance of the mean is not $\frac{\sigma^2}{n}$ and may not shrink at all (a measurement with the same systematic error each time doesn't average out). Finite variance is needed for the CLT as stated. The Cauchy distribution of the [last lesson](04-continuous-random-variables-and-the-normal.md) has no mean, and the average of $n$ Cauchy variables is again a Cauchy variable, with the same spread as one: in the simulation, averages of $n = 10$, $1{,}000$ and $100{,}000$ values came out as $-0.625$, $-0.736$ and $48.09$, with no sign of settling.

</div>

Chebyshev's bound is a ceiling. A value like $\frac{1}{9}$ doesn't mean the probability is near $\frac{1}{9}$: for a normal variable it is 0.0027. Use Chebyshev when you can't assume more, and the central limit theorem when you can.

The sample size in the rule "$n \ge 30$ is large enough" is a folk rule. For a symmetric distribution, $n = 5$ may do, as the dice in the figure show. For a very skewed one, such as incomes or file sizes, $n = 30$ is far from enough, and the true answer depends on the third moment, as the exponential row shows at $n = 10$.

## Tricks and shortcuts

Think in standard errors. The average of $n$ observations with standard deviation $\sigma$ has standard error $\frac{\sigma}{\sqrt{n}}$, and about 95% of the time the average is within $2\frac{\sigma}{\sqrt{n}}$ of $\mu$. To cut the error by a factor of 10, take 100 times as many observations. To check whether a difference between two averages is noise, compare it with the standard errors.

For a quick sample size: the margin of error of a proportion is about $\frac{1}{\sqrt{n}}$ at 95% (since $1.96 \cdot 0.5 \approx 1$), so $n = 100$ gives $\pm 10$ points, $n = 400$ gives $\pm 5$ and $n = 1000$ gives $\pm 3$.

For the sum, scale by $\sqrt{n}$, not by $n$: the sum of 100 independent rolls has standard deviation $10\sigma = 17.1$, and not $100\sigma$. The sum of 12 independent uniform variables on $[0, 1]$ has mean 6 and variance $12 \cdot \frac{1}{12} = 1$, so "sum of 12 uniforms minus 6" is an approximate standard normal, a cheap generator that was widely used before better methods became standard.

When the answer needs a rigorous guarantee, not an estimate, use Chebyshev's inequality or the union bound of the first lesson. When an estimate is enough, use the central limit theorem and say that it is approximate.

## In code

The code checks Theorem 1 and Chebyshev's bound on averages of dice, the normal approximation to a binomial against the exact sum, the $\frac{1}{\sqrt{n}}$ shrinking of the Monte Carlo error for $\pi$, the gambler's fallacy and the Cauchy average.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import random
from statistics import NormalDist, mean, pstdev

random.seed(2026)

# The sample mean of n = 100 die rolls: its spread is sigma / sqrt(n).
means = [mean(random.randint(1, 6) for _ in range(100)) for _ in range(20_000)]
print(round(mean(means), 3), round(pstdev(means), 4), round(math.sqrt(35 / 12 / 100), 4))
# 3.499 0.1705 0.1708
# Chebyshev: P(|mean - 3.5| >= 0.5) is at most 0.1167; the simulation gives far less.
print(sum(abs(m - 3.5) >= 0.5 for m in means) / len(means), round(35 / 12 / 100 / 0.25, 4))
# 0.00405 0.1167

# Normal approximation to Binomial(100, 0.5): P(X >= 60), with the continuity correction.
exact = sum(math.comb(100, k) for k in range(60, 101)) / 2**100
approx = 1 - NormalDist(50, 5).cdf(59.5)
print(round(exact, 4), round(approx, 4), round(1 - NormalDist(50, 5).cdf(60), 4))
# 0.0284 0.0287 0.0228

# Monte Carlo error for pi: the average error falls like 1 / sqrt(n).
for n in (100, 1_000, 10_000):
    errors = []
    for _ in range(200):
        hits = sum(1 for _ in range(n) if random.random() ** 2 + random.random() ** 2 <= 1)
        errors.append(abs(4 * hits / n - math.pi))
    print(n, round(mean(errors), 4), round(1.642 * math.sqrt(2 / math.pi) / math.sqrt(n), 4))
# 100 0.1264 0.131
# 1000 0.0401 0.0414
# 10000 0.0136 0.0131

# The gambler's fallacy: after five heads in a row, the next flip is still heads half the time.
flips = [random.random() < 0.5 for _ in range(2_000_000)]
after = [flips[i] for i in range(5, len(flips)) if all(flips[i - 5:i])]
print(len(after), round(sum(after) / len(after), 4))
# 61840 0.4996

# Cauchy variables have no mean, so the running average never settles.
random.seed(4)
cauchy = lambda: math.tan(math.pi * (random.random() - 0.5))
for n in (10, 1_000, 100_000):
    print(n, round(sum(cauchy() for _ in range(n)) / n, 3))
# 10 -0.625
# 1000 -0.736
# 100000 48.091
```

Each Monte Carlo error is the average of 200 runs, so the match with the theory is within a few percent. The gambler's fallacy check conditions on the previous five flips by filtering, as in the conditional probability lesson. For the Cauchy variable, the transform $\tan(\pi(U - \frac{1}{2}))$ of a uniform $U$ has the Cauchy density, by the inverse-CDF method.

</details>

## FAQ

### Does the law of large numbers say that I'll break even if I keep playing?

No. It says that your average winnings per play approach the expected value per play. In a game with a negative expected value, the average loss per play approaches that negative number, and the total loss grows with the number of plays. In a fair game the average approaches 0, but your total can still wander far from 0, by about $\sigma\sqrt{n}$. The law gives no reason for the total to return to 0, so staying in the game longer doesn't recover earlier losses.

### Why is it $\sqrt{n}$ and not $n$?

Because independent variances add, and standard deviations are square roots of variances. The sum of $n$ terms has variance $n\sigma^2$, so its standard deviation is $\sigma\sqrt{n}$, and dividing by $n$ to get the average leaves $\frac{\sigma}{\sqrt{n}}$. Positive and negative errors partly cancel, which is why the noise grows more slowly than $n$, and not completely, which is why it doesn't shrink faster.

### Why does the normal curve appear, whatever the distribution of the terms?

The mean and the variance survive averaging and everything else is washed out. Heuristically, the skewness of the standardized sum shrinks like $\frac{1}{\sqrt{n}}$, and the other features of the shape beyond the mean 0 and variance 1 fade as well. The bell curve is the one shape that is left unchanged when you add independent copies and standardize again. A proof with moment generating functions makes this precise, and the version for characteristic functions needs no assumption beyond a finite variance.

### Is $n = 30$ enough?

For the average to be close to normal, it depends on the distribution of the terms. A symmetric term can be close at $n = 5$. A skewed one (the exponential in the figure) is visibly off at $n = 10$. A heavy-tailed one with infinite variance never converges to a normal curve. Look at the shape of the data or use a simulation.

## Practice

### Warm-up

1\. A random variable has mean 50 and standard deviation 5. Bound $P(\lvert X - 50 \rvert \ge 15)$ with Chebyshev, and find the exact value if $X$ is normal.

<details class="solution" markdown>
<summary>Solution</summary>

Here $k = \frac{15}{5} = 3$, so Chebyshev gives $P \le \frac{1}{9} \approx 0.111$. For a normal $X$, the probability is $2\bigl(1 - \Phi(3)\bigr) = 2(0.00135) = 0.0027$.

Check: the exact value is below the bound, 0.0027 against 0.111, and the bound is about 40 times too high, which shows how blunt it is.

</details>

2\. Measurements have standard deviation $\sigma = 12$. What is the standard error of the average of $n = 400$ measurements? How many measurements are needed to make it 0.3?

<details class="solution" markdown>
<summary>Solution</summary>

The standard error is $\frac{12}{\sqrt{400}} = 0.6$. For 0.3, we need $\frac{12}{\sqrt{n}} = 0.3$, so $\sqrt{n} = 40$ and $n = 1600$.

Check: halving the standard error needed four times as many measurements, $400 \cdot 4 = 1600$.

</details>

3\. A web server's average response time is 200 ms. Use Markov's inequality to bound the fraction of requests that take at least a second.

<details class="solution" markdown>
<summary>Solution</summary>

The response time is nonnegative, so $P(X \ge 1000) \le \frac{200}{1000} = 0.2$. At most 20% of requests take a second or longer.

Check: if more than 20% took at least 1000 ms, those requests alone would contribute more than $0.2 \cdot 1000 = 200$ ms to the average, a contradiction since the other requests add at least 0.

</details>

### Standard

4\. A fair coin is flipped 200 times. Use the normal approximation with a continuity correction to estimate $P(X \le 90)$, and compare with the exact value.

<details class="solution" markdown>
<summary>Solution</summary>

$X \sim \text{Bin}(200, 0.5)$ has mean 100 and variance 50, so $\sigma = 7.071$. The event $X \le 90$ is the area to the left of $90.5$, with z-score $\frac{90.5 - 100}{7.071} = -1.343$. So $P(X \le 90) \approx \Phi(-1.343) = 0.0896$. The exact value is $\sum_{k=0}^{90}\binom{200}{k}2^{-200} = 0.0895$.

Check: without the correction, $z = \frac{90 - 100}{7.071} = -1.414$ and the answer is $0.0786$, about 12% too low. The corrected value 0.0896 is within 0.0001 of the exact one.

</details>

5\. How many rolls of a fair die guarantee, with the CLT approximation, that $P(\lvert\bar{X}_n - 3.5\rvert < 0.1) \ge 0.95$? How many does Chebyshev's inequality require for the same bound?

<details class="solution" markdown>
<summary>Solution</summary>

By the CLT, we need $1.96\,\frac{\sigma}{\sqrt{n}} \le 0.1$ with $\sigma = 1.708$, so $\sqrt{n} \ge 33.47$ and $n \ge 1120.5$, that is, $n = 1121$.

By Chebyshev, we need $P(\lvert\bar{X}_n - 3.5\rvert \ge 0.1) \le \frac{35/12}{n(0.1)^2} \le 0.05$, so $n \ge \frac{2.9167}{0.01 \cdot 0.05} = 5833.3$, that is, $n = 5834$.

Check: Chebyshev asks for about five times as many rolls, the price of a bound that makes no assumption about the shape. The CLT answer 1121 is an approximation, and the Chebyshev answer 5834 is a guarantee.

</details>

6\. To estimate $I = \int_0^1 e^{-x^2}\,dx$ by Monte Carlo, average $g(U) = e^{-U^2}$ over random $U$ uniform on $[0, 1]$, since $E[g(U)] = I$. The standard deviation of $g(U)$ is $0.2010$. How many samples give an error of at most 0.001 with probability 95%?

<details class="solution" markdown>
<summary>Solution</summary>

The standard error is $\frac{0.2010}{\sqrt{n}}$, and the 95% error is $1.96\cdot\frac{0.2010}{\sqrt{n}} \le 0.001$. So $\sqrt{n} \ge \frac{1.96 \cdot 0.2010}{0.001} = 393.96$, and $n \ge 155{,}200$ (155,192, rounded up).

Check: the exact value of the integral is $0.74682$, and $E[g^2] = \int_0^1 e^{-2x^2}\,dx = 0.59814$, so the variance is $0.59814 - 0.74682^2 = 0.04040$ and $\sigma = 0.2010$. The integrand varies little (between 0.37 and 1), so far fewer samples are needed than the 10.4 million for $\pi$ in Example 4 for the same error.

</details>

### Challenge

7\. Show that Chebyshev's inequality can't be improved: for each $k > 1$, find a random variable with $P(\lvert X - \mu \rvert \ge k\sigma) = \frac{1}{k^2}$ exactly.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Chebyshev's bound is $\frac{1}{k^2}$. What we want: a distribution where equality holds. The plan is to put all the probability that is not at the mean exactly at distance $k\sigma$.

Let $X = 1$ with probability $\frac{1}{2k^2}$, $X = -1$ with probability $\frac{1}{2k^2}$, and $X = 0$ otherwise, with probability $1 - \frac{1}{k^2}$. The probabilities are valid because $k > 1$. Then $\mu = 0$ and $\sigma^2 = E[X^2] = \frac{1}{k^2}$, so $\sigma = \frac{1}{k}$ and $k\sigma = 1$. Then $P(\lvert X - \mu \rvert \ge k\sigma) = P(\lvert X \rvert \ge 1) = \frac{1}{2k^2} + \frac{1}{2k^2} = \frac{1}{k^2}$.

Check with $k = 2$: $X = \pm 1$ with probability $\frac{1}{8}$ each and 0 with probability $\frac{3}{4}$. Then $\sigma^2 = \frac{1}{4}$, $\sigma = \frac{1}{2}$, and $P(\lvert X \rvert \ge 2\sigma = 1) = \frac{1}{4}$, equal to the bound.

</details>

8\. (Reviews [continuous random variables and the normal distribution](04-continuous-random-variables-and-the-normal.md).) Let $S$ be the sum of 12 independent uniform variables on $[0, 1]$. Find $E[S]$ and $\operatorname{Var}(S)$ using the uniform formulas, and use the CLT to estimate $P(\lvert S - 6 \rvert > 2)$. A simulation of 100,000 sums gave 0.0432. Is that consistent?

<details class="solution" markdown>
<summary>Solution</summary>

Each uniform variable has mean $\frac{1}{2}$ and variance $\frac{1}{12}$ (Theorem 1 of the previous lesson), so $E[S] = 12 \cdot \frac{1}{2} = 6$ and, by independence, $\operatorname{Var}(S) = 12 \cdot \frac{1}{12} = 1$. The CLT says that $S$ is approximately $N(6, 1)$, so $P(\lvert S - 6 \rvert > 2) \approx 2\bigl(1 - \Phi(2)\bigr) = 0.0455$.

The simulated 0.0432 is 0.0023 below. The standard error of a simulated frequency near 0.045 with 100,000 runs is $\sqrt{\frac{0.045 \cdot 0.955}{100{,}000}} = 0.00066$. The exact value for a sum of 12 uniforms (the Irwin-Hall distribution, computed in Python) is $0.0446$, which is 0.0014 below the CLT value, because the sum is bounded between 0 and 12 and has slightly lighter tails than the normal. The simulated 0.0432 is within about two standard errors of 0.0446, so the three numbers are consistent.

Check: the mean and variance are exact (6 and 1), and only the tail probability is approximate. At $n = 12$ the match of the shapes is excellent in the middle, as in the figure of the previous lesson, with small differences in the tails.

</details>

## Where this shows up

- Statistics is built on this lesson: a confidence interval is the sample mean plus or minus about two standard errors, and a hypothesis test asks how many standard errors a sample mean is from a claimed value ([confidence intervals](../08-statistics/02-confidence-intervals.md), [hypothesis testing](../08-statistics/03-hypothesis-testing.md), and [descriptive statistics and study design](../08-statistics/01-descriptive-statistics-and-study-design.md)). The $\frac{1}{\sqrt{n}}$ shrinking is also the reason regression estimates are more precise with more data ([correlation and linear regression](../08-statistics/04-correlation-and-linear-regression.md)).
- In CS, Monte Carlo methods, randomized algorithms, A/B tests and the estimation of a model's error from a test set all rest on the law of large numbers and the $\frac{1}{\sqrt{n}}$ error (discrete probability<!-- link: ../../06-cs-math/03-counting-and-discrete-probability/05-discrete-probability.md -->). Chebyshev-type tail bounds are how an algorithm's analysis turns an expected cost into a high-probability guarantee.
- In finance and insurance, an insurer's average claim per customer settles near the expected claim as the number of customers grows, which is why a pool of many independent policies is predictable (insurance and expected value<!-- link: ../../08-financial-math/07-taxes-insurance-and-planning/02-insurance-and-expected-value.md -->). Investment returns violate the assumptions in two ways, correlated terms and heavy tails, and that is why diversification has a floor (investing returns and risk<!-- link: ../../08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk.md -->).
