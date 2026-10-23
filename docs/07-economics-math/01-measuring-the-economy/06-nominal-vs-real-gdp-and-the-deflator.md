# Nominal vs real GDP and the deflator

After this lesson you can compute nominal and real GDP for a small economy, find the GDP deflator, split nominal growth into real growth and inflation (approximately and exactly), explain why the base year matters, and read Statistics Canada's chained-dollar figures.

Before this: [GDP and the circular flow](05-gdp-and-the-circular-flow.md), [index numbers](04-index-numbers.md) and [growth rates and CAGR](03-growth-rates-and-cagr.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Nominal GDP rises from 2,000 to 2,184 while the GDP deflator rises from 100 to 104. What are the nominal growth and the real growth?
2. Nominal GDP is 1,300 and the deflator is 125 (base year = 100). What is real GDP?
3. Real growth is 3% and the deflator rises 2%. About how fast does nominal GDP grow?

<details class="solution" markdown>
<summary>Answers</summary>

1. Nominal growth is $\frac{2184}{2000} - 1 = 9.2\%$. Real growth is $\frac{1.092}{1.04} - 1 = 5.0\%$, which is nominal growth stripped of the 4% price rise.
2. Real GDP is $\frac{1300}{125} \times 100 = 1040$.
3. About $3\% + 2\% = 5\%$. Exactly, $1.03 \times 1.02 - 1 = 5.06\%$.

</details>

## The idea

Canada's GDP in 2025 was about \$3.245 trillion, and in 2024 it was about \$3.109 trillion, a rise of 4.4% (Statistics Canada, Table 36-10-0104-01, current prices; see [GDP and the circular flow](05-gdp-and-the-circular-flow.md)). Did Canadians produce 4.4% more goods and services? No. Most of the rise was higher prices: the same loaf of bread is worth more dollars than it was a year earlier, so a dollar total can grow without any new bread being baked.

To measure the change in production itself, economists value each year's output at the same prices. The resulting figure is real GDP, and the dollar total at actual prices is nominal GDP. Dividing the nominal figure by the real one gives a price index for everything the economy produced, the GDP deflator. The three numbers are tied together so that if you know any two you can find the third, and nominal growth splits cleanly into a real part and an inflation part.

This lesson works through a two-good economy where you can see every number, and then reads the same decomposition in Canada's accounts.

## Definitions

**Nominal GDP** is GDP measured at the prices of the year in which the output was produced (current prices). In plain words, it is the output valued at that year's own prices. For goods $i = 1, \dots, m$, with current prices $p_{ti}$ and quantities $q_{ti}$ in year $t$,

$$
\text{nominal GDP}_t = \sum_i p_{ti}\, q_{ti}.
$$

**Real GDP** is GDP measured at the prices of a fixed base year, so that only quantities change from year to year. If $p_{bi}$ are the base-year prices,

$$
\text{real GDP}_t = \sum_i p_{bi}\, q_{ti}.
$$

In plain words, real GDP asks "what would this year's output have been worth at base-year prices?". In the base year itself, real and nominal GDP are equal.

The **GDP deflator** is the ratio of nominal to real GDP, times 100:

$$
\text{deflator}_t = 100 \times \frac{\text{nominal GDP}_t}{\text{real GDP}_t}.
$$

In plain words, it is a price index for all domestic output with the base year at 100. Substituting the definitions, the deflator is $100 \times \frac{\sum p_{ti} q_{ti}}{\sum p_{bi} q_{ti}}$, which is the Paasche price index from [index numbers](04-index-numbers.md) (current quantities in both the top and the bottom). A deflator of 129.7 means prices of domestic output are 29.7% higher than in the base year.

**Inflation**, measured by the deflator, is the growth rate of the deflator, $\pi_t = \frac{D_t}{D_{t-1}} - 1$, where $D_t$ is the deflator in year $t$. **Real growth** is the growth rate of real GDP. **Nominal growth** is the growth rate of nominal GDP.

**Chained dollars** are real values built by linking year-to-year volume changes instead of fixing one base year's prices forever. For each pair of adjacent years the volume change is computed with prices of those two years (Statistics Canada uses a Fisher-type formula), and the yearly growth factors are multiplied together (as in the chain index of [index numbers](04-index-numbers.md)). The result is quoted in "chained (2017) dollars", which means the real series equals nominal GDP in the reference year 2017 and moves by the chained volume growth in every other year.

## How to do it

### Nominal, real, deflator and growth from quantities and prices

1. List each good's price and quantity in each year, and pick the base year.
2. Compute nominal GDP in each year: price times quantity, summed over goods.
3. Compute real GDP in each year at base-year prices: base-year price times that year's quantity, summed over goods.
4. Compute the deflator: $100 \times \frac{\text{nominal}}{\text{real}}$.
5. Compute the growth rates of nominal GDP, real GDP and the deflator, with $\frac{x_t}{x_{t-1}} - 1$.
6. Check the identity in the next section: nominal growth factor = real growth factor times deflator growth factor.

### Splitting nominal growth into real growth and inflation

Since $\text{nominal} = \text{real} \times \frac{\text{deflator}}{100}$ in every year, dividing the equation for year $t$ by the one for year $t - 1$ gives

$$
\frac{N_t}{N_{t-1}} = \frac{R_t}{R_{t-1}} \cdot \frac{D_t}{D_{t-1}},
$$

where $N$, $R$ and $D$ are nominal GDP, real GDP and the deflator. In terms of growth rates, with $g_N$, $g_R$ and $\pi$:

$$
1 + g_N = (1 + g_R)(1 + \pi).
$$

This is the product rule from [growth rates and CAGR](03-growth-rates-and-cagr.md). Expanding it, $g_N = g_R + \pi + g_R \pi$, so for small rates

$$
g_N \approx g_R + \pi, \qquad g_R \approx g_N - \pi.
$$

In plain words, nominal growth is about real growth plus inflation, and the exact version has a small cross term. To get real growth exactly, divide: $g_R = \frac{1 + g_N}{1 + \pi} - 1$. In logs the identity is exact, $\ln\frac{N_t}{N_{t-1}} = \ln\frac{R_t}{R_{t-1}} + \ln\frac{D_t}{D_{t-1}}$.

### Why the base year matters, and how chaining helps

Real GDP depends on which year's prices are used as weights. Prices of different goods change at different rates, and quantities respond: goods whose prices fall tend to be bought in larger quantities. Valuing output at old prices gives more weight to goods that were expensive then and cheaper now (so a Laspeyres-type quantity measure, in the language of [index numbers](04-index-numbers.md)), and valuing at new prices does the opposite. For computers, whose prices keep falling while quantities soar, the choice can change real growth by a lot over a long span.

Chaining reduces the problem. Each year-to-year growth rate uses prices from the two adjacent years, so the weights stay up to date, and the growth rates are multiplied together. A drawback is that chained real components do not add up to chained real GDP: the sum of real $C$, $I$, $G$ and $NX$ in 2025 differs slightly from real GDP in that year, because each component is chained separately. Example 2 shows the gap in Canada's 2025 data. Only in the reference year does additivity hold exactly, since real and nominal agree there.

## Worked examples

<div class="example" markdown>

### Example 1: a two-good economy

These are made-up numbers. An economy makes apples and laptops. In year 1 (the base year), it produces 1,000 apples at \$2.00 and 50 laptops at \$800. In year 2, it produces 1,100 apples at \$2.20 and 60 laptops at \$820. Find nominal GDP, real GDP, the deflator and the growth rates.

Step 1: the base year is year 1.

Step 2: nominal GDP in year 1 is $1000 \times 2.00 + 50 \times 800 = 2{,}000 + 40{,}000 = 42{,}000$. In year 2 it is $1100 \times 2.20 + 60 \times 820 = 2{,}420 + 49{,}200 = 51{,}620$.

Step 3: real GDP in year 1 is 42,000 (the base year). In year 2, at year-1 prices, it is $1100 \times 2.00 + 60 \times 800 = 2{,}200 + 48{,}000 = 50{,}200$.

Step 4: the deflator in year 1 is 100. In year 2 it is $100 \times \frac{51{,}620}{50{,}200} = 102.83$.

Step 5: nominal growth is $\frac{51{,}620}{42{,}000} - 1 = 22.90\%$. Real growth is $\frac{50{,}200}{42{,}000} - 1 = 19.52\%$. Inflation (deflator) is $102.83 \div 100 - 1 = 2.83\%$.

Step 6: check the identity: $1.1952 \times 1.0283 = 1.2290$, which is the nominal growth factor. The approximation $19.52 + 2.83 = 22.35\%$ is about half a point below the exact 22.90%, because the growth rates are large.

Watch out at Step 3: using year-2 prices for the year-2 quantities is the nominal figure, not the real one. Real GDP changes only through the quantities, and every year's output is priced at \$2.00 and \$800.

</div>

<div class="example" markdown>

### Example 2: Canada, 2024 to 2025

Statistics Canada reports GDP at current prices and in chained (2017) dollars (Table 36-10-0104-01; annual figures here are the averages of the four seasonally adjusted quarterly values at annual rates, in millions of dollars). For 2024, nominal GDP was 3,108,551 and real GDP 2,456,310 (rounded). For 2025 they were 3,245,257 and 2,501,835. Find the deflator for each year and the three growth rates for 2025.

Step 1: the reference year of the chained series is 2017, so the deflator has 2017 = 100.

Step 2: deflators: $100 \times \frac{3{,}108{,}551}{2{,}456{,}310} = 126.55$ for 2024, and $100 \times \frac{3{,}245{,}257}{2{,}501{,}835} = 129.72$ for 2025.

Step 3: nominal growth: $\frac{3{,}245{,}257}{3{,}108{,}551} - 1 = 4.40\%$. Real growth: $\frac{2{,}501{,}835}{2{,}456{,}310} - 1 = 1.85\%$. Deflator growth: $\frac{129.72}{126.55} - 1 = 2.50\%$.

Step 4: the identity: $1.0185 \times 1.0250 = 1.0440$. The approximation: $1.85 + 2.50 = 4.35\%$ against the exact 4.40%.

So a bit over two-fifths of the 4.4% rise in Canada's nominal GDP in 2025 was extra output, and the rest was higher prices. Real GDP per person grew less than real GDP, because the population also grew (1.08%, Statistics Canada Table 17-10-0009-01): $\frac{1.0185}{1.0108} - 1 = 0.76\%$.

Check by chaining to the reference year: the deflator of 129.72 says prices of Canadian output in 2025 were 29.7% above 2017 levels, and the real series grew from 2,140,641 in 2017 to 2,501,835 in 2025, a CAGR of 1.97% a year over 8 years.

Non-additivity: the 2025 chained real components (household consumption 1,424,316, non-profit consumption 39,530, government consumption 553,824, fixed investment 531,291, inventories 7,436, exports 741,192, less imports 799,004, and a statistical discrepancy 822) sum to 2,499,407, which is 2,428 below real GDP of 2,501,835, a gap of 0.1%. That gap is the price of chaining.

</div>

<div class="example" markdown>

### Example 3: the base year changes real growth

Use the economy of Example 1 but take year 2 as the base year. Find real growth from year 1 to year 2, and compare with the 19.52% from Example 1.

Step 1: real GDP in year 2 is its nominal value, 51,620.

Step 2: real GDP in year 1 at year-2 prices is $1000 \times 2.20 + 50 \times 820 = 2{,}200 + 41{,}000 = 43{,}200$.

Step 3: real growth is $\frac{51{,}620}{43{,}200} - 1 = 19.49\%$.

The two base years give 19.52% and 19.49%, a very small gap here, because the relative prices barely changed. The chained measure takes the geometric mean of the two growth factors: $\sqrt{1.1952 \times 1.1949} - 1 = 19.51\%$.

Check: on the year-2 base, the deflator for year 1 is $100 \times \frac{42{,}000}{43{,}200} = 97.22$, so year 2's price level is $\frac{100}{97.22} = 1.0286$ times year 1's. That 2.86% inflation is close to the 2.83% from Example 1, and the identity holds on this base too: $1.1949 \times 1.0286 = 1.2290$.

</div>

<div class="example" markdown>

### Example 4: Canada in 2020 (finish it yourself)

Annual figures for Canada (Table 36-10-0104-01, millions of dollars, current prices and chained 2017 dollars): nominal GDP was 2,313,563 in 2019 and 2,220,527 in 2020. Real GDP was 2,241,331 in 2019 and 2,128,408 in 2020. Find nominal growth, real growth and deflator inflation for 2020.

Nominal growth: $\frac{2{,}220{,}527}{2{,}313{,}563} - 1 = -4.02\%$. Real growth: $\frac{2{,}128{,}408}{2{,}241{,}331} - 1 = -5.04\%$.

Now find deflator inflation using the ratio of the two growth factors, and check it against the approximation $g_N - g_R$.

<details class="solution" markdown>
<summary>Finish</summary>

The deflator's growth factor is $\frac{1 - 0.0402}{1 - 0.0504} = \frac{0.9598}{0.9496} = 1.0107$, so inflation was about 1.07%. The approximation is $-4.02 - (-5.04) = 1.02\%$.

Check: $0.9496 \times 1.0107 = 0.9598$, the nominal growth factor. In 2020, nominal GDP fell by 4.0% and real GDP by 5.0%: the fall in real output was bigger than the fall in nominal GDP, since prices rose slightly while output fell.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: nominal GDP growth is not output growth. Compare real GDP across years. A nominal rise of 4.4% with 2.5% inflation is 1.85% real growth.

</div>

<div class="warning" markdown>

Watch out: the base year has nothing to do with the year being studied. Real GDP in "2017 dollars" is a measure of 2025 output at 2017 prices. It is not the amount of money in 2017.

</div>

<div class="warning" markdown>

Watch out: with chained dollars, the parts don't add. Real $C$ + real $I$ + real $G$ + real $NX$ differs a little from real GDP, and that is not an error in your arithmetic. Add the parts in nominal terms, or accept a small residual in real terms.

</div>

<div class="warning" markdown>

Watch out: the approximation "real growth is nominal growth minus inflation" is good for rates of a few percent. For a high-inflation economy, nominal growth of 60% with inflation of 50% gives $\frac{1.60}{1.50} - 1 = 6.7\%$, not 10%. Use the exact division.

</div>

Real GDP can fall when nominal GDP rises (prices up, output down), and a rise in nominal GDP with a fall in the deflator means real growth is bigger than nominal growth, as in the 2019 to 2020 figures. The deflator can fall in years when the price of oil or computers drops sharply.

The GDP deflator is not the CPI. It covers everything produced in the country (including investment goods, government services and exports), and it leaves out imports. The CPI covers what households buy, including imports. The two inflation rates differ when export prices or import prices move: in 2025, the deflator rose 2.50% while the average CPI for 2025 was 2.07% above the 2024 average (computed from the monthly CPI in Bank of Canada data, Statistics Canada Table 18-10-0004-01), a gap of about 0.4 points. The next lesson, [CPI and inflation](07-cpi-and-inflation.md), builds the CPI.

If the base year changes, real GDP levels change, but growth rates change only a little. A level such as "\$2.5 trillion in 2017 dollars" cannot be compared to a level in another base.

## Tricks and shortcuts

Use $g_R \approx g_N - \pi$ to reason fast: if nominal GDP is up 5% and inflation is 2%, expect real growth near 3%. The exact figure (2.94%) is a hair under.

To restate an amount from one year in another year's prices, multiply by the ratio of deflators. A \$100 amount of 2024 output is worth $100 \times \frac{129.72}{126.55} = \$102.50$ in 2025 prices, since prices rose 2.5%. The reverse, restating \$100 of 2025 in 2024 prices, divides: $100 \times \frac{126.55}{129.72} = \$97.56$.

A table of nominal, real and deflator is redundant by one column. Given nominal and the deflator, real is $\frac{\text{nominal}}{\text{deflator}/100}$. Given real and the deflator, nominal is $\text{real} \times \frac{\text{deflator}}{100}$.

Real GDP per capita growth is about real GDP growth minus population growth. With 1.85% and 1.08%, that is about 0.77%, and the exact value is 0.76%.

## In code

The code computes Example 1 and the decomposition for Canada in 2025.

<details class="code" markdown>
<summary>In code</summary>

```python
# Example 1: made-up two-good economy; each entry is (price, quantity)
year1 = {"apples": (2.00, 1000), "laptops": (800.0, 50)}
year2 = {"apples": (2.20, 1100), "laptops": (820.0, 60)}

nominal1 = sum(p * q for p, q in year1.values())
nominal2 = sum(p * q for p, q in year2.values())
real2 = sum(year1[g][0] * year2[g][1] for g in year2)   # year-1 prices, year-2 quantities
deflator2 = 100 * nominal2 / real2
print(nominal1, nominal2, real2)  # 42000.0 51620.0 50200.0
print(round(deflator2, 2))        # 102.83

g_n = nominal2 / nominal1 - 1
g_r = real2 / nominal1 - 1
pi = deflator2 / 100 - 1
print(round(g_n * 100, 2), round(g_r * 100, 2), round(pi * 100, 2))  # 22.9 19.52 2.83
print(round((1 + g_r) * (1 + pi) - (1 + g_n), 12))  # 0.0

# Canada, millions of dollars (Table 36-10-0104-01)
n24, r24 = 3_108_551, 2_456_309.75
n25, r25 = 3_245_257, 2_501_835.0
d24, d25 = 100 * n24 / r24, 100 * n25 / r25
print(round(d24, 2), round(d25, 2))  # 126.55 129.72
print(round((n25 / n24 - 1) * 100, 2),
      round((r25 / r24 - 1) * 100, 2),
      round((d25 / d24 - 1) * 100, 2))  # 4.4 1.85 2.5
```

</details>

## FAQ

### Why not just use the CPI to deflate GDP?

The CPI prices a household basket, and GDP includes investment goods, government output and exports. Deflating by the CPI would apply household prices to goods households don't buy. The GDP deflator is built from the prices of every component of GDP, so it matches the thing being deflated.

### Is real GDP the amount of money in base-year dollars?

It is a value in the dollars of the reference year, meaning that output is priced at that year's prices. It is a convenient way to express quantity changes in dollar units. The word "real" means "adjusted for price changes" and doesn't mean "more accurate".

### Why does the deflator come out of nominal and real, and not the other way?

Statistics Canada measures nominal GDP from spending and income data, and estimates real GDP by deflating each component with its own price index. The "implicit" deflator is then the ratio of the two. The relation is an identity, so you can derive either from the other two.

### Why would real growth differ depending on the base year?

Because the weights are different prices. In a base year when computers are expensive, a rise in computer output adds a lot to real GDP, and in a later base year when computers are cheap, the same rise adds less. Chaining updates the weights every year, which reduces the problem at the cost of the non-additivity above.

## Practice

### Warm-up

1\. Nominal GDP is 1,300 and the deflator is 125. Find real GDP. If the base year's nominal GDP was 1,000, what is real growth since the base year?

<details class="solution" markdown>
<summary>Solution</summary>

Real GDP is $\frac{1300}{125} \times 100 = 1040$. In the base year nominal and real are equal, so real GDP was 1,000, and real growth is $\frac{1040}{1000} - 1 = 4\%$.

Check: $1040 \times 1.25 = 1300$.

</details>

2\. Nominal GDP grows 5.5% and the deflator rises 2.0%. Find real growth approximately and exactly.

<details class="solution" markdown>
<summary>Solution</summary>

Approximately, $5.5 - 2.0 = 3.5\%$. Exactly, $\frac{1.055}{1.02} - 1 = 3.43\%$.

Check: $1.0343 \times 1.02 = 1.0550$.

</details>

3\. In some year, nominal GDP is 1,200 and real GDP (in base-year dollars) is 1,000. What is the deflator, and what does it say about prices since the base year?

<details class="solution" markdown>
<summary>Solution</summary>

The deflator is $100 \times \frac{1200}{1000} = 120$, so the prices of domestic output are 20% higher than in the base year.

Check: $1000 \times 1.20 = 1200$.

</details>

### Standard

4\. An economy makes cars and haircuts. In year 1 (base), it makes 10 cars at \$20,000 and 1,000 haircuts at \$40. In year 2, it makes 12 cars at \$21,000 and 1,100 haircuts at \$44. Find nominal GDP, real GDP, the deflator and the growth rates for year 2.

<details class="solution" markdown>
<summary>Solution</summary>

Nominal year 1: $10 \times 20000 + 1000 \times 40 = 240{,}000$. Nominal year 2: $12 \times 21000 + 1100 \times 44 = 252{,}000 + 48{,}400 = 300{,}400$.

Real year 2 at year-1 prices: $12 \times 20000 + 1100 \times 40 = 240{,}000 + 44{,}000 = 284{,}000$.

Deflator for year 2: $100 \times \frac{300{,}400}{284{,}000} = 105.77$.

Growth: nominal $\frac{300{,}400}{240{,}000} - 1 = 25.17\%$, real $\frac{284{,}000}{240{,}000} - 1 = 18.33\%$, inflation 5.77%.

Check: $1.1833 \times 1.0577 = 1.2517$.

</details>

5\. Canada's nominal GDP was 2,965,201 in 2023 and 3,108,551 in 2024 (millions of dollars), and real GDP (chained 2017 dollars, annual averages of the quarterly table) was 2,407,055 and 2,456,310 (Table 36-10-0104-01). Find nominal growth, real growth and deflator inflation for 2024.

<details class="solution" markdown>
<summary>Solution</summary>

Nominal: $\frac{3{,}108{,}551}{2{,}965{,}201} - 1 = 4.83\%$. Real: $\frac{2{,}456{,}310}{2{,}407{,}055} - 1 = 2.05\%$. The deflators are $123.19$ and $126.55$, so inflation is $\frac{126.55}{123.19} - 1 = 2.73\%$.

Check: $1.0205 \times 1.0273 = 1.0483$, the nominal growth factor.

</details>

6\. Canada's real GDP in 2025 was 2,501,835 million chained (2017) dollars, and the population on July 1, 2025 was 41,608,982. In 2024 the figures were 2,456,310 million and 41,162,593. Find real GDP per person in each year and its growth.

<details class="solution" markdown>
<summary>Solution</summary>

2025: $\frac{2{,}501{,}835 \times 10^6}{41{,}608{,}982} = 60{,}127$ dollars. 2024: $\frac{2{,}456{,}310 \times 10^6}{41{,}162{,}593} = 59{,}673$ dollars (both in 2017 dollars). Growth: $\frac{60{,}127}{59{,}673} - 1 = 0.76\%$, matching $\frac{1.0185}{1.0108} - 1$.

Check: the approximation $1.85 - 1.08 = 0.77\%$ is within 0.01.

</details>

### Challenge

7\. An economy makes goods A and B. Year 1: A is 100 units at \$10, B is 50 units at \$20. Year 2: A is 90 units at \$15, B is 70 units at \$18. (a) Find real growth using year-1 prices. (b) Find it using year-2 prices. (c) Find the chained (geometric mean) growth. (d) Explain the gap.

<details class="solution" markdown>
<summary>Solution</summary>

Nominal: year 1 is $100 \times 10 + 50 \times 20 = 2000$, and year 2 is $90 \times 15 + 70 \times 18 = 1350 + 1260 = 2610$.

(a) Year 2 at year-1 prices: $90 \times 10 + 70 \times 20 = 900 + 1400 = 2300$, so real growth is $\frac{2300}{2000} - 1 = 15.0\%$.

(b) Year 1 at year-2 prices: $100 \times 15 + 50 \times 18 = 1500 + 900 = 2400$, so real growth is $\frac{2610}{2400} - 1 = 8.75\%$.

(c) $\sqrt{1.15 \times 1.0875} - 1 = 11.8\%$.

(d) Good A's price rose 50% and its quantity fell, while B's price fell 10% and its quantity rose. Year-1 prices put a high weight on B (relatively expensive then) and so reward its growth, while year-2 prices put a high weight on A, whose output fell. When relative prices and quantities move in opposite directions, the base year matters a lot, and chaining averages the two.

Check: nominal growth $\frac{2610}{2000} - 1 = 30.5\%$ equals $1.15 \times \frac{2610}{2300} - 1$.

</details>

8\. (Reviews [index numbers](04-index-numbers.md).) Show that the GDP deflator in Problem 4 equals the Paasche price index of cars and haircuts between year 1 and year 2.

<details class="solution" markdown>
<summary>Solution</summary>

The Paasche index uses year-2 quantities in both the numerator and the denominator: $100 \times \frac{12 \times 21000 + 1100 \times 44}{12 \times 20000 + 1100 \times 40} = 100 \times \frac{300{,}400}{284{,}000} = 105.77$.

The deflator was $100 \times \frac{\text{nominal}}{\text{real}}$ with nominal 300,400 and real 284,000, which is the same fraction.

Check: both equal 105.77.

</details>

## Where this shows up

- [CPI and inflation](07-cpi-and-inflation.md) measures the price side from a household basket, and [unemployment rate and labour statistics](08-unemployment-rate-and-labour-statistics.md) finishes the chapter. [Multipliers and the AD-AS model](../04-more-tools/02-multipliers-and-the-ad-as-model.md) uses real GDP on one axis and the price level on the other.
- In finance, real returns are nominal returns divided by the inflation factor, the same identity: inflation and real returns<!-- link: ../../08-financial-math/02-interest-and-growth/06-inflation-and-real-returns.md -->.
- Any time you compare money across years, whether salaries, tuition or a dataset's revenue column, you are choosing a deflator.
