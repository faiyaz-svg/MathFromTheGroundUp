# Renting vs buying a home

After this lesson you can list the costs of renting and of owning a home, compute the Ontario land transfer tax bracket by bracket, and compare renting with buying over ten years by tracking what each choice leaves you with.

Before this: [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md), [compound interest](../02-interest-and-growth/02-compound-interest.md) and [the loan amortization formula](../03-time-value-of-money/03-loan-amortization-formula.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Ontario land transfer tax is 0.5% on the first \$55,000 of a price, 1.0% on the next \$195,000 (up to \$250,000), 1.5% on the next \$150,000 (up to \$400,000) and 2.0% above \$400,000. Find the tax on a \$480,000 home.
2. A rule of thumb says the yearly cost of owning that you never get back is about 5% of the price. What is that per month for a \$600,000 home?
3. A \$500,000 home gains 3% a year for 10 years, and selling costs 5% of the sale price. How much do you receive, before paying off any mortgage?

<details class="solution" markdown>
<summary>Answers</summary>

1. The brackets give $0.005 \times 55000 + 0.01 \times 195000 + 0.015 \times 150000 + 0.02 \times 80000 = 275 + 1950 + 2250 + 1600 = 6075$, so \$6,075.
2. Yearly: $0.05 \times 600000 = 30000$. Monthly: $30000 \div 12 = 2500$, so \$2,500.
3. The value is $500000 \times 1.03^{10} = 671958.19\ldots$. Selling costs take 5%, so you keep 95%: $0.95 \times 671958.19 = 638360.28$, about \$638,360.

</details>

## The idea

Suppose you pay \$2,800 a month in rent for a two-bedroom condo, and a similar one is for sale at \$700,000. The owner's monthly bill looks bigger, but part of what an owner pays turns into something they keep: the part of each mortgage payment that pays down the loan is not spent, it is stored as ownership. So "rent is money thrown away" and "a mortgage payment is an investment" are both half true. The honest comparison asks where you stand after some number of years under each choice.

Three ideas make that comparison fair. First, some of the owner's costs are gone for good, like interest, property tax and repairs, and these are the ones to compare with rent. Second, money tied up in a down payment could have been invested elsewhere, which is a cost even though no bill arrives. Third, buying and selling a home costs thousands of dollars in fees and taxes, so owning for a short time is expensive.

This lesson builds a simple model of the comparison and runs it in code. The model uses made-up numbers, because the future price of a home, the return on investments and the growth of rent are all unknown. The model's value is in showing which assumptions the answer depends on. It is not financial advice, and it does not tell you what to do.

## Definitions

The **unrecoverable costs** of a choice are the money you spend on it that you do not get back. For a renter, unrecoverable costs are the rent and the renter's insurance. For an owner, they are mortgage interest, property tax, maintenance, home insurance and the fees paid to buy and sell.

In plain words: the principal part of a mortgage payment is not unrecoverable, because it reduces what you owe. Interest is, because it is the price of borrowing.

The **opportunity cost** of a choice is the value of the best alternative you give up by making it (see [opportunity cost](../../07-economics-math/02-markets/01-opportunity-cost-and-the-ppc.md)). A \$140,000 down payment that earns nothing in a house could have earned an investment return somewhere else, so that return is a cost of buying.

**Equity** is the market value of a home minus what is still owed on it. If a home is worth \$700,000 and the mortgage balance is \$560,000, the equity is \$140,000.

**Closing costs** are the one-time expenses of completing a purchase, such as land transfer tax, legal fees and a title search. They are paid on the closing date, when ownership passes to the buyer.

The **land transfer tax** is a tax on the price of a property, paid by the buyer when the purchase closes. Ontario's tax is graduated: each bracket of the price is taxed at its own rate, in the same way that income tax brackets work.

The **price-to-rent ratio** of a home is its price divided by the yearly rent for a comparable home:

$$
\text{price-to-rent ratio} = \frac{\text{price}}{12 \times \text{monthly rent}}.
$$

In plain words, it is the number of years of rent that would add up to the price. A \$700,000 home that rents for \$2,800 a month has a ratio of $700000 \div 33600 \approx 20.8$.

## How to do it

### What each side costs

A renter pays rent, and renter's insurance (a policy that covers your belongings and your liability). Rent changes over time, and the model just assumes a growth rate, such as 3% a year.

An owner pays more kinds of costs. This table lists them, with the made-up amounts used in this lesson for a \$700,000 home with a 20% down payment.

| Cost | What it is | Made-up amount |
|---|---|---|
| Mortgage interest | the price of the loan, the biggest cost early on | \$27,451 in year 1 |
| Property tax | charged each year by the municipality, as a percent of assessed value | 0.8% of value a year, \$5,600 |
| Maintenance | repairs and upkeep, such as a roof or a furnace | 1% of value a year, \$7,000 |
| Home insurance | covers damage and liability | \$1,500 a year |
| Opportunity cost | the return you give up on the down payment and closing costs | 5% a year of \$152,475, \$7,624 |

The mortgage interest comes from the schedule in [mortgage amortization schedules](03-mortgage-amortization-schedules.md): a \$560,000 mortgage at a quoted 5% (an example rate, not a market rate), amortized over 25 years. The property tax and maintenance rates are round assumptions. Real property tax rates differ by city, so look up your municipality's rate when you need it.

Condo owners also pay monthly condo fees, which are not in this table.

### Closing costs and the land transfer tax

Buyers of Ontario property pay the provincial land transfer tax. For 2026 the Ontario government lists these rates for a purchase price ([Ontario: calculating land transfer tax](https://www.ontario.ca/document/land-transfer-tax/calculating-land-transfer-tax)):

| Part of the price | Rate |
|---|---|
| up to \$55,000 | 0.5% |
| \$55,000 to \$250,000 | 1.0% |
| \$250,000 to \$400,000 | 1.5% |
| over \$400,000 | 2.0% |
| over \$2,000,000, for one or two single-family residences | 2.5% |

First-time buyers can get a refund of up to \$4,000, and there is no tax at all on the first \$368,000 of an eligible home ([Ontario: first-time homebuyer refund](https://www.ontario.ca/document/land-transfer-tax/land-transfer-tax-refunds-first-time-homebuyers)). The refund has conditions about who qualifies and when to apply, so read that page before counting on it.

The City of Toronto charges its own municipal land transfer tax on top of the provincial one. This lesson does not compute it; the rates are on the [City of Toronto's page](https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/).

<div class="note" markdown>

These figures are for 2026 and change from time to time. Check the linked pages before using them for real decisions.

</div>

Here are the steps for the tax:

1. For each bracket that the price reaches, find the part of the price inside it: the lesser of the price and the bracket's top, minus the bracket's bottom.
2. Multiply each part by that bracket's rate.
3. Add the results. Brackets above the price contribute nothing.
4. For a first-time buyer, subtract the refund: the smaller of the tax and \$4,000 (the tax on the first \$368,000 is \$3,995, so a home at that price or less has no net tax).
5. Check by a rough estimate: the tax is between 0.5% and 2% of the price.

Legal fees and other costs add to this. This lesson uses \$2,000 for them, a made-up figure.

### Comparing ten years of each choice

The model tracks one number for each choice: the amount of wealth you hold after 10 years. Both people have the same monthly budget and the same starting savings.

1. The renter starts by investing the down payment and the closing costs, \$140,000 plus \$12,475 (land transfer tax of \$10,475 and \$2,000 of legal fees, with no first-time refund).
2. Each month, compare the owner's cost (mortgage payment, a twelfth of the property tax, maintenance and insurance) with the renter's cost (rent and a twelfth of the renter's insurance). The person with the smaller cost invests the difference, so both people spend the same amount in total.
3. Property tax and maintenance are a fixed percent of the home's value, which grows each year. Rent grows each year too.
4. After 120 months, the owner's wealth is the sale price, minus the selling costs, minus the mortgage balance, plus any investments. The renter's wealth is their investment account.
5. Subtract: buying minus renting. A positive number favours buying under those assumptions.

The assumptions in this lesson are made up: a home price growth of 3% a year, an investment return of 5% a year, rent growth of 3% a year, selling costs of 5% of the sale price, and a mortgage at a quoted 5% for all 10 years. The figures are round examples. Nobody knows the next 10 years of any of them.

### Two rules of thumb

Two quick checks are often used before the full model. Both are rough, and neither is a law.

The 5% rule says that the unrecoverable cost of owning is about 5% of the home's price per year. The usual breakdown is about 1% for property tax, 1% for maintenance and 3% for the cost of capital (mortgage interest plus the return given up on the down payment). If the rent you pay is less than $\frac{5\%}{12}$ of the price each month, the rule says renting costs less; if it is more, buying costs less. The 3% in that breakdown depends on interest rates. With the 5% rate used here, the cost of capital is closer to 5%, and the rule would become a 7% rule.

The price-to-rent ratio is a second check. A high ratio means the home is expensive compared with renting one. A common rule of thumb says a ratio above 20 favours renting and one below 15 favours buying. These cut-offs are conventions from personal finance writing, not facts, and they move with interest rates.

## Worked examples

<div class="example" markdown>

### Example 1: land transfer tax on a \$700,000 home

A first-time buyer in Ontario buys a \$700,000 home. Find the land transfer tax, and the amount after the first-time refund.

Step 1: split the price into the parts inside each bracket.

| Bracket | Part of the price inside it |
|---|---|
| first \$55,000 | \$55,000 |
| \$55,000 to \$250,000 | $250000 - 55000 = 195000$ |
| \$250,000 to \$400,000 | $400000 - 250000 = 150000$ |
| over \$400,000 | $700000 - 400000 = 300000$ |

The parts add to \$700,000, which is a check that nothing was missed or counted twice.

Step 2: multiply each part by its rate:

$$
\begin{aligned}
0.005 \times 55000 &= 275, \\
0.010 \times 195000 &= 1950, \\
0.015 \times 150000 &= 2250, \\
0.020 \times 300000 &= 6000.
\end{aligned}
$$

Step 3: add them: $275 + 1950 + 2250 + 6000 = 10475$. The tax is \$10,475.

Step 4: the first-time refund is the smaller of the tax and \$4,000, which is \$4,000. The net tax is $10475 - 4000 = 6475$, so \$6,475.

Step 5: check against the estimate. The tax is $10475 \div 700000 = 0.01496$, about 1.5% of the price, between 0.5% and 2%. The top bracket pays 2%, and the lower brackets pay less, so a blended rate under 2% makes sense.

Watch out: the 2% does not apply to the whole price. Charging 2% on all \$700,000 would give \$14,000, which is \$3,525 too much.

</div>

<div class="example" markdown>

### Example 2: the first year of costs, side by side

Using the made-up numbers above, compare the unrecoverable costs of owning the \$700,000 home with renting a similar one for \$2,800 a month plus \$300 a year of renter's insurance.

Owner, in year 1: interest \$27,451.22 (from the schedule), property tax \$5,600, maintenance \$7,000, insurance \$1,500. These add to \$41,551.22. The opportunity cost of the \$152,475 down payment and closing costs at 5% is $0.05 \times 152475 = 7623.75$. The total is \$49,174.97.

Renter, in year 1: $12 \times 2800 + 300 = 33900$.

On unrecoverable costs alone, owning costs \$15,274.97 more in year 1. But a home that gains 3% in a year gains $0.03 \times 700000 = 21000$ in value. Subtracting that, the owner's net cost is $49174.97 - 21000 = 28174.97$, which is less than the renter's \$33,900.

So the first-year answer depends on the 3% guess. At 1% growth the gain is only \$7,000 and renting is cheaper. Check: the three amounts add as described, and $41551.22 + 7623.75 = 49174.97$.

</div>

<div class="example" markdown>

### Example 3: the two rules of thumb

The same home costs \$700,000 and rents for \$2,800 a month. What do the 5% rule and the price-to-rent ratio say?

For the 5% rule, the yearly unrecoverable cost is $0.05 \times 700000 = 35000$, or $35000 \div 12 = 2916.67$ a month. The rent of \$2,800 is below that, so the rule leans toward renting, but only by about \$117 a month, so it is close.

The price-to-rent ratio is $700000 \div (12 \times 2800) = 700000 \div 33600 = 20.83$. That is just over the usual cut-off of 20, so this rule also leans slightly toward renting.

Both rules lean the same way here, and both say "close". The model in the next section shows how close: the result flips with small changes in the assumptions.

Check: $2916.67 \times 12 = 35000$ and $20.83 \times 33600 = 699888$, which rounds to the price.

</div>

<div class="example" markdown>

### Example 4: tax on a \$520,000 home (finish it yourself)

A first-time buyer buys a \$520,000 home. Brackets 1 to 3 give \$275, \$1,950 and \$2,250. Find the tax in the top bracket, the total, and the net tax after the refund.

Step 1: the part of the price over \$400,000 is $520000 - 400000 = 120000$.

Now find the tax on that part, add all four amounts and subtract the refund.

<details class="solution" markdown>
<summary>Finish</summary>

The top bracket's tax is $0.02 \times 120000 = 2400$. The total is $275 + 1950 + 2250 + 2400 = 6875$, so \$6,875. The refund is the smaller of \$6,875 and \$4,000, which is \$4,000, so the net tax is \$2,875.

Check: $6875 \div 520000 \approx 1.32\%$, between 0.5% and 2%.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: rent is not the only thing to compare with the mortgage payment. A payment of \$3,257 is for the mortgage only. Add property tax, maintenance and insurance, and the owner's monthly cost in the first month becomes \$4,431.99. Comparing \$3,257 with \$2,800 leaves out \$1,175 of costs.

</div>

<div class="warning" markdown>

Watch out: counting the whole mortgage payment as a cost. Only the interest is spent. In year 1, \$11,632.64 of the payments goes to principal and is part of the owner's equity. The error runs the other way too: ignoring the principal and counting only interest makes buying look better when the down payment could have earned something.

</div>

<div class="warning" markdown>

Watch out: forgetting the cost of selling. If you sell a \$940,741 home, selling costs of 5% take about \$47,037. A model that ignores that overstates the owner's wealth by a similar amount, and the effect is largest for short stays.

</div>

A home price that rises is not guaranteed. Prices have fallen in some years and in some cities, and the table below shows the case of 0% growth. A negative growth rate is allowed in the model too.

If the owner's monthly cost is less than the rent, the owner invests the difference rather than the renter. The code in this lesson handles both cases by letting whichever side spends less invest the difference.

## Tricks and shortcuts

To estimate the land transfer tax in your head for a price over \$400,000, start from the tax at \$400,000, which is \$4,475, and add 2% of the amount over \$400,000. For \$520,000 that is $4475 + 2400 = 6875$.

To convert a price to a rule-of-thumb monthly cost, multiply by 5% and divide by 12, which is the same as multiplying by about $0.0042$. A \$480,000 home gives about \$2,000 a month.

## In code

The model fits in one function. It tracks the two investment accounts month by month, so you can change an assumption and see what happens.

<details class="code" markdown>
<summary>In code</summary>

```python
def ltt(price):
    """Ontario land transfer tax, bracket by bracket (2026 rates)."""
    brackets = [(55_000, 0.005), (250_000, 0.01), (400_000, 0.015), (2_000_000, 0.02)]
    tax, low = 0.0, 0
    for high, rate in brackets:
        if price > low:
            tax += (min(price, high) - low) * rate
        low = high
    if price > 2_000_000:
        tax += (price - 2_000_000) * 0.025  # one or two single-family residences
    return tax

def monthly_rate(quoted):             # Canadian rule, see the last lesson of the chapter
    return (1 + quoted / 2) ** (1 / 6) - 1

def payment(loan, quoted, years):
    i, n = monthly_rate(quoted), 12 * years
    return loan * i / (1 - (1 + i) ** -n)

def balance(loan, quoted, years, k):  # amount owed after k payments
    i, pay = monthly_rate(quoted), payment(loan, quoted, years)
    return loan * (1 + i) ** k - pay * ((1 + i) ** k - 1) / i

def buy_minus_rent(price=700_000, down=0.20, quoted=0.05, amortization=25,
                   home_growth=0.03, invest=0.05, rent_growth=0.03, rent=2800,
                   years=10, tax_rate=0.008, maint_rate=0.01, home_ins=1500,
                   rent_ins=300, selling=0.05, legal=2000):
    loan = price * (1 - down)
    pay = payment(loan, quoted, amortization)
    m = (1 + invest) ** (1 / 12) - 1
    renter = price * down + ltt(price) + legal   # the renter invests the upfront cash
    buyer = 0.0
    for month in range(12 * years):
        year = month // 12
        value = price * (1 + home_growth) ** year
        own = pay + (tax_rate + maint_rate) * value / 12 + home_ins / 12
        rental = rent * (1 + rent_growth) ** year + rent_ins / 12
        budget = max(own, rental)
        buyer = buyer * (1 + m) + (budget - own)
        renter = renter * (1 + m) + (budget - rental)
    sale = price * (1 + home_growth) ** years * (1 - selling)
    owner_wealth = sale - balance(loan, quoted, amortization, 12 * years) + buyer
    return owner_wealth - renter

print(ltt(700_000), ltt(520_000))      # 10475.0 6875.0
print(round(buy_minus_rent()))         # 19909

for growth in (0.0, 0.01, 0.02, 0.03, 0.04, 0.05):
    row = [round(buy_minus_rent(home_growth=growth, invest=r) / 1000) for r in (0.03, 0.05, 0.07)]
    print(f"{growth:.0%}", row)
# 0% [-123, -187, -262]
# 1% [-60, -125, -200]
# 2% [9, -56, -131]
# 3% [85, 20, -56]
# 4% [168, 103, 26]
# 5% [259, 193, 116]
```

The function returns the owner's wealth minus the renter's wealth after 10 years, in dollars. With the base assumptions, owning ends \$19,909 ahead.

</details>

The base case is a narrow win for buying. The table below is the same output, in thousands of dollars: positive numbers favour buying and negative numbers favour renting.

| Home price growth | Investments at 3% | Investments at 5% | Investments at 7% |
|---|---|---|---|
| 0% a year | $-123$ | $-187$ | $-262$ |
| 1% a year | $-60$ | $-125$ | $-200$ |
| 2% a year | $9$ | $-56$ | $-131$ |
| 3% a year | $85$ | $20$ | $-56$ |
| 4% a year | $168$ | $103$ | $26$ |
| 5% a year | $259$ | $193$ | $116$ |

Rent growth is 3% a year in every cell. With 5% investment returns, buying comes out ahead once home prices grow faster than about 2.7% a year. A one-point change in either assumption moves the result by \$60,000 to \$75,000, which is bigger than the base-case gap of \$19,909. The honest conclusion from the model is that the answer depends on guesses nobody can make, so the model is best used to see which guess matters most, not to pick a winner.

The model leaves out several things: income tax on investment returns (an account such as a TFSA or FHSA, covered in [retirement accounts](../06-investing-and-retirement/03-retirement-accounts.md), can shelter them), a change in the mortgage rate at renewal, and the value some people place on stability or on being free to move.

## FAQ

### Why does the renter invest the down payment in the model?

Because that money is the owner's down payment and closing costs, and a fair comparison gives both people the same starting cash. If the renter spent it, the renter would be starting with less wealth than the owner by choice. The model sets the renter's account to the same total the owner puts into the house, so any difference at the end comes from the choices and not from the starting amounts.

### Is a bigger down payment always better?

A bigger down payment means a smaller loan and less interest, and it can lower the mortgage insurance premium (see [mortgage basics](02-mortgage-basics.md)). It also means more cash tied up in the house. The model's opportunity cost shows the trade: each dollar in the house earns the avoided mortgage rate, and each dollar invested earns the investment return.

### Why does the answer swing so much with the growth rate?

The owner holds a \$700,000 asset financed mostly with debt. A 1% change in its value is \$7,000 a year at the start, and over 10 years it compounds. Because the owner's money is leveraged, a small change in the price growth has a large effect on the owner's equity.

### Do the rules of thumb replace the model?

No. They are a quick screen, using one year of costs and a guess about interest rates. The model follows the whole 10 years and shows how the result depends on each assumption.

## Practice

### Warm-up

1\. Find the Ontario land transfer tax on a \$300,000 home, and the net tax if the buyer qualifies for the first-time refund.

<details class="solution" markdown>
<summary>Solution</summary>

The brackets give $0.005 \times 55000 = 275$, $0.01 \times 195000 = 1950$ and $0.015 \times 50000 = 750$ (the part of the price between \$250,000 and \$300,000). The total is $275 + 1950 + 750 = 2975$, so \$2,975.

The refund is the smaller of \$2,975 and \$4,000, which is \$2,975, so the net tax is \$0.

Check: \$300,000 is below \$368,000, the price up to which the first-time buyer pays no tax, and $2975 \div 300000 \approx 0.99\%$, between 0.5% and 2%.

</details>

2\. A \$480,000 condo rents for \$2,000 a month. Find its price-to-rent ratio, and the monthly cost the 5% rule gives.

<details class="solution" markdown>
<summary>Solution</summary>

The yearly rent is $12 \times 2000 = 24000$, and the ratio is $480000 \div 24000 = 20$.

The 5% rule gives $0.05 \times 480000 = 24000$ a year, which is $24000 \div 12 = 2000$ a month, exactly the rent. Both rules say it is a toss-up.

Check: $20 \times 24000 = 480000$.

</details>

3\. A home is worth \$900,000 and the mortgage balance is \$610,000. Find the equity, and the equity after selling costs of 4% of the value.

<details class="solution" markdown>
<summary>Solution</summary>

The equity is $900000 - 610000 = 290000$, so \$290,000.

Selling costs are $0.04 \times 900000 = 36000$. After selling, the equity you receive is $290000 - 36000 = 254000$, so \$254,000.

Check: $0.96 \times 900000 = 864000$ and $864000 - 610000 = 254000$.

</details>

### Standard

4\. A \$500,000 home has these year-1 numbers (made up): mortgage interest \$19,000, property tax \$4,000, maintenance \$5,000 and insurance \$1,200. The \$100,000 down payment could earn 4% elsewhere. Rent for a similar home is \$2,000 a month plus \$250 a year of renter's insurance. If the home gains 3% in the year, which choice has the lower net cost in year 1?

<details class="solution" markdown>
<summary>Solution</summary>

Owner's unrecoverable costs: $19000 + 4000 + 5000 + 1200 = 29200$. The opportunity cost is $0.04 \times 100000 = 4000$, so the total is \$33,200.

The gain in value is $0.03 \times 500000 = 15000$, so the owner's net cost is $33200 - 15000 = 18200$.

The renter pays $12 \times 2000 + 250 = 24250$.

Owning has the lower net cost, \$18,200 against \$24,250, but only with the 3% gain. Without any gain, owning costs \$33,200 and renting wins.

Check: the owner's net cost is below the renter's by \$6,050, and a gain of only 1.2% (\$6,000) would be needed to make them equal, near the \$6,050 gap.

</details>

5\. A \$700,000 home grows at 2% a year for 10 years. Selling costs are 5% of the sale price, and the mortgage balance then is \$413,258.41. How much cash do you walk away with?

<details class="solution" markdown>
<summary>Solution</summary>

The sale price is $700000 \times 1.02^{10} = 853296.09$. Selling costs take 5%, leaving $0.95 \times 853296.09 = 810631.29$. Subtract the balance: $810631.29 - 413258.41 = 397372.88$.

You receive about \$397,373.

Check: $1.02^{10} \approx 1.219$, and $700000 \times 1.219 = 853300$, close to the value above.

</details>

6\. Using the sensitivity table, with 5% investment returns, home price growth of 2% gives $-56$ (thousand dollars) and 3% gives $20$. Estimate by interpolation the growth rate at which the two choices tie.

<details class="solution" markdown>
<summary>Solution</summary>

Between 2% and 3% the result rises by $20 - (-56) = 76$ (thousand dollars). To rise from $-56$ to 0 it needs $\frac{56}{76} \approx 0.74$ of that step, so the tie is at about $2\% + 0.74 \times 1\% = 2.74\%$.

Check: solving the model exactly gives 2.745%, so the interpolation is accurate to about a hundredth of a percentage point.

</details>

### Challenge

7\. A first-time buyer gets the \$4,000 refund, so closing costs fall by \$4,000. In the model, the renter's starting investment is the same as the owner's upfront cash, so it falls by \$4,000 too. By how much does the buy-minus-rent number change over 10 years at 5% investment returns?

<details class="solution" markdown>
<summary>Solution</summary>

The refund leaves \$4,000 less in the renter's starting account, and that \$4,000 would have grown at 5% for 10 years. So the owner's relative position improves by $4000 \times 1.05^{10} = 6515.58$.

The base result of \$19,909 becomes about \$26,425.

Check: running the code with legal fees lowered by \$4,000 gives a result higher by \$6,515.58.

</details>

8\. (Reviews [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md).) The rent starts at \$2,800 a month for year 1 and rises 3% each year, and the rent is constant within a year. Find the rent in year 10, and the total rent paid over 10 years.

<details class="solution" markdown>
<summary>Solution</summary>

The monthly rent in year 10 is $2800 \times 1.03^{9} = 3653.36$, so about \$3,653.36.

Each year's rent is $12 \times 2800 \times 1.03^{k}$ for $k = 0, 1, \ldots, 9$, a geometric series with first term $33600$ and ratio $1.03$:

$$
33600 \times \frac{1.03^{10} - 1}{1.03 - 1} = 33600 \times 11.4639 = 385186.34.
$$

The total is about \$385,186.

Check: adding the ten yearly amounts in code gives \$385,186.34.

</details>

## Where this shows up

- The next lesson, [mortgage basics](02-mortgage-basics.md), covers the rules behind the loan: down payments, mortgage insurance and the stress test. After it, [mortgage amortization schedules](03-mortgage-amortization-schedules.md) builds the month-by-month schedule used here.
- Economics calls the comparison of two choices by their next-best alternatives opportunity cost, and comparing money across years is present value ([present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md)).
- In CS, the `buy_minus_rent` function is a small simulation: a loop over months with a few parameters, and a sensitivity table is the same function called on a grid of inputs.
