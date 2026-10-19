# Fractions and equivalent fractions

After this lesson you can read a fraction three ways, write it as an equivalent fraction or in simplest form, compare two fractions, and switch between mixed numbers and improper fractions.

Before this: [long division](07-long-division.md) and [factors, multiples and primes](08-factors-multiples-and-primes.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write $\frac{84}{126}$ in simplest form.
2. Which is bigger, $\frac{5}{8}$ or $\frac{7}{11}$?
3. Write $\frac{47}{6}$ as a mixed number, and $3\frac{2}{5}$ as an improper fraction.

<details class="solution" markdown>
<summary>Answers</summary>

1. $\frac{2}{3}$. The GCF of 84 and 126 is 42, and $84 \div 42 = 2$ while $126 \div 42 = 3$.
2. $\frac{7}{11}$. Cross-multiply: $5 \times 11 = 55$ and $7 \times 8 = 56$, and 56 is bigger.
3. Since $47 = 7 \times 6 + 5$, the fraction $\frac{47}{6}$ is $7\frac{5}{6}$. In the other direction, $3\frac{2}{5} = \frac{3 \times 5 + 2}{5} = \frac{17}{5}$.

</details>

## The idea

Cut a pizza into 8 equal slices and eat 3 of them. You have eaten three eighths of the pizza, written $\frac{3}{8}$. The bottom number says what size the pieces are (eighths), and the top number counts how many of them you have (3).

Now share 3 pizzas equally among 8 people. Cut each pizza into 8 slices and give each person one slice from each pizza. Everyone gets 3 slices, each an eighth of a pizza, so everyone gets $\frac{3}{8}$ of a pizza again. That makes $\frac{3}{8}$ the answer to $3 \div 8$, and [long division](07-long-division.md) gives the same number as a decimal: $3 \div 8 = 0.375$.

A fraction is also a point on the number line. Cut the stretch from 0 to 1 into 8 equal pieces, and $\frac{3}{8}$ is the point at the end of the third piece. If you cut the same stretch into quarters, each quarter mark lands on every second eighth mark:

```text
0        1/4       2/4       3/4        1
|----+----|----+----|----+----|----+----|
0   1/8  2/8  3/8  4/8  5/8  6/8  7/8  8/8
```

So $\frac{2}{8}$ and $\frac{1}{4}$ are the same point, and so are $\frac{6}{8}$ and $\frac{3}{4}$. Fractions that look different but name the same point are equivalent, and most of this lesson is about making them and spotting them.

## Definitions

Let $a$ and $b$ be whole numbers with $b \ne 0$, where $\ne$ means "is not equal to". The **fraction** $\frac{a}{b}$ is the number $a \div b$. Its **numerator** is $a$, the number on top, and its **denominator** is $b$, the number on the bottom.

In plain words, the denominator says how many equal parts the whole is cut into, and the numerator says how many of those parts you have. In $\frac{3}{8}$ the whole is cut into 8 parts and you have 3 of them. The same fraction can be written $3/8$.

A **unit fraction** is a fraction with numerator 1, such as $\frac{1}{8}$, which is one part of the whole. Every fraction counts unit fractions. For example, $\frac{3}{8}$ is three copies of $\frac{1}{8}$:

$$
\frac{3}{8} = \frac{1}{8} + \frac{1}{8} + \frac{1}{8}.
$$

A **proper fraction** has a numerator smaller than its denominator, so it is less than 1, as $\frac{3}{8}$ is. An **improper fraction** has a numerator at least as big as its denominator, so it is 1 or more, as $\frac{11}{4}$ and $\frac{4}{4}$ are. A **mixed number** is a whole number followed by a proper fraction, and it means their sum: $2\frac{3}{4} = 2 + \frac{3}{4}$, which is $\frac{11}{4}$.

Two fractions are **equivalent** when they are equal as numbers, so they mark the same point on the number line. For example, $\frac{1}{4}$, $\frac{2}{8}$ and $\frac{25}{100}$ are equivalent, since each one equals 0.25. A test that needs no decimals is in [Comparing two fractions](#comparing-two-fractions): $\frac{a}{b} = \frac{c}{d}$ exactly when $a \times d = c \times b$.

A fraction is in **simplest form**, or lowest terms, when its numerator and denominator have no common factor except 1, that is, when $\gcd(a, b) = 1$. So $\frac{3}{4}$ is in simplest form, while $\frac{6}{8}$ is not, because 6 and 8 share the factor 2.

In this lesson numerators and denominators are whole numbers. Negative fractions come in [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md).

## How to do it

### Making equivalent fractions

Multiplying the numerator and the denominator by the same nonzero number gives an equivalent fraction. For every whole number $c \ne 0$,

$$
\frac{a}{b} = \frac{a \times c}{b \times c}.
$$

Here is why. Multiplying the denominator by $c$ cuts each piece into $c$ smaller pieces, so the whole now has $c$ times as many pieces, each $c$ times smaller. Multiplying the numerator by $c$ counts the same amount in the smaller pieces. Going from $\frac{3}{4}$ to $\frac{6}{8}$ cuts each quarter in half, and three quarters are six eighths. The division view agrees, since $6 \div 8 = 0.75 = 3 \div 4$.

Read from right to left, the same equation says that dividing the numerator and the denominator by a common factor also gives an equivalent fraction. The number $c$ can't be 0, because $\frac{a \times 0}{b \times 0} = \frac{0}{0}$, and that is not a number (see [Edge cases](#edge-cases-and-common-mistakes)).

### Writing a fraction in simplest form

1. Find the GCF of the numerator and the denominator, by listing factors or from prime factorizations, as in [factors, multiples and primes](08-factors-multiples-and-primes.md).
2. Divide the numerator and the denominator by the GCF.
3. Check that the new numerator and denominator have no common factor except 1.

If the GCF is hard to see, divide by a common factor you can spot, such as 2, 3 or 5, and repeat until no common factor is left. That takes more steps and reaches the same answer.

### Comparing two fractions

The symbol $>$ means "is greater than" and $<$ means "is less than".

1. If the denominators are equal, compare the numerators: $\frac{5}{9} > \frac{4}{9}$. If the numerators are equal, the fraction with the smaller denominator is bigger, because its pieces are bigger: $\frac{3}{5} > \frac{3}{7}$.
2. Otherwise, try a benchmark: compare each fraction with $\frac{1}{2}$ or with 1. A fraction $\frac{a}{b}$ is more than $\frac{1}{2}$ exactly when $2 \times a > b$, that is, when the numerator is more than half the denominator. If one fraction is below $\frac{1}{2}$ and the other is above, you are done.
3. Otherwise, rewrite both fractions over a common denominator, a number both denominators divide, such as their LCM. Then compare the numerators as in step 1.
4. Or cross-multiply. To compare $\frac{a}{b}$ with $\frac{c}{d}$, compare $a \times d$ with $c \times b$. The fraction whose numerator is in the bigger product is the bigger fraction, and equal products mean equivalent fractions.

Cross-multiplying is step 3 with $b \times d$ as the common denominator. Rewriting both fractions over it gives

$$
\frac{a}{b} = \frac{a \times d}{b \times d} \quad \text{and} \quad \frac{c}{d} = \frac{c \times b}{d \times b}.
$$

The denominators $b \times d$ and $d \times b$ are equal, so the fractions compare the same way as their numerators, $a \times d$ and $c \times b$. Cross-multiplying finds those two numerators and skips writing the denominator.

### Mixed numbers and improper fractions

To change an improper fraction into a mixed number:

1. Divide the numerator by the denominator.
2. The quotient is the whole-number part, and the remainder is the numerator of the fraction part. The denominator stays the same.

This is the division algorithm from [long division](07-long-division.md). Since $47 = 7 \times 6 + 5$, 47 sixths make 7 wholes (42 sixths) with 5 sixths left over, so $\frac{47}{6} = 7\frac{5}{6}$.

To change a mixed number into an improper fraction:

1. Multiply the whole number by the denominator, and add the numerator.
2. Write the result over the same denominator.

For $3\frac{2}{5}$: each whole is 5 fifths, so 3 wholes are 15 fifths, and 2 more fifths make $\frac{17}{5}$.

## Worked examples

<div class="example" markdown>

### Example 1: simplest form using the GCF

Step 1: find the GCF from prime factorizations. The ladder method gives

$$
180 = 2^2 \times 3^2 \times 5 \quad \text{and} \quad 252 = 2^2 \times 3^2 \times 7.
$$

The shared primes are 2 and 3, each with exponent 2 in both, so the GCF is $2^2 \times 3^2 = 36$.

Step 2: divide the numerator and the denominator by 36. Since $180 \div 36 = 5$ and $252 \div 36 = 7$,

$$
\frac{180}{252} = \frac{5}{7}.
$$

Step 3: the numbers 5 and 7 are different primes, so their only common factor is 1, and $\frac{5}{7}$ is in simplest form.

Check by cross-multiplying: $5 \times 252 = 1{,}260$ and $7 \times 180 = 1{,}260$. The products are equal, so the two fractions are equivalent.

Without the GCF, you can divide by 2 twice and then by 3 twice:

$$
\frac{180}{252} = \frac{90}{126} = \frac{45}{63} = \frac{15}{21} = \frac{5}{7}.
$$

That takes four steps instead of one, with the same answer.

<div class="warning" markdown>

Watch out: the fraction $\frac{15}{21}$ looks finished, but 3 divides both 15 and 21. Step 3 is there to catch it. Before you stop, test the numerator and the denominator for a common factor once more.

</div>

</div>

<div class="example" markdown>

### Example 2: comparing two fractions below one half

Compare $\frac{5}{12}$ and $\frac{4}{9}$. Step 1: the numerators differ, and so do the denominators. Step 2: both fractions are below $\frac{1}{2}$, since $2 \times 5 = 10$ is less than 12 and $2 \times 4 = 8$ is less than 9, so the benchmark doesn't settle it.

Step 3: the LCM of 12 and 9 is 36. Rewrite both fractions over 36:

$$
\frac{5}{12} = \frac{15}{36} \quad \text{and} \quad \frac{4}{9} = \frac{16}{36}.
$$

Since 16 is more than 15, the fraction $\frac{4}{9}$ is bigger. Step 4 agrees: $5 \times 9 = 45$ and $4 \times 12 = 48$, and the bigger product, 48, contains the numerator of $\frac{4}{9}$.

Check with long division: $5 \div 12 = 0.41666\ldots$ and $4 \div 9 = 0.444\ldots$, so $\frac{5}{12} < \frac{4}{9}$.

</div>

<div class="example" markdown>

### Example 3: ordering four fractions with benchmarks

Put $\frac{7}{12}$, $\frac{3}{8}$, $\frac{9}{10}$ and $\frac{2}{5}$ in order from smallest to largest.

Sort them by the benchmark $\frac{1}{2}$ first. Since $2 \times 3 = 6$ is less than 8 and $2 \times 2 = 4$ is less than 5, both $\frac{3}{8}$ and $\frac{2}{5}$ are below $\frac{1}{2}$. Since $2 \times 7 = 14$ is more than 12 and $2 \times 9 = 18$ is more than 10, both $\frac{7}{12}$ and $\frac{9}{10}$ are above it.

Below $\frac{1}{2}$, cross-multiply: $3 \times 5 = 15$ and $2 \times 8 = 16$, so $\frac{3}{8} < \frac{2}{5}$. Above $\frac{1}{2}$, compare the gaps to 1: $\frac{9}{10}$ is $\frac{1}{10}$ short of 1, while $\frac{7}{12}$ is $\frac{5}{12}$ short, a much bigger gap. So $\frac{7}{12} < \frac{9}{10}$, and the order is

$$
\frac{3}{8} < \frac{2}{5} < \frac{7}{12} < \frac{9}{10}.
$$

Check with decimals: 0.375, 0.4, 0.583 and 0.9, in that order.

</div>

<div class="example" markdown>

### Example 4: mixed numbers and a whole number

Write $\frac{23}{4}$ and $\frac{24}{4}$ as mixed numbers, and $5\frac{3}{8}$ as an improper fraction.

Since $23 = 5 \times 4 + 3$, the fraction $\frac{23}{4}$ is $5\frac{3}{4}$. Since $24 = 6 \times 4 + 0$, the remainder is 0, so $\frac{24}{4}$ is the whole number 6 with no fraction part. For the last one, $5 \times 8 + 3 = 43$, so $5\frac{3}{8} = \frac{43}{8}$.

Check: $5\frac{3}{4} = \frac{5 \times 4 + 3}{4} = \frac{23}{4}$, and $6 \times 4 = 24$. Converting $\frac{43}{8}$ back gives $43 = 5 \times 8 + 3$, which is $5\frac{3}{8}$ again.

Simplify an improper fraction before converting it, or simplify the fraction part afterwards; both give the same mixed number. For $\frac{46}{12}$, simplifying first gives $\frac{23}{6} = 3\frac{5}{6}$, and converting first gives $3\frac{10}{12}$, which is $3\frac{5}{6}$ after simplifying.

</div>

## Edge cases and common mistakes

Stopping before a fraction is in simplest form is flagged in Example 1, at the step where it happens. Here are the other cases.

<div class="warning" markdown>

Watch out: the denominator can't be 0. The fraction $\frac{5}{0}$ would be $5 \div 0$, a number $q$ with $q \times 0 = 5$, and there is none, because every number times 0 is 0. The fraction $\frac{0}{0}$ fails the other way: every number $q$ has $q \times 0 = 0$, so no single answer exists. A zero numerator is fine, though: $\frac{0}{5} = 0$, since 0 parts of anything is nothing.

</div>

<div class="warning" markdown>

Watch out: adding the same number to the numerator and the denominator does not give an equivalent fraction. Adding 1 to both parts of $\frac{1}{2}$ gives $\frac{2}{3}$, which is a different point, since $1 \times 3 = 3$ and $2 \times 2 = 4$ are not equal. Only multiplying or dividing both parts by the same nonzero number keeps the value.

</div>

<div class="warning" markdown>

Watch out: a bigger denominator means smaller pieces, not a bigger fraction. Although 8 is more than 4, $\frac{1}{8}$ is half of $\frac{1}{4}$. Comparing denominators alone works only when the numerators are equal, and then it works backwards.

</div>

<div class="warning" markdown>

Watch out: a mixed number is a sum, not a product. The mixed number $2\frac{3}{4}$ means $2 + \frac{3}{4} = \frac{11}{4}$, not $2 \times \frac{3}{4} = \frac{6}{4}$. In algebra, writing two things side by side does mean multiplying ($2x$ is $2 \times x$), so from middle school on, answers are usually written as improper fractions such as $\frac{11}{4}$.

</div>

A few fractions are worth knowing on sight. A denominator of 1 gives back the numerator, $\frac{7}{1} = 7$, so every whole number is a fraction. A numerator equal to the denominator gives 1, as in $\frac{9}{9} = 1$. An improper fraction can equal a whole number, as $\frac{24}{4} = 6$ did in Example 4.

## Tricks and shortcuts

Compare fractions near 1 by their gaps to 1. Since $\frac{7}{8}$ is $\frac{1}{8}$ short of 1 and $\frac{9}{10}$ is $\frac{1}{10}$ short, and $\frac{1}{10}$ is the smaller gap, $\frac{9}{10}$ is bigger.

Use the [divisibility rules](06-division-facts-and-remainders.md#divisibility-rules) to spot common factors. For $\frac{153}{171}$, both digit sums are 9, so 9 divides both, and $\frac{153}{171} = \frac{17}{19}$.

If the numerator is prime and doesn't divide the denominator, the fraction is already in simplest form. So $\frac{13}{20}$ and $\frac{7}{30}$ need no work.

When the denominator divides 100, scaling turns a fraction into hundredths, which gives the decimal and the percent at once: $\frac{3}{25} = \frac{12}{100} = 0.12$, which is 12% (see [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md)).

## In code

Python's `Fraction` type stores every fraction in simplest form, so it can check your simplifying and your comparisons.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction

print(Fraction(180, 252))                   # 5/7
print(Fraction(5, 12) < Fraction(4, 9))     # True
print(Fraction(1, 4) == Fraction(25, 100))  # True
q, r = divmod(47, 6)                        # quotient and remainder
print(q, Fraction(r, 6))                    # 7 5/6
print(Fraction(3 * 5 + 2, 5))               # 17/5
print(Fraction("0.375"))                    # 3/8
try:
    Fraction(5, 0)
except ZeroDivisionError as err:
    print(type(err).__name__)               # ZeroDivisionError
```

</details>

## FAQ

### Why is simplest form the standard answer?

Each fraction has exactly one simplest form, so two fractions are equal exactly when their simplest forms match. That makes answers easy to compare, and it is how `Fraction` tests equality. The proof that the simplest form is unique uses the fundamental theorem of arithmetic from [factors, multiples and primes](08-factors-multiples-and-primes.md).

### Is a fraction a number or a division?

Both. The fraction $\frac{3}{8}$ is a number, the point 0.375 on the number line, and it is also the result of the division $3 \div 8$. University courses define a rational number as a fraction $\frac{a}{b}$ of integers with $b \ne 0$, and the three views in [The idea](#the-idea) are three ways to picture that one number.

## Practice

### Warm-up

1\. Write three fractions equivalent to $\frac{3}{5}$, one of them with denominator 40.

<details class="solution" markdown>
<summary>Solution</summary>

Multiply the numerator and the denominator by the same number. Using 2 gives $\frac{6}{10}$ and using 3 gives $\frac{9}{15}$. For denominator 40, use $40 \div 5 = 8$: $\frac{3 \times 8}{5 \times 8} = \frac{24}{40}$.

Check by cross-multiplying with $\frac{3}{5}$: $3 \times 10 = 30 = 6 \times 5$, $3 \times 15 = 45 = 9 \times 5$ and $3 \times 40 = 120 = 24 \times 5$.

</details>

2\. Write $\frac{48}{72}$ and $\frac{105}{135}$ in simplest form.

<details class="solution" markdown>
<summary>Solution</summary>

Since $48 = 2^4 \times 3$ and $72 = 2^3 \times 3^2$, the GCF is $2^3 \times 3 = 24$, and $\frac{48}{72} = \frac{2}{3}$.

Both 105 and 135 end in 5, and both digit sums (6 and 9) are multiples of 3, so 15 divides both. Since $105 = 3 \times 5 \times 7$ and $135 = 3^3 \times 5$, the GCF is exactly $3 \times 5 = 15$, and $\frac{105}{135} = \frac{7}{9}$.

Check: $2 \times 72 = 144 = 3 \times 48$, and $7 \times 135 = 945 = 9 \times 105$. Both answers are in simplest form, since 2 and 3 share no factor but 1, and neither do 7 and 9.

</details>

### Standard

3\. Put $\frac{3}{8}$, $\frac{5}{12}$, $\frac{2}{5}$ and $\frac{1}{3}$ in order from smallest to largest.

<details class="solution" markdown>
<summary>Solution</summary>

All four are below $\frac{1}{2}$, so benchmarks don't help. Use a common denominator: the LCM of 8, 12, 5 and 3 is $2^3 \times 3 \times 5 = 120$. Then

$$
\frac{3}{8} = \frac{45}{120}, \quad \frac{5}{12} = \frac{50}{120}, \quad \frac{2}{5} = \frac{48}{120} \quad \text{and} \quad \frac{1}{3} = \frac{40}{120}.
$$

Ordering the numerators 40, 45, 48 and 50 gives

$$
\frac{1}{3} < \frac{3}{8} < \frac{2}{5} < \frac{5}{12}.
$$

Check with decimals: $0.333\ldots$, $0.375$, $0.4$ and $0.41666\ldots$, in that order.

</details>

4\. (a) Write $\frac{59}{8}$ as a mixed number. (b) Write $4\frac{5}{7}$ as an improper fraction. (c) You pour 17 litres of juice equally into 3 jugs. How much is in each jug, as a mixed number?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Since $59 = 7 \times 8 + 3$, the fraction $\frac{59}{8}$ is $7\frac{3}{8}$.

(b) Since $4 \times 7 + 5 = 33$, the mixed number $4\frac{5}{7}$ is $\frac{33}{7}$.

(c) Each jug holds $17 \div 3 = \frac{17}{3}$ litres. Since $17 = 5 \times 3 + 2$, that is $5\frac{2}{3}$ litres.

Check: (a) $7 \times 8 + 3 = 59$. (b) $33 = 4 \times 7 + 5$. (c) Three jugs of $5\frac{2}{3}$ litres hold 15 litres plus three lots of $\frac{2}{3}$ litre, which is 2 more litres, so 17 litres in all.

</details>

### Challenge

5\. Find three different fractions between $\frac{2}{3}$ and $\frac{3}{4}$.

<details class="solution" markdown>
<summary>Solution</summary>

Over the common denominator 12, the two fractions are $\frac{8}{12}$ and $\frac{9}{12}$, with no whole number between 8 and 9. So use a bigger common denominator. Multiplying both by 4 gives $\frac{32}{48}$ and $\frac{36}{48}$, with three numerators in between:

$$
\frac{33}{48}, \quad \frac{34}{48} \quad \text{and} \quad \frac{35}{48}.
$$

In simplest form, $\frac{33}{48} = \frac{11}{16}$ and $\frac{34}{48} = \frac{17}{24}$, while $\frac{35}{48}$ is already in simplest form.

Check with decimals: $\frac{2}{3} = 0.666\ldots$, then $0.6875$, $0.70833\ldots$ and $0.72916\ldots$, and finally $\frac{3}{4} = 0.75$. The same trick works for every pair of different fractions, so there is always another fraction between two of them.

</details>

6\. This one reviews [long division](07-long-division.md). Which is bigger, $\frac{7}{16}$ or 0.44? Answer it once by writing $\frac{7}{16}$ as a decimal, and once by writing 0.44 as a fraction.

<details class="solution" markdown>
<summary>Solution</summary>

By long division, $7 \div 16 = 0.4375$: sixteen goes into 70 four times with 6 left, into 60 three times with 12 left, into 120 seven times with 8 left, and into 80 five times exactly. Since $0.4375 < 0.44$, the decimal 0.44 is bigger.

As a fraction, $0.44 = \frac{44}{100} = \frac{11}{25}$. Cross-multiply: $7 \times 25 = 175$ and $11 \times 16 = 176$. The bigger product contains the numerator of $\frac{11}{25}$, so 0.44 is bigger again.

Check: $0.4375 \times 16 = 7$. The two numbers are close, and the products 175 and 176 differ by only 1, which fits.

</details>

## Where this shows up

- The next two lessons build on equivalent fractions: [adding and subtracting fractions](10-adding-and-subtracting-fractions.md) rewrites fractions over a common denominator, and [multiplying and dividing fractions](11-multiplying-and-dividing-fractions.md) simplifies as it goes. A percent is a fraction with denominator 100 ([percents](../02-middle-school/02-ratios-rates-percents/03-percents.md)).
- The proof that $\sqrt{2}$ is not a fraction starts by assuming it is one in simplest form, then reaches a contradiction: roots, irrationals and types of numbers<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md --> and proof by contradiction<!-- link: ../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md -->.
- The cross-multiplying test, $\frac{a}{b} = \frac{c}{d}$ exactly when $a \times d = c \times b$, is how university courses build the rational numbers from pairs of integers, in equivalence relations and partitions<!-- link: ../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md -->.
