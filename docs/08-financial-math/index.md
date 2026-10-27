# Financial math

Everyday money math, interest, loans, mortgages, investing, retirement accounts and income tax, using Canadian and Ontario rules.

Before this folder: Middle school percents and high school exponentials and logarithms. A few lessons use sums of geometric series.


## How to use this folder

Read the chapter cheat sheets first: [everyday money](01-everyday-money/index.md), [interest and growth](02-interest-and-growth/index.md), [time value of money](03-time-value-of-money/index.md), [borrowing](04-borrowing/index.md), [housing](05-housing/index.md), [investing and retirement](06-investing-and-retirement/index.md) and [taxes, insurance and planning](07-taxes-insurance-and-planning/index.md). Each lesson starts with a quick check, so you can test yourself and skip what you already know. Chapters 2 and 3 carry the formulas that every later chapter reuses, so do them in order.

Dollar limits, tax rates and premiums in this folder are the 2026 figures from the sources linked in each lesson. They change, usually every year, so check the linked page before you act on a number. The rates in the examples are made up. The formulas do not go out of date.

The [Anki deck for this folder](../downloads/anki/08-financial-math.apkg) holds the interest, annuity and amortization formulas, effective and real rates, the loan, mortgage and investing ideas, and the tax and insurance definitions. In Anki desktop choose File, then Import, and [Anki decks](../00-start-here/index.md#anki-decks) covers phones.

## Fast path

If you are a new grad starting work in Ontario, these lessons matter most for your first paycheque and the first few years after it. They are listed in reading order, so each one only needs the ones above it.

| Lesson | Why it matters |
|---|---|
| [Paycheques and budgeting](01-everyday-money/03-paycheques-and-budgeting.md) | gross against net pay, and what a first paycheque really is |
| [Compound interest](02-interest-and-growth/02-compound-interest.md) | the growth formula behind savings, debt and investing |
| [APR, APY and the effective annual rate](02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md) | comparing any two rates fairly |
| [Annuities and geometric series](03-time-value-of-money/02-annuities-and-geometric-series.md) | saving a fixed amount each month toward a goal |
| [The loan amortization formula](03-time-value-of-money/03-loan-amortization-formula.md) | the payment and interest on every loan |
| [Student loans](04-borrowing/01-student-loans.md) | OSAP repayment after the six-month grace period |
| [Credit cards and the minimum payment trap](04-borrowing/04-credit-cards-and-the-minimum-payment-trap.md) | why the minimum payment is not a plan |
| [Renting vs buying a home](05-housing/01-renting-vs-buying-a-home.md) | the real cost of a first apartment or a first home |
| [Mortgage basics](05-housing/02-mortgage-basics.md) | down payment, insurance and the stress test |
| [Canadian mortgage compounding](05-housing/04-canadian-mortgage-compounding.md) | why a Canadian fixed rate is not divided by 12 |
| [Retirement accounts: RRSP, TFSA and FHSA](06-investing-and-retirement/03-retirement-accounts.md) | where to put your first savings |
| [Index funds, fees and dollar-cost averaging](06-investing-and-retirement/02-index-funds-fees-and-dollar-cost-averaging.md) | what to buy inside those accounts, and what fees cost |
| [Income tax brackets: marginal vs effective](07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md) | what a raise or an RRSP deduction does to your tax |

## Cheat sheet

The formulas below are explained in the chapter cheat sheets linked above. Here $i$ is the rate per period and $n$ the number of periods.

| Idea | Formula |
|---|---|
| simple interest | $I = Prt$, $A = P(1 + rt)$ |
| compound interest | $A = P\left(1 + \frac{r}{n}\right)^{nt}$ |
| effective annual rate | $r_{\text{eff}} = \left(1 + \frac{r}{n}\right)^n - 1$ |
| continuous compounding | $A = Pe^{rt}$, $r_{\text{eff}} = e^{\delta} - 1$ |
| doubling time | $T_d = \frac{\ln 2}{\ln(1 + r)}$, about $\frac{72}{R}$ years at $R\%$ |
| real return | $\rho = \frac{1 + i}{1 + \pi} - 1 \approx i - \pi$ |
| future and present value | $\text{FV} = \text{PV}(1 + i)^n$, $\text{PV} = \text{FV}(1 + i)^{-n}$ |
| annuity future value | $\text{PMT}\,\frac{(1 + i)^n - 1}{i}$ |
| annuity present value | $\text{PMT}\,\frac{1 - (1 + i)^{-n}}{i}$ |
| loan payment | $\text{PMT} = \frac{\text{PV}\cdot i}{1 - (1 + i)^{-n}}$ |
| loan balance after $k$ payments | $\text{PMT}\,\frac{1 - (1 + i)^{-(n-k)}}{i}$ |
| total interest | $n\,\text{PMT} - \text{PV}$ |
| Canadian fixed mortgage, $p$ payments a year | $i_p = \left(1 + \frac{j}{2}\right)^{2/p} - 1$ |
| geometric mean return | $g = \left[\prod (1 + r_i)\right]^{1/n} - 1$, and $g \le \bar{r}$ |
| net of fees | balance $V_0(1 + g - m)^n$ |
| marginal tax | $T(x) = \sum r_k \max(0, \min(x, b_k) - b_{k-1})$ |
| expected loss and loading | $E[L] = \sum \ell\,p(\ell)$, $\lambda = \frac{P - E}{E}$ |

Key Canadian figures, as stated in the chapter cheat sheets:

- Ontario HST is 13%, made of 5% federal and 8% provincial, and is charged on the pre-tax price. Add it by multiplying by 1.13 and remove it by dividing by 1.13.
- The Canada Student Loan has had no federal interest since April 1, 2023. The Ontario part charges prime plus 1%.
- The Bank of Canada inflation target is 2%, the midpoint of a 1% to 3% range (agreement to the end of 2026).
- Minimum down payment: 5% up to \$500,000; 5% of the first \$500,000 plus 10% of the rest from \$500,000 up to \$1,500,000; 20% at \$1,500,000 or more. Under 20% down needs mortgage loan insurance (these are the 2026 values).
- Mortgage stress test: you qualify at the greater of the contract rate plus 2% and 5.25%. GDS is at most 39% and TDS at most 44% (2026 values).
- Ontario land transfer tax: 0.5% to \$55,000; 1.0% from \$55,000 to \$250,000; 1.5% from \$250,000 to \$400,000; 2.0% above \$400,000. First-time buyers get a refund of up to \$4,000 (2026 values).
- 2026 account figures: TFSA limit \$7,000; RRSP 18% of last year's earned income, up to \$33,810; FHSA \$8,000 a year and \$40,000 lifetime.
- 2026 payroll deductions: CPP is 5.95% of earnings from \$3,500 to \$74,600; second CPP is 4% from \$74,600 to \$85,000; EI is 1.63% up to \$68,900.
- Credit cards: a criminal interest rate is more than 35% APR (Criminal Code s. 347).

<!-- lessons:start -->
## Lessons

### 1. [Everyday money](01-everyday-money/index.md)

1. [Tips, discounts and HST](01-everyday-money/01-tips-discounts-and-hst.md)
2. [Unit price and comparison shopping](01-everyday-money/02-unit-price-and-comparison-shopping.md)
3. [Paycheques and budgeting](01-everyday-money/03-paycheques-and-budgeting.md)

### 2. [Interest and growth](02-interest-and-growth/index.md)

1. [Simple interest](02-interest-and-growth/01-simple-interest.md)
2. [Compound interest](02-interest-and-growth/02-compound-interest.md)
3. [APR, APY and the effective annual rate](02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md)
4. [Continuous compounding and e](02-interest-and-growth/04-continuous-compounding-and-e.md)
5. [Doubling time, the rule of 72 and logs](02-interest-and-growth/05-doubling-time-rule-of-72-and-logs.md)
6. [Inflation and real returns](02-interest-and-growth/06-inflation-and-real-returns.md)

### 3. [Time value of money](03-time-value-of-money/index.md)

1. [Present and future value](03-time-value-of-money/01-present-and-future-value.md)
2. [Annuities and geometric series](03-time-value-of-money/02-annuities-and-geometric-series.md)
3. [The loan amortization formula](03-time-value-of-money/03-loan-amortization-formula.md)

### 4. [Borrowing](04-borrowing/index.md)

1. [Student loans](04-borrowing/01-student-loans.md)
2. [Car loans and total cost](04-borrowing/02-car-loans-and-total-cost.md)
3. [Lease vs buy a car](04-borrowing/03-lease-vs-buy-a-car.md)
4. [Credit cards and the minimum payment trap](04-borrowing/04-credit-cards-and-the-minimum-payment-trap.md)
5. [Credit scores and paying off debt](04-borrowing/05-credit-scores-and-paying-off-debt.md)

### 5. [Housing](05-housing/index.md)

1. [Renting vs buying a home](05-housing/01-renting-vs-buying-a-home.md)
2. [Mortgage basics](05-housing/02-mortgage-basics.md)
3. [Mortgage amortization schedules](05-housing/03-mortgage-amortization-schedules.md)
4. [Canadian mortgage compounding](05-housing/04-canadian-mortgage-compounding.md)

### 6. [Investing and retirement](06-investing-and-retirement/index.md)

1. [Investing returns and risk](06-investing-and-retirement/01-investing-returns-and-risk.md)
2. [Index funds, fees and dollar-cost averaging](06-investing-and-retirement/02-index-funds-fees-and-dollar-cost-averaging.md)
3. [Retirement accounts: RRSP, TFSA and FHSA](06-investing-and-retirement/03-retirement-accounts.md)

### 7. [Taxes, insurance and planning](07-taxes-insurance-and-planning/index.md)

1. [Income tax brackets: marginal vs effective](07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md)
2. [Insurance and expected value](07-taxes-insurance-and-planning/02-insurance-and-expected-value.md)
3. [Spreadsheet finance functions and a capstone plan](07-taxes-insurance-and-planning/03-spreadsheet-finance-functions-and-capstone.md)

<!-- lessons:end -->
