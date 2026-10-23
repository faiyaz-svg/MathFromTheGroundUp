# CPI and inflation

After this lesson you can compute inflation from the Consumer Price Index (year over year and month over month), build a CPI from a basket with weights, restate wages and prices in today's dollars, say what core measures such as CPI-trim and CPI-median are for, describe the Bank of Canada's inflation target, and explain why the CPI can misstate the cost of living.

Before this: [index numbers](04-index-numbers.md), [growth rates and CAGR](03-growth-rates-and-cagr.md) and [nominal vs real GDP and the deflator](06-nominal-vs-real-gdp-and-the-deflator.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Canada's CPI (2002 = 100) was 164.9 in September 2025 and 170.0 in September 2026. What is the inflation rate over the year?
2. The CPI was 169.8 in August 2026 and 170.0 in September 2026. What is the monthly change?
3. The CPI was 116.9 in September 2010. What is \$1,000 of September 2010 worth in September 2026 dollars?

<details class="solution" markdown>
<summary>Answers</summary>

1. $\frac{170.0}{164.9} - 1 = 0.0309$, so 3.1% (the published rate, rounded to one decimal).
2. $\frac{170.0}{169.8} - 1 = 0.0012$, so about 0.12% for the month.
3. Multiply by the ratio of price levels: $1000 \times \frac{170.0}{116.9} = 1454.23$, about \$1,454.

</details>

## The idea

The Consumer Price Index (CPI) answers the question "how much has the cost of living changed?" by pricing a fixed shopping basket, the same list of goods and services in each period, and comparing its cost over time. The basket contains what households buy: food, rent, gasoline, phone plans, haircuts. Each item counts in proportion to how much households spend on it, so rent (a large part of a typical budget) counts for more than clothing.

Canadian data show how this works. In September 2026 the CPI stood at 170.0 (2002 = 100), against 164.9 a year earlier, so prices rose 3.1% over the year (Bank of Canada, [CPI data](https://www.bankofcanada.ca/rates/price-indexes/cpi/), Statistics Canada Table 18-10-0004-01). Within the total, gasoline was up 27.8% and food 2.2%, and a measure that ignores the most volatile prices, CPI-trim, was 1.8%. One headline number hides a mix, and a short list of related measures tells you more than one does.

The Bank of Canada uses the CPI to judge whether it is meeting its target of keeping inflation at 2%, the midpoint of a 1% to 3% control range (Bank of Canada, [inflation](https://www.bankofcanada.ca/core-functions/monetary-policy/inflation/)). The same index is used to adjust pensions, tax brackets and the value of old amounts of money. This lesson shows the arithmetic behind all of those uses and its limits.

## Definitions

The **Consumer Price Index (CPI)** is a price index that measures the change over time in the cost of a fixed basket of goods and services bought by consumers. It is a Laspeyres-type index from [index numbers](04-index-numbers.md), with weights taken from household spending. Statistics Canada's CPI has the base 2002 = 100 (so a value of 170.0 means prices are 70% above their 2002 average).

A **basket weight** is the share of total spending that a category of goods has in the basket. The weights add up to 100%. With category price relatives $\frac{p_{1i}}{p_{0i}}$ and weights $w_i$ (as decimals), the change in the CPI is the weighted average

$$
\frac{\text{CPI}_1}{\text{CPI}_0} \approx \sum_i w_i \frac{p_{1i}}{p_{0i}},
$$

with the weights measured at the base period's prices. In plain words, the CPI's growth is the average growth of the categories, weighted by how much households spend on each.

The **inflation rate** is the percent change in the price level, usually measured with the CPI. The **year-over-year** (12-month) rate compares a month with the same month a year earlier: $\pi_t^{\text{yoy}} = \frac{\text{CPI}_t}{\text{CPI}_{t-12}} - 1$. The **month-over-month** rate compares a month with the previous month, $\frac{\text{CPI}_t}{\text{CPI}_{t-1}} - 1$, and can be annualized as in [growth rates and CAGR](03-growth-rates-and-cagr.md). In plain words, the year-over-year rate says what happened over the last year, and the month-over-month rate says what happened last month, and it is noisier.

**Seasonally adjusted** values remove the regular pattern that repeats each year (clothing sales in January, gasoline in summer), so that months can be compared directly. Year-over-year rates need no seasonal adjustment, since the same month is compared with itself.

**Headline inflation** is the percent change in the total CPI. **Core inflation** is a measure meant to show the underlying trend by reducing the effect of volatile or one-off price changes. The Bank of Canada follows measures such as **CPI-trim**, the average price change after removing the components with the most extreme (largest and smallest) changes each month, and **CPI-median**, the price change of the component in the middle of the distribution, weighted by expenditure. In plain words, they ask what inflation looks like if you ignore the biggest outliers.

**Purchasing power** of a dollar is how much it buys, which is the reciprocal of the price level. If prices double, the purchasing power of a dollar halves.

## How to do it

### Inflation from the CPI

1. Find the CPI in the two months. For year over year, take the same month in two years.
2. Divide the later value by the earlier one and subtract 1: $\frac{\text{CPI}_t}{\text{CPI}_{t-12}} - 1$.
3. Round to one decimal place, as Statistics Canada publishes.
4. For a monthly rate, divide by the previous month; to annualize it, raise the monthly growth factor to the 12th power.
5. Check by multiplying: $\text{CPI}_{t-12} \times (1 + \pi) = \text{CPI}_t$.

### Adjusting an amount to another date's dollars

1. Find the CPI at the date of the amount, $\text{CPI}_{\text{then}}$, and at the date you want, $\text{CPI}_{\text{now}}$.
2. Multiply the amount by $\frac{\text{CPI}_{\text{now}}}{\text{CPI}_{\text{then}}}$.
3. Check the direction: moving forward in time, prices have risen, so the amount in today's dollars is bigger.

To compare a wage with prices, put both in the same dollars, or compare growth factors: real wage growth is $\frac{1 + \text{wage growth}}{1 + \text{inflation}} - 1$.

### Building a CPI from a basket

1. List the categories and their weights $w_i$ (as decimals that add to 1). The weights come from household spending surveys.
2. For each category, find the price relative: price now divided by price in the base period.
3. Compute the weighted average: $\sum w_i \times \text{relative}_i$.
4. Multiply by 100 for an index with the base at 100, and by the earlier index value if chaining.
5. Check that the answer lies between the smallest and largest relative.

Statistics Canada publishes the weights for the 2025 basket by category (Table 18-10-0007-01). At link month prices they are: food 16.93%, shelter 28.30%, household operations, furnishings and equipment 12.80%, clothing and footwear 4.50%, transportation 18.54%, health and personal care 5.40%, recreation, education and reading 9.81%, and alcoholic beverages, tobacco products and recreational cannabis 3.73% (the total is 100.01 because of rounding). Shelter and transportation together are nearly half of the basket.

### Contributions to inflation

The change in the all-items CPI is about the sum of each category's weight times its own price change. A category with a big weight and a modest price rise, or a small weight and a big rise, can each contribute a lot. Example 3 does this for September 2026.

### Core measures

Headline inflation moves with prices that jump around for reasons unrelated to the general trend, such as gasoline. Core measures reduce that. The Bank of Canada reports CPI-trim and CPI-median every month alongside the headline figure. When headline inflation is well above the core measures, one or a few components are pushing it. When they are close, price increases are broad.

### The Bank of Canada's target

The Bank aims to keep inflation at the 2% midpoint of a 1% to 3% control range, measured as the year-over-year increase in the total CPI. Its main tool is the target for the overnight rate, which stood at 2.25% in October 2026 (Bank of Canada Valet series V39079, daily value on October 20, 2026; the last change was a 25 basis point cut on October 29, 2025, according to the Bank's [key interest rate](https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/) page). A policy rate set above inflation makes borrowing more costly in real terms. The real rate is approximately the nominal rate minus inflation, $2.25\% - 3.1\% = -0.85$ points on the September 2026 figure, an ex-post number that looks backward (the finance lesson on inflation and real returns<!-- link: ../../08-financial-math/02-interest-and-growth/06-inflation-and-real-returns.md --> gives the exact formula).

### Why the CPI can misstate the cost of living

A fixed basket is a simplification, and the CPI can differ from the true change in the cost of living:

- Substitution bias. When one good gets expensive, households buy less of it, and a fixed basket keeps pricing the old quantities. This is the Laspeyres effect in [index numbers](04-index-numbers.md), and it makes the CPI tend to overstate the rise in the cost of living.
- Quality change. A phone that costs the same as last year's and does much more is a price fall in effect, and statisticians try to adjust for quality, imperfectly.
- New goods and outlets. Goods that did not exist when the basket was set, and shopping at discount outlets that spread, are caught late.
- Different households. The basket is an average. A household that rents faces a different price change than one with a mortgage, and a household that drives a lot is hit harder by gasoline prices.

These effects can push the measured rate above or below a particular household's experience, and the usual view is that on balance a fixed-basket CPI tends to overstate the true cost-of-living change by a small amount. The size is debated.

## Worked examples

<div class="example" markdown>

### Example 1: inflation from the index

Using the CPI (2002 = 100) of 164.9 in September 2025, 169.8 in August 2026 and 170.0 in September 2026 (Bank of Canada, [CPI data](https://www.bankofcanada.ca/rates/price-indexes/cpi/)), find the year-over-year rate for September 2026, the month-over-month rate and the annualized monthly rate.

Step 1: the two values for the year-over-year rate are 164.9 and 170.0.

Step 2: $\frac{170.0}{164.9} = 1.03093$.

Step 3: inflation is 3.09%, which rounds to 3.1%.

Step 4: month over month, $\frac{170.0}{169.8} = 1.001178$, so 0.12% for the month. Annualized, $1.001178^{12} - 1 = 1.42\%$.

Step 5: check: $164.9 \times 1.0309 = 170.0$.

The year-over-year rate (3.1%) and the annualized monthly rate (1.4%) are far apart. The first looks back over twelve months, during which gasoline prices rose a lot, and the second extrapolates one quiet month. Neither is wrong. They answer different questions.

</div>

<div class="example" markdown>

### Example 2: a monthly table with core measures

These are the Bank of Canada's published figures for 2026 (CPI index with 2002 = 100, then the year-over-year rates of the total CPI, CPI-trim and CPI-median, in percent; source: Bank of Canada Valet CPI group, from Statistics Canada):

| Month, 2026 | CPI | Total, yoy | CPI-trim | CPI-median |
|---|---|---|---|---|
| January | 165.0 | 2.3 | 2.4 | 2.5 |
| February | 165.9 | 1.8 | 2.3 | 2.3 |
| March | 167.4 | 2.4 | 2.2 | 2.3 |
| April | 168.0 | 2.8 | 2.0 | 2.1 |
| May | 169.6 | 3.2 | 2.0 | 2.1 |
| June | 169.0 | 2.8 | 1.9 | 1.9 |
| July | 169.9 | 3.0 | 1.9 | 2.0 |
| August | 169.8 | 3.0 | 1.9 | 2.0 |
| September | 170.0 | 3.1 | 1.8 | 1.9 |

Describe the pattern and compare with the target.

Step 1: from January to September the total CPI inflation rose from 2.3% to 3.1%, moving above the top of the 1% to 3% control range in May (3.2%) and again in September (3.1%).

Step 2: over the same months CPI-trim fell from 2.4% to 1.8% and CPI-median from 2.5% to 1.9%, both slightly below the 2% target by September.

Step 3: the gap between the headline rate and the core measures grew from $-0.1$ points in January (2.3 against 2.4) to $+1.3$ points in September (3.1 against 1.8).

Check: the CPI index agrees with the January-to-September rise of $\frac{170.0}{165.0} - 1 = 3.0\%$ over eight months. The rise in headline inflation came from a few components (Example 3), and the broad measures of underlying inflation were lower than the 2% target by September.

</div>

<div class="example" markdown>

### Example 3: contributions by category, September 2026

The 2025 basket weights (Statistics Canada Table 18-10-0007-01) and the September 2025 and September 2026 category indexes (Table 18-10-0004-01) are:

| Category | Weight (%) | Sept 2025 | Sept 2026 | Change (%) | Weight times change |
|---|---|---|---|---|---|
| Food | 16.93 | 197.5 | 201.8 | 2.18 | 0.369 |
| Shelter | 28.30 | 188.2 | 191.5 | 1.75 | 0.496 |
| Household operations, furnishings and equipment | 12.80 | 134.1 | 134.7 | 0.45 | 0.057 |
| Clothing and footwear | 4.50 | 93.5 | 95.1 | 1.71 | 0.077 |
| Transportation | 18.54 | 171.8 | 186.3 | 8.44 | 1.565 |
| Health and personal care | 5.40 | 155.8 | 158.5 | 1.73 | 0.094 |
| Recreation, education and reading | 9.81 | 129.6 | 135.6 | 4.63 | 0.454 |
| Alcohol, tobacco and cannabis | 3.73 | 200.8 | 204.1 | 1.64 | 0.061 |

Find the weighted sum and compare with the published 3.1%.

Step 1: add the last column: $0.369 + 0.496 + 0.057 + 0.077 + 1.565 + 0.094 + 0.454 + 0.061 = 3.173$ percentage points.

Step 2: the result, about 3.2%, is close to the published 3.1%. It is not identical because the weights are measured at the basket's own link-month prices and not at September 2025 prices (items that got relatively more expensive have a bigger share of spending now than in the table), and because of rounding.

Step 3: transportation contributes $1.565$ of the 3.17 points, nearly half, with 18.5% of the weight and an 8.4% rise. Gasoline is inside transportation. Its weight is 4.01% (link month prices) and its index rose from 209.4 to 267.6, which is 27.8%, so it alone contributes about $0.0401 \times 27.8 = 1.11$ points.

Check: the weights sum to 100.01%, and the weighted sum, divided by the weight total, is 3.17%, between the smallest (0.45%) and largest (8.44%) category changes.

</div>

<div class="example" markdown>

### Example 4: gasoline and the headline (finish it yourself)

Use Example 3 and the CPI-trim rate of 1.8% for September 2026. The gap between headline inflation (3.1%) and CPI-trim (1.8%) is 1.3 percentage points. Gasoline's weight is 4.01% and its price rose 27.8% over the year.

Find gasoline's contribution in percentage points, and say what share of the headline inflation of 3.1% it explains.

<details class="solution" markdown>
<summary>Finish</summary>

The contribution is $0.0401 \times 27.8 = 1.11$ percentage points. Its share of the 3.1% headline is $\frac{1.11}{3.1} = 36\%$.

Gasoline alone explains about 1.1 of the 1.3 points of gap, so most of the difference between headline inflation and the trimmed measure is gasoline. Without the gasoline rise, headline inflation would have been about 2.0%, close to the target.

Check: $3.1 - 1.1 = 2.0$, and this is an approximation (it ignores the small change in weights).

</details>

</div>

<div class="example" markdown>

### Example 5: today's dollars and a real wage

These wage figures are made up. In September 2010 you earned \$22 an hour, and now you earn \$28. The CPI was 116.9 in September 2010 and 170.0 in September 2026 (Table 18-10-0004-01). Did your buying power rise?

The old wage in September 2026 dollars is $22 \times \frac{170.0}{116.9} = 31.99$, about \$31.99. Your wage is \$28, below that, so buying power fell.

In growth terms, the wage rose $\frac{28}{22} - 1 = 27.3\%$ and prices rose $\frac{170.0}{116.9} - 1 = 45.4\%$. Real wage growth is $\frac{1.2727}{1.4542} - 1 = -12.5\%$.

Check: $31.99 \times (1 - 0.125) = 28.0$. A wage of \$28 buys what $28 \times \frac{116.9}{170.0} = \$19.25$ bought in 2010.

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the CPI is an index, not a rate. A CPI of 170.0 does not mean 170% inflation. It means the price level is 70% above the base year (2002). Inflation is the percent change between two index values.

</div>

<div class="warning" markdown>

Watch out: year-over-year and month-over-month rates answer different questions. A monthly rate of 0.35%, annualized, is 4.3%, and nobody should read it as the year's inflation. Monthly figures are noisy.

</div>

<div class="warning" markdown>

Watch out: inflation of 3.1% means prices are still going up, only more slowly than a year ago if the rate fell. When inflation falls from 8.1% to 3.1%, prices are not falling: the price level is still rising, by less each year. Prices fall only when the inflation rate is negative (deflation).

</div>

<div class="warning" markdown>

Watch out: "adjusting for inflation" goes the right way only if you multiply by the later index over the earlier one. To put a 2010 amount in 2026 dollars, multiply by $\frac{170.0}{116.9}$, not by $\frac{116.9}{170.0}$.

</div>

The peak in recent years was a year-over-year rate of 8.1% in June 2022 (computed from the CPI index, 152.9 against 141.4 a year earlier, and published as 8.1%). A level of prices that rose by 8.1% in a year doesn't come back down when inflation falls: the CPI in September 2026 (170.0) is still well above its June 2022 value, and a household's budget stays larger. To go back to a lower price level takes deflation, which is rare.

The CPI can't tell you about one household's cost of living. A renter in Toronto and a homeowner with no mortgage in a small town face the same national index but different prices. Core measures are also not "true" inflation. They are tools for seeing a trend, and the Bank still targets the total CPI.

## Tricks and shortcuts

To get a quick year-over-year rate from two index values, divide and subtract 1: 170.0 over 164.9 is just above 1.03, so a bit over 3%. To get dollars in another year, multiply by the ratio of indexes, and to find the loss in purchasing power, take the reciprocal: after 3.1% inflation, a dollar buys $\frac{1}{1.031} = 97\%$ of what it did, and after 10 years of 3.1%, it buys 73.7% of what it did (about a quarter less).

For a rough idea of the doubling of prices, divide 70 by the inflation rate: at the 2% target, prices double in 35 years, as in [growth rates and CAGR](03-growth-rates-and-cagr.md). Over 24 years from 2002 (index 100) to 2026 (170.0), prices rose by 70%, a CAGR of about 2.2%.

To see what is behind a headline number, multiply each category's weight by its price change, as in Example 3. A category with a 4% weight and a 28% rise contributes about 1.1 points.

When a news story gives inflation to one decimal place, don't read differences of 0.1 as a trend. The index is published to one decimal, and 0.1 of 170 is about 0.06% of the price level.

## In code

The code computes the rates of Example 1, the weighted sum of Example 3, and a price restated in today's dollars.

<details class="code" markdown>
<summary>In code</summary>

```python
cpi_sep25, cpi_aug26, cpi_sep26 = 164.9, 169.8, 170.0

yoy = cpi_sep26 / cpi_sep25 - 1
mom = cpi_sep26 / cpi_aug26 - 1
print(round(yoy * 100, 2), round(mom * 100, 2), round(((1 + mom) ** 12 - 1) * 100, 2))
# 3.09 0.12 1.42

# Contributions by category: (weight %, Sept 2025 index, Sept 2026 index)
basket = {
    "Food": (16.93, 197.5, 201.8),
    "Shelter": (28.30, 188.2, 191.5),
    "Household": (12.80, 134.1, 134.7),
    "Clothing": (4.50, 93.5, 95.1),
    "Transportation": (18.54, 171.8, 186.3),
    "Health": (5.40, 155.8, 158.5),
    "Recreation": (9.81, 129.6, 135.6),
    "Alcohol": (3.73, 200.8, 204.1),
}
contribution = sum(w * (new / old - 1) for w, old, new in basket.values())
print(round(contribution, 2))  # 3.17

# 22 dollars an hour in September 2010, in September 2026 dollars
print(round(22 * 170.0 / 116.9, 2))  # 31.99
```

</details>

## FAQ

### Why does the Bank of Canada target 2% and not zero?

A little inflation gives room to lower real interest rates in a downturn, and it makes the measured price level less likely to slip into deflation because of small measurement errors, such as quality changes that the CPI misses. Zero inflation would leave less room for error. The Bank's framework sets the target at 2%, with a control range of 1% to 3% around it.

### Why does my own inflation differ from the CPI?

The CPI uses average spending shares. If you spend more on rent or gasoline than the average household, price changes in those categories matter more to you. You can compute your own rate with your own weights, as in the basket method above.

### Why do headline and core inflation differ?

Headline inflation includes every component, and core measures reduce the weight of the components that are moving the most, which are often energy or food. When a few prices jump, headline moves and core doesn't. A persistent gap would mean the jump is lasting.

### Does a fall in the inflation rate mean prices are falling?

No. It means they are rising more slowly. Prices fall only if the rate is negative.

## Practice

### Warm-up

1\. The CPI was 161.1 in September 2024 and 164.9 in September 2025, and 158.5 in September 2023 (Table 18-10-0004-01). Find the year-over-year inflation for September 2025 and for September 2024.

<details class="solution" markdown>
<summary>Solution</summary>

September 2025: $\frac{164.9}{161.1} - 1 = 0.0236$, so 2.4%. September 2024: $\frac{161.1}{158.5} - 1 = 0.0164$, so 1.6%.

Check: $161.1 \times 1.0236 = 164.9$ and $158.5 \times 1.0164 = 161.1$.

</details>

2\. The CPI was 128.8 in September 2016 and 108.4 in September 2005, and 170.0 in September 2026. Find \$1,000 from each earlier date in September 2026 dollars.

<details class="solution" markdown>
<summary>Solution</summary>

From 2016: $1000 \times \frac{170.0}{128.8} = 1319.88$, about \$1,320. From 2005: $1000 \times \frac{170.0}{108.4} = 1568.27$, about \$1,568.

Check: the older amount grows more, as it should: more years of price increases.

</details>

3\. In September 2026, headline CPI inflation was 3.1%, CPI-trim 1.8% and CPI-median 1.9%. Find the gap between headline and each core measure in percentage points, and say which side of the 2% target each is on.

<details class="solution" markdown>
<summary>Solution</summary>

Headline minus trim is $3.1 - 1.8 = 1.3$ points, and minus median is $3.1 - 1.9 = 1.2$ points. The headline is above the 2% target (and just above the top of the 1% to 3% range), and both core measures are just below it.

Check: the median is 0.1 above the trim, so the gaps differ by 0.1.

</details>

### Standard

4\. A mini basket has weights 40% for food, 35% for rent and 25% for transport. Between two years food prices rise 5%, rent 2% and transport 10%. Find the CPI change.

<details class="solution" markdown>
<summary>Solution</summary>

The weighted average of the relatives is $0.40 \times 1.05 + 0.35 \times 1.02 + 0.25 \times 1.10 = 0.420 + 0.357 + 0.275 = 1.052$, so the CPI rose 5.2%.

Check: 5.2% lies between the smallest (2%) and the largest (10%) category increase.

</details>

5\. The seasonally adjusted CPI rises 0.35% in a month. Find the annualized rate (compounded) and the simple estimate. Why shouldn't you quote it as the year's inflation?

<details class="solution" markdown>
<summary>Solution</summary>

Compounded: $1.0035^{12} - 1 = 0.0428$, so 4.28%. Simple: $12 \times 0.35\% = 4.2\%$.

One month's change repeated for twelve months is a statement about that one month. Monthly CPI changes are volatile (for example, they react to gasoline), so the year's inflation could be very different.

Check: $1.0035^{12} = 1.0428$.

</details>

6\. These wages are made up. You earned \$30.00 an hour in September 2019 (CPI 136.2) and you earn \$31.20 in September 2026 (CPI 170.0), after a 4% raise this year. Find what the old wage is in 2026 dollars, and the real wage growth this year if inflation was 3.1%.

<details class="solution" markdown>
<summary>Solution</summary>

The old wage in 2026 dollars is $30.00 \times \frac{170.0}{136.2} = 37.44$, so \$37.44, and \$31.20 is far below it. The 4% raise against 3.1% inflation is a real gain of $\frac{1.04}{1.031} - 1 = 0.87\%$ this year.

Check: $1.0087 \times 1.031 = 1.04$. Over seven years, the raise this year can't offset the earlier loss of buying power, because \$31.20 is 17% below \$37.44.

</details>

### Challenge

7\. In [index numbers](04-index-numbers.md), Example 2 found a Laspeyres price index of 128.4 and a Fisher index of 124.9 for a made-up basket. Suppose the Fisher index measures the true change in the cost of living. By how much does the Laspeyres index overstate it? What does this say about the CPI?

<details class="solution" markdown>
<summary>Solution</summary>

The overstatement is $\frac{128.4}{124.9} - 1 = 0.028$, about 2.8% of the price level, or 3.5 index points.

The CPI is a fixed-basket index of the Laspeyres type, so it has this substitution bias in principle. The size here is large because the made-up basket has a dramatic switch from beef to chicken. In real data the bias is smaller, and statistical agencies update the basket weights to keep it down.

Check: $124.9 \times 1.028 = 128.4$.

</details>

8\. (Reviews [percent change vs percentage points](02-percent-change-vs-percentage-points.md).) CPI-trim was 3.1% in September 2025 and 1.8% in September 2026. Find the change in percentage points and basis points and the relative change.

<details class="solution" markdown>
<summary>Solution</summary>

The change is $1.8 - 3.1 = -1.3$ percentage points, which is $-130$ basis points. The relative change is $\frac{-1.3}{3.1} = -0.419$, a fall of 41.9% in the rate.

Check: $3.1 \times (1 - 0.419) = 1.8$. A headline "CPI-trim fell 42%" and "fell 1.3 points" are both true and describe different things.

</details>

## Where this shows up

- [Unemployment rate and labour statistics](08-unemployment-rate-and-labour-statistics.md) is the other number in the central bank's dual view of the economy. Inflation and real returns<!-- link: ../../08-financial-math/02-interest-and-growth/06-inflation-and-real-returns.md --> uses the CPI to turn nominal returns into real ones, and [multipliers and the AD-AS model](../04-more-tools/02-multipliers-and-the-ad-as-model.md) puts the price level on a graph.
- In personal finance, tax brackets, the Canada Pension Plan and many contracts are indexed to the CPI, so a few tenths of a percent matter to a large amount of money.
- In data work, adjusting any series in dollars (salaries, revenue, house prices) for inflation is one multiplication by a ratio of index values.
