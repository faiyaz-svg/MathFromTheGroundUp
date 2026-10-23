# Spreadsheet finance functions and a capstone plan

After this lesson you can use the spreadsheet functions PMT, FV, PV, NPER, RATE, NPV, IRR, EFFECT and NOMINAL with the right signs, match each one to its formula, write Python versions of them, and lay out a five-year money plan as a spreadsheet table.

Before this: [present and future value](../03-time-value-of-money/01-present-and-future-value.md), [annuities and geometric series](../03-time-value-of-money/02-annuities-and-geometric-series.md), [the loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md) and [income tax brackets: marginal vs effective](01-income-tax-brackets-marginal-vs-effective.md).

All rates, prices and salaries in the capstone are made up. Tax figures are the 2026 figures from the first lesson of this chapter, used in every year of the plan. The plan shows how the math fits together. It is not advice on what to buy.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. What does `=PMT(0.06/12, 36, 10000)` return, and why is the sign what it is?
2. What does `=NPV(0.10, 121)` return?
3. What does `=EFFECT(0.12, 12)` return?

<details class="solution" markdown>
<summary>Answers</summary>

1. It returns $-304.22$. The \$10,000 is money you receive (positive) and the payments are money you pay out (negative). The payment is $10000 \cdot \frac{0.005}{1 - 1.005^{-36}} = 304.22$.
2. The single value 121 is received one period from now, so `NPV` discounts it once: $121 \div 1.10 = 110$.
3. $(1 + 0.12/12)^{12} - 1 = 0.12683$, that is, 12.68%.

</details>

## The idea

Every formula from the finance chapters has a spreadsheet function, and the formulas and the functions agree to the cent. A spreadsheet is how most people actually run these numbers, so the skill is to read a function call as a formula, and to know which sign each argument needs. The signs are where most mistakes happen: the function does not know which money is yours.

A spreadsheet is also a good way to lay out a plan. Years go across the top, each row is one line of the plan, and each cell is a formula that refers to cells above it. The capstone below does this for a made-up graduate, and each row of the table comes from a lesson in this book.

## Definitions

A **cash flow** is an amount of money together with the time it is paid or received. The **sign convention** of the spreadsheet functions is that money you receive is positive and money you pay is negative. A loan gives the borrower a positive amount now and negative payments later. A deposit plan gives the saver negative payments now and a positive balance later.

An **ordinary annuity** pays at the end of each period, and an **annuity due** pays at the start of each period. In the functions, the argument `type` is 0 for an ordinary annuity (the default) and 1 for an annuity due.

The **net present value** (NPV) of cash flows $C_0, C_1, \ldots, C_n$ at the rate $i$ per period is

$$
\text{NPV} = \sum_{k=0}^{n} \frac{C_k}{(1+i)^k}.
$$

The **internal rate of return** (IRR) is the rate $i$ at which the NPV is exactly 0. In plain words, the NPV is the value today of the whole series, and the IRR is the rate of growth that the series itself earns. Both are taught with bonds in [present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md).

## How to do it

### The nine functions

Here $i$ is the rate per period (the yearly rate divided by the number of periods a year), $n$ is the number of periods, $A$ is the payment, $P$ is the present value and $F$ is the future value. Every function uses the same equation for an ordinary annuity:

$$
P\,(1+i)^n + A\,\frac{(1+i)^n - 1}{i} + F = 0.
$$

It says that the loan or deposit, the payments with their interest and the final balance add to zero when you count money in as positive and money out as negative. Each function solves this one equation for a different unknown.

| Function | Finds | Formula | Taught in |
|---|---|---|---|
| `PMT(rate, nper, pv, [fv], [type])` | the payment $A$ | $A = -\dfrac{P(1+i)^n + F}{\frac{(1+i)^n - 1}{i}}$ | [loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md) |
| `FV(rate, nper, pmt, [pv], [type])` | the future value $F$ | $F = -\left[P(1+i)^n + A\,\frac{(1+i)^n - 1}{i}\right]$ | [annuities and geometric series](../03-time-value-of-money/02-annuities-and-geometric-series.md) |
| `PV(rate, nper, pmt, [fv], [type])` | the present value $P$ | $P = -\dfrac{F + A\,\frac{(1+i)^n - 1}{i}}{(1+i)^n}$ | [present and future value](../03-time-value-of-money/01-present-and-future-value.md) |
| `NPER(rate, pmt, pv, [fv], [type])` | the number of periods $n$ | take logarithms of the equation | [logarithms](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md) |
| `RATE(nper, pmt, pv, [fv], [type])` | the rate $i$ | no closed form, solved by search | numerical root finding |
| `NPV(rate, value1, ...)` | the present value of future cash flows | $\sum_{k=1}^{n} \frac{C_k}{(1+i)^k}$ | [present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md) |
| `IRR(values)` | the rate with NPV 0 | solve $\sum_{k=0}^{n} \frac{C_k}{(1+i)^k} = 0$ | same lesson |
| `EFFECT(nominal_rate, npery)` | the effective annual rate | $\left(1 + \frac{r}{m}\right)^m - 1$ | [APR, APY and the effective annual rate](../02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md) |
| `NOMINAL(effect_rate, npery)` | the nominal annual rate | $m\left[(1 + r_e)^{1/m} - 1\right]$ | same lesson |

The `type` argument turns the ordinary annuity into an annuity due. The next theorem says exactly what it does.

*Theorem 1 (annuity due).* The future value of $n$ payments of $A$ made at the start of each period is $(1 + i)$ times the future value of the same payments made at the end of each period.

We know the future value of an ordinary annuity, $A\frac{(1+i)^n - 1}{i}$. We want the version where every payment is made one period earlier. The plan is to notice that each payment then earns exactly one more period of interest.

*Proof.* In the ordinary annuity the payment made at time $k$ grows for $n - k$ periods, for $k = 1, \ldots, n$. In the annuity due the same payment is made one period earlier, so it grows for $n - k + 1$ periods, which multiplies its value by $(1+i)$. Every payment is multiplied by the same factor, so the sum is multiplied by it too. $\blacksquare$

Look back: with a made-up 4% and five payments of \$5,600, the ordinary annuity is \$30,331.41 and the annuity due is $30331.41 \times 1.04 = 31544.66$. The same factor appears in `PMT`: paying at the start lowers the payment needed for a goal by the factor $1.04$.

### Using the functions

1. Choose the unknown: payment, balance, present value, number of periods or rate.
2. Divide the yearly rate by the number of periods a year, and count the periods ($0.072/12$ and 60 for a five-year monthly loan).
3. Decide the direction of each cash flow and give it a sign: money you receive positive, money you pay negative.
4. Decide whether payments are at the end (`type` 0) or the start (`type` 1) of the period.
5. Check the sign of the answer. A `PMT` for a loan should be negative if the loan amount is positive. A `PV` of payments you will receive should be positive.
6. Check the number with a rough calculation: total payments are about the loan plus interest.

For `NPV`, add one step: the function discounts the first value by one full period. If your first cash flow is today, keep it outside: `=C0 + NPV(rate, C1:Cn)`.

## Worked examples

<div class="example" markdown>

### Example 1: a car loan with PMT, then RATE

A made-up car loan is \$18,000 at a nominal 7.2% a year, paid monthly for 60 months. Find the payment, the interest paid, and check the rate.

Steps 1 and 2: the unknown is the payment, the monthly rate is $0.072/12 = 0.006$, and $n = 60$.

Steps 3 and 4: the \$18,000 is money received, so $P = +18000$ and $F = 0$. Payments are at the end of each month.

Step 5: the spreadsheet formula `=PMT(0.072/12, 60, 18000)` returns $-358.12$:

$$
A = 18000 \cdot \frac{0.006}{1 - 1.006^{-60}} = 358.1225.
$$

The negative sign is correct, because it is money you pay.

Step 6: 60 payments total $358.1225 \times 60 = 21{,}487.35$, so the interest is $21487.35 - 18000 = 3487.35$. Check with a rough estimate: the balance shrinks from \$18,000 to 0, so the average balance is about \$9,000 and the interest is about $0.072 \times 5 \times 9000 = 3240$. The true figure, \$3,487.35, is a little higher because the balance falls more slowly early on.

To go backwards, `=RATE(60, -358.1225, 18000)` gives 0.006, which is 0.6% a month. Multiply by 12 for the nominal 7.2%. The effective annual rate is `=EFFECT(0.072, 12)`, which is 7.44%.

</div>

<div class="example" markdown>

### Example 2: NPV, IRR and the off-by-one trap

A made-up project costs \$1,000 today and pays \$300, \$400 and \$500 at the ends of years 1, 2 and 3. At a discount rate of 6%, is it worth doing, and what is its IRR?

The cash flows are $C_0 = -1000$, then 300, 400 and 500. The spreadsheet formula that is right is `=-1000 + NPV(0.06, 300, 400, 500)`:

$$
\text{NPV} = -1000 + \frac{300}{1.06} + \frac{400}{1.06^2} + \frac{500}{1.06^3} = -1000 + 1058.83 = 58.83.
$$

The NPV is positive at 6%, so the project is worth more than its cost at that discount rate. The IRR is the rate that makes the NPV 0, `=IRR({-1000,300,400,500})`, which is 8.90%. The NPV is positive exactly when the discount rate is below the IRR, and 6% is below 8.90%.

The trap: writing `=NPV(0.06, -1000, 300, 400, 500)` treats the \$1,000 as if it were paid one year from now. The whole series is then discounted one period too many, so the result is $\frac{58.83}{1.06} = 55.50$, too low by a factor of 1.06. Check: the wrong formula's value is 55.50, and $58.83 \div 1.06 = 55.50$.

</div>

<div class="example" markdown>

### Example 3: saving with the type argument

You want \$30,000 in 5 years in an account that earns a made-up 4% a year. How much do you need to save each year, paying at the end of the year, and at the start?

At the end of each year: `=PMT(0.04, 5, 0, 30000)` returns $-5538.81$, so \$5,538.81 a year. At the start of each year: `=PMT(0.04, 5, 0, 30000, 1)` returns $-5325.78$, so \$5,325.78 a year.

Check with Theorem 1: $5538.81 \div 1.04 = 5325.78$. The ordinary payment is the due payment times 1.04. Also, $5538.81 \times 5.41632 = 30000$, where 5.41632 is the future value of 1 a year for 5 years at 4%.

</div>

<div class="example" markdown>

### Example 4: how long to pay off a balance (finish it yourself)

You owe \$10,000 at a nominal 6% a year, compounded monthly, and pay \$300 a month. How many payments does it take?

Steps 1 to 4: the unknown is $n$, the monthly rate is $0.005$, $P = +10000$ and $A = -300$.

Step 5: `=NPER(0.005, -300, 10000)` should be positive. Compute it, then decide how many payments are really needed, and what the last one is.

<details class="solution" markdown>
<summary>Finish</summary>

$n = \frac{\ln\left(\frac{z - F}{z + P}\right)}{\ln(1+i)}$ with $z = \frac{A}{i} = -60000$ and $F = 0$: $n = \frac{\ln(60000 \div 50000)}{\ln 1.005} = \frac{\ln 1.2}{\ln 1.005} = 36.56$.

The answer is not a whole number, and that is fine: you need 37 payments. After 36 payments of \$300 the balance is \$165.97, so the 37th payment is $165.97 \times 1.005 = 166.80$.

Check: $36 \times 300 + 166.80 = 10966.80$, which is \$966.80 over the \$10,000 loan, plausible for interest at 6% on a balance that falls over three years.

</details>

</div>

## Capstone: a five-year plan

A made-up graduate, Sam, starts a job in Ontario in 2026 at \$65,000 and gets a \$2,000 raise each year. This plan puts together the whole book so far. Every step is linked to the lesson it uses.

### The pieces

The paycheque. For each year, apply the 10 steps of the tax lesson ([income tax brackets: marginal vs effective](01-income-tax-brackets-marginal-vs-effective.md); payroll and budgeting are in [paycheques and budgeting](../01-everyday-money/03-paycheques-and-budgeting.md)). At \$65,000 the take-home pay is \$50,555.75, and for the five salaries it is \$50,556, \$51,842, \$53,130, \$54,443 and \$55,605 (rounded to dollars).

Student loans. Sam owes \$28,000: \$16,000 federal and \$12,000 Ontario. The federal part charges no interest ([National Student Loans Service Centre](https://www.csnpe-nslsc.canada.ca/en/things-you-need-to-know)). The Ontario part charges prime plus 1%, so the plan uses a made-up rate of 6% ([OSAP repayment](https://www.ontario.ca/page/pay-back-osap)). There is a six-month grace period, and interest on the Ontario part during it is added to the balance: $12000 \times 1.005^6 = 12364.53$. Then Sam repays both parts over 120 months. The Ontario payment is `=PMT(0.06/12, 120, 12364.53)`, which is \$137.27 a month, and the federal payment is $16000 \div 120 = 133.33$. Together that is \$270.60 a month, paid for 6 months in year 1 and 12 months in every later year. After 54 payments (the end of year 5) the Ontario balance is \$7,700.52 and the federal balance is \$8,800.00. Student loans are the topic of [student loans](../04-borrowing/01-student-loans.md).

Living costs. Rent, food, transit, phone, insurance and other costs total \$31,500 in year 1 and grow 3% a year (made up). Inflation is covered in [inflation and real returns](../02-interest-and-growth/06-inflation-and-real-returns.md).

Emergency fund. The first goal is three months of living costs plus loan payments: $3 \times (31500/12 + 270.60) = 8686.81$, which the plan rounds to \$8,700 and holds as cash. This is self-insurance, the idea behind [insurance and expected value](02-insurance-and-expected-value.md): a loss you can pay yourself is not worth paying a loading to insure.

Home savings. Sam wants a down payment on a \$550,000 home in five years. The minimum down payment is 5% of the first \$500,000 and 10% of the rest ([FCAC](https://www.canada.ca/en/financial-consumer-agency/services/mortgages/down-payment.html)), which is $25000 + 5000 = 30000$ dollars. At a made-up 4% a year, saving at the end of each year needs `=PMT(0.04, 5, 0, 30000)`, which is \$5,538.81 a year. The plan rounds up to \$5,600 a year in a First Home Savings Account (FHSA). Contributions to an FHSA are generally deductible ([CRA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/first-home-savings-account.html)), so each contribution also produces a refund the next spring. At Sam's marginal rate of 29.65% it is $0.2965 \times 5600 = 1660.40$. The rules of the three registered accounts are in [retirement accounts: RRSP, TFSA and FHSA](../06-investing-and-retirement/03-retirement-accounts.md), and housing costs in [renting vs buying a home](../05-housing/01-renting-vs-buying-a-home.md) and [mortgage basics](../05-housing/02-mortgage-basics.md).

TFSA or RRSP. Whatever is left goes into a TFSA. The reason comes from this comparison: put \$1,000 of pre-tax income into an RRSP, or pay tax now and put the rest into a TFSA. With growth factor $g = (1+r)^n$, the RRSP is worth $1000\,g\,(1 - t_{\text{later}})$ after tax when withdrawn, and the TFSA is worth $1000\,(1 - t_{\text{now}})\,g$. They are equal when the tax rate later equals the rate now, so the choice depends only on those two rates. With $r = 5\%$ and $n = 30$, $g = 4.3219$. At Sam's current marginal rate of 29.65% the TFSA gives \$3,040.49. The RRSP gives \$3,498.61 if the rate at withdrawal is 19.05%, \$3,040.49 if it is 29.65%, and \$2,445.79 if it is 43.41%. Sam's rate may be higher later, which favours the TFSA now, and the FHSA already gives the deduction for the home goal.

### The spreadsheet

Years go across the columns and each row is one line of the plan. All figures are in dollars, rounded for display, and the plan assumes payments and contributions at the end of each year.

| Row | Line | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|---|
| 1 | Salary | 65,000 | 67,000 | 69,000 | 71,000 | 73,000 |
| 2 | Take-home pay | 50,556 | 51,842 | 53,130 | 54,443 | 55,605 |
| 3 | Living costs | 31,500 | 32,445 | 33,418 | 34,421 | 35,454 |
| 4 | Student loan payments | 1,624 | 3,247 | 3,247 | 3,247 | 3,247 |
| 5 | FHSA refund from last year | 0 | 1,660 | 1,660 | 1,660 | 1,660 |
| 6 | Free cash (row 2 minus 3 minus 4 plus 5) | 17,432 | 17,810 | 18,125 | 18,435 | 18,565 |
| 7 | To emergency fund | 8,700 | 0 | 0 | 0 | 0 |
| 8 | To FHSA | 5,600 | 5,600 | 5,600 | 5,600 | 5,600 |
| 9 | To TFSA (row 6 minus 7 minus 8) | 3,132 | 12,210 | 12,525 | 12,835 | 12,965 |
| 10 | FHSA balance at 4% | 5,600 | 11,424 | 17,481 | 23,780 | 30,331 |
| 11 | TFSA balance at 5% | 3,132 | 15,499 | 28,799 | 43,074 | 58,192 |

In a spreadsheet the formulas in year-2 column C would read like this: `C3 = ROUND(31500*1.03^1, 0)`, `C6 = C2 - C3 - C4 + C5`, `C5 = 0.2965 * B8`, `C10 = B10 * 1.04 + C8` and `C11 = B11 * 1.05 + C9`. The first year's loan payment is six months' worth, `B4 = 270.60 * 6`. The FHSA balance after year 5 is \$30,331.41, which is above the \$30,000 target, and it equals `=FV(0.04, 5, -5600)`.

Checks. Row 10 reaches the goal with \$331 to spare, and the loan payments in rows 4 add up to the 54 monthly payments used in the balance above. TFSA contributions over the five years total about \$53,667. If Sam turned 18 in 2022 and has not used the room, the cumulative room is $6000 + 6500 + 7000 + 7000 + 7000 = 33500$ at the start of 2026, plus a limit that is assumed to stay at \$7,000 a year, which is \$61,500 by year 5. So the contributions fit. The TFSA limits are from the [CRA contribution limits table](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html).

### The car decision

Now suppose Sam is also considering an \$18,000 used car, financed as in Example 1 (a made-up 7.2% over 60 months, \$358.12 a month, or \$4,297 a year). Running costs of \$4,800 a year (insurance, fuel and maintenance) are made up, with \$1,000 a year saved on transit, and the car resells for \$9,000 at the end of year 5. The yearly cost is $4297.47 + 4800 - 1000 = 8097.47$. Over five years the net cost is $5 \times 8097.47 - 9000 = 31487.35$ dollars, and the present value of the costs at 4% is `=NPV(0.04, -8097.47, -8097.47, -8097.47, -8097.47, -8097.47 + 9000)`, which is $-28{,}651.15$. The loan itself costs \$3,487.35 in interest. The car and the loan are compared in [car loans and total cost](../04-borrowing/02-car-loans-and-total-cost.md) and [lease vs buy a car](../04-borrowing/03-lease-vs-buy-a-car.md).

Rerunning the plan with this extra yearly cost changes it a lot:

| Line | Without the car | With the car |
|---|---|---|
| Free cash, year 1 | 17,432 | 9,335 |
| To FHSA, year 1 | 5,600 | 635 |
| FHSA balance after year 5 | 30,331 | 24,523 |
| TFSA balance after year 5 | 58,192 | 17,779 |

With the car the emergency fund is still filled first, but the FHSA falls about \$5,500 short of the \$30,000 target at the end of year 5, and the TFSA is \$40,000 smaller. The math does not say whether the car is worth it. It says what it costs in the other goals, which is the information the decision needs.

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: sign errors. `=PV(0.05, 10, 1000)` returns $-7721.73$, since you are asked to pay that to receive \$1,000 a year, and `=PV(0.05, 10, -1000)` returns $+7721.73$. If an answer has a surprising sign, one of the inputs has the wrong direction. Give a loan amount and its payments opposite signs, and a deposit plan and its final balance opposite signs.

</div>

<div class="warning" markdown>

Watch out: the rate must match the period. For monthly payments use `rate/12` and the number of months, not the yearly rate with the number of months. `=PMT(0.072, 60, 18000)` treats the 60 as 60 yearly periods at 7.2% a year and returns \$1,316.31, which would be paid every year for 60 years. The rate and the count have to be in the same unit.

</div>

<div class="warning" markdown>

Watch out: `NPV` starts at period 1, not period 0 (Example 2). A cash flow that happens today belongs outside the function. `IRR`, in contrast, treats its first value as time 0.

</div>

`IRR` can have no answer or several answers. A series whose signs change more than once can have several rates with NPV 0 (Practice 7), and a series with all the same sign has none. `RATE` and `IRR` are solved by search, so a spreadsheet may ask for a guess or return an error if the search does not find a rate. Both functions need at least one positive and one negative cash flow.

## Tricks and shortcuts

Check any `PMT` result by multiplying by $n$: the total paid is the loan plus the interest. For a rough check, the interest on a loan paid in equal instalments is about the rate times the years times half the loan.

To get a yearly figure from a monthly one without a calculator, multiply the payment by 12, as in the \$4,297 above.

To switch a function between end-of-period and start-of-period, use Theorem 1: multiply a future value by $(1+i)$, or divide a payment by it.

For `NPV` with a cash flow today, write `=C0 + NPV(rate, C1:Cn)`. This always avoids the off-by-one trap.

## In code

`numpy-financial` is not needed: each function is a few lines. The code writes the nine functions with the spreadsheet sign convention, checks them against the values above, and then runs the capstone plan. The take-home pay figures come from the `tax_2026` function of the first lesson in this chapter.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

# Sign convention (as in a spreadsheet): money you receive is positive, money you pay is negative.
# when=0 means payments at the end of each period; when=1 means at the start (annuity due).


def fv(rate, nper, pmt, pv=0.0, when=0):
    if rate == 0:
        return -(pv + pmt * nper)
    g = (1 + rate) ** nper
    return -(pv * g + pmt * (1 + rate * when) * (g - 1) / rate)


def pv(rate, nper, pmt, fv=0.0, when=0):
    if rate == 0:
        return -(fv + pmt * nper)
    g = (1 + rate) ** nper
    return -(fv + pmt * (1 + rate * when) * (g - 1) / rate) / g


def pmt(rate, nper, pv, fv=0.0, when=0):
    if rate == 0:
        return -(pv + fv) / nper
    g = (1 + rate) ** nper
    return -(pv * g + fv) * rate / ((1 + rate * when) * (g - 1))


def nper(rate, pmt, pv, fv=0.0, when=0):
    if rate == 0:
        return -(pv + fv) / pmt
    z = pmt * (1 + rate * when) / rate
    return math.log((z - fv) / (z + pv)) / math.log(1 + rate)


def bisect(f, lo, hi):
    """Find a root of f between lo and hi, where f changes sign."""
    flo = f(lo)
    for _ in range(200):
        mid = (lo + hi) / 2
        if (f(mid) > 0) == (flo > 0):
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return (lo + hi) / 2


def rate(nper, pmt, pv, fv=0.0, when=0):
    f = lambda r: pv * (1 + r) ** nper + pmt * (1 + r * when) * ((1 + r) ** nper - 1) / r + fv
    return bisect(f, 1e-9, 1.0)          # searches rates from 0% to 100% per period


def npv(rate, values):
    """Spreadsheet NPV: the first value is discounted one full period."""
    return sum(v / (1 + rate) ** (k + 1) for k, v in enumerate(values))


def irr(values):
    f = lambda r: sum(v / (1 + r) ** k for k, v in enumerate(values))
    return bisect(f, -0.9, 1.0)


def effect(nominal_rate, npery):
    return (1 + nominal_rate / npery) ** npery - 1


def nominal(effect_rate, npery):
    return npery * ((1 + effect_rate) ** (1 / npery) - 1)


print(round(pmt(0.072 / 12, 60, 18_000), 2))             # -358.12   =PMT(0.072/12,60,18000)
print(round(fv(0.04, 5, -5_600), 2))                      # 30331.41  =FV(0.04,5,-5600)
print(round(fv(0.04, 5, -5_600, when=1), 2))              # 31544.66  =FV(0.04,5,-5600,0,1)
print(round(pv(0.05, 10, -1_000), 2))                     # 7721.73   =PV(0.05,10,-1000)
print(round(nper(0.005, -300, 10_000), 2))                # 36.56     =NPER(0.005,-300,10000)
print(round(rate(60, -377.42, 20_000) * 12, 4))           # 0.05      =RATE(60,-377.42,20000)*12
print(round(-200 + npv(0.10, [110, 121]), 2) + 0.0)       # 0.0       =-200+NPV(0.1,110,121)
print(round(irr([-1_000, 300, 400, 500]), 4))             # 0.089     =IRR({-1000,300,400,500})
print(round(effect(0.06, 12), 5), round(nominal(effect(0.06, 12), 12), 5))   # 0.06168 0.06


# ---- The capstone plan (all inputs made up, 2026 tax rules in every year) ----
salary = [65_000, 67_000, 69_000, 71_000, 73_000]
take_home = [50_555.75, 51_842.15, 53_129.87, 54_442.66, 55_605.45]    # from tax_2026 in lesson 1

# OSAP: $16,000 federal at 0% and $12,000 Ontario at an example rate of 6%, six-month grace period
ontario_after_grace = 12_000 * (1 + 0.06 / 12) ** 6
ontario_payment = -pmt(0.06 / 12, 120, ontario_after_grace)
federal_payment = 16_000 / 120
osap_month = ontario_payment + federal_payment
print(round(ontario_after_grace, 2), round(osap_month, 2))               # 12364.53 270.6
ontario_left = -fv(0.06 / 12, 54, -ontario_payment, ontario_after_grace)
print(round(ontario_left, 2), round(16_000 - federal_payment * 54, 2))   # 7700.52 8800.0

living0, inflation = 31_500, 0.03
emergency_target = round(3 * (living0 / 12 + osap_month), -2)            # three months of costs
fhsa_year, r_fhsa, r_tfsa, refund_rate = 5_600, 0.04, 0.05, 0.2965
print(emergency_target, round(-pmt(0.04, 5, 0, 30_000), 2))              # 8700.0 5538.81


def plan(car=False):
    car_cost = -pmt(0.072 / 12, 60, 18_000) * 12 + 4_800 - 1_000 if car else 0
    emergency = fhsa = tfsa = refund = 0.0
    rows = []
    for t in range(5):
        living = round(living0 * (1 + inflation) ** t)
        osap = osap_month * (6 if t == 0 else 12)
        free = take_home[t] - living - osap - car_cost + refund
        to_emergency = max(0.0, min(free, emergency_target - emergency))
        to_fhsa = max(0.0, min(free - to_emergency, fhsa_year))
        to_tfsa = max(0.0, free - to_emergency - to_fhsa)
        emergency += to_emergency
        fhsa = fhsa * (1 + r_fhsa) + to_fhsa
        tfsa = tfsa * (1 + r_tfsa) + to_tfsa
        refund = refund_rate * to_fhsa          # arrives in next year's row
        rows.append((t + 1, round(free), round(to_emergency), round(to_fhsa), round(to_tfsa), round(fhsa), round(tfsa)))
    return rows


print("year, free cash, emergency, FHSA, TFSA, FHSA balance, TFSA balance")
for row in plan():
    print(*row)
print("with the car:")
for row in plan(car=True):
    print(*row)

# the car as cash flows: loan payments and running costs, less $9,000 resale in year 5
yearly = -(-pmt(0.072 / 12, 60, 18_000) * 12 + 4_800 - 1_000)
flows = [yearly] * 4 + [yearly + 9_000]
print(round(npv(0.04, flows), 2), round(-sum(flows), 2))                 # -28651.15 31487.35

# TFSA or RRSP: $1,000 before tax, 5% for 30 years, tax rate now 29.65%
growth = 1.05 ** 30
for later in (0.1905, 0.2965, 0.4341):
    print(later, round(1_000 * growth * (1 - later), 2), round(1_000 * (1 - 0.2965) * growth, 2))
```

The output of the first block matches the comments: `-358.12`, `30331.41`, `31544.66`, `7721.73`, `36.56`, `0.05`, `0.0`, `0.089` and `0.06168 0.06`. The plan prints the rows of the table above (year 1 is `1 17432 8700 5600 3132 5600 3132`, year 5 is `5 18565 0 5600 12965 30331 58192`), and the rows with the car (year 1 is `1 9335 8700 635 0 635 0`, year 5 is `5 10467 0 5600 4867 24523 17779`). The last lines print `-28651.15 31487.35` and then three rows ending in `3040.49`, with RRSP values `3498.61`, `3040.49` and `2445.79`.

The function `rate` searches between 0% and 100% a period by bisection, and `irr` between $-90\%$ and 100%. They find one root, so they would miss the second IRR in Practice 7. Real spreadsheets use a similar search with a starting guess.

</details>

## FAQ

### Why does `PMT` come out negative?

Because the functions follow the sign convention: you receive the loan (positive) and pay the instalments (negative). If you want a positive payment, put a minus sign in front of the function or enter the loan as negative, as in `=-PMT(...)`.

### Why does `NPV` ignore my first cash flow's date?

It assumes that every value comes at the end of a period, starting with period 1. This is a convention that matches a series of future payments, such as a bond's coupons. The \$0 initial investment today is outside, so add it yourself.

### Do the spreadsheet functions give different answers from my formulas?

No, they solve the same equation. If the answers differ by a few cents, the cause is rounding of the payment: a loan payment rounded to the cent leaves a last payment of a slightly different size, as in Example 4.

### Which should Sam choose, the TFSA or the RRSP?

The comparison above says it depends on the tax rate now against the tax rate later, and the math cannot know the later rate. This is a case where the math narrows the question to a single number to guess. It does not make the guess for you.

## Practice

### Warm-up

1\. Find the monthly payment on a \$25,000 loan at a nominal 6% a year over 48 months, and the total interest. Write the spreadsheet formula.

<details class="solution" markdown>
<summary>Solution</summary>

The formula is `=PMT(0.06/12, 48, 25000)`. The monthly rate is 0.005, so $A = 25000 \cdot \frac{0.005}{1 - 1.005^{-48}} = 587.13$. The spreadsheet shows $-587.13$. The total paid is $587.1257 \times 48 = 28{,}182.03$, so the interest is $28182.03 - 25000 = 3182.03$.

Check: the interest is about the rate times the years times half the loan, $0.06 \times 4 \times 12500 = 3000$, a bit less than 3,182 as expected.

</details>

2\. You deposit \$200 a month for 10 years at a nominal 4% a year, compounded monthly. Find the balance for deposits at the end of each month and at the start. Write the formulas.

<details class="solution" markdown>
<summary>Solution</summary>

The formulas are `=FV(0.04/12, 120, -200)` and `=FV(0.04/12, 120, -200, 0, 1)`. With $i = \frac{0.04}{12}$, the ordinary balance is $200 \cdot \frac{(1+i)^{120} - 1}{i} = 29{,}449.96$. For deposits at the start, multiply by $1 + i = 1.003333$: $29449.96 \times 1.003333 = 29{,}548.13$. The deposits themselves total $200 \times 120 = 24{,}000$.

Check: the balance is above \$24,000, and the extra month of interest on each deposit adds about \$98 in total.

</details>

3\. (a) Find the effective annual rate of 9% compounded quarterly. (b) Find the nominal rate compounded monthly that is equivalent to an effective 5%.

<details class="solution" markdown>
<summary>Solution</summary>

(a) `=EFFECT(0.09, 4)`: $(1 + 0.09/4)^4 - 1 = 1.0225^4 - 1 = 0.09308$, about 9.31%.

(b) `=NOMINAL(0.05, 12)`: $12\left(1.05^{1/12} - 1\right) = 0.048889$, about 4.89%.

Check: 9.31% is above 9%, and 4.89% is below 5%, as they should be: compounding more often than yearly makes the effective rate larger than the nominal rate. Putting 4.89% back, $\left(1 + \frac{0.048889}{12}\right)^{12} = 1.05$.

</details>

### Standard

4\. What is the present value of \$1,200 received at the end of each year for 20 years at 5%? Write the formula, and check it with the geometric series sum.

<details class="solution" markdown>
<summary>Solution</summary>

`=PV(0.05, 20, -1200)` gives \$14,954.65. With the geometric series (the sum $\sum_{k=1}^{20} 1200 \cdot 1.05^{-k}$), the value is $1200 \cdot \frac{1 - 1.05^{-20}}{0.05} = 1200 \times 12.46221 = 14954.65$.

Check: 20 payments total \$24,000, and the present value is lower, \$14,954.65, as discounting makes it.

</details>

5\. A \$15,000 loan is repaid with \$350 a month for 48 months. Find the monthly rate and the nominal annual rate with `RATE`, then the effective annual rate and the total interest.

<details class="solution" markdown>
<summary>Solution</summary>

`=RATE(48, -350, 15000)` gives about 0.0047237 a month. The nominal annual rate is $12 \times 0.0047237 = 0.05668$, about 5.67%. The effective annual rate is `=EFFECT(0.05668, 12)`, which is $5.82\%$. The total interest is $350 \times 48 - 15000 = 1800$ dollars.

Check: with the rate found, the payment is $15000 \cdot \frac{0.0047237}{1 - 1.0047237^{-48}} = 350.00$.

</details>

6\. A project costs \$4,000 now and pays \$1,500, \$2,000 and \$2,000 at the ends of years 1, 2 and 3. Find the NPV at 7% and the IRR. Write the spreadsheet formulas.

<details class="solution" markdown>
<summary>Solution</summary>

The formulas are `=-4000 + NPV(0.07, 1500, 2000, 2000)` and `=IRR({-4000,1500,2000,2000})`. The present values are $\frac{1500}{1.07} = 1401.87$, $\frac{2000}{1.07^2} = 1746.88$ and $\frac{2000}{1.07^3} = 1632.60$, which add to \$4,781.34. The NPV is $4781.34 - 4000 = 781.34$. The IRR is 16.88%.

Check: at a rate of 16.88% the three present values add to \$4,000.00 (to the cent), and the NPV at 7% is positive because 7% is below the IRR.

</details>

### Challenge

7\. Show that the cash flows $-100$, $230$, $-132$ (times 0, 1 and 2) have two IRRs, and find both.

<details class="solution" markdown>
<summary>Solution</summary>

Let $x = \frac{1}{1+i}$. The NPV is $-100 + 230x - 132x^2 = 0$, so $132x^2 - 230x + 100 = 0$. The quadratic formula gives $x = \frac{230 \pm \sqrt{230^2 - 4 \cdot 132 \cdot 100}}{264} = \frac{230 \pm \sqrt{100}}{264} = \frac{230 \pm 10}{264}$. So $x = \frac{240}{264} = 0.9091$ or $x = \frac{220}{264} = 0.8333$. Then $i = \frac{1}{x} - 1$ is 10% and 20%.

Check: at 10%, $-100 + \frac{230}{1.1} - \frac{132}{1.21} = -100 + 209.09 - 109.09 = 0$. At 20%, $-100 + \frac{230}{1.2} - \frac{132}{1.44} = -100 + 191.67 - 91.67 = 0$. The signs change twice (minus, plus, minus), which is what allows two IRRs.

</details>

8\. (Reviews [present and future value](../03-time-value-of-money/01-present-and-future-value.md).) Sam has \$8,000 in a savings account that pays a nominal 5% compounded monthly, and leaves it for 6 years. Find the balance with the formula and with a spreadsheet function. What present value does \$10,792.14 in 6 years have at this rate?

<details class="solution" markdown>
<summary>Solution</summary>

With $i = \frac{0.05}{12}$ and $n = 72$, $FV = 8000\,(1 + i)^{72} = 8000 \times 1.34885 = 10{,}792.14$. The spreadsheet formula is `=FV(0.05/12, 72, 0, -8000)`, which gives the same \$10,792.14 (the deposit is negative, so the balance is positive). Going back, `=PV(0.05/12, 72, 0, 10792.14)` gives $-8000.00$: the present value is \$8,000.

Check: the interest earned is \$2,792.14, which is about 35% of the deposit; six years at 5% simple interest would be 30%, and compounding adds more.

</details>

## Where this shows up

- This is the last lesson of the chapter and of the book. The [financial math cheat sheet](../index.md) collects the formulas of the whole folder, and the other chapters give the rules behind each step of the capstone.
- Economics: NPV and IRR are how firms and governments compare projects ([present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md)).
- Computing: `rate` and `irr` are root-finding by bisection, the same algorithm used to search a sorted array.
