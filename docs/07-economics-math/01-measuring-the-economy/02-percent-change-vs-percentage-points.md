# Percent change vs percentage points

After this lesson you can tell a percent change from a change in percentage points, convert between percentage points and basis points, combine and average changes correctly, and read a news headline about interest, inflation or unemployment without mixing the two up.

Before this: [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md) and [how economists use math and graphs](01-how-economists-use-math-and-graphs.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. The Bank of Canada lowered its policy rate from 2.50% to 2.25% on October 29, 2025. By how many percentage points and basis points did it fall, and what is the percent change in the rate?
2. An unemployment rate goes from 5.0% to 6.0%. One headline says "up 1 point" and another says "up 20%". Are both right?
3. Sales rise 50% in one year and fall 50% the next. Is the average change 0%? What is the overall change?

<details class="solution" markdown>
<summary>Answers</summary>

1. The rate fell $2.50 - 2.25 = 0.25$ percentage points, which is 25 basis points. The percent change is $\frac{-0.25}{2.50} = -0.10$, a 10% decrease in the rate.
2. Both. The rate rose 1 percentage point, and $\frac{1.0}{5.0} = 20\%$ is the percent change in the rate.
3. No. The multipliers are $1.5 \times 0.5 = 0.75$, so sales end 25% lower. The plain average of $+50\%$ and $-50\%$ is 0%, which is why averaging percent changes is a trap.

</details>

## The idea

Suppose a news site reports "unemployment up 20%" and a second site reports "unemployment up 1 point". If you only saw one of them, you could imagine very different economies. In a country where the rate went from 5% to 6%, both headlines are true, and they describe the same event. In a country where it went from 20% to 24%, the first headline is also true (20% of 20 is 4, so up 20%) while the second is false (it rose 4 points).

The trouble is that a rate is already a percent. When a rate changes, there are two natural questions. How far did it move, in the units of the rate? That is a difference of percentages, measured in percentage points. How big was the move compared to where the rate started? That is a percent change of the rate. The first answers "how far", the second "how much, relatively". Economics reports rates constantly (interest, inflation, unemployment, growth, tax rates), so this one distinction decides whether a sentence says something true.

The Bank of Canada's policy rate shows both at once. From September 17 to October 29, 2025, the target for the overnight rate went from 2.50% to 2.25% (Bank of Canada, [key interest rate](https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/), checked October 2026). The move is 25 basis points, a quarter of a percentage point, and a relative cut of 10% in the rate. Central banks and banks talk in basis points because the relative figure changes with the starting level and the points figure doesn't.

## Definitions

A **percentage point** is the unit for the difference between two percentages. If a rate goes from $r_0\%$ to $r_1\%$, the change in percentage points is

$$
r_1 - r_0.
$$

In plain words, subtract the two percentages and call the result "points". From 4% to 5% is $+1$ percentage point. The word "point" is often shortened ("up half a point", "a 0.25-point cut"), which is fine when the quantity is plainly a rate.

A **basis point** (bp, plural bps) is one hundredth of a percentage point, that is, $0.01\%$. So

$$
1\ \text{percentage point} = 100\ \text{basis points}, \qquad 1\ \text{bp} = 0.01\% = 0.0001.
$$

In plain words, basis points are what you use when percentage points are too coarse. A 0.25-point cut is a 25 bp cut, and a rate of 2.25% can be said "225 bps".

The **percent change** of a quantity from $x_0$ to $x_1$ is, as before,

$$
\frac{x_1 - x_0}{x_0} \times 100\%,
$$

and when the quantity is itself a rate we call it the **relative change** of the rate. The **absolute change** is the plain difference $x_1 - x_0$ in the quantity's own units. For a rate, the absolute change is the change in percentage points. For a dollar amount, it is a number of dollars. In plain words, absolute change says how far, relative change says how far compared with where you started.

## How to do it

### Telling the two apart

When a sentence says a rate "rose 1%" or "fell 25%", decide which of the two it means before using the number.

1. Ask whether the quantity is a rate (a percent). Unemployment, inflation, interest, tax and growth rates are. A price, GDP or a head count is not, and for those only percent change makes sense.
2. If it is a rate, find the two values: the starting rate $r_0$ and the new rate $r_1$.
3. Compute the absolute change $r_1 - r_0$ in percentage points (multiply by 100 for basis points).
4. Compute the relative change $\frac{r_1 - r_0}{r_0}$ if you also need the comparison with the old rate.
5. Write both, with the unit: "25 basis points" or "0.25 percentage points" or "10%, relative to the old rate". A bare "0.25%" or "10%" is unclear.
6. Check that the two agree: new rate $= r_0 \times (1 + \text{relative change})$, and also $= r_0 + \text{points}$.

The two are linked by one formula. Dividing the change in points by the old rate gives the relative change:

$$
\text{relative change} = \frac{\text{change in points}}{r_0}.
$$

So for a given change in points, the relative change is large when the old rate is small. A 1-point rise is a 100% rise from 1%, a 25% rise from 4% and a 2.5% rise from 40%.

### Why changes in points add and percent changes do not

Changes measured in points are differences, and differences add. A rate that rises 0.5 points and then falls 0.5 points is back where it started. Relative changes are ratios, and ratios multiply ([percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md)). The same rate that rose 12.5% (from 4.0% to 4.5%) and then fell 11.1% (from 4.5% back to 4.0%) shows two different-looking relative changes for movements that cancel in points. Example 3 works this through.

When a rate multiplies something (an interest rate times a balance), the relative change in the rate is also the relative change in the product. A loan at 5.2% on a fixed balance pays 4.8% less interest at 4.95%, and that is the percent change from 5.2 to 4.95. Dollar interest changes in proportion, and points tell you the rate difference.

### Combining several percent changes

Compound changes in a quantity by multiplying multipliers. A rise of 10% and then a fall of 10% gives $1.10 \times 0.90 = 0.99$, so the quantity ends 1% lower, not unchanged. Take the same quantity twice, up 50% then down 50%: $1.5 \times 0.5 = 0.75$, a 25% fall. The second change is measured against a different base, so the same percent covers a different amount ([several changes in a row](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#several-changes-in-a-row)).

For small changes the error is small, and it grows with the size of the changes. The exact overall change from rates $r_1$ and $r_2$ is $r_1 + r_2 + r_1 r_2$, so adding the percents misses the cross term $r_1 r_2$. That is the extra 0.06 in $2\% + 3\% \to 5.06\%$.

### Averaging percent changes

The plain average (arithmetic mean) of several percent changes is usually the wrong summary. Sales that rise 60% and then fall 25% have a mean change of $\frac{60 - 25}{2} = 17.5\%$ per year. But the actual two-year change is $1.60 \times 0.75 = 1.20$, which is 20%, and if sales had really grown 17.5% twice they would have grown $1.175^2 = 1.3806$, or 38.1%. The number that does reproduce the result is the geometric mean of the multipliers, $\sqrt{1.20} = 1.0954$, a steady 9.5% a year. The next lesson, [growth rates and CAGR](03-growth-rates-and-cagr.md), builds this into the compound annual growth rate.

Percentages of different wholes also cannot be averaged without weights. If province A has an unemployment rate of 7% on a labour force of 8 million and province B has 5% on 2 million, the combined rate is the total unemployed over the total labour force:

$$
\frac{0.07 \times 8 + 0.05 \times 2}{8 + 2} = \frac{0.56 + 0.10}{10} = 0.066,
$$

or 6.6%, not the plain average 6%. The combined rate is a weighted average, with the labour forces as weights. The size of the whole matters, as in [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md#solving-part-whole-and-percent-problems): a percent is always a percent of something.

### Reading headlines

News reports use several patterns that blur the two ideas. A short list of what to check:

- "Inflation rose 29%." Inflation is a rate. A report of a 29% rise could mean inflation went from 2.4% to 3.1%, which is a 29% relative increase and a 0.7-point increase. The prices rose 3.1%, not 29%.
- "The rate is 10% lower." Lower than what, and in what units? From 2.50% to 2.25% is both 25 bps and 10% relative.
- "Up 1%" next to a rate. Often a point is meant. Check with the numbers in the article.
- "Interest rates doubled." That is a relative change (a 100% rise). From 1% to 2% it is one point, and from 4% to 8% it is four.
- A "0.5% rate hike". Most often means 50 bps, as in half a percentage point. When in doubt, the two rates in the article settle it.

## Worked examples

<div class="example" markdown>

### Example 1: a Bank of Canada rate cut

The target for the overnight rate was 2.50% after the September 17, 2025 decision and 2.25% after October 29, 2025 (Bank of Canada, [key interest rate](https://www.bankofcanada.ca/core-functions/monetary-policy/key-interest-rate/)). Describe the change.

Step 1: the overnight rate is a rate, so both measures make sense.

Step 2: $r_0 = 2.50$ and $r_1 = 2.25$.

Step 3: the absolute change is $2.25 - 2.50 = -0.25$ percentage points, which is $-25$ basis points.

Step 4: the relative change is $\frac{-0.25}{2.50} = -0.10$, which is $-10\%$.

Step 5: so the Bank cut the rate by 25 basis points, or 0.25 percentage points, which is a 10% cut relative to the old rate.

Step 6: check that $2.50 \times 0.90 = 2.25$ and $2.50 - 0.25 = 2.25$. Both agree.

<div class="warning" markdown>

Watch out at Step 5: "the Bank cut rates by 0.25%" is unclear. It could mean 25 bps or 0.25% relative (which would be a cut from 2.50% to 2.49375%). The unit decides.

</div>

</div>

<div class="example" markdown>

### Example 2: inflation and a price level

Annual CPI inflation was 2.4% in September 2025 and 3.1% in September 2026 (Bank of Canada, [consumer price index data](https://www.bankofcanada.ca/rates/price-indexes/cpi/), from Statistics Canada, Table 18-10-0004-01). Describe the change in the inflation rate, and say what a 3.1% rate means for prices.

The change in the rate is $3.1 - 2.4 = 0.7$ percentage points, or 70 basis points. The relative change is $\frac{0.7}{2.4} = 0.2917$, so the inflation rate rose about 29.2%.

A rate of 3.1% means the price level (the CPI) was 3.1% higher than a year earlier. The index went from 164.9 in September 2025 to 170.0 in September 2026, and $\frac{170.0}{164.9} - 1 = 0.0309$, which rounds to the published 3.1%.

Check: $2.4 \times 1.2917 = 3.1$. The figures of "29.2% more inflation" and "prices 3.1% higher" are about different quantities: one is the change in a rate, the other a change in a price level. A sentence that says "prices rose 29%" would be wrong by a factor of nearly ten.

</div>

<div class="example" markdown>

### Example 3: changes in a row, in points and in percent

A variable mortgage rate is 4.00%. The lender raises it by 50 bps, then lowers it by 50 bps. Find the change at each step in points and in relative terms, and the overall change.

First step: $4.00 + 0.50 = 4.50$. The change is $+0.50$ points, and the relative change is $\frac{0.50}{4.00} = 12.5\%$.

Second step: $4.50 - 0.50 = 4.00$. The change is $-0.50$ points, and the relative change is $\frac{-0.50}{4.50} = -11.1\%$.

Overall, the rate is back at 4.00%. In points the two changes add to $0.50 - 0.50 = 0$. In relative terms, $12.5\%$ and $-11.1\%$ do not add to 0, but the multipliers do compose: $1.125 \times 0.8889 = 1$.

Check: $4.00 \times 1.125 = 4.50$ and $4.50 \times \frac{8}{9} = 4.00$. The percent change that undoes a 12.5% rise is a fall of $\frac{0.125}{1.125} = 11.1\%$, which is the undo rule from [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).

</div>

<div class="example" markdown>

### Example 4: a pooled rate (finish it yourself)

These are made-up numbers. Region A has a labour force of 6.0 million and an unemployment rate of 9.0%. Region B has a labour force of 4.0 million and a rate of 6.0%. Find the unemployment rate for the two regions together.

The plain average of 9.0% and 6.0% is 7.5%, but the regions have different sizes, so the whole is the combined labour force. The unemployed in A number $0.09 \times 6.0 = 0.54$ million.

Now find the unemployed in B, add, divide by the combined labour force, and compare with 7.5%.

<details class="solution" markdown>
<summary>Finish</summary>

In B the unemployed number $0.06 \times 4.0 = 0.24$ million. Together that is $0.54 + 0.24 = 0.78$ million of a labour force of $6.0 + 4.0 = 10.0$ million, and $\frac{0.78}{10.0} = 0.078$, so the combined rate is 7.8%.

It is above the plain average 7.5% because the larger region, A, has the higher rate and gets more weight.

Check: weighted average with weights 0.6 and 0.4: $0.6 \times 9.0 + 0.4 \times 6.0 = 5.4 + 2.4 = 7.8$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a rate "up 1%" is not a rate up 1 point. If the unemployment rate is 6.0% and it "rises 1%", it moves to 6.06%, a tiny change. If it rises 1 point, it moves to 7.0%. A headline that wants the second meaning and writes the first is a common source of confusion. Check the two rates quoted in the story.

</div>

<div class="warning" markdown>

Watch out: a large percent change in a rate can be a small move in points. A rate that goes from 0.5% to 1.0% has doubled (up 100%), and it has risen half a point. Percent changes of low rates are large. A cut from 4.00% to 3.75% is smaller in relative terms (6.25%) than a cut from 0.50% to 0.25% (50%), though both are 25 bps.

</div>

<div class="warning" markdown>

Watch out: percent changes in a row do not add. Up 10% and then down 10% leaves the quantity 1% lower. The same applies to rates: "inflation rose 20% and then fell 20%" leaves it at 96% of where it started.

</div>

<div class="warning" markdown>

Watch out: do not average percentages of different wholes without weights. Combining 7% of 8 million and 5% of 2 million gives 6.6%, not 6%.

</div>

Percent change from a rate of 0 is undefined, because the formula divides by the old rate. A policy rate that goes from 0% to 0.25% rose 25 basis points, and there is no meaningful relative change.

A percent change can exceed 100%, and a rate can go negative in points: the policy rates of some central banks (the ECB and the Bank of Japan, for example) were below zero for years. A relative change of a negative rate gets signs that mislead: from $-0.5\%$ to $0.5\%$ the formula gives $\frac{1}{-0.5} = -200\%$ for a rise. Report the points when the old rate is zero or negative.

A change in points is not a statement about the size of the effect. A 1-point rise in a mortgage rate from 5% to 6% raises interest cost by 20%, while a 1-point rise in a savings rate from 1% to 2% doubles the interest earned. The same point change has different effects, which is why economists often work with relative changes when effects scale with the level.

## Tricks and shortcuts

Convert in your head by moving the decimal: 25 bps is 0.25 points is $0.0025$ as a decimal. A rate of 3.75% is 375 bps. To go from points to relative change, divide by the old rate: 0.25 over 2.50 is 0.1, so 10%.

Dollar effects of a rate change on a balance are balance times the change in the rate as a decimal. A 25 bp change on \$400,000 of floating-rate debt is $400000 \times 0.0025 = 1000$ dollars a year, so about \$83 a month. That avoids percent-of-percent arithmetic entirely.

To spot sloppy writing, translate the headline into the two numbers it implies. If a story says a rate "rose 50%" and it gives a rate of 3.0%, the new rate is 4.5% (a rise of 1.5 points). If the story says the rate is 3.5%, "50%" cannot be right, and a point was probably meant.

For small relative changes, the percent change in a product or ratio is approximately the sum or difference of the percent changes in the parts. The next lessons use this: a 2% rise in a price and a 3% rise in a quantity make about a 5% rise in revenue ($1.02 \times 1.03 = 1.0506$).

## In code

Three small functions cover the whole lesson: the change in points, the change in basis points, and the relative change.

<details class="code" markdown>
<summary>In code</summary>

```python
def points(old, new):
    return new - old

def basis_points(old, new):
    return round((new - old) * 100)

def relative_change(old, new):
    return (new - old) / old * 100

print(points(2.50, 2.25), basis_points(2.50, 2.25))      # -0.25 -25
print(round(relative_change(2.50, 2.25), 1))             # -10.0
print(round(relative_change(2.4, 3.1), 1))               # 29.2

# A pooled rate is a weighted average, not a plain average
sizes = [6.0, 4.0]      # labour forces, millions (made up)
rates = [9.0, 6.0]      # unemployment rates, percent
pooled = sum(s * r for s, r in zip(sizes, rates)) / sum(sizes)
print(round(pooled, 1), sum(rates) / len(rates))         # 7.8 7.5

# Up 50% then down 50% is a 25% fall
print(round((1.5 * 0.5 - 1) * 100, 1))                   # -25.0
```

</details>

## FAQ

### Why do central banks quote basis points?

Because rate moves are usually small and people want one clear unit. "25 bps" cannot be confused with 25% of the rate, while "a quarter point" and "0.25%" can. Basis points also make sums easy: a 25 bp rise followed by a 50 bp rise is 75 bps, with no decimals.

### Is a rate "up 1%" always wrong?

It is unclear, not always wrong. The two readings give nearly the same answer only when the starting rate is near 100%, and they differ by a factor of about 100 for a rate near 1%. The writer owes the reader the units. Some sources, including some official ones, write "percent" for points in tables of rates. Read the table notes.

### Why does the same cut look bigger or smaller depending on the measure?

The point change doesn't depend on the old rate, and the relative change divides by it. A cut of 25 bps from 2.50% is 10% relative, and from 5.00% it is only 5%. Relative figures answer "compared with where we were", which is sensible when effects scale with the rate, as interest cost does. Points answer "how far did it move", which is sensible when you compare policy actions of different eras.

### Can percentage points be negative?

Yes. A fall in a rate is a negative change in points ($-0.25$) and a negative relative change ($-10\%$). In text we usually drop the sign and say "fell".

## Practice

### Warm-up

1\. A rate goes from 3.00% to 3.50%. Find the change in percentage points, in basis points, and the percent change in the rate.

<details class="solution" markdown>
<summary>Solution</summary>

The change is $3.50 - 3.00 = 0.50$ percentage points, which is 50 basis points. The relative change is $\frac{0.50}{3.00} = 0.1667$, about 16.7%.

Check: $3.00 \times 1.1667 = 3.50$.

</details>

2\. Convert: (a) 75 bps to percentage points and to a decimal, (b) 1.6 percentage points to bps, (c) a rate falling from 4.2% to 4.0% in bps.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\frac{75}{100} = 0.75$ percentage points, which is $0.0075$ as a decimal. (b) $1.6 \times 100 = 160$ bps. (c) $4.0 - 4.2 = -0.2$ points, which is $-20$ bps.

Check: 100 bps is 1 point, so 75 bps is three quarters of a point and 20 bps is a fifth of a point.

</details>

3\. The unemployment rate goes from 5.0% to 5.5%. Give two correct headlines, one in points and one in percent change, and say what is wrong with the headline "unemployment up 0.5%".

<details class="solution" markdown>
<summary>Solution</summary>

"Unemployment rate up half a percentage point" and "unemployment rate up 10%" (since $\frac{0.5}{5.0} = 0.10$ relative to the old rate). The headline "up 0.5%" is unclear: read literally, 0.5% of 5.0 is 0.025, a move to 5.025%.

Check: $5.0 + 0.5 = 5.5$ and $5.0 \times 1.10 = 5.5$.

</details>

### Standard

4\. A sales tax rate is cut from 13% to 12%. (a) What is the change in percentage points? (b) What is the percent change in the rate? (c) By what percent does a tax-included price fall, if the pre-tax price stays the same?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $12 - 13 = -1$ percentage point. (b) $\frac{-1}{13} = -0.0769$, a fall of 7.7% in the rate. (c) The tax-included price is the pre-tax price times $1 + \text{rate}$, so it goes from $1.13$ to $1.12$ times the pre-tax price, and the percent change is $\frac{1.12}{1.13} - 1 = -0.00885$, a fall of about 0.88%.

The three answers differ because they have three different wholes: the rate points, the rate itself and the price. Check: on a \$100 pre-tax item the total goes from \$113 to \$112, and $\frac{1}{113} = 0.88\%$.

</details>

5\. Province A has a labour force of 3.0 million and an unemployment rate of 6%. Province B has 1.0 million and 10% (made-up numbers). (a) What is the pooled unemployment rate? (b) What is the plain average of the two rates, and why is it wrong?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The unemployed are $0.06 \times 3.0 = 0.18$ million and $0.10 \times 1.0 = 0.10$ million, which is 0.28 million of a labour force of 4.0 million, so the pooled rate is $\frac{0.28}{4.0} = 7.0\%$.

(b) The plain average is $\frac{6 + 10}{2} = 8\%$. It treats the two provinces as the same size, but A has three times as many workers, so it should count three times as much. Weights 0.75 and 0.25 give $0.75 \times 6 + 0.25 \times 10 = 7.0$.

Check: both methods in (a) give 7.0%.

</details>

6\. Sales rise 60% one year and fall 25% the next. (a) What is the overall change? (b) What is the plain average of the two changes, and what would two years at that rate give? (c) What steady yearly rate matches the overall change?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $1.60 \times 0.75 = 1.20$, an overall rise of 20%.

(b) The plain average is $\frac{60 - 25}{2} = 17.5\%$. Two years at 17.5% would give $1.175^2 = 1.3806$, a rise of 38.1%, which is far too high.

(c) The steady rate $g$ satisfies $(1 + g)^2 = 1.20$, so $1 + g = \sqrt{1.20} = 1.0954$, and $g = 9.5\%$ a year.

Check: $1.0954^2 = 1.2000$.

</details>

### Challenge

7\. You have a \$300,000 interest-only variable-rate loan at 5.20%, and the rate falls by 25 basis points. (a) What are the interest costs per year before and after? (b) What is the saving per month? (c) What is the percent change in the interest cost, and how does it compare with the percent change in the rate?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Before: $300000 \times 0.0520 = 15{,}600$ dollars. After, the rate is $5.20 - 0.25 = 4.95\%$ and the cost is $300000 \times 0.0495 = 14{,}850$ dollars.

(b) The saving is $15600 - 14850 = 750$ dollars a year, or $\frac{750}{12} = 62.50$ dollars a month.

(c) $\frac{14850 - 15600}{15600} = -0.04808$, a fall of 4.81%. The relative change in the rate is $\frac{-0.25}{5.20} = -0.04808$ too. The interest cost is the rate times a fixed balance, so it changes by the same percent as the rate.

Check: the shortcut gives $300000 \times 0.0025 = 750$, matching (b).

</details>

8\. (Reviews [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).) A rate falls 20% relative to its old value, from 5.0% to 4.0%. What relative rise brings it back to 5.0%? How many points is each move?

<details class="solution" markdown>
<summary>Solution</summary>

The multiplier of the fall is $0.80$, and the rise that undoes it has multiplier $\frac{1}{0.80} = 1.25$, a 25% rise. In points, the fall is $4.0 - 5.0 = -1.0$ point and the rise is $+1.0$ point.

So the two moves have the same size in points and different sizes in percent, because the second is measured from the lower rate.

Check: $5.0 \times 0.80 = 4.0$ and $4.0 \times 1.25 = 5.0$.

</details>

## Where this shows up

- [Growth rates and CAGR](03-growth-rates-and-cagr.md) replaces the plain average of this lesson with the geometric mean. [CPI and inflation](07-cpi-and-inflation.md) and the [unemployment rate](08-unemployment-rate-and-labour-statistics.md) are the two rates where the headline problem appears most.
- In finance, mortgage and bond quotes use basis points, and a rate change times a balance gives the dollar effect ([compound interest](../../08-financial-math/02-interest-and-growth/02-compound-interest.md)).
- In software, an A/B test that raises a conversion rate from 2.0% to 2.5% is a 0.5-point gain and a 25% relative lift, and a report that says only "up 25%" hides the size of the effect.
