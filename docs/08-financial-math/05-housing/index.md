# Housing

Renting against buying, the rules behind a Canadian mortgage, the month-by-month schedule of a loan, and the compounding rule that sets the payment.

1. [Renting vs buying a home](01-renting-vs-buying-a-home.md)
2. [Mortgage basics](02-mortgage-basics.md)
3. [Mortgage amortization schedules](03-mortgage-amortization-schedules.md)
4. [Canadian mortgage compounding](04-canadian-mortgage-compounding.md)

## Cheat sheet

Rates, prices and rents below are made-up examples. Tax, down payment, premium and qualifying figures are the 2026 values from the sources linked in each lesson, and they change.

### Renting vs buying a home

Unrecoverable costs are money you do not get back. For a renter: rent and renter's insurance. For an owner: mortgage interest, property tax, maintenance, home insurance, and buying and selling fees. The opportunity cost of a down payment is the return it could earn elsewhere. Equity is value minus balance owed.

Ontario land transfer tax, bracket by bracket: 0.5% to \$55,000; 1.0% from \$55,000 to \$250,000; 1.5% from \$250,000 to \$400,000; 2.0% above \$400,000 (2.5% above \$2,000,000 for one or two single-family residences). First-time buyers get a refund of up to \$4,000, so there is no tax on the first \$368,000. Toronto adds its own municipal tax.

| Price | Land transfer tax | After the \$4,000 refund |
|---|---|---|
| \$300,000 | \$2,975 | \$0 |
| \$520,000 | \$6,875 | \$2,875 |
| \$700,000 | \$10,475 | \$6,475 |

Rent vs buy over 10 years: both sides start with the same cash and spend the same each month. The cheaper side invests the difference. Compare owner's wealth (sale price less selling costs less balance, plus investments) with the renter's investments.

Rules of thumb, rough only: yearly unrecoverable cost is about 5% of the price (1% tax, 1% maintenance, 3% cost of capital, which depends on rates), and price-to-rent is $\frac{\text{price}}{12 \times \text{rent}}$.

Main mistakes:

- Comparing rent with the mortgage payment alone and leaving out property tax, maintenance and insurance.
- Counting all of the payment as a cost: the principal part is repaid, not spent.
- Charging the top land transfer rate on the whole price.
- Forgetting selling costs and the cost of the down payment.
- Trusting a model's winner: the answer swings with home growth and investment return.

### Mortgage basics

The term is how long the contract and its rate last (often 5 years). The amortization is how long the payments would take to pay off the loan (often 25 years).

| Price | Minimum down payment |
|---|---|
| up to \$500,000 | 5% |
| \$500,000 up to \$1,500,000 | 5% of the first \$500,000 plus 10% of the rest |
| \$1,500,000 or more | 20% (no insured mortgage) |

Under 20% down, the loan is high-ratio and needs mortgage loan insurance. Premium, as a percent of the loan, by loan-to-value: up to 65%, 0.60%; to 75%, 1.70%; to 80%, 2.40%; to 85%, 2.80%; to 90%, 3.10%; to 95%, 4.00%. The premium is added to the loan, and the rate comes from the loan before the premium. Ontario premiums also carry provincial sales tax, which cannot be added to the loan.

Stress test: you qualify at the greater of the contract rate plus 2% and 5.25%. GDS is housing costs (payment, property tax, heating, half of condo fees) over gross income, at most 39%. TDS adds all other debt payments, at most 44%. Both use the payment at the qualifying rate.

A 30-year amortization is open to first-time buyers and buyers of new builds with a high-ratio mortgage, with a premium 0.20 points higher. It lowers the payment and raises the total interest. A fixed rate holds for the term, and a variable rate can change, so check the budget against a rise of one or two points. A prepayment privilege is the extra amount you may pay each year without a penalty.

Main mistakes:

- Taking 5% of the whole price over \$500,000 instead of 10% of the excess.
- Reading the premium rate off the loan after the premium is added.
- Running GDS and TDS at the real rate instead of the qualifying rate.
- Treating the amortization as the term.

### Mortgage amortization schedules

For each payment: interest $I_k = i \cdot B_{k-1}$, principal $P_k = \text{PMT} - I_k$, and balance $B_k = B_{k-1} - P_k$. The payment is $\text{PMT} = L \cdot \frac{i}{1 - (1+i)^{-n}}$. The balance after $k$ payments is

$$
B_k = L(1+i)^k - \text{PMT} \cdot \frac{(1+i)^k - 1}{i}.
$$

For a \$560,000 loan at a quoted 5% over 25 years: payment \$3,256.99, first month's interest \$2,309.39, balance after 5 years \$495,642.04, total interest \$417,096.37.

| Change | Result |
|---|---|
| renew at 4% / 6% (20 years left) | \$2,994.90 / \$3,529.91 a month |
| accelerated biweekly (half the monthly payment) | paid off in 21.5 years, \$67,688 less interest |
| \$20,000 once at month 12 | 281 months, \$42,988 less interest |
| \$10,000 each year | 17 years, \$144,723 less interest |

Accelerated payments make 13 monthly payments' worth a year. A biweekly schedule that is not accelerated saves almost nothing.

Main mistakes:

- Dividing the quoted rate by 12.
- Picturing the balance as a straight line: early payments are mostly interest.
- Calling the down payment the whole equity.
- Comparing accelerated and ordinary biweekly payments as if they were the same.

### Canadian mortgage compounding

Interest Act section 6 requires a mortgage's rate to be stated "calculated yearly or half-yearly, not in advance". Fixed-rate Canadian mortgages are quoted with semi-annual compounding. For a quoted rate $j$ and $p$ payments a year,

$$
i_p = \Bigl(1 + \frac{j}{2}\Bigr)^{2/p} - 1, \qquad \text{EAR} = \Bigl(1 + \frac{j}{m}\Bigr)^m - 1.
$$

| Quoted 5% | Rate per payment | Effective annual rate |
|---|---|---|
| monthly payments | 0.412392% | 5.0625% |
| biweekly payments | 0.190124% | 5.0625% |
| weekly payments | 0.095017% | 5.0625% |
| compounded monthly instead | 0.416667% | 5.1162% |

On \$560,000 over 25 years, compounding monthly instead of semi-annually adds \$16.72 a month, about \$5,015 in total. Variable rates are often compounded monthly in practice, so read the contract. To compare offers, compare effective annual rates.

Main mistakes:

- Using $\frac{j}{12}$ for a fixed-rate Canadian mortgage.
- Dividing 2.5% by 6.
- Rounding the periodic rate to a few digits.
- Comparing quoted rates with different compounding as if they were the same.
