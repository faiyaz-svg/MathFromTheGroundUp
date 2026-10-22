# Integer arithmetic and sign rules

After this lesson you can add, subtract, multiply and divide integers, and explain from the distributive property why a negative number times a negative number is positive.

Before this: [negative numbers and absolute value](01-negative-numbers-and-absolute-value.md) and [properties of operations](../../01-elementary/04-properties-of-operations.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $-8 + 3$ and $-8 - 3$.
2. Work out $6 - (-9)$ and $-4 - (-10)$.
3. Work out $(-4) \times (-7)$, $(-36) \div 4$ and $(-2) \times (-3) \times (-5)$.

<details class="solution" markdown>
<summary>Answers</summary>

1. The answers are $-5$ and $-11$. Adding 3 moves 3 steps right from $-8$, and subtracting 3 moves 3 steps left.
2. 15 and 6. Subtracting a negative number is adding its opposite: $6 + 9 = 15$ and $-4 + 10 = 6$.
3. 28, $-9$ and $-30$. Two negative factors give a positive product; one negative number, or three, give a negative answer.

</details>

## The idea

Think of a bank account as a running total. A deposit is a positive number, a purchase is a negative number, and the balance is the sum of everything so far. Start at \$30 and buy something for \$45: the balance is $30 + (-45) = -15$, overdrawn by \$15. On the number line, adding a positive number moves right and adding a negative number moves left. From 30, move 45 steps left: the first 30 steps reach 0, and the other 15 end at $-15$.

Now suppose the bank finds that a \$20 charge on your account was a mistake and removes it. Taking away a $-20$ raises your balance by 20, exactly as a deposit of 20 would. So subtracting a negative number is adding a positive one, and in general, subtracting a number has the same effect as adding its opposite.

Multiplication as repeated addition still works when the number being repeated is negative. Three purchases of \$4 each change the balance by $3 \times (-4) = (-4) + (-4) + (-4) = -12$. A negative times a negative can't be read that way, since there is no such thing as adding a number negative three times. A pattern suggests the answer:

| Product | Value |
|---|---|
| $3 \times (-4)$ | $-12$ |
| $2 \times (-4)$ | $-8$ |
| $1 \times (-4)$ | $-4$ |
| $0 \times (-4)$ | $0$ |
| $(-1) \times (-4)$ | ? |
| $(-2) \times (-4)$ | ? |

Each time the first factor goes down by 1, the product goes up by 4. If the pattern continues, $(-1) \times (-4) = 4$ and $(-2) \times (-4) = 8$. A pattern is not a proof, though. The section [Why a negative times a negative is positive](#why-a-negative-times-a-negative-is-positive) shows that the distributive property forces this answer: every other value would break a rule of arithmetic you already use.

## Definitions

The opposite $-a$ from the last lesson is also called the **additive inverse** of $a$, because adding it undoes adding $a$:

$$
a + (-a) = 0.
$$

In plain words, a number and its opposite cancel, like a \$7 deposit and a \$7 purchase: $7 + (-7) = 0$.

For integers, subtraction is defined as adding the opposite. For all numbers $a$ and $b$,

$$
a - b = a + (-b).
$$

This agrees with [addition and subtraction](../../01-elementary/02-addition-and-subtraction.md), where $a - b$ is the number you add to $b$ to get $a$, because adding $b$ to $a + (-b)$ gives $a + (-b) + b = a + 0 = a$. The new version also works when $b$ is bigger than $a$: $3 - 7 = 3 + (-7) = -4$, the value that lesson pointed to.

The **sign rules** for multiplication and division say what sign the answer has when neither number is 0:

| Signs of the two numbers | Sign of the product or quotient | Example |
|---|---|---|
| positive and positive | positive | $3 \times 4 = 12$ |
| negative and negative | positive | $(-3) \times (-4) = 12$ |
| positive and negative | negative | $3 \times (-4) = -12$ |
| negative and positive | negative | $(-12) \div 4 = -3$ |

The absolute value of the answer doesn't depend on the signs: $\lvert a \times b \rvert = \lvert a \rvert \times \lvert b \rvert$. In plain words, the same signs give a positive answer, different signs give a negative one, and the size is worked out as if there were no signs at all. A product with a factor of 0 is 0, which has no sign.

Division follows the same rules because of how it is defined. For a number $b \ne 0$, the quotient $a \div b$ is the number $q$ with $q \times b = a$, as in [division facts and remainders](../../01-elementary/06-division-facts-and-remainders.md). So $(-12) \div 4 = -3$ because $(-3) \times 4 = -12$, and $(-12) \div (-4) = 3$ because $3 \times (-4) = -12$.

## How to do it

### Adding integers

1. If the two numbers have the same sign, add their absolute values and keep the sign: $-8 + (-5) = -13$.
2. If the signs differ, subtract the smaller absolute value from the larger, and give the answer the sign of the number with the larger absolute value. So $-8 + 5 = -3$, because $8 - 5 = 3$ and $-8$ has the larger absolute value.
3. If the numbers are opposites, the sum is 0. Adding 0 changes nothing.
4. Check on the number line: start at the first number and move right for a positive number, left for a negative one.

Step 2 is the distance rule from the last lesson at work. The sum $-8 + 5$ starts 8 steps left of 0 and moves 5 steps right, which ends 3 steps left of 0.

### Subtracting integers

1. Rewrite the subtraction as adding the opposite: keep the first number, change the minus sign to a plus sign, and change the second number to its opposite. So $-4 - (-10)$ becomes $-4 + 10$.
2. Add, using the steps above.
3. Check by adding back: $(a - b) + b$ should be $a$.

Watch out at Step 1: only the number right after the minus sign changes. In $-4 - (-10)$ the first number, $-4$, stays as it is.

The result has a meaning worth remembering: $a - b$ is the step you take to get from $b$ to $a$ on the number line. It is positive when $a$ is to the right of $b$ and negative when $a$ is to the left, so $a - b > 0$ says exactly that $a > b$.

### Multiplying and dividing integers

1. Multiply or divide the absolute values.
2. Find the sign. With two numbers, the same signs give a positive answer and different signs a negative one. With several factors, count the negative ones: an even number of negative factors gives a positive product, and an odd number gives a negative product.
3. Watch for 0. A product with a factor of 0 is 0. A division by 0 is undefined, so stop. A dividend of 0 with a nonzero divisor gives 0.
4. Check a division by multiplying back.

Counting works in Step 2 because the negative factors can be paired up, and each pair multiplies to a positive number. If one negative factor is left over, it makes the product negative.

### Mixed calculations

As with whole numbers, multiply and divide before you add and subtract. Put brackets around a negative number that follows an operation sign, as in $5 - (-3)$ and $4 \times (-2)$. Writing $5 - -3$ is legal but easy to misread as $5 - 3$. Powers of negative numbers, where $(-3)^2$ and $-3^2$ are different numbers, come in [exponents and order of operations](04-exponents-and-order-of-operations.md).

### Why a negative times a negative is positive

Here is the argument with numbers first. The zero property says $(-3) \times 0 = 0$. Write the 0 as $4 + (-4)$ and use the distributive property:

$$
0 = (-3) \times \bigl(4 + (-4)\bigr) = (-3) \times 4 + (-3) \times (-4) = -12 + (-3) \times (-4).
$$

So $-12$ plus the unknown product is 0. The number that adds to $-12$ to give 0 is 12, so $(-3) \times (-4) = 12$. The same argument works for every pair of numbers, which is what the theorem below says.

*Theorem.* For all numbers $a$ and $b$,

$$
(-a) \times (-b) = a \times b.
$$

We know the properties of operations (commutative, associative, identity, zero and distributive), which hold for negative numbers as well as positive ones. We also know the definition of the opposite, $x + (-x) = 0$. Finally, a number has only one opposite: if $x + y = 0$, then $y = -x$. Practice problem 7 proves this fact, and also that $-(-x) = x$. We want to show that $(-a) \times (-b) = a \times b$. The plan is to prove the sign rule for a positive times a negative first, as a lemma, and then use it twice.

*Lemma.* For all numbers $a$ and $b$, $a \times (-b) = -(a \times b)$.

*Proof of the lemma.*

$$
\begin{aligned}
a \times b + a \times (-b) &= a \times \bigl(b + (-b)\bigr) && \text{distributive property} \\
&= a \times 0 && \text{definition of the opposite} \\
&= 0 && \text{zero property}
\end{aligned}
$$

So $a \times (-b)$ adds to $a \times b$ to give 0. A number has only one opposite, so $a \times (-b) = -(a \times b)$.

*Proof of the theorem.*

$$
\begin{aligned}
(-a) \times (-b) &= -\bigl((-a) \times b\bigr) && \text{lemma, with } -a \text{ in place of } a \\
&= -\bigl(b \times (-a)\bigr) && \text{commutative property} \\
&= -\bigl(-(b \times a)\bigr) && \text{lemma, with } b \text{ and } a \text{ in place of } a \text{ and } b \\
&= b \times a && \text{the opposite of the opposite} \\
&= a \times b && \text{commutative property}
\end{aligned}
$$

Look back: the proof used only the rules you already accept for whole numbers, plus the meaning of the opposite. So once negative numbers obey the distributive property, a negative times a negative has to be positive; there is no choice left to make. The lemma explains the other sign rule too, since it says a positive number times a negative one is the opposite of a positive product. With $a = 3$ and $b = 4$, the theorem gives $(-3) \times (-4) = 12$, as in the version with numbers.

<div class="note" markdown>

A university course builds arithmetic this way. It takes the commutative, associative, identity and distributive properties as axioms, and then proves facts such as the zero property and the sign rules from them. Practice problem 5 of [properties of operations](../../01-elementary/04-properties-of-operations.md#practice) proves the zero property that way, and this section did the same for the sign rules. The full list of axioms is in [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md).

</div>

## Worked examples

<div class="example" markdown>

### Example 1: a change in temperature

At 6 a.m. the temperature in Edmonton is $-14$°C, and at 3 p.m. it is $-2$°C. By 11 p.m. it has fallen to $-17$°C. Find the change from 6 a.m. to 3 p.m., and from 3 p.m. to 11 p.m.

A change is the new value minus the old value. A positive change is a rise, and a negative change is a drop.

From 6 a.m. to 3 p.m., the change is $-2 - (-14)$.

Subtracting, Step 1: keep $-2$, change the minus sign to a plus sign, and change $-14$ to its opposite, 14. The calculation becomes $-2 + 14$.

Step 2: add. The signs differ, so subtract the absolute values, $14 - 2 = 12$, and take the sign of 14, which has the larger absolute value. The change is 12: the temperature rose 12 degrees.

Step 3: check by adding back. Starting from $-14$ and adding the change gives $-14 + 12 = -2$, the 3 p.m. reading. The distance rule from the last lesson agrees: $-14$ and $-2$ are on the same side of 0, and $14 - 2 = 12$.

From 3 p.m. to 11 p.m., the change is $-17 - (-2) = -17 + 2$. The signs differ, $17 - 2 = 15$, and $-17$ has the larger absolute value, so the change is $-15$: the temperature dropped 15 degrees. Check: $-2 + (-15) = -17$.

<div class="warning" markdown>

Watch out: the order is new minus old. Working out $-14 - (-2) = -12$ for the first change gives the right size with the wrong sign, and it would say the temperature fell during the day. Swapping the two numbers in a subtraction always flips the sign of the answer, because $b - a$ is the opposite of $a - b$.

</div>

</div>

<div class="example" markdown>

### Example 2: a running balance

Your account holds \$85. You pay \$120 for a textbook, get a \$40 refund, and are charged a \$15 fee. What is the balance now?

Write each amount as a signed number and add: $85 + (-120) + 40 + (-15)$. Every operation is now an addition, so the commutative and associative properties let you collect the positive and negative amounts:

$$
(85 + 40) + \bigl((-120) + (-15)\bigr) = 125 + (-135) = -10.
$$

The last step has different signs, so $135 - 125 = 10$ with the sign of $-135$. The account is overdrawn by \$10.

Check by going in order: $85 - 120 = -35$, then $-35 + 40 = 5$, then $5 - 15 = -10$.

</div>

<div class="example" markdown>

### Example 3: many factors, and zeros

- (a) $(-2) \times (-3) \times (-5) \times 4$. The absolute values multiply to $2 \times 3 \times 5 \times 4 = 120$. There are three negative factors, an odd number, so the product is $-120$.
- (b) $(-48) \div (-6)$. The same signs give a positive quotient, 8. Check: $8 \times (-6) = -48$.
- (c) $(-7) \times 0 \times (-9) = 0$. A factor of 0 makes the product 0, and the sign rule has nothing to decide, since 0 is neither positive nor negative.
- (d) $0 \div (-5) = 0$, because $0 \times (-5) = 0$.
- (e) $(-5) \div 0$ is undefined. It would have to be a number $q$ with $q \times 0 = -5$, and every number times 0 is 0.

Check (a) by multiplying in order: $(-2) \times (-3) = 6$, then $6 \times (-5) = -30$, then $-30 \times 4 = -120$.

</div>

<div class="example" markdown>

### Example 4: mixed operations (finish it yourself)

Work out $-3 \times 4 - (-10) \div 2$.

Multiply and divide first. The product $-3 \times 4$ has different signs, so it is $-12$. The quotient $(-10) \div 2$ also has different signs, so it is $-5$. The expression is now

$$
-12 - (-5).
$$

Finish the subtraction with the steps for subtracting integers, and check your answer.

<details class="solution" markdown>
<summary>Finish</summary>

Step 1: keep $-12$, change the subtraction to an addition, and change $-5$ to 5: $-12 + 5$. Step 2: the signs differ, $12 - 5 = 7$, and $-12$ has the larger absolute value, so the answer is $-7$.

Check: on the number line, start at $-12$ and move 5 steps right to $-7$. Adding back also works: $-7 + (-5) = -12$.

</details>

</div>

## Edge cases and common mistakes

The wrong order in a change (old minus new) is flagged in Example 1. Here are the others.

<div class="warning" markdown>

Watch out: "two negatives make a positive" is a rule for multiplication and division only. The sum $-3 + (-5)$ is $-8$, not 8: two purchases make a bigger overdraft, not a deposit. On the number line, start at $-3$ and move 5 more steps left.

</div>

<div class="warning" markdown>

Watch out when subtracting a negative number. The difference $6 - (-9)$ is $6 + 9 = 15$, not $6 - 9 = -3$. The slip comes from ignoring the brackets, which changes only one of the two signs. Check by adding back: $15 + (-9) = 6$, while $-3 + (-9) = -12$.

</div>

<div class="warning" markdown>

Watch out: counting negative factors decides the sign only when no factor is 0. In $(-1) \times (-1) \times (-1) \times 0$ there are three negative factors, but the product is 0, not a negative number.

</div>

Division by 0 stays undefined with negative numbers, for the same reason as before: $(-5) \div 0$ and $5 \div 0$ would both need a number that gives a nonzero answer when multiplied by 0. A dividend of 0 is fine: $0 \div (-5) = 0$.

The theorem $(-a) \times (-b) = a \times b$ doesn't say that $a$ and $b$ are positive. The letters can stand for negative numbers too. With $a = -3$ and $b = 2$, the left side is $(-(-3)) \times (-2) = 3 \times (-2) = -6$, and the right side is $(-3) \times 2 = -6$. Remember from the last lesson that $-a$ is "the opposite of $a$", which can be positive.

## Tricks and shortcuts

For subtraction, say "keep, change, change": keep the first number, change the minus to a plus, change the sign of the second number. So $-7 - (-12)$ becomes $-7 + 12 = 5$.

When you add a long list of positive and negative numbers, add the positive ones, add the negative ones, and combine the two totals at the end, as in Example 2. Only one step then has different signs.

Multiplying by $-1$ gives the opposite: $(-1) \times a = -a$ (Practice problem 7). So "take the opposite" and "multiply by $-1$" are the same operation. A minus sign in front of brackets can then be multiplied in like an ordinary factor: $-(3 - 8) = -3 + 8 = 5$. Working inside the brackets first agrees, since $3 - 8 = -5$, whose opposite is 5.

The difference $a - b$ is the step from $b$ to $a$. To find how far a value moved and in which direction, subtract the old value from the new one; the sign gives the direction and the absolute value gives the size.

## In code

For exact divisions, every programming language follows the sign rules. When a division leaves a remainder, languages disagree about negative numbers, and this is a common source of bugs.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

print(6 - -9, -4 - (-10))      # 15 6
print((-4) * (-7), -36 // 4)   # 28 -9
print(-7 // 2, -7 % 2)         # -4 1
print(math.trunc(-7 / 2))      # -3
print(divmod(-17, 5))          # (-4, 3), because -17 = 5 * (-4) + 3
```

Python's `//` rounds the quotient down, to the next integer to the left, so that the remainder `%` is never negative when the divisor is positive: $-7 = 2 \times (-4) + 1$. C, C++ and Java instead round the quotient toward 0, so in those languages `-7 / 2` is `-3` and `-7 % 2` is `-1`, since $-7 = 2 \times (-3) + (-1)$. A test such as `n % 2 == 1` for odd numbers therefore fails for negative odd `n` in Java, while `n % 2 != 0` works in every language.

</details>

## FAQ

### Could we define a negative times a negative to be negative instead?

Not without breaking the distributive property. Suppose $(-1) \times (-1)$ were $-1$. The zero property gives $(-1) \times \bigl(1 + (-1)\bigr) = (-1) \times 0 = 0$. Distributing the same product gives $(-1) \times 1 + (-1) \times (-1) = -1 + (-1) = -2$. Both are the same expression, so $0 = -2$, which is false. The sign rule is not a convention someone picked; the other rules of arithmetic force it.

### Is there a real situation where a negative times a negative comes up?

Yes, whenever a rate and a time can both be negative. A tank drains at 3 L per minute, which is a rate of $-3$ L per minute. Measure time from now, so that 4 minutes ago is $-4$ minutes. The change in the water from now to then is the rate times the time, $(-3) \times (-4) = 12$, so 4 minutes ago the tank held 12 L more than it does now. That matches common sense: a draining tank had more water in the past.

### Why bother writing subtraction as adding the opposite?

Addition is commutative and associative, and subtraction is neither ([properties of operations](../../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division)). Once every subtraction is an addition of a signed number, you can reorder and regroup freely, as Example 2 did. Algebra relies on this whenever it collects terms, as in [equivalent expressions](../03-expressions-equations-inequalities/02-equivalent-expressions.md).

## Practice

### Warm-up

1\. Work out (a) $-9 + 4$, (b) $-9 + (-4)$, (c) $9 + (-4)$ and (d) $-15 + 15$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The signs differ: $9 - 4 = 5$, with the sign of $-9$, so $-5$.
- (b) The signs are the same: $9 + 4 = 13$, kept negative, so $-13$.
- (c) The signs differ: $9 - 4 = 5$, with the sign of 9, so 5.
- (d) The numbers are opposites, so the sum is 0.

Check on the number line: from $-9$, four steps right reach $-5$ and four steps left reach $-13$; from 9, four steps left reach 5.

</details>

2\. Work out (a) $4 - 11$, (b) $-4 - 11$, (c) $-4 - (-11)$ and (d) $0 - (-6)$.

<details class="solution" markdown>
<summary>Solution</summary>

Rewrite each as adding the opposite, then add.

- (a) $4 + (-11) = -7$.
- (b) $-4 + (-11) = -15$.
- (c) $-4 + 11 = 7$.
- (d) $0 + 6 = 6$.

Check by adding back: $-7 + 11 = 4$, $-15 + 11 = -4$, $7 + (-11) = -4$ and $6 + (-6) = 0$.

</details>

3\. Work out (a) $(-6) \times 7$, (b) $(-6) \times (-7)$, (c) $(-56) \div 8$, (d) $(-56) \div (-7)$ and (e) $(-1) \times (-1) \times (-1) \times (-1) \times (-1)$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Different signs: $-42$.
- (b) The same signs: 42.
- (c) Different signs: $-7$.
- (d) The same signs: 8.
- (e) Five negative factors, an odd number, so the product is $-1$.

Check the divisions by multiplying back: $(-7) \times 8 = -56$ and $8 \times (-7) = -56$.

</details>

### Standard

4\. (a) The overnight low in Thunder Bay was $-23$°C, and the high the next afternoon was $-6$°C. What was the change from the low to the high? (b) A diver at an elevation of $-30$ m rises 12 m, then goes down 25 m. What is her elevation now?

<details class="solution" markdown>
<summary>Solution</summary>

(a) New minus old: $-6 - (-23) = -6 + 23 = 17$. The temperature rose 17 degrees.

(b) A rise is positive and a descent is negative: $-30 + 12 + (-25)$. First $-30 + 12 = -18$, then $-18 + (-25) = -43$. She is at $-43$ m, 43 m below the surface.

Check: (a) $-23 + 17 = -6$. (b) Collect the moves: $12 + (-25) = -13$, so she ends 13 m deeper than she started, and $-30 + (-13) = -43$.

</details>

5\. Work out (a) $(-3) \times (-4) - 20$, (b) $(-24) \div 6 + (-2) \times (-5)$, (c) $7 - 3 \times (-2)$ and (d) $(-18) \div (-3) \times (-2)$.

<details class="solution" markdown>
<summary>Solution</summary>

Multiply and divide first, then add and subtract.

- (a) $(-3) \times (-4) = 12$, and $12 - 20 = -8$.
- (b) $(-24) \div 6 = -4$ and $(-2) \times (-5) = 10$, so $-4 + 10 = 6$.
- (c) $3 \times (-2) = -6$, and $7 - (-6) = 7 + 6 = 13$.
- (d) Division and multiplication from left to right: $(-18) \div (-3) = 6$, then $6 \times (-2) = -12$.

Check (c) another way: subtracting $3 \times (-2)$ means taking away three charges of 2, which adds 6 to the 7.

</details>

6\. The overnight lows on five days were $-12$°C, $-5$°C, 3°C, $-8$°C and $-13$°C. (a) Find their mean, the sum divided by 5. (b) Which day's low was closest to the mean?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Collect the negative lows: $-12 + (-5) + (-8) + (-13) = -38$. Add the positive one: $-38 + 3 = -35$. Divide: $(-35) \div 5 = -7$, so the mean is $-7$°C.

(b) The distance from each low to $-7$ is $\lvert x - (-7) \rvert = \lvert x + 7 \rvert$:

| Low | Distance from $-7$ |
|---|---|
| $-12$ | $\lvert -12 + 7 \rvert = 5$ |
| $-5$ | $\lvert -5 + 7 \rvert = 2$ |
| $3$ | $\lvert 3 + 7 \rvert = 10$ |
| $-8$ | $\lvert -8 + 7 \rvert = 1$ |
| $-13$ | $\lvert -13 + 7 \rvert = 6$ |

The $-8$°C day was closest, 1 degree from the mean.

Check: $(-7) \times 5 = -35$, the sum of the lows. The mean is also between the lowest and highest values, $-13$ and 3, as a mean must be.

</details>

### Challenge

7\. (a) Prove that if $x + y = 0$, then $y = -x$. Use the identity, commutative and associative properties of addition and the definition of the opposite. (b) Use (a) to prove that $-(-x) = x$ for every number $x$. (c) Use the lemma in this lesson to prove that $(-1) \times a = -a$ for every number $a$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) We know that $x + y = 0$, and we want to show that $y$ is the opposite of $x$. The plan is to start from $y$, add 0 in a useful form, and regroup.

$$
\begin{aligned}
y &= 0 + y && \text{identity property} \\
&= \bigl((-x) + x\bigr) + y && \text{definition of the opposite, and the commutative property} \\
&= (-x) + (x + y) && \text{associative property} \\
&= (-x) + 0 && \text{since } x + y = 0 \\
&= -x && \text{identity property}
\end{aligned}
$$

(b) The definition of the opposite, with the commutative property, gives $(-x) + x = 0$. This is the hypothesis of (a) with $-x$ in place of $x$ and $x$ in place of $y$. So (a) says that $x$ is the opposite of $-x$, which is the statement $x = -(-x)$.

(c) The lemma says $a \times (-b) = -(a \times b)$. With $b = 1$ it gives $a \times (-1) = -(a \times 1) = -a$, using the identity property. The commutative property turns $a \times (-1)$ into $(-1) \times a$, so $(-1) \times a = -a$.

Look back: (a) is the fact "a number has only one opposite" that the proof of the lemma used. Part (c) is why the next lessons can treat a minus sign in front of an expression as a factor of $-1$. Check (c) with numbers: $(-1) \times 5 = -5$, and $(-1) \times (-5) = 5 = -(-5)$.

</details>

8\. This one reviews the division algorithm from [long division](../../01-elementary/07-long-division.md). The theorem there also holds when $n$ is a negative integer: for every integer $n$ and every whole number $d > 0$, there are unique integers $q$ and $r$ with $n = qd + r$ and $0 \le r < d$. Find $q$ and $r$ for (a) $n = -17$, $d = 5$, (b) $n = -20$, $d = 4$ and (c) $n = -1$, $d = 7$.

<details class="solution" markdown>
<summary>Solution</summary>

As in the proof in that lesson, $qd$ is the largest multiple of $d$ that is not bigger than $n$, and $r = n - qd$ is what is left.

- (a) The multiples of 5 near $-17$ are $-15$ and $-20$. The number $-15$ is bigger than $-17$, so the largest multiple not bigger than $-17$ is $-20 = 5 \times (-4)$. So $q = -4$ and $r = -17 - (-20) = 3$.
- (b) The number $-20 = 4 \times (-5)$ is itself a multiple of 4, so $q = -5$ and $r = 0$.
- (c) The largest multiple of 7 not bigger than $-1$ is $-7 = 7 \times (-1)$. So $q = -1$ and $r = -1 - (-7) = 6$.

Watch out in (a): $-17 = 5 \times (-3) + (-2)$ is a true equation, but its remainder $-2$ breaks the condition $0 \le r < d$, so it is not the answer the theorem describes.

Check: $5 \times (-4) + 3 = -20 + 3 = -17$, $4 \times (-5) + 0 = -20$ and $7 \times (-1) + 6 = -1$, and each $r$ is between 0 and $d - 1$. Python agrees: `divmod(-17, 5)`, `divmod(-20, 4)` and `divmod(-1, 7)` give `(-4, 3)`, `(-5, 0)` and `(-1, 6)`.

</details>

## Where this shows up

- The next lesson, [rational number arithmetic](03-rational-number-arithmetic.md), uses the same sign rules for fractions and decimals, and [exponents and order of operations](04-exponents-and-order-of-operations.md) uses them for powers. Solving [one- and two-step equations](../03-expressions-equations-inequalities/03-one-and-two-step-equations.md) undoes an addition by adding the opposite to both sides.
- Computer hardware subtracts by adding the opposite, which is how two's complement<!-- link: ../../06-cs-math/01-number-representation/03-binary-arithmetic-and-twos-complement.md --> works. The division algorithm for negative $n$ in Practice problem 8 is the base of modular arithmetic in [divisibility and modular arithmetic](../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md).
- Every percent change starts with new minus old ([percent change and applications](../02-ratios-rates-percents/04-percent-change-and-applications.md)). In economics, net exports are exports minus imports, a negative number when a country runs a trade deficit (GDP and the circular flow<!-- link: ../../07-economics-math/01-measuring-the-economy/05-gdp-and-the-circular-flow.md -->).
