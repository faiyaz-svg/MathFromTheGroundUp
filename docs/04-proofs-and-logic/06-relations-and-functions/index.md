# Relations and functions

Relations as sets of ordered pairs, the three kinds that matter (equivalence relations, partial orders, functions), the properties of functions, and how to compare the sizes of infinite sets.

1. [Relations and their properties](01-relations-and-their-properties.md)
2. [Equivalence relations and partitions](02-equivalence-relations-and-partitions.md)
3. [Partial orders](03-partial-orders.md)
4. [Functions and well-definedness](04-functions-and-well-definedness.md)
5. [Injective, surjective and bijective](05-injective-surjective-bijective.md)
6. [Cardinality and countability](06-cardinality-and-countability.md)

## Cheat sheet

### Relations and their properties

A relation on $A$ is a subset $R \subseteq A \times A$, and $a \mathrel{R} b$ means $(a, b) \in R$. It can be shown as a list, a digraph (arrow from $a$ to $b$) or a 0-1 matrix. The converse is $R^{-1} = \{(b, a) : (a, b) \in R\}$.

| Property | Definition | Prove by starting with | Disprove with |
|---|---|---|---|
| reflexive | $a \mathrel{R} a$ for all $a$ | "Let $a \in A$" | one $a$ with $a \not\mathrel{R} a$ |
| symmetric | $a \mathrel{R} b \Rightarrow b \mathrel{R} a$ | "Suppose $a \mathrel{R} b$" | one pair with no return |
| antisymmetric | $a \mathrel{R} b \wedge b \mathrel{R} a \Rightarrow a = b$ | "Suppose both" | two different elements related both ways |
| transitive | $a \mathrel{R} b \wedge b \mathrel{R} c \Rightarrow a \mathrel{R} c$ | "Suppose both" | a chain with no shortcut |

- Irreflexive means no loops, which is stronger than "not reflexive".
- Counts on $n$ elements: $2^{n^2}$ relations, $2^{n^2 - n}$ reflexive, $2^{n(n+1)/2}$ symmetric. For $n = 3$: 512, 64, 64, and also 216 antisymmetric and 171 transitive.
- Digraph test: loops, return arrows, two-way arrows between different vertices, shortcuts for two-step paths.

Main mistakes:

- Treating antisymmetric as "not symmetric". Equality is both, and a one-way arrow plus a two-way pair makes it neither.
- Proving a property from a few examples, or starting a proof with the conclusion.
- Forgetting that the set matters: divisibility is antisymmetric on $\mathbb{Z}^+$ and not on $\mathbb{Z}$ ($2 \mid -2$ and $-2 \mid 2$).
- Claiming symmetric and transitive give reflexive. That needs every element to be related to something.

### Equivalence relations and partitions

An equivalence relation is reflexive, symmetric and transitive, written $a \sim b$. The class of $a$ is $[a] = \{x : x \sim a\}$.

- $[a] = [b]$ exactly when $a \sim b$. Two classes are equal or disjoint. The classes form a partition: non-empty blocks, no overlap, covering $A$.
- Conversely, "in the same block" is an equivalence relation, so equivalence relations and partitions on $A$ are the same thing. The numbers of them for $1, 2, \dots, 6$ elements are 1, 2, 5, 15, 52, 203.
- A rule "$f(a) = f(b)$" is an equivalence relation for free (the kernel of $f$), and the classes are the preimages of single outputs.
- Congruence mod $n$ has exactly $n$ classes $[0], \dots, [n-1]$, and $a$ is in $[r]$ where $r$ is its remainder. So $-7 \in [2]$ mod 3.
- A rational number is a class of pairs $(a, b)$, $b \ne 0$, under $ad = bc$. Transitivity needs $d \ne 0$ to cancel.

Main mistakes:

- Writing $[a] = a$, or concluding $a = b$ from $[a] = [b]$. The class $[1] = [4]$ mod 3.
- Calling overlapping sets a partition, or leaving an element out.
- Using "near" ($\lvert x - y \rvert < 1$) as an equivalence relation. It fails transitivity.

### Partial orders

A partial order $\preceq$ is reflexive, antisymmetric and transitive. A strict order $\prec$ is irreflexive and transitive, and $a \prec b$ means $a \preceq b$ and $a \ne b$. Total means every two elements are comparable.

| Order | On | Total |
|---|---|---|
| $\le$ | $\mathbb{R}$ | yes |
| divides | $\mathbb{Z}^+$ | no ($2$, $3$ incomparable) |
| $\subseteq$ | $\mathcal{P}(S)$ | no, if $\lvert S \rvert \ge 2$ |
| lexicographic | strings, pairs | yes |

- Hasse diagram: draw only the covering pairs, upward. $a \preceq b$ means there is a path up from $a$ to $b$.
- Minimal: nothing strictly below. Least: below everything. A least element is unique and minimal, and a minimal element need not be least ($2$ and $3$ in $\{2, 3, 4, 6\}$).
- Every non-empty finite poset has a minimal element. Every finite poset has a linear extension: remove a minimal element, repeat. This is topological sorting.
- Chain: all pairs comparable. Antichain: none comparable.

Main mistakes:

- Reading "minimal" as "smallest", or "incomparable" as "unrelated in a way that rules out order".
- Reading a Hasse diagram as direct lines only. Follow paths.
- Calling divisibility on $\mathbb{Z}$ a partial order.

### Functions and well-definedness

A function $f \colon A \to B$ is a subset of $A \times B$ in which every $a \in A$ has exactly one partner. Prove existence (some output) and uniqueness (one output). Equal functions have the same domain, the same codomain and the same values.

- Image $f(S) = \{f(x) : x \in S\}$ and preimage $f^{-1}(T) = \{x : f(x) \in T\}$ (defined for every function). Preimages respect $\cup$, $\cap$ and complements. Images respect $\cup$ and only $f(S \cap S') \subseteq f(S) \cap f(S')$.
- $f(S) \subseteq T$ exactly when $S \subseteq f^{-1}(T)$.
- Composition $g \circ f$ is a function, associative, with $\text{id}$ as the neutral element, and not commutative.
- A rule on classes through a representative is well defined when $a \sim a'$ gives equal outputs. Test it with two names ($\frac{1}{2}$ and $\frac{2}{4}$, or $a$ and $a + n$).
- Addition and multiplication mod $n$ are well defined: $a' = a + nj$ and $b' = b + nk$ give $a'b' - ab = n(ak + bj + njk)$.
- A partial function has at most one output per input. Make it total by adding an "undefined" value.
- There are $\lvert B \rvert^{\lvert A \rvert}$ functions from $A$ to $B$.

Main mistakes:

- Writing $f(a/b) = a + b$ on rationals: $\frac{1}{2}$ gives 3 and $\frac{2}{4}$ gives 6.
- Overlapping cases in a piecewise rule ($f(0)$ defined twice).
- Reading $f^{-1}(T)$ as needing an inverse function.
- Mixing up $f(S)$ (a set) with $f(x)$ (an element).

### Injective, surjective and bijective

| Property | Definition | Proof template |
|---|---|---|
| injective | $f(a) = f(a') \Rightarrow a = a'$ | "Suppose $f(a) = f(a')$ ... so $a = a'$" |
| surjective | every $b \in B$ has an $a$ with $f(a) = b$ | "Let $b \in B$. Solve $f(a) = b$; check $a \in A$ and $f(a) = b$" |
| bijective | both | prove both; the solved $a$ is $f^{-1}(b)$ |

- Disprove injective with two inputs, one output. Disprove surjective with one output that has no input, and say why.
- Composition preserves each property. If $g \circ f$ is injective, $f$ is. If $g \circ f$ is surjective, $g$ is.
- $f$ has an inverse exactly when it is bijective, and the inverse is unique.
- Finite sets of equal size: injective, surjective and bijective are equivalent. Pigeonhole: if $\lvert A \rvert > \lvert B \rvert$, no injection.
- Counts for $m \to n$: $n^m$ functions, $n(n-1)\cdots(n-m+1)$ injective, $n!$ bijections when $m = n$. For $4 \to 3$ there are 81 functions and 36 surjections.
- A hash function from a large set to a small one is never injective, so collisions are unavoidable.

Main mistakes:

- Starting an injectivity proof with "suppose $a = a'$". That is true for every function.
- Solving $f(a) = b$ and not checking that $a$ is in the domain.
- Judging a function from a few values.
- Forgetting that the codomain is part of the question: $x^2$ is onto $[0, \infty)$ and not onto $\mathbb{R}$.

### Cardinality and countability

Sets $A$ and $B$ have the same cardinality when a bijection $A \to B$ exists. This is an equivalence relation. $\lvert A \rvert \le \lvert B \rvert$ means an injection exists.

- Countable means finite or the same size as $\mathbb{N}$, that is, it can be listed with every element at a finite position.
- Countably infinite: $\mathbb{N}$, $\mathbb{Z}$ (list $0, -1, 1, -2, 2, \dots$), the even numbers, $\mathbb{N} \times \mathbb{N}$ (pairing $\pi(i, j) = \frac{(i+j)(i+j+1)}{2} + j$), $\mathbb{Q}$ (zigzag, skipping fractions not in lowest terms), the finite binary strings (position of a string of length $L$ and value $v$ is $2^L - 1 + v$).
- To show countable: list it, or inject it into a countable set. Subsets of countable sets are countable. A surjection from $\mathbb{N}$ makes the target countable.
- Cantor's diagonal argument: for any list of infinite binary sequences, flip the diagonal, $d_n = 1 - s^{(n)}_n$. The result is on no row, so the set of such sequences is uncountable. The same argument gives $\mathbb{R}$ uncountable (use digits 4 and 5).
- Cantor's theorem: no function $A \to \mathcal{P}(A)$ is onto, because $D = \{a : a \notin f(a)\}$ is missed. So $\lvert A \rvert < \lvert \mathcal{P}(A) \rvert$.
- Programs are finite strings, so countably many. Decision problems are subsets of $\Sigma^*$, so uncountably many. Some problems have no program.

Main mistakes:

- Arguing from "part of" to "smaller" for infinite sets. $\mathbb{N}$ and the even numbers are the same size.
- Thinking that adding the diagonal sequence to the list completes it. The new list has a new diagonal.
- Building the diagonal real number from digits that allow a double expansion ($0.4999\ldots = 0.5000\ldots$).
- Reading "countable" as "has an end", or "uncountable" as "very large".
