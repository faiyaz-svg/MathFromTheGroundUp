# Investing returns and risk

After this lesson you can compute a holding-period and an annualized return, explain why the arithmetic mean of yearly returns overstates how fast your money grew, estimate the cost of volatility, and calculate how combining two investments changes the risk of a portfolio.

Before this: [compound interest](../02-interest-and-growth/02-compound-interest.md), [logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md), [descriptive statistics](../../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md) and [covariance and sums of random variables](../../05-university-core/07-probability/05-joint-distributions-covariance-and-sums.md).

Every return, volatility and correlation in this lesson is a made-up example chosen to make the arithmetic clear. None of them is a forecast or a claim about any real market. This is a lesson about the math of investing, not advice about what to buy.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. You put \$1,000 in a fund. It gains 50% in year 1 and loses 50% in year 2. What is the balance after two years?
2. An investment grows from \$8,000 to \$9,261 in 3 years. What is the annualized return?
3. A fund returns +30% one year and $-10\%$ the next. Find the arithmetic mean of the two returns and the single yearly rate that gives the same two-year growth.

<details class="solution" markdown>
<summary>Answers</summary>

1. $1000 \times 1.5 \times 0.5 = 750$, so \$750. The average of +50% and $-50\%$ is 0%, and you still lost a quarter of your money.
2. The growth factor is $\frac{9261}{8000} = 1.157625$, and $1.157625^{1/3} = 1.05$, so the annualized return is 5%. (Indeed $8000 \times 1.05^3 = 9261$.)
3. The arithmetic mean is $\frac{30 + (-10)}{2} = 10\%$. The growth factors multiply to $1.3 \times 0.9 = 1.17$, and $\sqrt{1.17} \approx 1.0817$, so the single yearly rate is about 8.17%.

</details>

## The idea

Suppose a friend says their investments "averaged 10% a year for the last two years". It sounds like \$1,000 should have become \$1,210. But if the two years were +30% and $-10\%$, the money grew to \$1,170, which is the same as earning 8.17% a year. The average of the yearly returns was 10%, and the growth you actually got was lower.

Two things drive the gap. The first is that returns multiply instead of adding: a 30% gain is applied to the starting balance, and the next year's $-10\%$ is applied to the bigger balance. The second is that losses hurt more than equal gains help, because a loss shrinks the base that later gains work on. The more the yearly returns bounce around, the larger the gap between the "average" and what you earned.

That bounce is called volatility, and it is the usual way of measuring how risky an investment is. This lesson builds the vocabulary (returns, averages, volatility), proves the inequality behind the gap, gives a rule of thumb for its size, and then looks at the one free improvement the math offers: spreading money over assets that don't move in lockstep.

![Ten thousand made-up 30-year paths for \$10,000 invested at an average of 7% a year with 15% volatility, shown as bands. The median ends near \$57,000, below the \$76,000 that a steady 7% would give. The 5th to 95th percentile band ends between about \$15,000 and \$203,000.](../../assets/figures/08-financial-math/investing-returns-and-risk-fan.svg)

The picture shows 10,000 simulated 30-year paths for \$10,000, built in [In code](#in-code) below. Every path faces the same average return, and the outcomes still spread out over a factor of more than 10. The orange dashed line is a steady 7% a year, and the typical (median) path ends below it.

## Definitions

The **holding-period return** of an investment is the total gain over the time you hold it, as a fraction of what you started with. If $V_0$ is the starting value, $V_1$ the ending value and $I$ any income received along the way (dividends or interest, not reinvested):

$$
R = \frac{V_1 - V_0 + I}{V_0}.
$$

In plain words, it is "what you got out, minus what you put in, divided by what you put in". The number $1 + R$ is the **growth factor**: \$2,000 that ends at \$2,260 after paying \$40 of income has $R = \frac{2260 - 2000 + 40}{2000} = 0.15$, a growth factor of 1.15.

The **annualized return** of a holding-period return $R$ over $n$ years is the single yearly rate that, compounded for $n$ years, gives the same growth:

$$
(1 + r_{\text{ann}})^n = 1 + R, \qquad r_{\text{ann}} = (1 + R)^{1/n} - 1.
$$

In plain words, it is the $n$-th root of the growth factor, minus 1. The 15% over two years above is $1.15^{1/2} - 1 \approx 7.24\%$ a year, which is a little less than half of 15% because of compounding. This is the same idea as the compound annual growth rate in [growth rates and CAGR](../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md).

Given yearly returns $r_1, r_2, \ldots, r_n$ (as decimals), the **arithmetic mean** is the usual average, $\bar{r} = \frac{r_1 + \cdots + r_n}{n}$. The **geometric mean return** is the annualized return of the whole sequence:

$$
g = \left[(1 + r_1)(1 + r_2)\cdots(1 + r_n)\right]^{1/n} - 1.
$$

In plain words, multiply the growth factors, take the $n$-th root, subtract 1. The arithmetic mean answers "what was a typical single year?". The geometric mean answers "what steady rate would have given the same final balance?".

The **volatility** of an investment is the standard deviation of its periodic returns. For a sample of returns, it is the sample standard deviation $s$ from [descriptive statistics](../../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md), the typical distance of a return from the mean. In plain words, a fund with 20% volatility has yearly returns that typically land about 20 percentage points away from its average. Volatility depends on the period: it is usually quoted per year. If the returns of different months are independent, variances add, so an annual volatility is the monthly one times $\sqrt{12}$.

## How to do it

### Comparing a sequence of returns

1. Write each return as a decimal and form the growth factors $1 + r_i$.
2. Multiply the growth factors to get the total growth over the whole period. This is the answer to "what happened to my money".
3. Take the $n$-th root, subtract 1, and you have the geometric mean $g$ (the annualized return).
4. Find the arithmetic mean $\bar{r}$ and the volatility $s$.
5. Check the three results against each other: $g \le \bar{r}$ always (Theorem 1), and for returns of modest size $g \approx \bar{r} - \frac{s^2}{2}$ (the volatility drag).

### Why the geometric mean is never bigger

*Theorem 1 (arithmetic mean at least geometric mean, two values).* For all numbers $a \ge 0$ and $b \ge 0$,

$$
\frac{a + b}{2} \ge \sqrt{ab},
$$

and equality holds exactly when $a = b$.

We know that a square of a real number is never negative. We want to compare the sum $a + b$ with $2\sqrt{ab}$. The plan is to write $a$ and $b$ as squares of their square roots, so that the difference becomes a square.

*Proof.* Let $x = \sqrt{a}$ and $y = \sqrt{b}$, so $a = x^2$ and $b = y^2$. Then

$$
\frac{a + b}{2} - \sqrt{ab} = \frac{x^2 + y^2 - 2xy}{2} = \frac{(x - y)^2}{2} \ge 0.
$$

So $\frac{a+b}{2} \ge \sqrt{ab}$. The difference is 0 exactly when $x = y$, that is, when $a = b$. $\blacksquare$

Look back: the proof says the gap between the two means is half of a square, so it is zero only when the two numbers are equal and grows as they spread apart. Apply it to the growth factors $a = 1 + r_1$ and $b = 1 + r_2$. The arithmetic mean of the factors is $1 + \bar{r}$, and the geometric mean of the factors is $1 + g$. So $1 + \bar{r} \ge 1 + g$, which is $g \le \bar{r}$, with equality only when the two returns are the same. The inequality is also true for $n$ values (the proof uses that the logarithm is concave, which comes with calculus), and the same conclusion holds for any number of years.

The proof also gives the exact size of the gap for two years. Write $m = \frac{r_1 + r_2}{2}$ and $d = \frac{r_1 - r_2}{2}$, so that $r_1 = m + d$ and $r_2 = m - d$. Then

$$
(1 + r_1)(1 + r_2) = (1 + m + d)(1 + m - d) = (1 + m)^2 - d^2.
$$

The two-year growth is the growth at a steady rate $m$ (the arithmetic mean), minus the square of $d$. Here $d$ is half the distance between the two returns: a measure of volatility.

### The size of the drag

For a rule of thumb, we use the approximation $\ln(1 + x) \approx x - \frac{x^2}{2}$, which is accurate when $x$ is small. (It comes from the first two terms of a Taylor series, the topic of [power series and Taylor series](../../05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md).) Taking logarithms of the definition of $g$ gives $\ln(1 + g)$ as the average of the numbers $\ln(1 + r_i)$. Replace each logarithm by its two-term approximation:

$$
\ln(1 + g) \approx \frac{1}{n}\sum_i \left(r_i - \frac{r_i^2}{2}\right) = \bar{r} - \frac{\overline{r^2}}{2}.
$$

The mean of the squares is $\overline{r^2} = \sigma^2 + \bar{r}^2$, where $\sigma^2$ is the variance of the returns. Also $\ln(1 + g) \approx g - \frac{g^2}{2}$. Since $g$ is close to $\bar{r}$, the square terms $\frac{g^2}{2}$ and $\frac{\bar{r}^2}{2}$ nearly cancel, leaving

$$
g \approx \bar{r} - \frac{\sigma^2}{2}.
$$

In plain words, the geometric mean is the arithmetic mean minus half the variance. This loss is called the **volatility drag**. With 10% volatility the drag is $\frac{0.1^2}{2} = 0.5$ percentage points a year, with 20% it is 2 points, and with 30% it is 4.5 points. The drag grows with the square of the volatility, so it matters little for a calm investment and a lot for a wild one.

### Combining two assets

Put a fraction $w$ of your money in asset A and the remaining $1 - w$ in asset B. If the returns are random variables $R_A$ and $R_B$ with means $\mu_A$ and $\mu_B$, standard deviations $\sigma_A$ and $\sigma_B$, and correlation $\rho$, the portfolio return is $R_p = wR_A + (1 - w)R_B$. Its mean is the weighted average of the means (linearity of expectation). For its variance we use the rules of the covariance lesson: $\operatorname{Var}(aX) = a^2\operatorname{Var}(X)$, $\operatorname{Cov}(aX, bY) = ab\operatorname{Cov}(X, Y)$ and $\operatorname{Cov}(X, Y) = \rho\sigma_X\sigma_Y$. Then

$$
\sigma_p^2 = w^2\sigma_A^2 + (1 - w)^2\sigma_B^2 + 2w(1 - w)\rho\,\sigma_A\sigma_B.
$$

When $\rho = 1$ the right side is $\bigl(w\sigma_A + (1 - w)\sigma_B\bigr)^2$, so the portfolio volatility is just the weighted average of the two volatilities and nothing is gained. For every $\rho < 1$ the volatility is lower than that average while the expected return stays the same. That gap is the benefit of **diversification**, spreading money over investments whose returns don't move together.

## Worked examples

<div class="example" markdown>

### Example 1: five years of returns

A fund (made up) returned 12%, $-8\%$, 20%, 3% and $-15\%$ in five years. Find the total growth, the annualized return, the arithmetic mean, the volatility, and compare the annualized return with the drag estimate. Then say what \$10,000 became.

Step 1: the growth factors are 1.12, 0.92, 1.20, 1.03 and 0.85.

Step 2: multiply them: $1.12 \times 0.92 \times 1.20 \times 1.03 \times 0.85 = 1.08253824$. The holding-period return is 8.25%, so \$10,000 became \$10,825.38.

Step 3: the geometric mean is $1.08253824^{1/5} - 1 = 0.015988\ldots$, about 1.60% a year.

Step 4: the arithmetic mean is $\frac{12 - 8 + 20 + 3 - 15}{5} = 2.4\%$. The deviations from 2.4% are $9.6, -10.4, 17.6, 0.6, -17.4$ points, and the sample variance is $\frac{9.6^2 + 10.4^2 + 17.6^2 + 0.6^2 + 17.4^2}{4} = 0.020331$, so the volatility is $s = 14.26\%$.

Step 5: the drag estimate is $2.4\% - \frac{0.020331}{2} = 2.4\% - 1.02\% = 1.38\%$. The true value is 1.60%, so the estimate is in the right area but not exact. Five returns this wild are a rough fit for a two-term approximation (and dividing by $n$ instead of $n - 1$ in the variance would give 1.59%, which shows how much noise a sample of five carries).

Check: the arithmetic mean would predict $10000 \times 1.024^5 = 11{,}259.00$, which is wrong by over \$430. The geometric mean reproduces the real result: $10000 \times 1.015988^5 = 10{,}825.38$. And $1.60\% \le 2.4\%$, as Theorem 1 says.

</div>

<div class="example" markdown>

### Example 2: the recovery after a loss

How big a gain do you need to get back to even after a 20% loss? After a 50% loss? After a 90% loss?

After a loss of $x$ (as a decimal), you have $1 - x$ of your money. A gain of $y$ multiplies that by $1 + y$. To get back to even we need $(1 - x)(1 + y) = 1$, so

$$
y = \frac{1}{1 - x} - 1 = \frac{x}{1 - x}.
$$

For $x = 0.2$ this is $\frac{0.2}{0.8} = 25\%$. For $x = 0.5$ it is $\frac{0.5}{0.5} = 100\%$. For $x = 0.9$ it is $\frac{0.9}{0.1} = 900\%$. The size of the needed gain explodes as the loss approaches 100%.

This is why +50% then $-50\%$ loses money. After the 50% gain you have 1.5 times your money, and the 50% loss takes half of the larger amount: $1.5 \times 0.5 = 0.75$. The annualized return is $\sqrt{0.75} - 1 \approx -13.4\%$. The drag estimate gives $0 - \frac{0.5^2}{2} = -12.5\%$, which is close, though less exact because 50% is not a small return.

Check: after a 20% loss, $0.8 \times 1.25 = 1$. After a 50% loss, $0.5 \times 2 = 1$. After a 90% loss, $0.1 \times 10 = 1$.

</div>

<div class="example" markdown>

### Example 3: a two-asset portfolio

Asset A is stock-like with an expected return of 8% and volatility of 20%. Asset B is bond-like with an expected return of 4% and volatility of 6%. These numbers are made up. You hold 60% in A and 40% in B. Find the expected return and the volatility of the portfolio for correlations $\rho = 1, 0.5, 0.2, 0$ and $-0.3$.

The expected return does not depend on $\rho$: $0.6 \times 8\% + 0.4 \times 4\% = 6.4\%$.

For the variance, the first two terms of the formula are $0.6^2 \times 0.2^2 = 0.0144$ and $0.4^2 \times 0.06^2 = 0.000576$. The covariance term is $2 \times 0.6 \times 0.4 \times \rho \times 0.2 \times 0.06 = 0.00576\rho$. So $\sigma_p^2 = 0.014976 + 0.00576\rho$, and:

| Correlation $\rho$ | Variance | Volatility $\sigma_p$ |
|---|---|---|
| $1$ | $0.020736$ | $14.40\%$ |
| $0.5$ | $0.017856$ | $13.36\%$ |
| $0.2$ | $0.016128$ | $12.70\%$ |
| $0$ | $0.014976$ | $12.24\%$ |
| $-0.3$ | $0.013248$ | $11.51\%$ |

At $\rho = 1$ the volatility is $0.6 \times 20\% + 0.4 \times 6\% = 14.4\%$, the plain weighted average, as the formula predicts. At $\rho = 0.2$ the same expected return of 6.4% comes with 1.7 points less volatility. Lower correlation gives a bigger gain.

Check: every row has a volatility at or below 14.4%, and the volatility falls as $\rho$ falls. The two numbers add up in the $\rho = 0.2$ row: $0.0144 + 0.000576 + 0.001152 = 0.016128$, whose square root is 0.12700.

</div>

<div class="example" markdown>

### Example 4: from monthly to yearly volatility (finish it yourself)

A fund's monthly returns have a standard deviation of 5% and are independent from month to month. The average yearly return is 9%. Estimate the yearly volatility and the geometric mean return.

Step 1: the variance of a year (12 independent months added) is 12 times the monthly variance: $12 \times 0.05^2 = 0.03$.

Step 2: the yearly volatility is the square root of that. Now find it, then use the drag rule to estimate the geometric mean, and check that it is below 9%.

<details class="solution" markdown>
<summary>Finish</summary>

Step 2: $\sqrt{0.03} = 0.1732$, so the yearly volatility is 17.3%. The drag is $\frac{0.03}{2} = 0.015$, that is 1.5 points, so the geometric mean is about $9\% - 1.5\% = 7.5\%$.

Check: $5\% \times \sqrt{12} = 17.32\%$ matches, and 7.5% is below the arithmetic mean of 9%, as Theorem 1 requires.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: an average return is not the return you earned. If a fund is described as "averaging 8% a year", ask whether that is the arithmetic or the geometric mean. The arithmetic mean can be much higher than the rate at which your balance actually grew. In Example 1 the arithmetic mean was 2.4% and the balance grew at only 1.6%.

</div>

<div class="warning" markdown>

Watch out: don't add percentage losses and gains. A 30% loss followed by a 30% gain is not break-even. It is $0.7 \times 1.3 = 0.91$, a 9% loss. The second percent applies to a different base, the balance after the first change.

</div>

<div class="warning" markdown>

Watch out: the drag formula $g \approx \bar{r} - \frac{\sigma^2}{2}$ is an approximation for small returns. For returns of $+30\%$ and $-10\%$ it gives 8% where the truth is 8.17%, close. For $+50\%$ and $-50\%$ it gives $-12.5\%$ where the truth is $-13.4\%$, a visible miss. The bigger the swings, the worse the fit.

</div>

<div class="warning" markdown>

Watch out: volatility is not the same thing as the chance of losing money. A fund with high volatility can have a large chance of a big gain as well as a big loss, and a calm fund can still lose to inflation over decades. Volatility measures spread, and "risk" in everyday speech also includes being short of money when you need it.

</div>

A return of exactly $-100\%$ (the whole investment is lost) gives a growth factor of 0, and the product of the growth factors becomes 0, so the geometric mean is $-100\%$ no matter how good the other years were. The arithmetic mean can look fine in such a sequence, which is another way it misleads.

Scaling volatility by $\sqrt{12}$ assumes the monthly returns are independent. If good months tend to follow good months, the yearly spread is larger, and if they tend to reverse, it is smaller. And when you estimate a standard deviation from only a few returns, expect the estimate itself to be noisy.

## Tricks and shortcuts

To estimate the drag in your head, square the volatility and halve it: 10% volatility costs about 0.5 points, 15% costs about 1.1 points ($\frac{0.15^2}{2} = 0.01125$), and 20% costs 2 points.

To find the gain needed after a loss of $x$, use $\frac{x}{1 - x}$. A 10% loss needs about 11.1%, a 20% loss needs 25%, a 30% loss needs 42.9%, and a 50% loss needs 100%.

For a portfolio of two assets with equal volatility $\sigma$ and a 50/50 split, the formula simplifies to $\sigma_p = \sigma\sqrt{\frac{1 + \rho}{2}}$. At $\rho = 0$ the volatility is $\frac{\sigma}{\sqrt{2}} \approx 0.71\sigma$, and at $\rho = -1$ it is 0.

## In code

The code simulates 10,000 made-up 30-year paths for \$10,000, with each year's return drawn independently from a normal distribution with mean 7% and standard deviation 15%. (Returns below $-95\%$ are cut off so the balance stays positive.) It needs NumPy. The figure at the top of the lesson was drawn from the same paths.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

rng = np.random.default_rng(2026)
paths, years = 10_000, 30
r = np.maximum(rng.normal(0.07, 0.15, size=(paths, years)), -0.95)
end = 10_000 * np.prod(1 + r, axis=1)

print(round(np.median(end)), round(end.mean()))          # 57081 76252
print(np.percentile(end, [5, 25, 75, 95]).round())       # [ 15167.  33444.  96112. 203040.]
print((end < 10_000).mean())                             # 0.017
print((end < 10_000 * 1.02**30).mean())                  # 0.0744
print(round((r < 0).mean(), 3))                          # 0.32

print(round(10_000 * 1.07**30))                          # 76123  (a steady 7%)
print(round(10_000 * (1 + 0.07 - 0.15**2 / 2) ** 30))    # 55437  (the drag estimate)
```

</details>

The mean of the ending values, \$76,252, is close to what a steady 7% gives, \$76,123, because the expected growth factor each year is exactly 1.07. The median, \$57,081, is much lower. It is close to the drag estimate, \$55,437, which is $10000(1 + 0.07 - \frac{0.15^2}{2})^{30}$. A few lucky paths with huge balances pull the mean up, and the typical path does worse than the mean. About 1.7% of paths end below the \$10,000 they started with, and 7.4% end below what a 2% yearly rate would have given. About a third of the individual years are losses (32%). These numbers come from the made-up model, not from any market.

## FAQ

### Why do we use the geometric mean at all if the arithmetic mean is bigger?

They answer different questions. The arithmetic mean is the best guess for the return of one future year, which is what an expected-value calculation needs. The geometric mean describes growth over many years: it is the steady rate that reproduces your final balance, so it is the right one to quote for a track record and to use when projecting a long-run median outcome.

### Is diversification a free lunch?

For a fixed expected return, yes: Example 3 shows less volatility from the same expected return of 6.4%. The word "free" needs care. Diversification can't remove the risk that all assets share (when $\rho$ is close to 1 the gain is small), and correlations are estimates that can change. The earlier lesson showed that with many assets of correlation $\rho$, the volatility has a floor of $\sqrt{\rho}\,\sigma$ and not zero.

### Does higher risk always mean higher return?

No. The usual idea is that an investment with higher volatility must offer a higher expected return, or nobody would buy it. That is a statement about expectations and prices, and it comes with no guarantee: the higher expected return is the compensation for the chance of doing badly, so it won't show up in every path, as the spread of the figure shows. Some risks are not rewarded at all, such as putting everything into a single company, which diversification can remove.

### Why does the simulation use independent returns?

It keeps the model simple enough to check by hand, and the key facts (the drag, the gap between the mean and the median) don't depend on it. Real markets have patterns that independent draws don't capture, so treat the simulation as a way to see the idea and not as a forecast.

## Practice

### Warm-up

1\. An investment grows from \$5,000 to \$5,900 in 3 years, with no other income. Find the holding-period return and the annualized return.

<details class="solution" markdown>
<summary>Solution</summary>

The holding-period return is $\frac{5900 - 5000}{5000} = 0.18$, so 18%. The annualized return is $1.18^{1/3} - 1 \approx 0.0567$, about 5.67% a year.

Check: $5000 \times 1.0567^3 \approx 5000 \times 1.17995 \approx 5900$. And 5.67% a year is a little under $\frac{18}{3} = 6\%$, as compounding requires.

</details>

2\. A fund returns +20% and then $-20\%$. Find the final value of \$100 and the annualized return over the two years.

<details class="solution" markdown>
<summary>Solution</summary>

The growth factors multiply to $1.2 \times 0.8 = 0.96$, so \$100 becomes \$96. The annualized return is $\sqrt{0.96} - 1 \approx -0.0202$, about $-2.02\%$ a year.

Check: $0.9798^2 \approx 0.96$. The arithmetic mean is 0%, and the geometric mean $-2.02\%$ is below it, as Theorem 1 says. The exact formula agrees: $(1 + 0)^2 - 0.2^2 = 0.96$.

</details>

3\. After a 30% loss, what gain brings you back to even?

<details class="solution" markdown>
<summary>Solution</summary>

Use $\frac{x}{1 - x}$ with $x = 0.3$: $\frac{0.3}{0.7} = 0.42857\ldots$, so about 42.9%.

Check: $0.7 \times 1.42857 = 1.0000$.

</details>

### Standard

4\. A fund (made up) returns 10%, $-5\%$, 15% and 0% over four years. Find the arithmetic mean, the sample volatility, the geometric mean, and the drag estimate. What does \$1,000 become?

<details class="solution" markdown>
<summary>Solution</summary>

The arithmetic mean is $\frac{10 - 5 + 15 + 0}{4} = 5\%$. The deviations are $5, -10, 10, -5$ points, so the sample variance is $\frac{25 + 100 + 100 + 25}{3} = 83.33$ in squared percentage points, that is $0.008333$, and the volatility is $s = 9.13\%$.

The growth factors are 1.10, 0.95, 1.15 and 1.00, with product $1.2017\ldots$ (exactly 1.20175). So \$1,000 becomes \$1,201.75. The geometric mean is $1.20175^{1/4} - 1 \approx 0.0470$, about 4.70%.

The drag estimate is $5\% - \frac{0.008333}{2} = 5\% - 0.417\% = 4.58\%$, close to 4.70%.

Check: the geometric mean 4.70% is below the arithmetic mean 5%, and $1000 \times 1.047^4 \approx 1201.8$, matching. The arithmetic mean would have overstated the result: $1000 \times 1.05^4 = 1215.51$.

</details>

5\. A portfolio is 50% asset A (expected return 10%, volatility 24%) and 50% asset B (expected return 5%, volatility 10%), with correlation 0.3. Find its expected return and volatility, and compare the volatility with the case $\rho = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

The expected return is $0.5 \times 10\% + 0.5 \times 5\% = 7.5\%$.

The variance is $0.5^2 \times 0.24^2 + 0.5^2 \times 0.10^2 + 2 \times 0.5 \times 0.5 \times 0.3 \times 0.24 \times 0.10 = 0.0144 + 0.0025 + 0.0036 = 0.0205$. The volatility is $\sqrt{0.0205} \approx 14.3\%$.

For $\rho = 1$, the volatility is the weighted average $0.5 \times 24\% + 0.5 \times 10\% = 17\%$. So the correlation of 0.3 lowers the volatility by about 2.7 points at the same expected return.

Check: with $\rho = 1$ the formula gives variance $0.0144 + 0.0025 + 0.0120 = 0.0289$, whose square root is 0.17. And 14.3% lies between the $\rho = 0$ value (13.0%) and the $\rho = 1$ value (17%), as it should for $\rho = 0.3$.

</details>

6\. Returns of +40% and $-20\%$ happen in two successive years. Compare the true geometric mean with the drag estimate.

<details class="solution" markdown>
<summary>Solution</summary>

The arithmetic mean is $\frac{40 - 20}{2} = 10\%$. The two returns are 30 points from the mean, so the volatility is 30% (the standard deviation of two equally likely values, using divisor 2). The drag estimate is $10\% - \frac{0.3^2}{2} = 10\% - 4.5\% = 5.5\%$.

The true geometric mean is $\sqrt{1.4 \times 0.8} - 1 = \sqrt{1.12} - 1 \approx 0.0583$, about 5.83%.

Check: the exact two-year formula gives $(1 + 0.1)^2 - 0.3^2 = 1.21 - 0.09 = 1.12$, matching $1.4 \times 0.8$. The estimate, 5.5%, is below the truth by 0.3 points, which is the fit error you expect for returns this large.

</details>

### Challenge

7\. Prove that for two yearly returns $r_1$ and $r_2$ with arithmetic mean $m$, the two-year growth factor is $(1 + m)^2 - d^2$ where $d = \frac{r_1 - r_2}{2}$, and conclude that two years of volatile returns always grow your money less than two years at the steady rate $m$, unless $r_1 = r_2$.

<details class="solution" markdown>
<summary>Solution</summary>

We know $m = \frac{r_1 + r_2}{2}$ and $d = \frac{r_1 - r_2}{2}$. Adding and subtracting gives $r_1 = m + d$ and $r_2 = m - d$. Then

$$
(1 + r_1)(1 + r_2) = (1 + m + d)(1 + m - d) = (1 + m)^2 - d^2,
$$

using the difference of squares. Since $d^2 \ge 0$, the two-year factor is at most $(1 + m)^2$, the factor for a steady rate $m$. Equality needs $d = 0$, which means $r_1 = r_2$. $\blacksquare$

Check with Quick check question 3: $m = 0.1$, $d = 0.2$, so the factor is $1.21 - 0.04 = 1.17$, which equals $1.3 \times 0.9$.

</details>

8\. (Reviews [logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md).) A fund's balance grows at a geometric mean of 5.875% a year, the drag estimate for 7% with 15% volatility. How many years until the balance doubles? How many years at a steady 7%?

<details class="solution" markdown>
<summary>Solution</summary>

We need $1.05875^n = 2$, so $n = \frac{\ln 2}{\ln 1.05875} = \frac{0.69315}{0.05709} \approx 12.14$ years. At a steady 7%, $n = \frac{\ln 2}{\ln 1.07} = \frac{0.69315}{0.06766} \approx 10.24$ years.

So the drag adds about 1.9 years to the doubling time.

Check: $1.05875^{12.14} \approx 2.00$ and $1.07^{10.24} \approx 2.00$.

</details>

## Where this shows up

- The next lesson, [index funds, fees and dollar-cost averaging](02-index-funds-fees-and-dollar-cost-averaging.md), uses the same made-up simulation to compare investing a lump sum with investing a bit at a time, and shows how a small yearly fee compounds into a large cost. Real returns are also eroded by inflation ([inflation and real returns](../02-interest-and-growth/06-inflation-and-real-returns.md)).
- In economics and statistics, the mean and variance of a sum of random variables, covariance and correlation drive portfolio theory, and the gap between the mean and the median of a skewed outcome appears again in [the law of large numbers](../../05-university-core/07-probability/06-law-of-large-numbers-and-clt.md).
- Simulation of random paths is a standard programming exercise (Monte Carlo methods), and AM-GM is a standard tool in algorithm analysis and optimization.
