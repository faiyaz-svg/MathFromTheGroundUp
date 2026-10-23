# Scratch work and proof strategies

After this lesson you can find a proof and not just check one: separate scratch work from the final proof, work backward from the goal, try small cases, unpack definitions, pick a first move from the shape of the statement, and know what to try when you are stuck.

Before this: [direct proof](01-direct-proof.md) and [how to read a proof](02-how-to-read-a-proof.md). The shape table below uses the vocabulary of [quantifiers](../02-logic-and-sets/04-quantifiers.md) and [conditionals and biconditionals](../02-logic-and-sets/02-conditionals-and-biconditionals.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For the claim "if $a$ and $b$ are real numbers with $0 < a < b$, then $a < \frac{a + b}{2}$", list the givens and the goal.
2. Name the shape of each statement and the usual first move. (a) For every real $x$, $x^2 - 6x + 10 > 0$. (b) There is an integer $n$ with $n^2 + n = 56$. (c) If $n$ is a prime greater than 2, then $n$ is odd.
3. Compute $n^3 - n$ for $n = 0, 1, 2, 3, 4, 5$, and guess a number that divides every value.

<details class="solution" markdown>
<summary>Answers</summary>

1. Givens: $a$ and $b$ are real, $0 < a$, $a < b$. Goal: $a < \frac{a + b}{2}$.
2. (a) "For every": let $x$ be an arbitrary real number, then prove the inequality. (b) "There exists": find a witness, then verify it; here $n = 7$ gives $49 + 7 = 56$. (c) "If ... then": suppose $n$ is a prime greater than 2, then show $n$ is odd.
3. The values are $0, 0, 6, 24, 60, 120$, and each is divisible by 6.

</details>

## The idea

When you read a proof in a textbook it often contains one step that seems to come out of nowhere. "Add and subtract $\frac{a^2}{4b}$." "Consider the number $p_1 p_2 \cdots p_n + 1$." "Let $\varepsilon = \frac{1}{2}$." You can check that the step works, and still be left asking how anyone would think of it. The honest answer is that the author didn't think of it first. They tried things, got stuck, worked backward from the goal, found something that fit, and then rewrote the argument in the order that is easiest to check. The step that looks like magic is the place where the scratch work was erased.

You know this pattern from programming. The commit that lands in the repository is a clean diff. The debugging session behind it had print statements, a wrong guess, a revert and a lucky look at the log. Nobody commits the print statements, and nobody expects the clean diff to show how the bug was found. A proof is the clean diff. This lesson is about the debugging session.

The method has a famous shape. George Pólya's *How to Solve It* gives four phases: understand the problem, make a plan, carry out the plan, look back. The proofs in this book are laid out that way: "what we know, what we want, the plan, the proof, look back". The first three phases take place on scratch paper before the proof is written, and the fourth tells you what to keep. His questions are worth keeping nearby: Can you restate the problem? Do you know a related problem? Can you solve a special case? Can you work backward from the goal?

## Definitions

**Scratch work** is the informal work you do to find a proof: examples, pictures, false starts, shorthand, equations written in any order. In plain words, it is for you, and it can be as messy as you like, because no one but you needs to follow it.

The **givens** of a proof are the statements you may use: the hypotheses, the definitions and the results already proved. The **goal** is the statement you must reach. In plain words, the givens are what's in your pocket and the goal is where you're going. Velleman's *How to Prove It* keeps two lists with those names, and updates them as the proof develops.

To **work backward** is to look at the goal and ask "what would be enough to prove it?", replacing the goal with a new goal that is enough for it. In plain words, you move the finish line closer to where you are. **Working forward** is the reverse: derive new statements from the givens. The **forward-backward method** alternates the two until the new givens meet the new goal.

A backward step "the goal $G$ follows if $G'$ is true" is **reversible** when $G$ and $G'$ are equivalent, so each implies the other. In plain words, a reversible step can be read in either direction. A step that is not reversible can be used only in the direction you need.

A **heuristic** is a rule of thumb that often helps and carries no guarantee. Everything in this lesson except the logic of backward steps is a heuristic. They fail sometimes, and then you try the next one.

## How to do it

### Scratch work is not the proof

The two documents have different jobs, and mixing them is the most common reason that a submitted proof is not accepted.

| | Scratch work | Final proof |
|---|---|---|
| Reader | you | a classmate who hasn't seen the argument |
| Order | the order you discovered things | logical order, from hypothesis forward to conclusion |
| Content | examples, false starts, shorthand | only what the argument needs |
| Language | symbols and arrows | full sentences with the symbols inside them |
| Goal | find an idea | convince the reader line by line |

Write the final proof as a new document. Don't copy the scratch work, and never hand in a backward argument as a forward one without checking every arrow.

### Six moves for finding a proof

1. Restate and unpack. Write the claim as "if $P$, then $Q$" or "for every ...", and replace each defined word in the hypothesis and the conclusion with its definition and fresh letters. Many "hard" proofs become routine at this step, because the definitions say what to do.
2. Try small cases. Plug in the smallest values, a typical value and an awkward one (zero, a negative number, equal values). Make a table. A pattern may suggest the proof, and a failure may show that the claim is false.
3. Draw a picture or a table. For an inequality, plot the two sides. For divisibility, list the multiples. For a statement about a set, draw a Venn diagram. A picture is not a proof, but it shows what the proof needs to say.
4. Work backward from the goal. Ask what would be enough. Write the answer as a new goal. Repeat until the goal is a statement you can prove from the givens.
5. Work forward from the givens. Write down what follows from the hypotheses: unpacked equations, consequences of earlier results. Mark the ones that look like they point towards the goal.
6. Choose a method from the shape of the claim. The table below gives the usual first move for each shape. If the first move leads nowhere, try the next method on the list.

### Choosing a method from the shape of the claim

| The claim has the shape | Usual first move | Taught in |
|---|---|---|
| for every $x$ in $S$, $P(x)$ | Let $x$ be an arbitrary element of $S$, and prove $P(x)$. | [direct proof](01-direct-proof.md) |
| there exists $x$ with $P(x)$ | Find a witness, then check it. If you can't build one, argue indirectly. | [existence and uniqueness proofs](../04-more-proof-methods/02-existence-and-uniqueness-proofs.md) |
| if $P$, then $Q$ | Suppose $P$ and derive $Q$. If $P$ gives little to use, try the contrapositive. | [direct proof](01-direct-proof.md), [contrapositive proof](05-contrapositive-proof.md) |
| not $P$, or a negative word ("irrational", "no", "does not divide") | Assume $P$ is true and look for something false. | [proof by contradiction](06-proof-by-contradiction.md) |
| $P$ or $Q$ | Assume $P$ is false and prove $Q$, or split into cases. | [proof by cases](04-proof-by-cases-and-wlog.md) |
| $P$ and $Q$ | Prove each part separately. | any of the methods above |
| $P$ if and only if $Q$ | Prove "if $P$ then $Q$", then "if $Q$ then $P$", or chain equivalences. | [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md) |
| there is exactly one $x$ | Prove that one exists, then assume two exist and show they are equal. | [existence and uniqueness proofs](../04-more-proof-methods/02-existence-and-uniqueness-proofs.md) |
| $A \subseteq B$, or $A = B$ | Let $x$ be in $A$ and show $x$ is in $B$ (and the reverse for equality). | [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md) |
| the statement is false (you must disprove it) | Find one example where the hypothesis holds and the conclusion fails. | [counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md) |
| for every $n \ge 1$, a claim built step by step | Prove the first case, and prove that each case gives the next. | [mathematical induction](../05-induction/01-mathematical-induction.md) |

A claim often has more than one shape. "For every integer $n$, if $n^2$ is even, then $n$ is even" is a "for every" statement whose body is an "if-then", and the body is the part that needs a method.

### When you are stuck

Being stuck is the normal state of proving, not a sign that something is wrong with you. These moves are ordered from cheap to expensive.

1. Reread the claim slowly. Check what every word means, and that you are proving the right direction.
2. Write the definitions out in full, with fresh letters. Look at the equations you now have.
3. Test the claim on an example. If it fails, you have a counterexample and no proof to write.
4. Prove a special case: set a variable to 0 or 1, or assume $a = b$. A special case shows which part of the argument is hard.
5. Change the problem: assume an extra hypothesis, prove a weaker conclusion, or look for a related problem you can already do. Then remove the extra assumption.
6. Try a different method, using the shape table, and in particular try the contrapositive and contradiction when the direct route gives little to work with.
7. Work from both ends, and write the gap between the givens and the goal as its own small claim.
8. Stop for an hour. Many proofs show up on the walk.

Once you find the proof, rewrite it from scratch in order. The scratch work gave you the idea, and the rewrite is where you check that you understood it.

## Worked examples

<div class="example" markdown>

### Example 1: from messy scratch to a clean proof

*Theorem 1.* For every real number $x > 0$, $x + \frac{4}{x} \ge 4$.

Here is the scratch work, in the order it happened.

Try numbers: $x = 1$ gives $5$, $x = 2$ gives $2 + 2 = 4$, $x = 4$ gives $4 + 1 = 5$, and $x = \frac{1}{2}$ gives $8.5$. The smallest value is $4$, at $x = 2$. So the claim looks right, and equality seems to happen at $x = 2$.

Try to prove it directly by algebra: $x + \frac{4}{x} - 4 = \frac{x^2 - 4x + 4}{x}$. Stuck for a minute on "what is the sign of this?" Then notice $x^2 - 4x + 4 = (x - 2)^2$, which has the equality point $x = 2$ built in. That is the idea.

Work backward to see the logic, since $x > 0$ lets us multiply: $x + \frac{4}{x} \ge 4$ is equivalent to $x^2 + 4 \ge 4x$, which is equivalent to $x^2 - 4x + 4 \ge 0$, which is equivalent to $(x - 2)^2 \ge 0$, which is true. Each "equivalent to" is reversible, because we multiplied or divided by $x > 0$.

Now the proof, written forward. What we know: $x > 0$, and a square is never negative. What we want: $x + \frac{4}{x} \ge 4$. The plan: begin with the square $(x - 2)^2$ and divide by $x$.

*Proof.* Let $x > 0$. The square of a real number is at least 0, so $(x - 2)^2 \ge 0$, that is, $x^2 - 4x + 4 \ge 0$. Dividing by $x$, which is positive, keeps the inequality's direction and gives $x - 4 + \frac{4}{x} \ge 0$. Adding 4 to both sides gives $x + \frac{4}{x} \ge 4$. $\blacksquare$

Look back: the hypothesis $x > 0$ is used once, in the division. The proof is a special case of a result we know. With $a = x$ and $b = \frac{4}{x}$, we have $\sqrt{ab} = 2$, and AM-GM (Theorem 4 of [direct proof](01-direct-proof.md#worked-examples)) says $\frac{x + 4/x}{2} \ge 2$. Spotting a related problem was the second route to the same proof. Check: $x = 2$ gives $2 + 2 = 4$ with equality, and $x = 8$ gives $8.5 \ge 4$.

</div>

<div class="example" markdown>

### Example 2: small cases lead to the proof

*Theorem 2.* For every integer $n$, the number $n^3 - n$ is divisible by 6.

Scratch work. Start with a table of small cases:

| $n$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|---|---|
| $n^3 - n$ | $-6$ | $0$ | $0$ | $0$ | $6$ | $24$ | $60$ | $120$ | $210$ |

Every value is a multiple of 6, so the claim looks true. Now unpack: factor $n^3 - n = n(n^2 - 1) = (n - 1) \cdot n \cdot (n + 1)$. That is the product of three consecutive integers. Among three consecutive integers there should be a multiple of 2 and a multiple of 3, so a multiple of 6. Two small claims, then: the product is divisible by 2, and it is divisible by 3. After that we have to combine them, and the combination is not automatic: $2 \mid 4$ and $4 \mid 4$, but $8 \nmid 4$, so "divisible by each of two numbers" does not always give "divisible by their product". For 2 and 3 it does, and the proof must say why.

Now the proof. What we know: $n^3 - n = (n - 1)n(n + 1)$; the theorem that $n^2 + n$ is even for every integer $n$; every integer has the form $3q$, $3q + 1$ or $3q + 2$. What we want: $n^3 - n = 6u$ for an integer $u$. The plan: prove divisibility by 2 and by 3 separately, then combine.

*Proof.* Let $n$ be an integer.

Divisibility by 2. We have $n^3 - n = (n - 1)(n^2 + n)$, and $n^2 + n = 2m$ for some integer $m$, by the theorem on $n^2 + n$. So $n^3 - n = 2(n - 1)m$, and $n^3 - n$ is even.

Divisibility by 3. Every integer is $3q$, $3q + 1$ or $3q + 2$ for some integer $q$, so there are three cases. If $n = 3q$, the factor $n$ of $(n - 1)n(n + 1)$ is divisible by 3. If $n = 3q + 1$, the factor $n - 1 = 3q$ is divisible by 3. If $n = 3q + 2$, the factor $n + 1 = 3(q + 1)$ is divisible by 3. In each case 3 divides one factor of the product, so 3 divides $n^3 - n$ (Lemma 2 of [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#building-on-lemmas)).

Combining. Write $n^3 - n = 3t$ for an integer $t$. We know $3t$ is even. If $t$ were odd, then $3t$ would be a product of two odd integers, which is odd (Theorem 4 of [proof language](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#worked-examples)). So $t$ is even, $t = 2u$, and $n^3 - n = 6u$. $\blacksquare$

Look back: the table suggested the claim, the factoring showed why, and the two small claims were the structure of the final proof. The step "combining" is the one a quick draft forgets, and it needs its own reason. The three-way split in the middle is a proof by cases, treated in [the next lesson](04-proof-by-cases-and-wlog.md). Check: $n = 5$ gives $n^3 - n = 120 = 6 \cdot 20$, with $n = 3 \cdot 1 + 2$ (the third case, $n + 1 = 6$ divisible by 3), $t = 40$ and $u = 20$.

</div>

<div class="example" markdown>

### Example 3: givens and goal

*Theorem 3.* If $a \mid b$ and $a \mid (b + c)$, then $a \mid c$.

This is the case that [direct proof](01-direct-proof.md#edge-cases-and-common-mistakes) warned about: the hypotheses are "$a$ divides $b$" and "$a$ divides $b + c$", and the conclusion is about $c$ alone. Keep two lists and update them.

| Step | Givens | Goal |
|---|---|---|
| Start | $a \mid b$, $a \mid (b + c)$ | $a \mid c$ |
| Unpack all three | $b = aj$, $b + c = ak$ | $c = al$ for some integer $l$ |
| Forward: eliminate $b$ | $c = (b + c) - b = ak - aj$ | $c = al$ |
| Match | $c = a(k - j)$ | $l = k - j$ is an integer |

What we know and want are in the first and last rows. The plan: express $c$ using the two given equations.

*Proof.* Let $a \mid b$ and $a \mid (b + c)$. Then $b = aj$ and $b + c = ak$ for integers $j$ and $k$. So $c = (b + c) - b = ak - aj = a(k - j)$. Since $k - j$ is an integer, $a \mid c$. $\blacksquare$

Look back: the proof is one line of algebra once the equations are unpacked, and the table made the trick visible: $c$ is a difference of the two things we are given. Check: $a = 4$, $b = 12$, $c = 8$ give $b + c = 20$, $j = 3$, $k = 5$, and $c = 4 \cdot (5 - 3) = 8$.

</div>

<div class="example" markdown>

### Example 4: complete the square (finish it yourself)

*Theorem 4.* For all real numbers $x$ and $y$, $x^2 + xy + y^2 \ge 0$, with equality only when $x = y = 0$.

Scratch work. Try numbers: $x = 1$, $y = -1$ gives $1 - 1 + 1 = 1$; $x = 2$, $y = -1$ gives $4 - 2 + 1 = 3$. No small case gives a negative value. The expression has an $xy$ term that blocks an easy square, so treat it as a quadratic in $x$ and complete the square: $x^2 + xy = \left(x + \frac{y}{2}\right)^2 - \frac{y^2}{4}$. Substituting,

$$
x^2 + xy + y^2 = \left(x + \frac{y}{2}\right)^2 + \frac{3y^2}{4}.
$$

Now write the proof forward, and decide when equality holds.

<details class="solution" markdown>
<summary>Finish</summary>

*Proof.* Let $x$ and $y$ be real numbers. Expanding the right side shows that $\left(x + \frac{y}{2}\right)^2 + \frac{3y^2}{4} = x^2 + xy + \frac{y^2}{4} + \frac{3y^2}{4} = x^2 + xy + y^2$. A square is at least 0, and $\frac{3y^2}{4}$ is at least 0 because $y^2 \ge 0$. So the sum is at least 0.

For equality, both parts must be 0, since each is at least 0 and their sum is 0. From $\frac{3y^2}{4} = 0$ we get $y = 0$, and then $\left(x + 0\right)^2 = 0$ gives $x = 0$. $\blacksquare$

Check: $x = 1$ and $y = -1$ give $\left(1 - \frac{1}{2}\right)^2 + \frac{3}{4} = \frac{1}{4} + \frac{3}{4} = 1$, matching $1 - 1 + 1 = 1$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for handing in a backward argument. A student wants to prove $-1 = 1$ and writes: "Square both sides: $1 = 1$, which is true. So $-1 = 1$." The scratch step "$-1 = 1$ implies $1 = 1$" is valid, and the proof needs the opposite arrow, "$1 = 1$ implies $-1 = 1$", which is false. Squaring is not reversible, because $(-1)^2 = 1^2$ does not make $-1 = 1$. A backward proof is acceptable only when every step is an equivalence, and then you should say so. Otherwise rewrite it forward.

</div>

<div class="warning" markdown>

Watch out for proving a pattern from small cases. The table in Example 2 suggests the claim and proves nothing. The expression $n^2 + n + 41$ is prime for $n = 0, \dots, 39$ and fails at $n = 40$ ([what is a proof](../01-language-and-notation/01-what-is-a-proof.md#the-idea)). Use small cases to guess and to test, and prove the guess.

</div>

<div class="warning" markdown>

Watch out for starting with a clever trick. Searching for the clever step first usually wastes time. Unpack the definitions, write the givens and the goal, and the trick often turns out to be an ordinary substitution.

</div>

<div class="warning" markdown>

Watch out for working on a false claim. Before you spend an hour on a proof, spend two minutes on small cases. A counterexample ends the search at once, and it tells you what the true statement might be.

</div>

When the scratch work gets long, it has usually split into sub-claims (like "divisible by 2" and "divisible by 3" in Example 2). Give each one a name and prove it separately. A proof built from lemmas is easier to find and easier to read than a long unbroken chain.

## Tricks and shortcuts

Look for the equality case. If a numerical test shows an inequality is tight at some point, such as $x = 2$ in Example 1, the proof usually contains a square that vanishes there.

When the hypothesis and the conclusion talk about different things, look for a quantity both can reach. In Example 3 the hypotheses named $b$ and $b + c$ and the conclusion named $c$, and the quantity in common was the difference.

Write the first and last lines of the proof before the middle. The first line is "Let ..." plus the unpacked hypothesis, and the last is the target. The middle is the path between two fixed points, and a path is easier to search for than a destination.

If you are unsure whether a backward step is reversible, check it in the forward direction. Multiplying or dividing by a positive number is reversible, squaring is not, and taking a square root is reversible only for non-negative numbers.

## In code

A short script is a fast way to make the small-case table and to test a conjecture before spending time on a proof. These lines produce the table from Example 2, check the guess on a large range, and test two false guesses to show how counterexamples look.

<details class="code" markdown>
<summary>In code</summary>

```python
ns = range(-2, 7)
print([n**3 - n for n in ns])                        # [-6, 0, 0, 0, 6, 24, 60, 120, 210]
print(all((n**3 - n) % 6 == 0 for n in range(-1000, 1001)))   # True: supports the claim, proves nothing

# the minimum of x + 4/x over a grid of positive x
grid = [k / 100 for k in range(1, 1001)]
best = min(grid, key=lambda x: x + 4 / x)
print(best, best + 4 / best)                         # 2.0 4.0

# test two false guesses before trying to prove them
print([n for n in range(1, 30) if (n**2 - n) % 4 != 0][:5])       # [2, 3, 6, 7, 10]: n^2 - n is not always a multiple of 4
print([n for n in range(1, 30) if (n**3 + n) % 3 != 0][:5])       # [1, 2, 4, 5, 7]: n^3 + n is not always a multiple of 3
```

The first two lines support the theorem. The last two show how quickly a false guess fails, which is why two minutes of testing come before the proof.

</details>

## FAQ

### Do professionals also have scratch work this messy?

Yes. Published proofs are the polished final version. Most mathematicians fill pages with failed attempts before the argument that works. The skill you are learning is not avoiding the mess; it is keeping the mess on scratch paper and writing a clean proof after.

### How do I know which method to use?

Start with the shape table, then use the heuristics. If you don't know, try the direct route for five minutes. If the hypothesis gives you nothing to work with, or the conclusion is a negative statement, switch to the contrapositive or contradiction. It is normal to try two or three methods on one problem.

### Is it cheating to guess the answer from examples first?

No, and it is how most results are found. Examples tell you what is true, and the proof tells you why. The mistake is stopping at the examples.

### What if I try everything and still can't find the proof?

Check that the claim is true, by testing a wider range of cases. Then look for a hint in the shape: a "for every" over the integers often needs cases or induction, and an "exists" often needs a construction. If you are still stuck, ask for the first idea only, and do the rest yourself. Looking at a full solution before you have struggled costs you the learning.

## Practice

### Warm-up

1\. State the shape of each claim and the first sentence of a proof. (a) For every integer $n$, the number $2n + 1$ is odd. (b) There is a real number $x$ with $x^2 - 2x - 3 = 0$. (c) If $x > 0$, then $\frac{x}{x^2 + 1} \le \frac{1}{2}$. (d) The number $\sqrt{3}$ is irrational.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) "For every": "Let $n$ be an integer." The proof then shows $2n + 1$ has the form $2k + 1$ with $k = n$.
- (b) "There exists": "Take $x = 3$." The proof then checks $9 - 6 - 3 = 0$.
- (c) "If-then": "Suppose $x > 0$." The proof then shows the inequality (scratch: it is equivalent to $2x \le x^2 + 1$, that is $(x - 1)^2 \ge 0$).
- (d) A negative statement ("not rational"): "Suppose, for contradiction, that $\sqrt{3}$ is rational."

Check: $x = -1$ is also a root in (b), since $1 + 2 - 3 = 0$, so the witness is not unique, which is fine for an "exists".

</details>

2\. Compute the sum $1 + 3 + 5 + \dots + (2n - 1)$ of the first $n$ odd numbers for $n = 1, 2, 3, 4, 5, 6$, and guess a formula. Is your guess proved?

<details class="solution" markdown>
<summary>Solution</summary>

The sums are $1, 4, 9, 16, 25, 36$. These are the perfect squares, so the guess is $n^2$.

It is not proved: six cases support the pattern and don't establish it for every $n$. [A proof by induction](../05-induction/01-mathematical-induction.md) is the standard tool.

Check: for $n = 6$, $1 + 3 + 5 + 7 + 9 + 11 = 36 = 6^2$.

</details>

3\. A student wants to prove that if $x^2 > 9$ then $x > 3$. Scratch work: "$x > 3$ gives $x^2 > 9$, which is the hypothesis. So we are done." What is wrong, and is the claim true?

<details class="solution" markdown>
<summary>Solution</summary>

The argument runs the wrong way. It shows "$x > 3$ implies $x^2 > 9$", which is the converse of the claim. The claim needs "$x^2 > 9$ implies $x > 3$".

The claim is false: $x = -4$ has $x^2 = 16 > 9$ and $x = -4 < 3$. The correct statement is "if $x^2 > 9$, then $x > 3$ or $x < -3$".

Check: $(-4)^2 = 16 > 9$.

</details>

### Standard

4\. Prove that $x^2 - 4x + 5 > 0$ for every real number $x$.

<details class="solution" markdown>
<summary>Solution</summary>

Scratch: complete the square. $x^2 - 4x + 5 = (x - 2)^2 + 1$. A square is at least 0, so the whole is at least 1.

What we know: squares are not negative. What we want: $x^2 - 4x + 5 > 0$. The plan: rewrite as $(x - 2)^2 + 1$.

*Proof.* Let $x$ be a real number. Then $(x - 2)^2 + 1 = x^2 - 4x + 4 + 1 = x^2 - 4x + 5$. Since $(x - 2)^2 \ge 0$, we have $x^2 - 4x + 5 \ge 1 > 0$. $\blacksquare$

Check: $x = 2$ gives $4 - 8 + 5 = 1$, the smallest value, and $x = 0$ gives 5.

</details>

5\. Prove that $x^2 + y^2 + 1 \ge x + y$ for all real numbers $x$ and $y$.

<details class="solution" markdown>
<summary>Solution</summary>

Scratch: move everything to one side, $x^2 - x + y^2 - y + 1 \ge 0$. Complete the square in each variable: $x^2 - x = \left(x - \frac{1}{2}\right)^2 - \frac{1}{4}$, and the same for $y$. So the left side is $\left(x - \frac{1}{2}\right)^2 + \left(y - \frac{1}{2}\right)^2 + \frac{1}{2}$.

*Proof.* Let $x$ and $y$ be real. Then

$$
x^2 + y^2 + 1 - (x + y) = \left(x - \tfrac{1}{2}\right)^2 + \left(y - \tfrac{1}{2}\right)^2 + \tfrac{1}{2},
$$

(expand the right side to check: $x^2 - x + \frac{1}{4} + y^2 - y + \frac{1}{4} + \frac{1}{2}$). Both squares are at least 0, so the right side is at least $\frac{1}{2} > 0$. Hence $x^2 + y^2 + 1 > x + y$, and in particular $\ge$. $\blacksquare$

Look back: we proved the strict inequality, which is more than asked. Check: $x = y = \frac{1}{2}$ gives $\frac{1}{4} + \frac{1}{4} + 1 = 1.5$ against $x + y = 1$, a gap of $0.5$.

</details>

6\. The backward argument "$-1 = 1 \Rightarrow 1 = 1$" fails as a proof. Here is a case where the same pattern works. Prove: if $a$ and $b$ are non-negative real numbers and $a^2 = b^2$, then $a = b$. State where non-negativity is used.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $a, b \ge 0$ and $a^2 = b^2$. What we want: $a = b$. The plan: move to one side and factor, $a^2 - b^2 = (a - b)(a + b) = 0$.

*Proof.* Let $a, b \ge 0$ with $a^2 = b^2$. Then $(a - b)(a + b) = a^2 - b^2 = 0$. A product of two real numbers is 0 only if one of them is 0. If $a - b = 0$, then $a = b$. If $a + b = 0$, then since $a \ge 0$ and $b \ge 0$, both must be 0 (a sum of two non-negative numbers is 0 only when both are 0), so again $a = b$. $\blacksquare$

Non-negativity is used in the second case. Without it the claim is false: $a = -1$ and $b = 1$ satisfy $a^2 = b^2$, and $a + b = 0$ with $a \ne b$. That is exactly the failure in the $-1 = 1$ argument.

Check: $a = 3$ and $b = 3$ satisfy $9 = 9$, and the first case applies.

</details>

### Challenge

7\. Prove that $n^5 - n$ is divisible by 5 for every integer $n$.

<details class="solution" markdown>
<summary>Solution</summary>

Scratch: small cases give $n^5 - n = 0, 0, 30, 240, 1020, 3120$ for $n = 0, \dots, 5$, all multiples of 5. Factor: $n^5 - n = n(n^4 - 1) = n(n - 1)(n + 1)(n^2 + 1)$. Every integer is $5q + r$ with $r \in \{0, 1, 2, 3, 4\}$, so check five cases and find the factor divisible by 5 in each.

*Proof.* Let $n$ be an integer, and write $n = 5q + r$ with $r \in \{0, 1, 2, 3, 4\}$. We have $n^5 - n = n(n - 1)(n + 1)(n^2 + 1)$.

- If $r = 0$, then $5 \mid n$.
- If $r = 1$, then $n - 1 = 5q$, so $5 \mid n - 1$.
- If $r = 4$, then $n + 1 = 5q + 5 = 5(q + 1)$, so $5 \mid n + 1$.
- If $r = 2$, then $n^2 + 1 = 25q^2 + 20q + 5 = 5(5q^2 + 4q + 1)$.
- If $r = 3$, then $n^2 + 1 = 25q^2 + 30q + 10 = 5(5q^2 + 6q + 2)$.

In each case 5 divides one factor of the product, so 5 divides $n^5 - n$ by Lemma 2 of [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#building-on-lemmas). $\blacksquare$

Check: $n = 7 = 5 \cdot 1 + 2$ gives $n^5 - n = 16807 - 7 = 16800 = 5 \cdot 3360$, and $n^2 + 1 = 50 = 5 \cdot 10$.

</details>

8\. (Reviews [inequalities](../../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md).) Prove that if $0 < a < b$, then $\frac{1}{b} < \frac{1}{a}$. Do the scratch work first, and say which steps are reversible.

<details class="solution" markdown>
<summary>Solution</summary>

Scratch, backward: $\frac{1}{b} < \frac{1}{a}$. Multiply both sides by $ab$, which is positive, so the direction stays: $a < b$. That is the hypothesis. The multiplication is reversible because $ab > 0$.

What we know: $0 < a < b$, so $ab > 0$. What we want: $\frac{1}{b} < \frac{1}{a}$. The plan: start from $a < b$ and divide by the positive number $ab$.

*Proof.* Let $0 < a < b$. Then $ab > 0$, so $\frac{1}{ab} > 0$. Multiplying both sides of $a < b$ by $\frac{1}{ab}$ keeps the direction, and gives $\frac{a}{ab} < \frac{b}{ab}$, that is, $\frac{1}{b} < \frac{1}{a}$. $\blacksquare$

Look back: positivity of $a$ and $b$ is used for the sign of $ab$. If $a < 0 < b$, then $\frac{1}{a} < 0 < \frac{1}{b}$, and the conclusion reverses. Check: $a = 2$ and $b = 5$ give $\frac{1}{5} = 0.2 < 0.5 = \frac{1}{2}$.

</details>

## Where this shows up

- The next lessons use these moves on specific methods: [proof by cases and WLOG](04-proof-by-cases-and-wlog.md) for the three-way split in Example 2, and [contrapositive proof](05-contrapositive-proof.md) and [proof by contradiction](06-proof-by-contradiction.md) for the "stuck" move of changing the method. [Counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md) covers the case where small cases kill the claim.
- In CS, finding an invariant or a loop bound is scratch work of the same kind: trace small inputs, guess what stays true, and then prove it ([invariants and algorithm correctness](../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md)). Debugging is the same cycle of hypothesis, test and fix.
- In economics, optimization results start with a guess about where the maximum is, and the proof shows the guess is right by completing a square, as in the revenue example of [what is a proof](../01-language-and-notation/01-what-is-a-proof.md#worked-examples) ([profit maximization and market structure](../../07-economics-math/03-firms-and-consumers/03-profit-maximization-and-market-structure.md)).
