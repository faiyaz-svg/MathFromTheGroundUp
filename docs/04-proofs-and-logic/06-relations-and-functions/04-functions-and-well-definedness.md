# Functions and well-definedness

After this lesson you can state a function as a relation with exactly one output for each input, prove that a set of pairs is a function, compute and prove facts about images and preimages, compose functions, and check that a rule defined through a representative is well defined.

Before this: [what is a function](../../03-high-school/03-functions/01-what-is-a-function.md) (domain, codomain, range, graph), [composition and inverse functions](../../03-high-school/03-functions/05-composition-and-inverse-functions.md), [relations and their properties](01-relations-and-their-properties.md), [equivalence relations and partitions](02-equivalence-relations-and-partitions.md) and [existence and uniqueness proofs](../04-more-proof-methods/02-existence-and-uniqueness-proofs.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Is $\{(1, a), (2, b), (2, c), (3, a)\}$ a function from $\{1, 2, 3\}$ to $\{a, b, c\}$? Is $\{(1, a), (3, b)\}$?
2. Let $f(x) = x^2$ on $\mathbb{Z}$. Find $f(\{-2, 0, 3\})$ and $f^{-1}(\{4, 5\})$.
3. Someone defines $g \colon \mathbb{Q} \to \mathbb{Z}$ by $g\left(\frac{a}{b}\right) = a$. Why is that not a function?

<details class="solution" markdown>
<summary>Answers</summary>

1. Neither. In the first, the input 2 has two outputs, $b$ and $c$. In the second, the input 2 has no output.
2. The image is $\{4, 0, 9\}$. The preimage is $\{-2, 2\}$, because $f(x) = 4$ for $x = \pm 2$ and $f(x) = 5$ for no integer $x$.
3. The same rational number has many names: $\frac{1}{2} = \frac{2}{4}$, and the rule sends it to $1$ by the first name and to $2$ by the second. The output is not determined by the number, only by how it is written.

</details>

## The idea

The high school definition of a function says that it assigns to each input exactly one output. That is a good working definition, and it hides a word, "assigns", that is not defined in set theory. A set theorist asks what an assignment is, and the answer from [relations and their properties](01-relations-and-their-properties.md) is already in hand: an assignment is a set of ordered pairs. The graph of a function is a subset of $A \times B$, and the lesson says that a function is its graph. The "exactly one output" becomes a condition on that subset.

This brings a payoff. Once a function is a set of pairs, a statement such as "this rule defines a function" is a statement we can prove, with two parts: every input has an output, and no input has two. Most rules that we write down satisfy both at a glance, as in $x \mapsto x^2$. The rules that don't are the interesting ones, and they fall into a common family. In that family, the input is something with several names, such as a fraction ($\frac{1}{2}$ or $\frac{2}{4}$), a remainder class ($[1]_6$ or $[7]_6$) or a set written as a list in different orders, and the rule computes the output from one of the names. The rule defines a function only if the output doesn't depend on which name was chosen. Checking that is called checking that the function is well defined, and it is a proof that is easy to forget and easy to get wrong.

The same check explains why modular arithmetic is legitimate, why a program that hashes the "same" value two ways is a bug, and why defining a function on a quotient set needs more than a formula.

## Definitions

### Functions as sets of pairs

Let $A$ and $B$ be sets. A **function** from $A$ to $B$, written $f \colon A \to B$, is a relation $f \subseteq A \times B$ such that for every $a \in A$ there is exactly one $b \in B$ with $(a, b) \in f$. In symbols: $\forall a \in A\ \exists! b \in B\ (a, b) \in f$. We write $f(a) = b$ for $(a, b) \in f$.

In plain words, a function is a relation in which every input has exactly one output. The two halves are named: **existence** (every $a \in A$ has at least one partner in $B$) and **uniqueness** (no $a \in A$ has two different partners). The set $A$ is the **domain**, the set $B$ is the **codomain**, and the **range** (or image) of $f$ is the set of outputs that occur, $\{f(a) : a \in A\}$. This matches the high school lesson [what is a function](../../03-high-school/03-functions/01-what-is-a-function.md), and the vertical line test is the uniqueness half drawn as a picture.

Two functions $f \colon A \to B$ and $g \colon C \to D$ are **equal** when $A = C$, $B = D$ and $f(x) = g(x)$ for every $x \in A$. This is the same definition as in the high school lesson, which keeps the codomain as part of the function. As sets of pairs, the graphs of $f$ and $g$ are then the same set. In plain words, equal functions are declared on the same sets and do the same thing to every input.

### Image and preimage of a set

Let $f \colon A \to B$, $S \subseteq A$ and $T \subseteq B$. The **image** of $S$ is the set of outputs from inputs in $S$, and the **preimage** of $T$ is the set of inputs whose output lands in $T$:

$$
f(S) = \{ f(x) : x \in S \}, \qquad f^{-1}(T) = \{ x \in A : f(x) \in T \}.
$$

In plain words, the image pushes a set of inputs forward, and the preimage pulls a set of outputs back. For a single output $y$, we write $f^{-1}(\{y\})$ for the set of all inputs that map to $y$. The preimage is defined for every function, even when $f$ has no inverse function. The notation is unfortunate, because $f^{-1}(T)$ here is a set built by a rule, and not the inverse function applied to $T$. If $f$ happens to have an inverse function $f^{-1}$, then $f^{-1}(T)$ is the set of its values at the elements of $T$, so the two meanings agree.

For $f(x) = x^2$ on $\mathbb{R}$, $f([-1, 2]) = [0, 4]$ and $f^{-1}(\{4\}) = \{-2, 2\}$ and $f^{-1}(\{-1\}) = \emptyset$.

### Identity and composition

The **identity function** on $A$ is $\text{id}_A \colon A \to A$ with $\text{id}_A(x) = x$. For $f \colon A \to B$ and $g \colon B \to C$, the **composition** $g \circ f \colon A \to C$ is the relation

$$
g \circ f = \{ (a, c) : \text{there is } b \in B \text{ with } (a, b) \in f \text{ and } (b, c) \in g \}.
$$

In plain words, $(g \circ f)(a)$ is $g(f(a))$: first $f$, then $g$. The codomain of $f$ must be the domain of $g$ (or sit inside it). This is the composition of [composition and inverse functions](../../03-high-school/03-functions/05-composition-and-inverse-functions.md), now defined for relations between arbitrary sets.

### Well-defined rules

Suppose the elements of a set $X$ are classes $[a]$ of an equivalence relation $\sim$ on a set $A$, and a rule $F$ defines $F([a])$ by a formula in the representative $a$. The rule is **well defined** when the output doesn't depend on the representative: if $a \sim a'$, then the formula gives the same output at $a$ and at $a'$, so $F([a]) = F([a'])$.

In plain words, a rule on classes is a rule on names, and it makes sense only if two names for the same class always give the same answer. If it fails, there are two different outputs for one input, and uniqueness, the second half of the definition of a function, is violated. "Well defined" is therefore the uniqueness half of "is a function", checked for rules that go through a choice.

## How to do it

### Proving that a set of pairs is a function

1. Name the sets $A$ and $B$, and the set of pairs $f \subseteq A \times B$ (or the rule that gives it).
2. Check that every pair has its first entry in $A$ and its second in $B$. A rule whose outputs can leave $B$ doesn't give a function into $B$.
3. Existence: let $a \in A$ and show that some $b \in B$ has $(a, b) \in f$. For a rule, say what $b$ is and check that it lies in $B$.
4. Uniqueness: suppose $(a, b) \in f$ and $(a, b') \in f$, and show $b = b'$.
5. Check on a small example, and remember that existence fails when the rule can break at some input (division by $0$, a square root of a negative number), and uniqueness fails when the rule involves a choice.

### Proving that two functions are equal

1. Check that the domains match, and that the codomains match.
2. Let $x$ be an arbitrary element of the domain and show $f(x) = g(x)$.
3. To show that they are not equal, find one $x$ with $f(x) \ne g(x)$, or note that the sets differ.

### Checking that a rule on classes is well defined

1. Say what the classes are and what the representative is.
2. Take two representatives of the same class: $a$ and $a'$ with $a \sim a'$, which means (by definition of $\sim$) that some equation or divisibility holds.
3. Compute the rule at both and show the outputs are equal as classes. This is where the proof is.
4. If the check fails, give two names of one class with different outputs. One pair is a complete disproof.

### Two theorems about images and preimages

*Theorem 1.* Let $f \colon A \to B$, let $S, S' \subseteq A$ and let $U, V \subseteq B$. Then (i) $f(S \cup S') = f(S) \cup f(S')$; (ii) $f(S \cap S') \subseteq f(S) \cap f(S')$, and equality can fail; (iii) $f^{-1}(U \cap V) = f^{-1}(U) \cap f^{-1}(V)$.

What we know: the definitions of image and preimage, and the method of [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md). What we want: two set equalities, one inclusion with a counterexample. The plan: for (i), prove the two inclusions through the description "$y \in f(S)$ iff $y = f(x)$ for some $x \in S$". For (iii), a chain of equivalences. For (ii), prove the inclusion, then find an example where it is strict.

*Proof.* (i) Let $y \in f(S \cup S')$. Then $y = f(x)$ for some $x \in S \cup S'$. If $x \in S$, then $y \in f(S)$, and if $x \in S'$, then $y \in f(S')$. In both cases $y \in f(S) \cup f(S')$. Conversely, let $y \in f(S) \cup f(S')$. If $y \in f(S)$, then $y = f(x)$ for some $x \in S \subseteq S \cup S'$, so $y \in f(S \cup S')$, and the case $y \in f(S')$ is the same.

(ii) Let $y \in f(S \cap S')$, so $y = f(x)$ for some $x \in S \cap S'$. Then $x \in S$, so $y \in f(S)$, and $x \in S'$, so $y \in f(S')$. Hence $y \in f(S) \cap f(S')$. For the failure of equality, take $f \colon \mathbb{Z} \to \mathbb{Z}$ with $f(x) = x^2$, $S = \{-1\}$ and $S' = \{1\}$. Then $S \cap S' = \emptyset$, so $f(S \cap S') = \emptyset$, but $f(S) \cap f(S') = \{1\} \cap \{1\} = \{1\}$.

(iii) For $x \in A$,

$$
\begin{aligned}
x \in f^{-1}(U \cap V) &\iff f(x) \in U \cap V && \text{definition of preimage} \\
&\iff f(x) \in U \text{ and } f(x) \in V && \text{definition of intersection} \\
&\iff x \in f^{-1}(U) \text{ and } x \in f^{-1}(V) && \text{definition of preimage} \\
&\iff x \in f^{-1}(U) \cap f^{-1}(V) && \text{definition of intersection.}
\end{aligned}
$$

Every step is an equivalence, so the two sets are equal. $\blacksquare$

Look back: preimages behave better than images. A preimage respects unions, intersections and complements, while an image respects unions only. In (ii) the two sets differ because the two different inputs $-1$ and $1$ meet at one output. Whether images respect intersections is exactly the question of whether the function is injective, which is Practice 7 and the next lesson. Check (iii) with $f(x) = x^2$ on $\{-3, \dots, 3\}$, $U = \{1, 4, 9\}$ and $V = \{4, 5\}$: $U \cap V = \{4\}$ has preimage $\{-2, 2\}$, and $f^{-1}(U) = \{-3, -2, -1, 1, 2, 3\}$ and $f^{-1}(V) = \{-2, 2\}$ intersect in $\{-2, 2\}$.

### Composition and the identity

*Theorem 2.* If $f \colon A \to B$ and $g \colon B \to C$ are functions, then $g \circ f$ is a function from $A$ to $C$ with $(g \circ f)(a) = g(f(a))$. Also, composition is associative, $(h \circ g) \circ f = h \circ (g \circ f)$, and $f \circ \text{id}_A = f = \text{id}_B \circ f$.

What we want: existence and uniqueness for $g \circ f$, and two equalities of functions. The plan: use $f$ and $g$ being functions at each step, and for the equalities, compare values at an arbitrary input.

*Proof.* Existence: let $a \in A$. Since $f$ is a function, $(a, f(a)) \in f$ with $f(a) \in B$. Since $g$ is a function, $(f(a), g(f(a))) \in g$. So $(a, g(f(a))) \in g \circ f$. Uniqueness: suppose $(a, c) \in g \circ f$ and $(a, c') \in g \circ f$. Then there are $b$ and $b'$ with $(a, b), (a, b') \in f$ and $(b, c), (b', c') \in g$. Uniqueness for $f$ gives $b = b'$, and then uniqueness for $g$ gives $c = c'$. So $g \circ f$ is a function, and its value at $a$ is $g(f(a))$.

For associativity, take $h \colon C \to D$. Both $(h \circ g) \circ f$ and $h \circ (g \circ f)$ have domain $A$ and codomain $D$. For $a \in A$, $((h \circ g) \circ f)(a) = (h \circ g)(f(a)) = h(g(f(a)))$, and $(h \circ (g \circ f))(a) = h((g \circ f)(a)) = h(g(f(a)))$. The values agree. For the identity, $(f \circ \text{id}_A)(a) = f(\text{id}_A(a)) = f(a)$ and $(\text{id}_B \circ f)(a) = \text{id}_B(f(a)) = f(a)$. $\blacksquare$

Look back: this proof is the first time that "is a function" had two halves to prove, and each half used the same half of the hypotheses. Check with $f(x) = x + 1$ and $g(x) = 2x$ on $\mathbb{Z}$: $(g \circ f)(5) = g(6) = 12$ and $(f \circ g)(5) = f(10) = 11$. Composition is associative and not commutative.

### Well-definedness of arithmetic modulo $n$

The classes of congruence modulo $n$ are $[0], \dots, [n-1]$ (previous lesson). We want to add them by $[a] + [b] = [a + b]$. This rule is written with representatives, so it needs a check.

*Theorem 3.* Let $n$ be a positive integer. If $a \equiv a'$ and $b \equiv b' \pmod{n}$, then $a + b \equiv a' + b'$ and $ab \equiv a'b' \pmod{n}$. So $[a] + [b] = [a + b]$ and $[a] \cdot [b] = [ab]$ are well-defined functions $\mathbb{Z}_n \times \mathbb{Z}_n \to \mathbb{Z}_n$.

What we know: $a \equiv a'$ means $a' = a + nj$ for some integer $j$, and $b' = b + nk$ for some integer $k$. What we want: $n \mid (a' + b') - (a + b)$ and $n \mid a'b' - ab$. The plan: substitute and factor out $n$.

*Proof.* For the sum,

$$
(a' + b') - (a + b) = (a + nj + b + nk) - (a + b) = n(j + k),
$$

which is a multiple of $n$. For the product,

$$
a'b' - ab = (a + nj)(b + nk) - ab = n(ak + bj + njk),
$$

and $ak + bj + njk$ is an integer. So $n$ divides both differences. By the definition of well defined, the class of $a + b$ and the class of $ab$ depend only on the classes of $a$ and $b$. $\blacksquare$

Look back: the proof is an algebra identity and no more, and it is the reason that remainders can be reduced at any stage of a calculation. Check with $n = 7$: $[3] + [5] = [8] = [1]$, and replacing $3$ by $10$ and $5$ by $-2$ gives $10 + (-2) = 8$, in the same class $[1]$.

### When it fails

*Example of failure.* Define $f \colon \mathbb{Q} \to \mathbb{Z}$ by $f\left(\frac{a}{b}\right) = a + b$. The names $\frac{1}{2}$ and $\frac{2}{4}$ are two representatives of the same rational number, since $1 \cdot 4 = 2 \cdot 2$. The rule gives $1 + 2 = 3$ for the first and $2 + 4 = 6$ for the second. One input has two outputs, so the rule doesn't define a function. A rule that does work is $\frac{a}{b} \mapsto \frac{a^2}{b^2}$: if $ad = bc$ then $(ad)^2 = (bc)^2$, which says $\frac{a^2}{b^2} = \frac{c^2}{d^2}$ as fractions, so the value depends only on the rational number (Example 3).

A map between classes can fail for a different reason. The rule $[a]_6 \mapsto [a]_4$ is not well defined, since $[0]_6 = [6]_6$ while $[0]_4 \ne [6]_4$. The rule $[a]_6 \mapsto [a]_3$ is well defined, because $6 \mid a - a'$ gives $3 \mid a - a'$.

### Partial functions

A **partial function** from $A$ to $B$ is a relation in which each $a \in A$ has at most one output. It is a function on the subset of $A$ where it is defined. In plain words, it satisfies uniqueness and may fail existence. Division $(a, b) \mapsto \frac{a}{b}$ is a partial function on $\mathbb{R} \times \mathbb{R}$ with no output when $b = 0$, and the square root is a partial function on $\mathbb{R}$. In code, a partial function either raises an exception or returns a special value such as `None` when the input is outside its domain of definition. The standard way back to a total function is to enlarge the codomain with one extra element, "undefined", which is the idea behind `Optional` in Python and `Maybe` in Haskell.

## Worked examples

<div class="example" markdown>

### Example 1: a relation that is not a function, and one that is

Let $R = \{(x, y) \in \mathbb{R} \times \mathbb{R} : x = y^2\}$. Is $R$ a function from $\mathbb{R}$ to $\mathbb{R}$? Then show that $R' = \{(x, y) \in [0, \infty) \times [0, \infty) : x = y^2\}$ is a function from $[0, \infty)$ to $[0, \infty)$.

Step 1 and 2: the sets are given, and every pair in $R$ is in $\mathbb{R} \times \mathbb{R}$ by definition.

Step 3, existence for $R$: take $x = -1$. We need $y$ with $-1 = y^2$, and no real number has a negative square. So $-1$ has no partner, and $R$ is not a function from $\mathbb{R}$. Step 4, uniqueness for $R$: take $x = 4$. Both $(4, 2)$ and $(4, -2)$ are in $R$, so $4$ has two partners. A single failure of either half is enough, and $R$ has both.

For $R'$, Step 3: let $x \ge 0$. Then $y = \sqrt{x}$ is a non-negative real number with $y^2 = x$, so $(x, y) \in R'$. Step 4: suppose $(x, y)$ and $(x, y')$ are in $R'$, so $y, y' \ge 0$ and $y^2 = x = y'^2$. Then $(y - y')(y + y') = y^2 - y'^2 = 0$, so $y = y'$ or $y + y' = 0$. In the second case, $y, y' \ge 0$ with sum $0$ forces $y = y' = 0$, and again $y = y'$. So the partner is unique, and $R'$ is the square root function.

Check: $R'$ has the pairs $(0, 0), (4, 2), (9, 3)$, and not $(4, -2)$. The difference between $R$ and $R'$ is that restricting the domain and the codomain removes the failures: the domain $[0, \infty)$ removes the negative $x$, and the codomain $[0, \infty)$ removes the negative root.

</div>

<div class="example" markdown>

### Example 2: image, preimage and the intersection warning

Let $f \colon \{-3, -2, \dots, 3\} \to \mathbb{Z}$ be $f(x) = x^2$. Find $f(\{-1, 0, 2\})$, $f^{-1}(\{1, 4, 5\})$ and $f^{-1}(\{-1\})$, and compare $f(S \cap S')$ with $f(S) \cap f(S')$ for $S = \{-2, 1\}$ and $S' = \{2, 3\}$.

The image: $f(-1) = 1$, $f(0) = 0$ and $f(2) = 4$, so $f(\{-1, 0, 2\}) = \{0, 1, 4\}$. The preimage of $\{1, 4, 5\}$: go through the domain and keep the $x$ with $x^2 \in \{1, 4, 5\}$. These are $x = \pm 1$ and $x = \pm 2$, and no integer has square $5$, so the preimage is $\{-2, -1, 1, 2\}$. The preimage of $\{-1\}$ is empty, since no square is negative.

For the intersection, $S \cap S' = \emptyset$, so $f(S \cap S') = \emptyset$. The images are $f(S) = \{4, 1\}$ and $f(S') = \{4, 9\}$, and their intersection is $\{4\}$. So $f(S \cap S') = \emptyset \subsetneq \{4\} = f(S) \cap f(S')$. The inclusion of Theorem 1(ii) is strict, because $-2 \in S$ and $2 \in S'$ both go to $4$.

Check: Python's set comprehension `{x for x in range(-3, 4) if x*x in {1, 4, 5}}` gives `{-2, -1, 1, 2}`, as the program in [In code](#in-code) shows.

</div>

<div class="example" markdown>

### Example 3: which rules on fractions are well defined

Decide whether each rule gives a function $\mathbb{Q} \to \mathbb{Q}$, writing a rational number as $\frac{a}{b}$ with $b \ne 0$. (a) $\frac{a}{b} \mapsto \frac{a}{b + 1}$. (b) $\frac{a}{b} \mapsto \frac{a^2}{b^2}$. (c) $\frac{a}{b} \mapsto \frac{a + b}{b}$.

Step 1 and 2: two names of one rational number are $\frac{a}{b}$ and $\frac{c}{d}$ with $ad = bc$. We compute the rule on both names.

(a) Take $\frac{1}{2}$ and $\frac{2}{4}$. The rule gives $\frac{1}{3}$ and $\frac{2}{5}$, which are different. So (a) is not well defined, and this one pair is the whole disproof.

(b) Suppose $ad = bc$. Then $(ad)^2 = (bc)^2$, so $a^2 d^2 = b^2 c^2$, and that says $\frac{a^2}{b^2} = \frac{c^2}{d^2}$. The two names give equal outputs. So (b) is well defined. (It is the squaring function in disguise.)

(c) Suppose $ad = bc$. We have $\frac{a + b}{b} = \frac{a}{b} + 1$ and $\frac{c + d}{d} = \frac{c}{d} + 1$. Since $\frac{a}{b} = \frac{c}{d}$, these are equal. So (c) is well defined. The rule is "add 1" written with a representative.

Check: with the names $\frac{1}{2}$ and $\frac{2}{4}$, rule (b) gives $\frac{1}{4}$ and $\frac{4}{16} = \frac{1}{4}$, and rule (c) gives $\frac{3}{2}$ and $\frac{6}{4} = \frac{3}{2}$. In both, the outputs agree.

</div>

<div class="example" markdown>

### Example 4: multiplication mod $n$ (finish it yourself)

Show that the rule $F([a]) = [3a]$ is a well-defined function from $\mathbb{Z}_5$ to $\mathbb{Z}_5$. (This is a special case of the product in Theorem 3, with one factor fixed at $3$, and it is worth doing by hand.)

Step 1: the classes are $[a]_5$, and the rule is written with the representative $a$. Step 2: take two representatives of one class, $a$ and $a'$ with $a \equiv a' \pmod{5}$, so $a' = a + 5j$ for some integer $j$. Step 3: compute the rule at $a'$:

$$
3a' = 3(a + 5j) = 3a + 15j.
$$

Now finish: show that $3a' \equiv 3a \pmod{5}$, so that $[3a'] = [3a]$.

<details class="solution" markdown>
<summary>Finish</summary>

$3a' - 3a = 15j = 5(3j)$, and $3j$ is an integer, so $5 \mid 3a' - 3a$. Hence $3a' \equiv 3a \pmod{5}$ and $[3a'] = [3a]$. The rule gives the same output for every representative, so $F$ is well defined.

Check: $[2]_5 = [7]_5$. The rule gives $[6]_5 = [1]_5$ at the representative $2$, and $[21]_5 = [1]_5$ at the representative $7$. Both are $[1]_5$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a rule that gives an output from a representative is not automatically a function on classes. Writing $F([a]) = a$ looks harmless, and it isn't: the class $[1]_6 = [7]_6$ would go to $1$ and to $7$. Always ask, "If I use a different name for the same input, do I get the same answer?"

</div>

<div class="warning" markdown>

Watch out: overlapping cases in a piecewise definition can break uniqueness. The rule $f(x) = x + 1$ for $x \ge 0$ and $f(x) = x^2$ for $x \le 0$ gives two values at $x = 0$, namely $1$ and $0$, so it isn't a function. The cases must agree wherever they overlap, or they must not overlap. The cases must also cover the domain: if they stop short, existence fails.

</div>

<div class="warning" markdown>

Watch out: $f^{-1}(T)$ for a set $T$ doesn't need an inverse function. For $f(x) = x^2$, $f^{-1}(\{4\}) = \{-2, 2\}$ is a perfectly good set, although $f$ has no inverse function. Read $f^{-1}(T)$ as "the set of inputs that land in $T$". It is the preimage, and it always exists.

</div>

<div class="warning" markdown>

Watch out: $f(S)$ and $f(x)$ are different kinds of object. The expression $f(\{1\})$ is a set, namely $\{f(1)\}$, and $f(1)$ is an element. Mixing them up gives statements like $f(\{1\}) = f(1)$, which are false because the left side is a set and the right side is an element.

</div>

<div class="warning" markdown>

Watch out: the codomain is part of the function. The functions $x \mapsto x^2$ from $\mathbb{R}$ to $\mathbb{R}$ and from $\mathbb{R}$ to $[0, \infty)$ have the same graph and are different functions in this book, one of which is surjective ([injective, surjective and bijective](05-injective-surjective-bijective.md)). If a rule's outputs can leave the stated codomain, the rule is not a function into that codomain.

</div>

Some small cases. For any set $B$ there is exactly one function from $\emptyset$ to $B$, the empty set of pairs: existence is vacuously true because there is no $a$ to fail. There is no function from a non-empty set $A$ to $\emptyset$, because the first $a$ would need an output in the empty set. A function from a one-element set $\{a\}$ to $B$ is a choice of one element of $B$, so there are $\lvert B \rvert$ of them. And a function with domain $A$ and codomain $B$ can be counted: each of the $\lvert A \rvert$ inputs independently picks one of $\lvert B \rvert$ outputs, so there are $\lvert B \rvert^{\lvert A \rvert}$ functions. This explains why the set of functions from $A$ to $B$ is sometimes written $B^A$, and why $\lvert \mathcal{P}(A) \rvert = 2^{\lvert A \rvert}$ counts functions from $A$ to a two-element set.

## Tricks and shortcuts

When a rule is defined through a representative, test it on one pair of names before trying to prove it. Two names of the same class that give different outputs end the question in a minute. For fractions, use $\frac{1}{2}$ and $\frac{2}{4}$. For remainder classes, use $a$ and $a + n$.

If the rule on the class can be written as a function of something that is already the same for all representatives (the value of the fraction, the remainder), it is well defined for free. In Example 3, rule (c) is "add 1 to the rational number", written with a representative, and rule (b) is "square the rational number". A rule that uses the numerator and denominator separately, such as $a + b$, is the warning sign.

For images and preimages, prefer preimages in proofs. They commute with unions, intersections and complements, and a proof reduces to a chain of equivalences. Images need existence statements ("there is an $x$ with ..."), and the intersection case needs more care.

## In code

A function between finite sets is a dictionary, and the checks are loops. The program tests the three sets of pairs from the Quick check, computes images and preimages, shows that $a + b$ is not well defined on fractions while $[a]_6 \to [a]_3$ is and $[a]_6 \to [a]_4$ isn't, checks addition modulo 7 on many representatives, counts functions, and shows a partial function in code.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import product

def is_function(A, B, R):
    """R is a set of pairs. A function from A to B: every a in A has exactly one b with (a, b) in R."""
    in_range = all(a in A and b in B for (a, b) in R)
    return in_range and all(len([b for (x, b) in R if x == a]) == 1 for a in A)

A, B = {1, 2, 3}, {4, 5, 6}
print(is_function(A, B, {(1, 4), (2, 5), (3, 4)}))        # True
print(is_function(A, B, {(1, 4), (2, 5)}))                # False: 3 has no output
print(is_function(A, B, {(1, 4), (1, 5), (2, 5), (3, 6)}))# False: 1 has two outputs

def image(f, S):
    return {f(x) for x in S}

def preimage(f, domain, T):
    return {x for x in domain if f(x) in T}

f = lambda x: x * x
dom = range(-3, 4)
print(sorted(image(f, {-1, 0, 2})))                       # [0, 1, 4]
print(sorted(preimage(f, dom, {1, 4, 5})))                # [-2, -1, 1, 2]
print(image(f, {-1} & {1}), image(f, {-1}) & image(f, {1}))   # set() {1}

# well-definedness: the rule "send the fraction a/b to a + b" depends on the name
print(1 + 2, 2 + 4)                                       # 3 6   (1/2 and 2/4 are the same fraction)

# a map between classes defined through a representative: [a]_m -> [a]_k
def well_defined(m, k, window=range(-30, 31)):
    """Is [a]_m -> [a]_k well defined? Check that a = a' (mod m) forces a = a' (mod k) on a window."""
    return all((a - b) % k == 0 for a in window for b in window if (a - b) % m == 0)

print(well_defined(6, 3), well_defined(6, 4))             # True False

# addition mod n does not depend on the representatives
n = 7
ok = all((a + b) % n == ((a + 7 * j) + (b + 7 * k)) % n
         for a in range(7) for b in range(7) for j in range(-3, 4) for k in range(-3, 4))
print(ok)                                                 # True

# counting functions
print(len(list(product("ab", repeat=3))), len(list(product([1, 2, 3], repeat=2))))   # 8 9

# a partial function in code, and a total version with None
def safe_div(a, b):
    return a / b if b != 0 else None

print(safe_div(6, 3), safe_div(6, 0))                     # 2.0 None
table = {"A123": 81, "B456": 74}
print(table.get("A123"), table.get("Z999"))               # 81 None

# composition and the identity
compose = lambda g, f: (lambda x: g(f(x)))
identity = lambda x: x
inc, dbl = (lambda x: x + 1), (lambda x: 2 * x)
print(all(compose(identity, inc)(x) == inc(x) == compose(inc, identity)(x) for x in range(10)))   # True
print(compose(dbl, inc)(5), compose(inc, dbl)(5))         # 12 11
```

The function `is_function` is the definition, word for word: the first test is "all pairs lie in $A \times B$", and the second says that each $a$ has exactly one partner. The window test in `well_defined` checks a finite range of integers, and it supports the claims about $[a]_6 \to [a]_3$ and $[a]_6 \to [a]_4$ without proving the first. The second is settled by one counterexample, as in the text. A dictionary with `.get` is a partial function, and `None` is the extra "undefined" value that makes it total.

</details>

## FAQ

### Why define a function as a set of pairs?

Because it makes "this rule defines a function" something that can be proved, and it gives one definition that covers rules, tables, graphs and programs. A function in a program is a table in disguise, and the set of input-output pairs is all that a caller can observe. Two programs that give the same output on every input are the same function, which matches "equal functions have the same pairs".

### Does a function need a formula?

No. A table is a function, and so is a rule such as "send each integer to $1$ if it is prime and $0$ if not", or a lookup of a student ID. Many functions have no closed formula. What a function does need is exactly one output for each input in its domain, which is the whole definition.

### Why is well-definedness only an issue for classes?

It is an issue whenever the input has more than one description, and classes are the typical case. For a function on $\mathbb{R}$, the input $2$ has one name, so a formula in $x$ always gives one output. For a function on fractions, remainder classes, sets written as lists, or rational numbers written as decimals ($0.5$ and $0.4999\dots$), the same input has several descriptions, so the formula could disagree with itself.

### What if a rule works for the representatives I picked?

Then you have checked it on two representatives, and that isn't a proof. A well-definedness proof covers all representatives: it starts with an arbitrary pair of names for the same class. One bad pair is enough to show a rule fails, and no finite number of good pairs shows that it works. In the same way, a few agreeing values don't prove that two functions are equal.

## Practice

### Warm-up

1\. Which of these are functions from $\{a, b, c\}$ to $\{1, 2\}$? (a) $\{(a, 1), (b, 2), (c, 1)\}$ (b) $\{(a, 1), (b, 2)\}$ (c) $\{(a, 1), (a, 2), (b, 1), (c, 1)\}$ (d) $\{(a, 1), (b, 1), (c, 3)\}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) A function: each of $a$, $b$, $c$ starts exactly one pair, and the outputs are in $\{1, 2\}$.
- (b) Not a function: $c$ has no output (existence fails).
- (c) Not a function: $a$ has two outputs, $1$ and $2$ (uniqueness fails).
- (d) Not a function into $\{1, 2\}$: the output $3$ is not in the codomain. (It would be a function into $\{1, 2, 3\}$.)

Check (a): the three first entries are $a, b, c$, once each.

</details>

2\. Let $f \colon \{1, 2, 3, 4\} \to \mathbb{Z}$ be $f(n) = n^2 - 5n$. Find $f(\{1, 2\})$, $f^{-1}(\{-6\})$, $f^{-1}(\{-6, -4\})$ and $f^{-1}(\{0\})$.

<details class="solution" markdown>
<summary>Solution</summary>

The values are $f(1) = -4$, $f(2) = -6$, $f(3) = -6$ and $f(4) = -4$.

- $f(\{1, 2\}) = \{-4, -6\}$.
- $f^{-1}(\{-6\}) = \{2, 3\}$.
- $f^{-1}(\{-6, -4\}) = \{1, 2, 3, 4\}$, since every output is $-4$ or $-6$.
- $f^{-1}(\{0\}) = \emptyset$, since no input gives $0$ (the roots $0$ and $5$ are not in the domain).

Check: the preimages of $\{-6\}$ and $\{-4\}$ are $\{2, 3\}$ and $\{1, 4\}$, and they have no element in common and together give the domain.

</details>

3\. Decide whether $f = g$. (a) $f, g \colon \mathbb{Z} \to \mathbb{Z}$ with $f(n) = n^2 + n$ and $g(n) = n(n + 1)$. (b) $f \colon \mathbb{Z} \to \mathbb{Z}$ and $g \colon \mathbb{Z} \to \mathbb{R}$, both $n \mapsto n$. (c) $f, g \colon \mathbb{Z} \to \mathbb{Z}$ with $f(n) = (-1)^n$ and $g(n) = 1 - 2(n \bmod 2)$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Equal. The domains and codomains match, and $n^2 + n = n(n + 1)$ for every integer $n$ by the distributive law.
- (b) Not equal in this book. The rules and domains agree, and the codomains $\mathbb{Z}$ and $\mathbb{R}$ differ.
- (c) Equal. For even $n$, $(-1)^n = 1$ and $n \bmod 2 = 0$, so $g(n) = 1$. For odd $n$, $(-1)^n = -1$ and $n \bmod 2 = 1$, so $g(n) = -1$. Every integer is even or odd.

Check (c) at $n = 3$ and $n = 4$: $f(3) = -1 = g(3)$ and $f(4) = 1 = g(4)$.

</details>

### Standard

4\. Decide whether each rule gives a function $\mathbb{Q} \to \mathbb{Q}$, with a proof or a counterexample: (a) $\frac{a}{b} \mapsto a$ (as a rational number), (b) $\frac{a}{b} \mapsto \frac{a + b}{b}$, (c) $\frac{a}{b} \mapsto \frac{a}{b + 1}$.

<details class="solution" markdown>
<summary>Solution</summary>

Two names of one rational: $\frac{a}{b} = \frac{c}{d}$ means $ad = bc$.

- (a) Not well defined: $\frac{1}{2} = \frac{2}{4}$ and the rule gives $1$ and $2$.
- (b) Well defined. $\frac{a + b}{b} = \frac{a}{b} + 1$ and $\frac{c + d}{d} = \frac{c}{d} + 1$. If $ad = bc$ then $\frac{a}{b} = \frac{c}{d}$, so the two outputs are equal.
- (c) Not well defined: $\frac{1}{2} = \frac{2}{4}$, and the rule gives $\frac{1}{3}$ and $\frac{2}{5}$.

Check (b) with $\frac{1}{2}$ and $\frac{3}{6}$: the rule gives $\frac{3}{2}$ and $\frac{9}{6} = \frac{3}{2}$.

</details>

5\. Find the flaw: "Define $f \colon \mathbb{Z}_6 \to \mathbb{Z}_4$ by $f([a]_6) = [a]_4$. This is a function, because each class $[a]_6$ is sent to a class." Then find a $k$ for which $[a]_6 \mapsto [a]_k$ is well defined, and prove it.

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is that the rule is written with the representative $a$, and nobody checked that a different representative gives the same output. The class $[0]_6$ equals $[6]_6$, and the rule gives $[0]_4$ for the first name and $[6]_4 = [2]_4$ for the second, and $[0]_4 \ne [2]_4$ since $4 \nmid 2$. One input, two outputs.

For $k = 3$: suppose $[a]_6 = [a']_6$, so $6 \mid a - a'$ and $a - a' = 6j$ for an integer $j$. Then $a - a' = 3(2j)$, so $3 \mid a - a'$ and $[a]_3 = [a']_3$. So $[a]_6 \mapsto [a]_3$ is well defined. (The same argument works for $k = 2$, $k = 1$ and $k = 6$: any divisor of $6$.)

Check: $[1]_6 = [7]_6$ goes to $[1]_3$ and $[7]_3 = [1]_3$, the same class.

</details>

6\. Let $f \colon A \to B$, $S \subseteq A$ and $T \subseteq B$. Prove that $f(S) \subseteq T$ if and only if $S \subseteq f^{-1}(T)$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $y \in f(S)$ means $y = f(x)$ for some $x \in S$, and $x \in f^{-1}(T)$ means $f(x) \in T$. What we want: two conditionals. The plan: prove each direction by taking an arbitrary element.

*Proof.* ($\Rightarrow$) Suppose $f(S) \subseteq T$, and let $x \in S$. Then $f(x) \in f(S)$, so $f(x) \in T$, which means $x \in f^{-1}(T)$. So $S \subseteq f^{-1}(T)$.

($\Leftarrow$) Suppose $S \subseteq f^{-1}(T)$, and let $y \in f(S)$. Then $y = f(x)$ for some $x \in S$. Since $x \in S \subseteq f^{-1}(T)$, we have $f(x) \in T$, so $y \in T$. So $f(S) \subseteq T$. $\blacksquare$

Check with $f(x) = x^2$, $S = \{-2, 2\}$ and $T = \{4, 9\}$: $f(S) = \{4\} \subseteq T$, and $f^{-1}(T) = \{-3, -2, 2, 3\}$ contains $S$. With $T = \{9\}$ both fail together.

</details>

### Challenge

7\. Call $f \colon A \to B$ injective if $f(a) = f(a')$ implies $a = a'$. Prove that $f(S \cap S') = f(S) \cap f(S')$ for all subsets $S, S'$ of $A$ if and only if $f$ is injective.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Theorem 1(ii) gives $f(S \cap S') \subseteq f(S) \cap f(S')$ for every function, so only the other inclusion matters. The plan: for ($\Leftarrow$), take $y$ in the right side and use injectivity to get one input in both sets. For ($\Rightarrow$), prove the contrapositive with $S$ and $S'$ chosen as two inputs that collide.

*Proof.* ($\Leftarrow$) Suppose $f$ is injective, and let $y \in f(S) \cap f(S')$. Then $y = f(x)$ for some $x \in S$ and $y = f(x')$ for some $x' \in S'$. So $f(x) = f(x')$, and injectivity gives $x = x'$. This $x$ is in $S \cap S'$, so $y \in f(S \cap S')$. With Theorem 1(ii), the sets are equal.

($\Rightarrow$) We prove the contrapositive: if $f$ is not injective, equality fails for some $S$ and $S'$. Suppose $a \ne a'$ and $f(a) = f(a')$. Let $S = \{a\}$ and $S' = \{a'\}$. Then $S \cap S' = \emptyset$, so $f(S \cap S') = \emptyset$, but $f(S) \cap f(S') = \{f(a)\} \cap \{f(a')\} = \{f(a)\}$, which is not empty. $\blacksquare$

Look back: Example 2 is the case $f(x) = x^2$, $a = -2$, $a' = 2$. Check with the injective function $f(x) = 2x$: $f(\{1, 2\} \cap \{2, 3\}) = f(\{2\}) = \{4\}$, and $f(\{1, 2\}) \cap f(\{2, 3\}) = \{2, 4\} \cap \{4, 6\} = \{4\}$.

</details>

8\. (Reviews [equivalence relations and partitions](02-equivalence-relations-and-partitions.md).) Let $f \colon A \to B$ be a function and let $\sim$ be its kernel, $a \sim a'$ when $f(a) = f(a')$. Prove that the rule $g([a]) = f(a)$ is a well-defined function $g \colon A/{\sim} \to B$, and that $g$ is injective in the sense of Practice 7.

<details class="solution" markdown>
<summary>Solution</summary>

*Proof.* Well defined: suppose $[a] = [a']$. By Theorem 1(ii) of the equivalence lesson, $a \sim a'$, which means $f(a) = f(a')$. So $g([a]) = g([a'])$, and the output doesn't depend on the representative. Existence is clear, since each class has a representative, so $g$ is a function.

Injective: suppose $g([a]) = g([a'])$. Then $f(a) = f(a')$, so $a \sim a'$, and $[a] = [a']$ by the same theorem. $\blacksquare$

Look back: this is how any function splits into "sort the inputs into classes" and "relabel each class by its output". Check with $f(n) = n \bmod 3$ on $\mathbb{Z}$: the classes are the three remainder classes, and $g([a]_3) = a \bmod 3$ sends $[0], [1], [2]$ to $0, 1, 2$, one output for each class.

</details>

## Where this shows up

- The next lesson, [injective, surjective and bijective](05-injective-surjective-bijective.md), classifies functions by how their images sit in the codomain, and [cardinality and countability](06-cardinality-and-countability.md) uses bijections to compare the sizes of infinite sets.
- Well-definedness is behind modular arithmetic (divisibility and modular arithmetic<!-- link: ../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->), the construction of the rationals from pairs, and in linear algebra the definition of maps on quotient spaces. A linear map is determined by what it does on a basis, and the definition is checked for well-definedness ([linear transformations, kernel and image](../../05-university-core/06-linear-algebra/05-linear-transformations-kernel-and-image.md)).
- In CS, a function in the mathematical sense is a pure function, and a partial function is one that can raise an exception or return nothing. Hash functions, type signatures and the `Optional` type are all about domains and codomains. In economics, a demand function $q = D(p)$ is a function only if each price has exactly one quantity demanded, and a demand correspondence, which allows several, is the relation version.
