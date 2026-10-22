# Place value and rounding

After this lesson you can read, write and compare whole numbers into the millions, round a number to any place, and estimate a sum with rounded numbers.

Before this: nothing. This is the first lesson in the book.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write "three million forty thousand six hundred seven" in digits, then in expanded form.
2. Round 2,996 to the nearest ten, and round 6,451,820 to the nearest hundred thousand.
3. Put these numbers in order from smallest to largest: 98,760; 100,001; 98,706.

<details class="solution" markdown>
<summary>Answers</summary>

1. 3,040,607, which is $3{,}000{,}000 + 40{,}000 + 600 + 7$. The zeros hold the empty hundred thousands, thousands and tens places.
2. 3,000 and 6,500,000. In 2,996 the ones digit 6 pushes the tens digit 9 up to 10, which carries into the hundreds and then into the thousands. In 6,451,820 the ten thousands digit is 5, so the hundred thousands digit 4 goes up to 5.
3. 98,706, then 98,760, then 100,001. The six-digit number is the largest, and the two five-digit numbers first differ in the tens place, where 0 is less than 6.

</details>

## The idea

A supplier packs paper clips in boxes of 10, cases of 10 boxes (100 clips) and cartons of 10 cases (1,000 clips). An order for 2,436 clips ships as 2 cartons, 4 cases, 3 boxes and 6 loose clips:

| Cartons (1,000 clips) | Cases (100 clips) | Boxes (10 clips) | Loose clips |
|---|---|---|---|
| 2 | 4 | 3 | 6 |

Each digit of 2,436 counts one size of package, and its position says which size. The same digits in a different order, 6,342, would mean 6 cartons and only 2 loose clips. That is place value: what a digit is worth depends on where it sits. Because each package holds exactly ten of the next size down, no digit ever needs to go past 9, since a tenth loose clip would fill another box.

Rounding answers a rougher question, such as "about how many cartons?" The order is between 2 cartons and 3, and closer to 2, so to the nearest thousand it is about 2,000 clips. To the nearest hundred it is about 2,400, because 2,436 is closer to 24 cases than to 25.

## Definitions

The **whole numbers** are 0, 1, 2, 3 and so on: the counting numbers together with zero. A **digit** is one of the ten symbols 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9, and every whole number is written as a string of digits.

In base 10, each position in a number has a **place value**. From the right, the places are worth 1, 10, 100, 1,000 and so on, and each place is worth 10 times the place to its right. The value of a digit is the digit times the place value of its position. In plain words, the 4 in 2,436 sits in the hundreds place, so it is worth $4 \times 100 = 400$.

Here are the places up to the millions, with the number 4,072,519 filled in:

| Millions | Hundred thousands | Ten thousands | Thousands | Hundreds | Tens | Ones |
|---|---|---|---|---|---|---|
| 1,000,000 | 100,000 | 10,000 | 1,000 | 100 | 10 | 1 |
| 4 | 0 | 7 | 2 | 5 | 1 | 9 |

The commas split the digits into groups of three from the right, called **periods**: the ones period (hundreds, tens and ones), the thousands period and the millions period. The pattern continues to the left with ten millions, hundred millions and then billions, where a billion is a thousand millions.

A 0 in a place means none of that place. It still has to be written, to keep the other digits where they belong: without its 0, 4,072,519 would become 472,519, about a tenth of the size.

The **expanded form** of a number writes it as the sum of the values of its digits:

$$
4{,}072{,}519 = 4{,}000{,}000 + 70{,}000 + 2{,}000 + 500 + 10 + 9.
$$

The usual way of writing the number, 4,072,519, is its **standard form**.

To **round** a whole number to a given place means to replace it with the nearest number that has only zeros to the right of that place. When the number is exactly halfway between two such numbers, as 2,450 is between 2,400 and 2,500, the usual rule, and the one this book uses, rounds up. In plain words, rounding 2,436 to the nearest hundred asks whether it is closer to 2,400 or to 2,500. It is 36 away from 2,400 and 64 away from 2,500, so it rounds to 2,400. We write $2{,}436 \approx 2{,}400$, where $\approx$ means "is approximately equal to".

To **truncate** a number to a given place means to replace every digit to the right of that place with 0, without looking at what those digits are. Truncating 2,996 to the tens gives 2,990, while rounding it gives 3,000. Truncating a whole number never makes it bigger, so it is the same as always rounding down.

An **estimate** is an approximate answer, usually worked out from rounded numbers. For example, $389 + 412 \approx 400 + 400 = 800$, and the exact sum is 801.

Comparing uses two symbols. The statement $a < b$ means "$a$ is less than $b$", and $a > b$ means "$a$ is greater than $b$". The open side of the sign faces the larger number, as in $472{,}519 < 4{,}072{,}519$.

<div class="note" markdown>

Base 10 is positional: a digit's value depends on its position, and each place is worth ten of the place to its right. Nothing in that idea needs the number ten. In base 2, or binary, each place is worth two of the place to its right, so the places are worth 1, 2, 4, 8, 16 and so on, and the only digits are 0 and 1. The binary number $1011_2$, where the small 2 names the base, means one 8, no 4s, one 2 and one 1, which is eleven. Computers store numbers this way, and [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md) shows how to convert between bases.

</div>

## How to do it

### Reading and writing large numbers

1. To read a number, split its digits into periods of three, starting from the right. Read each period as a number from 1 to 999, then say the name of the period: "million", "thousand", or nothing for the ones period. Skip a period that is 000.
2. To write a number given in words, write each period as exactly three digits, filling the empty places with zeros. Only the leftmost period may have fewer than three digits.
3. Check by reading your digits back aloud.

So 4,072,519 reads "four million, seventy-two thousand, five hundred nineteen". Leave "and" out of whole numbers, because "and" marks the point between whole units and parts of one: on a cheque, "four hundred nineteen and 50/100 dollars" means \$419.50.

In English Canada the comma is the usual separator, and this book uses it. Metric (SI) style and French use a space instead, as in 4 072 519, because in French the comma is the decimal point: 2,5 means two and a half. This book puts the comma in four-digit numbers too, as in 2,436, but not in years such as 2026.

### Comparing and ordering

1. Count the digits of each number, leaving out zeros at the left end. The number with more digits is larger.
2. If the numbers have the same number of digits, compare them one place at a time from the left. The first place where the digits differ decides: the number with the larger digit there is larger.
3. To put a list in order, line the numbers up at the ones in a place-value table and apply steps 1 and 2.

### Rounding to a given place

1. Find the rounding digit, the digit in the place you are rounding to.
2. Look at the next digit to its right, and only that digit.
3. If that digit is 5, 6, 7, 8 or 9, add 1 to the rounding digit (round up). If it is 0, 1, 2, 3 or 4, leave the rounding digit alone (round down).
4. Replace every digit to the right of the rounding place with 0. The digits to the left stay as they are, except when step 3 turned a 9 into 10: then write 0 and add 1 to the digit on its left, as when you carry in addition.
5. Check that the answer has only zeros right of the rounding place, and that it is no further from the original than half of that place: 5 for tens, 50 for hundreds, 500 for thousands.

### Estimating a sum

1. Round every number to the same place. Choose a place that leaves the larger numbers with one or two nonzero digits.
2. Add the rounded numbers.
3. Compare the estimate with the exact sum. If the two are far apart, look for a mistake in the exact sum.

## Worked examples

<div class="example" markdown>

### Example 1: rounding to the nearest thousand

Round 4,072,519 to the nearest thousand.

Step 1: the thousands digit is the 2, so it is the rounding digit.

Step 2: the next digit to the right is the hundreds digit, 5.

Step 3: 5 is in the round-up group, so the rounding digit 2 becomes 3.

Step 4: the hundreds, tens and ones become 0, and the digits to the left of the thousands stay as they are. The answer is 4,073,000.

Step 5: the answer should be the nearest whole number of thousands. The two candidates are 4,072,000 and 4,073,000, and the distances to them are

$$
\begin{aligned}
4{,}072{,}519 - 4{,}072{,}000 &= 519, \\
4{,}073{,}000 - 4{,}072{,}519 &= 481.
\end{aligned}
$$

The number is closer to 4,073,000, so $4{,}072{,}519 \approx 4{,}073{,}000$. The distance, 481, is less than 500, as step 5 requires.

Rounded to other places, the same number gives different answers. Each row looks at a single digit, the one right after the rounding digit:

| Round to the nearest | Rounding digit | Next digit | Answer |
|---|---|---|---|
| ten | 1 | 9 | 4,072,520 |
| hundred | 5 | 1 | 4,072,500 |
| thousand | 2 | 5 | 4,073,000 |
| ten thousand | 7 | 2 | 4,070,000 |
| hundred thousand | 0 | 7 | 4,100,000 |
| million | 4 | 0 | 4,000,000 |

</div>

<div class="example" markdown>

### Example 2: rounding with a 9

Round 2,996 to the nearest ten.

Steps 1 to 3: the rounding digit is the tens digit, 9, and the next digit is 6, so the 9 goes up by 1, to 10. A place can't hold 10, so step 4 takes over: write 0 in the tens and add 1 to the hundreds. The hundreds digit is also 9, so it becomes 10 as well. Write 0 there too and add 1 to the thousands, which turns the 2 into 3. The ones become 0, and the answer is 3,000.

Step 5 makes sense of it. The whole numbers of tens on either side of 2,996 are 2,990 and 3,000. The number is 6 above 2,990 and 4 below 3,000, so 3,000 is the nearest.

<div class="warning" markdown>

Watch out at step 4: writing the 10 into the tens place turns four digits into five, "29100", and dropping the carry gives 2,900, which is 96 away from 2,996. A rounded number always lands within half a place of the original, so the check in step 5 catches both.

</div>

</div>

<div class="example" markdown>

### Example 3: putting numbers in order

Order 4,072,519; 407,251; 4,027,915 and 4,072,600 from smallest to largest.

Step 1: 407,251 has six digits and the others have seven, so it is the smallest. Step 2 compares the three seven-digit numbers from the left:

| Number | Millions | Hundred thousands | Ten thousands | Thousands | Hundreds | Tens | Ones |
|---|---|---|---|---|---|---|---|
| 4,072,519 | 4 | 0 | 7 | 2 | 5 | 1 | 9 |
| 4,027,915 | 4 | 0 | 2 | 7 | 9 | 1 | 5 |
| 4,072,600 | 4 | 0 | 7 | 2 | 6 | 0 | 0 |

The millions and hundred thousands match. In the ten thousands, 4,027,915 has a 2 where the others have a 7, so it is the smallest of the three. The other two match until the hundreds, where 5 is less than 6. The order is

$$
407{,}251 < 4{,}027{,}915 < 4{,}072{,}519 < 4{,}072{,}600.
$$

Check: 4,027,915 has the largest hundreds digit of the three, a 9, but the ten thousands place had already decided. Only the first difference counts.

</div>

<div class="example" markdown>

### Example 4: estimating a budget

One month's costs are \$1,425 for rent, \$386 for groceries, \$128 for transit and \$65 for a phone. Estimate the total.

Steps 1 and 2: to the nearest hundred, the amounts are 1,400, 400, 100 and 100, which add to 2,000. So the month costs about \$2,000.

Step 3: the exact total is $1{,}425 + 386 + 128 + 65 = 2{,}004$, that is, \$2,004, very close to the estimate. Two of the amounts were rounded up (by 14 and 35) and two were rounded down (by 25 and 28), so the errors nearly cancelled.

Truncating to the hundreds instead gives $1{,}400 + 300 + 100 + 0 = 1{,}800$, which is \$204 short. Every truncated amount is lower than the real one, so the errors all point the same way and add up.

</div>

## Edge cases and common mistakes

Example 2 shows the carry from a 9 going wrong. Here are the other places where rounding and writing numbers go wrong.

<div class="warning" markdown>

Watch out: round in one step, from the original number. To round 1,449 to the nearest hundred, look at the tens digit, 4, and round down to 1,400. Rounding in a chain, first to 1,450 and then to 1,500, gives the wrong answer, because 1,449 is 49 from 1,400 and 51 from 1,500.

</div>

<div class="warning" markdown>

Watch out: rounding replaces digits with zeros; it doesn't remove them. Rounding 4,072,519 to the nearest thousand gives 4,073,000, not 4,073, which is a thousand times smaller. After a decimal point the digits are dropped instead, as [decimals: place value, adding and subtracting](12-decimals-place-value-and-adding.md) explains.

</div>

<div class="warning" markdown>

Watch out for missing zeros when you write a number from words. "Two million six thousand forty" needs three full periods, 2, then 006, then 040, so it is 2,006,040. Writing the parts as you hear them gives 2,640 or 26,040, and reading the digits back aloud (step 3) catches the slip.

</div>

<div class="warning" markdown>

Watch out: compare digit counts before digits. The number 98,760 starts with a 9 and 100,001 starts with a 1, but 100,001 has six digits and is larger. Comparing first digits only works for numbers of the same length.

</div>

Rounding to a place larger than the number can give 0: 381 rounded to the nearest thousand is 0, because 381 is closer to 0 than to 1,000. That answer is correct, if not very useful. A number that already has zeros to the right of the rounding place, such as 4,000 rounded to the nearest hundred, stays as it is. Zeros at the left end of a number change nothing, so 007 is 7, while a zero inside a number or at its right end is a real digit.

## Tricks and shortcuts

To round in your head, find the halfway mark first. Between 2,400 and 2,500 it is 2,450: a number below it rounds down, and a number at it or above it rounds up. This is the "look at the next digit" rule pictured on a number line.

News reports round large numbers and mix digits with words. A population of 2,431,906 becomes "2.4 million", which is 2,400,000, the population rounded to the nearest hundred thousand. To turn such a number back into digits, read "2.4 million" as 2 million plus 4 hundred thousand.

## In code

Python formats, rounds and truncates whole numbers in one line each. A negative second argument to `round` rounds to the left of the ones place: $-1$ for tens, $-3$ for thousands.

<details class="code" markdown>
<summary>In code</summary>

```python
n = 4072519
print(f"{n:,}")                          # 4,072,519
print(round(n, -3))                      # 4073000, the nearest thousand
print(round(2996, -1))                   # 3000, with the carry from the 9s
print(n // 1000 * 1000)                  # 4072000, truncated to the thousands
print(round(2450, -2), round(2550, -2))  # 2400 2600: halves go to the even neighbour
```

The expression `n // 1000` divides and drops the remainder, as in [long division](07-long-division.md), and multiplying by 1000 puts the zeros back. The last line is a surprise: Python's `round` doesn't round halves up. The FAQ explains why.

</details>

## FAQ

### Why does 5 round up when the number is exactly halfway?

It is a convention. The number 2,450 is 50 from 2,400 and 50 from 2,500, so neither is nearer, and a rule has to pick one. Rounding halves up is easy to apply, since you look at one digit. Its cost is a small upward drift: if many amounts end in exactly 50, rounding them all up makes their total too big. Python's `round` uses **round half to even** instead, also called banker's rounding, in which an exact half goes to the neighbour whose rounding digit is even. So 2,450 rounds to 2,400 and 2,550 rounds to 2,600, and over many numbers half the halves go up and half go down. It is also the default rule in floating-point arithmetic ([floating point basics](../06-cs-math/01-number-representation/04-floating-point-basics.md)).

### Should I round before or after I calculate?

For an estimate, round first, since that is what makes the arithmetic easy. For an answer you report, calculate with the exact numbers and round once, at the end. Rounding along the way can move the answer: $1{,}449 + 1{,}449 = 2{,}898$, which rounds to 2,900, but rounding first gives $1{,}400 + 1{,}400 = 2{,}800$.

## Practice

### Warm-up

1\. Write 5,030,208 in words and in expanded form. What is the 3 worth?

<details class="solution" markdown>
<summary>Solution</summary>

The periods are 5, then 030, then 208, so the number reads "five million, thirty thousand, two hundred eight". In expanded form it is $5{,}000{,}000 + 30{,}000 + 200 + 8$. The 3 sits in the ten thousands place, so it is worth $3 \times 10{,}000 = 30{,}000$.

Check: add the expanded form back up. The first two parts make 5,030,000, and adding 208 gives 5,030,208.

</details>

2\. Put these numbers in order from largest to smallest: 1,203,450; 1,230,045; 999,999; 1,203,405.

<details class="solution" markdown>
<summary>Solution</summary>

Step 1: 999,999 has six digits and the others have seven, so it is the smallest. Step 2: the seven-digit numbers all start 1, 2 in the millions and hundred thousands. In the ten thousands, 1,230,045 has a 3 and the other two have a 0, so it is the largest. The remaining two, 1,203,450 and 1,203,405, match up to the hundreds and differ in the tens, where 5 is more than 0.

The order is $1{,}230{,}045 > 1{,}203{,}450 > 1{,}203{,}405 > 999{,}999$.

Check: 999,999 is one less than a million, and the other three are all more than a million, so it belongs at the end.

</details>

### Standard

3\. Round 48,951 to the nearest ten, hundred, thousand and ten thousand.

<details class="solution" markdown>
<summary>Solution</summary>

| Round to the nearest | Rounding digit | Next digit | Answer |
|---|---|---|---|
| ten | 5 | 1 | 48,950 |
| hundred | 9 | 5 | 49,000 |
| thousand | 8 | 9 | 49,000 |
| ten thousand | 4 | 8 | 50,000 |

To the nearest hundred, the 9 becomes 10, so step 4 writes 0 and carries into the thousands, where 8 becomes 9. Two of the answers are the same, which is fine.

Check with step 5: the answers are 1, 49, 49 and 1,049 away from 48,951, and each distance is at most half the place (5, 50, 500 and 5,000).

</details>

4\. A café's sales for four days are \$3,812, \$4,097, \$2,950 and \$5,368. (a) Estimate the total by rounding each amount to the nearest hundred. (b) Find the exact total and compare. (c) What estimate does truncating to the hundreds give?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The rounded amounts are 3,800, 4,100, 3,000 and 5,400. The 2,950 is exactly halfway between 2,900 and 3,000, so it rounds up. The estimate is $3{,}800 + 4{,}100 + 3{,}000 + 5{,}400 = 16{,}300$, about \$16,300.

(b) The exact total is $3{,}812 + 4{,}097 + 2{,}950 + 5{,}368 = 16{,}227$, so the estimate is \$73 high.

(c) Truncating gives $3{,}800 + 4{,}000 + 2{,}900 + 5{,}300 = 16{,}000$, which is \$227 low, because every truncated amount is lower than the real one.

Check: the exact total, 16,227, rounds to 16,200 to the nearest hundred, and the rounded estimate of 16,300 is within a hundred of it.

</details>

### Challenge

5\. Use each of the digits 0, 3, 5, 8 and 9 exactly once. (a) Write the largest and the smallest five-digit numbers you can. (b) Round each one to the nearest thousand.

<details class="solution" markdown>
<summary>Solution</summary>

(a) For the largest, put the largest digits in the largest places: 98,530. For the smallest, put the smallest digits first, except that a five-digit number can't start with 0 (the string 03589 is the four-digit number 3,589). So start with 3, then 0: 30,589.

(b) In 98,530 the thousands digit is 8 and the next digit is 5, so it rounds up to 99,000. In 30,589 the thousands digit is 0 and the next digit is 5, so it rounds up to 31,000.

Check: 98,530 is 470 from 99,000 and 530 from 98,000, and 30,589 is 411 from 31,000 and 589 from 30,000. Both answers are the nearer thousand.

</details>

6\. A whole number rounds to 2,500 when rounded to the nearest hundred, and to 3,000 when rounded to the nearest thousand. Which numbers could it be?

<details class="solution" markdown>
<summary>Solution</summary>

The numbers that round to 2,500 to the nearest hundred run from the halfway mark 2,450, which rounds up, to 2,549. The next number, 2,550, rounds to 2,600.

The numbers that round to 3,000 to the nearest thousand run from 2,500, which is halfway and rounds up, to 3,499.

Both conditions hold from 2,500 to 2,549, which is 50 numbers.

Check the ends and their neighbours. The number 2,500 rounds to 2,500 and to 3,000, and so does 2,549. Outside the range, 2,499 rounds to 2,000 to the nearest thousand, and 2,550 rounds to 2,600 to the nearest hundred.

</details>

## Where this shows up

- Carrying in [addition and subtraction](02-addition-and-subtraction.md) and the bring-down step of [long division](07-long-division.md) both rest on the fact from this lesson that ten of one place make one of the next.
- Decimals add places to the right of the ones, worth tenths, hundredths and so on, and rounding money to the cent follows the same rule as here: see [decimals: place value, adding and subtracting](12-decimals-place-value-and-adding.md). [Estimation and sanity checks](../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md) builds on estimating with rounded numbers.
- In code, rounding and truncating are different functions: `round(x)` rounds and `int(x)` truncates toward zero. [Floating point basics](../06-cs-math/01-number-representation/04-floating-point-basics.md) shows why a computer has to round almost every decimal it stores.
