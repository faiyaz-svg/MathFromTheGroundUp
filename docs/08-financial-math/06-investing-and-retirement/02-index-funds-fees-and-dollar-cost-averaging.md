# Index funds, fees and dollar-cost averaging

After this lesson you can say what an index fund and an ETF are, compute how a yearly fee compounds into a large cost over decades, show with algebra why investing a fixed amount each period buys at the harmonic mean of the prices, and say honestly how that compares with investing everything at once.

Before this: [investing returns and risk](01-investing-returns-and-risk.md) and [compound interest](../02-interest-and-growth/02-compound-interest.md). The proof about averages uses the same trick as the AM-GM proof in the first lesson.

All returns, prices and fees in this lesson are made-up examples. This is a lesson about the math of costs and timing, not advice on what to buy.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A fund has a management expense ratio (MER) of 1.2% a year. About how many dollars a year does it cost on a \$20,000 balance?
2. You buy \$400 of a fund when the price per unit is \$20 and another \$400 when it is \$40. What is your average cost per unit, and how does it compare with the average of the two prices?
3. A balance of \$10,000 grows for 10 years at 5% a year in one fund and at 4% in another. What is each balance at the end?

<details class="solution" markdown>
<summary>Answers</summary>

1. $0.012 \times 20000 = 240$, so \$240 a year.
2. You buy $\frac{400}{20} = 20$ units and $\frac{400}{40} = 10$ units, 30 units for \$800, so the average cost is $\frac{800}{30} \approx 26.67$ dollars per unit. The average of the prices is \$30. Your average cost is lower.
3. $10000 \times 1.05^{10} \approx 16{,}288.95$ and $10000 \times 1.04^{10} \approx 14{,}802.44$. One point of return a year is worth about \$1,486 here.

</details>

## The idea

Suppose you want to own a small piece of many companies without choosing them one by one. You could buy a fund: a pool of money from many investors that holds a long list of investments, with each investor owning a share of the pool. Some funds have a team that picks investments. Others simply copy a published list, such as "the 500 largest companies in a country", and hold every item on it in proportion to its size. Copying a list needs far less work, and that difference is the reason the second kind of fund tends to charge less.

The charge is where this lesson's math starts. A fee of 1.5% a year sounds tiny. It isn't: the fee is taken every year, from a balance that is supposed to be compounding, so it eats the growth of the growth. Over 30 years a fee of 1.5% instead of 0.2% removes almost a third of the final balance in the example below.

The second question is about timing. If you have \$12,000 to invest, you can invest it all today or invest \$1,000 a month for a year. Investing a fixed amount on a schedule is called dollar-cost averaging, and it has a neat property that can be proved (you automatically buy more units when the price is low). It also has a limit that the math makes clear, and we will state it carefully.

![Growth of \$10,000 over 30 years at a made-up gross return of 6%. With no fee it ends at \$57,435. With a 0.2% fee (net 5.8%) it ends at \$54,271, and with a 1.5% fee (net 4.5%) it ends at \$37,453. The arrow marks the \$16,818 gap between the two fee levels.](../../assets/figures/08-financial-math/index-funds-fees-and-dollar-cost-averaging-fees.svg)

## Definitions

A **fund** is a pool of investors' money that holds a collection of investments, where each investor owns a share of the whole pool and its gains and losses. A **market index** is a published list of investments with a rule for the weights, such as "every company on this list, weighted by its size". An **index fund** is a fund that holds the investments on an index in the index's proportions, so its return follows the index (apart from fees and small tracking differences).

In plain words, an index fund doesn't try to beat the market; it tries to be the market, cheaply. An **exchange-traded fund** (ETF) is a fund whose units are bought and sold through a brokerage account during the day, like a share of a company. A mutual fund is bought from the fund company at the price calculated at the end of the day. A fund of either kind can follow an index, or not.

The **management expense ratio** (MER) is the fund's yearly cost, written as a percentage of the assets it holds. It covers the management fee and the fund's operating costs, and it is taken out of the fund continuously. You are never sent a bill. Instead, the return you see for the fund is already reduced by it. In plain words, an MER of 0.2% means \$2 a year for every \$1,000 invested.

A fee that is a percentage of the balance reduces the yearly growth rate. We use a simple model: if a fund earns a **gross return** $g$ before fees and has MER $m$, then the **net return** is $g - m$, and the balance after $n$ years is

$$
V_n = V_0\,(1 + g - m)^n.
$$

Dollar-cost averaging is the other new idea. **Dollar-cost averaging** (DCA) means investing the same amount of money at regular intervals, whatever the price. A **lump-sum investment** puts the whole amount in at once. The **harmonic mean** of positive numbers $p_1, \ldots, p_n$ is

$$
H = \frac{n}{\dfrac{1}{p_1} + \dfrac{1}{p_2} + \cdots + \dfrac{1}{p_n}},
$$

the reciprocal of the average of the reciprocals. In plain words, take each number's reciprocal, average those, and flip the result. For 20 and 40 it is $\frac{2}{\frac{1}{20} + \frac{1}{40}} = \frac{2}{0.075} \approx 26.67$, the number from Quick check question 2.

## How to do it

### Measuring the cost of a fee

1. Write the gross return and each MER as decimals: for example $g = 0.06$, $m_1 = 0.015$ and $m_2 = 0.002$.
2. Subtract to get the net returns, $0.045$ and $0.058$, and form the growth factors $1.045$ and $1.058$.
3. Raise each factor to the power of the number of years and multiply by the starting balance. The two balances are $V_0 \cdot 1.045^n$ and $V_0 \cdot 1.058^n$.
4. Find the share of the cheaper fund's ending balance that the expensive fund loses:

$$
1 - \left(\frac{1.045}{1.058}\right)^n.
$$

Since both balances start at the same $V_0$, the starting amount cancels from the share: the loss depends only on the two growth factors and the number of years. Here is that share for different horizons:

| Years | Share lost to the higher fee |
|---|---|
| 10 | 11.6% |
| 20 | 21.9% |
| 30 | 31.0% |
| 40 | 39.0% |

The ratio $\frac{1.045}{1.058} = 0.9877$ is the factor the expensive fund falls behind by every year, a little over 1.2% a year, compounded. If you contribute every year instead of once, the same ideas work with the formula for the value of regular contributions from [annuities and geometric series](../03-time-value-of-money/02-annuities-and-geometric-series.md): $V = P\cdot\frac{(1 + r)^n - 1}{r}$, with $r$ equal to the net return.

### Why a fixed dollar amount buys at the harmonic mean

*Theorem 2 (the average cost of dollar-cost averaging).* You invest the same amount $D$ at each of $n$ times, when the price per unit is $p_1, \ldots, p_n$ (all positive). Then your average cost per unit is the harmonic mean $H$ of the prices. Also $H \le A$, where $A = \frac{p_1 + \cdots + p_n}{n}$ is the plain average of the prices, with equality only if all the prices are equal.

We know that units bought equal money spent divided by price. We want a formula for the average cost, which is total money spent divided by total units bought, and a comparison of it with the average price. The plan is to compute the average cost directly, then compare $A$ and $H$ through the product of the sum of the prices and the sum of their reciprocals, which reduces to the fact that $x + \frac{1}{x} \ge 2$.

*Proof.* At time $i$ you buy $\frac{D}{p_i}$ units. The total spent is $nD$ and the total number of units is $D\left(\frac{1}{p_1} + \cdots + \frac{1}{p_n}\right)$. So the average cost per unit is

$$
\frac{nD}{D\left(\frac{1}{p_1} + \cdots + \frac{1}{p_n}\right)} = \frac{n}{\frac{1}{p_1} + \cdots + \frac{1}{p_n}} = H.
$$

For the comparison, first note that for every $x > 0$,

$$
x + \frac{1}{x} - 2 = \frac{x^2 - 2x + 1}{x} = \frac{(x - 1)^2}{x} \ge 0,
$$

so $x + \frac{1}{x} \ge 2$, with equality only for $x = 1$. Now multiply out the product of the two sums:

$$
(p_1 + \cdots + p_n)\left(\frac{1}{p_1} + \cdots + \frac{1}{p_n}\right) = \sum_{i}\sum_{j}\frac{p_i}{p_j} = n + \sum_{i < j}\left(\frac{p_i}{p_j} + \frac{p_j}{p_i}\right).
$$

The first $n$ comes from the terms with $i = j$, which are each 1. Each pair with $i < j$ contributes $x + \frac{1}{x}$ with $x = \frac{p_i}{p_j}$, which is at least 2, and there are $\frac{n(n-1)}{2}$ pairs. So the product is at least $n + 2 \cdot \frac{n(n-1)}{2} = n^2$. Dividing both sides by $n\left(\frac{1}{p_1} + \cdots + \frac{1}{p_n}\right)$ gives $\frac{p_1 + \cdots + p_n}{n} \ge \frac{n}{\frac{1}{p_1} + \cdots + \frac{1}{p_n}}$, that is, $A \ge H$. Equality needs every pair to have $x = 1$, which means all prices are equal. $\blacksquare$

Look back: the cheaper prices get more weight because you buy more units at a low price, and that pulls the average cost below the plain average of the prices. For two prices $a$ and $b$ the harmonic mean is $\frac{2ab}{a + b}$, and $\frac{2ab}{a + b} \le \frac{a + b}{2}$ is the same as $4ab \le (a + b)^2$, which is $(a - b)^2 \ge 0$.

Be careful about what this proves. It says your average cost per unit is below the average price. It does not say you earned a profit, and it does not say you did better than other ways of investing. The profit depends on the final price compared with your average cost.

### Rebalancing

If you want a fixed split between kinds of investments (a target allocation, such as 60% stocks and 40% bonds), their different returns will push the split away from the target. **Rebalancing** is selling some of what grew and buying some of what lagged to restore the target. Suppose \$10,000 is split \$6,000 and \$4,000. After a year the stock part is up 30% and the bond part is up 2%: \$7,800 and \$4,080, a total of \$11,880. The stock share is now 65.7%. To return to 60% you hold $0.6 \times 11880 = 7128$ in stocks, so you sell \$672 of stocks and buy \$672 of bonds.

Rebalancing controls how much risk you carry; it is not a way to raise returns. In a taxable account, selling can trigger tax on the gain, so people often rebalance with new contributions instead (put new money into the part that is below target), and inside a TFSA or RRSP, switching has no tax cost.

## Worked examples

<div class="example" markdown>

### Example 1: a fee over 30 years

A fund earns 6% a year before fees (made up). You invest \$10,000 for 30 years and can choose a fund with an MER of 0.2% or one with an MER of 1.5%. How much do you end up with in each, and what share does the higher fee cost?

Step 1: the gross return is $g = 0.06$, and the MERs are 0.002 and 0.015.

Step 2: the net returns are 5.8% and 4.5%, so the growth factors are 1.058 and 1.045.

Step 3: the balances are

$$
10000 \times 1.058^{30} = 54{,}271.28 \qquad\text{and}\qquad 10000 \times 1.045^{30} = 37{,}453.18.
$$

The difference is $54271.28 - 37453.18 = 16{,}818.09$ dollars, so the higher fee costs \$16,818.09.

Step 4: the share lost is $1 - \frac{37453.18}{54271.28} = 0.3099$, or 31.0%. Equivalently $1 - 0.9877^{30} = 0.3099$.

A 1.3-point gap in the fee, which is 1.3% of the balance each year, took 31% of the final balance. The 1.5% fee also takes a quarter of the gross return of 6% each year ($\frac{1.5}{6} = 0.25$), which explains why the damage is large.

Check: the difference between the two MERs is $1.5\% - 0.2\% = 1.3$ points, and $1.058^{30} \approx 5.427$ against $1.045^{30} \approx 3.745$, whose ratio is 0.690, so the higher-fee fund ends with 69.0% of the other, matching the 31.0% lost. With no fee at all, \$10,000 would reach $10000 \times 1.06^{30} = 57{,}434.91$.

</div>

<div class="example" markdown>

### Example 2: contributing every year

You invest \$3,600 at the end of every year for 30 years (about \$300 a month, simplified to once a year). The gross return is 6%, and the MER is again 0.2% or 1.5%. What is the balance in each case?

The value of regular contributions is $V = P\cdot\frac{(1 + r)^n - 1}{r}$ with $P = 3600$, $n = 30$ and $r$ the net return.

At 5.8%: $V = 3600 \cdot \frac{1.058^{30} - 1}{0.058} = 3600 \cdot \frac{4.4271}{0.058} \approx 274{,}787.23$ dollars.

At 4.5%: $V = 3600 \cdot \frac{1.045^{30} - 1}{0.045} = 3600 \cdot \frac{2.7453}{0.045} \approx 219{,}625.45$ dollars.

You paid in $3600 \times 30 = 108{,}000$ in both cases. The higher fee costs $274787.23 - 219625.45 = 55{,}161.78$ dollars, which is 20.1% of the final balance. The share lost is smaller than the 31% of Example 1 because the late contributions have little time to compound, so the fee gets less time to work on them.

Check: with no fee at all the balance would be $3600 \cdot \frac{1.06^{30} - 1}{0.06} \approx 284{,}609.47$ dollars, so both balances are below it and the 1.5% fund is further below. Each balance is also above the \$108,000 paid in, as it should be with positive returns.

</div>

<div class="example" markdown>

### Example 3: the average cost of a monthly purchase

You invest \$500 at the start of each of 5 months in a fund whose price per unit is \$50, \$40, \$25, \$40 and \$50 (made up). Find the units you own, your average cost, the plain average of the prices, and the value of your units at the end if the final price is \$50.

The units bought each month are $\frac{500}{50} = 10$, $\frac{500}{40} = 12.5$, $\frac{500}{25} = 20$, $12.5$ and $10$. Total: 65 units for \$2,500.

The average cost is $\frac{2500}{65} = 38.46$ dollars per unit, which equals the harmonic mean $\frac{5}{\frac{1}{50} + \frac{1}{40} + \frac{1}{25} + \frac{1}{40} + \frac{1}{50}} = \frac{5}{0.13} = 38.46$. The plain average of the five prices is $\frac{50 + 40 + 25 + 40 + 50}{5} = 41$ dollars.

At a final price of \$50 your 65 units are worth \$3,250, a gain of \$750 on \$2,500, or 30%. Notice what carried the result: in the cheap month you bought twice as many units as in the dear months, 20 against 10.

Check: $38.46 \le 41$, as Theorem 2 requires, and $65 \times 38.46 = 2{,}500$. If you had bought a fixed number of units each month instead of a fixed number of dollars, you would have paid the plain average of \$41 per unit.

<div class="warning" markdown>

Watch out: had the final price been \$30, your 65 units would be worth \$1,950, a loss of \$550, even though your average cost of \$38.46 is below the average price of \$41. Buying below the average price is not a guarantee of a profit.

</div>

</div>

<div class="example" markdown>

### Example 4: a smaller purchase (finish it yourself)

You invest \$200 a month for 4 months at unit prices \$10, \$8, \$5 and \$8. Find the units you own and your average cost, and compare with the plain average of the prices.

Step 1: the units bought are $\frac{200}{10} = 20$, $\frac{200}{8} = 25$, $\frac{200}{5} = 40$ and $25$. Step 2: the total is 110 units for \$800. Now find the average cost, compare it with the average price, and check it against the harmonic-mean formula.

<details class="solution" markdown>
<summary>Finish</summary>

The average cost is $\frac{800}{110} \approx 7.27$ dollars per unit. The plain average of the prices is $\frac{10 + 8 + 5 + 8}{4} = 7.75$ dollars, so the average cost is lower.

Check: the harmonic mean is $\frac{4}{\frac{1}{10} + \frac{1}{8} + \frac{1}{5} + \frac{1}{8}} = \frac{4}{0.55} \approx 7.27$, matching.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: don't treat a small fee as a small cost. A yearly percentage looks like a small number, but it is charged on the whole balance every year, including the growth. In Example 1, the 1.5% fee costs 31% of the final balance, not 1.5%. Always convert a fee to dollars at the end of the horizon you care about.

</div>

<div class="warning" markdown>

Watch out: the net return is gross minus MER only approximately. If a fund's costs are taken as a fraction of assets, the growth factor is $(1 + g)(1 - m)$. With $g = 6\%$ and $m = 1.5\%$ this is $1.06 \times 0.985 = 1.0441$, a net return of 4.41% rather than 4.5%, and 30 years at 4.41% gives \$36,497 instead of \$37,453. The simple subtraction in this lesson is a convenient model. Use whichever the situation gives you: when a fund quotes a return, the figure is already after the MER, and no subtraction is needed.

</div>

<div class="warning" markdown>

Watch out: dollar-cost averaging doesn't guarantee a profit, and it does not remove the risk of losing money. It lowers your average cost relative to the average price, and it spreads the timing of your purchases. In a market that falls and keeps falling, you lose on every purchase.

</div>

<div class="warning" markdown>

Watch out: "my average cost is below the average price" does not mean "DCA beat investing all at once". These compare two different things. The comparison with a lump sum is in [In code](#in-code) below: on average the lump sum wins when the expected return is positive.

</div>

A lower MER doesn't make a fund better on its own. Two funds that follow the same index with similar holdings earn almost the same gross return, so the cheaper one leaves you better off. Two funds that hold different things can have different gross returns, and then the fee is only one of the differences. The MER also isn't the whole cost: buying and selling units through a brokerage can have its own costs, and a fund's trading inside the fund adds costs that sit outside the MER.

If all the prices are equal, DCA and any other schedule give the same average cost, and $H = A$ exactly.

## Tricks and shortcuts

To judge a fee quickly, divide it by the gross return you expect: 1.5 out of 6 is a quarter of the return, and 0.2 out of 6 is about a thirtieth. A fee that takes a big fraction of the expected return is hard to recover from.

For the harmonic mean of two prices use $\frac{2ab}{a + b}$: for \$20 and \$40 that is $\frac{2 \times 800}{60} = 26.67$. The harmonic mean is always at most the geometric mean $\sqrt{ab}$ (here 28.28), which is at most the arithmetic mean (here 30).

To rebalance without selling, aim new contributions at the part of the portfolio that is below target.

## In code

The code computes the fee examples and the average cost, then compares a lump sum with dollar-cost averaging in a made-up model. You have \$12,000. The lump sum is invested at once and held for 12 months. The DCA plan invests \$1,000 at the start of each of 12 months, and the money that hasn't been invested yet sits in cash earning 0%. Monthly market returns are independent, drawn from a normal distribution with mean 0.5% and standard deviation 4.5%. It needs NumPy.

<details class="code" markdown>
<summary>In code</summary>

```python
import statistics
import numpy as np

# Fee drag on a single $10,000 over 30 years, gross return 6%.
for mer in (0.002, 0.015):
    print(mer, round(10_000 * (1 + 0.06 - mer) ** 30, 2))
# 0.002 54271.28
# 0.015 37453.18

# Average cost of $500 a month is the harmonic mean of the prices.
prices = [50, 40, 25, 40, 50]
units = sum(500 / p for p in prices)
print(units, round(2500 / units, 2), round(statistics.harmonic_mean(prices), 2), statistics.mean(prices))
# 65.0 38.46 38.46 41

# Lump sum against dollar-cost averaging, 20,000 made-up 12-month paths.
rng = np.random.default_rng(2026)
r = rng.normal(0.005, 0.045, size=(20_000, 12))
lump = 12_000 * np.prod(1 + r, axis=1)
dca = sum(1_000 * np.prod(1 + r[:, i:], axis=1) for i in range(12))

print(round(lump.mean()), round(dca.mean()))                    # 12749 12406
print((lump > dca).mean())                                      # 0.59835
print(round(lump.std()), round(dca.std()))                      # 1984 1186
print(np.percentile(lump, 5).round(), np.percentile(dca, 5).round())  # 9756.0 10577.0

# Exact expected values with a 0.5% monthly return:
print(round(12_000 * 1.005**12), round(sum(1_000 * 1.005 ** (12 - i) for i in range(12))))
# 12740 12397
```

</details>

The lump sum has the higher average result, \$12,749 against \$12,406, and it ends ahead in 59.8% of the paths. The reason is simple: each dollar that waits in cash in the DCA plan misses the expected 0.5% a month. On average a dollar waits 5.5 months, and the exact expected values, \$12,740 and \$12,397, differ by about \$343. The DCA plan has a lower spread (standard deviation \$1,186 against \$1,984) and a better 5th-percentile outcome (\$10,577 against \$9,756), because less money is exposed to the market at the start. That is its real benefit: it trades some expected return for less regret.

The result depends on the model. In the same model with a monthly mean of $-0.5\%$ (a market that tends to fall), DCA is ahead in 65.5% of paths. You can't know in advance which case you are in, and the model says that, when expected returns are positive, delaying costs money on average. If you simply invest part of each paycheque as it arrives, you are not choosing between the two plans, because the money does not exist yet.

## FAQ

### Why does the harmonic mean show up and not the usual average?

Because with a fixed amount of money, the quantity that adds up is the number of units, and units are money divided by price. The average cost is total money divided by total units, so the prices enter as reciprocals. If you instead bought a fixed number of units each time, the money would add up, and the average cost would be the plain average of the prices.

### Is dollar-cost averaging better than investing a lump sum?

On average, in a model where expected returns are positive, no: the lump sum is ahead more often and by more on average. DCA lowers the spread of outcomes and the chance of buying everything just before a drop, at the price of a lower average. Which you prefer depends on how much you dislike regret, and the math doesn't settle that for you.

### What is the difference between an ETF and an index fund?

The two words describe different things. "Index fund" says what the fund holds (the contents of an index). "ETF" says how you buy it (through a brokerage during the day). Many ETFs are index funds, and many index funds are mutual funds, not ETFs.

### If the MER is already out of the return, why does it matter?

Because the return you see is smaller by the fee, and the missing amount compounds. Compare two funds that hold the same investments: their gross returns are the same, so the whole difference between the net returns is the difference in the MERs, every year.

## Practice

### Warm-up

1\. A fund has an MER of 0.85% and you hold \$34,000 in it. What does it cost per year, in dollars?

<details class="solution" markdown>
<summary>Solution</summary>

$0.0085 \times 34000 = 289$, so \$289 a year.

Check: 1% of \$34,000 is \$340, and 0.85% is a bit less, so \$289 is reasonable.

</details>

2\. Prices per unit are \$10 and \$40, and you invest \$100 at each. Find your average cost and compare it with the plain average of the prices.

<details class="solution" markdown>
<summary>Solution</summary>

You buy $\frac{100}{10} = 10$ units and $\frac{100}{40} = 2.5$ units, 12.5 units for \$200, so the average cost is $\frac{200}{12.5} = 16$ dollars. The plain average of the prices is \$25.

Check: the harmonic mean formula gives $\frac{2 \times 10 \times 40}{10 + 40} = \frac{800}{50} = 16$.

</details>

3\. A fund earns a gross return of 7% and has an MER of 0.25%. What is \$5,000 worth after 20 years? What would it be worth with no fee?

<details class="solution" markdown>
<summary>Solution</summary>

The net return is $7\% - 0.25\% = 6.75\%$, so the balance is $5000 \times 1.0675^{20} \approx 18{,}464.08$, or \$18,464.08. With no fee it is $5000 \times 1.07^{20} \approx 19{,}348.42$, or \$19,348.42. The fee costs about \$884 over 20 years.

Check: $19348.42 - 18464.08 = 884.34$. The share lost is $1 - \left(\frac{1.0675}{1.07}\right)^{20} \approx 4.6\%$, and $884.34 \div 19348.42 \approx 4.6\%$.

</details>

### Standard

4\. A fund has a gross return of 7%. Compare MERs of 0.1% and 1.0% over 25 years: what share of the cheaper fund's ending balance does the higher fee cost? What are the balances for \$10,000?

<details class="solution" markdown>
<summary>Solution</summary>

The net returns are 6.9% and 6.0%. The balances are $10000 \times 1.069^{25}$ and $10000 \times 1.06^{25}$. The share lost is $1 - \left(\frac{1.06}{1.069}\right)^{25}$.

Numerically, $1.069^{25} \approx 5.3020$, so \$53,020 (to the nearest dollar), and $1.06^{25} \approx 4.2919$, so \$42,919. The share lost is $1 - \frac{42919}{53020} \approx 0.191$, about 19.1%.

Check: the ratio of the growth factors is $\frac{1.06}{1.069} = 0.99158$, and $0.99158^{25} \approx 0.809$, which is $1 - 0.191$.

</details>

5\. You invest \$300 a month for 6 months at unit prices \$20, \$25, \$16, \$20, \$25 and \$20. Find your units, your average cost, the plain average of the prices, and the value of your units if the price ends at \$20.

<details class="solution" markdown>
<summary>Solution</summary>

The units are $\frac{300}{20} = 15$, $12$, $18.75$, $15$, $12$ and $15$, for 87.75 units in total. You spent \$1,800, so the average cost is $\frac{1800}{87.75} \approx 20.51$. The plain average of the prices is $\frac{20 + 25 + 16 + 20 + 25 + 20}{6} = 21$.

At a price of \$20 the units are worth $87.75 \times 20 = 1{,}755$, a loss of \$45, even though the average cost is below the average price. The average cost, \$20.51, is above the final price of \$20.

Check: the harmonic mean is $\frac{6}{\frac{3}{20} + \frac{2}{25} + \frac{1}{16}} = \frac{6}{0.29250} \approx 20.51$, matching.

</details>

6\. A \$50,000 portfolio has a 60/40 target split between stocks and bonds. After a year the stocks are down 20% and the bonds are up 5%. What is the split now, and what trade restores 60/40?

<details class="solution" markdown>
<summary>Solution</summary>

Start with \$30,000 in stocks and \$20,000 in bonds. After the year the stocks are $0.8 \times 30000 = 24000$ and the bonds are $1.05 \times 20000 = 21000$, a total of \$45,000. The stock share is $\frac{24000}{45000} = 53.3\%$.

For 60/40, stocks should be $0.6 \times 45000 = 27000$. So you buy \$3,000 of stocks and sell \$3,000 of bonds, leaving \$27,000 and \$18,000.

Check: $27000 + 18000 = 45000$, and $\frac{27000}{45000} = 0.6$. Rebalancing here means buying the part that fell.

</details>

### Challenge

7\. Prove that for two positive prices $a$ and $b$, the harmonic mean is at most the geometric mean, which is at most the arithmetic mean: $\frac{2ab}{a + b} \le \sqrt{ab} \le \frac{a + b}{2}$.

<details class="solution" markdown>
<summary>Solution</summary>

The right inequality is Theorem 1 of the previous lesson. For the left one, we want $\frac{2ab}{a + b} \le \sqrt{ab}$. Since $a + b > 0$, this is equivalent to $2ab \le \sqrt{ab}\,(a + b)$. Divide both sides by $\sqrt{ab} > 0$: $2\sqrt{ab} \le a + b$, which is the right inequality again (the AM-GM inequality, proved as $(\sqrt{a} - \sqrt{b})^2 \ge 0$). Every step is reversible, so the left inequality holds. $\blacksquare$

Check with $a = 20$ and $b = 40$: $26.67 \le 28.28 \le 30$.

</details>

8\. (Reviews [logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md) and exponents.) With a gross return of 6%, how large a yearly MER cuts the 30-year ending balance in half, compared with having no fee? Use the model where the net return is $g - m$.

<details class="solution" markdown>
<summary>Solution</summary>

We want $\left(\frac{1.06 - m}{1.06}\right)^{30} = 0.5$. Take the 30th root: $\frac{1.06 - m}{1.06} = 0.5^{1/30} = 0.97716$. (With logarithms, $\ln 0.5 \div 30 = -0.023105$, and $e^{-0.023105} = 0.97716$.) So $m = 1.06(1 - 0.97716) = 1.06 \times 0.02284 \approx 0.0242$.

An MER of about 2.42% a year halves the final balance over 30 years.

Check: with $m = 0.02421$ the net return is 3.579%, and $\frac{1.03579^{30}}{1.06^{30}} = \frac{2.8718}{5.7435} \approx 0.5$. Directly, $10000 \times 1.03579^{30} \approx 28{,}718$ is half of \$57,435.

</details>

## Where this shows up

- The next lesson puts investments inside the tax-sheltered accounts, [retirement accounts: RRSP, TFSA and FHSA](03-retirement-accounts.md), where a fee drag works exactly the same way. Fees on a loan work in reverse (see [compound interest](../02-interest-and-growth/02-compound-interest.md)).
- The harmonic mean appears in computer science whenever rates are averaged: the average speed over equal distances, and the F1 score of a classifier. The inequality $H \le G \le A$ is a standard tool for algorithm analysis.
- Comparing paths with different timing is a pattern in economics too. It comes back as present value in [present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md).
