# Common mistakes

Each entry names a classic mistake, shows the wrong and the right version, says why the right one is right, and points to the lesson that teaches the idea. Most of them have a quick test: put in a small number, or work out both sides, and the wrong version gives a different answer. The lessons also flag each mistake at the step where it happens; this page collects them in one place.

## Arithmetic and order of operations

### Squaring a negative number without brackets

Wrong: $-3^2 = 9$

Right: $-3^2 = -9$, and $(-3)^2 = 9$

Exponents come before negation, so $-3^2$ means $-(3^2)$. To square the negative number, put it in brackets, and keep the brackets when you substitute a negative value: $2x^2$ at $x = -3$ is $2(-3)^2 = 18$, not $2 \cdot -3^2 = -18$. Calculators and Python follow the same rule: `-3**2` is `-9`. Excel is the exception, since its `=-3^2` gives 9.

Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#calculators-spreadsheets-and-code) and [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#example-1-evaluating-with-a-negative-value).

### Applying an exponent to more than the number before it

Wrong: $2 \times 3^2 = 6^2 = 36$

Right: $2 \times 3^2 = 2 \times 9 = 18$

An exponent applies only to the number or bracket right before it, and exponents come before multiplication. The same rule separates $3x^2$, which means $3 \cdot x^2$, from $(3x)^2$: at $x = 2$ the first is 12 and the second is 36.

Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#edge-cases-and-common-mistakes) and [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#how-multiplication-is-written).

### Dividing from right to left

Wrong: $24 \div 4 \div 2 = 24 \div 2 = 12$

Right: $24 \div 4 \div 2 = 6 \div 2 = 3$

Multiplication and division have the same rank, so they are done from left to right, and the same goes for addition and subtraction. The "DM" in BEDMAS doesn't put division first, and the "MD" in PEMDAS doesn't put multiplication first: $8 \div 2 \times 4 = 4 \times 4 = 16$, not $8 \div 8 = 1$. Division isn't associative, so moving the brackets changes the answer.

Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md) and [properties of operations](../01-elementary/04-properties-of-operations.md).

### Dividing by a sum term by term

Wrong: $12 \div (2 + 4) = 12 \div 2 + 12 \div 4 = 9$

Right: $12 \div (2 + 4) = 12 \div 6 = 2$

Division splits over a sum only when the sum is the number being divided: $(12 + 18) \div 6 = 2 + 3 = 5$. Dividing by a sum doesn't split, and the same goes for fractions, where $\frac{1}{2 + 4}$ is $\frac{1}{6}$, not $\frac{1}{2} + \frac{1}{4}$.

Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#edge-cases-and-common-mistakes).

### Typing a fraction on one line without brackets

Wrong: $\frac{12 + 6}{3 + 6}$ typed as `12 + 6 / 3 + 6`, which gives 20

Right: `(12 + 6) / (3 + 6)`, which gives 2

The fraction bar is a grouping symbol: it says to work out the whole numerator and the whole denominator first. Typed on one line, the bar becomes `/`, which ranks with multiplication, so only the 6 gets divided, and only by the 3. Put brackets around a numerator or a denominator that has more than one term.

Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#nested-brackets-and-the-fraction-bar).

### Rounding in stages

Wrong: 1,449 rounds to 1,450, and then to 1,500, so 1,449 to the nearest hundred is 1,500

Right: 1,449 to the nearest hundred is 1,400

Round once, from the original number, looking only at the digit right after the place you round to. Here that is the tens digit, 4, so the number rounds down: 1,449 is 49 from 1,400 and 51 from 1,500. Each stage can push the number a little further the same way, as 2.6449 goes to 2.645, 2.65 and then 2.7, while the right answer to the nearest tenth is 2.6.

Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#edge-cases-and-common-mistakes) and [decimals: place value, adding and subtracting](../01-elementary/12-decimals-place-value-and-adding.md#edge-cases-and-common-mistakes).

### Rounding in the middle of a calculation

Wrong: the 13% tax on five pastries at \$1.65 is $5 \times 0.21 = 1.05$ dollars, after rounding the tax on one pastry, $0.13 \times 1.65 = 0.2145$, to \$0.21

Right: the five pastries cost \$8.25, and the tax is $0.13 \times 8.25 = 1.0725$, or \$1.07

Each rounding dropped almost half a cent, and multiplying by 5 added the errors up. Keep every digit until the last step and round once, at the end. Rounding first is fine for an estimate, where easy arithmetic matters more than the last digit.

Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md#edge-cases-and-common-mistakes) and [place value and rounding](../01-elementary/01-place-value-and-rounding.md#should-i-round-before-or-after-i-calculate).

### Leaving out a zero in the quotient

Wrong: $612 \div 6 = 12$

Right: $612 \div 6 = 102$

After $6$ goes into $6$ once, the next digit brought down is $1$, which is smaller than $6$. That step still needs a digit in the quotient, so write $0$ there and bring down the $2$. The check catches the mistake: $12 \times 6 = 72$, far from $612$, while $102 \times 6 = 612$.

Taught in [long division](../01-elementary/07-long-division.md).

### Writing a remainder as a decimal digit

Wrong: $75 \div 12 = 6$ remainder 3, so $75 \div 12 = 6.3$

Right: $75 \div 12 = 6\frac{3}{12} = 6.25$

The 3 left over is 3 out of a divisor of 12, so it stands for $\frac{3}{12} = \frac{1}{4}$ of a whole, not for 3 tenths. Multiplying back catches the slip: $6.3 \times 12 = 75.6$, not 75. In the same way, $745 \div 3$ is 248 remainder 1, which is $248.333\ldots$ and not 248.1.

Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#edge-cases-and-common-mistakes) and [long division](../01-elementary/07-long-division.md#example-1-dividing-745-by-3).

## Negative numbers

### Ordering negative numbers by their digits

Wrong: $-27 > -4$, because 27 is bigger than 4

Right: $-27 < -4$

On the number line, $-27$ is further left than $-4$, and further left means less: a night at $-27^\circ\text{C}$ is colder than a night at $-4^\circ\text{C}$. Of two negative numbers, the one with the bigger absolute value is the smaller number.

Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#example-1-ordering-temperatures).

### Assuming the opposite of x is negative

Wrong: $-x$ is always negative

Right: $-x$ is the opposite of $x$, which is positive when $x$ is negative: if $x = -6$, then $-x = 6$

Read $-x$ as "the opposite of $x$" rather than "negative $x$", and its sign follows from the sign of $x$. This is why the definition of absolute value can say $\lvert x \rvert = -x$ for $x < 0$: there, $-x$ is positive.

Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#edge-cases-and-common-mistakes).

### Using "two negatives make a positive" in a sum

Wrong: $-3 + (-5) = 8$

Right: $-3 + (-5) = -8$

"Two negatives make a positive" is a rule for multiplication and division only. Adding a negative number moves left on the number line, so two purchases make a bigger overdraft, not a deposit.

Taught in [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#edge-cases-and-common-mistakes).

### Subtracting a negative number

Wrong: $6 - (-9) = 6 - 9 = -3$

Right: $6 - (-9) = 6 + 9 = 15$

Subtracting a number means adding its opposite, $a - b = a + (-b)$, and the opposite of $-9$ is 9. Dropping the brackets changes only one of the two signs. Check by adding back: $15 + (-9) = 6$.

Taught in [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#edge-cases-and-common-mistakes).

### Splitting an absolute value over a difference

Wrong: $\lvert 3 - 8 \rvert = \lvert 3 \rvert - \lvert 8 \rvert = -5$

Right: $\lvert 3 - 8 \rvert = \lvert -5 \rvert = 5$

Absolute value bars are grouping symbols, so work out what is inside them first. An absolute value is never negative, so $-5$ can't be right. Products do split, $\lvert ab \rvert = \lvert a \rvert \lvert b \rvert$, but sums and differences don't.

Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#edge-cases-and-common-mistakes) and [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#definitions).

### Putting the minus sign of a mixed number on the whole part only

Wrong: $-2\frac{1}{4} = -2 + \frac{1}{4}$

Right: $-2\frac{1}{4} = -\left(2 + \frac{1}{4}\right) = -\frac{9}{4}$

A mixed number is a sum, and the minus sign in front takes the opposite of all of it, the fraction part as well as the 2. The wrong version is $-1\frac{3}{4}$, a different number.

Taught in [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#example-2-negative-mixed-numbers).

## Factors, multiples and primes

### Calling 1 a prime

Wrong: the primes start 1, 2, 3, 5, 7

Right: the primes start 2, 3, 5, 7, and 1 is neither prime nor composite

A prime has exactly two positive factors, 1 and itself, and 1 has only one. Leaving 1 out keeps the fundamental theorem of arithmetic true: if 1 were prime, $6 = 2 \times 3 = 1 \times 2 \times 3$ would have two different prime factorizations.

Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions).

### Taking the product as the least common multiple

Wrong: $\operatorname{lcm}(12, 18) = 12 \times 18 = 216$

Right: $\operatorname{lcm}(12, 18) = 36$

The product of two numbers is always a common multiple, but it is the least one only when the two numbers have no common factor other than 1, as with 8 and 15. Fractions work the same way: the product of the denominators is always a common denominator, but for $\frac{3}{4}$ and $\frac{5}{6}$ the least one is 12, not 24.

Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#edge-cases-and-common-mistakes) and [adding and subtracting fractions](../01-elementary/10-adding-and-subtracting-fractions.md#definitions).

### Combining divisibility tests whose divisors share a factor

Wrong: 12 is divisible by 2 and by 4, so it is divisible by 8

Right: 12 is not divisible by 8

Two divisibility tests combine only when the divisors have no common factor other than 1. Divisible by 2 and by 3 does mean divisible by 6, but 2 and 4 share the factor 2, so together they only guarantee divisibility by 4, their least common multiple.

Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#edge-cases-and-common-mistakes).

### Reading Euclid's number as a prime

Wrong: $2 \times 3 \times 5 \times 7 \times 11 \times 13 + 1 = 30{,}031$ is prime, since no prime on the list divides it

Right: $30{,}031 = 59 \times 509$

Euclid's proof that there are infinitely many primes multiplies every prime on a finite list and adds 1. The result leaves remainder 1 when divided by each listed prime, so its prime factors are missing from the list. That is all the proof needs, and the number itself can be composite.

Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#the-sieve-of-eratosthenes).

### Giving a negative remainder

Wrong: $-17 = 5 \times (-3) + (-2)$, so $-17 \div 5$ has remainder $-2$

Right: $-17 = 5 \times (-4) + 3$, so the quotient is $-4$ and the remainder is 3

The division algorithm asks for $0 \le r < d$, so the remainder is never negative. Take the largest multiple of 5 that is not bigger than $-17$, which is $-20$. Python agrees, since `divmod(-17, 5)` is `(-4, 3)`. C, C++ and Java round the quotient toward 0 instead, so their `-17 % 5` is `-2`.

Taught in [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#challenge) and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

## Fractions, decimals and percents

### Adding the numerators and the denominators

Wrong: $\frac{1}{2} + \frac{1}{3} = \frac{2}{5}$

Right: $\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}$

Fractions can be added directly only when they count pieces of the same size, so rewrite them over a common denominator first. A size check shows the wrong answer can't be right: $\frac{2}{5}$ is less than $\frac{1}{2}$, but adding $\frac{1}{3}$ to $\frac{1}{2}$ has to give more than $\frac{1}{2}$.

Taught in [adding and subtracting fractions](../01-elementary/10-adding-and-subtracting-fractions.md).

### Multiplying mixed numbers part by part

Wrong: $2\frac{1}{2} \times 3\frac{1}{3} = 2 \times 3 + \frac{1}{2} \times \frac{1}{3} = 6\frac{1}{6}$

Right: $2\frac{1}{2} \times 3\frac{1}{3} = \frac{5}{2} \times \frac{10}{3} = \frac{50}{6} = 8\frac{1}{3}$

A mixed number is a sum, $2\frac{1}{2} = 2 + \frac{1}{2}$, and multiplying two sums takes four products, not two. Change each mixed number to an improper fraction first. The same misreading turns $2\frac{3}{4}$ into $2 \times \frac{3}{4}$, when it means $2 + \frac{3}{4} = \frac{11}{4}$.

Taught in [multiplying and dividing fractions](../01-elementary/11-multiplying-and-dividing-fractions.md#example-3-multiplying-two-mixed-numbers) and [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#edge-cases-and-common-mistakes).

### Flipping the wrong fraction when dividing

Wrong: $\frac{2}{3} \div \frac{4}{5} = \frac{3}{2} \times \frac{4}{5} = \frac{6}{5}$

Right: $\frac{2}{3} \div \frac{4}{5} = \frac{2}{3} \times \frac{5}{4} = \frac{5}{6}$

Dividing by a number means multiplying by its reciprocal, so only the divisor, the fraction after the $\div$ sign, flips. The wrong version works out $\frac{4}{5} \div \frac{2}{3}$, which is the reciprocal of the right answer.

Taught in [multiplying and dividing fractions](../01-elementary/11-multiplying-and-dividing-fractions.md#edge-cases-and-common-mistakes).

### Comparing decimals by their length

Wrong: $0.45 > 0.5$, because 45 is bigger than 5

Right: $0.45 < 0.5$

After the point, extra digits are smaller and smaller pieces, so more digits doesn't mean a bigger number. Pad with zeros to the same number of places and compare: 0.45 is 45 hundredths, and 0.50 is 50 hundredths.

Taught in [decimals: place value, adding and subtracting](../01-elementary/12-decimals-place-value-and-adding.md#example-3-putting-decimals-in-order).

### Keeping one decimal place in a product

Wrong: $0.4 \times 0.2 = 0.8$

Right: $0.4 \times 0.2 = 0.08$

Tenths times tenths are hundredths: $\frac{4}{10} \times \frac{2}{10} = \frac{8}{100}$. A product has as many decimal places as its two factors together, here $1 + 1 = 2$. Lining up the points is a rule for adding and subtracting, not for multiplying.

Taught in [multiplying and dividing decimals](../01-elementary/13-multiplying-and-dividing-decimals.md#edge-cases-and-common-mistakes).

### Moving only the divisor's decimal point

Wrong: $52.80 \div 1.65$ becomes $52.80 \div 165 = 0.32$

Right: move both points two places, so $52.80 \div 1.65 = 5280 \div 165 = 32$

A division is a fraction, and multiplying its numerator and denominator by the same power of 10 keeps its value. Moving only one point multiplies just the divisor by 100, which makes the answer 100 times too small. An estimate catches it: 1.65 goes into 52.80 a bit more than 30 times.

Taught in [multiplying and dividing decimals](../01-elementary/13-multiplying-and-dividing-decimals.md#example-4-dividing-by-a-decimal).

### Multiplying a decimal by 10 by writing a zero

Wrong: $4.6 \times 10 = 4.60$

Right: $4.6 \times 10 = 46$

Writing a 0 on the right works only for whole numbers, and 4.60 is the same number as 4.6. What really happens is that every digit moves one place to the left, so the point moves one place right. Multiplying by 1000 moves it three places, so $2.6 \times 1000 = 2600$, and dividing by 1000 moves it three places left, so $45 \div 1000 = 0.045$.

Taught in [multiplication and times tables](../01-elementary/03-multiplication-and-times-tables.md#edge-cases-and-common-mistakes) and [powers of ten](../01-elementary/14-powers-of-ten.md#example-1-multiplying-26-by-1000).

### Reading half a percent as one half

Wrong: $0.5\% = 0.5$

Right: $0.5\% = \frac{0.5}{100} = 0.005$, and $0.5 = 50\%$

Percent means "divide by 100", so going between a percent and a decimal moves the point two places. A 0.5% fee on \$2,000 is \$10; read as 50%, it would be \$1,000.

Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md).

### Using the wrong whole for a percent

Wrong: a seminar has 12 women and 18 men, so $\frac{12}{18} \approx 66.7\%$ of it is women

Right: the whole is everyone in the seminar, so the share of women is $\frac{12}{12 + 18} = \frac{12}{30} = 40\%$

Before you divide, ask "percent of what?" The whole is the amount that counts as 100%, usually the noun right after "of". Dividing by 18 answers a different question: it says there are two thirds as many women as men.

Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md#edge-cases-and-common-mistakes).

### Taking tax off by subtracting 13 percent

Wrong: a total of \$113.00 that includes 13% HST came from a price of $113 - 0.13 \times 113 = 98.31$

Right: the price before tax was $113 \div 1.13 = 100$, that is, \$100.00

The 13% was taken of the price before tax, not of the total, so the total is 113% of the price. Divide by $1.13$ to undo multiplying by $1.13$. Adding the tax back on shows the error: $1.13 \times 98.31 = 111.09$, which is not the total.

Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md) and [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).

### Dividing by the new value in a percent change

Wrong: a laptop that drops from \$1,299 to \$1,049 is $\frac{250}{1049} \approx 23.8\%$ cheaper

Right: it is $\frac{250}{1299} \approx 19.2\%$ cheaper

A percent change is measured against the starting value, so divide the change by the old value. The 23.8% answers a different question: the old price was 23.8% more than the new one.

Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#example-1-a-laptop-goes-on-sale).

### Adding percent changes

Wrong: a 10% rise followed by a 10% fall leaves a price where it started

Right: $100 \times 1.10 \times 0.90 = 99$, so the price ends 1% lower

Each change is a percent of a different whole: on a \$100 price, the rise is 10% of \$100 and the fall is 10% of \$110. Percent changes combine by multiplying their factors, $1.10 \times 0.90 = 0.99$, and adding the percents skips that step. Discounts work the same way: 40% off and then 25% off multiplies the price by $0.60 \times 0.75 = 0.45$, which is 55% off, not 65%. For the same reason, undoing a 25% rise takes a 20% fall, since $1.25 \times 0.80 = 1$.

Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#edge-cases-and-common-mistakes).

### Reading tripled as a 300 percent increase

Wrong: a price that triples has risen by 300%

Right: it has risen by 200%, since the new price is 300% of the old one

The multiplier is 3, and the rate of change is the multiplier minus 1, so it is $3 - 1 = 2$, or 200%. "300% of" and "300% more than" are different: the first is three times as much, and the second is four times as much.

Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#edge-cases-and-common-mistakes).

### Confusing markup with margin

Wrong: a 50% markup gives a 50% margin

Right: a 50% markup gives a margin of $\frac{50}{150} \approx 33.3\%$

Both compare the same profit, but the markup divides it by the cost and the margin divides it by the selling price, which is bigger. An item that costs \$100 and sells for \$150 has a markup of 50% and a margin of 33.3%. To get a 50% margin, a store has to mark its cost up by 100%.

Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#edge-cases-and-common-mistakes).

### Confusing percent change with percentage points

Wrong: an interest rate that goes from 4% to 5% has gone up by 1%

Right: it has gone up by 1 percentage point, which is a 25% increase, since $\frac{5 - 4}{4} = 0.25$

A percentage point is the plain difference between two percents. A percent change compares that difference to the starting value. News reports and economics papers use both, so check which one a sentence means.

Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#percent-change-or-percentage-points) and percent change vs percentage points<!-- link: ../07-economics-math/01-measuring-the-economy/02-percent-change-vs-percentage-points.md -->.

## Ratios and proportions

### Reading a part-to-part ratio as a fraction of the whole

Wrong: a lecture has economics and CS students in the ratio $3:5$, so $\frac{3}{5}$ of the lecture studies economics

Right: $\frac{3}{3 + 5} = \frac{3}{8}$ of the lecture studies economics

The ratio $3:5$ compares two parts. Out of every $3 + 5 = 8$ students, 3 study economics, so the part-to-whole ratio is $3:8$. Check that the parts make up the whole: $\frac{3}{8} + \frac{5}{8} = 1$.

Taught in [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#edge-cases-and-common-mistakes).

### Scaling a ratio by adding

Wrong: doubling a juice recipe of 1 can of concentrate to 3 cans of water gives the ratio $2:4$

Right: doubling it gives $2:6$

Equivalent ratios come from multiplying or dividing every term by the same nonzero number. Adding 1 to each term changes the comparison, since $\frac{1}{3} \ne \frac{2}{4}$, and the drink gets stronger.

Taught in [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#edge-cases-and-common-mistakes).

### Using a proportion when there is a fixed charge

Wrong: a 5 km taxi ride costs \$14.50, so a 10 km ride costs twice as much, \$29.00

Right: with a \$4.50 base fare and \$2.00 per kilometre, a 10 km ride costs $4.50 + 2.00 \times 10 = 24.50$ dollars

A proportion works only when zero of one quantity goes with zero of the other. A base fare, a delivery fee or a flat monthly charge breaks this, because you pay it once whatever the amount. Before you set up a proportion, ask "would zero of this cost zero?"

Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#edge-cases-and-common-mistakes).

## Measurement and geometry

### Converting square units with the length factor

Wrong: $1\ \text{m}^2 = 100\ \text{cm}^2$

Right: $1\ \text{m}^2 = 10{,}000\ \text{cm}^2$

A square 1 m on each side is 100 cm by 100 cm, so it holds 100 rows of 100 small squares. Area units convert with the square of the length factor and volume units with its cube, so $1\ \text{m}^3 = 1{,}000{,}000\ \text{cm}^3$. Scale drawings work the same way: at $1:50$, lengths scale by 50 but areas by $50^2 = 2500$.

Taught in [measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#edge-cases-and-common-mistakes) and [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#edge-cases-and-common-mistakes).

### Writing minutes as hundredths of an hour

Wrong: 3 h 40 min is 3.40 h

Right: 3 h 40 min is $3 + \frac{40}{60} \approx 3.67$ h

Minutes are sixtieths of an hour, not hundredths. The 0.40 in 3.40 h is $0.4 \times 60 = 24$ minutes.

Taught in [measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#example-3-decimal-hours).

### Using the slanted side as the height

Wrong: a parallelogram with base 8 cm, slanted sides of 5 cm and height 4 cm has area $8 \times 5 = 40\ \text{cm}^2$

Right: its area is base times height, $8 \times 4 = 32\ \text{cm}^2$

The height is the perpendicular distance from the base to the opposite side, measured at a right angle to the base. A slanted path between the two sides is always longer than the straight one, so using it makes the area too big. A triangle's area, $\frac{1}{2}bh$, uses the height in the same sense.

Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#example-2-a-parallelogram-and-a-slanted-side).

## Exponents and roots

### Multiplying the base by the exponent

Wrong: $10^3 = 10 \times 3 = 30$

Right: $10^3 = 10 \times 10 \times 10 = 1000$

The exponent counts how many copies of the base are multiplied together; it is not a factor. Saying the power aloud helps: "three tens multiplied together".

Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#edge-cases-and-common-mistakes).

### Multiplying the bases when multiplying powers

Wrong: $2^3 \cdot 2^4 = 4^7$

Right: $2^3 \cdot 2^4 = 2^{3+4} = 2^7 = 128$

The product is three 2s times four 2s, which is seven 2s, so the base stays $2$ and the exponents add. The wrong answer, $4^7 = 16{,}384$, is far too big. Powers with different bases and the same exponent combine the other way: $2^3 \cdot 5^3 = 10^3$.

Taught in [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).

### Treating a negative exponent as a negative number

Wrong: $2^{-1} = -2$

Right: $2^{-1} = \frac{1}{2}$

A negative exponent means a reciprocal: $a^{-n} = \frac{1}{a^n}$ for $a \ne 0$. The pattern $2^2 = 4$, $2^1 = 2$, $2^0 = 1$ halves at each step, so the next value is $2^{-1} = \frac{1}{2}$. Every power of a positive base is positive, so $10^{-2}$ is $0.01$, not $-100$.

Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#edge-cases-and-common-mistakes) and [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).

### Splitting a square root over a sum

Wrong: $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$

Right: $\sqrt{a + b}$ doesn't simplify in general. Products do split: $\sqrt{ab} = \sqrt{a}\,\sqrt{b}$ for $a, b \ge 0$.

Test with numbers: $\sqrt{9 + 16} = \sqrt{25} = 5$, while $\sqrt{9} + \sqrt{16} = 3 + 4 = 7$. A root, like a power, works with multiplication and not with addition.

Taught in [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md).

### Writing the square root of x squared as x

Wrong: $\sqrt{x^2} = x$

Right: $\sqrt{x^2} = \lvert x \rvert$

A square root is never negative, so it can't give back $x$ when $x$ is negative. With $x = -3$, the left side is $\sqrt{(-3)^2} = \sqrt{9} = 3$, which is $\lvert -3 \rvert$ and not $-3$. Watch for this step in any proof that takes the square root of both sides.

Taught in [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md).

### Mixing up a square root with the solutions of a square

Wrong: $\sqrt{9} = \pm 3$, or $x^2 = 9$ means $x = 3$

Right: $\sqrt{9} = 3$, and $x^2 = 9$ means $x = 3$ or $x = -3$

The symbol $\sqrt{9}$ names one number, the non-negative one. The equation $x^2 = 9$ asks for every number whose square is $9$, and there are two of them. When you solve, write $x = \pm\sqrt{9} = \pm 3$.

Taught in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md) and [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md).

## Algebra

### Writing a less-than phrase in the wrong order

Wrong: "5 less than twice $n$" is $5 - 2n$

Right: it is $2n - 5$

"5 less than" a number starts from the number and takes 5 away, so the 5 is subtracted even though it is said first. "5 subtracted from $n$" works the same way, while "the difference of $n$ and 5" keeps the spoken order, $n - 5$.

Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#writing-an-expression-from-words).

### Combining unlike terms

Wrong: $3x + 2 = 5x$

Right: $3x + 2$ is already simplified

Only like terms, with the same variables raised to the same powers, combine into one term. Test at $x = 2$: $3x + 2 = 8$, while $5x = 10$. In the same way, $x^2 + x$ is neither $x^3$ nor $2x^2$.

Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#edge-cases-and-common-mistakes).

### Squaring a sum term by term

Wrong: $(a + b)^2 = a^2 + b^2$

Right: $(a + b)^2 = a^2 + 2ab + b^2$

Squaring means multiplying $(a + b)(a + b)$, and the two cross products $ab$ and $ba$ make the middle term. Test with $a = b = 1$: the left side is $2^2 = 4$, but $a^2 + b^2 = 2$. With numbers, $(3 + 4)^2 = 49$, while $3^2 + 4^2 = 25$.

Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#edge-cases-and-common-mistakes) and [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md).

### Cancelling terms instead of factors

Wrong: $\frac{x + 3}{x} = 3$, by crossing out the $x$ on top and the $x$ on the bottom

Right: $\frac{x + 3}{x} = \frac{x}{x} + \frac{3}{x} = 1 + \frac{3}{x}$, for $x \ne 0$

Cancelling divides the numerator and the denominator by the same number, so it works only on a factor of the whole numerator. Here $x$ is a term of the numerator, not a factor of it. Test with $x = 1$: $\frac{1 + 3}{1} = 4$, not $3$. By contrast, $\frac{3x}{x} = 3$ for $x \ne 0$, because $x$ is a factor of $3x$. The same rule holds for numbers: in $\frac{2}{3} + \frac{3}{5}$ the two 3s don't cancel, because a sum is not a product.

Taught in [multiplying and dividing fractions](../01-elementary/11-multiplying-and-dividing-fractions.md#edge-cases-and-common-mistakes) and rational expressions<!-- link: ../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md -->.

### Subtracting only the first term in brackets

Wrong: $5 - (x + 2) = 5 - x + 2$

Right: $5 - (x + 2) = 5 - x - 2 = 3 - x$

The minus sign in front of the brackets multiplies every term inside by $-1$. Test with $x = 0$: the original is $5 - 2 = 3$, the right version gives $3 - 0 = 3$, and the wrong version gives $5 - 0 + 2 = 7$. A number in front of brackets has to reach every term too: $2(x + 3) = 2x + 6$, not $2x + 3$, and $3 \times (4 + 5) = 27$, not $3 \times 4 + 5 = 17$.

Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md) and [properties of operations](../01-elementary/04-properties-of-operations.md#edge-cases-and-common-mistakes).

### Distributing over a product

Wrong: $2(xy) = (2x)(2y)$

Right: $2(xy) = 2xy$

The distributive property spreads a multiplication over a sum, never over a product. A product is regrouped with the associative property, so the 2 multiplies only once. Test at $x = 3$ and $y = 5$: $2xy = 30$, while $(2x)(2y) = 60$.

Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#edge-cases-and-common-mistakes).

## Equations and inequalities

### Leaving the answer as the opposite of x

Wrong: $-x = 8$, so $x = 8$

Right: $-x = 8$, so $x = -8$

The equation says that $x$ is the opposite of 8. Since $-x$ means $-1 \cdot x$, divide both sides by $-1$. A check in the original equation catches the slip.

Taught in [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#edge-cases-and-common-mistakes).

### Checking a solution in a later line

Wrong: a slip turns $3x + 11 = 2$ into $3x = 9$, and $x = 3$ checks in $3x = 9$, so it looks right

Right: check in the original equation, where $3(3) + 11 = 20$, not 2; the solution is $x = -3$

A later line already contains every mistake made on the way to it, so a check there can't catch them. Only the original equation can.

Taught in [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#edge-cases-and-common-mistakes).

### Clearing fractions in only some terms

Wrong: multiplying $\frac{x}{2} + 3 = 5$ by 2 gives $x + 3 = 10$, so $x = 7$

Right: it gives $x + 6 = 10$, so $x = 4$

Multiplying both sides by 2 multiplies every term, including the ones with no fraction. The check shows the error: $\frac{7}{2} + 3 = 6.5$, not 5, while $\frac{4}{2} + 3 = 5$.

Taught in [multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#edge-cases-and-common-mistakes).

### Reading an always-true equation as the solution 0

Wrong: $2(x + 3) = 2x + 6$ simplifies to $0 = 0$, so $x = 0$

Right: every number is a solution

When the variable cancels and a true statement such as $0 = 0$ is left, the equation is an identity, and every number solves it. When a false statement such as $6 = 5$ is left, there is no solution. "The solution is 0" is a third case, as in $5x = 3x$, where the variable is still there to solve for.

Taught in [multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#edge-cases-and-common-mistakes).

### Not flipping an inequality after multiplying by a negative

Wrong: $-2x < 6$, so $x < -3$

Right: $-2x < 6$, so $x > -3$

Multiplying or dividing both sides by a negative number reverses the order, just as $2 < 3$ but $-2 > -3$. Check with a number from the right answer: $x = 0$ satisfies $0 > -3$, and $-2 \cdot 0 = 0 < 6$ is true.

Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md).

### Flipping an inequality because a negative number appears

Wrong: $3x < -12$, so $x > -4$

Right: $3x < -12$, so $x < -4$

Only multiplying or dividing both sides by a negative number reverses the symbol. Here you divide by 3, which is positive, so the symbol stays, and the $-12$ on the right changes nothing. Test $x = -5$: it satisfies $x < -4$, and $3(-5) = -15 < -12$ is true.

Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#edge-cases-and-common-mistakes).

### Dividing both sides by a variable that might be zero

Wrong: $x^2 = 3x$, and dividing by $x$ gives $x = 3$

Right: $x^2 - 3x = 0$, so $x(x - 3) = 0$, and $x = 0$ or $x = 3$

Dividing by $x$ is allowed only when $x \ne 0$, so it throws away the solution $x = 0$. Move every term to one side and factor instead. Both answers check: $0^2 = 3 \cdot 0$ and $3^2 = 3 \cdot 3$. The same slip turns $5x = 3x$ into $5 = 3$, which seems to say there is no solution, though $x = 0$ works.

Taught in [multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#dividing-by-an-expression-that-might-be-zero) and [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md).

### Keeping every solution after squaring both sides

Wrong: $\sqrt{x + 2} = x$ has the solutions $x = 2$ and $x = -1$

Right: only $x = 2$ is a solution

Squaring gives $x + 2 = x^2$, so $x^2 - x - 2 = 0$ and $(x - 2)(x + 1) = 0$. Squaring can add solutions, because $a = b$ and $a = -b$ both turn into $a^2 = b^2$, so check each candidate in the original equation. For $x = -1$ the left side is $\sqrt{1} = 1$ and the right side is $-1$, so $-1$ is an extraneous root.

Taught in rational and radical equations<!-- link: ../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md -->.

### Multiplying an inequality by an expression of unknown sign

Wrong: $\frac{1}{x} < 2$, so $1 < 2x$, so $x > \frac{1}{2}$

Right: $\frac{1}{x} < 2$ exactly when $x < 0$ or $x > \frac{1}{2}$

Multiplying by $x$ keeps the order only when $x > 0$. For $x < 0$ the order flips and gives $1 > 2x$, which every negative $x$ satisfies. Test $x = -1$: $\frac{1}{-1} = -1 < 2$, so it is a solution the wrong method lost. Split into cases by sign, or move every term to one side and use a sign chart.

Taught in polynomial and rational inequalities<!-- link: ../03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md -->.

## Functions and graphs

### Reading the inverse function as a reciprocal

Wrong: $f^{-1}(x) = \frac{1}{f(x)}$

Right: $f^{-1}$ undoes $f$, so $f^{-1}(y) = x$ exactly when $f(x) = y$

For $f(x) = 2x$ the inverse is $f^{-1}(x) = \frac{x}{2}$, so $f^{-1}(4) = 2$, while $\frac{1}{f(4)} = \frac{1}{8}$. The notation invites the mix-up, because $\sin^2 x$ means $(\sin x)^2$ but $\sin^{-1} x$ means the inverse function $\arcsin x$. When you mean the reciprocal, write $\frac{1}{f(x)}$ or $(f(x))^{-1}$.

Taught in [composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md).

### Adding h outside the function

Wrong: $f(x + h) = f(x) + h$

Right: replace every $x$ in the rule with $(x + h)$. For $f(x) = x^2$, that gives $f(x + h) = (x + h)^2 = x^2 + 2xh + h^2$.

Test with $x = 3$ and $h = 1$: $f(4) = 16$, while $f(3) + 1 = 10$. The input has changed, so the whole rule applies to the new input. This substitution is the first step of every derivative worked from the definition.

Taught in [what is a function](../03-high-school/03-functions/01-what-is-a-function.md) and the derivative definition<!-- link: ../05-university-core/02-derivatives/01-the-derivative-definition.md -->.

### Shifting a graph the wrong way

Wrong: the graph of $y = (x - 2)^2$ is the graph of $y = x^2$ moved 2 units left

Right: it is moved 2 units right

The new graph reaches each height when $x - 2$ equals the old input, which happens 2 units further right. The lowest point of $y = (x - 2)^2$ is at $x = 2$, where $x - 2 = 0$. Subtracting inside the function moves the graph right; subtracting outside, as in $y = x^2 - 2$, moves it down.

Taught in [transformations of functions](../03-high-school/03-functions/04-transformations-of-functions.md).

## Logarithms

### Splitting a logarithm over a sum

Wrong: $\log(a + b) = \log a + \log b$

Right: $\log(ab) = \log a + \log b$, and $\log(a + b)$ doesn't simplify

A logarithm turns multiplication into addition, because exponents add when you multiply powers of the same base. Test with base-10 logarithms: $\log(10 + 10) = \log 20 \approx 1.301$, while $\log 10 + \log 10 = 2$, which is $\log 100$.

Taught in logarithm properties<!-- link: ../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md -->.

### Treating a quotient of logarithms as one logarithm

Wrong: $\frac{\log 8}{\log 2} = \log 4$

Right: $\frac{\log 8}{\log 2} = \log_2 8 = 3$

A quotient of two logarithms is the change-of-base formula, $\log_b x = \frac{\log x}{\log b}$. The rule $\log \frac{x}{y} = \log x - \log y$ is about the logarithm of a quotient, which is a different thing. Check: $\log 4 \approx 0.602$ in base 10, but $\frac{\log 8}{\log 2} = 3$ in every base, since $2^3 = 8$.

Taught in logarithm properties<!-- link: ../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md -->.

## Logic and proofs

### Confusing a statement with its converse

Wrong: "if $n$ is divisible by 4, then $n$ is even" is true, so "if $n$ is even, then $n$ is divisible by 4" is true

Right: the converse is a different statement and needs its own proof. Here it is false, since $6$ is even but not divisible by $4$.

The converse of "if P, then Q" is "if Q, then P", and knowing one tells you nothing about the other. Only the contrapositive, "if not Q, then not P", is equivalent to the original.

Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

### Using the inverse in place of the contrapositive

Wrong: "if $x > 2$, then $x^2 > 4$" is equivalent to "if $x \le 2$, then $x^2 \le 4$"

Right: it is equivalent to its contrapositive, "if $x^2 \le 4$, then $x \le 2$"

The statement in the wrong line is the inverse, and it fails at $x = -3$, where $x \le 2$ but $(-3)^2 = 9 > 4$. The contrapositive negates both parts and swaps them; the inverse negates them without swapping. A proof by contrapositive has to start from "not Q".

Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md --> and contrapositive proof<!-- link: ../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md -->.

### Negating a statement about every case

Wrong: the negation of "every student passed" is "no student passed"

Right: the negation is "some student did not pass"

A statement about every case is false as soon as one case fails, so its negation says that a failing case exists. In symbols, $\neg(\forall x\ P(x)) \equiv \exists x\ \neg P(x)$, and $\neg(\exists x\ P(x)) \equiv \forall x\ \neg P(x)$. The sentence "no student passed" claims much more than the negation does, and it is usually false as well.

Taught in negation and translating English<!-- link: ../04-proofs-and-logic/02-logic-and-sets/05-negation-and-translating-english.md -->.

### Proving a general claim with examples

Wrong: $n^2 + n + 41$ is prime for $n = 0, 1, 2, 3, 4$, so it is prime for every natural number $n$

Right: examples can't prove a claim about every $n$. This claim is false: for $n = 40$, $40^2 + 40 + 41 = 1681 = 41^2$.

The formula gives a prime for every $n$ from $0$ to $39$ and still fails at $40$. To prove a claim for every $n$, take an arbitrary $n$ and argue from the definitions. Examples do settle the opposite question, since one counterexample disproves a claim about every case. The same holds for algebra: $x^2 + 2$ and $3x$ agree at $x = 1$ and $x = 2$, but they are not equivalent expressions.

Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division), [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#why-isnt-checking-a-few-values-enough), common proof mistakes<!-- link: ../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md --> and counterexamples and disproof<!-- link: ../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md -->.

### Assuming what you want to prove

Wrong: to prove $a^2 + b^2 \ge 2ab$, start from it, subtract $2ab$ to get $a^2 - 2ab + b^2 \ge 0$, reach $(a - b)^2 \ge 0$, and stop because that is true

Right: start from a known fact, $(a - b)^2 \ge 0$, expand it to $a^2 - 2ab + b^2 \ge 0$, and add $2ab$ to both sides to reach $a^2 + b^2 \ge 2ab$

Reaching a true statement from the claim proves nothing, because a false claim can lead to a true one: $-1 = 1$ is false, but squaring both sides gives $1 = 1$. Working backward is fine as scratch work for finding the steps. The written proof has to run forward from known facts, with each step following from the ones before it.

Taught in scratch work and proof strategies<!-- link: ../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md -->.

### Skipping the base case in induction

Wrong: every natural number $n$ satisfies $n > n + 1$, because if $k > k + 1$, then adding 1 to both sides gives $k + 1 > k + 2$

Right: that inductive step is valid, but the claim is false, because the base case fails: $0 > 1$ is false

Induction needs both parts. The inductive step only says that each case passes its truth on to the next one, and the base case is what starts the chain. Without it, the argument above would prove a statement that is false for every $n$.

Taught in mathematical induction<!-- link: ../04-proofs-and-logic/05-induction/01-mathematical-induction.md -->.

## Counting and probability

### Multiplying probabilities of events that are not independent

Wrong: $P(A \cap B) = P(A)\,P(B)$ for every pair of events

Right: $P(A \cap B) = P(A)\,P(B \mid A)$ always, and $P(A \cap B) = P(A)\,P(B)$ only when $A$ and $B$ are independent

Roll one die, and let $A$ be "even" and $B$ be "at least 4". Then $A \cap B = \{4, 6\}$, so $P(A \cap B) = \frac{2}{6} = \frac{1}{3}$, while $P(A)\,P(B) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$. Knowing the roll is even makes "at least 4" more likely ($\frac{2}{3}$ instead of $\frac{1}{2}$), so the events are not independent.

Taught in conditional probability and Bayes' theorem<!-- link: ../05-university-core/07-probability/02-conditional-probability-and-bayes.md -->.

### Swapping the two sides of a conditional probability

Wrong: $P(A \mid B) = P(B \mid A)$

Right: $P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$, which is Bayes' theorem, and the two sides are usually different

Draw one card from a standard deck. The probability that it is a king, given that it is a face card, is $\frac{4}{12} = \frac{1}{3}$; the probability that it is a face card, given that it is a king, is $1$. The same mistake misleads people about medical tests: a test that catches most sick people can still give mostly false alarms when the disease is rare.

Taught in conditional probability and Bayes' theorem<!-- link: ../05-university-core/07-probability/02-conditional-probability-and-bayes.md -->.

### Counting ordered choices when order doesn't matter

Wrong: the number of 2-person committees you can form from 5 people is $5 \times 4 = 20$

Right: it is $\binom{5}{2} = \frac{5 \times 4}{2} = 10$

The count $5 \times 4$ lists each committee twice, once as (Ana, Ben) and once as (Ben, Ana). Ask whether swapping two choices gives a different outcome. If it does, as with choosing a president and a vice-president, order matters and $20$ is right; if not, divide out the orderings.

Taught in counting: permutations and combinations<!-- link: ../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md -->.

### Counting the integers in a range off by one

Wrong: there are $10 - 3 = 7$ integers from 3 to 10, inclusive

Right: there are $10 - 3 + 1 = 8$

Subtracting counts the gaps between the numbers, and there is one more number than there are gaps, just as a fence with 7 gaps needs 8 posts. In general there are $b - a + 1$ integers from $a$ to $b$, inclusive. Python's `range(3, 11)` has 8 elements because it leaves out its upper end.

Taught in counting rules<!-- link: ../06-cs-math/03-counting-and-discrete-probability/01-counting-rules.md -->.

## Calculus

### Giving up on a limit that gives zero over zero

Wrong: $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$ doesn't exist, because putting in $x = 2$ gives $\frac{0}{0}$

Right: factor first. For $x \ne 2$, $\frac{x^2 - 4}{x - 2} = \frac{(x - 2)(x + 2)}{x - 2} = x + 2$, so the limit is $4$.

The form $\frac{0}{0}$ only says that substitution failed to give an answer. A limit depends on the values near $2$ and never on the value at $2$, so cancelling the factor $x - 2$, which is nonzero near $2$, is allowed.

Taught in limits, intuition and limit laws<!-- link: ../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md -->.

### Multiplying derivatives for the derivative of a product

Wrong: $\frac{d}{dx}(fg) = f'g'$

Right: $\frac{d}{dx}(fg) = f'g + fg'$

Test with $f(x) = g(x) = x$: the product is $x^2$, whose derivative is $2x$, but $f'g' = 1 \cdot 1 = 1$. The product rule gives $1 \cdot x + x \cdot 1 = 2x$. Quotients have their own rule as well, and $\left(\frac{f}{g}\right)'$ is not $\frac{f'}{g'}$.

Taught in differentiation rules<!-- link: ../05-university-core/02-derivatives/02-differentiation-rules.md -->.

### Forgetting the chain rule

Wrong: $\frac{d}{dx} \sin(3x) = \cos(3x)$

Right: $\frac{d}{dx} \sin(3x) = 3\cos(3x)$

When a function is applied to something other than plain $x$, multiply by the derivative of the inside: $\frac{d}{dx} f(g(x)) = f'(g(x))\,g'(x)$. The inside here is $3x$, with derivative $3$. In the same way, $\frac{d}{dx}(x^2 + 1)^5 = 5(x^2 + 1)^4 \cdot 2x$.

Taught in chain rule, implicit and inverse derivatives<!-- link: ../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md -->.

### Forgetting the constant of integration

Wrong: $\int 2x\,dx = x^2$

Right: $\int 2x\,dx = x^2 + C$, where $C$ stands for an arbitrary constant

Every function $x^2 + C$ has derivative $2x$ (for example $x^2 + 7$), so the indefinite integral is the whole family. The constant matters when a condition fixes it: if $F'(x) = 2x$ and $F(0) = 5$, then $F(x) = x^2 + 5$. A definite integral has no $+C$, because it cancels in $F(b) - F(a)$.

Taught in the fundamental theorem of calculus<!-- link: ../05-university-core/04-integrals/02-fundamental-theorem-of-calculus.md -->.

## Number bases

### Reading binary remainders from the top down

Wrong: dividing 13 by 2 again and again gives the remainders 1, 0, 1, 1, so $13 = 1011_2$

Right: read the remainders from the bottom up, so $13 = 1101_2$

The first remainder is the ones digit, so it goes on the right. Check by expanding: $1101_2 = 8 + 4 + 1 = 13$, while $1011_2 = 8 + 2 + 1 = 11$.

Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

### Numbering the places from 1 instead of 0

Wrong: $1101_2 = 2^4 + 2^3 + 2^1 = 26$

Right: $1101_2 = 2^3 + 2^2 + 2^0 = 13$

The rightmost place is $2^0 = 1$, so the exponent of each place is its position counted from $0$ at the right. A size check catches the slip: four bits hold at most $1111_2 = 15$, so 26 is too big.

Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).
