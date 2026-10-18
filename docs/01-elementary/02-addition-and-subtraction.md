# Addition and subtraction

After this lesson you can add and subtract whole numbers in your head and on paper, including borrowing across zeros, and check each answer by adding back or by estimating.

Before this: [place value and rounding](01-place-value-and-rounding.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $47 + 38$ and $92 - 57$ in your head.
2. Work out $6{,}487 + 2{,}936$.
3. Work out $5{,}003 - 1{,}768$, and check your answer.

<details class="solution" markdown>
<summary>Answers</summary>

1. 85 and 35. One way: $47 + 40 - 2 = 85$, and $92 - 60 + 3 = 35$.
2. 9,423. Every column carries: $7 + 6 = 13$, then $1 + 8 + 3 = 12$, then $1 + 4 + 9 = 14$, then $1 + 6 + 2 = 9$.
3. 3,235. Borrowing across the two zeros turns the top number into 4 thousands, 9 hundreds, 9 tens and 13 ones. Check: $3{,}235 + 1{,}768 = 5{,}003$.

</details>

## The idea

You have \$47 in your wallet, as four \$10 bills and seven loonies, and a friend pays you back \$38, as three tens and eight loonies. Together that makes 7 tens and 15 loonies. Fifteen is more than one place can hold, so trade ten of the loonies for a \$10 bill: now you have 8 tens and 5 loonies, which is \$85. On paper, that trade is the carry.

Subtraction runs the trade backwards. Suppose you have \$52, as 5 tens and 2 loonies, and you owe \$18. You can't hand over 8 loonies when you hold 2, so break one \$10 bill into ten loonies. That leaves 4 tens and 12 loonies, still \$52 in all. Pay 8 loonies and 1 ten, and 3 tens and 4 loonies are left: \$34.

Both work one place at a time, ones with ones and tens with tens. A place that reaches 10 or more passes one to the place on its left. A place that runs short takes one from the place on its left and gets ten in return.

## Definitions

In $a + b = c$, the numbers $a$ and $b$ are the **addends** and $c$ is their **sum**. In $47 + 38 = 85$, the sum is 85.

For whole numbers $a$ and $b$ with $a \ge b$, the **difference** $a - b$ is the whole number $c$ such that $b + c = a$. Here $\ge$ means "is greater than or equal to". In plain words, $52 - 18$ is the number you add to 18 to get 52, which is 34. When $a$ is less than $b$, no whole number works: $3 - 7$ would have to be a number that gives 3 when added to 7. That number is $-4$, a negative number, the subject of negative numbers and absolute value<!-- link: ../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md -->.

Two operations are **inverse operations** when each one undoes the other. Subtraction is the inverse of addition: adding 18 and then subtracting 18 gets you back where you started, and so does subtracting first and then adding. That is why a subtraction can be checked by adding back.

A **fact family** is the set of addition and subtraction facts made from the same three numbers. From 5, 7 and 12 come four facts:

$$
5 + 7 = 12, \quad 7 + 5 = 12, \quad 12 - 7 = 5, \quad 12 - 5 = 7.
$$

Knowing one of the four gives you the other three, so learning the addition facts also teaches the subtraction facts. To find $12 - 7$, ask what you add to 7 to make 12.

**Carrying** is the step in column addition where a column adds up to 10 or more: you write the ones digit of the column's sum and add its tens digit, the carry, to the next column on the left. **Borrowing** is the step in column subtraction where the top digit is too small: you take 1 from the next place on the left and add 10 to the top digit. Both are also called **regrouping**, which is the better name, because nothing is borrowed or paid back. The number stays the same and only its split among the places changes:

$$
52 = 5 \text{ tens} + 2 \text{ ones} = 4 \text{ tens} + 12 \text{ ones}.
$$

Addition is commutative: the order of the addends doesn't change the sum, so $a + b = b + a$ for every pair of whole numbers, and $8 + 5$ and $5 + 8$ are both 13. Subtraction is not: $7 - 3 = 4$, but $3 - 7$ is not even a whole number. [Properties of operations](04-properties-of-operations.md) collects these rules.

## How to do it

### Adding and subtracting in your head

| Strategy | Example | Working |
|---|---|---|
| Make 10 | $8 + 5$ | Split 5 into $2 + 3$: $8 + 2 = 10$, and $10 + 3 = 13$ |
| Doubles | $7 + 7$ | 14, a fact to know by heart |
| Near doubles | $7 + 8$ | $7 + 7 + 1 = 15$ |
| Compensation | $47 + 38$ | Add 40 instead of 38, then take back 2: $87 - 2 = 85$ |
| Compensation | $92 - 57$ | Subtract 60 instead of 57, then give back 3: $32 + 3 = 35$ |
| Counting up | $403 - 288$ | $288 + 12 = 300$ and $300 + 103 = 403$, so the answer is $12 + 103 = 115$ |

Making 10 works because 10 is the easiest number to add to: once one addend is 10, the sum is place value, $10 + 3 = 13$. Doubles are easy to remember, and near doubles lean on them. Compensation trades the given number for a round one nearby and then fixes the difference. Counting up uses the fact family: $403 - 288$ is the amount that takes 288 up to 403, which is also how a cashier counts out change.

<div class="warning" markdown>

Watch out for the direction of the fix in compensation. In $92 - 57$, subtracting 60 takes away 3 too many, so you add 3 back: $92 - 60 + 3 = 35$. Subtracting the 3 as well gives $92 - 60 - 3 = 29$, which is wrong. Adding back shows it: $35 + 57 = 92$, but $29 + 57 = 86$.

</div>

### Column addition

1. Write the numbers one under the other, lined up at the ones place, so that each column holds one place.
2. Add the ones column. If the sum is 9 or less, write it under the column. If it is 10 or more, write its ones digit and carry its tens digit to the top of the tens column.
3. Move one column to the left. Add its digits and the carry, if there is one, and write and carry as in step 2.
4. Repeat step 3 until you have added the leftmost column. A carry out of that column becomes a new digit at the left of the answer.
5. Check against an estimate, or by subtracting one addend from the sum.

With two addends the carry is always 0 or 1, because a column sum is at most $9 + 9 + 1 = 19$. When you add a longer list, a column can carry 2 or more.

### Column subtraction

1. Write the larger number on top, and line the two numbers up at the ones place.
2. Start with the ones column. If the top digit is at least as large as the bottom digit, subtract and write the difference.
3. If the top digit is smaller, borrow: take 1 from the top digit in the next column on the left (cross it out and write one less above it) and add 10 to the top digit in this column. Then subtract.
4. If the next digit on the left is 0, it has nothing to lend. Go left to the first nonzero digit, take 1 from it, and turn each 0 you passed over into 9. The column you started in gets 10 added. Then subtract.
5. Move one column to the left and repeat steps 2 to 4, using the new top digits, until every column is done.
6. Check by adding back: the answer plus the bottom number should equal the top number.

## Worked examples

<div class="example" markdown>

### Example 1: adding with a carry in every column

Work out $6{,}487 + 2{,}936$.

Step 1: write 6,487 above 2,936 with the ones lined up. Before adding, estimate: $6{,}500 + 2{,}900 = 9{,}400$.

Step 2: the ones are $7 + 6 = 13$. Write 3 in the ones place of the answer and carry the 1, which stands for one ten, to the top of the tens column.

Step 3: the tens are $1 + 8 + 3 = 12$, that is, 12 tens. Write 2 in the tens place and carry 1 to the hundreds, since 10 tens make a hundred. Then the hundreds are $1 + 4 + 9 = 14$: write 4 and carry 1 to the thousands.

Step 4: the thousands are $1 + 6 + 2 = 9$. Nothing carries out of this column, so the addition is done. Here is the finished layout, with each carry in small type above the column it was added to:

$$
\begin{array}{ccccc}
 & {\scriptstyle 1} & {\scriptstyle 1} & {\scriptstyle 1} & \\
 & 6 & 4 & 8 & 7 \\
+ & 2 & 9 & 3 & 6 \\
\hline
 & 9 & 4 & 2 & 3
\end{array}
$$

Step 5: the answer, 9,423, is close to the estimate of 9,400. Subtracting gives a second check: $9{,}423 - 2{,}936 = 6{,}487$.

<div class="warning" markdown>

Watch out at step 3: a forgotten carry makes the next column too small by one. Leave out all three carries here and the sum comes out as 8,313, which the estimate of 9,400 shows is about 1,100 too low.

</div>

</div>

<div class="example" markdown>

### Example 2: borrowing in three columns

Work out $8{,}352 - 4{,}679$. Estimate first: $8{,}400 - 4{,}700 = 3{,}700$.

| Column | Top digit | Borrow (step 3) | Subtract |
|---|---|---|---|
| Ones | 2 | 2 is less than 9, so take 1 ten: the tens digit 5 becomes 4 | $12 - 9 = 3$ |
| Tens | 4 | 4 is less than 7, so take 1 hundred: 3 becomes 2 | $14 - 7 = 7$ |
| Hundreds | 2 | 2 is less than 6, so take 1 thousand: 8 becomes 7 | $12 - 6 = 6$ |
| Thousands | 7 | none needed | $7 - 4 = 3$ |

The tens column starts from 4, not 5, because it lent one ten to the ones; step 5 says to use the new top digits. In the layout, each crossed-out digit has its new value written above it:

$$
\begin{array}{ccccc}
 & {\scriptstyle 7} & {\scriptstyle 12} & {\scriptstyle 14} & {\scriptstyle 12} \\
 & \cancel{8} & \cancel{3} & \cancel{5} & \cancel{2} \\
- & 4 & 6 & 7 & 9 \\
\hline
 & 3 & 6 & 7 & 3
\end{array}
$$

Check by adding back: $3{,}673 + 4{,}679 = 8{,}352$. The answer is also close to the estimate of 3,700.

</div>

<div class="example" markdown>

### Example 3: borrowing across zeros

Work out $5{,}003 - 1{,}768$. Estimate first: $5{,}000 - 1{,}800 = 3{,}200$.

The ones column needs to borrow, because 3 is less than 8. But the tens digit is 0, and so is the hundreds digit, so step 4 applies: the first nonzero digit to the left is the 5 in the thousands. Think of the paper clip cartons in [place value and rounding](01-place-value-and-rounding.md). Open one thousand into 10 hundreds, one of those hundreds into 10 tens, and one of those tens into 10 ones. That leaves

$$
5{,}003 = 4 \text{ thousands} + 9 \text{ hundreds} + 9 \text{ tens} + 13 \text{ ones}.
$$

So the 5 becomes 4, each 0 becomes 9, and the 3 becomes 13. Now no column needs to borrow:

$$
\begin{array}{ccccc}
 & {\scriptstyle 4} & {\scriptstyle 9} & {\scriptstyle 9} & {\scriptstyle 13} \\
 & \cancel{5} & \cancel{0} & \cancel{0} & \cancel{3} \\
- & 1 & 7 & 6 & 8 \\
\hline
 & 3 & 2 & 3 & 5
\end{array}
$$

Column by column, $13 - 8 = 5$, $9 - 6 = 3$, $9 - 7 = 2$ and $4 - 1 = 3$, so the answer is 3,235. Check: $3{,}235 + 1{,}768 = 5{,}003$, and 3,235 is close to the estimate of 3,200.

<div class="warning" markdown>

Watch out at step 4: each 0 you pass becomes 9, not 10, because it hands one of its ten on to the place on its right. Writing 10 in the tens and the hundreds gives $13 - 8 = 5$, $10 - 6 = 4$, $10 - 7 = 3$ and $4 - 1 = 3$, so 3,345. Adding back catches it: $3{,}345 + 1{,}768 = 5{,}113$, which is 110 too much.

</div>

</div>

## Edge cases and common mistakes

A forgotten carry (Example 1), zeros that should become 9s (Example 3) and a compensation fix in the wrong direction are flagged above. Here are the others.

<div class="warning" markdown>

Watch out: each column subtracts the bottom digit from the top digit. Taking the smaller digit from the larger in every column, whichever is on top, turns $5{,}003 - 1{,}768$ into $8 - 3 = 5$, $6 - 0 = 6$, $7 - 0 = 7$ and $5 - 1 = 4$, which gives 4,765. The estimate of 3,200 shows it is far too big. A column whose top digit is smaller has to borrow.

</div>

<div class="warning" markdown>

Watch out: line the numbers up at the ones place, not at the left. Written left-aligned, $4{,}250 + 37$ puts the 3 under the 2 and the 7 under the 5, and comes out as 4,620. Lined up at the right, it is 4,287.

</div>

<div class="warning" markdown>

Watch out for the last carry. In $857 + 286$ the hundreds column gives $1 + 8 + 2 = 11$, so the answer is 1,143, with one more digit than either addend. Dropping that carry gives 143.

</div>

The wording of a subtraction gives the order: "subtract 18 from 52" means $52 - 18$, so the number after "from" goes first. Zero is the easy case. Adding or subtracting 0 changes nothing, so $a + 0 = a$ and $a - 0 = a$, and every number minus itself is 0. But $0 - 5$ is not a whole number, for the same reason as $3 - 7$.

## Tricks and shortcuts

To subtract from 1,000 or 10,000, subtract each digit from 9 and the last digit from 10, as long as the last digit isn't 0. So $1{,}000 - 637 = 363$, from $9 - 6 = 3$, $9 - 3 = 6$ and $10 - 7 = 3$. This works because $1{,}000 - 637 = (999 - 637) + 1$, and subtracting from a row of 9s never borrows.

Adding the same number to both parts of a subtraction doesn't change the difference, so you can shift a subtraction to rounder numbers. Adding 32 to both parts gives

$$
5{,}003 - 1{,}768 = 5{,}035 - 1{,}800 = 3{,}235,
$$

with no borrowing at all. Picture two people standing some distance apart: if both take 32 steps in the same direction, the distance between them stays the same.

When adding a list, look for pairs that make a round number: $27 + 46 + 73 = (27 + 73) + 46 = 100 + 46 = 146$. Addition allows changing both the order and the grouping, as [properties of operations](04-properties-of-operations.md) explains, but subtraction allows neither.

## FAQ

### Can you add from left to right?

Yes, and in your head it is often easier. For $47 + 38$, add the tens ($40 + 30 = 70$), then the ones ($7 + 8 = 15$), then combine them to get 85. On paper, right to left is less work, because each carry is ready before you write the next column. Going left to right, a carry from a later column means going back to change a digit you already wrote.

### Why check by adding back instead of subtracting again?

Repeating the same subtraction tends to repeat the same mistake, since you see the same digits in the same places. Adding back is a different calculation with different carries, so a slip in one is unlikely to be matched by the same slip in the other. An estimate is a third check, cruder but faster, and it catches the big errors, such as a missing borrow.

## Practice

### Warm-up

1\. Work these out in your head, and say which strategy you used: (a) $8 + 7$, (b) $26 + 59$, (c) $83 - 48$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Make 10: split 7 into $2 + 5$, so $8 + 2 = 10$ and $10 + 5 = 15$. Near doubles works too: $7 + 7 + 1 = 15$.
- (b) Compensation: $26 + 60 = 86$, then take back the extra 1 to get 85.
- (c) Compensation: $83 - 50 = 33$, then give back the extra 2 to get 35. Counting up also works: $48 + 2 = 50$ and $50 + 33 = 83$, so the answer is $2 + 33 = 35$.

Check by the fact families: $15 - 7 = 8$, $85 - 59 = 26$ and $35 + 48 = 83$.

</details>

2\. Work out $3{,}768 + 4{,}595$ in columns.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate: $3{,}800 + 4{,}600 = 8{,}400$. The ones give $8 + 5 = 13$, so write 3 and carry 1. The tens give $1 + 6 + 9 = 16$, so write 6 and carry 1. The hundreds give $1 + 7 + 5 = 13$, so write 3 and carry 1. The thousands give $1 + 3 + 4 = 8$.

The sum is 8,363. Check: it is close to the estimate of 8,400, and $8{,}363 - 4{,}595 = 3{,}768$.

</details>

### Standard

3\. Work out $7{,}002 - 2{,}846$, and check by adding back.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate: $7{,}000 - 2{,}800 = 4{,}200$. The ones need to borrow, since 2 is less than 6, and the tens and hundreds digits are 0. So borrow from the 7 (step 4): $7{,}002$ is 6 thousands, 9 hundreds, 9 tens and 12 ones. Then $12 - 6 = 6$, $9 - 4 = 5$, $9 - 8 = 1$ and $6 - 2 = 4$.

The answer is 4,156. Check: $4{,}156 + 2{,}846 = 7{,}002$, and 4,156 is close to the estimate of 4,200.

</details>

4\. A classmate writes $6{,}030 - 2{,}457 = 4{,}427$. Find the mistake and the right answer.

<details class="solution" markdown>
<summary>Solution</summary>

The classmate took the smaller digit from the larger in every column: $7 - 0$, $5 - 3$, $4 - 0$ and $6 - 2$. The estimate $6{,}000 - 2{,}500 = 3{,}500$ already says 4,427 is too big, and adding back gives $4{,}427 + 2{,}457 = 6{,}884$, not 6,030.

Do it properly. Ones: 0 is less than 7, so borrow from the tens, where 3 becomes 2, and work out $10 - 7 = 3$. Tens: 2 is less than 5, and the hundreds digit is 0, so borrow from the thousands (step 4): 6 becomes 5, the hundreds 0 becomes 9 and the tens become 12, so $12 - 5 = 7$. Hundreds: $9 - 4 = 5$. Thousands: $5 - 2 = 3$.

The right answer is 3,573. Check: $3{,}573 + 2{,}457 = 6{,}030$.

</details>

### Challenge

5\. Each box stands for one missing digit, and different boxes can hold different digits. Find them all.

$$
\begin{array}{ccccc}
 & 4 & \square & 7 & 6 \\
+ & \square & 8 & \square & 9 \\
\hline
 & 7 & 2 & 0 & 5
\end{array}
$$

<details class="solution" markdown>
<summary>Solution</summary>

Work from the right, the way the addition itself goes.

- Ones: $6 + 9 = 15$, so the 5 is written and 1 carries, which matches the answer.
- Tens: $1 + 7 + \square$ must end in 0. The smallest such sum is 10, which needs a 2 in the box, and the next, 20, would need a 12, which is not a digit. So the box is 2, and 1 carries.
- Hundreds: $1 + \square + 8$ must end in 2. It is at least 9, so it must be 12, and the box is 3, with a carry of 1.
- Thousands: $1 + 4 + \square = 7$, so the box is 2.

The sum is $4{,}376 + 2{,}829 = 7{,}205$. Check by subtracting: $7{,}205 - 2{,}829 = 4{,}376$.

</details>

6\. This one reviews [place value and rounding](01-place-value-and-rounding.md). (a) Round 4,451 and 2,549 to the nearest hundred, then subtract. (b) Subtract the exact numbers, then round the answer to the nearest hundred. (c) Why do the answers differ, and which one should you report?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The numbers round to 4,500 and 2,500, and $4{,}500 - 2{,}500 = 2{,}000$.

(b) In columns, the ones borrow ($11 - 9 = 2$), the tens give $4 - 4 = 0$, the hundreds borrow ($14 - 5 = 9$) and the thousands give $3 - 2 = 1$. So $4{,}451 - 2{,}549 = 1{,}902$, which rounds to 1,900.

(c) Rounding moved 4,451 up by 49 and 2,549 down by 49, so the rounded numbers are $49 + 49 = 98$ further apart than the real ones: $2{,}000 - 1{,}902 = 98$. Rounding first is fine for an estimate. For an answer you report, subtract the exact numbers and round once at the end, which gives 1,900.

Check: $1{,}902 + 2{,}549 = 4{,}451$.

</details>

## Where this shows up

- [Multiplication and times tables](03-multiplication-and-times-tables.md) starts from repeated addition, and carrying comes back in [multi-digit multiplication](05-multi-digit-multiplication.md). The subtract step of [long division](07-long-division.md) is the column subtraction from this lesson.
- Binary addition carries when a column reaches 2 instead of 10, and computers subtract by adding (binary arithmetic and two's complement<!-- link: ../06-cs-math/01-number-representation/03-binary-arithmetic-and-twos-complement.md -->).
- A bank balance is a running sum of deposits minus withdrawals, and checking a statement against your own records is the add-back check on a larger scale.
