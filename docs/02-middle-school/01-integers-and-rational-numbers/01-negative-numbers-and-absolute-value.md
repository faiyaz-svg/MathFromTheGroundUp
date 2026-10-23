# Negative numbers and absolute value

After this lesson you can place negative numbers on the number line, compare and order them, find absolute values, and find the distance between two numbers, which is written $\lvert a - b \rvert$.

Before this: [place value and rounding](../../01-elementary/01-place-value-and-rounding.md) and [addition and subtraction](../../01-elementary/02-addition-and-subtraction.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Put these numbers in order from least to greatest: $4$, $-6$, $0$, $-1$, $-12$.
2. Find $\lvert -9 \rvert$, $\lvert 9 \rvert$ and $-\lvert -9 \rvert$.
3. A thermometer reads $-18$°C at 7 a.m. and 5°C at 3 p.m. How many degrees apart are the two readings?

<details class="solution" markdown>
<summary>Answers</summary>

1. The order is $-12$, $-6$, $-1$, $0$, $4$. Every negative number is less than 0, and among the negatives, the one furthest from 0 is the least.
2. They are 9, 9 and $-9$. The bars give the distance from 0, and the minus sign outside the bars in the third one stays.
3. 23 degrees. The readings are on opposite sides of 0, so add their distances from 0: $18 + 5 = 23$.

</details>

## The idea

The Celsius scale puts 0 at the temperature where water freezes. A January morning in Ottawa can be 15 degrees colder than that, and we write it as $-15$°C, read "negative fifteen degrees". No whole number describes it, because there is no whole number below 0. Negative numbers fill that gap.

The same thing happens whenever a quantity has a natural zero and can go either way from it. A bank balance of 0 means you have nothing and owe nothing; spend \$40 more than you have, and the balance is $-40$ dollars. A diver 12 m below the surface of a lake is at an elevation of $-12$ m, measured from the surface. In each case the sign says which side of zero you are on, and the number after it says how far.

The number line shows all of this at once. Mark the whole numbers at equal steps to the right of 0, then mirror them on the left:

```text
<---+----+----+----+----+----+----+----+----+----+----+----+----+-->
   -6   -5   -4   -3   -2   -1    0    1    2    3    4    5    6
```

Each negative number is the mirror image of a positive one: $-3$ is as far left of 0 as 3 is right of it. Numbers increase from left to right, so $-15$°C is colder than $-4$°C because $-15$ sits further left. Two measurements come up all the time. One is the distance of a number from 0, ignoring the side, which is called its absolute value. The other is the distance between two points, which is what you want when you ask how many degrees warmer one city is than another.

## Definitions

A **positive number** is a number greater than 0, and a **negative number** is a number less than 0. Zero is neither positive nor negative. A number that is positive or 0 is **non-negative**.

The **number line** is a straight line with one point marked 0, on which each number is a point. A positive number $x$ lies $x$ units to the right of 0, and the negative number $-x$ lies $x$ units to the left. In plain words, it is a ruler that goes on forever in both directions.

For numbers $a$ and $b$, the statement $a < b$ ("$a$ is less than $b$") means that $a$ lies to the left of $b$ on the number line. The statement $a > b$ means that $a$ lies to the right of $b$, so $-7 < -2$ and $-2 > -7$ say the same thing. As before, $a \le b$ means "$a < b$ or $a = b$".

The **opposite** of a number $a$, written $-a$, is the number at the same distance from 0 on the other side. So the opposite of 7 is $-7$, the opposite of $-7$ is 7, and the opposite of 0 is 0. Taking the opposite twice gets you back where you started, so $-(-7) = 7$.

The minus sign has three jobs, and it helps to read each one aloud differently:

| Written | Read | Meaning |
|---|---|---|
| $9 - 4$ | nine minus four | subtraction, between two numbers |
| $-4$ | negative four | part of the number: the point 4 units left of 0 |
| $-a$ | the opposite of $a$ | flip $a$ to the other side of 0 |

The third job causes most of the trouble, because $-a$ is not always negative. If $a = -7$, then $-a = -(-7) = 7$, which is positive. Reading $-a$ as "the opposite of $a$" rather than "negative $a$" keeps you from assuming its sign.

The **integers** are the whole numbers together with their opposites:

$$
\mathbb{Z} = \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}.
$$

The symbol $\mathbb{Z}$ names the set of all integers, and the dots mean that the list goes on forever in both directions. In plain words, the integers are the numbers with no fractional part: $-12$ and 40 are integers, while $-2.5$ and $\frac{1}{3}$ are not. In this book the natural numbers are $\mathbb{N} = \{0, 1, 2, \ldots\}$ ([symbols and notation](../../reference/symbols-and-notation.md#number-sets)), so every natural number is an integer, but not every integer is a natural number.

The **absolute value** of a number $x$, written $\lvert x \rvert$, is the distance from $x$ to 0 on the number line. As a formula,

$$
\lvert x \rvert = \begin{cases} x & \text{if } x \ge 0, \\ -x & \text{if } x < 0. \end{cases}
$$

The brace with two lines is a definition by cases: use the line whose condition is true for your $x$. In plain words, absolute value keeps the size of a number and drops its sign, so $\lvert -6 \rvert = 6$, $\lvert 6 \rvert = 6$ and $\lvert 0 \rvert = 0$. The second line looks wrong at first, as if it said that an absolute value can be negative. It can't be: that line is used only when $x$ is negative, and then $-x$ is the opposite of a negative number, which is positive. For $x = -6$ the second line gives $-(-6) = 6$.

The **distance** between two numbers $a$ and $b$ on the number line is $\lvert a - b \rvert$. For example, the distance between 3 and 8 is $\lvert 3 - 8 \rvert = \lvert -5 \rvert = 5$. It is also $\lvert 8 - 3 \rvert = 5$, because a distance doesn't depend on which end you start from. When $a$ or $b$ is negative, working out $a - b$ needs the subtraction rules of the next lesson, so this lesson finds distances by counting along the line. Counting gives the same number the formula does.

## How to do it

### Comparing and ordering numbers

1. Sort by sign: the negative numbers come first, then 0, then the positive numbers.
2. Compare two positive numbers as usual. The one with the bigger absolute value is the bigger number.
3. Compare two negative numbers by absolute value, the other way round. The one with the bigger absolute value is further left, so it is the smaller number: $-9 < -4$ because $9 > 4$.
4. Check with a picture. On a thermometer the lower reading is the smaller number, and between two bank balances the bigger debt is the smaller number.

### Finding an absolute value

1. Work out the number inside the bars first. The bars group what is inside them, as brackets do.
2. If that number is 0 or positive, the absolute value is the number itself. If it is negative, the absolute value is its opposite.
3. Keep every sign outside the bars: $-\lvert -5 \rvert = -5$.

### Finding the distance between two numbers

1. If one of the numbers is 0, the distance is the absolute value of the other.
2. If the numbers have the same sign, they are on the same side of 0. Subtract the smaller absolute value from the larger.
3. If they have opposite signs, 0 lies between them. Add the absolute values.
4. Check by counting along the number line. A distance is never negative.

## Worked examples

<div class="example" markdown>

### Example 1: ordering temperatures

Say the overnight lows in five cities one January night were Toronto $-8$°C, Vancouver 3°C, Winnipeg $-27$°C, Halifax $-4$°C and Montreal $-15$°C. Put the cities in order from coldest to warmest, and find how many degrees warmer the warmest city was than the coldest.

Step 1 of comparing: Vancouver's 3 is the only positive reading, so Vancouver was the warmest. The other four readings are negative and come before it.

Step 3: compare the four negative readings by absolute value. The absolute values are 8, 27, 4 and 15, and in decreasing order they are $27 > 15 > 8 > 4$. A bigger absolute value means a smaller negative number, so the order is reversed:

$$
-27 < -15 < -8 < -4 < 3.
$$

From coldest to warmest, that is Winnipeg, Montreal, Toronto, Halifax, Vancouver.

<div class="warning" markdown>

Watch out: comparing the digits alone gives the order backwards. The number $-27$ has bigger digits than $-4$, but it is further left, so it is the smaller number. A $-27$°C night is colder than a $-4$°C night, and colder means less.

</div>

For the gap, use Step 3 of finding a distance. The readings 3 and $-27$ have opposite signs, so add the absolute values: $27 + 3 = 30$. Vancouver was 30 degrees warmer than Winnipeg.

Step 4 of the distance method: count on the thermometer. From $-27$ up to 0 is 27 degrees, and from 0 up to 3 is 3 more, so 30 in all. The answer should also be more than 27, because 0 lies between the two readings and Winnipeg alone is 27 degrees from 0.

</div>

<div class="example" markdown>

### Example 2: absolute values

Work out (a) $\lvert -14 \rvert$, (b) $\lvert 3 \rvert + \lvert -8 \rvert$, (c) $-\lvert -5 \rvert$, (d) $\lvert 3 - 8 \rvert$ and (e) $\lvert -(-2) \rvert$.

- (a) The number $-14$ is negative, so its absolute value is its opposite, 14.
- (b) Each absolute value first: $3 + 8 = 11$.
- (c) Inside the bars, $\lvert -5 \rvert = 5$. The minus sign outside stays (Step 3), so the answer is $-5$.
- (d) Work inside the bars first (Step 1): $3 - 8 = -5$, a negative number, as in [addition and subtraction](../../01-elementary/02-addition-and-subtraction.md). Then $\lvert -5 \rvert = 5$.
- (e) Inside, $-(-2) = 2$, and $\lvert 2 \rvert = 2$.

Check (d) by counting: from 3 to 8 on the number line is 5 steps, which is the distance between 3 and 8.

</div>

<div class="example" markdown>

### Example 3: which numbers have a given absolute value

(a) Find every number $x$ with $\lvert x \rvert = 5$. These are the points at distance 5 from 0, and there are two of them, one on each side: $x = 5$ and $x = -5$.

(b) Find every $x$ with $\lvert x \rvert = 0$. Only 0 is at distance 0 from 0, so $x = 0$.

(c) Find every $x$ with $\lvert x \rvert = -2$. A distance can't be negative, so no number works. "There is no such number" is a complete and correct answer.

(d) List every integer $x$ with $\lvert x \rvert \le 2$. These are the integers within 2 steps of 0: $-2$, $-1$, $0$, $1$ and $2$.

Check (a): $\lvert 5 \rvert = 5$, and $\lvert -5 \rvert = -(-5) = 5$ by the second line of the definition. Equations and inequalities like these come back, with harder insides, in [absolute value equations and inequalities](../../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md).

</div>

<div class="example" markdown>

### Example 4: a bank balance (finish it yourself)

On Monday your chequing account is overdrawn by \$35, a balance of $-35$ dollars. On Friday, after payday, the balance is \$120. By how much did the balance go up?

The balance went up, so the amount it rose is the distance between $-35$ and 120 on the number line.

The numbers have opposite signs, so Step 3 of finding a distance applies: add the absolute values. The absolute values are $\lvert -35 \rvert = 35$ and $\lvert 120 \rvert = 120$.

Now add them, and check by counting in two pieces.

<details class="solution" markdown>
<summary>Finish</summary>

The sum is $35 + 120 = 155$, so the balance went up by \$155.

Check: the first \$35 of the pay clears the overdraft and brings the balance to 0, and the other \$120 is the balance you see on Friday. Together that is $35 + 120 = 155$.

</details>

</div>

## Edge cases and common mistakes

The mistake of ordering negative numbers by their digits is flagged in Example 1. Here are the others.

<div class="warning" markdown>

Watch out: absolute value bars group, so work inside them first. The value of $\lvert 3 - 8 \rvert$ is $\lvert -5 \rvert = 5$, but $\lvert 3 \rvert - \lvert 8 \rvert = 3 - 8 = -5$. Absolute value does not mean "make every number positive and then calculate". It turns the single number inside the bars into its distance from 0.

</div>

<div class="warning" markdown>

Watch out: $-x$ is not always negative. When $x$ is negative, the definition gives $\lvert x \rvert = -x$, which looks like a negative answer but is a positive one. With $x = -6$, the number $-x$ is $-(-6) = 6$. Before you decide the sign of an expression with a letter in it, ask what sign the letter has.

</div>

<div class="warning" markdown>

Watch out: a minus sign outside the bars is not removed by them. Both $-\lvert 4 \rvert$ and $-\lvert -4 \rvert$ are $-4$. An absolute value is never negative, but the opposite of an absolute value, $-\lvert x \rvert$, is never positive.

</div>

Zero is the boundary case. It is neither positive nor negative, its opposite is itself ($-0 = 0$), and its absolute value is 0. The words "positive" and "non-negative" differ only at 0, and that difference matters in definitions: the natural numbers in this book are the non-negative integers, while the positive integers $\mathbb{Z}^+ = \{1, 2, 3, \ldots\}$ leave 0 out.

Everyday words can mislead. For numbers, "smaller" means further left, not closer to 0. The number $-3$ is smaller than $-0.5$, even though $-0.5$ is closer to 0. When you mean closer to 0, say "smaller in absolute value": $-0.5$ is smaller in absolute value than $-3$.

## Tricks and shortcuts

Taking opposites reverses the order. Since $2 < 5$, the mirror images satisfy $-2 > -5$: the mirror swaps left and right. In symbols, if $a < b$, then $-a > -b$. The same flip happens when you multiply both sides of an inequality by a negative number, in [inequalities](../03-expressions-equations-inequalities/05-inequalities.md).

For distances, remember "same sides, subtract; opposite sides, add". The distance from $-6$ to $-15$ is $15 - 6 = 9$, and the distance from $-6$ to 15 is $6 + 15 = 21$.

To find the numbers at a given distance from a point, count that many steps each way. The numbers at distance 5 from $-2$ are $-7$ (five steps left) and 3 (five steps right). The number halfway between two numbers is the same distance from each: halfway between $-9$ and 3 is $-3$, which is 6 from both.

Every nonzero number is a sign together with an absolute value. Thinking of $-27$ as "negative, size 27" is what makes the comparison and distance rules quick: the sign tells you the side of 0, and the size tells you how far.

## In code

Python orders negative numbers correctly, and `abs` gives the absolute value. Sorting with `key=abs` sorts by distance from 0, and the last line shows the usual way to compare two floats: ask whether the distance between them is tiny.

<details class="code" markdown>
<summary>In code</summary>

```python
temps = [-8, 3, -27, -4, -15]
print(sorted(temps))              # [-27, -15, -8, -4, 3]
print(min(temps), max(temps))     # -27 3
print(abs(-27), abs(3), abs(0))   # 27 3 0
print(sorted(temps, key=abs))     # [3, -4, -8, -15, -27]
print(abs(3 - (-27)))             # 30, the distance between 3 and -27
print(0.1 + 0.2 == 0.3, abs((0.1 + 0.2) - 0.3) < 1e-9)  # False True
```

The sum `0.1 + 0.2` is not stored as exactly 0.3 (the reason is in [multiplying and dividing decimals](../../01-elementary/13-multiplying-and-dividing-decimals.md#in-code)), so `==` says the two differ. Their distance is about $5.6 \times 10^{-17}$, far below the tolerance `1e-9`, which is $10^{-9}$. The function `math.isclose` does the same test with a sensible default tolerance.

</details>

## FAQ

### Is 0 positive or negative?

Neither. Zero is the point that separates the positive numbers from the negative ones, and it belongs to neither side. When a statement needs to include 0 along with the positive numbers, the word is "non-negative": the absolute value of every number is non-negative, and so is every natural number in this book.

### Why does the definition of absolute value need two cases?

"Drop the minus sign" works on a number you can see, such as $-6$. It doesn't work on $\lvert x \rvert$, because the letter shows no sign to drop: you don't know whether $x$ is positive or negative. The definition by cases says what to do either way. Proofs about absolute value use it by splitting into cases, one for each line, as in Practice problem 7.

### Why is the opposite of negative 5 equal to 5?

The opposite of $-5$ is the number at the same distance from 0 on the other side, and that number is 5. Flipping twice brings you back. The next lesson gives the algebra version: the opposite of a number is the number you add to it to get 0, and since $-5 + 5 = 0$, the opposite of $-5$ is 5.

### Does the order matter in the distance formula?

No: $\lvert a - b \rvert = \lvert b - a \rvert$. The numbers $a - b$ and $b - a$ are opposites (the next lesson shows why), and opposites have the same absolute value, which Practice problem 7 proves. That matches the picture, since walking from $a$ to $b$ covers the same distance as walking from $b$ to $a$.

## Practice

### Warm-up

1\. Write each quantity as an integer: (a) 14 degrees below zero, (b) a deposit of \$250, (c) the third parking level below the ground floor, (d) a drop of 6 points in a stock index.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Below zero is negative: $-14$.
- (b) A deposit adds to the balance: 250.
- (c) The levels below the ground floor are negative, counting down from 0: $-3$.
- (d) A drop is a change in the negative direction: $-6$.

Check: the three negative answers are the quantities described with "below" or "drop", and the deposit, the only amount that adds to something, is positive.

</details>

2\. Write $<$ or $>$ between each pair: (a) $-3$ and $-8$, (b) $-1$ and 0, (c) $-15$ and 2, (d) $-100$ and $-99$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Both are negative, and 8 is the bigger absolute value, so $-8$ is smaller: $-3 > -8$.
- (b) Every negative number is less than 0: $-1 < 0$.
- (c) A negative number is less than a positive one: $-15 < 2$.
- (d) The absolute value 100 is bigger than 99, so $-100$ is further left: $-100 < -99$.

Check with a thermometer: $-3$°C is warmer than $-8$°C, and $-100$ degrees is colder than $-99$ degrees.

</details>

3\. Work out (a) $\lvert -23 \rvert$, (b) $-\lvert 23 \rvert$, (c) $\lvert 0 \rvert$, (d) $-(-(-4))$ and (e) $\lvert -6 \rvert + \lvert 2 \rvert$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The opposite of $-23$: 23.
- (b) The absolute value is 23, and the minus sign outside stays: $-23$.
- (c) Zero is at distance 0 from itself: 0.
- (d) Work from the inside out: $-(-4) = 4$, and then $-(4) = -4$. Three minus signs, an odd number of flips, leave the number negative.
- (e) Each absolute value first: $6 + 2 = 8$.

Check (d) on the number line: start at 4, flip to $-4$, flip back to 4, flip again to $-4$.

</details>

### Standard

4\. Put these numbers in order from least to greatest: $-2.5$, $1$, $-3$, $-\frac{1}{2}$, $0$, $-2$.

<details class="solution" markdown>
<summary>Solution</summary>

Step 1: the negative numbers are $-2.5$, $-3$, $-\frac{1}{2}$ and $-2$; then come 0 and 1.

Step 3: the absolute values of the negatives are 2.5, 3, 0.5 and 2. From biggest to smallest they are $3 > 2.5 > 2 > 0.5$, so from least to greatest the negatives are $-3$, $-2.5$, $-2$, $-\frac{1}{2}$. The full order is

$$
-3 < -2.5 < -2 < -\tfrac{1}{2} < 0 < 1.
$$

Check: $-2.5$ is halfway between $-3$ and $-2$, so it belongs between them, and $-\frac{1}{2}$ is the negative number closest to 0, so it comes last among the negatives.

</details>

5\. Find the distance between (a) $-6$ and $-15$, (b) $-6$ and 15, (c) 0 and $-42$. (d) A freezer is set to $-18$°C and a fridge to 4°C. How many degrees colder is the freezer?

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Same sign, so subtract the absolute values: $15 - 6 = 9$.
- (b) Opposite signs, so add: $6 + 15 = 21$.
- (c) One number is 0, so the distance is $\lvert -42 \rvert = 42$.
- (d) The readings $-18$ and 4 have opposite signs, so the freezer is $18 + 4 = 22$ degrees colder.

Check (a) by counting: from $-15$, nine steps right reach $-6$. Check (d): from $-18$ up to 0 is 18 degrees, and 4 more reach the fridge.

</details>

6\. (a) Which numbers are at distance 4 from $-1$? (b) List every integer whose distance from $-5$ is at most 2. (c) Which number is the same distance from $-9$ as from 3?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Count 4 steps each way from $-1$. Four steps left reach $-5$ and four steps right reach 3, so the numbers are $-5$ and 3.

(b) The integers from 2 steps left of $-5$ to 2 steps right of it: $-7$, $-6$, $-5$, $-4$ and $-3$.

(c) The distance from $-9$ to 3 is $9 + 3 = 12$, since they have opposite signs. The point halfway is 6 from each end: six steps right of $-9$ is $-3$. So the number is $-3$.

Check: (a) the distance between $-5$ and $-1$ is $5 - 1 = 4$, and between 3 and $-1$ it is $3 + 1 = 4$. (c) The distance from $-3$ to $-9$ is $9 - 3 = 6$, and from $-3$ to 3 it is $3 + 3 = 6$.

</details>

### Challenge

7\. Use the definition of absolute value by cases to prove that for every number $x$, (a) $\lvert x \rvert \ge 0$ and (b) $\lvert -x \rvert = \lvert x \rvert$. You may use the fact that the opposite of a positive number is negative and the opposite of a negative number is positive.

<details class="solution" markdown>
<summary>Solution</summary>

We know the definition of $\lvert x \rvert$, which has one line for $x \ge 0$ and one for $x < 0$, and the fact about opposites. We want both statements for every number $x$. The plan is a proof by cases: every number is positive, zero or negative, so if each case works, every number works.

*Proof of (a).* If $x \ge 0$, the first line gives $\lvert x \rvert = x$, which is at least 0. If $x < 0$, the second line gives $\lvert x \rvert = -x$, the opposite of a negative number, which is positive. In both cases $\lvert x \rvert \ge 0$.

*Proof of (b).* There are three cases.

- If $x > 0$, then $-x < 0$, so the second line applied to $-x$ gives $\lvert -x \rvert = -(-x) = x$. The first line gives $\lvert x \rvert = x$. The two sides are equal.
- If $x = 0$, then $-x = 0$, and both sides are $\lvert 0 \rvert = 0$.
- If $x < 0$, then $-x > 0$, so the first line applied to $-x$ gives $\lvert -x \rvert = -x$. The second line gives $\lvert x \rvert = -x$. The two sides are equal again.

Look back: part (b) needed three cases, not two, because the sign of $-x$ depends on whether $x$ is positive, zero or negative. Check one value: with $x = -6$, the left side is $\lvert 6 \rvert = 6$ and the right side is $\lvert -6 \rvert = 6$.

</details>

8\. This one reviews [place value and rounding](../../01-elementary/01-place-value-and-rounding.md). (a) Round $-3.7$ and $-3.2$ to the nearest integer, using distance on the number line. (b) The number $-3.5$ is exactly halfway between $-4$ and $-3$. Which integer do you get if you round halves up, toward the bigger number? Which if you round halves away from 0? (c) The rounding lesson says that truncating a whole number never makes it bigger. Truncate $-3.7$ to the ones place. Is the result bigger or smaller than $-3.7$?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The number $-3.7$ lies between $-4$ and $-3$. Its distance from $-4$ is $4 - 3.7 = 0.3$, and its distance from $-3$ is $3.7 - 3 = 0.7$, so it rounds to $-4$. The number $-3.2$ is $0.8$ from $-4$ and $0.2$ from $-3$, so it rounds to $-3$.

(b) The bigger of the two integers is $-3$, the one further right, so rounding halves up gives $-3$. Rounding halves away from 0 gives $-4$, the one with the bigger absolute value. Python's `round` uses round half to even, and `round(-3.5)` gives `-4`, since 4 is even. At an exact half the conventions disagree, so a program has to say which one it uses.

(c) Truncating drops the digits after the ones place and gives $-3$. On the number line, $-3$ is to the right of $-3.7$, so truncating made the number bigger. For negative numbers, truncating moves toward 0, which is up. That is why Python's `int(-3.7)` gives `-3`, while `math.floor(-3.7)`, which always rounds down, gives `-4`.

Check: $-3.7$ is closer to $-4$ than to $-3$, as the number line shows, so rounding and truncating give different answers here, $-4$ and $-3$.

</details>

## Where this shows up

- The next lesson, [integer arithmetic and sign rules](02-integer-arithmetic-and-sign-rules.md), shows how to work out $a - b$ for every pair of integers, which turns $\lvert a - b \rvert$ into a calculation. [Inequalities](../03-expressions-equations-inequalities/05-inequalities.md) uses the order on the number line, and [the coordinate plane](../05-linear-relationships-and-functions/01-coordinate-plane.md) puts two number lines at right angles.
- Distance as $\lvert x - a \rvert$ is the language of [the epsilon-delta definition](../../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md) of a limit, where "$x$ is close to $a$" becomes $\lvert x - a \rvert < \delta$. In computing, signed integers are stored with [two's complement](../../06-cs-math/01-number-representation/03-binary-arithmetic-and-twos-complement.md), and 8 bits hold the integers from $-128$ to 127.
- In money and economics, an overdrawn account, a trade deficit and a fall in GDP are all negative numbers, and the size of a change, whichever way it goes, is an absolute value.
