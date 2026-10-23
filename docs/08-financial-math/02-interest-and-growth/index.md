# Interest and growth

How money grows: simple and compound interest, effective annual rates, continuous compounding, doubling times, and what inflation does to the result.

1. [Simple interest](01-simple-interest.md)
2. [Compound interest](02-compound-interest.md)
3. [APR, APY and the effective annual rate](03-apr-apy-and-effective-annual-rate.md)
4. [Continuous compounding and e](04-continuous-compounding-and-e.md)
5. [Doubling time, the rule of 72 and logs](05-doubling-time-rule-of-72-and-logs.md)
6. [Inflation and real returns](06-inflation-and-real-returns.md)

## Cheat sheet

### Simple interest

Interest on the principal only, so equal steps of time add equal dollars. Rates go in as decimals and time in years.

| Unknown | Formula |
|---|---|
| interest $I$ | $I = Prt$ |
| principal $P$ | $P = \dfrac{I}{rt}$ |
| rate $r$ | $r = \dfrac{I}{Pt}$ |
| time $t$ | $t = \dfrac{I}{Pr}$ |
| amount $A$ | $A = P + I = P(1 + rt)$ |

- Months: $t = \frac{\text{months}}{12}$. Days: $t = \frac{\text{days}}{365}$ (actual/365). Conventions vary (360, 366), so read the agreement.
- $A(t) = P + Prt$ is a line with intercept $P$ and slope $Pr$.
- If the rate changes, split the loan into pieces, find each $I$ and add.

Main mistakes:

- Using months as years, or a rate of 4 instead of 0.04.
- Reading the interest over 9 months as a yearly rate. Divide by the time in years.
- Rounding the time (90/365) before multiplying.

### Compound interest

$$
A = P\left(1 + \frac{r}{n}\right)^{nt}
$$

with $n$ periods a year and $nt$ periods in all. Each period multiplies by $1 + \frac{r}{n}$.

| Unknown | Formula |
|---|---|
| $P$ | $\dfrac{A}{(1 + r/n)^{nt}}$ |
| $r$ | $n\left(\left(\dfrac{A}{P}\right)^{1/(nt)} - 1\right)$ |
| $t$ | $\dfrac{\ln(A/P)}{n\ln(1 + r/n)}$ |

- \$1,000 at 5% for 10 years: simple \$1,500, annual \$1,628.89, monthly \$1,647.01, daily \$1,648.66, continuous \$1,648.72.
- Check the answer lies between the simple and continuous values. Keep all digits of the factor and round the money at the end.

Main mistakes:

- Using the whole rate each period instead of $\frac{r}{n}$.
- Forgetting to multiply the exponent by $n$.
- Reading $\frac{\ln(A/P)}{\ln(1 + r/n)}$ as years. It is periods, so divide by $n$.

### APR, APY and the effective annual rate

$$
r_{\text{eff}} = \left(1 + \frac{r}{n}\right)^n - 1
$$

Compare deposits and loans by EAR. APY is the deposit name for the same number. A loan's APR also folds in some fees, and the lender's disclosure governs which.

- Equivalent rates: $r_2 = n_2\left(\left(1 + \frac{r_1}{n_1}\right)^{n_1/n_2} - 1\right)$.
- Nominal 5% by frequency: 5.0000%, 5.0625% (semi-annual), 5.0945%, 5.1162% (monthly), 5.1267% (daily).
- A 5% fixed Canadian mortgage (semi-annual) has EAR 5.0625% and monthly equivalent 4.9487%.
- Fees: \$2,000 for a year at 6% with a \$40 fee taken from the loan costs $\frac{160}{1960} = 8.16\%$.

Main mistakes:

- Comparing nominal rates with different compounding.
- Halving an EAR to get a semi-annual rate.
- Treating an APR as the whole cost of a loan.

### Continuous compounding and e

$$
\lim_{n \to \infty}\left(1 + \frac{r}{n}\right)^n = e^r, \qquad A = Pe^{rt}.
$$

| Conversion | Formula |
|---|---|
| continuous rate from EAR | $\delta = \ln(1 + r_{\text{eff}})$ |
| EAR from continuous rate | $r_{\text{eff}} = e^{\delta} - 1$ |
| time | $t = \dfrac{\ln(A/P)}{r}$ |

- Proof idea: $n\ln(1 + \frac{r}{n}) \to r$ because it is a difference quotient of $\ln$ at 1.
- Shortfall of $n$-times compounding from continuous: about $\frac{r^2t}{2n}$ of the amount.
- Continuous rates add across periods, percent changes don't: $+10\%$ then $-10\%$ is $-1\%$.

Main mistakes:

- Treating $e^r$ as $1 + r$.
- Using base-10 `log` where $\ln$ is needed.

### Doubling time, the rule of 72 and logs

$$
T_d = \frac{\ln 2}{\ln(1 + r)}, \qquad T_F = \frac{\ln F}{\ln(1 + r)}
$$

| Rate $R\%$ | 2 | 4 | 6 | 8 | 12 | 20 |
|---|---|---|---|---|---|---|
| exact $T_d$ | 35.00 | 17.67 | 11.90 | 9.01 | 6.12 | 3.80 |
| $72 \div R$ | 36.00 | 18.00 | 12.00 | 9.00 | 6.00 | 3.60 |

- $R \cdot T_d \approx 69.31\left(1 + \frac{r}{2} - \frac{r^2}{12}\right)$, so 72 fits best near 8%, 70 near 2%, 69.3 for continuous rates.
- Tripling: 114 over $R$. Quadrupling: 144 over $R$.
- Rate to double in $t$ periods: $2^{1/t} - 1$.
- At 2% inflation prices double in 35.0 years, at 3% in 23.45 years.

Main mistakes:

- Using $r = 0.06$ in $\frac{72}{R}$.
- Mixing months and years.
- Trusting the rule above about 20%.

### Inflation and real returns

$$
1 + i = (1 + \rho)(1 + \pi), \qquad \rho = \frac{1 + i}{1 + \pi} - 1 \approx i - \pi.
$$

- The approximation overstates $\rho$ by $\rho\pi$.
- Real value of $A$ after $t$ years: $\dfrac{A}{(1 + \pi)^t}$, or $A \cdot \frac{C_0}{C_1}$ with a CPI.
- Bank of Canada target: 2%, midpoint of a 1% to 3% range (agreement to the end of 2026).
- After-tax real return: $\dfrac{1 + i(1 - \tau)}{1 + \pi} - 1$. At 4%, 2% inflation and a 30% tax rate it is 0.784%, against 1.961% in a TFSA.

Main mistakes:

- Subtracting when rates are large (20% less 15% is 4.35%, not 5%).
- Multiplying instead of dividing by the price factor to find real value.
- Comparing a real figure with a nominal one.
