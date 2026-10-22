# Paycheques and budgeting

After this lesson you can turn an hourly wage or a salary into pay per pay period, work out the CPP and EI deductions on a paycheque, estimate the income tax taken off, find your net pay, and build a simple monthly budget and emergency fund from it.

Before this: [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md) and [tips, discounts and HST](01-tips-discounts-and-hst.md). The multiplier idea from [percent change](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md) shows up again here.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A job pays \$26 an hour for a 40-hour week, all year. What is the yearly pay, and what is the gross pay on a biweekly paycheque?
2. Using a CPP rate of 5.95% on pay above a basic exemption of \$3,500 a year, and an EI rate of 1.63%, find the CPP and EI on a biweekly paycheque of \$2,000.
3. Your monthly essential expenses are \$2,600. How much would an emergency fund of 3 to 6 months of them be?

<details class="solution" markdown>
<summary>Answers</summary>

1. A full-time year is $40 \times 52 = 2080$ hours, so the pay is $26 \times 2080 = 54{,}080$ dollars. There are 26 biweekly paycheques, so each is $54{,}080 \div 26 = 2{,}080$ dollars.
2. The exemption per paycheque is $3500 \div 26 = 134.62$. The CPP is $0.0595 \times (2000 - 134.62) = 110.99$ dollars. The EI is $0.0163 \times 2000 = 32.60$ dollars.
3. $3 \times 2600 = 7{,}800$ and $6 \times 2600 = 15{,}600$, so \$7,800 to \$15,600.

</details>

## The idea

An offer letter says \$62,400 a year, or \$30 an hour. The first paycheque that reaches your bank account is smaller than you expected. The offer was your gross pay, the amount before anything is taken off. What arrives is your net pay, after your employer takes off money for the Canada Pension Plan, Employment Insurance and income tax, and sends it to the government on your behalf.

So there are two tasks. The first is a chain of conversions: a wage or salary to a pay per period. The second is a chain of deductions, each one a percent of some amount, and the same question applies as in the HST lessons: percent of what? CPP is a percent of the pay above an exemption. EI is a percent of all the pay, up to a yearly limit. Income tax is a percent of the part of your income that falls in each bracket. A budget then asks what to do with the net amount.

This lesson does the payroll arithmetic with the 2026 rules. It estimates income tax and leaves the full calculation to the [income tax brackets](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md) lesson.

## Definitions

**Gross pay** is what you earn before any deductions. **Net pay**, or take-home pay, is what you receive after the deductions:

$$
\text{net pay} = \text{gross pay} - \text{deductions}.
$$

A **deduction** is an amount taken from your gross pay, and in this lesson the deductions are CPP, EI and income tax. A **pay period** is the stretch of time one paycheque covers. Common pay periods are weekly (52 paycheques a year), biweekly (every two weeks, 26 a year), semi-monthly (twice a month, on fixed dates, 24 a year) and monthly (12 a year).

An **hourly wage** is pay per hour worked, and a **salary** is a fixed yearly amount. A full-time year of 40 hours for 52 weeks is $40 \times 52 = 2080$ hours.

The **Canada Pension Plan (CPP)** is a mandatory pension plan funded by contributions from workers and employers. The employee contribution rate for 2026 is 5.95% ([CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html)). It applies to pay above the **basic exemption**, a yearly amount of \$3,500 that is not charged CPP, and up to the **year's maximum pensionable earnings (YMPE)**, which is \$74,600 for 2026. Contributions are charged on earnings from the exemption up to the maximum contributory earnings, \$71,100 (that is, $74{,}600 - 3{,}500$), so the most an employee pays in a year is $5.95\% \times 71{,}100 = 4{,}230.45$ dollars.

A second tier, **CPP2**, charges 4% on earnings between the YMPE and a higher limit, \$85,000 for 2026 ([CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html)). Its yearly maximum is $4\% \times (85{,}000 - 74{,}600) = 416$ dollars.

**Employment Insurance (EI)** is insurance that pays benefits to workers who lose their jobs or take certain leaves. The 2026 employee premium outside Quebec is 1.63% of earnings up to the **maximum insurable earnings** of \$68,900, so the yearly maximum is \$1,123.07 ([CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html)). There is no exemption for EI.

**Income tax withholding** is the amount your employer takes off each paycheque as an advance on your yearly income tax. It is an estimate based on the pay and on the claim amounts you give your employer, and your tax return settles the real amount.

A **budget** is a plan for how your net income is spent and saved. An **emergency fund** is cash set aside for surprise costs such as a job loss, measured in months of essential expenses.

<div class="note" markdown>

These figures are for 2026 and change every year. Check the linked pages before using them for real decisions.

</div>

## How to do it

### From hourly to annual, and back to a paycheque

1. For an hourly wage, multiply by the hours: $\text{hourly wage} \times 40 \times 52 = \text{hourly wage} \times 2080$ for full time.
2. Divide the annual gross by the number of pay periods: 52 for weekly, 26 for biweekly, 24 for semi-monthly, 12 for monthly.
3. Check by multiplying back. For a biweekly paycheque, the hours are 80 and $\text{wage} \times 80$ should match.

For \$62,400 a year the results are:

| Pay period | Paycheques a year | Gross per paycheque |
|---|---|---|
| weekly | 52 | \$1,200.00 |
| biweekly | 26 | \$2,400.00 |
| semi-monthly | 24 | \$2,600.00 |
| monthly | 12 | \$5,200.00 |

A biweekly paycheque is not "half a month". There are 26 of them in a year, not 24, so you usually get two months a year with three paycheques, and your monthly average is $\text{biweekly pay} \times \frac{26}{12}$.

### Deductions on one paycheque

Let $n$ be the number of pay periods and $g$ the gross pay for one period. The first two deductions are percent calculations:

$$
\text{CPP} = 0.0595 \times \left(g - \frac{3500}{n}\right), \qquad \text{EI} = 0.0163 \times g.
$$

The exemption is spread over the pay periods, so it is $\frac{3500}{n}$ per paycheque. Payroll rounds to the cent: the biweekly exemption is $3500 \div 26 = 134.615\ldots$, which becomes \$134.62.

1. Compute the gross pay for the period.
2. Subtract the exemption for the period and multiply by 5.95% to get the CPP. If the result would be negative, the CPP is \$0.
3. Multiply the gross pay by 1.63% to get the EI.
4. Estimate the income tax (next section).
5. Add the three deductions and subtract the total from the gross pay to get the net pay.
6. Check that deductions plus net pay equal gross pay, and compare the yearly totals with the caps.

CPP and EI stop for the year once you reach their maximums: \$4,230.45 for CPP and \$1,123.07 for EI. A high earner's paycheques get bigger late in the year, as Example 3 shows.

### Estimating income tax

The employer uses the CRA's payroll formulas, which depend on your claim amounts and other details, so the real figure varies. A rough estimate follows the structure of the tax system. This is only a sketch, and the [income tax brackets](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md) lesson does it properly.

For 2026 the federal rates are 14% on taxable income up to \$58,523 and 20.5% from there to \$117,045 ([CRA tax rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html)). The Ontario rates on that page are 5.05% up to \$53,891 and 9.15% from there to \$107,785. A credit for the basic personal amount lowers each tax: the federal amount is \$16,452 and the Ontario amount is \$12,989 ([CRA payroll formulas](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html)), each credited at the lowest rate of its bracket table. The estimate:

1. Take the annual gross pay as the taxable income. This ignores small deductions and credits.
2. Apply the federal rates by bracket, then subtract $0.14 \times 16{,}452$.
3. Apply the Ontario rates by bracket, then subtract $0.0505 \times 12{,}989$.
4. Add the two, divide by the number of pay periods.

This leaves out the credits for CPP and EI, the Canada employment amount and the Ontario health premium ([ontario.ca](https://www.ontario.ca/page/health-premium)), which the real formulas include, and the Ontario surtax, which does not apply at this income. The estimate is meant to be the right size, not exact.

### Budgeting

A budget starts from net pay, because that is the money you can spend.

1. Convert to a monthly net pay. For a biweekly paycheque it is $\text{net} \times \frac{26}{12}$.
2. List the fixed essentials (rent, groceries, transit, phone, insurance, minimum debt payments) and add them up.
3. Pick a split. The **50/30/20 rule** divides net pay into 50% for needs, 30% for wants and 20% for saving and extra debt payments. It is one simple starting point, popularized by Elizabeth Warren and Amelia Warren Tyagi in *All Your Worth* (2005), and not a law of nature: in a city with high rent, needs can take more than half.
4. Track what you spend for a month or two, compare it with the plan and adjust.
5. Build an emergency fund. The fund in months is $\frac{\text{savings}}{\text{monthly essential expenses}}$. Three to six months of essentials is a common rule of thumb, and the number you need depends on how steady your income is.

For example, take-home pay of \$4,000 a month splits into \$2,000 for needs, \$1,200 for wants and \$800 for saving. If your essentials are \$2,600 a month, the \$800 would take $\frac{3 \times 2600}{800} = 9.75$ months to build a 3-month fund, so a plan that works for you may differ from 50/30/20.

An example of a wage floor is Ontario's general minimum wage, which is \$17.95 an hour from October 1, 2026 to September 30, 2027 ([ontario.ca](https://www.ontario.ca/document/your-guide-employment-standards-act-0/minimum-wage)). Full time that is $17.95 \times 2080 = 37{,}336$ dollars a year before deductions. Example 2 works through that paycheque.

## Worked examples

<div class="example" markdown>

### Example 1: a full biweekly paycheque

Your offer is \$62,400 a year, paid biweekly, in Ontario. Find the gross pay, the CPP, the EI, an estimate of the income tax, and the net pay for one paycheque.

Step 1: the gross pay is $62{,}400 \div 26 = 2{,}400$ dollars.

Step 2: the exemption for one paycheque is $3500 \div 26 = 134.615\ldots$, which is \$134.62. The CPP is

$$
0.0595 \times (2400 - 134.62) = 0.0595 \times 2265.38 = 134.79\ldots
$$

so \$134.79. This pay is below the \$74,600 limit for the year, so there is no CPP2.

Step 3: the EI is $0.0163 \times 2400 = 39.12$ dollars.

Step 4: estimate the income tax with the sketch above, taking \$62,400 as the taxable income. Federal first:

$$
0.14 \times 58{,}523 + 0.205 \times (62{,}400 - 58{,}523) = 8193.22 + 794.79 = 8988.01.
$$

Subtract the credit $0.14 \times 16{,}452 = 2303.28$ to get \$6,684.73. Now Ontario:

$$
0.0505 \times 53{,}891 + 0.0915 \times (62{,}400 - 53{,}891) = 2721.50 + 778.57 = 3500.07,
$$

less $0.0505 \times 12{,}989 = 655.94$, which gives \$2,844.12. The yearly estimate is $6684.73 + 2844.12 = 9528.85$ dollars, and per paycheque it is $9528.85 \div 26 = 366.49$ dollars.

Step 5: the deductions total $134.79 + 39.12 + 366.49 = 540.40$ dollars, and the net pay is

$$
2400.00 - 540.40 = 1859.60.
$$

Step 6: check. Net plus deductions is $1859.60 + 540.40 = 2400.00$. The yearly CPP is $26 \times 134.79 = 3504.54$, and the formula $0.0595 \times (62{,}400 - 3500) = 3504.55$ differs by a cent because each paycheque was rounded. The yearly EI is $26 \times 39.12 = 1017.12$, under the \$1,123.07 maximum, and CPP is under \$4,230.45, so neither has run out. The deductions take $540.40 \div 2400 = 22.5\%$ of the gross, and the net is 77.5%.

The monthly net is about $1859.60 \times \frac{26}{12} = 4029.13$ dollars. In a month with three paycheques you receive \$5,578.80, so budget from the average and not from the three-cheque month.

<div class="warning" markdown>

Watch out at Step 2: charging CPP on the whole \$2,400 gives $0.0595 \times 2400 = 142.80$, which is \$8.01 too much. The exemption is not charged, and it is spread over the paycheques.

</div>

</div>

<div class="example" markdown>

### Example 2: full time at Ontario's minimum wage

A full-time job pays the minimum wage of \$17.95 an hour for 40 hours a week and is paid biweekly. Find the gross pay, the CPP, the EI, and the pay left before income tax.

The biweekly gross pay is $17.95 \times 80 = 1436.00$ dollars, and the annual gross pay is $17.95 \times 2080 = 37{,}336$ dollars.

The CPP is $0.0595 \times (1436.00 - 134.62) = 0.0595 \times 1301.38 = 77.43$ dollars. The EI is $0.0163 \times 1436.00 = 23.41$ dollars.

Before income tax, the pay is $1436.00 - 77.43 - 23.41 = 1335.16$ dollars, which is 93.0% of the gross. Income tax would take a smaller part of this pay than of the \$62,400 salary, since most of the income falls under the credits, but this lesson doesn't compute it.

Check: the yearly CPP is about $26 \times 77.43 = 2013.18$, and the formula gives $0.0595 \times (37{,}336 - 3500) = 2013.24$. The yearly EI is about \$608.58. Both are under their maximums.

</div>

<div class="example" markdown>

### Example 3: a high earner hits the caps

An employee earns \$120,000 a year, paid biweekly, with the same pay each time. When do CPP and EI stop, and what do they pay in the year?

The biweekly gross pay is $120{,}000 \div 26 = 4{,}615.38$ dollars. The CPP per paycheque is $0.0595 \times (4615.38 - 134.62) = 266.61$ dollars, and the EI is $0.0163 \times 4615.38 = 75.23$ dollars.

CPP: the yearly maximum is \$4,230.45, and $4230.45 \div 266.61 = 15.87$. So 15 full paycheques deduct $15 \times 266.61 = 3999.15$, the 16th deducts only the remaining $4230.45 - 3999.15 = 231.30$, and there is no CPP from the 17th on.

EI: $1123.07 \div 75.23 = 14.93$. Fourteen paycheques deduct $14 \times 75.23 = 1053.22$, the 15th deducts the remaining \$69.85, and EI stops after that.

CPP2: the pay is above the \$85,000 limit, so the full \$416 is paid for the year. It starts in the 17th paycheque, where the pay for the year so far passes the YMPE of \$74,600 (after 16 paycheques it is only $16 \times 4615.38 = 73{,}846.08$).

The yearly total is $4230.45 + 1123.07 + 416 = 5769.52$ dollars. The take-home is lower in the first paycheques and higher in the later ones, even though the gross pay never changes.

Check: the CPP maximum is also $0.0595 \times 71{,}100 = 4230.45$, and the CPP2 maximum is $0.04 \times 10{,}400 = 416$.

</div>

<div class="example" markdown>

### Example 4: a semi-monthly paycheque (finish it yourself)

A salary of \$52,800 is paid semi-monthly. Find the gross pay per paycheque, the CPP and the EI.

Step 1: there are 24 paycheques, so the gross pay is $52{,}800 \div 24 = 2{,}200$ dollars. Step 2: the exemption per paycheque is $3500 \div 24 = 145.83$ dollars (rounded to the cent).

Now find the CPP and the EI, and the pay left after those two deductions.

<details class="solution" markdown>
<summary>Finish</summary>

The CPP is $0.0595 \times (2200 - 145.83) = 0.0595 \times 2054.17 = 122.22$ dollars. The EI is $0.0163 \times 2200 = 35.86$ dollars. The two together are \$158.08, and the pay left before income tax is $2200 - 158.08 = 2041.92$ dollars.

Check: yearly, $24 \times 122.22 = 2933.28$, and the formula gives $0.0595 \times (52{,}800 - 3500) = 2933.35$, close, with the gap from rounding. EI is $24 \times 35.86 = 860.64$, which matches $0.0163 \times 52{,}800 = 860.64$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: budgeting from gross pay. A salary of \$62,400 is \$5,200 a month on paper, but the net is about \$4,029 a month in Example 1, almost \$1,200 less. Rent and everything else is paid from the net.

</div>

<div class="warning" markdown>

Watch out: multiplying a biweekly paycheque by 24, or dividing the annual pay by 24. Biweekly has 26 paycheques. A semi-monthly salary of \$2,600 and a biweekly salary of \$2,600 are different yearly amounts: \$62,400 and \$67,600.

</div>

<div class="warning" markdown>

Watch out: taking CPP on the full pay. The first \$3,500 a year is exempt and the pay above the YMPE has no basic CPP. And after you reach the yearly maximum, CPP stops.

</div>

<div class="warning" markdown>

Watch out: treating 50/30/20 as a rule you must follow. Rent in many Ontario cities is more than 30% of net pay for a student or a new graduate. The rule is a starting point, and the split should come from your own numbers.

</div>

A few edge cases are worth knowing. The figure 2080 assumes exactly 52 weeks of 40 hours, and a year is 52 weeks plus a day or two, so unpaid breaks and calendar quirks move the real hours a little. A paycheque whose gross pay is below the per-period exemption has a CPP of \$0, since the pay above the exemption is negative. Part-time pay works the same way as full-time pay, only with fewer hours in the first step.

## Tricks and shortcuts

To go from an hourly wage to a yearly salary, double the wage and add three zeros: \$30 an hour is about \$60,000. That uses 2000 hours and not 2080, so it is about 4% low. For the exact number, multiply by 2080.

From a biweekly paycheque to a monthly figure, multiply by 26 and divide by 12, which is about 2.17. A paycheque of \$1,859.60 gives \$4,029.13. A quick version is "double it and add a sixth".

A quick check on the deductions: for this lesson's examples, CPP is a little over 5.6% of gross and EI a little over 1.6%, so together they are a bit over 7%. For pay in the \$60,000 range, income tax adds roughly another 15%, so net pay is about three quarters of gross. Use this only as a sanity check, and use the full calculation for the real number.

To find the months in an emergency fund, divide the savings by the monthly essentials. With \$5,000 saved and essentials of \$2,600, you have $5000 \div 2600 = 1.9$ months.

## In code

A paycheque is a few lines of arithmetic. The function below uses Python's `decimal` module so the cents come out exactly, and it ignores the yearly maximums, so it fits a paycheque early in the year.

<details class="code" markdown>
<summary>In code</summary>

```python
from decimal import Decimal as D, ROUND_HALF_UP

def cents(x):
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)

def cpp(gross, periods):
    exemption = cents(D(3500) / periods)
    return cents(max(D(0), gross - exemption) * D("0.0595"))

def ei(gross):
    return cents(gross * D("0.0163"))

def paycheque(annual, periods, income_tax):
    gross = cents(D(annual) / periods)
    c, e = cpp(gross, periods), ei(gross)
    net = gross - c - e - D(income_tax)
    return gross, c, e, net

print(paycheque(62400, 26, "366.49"))   # gross 2400.00, cpp 134.79, ei 39.12, net 1859.60
print(paycheque(52800, 24, "0"))        # gross 2200.00, cpp 122.22, ei 35.86, net 2041.92

monthly_net = D("1859.60") * 26 / 12
print(cents(monthly_net))               # 4029.13
```

The `max(D(0), ...)` keeps the CPP from going negative when the pay is below the exemption. The income tax is an input here, because the estimate in Example 1 needs the brackets.

</details>

## FAQ

### Why is my first paycheque smaller than my salary divided by the pay periods?

Because of the deductions. The salary divided by the pay periods is the gross pay. The CPP, EI and income tax come off that, so the net is smaller. The offer letter's figure is gross unless it says otherwise.

### Why do my deductions change during the year?

CPP and EI stop when you reach the yearly maximums, so a high earner takes home more at the end of the year, as in Example 3. Income tax withholding can also change if your pay changes or you update the claim amounts you gave your employer.

### Is the CPP money lost?

No. CPP contributions earn you a pension later, and EI is insurance you can claim if you qualify, so neither is the same as a tax that buys you nothing. How the pension works belongs in [retirement accounts](../06-investing-and-retirement/03-retirement-accounts.md) and later lessons. Income tax is the part that pays for public services in general.

### Should I follow 50/30/20?

Use it as a first draft. If your needs are more than half of your net pay, change the split and look for the largest items to change. The rule does not account for debt with high interest, which usually deserves more than 20% (see [credit cards and the minimum payment trap](../04-borrowing/04-credit-cards-and-the-minimum-payment-trap.md)).

## Practice

### Warm-up

1\. A job pays \$26 an hour for a 40-hour week all year. Find the yearly gross pay and the gross pay for a weekly, a biweekly and a semi-monthly paycheque.

<details class="solution" markdown>
<summary>Solution</summary>

The yearly pay is $26 \times 2080 = 54{,}080$ dollars. Weekly: $54{,}080 \div 52 = 1040$ dollars. Biweekly: $54{,}080 \div 26 = 2080$ dollars. Semi-monthly: $54{,}080 \div 24 = 2253.33$ dollars.

Check: $1040 \times 52 = 54{,}080$, and $26 \times 80 = 2080$, the biweekly pay for 80 hours.

</details>

2\. Find the CPP and the EI on a biweekly paycheque of \$2,000.

<details class="solution" markdown>
<summary>Solution</summary>

The exemption is $3500 \div 26 = 134.62$. The CPP is $0.0595 \times (2000 - 134.62) = 0.0595 \times 1865.38 = 110.99$ dollars. The EI is $0.0163 \times 2000 = 32.60$ dollars.

Check: the CPP is a bit under 6% of \$1,865, which is about \$112, and the EI is 1.63% of \$2,000, a little over \$32.

</details>

3\. Your take-home pay is \$4,000 a month. Split it by the 50/30/20 rule.

<details class="solution" markdown>
<summary>Solution</summary>

Needs: $0.50 \times 4000 = 2000$ dollars. Wants: $0.30 \times 4000 = 1200$ dollars. Saving: $0.20 \times 4000 = 800$ dollars.

Check: $2000 + 1200 + 800 = 4000$.

</details>

### Standard

4\. Your essential expenses are \$2,600 a month. (a) How big is an emergency fund of 3 months, and of 6 months? (b) If you save \$400 a month, how many months does it take to build the 3-month fund?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $3 \times 2600 = 7800$ dollars and $6 \times 2600 = 15{,}600$ dollars.

(b) $7800 \div 400 = 19.5$, so it takes 19.5 months: you reach the goal during the 20th month.

Check: after 19 months you have $19 \times 400 = 7600$, short of 7,800, and after 20 months $8000$.

</details>

5\. A paycheque has gross pay \$2,400.00, CPP \$134.79, EI \$39.12 and income tax \$366.49. (a) What is the net pay? (b) What percent of the gross do the deductions take? (c) What is the net pay for the year, if there are 26 paycheques like this?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The deductions are $134.79 + 39.12 + 366.49 = 540.40$, so the net pay is $2400.00 - 540.40 = 1859.60$ dollars.

(b) $540.40 \div 2400 = 0.2252$, about 22.5%.

(c) $26 \times 1859.60 = 48{,}349.60$ dollars.

Check: $0.775 \times 2400 = 1860$, close to 1859.60.

</details>

6\. You earn \$30 an hour full time (\$62,400 a year) and get a raise to \$32 an hour. On a biweekly paycheque the gross pay rises by \$160. Estimate how much of the raise you keep, using the CPP rate 5.95%, the EI rate 1.63% and the marginal income tax rates 20.5% federal and 9.15% Ontario.

<details class="solution" markdown>
<summary>Solution</summary>

The CPP on the extra \$160 is $0.0595 \times 160 = 9.52$ dollars, because the pay is above the exemption already. The EI is $0.0163 \times 160 = 2.61$ dollars. The income tax on extra pay at this level is $(0.205 + 0.0915) \times 160 = 0.2965 \times 160 = 47.44$ dollars. The raise adds $160 - 9.52 - 2.61 - 47.44 = 100.43$ dollars to your net pay, which is 62.8% of the raise.

This is an estimate, since it ignores credits and the health premium. It shows why the raise on the offer letter is not the raise in your account.

Check: the deductions are $9.52 + 2.61 + 47.44 = 59.57$, and $160 - 59.57 = 100.43$.

</details>

### Challenge

7\. A salary is \$90,000, paid biweekly. (a) Find the CPP and EI per paycheque before the caps. (b) In which paycheque does each one run out? (c) What do CPP, CPP2 and EI add up to for the year?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The gross pay is $90{,}000 \div 26 = 3{,}461.54$. The CPP is $0.0595 \times (3461.54 - 134.62) = 197.95$ dollars, and the EI is $0.0163 \times 3461.54 = 56.42$ dollars.

(b) CPP: $4230.45 \div 197.95 = 21.37$, so 21 full paycheques take $21 \times 197.95 = 4156.95$ and the 22nd takes the remaining \$73.50. EI: $1123.07 \div 56.42 = 19.9$, so 19 full paycheques take $19 \times 56.42 = 1071.98$ and the 20th takes the remaining \$51.09.

(c) The pay is above \$85,000, so CPP2 is the full \$416. The total is $4230.45 + 416 + 1123.07 = 5769.52$ dollars.

Check: the totals are the same as for a \$120,000 salary, since both earn above every limit.

</details>

8\. (Reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).) Your monthly net pay is \$4,029.13 and your rent is \$1,450. (a) What percent of net pay is the rent? (b) Under 50/30/20, how much is left for other needs after rent? (c) What would the rent be as a percent of the 50% needs budget?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The whole is the net pay: $1450 \div 4029.13 = 0.3599$, about 36.0%.

(b) The needs budget is $0.50 \times 4029.13 = 2014.57$ dollars, so $2014.57 - 1450 = 564.57$ dollars is left for groceries, transit, phone and the other needs.

(c) The whole is now the needs budget: $1450 \div 2014.57 = 0.7198$, about 72.0%. The same rent is a different percent for a different whole.

Check: $0.72 \times 2014.57 = 1450.49$, and $0.36 \times 4029.13 = 1450.49$, both about \$1,450.

</details>

## Where this shows up

- The next chapter, interest and growth, starts with [simple interest](../02-interest-and-growth/01-simple-interest.md), the first way your savings and your debts change over time. The yearly pay-to-paycheque conversions here come back when [loans](../03-time-value-of-money/03-loan-amortization-formula.md) are paid in regular installments.
- The full tax calculation is in [income tax brackets: marginal vs effective](../07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md), and the registered accounts you might save into are in [retirement accounts](../06-investing-and-retirement/03-retirement-accounts.md).
- A pay stub is a small program with caps and rounding: a loop over paycheques with a running total, much like the `paycheque` function above. In economics, the gap between gross and net is the tax wedge on labour, and the wage floor links to supply and demand in [surplus and market interventions](../../07-economics-math/02-markets/04-surplus-and-market-interventions.md).
