# Estimation and sanity checks

After this lesson you can estimate a calculation in your head, build a rough answer to a question with no data (a Fermi estimate), and run a short checklist that catches most wrong answers before anyone else sees them.

Before this: [place value and rounding](../../01-elementary/01-place-value-and-rounding.md), [scientific notation](02-scientific-notation.md) and [percents](../02-ratios-rates-percents/03-percents.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Estimate $\dfrac{387 \times 5.2}{0.49}$ by rounding each number to one significant figure.
2. About how many seconds are there in a year? Give a power of ten times a one-digit number.
3. A friend says a 3% raise on a \$52,000 salary is \$15,600 a year. Check the claim.

<details class="solution" markdown>
<summary>Answers</summary>

1. About 4000: $\frac{400 \times 5}{0.5} = \frac{2000}{0.5} = 4000$. The exact value is about 4107.
2. About $3 \times 10^7$. A day has 86,400 seconds, and $86{,}400 \times 365 \approx 3.15 \times 10^7$, which is close to $\pi \times 10^7$.
3. Wrong. 10% of \$52,000 is \$5,200, so 3% is about \$1,560. The friend used 0.3 (which is 30%) instead of 0.03.

</details>

## The idea

You are about to pay for three cloud servers for a month, and a script you wrote reports the cost as \$8,985.60. Before you approve it, you do a rough calculation in your head: each server costs about 4 cents an hour, a month is about 700 hours, so three servers cost about $3 \times 0.04 \times 700 = 84$ dollars. The script is off by a factor of about 100, which points to a decimal point in the wrong place: it should say \$89.86. Your estimate didn't give the exact cost, but it showed in a few seconds that the exact answer was wrong.

That is the use of estimation in this lesson. A calculator, a spreadsheet or a program does exactly what you typed, so it can't tell you that you typed the wrong thing. A rough answer from rounded numbers can. If the exact answer and the estimate are close, you can trust the exact answer more. If they are far apart, one of them is wrong, and you find out now instead of later.

The same habit answers questions with no data at all. How many bytes would it take to store a record for every person in Canada? You can't look that up, but you can break it into pieces you know roughly (how many people, how many bytes per record), multiply, and get an answer that is right to within a factor of a few. That is often enough to make a decision.

## Definitions

An **estimate** is an approximate answer, usually worked out from rounded numbers ([place value and rounding](../../01-elementary/01-place-value-and-rounding.md#definitions)). This lesson adds names for the common ways to make one.

Rounding to **one significant figure** keeps only the first nonzero digit, rounded, and replaces the other digits before the decimal point with zeros: 387 becomes 400, 5.2 becomes 5, and 0.049 becomes 0.05. In scientific notation, it rounds the coefficient to a whole number: $3.87 \times 10^2$ becomes $4 \times 10^2$.

**Front-end estimation** works with the leading digits of each number first, then adjusts with the rest. For $4{,}385 + 2{,}917 + 1{,}602$, the fronts give $4{,}000 + 2{,}000 + 1{,}000 = 7{,}000$, the rest are about $400 + 900 + 600 = 1{,}900$, and the estimate is 8,900.

**Compatible numbers** are numbers close to the real ones that are easy to work with together. To estimate $3{,}592 \div 6.2$, replace it with $3{,}600 \div 6 = 600$, since 36 is a multiple of 6.

A **Fermi estimate** answers a question that has no data at hand by writing the unknown as a product (or quotient) of quantities you can estimate, then multiplying the estimates. The answer aims to be right to within a factor of about 10, its order of magnitude. The name comes from the physicist Enrico Fermi, who was known for these estimates.

A **sanity check** is a quick test of whether an answer is plausible: whether its units, sign and size make sense. A sanity check can show that an answer is wrong. It can't prove that an answer is right, but an answer that passes several different checks is very likely to be.

## How to do it

### Estimating a calculation

1. Round each number to one significant figure, or replace the numbers with compatible numbers.
2. Do the arithmetic with the rounded numbers. Handle the powers of ten separately, as in [scientific notation](02-scientific-notation.md#multiplying-and-dividing).
3. Note which way each rounding went. If every number was rounded up, the estimate is too high; if every number was rounded down, it is too low.
4. Compare with the exact answer. They should agree in the first digit and the power of ten, or at least be within a factor of about 2. If not, look for an error in one of them.

### Making a Fermi estimate

1. Write the unknown as a chain of quantities multiplied or divided together. Check that the units work out: (people) × (bytes per person) = bytes.
2. Estimate each quantity to one significant figure. Use facts you know (the table in [Tricks and shortcuts](#tricks-and-shortcuts) has some), and when you are unsure, pick a low and a high value.
3. Multiply, keeping the powers of ten separate.
4. Round the result to one significant figure. Say it as an order of magnitude ("about $10^{10}$").
5. Check it against something you know, from a different direction if you can. Work out the answer with your low and high values to see how much it could change.

### A checklist for any answer

Run these six checks on a final answer, in any order. Each takes seconds, and each catches a different kind of error.

1. Units. Carry units through the calculation. The answer's units must be the ones the question asks for: km/h times hours is km, but km/h times seconds is not metres until you convert.
2. Sign. Decide whether the answer should be positive or negative before you look at it. A temperature that dropped has a negative change; a price after a discount is less than the price before.
3. Size. Compare with an estimate. Ask whether the order of magnitude is reasonable: a person is about $10^0$ m tall, not $10^1$; monthly interest on a credit card is a small fraction of the balance.
4. Special cases. If the answer is a formula, put in values where you know the answer: 0, 1, equal values, or an extreme. An interest formula with a rate of 0 should give back the starting amount ([problem-solving playbook](../../00-start-here/problem-solving-playbook.md#check-extreme-and-edge-cases)).
5. Reverse operation. Undo the calculation: multiply back after dividing, add the tax back on, substitute the solution into the equation.
6. A second method. Get the answer another way: a different order, a different formula, a table instead of algebra, or code instead of paper.

## Worked examples

<div class="example" markdown>

### Example 1: checking a cloud bill

A cloud server costs \$0.0416 per hour. What do three of them cost for a 30-day month, running the whole time? Estimate first, then work out the exact cost and check it.

Estimate. A 30-day month has $30 \times 24 = 720$ hours. Step 1: round to one significant figure: \$0.0416 becomes \$0.04, and 720 hours becomes 700. Step 2:

$$
3 \times 0.04 \times 700 = 0.12 \times 700 = 84 \text{ dollars}.
$$

Step 3: both 0.0416 and 720 were rounded down, so the exact cost is a bit more than \$84.

Exact: $3 \times 0.0416 \times 720 = 0.1248 \times 720 = 89.856$, so \$89.86.

Step 4: \$89.86 is a bit more than \$84, as Step 3 predicted, and the two agree in the first digit. Now the checklist:

- Units: servers × (dollars per server-hour) × hours gives dollars.
- Sign: a cost is positive.
- Size: under \$100 for three small servers for a month is plausible, and \$8,985.60 is not.
- Reverse: $89.856 \div 720 \div 3 = 0.0416$.

<div class="warning" markdown>

Watch out at Step 1: rounding 0.0416 to 0.4 instead of 0.04 makes the estimate ten times too big. Rounding to one significant figure keeps the first nonzero digit in its place; the zeros in front of it stay. A size check on the rounding itself helps: 0.0416 is about 4 cents, and 0.4 is 40 cents.

</div>

</div>

<div class="example" markdown>

### Example 2: a record for every person in Canada

About how much storage does it take to keep one record (name, date of birth and address) for every person in Canada?

Step 1: storage = (number of people) × (bytes per record), and people × bytes per person gives bytes.

Step 2: Statistics Canada estimated the population at 41,417,056 on April 1, 2026 ([Canada's population estimates, first quarter 2026](https://www150.statcan.gc.ca/n1/daily-quotidien/260617/dq260617a-eng.htm)), which is about $4 \times 10^7$. For a record, a name is about 30 characters, a date 10 and an address about 60, so about 100 characters. At one or two bytes per character, plus some overhead, say 200 bytes, which is $2 \times 10^2$. A low value is 100 bytes and a high value is 1000.

Step 3: multiply, with the powers of ten kept apart:

$$
4 \times 10^7 \times 2 \times 10^2 = 8 \times 10^9 \text{ bytes}.
$$

Step 4: about $10^{10}$ bytes, or 8 GB.

Step 5: with the low value the answer is $4 \times 10^9$ bytes, and with the high value $4 \times 10^{10}$, so the answer is between 4 GB and 40 GB. Each of these fits on a laptop, and even the high one is small next to a 1 TB drive. So the decision ("can one machine hold this?") comes out the same at both ends of the range, and that is what makes the estimate useful.

</div>

<div class="example" markdown>

### Example 3: three errors that a check catches

Each answer below is wrong. Find the check that catches it.

(a) A credit card balance of \$2,400 is charged 19.99% interest a year, so the interest for one month is about $2400 \times 19.99 \div 12 = 3{,}998$ dollars. Size check: one month's interest can't be more than the whole balance. The rate went in as 19.99 instead of 0.1999, a decimal point two places off. The right value is $2400 \times 0.1999 \div 12 = 39.98$, so about \$40. Estimate to confirm: 20% of \$2,400 is \$480 a year, which is \$40 a month.

(b) A car travels at 100 km/h. How far does it go in the 3 seconds you look at your phone? The answer "$100 \times 3 = 300$ m" fails the units check: km/h times seconds is not metres. Convert the speed first: $100 \text{ km/h} = \frac{100{,}000 \text{ m}}{3600 \text{ s}} \approx 27.8$ m/s, so the car goes $27.8 \times 3 \approx 83$ m. That is longer than a hockey rink, which is about 61 m. A second method agrees: 100 km/h is 100,000 m in 3,600 s, and 3 s is $\frac{1}{1200}$ of an hour, so the distance is $\frac{100{,}000}{1200} \approx 83$ m.

(c) A jacket costs \$48 after 20% off. What was the original price? The answer "$48 \times 1.2 = 57.60$" fails the reverse check: 20% off \$57.60 is $57.60 \times 0.8 = 46.08$, not 48. The 20% was taken of the wrong whole, the sale price instead of the original price ([percent change](../02-ratios-rates-percents/04-percent-change-and-applications.md)). The sale price is 80% of the original, so the original is $48 \div 0.8 = 60$ dollars. Reverse check: $60 \times 0.8 = 48$.

</div>

<div class="example" markdown>

### Example 4: gasoline in Ontario (finish it yourself)

About how many litres of gasoline do cars in Ontario use in a year?

Step 1: litres = (number of cars) × (kilometres per car per year) × (litres per kilometre).

Step 2: Ontario had about 16.1 million people on April 1, 2026, by the same Statistics Canada release. Say about one car for every two people, so $8 \times 10^6$ cars. A car is driven about 15,000 km a year, which is $1.5 \times 10^4$ km, and uses about 8 L per 100 km, which is $8 \times 10^{-2}$ L per km.

Now do Steps 3 and 4, then check the answer with a per-person figure.

<details class="solution" markdown>
<summary>Finish</summary>

Step 3: one car uses $1.5 \times 10^4 \times 8 \times 10^{-2} = 12 \times 10^2 = 1200$ L a year. All the cars use $8 \times 10^6 \times 1.2 \times 10^3 = 9.6 \times 10^9$ L.

Step 4: about $10^{10}$ litres a year.

Step 5: per person that is $9.6 \times 10^9 \div 1.61 \times 10^7 \approx 600$ L a year, about 12 L a week. A household with one car and two drivers buying a tank of 40 to 50 L every few weeks fits that. The estimate ignores trucks and electric cars, which push it in opposite directions, so "about $10^{10}$ L" is as precise as it should claim to be.

</details>

</div>

## Edge cases and common mistakes

Rounding a small decimal to the wrong place is flagged in Example 1. Here are the others.

<div class="warning" markdown>

Watch out: an estimate can hide an error if you round toward the answer you expect. Round first, before you look at the exact answer, and round by the rule (nearest, or compatible numbers chosen for the arithmetic), not by what makes the numbers agree.

</div>

<div class="warning" markdown>

Watch out: rounding every number the same way piles up the error. In $87 \times 76 \times 64$, rounding each to one significant figure gives $90 \times 80 \times 60 = 432{,}000$, while the exact value is 423,168, so that one is fine. But $149 \times 149 \times 149$ rounds to $100 \times 100 \times 100 = 1{,}000{,}000$, and the exact value is 3,307,949, more than three times bigger: each factor dropped by a third. When a factor sits near a rounding boundary, keep two significant figures ($150^3 = 3{,}375{,}000$).

</div>

<div class="warning" markdown>

Watch out: a check that uses the same wrong step agrees with the wrong answer. If you set up a percent problem with the wrong whole, redoing the same arithmetic more carefully gives the same wrong result. A reverse check or a second method goes through different steps, which is why the checklist includes them.

</div>

Some answers can't be estimated well by rounding. A difference of two nearly equal numbers, such as $5{,}012 - 4{,}987 = 25$, rounds to $5{,}000 - 5{,}000 = 0$, which says nothing. For a difference, keep enough digits to see what is left, or estimate each number more closely.

A Fermi estimate is only as good as its chain. A missing factor, such as forgetting that only some people drink coffee, can throw the answer off by more than all the rounding put together. Say each factor in words, and ask whether every one of them belongs.

Zero and very small numbers need care with relative size. An answer of 0.0003 where you expected 0.0004 is close in absolute terms but 25% off, and an answer of 1 where you expected 0 can't be compared by ratio at all. Decide whether the question cares about the difference or about the ratio.

## Tricks and shortcuts

These facts come up in estimates often enough to memorize. The population figures are Statistics Canada's estimates for April 1, 2026; the rest don't change.

| Fact | Value | Rough |
|---|---|---|
| seconds in an hour | 3,600 | $3.6 \times 10^3$ |
| seconds in a day | 86,400 | $10^5$ (closer: $9 \times 10^4$) |
| seconds in a year (365.25 days) | 31,557,600 | $\pi \times 10^7 \approx 3 \times 10^7$ |
| hours in a year | 8,766 | $10^4$ |
| full-time work hours in a year | $40 \times 52 = 2{,}080$ | $2 \times 10^3$ |
| $2^{10}$ | 1,024 | $10^3$ |
| speed of light | 299,792,458 m/s | $3 \times 10^8$ m/s |
| population of Canada | 41,417,056 | $4 \times 10^7$ |
| population of Ontario | 16,103,890 | $1.6 \times 10^7$ |
| mass of 1 L of water | 1 kg | |
| distance around the Earth at the equator | 40,075 km | $4 \times 10^4$ km |

The "$\pi \times 10^7$ seconds in a year" fact is off by less than 0.5%, which is far better than an estimate needs. The work-hours row turns an hourly wage into a yearly one: \$25 an hour full time is about $25 \times 2{,}000 = 50{,}000$ dollars a year, before tax.

When you multiply, round one factor up and another down if you can, so the errors partly cancel. For $48 \times 53$, use $50 \times 50 = 2{,}500$; the exact value is 2,544.

When a Fermi quantity could be anywhere between a low and a high value that are far apart, use a middle value on a multiplying scale, not an adding one. Between 100 and 10,000 the middle is 1,000, because each is a factor of 10 away from it. (This is the geometric mean, $\sqrt{100 \times 10{,}000}$.) The ordinary average, about 5,000, gives too much weight to the high end.

Check the last digit of a product. The last digit of $387 \times 52$ must be the last digit of $7 \times 2 = 14$, so it ends in 4. An answer of 20,125 is wrong without any more work; the exact value is 20,124.

The nines check catches most slips in long multiplication. Add the digits of each number, and keep adding until you have one digit (a 9 counts as 0). For $387 \times 52 = 20{,}124$: the digits of 387 give $3 + 8 + 7 = 18$, then $1 + 8 = 9$, which counts as 0; the digits of 52 give 7; and $0 \times 7 = 0$. The answer's digits give $2 + 0 + 1 + 2 + 4 = 9$, which counts as 0, so it passes. A wrong answer such as 20,134 gives 1 and fails. The check can't catch two swapped digits (20,214 passes too), and why it works is modular arithmetic: [divisibility and modular arithmetic](../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md).

## In code

A sanity check in a program is an `assert`: a line that stops the program if a condition you expect is false. Checks like these catch the errors in Example 3 before the numbers reach anyone.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

seconds_per_year = 365.25 * 24 * 3600
print(seconds_per_year, round(math.pi * 1e7))   # 31557600.0 31415927

def monthly_interest(balance, annual_rate):
    """annual_rate is a decimal, such as 0.1999 for 19.99%."""
    assert 0 <= annual_rate < 1, "rate looks like a percent, not a decimal"
    return balance * annual_rate / 12

print(round(monthly_interest(2400, 0.1999), 2))  # 39.98

exact = 3 * 0.0416 * 720
estimate = 3 * 0.04 * 700
print(round(exact, 2), estimate)                      # 89.86 84.0
print(math.isclose(exact, estimate, rel_tol=0.25))    # True
```

Calling `monthly_interest(2400, 19.99)` stops with an `AssertionError` and the message about percents, which is the size check from Example 3 written into the code. The last line compares the exact cost with the estimate, allowing a 25% gap; a cost of 8985.60 would fail it.

</details>

## FAQ

### How close should an estimate be?

It depends on what the estimate is for. To check a calculation, the estimate should match the exact answer in its first digit and its power of ten, or be within a factor of about 2. A Fermi estimate aims for the right order of magnitude, within a factor of about 10 either way, because each factor in its chain is only a guess. Both are enough for their job, which is to catch large errors and to support decisions such as "yes, this fits on one machine".

### Why estimate when a calculator gives the exact answer?

A calculator gives the exact answer to the question you typed, which may not be the question you meant. Most real errors are in the setup: a decimal point, a unit, the wrong whole, a missing factor. The calculator can't see any of these, and an estimate made separately can. Estimating first also tells you roughly what to expect, so a strange result stands out right away.

### What should I do when the estimate and the exact answer disagree?

First check the estimate, since it is quicker: redo it with different rounding. If the two still disagree, look at the exact calculation for the common errors in this lesson: a decimal point off by a power of ten, a unit that wasn't converted, a percent of the wrong whole. A disagreement by a factor of exactly 10, 100 or 1000 almost always means a decimal point or a metric prefix; a factor of 8 suggests bits and bytes; a factor of 60 or 3,600 suggests minutes or hours.

## Practice

### Warm-up

1\. Round each number to one significant figure and estimate: (a) $48.7 \times 21.3$, (b) $0.0612 \times 3{,}890$, (c) $7{,}814 \div 39$. Then compare with the exact answers.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $50 \times 20 = 1{,}000$. Exact: 1,037.31.
- (b) $0.06 \times 4{,}000 = 240$. Exact: 238.068.
- (c) $8{,}000 \div 40 = 200$. Exact: about 200.36.

Each estimate matches the exact answer in its first digit and power of ten. In (a), one factor was rounded up and one down, so the errors partly cancelled.

</details>

2\. Estimate with front-end estimation or compatible numbers: (a) $2{,}346 + 5{,}781 + 1{,}195$, (b) $4{,}215 \div 7$, (c) $25 \times 3.98 \times 4$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Fronts: $2{,}000 + 5{,}000 + 1{,}000 = 8{,}000$. The rest: $346 + 781 + 195 \approx 300 + 800 + 200 = 1{,}300$. Estimate: 9,300. Exact: 9,322.
- (b) $4{,}200 \div 7 = 600$, since $42 \div 7 = 6$. Exact: about 602.14.
- (c) Multiply the compatible pair first: $25 \times 4 = 100$, and $100 \times 3.98 = 398$. Here the estimate is the exact answer, because only the order changed.

Check (b) by reversing: $7 \times 600 = 4{,}200$, which is 15 less than 4,215, so the exact quotient is a little over 600.

</details>

3\. Using the facts table, estimate (a) the seconds in a week, (b) the hours in a 365-day year, (c) $2^{30}$ as a power of ten, and (d) the yearly pay, before tax, of a full-time job at \$30 an hour.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $7 \times 86{,}400 = 604{,}800$, about $6 \times 10^5$.
- (b) $365 \times 24 = 8{,}760$, about $10^4$.
- (c) $2^{30} = (2^{10})^3 \approx (10^3)^3 = 10^9$. The exact value is 1,073,741,824.
- (d) $30 \times 2{,}000 = 60{,}000$ dollars. With 2,080 hours it is \$62,400.

Check (a) another way: $6 \times 10^5$ seconds divided by $3{,}600$ seconds per hour is about 167 hours, and a week has $7 \times 24 = 168$.

</details>

### Standard

4\. Each claim is wrong. Name the check that catches it, and give the right answer. (a) "My rent of \$1,200 is 30% of my monthly take-home pay of \$360." (b) "Twelve 250 mL bottles hold 30 L." (c) "A 4-hour flight at 800 km/h covers 200 km."

<details class="solution" markdown>
<summary>Solution</summary>

(a) Size: if rent is 30% of pay, the pay must be more than the rent, and \$360 is less. The claim took 30% of the rent. The pay is the whole, so it is $1{,}200 \div 0.3 = 4{,}000$ dollars. Reverse: $0.3 \times 4{,}000 = 1{,}200$.

(b) Units and size: $12 \times 250 = 3{,}000$ mL, and 1 L is 1,000 mL, so 3 L. Each bottle is a quarter of a litre, so twelve make 3 L, not 30.

(c) Units: km/h divided by hours is not km. Distance is speed times time: $800 \times 4 = 3{,}200$ km. Size: a plane flies much more than 200 km in 4 hours.

</details>

5\. Make a Fermi estimate of the number of cups of coffee drunk in Canada in one day. State each assumption, and give a low and a high value.

<details class="solution" markdown>
<summary>Solution</summary>

Step 1: cups per day = (people) × (fraction who drink coffee) × (cups per coffee drinker per day).

Step 2: Canada has about $4 \times 10^7$ people. About 4 in 5 are adults, and say about two thirds of adults drink coffee, so the fraction is about $0.8 \times 0.67 \approx 0.5$. Say a coffee drinker has about 2 cups a day.

Step 3: $4 \times 10^7 \times 0.5 \times 2 = 4 \times 10^7$ cups.

Step 4: about $4 \times 10^7$, forty million cups a day.

Step 5: a low case (40% drink coffee, 1.5 cups each) gives $4 \times 10^7 \times 0.4 \times 1.5 = 2.4 \times 10^7$, and a high case (60%, 3 cups) gives $7.2 \times 10^7$. Both are of order $10^7$, so the order of magnitude doesn't depend on the guesses. Your own assumptions may give a different number; anything from about $10^7$ to $10^8$ is a reasonable answer.

</details>

6\. A classmate computes the balance after 10 years of \$1,000 invested at 5% a year, compounded yearly, as $1000 \times 1.5^{10} = 57{,}665.04$ dollars. Use the checklist to find the error, then give the right balance.

<details class="solution" markdown>
<summary>Solution</summary>

Size: at 5% a year, simple interest would add \$50 a year, \$500 in 10 years, so the balance should be around \$1,500, a bit more because of compounding. An answer near \$58,000 is too big by a factor of more than 30.

Special case: with a rate of 0, the formula $1000 \times (1 + r)^{10}$ gives 1,000, which is right, so the shape of the formula is fine. The error is in the number: 5% as a decimal is 0.05, so the growth factor is $1 + 0.05 = 1.05$, not 1.5.

The right balance is $1000 \times 1.05^{10} \approx 1{,}628.89$ dollars.

Second method, year by year: 1,050.00, 1,102.50, 1,157.63, and so on, reaching about \$1,628.89 in year 10.

</details>

### Challenge

7\. An uncompressed video frame at 1920 by 1080 pixels uses 3 bytes per pixel. Would a 2-hour movie at 30 frames per second, stored uncompressed, fit on a 1 TB drive ($10^{12}$ bytes)? Estimate first, then compute.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate. One frame is about $2 \times 10^3 \times 1 \times 10^3 \times 3 = 6 \times 10^6$ bytes. Two hours is $7{,}200$ s, about $7 \times 10^3$ s, so there are about $30 \times 7 \times 10^3 = 2.1 \times 10^5$ frames. The movie is about $6 \times 10^6 \times 2 \times 10^5 = 1.2 \times 10^{12}$ bytes, just over 1 TB.

Exact. One frame is $1920 \times 1080 \times 3 = 6{,}220{,}800$ bytes, and there are $30 \times 7{,}200 = 216{,}000$ frames, so the movie is $6{,}220{,}800 \times 216{,}000 \approx 1.344 \times 10^{12}$ bytes.

So no: it needs about 1.34 TB. The estimate already said "just over", and since both rounded factors (2,000 for 1,920 and 1,000 for 1,080) were close, the exact answer was expected to be near it.

Check the units: (bytes per frame) × (frames per second) × (seconds) = bytes.

</details>

8\. This one reviews [percent change](../02-ratios-rates-percents/04-percent-change-and-applications.md#several-changes-in-a-row) and [exponent rules](01-exponent-rules.md). Prices rise 2% a year for 10 years. A friend says that is a 20% rise in total. Estimate $1.02^{10}$ without a calculator, using $1.02^{10} = (1.02^5)^2$, and decide whether the friend is right.

<details class="solution" markdown>
<summary>Solution</summary>

Work up in steps: $1.02^2 = 1.0404$, so $1.02^4 = 1.0404^2 \approx 1.0824$, and $1.02^5 \approx 1.0824 \times 1.02 \approx 1.1041$. Then $1.02^{10} = (1.1041)^2 \approx 1.2190$.

So prices rise about 21.9%, not 20%. The friend added the ten rises, which ignores that each year's 2% is taken on a bigger price.

Check with a second method: small rates almost add, so the total should be a little more than 20%, and 21.9% is. A calculator gives $1.02^{10} = 1.21899\ldots$

</details>

## Where this shows up

- The [problem-solving playbook](../../00-start-here/problem-solving-playbook.md#check-units-and-size) uses these checks in its "look back" step, and the lessons on [percents](../02-ratios-rates-percents/03-percents.md) and [multi-step equations](../03-expressions-equations-inequalities/04-multi-step-equations.md) end each solution with one. [Linear approximation and L'Hopital's rule](../../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md) turns the root estimate $n + \frac{d}{2n}$ from the last lesson into a general method.
- In CS, orders of magnitude decide whether an algorithm is fast enough ([asymptotic notation](../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md)), and Fermi estimates of storage, bandwidth and request rates are the first step of system design.
- In economics and finance, a per-person figure such as income per capita is a quick check on a national total, and the rule of 72 (doubling time, the rule of 72 and logs<!-- link: ../../08-financial-math/02-interest-and-growth/05-doubling-time-rule-of-72-and-logs.md -->) estimates growth in your head.
