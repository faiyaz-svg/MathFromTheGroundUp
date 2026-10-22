# Multiplying and dividing decimals

After this lesson you can multiply and divide decimals on paper, place the decimal point by counting places and check it with an estimate, and write any fraction as a decimal that either stops or repeats.

Before this: [multi-digit multiplication](05-multi-digit-multiplication.md), [long division](07-long-division.md), [multiplying and dividing fractions](11-multiplying-and-dividing-fractions.md) and [decimals: place value, adding and subtracting](12-decimals-place-value-and-adding.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $0.36 \times 2.5$.
2. Work out $7.56 \div 0.18$.
3. Write $\frac{5}{11}$ as a decimal.

<details class="solution" markdown>
<summary>Answers</summary>

1. 0.9. Since $36 \times 25 = 900$ and the factors have $2 + 1 = 3$ decimal places, the product is 0.900, which is 0.9. Estimate: $0.4 \times 2 = 0.8$.
2. 42. Multiply both numbers by 100 to get $756 \div 18 = 42$. Check: $42 \times 0.18 = 7.56$.
3. It is $0.\overline{45}$, that is, $0.4545\ldots$ with 4 and 5 repeating forever. Eleven goes into 50 four times with remainder 6, and into 60 five times with remainder 5. The remainder 5 is where the division started, so the same two steps repeat.

</details>

## The idea

Apples cost \$3.40 a kilogram, and you buy 2.5 kg. A quick estimate says about $3 \times 3 = 9$ dollars. For the exact amount, ignore the points and multiply: $34 \times 25 = 850$. The estimate says the answer is near 9, so the point goes after the 8, and the apples cost \$8.50.

Counting decimal places gives the same position, and fractions show why. Since $3.4 = \frac{34}{10}$ and $2.5 = \frac{25}{10}$,

$$
3.4 \times 2.5 = \frac{34}{10} \times \frac{25}{10} = \frac{34 \times 25}{10 \times 10} = \frac{850}{100} = 8.50.
$$

Each factor had one decimal place, which put a 10 in its denominator, and the two 10s multiplied to 100, which means two decimal places in the product. The whole-number multiplication does all the work. The decimal places only say what power of 10 to divide by at the end.

Division turns into whole-number division in a similar way. How many 0.25 L glasses does a 2 L bottle fill? Measured in hundredths of a litre, the bottle holds 200 and each glass takes 25, so the answer is $200 \div 25 = 8$. Changing the unit multiplied both numbers by 100, and that doesn't change how many glasses fit.

## Definitions

When long division turns a fraction into a decimal, the digits either stop or go on forever.

A **terminating decimal** has a finite number of decimal places, such as $\frac{7}{8} = 0.875$. A **repeating decimal** has a block of one or more digits that, from some place on, repeats forever. The block is written once with a bar over it: $\frac{1}{3} = 0.333\ldots = 0.\overline{3}$ and $\frac{5}{11} = 0.4545\ldots = 0.\overline{45}$. The bar can start after some digits that don't repeat, as in $\frac{7}{12} = 0.58\overline{3}$.

In plain words, a decimal terminates when the long division reaches a remainder of 0, and it repeats when a remainder comes back. For a fraction these are the only two possibilities; [Fractions as decimals](#fractions-as-decimals) below shows why.

## How to do it

### Multiplying decimals

1. Estimate. Round each factor to a number that is easy to multiply, and work out the rough answer.
2. Multiply as whole numbers, ignoring the points.
3. Count the decimal places in the two factors together. From the right end of the product, count that many digits to the left and put the point there. If the product has too few digits, write zeros in front of it first.
4. Check the answer against the estimate. Drop zeros at the end after the point only now, once the point is in place.

Step 3 works for every pair of factors. A decimal with $m$ decimal places is a whole number divided by $10^m$, which is 1 followed by $m$ zeros. So if the factors have $m$ and $n$ decimal places, and $a$ and $b$ are the factors with their points removed, then

$$
\frac{a}{10^m} \times \frac{b}{10^n} = \frac{a \times b}{10^{m+n}}.
$$

The denominator is 1 followed by $m + n$ zeros, so the product has $m + n$ decimal places.

### Dividing decimals

1. Make the divisor a whole number. Move its point to its right end, and move the point in the dividend the same number of places to the right, writing zeros on the end of the dividend if it runs out of digits.
2. Estimate the quotient.
3. Divide by long division. Put a point in the quotient directly above the point in the dividend, and divide as with whole numbers.
4. If there is a remainder when the dividend's digits run out, write zeros after it and keep bringing them down. Stop when the remainder is 0, when a remainder repeats, or when you have one more place than you need for rounding.
5. Check: multiply the quotient by the original divisor. You should get the original dividend.

Moving a point one place to the right multiplies the number by 10, because every digit moves into a place worth ten times as much ([powers of ten](14-powers-of-ten.md) has more). Step 1 is allowed because a division is a fraction, and multiplying the numerator and the denominator by the same number gives an equivalent fraction:

$$
7.56 \div 0.18 = \frac{7.56}{0.18} = \frac{7.56 \times 100}{0.18 \times 100} = \frac{756}{18}.
$$

So the quotient doesn't change. In money terms, asking how many 18-cent items \$7.56 buys is the same as dividing 756 cents by 18 cents. The point goes straight up in step 3 because long division works through the dividend one place at a time: the digit you find while dividing the tenths counts tenths, so it belongs in the tenths place of the quotient.

### Fractions as decimals

To write $\frac{n}{d}$ as a decimal, divide $n$ by $d$ using steps 3 and 4. [Long division](07-long-division.md) already did this for $7 \div 8 = 0.875$ and $1 \div 3 = 0.\overline{3}$. Two facts say what can happen in general.

First, the digits of a fraction always stop or repeat. Each remainder in a division by $d$ is one of the numbers $0, 1, \dots, d - 1$. A remainder of 0 ends the division. Otherwise every remainder is one of only $d - 1$ nonzero values, so a remainder has to come back within $d$ steps, and from then on the division repeats the same steps forever. So the repeating block of $\frac{n}{d}$ is at most $d - 1$ digits long.

Second, a fraction in simplest form is a terminating decimal exactly when its denominator has no prime factors other than 2 and 5 ([factors, multiples and primes](08-factors-multiples-and-primes.md)). A terminating decimal is a fraction over a power of 10, and $10 = 2 \times 5$. If the denominator is built from 2s and 5s, multiply by more 2s or 5s until they pair up into 10s:

$$
\frac{3}{40} = \frac{3}{2 \times 2 \times 2 \times 5} = \frac{3 \times 5 \times 5}{2 \times 2 \times 2 \times 5 \times 5 \times 5} = \frac{75}{1000} = 0.075.
$$

If the denominator has another prime factor, such as the 3 in 12, no power of 10 is a multiple of it, since the only prime factors of a power of 10 are 2 and 5. So the fraction can't be written over a power of 10, and the decimal never stops.

## Worked examples

<div class="example" markdown>

### Example 1: multiplying two decimals

Work out $4.36 \times 2.7$.

Step 1: round to $4 \times 3 = 12$, so the answer should be near 12.

Step 2: multiply 436 by 27 as whole numbers. The factors are lined up on the right, not by their points, since nothing needs to line up by place yet:

$$
\begin{array}{rl}
4.36 & \leftarrow 2 \text{ decimal places} \\
\underline{\times\;\;2.7} & \leftarrow 1 \text{ decimal place} \\
3052 & \leftarrow 436 \times 7 \\
\underline{+\;8720} & \leftarrow 436 \times 20 \\
11772 & \leftarrow \text{the digits of the product}
\end{array}
$$

Step 3: the factors have $2 + 1 = 3$ decimal places together. Count three digits from the right of 11772 and put the point there: 11.772.

Step 4: 11.772 is close to the estimate of 12. As fractions, $\frac{436}{100} \times \frac{27}{10} = \frac{11772}{1000} = 11.772$, which agrees.

</div>

<div class="example" markdown>

### Example 2: zeros in front and zeros at the end

Work out $0.04 \times 0.3$. Step 2 gives $4 \times 3 = 12$, and step 3 needs $2 + 1 = 3$ decimal places, but 12 has only two digits. Write a zero in front, 012, and place the point: 0.012. As fractions, $\frac{4}{100} \times \frac{3}{10} = \frac{12}{1000}$, which is 12 thousandths. The answer is smaller than both factors, as a product of two numbers less than 1 should be.

<div class="warning" markdown>

Watch out: drop zeros at the end only after the point is placed. In $2.5 \times 0.4$, step 2 gives $25 \times 4 = 100$, and two decimal places make 1.00, which is 1. Dropping the zeros of 100 first leaves 1, and two decimal places would then make it 0.01, a hundred times too small. The estimate catches it: 0.4 is a bit less than a half, and half of 2.5 is 1.25, so the answer should be near 1.

</div>

</div>

<div class="example" markdown>

### Example 3: dividing a decimal by a whole number

Eight friends split a \$47.60 bill equally. Each share is $47.60 \div 8$.

Step 1: the divisor is already a whole number. Step 2: $48 \div 8 = 6$, so expect a bit under \$6.

Step 3: eight goes into 47 five times, with $47 - 40 = 7$ left. Put the point in the quotient above the point in the dividend, then bring down the 6 to make 76. Eight goes into 76 nine times, with $76 - 72 = 4$ left. Then bring down the 0 to make 40, which gives 5 with nothing left. (Had the bill been written as 47.6, step 4 would supply that 0.)

$$
\begin{array}{rl}
5.95 & \\
8\,\overline{\smash{\big)}\,47.60} & \\
\underline{-\,40}\phantom{.00} & \leftarrow 5 \times 8 \\
7\phantom{.}6\phantom{0} & \leftarrow 47 - 40 = 7 \text{, bring down } 6 \\
\underline{-\,7\phantom{.}2}\phantom{0} & \leftarrow 9 \times 8 \\
40 & \leftarrow 76 - 72 = 4 \text{, bring down } 0 \\
\underline{-\,40} & \leftarrow 5 \times 8 \\
0 & \leftarrow \text{remainder } 0 \text{, so stop}
\end{array}
$$

Each friend pays \$5.95. Step 5: $5.95 \times 8 = 47.60$, and \$5.95 is a bit under the estimate of \$6.

</div>

<div class="example" markdown>

### Example 4: dividing by a decimal

At \$1.65 a litre, how many litres of gas does \$52.80 buy? The answer is $52.80 \div 1.65$.

Step 1: the divisor has two decimal places, so move both points two places to the right. The division becomes $5280 \div 165$. Step 2: $30 \times 1.65 = 49.50$, a bit less than 52.80, so expect a bit more than 30.

Step 3: 165 doesn't go into 5 or 52, so start with 528. Since $3 \times 165 = 495$, write 3 and subtract: $528 - 495 = 33$. Bring down the 0 to make 330, and $2 \times 165 = 330$ exactly. The quotient is 32, so \$52.80 buys 32 L.

Step 5: $32 \times 1.65 = 52.80$.

<div class="warning" markdown>

Watch out: move both points, not just the divisor's. Turning 1.65 into 165 and leaving 52.80 alone works out $52.80 \div 165 = 0.32$, which is 100 times too small. The estimate of a bit more than 30 rules it out.

</div>

</div>

<div class="example" markdown>

### Example 5: a fraction that repeats

Write $\frac{2}{7}$ as a decimal. Seven doesn't go into 2, so write 0 and a point and bring down zeros. Each row of the table is one pass of long division:

| Working number | Digit | Remainder |
|---|---|---|
| 20 | 2 | 6 |
| 60 | 8 | 4 |
| 40 | 5 | 5 |
| 50 | 7 | 1 |
| 10 | 1 | 3 |
| 30 | 4 | 2 |

The last remainder is 2, the number the division started with, so the next six passes repeat these six exactly, and so on forever:

$$
\frac{2}{7} = 0.285714\,285714\ldots = 0.\overline{285714}.
$$

The remainders 1 to 6 all appeared, so this block is as long as a block for denominator 7 can be. Check: $0.285714 \times 7 = 1.999998$, just short of 2. The digits cut off after the sixth place make up the difference.

</div>

## Edge cases and common mistakes

Two mistakes are flagged above where they happen: dropping zeros before placing the point (Example 2) and moving only the divisor's point (Example 4). Here are the others.

<div class="warning" markdown>

Watch out: the product doesn't keep the factors' number of decimal places. A common slip is $0.4 \times 0.2 = 0.8$, keeping one decimal place as addition would. The right answer is 0.08, because $\frac{4}{10} \times \frac{2}{10} = \frac{8}{100}$: tenths times tenths are hundredths.

</div>

A quotient bigger than the dividend is not a mistake. Dividing by a number less than 1 gives a bigger answer, as in $5 \div 0.2 = 25$, because 0.2 fits into 5 twenty-five times. Multiplying by a number less than 1 gives a smaller answer, as in [multiplying and dividing fractions](11-multiplying-and-dividing-fractions.md).

Dividing by zero is undefined, however it is written. Moving the point in 0.00 still leaves 0, so step 1 can't rescue $3.2 \div 0.00$.

Money splits are often untidy. Three people sharing \$10 each owe $10 \div 3 = 3.333\ldots$, which is \$3.33 to the nearest cent, but $3 \times 3.33 = 9.99$, one cent short. Someone pays \$3.34, and that is fine.

## Tricks and shortcuts

Some decimals are easier as fractions. Multiplying by 0.5 halves a number, by 0.25 takes a quarter of it, and by 0.1 moves the point one place left. Dividing does the opposite: dividing by 0.5 doubles, dividing by 0.25 multiplies by 4, and dividing by 0.1 moves the point one place right. So $36 \times 0.25 = 9$ and $36 \div 0.25 = 144$.

You can place the point by estimating alone, without counting. The digits of $0.0487 \times 612$ are 298044, from $487 \times 612$. Since $0.05 \times 600 = 30$, the answer must be 29.8044, and counting $4 + 0 = 4$ decimal places agrees.

## In code

Computers usually store decimals as binary floating-point numbers, and some simple decimals can't be stored exactly.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
from decimal import Decimal

print(0.1 + 0.2)                      # 0.30000000000000004
print(0.1 + 0.2 == 0.3)               # False
print(Decimal(0.1))                   # the float 0.1, written out exactly
print(math.isclose(0.1 + 0.2, 0.3))   # True
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True
```

The third line prints `0.1000000000000000055511151231257827021181583404541015625`. The rule for terminating decimals explains it, with 2 in place of 10. A float is a fraction whose denominator is a power of 2, and $\frac{1}{10}$ has a factor 5 in its denominator, so in binary it repeats forever, $0.000110011001100\ldots_2$, the way $\frac{1}{3}$ repeats in decimal. The computer keeps about 53 binary digits and rounds, so the stored 0.1, 0.2 and 0.3 are all slightly off, and the errors don't cancel. Compare floats with `math.isclose`, and use `Decimal` for money. [Floating point basics](../06-cs-math/01-number-representation/04-floating-point-basics.md) explains the format.

</details>

## Practice

### Warm-up

1\. Work out (a) $0.7 \times 0.6$, (b) $1.25 \times 0.08$ and (c) $3.6 \times 1.5$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Multiply $7 \times 6 = 42$ and place $1 + 1 = 2$ decimal places: 0.42.
- (b) Multiply $125 \times 8 = 1000$ and place $2 + 2 = 4$ decimal places: 0.1000, which is 0.1.
- (c) Multiply $36 \times 15 = 540$ and place $1 + 1 = 2$ decimal places: 5.40, which is 5.4.

Check by estimating: $0.7 \times 0.6$ is a bit less than $0.7 \times 0.7 = 0.49$; $1.25 \times 0.08$ is about $1 \times 0.1 = 0.1$; and $3.6 \times 1.5$ is about $4 \times 1.5 = 6$.

</details>

2\. Work out (a) $9.36 \div 4$, (b) $0.42 \div 0.06$ and (c) $5 \div 0.2$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The divisor is whole. Four goes into 9 twice with 1 left; put the point above the point; bring down 3 to make 13, which gives 3 with 1 left; bring down 6 to make 16, which gives 4. The answer is 2.34.
- (b) Move both points two places: $42 \div 6 = 7$.
- (c) Move both points one place, writing a zero on the 5: $50 \div 2 = 25$.

Check: $2.34 \times 4 = 9.36$, $7 \times 0.06 = 0.42$ and $25 \times 0.2 = 5$.

</details>

### Standard

3\. A 2.5 kg bag of rice costs \$6.85, and a 4 kg bag costs \$10.36. Which is cheaper per kilogram, and by how much?

<details class="solution" markdown>
<summary>Solution</summary>

Divide each price by its mass. For the small bag, move both points one place: $6.85 \div 2.5 = 68.5 \div 25$. Twenty-five goes into 68 twice with 18 left; put the point in the quotient and bring down the 5 to make 185, which gives 7 with 10 left; bring down a 0 to make 100, which gives 4. So the small bag is \$2.74 per kilogram.

For the big bag, $10.36 \div 4 = 2.59$, so \$2.59 per kilogram. The 4 kg bag is cheaper by $2.74 - 2.59 = 0.15$, that is, 15 cents per kilogram.

Check: $2.74 \times 2.5 = 6.85$ and $2.59 \times 4 = 10.36$.

</details>

4\. Without dividing, decide which of $\frac{7}{40}$, $\frac{5}{12}$ and $\frac{9}{75}$ are terminating decimals. Then write each one as a decimal.

<details class="solution" markdown>
<summary>Solution</summary>

- The fraction $\frac{7}{40}$ is in simplest form, and $40 = 2 \times 2 \times 2 \times 5$, so it terminates. Multiplying by 25 gives $\frac{175}{1000} = 0.175$.
- The fraction $\frac{5}{12}$ is in simplest form, and $12 = 2 \times 2 \times 3$ has a factor 3, so it repeats. Dividing, $50 \div 12 = 4$ remainder 2, $20 \div 12 = 1$ remainder 8, and $80 \div 12 = 6$ remainder 8, the same remainder again, so $\frac{5}{12} = 0.41\overline{6}$.
- The fraction $\frac{9}{75}$ is not in simplest form. Cancelling 3 gives $\frac{3}{25}$, and $25 = 5 \times 5$, so it terminates: $\frac{3}{25} = \frac{12}{100} = 0.12$. The 3 in $75 = 3 \times 5 \times 5$ didn't count, because it cancelled.

Check: $0.175 \times 40 = 7$ and $0.12 \times 75 = 9$, and $0.41666\ldots \times 12$ comes out just under 5 when you stop after a few 6s.

</details>

### Challenge

5\. Place the decimal point by estimating, then confirm by counting decimal places. (a) The digits of $0.0391 \times 52.7$ are 206057. (b) Work out $3.2 \div 0.0016$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Estimate: $0.04 \times 50 = 2$, so the product is about 2, and the point goes after the first digit: 2.06057. Counting gives $4 + 1 = 5$ decimal places, which agrees.

(b) Estimate: $1000 \times 0.0016 = 1.6$, and 3.2 is twice 1.6, so expect about 2000. To divide exactly, move both points four places: $32000 \div 16 = 2000$.

Check: $2000 \times 0.0016 = 3.2$.

</details>

6\. This one reviews [multiplying and dividing fractions](11-multiplying-and-dividing-fractions.md). Work out $0.6 \div 0.125$ two ways: by moving the decimal points, and by writing both numbers as fractions and multiplying by the reciprocal.

<details class="solution" markdown>
<summary>Solution</summary>

With decimals, move both points three places: $600 \div 125$. Since $4 \times 125 = 500$, write 4 with 100 left; put the point and bring down a 0 to make 1000, and $8 \times 125 = 1000$. The answer is 4.8.

With fractions, $0.6 = \frac{3}{5}$ and $0.125 = \frac{1}{8}$, so the division is $\frac{3}{5} \div \frac{1}{8} = \frac{3}{5} \times 8 = \frac{24}{5} = 4\frac{4}{5}$.

Check: $\frac{4}{5} = 0.8$, so the two answers agree, and $4.8 \times 0.125 = 0.6$.

</details>

## Where this shows up

- The [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md) lesson multiplies by 1.13 to add HST and divides by 1.13 to take it off. Unit prices<!-- link: ../08-financial-math/01-everyday-money/02-unit-price-and-comparison-shopping.md --> are the division from Practice 3.
- In [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md), counting decimal places becomes adding exponents, the $10^{m+n}$ from step 3.
- Every fraction gives a terminating or repeating decimal. Decimals that do neither, such as the digits of $\sqrt{2}$, are the irrational numbers in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).
