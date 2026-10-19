# Percents

After this lesson you can convert between fractions, decimals and percents, and find the missing number in a percent problem, such as the HST on a price or the price before tax on a receipt.

Before this: [fractions and equivalent fractions](../../01-elementary/09-fractions-and-equivalent-fractions.md), [multiplying and dividing decimals](../../01-elementary/13-multiplying-and-dividing-decimals.md), and [proportional relationships](02-proportional-relationships.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write $\frac{5}{8}$ as a percent, and write 0.8% as a decimal.
2. What percent of 36 is 27?
3. A receipt total, including 13% HST, is \$56.50. What was the price before tax?

<details class="solution" markdown>
<summary>Answers</summary>

1. Divide: $5 \div 8 = 0.625$, which is 62.5%. Dividing by 100 gives $0.8\% = 0.008$.
2. Divide the part by the whole: $27 \div 36 = 0.75$, so 27 is 75% of 36.
3. The total is 113% of the price, so the price is $56.50 \div 1.13 = 50$, that is, \$50.00.

</details>

## The idea

Suppose a survey finds that 35 out of every 100 students at a college walk to class. The short way to write "35 out of every 100" is 35%, read "35 percent". The "cent" in percent is the same as in the coin: a cent is one hundredth of a dollar, so 35% of a dollar is 35 cents.

Writing amounts per hundred makes them easy to compare when the wholes are different. Say you scored 42 out of 60 on one midterm and 36 out of 50 on another. The raw scores don't tell you which went better, because the totals differ. Scaled to marks out of 100, the first is 70 and the second is 72, so the second midterm went slightly better even though you earned fewer marks.

A percent is a fraction with denominator 100, so it can also be written as a decimal: the numbers 35%, $\frac{35}{100}$ and $0.35$ are all the same. Most percent questions involve three numbers. There is a whole (all 2,400 students at the college, say), a percent (35% walk) and the part that the percent picks out ($0.35 \times 2400 = 840$ students). If you know two of the three, one multiplication or one division gives you the third.

## Definitions

A **percent** is a ratio that compares a number to 100. For a number $x$, the expression $x\%$ (read "$x$ percent") is $x$ divided by 100:

$$
x\% = \frac{x}{100}.
$$

In plain words, the % sign means "divide by 100". So $35\% = 0.35$, $250\% = 2.5$ and $0.5\% = 0.005$. The number in front of the sign can be a decimal, and it can be bigger than 100.

In a statement of the form "the part is $x\%$ of the whole", the **whole** is the quantity the percent is taken of, and the **part** is the quantity equal to $x\%$ of it. (The whole is also called the base.) The three numbers are related by this equation:

$$
\text{part} = \frac{x}{100} \times \text{whole}.
$$

Said more simply, the whole is the amount that counts as 100%, and it is usually the noun right after the word "of". In "HST is 13% of the price", the price is the whole and the tax is the part. The name "part" fits best when the percent is under 100%, but the equation works for every percent: 250% of 18 is $2.5 \times 18 = 45$, a part bigger than its whole.

## How to do it

### Converting between fractions, decimals and percents

Since $x\% = \frac{x}{100}$, every conversion comes down to multiplying or dividing by 100, which moves the decimal point two places ([powers of ten](../../01-elementary/14-powers-of-ten.md)).

| From | To | Method | Example |
|---|---|---|---|
| percent | decimal | divide by 100: move the decimal point two places left | $7\% = 0.07$ |
| decimal | percent | multiply by 100: move the decimal point two places right | $1.25 = 125\%$ |
| fraction | percent | divide the numerator by the denominator, then multiply by 100 | $\frac{3}{8} = 0.375 = 37.5\%$ |
| percent | fraction | write the number over 100 and simplify | $37.5\% = \frac{375}{1000} = \frac{3}{8}$ |

Watch out in the first row: 7% is 0.07, not 0.7. Moving the point only one place is an easy slip, so check the size afterwards. A percent under 100% becomes a decimal under 1, and a percent under 1% becomes a decimal under 0.01.

In the last row, if the percent has a decimal point, multiply the numerator and the denominator by 10 until it is gone, then simplify. When the denominator of a fraction divides 100, you can also scale it instead of dividing: $\frac{3}{25} = \frac{12}{100} = 12\%$.

### Solving part, whole and percent problems

Every problem in this lesson comes down to one equation:

$$
\text{part} = \text{percent} \times \text{whole}.
$$

The percent in it is written as a decimal, and one of the three numbers is missing. These steps find it.

1. Find the whole by asking "percent of what?" The whole is the amount that counts as 100%, usually named right after "of". Choosing the wrong whole is the classic percent mistake (see the seminar example under [Edge cases](#edge-cases-and-common-mistakes)).
2. Decide which number is unknown: the part, the whole or the percent.
3. Write the percent as a decimal by dividing by 100: 13% is 0.13, and 0.5% is 0.005 (not 0.5).
4. Solve the equation for the unknown, using the table below.
5. Round once, at the end. Money goes to the cent and percents to one decimal place, unless the question says otherwise. Rounding in the middle can shift the answer by a cent or more.
6. Check by putting your answer back into the equation, or estimate with 10% or 50%.

Here are the three versions of Step 4, all built from the same three numbers:

| Unknown | Example question | Compute |
|---|---|---|
| the part | What is 15% of 80? | $\text{percent} \times \text{whole} = 0.15 \times 80 = 12$ |
| the whole | 12 is 15% of what number? | $\text{part} \div \text{percent} = 12 \div 0.15 = 80$ |
| the percent | What percent of 80 is 12? | $\text{part} \div \text{whole} = 12 \div 80 = 0.15$, which is $15\%$ |

You can also write the relationship as a proportion, which some people find easier to set up:

$$
\frac{\text{part}}{\text{whole}} = \frac{x}{100}.
$$

Put in the two numbers you know and cross-multiply. For "12 is 15% of what number?" the proportion is $\frac{12}{\text{whole}} = \frac{15}{100}$, so $15 \times \text{whole} = 1200$ and the whole is 80. Both methods are the same equation rearranged, so use whichever you set up faster.

Questions about change, such as "by what percent did the rent go up?", measure the change against the old value and get their own lesson: [percent change and applications](04-percent-change-and-applications.md).

## Worked examples

<div class="example" markdown>

### Example 1: adding HST to a price

Ontario's HST rate is 13% as of 2026: the 5% federal GST plus an 8% provincial part (source: the CRA's [GST/HST calculator and rates page](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate/calculator.html)). You buy headphones priced at \$24.99. How much tax do you pay, and what is the total?

Step 1: the tax is 13% of the price, so the whole is the price, \$24.99.

Step 2: the unknown is the part, which is the tax.

Step 3: write the percent as a decimal, $13\% = 0.13$.

Step 4: multiply the percent by the whole:

$$
\text{tax} = 0.13 \times 24.99 = 3.2487.
$$

Step 5: the total is the price plus the tax. Add the unrounded tax first, then round once:

$$
24.99 + 3.2487 = 28.2387.
$$

So the tax is \$3.25 and the total is \$28.24.

Step 6: check with an estimate. The price is about \$25, and 10% of \$25 is \$2.50 while 1% is \$0.25, so 13% is about $2.50 + 3 \times 0.25 = 3.25$. That matches. The rounded amounts also add up: $24.99 + 3.25 = 28.24$.

You can get the total in one multiplication, $1.13 \times 24.99 = 28.2387$. The FAQ explains why that works.

</div>

<div class="example" markdown>

### Example 2: what percent of your pay is rent

Your take-home pay is \$3,800 a month and your rent is \$1,450. What percent of your pay goes to rent?

The question asks for a percent of your pay, so the whole is 3800 and the part is 1450 (Steps 1 and 2). Divide the part by the whole (Step 4):

$$
1450 \div 3800 = 0.38157\ldots
$$

Multiply by 100 and round (Step 5): about 38.2%. The answer is not a whole number, and that is normal; one decimal place is enough.

The proportion gives the same number. From $\frac{1450}{3800} = \frac{x}{100}$, cross-multiplying gives $3800x = 145000$, so $x = 38.157\ldots$ as before.

Check: 40% of 3800 is 1520, a little more than the rent, so an answer a little under 40% makes sense. Putting the answer back in, $0.382 \times 3800 = 1451.6$, which is close to 1450; the small gap comes from rounding the percent.

</div>

<div class="example" markdown>

### Example 3: the price before tax

A receipt shows a total of \$33.89, including 13% HST. What was the price before tax?

Step 1 is the hard part here. The tax was 13% of the price before tax, so that price is the whole, and it is the unknown. The total is the price plus 13% of the price, which is 113% of the price. So the total, \$33.89, is the part, and the percent is 113%.

Steps 2 to 4: the whole is unknown, $113\% = 1.13$, and the whole is the part divided by the percent:

$$
\text{price} = 33.89 \div 1.13 = 29.99115\ldots
$$

Step 5: round to the cent, \$29.99. The division doesn't come out exact because the receipt total was itself rounded to the cent, and that is fine.

Step 6: check by adding the tax back on: $1.13 \times 29.99 = 33.8887$, which rounds to \$33.89, the total on the receipt.

<div class="warning" markdown>

Watch out: a tempting shortcut is to take 13% of the total and subtract it. That gives $0.13 \times 33.89 = 4.4057$ and $33.89 - 4.4057 = 29.4843$, about \$29.48, which is 51 cents too low. The check catches it: $1.13 \times 29.48 = 33.3124$, so a \$29.48 item would ring up as \$33.31, not \$33.89. The shortcut takes 13% of the wrong whole, because HST is 13% of the price, not of the total.

</div>

</div>

<div class="example" markdown>

### Example 4: a sale discount (finish it yourself)

A jacket regularly priced at \$64 is 35% off. How much do you save, and what is the sale price before tax?

Step 1: the discount is 35% of the regular price, so the whole is \$64.

Step 2: the unknown is the part, the amount you save.

Step 3: as a decimal, $35\% = 0.35$.

Now do Step 4 to find the saving, subtract it from \$64 to get the sale price, and check your answer.

<details class="solution" markdown>
<summary>Finish</summary>

Step 4: $0.35 \times 64 = 22.40$, so you save \$22.40. The sale price is $64 - 22.40 = 41.60$, that is, \$41.60.

Check: 10% of 64 is 6.40, and 35% is three 10%s plus a 5%, so $3 \times 6.40 + 3.20 = 22.40$. Also, $41.60 \div 64 = 0.65$: after 35% off you pay 65% of the regular price, as you should.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the wrong whole. A seminar has 12 women and 18 men. What percent of the seminar is women? The whole is everyone in the seminar, $12 + 18 = 30$, so the answer is $12 \div 30 = 0.4$, or 40%. Dividing by 18 gives 66.7%, which answers a different question: the number of women is 66.7% of the number of men. Before you divide, say the whole in words ("percent of the seminar" or "percent of the men").

</div>

<div class="warning" markdown>

Watch out: 0.5% is half of one percent, which is 0.005 as a decimal, not 0.5. The two differ by a factor of 100. A 0.5% fee on a \$2,000 transfer is $0.005 \times 2000 = 10$ dollars, but reading it as 50% would make the fee \$1,000. A size check catches this: anything under 1% is less than a hundredth of the whole, so 0.5% of \$2,000 has to be under \$20.

</div>

<div class="warning" markdown>

Watch out: the decimal point can move the wrong way. Going from a percent to a decimal makes the number smaller (7% becomes 0.07), and going from a decimal to a percent makes it bigger (0.07 becomes 7%). If 7% turns into 700, the point went right instead of left.

</div>

<div class="warning" markdown>

Watch out: rounding in the middle. Five pastries at \$1.65 each cost \$8.25, and the tax on the total is $0.13 \times 8.25 = 1.0725$, or \$1.07. If you round the tax on one pastry first, $0.13 \times 1.65 = 0.2145$ becomes \$0.21, and five of those make \$1.05, two cents short. Each rounding dropped almost half a cent, and multiplying by 5 added the errors up. Keep every digit until the last step, then round once.

</div>

Removing tax from a total is another place where the whole goes wrong. Divide the total by 1.13; don't subtract 13% of the total. Example 3 shows both and why the second fails.

Percents over 100% are fine: 250% means $\frac{250}{100} = 2.5$, and 250% of 18 is 45. A percent over 100% appears whenever the part is not a piece of the whole: a total with tax is 113% of the price. When the part is a piece of the whole, such as the questions you got right on a test, the percent stays between 0% and 100%.

Zero needs care too. When the percent is 0%, the part is 0, whatever the whole. But "what percent of 0 is 5?" has no answer, because finding a percent means dividing by the whole, and division by zero is undefined.

## Tricks and shortcuts

Ten percent is the easy one: move the decimal point one place left. One percent is two places left. Most other percents can be built from these two, as this table shows for a \$46 restaurant bill:

| Percent | How to build it | Of \$46 |
|---|---|---|
| $10\%$ | move the decimal point one place left | \$4.60 |
| $1\%$ | move the decimal point two places left | \$0.46 |
| $5\%$ | half of $10\%$ | \$2.30 |
| $20\%$ | double $10\%$ | \$9.20 |
| $15\%$ | $10\% + 5\%$ | \$6.90 |
| $18\%$ | $20\% - 2\%$ | \$8.28 |
| $13\%$ | $10\% + 3 \times 1\%$ | \$5.98 |
| $50\%$ | half | \$23.00 |
| $25\%$ | half of $50\%$ | \$11.50 |

So an 18% tip on a \$46 bill is \$8.28: 20% is \$9.20, 2% is \$0.92, and $9.20 - 0.92 = 8.28$. The 13% row is a quick way to estimate HST in your head, as in the check for Example 1.

You can also swap the two numbers: $x\%$ of $y$ equals $y\%$ of $x$. In symbols:

$$
\frac{x}{100} \times y = \frac{x \times y}{100} = \frac{y}{100} \times x.
$$

This works because multiplication can be done in either order. Use it when one direction is easier. For example, 8% of 50 is hard to see, but 50% of 8 is 4, so 8% of 50 is also 4.

A few fractions come up often enough to memorize:

| Fraction | Decimal | Percent |
|---|---|---|
| $\frac{1}{2}$ | $0.5$ | $50\%$ |
| $\frac{1}{3}$ | $0.333\ldots$ | $33\frac{1}{3}\%$, about $33.3\%$ |
| $\frac{2}{3}$ | $0.666\ldots$ | $66\frac{2}{3}\%$, about $66.7\%$ |
| $\frac{1}{4}$ | $0.25$ | $25\%$ |
| $\frac{3}{4}$ | $0.75$ | $75\%$ |
| $\frac{1}{5}$ | $0.2$ | $20\%$ |
| $\frac{1}{8}$ | $0.125$ | $12.5\%$ |
| $\frac{1}{10}$ | $0.1$ | $10\%$ |
| $\frac{1}{20}$ | $0.05$ | $5\%$ |

Knowing these turns some percent questions into fraction questions. For example, 25% of 36 is a quarter of 36, which is 9, and 12.5% of 64 is an eighth of 64, which is 8.

## In code

Each question type is one line of arithmetic, so each fits in a one-line function. The last lines show why code that handles money avoids plain floats.

<details class="code" markdown>
<summary>In code</summary>

```python
from decimal import Decimal, ROUND_HALF_UP

def find_part(percent, whole):
    return percent / 100 * whole

def find_whole(part, percent):
    return part / (percent / 100)

def find_percent(part, whole):
    return part / whole * 100

print(round(find_part(13, 24.99), 2))      # HST on $24.99: 3.25
print(round(find_whole(33.89, 113), 2))    # the total is 113% of the price: 29.99
print(round(find_percent(1450, 3800), 1))  # rent as a percent of pay: 38.2

print(round(2.675, 2))  # 2.67, because the float 2.675 is really 2.67499999...

tax = Decimal("0.13") * Decimal("24.99")
print(tax, tax.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))  # 3.2487 3.25
```

Python's `round` works on binary floats, which can't store most cent amounts exactly, so a value that looks like an exact half cent may round down. The `decimal` module stores `24.99` exactly and lets you pick the rounding rule; `ROUND_HALF_UP` rounds half a cent up. Floating-point basics<!-- link: ../../06-cs-math/01-number-representation/04-floating-point-basics.md --> explains why floats behave this way.

</details>

## FAQ

### Why per hundred and not some other number?

Another fixed denominator would make amounts just as easy to compare. The number 100 is convenient because we write numbers in base 10, so dividing by 100 only moves the decimal point. Other denominators exist: per mille means per thousand, and finance uses basis points, where one basis point is a hundredth of a percent (0.01%). Basis points come back in percent change vs percentage points<!-- link: ../../07-economics-math/01-measuring-the-economy/02-percent-change-vs-percentage-points.md -->.

### Is the tax 13% of the total?

No. The tax is 13% of the price, and the total is 113% of the price, so the tax is $\frac{13}{113} \approx 0.115$ of the total, about 11.5%. On the \$33.89 receipt from Example 3, the tax is $33.89 - 29.99 = 3.90$ dollars, and $3.90 \div 33.89 \approx 0.115$. This is the "percent of what?" question again: the answer depends on which whole you divide by.

### Why does multiplying by 1.13 give the total?

The total is the price plus 13% of the price. Factor out the price, using the [distributive property](../../01-elementary/04-properties-of-operations.md#distributive-property):

$$
\text{price} + 0.13 \times \text{price} = (1 + 0.13) \times \text{price} = 1.13 \times \text{price}.
$$

So adding the tax and multiplying by 1.13 are the same calculation, and dividing by 1.13 undoes it. Multiplying the total by 0.87 does not undo it, because that takes 13% of the total off, which is the wrong whole from Example 3.

### Does "of" always mean multiply?

In percent questions, yes: "15% of 80" means $0.15 \times 80$, the same way "half of 10" means $\frac{1}{2} \times 10$. The "of" is still a multiplication when the percent is the unknown: "what percent of 36 is 27?" means $\text{percent} \times 36 = 27$, and you divide by 36 to undo the multiplication.

## Practice

### Warm-up

1\. Convert each number: (a) $\frac{7}{20}$ to a percent, (b) $0.042$ to a percent, (c) 0.25% to a decimal and to a fraction in lowest terms, (d) 175% to a decimal and to a fraction in lowest terms.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The denominator 20 divides 100, so scale by 5: $\frac{7}{20} = \frac{35}{100} = 35\%$.
- (b) Multiply by 100: $0.042 \times 100 = 4.2$, so the answer is 4.2%.
- (c) Divide by 100: $0.25 \div 100 = 0.0025$. As a fraction, $\frac{0.25}{100} = \frac{25}{10000} = \frac{1}{400}$.
- (d) Divide by 100: $175 \div 100 = 1.75$. As a fraction, $\frac{175}{100} = \frac{7}{4}$.

Check: $7 \div 20 = 0.35$, $1 \div 400 = 0.0025$ and $7 \div 4 = 1.75$. The sizes make sense too: 0.25% is under 1%, so its decimal is under 0.01, and 175% is over 100%, so its decimal is over 1.

</details>

2\. Without a calculator, find (a) 10% of \$38, (b) 5% of \$38, (c) 15% of \$38 and (d) 4% of 75.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Move the decimal point one place left: \$3.80.
- (b) Half of 10%: half of \$3.80 is \$1.90.
- (c) Add the two: $3.80 + 1.90 = 5.70$, so \$5.70.
- (d) Swap the numbers: 4% of 75 equals 75% of 4, which is 3.

Check with multiplication: $0.15 \times 38 = 5.7$ and $0.04 \times 75 = 3$.

</details>

3\. A phone case costs \$12.49 in Toronto. Find the 13% HST and the total.

<details class="solution" markdown>
<summary>Solution</summary>

The tax is 13% of the price, so the whole is 12.49. The tax is $0.13 \times 12.49 = 1.6237$, and the total is $12.49 + 1.6237 = 14.1137$. Rounding once at the end, the tax is \$1.62 and the total is \$14.11.

Check: 13% of \$12.50 is about $1.25 + 3 \times 0.125 = 1.625$, close to \$1.62. The rounded amounts add up: $12.49 + 1.62 = 14.11$.

</details>

### Standard

4\. A test suite covers 1,377 of the 1,620 lines in a codebase. (a) What is the test coverage as a percent? (b) How many more lines must the tests cover to reach 90%?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The coverage is a percent of all the lines, so the whole is 1620. Divide the part by the whole: $1377 \div 1620 = 0.85$, which is 85%.

(b) Find the part that 90% would need: $0.9 \times 1620 = 1458$ lines. The tests cover 1377 now, so they need $1458 - 1377 = 81$ more lines.

Check: $0.85 \times 1620 = 1377$, and $1458 \div 1620 = 0.9$.

</details>

5\. Your receipt total, with 13% HST, is \$61.01. (a) What was the price before tax, and how much was the tax? (b) How far off would you be if you subtracted 13% of the total instead?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The total is 113% of the price, so the price is the whole and the total is the part: $61.01 \div 1.13 = 53.99115\ldots$, which rounds to \$53.99. The tax is the difference, $61.01 - 53.99 = 7.02$, so \$7.02.

(b) Taking 13% of the total gives $0.13 \times 61.01 = 7.9313$, and $61.01 - 7.9313 = 53.0787$, about \$53.08. That is $53.99 - 53.08 = 0.91$, so 91 cents too low.

Check: $1.13 \times 53.99 = 61.0087$, which rounds to \$61.01. The tax also matches: $0.13 \times 53.99 = 7.0187$, which rounds to \$7.02.

</details>

6\. A lecture has 40 students: 14 study economics and the rest study CS. (a) What percent of the lecture studies economics? (b) The number of economics students is what percent of the number of CS students? (c) The number of CS students is what percent of the number of economics students?

<details class="solution" markdown>
<summary>Solution</summary>

There are $40 - 14 = 26$ CS students. Each part asks for a percent of a different whole.

- (a) Percent of the lecture, so the whole is 40: $14 \div 40 = 0.35$, which is 35%.
- (b) Percent of the CS students, so the whole is 26: $14 \div 26 = 0.53846\ldots$, about 53.8%.
- (c) Percent of the economics students, so the whole is 14: $26 \div 14 = 1.85714\ldots$, about 185.7%.

The answer to (c) is over 100% because there are more CS students than economics students, and that is correct.

Check: $0.35 \times 40 = 14$, $0.538 \times 26 = 13.988$ (about 14) and $1.857 \times 14 = 25.998$ (about 26).

</details>

### Challenge

7\. You have \$75 in cash for dinner. HST is 13% of the pre-tax bill, and you want to tip 15% of the pre-tax bill. What is the largest pre-tax bill you can pay for?

<details class="solution" markdown>
<summary>Solution</summary>

The tax and the tip are percents of the same whole, the pre-tax bill, so they add. The amount you pay is the bill plus 13% of it plus 15% of it:

$$
\text{bill} + 0.13 \times \text{bill} + 0.15 \times \text{bill} = 1.28 \times \text{bill}.
$$

So the \$75 you can spend is 128% of the largest bill. That makes the bill the whole: $75 \div 1.28 = 58.59375$. With a budget, round down, because a bill one cent over is a bill you can't pay. The largest bill is \$58.59.

Check: $1.28 \times 58.59 = 74.9952$, which is under 75. Item by item, the tax is $0.13 \times 58.59 = 7.6167$ (\$7.62) and the tip is $0.15 \times 58.59 = 8.7885$ (\$8.79), and $58.59 + 7.62 + 8.79 = 75.00$. One cent more fails: $1.28 \times 58.60 = 75.008$, which is over 75.

</details>

8\. (Reviews [ratios](01-ratios-and-unit-rates.md) and [fractions](../../01-elementary/09-fractions-and-equivalent-fractions.md).) A trail mix has nuts, raisins and chocolate in the ratio $7:4:5$ by mass. (a) What percent of the mix is each ingredient? (b) How many grams of each are in a 400 g bag? (c) You add 100 g of raisins to the 400 g bag. What percent of the mix is raisins now?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The ratio has $7 + 4 + 5 = 16$ parts in total, so each ingredient is a fraction of 16:

- nuts: $\frac{7}{16} = 0.4375$, which is 43.75%,
- raisins: $\frac{4}{16} = \frac{1}{4}$, which is 25%,
- chocolate: $\frac{5}{16} = 0.3125$, which is 31.25%.

(b) Multiply each percent by the whole, 400 g: $0.4375 \times 400 = 175$ g of nuts, $0.25 \times 400 = 100$ g of raisins and $0.3125 \times 400 = 125$ g of chocolate.

(c) There are now $100 + 100 = 200$ g of raisins, and the whole has changed to $400 + 100 = 500$ g. So raisins are $200 \div 500 = 0.4$ of the mix, which is 40%. Adding 25% and 25% to get 50% is wrong: the added 100 g is 25% of the old bag, but the percent you want is of the new, bigger bag.

Check: (a) $43.75 + 25 + 31.25 = 100$. (b) $175 + 100 + 125 = 400$. (c) The other ingredients are $175 + 125 = 300$ g, which is $300 \div 500 = 60\%$ of the new bag, and $40\% + 60\% = 100\%$.

</details>

## Where this shows up

- The next lesson, [percent change and applications](04-percent-change-and-applications.md), measures changes against an old value. Interest is a percent of a balance: simple interest<!-- link: ../../08-financial-math/02-interest-and-growth/01-simple-interest.md --> takes it on the starting amount, and compound interest<!-- link: ../../08-financial-math/02-interest-and-growth/02-compound-interest.md --> takes it again on each new balance.
- Economics reports growth and inflation as percents of an earlier value (growth rates and CAGR<!-- link: ../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md -->). Probabilities are often written as percents too: a 30% chance of rain is a probability of 0.3 ([basic probability](../07-statistics-and-probability/02-basic-probability.md)).
- Computing is full of percents (CPU usage, test coverage, cache hit rates, battery level), and each one is the part divided by the whole, times 100. The first question is still "percent of what?": depending on the tool, a process at 100% CPU may be using one core fully or every core.
