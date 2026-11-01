# Side gigs and self-employment

After this lesson you can work out the CPP and income tax on freelance income in Ontario for 2026, say when GST/HST registration and tax instalments start, decide how much of each payment to set aside, and find the hourly rate that matches a salary.

Before this: [tips, discounts and HST](../01-everyday-money/01-tips-discounts-and-hst.md), [paycheques and budgeting](../01-everyday-money/03-paycheques-and-budgeting.md) and [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md).

All people and clients in this lesson are made up. The figures are the 2026 ones from the earlier lessons, with the sources linked where they are new. The lesson explains the math and is not tax advice.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A freelancer with no other job has a net business income of \$40,000 in 2026. Using the 2026 self-employed CPP rate of 11.9% above the \$3,500 exemption, find the CPP.
2. A freelancer's revenue in four consecutive quarters is \$7,000, \$7,500, \$8,000 and \$8,500. Are they still under the \$30,000 GST/HST limit?
3. A client pays \$1,130, which includes 13% HST. How much of it is HST?

<details class="solution" markdown>
<summary>Answers</summary>

1. $0.119 \times (40000 - 3500) = 4343.50$ dollars.
2. The four quarters add to \$31,000, which is over \$30,000, so no.
3. Divide by 1.13 to remove the tax: $1130 \div 1.13 = 1000$, so the HST is \$130.

</details>

## The idea

A salary arrives after the employer has done the arithmetic. It has taken off CPP, EI and income tax, paid its own half of CPP and EI, and sent everything to the government. A freelance payment arrives whole. Nobody has taken anything off it, and every deduction becomes your job.

So there are four questions. How much of the money is really income, after expenses? What do CPP and income tax take from it? Does the HST apply, and when do you have to start paying tax during the year and not in April? Then the question the first three lead to: what hourly rate leaves you as well off as a salary would? The answers are the same percent-of-what arithmetic as before, with one change. As an employee you pay half of CPP and the employer pays the other half. As a self-employed person you are both.

## Definitions

**Net business income** is revenue minus deductible expenses. In plain words, it is what is left of the money that came in after the cost of earning it, and it is the amount that is taxed.

A **deductible expense** is a reasonable current expense you incur to earn income. Personal expenses are not deductible, so only the business part of a mixed expense counts ([CRA, guide T4002, expenses](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-5.html)). Buying capital property, such as a laptop, is not deducted in one go: its cost is deducted over several years through **capital cost allowance**. The limit on meals is 50% of the amount, and the part of home costs for a work space is limited to a reasonable share and cannot create a loss.

**Self-employed CPP** is the CPP you pay on net business income. You pay the employee and the employer shares: 11.9% of earnings between the \$3,500 exemption and \$74,600, up to \$8,460.90 in 2026, and 8% on earnings from \$74,600 to \$85,000, up to \$832.00 ([CRA, CPP rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) and [CPP2 rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html), both dated October 30, 2026).

A **small supplier** is a person whose revenue from taxable supplies was \$30,000 or less in a single calendar quarter and over the last four consecutive calendar quarters. A small supplier does not have to register for GST/HST ([CRA, RC4022](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html)). A **registrant** charges the tax and remits it, minus the **input tax credits** for the tax paid on business expenses.

A tax **instalment** is a payment toward this year's tax made during the year. The **set-aside rate** is the share of each payment you keep aside for CPP and tax.

## How to do it

### Net business income and the expenses

1. Add up revenue for the year, before expenses and before any HST you collected for the government.
2. Subtract expenses that are reasonable, current and for the business. Take the business part of mixed costs, 50% of meals, and leave capital purchases for capital cost allowance. The deductible amount includes any GST/HST you paid on an expense and did not claim back as a credit ([CRA, T4002](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-5.html)).
3. The result is net business income. If you also have a job, it is added to your employment income.

### CPP on self-employment income

Let $E$ be your employment income and $N$ your net business income. The CPP room for the year is shared, and the \$3,500 exemption is used once. Your employer's payroll uses up the contributory earnings $\min(E, 74600) - 3500$ first, and the business income fills what is left under \$74,600. Let $c$ be the contributory earnings of the business income and $s$ the part of it in the second tier. For the usual case of a salary of at least \$3,500 and below \$74,600:

$$
c = \min(E + N,\ 74600) - E, \qquad s = \max\bigl(0,\ \min(E + N,\ 85000) - 74600\bigr).
$$

The CPP on the business income is $0.119\,c + 0.08\,s$. The CRA's Schedule 8 does the same calculation when you have both kinds of income ([CRA Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf)).

For the income tax, the CRA says to claim a non-refundable credit on 4.95% of the base contributions and a deduction on the other 4.95%, a deduction on the 2% enhanced portion, and a deduction on all of the CPP2 ([CRA, CPP enhancement](https://www.canada.ca/en/revenue-agency/news/2023/05/the-canada-pension-plan-enhancement--businesses-individuals-and-self-employed-what-it-means-for-you.html)). So the deduction is $0.0695\,c + 0.08\,s$, and the credit is on $0.0495\,c$.

There is no EI on business income. A self-employed person can opt in to EI special benefits, such as maternity, parental and sickness benefits. They then pay the employee premium rate and no employer share, and a minimum amount of self-employed earnings is required (\$9,254 for 2026) ([Employment and Social Development Canada, 2026 actuarial report](https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/reports/premium/rates2026.html)).

### Income tax, instalments and deadlines

Add the net business income to your other income, subtract the CPP deduction, and run the 2026 calculator from [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md). Self-employed people cannot claim the Canada employment amount. For the 2026 tax year the filing deadline is June 15, 2027, but a balance owing is due on April 30, 2027 ([CRA, 2027 tax deadlines](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html), page dated October 16, 2026).

You have to pay instalments for 2026 if your net tax owing is more than \$3,000 in 2026, and also more than \$3,000 in 2025 or in 2024. The due dates are March 15, June 15, September 15 and December 15. The CRA lets you base the payments on the CRA's own reminder, on the previous year, or on an estimate of the current year ([CRA, who has to pay](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html), [due dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html) and [options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html), all dated January 20, 2026). Net tax owing is the tax you owe after the tax already withheld at source. A first year with a big bill therefore has no instalments, but the bill is due on April 30, and the next year may have them.

### GST/HST and the \$30,000 limit

You do not have to register while you are a small supplier. The test uses revenue before expenses, and it has two parts: no single quarter above \$30,000 and no four consecutive quarters above \$30,000. If a single quarter goes over, you stop being a small supplier at once and must charge the tax on the sale that crossed the limit. If it is the four-quarter total, you stop being a small supplier at the end of the month after the quarter, and you must register within 29 days after your first sale as a registrant ([CRA, RC4022](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html), page dated January 7, 2026). The Ontario rate is 13%, as in [tips, discounts and HST](../01-everyday-money/01-tips-discounts-and-hst.md). The HST you collect is not income: it is held for the CRA.

### The share to set aside

The set-aside share is $\frac{\text{extra income tax} + \text{CPP}}{\text{net business income}}$, or the same amount over revenue if you want a share of each payment. It depends on your other income, because the extra income is taxed on top of it. An invoice with HST needs a second share, $\frac{13}{113} = 11.5\%$ of the amount paid, for the tax.

### The hourly rate that matches a salary

1. Start with the take-home pay of the salary you are comparing with, and add the yearly cost of the benefits you would have to buy yourself.
2. Solve for the net business income $N$ that leaves that amount after income tax and self-employed CPP. This needs the calculator, because the tax is not linear. A computer does it by bisection.
3. Add the yearly business expenses to get the required revenue $R$.
4. Divide $R$ by the billable hours, which are the hours you work times the share you can bill. Unpaid time off, and time spent on invoices and finding clients, are not billable.

## Worked examples

<div class="example" markdown>

### Example 1: a side gig on top of a salary

Ana (made up) has a \$65,000 salary, whose income tax was \$9,725.50 in [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md). She earns \$24,000 from freelance web work, with these deductible expenses.

| Expense | Amount spent | Deductible |
|---|---|---|
| Software and hosting | \$900.00 | \$900.00 |
| Phone plan, 30% for business | \$1,500.00 | \$450.00 |
| Client meals, at the 50% limit | \$800.00 | \$400.00 |
| Bookkeeping software | \$350.00 | \$350.00 |
| Liability insurance | \$300.00 | \$300.00 |
| Total | | \$2,400.00 |

A \$1,800 laptop is capital property, so it is left out and handled through capital cost allowance.

Steps 1 and 2 of the net income method: \$24,000 minus \$2,400 gives a net business income of \$21,600.

CPP: the payroll on her salary used $65000 - 3500 = 61500$ of contributory earnings, so $71100 - 61500 = 9600$ is left under the \$74,600 limit. That gives $c = 9600$ and a base CPP of $0.119 \times 9600 = 1142.40$ dollars. Her total of \$86,600 passes \$74,600 by more than the \$10,400 in the CPP2 tier, so $s = 85000 - 74600 = 10400$ and CPP2 is $0.08 \times 10400 = 832.00$. The self-employed CPP is \$1,974.40.

Tax: the CPP deduction is $0.0695 \times 9600 + 832 = 1499.20$ dollars, so taxable income rises from \$64,385 to $64385 + 21600 - 1499.20 = 84485.80$ dollars. The credit on $0.0495 \times 9600 = 475.20$ lowers the tax a little. The calculator gives a total income tax of \$15,744.86, which is \$6,019.36 more than before: about \$4,054 federal, \$1,815 Ontario and \$150 more Health Premium, because her taxable income passed \$72,000.

Set aside: $1974.40 + 6019.36 = 7993.76$ dollars, which is 37.0% of the net business income and 33.3% of the revenue. She keeps $21600 - 7993.76 = 13606.24$ dollars.

Check: her extra income is taxed at the 29.65% bracket rates and above, and the CPP is on top of that, so a set-aside near 37% of net income is plausible. Her CPP is only 9.1% of the business income ($\frac{1974.40}{21600}$), below 11.9%, because the \$3,500 exemption and part of the room were already used by her salary.

</div>

<div class="example" markdown>

### Example 2: the hourly rate that matches \$65,000

A job pays \$65,000 and its take-home pay is \$50,555.75 ([income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md)), for 2,080 paid hours, which is \$31.25 an hour. A freelancer wants the same take-home pay with no other job. Assume six weeks a year of unpaid time (vacation, holidays and sick days), so $46 \times 40 = 1840$ hours worked, and 75% of those hours billable, which is 1,380 hours. Business expenses are \$4,800 and benefits that the job would have given cost \$3,000 (made up), paid from take-home pay.

Step 1: the target after tax and CPP is $50555.75 + 3000 = 53555.75$ dollars.

Step 2: the calculator, with no employment income, gives the net business income that leaves this amount: \$73,017.03. Its self-employed CPP is \$8,272.53 and its income tax is \$11,188.75, and $73017.03 - 8272.53 - 11188.75 = 53555.75$.

Step 3: the revenue is $73017.03 + 4800 = 77817.03$ dollars.

Step 4: the hourly rate is $\frac{77817.03}{1380} = 56.39$ dollars, 1.80 times the job's \$31.25. With 13% HST added to an invoice, the client pays \$63.72 an hour.

The rate climbs in steps. \$65,000 over 1,840 hours worked is \$35.33; over 1,380 billable hours it is \$47.10; adding the \$7,800 of expenses and benefits it is \$52.75; and the remaining \$3.64 pays the second half of CPP and the tax on the extra income.

![Bars showing how the hourly rate grows from 31.25 dollars for the salary to 56.39 dollars for the freelancer: 35.33 after counting only the hours worked, 47.10 after counting only billable hours, 52.75 after adding expenses and benefits, and 56.39 after adding the extra CPP and tax.](../../assets/figures/08-financial-math/side-gigs-and-self-employment-bridge.svg)

Check: the unrounded rate times the hours is $56.3891 \times 1380 = 77816.96$, which is the \$77,817.03 of revenue up to the rounding of the rate.

</div>

<div class="example" markdown>

### Example 3: crossing \$30,000 over four quarters

Ana's quarterly revenue over six quarters is \$3,000, \$6,500, \$7,000, \$7,500, \$9,000 and \$9,500. Each quarter alone is far below \$30,000, so the question is the total of the last four.

| After quarter | Last four quarters | Small supplier? |
|---|---|---|
| 4 | \$24,000 | yes |
| 5 | \$30,000 | yes (equal to \$30,000 is not over) |
| 6 | \$33,000 | no |

After quarter 6 the total is over \$30,000, so Ana stops being a small supplier at the end of the month after that quarter. From then on she charges 13% HST. On a \$2,000 job she invoices \$2,000 plus \$260 of HST, \$2,260 in all. If she paid \$500 for supplies and \$65 of HST on them, she claims an input tax credit of \$65, so she remits $260 - 65 = 195$ dollars.

Check: the part of the \$2,260 payment that is not hers is $\frac{260}{2260} = 11.5\%$, the same as $\frac{13}{113}$.

</div>

<div class="example" markdown>

### Example 4: full-time freelancing (finish it yourself)

Dev (made up) has no job and a net business income of \$30,000.

Step 1: the CPP is $0.119 \times (30000 - 3500) = 3153.50$ dollars, and there is no CPP2.

Step 2: the deduction is $0.0695 \times 26500 = 1841.75$ dollars, so taxable income is $30000 - 1841.75 = 28158.25$ dollars. The credit amount for CPP is $0.0495 \times 26500 = 1311.75$.

Now find the federal tax, the Ontario tax, the \$300 Health Premium, and the set-aside share of the net business income.

<details class="solution" markdown>
<summary>Finish</summary>

Federal: $0.14 \times 28158.25 = 3942.16$ before credits, and the credits are $0.14 \times (16452 + 1311.75) = 2486.93$, so the federal tax is \$1,455.23. Ontario: $0.0505 \times 28158.25 = 1421.99$ before credits, and the credits are $0.0505 \times (12989 + 1311.75) = 722.19$, so it is \$699.80. With the \$300 premium, the income tax is $1455.23 + 699.80 + 300 = 2455.03$ dollars.

The set-aside is $3153.50 + 2455.03 = 5608.53$ dollars, which is 18.7% of the net business income. Dev keeps \$24,391.47.

Check: this is lower than Ana's 37% because Dev's income is in the lowest brackets, with the basic personal amounts shielding the first part.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: treating revenue as income. Tax and CPP are on net business income. Ana's \$24,000 of revenue became \$21,600 of income, and the \$2,400 of expenses is worth about \$890 of tax and CPP.

</div>

<div class="warning" markdown>

Watch out: spending the HST. A registrant holds the 13% for the CRA. On an invoice of \$2,260, \$260 is not yours.

</div>

<div class="warning" markdown>

Watch out: expecting a refund-style April. Nothing is withheld on business income, so the whole bill arrives on April 30. In the second year it may also bring instalments.

</div>

<div class="warning" markdown>

Watch out: pricing at your old hourly wage. A salary of \$65,000 is \$31.25 an hour over paid hours. The freelancer in Example 2 needs \$56.39, because unpaid time and unbillable time have to be paid for by the billed hours.

</div>

The small supplier test uses revenue, not profit, and it includes revenue of associated persons. A business that has expenses larger than revenue still counts its revenue. Losses on a side gig have their own rules, which this lesson does not cover. Self-employed CPP has the same yearly maximums as the sum of both halves, \$8,460.90 plus \$832.00, so past a net business income of \$85,000 the CPP stops growing.

## Tricks and shortcuts

For a first guess, set aside about a third of each payment for someone with a salary, as in Example 1 (33.3% of revenue), and a fifth for someone with a low income, as in Example 4. These are guesses to be replaced with a calculation.

To remove HST from a total, divide by 1.13. To find the tax portion, multiply the total by $\frac{13}{113}$.

To turn a salary into a freelance rate, divide the salary by billable hours and then add roughly 20% to 30% for the second half of CPP, benefits, expenses and tax. Example 2's ratio of 1.80 against the paid-hour rate comes from the unpaid time (1.13), the unbillable time (1.33) and the rest (about 1.20).

## In code

The function `tax_and_cpp` is a compact version of the calculator from the tax lesson with business income added. It reproduces Examples 1 and 2 and the quarterly test of Example 3.

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


def tax_and_cpp(emp, se):
    """2026 income tax and self-employed CPP for T4 income `emp` plus net business income `se` (simplified)."""
    c_emp = max(0.0, min(emp, 74_600) - 3_500)                  # contributory earnings already used by the employer's payroll
    c_se = max(0.0, min(emp + se, 74_600) - 3_500) - c_emp      # room left for the business income
    t2_se = max(0.0, min(emp + se, 85_000) - 74_600) - max(0.0, min(emp, 85_000) - 74_600)
    cpp_se = 0.119 * c_se + 0.08 * t2_se                        # both halves, plus CPP2 at 8%
    deduction = 0.0695 * c_se + 0.08 * t2_se                    # the part of the CPP that is a deduction
    credit_base = 0.0495 * c_se                                 # the part that is a credit
    cpp_emp_base, cpp_emp_enh = 0.0495 * c_emp, 0.01 * c_emp
    cpp2_emp = 0.04 * max(0.0, min(emp, 85_000) - 74_600)
    ei = 0.0163 * min(emp, 68_900)
    taxable = emp + se - cpp_emp_enh - cpp2_emp - deduction
    credits = cpp_emp_base + credit_base + ei
    fed = max(0.0, slices(taxable, FED) - 0.14 * (16_452 + (1_501 if emp > 0 else 0) + credits))
    ont = max(0.0, slices(taxable, ONT) - 0.0505 * (12_989 + credits))
    surtax = 0.20 * max(0.0, ont - 5_818) + 0.36 * max(0.0, ont - 7_446)
    return fed + ont + surtax + premium(taxable), cpp_se


# Ana: a $65,000 salary plus a side gig with $24,000 of revenue and $2,400 of deductible expenses.
net = 24_000 - 2_400
base_tax, _ = tax_and_cpp(65_000, 0)
tax, cpp = tax_and_cpp(65_000, net)
extra = tax - base_tax
print(round(cpp, 2), round(extra, 2), round(extra + cpp, 2), round((extra + cpp) / net, 4))   # 1974.4 6019.36 7993.76 0.3701
print(round(net - extra - cpp, 2))                                                            # 13606.24


def take_home_alone(n):
    t, c = tax_and_cpp(0, n)
    return n - t - c


# The hourly rate that matches a $65,000 salary (take-home $50,555.75), 1,840 hours worked, 75% billable.
target = 50_555.75 + 3_000                      # plus $3,000 a year for benefits the job would have given
lo, hi = 30_000.0, 150_000.0
for _ in range(60):                             # bisection for the net business income that leaves `target`
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if take_home_alone(mid) < target else (lo, mid)
revenue = lo + 4_800                            # add $4,800 of business expenses
print(round(lo, 2), round(revenue, 2), round(revenue / (1_840 * 0.75), 2))                   # 73017.03 77817.03 56.39


def small_supplier(quarters):
    """Last four quarters' revenue after each quarter, and whether it is still $30,000 or less."""
    return [(sum(quarters[i - 3:i + 1]), sum(quarters[i - 3:i + 1]) <= 30_000) for i in range(3, len(quarters))]


print(small_supplier([3_000, 6_500, 7_000, 7_500, 9_000, 9_500]))
# [(24000, True), (30000, True), (33000, False)]
```

The code leaves out the same things as the tax lesson's calculator, and it handles only one year with no raise and no EI opt-in. The quarterly test checks only the four-quarter total, not the single-quarter rule.

</details>

## FAQ

### Why do I pay both halves of CPP?

An employee's CPP is split between employee and employer. A self-employed person is both, so the CRA's table shows the self-employed maximum of \$8,460.90, twice the employee's \$4,230.45. The extra half is partly offset in tax, since half of the base contributions is a deduction.

### Should I register for GST/HST before I have to?

You may register voluntarily, and then you charge the tax and claim input tax credits. The math is the tax collected minus the credits, as in Example 3. Whether it suits you depends on your clients and your costs, which this lesson does not decide.

### What if I do not pay instalments I was supposed to?

The CRA charges instalment interest and may add a penalty when payments are late or too low ([CRA, who has to pay](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html)). Paying earlier is the cheaper path.

### Is 37% the right set-aside for everyone?

No. It is Ana's number, from her salary and her side income. A person with a lower income has a lower share (Example 4), and a higher income has a higher one. Run the calculator with your own figures.

## Practice

### Warm-up

1\. A freelancer with no other job has a net business income of \$50,000. Find the 2026 self-employed CPP.

<details class="solution" markdown>
<summary>Solution</summary>

$0.119 \times (50000 - 3500) = 0.119 \times 46500 = 5533.50$ dollars. There is no CPP2, since \$50,000 is under \$74,600.

Check: $5533.50 \div 46500 = 0.119$.

</details>

2\. A freelancer has revenue of \$10,000, spends \$1,200 on client meals and \$900 on software. Find the deductible expenses and the net business income.

<details class="solution" markdown>
<summary>Solution</summary>

Meals are limited to 50%: $0.5 \times 1200 = 600$. Software is \$900. The deductible expenses are \$1,500 and the net business income is $10000 - 1500 = 8500$ dollars.

Check: $8500 + 1500 = 10000$.

</details>

3\. A registered freelancer invoices \$1,500 plus 13% HST. Find the HST, the total, and the share of the total that belongs to the CRA.

<details class="solution" markdown>
<summary>Solution</summary>

The HST is $0.13 \times 1500 = 195$ dollars, the total is \$1,695, and the share is $\frac{195}{1695} = 11.5\%$.

Check: $\frac{13}{113} = 0.11504$.

</details>

### Standard

4\. A freelancer's net tax owing was \$2,800 in 2025, \$4,100 in 2026 and is expected to be \$5,200 in 2027. In 2024 it was \$0. Do instalments apply for 2026? For 2027?

<details class="solution" markdown>
<summary>Solution</summary>

For 2026, the net tax owing of \$4,100 is over \$3,000, but neither 2025 (\$2,800) nor 2024 (\$0) is, so no instalments are required. For 2027, the \$5,200 is over \$3,000 and 2026 (\$4,100) is also over \$3,000, so instalments are required, due March 15, June 15, September 15 and December 15.

Check: both tests must be true in the same year, which is the case only for 2027.

</details>

5\. Ana's salary is \$65,000 and she nets \$10,000 from a side gig. Find the self-employed CPP, then estimate the extra income tax by bracket rates (29.65% on taxable income, the credit on the base CPP at 19.05%, and \$150 more Health Premium), and give the set-aside share.

<details class="solution" markdown>
<summary>Solution</summary>

Room under \$74,600 is \$9,600, so the base CPP is $0.119 \times 9600 = 1142.40$. Her total of \$75,000 is \$400 over \$74,600, so CPP2 is $0.08 \times 400 = 32.00$. The CPP is \$1,174.40.

The deduction is $0.0695 \times 9600 + 32 = 699.20$, so taxable income rises by $10000 - 699.20 = 9300.80$. At 29.65% that is \$2,757.69. The credit on $0.0495 \times 9600 = 475.20$ is worth $0.1905 \times 475.20 = 90.53$. With \$150 more premium, the extra tax is $2757.69 - 90.53 + 150 = 2817.16$ dollars.

The set-aside is $1174.40 + 2817.16 = 3991.56$ dollars, which is 39.9% of \$10,000.

Check: the full calculator gives the same \$3,991.56.

</details>

6\. A freelancer needs \$78,000 of revenue. They work 46 weeks of 40 hours and 70% is billable. Find the hourly rate, and compare it with the \$31.25 an hour of a \$65,000 job.

<details class="solution" markdown>
<summary>Solution</summary>

The billable hours are $46 \times 40 \times 0.70 = 1288$. The rate is $\frac{78000}{1288} = 60.56$ dollars, which is $\frac{60.56}{31.25} = 1.94$ times the job's hourly pay.

Check: $60.56 \times 1288 = 78001$, within rounding of \$78,000.

</details>

### Challenge

7\. A freelancer's revenue in four quarters is \$4,000, \$6,500, \$7,000 and \$8,000. How much can they bill in the fifth quarter and still be a small supplier? And in the sixth, if the fifth is billed at that maximum?

<details class="solution" markdown>
<summary>Solution</summary>

The last four quarters after the fifth are quarters 2 to 5: $6500 + 7000 + 8000 + q_5 \le 30000$, so $q_5 \le 8500$. After the sixth they are quarters 3 to 6: $7000 + 8000 + 8500 + q_6 \le 30000$, so $q_6 \le 6500$.

Check: $6500 + 7000 + 8000 + 8500 = 30000$ and $7000 + 8000 + 8500 + 6500 = 30000$, and both are allowed because \$30,000 is not over the limit.

</details>

8\. (Reviews [paycheques and budgeting](../01-everyday-money/03-paycheques-and-budgeting.md).) An employee earns \$65,000 and pays CPP of \$3,659.25 and EI of \$1,059.50. A freelancer has a net business income of \$65,000. Find the freelancer's CPP and compare the two payroll totals.

<details class="solution" markdown>
<summary>Solution</summary>

The freelancer's CPP is $0.119 \times (65000 - 3500) = 7318.50$ dollars, twice the employee's \$3,659.25. There is no EI. The employee's total is $3659.25 + 1059.50 = 4718.75$, so the freelancer pays $7318.50 - 4718.75 = 2599.75$ dollars more.

Check: $2 \times 3659.25 = 7318.50$.

</details>

## Where this shows up

- Income from investments is taxed in other ways: [Taxes on investment income](02-taxes-on-investment-income.md). A first job's package, which the freelance rate is compared with, is in [Comparing job offers](01-comparing-job-offers.md).
- Software work often moves between employee, contractor and company. The percent-of-what thinking of [paycheques and budgeting](../01-everyday-money/03-paycheques-and-budgeting.md) and the present value idea of [present and future value](../03-time-value-of-money/01-present-and-future-value.md) both apply when you compare them.
- Computing: the rate in Example 2 is found by bisection, the same search used for a break-even share price or a loan rate.
