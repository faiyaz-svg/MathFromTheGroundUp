# Tips, discounts and HST

After this lesson you can work out the final price when discounts, HST and a tip are all involved, remove the tax from a receipt total, and explain why two discounts in a row are worth less than their percents added together.

Before this: [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md) and [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md). Both are quick to re-read, and this lesson reuses their multipliers.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A \$140 coat is 30% off, and the register takes an extra 10% off that price. What do you pay with 13% HST?
2. A receipt shows a total of \$67.80, HST included. What was the price before tax?
3. Dinner costs \$42.60 before tax. You tip 15% of that pre-tax amount. What is the total, with HST and the tip?

<details class="solution" markdown>
<summary>Answers</summary>

1. The multipliers are 0.70, 0.90 and 1.13. Then $140 \times 0.70 \times 0.90 = 88.20$ before tax, and $88.20 \times 1.13 = 99.666$, so \$99.67.
2. The total is 113% of the price, so the price is $67.80 \div 1.13 = 60$, that is, \$60.00.
3. The tax is $0.13 \times 42.60 = 5.538$ and the tip is $0.15 \times 42.60 = 6.39$. The total is $42.60 + 5.538 + 6.39 = 54.528$, so \$54.53.

</details>

## The idea

Take a night out. The menu prices don't include tax, the server adds HST at the end, and you add a tip on top. Before that, the shop where you bought a shirt took a sale price off the tag and then an extra discount at the register. Every one of these steps is a percent of some amount, and the only real question each time is: percent of what?

The [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md) lesson answered that for one step. Here the steps pile up, and the trick is to turn each step into a multiplier (the number you multiply by, from the [percent change lesson](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions)). Taking 20% off is a multiplication by 0.80. Adding 13% HST is a multiplication by 1.13. A chain of steps is then a chain of multiplications, and you can read the final price straight off it.

Two choices decide most of the confusion. First, the order: a percent discount and the HST can be done in either order and give the same total, but a fixed-dollar coupon cannot. Second, the whole you take a percent of, which matters most when you remove tax from a total and when you decide what your tip is a percent of.

## Definitions

The **Harmonized Sales Tax (HST)** is the sales tax charged on most goods and services in Ontario. Its rate is 13%: a 5% federal part (the old GST) and an 8% provincial part. The Ontario government says the HST "replaced the 5% federal goods and services tax (GST) and the 8% retail sales tax (RST)" and is 13% in Ontario ([ontario.ca](https://www.ontario.ca/document/harmonized-sales-tax-hst)). The CRA's [rates page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html) lists 13% for Ontario.

In plain words, the tax on a purchase is 13 cents for every dollar of the price, and 5 of those cents go to the federal government and 8 to the province.

The **pre-tax price** is the price before HST is added, which is the price on the tag or the menu. The **tax-included total** is what you pay after HST, so it is $(1 + 0.13)$ times the pre-tax price. HST is 13% of the pre-tax price, so the pre-tax price is the whole in every HST question.

A **discount** of rate $d$, written as a decimal, takes the fraction $d$ of the current price off, so the new price is $(1 - d)$ times the current price. The number $1 - d$ is the multiplier of the discount.

A **tip** (also called a gratuity) is an amount you add for service. In Ontario it is a custom and not a law, usually 15% to 20% at a restaurant. A tip rate $t$ is a percent of some base, and the base is whatever the two sides decide: the pre-tax bill or the tax-included bill.

<div class="note" markdown>

These figures are for 2026 and change every year. Check the linked pages before using them for real decisions.

</div>

## How to do it

### Adding HST

The tax is 13% of the pre-tax price $p$, so the total is $p + 0.13p = 1.13p$ (the [percents FAQ](../../02-middle-school/02-ratios-rates-percents/03-percents.md#why-does-multiplying-by-113-give-the-total) shows why). The two parts of the tax are separate percents of the same $p$:

| Part | Rate | On \$24.99 |
|---|---|---|
| federal | 5% | $0.05 \times 24.99 = 1.2495$, so \$1.25 |
| provincial | 8% | $0.08 \times 24.99 = 1.9992$, so \$2.00 |
| HST | 13% | $0.13 \times 24.99 = 3.2487$, so \$3.25 |

The rounded parts, \$1.25 and \$2.00, add up to the rounded tax, \$3.25. That does not always happen, so compute the 13% from the unrounded price.

### Removing HST

The total is $1.13p$, so the pre-tax price is the total divided by 1.13. The tax is the total minus the pre-tax price. Taking 13% off the total uses the wrong whole, as the [percents lesson](../../02-middle-school/02-ratios-rates-percents/03-percents.md#worked-examples) showed in its third example.

### Discounts first, then tax

A store discount lowers the price, and HST is charged on the lowered price. The method for a chain of steps:

1. Write down the pre-tax tag price.
2. Turn each percent discount into its multiplier, $1 - d$.
3. Multiply the tag price by all the discount multipliers, in any order. Keep every digit.
4. Subtract any fixed-dollar coupon from the discounted price, if the coupon comes off before tax.
5. Multiply by 1.13 to add HST. The tax is the difference between this and the discounted price.
6. Round once, to the cent, at the end. Check with a rough estimate.

### Two discounts in a row

Most people expect 20% off and then 10% off to be 30% off. It is a little less, and the reason is short enough to prove.

*Theorem (stacked discounts).* Let $a$ and $b$ be discount rates written as decimals, with $0 \le a \le 1$ and $0 \le b \le 1$. A discount of $a$ followed by a discount of $b$ is the same as a single discount of $d = a + b - ab$. Also $d \le a + b$, with equality only when $a = 0$ or $b = 0$.

What we know: the first discount multiplies the price by $1 - a$, and the second multiplies that new price by $1 - b$. What we want: one discount $d$ that gives the same final price, and a comparison of $d$ with $a + b$. The plan is to multiply out the two multipliers and match the result with $1 - d$.

Proof. Start from a price $P$ with $P > 0$. After the first discount the price is $(1 - a)P$, and after the second it is $(1 - b)(1 - a)P$. A single discount $d$ would leave $(1 - d)P$, so we need

$$
(1 - d)P = (1 - a)(1 - b)P.
$$

Divide both sides by $P$, which is allowed because $P \ne 0$, and multiply out the right side:

$$
1 - d = 1 - a - b + ab.
$$

Subtracting 1 from both sides and multiplying by $-1$ gives $d = a + b - ab$. Since $a \ge 0$ and $b \ge 0$, the product $ab$ is at least 0, so $d = (a + b) - ab \le a + b$. The product is exactly 0 only when $a = 0$ or $b = 0$, and that is when the two sides are equal. $\blacksquare$

Look back. For 20% and 10%, $d = 0.20 + 0.10 - 0.02 = 0.28$, a 28% discount and not 30%. The missing 2% is the product $ab$: the second discount takes 10% of a price that is already 20% lower, so it saves 10% of 80 and not 10% of 100. The formula is symmetric in $a$ and $b$, so the order of the two discounts doesn't matter.

## Worked examples

<div class="example" markdown>

### Example 1: a sale, an extra discount and HST

A jacket is tagged \$80. The store takes 20% off, and the register takes an extra 10% off the sale price. What is the total with HST, and how much of it is tax?

Step 1: the tag price is \$80.

Step 2: the multipliers are $1 - 0.20 = 0.80$ and $1 - 0.10 = 0.90$.

Step 3: multiply, keeping every digit:

$$
80 \times 0.80 \times 0.90 = 57.60.
$$

Step 4: there is no coupon.

Step 5: add the HST with the multiplier 1.13. The tax is 13% of the discounted price:

$$
57.60 \times 0.13 = 7.488, \qquad 57.60 \times 1.13 = 65.088.
$$

Step 6: round once. The tax is \$7.49 and the total is \$65.09, and $57.60 + 7.49 = 65.09$, so the pieces agree.

Check: the single discount is $0.20 + 0.10 - 0.02 = 0.28$, so the pre-tax price is $0.72 \times 80 = 57.60$. A flat 30% off would give \$56.00, so the stacked discounts cost the shopper \$1.60 more before tax. For an estimate, 57.60 is about 58, and 13% of 58 is about 7.5, so the total is about 65.

<div class="warning" markdown>

Watch out at Step 3: the second discount is 10% of \$64, the price after the first discount, so it saves \$6.40 and not \$8.00. Taking both percents off the tag price gives \$56, which is the 30% mistake.

</div>

</div>

<div class="example" markdown>

### Example 2: dinner, from the receipt backwards

The receipt for your dinner shows a total of \$48.14 with HST included. You want to tip 18% of the pre-tax amount. How much is the tip, and what do you pay in all?

The pre-tax price is the whole, and the total is 113% of it, so divide:

$$
48.14 \div 1.13 = 42.6017\ldots
$$

The pre-tax bill is \$42.60. The tip is $0.18 \times 42.60 = 7.668$, so \$7.67, and you pay $48.14 + 7.67 = 55.81$ dollars.

If you tipped 18% of the tax-included \$48.14 instead, the tip would be $0.18 \times 48.14 = 8.6652$, about \$8.67. That is \$1.00 more, and it is the same as tipping $0.18 \times 1.13 = 20.34\%$ of the pre-tax bill. Neither choice is wrong; they are different tips. Say which base you mean.

Check: $42.60 \times 1.13 = 48.138$, which rounds to the receipt's \$48.14. The tax line is \$5.54, and $42.60 + 5.54 = 48.14$.

</div>

<div class="example" markdown>

### Example 3: rounding at the till

You buy three taxable items at \$2.49, \$3.49 and \$1.29. How much HST do you pay, if the tax is worked out (a) on the subtotal and (b) item by item?

The subtotal is $2.49 + 3.49 + 1.29 = 7.27$.

(a) $0.13 \times 7.27 = 0.9451$, so \$0.95 and a total of \$8.22.

(b) The item taxes are $0.13 \times 2.49 = 0.3237$ (\$0.32), $0.13 \times 3.49 = 0.4537$ (\$0.45) and $0.13 \times 1.29 = 0.1677$ (\$0.17). They add up to $0.32 + 0.45 + 0.17 = 0.94$, one cent less.

Both numbers are honest roundings of the same quantity. Each item lost a fraction of a cent, and three roundings can lose a cent that one rounding doesn't. The untidy one-cent gap is not an error, and the way to avoid it in your own work is the usual rule: round once, at the end.

Check: the unrounded item taxes add up to $0.3237 + 0.4537 + 0.1677 = 0.9451$, which is the subtotal's tax exactly.

</div>

<div class="example" markdown>

### Example 4: a coupon in a different place (finish it yourself)

A \$200 TV is 15% off, and you have a \$20 coupon that comes off the sale price before tax. What do you pay with HST?

Step 1: the tag price is \$200. Step 2: the discount multiplier is 0.85. Step 3: $200 \times 0.85 = 170$ dollars.

Now do Steps 4 to 6: apply the coupon, add the HST, and check with an estimate.

<details class="solution" markdown>
<summary>Finish</summary>

Step 4: $170 - 20 = 150$ dollars before tax.

Steps 5 and 6: $150 \times 1.13 = 169.50$, so you pay \$169.50. The tax is $150 \times 0.13 = 19.50$ dollars.

Check: 10% of 150 is 15, and 3% is 4.50, so 13% is 19.50. If the coupon were taken off after tax, you would pay $170 \times 1.13 - 20 = 172.10$, which is \$2.60 more, the HST on the \$20. A percent discount can go in any order; a dollar coupon can't.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: adding discounts. "20% off, then 10% off" is 28% off, not 30%. The second percent applies to a smaller price. With bigger discounts the gap is larger: 50% off and then 40% off is $0.50 + 0.40 - 0.20 = 0.70$, a 70% discount and not 90%.

</div>

<div class="warning" markdown>

Watch out: taking 13% off the total to remove the tax. On a \$67.80 total that gives $67.80 - 0.13 \times 67.80 = 58.986$, about \$58.99, which is \$1.01 too low. Divide by 1.13 instead and you get \$60.00.

</div>

<div class="warning" markdown>

Watch out: the tip on the total changes the tip. A 15% tip on a tax-included bill is $0.15 \times 1.13 = 16.95\%$ of the pre-tax bill. That is fine if you meant it. It is a mistake if you thought you were tipping 15% of the food and drinks.

</div>

<div class="warning" markdown>

Watch out: rounding in the middle. If you round the discounted price to the cent and then the tax to the cent, you can end a cent away from the one-step answer. Keep the full number, then round once.

</div>

A few edge cases are worth knowing. A 100% discount leaves a price of \$0 and a tax of \$0. A discount over 100% is meaningless for a price. A tip of 0% is allowed, and a tip is never a number you have to compute exactly: a rounded figure such as \$7.50 on a \$7.67 tip is a normal choice.

Not every purchase carries 13% HST. Some goods are taxed at a lower rate or not at all, so the rate on your receipt is the one that counts. This lesson uses 13% throughout.

## Tricks and shortcuts

For tax and tips, build the percent from 10% and 1%, as in the [percents lesson](../../02-middle-school/02-ratios-rates-percents/03-percents.md#tricks-and-shortcuts). On a \$42.60 bill:

| What | How to build it | Of \$42.60 |
|---|---|---|
| 10% | move the decimal point one place left | \$4.26 |
| 13% (the HST) | $10\% + 3 \times 1\%$, and 1% is \$0.426 | \$5.54 |
| 15% tip | $10\%$ plus half of it | \$6.39 |
| 18% tip | $20\% - 2\%$ | \$7.67 |
| 20% tip | double the 10% | \$8.52 |

Two Ontario-specific tricks use the tax line itself. The tax is 13% of the bill, so a bit more than the tax is a 15% tip: the tax plus a sixth of the tax is $13\% \times \frac{7}{6} \approx 15.2\%$. On this bill, $5.54 + 0.92 = 6.46$, close to the exact \$6.39. And to remove the tax in your head, multiply the total by 0.885, since $1 \div 1.13 = 0.88496\ldots$. For \$67.80, that is $67.80 \times 0.885 = 60.003$, about \$60.00.

To compare stacked discounts, use $d = a + b - ab$ for the single equivalent. For two discounts, subtract the product from the sum: 25% and 20% give $45\% - 5\% = 40\%$.

## In code

A short function can apply the discounts, the tax and the tip, with Python's `decimal` module so the cents are exact. It rounds once, at the end.

<details class="code" markdown>
<summary>In code</summary>

```python
from decimal import Decimal as D, ROUND_HALF_UP

def cents(x):
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)

def checkout(price, discounts=(), tip=D("0"), hst=D("0.13")):
    p = D(price)
    for d in discounts:
        p *= 1 - D(d)              # each discount is a percent of the current price
    tax = p * hst
    tip_amount = p * D(tip)        # tip on the pre-tax price
    return cents(p), cents(tax), cents(tip_amount), cents(p + tax + tip_amount)

def pre_tax(total, hst=D("0.13")):
    return cents(D(total) / (1 + hst))

print(checkout("80", ["0.20", "0.10"]))   # (57.60, 7.49, 0.00, 65.09)
print(checkout("42.60", tip="0.15"))      # (42.60, 5.54, 6.39, 54.53)
print(pre_tax("67.80"))                   # 60.00
```

Writing the numbers as strings keeps `Decimal` exact, which a float like `0.1` is not. The first line is Example 1, the second is the third Quick check problem, and the third is the second one.

</details>

## FAQ

### Why do prices in Ontario not include the tax?

Prices on a tag or menu are shown before tax, and the tax is added at the till. The tax is calculated on the price, so any percent discount takes effect first. The practical result is that the number you compare is the pre-tax price, and you multiply by 1.13 only once, at the end.

### Does the order of discount and tax matter?

For percents, no. Both are multiplications, so $80 \times 0.80 \times 0.90 \times 1.13$ gives the same total in any order. For a fixed-dollar coupon it does matter, as Example 4 showed: a coupon taken off before tax also saves you 13% of its value in tax.

### Should I tip on the price before tax or after?

That is a choice and not a rule of arithmetic. Tipping on the pre-tax amount is common, and tipping on the total gives a tip that is 13% bigger. The difference on a \$42.60 bill at 15% is $0.13 \times 6.39 = 0.83$, 83 cents. What matters is that you know which one you picked.

### Why can't I just add the two discounts?

Because the second one is taken from a price that has already dropped. The theorem above shows the exact result, $a + b - ab$. The error is small for small discounts, since $ab$ is small, and large for big ones.

## Practice

### Warm-up

1\. A pair of earbuds costs \$38.40 before tax. Find the federal part (5%), the provincial part (8%), the total HST and the total price.

<details class="solution" markdown>
<summary>Solution</summary>

The federal part is $0.05 \times 38.40 = 1.92$ dollars. The provincial part is $0.08 \times 38.40 = 3.072$, about \$3.07. The HST is $0.13 \times 38.40 = 4.992$, about \$4.99, and the total is $1.13 \times 38.40 = 43.392$, about \$43.39.

Check: $1.92 + 3.07 = 4.99$, and $38.40 + 4.99 = 43.39$.

</details>

2\. A dinner bill is \$58 before tax. Without a calculator, find a 15% tip and a 20% tip on the pre-tax amount.

<details class="solution" markdown>
<summary>Solution</summary>

Ten percent of \$58 is \$5.80. For 15%, add half of that: $5.80 + 2.90 = 8.70$, so \$8.70. For 20%, double it: \$11.60.

Check: $0.15 \times 58 = 8.7$ and $0.20 \times 58 = 11.6$.

</details>

3\. A receipt total with HST is \$90.40. What was the price before tax, and how much was the tax?

<details class="solution" markdown>
<summary>Solution</summary>

The total is 113% of the price, so the price is $90.40 \div 1.13 = 80$, that is, \$80.00. The tax is $90.40 - 80.00 = 10.40$ dollars.

Check: $0.13 \times 80 = 10.40$, and the mental trick agrees: $90.40 \times 0.885 = 80.004$, about 80.

</details>

### Standard

4\. A \$120 jacket is 30% off, and the register takes an extra 15% off the sale price. (a) What is the total with HST? (b) What single discount is equivalent to the two? (c) How much more does the shopper pay than with a flat 45% off?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $120 \times 0.70 \times 0.85 = 71.40$ before tax, and $71.40 \times 1.13 = 80.682$, so \$80.68.

(b) By the theorem, $d = 0.30 + 0.15 - 0.30 \times 0.15 = 0.45 - 0.045 = 0.405$, a 40.5% discount.

(c) A flat 45% off leaves $0.55 \times 120 = 66.00$ before tax. The stacked price is \$71.40, which is \$5.40 more before tax, or about \$6.10 more with HST ($5.40 \times 1.13 = 6.102$).

Check: $0.595 \times 120 = 71.40$, and $1 - 0.405 = 0.595$.

</details>

5\. Your pre-tax dinner bill is \$64.00 and you tip 18%. (a) What is the total if the tip is on the pre-tax bill? (b) What is it if the tip is on the tax-included bill? (c) What pre-tax rate is the second tip equal to?

<details class="solution" markdown>
<summary>Solution</summary>

The HST is $0.13 \times 64 = 8.32$, so the tax-included bill is \$72.32.

(a) The tip is $0.18 \times 64 = 11.52$, and the total is $72.32 + 11.52 = 83.84$ dollars.

(b) The tip is $0.18 \times 72.32 = 13.0176$, about \$13.02, and the total is $72.32 + 13.02 = 85.34$ dollars. That is \$1.50 more than in (a).

(c) The tip as a rate of the pre-tax bill is $0.18 \times 1.13 = 0.2034$, which is 20.34%.

Check: $13.02 \div 64 = 0.2034$, and $11.52 \times 1.13 = 13.0176$.

</details>

6\. You paid a total of \$103.96, which included 13% HST on the food and a 15% tip on the tax-included amount. What was the food price before tax?

<details class="solution" markdown>
<summary>Solution</summary>

The tax-included amount is 1.13 times the food price $p$. The tip is 15% of that, so the total is $1.13p \times 1.15 = 1.2995p$. The food price is the whole:

$$
p = 103.96 \div 1.2995 = 80.0
$$

so the food cost \$80.00.

Check: $80 \times 1.13 = 90.40$, the tip is $0.15 \times 90.40 = 13.56$, and $90.40 + 13.56 = 103.96$.

</details>

### Challenge

7\. A store advertises "an extra 20% off already-reduced prices". What first discount would make the final price exactly half the tag price? Use the theorem, then check with a \$200 item.

<details class="solution" markdown>
<summary>Solution</summary>

Let the first discount be $x$. The extra 20% has multiplier 0.80, and the final multiplier should be 0.50, so $(1 - x) \times 0.80 = 0.50$. Then $1 - x = 0.625$, and $x = 0.375$: the first discount must be 37.5%.

Using the theorem, $d = x + 0.20 - 0.20x = 0.5$ gives $0.8x = 0.3$, so $x = 0.375$. It agrees.

Check: a \$200 item at 37.5% off costs $200 \times 0.625 = 125$ dollars, and 20% off \$125 is $125 \times 0.80 = 100$ dollars, half of \$200.

</details>

8\. (Reviews [percent change](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).) A video game goes from \$59.99 to \$69.99 before tax. (a) What is the percent increase in the tag price? (b) What does each version cost with HST? (c) Is the increase after tax the same percent?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The change is $69.99 - 59.99 = 10.00$, and $10.00 \div 59.99 = 0.1667$, so the tag price rose about 16.7%.

(b) With HST, $59.99 \times 1.13 = 67.7887$, so \$67.79, and $69.99 \times 1.13 = 79.0887$, so \$79.09.

(c) Yes. Both prices are multiplied by 1.13, which cancels in the ratio: $79.0887 \div 67.7887 = 69.99 \div 59.99$. The dollar increase grows from \$10.00 to \$11.30, but the percent stays 16.7%.

Check: $79.09 - 67.79 = 11.30 = 10 \times 1.13$, and $11.30 \div 67.79 = 0.1667$.

</details>

## Where this shows up

- The next lesson, [unit price and comparison shopping](02-unit-price-and-comparison-shopping.md), turns "buy 2 get 1 free" and percent-off deals into price per unit. After it, [paycheques and budgeting](03-paycheques-and-budgeting.md) takes the same multiplier thinking to the other side of the till, the pay you earn.
- A chain of multipliers is also how [compound interest](../02-interest-and-growth/02-compound-interest.md) works, and the "tax-included total divided by 1.13" move is the same one that removes inflation from a price ([inflation and real returns](../02-interest-and-growth/06-inflation-and-real-returns.md)).
- In software, an e-commerce checkout is exactly the `checkout` function above, and the one-cent rounding gap of Example 3 is why money code stores amounts in whole cents and rounds once. Economists call the tax a wedge between the price the buyer pays and the price the seller keeps ([surplus and market interventions](../../07-economics-math/02-markets/04-surplus-and-market-interventions.md)).
