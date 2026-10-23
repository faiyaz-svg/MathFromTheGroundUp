# Retirement accounts: RRSP, TFSA and FHSA

After this lesson you can work out your TFSA, RRSP and FHSA contribution room, show with algebra when a TFSA and an RRSP give the same after-tax result and when they don't, value an employer match as a return, size a retirement portfolio with the 4% rule of thumb, and compare starting CPP early or late as an annuity choice.

Before this: [investing returns and risk](01-investing-returns-and-risk.md), [index funds, fees and dollar-cost averaging](02-index-funds-fees-and-dollar-cost-averaging.md), [compound interest](../02-interest-and-growth/02-compound-interest.md) and [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md).

This lesson explains the rules and the math. It does not tell you which account to use or what to buy. Growth rates and tax rates in the examples are made up, while the limits are the real 2026 figures with their sources.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. You withdraw \$5,000 from your TFSA in March 2026. When does that room come back?
2. Your earned income in 2025 was \$90,000. Ignoring carry-forward room and pension adjustments, how much new RRSP room do you get for 2026?
3. You have \$1,000 of income before tax. Your tax rate is 30% now and will be 30% when you withdraw. Compare a TFSA and an RRSP after 20 years of growth at 5% a year.

<details class="solution" markdown>
<summary>Answers</summary>

1. On January 1, 2027, the next calendar year. Withdrawals are added back to room only then.
2. The room is 18% of the income, up to the dollar limit: $0.18 \times 90000 = 16{,}200$, which is under \$33,810, so \$16,200.
3. TFSA: pay the tax first, invest \$700, and it grows to $700 \times 1.05^{20} = 1{,}857.31$, tax-free. RRSP: invest \$1,000, it grows to \$2,653.30, and 30% tax leaves $0.7 \times 2653.30 = 1{,}857.31$. The results are the same.

</details>

## The idea

Money you invest in an ordinary account is taxed along the way: interest and some other income each year, and a share of any gain when you sell. A registered account gives the investment a tax shelter. The three accounts in this lesson shelter it in different ways, and the differences come down to one question: when do you pay the tax, if ever?

With a TFSA you put in money that has already been taxed, and the growth and the withdrawals are never taxed. With an RRSP you put in money before tax (you deduct the contribution from your income, so you pay less tax this year), the growth is sheltered, and you pay tax on whatever you take out. The FHSA mixes the two: you get the deduction when you put money in, and the withdrawal is tax-free when it is used to buy a first home.

Whether the TFSA or the RRSP leaves you with more is a question of algebra, and the algebra gives a clean answer: if your tax rate is the same when you put money in and when you take it out, the two are equal. That one fact explains most of the advice you will hear. The rest of the lesson covers the limits on each account, the value of an employer match, how large a nest egg to aim for, and the government pensions that start on a date you choose.

## Definitions

A **Tax-Free Savings Account** (TFSA) is a registered account in which investment growth and withdrawals are not taxed. Contributions are made with money that has already been taxed and are not deductible. Your **TFSA contribution room** is the total you are allowed to put in: the yearly dollar limits added up from the year you turned 18 (or 2009, if later) and are a Canadian resident, minus your contributions, plus your withdrawals from earlier years.

A **Registered Retirement Savings Plan** (RRSP) is a registered account in which contributions are deducted from your taxable income, growth is not taxed while it stays in the plan, and withdrawals are added to your taxable income. Your **RRSP deduction limit** is the room you have for deductible contributions.

A **First Home Savings Account** (FHSA) is a registered account for saving for a first home, with deductible contributions and tax-free growth, and withdrawals that are tax-free when they are qualifying withdrawals (money used to buy a qualifying first home).

Your **marginal tax rate** is the rate of tax on your next dollar of income (see [income tax brackets](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md)). In plain words, it is the share of an extra \$100 of income that goes to tax. It is the rate that matters when you compare a TFSA and an RRSP, because a deduction or a withdrawal moves your income at the margin.

An **employer match** is money your employer adds to your retirement savings when you contribute, usually a percentage of your contribution up to a limit.

## The three accounts and their 2026 limits

### TFSA

For 2026 the TFSA limit is \$7,000 ([CRA table of limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html)). The yearly limit has changed over time: \$5,000 for 2009 to 2012, \$5,500 for 2013 and 2014, \$10,000 for 2015, \$5,500 for 2016 to 2018, \$6,000 for 2019 to 2022, \$6,500 for 2023, and \$7,000 for 2024 to 2026. Adding these up gives \$109,000 of cumulative room through 2026 for someone who was 18 or older and a resident throughout. That total is a sum of the CRA's yearly table, computed for this book, and not a number the CRA states.

Room is used by contributions. Withdrawals don't give room back at once: "the amount you withdraw will only be added back as available contribution room on January 1 of the next calendar year" ([CRA, withdrawing from a TFSA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/tax-free-savings-account/withdraw.html)). Unused room carries forward without limit. Putting in more than your room is taxed at 1% per month on the excess.

### RRSP

Your new room each year is the lesser of 18% of your earned income from the previous year and the dollar limit for the year, added to unused room from earlier years (pension adjustments from a workplace pension reduce it) ([CRA, how contributions affect your deduction limit](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html)). The 2026 dollar limit is \$33,810 ([CRA table of limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html)). The 18% reaches the dollar limit when the previous year's earned income is $\frac{33810}{0.18} = 187{,}833.33$ dollars. Below that income, 18% of the income is the binding number.

A contribution counts for a tax year if it is made in that year or in the first 60 days of the next one. For the 2025 tax year the deadline was March 2, 2026 ([CRA, important dates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html)). You can go over your limit by \$2,000 without penalty, and above that the excess is taxed at 1% per month. Withdrawals are added to your income for the year you take them out.

### FHSA

The FHSA has an annual limit of \$8,000, and unused room carries forward, up to \$8,000, into the next year. So the most you can contribute in one year is \$16,000, and the lifetime limit is \$40,000 ([CRA, contributing to your FHSA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/contributing-your-fhsa.html)). The CRA page shows the \$40,000 in its room formula and doesn't name it as a limit in a sentence, so check the page for your own case. Contributions are deductible like RRSP contributions.

A withdrawal is a qualifying withdrawal, and is not added to your income, when you are a first-time home buyer for this purpose, have a written agreement to buy or build a qualifying home, and intend to live in it as your main home within one year ([CRA, withdrawals from your FHSA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account/withdrawing-money-from-your-fhsa.html)). Other withdrawals are taxable.

<div class="note" markdown>

These figures are for 2026 and change every year. Check the linked pages before using them for real decisions.

</div>

## How to do it

### Counting contribution room

1. List the yearly limits for each year you have been eligible, and add them (TFSA), or take 18% of last year's earned income up to the dollar limit (RRSP).
2. Subtract your contributions so far.
3. For the TFSA, add back withdrawals from earlier calendar years, not this one.
4. Compare any planned contribution with the result, and remember the deadlines (December 31 for the TFSA's calendar year, the first 60 days of the next year for an RRSP deduction).

### Comparing a TFSA and an RRSP

*Theorem 3 (equal tax rates).* Suppose you have an amount $P$ of income before tax, which grows at the same rate in either account over $n$ years, with a total growth factor $G = (1 + r)^n$. If your tax rate is $t$ when you contribute and $t$ when you withdraw, a TFSA and an RRSP leave you with the same after-tax amount, $P(1 - t)G$. If the rates are $t_c$ at contribution and $t_w$ at withdrawal, the RRSP result divided by the TFSA result is $\frac{1 - t_w}{1 - t_c}$.

We know how each account is taxed: the TFSA after contribution and never again, the RRSP only at withdrawal. We want to compare the amounts left in your hands after tax. The plan is to follow the amount $P$ through each account and write the result as a product of factors.

*Proof.* In the TFSA you first pay tax on the income, leaving $P(1 - t_c)$. This grows to $P(1 - t_c)G$, and the withdrawal is tax-free. In the RRSP you contribute all of $P$ (the contribution is deducted, so no tax is owed on it now). It grows to $PG$, and the withdrawal is taxed at $t_w$, leaving $PG(1 - t_w)$. The ratio of the RRSP result to the TFSA result is

$$
\frac{PG(1 - t_w)}{P(1 - t_c)G} = \frac{1 - t_w}{1 - t_c}.
$$

If $t_c = t_w = t$, the ratio is 1, and the two results $P(1 - t)G$ and $PG(1 - t)$ are the same product with the factors in a different order. $\blacksquare$

Look back: multiplication is commutative, so it doesn't matter whether the factor $(1 - t)$ is applied before or after the growth factor $G$. What matters is whether the two tax factors are different. If your rate in retirement is lower than your rate now ($t_w < t_c$), the ratio is above 1 and the RRSP wins. If it is higher, the TFSA wins. The growth rate, the number of years and the amount all cancel out.

One more point: the proof assumes the RRSP tax refund is invested too (or that the contribution is deducted at source, as with a workplace plan). If you contribute \$1,000 to an RRSP and spend the refund, you have contributed less money than you would in the TFSA version, and the comparison isn't like for like.

### Valuing an employer match

A match is a return that arrives at once. If you put in $C$ and the employer adds $m \cdot C$, you have gained a return of $m$ (as a decimal) before any investment growth. A 50% match is a 50% return on the day it is paid.

### The 4% rule

The **4% rule** is a rule of thumb for how much a retirement portfolio can support. You withdraw 4% of the portfolio's value in your first year of retirement and raise that dollar amount with inflation each year after. It comes from studies of US market history in the 1990s (Bengen 1994, and a 1998 study often called the Trinity study), which found that this pattern would have lasted at least 30 years in the periods they tested. It is not a law and carries no guarantee: the studies used US data, longer retirements, Canadian fees and taxes, or a different mix of investments can change the answer, and many planners prefer a lower starting rate. The studies themselves are not linked here, so treat their details as background and not as sourced results.

The arithmetic is simple. If you want to spend $S$ dollars a year, the rule says you need a portfolio of $\frac{S}{0.04} = 25S$. To spend \$40,000 a year you need \$1,000,000.

You can see what the rule assumes with the annuity formula from [annuities and geometric series](../03-time-value-of-money/02-annuities-and-geometric-series.md). If a portfolio earns a steady real (after-inflation) return $r$ and you withdraw a level real amount for $n$ years, the first-year withdrawal as a fraction of the starting balance is

$$
w = \frac{r}{1 - (1 + r)^{-n}}, \qquad \text{and } w = \frac{1}{n} \text{ when } r = 0.
$$

For $n = 30$, a withdrawal fraction of 4% matches a real return of about 1.22% a year. So the rule is not very demanding in a smooth world with steady returns. It is built from history because real returns arrive in an uneven order, and a bad stretch early in retirement does the most damage.

### Starting CPP early or late

CPP can start between 60 and 70, with 65 as the standard age. Each month before 65 reduces the payment by 0.6% (up to 36% at 60), and each month after 65 raises it by 0.7% (up to 42% at 70) ([Canada.ca, when to start CPP](https://www.canada.ca/en/services/benefits/publicpensions/cpp/when-start.html)). OAS has a similar rule for waiting, with 0.6% per month up to 36% at 70 ([Canada.ca, when to start OAS](https://www.canada.ca/en/services/benefits/publicpensions/old-age-security/when-start.html)).

Choosing a start age is choosing between two streams of payments, as in a choice between annuities: a smaller payment that starts earlier, or a larger one that starts later. Suppose the payment at 65 would be $B$ a month. Starting at age $a_1$ for $b_1$ a month or at age $a_2 > a_1$ for $b_2 > b_1$, and ignoring interest and indexing, the total received by age $T$ is $12b_1(T - a_1)$ against $12b_2(T - a_2)$. They are equal at

$$
T = \frac{b_2a_2 - b_1a_1}{b_2 - b_1}.
$$

If you live past $T$, waiting paid more in total, and if you don't, starting earlier did. The break-even age depends on how long you expect to live, which you don't know, so waiting works like insurance against a long life. A fuller comparison discounts the later payments, as in [present and future value](../03-time-value-of-money/01-present-and-future-value.md), which pushes the break-even ages later.

### Registered retirement income funds

An RRSP must be closed, converted to an annuity or converted to a **registered retirement income fund** (RRIF) by the end of the year you turn 71 ([CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/important-dates-rrsp-rrif-rdsp.html)). A RRIF keeps the money invested but requires a minimum withdrawal each year, equal to the balance at the start of the year times a factor from the CRA's [chart of prescribed factors](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/completing-slips-summaries/t4rsp-t4rif-information-returns/payments/chart-prescribed-factors.html). At age 70 and under the factor is $\frac{1}{90 - \text{age}}$, so 4.00% at 65 and 5.00% at 70. At 71 it is 5.28%, at 72 it is 5.40% and at 73 it is 5.53% (for most RRIFs). Withdrawals are taxable income. On a \$400,000 balance the minimum is \$21,120 at 71, \$21,600 at 72 and \$22,120 at 73 (if the balance were still \$400,000 at the start of each year).

## Worked examples

<div class="example" markdown>

### Example 1: TFSA room over four years

Someone turns 18 in 2023 and is a resident from then on. In 2024 they contribute \$10,000. In 2025 they withdraw \$4,000 and contribute nothing. How much room do they have on January 1, 2026 (after the 2026 limit is added), and how much is in the account (ignoring growth)?

Step 1: the room granted by the yearly limits is \$6,500 (2023), \$7,000 (2024), \$7,000 (2025) and \$7,000 (2026), a total of \$27,500.

Step 2: the \$10,000 contribution in 2024 uses room. The \$4,000 withdrawal in 2025 doesn't change the 2025 room, but it is added back on January 1, 2026.

Step 3: the room on January 1, 2026 is $27500 - 10000 + 4000 = 21{,}500$ dollars. The account holds $10000 - 4000 = 6{,}000$ dollars.

Check by timeline: after 2023, room is \$6,500. On January 1, 2024, add \$7,000 for \$13,500, then contribute \$10,000, leaving \$3,500. On January 1, 2025, add \$7,000 for \$10,500. On January 1, 2026, add \$7,000 and the \$4,000 withdrawn for $10500 + 7000 + 4000 = 21{,}500$.

<div class="warning" markdown>

Watch out: putting the \$4,000 back in 2025 would have been safe here, because 2025 room was \$10,500. For a person who had used all their room, the same re-contribution would be an over-contribution taxed at 1% a month.

</div>

</div>

<div class="example" markdown>

### Example 2: RRSP room and the refund

Your earned income in 2025 was \$90,000, you have no other room, and no pension. You contribute \$5,000 in 2026. Suppose your marginal tax rate is 30% (made up). What is your room, and what do you save in tax?

The new room is $\min(0.18 \times 90000, 33810) = \min(16200, 33810) = 16{,}200$. A \$5,000 contribution fits, and \$11,200 of room is left.

The deduction cuts your taxable income by \$5,000, which at 30% saves $0.3 \times 5000 = 1{,}500$ dollars. The out-of-pocket cost of the contribution is $5000 - 1500 = 3{,}500$ dollars.

Check: the \$5,000 in the plan is a pre-tax amount. If you later withdraw it at the same 30% rate, you keep \$3,500, which is exactly what it cost you.

</div>

<div class="example" markdown>

### Example 3: TFSA or RRSP for \$10,000 of pre-tax income

You have \$10,000 of income before tax. Money grows at 5% a year for 25 years, so $G = 1.05^{25} = 3.3864$. Compare the two accounts for three pairs of tax rates.

| Rate now $t_c$ | Rate at withdrawal $t_w$ | TFSA after tax | RRSP after tax | RRSP divided by TFSA |
|---|---|---|---|---|
| $30\%$ | $30\%$ | \$23,704.48 | \$23,704.48 | $1.000$ |
| $33\%$ | $25\%$ | \$22,688.58 | \$25,397.66 | $1.119$ |
| $20\%$ | $30\%$ | \$27,090.84 | \$23,704.48 | $0.875$ |

For the first row, the TFSA is $10000 \times 0.70 \times 3.3864 = 23{,}704.48$ and the RRSP is $10000 \times 3.3864 \times 0.70$, the same. For the second row, the TFSA is $10000 \times 0.67 \times G = 22{,}688.58$ and the RRSP is $10000 \times G \times 0.75 = 25{,}397.66$, a ratio of $\frac{0.75}{0.67} = 1.119$, so the RRSP is ahead by 11.9%. For the third row the ratio is $\frac{0.70}{0.80} = 0.875$, so the TFSA is ahead.

Check: each ratio equals $\frac{1 - t_w}{1 - t_c}$, as Theorem 3 says, and each product is the same set of factors in a different order when the rates match.

</div>

<div class="example" markdown>

### Example 4: when to start CPP

Suppose your CPP payment at 65 would be \$1,000 a month (made up, and ignoring indexing). What do you get if you start at 60 or at 70, and at what age does waiting pay off?

At 60 you are 60 months early: $1 - 0.006 \times 60 = 0.64$, so \$640 a month. At 70 you are 60 months late: $1 + 0.007 \times 60 = 1.42$, so \$1,420 a month.

Break-even of 60 against 65, using the formula with $(b_1, a_1) = (640, 60)$ and $(b_2, a_2) = (1000, 65)$: $T = \frac{1000 \times 65 - 640 \times 60}{1000 - 640} = \frac{26600}{360} \approx 73.9$. Break-even of 65 against 70: $T = \frac{1420 \times 70 - 1000 \times 65}{1420 - 1000} = \frac{34400}{420} \approx 81.9$.

So, without any interest, waiting from 60 to 65 pays off if you live past about 74, and waiting from 65 to 70 pays off past about 82. If the later payments are discounted at a real 2% a year (made up), the break-even ages move later, to about 75.4 and 84.5.

Check: at age 82 the person who started at 65 has received $12 \times 1000 \times 17 = 204{,}000$, and the person who started at 70 has received $12 \times 1420 \times 12 = 204{,}480$. They are about equal, as predicted.

</div>

<div class="example" markdown>

### Example 5: an employer match (finish it yourself)

Your salary is \$75,000. Your employer matches 100% of your contributions up to 3% of salary (made up). You contribute 3%. How much does the employer add, and what is the return on your contribution on the day it is paid?

Step 1: your contribution is $0.03 \times 75000 = 2{,}250$ dollars. Step 2: the match is 100% of that. Now find the match, the total in the plan, and the return, and say how many years of 5% growth it would take for an ordinary investment to earn the same.

<details class="solution" markdown>
<summary>Finish</summary>

The employer adds \$2,250, so \$4,500 goes into the plan. The return on your \$2,250 is $\frac{2250}{2250} = 100\%$ immediately. An investment growing at 5% a year takes $\frac{\ln 2}{\ln 1.05} \approx 14.2$ years to double.

Check: $2250 \times 1.05^{14.2} \approx 4500$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: an RRSP balance is a pre-tax amount. A \$100,000 RRSP and a \$100,000 TFSA are not worth the same to spend. At a 25% rate on withdrawal the RRSP is worth about \$75,000 after tax. Compare accounts after tax, as in Theorem 3.

</div>

<div class="warning" markdown>

Watch out: re-contributing a TFSA withdrawal in the same year. The room comes back only on January 1 of the next year. If you have no other room, the re-contribution is an over-contribution taxed at 1% a month.

</div>

<div class="warning" markdown>

Watch out: the RRSP deduction is a deferral, not a gift. The refund is a loan from the tax system that you repay, with the growth, as tax on withdrawal. It is worth the most when your rate falls between contribution and withdrawal.

</div>

<div class="warning" markdown>

Watch out: the 4% rule is a rule of thumb from historical data. It isn't a guaranteed safe rate. A portfolio that has to last longer, or earns less, or pays higher fees can't support the same 4%.

</div>

Contribution room depends on earned income, so a student with little or no earned income gets little or no new RRSP room, and a deduction at a low marginal rate is worth little. Unused RRSP room carries forward, and a contribution that you don't deduct right away can be deducted in a later year, so some people contribute now and deduct when their rate is higher. (the [CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html) calls these unused contributions from a previous year).

The comparison in Theorem 3 uses marginal rates and a single tax rate at withdrawal, and real retirements have more going on: RRSP and RRIF withdrawals can reduce income-tested benefits, TFSA withdrawals don't count as income, and your rate in retirement depends on other income. The algebra tells you which rate comparison matters, and your own numbers fill it in.

## Tricks and shortcuts

To find the income that reaches the RRSP dollar limit, divide the limit by 0.18: $\frac{33810}{0.18} \approx 187{,}833$.

To compare accounts quickly, ask one question: is my tax rate now higher or lower than it will be when I withdraw? Higher now favours the RRSP. Lower now favours the TFSA. Equal means a tie.

For the 4% rule, multiply the yearly spending you want, after other income such as CPP, by 25. For a gap of \$30,000 a year, that is \$750,000.

For the CPP, a quick approximation of the age at which waiting from 65 to 70 breaks even (no interest) is about 82, because 5 years of 42% extra payments take about 17 years of the extra amount to repay the 5 years of lost payments: $\frac{5}{0.42} \approx 11.9$ years of extra payments after 70, so $70 + 11.9 \approx 81.9$.

## In code

The code redoes the TFSA and RRSP comparison, the room calculation, the real return that makes a 4% withdrawal last 30 years, the CPP break-even ages, and the RRIF minimums.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

# TFSA against RRSP for $10,000 of pre-tax income, 25 years at 5%.
G = 1.05 ** 25
for t_now, t_later in [(0.30, 0.30), (0.33, 0.25), (0.20, 0.30)]:
    tfsa = 10_000 * (1 - t_now) * G
    rrsp = 10_000 * G * (1 - t_later)
    print(t_now, t_later, round(tfsa, 2), round(rrsp, 2), round(rrsp / tfsa, 3))
# 0.3 0.3 23704.48 23704.48 1.0
# 0.33 0.25 22688.58 25397.66 1.119
# 0.2 0.3 27090.84 23704.48 0.875

# TFSA limits 2009 to 2026, summed.
limits = [5000] * 4 + [5500] * 2 + [10000] + [5500] * 3 + [6000] * 4 + [6500] + [7000] * 3
print(len(limits), sum(limits))   # 18 109000

# RRSP room for 2025 earned income of $90,000, and the income that reaches the limit.
print(min(0.18 * 90_000, 33_810), round(33_810 / 0.18, 2))   # 16200.0 187833.33

# Level real withdrawal fraction w = r / (1 - (1 + r) ** -n), and the real return that gives 4%.
def w(r, n):
    return 1 / n if r == 0 else r / (1 - (1 + r) ** -n)

lo, hi = 0.0, 0.1
for _ in range(100):
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if w(mid, 30) < 0.04 else (lo, mid)
print(round(w(0, 30), 4), round(lo, 4))   # 0.0333 0.0122

# CPP break-even ages (no interest): start at a1 for b1 or at a2 for b2.
def breakeven(b1, a1, b2, a2):
    return (b2 * a2 - b1 * a1) / (b2 - b1)

print(round(breakeven(640, 60, 1000, 65), 1), round(breakeven(1000, 65, 1420, 70), 1))   # 73.9 81.9

# RRIF minimums on a $400,000 balance.
print([round(400_000 * f) for f in (0.0528, 0.0540, 0.0553)])   # [21120, 21600, 22120]
```

</details>

## FAQ

### Should I use a TFSA or an RRSP first?

The math says it depends on two tax rates: the one you pay now and the one you expect to pay at withdrawal. If the first is higher, the RRSP gains from the difference, and if it is lower, the TFSA does. An employer match is a separate matter: it is a large return that usually comes with the workplace plan, which is why people often take it first. For a student with a low income today, the deduction is worth little now, and the TFSA is attractive on that count alone. This lesson doesn't tell you what to do, and a real choice also depends on your income, goals and plans.

### Why is the RRSP deduction not free money?

Because the tax comes back at withdrawal. In Theorem 3 the RRSP's tax factor $(1 - t_w)$ is applied to the whole balance, growth included, instead of to the contribution alone. The deduction only helps if the rate you pay later is lower than the rate you saved at.

### What if I don't use all my TFSA room?

It carries forward to later years with no limit, so the cumulative room keeps growing even when you don't contribute. The room is a right to use, not a use-it-or-lose-it amount.

### Is the CPP early-or-late choice only about the break-even age?

No. The break-even age is a useful number, but it ignores interest on money you receive early, any other income, taxes, and the fact that payments continue as long as you live. Delaying is a bet on living long, and it also acts as insurance against outliving your savings.

## Practice

### Warm-up

1\. Your earned income in 2025 was \$52,000. How much new RRSP room do you get for 2026 (no carry-forward, no pension)?

<details class="solution" markdown>
<summary>Solution</summary>

$0.18 \times 52000 = 9{,}360$, which is below the \$33,810 limit, so the new room is \$9,360.

Check: \$9,360 is 18% of \$52,000, since $9360 \div 52000 = 0.18$.

</details>

2\. A person turned 18 in 2024 and has been a resident since. What is their total TFSA room through 2026 if they have not contributed anything?

<details class="solution" markdown>
<summary>Solution</summary>

The yearly limits for 2024, 2025 and 2026 are each \$7,000, so the total is $3 \times 7000 = 21{,}000$ dollars.

Check: this matches the cumulative table, in which the 2009 to 2023 total is \$88,000, and \$88,000 plus \$21,000 is \$109,000.

</details>

3\. Your CPP payment at 65 would be \$900 a month. What would it be if you start at 62, and what if you start at 68?

<details class="solution" markdown>
<summary>Solution</summary>

At 62 you are 36 months early: $1 - 0.006 \times 36 = 0.784$, so $900 \times 0.784 = 705.60$ dollars a month. At 68 you are 36 months late: $1 + 0.007 \times 36 = 1.252$, so $900 \times 1.252 = 1{,}126.80$ dollars a month.

Check: 62 is within 60 to 65 and 68 is within 65 to 70, so neither hits the 36% or 42% cap.

</details>

### Standard

4\. You have \$5,000 of income before tax. Your tax rate now is 28% and you expect 22% at withdrawal. Money grows at 6% for 20 years. Compare the TFSA and the RRSP after tax.

<details class="solution" markdown>
<summary>Solution</summary>

The growth factor is $1.06^{20} = 3.2071$. TFSA: $5000 \times 0.72 \times 3.2071 \approx 11{,}545.69$. RRSP: $5000 \times 3.2071 \times 0.78 \approx 12{,}507.83$. The ratio is $\frac{0.78}{0.72} = 1.0833$, so the RRSP is ahead by about 8.3%, or \$962.

Check: $12507.83 \div 11545.69 = 1.0833$.

</details>

5\. You want to spend \$52,000 a year in retirement. How large a portfolio does the 4% rule say you need? What if you use 3.5%?

<details class="solution" markdown>
<summary>Solution</summary>

At 4%: $\frac{52000}{0.04} = 1{,}300{,}000$. At 3.5%: $\frac{52000}{0.035} \approx 1{,}485{,}714.29$. A lower starting rate needs about \$185,714 more.

Check: $0.04 \times 1300000 = 52000$ and $0.035 \times 1485714.29 = 52000$.

</details>

6\. A RRIF holds \$250,000 at the start of the year in which the holder turns 72. What is the minimum withdrawal? What would it be at age 68, with the same balance?

<details class="solution" markdown>
<summary>Solution</summary>

At 72 the factor is 5.40%, so the minimum is $0.054 \times 250000 = 13{,}500$ dollars. At 68 the factor is $\frac{1}{90 - 68} = \frac{1}{22} \approx 4.545\%$, so the minimum is $\frac{250000}{22} \approx 11{,}363.64$ dollars.

Check: 5.40% is above 4.545%, and the minimum factor rises with age, as it should.

</details>

### Challenge

7\. Prove the break-even formula $T = \frac{b_2a_2 - b_1a_1}{b_2 - b_1}$ for starting a pension at age $a_1$ for $b_1$ a month or at age $a_2 > a_1$ for $b_2 > b_1$ a month, ignoring interest. Then apply it to \$1,000 at 65 against \$1,420 at 70.

<details class="solution" markdown>
<summary>Solution</summary>

By age $T$ (with $T > a_2$) the total received is $12b_1(T - a_1)$ for the early start and $12b_2(T - a_2)$ for the late start. They are equal when $b_1(T - a_1) = b_2(T - a_2)$, that is, $b_1T - b_1a_1 = b_2T - b_2a_2$. Collecting the terms in $T$ gives $(b_2 - b_1)T = b_2a_2 - b_1a_1$, and dividing by $b_2 - b_1 > 0$ gives the formula. $\blacksquare$

For \$1,000 at 65 and \$1,420 at 70: $T = \frac{1420 \times 70 - 1000 \times 65}{420} = \frac{34400}{420} \approx 81.9$.

Check: at $T = 81.9$ the early start has received $1000 \times 16.9 \times 12 = 202{,}800$ and the late start $1420 \times 11.9 \times 12 = 202{,}776$, equal up to rounding.

</details>

8\. (Reviews [logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md).) A TFSA holds \$109,000 and grows at a real 4% a year with no further contributions. How many years until it passes \$200,000?

<details class="solution" markdown>
<summary>Solution</summary>

We need $109000 \times 1.04^n = 200000$, so $n = \frac{\ln(200000 / 109000)}{\ln 1.04} = \frac{0.6070}{0.03922} \approx 15.48$ years. So the balance passes \$200,000 during year 16.

Check: $109000 \times 1.04^{15} \approx 196{,}303$, which is under \$200,000, and $109000 \times 1.04^{16} \approx 204{,}155$, which is over.

</details>

## Where this shows up

- The tax side of the comparison is in [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md), and the mortgage side of the FHSA is in [renting vs buying a home](../05-housing/01-renting-vs-buying-a-home.md).
- The 4% rule and the CPP choice are annuity problems, like the ones in [annuities and geometric series](../03-time-value-of-money/02-annuities-and-geometric-series.md). Break-even ages are the same kind of calculation as the break-even point in a linear model.
- In economics the question "pay tax now or later" is a question about the present value of a stream, which comes back in [present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md).
