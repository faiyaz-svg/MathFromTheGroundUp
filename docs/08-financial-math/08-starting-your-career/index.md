# Starting your career

Comparing job offers with bonuses, RSUs and a match, the tax on interest, dividends and capital gains, and the CPP, tax and GST/HST of a side gig.

1. [Comparing job offers](01-comparing-job-offers.md)
2. [Taxes on investment income](02-taxes-on-investment-income.md)
3. [Side gigs and self-employment](03-side-gigs-and-self-employment.md)

## Cheat sheet

Tax figures are the 2026 values from the sources linked in the lessons and change every year. All people, offers and holdings in the examples are made up.

### Comparing job offers

| Item | Rule | Example |
|---|---|---|
| Expected bonus | target $\times \sum p_k f_k$ | \$9,000 target, factors 0, 1, 1.5 with probabilities 0.2, 0.5, 0.3: \$8,550 |
| Clawback | leaving after $m<12$ months repays $\frac{12-m}{12}S$ | \$10,000 signing bonus, month 8: \$3,333.33 |
| RSU, 4 years, 1-year cliff | 25% vests at month 12, then $\frac{1}{48}$ a month | 1,920 units: 480, then 40 a month |
| RSU tax | value at delivery is employment income; ACB starts at that value | 480 units at \$25: \$12,000 |
| Stock option | benefit = value $-$ exercise price; half deductible if the conditions hold | \$30,000 benefit, \$15,000 taxable |
| Employer match | a return of $m$ on your contribution on day one | 100% on 5% of \$104,000: \$5,200 |
| Present value | $\sum N_t/(1+i)^t$ of after-tax pay | A \$294,584.88, B \$287,601.18 at 5% |

Steps: list the items by year, replace uncertain ones with expected values, tax each year with the 2026 calculator, discount, value non-cash items separately, then stress test the share price and the months you stay. A US offer is a simplified estimate: convert at a dated rate (1.3960 on October 30, 2026), apply the IRS brackets (standard deduction \$16,100 single), 6.2% Social Security up to \$184,500 and 1.45% Medicare, and subtract health costs (KFF 2026: \$1,672 premium, \$1,955 deductible).

Main mistakes:

- Comparing a grant value with a salary instead of the yearly vests.
- Treating a target bonus as certain.
- Ignoring the cliff, the clawback and the vesting rule on a match.
- Comparing before-tax pay, or US dollars with Canadian dollars.
- Counting the match as cash.

### Taxes on investment income

| Income | Added to taxable income | Extra tax per \$1,000 at \$65,000 | At \$120,000 |
|---|---|---|---|
| Interest | 100% | \$296.50 | \$434.10 |
| Eligible dividend | 138% (gross-up), then credits | \$63.90 | \$253.78 |
| Capital gain | 50% (inclusion rate) | \$148.25 | \$217.05 |

With combined bracket rate $r$ and no surtax: interest $rX$, dividend $1.38(r - 0.250198)X$, gain $0.5rX$. The federal credit is 15.0198% and the Ontario credit is 10% of the grossed-up amount. The dividend is taxed less than the gain when $r < 0.39236$. Credits only cancel tax, so they can be unused at a low income.

ACB of identical shares is the average cost, total cost $\div$ shares owned, and a sale does not change the average of the shares left. Gain = proceeds $-$ ACB $-$ selling costs. Losses go against gains of the year, then back three years or forward. A superficial loss (the same shares bought from 30 days before to 30 days after the sale and still held) is added to the ACB of the new shares.

After 20 years, \$10,000 at 6% (made up) is \$22,861.50 as taxed interest, \$29,328.39 as a dividend stock, \$28,799.28 as a growth stock and \$32,071.35 in a TFSA.

Main mistakes:

- Taxing or crediting the cash dividend instead of the grossed-up amount.
- Using first-in first-out for identical shares.
- Repurchasing inside the 61-day window and expecting the loss.
- Saying dividends are always taxed less than gains.

### Side gigs and self-employment

| Item | Rule (2026) |
|---|---|
| Net business income | revenue $-$ deductible expenses (business part, 50% of meals, capital property by CCA) |
| Self-employed CPP | 11.9% of earnings from \$3,500 to \$74,600 (max \$8,460.90), 8% from \$74,600 to \$85,000 (max \$832.00) |
| CPP in tax | credit on 4.95% base, deduction on the rest and all of CPP2 |
| EI | none, unless you opt in to special benefits |
| GST/HST | register when revenue is over \$30,000 in one quarter or in four consecutive quarters; 13% in Ontario |
| Instalments | net tax owing over \$3,000 now and in one of the two previous years; March 15, June 15, September 15, December 15 |
| Deadlines | file June 15, pay April 30 |

Set-aside share = (extra income tax + CPP) $\div$ net business income. On a \$65,000 salary plus \$21,600 net: \$7,993.76, 37.0%. With no other income and \$30,000 net: \$5,608.53, 18.7%. Tax in an invoice with HST is $\frac{13}{113}$ of the total.

Hourly rate matching a \$65,000 job: \$31.25 for paid hours becomes \$56.39 once unpaid time, unbillable time, expenses, benefits, both halves of CPP and tax are counted.

Main mistakes:

- Treating revenue as income.
- Spending HST that belongs to the CRA.
- Expecting no bill until April, with nothing set aside.
- Pricing at the old hourly wage.
