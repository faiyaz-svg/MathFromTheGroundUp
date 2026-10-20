# Negation and translating English

After this lesson you can negate a statement built from "and", "or", "if ... then", "for every" and "there exists", including statements with several nested quantifiers, and you can translate English sentences with hidden quantifiers into symbols without changing their meaning.

Before this: [truth tables and logical equivalence](03-truth-tables-and-logical-equivalence.md) (De Morgan's laws and $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$) and [quantifiers](04-quantifiers.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Negate "$n$ is greater than 3 and $n$ is even" (for an integer $n$), and simplify as far as you can.
2. Negate "Every student passed."
3. Negate "If it rains, the match is cancelled."

<details class="solution" markdown>
<summary>Answers</summary>

1. "$n \le 3$ or $n$ is odd". The "and" becomes "or" and each part is negated.
2. "Some student did not pass." It is not "No student passed": that is too strong, since it claims every student failed.
3. "It rains and the match is not cancelled." This is the only situation in which the conditional is false.

</details>

## The idea

Suppose a friend says "I've never lost at chess". What would prove them wrong? Not a game where they lost every time, and not a pile of games either. One lost game is enough. The negation of "never lost" is "lost at least once", and the negation of "I always tell the truth" is "I sometimes lie", not "I always lie".

Mathematics needs negation constantly. To disprove a claim you prove its negation. A proof by contradiction begins by assuming the negation of what you want. A proof by contrapositive negates both parts of a conditional. And some definitions are only understood once you can say what it means for them to fail: "this sequence does not converge" is the negation of a statement with three nested quantifiers.

The rules are short and they are the same ones you already have. De Morgan's laws handle "and" and "or". The one false row of the conditional handles "if". The new rule is the one that handles quantifiers, and it is the same idea once more: "not everything" means "something fails", and "nothing" means "everything fails". The skill is applying these rules one layer at a time, without skipping a layer.

## Definitions

### The negation rules

To **negate** a statement is to form a statement that is true exactly when the original is false. Every statement has many correct negations that look different. The useful one is the **normal form** where the "not" has been pushed in as far as it goes, so that it sits only on the smallest pieces, such as a single comparison. The rules for pushing a negation inward are:

| Statement | Its negation |
|---|---|
| $P \wedge Q$ | $\neg P \vee \neg Q$ |
| $P \vee Q$ | $\neg P \wedge \neg Q$ |
| $P \Rightarrow Q$ | $P \wedge \neg Q$ |
| $P \Leftrightarrow Q$ | $(P \wedge \neg Q) \vee (\neg P \wedge Q)$ |
| $\forall x\, P(x)$ | $\exists x\, \neg P(x)$ |
| $\exists x\, P(x)$ | $\forall x\, \neg P(x)$ |
| $\forall x\,(P(x) \Rightarrow Q(x))$ | $\exists x\,(P(x) \wedge \neg Q(x))$ |
| $\exists x\,(P(x) \wedge Q(x))$ | $\forall x\,(P(x) \Rightarrow \neg Q(x))$ |
| $\neg P$ | $P$ |

The first three rows are De Morgan's laws and Theorem 3(a) from the equivalence lesson. The biconditional row says the two sides disagree, in either direction; it is the exclusive or. The last two quantifier rows are the earlier rules combined. For the statement "every $P$ is a $Q$", the negation is "some $P$ is not a $Q$", and for "some $P$ is a $Q$" the negation is "no $P$ is a $Q$".

Comparison symbols have their own negations: $\neg(a < b)$ is $a \ge b$, $\neg(a \le b)$ is $a > b$, $\neg(a = b)$ is $a \ne b$, $\neg(x \in A)$ is $x \notin A$, and $\neg(A \subseteq B)$ is the statement "some element of $A$ is not in $B$", that is, $\exists x\,(x \in A \wedge x \notin B)$.

In plain words, negation swaps "all" with "some", "and" with "or", flips each comparison, and for a conditional keeps the hypothesis and negates the conclusion, joining them with "and".

*Theorem 1 (negating quantifiers).* For every open sentence $P(x)$ on a domain $D$, $\neg \forall x \in D,\ P(x)$ is equivalent to $\exists x \in D,\ \neg P(x)$, and $\neg \exists x \in D,\ P(x)$ is equivalent to $\forall x \in D,\ \neg P(x)$.

What we know: the truth conditions from the quantifiers lesson. A statement $\forall x\,P(x)$ is true when $P$ holds at every element, and false when it fails at some element. What we want: the negation of $\forall x\,P(x)$ is true in exactly the situations where $\exists x\,\neg P(x)$ is true. The plan is to go through both directions of "true exactly when".

*Proof.* Suppose $\neg \forall x\,P(x)$ is true. Then $\forall x\,P(x)$ is false, so $P(a)$ fails for some element $a \in D$. For that element $\neg P(a)$ is true, so $\exists x\,\neg P(x)$ is true. Conversely, suppose $\exists x\,\neg P(x)$ is true. Then $\neg P(a)$ holds for some $a \in D$, so $P(a)$ fails and $\forall x\,P(x)$ is false, which makes its negation true. The two statements are true in the same situations. For the second equivalence, apply the first to the open sentence $\neg P(x)$: $\neg \forall x\,\neg P(x) \equiv \exists x\,\neg\neg P(x) \equiv \exists x\,P(x)$. Negating both sides gives $\forall x\,\neg P(x) \equiv \neg \exists x\,P(x)$. $\blacksquare$

Look back: for a finite domain this is De Morgan's law. On $\{1, 2, 3\}$, $\neg(P(1) \wedge P(2) \wedge P(3)) \equiv \neg P(1) \vee \neg P(2) \vee \neg P(3)$, which is the same as $\exists x\,\neg P(x)$. The theorem says it extends to every domain, however large.

## How to do it

### Negating a statement, layer by layer

1. Write the statement in symbols. Restore everything English leaves out: every quantifier, the domain, and the arrow inside a "for every $P$, $Q$" statement.
2. Put a $\neg$ in front of the whole statement.
3. Push the $\neg$ inward one layer at a time, using the table. At each layer the $\neg$ passes through exactly one symbol. A quantifier flips ($\forall$ with $\exists$), "and" and "or" flip, and a conditional $P \Rightarrow Q$ becomes $P \wedge \neg Q$. The domain, the variable names and the order of the quantifiers stay the same.
4. At the innermost level, negate the comparison: $<$ becomes $\ge$, $=$ becomes $\ne$, and so on.
5. Cancel double negations.
6. Translate the result back into English and read it aloud. It should sound like the opposite of the original.
7. Test it on a case. Pick values for which the original is true, and check that the negation is false there, and the other way round.

### Translating an English sentence

1. Find the quantifier words: "all", "every", "each", "some", "there is", "no", "any", "a" and "an". Decide whether each is $\forall$ or $\exists$, using the table below.
2. Name the predicates and the domain. "Every student has a friend" has students and people, a predicate $F(x, y)$ for "$x$ and $y$ are friends", and two quantifiers.
3. Use the pairing: a restricted $\forall$ goes with $\Rightarrow$, and a restricted $\exists$ goes with $\wedge$.
4. Put the quantifiers in the order the sentence has them: the one that is mentioned first is outermost, unless the sentence says otherwise.
5. Read the symbols back in English, and check them against the original with a small example.

The common patterns are these.

| English | Symbols |
|---|---|
| All $A$ are $B$; every $A$ is a $B$; each $A$ is a $B$ | $\forall x\,(A(x) \Rightarrow B(x))$ |
| Some $A$ is a $B$; there is an $A$ that is a $B$; at least one $A$ is a $B$ | $\exists x\,(A(x) \wedge B(x))$ |
| No $A$ is a $B$; none of the $A$ are $B$ | $\forall x\,(A(x) \Rightarrow \neg B(x))$, or $\neg \exists x\,(A(x) \wedge B(x))$ |
| Not every $A$ is a $B$; some $A$ is not a $B$ | $\exists x\,(A(x) \wedge \neg B(x))$ |
| Only $A$'s are $B$'s; a $B$ must be an $A$ | $\forall x\,(B(x) \Rightarrow A(x))$ |

The last row reverses the order, in the same way "only if" did for conditionals. "Only members may enter" says that if someone enters, then they are a member.

## Worked examples

<div class="example" markdown>

### Example 1: negating a universal conditional

Negate "For every integer $n$, if $n$ is prime, then $n$ is odd." Then decide which of the statement and its negation is true.

Step 1: in symbols, $\forall n \in \mathbb{Z},\ (n \text{ is prime} \Rightarrow n \text{ is odd})$. Step 2: put $\neg$ in front. Step 3, first layer: the $\neg$ passes through the $\forall$ and turns it into $\exists$:

$$
\exists n \in \mathbb{Z},\ \neg\bigl(n \text{ is prime} \Rightarrow n \text{ is odd}\bigr).
$$

Second layer: $\neg(P \Rightarrow Q)$ becomes $P \wedge \neg Q$:

$$
\exists n \in \mathbb{Z},\ \bigl(n \text{ is prime} \wedge n \text{ is not odd}\bigr).
$$

Step 4: "not odd" for an integer is "even". Step 6: in English, "There is an integer that is prime and even." Step 7: $n = 2$ is such an integer. So the negation is true, and the original is false, and the original's counterexample is the number 2.

Check: the original claims that every prime is odd. A false universal statement is refuted by exactly the example the negation asks for, a prime that is not odd. A tempting wrong negation, "for every integer $n$, $n$ is prime and even", fails at $n = 9$, and it would fail even if the original were true, so it can't be the opposite of the original.

</div>

<div class="example" markdown>

### Example 2: negating a limit statement

The definition of a limit, which the epsilon-delta definition<!-- link: ../../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md --> lesson takes slowly, says that $\lim_{x \to a} f(x) = L$ when

$$
\forall \varepsilon > 0,\ \exists \delta > 0,\ \forall x,\ \bigl(0 < \lvert x - a \rvert < \delta \Rightarrow \lvert f(x) - L \rvert < \varepsilon\bigr).
$$

In words: however small a tolerance $\varepsilon$ you demand around $L$, there is a window of half-width $\delta$ around $a$ so that every $x$ in the window (other than $a$ itself) has $f(x)$ within the tolerance. Write the negation, and use it to show that $f(x) = 0$ for $x \le 0$ and $f(x) = 1$ for $x > 0$ does not have limit 0 at $a = 0$.

Step 1 is done; the statement has three quantifiers and an arrow inside. Step 2: put $\neg$ in front. Step 3, one layer per line:

$$
\begin{aligned}
&\neg\, \forall \varepsilon > 0\ \exists \delta > 0\ \forall x\ (0 < \lvert x - a \rvert < \delta \Rightarrow \lvert f(x) - L \rvert < \varepsilon) \\
&\exists \varepsilon > 0\ \neg\, \exists \delta > 0\ \forall x\ (\dots) \\
&\exists \varepsilon > 0\ \forall \delta > 0\ \neg\, \forall x\ (\dots) \\
&\exists \varepsilon > 0\ \forall \delta > 0\ \exists x\ \neg(0 < \lvert x - a \rvert < \delta \Rightarrow \lvert f(x) - L \rvert < \varepsilon) \\
&\exists \varepsilon > 0\ \forall \delta > 0\ \exists x\ (0 < \lvert x - a \rvert < \delta \wedge \lvert f(x) - L \rvert \ge \varepsilon)
\end{aligned}
$$

The last line is the negation. In words: there is a tolerance $\varepsilon$ such that for every window $\delta$, however small, some $x$ in the window (other than $a$) has $f(x)$ at least $\varepsilon$ away from $L$. Every quantifier flipped, the order stayed the same, the arrow became "and", and the final inequality was negated.

Now the example, with $a = 0$ and $L = 0$. The negation asks for an $\varepsilon$ first. Take $\varepsilon = \frac{1}{2}$. Then let $\delta > 0$ be arbitrary, and name an $x$ that depends on it: $x = \frac{\delta}{2}$. Then $0 < \lvert x \rvert = \frac{\delta}{2} < \delta$, and since $x > 0$, $f(x) = 1$, so $\lvert f(x) - 0 \rvert = 1 \ge \frac{1}{2}$. This is the negation, so $\lim_{x \to 0} f(x) = 0$ is false.

Check: the proof followed the order of the quantifiers. The $\exists \varepsilon$ was named first and cannot depend on $\delta$; the $\forall \delta$ was taken arbitrary; and the $\exists x$ was named last, with a formula in $\delta$. A window of half-width $0.001$ gives $x = 0.0005$, where $f$ is 1, which is not near 0.

</div>

<div class="example" markdown>

### Example 3: translating with nested quantifiers

Translate (a) "Every student has a friend." (b) "Some student has no friends." (c) "Not every student has a friend." Let the domain be people, $S(x)$ mean "$x$ is a student" and $F(x, y)$ mean "$x$ and $y$ are friends".

(a) Steps 1 to 4: "every student" is a restricted $\forall$, so it gets an arrow. "Has a friend" is an $\exists$ over people. So (a) is $\forall x\,\bigl(S(x) \Rightarrow \exists y\ F(x, y)\bigr)$.

(b) "Some student" is a restricted $\exists$, so it gets an "and". "Has no friends" is $\neg \exists y\ F(x, y)$, which is $\forall y\ \neg F(x, y)$. So (b) is $\exists x\,\bigl(S(x) \wedge \forall y\ \neg F(x, y)\bigr)$.

(c) Negate (a) layer by layer. $\neg \forall x\,\bigl(S(x) \Rightarrow \exists y\ F(x, y)\bigr)$ becomes $\exists x\,\neg\bigl(S(x) \Rightarrow \exists y\ F(x, y)\bigr)$, then $\exists x\,\bigl(S(x) \wedge \neg \exists y\ F(x, y)\bigr)$, then $\exists x\,\bigl(S(x) \wedge \forall y\ \neg F(x, y)\bigr)$. This is exactly (b).

Check: (b) and (c) are two English sentences for the same statement. Test with two students who are friends with each other and a third with no friends: (a) is false (the third has none), (b) is true, and (c) is true.

</div>

<div class="example" markdown>

### Example 4: negating "bounded above" (finish it yourself)

A sequence $a_1, a_2, a_3, \dots$ of real numbers is bounded above when $\exists M \in \mathbb{R},\ \forall n \in \mathbb{Z}^+,\ a_n \le M$. Write what it means for the sequence not to be bounded above.

Step 2: put $\neg$ in front. Step 3, first layer: $\neg \exists M\,(\dots)$ becomes $\forall M\ \neg\,\forall n\,(a_n \le M)$. Finish the other layers, translate to English, and test your answer on $a_n = n$ and on $a_n = \frac{1}{n}$.

<details class="solution" markdown>
<summary>Finish</summary>

The second layer turns $\neg \forall n\,(a_n \le M)$ into $\exists n\ \neg(a_n \le M)$, and Step 4 negates the comparison: $a_n > M$. So the sequence is not bounded above when

$$
\forall M \in \mathbb{R},\ \exists n \in \mathbb{Z}^+,\ a_n > M.
$$

In English: whatever number $M$ you name, some term of the sequence is bigger than it.

Check: for $a_n = n$, given $M$, take $n$ to be the larger of $1$ and $\lfloor M \rfloor + 1$. Then $n$ is a positive integer and $a_n = n > M$. So $a_n = n$ is not bounded above. For $a_n = \frac{1}{n}$, the original holds with $M = 1$, since $\frac{1}{n} \le 1$ for every $n$, so the negation must fail: no matter which $n$ you try, $a_n \le 1$, so $M = 1$ defeats the claim.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for "not all" and "all not". The negation of "all students passed" is "not all students passed", which is "some student did not pass", $\exists x\,\neg P(x)$. It isn't "all students did not pass", which is $\forall x\,\neg P(x)$ and means that nobody passed. In symbols, $\neg \forall x\,P(x)$ and $\forall x\,\neg P(x)$ are different statements. When one student failed and the rest passed, the first is true and the second is false.

</div>

<div class="warning" markdown>

Watch out for negating a conditional by negating only the conclusion. The negation of $P \Rightarrow Q$ is $P \wedge \neg Q$, not $P \Rightarrow \neg Q$. The statement "if it rains, the match is not cancelled" is true on every sunny day, so it can't be the opposite of "if it rains, the match is cancelled", which is also true on every sunny day. Both being true is a sign you wrote a contrary and not a negation.

</div>

<div class="warning" markdown>

Watch out for a negation that changes only some of the pieces. A negation must flip every quantifier in front. Negating $\forall \varepsilon\, \exists \delta\ (\dots)$ as $\forall \varepsilon\, \forall \delta\ \neg(\dots)$ or as $\exists \varepsilon\, \exists \delta\ \neg(\dots)$ leaves one quantifier unflipped, and gives a statement which is not the opposite.

</div>

<div class="warning" markdown>

Watch out for the word "any". It means "every" in a plain claim ("any prime greater than 2 is odd") and "some" after a negation, a question or an "if" ("if any test fails, stop" means "if some test fails"). The two readings turn out to agree when a conditional is rewritten: $(\exists t\ F(t)) \Rightarrow S$ is equivalent to $\forall t\,(F(t) \Rightarrow S)$. When a sentence with "any" is unclear, rewrite it with "every" or "some".

</div>

Negating a comparison needs care at the boundary. The negation of "$x < 3$" is "$x \ge 3$", not "$x > 3$". The number 3 itself is the case that gets lost.

English also has genuinely ambiguous sentences. "Every student read a book" can mean $\forall s\, \exists b$ (each student read some book, possibly different ones) or $\exists b\, \forall s$ (there is one book that all of them read). Mathematics sentences avoid this by stating the order; when you meet an ambiguous English sentence, write both translations and ask which one is meant.

## Tricks and shortcuts

Move left to right and flip. To negate a long statement, go through it from the left: every $\forall$ becomes $\exists$, every $\exists$ becomes $\forall$, until you reach the statement inside. Then negate that statement by its own rule (an arrow becomes "and ... not", a comparison flips). The variables and their order never change.

To check a negation, test whether it is a contrary. A statement and its negation can never be both true and can never be both false. If you can find a situation where your "negation" and the original are both true (like the rainy-day pair above) or both false, it is wrong.

Everyday words have fixed negations: "always" becomes "at least once not", "never" becomes "at least once", "everyone" becomes "someone doesn't", "nobody" becomes "somebody does", "at least 3" becomes "at most 2", and "at most 3" becomes "at least 4" (for whole numbers).

## In code

The rules $\neg \forall \equiv \exists \neg$ and $\neg \exists \equiv \forall \neg$ are exactly the relations between `all` and `any`. The code below tests them on a nested statement, and on every possible relation $P(x, y)$ over a three-element domain (512 relations), which is a complete check for that domain.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import product

D = [1, 2, 3]
pairs = [(x, y) for x in D for y in D]

xs = [3, 8, 11]
print(not all(x % 2 == 1 for x in xs), any(x % 2 == 0 for x in xs))   # True True
print(not any(x > 10 for x in xs), all(x <= 10 for x in xs))          # False False

# all 2**9 = 512 relations P(x, y) on D: the negation of "for all x there is y"
# is "there is x such that for all y, not P"
same = True
for bits in product([False, True], repeat=len(pairs)):
    P = dict(zip(pairs, bits))
    original = all(any(P[x, y] for y in D) for x in D)
    negation = any(all(not P[x, y] for y in D) for x in D)
    if original == negation:
        same = False
print(same)                                  # True: they are always opposite

# a counterexample search is the existential statement in the negation
print(next((n for n in range(2, 50) if all(n % d for d in range(2, n)) and n % 2 == 0), None))   # 2
```

The first two lines show `not all(...)` agreeing with `any(not ...)` and `not any(...)` agreeing with `all(not ...)` on one list. The loop is a brute-force proof for the domain $\{1, 2, 3\}$: in each of the 512 cases, "for all $x$ there is a $y$" and its negation have opposite truth values. The last line finds a prime that is even, which is the witness that makes the negation of "every prime is odd" true. A finite check doesn't settle an infinite domain, but Theorem 1 does.

</details>

## FAQ

### Why isn't the negation of "all" "none"?

Because "all" and "none" are the two extremes, and the negation of one extreme is everything except that extreme. "All" fails as soon as one case fails, so its negation is "at least one fails". "None" is much stronger than that: it asks for every case to fail. Between them is the large middle ground of "some but not all", where both "all" and "none" are false.

### How do I know my negation is right?

Use the two-sided test: the statement and its negation must have opposite truth values in every situation. Pick a small situation where you know the original is true and one where it is false, and check that the negation is false and true. If both are true in some case, you negated only part of the statement. A second test is to negate your negation and see whether you return to the original.

### Does the negation of "$x$ is greater than 3" mean "$x$ is less than 3"?

No. It means "$x$ is not greater than 3", which is "$x \le 3$". The missing case is $x = 3$. Writing the symbolic version first, $\neg(x > 3)$, and then flipping the comparison, $x \le 3$, avoids the slip.

### Why do proofs so often negate things?

Because of how a proof of "impossible" has to work. To show that no integer solves an equation, you assume one does and reach a contradiction (that begins by negating the claim). To show a universal statement is false, you prove its negation, an existence claim, by producing an example. Negation converts one kind of task into another, and the table above tells you which.

## Practice

### Warm-up

1\. Negate each statement about an integer $n$ and simplify. (a) "$n$ is even and $n > 10$." (b) "$n < 2$ or $n > 5$." (c) "If $n$ is divisible by 4, then $n$ is even."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) "$n$ is odd or $n \le 10$." The "and" becomes "or", and "not even" is "odd" for an integer.
- (b) "$2 \le n$ and $n \le 5$", which is $2 \le n \le 5$.
- (c) "$n$ is divisible by 4 and $n$ is odd." A conditional becomes hypothesis "and" not-conclusion.

Check (c): the original is true for every integer, so its negation should be false for every integer, and it is: a multiple of 4 is never odd. Check (b) at $n = 5$: the original is false and the negation is true.

</details>

2\. Negate each statement in words. (a) "Every dog barks." (b) "Some prime number is even." (c) "Nobody in the class failed." (d) "There is a largest integer."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) "Some dog does not bark."
- (b) "Every prime number is odd." (Or: "No prime is even".) This negation is false, since 2 is a prime and even.
- (c) "Somebody in the class failed."
- (d) "Every integer has a larger integer", that is, for each integer there is a greater one.

Check (b): the original is true (take 2), so its negation must be false, and it is.

</details>

3\. Translate into symbols, stating predicates and domain. (a) "A square is a rectangle." (b) "Every student has a friend." (c) "There is a student with no friends." (d) "Only members may enter."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The "a" is generic: $\forall x\,(\text{Square}(x) \Rightarrow \text{Rectangle}(x))$.
- (b) $\forall x\,\bigl(S(x) \Rightarrow \exists y\ F(x, y)\bigr)$, with $F(x, y)$ meaning "$x$ and $y$ are friends".
- (c) $\exists x\,\bigl(S(x) \wedge \forall y\ \neg F(x, y)\bigr)$.
- (d) $\forall x\,(\text{Enters}(x) \Rightarrow \text{Member}(x))$. The "only" puts the member condition in the conclusion.

Check (b) and (c): they should be negations of each other, which is Example 3 above.

</details>

### Standard

4\. Negate each statement on the domain $\mathbb{R}$, and say which of the statement and its negation is true. (a) $\forall x\, \exists y\ (y^2 = x)$. (b) $\exists y\, \forall x\ (x \le y)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The negation is $\exists x\, \forall y\ (y^2 \ne x)$. It is true: take $x = -1$, and then every real $y$ has $y^2 \ge 0 \ne -1$. So the original is false.

(b) The negation is $\forall y\, \exists x\ (x > y)$. It is true: given $y$, take $x = y + 1$. So the original, which claims a largest real number, is false.

Check each pair for opposite values: (a) original false, negation true. (b) original false, negation true. In both, the original is the stronger claim that the real line can't support.

</details>

5\. Negate "For every integer $n$, $n^2 > n$" and decide which of the two is true.

<details class="solution" markdown>
<summary>Solution</summary>

The negation is $\exists n \in \mathbb{Z},\ n^2 \le n$ (the negation of $>$ is $\le$). It is true: $n = 0$ gives $0 \le 0$, and $n = 1$ gives $1 \le 1$. So the original is false, and $n = 0$ is a counterexample to it.

Check: $0^2 = 0$ is not greater than 0, so the original fails at 0. The negation is true there, and exactly one of the pair is true.

</details>

6\. Write the negation of "For every real number $x$, $x^2 - 2x + 2 > 0$". Then prove the original by showing that the negation is false.

<details class="solution" markdown>
<summary>Solution</summary>

The negation is $\exists x \in \mathbb{R},\ x^2 - 2x + 2 \le 0$. To show this is false, we show that its property fails for every real $x$ (the last row of the proof table in the quantifiers lesson).

*Proof.* Let $x$ be an arbitrary real number. Completing the square, $x^2 - 2x + 2 = (x - 1)^2 + 1$. A square is not negative, so $(x - 1)^2 + 1 \ge 1 > 0$. Hence $x^2 - 2x + 2 \le 0$ is false for this $x$. Since $x$ was arbitrary, no real $x$ satisfies the negation, so the original holds for every real $x$. $\blacksquare$

Check: $x = 1$ gives $1 - 2 + 2 = 1$, the smallest value, and $x = 0$ gives 2. All are positive.

</details>

### Challenge

7\. A function $f$ is continuous at $a$ when $\forall \varepsilon > 0,\ \exists \delta > 0,\ \forall x\ (\lvert x - a \rvert < \delta \Rightarrow \lvert f(x) - f(a) \rvert < \varepsilon)$. Write the negation, and use it to show that $f(x) = 0$ for $x \le 0$ and $f(x) = 1$ for $x > 0$ is not continuous at $a = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

Push the negation in one layer at a time, as in Example 2:

$$
\exists \varepsilon > 0,\ \forall \delta > 0,\ \exists x\ \bigl(\lvert x - a \rvert < \delta \wedge \lvert f(x) - f(a) \rvert \ge \varepsilon\bigr).
$$

Now $a = 0$ and $f(0) = 0$. Take $\varepsilon = \frac{1}{2}$ (named first, since the $\exists \varepsilon$ is outermost). Let $\delta > 0$ be arbitrary, and take $x = \frac{\delta}{2}$. Then $\lvert x - 0 \rvert = \frac{\delta}{2} < \delta$, and $f(x) = 1$ because $x > 0$, so $\lvert f(x) - f(0) \rvert = 1 \ge \frac{1}{2}$. This proves the negation, so $f$ is not continuous at 0. $\blacksquare$

Check: the sequence of choices $\varepsilon = \frac{1}{2}$, then $\delta = 0.01$, then $x = 0.005$ gives $f(x) = 1$ and $f(0) = 0$. The jump of size 1 is the reason: no window around 0 keeps the values within $\frac{1}{2}$ of $f(0)$.

</details>

8\. (Reviews [conditionals and biconditionals](02-conditionals-and-biconditionals.md).) Write the contrapositive and the negation of "If $n^2$ is even, then $n$ is even." Which one is equivalent to the original? For the negation, say why no integer $n$ satisfies it.

<details class="solution" markdown>
<summary>Solution</summary>

The contrapositive is "If $n$ is not even, then $n^2$ is not even", that is, "if $n$ is odd, then $n^2$ is odd". It is equivalent to the original.

The negation is "$n^2$ is even and $n$ is not even", that is, "$n^2$ is even and $n$ is odd". It is not equivalent to the original: it is the statement that the original fails at $n$.

No integer satisfies the negation, because an odd $n = 2k + 1$ has $n^2 = 2(2k^2 + 2k) + 1$, which is odd (the proof in the conditionals lesson, Practice problem 7). The original statement holds for every integer exactly because its negation holds for none.

Check: $n = 5$ has $n^2 = 25$, odd, so "$n^2$ even" is false and the negation fails. $n = 6$ has $n^2 = 36$ even, and $n = 6$ is even, so "$n$ odd" is false and again the negation fails.

</details>

## Where this shows up

- The proof methods in the next chapter run on this lesson: contrapositive proof<!-- link: ../03-core-proof-methods/05-contrapositive-proof.md --> and proof by contradiction<!-- link: ../03-core-proof-methods/06-proof-by-contradiction.md --> start by writing a negation, and counterexamples and disproof<!-- link: ../04-more-proof-methods/04-counterexamples-and-disproof.md --> proves the negation of a universal statement.
- Calculus and analysis courses define limits, continuity and convergence with nested quantifiers, and prove that something is not continuous or does not converge by negating them, exactly as in Example 2 (limits, continuity and derivatives in the university core). In theory of computation, the pumping lemma for regular languages has four nested quantifiers (there is a length $p$ such that for every long string there is a split such that for every number of repeats ...), and using it to show a language is not regular means negating it (regular expressions and the pumping lemma<!-- link: ../../06-cs-math/06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md -->).
- Writing correct conditions in code is the same skill. The guard `if not (found and valid)` is negation of an "and", and a test that "fails for some input" is the negation of "passes for all inputs".
