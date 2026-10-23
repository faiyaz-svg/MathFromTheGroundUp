# Time value of money

Money on different dates can't be compared until it is moved to one date: moving single amounts, streams of equal payments, and loans.

1. [Present and future value](01-present-and-future-value.md)
2. [Annuities and geometric series](02-annuities-and-geometric-series.md)
3. [The loan amortization formula](03-loan-amortization-formula.md)

## Cheat sheet

### Present and future value

Let $i$ be the rate per period and $n$ the number of periods. Money moves forward by multiplying by $1 + i$ for each period and backward by dividing.

| Task | Formula | Example |
|---|---|---|
| Future value | $\text{FV} = \text{PV}(1 + i)^n$ | \$2,500 at 3.2% for 7 years is \$3,116.72 |
| Present value | $\text{PV} = \text{FV}(1 + i)^{-n}$ | \$20,000 in 4 years at 4.5% is \$16,771.23 today |
| Move from date $t$ to date $s$ | multiply by $(1 + i)^{s-t}$ | a negative exponent moves money back |
| Rate per period | $i = \frac{j}{m}$ for a nominal rate $j$ compounded $m$ times a year | 4.8% monthly is $i = 0.004$ |
| Effective annual rate | $e = (1 + i)^m - 1$ | $1.004^{12} - 1 = 4.91\%$ |
| Equivalent rate for $\frac{1}{p}$ of a year | $(1 + e)^{1/p} - 1$ | |

- To compare cash flows, move every one to the same date, then add. Any date gives the same ranking, and date 0 is the usual choice.
- The discount factor is $(1 + i)^{-n}$. A sum due later is worth less today for $i > 0$.
- The rate and the number of periods must use the same unit: $i = 0.004$ with $n = 36$ months, or $i = 0.048$ with $n = 3$ years.

Main mistakes:

- Adding amounts from different dates.
- Using the annual rate with a count of months.
- Dividing when you should multiply, or the reverse. A present value is smaller than the future value.
- Rounding the rate in the middle of a calculation.

### Annuities and geometric series

An ordinary annuity pays $\text{PMT}$ at the end of each of $n$ periods. It is a geometric series with ratio $1 + i$.

| Quantity | Ordinary annuity | Annuity due |
|---|---|---|
| Future value | $\text{PMT}\,\dfrac{(1 + i)^n - 1}{i}$ | times $(1 + i)$ |
| Present value | $\text{PMT}\,\dfrac{1 - (1 + i)^{-n}}{i}$ | times $(1 + i)$ |
| Perpetuity (present value) | $\dfrac{\text{PMT}}{i}$, for $i > 0$ | $(1 + i)\dfrac{\text{PMT}}{i}$ |

| Unknown | Formula |
|---|---|
| Payment for a goal | $\text{PMT} = \dfrac{\text{FV}\cdot i}{(1 + i)^n - 1}$ |
| Payment for a loan | $\text{PMT} = \dfrac{\text{PV}\cdot i}{1 - (1 + i)^{-n}}$ |
| Number of payments (saving) | $n = \dfrac{\ln\left(1 + \text{FV}\cdot i/\text{PMT}\right)}{\ln(1 + i)}$ |
| Number of payments (loan) | $n = \dfrac{-\ln\left(1 - \text{PV}\cdot i/\text{PMT}\right)}{\ln(1 + i)}$, needs $\text{PMT} > \text{PV}\cdot i$ |
| The rate $i$ | no formula: bisection or Newton's method, or a spreadsheet |

- Derivation: each payment grows by $(1 + i)^{n-k}$, and the sum of $1, (1 + i), \dots, (1 + i)^{n-1}$ is $\frac{(1 + i)^n - 1}{i}$. The present value is the future value divided by $(1 + i)^n$.
- Check by the recurrence $F_k = (1 + i)F_{k-1} + \text{PMT}$, with $F_0 = 0$.
- When payments don't match the compounding, use $i_p = (1 + j/m)^{m/p} - 1$ for $p$ payments a year.
- Round the number of payments up. The last payment is smaller.
- Example: \$300 a month for 25 years at 5% compounded monthly is \$178,652.91, of which \$90,000 is deposits.

Main mistakes:

- Using $n - 1$ as the exponent. The exponent is the number of payments.
- Treating the annual rate as the monthly rate.
- Using $\frac{j}{12}$ when interest is compounded semi-annually.
- Taking the logarithm when the payment is no bigger than the interest.
- Forgetting that the value is at the last payment (future value) or one period before the first (present value).

### The loan amortization formula

For a loan $\text{PV}$ repaid by $n$ payments at rate $i$ per period, the balance after $k$ payments follows $B_0 = \text{PV}$ and $B_{k+1} = (1 + i)B_k - \text{PMT}$.

| Quantity | Formula |
|---|---|
| Balance, closed form | $B_k = \text{PV}(1 + i)^k - \text{PMT}\,\dfrac{(1 + i)^k - 1}{i}$ |
| Payment | $\text{PMT} = \dfrac{\text{PV}\cdot i}{1 - (1 + i)^{-n}}$, from $B_n = 0$ |
| Balance after $k$ payments | $\text{PMT}\,\dfrac{1 - (1 + i)^{-(n-k)}}{i}$, the present value of the payments left |
| Interest portion of payment $k$ | $I_k = iB_{k-1}$ |
| Principal portion | $P_k = \text{PMT} - I_k$, and $P_{k+1} = (1 + i)P_k$ |
| Total interest | $n\,\text{PMT} - \text{PV}$ |
| Payments with an extra $E$ | $n' = \dfrac{-\ln\left(1 - \text{PV}\cdot i/(\text{PMT} + E)\right)}{\ln(1 + i)}$ |

- The first payment's interest is always $i \times \text{PV}$. Early payments are mostly interest, so half the payments leave much more than half the loan owing: \$30,000 at 0.5% a month over 10 years still owes \$17,227.79 after 5 years.
- A schedule works in cents, and the last payment absorbs the rounding.
- At $i = 0$ the payment is $\frac{\text{PV}}{n}$.
- Longer terms lower the payment and raise the interest. For \$30,000 at 0.5% a month: 5 years is \$579.98 a month and \$4,799.04 of interest, and 25 years is \$193.29 and \$27,987.13.
- The Canadian mortgage compounding rule is in [Canadian mortgage compounding](../05-housing/04-canadian-mortgage-compounding.md).

Main mistakes:

- Using the annual rate with monthly payments.
- Charging interest on the original amount every month.
- Treating the payment as the cost: total interest is $n\,\text{PMT} - \text{PV}$.
- Rounding the payment and expecting the balance to end at exactly \$0.00.
