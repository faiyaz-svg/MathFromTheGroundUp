# Credit cards and the minimum payment trap

After this lesson you can compute credit card interest from the daily balance, simulate how long a balance lasts under minimum payments and what it costs, and explain why a payment that is a percent of the balance almost never finishes the job.

Before this: [the loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md), [APR, APY and the effective annual rate](../02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md) and [exponential and logarithmic equations](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A card charges 20% a year. What is the daily rate, and how much interest does a \$1,000 balance earn for the card company over 30 days?
2. The minimum payment is the higher of \$10 or 3% of the balance. What is it on balances of \$1,500 and \$250?
3. A \$2,000 balance at 18% a year has a fixed \$60 monthly payment. What is the first month's interest, and does the balance fall?

<details class="solution" markdown>
<summary>Answers</summary>

1. The daily rate is $0.20 \div 365 = 0.000548$, that is, 0.0548% a day. Over 30 days the interest on \$1,000 is $1000 \times 0.000548 \times 30 = 16.44$, so \$16.44.
2. On \$1,500, 3% is \$45, which is more than \$10, so the minimum is \$45. On \$250, 3% is \$7.50, so the \$10 applies.
3. The monthly rate is $0.18 \div 12 = 0.015$, so the interest is $2000 \times 0.015 = 30$ dollars. The payment is \$60, so \$30 goes to principal and the balance falls to \$1,970.

</details>

## The idea

A credit card is a loan with no fixed end date. Each month you get a statement with a balance and a minimum payment. If you pay the whole balance by the due date, the card costs you no interest on purchases. If you pay anything less, the rest is a loan, and the rate on it is high compared with a car loan or a student loan.

The Financial Consumer Agency of Canada (FCAC) has a worked example: a \$2,000 balance at 18% with only the minimum payment of \$60 a month takes 3 years and 11 months to pay off and costs \$793 in interest; paying \$160 a month takes 1 year and 2 months and costs \$231 ([FCAC](https://www.canada.ca/en/financial-consumer-agency/services/credit-cards/pay-off-credit-card.html)). This lesson rebuilds those numbers from the interest rule and then asks what changes when the minimum falls as the balance does. The answer is the "trap": the payment shrinks, the payoff time stretches, and the interest can exceed the original balance.

All rates here are made-up examples unless a page is cited. They are not current market rates.

## Definitions

The **annual rate** is the yearly interest rate stated on the card, for example 20%. The **daily rate** is the annual rate divided by 365:

$$
\text{daily rate} = \frac{\text{annual rate}}{365}.
$$

In plain words: a card with a 20% annual rate charges 0.0548% each day on the balance owed that day.

The **daily balance** is what you owe at the end of a given day. The **average daily balance** over a billing cycle of $d$ days is the sum of the daily balances divided by $d$. The FCAC's sample credit card disclosure says interest is "calculated on your daily average balance and charged monthly to your account" ([FCAC sample](https://www.canada.ca/en/financial-consumer-agency/services/industry/bulletins/information-box-examples/credit-agreement-credit-card.html)).

The **grace period** is the interest-free time on new purchases if you pay your full balance by the due date. The same sample says "an interest-free grace period of at least 21 days", and that there is "no interest-free period on cash advances and balance transfers".

The **minimum payment** is the smallest amount you must pay each month. The FCAC describes two methods: a flat amount (usually \$10) plus interest and fees, or "the higher of a dollar amount, typically \$10, or a percentage of your outstanding balance, typically 3%". Your credit agreement says which one applies. (Quebec has a different rule, a 5% minimum since August 1, 2025, according to the same page.)

A **cash advance** is cash you take from your card, for example at a bank machine. The sample disclosure lists a separate rate (20% in the sample), a fee (\$5.00 in the sample), and no grace period.

## How to do it

### Interest from the daily balance

1. Find the daily rate: annual rate divided by 365.
2. List the balance on each day of the cycle.
3. Interest for the cycle is the daily rate times the sum of the daily balances. (Equivalently, the daily rate times the average daily balance times the number of days.)
4. A payment or a new purchase changes the balance from the day it posts, so split the cycle at those days.
5. If you pay the full statement balance by the due date, new purchases carry no interest during the grace period. Check the agreement for the details.

### Simulating a payoff

The monthly update is the loan update from the amortization chapter: with monthly rate $r$ (the annual rate divided by 12) and payment $P$,

$$
B_{k+1} = B_k (1 + r) - P.
$$

1. Start with balance $B_0$.
2. Each month, add interest $rB_k$, subtract the payment, and count the month.
3. Stop when the balance reaches zero. The last payment is smaller.
4. Total interest is the sum of the monthly interest amounts.

For a fixed payment $P > rB_0$, the number of payments solves the equation, as in the [student loans](01-student-loans.md) lesson:

$$
n = -\frac{\ln\!\left(1 - \frac{B_0 r}{P}\right)}{\ln(1 + r)}.
$$

### When the payment is a percent of the balance

Suppose the payment is $pB_k$, a percent $p$ of the current balance (ignoring the \$10 floor for now). Then

$$
B_{k+1} = B_k (1 + r - p),
$$

so $B_k = B_0 (1 + r - p)^k$. This is geometric decay with ratio $1 + r - p$. With $r = 0.015$ and $p = 0.03$ the ratio is 0.985. A geometric sequence with a positive ratio below 1 gets smaller and smaller but never reaches zero. Only the dollar floor, the \$10 minimum, ends it.

<div class="note" markdown>

These card figures (21-day grace period, 3% and \$10 minimums, the sample rates) come from FCAC pages dated 2025 and are examples of terms, not rules for every card. Your credit agreement controls. The rates in this lesson are made up.

</div>

## Worked examples

<div class="example" markdown>

### Example 1: interest for one billing cycle

Suppose a card charges 20% a year, and a 30-day cycle starts with a balance of \$1,000. On day 11 you buy \$400 of groceries and don't pay anything during the cycle. (The 20% is a made-up rate.)

Step 1: the daily rate is $0.20 \div 365 = 0.000547945$.

Step 2: the balance is \$1,000 for 10 days (days 1 to 10) and \$1,400 for 20 days (days 11 to 30).

Step 3: the interest is

$$
0.000547945 \times (1000 \times 10 + 1400 \times 20) = 0.000547945 \times 38000 = 20.82.
$$

The average daily balance is $38000 \div 30 = 1266.67$. And $1266.67 \times 0.000547945 \times 30 = 20.82$, the same number.

Step 4 and 5: the purchase counted from day 11 because the old balance wasn't paid in full. If the \$1,000 had been paid in full by the due date, the grace period would have covered the new purchase.

Check: the card's monthly rate is about $0.20 \div 12 = 0.01667$, and 1.667% of \$1,266.67 is \$21.11, close to \$20.82. (A 30-day cycle is a little under a twelfth of a year.)

</div>

<div class="example" markdown>

### Example 2: reproducing the FCAC example

The FCAC page: \$2,000 at 18%, a minimum payment of \$60, taking 3 years and 11 months with \$793 of interest. The page doesn't say how the \$60 is found, but it is 3% of \$2,000, and it is held fixed in the example.

Step 1: $r = 0.18 \div 12 = 0.015$. The first month's interest is \$30.00, so the balance goes to $2000 + 30 - 60 = 1970$.

Step 2: the second month's interest is $1970 \times 0.015 = 29.55$, and the balance is \$1,939.55. Continuing, the payoff time is

$$
n = -\frac{\ln(1 - 2000 \times 0.015 / 60)}{\ln 1.015} = -\frac{\ln 0.5}{\ln 1.015} = 46.56,
$$

so 47 payments, the last one small (\$33.44). That is 3 years and 11 months. The total interest is \$793.44, which rounds to the FCAC's \$793.

Step 3: at \$160 a month, the interest is \$4.57 in month 13 and the loan ends in month 14 with a payment of \$151.45. The total interest is \$231.45, which matches the FCAC's \$231 and its 1 year 2 months.

So the monthly-rate method reproduces both FCAC figures to the dollar.

Check: with \$60 paid 46 times and \$33.44 once, the total paid is $60 \times 46 + 33.44 = 2793.44$, and $2793.44 - 2000 = 793.44$.

</div>

<div class="example" markdown>

### Example 3: the real trap, a payment that shrinks

Now use the percent rule. Same \$2,000 at 18%, but each month you pay the higher of \$10 or 3% of that month's balance.

The first payments are \$60.00, \$59.10, \$58.21 and \$57.34, because the balance is falling. The balance after $k$ months is $2000 \times 0.985^k$ while 3% of it is above \$10. The 3% equals \$10 when the balance is \$333.33, which happens after

$$
k = \frac{\ln(333.33 \div 2000)}{\ln 0.985} = 118.6
$$

months. After that the payment is stuck at \$10 and the last of the balance takes another 46 months or so. The simulation gives 166 months, about 13 years and 10 months, with \$1,798.88 of interest. That is nearly as much as the original \$2,000.

| Payment rule | Months | Total interest |
|---|---|---|
| fixed \$160 | 14 | \$231.45 |
| fixed \$60 | 47 | \$793.44 |
| higher of \$10 or 3% of the balance | 166 | \$1,798.88 |

The percent rule starts at the same \$60 as the fixed rule, and it costs more than twice as much interest and takes over three times as long. The payment is a shrinking target, not a fixed schedule.

Check: the formula gives a balance of $2000 \times 0.985^{119} = 331.09$ after 119 months, below \$333.33, so the payment is \$10 from month 120 on, as described. The balance falls by only $0.03 - 0.015 = 1.5\%$ of itself each month, so a long payoff is what we should expect.

</div>

<div class="example" markdown>

### Example 4: a bigger balance (finish it yourself)

A \$3,000 balance at 20% (made up). Compare the percent rule (higher of \$10 or 3%) with a fixed \$150 payment.

Step 1: $r = 0.20 \div 12 = 0.016667$, and the first month's interest is \$50.

Step 2: the percent rule pays \$90 first. Its balance shrinks by the factor $1 + r - p = 0.98667$ a month until the payment hits \$10.

Step 3: for the fixed \$150, use $n = -\ln(1 - B_0 r / P) \div \ln(1 + r)$.

Find the months and total interest for both, then say what you notice.

<details class="solution" markdown>
<summary>Finish</summary>

Step 3: $B_0 r / P = 50 / 150 = 0.3333$, so $n = -\ln(0.6667) \div \ln(1.016667) = 24.5$, that is, 25 payments, and the simulated interest is \$679.82.

The percent rule takes 213 months, about 17 years and 9 months, and costs \$3,490.60 in interest, more than the original \$3,000 balance. A fixed \$90 (the first percent payment, held constant) takes 50 months and \$1,415.46.

Check: the total paid is the balance plus the interest, $3000 + 679.82 = 3679.82$. Twenty-four payments of \$150 make \$3,600, so the 25th payment is \$79.82, a small last one.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: assuming interest only starts after the due date. For a balance you carry from the last statement, interest runs on the daily balance. The grace period applies only if you paid the previous statement in full.

</div>

<div class="warning" markdown>

Watch out: assuming the cash advance has a grace period. The FCAC sample says there is none. A \$800 cash advance repaid after 15 days at 20% costs $800 \times 0.20 \div 365 \times 15 = 6.58$ in interest, plus a \$5 fee, which is \$11.58 for 15 days. As an annualized rate, that is $\frac{11.58}{800} \times \frac{365}{15} = 35.2\%$, though this is a rough comparison, not the legal APR calculation.

</div>

<div class="warning" markdown>

Watch out: using the minimum payment as a plan. It is the amount that keeps the account in good standing. Example 3 shows that following it can take 14 years.

</div>

<div class="warning" markdown>

Watch out: dividing the annual rate by 12 when the card charges daily. Dividing by 365 and counting days gives slightly different cycle interest in a 28-day or 31-day month. Example 2's monthly-rate model matched the FCAC to the dollar, but a statement may differ by a few cents.

</div>

The cap on interest rates is higher than most card rates. The Criminal Code defines the "criminal rate" as an annual percentage rate that exceeds 35 per cent on the credit advanced ([Criminal Code s. 347](https://laws-lois.justice.gc.ca/eng/acts/c-46/section-347.html)), a limit that took effect on January 1, 2025, according to a [Canada Gazette order](https://gazette.gc.ca/rp-pr/p2/2024/2024-06-19/html/si-tr25-eng.html). It does not make card rates near 20% a problem, but it caps lenders. Payday loans have their own exemption: \$14 per \$100 borrowed in provinces that regulate them, including Ontario ([FCAC](https://www.canada.ca/en/financial-consumer-agency/services/loans/payday-loans.html)).

## Tricks and shortcuts

A quick estimate of daily interest: 20% a year is about 0.055% a day, which is \$0.55 per day per \$1,000. A month is about \$16.50 per \$1,000 at 20%.

To see whether a payment makes progress, compare it with one month's interest, $rB$. If the payment is only a little above that, the payoff will take decades.

Pay more than the minimum. The FCAC says "increasing your monthly payment will shorten the time" to pay off the balance, and the closed form shows how: going from \$60 to \$160 in Example 2 cut 33 months and \$562 of interest.

## In code

The function simulates a payoff for a fixed payment or for the percent rule, and reproduces the FCAC numbers.

<details class="code" markdown>
<summary>In code</summary>

```python
def payoff(balance, apr, fixed=None, pct=0.03, floor=10.0):
    r = apr / 12
    months, interest = 0, 0.0
    while balance > 0.005:
        i = balance * r
        pay = fixed if fixed is not None else max(floor, pct * balance)
        pay = min(pay, balance + i)
        balance = balance + i - pay
        interest += i
        months += 1
    return months, round(interest, 2)

print(payoff(2000, 0.18, fixed=60))    # (47, 793.44)
print(payoff(2000, 0.18, fixed=160))   # (14, 231.45)
print(payoff(2000, 0.18))              # (166, 1798.88)
print(payoff(3000, 0.20))              # (213, 3490.6)
print(payoff(3000, 0.20, fixed=150))   # (25, 679.82)
```

</details>

## FAQ

### Why does the percent rule take so long?

The payment is a fixed percent of a shrinking balance, so the principal repaid each month shrinks too. The balance follows $B_0(1 + r - p)^k$, which gets small but doesn't hit zero. The dollar floor finishes it, slowly.

### Is the minimum payment the same on every card?

No. The FCAC describes two methods and says your agreement shows which one your card uses. For federally regulated issuers, statements must show the time needed to pay off the balance at the minimum payment.

### Does the interest rate get compounded daily?

The FCAC sample says interest is charged monthly on the daily average balance, so it is added to the balance once a month. That is why a monthly rate of $\text{annual} \div 12$ matches the FCAC's example. Your card's statement describes its own method.

### What is the 35% limit?

It is a legal ceiling on the annual percentage rate for most loans, set in the Criminal Code. Typical card rates are well below it, so it doesn't change card math, but it matters for high-cost loans.

## Practice

### Warm-up

1\. A card has a 24% annual rate. Find the daily rate and the interest on a \$2,400 balance over 30 days.

<details class="solution" markdown>
<summary>Solution</summary>

The daily rate is $0.24 \div 365 = 0.0006575$. The interest is $2400 \times 0.0006575 \times 30 = 47.34$, so \$47.34.

Check: monthly rate 2% of \$2,400 is \$48, a little more than \$47.34 because 30 days is under a twelfth of a year.

</details>

2\. A 30-day cycle: the balance is \$800 for 12 days, then you pay \$500 and it is \$300 for 18 days. Find the average daily balance and the interest at 24%.

<details class="solution" markdown>
<summary>Solution</summary>

The sum of daily balances is $800 \times 12 + 300 \times 18 = 15000$, so the average daily balance is $15000 \div 30 = 500$. The interest is $500 \times 0.0006575 \times 30 = 9.86$, that is, \$9.86.

Check: day by day, $800 \times 0.24 \div 365 \times 12 + 300 \times 0.24 \div 365 \times 18 = 6.31 + 3.55 = 9.86$.

</details>

3\. The minimum payment is the higher of \$10 or 3% of the balance. Find it for balances of \$4,000, \$900 and \$200.

<details class="solution" markdown>
<summary>Solution</summary>

3% of \$4,000 is \$120, which is above \$10, so \$120. 3% of \$900 is \$27, so \$27. 3% of \$200 is \$6, which is below \$10, so \$10.

Check: the switch happens at $10 \div 0.03 = 333.33$, so every balance above that uses the percent.

</details>

### Standard

4\. A \$1,500 balance at 24% (made up): compare the higher-of-\$10-or-3% rule with a fixed \$75 payment and a fixed \$45 payment.

<details class="solution" markdown>
<summary>Solution</summary>

The percent rule takes 206 months (17 years 2 months) and costs \$2,554.77 in interest. A fixed \$75 takes 26 months and costs \$434.81. A fixed \$45 takes 56 months and costs \$996.63.

Check: the monthly rate is 2%, so the first month's interest is \$30, and all three payments exceed it. The \$45 payment is the first percent payment held fixed, and it finishes in 56 months, far sooner than the 206 months of the shrinking payment.

</details>

5\. A \$5,000 balance at 18% with a fixed \$200 payment. Find the payoff time with the formula, and check it by simulation.

<details class="solution" markdown>
<summary>Solution</summary>

$B_0 r = 5000 \times 0.015 = 75$, and $n = -\ln(1 - 75/200) \div \ln(1.015) = 31.57$, so 32 payments. The simulation gives 32 months and \$1,313.96 of interest.

Check: the payment is \$200 against \$75 of first-month interest, so the loan ends, and $0.5 \times 5000 \times 0.18 \times 2.6 = 1170$ is near the \$1,314.

</details>

6\. A \$800 cash advance is repaid after 15 days. The rate is 20% and the fee is \$5 (as in the FCAC sample). Find the total cost and compare it with the same \$800 as a purchase paid in full by the due date.

<details class="solution" markdown>
<summary>Solution</summary>

The interest is $800 \times 0.20 \div 365 \times 15 = 6.58$, and the fee is \$5, so the cost is \$11.58. The purchase paid in full within the grace period costs \$0 in interest.

Check: \$11.58 over \$800 is 1.45% for 15 days.

</details>

### Challenge

7\. Show that with a payment rule of $p$ of the balance and monthly rate $r$, the balance after $k$ months is $B_0 (1 + r - p)^k$. For $B_0 = 2000$, $r = 0.015$ and $p = 0.03$, find when the payment first drops below \$10, and explain why the loan does not end then.

<details class="solution" markdown>
<summary>Solution</summary>

Know: $B_{k+1} = B_k(1 + r) - pB_k$. Want: a formula in $k$. Since $B_{k+1} = B_k (1 + r - p)$, each month multiplies the balance by the same number, so $B_k = B_0 (1 + r - p)^k$ (induction on $k$: true for $k = 0$, and if true for $k$ then multiplying by $1 + r - p$ gives it for $k + 1$).

The payment is $pB_k$, and it is below \$10 when $B_k < 333.33$. Solve $2000 \times 0.985^k < 333.33$, so $k > \ln(1/6) \div \ln(0.985) = 118.6$. The balance is first below that after 119 months (\$331.09), so the first \$10 payment is in month 120.

The loan does not end then because \$331.09 is still owed. The payment is stuck at \$10 and covers \$4.97 of interest plus only \$5.03 of principal in that month, so the rest takes another 46 or so months.

Check: $2000 \times 0.985^{119} = 331.09$, and 3% of it is \$9.93, below \$10.

</details>

8\. (Reviews [APR, APY and the effective annual rate](../02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md).) A card charges 1.5% a month on the balance. What is the effective annual rate if the interest is added to the balance each month?

<details class="solution" markdown>
<summary>Solution</summary>

Twelve months at 1.5% gives $1.015^{12} - 1 = 0.1956$, so the effective annual rate is 19.56%, not the 18% in the quoted annual rate.

Check: $1.015^{12} = 1.1956$, and 18% simple would give 1.18, so the effective rate is higher, as it should be with compounding.

</details>

## Where this shows up

- The last lesson of this chapter, [credit scores and paying off debt](05-credit-scores-and-paying-off-debt.md), compares ways to pay several debts off.
- In economics, a high borrowing rate with a payment tied to the balance is a model of liquidity constraints, and in CS the payoff simulation is a loop with a recurrence $B_{k+1} = f(B_k)$.
- In math, the percent rule is geometric decay, which you saw in [exponential functions](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md).
