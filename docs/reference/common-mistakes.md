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

Taught in [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#challenge), [existence and uniqueness proofs](../04-proofs-and-logic/04-more-proof-methods/02-existence-and-uniqueness-proofs.md#edge-cases-and-common-mistakes) and [divisibility and modular arithmetic](../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md).

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

Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#percent-change-or-percentage-points) and [percent change vs percentage points](../07-economics-math/01-measuring-the-economy/02-percent-change-vs-percentage-points.md).

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

Taught in [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#edge-cases-and-common-mistakes), [multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#dividing-by-an-expression-that-might-be-zero), [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md) and [if and only if proofs](../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md#edge-cases-and-common-mistakes), where dividing by a variable is an irreversible step in a chain.

### Keeping every solution after squaring both sides

Wrong: $\sqrt{x + 2} = x$ has the solutions $x = 2$ and $x = -1$

Right: only $x = 2$ is a solution

Squaring gives $x + 2 = x^2$, so $x^2 - x - 2 = 0$ and $(x - 2)(x + 1) = 0$. Squaring can add solutions, because $a = b$ and $a = -b$ both turn into $a^2 = b^2$, so check each candidate in the original equation. For $x = -1$ the left side is $\sqrt{1} = 1$ and the right side is $-1$, so $-1$ is an extraneous root.

Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#edge-cases-and-common-mistakes) and[rational and radical equations](../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md).

### Multiplying an inequality by an expression of unknown sign

Wrong: $\frac{1}{x} < 2$, so $1 < 2x$, so $x > \frac{1}{2}$

Right: $\frac{1}{x} < 2$ exactly when $x < 0$ or $x > \frac{1}{2}$

Multiplying by $x$ keeps the order only when $x > 0$. For $x < 0$ the order flips and gives $1 > 2x$, which every negative $x$ satisfies. Test $x = -1$: $\frac{1}{-1} = -1 < 2$, so it is a solution the wrong method lost. Split into cases by sign, or move every term to one side and use a sign chart.

Taught in [polynomial and rational inequalities](../03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md) and [direct proof](../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md#edge-cases-and-common-mistakes), where "$\frac{x}{y} \ge 2$, so $x \ge 2y$" is valid only for $y > 0$.

## Sets, intervals and absolute value

### Writing an element as a subset

Wrong: $2 \subseteq \{1, 2, 3\}$

Right: $2 \in \{1, 2, 3\}$, and $\{2\} \subseteq \{1, 2, 3\}$

The symbol $\in$ connects an element to a set, and $\subseteq$ connects two sets. The number 2 is not a set, so $2 \subseteq \{1, 2, 3\}$ is not even a statement.

Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#edge-cases-and-common-mistakes), [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#edge-cases-and-common-mistakes) and [proofs about sets](../04-proofs-and-logic/04-more-proof-methods/03-proofs-about-sets.md#edge-cases-and-common-mistakes).

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

Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#edge-cases-and-common-mistakes),[what is a function](../03-high-school/03-functions/01-what-is-a-function.md) and [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md).

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

Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#edge-cases-and-common-mistakes),[properties of operations](../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division), [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#why-isnt-checking-a-few-values-enough), [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md) and [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md).

### Assuming what you want to prove

Wrong: to prove $a^2 + b^2 \ge 2ab$, start from it, subtract $2ab$ to get $a^2 - 2ab + b^2 \ge 0$, reach $(a - b)^2 \ge 0$, and stop because that is true

Right: start from a known fact, $(a - b)^2 \ge 0$, expand it to $a^2 - 2ab + b^2 \ge 0$, and add $2ab$ to both sides to reach $a^2 + b^2 \ge 2ab$

Reaching a true statement from the claim proves nothing, because a false claim can lead to a true one: $-1 = 1$ is false, but squaring both sides gives $1 = 1$. Working backward is fine as scratch work for finding the steps. The written proof has to run forward from known facts, with each step following from the ones before it.

Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#why-not-do-the-same-to-both-sides), [scratch work and proof strategies](../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md#edge-cases-and-common-mistakes), [direct proof](../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-logic).

### Running a conditional backward from its conclusion

Wrong: "If it rains, the ground is wet. The ground is wet, so it rained."

Right: nothing follows about the rain. From "the ground is dry" you may conclude "it did not rain".

Going from $P \Rightarrow Q$ and $Q$ to $P$ is the fallacy of affirming the consequent, and a sprinkler also makes the ground wet. The contrapositive is the one valid way to use a conditional in reverse.

Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md#edge-cases-and-common-mistakes).

### Concluding the negation of the conclusion from the negation of the hypothesis

Wrong: "If a number is divisible by 6, it is even. The number 4 is not divisible by 6, so it is not even."

Right: the number 4 is even, and the conditional says nothing about it

From $P \Rightarrow Q$ and $\neg P$ nothing follows about $Q$, which is the fallacy of denying the antecedent. The conditional only says what happens when $P$ holds.

Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md#edge-cases-and-common-mistakes).

### Reading "only if" backward

Wrong: "You pass only if you hand in the project" means that handing in the project makes you pass

Right: it means "if you pass, then you handed in the project"

To test a reading, ask what would make the speaker a liar. A student who handed in the project and failed didn't. A student who passed without handing it in did. "$P$ only if $Q$" is $P \Rightarrow Q$.

Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md#edge-cases-and-common-mistakes).

### Reading the "if" of a theorem as "if and only if"

Wrong: a theorem says "$n$ is even if $n = 4k$", so every even $n$ has the form $4k$

Right: the theorem gives one direction only. The number 6 is even and is not of the form $4k$.

A definition's "if" means "if and only if", but a theorem's "if" does not, so read the exact wording before treating a statement as a characterization.

Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md#edge-cases-and-common-mistakes) and [if and only if proofs](../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md#edge-cases-and-common-mistakes).

### Moving a negation through a bracket without flipping the connective

Wrong: $\neg(P \wedge Q) \equiv \neg P \wedge \neg Q$, so the negation of "$x > 3$ and $x$ is even" is "$x \le 3$ and $x$ is odd"

Right: $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$, so the negation is "$x \le 3$ or $x$ is odd"

A "not" that enters a bracket flips the connective and negates each part. Test with $x = 2$: the original is false, so its negation must be true. The "or" version is true there, and the "and" version is false.

Taught in [truth tables and logical equivalence](../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md#edge-cases-and-common-mistakes) and [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#edge-cases-and-common-mistakes).

### Negating a conditional by negating only its conclusion

Wrong: the negation of "if it rains, the match is cancelled" is "if it rains, the match is not cancelled"

Right: the negation is "it rains and the match is not cancelled", which is $P \wedge \neg Q$

The original and the wrong version are both true on every sunny day, so they can't be opposites. A statement and its negation never have the same truth value.

Taught in [negation and translating English](../04-proofs-and-logic/02-logic-and-sets/05-negation-and-translating-english.md#edge-cases-and-common-mistakes).

### Flipping only some of the quantifiers when negating

Wrong: the negation of $\forall \varepsilon\ \exists \delta\ (\dots)$ is $\forall \varepsilon\ \forall \delta\ \neg(\dots)$

Right: the negation is $\exists \varepsilon\ \forall \delta\ \neg(\dots)$

Every quantifier in front flips, in the same order, and the statement inside is negated. Leaving one unflipped gives a statement that is not the opposite of the original.

Taught in [negation and translating English](../04-proofs-and-logic/02-logic-and-sets/05-negation-and-translating-english.md#edge-cases-and-common-mistakes).

### Using an arrow to mean "therefore"

Wrong: $x^2 = 9 \Rightarrow x = 3 \Rightarrow x + 1 = 4$

Right: $x^2 = 9$ gives $x = 3$ or $x = -3$, so $x + 1$ is 4 or $-2$

The expression $P \Rightarrow Q$ is one statement, and it can be false: the first arrow above is. When you mean "so", write "so" or "therefore". A chain of formulas joined by arrows with few words hides the reasons, which is why it is called symbol soup.

Taught in [reading math symbols](../04-proofs-and-logic/01-language-and-notation/04-reading-math-symbols.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-writing).

### Pairing the wrong connective with a quantifier

Wrong: "some student is a CS major who likes math" is $\exists x\,(C(x) \Rightarrow M(x))$

Right: it is $\exists x\,(C(x) \wedge M(x))$, and "every CS major likes math" is $\forall x\,(C(x) \Rightarrow M(x))$

The wrong version is true as soon as one student is not a CS major, since the conditional then holds vacuously. In the same way, $\forall x\,(C(x) \wedge M(x))$ would say that everybody is a CS major.

Taught in [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#edge-cases-and-common-mistakes).

### Swapping the order of quantifiers

Wrong: to prove "there is a natural number $N$ with $n \le N$ for every natural number $n$", let $n$ be given and take $N = n + 1$

Right: that proves "for every $n$ there is an $N$ with $n \le N$", a different and true statement. The original claim is false.

In $\forall x\,\exists y$ the number $y$ may depend on $x$, and in $\exists y\,\forall x$ one $y$ must work for every $x$. On the integers, "for every $x$ there is a $y$ with $y > x$" is true, and "there is a $y$ with $y > x$ for every $x$" is false.

Taught in [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-logic).

### Disproving a "there exists" claim with one failed example

Wrong: $x = 1$ doesn't satisfy $x^2 = 4$, so no $x$ does

Right: to disprove an existence claim you must show failure for every element of the domain. Here $x = 2$ works, so the claim is true.

One example settles a "there exists" claim only in the true direction: a single witness proves it.

Taught in [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#edge-cases-and-common-mistakes) and [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md#edge-cases-and-common-mistakes).

### Using one letter for two different integers

Wrong: in a proof about two even integers, "$m = 2k$ and $n = 2k$"

Right: $m = 2j$ and $n = 2k$, a new letter for each integer

Using $k$ twice forces $m = n$, so the proof covers only equal numbers. Each new integer needs its own letter.

Taught in [what is a proof](../04-proofs-and-logic/01-language-and-notation/01-what-is-a-proof.md#edge-cases-and-common-mistakes) and [proof language: let, suppose, WLOG](../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md#edge-cases-and-common-mistakes).

### Proving a special case

Wrong: "Let $m = 4$ and $n = 6$. Then $m + n = 10 = 2 \times 5$, which is even", offered as a proof that a sum of two even integers is even

Right: "Let $m$ and $n$ be even integers", and then argue with letters

A particular pair proves a fact about that pair. A specific number is the right choice only when the claim is about that number, or when you are giving a witness or a counterexample.

Taught in [what is a proof](../04-proofs-and-logic/01-language-and-notation/01-what-is-a-proof.md#edge-cases-and-common-mistakes) and [proof language: let, suppose, WLOG](../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md#edge-cases-and-common-mistakes).

### Proving the converse instead of the claim

Wrong: to prove "if $n^2$ is divisible by 4, then $n$ is even", suppose $n = 2k$ and show that $n^2 = 4k^2$ is divisible by 4

Right: prove the contrapositive. Suppose $n$ is odd, $n = 2k + 1$. Then $n^2 = 4(k^2 + k) + 1$ leaves remainder 1, so $4 \nmid n^2$.

Every line of the wrong version is true, and it proves the converse. Compare the first line of a contrapositive proof with "not $Q$" and its last line with "not $P$".

Taught in [contrapositive proof](../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-logic).

### Writing a negation wrongly in a contrapositive

Wrong: the contrapositive of "if $ab$ is even, then $a$ is even or $b$ is even" starts "suppose $a$ is odd or $b$ is odd"

Right: it starts "suppose $a$ and $b$ are both odd"

The negation of an "or" is an "and" of the negations. The wrong version is not equivalent to the claim: $a = 3$ and $b = 2$ make it fail.

Taught in [contrapositive proof](../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-logic).

### Using WLOG on a claim that is not symmetric

Wrong: to prove "if $ab$ is even, then $a$ is even", say that one of $a$ and $b$ is even, and without loss of generality it is $a$

Right: swapping $a$ and $b$ changes this claim, so WLOG is not allowed. The claim is false ($a = 3$, $b = 2$). The symmetric claim "then $a$ is even or $b$ is even" is true.

WLOG is a promise that the other case is the same argument with the names swapped. The promise is true only when the claim looks the same after the swap.

Taught in [proof language: let, suppose, WLOG](../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md#edge-cases-and-common-mistakes) and [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md#edge-cases-and-common-mistakes).

### Cases that miss a value

Wrong: to prove "for every real $x$, $x^2 \ge x$", treat $x > 1$ and $x < 0$ and stop

Right: the cases leave out $0 \le x \le 1$, where the claim fails: $x = \frac{1}{2}$ gives $\frac{1}{4} < \frac{1}{2}$

A proof by cases needs the cases to be exhaustive, so state why they cover everything. Splitting an integer by remainder on division by 3 needs three cases, and handling only two of them leaves the third unproved.

Taught in [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-method).

### Reaching a "contradiction" that is not one

Wrong: suppose there are finitely many primes, multiply them and add 1 to get $N$, observe that $N$ is not on the list so $N$ is not prime, and call that a contradiction

Right: "$N$ is not prime" clashes with nothing, since $N$ can be composite: $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \times 509$. Take a prime divisor $q$ of $N$. It is on the list, so it divides the product, and it divides $N$, so it divides 1.

A contradiction is a statement and its negation, both derived. If you can't name both halves of the clash, you haven't reached one.

Taught in [proof by contradiction](../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-method).

### A proof by contradiction that never uses its assumption

Wrong: to prove "if $m$ and $n$ are even, then $m + n$ is even", assume they are even and $m + n$ is odd, derive that $m + n = 2(j + k)$ is even, and call that a contradiction

Right: delete the assumption that $m + n$ is odd and the last sentence. What remains is a direct proof.

If a proof ends by contradicting its own extra assumption, with no use of that assumption in between, rewrite it directly.

Taught in [proof by contradiction](../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md#edge-cases-and-common-mistakes).

### Proving only one direction of an if-and-only-if

Wrong: "Suppose $n$ is odd, so $n^2$ is odd. Hence $n$ is odd if and only if $n^2$ is odd."

Right: also prove the other direction, which is a different statement: if $n^2$ is odd, then $n$ is odd

A converse can be false even when the forward half is true. Every multiple of 4 is even, and not every even number is a multiple of 4.

Taught in [if and only if proofs](../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md#edge-cases-and-common-mistakes).

### Taking a uniqueness proof for an existence proof

Wrong: "Let $N$ be the largest integer. If $M$ is also the largest integer, then $M \le N$ and $N \le M$, so $M = N$", offered as a proof that a largest integer exists

Right: the argument shows there is at most one largest integer. None exists.

Uniqueness talks only about objects you are given. Existence is separate work, and a claim of "exactly one" needs both.

Taught in [existence and uniqueness proofs](../04-proofs-and-logic/04-more-proof-methods/02-existence-and-uniqueness-proofs.md#edge-cases-and-common-mistakes).

### Offering a witness that is outside the domain

Wrong: the integer $x = \frac{5}{2}$ is a witness for "there is an integer $x$ with $2x = 5$"

Right: $\frac{5}{2}$ is not an integer, so it proves nothing, and no integer solves $2x = 5$

A witness has to satisfy every condition. For "a prime $p$ with $p + 2$ and $p + 6$ both prime", the value $p = 3$ gives 5 and 9, and 9 fails.

Taught in [existence and uniqueness proofs](../04-proofs-and-logic/04-more-proof-methods/02-existence-and-uniqueness-proofs.md#edge-cases-and-common-mistakes).

### A counterexample that breaks the hypothesis

Wrong: $n = 3$ is a counterexample to "if $n$ is even, then $n^2$ is even", since $3^2 = 9$ is odd

Right: $n = 3$ is not even, so it is not a counterexample, and the claim is true

A counterexample passes two checks: the hypothesis is true, and the conclusion is false. Write both checks out.

Taught in [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md#edge-cases-and-common-mistakes).

### Disproving the converse instead of the claim

Wrong: $n = 2$ is even and not divisible by 4, so "if $n$ is divisible by 4, then $n$ is even" is false

Right: $n = 2$ refutes the converse, "if $n$ is even, then $n$ is divisible by 4". The original claim is true.

A counterexample to the converse says nothing about the original statement.

Taught in [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md#edge-cases-and-common-mistakes).

### Circular reasoning

Wrong: the sum of two rationals is rational because the rationals are closed under addition

Right: write $\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$, an integer over a nonzero integer

"Closed under addition" is the claim itself, so it can't be the reason. A proof may use earlier results, but not the statement it is proving or one equivalent to it.

Taught in [how to write a proof](../04-proofs-and-logic/03-core-proof-methods/07-how-to-write-a-proof.md#definitions) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-logic).

### A filler word in place of the argument

Wrong: $n^3 - n = (n - 1)n(n + 1)$, which is divisible by 6 as the reader can see

Right: say why. Among three consecutive integers one is even and one is a multiple of 3, and $\gcd(2, 3) = 1$, so the product is divisible by 6.

In a textbook a word such as this means the author skipped a routine step. In a graded proof it means the grader will not give credit for it.

Taught in [how to read a proof](../04-proofs-and-logic/03-core-proof-methods/02-how-to-read-a-proof.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-the-writing).

### Skipping the base case in induction

Wrong: every natural number $n$ satisfies $n > n + 1$, because if $k > k + 1$, then adding 1 to both sides gives $k + 1 > k + 2$

Right: that inductive step is valid, but the claim is false, because the base case fails: $0 > 1$ is false

Induction needs both parts. The inductive step only says that each case passes its truth on to the next one, and the base case is what starts the chain. Without it, the argument above would prove a statement that is false for every $n$.

Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-induction).

## Induction

### Proving the inductive step backward

Wrong: for $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$, suppose the formula holds for $k + 1$, subtract $k + 1$ from both sides, and arrive at the formula for $k$

Right: start from the formula for $k$ and add the new term: $\sum_{i=1}^{k+1} i = \frac{k(k+1)}{2} + (k + 1) = \frac{(k+1)(k+2)}{2}$

The wrong version shows that $P(k + 1)$ implies $P(k)$, and induction needs $P(k)$ implies $P(k + 1)$. It starts from a statement nobody has shown to be true.

Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-induction).

### Treating checked cases as the inductive step

Wrong: $P(1), P(2), P(3)$ and $P(4)$ are true, so $P(k)$ implies $P(k + 1)$

Right: examples are evidence, and the step has to be an argument about an arbitrary $k$. The expression $n^2 + n + 41$ is prime for $n = 0, 1, \dots, 39$ and fails at $n = 40$, where it equals $41^2 = 1681$.

Checking cases can't replace the step.

Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#edge-cases-and-common-mistakes).

### A base case that does not support the step

Wrong: prove $n^2 < 2^n$ for every $n \ge 1$ by checking $n = 1$, where $1 < 2$, and giving an inductive step

Right: the claim fails at $n = 2, 3, 4$ (for example $16 = 2^4$ at $n = 4$), and the step works only from $k \ge 3$, so the proof has to start at the base case $n = 5$, where $25 < 32$

The step has to work for every $k$ from the base case on. A step that needs $k \ge 2$ without saying so, attached to a base case at 1, leaves the jump from 1 to 2 unproved.

Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#edge-cases-and-common-mistakes).

### Too few base cases in strong induction

Wrong: every $n \ge 8$ is a sum of 3s and 5s: the base case is $8 = 3 + 5$, and for $n \ge 9$ the number $n - 3$ is a sum of 3s and 5s by the hypothesis, so $n = (n - 3) + 3$ is too

Right: use three base cases, $8 = 3 + 5$, $9 = 3 + 3 + 3$ and $10 = 5 + 5$

For $n = 9$ the step calls on 6, and for $n = 10$ on 7, both below the starting value 8. The number 7 is not a sum of 3s and 5s, so the step leans on a false case. A step that reaches back three places needs three base cases.

Taught in [strong induction and well-ordering](../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-in-induction).

### Skipping a clause in a structural induction

Wrong: to show "every nonempty balanced string has the form $(x)$ with $x$ balanced", check the clause that builds $(x)$ from $x$, call the empty string irrelevant, and stop

Right: check every clause. The clause that joins two balanced strings gives $()()$, which cannot be written as $(x)$ with $x$ balanced, since the inside would be $)($. The claim is false.

A proof by structural induction has to treat the basis and every recursive clause.

Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#edge-cases-and-common-mistakes).

### Assuming the property for the new object

Wrong: in the recursive step for full binary trees, assume the property for the tree $T$ that is being built

Right: assume it for the two parts $T_1$ and $T_2$, and prove it for the tree $T$ built from them

Assuming the property for $T$ is assuming the conclusion.

Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#edge-cases-and-common-mistakes).

### Defining a function by recursion on an object with two constructions

Wrong: on balanced strings, define $f(\varepsilon) = 0$, $f((x)) = f(x) + 1$ and $f(xy) = 2f(x) + f(y)$

Right: this does not define a function. The string $()()()$ is $xy$ with $x = ()$ and $y = ()()$, which gives $f = 5$, and also $xy$ with $x = ()()$ and $y = ()$, which gives $f = 7$.

Structural induction is still valid on such a set, because it only needs every object to be built somehow. A recursive definition of a function needs each object to have exactly one construction, as full binary trees and strings built by appending do.

Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#edge-cases-and-common-mistakes).

### Leaving out the closure clause

Wrong: "$0 \in E$, and if $x \in E$ then $x + 2 \in E$", so every element of $E$ is even

Right: add the clause "nothing else is in $E$". Without it, $E$ could also contain 1 and every odd number.

The closure clause is what makes the induction cover everything in the set.

Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#edge-cases-and-common-mistakes).

## Sets, relations and functions

### Proving only one inclusion for a set equality

Wrong: to show $A \cap B = A$ when $A \subseteq B$, let $x \in A \cap B$; then $x \in A$ and $x \in B$, so $x \in A$

Right: that proves $A \cap B \subseteq A$, which is true for all sets. Add $A \subseteq A \cap B$: if $x \in A$, then $x \in B$ because $A \subseteq B$, so $x \in A \cap B$.

A set equality needs two inclusions. An unused hypothesis is a sign that one of them is missing.

Taught in [proofs about sets](../04-proofs-and-logic/04-more-proof-methods/03-proofs-about-sets.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-with-sets-and-functions).

### Proving a set identity from a Venn diagram

Wrong: a Venn diagram with three overlapping circles shows $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$, so the identity is proved

Right: use the diagram to guess, and prove with an element argument or a full truth table

A diagram shows one arrangement of the sets. It hides the cases where a region is empty, two sets are equal, or one set sits inside another.

Taught in [proofs about sets](../04-proofs-and-logic/04-more-proof-methods/03-proofs-about-sets.md#edge-cases-and-common-mistakes) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#edge-cases-and-common-mistakes).

### Taking a complement without a universe

Wrong: the complement of $\{1, 2\}$ is $\{3, 4, 5, 6\}$

Right: it depends on the universe. It is $\{3, 4, 5, 6\}$ when $U = \{1, \dots, 6\}$, and the set of all other integers when $U = \mathbb{Z}$.

Write the universe down before you start, even as a single line such as "$U = \mathbb{Z}$".

Taught in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#edge-cases-and-common-mistakes).

### Counting the subsets of a finite set as twice its size

Wrong: a set with $n$ elements has $2n$ subsets

Right: it has $2^n$, because each element is either in or out. A one-element set has two subsets, $\emptyset$ and itself.

The sets $\emptyset$, $\{\emptyset\}$ and $\{0\}$ are three different sets: the first has no elements, and the other two have one element each.

Taught in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#edge-cases-and-common-mistakes).

### Using an element where a subset belongs

Wrong: if $A \in B$ and $B \subseteq C$, then $A \subseteq C$

Right: the true conclusion is $A \in C$. With $A = \{1\}$, $B = \{\{1\}\}$ and $C = \{\{1\}, 2\}$, we have $A \in B$ and $B \subseteq C$, but $1 \notin C$.

The hypothesis $A \in B$ says that $A$ is one element of $B$. It does not say that the elements of $A$ are in $B$.

Taught in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-with-sets-and-functions).

### Calling antisymmetric the opposite of symmetric

Wrong: a relation that is not symmetric is antisymmetric

Right: the two properties are independent. Equality is both, and $\{(1, 2), (2, 1), (1, 3)\}$ is neither.

Symmetric says that every arrow is two-way. Antisymmetric says that a two-way arrow can only be a loop.

Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#edge-cases-and-common-mistakes).

### Looking for a chain before calling a relation transitive

Wrong: $R = \{(1, 2), (3, 4)\}$ is not transitive, because there is no pattern to check

Right: no pair ends where another starts, so there is nothing to break and $R$ is transitive

Transitivity says that if both hypotheses hold, then the conclusion holds. It does not say that a chain exists.

Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#edge-cases-and-common-mistakes).

### Treating an equivalence class as an element

Wrong: $[3]_5 = 3$, and $[1] = [4]$ under congruence mod 3 means $1 = 4$

Right: $[3]_5$ is the set $\{\dots, -2, 3, 8, \dots\}$, which contains 3. The classes $[1]$ and $[4]$ are equal because $1 \sim 4$.

Different names for the same class are the normal case. The test for equal classes is $a \sim b$, not $a = b$.

Taught in [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#edge-cases-and-common-mistakes).

### Assuming symmetry and transitivity give reflexivity

Wrong: $a \sim b$ and $b \sim a$ give $a \sim a$

Right: the relation $\{(1, 1), (2, 2)\}$ on $\{1, 2, 3\}$ is symmetric and transitive but not reflexive, and the element 3 is in no class

The argument assumes that $a$ is related to something.

Taught in [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#edge-cases-and-common-mistakes).

### Treating minimal as least

Wrong: a minimal element is the smallest element

Right: minimal means nothing is below it, and least means it is below everything. Among $\{2, 3, 4, 6, 12\}$ under divisibility, both 2 and 3 are minimal and there is no least element.

The mistake comes from total orders, where the two ideas coincide.

Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#edge-cases-and-common-mistakes).

### Treating divisibility on the integers as a partial order

Wrong: "$a \mid b$" is a partial order on $\mathbb{Z}$

Right: antisymmetry fails, since $2 \mid -2$ and $-2 \mid 2$ but $2 \ne -2$. Divisibility is a partial order on the positive integers.

When the set changes, check the properties again.

Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#edge-cases-and-common-mistakes).

### A piecewise rule with overlapping cases

Wrong: $f(x) = x + 1$ for $x \ge 0$ and $f(x) = x - 1$ for $x \le 0$ defines a function

Right: at $x = 0$ both rules apply and they disagree, since $f(0)$ would be both 1 and $-1$. Use $x < 0$ for the second rule.

A function gives exactly one output for each input, so cases must agree where they overlap, or not overlap. They must also cover the whole domain.

Taught in [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-with-sets-and-functions).

### A rule on classes that depends on the representative

Wrong: $F([a]) = a$ defines a function on the classes mod 6

Right: the class $[1]_6 = [7]_6$ would go to both 1 and 7, so the rule is not well defined

Always ask: if I use a different name for the same input, do I get the same answer?

Taught in [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#edge-cases-and-common-mistakes).

### Reading a preimage as an inverse function

Wrong: for $f(x) = x^2$, the notation $f^{-1}(\{4\})$ means nothing, because $f$ has no inverse function

Right: it is the preimage, the set of inputs that land in $\{4\}$, which is $\{-2, 2\}$

The preimage of a set always exists, whether or not $f$ has an inverse function.

Taught in [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#edge-cases-and-common-mistakes).

### Starting an injectivity proof from equal inputs

Wrong: to show that $f(x) = 5x - 2$ is injective, suppose $a = a'$; then $5a - 2 = 5a' - 2$

Right: suppose $f(a) = f(a')$. Then $5a = 5a'$, and dividing by 5 gives $a = a'$.

Equal inputs give equal outputs for every function, so the wrong version proves nothing. Injective means the reverse: equal outputs force equal inputs.

Taught in [injective, surjective and bijective](../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md#edge-cases-and-common-mistakes) and [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#mistakes-with-sets-and-functions).

### A surjectivity solution outside the domain

Wrong: $f(x) = \frac{1}{x}$ from $\mathbb{R} \setminus \{0\}$ to $\mathbb{R}$ is onto, because $\frac{1}{x} = y$ gives $x = \frac{1}{y}$

Right: at $y = 0$ there is no solution, so $f$ is not onto $\mathbb{R}$. It is onto $\mathbb{R} \setminus \{0\}$.

A surjectivity proof has to show that the $x$ it finds is an allowed input.

Taught in [injective, surjective and bijective](../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md#edge-cases-and-common-mistakes).

### Comparing infinite sets by part and whole

Wrong: the even numbers are only part of $\mathbb{N}$, so there are fewer of them

Right: $n \mapsto 2n$ is a bijection from $\mathbb{N}$ onto the even numbers, so the two sets have the same size

An infinite set can have the same size as a proper part of itself. Use a bijection to show equal sizes.

Taught in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#edge-cases-and-common-mistakes).

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

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#worked-examples) and [sample spaces, events and axioms](../05-university-core/07-probability/01-sample-spaces-events-and-axioms.md#edge-cases-and-common-mistakes).

### Adding probabilities for "at least one"

Wrong: the chance of at least one six in 4 rolls is $4 \times \frac{1}{6} = \frac{4}{6}$

Right: it is $1 - \left(\frac{5}{6}\right)^4 = \frac{671}{1296} \approx 0.518$

Adding counts the cases with two or more sixes more than once. Take the complement instead: the chance of no six at all, subtracted from 1.

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#worked-examples) and [sample spaces, events and axioms](../05-university-core/07-probability/01-sample-spaces-events-and-axioms.md#edge-cases-and-common-mistakes).

### Treating draws without replacement as independent

Wrong: the chance of two reds from a bag of 2 red and 3 blue marbles is $\left(\frac{2}{5}\right)^2 = \frac{4}{25}$

Right: after one red is drawn, 1 red is left among 4, so the chance is $\frac{2}{5} \cdot \frac{1}{4} = \frac{2}{20} = \frac{1}{10}$

Removing a marble changes the next draw, so the draws are not independent and the probabilities can't be squared.

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#edge-cases-and-common-mistakes) and [discrete random variables](../05-university-core/07-probability/03-discrete-random-variables.md#edge-cases-and-common-mistakes).

### Believing a streak makes the opposite result due

Wrong: after five heads in a row, tails is more likely on the next flip

Right: the next flip is still heads with probability $\frac{1}{2}$

The flips are independent, so the coin has no memory. Over many flips the proportion of heads settles toward $\frac{1}{2}$ because the early streak gets diluted, not because later flips compensate.

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#edge-cases-and-common-mistakes) and [the law of large numbers and the CLT](../05-university-core/07-probability/06-law-of-large-numbers-and-clt.md#edge-cases-and-common-mistakes).

### Reading association as causation

Wrong: towns with more libraries have more car accidents, so libraries cause accidents

Right: look for a confounding variable; here a larger population drives both counts

Two variables can move together because a third variable affects both. A scatter plot shows association, and a study design is needed to show causation.

Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#edge-cases-and-common-mistakes) and [joint distributions, covariance and sums](../05-university-core/07-probability/05-joint-distributions-covariance-and-sums.md#edge-cases-and-common-mistakes) and [correlation and linear regression](../05-university-core/08-statistics/04-correlation-and-linear-regression.md#edge-cases-and-common-mistakes).

### Extrapolating a line far beyond the data

Wrong: a fitted line predicts 147 out of 100 on a test after 20 hours of study

Right: don't use the line far outside the hours in the data

The line describes the range the data covers. Outside it the relationship can bend, level off or hit a limit, and a score above the maximum is the clue.

Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#edge-cases-and-common-mistakes) and [correlation and linear regression](../05-university-core/08-statistics/04-correlation-and-linear-regression.md#edge-cases-and-common-mistakes).

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

Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#edge-cases-and-common-mistakes) and[conditional probability and Bayes' theorem](../05-university-core/07-probability/02-conditional-probability-and-bayes.md) and [conditional probability and Bayes' theorem](../05-university-core/07-probability/02-conditional-probability-and-bayes.md#edge-cases-and-common-mistakes).

### Swapping the two sides of a conditional probability

Wrong: $P(A \mid B) = P(B \mid A)$

Right: $P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$, which is Bayes' theorem, and the two sides are usually different

Draw one card from a standard deck. The probability that it is a king, given that it is a face card, is $\frac{4}{12} = \frac{1}{3}$; the probability that it is a face card, given that it is a king, is $1$. The same mistake misleads people about medical tests: a test that catches most sick people can still give mostly false alarms when the disease is rare.

Taught in [conditional probability and Bayes' theorem](../05-university-core/07-probability/02-conditional-probability-and-bayes.md) and [conditional probability and Bayes' theorem](../05-university-core/07-probability/02-conditional-probability-and-bayes.md#edge-cases-and-common-mistakes).

### Counting ordered choices when order doesn't matter

Wrong: the number of 2-person committees you can form from 5 people is $5 \times 4 = 20$

Right: it is $\binom{5}{2} = \frac{5 \times 4}{2} = 10$

The count $5 \times 4$ lists each committee twice, once as (Ana, Ben) and once as (Ben, Ana). Ask whether swapping two choices gives a different outcome. If it does, as with choosing a president and a vice-president, order matters and $20$ is right; if not, divide out the orderings.

Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md).

### Counting the integers in a range off by one

Wrong: there are $10 - 3 = 7$ integers from 3 to 10, inclusive

Right: there are $10 - 3 + 1 = 8$

Subtracting counts the gaps between the numbers, and there is one more number than there are gaps, just as a fence with 7 gaps needs 8 posts. In general there are $b - a + 1$ integers from $a$ to $b$, inclusive. Python's `range(3, 11)` has 8 elements because it leaves out its upper end.

Taught in [counting rules](../06-cs-math/03-counting-and-discrete-probability/01-counting-rules.md).

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

Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#edge-cases-and-common-mistakes) and [infinite series basics](../05-university-core/05-sequences-and-series/02-infinite-series-basics.md#edge-cases-and-common-mistakes).

## Vectors and matrices

### Adding the lengths of vectors to get the length of the sum

Wrong: $\mathbf{u} = (3, 0)$ and $\mathbf{v} = (0, 4)$ give $\lVert \mathbf{u} + \mathbf{v} \rVert = 3 + 4 = 7$

Right: $\lVert (3, 4) \rVert = 5$

The lengths add only when the vectors point the same way. Otherwise the sum is shorter, because one side of a triangle is shorter than the other two together.

Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md#edge-cases-and-common-mistakes) and [vectors, dot product and span](../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md#edge-cases-and-common-mistakes).

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

Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#edge-cases-and-common-mistakes) and [matrix algebra and inverses](../05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md#edge-cases-and-common-mistakes).

### Assuming that matrix multiplication commutes

Wrong: $AB = BA$, so $(A + B)^2 = A^2 + 2AB + B^2$

Right: in general $AB \ne BA$, and $(A + B)^2 = A^2 + AB + BA + B^2$

This is the one rule of number arithmetic that fails. Whenever you rearrange a product of matrices, check that you haven't swapped two factors.

Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#edge-cases-and-common-mistakes) and [matrix algebra and inverses](../05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md#edge-cases-and-common-mistakes).

### Cancelling a matrix factor

Wrong: $AB = 0$ implies $A = 0$ or $B = 0$

Right: the product of two nonzero matrices can be zero

For example, $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ is the zero matrix. Cancelling works only with an invertible matrix, by multiplying both sides by its inverse.

Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#edge-cases-and-common-mistakes) and [matrix algebra and inverses](../05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md#edge-cases-and-common-mistakes).

## Limits and continuity

### Reading the limit as the value at the point

Wrong: $f(x) = \frac{x^2 - 1}{x - 1}$ is undefined at 1, so it has no limit there. If $f(1)$ were defined to be 7, the limit would be 7.

Right: the limit at 1 is 2 in both cases

The limit never looks at $x = 1$ itself. It describes the values near 1, so changing or removing the value at 1 changes nothing. Limit and value agree only for continuous functions.

Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#edge-cases-and-common-mistakes).

### Reading a 0/0 form as a number

Wrong: $\frac{0}{0} = 0$, or $\frac{0}{0} = 1$

Right: a $\frac{0}{0}$ form can come out as anything. At 0, the limit of $\frac{x^2}{x}$ is 0, the limit of $\frac{3x}{x}$ is 3, and $\frac{x}{x^2}$ has no limit because the sides disagree.

The form $\frac{0}{0}$ is a signal that the formula needs work. Only the cancellation tells you the answer. By contrast, $\frac{c}{0}$ with $c \ne 0$ always means a blow-up or a failed limit.

Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#edge-cases-and-common-mistakes).

### Using a limit law when a piece has no limit

Wrong: $x \cdot \frac{1}{x}$ has no limit at 0, because $\frac{1}{x}$ has none

Right: for $x \ne 0$ the product equals 1, so its limit at 0 is 1

The limit laws run one way: if the pieces have limits, the combination follows the formula. They don't say that a combination of pieces without limits has none. In the same way, $\sin\frac{1}{x} + \left(-\sin\frac{1}{x}\right)$ is 0 for every $x \ne 0$, although neither piece has a limit at 0.

Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#edge-cases-and-common-mistakes).

### Trusting a table on an oscillating function

Wrong: the values of $\sin\frac{1}{x}$ at $x = \frac{1}{n\pi}$ are all 0, so the limit at 0 is 0

Right: at $x = \frac{1}{2n\pi + \pi/2}$ the values are all 1. Two input sequences that close in on 0 give different answers, so the limit does not exist.

A table can support a guess but never proves one.

Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#edge-cases-and-common-mistakes).

### Doing arithmetic with infinity

Wrong: $\lim_{x \to \infty}(x^2 - x) = \infty - \infty = 0$

Right: factor it as $x(x - 1)$, a product of two large positive numbers, so the limit is $\infty$

The symbol $\infty$ is not a number, so "$\infty - \infty$" and "$0 \cdot \infty$" have no answer until the expression is rewritten.

Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#edge-cases-and-common-mistakes).

### Letting delta depend on x

Wrong: to prove $\lim_{x \to 3} x^2 = 9$, take $\delta = \frac{\varepsilon}{\lvert x + 3 \rvert}$

Right: choose $\delta$ from $\varepsilon$ alone, by bounding the factor $\lvert x + 3 \rvert$ on a fixed window around 3

The window size $\delta$ is chosen first, and the challenger picks $x$ afterwards, so a formula for $\delta$ that mentions $x$ names something that doesn't exist yet.

Taught in [the epsilon-delta definition](../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md#edge-cases-and-common-mistakes).

### Checking one epsilon

Wrong: for $\lim_{x \to 1} 2x = 2$, the choice $\delta = 0.05$ works for $\varepsilon = 0.1$, so the limit is proved

Right: give a rule that turns every $\varepsilon$ into a working $\delta$, here $\delta = \frac{\varepsilon}{2}$, and show that it works

Checking one $\varepsilon$ is a good test of the idea, but the definition says "for every $\varepsilon$".

Taught in [the epsilon-delta definition](../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md#edge-cases-and-common-mistakes).

### Calling a hole continuous

Wrong: $f(x) = \frac{x^2 - 4}{x - 2}$ is continuous at 2, because its limit there is 4

Right: $f(2)$ is undefined, so $f$ is discontinuous at 2 (a removable discontinuity)

Continuity needs three things: the value exists, the limit exists, and they are equal. A function with a hole is discontinuous at the hole, even when the hole can be filled.

Taught in [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#edge-cases-and-common-mistakes).

### Using the intermediate value theorem across a break

Wrong: $f(x) = \frac{1}{x}$ is negative at $-1$ and positive at 1, so it has a zero between them

Right: $f$ is not continuous on $[-1, 1]$, and it never equals 0

The theorem needs continuity on the whole closed interval. In the same way, $\lfloor x \rfloor$ goes from 0 to 1 on $[0.5, 1.5]$ and never equals $\frac{1}{2}$. A sign change on its own guarantees nothing.

Taught in [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#edge-cases-and-common-mistakes).

### Reversing the intermediate value theorem

Wrong: a function that takes every value between $f(a)$ and $f(b)$ must be continuous

Right: let $f(x) = \sin\frac{1}{x}$ for $x \ne 0$ and $f(0) = 0$. On $[-1, 1]$ it takes every value between $-1$ and 1, and it is discontinuous at 0.

The theorem says that continuity implies no skipped values, not the other way round.

Taught in [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#edge-cases-and-common-mistakes).

### Using the extreme value theorem on an open interval

Wrong: $\frac{1}{x}$ is continuous on $(0, 1]$, so it has a maximum there

Right: the interval is not closed, and $\frac{1}{x}$ grows without bound near 0, so there is no maximum

Both conditions of the theorem matter: continuity and a closed interval $[a, b]$.

Taught in [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#the-extreme-value-theorem) and [the mean value theorem and extrema](../05-university-core/03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md#edge-cases-and-common-mistakes).

## Calculus

### Giving up on a limit that gives zero over zero

Wrong: $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$ doesn't exist, because putting in $x = 2$ gives $\frac{0}{0}$

Right: factor first. For $x \ne 2$, $\frac{x^2 - 4}{x - 2} = \frac{(x - 2)(x + 2)}{x - 2} = x + 2$, so the limit is $4$.

The form $\frac{0}{0}$ only says that substitution failed to give an answer. A limit depends on the values near $2$ and never on the value at $2$, so cancelling the factor $x - 2$, which is nonzero near $2$, is allowed.

Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md) and [linear approximation and L'Hopital's rule](../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md#lhopitals-rule).

### Multiplying derivatives for the derivative of a product

Wrong: $\frac{d}{dx}(fg) = f'g'$

Right: $\frac{d}{dx}(fg) = f'g + fg'$

Test with $f(x) = g(x) = x$: the product is $x^2$, whose derivative is $2x$, but $f'g' = 1 \cdot 1 = 1$. The product rule gives $1 \cdot x + x \cdot 1 = 2x$. Quotients have their own rule as well, and $\left(\frac{f}{g}\right)'$ is not $\frac{f'}{g'}$.

Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md).

### Forgetting the chain rule

Wrong: $\frac{d}{dx} \sin(3x) = \cos(3x)$

Right: $\frac{d}{dx} \sin(3x) = 3\cos(3x)$

When a function is applied to something other than plain $x$, multiply by the derivative of the inside: $\frac{d}{dx} f(g(x)) = f'(g(x))\,g'(x)$. The inside here is $3x$, with derivative $3$. In the same way, $\frac{d}{dx}(x^2 + 1)^5 = 5(x^2 + 1)^4 \cdot 2x$.

Taught in [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md).

### Putting in h equals 0 too early

Wrong: $\frac{(x + h)^2 - x^2}{h}$ at $h = 0$ is $\frac{0}{0}$, so the derivative does not exist

Right: simplify first. The quotient is $\frac{2xh + h^2}{h} = 2x + h$, and letting $h \to 0$ gives $2x$.

A limit is about what happens as $h$ gets close to 0, not at 0. If an $h$ is still in the denominator after your algebra, you are not done.

Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#edge-cases-and-common-mistakes).

### Substituting the point before differentiating

Wrong: for $f(x) = x^2$, $f(3) = 9$ is a constant, so $f'(3) = 0$

Right: differentiate first, $f'(x) = 2x$, and then substitute: $f'(3) = 6$

The number $f'(3)$ means "find $f'(x)$, then put in $x = 3$". Substituting first and then differentiating gives the derivative of a constant.

Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#edge-cases-and-common-mistakes).

### Assuming that continuous means differentiable

Wrong: the graph of $\lvert x \rvert$ has no gaps, so it has a derivative at 0

Right: it has a corner at 0 and no tangent line there

Differentiable implies continuous. The implication does not go the other way.

Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#differentiable-implies-continuous).

### Counting an infinite slope as a derivative

Wrong: $f(x) = x^{1/3}$ has derivative $\infty$ at 0

Right: the difference quotient tends to $\infty$, which is not a real number, so $f'(0)$ does not exist. The graph has a vertical tangent there.

The definition of the derivative asks for a real-number limit.

Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#where-a-derivative-does-not-exist).

### Writing the quotient rule numerator in the wrong order

Wrong: $\left(\frac{f}{g}\right)' = \frac{fg' - f'g}{g^2}$

Right: $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$

Test with $f = 1$: the right formula gives $\left(\frac{1}{g}\right)' = -\frac{g'}{g^2}$, with a minus sign and no $f'$ term. The wrong order gives the opposite sign.

Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#edge-cases-and-common-mistakes).

### Using the power rule on an exponential

Wrong: $\frac{d}{dx}\,2^x = x \cdot 2^{x-1}$

Right: $\frac{d}{dx}\,2^x = 2^x \ln 2$

The power rule is for a variable base and a constant exponent. In $2^x$ the variable is in the exponent. At $x = 2$ the right derivative is $4 \ln 2 \approx 2.77$, and the wrong formula gives 4. For $x^x$, with the variable in both places, neither rule works, and logarithmic differentiation is used.

Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#edge-cases-and-common-mistakes) and [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md#edge-cases-and-common-mistakes).

### Getting the sign of the cosine derivative wrong

Wrong: $\frac{d}{dx}\cos x = \sin x$

Right: $\frac{d}{dx}\cos x = -\sin x$

The cosine falls just after $x = 0$, where $\sin x$ is positive, so its derivative must be negative there. These formulas hold in radians only.

Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#edge-cases-and-common-mistakes).

### Dropping the factor dy/dx in implicit differentiation

Wrong: $\frac{d}{dx}\,y^3 = 3y^2$

Right: $\frac{d}{dx}\,y^3 = 3y^2\,\frac{dy}{dx}$

Every term with $y$ gets a factor $\frac{dy}{dx}$, because $y$ depends on $x$. A term with $x$ alone gets none. On the circle $x^2 + y^2 = 25$, the equation $2x + 2y\frac{dy}{dx} = 0$ gives slope $-\frac{3}{4}$ at $(3, 4)$.

Taught in [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md#edge-cases-and-common-mistakes).

### Putting the derivative of the inside into the outer function

Wrong: $\frac{d}{dx}\sin(x^2) = \cos(2x)$

Right: $\frac{d}{dx}\sin(x^2) = \cos(x^2) \cdot 2x$

The expression $f'(g(x))$ means "differentiate $f$, then put $g(x)$ in". Putting $g'$ inside gives a different function.

Taught in [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md#edge-cases-and-common-mistakes).

### Using the slope of the original function at the wrong point

Wrong: for $f(x) = x^5 + x + 1$, $\left(f^{-1}\right)'(3) = \frac{1}{f'(3)}$

Right: find the input $a$ with $f(a) = 3$, which is $a = 1$, and use $\frac{1}{f'(1)} = \frac{1}{6}$

The slope of the inverse at $b$ comes from the slope of $f$ at the matching point $a$, where $f(a) = b$. The graph of $f$ near $(1, 3)$ is steep, so the reflected graph near $(3, 1)$ should be flat.

Taught in [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md#edge-cases-and-common-mistakes).

### Forgetting the constant of integration

Wrong: $\int 2x\,dx = x^2$

Right: $\int 2x\,dx = x^2 + C$, where $C$ stands for an arbitrary constant

Every function $x^2 + C$ has derivative $2x$ (for example $x^2 + 7$), so the indefinite integral is the whole family. The constant matters when a condition fixes it: if $F'(x) = 2x$ and $F(0) = 5$, then $F(x) = x^2 + 5$. A definite integral has no $+C$, because it cancels in $F(b) - F(a)$.

Taught in [the fundamental theorem of calculus](../05-university-core/04-integrals/02-fundamental-theorem-of-calculus.md) and [the fundamental theorem of calculus](../05-university-core/04-integrals/02-fundamental-theorem-of-calculus.md#edge-cases-and-common-mistakes).

## Applications of derivatives

### Substituting the numbers of the instant before differentiating

Wrong: a 13 m ladder with its foot 5 m out and its top 12 m up gives $5^2 + y^2 = 169$, so $2y\frac{dy}{dt} = 0$ and the top does not move

Right: keep $x$ as a letter, $x^2 + y^2 = 169$, differentiate to get $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$, and then put in $x = 5$ and $y = 12$. If the foot moves out at 2 m/s, $\frac{dy}{dt} = -\frac{5}{12} \cdot 2 = -\frac{5}{6}$ m/s

The foot's position changes with time, so it is a variable until the derivative has been taken. Substituting first turns it into a constant, and its derivative disappears.

Taught in [rates of change and marginal analysis](../05-university-core/03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md#edge-cases-and-common-mistakes).

### Losing the sign of a rate

Wrong: a tank draining at 0.5 m$^3$ per minute has $\frac{dV}{dt} = 0.5$

Right: $\frac{dV}{dt} = -0.5$

A quantity that is falling has a negative rate. If the answer for a falling level comes out positive, a sign was lost somewhere. Also convert every quantity to one system of units before differentiating.

Taught in [rates of change and marginal analysis](../05-university-core/03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md#edge-cases-and-common-mistakes).

### Using the average cost as the cost of the next unit

Wrong: with $C(q) = 1000 + 10q + 0.05q^2$, the next unit after 100 costs $\frac{C(100)}{100} = \$25$

Right: the next unit costs about $C'(100) = \$20$, and $C(101) - C(100) = \$20.05$

The average cost spreads the whole bill, including the fixed cost, over all the units. The marginal cost looks only at the next unit. They are equal only at the minimum of the average cost.

Taught in [rates of change and marginal analysis](../05-university-core/03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md#edge-cases-and-common-mistakes).

### Applying L'Hopital's rule when the form is not indeterminate

Wrong: $\lim_{x \to 0}\frac{x + 1}{x + 2}$ is $\lim_{x \to 0}\frac{1}{1} = 1$

Right: the limit is $\frac{1}{2}$, by direct substitution

The rule applies only to $\frac{0}{0}$ or $\frac{\infty}{\infty}$. Check the form first. The same limit also shows the next mistake: the rule differentiates the top and the bottom separately, so the new quotient is $\frac{f'}{g'}$ and not $\left(\frac{f}{g}\right)'$.

Taught in [linear approximation and L'Hopital's rule](../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md#edge-cases-and-common-mistakes).

### Concluding that a limit does not exist because the limit of the derivatives does not

Wrong: $\frac{1 + \cos x}{1}$ has no limit as $x \to \infty$, so $\lim_{x \to \infty}\frac{x + \sin x}{x}$ does not exist

Right: the rule gives no answer in that case, and the limit is 1, since $\frac{x + \sin x}{x} = 1 + \frac{\sin x}{x}$

L'Hopital's rule says that if the second limit exists, then the first equals it. It does not say anything when the second limit fails to exist.

Taught in [linear approximation and L'Hopital's rule](../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md#edge-cases-and-common-mistakes).

### Treating $1^\infty$ as 1

Wrong: $\lim_{x \to \infty}\left(1 + \frac{1}{x}\right)^x = 1^\infty = 1$

Right: the limit is $e$

The base tends to 1 but the exponent tends to infinity, and neither one decides the answer. Take the logarithm to turn the power into a product, find that limit, and then undo the logarithm. The forms $0 \cdot \infty$ and $\infty - \infty$ also need rewriting.

Taught in [linear approximation and L'Hopital's rule](../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md#the-other-indeterminate-forms).

### Using a linearization far from its base point, or in degrees

Wrong: $\sin x \approx x$ gives $\sin 1 \approx 1$, and $\sin 5^\circ \approx 5$

Right: $\sin 1 = 0.841$, and $\sin 5^\circ \approx 0.0873$ because $5^\circ$ is $0.0873$ radians

The tangent line is a good approximation only near the base point, and the formula $\sin x \approx x$ is for $x$ in radians. Convert degrees first.

Taught in [linear approximation and L'Hopital's rule](../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md#edge-cases-and-common-mistakes).

### Skipping the endpoints when finding absolute extrema

Wrong: the critical points of $f$ on $[0, 3.5]$ are all inside, so the maximum is at one of them

Right: compare the values at the critical points and at both endpoints

On a closed interval, the maximum and minimum are often at an end, where the derivative need not be 0.

Taught in [the mean value theorem and extrema](../05-university-core/03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md#edge-cases-and-common-mistakes).

### Believing that a zero derivative means an extremum

Wrong: $f'(0) = 0$ for $f(x) = x^3$, so $f$ has a local extremum at 0

Right: $f'(c) = 0$ marks a candidate. Test it with the sign of $f'$ on each side, or with $f''$

The function $x^3$ rises straight through its flat spot. A candidate list should also include the points where $f'$ does not exist, such as the corner of $\lvert x \rvert$ and the cusp of $x^{2/3}$ at 0, which solving $f'(x) = 0$ never finds.

Taught in [the mean value theorem and extrema](../05-university-core/03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md#edge-cases-and-common-mistakes).

### Using the mean value theorem without checking its conditions

Wrong: $f(x) = \lvert x \rvert$ on $[-1, 2]$ has a number $c$ with $f'(c) = \frac{f(2) - f(-1)}{3} = \frac{1}{3}$

Right: $f$ is not differentiable at 0, so the theorem does not apply, and no such $c$ exists

Both conditions are required: continuous on the closed interval and differentiable on the open one. The theorem also says only that some $c$ exists. It does not say where it is, or that it is unique.

Taught in [the mean value theorem and extrema](../05-university-core/03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md#edge-cases-and-common-mistakes).

### Calling every point with a zero second derivative an inflection point

Wrong: $f(x) = x^4$ has $f''(0) = 0$, so $(0, 0)$ is an inflection point

Right: an inflection point needs the sign of $f''$ to change, and $x^4$ is concave up on both sides of 0

The condition $f''(c) = 0$ gives a candidate only. The second derivative test also says nothing when $f''(c) = 0$: it cannot separate $x^4$, $-x^4$ and $x^3$, so use the sign chart of $f'$. Conversely, an inflection point can occur where $f''$ does not exist, as for $x^{1/3}$ at 0.

Taught in [concavity and curve sketching](../05-university-core/03-applications-of-derivatives/04-concavity-and-curve-sketching.md#edge-cases-and-common-mistakes).

### Leaving two variables in the objective function

Wrong: differentiate $A = xy$ with the fence constraint $2x + y = 200$ unused

Right: solve the constraint for $y = 200 - 2x$, substitute to get $A = x(200 - 2x)$, and then differentiate

A one-variable method needs a one-variable function. Substitute the constraint first, and note the allowed range of $x$.

Taught in [optimization](../05-university-core/03-applications-of-derivatives/05-optimization.md#edge-cases-and-common-mistakes).

### Accepting a critical point outside the feasible interval

Wrong: both roots of $V'(x) = 0$ are candidates, including $x = 12.74$ in the box problem

Right: only a root inside the feasible interval is a candidate, and the endpoints of that interval are candidates too

A root that gives a negative width, or a length longer than the material, is not an allowed choice. If no critical point is allowed, the answer is at an endpoint.

Taught in [optimization](../05-university-core/03-applications-of-derivatives/05-optimization.md#edge-cases-and-common-mistakes).

### Assuming that marginal revenue equal to marginal cost gives a maximum

Wrong: $R'(q) = C'(q)$ at $q^*$, so profit is largest at $q^*$

Right: check the sign of $P''(q^*)$, or the sign of $P'$ on each side

The condition $R' = C'$ also holds at a minimum of profit. It is the first-order condition and finds candidates only.

Taught in [optimization](../05-university-core/03-applications-of-derivatives/05-optimization.md#edge-cases-and-common-mistakes).

### Choosing a learning rate that is too large

Wrong: use a big step in $w_{n+1} = w_n - \eta f'(w_n)$ so that it converges faster

Right: lower $\eta$ when the loss rises. For $f(w) = \frac{\lambda}{2}w^2$ the iteration settles down only when $\eta < \frac{2}{\lambda}$

Gradient descent does not fail loudly: the values just grow. Print the loss at each step.

Taught in [optimization](../05-university-core/03-applications-of-derivatives/05-optimization.md#edge-cases-and-common-mistakes).

## Integrals

### Reading the integral as the area when the function changes sign

Wrong: $\int_0^{2\pi}\sin x\,dx$ is the area of the two arches, which is 4

Right: the integral is the signed area, and it is 0, because the arch below the axis cancels the arch above it

For the total area, split the interval where the function changes sign and integrate $\lvert f \rvert$. The distance travelled is likewise the integral of the speed, not of the velocity.

Taught in [Riemann sums and the definite integral](../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md#edge-cases-and-common-mistakes).

### Forgetting to divide by $n$ in a Riemann sum

Wrong: $\Delta x = b - a$, or adding all $n + 1$ points $x_0, \dots, x_n$ in a left or right sum

Right: $\Delta x = \frac{b - a}{n}$, and the left sum uses $x_0, \dots, x_{n-1}$ while the right sum uses $x_1, \dots, x_n$

The $n$ rectangles each have width $\frac{b - a}{n}$. A left sum skips the right end and a right sum skips the left end.

Taught in [Riemann sums and the definite integral](../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md#edge-cases-and-common-mistakes).

### Splitting the integral of a product

Wrong: $\int_0^1 x \cdot x\,dx = \int_0^1 x\,dx \cdot \int_0^1 x\,dx = \frac{1}{4}$

Right: $\int_0^1 x^2\,dx = \frac{1}{3}$

An integral splits over sums and pulls out constant factors, and it does not split over products or quotients.

Taught in [Riemann sums and the definite integral](../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md#edge-cases-and-common-mistakes).

### Applying the fundamental theorem across a discontinuity

Wrong: $\int_{-1}^{1}\frac{1}{x^2}\,dx = \left[-\frac{1}{x}\right]_{-1}^{1} = -1 - 1 = -2$

Right: the integrand is not continuous at 0, the integral is improper, and it diverges

A positive function cannot have a negative area. Before subtracting antiderivative values, scan the interval for a division by zero, the logarithm of 0 or the tangent at $\frac{\pi}{2}$.

Taught in [the fundamental theorem of calculus](../05-university-core/04-integrals/02-fundamental-theorem-of-calculus.md#edge-cases-and-common-mistakes).

### Using the power rule for $\frac{1}{x}$

Wrong: $\int \frac{1}{x}\,dx = \frac{x^0}{0}$

Right: $\int \frac{1}{x}\,dx = \ln\lvert x \rvert + C$

The formula $\frac{x^{n+1}}{n+1}$ divides by 0 when $n = -1$. For the other powers, raise the power by 1 and divide by the new power: $\int x^3\,dx = \frac{x^4}{4} + C$, not $4x^4$. Keep the absolute value, since the answer is wrong for $x < 0$ without it.

Taught in [the fundamental theorem of calculus](../05-university-core/04-integrals/02-fundamental-theorem-of-calculus.md#edge-cases-and-common-mistakes).

### Dropping the inner derivative when differentiating an integral

Wrong: $\frac{d}{dx}\int_0^{x^2}\cos\left(t^2\right)dt = \cos\left(x^4\right)$

Right: $\frac{d}{dx}\int_0^{x^2}\cos\left(t^2\right)dt = \cos\left(x^4\right) \cdot 2x$

The upper limit is a function of $x$, so the chain rule applies. Test the rule with $f = 1$: the integral $\int_0^{x^2}1\,dt$ is $x^2$, whose derivative is $2x$.

Taught in [the fundamental theorem of calculus](../05-university-core/04-integrals/02-fundamental-theorem-of-calculus.md#edge-cases-and-common-mistakes).

### Leaving an $x$ behind in a substitution

Wrong: with $u = x^2$, write $\int x\,e^{x^2}\,dx = \int x\,e^u\,du$

Right: $du = 2x\,dx$, so $x\,dx = \frac{1}{2}\,du$ and the integral is $\frac{1}{2}\int e^u\,du = \frac{1}{2}e^{x^2} + C$

Every part of the integrand, including $dx$, must be rewritten in $u$. A constant factor can come out of an integral, but a variable one cannot, which is why $\int e^{x^2}\,dx$ cannot be done this way.

Taught in [u-substitution](../05-university-core/04-integrals/03-u-substitution.md#edge-cases-and-common-mistakes).

### Keeping the old limits after a substitution

Wrong: $\int_0^2 x\left(1 + x^2\right)^3\,dx = \int_0^2 \tfrac{1}{2}u^3\,du$ with $u = 1 + x^2$

Right: the limits become $u = 1$ and $u = 5$, so the integral is $\frac{1}{2}\int_1^5 u^3\,du = \frac{5^4 - 1}{8} = 78$

The limits belong to the variable. Either change them with the substitution, or go back to $x$ before putting them in.

Taught in [u-substitution](../05-university-core/04-integrals/03-u-substitution.md#edge-cases-and-common-mistakes).

### Using integration by parts when a substitution works

Wrong: for $\int x\,e^{x^2}\,dx$, take $u = x$ and $dv = e^{x^2}\,dx$

Right: use $u = x^2$ in a substitution, since $dv = e^{x^2}\,dx$ cannot be integrated in closed form

Parts needs a $dv$ that can be integrated. Try substitution first, and use parts when the integrand is a product of different kinds of function. Check the answer by differentiating.

Taught in [integration by parts and trig integrals](../05-university-core/04-integrals/04-integration-by-parts-and-trig-integrals.md#edge-cases-and-common-mistakes).

### Getting the sign wrong in integration by parts

Wrong: $\int x\,e^x\,dx = x\,e^x + \int e^x\,dx = x\,e^x + e^x + C$

Right: $\int x\,e^x\,dx = x\,e^x - \int e^x\,dx = x\,e^x - e^x + C$

The formula is $\int u\,dv = uv - \int v\,du$. The wrong answer has derivative $xe^x + 2e^x$, which is not the integrand. For a definite integral, the term $\bigl[uv\bigr]_a^b$ is evaluated at both limits.

Taught in [integration by parts and trig integrals](../05-university-core/04-integrals/04-integration-by-parts-and-trig-integrals.md#edge-cases-and-common-mistakes).

### Integrating a squared sine as if it were the inside of a power

Wrong: $\int \sin^2 x\,dx = \frac{\sin^3 x}{3} + C$

Right: use $\sin^2 x = \frac{1 - \cos 2x}{2}$, which gives $\frac{x}{2} - \frac{\sin 2x}{4} + C$

The power rule works only if the derivative of the inside is also a factor of the integrand, as in $\int \sin^2 x \cos x\,dx$. Differentiating the wrong answer gives $\sin^2 x \cos x$.

Taught in [integration by parts and trig integrals](../05-university-core/04-integrals/04-integration-by-parts-and-trig-integrals.md#edge-cases-and-common-mistakes).

### Decomposing an improper fraction

Wrong: $\frac{x^2 + 1}{x^2 - 1} = \frac{A}{x - 1} + \frac{B}{x + 1}$

Right: divide first, $\frac{x^2 + 1}{x^2 - 1} = 1 + \frac{2}{x^2 - 1}$, and then decompose the remainder

For large $x$ the wrong form tends to 0 while the fraction tends to 1. Partial fractions apply only when the degree of the top is less than the degree of the bottom.

Taught in [partial fractions and improper integrals](../05-university-core/04-integrals/05-partial-fractions-and-improper-integrals.md#edge-cases-and-common-mistakes).

### Writing one term for a repeated factor

Wrong: $\frac{3x + 1}{(x - 1)^2} = \frac{A}{(x - 1)^2}$

Right: $\frac{A}{x - 1} + \frac{B}{(x - 1)^2}$, and a quadratic factor needs a linear numerator, $Bx + C$

Every power of a repeated factor gets its own term. With too few terms, the system for the unknown constants has no solution.

Taught in [partial fractions and improper integrals](../05-university-core/04-integrals/05-partial-fractions-and-improper-integrals.md#edge-cases-and-common-mistakes).

### Substituting infinity into an antiderivative

Wrong: $\int_1^\infty \frac{1}{x^2}\,dx = \left[-\frac{1}{x}\right]_1^{\infty} = -\frac{1}{\infty} + 1$

Right: $\lim_{b \to \infty}\left(-\frac{1}{b} + 1\right) = 1$

Write the limit. The step matters most when the answer is a difference of two terms that each tend to infinity.

Taught in [partial fractions and improper integrals](../05-university-core/04-integrals/05-partial-fractions-and-improper-integrals.md#edge-cases-and-common-mistakes).

### Assuming that an integrand tending to 0 gives a convergent integral

Wrong: $\frac{1}{x} \to 0$, so $\int_1^\infty \frac{1}{x}\,dx$ converges

Right: it diverges. The integral $\int_1^\infty \frac{1}{x^p}\,dx$ converges exactly when $p > 1$

The integrand must go to 0 faster than $\frac{1}{x}$. The test for a singularity at 0 goes the other way: $\int_0^1 \frac{1}{x^p}\,dx$ converges exactly when $p < 1$.

Taught in [partial fractions and improper integrals](../05-university-core/04-integrals/05-partial-fractions-and-improper-integrals.md#edge-cases-and-common-mistakes).

### Subtracting the curves in the wrong order

Wrong: area $= \int_a^b (g - f)\,dx$ with $f$ above $g$, or $\int_0^{2\pi}(\sin x - \cos x)\,dx$ across a crossing

Right: top minus bottom, split at each crossing, or integrate $\lvert f - g \rvert$

Subtracting the other way gives a negative area. Across a crossing, the part where the other curve is on top counts as negative and cancels some of the area.

Taught in [applications of integrals](../05-university-core/04-integrals/06-applications-of-integrals.md#edge-cases-and-common-mistakes).

### Squaring after integrating in the disc method

Wrong: $V = \pi\left(\int_0^4 \sqrt{x}\,dx\right)^2 = \pi\left(\frac{16}{3}\right)^2$

Right: $V = \pi\int_0^4 x\,dx = 8\pi$

Square the radius first and integrate afterwards. In the washer method, square each radius separately.

Taught in [applications of integrals](../05-university-core/04-integrals/06-applications-of-integrals.md#edge-cases-and-common-mistakes).

## Convergence, series and Taylor polynomials

### Solving $L = g(L)$ before proving that the limit exists

Wrong: $a_{n+1} = 2a_n$ with $a_1 = 1$ has a limit $L$ with $L = 2L$, so $L = 0$

Right: first show that the sequence is bounded and monotone, and only then solve $L = g(L)$. This sequence is $1, 2, 4, 8, \dots$ and it diverges

The equation $L = g(L)$ describes any limit that exists. It cannot show that one exists.

Taught in [sequences and their limits](../05-university-core/05-sequences-and-series/01-sequences-and-their-limits.md#edge-cases-and-common-mistakes).

### Thinking that terms getting closer together force convergence

Wrong: $a_{n+1} - a_n \to 0$, so the sequence converges

Right: not enough. The sequence $\sqrt{n}$ has $\sqrt{n+1} - \sqrt{n} \to 0$ and still goes to infinity

Closeness of neighbouring terms does not stop the whole sequence from drifting off.

Taught in [sequences and their limits](../05-university-core/05-sequences-and-series/01-sequences-and-their-limits.md#edge-cases-and-common-mistakes).

### Using only one of bounded and monotone

Wrong: the sequence is bounded, so it converges. Or: it is monotone, so it converges

Right: the monotone convergence theorem needs both. The sequence $(-1)^n$ is bounded and does not converge, and $n$ is monotone and does not converge

A bounded monotone sequence cannot wander, and it cannot escape, so it must settle.

Taught in [sequences and their limits](../05-university-core/05-sequences-and-series/01-sequences-and-their-limits.md#edge-cases-and-common-mistakes).

### Concluding that a series converges because its terms tend to 0

Wrong: $\frac{1}{k} \to 0$, so $\sum \frac{1}{k}$ converges

Right: the harmonic series diverges. The $n$-th term test only works in one direction: terms that do not tend to 0 prove divergence

Grouping the terms $\frac{1}{3} + \frac{1}{4}$, then the next four, and so on, shows that $H_{2^m} \ge 1 + \frac{m}{2}$.

Taught in [infinite series basics](../05-university-core/05-sequences-and-series/02-infinite-series-basics.md#edge-cases-and-common-mistakes).

### Starting the geometric series at the wrong index

Wrong: $\sum_{k=1}^{\infty}\left(\frac{1}{2}\right)^k = \frac{1}{1 - \frac{1}{2}} = 2$

Right: $\frac{a}{1 - r}$ uses the first term, which here is $a = \frac{1}{2}$, so the sum is 1

The formula $\frac{1}{1 - r}$ is for a series that starts at $k = 0$. The sum from $k = 1$ is that minus the first term, 1.

Taught in [infinite series basics](../05-university-core/05-sequences-and-series/02-infinite-series-basics.md#edge-cases-and-common-mistakes).

### Reading the ratio test as decisive when $L = 1$

Wrong: the limit of $\left\lvert \frac{a_{k+1}}{a_k} \right\rvert$ is 1, so the series diverges (or converges)

Right: the test gives no information. Both $\sum \frac{1}{k}$ and $\sum \frac{1}{k^2}$ give $L = 1$, and one diverges while the other converges

When $L = 1$, switch to another test, such as the integral test or a comparison.

Taught in [convergence tests](../05-university-core/05-sequences-and-series/03-convergence-tests.md#edge-cases-and-common-mistakes).

### Comparing in the wrong direction

Wrong: $\frac{1}{k^2} \le \frac{1}{k}$ and $\sum \frac{1}{k}$ diverges, so $\sum \frac{1}{k^2}$ diverges

Right: a series smaller than a divergent one proves nothing. Only "smaller than a convergent series converges" and "bigger than a divergent series diverges" are valid

For $\sum \frac{1}{k^2}$, compare with the convergent $\sum \frac{1}{k(k - 1)}$ from $k = 2$ on, or use the $p$-series test.

Taught in [convergence tests](../05-university-core/05-sequences-and-series/03-convergence-tests.md#edge-cases-and-common-mistakes).

### Using the integral test without checking the conditions

Wrong: apply $\int_1^\infty f(x)\,dx$ to any $f$ that matches the terms

Right: $f$ must be positive, continuous and decreasing. The function $\sin^2(\pi x)$ is not decreasing: its series $\sum \sin^2(\pi k)$ is all zeros and converges, while its integral diverges

The integral and the series converge or diverge together only under the three conditions.

Taught in [convergence tests](../05-university-core/05-sequences-and-series/03-convergence-tests.md#edge-cases-and-common-mistakes).

### Taking the sum of the series to be the value of the integral

Wrong: $\int_1^\infty \frac{1}{x^2}\,dx = 1$, so $\sum_{k=1}^\infty \frac{1}{k^2} = 1$

Right: the integral test says only that both converge. The sum is about 1.645, which is between 1 and 2

The remainder after $n$ terms is bounded by $\int_{n+1}^\infty f \le R_n \le \int_n^\infty f$.

Taught in [convergence tests](../05-university-core/05-sequences-and-series/03-convergence-tests.md#edge-cases-and-common-mistakes).

### Trusting a Taylor polynomial far from its centre

Wrong: the degree-4 Taylor polynomial of $e^x$ at 0 gives $e^{-3} \approx 1.375$

Right: $e^{-3} = 0.0498$. The polynomial is accurate only near the centre

Increase the degree or move the centre. For $e^x$, a standard trick is to write $x = m\ln 2 + r$ with $r$ small.

Taught in [power series and Taylor series](../05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md#edge-cases-and-common-mistakes).

### Assuming that the Taylor series always equals the function

Wrong: a function whose Taylor series converges everywhere equals its series

Right: it equals the series only where the remainder $R_n \to 0$. The function $e^{-1/x^2}$ (with value 0 at 0) has Taylor series 0 at 0, and it is not 0 anywhere else

Convergence of the series is not enough.

Taught in [power series and Taylor series](../05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md#edge-cases-and-common-mistakes).

### Forgetting the factorial in the Taylor coefficients

Wrong: the coefficient of $(x - a)^k$ is $f^{(k)}(a)$

Right: it is $\frac{f^{(k)}(a)}{k!}$

Without the $k!$ the series of $e^x$ at 0 would be $1 + x + x^2 + \cdots$, the geometric series.

Taught in [power series and Taylor series](../05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md#edge-cases-and-common-mistakes).

### Forgetting the endpoints of an interval of convergence

Wrong: $\sum \frac{x^k}{k}$ has radius 1, so it converges exactly on $(-1, 1)$

Right: the ratio test finds only the radius. Check each endpoint separately: at $x = -1$ the series converges, at $x = 1$ it is the harmonic series and diverges, so the interval is $[-1, 1)$

The ratio test is silent at the endpoints, because it gives $L = 1$ there. The series for $\ln(1 + x)$ also stops at $x = 1$ and cannot be used at $x = 2$, even though $\ln 3$ exists.

Taught in [power series and Taylor series](../05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md#edge-cases-and-common-mistakes).

## Linear algebra

### Keeping the order in the inverse or transpose of a product

Wrong: $(AB)^{-1} = A^{-1}B^{-1}$ and $(AB)^T = A^TB^T$

Right: $(AB)^{-1} = B^{-1}A^{-1}$ and $(AB)^T = B^TA^T$

To undo "first $B$, then $A$", undo $A$ first and then $B$. For transposes, the sizes force the order: $A^TB^T$ is often not even defined when $B^TA^T$ is.

Taught in [matrix algebra and inverses](../05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md#edge-cases-and-common-mistakes).

### Taking the inverse to be the matrix of reciprocals

Wrong: the inverse of $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ is $\begin{pmatrix} 1 & \frac{1}{2} \\ \frac{1}{3} & \frac{1}{4} \end{pmatrix}$

Right: use the row reduction of $[A \mid I]$, or for a $2 \times 2$ matrix $\frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$

Only a diagonal matrix has an inverse made of reciprocals of the entries.

Taught in [matrix algebra and inverses](../05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md#edge-cases-and-common-mistakes).

### Adding a multiple of a row to itself

Wrong: $R_2 \to R_2 + cR_2$ is a row operation

Right: it scales the row by $1 + c$, which is 0 when $c = -1$ and destroys information. Add a multiple of a different row

An elementary row operation must be reversible, and this one is not always.

Taught in [systems and Gaussian elimination](../05-university-core/06-linear-algebra/02-systems-and-gaussian-elimination.md#edge-cases-and-common-mistakes).

### Expecting infinitely many solutions when there are more unknowns than equations

Wrong: a system with more unknowns than equations always has infinitely many solutions

Right: only if it is consistent. The system $x + y + z = 1$, $x + y + z = 2$ has no solution

A row $[0\ 0\ 0 \mid 1]$ in the reduced matrix means no solution. A homogeneous system with more unknowns than equations always has a nontrivial solution, because it is always consistent.

Taught in [systems and Gaussian elimination](../05-university-core/06-linear-algebra/02-systems-and-gaussian-elimination.md#edge-cases-and-common-mistakes).

### Treating every zero row as a contradiction

Wrong: a row of zeros in the augmented matrix means there is no solution

Right: only a row $[0\ \cdots\ 0 \mid c]$ with $c \ne 0$ is a contradiction. A row $[0\ \cdots\ 0 \mid 0]$ says $0 = 0$, and it just drops out

A zero row means one equation was redundant, and it often means a free variable.

Taught in [systems and Gaussian elimination](../05-university-core/06-linear-algebra/02-systems-and-gaussian-elimination.md#edge-cases-and-common-mistakes).

### Taking pairwise independence to be independence

Wrong: no two of $(1, 0)$, $(0, 1)$ and $(1, 1)$ are multiples of each other, so the list is independent

Right: $(1, 1) = (1, 0) + (0, 1)$, so the list is dependent

A list is independent only if no vector is a combination of the others, which includes combinations of three or more. Row reduce the matrix of the vectors and look for a pivot in every column.

Taught in [linear independence, basis and dimension](../05-university-core/06-linear-algebra/04-linear-independence-basis-and-dimension.md#edge-cases-and-common-mistakes).

### Taking the basis of the column space from the reduced matrix

Wrong: the pivot columns of the RREF form a basis of $\operatorname{col}(A)$

Right: take the pivot columns of $A$ itself, in the positions where the RREF has pivots

Row operations change the column space. They keep the dependencies among the columns, which is why the pivot positions are right.

Taught in [linear independence, basis and dimension](../05-university-core/06-linear-algebra/04-linear-independence-basis-and-dimension.md#edge-cases-and-common-mistakes).

### Cancelling a vector from a dot product

Wrong: $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{w}$, so $\mathbf{v} = \mathbf{w}$

Right: $\mathbf{u} \cdot (\mathbf{v} - \mathbf{w}) = 0$, which says only that $\mathbf{v} - \mathbf{w}$ is perpendicular to $\mathbf{u}$

With $\mathbf{u} = (1, 0)$, the vectors $(2, 5)$ and $(2, -7)$ have the same dot product with $\mathbf{u}$ and are different.

Taught in [vectors, dot product and span](../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md#edge-cases-and-common-mistakes).

### Computing the nullity from the wrong count

Wrong: a $4 \times 6$ matrix of rank 3 has nullity $4 - 3 = 1$

Right: rank-nullity counts columns, so the nullity is $6 - 3 = 3$

The kernel lives in the domain, which has as many entries as the matrix has columns. The image lives in the codomain.

Taught in [linear transformations, kernel and image](../05-university-core/06-linear-algebra/05-linear-transformations-kernel-and-image.md#edge-cases-and-common-mistakes).

### Reading a composition from left to right

Wrong: $BA$ means "apply $B$, then $A$"

Right: $BA$ means apply $A$ first, then $B$, since $(BA)\mathbf{x} = B(A\mathbf{x})$

Read the product of matrices as a composition from the right to the left. Rotating about a point is $TRT^{-1}$, which translates the point to the origin first.

Taught in [linear transformations, kernel and image](../05-university-core/06-linear-algebra/05-linear-transformations-kernel-and-image.md#edge-cases-and-common-mistakes).

### Treating the determinant of a sum as a sum of determinants

Wrong: $\det(A + B) = \det A + \det B$

Right: $\det(AB) = \det A \cdot \det B$, and there is no such rule for sums

The determinant respects products and does not respect sums. With $A = I$ and $B = I$ in $2 \times 2$, $\det(A + B) = 4$ and $\det A + \det B = 2$.

Taught in [determinants](../05-university-core/06-linear-algebra/06-determinants.md#edge-cases-and-common-mistakes).

### Forgetting that scaling a matrix scales the determinant by $c^n$

Wrong: $\det(cA) = c\det A$

Right: for an $n \times n$ matrix, $\det(cA) = c^n \det A$

Every row is multiplied by $c$, and each row contributes one factor of $c$.

Taught in [determinants](../05-university-core/06-linear-algebra/06-determinants.md#edge-cases-and-common-mistakes).

### Multiplying the diagonal of a matrix that is not triangular

Wrong: $\det\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = 1 \cdot 4 = 4$

Right: the diagonal product works for a triangular matrix only. This determinant is $4 - 6 = -2$. Row reduce first, keeping track of swaps and scalings

Sarrus's rule for a $3 \times 3$ matrix does not extend to $4 \times 4$ either. Use cofactors or elimination.

Taught in [determinants](../05-university-core/06-linear-algebra/06-determinants.md#edge-cases-and-common-mistakes).

### Adding projections onto a basis that is not orthogonal

Wrong: project $\mathbf{y}$ onto each of $\mathbf{u}_1$ and $\mathbf{u}_2$ separately and add, when $\mathbf{u}_1 \cdot \mathbf{u}_2 \ne 0$

Right: first apply Gram-Schmidt to get an orthogonal basis, or solve the normal equations

The shadows on non-perpendicular directions overlap, so adding them counts some of the vector twice.

Taught in [orthogonality, projections and least squares](../05-university-core/06-linear-algebra/07-orthogonality-projections-and-least-squares.md#edge-cases-and-common-mistakes).

### Calling a matrix with orthogonal columns an orthogonal matrix

Wrong: the columns $(1, 1)$ and $(1, -1)$ are orthogonal, so the matrix is orthogonal and $Q^{-1} = Q^T$

Right: an orthogonal matrix has orthonormal columns. Here $Q^TQ = 2I$, so the columns must be divided by their length $\sqrt{2}$

Orthogonal columns of any length are not enough. The columns must also have length 1.

Taught in [orthogonality, projections and least squares](../05-university-core/06-linear-algebra/07-orthogonality-projections-and-least-squares.md#edge-cases-and-common-mistakes).

### Fitting a line without a column of ones

Wrong: fit $y = a + bx$ using only the column of $x$ values in $A$

Right: include a column of ones for the intercept $a$

Without it the fit is a line through the origin, the slope changes, and the residuals need not add to 0. With the column of ones, the residuals add to 0 and the line passes through $(\bar{x}, \bar{y})$.

Taught in [orthogonality, projections and least squares](../05-university-core/06-linear-algebra/07-orthogonality-projections-and-least-squares.md#edge-cases-and-common-mistakes).

### Accepting the zero vector as an eigenvector

Wrong: $A\mathbf{0} = \lambda\mathbf{0}$, so $\mathbf{0}$ is an eigenvector for every $\lambda$

Right: an eigenvector must be nonzero. An eigenvalue is a number $\lambda$ for which some nonzero $\mathbf{v}$ has $A\mathbf{v} = \lambda\mathbf{v}$

If $\mathbf{0}$ were allowed, every number would be an eigenvalue of every matrix.

Taught in [eigenvalues and eigenvectors](../05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md#edge-cases-and-common-mistakes).

### Reading eigenvalues off a row-reduced matrix

Wrong: row reduce $A$ to a triangular matrix and read the eigenvalues from its diagonal

Right: that works only if $A$ is triangular to begin with. Row operations change the eigenvalues, so solve $\det(A - \lambda I) = 0$

For a triangular matrix, the eigenvalues are the diagonal entries as it stands.

Taught in [eigenvalues and eigenvectors](../05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md#edge-cases-and-common-mistakes).

### Assuming that a repeated eigenvalue gives a diagonalizable matrix

Wrong: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has eigenvalue 1 twice, so it has two eigenvectors and is diagonalizable

Right: it has only one independent eigenvector, so it is not diagonalizable

A matrix is diagonalizable exactly when it has $n$ independent eigenvectors. Count them for each eigenvalue.

Taught in [eigenvalues and eigenvectors](../05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md#edge-cases-and-common-mistakes).

## Probability

### Believing that probability 0 means impossible

Wrong: a point chosen uniformly from a square has probability 0 of hitting any given location, so it cannot hit it

Right: probability 0 means impossible only for the empty event. Every single point of a continuous sample space has probability 0, and some point is hit anyway

Probabilities for continuous outcomes are areas. A set of zero area has probability 0 without being empty.

Taught in [sample spaces, events and axioms](../05-university-core/07-probability/01-sample-spaces-events-and-axioms.md#edge-cases-and-common-mistakes).

### Leaving out the denominator in Bayes' theorem

Wrong: a test with 90% sensitivity and a 1% base rate gives a posterior of $0.9 \times 0.01 = 0.9\%$, or the posterior is 90%

Right: divide by $P(E)$. With a 5% false positive rate, $P(E) = 0.9(0.01) + 0.05(0.99) = 0.0585$ and the posterior is $\frac{0.009}{0.0585} \approx 0.154$

The denominator includes the false positives from the large group without the condition. Skipping it gives a number that is not a probability, and ignoring the base rate gives 90%, which is the base rate fallacy.

Taught in [conditional probability and Bayes' theorem](../05-university-core/07-probability/02-conditional-probability-and-bayes.md#edge-cases-and-common-mistakes).

### Answering the Monty Hall problem with one half

Wrong: two doors are left, so each has probability $\frac{1}{2}$

Right: switching wins with probability $\frac{2}{3}$ when the host knows where the car is and always opens a goat door

The host's choice depends on the car's position, so it carries information. If the host opens a door at random and happens to show a goat, the probability is $\frac{1}{2}$. Simulating the game settles it.

Taught in [conditional probability and Bayes' theorem](../05-university-core/07-probability/02-conditional-probability-and-bayes.md#example-3-the-monty-hall-problem).

### Taking the expected square to be the square of the expected value

Wrong: $E[X^2] = (E[X])^2$

Right: $E[X^2] = \operatorname{Var}(X) + (E[X])^2$

The two are equal only when the variance is 0. For a fair die, $E[X^2] = \frac{91}{6} \approx 15.17$ and $(E[X])^2 = 12.25$.

Taught in [discrete random variables](../05-university-core/07-probability/03-discrete-random-variables.md#edge-cases-and-common-mistakes).

### Reading a density value as a probability

Wrong: the density of a uniform variable on $[0, 0.5]$ is 2, so the probability of a value is 2

Right: only areas under the density are probabilities. A density value can exceed 1

The probability of an interval is the area over it. The density is the probability per unit length.

Taught in [continuous random variables and the normal distribution](../05-university-core/07-probability/04-continuous-random-variables-and-the-normal.md#edge-cases-and-common-mistakes).

### Passing the variance where software wants the standard deviation

Wrong: `NormalDist(100, 225)` for a mean of 100 and a variance of 225

Right: `NormalDist(100, 15)`, since the second argument is $\sigma$

The notation $N(\mu, \sigma^2)$ writes the variance, and most software takes the standard deviation. Check which one the function expects.

Taught in [continuous random variables and the normal distribution](../05-university-core/07-probability/04-continuous-random-variables-and-the-normal.md#edge-cases-and-common-mistakes).

### Using the table's left-hand area for "above"

Wrong: $P(Z > 1.5) = \Phi(1.5) = 0.933$

Right: $P(Z > 1.5) = 1 - \Phi(1.5) = 0.067$

The standard normal table and `cdf` give the area to the left of $z$, so $P(Z \le z)$. For an upper tail, subtract from 1.

Taught in [continuous random variables and the normal distribution](../05-university-core/07-probability/04-continuous-random-variables-and-the-normal.md#edge-cases-and-common-mistakes).

### Subtracting variances for a difference

Wrong: $\operatorname{Var}(X - Y) = \operatorname{Var}(X) - \operatorname{Var}(Y)$

Right: for independent variables, $\operatorname{Var}(X - Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$

Both sources of noise feed into the difference. A variance cannot be negative, and the wrong formula can make it so.

Taught in [joint distributions, covariance and sums](../05-university-core/07-probability/05-joint-distributions-covariance-and-sums.md#edge-cases-and-common-mistakes).

### Adding standard deviations of independent variables

Wrong: standard deviations 4 and 3 combine to give $4 + 3 = 7$

Right: variances add, so the standard deviation is $\sqrt{16 + 9} = 5$

Independent errors partly cancel, so the total is smaller than the sum of the standard deviations.

Taught in [joint distributions, covariance and sums](../05-university-core/07-probability/05-joint-distributions-covariance-and-sums.md#edge-cases-and-common-mistakes).

### Concluding independence from zero covariance

Wrong: $\operatorname{Cov}(X, Y) = 0$, so $X$ and $Y$ are independent

Right: independent variables have zero covariance, and the converse is false. If $X$ is $-1$, $0$ or $1$ with equal probability, then $Y = X^2$ is fully determined by $X$ and still has $\operatorname{Cov}(X, Y) = 0$

Covariance measures only the linear part of the dependence.

Taught in [joint distributions, covariance and sums](../05-university-core/07-probability/05-joint-distributions-covariance-and-sums.md#edge-cases-and-common-mistakes).

### Expecting the law of large numbers to even out the counts

Wrong: after a run of heads, the number of tails will catch up, so the count of heads minus tails shrinks

Right: the average converges, and the difference between the counts typically grows like $\sqrt{n}$

The proportion approaches $\frac{1}{2}$ because the total grows faster than the difference does. The early run is diluted, not corrected.

Taught in [the law of large numbers and the CLT](../05-university-core/07-probability/06-law-of-large-numbers-and-clt.md#edge-cases-and-common-mistakes).

### Thinking that the central limit theorem makes the data normal

Wrong: with 1000 observations, the data are approximately normal

Right: the average (or sum) of many i.i.d. values is approximately normal, and the data keep their own shape

A histogram of skewed data stays skewed however many points there are. The theorem is about the sampling distribution of the mean.

Taught in [the law of large numbers and the CLT](../05-university-core/07-probability/06-law-of-large-numbers-and-clt.md#edge-cases-and-common-mistakes).

### Applying the central limit theorem to a distribution with no variance

Wrong: the average of Cauchy variables is approximately normal for large $n$

Right: the theorem needs a finite variance. The average of $n$ standard Cauchy variables is again standard Cauchy

Averaging does not help here, because extreme values are too common. The law of large numbers fails for the same reason.

Taught in [the law of large numbers and the CLT](../05-university-core/07-probability/06-law-of-large-numbers-and-clt.md#edge-cases-and-common-mistakes).

## Inference and regression

### Dividing by $n$ for a sample variance

Wrong: $s^2 = \frac{1}{n}\sum (x_i - \bar{x})^2$ for a sample

Right: $s^2 = \frac{1}{n - 1}\sum (x_i - \bar{x})^2$

The sample mean is closer to the data than the population mean is, so the squares come out too small on average. Dividing by $n - 1$ corrects it exactly, which is what makes $s^2$ unbiased.

Taught in [descriptive statistics and study design](../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md#edge-cases-and-common-mistakes).

### Flagging outliers with $\lvert z \rvert > 3$ in a small sample

Wrong: no point in a sample of 10 has $\lvert z \rvert > 3$, so there are no outliers

Right: use the IQR fences. In a sample of $n$, $\lvert z \rvert$ can never exceed $\frac{n - 1}{\sqrt{n}}$, which is 2.85 for $n = 10$

The outlier itself inflates $s$, so it hides from the rule. A boxplot and the IQR fences do not have this problem.

Taught in [descriptive statistics and study design](../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md#edge-cases-and-common-mistakes).

### Believing that a bigger sample fixes a biased one

Wrong: the survey reached 2.4 million people, so it must be accurate

Right: more data shrinks random error and leaves bias where it was

A flaw in who is chosen, or in who answers, affects every response in the same direction. Random sampling is what protects against it.

Taught in [descriptive statistics and study design](../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md#edge-cases-and-common-mistakes).

### Reading a 95% interval as a 95% probability

Wrong: there is a 95% probability that the true mean is in $(48.2, 51.8)$

Right: 95% of intervals built this way capture the true mean. This particular interval either does or does not

The parameter is fixed and the interval is random. After the data are in, the probability statement no longer applies.

Taught in [confidence intervals](../05-university-core/08-statistics/02-confidence-intervals.md#edge-cases-and-common-mistakes).

### Reading an interval for the mean as a range for individual values

Wrong: the 95% interval for the mean is $(48.2, 51.8)$, so 95% of people fall in that range

Right: the interval is for the mean. Individual values spread out by about $s$, and the interval's width shrinks like $\frac{1}{\sqrt{n}}$

The standard error shrinks with more data, but the spread of individuals does not.

Taught in [confidence intervals](../05-university-core/08-statistics/02-confidence-intervals.md#edge-cases-and-common-mistakes).

### Using the normal critical value with a small sample and an estimated spread

Wrong: for $n = 8$ and an estimated $s$, use $z^* = 1.96$

Right: use $t^*$ with $n - 1 = 7$ degrees of freedom, which is 2.365 for 95%

Replacing $\sigma$ by $s$ adds uncertainty, so the tails are heavier. The $t$ value approaches 1.96 as $n$ grows.

Taught in [confidence intervals](../05-university-core/08-statistics/02-confidence-intervals.md#edge-cases-and-common-mistakes).

### Concluding that there is no difference because two intervals overlap

Wrong: the intervals for the two means overlap, so the difference is not significant

Right: build one interval for the difference. Its standard error is $\sqrt{\text{SE}_1^2 + \text{SE}_2^2}$, which is less than $\text{SE}_1 + \text{SE}_2$

Two intervals can overlap a little while the interval for the difference excludes 0.

Taught in [confidence intervals](../05-university-core/08-statistics/02-confidence-intervals.md#edge-cases-and-common-mistakes).

### Reading the p-value as the probability that the null hypothesis is true

Wrong: $p = 0.03$ means a 3% chance that $H_0$ is true

Right: $p$ is the probability of data this extreme if $H_0$ were true, so $P(\text{data} \mid H_0)$

The probability of $H_0$ given the data is a different quantity, and it needs a prior, as Bayes' theorem does.

Taught in [hypothesis testing](../05-university-core/08-statistics/03-hypothesis-testing.md#what-a-p-value-is-not).

### Treating "fail to reject" as proof of no effect

Wrong: $p = 0.2$, so there is no effect

Right: the data do not rule out an effect. A low-power test misses real effects

Report the interval for the effect size too. A wide interval around 0 says that the study was uninformative.

Taught in [hypothesis testing](../05-university-core/08-statistics/03-hypothesis-testing.md#edge-cases-and-common-mistakes).

### Using the one-tail area as a two-sided p-value

Wrong: the statistic $z = 2.1$ has a one-tail area of 0.018, so $p = 0.018$

Right: for a two-sided alternative, double it: $p = 0.036$

Both tails count when the alternative is "different from".

Taught in [hypothesis testing](../05-university-core/08-statistics/03-hypothesis-testing.md#edge-cases-and-common-mistakes).

### Running many tests and reporting the significant one

Wrong: test 20 outcomes at the 0.05 level and report the one with $p = 0.03$

Right: correct for multiple testing with Bonferroni or Holm, or state the single test before looking at the data

If all 20 nulls are true, the chance of at least one false positive is $1 - 0.95^{20} \approx 0.64$.

Taught in [hypothesis testing](../05-university-core/08-statistics/03-hypothesis-testing.md#edge-cases-and-common-mistakes).

### Taking a tiny p-value to mean a big effect

Wrong: $p < 0.0001$, so the effect is important

Right: report the effect size with an interval. With a huge $n$, a tiny difference is significant

The p-value answers whether an effect is distinguishable from 0, not how large it is.

Taught in [hypothesis testing](../05-university-core/08-statistics/03-hypothesis-testing.md#edge-cases-and-common-mistakes).

### Trusting $r$ or $R^2$ without a plot

Wrong: $r = 0.82$, so a straight line describes the data

Right: plot the data and the residuals first. Anscombe's quartet has four very different data sets with the same $r$ and the same line

A curved pattern, a single influential point or two clusters can all give a high $r$. A U-shape in the residuals shows that a line is the wrong model.

Taught in [correlation and linear regression](../05-university-core/08-statistics/04-correlation-and-linear-regression.md#edge-cases-and-common-mistakes).

### Ignoring a high-leverage point

Wrong: report the fitted line without checking which points control it

Right: fit with and without the point, and report both if the slope changes much

A point whose $x$ is far from $\bar{x}$ pulls the line toward itself. One such point can change the slope a lot.

Taught in [correlation and linear regression](../05-university-core/08-statistics/04-correlation-and-linear-regression.md#edge-cases-and-common-mistakes).

### Inverting the line of $y$ on $x$ to predict $x$

Wrong: the line $\hat{y} = 3 + 2x$ gives $x = \frac{y - 3}{2}$ as the prediction of $x$ from $y$

Right: regress $x$ on $y$ to get a different line

The slope of $y$ on $x$ is $r\frac{s_y}{s_x}$ and the slope of $x$ on $y$ is $r\frac{s_x}{s_y}$, and the two slopes multiply to $r^2$, not 1.

Taught in [correlation and linear regression](../05-university-core/08-statistics/04-correlation-and-linear-regression.md#edge-cases-and-common-mistakes).

### Reading a drop after an extreme score as a real change

Wrong: the class with the lowest scores improved after the new method, so the method works

Right: part of an extreme score is luck, and luck does not repeat, so scores move toward the average anyway (regression to the mean)

Compare with a control group that did not get the method.

Taught in [correlation and linear regression](../05-university-core/08-statistics/04-correlation-and-linear-regression.md#edge-cases-and-common-mistakes).

## Multivariable calculus

### Taking the angle in polar coordinates from the arctangent alone

Wrong: for the point $(-1, 1)$, $\theta = \arctan\frac{y}{x} = -45^\circ$

Right: the point is in the second quadrant, so $\theta = 135^\circ$. Pick the quadrant, or use `atan2(y, x)`

The arctangent returns angles between $-90^\circ$ and $90^\circ$ only.

Taught in [parametric, polar and 3D coordinates](../05-university-core/09-multivariable-calculus-light/01-parametric-polar-and-3d-coordinates.md#edge-cases-and-common-mistakes).

### Reading the derivative with respect to time as the slope

Wrong: for a parametric curve, the slope is $\frac{dy}{dt}$

Right: the slope is $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$

The quantity $\frac{dy}{dt}$ is the vertical speed, and the two have different units.

Taught in [parametric, polar and 3D coordinates](../05-university-core/09-multivariable-calculus-light/01-parametric-polar-and-3d-coordinates.md#edge-cases-and-common-mistakes).

### Leaving out the one half in a polar area

Wrong: the area of the circle $r = 2$ is $\int_0^{2\pi} r^2\,d\theta = 8\pi$

Right: area $= \frac{1}{2}\int_0^{2\pi} r^2\,d\theta = 4\pi$

A thin sector is a triangle with area $\frac{1}{2}r^2\,d\theta$, not a rectangle.

Taught in [parametric, polar and 3D coordinates](../05-university-core/09-multivariable-calculus-light/01-parametric-polar-and-3d-coordinates.md#edge-cases-and-common-mistakes).

### Assuming that existing partial derivatives mean continuity

Wrong: $f_x$ and $f_y$ exist at the origin, so $f$ is continuous there

Right: not implied. The function $\frac{xy}{x^2 + y^2}$, with value 0 at the origin, has both partials 0 there and is not continuous: along $y = x$ it equals $\frac{1}{2}$

Partial derivatives look only along the axes.

Taught in [partial derivatives and the gradient](../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md#edge-cases-and-common-mistakes).

### Using a direction vector that is not a unit vector

Wrong: for $f = x^2y$ at $(1, 2)$ in the direction $(3, 4)$, the directional derivative is $\nabla f \cdot (3, 4) = (4, 1) \cdot (3, 4) = 16$

Right: divide by the length 5 first: $(4, 1) \cdot (0.6, 0.8) = 3.2$

The directional derivative is a rate per unit distance, so the direction must have length 1. The wrong answer is too large by the length of the vector.

Taught in [partial derivatives and the gradient](../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md#edge-cases-and-common-mistakes).

### Taking the slope of a level curve to be $\frac{f_x}{f_y}$

Wrong: the slope of $x^2 + y^2 = c$ is $\frac{f_x}{f_y} = \frac{x}{y}$

Right: the slope is $-\frac{f_x}{f_y} = -\frac{x}{y}$

Differentiating $f(x, y) = c$ implicitly gives $f_x + f_y\frac{dy}{dx} = 0$. The sign matters: the tangent to a circle is perpendicular to the radius.

Taught in [partial derivatives and the gradient](../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md#edge-cases-and-common-mistakes).

### Reading $D = 0$ as a saddle point

Wrong: the Hessian determinant is 0, so the critical point is a saddle

Right: the test gives no information. Both $x^4 + y^4$ (a minimum) and $x^3 + y^3$ (a saddle) have $D = 0$ at the origin

When $D = 0$, look at the function near the point directly.

Taught in [multivariable optimization and Lagrange multipliers](../05-university-core/09-multivariable-calculus-light/03-multivariable-optimization-and-lagrange-multipliers.md#edge-cases-and-common-mistakes).

### Missing the points where the constraint's gradient is zero

Wrong: solve $\nabla f = \lambda\nabla g$ and $g = c$, and list the solutions as all the candidates

Right: also check the points of the constraint where $\nabla g = \mathbf{0}$. To minimize $f = x$ on $y^2 = x^3$, the minimum is at the origin, where $\nabla g = (0, 0)$, and the Lagrange equations have no solution there

At those points the condition $\nabla f = \lambda\nabla g$ cannot hold unless $\nabla f$ is also zero.

Taught in [multivariable optimization and Lagrange multipliers](../05-university-core/09-multivariable-calculus-light/03-multivariable-optimization-and-lagrange-multipliers.md#edge-cases-and-common-mistakes).

### Forgetting the factor $r$ in a polar double integral

Wrong: $\iint f\,dA = \iint f\,dr\,d\theta$

Right: $\iint f\,r\,dr\,d\theta$

A small polar patch has width $dr$ and length $r\,d\theta$, so its area is $r\,dr\,d\theta$.

Taught in [double integrals](../05-university-core/09-multivariable-calculus-light/04-double-integrals.md#edge-cases-and-common-mistakes).

### Swapping the order of integration without a sketch

Wrong: swap the limits of $\int_0^1\int_0^x f\,dy\,dx$ to $\int_0^1\int_0^x f\,dx\,dy$

Right: sketch the region (here $0 \le y \le x \le 1$) and read off the new limits: $\int_0^1\int_y^1 f\,dx\,dy$

The limits come from the region. Swapping the symbols does not change the region.

Taught in [double integrals](../05-university-core/09-multivariable-calculus-light/04-double-integrals.md#edge-cases-and-common-mistakes).

## Differential equations

### Separating an equation that is not separable

Wrong: separate $y' = t + y$ into $\frac{dy}{dt} = t + y$ and integrate each side with respect to its own variable

Right: it is first-order linear. Use an integrating factor to get $y = Ce^t - t - 1$

An equation is separable only if the right side is a product $g(t)h(y)$, not a sum.

Taught in [first-order differential equations](../05-university-core/10-differential-equations-light/01-first-order-differential-equations.md#edge-cases-and-common-mistakes).

### Losing a constant solution by dividing by $y$

Wrong: separate $y' = y(1 - y)$ by dividing by $y(1 - y)$, and say the answer is the family found

Right: list the constant solutions $y = 0$ and $y = 1$ first. Dividing by $y$ removes $y = 0$ from consideration

The family found by integrating may not include the equilibria.

Taught in [first-order differential equations](../05-university-core/10-differential-equations-light/01-first-order-differential-equations.md#edge-cases-and-common-mistakes).

### Taking an Euler step that is too large

Wrong: use $h = 1$ for $y' = -3y$ because the step is easy to compute

Right: the method needs $h < \frac{2}{\lambda} = 0.67$ here. With $h = 1$ each step multiplies $y$ by $-2$, and the numbers blow up with alternating sign

This is the same limit as the learning rate in gradient descent.

Taught in [first-order differential equations](../05-university-core/10-differential-equations-light/01-first-order-differential-equations.md#edge-cases-and-common-mistakes).

### Writing $(C_1 + C_2)e^{rt}$ for a double root

Wrong: the characteristic equation has a double root $r$, so the general solution is $(C_1 + C_2)e^{rt}$

Right: $(C_1 + C_2t)e^{rt}$

The sum $C_1 + C_2$ is one constant in disguise, and one constant cannot fit two initial conditions.

Taught in [second-order linear equations](../05-university-core/10-differential-equations-light/02-second-order-linear-equations.md#edge-cases-and-common-mistakes).

### Dropping the growth factor for complex roots

Wrong: roots $-1 \pm 2i$ give $y = C_1\cos 2t + C_2\sin 2t$

Right: $y = e^{-t}\left(C_1\cos 2t + C_2\sin 2t\right)$

The real part of the root gives the factor $e^{\alpha t}$. Without it the oscillation never fades.

Taught in [second-order linear equations](../05-university-core/10-differential-equations-light/02-second-order-linear-equations.md#edge-cases-and-common-mistakes).

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

## CS math

### Negating in two's complement by flipping the bits only

Wrong: in 8 bits, $-5$ is $5 = 00000101$ with every bit flipped, $11111010$.

Right: flip the bits and add 1, so $-5$ is $11111011$.

Flipping alone gives the one's complement, which is one too small.

Taught in [binary arithmetic and two's complement](../06-cs-math/01-number-representation/03-binary-arithmetic-and-twos-complement.md#edge-cases-and-common-mistakes).

### Cancelling a common factor in a congruence

Wrong: Cancelling a common factor in a congruence, $6 \cdot 2 \equiv 6 \cdot 4$ so $2 \equiv 4 \pmod{12}$

Right: Divide the modulus too: $2 \equiv 4 \pmod{2}$

The factor and the modulus share a divisor, so it is not invertible.

Taught in [divisibility and modular arithmetic](../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md#edge-cases-and-common-mistakes).

### Reducing the exponent mod $n$

Wrong: Computing $a^e \bmod n$ by reducing the exponent mod $n$

Right: Reduce the base mod $n$, and the exponent only mod $\varphi(n)$ when $\gcd(a, n) = 1$

The exponent counts multiplications, not residues.

Taught in [Fermat, Euler and fast exponentiation](../06-cs-math/02-number-theory/05-fermat-euler-and-fast-exponentiation.md#edge-cases-and-common-mistakes).

### Using the wrong sign in the characteristic equation

Wrong: Using the characteristic equation $r^2 + c_1 r + c_2 = 0$ for $a_n = c_1 a_{n-1} + c_2 a_{n-2}$

Right: $r^2 - c_1 r - c_2 = 0$

Substituting $a_n = r^n$ and dividing by $r^{n-2}$ gives $r^2 = c_1 r + c_2$

Taught in [recurrences](../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md#edge-cases-and-common-mistakes).

### Treating any graph with $n - 1$ edges as a tree

Wrong: Believing any graph with $n - 1$ edges is a tree.

Right: Check connected with $n - 1$ edges, or acyclic with $n - 1$ edges.

A triangle plus an isolated vertex has 3 edges on 4 vertices and is not a tree.

Taught in [paths, connectivity and trees](../06-cs-math/05-graphs/02-paths-connectivity-and-trees.md#edge-cases-and-common-mistakes).

### Using $E \le 3V - 6$ to prove a graph is planar

Wrong: Using $E \le 3V - 6$ to prove a graph is planar.

Right: Use it only to prove a graph is not planar.

The bound is necessary, not sufficient.

Taught in [bipartite graphs, colouring and planar graphs](../06-cs-math/05-graphs/03-bipartite-coloring-and-planar-graphs.md#edge-cases-and-common-mistakes).

### Confusing "does not accept" with "rejects"

Wrong: Treating "the machine does not accept" as "the machine rejects".

Right: A recognizer may loop, and only a decider always halts.

Looping is a third outcome besides accept and reject.

Taught in [turing machines and the Church-Turing thesis](../06-cs-math/06-theory-of-computation/04-turing-machines-and-church-turing-thesis.md#edge-cases-and-common-mistakes).

### Reducing in the wrong direction to prove undecidability

Wrong: Reducing $B$ to a known undecidable $A$ to prove $B$ undecidable.

Right: Reduce the known undecidable $A$ to $B$

A reduction transfers decidability from $B$ to $A$, so it must start at the known hard problem.

Taught in [reductions and undecidability](../06-cs-math/06-theory-of-computation/06-reductions-and-undecidability.md#edge-cases-and-common-mistakes).

### Using the pumping lemma to show a language is regular

Wrong: Using the pumping lemma to show a language is regular.

Right: Use it only to show a language is not regular.

The lemma is necessary, not sufficient.

Taught in [regular expressions and the pumping lemma](../06-cs-math/06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md#edge-cases-and-common-mistakes).

## Economics math

### Calling a percentage point change a percent change

Wrong: A rate rising from 4% to 5% is "up 1%".

Right: Up 1 percentage point, or up 25% relative.

Points are a difference of rates, percent is a ratio.

Taught in [percent change vs percentage points](../07-economics-math/01-measuring-the-economy/02-percent-change-vs-percentage-points.md#edge-cases-and-common-mistakes).

### Reading a CPI level as an inflation rate

Wrong: A CPI of 170.0 means 170% inflation.

Right: Inflation is the percent change in the CPI between two dates.

The index level depends on the base period.

Taught in [CPI and inflation](../07-economics-math/01-measuring-the-economy/07-cpi-and-inflation.md#edge-cases-and-common-mistakes).

### Confusing absolute and comparative advantage

Wrong: A producer who needs fewer hours for both goods has the comparative advantage in both.

Right: Compare opportunity costs, and nobody has it in both.

Fewer hours is absolute advantage.

Taught in [comparative advantage and gains from trade](../07-economics-math/02-markets/02-comparative-advantage-and-gains-from-trade.md#edge-cases-and-common-mistakes).

### Thinking the taxed side pays the tax

Wrong: The person the law taxes pays the tax.

Right: The burden splits by the slopes (or elasticities) of supply and demand.

Price adjusts so both sides share it.

Taught in [surplus and market interventions](../07-economics-math/02-markets/04-surplus-and-market-interventions.md#edge-cases-and-common-mistakes).

### Setting price equal to marginal cost for a monopolist

Wrong: A monopolist sets p = MC.

Right: A monopolist sets MR = MC, and price is read off the demand curve.

Selling one more unit lowers the price on every unit, so MR is below p.

Taught in [profit maximization and market structure](../07-economics-math/03-firms-and-consumers/03-profit-maximization-and-market-structure.md#edge-cases-and-common-mistakes).

### Using the spending multiplier for a tax change

Wrong: The tax multiplier is 1/(1 - b).

Right: -b/(1 - b) for a lump-sum tax.

Part of a tax change comes out of saving, so the effect is smaller than a spending change by the factor b.

Taught in [multipliers and the AD-AS model](../07-economics-math/04-more-tools/02-multipliers-and-the-ad-as-model.md#edge-cases-and-common-mistakes).

### Treating a significant coefficient as causal

Wrong: A significant regression coefficient is a causal effect.

Right: It is causal only if the error is unrelated to x, and omitted variables bias it by beta_2 times delta_1.

Significance measures noise, not confounding.

Taught in [regression and econometrics intuition](../07-economics-math/04-more-tools/03-regression-and-econometrics-intuition.md#edge-cases-and-common-mistakes).

## Financial math

### Adding discounts

Wrong: 20% off then 10% off is 30% off.

Right: It is $0.8 \times 0.9 = 0.72$, so 28% off.

Each discount applies to the already reduced price, so they multiply.

Taught in [tips, discounts and HST](../08-financial-math/01-everyday-money/01-tips-discounts-and-hst.md#edge-cases-and-common-mistakes).

### Comparing nominal rates

Wrong: 5% compounded monthly and 5% compounded annually are the same rate.

Right: Compare effective annual rates, 5.1162% against 5%.

More frequent compounding earns interest on interest sooner.

Taught in [APR, APY and the effective annual rate](../08-financial-math/02-interest-and-growth/03-apr-apy-and-effective-annual-rate.md#edge-cases-and-common-mistakes).

### Annual rate with monthly periods

Wrong: Use $i = 0.048$ with $n = 36$ months.

Right: Use $i = 0.004$ with $n = 36$, or $i = 0.048$ with $n = 3$ years.

The rate and the number of periods must use the same unit.

Taught in [present and future value](../08-financial-math/03-time-value-of-money/01-present-and-future-value.md#edge-cases-and-common-mistakes).

### Dividing a Canadian mortgage rate by 12

Wrong: Monthly rate is the quoted fixed rate divided by 12.

Right: $i = (1 + j/2)^{1/6} - 1$, because fixed rates compound semi-annually.

Interest Act section 6 and market practice quote fixed rates with semi-annual compounding.

Taught in [canadian mortgage compounding](../08-financial-math/05-housing/04-canadian-mortgage-compounding.md#edge-cases-and-common-mistakes).

### Average return as growth rate

Wrong: Gains of +30% and -10% average 10%, so money grows 10% a year.

Right: The growth rate is the geometric mean, about 8.17% a year.

Returns multiply, and the arithmetic mean is at least the geometric mean.

Taught in [investing returns and risk](../08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk.md#edge-cases-and-common-mistakes).

### Taxing all income at the top rate

Wrong: The marginal rate applies to your whole income.

Right: Each rate applies only to the slice of income inside its bracket.

Tax is piecewise linear, so a raise never lowers take-home pay.

Taught in [income tax brackets: marginal vs effective](../08-financial-math/07-taxes-insurance-and-planning/01-income-tax-brackets-marginal-vs-effective.md#edge-cases-and-common-mistakes).

### Treating the minimum payment as a plan

Wrong: Paying the minimum clears the card in reasonable time.

Right: \$2,000 at 18% with the higher of \$10 or 3% takes 166 months and \$1,798.88 interest.

The payment shrinks with the balance, so the balance decays only slowly.

Taught in [credit cards and the minimum payment trap](../08-financial-math/04-borrowing/04-credit-cards-and-the-minimum-payment-trap.md#edge-cases-and-common-mistakes).
