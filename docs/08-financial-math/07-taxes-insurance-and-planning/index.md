# Taxes, insurance and planning

How Canadian and Ontario income tax is built from brackets and credits, insurance as an expected-value problem, and the spreadsheet functions and five-year plan that tie the finance chapters together.

1. [Income tax brackets: marginal vs effective](01-income-tax-brackets-marginal-vs-effective.md)
2. [Insurance and expected value](02-insurance-and-expected-value.md)
3. [Spreadsheet finance functions and a capstone plan](03-spreadsheet-finance-functions-and-capstone.md)

## Cheat sheet

Tax figures are the 2026 values from the sources linked in the first lesson and change every year. Probabilities, prices, premiums and rates in the examples are made up.

### Income tax brackets: marginal vs effective

The tax on taxable income $x$ is the sum of slices, with rates $r_1 < \cdots < r_n$ and limits $b_k$:

$$
T(x) = \sum_{k=1}^{n} r_k \max\bigl(0,\ \min(x, b_k) - b_{k-1}\bigr).
$$

$T$ is continuous and piecewise linear with slope $r_k$ on bracket $k$, so after-tax income $x - T(x)$ always rises with $x$.

| Quantity | Meaning | At \$65,000 in Ontario |
|---|---|---|
| Marginal rate | rate on the next dollar of taxable income | $20.5\% + 9.15\% = 29.65\%$ |
| Effective rate | total tax divided by income | \$9,725.50, about 15.0% |
| Take-home pay | income minus tax, CPP and EI | \$50,555.75 |

Steps for an employee:

1. CPP is 5.95% of earnings from \$3,500 to \$74,600 (4.95 points base, a credit; 1 point enhanced, a deduction). Second CPP is 4% from \$74,600 to \$85,000 (a deduction). EI is 1.63% up to \$68,900 (a credit).
2. Taxable income is income minus enhanced CPP, second CPP and deductions such as an RRSP contribution.
3. Federal tax is the slices at 14%, 20.5%, 26%, 29% and 33% (limits \$58,523, \$117,045, \$181,440, \$258,482), minus credits of (\$16,452 + \$1,501 + base CPP + EI) $\times$ 14%, and not below 0.
4. Ontario tax is the slices at 5.05%, 9.15%, 11.16%, 12.16% and 13.16% (limits \$53,891, \$107,785, \$150,000, \$220,000), minus credits of (\$12,989 + base CPP + EI) $\times$ 5.05%.
5. Surtax is 20% of Ontario tax over \$5,818 plus 36% of the part over \$7,446. The Health Premium is up to \$600 at \$48,000 to \$72,000 and up to \$900 above \$200,600.
6. Total tax is federal plus Ontario plus surtax plus premium.

A deduction of $d$ saves the sum of the bracket rates over the slices it removes, which is $r\,d$ when it stays in one bracket. A credit saves its amount times the lowest rate. An RRSP deduction of \$5,000 at \$65,000 saves $0.2965 \times 5000 = \$1{,}482.50$.

Main mistakes:

- Taxing all income at the top bracket's rate.
- Confusing marginal with effective, or a credit with a deduction.
- Believing a raise can lower take-home pay. Brackets can't do that. Benefits with a hard income limit can.
- Adding bracket rates when the surtax applies: the Ontario rate is multiplied by 1.2, then by 1.56.
- Letting a non-refundable credit make the tax negative.

### Insurance and expected value

| Quantity | Formula | Example |
|---|---|---|
| Expected loss | $E[L] = \sum \ell\,p(\ell)$ | 8% of \$900 is \$72 |
| Loading | $\lambda = \frac{P - E}{E}$ | \$110 against \$72 is 52.8% |
| Loss ratio | $\frac{E}{P}$, and $\lambda = \frac{1}{\text{loss ratio}} - 1$ | 65.5% |
| Payout with deductible $D$ | $\max(L - D, 0)$ | expected payout falls as $D$ rises |
| Expected total cost | $E[L] + \lambda\,E[\max(L - D, 0)]$ | \$343 at $D = 0$, \$293 at $D = 2000$ |
| Warranty break-even probability | price $\div$ repair cost | \$180 over \$600 is 30% |
| Term life need | PV of income + debts $-$ assets | 15 years of \$50,000 at 3%: \$596,896.75 |

An insurer with $n$ independent policies has mean profit $n(P - E)$ and standard deviation $s\sqrt{n}$, so its risk per policy shrinks like $\frac{1}{\sqrt{n}}$. A risk-averse person (strictly concave utility) strictly prefers full insurance at the fair premium. With $u(w) = \ln w$, wealth \$60,000 and a 5% chance of a \$20,000 loss, the most they would pay is \$1,204.15 against an expected loss of \$1,000.

Main mistakes:

- Treating "negative expected value" as "never buy". Large losses you can't absorb are worth a loading. Small ones aren't.
- Comparing premiums without comparing deductibles and the bill in a bad year.
- Forgetting that the probabilities are group estimates, and that disasters hit many policies at once.

### Spreadsheet finance functions and a capstone plan

Money you receive is positive and money you pay is negative. Every function solves one equation:

$$
P\,(1+i)^n + A\,\frac{(1+i)^n - 1}{i} + F = 0.
$$

| Function | Finds | Example |
|---|---|---|
| `PMT(rate, nper, pv, fv, type)` | payment | `=PMT(0.072/12,60,18000)` is $-358.12$ |
| `FV(rate, nper, pmt, pv, type)` | future value | `=FV(0.04,5,-5600)` is \$30,331.41 |
| `PV(rate, nper, pmt, fv, type)` | present value | `=PV(0.05,10,-1000)` is \$7,721.73 |
| `NPER(rate, pmt, pv, fv, type)` | number of periods | `=NPER(0.005,-300,10000)` is 36.56 |
| `RATE(nper, pmt, pv, fv, type)` | rate per period | solved by search |
| `NPV(rate, values)` | PV of flows from period 1 | `=C0 + NPV(rate, C1:Cn)` |
| `IRR(values)` | rate with NPV 0 | 8.90% for $-1000, 300, 400, 500$ |
| `EFFECT(nominal, m)` | effective annual rate | `=EFFECT(0.06,12)` is 6.168% |
| `NOMINAL(effect, m)` | nominal annual rate | inverse of `EFFECT` |

Use rate per period and number of periods in the same unit (`rate/12` with months). Type 1 (annuity due) multiplies a future value by $(1+i)$ and divides a payment by it. `NPV` discounts its first value one period, so keep a cash flow from today outside it. `IRR` can have two answers when the signs change twice.

The capstone: take-home pay from the tax calculator, OSAP repayment (a PMT after a six-month grace period), an emergency fund of three months of costs, a home goal of \$30,000 by `PMT` (\$5,538.81 a year at 4%), an FHSA for the home goal, a TFSA for the rest, and a car decision compared by NPV of costs (\$28,651 at 4%).

Main mistakes:

- Sign errors: loan and payments need opposite signs.
- Using the yearly rate with a monthly count.
- Using `NPV` with the first cash flow inside it.
- Comparing the TFSA and RRSP without comparing the tax rate now with the rate at withdrawal. They are equal when the two rates are equal.
