# Investing and retirement

Returns, risk and fees, the timing of investing, and the Canadian registered accounts and pensions you will use to save for retirement.

1. [Investing returns and risk](01-investing-returns-and-risk.md)
2. [Index funds, fees and dollar-cost averaging](02-index-funds-fees-and-dollar-cost-averaging.md)
3. [Retirement accounts: RRSP, TFSA and FHSA](03-retirement-accounts.md)

## Cheat sheet

### Investing returns and risk

| Quantity | Formula | Example |
|---|---|---|
| Holding-period return | $R = \frac{V_1 - V_0 + I}{V_0}$ | \$2,000 to \$2,260 plus \$40 income: $R = 15\%$ |
| Annualized return | $(1 + R)^{1/n} - 1$ | 15% over 2 years is $1.15^{1/2} - 1 \approx 7.24\%$ a year |
| Arithmetic mean | $\bar{r} = \frac{r_1 + \cdots + r_n}{n}$ | $+30\%$ and $-10\%$ give 10% |
| Geometric mean | $g = \left[\prod (1 + r_i)\right]^{1/n} - 1$ | $\sqrt{1.3 \times 0.9} - 1 \approx 8.17\%$ |
| Volatility | sample standard deviation $s$ of the returns | monthly 5% gives $5\% \times \sqrt{12} \approx 17.3\%$ a year |
| Volatility drag | $g \approx \bar{r} - \frac{\sigma^2}{2}$ | 20% volatility costs about 2 points a year |
| Gain needed after a loss $x$ | $\frac{x}{1 - x}$ | after $-20\%$ you need $+25\%$ |

- Arithmetic mean at least geometric mean: $\frac{a + b}{2} \ge \sqrt{ab}$, because $\frac{(\sqrt{a} - \sqrt{b})^2}{2} \ge 0$. So $g \le \bar{r}$, with equality only when all returns are equal.
- For two years, $(1 + r_1)(1 + r_2) = (1 + m)^2 - d^2$, with $m$ the mean and $d$ half the gap between the returns.
- Two assets with weight $w$ in A: the mean is $w\mu_A + (1 - w)\mu_B$ and $\sigma_p^2 = w^2\sigma_A^2 + (1 - w)^2\sigma_B^2 + 2w(1 - w)\rho\sigma_A\sigma_B$. At $\rho = 1$ the volatility is the weighted average of the two. Lower $\rho$ gives lower volatility for the same expected return.
- The same average return gives a wide spread of outcomes, and the median path ends below the mean (made-up 7% mean and 15% volatility, 30 years: median \$57,081 and mean \$76,252 from \$10,000).

Main mistakes:

- Treating an average return as the growth rate you earned. Ask whether it is arithmetic or geometric.
- Adding gains and losses: $-30\%$ then $+30\%$ is a 9% loss.
- Using the drag formula for big swings, where it misses by a point or more.
- Equating volatility with the chance of losing money.

### Index funds, fees and dollar-cost averaging

| Idea | Rule | Example |
|---|---|---|
| Index fund | holds an index's investments in its proportions | follows the index minus fees |
| ETF | a fund bought and sold like a share | a way to buy, not a kind of investment |
| MER | yearly cost as a percent of assets, already out of the return | 0.85% on \$34,000 is \$289 a year |
| Net return | about $g - m$ | 6% gross, 1.5% MER: 4.5% |
| Balance after $n$ years | $V_0(1 + g - m)^n$ | \$10,000 for 30 years: \$54,271 at 0.2%, \$37,453 at 1.5% |
| Share lost to a higher fee | $1 - \left(\frac{1 + g - m_1}{1 + g - m_2}\right)^n$ | 31.0% over 30 years, 11.6% over 10 |

- Regular contributions of $P$ a year: $V = P\cdot\frac{(1 + r)^n - 1}{r}$ with $r$ the net return. \$3,600 a year for 30 years at 5.8% against 4.5% is \$274,787 against \$219,625.
- Dollar-cost averaging: a fixed amount per period buys at the harmonic mean $H = \frac{n}{\sum 1/p_i}$ of the prices, and $H \le$ the plain average. Prices \$20 and \$40 give $\frac{2 \times 20 \times 40}{60} = 26.67$ against 30. For two prices, $H = \frac{2ab}{a + b}$, and $H \le \sqrt{ab} \le \frac{a + b}{2}$.
- Lump sum against DCA, in the made-up model with a positive expected return: the lump sum has the higher average and wins in about 60% of paths, and DCA has the smaller spread.
- Rebalancing: sell what grew, buy what lagged, to restore the target split. It controls risk and does not raise returns.

Main mistakes:

- Calling a small yearly fee a small cost. It compounds: 1.3 points of fee cost 31% of the final balance.
- Thinking an average cost below the average price means a profit, or that DCA beats a lump sum.
- Comparing funds by MER alone when they hold different things.

### Retirement accounts: RRSP, TFSA and FHSA

| Account | 2026 figures | Tax treatment |
|---|---|---|
| TFSA | limit \$7,000, cumulative room \$109,000 since 2009 (summed from the CRA table) | no deduction, growth and withdrawals tax-free |
| RRSP | 18% of last year's earned income, up to \$33,810 | deduction now, withdrawals taxed |
| FHSA | \$8,000 a year, carry-forward up to \$8,000, \$40,000 lifetime | deduction now, qualifying withdrawals tax-free |

These are 2026 figures, and they change every year; the lesson links the CRA pages.

- TFSA withdrawals are added back to room on January 1 of the next year. Over-contributions are taxed at 1% a month. RRSP deduction deadline for a tax year: 60 days after year end (March 2, 2026 for 2025). The RRSP over-contribution cushion is \$2,000.
- Same rate at contribution and withdrawal: the TFSA and the RRSP both end at $P(1 - t)(1 + r)^n$. Different rates: RRSP divided by TFSA is $\frac{1 - t_w}{1 - t_c}$. Higher rate now favours the RRSP, higher rate later favours the TFSA.
- An employer match of $m$ is an immediate return of $m$. A 50% match is a 50% return on the day it is paid.
- 4% rule (a rule of thumb from US studies, no guarantee): the portfolio needed is $\frac{\text{spending}}{0.04} = 25 \times \text{spending}$. A level real withdrawal fraction over $n$ years is $\frac{r}{1 - (1 + r)^{-n}}$, which is 4% over 30 years at a real return of about 1.22%.
- CPP: 0.6% less per month before 65 (36% at 60), 0.7% more per month after 65 (42% at 70). Break-even age (no interest): $T = \frac{b_2a_2 - b_1a_1}{b_2 - b_1}$, about 73.9 for 60 against 65 and 81.9 for 65 against 70 in the lesson's example.
- RRIF minimum: balance times $\frac{1}{90 - \text{age}}$ up to 70, then 5.28% at 71, 5.40% at 72 and 5.53% at 73. An RRSP must mature by the end of the year you turn 71.

Main mistakes:

- Comparing an RRSP balance with a TFSA balance before tax.
- Re-contributing a TFSA withdrawal in the same year without spare room.
- Reading the RRSP refund as free money: the tax comes back at withdrawal.
- Treating the 4% rule or a CPP break-even age as a guarantee.
