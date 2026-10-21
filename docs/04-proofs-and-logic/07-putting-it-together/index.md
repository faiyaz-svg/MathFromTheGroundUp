# Putting it together

Common mistakes in proofs, and a mixed set of proofs where you choose the method yourself.

1. [Common proof mistakes](01-common-proof-mistakes.md)
2. [Mixed proof practice](02-mixed-proof-practice.md)

## Cheat sheet

### Common proof mistakes

Check a proof in this order: is the claim true on a small case and an awkward case; does the first line assume exactly the hypothesis; is the last line exactly the claim; does every line have a reason; are the cases, base cases and inclusions all there; is each hypothesis used; does the proof survive a bad example.

Three kinds of trouble, and the repair depends on which one you have:

| Trouble | Repair |
|---|---|
| the claim is false | a counterexample, or a changed claim |
| a step is invalid | a different step |
| a step has no reason, or a case is missing | supply it |

Fifteen of the mistakes, in one line each:

| Mistake | In one line | Taught in |
|---|---|---|
| proving the converse | the proof assumes the conclusion and derives the hypothesis | [contrapositive proof](../03-core-proof-methods/05-contrapositive-proof.md) |
| assuming the conclusion | the reason for a step is the claim itself | [how to write a proof](../03-core-proof-methods/07-how-to-write-a-proof.md) |
| a wrong negation | "not ($P$ or $Q$)" is "not $P$ and not $Q$" | [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md) |
| quantifiers swapped | "there exists $N$ for every $n$" is not "for every $n$ there exists $N$" | [quantifiers](../02-logic-and-sets/04-quantifiers.md) |
| examples for a universal claim | examples can disprove a "for every" claim and never prove one | [counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md) |
| WLOG without a symmetry | swapping the names must give the same claim | [proof by cases and WLOG](../03-core-proof-methods/04-proof-by-cases-and-wlog.md) |
| a missing case | the cases must cover everything, and the proof says why | [proof by cases and WLOG](../03-core-proof-methods/04-proof-by-cases-and-wlog.md) |
| contradiction with no contradiction | derive a statement and its negation, not just something odd | [proof by contradiction](../03-core-proof-methods/06-proof-by-contradiction.md) |
| no base case | a correct step with no start proves nothing | [mathematical induction](../05-induction/01-mathematical-induction.md) |
| a step that fails for small $k$ | count base cases from the smallest $k$ where every cited case is in range | [strong induction and well-ordering](../05-induction/02-strong-induction-and-well-ordering.md) |
| proving the step backward | go from $P(k)$ to $P(k+1)$, never the reverse | [mathematical induction](../05-induction/01-mathematical-induction.md) |
| an element where a subset belongs | $A \in B$ does not mean $A \subseteq B$ | [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md) |
| one inclusion for a set equality | an equality needs both inclusions, and an unused hypothesis points to the missing half | [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md) |
| injectivity started from $a = a'$ | start from $f(a) = f(a')$ | [injective, surjective and bijective](../06-relations-and-functions/05-injective-surjective-bijective.md) |
| dividing by something that might be 0 | add the hypothesis, or factor instead | [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md) |

Four more in the full lesson: a rule that is not a function ([functions and well-definedness](../06-relations-and-functions/04-functions-and-well-definedness.md)), a letter used before it is introduced, symbol soup, and "clearly" in place of a reason ([how to write a proof](../03-core-proof-methods/07-how-to-write-a-proof.md)).

- Run your own proof on a bad input: $0$, a negative number, equal values, the empty set.
- List the hypotheses and tick off where each is used.
- Read the quantifiers aloud, left to right.
- A flawed proof of a true claim is common. A flawed proof of a false claim means the claim needs testing first.

### Mixed proof practice

Read the statement from the outside in. The full table, with the lesson for each row, is in [scratch work and proof strategies](../03-core-proof-methods/03-scratch-work-and-proof-strategies.md#choosing-a-method-from-the-shape-of-the-claim).

| The claim has the shape | Usual first line | Lesson |
|---|---|---|
| for every $x$ in $S$, $P(x)$ | Let $x$ be an arbitrary element of $S$. | [direct proof](../03-core-proof-methods/01-direct-proof.md) |
| there exists $x$ with $P(x)$ | Take $x = \dots$ (the witness), then check it. | [existence and uniqueness proofs](../04-more-proof-methods/02-existence-and-uniqueness-proofs.md) |
| if $P$, then $Q$ | Suppose $P$. | [direct proof](../03-core-proof-methods/01-direct-proof.md) |
| if $P$, then $Q$, with $P$ hard to use or $Q$ a negation | We prove the contrapositive: if not $Q$, then not $P$. | [contrapositive proof](../03-core-proof-methods/05-contrapositive-proof.md) |
| negative or "irrational", "no", "infinitely many" | Suppose, for contradiction, that ... | [proof by contradiction](../03-core-proof-methods/06-proof-by-contradiction.md) |
| $P$ or $Q$ | Suppose not $P$; we show $Q$. | [proof by cases and WLOG](../03-core-proof-methods/04-proof-by-cases-and-wlog.md) |
| a statement about parity, remainders or signs | There are two (or three) cases, covering ... | [proof by cases and WLOG](../03-core-proof-methods/04-proof-by-cases-and-wlog.md) |
| $P$ if and only if $Q$ | ($\Rightarrow$) Suppose $P$. Then later ($\Leftarrow$) Suppose $Q$. | [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md) |
| exactly one $x$ | Existence: ... Uniqueness: suppose $x$ and $y$ both ... | [existence and uniqueness proofs](../04-more-proof-methods/02-existence-and-uniqueness-proofs.md) |
| $A \subseteq B$ | Let $x \in A$. | [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md) |
| $A = B$ | We show $A \subseteq B$ and $B \subseteq A$. | [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md) |
| the claim may be false | Try $0$, $1$, $-1$, equal values, $\emptyset$; then a counterexample or a proof. | [counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md) |
| for every $n \ge n_0$, a sum, a recurrence or a divisibility claim | By induction on $n$. Base case, $n = n_0$. | [mathematical induction](../05-induction/01-mathematical-induction.md) |
| the step needs a case other than $k$ | By strong induction ... (count the base cases) | [strong induction and well-ordering](../05-induction/02-strong-induction-and-well-ordering.md) |
| a recursive set, tree or function | By structural induction: the basis, then each clause. | [recursive definitions and structural induction](../05-induction/03-recursive-definitions-and-structural-induction.md) |
| a relation is an equivalence relation or partial order | Check each property from its definition, starting from its own hypothesis. | [relations and their properties](../06-relations-and-functions/01-relations-and-their-properties.md) |
| a function is well defined | Take two names for one input and show the outputs agree. | [functions and well-definedness](../06-relations-and-functions/04-functions-and-well-definedness.md) |
| injective, surjective, bijective | Injective: suppose $f(a) = f(a')$. Surjective: let $b \in B$. | [injective, surjective and bijective](../06-relations-and-functions/05-injective-surjective-bijective.md) |
| a set is countable or uncountable | List it, or inject it into $\mathbb{N}$. For uncountable, a diagonal. | [cardinality and countability](../06-relations-and-functions/06-cardinality-and-countability.md) |
| a loop or recursive function is correct | State an invariant (or induct on input size). | [mathematical induction](../05-induction/01-mathematical-induction.md) |

- Two-minute rule: test small cases before writing a proof.
- A claim often has two shapes (a "for every" whose body is an "if-then"). The body needs the method.
- After solving, name the method in one line and say why you chose it.
- If nothing fits, write every defined word as its definition with fresh letters.
