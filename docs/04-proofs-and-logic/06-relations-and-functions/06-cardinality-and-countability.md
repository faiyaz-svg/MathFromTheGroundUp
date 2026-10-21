# Cardinality and countability

After this lesson you can say what it means for two sets to have the same size, prove that $\mathbb{Z}$, $\mathbb{N} \times \mathbb{N}$ and $\mathbb{Q}$ can be listed one by one, prove with Cantor's diagonal argument that the real numbers can't be, and explain why this means that some problems have no program.

Before this: [injective, surjective and bijective](05-injective-surjective-bijective.md) (bijections and the proof templates), [proof by contradiction](../03-core-proof-methods/06-proof-by-contradiction.md), [sets and set operations](../02-logic-and-sets/06-sets-and-set-operations.md#power-sets) (power sets) and [equivalence relations and partitions](02-equivalence-relations-and-partitions.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Show that $f(n) = 2n$ is a bijection from $\mathbb{N}$ to the set of even natural numbers.
2. List the first six elements of $\mathbb{Z}$ in the order $0, -1, 1, -2, 2, -3, \dots$ and say which natural number is sent to $2$ by that listing, counting from $0$.
3. A list of infinite binary sequences starts $0000\ldots$, $1111\ldots$, $0101\ldots$ (the sequences continue forever). Write down the first three digits of a sequence that is not on the list.

<details class="solution" markdown>
<summary>Answers</summary>

1. Injective: $2a = 2b$ gives $a = b$. Surjective: an even natural number is $2n$ for some $n \in \mathbb{N}$, and it is the output of $n$. So $f$ is a bijection.
2. The listing is $0, -1, 1, -2, 2, -3$, and the element $2$ is in position $4$ (counting from $0$), so the natural number $4$ is sent to $2$.
3. Change the first digit of the first sequence, the second digit of the second and the third of the third. The digits on the diagonal are $0, 1, 0$, so the new sequence starts $1, 0, 1$. It differs from each listed sequence in at least one place.

</details>

## The idea

How many natural numbers are there? Infinitely many. How many even natural numbers? Also infinitely many. Is that the same infinity? The even numbers are part of the natural numbers, with the odd numbers left out, so it is tempting to say there are fewer. But pair them off: $0$ with $0$, $1$ with $2$, $2$ with $4$, and $n$ with $2n$. Every natural number gets exactly one even partner and every even number is used exactly once. By any sensible meaning of "same number of things", the two sets are the same size.

That pairing is a bijection, and it is the definition of same size that works for all sets. For finite sets, a bijection exists exactly when the sets have the same number of elements, so nothing changes. For infinite sets, the definition gives surprises. A set can have the same size as a proper part of itself, and $\mathbb{Z}$, $\mathbb{N} \times \mathbb{N}$ and $\mathbb{Q}$ turn out to have the same size as $\mathbb{N}$, even though they look larger. A set with the size of $\mathbb{N}$ is called countable: it can be listed in a sequence, so that every element appears at some finite position.

Then the larger surprise. Cantor proved that the real numbers can't be listed. No sequence, however clever, can contain every real number, so there are different sizes of infinity. The argument is short, it uses only a bijection and a contradiction, and it has consequences for computing. A program is a finite string of symbols, and there are countably many of them. Problems, such as "is this number prime" or "does this program stop", correspond to sets of strings, and there are uncountably many sets of strings. So most problems have no program at all.

## Definitions

### Same size

Two sets $A$ and $B$ have the **same cardinality**, written $A \approx B$ or $\lvert A \rvert = \lvert B \rvert$, if there is a bijection $f \colon A \to B$. We write $\lvert A \rvert \le \lvert B \rvert$ if there is an injection $A \to B$, and $\lvert A \rvert < \lvert B \rvert$ if there is an injection but no bijection.

In plain words, two sets are the same size when their elements can be paired off with none left over on either side, and $A$ is at most as big as $B$ when $A$ can be fitted into $B$ without overlap. Nothing is counted, and no number is used. This is the idea behind a shepherd matching one pebble to each sheep without being able to count.

*Theorem 1.* For sets in a fixed universe, "has the same cardinality as" is an equivalence relation.

*Proof.* Reflexive: the identity $\text{id}_A \colon A \to A$ is a bijection. Symmetric: if $f \colon A \to B$ is a bijection, its inverse $f^{-1} \colon B \to A$ is a bijection (Theorem 2 of [injective, surjective and bijective](05-injective-surjective-bijective.md), and the inverse has an inverse, $f$). Transitive: if $f \colon A \to B$ and $g \colon B \to C$ are bijections, then $g \circ f$ is a bijection (Theorem 1 of the same lesson). $\blacksquare$

So the sets of a universe split into classes of sets of the same size, as in [equivalence relations and partitions](02-equivalence-relations-and-partitions.md), and a cardinality is the name of such a class.

### Finite, infinite, countable

A set $A$ is **finite** if $A \approx \{1, 2, \dots, n\}$ for some $n \in \mathbb{N}$ (with $n = 0$ giving $\emptyset$), and then $\lvert A \rvert = n$. A set is **infinite** if it is not finite. A set is **countably infinite** if $A \approx \mathbb{N}$, **countable** if it is finite or countably infinite, and **uncountable** otherwise.

In plain words, a countably infinite set can be written as a list $a_0, a_1, a_2, \dots$ in which each element appears exactly once. The bijection $n \mapsto a_n$ is the list. A set is countable when it can be listed, and the list may be finite. A set that can't be listed is uncountable.

The natural numbers here start at $0$, as in the rest of the book. A listing that starts at $1$ works just as well, because $n \mapsto n + 1$ is a bijection from $\mathbb{N}$ to the positive integers.

## How to do it

### Showing that a set is countable

1. Try to list it: say what $a_0$, $a_1$, $a_2$, ... are, in an order that reaches every element after finitely many steps.
2. Or build a bijection to a set already known to be countable, such as $\mathbb{N}$, and prove it with the templates for injective and surjective.
3. Or build an injection into a countable set, and use Lemma 1 below. This is often the easiest, because injective is the easy half to prove.
4. Check that no element is skipped (surjective) and no element repeats (injective). When you list by a pattern, the question is whether each element is reached at a finite position.

### Showing that a set is not countable

Only the diagonal argument is available. Assume a list of the set exists, build an element that the list misses, and conclude by contradiction.

### Countable sets

*Theorem 2.* $\mathbb{N} \approx \mathbb{Z}$.

What we want: a bijection. The plan: list $\mathbb{Z}$ as $0, -1, 1, -2, 2, \dots$, which alternates between the negatives and the positives, give the formula, and prove it by writing the inverse.

*Proof.* Define $g \colon \mathbb{N} \to \mathbb{Z}$ by $g(n) = \frac{n}{2}$ if $n$ is even and $g(n) = -\frac{n + 1}{2}$ if $n$ is odd. Define $h \colon \mathbb{Z} \to \mathbb{N}$ by $h(k) = 2k$ if $k \ge 0$ and $h(k) = -2k - 1$ if $k < 0$. The value $h(k)$ is a natural number in each case (for $k < 0$, $-2k - 1 \ge 1$). We check both composites. If $n$ is even, $g(n) = \frac{n}{2} \ge 0$ and $h\left(\frac{n}{2}\right) = n$. If $n$ is odd, $g(n) = -\frac{n+1}{2} < 0$ and $h(g(n)) = (n + 1) - 1 = n$. So $h \circ g = \text{id}_{\mathbb{N}}$. If $k \ge 0$, $h(k) = 2k$ is even and $g(2k) = k$. If $k < 0$, $h(k) = -2k - 1$ is odd and $g(-2k - 1) = -\frac{-2k}{2} = k$. So $g \circ h = \text{id}_{\mathbb{Z}}$. By Theorem 2 of the previous lesson, $g$ is a bijection. $\blacksquare$

Look back: nothing about the size of $\mathbb{Z}$ was assumed. The list $0, -1, 1, -2, 2, \dots$ reaches every integer at a finite position: the integer $-3$ is at position $5$ and $100$ is at position $200$. Check: `g` gives $0, -1, 1, -2, 2, -3, 3, -4, 4$ for $n = 0, \dots, 8$, with no repeats.

*Lemma 1.* If $A$ has an injection into a countable set $B$, then $A$ is countable.

What we know: an injection $i \colon A \to B$. What we want: a list of $A$, possibly finite. The plan: $A$ is the same size as its image $i(A) \subseteq B$, and a subset of a countable set can be listed in the order of $B$.

*Proof.* The function $i$ is a bijection from $A$ to $i(A)$, so it is enough to show that every subset $S$ of a countable set $B$ is countable. If $B$ is finite, $S$ is finite. Suppose $B \approx \mathbb{N}$, so we may assume $B = \mathbb{N}$ (relabel with the bijection) and $S \subseteq \mathbb{N}$. If $S$ is finite, we are done. If $S$ is infinite, list it in increasing order: $s_0$ is the least element of $S$ (it exists because every non-empty set of natural numbers has a least element, the [well-ordering principle](../05-induction/02-strong-induction-and-well-ordering.md)), and $s_{k+1}$ is the least element of $S$ larger than $s_k$ (it exists because $S$ is infinite). The list $s_0 < s_1 < s_2 < \cdots$ has no repeats. Every $s \in S$ appears: since $s_k \ge k$, there is a first $k$ with $s_k \ge s$. If $k = 0$, then $s_0$ is the least element of $S$, so $s_0 = s$. Otherwise $s_{k-1} < s$, and $s_k$ is the least element of $S$ larger than $s_{k-1}$, so $s_k \le s$, which gives $s_k = s$. So $k \mapsto s_k$ is a bijection $\mathbb{N} \to S$. $\blacksquare$

Look back: the lemma turns "list it" into the easier "fit it into something countable". It also gives: every subset of $\mathbb{N}$ is countable, and every set with a surjection from $\mathbb{N}$ is countable (Practice 8).

*Theorem 3.* $\mathbb{N} \times \mathbb{N} \approx \mathbb{N}$.

What we want: a bijection $\pi \colon \mathbb{N} \times \mathbb{N} \to \mathbb{N}$. The plan: arrange the pairs $(i, j)$ in a grid and read it by diagonals. The diagonal $k$ holds the $k + 1$ pairs with $i + j = k$. So the number of pairs on earlier diagonals is $1 + 2 + \cdots + k = \frac{k(k + 1)}{2}$, and the pair $(i, j)$ on diagonal $k = i + j$ sits in position $j$ within its diagonal.

*Proof.* Define

$$
\pi(i, j) = \frac{(i + j)(i + j + 1)}{2} + j.
$$

With $k = i + j$ and $T_k = \frac{k(k+1)}{2}$, we have $\pi(i, j) = T_k + j$, where $0 \le j \le k$. So $T_k \le \pi(i, j) \le T_k + k = T_{k+1} - 1$: the pairs on diagonal $k$ are sent to the block of numbers $T_k, \dots, T_{k+1} - 1$, and these blocks, for $k = 0, 1, 2, \dots$, split $\mathbb{N}$ into non-overlapping intervals that cover it (because $T_0 = 0$ and $T_k \to \infty$).

Surjective: let $n \in \mathbb{N}$. Then $n$ lies in exactly one block, say $T_k \le n < T_{k+1}$. Put $j = n - T_k$, so $0 \le j \le k$, and $i = k - j \ge 0$. Then $i + j = k$ and $\pi(i, j) = T_k + j = n$. Injective: suppose $\pi(i, j) = \pi(i', j') = n$. The block of $n$ determines the diagonal, so $i + j = i' + j' = k$, and then $j = n - T_k = j'$, which gives $i = k - j = i'$. $\blacksquare$

Look back: the proof is a recipe for going both ways. Check: $\pi(4, 9) = \frac{13 \cdot 14}{2} + 9 = 91 + 9 = 100$. Going back from $n = 100$: $T_{13} = 91 \le 100 < 105 = T_{14}$, so $k = 13$, $j = 9$ and $i = 4$. The first values are $\pi(0, 0) = 0$, $\pi(1, 0) = 1$, $\pi(0, 1) = 2$, $\pi(2, 0) = 3$, $\pi(1, 1) = 4$, $\pi(0, 2) = 5$.

*Theorem 4.* $\mathbb{Q}$ is countably infinite.

What we know: Theorems 2 and 3 and Lemma 1. What we want: an injection of $\mathbb{Q}$ into a countable set, and that $\mathbb{Q}$ is infinite. The plan: send each rational number to its numerator and denominator in lowest terms.

*Proof.* Every rational number $q$ can be written in a unique way as $\frac{a}{b}$ with $a \in \mathbb{Z}$, $b \in \mathbb{Z}^+$ and $\gcd(a, b) = 1$ (lowest terms with a positive denominator). Define $i(q) = (a, b - 1) \in \mathbb{Z} \times \mathbb{N}$. Then $i$ is injective, because $(a, b)$ determines $q = \frac{a}{b}$. The set $\mathbb{Z} \times \mathbb{N}$ is countable: the bijection $\mathbb{N} \to \mathbb{Z}$ from Theorem 2 gives a bijection $\mathbb{Z} \times \mathbb{N} \to \mathbb{N} \times \mathbb{N}$ by applying it to the first coordinate, and Theorem 3 finishes. By Lemma 1, $\mathbb{Q}$ is countable. It is infinite because it contains $\mathbb{N}$, so it is countably infinite. $\blacksquare$

Look back: the proof doesn't produce a nice list, and the picture does. Write the positive fractions $\frac{p}{q}$ in a grid, with the numerator $p$ across and the denominator $q$ down, and walk along the diagonals $p + q = 2, 3, 4, \dots$, changing direction on each diagonal so that the path is continuous. Skip any fraction that is not in lowest terms, because the same number has already appeared.

![A grid of fractions with numerators 1 to 6 across the top and denominators 1 to 6 down the left. A grey path zigzags along the diagonals. Fractions in lowest terms are numbered in order of visit, from 1/1 as number 1 through 1/6 as number 17. Fractions not in lowest terms, such as 2/2, 4/2 and 3/3, are greyed out and skipped.](../../assets/figures/04-proofs-and-logic/cardinality-and-countability-rationals.svg)

The numbers in green are the positions in the list. The list begins $1, 2, \frac{1}{2}, \frac{1}{3}, 3, 4, \frac{3}{2}, \frac{2}{3}, \frac{1}{4}, \frac{1}{5}, 5, 6, \dots$, and every positive rational appears exactly once, at a finite position. To include all rationals, list $0$, then each positive rational $r$ followed by $-r$: $0, 1, -1, 2, -2, \frac{1}{2}, -\frac{1}{2}, \dots$.

### Uncountable sets

Let $\mathbb{B}$ be the set of all infinite sequences of $0$s and $1$s, written $s = s_0 s_1 s_2 \ldots$ with each $s_n \in \{0, 1\}$. (A sequence is a function $\mathbb{N} \to \{0, 1\}$.) Examples are $000\ldots$, $0101\ldots$ and the binary digits of $\frac{1}{3}$.

*Theorem 5 (Cantor).* The set $\mathbb{B}$ is uncountable.

What we know: the definition of countable, and that a listing is a bijection from $\mathbb{N}$, and so in particular a surjection. What we want: no listing of $\mathbb{B}$ is complete. The plan is a proof by contradiction. Suppose a list $s^{(0)}, s^{(1)}, s^{(2)}, \dots$ contains every sequence. Build a sequence that differs from the $n$-th listed sequence at place $n$, so it is on no row of the list.

*Proof.* Suppose, for contradiction, that $\mathbb{B}$ is countable, so there is a list $s^{(0)}, s^{(1)}, s^{(2)}, \dots$ in which every sequence of $\mathbb{B}$ appears. Write $s^{(n)}_m$ for the digit at place $m$ of the $n$-th sequence. Define a sequence $d$ by flipping the diagonal:

$$
d_n = 1 - s^{(n)}_n \qquad\text{for each } n \in \mathbb{N}.
$$

Then $d \in \mathbb{B}$, because each $d_n$ is $0$ or $1$. By assumption $d$ is on the list, so $d = s^{(m)}$ for some $m$. Compare the digits at place $m$: $d_m = s^{(m)}_m$, since the sequences are equal. But $d_m = 1 - s^{(m)}_m \ne s^{(m)}_m$ by the definition of $d$. This is a contradiction. So no list contains every sequence, and $\mathbb{B}$ is not countable. It is infinite, because it contains the sequences $10\ldots$, $010\ldots$, $0010\ldots$ and so on, so it is uncountable. $\blacksquare$

Look back: the contradiction is a single place, $m$, where $d$ is both equal to and different from row $m$. The argument works for every list at once, because the construction of $d$ takes the list as input. A table shows the idea: take a few rows, read the diagonal, flip it.

| Row | Digits at places $0$ to $7$ |
|---|---|
| $s^{(0)}$ | 0 1 1 0 1 0 0 1 |
| $s^{(1)}$ | 1 1 0 0 1 0 1 0 |
| $s^{(2)}$ | 0 0 0 1 0 1 1 1 |
| $s^{(3)}$ | 1 0 1 0 1 1 0 0 |
| $s^{(4)}$ | 0 1 1 1 0 0 1 0 |
| $s^{(5)}$ | 1 1 1 0 0 0 0 1 |
| $s^{(6)}$ | 0 0 0 0 0 1 1 0 |
| $s^{(7)}$ | 1 0 0 1 1 1 0 1 |

The diagonal digits are $0, 1, 0, 0, 0, 0, 1, 1$, and flipping each gives $d = 1, 0, 1, 1, 1, 1, 0, 0$. The sequence $d$ differs from $s^{(0)}$ at place $0$, from $s^{(1)}$ at place $1$, and so on, so it matches none of the eight rows, whatever the rows contain after place $7$.

A sequence in $\mathbb{B}$ is the same thing as a subset of $\mathbb{N}$: the sequence $s$ corresponds to $\{n : s_n = 1\}$, the set of places holding a $1$. This correspondence is a bijection $\mathbb{B} \to \mathcal{P}(\mathbb{N})$, so the power set of $\mathbb{N}$ is uncountable too.

*Theorem 6.* The real numbers $\mathbb{R}$ are uncountable.

*Proof.* It is enough to show that the interval $(0, 1)$ is uncountable, because a set containing an uncountable set is uncountable (an injection into a countable set would make the subset countable, by Lemma 1). Suppose $x_0, x_1, x_2, \dots$ lists every number in $(0, 1)$, and write each in decimal, $x_n = 0.x^{(n)}_0 x^{(n)}_1 x^{(n)}_2 \ldots$. Define $y = 0.y_0 y_1 y_2 \ldots$ by $y_n = 5$ if $x^{(n)}_n \ne 5$ and $y_n = 4$ if $x^{(n)}_n = 5$. Then $y \in (0, 1)$ and $y$ differs from $x_n$ in the digit at place $n$. The digits of $y$ are only $4$ and $5$, so $y$ has no second decimal expansion (the double expansions such as $0.4999\ldots = 0.5000\ldots$ involve a tail of $9$s or $0$s). So $y \ne x_n$ for every $n$, which contradicts that the list contains $y$. $\blacksquare$

Look back: the choice of the digits $4$ and $5$ is the way around a technicality, and any two digits other than $0$ and $9$ would do. Using only $0$s and $1$s as in Theorem 5 would have hit the problem that $0.0999\ldots = 0.1000\ldots$.

*Theorem 7 (Cantor's theorem).* For every set $A$, there is no surjection from $A$ to $\mathcal{P}(A)$. Hence $\lvert A \rvert < \lvert \mathcal{P}(A) \rvert$.

What we know: an injection $a \mapsto \{a\}$ from $A$ into $\mathcal{P}(A)$. What we want: no function $f \colon A \to \mathcal{P}(A)$ is surjective. The plan: the diagonal argument with no list. Given $f$, define the set $D$ of elements that are not in their own image, and show that $D$ is not an image.

*Proof.* The map $a \mapsto \{a\}$ is injective, so $\lvert A \rvert \le \lvert \mathcal{P}(A) \rvert$. Let $f \colon A \to \mathcal{P}(A)$ be any function. Define

$$
D = \{ a \in A : a \notin f(a) \}.
$$

Then $D \in \mathcal{P}(A)$. Suppose $D = f(a_0)$ for some $a_0 \in A$. Is $a_0 \in D$? If $a_0 \in D$, then by the definition of $D$, $a_0 \notin f(a_0) = D$, a contradiction. If $a_0 \notin D$, then $a_0 \notin f(a_0)$, so $a_0$ meets the definition of $D$ and $a_0 \in D$, a contradiction. So no $a_0$ has $f(a_0) = D$, and $f$ is not surjective. In particular there is no bijection, so $\lvert A \rvert < \lvert \mathcal{P}(A) \rvert$. $\blacksquare$

Look back: for $A = \mathbb{N}$ this is Theorem 5 again, with $f(n)$ playing the role of row $n$ and $D$ the flipped diagonal. It is also the argument of Russell's paradox from [sets and set operations](../02-logic-and-sets/06-sets-and-set-operations.md). For a finite set it says $2^n > n$. The theorem gives an endless ladder of sizes: $\mathbb{N}$, $\mathcal{P}(\mathbb{N})$, $\mathcal{P}(\mathcal{P}(\mathbb{N}))$, and so on, each strictly larger than the last. Check with $A = \{0, 1, 2\}$ and $f(0) = \{0, 1\}$, $f(1) = \emptyset$, $f(2) = \{0, 2\}$: here $D = \{1\}$ (since $0 \in f(0)$, $1 \notin f(1)$ and $2 \in f(2)$), and $\{1\}$ is not among the three values of $f$.

### Why some problems have no program

A **decision problem** asks a yes-or-no question about each input string, such as "is this number prime" or "does this program print something". Fix a finite alphabet $\Sigma$ (for example the 128 ASCII characters) and let $\Sigma^*$ be the set of all finite strings over it. A decision problem is then determined by the set $L \subseteq \Sigma^*$ of inputs whose answer is yes, so the set of all decision problems is $\mathcal{P}(\Sigma^*)$.

*Theorem 8.* For a finite alphabet $\Sigma$, the set $\Sigma^*$ is countably infinite, and the set $\mathcal{P}(\Sigma^*)$ of decision problems is uncountable.

*Proof.* List $\Sigma^*$ by length, and within one length in dictionary order: first the empty string, then the strings of length $1$, then those of length $2$, and so on. Each length has finitely many strings, namely $\lvert \Sigma \rvert^L$ of them, so every string appears after finitely many steps. So $\Sigma^*$ is countably infinite. For $\Sigma = \{0, 1\}$ the list is $\varepsilon, 0, 1, 00, 01, 10, 11, 000, \dots$, and the string of length $L$ with binary value $v$ is at position $2^L - 1 + v$. Then $\Sigma^* \approx \mathbb{N}$, so $\mathcal{P}(\Sigma^*) \approx \mathcal{P}(\mathbb{N})$ through that bijection, and $\mathcal{P}(\mathbb{N})$ is uncountable by Theorem 7. $\blacksquare$

A program in any programming language is a finite string over a finite alphabet, so the set of all programs is a subset of $\Sigma^*$, which is countable (Lemma 1). Each program solves at most one decision problem, the one given by the inputs on which it answers yes. The map from programs to the problems they solve has a countable domain, so its range is countable (list the values in the order of the programs). The set of all problems is uncountable. So some problem is solved by no program: there are more problems than programs.

This proves that unsolvable problems exist, and it doesn't produce one. A specific one needs another diagonal argument. The program halts-on-itself diagonal gives the halting problem, which is the subject of decidability and the halting problem<!-- link: ../../06-cs-math/06-theory-of-computation/05-decidability-and-the-halting-problem.md -->.

## Worked examples

<div class="example" markdown>

### Example 1: a set the same size as a part of itself

Show that $\mathbb{N}$ and $E = \{0, 2, 4, 6, \dots\}$ have the same cardinality, and that $\mathbb{Z}$ has the same cardinality as the multiples of $5$.

Step 1 (try to build a bijection). Pair $n$ with $2n$. Define $f \colon \mathbb{N} \to E$ by $f(n) = 2n$.

Step 2 (injective). Suppose $f(a) = f(b)$. Then $2a = 2b$, so $a = b$.

Step 3 (surjective). Let $e \in E$. By definition of $E$, $e = 2n$ for some $n \in \mathbb{N}$, and then $f(n) = e$.

So $\mathbb{N} \approx E$, although $E \subsetneq \mathbb{N}$. For the second claim, $g \colon \mathbb{Z} \to 5\mathbb{Z}$ with $g(k) = 5k$ is a bijection by the same two checks: $5a = 5b$ gives $a = b$, and a multiple of $5$ is $5k$ for an integer $k$.

Check: $f(0), f(1), f(2), f(3) = 0, 2, 4, 6$, and every even number appears once. This is the behaviour that a finite set never has: a finite set is never the same size as one of its proper subsets (Theorem 3 of the previous lesson).

</div>

<div class="example" markdown>

### Example 2: pairing function, both directions

Compute $\pi(3, 2)$ and $\pi(0, 5)$. Then find the pair $(i, j)$ with $\pi(i, j) = 20$.

Use $\pi(i, j) = \frac{(i + j)(i + j + 1)}{2} + j$. For $(3, 2)$ the diagonal number is $k = 5$ and $T_5 = \frac{5 \cdot 6}{2} = 15$, so $\pi(3, 2) = 15 + 2 = 17$. For $(0, 5)$ it is also $k = 5$, so $\pi(0, 5) = 15 + 5 = 20$.

For the inverse, take $n = 20$. The triangular numbers are $0, 1, 3, 6, 10, 15, 21, \dots$, and $15 \le 20 < 21$, so $k = 5$. Then $j = 20 - 15 = 5$ and $i = k - j = 0$, so $(i, j) = (0, 5)$, as computed.

Check: $\pi(0, 5) = 20$ matches, and the diagonal $k = 5$ holds the six pairs with $i + j = 5$ that get the numbers $15$ to $20$: $(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)$, in that order. So $(3, 2)$ is third in the block, number $17$.

</div>

<div class="example" markdown>

### Example 3: the diagonal on a concrete list

Here are the first four digits of four sequences in $\mathbb{B}$: $s^{(0)} = 0110\ldots$, $s^{(1)} = 1010\ldots$, $s^{(2)} = 0011\ldots$ and $s^{(3)} = 1001\ldots$. Find the first four digits of a sequence that is not any of them, and explain why it can't be $s^{(2)}$.

The diagonal digits are the digit at place $n$ of row $n$: $s^{(0)}_0 = 0$, $s^{(1)}_1 = 0$, $s^{(2)}_2 = 1$ and $s^{(3)}_3 = 1$. Flip each: $d = 1100\ldots$.

The sequence $d$ can't be $s^{(2)}$ because $d_2 = 0$ and $s^{(2)}_2 = 1$: they differ at place $2$. For the same reason $d$ differs from $s^{(0)}$ at place $0$, from $s^{(1)}$ at place $1$ and from $s^{(3)}$ at place $3$.

Check: $d = 1100$ against the rows $0110$, $1010$, $0011$, $1001$: each row disagrees with $d$ at its own diagonal place, and no row equals $1100$. We only know the first four digits of each row, and that is enough to show that $d$ differs from each of them. The digits of $d$ after place $3$ are chosen the same way, once the later digits of the rows are known.

</div>

<div class="example" markdown>

### Example 4: finite binary strings (finish it yourself)

List the binary strings by length and then in dictionary order: $\varepsilon, 0, 1, 00, 01, 10, 11, 000, \dots$ with positions $0, 1, 2, \dots$. A string $w$ of length $L$ with binary value $v$ (and $v = 0$ for $\varepsilon$) is at position $2^L - 1 + v$. For example, $101$ has $L = 3$ and $v = 5$, so its position is $8 - 1 + 5 = 12$. Going backwards, the string at position $n$ is the binary form of $n + 1$ with its leading $1$ removed: for $n = 5$, $n + 1 = 6 = 110_2$, which gives $10$.

Now find the string at position $30$, and then the position of the string $100101$.

<details class="solution" markdown>
<summary>Finish</summary>

For position $30$: $n + 1 = 31 = 11111_2$, and removing the leading $1$ leaves $1111$. For the string $100101$: $L = 6$, and $100101_2 = 32 + 4 + 1 = 37$, so the position is $2^6 - 1 + 37 = 63 + 37 = 100$.

Check: going back the other way, the string $1111$ has $L = 4$ and $v = 15$, so its position is $16 - 1 + 15 = 30$. And for position $100$, $101 = 1100101_2$, and removing the leading $1$ gives $100101$. So the listing is a bijection between $\mathbb{N}$ and the finite binary strings, which proves that this set is countable.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a set can have the same size as a proper part of itself. That is not a contradiction, and it is what "infinite" means in this lesson. Don't use "the part is smaller than the whole" as an argument about size for infinite sets. Use a bijection to show equal sizes and, for different sizes, an injection with a proof that no bijection exists.

</div>

<div class="warning" markdown>

Watch out: "countable" doesn't mean "easy to list" or "has an end". It means that a listing exists, in which every element appears at some finite position. The rationals are dense on the number line, with another rational between any two, and are still countable. And "uncountable" doesn't mean "very large": $\{0, 1\}^{\mathbb{N}}$ has only two choices per place and is uncountable.

</div>

<div class="warning" markdown>

Watch out: you can't fix the diagonal argument by adding the new sequence to the list. The flaw in "add $d$ at the top and the list is complete" is that the new list has its own diagonal and its own missing sequence $d'$. The theorem is that no list works, whatever its order and however often it is repaired.

</div>

<div class="warning" markdown>

Watch out: when you list the rationals, skip the fractions that are not in lowest terms, or the list repeats ($\frac{1}{2}$, $\frac{2}{4}$, $\frac{3}{6}$, ...). Repeats don't hurt countability, since a list with repeats gives a surjection and Practice 8 shows that is enough, but a bijection needs one entry for each number.

</div>

<div class="warning" markdown>

Watch out: the diagonal argument for decimal expansions needs a way to avoid two expansions of one number ($0.5000\ldots = 0.4999\ldots$). If the new number is built with digits that could end in all $0$s or all $9$s, it might equal a listed number written the other way. Using only the digits $4$ and $5$ (Theorem 6) avoids the issue.

</div>

Some small cases. A finite set is countable, and the empty set is countable. A subset of a countable set is countable, and a union of two countable sets is countable (interleave the two lists, skipping repeats). A countable union of countable sets is countable, by the zigzag. A product of two countable sets is countable (Theorem 3). On the other side, the set of subsets of a countable infinite set is uncountable (Theorem 7), and so is the set of functions from $\mathbb{N}$ to $\{0, 1\}$.

## Tricks and shortcuts

To show that a set $A$ is countable, an injection into $\mathbb{N}$ or into $\mathbb{N} \times \mathbb{N}$ is enough (Lemma 1 and Theorem 3). Encode each element by a finite string or a finite list of integers. For example, a polynomial with integer coefficients is the finite list of its coefficients, so the set of such polynomials is countable. The same encoding shows that the set of programs is countable.

To show that a set is uncountable, compare with a known uncountable set: if $\mathbb{B}$ or $\mathcal{P}(\mathbb{N})$ injects into $A$, then $A$ is uncountable. Otherwise run the diagonal argument directly: assume a list, flip the diagonal.

When you do the diagonal argument, write down the rule for the new object first ("$d_n$ is the opposite of the $n$-th digit of row $n$") and then check that the new object is in the set and differs from each row. Those two checks are the proof.

## In code

The program prints the bijection from $\mathbb{N}$ to $\mathbb{Z}$, the pairing function and its inverse, the zigzag list of rationals, the numbering of binary strings, a diagonal sequence for the table in this lesson, and checks Cantor's theorem for a 3-element set by testing all 512 functions.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction
from itertools import combinations, product
from math import gcd, isqrt

# N -> Z: 0, 1, 2, 3, 4, ... goes to 0, -1, 1, -2, 2, ...
def to_int(n):
    return n // 2 if n % 2 == 0 else -(n + 1) // 2

print([to_int(n) for n in range(9)])           # [0, -1, 1, -2, 2, -3, 3, -4, 4]
print(len({to_int(n) for n in range(1000)}) == 1000)   # True: no repeats

# Cantor pairing N x N -> N and its inverse
def pair(i, j):
    return (i + j) * (i + j + 1) // 2 + j

def unpair(n):
    k = (isqrt(8 * n + 1) - 1) // 2          # the diagonal that n lies on
    j = n - k * (k + 1) // 2
    return k - j, j

print(pair(4, 9), unpair(100))                 # 100 (4, 9)
print(all(unpair(pair(i, j)) == (i, j) for i in range(80) for j in range(80)))   # True
print(sorted(pair(i, j) for i in range(30) for j in range(30) if i + j < 30) == list(range(465)))   # True

# the positive rationals in zigzag order, skipping fractions not in lowest terms
def zigzag(limit):
    for s in range(2, limit + 1):
        cells = [(p, s - p) for p in range(1, s)]
        if s % 2 == 1:
            cells.reverse()
        for p, q in cells:
            if gcd(p, q) == 1:
                yield Fraction(p, q)

first = []
for r in zigzag(12):
    first.append(r)
print([str(r) for r in first[:12]])
# ['1', '2', '1/2', '1/3', '3', '4', '3/2', '2/3', '1/4', '1/5', '5', '6']
print(len(first) == len(set(first)))           # True: each rational appears once

# all rationals: 0, then r and -r for each positive r
def all_rationals(n):
    out = [Fraction(0)]
    for r in zigzag(12):
        out += [r, -r]
        if len(out) >= n:
            break
    return out[:n]
print([str(r) for r in all_rationals(9)])      # ['0', '1', '-1', '2', '-2', '1/2', '-1/2', '1/3', '-1/3']

# finite binary strings: shortest first, then in dictionary order
def string_at(n):
    return bin(n + 1)[3:]

print([string_at(n) for n in range(10)])
# ['', '0', '1', '00', '01', '10', '11', '000', '001', '010']
index_of = lambda w: 2 ** len(w) - 1 + (int(w, 2) if w else 0)
print(string_at(30), index_of("1111"), index_of("101"))   # 1111 30 12
print(all(index_of(string_at(n)) == n for n in range(1000)))   # True

# the diagonal argument on a finite window of a "list" of infinite binary sequences
rows = ["01101001", "11001010", "00010111", "10101100", "01110010", "11100001", "00000110", "10011101"]
diagonal = "".join("1" if rows[n][n] == "0" else "0" for n in range(len(rows)))
print(diagonal)                                # 10111100
print([diagonal[n] != rows[n][n] for n in range(8)].count(True))   # 8: it differs from row n at place n
print(any(diagonal == r for r in rows))        # False

# Cantor's theorem on a 3-element set: no function A -> P(A) is onto
A = [0, 1, 2]
subsets = [frozenset(c) for r in range(4) for c in combinations(A, r)]
count_onto = 0
for values in product(subsets, repeat=3):
    f = dict(zip(A, values))
    if set(f.values()) == set(subsets):
        count_onto += 1
print(len(subsets), count_onto)                # 8 0
f = {0: frozenset({0, 1}), 1: frozenset(), 2: frozenset({0, 2})}
D = frozenset(a for a in A if a not in f[a])
print(sorted(D), D in f.values())              # [1] False
```

The function `unpair` is the surjectivity proof of Theorem 3: it finds the diagonal $k$ with the integer square root and then reads off $j$ and $i$. The checks on a finite window are evidence for the theorems, and the theorems are what cover the infinite sets. The last block is Theorem 7 in miniature: of the $8^3 = 512$ functions from a 3-element set to its 8 subsets, none is onto, and for a specific $f$ the diagonal set $D$ is the subset that $f$ misses.

</details>

## FAQ

### Are there sizes of infinity between $\mathbb{N}$ and $\mathbb{R}$?

The statement that there are none is the continuum hypothesis. Gödel and Cohen showed that it can neither be proved nor disproved from the standard axioms of set theory, so the question has no answer there. You will not need it in a CS course. What you need is that $\mathbb{N}$ is the smallest infinite size, that $\mathbb{R}$ is bigger, and that $\mathcal{P}(\mathbb{N})$ has the same size as $\mathbb{R}$ (a fact stated here without proof).

### Does this mean there are more real numbers than rational numbers?

Yes, in the sense of cardinality. The rationals can be listed, and the reals can't, so $\lvert \mathbb{Q} \rvert < \lvert \mathbb{R} \rvert$. Since the irrationals are the reals that are not rational, and the union of two countable sets would be countable, the irrationals must be uncountable: almost every real number is irrational, in the sense of size. Even the numbers you can define in a finite sentence, such as $\sqrt{2}$ and $\pi$, are only countably many.

### Why is a program a finite string, and why does that matter?

Source code is text, and a program that runs on a real machine has a finite description. There are only countably many finite strings over a finite alphabet, so there are countably many programs, in any language. The argument for Theorem 8 doesn't depend on which language it is, or on the machine. It would fail for a machine that could read an infinite description, which is not a program in the usual sense.

### Why can't I just list the reals in order, smallest first?

There is no smallest real number, and between any two reals there are infinitely many others. A list needs a first element and a next element for each element, and the reals have neither a smallest element nor an obvious "next" after $x$. The rationals have the same property and still can be listed, because a list doesn't need to follow the order of the number line. The diagonal argument proves that no list of any order works for the reals.

## Practice

### Warm-up

1\. Show that $f(n) = n + 5$ is a bijection from $\mathbb{N}$ to $\{5, 6, 7, \dots\}$.

<details class="solution" markdown>
<summary>Solution</summary>

Injective: $a + 5 = b + 5$ gives $a = b$. Surjective: an element of $\{5, 6, 7, \dots\}$ is an integer $m \ge 5$, and $n = m - 5 \ge 0$ is a natural number with $f(n) = m$. So $f$ is a bijection.

Check: $f(0) = 5$, $f(1) = 6$, $f(2) = 7$, and every integer from $5$ upwards is hit once.

</details>

2\. Compute $\pi(0, 0)$, $\pi(2, 1)$ and $\pi(3, 3)$, and find the pair that $\pi$ sends to $28$.

<details class="solution" markdown>
<summary>Solution</summary>

Using $\pi(i, j) = \frac{(i + j)(i + j + 1)}{2} + j$: $\pi(0, 0) = 0 + 0 = 0$. $\pi(2, 1)$ has $k = 3$ and $T_3 = 6$, so $\pi(2, 1) = 6 + 1 = 7$. $\pi(3, 3)$ has $k = 6$ and $T_6 = 21$, so $\pi(3, 3) = 21 + 3 = 24$.

For $n = 28$: the triangular numbers are $\dots, 21, 28, 36, \dots$, so $T_7 = 28 \le 28 < 36 = T_8$ and $k = 7$. Then $j = 28 - 28 = 0$ and $i = 7 - 0 = 7$. The pair is $(7, 0)$.

Check: $\pi(7, 0) = \frac{7 \cdot 8}{2} + 0 = 28$.

</details>

3\. In the zigzag list of positive rationals, which position (counting from $1$) does $\frac{3}{2}$ have, and what is the 10th fraction? Why is $\frac{2}{2}$ not in the list?

<details class="solution" markdown>
<summary>Solution</summary>

The list is $1, 2, \frac{1}{2}, \frac{1}{3}, 3, 4, \frac{3}{2}, \frac{2}{3}, \frac{1}{4}, \frac{1}{5}, 5, 6, \dots$. So $\frac{3}{2}$ is in position $7$ and the 10th fraction is $\frac{1}{5}$. The fraction $\frac{2}{2}$ is skipped because it is not in lowest terms: it equals $1$, which is already at position $1$.

Check: positions $1$ to $10$ are $1, 2, \frac{1}{2}, \frac{1}{3}, 3, 4, \frac{3}{2}, \frac{2}{3}, \frac{1}{4}, \frac{1}{5}$, ten different numbers, matching the numbers in the figure.

</details>

### Standard

4\. Prove that $\mathbb{Z} \times \mathbb{Z}$ is countable.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $\mathbb{N} \approx \mathbb{Z}$ (Theorem 2) and $\mathbb{N} \times \mathbb{N} \approx \mathbb{N}$ (Theorem 3). What we want: a bijection, or an injection into a countable set. The plan: apply the bijection $h \colon \mathbb{Z} \to \mathbb{N}$ of Theorem 2 to both coordinates.

*Proof.* Define $H \colon \mathbb{Z} \times \mathbb{Z} \to \mathbb{N} \times \mathbb{N}$ by $H(a, b) = (h(a), h(b))$. It is injective: if $(h(a), h(b)) = (h(a'), h(b'))$, then $h(a) = h(a')$ and $h(b) = h(b')$, so $a = a'$ and $b = b'$ because $h$ is injective. It is surjective: given $(m, n) \in \mathbb{N} \times \mathbb{N}$, surjectivity of $h$ gives $a$ and $b$ with $h(a) = m$ and $h(b) = n$. So $H$ is a bijection. Composing with $\pi \colon \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ gives a bijection $\mathbb{Z} \times \mathbb{Z} \to \mathbb{N}$. $\blacksquare$

Check: $H(-1, 2) = (h(-1), h(2)) = (1, 4)$ and $\pi(1, 4) = 15 + 4 = 19$, so the point $(-1, 2)$ is number $19$ in the list of lattice points.

</details>

5\. Find the flaw in this argument and say what is true. "The real numbers in $(0, 1)$ are countable. Suppose someone gives a list. The diagonal number $d$ is not on it. But we can just add $d$ to the front of the list. Now the list contains $d$, so it is complete."

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is that adding $d$ gives a new list, and the same construction applied to the new list gives a new diagonal number $d'$ that is not on it. The claim "the list is complete" would need that no number is missing, and the argument itself shows that a number is always missing. The diagonal argument is a recipe: for every list there is a number the list misses. Repairing one list doesn't change that.

What is true: no list of the real numbers in $(0, 1)$ is complete, so $(0, 1)$ is uncountable.

Check: take the list $0.1000\ldots$, $0.2000\ldots$, $0.3000\ldots, \dots$. The diagonal digits are $1, 0, 0, 0, \dots$, none of them $5$, so the diagonal number built with the digits $4$ and $5$ is $d = 0.5555\ldots$. Put $d$ at the front. In the new list the diagonal digits are $5, 0, 0, \dots$, so the new diagonal number is $0.4555\ldots$, which is not on the new list.

</details>

6\. Prove that the set $F$ of infinite binary sequences with only finitely many $1$s is countable. Why doesn't this contradict Theorem 5?

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Lemma 1 and the countability of the finite binary strings (Theorem 8). What we want: an injection of $F$ into the finite strings. The plan: send a sequence to the string that runs up to its last $1$.

*Proof.* Define $i \colon F \to \{0, 1\}^*$ as follows. For the sequence $0000\ldots$, let $i(s) = \varepsilon$ (the empty string). Otherwise let $m$ be the place of the last $1$ in $s$ (it exists because $s$ has finitely many $1$s and at least one), and let $i(s) = s_0 s_1 \cdots s_m$. The map $i$ is injective: from the string $s_0 \cdots s_m$ we recover $s$ by adding zeros forever, and the empty string recovers the zero sequence. Since $\{0, 1\}^*$ is countable, $F$ is countable by Lemma 1. $\blacksquare$

It does not contradict Theorem 5, because $F$ is a small part of $\mathbb{B}$. The diagonal sequence $d$ built from a list of members of $F$ is not guaranteed to have finitely many $1$s, so it need not be in $F$, and the argument doesn't apply.

Check: the sequence $1010000\ldots$ goes to the string $101$, which is at position $12$ in the list of binary strings. The sequence with a $1$ in every place goes to no string at all, and it is not in $F$.

</details>

### Challenge

7\. Let $S$ be the set of real numbers in $(0, 1)$ whose decimal expansions use only the digits $4$ and $5$. Prove that $S$ is uncountable.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: a number with digits only $4$ and $5$ has no second decimal expansion, since a double expansion ends in all $0$s or all $9$s. What we want: no list of $S$ is complete. The plan: a diagonal argument in which the new digit is $9$ minus the diagonal digit, which swaps $4$ and $5$.

*Proof.* Suppose, for contradiction, that $x_0, x_1, x_2, \dots$ lists all of $S$, and write $x_n = 0.x^{(n)}_0 x^{(n)}_1 \ldots$ with every digit $4$ or $5$. Define $y = 0.y_0 y_1 y_2 \ldots$ by $y_n = 9 - x^{(n)}_n$. Then $y_n = 5$ when $x^{(n)}_n = 4$, and $y_n = 4$ when $x^{(n)}_n = 5$, so all digits of $y$ are $4$ or $5$, and $y \in S$. The digit of $y$ at place $n$ differs from the digit of $x_n$ at place $n$. Since both expansions use only $4$ and $5$, they are the unique expansions of their numbers, so $y \ne x_n$ for every $n$. This contradicts that the list contains every element of $S$. $\blacksquare$

Check with the first three rows $x_0 = 0.4\ldots$, $x_1 = 0.55\ldots$, $x_2 = 0.445\ldots$: the diagonal digits are $4, 5, 5$, so $y = 0.544\ldots$, which differs from $x_0$ at the first place, $x_1$ at the second and $x_2$ at the third.

</details>

8\. (Reviews [injective, surjective and bijective](05-injective-surjective-bijective.md).) Prove that if there is a surjection $f \colon \mathbb{N} \to B$ for a set $B$, then $B$ is countable.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $f$ is surjective, so each $b \in B$ has at least one $n$ with $f(n) = b$. What we want: an injection $B \to \mathbb{N}$, and then Lemma 1. The plan: send each $b$ to the least $n$ that $f$ sends to $b$.

*Proof.* For $b \in B$, the set $\{n \in \mathbb{N} : f(n) = b\}$ is non-empty because $f$ is surjective, so it has a least element by the well-ordering principle. Let $g(b)$ be that least element. Then $g \colon B \to \mathbb{N}$ is a function. It is injective: suppose $g(b) = g(b') = n$. Then $f(n) = b$ and $f(n) = b'$, so $b = b'$. By Lemma 1, $B$ is countable. $\blacksquare$

Check with $f(n) = n \bmod 3$ from $\mathbb{N}$ onto $\{0, 1, 2\}$: $g(0) = 0$, $g(1) = 1$ and $g(2) = 2$, the first $n$ for each value, and $g$ is injective.

</details>

## Where this shows up

- The last chapter of this folder collects the slips that proofs like these invite (common proof mistakes<!-- link: ../07-putting-it-together/01-common-proof-mistakes.md -->). The idea of a bijection comes back in counting: counting a set means finding a bijection to $\{1, \dots, n\}$ (counting rules<!-- link: ../../06-cs-math/03-counting-and-discrete-probability/01-counting-rules.md -->).
- In CS, Theorem 8 is the first step of the theory of computation. The existence of a problem with no program is shown here, and the halting problem is a specific one (decidability and the halting problem<!-- link: ../../06-cs-math/06-theory-of-computation/05-decidability-and-the-halting-problem.md -->, reductions and undecidability<!-- link: ../../06-cs-math/06-theory-of-computation/06-reductions-and-undecidability.md -->). The countable sets are the ones a program can enumerate, and the same diagonal argument proves that the halting problem is undecidable.
- In analysis and probability, "countable" is the line between sums and integrals. A sum over a countable set is a series ([summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md)), and a probability distribution that puts positive weight on each of countably many points is discrete. A uniform distribution on $[0, 1]$ puts no weight on any single point, and that is possible because the interval is uncountable.
