# Mental addition and subtraction

After this lesson you can add and subtract numbers of up to four digits in your head, by working left to right, by rounding and adjusting and by counting up, and you can check each answer in three ways.

Before this: [addition and subtraction](../../01-elementary/02-addition-and-subtraction.md), [properties of operations](../../01-elementary/04-properties-of-operations.md) and [place value and rounding](../../01-elementary/01-place-value-and-rounding.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $398 + 247$ and $703 - 298$ in your head.
2. You pay for a \$13.65 purchase with a \$20 bill. How much change do you get?
3. Add \$3.99, \$12.49 and \$7.95.

<details class="solution" markdown>
<summary>Answers</summary>

1. $398 + 247 = 645$: adding 400 would be 2 too much, since $400 + 247 = 647$. And $703 - 298 = 405$: subtracting 300 takes away 2 too many, so give them back, $703 - 300 + 2 = 405$.
2. Count up from \$13.65. Another 35 cents reaches \$14, and \$6 more reaches \$20, so the change is \$6.35.
3. Round each price up: \$4.00, \$12.50 and \$8.00 add to \$24.50. The rounding added 1 cent, 1 cent and 5 cents, which is 7 cents, so the total is \$24.50 minus 7 cents, that is, \$24.43.

</details>

## The idea

A cashier giving change doesn't subtract. For a \$13.65 purchase paid with a \$20 bill, they start at \$13.65 and count up: "thirty-five cents makes fourteen, and six more makes twenty." The change is the sum of the jumps, \$6.35, and no digit was borrowed.

That is the first idea in this lesson: a subtraction can be an addition of gaps, and gaps are easy when you stop at round numbers. The second idea is the order of work. On paper you add from the right, because carries move left and each one is ready before you write the next digit. In your head the order flips. You say numbers from the left ("four thousand five hundred sixty-eight"), and the leftmost digits matter most for the size. Working left to right on paper would mean going back to change digits you had already written whenever a carry arrived, but in your head nothing is written. You keep one number in mind, the running total, add the big pieces first and replace the total at every step. If you stop early, the total is already a good estimate.

The third idea is that rounding can be undone. A number a little off a round one, such as 398, 2,997 or 1,002, can be rounded, used in the easy calculation and corrected afterwards. All three ideas come from the properties of operations, and each method below says in one line why it works.

## Definitions

A **running total** is the sum so far in a calculation done in several steps. At each step you add the next piece to it and replace the old total with the new one, so you only ever hold one number.

To **split by place value** is to write a number as the sum of its nonzero digits times powers of ten: $356 = 300 + 50 + 6$ and $4{,}002 = 4{,}000 + 2$. In plain words, you take the number apart at its places, biggest piece first.

To **round and adjust** (also called compensation) is to replace a number by a nearby round one, calculate with it, and correct the answer by the amount you moved. In symbols, for numbers $a$, $b$ and $c$,

$$
a + b = (a + c) + b - c.
$$

In plain words, if you add $c$ too much, take $c$ back. With $a = 398$, $b = 247$ and $c = 2$ this reads $398 + 247 = 400 + 247 - 2$.

To **count up** from $b$ to $a$, where $b \le a$, is to find $a - b$ as the sum of the gaps between friendly stopping points. For any $m$ with $b \le m \le a$,

$$
a - b = (m - b) + (a - m).
$$

In plain words, the distance from $b$ to $a$ is the distance from $b$ to $m$ plus the distance from $m$ to $a$, which is the meaning of subtraction as a distance from [negative numbers and absolute value](../01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md).

## How to do it

The elementary lesson already shows compensation and counting up for small numbers ([addition and subtraction](../../01-elementary/02-addition-and-subtraction.md#adding-and-subtracting-in-your-head)). Here the same ideas are stretched to four digits and to money, and joined by a way to check every answer.

### Adding left to right

1. Take the first number as your running total.
2. Split the second number by place value, largest piece first: $2{,}739 = 2{,}000 + 700 + 30 + 9$.
3. Add the largest piece to the running total. Say the new total in full, and forget the old one.
4. Repeat Step 3 with each remaining piece, until none is left.
5. Check the answer (see [Checking the answer](#checking-the-answer) below).

Why it works: $2{,}739 = 2{,}000 + 700 + 30 + 9$, so $4{,}568 + 2{,}739$ is the same as adding the four pieces one after another, and each addition is easy because you add a single digit at a time. This is the order taught in Arthur Benjamin and Michael Shermer's *Secrets of Mental Math* (2006). With practice you can take two digits at a time, as in $4{,}568 + 2{,}700 = 7{,}268$ and then $7{,}268 + 39 = 7{,}307$.

### Rounding and adjusting

1. Look for a number a little off a round one: it ends in 8 or 9, or sits just above a round number, as 1,002 does.
2. Replace it with the round number, and note how far you moved and in which direction.
3. Do the easy calculation with the round number.
4. Correct the answer with the move. If you added too much, take it back. If you took away too much, give it back.

Why it works: $398 = 400 - 2$, so $398 + 247 = 400 + 247 - 2$. For a subtraction, $298 = 300 - 2$, and subtracting a difference adds the second part back: $703 - (300 - 2) = 703 - 300 + 2$. Another way to handle a subtraction is to shift both numbers by the same amount, $703 - 298 = 705 - 300$, the trick from the [addition and subtraction lesson](../../01-elementary/02-addition-and-subtraction.md#tricks-and-shortcuts).

### Counting up

1. Start at the smaller number.
2. Jump to the next round number (the next ten, hundred, thousand or whole dollar) and note the size of the jump.
3. Keep jumping by the biggest round steps that don't pass the larger number. Make the last jump land exactly on it.
4. Add the jumps, biggest first.

For $1{,}000 - 637$ the jumps look like this:

```text
637 --(+3)--> 640 --(+60)--> 700 --(+300)--> 1,000        3 + 60 + 300 = 363
```

Why it works: each stop is an $m$ in the formula above, and the gaps add up to $a - b$.

### Subtracting left to right

1. Take the larger number as your running total.
2. Split the number you are subtracting by place value.
3. Subtract the largest piece, then the next, and so on, saying the running total each time.

For $842 - 359$ the totals are $842 - 300 = 542$, then $542 - 50 = 492$, then $492 - 9 = 483$. Why it works: taking away a number is the same as taking it away in pieces, so $842 - 359 = 842 - 300 - 50 - 9$.

Which of the subtraction methods to use depends on the numbers:

| Situation | Method | Example |
|---|---|---|
| the larger number is round, or you are making change | count up | $1{,}000 - 637$ |
| the numbers are close together | count up | $5{,}003 - 4{,}968$, a gap of $32 + 3 = 35$ |
| the number you subtract is just under a round one | round and adjust | $1{,}203 - 998$ |
| the digits of the lower number are small | subtract left to right | $842 - 359$ |

### Subtracting from a power of ten

The [elementary lesson](../../01-elementary/02-addition-and-subtraction.md#tricks-and-shortcuts) gives the rule for $1{,}000 - 637$: subtract each digit from 9 and the last digit from 10. Two extensions cover most cases.

- If the number is shorter than the power of ten, pad it with zeros on the left: $1{,}000 - 37 = 1{,}000 - 037 = 963$.
- If the number ends in zeros, leave them as zeros and take the last nonzero digit from 10: $10{,}000 - 3{,}070 = 6{,}930$, from $9 - 3 = 6$, $9 - 0 = 9$, $10 - 7 = 3$ and the final 0.

Why it works: $10{,}000 - n = (9{,}999 - n) + 1$, and subtracting from 9,999 never borrows. For $n = 3{,}070$ the zero in the ones place gives a 9, so $9{,}999 - 3{,}070 = 6{,}929$. Adding 1 turns that 9 into a 0 and carries into the tens place, where $9 - 7 = 2$ becomes $3$, which is $10 - 7$.

### Adding a column of prices

1. Round each price up to a friendly amount: the whole dollar if it is within 5 cents of one, otherwise the next 10 cents.
2. Note how many cents each rounding added.
3. Add the rounded prices from left to right.
4. Add up the cents you noted.
5. Subtract that total from the sum of the rounded prices.

For \$3.99, \$12.49, \$7.95, \$0.99, \$5.49 and \$2.29, the rounded prices are \$4.00, \$12.50, \$8.00, \$1.00, \$5.50 and \$2.30, which add to \$33.30. The roundings added $1 + 1 + 5 + 1 + 1 + 1 = 10$ cents, so the total is \$33.20.

Why it works: each price is its rounded price minus the cents you added, so the total of the prices is the total of the rounded prices minus the total of the roundings, which is rounding and adjusting applied to every term.

### Checking the answer

Run these checks from the quickest to the most thorough.

1. Size. Round each number to its first one or two digits and redo the calculation. For $4{,}568 + 2{,}739$, that is about $4{,}600 + 2{,}700 = 7{,}300$. This catches a wrong place value or a missing thousand.
2. Last digit. Every digit except the last stands for a multiple of 10, so the last digit of a sum depends only on the last digits of the numbers. For $4{,}568 + 2{,}739$ the last digits give $8 + 9 = 17$, so the sum ends in 7. For a difference, check that the answer plus the smaller number ends in the same digit as the larger number.
3. Casting out nines. Reduce each number to its digit sum, as in [multi-digit multiplication](../../01-elementary/05-multi-digit-multiplication.md#casting-out-nines), add the two results, and reduce again. Reduce the answer too. For a sum the two must match. For a difference, add the answer to the smaller number and compare with the larger. It works because a number and its digit sum leave the same remainder on division by 9, and remainders add.

No single check catches everything. Casting out nines misses swapped digits, which size catches, and size misses a slip of 10 or 100, which casting out nines catches.

## Worked examples

<div class="example" markdown>

### Example 1: adding four-digit numbers left to right

Work out $4{,}568 + 2{,}739$ without writing anything down.

Step 1: the running total starts at 4,568.

Step 2: split 2,739 into $2{,}000 + 700 + 30 + 9$.

Steps 3 and 4: add the pieces one at a time and say each total in full.

$$
4{,}568 + 2{,}000 = 6{,}568, \quad 6{,}568 + 700 = 7{,}268, \quad 7{,}268 + 30 = 7{,}298, \quad 7{,}298 + 9 = 7{,}307.
$$

In the second addition, 5 hundreds and 7 hundreds make 12 hundreds, so the thousands digit goes up by 1. Saying "seven thousand two hundred sixty-eight" in full builds that carry in.

Step 5: check all three ways. The size estimate is $4{,}600 + 2{,}700 = 7{,}300$, close to 7,307. The last digits give $8 + 9 = 17$, which ends in 7. For casting out nines, 4,568 gives $4 + 5 + 6 + 8 = 23$ and then 5, and 2,739 gives $2 + 7 + 3 + 9 = 21$ and then 3. Since $5 + 3 = 8$, and 7,307 gives $7 + 3 + 0 + 7 = 17$ and then 8, the answer passes.

The checks have different strengths. A slip to 7,317 passes the size and last-digit checks, but its digit sum is 9 and not 8, so casting out nines catches it. A slip to 7,037, with two digits swapped, passes the last digit and casting out nines, but 7,037 is far from the estimate 7,300.

</div>

<div class="example" markdown>

### Example 2: rounding and adjusting, in both directions

Work out $2{,}997 + 1{,}458$ and $1{,}203 - 998$.

For the sum, 2,997 is 3 below 3,000. Add 3,000 instead: $3{,}000 + 1{,}458 = 4{,}458$. That added 3 too much, so take 3 back: 4,455.

For the difference, 998 is 2 below 1,000. Subtract 1,000 instead: $1{,}203 - 1{,}000 = 203$. That took away 2 too many, so give 2 back: 205.

Check: $4{,}455 - 1{,}458 = 2{,}997$, counting up from 1,458 to 1,500 (42), to 4,000 (2,500) and to 4,455 (455), and $42 + 2{,}500 + 455 = 2{,}997$. And $205 + 998 = 1{,}203$, since $205 + 1{,}000 = 1{,}205$ and that is 2 too much.

</div>

<div class="example" markdown>

### Example 3: counting up through a zero, and a power of ten with zeros

Work out $5{,}003 - 1{,}768$ and $10{,}000 - 3{,}070$.

For the first, count up from 1,768. The jump to 1,800 is 32. The jump from 1,800 to 5,000 is 3,200. The last jump to 5,003 is 3. The gaps add to $32 + 3{,}200 + 3 = 3{,}235$. No borrowing across the zeros was needed.

For the second, the number ends in a zero. Keep that zero, take the last nonzero digit, 7, from 10, and take the others from 9: $9 - 3 = 6$, $9 - 0 = 9$, $10 - 7 = 3$. The answer is 6,930.

Check: $3{,}235 + 1{,}768 = 5{,}003$ (add 1,768 as $3{,}235 + 1{,}700 = 4{,}935$, then $+ 68 = 5{,}003$). And $6{,}930 + 3{,}070 = 10{,}000$, because $930 + 70 = 1{,}000$.

</div>

<div class="example" markdown>

### Example 4: a receipt and the change (finish it yourself)

A receipt lists \$6.99, \$3.49, \$12.95, \$2.99 and \$8.49, and you pay with a \$50 bill. What is the total, and what is the change?

Steps 1 and 2 of the column method: round each price up, to \$7.00, \$3.50, \$13.00, \$3.00 and \$8.50. The rounding added 1, 1, 5, 1 and 1 cents.

Steps 3 to 5 are left for you. Add the rounded prices, subtract the cents the rounding added, and then count up from the total to \$50 to find the change.

<details class="solution" markdown>
<summary>Finish</summary>

The rounded prices add to \$35.00: $7 + 3.50 + 13 + 3 + 8.50 = 35$. The rounding added 9 cents in all, so the total is \$34.91.

To find the change, count up from \$34.91. The jump to \$35.00 is 9 cents, and the jump from \$35 to \$50 is \$15, so the change is \$15.09.

Check: $34.91 + 15.09 = 50.00$, since 91 cents and 9 cents make a dollar and \$34 + \$15 + \$1 is \$50.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for a lost carry in the running total. Adding 50 to 778 gives 828, because 7 tens and 5 tens are 12 tens, which is 1 hundred and 2 tens. Changing only the tens digit, "778 and 50 is 728", forgets the hundred. Say the whole total each time, and test it against the size: $778 + 50$ must be a little over 800.

</div>

<div class="warning" markdown>

Watch out for the direction of the fix. In $1{,}203 - 998$, subtracting 1,000 takes away 2 too many, so the answer 203 is 2 too small and you add 2. Writing $1{,}203 - 1{,}000 - 2 = 201$ goes the wrong way. Adding back shows it: $201 + 998 = 1{,}199$, not 1,203.

</div>

<div class="warning" markdown>

Watch out for trailing zeros in "all from 9". For $1{,}000 - 640$, subtracting every digit from 9 gives $359$, which is $999 - 640$ and is 1 too small. The "from 10" belongs to the last nonzero digit, here the 4, so the answer is 360. Check: $360 + 640 = 1{,}000$.

</div>

<div class="warning" markdown>

Watch out for forgetting the overshoot in a column of prices. The rounded sum in Example 4 is \$35.00, but the true total is \$34.91, and the 9 cents decides the change. On a long receipt the roundings can add up to a dollar or more, so subtract them before you call the total final.

</div>

Counting up always gives a gap, which is never negative, so it can hide a sign. To work out $637 - 1{,}000$, count up from 637 to 1,000 for a gap of 363, then notice that 637 is the smaller number, so the answer is $-363$. Decide the sign by asking which number is larger before you start.

## Tricks and shortcuts

Near doubles and bridging both move an amount from one addend to the other, which keeps the sum the same, $a + b = (a + c) + (b - c)$. For $47 + 49$, move 1 from 49 to 47: $48 + 48 = 96$. To bridge to 100, move whatever the first number needs: for $87 + 76$, take 13 from 76 and give it to 87, so $100 + 63 = 163$.

To add 9, 19 or 29, add 10, 20 or 30 and take away 1. To subtract 9, 99 or 999, subtract 10, 100 or 1,000 and give 1 back: $4{,}786 - 2{,}999 = 4{,}786 - 3{,}000 + 1 = 1{,}787$.

In a long column, look for pairs that make a round number before you add anything, as the [addition lesson](../../01-elementary/02-addition-and-subtraction.md#tricks-and-shortcuts) suggests: $49 + 51 + 38 + 62 = 100 + 100 = 200$.

## In code

A seeded generator makes the same practice set every time, and a checker marks typed answers. The generator uses `random.Random(7)`, so the six problems below are the same on every run. To practise with your own typing, call `quiz(problems)` with no `replies`; the call at the bottom passes a list of answers instead so the example can run without a keyboard.

<details class="code" markdown>
<summary>In code</summary>

```python
import random

def make_problems(seed, n=6):
    rng = random.Random(seed)
    problems = []
    for _ in range(n):
        a, b = rng.randint(120, 4999), rng.randint(120, 4999)
        if rng.random() < 0.5:
            problems.append((f"{a} + {b}", a + b))
        else:
            big, small = max(a, b), min(a, b)
            problems.append((f"{big} - {small}", big - small))
    return problems

def quiz(problems, replies=None):
    score = 0
    for i, (text, answer) in enumerate(problems):
        reply = replies[i] if replies else input(f"{text} = ")
        right = reply.strip().replace(",", "") == str(answer)
        score += right
        print(f"{text} = {reply}", "right" if right else f"wrong, it is {answer}")
    print(f"score: {score} out of {len(problems)}")

problems = make_problems(seed=7)
quiz(problems, replies=["4,127", "198", "2,234", "6,154", "7,117", "5,497"])
```

The run prints this. The two wrong replies are off by 10 and by 100, the size of a lost carry.

```text
2772 + 1355 = 4,127 right
713 - 515 = 198 right
3115 - 891 = 2,234 wrong, it is 2224
4276 + 1878 = 6,154 right
3672 + 3545 = 7,117 wrong, it is 7217
863 + 4634 = 5,497 right
score: 4 out of 6
```

</details>

## FAQ

### Why not use the written method in my head?

The written method needs you to hold a carry or a borrow for each column and keep the digits you have already found, and a slip in any of them spoils the answer with no warning. The running-total method holds one number and gives a rough answer after the first step. The written method is still the right tool when you can write.

### What do I do when I lose the number halfway?

Go back to the last total you said and carry on from there. Saying each total under your breath leaves a trace to return to. Practise with three-digit numbers until each piece-by-piece addition is automatic, since that frees room for the next piece. Working memory is small, which is why the methods replace the total at every step and never pile up several partial results.

### Do these methods work with decimals and money?

Yes, because they only use place value and the properties of addition, and both hold for decimals. A price of \$13.65 is 13 dollars and 65 cents, and you can treat the cents as a two-digit number, as in the change example. Keep the decimal point in the same place in every number you add.

## Practice

### Warm-up

1\. Add left to right, saying each running total: (a) $365 + 428$, (b) $1{,}847 + 2{,}356$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $365 + 400 = 765$, then $765 + 20 = 785$, then $785 + 8 = 793$.

(b) $1{,}847 + 2{,}000 = 3{,}847$, then $3{,}847 + 300 = 4{,}147$, then $4{,}147 + 50 = 4{,}197$, then $4{,}197 + 6 = 4{,}203$.

Check: for (a) the last digits give $5 + 8 = 13$, so it ends in 3, and the size is $370 + 430 = 800$. For (b), $7 + 6 = 13$ ends in 3, and the size is $1{,}800 + 2{,}400 = 4{,}200$.

</details>

2\. Round and adjust: (a) $599 + 387$, (b) $4{,}998 + 2{,}745$, (c) $835 - 298$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Add 600 instead of 599, then take 1 back: $600 + 387 - 1 = 986$.

(b) Add 5,000 instead of 4,998, then take 2 back: $5{,}000 + 2{,}745 - 2 = 7{,}743$.

(c) Subtract 300 instead of 298, then give 2 back: $835 - 300 + 2 = 537$.

Check: $537 + 298 = 835$, since $537 + 300 = 837$ is 2 too much. The sums pass the size check: $600 + 400 = 1{,}000$ is near 986, and $5{,}000 + 2{,}700$ is near 7,743.

</details>

3\. Find the change from a \$20 bill for a \$7.35 purchase, and from a \$50 bill for a \$37.42 purchase.

<details class="solution" markdown>
<summary>Solution</summary>

For the first, count up from \$7.35: 65 cents reaches \$8.00, and \$12 more reaches \$20, so the change is \$12.65.

For the second, count up from \$37.42: 58 cents reaches \$38.00, and \$12 more reaches \$50, so the change is \$12.58.

Check: $7.35 + 12.65 = 20.00$ and $37.42 + 12.58 = 50.00$, because 35 and 65 cents, and 42 and 58 cents, each make a dollar.

</details>

### Standard

4\. Subtract from a power of ten: (a) $1{,}000 - 468$, (b) $10{,}000 - 4{,}370$, (c) $1{,}000 - 640$, (d) $1{,}000 - 37$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Take each digit from 9 and the last from 10: $9 - 4 = 5$, $9 - 6 = 3$, $10 - 8 = 2$, so 532.

(b) The number ends in a zero, so the last nonzero digit, 7, is taken from 10: $9 - 4 = 5$, $9 - 3 = 6$, $10 - 7 = 3$, then the zero, so 5,630.

(c) The last nonzero digit is 4: $9 - 6 = 3$ and $10 - 4 = 6$, then the zero, so 360.

(d) Pad to 037: $9 - 0 = 9$, $9 - 3 = 6$, $10 - 7 = 3$, so 963.

Check by adding back: $532 + 468 = 1{,}000$, $5{,}630 + 4{,}370 = 10{,}000$, $360 + 640 = 1{,}000$ and $963 + 37 = 1{,}000$.

</details>

5\. A receipt lists \$4.99, \$2.49, \$9.95, \$1.99, \$6.49 and \$3.29. (a) Find the total with the round-up method. (b) What is the change from \$50?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Round each price up: \$5.00 (1 cent added), \$2.50 (1), \$10.00 (5), \$2.00 (1), \$6.50 (1) and \$3.30 (1). The rounded prices add to \$29.30, and the roundings added $1 + 1 + 5 + 1 + 1 + 1 = 10$ cents, so the total is \$29.20.

(b) Count up from \$29.20: 80 cents reaches \$30, and \$20 more reaches \$50, so the change is \$20.80.

Check: adding the dollars first gives $4 + 2 + 9 + 1 + 6 + 3 = 25$, and the cents are $99 + 49 + 95 + 99 + 49 + 29 = 420$, which is \$4.20, so the total is $25 + 4.20 = 29.20$. And $29.20 + 20.80 = 50.00$.

</details>

6\. A classmate says that $3{,}849 + 2{,}675 = 6{,}424$. Run the size, last-digit and casting-out-nines checks. Which ones catch the error, and what is the right answer?

<details class="solution" markdown>
<summary>Solution</summary>

Size: $3{,}800 + 2{,}700 = 6{,}500$, and 6,424 is within the roughness of the estimate, so this check does not catch the error. Last digit: $9 + 5 = 14$, so the sum should end in 4, and 6,424 does. Casting out nines: 3,849 gives $24$ and then 6, and 2,675 gives $20$ and then 2, so the sum should reduce to $6 + 2 = 8$. But 6,424 gives $16$ and then 7, so it fails.

The error is 100, which is invisible to the last digit and to a rough estimate, and casting out nines catches it. The right sum, left to right, is $3{,}849 + 2{,}000 = 5{,}849$, then $+ 600 = 6{,}449$, then $+ 70 = 6{,}519$, then $+ 5 = 6{,}524$.

Check: 6,524 gives $17$ and then 8, which matches, and it ends in 4.

</details>

### Challenge

7\. A chequing account starts the week at \$1,240.50. Track the balance in your head after each of these: rent, $-\$725.00$; groceries, $-\$87.35$; a paycheque, $+\$650.00$; a subscription, $-\$49.99$; a transfer, $-\$15.00$.

<details class="solution" markdown>
<summary>Solution</summary>

After the rent: $1{,}240.50 - 725 = 515.50$, since $1{,}240 - 725 = 515$.

After the groceries: subtract 87 to get 428.50, then subtract 35 cents to get \$428.15.

After the paycheque: $428.15 + 650 = 1{,}078.15$.

After the subscription: subtract 50 and give 1 cent back, $1{,}078.15 - 50 + 0.01 = 1{,}028.16$.

After the transfer: $1{,}028.16 - 15 = 1{,}013.16$.

Check: the net change is $-725 - 87.35 + 650 - 49.99 - 15 = -227.34$, and $1{,}240.50 - 227.34 = 1{,}013.16$.

</details>

8\. (Reviews [negative numbers and absolute value](../01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md).) (a) Work out $637 - 1{,}000$ by counting up. (b) Find the distance between $-48$ and 75 on the number line. (c) Explain, using distance, why $5{,}003 - 1{,}768 = 5{,}035 - 1{,}800$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Counting up from 637 to 1,000 gives a gap of 363. Since 637 is the smaller number, the difference is negative: $-363$.

(b) From $-48$ up to 0 is 48, and from 0 up to 75 is 75, so the distance is $48 + 75 = 123$.

(c) The difference $5{,}003 - 1{,}768$ is the distance from 1,768 to 5,003. Moving both numbers up by 32 moves both ends of the gap by the same amount, so the distance between them stays the same: 1,768 becomes 1,800, and 5,003 becomes 5,035.

Check: (a) $-363 + 1{,}000 = 637$. (b) $75 - (-48) = 123$. (c) Both differences are 3,235, from $32 + 3{,}200 + 3$ and from $5{,}035 - 1{,}800$.

</details>

### Drill

Do these in your head, in under a minute each at first. Then open the answers and compare your method with the fastest one.

1. $38 + 47$
2. $64 + 29$
3. $273 + 148$
4. $456 + 299$
5. $1{,}250 + 3{,}875$
6. $87 - 39$
7. $200 - 76$
8. $523 - 187$
9. $1{,}000 - 723$
10. $5{,}000 - 2{,}346$
11. $10{,}000 - 6{,}300$
12. $1{,}402 - 998$
13. Change from \$100 for a \$37.65 bill
14. Change from \$20 for a \$14.85 bill
15. The total of \$2.99, \$4.99 and \$6.99
16. The total of \$12.50, \$7.75 and \$3.25
17. $3{,}456 + 2{,}789$
18. $7{,}004 - 3{,}896$
19. $49 + 51 + 38 + 62$
20. True or false: $7{,}846 - 2{,}958 = 4{,}988$

<details class="solution" markdown>
<summary>Answers and fastest tricks</summary>

1. 85. Make a ten: $38 + 2 = 40$, then $40 + 45$.
2. 93. Round and adjust: $64 + 30 - 1$.
3. 421. Left to right: $273 + 100 = 373$, $+ 40 = 413$, $+ 8 = 421$.
4. 755. Round and adjust: $456 + 300 - 1$.
5. 5,125. Left to right: $1{,}250 + 3{,}000 = 4{,}250$, $+ 800 = 5{,}050$, $+ 75 = 5{,}125$.
6. 48. Round and adjust: $87 - 40 + 1$.
7. 124. Count up: 76 to 80 is 4, and 80 to 200 is 120.
8. 336. Round and adjust: $523 - 200 + 13$, since 187 is 13 below 200.
9. 277. All from 9, the last from 10: 2, 7, 7.
10. 2,654. Count up: 2,346 to 2,350 is 4, to 2,400 is 50, to 5,000 is 2,600, and $4 + 50 + 2{,}600 = 2{,}654$.
11. 3,700. Drop the two zeros, $100 - 63 = 37$, and put the zeros back.
12. 404. Round and adjust: $1{,}402 - 1{,}000 + 2$.
13. \$62.35. Count up: 35 cents to \$38.00, then \$62 to \$100.
14. \$5.15. Count up: 15 cents to \$15.00, then \$5 to \$20.
15. \$14.97. Three prices are each 1 cent under \$3, \$5 and \$7, so $15 - 0.03$.
16. \$23.50. Pair the quarters first: $7.75 + 3.25 = 11.00$, then $+ 12.50$.
17. 6,245. Left to right: $3{,}456 + 2{,}000 = 5{,}456$, $+ 700 = 6{,}156$, $+ 80 = 6{,}236$, $+ 9 = 6{,}245$.
18. 3,108. Round and adjust: $7{,}004 - 3{,}900 + 4$, since 3,896 is 4 below 3,900.
19. 200. Pairs that make 100: $49 + 51$ and $38 + 62$.
20. False. The last-digit check passes, but casting out nines catches it: 4,988 gives 2 and 2,958 gives 6, so $2 + 6 = 8$, while 7,846 gives 7. The true difference is $7{,}846 - 3{,}000 + 42 = 4{,}888$.

</details>

## Where this shows up

- The next lesson, [Mental multiplication and division](02-mental-multiplication-and-division.md), uses the running total to add up partial products, and Percents, fractions and money in your head<!-- link: 03-percents-fractions-and-money-in-your-head.md --> uses it for tips, change and tax. The size and last-digit checks reappear in [estimation and sanity checks](../04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md).
- In computing, "all from 9, the last from 10" is the decimal ancestor of two's complement. Subtracting from $10^k$ is subtracting from $10^k - 1$ and adding 1, and in binary, flipping every bit and adding 1 does the same job ([binary arithmetic and two's complement](../../06-cs-math/01-number-representation/03-binary-arithmetic-and-twos-complement.md)). Why casting out nines works is modular arithmetic ([divisibility and modular arithmetic](../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md)).
- Money is mental addition all day: totals at the till, change, and running balances in a chequing account.
