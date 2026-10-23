# How to write a proof

After this lesson you can turn scratch work into a finished proof that a classmate can check without asking you anything: state the claim and the method, introduce every letter, write in full sentences, justify the steps that need it, end with the claim, and test the result with a checklist. You can also rewrite a weak proof.

Before this: the other lessons of this chapter, especially [direct proof](01-direct-proof.md) and [scratch work and proof strategies](03-scratch-work-and-proof-strategies.md), and the phrasebook in [proof language: let, suppose, WLOG](../01-language-and-notation/03-proof-language-let-suppose-wlog.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. What is missing from this proof of "if $n$ is even, then $n^2$ is even"? "Let $n$ be even. $n = 2k$. $n^2 = 4k^2$. Done."
2. Rewrite this sentence so it does not start with a symbol and gives its reason: "$n^2 = 2(2k^2)$ is even."
3. Name two things the first sentence of a proof by contradiction should contain.

<details class="solution" markdown>
<summary>Answers</summary>

1. Three things. The letter $k$ is never introduced (where does it come from?). The step from $n^2 = 4k^2$ to "even" is not justified, since the proof does not say that $4k^2 = 2(2k^2)$ with $2k^2$ an integer. And the last word "Done" doesn't say what has been shown. A good version: "Let $n$ be an even integer. Then $n = 2k$ for some integer $k$, so $n^2 = 4k^2 = 2(2k^2)$. Since $2k^2$ is an integer, $n^2$ is even."
2. "Since $n^2 = 2(2k^2)$ and $2k^2$ is an integer, the number $n^2$ is even."
3. The announcement of the method ("Suppose, for contradiction, ...") and the exact negation of the claim.

</details>

## The idea

When you open a pull request, you don't paste your terminal history. You write a description: what the change does, why it is correct, what to look at. Then the diff. The reviewer can't interrupt you, so every question they would have asked is answered on the page. A proof is read the same way, by someone who can't ask you what you meant. A grader, a classmate or you in six months will have nothing but the page.

The previous lessons covered how to find a proof. Writing is a separate skill, and a proof you found can still be written badly. A proof can be correct in your head and unreadable on paper, and a reader who can't follow it will assume it is wrong. The goal of this lesson is the opposite situation: you write each proof so that its correctness is easy to see.

Mathematical writing has three levels. A proof sketch gives the main idea and leaves the details to the reader, which suits a colleague who knows the area. A formal proof spells out every step in a form a program can check, which suits a proof assistant. Between them is the ordinary proof, and it is the target of this book: every step is either stated or something a classmate could fill in at once. The standard for the middle level comes from [what is a proof](../01-language-and-notation/01-what-is-a-proof.md): write for someone who knows the definitions and the earlier results and has not seen your argument.

## Definitions

**Circular reasoning** is an argument that uses the claim itself, or something equivalent to it, as one of its reasons. In plain words, the proof assumes what it is trying to show. "The sum of two rationals is rational because rationals are closed under addition" is circular, since "closed under addition" is the claim.

**Symbol soup** is a string of formulas joined by arrows or equals signs, with few or no words, so that the reader must guess how each formula follows from the last. In plain words, it is a proof where the logic lives in the writer's head. The arrow $\Rightarrow$ is a statement ("implies"), not a way to say "and then", and a chain of arrows hides the reasons.

A finished proof has four parts: the **claim** (a numbered theorem, copied exactly), the **method** (named in the first sentence), the **argument** (the steps, each with a reason) and the **ending** (a sentence that says the claim is proved, then an end mark). In plain words, tell the reader what you will do, do it, and say when you are done.

## How to do it

### Seven rules

1. State what you are proving, and say how. Copy the claim exactly. Then, in the first sentence of the proof, name the method when it is not a plain direct proof: "We prove the contrapositive", "Suppose, for contradiction, that ...", "We consider two cases."
2. Introduce every letter before you use it, and say what kind of object it is. "Let $n$ be an integer", "there is an integer $k$ with $n = 2k$". Use a different letter for each different object.
3. Put one idea in each sentence. A sentence that carries two steps ("so $n^2 = 4k^2$ which is $2(2k^2)$, an even number, as $2k^2$ is an integer") is harder to check than the same steps in two sentences.
4. Write in sentences, with formulas inside them. A sentence is allowed to contain a formula, and a formula is not allowed to replace a sentence. Put words between displayed formulas, and punctuate the displays as part of the sentence. Never begin a sentence with a symbol.
5. Justify the steps that need it. Name the definition ("by the definition of even"), the result ("by the linear combination theorem") or the rule ("by the distributive property"). Say "by algebra" only when a classmate could do the algebra in their head.
6. Keep the order logical. Move forward from the hypothesis to the conclusion. Define a thing before you use it. Leave the scratch work out.
7. End with the claim. Say the last line in the words of the claim ("So $m + n$ is even"), and add the end mark $\blacksquare$. In a contradiction proof, name the contradiction. In a proof by cases, say that the cases cover everything.

### The checklist

Run the finished proof through these questions, one by one. A "no" is something to fix.

| Question | Where it comes from |
|---|---|
| Is the claim copied exactly, with its hypotheses? | rule 1 |
| Does the first sentence name the method, if it isn't direct? | rule 1 |
| Is every letter introduced before it is used, with its type? | rule 2 |
| Does each different object have its own letter? | rule 2 |
| Does every sentence make exactly one step? | rule 3 |
| Does any sentence start with a symbol, or consist only of symbols? | rule 4 |
| Is every arrow $\Rightarrow$ or $\Leftrightarrow$ really a statement being made? | rule 4 |
| Can you point to the reason for every line? | rule 5 |
| Is the proof forward: no line depends on a line below it? | rule 6 |
| Is every hypothesis used, or is its absence explained? | [reading a proof](02-how-to-read-a-proof.md), question 7 |
| Does the last line say the claim, in the words of the theorem? | rule 7 |
| Is there an end mark? | rule 7 |
| Did the proof avoid "clearly", "obviously" and "it is easy to see"? | rule 5 |

The last row is why this book never writes those words: each of them stands in for a reason you could write.

### Opening and closing sentences by method

| Method | An opening that works | A closing that works |
|---|---|---|
| direct | "Let $x$ be [an object satisfying the hypothesis]." | "So [the conclusion], as claimed." |
| contrapositive | "We prove the contrapositive: if [not $Q$], then [not $P$]. Suppose [not $Q$]." | "This is the contrapositive of the claim, so the claim is true." |
| contradiction | "Suppose, for contradiction, that [the negation of the claim]." | "This contradicts [the named fact]. So the assumption is false, and [the claim] holds." |
| cases | "There are [k] cases, and they cover every [integer, real number]: ..." | "In every case [the conclusion] holds, so it holds in general." |
| existence | "Take [the witness]." | "So [the witness] has the property, and [the object] exists." |

### Typing proofs in Markdown and LaTeX

In this book's Markdown, inline math goes between single dollar signs with no space inside: `$m + n$`. A displayed formula sits between lines of `$$`, with a blank line before and after, and punctuation inside it when the sentence continues or ends there. Italicize the label (`*Proof.*`) and end with `$\blacksquare$`. In a table, write the divides sign as `\mid` and absolute value as `\lvert x \rvert`, since a plain vertical bar ends the table cell. Typing `\ne`, `\le`, `\ge` and `\sqrt{}` covers most proofs of this chapter.

Some tips that apply anywhere you type math:

- Type the words first and the formulas second. Draft the proof as English with blanks, such as "Since ___ is an integer, ___ is even", then fill the blanks.
- For several lines of algebra, use one aligned display so the equals signs line up, and read each line as "which equals".
- Write text inside math with `\text{...}` sparingly. If you are writing "for some integer", it belongs outside the formula.
- Avoid the symbols $\therefore$, $\Rightarrow$ and $\exists$ in the prose of a proof. Write "so", "hence" and "there is".

In a course that uses LaTeX, the `amsthm` package gives you theorem and proof environments that supply the label and the end mark for you:

```latex
\documentclass{article}
\usepackage{amsmath, amsthm, amssymb}
\newtheorem{theorem}{Theorem}

\begin{document}

\begin{theorem}
If $m$ and $n$ are even integers, then $m + n$ is even.
\end{theorem}

\begin{proof}
Let $m$ and $n$ be even integers. Then $m = 2j$ and $n = 2k$ for some
integers $j$ and $k$, so
\begin{align*}
  m + n &= 2j + 2k \\
        &= 2(j + k).
\end{align*}
Since $j + k$ is an integer, $m + n$ is even.
\end{proof}

\end{document}
```

The `proof` environment prints "Proof." at the start and a square at the end, and `align*` lines the equals signs up. The same habits apply: a sentence before the display, a reason after it.

## Worked examples

<div class="example" markdown>

### Example 1: a circular proof

*Claim.* If $n$ is an integer and $n^2$ is even, then $n$ is even.

*Weak version.* "Since $n^2$ is even, $n \cdot n$ is even. A product is even only if one of its factors is even, so $n$ is even."

What is wrong. The second sentence says that an even product has an even factor. Applied to $n \cdot n$, that is the claim itself in other words (if $n \cdot n$ is even, then $n$ is even). The proof uses what it set out to prove as a reason. The reader who asks "why does an even product have an even factor?" gets no answer, and has found the gap.

What we know and want. We know $n^2$ is even. We want $n$ even. The hypothesis is hard to unpack (an integer equation in $n^2$), so the plan is the contrapositive, which starts from something concrete.

*Rewrite.* We prove the contrapositive: if $n$ is odd, then $n^2$ is odd. Suppose $n$ is odd, so $n = 2k + 1$ for some integer $k$. Then

$$
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.
$$

Since $2k^2 + 2k$ is an integer, $n^2$ is odd. This is the contrapositive of the claim, so if $n^2$ is even, then $n$ is even. $\blacksquare$

Look back: the rewrite names its method, introduces $k$, gives the computation, and ends with the claim. It never relies on "an even product has an even factor". Check: $n = 5$, $k = 2$, $n^2 = 25 = 2 \cdot 12 + 1$ with $12 = 2k^2 + 2k$.

</div>

<div class="example" markdown>

### Example 2: a missing quantifier

*Claim.* For every real number $x$ there is a real number $y$ with $y^2 > x$.

*Weak version.* "Take $y = x + 1$. Then $y^2 > x$."

What is wrong. The letter $x$ is never introduced, so the reader doesn't know whether $x$ is a fixed number or a variable, and the claim is "for every". The witness $y = x + 1$ depends on $x$, which is allowed, but only if $x$ comes first. And "then $y^2 > x$" is the whole claim stated again, with no reason. The weak version has the right idea and none of the proof.

What we know and want. We know nothing about $x$ except that it is real. We want a $y$ built from $x$ with $y^2 > x$. The plan: use $y = x + 1$, and check by computing $y^2 - x$.

*Rewrite.* Let $x$ be a real number. Put $y = x + 1$. Then

$$
y^2 - x = x^2 + 2x + 1 - x = x^2 + x + 1 = \left(x + \tfrac{1}{2}\right)^2 + \tfrac{3}{4}.
$$

A square is at least 0, so $y^2 - x \ge \frac{3}{4} > 0$, and $y^2 > x$. So for the arbitrary $x$ we have found a real number $y$ with $y^2 > x$. $\blacksquare$

Look back: the rewrite introduces $x$ with "Let", builds $y$ from $x$ in the right order, and proves the inequality instead of asserting it. Check: $x = -3$ gives $y = -2$ and $y^2 = 4 > -3$, and $x = 0.5$ gives $y = 1.5$ and $y^2 = 2.25 > 0.5$.

</div>

<div class="example" markdown>

### Example 3: symbol soup

*Claim.* If $a \mid b$ and $a \mid c$, then $a \mid b + c$.

*Weak version.* "$a \mid b \Rightarrow b = ak \Rightarrow c = aj \Rightarrow b + c = ak + aj = a(k + j) \Rightarrow a \mid b + c$."

What is wrong. Read the arrows as statements: "$b = ak$ implies $c = aj$" is false as written, since the first equation says nothing about $c$. The letters $k$ and $j$ appear without being introduced, and the hypothesis $a \mid c$ is never stated, so the reader has to guess where $c = aj$ comes from. The reason that $k + j$ is an integer is missing. The arrows are doing the work of the words "since", "so" and "and", and they are doing it wrongly.

What we know and want. We know $b = ak$ and $c = aj$ for some integers, by the definition. We want $b + c = al$ for an integer $l$. The plan: add the two equations.

*Rewrite.* Let $a \mid b$ and $a \mid c$. By the definition of divides, there are integers $k$ and $j$ with $b = ak$ and $c = aj$. Then

$$
b + c = ak + aj = a(k + j).
$$

Since $k + j$ is an integer, $a$ divides $b + c$. $\blacksquare$

Look back: each sentence makes one step, the letters are introduced where they are born, and the equals chain in the display is a single computation. The arrow is gone, since it was not carrying meaning. Check: $a = 4$, $b = 12$, $c = 20$ give $k = 3$, $j = 5$, and $b + c = 32 = 4 \cdot 8$ with $8 = k + j$.

</div>

<div class="example" markdown>

### Example 4: rewrite it yourself

*Claim.* If $n$ is odd, then $n^2$ is odd.

*Weak version.* "$n = 2k + 1$, $n^2 = 4k^2 + 4k + 1$, which is odd."

Start the rewrite: "Let $n$ be an odd integer. Then $n = 2k + 1$ for some integer $k$. So $n^2 = 4k^2 + 4k + 1$." Finish it. The "which is odd" needs a reason, and the proof needs an ending in the words of the claim.

<details class="solution" markdown>
<summary>Finish</summary>

"... So $n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$. Since $2k^2 + 2k$ is an integer, $n^2$ has the form $2l + 1$ with $l = 2k^2 + 2k$. Hence $n^2$ is odd. $\blacksquare$"

What the rewrite adds: the introduction of $n$ and its type, the step that exposes the form $2l + 1$, the reason that $l$ is an integer, and the final sentence in the words of the claim. Check: $n = 3$, $k = 1$, $l = 4$, $2 \cdot 4 + 1 = 9 = 3^2$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for too little and too much. A proof for a first course can say "by the distributive property" for $2j + 2k = 2(j + k)$. A proof for a later course should not. A proof that explains every algebra step in a paragraph is as hard to read as one that skips them. Calibrate to the audience: a classmate who has the same course and the same results.

</div>

<div class="warning" markdown>

Watch out for leaving scratch work in. Lines such as "we want to show ..." followed by a formula that the proof then treats as known are the backward argument in disguise. "We want to show $X$" is a statement of the goal and belongs at the start. If $X$ appears later as an assumption, you have assumed the conclusion.

</div>

<div class="warning" markdown>

Watch out for the missing ending. A proof that stops after the last computation leaves the reader to decide whether you finished. State the conclusion in the words of the claim, even when it feels redundant: "so $m + n$ is even". It is also the check on yourself, because a proof whose last line doesn't match the claim has proved something else.

</div>

<div class="warning" markdown>

Watch out for a hidden dependence on order. A line such as "Then $k$ is an integer" before $k$ exists, or a lemma used before it is stated, makes the reader jump around. Read the proof once with a finger on each sentence, and ask whether every object in it has already been introduced.

</div>

A proof can be correct and badly written, and a badly written proof can be scored as wrong. The cure is not more symbols; it is more words in the right places.

## Tricks and shortcuts

Read the proof aloud. If you stumble over a sentence, the reader will. If you say "and then" where the page has an arrow, put the word in.

The "blah" test from the style rules: replace each formula by "blah" and read it. "Let blah be an integer. Then blah for some integer blah, so blah. Since blah is an integer, blah is even." That reads as a proof. If the blah version reads as nonsense, you have symbols standing in for sentences.

Write the first and last sentences first. The first says what is assumed and by which method; the last says what is shown. Then fill the middle.

Wait before you hand a proof in. Reading it the next morning, you read what is on the page, not what you meant, and the gaps show up.

Trade proofs with a classmate and mark each other's with the checklist. Finding a gap in someone else's writing teaches you to see your own.

## FAQ

### How long should a proof be?

As long as it takes to make every step checkable, and no longer. A short proof is not better because it is short; a short proof that skips a step is a gap. If a step takes two lines and you have one, write the second line.

### Should I hand in my scratch work?

Only if the assignment asks for it. The proof is the final document. Scratch work belongs in your notebook, and it is worth keeping because it shows where you got stuck.

### Can I use abbreviations such as "iff", "s.t." and "WLOG"?

They are fine in notes and in scratch work. In a proof that others will read, write "if and only if" and "such that" out, and use "without loss of generality" only with a reason. WLOG is a legitimate part of the language, but it must be justified ([proof by cases and WLOG](04-proof-by-cases-and-wlog.md)). Follow your course's convention if it has one.

### Is it wrong to write "QED" instead of the square?

No. "QED" (from the Latin for "which was to be shown"), "as required" and the black square all mean the same. This book uses the square. What matters is that you have some ending.

## Practice

### Warm-up

1\. Name the problem with each sentence from a proof. (a) "$n^2 = 4k^2$ is even." (b) "Therefore $n$ is even." (as the first line of a proof) (c) "$x > 0 \Rightarrow x^2 > 0 \Rightarrow x^2 + 1 > 1$."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) It starts with a symbol, and it gives no reason for "even" ($k$ is not introduced, and the integer $2k^2$ is not mentioned). Fix: "Since $n = 2k$ for an integer $k$, we have $n^2 = 4k^2 = 2(2k^2)$, which is even."
- (b) "Therefore" with nothing before it to follow from. A conclusion needs premises on the page.
- (c) The arrows chain statements with no words. The first arrow is read as "if $x > 0$ then $x^2 > 0$", which is true, but the proof has not said that it assumes $x > 0$ or why squaring keeps positivity. Fix: "Suppose $x > 0$. Then $x^2 > 0$, because a positive number times a positive number is positive. Adding 1 to both sides gives $x^2 + 1 > 1$."

Check: $x = 2$ gives $4 > 0$ and $5 > 1$.

</details>

2\. Write the opening sentence and the closing sentence for each proof. (a) A contrapositive proof of "if $3n + 2$ is odd, then $n$ is odd". (b) A contradiction proof that there is no largest integer. (c) A proof by cases that $n^2 - n$ is even for every integer $n$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Opening: "We prove the contrapositive: if $n$ is even, then $3n + 2$ is even. Suppose $n = 2k$ for an integer $k$." Closing: "So $3n + 2$ is even. This is the contrapositive of the claim, so the claim is true."
- (b) Opening: "Suppose, for contradiction, that $M$ is the largest integer." Closing: "But $M + 1$ is an integer greater than $M$, which contradicts the choice of $M$. So there is no largest integer."
- (c) Opening: "Let $n$ be an integer. Every integer is even or odd, so there are two cases." Closing: "In both cases $n^2 - n$ is even, and the cases cover every integer, so $n^2 - n$ is even for every integer $n$."

Check: each opening names the method, and each closing says what has been shown.

</details>

3\. Use the checklist on this proof, and list every item that fails. *Claim:* for every real number $x$, $x^2 - 2x + 1 \ge 0$. "Proof. $x^2 - 2x + 1 = (x - 1)^2 \ge 0$."

<details class="solution" markdown>
<summary>Solution</summary>

The mathematics is right. The items that fail:

- The letter $x$ is not introduced. A proof of a "for every" claim should begin "Let $x$ be a real number."
- The step $(x - 1)^2 \ge 0$ has no reason. The reason is that the square of a real number is never negative.
- The last line is a formula, and it doesn't state the claim in words.
- There is no end mark.

A good version: "Let $x$ be a real number. Expanding gives $x^2 - 2x + 1 = (x - 1)^2$, and the square of a real number is never negative. So $x^2 - 2x + 1 \ge 0$. $\blacksquare$"

Check: $x = 1$ gives $0 \ge 0$ and $x = -2$ gives $9 \ge 0$.

</details>

### Standard

4\. Rewrite this symbol soup as a proof in sentences. *Claim:* if $x^2 - 5x + 6 = 0$, then $x = 2$ or $x = 3$. "$x^2 - 5x + 6 = 0 \Rightarrow (x - 2)(x - 3) = 0 \Rightarrow x = 2, 3$."

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $x^2 - 5x + 6 = 0$. What we want: $x = 2$ or $x = 3$. The plan: factor, and use the fact that a product is zero only if a factor is.

*Proof.* Let $x$ be a real number with $x^2 - 5x + 6 = 0$. Factoring the left side gives $(x - 2)(x - 3) = 0$. A product of two real numbers is zero only if one of them is zero (the zero-product property). So $x - 2 = 0$ or $x - 3 = 0$, which means $x = 2$ or $x = 3$. $\blacksquare$

Look back: the weak version's "$x = 2, 3$" is ambiguous (does it mean both at once?). The rewrite says "or". Check: $2^2 - 10 + 6 = 0$ and $3^2 - 15 + 6 = 0$.

</details>

5\. Rewrite this circular proof. *Claim:* if $r$ and $s$ are rational, then $r + s$ is rational. "Let $r$ and $s$ be rational. Then $r + s$ is rational, because the rational numbers are closed under addition."

<details class="solution" markdown>
<summary>Solution</summary>

"Closed under addition" says that the sum of two rationals is rational, which is the claim. The proof uses the claim as its reason.

*Rewrite.* Let $r$ and $s$ be rational numbers. By the definition of rational, $r = \frac{a}{b}$ and $s = \frac{c}{d}$ for integers $a$, $b$, $c$, $d$ with $b \ne 0$ and $d \ne 0$. Then

$$
r + s = \frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}.
$$

The numerator $ad + bc$ and the denominator $bd$ are integers, and $bd \ne 0$ because $b \ne 0$ and $d \ne 0$. So $r + s$ is a quotient of integers with nonzero denominator, which means it is rational. $\blacksquare$

Check: $r = \frac{1}{2}$ and $s = \frac{1}{3}$ give $\frac{3 + 2}{6} = \frac{5}{6}$.

</details>

6\. Rewrite this proof, which is missing its quantifier and its reasons. *Claim:* for every integer $n$, the number $n^2 + n + 1$ is odd. "$n^2 + n + 1 = 2k + 1$. So it is odd."

<details class="solution" markdown>
<summary>Solution</summary>

What is wrong: $n$ is not introduced as an arbitrary integer, $k$ is not introduced or identified, and "$n^2 + n + 1 = 2k + 1$" is asserted rather than shown. What we know: $n^2 + n$ is even for every integer $n$ (the theorem in [proof language](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#worked-examples)). What we want: $n^2 + n + 1 = 2k + 1$ for an integer $k$.

*Rewrite.* Let $n$ be an integer. By the theorem that $n^2 + n$ is even for every integer $n$, we have $n^2 + n = 2k$ for some integer $k$. Then $n^2 + n + 1 = 2k + 1$, so $n^2 + n + 1$ is odd. $\blacksquare$

Look back: the original is true, and its "$2k + 1$" is the right shape. The rewrite says where $k$ comes from. Check: $n = 4$ gives $21 = 2 \cdot 10 + 1$ with $k = 10$, since $n^2 + n = 20$.

</details>

### Challenge

7\. Rewrite this proof in full. *Claim:* for every integer $n$, $6 \mid n^3 - n$. "$n^3 - n = (n - 1)n(n + 1)$. Three in a row, so one is divisible by 3 and one by 2. So 6."

<details class="solution" markdown>
<summary>Solution</summary>

What is wrong: $n$ is not introduced, the claims "one is divisible by 3 and one by 2" are asserted without reasons, and the last step from "divisible by 2 and by 3" to "divisible by 6" is skipped, though it needs a reason (it fails for 2 and 4, where $2 \mid 4$ and $4 \mid 4$ but $8 \nmid 4$).

*Rewrite.* Let $n$ be an integer. Factoring, $n^3 - n = (n - 1)n(n + 1)$.

Divisibility by 2. The number $n^2 + n$ is even, so $n^2 + n = 2m$ for an integer $m$, and $n^3 - n = (n - 1)(n^2 + n) = 2(n - 1)m$. So $n^3 - n$ is even.

Divisibility by 3. Every integer is $3q$, $3q + 1$ or $3q + 2$. If $n = 3q$, then 3 divides the factor $n$. If $n = 3q + 1$, then $n - 1 = 3q$. If $n = 3q + 2$, then $n + 1 = 3(q + 1)$. In each case 3 divides a factor of the product, so $n^3 - n = 3t$ for an integer $t$.

Combining. Since $3t$ is even, $t$ is even: if $t$ were odd, $3t$ would be a product of odd integers, which is odd. So $t = 2u$, and $n^3 - n = 6u$. Hence $6 \mid n^3 - n$. $\blacksquare$

Check: $n = 5$ gives $120 = 6 \cdot 20$ (the case $n = 3 \cdot 1 + 2$ with factor $n + 1 = 6$), and $n = 4$ gives $60 = 6 \cdot 10$ (the case $n = 3 \cdot 1 + 1$ with factor $n - 1 = 3$).

</details>

8\. (Reviews [reading math symbols](../01-language-and-notation/04-reading-math-symbols.md).) Read $\forall n \in \mathbb{N}\ \exists p\ (p \text{ is prime and } p > n)$ aloud as a sentence, then prove it in full sentences, using Theorem 2 of [proof by contradiction](06-proof-by-contradiction.md#worked-examples).

<details class="solution" markdown>
<summary>Solution</summary>

In words: for every natural number $n$ there is a prime greater than $n$. The statement is "for every, then there exists", so $n$ comes first and the prime may depend on $n$.

What we know: there are infinitely many primes (Theorem 2). What we want: for the given $n$, a prime above it. The plan: contradiction, because a prime that is at most $n$ can be one of only finitely many numbers.

*Proof.* Let $n$ be a natural number. Suppose, for contradiction, that every prime is at most $n$. Then every prime is one of the numbers $0, 1, \dots, n$, so there are at most $n + 1$ primes. That contradicts the theorem that there are infinitely many primes. Hence some prime $p$ satisfies $p > n$. $\blacksquare$

Look back: the proof is short because the infinitude of primes does the work. Check: $n = 10$ gives $p = 11$, and $n = 100$ gives $p = 101$.

</details>

## Where this shows up

- This is the last lesson of the chapter. The next chapter, more proof methods, applies the writing rules to [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md) and [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md), and [common proof mistakes](../07-putting-it-together/01-common-proof-mistakes.md) collects the errors the checklist is built to catch. [Mixed proof practice](../07-putting-it-together/02-mixed-proof-practice.md) is where to apply all of it.
- In CS courses, proofs are graded on the writing as well as the idea: a correctness argument for an algorithm, a reduction in the theory of computation (reductions and undecidability<!-- link: ../../06-cs-math/06-theory-of-computation/06-reductions-and-undecidability.md -->) and the arguments in a design document all follow the same layout of claim, method, steps and ending.
- In economics, a result is written as a model with stated assumptions, a theorem and a proof, so the habit of naming what is assumed and what is concluded carries over ([profit maximization and market structure](../../07-economics-math/03-firms-and-consumers/03-profit-maximization-and-market-structure.md)).
