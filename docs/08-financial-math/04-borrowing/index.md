# Borrowing

Student loans, car loans and leases, credit cards, credit scores and paying off several debts, all built on the loan payment formula.

1. [Student loans](01-student-loans.md)
2. [Car loans and total cost](02-car-loans-and-total-cost.md)
3. [Lease vs buy a car](03-lease-vs-buy-a-car.md)
4. [Credit cards and the minimum payment trap](04-credit-cards-and-the-minimum-payment-trap.md)
5. [Credit scores and paying off debt](05-credit-scores-and-paying-off-debt.md)

All rates, prices and balances in these lessons are made-up examples. Rules and figures come from the official pages linked in each lesson and change over time.

## Cheat sheet

### Student loans

OSAP has two parts. The Canada Student Loan has had no federal interest since April 1, 2023 ([NSLSC](https://www.csnpe-nslsc.canada.ca/en/things-you-need-to-know)). The Ontario part charges prime plus 1% ([ontario.ca](https://www.ontario.ca/page/pay-back-osap)), and interest on it is charged during the six months after studies and added to the principal.

| Step | Formula | Example |
|---|---|---|
| Ontario rate | prime plus 1% | 4.5% prime gives 5.5% |
| Balance after six months | $B = B_0(1 + r)^6$, with $r$ the annual rate divided by 12 | \$12,000 becomes \$12,333.80 |
| Ontario payment | $\text{PMT} = \frac{Br}{1 - (1 + r)^{-n}}$ | \$133.85 over 120 months |
| Federal payment | balance divided by $n$ | \$18,000 over 120 months is \$150 |
| Months with payment $P$ | $n = -\frac{\ln(1 - Br/P)}{\ln(1 + r)}$ | \$233.85 gives 61 months |

- Repayment Assistance Plan: federal payments capped at 10% of household income, with no payments until income passes a threshold (\$40,000 for a single borrower when announced in 2022, indexed). Ontario's plan caps payments at 20% of family income and covers interest relief for up to 60 months. They are two plans.
- An extra \$100 a month on the example Ontario loan saves \$1,911.14 in interest.

Main mistakes:

- Leaving out the six months of interest, which makes the payment too small.
- Using 5.5 instead of $0.055 \div 12$ for the monthly rate.
- Mixing the 10% federal cap with the 20% Ontario cap.

### Car loans and total cost

| Item | Rule | Example |
|---|---|---|
| Price with HST | multiply by 1.13 (13% in Ontario) | \$28,000 becomes \$31,640 |
| Amount financed | price with tax minus down payment and trade-in | \$28,640 |
| Payment and interest | loan formula; interest is $n \cdot \text{PMT} - \text{PV}$ | \$569.81, interest \$5,548.76 (7.2%, 60 months) |
| Depreciation | $V_t = V_0(1 - d)^t$ | 15% a year: \$28,000 is \$12,423.75 after 5 years |
| Cost of ownership | price with tax minus resale value, plus interest and running costs | \$49,265, about \$821 a month |

- Longer terms lower the payment and raise the interest: 48 to 84 months on \$28,640 at 7.2% takes the payment from \$688.48 to \$435.06 and the interest from \$4,407.09 to \$7,905.03.
- 0% offer against rebate plus bank loan: set the payments equal and solve for the rate. For \$31,640 with a \$3,000 rebate over 60 months the break-even is 3.99%. A bank rate below it favours the rebate.

Main mistakes:

- Shopping by monthly payment and ignoring the term.
- Forgetting HST in the amount financed.
- Treating 0% as free when it costs the rebate.
- Leaving depreciation out of the cost.

### Lease vs buy a car

$$
\text{PMT} = \frac{C - R}{n} + (C + R)\, m, \qquad m = \frac{\text{rate in percent}}{2400}.
$$

Here $C$ is the net price, $R$ the residual value and $n$ the number of months. The first part is the depreciation charge and the second is the rent charge. The money factor is a US convention; a Canadian lessor may quote a rate, so ask which.

| Item | Example |
|---|---|
| \$34,000, residual 58%, 48 months, 6% | depreciation \$297.50 plus rent \$134.30 is \$431.80 |
| With 13% HST on the payment | \$487.93 |
| Exact (loan formula with a balloon) | \$433.97, so the money factor is a little low |
| Convert | 0.0021 is 5.04%; 5.4% is 0.00225 |

- Compare totals over the same period: lease total is the amount due at signing, payments with tax, fees and excess kilometres. Buy total is the down payment plus loan payments minus the sale price.
- In the example the break-even sale price is \$16,757.32. Above it buying costs less. A higher residual lowers the payment by about $\frac{1}{n} - m$ per dollar of residual.
- Excess kilometres: 16,000 km over at \$0.15 is \$2,400.

Main mistakes:

- Comparing a lease payment with a loan payment, which buy different things.
- Reading the money factor as a rate (0.0025 is 6%, not 0.25%).
- Forgetting the kilometre limit and end-of-lease charges.

### Credit cards and the minimum payment trap

Daily rate is the annual rate divided by 365. Interest for a cycle is the daily rate times the sum of the daily balances. The FCAC sample disclosure has a grace period of at least 21 days on purchases if you pay in full, and none on cash advances ([FCAC](https://www.canada.ca/en/financial-consumer-agency/services/industry/bulletins/information-box-examples/credit-agreement-credit-card.html)).

| Payment rule on \$2,000 at 18% | Months | Interest |
|---|---|---|
| fixed \$160 | 14 | \$231.45 |
| fixed \$60 (the FCAC example) | 47 | \$793.44 |
| higher of \$10 or 3% of balance | 166 | \$1,798.88 |

- The monthly-rate model matches the FCAC's \$793 and \$231 to the dollar.
- A payment of $pB$ makes the balance follow $B_0(1 + r - p)^k$, which never reaches zero by itself; only the dollar floor ends it.
- Criminal rate: more than 35% APR ([Criminal Code s. 347](https://laws-lois.justice.gc.ca/eng/acts/c-46/section-347.html)).
- Cash advance (FCAC sample): separate rate, a fee, no grace period.

Main mistakes:

- Treating the minimum payment as a plan.
- Assuming cash advances have a grace period.
- Comparing only the payment, not the payoff time.

### Credit scores and paying off debt

The FCAC says scores are usually 300 to 900, formulas are not public, and common factors include credit history (how long you've had credit, kinds of credit, collections, insolvency) and credit habits (carrying a balance, missed payments, total debt, nearness to your limit, new applications) ([FCAC](https://www.canada.ca/en/financial-consumer-agency/services/credit-reports-score/credit-report-score-basics.html)).

| Item | Rule | Example |
|---|---|---|
| Utilization | balance divided by limit | \$3,500 of \$5,000 is 70% |
| Blended rate | sum of balance times rate, divided by total | 14.8% on \$10,400 |
| Snowball | smallest balance first | \$1,608.39 interest, 27 months |
| Avalanche | highest rate first | \$1,547.45 interest, 27 months |

- Avalanche minimizes interest by an exchange argument: moving $x$ from a lower-rate debt to a higher-rate one lowers the combined balance by $x[(1 + r_i)^s - (1 + r_j)^s]$ after $s$ months.
- Consolidation is a rate comparison at the same payment. For \$10,400 at \$450 a month the break-even loan rate is 12.41%, and a fee or moving a cheap debt into a dearer loan can erase the gain.

Main mistakes:

- Skipping minimums on the other debts.
- Dropping the payment when one debt closes.
- Comparing payments instead of rates and terms in a consolidation.
- Averaging rates without weighting by balance.
