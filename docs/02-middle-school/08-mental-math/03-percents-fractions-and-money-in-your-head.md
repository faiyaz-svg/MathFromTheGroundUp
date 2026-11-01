# Percents, fractions and money in your head

After this lesson you can take 13% HST off a total in your head, combine discounts and round trips, work out a tip and a bill split, compare unit prices, use fractions such as $\frac{1}{6}$ and $\frac{1}{7}$ as percents, and estimate a currency conversion and a doubling time.

Before this: [ratios and unit rates](../02-ratios-rates-percents/01-ratios-and-unit-rates.md), [percents](../02-ratios-rates-percents/03-percents.md), [percent change and applications](../02-ratios-rates-percents/04-percent-change-and-applications.md), [multiplying and dividing fractions](../../01-elementary/11-multiplying-and-dividing-fractions.md) and [Mental multiplication and division](02-mental-multiplication-and-division.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A restaurant total is \$84.75, including 13% HST. What was the price before tax?
2. An \$80 jacket is 20% off, and then 10% off the sale price. What single discount is that, and what do you pay before tax?
3. A price rises 25% and then falls 20%. What is the net change? Also write $\frac{5}{6}$ as a percent.

<details class="solution" markdown>
<summary>Answers</summary>

1. The total is 113% of the price, so the tax is $\frac{13}{113}$ of the total, about 11.5%. Take that off: 10% of \$84.75 is \$8.48, 1% is \$0.85 and half a percent is \$0.42, which add to \$9.75, and $84.75 - 9.75 = 75.00$. The price was \$75.00. Check going forward: 13% of 75 is $7.50 + 2.25 = 9.75$, and $75 + 9.75 = 84.75$.
2. The multipliers are 0.8 and 0.9, and $0.8 \times 0.9 = 0.72$, so it is 28% off, not 30%. You pay $80 \times 0.72 = 57.60$, that is, \$57.60. In steps, $80 - 16 = 64$, then $64 - 6.40 = 57.60$.
3. $1.25 \times 0.8 = 1$, so the price is back where it started and the net change is 0%. And $\frac{5}{6} = 1 - \frac{1}{6}$, which is $100\% - 16.7\% = 83.3\%$.

</details>

## The idea

The receipt says \$84.75, tax included, and you want the price of the meal. The [percents lesson](../02-ratios-rates-percents/03-percents.md#tricks-and-shortcuts) has a table that builds a percent of a number from 10%, 1% and a half. That table answers "what is 13% of \$46?". This lesson starts where it stops, with the harder questions that come up at a till or in a bank statement.

It uses two tools. The first is the multiplier. A 13% tax multiplies by 1.13, a 20% discount multiplies by 0.8 and a doubling multiplies by 2. Undoing a change divides by its multiplier, and a chain of changes multiplies the multipliers. The second tool is the friendly fraction. A multiplier or a share is easy to handle in your head when it is close to a fraction you know, such as a quarter, an eighth or a ninth. Most of the tricks below find the friendly fraction that sits behind an awkward percent, and each says in one line why it works.

## Definitions

A **reverse percent** problem gives the result of a percent change and asks for the amount before the change. If the new amount is $\text{new} = (1 + r)\,\text{old}$, with $r$ the rate as a decimal, then

$$
\text{old} = \frac{\text{new}}{1 + r}.
$$

In plain words, divide by the multiplier. The receipt total \$84.75 came from the price times 1.13, so the price is $84.75 \div 1.13$.

A **round trip** is a change followed by a second change that returns to the starting amount. With rates $r$ and $s$ as decimals, that happens exactly when $(1 + r)(1 + s) = 1$. In plain words, the two multipliers cancel: a rise of 25% and a fall of 20% is a round trip, since $1.25 \times 0.8 = 1$.

A **benchmark fraction** is a fraction whose decimal and percent forms you know by heart, so that nearby values can be found from it. In plain words, it is a fraction you can use as a ruler: knowing that $\frac{1}{8} = 12.5\%$ tells you that 13% is a little more than an eighth.

## How to do it

### Percents past the table

Three more building blocks cover most of the percents the earlier table doesn't: a quarter of 10% is 2.5%, an eighth of an amount is 12.5%, and a percent below 100% can be built by taking away from the whole. Here they are on \$48.

| Percent | How to build it | Of \$48 |
|---|---|---|
| $2.5\%$ | a quarter of 10% | \$1.20 |
| $7.5\%$ | $5\% + 2.5\%$ | \$3.60 |
| $12.5\%$ | an eighth of the amount | \$6.00 |
| $17.5\%$ | $20\% - 2.5\%$ | \$8.40 |
| $35\%$ | $25\% + 10\%$ | \$16.80 |
| $90\%$ | the amount minus 10% | \$43.20 |
| $0.5\%$ | half of 1% | \$0.24 |

Why it works: the percent of a number adds and subtracts like the percents themselves, because $(a + b)\%$ of $n$ equals $a\%$ of $n$ plus $b\%$ of $n$, by the distributive property.

### Undoing a percent change

1. Write the multiplier of the change: 13% tax is $\times 1.13$.
2. Undo it by division, never by subtracting the same percent. The quick way to divide by 1.13 is to take off the share of the total that the tax makes up, which is $\frac{13}{113}$, about 11.5%: that is 10% plus 1% plus half a percent of the total.
3. For the exact cent, guess a price, add the tax going forward and adjust by the gap.
4. Check by going forward: the price times 1.13 should be the total.

Why it works: the total is 113 parts, 100 of them price and 13 of them tax, so the tax is $\frac{13}{113}$ of the total. Taking 13% of the total takes off too much, because the total is bigger than the price. The shares for common rates are these:

| Added | Multiplier | Share of the total to take off |
|---|---|---|
| 5% (GST) | 1.05 | $\frac{1}{21}$, about 4.8% |
| 10% | 1.1 | $\frac{1}{11}$, about 9.1% |
| 13% (HST) | 1.13 | $\frac{13}{113}$, about 11.5% |
| 15% | 1.15 | $\frac{3}{23}$, about 13.0% |
| 20% | 1.2 | $\frac{1}{6}$, about 16.7% |
| 25% | 1.25 | $\frac{1}{5}$, 20% |
| 50% | 1.5 | $\frac{1}{3}$, about 33.3% |

A discount is undone the same way, and the fractions make it quick. A 25% discount leaves three quarters of the price, so one quarter is a third of the sale price, and the original is the sale price plus a third of it: \$60 becomes $60 + 20 = 80$.

| Discount | The sale price is | To get the original |
|---|---|---|
| 10% off | $\frac{9}{10}$ of it | add a ninth of the sale price |
| 20% off | $\frac{4}{5}$ of it | add a quarter |
| 25% off | $\frac{3}{4}$ of it | add a third |
| 50% off | half of it | double it |

### Changes in a row

1. Turn each change into a multiplier, or take each off the amount left by the one before.
2. Multiply the multipliers, or carry the amount through.
3. Read the result as a percent: $1 - \text{product}$ is the discount, and $\text{product} - 1$ is the rise.

Why it works: a chain of percent changes is a product of multipliers, and the products are easy when the multipliers are friendly. For a discount of 20% and then 10%, go $100 \to 80 \to 72$: the second discount takes 10% of 80, not of 100, so the result is 28% off. Three discounts of 20%, 10% and 5% give $0.8 \times 0.9 \times 0.95 = 0.684$, or 31.6% off. The exact rule for two discounts is in [tips, discounts and HST](../../08-financial-math/01-everyday-money/01-tips-discounts-and-hst.md#two-discounts-in-a-row).

A rise of $r$ followed by a fall of $r$ doesn't cancel. It multiplies by $(1 + r)(1 - r) = 1 - r^2$, the difference of squares from the last lesson. A 10% rise and a 10% fall leave $1 - 0.01 = 0.99$, so you lose 1%. At 20% you lose 4%, and at 50% you lose 25%. The loss is $r\%$ of $r\%$.

A round trip needs different percents. A rise of $\frac{1}{n}$ is undone by a fall of $\frac{1}{n+1}$, because

$$
\left(1 + \frac{1}{n}\right)\left(1 - \frac{1}{n + 1}\right) = \frac{n + 1}{n} \times \frac{n}{n + 1} = 1.
$$

| Rise | As a fraction | The fall that undoes it |
|---|---|---|
| 100% | $1$ | $\frac{1}{2}$, which is 50% |
| 50% | $\frac{1}{2}$ | $\frac{1}{3}$, about 33.3% |
| 25% | $\frac{1}{4}$ | $\frac{1}{5}$, which is 20% |
| 20% | $\frac{1}{5}$ | $\frac{1}{6}$, about 16.7% |
| 10% | $\frac{1}{10}$ | $\frac{1}{11}$, about 9.1% |

Read the table the other way for a fall: a fall of $\frac{1}{n}$ is undone by a rise of $\frac{1}{n - 1}$, so a 20% fall needs a 25% rise. A rise that isn't a fraction like $\frac{1}{n}$ is undone by dividing: a 30% rise is undone by a fall of $\frac{0.3}{1.3} = \frac{3}{13}$, about 23.1%.

### Tips and splitting a bill

1. Start from the subtotal, the amount before tax.
2. Build the tip percent from 10%, 5% and 1%: 15% is 10% plus half of it, 18% is 20% minus 2%, and 20% is double 10%.
3. Add the tax in the same way. The tax and the tip are percents of the same subtotal, so they add to a single multiplier.
4. To split, divide before multiplying when that is easier.

Why it works: with 13% tax and a 15% tip on the subtotal $s$, the bill is $s + 0.13s + 0.15s = 1.28s$. Dividing by the number of people $k$ and multiplying by 1.28 can go in either order, because $\frac{1.28s}{k} = 1.28 \times \frac{s}{k}$. For a \$86.00 subtotal split four ways, the share of the subtotal is \$21.50, and $1.28 \times 21.50 = 21.50 + 5.375 + 0.645 = 27.52$, a quarter and 3% on top. Four shares make \$110.08, which is $86 \times 1.28$.

The tax line is a ruler for the tip. The HST is 13% of the subtotal, so one and a half times the tax line is 19.5%, close to a 20% tip. The [tips lesson](../../08-financial-math/01-everyday-money/01-tips-discounts-and-hst.md#tricks-and-shortcuts) has a similar trick for 15%.

### Unit prices

1. Write the size in hundreds of grams (or hundreds of millilitres): 225 g is 2.25.
2. Divide the price by that number, using a friendly fraction for the division. Dividing by 2.25 is multiplying by $\frac{4}{9}$, dividing by 4.5 is multiplying by $\frac{2}{9}$, and dividing by 3.5 is multiplying by $\frac{2}{7}$.
3. Compare the unit prices. If they are close, scale one package to the other's size instead, as the [unit price lesson](../../08-financial-math/01-everyday-money/02-unit-price-and-comparison-shopping.md#tricks-and-shortcuts) shows.

Why it works: dividing by a fraction is multiplying by its reciprocal, and $2.25 = \frac{9}{4}$. For \$2.99 for 225 g, round the price to \$3: $3 \times \frac{4}{9} = \frac{4}{3}$, about \$1.33 per 100 g. The exact value is $2.99 \times \frac{4}{9} = 1.3289$, also \$1.33.

### Fractions as percents

The earlier table has $\frac{1}{2}$, $\frac{1}{3}$, $\frac{1}{4}$, $\frac{1}{5}$, $\frac{1}{8}$, $\frac{1}{10}$ and $\frac{1}{20}$. These extend it.

| Fraction | Decimal | Percent | How to remember it |
|---|---|---|---|
| $\frac{1}{6}$ | $0.1667$ | $16.7\%$ | half of $\frac{1}{3}$ |
| $\frac{1}{7}$ | $0.1429$ | $14.3\%$ | the digits 142857 repeat |
| $\frac{1}{9}$ | $0.1111$ | $11.1\%$ | a third of $\frac{1}{3}$ |
| $\frac{1}{11}$ | $0.0909$ | $9.1\%$ | $11 \times 9 = 99$ |
| $\frac{1}{12}$ | $0.0833$ | $8.3\%$ | half of $\frac{1}{6}$ |
| $\frac{3}{8}$ | $0.375$ | $37.5\%$ | three times 12.5% |
| $\frac{5}{8}$ | $0.625$ | $62.5\%$ | five times 12.5% |
| $\frac{7}{8}$ | $0.875$ | $87.5\%$ | 100% minus 12.5% |

Why they work: dividing $33.3\%$ by 2, by 3 and by 4 gives $\frac{1}{6}$, $\frac{1}{9}$ and $\frac{1}{12}$. The repeating blocks come from the factors of 99 and 999,999, as in [repeating decimals](../01-integers-and-rational-numbers/03-rational-number-arithmetic.md): $99 = 9 \times 11$ and $999{,}999 = 7 \times 142{,}857$. So $\frac{n}{11} = \frac{9n}{99}$, and the repeating block is $9n$ written with two digits: $\frac{3}{11} = \frac{27}{99} = 0.2727\ldots$ Every ninth repeats one digit, $\frac{4}{9} = 0.444\ldots$, and every seventh uses the same six digits in a rotated order: $\frac{2}{7} = 0.2857\ldots$ and $\frac{5}{7} = 0.7142\ldots$.

To find a fraction of an amount, divide by the denominator and multiply by the numerator: $\frac{5}{9}$ of 72 is $5 \times 8 = 40$, and $\frac{1}{12}$ of a \$62,400 salary is \$5,200 a month.

### Currency at a round rate

1. Round the exchange rate to a friendly number, such as 1.40, 1.25 or 1.50 Canadian dollars for one US dollar.
2. To go from US to Canadian dollars, multiply by the rate. A rate of 1.40 means adding four tenths, a rate of 1.25 means adding a quarter and a rate of 1.50 means adding half.
3. To go back, undo the rise with the round-trip table: after adding a quarter, take off a fifth; after adding half, take off a third; after adding four tenths, take off two sevenths.
4. Check by converting back.

Why it works: a rate of $1 + \frac{1}{n}$ is a rise of $\frac{1}{n}$, and the round-trip rule gives the way back. At 1.40, USD 35 is $35 + 14 = 49$ Canadian dollars, and CAD 49 goes back to $49 \times \frac{5}{7} = 35$. At 1.25, CAD 90 is $90 - 18 = 72$ US dollars.

The rate 1.40 here is an example chosen to be round, not a quote. Look up the current rate before relying on a conversion, and expect a card or an exchange counter to add a fee.

### Doubling time and the rule of 72

1. Write the rate as a number of percent, $R$: 6% is $R = 6$, not 0.06.
2. Divide 72 by $R$. The answer is the doubling time in the same periods as the rate. The numbers 2, 3, 4, 6, 8, 9 and 12 divide 72, so those are exact: $\frac{72}{6} = 12$ years.
3. For another rate, use a nearby rate that divides 72, or a benchmark fraction: $72 \times \frac{1}{7} = 10.3$ years at 7%.
4. To find the rate that doubles money in $N$ years, divide 72 by $N$. For a quadrupling, which is two doublings, use 144 instead of 72.

Why it works: the exact doubling time is $\frac{\ln 2}{\ln(1 + r)}$, which is a little over $\frac{69.3}{R}$, and 72 is close to that and has many divisors. The lesson on [doubling time, the rule of 72 and logs](../../08-financial-math/02-interest-and-growth/05-doubling-time-rule-of-72-and-logs.md) proves this and shows how the error grows with $R$.

| Rate $R$ | 2 | 3 | 4 | 6 | 7 | 8 | 9 | 12 |
|---|---|---|---|---|---|---|---|---|
| $\frac{72}{R}$ | 36 | 24 | 18 | 12 | 10.3 | 9 | 8 | 6 |
| exact years | 35.0 | 23.4 | 17.7 | 11.9 | 10.2 | 9.0 | 8.0 | 6.1 |

## Worked examples

<div class="example" markdown>

### Example 1: the price before tax

A receipt shows a total of \$72.41, including 13% HST. What was the price before tax?

Step 1: the multiplier is 1.13, so the total is 113% of the price.

Step 2: take off the tax's share of the total, about 11.5%. Ten percent of \$72.41 is \$7.24, 1% is \$0.72 and half a percent is \$0.36, which add to \$8.32. Then $72.41 - 8.32 = 64.09$, so the price is about \$64.09.

Step 3: for the exact cent, guess \$64 and go forward. The tax on \$64 is $6.40 + 1.92 = 8.32$ (10% plus 3%), so the total would be \$72.32. The real total is 9 cents more, and 9 cents divided by 1.13 is about 8 cents, so the price is \$64.08.

Step 4: check going forward: $64.08 \times 1.13 = 72.41$, to the cent. The two methods agree to within a cent, and the exact value is $72.41 \div 1.13 = 64.0796\ldots$

<div class="warning" markdown>

Watch out: subtracting 13% of the total gives $72.41 - 9.41 = 63.00$, which is \$1.08 too low. Going forward shows it: $63.00 \times 1.13 = 71.19$, not 72.41. The tax is 13% of the price, so it is only about 11.5% of the total.

</div>

</div>

<div class="example" markdown>

### Example 2: stacked discounts, tax and a round trip

A \$150 jacket is 20% off, then an extra 10% off, and then 13% HST is added. What is the final price? Then, a share price rises 25% in one quarter and falls 25% in the next: where does it end?

Take off 20%: $150 - 30 = 120$. Take 10% off that: $120 - 12 = 108$. The single discount is $150 - 108 = 42$, which is 28% of 150, not 30%.

The HST on \$108 is $10.80 + 3.24 = 14.04$ (10% plus 3 times 1%), so the total is $108 + 14.04 = 122.04$, that is, \$122.04. Check with multipliers: $150 \times 0.72 \times 1.13 = 122.04$.

For the share price, a 25% fall is not the undo of a 25% rise. Starting at 100, it goes to 125 and then to $125 \times 0.75 = 93.75$, which is 6.25% below the start. The fall that undoes a rise of $\frac{1}{4}$ is $\frac{1}{5}$, which is 20%: $125 \times 0.8 = 100$.

</div>

<div class="example" markdown>

### Example 3: a dinner for three

The subtotal is \$92.00. HST is 13% and the tip is 15%, both on the subtotal, and three people split the bill. How much does each pay?

Ten percent of 92 is 9.20, and 1% is 0.92. The HST is $9.20 + 3 \times 0.92 = 9.20 + 2.76 = 11.96$. The tip is $9.20 + 4.60 = 13.80$. The total is $92 + 11.96 + 13.80 = 117.76$.

Check with one multiplier: $92 \times 1.28 = 92 + 23 + 2.76 = 117.76$, where 23 is a quarter of 92 and 2.76 is 3%.

Now divide by 3: $117.76 \div 3 = 39.2533\ldots$ The bill doesn't split evenly in cents. Two people can pay \$39.25 and one \$39.26, which adds to \$117.76. Or each pays \$39.26 and the table leaves 2 cents extra, which is fine for a tip. An untidy division like this is normal.

</div>

<div class="example" markdown>

### Example 4: which bag is cheaper (finish it yourself)

A 450 g bag of rice costs \$3.49 and a 650 g bag costs \$5.20. Which is cheaper per 100 g?

Step 1: 450 g is 4.5 hundreds of grams, and 650 g is 6.5. For the big bag, $5.20 \div 6.5 = 0.80$, because $6.5 \times 0.8 = 5.2$, so it costs \$0.80 per 100 g.

Step 2: dividing by 4.5 is multiplying by $\frac{2}{9}$. The first part, $3.49 \times 2 = 6.98$, is done.

Now divide 6.98 by 9, compare the two unit prices, and check with the scaling trick.

<details class="solution" markdown>
<summary>Finish</summary>

$6.98 \div 9 = 0.7755\ldots$, about \$0.78 per 100 g. That is under \$0.80, so the 450 g bag is cheaper per 100 g, by about 2 cents.

Check by scaling: 650 g is $\frac{13}{9}$ of 450 g, so 650 g of the small bag's rice would cost $3.49 \times \frac{13}{9} = 5.04$, about \$5.04. The big bag costs \$5.20, which is more, so the small bag is cheaper.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for undoing a percent with the same percent. Taking 13% off a \$113 total leaves \$98.31, but the price was \$100. The mistake is only 1.7% of the price, so it looks harmless, and it grows with the total. Divide by 1.13 or take off 11.5%.

</div>

<div class="warning" markdown>

Watch out for adding discounts. Twenty percent off and then 10% off is 28% off, not 30%, because the second discount is taken from a price that is already lower. For a long chain, multiply the multipliers.

</div>

<div class="warning" markdown>

Watch out for the direction of a currency conversion. At 1.40 Canadian dollars per US dollar, a US dollar is worth more, so the same price is a bigger number in Canadian dollars and a smaller number in US dollars. Converting CAD 49 by multiplying gives USD 68.6, which is more US dollars than Canadian ones. The right answer is USD 35.

</div>

<div class="warning" markdown>

Watch out for the rate in the rule of 72. For 6%, use $R = 6$. Using 0.06 gives $\frac{72}{0.06} = 1{,}200$ years. The rule also loses accuracy at high rates: at 50% it says 1.44 periods, while the exact time is 1.71. Use it for rates up to about 15%, where it is off by about 3%.

</div>

A unit price needs the right place value. For 450 g, the size is 4.5 hundreds, not 45. A quick size check helps: a pack over 100 g must cost less per 100 g than the pack itself.

## Tricks and shortcuts

The HST rate of 13% is a hair over an eighth, which is 12.5%. So adding HST is about adding an eighth, and the round-trip rule says that undoing it is about taking off a ninth. For \$84.75, a ninth is \$9.42 and $84.75 - 9.42 = 75.33$. That is within half a percent of the exact \$75.00, and quick enough for a menu.

A 20% tip is about one and a half times the tax line, and a 15% tip is the tax line plus a sixth of it. Both land within 3% of the exact tip.

To estimate how long a steady growth takes to multiply by 4, double the doubling time. Prices rising 3% a year double in about $\frac{72}{3} = 24$ years and quadruple in about 48. A service whose traffic grows 12% a month doubles in about 6 months.

## In code

The generator makes tax, tip and reverse-tax problems, and the checker accepts an answer within 1% because a mental answer is approximate. It uses `random.Random(4)`, so the six problems are the same on every run. To practise with your own typing, call `quiz(make_problems(4))` with no `replies`.

<details class="code" markdown>
<summary>In code</summary>

```python
import random

def make_problems(seed, n=6):
    rng = random.Random(seed)
    problems = []
    for _ in range(n):
        price = rng.randint(20, 150)
        kind = rng.choice(["tax", "tip", "undo"])
        if kind == "undo":
            problems.append((f"price before tax when the total is ${price * 1.13:.2f}", price))
        else:
            rate = 0.13 if kind == "tax" else 0.18
            problems.append((f"{kind} at {rate:.0%} on ${price}", price * rate))
    return problems

def quiz(problems, replies=None, tolerance=0.01):
    score = 0
    for i, (text, answer) in enumerate(problems):
        reply = float(replies[i] if replies else input(f"{text}? "))
        close = abs(reply - answer) <= tolerance * answer
        score += close
        print(f"{text}: {reply:g}", "close enough" if close else "too far", f"(exact {answer:.2f})")
    print(f"score: {score} out of {len(problems)}")

quiz(make_problems(seed=4), replies=[14.4, 45.2, 21.8, 7.7, 4.8, 122.5])
```

The run prints this. The second reply, 45.2, is the slip of taking 13% off the total, and the 1% tolerance catches it. The last reply, 122.5, comes from the "take off a ninth" trick, and it passes.

```text
tip at 18% on $80: 14.4 close enough (exact 14.40)
price before tax when the total is $51.98: 45.2 too far (exact 46.00)
tip at 18% on $121: 21.8 close enough (exact 21.78)
tax at 13% on $59: 7.7 close enough (exact 7.67)
tax at 13% on $37: 4.8 close enough (exact 4.81)
price before tax when the total is $137.86: 122.5 close enough (exact 122.00)
score: 5 out of 6
```

</details>

## FAQ

### Why is a rise of a quarter undone by a fall of a fifth?

A rise of a quarter turns 4 parts into 5 parts. To get back from 5 parts to 4, you remove 1 part out of 5, which is a fifth. The fall is measured against the new, bigger amount, so it is a smaller fraction than the rise. In general, a rise of $\frac{1}{n}$ turns $n$ parts into $n + 1$, and the way back removes 1 part of $n + 1$.

### How accurate should a mental answer be?

It depends on the use. For a tip, the nearest 10 cents is enough. For a check on a calculation or an estimate of a price, within 1% to 2% is a good target. For any amount you will pay, sign or file, work it out exactly, on paper or with a calculator, and use the mental answer as the check.

### Is the rule of 72 only for interest?

No. It works for any quantity that grows by the same percent each period, such as prices under steady inflation, a population, a data volume or a debt left unpaid. The percent must be steady, and the period of the rate must match the period you want the answer in: a rate per month gives a time in months.

## Practice

### Warm-up

1\. Find (a) 2.5% of \$80, (b) 12.5% of \$72, (c) 17.5% of \$40, (d) 35% of \$60.

<details class="solution" markdown>
<summary>Solution</summary>

(a) 10% of 80 is 8, and a quarter of that is 2: \$2.00.

(b) An eighth of 72 is 9: \$9.00.

(c) $20\% - 2.5\%$ of 40 is $8 - 1 = 7$: \$7.00.

(d) $25\% + 10\%$ of 60 is $15 + 6 = 21$: \$21.00.

Check by multiplying: $0.025 \times 80 = 2$, $0.125 \times 72 = 9$, $0.175 \times 40 = 7$ and $0.35 \times 60 = 21$.

</details>

2\. (a) Write $\frac{5}{6}$, $\frac{4}{7}$ and $\frac{5}{11}$ as percents. (b) Find $\frac{1}{12}$ of \$62,400 and $\frac{5}{9}$ of 72.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\frac{5}{6} = 1 - \frac{1}{6} = 100\% - 16.7\% = 83.3\%$. For $\frac{4}{7}$, four times 14.3% is 57.1%. For $\frac{5}{11}$, five times 9.1% is 45.5%.

(b) $62{,}400 \div 12 = 5{,}200$, so \$5,200. And $72 \div 9 = 8$, so $\frac{5}{9}$ of 72 is $5 \times 8 = 40$.

Check: $\frac{5}{6} + \frac{1}{6} = 1$, and $83.3\% + 16.7\% = 100\%$. Also $4 \div 7 = 0.5714$, $5 \div 11 = 0.4545$ and $12 \times 5{,}200 = 62{,}400$.

</details>

3\. A receipt total with 13% HST is \$58.90. Estimate the price before tax in your head, and then give it to the cent.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate: take off about 11.5%. Ten percent of \$58.90 is \$5.89, 1% is \$0.59 and half a percent is \$0.29, which add to \$6.77. So the price is about $58.90 - 6.77 = 52.13$.

To the cent: guess \$52. The tax is $5.20 + 1.56 = 6.76$, so the total would be \$58.76. The real total is 14 cents more, and $0.14 \div 1.13$ is about 12 cents. So the price is \$52.12.

Check: $52.12 \times 1.13 = 58.8956$, which rounds to \$58.90. Taking 13% off the total instead would give \$51.24, which is 88 cents too low.

</details>

### Standard

4\. A \$240 coat is 25% off, then an extra 10% off, and then 13% HST is added. (a) What single discount matches the two discounts? (b) What is the final price?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The multipliers are 0.75 and 0.9, and $0.75 \times 0.9 = 0.675$. So the single discount is $1 - 0.675 = 0.325$, which is 32.5% off, not 35%.

(b) Take 25% off: $240 - 60 = 180$. Take 10% off that: $180 - 18 = 162$. The HST is $16.20 + 4.86 = 21.06$ (10% plus 3 times 1%), so the total is $162 + 21.06 = 183.06$, that is, \$183.06.

Check: $240 \times 0.675 = 162$ and $162 \times 1.13 = 183.06$.

</details>

5\. A dinner has a subtotal of \$128.00. The HST is 13% and the tip is 18%, both on the subtotal, and five people split the bill equally. How much does each person pay?

<details class="solution" markdown>
<summary>Solution</summary>

The multiplier is $1 + 0.13 + 0.18 = 1.31$. Divide first: $128 \div 5 = 25.60$ is each person's share of the subtotal. Then $1.31 \times 25.60 = 25.60 + 7.68 + 0.256 = 33.536$, where 7.68 is 30% of 25.60 and 0.256 is 1%.

Each person pays \$33.54 when rounding up to the cent.

Check: the whole bill is $1.31 \times 128 = 167.68$, from tax $16.64$ and tip $23.04$ added to 128, and $167.68 \div 5 = 33.536$. Five payments of \$33.54 make \$167.70, two cents over.

</details>

6\. (a) A 750 g jar of peanut butter costs \$6.49 and a 500 g jar costs \$4.49. Which is cheaper per 100 g? (b) At a rate of 1.40 Canadian dollars per US dollar, find the Canadian price of a USD 45 keyboard and the US price of a CAD 98 book.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Scale: 750 g is 1.5 times 500 g, and $1.5 \times 4.49 = 6.735$. The big jar costs \$6.49, which is less, so it is cheaper per gram. Per 100 g, $6.49 \div 7.5 = 0.865$ and $4.49 \div 5 = 0.898$, so about \$0.87 against \$0.90.

(b) The keyboard: adding four tenths of 45 gives $45 + 18 = 63$, so CAD 63. The book: take off two sevenths, or divide by 7 and multiply by 5: $98 \div 7 = 14$ and $14 \times 5 = 70$, so USD 70.

Check: $7.5 \times 0.865 = 6.49$. And $70 \times 1.4 = 98$ and $63 \div 1.4 = 45$.

</details>

### Challenge

7\. (a) Prove that a rise of $\frac{1}{n}$ followed by a fall of $\frac{1}{n + 1}$ returns to the start. (b) What fall undoes a rise of 12.5%? (c) What fall undoes a rise of 30%?

<details class="solution" markdown>
<summary>Solution</summary>

(a) What we know: a rise of $\frac{1}{n}$ multiplies by $1 + \frac{1}{n} = \frac{n + 1}{n}$, and a fall of $\frac{1}{n + 1}$ multiplies by $1 - \frac{1}{n + 1} = \frac{n}{n + 1}$. What we want: the product of the two multipliers. The product is $\frac{n + 1}{n} \times \frac{n}{n + 1} = 1$, so the amount is unchanged. $\blacksquare$

(b) Since $12.5\% = \frac{1}{8}$, the fall is $\frac{1}{9}$, about 11.1%.

(c) A rise of 30% is $\frac{3}{10}$, which isn't of the form $\frac{1}{n}$, so divide: the multiplier is 1.3, and the fall is $\frac{0.3}{1.3} = \frac{3}{13}$, about 23.1%.

Check: $1.125 \times \frac{8}{9} = 1$ and $1.3 \times \frac{10}{13} = 1$.

</details>

8\. (Reviews [exponent rules](../04-powers-roots-and-real-numbers/01-exponent-rules.md).) You invest \$2,000 at 6% a year, compounded yearly. (a) Use the rule of 72 for the doubling time. (b) Estimate the value after 36 years by counting doublings. (c) The exact value is $2000 \times 1.06^{36}$. How far off is the estimate?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\frac{72}{6} = 12$ years.

(b) 36 years is 3 doublings, so the value is about $2{,}000 \times 2^3 = 16{,}000$ dollars.

(c) The exact value is $2000 \times 1.06^{36} = 16{,}294.50$. The estimate is \$294.50 low, which is 1.8% of the exact value. The reason is that $1.06^{12} = 2.012$, a little more than 2, so each block of 12 years multiplies by slightly more than a doubling. By the power of a power rule, $1.06^{36} = (1.06^{12})^3 = 2.012^3 = 8.147$.

Check: $2{,}000 \times 8.147 = 16{,}294$, which matches the exact value to the dollar.

</details>

### Drill

Do these in your head. Open the answers afterwards and compare your method with the fastest one.

1. 15% of \$64
2. 2.5% of \$200
3. 12.5% of 96
4. 7.5% of 80
5. The price per 100 g of a 300 g pack that costs \$4.50
6. The price before 13% HST when the total is \$113.00
7. The price before 13% HST when the total is \$33.90
8. The price before a 25% discount, when the sale price is \$60
9. The single discount equal to 20% off and then 10% off
10. The net change after a rise of 20% and a fall of 20%
11. The fall that undoes a rise of 25%
12. $\frac{1}{6}$ of 84
13. $\frac{5}{9}$ of 72
14. $\frac{3}{8}$ as a percent
15. $\frac{1}{7}$ as a percent
16. USD 50 in Canadian dollars at 1.40
17. CAD 90 in US dollars at 1.25
18. The doubling time at 9% a year
19. The rate that doubles money in 6 years
20. \$87.60 split four ways

<details class="solution" markdown>
<summary>Answers and fastest tricks</summary>

1. \$9.60. A tenth is 6.40, and half of that is 3.20.
2. \$5.00. A tenth is 20, and a quarter of that is 5.
3. 12. An eighth of 96.
4. 6. A tenth is 8, half of that is 4 (5%), and a quarter of 8 is 2 (2.5%), so $4 + 2$.
5. \$1.50. A 300 g pack is 3 hundreds, so $4.50 \div 3$.
6. \$100.00. The total is 100 parts price plus 13 parts tax, so the price is 100.
7. \$30.00. Guess and check: $30 \times 1.13 = 33.90$.
8. \$80. Three quarters is 60, so add a third of 60: $60 + 20$.
9. 28%. Go $100 \to 80 \to 72$.
10. $-4\%$. $(1.2)(0.8) = 1 - 0.2^2 = 0.96$.
11. 20%. A rise of a quarter is undone by a fall of a fifth.
12. 14. $84 \div 6$.
13. 40. $72 \div 9 = 8$, and $5 \times 8$.
14. 37.5%. Three times 12.5%.
15. About 14.3%. The digits 142857 repeat.
16. CAD 70. Add four tenths: $50 + 20$.
17. USD 72. Take off a fifth, which is 18: $90 - 18$.
18. About 8 years. $72 \div 9$.
19. About 12%. $72 \div 6$.
20. \$21.90. Halve twice: 43.80, then 21.90.

</details>

## Where this shows up

- The financial math lessons use these numbers in full: [tips, discounts and HST](../../08-financial-math/01-everyday-money/01-tips-discounts-and-hst.md) proves the rule for stacked discounts, [unit price and comparison shopping](../../08-financial-math/01-everyday-money/02-unit-price-and-comparison-shopping.md) compares packages, and [doubling time, the rule of 72 and logs](../../08-financial-math/02-interest-and-growth/05-doubling-time-rule-of-72-and-logs.md) gives the exact time and the error of the rule.
- Economics reports growth and inflation as percents, and the rule of 72 turns a rate into a doubling time ([CPI and inflation](../../07-economics-math/01-measuring-the-economy/07-cpi-and-inflation.md)). A percent loss and a percent gain of the same size don't cancel, which is why a 50% fall in a share price needs a 100% rise to recover.
- In computing, growth in traffic, storage or cost is usually a steady percent per month, and the doubling time turns that rate into a date for a capacity plan. A cut of 20% in a cost, such as a cheaper server plan, is undone by a rise of 25%, so 25% growth in usage cancels the saving.
