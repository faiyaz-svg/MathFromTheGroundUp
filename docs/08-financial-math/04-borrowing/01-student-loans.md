# Student loans

After this lesson you can work out the monthly payment on an OSAP loan, including the interest that builds up during the six months after school, see how extra payments cut the interest, and read the basics of the Repayment Assistance Plan.

Before this: [the loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md), and [compound interest](../02-interest-and-growth/02-compound-interest.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. An Ontario loan of \$8,000 has a rate of 5.5% a year, charged monthly, and is repaid over 60 months. What is the monthly payment?
2. A federal loan of \$15,000 charges no interest and is repaid over 10 years in equal payments. What is the monthly payment?
3. A balance of \$10,000 grows at 6% a year, charged monthly, for six months before any payment is due. How much interest has been added?

<details class="solution" markdown>
<summary>Answers</summary>

1. The monthly rate is $r = 0.055 \div 12$, and $\text{PMT} = \frac{8000\,r}{1 - (1 + r)^{-60}} = 152.81$, so about \$152.81.
2. With no interest, the payment is the balance split evenly: $15000 \div 120 = 125$, that is, \$125.00 a month.
3. The balance becomes $10000 \times (1.005)^6 = 10303.78$, so \$303.78 of interest has been added.

</details>

## The idea

An Ontario student who takes OSAP gets one package with two loans inside it: a federal part and a provincial part. The federal part charges no interest. The Ontario part charges interest, and the interest starts before the first payment is due. So the balance you start repaying is a bit bigger than the total you borrowed.

After that, a student loan is an ordinary amortized loan: a fixed number of equal monthly payments, each covering that month's interest and some principal. Everything you learned about the payment formula applies. What is special is the rules around it: which part is interest-free, when payments start, and what help exists if your income is low.

The numbers below are made up. The rules come from the official pages linked in each section, and they change, so use the linked pages for real decisions. This lesson explains the math and the rules; it doesn't tell you how to repay.

## Definitions

The **Canada Student Loan** is the federal part of an OSAP loan. Since April 1, 2023, the Government of Canada has permanently stopped charging interest on it. The National Student Loans Service Centre says: "the Government of Canada has permanently eliminated the accumulation of interest on all Canada Student Loans" ([NSLSC](https://www.csnpe-nslsc.canada.ca/en/things-you-need-to-know)). The Ontario page says the federal rate is 0%.

In plain words: the federal balance stays the same size until you pay it down. Each dollar you pay goes to principal.

The **Ontario student loan** is the provincial part. Ontario's page says: "Ontario interest rate is calculated at prime rate plus 1%" ([ontario.ca, pay back OSAP](https://www.ontario.ca/page/pay-back-osap)). The **prime rate** is the benchmark rate that banks set for their best borrowers; it moves when the Bank of Canada changes its policy rate. The page also says the rates on your first payment date set your monthly payment. It does not say whether the rate then stays fixed or floats, so check your loan agreement.

The **non-repayment period** is the stretch after you graduate or leave full-time studies before payments are due. The Ontario page says: "You have six months after you graduate or leave full-time studies before you need to start repaying your OSAP loan." It also says: "You will be charged interest on the Ontario portion of your loan during your six-month grace period", and that this interest is added to the principal. Federal interest isn't charged.

The **Repayment Assistance Plan** (RAP) lowers your payment when it is too large for your income. There are two versions, one from each government, covered in their own section below.

## How to do it

### Computing an OSAP repayment

Name the numbers. The Ontario portion borrowed is $B_0$, the annual rate is the prime rate plus 1 percentage point, and the monthly rate is $r$, the annual rate divided by 12. (Real lenders may count days or use another convention. The linked pages and your agreement say how OSAP does it, so treat the numbers here as close estimates.)

1. Find the Ontario rate: prime rate plus 1%. Divide by 12 to get $r$.
2. Grow the Ontario balance through the six months with no payments: $B = B_0 (1 + r)^6$. The interest added is $B - B_0$.
3. Choose the number of monthly payments $n$ (this is a made-up choice here; the repayment length is in your loan documents).
4. Compute the Ontario payment with the amortization formula from the [time value of money chapter](../03-time-value-of-money/03-loan-amortization-formula.md):

$$
\text{PMT}_{\text{Ontario}} = \frac{B\, r}{1 - (1 + r)^{-n}}.
$$

5. Compute the federal payment, which has no interest: $\text{PMT}_{\text{federal}} = F \div n$, where $F$ is the federal balance.
6. Add the two payments for your monthly total. Check by multiplying the payment by $n$ and subtracting the balance, which gives the total interest.

For a quick sanity check, the Ontario total of all payments must exceed $B$ by a modest amount, and the federal total must equal $F$ exactly.

<div class="note" markdown>

These figures are for 2026 and change every year. Check the linked pages before using them for real decisions. The prime rate and the repayment length in this lesson are made up for illustration.

</div>

### How an extra payment saves interest

Each month, interest is charged on the balance that is left. If you pay more than the required payment, the extra goes straight to principal. The balance is smaller from then on, so every later month charges less interest, and the loan ends sooner. To find the new payoff time, solve the loan equation for $n$:

$$
n = -\frac{\ln\!\left(1 - \frac{B\, r}{P}\right)}{\ln(1 + r)},
$$

where $P$ is the payment you actually make. This is the exponential-equation method from [exponential and logarithmic equations](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md). It needs $P > Br$, the first month's interest, or the balance never goes down. The result is usually not a whole number: round up, and the last payment is smaller.

On the federal portion there is no interest to save, so paying extra there only shortens the time. Which portion to pay down first is a real question, and the interest rates tell you the answer: the 0% part costs nothing to carry, and the Ontario part does.

### The Repayment Assistance Plan

Both governments offer repayment assistance ([ontario.ca](https://www.ontario.ca/page/pay-back-osap)). They are two plans with different rules, so don't mix their numbers.

The federal plan, as described by the Government of Canada when it was announced in November 2022 ([news release](https://www.canada.ca/en/employment-social-development/news/2022/11/the-repayment-assistance-plan.html)): no payments until income is at least \$40,000 for a single borrower (higher with family size, and indexed each year), payments capped at 10% of household income, a maximum of 15 years, and a new application every six months. Those 2022 thresholds are indexed, so the current dollar figures are higher. Look up the current amount on the official federal RAP page.

The Ontario plan, from the Ontario page: your payment is based on family income and family size and never exceeds 20% of family income. You reapply every six months. Interest relief lasts up to 60 months, and the Government of Ontario covers the monthly interest that your payment doesn't.

The math of RAP is a cap. If the standard payment is below the cap, the cap doesn't matter. If it is above, the plan lowers your payment to what the plan sets for your income. The exact payment formula is on the official pages; this lesson only uses the caps.

## Worked examples

<div class="example" markdown>

### Example 1: a full OSAP repayment

Suppose you leave school with \$18,000 in federal loans and \$12,000 in Ontario loans. Suppose the prime rate is 4.5% (a made-up value). You choose 120 monthly payments.

Step 1: the Ontario rate is $4.5\% + 1\% = 5.5\%$ a year, so $r = 0.055 \div 12 = 0.0045833\ldots$ a month.

Step 2: grow the Ontario balance for six months:

$$
B = 12000 \times (1 + 0.0045833)^6 = 12333.80.
$$

So \$333.80 of interest is added before the first payment. The federal balance is still \$18,000.

Step 3: $n = 120$.

Step 4: the Ontario payment is

$$
\text{PMT}_{\text{Ontario}} = \frac{12333.80 \times 0.0045833}{1 - (1.0045833)^{-120}} = 133.85.
$$

Step 5: the federal payment is $18000 \div 120 = 150.00$.

Step 6: the total is $133.85 + 150.00 = 283.85$ dollars a month. Over 120 payments the Ontario part costs $133.854 \times 120 = 16062.50$ in total, so the interest on it is $16062.50 - 12333.80 = 3728.70$. Counting the \$333.80 from the six months, the Ontario loan cost \$4,062.50 more than the \$12,000 you borrowed. The federal part cost nothing extra.

Check: the Ontario balance after the 120th payment should be zero. The payoff loop in the code box below ends after exactly 120 months for this payment, and the first month's interest is $12333.80 \times 0.0045833 = 56.53$, which is less than the \$133.85 payment, so the balance is going down.

</div>

<div class="example" markdown>

### Example 2: what \$100 extra a month does

Keep the Ontario loan from Example 1: balance \$12,333.80, $r = 0.0045833$, required payment \$133.85. Suppose you pay \$100 extra every month, so $P = 233.85$.

The payoff time is

$$
n = -\frac{\ln\!\left(1 - \frac{12333.80 \times 0.0045833}{233.85}\right)}{\ln(1.0045833)} = 60.5,
$$

so 61 payments, the last one small. The interest paid is \$1,817.56, against \$3,728.70 on the original plan. The extra \$100 a month saves \$1,911.14 in interest and finishes 59 months sooner.

Check: the total paid is the balance plus the interest, $12333.80 + 1817.56 = 14151.36$. Sixty payments of \$233.85 come to \$14,031.00, so the 61st payment is about \$120, a small last one.

</div>

<div class="example" markdown>

### Example 3: the rate moves

The rate on the Ontario part is prime plus 1%, and prime changes. Suppose prime were 5.5% instead, so the Ontario rate is 6.5%. On the same \$12,333.80 over 120 months, the payment is

$$
\frac{12333.80 \times (0.065 \div 12)}{1 - (1 + 0.065 \div 12)^{-120}} = 140.05.
$$

That is \$6.20 more a month than at 5.5%, and total interest on it is $140.048 \times 120 - 12333.80 = 4471.94$, which is \$743.24 more than the \$3,728.70 in Example 1. One percentage point on a 10-year loan is worth about \$740 here.

The page says the first payment date's rates set your monthly payment, so this comparison is what "prime was higher on the day payments began" would mean. It does not say what happens later if prime changes, so read your agreement.

Check: $140.05 - 133.85 = 6.20$, and $6.20 \times 120 = 744$, matching the interest difference up to rounding.

</div>

<div class="example" markdown>

### Example 4: when does a payment even cover the interest (finish it yourself)

On the \$12,333.80 balance at 5.5%, find the smallest monthly payment that keeps the balance from growing, then the number of months to repay if you pay \$100 a month.

Step 1: the balance stops growing when the payment equals one month's interest, $Br$.

Step 2: compute $Br = 12333.80 \times 0.0045833$.

Step 3: for \$100, use $n = -\ln(1 - Br/P) \div \ln(1 + r)$.

<details class="solution" markdown>
<summary>Finish</summary>

Step 2: $Br = 56.53$, so any payment under \$56.53 leaves the balance larger each month. Step 3: $1 - 56.53/100 = 0.4347$, and $n = -\ln(0.4347) \div \ln(1.0045833) = 182.2$, so 183 payments, about 15.25 years.

Check: $100 \times 182.2 = 18220$ in payments against a balance of \$12,333.80 means about \$5,886 of interest, which is plausible for a payment only a little above the \$56.53 of monthly interest.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: forgetting the six months of interest. If you plug \$12,000 into the payment formula instead of \$12,333.80, you get \$130.23, which is \$3.62 short each month. The loan then isn't paid off at the end. The balance that matters is the one on the day payments start.

</div>

<div class="warning" markdown>

Watch out: treating the federal and Ontario parts as one loan at one rate. The federal part has 0% interest and the Ontario part has prime plus 1%. A blended rate would hide that paying down the Ontario part is where interest is saved.

</div>

<div class="warning" markdown>

Watch out: mixing up the two RAP plans. The federal caps payments at 10% of household income and the Ontario plan at 20% of family income. They are different plans for different parts of the loan, and the two percentages are not a conflict.

</div>

<div class="warning" markdown>

Watch out: using 5.5% where you need 0.055. In the formula, $r$ is the monthly rate as a decimal, $0.055 \div 12$. Using 5.5 or 0.055 gives a payment that is wildly wrong; a size check catches it, because the first month's interest should be about \$56, not \$680.

</div>

Untidy answers are normal. A payoff time of 60.5 months means 60 full payments and one small final one. The last payment is whatever is left, and it is less than the others.

## Tricks and shortcuts

A quick estimate of the total interest on a loan that is paid down evenly is about half the balance times the annual rate times the number of years. For \$12,333.80 at 5.5% over 10 years, that is $0.5 \times 12333.80 \times 0.055 \times 10 = 3391.80$, close to the exact \$3,728.70 and good enough to catch a large mistake. It is rough because it uses the average balance without compounding.

The interest-only payment, $Br$, is a lower bound on any useful payment. If you can't pay at least that, the loan is growing.

## In code

The schedule below recomputes the numbers in Examples 1 and 2.

<details class="code" markdown>
<summary>In code</summary>

```python
from math import log

def payment(pv, r, n):
    return pv * r / (1 - (1 + r) ** -n)

def payoff(balance, r, pay):
    months, interest = 0, 0.0
    while balance > 0.005:
        i = balance * r
        interest += i
        balance = balance + i - min(pay, balance + i)
        months += 1
    return months, interest

r = 0.055 / 12
b = 12000 * (1 + r) ** 6
p = payment(b, r, 120)
print(round(b, 2), round(p, 2))                      # 12333.8 133.85
print(round(p * 120 - b, 2))                         # 3728.7
print(payoff(b, r, p)[0])                            # 120
months, interest = payoff(b, r, p + 100)
print(months, round(interest, 2))                    # 61 1817.56
print(round(-log(1 - b * r / (p + 100)) / log(1 + r), 1))  # 60.5
```

</details>

## FAQ

### Why does the federal part stay interest-free while the Ontario part does not?

They are two loans from two governments. The federal government permanently stopped charging interest on Canada Student Loans from April 1, 2023, and Ontario charges prime plus 1% on its portion. The math is the same for both; the rate is the difference.

### Does interest really build up while I'm still in school?

The Ontario page says interest is charged on the Ontario portion during the six months after you finish, and this lesson uses that. It doesn't say what happens during full-time studies, so check your agreement for the in-school rules.

### Is it better to pay the Ontario part first?

It saves more interest than paying down the federal part, because the federal part has none. Whether to pay extra at all depends on what else the money could do, such as paying a credit card at 20%. That comparison is the subject of the last lesson of this chapter.

### What if my payment is too large for my income?

Apply to the Repayment Assistance Plan. The plan sets a payment from your family income and size, and it is capped. The caps above are in the official pages. The plan also covers interest the payment doesn't, for up to 60 months on the Ontario side.

## Practice

### Warm-up

1\. The prime rate is 4.5% (made up). What is the Ontario rate, the monthly rate, and the first month's interest on \$12,000?

<details class="solution" markdown>
<summary>Solution</summary>

The Ontario rate is $4.5\% + 1\% = 5.5\%$. The monthly rate is $0.055 \div 12 = 0.0045833$. The first month's interest is $12000 \times 0.0045833 = 55.00$, so \$55.00.

Check: 5.5% of \$12,000 is \$660 a year, and $660 \div 12 = 55$.

</details>

2\. A federal balance of \$21,600 is repaid over 9 years. What is the monthly payment, and how much interest is paid?

<details class="solution" markdown>
<summary>Solution</summary>

Nine years is 108 months, and $21600 \div 108 = 200$, so \$200.00 a month. There is no interest, so the interest paid is \$0.

Check: $200 \times 108 = 21600$, the balance.

</details>

3\. An Ontario balance of \$9,000 grows at 5.5% a year, charged monthly, during the six months before payments start. How much interest is added?

<details class="solution" markdown>
<summary>Solution</summary>

The balance becomes $9000 \times (1 + 0.055/12)^6 = 9250.35$, so the interest added is \$250.35.

Check: simple interest for half a year is $9000 \times 0.055 \times 0.5 = 247.50$, and compounding adds a little more.

</details>

### Standard

4\. Find the monthly payment on \$9,000 at 5.5%, over 96 months, and the total interest.

<details class="solution" markdown>
<summary>Solution</summary>

With $r = 0.055/12$ and $n = 96$, $\text{PMT} = \frac{9000\,r}{1 - (1 + r)^{-96}} = 116.09$, about \$116.09. The total paid is $116.0939 \times 96 = 11145.01$, so the interest is $11145.01 - 9000 = 2145.01$.

Check: the first month's interest is \$41.25, below the payment, and the rough estimate $0.5 \times 9000 \times 0.055 \times 8 = 1980$ is near \$2,145.

</details>

5\. The Ontario balance is \$12,333.80 and the term is 120 months. By how much does the monthly payment rise if the rate goes from 5.5% to 6.5%?

<details class="solution" markdown>
<summary>Solution</summary>

At 5.5% the payment is \$133.85; at 6.5% it is \$140.05. The difference is $140.05 - 133.85 = 6.20$, so \$6.20 more a month.

Check: that is $6.20 \times 120 = 744$ dollars over the loan, close to the interest difference of \$743.24 (the gap is rounding).

</details>

6\. On the \$12,333.80 balance at 5.5% with a \$133.85 payment, you add \$50 a month. How many payments, and how much interest is saved compared with 120 payments?

<details class="solution" markdown>
<summary>Solution</summary>

The new payment is \$183.85. Then $n = -\ln(1 - 56.53/183.85) \div \ln(1.0045833) = 80.3$, so 81 payments. The total interest on the faster plan is \$2,438.03, against \$3,728.70, so you save \$1,290.67 and finish 39 months sooner.

Check: the balance plus interest is $12333.80 + 2438.03 = 14771.83$. Eighty payments of \$183.85 make \$14,708.00, so the 81st payment is about \$64, a small last one.

</details>

### Challenge

7\. A borrower can pay only \$100 a month on the Ontario balance of \$12,333.80 at 5.5%. Show that this is enough to repay the loan, and find the number of payments. Then find the household income at which a 10% cap equals the \$150 federal payment from Example 1.

<details class="solution" markdown>
<summary>Solution</summary>

The first month's interest is \$56.53, and \$100 is more than that, so the principal falls each month and the loan ends. The number of payments is $n = -\ln(1 - 56.53/100) \div \ln(1.0045833) = 182.2$, so 183 payments.

For the cap, 10% of income per year must equal $150 \times 12 = 1800$, so income is $1800 \div 0.10 = 18000$, that is, \$18,000 a year. At a household income below that, the 10% cap is below \$150 a month. (Whether the plan applies also depends on the official threshold and family size; this only shows how the cap works.)

Check: $0.10 \times 18000 \div 12 = 150$.

</details>

8\. (Reviews [exponential and logarithmic equations](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md).) If an Ontario balance of \$12,000 at 5.5%, charged monthly, were left unpaid, how many months until it doubles?

<details class="solution" markdown>
<summary>Solution</summary>

Solve $(1 + 0.055/12)^n = 2$. Taking logs, $n = \ln 2 \div \ln(1.0045833) = 151.6$ months, about 12.6 years.

Check: $(1.0045833)^{151.6} \approx 2.00$, and the rule of 72 gives $72 \div 5.5 = 13.1$ years, close.

</details>

## Where this shows up

- Next, [car loans and total cost](02-car-loans-and-total-cost.md) uses the same payment formula for a larger loan with a shorter term.
- In economics, a student loan is a standard example of borrowing against future income, and the RAP caps work like an income-contingent loan.
- In CS terms, the schedule in the code box is a simple loop with state (the balance), the same pattern as many simulations.
