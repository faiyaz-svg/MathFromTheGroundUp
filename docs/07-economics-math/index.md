# Economics math

The math behind introductory economics. Measuring the economy, markets, firms and consumers, present value, regression and game theory, with Canadian data.

Before this folder: High school, plus derivatives and Lagrange multipliers from the university core for chapter 3.


## How to use this folder

Take the [diagnostic](diagnostic.md) first, with a calculator but without notes. It asks two questions on each of the 22 lessons, 44 in all, and its answer table names the lesson to study for each one you miss, so you can do only those lessons and skip the rest. Then work through the four chapters in order if you are taking intro micro, intro macro or econometrics, because each chapter only needs the ones before it. Chapter 3 also needs derivatives and Lagrange multipliers from the [university core](../05-university-core/index.md). Each chapter has its own cheat sheet (the links are below), and each lesson starts with a quick check, so you can test yourself before reading it. Dollar figures and rates are Canadian.

The [Anki deck for this folder](../downloads/anki/07-economics-math.apkg) holds the formulas for growth rates, index numbers, real and nominal values, equilibrium and surplus, elasticity, cost and profit rules, utility maximization, present value, the multiplier, regression readings and Nash equilibrium, plus the pairs that are easy to confuse, such as percent change and percentage points, a shift and a move along a curve, and a Laspeyres and a Paasche index. In Anki desktop choose File, then Import, and [Anki decks](../00-start-here/index.md#anki-decks) covers phones.

## Fast path for a CS student with an economics minor

If you are short on time, these lessons carry the most weight in intro micro, intro macro and econometrics. They are listed in reading order.

| Lesson | Where it comes back |
|---|---|
| [Percent change vs percentage points](01-measuring-the-economy/02-percent-change-vs-percentage-points.md) | every news story about interest rates, unemployment and inflation |
| [Growth rates and CAGR](01-measuring-the-economy/03-growth-rates-and-cagr.md) | macro growth questions, and log differences in econometrics |
| [Nominal vs real GDP and the deflator](01-measuring-the-economy/06-nominal-vs-real-gdp-and-the-deflator.md) | the first macro midterm |
| [CPI and inflation](01-measuring-the-economy/07-cpi-and-inflation.md) | real values, and the Bank of Canada's 2% target |
| [Supply and demand equilibrium algebra](02-markets/03-supply-and-demand-equilibrium-algebra.md) | the standard micro problem, in every course |
| [Surplus and market interventions](02-markets/04-surplus-and-market-interventions.md) | taxes, price controls and deadweight loss |
| [Elasticity](02-markets/05-elasticity.md) | revenue questions, and the log-log slope in regression |
| [Marginal analysis with derivatives](03-firms-and-consumers/01-marginal-analysis-with-derivatives.md) | $MR = MC$ in every later micro topic |
| [Profit maximization and market structure](03-firms-and-consumers/03-profit-maximization-and-market-structure.md) | competition, monopoly and Cournot |
| [Utility and indifference curves](03-firms-and-consumers/04-utility-and-indifference-curves.md) | consumer choice in intermediate micro |
| [Lagrange multipliers, utility and cost minimization](03-firms-and-consumers/05-lagrange-multipliers-utility-and-cost-minimization.md) | demand functions and cost minimization |
| [Present value, NPV and bond prices](04-more-tools/01-present-value-npv-and-bond-prices.md) | finance, and [time value of money](../08-financial-math/03-time-value-of-money/index.md) |
| [Multipliers and the AD-AS model](04-more-tools/02-multipliers-and-the-ad-as-model.md) | the Keynesian cross in intro macro |
| [Regression and econometrics intuition](04-more-tools/03-regression-and-econometrics-intuition.md) | reading a regression table, and omitted variable bias |
| [Game theory and Nash equilibrium](04-more-tools/04-game-theory-and-nash-equilibrium.md) | strategy questions in micro and in algorithmic game theory |

The lessons not in the table can wait. Come back to comparative advantage before a trade unit, to index numbers and the labour statistics when a macro course reaches them, and to production and cost functions before the cost curves of a firm.

## Cheat sheet

Each chapter has a cheat sheet with the rules, tables and common mistakes of its lessons. This is the map.

- [Measuring the economy](01-measuring-the-economy/index.md#cheat-sheet) covers percent change against points, growth rates and CAGR, index numbers, the three ways to measure GDP, the deflator, CPI and the labour statistics.
- [Markets](02-markets/index.md#cheat-sheet) covers opportunity cost, comparative advantage, equilibrium algebra, surplus, taxes and price controls, and elasticity.
- [Firms and consumers](03-firms-and-consumers/index.md#cheat-sheet) covers marginal analysis, production and cost, profit maximization by market type, utility, and Lagrange multipliers.
- [More tools](04-more-tools/index.md#cheat-sheet) covers present value and bonds, the multiplier and AD-AS, regression readings and omitted variable bias, and Nash equilibrium.

The results used most often are below in short form.

| Topic | The result to keep |
|---|---|
| growth and CAGR | $g = \frac{x_t}{x_{t-1}} - 1$, and $\left(\frac{x_n}{x_0}\right)^{1/n} - 1$ |
| real growth | $1 + g_N = (1 + g_R)(1 + \pi)$ |
| inflation | $\frac{\text{CPI}_t}{\text{CPI}_{t-12}} - 1$ |
| equilibrium | $P^* = \frac{d_0 - s_0}{d_1 + s_1}$ for $Q_d = d_0 - d_1P$, $Q_s = s_0 + s_1P$ |
| elasticity | $E = \frac{dQ}{dP}\cdot\frac{P}{Q}$, and $\text{MR} = P\left(1 + \frac{1}{E}\right)$ |
| profit rule | $MR = MC$ with $MC$ rising; a price taker has $p = MC$ |
| consumer optimum | $MRS = \frac{p_x}{p_y}$ on the budget line |
| present value | $\frac{C}{(1 + r)^t}$, and $\frac{C}{r}$ for a perpetuity |
| multiplier | $\frac{1}{1 - b}$ for spending, $-\frac{b}{1 - b}$ for a lump-sum tax |
| regression | log-log slope is an elasticity; omitted variable bias is $\beta_2\delta_1$ |
| Nash equilibrium | each strategy is a best response to the others |

<!-- lessons:start -->
## Lessons

### 1. [Measuring the economy](01-measuring-the-economy/index.md)

1. [How economists use math and graphs](01-measuring-the-economy/01-how-economists-use-math-and-graphs.md)
2. [Percent change vs percentage points](01-measuring-the-economy/02-percent-change-vs-percentage-points.md)
3. [Growth rates and CAGR](01-measuring-the-economy/03-growth-rates-and-cagr.md)
4. [Index numbers](01-measuring-the-economy/04-index-numbers.md)
5. [GDP and the circular flow](01-measuring-the-economy/05-gdp-and-the-circular-flow.md)
6. [Nominal vs real GDP and the deflator](01-measuring-the-economy/06-nominal-vs-real-gdp-and-the-deflator.md)
7. [CPI and inflation](01-measuring-the-economy/07-cpi-and-inflation.md)
8. [Unemployment rate and labour statistics](01-measuring-the-economy/08-unemployment-rate-and-labour-statistics.md)

### 2. [Markets](02-markets/index.md)

1. [Opportunity cost and the PPC](02-markets/01-opportunity-cost-and-the-ppc.md)
2. [Comparative advantage and gains from trade](02-markets/02-comparative-advantage-and-gains-from-trade.md)
3. [Supply and demand equilibrium algebra](02-markets/03-supply-and-demand-equilibrium-algebra.md)
4. [Surplus and market interventions](02-markets/04-surplus-and-market-interventions.md)
5. [Elasticity](02-markets/05-elasticity.md)

### 3. [Firms and consumers](03-firms-and-consumers/index.md)

1. [Marginal analysis with derivatives](03-firms-and-consumers/01-marginal-analysis-with-derivatives.md)
2. [Production and cost functions](03-firms-and-consumers/02-production-and-cost-functions.md)
3. [Profit maximization and market structure](03-firms-and-consumers/03-profit-maximization-and-market-structure.md)
4. [Utility and indifference curves](03-firms-and-consumers/04-utility-and-indifference-curves.md)
5. [Lagrange multipliers, utility and cost minimization](03-firms-and-consumers/05-lagrange-multipliers-utility-and-cost-minimization.md)

### 4. [More tools](04-more-tools/index.md)

1. [Present value, NPV and bond prices](04-more-tools/01-present-value-npv-and-bond-prices.md)
2. [Multipliers and the AD-AS model](04-more-tools/02-multipliers-and-the-ad-as-model.md)
3. [Regression and econometrics intuition](04-more-tools/03-regression-and-econometrics-intuition.md)
4. [Game theory and Nash equilibrium](04-more-tools/04-game-theory-and-nash-equilibrium.md)

<!-- lessons:end -->
