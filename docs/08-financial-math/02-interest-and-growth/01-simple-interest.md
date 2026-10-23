# Simple interest

After this lesson you can find the interest on a loan or deposit that earns simple interest, solve $I = Prt$ for any one of its four quantities, handle times given in months or days, and recognize simple interest as a linear function.

Before this: [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md) and [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. How much simple interest does \$2,500 earn at 4% a year in 3 years, and what is the total at the end?
2. A deposit of \$800 earns \$60 of simple interest in 6 months. What is the annual rate?
3. A \$5,000 loan charges 6% a year simple interest and is repaid after 90 days. Using a 365-day year, how much interest is owed?

<details class="solution" markdown>
<summary>Answers</summary>

1. The interest is $2500 \times 0.04 \times 3 = 300$, that is, \$300. The total is $2500 + 300 = 2800$, so \$2,800.
2. Six months is 0.5 years, so $r = \dfrac{60}{800 \times 0.5} = 0.15$, which is 15% a year.
3. The time is $\frac{90}{365}$ of a year, so the interest is $5000 \times 0.06 \times \frac{90}{365} = 73.97\ldots$, that is, \$73.97.

</details>

## The idea

Suppose you lend a friend \$1,000 for a year and agree that they pay you 5% for the use of the money. At the end of the year they give back the \$1,000 and \$50 extra. If you lend the same \$1,000 for 3 years on the same terms, the extra amount is \$150: 5% of \$1,000 each year, three times. The \$50 you earned in the first year does not earn anything in the second. The interest is always figured on the amount you originally lent.

That is simple interest, and it is the simplest way to charge for borrowing money: a fixed percent of the original amount, for each year the money is out. A lender charges it because having money now is worth something. A saver earns it because the bank is borrowing their money. In both cases the arithmetic is the percent-of-a-whole calculation from [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md), repeated once for every year.

The next lesson looks at what changes when interest is added to the balance and starts earning interest of its own. This lesson stays with the case where it doesn't, because the formulas are short and everything else builds on them.

## Definitions

The **principal** $P$ is the amount of money that is borrowed or deposited at the start, in dollars.

The **annual interest rate** $r$ is the interest earned in one year, as a fraction of the principal. It is written as a decimal in formulas, so a rate of 5% a year is $r = 0.05$. The phrase "per annum" (p.a.) means "per year".

The **time** $t$ is the length of the loan or deposit, measured in years. Six months is $t = 0.5$ and 90 days is $t = \frac{90}{365}$ years.

**Simple interest** is interest calculated only on the principal, so each year earns the same amount. The interest $I$ over $t$ years is

$$
I = P r t.
$$

In plain words, the interest is the principal, times the rate per year, times the number of years. For \$1,000 at 5% for 3 years, $I = 1000 \times 0.05 \times 3 = 150$.

The **amount** $A$ (also called the maturity value, or the future value) is the principal plus the interest:

$$
A = P + I = P(1 + rt).
$$

In plain words, you get back what you put in plus the interest. Factoring out $P$, as we did for the HST multiplier in the percents lesson, gives the second form: the amount is the principal times $1 + rt$. The next chapter calls $P$ the present value and $A$ the future value (see [present and future value](../03-time-value-of-money/01-present-and-future-value.md)).

## How to do it

### Finding the interest and the amount

1. Write down what you know: the principal $P$, the annual rate $r$ and the time $t$.
2. Change the rate to a decimal by dividing by 100: 4.5% becomes $0.045$.
3. Change the time to years. For months, divide by 12. For days, divide by the number of days in the year (see the next section).
4. Multiply: $I = Prt$. Round to the cent at the end, not before.
5. If you want the total, add: $A = P + I$.
6. Check the size. Interest for one full year is $r$ times $P$, so for $t$ years it should be about $t$ times that.

### Solving for the other variables

The formula $I = Prt$ has four letters, and you can solve for any one of them when you know the other three. Each time you divide both sides by the product of the two letters you know:

| Unknown | Formula | Example |
|---|---|---|
| interest $I$ | $I = Prt$ | \$600 at 3% for 2 years: $600 \times 0.03 \times 2 = 36$ |
| principal $P$ | $P = \dfrac{I}{rt}$ | \$36 interest at 3% in 2 years: $\dfrac{36}{0.03 \times 2} = 600$ |
| rate $r$ | $r = \dfrac{I}{Pt}$ | \$36 interest on \$600 in 2 years: $\dfrac{36}{600 \times 2} = 0.03$ |
| time $t$ | $t = \dfrac{I}{Pr}$ | \$36 interest on \$600 at 3%: $\dfrac{36}{600 \times 0.03} = 2$ years |

If you know the amount instead of the interest, first find $I = A - P$, then use the table. The rate you find is an annual rate, so it comes out as 0.03 (that is, 3%) even when the loan lasted only a few months. Divide by the time in years, not by the number of months.

### Counting the time in days

Short loans are measured in days. The usual rule is to count the actual number of days between the two dates (the day money goes out counts, the day it comes back does not) and to divide by the number of days in a year. A common convention at Canadian banks is "actual/365": actual days over 365. It is a convention, and it is not the same for every product or institution. Some lenders divide by 360, or by 366 in a leap year, and others count every month as 30 days. The loan agreement says which one applies, so read it before you trust a calculator.

The differences are small. Here they are for \$10,000 at 5.5% from March 3 to June 21 in a non-leap year, which is 110 actual days:

| Convention | Time in years | Interest |
|---|---|---|
| actual/365 | $\frac{110}{365}$ | \$165.75 |
| actual/360 | $\frac{110}{360}$ | \$168.06 |
| actual/366 | $\frac{110}{366}$ | \$165.30 |

This book uses actual/365 unless it says otherwise.

### Simple interest as a linear function

Fix $P$ and $r$ and let $t$ vary. The amount is $A(t) = P + Prt$, which has the form $y = b + mx$ from [slope and linear equations](../../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md). The graph is a straight line. Its intercept is the principal $P$, because at time 0 you have what you started with, and its slope is $Pr$, the dollars of interest earned each year.

For \$1,000 at 5%, the slope is \$50 a year:

| Years $t$ | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Amount $A$ | \$1,000 | \$1,050 | \$1,100 | \$1,150 | \$1,200 | \$1,250 |

Equal steps of time add equal dollars. That is the signature of linear growth, and it is what separates simple interest from the compound interest in the next lesson, where equal steps of time multiply the balance by equal factors. Doubling the principal, the rate or the time doubles the interest, because $I$ is proportional to each of the three.

## Worked examples

<div class="example" markdown>

### Example 1: a short deposit

A \$3,000 deposit earns 3.6% a year simple interest for 8 months. How much interest does it earn, and what is the total at the end?

Step 1: $P = 3000$, $r = 3.6\%$ and the time is 8 months.

Step 2: as a decimal, $r = 0.036$.

Step 3: 8 months is $\frac{8}{12} = \frac{2}{3}$ of a year. Keep it as a fraction, because $0.6667$ would introduce a rounding error.

Step 4: multiply:

$$
I = 3000 \times 0.036 \times \frac{8}{12} = 72.
$$

The interest is \$72.00.

Step 5: the total is $A = 3000 + 72 = 3072$, that is, \$3,072.

Step 6: check the size. A full year would earn $3000 \times 0.036 = 108$, and 8 months is two thirds of a year, and two thirds of 108 is 72. That matches.

</div>

<div class="example" markdown>

### Example 2: finding the rate

You borrow \$1,200 from a relative and repay \$1,254 after 9 months. What annual simple rate did you pay?

You know the amount, so first find the interest: $I = 1254 - 1200 = 54$. The time is $\frac{9}{12} = 0.75$ years. Solve $I = Prt$ for $r$:

$$
r = \frac{I}{Pt} = \frac{54}{1200 \times 0.75} = \frac{54}{900} = 0.06.
$$

The rate is 6% a year. Check: $1200 \times 0.06 \times 0.75 = 54$.

<div class="warning" markdown>

Watch out: the loan lasted 9 months, but $\frac{54}{1200} = 4.5\%$ is the interest over those 9 months, not a yearly rate. The rate has to be a rate per year, so divide by the time in years.

</div>

</div>

<div class="example" markdown>

### Example 3: counting days

A business lends \$10,000 on March 3 at 5.5% a year simple interest, and is repaid on June 21 of the same (non-leap) year. How much interest is owed on an actual/365 basis? What is the interest per day?

Count the days. March 3 to March 31 is 28 days, April has 30, May has 31, and March 31 to June 21 adds 21 more days in June, so the total is $28 + 30 + 31 + 21 = 110$ days. A date function gives the same count (see In code).

The interest is

$$
I = 10000 \times 0.055 \times \frac{110}{365} = 165.7534\ldots
$$

so it is \$165.75. The interest per day is $\frac{10000 \times 0.055}{365} = 1.5068\ldots$, about \$1.51, and 110 days of it is $110 \times 1.5068 = 165.75$.

Check: 110 days is a bit less than a third of a year, and a third of the yearly interest of \$550 is \$183.33. A bit less than that, \$165.75, fits.

</div>

<div class="example" markdown>

### Example 4: a very short loan as a yearly rate (finish it yourself)

Payday lenders charge a fee per \$100 borrowed instead of quoting a yearly rate. The Financial Consumer Agency of Canada (FCAC) reports a limit of \$14 for every \$100 borrowed in provinces that regulate payday lending, Ontario included ([FCAC, payday loans](https://www.canada.ca/en/financial-consumer-agency/services/loans/payday-loans.html), page dated 2025-10-14). Suppose you borrow \$300 for 14 days at that fee. What annual simple rate does the fee amount to?

Step 1: the fee is the interest. For \$300 it is 3 hundreds, so $I = 3 \times 14 = 42$ dollars.

Step 2: the time is $t = \frac{14}{365}$ years.

Step 3: solve for the rate, $r = \dfrac{I}{Pt}$. Do the division and write the answer as a percent.

<details class="solution" markdown>
<summary>Finish</summary>

Step 3: $r = \dfrac{42}{300 \times 14/365} = \dfrac{42 \times 365}{4200} = 3.65$, which is 365% a year.

Check: \$14 on \$100 is 14% for 14 days. A year has $\frac{365}{14}$ such periods, and $14\% \times \frac{365}{14} = 365\%$. Then $300 \times 3.65 \times \frac{14}{365} = 42$.

</details>

</div>

<div class="note" markdown>

The payday limit is a changing figure. It is the FCAC's wording as fetched in October 2026. Rules for loans, fees and limits change, so check the linked page before using the number for a real decision. The 365% is a way to compare a 14-day fee with yearly rates, not a statement about what you would pay if you borrowed for a year.

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: using months as years. A 9-month loan has $t = 0.75$, not 9. If you put in 9, the interest comes out twelve times too big. A size check catches it: the interest on any loan shorter than a year must be less than $P \times r$.

</div>

<div class="warning" markdown>

Watch out: using the rate as a whole number. At 4% the formula needs $r = 0.04$. Writing $r = 4$ makes the interest 100 times too big. This is the same decimal-point slip as writing 7% as 0.7 in the percents lesson.

</div>

<div class="warning" markdown>

Watch out: rates that are not per year. A card that says "1.5% per month" has a monthly rate of $r_{\text{month}} = 0.015$. Plugging it into $I = Prt$ works only if $t$ is also in months. Using $t$ in years with a monthly rate gives a number that is 12 times too small. The simple annual rate is $12 \times 1.5\% = 18\%$.

</div>

<div class="warning" markdown>

Watch out: rounding the time. A 90-day loan is $\frac{90}{365} = 0.246575\ldots$ of a year. Rounding it to 0.25 changes \$73.97 on a \$5,000 loan at 6% to \$75.00. Keep the fraction, multiply everything and round once at the end.

</div>

Two cases are worth a sentence each. When $t = 0$ no time has passed, so $I = 0$ and $A = P$. And if the rate is 0%, the interest is zero for every $t$ and the line is flat.

There is also a rule in Canadian law about how a rate is written. Section 4 of the federal [Interest Act](https://laws-lois.justice.gc.ca/eng/acts/i-15/FullText.html) says that when a written contract states interest at a rate per day, week, month or any period shorter than a year (mortgages on real property are handled separately), the lender cannot charge more than 5% a year on the principal unless the contract also states the equivalent yearly rate. So a lender who writes "0.1% per day" has to say that this is 36.5% a year. The law keeps a rate quoted per day or per month from hiding how large it is once it is stated per year.

## Tricks and shortcuts

Think of daily interest as $\frac{Pr}{365}$ dollars a day, and monthly interest as $\frac{Pr}{12}$. Then any time in days or months is a count of those small steps. For \$5,000 at 6%:

| Period | Interest |
|---|---|
| one year | \$300.00 |
| one month | \$25.00 |
| one day | \$0.82 |
| 90 days | \$73.97 |

A quarter of a year is about 91 days, so 90 days is a little less than a quarter of the yearly interest: a quarter of \$300 is \$75, and \$73.97 is just under that.

To go from a monthly rate to a simple annual rate, multiply by 12. To go from a fee on a short loan to a yearly rate, multiply the percent fee by the number of such loans that fit into a year: 14% for 14 days is $14\% \times \frac{365}{14} = 365\%$.

## In code

The function takes the time in days, so the actual/365 rule is one division. A date subtraction counts the days between two dates.

<details class="code" markdown>
<summary>In code</summary>

```python
from datetime import date

def simple_interest(principal, rate, days=None, years=None, basis=365):
    """Interest on a simple-interest loan. Give days or years."""
    if years is None:
        years = days / basis
    return principal * rate * years

print(round(simple_interest(5000, 0.06, days=90), 2))      # 73.97
print(round(simple_interest(3000, 0.036, years=8 / 12), 2))  # 72.0

days = (date(2027, 6, 21) - date(2027, 3, 3)).days
print(days)                                                # 110
for basis in (365, 360, 366):
    print(basis, round(simple_interest(10000, 0.055, days=days, basis=basis), 2))
    # 365 165.75, then 360 168.06, then 366 165.3

# the rate from a short loan's fee: 42 dollars on 300 dollars for 14 days
print(42 / (300 * 14 / 365))                               # 3.65, that is 365% a year
```

</details>

## FAQ

### Why divide the days by 365 and not by something else?

There are 365 days in most years, so dividing by 365 makes a year of days equal to one year. Some lenders use 360 (a banker's year of twelve 30-day months) because it makes the arithmetic round, and some use 366 in leap years. None is wrong, but they give slightly different interest, as the table showed. What matters is that the agreement states the rule, and that you use the same one when you compare offers.

### What if the rate changes during the loan?

Split the loan into pieces with a constant rate, find the interest for each piece with $I = Prt$ and add them. Because simple interest never touches the interest already earned, the pieces don't affect each other. A \$5,000 loan at 3% for 8 months and then 5% for 4 months owes $5000 \times (0.03 \times \frac{8}{12} + 0.05 \times \frac{4}{12}) = 183.33$ dollars.

### If simple interest is so easy, why does anyone use compound interest?

Because most accounts and loans do add interest to the balance. When you leave interest in the account, the bank has your interest as well as your principal, so it pays interest on both. Simple interest still appears in short loans, in some term deposits that pay interest once at maturity, and as the first step of every compound calculation. Over a single year with annual compounding the two give the same interest, which is why the formulas in this lesson reappear inside the next one.

## Practice

### Warm-up

1\. Find the interest and the total amount for \$1,800 at 3.5% a year simple interest for 4 years.

<details class="solution" markdown>
<summary>Solution</summary>

$I = 1800 \times 0.035 \times 4 = 252$, so the interest is \$252. The total is $1800 + 252 = 2052$, that is, \$2,052.

Check: one year earns $1800 \times 0.035 = 63$, and four years earn $4 \times 63 = 252$.

</details>

2\. A loan at 2.5% simple interest for 3 years costs \$90 in interest. What was the principal?

<details class="solution" markdown>
<summary>Solution</summary>

Solve for $P$: $P = \dfrac{I}{rt} = \dfrac{90}{0.025 \times 3} = \dfrac{90}{0.075} = 1200$. The principal was \$1,200.

Check: $1200 \times 0.025 \times 3 = 90$.

</details>

3\. How long does it take \$2,000 at 4.5% simple interest to earn \$135?

<details class="solution" markdown>
<summary>Solution</summary>

$t = \dfrac{I}{Pr} = \dfrac{135}{2000 \times 0.045} = \dfrac{135}{90} = 1.5$ years, which is 18 months.

Check: one year earns \$90, and half a year earns \$45, so $90 + 45 = 135$.

</details>

### Standard

4\. A deposit of \$2,400 earns \$36 in 73 days. Using a 365-day year, what annual simple rate is that?

<details class="solution" markdown>
<summary>Solution</summary>

The time is $\frac{73}{365} = 0.2$ years. Then $r = \dfrac{36}{2400 \times 0.2} = \dfrac{36}{480} = 0.075$, which is 7.5% a year.

Check: $2400 \times 0.075 \times 0.2 = 36$. The size makes sense too: 73 days is a fifth of a year, and a fifth of the yearly interest \$180 is \$36.

</details>

5\. A \$5,000 loan is repaid after 2 years. The rate is 3% for the first year and 4% for the second. (a) How much interest is paid? (b) What single rate for the whole 2 years gives the same interest? (c) Another \$5,000 loan charges 3% for the first 8 months and 5% for the next 4. What is its interest?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Add the interest of each year: $5000 \times 0.03 + 5000 \times 0.04 = 150 + 200 = 350$, so \$350.

(b) The equal rate is $r = \dfrac{350}{5000 \times 2} = 0.035$, which is 3.5%. It is the average of 3% and 4% because the two pieces last the same time.

(c) The pieces last $\frac{8}{12}$ and $\frac{4}{12}$ of a year: $5000 \times (0.03 \times \frac{8}{12} + 0.05 \times \frac{4}{12}) = 100 + 83.33 = 183.33$, that is, \$183.33. The average rate is not 4% here, because the lower rate lasts longer: $\frac{183.33}{5000} = 3.67\%$ over one year.

Check: (b) $5000 \times 0.035 \times 2 = 350$. (c) $183.33 / 5000 = 0.036667$, which is between 3% and 5% and closer to 3%.

</details>

6\. The balance of a savings deposit is $A(t) = 1500 + 90t$ dollars after $t$ years. (a) Identify the principal and the simple annual rate. (b) When does the balance reach \$2,000?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The function has the form $A(t) = P + Prt$. The intercept is the principal, $P = 1500$, and the slope is $Pr = 90$, so $r = \frac{90}{1500} = 0.06$, which is 6%.

(b) Set $1500 + 90t = 2000$. Then $90t = 500$ and $t = \frac{500}{90} = 5.555\ldots$ years, about 5 years and 6.7 months ($0.5556 \times 12 = 6.67$).

Check: $1500 + 90 \times 5.5556 = 2000$.

</details>

### Challenge

7\. A friend asks for \$1,000 for 30 days and offers to repay \$1,025. (a) What annual simple rate is that? (b) A bank offers a loan at 12% a year simple interest. For \$1,000 over 30 days, how much do you save by choosing the bank?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The interest is \$25 and the time is $\frac{30}{365}$ years: $r = \dfrac{25}{1000 \times 30/365} = \dfrac{25 \times 365}{30000} = 0.30417$, about 30.4% a year. Two and a half percent for one month sounds small, and as a yearly rate it is not.

(b) At 12% the interest is $1000 \times 0.12 \times \frac{30}{365} = 9.86$ dollars (\$9.863 before rounding). The saving is $25 - 9.86 = 15.14$ dollars.

Check: $1000 \times 0.30417 \times \frac{30}{365} = 25.00$.

</details>

8\. (Reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).) A \$2,000 balance is charged 1.5% per month in simple interest. (a) How much interest is charged in one month? (b) What simple annual rate is that? (c) After 8 months, what percent of the original balance is the interest?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The whole is the balance: $0.015 \times 2000 = 30$, so \$30 a month.

(b) A year has 12 months, so the annual rate is $12 \times 1.5\% = 18\%$.

(c) Eight months of interest is $8 \times 30 = 240$ dollars, and $\frac{240}{2000} = 0.12$, so 12% of the original balance. That is the same as the annual rate for $\frac{8}{12}$ of a year: $18\% \times \frac{8}{12} = 12\%$.

Check: $2000 \times 0.18 \times \frac{8}{12} = 240$.

</details>

## Where this shows up

- The next lesson, [compound interest](02-compound-interest.md), changes one thing: the interest is added to the balance, so it earns interest too. Later you will see the same short-loan arithmetic in [effective annual rates](03-apr-apy-and-effective-annual-rate.md) and in [student loans](../04-borrowing/01-student-loans.md).
- Linear functions again: a line with intercept $P$ and slope $Pr$ is the model for any steady, non-compounding charge. Economics uses the same shape for a fixed cost plus a steady charge per unit.
- Everyday money: short-term deposits that pay interest once at the end, payday loans and the interest on a late bill are all computed with $I = Prt$ over a number of days.
