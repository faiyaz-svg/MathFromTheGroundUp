# How to read a proof

After this lesson you can read a proof so that you could defend every line: find the claim's shape and the method, track every letter, give a reason for each step, fill in the steps a textbook skips, test the proof on an example, find where each hypothesis is used, and say in one sentence what the proof does.

Before this: [direct proof](01-direct-proof.md), and from the previous chapters [proof language: let, suppose, WLOG](../01-language-and-notation/03-proof-language-let-suppose-wlog.md) and [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A proof begins "Suppose, for contradiction, that $n$ is the largest integer." What method is it, and what must the proof reach before it can end?
2. A proof reads: "Let $n$ be an integer. Then $n = 2k$. So $n^2 = 4k^2$." Name two things a careful reader should object to.
3. A theorem says "If $a > 0$ and $b > 0$, then ..." and its proof never uses $b > 0$. Give two possible explanations.

<details class="solution" markdown>
<summary>Answers</summary>

1. It is a proof by contradiction. The proof must reach a statement that is false, or that contradicts something known (the assumption itself, a hypothesis or an established fact), and then say so.
2. The letter $k$ is never introduced, so we don't know where it comes from. Worse, $n$ was only said to be an integer, so $n = 2k$ is not justified: it holds only if $n$ is even.
3. Either the theorem is true without the condition $b > 0$ (so it could be stated more strongly), or the proof has a gap, with a step that silently needs $b > 0$ and doesn't say so.

</details>

## The idea

When you review a teammate's pull request, "it looks fine" is not a review. You read each change, ask what it does, run the tests, and try a nasty input. You merge when you could defend each line, not when nothing jumped out at you. Reading a proof is the same job. The author claims that a statement is true for every case, and your job is to decide whether the argument really covers every case.

Most students read a proof the way they read a news article: they follow the sentences, nod at each one and arrive at the end feeling that they understood. That feeling is unreliable. A proof can be built from lines that each look fine, while the whole thing proves a different statement from the one on the page, or leans on a fact that is false. Nodding is not checking.

Active reading replaces nodding with questions you can answer. Where did this letter come from? Why does this line follow? What does the author mean by "clearly" here? What happens if I put in actual numbers? Proofs are meant to be read slowly. A page of proof can take half an hour, and a professor who says "this is a short proof" means it is short to write down, not short to digest.

One difference from code review is worth stating. You can't run a proof, so you have to substitute. The substitute for running is working an example through the lines, which is the move that catches the most errors.

## Definitions

**Active reading** of a proof means reading with pencil and paper, and answering a list of questions about the claim, the method, the letters, the reasons for each line and the use of each hypothesis. In plain words, you don't take any line on trust; you write the reason beside it.

A **gap** in a proof is a step whose justification is not on the page and that the reader cannot fill in at once. In plain words, a gap is a line where you ask "why?" and don't get an answer from anything above it. Some gaps are routine, and the audience fills them in silently. Others hide the whole difficulty, and a proof with such a gap is not yet a proof.

The **skeleton** of a proof is its claim, its method, its assumptions and its final line, with the middle left out. In plain words, it is what you could write on the back of a hand to say how the proof is organized: "assume the opposite, build a number $N$, show $N$ has a prime divisor, derive that it divides 1."

Textbook authors compress. They use a small vocabulary of phrases that stand for "a justification exists, and I won't write it out". The table says what each one asks of you. This book avoids the first row in its own proofs, but you will meet all of them in other texts.

| Phrase in a text | What it means | What you do |
|---|---|---|
| "clearly", "obviously", "trivially", "it is easy to see" | The author finds the step routine. It may be, or may not be. | Write out the step yourself. If you can't, you have found a gap. |
| "it follows that" | A conclusion that needs an argument nearby. | Find the lines it follows from, and the rule used. |
| "similarly", "the other case is analogous" | A case is left out because it repeats another. | Write it out once, with the names changed, and check it works. |
| "by symmetry", "without loss of generality" | The cases are mirror images. | Check that swapping the objects leaves the claim unchanged, as in the [phrasebook](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#using-without-loss-of-generality). |
| "one checks", "a routine calculation shows" | An algebra or computation is skipped. | Do the computation on paper. |
| "by the lemma", "by Theorem 3.2" | The step cites an earlier result. | Find the result, and check that its hypotheses hold here. |
| "the rest is similar", "the remaining details are left to the reader" | The author hands you work. | Do it. It is a built-in exercise. |

## How to do it

### Eight questions to ask of every proof

1. What is claimed, and what is its shape? Write the claim as "if $P$, then $Q$" or "for every $x$, ..." or "there exists ...", and name the hypothesis and the conclusion. Test the claim on one small example before you read the proof.
2. What method does the first sentence announce, and what must the last line say? "Let $x$ be arbitrary" suggests a direct proof, "Suppose $Q$ is false" a contrapositive or contradiction, "Case 1" a proof by cases. The method tells you what the final line must be.
3. Track every letter. For each symbol, find where it is introduced, what kind of object it is, whether it is arbitrary (from a "for every") or particular (from a "there exists"), and where its scope ends. A table helps.
4. Give a reason for each line. Beside each line write a tag: H for a hypothesis, D for a definition, R for an earlier result, L for an earlier line of this proof, A for algebra or arithmetic. A line with no tag is a gap.
5. Fill each gap, starting with the "clearly" lines. Write out the missing computation. If it works, you now own the step. If it doesn't, you have found an error or a missing hypothesis.
6. Test the proof on an example. Choose concrete values that satisfy the hypothesis, and push them through the lines. Then choose values that violate the hypothesis, and see which line fails.
7. Find where each hypothesis is used. For each hypothesis, point to the line that needs it, and say what would go wrong without it. A hypothesis that is never used is a signal that the claim is stronger than stated, or that the proof is wrong.
8. Say what the proof does in one sentence, and compare the last line with the claim. Do the quantifiers match? Is the direction right ($P$ implies $Q$, not $Q$ implies $P$)?

### Reading the first line and the last line first

Before reading the middle, read the claim, the first sentence and the last sentence. The first sentence says what is assumed and which method is in use. The last says what has been reached. A proof whose first and last sentences don't fit the claim ("Suppose $n$ is even ... so $n^2$ is even" for the claim "if $n^2$ is even, then $n$ is even") is wrong before you read a line of the middle.

## Worked examples

<div class="example" markdown>

### Example 1: Euclid's proof, line by line

Here is the proof in the terse style of a textbook. We read it with the eight questions.

*Theorem.* There are infinitely many primes.

*Proof.* Suppose there were only finitely many primes, $p_1, p_2, \dots, p_n$. Let $N = p_1 p_2 \cdots p_n + 1$. Then $N > 1$, so $N$ has a prime divisor $p$. Since $p_1, \dots, p_n$ are all the primes, $p = p_i$ for some $i$. Then $p \mid p_1 \cdots p_n$ and $p \mid N$, so $p \mid N - p_1 \cdots p_n = 1$. This is absurd, since $p > 1$. $\blacksquare$

Question 1: the claim is a statement about the whole set of primes: "the set of primes is not finite". It has no if-then shape, so we need the method to find the structure. Test: the primes 2, 3, 5 are a list that is not all the primes, since 7 is missing.

Question 2: "Suppose there were only finitely many primes" opens a proof by contradiction. The last line must therefore be a contradiction, and it is: "This is absurd."

Question 3, the letters:

| Letter | What it is | Introduced | Arbitrary or particular |
|---|---|---|---|
| $n$ | the number of primes in the assumed list | line 1 | particular (from the assumption) |
| $p_1, \dots, p_n$ | the primes, all of them | line 1 | particular |
| $N$ | the integer $p_1 \cdots p_n + 1$ | line 2 | defined from the list |
| $p$ | a prime divisor of $N$ | line 3 | particular (exists by the line's reason) |
| $i$ | the index with $p = p_i$ | line 4 | particular |

Question 4, the reasons for each line:

| Line | Tag | Reason |
|---|---|---|
| "Suppose there were only finitely many primes" | assumption | the negation of the claim |
| "Let $N = p_1 \cdots p_n + 1$" | definition | a new name for an integer |
| "Then $N > 1$" | A | each $p_k \ge 2$, so the product is at least 2, and $N \ge 3$ |
| "so $N$ has a prime divisor $p$" | R | every integer greater than 1 has a prime divisor (a lemma the text doesn't state) |
| "$p = p_i$ for some $i$" | L | the list contains every prime, and $p$ is a prime |
| "$p \mid p_1 \cdots p_n$" | L, R | $p$ is one of the factors; a factor divides the product |
| "$p \mid N$" | L | the prime divisor was chosen so |
| "$p \mid N - p_1 \cdots p_n = 1$" | R | the linear combination theorem with $x = 1$ and $y = -1$ |
| "absurd, since $p > 1$" | D | a prime exceeds 1, and nothing greater than 1 divides 1 |

Question 5, the gaps. The line "so $N$ has a prime divisor" is a gap in the text. It uses the lemma that every integer greater than 1 has at least one prime divisor, and it is a real lemma (proved in [proof by contradiction](06-proof-by-contradiction.md)). The proof is incomplete until that lemma is available. The line "nothing greater than 1 divides 1" is also routine but worth writing: if $p \mid 1$ then $1 = pk$ for an integer $k$, and $k$ must be positive since $pk > 0$, so $pk \ge p > 1$, which is false.

Question 6, the test. Take the list 2, 3, 5. Then $N = 31$, which is prime and not in the list. The proof says the list can't contain every prime, and it doesn't. A second test shows a common misreading. Take the list 2, 3, 5, 7, 11, 13. Then $N = 30031 = 59 \times 509$ is not prime. The proof never claims $N$ is prime, only that $N$ has a prime divisor, and that prime ($59$) is not in the list either. Reading "so $N$ is a new prime" is the usual mistake.

Question 7, the hypotheses. The only assumption is that the list contains all primes, and it is used in the line "$p = p_i$ for some $i$". Without it, $p$ could be a prime outside the list, and nothing would be absurd. That is the point of the proof: the contradiction exists because the list was assumed complete.

Question 8, the summary: given any finite list of primes, the number (product plus 1) has a prime divisor outside the list. The last line matches the claim: a finite list can't hold all the primes, so there are infinitely many.

Check: $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \times 509$, and 59 is not on the list $2, 3, 5, 7, 11, 13$.

</div>

<div class="example" markdown>

### Example 2: filling in a "clearly" step

A textbook proves that $x + \frac{1}{x} \ge 2$ for every $x > 0$ like this: "Note that $x + \frac{1}{x} - 2 = \frac{(x - 1)^2}{x}$. This is clearly non-negative, so the claim follows."

There are two things to fill in. The first is the identity. Put everything over the common denominator $x$:

$$
x + \frac{1}{x} - 2 = \frac{x^2 + 1 - 2x}{x} = \frac{(x - 1)^2}{x}.
$$

The second is the word "clearly". The numerator $(x - 1)^2$ is a square, so it is at least 0. The denominator $x$ is positive by the hypothesis $x > 0$. A non-negative number divided by a positive number is non-negative. So the whole fraction is at least 0, and adding 2 to both sides of $x + \frac{1}{x} - 2 \ge 0$ gives the claim.

Hypothesis test (question 7): the hypothesis $x > 0$ is used only for the sign of the denominator. For $x = -1$, the fraction is $\frac{4}{-1} = -4 < 0$, and indeed $-1 + (-1) = -2 < 2$. The word "clearly" hid exactly the step where the hypothesis enters.

Check: $x = 4$ gives $4 + \frac{1}{4} - 2 = \frac{9}{4}$, and $\frac{(4 - 1)^2}{4} = \frac{9}{4}$.

</div>

<div class="example" markdown>

### Example 3: a test on an example catches a flawed proof

Here is a plausible proof. *Claim:* if $a \mid bc$, then $a \mid b$ or $a \mid c$. *Proof.* Suppose $a \mid bc$. Then $bc = ak$ for some integer $k$. So $a$ divides the product $b \cdot c$, which means $a$ divides one of the factors. $\blacksquare$

Each sentence reads fine. Apply question 6 and push numbers through. Take $a = 6$, $b = 2$ and $c = 3$. Then $bc = 6 = 6 \times 1$, so $a \mid bc$ holds, and the proof's lines go through. But $6 \nmid 2$ and $6 \nmid 3$, so the conclusion fails. The claim is false, and the last sentence of the "proof" is where it breaks: "divides the product, so divides one of the factors" was written down with no reason.

Question 4 would have flagged the same line: no tag fits it. It is not a hypothesis, a definition, an earlier line or algebra. What is true is the same statement for a prime $a$ (Euclid's lemma), proved in [primes and unique factorization](../../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md). For composite $a$ it fails exactly when $a$ splits across the factors, as 6 does across 2 and 3.

Check: $6 \mid 6$, $6 \nmid 2$ and $6 \nmid 3$. For a prime, $a = 5$, $b = 10$ and $c = 7$: $5 \mid 70$ and $5 \mid 10$, as the true statement predicts.

</div>

<div class="example" markdown>

### Example 4: which hypothesis is used? (finish it yourself)

Read this proof. *Claim:* if $n$ is an odd integer, then $n^2 + n + 1$ is odd. *Proof.* Let $n$ be odd, so $n = 2k + 1$ for some integer $k$. Then

$$
n^2 + n + 1 = (4k^2 + 4k + 1) + (2k + 1) + 1 = 4k^2 + 6k + 3 = 2(2k^2 + 3k + 1) + 1.
$$

The number $2k^2 + 3k + 1$ is an integer, so $n^2 + n + 1$ is odd. $\blacksquare$

The proof is correct. Do question 7: where is the hypothesis "$n$ is odd" used, and is it needed? Test the claim on an even $n$ before you answer.

<details class="solution" markdown>
<summary>Finish</summary>

The hypothesis is used on the second line, to write $n = 2k + 1$. But it is not needed. For an even $n$, such as $n = 4$, $n^2 + n + 1 = 21$, which is odd. The reason is that $n^2 + n$ is even for every integer $n$ (the theorem in [proof language](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#worked-examples)), so $n^2 + n + 1$ is always odd. The claim is true for every integer, and the hypothesis can be dropped.

The proof is valid, but the reading tells us something: the theorem is weaker than the truth, and a proof that does not use the hypothesis would be shorter. Check: $n = 4$ gives 21 (odd), $n = 5$ gives 31 (odd), $n = -3$ gives $9 - 3 + 1 = 7$ (odd).

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for reading to agree. If you read a proof hoping it is right, you will find that it is. Read as the grader: look for the line that doesn't follow. A proof you attacked and couldn't break is a proof you understand.

</div>

<div class="warning" markdown>

Watch out for checking lines but not the whole. Every line may be correct while the proof proves something else. A proof of "if $n$ is even, then $n^2$ is even" offered as a proof of "if $n^2$ is even, then $n$ is even" is the standard example: all the lines are true, and the proof is of the converse. Compare the last line with the claim every time (question 8).

</div>

<div class="warning" markdown>

Watch out for trusting the theorem. Knowing that a statement is true is no help in deciding whether a proof of it is valid, since a bad proof can prove a true statement. Judge the argument, not the conclusion.

</div>

<div class="warning" markdown>

Watch out for confusing "I followed it" with "I understand it". Following means you checked each line. Understanding means you can state the idea in a sentence and write the proof again from that sentence with the book closed. The second is the test that counts.

</div>

If a line of a proof cannot be justified, you are in one of three situations: the step is routine and you haven't found the reason yet, the step is a real gap that the author skipped, or the step is false. The way to tell them apart is question 5 (write the step out) and question 6 (test it on numbers). Don't skip a step because you assume the author must be right.

## Tricks and shortcuts

Cover the proof and try the theorem yourself for five minutes, even if you fail. You will read the real proof much better, because you know where the difficulty is and which of its moves are a surprise.

Write a one-line proof card for every proof you study: the claim, the method, the key move, where the hypotheses are used. A page of cards is a better revision tool than a page of rereads, and it is the thing to write in the margin before an exam.

For any proof that uses a letter whose meaning you lost, scan back to the last "let", "suppose" or "there exists" that introduced it. If you can't find one, the letter has no origin.

When a proof has several cases, check the cover first (do the cases exhaust the possibilities?) and then check each case as a separate small proof.

## In code

A short script can do the two testing moves from questions 6 and 7 when the claim is about integers: build the number from Euclid's proof for the first few lists of primes, and search for a counterexample to the flawed claim in Example 3.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import factorint, primerange

# Euclid's N = product of the first k primes + 1: it is not always prime
product = 1
for k, p in enumerate(primerange(2, 20), start=1):
    product *= p
    n = product + 1
    print(k, n, factorint(n))
# 1 3 {3: 1}
# 2 7 {7: 1}
# 3 31 {31: 1}
# 4 211 {211: 1}
# 5 2311 {2311: 1}
# 6 30031 {59: 1, 509: 1}
# 7 510511 {19: 1, 97: 1, 277: 1}
# 8 9699691 {347: 1, 27953: 1}

# "if a divides b*c then a divides b or a divides c": search for failures
bad = [(a, b, c) for a in range(2, 13) for b in range(1, 13) for c in range(1, 13)
       if (b * c) % a == 0 and b % a != 0 and c % a != 0]
print(bad[:3])             # [(4, 2, 2), (4, 2, 6), (4, 2, 10)]
print(all(a in (4, 6, 8, 9, 10, 12) for a, _, _ in bad))   # True: only composite a fail
```

The first block checks that each $N$ has prime factors outside the list, as the proof says, and shows that $N$ itself can be composite. The second block finds counterexamples to Example 3's claim, and all of them have a composite $a$.

</details>

## FAQ

### How long should it take to read a proof?

Much longer than reading the same number of lines of prose. A one-page proof often takes 20 to 40 minutes the first time, because you stop to expand steps and run examples. That is the normal speed, and fast readers have simply done it more often.

### What do I do when I can't follow one step?

Say precisely what you can't justify, and write the step's input and output side by side. Try it on a small example. Look back for the definition of any word in the line. If you still can't, mark the line and carry on: later lines may explain it. After the proof ends, return to it. Ask a classmate or a teaching assistant about that line, not about "the proof".

### Do I need to understand the idea, or only check each line?

Both, and they do different jobs. Checking tells you the proof is correct. The idea tells you why the claim is true, and lets you write the proof again, adapt it to a similar claim and spot when it would fail. Question 8 (the one-sentence summary) is where the idea lives.

### Why do textbooks leave out so many steps?

Because a proof is written for an audience, and a book for second-year students assumes the first-year material. A step that is routine for the author is a gap for you until you have done it a few times. This is why the habit of filling in every "clearly" step pays off: each one you do makes the next one routine.

## Practice

### Warm-up

1\. For each opening sentence, name the method and say what the last line of the proof must be. (a) "Let $x$ be a real number." (b) "We prove the contrapositive. Suppose $n$ is not divisible by 3." (c) "Suppose, for contradiction, that $\sqrt{2}$ is rational." (d) "We consider two cases: $n$ even and $n$ odd."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) A direct proof of a "for every" statement. The last line is the property claimed about $x$.
- (b) Proof by contrapositive. The original claim has the form "if $P$, then $n$ is divisible by 3", and the proof assumes the negation of the conclusion. So the last line must say that $P$ is false.
- (c) Proof by contradiction. The last line is a contradiction (such as "$a$ and $b$ have a common factor, but we chose them with none"), followed by "so $\sqrt{2}$ is irrational".
- (d) Proof by cases. Each case must end with the same conclusion, and the cases must cover every integer.

Check: in (b), "not divisible by 3" is the negation of the conclusion, which is how the contrapositive begins.

</details>

2\. Label each line of this proof with H (hypothesis), D (definition), L (earlier line), R (earlier result) or A (algebra). *Claim:* if $a \mid b$ and $a \mid c$, then $a \mid 2b - 3c$.

1. Let $a \mid b$ and $a \mid c$.
2. Then $b = aj$ and $c = ak$ for integers $j$ and $k$.
3. So $2b - 3c = 2aj - 3ak$.
4. This equals $a(2j - 3k)$.
5. Since $2j - 3k$ is an integer, $a \mid 2b - 3c$.

<details class="solution" markdown>
<summary>Solution</summary>

1. H.
2. D (definition of divides, applied to each hypothesis, with a different letter for each).
3. L (substitution into the expression, using line 2).
4. A (the distributive property, pulling out the factor $a$).
5. D (definition of divides, with the integer $2j - 3k$), plus R (a combination of integers is an integer).

Check: $a = 5$, $b = 15$, $c = 10$ give $j = 3$, $k = 2$, and $2b - 3c = 0 = 5 \cdot (6 - 6)$ with $2j - 3k = 0$. With $c = 20$ instead, $k = 4$ and $2b - 3c = 30 - 60 = -30 = 5 \cdot (-6)$ with $2j - 3k = 6 - 12 = -6$.

</details>

3\. (Reviews [conditionals and biconditionals](../02-logic-and-sets/02-conditionals-and-biconditionals.md).) What does this proof prove, and is it a proof of the stated claim? *Claim:* if $n^2$ is even, then $n$ is even. "Proof. Let $n$ be even, so $n = 2k$ for an integer $k$. Then $n^2 = 4k^2 = 2(2k^2)$, which is even."

<details class="solution" markdown>
<summary>Solution</summary>

The proof assumes "$n$ is even" and derives "$n^2$ is even". That is the converse of the claim, "if $n$ is even, then $n^2$ is even". The converse is true, but a proof of it doesn't prove the claim, since a conditional and its converse are different statements. (For $n^2$ even, the first line should assume $n^2$ is even, or the proof should be a proof of the contrapositive: if $n$ is odd, then $n^2$ is odd.)

Question 8 catches this at once: the first line assumes the claim's conclusion ("$n$ is even"), and the last line reaches the claim's hypothesis ("$n^2$ is even"). The two have traded places.

Check: $n = 6$ gives $n^2 = 36$, and the proof's algebra works ($k = 3$, $36 = 2 \cdot 18$). The proof is a correct proof of a different theorem.

</details>

### Standard

4\. Read this proof. (a) Fill in the "clearly" step. (b) State the hidden lemma. *Claim:* if $4 \mid n$ and $6 \mid n$, then $12 \mid n$. "Proof. Write $n = 4a$ and $n = 6b$. Then $4a = 6b$, so $2a = 3b$. Clearly $a$ is divisible by 3, so $a = 3c$, and $n = 4a = 12c$."

<details class="solution" markdown>
<summary>Solution</summary>

(a) From $2a = 3b$ we want $3 \mid a$. Write $a = 3q + r$ with $r \in \{0, 1, 2\}$ (the remainder on division by 3). Then $2a = 6q + 2r$, and $2a = 3b$ is divisible by 3, so $2r = 2a - 6q$ is divisible by 3. The possible values of $2r$ are 0, 2 and 4, and only 0 is divisible by 3. So $r = 0$, which means $a = 3q$. The proof then continues as written: $n = 4a = 12q$.

(b) The hidden lemma is "if $3 \mid 2a$, then $3 \mid a$". It is not true for every divisor in place of 3: $4 \mid 2 \cdot 2$ holds but $4 \nmid 2$. The step needs 3 to be prime (so that it cannot split across the factors 2 and $a$), or the case check above.

Check: $n = 24$ gives $a = 6$, $b = 4$, and $3 \mid 6$ with $q = 2$, so $n = 12 \cdot 2 = 24$.

</details>

5\. Find the invalid line in this "proof" that $2 = 1$. "Let $a = b$. Then $a^2 = ab$. Subtract $b^2$: $a^2 - b^2 = ab - b^2$. Factor: $(a + b)(a - b) = b(a - b)$. Divide by $a - b$: $a + b = b$. Since $a = b$, this says $2b = b$, so $2 = 1$."

<details class="solution" markdown>
<summary>Solution</summary>

The invalid line is "Divide by $a - b$". Since $a = b$, we have $a - b = 0$, and dividing by 0 is not allowed. Question 4 on this line: the tag would be A (algebra), but the rule being used ("cancel a common factor") requires the factor to be nonzero, and the hypothesis $a = b$ says it is zero.

Question 6 (test on numbers) finds it at once: take $a = b = 3$. Then $(a + b)(a - b) = 6 \cdot 0 = 0$ and $b(a - b) = 3 \cdot 0 = 0$. Both sides are 0, and dividing 0 by 0 gives no information.

Check: $a + b = b$ with $a = b = 3$ says $6 = 3$, which is false, and it cannot be derived from the true line $0 = 0$.

</details>

6\. Read the proof of Theorem 4 (AM-GM) in [direct proof](01-direct-proof.md#worked-examples). For each hypothesis, say where it is used and what goes wrong without it.

<details class="solution" markdown>
<summary>Solution</summary>

The hypotheses are $a \ge 0$ and $b \ge 0$. Both are used in one place: to say that $\sqrt{a}$ and $\sqrt{b}$ are real numbers and that $\sqrt{a}\sqrt{b} = \sqrt{ab}$. Without them, the first line "$(\sqrt{a} - \sqrt{b})^2 \ge 0$" has no meaning in the real numbers when $a < 0$ or $b < 0$. With $a = b = -1$, the right side of the claim is $\sqrt{ab} = 1$ while the left side is $-1$, so the inequality fails.

The proof does not use that $a$ and $b$ are different, which is why the equality case $a = b$ is in the statement.

Check: $a = 0$ and $b = 4$ give $\frac{4}{2} = 2 \ge \sqrt{0} = 0$, so the nonnegative boundary case works.

</details>

### Challenge

7\. In the proof that $\sqrt{2}$ is irrational (in [roots, irrationals and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#proving-that-the-square-root-of-2-is-irrational)), the fraction is chosen in simplest form. (a) Where is that choice used? (b) Run the same proof for $\sqrt{4}$, which is rational, and find the line that fails.

<details class="solution" markdown>
<summary>Solution</summary>

(a) It is used only at the end: "$a$ and $b$ are both even, which contradicts our choice of the fraction in simplest form". Without the choice, "both even" is not a contradiction, since $\frac{4}{2}$ is a fine fraction.

(b) Suppose $\sqrt{4} = \frac{a}{b}$ in simplest form. Then $a^2 = 4b^2$, so $a^2$ is even, so $a$ is even, $a = 2k$. Substituting gives $4k^2 = 4b^2$, so $b^2 = k^2$. The proof for $\sqrt{2}$ has $b^2 = 2k^2$ here, which makes $b^2$ even. For $\sqrt{4}$ there is no factor of 2 in front, so $b^2 = k^2$ doesn't make $b$ even. The line "Now $b^2$ is even" fails, and no contradiction follows. In fact $\sqrt{4} = 2 = \frac{2}{1}$ is in simplest form with $a$ even and $b$ odd.

So the proof is sensitive to the 2 in $a^2 = 2b^2$, which is the whole point.

Check: $a = 2$, $b = 1$ satisfies $a^2 = 4b^2$ with $\gcd(a, b) = 1$.

</details>

8\. A student writes: "Let $p_1, \dots, p_n$ be all the primes. Then $N = p_1 \cdots p_n + 1$ is prime, and it is not in the list, a contradiction." Find the false claim and give the counterexample from the lesson. What small change repairs the proof?

<details class="solution" markdown>
<summary>Solution</summary>

The false claim is "$N$ is prime". With the first six primes, $N = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \times 509$, which is composite.

The repair: say that $N > 1$ has some prime divisor $p$ (by the lemma that every integer greater than 1 has one), and show that $p$ is not in the list, because $p = p_i$ would give $p \mid 1$. The proof then needs only that $N$ has a prime divisor, not that $N$ is prime.

Check: $59 \times 509 = 30031$, and neither 59 nor 509 is among $2, 3, 5, 7, 11, 13$.

</details>

## Where this shows up

- The next lesson, [scratch work and proof strategies](03-scratch-work-and-proof-strategies.md), is the other side of the same skill: how to find the chain that you are checking here. Reading a proof well is the best preparation, because every proof you read gives you a pattern to reuse. [How to write a proof](07-how-to-write-a-proof.md) turns the questions above into a checklist for your own writing.
- In CS courses, reading proofs is how you learn algorithm correctness arguments and reductions, and it is the same skill as code review: state what a unit does, check its inputs and outputs, and run a test case ([invariants and algorithm correctness](../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md)).
- In economics, a theorem is a promise that depends on its assumptions, and the reading habit of "where is each hypothesis used?" is how you find out which assumption a result stands on ([profit maximization and market structure](../../07-economics-math/03-firms-and-consumers/03-profit-maximization-and-market-structure.md)).
