# Powers of ten

After this lesson you can multiply and divide by 10, 100, 1000, 0.1 and 0.01 by moving the decimal point, write powers of ten with exponents, and read metric prefixes such as kilo and milli as powers of ten.

Before this: [decimals: place value, adding and subtracting](12-decimals-place-value-and-adding.md) and [multiplying and dividing decimals](13-multiplying-and-dividing-decimals.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $0.47 \times 1000$ and $36 \div 100$.
2. Write $10^5$ as an ordinary number, and write 0.001 as a power of ten.
3. A kilometre is $10^3$ metres and a gigabyte is $10^9$ bytes. Write 2.5 km in metres and 2.5 GB in bytes.

<details class="solution" markdown>
<summary>Answers</summary>

1. 470 and 0.36. Multiplying by 1000 moves the decimal point three places right, and dividing by 100 moves it two places left.
2. The power $10^5$ is 100,000, a 1 followed by five zeros. Since $0.001 = \frac{1}{1000}$, it is $10^{-3}$.
3. In metres, 2.5 km is $2.5 \times 1000 = 2{,}500$ m. In bytes, 2.5 GB is $2.5 \times 10^9 = 2{,}500{,}000{,}000$ bytes.

</details>

## The idea

Ten friends each chip in \$4.75 for a gift. Think of \$4.75 as 4 dollars, 7 dimes and 5 cents. Ten times that is 40 dollars, 70 dimes and 50 cents. But 70 dimes make 7 dollars, and 50 cents make 5 dimes, so the total is \$47.50. Each coin has turned into the next bigger kind, because each kind is worth exactly ten of the kind below it.

The place-value chart shows the same thing. Every digit moves one place to the left:

| | Tens | Ones | Tenths | Hundredths |
|---|---|---|---|---|
| $4.75$ | | 4 | 7 | 5 |
| $4.75 \times 10 = 47.5$ | 4 | 7 | 5 | |

This works because each place is worth ten times the place to its right: a ten is ten ones, a one is ten tenths, a tenth is ten hundredths. Multiplying by 10 makes the value of each digit ten times bigger, and that is the value of the next place to the left. Written out with the [distributive property](04-properties-of-operations.md), it is

$$
10 \times 4.75 = 10 \times 4 + 10 \times 0.7 + 10 \times 0.05 = 40 + 7 + 0.5 = 47.5.
$$

So the digits move and the decimal point stays put. On paper it is quicker to move the point the other way, which gives the same result: "move the point one place right" is shorthand for "every digit moves one place left". Dividing by 10 runs the chart backwards. Multiplying by 100 is multiplying by 10 twice, so the digits move two places.

## Definitions

A **power of ten** is a number made by multiplying 10 by itself some number of times, such as $10 \times 10 \times 10 = 1000$. The numbers 1, 0.1 and 0.01 also count, as the pattern below shows.

Exponent notation writes such products in short form. For a number $b$ and a positive integer $n$,

$$
b^n = \underbrace{b \times b \times \cdots \times b}_{n \text{ factors}}.
$$

The number $b$ is the **base**, the small raised number $n$ is the **exponent**, and $b^n$ is a **power** of $b$, read "$b$ to the power $n$" or "$b$ to the $n$". In $10^3$ the base is 10 and the exponent is 3, so $10^3 = 10 \times 10 \times 10 = 1000$. Two exponents have their own names: $10^2$ is "ten squared" and $10^3$ is "ten cubed", after the area of a square and the volume of a cube ([geometry basics](16-geometry-basics-area-perimeter-volume.md)).

In plain words, the exponent counts how many copies of the base are multiplied together. So for powers of ten, $10^n$ is a 1 followed by $n$ zeros.

| Power | Product | Value | Name |
|---|---|---|---|
| $10^1$ | $10$ | 10 | ten |
| $10^2$ | $10 \times 10$ | 100 | hundred |
| $10^3$ | $10 \times 10 \times 10$ | 1,000 | thousand |
| $10^6$ | six 10s | 1,000,000 | million |
| $10^9$ | nine 10s | 1,000,000,000 | billion |

### Zero and negative exponents

Read the pattern below from the top down. Each line divides the one above it by 10, and the exponent drops by 1:

| Power | Value |
|---|---|
| $10^3$ | 1,000 |
| $10^2$ | 100 |
| $10^1$ | 10 |
| $10^0$ | 1 |
| $10^{-1}$ | 0.1 |
| $10^{-2}$ | 0.01 |
| $10^{-3}$ | 0.001 |

After $10^1 = 10$, one more division gives $10 \div 10 = 1$, so the next line is $10^0 = 1$. This is a definition, because "multiply zero copies of 10" gives no instructions, and 1 is the only value that keeps the pattern going. [Exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md) uses the same definition for every base: $b^0 = 1$ for every number $b \ne 0$, where $\ne$ means "is not equal to".

Going further down gives negative exponents, which this lesson only previews. For a positive integer $n$,

$$
10^{-n} = \frac{1}{10^n}, \qquad \text{so} \qquad 10^{-2} = \frac{1}{100} = 0.01.
$$

A negative exponent means "divide by that many 10s", which gives a small positive number, not a negative one. In decimal form, $10^{-n}$ has its 1 in the $n$-th place after the point.

### Metric prefixes

A **metric prefix** is a word put in front of a unit to multiply it by a power of ten. A kilometre is $10^3$ metres, and a milligram is $10^{-3}$ grams. These are the prefixes you will meet most:

| Prefix | Symbol | Power of ten | Value | Example |
|---|---|---|---|---|
| giga | G | $10^9$ | 1,000,000,000 | gigabyte (GB) |
| mega | M | $10^6$ | 1,000,000 | megabyte (MB) |
| kilo | k | $10^3$ | 1,000 | kilometre (km), kilogram (kg) |
| (none) | | $10^0$ | 1 | metre (m), gram (g), litre (L) |
| centi | c | $10^{-2}$ | 0.01 | centimetre (cm) |
| milli | m | $10^{-3}$ | 0.001 | millimetre (mm), millilitre (mL) |

The symbols are case-sensitive: M is mega, while m is milli (and, on its own, the metre). In computing, "kilo" sometimes means $2^{10} = 1{,}024$ instead of 1,000, for the reason given in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md). This book uses the metric meaning unless it says otherwise.

## How to do it

To multiply or divide a number by a power of ten:

1. Find how many places to move. For 10, 100 or 1000, count the zeros or read the exponent: 1000 and $10^3$ both mean 3 places. For 0.1, 0.01 or 0.001, count the decimal places: 0.01 means 2 places.
2. Pick the direction. Multiplying by 10, 100 or 1000 makes the number bigger, so the point moves right, and dividing moves it left. With 0.1, 0.01 or 0.001 the directions swap (see the table below).
3. Find the decimal point. A whole number has an unwritten one at its right end: 47 is 47.0.
4. Move the point that many places, one digit at a time.
5. Fill each empty place with a 0. Moving right past the last digit, write zeros at the end. Moving left past the first digit, write zeros in front of it, and a 0 before the point.
6. Tidy up and check. Drop zeros at the end of the decimal part (2.50 is 2.5) and a point with nothing after it. Then compare the answer with an estimate.

Here is Step 2 as a table:

| Operation | Same as | The point moves |
|---|---|---|
| $\times 10$, $\times 100$, $\times 1000$ | | right 1, 2 or 3 places |
| $\div 10$, $\div 100$, $\div 1000$ | | left 1, 2 or 3 places |
| $\times 0.1$, $\times 0.01$, $\times 0.001$ | $\div 10$, $\div 100$, $\div 1000$ | left 1, 2 or 3 places |
| $\div 0.1$, $\div 0.01$, $\div 0.001$ | $\times 10$, $\times 100$, $\times 1000$ | right 1, 2 or 3 places |

The last two rows come from fractions. Since $0.1 = \frac{1}{10}$, multiplying by 0.1 takes a tenth of the number, which is dividing by 10. Dividing by 0.1 asks how many tenths fit into the number, and every whole holds ten of them, so the answer is ten times as big ([multiplying and dividing fractions](11-multiplying-and-dividing-fractions.md) has the general rule).

## Worked examples

<div class="example" markdown>

### Example 1: multiplying 2.6 by 1000

Step 1: 1000 has three zeros, so the point moves 3 places.

Step 2: multiplying by 1000 makes the number bigger, so the point moves right.

Step 3: in 2.6 the point sits between the 2 and the 6.

Steps 4 and 5: move the point right one place at a time. After the first place there are no digits left, so each further place gets a 0:

| Places moved | Number |
|---|---|
| 0 | 2.6 |
| 1 | 26 |
| 2 | 260 |
| 3 | 2600 |

Step 6: the answer is $2.6 \times 1000 = 2{,}600$. Check: 2.6 is a little under 3, and $3 \times 1000 = 3{,}000$, so the answer should be a little under 3,000. Dividing back also works: $2{,}600 \div 1000 = 2.6$.

<div class="warning" markdown>

Watch out at Step 5: "multiplying by 1000 adds three zeros" is only true for whole numbers, as in $26 \times 1000 = 26{,}000$. Adding three zeros to 2.6 gives 2.6000, which is still 2.6. With a decimal point, move the point.

</div>

</div>

<div class="example" markdown>

### Example 2: moving left

Work out $45 \div 1000$ and $380 \times 0.01$.

For $45 \div 1000$, Steps 1 and 2 say 3 places left, and Step 3 puts the point after the 5. Moving it gives 4.5, then 0.45, and the third move passes the 4, so a 0 fills the empty place in front of it (Step 5): 0.045.

<div class="warning" markdown>

Watch out: stopping at 0.45 is the common slip. The point has to move three places, one for each zero in 1000, and the 0 between the point and the 4 records the third move. Check the size: 45 is far less than 1000, so the answer must be far less than 1, and $0.045 \times 1000 = 45$.

</div>

For $380 \times 0.01$, the number 0.01 has two decimal places, and multiplying by it is the same as dividing by 100, so the point moves 2 places left: 3.80, which tidies to 3.8. Check: 0.01 is 1%, and 1% of 380 is 3.8 ([percents](../02-middle-school/02-ratios-rates-percents/03-percents.md)).

</div>

<div class="example" markdown>

### Example 3: dividing by 0.1

Work out $6.4 \div 0.1$.

The question is how many tenths fit into 6.4. Each whole holds 10 tenths, so 6 wholes hold 60 tenths, and the extra 0.4 is 4 more, which makes 64. The table in Step 2 agrees: dividing by 0.1 moves the point one place right.

The answer is bigger than the number you started with, and that is correct. Dividing a positive number by a number between 0 and 1 always gives a bigger answer. Check: $64 \times 0.1 = 6.4$.

</div>

<div class="example" markdown>

### Example 4: a number times a power of ten

Work out $3.2 \times 10^4$ and $7 \times 10^{-3}$.

The exponent is the number of places. In $3.2 \times 10^4$ the point moves 4 places right: 32, 320, 3200, 32000. So $3.2 \times 10^4 = 32{,}000$.

In $7 \times 10^{-3}$, multiplying by $10^{-3} = 0.001$ is dividing by 1000, so the point moves 3 places left: 0.7, 0.07, 0.007. So $7 \times 10^{-3} = 0.007$.

Check: $10^4 = 10{,}000$ and $3.2 \times 10{,}000 = 32{,}000$; and $0.007 \times 1000 = 7$. Writing a number as a decimal times a power of ten like this is the start of [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md).

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the exponent is a count, not a factor. The power $10^3$ is $10 \times 10 \times 10 = 1000$, not $10 \times 3 = 30$. Saying it aloud helps: "three tens multiplied together".

</div>

<div class="warning" markdown>

Watch out: $10^{-2}$ is $0.01$, not $-100$ and not $-20$. A negative exponent divides by 10 that many times. Every power of 10 is a positive number, however negative its exponent.

</div>

<div class="warning" markdown>

Watch out for capital letters in prefixes. A power station's output is measured in MW (megawatts) and a laser pointer's in mW (milliwatts). Since 1 MW is 1,000,000 watts and 1 mW is 0.001 watts, the two units differ by a factor of a billion. Copy the symbol exactly as written.

</div>

Zero needs a moment's thought in two places. Zero times every power of ten is 0, so there is nothing to move. And the power $10^0$ is 1, not 0, so multiplying by $10^0$ moves the point zero places and leaves the number as it was.

Zeros inside a number stay where they are. In $4.05 \times 100 = 405$, the 0 is a real digit (zero tenths) and moves with the others. Only the empty places at the ends get new zeros.

## Tricks and shortcuts

To multiply numbers that end in zeros, multiply the front parts and then write all the zeros at the end. For $300 \times 4000$, work out $3 \times 4 = 12$, then attach the $2 + 3 = 5$ zeros: 1,200,000. This works because $300 \times 4000 = 3 \times 4 \times 100 \times 1000$, and $100 \times 1000 = 10^2 \times 10^3 = 10^5$. When you multiply powers of ten, the exponents add, which is the first of the [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).

To divide, cross off the same number of end zeros from both numbers. In $36{,}000 \div 900$, cross off two from each to get $360 \div 9 = 40$. Dividing both numbers by 100 doesn't change the quotient, for the same reason that $\frac{36000}{900}$ and $\frac{360}{9}$ are [equivalent fractions](09-fractions-and-equivalent-fractions.md).

The full list of metric prefixes from kilo down to milli is kilo, hecto, deca, (the unit), deci, centi, milli, and each unit in the list is ten times smaller than the one before it. One memory aid is "King Henry Doesn't Usually Drink Chocolate Milk", whose first letters are K, H, D, U, D, C, M. To go from metres to centimetres, count the steps from U to C (two) and move the point two places right, since the smaller unit needs a bigger number.

Before you move the point, ask whether the answer should be bigger or smaller than the number you started with. That one question catches most direction mistakes.

## Practice

### Warm-up

1\. Work out (a) $0.38 \times 100$, (b) $5.1 \div 1000$, (c) $72 \times 0.1$ and (d) $0.9 \div 0.01$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Two places right: 38.
- (b) Three places left. From 5.1 that gives 0.51, then 0.051, then 0.0051, with zeros filling the empty places: 0.0051.
- (c) Multiplying by 0.1 is dividing by 10, so one place left: 7.2.
- (d) Dividing by 0.01 is multiplying by 100, so two places right: 0.9 becomes 9, then 90.

Check by undoing each one: $38 \div 100 = 0.38$, $0.0051 \times 1000 = 5.1$, $7.2 \times 10 = 72$ and $90 \times 0.01 = 0.9$.

</details>

2\. (a) Write each number as a power of ten: 1,000,000; 10; 1; 0.001. (b) Write $10^4$ and $10^{-2}$ as ordinary numbers.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Count the zeros, or the decimal places for a number below 1: $1{,}000{,}000 = 10^6$, $10 = 10^1$, $1 = 10^0$ and $0.001 = 10^{-3}$.

(b) The power $10^4$ is 10,000, a 1 and four zeros, and $10^{-2} = \frac{1}{100} = 0.01$.

Check: $10^6 = 10 \times 10 \times 10 \times 10 \times 10 \times 10$, and six 10s multiplied together give a 1 followed by six zeros.

</details>

### Standard

3\. Find the power of ten that goes in each box: (a) $0.072 \times \square = 72$, (b) $5{,}600 \div \square = 5.6$, (c) $8 \times \square = 0.08$, (d) $1.5 \div \square = 150$.

<details class="solution" markdown>
<summary>Solution</summary>

Compare the point before and after, then use the table in Step 2.

- (a) The point moved 3 places right while multiplying, so the box is 1000.
- (b) The point moved 3 places left while dividing, so the box is 1000.
- (c) The point moved 2 places left, but the operation is a multiplication, so the box is 0.01.
- (d) The point moved 2 places right, but the operation is a division, so the box is 0.01.

Check: $0.072 \times 1000 = 72$, $5{,}600 \div 1000 = 5.6$, $8 \times 0.01 = 0.08$ and $1.5 \div 0.01 = 150$.

</details>

4\. A phone plan includes 3.5 GB of data a month. Use giga $= 10^9$, mega $= 10^6$ and kilo $= 10^3$. (a) How many megabytes is that? (b) How many bytes? (c) How many times bigger is a gigabyte than a kilobyte?

<details class="solution" markdown>
<summary>Solution</summary>

(a) A gigabyte is $10^9$ bytes and a megabyte is $10^6$ bytes, so 1 GB is $10^9 \div 10^6 = 1000$ MB. Then $3.5 \times 1000 = 3{,}500$ MB.

(b) In $3.5 \times 10^9$ the point moves 9 places right, giving 3,500,000,000 bytes.

(c) Divide the two sizes: $1{,}000{,}000{,}000 \div 1{,}000 = 1{,}000{,}000$, so a gigabyte is a million times bigger. In exponents, $10^9 \div 10^3 = 10^6$.

Check: $3{,}500 \times 10^6 = 3{,}500{,}000{,}000$, the same as (b).

</details>

### Challenge

5\. A pack of 500 sheets of printer paper is 5 cm thick. How thick is one sheet, in millimetres and in metres? Write the answer in metres as a power of ten.

<details class="solution" markdown>
<summary>Solution</summary>

A centimetre is $10^{-2}$ m and a millimetre is $10^{-3}$ m, so 1 cm = 10 mm, and 5 cm = 50 mm.

One sheet is $50 \div 500$ mm. Cross off one end zero from each number: $5 \div 50 = 0.1$ mm.

In metres, divide by 1000, which moves the point 3 places left: $0.1\ \text{mm} = 0.0001\ \text{m}$. The 1 is in the fourth place after the point, so this is $10^{-4}$ m.

Check: $0.1 \times 500 = 50$ mm, which is 5 cm. The size is believable too: a single sheet is much thinner than a millimetre.

</details>

6\. This one reviews [multiplying and dividing decimals](13-multiplying-and-dividing-decimals.md). Work out $0.6 \times 0.05$ and $0.6 \div 0.05$ by writing each decimal as a whole number times a power of ten.

<details class="solution" markdown>
<summary>Solution</summary>

Write $0.6 = 6 \times 0.1$ and $0.05 = 5 \times 0.01$. For the product, multiply the whole numbers and the powers of ten separately:

$$
0.6 \times 0.05 = (6 \times 5) \times (0.1 \times 0.01) = 30 \times 0.001 = 0.03.
$$

For the quotient, multiply both numbers by 100, which doesn't change a quotient (the same reason as crossing off zeros): $0.6 \div 0.05 = 60 \div 5 = 12$.

Check: $0.03 \div 0.05 = 0.6$, since $0.05 \times 0.6 = 0.03$, and $12 \times 0.05 = 0.6$. The quotient is bigger than 0.6 because 0.05 is less than 1, as in Example 3.

</details>

## Where this shows up

- [Scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md) writes very large and very small numbers as a decimal times a power of ten, such as $3.2 \times 10^4$, and [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md) extends $10^2 \times 10^3 = 10^5$ to every base.
- The next lesson, [measurement and unit conversion](15-measurement-and-unit-conversion.md), converts between metric units by moving the decimal point.
- In binary each place is worth twice the one to its right, so multiplying by 2 moves every digit one place left, which is the bit shift `x << 1` in code ([number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md)). Python writes $3.2 \times 10^4$ as `3.2e4` and $10^3$ as `10**3`.
