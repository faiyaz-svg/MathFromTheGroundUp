# Rational number arithmetic

After this lesson you can add, subtract, multiply and divide fractions and decimals that may be negative, tell from a fraction's denominator whether its decimal stops, and turn a repeating decimal back into a fraction.

Before this: [integer arithmetic and sign rules](02-integer-arithmetic-and-sign-rules.md), [adding and subtracting fractions](../../01-elementary/10-adding-and-subtracting-fractions.md), [multiplying and dividing fractions](../../01-elementary/11-multiplying-and-dividing-fractions.md) and [multiplying and dividing decimals](../../01-elementary/13-multiplying-and-dividing-decimals.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $-\frac{2}{3} + \frac{1}{4}$.
2. Work out $\left(-\frac{3}{5}\right) \div \left(-\frac{9}{10}\right)$.
3. Write $0.\overline{36}$ as a fraction in simplest form.

<details class="solution" markdown>
<summary>Answers</summary>

1. The answer is $-\frac{5}{12}$. Over the common denominator 12, the sum is $-\frac{8}{12} + \frac{3}{12} = \frac{-8 + 3}{12}$.
2. The answer is $\frac{2}{3}$. The same signs give a positive quotient, and $\frac{3}{5} \times \frac{10}{9} = \frac{30}{45} = \frac{2}{3}$.
3. The answer is $\frac{4}{11}$. With $x = 0.\overline{36}$, subtracting $x$ from $100x$ gives $99x = 36$, so $x = \frac{36}{99} = \frac{4}{11}$.

</details>

## The idea

Say you set a weekly food budget and track how far off you are. Going \$12.75 over budget one week is $-12.75$, and coming in \$4.50 under the next week is $4.50$. Over the two weeks you are at $-12.75 + 4.50 = -8.25$, which is \$8.25 over. The numbers have decimal parts, but the sign works exactly as it does for integers: the signs differ, so subtract the sizes, $12.75 - 4.50 = 8.25$, and keep the sign of the larger one.

That is most of this lesson in one rule: a fraction or decimal with a sign follows the fraction and decimal methods you already know for its size, and the sign rules from the last lesson for its sign. The numbers you get this way fill in the number line between the integers. For example, $-\frac{1}{2}$ is halfway between $-1$ and 0, and $-2.75$ is three quarters of the way from $-2$ to $-3$.

Two things are new. One is where a minus sign can go in a fraction. The other is what the decimals of these numbers look like: they either stop, as $-\frac{3}{8} = -0.375$ does, or repeat forever, as $\frac{4}{11} = 0.3636\ldots$ does. Every repeating decimal can be turned back into a fraction, with a short piece of algebra that also shows that $0.999\ldots$ is exactly 1.

## Definitions

A **rational number** is a number that can be written as $\frac{a}{b}$, where $a$ and $b$ are integers and $b \ne 0$. The set of rational numbers is written $\mathbb{Q}$, for "quotient".

In plain words, a rational number is a fraction of integers, and it can be positive, negative or zero. Every integer is rational, since $-7 = \frac{-7}{1}$. So is every terminating decimal, since $-0.45 = -\frac{45}{100} = -\frac{9}{20}$, and so is every repeating decimal, as this lesson shows. The words "can be written" matter: $\frac{0.5}{2}$ is not written as a fraction of integers, but it equals $\frac{1}{4}$, so it is rational.

### Where the minus sign goes

For integers $a$ and $b$ with $b \ne 0$,

$$
-\frac{a}{b} = \frac{-a}{b} = \frac{a}{-b} \qquad \text{and} \qquad \frac{-a}{-b} = \frac{a}{b}.
$$

The reason is that a fraction is a division, and division follows the sign rules. Both $(-a) \div b$ and $a \div (-b)$ divide two numbers of different signs (when $a$ and $b$ are positive), so each one is the opposite of $a \div b$. In $(-a) \div (-b)$ the signs are the same, so it equals $a \div b$. For example, $-\frac{3}{4}$, $\frac{-3}{4}$ and $\frac{3}{-4}$ all name the number $-0.75$.

All three ways of writing the sign are correct, but the simplest form of a rational number keeps its denominator positive: write $-\frac{3}{4}$ or $\frac{-3}{4}$, not $\frac{3}{-4}$. With that rule, each rational number has exactly one simplest form $\frac{a}{b}$, with $b > 0$ and $\gcd(\lvert a \rvert, b) = 1$, where $\gcd$ is the greatest common factor from [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md).

A negative mixed number is the opposite of the whole mixed number. So $-2\frac{1}{4}$ means $-\left(2 + \frac{1}{4}\right) = -\frac{9}{4}$, and the minus sign applies to the fraction part as well as to the 2.

### Terminating and repeating decimals

[Multiplying and dividing decimals](../../01-elementary/13-multiplying-and-dividing-decimals.md#fractions-as-decimals) proved two facts about the decimal of a fraction. First, it either terminates or repeats. Second, a fraction in simplest form terminates exactly when its denominator has no prime factors other than 2 and 5, because a terminating decimal is a fraction over a power of 10, and $10 = 2 \times 5$. A minus sign changes neither fact, since $-\frac{a}{b}$ has the same digits as $\frac{a}{b}$.

The rule also says how many decimal places a terminating decimal has. If the denominator is $2^m \times 5^n$, multiplying the numerator and the denominator by enough 2s or 5s turns the denominator into $10^k$, where $k$ is the larger of $m$ and $n$, so the decimal has $k$ places. For example, $40 = 2^3 \times 5$, so $\frac{3}{40}$ has 3 places: $\frac{3}{40} = \frac{75}{1000} = 0.075$.

## How to do it

### Arithmetic with signed fractions and decimals

1. Get each number into a form you can work with. Write a mixed number as an improper fraction, with the minus sign in front of the whole thing, and put every minus sign in the numerator or in front, so that every denominator is positive.
2. For multiplication and division, find the sign of the answer with the sign rules. Then work with the absolute values, using the methods for fractions or decimals.
3. For addition and subtraction, first rewrite each subtraction as adding the opposite. For fractions, write them over a common denominator with the signs in the numerators, and add the numerators as integers. For decimals, use the rules for adding integers on the sizes.
4. Simplify: cancel common factors, and keep the denominator positive.
5. Check the sign and the size, with decimals or with an estimate.

### Deciding whether a fraction's decimal terminates

1. Write the fraction in simplest form. The sign doesn't matter.
2. Factor the denominator into primes.
3. If the only primes are 2 and 5, the decimal terminates, and the number of decimal places is the larger exponent of 2 or 5. If another prime appears, the decimal repeats.
4. To write a terminating decimal, multiply the numerator and the denominator by 2s or 5s until the denominator is a power of 10.

### Turning a repeating decimal into a fraction

The steps use a letter for the number you are looking for, as in [variables and expressions](../03-expressions-equations-inequalities/01-variables-and-expressions.md). Here they are for $0.\overline{36}$.

1. Call the number $x$. Here $x = 0.363636\ldots$
2. Count the digits in the repeating block, and call the count $k$. The block is 36, so $k = 2$.
3. Multiply by $10^k$, which moves the decimal point one whole block to the right: $100x = 36.363636\ldots$
4. Subtract $x$. The digits after the point line up exactly and cancel, so $100x - x = 36.3636\ldots - 0.3636\ldots = 36$. Since $100x - x = 99x$, this says $99x = 36$.
5. Divide by the number in front of $x$, and simplify. If 99 copies of $x$ make 36, then $x = \frac{36}{99}$, and dividing both by 9 gives $x = \frac{4}{11}$.
6. Check by dividing: $4 \div 11 = 0.3636\ldots$

If some digits come before the repeating block, as in $0.1\overline{6} = 0.1666\ldots$, first multiply by a power of 10 that moves those digits in front of the point: $10x = 1.666\ldots$ Then do Step 3 to that number: $100x = 16.666\ldots$ Subtracting, $100x - 10x = 15$, so $90x = 15$ and $x = \frac{15}{90} = \frac{1}{6}$.

The method works because the decimal repeats. After a shift of exactly one block, the digits after the point are the same endless string as before, so the subtraction removes all of them at once. Step 5 is a one-step equation, the kind solved in [one- and two-step equations](../03-expressions-equations-inequalities/03-one-and-two-step-equations.md).

### Why 0.999 repeating equals 1

Apply the method to $x = 0.999\ldots$, whose block is one digit long. Then $10x = 9.999\ldots$, and subtracting gives $10x - x = 9$, so $9x = 9$ and $x = 1$. The two decimals $0.\overline{9}$ and $1$ name the same number, the way $\frac{1}{2}$ and $\frac{2}{4}$ do.

A second argument gives the same answer. Long division shows $\frac{1}{3} = 0.333\ldots$, and multiplying both sides by 3 gives $1 = 0.999\ldots$, since each digit 3 becomes a 9 with nothing to carry.

Both arguments take for granted that an infinite decimal can be multiplied by 10 by shifting it, and that two infinite decimals can be subtracted digit by digit. Both facts are true. The full proof treats $0.999\ldots$ as the infinite sum $\frac{9}{10} + \frac{9}{100} + \frac{9}{1000} + \cdots$, which is done in infinite series basics<!-- link: ../../05-university-core/05-sequences-and-series/02-infinite-series-basics.md -->. The FAQ below gives an argument that uses only distance.

One result is that every terminating decimal has a second decimal form, ending in repeating 9s: $0.5 = 0.4\overline{9}$, and $2.37 = 2.36\overline{9}$. This book always writes the terminating one.

### Not every number is rational

The decimal of a fraction always stops or repeats. So a decimal that does neither is not a fraction of integers. You can write one down: $0.101001000100001\ldots$, where each run of zeros is one longer than the one before it. It never settles into a block that repeats, so it is not rational. Two famous examples are $\sqrt{2} = 1.41421\ldots$ and $\pi = 3.14159\ldots$, whose digits also never stop or repeat. Numbers like these are called irrational, and they are the subject of roots, irrational numbers and types of numbers<!-- link: ../04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md -->. Showing that a particular number such as $\sqrt{2}$ is irrational takes a proof by contradiction<!-- link: ../../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md -->.

## Worked examples

<div class="example" markdown>

### Example 1: subtracting a negative fraction

Work out $-\frac{5}{6} - \left(-\frac{3}{4}\right)$.

Step 1: both numbers are already fractions with positive denominators, and the minus signs are in front.

Step 3: rewrite the subtraction as adding the opposite. The opposite of $-\frac{3}{4}$ is $\frac{3}{4}$, so the calculation becomes

$$
-\frac{5}{6} + \frac{3}{4}.
$$

The least common denominator of 6 and 4 is 12, so write both fractions over 12, with the signs in the numerators:

$$
-\frac{10}{12} + \frac{9}{12} = \frac{-10 + 9}{12} = \frac{-1}{12}.
$$

The numerators are added as integers: the signs differ, $10 - 9 = 1$, and $-10$ has the larger absolute value, so $-10 + 9 = -1$.

<div class="warning" markdown>

Watch out at Step 3: the minus sign belongs to the 10 only. Writing $-\frac{10}{12} + \frac{9}{12}$ as $-\frac{10 + 9}{12} = -\frac{19}{12}$ makes the 9 negative too. Moving the sign into the numerator first, as $\frac{-10}{12}$, makes it clear which number it belongs to.

</div>

Step 4: $-\frac{1}{12}$ is in simplest form, with a positive denominator.

Step 5: check with decimals. The fraction $-\frac{5}{6}$ is about $-0.833$, and $-\frac{3}{4} = -0.75$, so the calculation is about $-0.833 + 0.75 = -0.083$, which is $-\frac{1}{12}$ to three places. The sign makes sense too: $-\frac{5}{6}$ is further left than $-\frac{3}{4}$, and a smaller number minus a bigger one is negative.

</div>

<div class="example" markdown>

### Example 2: negative mixed numbers

Work out (a) $-2\frac{1}{4} \times \left(-\frac{2}{3}\right)$ and (b) $\frac{5}{6} \div \left(-1\frac{1}{4}\right)$.

(a) Step 1: $-2\frac{1}{4} = -\frac{9}{4}$. Step 2: both factors are negative, so the product is positive. Multiply the absolute values, cancelling first: the 9 and the 3 share a factor 3, and the 2 and the 4 share a factor 2.

$$
\frac{9}{4} \times \frac{2}{3} = \frac{3 \times 1}{2 \times 1} = \frac{3}{2}.
$$

The answer is $\frac{3}{2}$, or $1\frac{1}{2}$. Check: $2.25 \times 0.666\ldots = 1.5$.

(b) Step 1: $-1\frac{1}{4} = -\frac{5}{4}$. Step 2: the signs differ, so the quotient is negative. Multiply by the reciprocal: $\frac{5}{6} \times \frac{4}{5} = \frac{20}{30} = \frac{2}{3}$. The answer is $-\frac{2}{3}$. Check by multiplying back: $\left(-\frac{2}{3}\right) \times \left(-\frac{5}{4}\right) = \frac{10}{12} = \frac{5}{6}$.

<div class="warning" markdown>

Watch out: $-2\frac{1}{4}$ is not $-2 + \frac{1}{4}$. That sum is $-1\frac{3}{4}$, a different number. The mixed number $2\frac{1}{4}$ means $2 + \frac{1}{4}$, and the minus sign in front takes the opposite of all of it: $-2\frac{1}{4} = -2 - \frac{1}{4}$.

</div>

</div>

<div class="example" markdown>

### Example 3: which decimals terminate

Without dividing, decide which of $-\frac{13}{80}$, $\frac{7}{30}$ and $\frac{21}{-56}$ terminate, and write each as a decimal.

- The fraction $-\frac{13}{80}$ is in simplest form, since 13 is prime and doesn't divide 80. Factoring gives $80 = 2^4 \times 5$, so the decimal terminates after 4 places. Multiplying by $5^3 = 125$ gives $-\frac{13 \times 125}{80 \times 125} = -\frac{1625}{10000} = -0.1625$.
- The fraction $\frac{7}{30}$ is in simplest form, and $30 = 2 \times 3 \times 5$ has the prime 3, so the decimal repeats. Dividing, $7 \div 30 = 0.2333\ldots = 0.2\overline{3}$.
- Move the sign first: $\frac{21}{-56} = -\frac{21}{56}$. The denominator $56 = 2^3 \times 7$ has a 7, but the fraction is not in simplest form yet. Cancelling 7 gives $-\frac{3}{8}$, and $8 = 2^3$, so it terminates after 3 places: $-\frac{3}{8} = -\frac{375}{1000} = -0.375$.

Check: $0.1625 \times 80 = 13$ and $0.375 \times 8 = 3$. For the repeating one, $0.2333 \times 30 = 6.999$, just short of 7, because the 3s were cut off.

</div>

<div class="example" markdown>

### Example 4: a repeating decimal with a lead-in digit (finish it yourself)

Write $1.2\overline{7} = 1.2777\ldots$ as a fraction.

Call the number $x$. One digit, the 2, comes before the repeating block, so first multiply by 10: $10x = 12.777\ldots$ The block is one digit long, so multiply by 10 once more: $100x = 127.777\ldots$

Now subtract $10x$ from $100x$, solve for $x$, simplify, and check.

<details class="solution" markdown>
<summary>Finish</summary>

Step 4: $100x - 10x = 127.777\ldots - 12.777\ldots = 115$, so $90x = 115$. Step 5: $x = \frac{115}{90}$, and dividing both by 5 gives $x = \frac{23}{18}$.

Check: $18 = 2 \times 3^2$ has a 3, so the decimal should repeat, and it does. Dividing, 18 goes into 23 once with remainder 5, into 50 twice with remainder 14, and into 140 seven times with remainder 14 again, so $\frac{23}{18} = 1.2777\ldots$

</details>

</div>

## Edge cases and common mistakes

The two mistakes in the examples, letting a minus sign spread to other numerators and misreading a negative mixed number, are flagged where they happen. Here are the others.

<div class="warning" markdown>

Watch out: a rounded repeating decimal is a different number. The decimal $0.36$ is $\frac{36}{100} = \frac{9}{25}$, while $0.\overline{36}$ is $\frac{4}{11}$. They differ by $\frac{4}{11} - \frac{9}{25} = \frac{100 - 99}{275} = \frac{1}{275}$. Only the bar (or the dots) says that the digits go on forever.

</div>

<div class="warning" markdown>

Watch out: shift by exactly one block. For $x = 0.\overline{36}$, multiplying by 10 instead of 100 gives $10x = 3.6363\ldots$, and $10x - x = 3.2727\ldots$ still has an endless tail. The power of 10 must have as many zeros as the block has digits, so that the tails line up.

</div>

<div class="warning" markdown>

Watch out: count all the minus signs in a fraction. Two of them cancel, so $\frac{-6}{-8} = \frac{6}{8} = \frac{3}{4}$ is positive. Three leave a negative number: $-\frac{-3}{-4} = -\frac{3}{4}$. Each minus sign is a factor of $-1$, so the counting rule for products applies.

</div>

The test for terminating decimals needs simplest form first, as Example 3 showed with $\frac{21}{56}$. The numerator and the sign play no part in the test, only the denominator after cancelling.

Zero is rational, since $0 = \frac{0}{1}$, and $\frac{0}{b} = 0$ for every $b \ne 0$. An expression with denominator 0, such as $\frac{5}{0}$, is not a number at all, so it is not rational either.

Comparing negative fractions uses the rule from the first lesson of the chapter: compare the absolute values, then reverse. Since $\frac{2}{3} < \frac{3}{4}$, the negatives are the other way round, $-\frac{2}{3} > -\frac{3}{4}$.

## Tricks and shortcuts

A decimal that repeats from the first place after the point is its block over the same number of 9s:

$$
0.\overline{d_1 d_2 \ldots d_k} = \frac{d_1 d_2 \ldots d_k}{99\ldots9}, \qquad \text{with } k \text{ nines}.
$$

Here $d_1 d_2 \ldots d_k$ means the block read as a whole number, not a product. This is Steps 3 to 5 done at once, since $10^k x - x = (10^k - 1)x$, and $10^k - 1$ is $k$ nines. So $0.\overline{7} = \frac{7}{9}$, $0.\overline{36} = \frac{36}{99}$ and $0.\overline{142857} = \frac{142857}{999999} = \frac{1}{7}$.

The elevenths follow from the nines rule. Since $\frac{n}{11} = \frac{9n}{99}$, the block of $\frac{n}{11}$ is $9n$ written with two digits: $\frac{1}{11} = 0.\overline{09}$, $\frac{4}{11} = 0.\overline{36}$ and $\frac{7}{11} = 0.\overline{63}$.

Decide the sign before you do the arithmetic, then work with positive numbers only. It is one fewer thing to track through a long calculation, and the sign rules make the decision quick.

To check an answer, convert the numbers to decimals with a calculator and compare. A wrong sign or a wrong denominator almost always shows up in the first decimal place.

## In code

Python's `fractions` module does exact arithmetic with rational numbers. It keeps every fraction in simplest form with a positive denominator, the same convention as this lesson.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction

print(Fraction(3, -4), Fraction(-6, -8))         # -3/4 3/4
print(Fraction(-5, 6) - Fraction(-3, 4))         # -1/12
print(Fraction(-9, 4) * Fraction(-2, 3))         # 3/2
print(Fraction(36, 99), float(Fraction(4, 11)))  # 4/11 0.36363636363636365
print(Fraction("0.1"), Fraction(0.1))            # 1/10 3602879701896397/36028797018963968
```

The last line shows why floats are inexact. `Fraction("0.1")` reads the text 0.1 exactly, but `Fraction(0.1)` converts the float 0.1, which is stored as a fraction whose denominator is $2^{55} = 36{,}028{,}797{,}018{,}963{,}968$. In binary, the terminating rule allows only the prime 2 in the denominator, and $\frac{1}{10}$ has a 5, so the computer stores the nearest fraction it can. Floating point basics<!-- link: ../../06-cs-math/01-number-representation/04-floating-point-basics.md --> explains the format.

</details>

## FAQ

### Is every integer a rational number?

Yes. Every integer $n$ equals $\frac{n}{1}$, which is a fraction of integers. So each set of numbers in this chapter sits inside the next: every natural number is an integer, and every integer is rational. Zero is in all three.

### Isn't 0.999... a tiny bit less than 1?

No, and the idea of distance shows why. If the two numbers were different, the distance $1 - 0.999\ldots$ would be some positive number. But $0.9$ is $0.1$ below 1, $0.99$ is $0.01$ below 1, $0.999$ is $0.001$ below 1, and $0.999\ldots$ is at least as big as each of these. So its distance from 1 is at most $0.1$, at most $0.01$, at most $0.001$, and so on: at most $10^{-n}$ for every $n$. Every positive number is bigger than some $10^{-n}$ (a positive number such as $0.00003$ is bigger than $10^{-5}$), so the only distance that fits is 0. A distance of 0 means the two numbers are the same.

### Is there a next fraction after 0?

No. Half of a positive fraction is a smaller positive fraction, so there is no smallest one. More generally, between two different rational numbers there is always another one, their average, which Practice problem 7 proves. Even so, the rational numbers don't fill the number line: $\sqrt{2}$ is a point on the line that no fraction names.

## Practice

### Warm-up

1\. Show that each number is rational by writing it as $\frac{a}{b}$ with integers $a$ and $b$: (a) $-7$, (b) $0.45$, (c) $-1\frac{2}{3}$, (d) $0.\overline{5}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $-7 = \frac{-7}{1}$.
- (b) $0.45 = \frac{45}{100} = \frac{9}{20}$.
- (c) $-1\frac{2}{3} = -\left(1 + \frac{2}{3}\right) = -\frac{5}{3}$, which is $\frac{-5}{3}$.
- (d) With $x = 0.555\ldots$, the block has one digit, so $10x = 5.555\ldots$ and $10x - x = 5$. Then $9x = 5$ and $x = \frac{5}{9}$.

Check: $9 \div 20 = 0.45$, $-5 \div 3 = -1.666\ldots$ and $5 \div 9 = 0.555\ldots$

</details>

2\. Work out (a) $-\frac{3}{8} + \frac{5}{8}$, (b) $\frac{1}{6} - \frac{3}{4}$, (c) $-\frac{2}{5} \times \frac{15}{4}$ and (d) $-\frac{7}{10} \div \left(-\frac{14}{5}\right)$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The denominators match: $\frac{-3 + 5}{8} = \frac{2}{8} = \frac{1}{4}$.
- (b) Over 12: $\frac{2}{12} - \frac{9}{12} = \frac{2 - 9}{12} = -\frac{7}{12}$.
- (c) Different signs, so negative. Cancel the 5 with the 15 and the 2 with the 4: $\frac{1 \times 3}{1 \times 2} = \frac{3}{2}$, so the answer is $-\frac{3}{2}$.
- (d) The same signs, so positive: $\frac{7}{10} \times \frac{5}{14} = \frac{35}{140} = \frac{1}{4}$.

Check with decimals: (b) $0.1667 - 0.75 = -0.5833$, which is $-\frac{7}{12}$ to four places; (c) $-0.4 \times 3.75 = -1.5$; (d) $-0.7 \div (-2.8) = 0.25$.

</details>

3\. Work out (a) $-3.6 + 1.25$, (b) $-0.4 \times (-0.15)$, (c) $-7.2 \div 0.9$ and (d) $2.5 - 4.75$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The signs differ: $3.6 - 1.25 = 2.35$, with the sign of $-3.6$, so $-2.35$.
- (b) The same signs, so positive: $4 \times 15 = 60$ with 3 decimal places, so $0.060 = 0.06$.
- (c) Different signs, so negative: $7.2 \div 0.9 = 72 \div 9 = 8$, so $-8$.
- (d) Add the opposite: $2.5 + (-4.75)$. The signs differ, $4.75 - 2.5 = 2.25$, so $-2.25$.

Check: $-2.35 - 1.25 = -3.6$, $0.06 \div (-0.15) = -0.4$, $-8 \times 0.9 = -7.2$ and $-2.25 + 4.75 = 2.5$.

</details>

### Standard

4\. Without dividing, decide which of these fractions terminate, then write each as a decimal: $-\frac{9}{64}$, $\frac{5}{36}$, $\frac{14}{-35}$, $\frac{4}{15}$.

<details class="solution" markdown>
<summary>Solution</summary>

- The fraction $-\frac{9}{64}$ is in simplest form, and $64 = 2^6$, so it terminates after 6 places. Multiplying by $5^6 = 15625$ gives $-\frac{140625}{1000000} = -0.140625$.
- The fraction $\frac{5}{36}$ is in simplest form, and $36 = 2^2 \times 3^2$ has a 3, so it repeats. Dividing, $\frac{5}{36} = 0.13888\ldots = 0.13\overline{8}$.
- First $\frac{14}{-35} = -\frac{14}{35} = -\frac{2}{5}$ after cancelling 7. The denominator 5 is allowed, so it terminates: $-0.4$.
- The fraction $\frac{4}{15}$ is in simplest form, and $15 = 3 \times 5$ has a 3, so it repeats: $\frac{4}{15} = 0.2666\ldots = 0.2\overline{6}$.

Check: $0.140625 \times 64 = 9$ and $0.4 \times 35 = 14$. For the repeating ones, $0.1389 \times 36 = 5.0004$ and $0.2667 \times 15 = 4.0005$, both close to the numerators.

</details>

5\. Write each decimal as a fraction in simplest form: (a) $0.\overline{8}$, (b) $0.\overline{27}$, (c) $0.\overline{123}$, (d) $-0.8\overline{3}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) One repeating digit, so one 9: $\frac{8}{9}$.
- (b) Two repeating digits: $\frac{27}{99} = \frac{3}{11}$.
- (c) Three repeating digits: $\frac{123}{999}$. Both are divisible by 3, which gives $\frac{41}{333}$, and $333 = 3^2 \times 37$ shares no factor with 41.
- (d) Work with $x = 0.8333\ldots$ and put the sign back at the end. One digit comes before the block, so $10x = 8.333\ldots$ and $100x = 83.333\ldots$ Then $100x - 10x = 75$, so $90x = 75$ and $x = \frac{75}{90} = \frac{5}{6}$. The answer is $-\frac{5}{6}$.

Check: $8 \div 9 = 0.888\ldots$, $3 \div 11 = 0.2727\ldots$, $41 \div 333 = 0.123123\ldots$ and $-5 \div 6 = -0.8333\ldots$

</details>

6\. A small company's profits for the four quarters of a year, in millions of dollars, were $-2.4$, $1.75$, $-0.6$ and $3.05$. (a) What was the total profit for the year? (b) What was the average profit per quarter? (c) What was the change in profit from the first quarter to the second?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Collect the positive and negative quarters: $1.75 + 3.05 = 4.8$ and $-2.4 + (-0.6) = -3$. Then $4.8 + (-3) = 1.8$, so the total was 1.8 million dollars.

(b) Divide by 4: $1.8 \div 4 = 0.45$, so 0.45 million dollars, or \$450,000, per quarter.

(c) New minus old: $1.75 - (-2.4) = 1.75 + 2.4 = 4.15$. Profit rose by 4.15 million dollars.

Check: adding in order, $-2.4 + 1.75 = -0.65$, then $-0.65 - 0.6 = -1.25$, then $-1.25 + 3.05 = 1.8$. For (c), $-2.4 + 4.15 = 1.75$.

</details>

### Challenge

7\. Prove that between two different rational numbers there is always another one: if $p$ and $q$ are rational and $p < q$, then $m = \frac{p + q}{2}$ is rational and $p < m < q$. Then find a rational number between $-\frac{1}{3}$ and $-\frac{1}{4}$.

<details class="solution" markdown>
<summary>Solution</summary>

We know the definition of a rational number, and from the last lesson that $a - b > 0$ means $a > b$. We want two things: that $m$ can be written as a fraction of integers, and that it lies between $p$ and $q$. The plan is to write $p$ and $q$ as fractions and add them, then show that $m - p$ and $q - m$ are positive.

*Proof.* Since $p$ and $q$ are rational, $p = \frac{a}{b}$ and $q = \frac{c}{d}$ for some integers $a$, $b$, $c$ and $d$ with $b \ne 0$ and $d \ne 0$. Adding over the common denominator $bd$ and halving,

$$
m = \frac{1}{2} \left( \frac{a}{b} + \frac{c}{d} \right) = \frac{1}{2} \times \frac{ad + bc}{bd} = \frac{ad + bc}{2bd}.
$$

The numerator $ad + bc$ is an integer, because sums and products of integers are integers, and so is the denominator $2bd$. The denominator is not 0, since none of 2, $b$ and $d$ is 0. So $m$ is rational.

For the order, $m - p = \frac{p + q}{2} - \frac{2p}{2} = \frac{q - p}{2}$, and in the same way $q - m = \frac{2q}{2} - \frac{p + q}{2} = \frac{q - p}{2}$. Since $p < q$, the difference $q - p$ is positive, so half of it is positive too. So $m - p > 0$ and $q - m > 0$, which say that $p < m$ and $m < q$.

For the numbers: $m = \frac{1}{2}\left(-\frac{1}{3} + \left(-\frac{1}{4}\right)\right) = \frac{1}{2} \times \left(-\frac{7}{12}\right) = -\frac{7}{24}$.

Look back: the same step can be used again on $p$ and $m$, then again, so there are as many rational numbers between $p$ and $q$ as you like. Check the example: $-\frac{1}{3} = -\frac{8}{24}$ and $-\frac{1}{4} = -\frac{6}{24}$, and $-\frac{8}{24} < -\frac{7}{24} < -\frac{6}{24}$.

</details>

8\. This one reviews least common multiples from [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md). Work out $-\frac{5}{12} + \frac{7}{18} - \frac{1}{8}$, finding the least common denominator from prime factorizations. Then decide whether the answer is a terminating decimal, and write it as a decimal.

<details class="solution" markdown>
<summary>Solution</summary>

The denominators factor as $12 = 2^2 \times 3$, $18 = 2 \times 3^2$ and $8 = 2^3$. The least common multiple takes the highest power of each prime: $2^3 \times 3^2 = 72$. Over 72 the fractions are $-\frac{30}{72}$, $\frac{28}{72}$ and $\frac{9}{72}$, so

$$
-\frac{30}{72} + \frac{28}{72} - \frac{9}{72} = \frac{-30 + 28 - 9}{72} = \frac{-11}{72} = -\frac{11}{72}.
$$

The numerator 11 is prime and doesn't divide 72, so this is in simplest form. The denominator has the prime 3, so the decimal repeats: $11 \div 72 = 0.152777\ldots$, so the answer is $-0.152\overline{7}$.

Check with decimals: $-0.41667 + 0.38889 - 0.125 = -0.15278$, which matches.

</details>

## Where this shows up

- The next lesson, [exponents and order of operations](04-exponents-and-order-of-operations.md), raises fractions and negative numbers to powers. [Percents](../02-ratios-rates-percents/03-percents.md) and [ratios and unit rates](../02-ratios-rates-percents/01-ratios-and-unit-rates.md) are rational arithmetic with names attached, and [multi-step equations](../03-expressions-equations-inequalities/04-multi-step-equations.md) often have fractions as answers.
- The rational numbers can be listed one after another even though there is no next one after each, which is the surprise in cardinality and countability<!-- link: ../../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md -->. Every float is a rational number with a power of 2 as its denominator, as the In code box shows.
- In finance and economics, rates are decimals that can be negative: a return of $-2.5\%$ is $-0.025$, and a real return after inflation can be negative even when the account grows (inflation and real returns<!-- link: ../../08-financial-math/02-interest-and-growth/06-inflation-and-real-returns.md -->).
