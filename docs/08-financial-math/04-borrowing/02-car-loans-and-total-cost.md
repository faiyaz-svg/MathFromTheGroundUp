# Car loans and total cost

After this lesson you can compute a car loan payment and its total interest, add Ontario HST to a vehicle price, compare a 0% offer with a rebate plus a bank loan, and add depreciation and running costs to see what a car costs to own.

Before this: [the loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md), [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md) and [student loans](01-student-loans.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A car costs \$26,500 before tax. What are the 13% HST and the total?
2. A \$20,000 loan at 6% a year, charged monthly, is repaid over 60 months. Find the monthly payment and the total interest.
3. The same loan is repaid over 84 months instead. What are the payment and the total interest?

<details class="solution" markdown>
<summary>Answers</summary>

1. The tax is $0.13 \times 26500 = 3445$, so \$3,445.00, and the total is \$29,945.00.
2. With $r = 0.06 \div 12 = 0.005$, $\text{PMT} = \frac{20000 \times 0.005}{1 - 1.005^{-60}} = 386.66$. The total paid is $386.656 \times 60 = 23199.36$, so the interest is \$3,199.36.
3. For $n = 84$, the payment is \$292.17 and the total paid is \$24,542.37, so the interest is \$4,542.37. The payment is \$94.49 lower and the interest is \$1,343.01 higher.

</details>

## The idea

A car is the first big purchase for many people, and it is usually bought with a loan. The salesperson often talks about the monthly payment, because that number is easy to fit into a budget. But a payment is only one side of the cost. A lower payment can come from a longer loan, and a longer loan means more months of interest. The other side is the total: everything you pay for the car, over the whole time, minus what the car is worth at the end.

This lesson builds that total in layers. First the loan itself (payment and interest), then the tax that goes on top of the sticker price, then two comparisons that come up in showrooms (a 0% offer against a rebate, and a short loan against a long one), and last the costs that have nothing to do with the loan: depreciation, insurance, fuel and repairs.

All rates, prices and depreciation rates here are made up. Your own numbers come from real offers. This lesson explains the math and doesn't tell you what to buy.

## Definitions

The **amount financed** is the principal of the loan: the price plus tax and fees, minus the down payment (money you pay at the start) and any trade-in value.

In plain words: it is what you owe on day one.

The **term** of a loan is the number of monthly payments, $n$. A 60-month loan has a term of five years.

The **total cost of the loan** is the sum of all the payments you make, $n \times \text{PMT}$. The **total interest** is that sum minus the amount financed. These two numbers don't include the down payment, so the total you pay out of pocket is the total cost of the loan plus the down payment.

**Depreciation** is the loss of a car's value over time. If a car is worth $V_0$ today and loses a fixed fraction $d$ of its value each year, its value after $t$ years is

$$
V_t = V_0 (1 - d)^t.
$$

In plain words: each year the car keeps $(1 - d)$ of what it was worth the year before. This is exponential decay, the same shape as [exponential functions](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md) with a base less than 1.

The **total cost of ownership** is everything you spend to own and run the car over a period, minus what you get when you sell it at the end.

## How to do it

### The payment and the total

The payment formula is the one from the [time value of money chapter](../03-time-value-of-money/03-loan-amortization-formula.md). With amount financed $\text{PV}$, monthly rate $r$ (the annual rate divided by 12) and term $n$:

$$
\text{PMT} = \frac{\text{PV}\, r}{1 - (1 + r)^{-n}}.
$$

1. Start from the price before tax. Add 13% HST by multiplying by 1.13 (Ontario's HST is 13%, the 5% federal part plus an 8% provincial part; see the [CRA rates page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) and [ontario.ca](https://www.ontario.ca/document/harmonized-sales-tax-hst)).
2. Subtract the down payment and trade-in to get the amount financed $\text{PV}$.
3. Compute $r$ and $n$, then $\text{PMT}$.
4. The total cost of the loan is $n \times \text{PMT}$ and the interest is that minus $\text{PV}$.
5. Check: the interest in the first month is $\text{PV} \times r$, and it must be less than $\text{PMT}$.

<div class="note" markdown>

The HST rate is for 2026 and changes only when the law changes. Check the linked pages before using it for real decisions. Dealers can add other charges such as licensing or delivery fees; this lesson leaves them out.

</div>

### A 0% offer against a rebate

Dealers sometimes offer a choice: finance at 0%, or take a cash rebate and finance at a bank's rate. The 0% offer has no interest, so its total cost is just the price. The rebate option lowers the price you finance but charges interest. Which is cheaper depends on the bank's rate, and there is a rate where the two cost the same.

1. Compute the 0% payment: $P_A = \text{price} \div n$.
2. Compute the rebate option's amount financed: $\text{PV}_B = \text{price} - \text{rebate}$.
3. Find the rate $j$ at which the payment on $\text{PV}_B$ over $n$ months equals $P_A$. There is no closed form for $j$, so try rates (or let a program do bisection) until the payments match.
4. If the bank offers a rate below $j$, the rebate option costs less. Above $j$, the 0% offer costs less.

To keep the comparison simple, assume the same HST applies in both cases and that you finance the whole tax-included price. Whether HST is charged before or after a rebate depends on the deal, so ask the dealer.

### Longer terms

A longer term lowers the payment and raises the total interest. The reason is in the formula: spreading the same principal over more months makes each payment smaller, but the interest is charged on the balance for more months. Example 2 shows the numbers.

### Depreciation and total cost of ownership

1. Pick a yearly depreciation rate $d$ (made up here) and compute the value at the end of your holding period, $V_0(1 - d)^t$.
2. The cost of the car itself is price plus HST minus that resale value.
3. Add the interest paid on the loan.
4. Add running costs: insurance, fuel, maintenance, licensing. Use the amounts you actually expect.
5. Divide by the number of months or years for a cost per month or per year.

## Worked examples

<div class="example" markdown>

### Example 1: a car loan from sticker price to total

Suppose a car's price is \$28,000 before tax. You put \$3,000 down. Suppose the bank rate is 7.2% a year, charged monthly (a made-up rate), over 60 months.

Step 1: the HST is $0.13 \times 28000 = 3640$, so the price with tax is \$31,640.

Step 2: the amount financed is $31640 - 3000 = 28640$, that is, \$28,640.

Step 3: $r = 0.072 \div 12 = 0.006$ and $n = 60$.

Step 4: the payment is

$$
\text{PMT} = \frac{28640 \times 0.006}{1 - 1.006^{-60}} = 569.81.
$$

The total cost of the loan is $569.81 \times 60 = 34188.76$, so the interest is $34188.76 - 28640 = 5548.76$. With the down payment, you pay \$37,188.76 in all for a car whose price with tax was \$31,640.

Step 5: the first month's interest is $28640 \times 0.006 = 171.84$, less than \$569.81, so the balance falls.

Check: the interest is $5548.76 \div 28640 = 19.4\%$ of the amount financed, close to the rough estimate $0.5 \times 7.2\% \times 5 = 18\%$ for a five-year loan.

</div>

<div class="example" markdown>

### Example 2: longer terms, lower payments, more interest

Keep the \$28,640 and the 7.2% rate, and change the term:

| Term (months) | Payment | Total paid | Total interest |
|---|---|---|---|
| 48 | \$688.48 | \$33,047.09 | \$4,407.09 |
| 60 | \$569.81 | \$34,188.76 | \$5,548.76 |
| 72 | \$491.04 | \$35,354.79 | \$6,714.79 |
| 84 | \$435.06 | \$36,545.03 | \$7,905.03 |

Going from 48 to 84 months cuts the payment by \$253.42 a month, but adds \$3,497.94 of interest. Each extra year costs between \$1,100 and \$1,200 more.

There is a second cost not in the table. A car loses value fast in the early years, and a long loan pays down the principal slowly, so for the first years you may owe more than the car is worth.

Check: $688.48 \times 48 = 33047.04$ and $435.06 \times 84 = 36545.04$, matching the totals up to rounding.

</div>

<div class="example" markdown>

### Example 3: 0% against a rebate

A car with tax costs \$31,640. The dealer offers either 0% for 60 months, or a \$3,000 rebate with your own bank loan for 60 months. Suppose you would finance the whole amount in both cases.

The 0% offer: payment $31640 \div 60 = 527.33$, total \$31,640.00.

The rebate offer finances $31640 - 3000 = 28640$. Which bank rate makes its payment \$527.33? Trying rates:

| Bank rate | Payment | Total paid | Compared with 0% |
|---|---|---|---|
| 3% | \$514.62 | \$30,877.40 | \$762.60 cheaper |
| 4% | \$527.45 | \$31,646.95 | \$6.95 dearer |
| 5% | \$540.47 | \$32,428.33 | \$788.33 dearer |
| 6% | \$553.69 | \$33,221.49 | \$1,581.49 dearer |

The break-even rate is between 3% and 4%, close to 4%. Solving the equal-payment condition numerically gives $j = 3.991\%$ a year. A bank rate below 3.99% makes the rebate option cheaper; above it, the 0% offer is cheaper.

Check: the payment on \$28,640 at 3.991% over 60 months is \$527.33, the same as the 0% payment.

<div class="warning" markdown>

Watch out: comparing only the payments of a bank loan with no rebate. The 0% offer must be compared with the rebate, not with the sticker price, because the rebate is what you give up by taking the 0%.

</div>

</div>

<div class="example" markdown>

### Example 4: depreciation and the cost of ownership (finish it yourself)

Suppose the car from Example 1 loses 15% of its value a year, measured on the \$28,000 price before tax. You keep it for 5 years. Insurance is \$1,800 a year, fuel \$2,400 and maintenance \$700 (all made up).

Step 1: the value after 5 years is $28000 \times 0.85^5$.

Step 2: the cost of the car itself is the price with tax, \$31,640, minus that value.

Step 3: add the loan interest from Example 1, \$5,548.76, and the running costs for five years.

Find the total, and the cost per month.

<details class="solution" markdown>
<summary>Finish</summary>

Step 1: $28000 \times 0.85^5 = 12423.75$, so the car is worth about \$12,424. (After each year the value is \$23,800, \$20,230, \$17,195.50, \$14,616.17 and \$12,423.75.)

Step 2: $31640 - 12423.75 = 19216.25$.

Step 3: the running costs are $5 \times (1800 + 2400 + 700) = 24500$. The total is $19216.25 + 5548.76 + 24500 = 49265.01$, so about \$49,265. Over 60 months that is $49265.01 \div 60 = 821.08$, about \$821 a month, while the loan payment alone is \$569.81.

Check: the pieces add up, $19216.25 + 5548.76 = 24765.01$ and $24765.01 + 24500 = 49265.01$. The running costs are the biggest piece, which is the point: the loan payment is not the whole cost.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: shopping by the monthly payment. A dealer can hit any payment you name by stretching the term. Always ask for the term and the total, then compare totals. Example 2 shows an 84-month loan costing \$3,497.94 more interest than a 48-month one.

</div>

<div class="warning" markdown>

Watch out: forgetting the HST when you compare with a quoted price. The sticker price of \$28,000 is not what you finance. In Ontario the amount financed starts from \$31,640, and tax-in and tax-out prices are different numbers.

</div>

<div class="warning" markdown>

Watch out: counting the 0% offer as free. It has no interest, but it comes with a rebate you give up. Example 3 shows that at a bank rate of 5% the 0% offer is \$788.33 cheaper, and at 3% it is \$762.60 dearer, so neither is free.

</div>

<div class="warning" markdown>

Watch out: treating depreciation as zero because no cheque is written. Depreciation is a real cost; it shows up when you sell. In Example 4 it is about \$19,000 of the \$49,000.

</div>

An edge case is a loan at 0%: the formula divides by zero when $r = 0$, so the payment is just $\text{PV} \div n$. Another is a payoff that isn't a whole number of months: the last payment is smaller.

## Tricks and shortcuts

A quick check on a loan: the total interest is roughly half the amount financed times the annual rate times the years. For \$28,640 at 7.2% over 5 years, that gives about \$5,150, against the exact \$5,548.76. It is a quick way to see a payment that is far off.

To get a price with HST, multiply by 1.13. To go back from a tax-in price to the price before tax, divide by 1.13, not subtract 13%, as in [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).

## In code

The program finds the break-even rate in Example 3 by bisection: it repeatedly halves an interval that contains the answer.

<details class="code" markdown>
<summary>In code</summary>

```python
def payment(pv, r, n):
    return pv * r / (1 - (1 + r) ** -n)

price = 28000 * 1.13               # 31,640 with HST
print(round(price, 2))             # 31640.0
loan = price - 3000
p = payment(loan, 0.072 / 12, 60)
print(round(p, 2), round(p * 60 - loan, 2))   # 569.81 5548.76

target = price / 60                # the 0% payment
lo, hi = 0.0, 0.2
for _ in range(100):
    mid = (lo + hi) / 2
    if payment(loan, mid / 12, 60) > target:
        hi = mid
    else:
        lo = mid
print(round(lo * 100, 3))          # 3.991
```

</details>

## FAQ

### Why does a longer loan cost more if the rate is the same?

The rate is the same, but you owe the money for more months. Interest is charged each month on the balance, so slower repayment means a larger balance for longer. The extra months add interest.

### Is it ever right to take a longer term?

The math says it costs more in interest. The reason to take one is the budget: a payment that fits. If you pick a long term, you can still pay extra to shorten it, as in [student loans](01-student-loans.md), if the loan has no prepayment penalty. Check the contract.

### Why is the break-even rate not a round number?

The equal-payment condition is $\text{PMT}(28640, j, 60) = 527.33$, and the payment formula has $j$ inside a power. Such equations rarely have a closed-form solution, so you solve them with a search like the one in the code box.

### Does depreciation really follow a fixed percent per year?

No. Real cars lose more in the first year or two and then less. A fixed 15% is a simple model that gets the shape right. Use real used-car prices for a real decision.

## Practice

### Warm-up

1\. A car costs \$26,500 before tax. Find the HST and the total at 13%.

<details class="solution" markdown>
<summary>Solution</summary>

The tax is $0.13 \times 26500 = 3445$, so \$3,445.00, and the total is $26500 + 3445 = 29945$, that is, \$29,945.00.

Check: $1.13 \times 26500 = 29945$.

</details>

2\. Find the monthly payment and total interest on \$20,000 at 6% for 60 months.

<details class="solution" markdown>
<summary>Solution</summary>

With $r = 0.005$ and $n = 60$, $\text{PMT} = \frac{20000 \times 0.005}{1 - 1.005^{-60}} = 386.66$. The total is $386.656 \times 60 = 23199.36$, so the interest is \$3,199.36.

Check: the first month's interest is \$100, below the payment.

</details>

3\. A car worth \$30,000 loses 18% of its value each year. What is it worth after 3 years, and how much value was lost?

<details class="solution" markdown>
<summary>Solution</summary>

The value is $30000 \times 0.82^3 = 16541.04$, so about \$16,541. The loss is $30000 - 16541.04 = 13458.96$, that is, \$13,458.96. By year the value is \$30,000, \$24,600, \$20,172 and \$16,541.04.

Check: three yearly losses of 18% of a shrinking value add up to less than $3 \times 18\% = 54\%$ of \$30,000, which is \$16,200. The loss of \$13,458.96 is under that, as expected.

</details>

### Standard

4\. For \$20,000 at 6%, compare a 48-month and a 72-month loan: payment, total interest, and the difference in interest.

<details class="solution" markdown>
<summary>Solution</summary>

At 48 months the payment is \$469.70 and the interest is \$2,545.63. At 72 months the payment is \$331.46 and the interest is \$3,864.96. The longer loan has a payment \$138.24 lower and \$1,319.33 more interest.

Check: $469.70 \times 48 = 22545.60$, which is $20000 + 2545.63$ up to rounding.

</details>

5\. A \$25,000 car with 13% HST is offered at 0% for 48 months, or with a \$2,000 rebate and a bank loan for 48 months. At what bank rate are the two the same?

<details class="solution" markdown>
<summary>Solution</summary>

The price with tax is $25000 \times 1.13 = 28250$. The 0% payment is $28250 \div 48 = 588.54$. The rebate option finances $28250 - 2000 = 26250$. Searching for the rate that gives a \$588.54 payment gives 3.65% a year.

Check: at 5% the payment on \$26,250 is \$604.52, higher than \$588.54, so a 5% bank rate favours the 0% offer, and the break-even must be lower than 5%, as found.

</details>

6\. A \$22,000 car (before tax) is financed for 60 months at 6% with \$2,000 down. It loses 15% a year, and running costs are \$4,000 a year. Find the cost of ownership over 5 years and per month.

<details class="solution" markdown>
<summary>Solution</summary>

With tax the price is \$24,860, so the amount financed is \$22,860. The payment is \$441.95 and the interest is \$3,656.87. The resale value is $22000 \times 0.85^5 = 9761.52$. The cost of the car is $24860 - 9761.52 = 15098.48$. Running costs are $5 \times 4000 = 20000$. The total is $15098.48 + 3656.87 + 20000 = 38755.35$, so about \$38,755, or \$645.92 a month.

Check: $38755.35 \div 60 = 645.92$.

</details>

### Challenge

7\. You can afford \$400 a month on a \$20,000 loan at 6% a year, charged monthly. How many months will it take? Explain why \$100 a month would not work.

<details class="solution" markdown>
<summary>Solution</summary>

Use $n = -\ln(1 - \text{PV}\, r / P) \div \ln(1 + r)$ with $\text{PV}\, r = 100$. Then $n = -\ln(1 - 100/400) \div \ln(1.005) = 57.68$, so 58 payments.

At \$100 a month the payment equals the first month's interest, $20000 \times 0.005 = 100$. The balance never falls, and the formula would take the log of 0.

Check: at 60 months the payment is \$386.66, a little under \$400, and 58 payments of about \$400 is consistent.

</details>

8\. (Reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).) A dealer's window shows a total of \$33,900 including 13% HST. What was the price before tax? What would you get by subtracting 13% of \$33,900 instead?

<details class="solution" markdown>
<summary>Solution</summary>

The total is 113% of the price, so the price is $33900 \div 1.13 = 30000$, that is, \$30,000. Subtracting 13% of the total gives $33900 - 0.13 \times 33900 = 29493$, which is \$507 too low.

Check: $1.13 \times 30000 = 33900$.

</details>

## Where this shows up

- The next lesson, [lease vs buy a car](03-lease-vs-buy-a-car.md), compares this total with a lease over the same period.
- In economics, depreciation is how a durable good's value is spread over its life, and the same exponential decay appears in capital stock models.
- In CS, a search for the break-even rate is bisection, the same idea as a binary search on a monotone function.
