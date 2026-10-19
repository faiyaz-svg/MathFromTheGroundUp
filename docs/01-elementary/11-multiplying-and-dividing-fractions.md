# Multiplying and dividing fractions

After this lesson you can multiply and divide fractions and mixed numbers, cancel common factors before you multiply, and explain why dividing by a fraction is the same as multiplying by its reciprocal.

Before this: [factors, multiples and primes](08-factors-multiples-and-primes.md) and [fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $\frac{4}{9} \times \frac{15}{8}$ in simplest form.
2. Work out $2\frac{1}{4} \div \frac{3}{8}$.
3. Which is bigger, $\frac{5}{6}$ of 30 or $30 \div \frac{5}{6}$? Decide before you work them out.

<details class="solution" markdown>
<summary>Answers</summary>

1. The answer is $\frac{5}{6}$. Cancel the 4 with the 8 (divide both by 4) and the 15 with the 9 (divide both by 3), which leaves $\frac{1 \times 5}{3 \times 2} = \frac{5}{6}$.
2. 6. Write $2\frac{1}{4}$ as $\frac{9}{4}$ and flip the divisor: $\frac{9}{4} \times \frac{8}{3} = \frac{72}{12} = 6$. Check: $6 \times \frac{3}{8} = \frac{18}{8} = \frac{9}{4}$.
3. The division. Multiplying by a number less than 1 makes 30 smaller, $\frac{5}{6} \times 30 = 25$, and dividing by a number less than 1 makes it bigger, $30 \times \frac{6}{5} = 36$.

</details>

## The idea

You cut a piece from the corner of a sheet of plywood that is 1 m wide and 1 m tall. The piece is $\frac{2}{3}$ m wide and $\frac{3}{4}$ m tall. What fraction of the sheet is it? The area of a rectangle is its width times its height, so the answer is $\frac{2}{3} \times \frac{3}{4}$. To see what that is, cut the whole sheet into 3 equal columns and 4 equal rows, and mark the cells inside the piece:

$$
\begin{array}{|c|c|c|}
\hline
\blacksquare & \blacksquare & \phantom{\blacksquare} \\
\hline
\blacksquare & \blacksquare & \\
\hline
\blacksquare & \blacksquare & \\
\hline
\phantom{\blacksquare} & & \\
\hline
\end{array}
\qquad
\begin{aligned}
&\text{width: 2 of 3 columns, so } \tfrac{2}{3} \\
&\text{height: 3 of 4 rows, so } \tfrac{3}{4} \\
&\text{piece: 6 of 12 cells, so } \tfrac{6}{12}
\end{aligned}
$$

The piece is $2 \times 3 = 6$ cells, and the sheet is $3 \times 4 = 12$ cells of the same size, so the piece is $\frac{6}{12}$ of the sheet, which is $\frac{1}{2}$. The numerators multiplied to count the marked cells, and the denominators multiplied to count all the cells. That is the whole rule: multiply the numerators, and multiply the denominators.

The same product answers "what is $\frac{2}{3}$ of $\frac{3}{4}$?", because the piece is $\frac{2}{3}$ of a strip that is $\frac{3}{4}$ of the sheet. "Of" means multiply, as in "half of 10 is 5". This also shows that multiplying doesn't always make a number bigger. Multiplying by $\frac{2}{3}$ scales a number down to two thirds of its size, and in general multiplying by a number less than 1 makes it smaller, while multiplying by a number greater than 1 makes it bigger.

Division asks a different question. The division $3 \div \frac{1}{2}$ asks how many halves fit into 3. Each whole holds 2 halves, so 3 wholes hold 6, and $3 \div \frac{1}{2} = 6 = 3 \times 2$. In the same way, $\frac{3}{4}$ fits into 3 four times, since $4 \times \frac{3}{4} = 3$, so $3 \div \frac{3}{4} = 4 = 3 \times \frac{4}{3}$. Both times, dividing by a fraction gave the same answer as multiplying by that fraction turned upside down. [How to do it](#how-to-do-it) shows why this always works.

## Definitions

For fractions $\frac{a}{b}$ and $\frac{c}{d}$, where $a$, $b$, $c$ and $d$ are whole numbers and $b$ and $d$ are not 0, the product is

$$
\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}.
$$

A whole number $n$ is the fraction $\frac{n}{1}$, so the rule covers whole numbers too: $5 \times \frac{2}{7} = \frac{5}{1} \times \frac{2}{7} = \frac{10}{7}$.

The **reciprocal** of a nonzero number $x$, also called its **multiplicative inverse**, is the number $\frac{1}{x}$, the only number whose product with $x$ is 1. For a fraction $\frac{a}{b}$ with $a$ and $b$ both nonzero, the reciprocal is $\frac{b}{a}$, because

$$
\frac{a}{b} \times \frac{b}{a} = \frac{a \times b}{b \times a} = 1.
$$

In plain words, the reciprocal of a fraction is the fraction flipped over. The reciprocal of $\frac{3}{8}$ is $\frac{8}{3}$, the reciprocal of 5 (which is $\frac{5}{1}$) is $\frac{1}{5}$, and the reciprocal of $\frac{1}{4}$ is 4. The number 0 has no reciprocal: every number times 0 is 0, so no number times 0 gives 1. Flipping $\frac{0}{5}$ would give $\frac{5}{0}$, which is undefined.

University algebra courses define division through the reciprocal. For numbers $x$ and $y$ with $y \ne 0$,

$$
x \div y = x \times \frac{1}{y}.
$$

So dividing by a fraction means multiplying by its reciprocal: $\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c}$, as long as $c$ is not 0 either.

## How to do it

These steps multiply or divide two fractions. Step 2 is only for division.

1. Convert. Write each whole number as a fraction over 1, and each mixed number as an improper fraction (one whose numerator is at least its denominator): $2\frac{1}{4} = \frac{2 \times 4 + 1}{4} = \frac{9}{4}$.
2. Flip the divisor (division only). Keep the first fraction, replace the second fraction by its reciprocal, and change $\div$ to $\times$. Only the second fraction flips.
3. Cancel. If a numerator and a denominator have a common factor, divide both by it. The two can come from different fractions. Repeat until no numerator shares a factor with any denominator.
4. Multiply the numerators to get the numerator of the answer, and multiply the denominators to get its denominator.
5. Simplify. If step 3 removed every common factor, the answer is already in simplest form. Write it as a mixed number if the question asks for one.
6. Check. Compare the size of the answer with what scaling predicts. For a division, also multiply the answer by the original divisor: you should get back the original dividend.

Many people remember step 2 as "keep, change, flip": keep the first fraction, change $\div$ to $\times$, flip the second. The two sections below say why steps 2 and 3 are allowed.

### Why cancelling is allowed

Cancelling across two fractions looks like a trick, but it is ordinary simplifying. Before you multiply, $\frac{4}{9} \times \frac{15}{8}$ is the single fraction $\frac{4 \times 15}{9 \times 8}$. Dividing the numerator and the denominator of a fraction by the same number gives an equivalent fraction, and this numerator and denominator share a factor of 4 (from the 4 and the 8) and a factor of 3 (from the 15 and the 9). Since multiplication can be done in any order, it doesn't matter which fraction each factor started in. Cancelling first gives the same answer as simplifying $\frac{60}{72}$ at the end, but with smaller numbers.

### Why dividing means multiplying by the reciprocal

Write the division as one fraction, with $\frac{a}{b}$ as its numerator and $\frac{c}{d}$ as its denominator. Multiplying the numerator and the denominator of a fraction by the same nonzero number doesn't change its value, so multiply both by $\frac{d}{c}$:

$$
\frac{a}{b} \div \frac{c}{d} = \frac{\frac{a}{b} \times \frac{d}{c}}{\frac{c}{d} \times \frac{d}{c}} = \frac{\frac{a}{b} \times \frac{d}{c}}{1} = \frac{a}{b} \times \frac{d}{c}.
$$

The denominator becomes 1 because a number times its reciprocal is 1, and dividing by 1 changes nothing. The check in step 6 confirms this from the other side: $\frac{a}{b} \times \frac{d}{c} \times \frac{c}{d} = \frac{a}{b}$, so the answer times the divisor gives back the dividend, which is what a quotient has to do.

## Worked examples

<div class="example" markdown>

### Example 1: multiplying with cancelling

Work out $\frac{6}{25} \times \frac{10}{21}$.

Steps 1 and 2 have nothing to do: both numbers are fractions already, and this is a multiplication.

Step 3: look for a numerator and a denominator with a common factor. The numerator 6 and the denominator 21 are both multiples of 3, so divide both by 3: 6 becomes 2 and 21 becomes 7. The numerator 10 and the denominator 25 are both multiples of 5, so 10 becomes 2 and 25 becomes 5. Written as one fraction, the cancelling is

$$
\frac{6 \times 10}{25 \times 21} = \frac{2 \times 2}{5 \times 7}.
$$

Nothing more cancels: the numerators are both 2, and 2 is not a factor of 5 or 7.

Step 4: multiply across. The numerator is $2 \times 2 = 4$ and the denominator is $5 \times 7 = 35$, so the product is $\frac{4}{35}$.

Step 5: the answer is already in simplest form, because step 3 removed every common factor.

Step 6: check two ways. Without cancelling, the product is $\frac{60}{525}$, and dividing both numbers by 15 gives $\frac{4}{35}$ again. For size, $\frac{6}{25}$ is about $\frac{1}{4}$ and $\frac{10}{21}$ is about $\frac{1}{2}$, so the product should be about $\frac{1}{8}$; and $\frac{4}{35}$ is a little less than $\frac{4}{32} = \frac{1}{8}$.

<div class="warning" markdown>

Watch out: cancelling always pairs a numerator with a denominator. Two numerators can't cancel each other. In $\frac{2}{3} \times \frac{4}{5}$ the 2 and the 4 are both numerators, and dividing both by 2 would give $\frac{1 \times 2}{3 \times 5} = \frac{2}{15}$ instead of the right answer, $\frac{8}{15}$. The same goes for two denominators.

</div>

</div>

<div class="example" markdown>

### Example 2: dividing a mixed number by a fraction

A pot holds $3\frac{3}{4}$ L of soup. How many servings of $\frac{5}{8}$ L does it hold?

The question is how many times $\frac{5}{8}$ fits into $3\frac{3}{4}$, so it is the division $3\frac{3}{4} \div \frac{5}{8}$.

Step 1: $3\frac{3}{4} = \frac{3 \times 4 + 3}{4} = \frac{15}{4}$. Step 2: flip the divisor, so the problem becomes $\frac{15}{4} \times \frac{8}{5}$. Step 3: 15 and 5 share a factor of 5, which leaves 3 and 1, and 8 and 4 share a factor of 4, which leaves 2 and 1. Step 4: $\frac{3 \times 2}{1 \times 1} = 6$.

The pot holds 6 servings. Check: $6 \times \frac{5}{8} = \frac{30}{8} = \frac{15}{4} = 3\frac{3}{4}$. The size makes sense too: dividing by a number less than 1 gave an answer bigger than $3\frac{3}{4}$.

</div>

<div class="example" markdown>

### Example 3: multiplying two mixed numbers

Work out $2\frac{1}{2} \times 3\frac{1}{3}$. Step 1 gives $\frac{5}{2} \times \frac{10}{3}$. In step 3 the 10 and the 2 share a factor of 2, leaving 5 and 1, so step 4 gives $\frac{5 \times 5}{1 \times 3} = \frac{25}{3}$, which is $8\frac{1}{3}$.

Check: $2\frac{1}{2} \times 3 = 7\frac{1}{2}$ and $2\frac{1}{2} \times 4 = 10$, so the answer should lie between $7\frac{1}{2}$ and 10, and it does.

<div class="warning" markdown>

Watch out: multiplying the whole parts and the fraction parts separately gives $2 \times 3 + \frac{1}{2} \times \frac{1}{3} = 6\frac{1}{6}$, which is wrong. A mixed number is a sum, $2\frac{1}{2} = 2 + \frac{1}{2}$, and multiplying two sums takes four products, the same way two-digit numbers do in multi-digit multiplication:

$$
\left(2 + \tfrac{1}{2}\right) \times \left(3 + \tfrac{1}{3}\right) = 6 + \tfrac{2}{3} + \tfrac{3}{2} + \tfrac{1}{6} = 6 + \tfrac{4}{6} + \tfrac{9}{6} + \tfrac{1}{6} = 8\tfrac{1}{3}.
$$

The shortcut keeps two of the four products and drops the middle two. Converting to improper fractions first avoids the problem.

</div>

</div>

<div class="example" markdown>

### Example 4: dividing by a whole number

Three roommates split $\frac{4}{5}$ kg of coffee equally. Each one gets $\frac{4}{5} \div 3$ kg. Step 1 writes 3 as $\frac{3}{1}$, and step 2 flips it to $\frac{1}{3}$, so each share is $\frac{4}{5} \times \frac{1}{3} = \frac{4}{15}$ kg. Nothing cancels, and the answer is untidy; that is fine.

Dividing by 3 is the same as taking a third. Check: $3 \times \frac{4}{15} = \frac{12}{15} = \frac{4}{5}$.

<div class="warning" markdown>

Watch out: dividing a fraction by 3 doesn't mean dividing its numerator and its denominator by 3. That gives an equivalent fraction, with the same value: $\frac{6}{9}$ and $\frac{2}{3}$ are equal. A third of $\frac{6}{9}$ is $\frac{6}{9} \times \frac{1}{3} = \frac{6}{27} = \frac{2}{9}$. You can divide just the numerator, as in $\frac{6}{7} \div 3 = \frac{2}{7}$, because that is the same as multiplying the denominator by 3 and then cancelling.

</div>

</div>

## Edge cases and common mistakes

Three mistakes are flagged above, at the step where they happen: cancelling two numerators (Example 1), multiplying the parts of mixed numbers separately (Example 3), and dividing both the numerator and the denominator when dividing a fraction by a whole number (Example 4). Here are the others.

<div class="warning" markdown>

Watch out for flipping the wrong fraction. In $\frac{2}{3} \div \frac{4}{5}$, flipping the first one gives $\frac{3}{2} \times \frac{4}{5} = \frac{6}{5}$, but the answer is $\frac{2}{3} \times \frac{5}{4} = \frac{5}{6}$. The wrong version works out $\frac{4}{5} \div \frac{2}{3}$, which is why it comes out as the reciprocal of the right answer. The step 6 check catches it: $\frac{6}{5} \times \frac{4}{5} = \frac{24}{25}$, not $\frac{2}{3}$.

</div>

<div class="warning" markdown>

Watch out: cancelling works across a $\times$ sign, never across $+$ or $-$. In $\frac{2}{3} + \frac{3}{5}$, the two 3s don't cancel, because a sum is not a product, and its numerator and denominator are not $2 \times 3$ and $3 \times 5$. Adding needs a common denominator: $\frac{10}{15} + \frac{9}{15} = \frac{19}{15}$.

</div>

Take the reciprocal of a mixed number only after converting it. The reciprocal of $2\frac{1}{2}$ is $\frac{2}{5}$, because $2\frac{1}{2} = \frac{5}{2}$. Flipping only the fraction part, to get $2\frac{2}{1} = 4$, is wrong, since $2\frac{1}{2} \times 4 = 10$, not 1.

Multiplying doesn't need a common denominator. Adding counts pieces, so the pieces must be the same size, but multiplying takes a fraction of a fraction, and the product of the denominators sets the new piece size by itself (the 12 cells of the plywood grid). If you rewrite $\frac{1}{2} \times \frac{1}{3}$ as $\frac{3}{6} \times \frac{2}{6}$ anyway, you still have to multiply the denominators, which gives $\frac{6}{36} = \frac{1}{6}$. Keeping the 6 as the denominator, as you would when adding, gives $\frac{6}{6} = 1$, which is wrong.

Zero times every fraction is 0, and 0 divided by every nonzero fraction is 0: $0 \div \frac{3}{4} = 0 \times \frac{4}{3} = 0$. Dividing by 0 is undefined, because 0 has no reciprocal to multiply by. A fraction with numerator 0, such as $\frac{0}{7}$, is 0, so dividing by it is also division by zero.

## Tricks and shortcuts

For a fraction of a whole number, divide by the denominator first and then multiply by the numerator. For $\frac{3}{4}$ of 20, work out $20 \div 4 = 5$ and then $5 \times 3 = 15$. This is the cancelling of step 3 done in your head, and it keeps the numbers small.

Dividing by $\frac{1}{n}$ is multiplying by $n$, where $n$ is a nonzero whole number. Dividing by $\frac{1}{2}$ doubles a number, and dividing by $\frac{1}{10}$ multiplies it by 10.

When two fractions have the same denominator, divide the numerators: $\frac{9}{10} \div \frac{3}{10} = 9 \div 3 = 3$. Nine tenths holds three tenths 3 times, just as 9 holds 3 three times. In general $\frac{a}{b} \div \frac{c}{b} = \frac{a}{c}$, and multiplying by the reciprocal gives the same thing, because the two copies of $b$ cancel.

Before you calculate, predict whether the answer is bigger or smaller than the number you start with. For positive numbers:

| Operation | By a number less than 1 | By a number greater than 1 |
|---|---|---|
| Multiply | the answer is smaller | the answer is bigger |
| Divide | the answer is bigger | the answer is smaller |

To check an answer on a computer, use Python's `fractions` module, which does exact fraction arithmetic and reduces to simplest form: `Fraction(6, 25) * Fraction(10, 21)` gives `Fraction(4, 35)`, and `1 / Fraction(0)` raises a `ZeroDivisionError`, since 0 has no reciprocal.

## Practice

### Warm-up

1\. Work out (a) $\frac{3}{5} \times \frac{2}{7}$ and (b) $\frac{3}{4}$ of 28, and (c) write down the reciprocals of 7, $\frac{2}{9}$ and $1\frac{1}{3}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Nothing cancels, so multiply across: $\frac{3 \times 2}{5 \times 7} = \frac{6}{35}$.
- (b) Divide by the denominator first: $28 \div 4 = 7$, and $7 \times 3 = 21$.
- (c) The reciprocal of 7 is $\frac{1}{7}$, and the reciprocal of $\frac{2}{9}$ is $\frac{9}{2}$. For the mixed number, convert first: $1\frac{1}{3} = \frac{4}{3}$, so its reciprocal is $\frac{3}{4}$.

Check: $\frac{6}{35}$ is less than both factors, as a product of two numbers less than 1 should be. Each number times its reciprocal is 1; for example, $\frac{4}{3} \times \frac{3}{4} = \frac{12}{12} = 1$.

</details>

2\. Work out $\frac{7}{12} \div \frac{7}{8}$.

<details class="solution" markdown>
<summary>Solution</summary>

Flip the divisor: $\frac{7}{12} \times \frac{8}{7}$. The 7s cancel, and 8 and 12 share a factor of 4, which leaves 2 and 3. So the answer is $\frac{1 \times 2}{3 \times 1} = \frac{2}{3}$.

Check: $\frac{2}{3} \times \frac{7}{8} = \frac{14}{24} = \frac{7}{12}$, the dividend.

</details>

### Standard

3\. Work out $1\frac{3}{5} \times 2\frac{1}{2} \times \frac{3}{8}$.

<details class="solution" markdown>
<summary>Solution</summary>

Convert: $\frac{8}{5} \times \frac{5}{2} \times \frac{3}{8}$. The steps work the same way with three fractions. The 8 in the numerator cancels with the 8 in the denominator, and so do the two 5s, which leaves $\frac{1 \times 1 \times 3}{1 \times 2 \times 1} = \frac{3}{2}$, or $1\frac{1}{2}$.

Check without cancelling: $\frac{8 \times 5 \times 3}{5 \times 2 \times 8} = \frac{120}{80} = \frac{3}{2}$.

</details>

4\. A cable $4\frac{1}{2}$ m long is cut into pieces $\frac{5}{8}$ m long. How many full pieces do you get, and how much cable is left over?

<details class="solution" markdown>
<summary>Solution</summary>

The number of pieces is $4\frac{1}{2} \div \frac{5}{8} = \frac{9}{2} \times \frac{8}{5}$. The 8 and the 2 share a factor of 2, which leaves 4 and 1, so the answer is $\frac{9 \times 4}{1 \times 5} = \frac{36}{5} = 7\frac{1}{5}$.

So you get 7 full pieces. They use $7 \times \frac{5}{8} = \frac{35}{8} = 4\frac{3}{8}$ m, which leaves $4\frac{4}{8} - 4\frac{3}{8} = \frac{1}{8}$ m. The $\frac{1}{5}$ in the answer is that leftover measured in pieces: $\frac{1}{8} \div \frac{5}{8} = \frac{1}{5}$.

Check: $4\frac{3}{8} + \frac{1}{8} = 4\frac{1}{2}$, the length of the cable.

</details>

### Challenge

5\. Without working them out, decide which of these are less than 12, which are more than 12, and which are equal to each other. Then work them out. (a) $12 \times \frac{4}{5}$, (b) $12 \div \frac{4}{5}$, (c) $12 \times \frac{5}{4}$, (d) $12 \div \frac{5}{4}$.

<details class="solution" markdown>
<summary>Solution</summary>

By the table in [Tricks and shortcuts](#tricks-and-shortcuts), (a) and (d) are less than 12, and (b) and (c) are more. Since dividing by a number is multiplying by its reciprocal, (b) is the same calculation as (c), and (d) is the same as (a).

- (a) and (d): $12 \times \frac{4}{5} = \frac{48}{5} = 9\frac{3}{5}$.
- (b) and (c): $12 \times \frac{5}{4} = \frac{60}{4} = 15$.

Check: $15 \times \frac{4}{5} = 12$ and $9\frac{3}{5} \times \frac{5}{4} = \frac{48}{5} \times \frac{5}{4} = \frac{48}{4} = 12$.

</details>

6\. This one reviews [adding and subtracting fractions](10-adding-and-subtracting-fractions.md). Work out $\left(\frac{1}{2} + \frac{1}{3}\right) \div \left(\frac{1}{2} - \frac{1}{3}\right)$.

<details class="solution" markdown>
<summary>Solution</summary>

Work out the brackets first, over the common denominator 6. The sum is $\frac{3}{6} + \frac{2}{6} = \frac{5}{6}$, and the difference is $\frac{3}{6} - \frac{2}{6} = \frac{1}{6}$.

Then divide. Both fractions have denominator 6, so divide the numerators: $\frac{5}{6} \div \frac{1}{6} = 5$. Flipping gives the same answer, $\frac{5}{6} \times \frac{6}{1} = 5$.

Check: $5 \times \frac{1}{6} = \frac{5}{6}$. Cancelling the halves or the thirds at the start would be the mistake from the edge cases, because they sit inside a sum and a difference, not a product.

</details>

## Where this shows up

- A rate often comes from dividing fractions: walking $\frac{3}{4}$ km in $\frac{1}{6}$ of an hour is $\frac{3}{4} \div \frac{1}{6} = 4\frac{1}{2}$ km per hour ([ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md)). In [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md), "of" means multiply again, and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md) adds negative fractions to the same rules.
- Rational expressions<!-- link: ../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md --> in algebra use the same three moves: multiply across, cancel common factors (never terms of a sum), and flip to divide.
- In probability, the chance that two independent events both happen is the product of their probabilities, so a coin landing heads and a die showing 6 has probability $\frac{1}{2} \times \frac{1}{6} = \frac{1}{12}$ ([basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md)).
