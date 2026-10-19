# Division facts and remainders

After this lesson you can find a quotient and remainder from the times tables, decide what a remainder means in a word problem, and test a number for divisibility by 2, 3, 4, 5, 6, 8, 9 and 10 without dividing.

Before this: [multiplication and times tables](03-multiplication-and-times-tables.md) and [properties of operations](04-properties-of-operations.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A ferry carries 9 cars per trip. How many trips does it need to carry 58 cars?
2. Which of the numbers 2, 3, 4, 5, 6, 8, 9 and 10 is 4,572 divisible by?
3. What is $0 \div 9$, and what is $9 \div 0$?

<details class="solution" markdown>
<summary>Answers</summary>

1. 7 trips. Since $58 = 6 \times 9 + 4$, six full trips leave 4 cars, and those need a seventh trip.
2. 2, 3, 4, 6 and 9. The last digit is even, and the digit sum $4 + 5 + 7 + 2 = 18$ is divisible by 3 and by 9. The last two digits make $72 = 18 \times 4$, and divisible by both 2 and 3 means divisible by 6. It is not divisible by 5 or 10 (the last digit is 2), or by 8, since $572 = 71 \times 8 + 4$.
3. Zero divided by 9 is 0, because $0 \times 9 = 0$. But $9 \div 0$ is undefined: no number times 0 gives 9.

</details>

## The idea

You have 24 cookies, and two different questions lead to the same division.

- Share them equally among 4 friends. How many does each friend get?
- Pack them in bags of 4. How many bags do you fill?

Picture the cookies in 4 rows of 6:

$$
\begin{array}{ccccccl}
\bullet & \bullet & \bullet & \bullet & \bullet & \bullet & \quad \text{friend 1} \\
\bullet & \bullet & \bullet & \bullet & \bullet & \bullet & \quad \text{friend 2} \\
\bullet & \bullet & \bullet & \bullet & \bullet & \bullet & \quad \text{friend 3} \\
\bullet & \bullet & \bullet & \bullet & \bullet & \bullet & \quad \text{friend 4}
\end{array}
$$

Read across, each row is one friend's share, so each friend gets 6. Read down, each column of 4 is one bag, so you fill 6 bags.

Both questions are $24 \div 4 = 6$. The first is sharing: you know how many groups there are and want the size of each. The second is grouping: you know the size of each group and want to know how many groups there are. Either way you are looking for the missing number in $4 \times \square = 24$, which is why every division fact is a times-table fact read backwards.

Now take 26 cookies. Each friend still gets 6, and 2 cookies are left that can't be shared out equally. Those 2 are the remainder. What you do with them depends on the question: in a sharing problem you might cut them up, and in a packing problem they might go in a seventh bag that isn't full.

## Definitions

In a division $n \div d$, the **dividend** $n$ is the number being divided, and the **divisor** $d$ is the number you divide by. In $26 \div 4$, the dividend is 26 and the divisor is 4.

Let $n$ and $d$ be whole numbers with $d > 0$. The **quotient** $q$ and the **remainder** $r$ of $n \div d$ are the whole numbers with

$$
n = qd + r \quad \text{and} \quad 0 \le r < d.
$$

Here $qd$ means $q \times d$, and $0 \le r < d$ says that $r$ is at least 0 and less than $d$. In plain words, the quotient is the number of whole times the divisor fits into the dividend, and the remainder is what is left over, which is too small to make another group. For 26 cookies in bags of 4, the quotient is 6 and the remainder is 2, because $26 = 6 \times 4 + 2$ and 2 is less than 4. This is written $26 \div 4 = 6$ remainder 2, sometimes shortened to 6 R 2.

The condition $r < d$ matters. The equation $26 = 5 \times 4 + 6$ is true, but 6 leftover cookies still fill another bag, so 5 and 6 are not the quotient and remainder. [Long division](07-long-division.md) proves that exactly one pair $q$ and $r$ meets both conditions, a theorem called the division algorithm.

A whole number $n$ is **divisible** by a nonzero whole number $d$ when the remainder of $n \div d$ is 0, that is, when $n = kd$ for some whole number $k$. In plain words, $d$ goes into $n$ exactly: 24 is divisible by 4, because $24 = 6 \times 4$, and 26 is not. Other ways to say it are "$d$ divides $n$", "$d$ is a factor of $n$" and "$n$ is a multiple of $d$" ([factors, multiples and primes](08-factors-multiples-and-primes.md)). Later lessons write $d \mid n$.

Two operations are **inverse operations** when each one undoes the other. Multiplying by a nonzero number $d$ and dividing by $d$ are inverse operations: for every number $n$,

$$
(n \times d) \div d = n \quad \text{and} \quad (n \div d) \times d = n.
$$

In plain words, multiply by 4 and then divide by 4, and you are back where you started. Addition and subtraction are inverse operations in the same way. So a division fact is a multiplication fact read backwards: $56 \div 7 = 8$ because $8 \times 7 = 56$.

The **fact family** of two factors and their product is the set of four facts that link them. For 3, 8 and 24 it is

$$
3 \times 8 = 24, \quad 8 \times 3 = 24, \quad 24 \div 3 = 8, \quad 24 \div 8 = 3.
$$

In plain words, each multiplication fact you know gives you two division facts. To find $63 \div 9$, ask "9 times what is 63?", or find 63 in the 9 row of the times table and read the number at the top of its column.

## How to do it

### Finding a quotient and remainder

1. Find the largest multiple of the divisor that is not bigger than the dividend. Walk up the divisor's times table, or start from a fact you know near the dividend.
2. That multiple is $q \times d$, so the number you multiplied by is the quotient $q$.
3. Subtract to get the remainder: $r = n - qd$.
4. Check that $r < d$. If it isn't, the multiple in step 1 was too small: raise $q$ by 1 and take $d$ away from $r$.
5. Check that $qd + r = n$.

When the dividend is too big for the times tables, as in $745 \div 3$, [long division](07-long-division.md) runs these steps one place value at a time.

### Deciding what to do with a remainder

In a word problem the division is the easy part, and the question decides the answer. Here is one division, $75 \div 12 = 6$ remainder 3, answering four questions:

| Question | Answer | What happens to the remainder |
|---|---|---|
| 75 people ride in vans that seat 12. How many vans are needed? | 7 vans | Round up: the 3 extra people still need a van. |
| 75 eggs go into cartons of 12. How many cartons can be filled? | 6 cartons | Round down: 3 eggs don't fill a carton. |
| How many eggs are left over? | 3 eggs | The remainder is the answer. |
| \$75 is split equally among 12 people. How much does each get? | \$6.25 | Keep dividing: the \$3 left over is split 12 ways, and $\frac{3}{12} = \frac{1}{4}$ of a dollar is 25 cents. |

To decide, ask what the answer counts. If everything has to be covered (every person seated, every item shipped), round the quotient up. If only complete groups count (full cartons, things you can afford), round it down. If the amount can be cut into pieces, as money or pizza can, keep the remainder as a fraction or a decimal: $75 \div 12 = 6\frac{3}{12} = 6\frac{1}{4} = 6.25$. [Long division](07-long-division.md) shows how to continue a division into decimals, and [fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md) shows why $\frac{3}{12} = \frac{1}{4}$.

### Divisibility rules

These rules decide whether a number is divisible by $d$ from its digits alone. The digit sum is the sum of the digits, as in casting out nines from [multi-digit multiplication](05-multi-digit-multiplication.md#casting-out-nines).

| Divisor | The number is divisible when | Example |
|---|---|---|
| 2 | its last digit is 0, 2, 4, 6 or 8 | 3,578 |
| 3 | its digit sum is divisible by 3 | 5,184, with digit sum 18 |
| 4 | its last two digits make a number divisible by 4 | 5,184, since $84 = 21 \times 4$ |
| 5 | its last digit is 0 or 5 | 3,575 |
| 6 | it is divisible by both 2 and 3 | 5,184 |
| 8 | its last three digits make a number divisible by 8 | 5,184, since $184 = 23 \times 8$ |
| 9 | its digit sum is divisible by 9 | 5,184, with digit sum 18 |
| 10 | its last digit is 0 | 3,570 |

The rules for 2, 5 and 10 look only at the last digit, because every whole number is a multiple of 10 plus its last digit: $3{,}578 = 357 \times 10 + 8$. The multiple of 10 is divisible by 2, by 5 and by 10, so the last digit decides. The rules for 4 and 8 work the same way, since $100 = 25 \times 4$ and $1{,}000 = 125 \times 8$. In $5{,}184 = 51 \times 100 + 84$, the part $51 \times 100$ is divisible by 4, so only the 84 matters.

For 3 and 9 the reason fits in one line. Each place value is one more than a multiple of 9 ($10 = 9 + 1$, $100 = 99 + 1$, $1{,}000 = 999 + 1$), so every number is a multiple of 9 plus its digit sum. For 5,184 that reads

$$
5{,}184 = (5 \times 999 + 1 \times 99 + 8 \times 9) + (5 + 1 + 8 + 4).
$$

The first bracket is a sum of multiples of 9, so it is a multiple of 9, and of 3 as well (Practice problem 6 proves the fact about sums). So a number and its digit sum leave the same remainder when divided by 9, and the same remainder when divided by 3. That is also the fact casting out nines uses.

The rule for 6 combines two rules. Since $6 = 2 \times 3$, a number divisible by both 2 and 3 is divisible by 6. Combining works here because 2 and 3 have no common factor other than 1, and it fails for 2 and 4, as a warning below shows.

## Worked examples

<div class="example" markdown>

### Example 1: dividing 53 by 7

Step 1: walk up the 7 times table: 7, 14, 21, 28, 35, 42, 49, 56. The multiple 56 is bigger than 53, so the largest multiple that fits is 49. If you know that $7 \times 7 = 49$ and $7 \times 8 = 56$, you can start there instead.

Step 2: since $49 = 7 \times 7$, the quotient is 7.

Step 3: the remainder is $53 - 49 = 4$.

Step 4: 4 is less than 7, so another 7 doesn't fit and the quotient is right.

Step 5: $7 \times 7 + 4 = 49 + 4 = 53$, which is the dividend.

So $53 \div 7 = 7$ remainder 4, or $53 = 7 \times 7 + 4$ in the form of the definition: 53 stickers in packs of 7 make 7 full packs, with 4 stickers left over.

</div>

<div class="example" markdown>

### Example 2: one division, two answers

A teacher has 50 pencils to share equally among 8 students. How many does each student get? Later, the school needs one pencil for each of 50 students, and pencils come in packs of 8. How many packs does it need?

Both questions are $50 \div 8$. The largest multiple of 8 that fits is $48 = 6 \times 8$, so $50 = 6 \times 8 + 2$, with quotient 6 and remainder 2.

In the first question, each student gets 6 pencils and 2 are left over. Round down, since nobody can get a seventh pencil unless someone else misses out. In the second, 6 packs hold only 48 pencils and 2 students would have none, so round up to 7 packs.

Check: $6 \times 8 = 48$ is at most 50, and $7 \times 8 = 56$ is more than 50.

</div>

<div class="example" markdown>

### Example 3: testing 2,316

Test 2,316 for divisibility by 2, 3, 4, 6, 8 and 9.

| Divisor | Test | Divisible? |
|---|---|---|
| 2 | the last digit, 6, is even | yes |
| 3 | the digit sum is $2 + 3 + 1 + 6 = 12$, and $12 = 4 \times 3$ | yes |
| 4 | the last two digits make $16 = 4 \times 4$ | yes |
| 6 | it is divisible by 2 and by 3 | yes |
| 8 | the last three digits make 316, and $316 = 39 \times 8 + 4$ | no |
| 9 | the digit sum, 12, is not a multiple of 9 | no |

The digit sum also gives the remainder for 9: 12 leaves remainder 3 when divided by 9, so 2,316 does too, and indeed $2{,}316 = 257 \times 9 + 3$.

Check two of the "yes" answers by multiplying: $386 \times 6 = 2{,}316$ and $579 \times 4 = 2{,}316$. Notice that 2,316 is divisible by 2 and by 4, but not by 8.

</div>

## Edge cases and common mistakes

Zero divided by a nonzero number is 0: $0 \div 5 = 0$ because $0 \times 5 = 0$, and sharing nothing among 5 people gives each person nothing. The remainder is 0 too, since $0 = 0 \times 5 + 0$, so 0 is divisible by every nonzero whole number. In particular, 0 is even.

A division by 0 is **undefined**: the rules of arithmetic give it no value, so it is not a number and can't be used in a calculation. The answer to $5 \div 0$ would be a number $q$ with $q \times 0 = 5$, and no number works, because every number times 0 is 0 (the zero property from [properties of operations](04-properties-of-operations.md)). Grouping says the same thing: groups of 0 never add up to 5, however many you take.

The case $0 \div 0$ fails in a different way. Every number $q$ satisfies $q \times 0 = 0$, so there is no single answer, and $0 \div 0$ is undefined too. The definition of quotient and remainder asks for $d > 0$ for the same reason: no remainder $r$ satisfies $0 \le r < 0$.

Dividing by 1 changes nothing, and a nonzero number divided by itself is 1: $9 \div 1 = 9$ and $9 \div 9 = 1$. When the dividend is smaller than the divisor, the quotient is 0 and the remainder is the dividend: $5 \div 8 = 0$ remainder 5, because $5 = 0 \times 8 + 5$.

<div class="warning" markdown>

Watch out: a remainder must be smaller than the divisor. Writing $38 \div 5 = 6$ remainder 8 breaks $r < d$, because the 8 left over still holds another 5. The right answer is 7 remainder 3. Check: $7 \times 5 + 3 = 38$, and 3 is less than 5.

</div>

<div class="warning" markdown>

Watch out: round up only when there is a remainder. Seventy-two people in vans that seat 12 need exactly 6 vans, because $72 = 6 \times 12 + 0$. A seventh van would be empty.

</div>

<div class="warning" markdown>

Watch out: a remainder is not a decimal digit. The answer $75 \div 12 = 6$ remainder 3 is not 6.3, because the 3 left over stands for $\frac{3}{12}$ of a whole, so the decimal is 6.25. Multiplying back catches the slip: $6.3 \times 12 = 75.6$, not 75.

</div>

<div class="warning" markdown>

Watch out: the digit-sum test works only for 3 and 9. The number 28 is divisible by 4, but its digit sum, 10, is not, so for 4 and 8 use the last two or three digits. Rules also combine only for divisors with no common factor other than 1. The number 12 is divisible by 2 and by 4 but not by 8, because 2 and 4 share the factor 2, while 2 and 3 share no factor and combine to give the rule for 6.

</div>

## Tricks and shortcuts

Dividing by 4 is halving twice, and dividing by 8 is halving three times, because $8 = 2 \times 2 \times 2$. For $184 \div 8$, halve three times: 184, 92, 46, 23.

Dividing by 5 is doubling and then dividing by 10: $135 \div 5 = 270 \div 10 = 27$.

The rules give remainders as well as yes-or-no answers. The last digit is the remainder for 10, and the digit sum gives the remainder for 3 and 9, as in Example 3. When you add up the digits for the 9 rule, you can skip every 9 and every group of digits that adds to 9. In 9,459, skip both 9s and the pair $4 + 5$: nothing is left, so 9,459 is divisible by 9.

## In code

Python's `//` and `%` operators give the quotient and the remainder, and each way of handling a remainder is one line.

<details class="code" markdown>
<summary>In code</summary>

```python
n, d = 75, 12
print(n // d, n % d)   # 6 3: quotient and remainder, since 75 = 6 * 12 + 3
print(divmod(n, d))    # (6, 3): both at once
print(n / d)           # 6.25: keep the remainder as a decimal
print(-(-n // d))      # 7: round up, the number of vans
print(0 // d, 0 % d)   # 0 0

try:
    n // 0
except ZeroDivisionError:
    print("dividing by 0 raises ZeroDivisionError")
```

The operator `//` always rounds down, so `-(-n // d)` rounds up: negating before and after the division turns rounding down into rounding up. The same line gives the number of pages needed to show `n` items with `d` items on each page.

</details>

## Practice

### Warm-up

1\. Write the fact family for 7, 9 and 63, and use it to find $63 \div 7$ and $63 \div 9$.

<details class="solution" markdown>
<summary>Solution</summary>

The fact family is $7 \times 9 = 63$, $9 \times 7 = 63$, $63 \div 7 = 9$ and $63 \div 9 = 7$. So $63 \div 7 = 9$ and $63 \div 9 = 7$.

Check by multiplying back: $9 \times 7 = 63$ and $7 \times 9 = 63$.

</details>

2\. Find the quotient and remainder, and write each answer in the form $n = qd + r$: (a) $47 \div 6$, (b) $60 \div 7$, (c) $5 \div 9$, (d) $0 \div 4$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The 6 times table goes 36, 42, 48, and 48 is too big, so the quotient is 7 and the remainder is $47 - 42 = 5$: $47 = 7 \times 6 + 5$.
- (b) The 7 times table goes 49, 56, 63, and 63 is too big, so $60 = 8 \times 7 + 4$.
- (c) Nine doesn't fit into 5 even once, so the quotient is 0 and the remainder is 5: $5 = 0 \times 9 + 5$.
- (d) Zero divided by 4 is 0 with nothing left over: $0 = 0 \times 4 + 0$.

Check: each remainder is less than its divisor (5 is less than 6, 4 less than 7, 5 less than 9, and 0 less than 4), and the right sides work out to 47, 60, 5 and 0.

</details>

### Standard

3\. A class of 45 students goes on an overnight trip. (a) Each hostel room sleeps 6. How many rooms are needed? (b) The class has \$100 for snacks, and a bag of snacks costs \$6. How many bags can it buy? (c) In one room, 6 roommates split a \$27 pizza bill equally. How much does each pay?

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $45 = 7 \times 6 + 3$. Seven rooms hold 42 students, and the other 3 still need beds, so round up: 8 rooms.
- (b) $100 = 16 \times 6 + 4$. Sixteen bags cost \$96, and the \$4 left can't buy another bag, so round down: 16 bags.
- (c) $27 = 4 \times 6 + 3$. Money can be split, so keep the remainder as a fraction: each pays $4\frac{3}{6} = 4\frac{1}{2}$ dollars, which is \$4.50.

Check: $8 \times 6 = 48$ beds is enough for 45 students, while $7 \times 6 = 42$ is not. Sixteen bags cost \$96, within budget, while 17 would cost \$102. And $6 \times 4.50 = 27$.

</details>

4\. Use the divisibility rules to test 3,816 for divisibility by 2, 3, 4, 5, 6, 8, 9 and 10. Then check two of your "yes" answers by multiplying.

<details class="solution" markdown>
<summary>Solution</summary>

| Divisor | Test | Divisible? |
|---|---|---|
| 2 | the last digit, 6, is even | yes |
| 3 | the digit sum is $3 + 8 + 1 + 6 = 18$, and $18 = 6 \times 3$ | yes |
| 4 | the last two digits make $16 = 4 \times 4$ | yes |
| 5 | the last digit is not 0 or 5 | no |
| 6 | it is divisible by 2 and by 3 | yes |
| 8 | the last three digits make $816 = 102 \times 8$ | yes |
| 9 | the digit sum is $18 = 2 \times 9$ | yes |
| 10 | the last digit is not 0 | no |

So 3,816 is divisible by 2, 3, 4, 6, 8 and 9, and not by 5 or 10.

Check: $477 \times 8 = 3{,}816$ and $424 \times 9 = 3{,}816$.

</details>

### Challenge

5\. The four-digit number $47\square 2$ has one digit missing. (a) Which digit makes it divisible by 9? (b) Which digits make it divisible by 3? (c) Which of the numbers from (b) are also divisible by 4?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The known digits add to $4 + 7 + 2 = 13$, so the digit sum is 13 plus the missing digit, somewhere from 13 to 22. The only multiple of 9 in that range is 18, so the missing digit is 5 and the number is 4,752.

(b) The multiples of 3 from 13 to 22 are 15, 18 and 21, so the missing digit is 2, 5 or 8. The numbers are 4,722, 4,752 and 4,782.

(c) Their last two digits are 22, 52 and 82. Only 52 is divisible by 4, since $52 = 13 \times 4$, so 4,752 is the only one.

Check: $528 \times 9 = 4{,}752$, $1{,}188 \times 4 = 4{,}752$, $1{,}574 \times 3 = 4{,}722$ and $1{,}594 \times 3 = 4{,}782$.

</details>

6\. This one reviews the distributive property from [properties of operations](04-properties-of-operations.md). Show that if two whole numbers are both divisible by 3, then their sum is divisible by 3. Then explain how this fact is used in the rule for 3.

<details class="solution" markdown>
<summary>Solution</summary>

Call the two numbers $n$ and $m$. We know they are divisible by 3, so by the definition of divisible, $n = 3 \times j$ and $m = 3 \times k$ for some whole numbers $j$ and $k$. We want to write $n + m$ as 3 times a whole number. The plan is to pull out the common factor 3.

*Proof.*

$$
\begin{aligned}
n + m &= 3 \times j + 3 \times k \\
&= 3 \times (j + k) && \text{distributive property, read from right to left}
\end{aligned}
$$

Since $j + k$ is a whole number, $n + m$ is divisible by 3.

Look back: nothing about 3 was special, so the same proof works for every divisor. With subtraction it works for differences too, since $3 \times j - 3 \times k = 3 \times (j - k)$. Check with numbers: for $21 + 15 = 36$, the proof uses $j = 7$ and $k = 5$, and $3 \times (7 + 5) = 36$.

The rule for 3 uses this fact in both directions. A number is a multiple of 9 plus its digit sum, as in $5{,}184 = 5{,}166 + 18$, and a multiple of 9 is a multiple of 3. If the digit sum is divisible by 3, the number is a sum of two multiples of 3, so it is divisible by 3. If the number is divisible by 3, the digit sum is a difference of two multiples of 3, as in $18 = 5{,}184 - 5{,}166$, so it is divisible by 3 too.

</details>

## Where this shows up

- [Long division](07-long-division.md), the next lesson, finds the quotient and remainder when the dividend is too big for the times tables.
- A division is a fraction, $n \div d = \frac{n}{d}$, and the remainder becomes the fraction part of a mixed number ([fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md)). The divisibility rules speed up finding factors and simplifying fractions ([factors, multiples and primes](08-factors-multiples-and-primes.md)).
- Rounding a quotient up or down is the ceiling or the floor of the fraction: $\lceil 75/12 \rceil = 7$ and $\lfloor 75/12 \rfloor = 6$ ([piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md)). In code, the remainder `n % d` tests for even and odd and sorts keys into hash buckets, and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md --> proves the digit-sum rules in general.
