# Long division

After this lesson you can divide a whole number by a one- or two-digit number on paper, write the answer as a quotient and remainder, a fraction or a decimal, and check it.

Before this: [division facts and remainders](06-division-facts-and-remainders.md) and [multi-digit multiplication](05-multi-digit-multiplication.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $4{,}236 \div 4$.
2. Find the quotient and remainder when 1,000 is divided by 17.
3. Write $13 \div 8$ as a decimal.

<details class="solution" markdown>
<summary>Answers</summary>

1. 1,059. Four doesn't go into the 2, so the second digit of the quotient is 0. Check: $1{,}059 \times 4 = 4{,}236$.
2. Quotient 58, remainder 14, because $1{,}000 = 58 \times 17 + 14$ and 14 is less than 17.
3. 1.625. Eight goes into 13 once with 5 left over. Then $50 \div 8 = 6$ remainder 2, $20 \div 8 = 2$ remainder 4, and $40 \div 8 = 5$ remainder 0.

</details>

## The idea

Six people share \$618, paid out as six \$100 bills, one \$10 bill and eight loonies. You hand out the biggest bills first.

Each person gets one \$100 bill, and the hundreds are used up. The single \$10 bill can't go to six people, so nobody gets a ten; you change it for ten loonies instead. That makes 18 loonies, 3 for each person.

| Place | To share | Each person gets | Left over |
|---|---|---|---|
| Hundreds | 6 | 1 | 0 |
| Tens | 1 | 0 | 1, changed into 10 ones |
| Ones | 10 + 8 = 18 | 3 | 0 |

Read down the "each person gets" column and you have the answer: \$103 each.

Long division is this process written down. It works through the number being divided one place at a time, from the biggest place to the smallest, and shares out what it can at each place. Whatever is left over moves to the next place down, where each leftover unit is worth ten of the smaller units. On paper, that move is the "bring down" step.

The 0 in 103 records the tens place, where there was nothing to share. Leave it out and each person gets \$13, with \$540 still on the table.

## Definitions

In a division $n \div d$, the **dividend** $n$ is the number being divided, and the **divisor** $d$ is the number you divide by. In $618 \div 6$ the dividend is 618 and the divisor is 6. The same division can be written $618 / 6$ or $\frac{618}{6}$.

The answer has two parts, and they come from a theorem called the **division algorithm**.

*Theorem.* Let $n$ and $d$ be integers with $d > 0$. Then there exist unique integers $q$ and $r$ such that

$$
n = qd + r \quad \text{and} \quad 0 \le r < d.
$$

The integer $q$ is the **quotient** and $r$ is the **remainder** when $n$ is divided by $d$. Here $qd$ means $q \times d$, and $0 \le r < d$ says that $r$ is at least 0 and less than $d$.

In plain words, the divisor fits into the dividend $q$ whole times, and the remainder is what is left over, which is too small to hold another divisor. For $47 \div 5$ the quotient is 9 and the remainder is 2, because $47 = 9 \times 5 + 2$. In the long division layout, each part has its own place:

$$
\begin{array}{rl}
9 & \leftarrow \text{quotient} \\
5\,\overline{\smash{\big)}\,47} & \leftarrow \text{divisor } 5 \text{, dividend } 47 \\
\underline{-\,45} & \leftarrow 9 \times 5 \\
2 & \leftarrow \text{remainder}
\end{array}
$$

Here is why the theorem holds when $n$ is a whole number. We want a pair $q$ and $r$ that fits, and no second pair; the plan is to walk up the multiples of $d$.

*Proof.* List the multiples $0, d, 2d, 3d, \dots$ and stop at the largest one that is not bigger than $n$. Call it $qd$ and set $r = n - qd$, so $n = qd + r$ and $r \ge 0$. The next multiple, $qd + d$, is bigger than $n$, so $d > n - qd = r$. No other $q$ works: a smaller one leaves a remainder of at least $r + d$, which is too big, and a bigger one makes $qd$ bigger than $n$, which leaves a negative remainder.

Look back: the condition $0 \le r < d$ is what makes the pair unique. Without it, $47 = 8 \times 5 + 7$ would count too, even though a leftover of 7 still holds another 5. The proof for negative $n$ is in divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

Despite its name, the division algorithm is a theorem: it says that $q$ and $r$ exist and are unique, but not how to find them. **Long division** is a pencil-and-paper method that finds them, one digit of the quotient at a time. In this lesson $n$ is never negative, so $q$ and $r$ are whole numbers too.

## How to do it

Write the divisor to the left of the bracket and the dividend under it. If the dividend has a thousands comma, leave it out, so each digit has its own column. Each pass divides one working number: at the start it is the first digit or first few digits of the dividend, and after that it is the last difference with the next digit attached.

1. Estimate. Round the numbers to get a rough answer, so you know about how big the quotient should be.
2. Divide. Find how many times the divisor goes into the working number, and write that digit in the quotient, above the last digit of the working number. For the first working number, use the fewest leading digits of the dividend that make a number at least as big as the divisor.
3. Multiply the new quotient digit by the divisor and write the product under the working number. If the product is bigger than the working number, the digit is too big: lower it by 1.
4. Subtract the product from the working number.
5. Compare the difference with the divisor. The difference must be smaller. If it is not, the digit is too small: raise it by 1 and redo steps 3 and 4.
6. Bring down the next digit of the dividend and write it to the right of the difference. That is the new working number; go back to step 2. Every digit you bring down adds a digit to the quotient, even when that digit is 0.
7. Finish and check. When there are no digits left to bring down, the last difference is the remainder. Check that $qd + r = n$ (quotient times divisor, plus remainder, gives the dividend) and that the answer is close to your estimate.

Steps 2 to 6 are a loop that runs once for each digit of the quotient: Divide, Multiply, Subtract, Compare, Bring down. To keep the order straight, remember "Dad, Mom, Sister, Cousin, Brother", whose first letters are D, M, S, C, B.

## Worked examples

<div class="example" markdown>

### Example 1: dividing 745 by 3

Step 1: round 745 to 750. Since $750 \div 3 = 250$, the answer should be a little under 250.

First pass. Step 2: the first digit, 7, is at least 3, so 7 is the first working number. Three goes into 7 twice ($3 \times 3 = 9$ is too much), so write 2 above the 7. Step 3: $2 \times 3 = 6$, so write 6 under the 7. Step 4: $7 - 6 = 1$.

Step 5: the difference 1 is less than 3, so the digit 2 is right. Step 6: bring down the 4 next to the 1, which makes the new working number 14.

Second pass. Three goes into 14 four times ($4 \times 3 = 12$, and $5 \times 3 = 15$ is too much). Write 4 above the 4, subtract $14 - 12 = 2$, see that 2 is less than 3, and bring down the 5 to make 25.

Third pass. Three goes into 25 eight times, since $8 \times 3 = 24$. Write 8 above the 5 and subtract: $25 - 24 = 1$. There is nothing left to bring down, so the remainder is 1. Here is the finished layout, with each line labelled:

$$
\begin{array}{rl}
248 & \\
3\,\overline{\smash{\big)}\,745} & \\
\underline{-\,6}\phantom{00} & \leftarrow 2 \times 3 \\
14\phantom{0} & \leftarrow 7 - 6 = 1 \text{, bring down } 4 \\
\underline{-\,12}\phantom{0} & \leftarrow 4 \times 3 \\
25 & \leftarrow 14 - 12 = 2 \text{, bring down } 5 \\
\underline{-\,24} & \leftarrow 8 \times 3 \\
1 & \leftarrow 25 - 24 = 1 \text{, remainder}
\end{array}
$$

Step 7: check by multiplying back. Since $248 \times 3 = 744$ and $744 + 1 = 745$, the answer is right, and 248 is close to the estimate of 250. In the form of the division algorithm, $745 = 248 \times 3 + 1$.

The remainder can also go into the answer as a fraction. The 1 left over still has to be split 3 ways, which makes $\frac{1}{3}$, so $745 \div 3 = 248\frac{1}{3}$ (a mixed number: 248 and one third).

<div class="warning" markdown>

Watch out: 248 remainder 1 is not 248.1. The remainder stands for $\frac{1}{3}$ of a whole, and continuing into decimals (Example 4) gives $248.333\ldots$, with 3s forever. Multiplying back catches the slip: $248.1 \times 3 = 744.3$, not 745.

</div>

</div>

<div class="example" markdown>

### Example 2: a zero in the quotient

Divide 618 by 6, the sharing problem from the start of the lesson. Step 1: $600 \div 6 = 100$, so expect about 100.

Six goes into 6 once, and $6 - 6 = 0$. Bring down the 1. The working number is now 1, which is smaller than 6, so six goes into it 0 times: write 0 in the quotient, above the 1.

<div class="warning" markdown>

Watch out: this is where the zero goes missing. Seeing that 6 doesn't fit, people bring down the 8 straight away and never write the 0, which turns 103 into 13. Every digit you bring down needs a quotient digit above it.

</div>

Finish the pass instead: $0 \times 6 = 0$ and $1 - 0 = 1$. Then bring down the 8 to make 18, and six goes into 18 exactly 3 times.

$$
\begin{array}{rl}
103 & \\
6\,\overline{\smash{\big)}\,618} & \\
\underline{-\,6}\phantom{00} & \leftarrow 1 \times 6 \\
01\phantom{0} & \leftarrow 6 - 6 = 0 \text{, bring down } 1 \\
\underline{-\,0}\phantom{0} & \leftarrow 0 \times 6 \text{, since } 6 > 1 \\
18 & \leftarrow 1 - 0 = 1 \text{, bring down } 8 \\
\underline{-\,18} & \leftarrow 3 \times 6 \\
0 & \leftarrow \text{remainder}
\end{array}
$$

Check: $103 \times 6 = 618$, with remainder 0. The estimate of 100 also rules out 13, the answer you get by skipping the zero.

</div>

<div class="example" markdown>

### Example 3: a two-digit divisor

Divide 4,567 by 23. Step 1: $200 \times 23 = 4{,}600$, which is just above 4,567, so the quotient is a little under 200.

Step 2 is harder now, because you probably don't know the multiples of 23 by heart. Round the divisor to the nearest ten, so 23 becomes 20, and guess each digit by dividing the leading digits of the working number by 2. The guess is often off by 1, and steps 3 and 5 tell you which way to fix it.

Since 23 doesn't go into 4, the first working number is 45, and the first quotient digit goes above the 5.

| Working number | Guess (think of 23 as 20) | Multiply | Result |
|---|---|---|---|
| 45 | $4 \div 2 = 2$ | $2 \times 23 = 46$ | 46 is more than 45, so use 1: $45 - 23 = 22$ |
| 226 | $22 \div 2 = 11$, but a digit is at most 9 | $9 \times 23 = 207$ | $226 - 207 = 19$, less than 23 |
| 197 | $19 \div 2$ gives 9 | $9 \times 23 = 207$ | 207 is more than 197, so use 8: $197 - 184 = 13$ |

$$
\begin{array}{r}
198 \\
23\,\overline{\smash{\big)}\,4567} \\
\underline{-\,23}\phantom{00} \\
226\phantom{0} \\
\underline{-\,207}\phantom{0} \\
197 \\
\underline{-\,184} \\
13
\end{array}
$$

The quotient is 198 and the remainder is 13. Check: $198 \times 23 = 4{,}554$ and $4{,}554 + 13 = 4{,}567$.

Rounding 23 down to 20 made two of the three guesses too big, because 20 fits more times than 23 does. Rounding up, say 37 to 40, makes guesses too small instead, and step 5 catches those (Practice problem 3 has one).

</div>

<div class="example" markdown>

### Example 4: continuing into decimals

Divide 7 by 8. The divisor is bigger than the dividend, so in whole numbers the answer is 0 remainder 7, since $7 = 0 \times 8 + 7$. To go further, write 7 as 7.000 (zeros after the decimal point don't change a number) and put a decimal point in the quotient directly above the one in the dividend. Then run the same loop, bringing down the zeros.

Eight doesn't go into 7, so write 0 before the point. Bringing down the first 0 makes 70, and eight goes into 70 eight times:

$$
\begin{array}{rl}
0.875 & \\
8\,\overline{\smash{\big)}\,7.000} & \\
\underline{-\,6\phantom{.}4}\phantom{00} & \leftarrow 8 \times 8 = 64 \\
60\phantom{0} & \leftarrow 70 - 64 = 6 \text{, bring down } 0 \\
\underline{-\,56}\phantom{0} & \leftarrow 7 \times 8 \\
40 & \leftarrow 60 - 56 = 4 \text{, bring down } 0 \\
\underline{-\,40} & \leftarrow 5 \times 8 \\
0 & \leftarrow \text{remainder } 0 \text{, so stop}
\end{array}
$$

In the first subtraction the 6 sits under the 7 and the 4 under the first 0, with the decimal point between them. The difference reaches 0 after three decimal places, so $7 \div 8 = 0.875$. Check: $0.875 \times 8 = 7$.

</div>

## Edge cases and common mistakes

Two mistakes are flagged above, at the step where they happen: a missing zero in the quotient (Example 2) and a remainder written after a decimal point (Example 1). Here are the other cases.

<div class="warning" markdown>

Watch out: a difference as big as the divisor means the quotient digit is too small. In $745 \div 3$, guessing 1 for the first digit gives $7 - 3 = 4$, and 4 is not less than 3, so another 3 still fits. Raise the digit to 2. A remainder of 4 when you divide by 3 is never right.

</div>

When the divisor is bigger than the first digit, start with the first two digits. In $256 \div 4$, four doesn't go into 2, so the first working number is 25 and the first quotient digit goes above the 5; the answer is 64. Writing a 0 above the 2 does no harm, because a zero at the left end of a number changes nothing (064 is 64). A zero missing from the middle is the real danger.

When the dividend is smaller than the divisor, the quotient is 0 and the remainder is the whole dividend: $5 \div 8$ is 0 remainder 5, because $5 = 0 \times 8 + 5$. Zero divided by a nonzero number is 0 with remainder 0, as in $0 = 0 \times 7 + 0$.

Dividing by zero is undefined. The answer to $5 \div 0$ would be a number $q$ with $q \times 0 = 5$, and there is none, because every number times 0 is 0. The division algorithm leaves out $d = 0$ for the same reason: no $r$ satisfies $0 \le r < 0$.

When you continue into decimals, the difference doesn't always reach 0. If a difference repeats, the digits after it repeat forever. In $1 \div 3$ every pass leaves 1, brings down a 0 and gives $10 \div 3 = 3$ remainder 1 again, so $1 \div 3 = 0.333\ldots$, written $0.\overline{3}$ (the bar means the digit under it repeats forever). Stop when the difference is 0 or starts to repeat, or when you have enough decimal places to round.

## Tricks and shortcuts

Count the quotient's digits before you start. The quotient gets one digit from the first working number and one more for each digit you bring down. In $4{,}567 \div 23$ the first working number is 45 and two digits (6 and 7) are brought down, so the quotient has 3 digits. If your answer has fewer, a zero went missing.

For a two-digit divisor, you can list its multiples first by adding it to itself again and again. For 23 they are 23, 46, 69, 92, 115, 138, 161, 184 and 207. Then each quotient digit is a lookup, the largest multiple that is not bigger than the working number: 207 (which is $9 \times 23$) for 226, and 184 (which is $8 \times 23$) for 197. The list pays off when you divide by the same number several times.

The method of **partial quotients** is a variation of long division in which you subtract any convenient multiple of the divisor, such as 100 or 50 times it, and add up the multipliers at the end. The guesses don't need to be exact, since a guess that is too small costs an extra line instead of a redo. Here is $4{,}567 \div 23$ again, with multiples that are easy to work out:

| Take away | What is left |
|---|---|
| $100 \times 23 = 2{,}300$ | $4{,}567 - 2{,}300 = 2{,}267$ |
| $50 \times 23 = 1{,}150$ | $2{,}267 - 1{,}150 = 1{,}117$ |
| $40 \times 23 = 920$ | $1{,}117 - 920 = 197$ |
| $8 \times 23 = 184$ | $197 - 184 = 13$ |

The multipliers add up to $100 + 50 + 40 + 8 = 198$, and 13 is left: the same quotient and remainder as Example 3.

## FAQ

### Why does long division start at the left?

Addition, subtraction and multiplication start at the right because their carries and borrows change the digit to the left, so each place has to be settled before the one to its left. In division the leftovers move the other way, to the right: a leftover hundred becomes ten tens, as the \$10 bill became ten loonies in [The idea](#the-idea). So division starts with the biggest place.

### Should the answer be a remainder, a fraction or a decimal?

It depends on the question. If 745 students form teams of 3, there are 248 full teams and 1 student left over, so the remainder is the useful answer. If \$745 is split three ways, each share is \$248.33, a decimal rounded to the cent. When the answer has to be exact, give the fraction: $745 \div 3 = 248\frac{1}{3}$.

## Practice

### Warm-up

1\. Work out $2{,}416 \div 8$.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate: $2{,}400 \div 8 = 300$. Eight doesn't go into 2, so the first working number is 24, which gives 3 with nothing left. Bring down the 1. Eight doesn't go into 1, so the next quotient digit is 0, and 1 is left. Bring down the 6 to make 16, which gives 2 with nothing left.

The answer is 302. Check: $302 \times 8 = 2{,}416$, close to the estimate of 300.

</details>

2\. Work out $758 \div 4$. Write the answer in the form $n = qd + r$ and as a mixed number.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate: $800 \div 4 = 200$, so the answer is a bit under 200. Four goes into 7 once, with $7 - 4 = 3$ left. Bring down the 5 to make 35: $8 \times 4 = 32$, and $35 - 32 = 3$. Bring down the 8 to make 38: $9 \times 4 = 36$, and $38 - 36 = 2$.

The quotient is 189 and the remainder is 2, so $758 = 189 \times 4 + 2$. As a mixed number the answer is $189\frac{2}{4}$, which simplifies to $189\frac{1}{2}$ ([fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md) covers simplifying).

Check: $189 \times 4 = 756$ and $756 + 2 = 758$.

</details>

### Standard

3\. Work out $9{,}235 \div 37$. Round 37 to 40 to guess each digit, and watch for a guess that is too small.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate: $9{,}200 \div 40 = 230$. The divisor 37 is a bit less than 40, so expect a bit more than 230. Thirty-seven doesn't go into 9, so the first working number is 92.

| Working number | Guess (think of 37 as 40) | Multiply | Subtract |
|---|---|---|---|
| 92 | $9 \div 4$ gives 2 | $2 \times 37 = 74$ | $92 - 74 = 18$ |
| 183 | $18 \div 4$ gives 4 | $4 \times 37 = 148$ | $183 - 148 = 35$ |
| 355 | $35 \div 4$ gives 8 | $8 \times 37 = 296$ | $355 - 296 = 59$, too big |
| 355 | raise the digit to 9 | $9 \times 37 = 333$ | $355 - 333 = 22$ |

In the third row, 59 is bigger than 37, so step 5 says the digit 8 is too small, and 9 works. The quotient is 249 and the remainder is 22. Check: $249 \times 37 = 9{,}213$ and $9{,}213 + 22 = 9{,}235$.

</details>

4\. A classmate writes $425 \div 6 = 69$ remainder 11. What is wrong, and what is the right answer?

<details class="solution" markdown>
<summary>Solution</summary>

The remainder 11 is bigger than the divisor 6, so another 6 still fits. The equation $69 \times 6 + 11 = 425$ is true, but it breaks the condition $0 \le r < d$, so 69 and 11 are not the quotient and remainder.

Redo the division. Six doesn't go into 4, so start with 42: six goes into 42 exactly 7 times, with 0 left. Bring down the 5. Six doesn't go into 5, so the last quotient digit is 0 and the remainder is 5. The answer is 70 remainder 5. You can also repair the classmate's answer directly: $11 = 6 + 5$, so one more 6 moves into the quotient, which gives 70 remainder 5.

Check: $70 \times 6 + 5 = 425$, and 5 is less than 6.

</details>

### Challenge

5\. A timer counts 10,000 seconds. Write this time in hours, minutes and seconds, using two long divisions. (A minute is 60 seconds and an hour is 60 minutes.)

<details class="solution" markdown>
<summary>Solution</summary>

First change seconds to minutes by dividing 10,000 by 60. Sixty doesn't go into 1 or 10, so the first working number is 100, which gives 1 with 40 left. Each of the last two 0s, brought down, makes 400, which gives 6 with 40 left ($6 \times 60 = 360$). So $10{,}000 = 166 \times 60 + 40$: 166 minutes and 40 seconds.

Then change minutes to hours. Sixty goes into 166 twice, with $166 - 120 = 46$ left, so the time is 2 hours, 46 minutes and 40 seconds.

Check: $2 \times 3{,}600 + 46 \times 60 + 40 = 7{,}200 + 2{,}760 + 40 = 10{,}000$. In Python, `divmod(10000, 60)` returns `(166, 40)`, the quotient and remainder of the first division.

</details>

6\. This one reviews rounding from [place value and rounding](01-place-value-and-rounding.md). Write $7 \div 12$ as a decimal, explain why the digits never stop, and round the answer to the nearest hundredth.

<details class="solution" markdown>
<summary>Solution</summary>

Twelve doesn't go into 7, so the quotient starts with 0 and a decimal point, and you bring down zeros. Twelve goes into 70 five times, since $5 \times 12 = 60$, leaving 10. Bring down a 0 to make 100: $8 \times 12 = 96$, leaving 4. Bring down a 0 to make 40: $3 \times 12 = 36$, leaving 4 again.

The difference 4 has come up twice in a row, so every pass from here is the same: bring down a 0, get 40, write 3, leave 4. The 3s never stop, and $7 \div 12 = 0.58333\ldots = 0.58\overline{3}$.

To round to the nearest hundredth, look at the thousandths digit. It is 3, which is less than 5, so round down: $7 \div 12 \approx 0.58$, where $\approx$ means "is about".

Check: $0.58 \times 12 = 6.96$, just under 7, as it should be after rounding down.

</details>

## Where this shows up

- In high school, polynomial long division runs the same loop (divide, multiply, subtract, bring down) with powers of $x$ in place of tens and hundreds: [polynomial division and the remainder theorem](../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md).
- Modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md --> keeps only the remainder. In code, `n // d` is the quotient, `n % d` is the remainder, and Python's `divmod(n, d)` returns both.
- Writing a number in binary is repeated division by 2, keeping the remainders: see [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).
