# Proofs and logic

The language of mathematics, logic, sets, and how to read, find and write proofs. The bridge from high school math to university courses.

Before this folder: High school, especially functions, sets notation and sequences.

## How to use this folder

Take the [diagnostic](diagnostic.md) first, without notes. It asks two questions on each of the first 31 lessons and one on the mixed proof practice, 63 in all, and its answer table names the lesson to study for each one you miss, so you can do only those lessons. Each chapter has a cheat sheet (the links are below), and each lesson starts with a quick check.

The [Anki deck for this folder](../downloads/anki/04-proofs-and-logic.apkg) holds the definitions, negation rules, equivalences, first lines of the proof methods and the pairs that are easy to confuse, such as the converse and the contrapositive, an element and a subset, and injective and surjective. In Anki desktop choose File, then Import, and [Anki decks](../00-start-here/index.md#anki-decks) covers phones.

Use the last lesson, [mixed proof practice](07-putting-it-together/02-mixed-proof-practice.md), as the final check. For each problem, name the method and write the first line before you open the solution. If you can do that for most of the warm-up and standard problems, you have the base that proof-heavy courses assume.

## Fast path for a CS student

If you are short on time, these lessons carry the most weight in the later folders and in a CS degree. They are listed in reading order, so each one only needs the ones above it.

| Lesson | Where it comes back |
|---|---|
| [Proof language: let, suppose, WLOG](01-language-and-notation/03-proof-language-let-suppose-wlog.md) | the wording of every proof in discrete math and algorithms |
| [Reading math symbols](01-language-and-notation/04-reading-math-symbols.md) | every textbook, and the notation of linear algebra |
| [Conditionals and biconditionals](02-logic-and-sets/02-conditionals-and-biconditionals.md) | theorem statements, specifications and `if` conditions in code |
| [Quantifiers](02-logic-and-sets/04-quantifiers.md) | the [epsilon-delta definition](../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md) of a limit, and discrete math |
| [Negation and translating English](02-logic-and-sets/05-negation-and-translating-english.md) | negating a limit definition, the pumping lemma in theory of computation |
| [Direct proof](03-core-proof-methods/01-direct-proof.md) | most proofs in discrete math and linear algebra |
| [How to read a proof](03-core-proof-methods/02-how-to-read-a-proof.md) | every course, since you learn from the proofs in the text |
| [Scratch work and proof strategies](03-core-proof-methods/03-scratch-work-and-proof-strategies.md) | finding a proof in algorithms and discrete math |
| [Proof by contradiction](03-core-proof-methods/06-proof-by-contradiction.md) | irrationality, infinitely many primes, and the halting problem in theory of computation |
| [How to write a proof](03-core-proof-methods/07-how-to-write-a-proof.md) | every graded proof you hand in |
| [Proofs about sets](04-more-proof-methods/03-proofs-about-sets.md) | languages in theory of computation, and subspaces in linear algebra |
| [Mathematical induction](05-induction/01-mathematical-induction.md) | sums and recurrences in discrete math, and loop invariants in algorithms |
| [Strong induction and well-ordering](05-induction/02-strong-induction-and-well-ordering.md) | correctness of recursive algorithms, and divide and conquer |
| [Injective, surjective and bijective](06-relations-and-functions/05-injective-surjective-bijective.md) | one-to-one and onto linear maps, and counting by bijection in discrete math |
| [Common proof mistakes](07-putting-it-together/01-common-proof-mistakes.md) | checking your own proofs before you hand them in |

The lessons not in the table can wait. Skim the first two lessons of chapter 1 and the lessons on cases, the contrapositive and counterexamples if the diagnostic questions on them were easy. Come back to the chapter on relations and functions when discrete math reaches equivalence relations and partial orders, to cardinality and countability before theory of computation, and to structural induction when you meet recursive data types.

## Cheat sheet

Each chapter has a cheat sheet with the rules, tables and common mistakes of its lessons. This is the map.

- [Language and notation](01-language-and-notation/index.md#cheat-sheet) covers what counts as a proof, the working definitions, proof phrases and how to read symbols.
- [Logic and sets](02-logic-and-sets/index.md#cheat-sheet) covers truth tables, conditionals, equivalence laws, quantifiers, negation and set operations.
- [Core proof methods](03-core-proof-methods/index.md#cheat-sheet) covers direct proof, reading and writing proofs, cases, the contrapositive and contradiction.
- [More proof methods](04-more-proof-methods/index.md#cheat-sheet) covers if and only if, existence and uniqueness, proofs about sets and counterexamples.
- [Induction](05-induction/index.md#cheat-sheet) covers ordinary and strong induction, well-ordering and structural induction.
- [Relations and functions](06-relations-and-functions/index.md#cheat-sheet) covers relation properties, equivalence relations, partial orders, well-definedness, injective and surjective maps, and countability.
- [Putting it together](07-putting-it-together/index.md#cheat-sheet) covers the common proof mistakes and the full strategy table.

The two tables used most are below in short form. The [full strategy table](07-putting-it-together/index.md#cheat-sheet) names a lesson for each row.

| The claim has the shape | Usual first line |
|---|---|
| for every $x$ in $S$, $P(x)$ | Let $x$ be an arbitrary element of $S$. |
| there exists $x$ with $P(x)$ | Take $x = \dots$, then check it. |
| if $P$, then $Q$ | Suppose $P$. Or prove the contrapositive. |
| negative, "irrational", "infinitely many" | Suppose, for contradiction, that ... |
| $P$ or $Q$ | Suppose not $P$; we show $Q$. |
| $P$ if and only if $Q$ | Prove ($\Rightarrow$) and ($\Leftarrow$), each from its own hypothesis. |
| exactly one $x$ | Existence, then uniqueness: suppose $x$ and $y$ both work. |
| $A \subseteq B$, $A = B$ | Let $x \in A$; for equality, prove both inclusions. |
| for every $n \ge n_0$, a sum or a recurrence | By induction on $n$; check the base case. |
| the claim may be false | Test $0$, $1$, $-1$ and $\emptyset$, then find a counterexample. |

The negation rules, each pushed in one layer:

| Statement | Negation |
|---|---|
| $\neg P$ | $P$ |
| $P \wedge Q$ | $\neg P \vee \neg Q$ |
| $P \vee Q$ | $\neg P \wedge \neg Q$ |
| $P \Rightarrow Q$ | $P \wedge \neg Q$ |
| $\forall x\,P(x)$ | $\exists x\,\neg P(x)$ |
| $\exists x\,P(x)$ | $\forall x\,\neg P(x)$ |


<!-- lessons:start -->
## Lessons

### 1. [Language and notation](01-language-and-notation/index.md)

1. [What is a proof](01-language-and-notation/01-what-is-a-proof.md)
2. [Definitions, theorems, lemmas and corollaries](01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md)
3. [Proof language: let, suppose, WLOG](01-language-and-notation/03-proof-language-let-suppose-wlog.md) (fast path)
4. [Reading math symbols](01-language-and-notation/04-reading-math-symbols.md) (fast path)

### 2. [Logic and sets](02-logic-and-sets/index.md)

1. [Statements and connectives](02-logic-and-sets/01-statements-and-connectives.md)
2. [Conditionals and biconditionals](02-logic-and-sets/02-conditionals-and-biconditionals.md) (fast path)
3. [Truth tables and logical equivalence](02-logic-and-sets/03-truth-tables-and-logical-equivalence.md)
4. [Quantifiers](02-logic-and-sets/04-quantifiers.md) (fast path)
5. [Negation and translating English](02-logic-and-sets/05-negation-and-translating-english.md) (fast path)
6. [Sets and set operations](02-logic-and-sets/06-sets-and-set-operations.md)

### 3. [Core proof methods](03-core-proof-methods/index.md)

1. [Direct proof](03-core-proof-methods/01-direct-proof.md) (fast path)
2. [How to read a proof](03-core-proof-methods/02-how-to-read-a-proof.md) (fast path)
3. [Scratch work and proof strategies](03-core-proof-methods/03-scratch-work-and-proof-strategies.md) (fast path)
4. [Proof by cases and WLOG](03-core-proof-methods/04-proof-by-cases-and-wlog.md)
5. [Contrapositive proof](03-core-proof-methods/05-contrapositive-proof.md)
6. [Proof by contradiction](03-core-proof-methods/06-proof-by-contradiction.md) (fast path)
7. [How to write a proof](03-core-proof-methods/07-how-to-write-a-proof.md) (fast path)

### 4. [More proof methods](04-more-proof-methods/index.md)

1. [If and only if proofs](04-more-proof-methods/01-if-and-only-if-proofs.md)
2. [Existence and uniqueness proofs](04-more-proof-methods/02-existence-and-uniqueness-proofs.md)
3. [Proofs about sets](04-more-proof-methods/03-proofs-about-sets.md) (fast path)
4. [Counterexamples and disproof](04-more-proof-methods/04-counterexamples-and-disproof.md)

### 5. [Induction](05-induction/index.md)

1. [Mathematical induction](05-induction/01-mathematical-induction.md) (fast path)
2. [Strong induction and well-ordering](05-induction/02-strong-induction-and-well-ordering.md) (fast path)
3. [Recursive definitions and structural induction](05-induction/03-recursive-definitions-and-structural-induction.md)

### 6. [Relations and functions](06-relations-and-functions/index.md)

1. [Relations and their properties](06-relations-and-functions/01-relations-and-their-properties.md)
2. [Equivalence relations and partitions](06-relations-and-functions/02-equivalence-relations-and-partitions.md)
3. [Partial orders](06-relations-and-functions/03-partial-orders.md)
4. [Functions and well-definedness](06-relations-and-functions/04-functions-and-well-definedness.md)
5. [Injective, surjective and bijective](06-relations-and-functions/05-injective-surjective-bijective.md) (fast path)
6. [Cardinality and countability](06-relations-and-functions/06-cardinality-and-countability.md)

### 7. [Putting it together](07-putting-it-together/index.md)

1. [Common proof mistakes](07-putting-it-together/01-common-proof-mistakes.md) (fast path)
2. [Mixed proof practice](07-putting-it-together/02-mixed-proof-practice.md)

<!-- lessons:end -->
