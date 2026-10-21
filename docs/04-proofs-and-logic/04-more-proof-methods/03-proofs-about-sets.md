# Proofs about sets

After this lesson you can prove that one set is a subset of another by choosing an arbitrary element, prove that two sets are equal by two inclusions or by a chain of equivalences, prove set identities such as the distributive law and De Morgan's laws, and disprove a false identity with small sets.

Before this: [sets and set operations](../02-logic-and-sets/06-sets-and-set-operations.md), [truth tables and logical equivalence](../02-logic-and-sets/03-truth-tables-and-logical-equivalence.md) and [if and only if proofs](01-if-and-only-if-proofs.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Let $A = \{1, 2, 3, 4\}$, $B = \{3, 4, 5\}$ and $C = \{4, 5, 6\}$. Compute $A \cap (B \cup C)$ and $(A \cap B) \cup (A \cap C)$.
2. Which are true? (a) $\emptyset \subseteq \{1\}$. (b) $\emptyset \in \{1\}$. (c) $\{1\} \in \{\{1\}\}$.
3. What is the first line, and what is the last line, of a proof that $A \subseteq B$?

<details class="solution" markdown>
<summary>Answers</summary>

1. $B \cup C = \{3, 4, 5, 6\}$, so $A \cap (B \cup C) = \{3, 4\}$. Also $A \cap B = \{3, 4\}$ and $A \cap C = \{4\}$, so $(A \cap B) \cup (A \cap C) = \{3, 4\}$. The two sets are equal.
2. (a) True: the empty set is a subset of every set. (b) False: the only element of $\{1\}$ is the number 1. (c) True: the only element of $\{\{1\}\}$ is the set $\{1\}$.
3. First line: "Let $x \in A$." Last line: "So $x \in B$." Between them, a chain of justified steps.

</details>

## The idea

A set is determined by its elements and nothing else: two sets are the same exactly when they have the same members. That one fact turns every statement about sets into a statement about elements. To say that $A \cap B$ is contained in $A$, you say that anything that lies in both $A$ and $B$ lies in $A$. The union, the intersection and the complement each come with a membership test, a sentence that says when an element belongs, and a set proof is a chain of those sentences.

The comparison with code is direct. In Python, `x in A & B` is the same as `x in A and x in B`, and `x in A | B` is `x in A or x in B`. Proving a set identity is the same as proving that two Boolean expressions agree for every `x`. That is the link to logic in this lesson: each set identity you prove is a propositional equivalence from the truth-table lesson, in disguise.

Venn diagrams are good for guessing which identities are true, and for seeing the pattern behind a proof. They are not proofs, for the reason in the first proof lesson: a drawing shows one arrangement of the sets, usually with all regions nonempty, and it can't show that the claim holds when two sets are equal or when one is empty. The proof method here handles every arrangement at once, because it never draws the sets.

## Definitions

Every set in this lesson is a subset of a fixed universal set $U$, and the elements are whatever $U$ contains. The membership tests are the definitions of the operations. For sets $A$ and $B$ and an element $x$:

| Set | The test for membership |
|---|---|
| $A \cap B$ | $x \in A \cap B$ if and only if $x \in A$ and $x \in B$ |
| $A \cup B$ | $x \in A \cup B$ if and only if $x \in A$ or $x \in B$ (or both) |
| $A \setminus B$ | $x \in A \setminus B$ if and only if $x \in A$ and $x \notin B$ |
| $A^c$ | $x \in A^c$ if and only if $x \in U$ and $x \notin A$ |
| $\emptyset$ | $x \in \emptyset$ is false for every $x$ |

These are definitions, so each "if and only if" can be used in both directions, as in [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#if-in-a-definition-means-if-and-only-if).

A set $A$ is a **subset** of $B$, written $A \subseteq B$, when every element of $A$ is an element of $B$: for every $x$, if $x \in A$ then $x \in B$. Two sets are **equal**, $A = B$, when they have the same elements, which is the same as $A \subseteq B$ and $B \subseteq A$. In plain words, $A \subseteq B$ says that $B$ has room for all of $A$, and $A = B$ says that each has room for all of the other.

The **empty set** $\emptyset$ has no elements. Since there is no $x$ in $\emptyset$, the claim "for every $x \in \emptyset$, $x \in B$" has nothing to check, and it is true for every set $B$. A statement that is true because there is nothing to check is **vacuously true**. So $\emptyset \subseteq B$ for every set $B$. Keep three objects apart: $\emptyset$ has no elements, $\{\emptyset\}$ has one element (the empty set), and $\{0\}$ has one element (the number 0).

The **power set** of $A$, written $\mathcal{P}(A)$, is the set of all subsets of $A$. So $S \in \mathcal{P}(A)$ if and only if $S \subseteq A$. For $A = \{1, 2\}$, the power set is $\{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$. A set with $n$ elements has $2^n$ subsets, because each element is in or out. The elements of a power set are sets, which is why the membership test for it is a subset test.

An **ordered pair** $(a, b)$ is a pair where the order counts: $(a, b) = (c, d)$ if and only if $a = c$ and $b = d$. The **Cartesian product** of $A$ and $B$ is $A \times B = \{(a, b) : a \in A \text{ and } b \in B\}$. So $(a, b) \in A \times B$ if and only if $a \in A$ and $b \in B$. For $A = \{1, 2\}$ and $B = \{x, y, z\}$, the product has $2 \times 3 = 6$ pairs. In general $A \times B \ne B \times A$, because $(1, x)$ is not $(x, 1)$.

## How to do it

### Proving that $A \subseteq B$

1. Write what is to be shown: every element of $A$ is an element of $B$.
2. Begin with "Let $x \in A$." The letter $x$ is arbitrary, so assume nothing else about it.
3. Unpack the membership $x \in A$ with the test for $A$: if $A$ is an intersection, you get two facts, and if it is a set-builder set $\{y : P(y)\}$, you get $P(x)$.
4. Use the hypotheses and earlier results to reach the test for $B$. This is the working part.
5. Conclude "So $x \in B$." Since $x$ was arbitrary, $A \subseteq B$.

### Proving that $A = B$

Method one: two inclusions. Prove $A \subseteq B$ by the five steps above, then prove $B \subseteq A$ the same way. Label the two halves ($\subseteq$) and ($\supseteq$), exactly as in [if and only if proofs](01-if-and-only-if-proofs.md). The two halves may need different arguments.

Method two: a chain of equivalences. Start with "$x \in A$" and replace it, line by line, by statements that say the same thing, until you reach "$x \in B$". Every line must be equivalent to the line above it, so use only reversible steps. The justifications are the membership tests and the laws of logic, such as the distributive law or De Morgan's law for statements. Because the steps are reversible, one chain proves both inclusions.

### Set identities and truth tables

An identity between sets is an identity between statements. Write $p$ for "$x \in A$", $q$ for "$x \in B$" and $r$ for "$x \in C$". Then the membership of $x$ in the left side and in the right side of an identity are two compound statements in $p$, $q$, $r$, and the identity holds exactly when those statements are logically equivalent. For example, $x \in A \cap (B \cup C)$ means $p \wedge (q \vee r)$, and $x \in (A \cap B) \cup (A \cap C)$ means $(p \wedge q) \vee (p \wedge r)$.

The truth table has eight rows, one for each way an element can sit relative to three sets, which are the eight regions of a three-set Venn diagram. Here it is for the distributive law:

| $x \in A$ | $x \in B$ | $x \in C$ | $x \in B \cup C$ | $x \in A \cap (B \cup C)$ | $x \in A \cap B$ | $x \in A \cap C$ | $x \in (A \cap B) \cup (A \cap C)$ |
|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T | T |
| T | T | F | T | T | T | F | T |
| T | F | T | T | T | F | T | T |
| T | F | F | F | F | F | F | F |
| F | T | T | T | F | F | F | F |
| F | T | F | T | F | F | F | F |
| F | F | T | T | F | F | F | F |
| F | F | F | F | F | F | F | F |

The two columns for the left and right sides match in every row, so the identity holds. A truth table is a complete proof for any identity in a fixed number of sets, because an element can only be in one of the finitely many positions. It is the same method as in the truth-table lesson, with the columns renamed.

Two things the table does not do. It does not teach you much about why the identity holds, and it does not extend to statements about infinitely many sets. For those, use element chasing.

### Disproving a set claim

To show that a set identity is false, build sets where the two sides differ.

1. Find a row of the truth table where the two sides disagree. That row says where a single element has to sit.
2. Put one element in exactly those sets, and keep the other sets empty or tiny.
3. Compute both sides for your sets and show that they differ.

A claim about sets is false as soon as one choice of sets breaks it, so small sets are enough. Example 4 does this twice.

### A first theorem, in full

*Theorem 1 (distributive law).* For all sets $A$, $B$ and $C$, $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.

What we know: the membership tests for $\cap$ and $\cup$. What we want: each side is a subset of the other. The plan: two inclusions, where each step unpacks one test and the logic is the distributive law for "and" over "or".

*Proof.* ($\subseteq$) Let $x \in A \cap (B \cup C)$. Then $x \in A$ and $x \in B \cup C$. The second fact means $x \in B$ or $x \in C$. If $x \in B$, then $x \in A$ and $x \in B$, so $x \in A \cap B$. If $x \in C$, then $x \in A$ and $x \in C$, so $x \in A \cap C$. In both cases $x \in (A \cap B) \cup (A \cap C)$.

($\supseteq$) Let $x \in (A \cap B) \cup (A \cap C)$. Then $x \in A \cap B$ or $x \in A \cap C$. If $x \in A \cap B$, then $x \in A$ and $x \in B$, so $x \in B \cup C$ and therefore $x \in A \cap (B \cup C)$. If $x \in A \cap C$, then $x \in A$ and $x \in C$, so again $x \in B \cup C$ and $x \in A \cap (B \cup C)$. $\blacksquare$

Look back: each half has a proof by cases, one case for each side of the "or". The cases correspond to the rows of the table in which the element is in $A$. The proof is also correct when a set is empty or when two sets are equal, because it never assumed otherwise.

## Worked examples

<div class="example" markdown>

### Example 1: a subset stays a subset after intersecting

*Theorem 2.* Let $A$, $B$ and $C$ be sets. If $A \subseteq B$, then $A \cap C \subseteq B \cap C$.

The statement has the form "if $P$, then $Q$", and the conclusion is a subset claim. We use the steps of "Proving that $A \subseteq B$".

What we know: every element of $A$ is in $B$ (the hypothesis). What we want: every element of $A \cap C$ is in $B \cap C$. The plan: an element of $A \cap C$ is in $A$, so the hypothesis puts it in $B$; it is also in $C$, so it lies in both $B$ and $C$.

*Proof.* Suppose $A \subseteq B$. To show $A \cap C \subseteq B \cap C$, let $x \in A \cap C$ (Steps 1 and 2). Then $x \in A$ and $x \in C$ (Step 3). Since $x \in A$ and $A \subseteq B$, we have $x \in B$ (Step 4, using the hypothesis). So $x \in B$ and $x \in C$, that is, $x \in B \cap C$ (Step 5). Since $x$ was an arbitrary element of $A \cap C$, we have $A \cap C \subseteq B \cap C$. $\blacksquare$

Look back: the hypothesis was used once, on the element's membership in $A$. The converse is false: from $A \cap C \subseteq B \cap C$ you can't conclude $A \subseteq B$. For $A = \{1, 2\}$, $B = \{1\}$ and $C = \{1\}$, we get $A \cap C = \{1\} \subseteq \{1\} = B \cap C$, but $A \not\subseteq B$ since $2 \in A$ and $2 \notin B$.

Check with small sets: $A = \{1, 2\}$, $B = \{1, 2, 3\}$ and $C = \{2, 3, 4\}$. Then $A \cap C = \{2\}$ and $B \cap C = \{2, 3\}$, and $\{2\} \subseteq \{2, 3\}$.

</div>

<div class="example" markdown>

### Example 2: De Morgan's law for sets

*Theorem 3.* For all subsets $A$ and $B$ of a universal set $U$, $(A \cup B)^c = A^c \cap B^c$.

The proof is a chain of equivalences. Each step is justified by a membership test or by De Morgan's law for statements from the truth-table lesson, $\neg(p \vee q) \equiv \neg p \wedge \neg q$.

*Proof.* Let $x \in U$. Then

$$
\begin{aligned}
x \in (A \cup B)^c &\Leftrightarrow x \notin A \cup B && \text{(test for the complement)} \\
&\Leftrightarrow \neg(x \in A \text{ or } x \in B) && \text{(test for the union)} \\
&\Leftrightarrow x \notin A \text{ and } x \notin B && \text{(De Morgan's law for statements)} \\
&\Leftrightarrow x \in A^c \text{ and } x \in B^c && \text{(test for the complement)} \\
&\Leftrightarrow x \in A^c \cap B^c && \text{(test for the intersection).}
\end{aligned}
$$

So the two sets have the same elements. $\blacksquare$

Look back: the set law is the statement law with $\vee$ changed to $\cup$ and $\wedge$ changed to $\cap$. The other De Morgan law, $(A \cap B)^c = A^c \cup B^c$, has the same proof with the roles swapped. Every step is a biconditional, which is what allows one chain to prove both inclusions.

Check: with $U = \{1, \dots, 6\}$, $A = \{1, 2, 3\}$ and $B = \{2, 3, 4\}$: $A \cup B = \{1, 2, 3, 4\}$, so $(A \cup B)^c = \{5, 6\}$. Also $A^c = \{4, 5, 6\}$ and $B^c = \{1, 5, 6\}$, so $A^c \cap B^c = \{5, 6\}$.

</div>

<div class="example" markdown>

### Example 3: the empty set and vacuous truth

*Theorem 4.* For every set $A$: (a) $\emptyset \subseteq A$; (b) $A \cap \emptyset = \emptyset$; (c) if $A \subseteq \emptyset$, then $A = \emptyset$.

*Proof.* (a) We must show that every element of $\emptyset$ is in $A$. The empty set has no elements, so there is nothing to check, and the statement is true. (If you prefer to see a contradiction: suppose $\emptyset \not\subseteq A$. Then some $x \in \emptyset$ has $x \notin A$, but nothing is in $\emptyset$.)

(b) We show two inclusions. ($\subseteq$) Let $x \in A \cap \emptyset$. Then $x \in A$ and $x \in \emptyset$, so in particular $x \in \emptyset$. ($\supseteq$) By part (a), $\emptyset \subseteq A \cap \emptyset$, because the empty set is a subset of every set.

(c) Suppose $A \subseteq \emptyset$. Also $\emptyset \subseteq A$ by (a). Two inclusions give $A = \emptyset$. $\blacksquare$

Look back: the point of (a) is that a statement "for every element of this set, ..." about the empty set is true with no checking. This is why $\{x \in \mathbb{R} : x^2 = -1\} \subseteq \mathbb{Z}$ is true. The common error is to confuse $\emptyset \subseteq A$ (true for all $A$) with $\emptyset \in A$ (true only if $A$ happens to contain the empty set as an element).

Check: $A \cap \emptyset$ for $A = \{1, 2\}$: no element is in both, so the result is $\emptyset$. And $\{1, 2\} \subseteq \emptyset$ is false, which is consistent with (c): its hypothesis fails.

</div>

<div class="example" markdown>

### Example 4: two false identities

Disprove each claim. (a) For all sets, $A \cup (B \setminus C) = (A \cup B) \setminus C$. (b) For all sets, $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$.

(a) Step 1 of "Disproving a set claim": find a row of the truth table where the sides differ. An element in $A$ and in $C$ but not in $B$ is in the left side (it is in $A$) but not in the right side (it is in $C$). Step 2: put one element in $A$ and $C$ only. Take $A = \{1\}$, $B = \emptyset$ and $C = \{1\}$. Step 3: the left side is $\{1\} \cup (\emptyset \setminus \{1\}) = \{1\} \cup \emptyset = \{1\}$. The right side is $(\{1\} \cup \emptyset) \setminus \{1\} = \{1\} \setminus \{1\} = \emptyset$. Since $\{1\} \ne \emptyset$, the claim is false.

(b) Take $A = \{1\}$ and $B = \{2\}$. Then $\mathcal{P}(A) = \{\emptyset, \{1\}\}$ and $\mathcal{P}(B) = \{\emptyset, \{2\}\}$, so $\mathcal{P}(A) \cup \mathcal{P}(B) = \{\emptyset, \{1\}, \{2\}\}$ has 3 elements. But $A \cup B = \{1, 2\}$, and $\mathcal{P}(A \cup B) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$ has 4 elements, including $\{1, 2\}$. The set $\{1, 2\}$ is in the left side and not in the right side, so the claim is false.

Look back: in (b) one inclusion is true, and the proof is a good short exercise: $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$. The false direction needs a subset that takes elements from both sets. In (a), the correct identity is $(A \cup B) \setminus C \subseteq A \cup (B \setminus C)$, with equality when $A \cap C = \emptyset$.

Check: both sides were computed in full, so the sets differ by listing, with $\{1\}$ against $\emptyset$ and $4$ elements against $3$.

</div>

<div class="example" markdown>

### Example 5: a product over a union (finish it yourself)

*Theorem 5.* For all sets $A$, $B$ and $C$, $A \times (B \cup C) = (A \times B) \cup (A \times C)$.

An element of a product is an ordered pair, so we start with an arbitrary pair and use the test for the product.

($\subseteq$) Let $(a, b) \in A \times (B \cup C)$. Then $a \in A$ and $b \in B \cup C$, so $b \in B$ or $b \in C$. If $b \in B$, then $(a, b) \in A \times B$. If $b \in C$, then $(a, b) \in A \times C$. In either case $(a, b) \in (A \times B) \cup (A \times C)$.

($\supseteq$) Now prove the other inclusion: start with an arbitrary element of $(A \times B) \cup (A \times C)$ and show it lies in $A \times (B \cup C)$.

<details class="solution" markdown>
<summary>Finish</summary>

($\supseteq$) Let $z \in (A \times B) \cup (A \times C)$. Then $z \in A \times B$ or $z \in A \times C$, so $z$ is an ordered pair $(a, b)$ with $a \in A$ and either $b \in B$ or $b \in C$. In both cases $b \in B \cup C$, so $(a, b) \in A \times (B \cup C)$. $\blacksquare$

Check: $A = \{1, 2\}$, $B = \{x\}$, $C = \{y\}$. Then $B \cup C = \{x, y\}$ and $A \times (B \cup C)$ has 4 pairs: $(1, x), (1, y), (2, x), (2, y)$. Also $A \times B = \{(1, x), (2, x)\}$ and $A \times C = \{(1, y), (2, y)\}$, whose union is the same 4 pairs.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for proving a set claim from a Venn diagram. A diagram with three overlapping circles shows one arrangement. It does not show the cases where a region is empty, two sets are equal or one set contains another. Use the diagram to guess, and use element chasing or a full truth table to prove.

</div>

<div class="warning" markdown>

Watch out for proving only one inclusion. "Let $x \in A \cap (B \cup C)$ ... so $x \in (A \cap B) \cup (A \cap C)$" proves $A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C)$ and no more. For equality, the reverse inclusion is a separate proof, unless every line of your chain is an equivalence.

</div>

<div class="warning" markdown>

Watch out for starting with the conclusion. A proof that $A \subseteq B$ begins with "Let $x \in A$", not "Let $x \in B$". Starting from $x \in B$ and arriving at $x \in A$ proves $B \subseteq A$, the other claim.

</div>

<div class="warning" markdown>

Watch out for confusing $\in$ with $\subseteq$. The statement $1 \in \{1, 2\}$ is true, and $1 \subseteq \{1, 2\}$ is not even meaningful, because 1 is a number and not a set. On the other hand $\{1\} \subseteq \{1, 2\}$ is true, and $\{1\} \in \{1, 2\}$ is false. For the empty set, $\emptyset \subseteq \{1\}$ is true and $\emptyset \in \{1\}$ is false. Check which side of the symbol is an element and which is a set.

</div>

<div class="warning" markdown>

Watch out for a proof that needs a set to be nonempty without saying so. A first step such as "Pick an element $a \in A$" is not available when $A = \emptyset$, and the claim may still be true: $\emptyset \times B = \emptyset$ is an example. The "Let $x \in A$" of element chasing is safe, because if $A$ is empty there is nothing left to prove.

</div>

The universal set matters for complements. In De Morgan's law, $A^c$ means "in $U$ and not in $A$". If the problem doesn't name $U$, the proof should say "all sets are subsets of a universal set $U$".

## Tricks and shortcuts

Turn a set identity into a statement about one element, and translate to logic with $p$, $q$ and $r$. If the two compound statements are equivalent, the identity is true, and the chain of equivalences you used to check it is the proof.

A universe with one element is one row of the truth table. For an identity built from $\cap$, $\cup$, $\setminus$ and complements, checking every choice of $A$, $B$ and $C$ inside the one-element universe $\{1\}$ takes $2^3 = 8$ cases, one for each row of the table. If the identity fails for some sets, it fails in one of those eight cases, so a short program (see below) finds a counterexample fast.

For "if $A \subseteq B$ then ..." claims, use the hypothesis only on elements of $A$. The hypothesis says nothing about elements outside $A$.

To build a counterexample, make the sets as small as the failing row of the table needs. Often one element and some empty sets suffice.

## In code

Python's `set` type has the same operators as the proofs: `&`, `|`, `-`, `<=` and `==`. The code checks the distributive law and De Morgan's law on all subsets of a 3-element universe, counts the failures of a false identity, and builds a power set and a Cartesian product.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import combinations, product

def power_set(s):
    s = list(s)
    return [frozenset(c) for r in range(len(s) + 1) for c in combinations(s, r)]

U = frozenset({1, 2, 3})
subsets = power_set(U)
print(len(subsets))                                              # 8

def comp(X):
    return U - X

print(all(A & (B | C) == (A & B) | (A & C)
          for A in subsets for B in subsets for C in subsets))   # True
print(all(comp(A | B) == comp(A) & comp(B) for A in subsets for B in subsets))   # True

bad = [(set(A), set(B), set(C)) for A, B, C in product(subsets, repeat=3)
       if A | (B - C) != (A | B) - C]
print(len(bad), min(bad, key=lambda t: sum(map(len, t))))        # 296 ({1}, set(), {1})

A, B = frozenset({1}), frozenset({2})
lhs = set(power_set(A | B))
rhs = set(power_set(A)) | set(power_set(B))
print(len(lhs), len(rhs), rhs <= lhs)                            # 4 3 True

X, Y, Z = {1, 2}, {'x'}, {'y'}
print(set(product(X, Y | Z)) == set(product(X, Y)) | set(product(X, Z)))   # True
```

This tests 512 triples of subsets of a 3-element universe. It supports the identities but does not prove them for all sets; the element-chasing proof does. The counterexample found for the false identity is the same one used in Example 4: $A = \{1\}$, $B = \emptyset$, $C = \{1\}$.

</details>

## FAQ

### Why is the empty set a subset of every set?

Because to fail to be a subset, a set needs an element that is not in the other set, and the empty set has no elements. A statement that begins "for every element of the empty set" can never be falsified. This is the same reason that "every unicorn in this room is purple" is true when the room has no unicorns. It is a useful convention, and also a theorem: with the definition of subset as stated, $\emptyset \subseteq A$ follows.

### Do I have to prove both inclusions every time?

Unless your chain of steps is made only of equivalences, yes. A chain made only of equivalences proves both inclusions at once, as in Example 2. A chain that uses "implies" in one step proves one inclusion only. When in doubt, write the two halves separately; it takes little extra space.

### What is the difference between $\mathcal{P}(A)$ and $A$ itself?

$A$ is a set of objects, and $\mathcal{P}(A)$ is a set of sets: its elements are the subsets of $A$. So $1 \in A$ but $1 \notin \mathcal{P}(A)$, while $\{1\} \in \mathcal{P}(A)$. Every element of $A$ becomes a one-element subset, and the empty set and $A$ itself are in $\mathcal{P}(A)$ too.

### Is a proof by truth table acceptable?

Yes, if the identity involves a fixed number of sets and you fill the table correctly, because it checks every possible position of an element. Your course may ask for element chasing instead, which gives a reason as well as a check. Learn both. The element-chasing proof also extends to infinite families of sets, which a table can't.

## Practice

### Warm-up

1\. Let $U = \{1, 2, 3, 4, 5, 6\}$, $A = \{1, 2, 3\}$, $B = \{2, 3, 4\}$ and $C = \{3, 4, 5\}$. Compute (a) $A \cap (B \cup C)$ and $(A \cap B) \cup (A \cap C)$; (b) $(A \cup B)^c$ and $A^c \cap B^c$; (c) $A \setminus B$ and $A \cap B^c$; (d) $\lvert \mathcal{P}(A) \rvert$ and $\lvert A \times B \rvert$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $B \cup C = \{2, 3, 4, 5\}$, so $A \cap (B \cup C) = \{2, 3\}$. Also $A \cap B = \{2, 3\}$ and $A \cap C = \{3\}$, so the union is $\{2, 3\}$.
- (b) $A \cup B = \{1, 2, 3, 4\}$, so $(A \cup B)^c = \{5, 6\}$. Also $A^c = \{4, 5, 6\}$ and $B^c = \{1, 5, 6\}$, so $A^c \cap B^c = \{5, 6\}$.
- (c) $A \setminus B = \{1\}$. Also $B^c = \{1, 5, 6\}$, so $A \cap B^c = \{1\}$.
- (d) $A$ has 3 elements, so $\lvert \mathcal{P}(A) \rvert = 2^3 = 8$. And $\lvert A \times B \rvert = 3 \cdot 3 = 9$.

Check: each pair in (a), (b) and (c) matches, which is what Theorems 1, 3 and Practice problem 4 say.

</details>

2\. Decide whether each statement is true or false, with a reason. (a) $\emptyset \subseteq \emptyset$. (b) $\emptyset \in \emptyset$. (c) $\emptyset \in \{\emptyset\}$. (d) $\emptyset \subseteq \{\emptyset\}$. (e) $\{\emptyset\} \subseteq \emptyset$. (f) $\emptyset \in \mathcal{P}(\{1, 2\})$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) True: the empty set is a subset of every set, itself included.
- (b) False: the empty set has no elements.
- (c) True: the one element of $\{\emptyset\}$ is $\emptyset$.
- (d) True: $\emptyset$ is a subset of every set.
- (e) False: $\{\emptyset\}$ has an element, $\emptyset$, which is not in $\emptyset$.
- (f) True: $\emptyset$ is a subset of $\{1, 2\}$, so it is an element of the power set.

Check: the power set of $\{1, 2\}$ is $\{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$, and it lists $\emptyset$ as an element.

</details>

3\. (Reviews [compound inequalities and interval notation](../../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md).) Prove that $[1, 5] \cap (3, 8) = (3, 5]$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $x \in [1, 5]$ means $1 \le x \le 5$, and $x \in (3, 8)$ means $3 < x < 8$. What we want: the elements of the intersection are exactly those with $3 < x \le 5$. The plan: a chain of equivalences, using that some of the inequalities follow from the others.

*Proof.* For a real number $x$,

$$
\begin{aligned}
x \in [1, 5] \cap (3, 8) &\Leftrightarrow (1 \le x \le 5) \text{ and } (3 < x < 8) \\
&\Leftrightarrow 3 < x \le 5.
\end{aligned}
$$

The second step: if $3 < x \le 5$, then $1 \le x$ (because $1 < 3 < x$) and $x < 8$ (because $x \le 5 < 8$), so all four inequalities hold. Conversely, the four inequalities include $3 < x$ and $x \le 5$. So the two lines are equivalent, and $x \in (3, 5]$. $\blacksquare$

Check: $x = 4$ is in both sides, and $x = 3$ and $x = 5.5$ are in neither. The point $x = 5$ is in the intersection, since $5 \in [1, 5]$ and $5 \in (3, 8)$.

</details>

### Standard

4\. Prove that for subsets of a universal set $U$, $A \setminus B = A \cap B^c$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the tests for $\setminus$, $\cap$ and the complement. What we want: the same elements on both sides. The plan: a chain of equivalences, since each test is a biconditional.

*Proof.* For $x \in U$,

$$
\begin{aligned}
x \in A \setminus B &\Leftrightarrow x \in A \text{ and } x \notin B && \text{(test for difference)} \\
&\Leftrightarrow x \in A \text{ and } x \in B^c && \text{(test for complement)} \\
&\Leftrightarrow x \in A \cap B^c && \text{(test for intersection).}
\end{aligned}
$$

$\blacksquare$

Look back: this identity lets you rewrite any difference as an intersection, which is why many texts do not treat $\setminus$ as a separate operation. Check: $A = \{1, 2, 3\}$, $B = \{2, 3, 4\}$, $U = \{1, \dots, 6\}$: both sides are $\{1\}$.

</details>

5\. Prove that for sets $A$ and $B$, the following are equivalent: (i) $A \subseteq B$; (ii) $A \cap B = A$; (iii) $A \cup B = B$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the definitions of subset, intersection and union. What we want: a cycle (i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) $\Rightarrow$ (i), as in Example 3 of [if and only if proofs](01-if-and-only-if-proofs.md#worked-examples).

*Proof.* (i) $\Rightarrow$ (ii). Suppose $A \subseteq B$. Always $A \cap B \subseteq A$. For the reverse, let $x \in A$. Then $x \in B$ by (i), so $x \in A \cap B$. Hence $A \cap B = A$.

(ii) $\Rightarrow$ (iii). Suppose $A \cap B = A$. Always $B \subseteq A \cup B$. For the reverse, let $x \in A \cup B$. If $x \in B$ we are done. If $x \in A$, then $x \in A \cap B$ by (ii), so $x \in B$. Hence $A \cup B = B$.

(iii) $\Rightarrow$ (i). Suppose $A \cup B = B$. Let $x \in A$. Then $x \in A \cup B = B$, so $x \in B$. Hence $A \subseteq B$. $\blacksquare$

Check: $A = \{1, 2\}$ and $B = \{1, 2, 3\}$ satisfy all three: $A \cap B = \{1, 2\} = A$ and $A \cup B = \{1, 2, 3\} = B$. With $A = \{1, 4\}$, none of them hold.

</details>

6\. Prove or disprove each claim. (a) $A \cap (B \setminus C) = (A \cap B) \setminus C$. (b) $A \cup (B \setminus C) = (A \cup B) \setminus C$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) True. For any $x$:

$$
\begin{aligned}
x \in A \cap (B \setminus C) &\Leftrightarrow x \in A \text{ and } (x \in B \text{ and } x \notin C) \\
&\Leftrightarrow (x \in A \text{ and } x \in B) \text{ and } x \notin C \\
&\Leftrightarrow x \in (A \cap B) \setminus C.
\end{aligned}
$$

The middle step regroups "and". Each line is an equivalence, so the sets are equal.

(b) False. Take $A = \{1\}$, $B = \emptyset$ and $C = \{1\}$. The left side is $\{1\}$ and the right side is $\emptyset$ (Example 4).

Check for (a) with $A = \{1, 2, 3\}$, $B = \{2, 3, 4\}$ and $C = \{3\}$: $B \setminus C = \{2, 4\}$ and $A \cap \{2, 4\} = \{2\}$; also $A \cap B = \{2, 3\}$ and $\{2, 3\} \setminus \{3\} = \{2\}$.

</details>

### Challenge

7\. Prove that $\mathcal{P}(A) \cap \mathcal{P}(B) = \mathcal{P}(A \cap B)$ for all sets $A$ and $B$. Then prove that $\mathcal{P}(A) \cup \mathcal{P}(B) \subseteq \mathcal{P}(A \cup B)$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $S \in \mathcal{P}(X)$ means $S \subseteq X$. What we want: a chain of equivalences for the first claim, and one inclusion for the second. The plan: apply the subset test for each side, and use that being a subset of both $A$ and $B$ means being a subset of $A \cap B$.

*Proof of the first claim.* Let $S$ be any set. Then $S \in \mathcal{P}(A) \cap \mathcal{P}(B)$ if and only if $S \subseteq A$ and $S \subseteq B$. This holds if and only if every element of $S$ is in $A$ and in $B$, which means every element of $S$ is in $A \cap B$, that is, $S \subseteq A \cap B$, that is, $S \in \mathcal{P}(A \cap B)$.

*Proof of the second claim.* Let $S \in \mathcal{P}(A) \cup \mathcal{P}(B)$. Then $S \subseteq A$ or $S \subseteq B$. In the first case, every element of $S$ is in $A$, hence in $A \cup B$; in the second case the same argument works with $B$. Either way $S \subseteq A \cup B$, so $S \in \mathcal{P}(A \cup B)$. $\blacksquare$

The inclusion in the second claim can be strict, as Example 4(b) shows.

Check: $A = \{1, 2\}$, $B = \{2, 3\}$. Then $A \cap B = \{2\}$ and $\mathcal{P}(A \cap B) = \{\emptyset, \{2\}\}$. Also $\mathcal{P}(A) \cap \mathcal{P}(B)$: the subsets of $A$ are $\emptyset, \{1\}, \{2\}, \{1, 2\}$ and of $B$ are $\emptyset, \{2\}, \{3\}, \{2, 3\}$, and the common ones are $\emptyset$ and $\{2\}$.

</details>

8\. Prove that $(A \cap B) \times (C \cap D) = (A \times C) \cap (B \times D)$ for all sets $A$, $B$, $C$ and $D$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the tests for $\times$ and $\cap$. What we want: equality of two sets of pairs. The plan: a chain of equivalences on an arbitrary pair.

*Proof.* A pair $(x, y)$ belongs to the left side or to the right side; consider an arbitrary ordered pair $(x, y)$. Then

$$
\begin{aligned}
(x, y) \in (A \cap B) \times (C \cap D) &\Leftrightarrow x \in A \cap B \text{ and } y \in C \cap D \\
&\Leftrightarrow (x \in A \text{ and } x \in B) \text{ and } (y \in C \text{ and } y \in D) \\
&\Leftrightarrow (x \in A \text{ and } y \in C) \text{ and } (x \in B \text{ and } y \in D) \\
&\Leftrightarrow (x, y) \in A \times C \text{ and } (x, y) \in B \times D \\
&\Leftrightarrow (x, y) \in (A \times C) \cap (B \times D).
\end{aligned}
$$

The third line only rearranges the four statements joined by "and". Every element of either side is an ordered pair, so the two sets are equal. $\blacksquare$

Look back: the identity for union is different. $(A \cup B) \times (C \cup D)$ is not in general equal to $(A \times C) \cup (B \times D)$: with $A = C = \{1\}$ and $B = D = \{2\}$, the left side has the pair $(1, 2)$ and the right side doesn't. Check: $A = \{1, 2\}$, $B = \{2, 3\}$, $C = \{a\}$, $D = \{a, b\}$: the left side is $\{2\} \times \{a\} = \{(2, a)\}$, and the right side is $\{(1, a), (2, a)\} \cap \{(2, a), (2, b), (3, a), (3, b)\} = \{(2, a)\}$.

</details>

## Where this shows up

- The next lesson, [counterexamples and disproof](04-counterexamples-and-disproof.md), applies the small-set method of Example 4 to many kinds of claims. Later chapters use the same element-chasing proofs for relations and functions: the image of a union, the preimage of an intersection, and [whether a function is injective](../06-relations-and-functions/05-injective-surjective-bijective.md).
- In CS, a set identity is a query identity: `A INTERSECT (B UNION C)` equals `(A INTERSECT B) UNION (A INTERSECT C)` in SQL, and a query planner uses it to rewrite a query. Regular languages and automata are sets of strings, and the closure properties of those languages (union, intersection, complement) are proved by element chasing on strings; see Finite automata: DFA and NFA<!-- link: ../../06-cs-math/06-theory-of-computation/01-finite-automata-dfa-and-nfa.md -->.
- In probability, events are sets, and De Morgan's laws turn "neither event happens" into the complement of a union (sample spaces, events and axioms<!-- link: ../../05-university-core/07-probability/01-sample-spaces-events-and-axioms.md -->).
