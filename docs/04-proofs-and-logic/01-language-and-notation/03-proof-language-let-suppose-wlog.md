# Proof language: let, suppose, WLOG

After this lesson you can read and write the standard phrases of a proof, say what each one does, name every object before you use it, and use "without loss of generality" only when it is justified.

Before this: [what is a proof](01-what-is-a-proof.md) and [definitions, theorems, lemmas and corollaries](02-definitions-theorems-lemmas-corollaries.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. What is the difference between "Let $n$ be an integer" and "Let $n = 3$"? Which of the two can start a proof that every integer has some property?
2. A proof says "Suppose $n$ is even. Then $n = 2k$." Where does $k$ come from? What would be wrong with using $k$ in the sentence before this one?
3. For which of these claims is "without loss of generality, $a \le b$" legitimate? (i) For all integers $a$ and $b$, the numbers $a - b$ and $b - a$ are both even or both odd. (ii) For all integers $a$ and $b$, $a - b < 5$.

<details class="solution" markdown>
<summary>Answers</summary>

1. "Let $n$ be an integer" introduces an arbitrary integer, about which we assume only that it is an integer. "Let $n = 3$" fixes one particular value. Only the first can start a proof about every integer.
2. The integer $k$ comes from the definition of even: because $n$ is even, there exists an integer $k$ with $n = 2k$. Before that sentence, no letter $k$ has been introduced, so using it would be using a name nobody has defined.
3. Only (i). Swapping $a$ and $b$ turns the statement into itself, so assuming $a \le b$ loses nothing. In (ii), swapping turns "$a - b < 5$" into "$b - a < 5$", a different claim, and with $a \le b$ it would make (ii) look true when it isn't (take $a = 20$ and $b = 0$).

</details>

## The idea

Proofs are written in a small, stable dialect. A handful of phrases do almost all the work, and each one is a signal to the reader: "a new object is being named", "an assumption starts here", "a conclusion has been reached", "the proof is over". Once you know the signals, a proof becomes much easier to read, because you can see the structure before you check any line, and much easier to write, because the phrase you need is nearly always on the short list below.

If you program, there is a useful comparison. "Let" declares a variable, "suppose" opens a block that holds only under an assumption, and "thus" is a return statement that must be backed by what came before. A letter in a proof has a scope, just as a variable does, and using a letter before you have declared it is the proof version of a `NameError`. The comparison stops at one point: a proof is read by a person, not run, so a missing declaration doesn't crash anything. The reader just stops believing you.

## Definitions

A letter is **arbitrary** when the only things assumed about it are the hypotheses of the claim. In plain words, it stands for any member of the set, and it is not allowed to depend on a special choice. "Let $n$ be an integer" introduces an arbitrary integer. Whatever you prove about it holds for every integer, since $n$ could have been any of them.

Some claims say that an object exists, and a proof of such a claim provides one. A **witness** is an object that shows an existence claim is true. In "$n$ is even if $n = 2k$ for some integer $k$", the integer $k$ is the witness. Proving that $n$ is even means producing a witness. Using the fact that $n$ is even means receiving a witness and giving it a name.

**Without loss of generality** (abbreviated WLOG) introduces an extra assumption in a proof when the general case follows from that special case by symmetry or by renaming. In plain words, it says "the other case is the same argument with the names swapped, so we only write one of them". It is a promise to the reader, and the promise has to be true.

## How to do it

### Name every object before using it

1. Introduce each letter at its first use, with a phrase that gives it a type: "Let $n$ be an integer", "Fix a real number $x > 0$", "Since $n$ is even, there is an integer $k$ with $n = 2k$."
2. Decide whether the letter is arbitrary or particular. A letter for a "for every" statement is arbitrary: you don't know which member it is. A letter obtained from "there exists" is particular, but you know only the property that the existence statement gives it.
3. Give different objects different letters. If two integers are both halves of something, call them $j$ and $k$.
4. Respect scope. A letter introduced inside a case or under a "suppose" belongs to that case. Don't use it after the case ends.
5. Use "let" for objects and "suppose" for assumptions. A sentence like "Suppose $n$ is an integer" is acceptable, but "Let $n$ be an integer" is the habit to build.

### The four moves with "for all" and "there exists"

Quantifier phrases have two directions each. You may be proving the statement or using it as a known fact, and the correct move is different. The details are in the lesson on [quantifiers](../02-logic-and-sets/04-quantifiers.md); this table is the working version.

| The statement | When you must prove it | When you are given it |
|---|---|---|
| for every $x$ in $S$, $P(x)$ | Let $x$ be an arbitrary element of $S$, and prove $P(x)$ | Choose any element of $S$ you like, and conclude $P$ for it |
| there exists $x$ in $S$ with $P(x)$ | Produce a particular $x$ (a witness) and check $P(x)$ | Say "let $x$ be such an element", and use only $P(x)$ |

The phrase "for some" means "there exists", and "for each", "for any" and "for all" mean "for every". Words like "for any" can be ambiguous in plain English ("it is true for any $x$" can mean "for every $x$" or "for some $x$"), so this book uses "for every".

### Assumptions: suppose, assume

"Suppose" and "assume" start an assumption that may not be known to be true. They appear in three places: at the start of a proof of "if $P$, then $Q$" (suppose $P$), at the start of a case (suppose $n$ is even), and at the start of a proof by contradiction. An assumption lasts until the end of the proof or the case it was opened for. When the case ends, the assumption is dropped. Nothing proved under "suppose $n$ is even" is known for odd $n$.

### Using without loss of generality

1. Check that the claim is symmetric in the objects you want to order or rename. If you swap $a$ and $b$ everywhere in the statement, you must get the same statement.
2. State the extra assumption and the reason in one sentence: "Without loss of generality, $a$ is even, since the roles of $a$ and $b$ are interchangeable."
3. Make sure the assumption covers all the cases. Of two objects, one is the first, so "$a \le b$" or "$b \le a$" always holds. If one case remains after your assumption, you still have to deal with it.
4. Prove the special case in full. After it, don't use the case you dropped.

### The phrasebook

| Phrase | What it does | Example |
|---|---|---|
| "Let ... be ..." | Introduces an object, usually arbitrary, with its type. | Let $m$ and $n$ be even integers. |
| "Fix ..." | Same as "let", for an object that stays constant while something else varies. | Fix a real number $x$. |
| "Suppose ..." / "Assume ..." | Opens an assumption (the hypothesis, a case, or a contradiction). | Suppose $n$ is odd. |
| "Then ..." | Moves to a consequence of what is already on the page. | Then $n = 2k + 1$. |
| "So", "thus", "hence", "therefore" | Draws a conclusion from the previous line or lines. | Thus $m + n = 2(j + k)$. |
| "It follows that ..." | A conclusion that takes a short argument, which the sentence before it usually supplies. | It follows that $m + n$ is even. |
| "We claim ..." | States an intermediate fact, to be proved before continuing. | We claim that $j + k$ is an integer. |
| "By definition ..." | Unpacks or applies a definition. Name which one. | By the definition of even, ... |
| "Since ..." / "because ..." | Gives the reason in the same sentence. | Since $j$ and $k$ are integers, $j + k$ is an integer. |
| "There exists ..." / "for some ..." | States (or gives) a witness. | There is an integer $k$ with $n = 2k$. |
| "For every ..." / "for each ..." | States that something holds for all members of a set. | For every integer $n$, $n^2 \ge 0$. |
| "... such that ..." | Attaches a property to an object being introduced. | an integer $k$ such that $n = 2k$ |
| "Without loss of generality" | Narrows to one case by symmetry. | WLOG, $a$ is even. |
| "In particular ..." | Applies a general fact to one specific case. | In particular, $0$ is even. |
| "Conversely ..." | Starts the proof of the opposite direction. | Conversely, suppose $n = 2k$ ... |
| "as required", "which is what we wanted", QED, $\blacksquare$ | Says the last line is the claim. | So $m + n$ is even, as required. $\blacksquare$ |

A word on "so", "thus", "hence" and "therefore": they all say "the next statement follows from what you just read". They are not interchangeable with "and". Each one is a small promise that the reason is on the page, so use them only when it is.

### Words that hide a step

Some textbooks write "clearly", "obviously", "trivially" or "it is easy to see" before a statement. These words mean "the justification is short and routine, and the author expects you to supply it". They are not arguments, and some authors have used them on statements that were false. When you read such a word, treat the sentence as an exercise: write out the step yourself. When you write, don't use them. Say why instead, or if the step is truly routine, say "by algebra" and make sure your classmate could fill it in at once.

### Good and bad sentences

| Bad sentence | What is wrong | Good sentence |
|---|---|---|
| "Let $n = 4$. Then $n^2 = 16$ is even." | One value, not an arbitrary integer. It proves a fact about 4. | "Let $n$ be an even integer. Then $n = 2k$ for some integer $k$." |
| "Since $n = 2k$, we get $n^2 = 4k^2$." (no earlier mention of $k$) | The letter $k$ appears out of nowhere. | "Since $n$ is even, $n = 2k$ for some integer $k$. So $n^2 = 4k^2$." |
| "Let $m = 2k$ and $n = 2k$." | One letter for two integers forces $m = n$. | "Let $m = 2j$ and $n = 2k$." |
| "Thus $n$ is even." (as the first line) | "Thus" with nothing before it to follow from. | "Since $n = 2l$ for the integer $l$, $n$ is even." |
| "Suppose $n$ is even. ... So $n^2$ is even. Therefore $n$ is even." | The assumption is mixed up with the conclusion. | End with "Therefore $n^2$ is even." |
| "WLOG $a < b$. Then $a - b < 0$." (for a claim about $a - b$) | $a - b$ changes when $a$ and $b$ swap, so WLOG is not available. | Treat both orders, or choose a quantity that does not change, such as $\lvert a - b \rvert$. |

## Worked examples

<div class="example" markdown>

### Example 1: a proof with its phrases marked

*Theorem 1.* For every integer $n$, the number $n^2 + n$ is even.

We use the steps from "Name every object before using it" and the phrasebook. The notes in square brackets say what each sentence does.

*Proof.* Let $n$ be an integer. [Introduces an arbitrary integer: step 1 and step 2.] Every integer is even or odd (the division algorithm with divisor 2), so we consider the two cases. [A claim that makes the cases cover everything.]

Case 1: suppose $n$ is even. [Opens an assumption for this case only.] Then $n = 2k$ for some integer $k$. [Definition of even gives a witness, named $k$.] So

$$
n^2 + n = 4k^2 + 2k = 2(2k^2 + k).
$$

[Substitution and factoring.] Since $2k^2 + k$ is an integer, $n^2 + n$ is even. [Matches the definition.]

Case 2: suppose $n$ is odd. [The Case 1 assumption is gone; a new one begins.] Then $n = 2k + 1$ for some integer $k$. [A new witness, again named $k$, because the old $k$ is out of scope.] So

$$
n^2 + n = (4k^2 + 4k + 1) + (2k + 1) = 4k^2 + 6k + 2 = 2(2k^2 + 3k + 1),
$$

and $2k^2 + 3k + 1$ is an integer, so $n^2 + n$ is even.

In both cases $n^2 + n$ is even, as required. $\blacksquare$

Check: $n = 5$ is odd with $k = 2$, and $n^2 + n = 30 = 2 \times 15$ with $2k^2 + 3k + 1 = 8 + 6 + 1 = 15$. For $n = 4$, $k = 2$ and $20 = 2 \times 10$ with $2k^2 + k = 10$.

</div>

<div class="example" markdown>

### Example 2: a witness that depends on the arbitrary object

*Theorem 2.* For every integer $n$, there is an odd integer $m$ with $m > n$.

The statement has the shape "for every $n$, there exists $m$". By the table of four moves, we let $n$ be arbitrary, and then produce a witness $m$. The witness may be built from $n$.

*Proof.* Let $n$ be an integer. Put $m = 2\lvert n \rvert + 1$. This is an odd integer, since it has the form $2k + 1$ with the integer $k = \lvert n \rvert$. To see that $m > n$, note that $\lvert n \rvert \ge 0$ and $\lvert n \rvert \ge n$, so $2\lvert n \rvert \ge \lvert n \rvert \ge n$. Adding 1 gives $m = 2\lvert n \rvert + 1 > n$. $\blacksquare$

Look back: the order matters. The witness $m = 2\lvert n \rvert + 1$ uses $n$, so $n$ had to be introduced first. If the statement were "there exists an $m$ such that for every $n$, $m > n$" (the same words in a different order), no single $m$ could beat every integer, and the claim would be false.

Check: $n = -7$ gives $m = 15$, and $n = 4$ gives $m = 9$. Both are odd and bigger than $n$.

</div>

<div class="example" markdown>

### Example 3: a legitimate WLOG

*Theorem 3.* Let $a$ and $b$ be integers. If $a$ is even or $b$ is even, then $ab$ is even.

Check the symmetry first (step 1 of using WLOG): swapping $a$ and $b$ turns the hypothesis "$a$ is even or $b$ is even" into "$b$ is even or $a$ is even", the same statement, and turns the conclusion "$ab$ is even" into "$ba$ is even", which is the same because $ba = ab$.

*Proof.* Suppose $a$ is even or $b$ is even. Without loss of generality, $a$ is even, because the hypothesis and the conclusion are unchanged when $a$ and $b$ are swapped. Then $a = 2k$ for some integer $k$, so $ab = 2kb = 2(kb)$, and $kb$ is an integer. Hence $ab$ is even. $\blacksquare$

Look back: the proof is half as long as writing both cases, and the second case would be a copy of the first with $a$ and $b$ exchanged. The reason must be given, and here it is, in the clause after "because". Check: $a = 3$ and $b = 10$ makes $b$ the even one; the proof with the names swapped gives $b = 2 \times 5$ and $ab = 30 = 2 \times 15$.

</div>

<div class="example" markdown>

### Example 4: the product of two odd integers (finish it yourself)

*Theorem 4.* If $m$ and $n$ are odd integers, then $mn$ is odd.

*Proof.* Let $m$ and $n$ be odd integers. Then $m = 2j + 1$ and $n = 2k + 1$ for some integers $j$ and $k$. Multiplying out,

$$
mn = (2j + 1)(2k + 1) = 4jk + 2j + 2k + 1.
$$

Now finish the proof: factor so that one 2 appears, say why the remaining factor is an integer, and match the result to the definition of odd.

<details class="solution" markdown>
<summary>Finish</summary>

Group the first three terms: $mn = 2(2jk + j + k) + 1$. The number $2jk + j + k$ is an integer, because $j$ and $k$ are integers. So $mn = 2l + 1$ with $l = 2jk + j + k$, and $mn$ is odd. $\blacksquare$

Check: $m = 3$ and $n = 7$ give $j = 1$ and $k = 3$, so $l = 6 + 1 + 3 = 10$, and $2 \times 10 + 1 = 21 = 3 \times 7$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for "let $n = 3$" when you mean any integer. A proof that begins with a particular value proves a statement about that value. If you want a general statement, name the object by a letter and say what it is. Using a specific number is right in two situations only: when the claim is about that number, and when you are giving a witness or a counterexample.

</div>

<div class="warning" markdown>

Watch out for a letter that has not been introduced, and for a letter reused. The usual symptom is a line like "$n = 2k$" that appears with no "for some integer $k$" before it. The other symptom is the same letter standing for two different integers in one argument (the first warning in [what is a proof](01-what-is-a-proof.md#edge-cases-and-common-mistakes)). Both come from losing track of which objects exist at that point.

</div>

<div class="warning" markdown>

Watch out for carrying an assumption out of its scope. If Case 1 supposes $n$ is even, nothing in Case 1 can be used in Case 2, and the final conclusion of the proof can't depend on either case's assumption. The same applies to a contradiction: the assumption you make to reach a contradiction is false, so the proof never states it as a fact.

</div>

<div class="warning" markdown>

Watch out for WLOG on a claim that isn't symmetric. In the claim "if $ab$ is even, then $a$ is even", swapping $a$ and $b$ produces a different claim, "if $ab$ is even, then $b$ is even". A proof that says "without loss of generality $a$ is even" has assumed the conclusion. The claim is false: $a = 3$ and $b = 2$ give $ab = 6$, which is even, with $a$ odd.

</div>

<div class="warning" markdown>

Watch out for the order of "for every" and "there exists". "For every $x$ there is a $y$ with $y > x$" is true for integers, and "there is a $y$ such that for every $x$, $y > x$" is false (take $x = y$). The two read almost alike, and the proof of each begins differently, as Example 2 shows. The phrase "such that" doesn't tell you the order, so read the quantifiers from left to right.

</div>

The phrase "by definition" is incomplete without a name. Write "by the definition of even" or "by the definition of divides", so that your classmate knows which definition to unpack.

## Tricks and shortcuts

The shape of the claim tells you what the first line of the proof is. Write that line before anything else:

| The claim has the shape | The proof starts with |
|---|---|
| For every $x$ in $S$, $P(x)$ | "Let $x$ be an element of $S$." |
| If $P$, then $Q$ | "Suppose $P$." |
| There exists $x$ with $P(x)$ | "Take $x = \dots$" and then check $P(x)$. |
| $P$ and $Q$ | Prove $P$, then prove $Q$. |
| $P$ or $Q$ | "Suppose $P$ is false" and prove $Q$, or split into cases. |
| $P$ if and only if $Q$ | "Forward direction: suppose $P$ ..." and then "Backward direction: suppose $Q$ ..." |

The last two rows are developed in [proof by cases and WLOG](../03-core-proof-methods/04-proof-by-cases-and-wlog.md) and [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md).

A reader-friendly habit: end every proof with a sentence that repeats the claim in the words of the theorem ("So $mn$ is odd"), and then the end mark. It lets the reader check that you proved what you set out to prove.

## In code

The scoping idea has a direct translation. Writing "let $n$ be an integer" is like writing a function with a parameter: the code has to work for every input. Writing "let $n = 3$" is an assignment. "For every" is `all`, "there exists" is `any`, and a witness is the value `next` finds. A computer tests these on a finite range, so it supports a claim and doesn't prove it.

<details class="code" markdown>
<summary>In code</summary>

```python
n = 3                                    # "let n = 3": one particular value

def n_squared_plus_n_is_even(n):         # "let n be an integer": the code must work for any input
    return (n * n + n) % 2 == 0

print(all(n_squared_plus_n_is_even(m) for m in range(-50, 51)))    # True: "for every", tested on 101 values
print(any(m * m == 2 for m in range(-50, 51)))                     # False: no integer has square 2
print(next(k for k in range(100) if 2 * k + 1 == 37))              # 18: the witness k in 37 = 2k + 1

a, b = 8, 3
print(abs(a - b) == abs(min(a, b) - max(a, b)))     # True: sorting first (WLOG a <= b) keeps |a - b|
print(a - b == min(a, b) - max(a, b))               # False: but it changes a - b from 5 to -5
```

The last two lines are the WLOG rule in code. Putting the smaller number first is safe for a quantity that is the same either way round, such as $\lvert a - b \rvert$, and unsafe for one that isn't, such as $a - b$.

</details>

## FAQ

### Is there a difference between "suppose" and "assume"?

Not in meaning. Many writers use "assume" for the standing hypotheses of a section and "suppose" for a local assumption in a proof, but nothing depends on the choice. Pick one and keep it.

### Why do proofs say "we" instead of "I"?

It is a convention: the writer and the reader carry out the argument together ("we see that..."). It also keeps the focus on the argument, not on who made it. Use "we" in your own proofs unless your course says otherwise.

### Do I have to write "as required" or draw the square at the end?

No, but you do need some signal that the proof is finished, so the reader knows you aren't trailing off. Courses differ: "$\blacksquare$", "QED" and "as required" are all common. This book uses the black square.

### Can I use $\forall$, $\exists$ and $\Rightarrow$ in my proofs?

It depends on your course, and this book's rule is to write the connecting words in prose and keep symbols for formulas. The proofs in this chapter say "for every" and "there exists". The lesson [reading math symbols](04-reading-math-symbols.md) explains what each symbol means and when a symbolic sentence is clearer than a worded one.

## Practice

### Warm-up

1\. Say what each sentence does: introduces a new object, opens an assumption, draws a conclusion, or states a definition. (a) "Let $x$ be a real number." (b) "Suppose that $x > 0$." (c) "Choose an integer $k$ with $n = 2k$." (d) "Thus $n^2$ is even." (e) "By the definition of divides, $b = ak$ for some integer $k$."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Introduces a new object, an arbitrary real number.
- (b) Opens an assumption, which holds for the part of the proof that follows.
- (c) Introduces a new object, a witness named $k$, which exists because $n$ is even.
- (d) Draws a conclusion, from the lines before it.
- (e) Applies (unpacks) a definition, and names a witness $k$ in doing so.

Check: only (d) should be backed by reasons in the lines above it, and it is the one that begins with "thus".

</details>

2\. Each sentence is a bad proof sentence. Rewrite it. (a) "Let $n = 6$. Then $n$ is even, so $n^2$ is even." (b) "Then $n = 2k$, so $n + 2 = 2k + 2$." (c) "Let $a = 2k$ and $b = 2k$ be even integers."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Replace the particular value with an arbitrary one: "Let $n$ be an even integer. Then $n = 2k$ for some integer $k$, so $n^2 = 4k^2 = 2(2k^2)$, which is even." The original proves a fact about 6 only.
- (b) Introduce $k$: "Since $n$ is even, $n = 2k$ for some integer $k$, so $n + 2 = 2k + 2 = 2(k + 1)$."
- (c) Use two letters: "Let $a = 2j$ and $b = 2k$ be even integers, where $j$ and $k$ are integers." With one letter, $a$ and $b$ would be forced to be equal.

Check (a) with $n = 6$: $n^2 = 36 = 2 \times 18$ and $18 = 2k^2$ with $k = 3$.

</details>

3\. Write the first sentence of a proof of each claim. (a) For every real number $x$, $x^2 \ge 0$. (b) If $n$ is odd, then $n + 1$ is even. (c) There is an even prime. (d) For every integer $n$ there is an integer $m$ with $m > n$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) "Let $x$ be a real number."
- (b) "Suppose $n$ is odd." (Or: "Let $n$ be an odd integer.")
- (c) "Take $p = 2$." The proof then checks that 2 is prime and even.
- (d) "Let $n$ be an integer." The proof then names $m = n + 1$.

Check: (a) and (d) begin with "let" because they are "for every" claims, and (c) begins with a choice because it is a "there exists" claim.

</details>

### Standard

4\. Prove that for every integer $n$, the number $3n^2 + n$ is even. Use two cases.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $n$ is an integer, so $n$ is even or odd. What we want: $3n^2 + n = 2l$ for some integer $l$. The plan: substitute $n = 2k$ and $n = 2k + 1$ in turn, and factor out 2.

*Proof.* Let $n$ be an integer. Every integer is even or odd, so there are two cases.

Case 1: suppose $n$ is even, so $n = 2k$ for some integer $k$. Then $3n^2 + n = 12k^2 + 2k = 2(6k^2 + k)$, and $6k^2 + k$ is an integer.

Case 2: suppose $n$ is odd, so $n = 2k + 1$ for some integer $k$. Then

$$
3n^2 + n = 3(4k^2 + 4k + 1) + 2k + 1 = 12k^2 + 14k + 4 = 2(6k^2 + 7k + 2),
$$

and $6k^2 + 7k + 2$ is an integer.

In both cases $3n^2 + n$ is twice an integer, so it is even. $\blacksquare$

Check: $n = 3$ gives $27 + 3 = 30 = 2 \times 15$, and $k = 1$ gives $6 + 7 + 2 = 15$. For $n = 4$ (even, $k = 2$), $48 + 4 = 52 = 2 \times 26$ and $6k^2 + k = 24 + 2 = 26$.

</details>

5\. Find the error in this proof, and say whether the claim is true. Claim: if $a$ and $b$ are integers and $ab$ is even, then $a$ is even. "Proof. Suppose $ab$ is even. Then one of $a$ and $b$ is even. Without loss of generality, $a$ is even. So $a$ is even, as required."

<details class="solution" markdown>
<summary>Solution</summary>

The error is the "without loss of generality". The conclusion is about $a$ in particular, so $a$ and $b$ are not interchangeable: swapping them changes the claim from "$a$ is even" to "$b$ is even". The sentence assumes the thing to be proved.

The claim is false. Take $a = 3$ and $b = 2$: the product $6$ is even, and $a = 3$ is odd. The true statement is "if $ab$ is even, then $a$ is even or $b$ is even".

Check: $3 \times 2 = 6 = 2 \times 3$, so $ab$ is even while $a$ is odd.

</details>

6\. Use WLOG correctly to prove: if $a$ and $b$ are integers, one even and one odd, then $a + b$ is odd. State the symmetry that justifies it.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: one of the two integers is even and the other is odd. What we want: $a + b = 2l + 1$ for some integer $l$. The plan: assume the even one is $a$, by symmetry, and add.

The hypothesis "one of $a$, $b$ is even and the other odd" and the conclusion "$a + b$ is odd" are both unchanged by swapping $a$ and $b$, because $a + b = b + a$. So WLOG applies.

*Proof.* Let $a$ and $b$ be integers, one even and one odd. Without loss of generality, $a$ is even and $b$ is odd, since the hypothesis and the conclusion are unchanged when $a$ and $b$ are swapped. Then $a = 2j$ and $b = 2k + 1$ for some integers $j$ and $k$, so $a + b = 2(j + k) + 1$, and $j + k$ is an integer. Hence $a + b$ is odd. $\blacksquare$

Check: $a = 7$ and $b = 10$ (the even one second): swapping the names, $10 = 2 \times 5$ and $7 = 2 \times 3 + 1$, so the sum is $2 \times 8 + 1 = 17$.

</details>

### Challenge

7\. Prove that every odd integer is a difference of two squares: for every odd integer $n$, there exist integers $a$ and $b$ with $n = a^2 - b^2$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $n$ is odd, so $n = 2k + 1$ for an integer $k$. What we want: integers $a$ and $b$, built from $k$, with $a^2 - b^2 = n$. The plan: try consecutive integers. We have $(k + 1)^2 - k^2 = 2k + 1$.

*Proof.* Let $n$ be an odd integer. Then $n = 2k + 1$ for some integer $k$. Put $a = k + 1$ and $b = k$. Both are integers, and

$$
a^2 - b^2 = (k + 1)^2 - k^2 = k^2 + 2k + 1 - k^2 = 2k + 1 = n.
$$

So $n$ is a difference of two squares. $\blacksquare$

Look back: the witnesses $a$ and $b$ depend on $n$ through $k$, as in Example 2, and $n$ was introduced first. Check: $n = 7$ has $k = 3$, and $4^2 - 3^2 = 16 - 9 = 7$. For $n = -5$, $k = -3$ and $(-2)^2 - (-3)^2 = 4 - 9 = -5$.

</details>

8\. (Reviews [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md).) The two-column proof in that lesson shows that if $M$ is the midpoint of $AB$ and $AB = 10$, then $AM = 5$. Write it as a paragraph proof, using the phrases of this lesson, and mark which phrase introduces an object, which opens a hypothesis and which gives a reason.

<details class="solution" markdown>
<summary>Solution</summary>

*Proof.* Let $A$ and $B$ be points and let $M$ be the midpoint of segment $AB$, where $AB = 10$. [Introduces the objects and states the hypothesis.] By the definition of midpoint, $AM = MB$. [Reason: a named definition.] Since $M$ is between $A$ and $B$, the segment addition postulate gives $AM + MB = AB$. [Reason: a named postulate.] Substituting $AM$ for $MB$ and 10 for $AB$ gives $2AM = 10$. Therefore $AM = 5$, by dividing both sides by 2, as required. $\blacksquare$

Check: $5 + 5 = 10$, and each sentence in the paragraph matches one row of the original table: the same five reasons, in the same order.

</details>

## Where this shows up

- The next lesson, [reading math symbols](04-reading-math-symbols.md), turns the same phrases into symbols, and the core methods start with [direct proof](../03-core-proof-methods/01-direct-proof.md) and [how to write a proof](../03-core-proof-methods/07-how-to-write-a-proof.md), which apply this phrasebook to whole proofs. [Proof by cases and WLOG](../03-core-proof-methods/04-proof-by-cases-and-wlog.md) returns to the last phrase in detail.
- Proof assistants such as Lean use the same moves as commands: introducing an arbitrary object (`intro`), taking a witness out of an existence statement (`obtain`), and splitting into cases. A formal proof is a written proof in which every "let", "suppose" and "so" is checked by a program.
- In economics, "without loss of generality, normalize the price of good 2 to 1" is a WLOG. It is valid when multiplying every price by the same positive number changes no choice, so one price can be fixed at 1 without losing any case.
