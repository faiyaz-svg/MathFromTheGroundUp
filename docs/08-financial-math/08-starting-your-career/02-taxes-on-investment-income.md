# Taxes on investment income

After this lesson you can work out the 2026 federal and Ontario tax on interest, eligible dividends and capital gains, track the adjusted cost base of shares you buy in several lots, use a capital loss and spot a superficial loss, and compare what the same investment keeps after tax in a TFSA and in an ordinary account.

Before this: [investing returns and risk](../06-investing-and-retirement/01-investing-returns-and-risk.md), [retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md), [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md) and [Comparing job offers](01-comparing-job-offers.md).

All people and holdings in this lesson are made up, and the growth rates are examples, not forecasts. The tax figures are for 2026, with the sources linked where they are used. The lesson explains the math of the rules. It is not tax advice.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. You earn \$1,000 of interest in an ordinary account, and your next dollar is taxed at a combined 29.65%. How much tax is that?
2. A company pays you an eligible dividend of \$1,000 in cash. What amount goes on your tax return?
3. You sell shares for a capital gain of \$1,000. How much of it is taxable, and what is the tax at 29.65%?

<details class="solution" markdown>
<summary>Answers</summary>

1. Interest is taxed in full: $0.2965 \times 1000 = 296.50$ dollars.
2. The cash is grossed up by 38%: $1.38 \times 1000 = 1380$ dollars goes on the return.
3. The inclusion rate is 50%, so \$500 is taxable, and the tax is $0.2965 \times 500 = 148.25$ dollars.

</details>

## The idea

A savings account, a share of a company and a bond all pay you in different ways, and the tax system treats each way differently. Money lent out earns interest. A company that makes a profit can pay part of it to its shareholders as a dividend. A share that rises in price gives you a gain, but only on the day you sell.

Take an Ontario employee on \$65,000, the one from [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md), whose next dollar is taxed at 29.65%. On \$1,000 of interest they owe \$296.50. On \$1,000 of eligible dividends they owe \$63.90. On a \$1,000 capital gain they owe \$148.25. Three kinds of income with the same \$1,000 face value leave the investor \$703.50, \$936.10 and \$851.75. A TFSA charges none of the three.

Where do the odd numbers come from? Dividends are paid out of profit that the company has already paid corporate tax on, so the system adds a markup to the dividend and then gives credits to make up for the corporate tax. A gain is taxed at half the rate of other income. This lesson works out both rules with the 2026 figures, shows the one formula that ties them together, and then asks which account should hold which kind of income.

## Definitions

**Interest income** is a payment for lending money, such as the interest on a savings account, a bond or a guaranteed investment certificate (GIC). It is added to your income in full. In plain words, \$1 of interest is taxed like \$1 of salary.

A **dividend** is a payment a corporation makes to its shareholders out of its profit. An **eligible dividend** is one that the corporation paid from income taxed at the general corporate rate, which includes most dividends from public companies. This lesson covers eligible dividends only.

The **gross-up** is the amount added to the cash dividend before it is taxed. For eligible dividends it is 38%, so the taxable amount is $1.38 \times$ the cash. The **dividend tax credit** is a non-refundable credit based on the grossed-up amount. In plain words, the markup pretends you received the profit before the company's tax, and the credit gives back the company's tax.

A **capital gain** is the amount by which the proceeds from selling a capital property, such as shares, exceed its adjusted cost base plus the selling costs. A **capital loss** is the same calculation with a negative result. The **inclusion rate** is the fraction of a gain that is taxable. The **taxable capital gain** is the gain times the inclusion rate, and an **allowable capital loss** is the loss times the inclusion rate.

The **adjusted cost base** (ACB) of a property is its cost plus the expenses of buying it, adjusted for later events. For shares of the same company and class, called **identical properties**, the ACB is the **average cost**: the total cost of all the shares you own divided by the number you own. In plain words, the ACB is what you are treated as having paid, and the gain is what you get above it.

A **superficial loss** is a capital loss that the rules deny because you, or someone affiliated with you, bought the same or identical property in the window from 30 days before the sale to 30 days after it and still held it 30 days after the sale. A **non-registered account** is an ordinary investment account with no tax shelter.

## How to do it

### The 2026 figures

Interest is reported in full. For a compound-interest GIC, the CRA requires you to report the interest earned in each complete investment year, even if it is paid only at maturity ([CRA, line 12100](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12100-interest-other-investment-income.html)).

For eligible dividends the CRA gives these figures when you have no slip: multiply the amount received by 138% and report it on line 12000 ([CRA, lines 12000 and 12010](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12000-taxable-amount-dividends-eligible-other-than-eligible-taxable-canadian-corporations.html)). The federal credit is 15.0198% of that taxable amount ([CRA Federal Worksheet](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf)), and the Ontario credit is 10% of it ([CRA Worksheet ON428](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-d/5006-d-25e.pdf); Ontario lists 10.0% for the years 2020 to 2026 at [ontario.ca](https://www.ontario.ca/page/ontario-dividend-tax-credit)). On a T5 slip, box 24 shows the actual eligible dividend, box 25 the taxable amount and box 26 the federal credit ([CRA, T5 slip](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/tax-slips/understand-your-tax-slips/t5-slips/t5-statement-investment-income-slip-information-individuals.html)). Dividends from foreign corporations do not qualify for the federal credit ([CRA, line 40425](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-40425-federal-dividend-tax-credit.html)).

For capital gains, the CRA's guide gives an inclusion rate of 50% for every year from 2001 to 2025 ([CRA, capital gains guide T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)). A proposal to raise it to two-thirds for gains over \$250,000 was cancelled: the Prime Minister announced the cancellation on March 21, 2025 ([Prime Minister of Canada](https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase)), and the Department of Finance's 2026 tax expenditures report says the government confirmed in Budget 2025 that it would not proceed ([Finance Canada](https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-2.html)). As of 2026 the inclusion rate is 50%.

<div class="note" markdown>

These figures are for 2026 and change every year. Check the linked pages before using them for real decisions. The credits above are the 2025 worksheet values, and the Ontario page lists the same 10.0% through 2026.

</div>

### Interest, dividends and gains, step by step

1. Find your marginal rates. Take the federal rate $r_f$ and the Ontario rate $r_o$ of the brackets that your next dollar falls in, from [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md). Above about \$100,000 of income the Ontario surtax multiplies the Ontario tax, and the calculator in that lesson handles it.
2. Interest. Add it to income. The extra tax is $(r_f + r_o)$ times the interest.
3. Eligible dividends. Multiply the cash by 1.38 and add that to income. Tax it at $r_f$ and $r_o$. Subtract the federal credit, $0.150198 \times$ the grossed-up amount, and the Ontario credit, $0.10 \times$ the grossed-up amount. A credit can only cancel tax: it cannot make the total tax negative.
4. Capital gains. Find the gain as proceeds minus ACB minus selling costs. Add half of it to income and tax it at $r_f$ and $r_o$. Gains are only taxed in the year you sell, so growth you have not sold is not taxed yet.
5. Losses. A capital loss is first set against capital gains of the same year. A net capital loss for the year, after that, can be carried back to any of the three previous years or forward to any future year, and it applies only against taxable capital gains ([CRA, T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)).
6. Check by running the whole return through the calculator with and without the investment income.

### One formula for the three rates

*Theorem 1 (the three rates).* Suppose the next dollar of taxable income is taxed at the federal rate $r_f$ and the Ontario rate $r_o$, with no Ontario surtax, and your other tax is large enough to use every credit. Let $r = r_f + r_o$. An extra cash amount $X$ received as interest, as an eligible dividend or as a realized capital gain adds this much tax:

$$
T_{\text{interest}} = r\,X, \qquad T_{\text{dividend}} = 1.38\,(r - 0.250198)\,X, \qquad T_{\text{gain}} = 0.5\,r\,X.
$$

The dividend is taxed less than the gain exactly when $r < 0.39236$.

We know how each kind of income enters the return and what the credits are. We want the extra tax per dollar of cash. The plan is to compute the added taxable income for each kind, tax it at $r$, and subtract the credits.

*Proof.* Interest adds $X$ to taxable income, which is taxed at $r_f + r_o$, so the tax is $rX$. A gain adds only $0.5X$ to taxable income, so the tax is $0.5rX$. A dividend adds $1.38X$ to taxable income, so the tax before credits is $1.38rX$. The credits are $0.150198 \times 1.38X$ federally and $0.10 \times 1.38X$ in Ontario, which add to $0.250198 \times 1.38X$. The tax is $1.38rX - 0.250198 \times 1.38X = 1.38(r - 0.250198)X$. For the comparison, the dividend rate is below the gain rate when $1.38(r - 0.250198) < 0.5r$, that is, $0.88r < 1.38 \times 0.250198 = 0.345273$, so $r < 0.39236$. $\blacksquare$

Look back: at $r = 0.2965$ the dividend rate is $1.38 \times 0.046302 = 6.39\%$, so the result is the \$63.90 per \$1,000 in the idea section. Below $r = 0.250198$ the formula gives a negative number, which is Example 3: the credits cannot refund tax you do not owe. At a higher $r$ the order of dividends and gains switches. The surtax changes the Ontario part of $r$ but not the 10% credit, so at a \$120,000 salary the calculator gives \$434.10 on \$1,000 of interest, \$253.78 on \$1,000 of dividends and \$217.05 on \$1,000 of gains.

![Tax on an extra 1,000 dollars of interest, eligible dividends and capital gains against salary, from 12 to 250 thousand dollars. Interest is taxed the most: about 190 dollars at 30 thousand, 296.50 at 65 thousand and 434 at 120 thousand. Capital gains are half of that. Eligible dividends start below zero, at minus 82 dollars at 30 thousand, because the credits cancel tax on other income, rise to 63.90 at 65 thousand, and pass capital gains near 117 thousand, reaching about 340 dollars above 220 thousand.](../../assets/figures/08-financial-math/taxes-on-investment-income-by-type.svg)

The figure uses the 2026 federal and Ontario rates, the basic credits, the surtax and the dividend credits, and leaves out the Ontario Health Premium.

### Adjusted cost base and the superficial loss rule

For identical properties the CRA's rule is to calculate the average cost at each purchase: the total cost of the shares you own divided by their number. Selling shares does not change the average cost of the shares that remain ([CRA, T4037](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4037/capital-gains.html)). Shares in the same company bought at different times are one pool, so you do not match a sale to a particular lot as first-in first-out would.

A superficial loss cannot be deducted in the year of the sale. The CRA says that the loss can usually be added to the ACB of the substituted property, which lowers a later gain or raises a later loss. So a superficial loss is postponed and not lost. The CRA lists affiliated persons, for example you and your spouse or common-law partner, among those whose purchases count.

### Which account should hold what

The same \$1,000 of income is taxed at three different rates, and a TFSA removes all three. Ranking by the tax saved per dollar of income, the order at a \$65,000 salary is interest (\$296.50 saved), then a realized gain (\$148.25), then eligible dividends (\$63.90). At \$120,000 the order of the last two switches (\$253.78 for dividends and \$217.05 for gains), and interest is still first. An RRSP is different: withdrawals are taxed as ordinary income whatever the investment earned, so inside an RRSP a dividend or a gain loses its credit and its half inclusion. Dividends from foreign companies get no federal credit, so they are taxed like interest. Registered accounts also have limited room, so the question is always which holdings use the room best, as in [retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md).

A comparison over 20 years shows how big the difference gets. Take \$10,000 at a total return of 6% a year, a combined marginal rate of 29.65% and the dividend rate of 6.39% on every year's dividend.

| Account | What it earns | After 20 years |
|---|---|---|
| Non-registered | 6% as interest, taxed every year | \$22,861.50 |
| Non-registered | 3% dividends (taxed each year and reinvested) and 3% price growth, sold at the end | \$29,328.39 |
| Non-registered | 6% price growth only, sold at the end | \$28,799.28 |
| TFSA | 6% any way, nothing taxed | \$32,071.35 |

The interest account keeps an after-tax rate of $0.06 \times (1 - 0.2965) = 4.221\%$ a year, and compounding does the rest. The gap between the TFSA and the interest account is \$9,209.85, which is 28.7% of the TFSA balance.

## Worked examples

<div class="example" markdown>

### Example 1: three kinds of income at \$65,000

An Ontario employee with a \$65,000 salary (taxable income \$64,385, marginal rates 20.5% and 9.15%) receives \$2,000 of interest, \$1,500 of eligible dividends in cash and sells shares for a \$3,000 gain, all in the same year.

Step 1: the bracket rates are $r_f = 0.205$ and $r_o = 0.0915$, so $r = 0.2965$. After adding the income, taxable income is $64385 + 2000 + 2070 + 1500 = 69955$ dollars (the dividend counts at its grossed-up amount, step 3). That stays above \$58,523 and below \$107,785, and inside the \$48,000 to \$72,000 Health Premium band, so the rates and the premium do not change.

Step 2: interest. The tax is $0.2965 \times 2000 = 593.00$ dollars.

Step 3: dividends. The grossed-up amount is $1.38 \times 1500 = 2070$ dollars. The tax before credits is $0.205 \times 2070 = 424.35$ federally and $0.0915 \times 2070 = 189.41$ in Ontario. The credits are $0.150198 \times 2070 = 310.91$ and $0.10 \times 2070 = 207.00$. The net tax is $424.35 - 310.91 + 189.41 - 207.00 = 95.85$ dollars.

Step 4: the gain. Half of \$3,000 is \$1,500 taxable, and the tax is $0.2965 \times 1500 = 444.75$ dollars.

The total extra tax is $593.00 + 95.85 + 444.75 = 1133.60$ dollars on \$6,500 of cash, so the investor keeps \$5,366.40, which is 82.6%.

Step 6, check: the calculator from the tax lesson, run with and without the three amounts, gives the same extra tax, \$1,133.60. If the whole \$6,500 had been interest, the tax would have been $0.2965 \times 6500 = 1927.25$ dollars, which is \$793.65 more.

</div>

<div class="example" markdown>

### Example 2: average cost and a loss in the same year

You receive 480 shares of your employer from RSUs, delivered when they were worth \$25.00 each, so the ACB of those shares is $480 \times 25 = 12000$ dollars ([Comparing job offers](01-comparing-job-offers.md) explains why). Later you buy 120 more shares of the same company at \$31.00 each, for \$3,720.

The 600 shares are one pool. The total cost is $12000 + 3720 = 15720$ dollars, so the ACB is $\frac{15720}{600} = 26.20$ dollars a share. You sell 200 shares at \$30.00, for proceeds of \$6,000 (ignoring commissions). The ACB of those 200 is $200 \times 26.20 = 5240$ dollars, so the gain is $6000 - 5240 = 760$ dollars and the taxable part is \$380. At 29.65% the tax is $0.2965 \times 380 = 112.67$ dollars. The 400 shares that remain still have an ACB of \$26.20 each, \$10,480 in total.

First-in first-out would treat the 200 shares as part of the first lot with an ACB of \$25.00, and give a gain of \$1,000. That is the wrong method in Canada, and it overstates the gain by \$240.

Later in the same year you sell the other 400 at \$24.00. The loss is $400 \times (24 - 26.20) = -880$ dollars. Together with the \$760 gain, the result for the year is $760 - 880 = -120$ dollars, so there is a net capital loss of \$120 and an allowable capital loss of \$60. No tax is owing on the shares for the year, and the net capital loss can be carried back three years or forward against taxable capital gains.

Check: the cost of all 600 shares is \$15,720, and they were sold for $6000 + 9600 = 15600$ dollars, a total loss of \$120.

</div>

<div class="example" markdown>

### Example 3: dividends at a low income

An employee has a salary of \$30,000. Their 2026 federal tax is \$1,397.38 and their Ontario tax is \$754.74 (Practice 4 of the tax lesson works this out). They receive an eligible dividend of \$1,000.

The grossed-up amount is \$1,380. Federally, the tax on it is $0.14 \times 1380 = 193.20$ and the credit is $0.150198 \times 1380 = 207.27$, a change of $-14.07$. In Ontario, the tax is $0.0505 \times 1380 = 69.69$ and the credit is \$138.00, a change of $-68.31$. The total change is $-14.07 - 68.31 = -82.38$ dollars. The dividend lowers the tax bill by \$82.38, because the credits are used against the tax on the salary.

This only works while there is tax to cancel. With a salary of \$15,000, the federal tax is already \$0 and the Ontario tax is \$54.65, so the dividend takes the Ontario tax to \$0 and the rest of the credits, \$207.27 federally and \$13.66 in Ontario, are unused. Total tax falls only by \$54.65. Credits are not refunded.

Check: Theorem 1 gives $1.38 \times (0.1905 - 0.250198) \times 1000 = -82.38$ dollars, with $r = 0.14 + 0.0505 = 0.1905$.

</div>

<div class="example" markdown>

### Example 4: a superficial loss (finish it yourself)

You own 200 shares with a total ACB of \$6,000 (\$30.00 each). On November 20, 2026 you sell all 200 at \$24.00 for \$4,800, hoping to claim the loss. On December 5, 2026, 15 days later, you buy 200 shares of the same company for \$5,000 (\$25.00 each) and still hold them on December 20. The window for the sale runs from October 21 to December 20.

Step 1: the purchase is inside the window and you still hold the shares 30 days after the sale, so the loss of $6000 - 4800 = 1200$ dollars is a superficial loss. You cannot deduct it in 2026.

Now find the ACB of the new shares, and the gain when you sell all 200 of them for \$33.00 each in a later year. Compare it with the gain you would have had if the \$1,200 loss had been allowed.

<details class="solution" markdown>
<summary>Finish</summary>

The denied loss is added to the ACB of the new shares: $5000 + 1200 = 6200$ dollars, or \$31.00 a share. A later sale at \$33.00 gives proceeds of \$6,600 and a gain of $6600 - 6200 = 400$ dollars. Without the rule, the ACB would be \$5,000 and the gain \$1,600.

Check: the \$1,200 reappears as a lower gain, \$400 instead of \$1,600. If you had waited until December 21 (31 days after the sale) to buy back, the loss would have been allowed in 2026.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: taxing the dividend you receive. The tax is on the grossed-up amount, \$1,380 for a \$1,000 dividend, and the credits are also based on \$1,380. Using \$1,000 for both would give $0.2965 \times 1000 - 0.250198 \times 1000 = 46.30$ dollars instead of \$63.90.

</div>

<div class="warning" markdown>

Watch out: believing a dividend is "always taxed less". Theorem 1 says the dividend rate is below the capital gains rate only while your combined marginal rate is under about 39.2%. At a \$120,000 salary, dividends cost \$253.78 per \$1,000 and gains \$217.05.

</div>

<div class="warning" markdown>

Watch out: using first-in first-out. For shares of the same company, the ACB is the average cost of the whole pool, and a sale does not change the average cost of what remains.

</div>

<div class="warning" markdown>

Watch out: buying back too soon. A repurchase of the same shares inside the 61-day window (30 days before to 30 days after the sale) denies the loss for now. The rule is about identical property, and whether two similar funds count as identical depends on their details, which the math here cannot settle.

</div>

<div class="warning" markdown>

Watch out: assuming the gross-up is only a tax detail. Line 12000 holds the grossed-up amount, so anything that depends on your net income sees \$1,380 for a \$1,000 dividend.

</div>

A capital gain is taxed only when you sell, so unsold growth costs nothing this year, but it has not escaped tax, and a later sale is taxed with the rates of that year. Interest in a TFSA, an RRSP or an FHSA is not reported on your return, and the account's own rules decide the tax when money comes out. This lesson assumes a resident of Ontario with Canadian investments. Foreign investments bring foreign withholding tax and currency rules that it leaves out.

## Tricks and shortcuts

Keep three numbers for an Ontario earner around \$65,000: a dividend keeps about 94 cents on the dollar, a gain about 85 cents and interest about 70 cents, as in the idea section. At a \$120,000 salary the numbers are about 75 cents, 78 cents and 57 cents.

Quick ACB: new average cost = (old total cost + new cost) $\div$ (old shares + new shares). Selling leaves the per-share average alone, so the cost left is the shares left times the average.

A TFSA or an RRSP does not need any of this tracking, because gains and dividends inside it are not reported. In a non-registered account, keep the confirmation of every purchase and sale, since you need them to support your ACB.

## In code

The code shows the three rates of Theorem 1 at a \$65,000 salary, tracks the average cost of the RSU shares in Example 2, and compares 20 years of growth in four settings. Every printed value matches the lesson.

<details class="code" markdown>
<summary>In code</summary>

```python
# Theorem 1 at a $65,000 salary: federal 20.5%, Ontario 9.15%, no surtax (2026).
rf, ro = 0.205, 0.0915
r = rf + ro
t_interest = r
t_dividend = 1.38 * ((rf - 0.150198) + (ro - 0.10))   # gross-up 38%, then both credits
t_gain = 0.5 * r
print(round(1000 * t_interest, 2), round(1000 * t_dividend, 2), round(1000 * t_gain, 2))   # 296.5 63.9 148.25

# Average cost: 480 shares at $25.00 (RSUs), then 120 shares at $31.00.
shares, cost = 480, 480 * 25.00
shares, cost = shares + 120, cost + 120 * 31.00
acb = cost / shares
gain = 200 * 30.00 - 200 * acb              # sell 200 at $30.00
print(round(acb, 2), round(gain, 2), round(0.5 * gain * r, 2))   # 26.2 760.0 112.67

# 20 years of $10,000 growing at 6% a year in four settings.
P, n = 10_000.0, 20
t_gain_sale = 0.5 * r                              # tax rate on a gain realized at the end
interest = P * (1 + 0.06 * (1 - t_interest)) ** n

value, base = P, P                                 # 3% dividends reinvested after tax, 3% price growth
for _ in range(n):
    after_tax_dividend = 0.03 * value * (1 - t_dividend)
    value = value * 1.03 + after_tax_dividend
    base += after_tax_dividend                     # reinvested dividends raise the ACB
dividend_stock = value - t_gain_sale * (value - base)

growth = P * 1.06 ** n
growth_only = growth - t_gain_sale * (growth - P)
tfsa = P * 1.06 ** n
print(round(interest, 2), round(dividend_stock, 2), round(growth_only, 2), round(tfsa, 2))
# 22861.5 29328.39 28799.28 32071.35
```

The last line shows the four results: the interest account, the dividend stock, the growth-only stock and the TFSA. The dividend stock finishes ahead of the growth-only stock here because, at this income, dividends are taxed at 6.39% a year while the gain is taxed at 14.8% at the end. Change `rf` and `ro` to see how the order depends on the rates. The code ignores the Ontario surtax and the Health Premium.

</details>

## FAQ

### Why is there a gross-up at all?

A corporation pays tax on its profit before it can pay a dividend. If the shareholder paid full tax on the dividend as well, the same profit would be taxed twice. Ontario's page on the credit says that the federal and provincial dividend tax credits are intended to compensate individual shareholders for income tax paid by the companies they invest in ([ontario.ca](https://www.ontario.ca/page/ontario-dividend-tax-credit)). The gross-up raises the dividend toward the profit before corporate tax, and the credit gives back some of that tax.

### Why is a capital gain only half taxed?

The law counts half of a gain as income, and the CRA's table shows 50% for every year from 2001 to 2025. The size of the inclusion rate is a policy choice and not a mathematical fact, and a proposal to raise it for large gains was cancelled in 2025. Rates can change again, so check the CRA's current page before relying on a figure.

### Is a superficial loss gone forever?

No. The denied loss is added to the ACB of the shares you bought back, so it reduces the gain or increases the loss when you finally sell them (Example 4).

### Should I hold dividend stocks in my TFSA or in an ordinary account?

The math says what each choice saves. In the ordinary account an eligible dividend costs about \$63.90 per \$1,000 at \$65,000 (Theorem 1), and in a TFSA it costs nothing. The TFSA limit is \$7,000 for 2026 ([retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md)), so the room is limited, and interest saves the most tax per dollar of income. Which holdings to put where also depends on your goals and risk, and this lesson does not tell you what to hold.

## Practice

### Warm-up

1\. You receive an eligible dividend of \$2,000 in cash. Find the grossed-up amount, the federal credit and the Ontario credit.

<details class="solution" markdown>
<summary>Solution</summary>

The grossed-up amount is $1.38 \times 2000 = 2760$ dollars. The federal credit is $0.150198 \times 2760 = 414.55$ dollars, and the Ontario credit is $0.10 \times 2760 = 276.00$ dollars.

Check: the credits together are $0.250198 \times 2760 = 690.55$, and $414.55 + 276.00 = 690.55$.

</details>

2\. You buy 50 shares at \$40 and later 150 shares of the same company at \$48. Find the ACB per share. Then you sell 100 shares at \$55. Find the capital gain and the taxable capital gain.

<details class="solution" markdown>
<summary>Solution</summary>

The total cost is $50 \times 40 + 150 \times 48 = 2000 + 7200 = 9200$ dollars for 200 shares, so the ACB is $\frac{9200}{200} = 46.00$ dollars. The gain on 100 shares is $100 \times (55 - 46) = 900$ dollars, and the taxable part is $0.5 \times 900 = 450$ dollars.

Check: the remaining 100 shares have an ACB of $100 \times 46 = 4600$ dollars, and the sold shares had $4600$ too, which adds to the \$9,200.

</details>

3\. In one year you sell shares at a loss of \$2,000 and other shares at a gain of \$5,000. Find the net capital gain and the taxable capital gain.

<details class="solution" markdown>
<summary>Solution</summary>

The net capital gain is $5000 - 2000 = 3000$ dollars, and the taxable capital gain is $0.5 \times 3000 = 1500$ dollars.

Check: the same answer comes from $0.5 \times 5000 - 0.5 \times 2000 = 2500 - 1000 = 1500$.

</details>

### Standard

4\. You sell 100 shares at a loss on March 10, 2026. Which of these repurchases of the same shares would make the loss superficial, assuming you keep them for at least 30 days: February 5, February 10, April 9, April 10?

<details class="solution" markdown>
<summary>Solution</summary>

The window runs from 30 days before to 30 days after March 10, that is, from February 8 to April 9, 2026. February 10 and April 9 are inside it, so those repurchases make the loss superficial. February 5 is 33 days before the sale, and April 10 is 31 days after it, so those are outside.

Check: March 10 minus 30 days is February 8 (February 2026 has 28 days: March 10 is day 69 of the year, and day 39 is February 8), and March 10 plus 30 days is April 9.

</details>

5\. An employee with a \$65,000 salary gets \$3,000 in dividends from a foreign company, with no foreign tax withheld, and another employee gets \$3,000 in eligible dividends from a Canadian company. Compare the extra tax, using the combined rate of 29.65%.

<details class="solution" markdown>
<summary>Solution</summary>

The foreign dividend gets no federal credit and, for this lesson, is taxed like interest: $0.2965 \times 3000 = 889.50$ dollars. The eligible dividend is grossed up to $1.38 \times 3000 = 4140$ dollars and the tax is $4140 \times (0.2965 - 0.250198) = 4140 \times 0.046302 = 191.69$ dollars. The foreign dividend costs \$697.81 more.

Check: Theorem 1 gives $1.38 \times 0.046302 \times 3000 = 191.69$, and $889.50 - 191.69 = 697.81$.

</details>

6\. You invest \$5,000 for 10 years at 5% a year. In an ordinary account the 5% is interest, taxed each year at 29.65%. In a TFSA it is not taxed. Find the two final balances and the difference.

<details class="solution" markdown>
<summary>Solution</summary>

The TFSA grows at 5%: $5000 \times 1.05^{10} = 8144.47$ dollars. The ordinary account keeps $0.05 \times (1 - 0.2965) = 3.5175\%$ a year: $5000 \times 1.035175^{10} = 7064.93$ dollars. The difference is $8144.47 - 7064.93 = 1079.54$ dollars.

Check: the ordinary account earns 3.5175% a year against 5%, so its balance has to be lower, and $1.035175^{10} = 1.41299$ against $1.05^{10} = 1.62889$.

</details>

### Challenge

7\. Use Theorem 1 to find the combined marginal rate $r$ at which an eligible dividend and a capital gain of the same size are taxed equally, and the tax on \$1,000 at that rate.

<details class="solution" markdown>
<summary>Solution</summary>

Set $1.38(r - 0.250198) = 0.5r$. Then $1.38r - 0.345273 = 0.5r$, so $0.88r = 0.345273$ and $r = 0.39236$. The rate on each is $0.5 \times 0.39236 = 0.19618$, so the tax on \$1,000 is \$196.18 for either one.

Check: $1.38 \times (0.39236 - 0.250198) = 1.38 \times 0.142162 = 0.19618$. Below $r = 0.39236$ the dividend is cheaper and above it the gain is.

</details>

8\. (Reviews [inflation and real returns](../02-interest-and-growth/06-inflation-and-real-returns.md).) A GIC pays 4.5% interest in an ordinary account, your combined marginal rate is 29.65% and inflation is 2.5%. Find the after-tax rate and the after-tax real return, and compare the real return with the one before tax.

<details class="solution" markdown>
<summary>Solution</summary>

The after-tax rate is $0.045 \times (1 - 0.2965) = 0.0316575$, about 3.17%. The real return after tax is $\frac{1.0316575}{1.025} - 1 = 0.00650$, about 0.65%. Before tax it is $\frac{1.045}{1.025} - 1 = 0.01951$, about 1.95%.

Check: tax takes 29.65% of the nominal return and about two thirds of the real return, since $\frac{1.95 - 0.65}{1.95} = 67\%$, because inflation is not deducted before the tax is calculated.

</details>

## Where this shows up

- The side income of a freelancer or a gig worker is taxed in yet another way: see [Side gigs and self-employment](03-side-gigs-and-self-employment.md).
- The tax calculator in [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md) takes these three kinds of income as extra inputs, and the account rules are in [retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md).
- Computing: the ACB is a running average that updates on each purchase, and the superficial loss rule is a sliding window over a transaction log.
