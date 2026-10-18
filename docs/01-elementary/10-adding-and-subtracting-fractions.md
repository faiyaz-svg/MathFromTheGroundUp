# Adding and subtracting fractions

After this lesson you can add and subtract fractions and mixed numbers with any denominators, using the least common denominator, and check the answer with an estimate.

Before this: [fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md), [factors, multiples and primes](08-factors-multiples-and-primes.md) for the least common multiple, and [addition and subtraction](02-addition-and-subtraction.md) for regrouping.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Work out $\frac{5}{6} + \frac{3}{8}$.
2. Work out $\frac{7}{10} - \frac{4}{15}$.
3. Work out $6\frac{1}{3} - 2\frac{3}{4}$.

<details class="solution" markdown>
<summary>Answers</summary>

1. $\frac{29}{24} = 1\frac{5}{24}$. The least common denominator is 24, and $\frac{20}{24} + \frac{9}{24} = \frac{29}{24}$.
2. $\frac{13}{30}$. The least common denominator is 30, and $\frac{21}{30} - \frac{8}{30} = \frac{13}{30}$.
3. $3\frac{7}{12}$. Over 12 the problem is $6\frac{4}{12} - 2\frac{9}{12}$. Regroup to $5\frac{16}{12} - 2\frac{9}{12}$, which is $3\frac{7}{12}$.

</details>

## The idea

You study for half an hour, take a break, then study for another quarter of an hour. In minutes that is $30 + 15 = 45$, which is three quarters of an hour. Minutes made the sum easy. A half and a quarter are different-sized pieces of an hour, but each is a whole number of minutes: $\frac{1}{2}$ of an hour is $\frac{30}{60}$ and $\frac{1}{4}$ is $\frac{15}{60}$.

Adding fractions works the same way. Fractions with the same denominator count pieces of the same size, so you add the counts: 3 eighths and 2 eighths are 5 eighths, just as 3 apples and 2 apples are 5 apples. Fractions with different denominators count pieces of different sizes, so first cut both into a common, smaller piece. Halves and thirds both cut evenly into sixths, so

$$
\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}.
$$

The tempting shortcut is to add the numerators and add the denominators. It fails on the simplest sum there is. Half a pizza plus half a pizza is a whole pizza, but the shortcut gives $\frac{1 + 1}{2 + 2} = \frac{2}{4}$, which is only half a pizza. In symbols, with $\ne$ meaning "is not equal to":

$$
\frac{1}{2} + \frac{1}{2} \ne \frac{2}{4}.
$$

The denominator names the size of the pieces, and putting two halves together doesn't change the size of a half. The right answer is two halves, $\frac{2}{2} = 1$.

## Definitions

When two fractions have the same denominator $b$ (with $b \ne 0$), add or subtract the numerators and keep the denominator:

$$
\frac{a}{b} + \frac{c}{b} = \frac{a + c}{b} \quad \text{and} \quad \frac{a}{b} - \frac{c}{b} = \frac{a - c}{b}.
$$

This works because $\frac{a}{b}$ is $a$ copies of the unit fraction $\frac{1}{b}$, and $\frac{c}{b}$ is $c$ more copies, so together they make $a + c$ copies. Subtracting takes $c$ copies away from $a$.

A **common denominator** of two or more fractions is a common multiple of their denominators. The **least common denominator** (LCD) is the least common multiple of the denominators. For $\frac{3}{4}$ and $\frac{5}{6}$, the common denominators are 12, 24, 36 and so on, and the LCD is $\operatorname{lcm}(4, 6) = 12$.

In plain words, a common denominator is a piece size that both fractions can be cut into evenly. Every common denominator gives the right answer, and the LCD keeps the numbers smallest, so there is less to simplify at the end. The product of the denominators is always a common denominator, but it is the LCD only when the denominators are relatively prime: for 4 and 6 the product is 24, not 12.

## How to do it

### Adding or subtracting two fractions

1. Find the LCD, the least common multiple of the denominators. If the denominators are already equal, go to step 3.
2. Rewrite each fraction over the LCD. Divide the LCD by the fraction's denominator, and multiply the numerator and the denominator by the result.
3. Add or subtract the numerators, and keep the denominator.
4. Simplify: divide the numerator and the denominator by their GCF. If the answer is an improper fraction and the question uses mixed numbers, convert it.
5. Check with an estimate. Round each fraction to the nearest benchmark (0, $\frac{1}{2}$ or 1) and work out the rough answer in your head. For a subtraction, also add the answer back to the number you subtracted.

### Mixed numbers

Method A uses improper fractions. Convert each mixed number to an improper fraction, follow steps 1 to 5, and convert the answer back. This always works, and it is the method algebra uses later, but the numerators get bigger.

Method B works on the parts separately. Rewrite the fraction parts over the LCD, then add or subtract the whole-number parts and the fraction parts on their own.

- When adding, the fraction parts may add up to 1 or more. Carry the whole: in $2\frac{7}{12} + 1\frac{9}{12}$, the fraction parts make $\frac{16}{12} = 1\frac{4}{12}$, so the answer is $3 + 1\frac{4}{12} = 4\frac{4}{12} = 4\frac{1}{3}$.
- When subtracting, the fraction part you subtract may be bigger than the one you start from. Regroup first: take 1 from the whole-number part and add it to the fraction part as $\frac{b}{b}$, where $b$ is the LCD. For example, $5\frac{3}{12} = 4 + \frac{12}{12} + \frac{3}{12} = 4\frac{15}{12}$.

Regrouping is the same move as in whole-number subtraction (where it is also called borrowing), except that the 1 you regroup is worth $\frac{12}{12}$ here instead of 10.

## Worked examples

<div class="example" markdown>

### Example 1: adding with the least common denominator

Work out $\frac{3}{4} + \frac{5}{6}$. Step 1: find the LCD. The multiples of 6 are 6, 12, 18, and so on, and 12 is the first one that 4 divides, so the LCD is 12. Prime factorizations give the same answer: $4 = 2^2$ and $6 = 2 \times 3$, so $\operatorname{lcm}(4, 6) = 2^2 \times 3 = 12$.

Step 2: rewrite each fraction over 12. Since $12 \div 4 = 3$, multiply the numerator and the denominator of $\frac{3}{4}$ by 3. Since $12 \div 6 = 2$, multiply both parts of $\frac{5}{6}$ by 2:

$$
\frac{3}{4} = \frac{3 \times 3}{4 \times 3} = \frac{9}{12} \quad \text{and} \quad \frac{5}{6} = \frac{5 \times 2}{6 \times 2} = \frac{10}{12}.
$$

<div class="warning" markdown>

Watch out: changing the denominator without changing the numerator gives a different number. Writing $\frac{3}{4}$ as $\frac{3}{12}$ turns three quarters into one quarter, since $\frac{3}{12} = \frac{1}{4}$. Whatever you multiply the denominator by, multiply the numerator by the same number.

</div>

Step 3: add the numerators and keep the denominator:

$$
\frac{9}{12} + \frac{10}{12} = \frac{19}{12}.
$$

Step 4: the numerator 19 is prime and doesn't divide 12, so $\frac{19}{12}$ is in simplest form. As a mixed number, $19 = 1 \times 12 + 7$ gives $1\frac{7}{12}$.

Step 5: both fractions are between $\frac{1}{2}$ and 1, so the sum is between 1 and 2. More closely, $\frac{3}{4}$ is 0.75 and $\frac{5}{6}$ is about 0.83, which add to about 1.58, and $1\frac{7}{12}$ is about 1.58 too.

Using the product $4 \times 6 = 24$ as the common denominator also works: $\frac{18}{24} + \frac{20}{24} = \frac{38}{24}$, and dividing by the GCF 2 gives $\frac{19}{12}$ again. It costs one more simplifying step.

</div>

<div class="example" markdown>

### Example 2: subtracting and checking by adding back

Work out $\frac{7}{12} - \frac{3}{8}$. The LCD of 12 and 8 is 24, since 24 is the first multiple of 12 that 8 divides. Rewrite and subtract:

$$
\frac{7}{12} - \frac{3}{8} = \frac{14}{24} - \frac{9}{24} = \frac{5}{24}.
$$

The numerator 5 is prime and doesn't divide 24, so $\frac{5}{24}$ is in simplest form.

Check by adding back: $\frac{5}{24} + \frac{9}{24} = \frac{14}{24} = \frac{7}{12}$. The estimate fits too: $\frac{7}{12}$ is a little more than $\frac{1}{2}$ and $\frac{3}{8}$ a little less, so the difference is a small fraction, and $\frac{5}{24}$ is about 0.21.

</div>

<div class="example" markdown>

### Example 3: an answer that still simplifies

Work out $\frac{7}{10} + \frac{2}{15}$. Since $10 = 2 \times 5$ and $15 = 3 \times 5$, the LCD is $2 \times 3 \times 5 = 30$, and

$$
\frac{7}{10} + \frac{2}{15} = \frac{21}{30} + \frac{4}{30} = \frac{25}{30}.
$$

Even over the LCD, the answer can need simplifying. The GCF of 25 and 30 is 5, so $\frac{25}{30} = \frac{5}{6}$.

Check by subtracting: $\frac{5}{6} - \frac{2}{15} = \frac{25}{30} - \frac{4}{30} = \frac{21}{30} = \frac{7}{10}$.

</div>

<div class="example" markdown>

### Example 4: subtracting mixed numbers two ways

Work out $5\frac{1}{4} - 2\frac{2}{3}$. Estimate first: $5\frac{1}{4}$ is a bit more than 5 and $2\frac{2}{3}$ is a bit less than 3, so the answer is a bit more than 2.

Method B. The LCD of 4 and 3 is 12, so the problem is $5\frac{3}{12} - 2\frac{8}{12}$. The fraction part you start from, $\frac{3}{12}$, is smaller than the $\frac{8}{12}$ you take away, so regroup. Take 1 from the 5 and add it as $\frac{12}{12}$:

$$
5\frac{3}{12} = 4 + \frac{12}{12} + \frac{3}{12} = 4\frac{15}{12}.
$$

Now subtract the parts separately: $4 - 2 = 2$ and $\frac{15}{12} - \frac{8}{12} = \frac{7}{12}$, so the answer is $2\frac{7}{12}$.

<div class="warning" markdown>

Watch out: the 1 you regroup is $\frac{12}{12}$, not 10. Habit from whole-number subtraction turns $5\frac{3}{12}$ into $4\frac{13}{12}$, which is wrong: $4\frac{13}{12}$ is $5\frac{1}{12}$, not $5\frac{3}{12}$. Regrouping 1 adds the denominator to the numerator.

</div>

Method A. Convert to improper fractions: $5\frac{1}{4} = \frac{21}{4}$ and $2\frac{2}{3} = \frac{8}{3}$. Then

$$
\frac{21}{4} - \frac{8}{3} = \frac{63}{12} - \frac{32}{12} = \frac{31}{12} = 2\frac{7}{12}.
$$

Both methods agree, and $2\frac{7}{12}$ is a bit more than 2, as estimated. Check by adding back: $2\frac{7}{12} + 2\frac{8}{12} = 4\frac{15}{12} = 5\frac{3}{12} = 5\frac{1}{4}$.

</div>

## Edge cases and common mistakes

Two mistakes are flagged above, at the step where they happen: changing a denominator without its numerator (Example 1) and regrouping 10 instead of a whole (Example 4). Here are the other cases.

<div class="warning" markdown>

Watch out for adding the numerators and the denominators. The shortcut gives $\frac{1}{2} + \frac{1}{3} = \frac{2}{5}$, but the right answer is $\frac{5}{6}$. A size check rules the shortcut out: adding $\frac{1}{3}$ to $\frac{1}{2}$ must give more than $\frac{1}{2}$, and $\frac{2}{5}$ is less than $\frac{1}{2}$. In general the shortcut gives a number between the two fractions, while the sum of two positive fractions is bigger than both.

</div>

<div class="warning" markdown>

Watch out when a whole number has no fraction part. To work out $4 - 1\frac{2}{5}$, write the 4 as $3\frac{5}{5}$ first. Then $3\frac{5}{5} - 1\frac{2}{5} = 2\frac{3}{5}$. Writing $4 - 1\frac{2}{5} = 3\frac{2}{5}$ subtracts the 1 and forgets the $\frac{2}{5}$.

</div>

An answer can be a whole number or 0, and that is fine: $\frac{3}{8} + \frac{5}{8} = \frac{8}{8} = 1$, and $\frac{5}{6} - \frac{10}{12} = 0$, because the two fractions are equivalent.

Subtracting a bigger fraction from a smaller one gives a negative answer: $\frac{1}{3} - \frac{1}{2} = \frac{2}{6} - \frac{3}{6} = -\frac{1}{6}$. That is a correct answer too, and rational number arithmetic<!-- link: ../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md --> covers negative fractions. With mixed numbers, such as $1\frac{1}{2} - 2\frac{1}{3}$, Method B has nothing to regroup from, so use Method A: $\frac{3}{2} - \frac{7}{3} = \frac{9}{6} - \frac{14}{6} = -\frac{5}{6}$.

For three or more fractions, the LCD is the LCM of all the denominators, and the steps don't change (Practice problem 6 has one).

## Tricks and shortcuts

For two unit fractions, the sum and difference have a pattern:

$$
\frac{1}{a} + \frac{1}{b} = \frac{a + b}{a \times b} \quad \text{and} \quad \frac{1}{a} - \frac{1}{b} = \frac{b - a}{a \times b}.
$$

So $\frac{1}{3} + \frac{1}{4} = \frac{7}{12}$ and $\frac{1}{4} - \frac{1}{5} = \frac{1}{20}$ in one step each. The pattern uses the product $a \times b$ as the common denominator, so simplify afterwards when $a$ and $b$ share a factor: $\frac{1}{4} + \frac{1}{6} = \frac{10}{24} = \frac{5}{12}$.

The general version works for every pair of fractions, with the product of the denominators as the common denominator:

$$
\frac{a}{b} + \frac{c}{d} = \frac{a \times d + c \times b}{b \times d}.
$$

It is the fastest method when the denominators are relatively prime, as in $\frac{2}{3} + \frac{3}{5} = \frac{10 + 9}{15} = \frac{19}{15}$.

To find the LCD quickly, list multiples of the largest denominator until the other denominators divide one. For 6, 8 and 12, the multiples of 12 are 12 and 24, and both 6 and 8 divide 24.

To check an answer by computer, Python's `Fraction` type adds exactly: `Fraction(3, 4) + Fraction(5, 6)` gives `Fraction(19, 12)`. The In code box in [fractions and equivalent fractions](09-fractions-and-equivalent-fractions.md#in-code) has more.

## Practice

### Warm-up

1\. Work out (a) $\frac{2}{9} + \frac{5}{9}$ and (b) $\frac{11}{12} - \frac{5}{12}$.

<details class="solution" markdown>
<summary>Solution</summary>

The denominators are equal, so add or subtract the numerators. (a) $\frac{2 + 5}{9} = \frac{7}{9}$, already in simplest form. (b) $\frac{11 - 5}{12} = \frac{6}{12}$, which simplifies to $\frac{1}{2}$.

Check: (a) $\frac{7}{9} - \frac{5}{9} = \frac{2}{9}$. (b) $\frac{6}{12} + \frac{5}{12} = \frac{11}{12}$.

</details>

2\. Work out (a) $\frac{1}{4} + \frac{2}{3}$ and (b) $\frac{5}{6} - \frac{1}{4}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The LCD of 4 and 3 is 12: $\frac{3}{12} + \frac{8}{12} = \frac{11}{12}$.

(b) The LCD of 6 and 4 is 12: $\frac{10}{12} - \frac{3}{12} = \frac{7}{12}$.

Check: (a) $\frac{1}{4} + \frac{2}{3}$ is about $0.25 + 0.67 = 0.92$, and $\frac{11}{12}$ is about 0.92. (b) Adding back, $\frac{7}{12} + \frac{3}{12} = \frac{10}{12} = \frac{5}{6}$.

</details>

### Standard

3\. Work out (a) $\frac{7}{8} + \frac{5}{12}$, as a mixed number, and (b) $\frac{9}{10} - \frac{4}{15}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The LCD of 8 and 12 is 24, since 24 is the first multiple of 12 that 8 divides. Then $\frac{21}{24} + \frac{10}{24} = \frac{31}{24}$, and 31 is prime, so this is in simplest form. Since $31 = 1 \times 24 + 7$, the answer is $1\frac{7}{24}$.

(b) Since $10 = 2 \times 5$ and $15 = 3 \times 5$, the LCD is 30. Then $\frac{27}{30} - \frac{8}{30} = \frac{19}{30}$, and 19 is prime and doesn't divide 30.

Check: (a) $\frac{7}{8}$ is close to 1 and $\frac{5}{12}$ is a bit under $\frac{1}{2}$, so the sum is a bit under $1\frac{1}{2}$, and $1\frac{7}{24}$ fits. (b) Adding back, $\frac{19}{30} + \frac{8}{30} = \frac{27}{30} = \frac{9}{10}$.

</details>

4\. Work out $4\frac{1}{6} - 1\frac{3}{4}$.

<details class="solution" markdown>
<summary>Solution</summary>

The LCD of 6 and 4 is 12, so the problem is $4\frac{2}{12} - 1\frac{9}{12}$. Since $\frac{2}{12}$ is smaller than $\frac{9}{12}$, regroup: $4\frac{2}{12} = 3\frac{14}{12}$. Then $3 - 1 = 2$ and $\frac{14}{12} - \frac{9}{12} = \frac{5}{12}$, so the answer is $2\frac{5}{12}$.

Check with Method A: $\frac{25}{6} - \frac{7}{4} = \frac{50}{12} - \frac{21}{12} = \frac{29}{12} = 2\frac{5}{12}$. The estimate fits as well: about 4 minus about 2 is about 2.

</details>

### Challenge

5\. You plan 6 hours for an assignment. You work $1\frac{3}{4}$ hours on Monday and $2\frac{2}{3}$ hours on Tuesday. How much time is left, in hours and in minutes?

<details class="solution" markdown>
<summary>Solution</summary>

First add the two days. The LCD of 4 and 3 is 12, so the sum is $1\frac{9}{12} + 2\frac{8}{12} = 3\frac{17}{12}$. Since $\frac{17}{12} = 1\frac{5}{12}$, carry the 1: the total is $4\frac{5}{12}$ hours.

Then subtract from 6. Write 6 as $5\frac{12}{12}$, so $5\frac{12}{12} - 4\frac{5}{12} = 1\frac{7}{12}$ hours are left. An hour is 60 minutes, and $\frac{1}{12}$ of an hour is 5 minutes, so $\frac{7}{12}$ of an hour is 35 minutes. The time left is 1 hour and 35 minutes.

Check in minutes: Monday is $60 + 45 = 105$ minutes, Tuesday is $120 + 40 = 160$ minutes, and the time left is 95 minutes. These add to $105 + 160 + 95 = 360$ minutes, which is 6 hours.

</details>

6\. This one reviews the LCM from [factors, multiples and primes](08-factors-multiples-and-primes.md). Work out $\frac{1}{6} + \frac{1}{10} + \frac{1}{15}$.

<details class="solution" markdown>
<summary>Solution</summary>

The denominators are $6 = 2 \times 3$, $10 = 2 \times 5$ and $15 = 3 \times 5$. The LCM takes each prime with its largest exponent, so the LCD is $2 \times 3 \times 5 = 30$. Then

$$
\frac{1}{6} + \frac{1}{10} + \frac{1}{15} = \frac{5}{30} + \frac{3}{30} + \frac{2}{30} = \frac{10}{30} = \frac{1}{3}.
$$

The product of the denominators, $6 \times 10 \times 15 = 900$, also works as a common denominator, but it gives $\frac{150}{900} + \frac{90}{900} + \frac{60}{900} = \frac{300}{900}$, which takes more simplifying to reach $\frac{1}{3}$.

Check: $\frac{1}{3} - \frac{1}{15} = \frac{5}{15} - \frac{1}{15} = \frac{4}{15}$, and $\frac{1}{6} + \frac{1}{10} = \frac{5}{30} + \frac{3}{30} = \frac{8}{30} = \frac{4}{15}$.

</details>

## Where this shows up

- Adding decimals is adding fractions over 10, 100 or 1,000, and lining up the decimal points puts them over a common denominator: $0.7 + 0.25 = \frac{70}{100} + \frac{25}{100}$. See [decimals: place value, adding and subtracting](12-decimals-place-value-and-adding.md).
- In high school the same LCD steps add algebraic fractions, such as $\frac{1}{x} + \frac{1}{x + 1} = \frac{2x + 1}{x(x + 1)}$ (rational expressions<!-- link: ../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md -->), and calculus runs them backwards in partial fractions<!-- link: ../05-university-core/04-integrals/05-partial-fractions-and-improper-integrals.md -->.
- Probabilities of outcomes that can't happen together add as fractions. On one roll of a die, rolling a 6 has probability $\frac{1}{6}$ and rolling a 1 or a 2 has probability $\frac{1}{3}$, so one of the three happens with probability $\frac{1}{6} + \frac{2}{6} = \frac{1}{2}$ (basic probability<!-- link: ../02-middle-school/07-statistics-and-probability/02-basic-probability.md -->).
