# Elementary

Whole numbers, the four operations, fractions, decimals, measurement and basic geometry. Grades 1 to 5, written compactly for an adult who knows most of it.

Before this folder: Nothing. This is the start.

## How to use this folder

Take the [diagnostic](diagnostic.md) first, without notes. It asks two questions on each lesson, and its answer table names the lesson to study for each one you miss, so you can do only those lessons and skip the rest. Come back to the cheat sheet below for fast lookup. The [Anki deck for this folder](../downloads/anki/01-elementary.apkg) holds the facts worth memorizing, such as the hard times-table facts, the divisibility rules and the metric prefixes; in Anki desktop choose File, then Import, and [Anki decks](../00-start-here/index.md#anki-decks) covers phones.

## Cheat sheet

### [Place value and rounding](01-place-value-and-rounding.md)

- Each place is worth 10 times the place to its right, so the 4 in 2,436 is worth 400, and the expanded form is $2{,}000 + 400 + 30 + 6$.
- Commas split the digits into periods of three: ones, thousands, millions. From words, every period after the first gets three digits, so "two million six thousand forty" is 2,006,040.
- To compare, count the digits first, then find the first place from the left where they differ.

To round to a place:

1. Look at the digit just right of the rounding place, and only that digit.
2. If it is 5 to 9, add 1 to the rounding digit. If it is 0 to 4, leave the rounding digit alone.
3. Replace every digit to its right with 0. A 9 that becomes 10 carries 1 to the left: 2,996 to the nearest ten is 3,000.

Truncating always rounds down (2,996 to 2,990). Python's `round` sends a half to the even neighbour, so `round(2450, -2)` is 2400.

Common mistakes:

- Rounding in a chain: 1,449 to the nearest hundred is 1,400, not 1,500.
- Dropping the zeros: to the nearest thousand, 4,072,519 is 4,073,000, not 4,073.

### [Addition and subtraction](02-addition-and-subtraction.md)

Check a subtraction by adding back: $52 - 18 = 34$ because $34 + 18 = 52$.

| Mental strategy | Example |
|---|---|
| Make 10 | $8 + 5 = 8 + 2 + 3 = 13$ |
| Compensation | $47 + 38 = 47 + 40 - 2 = 85$ and $92 - 57 = 92 - 60 + 3 = 35$ |
| Counting up | $403 - 288$: $288 + 12 = 300$ and $300 + 103 = 403$, so 115 |
| Subtract from 1,000 | each digit from 9, the last from 10: $1{,}000 - 637 = 363$ |

Borrowing in column subtraction:

1. Line the numbers up at the ones, larger on top, and work from the right.
2. If a top digit is smaller than the digit below it, take 1 from the next place to the left and add 10 to it.
3. If that place is 0, take 1 from the first nonzero digit to the left and turn each 0 you pass into 9: 5,003 becomes 4 thousands, 9 hundreds, 9 tens and 13 ones.

Common mistakes:

- Taking the smaller digit from the larger in every column: $5{,}003 - 1{,}768$ is 3,235, not 4,765.
- Fixing compensation the wrong way: $92 - 60 + 3$, not $92 - 60 - 3$.
- Dropping the last carry: $857 + 286 = 1{,}143$.

### [Multiplication and times tables](03-multiplication-and-times-tables.md)

The product $n \times a$ is $n$ copies of $a$ added together, or an array of $n$ rows of $a$.

| Family | Rule | Example |
|---|---|---|
| 2s, 4s, 8s | double, again, again | $2 \times 7 = 14$, $4 \times 7 = 28$, $8 \times 7 = 56$ |
| 5s | half of the 10s | $5 \times 7 = 35$ |
| 9s | the 10s minus one group | $9 \times 7 = 70 - 7 = 63$ |
| 11s | the digit twice, up to $11 \times 9$ | $11 \times 7 = 77$, $11 \times 12 = 132$ |
| 12s | the 10s plus the 2s | $12 \times 7 = 70 + 14 = 84$ |
| 3s and 6s | a double plus one group; the 5s plus one group | $3 \times 7 = 21$, $6 \times 7 = 35 + 7 = 42$ |

Memorize the squares $6 \times 6 = 36$, $7 \times 7 = 49$, $8 \times 8 = 64$ and $12 \times 12 = 144$, and the facts no rule reaches quickly: $6 \times 7 = 42$, $6 \times 8 = 48$ and $7 \times 8 = 56$ ("5, 6, 7, 8"). The digits of $9 \times n$ add to 9 for $n$ from 1 to 10. To multiply a whole number by 10, 100 or 1,000, write 1, 2 or 3 zeros on its right, so $40 \times 50$ is $4 \times 5 = 20$ with both zeros attached: 2,000.

Common mistakes:

- Zero times 7 is 0, not 7.
- Writing a 0 on a decimal: $4.6 \times 10 = 46$, not 4.60.
- Swapping look-alikes: $7 \times 8 = 56$ but $6 \times 9 = 54$; $6 \times 8 = 48$ but $7 \times 7 = 49$.

### [Properties of operations](04-properties-of-operations.md)

| Property | Addition | Multiplication |
|---|---|---|
| Commutative | $a + b = b + a$ | $a \times b = b \times a$ |
| Associative | $(a + b) + c = a + (b + c)$ | $(a \times b) \times c = a \times (b \times c)$ |
| Identity | $a + 0 = a$ | $a \times 1 = a$ |
| Zero | | $a \times 0 = 0$ |
| Distributive | | $a \times (b + c) = a \times b + a \times c$ |

The distributive property also works over subtraction and with the multiplier on the right. Subtraction and division are neither commutative nor associative: $(24 \div 4) \div 2 = 3$ but $24 \div (4 \div 2) = 12$. A sum being divided splits, $(12 + 18) \div 6 = 2 + 3$, but a sum you divide by doesn't: $12 \div (2 + 4)$ is 2, not 9. One counterexample disproves a statement about all numbers.

To rearrange a calculation:

1. Look for pairs that make round numbers: $2 \times 5 = 10$, $4 \times 25 = 100$, $8 \times 125 = 1{,}000$, $36 + 64 = 100$.
2. If there are only additions, or only multiplications, reorder and regroup to bring the pairs together.
3. Write a factor near a round number as a sum or difference and distribute: $7 \times 98 = 700 - 14 = 686$.
4. Never swap or regroup across a minus or division sign.

Common mistakes:

- Distributing to one term only: $3 \times (4 + 5) = 12 + 15 = 27$, not $12 + 5$.
- Regrouping a subtraction: $100 - 30 - 20 = 50$, but $100 - (30 - 20) = 90$.

### [Multi-digit multiplication](05-multi-digit-multiplication.md)

Split the factors by place value and add the partial products. The area model for $47 \times 36$:

| $\times$ | $40$ | $7$ |
|---|---|---|
| $30$ | $1{,}200$ | $210$ |
| $6$ | $240$ | $42$ |

The total is $1{,}200 + 210 + 240 + 42 = 1{,}692$. The column method:

1. Estimate with one nonzero digit per factor: $50 \times 40 = 2{,}000$.
2. Multiply the top number by the ones digit, right to left, adding each carry after the next multiplication: $47 \times 6 = 282$.
3. Start the second row with a 0, then multiply by the tens digit: $47 \times 30 = 1{,}410$.
4. Add the rows, $282 + 1{,}410 = 1{,}692$, and compare with the estimate.

Casting out nines, a check with repeated digit sums, catches many wrong digits but not every mistake.

Common mistakes:

- A missing shift: $56 \times 34$ is $224 + 1{,}680 = 1{,}904$, not $224 + 168 = 392$.
- Adding a carry before multiplying: in $47 \times 6$, the tens are $4 \times 6 + 4$, not $(4 + 4) \times 6$.
- Skipping a 0 in the top number: $308 \times 4$ is 1,232, not 152.

### [Division facts and remainders](06-division-facts-and-remainders.md)

In $n \div d$, the dividend $n$ is divided by the divisor $d$, and the quotient $q$ and remainder $r$ satisfy $n = qd + r$ with $0 \le r < d$. Zero divided by a nonzero number is 0, while $5 \div 0$ and $0 \div 0$ are undefined.

| For $75 \div 12 = 6$ remainder 3, the question asks | Answer |
|---|---|
| how many 12-seat vans 75 people need | 7, round up |
| how many cartons of 12 the eggs fill | 6, round down |
| each share of \$75 | \$6.25, keep dividing |

| Divisor | Divisible when |
|---|---|
| 2, 5, 10 | the last digit is even; is 0 or 5; is 0 |
| 4, 8 | the last two digits make a multiple of 4; the last three, of 8 |
| 3, 9 | the digit sum is a multiple of 3; of 9 |
| 6 | the number is divisible by 2 and by 3 |

Common mistakes:

- A remainder as big as the divisor: $38 \div 5$ is 7 remainder 3, not 6 remainder 8.
- Writing the remainder as a decimal digit: $75 \div 12$ is 6.25, not 6.3.
- Combining rules whose divisors share a factor: 12 is divisible by 2 and by 4 but not by 8.

### [Long division](07-long-division.md)

The division algorithm: for integers $n$ and $d$ with $d > 0$, there exist unique integers $q$ and $r$ with $n = qd + r$ and $0 \le r < d$. Long division finds them one digit at a time:

1. Divide: find how many times the divisor goes into the working number, and write that digit in the quotient.
2. Multiply the digit by the divisor, and subtract.
3. Compare: the difference must be smaller than the divisor.
4. Bring down the next digit, and repeat. Every digit brought down gets a quotient digit, even 0.
5. Check: $qd + r = n$.

The memory aid is "Dad, Mom, Sister, Cousin, Brother". To continue into decimals, write zeros after the point and keep going until the remainder is 0 or repeats: $7 \div 8 = 0.875$ and $1 \div 3 = 0.\overline{3}$.

Common mistakes:

- Skipping the zero in the quotient: $618 \div 6$ is 103, not 13.
- Putting the remainder after a point: $745 \div 3$ is 248 remainder 1, which is $248\frac{1}{3}$, not 248.1.

### [Factors, multiples and primes](08-factors-multiples-and-primes.md)

- A number $a$ is a factor of $b$, and $b$ a multiple of $a$, when $b = ka$ for a whole number $k$.
- A prime is a whole number greater than 1 whose only factors are 1 and itself. The numbers 0 and 1 are neither prime nor composite, and 2 is the only even prime.
- The 25 primes under 100: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97.
- By the fundamental theorem of arithmetic, every whole number greater than 1 is a product of primes in exactly one way, apart from order: $360 = 2^3 \times 3^2 \times 5$.
- To test for a prime, try only the primes whose squares are at most the number.

For the GCF and the LCM:

1. Write both prime factorizations.
2. GCF: each shared prime, with the smaller exponent. LCM: each prime in either, with the larger exponent.
3. Check: $\gcd(a, b) \times \operatorname{lcm}(a, b) = a \times b$.

From $84 = 2^2 \times 3 \times 7$ and $360 = 2^3 \times 3^2 \times 5$, the GCF is 12 and the LCM is 2,520. Euclid's algorithm gets the GCF from remainders alone: $360 = 4 \times 84 + 24$, $84 = 3 \times 24 + 12$, $24 = 2 \times 12 + 0$.

Common mistakes:

- Calling an odd number prime on sight: $51 = 3 \times 17$ and $91 = 7 \times 13$.
- Taking the product as the LCM: 12 and 18 have product 216 but LCM 36.

### [Fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md)

- The fraction $\frac{a}{b}$ is $a \div b$, with numerator $a$ and denominator $b \ne 0$. A mixed number is a sum: $2\frac{3}{4} = 2 + \frac{3}{4} = \frac{11}{4}$.
- Equivalent fractions: $\frac{a}{b} = \frac{a \times c}{b \times c}$ for $c \ne 0$, and $\frac{a}{b} = \frac{c}{d}$ exactly when $a \times d = c \times b$.
- Simplest form divides by the GCF: $\frac{180}{252} = \frac{5}{7}$.
- Improper to mixed, divide: $47 = 7 \times 6 + 5$, so $\frac{47}{6} = 7\frac{5}{6}$. Mixed to improper: $3\frac{2}{5} = \frac{3 \times 5 + 2}{5} = \frac{17}{5}$.

To compare two fractions:

1. With equal denominators, compare the numerators. With equal numerators, the smaller denominator wins.
2. Try the benchmark $\frac{1}{2}$: a fraction $\frac{a}{b}$ is bigger than it exactly when $2a > b$.
3. Otherwise cross-multiply. For $\frac{5}{8}$ and $\frac{7}{11}$, the products $5 \times 11 = 55$ and $7 \times 8 = 56$ show that $\frac{7}{11}$ is bigger.

Common mistakes:

- Adding the same number to the numerator and the denominator: $\frac{1}{2} \ne \frac{2}{3}$.
- Thinking a bigger denominator means a bigger fraction: $\frac{1}{8} < \frac{1}{4}$.
- Stopping too soon: $\frac{15}{21}$ still simplifies to $\frac{5}{7}$.

### [Adding and subtracting fractions](10-adding-and-subtracting-fractions.md)

1. Find the least common denominator (LCD), the LCM of the denominators.
2. Rewrite each fraction over the LCD, multiplying its numerator and denominator by the same number.
3. Add or subtract the numerators and keep the denominator.
4. Simplify, and check with an estimate.

For example, $\frac{3}{4} + \frac{5}{6} = \frac{9}{12} + \frac{10}{12} = \frac{19}{12} = 1\frac{7}{12}$. For mixed numbers, convert to improper fractions, or regroup 1 as $\frac{b}{b}$ when the fraction part is too small: $5\frac{1}{4} - 2\frac{2}{3} = 4\frac{15}{12} - 2\frac{8}{12} = 2\frac{7}{12}$. For two unit fractions, $\frac{1}{a} + \frac{1}{b} = \frac{a + b}{a \times b}$.

Common mistakes:

- Adding numerators and denominators: $\frac{1}{2} + \frac{1}{3}$ is $\frac{5}{6}$, not $\frac{2}{5}$.
- Changing a denominator without its numerator: $\frac{3}{4} = \frac{9}{12}$, not $\frac{3}{12}$.
- Regrouping 10 instead of a whole: $5\frac{3}{12} = 4\frac{15}{12}$, not $4\frac{13}{12}$.

### [Multiplying and dividing fractions](11-multiplying-and-dividing-fractions.md)

Multiply straight across, $\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}$, with no common denominator; "of" means multiply. The reciprocal of $\frac{a}{b}$ is $\frac{b}{a}$, and 0 has none. Dividing means multiplying by the reciprocal.

1. Write whole numbers over 1 and mixed numbers as improper fractions.
2. To divide, keep the first fraction, change $\div$ to $\times$ and flip the second.
3. Cancel a numerator with a denominator that shares a factor.
4. Multiply across, then check the size or multiply back.

For example, $2\frac{1}{4} \div \frac{3}{8} = \frac{9}{4} \times \frac{8}{3} = 6$. For positive numbers, multiplying by a number less than 1 makes the answer smaller and dividing by it makes the answer bigger: $\frac{5}{6} \times 30 = 25$ but $30 \div \frac{5}{6} = 36$.

Common mistakes:

- Cancelling two numerators, or cancelling across $+$ or $-$.
- Multiplying mixed numbers part by part: $2\frac{1}{2} \times 3\frac{1}{3}$ is $8\frac{1}{3}$, not $6\frac{1}{6}$.
- Flipping the first fraction instead of the divisor.

### [Decimal place value, adding and subtracting](12-decimals-place-value-and-adding.md)

- After the point come tenths, hundredths and thousandths: 24.375 is "twenty-four and three hundred seventy-five thousandths".
- Decimal to fraction: $0.45 = \frac{45}{100} = \frac{9}{20}$. Fraction to decimal: scale, as in $\frac{7}{20} = \frac{35}{100} = 0.35$, or divide, as in $\frac{3}{8} = 0.375$.
- To compare, pad with zeros to the same length: 0.405, 0.450 and 0.500 give $0.405 < 0.45 < 0.5$.
- To add or subtract, line up the decimal points (a whole number's point is at its right end), pad with zeros, and work as with whole numbers.

Common mistakes:

- Thinking longer means bigger: 0.45 is less than 0.5.
- Lining up the last digits: $14.3 + 2.75$ is 17.05, not 4.18.
- Dropping a zero after the point: 2.05 is not 2.5.

### [Multiplying and dividing decimals](13-multiplying-and-dividing-decimals.md)

To multiply, multiply as whole numbers, then count the decimal places in both factors together and place the point that many digits from the right: $4.36 \times 2.7$ is $436 \times 27 = 11{,}772$ with 3 places, 11.772.

To divide:

1. Move the divisor's point to its right end, and the dividend's point the same number of places.
2. Divide by long division, with the quotient's point straight above the dividend's.
3. Check: the quotient times the original divisor gives the dividend.

So $7.56 \div 0.18 = 756 \div 18 = 42$. A fraction in simplest form gives a terminating decimal exactly when its denominator has no prime factors other than 2 and 5, and otherwise it repeats: $\frac{3}{40} = 0.075$, but $\frac{5}{12} = 0.41\overline{6}$. In Python, `0.1 + 0.2 == 0.3` is `False`, because floats are binary fractions.

Common mistakes:

- Keeping one decimal place: $0.4 \times 0.2$ is 0.08, not 0.8.
- Moving only the divisor's point: $52.80 \div 1.65$ is 32, not 0.32.
- Dropping zeros before placing the point: $2.5 \times 0.4$ is 1.00, which is 1, not 0.01.

### [Powers of ten](14-powers-of-ten.md)

In $10^n$ the exponent $n$ counts the 10s multiplied together, so $10^n$ is 1 followed by $n$ zeros. Also $10^0 = 1$ and $10^{-n} = \frac{1}{10^n}$, so $10^{-2} = 0.01$.

| Operation | The point moves |
|---|---|
| $\times 10$, $\times 100$, $\times 1000$ | right 1, 2 or 3 places |
| $\div 10$, $\div 100$, $\div 1000$ | left 1, 2 or 3 places |
| $\times 0.1$, $\times 0.01$, $\times 0.001$ | left 1, 2 or 3 places |
| $\div 0.1$, $\div 0.01$, $\div 0.001$ | right 1, 2 or 3 places |

Fill empty places with zeros: $45 \div 1000 = 0.045$. The prefixes are giga (G) $10^9$, mega (M) $10^6$, kilo (k) $10^3$, centi (c) $10^{-2}$ and milli (m) $10^{-3}$.

Common mistakes:

- Treating the exponent as a factor: $10^3$ is 1000, not 30.
- Reading a negative exponent as a negative number: $10^{-2}$ is 0.01, not $-100$.
- Adding zeros to a decimal: $2.6 \times 1000$ is 2,600, not 2.6000.
- Mixing up M and m: a megawatt is a billion milliwatts.

### [Measurement and unit conversion](15-measurement-and-unit-conversion.md)

| Quantity | Facts |
|---|---|
| Length | 1 km = 1000 m, 1 m = 100 cm = 1000 mm |
| Mass | 1 kg = 1000 g, 1 g = 1000 mg |
| Capacity | 1 L = 1000 mL, $1\ \text{mL} = 1\ \text{cm}^3$, 1 L of water is about 1 kg |
| Area and volume | $1\ \text{m}^2 = 10{,}000\ \text{cm}^2$, $1\ \text{m}^3 = 1{,}000{,}000\ \text{cm}^3$ |
| Time | 1 min = 60 s, 1 h = 3600 s |
| Imperial (exact) | 1 in = 2.54 cm, 1 mi = 1.609344 km, 1 lb = 0.45359237 kg |

Between metric units, multiply going to a smaller unit and divide going to a bigger one. Otherwise multiply by conversion factors, fractions equal to 1, chosen so that each unwanted unit cancels:

$$
72\ \frac{\text{km}}{\text{h}} \times \frac{1000\ \text{m}}{1\ \text{km}} \times \frac{1\ \text{h}}{3600\ \text{s}} = 20\ \frac{\text{m}}{\text{s}}
$$

The shortcut is km/h divided by 3.6. Fahrenheit is $\frac{9}{5} \times \text{Celsius} + 32$ and Celsius is $\frac{5}{9} \times (\text{Fahrenheit} - 32)$, so 25°C is 77°F and 50°F is 10°C.

Common mistakes:

- Going the wrong way: 450 mg is 0.45 g, not 450,000 g.
- Using the length factor once for an area: $1\ \text{m}^2$ is $10{,}000\ \text{cm}^2$, not 100.
- Reading decimal hours as minutes: 3 h 40 min is about 3.67 h, and 0.4 h is 24 min.
- Skipping the 32: subtract it before multiplying by $\frac{5}{9}$.

### [Geometry basics](16-geometry-basics-area-perimeter-volume.md)

An acute angle is less than $90^\circ$, a right angle is $90^\circ$, an obtuse angle is between $90^\circ$ and $180^\circ$, and a straight angle is $180^\circ$. The height of a shape is the perpendicular distance from its base to the opposite vertex or side.

| Shape | Perimeter | Area or volume |
|---|---|---|
| rectangle, length $l$, width $w$ | $2l + 2w$ | $A = lw$ |
| square, side $s$ | $4s$ | $A = s^2$ |
| triangle, base $b$, height $h$ | add the sides | $A = \frac{1}{2}bh$ |
| parallelogram, base $b$, height $h$ | add the sides | $A = bh$ |
| rectangular box, $l$ by $w$ by $h$ | | $V = lwh$ |

Perimeter is a length (cm), area is in square units ($\text{cm}^2$) and volume in cubic units ($\text{cm}^3$). Convert every length to one unit first, and split an L-shape into rectangles. Doubling every length multiplies an area by 4 and a volume by 8.

Common mistakes:

- Using the slanted side as the height: a parallelogram with base 8, sides 5 and height 4 has area 32, not 40.
- Adding the length and the width once: an 8 by 5 rectangle has perimeter 26, not 13.
- Expecting the perimeter to fix the area: a 9 by 1 and a 5 by 5 rectangle both have perimeter 20, with areas 9 and 25.

<!-- lessons:start -->
## Lessons

1. [Place value and rounding](01-place-value-and-rounding.md)
2. [Addition and subtraction](02-addition-and-subtraction.md)
3. [Multiplication and times tables](03-multiplication-and-times-tables.md)
4. [Properties of operations](04-properties-of-operations.md)
5. [Multi-digit multiplication](05-multi-digit-multiplication.md)
6. [Division facts and remainders](06-division-facts-and-remainders.md)
7. [Long division](07-long-division.md)
8. [Factors, multiples and primes](08-factors-multiples-and-primes.md)
9. [Fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md)
10. [Adding and subtracting fractions](10-adding-and-subtracting-fractions.md)
11. [Multiplying and dividing fractions](11-multiplying-and-dividing-fractions.md)
12. [Decimals: place value, adding and subtracting](12-decimals-place-value-and-adding.md)
13. [Multiplying and dividing decimals](13-multiplying-and-dividing-decimals.md)
14. [Powers of ten](14-powers-of-ten.md)
15. [Measurement and unit conversion](15-measurement-and-unit-conversion.md)
16. [Geometry basics: area, perimeter and volume](16-geometry-basics-area-perimeter-volume.md)

<!-- lessons:end -->
