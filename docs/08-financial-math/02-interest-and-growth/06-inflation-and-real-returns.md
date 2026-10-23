# Inflation and real returns

After this lesson you can convert a nominal return into a real return with the Fisher relation, use the approximation and know its error, find what savings are worth in today's dollars, and see how tax changes the real return.

Before this: [compound interest](02-compound-interest.md), [APR, APY and the effective annual rate](03-apr-apy-and-effective-annual-rate.md), [doubling time, the rule of 72 and logs](05-doubling-time-rule-of-72-and-logs.md) and [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md). The economics chapter measures inflation itself in [CPI and inflation](../../07-economics-math/01-measuring-the-economy/07-cpi-and-inflation.md); this lesson stays with what it does to personal money.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. An account pays 4% a year while prices rise 2.5% a year. What is the real return, to two decimal places?
2. With 2% inflation a year, what are \$10,000 worth, in today's dollars, after 20 years?
3. Inflation is 3% a year. What nominal rate gives a real return of 2%?

<details class="solution" markdown>
<summary>Answers</summary>

1. $\frac{1.04}{1.025} - 1 = 0.01463$, so 1.46%.
2. Prices are $1.02^{20}$ times as high, so the money buys $\frac{10000}{1.02^{20}} = 6729.71$, that is, \$6,729.71 in today's dollars.
3. $1.02 \times 1.03 - 1 = 0.0506$, so 5.06%.

</details>

## The idea

Suppose you deposit \$10,000 at 1.5% a year (an example rate) while prices rise 3% a year. After five years the account shows \$10,772.84, which is more than you put in. But a basket of groceries that cost \$10,000 at the start now costs $10000 \times 1.03^5 = 11{,}592.74$. The account has grown, and what it can buy has shrunk: in today's dollars your balance is worth \$9,292.75, about 7% less than you started with.

A **nominal** amount is a number of dollars. A **real** amount is the same money measured by what it can buy, in the dollars of one chosen year. Interest rates are quoted nominally. To know whether you are actually better off, you need the real return, which strips out the rise in prices.

This is the same arithmetic as before. Inflation compounds like interest, and a nominal rate and an inflation rate combine by multiplication, not by subtraction. The subtraction is a good approximation, and in this lesson we find out how good.

## Definitions

The **inflation rate** $\pi$ is the percent rise in the general price level over a period, written as a decimal. Prices that rise $\pi$ in a year are multiplied by $1 + \pi$. (The letter $\pi$ is used here for the inflation rate, as in economics. It is not the number 3.14.)

The **nominal return** $i$ is the growth rate of money measured in dollars. The **real return** $\rho$ (the Greek letter rho) is the growth rate of money measured by what it buys. The **Fisher relation** connects the three:

$$
1 + i = (1 + \rho)(1 + \pi).
$$

In plain words, the dollars grow by the factor $1 + i$, prices grow by $1 + \pi$, and purchasing power grows by what is left, $1 + \rho$. Solving for the real return:

$$
\rho = \frac{1 + i}{1 + \pi} - 1.
$$

The **Fisher approximation** is $\rho \approx i - \pi$: the real return is about the nominal return minus the inflation rate.

The **consumer price index** (CPI) is an index of the cost of a fixed basket of goods and services. If the CPI goes from $C_0$ to $C_1$, prices have risen by the factor $\frac{C_1}{C_0}$, so the inflation over the period is $\frac{C_1}{C_0} - 1$. Statistics Canada publishes the CPI, and the economics chapter explains how it is built. The numbers in this lesson are made up so that they don't go out of date.

The **real value** of an amount $A_1$ of money at a later time, in the dollars of the earlier time, is $A_1 \cdot \frac{C_0}{C_1}$. In plain words, divide by the price factor.

## How to do it

### Real return from a nominal return

1. Write the nominal rate $i$ and the inflation rate $\pi$ as decimals, for the same period.
2. Divide the growth factors: $\frac{1 + i}{1 + \pi}$.
3. Subtract 1 to get the real return $\rho$.
4. Check against the approximation $i - \pi$. The two should be close, and the approximation is always a little too high when $\rho > 0$.

### How good the approximation is

Multiplying out the Fisher relation gives $1 + i = 1 + \rho + \pi + \rho\pi$, so

$$
i - \pi = \rho + \rho\pi.
$$

In plain words, subtracting overstates the real return by $\rho\pi$, the product of the real return and the inflation rate. This is small when either rate is small:

| Nominal $i$ | Inflation $\pi$ | Exact real $\rho$ | Approximation $i - \pi$ | Overstated by |
|---|---|---|---|---|
| 5% | 2% | 2.941% | 3.0% | 0.059 points |
| 8% | 2% | 5.882% | 6.0% | 0.118 points |
| 12% | 9% | 2.752% | 3.0% | 0.248 points |
| 20% | 15% | 4.348% | 5.0% | 0.652 points |
| 1.5% | 3% | -1.456% | -1.5% | -0.044 points |

At the low rates typical of Canada, the approximation is good to a tenth of a percentage point or better. At high inflation, it is not: 20% against 15% is a real return of 4.35%, not 5%.

### Real value over time

To find what an amount will be worth in today's dollars, divide by the price factor: after $t$ years with inflation $\pi$, the real value of $A$ is $\frac{A}{(1 + \pi)^t}$. With a CPI you divide by the ratio of index values. An account growing at the nominal rate $i$ has real value $P\left(\frac{1 + i}{1 + \pi}\right)^t = P(1 + \rho)^t$, which is why the real return is the right rate for the real balance.

### The Bank of Canada target

Canada's inflation target is 2%. The Bank of Canada aims for 2%, the midpoint of a control range of 1% to 3%, and the current agreement with the federal government covers the five years to the end of 2026 ([Bank of Canada, inflation-control target](https://www.bankofcanada.ca/core-functions/monetary-policy/inflation-control-target/), fetched 2026-10-21). Actual inflation in a given year can be above or below it.

<div class="note" markdown>

The 2% target and its 1% to 3% range are figures for 2026. The agreement is renewed periodically and the terms can change. Check the linked page before using them for real decisions. The inflation rates used in the examples below are made up.

</div>

If prices rise 2% a year, they double in $\frac{\ln 2}{\ln 1.02} = 35.0$ years, so a dollar loses half its buying power over that time, the half-life of purchasing power from the [doubling time lesson](05-doubling-time-rule-of-72-and-logs.md). After 10 years a dollar buys $\frac{1}{1.02^{10}} = 0.82$ of what it buys now.

### Tax and the real return

Tax is charged on nominal interest. Suppose interest in an account outside a registered plan is taxed at the rate $\tau$ (the Greek letter tau, the marginal tax rate as a decimal) in the year it is earned. Then the after-tax nominal return is $i(1 - \tau)$, and the after-tax real return is

$$
\rho_{\text{after tax}} = \frac{1 + i(1 - \tau)}{1 + \pi} - 1.
$$

Inflation is not subtracted before the tax is figured, so tax takes a bigger share of the real return than it appears. In a Tax-Free Savings Account (TFSA), interest is not taxed, so $\tau = 0$. The [retirement accounts lesson](../06-investing-and-retirement/03-retirement-accounts.md) covers the TFSA, RRSP and FHSA, and the tax rates used here are only examples.

## Worked examples

<div class="example" markdown>

### Example 1: a savings account that loses to inflation

\$10,000 sits in an account at 1.5% a year for 5 years, while inflation is 3% a year. Both rates are made up. What is the balance, what is it worth in today's dollars, and what is the real return per year?

Step 1: $i = 0.015$ and $\pi = 0.03$.

Step 2: the nominal balance is $10000 \times 1.015^5 = 10772.84$, so \$10,772.84.

Step 3: the real return is $\rho = \frac{1.015}{1.03} - 1 = -0.01456$, that is, $-1.46\%$ a year. The approximation $i - \pi = -1.5\%$ is close.

Step 4: the real value is $10000 \times \left(\frac{1.015}{1.03}\right)^5 = 9292.75$, so \$9,292.75 in today's dollars. The same number comes from $\frac{10772.84}{1.03^5}$.

Check: the real value is below \$10,000 although the balance is above it. A negative real return means you can buy less.

</div>

<div class="example" markdown>

### Example 2: a GIC against 2% inflation

A 5-year GIC pays 4.5% a year compounded annually (a made-up rate), and inflation is 2% a year, the Bank of Canada's target. Find the real return and the real value of \$10,000 at maturity.

The real return is $\frac{1.045}{1.02} - 1 = 0.02451$, that is, 2.451% a year, against the approximation of 2.5%.

At maturity the balance is $10000 \times 1.045^5 = 12461.82$. In today's dollars it is $\frac{12461.82}{1.02^5} = 11287.05$, so \$11,287.05. The real gain is \$1,287.05, about half of the nominal gain of \$2,461.82.

Check: $10000 \times 1.02451^5 = 11287.05$.

</div>

<div class="example" markdown>

### Example 3: using a CPI

Suppose the CPI is 120.0 in one year and 138.0 some years later (made-up values). (a) How much did prices rise? (b) How much must you earn later to match \$1,000 earned in the first year? (c) What do \$1,000 in the later year buy, in first-year dollars?

(a) $\frac{138}{120} - 1 = 0.15$, so prices rose 15%.

(b) You need the same buying power: $1000 \times \frac{138}{120} = 1150$, that is, \$1,150.

(c) The real value is $1000 \times \frac{120}{138} = 869.57$, so \$869.57 in first-year dollars.

Check: $869.57 \times 1.15 = 1000.00$.

</div>

<div class="example" markdown>

### Example 4: after-tax real return (finish it yourself)

An account pays 4% interest a year, and inflation is 2%. Your marginal tax rate is 30% (an example). Compare the real return of the taxed interest with the same account inside a TFSA.

Step 1: after tax, the nominal return is $0.04 \times (1 - 0.30) = 0.028$, that is, 2.8%.

Step 2: the real return after tax is $\frac{1.028}{1.02} - 1$.

Finish: compute it, then compute the real return in the TFSA, where nothing is taxed.

<details class="solution" markdown>
<summary>Finish</summary>

Taxed: $\frac{1.028}{1.02} - 1 = 0.00784$, so 0.784%. TFSA: $\frac{1.04}{1.02} - 1 = 0.01961$, so 1.961%. Tax takes 30% of the nominal return but 60% of the real return: $\frac{1.961 - 0.784}{1.961} = 0.60$.

Over 20 years, \$10,000 grows to \$11,691.19 in today's dollars when taxed and to \$14,745.63 in the TFSA.

Check: the nominal balances are $10000 \times 1.028^{20} = 17372.50$ and $10000 \times 1.04^{20} = 21911.23$, and dividing by $1.02^{20} = 1.4859$ gives the real values.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: subtracting when the rates are large. With 20% nominal and 15% inflation, the real return is 4.35%, not 5%. The approximation is reliable only when both rates are small.

</div>

<div class="warning" markdown>

Watch out: comparing a real return to a nominal one. A GIC at 4.5% and an inflation-adjusted figure of 2.45% describe the same investment in different units. Compare like with like.

</div>

<div class="warning" markdown>

Watch out: dividing by the wrong factor. To bring a later amount back to today's dollars, divide by the price factor, as in Example 3(c). Multiplying by it, or subtracting 15% of it, gives the wrong value.

</div>

<div class="warning" markdown>

Watch out: mixing periods. An inflation rate of 3% a year and a monthly nominal rate must be put on the same basis first, for instance as an effective annual rate from [the APR lesson](03-apr-apy-and-effective-annual-rate.md).

</div>

The real return can be negative, as in Example 1, and an amount can grow in dollars while it shrinks in buying power. With deflation, $\pi < 0$, the real return is above the nominal one. The Fisher relation still holds.

Past inflation is a fact and future inflation is a guess. A calculation with a constant 2% rate for 30 years is a scenario, not a prediction.

## Tricks and shortcuts

To estimate a real return, subtract: 4.5% minus 2% is about 2.5%, and the exact 2.45% is slightly less. For a quick check of any exact answer, the exact real return is always a little lower than $i - \pi$ when it is positive.

To estimate the real value after $t$ years, use the half-life: at 2% inflation, money loses about half its buying power in 35 years, a quarter in 70. At 3%, the rule of 72 gives about 24 years per halving.

Rule of thumb for tax: every dollar of interest taxed at $\tau$ leaves $1 - \tau$, so when the real return is small, a modest tax rate can take most of it, as in Example 4.

## In code

The code applies the Fisher relation, finds real values and compares a taxed account with a TFSA.

<details class="code" markdown>
<summary>In code</summary>

```python
def real_return(nominal, inflation):
    return (1 + nominal) / (1 + inflation) - 1

print(round(100 * real_return(0.045, 0.02), 3))       # 2.451
print(round(100 * real_return(0.015, 0.03), 3))       # -1.456

print(round(10000 * 1.015 ** 5, 2))                   # 10772.84
print(round(10000 * (1.015 / 1.03) ** 5, 2))          # 9292.75
print(round(10000 / 1.02 ** 20, 2))                   # 6729.71

taxed = real_return(0.04 * (1 - 0.30), 0.02)
tfsa = real_return(0.04, 0.02)
print(round(100 * taxed, 3), round(100 * tfsa, 3))    # 0.784 1.961
print(round(10000 * (1 + taxed) ** 20, 2))            # 11691.19
print(round(10000 * (1 + tfsa) ** 20, 2))             # 14745.63
```

</details>

## FAQ

### Why multiply instead of subtract?

Both the dollars and the prices grow by factors, and purchasing power is dollars divided by prices. So the growth factor of purchasing power is $\frac{1 + i}{1 + \pi}$. Subtracting the percentages mixes up what each percent is a percent of: the 2% inflation applies to the grown balance, not to the original one. The difference is the small term $\rho\pi$.

### Is 2% inflation good or bad for savers?

It is neither: it depends on the rate you earn. If a savings account pays less than inflation, the real return is negative and you lose buying power. If it pays more, you gain. The point of the Bank of Canada's target is steadiness, so that people can plan with a known rate.

### Which price index should I use for my own situation?

The CPI measures a typical basket, and your spending may differ, for example if rent is a large share of it. For a rough personal estimate the CPI is the standard choice, and a different rate for a specific cost, such as tuition, is a reasonable alternative if you state it.

## Practice

### Warm-up

1\. Find the real return when a nominal 6% meets inflation of 2%, and compare with $i - \pi$.

<details class="solution" markdown>
<summary>Solution</summary>

$\rho = \frac{1.06}{1.02} - 1 = 0.03922$, so 3.92%. The approximation gives $6\% - 2\% = 4\%$, which is 0.08 points too high.

Check: $1.0392 \times 1.02 = 1.0600$.

</details>

2\. What are \$5,000 worth, in today's dollars, after 10 years of 3% inflation?

<details class="solution" markdown>
<summary>Solution</summary>

$\frac{5000}{1.03^{10}} = \frac{5000}{1.3439} = 3720.47$, so \$3,720.47.

Check: $3720.47 \times 1.03^{10} = 5000.00$.

</details>

3\. A savings account pays 1.5% while inflation is 3%. What is the real return?

<details class="solution" markdown>
<summary>Solution</summary>

$\rho = \frac{1.015}{1.03} - 1 = -0.01456$, so $-1.46\%$. The approximation gives $-1.5\%$.

Check: $0.98544 \times 1.03 = 1.01500$.

</details>

### Standard

4\. Inflation is 2.5% a year. What nominal rate gives a real return of 3%?

<details class="solution" markdown>
<summary>Solution</summary>

From the Fisher relation, $1 + i = 1.03 \times 1.025 = 1.05575$, so $i = 5.575\%$. The approximation $3\% + 2.5\% = 5.5\%$ is 0.075 points low.

Check: $\frac{1.05575}{1.025} - 1 = 0.03$.

</details>

5\. The CPI rises from 125.0 to 140.0 (made-up values). (a) What is the inflation over the period? (b) A salary was \$60,000 in the first year. What salary matches its buying power in the later year? (c) What are \$2,000 of later dollars worth in first-year dollars?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\frac{140}{125} - 1 = 0.12$, so 12%.

(b) $60000 \times \frac{140}{125} = 67200$, so \$67,200.

(c) $2000 \times \frac{125}{140} = 1785.71$, so \$1,785.71.

Check: $1785.71 \times 1.12 = 2000.00$ and $60000 \times 1.12 = 67200$.

</details>

6\. A nominal return of 12% is earned during 9% inflation. (a) Find the exact real return. (b) By how much does $i - \pi$ overstate it, and does that match $\rho\pi$?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\rho = \frac{1.12}{1.09} - 1 = 0.02752$, so 2.752%.

(b) $i - \pi = 3\%$, which is 0.248 points too high. The formula gives $\rho\pi = 0.02752 \times 0.09 = 0.002477$, which is 0.248 points. They match.

Check: $3 - 2.752 = 0.248$.

</details>

### Challenge

7\. A GIC pays 5% interest a year, taxed at 40% (an example marginal rate) in an account outside a registered plan, while inflation is 2.5%. Over 10 years, compare \$10,000 in that account with \$10,000 in a TFSA at the same rate. Report the real value of each.

<details class="solution" markdown>
<summary>Solution</summary>

Taxed: the after-tax nominal return is $5\% \times 0.6 = 3\%$ and the real return is $\frac{1.03}{1.025} - 1 = 0.488\%$. After 10 years the real value is $10000 \times 1.00488^{10} = 10498.65$.

TFSA: the real return is $\frac{1.05}{1.025} - 1 = 2.439\%$, and the real value is $10000 \times 1.02439^{10} = 12724.90$.

The TFSA is worth \$2,226.25 more in today's dollars. The taxed account barely beats inflation: its real gain is \$498.65.

Check: the nominal values are $10000 \times 1.03^{10} = 13439.16$ and $10000 \times 1.05^{10} = 16288.95$, and dividing each by $1.025^{10} = 1.28008$ gives 10498.65 and 12724.90.

</details>

8\. (Reviews [doubling time](05-doubling-time-rule-of-72-and-logs.md).) Prices rise 4% a year. After how many years does a dollar buy half as much? Compare with the rule of 72.

<details class="solution" markdown>
<summary>Solution</summary>

Prices double when $1.04^t = 2$, so $t = \frac{\ln 2}{\ln 1.04} = 17.67$ years. The rule of 72 gives $\frac{72}{4} = 18$ years.

Check: $1.04^{17.67} = 2.00$, and $\frac{1}{1.04^{17.67}} = 0.50$.

</details>

## Where this shows up

- Later lessons use the real return for goals that are far away: [present and future value](../03-time-value-of-money/01-present-and-future-value.md) discounts by a rate, and [retirement accounts](../06-investing-and-retirement/03-retirement-accounts.md) shows why a TFSA's tax-free growth matters most when the real return is small. The economics side is in [CPI and inflation](../../07-economics-math/01-measuring-the-economy/07-cpi-and-inflation.md) and in [nominal vs real GDP and the deflator](../../07-economics-math/01-measuring-the-economy/06-nominal-vs-real-gdp-and-the-deflator.md).
- Computing: the same "divide by the growth factor to get back to the base year" step is how a time series is deflated in data analysis.
- Everyday money: a raise, a GIC rate and a loan's interest all mean more once they are set against the inflation rate for the same period.
