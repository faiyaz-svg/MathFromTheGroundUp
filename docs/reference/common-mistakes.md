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

### Not converting units in an estimate

Wrong: a car at 100 km/h covers about $100 \times 3 = 300$ m in 3 seconds

Right: it covers about 83 m, since $100\ \text{km/h} = \frac{100{,}000}{3600} \approx 27.8$ m/s and $27.8 \times 3 \approx 83$

The 100 is in kilometres per hour and the 3 is in seconds, so the product has no meaning until the units match. A sanity check on size catches it: 300 m in 3 seconds would be a speed of 360 km/h. Convert first, then estimate.

Taught in [estimation and sanity checks](../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md#worked-examples).

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

Taught in [absolute value equations and inequalities](../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md#edge-cases-and-common-mistakes),[negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#edge-cases-and-common-mistakes) and [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#definitions).

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

Taught in [estimation and sanity checks](../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md#worked-examples),[percents](../02-middle-school/02-ratios-rates-percents/03-percents.md) and [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).

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

Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#edge-cases-and-common-mistakes),[measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#edge-cases-and-common-mistakes) and [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#edge-cases-and-common-mistakes).

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

### Using n times 180 for the interior angle sum

Wrong: the interior angles of a hexagon add to $6 \times 180^\circ = 1080^\circ$

Right: they add to $(6 - 2) \times 180^\circ = 720^\circ$, so each angle of a regular hexagon is $120^\circ$

A polygon with $n$ sides splits into $n - 2$ triangles from one vertex, and each triangle contributes $180^\circ$.

Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#edge-cases-and-common-mistakes).

### Using the diameter in the circle area formula

Wrong: a circle of diameter 10 cm has area $\pi \times 10^2 = 100\pi\ \text{cm}^2$

Right: the radius is 5 cm, so the area is $25\pi \approx 78.5\ \text{cm}^2$

The formula $\pi r^2$ uses the radius. Halve the diameter first. Squaring the product, as in $(\pi r)^2$, is a related slip: at $r = 5$ it gives about 246.7, over three times too big.

Taught in [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md#edge-cases-and-common-mistakes).

### Using the slant height in a volume formula

Wrong: the volume of a cone uses the slant height as $h$

Right: the volume uses the perpendicular height, from the apex straight down to the base

A slanted path down a side is longer than the straight one, so the volume would come out too big. For a cone with $r = 3$ and slant height 5, the perpendicular height is 4, and $V = \frac{1}{3}\pi \cdot 3^2 \cdot 4 = 12\pi$.

Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#edge-cases-and-common-mistakes).

### Adding the squares when the hypotenuse is given

Wrong: a ladder 13 m long leans against a wall with its foot 5 m out, so it reaches $\sqrt{13^2 + 5^2} \approx 13.9$ m up

Right: it reaches $\sqrt{13^2 - 5^2} = 12$ m up

The theorem is $a^2 + b^2 = c^2$ with $c$ the hypotenuse. When the hypotenuse is known, subtract. A leg can never be longer than the hypotenuse, which rules out 13.9.

Taught in [the Pythagorean theorem](../02-middle-school/06-geometry/04-pythagorean-theorem.md#edge-cases-and-common-mistakes).

### Turning the wrong way under a rotation rule

Wrong: a $90^\circ$ counterclockwise turn about the origin sends $(x, y)$ to $(y, -x)$

Right: it sends $(x, y)$ to $(-y, x)$

Test on $(1, 0)$, which should end up at $(0, 1)$ after a quarter turn counterclockwise. The wrong rule sends it to $(0, -1)$, a clockwise turn.

Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#edge-cases-and-common-mistakes).

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

Taught in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#edge-cases-and-common-mistakes) and[radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md).

### Writing the square root of x squared as x

Wrong: $\sqrt{x^2} = x$

Right: $\sqrt{x^2} = \lvert x \rvert$

A square root is never negative, so it can't give back $x$ when $x$ is negative. With $x = -3$, the left side is $\sqrt{(-3)^2} = \sqrt{9} = 3$, which is $\lvert -3 \rvert$ and not $-3$. Watch for this step in any proof that takes the square root of both sides.

Taught in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#edge-cases-and-common-mistakes) and[radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md).

### Mixing up a square root with the solutions of a square

Wrong: $\sqrt{9} = \pm 3$, or $x^2 = 9$ means $x = 3$

Right: $\sqrt{9} = 3$, and $x^2 = 9$ means $x = 3$ or $x = -3$

The symbol $\sqrt{9}$ names one number, the non-negative one. The equation $x^2 = 9$ asks for every number whose square is $9$, and there are two of them. When you solve, write $x = \pm\sqrt{9} = \pm 3$.

Taught in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md) and [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md).

### Raising only part of a product to the outer power

Wrong: $(2x^3)^4 = 2x^{12}$

Right: $(2x^3)^4 = 2^4 x^{12} = 16x^{12}$

The outer exponent applies to every factor inside the brackets, the coefficient as well as the variable. Test with $x = 1$: the left side is $2^4 = 16$, but the wrong answer is 2.

Taught in [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md#worked-examples).

### Adding exponents in a sum of powers

Wrong: $2^3 + 2^4 = 2^7 = 128$, and $2 \times 10^3 + 3 \times 10^3 = 5 \times 10^6$

Right: $2^3 + 2^4 = 8 + 16 = 24$, and $2 \times 10^3 + 3 \times 10^3 = 5 \times 10^3$

Exponents add when powers are multiplied, not when they are added. In a sum of numbers in scientific notation with the same power of ten, add the coefficients and keep the power.

Taught in [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md#edge-cases-and-common-mistakes) and [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md#worked-examples).

### Counting zeros instead of places in scientific notation

Wrong: $93{,}000{,}000 = 9.3 \times 10^6$, because the number has six zeros

Right: $93{,}000{,}000 = 9.3 \times 10^7$

The exponent is the number of places the decimal point moves, here from after the last 0 to after the 9. Count the places, not the zeros. The check is to expand: $9.3 \times 10^7$ is 9.3 times ten million.

Taught in [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md#worked-examples).

### Using the caret for a power in Python

Wrong: `2 * 10^3` for 2000

Right: `2 * 10**3`, or the literal `2e3`

In Python, `^` is bitwise XOR and not a power. Because `*` ranks above `^`, the wrong line works out `(2 * 10) ^ 3`, which is 23. Excel and many calculators do use `^` for a power, so the habit carries over without warning.

Taught in [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md#edge-cases-and-common-mistakes).

### Taking the cube root of a negative number with a fractional power

Wrong: `(-8) ** (1/3)` to get $-2$

Right: `math.cbrt(-8)`, which gives `-2.0`

The fractional power of a negative float returns a complex number, about `1+1.732j`. The exponent `1/3` is also not exactly one third in floating point. `math.cbrt` (Python 3.11 and later) takes a real cube root directly.

Taught in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#in-code).

### Reading a rational exponent as a fraction of the power

Wrong: $8^{2/3} = \frac{8^2}{3} = \frac{64}{3}$

Right: $8^{2/3} = \left(\sqrt[3]{8}\right)^2 = 2^2 = 4$

In $a^{m/n}$ the denominator is the index of the root and the numerator is the power. Take the root first when the number is a perfect power, since it keeps the numbers small.

Taught in [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md#worked-examples).

### Averaging growth by dividing the total change

Wrong: a balance that grows from \$1,000 to \$1,331 in 3 years has grown by $\frac{33.1\%}{3} \approx 11.0\%$ a year

Right: the yearly growth factor is $\left(\frac{1331}{1000}\right)^{1/3} = 1.1$, so the growth is 10% a year

Growth compounds, so the yearly factors multiply and the right average is the root of the total factor. Check by compounding: $1000 \times 1.1^3 = 1331$, while $1000 \times 1.11^3 \approx 1367$.

Taught in [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md#worked-examples).

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

Taught in [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md#edge-cases-and-common-mistakes) and[equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#edge-cases-and-common-mistakes).

### Squaring a sum term by term

Wrong: $(a + b)^2 = a^2 + b^2$

Right: $(a + b)^2 = a^2 + 2ab + b^2$

Squaring means multiplying $(a + b)(a + b)$, and the two cross products $ab$ and $ba$ make the middle term. Test with $a = b = 1$: the left side is $2^2 = 4$, but $a^2 + b^2 = 2$. With numbers, $(3 + 4)^2 = 49$, while $3^2 + 4^2 = 25$.

Taught in [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md#edge-cases-and-common-mistakes),[exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#edge-cases-and-common-mistakes) and [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md).

### Cancelling terms instead of factors

Wrong: $\frac{x + 3}{x} = 3$, by crossing out the $x$ on top and the $x$ on the bottom

Right: $\frac{x + 3}{x} = \frac{x}{x} + \frac{3}{x} = 1 + \frac{3}{x}$, for $x \ne 0$

Cancelling divides the numerator and the denominator by the same number, so it works only on a factor of the whole numerator. Here $x$ is a term of the numerator, not a factor of it. Test with $x = 1$: $\frac{1 + 3}{1} = 4$, not $3$. By contrast, $\frac{3x}{x} = 3$ for $x \ne 0$, because $x$ is a factor of $3x$. The same rule holds for numbers: in $\frac{2}{3} + \frac{3}{5}$ the two 3s don't cancel, because a sum is not a product.

Taught in [multiplying and dividing fractions](../01-elementary/11-multiplying-and-dividing-fractions.md#edge-cases-and-common-mistakes) and [rational expressions](../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md).

### Subtracting only the first term in brackets

Wrong: $5 - (x + 2) = 5 - x + 2$

Right: $5 - (x + 2) = 5 - x - 2 = 3 - x$

The minus sign in front of the brackets multiplies every term inside by $-1$. Test with $x = 0$: the original is $5 - 2 = 3$, the right version gives $3 - 0 = 3$, and the wrong version gives $5 - 0 + 2 = 7$. A number in front of brackets has to reach every term too: $2(x + 3) = 2x + 6$, not $2x + 3$, and $3 \times (4 + 5) = 27$, not $3 \times 4 + 5 = 17$.

Taught in [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md#edge-cases-and-common-mistakes),[equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md) and [properties of operations](../01-elementary/04-properties-of-operations.md#edge-cases-and-common-mistakes).

### Distributing over a product

Wrong: $2(xy) = (2x)(2y)$

Right: $2(xy) = 2xy$

The distributive property spreads a multiplication over a sum, never over a product. A product is regrouped with the associative property, so the 2 multiplies only once. Test at $x = 3$ and $y = 5$: $2xy = 30$, while $(2x)(2y) = 60$.

Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#edge-cases-and-common-mistakes).

## Polynomials

### Stopping before a polynomial is factored completely

Wrong: $2x^4 - 32 = 2(x^2 - 4)(x^2 + 4)$

Right: $2x^4 - 32 = 2(x - 2)(x + 2)(x^2 + 4)$

The factor $x^2 - 4$ is a difference of squares, so it factors again. Factoring is finished when every factor is prime over the integers. The sum $x^2 + 4$ stays.

Taught in [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#worked-examples).

### Using the zero-product property when the right side is not zero

Wrong: $x(x - 3) = 10$ gives $x = 10$ or $x - 3 = 10$

Right: move 10 across to get $x^2 - 3x - 10 = 0$, so $(x - 5)(x + 2) = 0$ and $x = 5$ or $x = -2$

A product forces a factor to be zero only when the product is zero. Many pairs of numbers multiply to 10. Check: $5 \cdot 2 = 10$ and $(-2)(-5) = 10$.

Taught in [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#edge-cases-and-common-mistakes) and [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md#edge-cases-and-common-mistakes).

### Treating a sum of squares or cubes like a perfect power

Wrong: $x^2 + 9 = (x + 3)^2$, and $x^3 + 27 = (x + 3)^3$

Right: $(x + 3)^2 = x^2 + 6x + 9$, so $x^2 + 9$ is prime over the real numbers, and $x^3 + 27 = (x + 3)(x^2 - 3x + 9)$

The middle terms don't cancel in a sum of squares, and a sum of cubes has its own pattern. Expanding the claimed answer is the check.

Taught in [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#edge-cases-and-common-mistakes).

### Concluding that there is no zero because the signs match

Wrong: $f(x) = (x - 1)(x - 2)$ is positive at $x = 0$ and at $x = 3$, so it has no zero between them

Right: it has two zeros between them, at 1 and 2

A sign change guarantees an odd number of zeros between two points. Matching signs say only that the number of zeros between is even, which includes 2.

Taught in [polynomial functions and graphs](../03-high-school/04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#worked-examples).

## Quadratics and complex numbers

### Reading the vertex with the wrong sign

Wrong: the vertex of $2(x + 3)^2 - 8$ is $(3, -8)$

Right: it is $(-3, -8)$

The form is $a(x - h)^2 + k$, and $x + 3 = x - (-3)$, so $h = -3$. The vertex is where the bracket is zero.

Taught in [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#edge-cases-and-common-mistakes).

### Forgetting to multiply the subtracted square by the leading coefficient

Wrong: $2x^2 + 8x + 3 = 2(x + 2)^2 - 1$

Right: $2x^2 + 8x + 3 = 2(x + 2)^2 - 5$

Adding and subtracting 4 inside the bracket means subtracting $2 \cdot 4 = 8$ outside it. Expanding the answer is the check: at $x = 0$ the original is 3, the right form gives $8 - 5 = 3$, and the wrong form gives 7.

Taught in [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#edge-cases-and-common-mistakes).

### Computing the discriminant with the wrong sign

Wrong: for $x^2 - 3x - 5$, $D = 9 - 20 = -11$

Right: $D = (-3)^2 - 4(1)(-5) = 9 + 20 = 29$

When $c$ is negative, $-4ac$ is positive. Put the numbers in brackets before you square or multiply. A positive discriminant here means two real solutions, and $-11$ would have claimed there were none.

Taught in [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md#edge-cases-and-common-mistakes).

### Forgetting that i squared is minus 1 when multiplying

Wrong: $(2 + 3i)^2 = 4 + 12i + 9 = 13 + 12i$

Right: $(2 + 3i)^2 = 4 + 12i + 9i^2 = -5 + 12i$

The term $9i^2$ is $-9$, not $+9$. A check with the modulus: $\lvert 2 + 3i \rvert^2 = 13$ and $\lvert -5 + 12i \rvert = 13$, which agree, since the modulus of a square is the square of the modulus.

Taught in [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#edge-cases-and-common-mistakes).

### Using the product rule for roots with negative numbers

Wrong: $\sqrt{-4}\,\sqrt{-9} = \sqrt{36} = 6$

Right: $\sqrt{-4}\,\sqrt{-9} = (2i)(3i) = 6i^2 = -6$

The rule $\sqrt{a}\sqrt{b} = \sqrt{ab}$ needs $a, b \ge 0$. Write each root with $i$ first, then multiply.

Taught in [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#edge-cases-and-common-mistakes).

## Rational expressions and equations

### Calling a cancelled factor a vertical asymptote

Wrong: $f(x) = \frac{(x - 2)(x + 1)}{x - 2}$ has a vertical asymptote at $x = 2$

Right: it has a hole at $x = 2$, at height 3, and no vertical asymptote

Cancel first, then look at the denominator that is left. A zero of the reduced denominator is a vertical asymptote, and a cancelled factor leaves a hole.

Taught in [rational functions and asymptotes](../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md#edge-cases-and-common-mistakes).

### Averaging two speeds over equal distances

Wrong: driving 60 km/h out and 40 km/h back averages $\frac{60 + 40}{2} = 50$ km/h

Right: the average is $\frac{2(60)(40)}{60 + 40} = 48$ km/h

More time goes to the slow leg, so the slow speed counts for more. For a 240 km leg each way, the trip takes $4 + 6 = 10$ hours for 480 km, and $\frac{480}{10} = 48$.

Taught in [rational and radical equations](../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md#edge-cases-and-common-mistakes).

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

Taught in [polynomial and rational inequalities](../03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md#edge-cases-and-common-mistakes) and[inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md).

### Flipping an inequality because a negative number appears

Wrong: $3x < -12$, so $x > -4$

Right: $3x < -12$, so $x < -4$

Only multiplying or dividing both sides by a negative number reverses the symbol. Here you divide by 3, which is positive, so the symbol stays, and the $-12$ on the right changes nothing. Test $x = -5$: it satisfies $x < -4$, and $3(-5) = -15 < -12$ is true.

Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#edge-cases-and-common-mistakes).

### Dividing both sides by a variable that might be zero

Wrong: $x^2 = 3x$, and dividing by $x$ gives $x = 3$

Right: $x^2 - 3x = 0$, so $x(x - 3) = 0$, and $x = 0$ or $x = 3$

Dividing by $x$ is allowed only when $x \ne 0$, so it throws away the solution $x = 0$. Move every term to one side and factor instead. Both answers check: $0^2 = 3 \cdot 0$ and $3^2 = 3 \cdot 3$. The same slip turns $5x = 3x$ into $5 = 3$, which seems to say there is no solution, though $x = 0$ works.

Taught in [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#edge-cases-and-common-mistakes),[multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#dividing-by-an-expression-that-might-be-zero) and [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md).

### Keeping every solution after squaring both sides

Wrong: $\sqrt{x + 2} = x$ has the solutions $x = 2$ and $x = -1$

Right: only $x = 2$ is a solution

Squaring gives $x + 2 = x^2$, so $x^2 - x - 2 = 0$ and $(x - 2)(x + 1) = 0$. Squaring can add solutions, because $a = b$ and $a = -b$ both turn into $a^2 = b^2$, so check each candidate in the original equation. For $x = -1$ the left side is $\sqrt{1} = 1$ and the right side is $-1$, so $-1$ is an extraneous root.

Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#edge-cases-and-common-mistakes) and[rational and radical equations](../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md).

### Multiplying an inequality by an expression of unknown sign

Wrong: $\frac{1}{x} < 2$, so $1 < 2x$, so $x > \frac{1}{2}$

Right: $\frac{1}{x} < 2$ exactly when $x < 0$ or $x > \frac{1}{2}$

Multiplying by $x$ keeps the order only when $x > 0$. For $x < 0$ the order flips and gives $1 > 2x$, which every negative $x$ satisfies. Test $x = -1$: $\frac{1}{-1} = -1 < 2$, so it is a solution the wrong method lost. Split into cases by sign, or move every term to one side and use a sign chart.

Taught in [polynomial and rational inequalities](../03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md).

## Sets, intervals and absolute value

### Writing an element as a subset

Wrong: $2 \subseteq \{1, 2, 3\}$

Right: $2 \in \{1, 2, 3\}$, and $\{2\} \subseteq \{1, 2, 3\}$

The symbol $\in$ connects an element to a set, and $\subseteq$ connects two sets. The number 2 is not a set, so $2 \subseteq \{1, 2, 3\}$ is not even a statement.

Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#edge-cases-and-common-mistakes).

### Using a union for "and"

Wrong: $x > 1$ and $x < 3$ is $(1, \infty) \cup (-\infty, 3)$

Right: it is $(1, 3)$

"And" means intersection, so only the numbers in both sets count. The union of the two rays is every real number, since each number is in at least one of them. Test $x = 10$: it is not less than 3.

Taught in [compound inequalities and interval notation](../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md#edge-cases-and-common-mistakes).

### Splitting an absolute value equation before isolating it

Wrong: $\lvert x - 1 \rvert + 3 = 7$ gives $x - 1 + 3 = \pm 7$

Right: isolate first, $\lvert x - 1 \rvert = 4$, so $x - 1 = 4$ or $x - 1 = -4$, and $x = 5$ or $x = -3$

The $\pm$ applies to the whole absolute value, so the bars have to stand alone on one side before you split. Check: $\lvert 5 - 1 \rvert + 3 = 7$ and $\lvert -3 - 1 \rvert + 3 = 7$.

Taught in [absolute value equations and inequalities](../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md#edge-cases-and-common-mistakes).

## Lines and systems of equations

### Plotting the coordinates in the wrong order

Wrong: plot $(2, 5)$ by going up 2 and across 5

Right: go across 2, then up 5

The first number of an ordered pair is the horizontal position. The pairs $(2, 5)$ and $(5, 2)$ are different points.

Taught in [the coordinate plane](../02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md#edge-cases-and-common-mistakes).

### Subtracting the coordinates in a different order on top and bottom

Wrong: the slope through $(1, 2)$ and $(4, 8)$ is $\frac{8 - 2}{1 - 4} = -2$

Right: $\frac{8 - 2}{4 - 1} = 2$

Whichever point comes first on the top has to come first on the bottom. The sign is a check: the line rises from left to right, so the slope is positive.

Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#worked-examples).

### Reading the slope and intercept off standard form

Wrong: $2x + 3y = 12$ has slope $\frac{2}{3}$ and $y$-intercept 12

Right: it has slope $-\frac{2}{3}$ and $y$-intercept 4

Solve for $y$ first: $y = 4 - \frac{2}{3}x$. In general, $Ax + By = C$ has slope $-\frac{A}{B}$ and $y$-intercept $\frac{C}{B}$.

Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#edge-cases-and-common-mistakes) and [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md#edge-cases-and-common-mistakes).

### Mixing up zero slope and undefined slope

Wrong: a vertical line has slope 0

Right: a horizontal line has slope 0 and the equation $y = c$; a vertical line has no slope (the run is 0) and the equation $x = c$

Between $(3, 1)$ and $(3, 7)$ the slope would be $\frac{6}{0}$, which is undefined. A vertical line is not the graph of a function of $x$.

Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#edge-cases-and-common-mistakes) and [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md#edge-cases-and-common-mistakes).

### Using the sign of the point in point-slope form

Wrong: the line through $(-2, 5)$ with slope $m$ is $y - 5 = m(x - 2)$

Right: $y - 5 = m(x + 2)$

The form is $y - y_1 = m(x - x_1)$, and $x - (-2) = x + 2$. Check that the point satisfies the equation: at $x = -2$ the right side is 0, so $y = 5$.

Taught in [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md#edge-cases-and-common-mistakes).

### Forgetting to flip and negate for a perpendicular slope

Wrong: a line perpendicular to one of slope $\frac{3}{4}$ has slope $\frac{4}{3}$ or $-\frac{3}{4}$

Right: its slope is $-\frac{4}{3}$

The slopes of perpendicular lines multiply to $-1$, so take the reciprocal and change the sign. Check: $\frac{3}{4} \cdot \left(-\frac{4}{3}\right) = -1$.

Taught in [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md#edge-cases-and-common-mistakes).

### Reading an always-true result in a system as the solution zero

Wrong: elimination leaves $0 = 0$, so the solution is $(0, 0)$

Right: the two equations describe the same line, so there are infinitely many solutions; a false result such as $0 = 5$ means no solution

The result $0 = 0$ says that the equations agree everywhere. It doesn't give values for $x$ and $y$. For example, $2x + 3y = 12$ and $4x + 6y = 24$ are one line.

Taught in [systems of linear equations](../02-middle-school/05-linear-relationships-and-functions/04-systems-of-linear-equations.md#worked-examples) and [systems of linear equations](../03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md#edge-cases-and-common-mistakes).

### Checking a solution in only one equation

Wrong: $(5, 2)$ solves $x + y = 7$ and $x - y = 1$, because $5 + 2 = 7$

Right: $5 - 2 = 3$, not 1, so $(5, 2)$ fails the second equation; the solution is $(4, 3)$

A solution of a system has to satisfy every equation. A point that satisfies one equation lies on one line only.

Taught in [systems of linear equations](../02-middle-school/05-linear-relationships-and-functions/04-systems-of-linear-equations.md#edge-cases-and-common-mistakes).

### Shading by the look of the inequality symbol

Wrong: $-2y < 6$ is shaded below the line, because the symbol is $<$

Right: dividing by $-2$ reverses the symbol, giving $y > -3$, so the region above the line is shaded

Don't trust the symbol before the inequality is solved for $y$. A test point settles it: $(0, 0)$ gives $0 < 6$, which is true, and $(0, 0)$ is above the line $y = -3$.

Taught in [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#worked-examples).

## Functions and graphs

### Reading the inverse function as a reciprocal

Wrong: $f^{-1}(x) = \frac{1}{f(x)}$

Right: $f^{-1}$ undoes $f$, so $f^{-1}(y) = x$ exactly when $f(x) = y$

For $f(x) = 2x$ the inverse is $f^{-1}(x) = \frac{x}{2}$, so $f^{-1}(4) = 2$, while $\frac{1}{f(4)} = \frac{1}{8}$. The notation invites the mix-up, because $\sin^2 x$ means $(\sin x)^2$ but $\sin^{-1} x$ means the inverse function $\arcsin x$. When you mean the reciprocal, write $\frac{1}{f(x)}$ or $(f(x))^{-1}$.

Taught in [right triangle trigonometry](../03-high-school/09-trigonometry/01-right-triangle-trigonometry.md#edge-cases-and-common-mistakes) and[composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md).

### Adding h outside the function

Wrong: $f(x + h) = f(x) + h$

Right: replace every $x$ in the rule with $(x + h)$. For $f(x) = x^2$, that gives $f(x + h) = (x + h)^2 = x^2 + 2xh + h^2$.

Test with $x = 3$ and $h = 1$: $f(4) = 16$, while $f(3) + 1 = 10$. The input has changed, so the whole rule applies to the new input. This substitution is the first step of every derivative worked from the definition.

Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#edge-cases-and-common-mistakes),[what is a function](../03-high-school/03-functions/01-what-is-a-function.md) and the derivative definition<!-- link: ../05-university-core/02-derivatives/01-the-derivative-definition.md -->.

### Shifting a graph the wrong way

Wrong: the graph of $y = (x - 2)^2$ is the graph of $y = x^2$ moved 2 units left

Right: it is moved 2 units right

The new graph reaches each height when $x - 2$ equals the old input, which happens 2 units further right. The lowest point of $y = (x - 2)^2$ is at $x = 2$, where $x - 2 = 0$. Subtracting inside the function moves the graph right; subtracting outside, as in $y = x^2 - 2$, moves it down.

Taught in [transformations of functions](../03-high-school/03-functions/04-transformations-of-functions.md).

### Taking the range from the arrow in the signature

Wrong: $f \colon \mathbb{R} \to \mathbb{R}$ with $f(x) = x^2$ has range $\mathbb{R}$

Right: the range is $[0, \infty)$

The set after the arrow is the codomain, the set the outputs are allowed to land in. The range is the set of outputs that actually occur, and no square is negative.

Taught in [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#edge-cases-and-common-mistakes).

### Treating a cancelled formula as the same function

Wrong: $f(x) = \frac{x^2 - 4}{x - 2}$ is the same function as $g(x) = x + 2$

Right: they agree for $x \ne 2$, but $f(2)$ is undefined

Two functions are equal only when they have the same domain and the same outputs. Cancelling the factor $x - 2$ is valid only for $x \ne 2$, so the domain of $f$ stays without 2.

Taught in [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#edge-cases-and-common-mistakes).

### Rounding a negative number toward zero for the floor function

Wrong: $\lfloor -3.7 \rfloor = -3$

Right: $\lfloor -3.7 \rfloor = -4$

The floor is the greatest integer that is less than or equal to the number, and $-4 < -3.7 < -3$. Dropping the decimal part gives the ceiling for a negative number. Python's `//` floors too, so `-7 // 2` is `-4`.

Taught in [piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md#edge-cases-and-common-mistakes).

### Taxing all income at the top bracket rate

Wrong: with a 10% rate up to \$50,000 and 20% above, an income of \$60,000 pays $0.20 \times 60{,}000 = \$12{,}000$

Right: it pays $0.10 \times 50{,}000 + 0.20 \times 10{,}000 = \$7{,}000$

A marginal rate applies only to the income above its bracket limit. The average rate, $\frac{7000}{60000} \approx 11.7\%$, is lower than the top marginal rate. The brackets here are made up for practice.

Taught in [piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md#edge-cases-and-common-mistakes).

### Stretching when the input is multiplied

Wrong: the graph of $f(2x)$ is the graph of $f(x)$ stretched horizontally by 2

Right: it is compressed horizontally by a factor of 2

The graph of $f(2x)$ reaches each height at half the old input, because the doubled input gets there twice as fast. In the same way, $\lvert 2x - 6 \rvert$ is shifted 3 units right, not 6, since $\lvert 2x - 6 \rvert = 2\lvert x - 3 \rvert$. Factor out the coefficient of $x$ before you read a shift.

Taught in [transformations of functions](../03-high-school/03-functions/04-transformations-of-functions.md#edge-cases-and-common-mistakes).

### Composing functions in the wrong order

Wrong: $f \circ g = g \circ f$

Right: in general the two compositions differ

Take $f(x) = x + 1$ and $g(x) = 2x$. Then $f(g(2)) = 5$, while $g(f(2)) = 6$. The expression $(f \circ g)(x)$ applies $g$ first.

Taught in [composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md#edge-cases-and-common-mistakes).

### Undoing steps in the order they were applied

Wrong: the inverse of "multiply by 2, then add 3" is $y \mapsto \frac{y}{2} - 3$

Right: undo the last step first, $y \mapsto \frac{y - 3}{2}$

Check by composing: $f(1) = 5$, and the right inverse gives $\frac{5 - 3}{2} = 1$, while the wrong one gives $\frac{5}{2} - 3 = -0.5$.

Taught in [composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md#edge-cases-and-common-mistakes).

## Exponential growth and decay

### Adding percent growth over several periods

Wrong: 8% growth for 10 years is 80% growth in total

Right: it is $1.08^{10} \approx 2.159$ times the starting amount, a growth of about 115.9%

Each year's growth is a percent of a bigger amount, so the yearly factors multiply. Adding the percents is the simple-interest answer.

Taught in [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#edge-cases-and-common-mistakes).

### Mixing a monthly rate with years

Wrong: a balance growing 2% a month for $t$ years is $A_0 \cdot 1.02^t$

Right: it is $A_0 \cdot 1.02^{12t}$

The exponent has to count periods, and the rate is per month, so $t$ years is $12t$ months. The yearly factor is $1.02^{12} \approx 1.268$, not 1.02.

Taught in [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#edge-cases-and-common-mistakes).

## Logarithms

### Splitting a logarithm over a sum

Wrong: $\log(a + b) = \log a + \log b$

Right: $\log(ab) = \log a + \log b$, and $\log(a + b)$ doesn't simplify

A logarithm turns multiplication into addition, because exponents add when you multiply powers of the same base. Test with base-10 logarithms: $\log(10 + 10) = \log 20 \approx 1.301$, while $\log 10 + \log 10 = 2$, which is $\log 100$.

Taught in [exponential and logarithmic equations](../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md#edge-cases-and-common-mistakes) and[logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md).

### Treating a quotient of logarithms as one logarithm

Wrong: $\frac{\log 8}{\log 2} = \log 4$

Right: $\frac{\log 8}{\log 2} = \log_2 8 = 3$

A quotient of two logarithms is the change-of-base formula, $\log_b x = \frac{\log x}{\log b}$. The rule $\log \frac{x}{y} = \log x - \log y$ is about the logarithm of a quotient, which is a different thing. Check: $\log 4 \approx 0.602$ in base 10, but $\frac{\log 8}{\log 2} = 3$ in every base, since $2^3 = 8$.

Taught in [logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md).

### Taking the logarithm of zero or a negative number

Wrong: $\log_2(-8) = -3$

Right: $\log_2(-8)$ is undefined in the real numbers

Every power of a positive base is positive, so no exponent gives 0 or a negative number. This matters when you solve: any answer that makes the argument of a logarithm zero or negative is rejected.

Taught in [logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md#edge-cases-and-common-mistakes).

### Swapping the base and the result

Wrong: $\log_5 125 = 3$ means $3^5 = 125$

Right: it means $5^3 = 125$

The base of the logarithm stays the base of the power: $\log_b x = y$ means $b^y = x$. Check: $3^5 = 243$.

Taught in [logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md#edge-cases-and-common-mistakes).

### Assuming the logarithm function in a program is base 10

Wrong: `math.log(100)` gives 2

Right: it gives about 4.605, the natural logarithm; `math.log10(100)` gives 2.0

Most languages use `log` for the natural logarithm. Use `log10` or `log2` for those bases, or divide by the logarithm of the base.

Taught in [logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md#edge-cases-and-common-mistakes).

### Taking logarithms of each term in an equation with a sum

Wrong: $2^x + 3 = 11$ gives $x\log 2 + \log 3 = \log 11$

Right: isolate the power first, $2^x = 8$, and then $x = \log_2 8 = 3$

A logarithm of a sum has no rule, so the term-by-term step is not valid. Isolate the exponential, then take the logarithm of both sides.

Taught in [exponential and logarithmic equations](../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md#edge-cases-and-common-mistakes).

### Rounding a logarithm before dividing

Wrong: rounding $\ln 1.003333 \approx 0.003$ gives a doubling time of $\frac{\ln 2}{12 \cdot 0.003} \approx 19.25$ years

Right: keep six or more digits, which gives $\frac{\ln 2}{12 \ln 1.003333} \approx 17.36$ years

A small number in a denominator magnifies its rounding error. Keep full precision through the calculation and round the final answer.

Taught in [exponential and logarithmic equations](../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md#edge-cases-and-common-mistakes).

### Keeping a solution that makes a logarithm undefined

Wrong: $\log_2 x + \log_2(x - 2) = 3$ gives $x(x - 2) = 8$, so $x = 4$ or $x = -2$

Right: only $x = 4$ works

Combining the logarithms enlarged the domain: the original equation needs $x > 2$. For $x = -2$, the term $\log_2(-2)$ is undefined. Check every candidate in the original equation.

Taught in [exponential and logarithmic equations](../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md#worked-examples).

## Trigonometry

### Leaving the calculator in the wrong angle mode

Wrong: `sin(30)` gives $-0.988$, so $\sin 30^\circ = -0.988$

Right: in degree mode `sin(30)` gives 0.5

A calculator or a program reads the number as degrees or radians according to its mode, and Python's `math.sin` always uses radians. Check against a value you know: $\sin 30^\circ = 0.5$.

Taught in [right triangle trigonometry](../03-high-school/09-trigonometry/01-right-triangle-trigonometry.md#edge-cases-and-common-mistakes).

### Using degrees in an arc length formula

Wrong: an arc of $60^\circ$ on a circle of radius 3 has length $3 \times 60 = 180$

Right: convert to radians first, $60^\circ = \frac{\pi}{3}$, so the length is $3 \cdot \frac{\pi}{3} = \pi \approx 3.14$

The formulas $s = r\theta$ and $A = \frac{1}{2}r^2\theta$ need $\theta$ in radians. In degrees, the arc is the fraction $\frac{60}{360}$ of the circumference $2\pi \cdot 3$, which is also $\pi$.

Taught in [radians and the unit circle](../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md#edge-cases-and-common-mistakes).

### Taking the calculator's inverse as the angle in every quadrant

Wrong: $\tan\theta = \frac{3}{4}$ with $\theta$ in quadrant III, so $\theta = \tan^{-1}\frac{3}{4} \approx 36.87^\circ$

Right: $\theta = 180^\circ + 36.87^\circ = 216.87^\circ$

An inverse function returns one angle, the reference angle or principal value. Look at the quadrant, then add or subtract to land there.

Taught in [radians and the unit circle](../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md#edge-cases-and-common-mistakes).

### Reading the phase shift before factoring out the coefficient

Wrong: the graph of $y = \sin(2x - \pi)$ is shifted $\pi$ units right

Right: it is shifted $\frac{\pi}{2}$ units right

Factor out the coefficient of $x$ first: $\sin(2x - \pi) = \sin\left(2\left(x - \frac{\pi}{2}\right)\right)$.

Taught in [graphs of trig functions](../03-high-school/09-trigonometry/03-graphs-of-trig-functions.md#edge-cases-and-common-mistakes).

### Distributing a trig function over a sum

Wrong: $\sin(a + b) = \sin a + \sin b$

Right: $\sin(a + b) = \sin a\cos b + \cos a\sin b$

Test with $a = b = 30^\circ$: $\sin 60^\circ \approx 0.866$, while $\sin 30^\circ + \sin 30^\circ = 1$.

Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#edge-cases-and-common-mistakes).

### Assuming the inverse sine undoes the sine everywhere

Wrong: $\arcsin(\sin x) = x$ for every $x$

Right: it holds only for $x$ from $-\frac{\pi}{2}$ to $\frac{\pi}{2}$; for example $\arcsin(\sin\pi) = 0$, not $\pi$

The inverse is defined on a restricted domain so that it is one-to-one, and it returns an angle in that range.

Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#edge-cases-and-common-mistakes).

### Taking only the acute angle in the ambiguous case

Wrong: $\sin B = 0.8$, so $B = 53.13^\circ$ and there is one triangle

Right: also test $B = 180^\circ - 53.13^\circ = 126.87^\circ$, which gives a second triangle if the angles still sum to less than $180^\circ$

Sine takes the same value at an angle and at its supplement. The data (two sides and a non-included angle) can give no triangle, one or two.

Taught in [law of sines and law of cosines](../03-high-school/09-trigonometry/05-law-of-sines-and-cosines.md#edge-cases-and-common-mistakes).

## Logic and proofs

### Confusing a statement with its converse

Wrong: "if $n$ is divisible by 4, then $n$ is even" is true, so "if $n$ is even, then $n$ is divisible by 4" is true

Right: the converse is a different statement and needs its own proof. Here it is false, since $6$ is even but not divisible by $4$.

The converse of "if P, then Q" is "if Q, then P", and knowing one tells you nothing about the other. Only the contrapositive, "if not Q, then not P", is equivalent to the original.

Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#edge-cases-and-common-mistakes) and[conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md).

### Using the inverse in place of the contrapositive

Wrong: "if $x > 2$, then $x^2 > 4$" is equivalent to "if $x \le 2$, then $x^2 \le 4$"

Right: it is equivalent to its contrapositive, "if $x^2 \le 4$, then $x \le 2$"

The statement in the wrong line is the inverse, and it fails at $x = -3$, where $x \le 2$ but $(-3)^2 = 9 > 4$. The contrapositive negates both parts and swaps them; the inverse negates them without swapping. A proof by contrapositive has to start from "not Q".

Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md) and [contrapositive proof](../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md).

### Negating a statement about every case

Wrong: the negation of "every student passed" is "no student passed"

Right: the negation is "some student did not pass"

A statement about every case is false as soon as one case fails, so its negation says that a failing case exists. In symbols, $\neg(\forall x\ P(x)) \equiv \exists x\ \neg P(x)$, and $\neg(\exists x\ P(x)) \equiv \forall x\ \neg P(x)$. The sentence "no student passed" claims much more than the negation does, and it is usually false as well.

Taught in [negation and translating English](../04-proofs-and-logic/02-logic-and-sets/05-negation-and-translating-english.md).

### Proving a general claim with examples

Wrong: $n^2 + n + 41$ is prime for $n = 0, 1, 2, 3, 4$, so it is prime for every natural number $n$

Right: examples can't prove a claim about every $n$. This claim is false: for $n = 40$, $40^2 + 40 + 41 = 1681 = 41^2$.

The formula gives a prime for every $n$ from $0$ to $39$ and still fails at $40$. To prove a claim for every $n$, take an arbitrary $n$ and argue from the definitions. Examples do settle the opposite question, since one counterexample disproves a claim about every case. The same holds for algebra: $x^2 + 2$ and $3x$ agree at $x = 1$ and $x = 2$, but they are not equivalent expressions.

Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#edge-cases-and-common-mistakes),[properties of operations](../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division), [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#why-isnt-checking-a-few-values-enough), common proof mistakes<!-- link: ../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md --> and [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md).

### Assuming what you want to prove

Wrong: to prove $a^2 + b^2 \ge 2ab$, start from it, subtract $2ab$ to get $a^2 - 2ab + b^2 \ge 0$, reach $(a - b)^2 \ge 0$, and stop because that is true

Right: start from a known fact, $(a - b)^2 \ge 0$, expand it to $a^2 - 2ab + b^2 \ge 0$, and add $2ab$ to both sides to reach $a^2 + b^2 \ge 2ab$

Reaching a true statement from the claim proves nothing, because a false claim can lead to a true one: $-1 = 1$ is false, but squaring both sides gives $1 = 1$. Working backward is fine as scratch work for finding the steps. The written proof has to run forward from known facts, with each step following from the ones before it.

Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#why-not-do-the-same-to-both-sides) and[scratch work and proof strategies](../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md).

### Skipping the base case in induction

Wrong: every natural number $n$ satisfies $n > n + 1$, because if $k > k + 1$, then adding 1 to both sides gives $k + 1 > k + 2$

Right: that inductive step is valid, but the claim is false, because the base case fails: $0 > 1$ is false

Induction needs both parts. The inductive step only says that each case passes its truth on to the next one, and the base case is what starts the chain. Without it, the argument above would prove a statement that is false for every $n$.

Taught in mathematical induction<!-- link: ../04-proofs-and-logic/05-induction/01-mathematical-induction.md -->.

## Proof and logic in geometry

### Reading sizes and angles off a drawing

Wrong: the angles in a diagram look equal, so write "$\angle A = \angle B$" as a step

Right: use only facts that are marked, given or already proved

A drawing is a sketch, and it can mislead. In a proof, a statement holds because of a reason, such as a given, a definition, a postulate or an earlier theorem.

Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#edge-cases-and-common-mistakes).

### Citing SSA as a congruence test

Wrong: two sides and a non-included angle are equal, so the triangles are congruent

Right: use SSS, SAS, ASA, AAS or HL; SSA is not a test

With two sides and a non-included angle, the third vertex can sit at two different places, where a circle meets a ray twice. The right-triangle case, HL, is the exception.

Taught in [congruence and triangle proofs](../03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md#edge-cases-and-common-mistakes).

### Using CPCTC before the triangles are proved congruent

Wrong: use "corresponding parts are equal" as a step to prove that the triangles are congruent

Right: first prove the congruence by SSS, SAS, ASA, AAS or HL, and only then use CPCTC for the parts

CPCTC is the definition of congruent triangles read in the other direction. Using it before the congruence is established is circular.

Taught in [congruence and triangle proofs](../03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md#edge-cases-and-common-mistakes).

### Mixing part-to-part and part-to-whole in a similarity proportion

Wrong: for a line $DE$ parallel to $BC$ in $\triangle ABC$, $\frac{AD}{DB} = \frac{DE}{BC}$

Right: $\frac{AD}{AB} = \frac{DE}{BC}$, or $\frac{AD}{DB} = \frac{AE}{EC}$

The left side compares the piece $AD$ with the other piece $DB$, while the right side compares $DE$ with the whole side $BC$. Compare a piece with its whole on both sides, or a piece with a piece on both sides.

Taught in [similarity](../03-high-school/08-geometry-and-proof/03-similarity.md#edge-cases-and-common-mistakes).

### Concluding similarity from two matching ratios

Wrong: two pairs of sides are in the ratio $1:2$, so the triangles are similar

Right: all three pairs must match (SSS), or two pairs must match with the included angles equal (SAS)

Two proportional sides leave the third side free. A $3, 4, 5$ triangle and a $6, 8, 9$ triangle have two ratios equal to 2, and they are not similar.

Taught in [similarity](../03-high-school/08-geometry-and-proof/03-similarity.md#edge-cases-and-common-mistakes).

### Reading the centre of a circle with the wrong signs

Wrong: the circle $(x + 2)^2 + (y - 3)^2 = 16$ has centre $(2, -3)$ and radius 16

Right: it has centre $(-2, 3)$ and radius 4

The equation has the form $(x - h)^2 + (y - k)^2 = r^2$, and $x + 2 = x - (-2)$. The right side is $r^2$, so the radius is the square root.

Taught in [coordinate geometry and circles](../03-high-school/08-geometry-and-proof/04-coordinate-geometry-and-circles.md#edge-cases-and-common-mistakes).

## Statistics and data

### Averaging grade components without weights

Wrong: components worth 25%, 25%, 40% and 10% with marks 88, 71, 62 and 95 average $\frac{88 + 71 + 62 + 95}{4} = 79$

Right: the weighted mean is $0.25(88) + 0.25(71) + 0.40(62) + 0.10(95) = 74.05$

Components that count differently need weights. The plain mean treats the 10% component like the 40% one.

Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#edge-cases-and-common-mistakes).

### Taking the median without sorting

Wrong: the median of 12, 3, 10, 8 is $\frac{3 + 10}{2} = 6.5$

Right: sort first, 3, 8, 10, 12, and the median is $\frac{8 + 10}{2} = 9$

The median is the middle of the sorted list. Taking the two values in the middle of the list as given gives a number that depends on how the data happened to be written.

Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#edge-cases-and-common-mistakes).

### Treating the sums of two dice as equally likely

Wrong: the sums 2 to 12 are 11 outcomes, so each has probability $\frac{1}{11}$

Right: the 36 equally likely pairs give a sum of 7 six ways and a sum of 2 one way, so $P(7) = \frac{1}{6}$ and $P(2) = \frac{1}{36}$

Equally likely outcomes are the pairs, not the sums. Count the cells of the 6 by 6 table.

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#worked-examples).

### Adding probabilities for "at least one"

Wrong: the chance of at least one six in 4 rolls is $4 \times \frac{1}{6} = \frac{4}{6}$

Right: it is $1 - \left(\frac{5}{6}\right)^4 = \frac{671}{1296} \approx 0.518$

Adding counts the cases with two or more sixes more than once. Take the complement instead: the chance of no six at all, subtracted from 1.

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#worked-examples).

### Treating draws without replacement as independent

Wrong: the chance of two reds from a bag of 2 red and 3 blue marbles is $\left(\frac{2}{5}\right)^2 = \frac{4}{25}$

Right: after one red is drawn, 1 red is left among 4, so the chance is $\frac{2}{5} \cdot \frac{1}{4} = \frac{2}{20} = \frac{1}{10}$

Removing a marble changes the next draw, so the draws are not independent and the probabilities can't be squared.

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#edge-cases-and-common-mistakes).

### Believing a streak makes the opposite result due

Wrong: after five heads in a row, tails is more likely on the next flip

Right: the next flip is still heads with probability $\frac{1}{2}$

The flips are independent, so the coin has no memory. Over many flips the proportion of heads settles toward $\frac{1}{2}$ because the early streak gets diluted, not because later flips compensate.

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#edge-cases-and-common-mistakes).

### Reading association as causation

Wrong: towns with more libraries have more car accidents, so libraries cause accidents

Right: look for a confounding variable; here a larger population drives both counts

Two variables can move together because a third variable affects both. A scatter plot shows association, and a study design is needed to show causation.

Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#edge-cases-and-common-mistakes).

### Extrapolating a line far beyond the data

Wrong: a fitted line predicts 147 out of 100 on a test after 20 hours of study

Right: don't use the line far outside the hours in the data

The line describes the range the data covers. Outside it the relationship can bend, level off or hit a limit, and a score above the maximum is the clue.

Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#edge-cases-and-common-mistakes).

### Mixing up row and column percents in a two-way table

Wrong: 30% of computer science students use Linux, so 30% of Linux users study computer science

Right: the two percents have different wholes: one is a share of a row, the other a share of a column

Ask "percent of what?" before reading a table. Comparing counts across groups of different sizes has the same problem, which is why row or column relative frequencies are used.

Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#edge-cases-and-common-mistakes).

## Counting and probability

### Multiplying probabilities of events that are not independent

Wrong: $P(A \cap B) = P(A)\,P(B)$ for every pair of events

Right: $P(A \cap B) = P(A)\,P(B \mid A)$ always, and $P(A \cap B) = P(A)\,P(B)$ only when $A$ and $B$ are independent

Roll one die, and let $A$ be "even" and $B$ be "at least 4". Then $A \cap B = \{4, 6\}$, so $P(A \cap B) = \frac{2}{6} = \frac{1}{3}$, while $P(A)\,P(B) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$. Knowing the roll is even makes "at least 4" more likely ($\frac{2}{3}$ instead of $\frac{1}{2}$), so the events are not independent.

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#edge-cases-and-common-mistakes) andconditional probability and Bayes' theorem<!-- link: ../05-university-core/07-probability/02-conditional-probability-and-bayes.md -->.

### Swapping the two sides of a conditional probability

Wrong: $P(A \mid B) = P(B \mid A)$

Right: $P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$, which is Bayes' theorem, and the two sides are usually different

Draw one card from a standard deck. The probability that it is a king, given that it is a face card, is $\frac{4}{12} = \frac{1}{3}$; the probability that it is a face card, given that it is a king, is $1$. The same mistake misleads people about medical tests: a test that catches most sick people can still give mostly false alarms when the disease is rare.

Taught in conditional probability and Bayes' theorem<!-- link: ../05-university-core/07-probability/02-conditional-probability-and-bayes.md -->.

### Counting ordered choices when order doesn't matter

Wrong: the number of 2-person committees you can form from 5 people is $5 \times 4 = 20$

Right: it is $\binom{5}{2} = \frac{5 \times 4}{2} = 10$

The count $5 \times 4$ lists each committee twice, once as (Ana, Ben) and once as (Ben, Ana). Ask whether swapping two choices gives a different outcome. If it does, as with choosing a president and a vice-president, order matters and $20$ is right; if not, divide out the orderings.

Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md).

### Counting the integers in a range off by one

Wrong: there are $10 - 3 = 7$ integers from 3 to 10, inclusive

Right: there are $10 - 3 + 1 = 8$

Subtracting counts the gaps between the numbers, and there is one more number than there are gaps, just as a fence with 7 gaps needs 8 posts. In general there are $b - a + 1$ integers from $a$ to $b$, inclusive. Python's `range(3, 11)` has 8 elements because it leaves out its upper end.

Taught in counting rules<!-- link: ../06-cs-math/03-counting-and-discrete-probability/01-counting-rules.md -->.

### Counting a case twice in an "at least one" count

Wrong: a committee of 3 from 6 people must include Ana or Ben, so choose one of them (2 ways) and then 2 others from the remaining 5, giving $2 \cdot \binom{5}{2} = 20$

Right: $\binom{6}{3} - \binom{4}{3} = 20 - 4 = 16$

Committees containing both Ana and Ben are counted twice in the first method, once for each way of calling one of them "first". The complement is cleaner: all committees, minus those with neither.

Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md#edge-cases-and-common-mistakes).

### Writing zero factorial as zero

Wrong: $0! = 0$

Right: $0! = 1$

The recurrence $n! = n \cdot (n-1)!$ gives $1! = 1 \cdot 0!$, so $0!$ must be 1. It also matches the count: there is one way to arrange nothing. In the same way $\binom{n}{0} = 1$.

Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md#edge-cases-and-common-mistakes).

## Sequences and series

### Trusting a pattern from a few terms

Wrong: points on a circle joined by chords cut it into $1, 2, 4, 8, 16$ regions, so six points give 32

Right: six points give 31 regions

A formula that fits the first five cases can fail on the sixth. A guessed pattern needs a proof, and the proof is usually induction.

Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#edge-cases-and-common-mistakes).

### Off-by-one errors in the index of a term

Wrong: the tenth term of a list that starts at index 0 is $a_{10}$

Right: it is $a_9$, because $a_{10}$ is the eleventh term

Decide the starting index before you write a formula, and check the formula on the first term. A list of 10 terms starting at index 0 ends at $a_9$.

Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#edge-cases-and-common-mistakes).

### Counting the terms of a sum as the upper bound minus the lower

Wrong: $\sum_{k=3}^{7} 4$ has $7 - 3 = 4$ terms, so it equals 16

Right: it has $7 - 3 + 1 = 5$ terms, so it equals 20

The sum from $m$ to $n$ has $n - m + 1$ terms. The same slip puts the wrong exponent in the geometric formula: $\sum_{k=0}^{9} 2^k$ has 10 terms, so it is $\frac{1 - 2^{10}}{1 - 2} = 1023$, not 511.

Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#edge-cases-and-common-mistakes).

### Using the formula for the first n whole numbers from a different start

Wrong: $\sum_{k=5}^{20} k = \frac{20 \cdot 21}{2} = 210$

Right: $210 - \sum_{k=1}^{4} k = 210 - 10 = 200$

The formula $\frac{n(n+1)}{2}$ assumes the sum starts at 1. Subtract the part you don't want, and check by the average rule: 16 terms with ends 5 and 20 give $16 \cdot \frac{25}{2} = 200$.

Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#edge-cases-and-common-mistakes).

### Applying the infinite geometric formula when the ratio is too big

Wrong: $1 + 2 + 4 + 8 + \cdots = \frac{1}{1 - 2} = -1$

Right: the series has no sum, because the partial sums $1, 3, 7, 15, \dots$ grow without bound

The formula $\frac{a}{1 - r}$ needs $\lvert r \rvert < 1$. A series with $r = -1$, such as $1 - 1 + 1 - 1 + \cdots$, has partial sums $1, 0, 1, 0, \dots$ and also has no sum.

Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#edge-cases-and-common-mistakes).

## Vectors and matrices

### Adding the lengths of vectors to get the length of the sum

Wrong: $\mathbf{u} = (3, 0)$ and $\mathbf{v} = (0, 4)$ give $\lVert \mathbf{u} + \mathbf{v} \rVert = 3 + 4 = 7$

Right: $\lVert (3, 4) \rVert = 5$

The lengths add only when the vectors point the same way. Otherwise the sum is shorter, because one side of a triangle is shorter than the other two together.

Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md#edge-cases-and-common-mistakes).

### Taking the direction angle from the arctangent alone

Wrong: the direction of $(-3, 4)$ is $\arctan\frac{4}{-3} \approx -53.1^\circ$

Right: the vector is in the second quadrant, so the angle is $-53.1^\circ + 180^\circ = 126.9^\circ$

The arctangent of a ratio loses the signs of the components. Look at the signs, or use `math.atan2(b, a)`, which gets the quadrant.

Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md#edge-cases-and-common-mistakes).

### Treating the dot product like a vector

Wrong: $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{w}$ implies $\mathbf{v} = \mathbf{w}$

Right: the dot product is a number, and equal dot products don't make equal vectors

For $\mathbf{u} = (1, 0)$, both $(2, 5)$ and $(2, -7)$ give 2. For the same reason $(\mathbf{u} \cdot \mathbf{v}) \cdot \mathbf{w}$ makes no sense, since it dots a number with a vector.

Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md#edge-cases-and-common-mistakes).

### Multiplying matrices entry by entry

Wrong: $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 3 & 0 \end{pmatrix}$

Right: each entry is a row times a column, and the first entry is $1 \cdot 0 + 2 \cdot 1 = 2$

Entry-by-entry multiplication exists, but it is a different operation and it doesn't compose substitutions. The sizes also decide whether the product exists at all.

Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#edge-cases-and-common-mistakes).

### Assuming that matrix multiplication commutes

Wrong: $AB = BA$, so $(A + B)^2 = A^2 + 2AB + B^2$

Right: in general $AB \ne BA$, and $(A + B)^2 = A^2 + AB + BA + B^2$

This is the one rule of number arithmetic that fails. Whenever you rearrange a product of matrices, check that you haven't swapped two factors.

Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#edge-cases-and-common-mistakes).

### Cancelling a matrix factor

Wrong: $AB = 0$ implies $A = 0$ or $B = 0$

Right: the product of two nonzero matrices can be zero

For example, $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ is the zero matrix. Cancelling works only with an invertible matrix, by multiplying both sides by its inverse.

Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#edge-cases-and-common-mistakes).

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
