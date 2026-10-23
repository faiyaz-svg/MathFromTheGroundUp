# Income tax brackets: marginal vs effective

After this lesson you can compute the 2026 federal and Ontario income tax for an employee step by step, find their marginal and effective rates, explain why a raise never lowers take-home pay, and value an RRSP deduction at the marginal rate.

Before this: [piecewise, absolute value and step functions](../../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md), [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md) and [paycheques and budgeting](../01-everyday-money/03-paycheques-and-budgeting.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A made-up tax charges 10% on the first \$40,000 of income and 20% on everything above that. Find the tax on \$50,000, the marginal rate and the average rate.
2. A non-refundable credit is worth "amount times the lowest rate". What is a \$5,000 credit worth at a lowest rate of 14%?
3. An RRSP deduction of \$2,000 is taken at a combined marginal rate of 29.65%. How much tax does it save?

<details class="solution" markdown>
<summary>Answers</summary>

1. The first \$40,000 pays $0.10 \times 40000 = 4000$ and the other \$10,000 pays $0.20 \times 10000 = 2000$, so the tax is \$6,000. The marginal rate is 20% (the rate on the next dollar) and the average rate is $6000 \div 50000 = 12\%$.
2. $0.14 \times 5000 = 700$, so the credit cuts the tax by \$700.
3. $0.2965 \times 2000 = 593$, so it saves \$593.

</details>

## The idea

Suppose you start a job in Ontario at \$65,000 a year. The tax is not 29.65% of everything you earn, even though your next dollar of income would be taxed at about that rate. It is not 0% on the first stretch and a flat rate afterwards either. The tax on income is built in slices. A first slice is taxed at a low rate, the next slice at a higher rate, and each slice has its own rate. Moving into a higher slice raises the rate on the new dollars only.

Two numbers come out of this, and people mix them up all the time. The rate on the next dollar is the marginal rate, and it decides what a raise, a bonus or a deduction is worth. The total tax divided by the total income is the effective rate, and it says what share of your income the government actually takes. For a salary of \$65,000 the marginal rate is about 30% and the effective rate is about 15%: half the size, because the early dollars were taxed at lower rates and some were not taxed at all.

On top of the slices there are credits (fixed amounts of your income that are tax-free, in effect), an Ontario surtax that applies to higher incomes, and a small Ontario Health Premium. This lesson builds the whole calculation for one employee, one step at a time. It gets its figure on the page from the [piecewise functions lesson](../../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md): the tax is a function made of line segments whose slopes are the rates.

## Definitions

**Taxable income** is the income that the brackets are applied to: total income minus deductions. A **deduction** is an amount subtracted from income before the brackets are applied. In plain words, a deduction makes less of your income count.

A **tax bracket** is a range of taxable income with one rate. With limits $0 = b_0 < b_1 < \cdots < b_n = \infty$ and rates $r_1, \ldots, r_n$, the bracket $k$ is the range from $b_{k-1}$ to $b_k$ and its rate is $r_k$. A **progressive tax** has increasing rates, $r_1 < r_2 < \cdots < r_n$. Its tax on a taxable income $x$ is

$$
T(x) = \sum_{k=1}^{n} r_k \cdot \max\bigl(0,\ \min(x, b_k) - b_{k-1}\bigr).
$$

The term $\min(x, b_k) - b_{k-1}$ is how much of your income falls inside bracket $k$ (when it is negative, the $\max$ makes it 0). In plain words, each slice of income pays its own rate, and $T(x)$ adds the slices up.

The **marginal tax rate** at income $x$ is the rate of the bracket that the next dollar falls in, which is the slope of $T$ at $x$. The **effective tax rate** (also called the average rate) is the total tax divided by the income, $\frac{T(x)}{x}$. In plain words, marginal is "what the next dollar pays" and effective is "what the average dollar paid".

A **non-refundable tax credit** is an amount that is subtracted from the tax itself, not from income, and that can reduce the tax to zero but not below. Federal credits are an amount times the lowest federal rate, and Ontario credits are an amount times the lowest Ontario rate. So a credit of \$1,000 at the 14% rate is worth \$140 in tax. In plain words, a deduction saves you your marginal rate times its size, while a credit saves you the lowest rate times its size, whatever your income is.

The Ontario **surtax** is an extra tax computed on the Ontario tax itself, not on income. After the Ontario credits, the "basic" Ontario tax $B$ is raised by 20% of the part above \$5,818 and by a further 36% of the part above \$7,446. The **Ontario Health Premium** is a charge of up to \$900 that depends on taxable income.

## How to do it

### The figures for 2026

For 2026 the federal rates and limits for taxable income are 14% up to \$58,523, 20.5% up to \$117,045, 26% up to \$181,440, 29% up to \$258,482 and 33% above that ([CRA tax rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html)). The Ontario brackets are in the same table, and the two are applied separately to the same taxable income.

| Federal bracket (taxable income) | Rate | Ontario bracket (taxable income) | Rate |
|---|---|---|---|
| up to \$58,523 | 14% | up to \$53,891 | 5.05% |
| \$58,523 to \$117,045 | 20.5% | \$53,891 to \$107,785 | 9.15% |
| \$117,045 to \$181,440 | 26% | \$107,785 to \$150,000 | 11.16% |
| \$181,440 to \$258,482 | 29% | \$150,000 to \$220,000 | 12.16% |
| over \$258,482 | 33% | over \$220,000 | 13.16% |

The other figures used below, all for 2026:

- Federal basic personal amount: \$16,452 (it shrinks to \$14,829 between taxable incomes of \$181,440 and \$258,482). Ontario basic personal amount: \$12,989. ([CRA T4127 payroll formulas](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4127-payroll-deductions-formulas/t4127-jan/t4127-jan-payroll-deductions-formulas-computer-programs.html))
- Canada employment amount: \$1,501.
- CPP: 5.95% of pensionable earnings between \$3,500 and \$74,600, then 4% on earnings from \$74,600 to \$85,000 ([CRA CPP rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html)).
- EI: 1.63% of earnings up to \$68,900 ([CRA EI rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html)).
- Ontario surtax: 20% of Ontario basic tax over \$5,818, plus 36% of the part over \$7,446 ([CRA T4032-ON](https://www.canada.ca/en/revenue-agency/services/forms-publications/payroll/t4032-payroll-deductions-tables/t4032on-jan/t4032on-january-general-information.html)).
- Ontario Health Premium: \$0 up to \$20,000 of taxable income, then up to \$300, \$450, \$600, \$750 and finally \$900 above \$200,600 ([Ontario](https://www.ontario.ca/page/health-premium)). Within each band the premium phases in over a few hundred dollars; this lesson uses the top amount of each band.

<div class="note" markdown>

These figures are for 2026 and change every year. Check the linked pages before using them for real decisions. This lesson explains the math and the rules. It is not tax advice.

</div>

### Two facts about the tax function

*Theorem 1 (the tax function is continuous and a raise never lowers take-home pay).* Let $T$ be the tax function above with rates $0 \le r_k < 1$. Then $T$ is continuous, it is linear with slope $r_k$ on each bracket, and the after-tax income $x - T(x)$ is strictly increasing in $x$.

We know the formula for $T$ as a sum of slices. We want to show that there are no jumps and that more income always leaves more after tax. The plan is to look at one slice at a time, then add.

*Proof.* Write one slice as $s_k(x) = r_k \max(0, \min(x, b_k) - b_{k-1})$. The functions $\min$ and $\max$ of continuous functions are continuous (each is a continuous function of its inputs: $\min(a,b) = \frac{a + b - \lvert a - b \rvert}{2}$, and similarly for $\max$), so each $s_k$ is continuous, and so is the sum $T$. On the bracket $b_{k-1} \le x \le b_k$ the earlier slices $s_1, \ldots, s_{k-1}$ are constants (each earlier bracket is full), the later slices are 0, and $s_k(x) = r_k(x - b_{k-1})$. So $T(x) = T(b_{k-1}) + r_k(x - b_{k-1})$ on that bracket, a line with slope $r_k$. For after-tax income, $x - T(x)$ has slope $1 - r_k > 0$ on every bracket, and it is continuous. A continuous function that is increasing on each of finitely many consecutive intervals is increasing on their union, so $x - T(x)$ is strictly increasing. $\blacksquare$

Look back: the proof is the reason the myth in Example 3 is false. The rate changes at $b_k$ only for the next dollar. Because the slices are added, the dollars below $b_k$ keep their old rate, and the tax has no jump. A tax that applied one rate to the whole income would be a different function, with a jump at each limit, and you could lose money by crossing a limit. Brackets are not built that way.

*Theorem 2 (the value of a deduction).* Suppose a deduction of $d$ lowers taxable income from $x$ to $x - d$. The tax saved is $T(x) - T(x - d)$. If both $x - d$ and $x$ lie in one bracket with rate $r$, the saving is $r\,d$. If they lie in different brackets, the saving is the sum of $r_k$ times the part of $d$ that falls in bracket $k$.

This follows directly from the slope formula in Theorem 1: the saving is the change in $T$, and $T$ changes at the rate $r_k$ on bracket $k$. In plain words, a deduction removes the top dollars of your income first, so it is worth the rates of the top dollars.

### Computing the tax for an employee

Here are the steps for an employee who earns an income $I$ from a job in Ontario and has no other income. They work from the top of your pay stub down to the final tax.

1. Compute the payroll contributions. CPP is 5.95% of the earnings between \$3,500 and \$74,600. Of that rate, 4.95 percentage points are the "base" part and 1 point is the "enhanced" part ([CRA line 30800](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-30800-cpp-qpp-contributions-through-employment.html)). Earnings between \$74,600 and \$85,000 pay a second CPP contribution of 4%, which is a deduction. EI is 1.63% of earnings up to \$68,900.
2. Find taxable income: income minus the enhanced CPP, minus the second CPP contribution, minus deductions such as an RRSP contribution. The base CPP and EI are not deductions. They become credits.
3. Compute the federal tax before credits, $T_{\text{fed}}(x)$, by slices.
4. Compute the federal credits: (basic personal amount + Canada employment amount + base CPP + EI) $\times$ 14%. The federal tax is the tax before credits minus the credits, but not below 0.
5. Compute the Ontario tax before credits, $T_{\text{ON}}(x)$, by slices.
6. Compute the Ontario credits: (Ontario basic personal amount + base CPP + EI) $\times$ 5.05%. The Ontario basic tax $B$ is the tax before credits minus the credits, but not below 0.
7. Compute the Ontario surtax from $B$: $0.20 \max(0, B - 5818) + 0.36 \max(0, B - 7446)$.
8. Look up the Ontario Health Premium for the taxable income.
9. Add federal tax, Ontario basic tax, surtax and premium for the total income tax. The effective rate is the total divided by $I$. The marginal rate is the federal rate plus the Ontario rate for the brackets that the next dollar of taxable income falls in (times the surtax multiplier when the surtax applies).
10. Check: the take-home pay should be $I$ minus the income tax minus the payroll contributions, and it should be less than $I$ but more than $I \times (1 - \text{top rates})$.

## Worked examples

<div class="example" markdown>

### Example 1: a \$65,000 salary in Ontario

Use the steps above for an income of \$65,000 (a made-up salary).

Step 1: the pensionable earnings are $65000 - 3500 = 61500$. CPP is $0.0595 \times 61500 = 3659.25$, which splits into base $0.0495 \times 61500 = 3044.25$ and enhanced $0.01 \times 61500 = 615.00$. There is no second CPP contribution below \$74,600. EI is $0.0163 \times 65000 = 1059.50$, which is under the maximum.

Step 2: taxable income is $65000 - 615 = 64385$.

Step 3: the federal tax before credits has a full first bracket and part of the second:

$$
0.14 \times 58523 + 0.205 \times (64385 - 58523) = 8193.22 + 0.205 \times 5862 = 8193.22 + 1201.71 = 9394.93.
$$

Step 4: the credit amounts add up to $16452 + 1501 + 3044.25 + 1059.50 = 22056.75$, and at 14% the credits are $0.14 \times 22056.75 = 3087.945$. The federal tax is $9394.93 - 3087.945 = 6306.985$, about \$6,306.99. (This one lands exactly on half a cent. Whether you round it up or down, the grand total below is \$9,725.50 to the cent.)

Step 5: the Ontario tax before credits is

$$
0.0505 \times 53891 + 0.0915 \times (64385 - 53891) = 2721.4955 + 960.201 = 3681.6965.
$$

Step 6: the Ontario credit amounts add up to $12989 + 3044.25 + 1059.50 = 17092.75$, and at 5.05% the credits are $863.1839$. The Ontario basic tax is $3681.6965 - 863.1839 = 2818.5126$, about \$2,818.51.

Step 7: $B = 2818.51$ is below \$5,818, so the surtax is \$0.

Step 8: a taxable income of \$64,385 is in the \$48,000 to \$72,000 band, so the premium is \$600.

Step 9: the total income tax is $6306.985 + 2818.5126 + 0 + 600 = 9725.4976$, which is \$9,725.50. The effective rate is $9725.50 \div 65000 = 0.1496$, about 15.0%. The next dollar of taxable income is in the 20.5% federal bracket (above \$58,523) and the 9.15% Ontario bracket (above \$53,891), so the marginal rate is $20.5\% + 9.15\% = 29.65\%$.

Step 10: take-home pay is $65000 - 9725.50 - 3659.25 - 1059.50 = 50555.75$. The employee keeps \$50,555.75 of \$65,000, about 77.8%. Check: 15% of \$65,000 is \$9,750, close to the tax, and a marginal rate near 30% with an effective rate near half of it is what the figure below shows at this income.

The marginal rate and the effective rate are different numbers for good reasons. On the next \$1,000 of salary the employee would pay about \$296.50 in income tax by the bracket rates, while the tax on the first \$65,000 averages \$0.15 per dollar.

![Marginal tax rate as a staircase and average tax rate as a smooth curve against taxable income from 0 to 300 thousand dollars. The marginal rate steps up from 0 to 5.05%, 19.05%, 23.15%, 29.65%, then 31.5%, 34%, 38%, 43.4%, 45%, 48%, 49.6% and 53.5% as brackets and the Ontario surtax kick in. The average rate rises slowly, reaching about 14.7% at 60 thousand and 38% at 300 thousand.](../../assets/figures/08-financial-math/income-tax-brackets-marginal-vs-effective-rates.svg)

The figure shows the combined federal and Ontario rates on taxable income, using only the basic personal amounts as credits and leaving out the Health Premium. The staircase is the marginal rate. The curve is the effective rate: it always stays below the staircase, and it creeps up toward the top rate without reaching it.

</div>

<div class="example" markdown>

### Example 2: a \$90,000 salary, where the caps apply

Take an income of \$90,000 (made up). Now the contribution caps matter.

Step 1: CPP applies to earnings only up to \$74,600, so the pensionable earnings are \$71,100. CPP is $0.0595 \times 71100 = 4230.45$, with base $3519.45$ and enhanced $711.00$. Earnings between \$74,600 and \$85,000 pay the second CPP at 4%, which is $0.04 \times 10400 = 416.00$. EI stops at \$68,900, so it is the maximum, $1123.07$.

Step 2: taxable income is $90000 - 711 - 416 = 88873$.

Steps 3 and 4: the federal tax before credits is $8193.22 + 0.205 \times (88873 - 58523) = 8193.22 + 6221.75 = 14414.97$. The credits are $0.14 \times (16452 + 1501 + 3519.45 + 1123.07) = 0.14 \times 22595.52 = 3163.37$. The federal tax is \$11,251.60.

Steps 5 and 6: Ontario before credits is $2721.4955 + 0.0915 \times (88873 - 53891) = 2721.4955 + 3200.853 = 5922.35$. The credits are $0.0505 \times (12989 + 3519.45 + 1123.07) = 890.39$. The Ontario basic tax is \$5,031.96.

Step 7: \$5,031.96 is under \$5,818, so there is still no surtax. Step 8: the premium is \$750 (band from \$72,000 to \$200,600).

Step 9: the total income tax is $11251.60 + 5031.96 + 750 = 17033.55$, an effective rate of $17033.55 \div 90000 = 18.9\%$. The marginal rate is still 29.65%. The take-home pay is $90000 - 17033.55 - (4230.45 + 416.00 + 1123.07) = 67196.93$.

Check: the effective rate rose from 15.0% to 18.9% while the marginal rate stayed at 29.65%, which fits the picture: the effective rate moves toward the marginal rate slowly. Above \$74,600 CPP stops rising, so each extra dollar between \$85,000 and \$90,000 has no CPP at all.

</div>

<div class="example" markdown>

### Example 3: a raise that crosses a bracket limit

A made-up employee earning \$58,000 gets a \$2,000 raise to \$60,000. Their taxable income goes from \$57,455 to \$59,435, so it crosses the federal limit of \$58,523. Does take-home pay fall?

Running the 10 steps at each salary gives the following (every figure is for 2026 and rounded to the cent):

| | At \$58,000 | At \$60,000 | Change |
|---|---|---|---|
| CPP and EI | \$4,188.15 | \$4,339.75 | \$151.60 |
| Income tax | \$7,827.92 | \$8,320.50 | \$492.58 |
| Take-home pay | \$45,983.93 | \$47,339.75 | \$1,355.82 |

The raise is \$2,000. Payroll contributions take \$151.60 of it and income tax takes \$492.58, so the employee keeps \$1,355.82, which is 67.8% of the raise. Take-home pay goes up, as Theorem 1 says.

The dollars in the raise are not all taxed at the same rate. Only the \$912 of taxable income above \$58,523 ($59435 - 58523$) is taxed at the higher federal rate of 20.5%, and the rest of the raise is taxed at 14%. The "tax goes up by \$492.58" is less than 29.65% of the raise ($0.2965 \times 2000 = 593$) because most of the raise is in the lower bracket and because the extra CPP and EI create extra credits.

<div class="warning" markdown>

Watch out: the myth says that "a raise can push you into a higher bracket and lower your take-home pay". It would be true for a tax that applied the higher rate to your whole income. It is false for brackets. Taxing the whole \$60,000 at 20.5% would give $0.205 \times 60000 = 12300$, far more than the real \$8,320.50. Some benefits do work differently: the Canada Child Benefit and the GST/HST credit shrink as income grows, and a few programs end at a hard income limit. Those are separate rules, not the tax brackets.

</div>

</div>

<div class="example" markdown>

### Example 4: an RRSP contribution that crosses a limit (finish it yourself)

The \$65,000 employee from Example 1 puts \$8,000 into an RRSP and deducts it. How much income tax does the deduction save?

Step 1: the deduction lowers taxable income from \$64,385 to \$56,385. The federal limit \$58,523 lies between them, and the Ontario limit \$53,891 does not.

Step 2: split the \$8,000 by bracket. The part from \$58,523 up to \$64,385 is \$5,862, and it is worth the combined rate $20.5\% + 9.15\% = 29.65\%$. The part from \$56,385 down to \$58,523 is $58523 - 56385 = 2138$, and it is worth $14\% + 9.15\% = 23.15\%$.

Now add the two savings and compare with 29.65% of \$8,000.

<details class="solution" markdown>
<summary>Finish</summary>

The savings are $0.2965 \times 5862 = 1738.08$ and $0.2315 \times 2138 = 494.95$, for \$2,233.03 in total. That is 27.9% of the contribution, below the 29.65% rate at the top. The \$8,000 effectively costs \$5,766.97 after the refund.

Check: the full calculator (see In code) gives the same \$2,233.03. A \$5,000 contribution stays in the top bracket, so it saves exactly $0.2965 \times 5000 = 1482.50$. The Health Premium stays at \$600 because both taxable incomes are in the same band.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: do not apply your top bracket's rate to all of your income. At \$65,000, taxing everything at the marginal 29.65% would give \$19,272.50, double the real \$9,725.50. Only the slices above the limits pay the higher rates.

</div>

<div class="warning" markdown>

Watch out: a credit is not a deduction. A \$1,000 deduction at a marginal rate of 29.65% saves \$296.50, and a \$1,000 credit at the lowest federal rate saves \$140 federally (plus \$50.50 in Ontario), whoever you are. When you compare "claim it as a deduction" with "claim it as a credit", multiply by the right rate.

</div>

<div class="warning" markdown>

Watch out: credits can only cancel tax, not create a refund. For a taxable income of \$15,000 the federal tax before credits is \$2,100, but the basic personal amount alone is worth $0.14 \times 16452 = 2303.28$, so the federal tax is \$0, not a negative number.

</div>

<div class="warning" markdown>

Watch out: the combined marginal rate is not always the two bracket rates added. Once the Ontario surtax applies, an extra dollar of Ontario tax also raises the surtax, so the Ontario part is multiplied by 1.2 and then by 1.56. At a taxable income of \$140,000 the marginal rate is $26\% + 11.16\% \times 1.56 = 43.41\%$, not $26\% + 11.16\% = 37.16\%$.

</div>

The surtax starts when the Ontario basic tax passes \$5,818, which happens at an income of roughly \$100,000 for an employee, so it does not affect the \$65,000 salary. The top combined marginal rate in 2026 is $33\% + 13.16\% \times 1.56 = 53.53\%$.

The tax withheld from each paycheque is the employer's estimate. At filing time the real tax is computed on the whole year, and the difference comes back as a refund or is owed. A refund is your own money coming back, not a bonus. Extra deductions such as an RRSP contribution lower the real tax, and you get the money back as a refund unless you also tell the employer to withhold less.

## Tricks and shortcuts

The 10 steps give the exact answer, and these give a fast estimate.

For credits, multiply the amount by the lowest rate. The two basic personal amounts alone are worth $0.14 \times 16452 + 0.0505 \times 12989 = 2303.28 + 655.94 = 2959.22$ dollars a year before anything else is counted.

For a quick effective rate, compute the tax on the top bracket only and remember that the earlier brackets average lower. For \$65,000 the marginal rate is 29.65% and the effective rate is about half of it.

For a deduction, find which side of each limit the deduction leaves you on. If the whole deduction stays in one bracket, multiply by the marginal rate. If it crosses a limit, split it, as in Example 4.

To find the income at which you enter a bracket, run the tax backward: tax at the start of the bracket plus $r(x - b)$. For example, the federal tax before credits at \$58,523 is \$8,193.22, and a federal tax of exactly \$20,000 before credits needs $x = 58523 + \frac{20000 - 8193.22}{0.205} = 116117.05$.

## In code

The function below computes a simplified 2026 Ontario tax. It follows the 10 steps, so every line corresponds to a step. It is a calculator for this lesson, not a tax return.

<details class="code" markdown>
<summary>In code</summary>

```python
FED = [(58_523, 0.14), (117_045, 0.205), (181_440, 0.26), (258_482, 0.29), (float("inf"), 0.33)]
ONT = [(53_891, 0.0505), (107_785, 0.0915), (150_000, 0.1116), (220_000, 0.1216), (float("inf"), 0.1316)]


def slices(taxable, brackets):
    """Tax before credits: each rate applies only to the part of income inside its bracket."""
    tax, lower = 0.0, 0.0
    for upper, rate in brackets:
        tax += rate * max(0.0, min(taxable, upper) - lower)
        lower = upper
    return tax


def health_premium(taxable):
    """Ontario Health Premium, simplified to the top of each band (see the list of omissions)."""
    for upper, amount in [(20_000, 0), (36_000, 300), (48_000, 450), (72_000, 600), (200_600, 750)]:
        if taxable <= upper:
            return amount
    return 900


def tax_2026(income, rrsp=0.0):
    """Simplified 2026 federal + Ontario tax for an employee with only employment income."""
    pensionable = max(0.0, min(income, 74_600) - 3_500)
    cpp_base = 0.0495 * pensionable              # credit
    cpp_enhanced = 0.0100 * pensionable          # deduction
    cpp2 = 0.04 * max(0.0, min(income, 85_000) - 74_600)   # deduction
    ei = 0.0163 * min(income, 68_900)            # credit
    taxable = income - cpp_enhanced - cpp2 - rrsp

    # federal basic personal amount shrinks from $16,452 to $14,829 between $181,440 and $258,482
    shrink = (min(max(taxable, 181_440), 258_482) - 181_440) / (258_482 - 181_440)
    fed_bpa = 16_452 - (16_452 - 14_829) * shrink
    fed_credits = 0.14 * (fed_bpa + min(1_501, income) + cpp_base + ei)
    federal = max(0.0, slices(taxable, FED) - fed_credits)

    ont_credits = 0.0505 * (12_989 + cpp_base + ei)
    ont_basic = max(0.0, slices(taxable, ONT) - ont_credits)
    surtax = 0.20 * max(0.0, ont_basic - 5_818) + 0.36 * max(0.0, ont_basic - 7_446)
    premium = health_premium(taxable)

    total = federal + ont_basic + surtax + premium
    return {"taxable": taxable, "federal": federal, "ontario": ont_basic, "surtax": surtax,
            "premium": premium, "total": total, "effective": total / income,
            "payroll": cpp_base + cpp_enhanced + cpp2 + ei}


r = tax_2026(65_000)
print({k: round(v, 4) for k, v in r.items()})
print(round(65_000 - r["total"] - r["payroll"], 2))      # take-home

# marginal rate by brute force: tax on one more dollar
print(round(tax_2026(65_001)["total"] - r["total"], 4))

# an RRSP deduction of $5,000
print(round(r["total"] - tax_2026(65_000, rrsp=5_000)["total"], 2))

# the raise myth: take-home rises with income, even across a bracket limit
def take_home(x):
    t = tax_2026(x)
    return x - t["total"] - t["payroll"]

print(all(take_home(x + 1) > take_home(x) for x in range(10_000, 300_000, 37)))
```

The output is `{'taxable': 64385.0, 'federal': 6306.985, 'ontario': 2818.5126, 'surtax': 0.0, 'premium': 600, 'total': 9725.4976, 'effective': 0.1496, 'payroll': 4718.75}`, then `50555.75`, `0.281`, `1482.5` and `True`. The brute-force marginal rate is 0.281, not 0.2965, because one more dollar of pay also raises the CPP and EI credits and the enhanced CPP deduction a little. The bracket rate of 29.65% is the rate on the extra dollar of taxable income, and the 28.1% includes those small side effects. The raise test checks that take-home pay rises at every income it samples, which is evidence and not a proof; Theorem 1 is the proof.

The function is simplified. It leaves out:

- the Ontario Tax Reduction, a credit for lower-income filers, and the phase-in of the Health Premium within each band;
- other credits and deductions: tuition, student loan interest, medical expenses, donations, union dues, moving and child care costs, and the age and pension amounts;
- other kinds of income: self-employment, capital gains (only half is taxed), dividends and their credits, interest, rent and OAS, and the OAS clawback;
- benefits that depend on income (the Canada Child Benefit, the GST/HST credit, the Ontario Trillium Benefit);
- part-year residence, Quebec, and how the employer actually withholds tax during the year;
- indexation: it uses the 2026 figures at every income, so it is not a forecast for later years.

</details>

## FAQ

### Why does the effective rate stay below the marginal rate?

Because $T(x)/x$ averages the rates of all the slices up to $x$, and the lower slices have lower rates. The average of a list that ends with its largest number is below that number unless every number is equal. The credits push the average down further, since they take a fixed amount off the tax. Only at incomes so high that the first slices are tiny compared with the rest does the effective rate approach the top marginal rate.

### Why is the surtax computed on tax and not on income?

It is a rule of the Ontario tax system, and it works as an extra layer on the Ontario tax. The effect is to raise the Ontario marginal rate by 20% (and later by 56%) of itself. For modelling, treat it as part of the Ontario tax function $B \mapsto B + 0.2\max(0, B - 5818) + 0.36\max(0, B - 7446)$, which is another piecewise linear function of $B$, and so it is continuous too.

### Can earning more ever leave me with less money?

Not through the income tax brackets, by Theorem 1. It can happen through a benefit with a hard income cut-off. If losing a \$1,000 benefit comes with crossing \$50,000, a \$500 raise across that line loses money; Practice problem 7 works this out. Phase-outs, where the benefit shrinks by cents per dollar, do not do this: they raise the effective marginal rate but keep it under 100%.

### Is an RRSP deduction always worth the marginal rate?

It is worth the marginal rate today. The money is taxed again when you take it out of the RRSP, at the rate you pay then. So the comparison with a TFSA is about today's marginal rate against your marginal rate at withdrawal. That comparison is in [retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md).

## Practice

### Warm-up

1\. A taxable income is \$68,523. Find the federal tax before credits and the average rate on that income.

<details class="solution" markdown>
<summary>Solution</summary>

The first \$58,523 pays 14%: \$8,193.22. The other $68523 - 58523 = 10000$ pays 20.5%: \$2,050. The tax is $8193.22 + 2050 = 10243.22$, so \$10,243.22. The average rate is $10243.22 \div 68523 = 0.14949$, about 14.9%.

Check: the average is between 14% and 20.5%, closer to 14% because most of the income is in the first bracket.

</details>

2\. A person has a taxable income of \$15,000. (a) What are the federal and Ontario credits for the basic personal amounts? (b) What is their federal tax if these are their only credits?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Federal: $0.14 \times 16452 = 2303.28$. Ontario: $0.0505 \times 12989 = 655.9445$, so \$655.94.

(b) The federal tax before credits is $0.14 \times 15000 = 2100$. The credit is larger, and a non-refundable credit can only reduce the tax to 0, so the federal tax is \$0.

Check: the tax of \$2,100 is less than \$2,303.28, so the credit covers it all.

</details>

3\. Use the bracket rates only. What are the combined federal and Ontario marginal rates at a taxable income of \$58,500 and at \$58,600? What is the tax on the \$58,524th dollar?

<details class="solution" markdown>
<summary>Solution</summary>

At \$58,500 the federal rate is 14% (under \$58,523) and the Ontario rate is 9.15% (above \$53,891), so the combined rate is 23.15%. At \$58,600 the federal rate is 20.5%, so the combined rate is $20.5\% + 9.15\% = 29.65\%$. The dollar from \$58,523 to \$58,524 is the first one in the 20.5% bracket, so it is taxed $0.205 + 0.0915 = 0.2965$, that is, 29.65 cents.

Check: the jump from 23.15% to 29.65% is 6.5 points, which is the difference between 20.5% and 14%.

</details>

### Standard

4\. An Ontario employee earns \$30,000 (made up). Find the total 2026 income tax, the effective rate and the take-home pay.

<details class="solution" markdown>
<summary>Solution</summary>

Pensionable earnings are $30000 - 3500 = 26500$. CPP is base $0.0495 \times 26500 = 1311.75$ and enhanced $0.01 \times 26500 = 265.00$. EI is $0.0163 \times 30000 = 489.00$. Taxable income is $30000 - 265 = 29735$.

Federal before credits: $0.14 \times 29735 = 4162.90$. Credits: $0.14 \times (16452 + 1501 + 1311.75 + 489) = 0.14 \times 19753.75 = 2765.525$. Federal tax: $1397.375$.

Ontario before credits: $0.0505 \times 29735 = 1501.6175$. Credits: $0.0505 \times (12989 + 1311.75 + 489) = 0.0505 \times 14789.75 = 746.88$. Ontario basic tax: $754.735$. No surtax. The premium for a taxable income in the \$25,000 to \$36,000 range is \$300.

Total: $1397.375 + 754.735 + 300 = 2452.11$, so \$2,452.11. Effective rate: $2452.11 \div 30000 = 8.17\%$, about 8.2%. Take-home: $30000 - 2452.11 - 1311.75 - 265.00 - 489.00 = 25482.14$, \$25,482.14.

Check: the function in In code returns 2452.11 for \$30,000, and 8.2% is much below the \$65,000 case's 15.0%, as it should be, since the basic credits remove a larger share of the tax.

</details>

5\. An Ontario basic tax is \$9,000. Find the surtax and the total Ontario tax before the Health Premium.

<details class="solution" markdown>
<summary>Solution</summary>

The surtax is 20% of the part above \$5,818 plus 36% of the part above \$7,446: $0.20 \times (9000 - 5818) = 0.20 \times 3182 = 636.40$ and $0.36 \times (9000 - 7446) = 0.36 \times 1554 = 559.44$. The surtax is $636.40 + 559.44 = 1195.84$. The total Ontario tax is $9000 + 1195.84 = 10195.84$, that is, \$10,195.84.

Check: the surtax is 13.3% of the basic tax, between the 20% that applies to the first part and the 56% that applies to the top part.

</details>

6\. A federal tax before credits of exactly \$20,000 is owed. What taxable income does that correspond to?

<details class="solution" markdown>
<summary>Solution</summary>

The tax at the end of the second bracket, \$117,045, is $8193.22 + 0.205 \times 58522 = 20190.23$. Since \$20,000 is less than that, the income is in the second bracket. Solve $8193.22 + 0.205(x - 58523) = 20000$: $x - 58523 = 11806.78 \div 0.205 = 57594.05$, so $x = 116117.05$, that is, \$116,117.05.

Check: $8193.22 + 0.205 \times 57594.05 = 8193.22 + 11806.78 = 20000.00$.

</details>

### Challenge

7\. (A made-up benefit.) A program pays \$1,000, but only to people whose income is \$50,000 or less. Use the bracket rate of 19.05% (14% federal plus 5.05% Ontario) on the whole raise and ignore CPP and EI. (a) Someone at \$49,500 gets a \$1,500 raise to \$51,000. Do they come out ahead? (b) How big does the raise have to be to break even? (c) Why does Theorem 1 not contradict this?

<details class="solution" markdown>
<summary>Solution</summary>

(a) After tax, the raise is worth $1500 \times (1 - 0.1905) = 1214.25$. The benefit is lost, so the net change is $1214.25 - 1000 = 214.25$. They come out ahead, by \$214.25.

(b) A raise $h$ that crosses the limit nets $h(1 - 0.1905) - 1000 = 0.8095h - 1000$. This is zero at $h = 1000 \div 0.8095 = 1235.33$. Any raise that crosses the \$50,000 line but is under about \$1,235.34 leaves the person worse off; for example, a \$600 raise nets $0.8095 \times 600 - 1000 = -514.30$.

(c) Theorem 1 is about the tax function $T$ only. The benefit is another rule added to it, and a rule with a jump (a cliff) breaks continuity. The income tax brackets themselves never create such a drop.

Check: at $h = 1235.34$, $0.8095 \times 1235.34 = 1000.00$ to the cent, so the net change is 0. In (a) the raise of \$1,500 is above the break-even raise, which agrees with the positive answer.

</details>

8\. (Reviews [piecewise functions](../../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md).) Write the Ontario tax before credits $T(x)$ as a piecewise function for the first three brackets (the third being all taxable income above \$107,785 up to \$150,000). Find $T(100000)$, and check that the pieces agree at \$107,785.

<details class="solution" markdown>
<summary>Solution</summary>

The tax at \$53,891 is $0.0505 \times 53891 = 2721.4955$. The tax at \$107,785 is $2721.4955 + 0.0915 \times (107785 - 53891) = 2721.4955 + 4931.301 = 7652.7965$. So

$$
T(x) =
\begin{cases}
0.0505\,x & \text{if } 0 \le x \le 53891, \\
2721.4955 + 0.0915\,(x - 53891) & \text{if } 53891 < x \le 107785, \\
7652.7965 + 0.1116\,(x - 107785) & \text{if } 107785 < x \le 150000.
\end{cases}
$$

At \$100,000: $T(100000) = 2721.4955 + 0.0915 \times 46109 = 2721.4955 + 4218.9735 = 6940.469$, about \$6,940.47.

Check at the break point: the second piece at \$107,785 gives \$7,652.7965, and the third piece gives $7652.7965 + 0.1116 \times 0 = 7652.7965$. They agree, so $T$ is continuous there, as Theorem 1 says. The slopes 0.0505, 0.0915 and 0.1116 are the rates.

</details>

## Where this shows up

- The next lesson treats insurance as an expected-value problem: [insurance and expected value](02-insurance-and-expected-value.md). The RRSP, TFSA and FHSA rules use your marginal rate: [retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md). The capstone in [spreadsheet finance functions and a capstone plan](03-spreadsheet-finance-functions-and-capstone.md) uses this calculator for every paycheque.
- Economics: the marginal rate is a marginal cost of earning, and it shapes how much people choose to work ([rates of change and marginal analysis](../../05-university-core/03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md)).
- Computing: the tax function is a prefix sum over slices, the same shape as a cumulative distribution function built from a table, and "marginal" is the derivative of a piecewise linear function.
