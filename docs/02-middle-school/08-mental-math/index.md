# Mental math

Adding, subtracting, multiplying, dividing and working with percents and money without paper, with the reason behind each trick.

1. [Mental addition and subtraction](01-mental-addition-and-subtraction.md)
2. [Mental multiplication and division](02-mental-multiplication-and-division.md)
3. [Percents, fractions and money in your head](03-percents-fractions-and-money-in-your-head.md)

## Cheat sheet

### Mental addition and subtraction

Work left to right with a running total: say the whole total after each piece, and forget the old one.

| Task | Method | Example |
|---|---|---|
| Add | split the second number by place value, biggest piece first | $4{,}568 + 2{,}739$ gives 6,568, 7,268, 7,298, 7,307 |
| Add a number just under a round one | round, add, take the move back | $398 + 247 = 400 + 247 - 2 = 645$ |
| Subtract a number just under a round one | round, subtract, give the move back | $703 - 298 = 703 - 300 + 2 = 405$ |
| Subtract, or make change | count up in round jumps and add the jumps | \$20 minus \$13.65: 35 cents to \$14, then \$6 to \$20, so \$6.35 |
| Subtract left to right | take off the pieces of the lower number, biggest first | $842 - 359$ gives 542, 492, 483 |
| Subtract from a power of ten | every digit from 9, the last nonzero digit from 10, trailing zeros stay | $10{,}000 - 3{,}070 = 6{,}930$ |
| Add a column of prices | round each up, add, subtract the cents you added | \$24.50 minus 7 cents is \$24.43 for \$3.99, \$12.49 and \$7.95 |

- Round and adjust: $a + b = (a + c) + b - c$. If you added too much, take it back, and if you took away too much, give it back.
- Counting up: for $b \le m \le a$, $a - b = (m - b) + (a - m)$.
- Near doubles and bridges move an amount between addends: $47 + 49 = 48 + 48$, and $87 + 76 = 100 + 63$.
- Check with size, the last digit and casting out nines. Casting out nines misses swapped digits, and size misses a slip of 10 or 100.

Main mistakes:

- Losing a carry in the running total. Say the whole total each time.
- Fixing in the wrong direction: $1{,}203 - 998$ is $1{,}203 - 1{,}000 + 2$, not $- 2$.
- Using "all from 9" on trailing zeros: $1{,}000 - 640$ is 360, not 359.
- Forgetting the cents added by rounding in a column of prices.
- Losing the sign when counting up: $637 - 1{,}000 = -363$.

### Mental multiplication and division

Split one factor and keep a running total, or use a friendly factor.

| Multiply by | Do this | Example |
|---|---|---|
| $5$ | times 10, then halve | $68 \times 5 = 680 \div 2 = 340$ |
| $25$ | times 100, then halve twice | $36 \times 25 = 3{,}600 \div 4 = 900$ |
| $125$ | times 1,000, then halve three times | $48 \times 125 = 6{,}000$ |
| $9$, $99$ | times 10 or 100, subtract the number | $47 \times 99 = 4{,}700 - 47 = 4{,}653$ |
| $11$ | times 10, add the number (digits $a$, $a + b$, $b$, with a carry) | $68 \times 11 = 748$ |
| $15$ | times 10, add half of that | $46 \times 15 = 460 + 230 = 690$ |
| $75$ | times 100, take off a quarter | $84 \times 75 = 8{,}400 - 2{,}100 = 6{,}300$ |

- Distributive property: $a(b + c) = ab + ac$ and $a(b - c) = ab - ac$. A two-digit product has four partial products.
- Halve and double: $ab = \frac{a}{2} \times 2b$, so $35 \times 18 = 70 \times 9 = 630$.
- Difference of squares: $(m - d)(m + d) = m^2 - d^2$, so $47 \times 53 = 50^2 - 3^2 = 2{,}491$. Add the two numbers and halve to find $m$.
- Any square: $n^2 = (n - d)(n + d) + d^2$. Near 50, $(50 + d)^2 = 100(25 + d) + d^2$. Near 100, $(100 + d)^2 = 100(100 + 2d) + d^2$. So $53^2 = 2{,}809$ and $96^2 = 9{,}216$.
- Same tens digit and ones digits that add to 10: $43 \times 47 = 4 \times 5$ then $3 \times 7$, so 2,021.
- Divide by 5 as double then $\div 10$, by 25 as times 4 then $\div 100$, and by a product such as 12 in steps: $1{,}344 \div 4 \div 3 = 112$. To divide by a number that isn't one of these, split the dividend: $672 \div 6 = 100 + 12$.
- Remainders in steps: the second step's remainder counts groups of the first divisor, so $1{,}003 \div 12$ has remainder $1 \times 4 + 3 = 7$.

Main mistakes:

- Keeping two of the four partial products: $47 \times 68 \ne 40 \times 60 + 7 \times 8$.
- Not carrying in $\times 11$: $68 \times 11$ is 748, not 6148.
- Using the difference of squares on numbers that aren't the same distance from $m$, or reading $m^2 - d^2$ as $(m - d)^2$.
- Splitting the divisor: $240 \div 12 \ne 240 \div 10 + 240 \div 2$.
- Writing $d^2$ as one digit in a square near 50: $53^2$ is 2,809, not 289.

### Percents, fractions and money in your head

Every percent question is a multiplier question, and every awkward multiplier has a friendly fraction behind it.

| Task | Method | Example |
|---|---|---|
| Undo 13% HST | take off $\frac{13}{113}$, about 11.5% of the total (10% + 1% + half a percent) | \$84.75 minus \$9.75 is \$75.00 |
| Undo an added $r$ | take off $\frac{r}{1 + r}$ of the total | +25% is undone by $-20\%$ |
| Undo a discount | add back a fraction of the sale price | 25% off: add a third, so \$60 becomes \$80 |
| Stacked changes | multiply multipliers | 20% off then 10% off: $0.72$, so 28% off |
| Rise then fall of $r$ | multiplier $1 - r^2$ | +10% then $-10\%$ is $0.99$ |
| Round trip | rise of $\frac{1}{n}$ is undone by a fall of $\frac{1}{n+1}$ | +50% is undone by $-33.3\%$ |
| Tip and tax | both are percents of the subtotal, so $1 + 0.13 + 0.15 = 1.28$ | \$86 split 4 ways: $21.50 \times 1.28 = 27.52$ |
| Unit price | divide by the size in hundreds, using a fraction | 225 g: times $\frac{4}{9}$ |
| Currency | round the rate to $1 + \frac{1}{n}$, add that fraction, undo with the round trip | at 1.40, USD 35 is CAD 49 |
| Doubling time | $\frac{72}{R}$ for a rate of $R$ percent | 9% doubles in about 8 years |

| Fraction | Percent | Fraction | Percent |
|---|---|---|---|
| $\frac{1}{6}$ | 16.7% | $\frac{1}{11}$ | 9.1% |
| $\frac{1}{7}$ | 14.3% | $\frac{1}{12}$ | 8.3% |
| $\frac{1}{9}$ | 11.1% | $\frac{3}{8}$, $\frac{5}{8}$, $\frac{7}{8}$ | 37.5%, 62.5%, 87.5% |

- Building blocks past the percents table: 2.5% is a quarter of 10%, 7.5% is 5% + 2.5%, 12.5% is an eighth, 17.5% is 20% − 2.5%.
- HST at 13% is a little over an eighth, so adding it is about adding an eighth and removing it is about taking off a ninth.
- Tip by the tax line: 1.5 times the HST is about a 20% tip.
- The numbers 2, 3, 4, 6, 8, 9 and 12 divide 72. For a quadrupling, use 144 instead of 72.
- Exchange rates change daily, so a round rate is for an estimate only.

Main mistakes:

- Taking 13% off the total instead of dividing by 1.13.
- Adding discounts: 20% and 10% make 28%, not 30%.
- Expecting a rise and a fall of the same percent to cancel.
- Converting currency in the wrong direction.
- Using 0.06 for 6% in the rule of 72, or using the rule above about 15%.
