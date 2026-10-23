# Index numbers

After this lesson you can build an index from a series, rebase it, splice two indexes with a chain link, compute Laspeyres, Paasche and Fisher price indexes for a small basket, explain why they differ, and use an index to turn nominal amounts into real ones.

Before this: [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md), [growth rates and CAGR](03-growth-rates-and-cagr.md) and [ratios and unit rates](../../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A value is 150 and the base value is 120. What is the index, with the base at 100?
2. Canada's CPI (2002 = 100) was 136.2 in September 2019 and 170.0 in September 2026. Rebase so that September 2019 is 100, and say what the new value for September 2026 means.
3. A wage was \$30.00 an hour in September 2019. What wage in September 2026 dollars keeps the same buying power?

<details class="solution" markdown>
<summary>Answers</summary>

1. $100 \times \frac{150}{120} = 125$.
2. $100 \times \frac{170.0}{136.2} = 124.8$. Prices were 24.8% higher in September 2026 than in September 2019.
3. Multiply by the ratio of the price levels: $30 \times \frac{170.0}{136.2} = 37.44$, about \$37.44.

</details>

## The idea

A price is a number with a unit: \$4.50 for a litre of milk, \$1.60 for a litre of gas. The price level of a whole economy is harder, because it has thousands of goods in different units, and a "typical" price has no unit at all. Economists build a price index: they pick a base period, set its price level to 100, and report every other period as a percentage of the base. An index of 124.8 means "24.8% above the base".

Dropping the units is the point. An index lets you compare the growth of different things on one scale (wages, rents, exports), splice series that were published on different bases, and strip inflation out of money amounts. The cost is that an index number says nothing about the level of anything: only comparisons between index values, in the same index, mean something.

The harder question is how to combine many prices into one. Suppose beef rises 50% and bread rises 25%. A household that eats both feels some average of the two, and the average depends on how much of each it buys. Which quantities do you use, those of the base year or those of the current year? That choice gives two different price indexes, named after Laspeyres and Paasche, and the gap between them is a real feature of the economy: people substitute away from what gets expensive.

## Definitions

An **index number** measures the value of a variable in each period relative to its value in a base period. Let $x_t$ be the value in period $t$ and $x_0$ the value in the **base period**. The index with base 0 is

$$
I_t = 100 \times \frac{x_t}{x_0}.
$$

In plain words, the base period is 100, and a value of $I_t$ means the variable is $I_t\%$ of its base level. So 124.8 means 24.8% more than the base, and 80 means 20% less.

To **rebase** an index means to change the base period from 0 to another period $b$. Divide every value by the value in the new base period and multiply by 100:

$$
I_t^{\text{new}} = 100 \times \frac{I_t^{\text{old}}}{I_b^{\text{old}}}.
$$

In plain words, rescale so the new base period reads 100. The ratios between values don't change, so percent changes between any two periods are the same before and after.

A **price relative** is the price of one good in the current period divided by its price in the base period, $\frac{p_1}{p_0}$ (times 100 if you write it as an index). A **basket** is a fixed list of goods with quantities. For goods $i = 1, \dots, m$, let $p_{0i}$ and $p_{1i}$ be the prices in the base period and the current period, and $q_{0i}$ and $q_{1i}$ the quantities bought in each. The sum $\sum_i p_{1i} q_{0i}$ means "add up the amounts $p_{1i} q_{0i}$ over all goods", as in [summation notation](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md).

The **Laspeyres price index** prices the base-period basket in both periods:

$$
L = 100 \times \frac{\sum_i p_{1i} q_{0i}}{\sum_i p_{0i} q_{0i}}.
$$

The **Paasche price index** prices the current-period basket in both periods:

$$
P = 100 \times \frac{\sum_i p_{1i} q_{1i}}{\sum_i p_{0i} q_{1i}}.
$$

The **Fisher price index** is the geometric mean of the two, $F = \sqrt{L \times P}$. In plain words, Laspeyres asks "what does last period's basket cost now, compared with then?", Paasche asks "what does this period's basket cost now, compared with what it would have cost then?", and Fisher splits the difference with a geometric mean.

A **chain index** (or chain-linked index) multiplies period-to-period links. With links $\ell_t = \frac{x_t}{x_{t-1}}$ (the growth factors from [growth rates and CAGR](03-growth-rates-and-cagr.md)), the chained index is $I_t = 100 \times \ell_1 \ell_2 \cdots \ell_t$. In plain words, each year's index is last year's index times that year's growth factor, and the weights (the basket) can be updated every year.

**Nominal** values are measured in the money of the period they belong to. **Real** values are measured in the money of a fixed base period, so they remove the effect of price changes. With a price index $I_t$ (base 100), the real value is

$$
\text{real}_t = \frac{\text{nominal}_t}{I_t / 100}.
$$

## How to do it

### Building and reading an index

1. Choose the base period and its value $x_0$ (it must be positive).
2. For each period, divide $x_t$ by $x_0$ and multiply by 100.
3. Read the result as a percent of the base: 112.1 is 12.1% above the base.
4. To get the percent change between two other periods, divide the two index values: $\frac{I_t}{I_s} - 1$. Subtracting the index values gives index points, which equal percent changes only when the earlier value is 100.
5. Check that the base period reads exactly 100.

### Rebasing

1. Pick the new base period $b$ and read its old index value $I_b^{\text{old}}$.
2. Divide each old index value by $I_b^{\text{old}}$ and multiply by 100.
3. Check that period $b$ now reads 100, and that a percent change between two periods is unchanged.

Rebasing is only division by a constant, so the shape of a series doesn't change. Agencies rebase to keep numbers near 100 and to reflect a more recent reference year. Statistics Canada's CPI uses 2002 as its base, so the index in September 2026 is 170.0 (Bank of Canada, [CPI data](https://www.bankofcanada.ca/rates/price-indexes/cpi/); Statistics Canada, Table 18-10-0004-01).

### Chain linking

Suppose an old index with base 0 stops at period $s$, and a new index with its own base $s$ (so it reads 100 at $s$) continues the series. To produce one continuous series on the old base:

1. Take the old index value at the overlap period, $I_s^{\text{old}}$.
2. For each later period $t$, compute $I_t^{\text{old base}} = I_s^{\text{old}} \times \frac{I_t^{\text{new}}}{100}$.
3. Check the overlap: the spliced series equals the old series at $s$ and has the same growth as the new series after $s$.

The link factor is $\frac{I_s^{\text{old}}}{100}$. A chain index applies this idea every year, so that the weights can change each year, and the index is the product of the yearly growth factors.

### Laspeyres, Paasche and Fisher

1. List each good's base and current prices and quantities.
2. For Laspeyres, compute $\sum p_{1i} q_{0i}$ (cost of the old basket at new prices) and $\sum p_{0i} q_{0i}$ (its cost at old prices). Divide and multiply by 100.
3. For Paasche, compute $\sum p_{1i} q_{1i}$ (cost of the new basket at new prices) and $\sum p_{0i} q_{1i}$ (its cost at old prices). Divide and multiply by 100.
4. Fisher is the square root of the product of the two.
5. Check that each index lies between the smallest and largest price relative: it is a weighted average of the price relatives.

Why each is a weighted average of price relatives: Laspeyres equals $\sum_i w_i \frac{p_{1i}}{p_{0i}}$ with weights $w_i = \frac{p_{0i} q_{0i}}{\sum_j p_{0j} q_{0j}}$ (base-period spending shares). In words, a good counts more when the household spent more on it in the base period.

Why the two differ: each uses a different basket. People buy less of a good whose price rises faster and more of one whose price rises slower (substitution). The base-period basket still contains the good that got expensive, so Laspeyres puts too much weight on it, and tends to overstate the rise in the cost of living. The current basket has already shifted away from expensive goods, so Paasche gives them too little weight, and tends to understate it. The Fisher index lies between the two. The CPI is a fixed-basket index of the Laspeyres type (with basket weights updated from time to time), so it is subject to this substitution bias, a point the lesson on [CPI and inflation](07-cpi-and-inflation.md) returns to.

### Real versus nominal with an index

1. Choose the price index and its base period. The real amounts will be in base-period dollars (or in the dollars of any period you rebase to).
2. Divide each nominal amount by the price index divided by 100.
3. Compute real growth between two periods as $\frac{\text{real}_t}{\text{real}_s} - 1$, which equals $\frac{1 + \text{nominal growth}}{1 + \text{inflation}} - 1$.
4. For quick work, real growth $\approx$ nominal growth minus inflation, which is the ratio rule from [growth rates and CAGR](03-growth-rates-and-cagr.md).

## Worked examples

<div class="example" markdown>

### Example 1: building and rebasing a CPI series

These are the CPI values (2002 = 100) for September of each year (Bank of Canada, [CPI data](https://www.bankofcanada.ca/rates/price-indexes/cpi/), Statistics Canada Table 18-10-0004-01): 136.2 (2019), 136.9 (2020), 142.9 (2021), 152.7 (2022), 158.5 (2023), 161.1 (2024), 164.9 (2025) and 170.0 (2026). Rebase the series so that September 2019 is 100.

Step 1: the new base is 2019, with old value 136.2.

Step 2: divide each value by 136.2 and multiply by 100:

| Year | CPI (2002 = 100) | CPI (Sept 2019 = 100) |
|---|---|---|
| 2019 | 136.2 | 100.0 |
| 2020 | 136.9 | 100.5 |
| 2021 | 142.9 | 104.9 |
| 2022 | 152.7 | 112.1 |
| 2023 | 158.5 | 116.4 |
| 2024 | 161.1 | 118.3 |
| 2025 | 164.9 | 121.1 |
| 2026 | 170.0 | 124.8 |

Step 3: the 2026 value, 124.8, says prices were 24.8% higher than in September 2019.

Check: the base year reads exactly 100. The percent change from 2022 to 2026 is $\frac{170.0}{152.7} - 1 = 11.33\%$ on the old base, and $\frac{124.8}{112.1} - 1 = 11.33\%$ on the new one. Rebasing doesn't change ratios. The difference in index points on the new base, $124.8 - 112.1 = 12.7$, is not 11.3%, because the earlier value is not 100.

</div>

<div class="example" markdown>

### Example 2: Laspeyres, Paasche and Fisher for a three-good basket

These are made-up prices and quantities for a student's monthly purchases, in two years. Bread costs \$2.00 and \$2.50, with 100 and 90 loaves bought. Beef costs \$10.00 and \$15.00 per kilogram, with 20 and 10 kg bought. Chicken costs \$6.00 and \$6.50 per kilogram, with 30 and 45 kg bought.

Step 1: the base year is year 0, the current year is year 1.

Step 2 (Laspeyres): the base basket costs, at base prices, $2.00 \times 100 + 10.00 \times 20 + 6.00 \times 30 = 200 + 200 + 180 = 580$. At current prices it costs $2.50 \times 100 + 15.00 \times 20 + 6.50 \times 30 = 250 + 300 + 195 = 745$. So $L = 100 \times \frac{745}{580} = 128.4$.

Step 3 (Paasche): the current basket costs, at current prices, $2.50 \times 90 + 15.00 \times 10 + 6.50 \times 45 = 225 + 150 + 292.50 = 667.50$. At base prices it would cost $2.00 \times 90 + 10.00 \times 10 + 6.00 \times 45 = 180 + 100 + 270 = 550$. So $P = 100 \times \frac{667.5}{550} = 121.4$.

Step 4 (Fisher): $F = \sqrt{128.4 \times 121.4} = 124.9$.

Step 5: the price relatives are 125 (bread), 150 (beef) and 108.3 (chicken), and all three indexes lie between 108.3 and 150.

The Laspeyres index (128.4) is higher than the Paasche (121.4). The student switched from beef, whose price rose 50%, to chicken, whose price rose 8.3%: beef purchases halved, and chicken purchases rose by half. The Laspeyres basket still has 20 kg of beef, so it is dominated by the big price rise, while the Paasche basket has only 10. Actual spending went from \$580 to \$667.50, a rise of 15.1%, less than either price index, because the student also bought less.

</div>

<div class="example" markdown>

### Example 3: splicing two indexes

These are made-up figures. An old index with base 2002 = 100 reads 125 in 2015, the year it is discontinued. A new index with base 2015 = 100 reads 108 in 2020. Put the 2020 value on the old base.

Step 1: the overlap year is 2015, with old value 125.

Step 2: the link factor is $\frac{125}{100} = 1.25$, and the 2020 value on the old base is $125 \times \frac{108}{100} = 135$.

Check: the new index says prices rose 8% from 2015 to 2020, and $135 \div 125 = 1.08$ is the same 8%. The splice keeps the old index at 125 in 2015 and applies the new index's growth after that.

</div>

<div class="example" markdown>

### Example 4: a real wage (finish it yourself)

These are made-up wages. Your hourly wage was \$30.00 in September 2019 and is \$38.00 in September 2026. Using the CPI from Example 1, find the 2026 wage in September 2019 dollars, and the percent change in real terms.

Step 1: the price index in 2026 is 124.8 on the 2019 base, or $\frac{170.0}{136.2}$ as a ratio. Nominal wage growth is $\frac{38}{30} - 1 = 26.7\%$ and inflation is 24.8%.

Now compute the real 2026 wage by dividing by the price index ratio, and the real percent change. Compare with the approximation "nominal minus inflation".

<details class="solution" markdown>
<summary>Finish</summary>

The real wage is $38.00 \times \frac{136.2}{170.0} = 30.44$, so \$30.44 in 2019 dollars. The real change is $\frac{30.44}{30.00} - 1 = 1.48\%$.

The approximation is $26.7\% - 24.8\% = 1.9\%$, a bit high. The exact version is $\frac{1.2667}{1.2482} - 1 = 1.48\%$, the ratio rule.

Check: $30.00 \times 1.2482 = 37.44$ is the 2026 wage that would only keep pace with prices, and \$38.00 is \$0.56 above it, which is $\frac{0.56}{37.44} = 1.5\%$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: index points are not percent. A CPI that goes from 136.2 to 170.0 rose 33.8 points, which is 24.8%, not 33.8%. A change in points equals a percent change only when the starting index is 100. Divide the two values.

</div>

<div class="warning" markdown>

Watch out: only compare index values in the same index and on the same base. A CPI of 170.0 (2002 = 100) and a regional index reading 110 (2019 = 100) cannot be set side by side. If two cities have indexes of 110 and 105, the first city did not become the more expensive one: the index measures change from each city's own base, not the level of prices.

</div>

<div class="warning" markdown>

Watch out: the base value is 100 only in the base period. After rebasing, the old base period no longer reads 100. On the September 2019 base of Example 1, the old base year 2002 would read $100 \times \frac{100}{136.2} = 73.4$.

</div>

<div class="warning" markdown>

Watch out: Laspeyres and Paasche answer different questions, and neither is the "true" cost of living. Laspeyres treats quantities as fixed and overstates the effect of substitution. Quoting an average of them without saying which is used mixes two different baskets.

</div>

Weights need to be positive and the base value cannot be 0. If a good disappears from the basket (for example, a technology no longer sold), the old-basket price has no counterpart. Statistics agencies handle new and vanished goods with quality adjustments and by changing the basket, and the limits of that process are one reason CPI can misstate the cost of living.

Laspeyres is not always above Paasche. If consumers buy more of the goods whose prices rise most (for example because they are complements, or because income grows and tastes shift), the Paasche index can exceed the Laspeyres. Problem 7 builds such a basket. The usual ordering ($L \ge P$) comes from substitution in response to prices, and it is not a theorem for every data set.

An index cannot tell you what happened to any one household. The basket is an average over many households, and a renter and a homeowner may face very different price changes.

## Tricks and shortcuts

To read a percent change from an index, subtract 100 when the earlier value is 100 (the base). So 124.8 is 24.8% above base. For two other periods, divide: 170.0 over 152.7.

A quick real-versus-nominal conversion between two dates is a ratio of index values: amounts in the later period's dollars are the earlier amount times $\frac{I_{\text{later}}}{I_{\text{earlier}}}$. For \$30 in September 2019, that is $30 \times \frac{170.0}{136.2}$.

Laspeyres and Paasche always bracket the Fisher, because the Fisher is their geometric mean, and for two numbers that are not far apart the geometric mean is close to the arithmetic mean: $\sqrt{128.4 \times 121.4} = 124.9$ against the average 124.9. A rough check on a pair of indexes is that the Fisher is near their midpoint.

A price index and a quantity index can be combined: nominal spending growth is approximately the price index growth plus the quantity index growth, from the product rule in [growth rates and CAGR](03-growth-rates-and-cagr.md). In Example 2, spending rose 15.1% while prices (Fisher) rose 24.9%, so the implied quantity change is $\frac{1.1509}{1.2486} - 1 = -7.8\%$.

## In code

The code builds the Example 1 table, the three price indexes of Example 2, and a real wage.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

# Rebase the September CPI series so that 2019 = 100
cpi = {2019: 136.2, 2020: 136.9, 2021: 142.9, 2022: 152.7,
       2023: 158.5, 2024: 161.1, 2025: 164.9, 2026: 170.0}
rebased = {y: round(v / cpi[2019] * 100, 1) for y, v in cpi.items()}
print(rebased[2022], rebased[2026])  # 112.1 124.8

# goods: (p0, q0, p1, q1)
basket = {"bread": (2.00, 100, 2.50, 90),
          "beef": (10.00, 20, 15.00, 10),
          "chicken": (6.00, 30, 6.50, 45)}

def cost(prices_index, quantities_index):
    return sum(g[prices_index] * g[quantities_index] for g in basket.values())

# indexes in the tuple: 0 = p0, 1 = q0, 2 = p1, 3 = q1
laspeyres = 100 * cost(2, 1) / cost(0, 1)
paasche = 100 * cost(2, 3) / cost(0, 3)
fisher = math.sqrt(laspeyres * paasche)
print(round(laspeyres, 1), round(paasche, 1), round(fisher, 1))  # 128.4 121.4 124.9

# Real wage in September 2019 dollars
real = 38.00 * cpi[2019] / cpi[2026]
print(round(real, 2), round((real / 30 - 1) * 100, 2))  # 30.44 1.48
```

</details>

## FAQ

### Why is the base always 100?

It is a convention that makes reading easy: a value of 112 is 12% above the base. Any positive number would work, and some indexes use 1 or 1,000. The base year is also arbitrary, which is why agencies rebase from time to time.

### Why not use the current year's basket, since it is more up to date?

Because it makes the index hard to compute and to compare over time: the weights change every year and you need current quantities, which arrive late. Laspeyres needs only prices in the current period (quantities stay fixed from the base period). That makes it fast and cheap, which is why price indexes like the CPI use it, with the basket refreshed periodically.

### Which index is right: Laspeyres, Paasche or Fisher?

None is right in every sense. They answer different questions, and they differ when relative prices and quantities have moved. Fisher is a useful compromise, and statistical agencies use Fisher-type formulas for some real measures. The size of the gap in Example 2 (7 index points, about 6%) is exaggerated by a dramatic switch from beef to chicken.

### Can an index be below 100?

Yes. Below 100 means the variable is below its base level. An index of 80 means 20% lower. An index of 0 would mean the variable fell to zero, and a negative index can't arise from positive values.

## Practice

### Warm-up

1\. A value is 84 and the base value is 70. Find the index. What does an index of 80 mean?

<details class="solution" markdown>
<summary>Solution</summary>

$100 \times \frac{84}{70} = 120$, so the value is 20% above the base. An index of 80 means the variable is 80% of its base, which is 20% below it.

Check: $70 \times 1.20 = 84$.

</details>

2\. An index with 2010 = 100 reads 118 in 2015 and 130 in 2020. Rebase it so that 2015 = 100, and find the new values for 2010 and 2020.

<details class="solution" markdown>
<summary>Solution</summary>

Divide by 118 and multiply by 100. For 2010: $\frac{100}{118} \times 100 = 84.7$. For 2020: $\frac{130}{118} \times 100 = 110.2$.

Check: the 2015 value is 100, and the growth from 2015 to 2020 is $\frac{130}{118} - 1 = 10.2\%$, which matches $110.2 - 100$ because the 2015 value is 100.

</details>

3\. An index rises from 125 to 130. Find the change in points and the percent change.

<details class="solution" markdown>
<summary>Solution</summary>

The change is $130 - 125 = 5$ points. The percent change is $\frac{130}{125} - 1 = 0.04$, which is 4%.

Check: $125 \times 1.04 = 130$. The two differ because the starting index is not 100.

</details>

### Standard

4\. A basket has two goods. Good X: base price \$4, base quantity 10, current price \$5, current quantity 8. Good Y: base price \$10, base quantity 5, current price \$11, current quantity 6 (made-up). Find the Laspeyres, Paasche and Fisher price indexes.

<details class="solution" markdown>
<summary>Solution</summary>

Laspeyres: $\frac{5 \times 10 + 11 \times 5}{4 \times 10 + 10 \times 5} = \frac{105}{90}$, so $L = 116.7$.

Paasche: $\frac{5 \times 8 + 11 \times 6}{4 \times 8 + 10 \times 6} = \frac{106}{92}$, so $P = 115.2$.

Fisher: $\sqrt{116.67 \times 115.22} = 115.9$.

Check: the price relatives are 125 (X) and 110 (Y), and each index lies between them. $L > P$, as expected when buyers shift from X (the faster riser) to Y.

</details>

5\. An old index (2002 = 100) reads 140 in 2012. A new index (2012 = 100) reads 106 in 2018 and 115 in 2022. Put 2018 and 2022 on the old base, and find the percent growth from 2012 to 2022.

<details class="solution" markdown>
<summary>Solution</summary>

The link factor is $\frac{140}{100} = 1.40$. The 2018 value is $140 \times 1.06 = 148.4$ and the 2022 value is $140 \times 1.15 = 161.0$. Growth from 2012 to 2022 is $\frac{161.0}{140} - 1 = 15\%$, the same as the new index's 115.

Check: $148.4 \div 140 = 1.06$ and $161.0 \div 148.4 = 1.0849$, matching $\frac{115}{106}$.

</details>

6\. A nominal wage index (2020 = 100) is 118 in 2025, and the CPI (2020 = 100) is 112 in 2025 (made-up values). Find the real wage index for 2025 and the real growth, and compare with nominal growth minus inflation.

<details class="solution" markdown>
<summary>Solution</summary>

The real wage index is $100 \times \frac{118}{112} = 105.4$, so real wages are 5.4% higher. Nominal growth minus inflation is $18 - 12 = 6$ points, a rounder, slightly high version.

Check: $1.18 \div 1.12 = 1.0536$.

</details>

### Challenge

7\. Build a two-good basket in which the Paasche index is larger than the Laspeyres index. Use good X with prices \$2 then \$3 and quantities 10 then 12, and good Y with prices \$5 then \$5 and quantities 10 then 8. Compute $L$, $P$ and $F$, and explain what happened to the quantities.

<details class="solution" markdown>
<summary>Solution</summary>

Laspeyres: $\frac{3 \times 10 + 5 \times 10}{2 \times 10 + 5 \times 10} = \frac{80}{70}$, so $L = 114.3$.

Paasche: $\frac{3 \times 12 + 5 \times 8}{2 \times 12 + 5 \times 8} = \frac{76}{64}$, so $P = 118.75$.

Fisher: $\sqrt{114.29 \times 118.75} = 116.5$.

The buyer bought more of X, the good whose price rose 50%, and less of Y, whose price did not change. That is the opposite of substitution, so the current basket leans toward the good whose price rose, and $P > L$. The ordering $L \ge P$ rests on buyers shifting toward the goods whose prices rise less.

Check: $L$ and $P$ are both between the price relatives, 100 and 150.

</details>

8\. (Reviews [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).) A price index is 100 in year 0, rises 5% in year 1, then falls 5% in year 2. What is the index in year 2? Is the change from year 0 to year 2 equal to 0 points?

<details class="solution" markdown>
<summary>Solution</summary>

Year 1: $100 \times 1.05 = 105$. Year 2: $105 \times 0.95 = 99.75$. So the index is 99.75, a fall of 0.25 points, which is 0.25% (since the base is 100). Rises and falls of the same percent don't cancel.

Check: $1.05 \times 0.95 = 0.9975$.

</details>

## Where this shows up

- [GDP and the circular flow](05-gdp-and-the-circular-flow.md) and [nominal vs real GDP and the deflator](06-nominal-vs-real-gdp-and-the-deflator.md) apply Laspeyres, Paasche and chain-linking to output, and [CPI and inflation](07-cpi-and-inflation.md) builds the CPI as a fixed-basket index and discusses its substitution bias.
- Finance: the S&P/TSX Composite and other stock indexes are weighted averages of prices, and inflation and real returns<!-- link: ../../08-financial-math/02-interest-and-growth/06-inflation-and-real-returns.md --> uses the real-versus-nominal formula from this lesson.
- In data work, normalizing a series to its first value (so it starts at 1 or 100) is an index, and it is the standard way to put differently scaled series on one chart.
