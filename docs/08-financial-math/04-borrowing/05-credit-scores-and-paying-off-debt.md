# Credit scores and paying off debt

After this lesson you can describe what goes into a credit score, compute credit utilization, compare the avalanche and snowball ways of paying off several debts, explain why the avalanche minimizes interest, and judge a consolidation loan by its rate.

Before this: [credit cards and the minimum payment trap](04-credit-cards-and-the-minimum-payment-trap.md), [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md) and [direct proof](../../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A card has a \$5,000 limit and a \$3,500 balance. What is its utilization?
2. You owe \$900 at 18% and \$3,500 at 24%. What is the average rate on the combined \$4,400, weighting each rate by its balance?
3. You have \$100 extra this month. The card at 24% or the one at 18%: which one saves more interest, and by how much in one month?

<details class="solution" markdown>
<summary>Answers</summary>

1. Utilization is the balance divided by the limit: $3500 \div 5000 = 0.70$, that is, 70%.
2. The yearly interest is $900 \times 0.18 + 3500 \times 0.24 = 162 + 840 = 1002$, and $1002 \div 4400 = 0.2277$, so about 22.8%.
3. Each dollar paid to the 24% card saves 2% a month and each dollar paid to the 18% card saves 1.5%, so \$100 saves \$2.00 against \$1.50, which is 50 cents more in the first month.

</details>

## The idea

Two questions come up once you owe money in several places. The first is how a lender decides whether to trust you with more: the answer is a credit score, a number built from your borrowing history. The second is what to pay first when you have several debts and not enough money to clear them all.

On the second question there are two well-known orders. The snowball method pays the smallest balance first, for the quick win of closing an account. The avalanche method pays the highest interest rate first. This lesson compares them on a made-up set of debts, shows with an exchange argument why the avalanche costs the least interest, and then looks at consolidation, which swaps several debts for one loan at a new rate.

The math says which order costs less interest. It doesn't say which order you will actually stick to, and that matters too. All balances and rates here are made up.

## Definitions

A **credit report** is a record of your borrowing history, and a **credit score** is a number computed from it. The Financial Consumer Agency of Canada (FCAC) says scores are "usually" 300 to 900, higher is better, and that "credit bureaus and lenders use different formulas to calculate your score, but they don't share the exact details" ([FCAC](https://www.canada.ca/en/financial-consumer-agency/services/credit-reports-score/credit-report-score-basics.html)).

The same page groups the factors that commonly influence the score into two kinds. Credit history: how long you've had credit, the kinds of credit you hold, whether debts went to a collection agency, and any insolvency or bankruptcy filings. Credit habits: whether you carry a balance on your credit cards, missed payments, the total debt you owe, how close you are to your credit limit, and how often you apply for new credit. The page does not give weights for these, and this lesson doesn't either.

The **credit utilization** of a card is its balance divided by its credit limit. For several cards, the combined utilization is the total of the balances divided by the total of the limits. In plain words: the share of your available credit that you are using. "How close you are to your credit limit" is on the FCAC list; the page gives no cutoff, and whether a bureau looks at each card or the total is part of the undisclosed formula.

A **payoff strategy** is a rule that says where to send the money each month. In the **snowball method** the extra money goes to the debt with the smallest balance. In the **avalanche method** it goes to the debt with the highest interest rate. In both, you keep paying the required minimum on every debt, and the extra goes to the one the rule picks. When a debt is paid off, its minimum payment joins the extra.

**Debt consolidation** replaces several debts with one new loan, usually used to pay them off. What changes is the interest rate, the term, and the payment, and sometimes there are fees.

## How to do it

### Utilization

1. Add up the balances.
2. Add up the limits.
3. Divide the first by the second, and write it as a percent.

For each card, do the same with that card's balance and limit. Paying a balance down, or having a higher limit with the same balance, lowers the ratio.

### Comparing two strategies

1. List each debt with its balance, annual rate and minimum payment.
2. Fix the total monthly budget (the minimums plus the extra).
3. Each month: add interest ($\text{balance} \times \text{annual rate} \div 12$) to each debt, pay every minimum, then send all the remaining budget to the debt the strategy picks (smallest balance or highest rate). Cap each payment at the balance owed.
4. Repeat until every balance is zero. Count the months and add up the interest.
5. Compare the two totals. They use the same budget, so a lower total interest means a better plan in dollars.

### Consolidation as a rate comparison

1. Find your current blended rate: sum of balance times rate, divided by the total balance.
2. Compare it with the new loan's rate, and add any fee to the new loan's balance.
3. Keep the monthly payment the same in both plans, so the comparison is about interest, not about a lower payment.
4. Compute the total interest for the current plan (for example with the avalanche) and for the new loan, using $n = -\ln(1 - Br/P) \div \ln(1 + r)$ for the loan.
5. The break-even rate is the new-loan rate at which the two totals are equal. A lower rate wins.

<div class="note" markdown>

The FCAC credit score factors are from a page that describes the common factors, not a formula, and may be updated. Check the linked page. The balances, rates and loan offers in this lesson are made up.

</div>

## Worked examples

<div class="example" markdown>

### Example 1: avalanche against snowball

Suppose you owe three debts, with the monthly minimum and annual rate shown (all made up), and a budget of \$450 a month in all.

| Debt | Balance | Rate | Minimum |
|---|---|---|---|
| Store card | \$900 | 18% | \$25 |
| Credit card | \$3,500 | 24% | \$105 |
| Line of credit | \$6,000 | 9% | \$120 |

The minimums add to \$250, so \$200 a month is extra.

Step 1: list the debts, as above.

Step 2: the budget is \$450.

Step 3 and 4: run the monthly update. The snowball sends the extra \$200 first to the store card (the smallest balance), then to the credit card, then to the line of credit. The avalanche sends it first to the credit card (24%), then the store card (18%), then the line of credit (9%).

Step 5: the results.

| Method | Months to be debt-free | Total interest | Order of payoff (month) |
|---|---|---|---|
| Snowball | 27 | \$1,608.39 | store card 5, credit card 16, line of credit 27 |
| Avalanche | 27 | \$1,547.45 | credit card 14, store card 16, line of credit 27 |

Both finish in 27 months. The avalanche pays \$60.94 less interest. The snowball closes an account in month 5, the avalanche not until month 14. Paying only the minimums, with no extra, would cost \$4,277.64 in interest, and the last debt would take 63 months. (That figure assumes each minimum stays fixed instead of shrinking.)

Check: both plans pay \$450 a month until the last month, so 26 full payments make \$11,700. The balance plus interest is $10400 + 1547.45 = 11947.45$ for the avalanche, so its last payment is \$247.45. For the snowball it is $10400 + 1608.39 - 11700 = 308.39$. The avalanche pays less in total because the dollars sit on the 24% debt first.

</div>

<div class="example" markdown>

### Example 2: utilization

Suppose the store card has a \$1,500 limit and the credit card a \$5,000 limit (made up).

Store card: $900 \div 1500 = 0.60$, that is, 60%. Credit card: $3500 \div 5000 = 0.70$, that is, 70%. Combined: $(900 + 3500) \div (1500 + 5000) = 4400 \div 6500 = 0.677$, that is, 67.7%.

If you pay the credit card down to \$1,500, the combined ratio is $(900 + 1500) \div 6500 = 0.369$, about 36.9%. If instead the card's limit rose to \$6,500 and the balance stayed at \$3,500, the card would be at $3500 \div 6500 = 53.8\%$.

Check: the combined ratio lies between the two single ratios (60% and 70%), weighted toward the card with the larger limit. That is $0.677$.

</div>

<div class="example" markdown>

### Example 3: consolidation as a rate comparison

The three debts total \$10,400, and their blended rate is $\frac{900 \times 0.18 + 3500 \times 0.24 + 6000 \times 0.09}{10400} = 0.1483$, about 14.8%. Suppose a bank offers a consolidation loan on all \$10,400 at 11% (made up), and you keep paying \$450 a month.

At 11%, $r = 0.11 \div 12 = 0.009167$, and $n = -\ln(1 - 10400 \times 0.009167 / 450) \div \ln(1.009167) = 26.6$, so 27 payments and \$1,340.69 of interest. That is \$206.76 less than the avalanche's \$1,547.45.

The break-even rate (found by trial) is 12.41%: a consolidation loan above that rate costs more than the avalanche at this payment. Fees matter: if the loan charged a 3% fee (\$312) added to the balance, the interest would be \$1,427.85. At 14% the interest would be \$1,790.05, at 18% \$2,466.38.

There is a catch. The line of credit is at 9%, which is below 11%. Consolidating only the store card and the credit card (\$4,400) into an 11% loan, and keeping the line of credit, gives a plan with 26 months and \$1,131.16 of interest, better than moving everything. Consolidating a cheap debt into a dearer loan raises its rate.

Check: the total paid is the balance plus interest, $10400 + 1340.69 = 11740.69$. Twenty-six payments of \$450 make \$11,700, so the 27th payment is \$40.69, a small last one.

</div>

<div class="example" markdown>

### Example 4: where the avalanche matters (finish it yourself)

Two debts: \$1,000 at 8% with a \$25 minimum, and \$3,000 at 22% with a \$50 minimum. The budget is \$300 a month. The snowball pays the \$1,000 debt first, and the avalanche pays the \$3,000 debt first.

Step 1: the extra is $300 - 75 = 225$ a month.

Step 2: the snowball puts the \$225 on the small, cheap debt, while the avalanche puts it on the large, expensive one.

Find the months and total interest for each, and the saving.

<details class="solution" markdown>
<summary>Finish</summary>

Running the monthly update: the snowball takes 16 months and costs \$590.99 in interest. The avalanche takes 15 months and costs \$460.57. The saving is \$130.42, and one month sooner. When the high-rate debt is the bigger one, the order matters more than in Example 1.

Check: at the start, \$225 on the 22% debt saves $225 \times 0.22 \div 12 = 4.13$ a month in interest, against $225 \times 0.08 \div 12 = 1.50$ on the 8% debt, a gap of \$2.63 in the first month alone.

</details>

</div>

## An exchange argument

The avalanche claim is a theorem, and the proof is an exchange argument: take any plan that does not follow the avalanche, swap a dollar to follow it, and show the swap saves money.

Claim: Fix a monthly budget that is paid in full each month, and fix the minimum payments. Among all ways of splitting the extra money across debts, the avalanche has the lowest total interest. (This is a sketch: it ignores the months when a balance reaches zero partway through and the leftover moves on, and any dollar floors.)

Know: Debt $i$ has monthly rate $r_i$, and debt $j$ has monthly rate $r_j$ with $r_i > r_j$. In some month $t$, a plan pays an extra amount $x > 0$ to debt $j$, while debt $i$ still has a balance of at least $x$ left after that month's payments.

Want: A plan with less total interest, that uses the same budget.

Plan: Move the amount $x$ from debt $j$ to debt $i$ in month $t$ and keep every other payment the same. Compare the balances afterwards.

Proof: After the swap, debt $i$'s balance at the end of month $t$ is lower by $x$ and debt $j$'s is higher by $x$. Both debts then grow at their own rates, with unchanged payments. After $s$ more months, the change in the combined balance is

$$
-x(1 + r_i)^s + x(1 + r_j)^s = -x\left[(1 + r_i)^s - (1 + r_j)^s\right].
$$

Since $r_i > r_j$ and $s \ge 1$, the bracket is positive, so the combined balance is lower after the swap, and the gap grows with $s$. With the same budget and a lower balance, the plan reaches zero no later, and what you pay beyond the principal, the interest, is lower. So any plan that pays extra to a lower-rate debt while a higher-rate debt is still open can be improved. The plans that cannot be improved are those that always put the extra on the highest-rate open debt, which are the avalanche. $\blacksquare$

Look back: The proof used only that one dollar owed at a higher rate grows faster than one dollar owed at a lower rate. Numerically, in Example 1's first month, moving \$100 from the store card (18%) to the credit card (24%) leaves \$7.26 less owed after 12 months: $100(1.02^{12} - 1.015^{12}) = 7.26$. Nothing in the proof depends on balance sizes, which is why the snowball, which looks at balance, can lose. It also explains why the saving in Example 1 is small: the rates differ by only a few points on a modest balance.

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: ignoring the minimums on the other debts. Missed payments are on the FCAC list of things that influence a score, and cost fees. Both strategies pay every minimum first.

</div>

<div class="warning" markdown>

Watch out: forgetting to roll a paid-off debt's payment into the extra. In Example 1 the plan stays at \$450 a month. If you drop to the remaining minimums when a debt closes, the payoff takes much longer.

</div>

<div class="warning" markdown>

Watch out: using a consolidation loan and then spending on the cleared card. The debts you cleared are still there as available credit. If the balances grow again, you owe the new loan plus new card debt.

</div>

<div class="warning" markdown>

Watch out: comparing the new payment instead of the new rate and term. A consolidation loan with a lower payment and a longer term can cost more in total interest. Compare at the same monthly payment, as in Example 3.

</div>

Ties and untidy results are normal. When two debts have the same rate, either order gives the same interest. Months are whole numbers, but the last payment is smaller.

## Tricks and shortcuts

A fast check on which debt gets the extra: compare rates. Each \$100 on a 24% debt saves \$2.00 in the next month and on an 18% debt \$1.50. You can do this without a spreadsheet.

A quick blended rate is a weighted average: multiply each balance by its rate, add, and divide by the total balance. The simple average of the rates is wrong when the balances differ. For 18%, 24% and 9% it would be 17%, against the true 14.8%.

## In code

The function runs either strategy and reports months and total interest, and a bisection search finds the break-even consolidation rate.

<details class="code" markdown>
<summary>In code</summary>

```python
debts = [("Store card", 900, 0.18, 25),
         ("Credit card", 3500, 0.24, 105),
         ("Line of credit", 6000, 0.09, 120)]

def payoff(debts, budget, order):
    bal = {n: b for n, b, r, m in debts}
    rate = {n: r / 12 for n, b, r, m in debts}
    mini = {n: m for n, b, r, m in debts}
    months, interest, done = 0, 0.0, {}
    while any(v > 0.005 for v in bal.values()):
        months += 1
        for n in bal:
            if bal[n] > 0:
                i = bal[n] * rate[n]
                bal[n] += i
                interest += i
        avail = budget
        for n in bal:
            pay = min(mini[n], bal[n])
            bal[n] -= pay
            avail -= pay
        for n in sorted((n for n in bal if bal[n] > 0.005), key=order):
            pay = min(avail, bal[n])
            bal[n] -= pay
            avail -= pay
        for n in bal:
            if bal[n] <= 0.005 and n not in done:
                done[n] = months
    return months, round(interest, 2), done

info = {n: (b, r) for n, b, r, m in debts}
snow = payoff(debts, 450, lambda n: info[n][0])    # smallest balance first
aval = payoff(debts, 450, lambda n: -info[n][1])   # highest rate first
print(snow)  # (27, 1608.39, {'Store card': 5, 'Credit card': 16, 'Line of credit': 27})
print(aval)  # (27, 1547.45, {'Credit card': 14, 'Store card': 16, 'Line of credit': 27})
print(round(snow[1] - aval[1], 2))                 # 60.94

def loan_interest(pv, apr, pay):
    r, b, tot = apr / 12, pv, 0.0
    while b > 0.005:
        i = b * r
        tot += i
        b += i - min(pay, b + i)
    return tot

lo, hi = 0.0, 0.3
for _ in range(60):
    mid = (lo + hi) / 2
    if loan_interest(10400, mid, 450) > aval[1]:
        hi = mid
    else:
        lo = mid
print(round(lo * 100, 2))                          # 12.41
```

</details>

## FAQ

### Is the avalanche always the best choice?

It always has the lowest interest for a fixed budget, by the exchange argument. It isn't always the one a person follows: the snowball closes accounts sooner. The cost of choosing the snowball in Example 1 is \$60.94 over 27 months. That is the price tag, and the decision is yours.

### Is there a utilization number I should stay under?

The FCAC page doesn't give one. Lenders and websites quote rules of thumb, but the bureaus keep their formulas private, so treat any specific cutoff as unverified.

### Why is consolidating not always a good idea?

Because the question is the rate and the fees. Example 3 shows that moving a 9% debt into an 11% loan makes that part dearer, and that a fee can erase the saving.

## Practice

### Warm-up

1\. A card has a \$2,000 limit and a \$700 balance. A second has a \$4,500 limit and a \$2,300 balance. Find each card's utilization and the combined utilization.

<details class="solution" markdown>
<summary>Solution</summary>

First card: $700 \div 2000 = 0.35$, that is, 35%. Second card: $2300 \div 4500 = 0.511$, that is, 51.1%. Combined: $(700 + 2300) \div (2000 + 4500) = 3000 \div 6500 = 0.4615$, that is, 46.2%.

Check: 46.2% lies between 35% and 51.1%, closer to the second because its limit is larger.

</details>

2\. You owe \$1,000 at 20% and \$3,000 at 10%. Find the blended rate.

<details class="solution" markdown>
<summary>Solution</summary>

The yearly interest is $1000 \times 0.20 + 3000 \times 0.10 = 500$, and $500 \div 4000 = 0.125$, so 12.5%.

Check: the simple average of 20% and 10% is 15%, too high, because most of the money is at 10%.

</details>

3\. List the factors that the FCAC page says influence a credit score, in your own words, and say which two relate to this lesson's utilization.

<details class="solution" markdown>
<summary>Solution</summary>

Credit history: how long you've had credit, the kinds of credit, collections, and insolvency or bankruptcy. Credit habits: carrying a card balance, missed payments, total debt owed, how close you are to your limits, and how often you apply for new credit. Utilization relates to "how close you are to your credit limit" and to "if you carry a balance".

Check: the FCAC page gives no weights, so the answer shouldn't rank them.

</details>

### Standard

4\. Debts: \$1,000 at 8% (minimum \$25) and \$3,000 at 22% (minimum \$50), with a \$300 budget. Report months and total interest for the snowball and the avalanche.

<details class="solution" markdown>
<summary>Solution</summary>

Snowball: 16 months and \$590.99. Avalanche: 15 months and \$460.57. The avalanche saves \$130.42.

Check: the avalanche sends the extra \$225 to the 22% debt, which saves about \$2.63 more than the snowball in the first month, and the gap compounds.

</details>

5\. A bank offers a loan at 12% to pay the \$10,400 in Example 1, and you keep paying \$450 a month. Is it better than the avalanche? What if there is a 3% fee added to the loan?

<details class="solution" markdown>
<summary>Solution</summary>

Run the payoff loop for the loan at \$450 a month. At 12% it takes 27 months and costs \$1,485.97 in interest, which is \$61.48 less than the avalanche's \$1,547.45. With a 3% fee added, the balance is $10400 \times 1.03 = 10712$, and the loan takes 28 months and costs \$1,583.58, which is \$36.13 more than the avalanche. The fee turns a saving into a loss.

Check: 12% is below the break-even rate of 12.41%, so the plain loan should win, and the fee raises the balance enough to push the cost above the avalanche.

</details>

6\. A card with a \$5,000 limit has a balance of \$3,500. By how many percentage points does utilization fall if you pay \$1,000? If instead the limit rises to \$6,500?

<details class="solution" markdown>
<summary>Solution</summary>

Now: 70%. After paying \$1,000: $2500 \div 5000 = 50\%$, which is 20 percentage points lower. With the limit at \$6,500: $3500 \div 6500 = 53.8\%$, which is 16.2 percentage points lower.

Check: paying down the balance changes the top of the fraction, the limit changes the bottom, and both lower the ratio.

</details>

### Challenge

7\. In the exchange argument, show that the combined balance is lower by $x\left[(1 + r_i)^s - (1 + r_j)^s\right]$ after $s$ months. Then evaluate it for $x = 100$, $r_i = 0.02$, $r_j = 0.015$ and $s = 12$.

<details class="solution" markdown>
<summary>Solution</summary>

Debt $i$ owes $x$ less at the end of month $t$. With unchanged later payments, an amount owed grows by the factor $(1 + r_i)$ each month, so after $s$ months the difference is $x(1 + r_i)^s$ less. Debt $j$ owes $x$ more, which grows to $x(1 + r_j)^s$ more. The net change in the combined balance is $-x(1 + r_i)^s + x(1 + r_j)^s$, which is the stated expression with a minus sign in front.

With the numbers, $100 \times (1.02^{12} - 1.015^{12}) = 100 \times (1.26824 - 1.19562) = 7.26$, so \$7.26 less is owed after 12 months.

Check: $1.02^{12} = 1.26824$ and $1.015^{12} = 1.19562$, and their gap is positive because $0.02 > 0.015$.

</details>

8\. (Reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).) A card's limit rises from \$5,000 to \$6,500. By what percent did the limit rise? If the balance stays at \$3,500, utilization drops from 70% to 53.8%; by what percent did utilization fall?

<details class="solution" markdown>
<summary>Solution</summary>

The limit rose by $1500 \div 5000 = 0.30$, that is, 30%. Utilization fell from 70% to 53.8%, a drop of 16.2 percentage points, which is $16.15 \div 70 = 0.2308$, about 23.1% of the old utilization.

Check: the new ratio is the old one divided by 1.3, and $70 \div 1.3 = 53.8$.

</details>

## Where this shows up

- The next chapter, on housing, brings in the biggest loan most people take; your credit and your debts affect how much a lender will offer. See [mortgage basics](../05-housing/02-mortgage-basics.md).
- In algorithms, the avalanche is a greedy rule, and an exchange argument is a standard way to prove that a greedy choice is correct.
- In economics, comparing debts by rate is a small case of equalizing marginal returns across uses of money.
