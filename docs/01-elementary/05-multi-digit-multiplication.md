# Multi-digit multiplication

After this lesson you can multiply a two- or three-digit number by a two-digit number on paper, with the area model or the column method, explain the zero that starts each shifted row, and check the answer.

Before this: [multiplication and times tables](03-multiplication-and-times-tables.md) and [properties of operations](04-properties-of-operations.md), especially the distributive property.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $63 \times 28$.
2. Work out $405 \times 37$.
3. A classmate works out $56 \times 34$ and gets 392. Show that this can't be right without redoing the multiplication, then find the mistake.

<details class="solution" markdown>
<summary>Answers</summary>

1. 1,764. The rows are $63 \times 8 = 504$ and $63 \times 20 = 1{,}260$, and $504 + 1{,}260 = 1{,}764$.
2. 14,985. The rows are $405 \times 7 = 2{,}835$ and $405 \times 30 = 12{,}150$, and they add to 14,985.
3. An estimate is $60 \times 30 = 1{,}800$, so 392 is far too small. The rows should be $56 \times 4 = 224$ and $56 \times 30 = 1{,}680$, but the classmate wrote 168 for the second row, leaving out the 0, and $224 + 168 = 392$. The right answer is $224 + 1{,}680 = 1{,}904$.

</details>

## The idea

A concert hall has 36 rows with 47 seats in each row, so it has $47 \times 36$ seats. The times tables give you $4 \times 3$ and $7 \times 6$, but not $47 \times 36$. So split each number by place value, $47 = 40 + 7$ and $36 = 30 + 6$, and multiply the pieces.

Picture the seats as a rectangle 47 seats wide and 36 rows deep. Cut it along the place-value split and you get four smaller rectangles, each easy to count:

| $\times$ | $40$ | $7$ |
|---|---|---|
| $30$ | $1{,}200$ | $210$ |
| $6$ | $240$ | $42$ |

Each box holds its column heading times its row heading. For example, $40 \times 30 = 1{,}200$ comes from the one-digit fact $4 \times 3 = 12$ with two zeros attached, one from the 40 and one from the 30. Adding the four boxes counts every seat once:

$$
1{,}200 + 210 + 240 + 42 = 1{,}692.
$$

So the hall has 1,692 seats. The pencil-and-paper methods taught in school all work this way: they break the problem into one-digit facts with zeros attached, then add. The column method, the usual school method, is a compact way of writing these four boxes.

## Definitions

When the factors of a product are split into place-value parts, the product of a part of one factor with a part of the other, or with the whole other factor, is a **partial product**. The product is the sum of the partial products.

In plain words, a partial product is one piece of the answer. In $47 \times 36$ the four boxes above are partial products, and so are $47 \times 30 = 1{,}410$ and $47 \times 6 = 282$. The distributive property from [properties of operations](04-properties-of-operations.md), used in both its left and right versions, is why the pieces add up to the whole:

$$
\begin{aligned}
47 \times 36 &= 47 \times (30 + 6) = 47 \times 30 + 47 \times 6 \\
&= (40 + 7) \times 30 + (40 + 7) \times 6 \\
&= 40 \times 30 + 7 \times 30 + 40 \times 6 + 7 \times 6.
\end{aligned}
$$

The **area model**, also called the box method, draws the two factors as the sides of a rectangle and splits each side by place value. Each small rectangle is a partial product, and the whole area is the product.

The **column method**, also called long multiplication or the standard algorithm, writes one factor above the other, works out one row for each digit of the bottom factor, and adds the rows. Each row is a partial product: the top number times one digit of the bottom number, shifted to that digit's place.

## How to do it

### The area model

Split each factor into its place-value parts, and draw a grid with a column for each part of one factor and a row for each part of the other. Fill each box by multiplying the nonzero digits and then attaching all the zeros of both parts. That works because $40 \times 30 = (4 \times 10) \times (3 \times 10) = (4 \times 3) \times (10 \times 10) = 12 \times 100$, by the commutative and associative properties. Then add the boxes.

A three-digit factor gives three parts, as in $769 = 700 + 60 + 9$, and a zero digit gives no part, so 308 splits as $300 + 8$.

### The column method

1. Estimate. Round each factor to a number with one nonzero digit, such as 47 to 50 and 36 to 40, and multiply. The answer should be near this estimate.
2. Write the factor with more digits on top and the other below it, with the ones digits in the same column.
3. Multiply the top number by the ones digit of the bottom number, working from right to left. At each digit, write the ones digit of the small product and carry its tens digit to the next column, as in addition. Add a carry after the next multiplication, not before. This row is the first partial product.
4. Cross out the carries. Start the second row with a 0 in the ones column, because the next digit of the bottom number stands for tens.
5. Multiply the top number by the tens digit of the bottom number, right to left, carrying as in step 3, and write the result to the left of the 0. This row is the second partial product.
6. Add the two rows.
7. Check. The answer should be close to the estimate. For a second check, multiply in the other order, or cast out nines (see [Tricks and shortcuts](#tricks-and-shortcuts)).

A three-digit bottom factor needs a third row, which starts with two zeros because its digit stands for hundreds.

### Why the second row starts with a zero

In $47 \times 36$, the 3 in 36 stands for 30, so the second row is $47 \times 30$, not $47 \times 3$:

$$
47 \times 30 = 47 \times (3 \times 10) = (47 \times 3) \times 10 = 141 \times 10 = 1{,}410.
$$

The middle step is the associative property. Multiplying by 10 moves every digit one place to the left and puts a 0 in the ones place ([powers of ten](14-powers-of-ten.md)), and the 0 that starts the second row is that move. Some people were taught to leave the ones place blank instead of writing the 0. That works too, as long as the digits still shift one place left. Leaving out the shift altogether turns 1,410 into 141, which is the mistake in Quick check 3.

## Worked examples

<div class="example" markdown>

### Example 1: 47 times 36 with the column method

Step 1: estimate. Rounding gives $50 \times 40 = 2{,}000$. Both factors were rounded up, so the answer should be a little under 2,000.

Step 2: write 47 on top and 36 below it, with the 7 above the 6.

Step 3: multiply 47 by 6, starting at the right. First, $7 \times 6 = 42$: write the 2 in the ones column and carry the 4 to the tens column. Next, $4 \times 6 = 24$, and adding the carried 4 gives 28, so write 28. The first row is 282, which is $47 \times 6$.

<div class="warning" markdown>

Watch out: the carry is added after you multiply. Adding it first gives $(4 + 4) \times 6 = 48$ and a row of 482, which is 200 too big.

</div>

Step 4: cross out the carried 4, and write a 0 in the ones column of the second row.

Step 5: multiply 47 by 3, the tens digit. First, $7 \times 3 = 21$: write the 1 to the left of the 0 and carry the 2. Next, $4 \times 3 = 12$, plus the carried 2 makes 14, so write 14. The second row is 1,410, which is $47 \times 30$.

Step 6: add the rows, $282 + 1{,}410 = 1{,}692$. Here is the finished layout, with each line labelled:

$$
\begin{array}{rl}
47 & \\
\underline{\times\,36} & \\
282 & \leftarrow 47 \times 6 \\
\underline{+\,1410} & \leftarrow 47 \times 30 \text{, with a 0 in the ones place} \\
1692 & \leftarrow 282 + 1{,}410
\end{array}
$$

The two rows are the rows of the box in [The idea](#the-idea): the 6 row there holds $240 + 42 = 282$, and the 30 row holds $1{,}200 + 210 = 1{,}410$.

Step 7: check. The answer, 1,692, is a little under the estimate of 2,000, as expected. Multiplying the other way round, $36 \times 47$, gives different rows, $36 \times 7 = 252$ and $36 \times 40 = 1{,}440$, and the same total, $252 + 1{,}440 = 1{,}692$.

</div>

<div class="example" markdown>

### Example 2: a zero in the top number

Work out $308 \times 24$. Step 1: $300 \times 24 = 7{,}200$, from $3 \times 24 = 72$, so expect a little more than 7,200.

Step 3: multiply 308 by 4. First, $8 \times 4 = 32$: write 2 and carry 3. Next comes the 0: $0 \times 4 = 0$, plus the carried 3 is 3, so write 3. Last, $3 \times 4 = 12$, so write 12. The first row is 1,232.

<div class="warning" markdown>

Watch out: the zero still gets its turn. People who skip it add the carried 3 to $3 \times 4$ and write 152, which is $38 \times 4$: the 0 in 308 has disappeared. A quick test catches it. Multiplying by a digit from 1 to 9 never makes a number smaller, so a row can't be smaller than the top number, and 152 is smaller than 308.

</div>

Steps 4 and 5: write the 0, then multiply 308 by 2. First, $8 \times 2 = 16$: write 6 and carry 1. Next, $0 \times 2 = 0$, plus the carried 1 is 1. Last, $3 \times 2 = 6$. The second row is 6,160.

Step 6: add the rows.

$$
\begin{array}{rl}
308 & \\
\underline{\times\,24} & \\
1232 & \leftarrow 308 \times 4 \\
\underline{+\,6160} & \leftarrow 308 \times 20 \\
7392 & \leftarrow 1{,}232 + 6{,}160
\end{array}
$$

Step 7: the answer, 7,392, is a little more than the estimate of 7,200, as expected.

</div>

<div class="example" markdown>

### Example 3: three digits and a carry in every column

Work out $769 \times 58$. The estimate is $800 \times 60 = 48{,}000$, and both factors were rounded up, so expect less than that.

| Row | Work, from right to left | Partial product |
|---|---|---|
| $769 \times 8$ | $9 \times 8 = 72$, write 2, carry 7; $6 \times 8 + 7 = 55$, write 5, carry 5; $7 \times 8 + 5 = 61$ | $6{,}152$ |
| $769 \times 50$ | write 0; $9 \times 5 = 45$, write 5, carry 4; $6 \times 5 + 4 = 34$, write 4, carry 3; $7 \times 5 + 3 = 38$ | $38{,}450$ |

Adding the rows gives $6{,}152 + 38{,}450 = 44{,}602$, which is under the estimate of 48,000, as expected. [Casting out nines](#casting-out-nines) checks this answer a second way.

</div>

## Edge cases and common mistakes

Two mistakes are flagged above, at the step where they happen: adding a carry before multiplying (Example 1) and skipping a zero in the top number (Example 2). Here are the others.

<div class="warning" markdown>

Watch out for a missing shift. Writing the second row of $56 \times 34$ as 168 instead of 1,680 gives 392, the wrong answer from Quick check 3, and the estimate $60 \times 30 = 1{,}800$ catches it at once.

</div>

<div class="warning" markdown>

Watch out for old carries. The carries from the first row belong to that row only, and if you leave them in place it is easy to add them again in the second row. Cross them out at step 4.

</div>

When the bottom number ends in 0, as in $236 \times 40$, its ones row is all zeros. Skip that row: write the 0 and go straight to $236 \times 4 = 944$, so $236 \times 40 = 9{,}440$. The next section handles zeros at the end of either factor.

## Tricks and shortcuts

### Zeros at the end

When a factor ends in zeros, multiply without them, then attach all the zeros from both factors. For $450 \times 30$, work out $45 \times 3 = 135$ and attach two zeros, which gives 13,500. This works because

$$
450 \times 30 = (45 \times 10) \times (3 \times 10) = (45 \times 3) \times 100,
$$

by the commutative and associative properties. Count the zeros before you start. Attaching only one here gives 1,350, and the estimate $500 \times 30 = 15{,}000$ shows that it is ten times too small.

### Casting out nines

The **digit sum** of a whole number is the sum of its digits: the digit sum of 769 is $7 + 6 + 9 = 22$. Take the digit sum again and again until one digit is left, so 769 gives 22, and 22 gives 4. That last digit is the remainder when the number is divided by 9, except that an end result of 9 means a remainder of 0. ([Division facts and remainders](06-division-facts-and-remainders.md#divisibility-rules) shows why a number and its digit sum leave the same remainder.)

**Casting out nines** is a check on a product that compares these remainders. Reduce each factor to one digit, multiply the two digits, and reduce that product to one digit too. Then reduce your answer. If the two final digits differ, the answer is wrong. Here is the check for Example 3:

| Number | Repeated digit sums | Final digit |
|---|---|---|
| $769$ | $7 + 6 + 9 = 22$, then $2 + 2 = 4$ | 4 |
| $58$ | $5 + 8 = 13$, then $1 + 3 = 4$ | 4 |
| $4 \times 4 = 16$ | $1 + 6 = 7$ | 7 |
| $44{,}602$ | $4 + 4 + 6 + 0 + 2 = 16$, then $1 + 6 = 7$ | 7 |

The digits match, so 44,602 passes. The reason is the distributive property again. Write each factor as a multiple of 9 plus its remainder, $769 = 9 \times 85 + 4$ and $58 = 9 \times 6 + 4$, and multiply out. Every partial product except $4 \times 4$ has a factor of 9, so the product is a multiple of 9 plus 16, and it leaves the same remainder as 16, which is 7. The general argument is in divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

<div class="warning" markdown>

Watch out: passing the check doesn't prove the answer is right. Casting out nines misses every mistake that changes the answer by a multiple of 9. Swapping two digits is one such mistake: 44,062 has the same digits as 44,602, so it passes, and it is wrong.

A missing shift is another, because it changes a row from 10 times a number to the number itself, a change of 9 times the number. The wrong 392 from Quick check 3 passes: 56 gives 2, 34 gives 7, $2 \times 7 = 14$ gives 5, and 392 gives 14 and then 5. So use casting out nines together with an estimate. The estimate catches mistakes in size, such as a missing shift, and casting out nines catches many wrong digits that an estimate can't see (Practice problem 4 has one).

</div>

## Practice

### Warm-up

1\. Use the area model to work out $34 \times 26$.

<details class="solution" markdown>
<summary>Solution</summary>

Split $34 = 30 + 4$ and $26 = 20 + 6$, and fill the four boxes:

| $\times$ | $30$ | $4$ |
|---|---|---|
| $20$ | $600$ | $80$ |
| $6$ | $180$ | $24$ |

The product is $600 + 80 + 180 + 24 = 884$.

Check: the estimate $30 \times 30 = 900$ is close. The column method gives the same answer, with rows $34 \times 6 = 204$ and $34 \times 20 = 680$, which add to 884.

</details>

2\. Estimate $53 \times 47$, then work it out with the column method.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate: $50 \times 50 = 2{,}500$.

First row, $53 \times 7$: $3 \times 7 = 21$, write 1, carry 2; then $5 \times 7 + 2 = 37$. The row is 371. Second row, $53 \times 40$: write 0; $3 \times 4 = 12$, write 2, carry 1; then $5 \times 4 + 1 = 21$. The row is 2,120. The answer is $371 + 2{,}120 = 2{,}491$.

Check: 2,491 is close to 2,500, because one factor was rounded up and the other down, so the two errors partly cancel. In the other order, $47 \times 3 = 141$ and $47 \times 50 = 2{,}350$, which add to 2,491.

</details>

### Standard

3\. Work out $607 \times 35$, and check it two ways.

<details class="solution" markdown>
<summary>Solution</summary>

Estimate: $600 \times 35 = 21{,}000$, from $6 \times 35 = 210$.

First row, $607 \times 5$: $7 \times 5 = 35$, write 5, carry 3; $0 \times 5 + 3 = 3$; $6 \times 5 = 30$. The row is 3,035. Second row, $607 \times 30$: write 0; $7 \times 3 = 21$, write 1, carry 2; $0 \times 3 + 2 = 2$; $6 \times 3 = 18$. The row is 18,210. The answer is $3{,}035 + 18{,}210 = 21{,}245$.

Check: the answer is a little over the estimate of 21,000. Casting out nines: 607 gives 13 and then 4, 35 gives 8, $4 \times 8 = 32$ gives 5, and 21,245 gives 14 and then 5. The digits match.

</details>

4\. A classmate works out $84 \times 26$ like this:

$$
\begin{array}{r}
84 \\
\underline{\times\,26} \\
604 \\
\underline{+\,1680} \\
2284
\end{array}
$$

(a) Does the answer pass an estimate? (b) Does it pass casting out nines? (c) Find the mistake and the right answer.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Yes. The estimate is $80 \times 30 = 2{,}400$, and 2,284 is close to it.

(b) No. The factor 84 gives 12 and then 3, 26 gives 8, and $3 \times 8 = 24$ gives 6. But 2,284 gives 16 and then 7. The digits differ, so the answer is wrong.

(c) The first row should be $84 \times 6$. Its first step is right: $4 \times 6 = 24$, write 4, carry 2. In the second step the classmate added the carry before multiplying, $(8 + 2) \times 6 = 60$, instead of $8 \times 6 + 2 = 50$. So the first row is 504, and the answer is $504 + 1{,}680 = 2{,}184$.

Check: 2,184 gives 15 and then 6, which matches. In the other order, $26 \times 4 = 104$ and $26 \times 80 = 2{,}080$, which add to 2,184.

</details>

### Challenge

5\. A theatre has 24 rows of 32 seats, and every ticket costs \$15. How many seats are there, and how much money does a sold-out show bring in?

<details class="solution" markdown>
<summary>Solution</summary>

The number of seats is $32 \times 24$. The rows are $32 \times 4 = 128$ and $32 \times 20 = 640$, so there are $128 + 640 = 768$ seats.

The money is $768 \times 15$ dollars. First row, $768 \times 5$: $8 \times 5 = 40$, write 0, carry 4; $6 \times 5 + 4 = 34$, write 4, carry 3; $7 \times 5 + 3 = 38$. The row is 3,840. Second row, $768 \times 10 = 7{,}680$. The total is $3{,}840 + 7{,}680 = 11{,}520$, so a sold-out show brings in \$11,520.

Check: the estimate $800 \times 15 = 12{,}000$ is a bit high, as it should be, since 768 was rounded up. Casting out nines: 768 gives 21 and then 3, 15 gives 6, and $3 \times 6 = 18$ gives 9; 11,520 also gives 9.

</details>

6\. This one reviews [properties of operations](04-properties-of-operations.md). Work out $125 \times 48$ two ways: with the column method, and by writing $48 = 8 \times 6$ and using the associative property. Which way is faster?

<details class="solution" markdown>
<summary>Solution</summary>

Column method. First row, $125 \times 8$: $5 \times 8 = 40$, write 0, carry 4; $2 \times 8 + 4 = 20$, write 0, carry 2; $1 \times 8 + 2 = 10$. The row is 1,000. Second row, $125 \times 40$: write 0, then $125 \times 4 = 500$, so the row is 5,000. The answer is $1{,}000 + 5{,}000 = 6{,}000$.

With the properties:

$$
125 \times 48 = 125 \times (8 \times 6) = (125 \times 8) \times 6 = 1{,}000 \times 6 = 6{,}000.
$$

The middle step is the associative property. The second way is faster, because $125 \times 8 = 1{,}000$ is one of the round-number products. The column method always works, but look at the numbers first: it isn't always the shortest route.

Check with a third way, the distributive property: $125 \times 48 = 125 \times 50 - 125 \times 2 = 6{,}250 - 250 = 6{,}000$.

</details>

## Where this shows up

- [Multiplying and dividing decimals](13-multiplying-and-dividing-decimals.md) uses the same column method and then places the decimal point.
- Multiplying polynomials is the area model with $x$ in place of 10. In algebra, $(4x + 7)(3x + 6) = 12x^2 + 45x + 42$, and putting in $x = 10$ gives $1{,}200 + 450 + 42 = 1{,}692$, which is $47 \times 36$ ([polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md)).
- Computers multiply binary numbers with the same shifted rows, where each shift is one bit instead of one decimal place (binary arithmetic and two's complement<!-- link: ../06-cs-math/01-number-representation/03-binary-arithmetic-and-twos-complement.md -->). The column method takes about $n^2$ one-digit products for two $n$-digit numbers. Karatsuba's algorithm needs fewer by splitting each number in half, a divide-and-conquer method ([divide and conquer and the master theorem](../06-cs-math/04-sums-recurrences-and-algorithms/05-divide-and-conquer-and-master-theorem.md)).
