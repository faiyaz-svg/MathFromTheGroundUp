# Comparing job offers

After this lesson you can put job offers on one footing: turn a target bonus into an expected value, value a signing bonus, RSUs and an employer match, compare after-tax pay over four years as a present value with the 2026 Ontario tax rules, and make a simplified estimate for a US offer.

Before this: [paycheques and budgeting](../01-everyday-money/03-paycheques-and-budgeting.md), [present and future value](../03-time-value-of-money/01-present-and-future-value.md), [retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md), [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md) and [insurance and expected value](../07-taxes-insurance-and-planning/02-insurance-and-expected-value.md).

All people, companies and offers in this lesson are made up. The tax figures are the 2026 ones from the earlier lessons. The lesson shows the math and the trade-offs, and it does not tell you which offer to take.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A bonus is targeted at 10% of a \$90,000 salary. It pays 0% of the target with probability 0.2, 100% with probability 0.5 and 150% with probability 0.3. Find the expected bonus.
2. An employer matches 100% of your retirement contributions up to 5% of a \$104,000 salary. You contribute 5%. How much does the employer add, and what is the return on your contribution on the day it is paid?
3. A \$10,000 signing bonus must be repaid in proportion to the months left in the first 12 if you leave. You leave after 8 months. How much do you repay?

<details class="solution" markdown>
<summary>Answers</summary>

1. The target is $0.10 \times 90000 = 9000$ dollars. The expected payout factor is $0.2(0) + 0.5(1) + 0.3(1.5) = 0.95$, so the expected bonus is $0.95 \times 9000 = 8550$ dollars.
2. You contribute $0.05 \times 104000 = 5200$ dollars and the employer adds \$5,200. The return on your \$5,200 is $\frac{5200}{5200} = 100\%$ immediately.
3. Four months of the 12 are left, so you repay $\frac{4}{12} \times 10000 = 3333.33$ dollars.

</details>

## The idea

Two offers arrive for the same kind of job. One says \$90,000, the other \$104,000. The first also mentions a bonus, a signing bonus and "RSUs". The second mentions a retirement match. It is tempting to compare the two salaries and stop, but the salary is only the certain part of each offer.

A bonus is a bet, and the payout varies from year to year. RSUs are a promise of shares that arrive on a schedule, worth whatever the share price is on the day. A signing bonus comes with a rule about leaving. A retirement match is a guaranteed return, but it only exists if you stay long enough for it to belong to you. Each piece is also taxed in its own way and arrives in a different year.

The method has three moves, and all three are already in this book. Replace each uncertain amount with its expected value and look at the spread around it. Subtract the tax and the payroll deductions year by year, since a bigger package is taxed at higher rates. Then discount each year to today, so that money in year 4 counts for less than money in year 1. What comes out is one number per offer that you can compare, plus a list of the assumptions that would change the order.

## Definitions

**Total compensation** is everything an employer gives for the work: base salary, bonus, equity, retirement contributions and benefits. In plain words, it is the whole package, and the number on the first line is one part of it.

The **base salary** is the fixed yearly pay. A **target bonus** is a bonus quoted as a percent of the base salary, paid in full when the employee and the company hit their goals. The actual payout is the target times a payout factor that can be below or above 1. If the factor $F$ takes the values $f_k$ with probabilities $p_k$, the **expected bonus** is

$$
E[\text{bonus}] = \text{target} \times E[F] = \text{target} \times \sum_k p_k f_k.
$$

This is the expected value from [insurance and expected value](../07-taxes-insurance-and-planning/02-insurance-and-expected-value.md), and the probabilities come from [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md). In plain words, it is the average bonus over many years like this one, not the bonus you will get in any one year.

A **signing bonus** is a payment made when you start. A **clawback** is a rule that makes you repay part of it if you leave early, usually in proportion to the months left in a period such as 12.

A **restricted stock unit** (RSU) is a promise of one share of the employer's stock for each unit, delivered once conditions are met. The **vesting schedule** says when units become yours. A **cliff** is a period at the start during which nothing vests; the first block vests all at once when the cliff ends. The **grant value** is the number of units times the share price on the grant date.

An **employee stock option** is a right to buy shares at a fixed **exercise price**. When you exercise it, the value of the shares at that moment minus the exercise price is your benefit.

An **employer match** adds money to your retirement savings in proportion to what you contribute. It is paid into a group RRSP or a **deferred profit sharing plan** (DPSP), a registered plan to which only the employer contributes.

## How to do it

### Putting offers on one footing

1. List every item of pay for each year: base salary, expected bonus, signing bonus, RSU vests and the retirement match. Leave out anything that is the same in both offers, such as the same extended health plan, and say that you did.
2. Replace each uncertain amount with its expected value, and note how far it can move. A bonus gets a payout factor. An RSU vest gets a share price.
3. Put each item in the year it arrives. A signing bonus is in year 1. An RSU counts in the year it vests, not the year it is granted.
4. Tax each year. Add the cash items of the year, which are all employment income, and run the 2026 calculator from [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md). Subtract the tax and the CPP and EI. The retirement match is not cash, so it stays out of this step.
5. Discount. With a yearly rate $i$ that you pick, the present value of the after-tax amounts $N_1, \ldots, N_4$ is $\sum_{t=1}^{4} \frac{N_t}{(1+i)^t}$.
6. Value the non-cash items separately. A match is money in a registered plan that is taxed when it comes out, so it is worth its face value times one minus the tax rate you expect at withdrawal.
7. Stress test. Move the share price, the bonus payout and the number of months you stay, and find the point at which the order of the offers changes.

### Bonuses and the signing bonus

The expected bonus uses the formula above. It is a good summary of many years and a poor summary of one: with a target of \$9,000, the bonus above has an expected value of \$8,550 but pays nothing one year in five. The standard deviation of the factor is $\sqrt{0.2(0 - 0.95)^2 + 0.5(1 - 0.95)^2 + 0.3(1.5 - 0.95)^2} = 0.522$, so the bonus has a standard deviation of $0.522 \times 9000 = 4698.14$ dollars. If the bonus helps to pay the rent, compare that spread with your emergency fund.

A clawback is a pro rata repayment. If a signing bonus $S$ is repaid in proportion to the months left in the first 12, leaving after $m < 12$ months costs $\frac{12 - m}{12}S$, and leaving after 12 costs nothing. The agreement decides whether the repayment is of the gross amount, which is the usual wording, and how the tax already paid on the bonus is handled. Read that line before you sign.

### RSUs: vesting, the cliff and tax

A typical schedule is a four-year vest with a one-year cliff: 25% of the units vest at month 12, then $\frac{1}{48}$ of the grant vests each month. With 1,920 units, that is 480 units at month 12 and 40 units a month after it. The figure shows the value of the vested units at a constant \$25 a unit. The dashed line is a schedule with no cliff, and the gap between the two is what the cliff takes from someone who leaves early.

![Value of vested RSUs against months since the start date, from 0 to 48 months. With a one-year cliff nothing vests until month 12, when 25% of the grant, \$12,000 at \$25 a unit, vests at once; after that the value rises by \$1,000 a month to \$48,000 at month 48. A dashed straight line shows a schedule with no cliff. A person who leaves at month 11 has \$0 and one who leaves at month 18 has \$18,000.](../../assets/figures/08-financial-math/comparing-job-offers-vesting.svg)

The table shows what a person has after leaving at different times, for the signing bonus above and this grant.

| Months worked | Signing bonus repaid | RSUs vested | Value of vested RSUs at \$25 |
|---|---|---|---|
| 8 | \$3,333.33 | 0 | \$0 |
| 11 | \$833.33 | 0 | \$0 |
| 12 | \$0 | 480 | \$12,000 |
| 18 | \$0 | 720 | \$18,000 |
| 24 | \$0 | 960 | \$24,000 |

Tax works as follows. The CRA describes a restricted stock plan or RSU as an arrangement in which the employer agrees to issue or sell securities, with a vesting period after which the employee has full rights ([CRA, employee security options](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/benefits-allowances/security-options.html)). The taxable benefit is the fair market value of the shares when the employee acquires them, minus anything paid, and it is reported as employment income on the T4. An RSU costs nothing, so when the shares are delivered, normally at vest, the whole value is added to your income for that year and taxed at your marginal rates.

The same page lists the conditions for the half deduction that makes stock options so favourable, and one of them is that the price paid is not less than the fair market value when the agreement was made. An RSU's price is zero, so that deduction does not apply to it. The adjusted cost base of the shares you now own, the cost that a later gain or loss is measured from, starts at their value on the day they were delivered, which is the amount you were already taxed on. The CRA's page lists the rule for the cost of shares acquired under a security option agreement as paragraph 53(1)(j) of the Income Tax Act. If you sell the shares at once, you have no gain or loss. If you hold them, the later change in price is a capital gain or loss, which is the subject of [Taxes on investment income](02-taxes-on-investment-income.md).

Two consequences matter for the comparison. The tax is due on the vest value even if the price falls the next day, so holding the shares is a separate bet on top of the pay. And some plans sell part of the shares at vest to cover the tax withheld, so fewer shares arrive than the grant suggests; check how your plan works.

### Stock options, at a light level

An option is taxed at exercise on the benefit, which is the value of the shares minus the exercise price. The CRA's conditions for the deduction under paragraph 110(1)(d) include that the price is at least the fair market value when the agreement was made, and then the employee can deduct one half of the benefit. For options from a public company that leaves a taxable amount of half the benefit, the same as a capital gain. A \$200,000 yearly vesting limit applies to the qualifying options of large employers (revenue of more than \$500 million). Options from a Canadian-controlled private corporation follow other rules about timing and a two-year holding condition, and this lesson does not cover them ([CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/benefits-allowances/security-options.html)).

### Retirement match and benefits

A match is a return that is paid at once: a match of $m$ on your contributions is a return of $m$ before any growth ([retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md)). Employer contributions to a group RRSP are a taxable benefit to you, reported on the T4 ([CRA, taxable benefits](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4130/employers-guide-taxable-benefits-allowances.html)), and you deduct them as RRSP contributions. Employer contributions to a DPSP are not taxed until withdrawal ([CRA, DPSP overview](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/deferred-profit-sharing-plans/register-overview.html)). In both cases the contribution reduces your RRSP room, and a DPSP's employer money must vest after two years of membership at the latest, or sooner if the plan says so ([CRA, DPSP contributions](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/deferred-profit-sharing-plans/contributions.html)). Someone who leaves a plan with two-year vesting at month 18 keeps none of the employer's money.

Other benefits, such as extended health, dental, a pension, paid leave and a learning budget, get a dollar value only if the offers differ. Price what you would otherwise buy yourself, and count it as after-tax money, since the benefit replaces a cost you would pay from take-home pay.

### A US offer, as a simplified estimate

A US offer is in US dollars, taxed under US rules, and comes with a different health system. This is a rough estimate for a single filer in a state with no tax on wages. It is not a cross-border tax calculation, and a move to the US also changes your Canadian tax status, which this lesson does not cover.

1. Convert at a dated rate. The Bank of Canada's daily average for USD/CAD was 1.3960 on October 30, 2026 ([Bank of Canada, series FXUSDCAD](https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?recent=5)). One US dollar is 1.3960 Canadian dollars, and the rate changes every day.
2. Federal income tax. For 2026 the standard deduction for a single filer is \$16,100, and the rates are 10% up to \$12,400 of taxable income, 12% up to \$50,400, 22% up to \$105,700, 24% up to \$201,775, 32% up to \$256,225, 35% up to \$640,600 and 37% above ([IRS](https://www.irs.gov/newsroom/working-families-tax-cuts-individuals-and-workers)).
3. Social Security and Medicare. The employee pays 6.2% of wages up to \$184,500 in 2026, and 1.45% of all wages ([IRS, Topic 751](https://www.irs.gov/taxtopics/tc751)).
4. State income tax varies from nothing to a large share, so the estimate leaves it out and a check at the end tries a few rates.
5. Health costs. KFF's 2026 employer survey reports that covered workers with single coverage paid \$1,672 a year toward the premium on average, and that the average deductible was \$1,955 ([KFF, 2026 Employer Health Benefits Survey](https://www.kff.org/health-costs/2026-employer-health-benefits-survey/), published October 22, 2026). A person who uses care pays toward the deductible as well. In Ontario the Ontario Health Premium is already in the tax calculation, and there is no premium or deductible.
6. Convert the result to Canadian dollars at the rate in step 1 and compare it with the after-tax Canadian figures.

<div class="note" markdown>

These figures are for 2026 and change every year. Check the linked pages before using them for real decisions. The estimate does not include cost of living, which can differ a lot between cities, or a 401(k) match, which is retirement money like the Canadian match.

</div>

## Worked examples

<div class="example" markdown>

### Example 1: two Toronto offers over four years

Offer A is a base of \$90,000, a target bonus of 10% with the payout distribution from the quick check, a \$10,000 signing bonus paid in year 1, and the 1,920-unit RSU grant above (grant value \$48,000 at \$25, so 480 units vest each year, worth \$12,000 a year if the price stays at \$25). Offer B is a base of \$104,000 with no bonus and a DPSP match of 100% of 5% of salary, \$5,200 a year. Assume you stay four years, there are no raises, extended health is the same, and the discount rate is 5% (made up).

Steps 1 to 3: the cash items of Offer A in year 1 are $90000 + 8550 + 12000 + 10000 = 120{,}550$ dollars, and in years 2 to 4 they are $90000 + 8550 + 12000 = 110{,}550$ dollars. Offer B pays \$104,000 in every year, and its \$5,200 goes into the plan.

Step 4: the calculator gives these results.

| | Employment income | Income tax | CPP and EI | Take-home pay |
|---|---|---|---|---|
| Offer A, year 1 | \$120,550.00 | \$27,126.46 | \$5,769.52 | \$87,654.02 |
| Offer A, years 2 to 4 | \$110,550.00 | \$23,384.99 | \$5,769.52 | \$81,395.49 |
| Offer B, every year | \$104,000.00 | \$21,283.55 | \$5,769.52 | \$76,946.93 |

Both salaries are above the CPP and EI limits, so the payroll deductions are at their 2026 maximums (\$4,230.45 + \$416.00 + \$1,123.07 = \$5,769.52). In years 2 to 4, Offer A has \$6,550 more employment income than Offer B and \$2,101.44 more income tax, so the extra money keeps only about 68 cents on the dollar.

Step 5: the discount factors at 5% are $\frac{1}{1.05^t}$ for $t = 1, \ldots, 4$, and they add to 3.545951. Offer A's present values are \$83,480.02, \$73,828.11, \$70,312.48 and \$66,964.27, which add to \$294,584.88. Offer B pays the same amount each year, so its present value is $76946.93 \times 3.545951 \approx 272{,}850$ dollars.

Step 6: the match is worth $5200 \times 3.545951 = 18{,}438.94$ dollars as a present value of face amounts. If you expect to pay 20% tax when it comes out (made up), it is worth $0.80 \times 18438.94 = 14{,}751.15$ dollars. Offer B totals about \$287,601.

Offer A comes out about \$6,984 ahead at a share price of \$25. That is a small margin for a package whose bonus can be zero and whose shares can fall, which is why Step 7 matters, and Example 2 does it.

Check: the after-tax present value of Offer A is about 73% of its pre-tax present value of \$401,528.64, which fits an average tax-and-payroll rate of about 27%.

</div>

<div class="example" markdown>

### Example 2: how much can the share price fall?

Keep Offer A and change the price at each vest. If the price is \$17.50 (30% lower than at grant) at every vest, a year's vest is $480 \times 17.5 = 8400$ dollars. If it is \$35 (40% higher), it is $480 \times 35 = 16{,}800$ dollars.

| Price at every vest | Yearly vest value | Added tax in year 2 | Present value of Offer A |
|---|---|---|---|
| \$17.50 | \$8,400 | \$2,643.58 | \$286,285.48 |
| \$25.00 | \$12,000 | \$3,816.36 | \$294,584.88 |
| \$35.00 | \$16,800 | \$5,455.74 | \$305,369.17 |

The added tax is the extra income tax in year 2 from the vest, from the calculator: \$3,816.36 on \$12,000 is 31.8%, a little above the combined bracket rate because the Ontario surtax has started. Offer B is worth about \$287,601, so Offer A beats it at \$25 and \$35 but loses at \$17.50. Solving for the price at which the two tie gives \$18.66, which is 25% below the grant price. Over four years, A is ahead as long as the share price stays above about \$18.66.

Now suppose you keep the 480 shares delivered in year 1 instead of selling. Their adjusted cost base is \$12,000, the value at vest. If you sell later at \$17.50 you have a capital loss of $480 \times (17.5 - 25) = -3600$ dollars, of which half, \$1,800, is an allowable loss that can only be used against taxable capital gains. If you sell at \$35 you have a gain of \$4,800, of which half, \$2,400, is taxable. In either case, the \$3,816.36 of tax on the \$12,000 vest was already paid.

Check: at \$25 the sale at vest leaves $12000 - 3816.36 = 8183.64$ dollars, which is the after-tax value of one year's vest in the table's middle row.

</div>

<div class="example" markdown>

### Example 3: a US offer

Offer C is a base of USD 80,000, a single filer in a state with no tax on wages. Use the six steps of the US estimate.

Step 2: the taxable income is $80000 - 16100 = 63900$. The federal tax is $0.10 \times 12400 + 0.12 \times (50400 - 12400) + 0.22 \times (63900 - 50400) = 1240 + 4560 + 2970 = 8770$ dollars.

Step 3: Social Security is $0.062 \times 80000 = 4960$ and Medicare is $0.0145 \times 80000 = 1160$, which is \$6,120 together.

Step 5: subtract the average premium, \$1,672. The take-home pay is $80000 - 8770 - 6120 - 1672 = 63438$ US dollars.

Steps 1 and 6: at 1.3960 that is $63438 \times 1.3960 = 88{,}559.45$ Canadian dollars. Offer B's take-home pay was \$76,946.93, so on cash alone Offer C is about \$11,600 ahead.

That gap is the first number, not the last. A state income tax of 5% of the \$63,900 taxable income is \$3,195, or about \$4,460 in Canadian dollars. A year in which you spend the whole average deductible of \$1,955 costs about \$2,729. With both, the gap shrinks to about \$4,423, and a state tax of about 10% with the deductible spent would erase it. None of this counts rent, moving costs, a visa or the fact that an exchange rate of 1.30 instead of 1.3960 would cut the Canadian-dollar figure by about 7%.

Check: the US federal tax and payroll taxes are $\frac{8770 + 6120}{80000} = 18.6\%$ of the salary, while Offer B's income tax, CPP and EI are $\frac{21283.55 + 5769.52}{104000} = 26.0\%$ of its salary. A bigger share left after tax is what the gap in take-home pay predicts.

</div>

<div class="example" markdown>

### Example 4: a stock option (finish it yourself)

You are granted 1,000 options with an exercise price of \$20, which equals the share price at the grant. Two years later you exercise them when the shares trade at \$50. Your employer is a public company, the conditions for the deduction are met, and your marginal rate on this amount is 29.65% (the combined bracket rate from [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md), with no surtax and no CPP or EI effects).

Step 1: the benefit is $1000 \times (50 - 20) = 30000$ dollars. Step 2: the deduction is one half of the benefit, so the taxable amount is \$15,000.

Now find the tax with the deduction, the tax without it, and the share of the benefit that goes to tax.

<details class="solution" markdown>
<summary>Finish</summary>

With the deduction the tax is $0.2965 \times 15000 = 4447.50$ dollars. Without it, the benefit would be taxed like salary: $0.2965 \times 30000 = 8895.00$ dollars. The tax with the deduction is 14.8% of the benefit, which is half the marginal rate, the same as a capital gain.

Check: the saving is $8895.00 - 4447.50 = 4447.50$ dollars, which is $0.2965 \times 15000$, the tax on the deducted half.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: comparing a grant value with a salary. A grant of \$48,000 in RSUs over four years is \$12,000 a year, not \$48,000 a year. Put each vest in the year it arrives.

</div>

<div class="warning" markdown>

Watch out: treating a target bonus as pay you will get. The target is the payout at a factor of 1. Example 1 uses the expected value, \$8,550, and the spread around it is \$4,698. If you rely on the bonus to cover rent, use a lower number.

</div>

<div class="warning" markdown>

Watch out: ignoring the rules about leaving. A cliff, a clawback and a two-year vesting rule on a match all decide what you keep if you leave. A package that wins over four years can lose over 11 months.

</div>

<div class="warning" markdown>

Watch out: comparing before-tax pay across the border, or US dollars with Canadian dollars. Convert at a dated rate and compare after-tax and after-premium amounts. The tax systems differ, and so does what the money buys.

</div>

<div class="warning" markdown>

Watch out: counting the match as cash. The employer's \$5,200 goes into a registered plan and is taxed when it comes out. It is worth its face value only if the tax on withdrawal were 0.

</div>

The expected value of a bonus ignores whether the company can pay it, and a share price can fall to zero. A company's stock is a bet on one firm, which carries the risk discussed in [investing returns and risk](../06-investing-and-retirement/01-investing-returns-and-risk.md). A raise changes every later year, so a comparison over four years with no raises is a first pass. You can add a yearly raise to each year's salary in the code below.

## Tricks and shortcuts

What an extra \$1,000 of pay leaves depends on where you start, and it is never your average rate. From the calculator, an employee with a salary of \$65,000 keeps \$643.20 (tax takes \$281.00 and CPP and EI \$75.80), at \$90,000 keeps \$703.50, at \$104,000 keeps \$685.20, and at \$130,000 keeps \$565.90.

Present value of four equal year-end payments at 5%: multiply one payment by 3.546. At 3% the factor is 3.717, and at 8% it is 3.312.

The break-even share price between two offers that differ only by the vests is the base-pay gap divided by the units. If an offer pays \$7,000 a year more in salary than another that grants 600 units a year, the grant needs a price of $\frac{7000}{600} = 11.67$ dollars to tie, as long as both amounts are taxed at the same rate. Practice 7 asks why the tax rate does not matter here.

## In code

The function `net_pay` is a compact version of the calculator from the tax lesson for an employee. The rest of the code discounts the four years, finds the break-even share price by bisection and does the US estimate. Every printed value matches Examples 1 to 3.

<details class="code" markdown>
<summary>In code</summary>

```python
FED = [(58_523, 0.14), (117_045, 0.205), (181_440, 0.26), (258_482, 0.29), (float("inf"), 0.33)]
ONT = [(53_891, 0.0505), (107_785, 0.0915), (150_000, 0.1116), (220_000, 0.1216), (float("inf"), 0.1316)]


def slices(taxable, brackets):
    tax, lower = 0.0, 0.0
    for upper, rate in brackets:
        tax += rate * max(0.0, min(taxable, upper) - lower)
        lower = upper
    return tax


def premium(taxable):
    for upper, amount in [(20_000, 0), (36_000, 300), (48_000, 450), (72_000, 600), (200_600, 750)]:
        if taxable <= upper:
            return amount
    return 900


def net_pay(income):
    """Take-home pay for an Ontario employee with only employment income, 2026 rules (simplified)."""
    pens = max(0.0, min(income, 74_600) - 3_500)
    cpp_base, cpp_enh = 0.0495 * pens, 0.01 * pens
    cpp2 = 0.04 * max(0.0, min(income, 85_000) - 74_600)
    ei = 0.0163 * min(income, 68_900)
    taxable = income - cpp_enh - cpp2
    fed = max(0.0, slices(taxable, FED) - 0.14 * (16_452 + 1_501 + cpp_base + ei))
    ont = max(0.0, slices(taxable, ONT) - 0.0505 * (12_989 + cpp_base + ei))
    surtax = 0.20 * max(0.0, ont - 5_818) + 0.36 * max(0.0, ont - 7_446)
    return income - (fed + ont + surtax + premium(taxable)) - (cpp_base + cpp_enh + cpp2 + ei)


def pv(flows, i=0.05):
    """Present value of year-end cash flows (the first one is one year away)."""
    return sum(c / (1 + i) ** (t + 1) for t, c in enumerate(flows))


def offer_a(price):
    """Base 90,000, expected bonus 8,550, 10,000 signing bonus in year 1, 480 RSUs vest each year."""
    return pv([net_pay(90_000 + 8_550 + 480 * price + (10_000 if y == 0 else 0)) for y in range(4)])


offer_b_cash = pv([net_pay(104_000)] * 4)
offer_b_match = pv([0.05 * 104_000] * 4) * 0.80      # match, valued after a 20% tax at withdrawal
offer_b = offer_b_cash + offer_b_match
for price in (17.50, 25.00, 35.00):
    print(price, round(offer_a(price), 2))
print(round(offer_b_cash, 2), round(offer_b_match, 2), round(offer_b, 2))

lo, hi = 5.0, 40.0                                    # bisection for the break-even share price
for _ in range(60):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if offer_a(mid) < offer_b else (lo, mid)
print(round(lo, 2))

# A US offer, simplified: single filer, 2026 federal brackets, no state tax.
US = [(12_400, 0.10), (50_400, 0.12), (105_700, 0.22), (201_775, 0.24), (256_225, 0.32), (640_600, 0.35), (float("inf"), 0.37)]
usd_cad = 1.3960                                      # Bank of Canada, October 30, 2026
base = 80_000
fed_us = slices(base - 16_100, US)
fica = 0.062 * min(base, 184_500) + 0.0145 * base
net_usd = base - fed_us - fica - 1_672                # 1,672 is the average worker premium for single coverage
print(fed_us, fica, net_usd, round(net_usd * usd_cad, 2))
```

The output is `17.5 286285.48`, `25.0 294584.88` and `35.0 305369.17` for the three share prices. Then `272850.02 14751.15 287601.18` gives Offer B's cash, its match and the total, and `18.66` is the break-even price. The last line is `8770.0 6120.0 63438.0 88559.45`. The total `287601.18` is the sum before rounding, so it is a cent above the sum of the two rounded parts.

The tax function is simplified in the same ways as in the tax lesson: it uses the top amount of each Health Premium band and leaves out smaller credits. The share price is held constant within each scenario, and the 5% discount rate and the 20% tax at withdrawal are made up.

</details>

## FAQ

### Why use an expected value for a bonus I only get once?

Because it is the one number that lets you add the bonus to the rest of the package, and it is correct on average over many such years. For a single year the spread matters too. Use the expected value for the comparison and a low case, such as a payout of 0, for planning what you can afford.

### Why discount the later years?

Money in year 4 is worth less than money now, because money now can be invested or used to pay debt, as in [present and future value](../03-time-value-of-money/01-present-and-future-value.md). Without discounting, a package that pays more late looks better than it is. The rate is your choice: use what you would earn on savings or pay on debt.

### Is an RSU worth the same as a cash bonus of the same size?

On the day of the vest, yes for tax: both are employment income. Before the vest, no. The RSU's value moves with the share price, it is lost if you leave before the vest, and you have to wait for it. A cash bonus has only the payout risk.

### Why does the US estimate leave out a retirement match?

A US 401(k) match is retirement money, like the Canadian match, and it is worth its face value after the tax you expect when it comes out. The comparison above uses cash. To include it, add its present value, valued as in Step 6, to each side.

## Practice

### Warm-up

1\. A bonus has a target of \$6,000 and pays 50% of the target with probability 0.25, 100% with probability 0.5 and 130% with probability 0.25. Find the expected bonus.

<details class="solution" markdown>
<summary>Solution</summary>

The expected payout factor is $0.25(0.5) + 0.5(1) + 0.25(1.3) = 0.125 + 0.5 + 0.325 = 0.95$. The expected bonus is $0.95 \times 6000 = 5700$ dollars.

Check: the three payouts are \$3,000, \$6,000 and \$7,800, and $0.25(3000) + 0.5(6000) + 0.25(7800) = 750 + 3000 + 1950 = 5700$.

</details>

2\. A grant is 2,400 RSUs over four years with a one-year cliff, then monthly vesting. How many units have vested after 10 months, after 12 months and after 30 months?

<details class="solution" markdown>
<summary>Solution</summary>

After 10 months the cliff has not ended, so 0 units have vested. At 12 months, 25% vests: $0.25 \times 2400 = 600$ units. After that, $\frac{2400}{48} = 50$ units vest each month, so at 30 months $50 \times 30 = 1500$ units have vested.

Check: 600 units at month 12 plus 18 more months at 50 units is $600 + 900 = 1500$.

</details>

3\. A \$6,000 signing bonus is repaid in proportion to the months left in the first 24 months. You leave after 15 months. How much do you repay?

<details class="solution" markdown>
<summary>Solution</summary>

Nine months of the 24 are left, so you repay $\frac{9}{24} \times 6000 = 2250$ dollars.

Check: you keep $\frac{15}{24} \times 6000 = 3750$ dollars, and $3750 + 2250 = 6000$.

</details>

### Standard

4\. An employer matches 50% of your contributions up to 6% of an \$80,000 salary. (a) What contribution captures the whole match, and how much is the match? (b) If you contribute 4%, what is the match? (c) What is the return on your own contribution in (a)?

<details class="solution" markdown>
<summary>Solution</summary>

(a) 6% of \$80,000 is \$4,800. The match is $0.50 \times 4800 = 2400$ dollars.

(b) A 4% contribution is \$3,200, and the match is $0.50 \times 3200 = 1600$ dollars. You leave \$800 of match unused.

(c) The return is $\frac{2400}{4800} = 50\%$ on the day it is paid.

Check: the unused match in (b) is $2400 - 1600 = 800$, which is 50% of the \$1,600 of contribution you did not make.

</details>

5\. An RSU grant vests \$10,000 at the end of each of years 1 to 4. The combined marginal tax rate on the vests is 30% (made up). What is the present value of the after-tax vests at a discount rate of 6%?

<details class="solution" markdown>
<summary>Solution</summary>

After tax, each vest is $10000 \times 0.70 = 7000$ dollars. The present value of four year-end payments at 6% is $7000 \times \frac{1 - 1.06^{-4}}{0.06} = 7000 \times 3.465106 = 24{,}255.74$ dollars.

Check: the four terms are \$6,603.77, \$6,229.98, \$5,877.33 and \$5,544.66, and they add to \$24,255.74, the same as the formula.

</details>

6\. A US offer pays USD 70,000. For a single filer in a state with no tax on wages, find the 2026 federal income tax, Social Security and Medicare, the take-home pay after a \$1,672 health premium, and its value in Canadian dollars at 1.3960.

<details class="solution" markdown>
<summary>Solution</summary>

The taxable income is $70000 - 16100 = 53900$. The federal tax is $1240 + 4560 + 0.22 \times (53900 - 50400) = 1240 + 4560 + 770 = 6570$ dollars. Social Security is $0.062 \times 70000 = 4340$ and Medicare is $0.0145 \times 70000 = 1015$, so the payroll taxes are \$5,355. The take-home pay is $70000 - 6570 - 5355 - 1672 = 56403$ US dollars, and in Canadian dollars it is $56403 \times 1.3960 = 78{,}738.59$.

Check: $6570 + 5355 + 1672 = 13597$ and $70000 - 13597 = 56403$.

</details>

### Challenge

7\. Offer X pays a base of \$95,000 and 600 RSUs a year. Offer Y pays a base of \$102,000 and no RSUs. At what share price do the two pay the same before tax? Explain why the answer is the same after tax if both extra amounts are taxed at one marginal rate.

<details class="solution" markdown>
<summary>Solution</summary>

Offer Y pays \$7,000 a year more in salary. The vests tie that amount when $600p = 7000$, so $p = 11.67$ dollars (to the cent, \$11.67).

After tax at a single marginal rate $t$, X's extra is $600p(1 - t)$ and Y's extra is $7000(1 - t)$. These are equal when $600p = 7000$, since the factor $(1 - t)$ cancels. The tie price does not depend on the tax rate as long as both amounts fall in the same bracket.

Check: at \$11.67, $600 \times 11.67 = 7002$, which is within about \$2 of \$7,000. In practice the two amounts are on top of different salaries, so the brackets can differ and the tie moves a little.

</details>

8\. (Reviews [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md).) A \$5,000 bonus is added to a \$65,000 salary, whose taxable income is \$64,385. Use the bracket rates only, and take 5.95% CPP and 1.63% EI off the bonus as well. How much of the bonus does the employee keep?

<details class="solution" markdown>
<summary>Solution</summary>

The bonus lands in the 20.5% federal and 9.15% Ontario brackets: taxable income goes from \$64,385 to \$69,385, below \$107,785 and above \$58,523. The tax is $0.2965 \times 5000 = 1482.50$ dollars. The CPP is $0.0595 \times 5000 = 297.50$ and the EI is $0.0163 \times 5000 = 81.50$. The employee keeps $5000 - 1482.50 - 297.50 - 81.50 = 3138.50$ dollars, which is 62.8% of the bonus.

Check: the full calculator leaves \$3,230.51 (extra income tax \$1,408.42, extra CPP and EI \$361.07). It is \$92.01 higher than this estimate because the extra CPP and EI also earn credits and a deduction, which the estimate leaves out.

</details>

## Where this shows up

- Selling shares that came from an RSU, and the tax on dividends and gains from investments, is in [Taxes on investment income](02-taxes-on-investment-income.md). The tax and CPP on income from a side gig are in [Side gigs and self-employment](03-side-gigs-and-self-employment.md).
- Computing: an offer is a small decision tree with probabilities, which is the setting of [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md), and the break-even price is a root-finding problem like the one in [spreadsheet finance functions and a capstone plan](../07-taxes-insurance-and-planning/03-spreadsheet-finance-functions-and-capstone.md).
- Economics: discounting a stream of pay is the present value idea of [present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md).
