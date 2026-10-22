# Decimals: place value, adding and subtracting

After this lesson you can read and write decimals, convert between decimals and fractions, compare and round decimals, and add and subtract them on paper, including amounts of money.

Before this: [place value and rounding](01-place-value-and-rounding.md), [long division](07-long-division.md) and [fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write $\frac{3}{8}$ as a decimal, and write 0.45 as a fraction in simplest form.
2. Put these in order from smallest to largest: 0.5, 0.45, 0.405, 0.54.
3. Work out $12.6 - 4.75$, then round the answer to the nearest tenth.

<details class="solution" markdown>
<summary>Answers</summary>

1. 0.375, from $3 \div 8$. And $0.45 = \frac{45}{100} = \frac{9}{20}$, dividing the numerator and the denominator by 5.
2. 0.405, 0.45, 0.5, 0.54. With three decimal places each, they are 0.405, 0.450, 0.500 and 0.540, which compare like the whole numbers 405, 450, 500 and 540.
3. 7.85, which rounds to 7.9 because the hundredths digit is 5. Check: $7.85 + 4.75 = 12.6$.

</details>

## The idea

A price of \$4.37 is 4 dollars, 3 dimes and 7 cents. A dime is a tenth of a dollar and a cent is a hundredth of a dollar, so the price is

$$
4 + \frac{3}{10} + \frac{7}{100} \text{ dollars}.
$$

The digits after the point carry on the pattern of whole-number place value. In 444, each 4 is worth ten times as much as the 4 to its right: 400, then 40, then 4. Keep going to the right past the ones, and each new place is worth a tenth of the place before it. The place after the ones is the tenths, then come the hundredths, then the thousandths. The point sits just to the right of the ones digit and marks where the whole part stops.

So a decimal is a way of writing fractions with denominators 10, 100, 1,000 and so on, inside the same place-value system as whole numbers. That is why decimals add and subtract the way whole numbers do, as long as each digit lines up with the other digits in its place.

## Definitions

A **decimal** is a number written in base 10 with a **decimal point**, where the digits after the point stand for tenths, hundredths, thousandths and smaller places. Each place is worth a tenth of the place to its left. Formally, a decimal with whole part $n$ and digits $d_1 d_2 \dots d_k$ after the point stands for

$$
n + \frac{d_1}{10} + \frac{d_2}{100} + \dots + \frac{d_k}{10^k},
$$

where $10^k$ means 1 followed by $k$ zeros ([powers of ten](14-powers-of-ten.md) covers this notation). The first place after the point is the **tenths** place, worth $\frac{1}{10}$; the second is the **hundredths** place, worth $\frac{1}{100}$; the third is the **thousandths** place, worth $\frac{1}{1000}$. The digits after the point are the **decimal places** of the number, so 24.375 has three decimal places and 6 has none.

In plain words, here is 24.375 in a place-value table:

| Tens | Ones | Point | Tenths | Hundredths | Thousandths |
|---|---|---|---|---|---|
| 10 | 1 | | $\frac{1}{10} = 0.1$ | $\frac{1}{100} = 0.01$ | $\frac{1}{1000} = 0.001$ |
| 2 | 4 | . | 3 | 7 | 5 |

So $24.375 = 20 + 4 + \frac{3}{10} + \frac{7}{100} + \frac{5}{1000}$. Over the common denominator 1,000, the part after the point is $\frac{300}{1000} + \frac{70}{1000} + \frac{5}{1000} = \frac{375}{1000}$, so 24.375 is 24 and 375 thousandths.

That last sentence is also how to read a decimal in full: the whole part, then "and" for the point, then the digits after the point as one number followed by the name of the last place. So 24.375 is "twenty-four and three hundred seventy-five thousandths", and 2.05 is "two and five hundredths". In everyday speech, people say the digits after the point one at a time: "twenty-four point three seven five". A decimal less than 1 is written with a 0 in front, as 0.45 rather than .45, so the point can't be missed.

## How to do it

### Converting between decimals and fractions

To write a decimal as a fraction:

1. Put the digits after the point over 1 followed by as many zeros as there are decimal places. The whole part stays as it is.
2. Simplify.

For example, $0.45 = \frac{45}{100} = \frac{9}{20}$, and $2.125 = 2\frac{125}{1000} = 2\frac{1}{8}$.

To write a fraction as a decimal:

1. If the denominator is a factor of 10, 100 or 1,000 (such as 2, 4, 5, 8, 20, 25 or 125), scale the fraction to that denominator: $\frac{7}{20} = \frac{35}{100} = 0.35$.
2. Otherwise, divide the numerator by the denominator and continue into decimals, as in Example 4 of [long division](07-long-division.md): $\frac{3}{8} = 3 \div 8 = 0.375$.

Some fractions never finish. The division $1 \div 3$ leaves a remainder of 1 at every step, so $\frac{1}{3} = 0.333\ldots$, written $0.\overline{3}$, and no decimal with a fixed number of places equals it exactly; 0.33 is $\frac{1}{300}$ short. [Multiplying and dividing decimals](13-multiplying-and-dividing-decimals.md) explains which fractions repeat and why, and repeating decimals come back in [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md).

### Comparing decimals

1. Pad the decimals with zeros at the end so they all have the same number of decimal places. Zeros at the end, after the point, don't change a value: $0.5 = 0.50$, because $\frac{5}{10} = \frac{50}{100}$.
2. Compare the whole parts. If they are equal, compare the digits after the point from left to right, as with whole numbers. The first place where the digits differ decides.

### Rounding decimals

The rule is the one for whole numbers in [place value and rounding](01-place-value-and-rounding.md).

1. Find the digit in the place you are rounding to. "To two decimal places" means to the hundredths place.
2. Look at the next digit to the right. If it is 5 or more, add 1 to the rounding digit, carrying if that digit is a 9. If it is less than 5, leave the rounding digit alone.
3. Drop every digit to the right of the rounding place. Keep a 0 that sits in the rounding place, so that the answer shows how many places it was rounded to.

Money in dollars goes to two decimal places, the nearest cent: \$5.5 is written \$5.50.

### Adding and subtracting

1. Write the numbers in a column with their decimal points lined up. A whole number has its point at its right end: $6 = 6.0$.
2. Pad with zeros so that every number has the same number of decimal places.
3. Add or subtract column by column from the right, as with whole numbers. Carrying and borrowing work across the point.
4. Put the decimal point in the answer directly under the points above it.
5. Check: estimate with whole numbers, and after a subtraction, add the answer back.

## Worked examples

<div class="example" markdown>

### Example 1: adding three decimals

Work out $14.3 + 2.75 + 6$.

Step 1: line up the decimal points. The 6 has no point written, so its point goes at its right end.

Step 2: the longest number, 2.75, has two decimal places, so pad the others: 14.3 becomes 14.30 and 6 becomes 6.00.

Step 3: add from the right. In the hundredths column, $0 + 5 + 0 = 5$. In the tenths column, $3 + 7 + 0 = 10$, so write 0 and carry 1 to the ones: ten tenths make one, as ten dimes make a dollar. In the ones column, $4 + 2 + 6 + 1 = 13$, so write 3 and carry 1. In the tens column, $1 + 1 = 2$.

Step 4: the point goes under the points above, which gives 23.05:

$$
\begin{array}{r}
14.30 \\
2.75 \\
+\;\;6.00 \\
\hline
23.05
\end{array}
$$

Step 5: estimate with whole numbers: $14 + 3 + 6 = 23$, which matches.

<div class="warning" markdown>

Watch out: lining up the last digits instead of the points puts the 3 tenths of 14.3 in the hundredths column. Then $14.3 + 2.75$ comes out as 4.18, which is really $1.43 + 2.75$. The estimate catches it, since the sum should be about $14 + 3 = 17$. Line up the points, and the digits line up by place.

</div>

</div>

<div class="example" markdown>

### Example 2: making change

You pay for a \$13.47 order with a \$20 bill. Your change is $20 - 13.47$. Steps 1 and 2 write 20 as 20.00.

Step 3 needs a borrow right away: 7 hundredths can't come out of 0 hundredths, and the tenths and ones are 0 too. So borrow from the tens. Since $20.00 = 19.90 + 0.10$, you can rewrite 20.00 as 1 ten, 9 ones, 9 tenths and 10 hundredths. Then $10 - 7 = 3$, $9 - 4 = 5$, $9 - 3 = 6$ and $1 - 1 = 0$:

$$
\begin{array}{r}
20.00 \\
-\;13.47 \\
\hline
6.53
\end{array}
$$

The change is \$6.53. Check by adding back: $13.47 + 6.53 = 20.00$.

</div>

<div class="example" markdown>

### Example 3: putting decimals in order

Put 0.5, 0.45, 0.405 and 0.054 in order from smallest to largest.

Step 1 of comparing: pad to three decimal places, the most that any of them has. That gives 0.500, 0.450, 0.405 and 0.054, which are 500, 450, 405 and 54 thousandths. Step 2: the whole parts are all 0, so compare as thousandths:

$$
0.054 < 0.405 < 0.45 < 0.5.
$$

<div class="warning" markdown>

Watch out for "longer is bigger". With whole numbers, more digits means a bigger number, but after the point the extra digits are smaller and smaller pieces. So 0.45 is less than 0.5: it is 45 hundredths, and 0.5 is 50 hundredths. Comparing the tenths digits first settles it, since 4 tenths is less than 5 tenths. Saying "point four five" instead of "point forty-five" helps, because the second makes 45 sound bigger than 5.

</div>

</div>

<div class="example" markdown>

### Example 4: rounding with a carry

Round 2.6951 to the nearest hundredth. Step 1: the hundredths digit is 9. Step 2: the next digit is 5, so add 1 to the 9. That makes 10 hundredths, so write 0 and carry 1 into the tenths, where 6 becomes 7. Step 3: drop the digits after the hundredths place.

The answer is 2.70. The 0 stays, because it shows the number was rounded to the hundredths place; 2.7 would read as rounded to the tenths. Check: 2.6951 is between 2.69 and 2.70, and it is closer to 2.70.

</div>

## Edge cases and common mistakes

Two mistakes are flagged above where they happen: lining up the last digits instead of the points (Example 1), and "longer is bigger" (Example 3). Here are the others.

<div class="warning" markdown>

Watch out: round once, from the original number. To round 2.6449 to the nearest tenth, look at the hundredths digit, which is 4, so the answer is 2.6. Rounding in stages, first to 2.645, then to 2.65, then to 2.7, pushes the number up at each stage and gives the wrong answer.

</div>

Zeros change a decimal only in some positions. A zero at the end, after the point, changes nothing: $3.4 = 3.40$. A zero between the point and a digit does change it: 0.05 is five hundredths, a tenth of 0.5. And a zero at the end of a whole number changes it too, since 50 is not 5. Dropping the 0 from 2.05 turns it into 2.5.

A rounded decimal is not equal to the fraction it came from. Since $\frac{2}{3} = 0.666\ldots$, rounding to three places gives 0.667, but $0.667 \times 3 = 2.001$, not 2. Use the fraction, or keep more places, when the answer must be exact.

## Tricks and shortcuts

Make change by counting up from the price. From \$13.47, add 3 cents to reach \$13.50, then 50 cents to reach \$14, then \$6 to reach \$20. The change is $0.03 + 0.50 + 6.00 = 6.53$, the same as Example 2, with no borrowing.

Add a decimal near a whole number by rounding it and fixing the difference afterwards. To work out $4.98 + 3.47$, add 5 instead, which gives 8.47, then take back the extra 0.02: the answer is 8.45.

A few fractions are worth knowing as decimals. Halves, quarters and fifths are quick ($\frac{1}{4} = 0.25$, $\frac{3}{5} = 0.6$), and each eighth adds 0.125, so $\frac{1}{8} = 0.125$, $\frac{3}{8} = 0.375$, $\frac{5}{8} = 0.625$ and $\frac{7}{8} = 0.875$. The table in [Percents](../02-middle-school/02-ratios-rates-percents/03-percents.md#tricks-and-shortcuts) lists more.

## FAQ

### Why is there no "oneths" place?

The places are arranged around the ones place, not around the point. Tens sit one place to the left of the ones and tenths one place to the right; hundreds are two places left and hundredths two places right. The ones place is its own mirror image, so there is nothing for "oneths" to name: one oneth would just be one.

## Practice

### Warm-up

1\. Write as decimals: (a) seven and four hundredths, (b) $\frac{3}{1000}$, (c) $\frac{9}{25}$. Write as fractions in simplest form: (d) 0.6, (e) 2.125.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The whole part is 7, and 4 hundredths puts a 4 in the second place after the point, with 0 tenths: 7.04.
- (b) Three thousandths puts a 3 in the third place: 0.003.
- (c) Scale to hundredths: $\frac{9}{25} = \frac{36}{100} = 0.36$.
- (d) One decimal place: $0.6 = \frac{6}{10} = \frac{3}{5}$.
- (e) Three decimal places: $2.125 = 2\frac{125}{1000} = 2\frac{1}{8}$, which is $\frac{17}{8}$ as an improper fraction.

Check: $3 \div 5 = 0.6$ and $17 \div 8 = 2.125$.

</details>

2\. Put in order from smallest to largest: 0.7, 0.07, 0.707, 0.77, 0.077.

<details class="solution" markdown>
<summary>Solution</summary>

Pad to three decimal places: 0.700, 0.070, 0.707, 0.770 and 0.077. As thousandths these are 700, 70, 707, 770 and 77, so the order is

$$
0.07 < 0.077 < 0.7 < 0.707 < 0.77.
$$

Check: the two numbers with 0 tenths come first, and 0.77 is last because it has the most tenths and then the most hundredths.

</details>

### Standard

3\. A grocery receipt lists \$3.49, \$12.99, \$0.89 and \$6.50. What is the total, and how much change do you get from \$30?

<details class="solution" markdown>
<summary>Solution</summary>

All four prices have two decimal places, so they line up as they are. Adding one at a time: $3.49 + 12.99 = 16.48$, then $16.48 + 0.89 = 17.37$, then $17.37 + 6.50 = 23.87$. The total is \$23.87.

The change is $30.00 - 23.87 = 6.13$, so \$6.13. Counting up gives the same answer: 13 cents takes \$23.87 to \$24, and \$6 more takes it to \$30.

Check: rounding each price to the nearest dollar gives $3 + 13 + 1 + 7 = 24$, close to \$23.87. Adding back, $23.87 + 6.13 = 30.00$.

</details>

4\. Write $\frac{5}{16}$ as a decimal by long division, then round it to the nearest hundredth.

<details class="solution" markdown>
<summary>Solution</summary>

Sixteen doesn't go into 5, so write 0 and a point and bring down zeros. Then $50 \div 16 = 3$ remainder 2, $20 \div 16 = 1$ remainder 4, $40 \div 16 = 2$ remainder 8, and $80 \div 16 = 5$ remainder 0. So $\frac{5}{16} = 0.3125$.

To round to the hundredths, look at the thousandths digit. It is 2, which is less than 5, so the answer is 0.31.

Check: $\frac{5}{16}$ is a little less than $\frac{5}{15} = \frac{1}{3} = 0.333\ldots$, and 0.3125 is a little less than that.

</details>

### Challenge

5\. Find a decimal between 0.4 and 0.41, and one between 0.999 and 1. Is there a largest decimal that is less than 1?

<details class="solution" markdown>
<summary>Solution</summary>

Pad with a zero to make room: 0.4 and 0.41 are 0.400 and 0.410, and every decimal from 0.401 to 0.409 lies between them, such as 0.405. In the same way, 0.999 and 1 are 0.9990 and 1.0000, so 0.9995 lies between them.

There is no largest decimal less than 1. Take any decimal less than 1, add a zero at its end, and change that zero to a 5. The new number is bigger, because it has an extra 5 in a place smaller than all of its other digits. It is still less than 1, because the old number was short of 1 by at least one unit of its last place (0.999 is 0.001 short), and the 5 adds only half of that unit. So there is always a bigger one.

Check: $0.4 < 0.405 < 0.41$ and $0.999 < 0.9995 < 1$, comparing with the padded forms.

</details>

6\. This one reviews [adding and subtracting fractions](10-adding-and-subtracting-fractions.md). Work out $\frac{3}{4} + \frac{2}{5}$ with fractions, then again by converting both to decimals first. Check that the two answers agree.

<details class="solution" markdown>
<summary>Solution</summary>

With fractions, the common denominator is 20: $\frac{15}{20} + \frac{8}{20} = \frac{23}{20} = 1\frac{3}{20}$.

With decimals, $\frac{3}{4} = 0.75$ and $\frac{2}{5} = 0.4 = 0.40$, so the sum is $0.75 + 0.40 = 1.15$.

Check: $\frac{3}{20} = \frac{15}{100} = 0.15$, so $1\frac{3}{20} = 1.15$, and the two answers agree.

</details>

## Where this shows up

- The next lesson, [multiplying and dividing decimals](13-multiplying-and-dividing-decimals.md), uses decimal places to place the point in a product, and [powers of ten](14-powers-of-ten.md) explains why multiplying by 10 moves the point. [Percents](../02-middle-school/02-ratios-rates-percents/03-percents.md) are hundredths with a new name.
- Every money calculation in the finance folder rounds to two decimal places, the nearest cent, starting with [tips, discounts and HST](../08-financial-math/01-everyday-money/01-tips-discounts-and-hst.md).
- Places after the point work the same way in other bases: in binary they are worth $\frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \dots$ ([number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md)). That is why 0.1 can't be stored exactly in a float ([floating point basics](../06-cs-math/01-number-representation/04-floating-point-basics.md)).
