# Proof by cases and WLOG

After this lesson you can split a proof into cases that cover every possibility, prove each case, check that nothing is missing, and use "without loss of generality" to merge cases that are mirror images, with a reason the reader can check.

Before this: [direct proof](01-direct-proof.md) and [proof language: let, suppose, WLOG](../01-language-and-notation/03-proof-language-let-suppose-wlog.md), which introduced cases and WLOG. For absolute value, see [absolute value equations and inequalities](../../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Which of these splits of an integer $n$ cover every possibility? (a) $n$ is even, or $n$ is odd. (b) $n < 0$, or $n > 0$. (c) $n \le 0$, or $n \ge 0$. (d) $n = 3q$, $n = 3q + 1$ or $n = 3q + 2$ for an integer $q$.
2. Write $\lvert x - 3 \rvert$ without absolute value bars, as a statement in two cases.
3. For which of these claims may you say "without loss of generality, $a \le b$"? (i) For all real $a$ and $b$, $ab \le \frac{a^2 + b^2}{2}$. (ii) For all real $a$ and $b$, $a - b < 10$.

<details class="solution" markdown>
<summary>Answers</summary>

1. (a), (c) and (d) cover everything. In (b) the number $0$ is missing. Overlap, as at $0$ in (c), is harmless.
2. $\lvert x - 3 \rvert = x - 3$ when $x \ge 3$, and $\lvert x - 3 \rvert = 3 - x$ when $x < 3$.
3. Only (i). Swapping $a$ and $b$ gives the same claim. In (ii) the swap gives "$b - a < 10$", a different claim, and assuming $a \le b$ would make $a - b \le 0 < 10$ look true when $a = 20$, $b = 0$ shows it is false.

</details>

## The idea

Every programmer knows the bug where an `if/elif` chain handles the cases the author thought of and falls through on the one they didn't. A proof by cases is that same chain, with two obligations. The first is coverage: every input must reach some branch. The second is correctness: every branch must give the right answer. A proof can fail on either, and the failure on coverage is the more common one, because the missed case is by definition the one nobody was looking at.

You have already used the method. The theorem that $n^2 + n$ is even for every integer $n$ was proved in [proof language](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#worked-examples) by splitting into "$n$ is even" and "$n$ is odd". It worked because each branch hands you something concrete. An even $n$ is $2k$, an odd one is $2k + 1$, and then it is algebra. That is the point of cases: an abstract integer is hard to compute with, and each of its types is easy.

Cases are often the right tool when a definition itself has branches. The absolute value $\lvert x \rvert$ is $x$ for some inputs and $-x$ for others, and no formula in $x$ alone says that in one line. Cases follow the definition. The same is true of $\max$ and $\min$, of piecewise functions, and of the remainder on division.

The cost is that a proof with many cases is long, and long proofs hide mistakes. The second half of the lesson is about keeping the case count small: choose the split well, and merge mirror-image cases with WLOG when the claim really is symmetric.

## Definitions

A **proof by cases** of a statement $Q$ chooses statements $C_1, C_2, \dots, C_k$, shows that at least one of them must be true, and then shows that each $C_i$ gives $Q$. In plain words, you say "there are $k$ possibilities", you prove the claim in each, and you conclude it holds in all.

The cases are **exhaustive** when at least one of them holds in every situation the claim covers. They are **mutually exclusive** when at most one holds. A proof needs the first property. It does not need the second, though cases that don't overlap are easier to check. The logic behind the method is a tautology you can check with a truth table: if $C_1$ or $C_2$ is true, and $C_1$ gives $Q$, and $C_2$ gives $Q$, then $Q$ is true (see [truth tables and logical equivalence](../02-logic-and-sets/03-truth-tables-and-logical-equivalence.md)).

The **division algorithm** says that for every integer $n$ and every positive integer $d$ there are unique integers $q$ and $r$ with $n = dq + r$ and $0 \le r < d$; the integer $r$ is the remainder. In plain words, it is long division from [division facts and remainders](../../01-elementary/06-division-facts-and-remainders.md), allowed for any integer $n$. For $d = 3$ it says that every integer is $3q$, $3q + 1$ or $3q + 2$, which gives three exhaustive cases, and that these are different (no integer has two remainders).

The **absolute value** of a real number $x$ is $\lvert x \rvert = x$ if $x \ge 0$ and $\lvert x \rvert = -x$ if $x < 0$. The **maximum** and **minimum** of real numbers $a$ and $b$ are $\max(a, b) = a$ and $\min(a, b) = b$ if $a \ge b$, and $\max(a, b) = b$ and $\min(a, b) = a$ if $a < b$. In plain words, they are the larger and the smaller of the two, and when $a = b$ both equal that common value.

A statement about objects $a$ and $b$ is **symmetric** in $a$ and $b$ if swapping the names $a$ and $b$ everywhere gives the same statement (or an equivalent one). In plain words, the claim doesn't care which object is called which. This is the property WLOG needs, as the [phrasebook](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#using-without-loss-of-generality) says.

## How to do it

### Proof by cases in five steps

1. Choose a split where each case makes the definitions concrete. A good split gives a formula in every branch (parity gives $2k$ and $2k + 1$; the sign of $x$ removes the bars from $\lvert x \rvert$).
2. Show that the cases are exhaustive, and say why: "every integer is even or odd", "$x \ge 0$ or $x < 0$".
3. Open each case with a label and an assumption: "Case 1: suppose $n$ is even." Introduce new letters inside the case, and keep them there.
4. Prove the conclusion in each case, and end each case with a sentence that states the conclusion.
5. Close with a sentence that says the conclusion holds in every case, and that the cases cover everything.

### Choosing the cases

| What appears in the claim | A natural split |
|---|---|
| an integer and "even" or "odd" | $n = 2k$ or $n = 2k + 1$ |
| divisibility by $m$ | $n = mq + r$ with $r = 0, 1, \dots, m - 1$ |
| absolute value $\lvert x \rvert$ | $x \ge 0$ or $x < 0$ |
| $\max$, $\min$ of two numbers | $a \ge b$ or $a < b$ |
| a piecewise function | one case for each piece |
| a product, a quotient or a sign | the signs of the factors |
| a hypothesis of the form "$P$ or $R$" | one case for each alternative |
| two numbers to compare | $a < b$, $a = b$ or $a > b$ |

### Checking that the cases cover everything

Write the cases as a list of statements, and ask: can all of them be false at once? For the three remainders, a failure would be an integer that is none of $3q$, $3q + 1$, $3q + 2$, and the division algorithm rules that out. For "$x < 0$ or $x > 0$", the number $x = 0$ is missed, so the list is incomplete. Two habits catch most omissions: test the boundary values (zero, equal numbers, the point where one branch ends and the next begins), and check that a case with sub-cases is itself covered by the sub-cases.

### Merging cases with WLOG

WLOG is a shortcut for "this case is the same as the one I proved, with the names swapped". It is valid only when the swap is a true symmetry. Before you use it:

1. Swap the names in the whole claim (the hypothesis and the conclusion) and compare. If the swapped claim is the same claim, WLOG is available.
2. State the assumption and the reason in the same sentence: "Without loss of generality, $a \ge 0$ and $b < 0$, since the claim is unchanged when $a$ and $b$ are swapped."
3. Check that the assumption together with the other case covers everything. Of two mixed-sign cases, "$a \ge 0$ and $b < 0$" and "$a < 0$ and $b \ge 0$", swapping turns one into the other.
4. Prove the one case fully.

Symmetry doesn't have to be a swap. If a claim stays the same when $x$ is replaced by $-x$ (as "$\lvert x \rvert^2 = x^2$" does), you may assume $x \ge 0$.

Two limits. A claim symmetric in $a$ and $b$ only is not symmetric in a third number $c$, so you may order $a$ and $b$ and still have to treat $c$ on its own. And if you are not sure, write both cases. A second case that takes four lines costs less than a doubtful WLOG.

## Worked examples

<div class="example" markdown>

### Example 1: squares modulo 3

*Theorem 1.* Let $n$ be an integer. If $3 \mid n$, then $n^2$ is a multiple of 3. If $3 \nmid n$, then $n^2 = 3k + 1$ for some integer $k$.

Step 1: the claim is about divisibility by 3, so we split by the remainder of $n$ on division by 3 (table, second row). Test: $n = 4$ gives $16 = 3 \cdot 5 + 1$, and $n = 5$ gives $25 = 3 \cdot 8 + 1$, and $n = 6$ gives $36 = 3 \cdot 12$.

Step 2: by the division algorithm, $n = 3q$, $n = 3q + 1$ or $n = 3q + 2$ for an integer $q$, and these cover every integer. Also, $3 \mid n$ exactly in the first case, because the remainder of an integer is unique.

What we know: the three forms of $n$. What we want: the stated form of $n^2$ in each case. The plan: square each form.

*Proof.* Let $n$ be an integer. By the division algorithm, there are three cases.

Step 3 and 4. Case 1: suppose $n = 3q$. Then $n^2 = 9q^2 = 3(3q^2)$, a multiple of 3, as claimed for $3 \mid n$.

Case 2: suppose $n = 3q + 1$. Then $n^2 = 9q^2 + 6q + 1 = 3(3q^2 + 2q) + 1$, which has the form $3k + 1$.

Case 3: suppose $n = 3q + 2$. Then $n^2 = 9q^2 + 12q + 4 = 3(3q^2 + 4q + 1) + 1$, which again has the form $3k + 1$.

Step 5. The integer $n$ is divisible by 3 only in Case 1, and in Cases 2 and 3 it is not. So if $3 \mid n$, then $n^2$ is a multiple of 3, and if $3 \nmid n$, then $n^2 = 3k + 1$. $\blacksquare$

Look back: the squares leave only the remainders 0 and 1, never 2. So a number of the form $3m + 2$ is never a perfect square (by uniqueness of the remainder), and $n^2 + 1$ is never divisible by 3. Check: $n = 7 = 3 \cdot 2 + 1$ gives $49 = 3 \cdot 16 + 1$, and $n = 8 = 3 \cdot 2 + 2$ gives $64 = 3 \cdot 21 + 1$. The numbers $2, 5, 8, 11, \dots$ are not squares.

</div>

<div class="example" markdown>

### Example 2: the triangle inequality

*Theorem 2 (triangle inequality).* For all real numbers $a$ and $b$, $\lvert a + b \rvert \le \lvert a \rvert + \lvert b \rvert$.

Step 1: the definition of absolute value has two branches, so we split by the signs of $a$ and $b$. Test: $a = 5$, $b = -8$ gives $3 \le 13$, and $a = -7$, $b = 2$ gives $5 \le 9$.

Step 2: each of $a$ and $b$ is either $\ge 0$ or $< 0$, which gives four combinations: both $\ge 0$; both $< 0$; $a \ge 0$ and $b < 0$; $a < 0$ and $b \ge 0$. These cover everything.

What we know: the definition of $\lvert x \rvert$. What we want: the inequality in each combination. The plan: remove the bars in each case and compare.

*Proof.* Let $a$ and $b$ be real numbers.

Case 1: $a \ge 0$ and $b \ge 0$. Then $a + b \ge 0$, so $\lvert a + b \rvert = a + b = \lvert a \rvert + \lvert b \rvert$. The inequality holds, with equality.

Case 2: $a < 0$ and $b < 0$. Then $a + b < 0$, so $\lvert a + b \rvert = -(a + b) = (-a) + (-b) = \lvert a \rvert + \lvert b \rvert$. Again equality.

Case 3: $a$ and $b$ have different signs. Swapping $a$ and $b$ leaves the claim unchanged, since $a + b = b + a$ and the right side is a sum. So, without loss of generality, $a \ge 0$ and $b < 0$ (the combination "$a < 0$ and $b \ge 0$" is the same one with the names swapped). Then $\lvert a \rvert + \lvert b \rvert = a - b$. Two sub-cases:

- If $a + b \ge 0$, then $\lvert a + b \rvert = a + b$. Since $b < 0$, we have $b < -b$, so $a + b < a - b$.
- If $a + b < 0$, then $\lvert a + b \rvert = -a - b$. Since $a \ge 0$, we have $-a \le a$, so $-a - b \le a - b$.

In both sub-cases $\lvert a + b \rvert \le a - b = \lvert a \rvert + \lvert b \rvert$. The four combinations are covered, so the inequality holds for all $a$ and $b$. $\blacksquare$

Look back: the three kinds of case have different jobs. Cases 1 and 2 are equalities, Case 3 is the only place the inequality can be strict, and WLOG halved the work there. Check: $a = 5$ and $b = -8$ is Case 3 with $a + b = -3 < 0$, so $\lvert a + b \rvert = 3 = -5 + 8 \le 13$. For $a = -7$ and $b = 2$, the names swapped give $a' = 2$, $b' = -7$, $a' + b' = -5$, and $5 \le 9$.

</div>

<div class="example" markdown>

### Example 3: maximum and minimum

*Theorem 3.* For all real numbers $a$ and $b$: (i) $\max(a, b) + \min(a, b) = a + b$ and $\max(a, b) \cdot \min(a, b) = ab$; (ii) $\max(a, b) = \frac{a + b + \lvert a - b \rvert}{2}$.

The definitions of $\max$ and $\min$ both split by whether $a \ge b$, so we use that split.

*Proof.* Let $a$ and $b$ be real numbers.

Case 1: $a \ge b$. Then $\max(a, b) = a$ and $\min(a, b) = b$, so the sum is $a + b$ and the product is $ab$. Also $a - b \ge 0$, so $\lvert a - b \rvert = a - b$, and $\frac{a + b + (a - b)}{2} = \frac{2a}{2} = a = \max(a, b)$.

Case 2: $a < b$. Then $\max(a, b) = b$ and $\min(a, b) = a$, so the sum is $b + a = a + b$ and the product is $ba = ab$. Also $a - b < 0$, so $\lvert a - b \rvert = b - a$, and $\frac{a + b + (b - a)}{2} = \frac{2b}{2} = b = \max(a, b)$.

The two cases cover every pair, so (i) and (ii) hold. $\blacksquare$

Look back: the case $a = b$ belongs to Case 1 and gives $\max = \min = a$, which is consistent. The cases overlap nowhere here, because the second is "$a < b$" and the first is "$a \ge b$": the boundary $a = b$ was assigned to exactly one of them. WLOG would not shorten the proof. The second case is the mirror of the first, but showing that the claim is symmetric requires checking the definitions of max and min on both orders, which is the same work. Check: $a = 3$ and $b = 7$ give $\max = 7$, $\min = 3$, $7 + 3 = 10$, $7 \cdot 3 = 21$, and $\frac{3 + 7 + 4}{2} = 7$. A companion formula, $\min(a, b) = \frac{a + b - \lvert a - b \rvert}{2}$, follows by subtracting (ii) from the sum in (i).

</div>

<div class="example" markdown>

### Example 4: the absolute value of a product (finish it yourself)

*Theorem 4.* For all real numbers $a$ and $b$, $\lvert a \rvert \lvert b \rvert = \lvert ab \rvert$.

Split by signs, as in Example 2. Case 1: $a \ge 0$ and $b \ge 0$. Then $ab \ge 0$, so $\lvert ab \rvert = ab = \lvert a \rvert \lvert b \rvert$. Case 2: $a < 0$ and $b < 0$. Then $ab > 0$, so $\lvert ab \rvert = ab$, and $\lvert a \rvert \lvert b \rvert = (-a)(-b) = ab$.

The claim is symmetric in $a$ and $b$ (the product is commutative), so the mixed case reduces to one combination. Do Case 3: assume without loss of generality that $a \ge 0$ and $b < 0$, and finish the proof. Be careful with $a = 0$.

<details class="solution" markdown>
<summary>Finish</summary>

Case 3: $a \ge 0$ and $b < 0$. Then $ab \le 0$ (a non-negative number times a negative number), so $\lvert ab \rvert = -ab$. This holds even when $ab = 0$, because $-0 = 0$. On the other side, $\lvert a \rvert = a$ and $\lvert b \rvert = -b$, so $\lvert a \rvert \lvert b \rvert = a(-b) = -ab$. The two sides are equal. The mirror combination follows by symmetry. $\blacksquare$

Check: $a = 4$ and $b = -3$ give $\lvert 4 \rvert \lvert -3 \rvert = 12 = \lvert -12 \rvert$, and $a = 0$, $b = -5$ gives $0 = 0$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for cases that miss a value. "If $x > 0$ ... If $x < 0$ ..." says nothing about $x = 0$. A missed case can hide a false claim. Consider "for every real $x$, $x^2 \ge x$", with the "proof": "if $x > 1$, multiply $x > 1$ by $x$ to get $x^2 > x$; if $x < 0$, then $x^2 > 0 > x$". The cases leave out $0 \le x \le 1$, where the claim fails ($x = \frac{1}{2}$ gives $\frac{1}{4} < \frac{1}{2}$).

</div>

<div class="warning" markdown>

Watch out for "similarly" when the second case is not a copy. A case is a mirror image only if the claim is symmetric. In Example 2 the two sub-cases of Case 3 are not mirror images of each other, and each needed its own argument. Write the second case, or give the symmetry reason.

</div>

<div class="warning" markdown>

Watch out for WLOG on a quantity that changes under the swap. The claim "if $ab$ is even, then $a$ is even" is not symmetric, and the argument "without loss of generality $a$ is even" assumes the conclusion ([the earlier lesson](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#edge-cases-and-common-mistakes) has the counterexample $a = 3$, $b = 2$). Another mistake is using WLOG twice: you may order two numbers, and then you may not also order the second against a third unless the claim is symmetric in all three. For three numbers where the claim is symmetric in all of them, a single sentence "without loss of generality $a \le b \le c$" is legitimate, because any three numbers can be renamed in sorted order.

</div>

<div class="warning" markdown>

Watch out for using a case's assumption after the case ends. Facts proved under "suppose $n$ is even" are not known for odd $n$. If a later sentence needs the fact, the proof has to prove it again in the other case.

</div>

Too many cases is a quieter failure. If you find yourself writing eight cases, look for a smarter split. Example 2 of [scratch work and proof strategies](03-scratch-work-and-proof-strategies.md#worked-examples) factored $n^3 - n$ into three consecutive integers and needed three cases for divisibility by 3, not six for divisibility by 6.

## Tricks and shortcuts

Write the list of cases, and the reason they cover everything, before you start any case. If you can't state the reason in one sentence, the split isn't ready.

When a claim is about remainders modulo $m$, there are only $m$ cases, whatever $n$ is. This is why the squares modulo 3 and 4 are quick to find. Squares leave remainder 0 or 1 modulo 3 and modulo 4, so they can't equal $3m + 2$ or $4m + 3$, which settles many "no solutions" questions in a few lines.

For a claim with an absolute value, the sign split is the default. For a claim with two absolute values, split at the points where each bar expression changes sign, and order those points on a number line (problem 2 does this).

If two cases end in the same computation, consider whether a different split makes them one. In Example 3, the identity (ii) removes the cases altogether once it is proved, and later proofs can use it.

## In code

The case split by remainder is a finite check, because $n^2 \bmod 3$ depends only on $n \bmod 3$. Python can list the three cases, and then test the triangle inequality on exact fractions over a seeded sample. The sample supports Theorem 2. The case analysis proves it.

<details class="code" markdown>
<summary>In code</summary>

```python
import random
from fractions import Fraction

print([(r, (r * r) % 3) for r in range(3)])        # [(0, 0), (1, 1), (2, 1)]
print({(n * n) % 3 for n in range(-50, 51)})       # {0, 1}: never 2

random.seed(1)
vals = [Fraction(random.randint(-30, 30), random.randint(1, 9)) for _ in range(300)]
print(all(abs(a + b) <= abs(a) + abs(b) for a in vals for b in vals))   # True

def sign_case(a, b):
    return ("a>=0" if a >= 0 else "a<0", "b>=0" if b >= 0 else "b<0")

print(sorted({sign_case(a, b) for a in vals for b in vals}))
# [('a<0', 'b<0'), ('a<0', 'b>=0'), ('a>=0', 'b<0'), ('a>=0', 'b>=0')]: the four cases cover everything

print(all(max(a, b) == (a + b + abs(a - b)) / 2 for a in vals for b in vals))   # True: Theorem 3 (ii)
```

The sign check shows that every sampled pair falls into exactly one of the four combinations, which is the covering claim of Example 2 made visible.

</details>

## FAQ

### How many cases is too many?

There is no fixed limit, but each case is a place to make an error and a place where the reader loses the thread. If the cases are genuinely different (like the sign combinations in the triangle inequality), a handful is fine. If they are copies of each other, merge them with WLOG or look for a better split. A good test is whether each case has a one-line reason to exist.

### Do cases have to be disjoint?

No. They must cover everything, and overlap is harmless, because a statement proved in two overlapping cases is just proved twice for the shared inputs. Disjoint cases are easier to check, so prefer them when it costs nothing.

### Why must I justify "without loss of generality"?

Because it is a promise that a whole case is a copy of another, and the reader cannot see that unless you say why. A WLOG with no reason looks the same as a WLOG that is wrong. One clause ("since the claim is unchanged when $a$ and $b$ are swapped") is enough.

### Is proof by cases the same as an if-else statement in code?

It is the same structure, and the same two obligations: every input reaches a branch, and each branch is right. The difference is that a program can fall through silently and a proof can't, because the reader checks the coverage as part of reading.

## Practice

### Warm-up

1\. Decide which of these lists of cases is exhaustive for an integer $n$ or a real $x$, and say what is missing otherwise. (a) $x < 0$, $x = 0$, $x > 0$. (b) $n$ is even, or $n$ is a multiple of 3. (c) $n = 4q$, $4q + 1$, $4q + 2$, $4q + 3$. (d) $x \le 1$ or $x \ge 1$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Exhaustive (this is trichotomy).
- (b) Not exhaustive. The integers 1, 5, 7, 11, ... are neither even nor multiples of 3.
- (c) Exhaustive, by the division algorithm with $d = 4$.
- (d) Exhaustive. The cases overlap at $x = 1$, which is harmless.

Check: for (b), $n = 5$ is odd and not a multiple of 3, so it falls in no case.

</details>

2\. Rewrite $\lvert x - 1 \rvert + \lvert x + 2 \rvert$ without absolute value bars, in cases, and check each case with a number.

<details class="solution" markdown>
<summary>Solution</summary>

The bar expressions change sign at $x = 1$ and $x = -2$, so there are three intervals.

- If $x < -2$: both $x - 1 < 0$ and $x + 2 < 0$, so the sum is $-(x - 1) - (x + 2) = -2x - 1$.
- If $-2 \le x < 1$: $x - 1 < 0$ and $x + 2 \ge 0$, so the sum is $-(x - 1) + (x + 2) = 3$.
- If $x \ge 1$: both are non-negative, so the sum is $(x - 1) + (x + 2) = 2x + 1$.

The three intervals cover all real numbers. Check: $x = -3$ gives $4 + 1 = 5 = -2(-3) - 1$. $x = 0$ gives $1 + 2 = 3$. $x = 2$ gives $1 + 4 = 5 = 2 \cdot 2 + 1$.

</details>

3\. Prove by cases on parity that $n^2 - n$ is even for every integer $n$. Then give a second, one-line proof that avoids cases.

<details class="solution" markdown>
<summary>Solution</summary>

*Proof by cases.* Let $n$ be an integer. If $n$ is even, $n = 2k$, and $n^2 - n = 4k^2 - 2k = 2(2k^2 - k)$. If $n$ is odd, $n = 2k + 1$, and $n^2 - n = 4k^2 + 4k + 1 - 2k - 1 = 4k^2 + 2k = 2(2k^2 + k)$. In both cases $n^2 - n$ is twice an integer. $\blacksquare$

*Without cases.* We have $n^2 - n = n(n - 1)$, a product of two consecutive integers. The proof that $n^2 + n$ is even applies to the integer $n - 1$ in place of $n$: $(n - 1)^2 + (n - 1) = n^2 - n$, which is therefore even. $\blacksquare$

Check: $n = 5$ gives $20$, $n = -2$ gives $4 + 2 = 6$, both even.

</details>

### Standard

4\. Prove that for every integer $n$, the remainder of $n^2$ on division by 4 is 0 or 1. Conclude that no integer of the form $4m + 3$ is a perfect square.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: every integer is even or odd. What we want: $n^2 = 4k$ or $n^2 = 4k + 1$. The plan: split by parity and square.

*Proof.* Let $n$ be an integer. If $n$ is even, $n = 2j$, and $n^2 = 4j^2$, which is $4k$ with $k = j^2$. If $n$ is odd, $n = 2j + 1$, and $n^2 = 4j^2 + 4j + 1 = 4(j^2 + j) + 1$, which is $4k + 1$ with $k = j^2 + j$. In both cases the remainder on division by 4 is 0 or 1. If $4m + 3$ were a perfect square, its remainder 3 would have to be 0 or 1, by the uniqueness of the remainder, which is false. $\blacksquare$

Check: $n = 6$ gives $36 = 4 \cdot 9$, $n = 7$ gives $49 = 4 \cdot 12 + 1$, and the numbers $3, 7, 11, 15, \dots$ are not squares.

</details>

5\. Use the triangle inequality to prove that $\lvert a - b \rvert \ge \lvert a \rvert - \lvert b \rvert$ for all real numbers $a$ and $b$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $\lvert x + y \rvert \le \lvert x \rvert + \lvert y \rvert$ for all real $x$ and $y$. What we want: $\lvert a \rvert \le \lvert a - b \rvert + \lvert b \rvert$ (the same inequality, rearranged). The plan: write $a = (a - b) + b$ and apply the triangle inequality to $x = a - b$ and $y = b$.

*Proof.* Let $a$ and $b$ be real numbers. Since $a = (a - b) + b$, the triangle inequality gives $\lvert a \rvert \le \lvert a - b \rvert + \lvert b \rvert$. Subtracting $\lvert b \rvert$ from both sides gives $\lvert a \rvert - \lvert b \rvert \le \lvert a - b \rvert$. $\blacksquare$

Look back: no cases are needed here, because the cases were paid for in Theorem 2. Check: $a = 3$ and $b = 10$ give $\lvert a - b \rvert = 7 \ge 3 - 10 = -7$, and $a = -10$, $b = 3$ give $13 \ge 10 - 3 = 7$.

</details>

6\. A student "proves" that $x^2 \ge x$ for all real $x$: "If $x > 1$, multiply $x > 1$ by $x$ to get $x^2 > x$. If $x < 0$, then $x^2 > 0 > x$." Find the missing case, and say whether the claim is true.

<details class="solution" markdown>
<summary>Solution</summary>

The cases are $x > 1$ and $x < 0$. They miss every $x$ with $0 \le x \le 1$. For those values the claim fails except at the endpoints: $x = \frac{1}{2}$ gives $x^2 = \frac{1}{4} < \frac{1}{2} = x$. So the claim is false, and the missing case hid the counterexample.

The true statement is "$x^2 \ge x$ if and only if $x \le 0$ or $x \ge 1$", which is exactly what the two correct cases and the endpoints $x = 0$, $x = 1$ show.

Check: $x = 0$ gives $0 \ge 0$ and $x = 1$ gives $1 \ge 1$, true, while $x = 0.9$ gives $0.81 < 0.9$.

</details>

### Challenge

7\. Prove that if $a$ and $b$ are integers and $3 \mid a^2 + b^2$, then $3 \mid a$ and $3 \mid b$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Theorem 1: a multiple of 3 squares to a multiple of 3, and a non-multiple squares to $3k + 1$. What we want: both $a$ and $b$ are multiples of 3. The plan: split by whether each of $a$ and $b$ is divisible by 3 (four cases), and show that only one case allows $3 \mid a^2 + b^2$.

*Proof.* Let $3 \mid a^2 + b^2$. By Theorem 1, $a^2 = 3j$ or $a^2 = 3j + 1$, and likewise $b^2 = 3k$ or $b^2 = 3k + 1$, according to whether $3 \mid a$ and $3 \mid b$.

- If $3 \mid a$ and $3 \mid b$: nothing to prove.
- If $3 \mid a$ and $3 \nmid b$: $a^2 + b^2 = 3j + 3k + 1 = 3(j + k) + 1$, with remainder 1, so $3 \nmid a^2 + b^2$.
- If $3 \nmid a$ and $3 \mid b$: the same, by symmetry in $a$ and $b$ (the claim is unchanged when they are swapped).
- If $3 \nmid a$ and $3 \nmid b$: $a^2 + b^2 = 3j + 3k + 2 = 3(j + k) + 2$, with remainder 2, so $3 \nmid a^2 + b^2$.

The last three cases contradict the hypothesis, so only the first can occur: $3 \mid a$ and $3 \mid b$. $\blacksquare$

Check: $a = 3$ and $b = 6$ give $45 = 3 \cdot 15$. And $a = 1$, $b = 1$ gives $2$, $a = 3$, $b = 1$ gives $10$, $a = 2$, $b = 4$ gives $20$, none divisible by 3.

</details>

8\. (Reviews [absolute value equations and inequalities](../../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md).) Solve $\lvert x - 1 \rvert = 2x + 3$ by cases, and check each candidate.

<details class="solution" markdown>
<summary>Solution</summary>

Split by the sign of $x - 1$.

- Case $x \ge 1$: the equation is $x - 1 = 2x + 3$, so $x = -4$. This is not in the case $x \ge 1$, so it is rejected.
- Case $x < 1$: the equation is $-(x - 1) = 2x + 3$, so $1 - x = 2x + 3$, giving $3x = -2$ and $x = -\frac{2}{3}$. This is in the case $x < 1$, so it is accepted.

The only solution is $x = -\frac{2}{3}$. Check: $\lvert -\frac{2}{3} - 1 \rvert = \frac{5}{3}$ and $2 \cdot \left(-\frac{2}{3}\right) + 3 = \frac{5}{3}$. The rejected candidate $x = -4$ gives $\lvert -5 \rvert = 5$ and $2(-4) + 3 = -5$, which is not equal.

</details>

## Where this shows up

- The next lesson, [contrapositive proof](05-contrapositive-proof.md), often ends with a split by parity or remainder, and [proof by contradiction](06-proof-by-contradiction.md) uses cases in the challenge problem about quadratic roots. [Disproving a claim by a counterexample](../04-more-proof-methods/04-counterexamples-and-disproof.md) often means finding the case the proof left out, as in problem 6.
- In CS, case analysis is the structure of code that handles branches and of correctness proofs for them: every input must reach a branch, and each branch must be right ([invariants and algorithm correctness](../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md)). Remainder cases are the heart of modular arithmetic (divisibility and modular arithmetic<!-- link: ../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->).
- In economics, piecewise functions such as a tax schedule or a profit function with a kink are handled one piece at a time, and "without loss of generality, assume the price of good 2 is 1" is a WLOG of the kind in this lesson (utility and indifference curves<!-- link: ../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md -->).
