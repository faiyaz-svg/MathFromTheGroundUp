# Percent change and applications

After this lesson you can find a percent increase or decrease, go from an old value to a new one and back with a multiplier, combine several percent changes, tell a percent change from a change in percentage points, and work out markups, margins, stacked discounts, simple interest and the HST on a sale price.

Before this: [percents](03-percents.md), especially finding the whole, and the distributive property from [properties of operations](../../01-elementary/04-properties-of-operations.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Your rent goes from \$1,600 to \$1,720 a month. What is the percent increase?
2. After a 30% discount, a price is \$56. What was the price before the discount?
3. A price rises 20% and then falls 20%. What is the overall percent change?

<details class="solution" markdown>
<summary>Answers</summary>

1. The change is $1720 - 1600 = 120$, and $120 \div 1600 = 0.075$, so the rent rose 7.5%.
2. After 30% off you pay 70% of the price, so the price was $56 \div 0.70 = 80$, that is, \$80.
3. Multiply the multipliers: $1.20 \times 0.80 = 0.96$. The price ends at 96% of where it started, a 4% decrease.

</details>

## The idea

Your rent goes up from \$1,600 to \$1,720 a month, and your monthly grocery bill goes up from \$400 to \$520. Both rose by \$120, but the two changes don't feel the same. The rent rose by $\frac{120}{1600} = 0.075$ of what it was, which is 7.5%, while the groceries rose by $\frac{120}{400} = 0.3$, which is 30%.

That is a percent change: the change, written as a percent of the value you started from. The starting value is the whole, the amount that counts as 100%, just as in [percents](03-percents.md#solving-part-whole-and-percent-problems). Most mistakes in this lesson come from dividing by some other number, usually the new value.

A second idea runs through the whole lesson. Going up 7.5% means ending at 107.5% of where you started, so the new rent is the old rent times 1.075. Once every percent change is a multiplication, the harder questions (undoing a change, or combining several) become one more multiplication or division.

## Definitions

Let $\text{old}$ be a starting value that is not 0, and $\text{new}$ the value after a change. The **percent change** from old to new is

$$
\text{percent change} = \frac{\text{new} - \text{old}}{\text{old}} \times 100\%.
$$

A positive percent change is a **percent increase**, and a negative one is a **percent decrease**. A decrease is usually reported without its minus sign, as in "the price fell 19.2%". In plain words, the percent change is the change divided by where you started: from \$1,600 to \$1,720 the change is \$120, and $\frac{120}{1600} = 7.5\%$.

For a change at the rate $r$, written as a decimal (0.075 for a 7.5% increase, $-0.30$ for a 30% decrease), the new value is

$$
\text{new} = (1 + r) \times \text{old}.
$$

The number $1 + r$ is the **multiplier** of the change, also called the growth factor. A 7.5% increase has multiplier 1.075, and a 30% decrease has multiplier $1 - 0.30 = 0.70$. The finance lessons use the same letter $r$ for an interest rate, which is a percent change per period.

A **percentage point** is the unit for the plain difference between two percents. A rate that goes from 4% to 5% has risen by 1 percentage point, while its percent change is $\frac{5 - 4}{4} = 0.25$, or 25%.

A store's **markup** is the amount it adds to its cost to get the selling price, usually written as a percent of the cost. Its **margin**, or gross margin, is the same profit written as a percent of the selling price. An item bought for \$40 and sold for \$50 makes a profit of \$10, so its markup is $\frac{10}{40} = 25\%$ and its margin is $\frac{10}{50} = 20\%$.

**Simple interest** is interest paid only on the amount first borrowed or saved, called the **principal**. For a principal $P$ at an annual interest rate $r$ for $t$ years, the simple interest is

$$
I = Prt.
$$

In plain words, the interest is the same every year: \$2,000 at 4% earns $2000 \times 0.04 = 80$ dollars a year. The finance lessons write the principal as $\text{PV}$, for present value, so the same formula appears there as $I = \text{PV} \times r \times t$.

## How to do it

### Finding a percent change

1. Find the old value. It is the whole, the amount that counts as 100%. The question usually names it after "from" ("from \$1,600 to \$1,720") or after "than" ("12% more than last year").
2. Subtract to find the change: $\text{new} - \text{old}$. A negative change is a decrease.
3. Divide the change by the old value.
4. Multiply by 100 to get a percent, and round once, at the end.
5. Check that the old value times the multiplier $1 + r$ gives the new value.

### Finding the new value: multiply

A change at the rate $r$ adds $r \times \text{old}$ to the old value. Factoring out the old value with the distributive property gives

$$
\text{old} + r \times \text{old} = (1 + r) \times \text{old}.
$$

So for a 7.5% increase you multiply by 1.075, and for 30% off you multiply by 0.70. This is the same reason that multiplying a price by 1.13 adds 13% HST, as the [percents FAQ](03-percents.md#faq) shows.

### Finding the old value: divide

Since $\text{new} = (1 + r) \times \text{old}$, dividing both sides by the multiplier gives

$$
\text{old} = \frac{\text{new}}{1 + r}.
$$

Don't take the opposite percent of the new value instead. That uses the new value as the whole, which is the receipt mistake from the [percents worked examples](03-percents.md#worked-examples), where subtracting 13% of a total failed to remove the tax.

### Several changes in a row

Each change multiplies the value by its own multiplier, so the multipliers multiply. A rise of 10% followed by a fall of 10% gives

$$
1.10 \times 0.90 = 0.99,
$$

so the value ends at 99% of where it started. That is a 1% decrease, not 0%. On \$100, the rise gives \$110, and 10% of \$110 is \$11, which leaves \$99: the fall is 10% of a bigger whole than the rise, so it takes away more than the rise added.

The overall percent change is the product of the multipliers minus 1. The order of the changes doesn't matter, because multiplication can be done in any order, so a fall of 10% followed by a rise of 10% also ends at 99%. The same change made $n$ times multiplies the value by $(1 + r)^n$, a power from [exponents and order of operations](../01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md). For example, prices that rise 2% a year for 10 years rise by a factor of $1.02^{10} \approx 1.219$, which is 21.9% and not 20%.

### Percent change or percentage points

When the quantity is itself a percent, such as an interest rate, a tax rate or an unemployment rate, the phrase "it went up 1%" is unclear. Use percentage points for the subtraction, and percent change for the comparison with the old value:

| Rate goes from | Change in percentage points | Percent change |
|---|---|---|
| 4% to 5% | $+1$ point | $\frac{1}{4} = 25\%$ |
| 2% to 3% | $+1$ point | $\frac{1}{2} = 50\%$ |
| 3.25% to 3.00% | $-0.25$ points | $\frac{-0.25}{3.25} \approx -7.7\%$ |

The first two rows have the same change in points and very different percent changes, because the old values differ. Finance often counts small changes in basis points, where a basis point is a hundredth of a percentage point, so the last row is a cut of 25 basis points.

### Markups and margins

A markup and a margin start from the same profit, the price minus the cost. They differ in the whole they divide by:

$$
\text{markup} = \frac{\text{price} - \text{cost}}{\text{cost}}, \qquad \text{margin} = \frac{\text{price} - \text{cost}}{\text{price}}.
$$

A markup is a percent change from the cost to the price, so $\text{price} = \text{cost} \times (1 + \text{markup})$. A margin works from the other end. The cost is the part of the price that isn't margin, so $\text{cost} = \text{price} \times (1 - \text{margin})$, and dividing gives $\text{price} = \text{cost} \div (1 - \text{margin})$.

### Simple interest

To use $I = Prt$, write the rate as a decimal and make the rate and the time use the same unit: an annual rate needs the time in years, so 18 months is $t = 1.5$. At 4% a year for 3 years, \$2,000 earns

$$
I = 2000 \times 0.04 \times 3 = 240
$$

dollars, and the balance is \$2,240. Simple interest adds the same \$80 every year. If instead the account added 4% of each new balance, the multipliers would multiply, as in the section on several changes, and the balance after 3 years would be $2000 \times 1.04^3 = 2249.728$, about \$2,249.73. That is compound interest, and the two methods get full lessons in [simple interest](../../08-financial-math/02-interest-and-growth/01-simple-interest.md) and [compound interest](../../08-financial-math/02-interest-and-growth/02-compound-interest.md).

## Worked examples

<div class="example" markdown>

### Example 1: a laptop goes on sale

A laptop's price drops from \$1,299 to \$1,049. What is the percent decrease?

Step 1: the price drops from \$1,299, so the old value is 1299, and it is the whole.

Step 2: the change is $1049 - 1299 = -250$ dollars. It is negative, so this is a decrease.

Step 3: divide the change by the old value:

$$
\frac{-250}{1299} = -0.19245\ldots
$$

Step 4: multiply by 100 and round once: about $-19.2\%$. The price fell by about 19.2%.

<div class="warning" markdown>

Watch out at Step 3: dividing by the new price instead gives $250 \div 1049 = 0.238$, about 23.8%. That number answers a different question: the old price was 23.8% more than the new one. A percent decrease is measured against the price before the drop.

</div>

Step 5: check with the multiplier. A 19.2% decrease has multiplier $1 - 0.192 = 0.808$, and $1299 \times 0.808 = 1049.59$, close to \$1,049; the small gap comes from rounding the percent. With the unrounded rate, $1299 \times (1 - 0.19245\ldots)$ is exactly 1049. For an estimate, 20% of \$1,300 is \$260, a little more than the \$250 drop, so a little under 20% makes sense.

</div>

<div class="example" markdown>

### Example 2: your wage before a raise

After a 15% raise, your wage is \$21.85 an hour. What was it before the raise?

The raise was 15% of the old wage, so the old wage is the whole and the unknown. The multiplier is 1.15, so divide:

$$
\text{old} = \frac{21.85}{1.15} = 19.
$$

Your wage was \$19.00 an hour. Check: $19 \times 1.15 = 21.85$.

Taking 15% off the new wage is the tempting shortcut, and it gives $21.85 \times 0.85 = 18.5725$, about \$18.57. The check shows it fails: a 15% raise on \$18.57 gives $18.57 \times 1.15 = 21.3555$, about \$21.36, not \$21.85.

</div>

<div class="example" markdown>

### Example 3: two discounts and the HST

A jacket's regular price is \$120. It is 40% off, and at the register you get an extra 25% off the sale price. Stores charge HST on the price after their discounts, and Ontario's HST is 13% as of 2026 (source: the CRA's [GST/HST calculator and rates page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html)). What do you pay, and what single discount would match the two?

Write the three changes as multipliers: 40% off is 0.60, 25% off is 0.75, and adding 13% HST is 1.13. Then multiply in order:

$$
120 \times 0.60 = 72, \qquad 72 \times 0.75 = 54, \qquad 54 \times 1.13 = 61.02.
$$

You pay \$61.02, of which $54 \times 0.13 = 7.02$ dollars is HST.

The two discounts together have multiplier $0.60 \times 0.75 = 0.45$, so you pay 45% of the regular price before tax. That is a single discount of 55%, not $40\% + 25\% = 65\%$. The second discount was 25% of \$72, not of \$120, so it saved \$18 rather than \$30.

Check: \$54 is 45% of \$120, since $0.45 \times 120 = 54$. A 65% discount would have left $0.35 \times 120 = 42$ dollars before tax, so the stacked discounts cost \$12 more before tax than the sum of the percents suggests.

</div>

<div class="example" markdown>

### Example 4: markup and margin (finish it yourself)

A store buys hoodies for \$32 each and sells them for \$48. Find the markup and the margin, as percents.

The profit on each hoodie is $48 - 32 = 16$ dollars. The markup is the profit as a percent of the cost:

$$
\text{markup} = \frac{16}{32} = 0.5 = 50\%.
$$

Now find the margin, the same profit as a percent of the price, and check it by working back from the price to the cost.

<details class="solution" markdown>
<summary>Finish</summary>

The margin is $\frac{16}{48} = \frac{1}{3}$, about 33.3%. The same \$16 is a smaller percent of the price than of the cost, because the price is the bigger whole.

Check: $\text{cost} = \text{price} \times (1 - \text{margin})$, and $48 \times \left(1 - \frac{1}{3}\right) = 48 \times \frac{2}{3} = 32$. The markup checks too: $32 \times 1.5 = 48$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the same percent doesn't undo a change. A price that rises 25% and then falls 25% ends at $1.25 \times 0.75 = 0.9375$ of where it started, 6.25% lower. To undo a 25% rise you need a 20% fall, since $1.25 \times 0.80 = 1$. In general, divide by the multiplier, as in [Finding the old value](#finding-the-old-value-divide).

</div>

<div class="warning" markdown>

Watch out: percent changes in a row don't add. Discounts of 40% and then 25% make a 55% discount, not 65% (Example 3), and a rise of 10% followed by a fall of 10% is a 1% loss. Each change after the first is a percent of a new whole, so multiply the multipliers.

</div>

<div class="warning" markdown>

Watch out for percent and percentage points. If a loan's interest rate rises from 4% to 5%, saying "it rose 1%" suggests a tiny change, from 4% to 4.04%. The rate rose 1 percentage point, which is a 25% increase in the rate. On the same balance the yearly interest rises 25% too: on \$10,000 it goes from \$400 to \$500.

</div>

<div class="warning" markdown>

Watch out: a markup is not a margin. A 50% markup is a 33.3% margin, because the markup divides the profit by the cost and the margin divides it by the bigger price. A store that wants a 50% margin has to mark the cost up by 100%, doubling it.

</div>

<div class="warning" markdown>

Watch out with "times as much" and "more than". A price that triples ends at 300% of where it started, so it has risen by 200%, not 300%. The multiplier is 3, and the rate is $3 - 1 = 2$.

</div>

A decrease of more than 100% is impossible for an amount that can't go below zero, such as a price: a 100% decrease leaves nothing. Increases have no limit, since doubling is a 100% increase and multiplying by 10 is a 900% increase.

Percent change from 0 is undefined, because the formula divides by the old value. An app that goes from 0 users to 500 users has grown by 500 users, and no percent describes that.

When the old value is negative, such as a company's loss, the formula gives misleading signs. A loss of \$2 million that becomes a profit of \$1 million has the percent change $\frac{1 - (-2)}{-2} = -150\%$, a "decrease" for an improvement ([integer arithmetic and sign rules](../01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md)). Reports usually give the dollar change in that case.

## Tricks and shortcuts

To undo a percent change, divide by its multiplier. The undo of a rise of $r$ is a fall of $\frac{r}{1 + r}$, and a few pairs come up often:

| Change | Change that undoes it |
|---|---|
| $+10\%$ | about $-9.1\%$ |
| $+25\%$ | $-20\%$ |
| $+50\%$ | about $-33.3\%$ |
| $+100\%$ (doubling) | $-50\%$ (halving) |
| $-50\%$ (halving) | $+100\%$ (doubling) |

Small changes almost add. Rises of 2% and then 3% give $1.02 \times 1.03 = 1.0506$, a rise of 5.06%, close to 5%. The extra 0.06% is $0.02 \times 0.03 = 0.0006$, the product of the two rates, which is tiny when both rates are small. For a quick estimate with small rates, add them; for an exact answer, multiply the multipliers.

Read a multiplier as a percent: 0.85 is 15% off, 1.075 is a 7.5% increase, and 2.5 is a 150% increase.

To turn a markup into a margin, divide the markup by 1 plus the markup. A 25% markup is a $\frac{0.25}{1.25} = 20\%$ margin, a 50% markup is a $\frac{0.5}{1.5} \approx 33.3\%$ margin, and a 100% markup is a 50% margin.

## In code

Combining changes is a product of multipliers, which Python's `math.prod` computes in one line. The format code `:.2%` multiplies by 100 and adds the percent sign.

<details class="code" markdown>
<summary>In code</summary>

```python
from math import prod

def overall_change(*rates):
    """Combine percent changes written as decimals, such as 0.10 for +10%."""
    return prod(1 + r for r in rates) - 1

print(f"{overall_change(0.10, -0.10):.2%}")    # +10% then -10%: -1.00%
print(f"{overall_change(-0.40, -0.25):.2%}")   # 40% off, then 25% off: -55.00%
print(f"{overall_change(*[0.02] * 10):.2%}")   # +2% a year for 10 years: 21.90%

def undo(r):
    """The percent change that takes the new value back to the old one."""
    return 1 / (1 + r) - 1

print(f"{undo(0.25):.2%}", f"{undo(-0.50):.2%}")   # -20.00% 100.00%
```

The expression `[0.02] * 10` builds a list of ten copies of 0.02, and the `*` in front of it passes them as ten separate arguments.

</details>

## FAQ

### Why does a 50% loss need a 100% gain to break even?

The gain is a percent of a smaller whole. An investment of \$1,000 that falls 50% is worth \$500, and getting back to \$1,000 means gaining \$500, which is 100% of \$500. In multipliers, the fall is 0.5, and the gain that undoes it is $1 \div 0.5 = 2$, a doubling.

### Does it matter whether the discount or the tax comes first?

Not for percents. Each one is a multiplication, and $120 \times 0.60 \times 0.75 \times 1.13$ gives \$61.02 in every order. It does matter for a fixed dollar amount. On the \$54 jacket from Example 3, a \$10 coupon taken off before tax gives $(54 - 10) \times 1.13 = 49.72$ dollars, while taking \$10 off the total after tax gives $54 \times 1.13 - 10 = 51.02$ dollars. The difference is the HST on the \$10, which is \$1.30.

### Why measure the change against the old value?

Because the question is usually "how big is this change compared with where we started?". Nothing stops you from measuring against another value, and some measures do: the margin compares the profit with the price, not the cost. What matters is to say which whole you used, because the same change gives different percents against different wholes, as Example 1 showed with 19.2% and 23.8%.

## Practice

### Warm-up

1\. Find the percent change: (a) from 80 to 92, (b) from 250 to 215, (c) from 40 to 100.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The change is $92 - 80 = 12$, and $12 \div 80 = 0.15$, a 15% increase.
- (b) The change is $215 - 250 = -35$, and $-35 \div 250 = -0.14$, a 14% decrease.
- (c) The change is $100 - 40 = 60$, and $60 \div 40 = 1.5$, a 150% increase.

Check with multipliers: $80 \times 1.15 = 92$, $250 \times 0.86 = 215$ and $40 \times 2.5 = 100$.

</details>

2\. Write the multiplier, then find the new value: (a) \$64 increased by 12.5%, (b) \$64 decreased by 12.5%, (c) 1,200 decreased by 0.4%.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The multiplier is $1 + 0.125 = 1.125$, and $64 \times 1.125 = 72$, so \$72.
- (b) The multiplier is $1 - 0.125 = 0.875$, and $64 \times 0.875 = 56$, so \$56.
- (c) As a decimal, 0.4% is 0.004, so the multiplier is $1 - 0.004 = 0.996$, and $1200 \times 0.996 = 1195.2$.

Check: 12.5% of 64 is 8, and $64 + 8 = 72$ while $64 - 8 = 56$. Also 0.4% of 1200 is 4.8, and $1200 - 4.8 = 1195.2$.

</details>

3\. A bank's interest rate on a loan goes from 4.5% to 5.4%. (a) By how many percentage points did it rise? (b) What is the percent change in the rate?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Subtract the percents: $5.4 - 4.5 = 0.9$, so the rate rose 0.9 percentage points.

(b) Divide the change by the old rate: $0.9 \div 4.5 = 0.2$, so the rate rose 20%.

Check: $4.5 \times 1.2 = 5.4$.

</details>

### Standard

4\. A video game is on sale for \$52.49 after 25% off. (a) What was the regular price? (b) How much do you save?

<details class="solution" markdown>
<summary>Solution</summary>

(a) After 25% off you pay 75% of the regular price, so the regular price is the whole: $52.49 \div 0.75 = 69.9866\ldots$, which rounds to \$69.99.

(b) You save $69.99 - 52.49 = 17.50$ dollars.

Check: $69.99 \times 0.75 = 52.4925$, which rounds to \$52.49. And 25% of about \$70 is \$17.50.

</details>

5\. A pair of boots costs \$85. The store takes 30% off, then an extra 20% off the sale price, and then adds 13% HST. (a) What do you pay? (b) What single discount equals the two discounts?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Multiply by the three multipliers: $85 \times 0.70 = 59.50$, then $59.50 \times 0.80 = 47.60$, then $47.60 \times 1.13 = 53.788$. You pay about \$53.79.

(b) The discounts have multiplier $0.70 \times 0.80 = 0.56$, so you pay 56% of the regular price, which is a single discount of 44%, not 50%.

Check: $0.56 \times 85 = 47.60$, the price before tax from part (a).

</details>

6\. A bookstore pays \$96 for a textbook and wants a 25% margin on it. (a) What should the selling price be? (b) What markup is that?

<details class="solution" markdown>
<summary>Solution</summary>

(a) With a 25% margin, the cost is the other 75% of the price, so the price is $96 \div 0.75 = 128$ dollars.

(b) The profit is $128 - 96 = 32$ dollars, and the markup is $32 \div 96 = \frac{1}{3}$, about 33.3%.

Check: the margin is $32 \div 128 = 0.25$, as wanted. A 25% markup by mistake would give $96 \times 1.25 = 120$ dollars, a margin of only $24 \div 120 = 20\%$.

</details>

### Challenge

7\. You put \$2,500 into an account for 5 years at 4% a year. (a) With simple interest, how much interest do you earn, and what is the final balance? (b) If instead 4% of each year's balance is added at the end of the year, what is the final balance? (c) What is the percent change in the balance over the 5 years in each case?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $I = Prt = 2500 \times 0.04 \times 5 = 500$ dollars, so the balance is \$3,000.

(b) Each year multiplies the balance by 1.04, so after 5 years it is $2500 \times 1.04^5 = 3041.632\ldots$, about \$3,041.63, which is \$41.63 more than with simple interest.

(c) Simple: $\frac{3000 - 2500}{2500} = 0.2$, a 20% increase, which is 5 years times 4%. Yearly multiplier: $\frac{3041.63 - 2500}{2500} = 0.21665\ldots$, about 21.7%, more than 20% because each year's 4% is taken of a bigger balance.

Check: $1.04^5 = 1.04 \times 1.04 \times 1.04 \times 1.04 \times 1.04 \approx 1.2167$, which matches the 21.7%.

</details>

8\. (Reviews [ratios and unit rates](01-ratios-and-unit-rates.md).) A 1.5 kg bag of rice used to cost \$6.49. The store replaces it with a 1.2 kg bag at \$5.99. (a) What is the percent change in the shelf price? (b) What is the percent change in the price per 100 g?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The change is $5.99 - 6.49 = -0.50$ dollars, and $-0.50 \div 6.49 = -0.0770\ldots$, so the shelf price fell about 7.7%.

(b) The old bag is 15 lots of 100 g and the new bag is 12 lots. The old unit price is $6.49 \div 15 = 0.43266\ldots$ dollars per 100 g, and the new one is $5.99 \div 12 = 0.49916\ldots$ dollars per 100 g. The percent change is

$$
\frac{0.49916\ldots - 0.43266\ldots}{0.43266\ldots} = 0.1536\ldots,
$$

about a 15.4% increase. The price on the shelf went down while the price of the rice went up, because the bag shrank by 20%. Keep the unrounded unit prices here: rounded to \$0.43 and \$0.50 they would give 16.3%.

Check with multipliers: the price multiplier is $5.99 \div 6.49 \approx 0.923$ and the size multiplier is $1.2 \div 1.5 = 0.8$, and $0.923 \div 0.8 \approx 1.154$, a 15.4% rise per gram.

</details>

## Where this shows up

- In finance, [compound interest](../../08-financial-math/02-interest-and-growth/02-compound-interest.md) is a percent change repeated with the same multiplier, and [tips, discounts and HST](../../08-financial-math/01-everyday-money/01-tips-discounts-and-hst.md) and [inflation and real returns](../../08-financial-math/02-interest-and-growth/06-inflation-and-real-returns.md) use the multipliers from this lesson.
- Economics reports almost everything as a percent change, and the units matter: see [percent change vs percentage points](../../07-economics-math/01-measuring-the-economy/02-percent-change-vs-percentage-points.md), [growth rates and CAGR](../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md) and [CPI and inflation](../../07-economics-math/01-measuring-the-economy/07-cpi-and-inflation.md). An elasticity is a ratio of two percent changes ([elasticity](../../07-economics-math/02-markets/05-elasticity.md)).
- In software, an A/B test that raises a sign-up rate from 2% to 3% is a gain of 1 percentage point and a 50% relative lift, and reports quote whichever sounds bigger. A program whose run time drops from 50 s to 40 s takes 20% less time but runs 1.25 times as fast, since $50 \div 40 = 1.25$.
