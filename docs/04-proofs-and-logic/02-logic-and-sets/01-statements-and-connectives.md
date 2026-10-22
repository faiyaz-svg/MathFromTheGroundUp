# Statements and connectives

After this lesson you can decide whether a sentence is a statement, build compound statements with not, and, or and exclusive or, find their truth values from a truth table, and translate between English, symbols and Python conditions.

Before this: [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md) (hypothesis and conclusion) and [compound inequalities and interval notation](../../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md) (what "and" and "or" do to solution sets). The first lesson of this folder, [what is a proof](../01-language-and-notation/01-what-is-a-proof.md), says why a proof needs this precision.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Which of these are statements? (a) $3 + 4 = 8$. (b) Is 7 prime? (c) $x > 2$. (d) Every even integer greater than 2 is the sum of two primes.
2. Let $P$ be "$5 > 3$" and $Q$ be "7 is even". Find the truth value of $P \wedge Q$, $P \vee Q$, $\neg P \vee Q$ and $P \oplus Q$.
3. With `x = 5`, what does Python print for `(x > 3) and (x % 2 == 0)`, and for `not (x > 3) or x < 10`?

<details class="solution" markdown>
<summary>Answers</summary>

1. (a) is a statement, and a false one. (b) is a question, so it is not a statement. (c) is not a statement, because its truth depends on $x$. (d) is a statement: it is either true or false, even though nobody knows which (it is Goldbach's conjecture, still open).
2. Here $P$ is true and $Q$ is false. So $P \wedge Q$ is false, $P \vee Q$ is true, $\neg P \vee Q$ is $\text{F} \vee \text{F}$, which is false, and $P \oplus Q$ (exactly one is true) is true.
3. `False`, because $5$ is odd. And `True`: `not (x > 3)` is `False`, but `x < 10` is `True`, and `or` needs only one.

</details>

## The idea

Open a bank's website and filter transactions by "category is groceries and amount is over \$50, or category is restaurants". Is a \$20 restaurant meal in the results? If the filter means "(groceries and over \$50) or restaurants", yes. If it means "groceries and (over \$50 or restaurants)", no. A program can't guess which one you meant. It needs an exact rule for every way of combining conditions.

Logic is that rule book. It starts with the smallest unit, a sentence that is definitely true or definitely false, and then says exactly how to build bigger sentences from small ones and how the truth of the big one depends on the truth of the parts. Everything in this folder rests on this: a proof is a chain of such sentences, and each link has to be judged true or false without wiggle room.

Natural language is full of wiggle room. "Soup or salad" usually means one of the two. "If you mow the lawn, I'll give you \$20" usually also means that if you don't mow it, you get nothing. Math fixes one meaning for each connecting word and sticks to it. The cost is a few conventions to learn. The benefit is that two readers, or a reader and a computer, can never disagree about what a statement says.

## Definitions

### Statements

A **statement** (also called a **proposition**) is a sentence that is either true or false, but not both. Whether it is true is its **truth value**, written T or F.

In plain words, a statement is a claim that can be right or wrong. The sentence "$3 + 4 = 8$" is a statement whose truth value is F. "Toronto is in Ontario" is a statement with value T. A statement doesn't have to be known: "there are infinitely many primes $p$ with $p + 2$ also prime" is a statement, because it is one or the other, even though nobody has settled which.

Many sentences are not statements.

- Questions and commands: "Is 7 prime?" and "Solve $x^2 = 9$" are neither true nor false.
- Open sentences: "$x + 2 = 5$" and "$n$ is even" contain a variable with no value, so they have no truth value yet. Write $P(x)$ for such a sentence. Plugging in a value ($x = 3$) turns it into a statement, and so does a quantifier, which is the subject of [quantifiers](04-quantifiers.md).
- Sentences that depend on the speaker or the moment: "it is raining" is a statement only once we say where and when.

Letters $P$, $Q$, $R$ stand for statements, as in the [symbols page](../../reference/symbols-and-notation.md#logic). A statement that has no smaller statement inside it is **atomic**.

### The connectives

A **connective** builds a new statement from one or two old ones, and the truth value of the new statement depends only on the truth values of the old ones. There are four to learn now. A **truth table** lists every combination of truth values of the parts, one row each, and gives the truth value of the whole in each row.

**Negation.** The statement $\neg P$ (read "not $P$") is true exactly when $P$ is false.

| $P$ | $\neg P$ |
|---|---|
| T | F |
| F | T |

In plain words, it flips the truth value. If $P$ is "$5 > 3$", then $\neg P$ is "$5 \le 3$", which is false. Notice that $\neg P$ is not "$5 < 3$": the negation of "greater than" is "less than or equal to".

**Conjunction.** The statement $P \wedge Q$ (read "$P$ and $Q$") is true exactly when both $P$ and $Q$ are true.

**Disjunction.** The statement $P \vee Q$ (read "$P$ or $Q$") is true exactly when at least one of $P$ and $Q$ is true. This is the **inclusive or**: it is true when both are true.

**Exclusive or.** The statement $P \oplus Q$ (read "$P$ xor $Q$", or "exactly one of $P$ and $Q$") is true exactly when one of $P$, $Q$ is true and the other is false.

| $P$ | $Q$ | $P \wedge Q$ | $P \vee Q$ | $P \oplus Q$ |
|---|---|---|---|---|
| T | T | T | T | F |
| T | F | F | T | T |
| F | T | F | T | T |
| F | F | F | F | F |

In plain words, "and" is demanding (one false part ruins it), "or" is generous (one true part rescues it), and "xor" is the "or" of a restaurant menu: you may pick one, not both. The only row where $\vee$ and $\oplus$ differ is the first, where both parts are true.

Mathematics uses the inclusive or by default. A mathematician who says "$n$ is even or $n > 10$" accepts $n = 12$. If the exclusive meaning is wanted, it is said outright: "exactly one of", "either ... or ... but not both". The same convention made "or" produce a union in [compound inequalities](../../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md): a number that satisfies both inequalities is a solution, and is listed once.

### Compound statements and precedence

A **compound statement** is built from atomic statements with connectives, such as $(P \vee Q) \wedge \neg R$. A table for it has $2^n$ rows when it involves $n$ atomic statements, because each can be T or F independently: 2 rows for one statement, 4 for two, 8 for three.

Brackets say what is joined to what. Without them, this book uses the standard order of operations for logic:

1. first the negation $\neg$, applying to the smallest statement right after it,
2. then $\wedge$,
3. then $\vee$,
4. then $\Rightarrow$ and $\Leftrightarrow$ (next lesson).

So $\neg P \vee Q \wedge R$ means $(\neg P) \vee (Q \wedge R)$, the same way $-2 + 3 \cdot 4$ means $(-2) + (3 \cdot 4)$. Python has the same order: `not` before `and` before `or`.

Many authors don't trust this and neither should you. When $\wedge$ and $\vee$ appear together, write the brackets, even where the rule would make them unnecessary. A reader should never have to run the precedence rules in their head to understand your statement.

## How to do it

### Evaluating a compound statement

1. Name the atomic statements with letters, and note the truth value of each (or leave them open if you want a full table).
2. Find the main connective, the one applied last. It is the one outside all brackets. With no brackets, it is the connective that binds loosest, so a $\vee$ comes before a $\wedge$, and a $\wedge$ before a $\neg$.
3. Work from the inside out: evaluate each bracket, and then each negation, before the connective that joins them.
4. Write the value under each connective as you go. In a table, give each part its own column.
5. Check by reading the finished statement aloud in English with the values filled in.

### Translating English into symbols

1. Underline the atomic statements and give each a letter. Make each letter a complete statement, not a fragment: $P$ is "the file is saved", not "saved".
2. Replace the connecting words: "and", "but", "although" and "however" become $\wedge$ ("but" adds contrast, not a different truth condition); "or" becomes $\vee$ unless the sentence says "but not both"; "not", "it is false that" and "it is not the case that" become $\neg$.
3. Watch for compound connecting phrases: "neither $P$ nor $Q$" is $\neg P \wedge \neg Q$, "not both $P$ and $Q$" is $\neg(P \wedge Q)$, and "$P$ but not $Q$" is $P \wedge \neg Q$.
4. Put in the brackets that match the grouping you hear in the sentence, and read your symbols back as English to see whether the meaning survived.

## Worked examples

<div class="example" markdown>

### Example 1: evaluating with given truth values

Let $P$ be "7 is prime", $Q$ be "9 is prime" and $R$ be "12 is divisible by 4". Find the truth value of (a) $\neg(P \wedge Q) \vee R$, (b) $(\neg P \vee Q) \wedge R$ and (c) $P \wedge (Q \vee \neg R)$.

Step 1: 7 is prime, so $P$ is T. Since $9 = 3 \cdot 3$, $Q$ is F. And $12 = 4 \cdot 3$, so $R$ is T.

For (a), Step 2 says the main connective is the $\vee$ in the middle. Step 3: the inside bracket first, $P \wedge Q$ is $\text{T} \wedge \text{F}$, which is F. Then $\neg(P \wedge Q)$ is T. Finally $\text{T} \vee R$ is T, because one true part is enough. So (a) is T.

For (b), the main connective is the $\wedge$. The bracket is $\neg P \vee Q$, which is $\text{F} \vee \text{F}$, so F. Then $\text{F} \wedge R$ is F, and (b) is F.

For (c), the main connective is the first $\wedge$. The bracket is $Q \vee \neg R$, which is $\text{F} \vee \text{F}$, so F. Then $P \wedge \text{F}$ is F, so (c) is F.

Step 5, check (a) in English: "It is not the case that both 7 and 9 are prime, or 12 is divisible by 4." Both halves of that sentence are true, so (a) is T.

</div>

<div class="example" markdown>

### Example 2: English to symbols

Translate (a) "You may pay by debit or by credit, but not both." (b) "The server is up, and neither the cache nor the load balancer is down."

For (a), Step 1: let $D$ be "you pay by debit" and $C$ be "you pay by credit". Step 2: the "or" is exclusive, since the sentence adds "but not both". So the statement is $D \oplus C$. It can also be written with the other connectives as $(D \vee C) \wedge \neg(D \wedge C)$: at least one, and not both. Check on the four rows: if $D$ and $C$ are both T, then $D \vee C$ is T but $\neg(D \wedge C)$ is F, so the whole is F, as the sentence demands.

For (b), Step 1: let $S$ be "the server is up", $K$ be "the cache is down" and $B$ be "the load balancer is down". Step 3: "neither $K$ nor $B$" is $\neg K \wedge \neg B$. So the statement is $S \wedge (\neg K \wedge \neg B)$, which can be written $S \wedge \neg K \wedge \neg B$ because a chain of $\wedge$ signs doesn't need brackets (it gives the same value in every grouping). Check: it is true only if $S$ is T and both $K$ and $B$ are F, which is the situation "everything is fine".

</div>

<div class="example" markdown>

### Example 3: edge case, "or" and the sign $\le$

Is $3 \le 3$ true? The symbol $\le$ is an abbreviation: $a \le b$ means "$a < b$ or $a = b$". With $a = b = 3$, "$3 < 3$" is F and "$3 = 3$" is T. An inclusive "or" needs only one true part, so $3 \le 3$ is T.

This is the most common place where inclusive "or" appears without being named. It also explains why "$x \ge 5$ or $x \le 5$" is true for every real $x$: at $x = 5$ both parts are true, and for every other $x$ exactly one is. The statement "$x \ge 5$ and $x \le 5$" is true only at $x = 5$.

Check with $x = 7$: "$7 \ge 5$" is T and "$7 \le 5$" is F, so the "or" statement is T and the "and" statement is F.

</div>

<div class="example" markdown>

### Example 4: precedence (finish it yourself)

Let $P$ be F, $Q$ be T and $R$ be F. Evaluate $\neg P \vee Q \wedge R$ using the precedence rules, and compare it with the statement you get by grouping the other way, $(\neg P \vee Q) \wedge R$.

Step 1 is done: $P = \text{F}$, $Q = \text{T}$, $R = \text{F}$. Step 2: by precedence, the $\wedge$ binds tighter, so the statement is $(\neg P) \vee (Q \wedge R)$ and the main connective is $\vee$. Now do Step 3 for both groupings.

<details class="solution" markdown>
<summary>Finish</summary>

Precedence grouping: $\neg P$ is T, and $Q \wedge R$ is $\text{T} \wedge \text{F}$, which is F. So $\text{T} \vee \text{F}$ is T.

The other grouping: $\neg P \vee Q$ is $\text{T} \vee \text{T}$, which is T, and then $\text{T} \wedge R$ is $\text{T} \wedge \text{F}$, which is F.

The two groupings give different values, so the brackets matter. Check by running the Python expression `not p or q and r` with `p = False, q = True, r = False`: it prints `True`, matching the precedence grouping.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: in math, "or" includes "both". "A number is a root if it is a zero of the numerator or a zero of the denominator" doesn't exclude a number that is both. When you mean exactly one, say so, or write $\oplus$.

</div>

<div class="warning" markdown>

Watch out for the negation of "and" and "or". The negation of "$x > 3$ and $x$ is even" is not "$x \le 3$ and $x$ is odd". Negating a pair of conditions turns "and" into "or" (next two lessons give the rule, called De Morgan's laws), and the correct negation is "$x \le 3$ or $x$ is odd". Test: $x = 2$ makes the original false (it is not above 3), so its negation must be true, and "$x \le 3$ or $x$ is odd" is true there, while "$x \le 3$ and $x$ is odd" is false.

</div>

<div class="warning" markdown>

Watch out: an open sentence is not a statement. "$x^2 > 4$" is neither true nor false until $x$ has a value or a quantifier. If you write "$x^2 > 4$ is true" in a proof, ask: for which $x$? A claim about "all $x$" or "some $x$" needs those words.

</div>

<div class="warning" markdown>

Watch out when translating "not both" and "both not". "Not both $P$ and $Q$" is $\neg(P \wedge Q)$, which is true when at least one fails. "Both not $P$ and not $Q$" is $\neg P \wedge \neg Q$, which is true only when both fail. They differ at the row where exactly one of $P$, $Q$ is true.

</div>

Another small trap is the dropped negation sign: the negation of "$x < 5$" is "$x \ge 5$". It is not "$x > 5$", which leaves out $x = 5$.

A statement with no variable can still be tricky to evaluate. "$P$ is T" doesn't mean the sentence is easy; "every even integer greater than 2 is a sum of two primes" has a truth value, and no one has proved which. Knowing the truth value and being able to prove it are different things. Proofs are the tool for the second.

## Tricks and shortcuts

Count the rows before you start: $n$ atomic statements give $2^n$ rows. A table for 4 statements already has 16 rows, so for big expressions use the structure instead.

Remember the two lopsided rows. A conjunction is true in only one row (all parts true), so it is false as soon as one part is false. A disjunction is false in only one row (all parts false), so it is true as soon as one part is true. Most evaluations finish in one glance using these two facts.

If you think of T as 1 and F as 0, then $P \wedge Q$ is the product $P \cdot Q$, $P \vee Q$ is the larger of the two, $\neg P$ is $1 - P$, and $P \oplus Q$ is the sum $P + Q$ with a result of 2 counted as 0, which is $(P + Q) \bmod 2$. The XOR case is why $\oplus$ shows up in bit operations: [bitwise operations and masks](../../06-cs-math/01-number-representation/05-bitwise-operations-and-masks.md) uses it on whole numbers, bit by bit.

## In code

Python's `and`, `or` and `not` are the connectives. Two details matter. First, `and` and `or` short-circuit: Python evaluates the left side, and evaluates the right side only if the answer isn't settled yet. That is why `len(items) > 0 and items[0] == 5` is safe. Second, `or` and `and` return one of their operands, not always `True` or `False`, which causes a classic bug.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import product

print("P Q and or xor")
for p, q in product([True, False], repeat=2):
    print(p, q, p and q, p or q, p != q)

def check(label, value):
    print("checking", label)
    return value

check("A", False) and check("B", True)   # prints only: checking A
check("A", True) or check("B", True)     # prints only: checking A

items = []
print(len(items) > 0 and items[0] == 5)  # False, and items[0] is never evaluated

x = 3
print(x == 1 or 2)       # 2, which counts as true in an if
print(x == 1 or x == 2)  # False
print(x in (1, 2))       # False

print(True ^ True, True ^ False)  # False True
```

The first loop prints the table of this lesson, with `p != q` as xor: two booleans differ exactly when one is true. The short-circuit lines print `checking A` once each, because in the first line `False and ...` is already false and in the second `True or ...` is already true. The `x == 1 or 2` line is read as `(x == 1) or 2`, and a nonzero number such as `2` counts as true, so `if x == 1 or 2:` is always taken. Write `x == 1 or x == 2`, or `x in (1, 2)`.

</details>

## FAQ

### Why is "or" inclusive in math?

Because it makes the rules simpler. With the inclusive meaning, "$P$ or $Q$" is false only in one row, and the rules for negation and for sets (a union contains everything in either set) come out clean. The exclusive meaning can be built from the inclusive one in a line ($(P \vee Q) \wedge \neg(P \wedge Q)$), but building the inclusive one from the exclusive one takes more work. English often gives the exclusive meaning from context, so when you translate, decide from the sentence, not from habit.

### Is "This sentence is false" a statement?

No. If it were true, it would say that it is false, and if it were false, then what it says would be true. It has no consistent truth value, so it is not a statement. Self-reference of this kind is why logicians are careful about what counts as a statement, and a version of it is behind the proof that no program can solve the halting problem (see decidability and the halting problem<!-- link: ../../06-cs-math/06-theory-of-computation/05-decidability-and-the-halting-problem.md -->).

### If "$x > 2$" is not a statement, how can a theorem about it be true?

A theorem like "if $x > 2$, then $x^2 > 4$" hides a quantifier: it means "for every real $x$, if $x > 2$ then $x^2 > 4$". The open sentence becomes a statement once the quantifier is there. [Quantifiers](04-quantifiers.md) explains how, and most theorems in the rest of this book have this shape.

### Why bother with symbols when English works?

English works until the sentence has three or four conditions. "I'll go if it's sunny and warm or it's the weekend" has two readings, and the symbols $(S \wedge W) \vee K$ against $S \wedge (W \vee K)$ show them. In a proof, each statement also has to be handled by rule, and rules are easier to apply to symbols.

## Practice

### Warm-up

1\. Decide whether each is a statement. If so, say whether it is true, false, or unknown. (a) $2^{10} = 1000$. (b) $n^2 + 1$ is prime. (c) What is $2^{10}$? (d) Every prime greater than 2 is odd. (e) There is an even prime.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) A statement, false, since $2^{10} = 1024$.
- (b) Not a statement: it has a free variable $n$, so it has no truth value yet.
- (c) A question, so not a statement.
- (d) A statement, true: an even number greater than 2 has the factor 2 and another factor, so it isn't prime.
- (e) A statement, true: 2 is an even prime.

Check (a) by computing: $2^{10} = 1024 \ne 1000$.

</details>

2\. Let $P$ be "$12 > 10$", $Q$ be "13 is even" and $R$ be "$3 \mid 12$" (3 divides 12). Find the truth value of (a) $P \wedge Q$, (b) $\neg Q \wedge R$, (c) $\neg(P \vee Q)$, (d) $Q \oplus R$.

<details class="solution" markdown>
<summary>Solution</summary>

First the atoms: $P$ is T, $Q$ is F (13 is odd), $R$ is T ($12 = 3 \cdot 4$).

- (a) $\text{T} \wedge \text{F}$ is F.
- (b) $\neg Q$ is T, and $\text{T} \wedge \text{T}$ is T.
- (c) $P \vee Q$ is T, so its negation is F.
- (d) Exactly one of $Q$, $R$ is true, so $Q \oplus R$ is T.

Check (c) another way: a negated "or" is true only if both parts are false, and $P$ is true, so (c) must be F.

</details>

3\. Translate into symbols, defining your letters. (a) "The list is sorted but not empty." (b) "Neither the first nor the second test passed." (c) "Either the user is logged in or the page redirects, but not both."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Let $S$ be "the list is sorted" and $E$ be "the list is empty". The statement is $S \wedge \neg E$.
- (b) Let $F$ be "the first test passed" and $G$ be "the second test passed". The statement is $\neg F \wedge \neg G$.
- (c) Let $L$ be "the user is logged in" and $R$ be "the page redirects". The statement is $L \oplus R$, or $(L \vee R) \wedge \neg(L \wedge R)$.

Check (b) by reading back: $\neg F \wedge \neg G$ is "the first did not pass and the second did not pass", which is the same as "neither passed". The version $\neg(F \wedge G)$ would be wrong, because it is true when only one of the tests failed.

</details>

### Standard

4\. Build the truth table of $(P \vee Q) \wedge \neg(P \wedge Q)$. Which connective from this lesson has the same column?

<details class="solution" markdown>
<summary>Solution</summary>

Add a column for each part, inside out.

| $P$ | $Q$ | $P \vee Q$ | $P \wedge Q$ | $\neg(P \wedge Q)$ | $(P \vee Q) \wedge \neg(P \wedge Q)$ |
|---|---|---|---|---|---|
| T | T | T | T | F | F |
| T | F | T | F | T | T |
| F | T | T | F | T | T |
| F | F | F | F | T | F |

The last column is F, T, T, F, which is the column of $P \oplus Q$. So the statement is the exclusive or, as Example 2(a) claimed.

Check: the statement should be true exactly when $P$ and $Q$ have different truth values, and rows 2 and 3 are the only rows like that.

</details>

5\. Put full brackets on $P \vee \neg Q \wedge R \vee S$ using the precedence rules. Then evaluate it when $P$ is F, $Q$ is T, $R$ is T and $S$ is F.

<details class="solution" markdown>
<summary>Solution</summary>

The $\neg$ applies to $Q$ only, and then $\wedge$ binds before $\vee$. So the statement is $P \vee \bigl((\neg Q) \wedge R\bigr) \vee S$. A chain of $\vee$ signs gives the same value however it is grouped, so no more brackets are needed.

Now evaluate. Since $Q$ is T, $\neg Q$ is F, so $(\neg Q) \wedge R$ is $\text{F} \wedge \text{T}$, which is F. Then $P \vee \text{F} \vee S$ is $\text{F} \vee \text{F} \vee \text{F}$, which is F.

Check in Python: `p, q, r, s = False, True, True, False` and `p or not q and r or s` prints `False`.

</details>

6\. Predict the output of each line, then run it to check. (a) `print(5 > 3 and 2 > 4)` (b) `print(5 > 3 or 2 > 4)` (c) `print(not 5 > 3 or 2 > 4)` (d) `print(0 or "hello")` (e) `print([] and 1)`

<details class="solution" markdown>
<summary>Solution</summary>

- (a) `False`: the second part is false.
- (b) `True`: the first part is true, and `or` stops there.
- (c) `False`: `not` applies to `5 > 3` only (comparison before `not`), giving `False`, and `2 > 4` is `False`, so `False or False` is `False`.
- (d) `hello`: `0` counts as false, so `or` returns its second operand.
- (e) `[]`: an empty list counts as false, so `and` returns it without looking at the right side.

Check (c) with brackets: `(not (5 > 3)) or (2 > 4)`. Lines (d) and (e) show that `and` and `or` return an operand, not a bare `True` or `False`.

</details>

### Challenge

7\. On an island, knights always tell the truth and knaves always lie. Person A says: "I am a knave or B is a knight." What are A and B?

<details class="solution" markdown>
<summary>Solution</summary>

We know the rule: a knight's statement is true, and a knave's statement is false. We want the type of A and the type of B. The plan is to try each type for A in turn.

Let $S$ be A's statement, "A is a knave or B is a knight". Suppose A is a knave. Then $S$ must be false. But "A is a knave" is true in this case, so the "or" is true, and $S$ is true. That contradicts the knave always lying, so A is not a knave. So A is a knight, and $S$ is true.

Now A is a knight, so "A is a knave" is false. For the "or" to be true, "B is a knight" must be true. So both A and B are knights.

Check: A and B are knights. A's statement is "F or T", which is true, as a knight's statement must be. The other combinations fail: A knight and B knave makes $S$ false, which a knight can't say, and A knave makes $S$ true, which a knave can't say.

</details>

8\. (Reviews [compound inequalities and interval notation](../../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md).) Write "$x$ is in $(-1, 3]$" as a statement built from two inequalities with a connective. Then write its negation using inequalities and a connective, and write the negation's solution set in interval notation.

<details class="solution" markdown>
<summary>Solution</summary>

The interval $(-1, 3]$ holds the numbers above $-1$ and at most 3, so the statement is $x > -1 \wedge x \le 3$.

For the negation, a pair of conditions fails when at least one of them fails. The negation of $x > -1$ is $x \le -1$, and the negation of $x \le 3$ is $x > 3$. So the negation is $x \le -1 \vee x > 3$, and its solution set is $(-\infty, -1] \cup (3, \infty)$.

Check with three test values. At $x = -1$ the original is false (since $-1 > -1$ is false) and the negation is true. At $x = 3$ the original is true and the negation is false. At $x = 3.5$ the original is false and the negation is true. In each case the two have opposite truth values, as a statement and its negation must.

</details>

## Where this shows up

- The next lesson, [conditionals and biconditionals](02-conditionals-and-biconditionals.md), adds "if ... then" to this list, and [truth tables and logical equivalence](03-truth-tables-and-logical-equivalence.md) shows how to tell when two compound statements say the same thing.
- Every `if`, `while` and filter in a program is a compound statement. [Boolean algebra and logic gates](../../06-cs-math/01-number-representation/06-boolean-algebra-and-logic-gates.md) turns $\wedge$, $\vee$, $\neg$ and $\oplus$ into circuits, and satisfiability, which asks whether a compound statement can be made true, is the starting point of P, NP and NP-completeness<!-- link: ../../06-cs-math/06-theory-of-computation/07-p-np-and-np-completeness.md -->.
- In economics and finance, conditions like "income above the threshold and the account is open" decide eligibility rules, and a carefully parsed "and" or "or" is the difference between two different tax rules.
