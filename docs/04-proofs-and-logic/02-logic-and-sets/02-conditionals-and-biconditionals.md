# Conditionals and biconditionals

After this lesson you can build the truth table of "if $P$, then $Q$", explain why it is true when $P$ is false, rewrite each English form of a conditional ("only if", "sufficient", "necessary", "whenever", "unless") in standard form, write the converse, inverse and contrapositive and say which are equivalent, and handle "if and only if".

Before this: [statements and connectives](01-statements-and-connectives.md) (truth tables for not, and, or), and [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements), where you met the hypothesis, the conclusion, the converse and the contrapositive without a truth table. This lesson supplies the table and goes deeper.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Is "If $2 > 3$, then 5 is even" true or false?
2. Write the converse and the contrapositive of "If $n$ is divisible by 4, then $n$ is even". Which of the original, the converse and the contrapositive are true?
3. Rewrite "You can enter only if you have a ticket" in the form "if ..., then ...".

<details class="solution" markdown>
<summary>Answers</summary>

1. True. The hypothesis "$2 > 3$" is false, and a conditional with a false hypothesis is true (it is true vacuously).
2. Converse: "If $n$ is even, then $n$ is divisible by 4". Contrapositive: "If $n$ is not even, then $n$ is not divisible by 4". The original is true and so is its contrapositive. The converse is false: $n = 2$ is even and is not divisible by 4.
3. "If you can enter, then you have a ticket." What follows "only if" is the conclusion.

</details>

## The idea

A professor announces: "If you hand in the project, you will get at least a pass." When has the professor broken the promise? Look at the four things that can happen.

| You hand in the project | You get at least a pass | Was the promise broken? |
|---|---|---|
| yes | yes | no |
| yes | no | yes |
| no | yes | no |
| no | no | no |

Only the second row breaks it: you handed in the project and still failed. In the third row, the professor may have been generous. In the fourth, the promise says nothing at all about students who don't hand in the project, so it can't have been broken. A promise is broken only when its condition is met and its result fails to follow.

That is exactly how mathematics defines "if $P$, then $Q$": it is false in the one case where $P$ is true and $Q$ is false, and true in the other three. The odd rows are the ones where $P$ is false. They look strange at first, because in everyday speech an "if" suggests that something is going on between $P$ and $Q$. The mathematical conditional doesn't care whether there is a connection. It only forbids one combination of truth values. The reason this is the right choice, and not just a convention, is that it makes statements like "every multiple of 4 is even" mean what we want: no number can be a counterexample unless it is a multiple of 4 and is not even.

## Definitions

### The conditional

Let $P$ and $Q$ be statements. The **conditional** statement $P \Rightarrow Q$ (read "$P$ implies $Q$" or "if $P$, then $Q$") is false when $P$ is true and $Q$ is false, and true in every other case.

| $P$ | $Q$ | $P \Rightarrow Q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

The statement $P$ is the **hypothesis** (or **antecedent**), and $Q$ is the **conclusion** (or **consequent**). In plain words, $P \Rightarrow Q$ promises that whenever $P$ holds, $Q$ holds too, and it is broken only by a case where $P$ holds and $Q$ doesn't.

When $P$ is false, $P \Rightarrow Q$ is true whatever $Q$ is, and we say it is **vacuously true**. The statement "If $2 > 3$, then every cat can fly" is vacuously true, and so is "If $1 = 2$, then $1 = 3$". Vacuous truth is not a trick. It is the same reason that the empty set is a subset of every set, as in [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#why-is-the-empty-set-a-subset-of-every-set): there is no case that could break the claim.

### Many ways to say $P \Rightarrow Q$

Mathematics has many ways to say the same conditional, and textbooks switch among them freely. Each row of this table says $P \Rightarrow Q$.

| Wording | Example with $P$ = "$n$ is divisible by 8", $Q$ = "$n$ is divisible by 4" |
|---|---|
| If $P$, then $Q$ | If $n$ is divisible by 8, then $n$ is divisible by 4. |
| $Q$ if $P$ | $n$ is divisible by 4 if $n$ is divisible by 8. |
| $P$ implies $Q$ | $n$ divisible by 8 implies $n$ divisible by 4. |
| $Q$ whenever $P$ | $n$ is divisible by 4 whenever it is divisible by 8. |
| $P$ only if $Q$ | $n$ is divisible by 8 only if it is divisible by 4. |
| $P$ is sufficient for $Q$ | Divisibility by 8 is sufficient for divisibility by 4. |
| $Q$ is necessary for $P$ | Divisibility by 4 is necessary for divisibility by 8. |
| $Q$ follows from $P$ | That $n$ is divisible by 4 follows from $n$ being divisible by 8. |

Two rows cause nearly all the trouble. "$P$ only if $Q$" says $P \Rightarrow Q$, not $Q \Rightarrow P$: whatever follows "only if" is the conclusion. And "$Q$ if $P$" puts the conclusion first, so the hypothesis is the part after "if". A quick way to keep them apart is to remember that "if" introduces the hypothesis and "only if" introduces the conclusion.

"Sufficient" and "necessary" are two views of the same arrow. If $P \Rightarrow Q$, then $P$ is enough to guarantee $Q$ (sufficient), and $Q$ can't be missing when $P$ holds (necessary). The condition at the tail of the arrow is the sufficient one; the condition at the head is the necessary one.

The word "unless" needs care. "$P$ unless $Q$" is read as $\neg Q \Rightarrow P$: if $Q$ doesn't happen, then $P$. For instance, "You will miss the bus unless you run" is "If you don't run, you will miss the bus". In ordinary speech, people also hear the reverse ("if you run, you will catch it"). Mathematical usage keeps only the one direction.

### Converse, inverse and contrapositive

Starting from $P \Rightarrow Q$, three related conditionals can be formed.

| Name | Form | Example from "If $x > 4$, then $x^2 > 16$" |
|---|---|---|
| the original | $P \Rightarrow Q$ | If $x > 4$, then $x^2 > 16$. True. |
| the **converse** | $Q \Rightarrow P$ | If $x^2 > 16$, then $x > 4$. False: $x = -5$. |
| the **inverse** | $\neg P \Rightarrow \neg Q$ | If $x \le 4$, then $x^2 \le 16$. False: $x = -5$. |
| the **contrapositive** | $\neg Q \Rightarrow \neg P$ | If $x^2 \le 16$, then $x \le 4$. True. |

Here $\neg(x > 4)$ is $x \le 4$ and $\neg(x^2 > 16)$ is $x^2 \le 16$. Put the four conditionals in one truth table:

| $P$ | $Q$ | $P \Rightarrow Q$ | $Q \Rightarrow P$ | $\neg P \Rightarrow \neg Q$ | $\neg Q \Rightarrow \neg P$ |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | F | F | T | T | F |
| F | T | T | F | F | T |
| F | F | T | T | T | T |

Read the columns. The original and the contrapositive agree in every row, and the converse and the inverse agree in every row. So a conditional and its contrapositive are interchangeable, and a conditional and its converse are not. Two statements that agree in every row are logically equivalent, a notion that [truth tables and logical equivalence](03-truth-tables-and-logical-equivalence.md) makes precise.

In plain words, "every dog is a mammal" and "anything that isn't a mammal isn't a dog" say the same thing. But "every dog is a mammal" does not say "every mammal is a dog". Confusing a conditional with its converse is the most common logical error in a first proof course. It has a name, the fallacy of affirming the consequent, and the next section lists it among the mistakes.

### The biconditional

The **biconditional** $P \Leftrightarrow Q$ (read "$P$ if and only if $Q$", often shortened to "$P$ iff $Q$") is true when $P$ and $Q$ have the same truth value, and false when they differ.

| $P$ | $Q$ | $P \Leftrightarrow Q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

Compare with the table above: the column is T, F, F, T, which is the column of $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$. In plain words, "$P$ if and only if $Q$" packs two statements into one: "$P$ if $Q$" (that is, $Q \Rightarrow P$) and "$P$ only if $Q$" (that is, $P \Rightarrow Q$). So $P$ is both necessary and sufficient for $Q$, and each one implies the other.

Definitions are biconditionals, even when they are written with a plain "if". The definition "an integer is even if it is $2k$ for some integer $k$" means "if and only if", as the geometry lesson noted for midpoints. A theorem that is a biconditional needs a proof in two directions, which is the subject of [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md).

## How to do it

### Putting a conditional in standard form

1. Find the two parts of the sentence and name them with letters, each a complete statement.
2. Decide which one is the hypothesis, using the table of wordings: the part after "if" or "whenever", the part before "only if", "implies" or "is sufficient for", and the part after "is necessary for".
3. Write it as "if $P$, then $Q$".
4. Ask what would break it. A claim "if $P$, then $Q$" is broken by a case with $P$ true and $Q$ false. If that is not what the original sentence forbids, you swapped the parts.

A sentence with no "if" in it can hide a conditional: "Primes greater than 2 are odd" is "if $p$ is a prime greater than 2, then $p$ is odd". Ask what you are given (the hypothesis) and what you are told is true about it (the conclusion).

### Forming the converse, inverse and contrapositive

1. Put the original in standard form, "if $P$, then $Q$".
2. Converse: swap the two parts, "if $Q$, then $P$".
3. Inverse: negate both parts without swapping, "if not $P$, then not $Q$".
4. Contrapositive: swap and negate, "if not $Q$, then not $P$".
5. Negate carefully. The negation of "$x > 4$" is "$x \le 4$", and the negation of "all" is "not all" (the full rules are in [negation and translating English](05-negation-and-translating-english.md)).
6. Decide each truth value, using one counterexample for a false conditional. The contrapositive has the value of the original, and the inverse has the value of the converse, so you only need to decide two.

## Worked examples

<div class="example" markdown>

### Example 1: all the forms of one conditional

Take "A number is divisible by 6 only if it is even". Put it in standard form and write the converse, inverse and contrapositive. Decide which are true. (The numbers are integers.)

Step 1: the parts are $P$ = "$n$ is divisible by 6" and $Q$ = "$n$ is even". Step 2: "only if" introduces the conclusion, so $Q$ is the conclusion. Step 3: the standard form is "If $n$ is divisible by 6, then $n$ is even". Step 4: this would be broken by a multiple of 6 that is odd, and there is none, because $n = 6k = 2(3k)$ is even. The statement is true.

Converse (swap the parts): "If $n$ is even, then $n$ is divisible by 6." False, since $n = 4$ is even and $4 = 6 \cdot \frac{2}{3}$ is not a multiple of 6.

Inverse: "If $n$ is not divisible by 6, then $n$ is odd." False, for the same $n = 4$: it isn't divisible by 6 and it is not odd.

Contrapositive: "If $n$ is odd, then $n$ is not divisible by 6." True. This is the original in different clothes: an odd number can't be a multiple of 6.

Check the pairing: the original and the contrapositive are both true, and the converse and the inverse are both false, as the table says they must be.

</div>

<div class="example" markdown>

### Example 2: truth values, including vacuous ones

Find the truth value of (a) "If $2 + 2 = 5$, then 3 is even." (b) "If 3 is odd, then $2 + 2 = 5$." (c) "If $2 + 2 = 5$, then 3 is odd." (d) "If 7 is prime, then 9 is prime."

Look up the hypothesis and conclusion in the table for $P \Rightarrow Q$.

(a) $P$ is F ($2 + 2 = 4$) and $Q$ is F. The row F, F gives T. The conditional is vacuously true.

(b) $P$ is T and $Q$ is F. This is the one false row, so the conditional is F.

(c) $P$ is F and $Q$ is T. The row F, T gives T, again vacuously.

(d) $P$ is T (7 is prime) and $Q$ is F ($9 = 3^2$). The conditional is F.

Check (a) and (c) against the promise analogy: the professor's promise isn't broken when nobody hands in the project. The two false conditionals, (b) and (d), are the ones where the hypothesis is satisfied and the conclusion fails.

</div>

<div class="example" markdown>

### Example 3: "unless" and "only if" in real sentences

Translate (a) "The build fails unless every test passes." (b) "Free shipping applies only if the order is over \$50."

(a) The word "unless" gives $\neg Q \Rightarrow P$. Let $T$ be "every test passes" and $F$ be "the build fails". Then the sentence is $\neg T \Rightarrow F$: if some test fails, the build fails. It doesn't claim that a build with every test passing succeeds, since it may fail for another reason. Using the table, $\neg T \Rightarrow F$ has the same truth values as $T \vee F$: "either every test passes or the build fails".

(b) "Only if" introduces the conclusion. Let $S$ be "free shipping applies" and $O$ be "the order is over \$50". The sentence is $S \Rightarrow O$: if you got free shipping, the order was over \$50. It does not say that an order over \$50 gets free shipping. A \$60 order may still pay for shipping, because other conditions can apply, and that would not contradict the sentence.

Check (b) by asking what breaks it: an order of \$30 that got free shipping breaks $S \Rightarrow O$, and a \$60 order that paid for shipping does not.

</div>

<div class="example" markdown>

### Example 4: sufficient and necessary (finish it yourself)

Let $P$ be "$n$ is divisible by 8" and $Q$ be "$n$ is divisible by 4", for an integer $n$. We know $P \Rightarrow Q$. Complete each sentence with "sufficient", "necessary", or "both", and decide whether $P \Leftrightarrow Q$.

(a) Divisibility by 8 is ___ for divisibility by 4.
(b) Divisibility by 4 is ___ for divisibility by 8.

Hint: the condition at the tail of the arrow $P \Rightarrow Q$ is the sufficient one. Then look for a number that is divisible by 4 and not by 8 to see whether the converse holds.

<details class="solution" markdown>
<summary>Finish</summary>

(a) Sufficient: if $n$ is divisible by 8, then $n = 8k = 4(2k)$ is divisible by 4. Divisibility by 8 isn't necessary for divisibility by 4, because $n = 4$ is divisible by 4 and not by 8.

(b) Necessary: a number that is not divisible by 4 can't be divisible by 8 (the contrapositive of $P \Rightarrow Q$). Divisibility by 4 isn't sufficient, again because $n = 4$.

So $P$ is sufficient but not necessary, $Q$ is necessary but not sufficient, and $P \Leftrightarrow Q$ is false, because $n = 4$ makes $Q$ true and $P$ false.

Check: $n = 16$ is divisible by 8 and by 4, $n = 4$ is divisible by 4 only, and $n = 6$ is divisible by neither. No $n$ is divisible by 8 and not by 4, which is what $P \Rightarrow Q$ says.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the converse. From "if it rains, the ground is wet" and "the ground is wet" you can't conclude "it rained": a sprinkler works too. Reasoning from $P \Rightarrow Q$ and $Q$ to $P$ is the fallacy of affirming the consequent. What you can conclude is the contrapositive: from "the ground is dry" you may conclude "it did not rain".

</div>

<div class="warning" markdown>

Watch out for the inverse. From $P \Rightarrow Q$ and $\neg P$, you can't conclude $\neg Q$ (the fallacy of denying the antecedent). "If a number is divisible by 6, it is even" and "this number isn't divisible by 6" tell you nothing about whether it is even: 4 isn't divisible by 6 and is even.

</div>

<div class="warning" markdown>

Watch out: "only if" does not reverse. "You pass only if you hand in the project" is the same as "if you pass, then you handed in the project", and not "if you hand in the project, you pass". A reliable test is to ask what would make the speaker a liar. Someone who handed in the project and failed didn't make the speaker a liar. A student who passed without handing it in did.

</div>

<div class="warning" markdown>

Watch out for reading "if" as "if and only if" in a theorem. In everyday speech, "I'll pay you if you mow the lawn" often means that you get paid exactly when you mow. A theorem that says "if $P$, then $Q$" claims only one direction. The exception is a definition, which is a biconditional even when it is written with "if".

</div>

A false hypothesis can seem to make a conditional meaningless, which is why the vacuous cases confuse people. They are rarely the point of a proof, but they make general statements work. The claim "every element of $\emptyset$ is greater than 5" is true, and it has the form "for every $x$, if $x \in \emptyset$, then $x > 5$". The hypothesis $x \in \emptyset$ is false for every $x$, so every instance holds vacuously.

Also, $P \Rightarrow Q$ is not about cause. "If $2 + 2 = 4$, then Toronto is in Ontario" is a true conditional (T, T) even though one fact has nothing to do with the other. In proofs the conditionals that matter are the ones where the hypothesis really does lead to the conclusion, and the proof is what shows it.

## Tricks and shortcuts

To remember the one false row, say it as the promise: a conditional is false only when the hypothesis is true and the conclusion is false. To evaluate a conditional quickly, look at the conclusion first. If it is true, the conditional is true. Otherwise look at the hypothesis: if it is false, the conditional is true, and if it is true, the conditional is false.

To decide whether something is necessary or sufficient, test it with a boundary example. Condition $A$ is sufficient for $B$ if every case with $A$ also has $B$. Condition $A$ is necessary for $B$ if every case with $B$ also has $A$. "Winning the lottery is sufficient for having money, and not necessary", because you can have money without winning.

A conditional $P \Rightarrow Q$ can be restated without a symbol as $\neg P \vee Q$: "either $P$ fails or $Q$ holds". The next lesson proves this. It is useful in code, and it is how you check a conditional on a list of cases: every case must either fail $P$ or satisfy $Q$.

### Necessary and sufficient in CS and economics

A program that is correct must pass its test suite, so passing the tests is necessary for correctness. It is not sufficient: a suite can miss a case. In symbols, "correct $\Rightarrow$ passes the tests", and the converse is false. Edsger Dijkstra's remark that testing shows the presence of bugs and never their absence is this fact. What a test does prove is the contrapositive: "fails a test $\Rightarrow$ not correct".

In calculus, if a function has a maximum or minimum at an interior point $c$ and is differentiable there, then $f'(c) = 0$. So $f'(c) = 0$ is necessary for an interior extremum, but not sufficient: $f(x) = x^3$ has $f'(0) = 0$ and no extremum at 0. This is why [optimization](../../05-university-core/03-applications-of-derivatives/05-optimization.md) checks the critical points instead of stopping at them.

In economics, every Giffen good (a good whose quantity demanded rises when its price rises) is an inferior good (one that people buy less of when their income rises), but most inferior goods are not Giffen goods. So being inferior is necessary for being a Giffen good and not sufficient, which is the same pattern as "tests pass" and "correct".

## In code

On booleans, $P \Rightarrow Q$ is `not p or q`, which is the rewrite from the previous section. Python's comparison operator `<=` also works as implication on `True` and `False`, because `False < True`.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import product

def implies(p, q):
    return (not p) or q

print("P      Q      P=>Q   Q=>P   iff")
for p, q in product([True, False], repeat=2):
    print(p, q, implies(p, q), implies(q, p), p == q)

# the contrapositive always agrees with the original, the converse does not
rows = list(product([True, False], repeat=2))
print(all(implies(p, q) == implies(not q, not p) for p, q in rows))   # True
print(all(implies(p, q) == implies(q, p) for p, q in rows))           # False

# checking "if n is divisible by 8, then n is divisible by 4" on 1..200
print(all(implies(n % 8 == 0, n % 4 == 0) for n in range(1, 201)))    # True
print(all(implies(n % 4 == 0, n % 8 == 0) for n in range(1, 201)))    # False
print([n for n in range(1, 201) if not implies(n % 4 == 0, n % 8 == 0)][:3])  # [4, 12, 20]

print(all(implies(x > 5, x > 100) for x in []))   # True: no cases, so no counterexample
print(False <= True, True <= False)               # True False
```

The first table reproduces the tables above, with `p == q` as the biconditional. The two `all` lines over four rows say that the contrapositive always agrees with the original and the converse does not. The tests on the range 1 to 200 are a search for counterexamples: the first conditional has none, and the converse fails at 4, 12, 20 and so on (multiples of 4 that are not multiples of 8). A passing check on 200 cases is evidence and not a proof; the proof was the one-line argument $8k = 4(2k)$. The empty list shows vacuous truth in code: `all` of nothing is `True`.

</details>

## FAQ

### Why is "false implies true" true?

Because the conditional only forbids one case, and a false hypothesis is not that case. There is also a test you can run. We want "for every integer $n$, if $n > 3$, then $n > 2$" to be true, since it plainly is. Try $n = 1$: the hypothesis is false and the conclusion is false. Try $n = 3$: the hypothesis is false and the conclusion is true. Try $n = 4$: both are true. For the sentence to hold for every $n$, the conditional must be true in all three cases, so "false implies false" and "false implies true" must both be true. If either were false, a plain sentence like this one would fail.

### Does "if $P$, then $Q$" say that $P$ causes $Q$?

No. Logic checks only the truth values. "If $2 + 2 = 4$, then Toronto is in Ontario" is true, and a useless thing to say. Theorems of the form "if $P$, then $Q$" are interesting because the proof finds a reason that $P$ leads to $Q$, and the reason is the content. Cause and effect belong to the real world, not to the connective.

### Is "if" in a definition really "if and only if"?

Yes, by convention. When a book says "a number is called even if it is twice an integer", it means that the numbers twice an integer are even and those are the only ones. Otherwise, the definition would leave open whether 7 is even. In a theorem, the same word "if" means one direction only, so read each case on its own. When the direction matters, a careful author writes "if and only if" or "iff".

### Why is the contrapositive worth so much attention?

Because a statement can be hard to prove as it stands and easy to prove through its contrapositive. To prove "if $n^2$ is even, then $n$ is even", it is simpler to assume $n$ is odd and show $n^2$ is odd. The two proofs are equivalent as a matter of logic, and [contrapositive proof](../03-core-proof-methods/05-contrapositive-proof.md) builds on the table in this lesson.

## Practice

### Warm-up

1\. Find the truth value of each. (a) If $4$ is even, then $4 > 3$. (b) If $4 > 3$, then $4$ is odd. (c) If $4 < 3$, then $4$ is odd. (d) If $4 < 3$, then $4$ is even.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) T, T gives T.
- (b) T, F gives F.
- (c) The hypothesis is false, so the conditional is T (vacuously).
- (d) The hypothesis is false, so the conditional is T (vacuously).

Check: only (b) has a true hypothesis and a false conclusion, and that is the only false conditional.

</details>

2\. Rewrite each as "if ..., then ...". (a) A triangle is equilateral only if it is isosceles. (b) Being a square is sufficient for being a rectangle. (c) A sequence is bounded whenever it converges. (d) Having a valid ticket is necessary for entering. (e) Rectangles with equal sides are squares.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) "Only if" introduces the conclusion: if a triangle is equilateral, then it is isosceles.
- (b) The sufficient condition is the hypothesis: if a shape is a square, then it is a rectangle.
- (c) "Whenever" introduces the hypothesis: if a sequence converges, then it is bounded.
- (d) The necessary condition is the conclusion: if you enter, then you have a valid ticket.
- (e) The sentence hides the "if": if a rectangle has equal sides, then it is a square.

Check each by asking what would break it. For (a) it would be an equilateral triangle that is not isosceles, which doesn't exist, since all three of its sides are equal. For (d) it would be a person who got in without a ticket.

</details>

3\. For "If $n$ is divisible by 10, then $n$ is divisible by 5" (integers), write the converse, inverse and contrapositive, and give the truth value of all four statements.

<details class="solution" markdown>
<summary>Solution</summary>

- The original is true: $n = 10k = 5(2k)$.
- The converse, "If $n$ is divisible by 5, then $n$ is divisible by 10", is false: $n = 15$.
- The inverse, "If $n$ is not divisible by 10, then $n$ is not divisible by 5", is false for the same $n = 15$.
- The contrapositive, "If $n$ is not divisible by 5, then $n$ is not divisible by 10", is true.

Check: the original and the contrapositive agree (both T), and the converse and the inverse agree (both F).

</details>

### Standard

4\. Build the truth table of $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$ and compare it with the column of $P \Leftrightarrow Q$.

<details class="solution" markdown>
<summary>Solution</summary>

| $P$ | $Q$ | $P \Rightarrow Q$ | $Q \Rightarrow P$ | $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$ | $P \Leftrightarrow Q$ |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | F | F | T | F | F |
| F | T | T | F | F | F |
| F | F | T | T | T | T |

The two last columns are identical (T, F, F, T), so the biconditional says the same as the two conditionals together.

Check: $P \Leftrightarrow Q$ should be true exactly when $P$ and $Q$ have the same truth value, and that is the first and last rows.

</details>

5\. Decide which statements are true. (a) Being in Toronto is sufficient for being in Ontario. (b) Being in Ontario is sufficient for being in Toronto. (c) Being in Ontario is necessary for being in Toronto. (d) Being in Toronto is necessary for being in Ontario. (e) For a program, is passing all its unit tests sufficient for being correct, necessary, both or neither?

<details class="solution" markdown>
<summary>Solution</summary>

Write $T$ for "in Toronto" and $O$ for "in Ontario". Then $T \Rightarrow O$ is true and $O \Rightarrow T$ is false (Ottawa).

- (a) True, since "sufficient for" follows the arrow $T \Rightarrow O$.
- (b) False: Ottawa is a counterexample.
- (c) True: "Ontario is necessary for Toronto" is $T \Rightarrow O$ again.
- (d) False, for the same reason as (b).
- (e) Passing all the tests is necessary for correctness (a correct program passes its tests) and not sufficient (a suite can miss a bug).

Check (a) and (c): they are two wordings of the same conditional, so they must have the same truth value, and they do. So do (b) and (d).

</details>

6\. Use a truth table to show that $(P \Rightarrow Q) \wedge (P \Rightarrow \neg Q)$ has the same truth values as $\neg P$.

<details class="solution" markdown>
<summary>Solution</summary>

| $P$ | $Q$ | $\neg Q$ | $P \Rightarrow Q$ | $P \Rightarrow \neg Q$ | $(P \Rightarrow Q) \wedge (P \Rightarrow \neg Q)$ | $\neg P$ |
|---|---|---|---|---|---|---|
| T | T | F | T | F | F | F |
| T | F | T | F | T | F | F |
| F | T | F | T | T | T | T |
| F | F | T | T | T | T | T |

The two last columns agree in every row, so they have the same truth values.

In words: if $P$ led to both $Q$ and not $Q$, then $P$ could only be false. This is the logic behind proof by contradiction. Check row 1: if $P$ is true, one of the two conditionals has a true hypothesis and a false conclusion, so the "and" is false, matching $\neg P$ being false.

</details>

### Challenge

7\. Prove that for an integer $n$, $n$ is even if and only if $n^2$ is even. Write the proof of each direction. (An integer is even if it is $2k$ for some integer $k$, and odd if it is $2k + 1$.)

<details class="solution" markdown>
<summary>Solution</summary>

A biconditional needs two conditionals: ($\Rightarrow$) if $n$ is even, then $n^2$ is even, and ($\Leftarrow$) if $n^2$ is even, then $n$ is even.

What we know for ($\Rightarrow$): $n = 2k$ for some integer $k$. We want $n^2 = 2m$ for some integer $m$. Plan: square and factor out a 2. Proof: $n^2 = (2k)^2 = 4k^2 = 2(2k^2)$, and $2k^2$ is an integer, so $n^2$ is even.

For ($\Leftarrow$), a direct approach is awkward, because knowing $n^2 = 2m$ doesn't hand us a formula for $n$. We use the contrapositive instead: "if $n$ is not even, then $n^2$ is not even", and an integer that isn't even is odd. Suppose $n = 2k + 1$. Then $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$, and $2k^2 + 2k$ is an integer, so $n^2$ is odd. Since the contrapositive is true, so is the original: if $n^2$ is even, then $n$ is even. Together the two directions give the biconditional. $\blacksquare$

Look back: the second direction was a proof of the contrapositive, and it is valid because a conditional and its contrapositive have the same truth table. Check with numbers: $n = 6$ gives $36$ (even, even), $n = 7$ gives $49$ (odd, odd). No integer pairs an even $n$ with an odd $n^2$ or an odd $n$ with an even $n^2$.

</details>

8\. (Reviews [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md).) The statement "If $x^2 > 9$, then $x > 3$" appeared in that lesson as false. Write its converse, inverse and contrapositive, decide the truth value of each, and say which pairs agree.

<details class="solution" markdown>
<summary>Solution</summary>

The original is false: $x = -4$ has $x^2 = 16 > 9$, and $-4$ is not greater than 3.

- Converse: "If $x > 3$, then $x^2 > 9$." True: when $x > 3$, then $x \cdot x > 3 \cdot 3$ because both factors are positive and bigger than 3.
- Inverse: "If $x^2 \le 9$, then $x \le 3$." True: $x^2 \le 9$ means $-3 \le x \le 3$.
- Contrapositive: "If $x \le 3$, then $x^2 \le 9$." False: $x = -4$ has $x \le 3$ and $x^2 = 16$.

The original and the contrapositive are both false, and the converse and the inverse are both true, so the pairs agree as the table says. The same counterexample $x = -4$ breaks both false statements.

Check the last point: for $x = -4$, the original has hypothesis T and conclusion F, and the contrapositive has hypothesis "$-4 \le 3$" T and conclusion "$16 \le 9$" F. Both are the false row.

</details>

## Where this shows up

- The next lesson, [truth tables and logical equivalence](03-truth-tables-and-logical-equivalence.md), proves the equivalences used here, including $P \Rightarrow Q \equiv \neg P \vee Q$. [Negation and translating English](05-negation-and-translating-english.md) negates a conditional.
- Nearly every theorem is a conditional, so the proof methods use this lesson directly: [direct proof](../03-core-proof-methods/01-direct-proof.md) assumes the hypothesis and derives the conclusion, [contrapositive proof](../03-core-proof-methods/05-contrapositive-proof.md) proves the equivalent contrapositive, and [counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md) breaks a conditional with the one false row.
- In programming, a loop invariant is a conditional that must hold before and after each step, and a precondition and postcondition pair says "if the input satisfies the precondition, then the output satisfies the postcondition". In economics, "if the price rises, quantity demanded falls" is a conditional that a model must either assume or prove.
