# Logic and sets

The exact meaning of "and", "or", "not", "if", "for every" and "there exists", how to negate and translate statements, and the language of sets that every later proof is written in.

1. [Statements and connectives](01-statements-and-connectives.md)
2. [Conditionals and biconditionals](02-conditionals-and-biconditionals.md)
3. [Truth tables and logical equivalence](03-truth-tables-and-logical-equivalence.md)
4. [Quantifiers](04-quantifiers.md)
5. [Negation and translating English](05-negation-and-translating-english.md)
6. [Sets and set operations](06-sets-and-set-operations.md)

## Cheat sheet

### Statements and connectives

A statement is a sentence that is true or false. Questions, commands and open sentences such as "$x > 2$" are not statements. Math's "or" is inclusive.

| $P$ | $Q$ | $\neg P$ | $P \wedge Q$ | $P \vee Q$ | $P \oplus Q$ |
|---|---|---|---|---|---|
| T | T | F | T | T | F |
| T | F | F | F | T | T |
| F | T | T | F | T | T |
| F | F | T | F | F | F |

- Precedence: $\neg$, then $\wedge$, then $\vee$, then $\Rightarrow$ and $\Leftrightarrow$. Write brackets whenever $\wedge$ and $\vee$ mix.
- "But" and "although" mean $\wedge$. "Neither $P$ nor $Q$" is $\neg P \wedge \neg Q$. "Not both" is $\neg(P \wedge Q)$.
- A table with $n$ statements has $2^n$ rows. Python's `and` and `or` short-circuit and return an operand.

Main mistakes: reading "or" as exclusive; treating "$x > 2$" as a statement; writing `x == 1 or 2` for "x is 1 or 2".

### Conditionals and biconditionals

| $P$ | $Q$ | $P \Rightarrow Q$ | $Q \Rightarrow P$ | $\neg P \Rightarrow \neg Q$ | $\neg Q \Rightarrow \neg P$ | $P \Leftrightarrow Q$ |
|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T |
| T | F | F | T | T | F | F |
| F | T | T | F | F | T | F |
| F | F | T | T | T | T | T |

- $P \Rightarrow Q$ is false only when $P$ is true and $Q$ is false. A false hypothesis makes it vacuously true.
- All of these say $P \Rightarrow Q$: "if $P$, then $Q$", "$Q$ if $P$", "$P$ only if $Q$", "$Q$ whenever $P$", "$P$ is sufficient for $Q$", "$Q$ is necessary for $P$". "$P$ unless $Q$" is $\neg Q \Rightarrow P$.
- The contrapositive is equivalent to the original; the converse is equivalent to the inverse; the original and the converse are not equivalent.
- $P \Leftrightarrow Q$ means $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$. Definitions are biconditionals.

Main mistakes: affirming the consequent (from $P \Rightarrow Q$ and $Q$, concluding $P$); reversing "only if"; thinking a conditional claims cause.

### Truth tables and logical equivalence

A tautology is true in every row, a contradiction in none. Statements are logically equivalent ($\equiv$) when their columns agree in every row.

| Law | Equivalence |
|---|---|
| Double negation | $\neg\neg P \equiv P$ |
| De Morgan | $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$, $\ \neg(P \vee Q) \equiv \neg P \wedge \neg Q$ |
| Distributive | $P \wedge (Q \vee R) \equiv (P \wedge Q) \vee (P \wedge R)$, $\ P \vee (Q \wedge R) \equiv (P \vee Q) \wedge (P \vee R)$ |
| Conditional as "or" | $P \Rightarrow Q \equiv \neg P \vee Q$ |
| Contrapositive | $P \Rightarrow Q \equiv \neg Q \Rightarrow \neg P$ |
| Negated conditional | $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$ |
| Absorption | $P \vee (P \wedge Q) \equiv P$, $\ P \wedge (P \vee Q) \equiv P$ |
| Exportation | $(P \wedge Q) \Rightarrow R \equiv P \Rightarrow (Q \Rightarrow R)$ |

- To prove an equivalence, use a table ($2^n$ rows, innermost columns first) or a chain of laws with the name of each law beside each step. To disprove one, give one row where they differ.
- To test for a tautology without a table, try to make it false and look for a contradiction.
- A statement is satisfiable if some row makes it true. Checking all rows takes $2^n$ steps, and no fast method for every formula is known (SAT).

Main mistakes: pushing a $\neg$ through a bracket without flipping $\wedge$ and $\vee$; treating $\Rightarrow$ as commutative or associative; confusing $\equiv$ with $\Leftrightarrow$.

### Quantifiers

$\forall x \in D,\ P(x)$ is true when $P$ holds for every element of $D$. $\exists x \in D,\ P(x)$ is true when it holds for at least one. The domain matters: $\forall x,\ x^2 \ge x$ is true on $\mathbb{N}$ and false on $\mathbb{R}$.

| To show | Do this |
|---|---|
| $\forall x\,P(x)$ true | "Let $x$ be arbitrary", then prove $P(x)$ |
| $\exists x\,P(x)$ true | Name one $x$ and check it |
| $\forall x\,P(x)$ false | One counterexample |
| $\exists x\,P(x)$ false | Show $P$ fails for an arbitrary $x$ |

- Restricted $\forall$ pairs with $\Rightarrow$, restricted $\exists$ pairs with $\wedge$.
- In $\forall x\,\exists y$ the $y$ may depend on $x$. In $\exists y\,\forall x$ it can't. The second implies the first, and the first doesn't imply the second.
- Same-kind quantifiers swap freely. Over an empty domain, $\forall$ is true and $\exists$ is false.
- Code: `all(...)` is $\forall$ and `any(...)` is $\exists$.

Main mistakes: proving a "for all" by examples; disproving an "exists" by one failure; $\exists x\,(P \Rightarrow Q)$ for "some $P$ is $Q$"; swapping $\forall \exists$ into $\exists \forall$.

### Negation and translating English

| Statement | Negation |
|---|---|
| $P \wedge Q$ | $\neg P \vee \neg Q$ |
| $P \vee Q$ | $\neg P \wedge \neg Q$ |
| $P \Rightarrow Q$ | $P \wedge \neg Q$ |
| $\forall x\,P(x)$ | $\exists x\,\neg P(x)$ |
| $\exists x\,P(x)$ | $\forall x\,\neg P(x)$ |
| $\forall x\,(P(x) \Rightarrow Q(x))$ | $\exists x\,(P(x) \wedge \neg Q(x))$ |

- To negate a long statement, put $\neg$ in front and push it in one layer at a time. Quantifiers flip, order and domain stay, an arrow becomes "and", and the last comparison flips. Test the result on an example.
- Limit statements negate this way: $\forall \varepsilon\,\exists \delta\,\forall x\,(\dots)$ becomes $\exists \varepsilon\,\forall \delta\,\exists x\,(\dots \wedge \text{error} \ge \varepsilon)$.
- English: "all, every, each" is $\forall$ with $\Rightarrow$; "some, there is" is $\exists$ with $\wedge$; "no $A$ is $B$" is $\forall x\,(A \Rightarrow \neg B)$; "only $A$'s are $B$'s" is $\forall x\,(B \Rightarrow A)$.

Main mistakes: "not all" versus "all not" (the negation of "all pass" is "some fail", not "none pass"); negating only the conclusion of a conditional; flipping only one quantifier; "any" (it means "every" in a claim and "some" after a negation or an "if"); negating $x < 3$ as $x > 3$.

### Sets and set operations

| Operation | Meaning | Logic |
|---|---|---|
| $A \cup B$ | in $A$ or in $B$ (or both) | $\vee$ |
| $A \cap B$ | in both | $\wedge$ |
| $A \setminus B$ | in $A$ and not in $B$ | $\wedge \neg$ |
| $A^c$ | in $U$ and not in $A$ | $\neg$ |
| $A \subseteq B$ | every element of $A$ is in $B$ | $\Rightarrow$ |
| $A = B$ | $A \subseteq B$ and $B \subseteq A$ | $\Leftrightarrow$ |

- Counting: $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$. A set with $n$ elements has $2^n$ subsets, and $\lvert A \times B \rvert = \lvert A \rvert \cdot \lvert B \rvert$.
- $\mathcal{P}(A)$ is the set of all subsets of $A$ (it contains $\emptyset$ and $A$). $A \times B$ is the set of ordered pairs $(a, b)$, and $(a, b) = (c, d)$ means $a = c$ and $b = d$.
- Set identities mirror the logic laws: De Morgan, $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$; distributive laws; $A \setminus B = A \cap B^c$; $A \subseteq B \iff B^c \subseteq A^c$.
- To prove an identity, take an arbitrary $x$ and chain equivalences of the form $x \in \dots \iff \dots$, naming each logic law. A Venn diagram or a small example finds the answer but is not a proof.
- Code: `|`, `&`, `-`, `^`, `<=`; a complement is `U - A`; a set of sets uses `frozenset`.

Main mistakes: $\in$ versus $\subseteq$ ($\{1\} \in \{\{1\}, 2\}$ is true, $1 \in \{\{1\}, 2\}$ is false); $\emptyset$ versus $\{\emptyset\}$; $\lvert \mathcal{P}(A) \rvert = 2n$ instead of $2^n$; a complement with no universe; treating $A \setminus B$ or $A \times B$ as symmetric.
