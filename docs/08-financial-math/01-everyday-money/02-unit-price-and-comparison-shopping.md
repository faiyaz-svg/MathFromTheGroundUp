# Unit price and comparison shopping

After this lesson you can compare packages of different sizes and units by price per unit, turn deals such as "buy 2 get 1 free" into a unit price, see when buying in bulk stops paying off, and find how much you must spend for a store membership to be worth its fee.

Before this: [ratios and unit rates](../../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md), which introduced unit prices, and [tips, discounts and HST](01-tips-discounts-and-hst.md). A quick look at [estimation and sanity checks](../../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md) also helps, since most comparisons here can be checked by rounding.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A 500 g jar of peanut butter costs \$4.49 and a 1 kg jar costs \$7.99. Which has the lower price per 100 g?
2. A store sells a tin of soup for \$3.50, with "buy 2 get 1 free". What is the price per tin when you take the deal, and what percent discount is that?
3. A box of cereal goes from 450 g to 400 g, and the price stays at \$5.49. By what percent did the price per gram change?

<details class="solution" markdown>
<summary>Answers</summary>

1. The small jar is 5 lots of 100 g, so it costs $4.49 \div 5 = 0.898$, about \$0.90 per 100 g. The big jar is 10 lots, so $7.99 \div 10 = 0.799$, about \$0.80. The 1 kg jar is cheaper.
2. You pay for 2 tins and get 3, so the price per tin is $2 \times 3.50 \div 3 = 2.333\ldots$, about \$2.33. That is $\frac{1}{3}$ off, a 33.3% discount.
3. You get $\frac{400}{450} = 0.8889$ of the cereal for the same money, so each gram costs $\frac{450}{400} = 1.125$ times as much: a 12.5% increase.

</details>

## The idea

The two jars in the first Quick check problem have different prices and different sizes, so the tags alone don't say which is the better deal. A price compares nothing until you say per what. Dividing by the amount gives the price of one unit, and that number can be compared across any two products that are sold in the same kind of unit.

The method is the same as for any rate (see [ratios and unit rates](../../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions)). What this lesson adds is the money side: deals that hide a unit price inside a promotion, packages that shrink without notice, a bulk pack you can't finish, and a membership that charges a fee up front for lower prices later. Each one is a question about which number to divide by.

Two warnings run through the lesson. A lower unit price is only a saving if you use what you buy, and a lower unit price only matters if you would have bought the product anyway. The arithmetic is simple. Deciding what counts as the amount is where people go wrong.

## Definitions

The **unit price** of a product is its price divided by the quantity in the package, in a stated unit:

$$
\text{unit price} = \frac{\text{price}}{\text{quantity}}.
$$

In plain words, it is the cost of one unit, such as one kilogram, one litre or one item. Shelf labels often use 100 g or 100 mL as the unit, so that the numbers are not tiny. Two unit prices can be compared directly only when they use the same unit.

The **effective unit price** is the price divided by the quantity you actually use. If you throw out part of what you buy, the effective unit price is higher than the label's.

A **multi-buy deal** is an offer that sets the price for a group of items. "Buy $n$ get $m$ free" means you pay for $n$ items and get $n + m$ of them. The **effective discount** of a deal is the percent by which it lowers the price per item.

**Shrinkflation** is a package getting smaller while its price stays the same or rises, so the unit price goes up even though the tag did not move.

A **membership fee** is a yearly charge for the right to shop at a store, in return for lower prices. Its **break-even spending** is the amount of yearly spending at which the savings exactly equal the fee.

## How to do it

### Comparing unit prices

1. Write each price and quantity with units. A price of \$4.49 for 500 g is $\frac{4.49\ \text{dollars}}{500\ \text{g}}$.
2. Convert to one unit. Compare grams with grams, or kilograms with kilograms, and use the conversion facts from [measurement and unit conversion](../../01-elementary/15-measurement-and-unit-conversion.md): 1 kg is 1000 g, 1 L is 1000 mL, and 1 lb is 0.45359237 kg.
3. Divide the price by the quantity, with the price on top. The lower unit price is the cheaper product.
4. Round once, at the end, and compare with the unrounded numbers if two prices are close.
5. Check by scaling one package to the other's size, or with a rough estimate.
6. Ask whether the unit price is the real cost: how much will you use, and does the price include a deal or a limit?

A spreadsheet does Steps 2 and 3 for a whole list. Put the price in column B and the size in grams in column C, and type the formula `=B2/(C2/100)` in column D for the price per 100 g. The table shows four jars of peanut butter, with the rank by unit price in the last column:

| Jar | Price (B) | Size in g (C) | Price per 100 g (`=B2/(C2/100)`) | Rank |
|---|---|---|---|---|
| small | \$2.79 | 250 | \$1.1160 | 4 |
| medium | \$4.49 | 500 | \$0.8980 | 3 |
| large | \$7.99 | 1000 | \$0.7990 | 2 |
| jumbo | \$12.99 | 2000 | \$0.6495 | 1 |

Each jar costs less per gram than the one before it. The drop from the small jar to the medium one is about 20%, and from the large to the jumbo it is about 19%. More on spreadsheets in [spreadsheet finance functions and a capstone plan](../07-taxes-insurance-and-planning/03-spreadsheet-finance-functions-and-capstone.md).

### Deals as unit prices

A deal is only a price for a group, so divide it by the number of items. For "buy $n$ get $m$ free" on an item with price $p$, you pay $np$ for $n + m$ items, so

$$
\text{price per item} = \frac{np}{n + m}, \qquad \text{effective discount} = 1 - \frac{n}{n + m} = \frac{m}{n + m}.
$$

The discount is the free items as a fraction of all the items you take home. Some common deals:

| Deal | You pay for | You get | Effective discount |
|---|---|---|---|
| buy 1 get 1 free | 1 | 2 | $\frac{1}{2} = 50\%$ |
| buy 2 get 1 free | 2 | 3 | $\frac{1}{3} \approx 33.3\%$ |
| buy 3 get 1 free | 3 | 4 | $\frac{1}{4} = 25\%$ |
| buy 1 get 1 half off | 1.5 | 2 | $\frac{0.5}{2} = 25\%$ |
| 2 for \$5, when one costs \$2.99 | \$5 | 2 | $1 - \frac{2.50}{2.99} \approx 16.4\%$ |

The last row compares the deal price per item with the single price. A percent-off deal is the same kind of comparison with a multiplier: 20% off is $\times 0.80$. When two offers are on the same item, convert both to a price per item and compare. Read the fine print too: some deals need you to buy the full group, and some give the best price only at a set size.

### Bulk versus waste

A bigger package usually has a lower unit price, but it only saves money if you use it. If you use a fraction $u$ of what you buy (with $0 < u \le 1$), the effective unit price is the label's unit price divided by $u$. Suppose a big package has the lower label price per unit, and a small one has the higher label price per unit, call them $U_{\text{big}}$ and $U_{\text{small}}$. If you finish the small package and use only the fraction $u$ of the big one, the big package is cheaper per unit used when

$$
\frac{U_{\text{big}}}{u} < U_{\text{small}} \quad\Longleftrightarrow\quad u > \frac{U_{\text{big}}}{U_{\text{small}}}.
$$

So the break-even fraction is the ratio of the two unit prices. A 1 kg pack of cheese at \$4.99 is \$0.499 per 100 g, and a 400 g pack at \$2.49 is \$0.6225 per 100 g. The break-even fraction is $0.499 \div 0.6225 = 0.8016$. You have to use more than about 80% of the big pack for it to win, and if a fifth goes mouldy, the small pack is the better buy.

### Shrinkflation

If the price changes by a factor $f_P$ (the price multiplier) and the quantity by a factor $f_Q$, the unit price changes by the factor $f_P \div f_Q$. This follows from the definition of unit price: the new unit price is

$$
\frac{P'}{Q'} = \frac{f_P P}{f_Q Q} = \frac{f_P}{f_Q} \times \frac{P}{Q}.
$$

A package that goes from 450 g to 400 g at the same price has $f_P = 1$ and $f_Q = \frac{400}{450}$, so the unit price is multiplied by $\frac{450}{400} = 1.125$. Fewer grams for the same money is a 12.5% price rise per gram. This is the same calculation as the last practice problem of [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#practice).

### The break-even for a membership

Suppose a club charges a yearly fee $F$ and its prices on the goods you buy are lower than the regular store's by the fraction $s$ (so $s = 0.12$ means 12% lower). If you buy goods that cost $S$ dollars a year at the regular store, you save $sS$ at the club. The net gain after the fee is

$$
\text{net} = sS - F,
$$

and the break-even spending is where it is zero: $S^{*} = \frac{F}{s}$. Above $S^{*}$ the membership pays, and below it the fee costs you more than you save. Here $S$ is measured at the regular store's prices, because the saving is a fraction of that. The comparison is only fair when the club's goods are the same ones you already buy.

## Worked examples

<div class="example" markdown>

### Example 1: pounds against kilograms

A 2.5 kg bag of flour costs \$5.49. Another brand sells a 10 lb bag for \$8.99. Which has the lower unit price, and by how much per 100 g?

Step 1: the prices and quantities are $\frac{5.49\ \text{dollars}}{2.5\ \text{kg}}$ and $\frac{8.99\ \text{dollars}}{10\ \text{lb}}$.

Step 2: convert the second to kilograms. Since 1 lb is 0.45359237 kg, 10 lb is 4.5359237 kg.

Step 3: divide the price by the quantity:

$$
5.49 \div 2.5 = 2.196, \qquad 8.99 \div 4.5359237 = 1.9819\ldots
$$

These are dollars per kilogram. Divide by 10 for dollars per 100 g: \$0.2196 and \$0.1982.

Step 4: the 10 lb bag is cheaper, by about \$0.0214 per 100 g, or about 2.1 cents. It is about 9.7% cheaper per kilogram: $\frac{2.196 - 1.982}{2.196} = 0.0975$.

Step 5: check. A kilogram is about 2.2 lb, so 10 lb is about 4.5 kg. At the first bag's price, 4.5 kg would cost about $4.5 \times 2.196 = 9.88$ dollars, and the second bag costs \$8.99, so it is cheaper.

<div class="warning" markdown>

Watch out at Step 2: comparing 2.5 with 10 is the mistake. The bag with the larger number looks bigger but is not 4 times as big: 10 lb is only 1.8 times 2.5 kg. Convert first, then compare.

</div>

</div>

<div class="example" markdown>

### Example 2: a multi-buy deal against a bigger jar

A 640 mL jar of pasta sauce costs \$3.29. This week it is "buy 2 get 1 free". The store also sells a 1.5 L jar of the same sauce for \$5.49. Which is the better buy?

For the deal, you pay for 2 jars and get 3, so the price per jar is $\frac{2 \times 3.29}{3} = 2.1933\ldots$ dollars, and 3 jars hold $3 \times 640 = 1920$ mL, which is 19.2 lots of 100 mL. The unit price is $6.58 \div 19.2 = 0.3427\ldots$ dollars per 100 mL.

For the big jar, 1.5 L is 15 lots of 100 mL, so the unit price is $5.49 \div 15 = 0.366$ dollars per 100 mL.

The deal is cheaper, \$0.343 against \$0.366 per 100 mL, about 6.4% less. Without the deal, the small jar is $3.29 \div 6.4 = 0.514$ dollars per 100 mL, so the big jar would have won by a wide margin.

Check: three small jars hold 1.92 L, a bit more than one big jar, for \$6.58. At the big jar's price, 1.92 L would cost $1.92 \times 3.66 = 7.03$ dollars, which is more than \$6.58.

</div>

<div class="example" markdown>

### Example 3: shrinkflation, with the price going down

A bag of chips used to be 220 g for \$4.49. The store now sells 200 g for \$4.29. Is it cheaper or more expensive per gram?

The price multiplier is $\frac{4.29}{4.49} = 0.9555\ldots$, a 4.5% drop in the tag price. The quantity multiplier is $\frac{200}{220} = 0.9091$. The unit price multiplier is their quotient:

$$
\frac{0.9555\ldots}{0.9091\ldots} = 1.0510\ldots
$$

so each gram costs about 5.1% more even though the tag fell. Directly: the old unit price is $4.49 \div 2.2 = 2.0409$ dollars per 100 g, the new one is $4.29 \div 2 = 2.145$, and $\frac{2.145}{2.0409} = 1.0510$. To hold the old unit price, the 200 g bag would have to cost $4.49 \times \frac{200}{220} = 4.08$ dollars.

The tag went down and the real price went up. This is the untidy case: the signal on the tag and the signal in the unit price point in opposite directions, so trust the unit price.

Check: 5.1% more per gram for 9.1% less chips and 4.5% less money, and $0.955 \div 0.909 = 1.051$.

</div>

<div class="example" markdown>

### Example 4: is the membership worth it? (finish it yourself)

A warehouse club charges \$65 a year. Its prices on the things you buy run 9% below the regular store's. You normally spend about \$30 a month on those things at the regular store. Is the membership worth it, and what would break-even spending be?

Step 1: the fee is $F = 65$ and the saving rate is $s = 0.09$. Step 2: the break-even spending at regular prices is $S^{*} = \frac{F}{s} = \frac{65}{0.09}$.

Now work out $S^{*}$ for a year and for a month, compare it with your \$360 a year, and find the net gain.

<details class="solution" markdown>
<summary>Finish</summary>

$S^{*} = 65 \div 0.09 = 722.22$ dollars a year, which is $722.22 \div 12 = 60.19$ dollars a month. You spend \$360 a year, well below that.

The saving is $0.09 \times 360 = 32.40$ dollars, and the net gain is $32.40 - 65 = -32.60$ dollars. You would lose \$32.60 a year.

Check: at exactly the break-even spending, $0.09 \times 722.22 = 65.00$, the fee.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: comparing unit prices in different units. A label of \$1.29 per 100 g and one of \$12.20 per kg look nothing alike, but the second is \$1.22 per 100 g. Put both in one unit before you look at which is smaller.

</div>

<div class="warning" markdown>

Watch out: taking the bulk label at face value. A bigger package with a lower unit price is a saving only for the part you use. The 1 kg cheese pack saves nothing if only 70% gets eaten, since $0.499 \div 0.70 = 0.713$ dollars per 100 g used is worse than the small pack's \$0.6225.

</div>

<div class="warning" markdown>

Watch out: a deal on something you don't need. A 33.3% discount on a third tin of soup saves money only if you would have bought that tin. A "buy 2 get 1 free" deal costs more than not buying when you needed only one. Compare the deal's price to what you would have spent, not to the regular price.

</div>

<div class="warning" markdown>

Watch out: flipping the division. Grams per dollar is a correct rate, but then the bigger number is better. Mixing it with dollars per gram makes the comparison backwards, as in [ratios and unit rates](../../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#worked-examples).

</div>

Unit price ignores quality, taste and storage. Two cereals at the same unit price are not the same product, and a package that doesn't fit in your fridge is no bargain. It also ignores unit differences inside a category: a label for laundry soap per load and one per litre can't be compared until both are in the same unit.

A zero-size package, or a quantity of 0, has no unit price, since the division is by zero. A free sample has a unit price of \$0, which is fine.

## Tricks and shortcuts

To compare two packages quickly, scale one to the other's size, as in the check for Example 1 and the [ratios lesson's trick](../../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#tricks-and-shortcuts). A 500 g box at \$3.49 and a 1.2 kg box at \$7.99: 1.2 kg is 2.4 boxes, which would cost $2.4 \times 3.49 = 8.38$ dollars, so the big box is cheaper.

A deal's effective discount is the free fraction. "Buy 2 get 1 free" is one in three, 33%. "Buy 3 get 1 free" is one in four, 25%. If you only need half the group, divide the saving by how much of the group you will actually use.

For the unit price of a multi-buy, divide the group price by the group size, then by the unit. "3 for \$10" is \$3.33 each. Memorize that a "2 for" deal is a discount only when the pair costs less than twice the single price.

To spot shrinkflation, compare the old and new sizes. A 10% smaller package at the same price is an 11.1% price rise per unit, since $\frac{1}{0.9} = 1.111$. The rise is bigger than the shrink, because the quantity is the divisor.

For a membership, estimate break-even spending as the fee divided by the saving rate. A \$65 fee at 10% savings needs \$650 a year, about \$54 a month, so ask whether you really spend that much at the club.

## In code

A unit price is one division, and sorting a list of packages by it takes one line. The function below converts to a common unit first, so the comparison is fair.

<details class="code" markdown>
<summary>In code</summary>

```python
UNITS = {"g": 1.0, "kg": 1000.0, "lb": 453.59237, "oz": 28.349523125}

def price_per_100g(price, amount, unit):
    grams = amount * UNITS[unit]
    return price / (grams / 100)

packages = [
    ("flour 2.5 kg", 5.49, 2.5, "kg"),
    ("flour 10 lb", 8.99, 10, "lb"),
    ("peanut butter 250 g", 2.79, 250, "g"),
    ("peanut butter 2 kg", 12.99, 2, "kg"),
]
for name, price, amount, unit in sorted(packages, key=lambda p: price_per_100g(*p[1:])):
    print(f"{name}: {price_per_100g(price, amount, unit):.4f}")

def breakeven_spending(fee, saving_rate):
    return fee / saving_rate

print(round(breakeven_spending(65, 0.09), 2))   # 722.22
```

The loop prints the cheapest package first: the 10 lb flour at 0.1982, the 2.5 kg flour at 0.2196, the 2 kg peanut butter at 0.6495 and the 250 g jar at 1.1160. Flour is far cheaper per gram than peanut butter, so comparing across products tells you nothing; the sort is only meaningful within one product. The `lambda` is a small function that tells `sorted` which number to sort by.

</details>

## FAQ

### Is the lowest unit price always the best buy?

No. It is the best price per unit, which is the best buy only if you will use all of it, if the quality is the same and if it fits your budget. A cheaper-per-gram jumbo pack that you throw out costs more than a small one you finish, as the break-even fraction shows.

### Should I use 100 g or 1 kg as the unit?

Either, as long as both products use it. A per-100-g label gives numbers around 0.5 to 3 for groceries, which are easy to compare. Per kilogram gives numbers ten times as big. Pick the unit that keeps the numbers readable, and never compare two different ones.

### Why not just buy the biggest package every time?

Because the benefit shrinks while the risk grows. The drop in unit price from one size to the next usually gets smaller (in the peanut butter table, the saving is about 20% from small to medium and about 19% from large to jumbo), and a bigger package is more likely to go to waste. Also, a bigger package ties up more cash and can crowd out other things you need.

### Do all warehouse clubs work this way?

The arithmetic is the same for any fee that buys lower prices: fee divided by saving rate. The saving rate depends on what you buy, and it is a number you estimate for yourself. This lesson doesn't say how much any real club charges or saves.

## Practice

### Warm-up

1\. A 1.89 L carton of juice costs \$4.29, and a 946 mL carton costs \$2.49. Which has the lower price per 100 mL?

<details class="solution" markdown>
<summary>Solution</summary>

The 1.89 L carton is 18.9 lots of 100 mL, so it costs $4.29 \div 18.9 = 0.2270$ dollars per 100 mL. The 946 mL carton is 9.46 lots, so it costs $2.49 \div 9.46 = 0.2632$ dollars. The big carton is cheaper by about 3.6 cents per 100 mL.

Check: 946 mL is about half of 1.89 L, and half of \$4.29 is about \$2.15, less than \$2.49.

</details>

2\. A shirt costs \$6.00 and the store offers "buy 1 get 1 half off". What do you pay for two, what is the price per shirt, and what is the effective discount?

<details class="solution" markdown>
<summary>Solution</summary>

The second shirt costs \$3.00, so two cost \$9.00. The price per shirt is \$4.50, and the discount is $\frac{1.50}{6.00} = 25\%$.

Check: $1.5 \times 6.00 = 9.00$ and $9.00 \div 2 = 4.50$.

</details>

3\. Ground beef is \$3.49 per lb. What is that per kilogram?

<details class="solution" markdown>
<summary>Solution</summary>

A pound is 0.45359237 kg, so \$3.49 per lb is $3.49 \div 0.45359237 = 7.6940\ldots$, about \$7.69 per kg.

Check: a kilogram is about 2.2 lb, and $2.2 \times 3.49 = 7.68$.

</details>

### Standard

4\. Rice comes in a 900 g bag at \$3.49 and a 2.27 kg bag at \$8.49. (a) Which is cheaper per kilogram? (b) How much does the cheaper one save per kilogram, in percent?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The small bag costs $3.49 \div 0.9 = 3.8778$ dollars per kg. The big bag costs $8.49 \div 2.27 = 3.7401$ dollars per kg. The big bag is cheaper.

(b) The saving is $3.8778 - 3.7401 = 0.1377$ dollars per kg, which is $0.1377 \div 3.8778 = 0.0355$, about 3.6% of the small bag's unit price. That is a small saving, so only buy the big bag if you will use it.

Check: scale the small bag to 2.27 kg: that is 2.52 bags, costing $2.52 \times 3.49 = 8.80$ dollars, which is more than \$8.49.

</details>

5\. A chip bag goes from 220 g to 200 g with the price held at \$4.49. (a) By what percent does the unit price rise? (b) The store later raises the price to \$4.69 for the same 200 g. By what percent has the unit price risen since the 220 g bag?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The price multiplier is 1 and the size multiplier is $\frac{200}{220}$, so the unit price multiplier is $\frac{220}{200} = 1.10$: a 10% rise.

(b) The price multiplier is $\frac{4.69}{4.49} = 1.0445$. The unit price multiplier is $1.0445 \times 1.10 = 1.1490$, so the unit price rose about 14.9%.

Check: the old unit price is $4.49 \div 2.2 = 2.0409$ and the new one is $4.69 \div 2 = 2.345$, and $2.345 \div 2.0409 = 1.149$.

</details>

6\. A 12-pack of buns costs \$5.40 and a 6-pack costs \$3.19. You would eat all 6 of the small pack. How many buns of the 12-pack must you eat for it to be the cheaper choice per bun eaten?

<details class="solution" markdown>
<summary>Solution</summary>

The 6-pack costs $3.19 \div 6 = 0.5317$ dollars per bun. If you eat $k$ buns of the 12-pack, it costs $5.40 \div k$ per bun eaten. The 12-pack wins when $\frac{5.40}{k} < 0.5317$, which means $k > 5.40 \div 0.5317 = 10.16$. You must eat at least 11 of the 12 buns.

As a fraction: $\frac{10.16}{12} = 0.846$, so you use at least 85% of the pack.

Check: with 10 eaten, $5.40 \div 10 = 0.540$, more than 0.5317. With 11, $5.40 \div 11 = 0.4909$, less. So 11 is the least.

</details>

### Challenge

7\. A club charges \$120 a year and its prices are 18% below a regular store's. (a) What is the break-even yearly spending, measured at regular prices? (b) You spend \$450 a year at regular prices on the things the club sells. What is your net gain or loss? (c) You buy 40% more goods because the packs are big. Compare your total yearly cost, fee included, with the \$450 you spent before.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $S^{*} = 120 \div 0.18 = 666.67$ dollars a year, about \$55.56 a month.

(b) The saving is $0.18 \times 450 = 81.00$ dollars, so the net is $81.00 - 120 = -39.00$. You lose \$39 a year.

(c) The extra goods would cost $1.4 \times 450 = 630$ dollars at the regular store, and the club's price is $0.82 \times 630 = 516.60$ dollars. With the \$120 fee the total is \$636.60, which is \$186.60 more than the \$450 you spent before.

The "saving" of 18% hides this: the percent applies to each item's price, but you spent more in total. Compare what you spend, not the discount.

Check: $0.82 \times 630 = 516.6$, and $516.60 + 120 - 450 = 186.60$.

</details>

8\. (Reviews [ratios](../../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md) and [percent change](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).) A 500 g jar of peanut butter at \$4.49 is "20% off this week". A 1 kg jar is \$7.99 at the regular price. (a) Which is cheaper per 100 g? (b) By what percent is it cheaper? (c) What discount on the 1 kg jar would make the two equal?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The sale price of the small jar is $4.49 \times 0.80 = 3.592$ dollars, so its unit price is $3.592 \div 5 = 0.7184$ dollars per 100 g. The big jar is \$0.799 per 100 g, so the small jar is cheaper this week.

(b) The percent difference, measured against the big jar, is $\frac{0.799 - 0.7184}{0.799} = 0.1009$, about 10.1% cheaper.

(c) The big jar needs a multiplier of $\frac{0.7184}{0.799} = 0.8991$, which is a discount of about 10.1%. That is the same number as in (b), since the discount that equalizes the two prices is the percent difference measured against the big jar.

Check: $7.99 \times 0.8991 = 7.184$, and $7.184 \div 10 = 0.7184$.

</details>

## Where this shows up

- The next lesson, [paycheques and budgeting](03-paycheques-and-budgeting.md), puts the same unit-rate thinking to work on pay: a wage is a price per hour, and a budget compares what you earn with what you spend each month.
- In economics, the unit price is the average cost of one unit, and a bulk discount is a case of paying less per unit as the quantity grows. The same trade-off of what you give up for what you get appears in [opportunity cost and the PPC](../../07-economics-math/02-markets/01-opportunity-cost-and-the-ppc.md).
- In computing, a cloud bill is a unit price times usage (dollars per GB or per hour), and comparing a reserved plan with pay-as-you-go is the same break-even calculation as the membership fee: a fixed charge divided by the saving per unit.
