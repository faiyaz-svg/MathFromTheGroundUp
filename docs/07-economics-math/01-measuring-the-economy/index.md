# Measuring the economy

Reading economics graphs, comparing rates and index numbers, and the arithmetic behind GDP, inflation and the labour statistics, with Canadian data.

1. [How economists use math and graphs](01-how-economists-use-math-and-graphs.md)
2. [Percent change vs percentage points](02-percent-change-vs-percentage-points.md)
3. [Growth rates and CAGR](03-growth-rates-and-cagr.md)
4. [Index numbers](04-index-numbers.md)
5. [GDP and the circular flow](05-gdp-and-the-circular-flow.md)
6. [Nominal vs real GDP and the deflator](06-nominal-vs-real-gdp-and-the-deflator.md)
7. [CPI and inflation](07-cpi-and-inflation.md)
8. [Unemployment rate and labour statistics](08-unemployment-rate-and-labour-statistics.md)

## Cheat sheet

### How economists use math and graphs

Economics graphs put price on the vertical axis (Marshall's convention), so a demand curve is the graph of the inverse function: from $Q = 100 - 2P$ get $P = 50 - \frac{Q}{2}$. The slope on the page is $\frac{\Delta P}{\Delta Q} = -0.5$, the reciprocal of the coefficient $-2$.

| Idea | Rule |
|---|---|
| Slope | rise over run, in units of the vertical variable per unit of the horizontal one |
| Ceteris paribus | change one variable, hold the others fixed |
| Move along a curve | the variable on an axis changes |
| Shift of a curve | something else in the equation changes |
| Stock | measured at a moment (balance, population) |
| Flow | measured over a period (income, GDP); $S_t = S_{t-1} + I_t - O_t$ |
| Log axis | equal distances mean equal ratios, so constant growth is a straight line |

Main mistakes: reading the equation's coefficient as the slope of the picture, treating a shift as a move along the curve, adding a stock to a flow, putting a series that crosses zero on a log axis, and reading correlation as causation.

### Percent change vs percentage points

For a rate going from $r_0$ to $r_1$: change in points is $r_1 - r_0$, and the relative change is $\frac{r_1 - r_0}{r_0}$. One percentage point is 100 basis points. The Bank of Canada's cut from 2.50% to 2.25% is $-0.25$ points, $-25$ bps and $-10\%$ relative.

- Points add. Percent changes multiply: up 10% then down 10% is $1.10 \times 0.90 = 0.99$.
- Average percent changes with the geometric mean, not the plain mean: $+50\%$ and $-50\%$ end 25% lower.
- Pool rates with weights: 7% of 8 million and 5% of 2 million is $\frac{0.56 + 0.10}{10} = 6.6\%$.
- Dollar effect of a rate change on a balance: balance times the change as a decimal (25 bps on \$400,000 is \$1,000 a year).

Main mistakes: "up 1%" for 1 point, averaging rates without weights, adding successive percent changes, and quoting the relative change when the points change is meant.

### Growth rates and CAGR

| Task | Formula |
|---|---|
| Growth rate | $g = \frac{x_t}{x_{t-1}} - 1$ |
| Annualize (compounded) | $(1 + g)^k - 1$, with $k = 12$ for months and $k = 4$ for quarters |
| CAGR | $\left(\frac{x_n}{x_0}\right)^{1/n} - 1 = e^{\ln(x_n/x_0)/n} - 1$ |
| Log difference | $\ln x_t - \ln x_{t-1} = \ln(1 + g)$, close to $g$ for small $g$ |
| Doubling time | $\frac{\ln 2}{\ln(1 + g)}$, about $\frac{70}{R}$ at $R\%$ per period |
| Product | $g_{xy} = g_x + g_y + g_x g_y \approx g_x + g_y$ |
| Ratio | $g_{x/y} \approx g_x - g_y$, exactly $\frac{1 + g_x}{1 + g_y} - 1$ |

- The CPI went from 136.2 (September 2019) to 170.0 (September 2026), a CAGR of 3.22% over $n = 7$ years.
- Log differences add exactly over time (a telescoping sum). Percent changes do not.
- Use 70 for rates below about 4% and 72 near 8%.

Main mistakes: dividing total growth by the number of years, using the number of data points for $n$ instead of the number of years, averaging yearly rates, and treating one annualized month as the year's inflation.

### Index numbers

$I_t = 100 \times \frac{x_t}{x_0}$. Rebase by dividing by the new base value and multiplying by 100; ratios don't change. Splice with a link factor: old value at the overlap times the new index over 100.

| Index | Formula | Weights |
|---|---|---|
| Laspeyres | $100 \times \frac{\sum p_1 q_0}{\sum p_0 q_0}$ | base-period quantities |
| Paasche | $100 \times \frac{\sum p_1 q_1}{\sum p_0 q_1}$ | current quantities |
| Fisher | $\sqrt{L \times P}$ | geometric mean of the two |

- Laspeyres tends to be above Paasche because buyers substitute away from goods whose prices rise (substitution bias), but this is not a theorem.
- Real value is nominal divided by the index over 100. To restate an old amount in new dollars, multiply by the later index over the earlier one.

Main mistakes: reading index points as percent (170.0 from 136.2 is 24.8%, not 33.8%), comparing indexes on different bases, and thinking a higher index for one city means higher prices there.

### GDP and the circular flow

GDP is the market value of final goods and services produced within the borders in a period. Three ways, one answer:

- Expenditure: $Y = C + I + G + (X - M)$.
- Income: compensation of employees, gross operating surplus, gross mixed income, and taxes less subsidies.
- Value added: sales minus intermediate purchases, summed over firms (it telescopes to the final sale).

Canada in 2025 (Statistics Canada, Table 36-10-0104-01, current prices): GDP \$3,245,257 million, with $C$ 55.8%, $G$ 26.1%, $I$ 19.0% and net exports $-0.9\%$ of GDP. GDP per person was about \$77,994.

Left out of GDP: unpaid work, underground activity, leisure, environmental damage, distribution, used goods, financial trades and transfers.

Main mistakes: adding all sales (double counting), putting transfers in $G$, forgetting to subtract imports, and treating buying shares as investment.

### Nominal vs real GDP and the deflator

Nominal GDP is $\sum p_t q_t$ and real GDP is $\sum p_b q_t$ at base-year prices. The deflator is $100 \times \frac{\text{nominal}}{\text{real}}$, a Paasche price index.

$$
1 + g_N = (1 + g_R)(1 + \pi), \qquad g_R = \frac{1 + g_N}{1 + \pi} - 1 \approx g_N - \pi.
$$

- Canada 2025: nominal $+4.40\%$, real $+1.85\%$, deflator $+2.50\%$ (chained 2017 dollars, from the table above).
- Real GDP per person grows about as fast as real GDP minus population: $\frac{1.0185}{1.0108} - 1 = 0.76\%$.
- Chained real components do not add to real GDP exactly, and the base year changes levels more than growth rates.

Main mistakes: reading nominal growth as output growth, treating "2017 dollars" as money in 2017, and adding chained components.

### CPI and inflation

Inflation is $\frac{\text{CPI}_t}{\text{CPI}_{t-12}} - 1$ for year over year (September 2026: $\frac{170.0}{164.9} - 1 = 3.1\%$), and $\frac{\text{CPI}_t}{\text{CPI}_{t-1}} - 1$ for month over month. To restate an amount in today's dollars, multiply by $\frac{\text{CPI}_{\text{now}}}{\text{CPI}_{\text{then}}}$.

- Contribution of a category to inflation is its weight times its price change. Gasoline in September 2026: $0.0401 \times 27.8 \approx 1.1$ points.
- Core measures (CPI-trim 1.8% and CPI-median 1.9% in September 2026) reduce the effect of extreme components.
- The Bank of Canada targets 2%, the midpoint of a 1% to 3% control range, on the year-over-year total CPI.
- The CPI can overstate the cost-of-living change through substitution, and it misses quality changes and new goods.

Main mistakes: reading a CPI of 170.0 as 170% inflation, quoting one annualized month as the year, thinking falling inflation means falling prices, and multiplying the wrong way when adjusting for inflation.

### Unemployment rate and labour statistics

$L = E + U$, $u = \frac{U}{L}$, $p = \frac{L}{N}$, $e = \frac{E}{N}$, and $e = p(1 - u)$, so $u = 1 - \frac{e}{p}$. A fall in the number of unemployed is $\Delta U = \Delta L - \Delta E$.

- Unemployed means without work, available, and either searching in the past four weeks, on temporary layoff or about to start a job. Discouraged searchers are not in the labour force.
- Canada, September 2026 (Table 14-10-0287-01, seasonally adjusted): $u = 6.5\%$, $p = 64.8\%$, $e = 60.6\%$. Ontario: $u = 7.0\%$, $p = 64.6\%$, $e = 60.1\%$.
- Canada's rate fell from 7.1% to 6.5% in a year with participation down and the employment rate flat. With participation held at its 2025 level, the rate would have been about 7.1%.
- Steady state with separation rate $s$ and job-finding rate $f$: $u^* = \frac{s}{s + f}$.

Main mistakes: dividing by the population instead of the labour force, counting every non-worker as unemployed, and reading a falling unemployment rate as more people working.
