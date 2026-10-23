# Direct proof

After this lesson you can prove "if $P$, then $Q$" by a direct proof in parity, divisibility, inequality and algorithm settings, build a proof from results you already have, and write the proof forward even when you found it backward.

Before this: [what is a proof](../01-language-and-notation/01-what-is-a-proof.md) (the method for a first proof), [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md) (the five working definitions and the divisibility results) and [proof language: let, suppose, WLOG](../01-language-and-notation/03-proof-language-let-suppose-wlog.md) (the phrasebook).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For the claim "if $m$ and $n$ are odd integers, then $m - n$ is even", write the first line and the last line of a direct proof.
2. Prove that $a^2 + b^2 \ge 2ab$ for all real numbers $a$ and $b$.
3. A student proves "if $a \mid b$ and $b \mid c$, then $a \mid c$" like this: "We have $b = aj$ and $c = bk$, so $c = ajk$. So $a \mid c$." What sentence is missing before the conclusion?

<details class="solution" markdown>
<summary>Answers</summary>

1. First line: "Let $m$ and $n$ be odd integers, so $m = 2j + 1$ and $n = 2k + 1$ for integers $j$ and $k$." Last line: "So $m - n = 2(j - k)$, and $j - k$ is an integer, which means $m - n$ is even."
2. The square of a real number is never negative, so $(a - b)^2 \ge 0$. Expanding gives $a^2 - 2ab + b^2 \ge 0$, and adding $2ab$ to both sides gives $a^2 + b^2 \ge 2ab$.
3. The definition of divides asks for an integer $l$ with $c = al$. The proof must say that $c = a(jk)$ and that $jk$ is an integer, because $j$ and $k$ are.

</details>

## The idea

Here is a line of code you may have written: `n * (n + 1) // 2`. It gives the sum $1 + 2 + \dots + n$ if the division is exact, and the `//` hides a risk, because integer division throws away a remainder. You want to know that nothing is thrown away. Testing a million values of `n` would make you confident, but you want a reason that covers every `n`. The reason is short. Of two consecutive integers one is even, so $n(n + 1)$ is even, so it is twice an integer, so dividing by 2 leaves no remainder.

That reason is a **direct proof**: start with what the claim assumes, and walk, one justified step at a time, to what the claim promises. Each step is a fact you already have (a hypothesis, a definition, a result proved earlier) or follows from the lines above it. Nothing is assumed about the conclusion, and nothing is split into cases or turned upside down. It is the proof you try first, and most of the proofs in a first discrete mathematics course are of this kind.

A direct proof is written forward and is usually found backward. When you sit down with a claim, you often don't know the first step. You do know the last: it has to produce the conclusion. So you work from the end towards the start on scratch paper, and then you write the proof in the opposite direction. The inequality at the heart of this lesson shows how far apart the two directions can look. The finished proof begins with a square, $(\sqrt{a} - \sqrt{b})^2 \ge 0$, which seems to come from nowhere. It comes from the scratch work at the bottom of the page, where the square was the last thing you reached. Writing the proof forward hides the search, and a reader who sees only the forward version should still be able to check every line.

## Definitions

A **direct proof** of a statement "if $P$, then $Q$" is a proof that assumes $P$ and then derives $Q$ through a chain of statements, each of which is a hypothesis, a definition, a result already proved, or a consequence of earlier lines.

In plain words: you are handed $P$ and asked for $Q$, so you start at $P$ and arrive at $Q$ without any detour. The shape of the page is "Suppose $P$. ... Therefore $Q$."

For real numbers $a$ and $b$ that are not negative, the **arithmetic mean** is $\frac{a + b}{2}$ and the **geometric mean** is $\sqrt{ab}$. In plain words, the arithmetic mean is the usual average, and the geometric mean is the side of a square whose area equals the area of an $a$ by $b$ rectangle. For $a = 4$ and $b = 9$ the arithmetic mean is $6.5$ and the geometric mean is $6$.

For integers $b$ and $c$, a **linear combination** of $b$ and $c$ is a number $bx + cy$ with integers $x$ and $y$. In plain words, it is what you get by multiplying $b$ and $c$ by whole numbers and adding. The divisibility theorem of the previous chapter says that a divisor of both $b$ and $c$ divides every linear combination of them.

Each of these is used the same way as the five working definitions: when you are given the term, you unpack it, and when you must prove it, you aim at it.

## How to do it

### A direct proof in six moves

1. Put the claim in the form "if $P$, then $Q$". If it says "for every integer $n$, ...", the hypothesis is only "$n$ is an integer", and the rest is the conclusion.
2. Write the first line. It names the objects and records the hypothesis: "Let $m$ and $n$ be integers such that $m + n$ is even."
3. Write the target. On scratch paper, unpack the conclusion into what must be shown: "we need an integer $l$ with $m - n = 2l$."
4. Unpack the hypothesis into equations or inequalities with fresh letters: "$m + n = 2k$ for some integer $k$."
5. Connect the two with steps you can justify. If you are stuck at the start, work backward from the target (see the next subsection), or ask what the hypothesis lets you replace.
6. Write the proof from first line to target, one justified step at a time. End by saying that the last line is the conclusion, using the words of the claim.

### Found backward, written forward

On scratch paper it is fine to write the target and ask "what would make this true?" A chain like this one is the usual product:

$$
Q \Longleftarrow S_1 \Longleftarrow S_2 \Longleftarrow \cdots \Longleftarrow S_n,
$$

where $S_n$ follows directly from the hypothesis. Each arrow says "$S_{k+1}$ is enough to give $S_k$". The finished proof reverses the order: it proves $S_n$ first, then $S_{n-1}$ from it, and so on until $Q$.

The reversal is where mistakes enter. Two things have to hold before you copy scratch work into a proof.

- Each arrow must point towards $Q$. A scratch line "$x^2 > 9$, so $x > 3$" has the arrow going the wrong way: $x^2 > 9$ is also true for $x = -5$.
- If you used equivalences (arrows both ways) in the scratch work, the proof may run them in the opposite direction, but each one needs a real reason in that direction. Multiplying both sides of an inequality by $b$ is reversible only when $b > 0$.

A simple test: read your finished proof from the top and ask of every line, "does this follow from what is above it?" If a line seems to follow only from the lines below it, you copied the scratch work backward.

### Using earlier results

A direct proof can cite a result that is already proved, as long as the result's own proof does not depend on the claim you are proving. Citing a result is an instance of that result: you check its hypotheses against what you have, then write its conclusion with your values.

- Name the result ("by the linear combination theorem") so the reader can find it.
- Match the letters: say what $a$, $b$, $x$, $y$ stand for in this use.
- Check each hypothesis of the result, including the side conditions such as $b > 0$ or $a \ne 0$.

### Two short proofs to learn from

*Theorem 1.* If $m$ and $n$ are integers and $m + n$ is even, then $m - n$ is even.

What we know: $m + n = 2k$ for some integer $k$. What we want: $m - n = 2l$ for some integer $l$. The plan: write $m - n$ using $m + n$, since $m - n = (m + n) - 2n$.

*Proof.* Let $m$ and $n$ be integers with $m + n$ even. Then $m + n = 2k$ for some integer $k$. So

$$
m - n = (m + n) - 2n = 2k - 2n = 2(k - n).
$$

Since $k - n$ is an integer, $m - n$ is even. $\blacksquare$

Look back: no cases on whether $m$ and $n$ are even or odd were needed. The proof also shows the hypothesis is used exactly once, and that it does most of the work. Check: $m = 9$ and $n = 5$ give $m + n = 14 = 2 \cdot 7$, so $k = 7$, and $m - n = 4 = 2 \cdot (7 - 5)$.

*Theorem 2.* For every integer $n$, the number $\frac{n(n + 1)}{2}$ is an integer.

What we know: the theorem "for every integer $n$, the number $n^2 + n$ is even" from [proof language](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#worked-examples). What we want: an integer $k$ with $\frac{n(n+1)}{2} = k$. The plan: cite that theorem, and divide.

*Proof.* Let $n$ be an integer. By the theorem just quoted, $n^2 + n$ is even, so $n^2 + n = 2k$ for some integer $k$. Then $\frac{n(n + 1)}{2} = \frac{n^2 + n}{2} = k$, an integer. $\blacksquare$

Look back: the proof is two lines because the work was done by an earlier result. This is the point of keeping a list of what has been proved. Check: $n = 6$ gives $\frac{6 \cdot 7}{2} = 21$, and $n = -5$ gives $\frac{(-5)(-4)}{2} = 10$.

A divisibility proof, an inequality proof and an algorithm fact come next, in the worked examples.

## Worked examples

<div class="example" markdown>

### Example 1: divisibility of products

*Theorem 3.* If $a \mid b$ and $c \mid d$, then $ac \mid bd$.

Step 1: the hypothesis is "$a \mid b$ and $c \mid d$" and the conclusion is "$ac \mid bd$". Test it: $3 \mid 12$ and $5 \mid 10$, and $15 \mid 120$ because $120 = 15 \times 8$.

Step 2: the objects are four integers $a$, $b$, $c$ and $d$.

Step 3: the target. By the definition of divides, to prove $ac \mid bd$ we need an integer $l$ with $bd = (ac)l$.

Step 4: unpack the hypothesis with a different letter for each "for some". From $a \mid b$ there is an integer $j$ with $b = aj$. From $c \mid d$ there is an integer $k$ with $d = ck$.

Step 5: connect. Multiply the two equations:

$$
bd = (aj)(ck) = (ac)(jk).
$$

The regrouping uses the commutative and associative properties of multiplication.

Step 6: the product $jk$ is an integer, so $bd = (ac)l$ with $l = jk$. By the definition of divides, $ac \mid bd$. $\blacksquare$

Check: $a = 3$, $b = 12$, $c = 5$, $d = 10$ give $j = 4$ and $k = 2$, so $l = 8$ and $15 \times 8 = 120 = 12 \times 10$.

</div>

<div class="example" markdown>

### Example 2: the arithmetic mean is at least the geometric mean

*Theorem 4 (AM-GM for two numbers).* If $a \ge 0$ and $b \ge 0$ are real numbers, then $\frac{a + b}{2} \ge \sqrt{ab}$, with equality exactly when $a = b$.

Scratch work, written backward. We want $\frac{a + b}{2} \ge \sqrt{ab}$. Multiplying by 2 is reversible, so this is the same as $a + b \ge 2\sqrt{ab}$. Moving everything to one side gives $a - 2\sqrt{ab} + b \ge 0$. Now write $a = (\sqrt{a})^2$, $b = (\sqrt{b})^2$ and $\sqrt{ab} = \sqrt{a}\sqrt{b}$ (this needs $a, b \ge 0$). The left side becomes $(\sqrt{a})^2 - 2\sqrt{a}\sqrt{b} + (\sqrt{b})^2$, which is $(\sqrt{a} - \sqrt{b})^2$. So the target is equivalent to $(\sqrt{a} - \sqrt{b})^2 \ge 0$, and that is true for a reason we know: a square is never negative.

Every scratch step above is an equivalence, so it can be read in either direction. We write the proof forward.

What we know: $a, b \ge 0$, so $\sqrt{a}$ and $\sqrt{b}$ are real numbers, and a square of a real number is at least 0. What we want: $\frac{a + b}{2} \ge \sqrt{ab}$, and the equality case. The plan: start from $(\sqrt{a} - \sqrt{b})^2 \ge 0$ and expand.

*Proof.* Let $a$ and $b$ be non-negative real numbers. Since $\sqrt{a} - \sqrt{b}$ is a real number, its square is not negative:

$$
(\sqrt{a} - \sqrt{b})^2 \ge 0.
$$

Expanding the square, and using $\sqrt{a}\sqrt{b} = \sqrt{ab}$ (valid because $a, b \ge 0$, as in [radicals and rational exponents](../../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md)), gives $a - 2\sqrt{ab} + b \ge 0$. Adding $2\sqrt{ab}$ to both sides gives $a + b \ge 2\sqrt{ab}$, and dividing both sides by 2 gives $\frac{a + b}{2} \ge \sqrt{ab}$.

For equality, the steps above are reversible, so $\frac{a + b}{2} = \sqrt{ab}$ holds exactly when $(\sqrt{a} - \sqrt{b})^2 = 0$. That happens exactly when $\sqrt{a} = \sqrt{b}$, which means $a = b$. $\blacksquare$

Look back: the hypothesis $a, b \ge 0$ was used twice, to make the square roots exist and to split $\sqrt{ab}$. Without it the statement is meaningless: for $a = b = -1$ the root $\sqrt{ab} = 1$ exists but $\frac{a + b}{2} = -1$ is smaller. A one-line corollary: for positive $x$, $x + \frac{1}{x} \ge 2$ (take $a = x$ and $b = \frac{1}{x}$, so $\sqrt{ab} = 1$).

Check: $a = 4$ and $b = 9$ give $\frac{13}{2} = 6.5 \ge \sqrt{36} = 6$, and $a = b = 5$ gives $5 = 5$.

</div>

<div class="example" markdown>

### Example 3: why Euclid's algorithm works

Euclid's algorithm finds a greatest common divisor by replacing the pair $(a, b)$ with $(b, r)$, where $r$ is the remainder of $a$ divided by $b$. The step is justified by this fact: the pair $(a, b)$ and the pair $(b, r)$ have the same common divisors, so they have the same greatest one.

*Theorem 5.* Let $a$, $b$, $q$ and $r$ be integers with $a = bq + r$. Then (i) if $d \mid a$ and $d \mid b$, then $d \mid r$; and (ii) if $d \mid b$ and $d \mid r$, then $d \mid a$.

What we know: $a = bq + r$, and the linear combination theorem (Theorem 3 of [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#building-on-lemmas)): if $d$ divides $b$ and $c$, then $d$ divides $bx + cy$ for all integers $x$ and $y$. What we want: the two divisibility statements. The plan: write $r$ as a linear combination of $a$ and $b$ for (i), and $a$ as a linear combination of $b$ and $r$ for (ii).

*Proof.* (i) Suppose $d \mid a$ and $d \mid b$. Rearranging the equation gives $r = a \cdot 1 + b \cdot (-q)$. This is a linear combination of $a$ and $b$, so by the linear combination theorem, $d \mid r$.

(ii) Suppose $d \mid b$ and $d \mid r$. Then $a = b \cdot q + r \cdot 1$ is a linear combination of $b$ and $r$, so $d \mid a$. $\blacksquare$

Look back: every common divisor of $a$ and $b$ is a common divisor of $b$ and $r$ by (i), and the other way round by (ii). So the two lists of common divisors are the same list, and the greatest on the list is the same. The proof is two lines because the real work was in the linear combination theorem. The statement is the first step of the correctness proof of the algorithm, developed in [GCD and Euclid's algorithm](../../06-cs-math/02-number-theory/02-gcd-and-euclids-algorithm.md).

Check: $a = 252$, $b = 105$, $q = 2$, $r = 42$. The common divisors of 252 and 105 are 1, 3, 7, 21, and the common divisors of 105 and 42 are also 1, 3, 7, 21.

</div>

<div class="example" markdown>

### Example 4: an odd square minus 1 (finish it yourself)

*Theorem 6.* If $n$ is an odd integer, then $8 \mid n^2 - 1$.

Steps 1 to 4: the hypothesis is "$n$ is odd" and the conclusion is "$8 \mid n^2 - 1$". Let $n$ be an odd integer, so $n = 2k + 1$ for some integer $k$. To prove the conclusion we need an integer $l$ with $n^2 - 1 = 8l$.

Step 5, first half: expand.

$$
n^2 - 1 = (2k + 1)^2 - 1 = 4k^2 + 4k = 4(k^2 + k).
$$

We have a factor of 4 and need one more factor of 2. Now finish: use a result you have already seen about $k^2 + k$, and state the final line.

<details class="solution" markdown>
<summary>Finish</summary>

By the theorem "for every integer $n$, $n^2 + n$ is even" (applied to the integer $k$), $k^2 + k = 2l$ for some integer $l$. So $n^2 - 1 = 4 \cdot 2l = 8l$, and $8 \mid n^2 - 1$. $\blacksquare$

Check: $n = 7$ gives $k = 3$, $k^2 + k = 12 = 2 \cdot 6$, so $l = 6$, and $n^2 - 1 = 48 = 8 \cdot 6$. For $n = -3$, $k = -2$, $k^2 + k = 2$, $l = 1$, and $9 - 1 = 8 = 8 \cdot 1$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for starting at the conclusion. "To prove $a^2 + b^2 \ge 2ab$: suppose $a^2 + b^2 \ge 2ab$. Then $(a - b)^2 \ge 0$, which is true. So the claim is true." The argument ran from the claim to a true statement, and a true statement can follow from a false one. The fix is to check that each step reverses, or, simpler, to write the proof forward: "$(a - b)^2 \ge 0$, so $a^2 - 2ab + b^2 \ge 0$, so $a^2 + b^2 \ge 2ab$." The lesson [scratch work and proof strategies](03-scratch-work-and-proof-strategies.md) has a case where the backward version proves a false statement.

</div>

<div class="warning" markdown>

Watch out for an unused hypothesis. If you never used a hypothesis, one of two things is true: the claim holds without it (fine, and worth saying), or you made a mistake. The hypothesis $a, b \ge 0$ in Example 2 is used to take square roots. If a proof of AM-GM never mentions it, check the proof for a hidden use of roots of negative numbers.

</div>

<div class="warning" markdown>

Watch out for an inequality that changes direction. Multiplying or dividing both sides by a negative number reverses the inequality, and multiplying by an unknown sign can go either way. In "$\frac{x}{y} \ge 2$, so $x \ge 2y$" the step is valid only when $y > 0$. Say which case you are in, or avoid the step.

</div>

<div class="warning" markdown>

Watch out for citing a result with unmet hypotheses. The linear combination theorem needs $d \mid b$ and $d \mid c$ both. You cannot apply it to "$d \mid b$ and $d \mid (b + c)$" without first showing $d \mid c$ (which is true, but it takes the argument $c = (b + c) - b$ using the theorem again).

</div>

Two small matters. Zero and negative numbers need no special treatment in Theorems 1 to 3, because the definitions hold for every integer. In Theorem 4 they do matter, as the first warning above shows: $\sqrt{ab}$ is not defined by the same rules for negative $a$ and $b$.

## Tricks and shortcuts

Write the unpacked hypothesis on the first line of your scratch paper and the unpacked target on the last line, with a gap between. The proof is the path across the gap. If the hypothesis is an equation and the target is an equation, try to turn one into the other by substitution.

When a proof of an inequality is hard to find, bring everything to one side and look for a square, or a product of positive factors. The sign of the whole expression is then visible. The AM-GM proof, the proof that $a^2 + b^2 \ge 2ab$ and the revenue bound in [what is a proof](../01-language-and-notation/01-what-is-a-proof.md#worked-examples) all have this form.

For divisibility, name the quotient. Every statement "$a \mid b$" becomes an equation "$b = ak$" with a fresh letter, and then the proof is algebra. The step to remember is the last one: say that the new multiplier is an integer.

After writing a proof, mark where each hypothesis is used. A hypothesis with no mark is a warning.

## In code

Code can check a claim on a finite range, and it can compute the objects a proof talks about. The first lines check that `n * (n + 1) // 2` loses nothing, and the next two compare the arithmetic and geometric means and Euclid's step on example numbers. As always, a test supports a theorem and doesn't prove it.

<details class="code" markdown>
<summary>In code</summary>

```python
from math import gcd, sqrt

print(all(n * (n + 1) % 2 == 0 for n in range(-1000, 1001)))   # True: nothing is lost by //

a, b = 4, 9
print((a + b) / 2, sqrt(a * b))                                  # 6.5 6.0: AM >= GM
print(all((x + y) / 2 >= sqrt(x * y) - 1e-12
          for x in range(0, 60) for y in range(0, 60)))          # True (1e-12 allows for rounding)

a, b = 252, 105
q, r = divmod(a, b)
divisors = lambda m, n: [d for d in range(1, min(m, n) + 1) if m % d == 0 and n % d == 0]
print(q, r)                                                      # 2 42
print(divisors(a, b), divisors(b, r))                            # [1, 3, 7, 21] [1, 3, 7, 21]
print(gcd(a, b), gcd(b, r))                                      # 21 21
```

The two lists of common divisors match, as Theorem 5 says they must for any $a = bq + r$. The proof covers all integers and the code covers a handful.

</details>

## FAQ

### Do I have to prove everything from the definitions each time?

No. You may cite anything proved earlier, as long as you name it and its own proof doesn't lean on your claim. Example 3 is two lines because it cites one theorem. Cite when a result fits cleanly, and unpack the definitions when it doesn't.

### How do I know which direction to work from?

Try both on scratch paper. If the hypothesis gives you an equation to substitute, start there. If the conclusion is an inequality or has a clear form to reach, start there and ask what would make it true. Most proofs are found by working from both ends until the two pieces meet, which [scratch work and proof strategies](03-scratch-work-and-proof-strategies.md) covers in detail.

### Is it a direct proof if I use algebra tricks or a cited theorem?

Yes. "Direct" means you assume $P$ and reach $Q$ without assuming something else (such as the negation of $Q$). Cases are still direct if you split the hypothesis into cases. The names of the other methods, [contrapositive](05-contrapositive-proof.md) and [contradiction](06-proof-by-contradiction.md), say what they assume instead.

### What if the proof comes out too short to be believable?

A proof such as Theorem 2 is short because earlier work carried the weight. Short is fine if each line has a reason. If you feel something must be missing, run the check at the end of the proof with a number, and read each line aloud with "because" after it.

## Practice

### Warm-up

1\. Write the first line (introducing the objects and hypothesis) and the target (what you must show) for each claim. You don't need to finish the proofs. (a) If $n$ is an integer divisible by 6, then $n$ is even. (b) If $x$ and $y$ are positive reals, then $x + y > 0$. (c) If $a \mid b$, then $a \mid -b$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) First line: "Let $n$ be an integer with $6 \mid n$, so $n = 6k$ for some integer $k$." Target: an integer $l$ with $n = 2l$.
- (b) First line: "Let $x$ and $y$ be real numbers with $x > 0$ and $y > 0$." Target: $x + y > 0$.
- (c) First line: "Let $a$ and $b$ be integers with $a \mid b$, so $b = ak$ for some integer $k$." Target: an integer $l$ with $-b = al$.

Check: each target is the conclusion unpacked by its definition. For (a), taking $l = 3k$ works since $6k = 2 \cdot 3k$, and for (c), taking $l = -k$ works.

</details>

2\. Prove that if $m$ is an odd integer and $n$ is an odd integer, then $m - n$ is even.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $m = 2j + 1$ and $n = 2k + 1$ for integers $j$ and $k$. What we want: $m - n = 2l$ for an integer $l$. The plan: subtract; the 1s cancel.

*Proof.* Let $m$ and $n$ be odd integers. Then $m = 2j + 1$ and $n = 2k + 1$ for some integers $j$ and $k$, and

$$
m - n = (2j + 1) - (2k + 1) = 2j - 2k = 2(j - k).
$$

Since $j - k$ is an integer, $m - n$ is even. $\blacksquare$

Check: $m = 9$ and $n = 3$ give $j = 4$ and $k = 1$, and $m - n = 6 = 2 \cdot 3$ with $3 = j - k$.

</details>

3\. Give the reason for each numbered line of this proof that if $a \mid b$, then $a \mid b^3$.

1. Let $a$ and $b$ be integers with $a \mid b$.
2. There is an integer $k$ with $b = ak$.
3. Then $b^3 = (ak)^3$.
4. So $b^3 = a(a^2k^3)$.
5. The number $a^2k^3$ is an integer.
6. Therefore $a \mid b^3$.

<details class="solution" markdown>
<summary>Solution</summary>

1. The hypothesis.
2. The definition of divides, applied to $a \mid b$.
3. Substitution of $ak$ for $b$.
4. The law of exponents $(ak)^3 = a^3k^3$, then pulling out one factor of $a$.
5. Products of integers are integers.
6. The definition of divides, with the integer $a^2k^3$ in the role of the multiplier.

Check: $a = 2$, $b = 6$, $k = 3$ give $b^3 = 216 = 2 \cdot 108$ and $a^2k^3 = 4 \cdot 27 = 108$.

</details>

### Standard

4\. Prove that if $a \mid b$ and $a \mid c$, then $a^2 \mid bc$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $b = aj$ and $c = ak$ for integers $j$ and $k$. What we want: $bc = a^2 l$ for an integer $l$. The plan: multiply the two equations, as in Example 1.

*Proof.* Let $a \mid b$ and $a \mid c$. Then $b = aj$ and $c = ak$ for some integers $j$ and $k$, so

$$
bc = (aj)(ak) = a^2(jk).
$$

Since $jk$ is an integer, $a^2 \mid bc$. $\blacksquare$

Check: $a = 3$, $b = 12$, $c = 21$ give $bc = 252 = 9 \cdot 28$ and $jk = 4 \cdot 7 = 28$.

</details>

5\. Find the flaw in this "proof" that $x + \frac{1}{x} \ge 2$ for every $x > 0$, then write a correct proof. "Suppose $x + \frac{1}{x} \ge 2$. Multiplying by $x$ gives $x^2 + 1 \ge 2x$. So $x^2 - 2x + 1 \ge 0$, which is $(x - 1)^2 \ge 0$, and that is true. So the claim holds."

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is the first word, "Suppose". The proof begins by assuming the conclusion and derives a true statement, which proves nothing: a true statement can follow from a false one. Here the steps do happen to reverse (multiplying by $x > 0$ is reversible), but the proof never says so, and it never uses $x > 0$ to justify the reversal.

Correct proof. What we know: $x > 0$ and squares are not negative. What we want: $x + \frac{1}{x} \ge 2$. The plan: start from the square and divide by $x$.

*Proof.* Let $x > 0$. Since $(x - 1)^2 \ge 0$, we have $x^2 - 2x + 1 \ge 0$, so $x^2 + 1 \ge 2x$. Dividing both sides by $x$, which is positive so the inequality keeps its direction, gives $x + \frac{1}{x} \ge 2$. $\blacksquare$

Look back: the hypothesis $x > 0$ is used once, in the division. For $x = -1$ the claim fails: $-1 + (-1) = -2 < 2$. Check: $x = 3$ gives $3 + \frac{1}{3} = \frac{10}{3} \ge 2$.

</details>

6\. Prove that if $a$ and $b$ are positive real numbers, then $(a + b)\left(\frac{1}{a} + \frac{1}{b}\right) \ge 4$. Do it by citing Theorem 4 twice.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $a, b > 0$, so $\frac{1}{a}$ and $\frac{1}{b}$ are also positive, and Theorem 4 applies to the pair $(a, b)$ and to the pair $\left(\frac{1}{a}, \frac{1}{b}\right)$. What we want: the product is at least 4. The plan: get two inequalities, multiply them (all sides are positive), and simplify.

*Proof.* By Theorem 4, $\frac{a + b}{2} \ge \sqrt{ab}$, and, applied to $\frac{1}{a}$ and $\frac{1}{b}$, $\frac{1}{2}\left(\frac{1}{a} + \frac{1}{b}\right) \ge \sqrt{\frac{1}{ab}}$. All four quantities are positive, so we may multiply the two inequalities:

$$
\frac{(a + b)}{2} \cdot \frac{1}{2}\left(\frac{1}{a} + \frac{1}{b}\right) \ge \sqrt{ab} \cdot \frac{1}{\sqrt{ab}} = 1.
$$

Multiplying by 4 gives $(a + b)\left(\frac{1}{a} + \frac{1}{b}\right) \ge 4$. $\blacksquare$

Look back: multiplying two inequalities needs the sides to be non-negative, which is why positivity is in the hypothesis. Check: $a = 1$ and $b = 4$ give $5 \cdot \frac{5}{4} = 6.25 \ge 4$, and $a = b = 2$ gives $4 \cdot 1 = 4$, equality.

</details>

### Challenge

7\. Prove that for all real numbers $a$ and $b$, $\left(\frac{a + b}{2}\right)^2 \le \frac{a^2 + b^2}{2}$, and say when equality holds.

<details class="solution" markdown>
<summary>Solution</summary>

Scratch: bring everything to one side. $\frac{a^2 + b^2}{2} - \frac{(a + b)^2}{4} = \frac{2a^2 + 2b^2 - a^2 - 2ab - b^2}{4} = \frac{a^2 - 2ab + b^2}{4} = \frac{(a - b)^2}{4}$. That is a square divided by 4, so it is not negative.

What we know: squares are not negative. What we want: the gap is at least 0. The plan: show the gap equals $\frac{(a - b)^2}{4}$.

*Proof.* Let $a$ and $b$ be real numbers. Then

$$
\frac{a^2 + b^2}{2} - \left(\frac{a + b}{2}\right)^2 = \frac{2a^2 + 2b^2 - (a^2 + 2ab + b^2)}{4} = \frac{(a - b)^2}{4}.
$$

The right side is at least 0, so $\left(\frac{a + b}{2}\right)^2 \le \frac{a^2 + b^2}{2}$. It is 0 exactly when $a = b$. $\blacksquare$

Look back: no hypothesis on the signs of $a$ and $b$ is needed, unlike AM-GM. Check: $a = 1$ and $b = 5$ give $\left(\frac{6}{2}\right)^2 = 9 \le \frac{26}{2} = 13$, and the gap is $4 = \frac{16}{4}$.

</details>

8\. (Reviews [rational number arithmetic](../../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md).) Prove that if $r$ and $s$ are rational numbers with $r < s$, then $\frac{r + s}{2}$ is rational and $r < \frac{r + s}{2} < s$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $r < s$, and sums and products of rationals are rational (note that $\frac{r+s}{2} = \frac{1}{2}(r + s)$ is a product of two rationals). What we want: rationality and the two inequalities. The plan: cite the closure results for the first part, and add $r$ or $s$ to the inequality $r < s$ for the second.

*Proof.* Let $r$ and $s$ be rational with $r < s$. The sum $r + s$ is rational, and so is the product of $\frac{1}{2}$ with it, by Proposition 6 and by problem 7 in [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md), which show that sums and products of rationals are rational. So $\frac{r + s}{2}$ is rational.

Adding $r$ to both sides of $r < s$ gives $2r < r + s$, and dividing by 2 gives $r < \frac{r + s}{2}$. Adding $s$ to both sides of $r < s$ gives $r + s < 2s$, and dividing by 2 gives $\frac{r + s}{2} < s$. $\blacksquare$

Look back: between any two rationals there is another rational, so between any two rationals there are infinitely many. Check: $r = \frac{1}{3}$ and $s = \frac{1}{2}$ give $\frac{5/6}{2} = \frac{5}{12}$, and $\frac{1}{3} = \frac{4}{12} < \frac{5}{12} < \frac{6}{12} = \frac{1}{2}$.

</details>

## Where this shows up

- The next lesson, [how to read a proof](02-how-to-read-a-proof.md), turns the question around: given a finished proof, how do you check it? And [scratch work and proof strategies](03-scratch-work-and-proof-strategies.md) covers how to find the chain in the first place.
- In CS courses, the correctness of an algorithm step, such as Euclid's, is a direct proof, and so are the bounds in algorithm analysis ([invariants and algorithm correctness](../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md)). The inequality $x + \frac{1}{x} \ge 2$ appears when you minimize a cost with two competing terms.
- In economics, AM-GM and its relatives bound utility and cost functions, and the inequality between the arithmetic and geometric means appears in [utility and indifference curves](../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md).
