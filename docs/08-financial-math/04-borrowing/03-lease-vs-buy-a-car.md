# Lease vs buy a car

After this lesson you can build a lease payment from its two parts, convert between a money factor and a rate, and compare the total cost of a lease with the cost of buying the same car and selling it at the end.

Before this: [car loans and total cost](02-car-loans-and-total-cost.md), [the loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md) and [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A lease has a net price of \$30,000, a residual value of \$17,400, 36 months, and a lease rate of 4.8% a year. Using the money factor method, what is the monthly payment before tax?
2. What money factor is the same as a 5.04% rate?
3. A lease allows 20,000 km a year for 3 years, and charges \$0.12 for each extra kilometre. You drive 75,000 km. What is the excess charge?

<details class="solution" markdown>
<summary>Answers</summary>

1. The money factor is $4.8 \div 2400 = 0.002$. The depreciation part is $(30000 - 17400) \div 36 = 350$. The rent charge is $(30000 + 17400) \times 0.002 = 94.80$. The payment is $350 + 94.80 = 444.80$, so \$444.80.
2. Divide the rate in percent by 2400: $5.04 \div 2400 = 0.0021$.
3. The limit is $3 \times 20000 = 60000$ km, so you are 15,000 km over, and the charge is $15000 \times 0.12 = 1800$, that is, \$1,800.

</details>

## The idea

A lease is a long rental of a car. You pay a monthly amount for the right to drive it for a set time, usually 3 to 5 years, and then give it back. The Financial Consumer Agency of Canada describes it this way: "You make regular payments for the use of the car over a set period", usually to a financial institution, and the payments are generally lower than a car loan with the same term ([FCAC](https://www.canada.ca/en/financial-consumer-agency/services/loans/financing-car/financing-options.html)).

Why lower? Because you aren't paying for the whole car. You pay for the part of its value that is used up while you drive it, plus a charge for tying up the owner's money. The part that is left at the end, the residual value, is never paid by you. A loan is different: you pay for the whole car and then own it.

That makes lease against buy a question about total cost over the same time. Compare the total you pay on a lease with the total you pay to buy the car and sell it when the lease would have ended. The answer depends on numbers nobody knows in advance, such as the car's market value in four years, so the useful tool is a sensitivity table: change one assumption and see what happens.

All the prices, rates and fees in this lesson are made up. They are not offers, and real leases vary.

## Definitions

The **net capitalized cost** (or cap cost) is the price the lease is based on: the car's price after any trade-in or down payment that lowers it. Call it $C$.

The **residual value** is the amount the lessor expects the car to be worth at the end of the lease, set in the contract. Call it $R$. It is often given as a percent of the original price.

In plain words: $C - R$ is the value you use up.

The **lease term** is the number of months, $n$.

The **depreciation charge** is the part of the monthly payment that pays for the value you use up: $(C - R) \div n$.

The **rent charge** is the part that pays for the money tied up in the car. The US convention is to write it using a **money factor** $m$, a small decimal:

$$
\text{rent charge} = (C + R)\, m, \qquad m = \frac{\text{rate in percent}}{2400}.
$$

The monthly payment before tax is the sum of the two parts:

$$
\text{PMT} = \frac{C - R}{n} + (C + R)\, m.
$$

In plain words: you pay one share of the value you use up each month, plus a charge on the average amount the lessor has tied up.

A **kilometre allowance** is the number of kilometres the lease permits, and the **excess kilometre charge** is the price per kilometre beyond it.

## How to do it

### Building a lease payment

1. Write down $C$, $R$, $n$ and the rate (or the money factor).
2. If you have a rate, find the money factor: divide the rate in percent by 2400. If you have a money factor, multiply by 2400 to get the rate in percent.
3. Compute the depreciation charge $(C - R) \div n$.
4. Compute the rent charge $(C + R)\, m$.
5. Add them for the payment before tax.
6. Add tax. In Ontario the HST applies to each lease payment rather than all at once; the ISED notes for its lease calculator say lessees pay tax on each payment and buyers pay it up front ([ISED](https://ised-isde.canada.ca/site/vllc/en/lease-loan-calculator/tips)).
7. Check: set $R = C$ in the formula. Then the depreciation charge is 0, and the rent charge is $2Cm = C \times \text{rate} \div 12$, one month's interest on $C$. A lease with no depreciation should cost exactly the interest.

### Why 2400?

The lessor has $C$ tied up at the start and $R$ at the end, so on average about $\frac{C + R}{2}$. A year's interest at rate $i$ (as a decimal) on that average is $\frac{C + R}{2} \times \frac{i}{12}$ per month. Writing this as $(C + R)\, m$ gives $m = \frac{i}{24}$. If you write the rate in percent, $i = \frac{\text{rate}}{100}$, and so

$$
m = \frac{\text{rate in percent}}{100 \times 24} = \frac{\text{rate in percent}}{2400}.
$$

This is an approximation, because the average of $C$ and $R$ isn't exactly the average balance. The exact payment from the loan formula, with the residual as a balloon at the end, is slightly different. Example 1 shows by how much.

### What Canadian lessors quote

The money factor is a US convention. No official Canadian page I checked says how Canadian lessors quote the charge, and the FCAC page above doesn't mention a money factor, a residual value or a kilometre limit. A lessor may state a lease rate, a money factor or only a payment, so ask which. The general idea is the same in every form. Ask for the net price, the residual, the term, the kilometre allowance, the excess charge and the rate, and then check the payment with the formulas here. If you are given a money factor, multiply it by 2400 to get a rate you can compare with a loan rate.

### Comparing with buying

To compare fairly, use the same car and the same period.

1. Lease total: any amount due at signing, plus the payments with tax, plus fees, plus excess kilometre charges at the end.
2. Buy total: the down payment, plus all loan payments, minus what you sell the car for at the end of the same period.
3. Compare the two totals. The difference is the saving of one option over the other.
4. Change the unknowns (the sale price, the loan rate, the kilometres) and recompute. A table of the differences is a sensitivity table.

<div class="note" markdown>

The lease and loan rates and prices here are made up and are not current market figures. The tax treatment is as described by ISED and may differ by deal. Check the linked pages and your own contract before using any of this for a real decision.

</div>

## Worked examples

<div class="example" markdown>

### Example 1: a lease payment from scratch

Suppose a car has a net price of \$34,000, a residual value of 58% after 48 months, and a lease rate of 6% a year (made-up numbers).

Step 1: $C = 34000$, $R = 0.58 \times 34000 = 19720$, $n = 48$.

Step 2: the money factor is $6 \div 2400 = 0.0025$.

Step 3: the depreciation charge is $(34000 - 19720) \div 48 = 297.50$.

Step 4: the rent charge is $(34000 + 19720) \times 0.0025 = 134.30$.

Step 5: the payment before tax is $297.50 + 134.30 = 431.80$, so \$431.80.

Step 6: with 13% HST on the payment, the tax is \$56.13 and the payment is \$487.93.

Step 7: check. With $R = C = 34000$, the rent charge is $68000 \times 0.0025 = 170$, and one month's interest on \$34,000 at 6% is $34000 \times 0.06 \div 12 = 170$. They match.

How good is the money factor? The exact payment from the loan formula for a \$34,000 balance at 0.5% a month with a \$19,720 balloon is $\frac{(C - R(1 + r)^{-n})\, r}{1 - (1 + r)^{-n}} = 433.97$. The money factor gives \$431.80, which is \$2.17 lower. Put another way, \$431.80 is the exact payment for a rate of 5.906%, not 6%. The shortcut is close but not exact.

</div>

<div class="example" markdown>

### Example 2: how the residual changes the payment

Keep $C = 34000$, $n = 48$ and $m = 0.0025$, and change the residual:

| Residual (% of price) | Residual | Payment before tax |
|---|---|---|
| 50% | \$17,000 | \$481.67 |
| 55% | \$18,700 | \$450.50 |
| 58% | \$19,720 | \$431.80 |
| 62% | \$21,080 | \$406.87 |

A higher residual lowers the payment, because you use up less value. A lessor can make a payment look low by setting a high residual. The risk is yours if you buy the car at the end at that residual and it's worth less, and the lessor's if you return it. The contract tells you which.

Check: from 50% to 62% the residual rises by \$4,080, and the payment falls by $481.67 - 406.87 = 74.80$. The formula explains the size. The residual enters the depreciation part as $-\frac{R}{n}$ and the rent part as $+Rm$, so each extra dollar of residual changes the payment by $-\frac{1}{48} + 0.0025 = -0.018333$, and \$4,080 gives $-74.80$.

</div>

<div class="example" markdown>

### Example 3: lease against buy over four years

Use Example 1's lease. Add \$1,000 due at signing, \$600 of lease fees, and a 20,000 km a year allowance, so 80,000 km in 48 months, with an excess charge of \$0.15 a km. You expect to drive 24,000 km a year, so 96,000 km.

Lease total (assume the \$1,000 and the fees already include tax): the payment with tax is \$487.93, so the 48 payments are $487.934 \times 48 = 23420.83$. The excess is $(96000 - 80000) \times 0.15 = 2400$. The total is

$$
1000 + 23420.83 + 600 + 2400 = 27420.83.
$$

Buy: the same \$34,000 car, with 13% HST, \$1,000 down, and a 48-month loan at 7.2% (made up). The amount financed is $34000 \times 1.13 - 1000 = 37420$, the payment is \$899.54, and the loan payments total \$43,178.15. Add the \$1,000 down for \$44,178.15 paid in all. Suppose you sell the car at the end for \$19,720, the lease residual. The buy total is $44178.15 - 19720 = 24458.15$.

Buying costs \$2,962.68 less here. But the sale price is a guess. The break-even sale price is the one where buying costs the same as the lease total: $44178.15 - 27420.83 = 16757.32$. If the car sells for more than about \$16,757, buying wins; if less, the lease wins.

Check: $44178.15 - 16757.32 = 27420.83$, the lease total.

</div>

<div class="example" markdown>

### Example 4: a sensitivity table (finish it yourself)

The table shows the buy total minus the lease total (in dollars, rounded) for different loan rates and sale prices. A negative number means buying is cheaper.

| Loan rate | Sells for \$16,000 | \$18,000 | \$20,000 | \$22,000 |
|---|---|---|---|---|
| 4% | $-1865$ | $-3865$ | $-5865$ | $-7865$ |
| 6% | $-238$ | $-2238$ | $-4238$ | $-6238$ |
| 8% | $1429$ | $-571$ | $-2571$ | $-4571$ |

Step 1: read the 6% row. At what sale price does buying stop being cheaper?

Step 2: each \$2,000 more in the sale price moves the difference by \$2,000, so the columns step by 2,000 in every row. Why?

Step 3: what happens to the break-even sale price if you drive 120,000 km instead of 96,000, so the lease excess charge is $40000 \times 0.15$?

<details class="solution" markdown>
<summary>Finish</summary>

Step 1: at 6% the difference is $-238$ at \$16,000, so it reaches zero a little below \$16,000, at $16000 - 238 = 15762$. Buying stops being cheaper below about \$15,762.

Step 2: the sale price enters the buy total with a minus sign, one dollar for one dollar, so \$2,000 more makes buying \$2,000 cheaper.

Step 3: the excess charge rises from \$2,400 to \$6,000, so the lease total rises by \$3,600 and the break-even sale price falls by \$3,600, to $16757.32 - 3600 = 13157.32$ at 7.2%. (A heavily driven car would also sell for less, so the buyer's side moves too.)

Check: at 7.2% and \$16,000 the difference from Example 3 is $28178.15 - 27420.83 = 757.32$. A $16,757.32$ sale makes it zero, as in the example.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: comparing a lease payment with a loan payment. They buy different things. A lease payment on a \$34,000 car is \$487.93 with tax and the loan payment is \$899.54, but at the end of the loan you own a car worth something, and at the end of the lease you own nothing. Compare totals over the same period, with the sale value subtracted from the buy side.

</div>

<div class="warning" markdown>

Watch out: forgetting the kilometre limit. If you drive 24,000 km a year on a 20,000 km lease, Example 3 shows a \$2,400 charge, about \$50 a month on top of the payment. Ask whether extra kilometres can be bought up front, and at what price per kilometre.

</div>

<div class="warning" markdown>

Watch out: believing the money factor is a rate. It is a rate divided by 2400. A money factor of 0.0025 is a 6% rate, not 0.25%. The size check is that a monthly interest charge should be near the rate divided by 12 times the balance.

</div>

<div class="warning" markdown>

Watch out: ignoring wear-and-tear and early-termination costs. They are real money and they depend on the contract. Leaving early can be very costly, so the "cheaper" lease can end up dearer.

</div>

The answers do not come out even. Differences like \$2,962.68 are normal, and you should keep cents until the end.

## Tricks and shortcuts

A fast estimate of a lease payment: take the depreciation part, $(C - R) \div n$, and add the rate in percent divided by 2400 times $(C + R)$. The second part is roughly one month's interest on the average amount owed, so at a 6% rate it is about 0.25% of $(C + R)$ each month.

To convert a quoted money factor into a rate you can compare with a loan, multiply by 2400. A factor of 0.0021 is 5.04%.

Expected value works for the sale price. If the sale price could be \$16,000 (probability 0.3), \$19,720 (0.5) or \$22,000 (0.2), its mean is $0.3 \times 16000 + 0.5 \times 19720 + 0.2 \times 22000 = 19060$. By linearity of expectation (see [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md)), the expected buy total is $44178.15 - 19060 = 25118.15$, against \$27,420.83 for the lease. The probabilities are made up; the point is that you can put your own beliefs about the sale price into one number.

## In code

The code builds the lease payment and the buy total from Example 3.

<details class="code" markdown>
<summary>In code</summary>

```python
def lease_payment(cap, residual, n, rate_pct):
    mf = rate_pct / 2400
    return (cap - residual) / n + (cap + residual) * mf

def loan_payment(pv, r, n):
    return pv * r / (1 - (1 + r) ** -n)

cap, n = 34000, 48
residual = 0.58 * cap
pay = lease_payment(cap, residual, n, 6)
print(round(pay, 2), round(pay * 1.13, 2))      # 431.8 487.93

lease_total = 1000 + pay * 1.13 * n + 600 + max(0, 96000 - 80000) * 0.15
print(round(lease_total, 2))                    # 27420.83

loan = cap * 1.13 - 1000
pb = loan_payment(loan, 0.072 / 12, n)
for sale in (16000, 19720, 22000):
    print(sale, round(1000 + pb * n - sale, 2)) # 28178.15, 24458.15, 22178.15
print(round(1000 + pb * n - lease_total, 2))    # 16757.32
```

</details>

## FAQ

### Why does a lease payment look low?

You pay only for the value used, $C - R$, plus a charge on the money tied up. A loan payment covers the whole price. The low payment is real, but you end with no car, so compare totals, not payments.

### Does the money factor depend on the residual?

It doesn't enter the money factor directly, but the rent charge is $(C + R)\, m$, so a higher residual raises the rent charge a little while lowering the depreciation part. Net, a higher residual lowers the payment by about $\frac{1}{n} - m$ dollars per dollar of residual.

### Is leasing ever cheaper in total?

It can be, if the car sells for less than the break-even price in the buy plan, or if the loan rate is high. The sensitivity table shows both. It can also be dearer, if you drive a lot or keep the car for a long time. Long ownership favours buying because the lease payments start over each term.

### Why is the money factor not exact?

It assumes the lessor's balance falls in a straight line from $C$ to $R$ and uses the average. The true balance falls along a curve. The difference was \$2.17 a month in Example 1.

## Practice

### Warm-up

1\. A lease has $C = 30000$, $R = 17400$, $n = 36$ and a 4.8% rate. Find the money factor, the two parts of the payment and the payment.

<details class="solution" markdown>
<summary>Solution</summary>

The money factor is $4.8 \div 2400 = 0.002$. The depreciation part is $12600 \div 36 = 350$. The rent charge is $47400 \times 0.002 = 94.80$. The payment is $444.80$, that is, \$444.80.

Check: with 13% HST the payment is $444.80 \times 1.13 = 502.62$.

</details>

2\. Convert (a) a money factor of 0.0021 to a rate, and (b) a rate of 5.4% to a money factor.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $0.0021 \times 2400 = 5.04$, so 5.04%. (b) $5.4 \div 2400 = 0.00225$.

Check: $0.00225 \times 2400 = 5.4$.

</details>

3\. A lease allows 18,000 km a year for 4 years with a charge of \$0.12 per extra kilometre. You drive 85,000 km. Is there an excess charge?

<details class="solution" markdown>
<summary>Solution</summary>

The allowance is $4 \times 18000 = 72000$ km. You are 13,000 km over, so the charge is $13000 \times 0.12 = 1560$, that is, \$1,560.

Check: $72000 + 13000 = 85000$.

</details>

### Standard

4\. Use $C = 30000$, $n = 36$, a 4.8% rate. Find the payment if the residual is 50%, 58% and 60% of the price.

<details class="solution" markdown>
<summary>Solution</summary>

At 50%, $R = 15000$, and the payment is $15000 \div 36 + 45000 \times 0.002 = 416.67 + 90 = 506.67$. At 58%, $R = 17400$, and the payment is \$444.80. At 60%, $R = 18000$, and the payment is $12000 \div 36 + 48000 \times 0.002 = 333.33 + 96 = 429.33$.

Check: each extra dollar of residual lowers the payment by $\frac{1}{36} - 0.002 = 0.02578$, and \$3,000 more gives $77.33$; indeed $506.67 - 429.33 = 77.34$, equal up to rounding.

</details>

5\. For the lease in Problem 1, find the total of 36 payments with HST, and compare the money factor payment with the exact payment from the loan formula.

<details class="solution" markdown>
<summary>Solution</summary>

With tax the payment is \$502.62, so 36 payments total $502.624 \times 36 = 18094.46$. The exact payment from the loan formula with the residual as a balloon is \$446.10. That is \$1.30 more than the money factor payment of \$444.80.

Check: both numbers agree to within 0.3%, as the averaging approximation should.

</details>

6\. In Example 3, the car sells for \$19,060 (the mean of the three scenarios). Find the buy total and the saving over the lease. Then find the lease total if you drive only 80,000 km.

<details class="solution" markdown>
<summary>Solution</summary>

The buy total is $44178.15 - 19060 = 25118.15$. The saving over the \$27,420.83 lease is \$2,302.68. With only 80,000 km there is no excess charge, so the lease total falls by \$2,400 to \$25,020.83, and the lease is now \$97.32 cheaper than buying ($25118.15 - 25020.83 = 97.32$).

Check: $27420.83 - 2400 = 25020.83$.

</details>

### Challenge

7\. Show that a lease with no depreciation ($R = C$) has a payment equal to one month's interest on $C$. Then use Example 1 to say whether the money factor payment overstates or understates the cost of a true 6% rate.

<details class="solution" markdown>
<summary>Solution</summary>

With $R = C$, the depreciation part is 0 and the rent charge is $2C \times \frac{i}{24} = \frac{Ci}{12}$, where $i$ is the rate as a decimal. That is one month's interest on $C$ at the annual rate $i$, as required.

In Example 1 the exact payment at 6% is \$433.97 and the money factor gives \$431.80. The money factor payment equals the exact payment at 5.906%, a slightly lower rate, so it understates the cost by about \$2.17 a month.

Check: $433.97 - 431.80 = 2.17$.

</details>

8\. (Reviews [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md).) With the sale price scenarios in the Tricks section, find the variance of the sale price, and say what it measures for the buyer.

<details class="solution" markdown>
<summary>Solution</summary>

The mean is $19060$. The squared deviations are $(16000 - 19060)^2 = 9363600$, $(19720 - 19060)^2 = 435600$ and $(22000 - 19060)^2 = 8643600$. The variance is $0.3 \times 9363600 + 0.5 \times 435600 + 0.2 \times 8643600 = 4755600$ dollars squared. The standard deviation is about \$2,181.

For the buyer this is the spread of the cost. The lessor sets the residual, so the lease total has no such spread (apart from kilometres and wear), and the buyer carries the sale-price risk.

Check: $0.3 + 0.5 + 0.2 = 1$, and $E[X^2] - 19060^2$ gives the same variance.

</details>

## Where this shows up

- The next lesson, [credit cards and the minimum payment trap](04-credit-cards-and-the-minimum-payment-trap.md), is about the most expensive kind of borrowing.
- In economics, a lease is a rental price for a durable good, and a buyer's choice is an asset price against a rental price, as in [renting vs buying a home](../05-housing/01-renting-vs-buying-a-home.md).
- In CS, the sensitivity table is the same idea as a parameter sweep: fix everything, vary one input, record the output.
