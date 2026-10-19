# Scientific notation

After this lesson you can write very large and very small numbers in scientific notation, multiply, divide, add and subtract them, read E notation on a calculator or in Python, and convert between storage units such as GB and GiB.

Before this: [powers of ten](../../01-elementary/14-powers-of-ten.md) and [exponent rules](01-exponent-rules.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write 3,080,000 and 0.000042 in scientific notation.
2. Work out $(6 \times 10^4) \times (5 \times 10^{-7})$, and give the answer in scientific notation.
3. A drive is sold as 2 TB, where 1 TB is $10^{12}$ bytes. How many GiB is that, where 1 GiB is $2^{30}$ bytes? Round to the nearest GiB.

<details class="solution" markdown>
<summary>Answers</summary>

1. $3.08 \times 10^6$ and $4.2 \times 10^{-5}$. The point moves 6 places left in the first and 5 places right in the second.
2. $3 \times 10^{-2}$. The coefficients give $6 \times 5 = 30$ and the exponents give $10^{4 + (-7)} = 10^{-3}$, so the product is $30 \times 10^{-3} = 3.0 \times 10^{-2}$.
3. About 1,863 GiB: $2 \times 10^{12} \div 2^{30} = 2 \times 10^{12} \div 1{,}073{,}741{,}824 \approx 1862.6$.

</details>

## The idea

Light travels 299,792,458 metres per second, and the Earth is about 149,600,000,000 metres from the Sun. To find how long sunlight takes to reach us, you divide the second number by the first. Written out like this, the numbers are hard to read and easy to miscopy: one missing zero makes the answer ten times too small.

Scientific notation writes each number as a short decimal times a power of ten. The distance is $1.496 \times 10^{11}$ m, which says "about 1.5, shifted 11 places". The speed is $2.998 \times 10^8$ m/s. Now the division splits into two easy parts, $1.496 \div 2.998 \approx 0.5$ and $10^{11} \div 10^8 = 10^3$, so the time is about $0.5 \times 10^3 = 500$ seconds, a little over 8 minutes.

The same notation handles tiny numbers. A processor running at 3 GHz does $3 \times 10^9$ cycles a second, so one cycle lasts $\frac{1}{3} \times 10^{-9}$ s, about $3.3 \times 10^{-10}$ seconds. The power of ten tells you the size at a glance, and the decimal in front gives the digits that matter.

## Definitions

A number is in **scientific notation** when it is written as

$$
a \times 10^n,
$$

where $1 \le \lvert a \rvert < 10$ and $n$ is an integer. The number $a$ is called the coefficient (computing books call it the significand), and $n$ is the exponent.

In plain words, the coefficient has exactly one nonzero digit before the decimal point, and the power of ten records how far the point was moved. For example, $45{,}000 = 4.5 \times 10^4$ and $-0.0072 = -7.2 \times 10^{-3}$. The forms $45 \times 10^3$ and $0.45 \times 10^5$ have the same value, but they are not in scientific notation, because 45 is too big and 0.45 too small. A number between 1 and 10 has exponent 0: $5.2 = 5.2 \times 10^0$. Zero has no scientific notation, since no power of ten turns a coefficient of at least 1 into 0; it is written 0.

The **order of magnitude** of a number is the power of ten in its scientific notation. So $4.5 \times 10^4$ and $9.1 \times 10^4$ have the same order of magnitude, 4, and a number of order 4 is roughly 10 times a number of order 3. Some books round first, so that $9.1 \times 10^4$ counts as order 5 because it is closer to $10^5$; when it matters, say which you mean. Two quantities "differ by three orders of magnitude" when one is about $10^3 = 1000$ times the other.

The **significant figures** of a number in scientific notation are the digits of its coefficient. The number $3.08 \times 10^6$ has three of them, and writing $3.080 \times 10^6$ claims a fourth: that the next digit is known to be 0. This lesson uses significant figures only to say how many digits to keep, which is usually three.

**E notation** is the form calculators and programming languages use for scientific notation: the letter E or e stands for "times ten to the". So `1.5e-3` means $1.5 \times 10^{-3} = 0.0015$, and `6.02E23` means $6.02 \times 10^{23}$.

## How to do it

### Converting to and from scientific notation

1. Put the decimal point just after the first nonzero digit. The digits from there on, without zeros at the start, form the coefficient. For 0.000042 the coefficient is 4.2.
2. Count how many places the point moved to get there. For 0.000042, it moved 5 places, past 0, 0, 0, 0 and 4.
3. Choose the sign of the exponent. A number of 10 or more gets a positive exponent (the point moved left), a number between 0 and 1 gets a negative one (the point moved right), and a number from 1 to 10 gets 0.
4. Drop zeros at the end of the coefficient unless they are significant, and write $a \times 10^n$.
5. Check by moving the point back: $4.2 \times 10^{-5}$ means 5 places left, which gives 0.000042.

To go back to an ordinary number, move the point $n$ places right for a positive exponent and $\lvert n \rvert$ places left for a negative one, filling empty places with zeros, as in [powers of ten](../../01-elementary/14-powers-of-ten.md#how-to-do-it).

### Multiplying and dividing

1. Multiply (or divide) the coefficients.
2. Add the exponents to multiply, or subtract them to divide. These are the product and quotient rules for base 10.
3. Normalize: if the new coefficient is 10 or more, or less than 1, move its point and change the exponent to make up for it. Moving the point one place left multiplies the power by 10: $30 \times 10^{-3} = 3.0 \times 10^{-2}$.
4. Round the coefficient to the number of significant figures you need.
5. Check with a rough estimate of the order of magnitude.

### Adding and subtracting

The exponents must match before you add, because $2 \times 10^5$ and $3 \times 10^3$ count different things (hundred-thousands and thousands), the way you can only add tenths to tenths.

1. Rewrite the number with the smaller exponent so that it has the larger exponent. Raising the exponent by $k$ moves the coefficient's point $k$ places left: $3 \times 10^3 = 0.03 \times 10^5$.
2. Add or subtract the coefficients, and keep the common power of ten.
3. Normalize and round, as for multiplication.
4. Check: the sum should be close to the larger number when the exponents are far apart.

### SI prefixes

Each metric prefix is a power of ten, so a measurement with a prefix is already halfway to scientific notation. These are the prefixes from nano to tera; [powers of ten](../../01-elementary/14-powers-of-ten.md#metric-prefixes) introduced the middle of the table.

| Prefix | Symbol | Power | Example |
|---|---|---|---|
| tera | T | $10^{12}$ | a 1 TB drive holds $10^{12}$ bytes |
| giga | G | $10^{9}$ | a 3 GHz processor does $3 \times 10^9$ cycles a second |
| mega | M | $10^{6}$ | a 100 Mbit/s connection carries $10^8$ bits a second |
| kilo | k | $10^{3}$ | 5 km is $5 \times 10^3$ m |
| milli | m | $10^{-3}$ | 250 mL is $2.5 \times 10^{-1}$ L |
| micro | $\mu$ | $10^{-6}$ | a hair about 70 $\mu\text{m}$ thick is $7 \times 10^{-5}$ m |
| nano | n | $10^{-9}$ | one cycle at 1 GHz lasts 1 ns, $10^{-9}$ s |

Each step in the table is a factor of $10^3$. To convert, replace the prefix with its power and use the exponent rules: $350 \text{ ns} = 350 \times 10^{-9} \text{ s} = 3.5 \times 10^{-7} \text{ s}$. In plain text, a microsecond is often typed "us" because $\mu$ is hard to type.

### KB or KiB

Memory comes in powers of 2, and $2^{10} = 1024$ is close to 1000, so computing has long used "kilobyte" for both 1000 and 1024 bytes. The International Electrotechnical Commission (IEC) gave the binary sizes their own names, with an "i" in the symbol:

| Decimal (SI) | Bytes | Binary (IEC) | Bytes | Binary is bigger by |
|---|---|---|---|---|
| kB, kilobyte | $10^3$ | KiB, kibibyte | $2^{10} = 1{,}024$ | 2.4% |
| MB, megabyte | $10^6$ | MiB, mebibyte | $2^{20} = 1{,}048{,}576$ | 4.9% |
| GB, gigabyte | $10^9$ | GiB, gibibyte | $2^{30} = 1{,}073{,}741{,}824$ | 7.4% |
| TB, terabyte | $10^{12}$ | TiB, tebibyte | $2^{40} \approx 1.0995 \times 10^{12}$ | 10.0% |

Drive makers and network speeds use the decimal units. Memory chips, and many operating systems, use the binary ones, but often still print "GB". Windows File Explorer, for example, divides by $2^{30}$ and labels the result GB. That is why a drive sold as 1 TB shows up as about 931 "GB": nothing is missing, the two numbers measure the same bytes in different units. Example 4 does the conversion.

## Worked examples

<div class="example" markdown>

### Example 1: converting both ways

Write (a) 93,000,000 and (b) 0.00052 in scientific notation, and (c) write $7.05 \times 10^{-4}$ as an ordinary number.

(a) Step 1: the first nonzero digit is the 9, so the point goes after it, and the coefficient is 9.3 (the zeros after the 3 are dropped in Step 4). Step 2: the point started at the right end, after the last 0, and moved to just after the 9, which is 7 places. Step 3: the number is bigger than 10, so the exponent is positive. Step 4: $93{,}000{,}000 = 9.3 \times 10^7$.

<div class="warning" markdown>

Watch out at Step 2: count the places the point moves, not the zeros you see. The number 93,000,000 has six zeros, but the point also moves past the 3, so the exponent is 7. Writing $9.3 \times 10^6$ is the usual slip, and it gives 9,300,000, ten times too small.

</div>

Step 5: check by moving the point 7 places right from 9.3: 93, 930, and so on up to 93,000,000. Counting digits also works: 93,000,000 has 8 digits, and a number with $d$ digits before the point has exponent $d - 1$.

(b) Step 1: the first nonzero digit is the 5, so the coefficient is 5.2. Step 2: the point moves from just after the first 0 to just after the 5, past 0, 0, 0 and 5, which is 4 places. Step 3: the number is less than 1, so the exponent is negative. The answer is $5.2 \times 10^{-4}$.

Step 5: $5.2 \times 10^{-4}$ means moving 4 places left from 5.2: 0.52, 0.052, 0.0052, 0.00052.

(c) The exponent is $-4$, so move the point 4 places left, filling with zeros: 0.705, 0.0705, 0.00705, 0.000705. So $7.05 \times 10^{-4} = 0.000705$. Check: the 0 inside 7.05 is a real digit and stays between the 7 and the 5.

</div>

<div class="example" markdown>

### Example 2: how long sunlight takes to reach Earth

The mean distance from the Earth to the Sun is $1.496 \times 10^{11}$ m, and light travels $2.998 \times 10^8$ m/s. How long does sunlight take to reach Earth?

Time is distance divided by speed. Divide the coefficients and subtract the exponents:

$$
\frac{1.496 \times 10^{11}}{2.998 \times 10^8} = \frac{1.496}{2.998} \times 10^{11 - 8} \approx 0.4990 \times 10^3 \text{ s}.
$$

The coefficient 0.4990 is less than 1, so normalize: move its point one place right and lower the exponent by 1. The time is $4.990 \times 10^2$ s, about 499 seconds, or 8.3 minutes.

Check the units: $\frac{\text{m}}{\text{m/s}} = \text{s}$. Check the size: $1.5 \div 3 = 0.5$ and $10^{11} \div 10^8 = 10^3$ give 500 s.

</div>

<div class="example" markdown>

### Example 3: adding and subtracting

Work out (a) $4.5 \times 10^6 + 3.2 \times 10^4$ and (b) $1.2 \times 10^{-3} - 9.5 \times 10^{-4}$.

(a) Step 1: rewrite the smaller one with exponent 6. Raising the exponent by 2 moves the point 2 places left: $3.2 \times 10^4 = 0.032 \times 10^6$. Step 2: $4.5 + 0.032 = 4.532$, so the sum is $4.532 \times 10^6$, already normalized. Check: the second number is 100 times smaller, so the sum is only a little bigger than 4.5 million.

(b) The larger exponent is $-3$, since $-3 > -4$. Rewrite the second number: $9.5 \times 10^{-4} = 0.95 \times 10^{-3}$. Subtracting, $1.2 - 0.95 = 0.25$, so the difference is $0.25 \times 10^{-3}$. Normalize by moving the point one place right and lowering the exponent: $2.5 \times 10^{-4}$.

Check (b) with ordinary decimals: $0.0012 - 0.00095 = 0.00025$.

<div class="warning" markdown>

Watch out: don't add the exponents when you add the numbers. $2 \times 10^3 + 3 \times 10^3$ is $5 \times 10^3$, not $5 \times 10^6$. Adding exponents is for multiplying. In ordinary numbers, 2,000 plus 3,000 is 5,000.

</div>

</div>

<div class="example" markdown>

### Example 4: the "missing" space on a 1 TB drive (finish it yourself)

A drive is sold as 1 TB, which is $10^{12}$ bytes. How many GiB is that, and how many TiB?

A GiB is $2^{30} = 1{,}073{,}741{,}824$ bytes, which is about $1.0737 \times 10^9$. Dividing,

$$
\frac{10^{12}}{1.0737 \times 10^9} = \frac{1}{1.0737} \times 10^{12 - 9}.
$$

Finish the division, normalize, and then find the size in TiB, where 1 TiB is $2^{40} = 1024$ GiB.

<details class="solution" markdown>
<summary>Finish</summary>

$\frac{1}{1.0737} \approx 0.9313$, so the size is $0.9313 \times 10^3 = 9.313 \times 10^2$, about 931 GiB. This is the 931 "GB" an operating system shows. In TiB it is $931.3 \div 1024 \approx 0.909$ TiB.

Check: $931.3 \times 1{,}073{,}741{,}824 \approx 1.0000 \times 10^{12}$ bytes. The size also makes sense: a GiB is bigger than a GB, so the same bytes make fewer of them.

</details>

</div>

## Edge cases and common mistakes

Counting zeros instead of places, and adding exponents during a sum, are flagged in the examples. Here are the others.

<div class="warning" markdown>

Watch out: a negative exponent makes a small number, not a negative one. $3 \times 10^{-4} = 0.0003$, which is positive. A negative number has the minus sign in front of the coefficient: $-3 \times 10^4 = -30{,}000$. So $-3 \times 10^{-4}$ is $-0.0003$, a negative number close to 0.

</div>

<div class="warning" markdown>

Watch out: an answer such as $45 \times 10^3$ or $0.8 \times 10^{-2}$ is equal to the right number but not in scientific notation. Normalize it: $4.5 \times 10^4$ and $8 \times 10^{-3}$. When the coefficient gets smaller, the exponent goes up, and the other way round, so the value stays the same.

</div>

<div class="warning" markdown>

Watch out when typing powers of ten into code. In Python, `^` is not a power: it is bitwise XOR, so `2 * 10^3` is `20 ^ 3`, which is 23. Write `2e3` or `2 * 10**3`. On a calculator with an EE or EXP key, that key already means "times ten to the", so typing `5 × 10 EE 3` gives $5 \times 10 \times 10^3 = 5 \times 10^4$. Type `5 EE 3` for $5 \times 10^3$.

</div>

<div class="warning" markdown>

Watch out for bits and bytes. Network speeds are in bits per second (Mbit/s or Mbps), while file sizes are in bytes (MB), and a byte is 8 bits. A 100 Mbit/s connection moves at most $12.5$ MB per second ([problem-solving playbook](../../00-start-here/problem-solving-playbook.md#check-units-and-size)).

</div>

Comparing two numbers in scientific notation is quick when both are positive: the larger exponent wins, and only when the exponents match do you compare coefficients. So $9.8 \times 10^{-5} < 3.1 \times 10^{-4}$, because $-5 < -4$, even though 9.8 is bigger than 3.1. For negative numbers the order reverses, as on the number line.

## Tricks and shortcuts

Count digits to find the exponent. A whole number with $d$ digits has exponent $d - 1$: 93,000,000 has 8 digits, so it is $9.3 \times 10^7$. A decimal less than 1 whose first nonzero digit is in the $k$-th place after the point has exponent $-k$: in 0.00052 the 5 is in the 4th place, so the exponent is $-4$.

Exponents that are multiples of 3 match the prefixes. **Engineering notation** allows a coefficient from 1 up to 1000 so that the exponent is always a multiple of 3: $4.7 \times 10^{-8}$ s becomes $47 \times 10^{-9}$ s, which reads straight off as 47 ns.

For a square root, make the exponent even first. $\sqrt{4 \times 10^6} = 2 \times 10^3$, since $(10^3)^2 = 10^6$. With an odd exponent, move one power into the coefficient: $9 \times 10^5 = 90 \times 10^4$, so its square root is $\sqrt{90} \times 10^2 \approx 9.5 \times 10^2$.

The binary and decimal prefixes stay close because $2^{10} \approx 10^3$, and the gap grows by about 2.4% per step. That is why the difference is easy to ignore for a KiB and hard to ignore for a TiB.

## In code

Python reads and writes E notation, and its format codes put any number in scientific notation.

<details class="code" markdown>
<summary>In code</summary>

```python
print(1.5e-3, 6.02e23)              # 0.0015 6.02e+23
print(0.00001, 1e16, 12345.0)       # 1e-05 1e+16 12345.0
print(f"{93_000_000:.2e}")          # 9.30e+07
print(f"{1.496e11 / 2.998e8:.4g}")  # 499
print(1e3, type(1e3).__name__)      # 1000.0 float
print(2 * 10^3, 2 * 10**3)          # 23 2000
print(10**12 / 2**30)               # 931.3225746154785
```

Python switches to E notation by itself for very small or very large floats, as the second line shows. The format code `.2e` gives scientific notation with 2 digits after the point, and `.4g` keeps 4 significant figures. A number written with `e` is always a float, even `1e3`. The sixth line is the XOR trap from the warning above.

</details>

## FAQ

### Why must the coefficient be at least 1 and less than 10?

So that each number has exactly one form. Without the rule, 45,000 could be $45 \times 10^3$ or $0.45 \times 10^5$ or many others, and comparing two numbers would take work. With it, the exponent alone tells you the size, and two numbers with the same exponent can be compared digit by digit.

### Does scientific notation change the value of a number?

No. $4.5 \times 10^4$ and 45,000 are the same number. What can change is the precision you claim: $4.5 \times 10^4$ suggests that the number is known to two significant figures, while 45,000 doesn't say whether the zeros were measured or are only placeholders.

### Why does my 16 GB of memory show as 16 GB, but my 1 TB drive shows less?

Memory is made in powers of 2, so a "16 GB" module really holds 16 GiB, $16 \times 2^{30}$ bytes, and the operating system's binary count shows 16. A drive maker counts in powers of 10, so the same operating system shows $10^{12} \div 2^{30} \approx 931$. The units are the cause in both cases; no space is lost.

## Practice

### Warm-up

1\. Write in scientific notation: (a) 7,200,000, (b) 0.00309, (c) 51, (d) $-0.8$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The point moves 6 places left: $7.2 \times 10^6$.
- (b) The point moves 3 places right, past 0, 0 and 3: $3.09 \times 10^{-3}$.
- (c) One place left: $5.1 \times 10^1$.
- (d) One place right, and the sign stays in front: $-8 \times 10^{-1}$.

Check by moving the point back: 7,200,000, 0.00309, 51 and $-0.8$.

</details>

2\. Write as ordinary numbers: (a) $4.06 \times 10^5$, (b) $9 \times 10^{-4}$, (c) $1.0 \times 10^0$, (d) `2.5e-2`.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) 5 places right: 406,000.
- (b) 4 places left: 0.0009.
- (c) $10^0 = 1$, so the number is 1.0, which is 1.
- (d) E notation for $2.5 \times 10^{-2}$: 2 places left gives 0.025.

Check (a): 406,000 has 6 digits, and $6 - 1 = 5$.

</details>

3\. Which is larger in each pair? (a) $3.1 \times 10^{-4}$ or $9.8 \times 10^{-5}$, (b) $7 \times 10^8$ or $6.9 \times 10^9$, (c) $-2 \times 10^3$ or $-5 \times 10^2$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $3.1 \times 10^{-4}$, because $-4 > -5$. As decimals: 0.00031 against 0.000098.
- (b) $6.9 \times 10^9$, because its exponent is larger. It is about 10 times the other.
- (c) Both are negative, so the one closer to 0 is larger: $-5 \times 10^2 = -500$ is larger than $-2 \times 10^3 = -2000$.

Check (b): 6,900,000,000 against 700,000,000.

</details>

### Standard

4\. Work out, in scientific notation: (a) $(3 \times 10^5)(4 \times 10^6)$, (b) $\dfrac{8.4 \times 10^{-3}}{2.1 \times 10^4}$, (c) $6.1 \times 10^8 - 4 \times 10^7$, (d) $(5 \times 10^{-3})^2$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $3 \times 4 = 12$ and $10^{5+6} = 10^{11}$, so $12 \times 10^{11} = 1.2 \times 10^{12}$ after normalizing.

(b) $8.4 \div 2.1 = 4$ and $10^{-3-4} = 10^{-7}$, so $4 \times 10^{-7}$.

(c) Match exponents: $4 \times 10^7 = 0.4 \times 10^8$. Then $6.1 - 0.4 = 5.7$, so $5.7 \times 10^8$.

(d) Power of a product: $5^2 \times (10^{-3})^2 = 25 \times 10^{-6} = 2.5 \times 10^{-5}$.

Check (d) with decimals: $0.005^2 = 0.000025$.

</details>

5\. A processor runs at 3.2 GHz, that is, $3.2 \times 10^9$ cycles per second. (a) How long is one cycle, in seconds (scientific notation) and in nanoseconds? (b) How many cycles does it run in one minute?

<details class="solution" markdown>
<summary>Solution</summary>

(a) One cycle lasts $\frac{1}{3.2 \times 10^9}$ s. Since $1 \div 3.2 = 0.3125$, that is $0.3125 \times 10^{-9} = 3.125 \times 10^{-10}$ s. A nanosecond is $10^{-9}$ s, so this is 0.3125 ns.

(b) A minute is 60 s: $3.2 \times 10^9 \times 60 = 192 \times 10^9 = 1.92 \times 10^{11}$ cycles.

Check (a): the length of one cycle times the number of cycles per second should be 1 second, and $3.125 \times 10^{-10} \times 3.2 \times 10^9 = 10 \times 10^{-1} = 1$.

</details>

6\. A phone has 128 GB of storage, where GB means $10^9$ bytes. (a) How many 3.5 MB photos fit, where MB means $10^6$ bytes? (b) How many GiB does the phone report?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Divide: $\frac{1.28 \times 10^{11}}{3.5 \times 10^6} = \frac{1.28}{3.5} \times 10^5 \approx 0.3657 \times 10^5 = 3.657 \times 10^4$. That is 36,571.4, so 36,571 whole photos, about $3.7 \times 10^4$.

(b) $\frac{1.28 \times 10^{11}}{2^{30}} = \frac{1.28 \times 10^{11}}{1.0737 \times 10^9} \approx 1.192 \times 10^2$, about 119 GiB.

Check (a) by size: 128 GB is 128,000 MB, and $128{,}000 \div 3.5$ is a bit less than $128{,}000 \div 3 \approx 43{,}000$.

</details>

### Challenge

7\. Light travels $2.998 \times 10^8$ m/s. (a) How far does it go in one nanosecond? (b) A light-year is the distance light travels in a year of 365.25 days. Find it in kilometres, in scientific notation with four significant figures.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $2.998 \times 10^8 \times 10^{-9} = 2.998 \times 10^{-1}$ m, about 30 cm. So a signal can't cross a 30 cm circuit board in less than about a nanosecond, which is one reason chips are small.

(b) Seconds in a year: $365.25 \times 24 \times 3600 = 31{,}557{,}600 \approx 3.15576 \times 10^7$. In km/s the speed is $2.998 \times 10^5$, since 1 km is $10^3$ m. Then

$$
2.998 \times 10^5 \times 3.15576 \times 10^7 = 9.461 \times 10^{12} \text{ km},
$$

because $2.998 \times 3.15576 \approx 9.461$ and $10^{5+7} = 10^{12}$.

Check the size: $3 \times 10^5 \times 3 \times 10^7 = 9 \times 10^{12}$.

</details>

8\. This one reviews area and volume units from [measurement and unit conversion](../../01-elementary/15-measurement-and-unit-conversion.md#area-and-volume-units). (a) Write $1 \text{ km}^2$ in square metres and $1 \text{ m}^3$ in cubic millimetres, using powers of ten. (b) A storm drops 25 mm of rain on $1 \text{ km}^2$ of land. How many cubic metres of water is that, and how many litres? (A cubic metre is 1000 L.)

<details class="solution" markdown>
<summary>Solution</summary>

(a) A kilometre is $10^3$ m, so $1 \text{ km}^2 = (10^3 \text{ m})^2 = 10^6 \text{ m}^2$ by the power of a product. A metre is $10^3$ mm, so $1 \text{ m}^3 = (10^3)^3 \text{ mm}^3 = 10^9 \text{ mm}^3$.

(b) The water is a thin slab with area $10^6 \text{ m}^2$ and depth 25 mm, which is $2.5 \times 10^{-2}$ m. Its volume is $10^6 \times 2.5 \times 10^{-2} = 2.5 \times 10^4 \text{ m}^3$. In litres, $2.5 \times 10^4 \times 10^3 = 2.5 \times 10^7$ L, 25 million litres.

Check the units: $\text{m}^2 \times \text{m} = \text{m}^3$. Check one square metre: it gets $0.025 \text{ m}^3 = 25$ L, and $25 \times 10^6 = 2.5 \times 10^7$.

</details>

## Where this shows up

- The next two lessons use orders of magnitude: [roots, irrational numbers and types of numbers](03-roots-irrationals-and-types-of-numbers.md) estimates roots, and [estimation and sanity checks](04-estimation-and-sanity-checks.md) builds whole estimates from powers of ten.
- A float is scientific notation in base 2, with a significand and an exponent stored in fixed numbers of bits (floating point basics<!-- link: ../../06-cs-math/01-number-representation/04-floating-point-basics.md -->). Byte counts, bandwidths and running times in systems courses are all read this way.
- Economics and finance report in thousands, millions and billions of dollars. Comparing two such numbers, for example a debt and a national income in GDP and the circular flow<!-- link: ../../07-economics-math/01-measuring-the-economy/05-gdp-and-the-circular-flow.md -->, is a division in scientific notation.
