# Growth rates and CAGR

After this lesson you can compute a period growth rate, annualize a monthly or quarterly rate, find a compound annual growth rate (CAGR) from two values, estimate a doubling time with the rule of 70, use log differences as continuous growth rates, and find the growth rate of a product, a ratio or a per-capita figure.

Before this: [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md), [exponential and logarithmic equations](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md) and [percent change vs percentage points](02-percent-change-vs-percentage-points.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A price index grows 0.5% every month. What is the growth over 12 months, and how does it compare with $12 \times 0.5\%$?
2. An investment grows from \$50 to \$80 in 6 years. What is the compound annual growth rate?
3. By the rule of 70, about how long does a quantity growing 3.5% a year take to double?

<details class="solution" markdown>
<summary>Answers</summary>

1. The twelve monthly multipliers give $1.005^{12} = 1.0617$, a 6.17% rise. It is a little more than $12 \times 0.5\% = 6\%$, because each month's 0.5% is taken of a bigger base.
2. $\left(\frac{80}{50}\right)^{1/6} - 1 = 1.6^{1/6} - 1 = 0.0815$, about 8.15% a year.
3. $\frac{70}{3.5} = 20$ years. (The exact value is $\frac{\ln 2}{\ln 1.035} = 20.15$ years.)

</details>

## The idea

Canada's consumer price index (CPI) stood at 136.2 in September 2019 and at 170.0 in September 2026 (Bank of Canada, [consumer price index data](https://www.bankofcanada.ca/rates/price-indexes/cpi/), from Statistics Canada Table 18-10-0004-01; index with 2002 = 100). Prices rose $\frac{170.0}{136.2} - 1 = 24.8\%$ over seven years. If someone asks "how fast is that per year?", the tempting answer is $\frac{24.8\%}{7} = 3.5\%$. That is too high. The right answer is the yearly rate that, applied seven times in a row, turns 136.2 into 170.0, and it comes out at 3.2% a year.

Economic data arrive as growth rates over different periods: a quarter, a month, a year. They have to be compared on the same footing (annualized), turned into one average rate over a long span (CAGR), and combined across variables (GDP per person, revenue from price and quantity). The tools are the exponential growth formulas from high school, with a few conventions that economists use. The most useful convention is that for small rates, percent changes behave like logarithms, so growth rates of products and ratios can be added and subtracted.

## Definitions

Let $x_t$ be the value of a variable in period $t$, with $x_{t-1} > 0$. The **growth rate** over period $t$ is the percent change from the previous period, as a decimal:

$$
g_t = \frac{x_t - x_{t-1}}{x_{t-1}}.
$$

The number $1 + g_t = \frac{x_t}{x_{t-1}}$ is the **growth factor** for the period (the multiplier from [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md)). In plain words, the growth rate is the change as a fraction of last period's level. A growth rate is a rate in the sense of [the first lesson](01-how-economists-use-math-and-graphs.md), a ratio with no units except "per period".

To **annualize** a rate means to restate a growth rate for a period shorter than a year as the growth over a full year at the same pace. If a period is $\frac{1}{k}$ of a year ($k = 12$ for months, $k = 4$ for quarters) and the growth rate per period is $g$, the **annualized rate** (compounded) is

$$
(1 + g)^k - 1.
$$

The simple annualized rate is $k \times g$, which is the version often used for a quick estimate. In plain words, compounded annualizing asks "if every month were like this one, how much would prices rise in 12 months?".

The **compound annual growth rate** (CAGR) from a starting value $x_0$ to an ending value $x_n$ over $n$ years is the constant yearly rate $g$ with $x_0(1 + g)^n = x_n$, that is,

$$
\text{CAGR} = \left(\frac{x_n}{x_0}\right)^{1/n} - 1 = e^{\frac{\ln(x_n/x_0)}{n}} - 1.
$$

In plain words, it is the steady yearly growth that would give the same result as the actual, bumpy path. It depends only on the first value, the last value and the number of years between them. The number $n$ is the number of years elapsed, so from 2019 to 2026 it is 7, and not the 8 values on the list.

The **continuous growth rate** (or log growth rate) from $x_0$ to $x_n$ over $n$ years is

$$
\frac{\ln x_n - \ln x_0}{n} = \frac{\ln(x_n/x_0)}{n}.
$$

The quantity $\ln x_t - \ln x_{t-1}$ is a **log difference**. In plain words, a log difference is the growth rate you would get if growth happened continuously through the period, the $e^{kt}$ model from [exponential functions and growth](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md).

The **doubling time** is the time $t_d$ with $(1 + g)^{t_d} = 2$. The **rule of 70** says that at a growth rate of $R\%$ per period, the doubling time is about $\frac{70}{R}$ periods.

## How to do it

### Annualizing a monthly or quarterly rate

1. Find the growth factor for the short period, $\frac{x_t}{x_{t-1}}$, and the number $k$ of such periods in a year.
2. Raise the factor to the power $k$: $\left(\frac{x_t}{x_{t-1}}\right)^k$.
3. Subtract 1 and write it as a percent. That is the compounded annualized rate.
4. For a quick estimate, multiply the short-period rate by $k$. It is accurate for small rates and gets worse as the rate grows.
5. Remember that annualized is not the same as year-over-year. An annualized monthly rate says what would happen if the month repeated 12 times. The year-over-year rate compares with the same month a year ago, and it measures what did happen.

Statistics Canada reports quarterly GDP growth "at annual rates", which means the compounded annualizing in Step 3. A quarterly growth of 0.6% is $1.006^4 - 1 = 2.4\%$ at an annual rate.

### Computing a CAGR

1. Write the start value $x_0$, the end value $x_n$ and the number of years $n$ between them (the difference of the dates).
2. Divide: the total growth factor is $\frac{x_n}{x_0}$.
3. Take the $n$-th root, which is the power $\frac{1}{n}$: $\left(\frac{x_n}{x_0}\right)^{1/n}$. On a calculator, take $\ln$ of the ratio, divide by $n$, and apply $e^{(\cdot)}$.
4. Subtract 1 and convert to a percent.
5. Check by compounding: $x_0 (1 + g)^n$ should return $x_n$.

Steps 3 and the log form agree because $a^{1/n} = e^{\ln(a)/n}$, which follows from $a = e^{\ln a}$ and the power rule for exponents.

The CAGR is not the average of the yearly growth rates. The plain average of the yearly rates is the arithmetic mean, and the CAGR is the geometric mean of the growth factors, minus 1. By the AM-GM inequality, the arithmetic mean of the rates is at least the CAGR, and strictly larger unless every year's rate is identical. The gap grows with the variability of the yearly rates: rates of $+50\%$ and $-50\%$ average to 0%, and the CAGR is $\sqrt{0.75} - 1 = -13.4\%$. Look at [percent change vs percentage points](02-percent-change-vs-percentage-points.md#averaging-percent-changes) for the same warning from the other direction.

### Doubling time and the rule of 70

Setting $(1 + g)^{t_d} = 2$ and taking logs, as in [exponential and logarithmic equations](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md):

$$
t_d = \frac{\ln 2}{\ln(1 + g)}.
$$

For a small rate, $\ln(1 + g)$ is close to $g$ (the table later in this lesson shows how close). So $t_d \approx \frac{\ln 2}{g} = \frac{0.693}{g}$. Writing the rate as a percent, $R = 100g$, this is $\frac{69.3}{R}$, which rounds to the memorable $\frac{70}{R}$. The 70 is $100 \times \ln 2$, and the reason for it is the natural logarithm of 2.

Why 70 and not 72, which is the number in the [rule of 72](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md#the-rule-of-72)? Because $\ln(1 + g)$ is a little less than $g$, the true doubling time is a little more than $\frac{69.3}{R}$. For rates around 8% the correction pushes it to about 72. This table compares the three numbers, computed from the exact formula:

| Rate $R\%$ | Exact $\frac{\ln 2}{\ln(1 + R/100)}$ | Rule of 70 | Rule of 72 |
|---|---|---|---|
| 1 | 69.66 | 70.0 | 72.0 |
| 2 | 35.00 | 35.0 | 36.0 |
| 3.5 | 20.15 | 20.0 | 20.6 |
| 5 | 14.21 | 14.0 | 14.4 |
| 7 | 10.24 | 10.0 | 10.3 |
| 10 | 7.27 | 7.0 | 7.2 |

For the low rates that dominate macroeconomics (inflation, GDP growth), 70 is the better rule. For interest rates of 6% to 10%, 72 is. Both are mental arithmetic, and neither is a replacement for the formula when you need two decimals.

### Continuous growth rates and log differences

Take $x_t = x_{t-1}(1 + g)$ and take natural logs of both sides:

$$
\ln x_t - \ln x_{t-1} = \ln(1 + g).
$$

So the log difference is $\ln(1 + g)$, which is a bit less than $g$. For small $g$ the two nearly agree. Using the exact values:

| $g$ | $\ln(1 + g)$ | Difference |
|---|---|---|
| 1% | 0.00995 | $-0.00005$ |
| 5% | 0.04879 | $-0.00121$ |
| 10% | 0.09531 | $-0.00469$ |
| 20% | 0.18232 | $-0.01768$ |
| 50% | 0.40547 | $-0.09453$ |

The approximation $\ln(1 + g) \approx g$ is excellent below 5% and rough above 20%. The reason economists use log differences anyway is a property that percent changes lack.

*Theorem (log differences add over time).* For positive values $x_0, x_1, \dots, x_n$,

$$
\sum_{t=1}^{n} (\ln x_t - \ln x_{t-1}) = \ln x_n - \ln x_0.
$$

What we know: each term is the log of a ratio, and the logarithm turns products into sums ([logarithm properties](../../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md)). What we want: the total log growth equals the sum of the period log growths, exactly. The plan is to write out the sum and watch the middle terms cancel.

Proof. Writing the sum out gives $(\ln x_1 - \ln x_0) + (\ln x_2 - \ln x_1) + \cdots + (\ln x_n - \ln x_{n-1})$. Each $\ln x_t$ for $0 < t < n$ appears once with a plus sign and once with a minus sign, so those terms cancel in pairs, and $\ln x_n - \ln x_0$ remains. $\blacksquare$

Looking back: this is a telescoping sum. Percent changes do not telescope. A rise of 10% followed by a fall back to the start is $+10\%$ and $-9.09\%$, which sum to $+0.91\%$ although nothing changed overall. The log differences are $+0.0953$ and $-0.0953$, which sum to exactly 0. So for a long series, economists often chart $100 \times \ln x_t$ differences, and an average log difference over $n$ periods is exactly the continuous growth rate.

The continuous growth rate and the CAGR are linked: if the continuous rate is $k$, then $\text{CAGR} = e^{k} - 1$, and conversely $k = \ln(1 + \text{CAGR})$. For the CPI from 2019 to 2026, $k = \frac{\ln(170.0/136.2)}{7} = 3.17\%$ and $\text{CAGR} = e^{0.0317} - 1 = 3.22\%$.

### Growth of a product, a ratio or a per-capita figure

Let $z = xy$, with growth factors $1 + g_x$ and $1 + g_y$ over a period.

*Theorem.* $1 + g_z = (1 + g_x)(1 + g_y)$, so $g_z = g_x + g_y + g_x g_y$, and for small rates $g_z \approx g_x + g_y$.

What we know: $z_t = x_t y_t$ in both periods. What we want: the growth factor of $z$ in terms of those of $x$ and $y$. The plan is to divide $z_t$ by $z_{t-1}$.

Proof. $\frac{z_t}{z_{t-1}} = \frac{x_t y_t}{x_{t-1} y_{t-1}} = \frac{x_t}{x_{t-1}} \cdot \frac{y_t}{y_{t-1}} = (1 + g_x)(1 + g_y)$. Expanding, $1 + g_z = 1 + g_x + g_y + g_x g_y$. The cross term $g_x g_y$ is the product of two small numbers, so it is much smaller than either. $\blacksquare$

Looking back: in logs the statement is exact, $\ln z = \ln x + \ln y$, so the log growth of a product is exactly the sum of the log growths. The same argument for a ratio $w = \frac{x}{y}$ gives $1 + g_w = \frac{1 + g_x}{1 + g_y}$, and $g_w \approx g_x - g_y$ (exactly $\ln w = \ln x - \ln y$ in logs).

So revenue growth is about price growth plus quantity growth. Real GDP per person grows at about the growth of real GDP minus the growth of population. A debt-to-GDP ratio rises when debt grows faster than GDP. The exact versions are in the proof, and the approximations are good when rates are a few percent.

## Worked examples

<div class="example" markdown>

### Example 1: annualizing a monthly CPI change

The CPI was 169.8 in August 2026 and 170.0 in September 2026 (Bank of Canada, [consumer price index data](https://www.bankofcanada.ca/rates/price-indexes/cpi/), Statistics Canada Table 18-10-0004-01). Find the monthly growth and the annualized rate, in the unadjusted index and in the seasonally adjusted one, which was 169.4 in August and 170.0 in September.

Step 1: unadjusted growth factor $\frac{170.0}{169.8} = 1.001178$, so monthly growth is 0.118%. There are $k = 12$ months in a year.

Step 2: $1.001178^{12} = 1.01423$.

Step 3: the annualized rate is 1.42%. The quick estimate $12 \times 0.118\% = 1.41\%$ is close.

Seasonally adjusted: $\frac{170.0}{169.4} = 1.003542$, so monthly growth is 0.354%, and $1.003542^{12} - 1 = 4.33\%$ annualized. The quick estimate is 4.25%.

Check: a monthly rate of 0.354% repeated 12 times gives $1.00354^{12} = 1.0433$. The annualized seasonally adjusted rate (4.3%) is far above the 3.1% year-over-year rate for September 2026, which is possible: one month's growth, repeated for 12 months, is a statement about that month alone. Watch out: a monthly rate has noise, which annualizing multiplies by 12. One month is not a trend.

</div>

<div class="example" markdown>

### Example 2: the CAGR of the CPI

Using the CPI of 136.2 (September 2019) and 170.0 (September 2026), find the CAGR over those 7 years.

Step 1: $x_0 = 136.2$, $x_n = 170.0$, and $n = 2026 - 2019 = 7$ years (not 8).

Step 2: the total growth factor is $\frac{170.0}{136.2} = 1.24816$, so the total growth is 24.8%.

Step 3: take the seventh root. By logs, $\ln 1.24816 = 0.22167$, and $\frac{0.22167}{7} = 0.031668$. Then $e^{0.031668} = 1.03217$.

Step 4: CAGR $= 3.22\%$ a year.

Step 5: check by compounding: $136.2 \times 1.03217^{7} = 170.0$.

Compare with the arithmetic mean of the seven September-to-September rates computed from the same index (0.51%, 4.38%, 6.86%, 3.80%, 1.64%, 2.36%, 3.09%), which is 3.23%. It is above the CAGR 3.22%, as the AM-GM inequality says, and close because the rates vary only moderately. The tempting shortcut $\frac{24.8\%}{7} = 3.5\%$ is worse, because it ignores compounding.

</div>

<div class="example" markdown>

### Example 3: doubling time of prices

How long do prices take to double at (a) the Bank of Canada's 2% inflation target, (b) the 3.1% inflation rate of September 2026 (Statistics Canada via the Bank of Canada, as in Example 1)?

(a) The rule of 70 gives $\frac{70}{2} = 35$ years. The exact formula gives $\frac{\ln 2}{\ln 1.02} = \frac{0.6931}{0.01980} = 35.00$ years.

(b) The rule gives $\frac{70}{3.1} = 22.6$ years. The exact formula is $\frac{0.6931}{\ln 1.031} = \frac{0.6931}{0.03053} = 22.7$ years.

Check: $1.02^{35} = 1.9999$ and $1.031^{22.7} = 2.00$. If inflation stays at 3.1% a year, a dollar buys half as much in about 23 years. At 2% the same halving takes 35 years.

</div>

<div class="example" markdown>

### Example 4: real GDP per person (finish it yourself)

These are made-up numbers. An economy's real GDP grows 3.0% in a year while its population grows 1.2%. Find the growth rate of real GDP per person, first by the approximation and then exactly.

The approximation is the difference of the growth rates, $3.0 - 1.2 = 1.8\%$. For the exact value use the ratio theorem: the growth factor of the ratio is $\frac{1.030}{1.012}$.

Now compute the exact growth rate, and also the log-difference version $\ln 1.030 - \ln 1.012$. Which is closer to the exact value?

<details class="solution" markdown>
<summary>Finish</summary>

$\frac{1.030}{1.012} = 1.017787$, so exact per-person growth is 1.779%. The log-difference version is $\ln 1.030 - \ln 1.012 = 0.029559 - 0.011929 = 0.017630$, or 1.763%, which is the continuous per-person growth rate. The plain difference $1.8\%$ is a bit above the exact 1.779%, and the log difference is a bit below it. All three agree to within 0.04 points.

Check: $1.017787 \times 1.012 = 1.030$, so per-person output grew by exactly the factor that recovers the 3.0% total.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the CAGR uses the number of years between the dates, not the number of data points. Eight yearly values from 2019 to 2026 span 7 years. Using 8 gives $1.24816^{1/8} - 1 = 2.81\%$ in place of 3.22%.

</div>

<div class="warning" markdown>

Watch out: total growth divided by the number of years is not the yearly rate. A total rise of 24.8% over 7 years is not 3.5% a year. Compounding means a steady 3.22% a year does the job.

</div>

<div class="warning" markdown>

Watch out: do not average growth rates to get a long-run rate. Rates of $+50\%$ and $-50\%$ average to 0, yet the quantity ends 25% lower. Use the CAGR from the end values, which is the geometric mean.

</div>

<div class="warning" markdown>

Watch out: annualized is not year-over-year. An annualized quarterly GDP growth of 2.4% (from a 0.6% quarterly rise) is the pace of one quarter stretched over a year. The year-over-year growth compares with the same quarter a year earlier and could be far from 2.4%.

</div>

<div class="warning" markdown>

Watch out: the rule of 70 is for a rate per period and a doubling time in the same periods. A monthly rate of 1% gives 70 months, not 70 years.

</div>

The CAGR needs both values positive. A series that crosses zero (a profit that turns into a loss, net exports) has no CAGR, and neither does a ratio with a zero start. A negative CAGR is allowed: a fall from 100 to 80 over 5 years is $0.8^{1/5} - 1 = -4.36\%$ a year. The CAGR also hides what happened between the dates: a series that went from 100 to 150 in the first year and drifted down to 130 has the same CAGR over 5 years as one that rose steadily.

Log differences are for small changes. For a 50% rise the log difference is 40.5%, and calling it "growth of 40.5%" is wrong in the usual sense. Use the percent change when a reader expects one, and log differences for modelling and for adding changes over time.

## Tricks and shortcuts

For a small rate, annualize a monthly rate by multiplying by 12 and a quarterly rate by 4, and add a correction if you want more digits: the compounded rate is about $kg + \frac{k(k-1)}{2}g^2$. For $g = 0.5\%$ and $k = 12$ that is $6\% + 66 \times 0.000025 = 6.165\%$, against the exact 6.168%.

A fast CAGR: from the doubling time. If a series doubled in 10 years, then $\frac{70}{10} = 7$, about 7% a year. If it tripled in 16 years, $\ln 3 \approx 1.1$, so the rate is about $\frac{110}{16} \approx 6.9\%$. The idea is $R \approx \frac{100 \ln(\text{total factor})}{n}$.

To find the rate that gives a target doubling time, divide: a doubling in 25 years needs about $\frac{70}{25} = 2.8\%$.

When you must go from a yearly rate to a monthly one, take the twelfth root, not a twelfth: a yearly rate of 2% is $1.02^{1/12} - 1 = 0.165\%$ a month, and $\frac{2\%}{12} = 0.1667\%$ is slightly too high.

## In code

Four small functions cover the lesson: annualizing, the CAGR, the doubling time and a log difference.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def annualize(g, k):
    """Compounded annual rate from a rate g per period, k periods a year."""
    return (1 + g) ** k - 1

def cagr(start, end, years):
    return (end / start) ** (1 / years) - 1

def doubling_time(g):
    return math.log(2) / math.log(1 + g)

print(round(annualize(170.0 / 169.8 - 1, 12) * 100, 2))   # 1.42
print(round(annualize(170.0 / 169.4 - 1, 12) * 100, 2))   # 4.33
print(round(cagr(136.2, 170.0, 7) * 100, 2))              # 3.22
print(round(doubling_time(0.02), 2), round(70 / 2, 2))    # 35.0 35.0
print(round(doubling_time(0.031), 1))                     # 22.7

# Log differences add exactly, percent changes do not
series = [100, 110, 100]
pct = [b / a - 1 for a, b in zip(series, series[1:])]
logs = [math.log(b) - math.log(a) for a, b in zip(series, series[1:])]
print([round(x, 4) for x in pct], round(sum(pct), 4))     # [0.1, -0.0909] 0.0091
print([round(x, 4) for x in logs], round(sum(logs), 4))   # [0.0953, -0.0953] 0.0
```

</details>

## FAQ

### Why compound the annualized rate and not just multiply by 12?

Because growth does compound. If prices rise 0.5% a month, the second month's 0.5% applies to a higher base. Multiplication is a fine shortcut for small rates, and it understates the true result more as the rate grows: at 5% a month the compounded annual rate is 79.6% while $12 \times 5\%$ is 60%.

### Which is better, CAGR or the average yearly rate?

They answer different questions. The CAGR says what steady rate reproduces the end value, so it is the right summary for "how much did this grow per year". The average of yearly rates is larger or equal, and it is what you would expect from a randomly chosen year. For a long investment horizon the CAGR is the one that tells you what happened to the money.

### Why does economics prefer log differences?

They add over time and they turn products and ratios into sums and differences exactly. They are also symmetric: a rise from 100 to 110 and a fall from 110 to 100 have log differences of $+0.0953$ and $-0.0953$. The cost is that they are not what readers expect, so reports convert back to percent changes.

### Is 70 or 72 the right number?

Both are approximations to $\frac{100 \ln 2}{\ln(1 + g)}$. Use 70 for small rates (below about 4%) and 72 for rates near 8%. The table in this lesson shows the errors.

## Practice

### Warm-up

1\. A quarterly growth rate is 0.8%. Find the compounded annualized rate and the simple estimate.

<details class="solution" markdown>
<summary>Solution</summary>

Compounded: $1.008^4 - 1 = 0.03239$, so 3.24%. Simple: $4 \times 0.8\% = 3.2\%$.

Check: the compounded figure is slightly larger, as it should be.

</details>

2\. A quantity grows from 200 to 260 in 3 years. Find the CAGR.

<details class="solution" markdown>
<summary>Solution</summary>

The total factor is $\frac{260}{200} = 1.3$, and the CAGR is $1.3^{1/3} - 1 = 0.0914$, about 9.14% a year.

Check: $1.0914^3 = 1.3000$. (The shortcut $\frac{30\%}{3} = 10\%$ is too high.)

</details>

3\. By the rule of 70, how long does a quantity growing 5% a year take to double? What is the exact value?

<details class="solution" markdown>
<summary>Solution</summary>

$\frac{70}{5} = 14$ years. Exactly, $\frac{\ln 2}{\ln 1.05} = \frac{0.6931}{0.04879} = 14.21$ years.

Check: $1.05^{14} = 1.980$ and $1.05^{14.21} = 2.000$.

</details>

### Standard

4\. An index of real output was 100 ten years ago and is 138 today. (a) Find the CAGR. (b) At that pace, what will the index be in 10 more years? (c) What is the doubling time?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $1.38^{1/10} - 1 = 0.03273$, about 3.27% a year.

(b) Another 10 years multiplies by 1.38 again: $138 \times 1.38 = 190.4$.

(c) $\frac{\ln 2}{\ln 1.03273} = 21.5$ years. The rule of 70 gives $\frac{70}{3.27} = 21.4$ years.

Check: $1.03273^{10} = 1.380$.

</details>

5\. A series is 80, then 100, then 90. (a) Find the percent changes and the log differences. (b) Add each pair. Which sum equals the overall change from 80 to 90?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Percent changes: $\frac{100}{80} - 1 = 25\%$ and $\frac{90}{100} - 1 = -10\%$. Log differences: $\ln \frac{100}{80} = 0.2231$ and $\ln \frac{90}{100} = -0.1054$.

(b) The percent changes sum to 15%, while the actual change from 80 to 90 is $\frac{90}{80} - 1 = 12.5\%$. The log differences sum to $0.1178$, which equals $\ln \frac{90}{80}$ exactly.

Check: $e^{0.1178} = 1.125$.

</details>

6\. A firm's price rises 4% and its quantity sold falls 3%. (a) Find the exact change in revenue. (b) Find the approximation by adding the growth rates. (c) Find the exact change in the ratio price per unit quantity, $\frac{p}{q}$, and compare with the difference of the rates.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $1.04 \times 0.97 = 1.0088$, so revenue rises 0.88%. (b) $4\% - 3\% = 1\%$, a little high. (c) $\frac{1.04}{0.97} = 1.0722$, a rise of 7.2%, against the approximation $4\% - (-3\%) = 7\%$.

Check: $1.0088 \times 100 = 100.88$ and $104 \times 0.97 = 100.88$.

</details>

### Challenge

7\. Monthly price growth is 0.25% for a year. (a) What is the annualized rate, compounded? (b) What monthly rate gives exactly 2% for the year? (c) A student divides 2% by 12 to get a monthly rate. By how much do the resulting yearly prices overshoot 2%?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $1.0025^{12} - 1 = 0.03042$, which is 3.04%, a bit above the simple estimate 3%.

(b) $1.02^{1/12} - 1 = 0.001652$, so 0.1652% a month.

(c) $\frac{2\%}{12} = 0.16667\%$ a month gives $\left(1 + \frac{0.02}{12}\right)^{12} - 1 = 0.020184$, or 2.018%, so it overshoots by about 0.018 percentage points.

Check: $1.001652^{12} = 1.0200$.

</details>

8\. (Reviews [exponential functions and growth](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md).) A town of 400 people grows 8% a year. How long until it doubles, by the exact formula, the rule of 70 and the rule of 72? Which is closest?

<details class="solution" markdown>
<summary>Solution</summary>

Exact: $\frac{\ln 2}{\ln 1.08} = \frac{0.6931}{0.07696} = 9.01$ years. Rule of 70: $\frac{70}{8} = 8.75$. Rule of 72: $\frac{72}{8} = 9.00$. The rule of 72 is closest at 8%.

Check: $400 \times 1.08^{9.01} = 800$.

</details>

## Where this shows up

- [Index numbers](04-index-numbers.md) are the data behind most growth rates, and [nominal vs real GDP and the deflator](06-nominal-vs-real-gdp-and-the-deflator.md) uses the sum-and-difference approximations from this lesson. [CPI and inflation](07-cpi-and-inflation.md) is where the annualized monthly rate and the doubling time of prices get used.
- Finance: [compound interest](../../08-financial-math/02-interest-and-growth/02-compound-interest.md) is the CAGR formula run backwards, and [doubling time, the rule of 72 and logs](../../08-financial-math/02-interest-and-growth/05-doubling-time-rule-of-72-and-logs.md) goes further with the same ideas. [Investing returns and risk](../../08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk.md) uses the geometric mean for investment returns.
- In computer science, a quantity that doubles every fixed period (users, storage, run time) follows the same formulas, and the doubling time is the natural way to compare growth rates.
