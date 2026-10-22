# Truth tables and logical equivalence

After this lesson you can build the truth table of a compound statement, classify it as a tautology, a contradiction or neither, decide whether two statements are logically equivalent (by a table or by a chain of known equivalences), and use De Morgan's laws and the conditional rewrite to simplify a condition in code.

Before this: [statements and connectives](01-statements-and-connectives.md) and [conditionals and biconditionals](02-conditionals-and-biconditionals.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Build the truth table of $\neg(P \vee Q)$ and of $\neg P \wedge \neg Q$. Do the two columns agree?
2. Is $(P \wedge Q) \Rightarrow P$ a tautology, a contradiction or neither? What about $P \Rightarrow \neg P$?
3. Rewrite the Python condition `not (a and b)` using `or`, with no `not` outside a bracket.

<details class="solution" markdown>
<summary>Answers</summary>

1. The columns are F, F, F, T for both statements (rows TT, TF, FT, FF), so they agree in every row. The first is false whenever $P \vee Q$ is true, which is every row except FF, and the second is true only when both $P$ and $Q$ are false, which is the row FF.
2. The statement $(P \wedge Q) \Rightarrow P$ is a tautology: when the hypothesis is true, $P$ is true, so the conclusion is true. The statement $P \Rightarrow \neg P$ is neither: it is false when $P$ is true and true when $P$ is false.
3. `(not a) or (not b)`. This is one of De Morgan's laws.

</details>

## The idea

A colleague writes `if not (user.is_admin and user.is_active):` and you want to read it aloud. You could say "it's not the case that the user is an active admin", which is correct. You could also say "the user is not an admin, or not active", which is also correct and perhaps easier. Are they really the same? If you reply "they sound the same", a test suite will eventually disagree with you. There needs to be a way to prove it.

A truth table is that way, and it is brute force. A compound statement made from $n$ atomic statements has $2^n$ ways its parts can be true or false, and the table lists all of them. If two compound statements have the same truth value in every row, they say the same thing in every possible situation, and we call them logically equivalent. That is a fact about the shape of the statements. It doesn't depend on what $P$ and $Q$ mean.

Then a second, faster tool appears. Once a few equivalences have been proved by tables, they act like the rules of algebra: a long statement can be rewritten step by step into a short one, with each step justified by a rule, in the same way $3(x + 4) - 3x$ is simplified to 12. This is the main skill of the lesson, and it is the logic behind every simplification of a condition in a program.

## Definitions

### Tautologies and contradictions

A **tautology** is a compound statement that is true in every row of its truth table, whatever the truth values of its parts. A **contradiction** is a compound statement that is false in every row. A statement that is true in some rows and false in others is called **contingent**.

In plain words, a tautology is true by its shape alone: "it rains or it doesn't rain", $P \vee \neg P$, says nothing about the weather. A contradiction is false by its shape: $P \wedge \neg P$. Both are useless as information and useful as tools, because a proof by contradiction works by reaching a contradiction.

### Logical equivalence

Two compound statements $A$ and $B$ are **logically equivalent**, written $A \equiv B$, when they have the same truth value in every row of the truth table (for the same atomic statements).

In plain words, they are the same condition written two ways: whenever one is true so is the other, and whenever one is false so is the other. Be careful with two symbols that look alike. The symbol $\Leftrightarrow$ is a connective: $A \Leftrightarrow B$ is a statement, which might be true or false. The symbol $\equiv$ is a claim about two statements: "$A \equiv B$" says that $A \Leftrightarrow B$ is a tautology. For two atomic statements $P$ and $Q$, the statement $P \Leftrightarrow Q$ is true in the rows TT and FF, but the claim $P \equiv Q$ is false, because the rows TF and FT separate them. Equivalence has to hold in every row, not in the one you happen to be looking at.

### The standard equivalences

These are the rules of the algebra of statements. Each one can be checked with a truth table, and the lesson proves the most important ones below. In the table, $\mathbf{T}$ stands for a statement that is always true and $\mathbf{F}$ for one that is always false.

| Name | Equivalence |
|---|---|
| Double negation | $\neg\neg P \equiv P$ |
| Commutative laws | $P \wedge Q \equiv Q \wedge P$, $\quad P \vee Q \equiv Q \vee P$ |
| Associative laws | $(P \wedge Q) \wedge R \equiv P \wedge (Q \wedge R)$, $\quad (P \vee Q) \vee R \equiv P \vee (Q \vee R)$ |
| Distributive laws | $P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$, $\quad P \vee (Q \wedge R) \equiv (P \vee Q) \wedge (P \vee R)$ |
| De Morgan's laws | $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$, $\quad \neg(P \vee Q) \equiv \neg P \wedge \neg Q$ |
| Idempotent laws | $P \wedge P \equiv P$, $\quad P \vee P \equiv P$ |
| Identity laws | $P \wedge \mathbf{T} \equiv P$, $\quad P \vee \mathbf{F} \equiv P$ |
| Domination laws | $P \vee \mathbf{T} \equiv \mathbf{T}$, $\quad P \wedge \mathbf{F} \equiv \mathbf{F}$ |
| Complement laws | $P \vee \neg P \equiv \mathbf{T}$, $\quad P \wedge \neg P \equiv \mathbf{F}$ |
| Absorption laws | $P \vee (P \wedge Q) \equiv P$, $\quad P \wedge (P \vee Q) \equiv P$ |
| Conditional as "or" | $P \Rightarrow Q \equiv \neg P \vee Q$ |
| Contrapositive | $P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$ |
| Negation of a conditional | $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$ |
| Biconditional | $P \Leftrightarrow Q \equiv (P \Rightarrow Q) \wedge (Q \Rightarrow P)$ |
| Exportation | $(P \wedge Q) \Rightarrow R \equiv P \Rightarrow (Q \Rightarrow R)$ |

Look at the distributive laws: there are two, and they are symmetric. Ordinary algebra has only one distributive law (multiplication over addition), because $a + (b \cdot c) = (a + b)(a + c)$ is false for numbers. For statements, $\wedge$ distributes over $\vee$, and $\vee$ distributes over $\wedge$.

The laws also show that some connectives are redundant. Using $P \Rightarrow Q \equiv \neg P \vee Q$ and De Morgan, $\neg$, $\wedge$ and $\vee$ are enough to write all the others, and $\neg$ with $\wedge$ alone is also enough (Practice problem 7 asks for the details).

## How to do it

### Proving an equivalence with a truth table

1. List the atomic statements. If there are $n$, you need $2^n$ rows. Write the rows in a fixed order so none is skipped: for two statements TT, TF, FT, FF, and for three the same pattern with the last column alternating fastest (TTT, TTF, TFT, TFF, FTT, FTF, FFT, FFF).
2. Give every subformula its own column, working from the innermost bracket outward, so each column uses only columns already filled in.
3. Compare the two final columns. If they match in every row, the statements are equivalent. If they differ in even one row, they are not.
4. To show that two statements are not equivalent, you don't need the whole table. Find one row where they differ, and say which row.

### Proving an equivalence by a chain

1. Start with one side. Write the statement.
2. Apply one law at a time, and write the name of the law beside each new line. Change only one part of the statement per step.
3. Aim for the other side. The statement of the goal tells you which direction to go: if the goal has fewer connectives, look for De Morgan, absorption, or the complement and identity laws.
4. Check the result with one row of a truth table, or by evaluating both sides for some values.

### Three theorems, with proofs

*Theorem 1 (De Morgan's laws).* For all statements $P$ and $Q$, $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$ and $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$.

What we know: the truth tables of $\neg$, $\wedge$ and $\vee$. What we want: the columns of the two sides agree in all four rows. The plan is to build one table for the first law, and then derive the second from the first.

*Proof.* A table for the first law:

| $P$ | $Q$ | $P \wedge Q$ | $\neg(P \wedge Q)$ | $\neg P$ | $\neg Q$ | $\neg P \vee \neg Q$ |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

The columns for $\neg(P \wedge Q)$ and $\neg P \vee \neg Q$ both read F, T, T, T. For the second law, apply the first law to the statements $\neg P$ and $\neg Q$: $\neg(\neg P \wedge \neg Q) \equiv \neg\neg P \vee \neg\neg Q \equiv P \vee Q$ by double negation. Negating both sides of this equivalence, and using double negation on the left, gives $\neg P \wedge \neg Q \equiv \neg(P \vee Q)$. $\blacksquare$

Look back: the words say the same thing. "Not both" is true when at least one fails, and "neither" is true when both fail. A "not" moving through a bracket swaps $\wedge$ with $\vee$, and it also negates each part. Forgetting one of those two things is the most common slip with these laws.

*Theorem 2 (the conditional as "or").* For all statements $P$ and $Q$, $P \Rightarrow Q \equiv \neg P \vee Q$.

What we want: the two columns agree in every row. The plan is again a table.

*Proof.*

| $P$ | $Q$ | $P \Rightarrow Q$ | $\neg P$ | $\neg P \vee Q$ |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | F | F | F |
| F | T | T | T | T |
| F | F | T | T | T |

The columns for $P \Rightarrow Q$ and $\neg P \vee Q$ are both T, F, T, T. $\blacksquare$

Look back: in words, "if $P$, then $Q$" says that either $P$ fails or $Q$ holds. This is the form to use when you need to compute with a conditional, and it explains the vacuous cases: when $P$ fails, the "or" is already true.

*Theorem 3.* For all statements $P$ and $Q$: (a) $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$, and (b) $P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$.

What we know: Theorems 1 and 2 and double negation. What we want: both claims, by chains. The plan is to turn each conditional into an "or" and apply a law.

*Proof of (a).* Each line follows from the one before by the law on the right.

$$
\begin{aligned}
\neg(P \Rightarrow Q) &\equiv \neg(\neg P \vee Q) && \text{Theorem 2} \\
&\equiv \neg\neg P \wedge \neg Q && \text{De Morgan} \\
&\equiv P \wedge \neg Q && \text{double negation}
\end{aligned}
$$

*Proof of (b).*

$$
\begin{aligned}
\neg Q \Rightarrow \neg P &\equiv \neg\neg Q \vee \neg P && \text{Theorem 2, applied to } \neg Q \text{ and } \neg P \\
&\equiv Q \vee \neg P && \text{double negation} \\
&\equiv \neg P \vee Q && \text{commutative law} \\
&\equiv P \Rightarrow Q && \text{Theorem 2} \qquad \blacksquare
\end{aligned}
$$

Look back: part (a) says a conditional fails exactly when the hypothesis holds and the conclusion fails, which agrees with the one false row in its truth table. Part (b) proves what the earlier lesson showed by table, and shows why the inverse is *not* equivalent to the original: the inverse $\neg P \Rightarrow \neg Q$ turns into $P \vee \neg Q$, which is a different statement.

### Satisfiability, briefly

A compound statement is **satisfiable** if at least one row of its truth table makes it true. Tautologies are satisfiable. Contradictions are not. A statement $A$ is a tautology exactly when $\neg A$ is not satisfiable, because "true in every row" is "the negation is true in no row".

To decide satisfiability, the truth table method tries every row. With 3 statements that is 8 rows. With 20 it is $2^{20} = 1{,}048{,}576$ rows, and with 30 it is $2^{30} = 1{,}073{,}741{,}824$. The question "is this statement satisfiable?", called SAT, is the first problem proved to be NP-complete: no one knows a method that is fast in the worst case for every statement, although real-world solvers handle enormous instances. Chapters of the CS math folder return to it in P, NP and NP-completeness<!-- link: ../../06-cs-math/06-theory-of-computation/07-p-np-and-np-completeness.md -->.

## Worked examples

<div class="example" markdown>

### Example 1: a three-variable table

Show that $P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$.

Step 1: three atomic statements give $2^3 = 8$ rows, in the order given. Step 2: columns for $Q \vee R$, then for $P \wedge (Q \vee R)$, then for $P \wedge Q$, $P \wedge R$ and their "or".

| $P$ | $Q$ | $R$ | $Q \vee R$ | $P \wedge (Q \vee R)$ | $P \wedge Q$ | $P \wedge R$ | $(P \wedge Q) \vee (P \wedge R)$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T |
| T | T | F | T | T | T | F | T |
| T | F | T | T | T | F | T | T |
| T | F | F | F | F | F | F | F |
| F | T | T | T | F | F | F | F |
| F | T | F | T | F | F | F | F |
| F | F | T | T | F | F | F | F |
| F | F | F | F | F | F | F | F |

Step 3: the fifth column and the last column are both T, T, T, F, F, F, F, F, so the statements are equivalent.

Check with a story: "I'll go if it's the weekend, and it's either sunny or warm" has the same meaning as "I'll go if it's the weekend and sunny, or the weekend and warm". Both are true only in the first three rows, where $P$ is true and at least one of $Q$, $R$ is true.

</div>

<div class="example" markdown>

### Example 2: simplifying with a chain

Show that $\neg(\neg P \vee Q) \vee (P \wedge Q) \equiv P$.

The right side is shorter, so look for laws that remove connectives. Each line carries its reason.

$$
\begin{aligned}
\neg(\neg P \vee Q) \vee (P \wedge Q) &\equiv (\neg\neg P \wedge \neg Q) \vee (P \wedge Q) && \text{De Morgan} \\
&\equiv (P \wedge \neg Q) \vee (P \wedge Q) && \text{double negation} \\
&\equiv P \wedge (\neg Q \vee Q) && \text{distributive law, read right to left} \\
&\equiv P \wedge (Q \vee \neg Q) && \text{commutative law} \\
&\equiv P \wedge \mathbf{T} && \text{complement law} \\
&\equiv P && \text{identity law}
\end{aligned}
$$

Check with one row. For $P$ true and $Q$ false, the left side is $\neg(\text{F} \vee \text{F}) \vee (\text{T} \wedge \text{F})$, which is $\text{T} \vee \text{F}$, so T, and the right side $P$ is T. For $P$ false and $Q$ true, the left side is $\neg(\text{T} \vee \text{T}) \vee (\text{F} \wedge \text{T})$, which is $\text{F} \vee \text{F}$, so F, and $P$ is F.

</div>

<div class="example" markdown>

### Example 3: statements that are not equivalent

Are $(P \Rightarrow Q) \Rightarrow R$ and $P \Rightarrow (Q \Rightarrow R)$ equivalent?

Following Step 4 of the table method, we look for one row where they differ, instead of building all eight. A good place to look is where a conditional's hypothesis is false. Try $P$ false, $Q$ true, $R$ false.

- Left side: $P \Rightarrow Q$ is $\text{F} \Rightarrow \text{T}$, which is T, so the left side is $\text{T} \Rightarrow \text{F}$, which is F.
- Right side: $Q \Rightarrow R$ is $\text{T} \Rightarrow \text{F}$, which is F, and $P \Rightarrow \text{F}$ with $P$ false is T.

The left is F and the right is T, so the statements are not equivalent. Brackets matter for $\Rightarrow$: it isn't associative, and an expression like $P \Rightarrow Q \Rightarrow R$ needs brackets. Exportation is a different statement, since it has $P \wedge Q$ in front of the first arrow: $(P \wedge Q) \Rightarrow R \equiv P \Rightarrow (Q \Rightarrow R)$.

Check by a story: let $P$ be "I study", $Q$ be "I pass" and $R$ be "I'm happy". Take someone who didn't study, passed anyway and is not happy. The right side, "if I study, then (if I pass, I'm happy)", holds vacuously, because they didn't study. The left side, "if (studying leads to passing), then I'm happy", fails: its hypothesis "if I study, I pass" is true for them, also vacuously, and its conclusion "I'm happy" is false.

</div>

<div class="example" markdown>

### Example 4: simplifying a condition in code (finish it yourself)

A function runs `if not (x > 0 and not (y > 0)):`. Rewrite the condition without any `not` outside a comparison. Let $A$ be "$x > 0$" and $B$ be "$y > 0$". The condition is $\neg(A \wedge \neg B)$.

Step 1: apply De Morgan's law to the outer negation: $\neg A \vee \neg\neg B$. Now finish: simplify $\neg\neg B$, turn $\neg A$ and $B$ back into comparisons, and test your answer on $(x, y) = (1, -1)$ and $(x, y) = (-1, -1)$.

<details class="solution" markdown>
<summary>Finish</summary>

By double negation, $\neg A \vee \neg\neg B \equiv \neg A \vee B$. The negation of "$x > 0$" is "$x \le 0$", so the condition is `x <= 0 or y > 0`.

Check: at $(1, -1)$ the original is `not (True and not False)` = `not (True and True)` = `False`, and the new condition is `False or False` = `False`. At $(-1, -1)$ the original is `not (False and ...)` = `True`, and the new condition is `True or False` = `True`. The two agree on both. This condition is also the conditional "if $x > 0$ then $y > 0$", by Theorem 2.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out when moving a negation through a bracket. The statement $\neg(P \wedge Q)$ is not $\neg P \wedge \neg Q$. A "not" that enters a bracket must flip the connective *and* negate each part. Test with $P$ true and $Q$ false: $\neg(P \wedge Q)$ is T, but $\neg P \wedge \neg Q$ is F.

</div>

<div class="warning" markdown>

Watch out: a conditional is not equivalent to its converse or inverse, and it is not commutative. The statements $P \Rightarrow Q$ and $Q \Rightarrow P$ differ in the rows TF and FT. A truth table of both is how to settle an argument about it.

</div>

<div class="warning" markdown>

Watch out for skipping rows. A table with 3 variables has 8 rows, and a table with 7 rows can show equivalence by accident. Write the rows in the fixed order (last column alternating fastest) and count them before you compare the final columns.

</div>

<div class="warning" markdown>

Watch out for treating $\equiv$ as the same thing as $=$ or $\Leftrightarrow$. You may replace a part of a statement with an equivalent part (a substitution inside a bracket), but you may not reason from "$A$ and $B$ agree in this row" to "$A \equiv B$". Equivalence has to hold in every row.

</div>

A table works however many connectives there are, but each new variable doubles its size, so for a statement with many variables, a chain or a test of a few rows is better. Another subtle point: the laws hold when each of $P$, $Q$ and $R$ is replaced by a statement of your choice. De Morgan's law holds with $P$ replaced by "$x > 3$" and $Q$ replaced by "$x$ is even", and also with $P$ replaced by the compound statement $(R \vee S)$. A law is a pattern, and you may substitute a whole bracketed statement for each letter.

## Tricks and shortcuts

To test whether a statement is a tautology without a table, try to falsify it. To show $(P \wedge (P \Rightarrow Q)) \Rightarrow Q$ is a tautology, suppose it is false in some row. Then the hypothesis $P \wedge (P \Rightarrow Q)$ is true and $Q$ is false. The hypothesis being true makes $P$ true, and then $P \Rightarrow Q$ being true with $P$ true makes $Q$ true. That contradicts $Q$ being false, so the statement can never be false. (This tautology is *modus ponens*, the rule behind nearly every proof: from "$P$" and "if $P$, then $Q$", conclude "$Q$".)

To disprove an equivalence, search for a row of the kind that tends to break things: one where a hypothesis is false, or where one part is true and the other false. To prove one, use whichever method has less work: a table for two or three variables, a chain for more.

A compact memory aid for De Morgan: "the negation of 'and' is 'or', the negation of 'or' is 'and', and each part is negated". Read $\neg(x > 0 \wedge y > 0)$ aloud as "not both positive", which means "at least one is not positive", so $x \le 0 \vee y \le 0$.

## In code

A truth table in code is a loop over `itertools.product`. Writing the check as a function lets you test an equivalence on all rows, and the same idea checks satisfiability and tautology.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import product

def rows(n):
    return list(product([True, False], repeat=n))

def implies(p, q):
    return (not p) or q

def equivalent(f, g, n):
    return all(f(*r) == g(*r) for r in rows(n))

def tautology(f, n):
    return all(f(*r) for r in rows(n))

def satisfiable(f, n):
    return any(f(*r) for r in rows(n))

# De Morgan, and the conditional as "or"
print(equivalent(lambda p, q: not (p and q), lambda p, q: (not p) or (not q), 2))   # True
print(equivalent(lambda p, q: implies(p, q), lambda p, q: (not p) or q, 2))        # True

# the conditional is not associative
f = lambda p, q, r: implies(implies(p, q), r)
g = lambda p, q, r: implies(p, implies(q, r))
print(equivalent(f, g, 3))                                  # False
print([r for r in rows(3) if f(*r) != g(*r)])               # [(False, True, False), (False, False, False)]

# the simplification from Example 4
orig = lambda x, y: not (x > 0 and not (y > 0))
new = lambda x, y: x <= 0 or y > 0
print(all(orig(x, y) == new(x, y) for x in range(-3, 4) for y in range(-3, 4)))    # True

# modus ponens is a tautology; P and (not P) is not satisfiable
print(tautology(lambda p, q: implies(p and implies(p, q), q), 2))     # True
print(satisfiable(lambda p: p and not p, 1))                          # False
print(next(r for r in rows(3) if (r[0] or r[1]) and (not r[0] or r[2]) and (not r[1] or not r[2])))
# (True, False, True): the first assignment that satisfies all three clauses
```

The equivalence checker is the table method with the comparison automated. The list printed after the `False` gives the rows where the two conditionals differ. Both have $P$ false and $R$ false, which includes the row used in Example 3. Checking the simplified condition on a grid of integers is a test, not a proof; the proof was the chain of laws. The last line is brute-force satisfiability: it tries the 8 rows in order and returns the first that works. For a statement with 30 variables the same loop would need over a billion rows.

</details>

## FAQ

### Why not use truth tables for everything?

They are reliable and mechanical, and they double in size with each new variable: 10 variables give 1,024 rows. They also only work for statements built from connectives. Statements with "for all" and "there exists" (the next lesson) have no finite table, so you need rules and chains there. Truth tables are the foundation, and the chain method is the working tool.

### Is $\equiv$ the same as an equals sign?

It plays the same role, with a different object. An equals sign says two numbers are the same number. The symbol $\equiv$ says two statements have the same truth value in every row. Both allow substitution: you can replace a statement by an equivalent one inside a larger statement, just as you can replace a number by an equal one inside a larger expression.

### Why does De Morgan's law hold? It still feels like a trick.

Think of "not both" and "neither". "It is not true that I did both the reading and the exercises" means that at least one of them was not done: either I skipped the reading or I skipped the exercises. "It is not true that I did the reading or the exercises" means that I did neither. A negation turns "all must hold" into "at least one fails", and turns "at least one holds" into "all fail". The table just records that.

### How can $P \Rightarrow Q$ be the same as "not $P$ or $Q$" when they sound so different?

They sound different because everyday "if" carries a suggestion of connection. The table contains no suggestion, only the truth values, and they match row by row. In practice the "or" form is useful because it has no arrow: you can apply De Morgan to it, distribute over it, and use it in code.

## Practice

### Warm-up

1\. Classify each as a tautology, a contradiction or neither. (a) $P \vee \neg P$ (b) $P \wedge \neg P$ (c) $P \Rightarrow P$ (d) $(P \wedge Q) \Rightarrow P$ (e) $P \Rightarrow (P \wedge Q)$

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Tautology: one of $P$, $\neg P$ is true in each row.
- (b) Contradiction: $P$ and $\neg P$ are never both true.
- (c) Tautology: when $P$ is true the conclusion is true, and when $P$ is false the conditional is vacuously true.
- (d) Tautology: if $P \wedge Q$ is true, then $P$ is true.
- (e) Neither. It is false for $P$ true and $Q$ false, since then $P \wedge Q$ is false. It is true when $P$ is false.

Check (e) with the row TF: $P \Rightarrow (P \wedge Q)$ is $\text{T} \Rightarrow \text{F}$, which is F, and the row TT gives T, so it isn't a tautology or a contradiction.

</details>

2\. Use De Morgan's laws and double negation to rewrite each without a negation outside a bracket. (a) $\neg(\neg P \wedge Q)$ (b) $\neg(P \vee \neg Q)$ (c) $\neg(\neg P \vee \neg Q)$

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $\neg\neg P \vee \neg Q \equiv P \vee \neg Q$.
- (b) $\neg P \wedge \neg\neg Q \equiv \neg P \wedge Q$.
- (c) $\neg\neg P \wedge \neg\neg Q \equiv P \wedge Q$.

Check (a) at $P$ false, $Q$ true: the original is $\neg(\text{T} \wedge \text{T})$, which is F, and $P \vee \neg Q$ is $\text{F} \vee \text{F}$, which is F. At $P$ true, $Q$ true: the original is $\neg(\text{F} \wedge \text{T})$, which is T, and $P \vee \neg Q$ is T.

</details>

3\. For each pair, say whether the statements are equivalent. If not, give a row that separates them. (a) $P \Rightarrow Q$ and $Q \Rightarrow P$. (b) $P \Rightarrow Q$ and $\neg Q \Rightarrow \neg P$. (c) $\neg(P \vee Q)$ and $\neg P \wedge \neg Q$. (d) $\neg(P \wedge Q)$ and $\neg P \wedge \neg Q$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Not equivalent. At $P$ true and $Q$ false, the first is F and the second is T.
- (b) Equivalent (Theorem 3(b)).
- (c) Equivalent (De Morgan).
- (d) Not equivalent. At $P$ true and $Q$ false, $\neg(P \wedge Q)$ is T and $\neg P \wedge \neg Q$ is $\text{F} \wedge \text{T}$, which is F.

Check (a) by words: "if it rains, the street is wet" is not the same as "if the street is wet, it rained".

</details>

### Standard

4\. Prove the absorption law $P \vee (P \wedge Q) \equiv P$ with a truth table, and then explain it in one sentence.

<details class="solution" markdown>
<summary>Solution</summary>

| $P$ | $Q$ | $P \wedge Q$ | $P \vee (P \wedge Q)$ |
|---|---|---|---|
| T | T | T | T |
| T | F | F | T |
| F | T | F | F |
| F | F | F | F |

The last column is T, T, F, F, which is the column of $P$. So the two are equivalent.

In one sentence: if $P$ is true the "or" is true, and if $P$ is false then $P \wedge Q$ is false too, so the "or" is false; the extra part $P \wedge Q$ can never change the answer.

Check with numbers: let $P$ be "$x > 5$" and $Q$ be "$x$ is even". "$x > 5$, or ($x > 5$ and $x$ is even)" is true exactly when $x > 5$.

</details>

5\. Use a chain of equivalences to show that $(P \wedge Q) \Rightarrow R \equiv P \Rightarrow (Q \Rightarrow R)$ (exportation).

<details class="solution" markdown>
<summary>Solution</summary>

What we want: to turn the left side into the right side. The plan is to remove the arrows with Theorem 2, rearrange with De Morgan and the associative law, and put the arrows back.

$$
\begin{aligned}
(P \wedge Q) \Rightarrow R &\equiv \neg(P \wedge Q) \vee R && \text{Theorem 2} \\
&\equiv (\neg P \vee \neg Q) \vee R && \text{De Morgan} \\
&\equiv \neg P \vee (\neg Q \vee R) && \text{associative law} \\
&\equiv \neg P \vee (Q \Rightarrow R) && \text{Theorem 2, applied to } Q \Rightarrow R \\
&\equiv P \Rightarrow (Q \Rightarrow R) && \text{Theorem 2}
\end{aligned}
$$

Check at $P$ true, $Q$ true, $R$ false, the one row where the left side is false: $(\text{T} \wedge \text{T}) \Rightarrow \text{F}$ is F, and $\text{T} \Rightarrow (\text{T} \Rightarrow \text{F})$ is $\text{T} \Rightarrow \text{F}$, which is F. In code this is currying: a function of two arguments is a function that returns a function.

</details>

6\. Simplify the condition `not (x < 0 or y < 0) and not (x == 0)`, for real numbers `x` and `y`, to one with no `not`. Check it on a few pairs.

<details class="solution" markdown>
<summary>Solution</summary>

By De Morgan, $\neg(x < 0 \vee y < 0) \equiv \neg(x < 0) \wedge \neg(y < 0)$, which is $x \ge 0 \wedge y \ge 0$. The second part is $\neg(x = 0)$, which is $x \ne 0$. Together: $x \ge 0 \wedge y \ge 0 \wedge x \ne 0$.

For real $x$, "$x \ge 0$ and $x \ne 0$" means $x > 0$. So the condition is `x > 0 and y >= 0`.

Check: $(1, 0)$ gives `not (False or False) and not False` = `True and True` = `True`, and `1 > 0 and 0 >= 0` is `True`. $(0, 1)$ gives `not (False or False) and not True` = `False`, and `0 > 0 and ...` is `False`. $(2, -1)$ gives `not (False or True) and ...` = `False`, and `-1 >= 0` is `False`.

</details>

### Challenge

7\. Let $P \uparrow Q$ ("nand") mean $\neg(P \wedge Q)$. Show that $\neg P \equiv P \uparrow P$ and $P \wedge Q \equiv (P \uparrow Q) \uparrow (P \uparrow Q)$, and then write $P \vee Q$ using only $\uparrow$. (This is why a circuit built only from NAND gates can compute every condition.)

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the definition $P \uparrow Q \equiv \neg(P \wedge Q)$, and the laws above. The plan is to substitute into the definition and simplify.

First, $P \uparrow P \equiv \neg(P \wedge P) \equiv \neg P$, using the idempotent law $P \wedge P \equiv P$.

Second, $(P \uparrow Q) \uparrow (P \uparrow Q)$ is $A \uparrow A$ with $A = P \uparrow Q$, and by the first part $A \uparrow A \equiv \neg A$. So it is $\neg(P \uparrow Q) \equiv \neg\neg(P \wedge Q) \equiv P \wedge Q$.

Third, by De Morgan, $P \vee Q \equiv \neg(\neg P \wedge \neg Q) \equiv \neg P \uparrow \neg Q$. Replacing each $\neg$ by the first part gives $P \vee Q \equiv (P \uparrow P) \uparrow (Q \uparrow Q)$.

Check with a table for $(P \uparrow P) \uparrow (Q \uparrow Q)$: at $P$ true and $Q$ false, $P \uparrow P$ is F and $Q \uparrow Q$ is T, so $\text{F} \uparrow \text{T} = \neg(\text{F} \wedge \text{T})$ is T, and $P \vee Q$ is T. At both false, $P \uparrow P$ and $Q \uparrow Q$ are both T, so the result is $\neg(\text{T} \wedge \text{T})$, which is F, and $P \vee Q$ is F. The other two rows work in the same way.

</details>

8\. (Reviews [conditionals and biconditionals](02-conditionals-and-biconditionals.md).) Show by a chain of equivalences that the converse $Q \Rightarrow P$ and the inverse $\neg P \Rightarrow \neg Q$ of a conditional are equivalent to each other.

<details class="solution" markdown>
<summary>Solution</summary>

What we want: to turn $\neg P \Rightarrow \neg Q$ into $Q \Rightarrow P$. The plan is to write both as "or" statements.

$$
\begin{aligned}
\neg P \Rightarrow \neg Q &\equiv \neg\neg P \vee \neg Q && \text{Theorem 2} \\
&\equiv P \vee \neg Q && \text{double negation} \\
&\equiv \neg Q \vee P && \text{commutative law} \\
&\equiv Q \Rightarrow P && \text{Theorem 2, with } Q \text{ in the place of } P
\end{aligned}
$$

Check with the row $P$ true, $Q$ false: the inverse is $\text{F} \Rightarrow \text{T}$, which is T, and the converse is $\text{F} \Rightarrow \text{T}$, which is T. With $P$ false and $Q$ true: the inverse is $\text{T} \Rightarrow \text{F}$, which is F, and the converse is $\text{T} \Rightarrow \text{F}$, which is F. The earlier lesson's table had the same two columns equal.

</details>

## Where this shows up

- The rest of this chapter is built on these rules: [quantifiers](04-quantifiers.md) and [negation and translating English](05-negation-and-translating-english.md) extend De Morgan's laws to "for all" and "there exists", and [sets and set operations](06-sets-and-set-operations.md) has identical laws for $\cup$, $\cap$ and complement.
- [Contrapositive proof](../03-core-proof-methods/05-contrapositive-proof.md) and [proof by contradiction](../03-core-proof-methods/06-proof-by-contradiction.md) rest on Theorem 3(b) and on the idea that a statement and its negation can't both be true. Discrete math courses start with exactly these equivalences.
- In computing, compilers and linters simplify conditions with these laws; [Boolean algebra and logic gates](../../06-cs-math/01-number-representation/06-boolean-algebra-and-logic-gates.md) turns them into circuit simplification, and SAT solvers, which check satisfiability on formulas with millions of variables, are used to verify hardware and software.
