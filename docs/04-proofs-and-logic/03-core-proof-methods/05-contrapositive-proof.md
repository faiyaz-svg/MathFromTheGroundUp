# Contrapositive proof

After this lesson you can prove "if $P$, then $Q$" by proving "if not $Q$, then not $P$", explain why the two statements say the same thing, choose between a direct proof and a contrapositive proof, and avoid mixing up the contrapositive with the converse.

Before this: [conditionals and biconditionals](../02-logic-and-sets/02-conditionals-and-biconditionals.md) (converse, inverse, contrapositive), [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md), and [direct proof](01-direct-proof.md). The case split by remainders is in [proof by cases and WLOG](04-proof-by-cases-and-wlog.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write the converse and the contrapositive of "if $n$ is divisible by 6, then $n$ is even". Which one is equivalent to the original?
2. What is the first line of a proof by contrapositive of "if $n^2$ is even, then $n$ is even"?
3. Negate the statement "$x$ is irrational or $y$ is irrational".

<details class="solution" markdown>
<summary>Answers</summary>

1. Converse: if $n$ is even, then $n$ is divisible by 6 (false for $n = 2$). Contrapositive: if $n$ is not even, then $n$ is not divisible by 6. The contrapositive is equivalent to the original.
2. "We prove the contrapositive. Suppose $n$ is odd." (For an integer, "not even" means "odd".)
3. "$x$ is rational and $y$ is rational." This is De Morgan's law: the negation of "or" is "and" of the negations.

</details>

## The idea

Suppose a colleague tells you: "If the build passes, the tests ran." You see that the tests did not run. You conclude at once that the build did not pass, and you didn't need to know anything about how the build works. The logic you used is that the original statement and "if the tests didn't run, the build didn't pass" are the same fact in two shapes. This is the contrapositive, and it is the most common alternative to a direct proof.

It matters in proofs because a direct proof sometimes starts from a hypothesis that is hard to use. Take "if $n^2$ is even, then $n$ is even". The hypothesis says $n^2 = 2k$. You can't take a square root of an integer equation and stay inside the integers, so you have nothing to compute with. Now flip the statement: "if $n$ is odd, then $n^2$ is odd". The hypothesis is $n = 2k + 1$, which is something you can square. The two statements are equivalent, and the second is easy.

The technique is "flip and negate". You swap the roles of hypothesis and conclusion, and you negate both. What you gain is a different starting point. Sometimes that starting point is much richer than the original one, and sometimes it is no better, so the skill is knowing the signs that it will help.

You have seen this move already. The lemma in the proof that $\sqrt{2}$ is irrational (in [roots, irrationals and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#proving-that-the-square-root-of-2-is-irrational)) says that if $n^2$ is even then $n$ is even, and its proof shows that an odd $n$ can't have an even square. That is a contrapositive proof written without the name.

## Definitions

The **contrapositive** of the statement "if $P$, then $Q$" is the statement "if not $Q$, then not $P$". In plain words, you assume the conclusion fails and show that the hypothesis must fail too. For "if it is a square, then it has four sides", the contrapositive is "if it doesn't have four sides, then it is not a square".

A **proof by contrapositive** of "if $P$, then $Q$" is a direct proof of "if not $Q$, then not $P$". In plain words, you start from "$Q$ is false" and walk to "$P$ is false".

Two other relatives are easy to confuse with it. The **converse** is "if $Q$, then $P$", and the **inverse** is "if not $P$, then not $Q$". They are equivalent to each other and, in general, not to the original. For "if $n$ is divisible by 6, then $n$ is even", the converse "if $n$ is even, then $n$ is divisible by 6" is false ($n = 2$).

*Theorem 1.* A conditional statement and its contrapositive are logically equivalent: "if $P$, then $Q$" is true in exactly the same situations as "if not $Q$, then not $P$".

*Proof.* A truth table lists every combination of truth values of $P$ and $Q$:

| $P$ | $Q$ | if $P$ then $Q$ | not $Q$ | not $P$ | if not $Q$ then not $P$ | if $Q$ then $P$ |
|---|---|---|---|---|---|---|
| T | T | T | F | F | T | T |
| T | F | F | T | F | F | T |
| F | T | T | F | T | T | F |
| F | F | T | T | T | T | T |

The third and sixth columns agree in every row. The last column (the converse) disagrees with the third in rows 2 and 3. $\blacksquare$

Look back: a conditional is false in exactly one situation, when $P$ is true and $Q$ is false. The contrapositive is false in that situation too (here "not $Q$" is true and "not $P$" is false). That is the whole reason. The details of such tables are in [truth tables and logical equivalence](../02-logic-and-sets/03-truth-tables-and-logical-equivalence.md).

### Negating the words you meet in proofs

The first step of a contrapositive proof is negating a conclusion, and the negation has to be a usable statement. This table covers the common cases.

| Statement | Its negation |
|---|---|
| $n$ is even (for an integer $n$) | $n$ is odd |
| $n$ is odd (for an integer $n$) | $n$ is even |
| $3 \mid n$ | $3 \nmid n$, which means $n = 3q + 1$ or $n = 3q + 2$ |
| $x$ is rational | $x$ is irrational |
| $x \le y$ | $x > y$ |
| $x \ne y$ | $x = y$ |
| $P$ or $Q$ | not $P$ and not $Q$ |
| $P$ and $Q$ | not $P$ or not $Q$ |
| for every $x$, $P(x)$ | there is an $x$ with not $P(x)$ |
| there is an $x$ with $P(x)$ | for every $x$, not $P(x)$ |

The first two rows are true because every integer is even or odd and never both, by the division algorithm with divisor 2. For a real number that is not an integer, "not even" does not mean "odd", so those rows are about integers only. The last four rows are covered in detail in [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md).

## How to do it

### Proving "if $P$, then $Q$" by contrapositive

1. Write the claim as "if $P$, then $Q$", and mark $P$ and $Q$.
2. Decide whether a contrapositive helps (see the table below).
3. Negate carefully. Write "not $Q$" and "not $P$" as statements with no word "not" in them if you can, using the table above.
4. Announce the method in the first line: "We prove the contrapositive: if (not $Q$), then (not $P$)."
5. Assume (not $Q$). Introduce letters and unpack definitions, as in a direct proof.
6. Derive (not $P$).
7. Finish: "This is the contrapositive of the claim, so the claim is true."

### When to choose it

The signs are in the way the claim is shaped. A direct proof can stall at the start or at the end, and the contrapositive can fix whichever end is stuck.

| The direct proof is hard because | The contrapositive helps because |
|---|---|
| the conclusion is a negative statement ("does not divide", "is irrational", "is not equal") and has no handle | its negation is positive and becomes the hypothesis, which you can unpack |
| the conclusion is an "or" ("$x$ or $y$ is irrational") | its negation is an "and", which gives you two facts to use |
| the hypothesis is a negative statement ("$x$ is irrational") and has nothing to unpack | its negation is positive and becomes the thing to prove, usually by producing a witness |
| the hypothesis is about a function of the variable ($n^2$ even) from which you can't recover the variable | the negated conclusion is about the variable itself ($n$ odd), which you can parametrize |

A good habit: spend two minutes on the direct route, and if you can't write down the first equation after the hypothesis, switch. The converse caution goes both ways. The contrapositive does not always help. For a statement like "if $f(x) = f(y)$, then $x = y$" the hypothesis is an equation you can work with, and the contrapositive "if $x \ne y$, then $f(x) \ne f(y)$" is harder to use.

## Worked examples

<div class="example" markdown>

### Example 1: a square that is even

*Theorem 2.* Let $n$ be an integer. If $n^2$ is even, then $n$ is even.

Step 1: the hypothesis $P$ is "$n^2$ is even", and the conclusion $Q$ is "$n$ is even". Test: $n = 6$ gives $36$, even; $n = 5$ gives $25$, odd.

Step 2: the hypothesis gives $n^2 = 2k$, from which we can't recover $n$. The last row of the choice table applies, so we use the contrapositive.

Step 3: not $Q$ is "$n$ is odd" (for an integer), and not $P$ is "$n^2$ is odd". The contrapositive is: if $n$ is odd, then $n^2$ is odd.

What we know: $n = 2k + 1$ for some integer $k$. What we want: $n^2 = 2l + 1$ for some integer $l$. The plan: square, and pull out a factor of 2.

*Proof.* We prove the contrapositive: if $n$ is odd, then $n^2$ is odd. Step 4 and 5. Suppose $n$ is odd, so $n = 2k + 1$ for some integer $k$. Step 6. Then

$$
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.
$$

The number $2k^2 + 2k$ is an integer, so $n^2$ is odd. Step 7. This is the contrapositive of the claim, so if $n^2$ is even, then $n$ is even. $\blacksquare$

Look back: the proof is the same computation as problem 4 of [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#practice). The same technique shows that $3 \mid n^2$ implies $3 \mid n$ (problem 6 here). Check: $n = 7$ gives $k = 3$, $2k^2 + 2k = 24$, and $2 \cdot 24 + 1 = 49 = 7^2$.

</div>

<div class="example" markdown>

### Example 2: a product that is irrational

*Theorem 3.* Let $x$ and $y$ be real numbers. If $xy$ is irrational, then $x$ is irrational or $y$ is irrational.

Step 1: $P$ is "$xy$ is irrational", and $Q$ is "$x$ is irrational or $y$ is irrational". Test: $x = \sqrt{2}$ and $y = \sqrt{2}$ give $xy = 2$, which is rational, so the hypothesis fails and nothing is claimed. With $x = \sqrt{2}$ and $y = 3$, $xy = 3\sqrt{2}$ is irrational and $x$ is irrational, as the claim says.

Step 2: both ends are awkward. The hypothesis is negative ("not a fraction"), and the conclusion is an "or" of negatives.

Step 3: not $Q$ is "$x$ is rational and $y$ is rational" (De Morgan's law, and "not irrational" means rational). Not $P$ is "$xy$ is rational". The contrapositive is: if $x$ and $y$ are both rational, then $xy$ is rational.

What we know: $x = \frac{a}{b}$ and $y = \frac{c}{d}$ with integers $a, b, c, d$ and $b \ne 0$, $d \ne 0$. What we want: $xy = \frac{p}{q}$ with integers $p$ and $q \ne 0$. The plan: multiply the fractions.

*Proof.* We prove the contrapositive: if $x$ and $y$ are both rational, then $xy$ is rational. Suppose $x = \frac{a}{b}$ and $y = \frac{c}{d}$ with $b \ne 0$ and $d \ne 0$. Then $xy = \frac{ac}{bd}$. The numerator $ac$ and the denominator $bd$ are integers, and $bd \ne 0$ since a product of nonzero numbers is nonzero. So $xy$ is rational. $\blacksquare$

Look back: the proof of the contrapositive is the first claim of problem 7 in [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#practice), and the contrapositive turns two negative facts into two positive ones, which gave us fractions to multiply. Check: $x = \frac{2}{3}$ and $y = \frac{3}{4}$ give $\frac{6}{12} = \frac{1}{2}$.

</div>

<div class="example" markdown>

### Example 3: a sum of at least 100

*Theorem 4.* Let $a$ and $b$ be real numbers. If $a + b \ge 100$, then $a \ge 50$ or $b \ge 50$.

The conclusion is an "or", and the hypothesis is an inequality that doesn't say which of $a$ and $b$ is large. The contrapositive has a conjunction as its hypothesis.

*Proof.* We prove the contrapositive: if $a < 50$ and $b < 50$, then $a + b < 100$. Suppose $a < 50$ and $b < 50$. Adding the two inequalities gives $a + b < 100$. $\blacksquare$

Look back: the proof is one line because the negation of "or" gave us two facts. A direct proof would need cases on which of $a$ and $b$ is larger. Check: $a = 49.9$ and $b = 50.1$ have $a + b = 100$ and $b \ge 50$, and $a = b = 49$ has $a + b = 98 < 100$.

</div>

<div class="example" markdown>

### Example 4: a quadratic that is even (finish it yourself)

*Theorem 5.* Let $n$ be an integer. If $n^2 - 6n + 5$ is even, then $n$ is odd.

Steps 1 to 3: $P$ is "$n^2 - 6n + 5$ is even" and $Q$ is "$n$ is odd". The hypothesis is an equation in $n^2$ we can't unwind, so we use the contrapositive: if $n$ is even, then $n^2 - 6n + 5$ is odd. Suppose $n$ is even, so $n = 2k$ for an integer $k$. To finish we need $n^2 - 6n + 5 = 2l + 1$ for an integer $l$.

Now finish the proof by substituting $n = 2k$ and finding $l$.

<details class="solution" markdown>
<summary>Finish</summary>

Substituting, $n^2 - 6n + 5 = 4k^2 - 12k + 5 = 2(2k^2 - 6k + 2) + 1$. The number $2k^2 - 6k + 2$ is an integer, so $n^2 - 6n + 5$ is odd. This is the contrapositive, so the claim holds. $\blacksquare$

Check: $n = 4$ gives $k = 2$, $16 - 24 + 5 = -3 = 2(8 - 12 + 2) + 1 = 2(-2) + 1$. The claim itself: $n = 3$ gives $9 - 18 + 5 = -4$, even, and $n = 3$ is odd.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for proving the converse. A student asked to prove "if $n^2$ is divisible by 4, then $n$ is even" writes: "Suppose $n$ is even, so $n = 2k$. Then $n^2 = 4k^2$, which is divisible by 4." Every line is right, and it proves "if $n$ is even, then $n^2$ is divisible by 4", the converse. The contrapositive of the claim starts from "$n$ is odd", not "$n$ is even". Compare the first line of your proof with "not $Q$".

</div>

<div class="warning" markdown>

Watch out for proving the inverse. The inverse of "if $n^2$ is even, then $n$ is even" is "if $n^2$ is odd, then $n$ is odd", which starts from the wrong side. It is equivalent to the converse, not to the original. The check is the same: the first line must negate the conclusion, and the last line must negate the hypothesis.

</div>

<div class="warning" markdown>

Watch out for a wrong negation. The negation of "$x$ is irrational or $y$ is irrational" is "$x$ and $y$ are both rational", not "$x$ and $y$ are both irrational" and not "$x$ is rational or $y$ is rational". The negation of a quantified statement also changes the quantifier: the negation of "for every $x$, $P(x)$" is "there is an $x$ with not $P(x)$". Write the negation out, then test it on an example.

</div>

<div class="warning" markdown>

Watch out for "not even" when $n$ is not an integer. "Not even means odd" is a fact about integers. If the claim is about real numbers, the negation of "even" is not "odd", and the proof must say what the negation really is.

</div>

One more caution. A proof by contrapositive should not mention the original hypothesis in its middle. If you assume "not $Q$" and also "$P$", you are doing a proof by contradiction (see [the next lesson](06-proof-by-contradiction.md)), which is a different structure and not wrong, but the proof is cleaner if you commit to one.

## Tricks and shortcuts

Flip and negate on paper: write "$P \to Q$" and under it "$\neg Q \to \neg P$". Fill in each negation using the table. Then check the pair with one example: if the original is true, no example can satisfy "not $Q$" and fail "not $P$". A single example of that kind shows the original is false.

The smell of a contrapositive proof is a hypothesis that is a statement about a quantity (a square, a product, a sum) and a conclusion that is a statement about one of the parts. "If $ab$ is even, then $a$ or $b$ is even" and "if $a + b$ is odd, then one is even" have this shape.

For "if $n^2$ is divisible by $m$, then $n$ is divisible by $m$", the contrapositive says that when $m \nmid n$, then $m \nmid n^2$. That is a finite check on remainders (Theorem 1 of [proof by cases and WLOG](04-proof-by-cases-and-wlog.md#worked-examples) does it for $m = 3$).

## In code

The equivalence in Theorem 1 can be checked in four lines, and the same loop shows the converse is different. The second block tests Theorem 2 and its converse on a range of integers. A test supports a theorem and doesn't prove it. The proof above covers every integer.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import product

implies = lambda p, q: (not p) or q

for P, Q in product([True, False], repeat=2):
    print(P, Q, implies(P, Q), implies(not Q, not P), implies(Q, P))
# True True True True True
# True False False False True
# False True True True False
# False False True True True

ns = range(-100, 101)
print(all(implies(n * n % 2 == 0, n % 2 == 0) for n in ns))       # True: the claim
print(all(implies(n % 2 != 0, n * n % 2 != 0) for n in ns))       # True: its contrapositive
print(all(implies(n % 2 == 0, n * n % 4 == 0) for n in ns))       # True: if n is even, n^2 is divisible by 4
print(all(implies(n * n % 4 == 0, n % 2 == 0) for n in ns))       # True: if n^2 is divisible by 4, n is even
print([n for n in range(1, 13) if not implies(n % 2 == 0, n % 6 == 0)][:3])   # [2, 4, 8]: evens that are not multiples of 6
```

The third column of the table (the original) equals the fourth column (the contrapositive) in every row, and the fifth column (the converse) differs in rows 2 and 3. The last line is the counterexample to the converse from the quick check.

</details>

## FAQ

### Isn't the contrapositive a different statement? Why can I prove it instead?

It looks different and means the same. Both statements are false in exactly one situation (the hypothesis true and the conclusion false), so each is true exactly when the other is. Proving one proves the other, in the way that proving $a \le b$ proves "not $a > b$".

### Is proof by contrapositive the same as proof by contradiction?

No, though they are close relatives. A contrapositive proof assumes only "not $Q$" and derives "not $P$", a specific target you know in advance. A contradiction proof assumes "$P$ and not $Q$" and derives any false statement. Every contrapositive proof can be turned into a contradiction proof (assume $P$ too, and reach the clash between $P$ and "not $P$"), but the contrapositive version is cleaner when the target is known. [The next lesson](06-proof-by-contradiction.md) compares them.

### Why not just prove the converse? It looks easier.

Because the converse is a different statement. It can be false while the original is true, and it can be true while the original is false. Proving "if $n$ is even then $n^2$ is even" says nothing about "if $n^2$ is even then $n$ is even". The test of a contrapositive proof is the first line: it assumes the conclusion fails.

### Does injectivity use a contrapositive?

Yes. A function $f$ is one-to-one if different inputs give different outputs: if $x \ne y$, then $f(x) \ne f(y)$. Its contrapositive is: if $f(x) = f(y)$, then $x = y$. The second form has an equation as its hypothesis, so it is the one used in proofs. This is the same idea, and it comes up again in injective, surjective and bijective<!-- link: ../06-relations-and-functions/05-injective-surjective-bijective.md -->.

## Practice

### Warm-up

1\. Write the converse, the inverse and the contrapositive of each statement, and say which are true. (a) If $x > 3$, then $x^2 > 9$. (b) If $n$ is divisible by 6, then $n$ is divisible by 3. (c) If $xy = 0$, then $x = 0$ or $y = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The original is true. The contrapositive is "if $x^2 \le 9$, then $x \le 3$", true. The converse is "if $x^2 > 9$, then $x > 3$", false ($x = -4$). The inverse is "if $x \le 3$, then $x^2 \le 9$", false (same $x = -4$).
- (b) The original is true. The contrapositive is "if $n$ is not divisible by 3, then $n$ is not divisible by 6", true. The converse is "if $n$ is divisible by 3, then $n$ is divisible by 6", false ($n = 3$). The inverse is "if $n$ is not divisible by 6, then $n$ is not divisible by 3", false ($n = 3$).
- (c) The original is true. The contrapositive is "if $x \ne 0$ and $y \ne 0$, then $xy \ne 0$", true. The converse is "if $x = 0$ or $y = 0$, then $xy = 0$", true. The inverse is "if $xy \ne 0$, then $x \ne 0$ and $y \ne 0$", true. Here the statement is really an if-and-only-if.

Check: in each case the contrapositive has the same truth value as the original, and the converse and inverse always agree with each other.

</details>

2\. Write the first line and the last line of a proof by contrapositive of each claim. (a) If $3n + 2$ is odd, then $n$ is odd. (b) If $a + b$ is odd, then $a$ is even or $b$ is even (integers $a$, $b$). (c) If $x^2$ is irrational, then $x$ is irrational.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) First: "We prove the contrapositive. Suppose $n$ is even, so $n = 2k$." Last: "So $3n + 2$ is even."
- (b) First: "We prove the contrapositive. Suppose $a$ and $b$ are both odd." Last: "So $a + b$ is even."
- (c) First: "We prove the contrapositive. Suppose $x$ is rational, so $x = \frac{p}{q}$ with $q \ne 0$." Last: "So $x^2 = \frac{p^2}{q^2}$ is rational."

Check: the negation of "or" in (b) is "and", and the negation of "irrational" in (c) is "rational".

</details>

3\. What is wrong with this proof of "if $n^2$ is divisible by 4, then $n$ is even"? "Suppose $n$ is even, so $n = 2k$. Then $n^2 = 4k^2$ is divisible by 4."

<details class="solution" markdown>
<summary>Solution</summary>

The proof assumes "$n$ is even" and derives "$n^2$ is divisible by 4". That is the converse of the claim. A proof of the claim by contrapositive would start from "$n$ is odd" and derive "$n^2$ is not divisible by 4": $n = 2k + 1$ gives $n^2 = 4(k^2 + k) + 1$, whose remainder on division by 4 is 1.

Check: $n = 3$ gives $n^2 = 9 = 4 \cdot 2 + 1$, not divisible by 4, as the contrapositive says.

</details>

### Standard

4\. Prove that if $3n + 2$ is odd, then $n$ is odd.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: in the contrapositive, $n$ is even, so $n = 2k$. What we want: $3n + 2$ is even. The plan: substitute and pull out a factor of 2.

*Proof.* We prove the contrapositive: if $n$ is even, then $3n + 2$ is even. Suppose $n = 2k$ for an integer $k$. Then $3n + 2 = 6k + 2 = 2(3k + 1)$, and $3k + 1$ is an integer. So $3n + 2$ is even. $\blacksquare$

Look back: a direct proof would start from $3n + 2 = 2m + 1$ and solve for $n$, which gives $n = \frac{2m - 1}{3}$, an awkward expression. Check: $n = 4$ gives $14 = 2 \cdot 7$, and $n = 5$ gives $17$, odd with $n$ odd.

</details>

5\. Prove that if $x^2$ is irrational, then $x$ is irrational.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: in the contrapositive, $x$ is rational, $x = \frac{p}{q}$. What we want: $x^2$ is rational. The plan: square the fraction.

*Proof.* We prove the contrapositive: if $x$ is rational, then $x^2$ is rational. Suppose $x = \frac{p}{q}$ with integers $p$ and $q$ and $q \ne 0$. Then $x^2 = \frac{p^2}{q^2}$. The numbers $p^2$ and $q^2$ are integers, and $q^2 \ne 0$. So $x^2$ is rational. $\blacksquare$

Look back: the converse is false: $x = \sqrt{2}$ is irrational while $x^2 = 2$ is rational. Check: $x = \frac{3}{4}$ gives $\frac{9}{16}$.

</details>

6\. Prove that if $n^2$ is divisible by 3, then $n$ is divisible by 3. Use Theorem 1 of [proof by cases and WLOG](04-proof-by-cases-and-wlog.md#worked-examples).

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Theorem 1 says that if $3 \nmid n$, then $n^2 = 3k + 1$ for some integer $k$. What we want: from $3 \mid n^2$ conclude $3 \mid n$. The plan: the contrapositive is "if $3 \nmid n$, then $3 \nmid n^2$", and Theorem 1 gives most of it.

*Proof.* We prove the contrapositive: if $3 \nmid n$, then $3 \nmid n^2$. Suppose $3 \nmid n$. By Theorem 1, $n^2 = 3k + 1$ for some integer $k$. An integer of the form $3k + 1$ has remainder 1 on division by 3, and the remainder is unique, so it is not a multiple of 3. Hence $3 \nmid n^2$. $\blacksquare$

Look back: this is the lemma that makes the proof that $\sqrt{3}$ is irrational work, in the same way the even-square lemma works for $\sqrt{2}$. Check: $n = 5$ gives $25 = 3 \cdot 8 + 1$, not divisible by 3, and $n = 6$ gives $36$, divisible by 3, with $3 \mid 6$.

</details>

### Challenge

7\. Prove that if $a$, $b$ and $c$ are integers with $a^2 + b^2 = c^2$, then $a$ is even or $b$ is even.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: in the contrapositive, $a$ and $b$ are both odd, and we know squares have remainder 0 or 1 on division by 4 (problem 4 of [proof by cases and WLOG](04-proof-by-cases-and-wlog.md#practice)). What we want: $a^2 + b^2 \ne c^2$ for every integer $c$. The plan: show $a^2 + b^2$ has remainder 2 on division by 4, which no square has.

*Proof.* We prove the contrapositive: if $a$ and $b$ are both odd, then $a^2 + b^2 \ne c^2$ for every integer $c$. Suppose $a = 2j + 1$ and $b = 2k + 1$. Then

$$
a^2 + b^2 = 4j^2 + 4j + 1 + 4k^2 + 4k + 1 = 4(j^2 + j + k^2 + k) + 2.
$$

So $a^2 + b^2$ has remainder 2 on division by 4. Every integer square has remainder 0 or 1 on division by 4, so $a^2 + b^2$ is not a square. Hence $a^2 + b^2 \ne c^2$ for every integer $c$. $\blacksquare$

Look back: the contrapositive turned an equation with three unknowns into a statement about remainders. Check: the Pythagorean triple $3, 4, 5$ has $b = 4$ even, and $5, 12, 13$ has $b = 12$ even. For odd $a = 3$ and $b = 5$, $a^2 + b^2 = 34$, which is not a square, and $34 = 4 \cdot 8 + 2$.

</details>

8\. (Reviews [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md).) The statement "if a triangle is equilateral, then it is isosceles" is true. Write its converse and its contrapositive, say which is true, and prove the contrapositive from the definitions (equilateral: three equal sides; isosceles: at least two equal sides).

<details class="solution" markdown>
<summary>Solution</summary>

Converse: "if a triangle is isosceles, then it is equilateral", false: a triangle with sides 5, 5, 8 is isosceles and not equilateral. Contrapositive: "if a triangle is not isosceles, then it is not equilateral", true.

*Proof of the contrapositive.* Suppose a triangle is not isosceles. Then no two of its sides are equal. If it were equilateral, all three sides would be equal, so in particular two of them would be equal, contradicting that no two are equal. Hence the triangle is not equilateral. $\blacksquare$

Look back: this uses a contradiction inside the proof, which shows how quickly the structures merge. A direct proof of the original is shorter: three equal sides include two equal sides. Check: sides 5, 5, 5 are isosceles and equilateral, and sides 3, 4, 5 are neither.

</details>

## Where this shows up

- The next lesson, [proof by contradiction](06-proof-by-contradiction.md), assumes "$P$ and not $Q$" and compares itself with this one, and [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md) often prove one direction directly and the other by contrapositive.
- In CS, the contrapositive is the logic of debugging ("if the output is wrong, some assumption is false") and of testing: a failing test is the contrapositive of "if the code is correct, the test passes". In the theory of computation, a reduction from $A$ to $B$ is used through its contrapositive: if $B$ is easy, then $A$ is easy, so if $A$ is hard, $B$ is hard (reductions and undecidability<!-- link: ../../06-cs-math/06-theory-of-computation/06-reductions-and-undecidability.md -->).
- In economics, "if the market is efficient, then there are no arbitrage opportunities" is usually applied as its contrapositive: finding an arbitrage shows the market isn't efficient. Necessary and sufficient conditions in optimization (profit maximization and market structure<!-- link: ../../07-economics-math/03-firms-and-consumers/03-profit-maximization-and-market-structure.md -->) are used in both forms.
