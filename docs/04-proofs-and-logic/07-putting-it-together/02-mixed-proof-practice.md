# Mixed proof practice

After this lesson you can pick a proof method from the shape of a statement you have not seen before, and write a complete proof in the style a grader accepts.

Before this: the whole folder. This page is a practice set, so it drops the sections that don't fit one (the idea, definitions, worked examples, edge cases, tricks, code and FAQ). It keeps a quick check and "Where this shows up", and every problem has a hint and a full model proof.

## Quick check

Write only the first sentence of a proof for each statement, the sentence that opens the method you would use. Do not prove anything.

1. For every integer $n$, if $n^2 - 1$ is even, then $n$ is odd.
2. For all sets $A$ and $B$, $A \setminus (A \setminus B) = A \cap B$.
3. For every integer $n \ge 1$, $1 + 3 + 5 + \cdots + (2n - 1) = n^2$.

<details class="solution" markdown>
<summary>Answers</summary>

1. "We prove the contrapositive: if $n$ is even, then $n^2 - 1$ is odd." The hypothesis is about $n^2 - 1$, which is hard to use, and the conclusion "$n$ is odd" has a clean negation.
2. "We show each set is a subset of the other. Let $x \in A \setminus (A \setminus B)$." A set equality needs two inclusions (or a chain of equivalences).
3. "By induction on $n$. Base case, $n = 1$: $1 = 1^2$." The statement is for every integer from 1 up, and each sum grows from the last by one term.

</details>

## Choosing a method

A textbook chapter tells you which method to use, and an exam does not. That is why mixed practice is harder than chapter practice, and why it is the practice that transfers: choosing the method is part of the skill. The full table is in [scratch work and proof strategies](../03-core-proof-methods/03-scratch-work-and-proof-strategies.md#choosing-a-method-from-the-shape-of-the-claim). The short version is to read the statement from the outside in.

1. Find the outermost quantifier or connective. "For every" means pick an arbitrary object. "There exists" means find a witness. "If ... then" means assume the hypothesis. "If and only if" means two proofs. "Exactly one" means existence, then uniqueness.
2. Look at what is being compared. Two sets being equal means two inclusions. A function being injective or surjective means the definition, started from the right end. A property of every $n \ge n_0$ that grows step by step, or a recursive definition, or a loop, suggests induction.
3. Look for a negative. "Irrational", "no", "not", "infinitely many" and "there is no largest" usually go by contradiction. A conclusion that is "$P$ or $Q$", or a hypothesis about a function of the variable such as $n^2$, usually goes by the contrapositive.
4. If the statement could be false, spend two minutes on small cases before writing anything. If a case fails, switch to a disproof.
5. If nothing fits, write the definitions of every defined word with fresh letters and see what you have.

After you solve a problem, say in one line which method you used and why you picked it. The solutions below do that in the first sentence. Try each problem for at least ten minutes before opening the hint, and open the hint before the solution. The solutions are model answers, and a correct proof by a different method is fine.

## Practice

### Warm-up

1\. Prove that the sum of any three consecutive integers is divisible by 3.

<details class="solution" markdown>
<summary>Hint</summary>

Name the smallest of the three integers, and write the other two in terms of it.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A direct proof of a "for every" statement: take an arbitrary integer and compute.

*Proof.* Let $n$ be the smallest of three consecutive integers, so the integers are $n$, $n + 1$ and $n + 2$. Their sum is $n + (n + 1) + (n + 2) = 3n + 3 = 3(n + 1)$. Since $n + 1$ is an integer, the sum is divisible by 3. $\blacksquare$

Check: $4 + 5 + 6 = 15 = 3 \cdot 5$.

</details>

2\. Let $n$ be an integer. Prove that if $5n + 3$ is even, then $n$ is odd.

<details class="solution" markdown>
<summary>Hint</summary>

Which is easier to start from: "$5n + 3$ is even", or "$n$ is not odd"?

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A proof by the contrapositive, because the conclusion "$n$ is odd" has a clean negation and the hypothesis is awkward to unpack.

*Proof.* We prove the contrapositive: if $n$ is even, then $5n + 3$ is odd. Let $n$ be even, so $n = 2k$ for an integer $k$. Then $5n + 3 = 10k + 3 = 2(5k + 1) + 1$, and $5k + 1$ is an integer, so $5n + 3$ is odd. $\blacksquare$

Check: $n = 4$ gives $23$, which is odd. And $n = 3$ gives $18$, which is even, with $n$ odd, as the claim says.

</details>

3\. Prove that $(A \setminus B) \cup (A \cap B) = A$ for all sets $A$ and $B$.

<details class="solution" markdown>
<summary>Hint</summary>

Prove two inclusions. For $A \subseteq (A \setminus B) \cup (A \cap B)$, an element of $A$ is either in $B$ or not.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A set equality, so two inclusions, with a split into two cases in one of them.

*Proof.* ($\subseteq$) Let $x \in (A \setminus B) \cup (A \cap B)$. If $x \in A \setminus B$, then $x \in A$. If $x \in A \cap B$, then $x \in A$. Either way $x \in A$.

($\supseteq$) Let $x \in A$. Either $x \in B$ or $x \notin B$. If $x \in B$, then $x \in A \cap B$. If $x \notin B$, then $x \in A \setminus B$. In both cases $x \in (A \setminus B) \cup (A \cap B)$.

The two inclusions give equality. $\blacksquare$

Check: $A = \{1, 2, 3\}$ and $B = \{2, 4\}$ give $\{1, 3\} \cup \{2\} = \{1, 2, 3\}$.

</details>

4\. Prove that $1 \cdot 2 + 2 \cdot 3 + \cdots + n(n + 1) = \frac{n(n + 1)(n + 2)}{3}$ for every integer $n \ge 1$.

<details class="solution" markdown>
<summary>Hint</summary>

Write $P(k)$ and $P(k + 1)$ on their own lines. The sum for $k + 1$ is the sum for $k$ plus one term.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

Induction: a statement for every $n \ge 1$ about a sum that grows by one term.

*Proof.* By induction on $n$.

Base case, $n = 1$: the left side is $1 \cdot 2 = 2$ and the right side is $\frac{1 \cdot 2 \cdot 3}{3} = 2$.

Inductive step. Let $k \ge 1$ and suppose $1 \cdot 2 + \cdots + k(k + 1) = \frac{k(k + 1)(k + 2)}{3}$. We must show that $1 \cdot 2 + \cdots + (k + 1)(k + 2) = \frac{(k + 1)(k + 2)(k + 3)}{3}$. Peeling off the last term and using the hypothesis,

$$
\frac{k(k + 1)(k + 2)}{3} + (k + 1)(k + 2) = (k + 1)(k + 2)\left(\frac{k}{3} + 1\right) = \frac{(k + 1)(k + 2)(k + 3)}{3}.
$$

By induction, the formula holds for every $n \ge 1$. $\blacksquare$

Check: $n = 3$ gives $2 + 6 + 12 = 20$ and $\frac{3 \cdot 4 \cdot 5}{3} = 20$.

</details>

5\. Define a relation $R$ on $\mathbb{Z}$ by $a \mathrel{R} b$ when $3 \mid a - b$. Prove that $R$ is an equivalence relation, and describe its equivalence classes.

<details class="solution" markdown>
<summary>Hint</summary>

Three properties, each started from its own hypothesis. For the classes, ask what remainders a division by 3 can leave.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

An equivalence relation is proved by checking the three properties from the definition.

*Proof.* Reflexive: for an integer $a$, $a - a = 0 = 3 \cdot 0$, so $a \mathrel{R} a$. Symmetric: suppose $a \mathrel{R} b$, so $a - b = 3k$ for an integer $k$. Then $b - a = 3(-k)$, so $b \mathrel{R} a$. Transitive: suppose $a \mathrel{R} b$ and $b \mathrel{R} c$, so $a - b = 3k$ and $b - c = 3l$. Then $a - c = (a - b) + (b - c) = 3(k + l)$, so $a \mathrel{R} c$.

Classes. Every integer $a$ can be written $a = 3q + r$ with $r \in \{0, 1, 2\}$, and then $a - r = 3q$, so $a \mathrel{R} r$. So every class contains one of $0$, $1$, $2$. These three classes are different, because $1 - 0$, $2 - 0$ and $2 - 1$ are not divisible by 3. So there are exactly three classes: the multiples of 3, the integers one more than a multiple of 3, and the integers two more. $\blacksquare$

Check: $7 \mathrel{R} 1$ since $7 - 1 = 6$, and $-2 \mathrel{R} 1$ since $-2 - 1 = -3$.

</details>

6\. Prove that the function $f \colon \mathbb{R} \to \mathbb{R}$ given by $f(x) = 3x - 7$ is a bijection.

<details class="solution" markdown>
<summary>Hint</summary>

Bijective means injective and surjective. For injective, start from equal outputs. For surjective, solve $f(x) = y$ and check the answer is in the domain.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

The definitions of injective and surjective, each with its own template.

*Proof.* Injective: suppose $f(a) = f(a')$. Then $3a - 7 = 3a' - 7$, so $3a = 3a'$ and $a = a'$.

Surjective: let $y \in \mathbb{R}$. Put $x = \frac{y + 7}{3}$, which is a real number. Then $f(x) = 3 \cdot \frac{y + 7}{3} - 7 = y$.

So $f$ is injective and surjective, hence bijective. $\blacksquare$

Check: $f(4) = 5$, and the formula gives $\frac{5 + 7}{3} = 4$.

</details>

### Standard

7\. Prove that for every integer $n$, the number $n^2 + 2$ is not divisible by 4.

<details class="solution" markdown>
<summary>Hint</summary>

Split by the parity of $n$ and look at the remainder of $n^2 + 2$ on division by 4 in each case.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A proof by cases: parity splits an arbitrary integer into two cases that make the squares concrete.

*Proof.* Let $n$ be an integer. Every integer is even or odd, so there are two cases.

If $n = 2k$, then $n^2 + 2 = 4k^2 + 2 = 4(k^2) + 2$, which has remainder 2 on division by 4.

If $n = 2k + 1$, then $n^2 + 2 = 4k^2 + 4k + 3 = 4(k^2 + k) + 3$, which has remainder 3 on division by 4.

The remainder is never 0, so $4 \nmid n^2 + 2$. $\blacksquare$

Check: $n = 3$ gives $11 = 4 \cdot 2 + 3$ and $n = 4$ gives $18 = 4 \cdot 4 + 2$.

</details>

8\. Prove that $\log_2 3$ is irrational.

<details class="solution" markdown>
<summary>Hint</summary>

If $\log_2 3 = \frac{a}{b}$, what equation do you get by raising 2 to both sides, and what do you know about the parities of powers of 2 and of 3?

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A proof by contradiction: the claim is negative ("irrational"), and the negation gives something to compute with.

*Proof.* Suppose, for contradiction, that $\log_2 3$ is rational. Since $3 > 1$, we have $\log_2 3 > 0$, so $\log_2 3 = \frac{a}{b}$ for positive integers $a$ and $b$. Then $2^{a/b} = 3$. Raising both sides to the power $b$ gives $2^a = 3^b$.

The left side is even, since $a \ge 1$. The right side is odd, since it is a product of copies of the odd number 3 (a product of odd integers is odd). A number cannot be both even and odd, which is a contradiction. So $\log_2 3$ is irrational. $\blacksquare$

Check: $\log_2 3 \approx 1.585$, and no small pair works, for instance $2^3 = 8$ and $3^2 = 9$.

</details>

9\. Prove that for every real number $x$, $\lvert x - 3 \rvert < 2$ if and only if $1 < x < 5$.

<details class="solution" markdown>
<summary>Hint</summary>

Two directions, each starting from its own hypothesis. In each, the absolute value needs a split on the sign of $x - 3$.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A biconditional, so two implications, and each one uses cases on the sign of $x - 3$.

*Proof.* ($\Rightarrow$) Suppose $\lvert x - 3 \rvert < 2$. If $x \ge 3$, then $\lvert x - 3 \rvert = x - 3 < 2$, so $x < 5$, and $x \ge 3 > 1$. If $x < 3$, then $\lvert x - 3 \rvert = 3 - x < 2$, so $x > 1$, and $x < 3 < 5$. In both cases $1 < x < 5$.

($\Leftarrow$) Suppose $1 < x < 5$. If $x \ge 3$, then $\lvert x - 3 \rvert = x - 3 < 5 - 3 = 2$. If $x < 3$, then $\lvert x - 3 \rvert = 3 - x < 3 - 1 = 2$. In both cases $\lvert x - 3 \rvert < 2$. $\blacksquare$

Check: $x = 4$ gives $1 < 2$. The endpoint $x = 5$ gives $\lvert 2 \rvert = 2$, which is not less than 2, and $5$ is not less than 5, so both sides fail together.

</details>

10\. Prove that the equation $x^3 + x = 5$ has exactly one real solution.

<details class="solution" markdown>
<summary>Hint</summary>

Existence: look for two values where $x^3 + x - 5$ has opposite signs, and use the intermediate value theorem. Uniqueness: assume two solutions $a < b$ and compare $a^3 + a$ with $b^3 + b$.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

Existence and uniqueness: two separate parts. Existence is non-constructive (the intermediate value theorem), and uniqueness assumes two solutions.

*Proof.* Let $f(x) = x^3 + x - 5$. A solution of the equation is a root of $f$.

Existence. The function $f$ is continuous, $f(1) = -3 < 0$ and $f(2) = 5 > 0$. By the intermediate value theorem, $f$ has a root between 1 and 2.

Uniqueness. Suppose $a$ and $b$ are roots with $a < b$. Then $b^3 - a^3 = (b - a)(b^2 + ab + a^2)$, and $b^2 + ab + a^2 = \left(a + \frac{b}{2}\right)^2 + \frac{3b^2}{4}$. This is positive, because it is a sum of two non-negative terms and is 0 only if $a = b = 0$, which $a < b$ rules out. So $b^3 > a^3$, and then $b^3 + b > a^3 + a$. But both sides equal 5, a contradiction. So there is at most one root, and with existence, exactly one. $\blacksquare$

Check: the root is $x \approx 1.516$, and $1.516^3 + 1.516 \approx 3.484 + 1.516 = 5.000$.

</details>

11\. Prove that every integer $n \ge 12$ can be written as $4a + 5b$ for some integers $a, b \ge 0$.

<details class="solution" markdown>
<summary>Hint</summary>

Write the first few cases by hand: $12, 13, 14, 15, 16$. Which earlier case does $16$ reduce to?

</details>

<details class="solution" markdown>
<summary>Solution</summary>

Strong induction: the step for $n$ reaches back four places, to $n - 4$, so four base cases are needed.

*Proof.* By strong induction on $n \ge 12$.

Base cases: $12 = 4 \cdot 3$, $13 = 4 \cdot 2 + 5$, $14 = 4 + 5 \cdot 2$ and $15 = 5 \cdot 3$.

Inductive step. Let $n \ge 16$ and suppose the claim holds for every integer $m$ with $12 \le m < n$. Then $m = n - 4$ satisfies $12 \le n - 4 < n$, so $n - 4 = 4a + 5b$ with $a, b \ge 0$. Then $n = 4(a + 1) + 5b$, with $a + 1 \ge 0$.

By strong induction, the claim holds for every $n \ge 12$. $\blacksquare$

Check: $n = 23$ gives $23 = 4 \cdot 2 + 5 \cdot 3$. The bound is sharp: $11$ is not of the form $4a + 5b$.

</details>

12\. A *full binary tree* is either a single node, or a new root node joined to two full binary trees. Prove that every full binary tree has an odd number of nodes.

<details class="solution" markdown>
<summary>Hint</summary>

The definition has two clauses, so the proof has two parts. Let $n(T)$ be the number of nodes of $T$ and count the nodes of the second kind of tree using its two subtrees.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

Structural induction, because the set is defined recursively with one basis clause and one recursive clause.

*Proof.* By structural induction on the tree $T$. Let $n(T)$ be the number of nodes.

Basis. A single node has $n(T) = 1$, which is odd.

Recursive clause. Let $T$ consist of a root joined to full binary trees $T_1$ and $T_2$, and suppose $n(T_1)$ and $n(T_2)$ are odd. Then $n(T) = 1 + n(T_1) + n(T_2)$. A sum of two odd numbers is even, and one more is odd, so $n(T)$ is odd.

Every full binary tree is built from the basis by the recursive clause, so every one has an odd number of nodes. $\blacksquare$

Check: a root with two leaves has $3$ nodes. Joining that tree and a leaf under a new root gives $1 + 3 + 1 = 5$.

</details>

13\. On $\mathbb{N} \times \mathbb{N}$ define $(a, b) \preceq (c, d)$ to mean $a \le c$ and $b \le d$. Prove that $\preceq$ is a partial order, and that it is not a total order.

<details class="solution" markdown>
<summary>Hint</summary>

A partial order is reflexive, antisymmetric and transitive. To show it is not total, find two pairs where neither is below the other.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

The definition of a partial order gives three checks, and a disproof (one example) settles "not total".

*Proof.* Reflexive: $a \le a$ and $b \le b$, so $(a, b) \preceq (a, b)$. Antisymmetric: suppose $(a, b) \preceq (c, d)$ and $(c, d) \preceq (a, b)$. Then $a \le c$ and $c \le a$, so $a = c$, and similarly $b = d$, so $(a, b) = (c, d)$. Transitive: suppose $(a, b) \preceq (c, d)$ and $(c, d) \preceq (e, f)$. Then $a \le c \le e$ and $b \le d \le f$, so $(a, b) \preceq (e, f)$.

Not total: take $(1, 0)$ and $(0, 1)$. In the first coordinate $1 \not\le 0$, so $(1, 0) \not\preceq (0, 1)$. In the second coordinate $1 \not\le 0$, so $(0, 1) \not\preceq (1, 0)$. These two pairs are incomparable. $\blacksquare$

Check: $(2, 3) \preceq (2, 5)$ is true, and $(2, 3)$ and $(3, 2)$ are incomparable.

</details>

14\. Let $f \colon A \to B$ and $g \colon B \to C$ be functions. Prove that if $g \circ f$ is surjective, then $g$ is surjective. Give an example where $g \circ f$ is surjective and $f$ is not.

<details class="solution" markdown>
<summary>Hint</summary>

Start with an arbitrary $c \in C$. The hypothesis gives an element of $A$; where does $f$ send it?

</details>

<details class="solution" markdown>
<summary>Solution</summary>

The definition of surjective, started from an arbitrary element of the codomain, plus a small example for the second part.

*Proof.* Let $c \in C$. Since $g \circ f$ is surjective, there is $a \in A$ with $g(f(a)) = c$. Put $b = f(a)$, an element of $B$. Then $g(b) = c$. So every $c \in C$ has a preimage under $g$, and $g$ is surjective. $\blacksquare$

Example. Let $A = \{1\}$, $B = \{1, 2\}$, $C = \{1\}$, with $f(1) = 1$ and $g(1) = g(2) = 1$. Then $g \circ f(1) = 1$, so $g \circ f$ is surjective onto $C$. But $f$ misses $2 \in B$, so $f$ is not surjective.

Check: in the example, $b = f(1) = 1$ and $g(1) = 1 = c$.

</details>

15\. Prove or disprove: for all sets $A$, $B$, $C$, $A \setminus (B \setminus C) = (A \setminus B) \setminus C$.

<details class="solution" markdown>
<summary>Hint</summary>

Try $\emptyset$ and one-element sets first. Let $x \in A \setminus (B \setminus C)$ and ask what you know about $x$ and $C$.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

The statement is false, so the method is a counterexample. Small cases with an empty set find it.

*Disproof.* Take $A = \{1\}$, $B = \emptyset$ and $C = \{1\}$. Then $B \setminus C = \emptyset$, so $A \setminus (B \setminus C) = \{1\}$. And $A \setminus B = \{1\}$, so $(A \setminus B) \setminus C = \emptyset$. The two sides are $\{1\}$ and $\emptyset$, which are different. $\blacksquare$

Why it fails: an element $x$ of the left side has $x \in A$ and either $x \notin B$ or $x \in C$. The right side keeps only the $x \in A$ with $x \notin B$ and $x \notin C$. So an element of $A \cap C$ is on the left whatever $B$ is, and never on the right.

Check: $1 \in A$, $1 \in C$ and $1 \notin B$. The element $1$ is on the left because $1 \notin B \setminus C$, and not on the right because $1 \in C$.

</details>

16\. For an integer $a$, let $[a]_5$ be the class of $a$ modulo 5. Prove that the rule $F([a]_5) = [a^2 + a]_5$ defines a function $\mathbb{Z}_5 \to \mathbb{Z}_5$.

<details class="solution" markdown>
<summary>Hint</summary>

The rule is written with a representative $a$. Take two names for the same class and show the outputs agree.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A well-definedness proof: the rule uses a representative, so the output must not depend on which representative.

*Proof.* Suppose $[a]_5 = [a']_5$. Then $a' = a + 5j$ for some integer $j$. Compute

$$
a'^2 + a' - (a^2 + a) = (a + 5j)^2 + (a + 5j) - a^2 - a = 10aj + 25j^2 + 5j = 5(2aj + 5j^2 + j).
$$

Since $2aj + 5j^2 + j$ is an integer, $5 \mid (a'^2 + a') - (a^2 + a)$, so $[a'^2 + a']_5 = [a^2 + a]_5$. The output is the same for every representative, so $F$ is well defined. $\blacksquare$

Check: $[1]_5 = [6]_5$, and $1^2 + 1 = 2$ while $6^2 + 6 = 42 = 5 \cdot 8 + 2$, so both give $[2]_5$.

</details>

17\. The Python function below is meant to return the largest element of a non-empty list. Prove that it does, for every non-empty list.

```python
def mx(xs):
    if len(xs) == 1:
        return xs[0]
    m = mx(xs[1:])
    return xs[0] if xs[0] > m else m
```

<details class="solution" markdown>
<summary>Hint</summary>

Induct on the length of the list. In the recursive call, what is the length of `xs[1:]`, and what does the last line compute?

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A recursive function is proved correct by induction on the size of its input: the base branch is the base case, and the recursive call is on a smaller input.

*Proof.* Let $P(n)$ be the statement "for every list of length $n$, `mx` returns its largest element", for $n \ge 1$. We use induction on $n$.

Base case, $n = 1$: the list is `[x]`, the function returns `xs[0]`, which is its only and largest element.

Inductive step. Let $k \ge 1$ and suppose $P(k)$. Let `xs` have length $k + 1$. The slice `xs[1:]` has length $k$ and is non-empty, so by $P(k)$ the call returns $m$, the largest element of `xs[1:]`. The last line returns `xs[0]` if `xs[0] > m`, and $m$ otherwise. The elements of `xs` are `xs[0]` together with those of `xs[1:]`. If `xs[0] > m`, then `xs[0]` is larger than every element of `xs[1:]` and is the largest. Otherwise `xs[0]` $\le m$, and $m$ is at least `xs[0]` and at least every element of `xs[1:]`, so it is the largest. In both cases the function returns the largest element of `xs`.

By induction, `mx` is correct for every non-empty list. $\blacksquare$

Check: `mx([3, 9, 2])` calls `mx([9, 2])`, which calls `mx([2])` $= 2$, returns $9$, and then returns $9$ because $3 > 9$ is false.

</details>

### Challenge

18\. Prove that the function below returns $b^e$ for every integer $b$ and every integer $e \ge 0$.

```python
def power(b, e):
    r, x, k = 1, b, e
    while k > 0:
        if k % 2 == 1:
            r = r * x
        x = x * x
        k = k // 2
    return r
```

<details class="solution" markdown>
<summary>Hint</summary>

Find a quantity built from `r`, `x` and `k` that the loop does not change and that equals $b^e$ at the start. Then show it is kept by one pass for odd `k` and for even `k` separately.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A loop invariant: a statement true before the loop, kept by each pass, and strong enough at exit. Inside the step there is a proof by cases on the parity of `k`.

The invariant is $r \cdot x^k = b^e$.

*Proof.* Before the loop: $r = 1$, $x = b$ and $k = e$, so $r \cdot x^k = b^e$.

One pass keeps it. Suppose $r \cdot x^k = b^e$ at the start of a pass with $k > 0$, and let $r', x', k'$ be the values at the end.

If $k$ is odd, then $r' = rx$, $x' = x^2$ and $k' = \frac{k - 1}{2}$ (floor division of an odd number). So $r' x'^{k'} = rx \cdot x^{k - 1} = rx^k = b^e$.

If $k$ is even, then $r' = r$, $x' = x^2$ and $k' = \frac{k}{2}$. So $r' x'^{k'} = r \cdot x^k = b^e$.

The loop stops. Each pass replaces a positive integer $k$ by a strictly smaller non-negative integer, since $\lfloor k / 2 \rfloor < k$ for $k > 0$, so $k$ reaches 0 after finitely many passes.

At exit, $k = 0$, so the invariant says $r \cdot x^0 = r = b^e$. The function returns $b^e$. $\blacksquare$

Check: `power(3, 5)`: start $(r, x, k) = (1, 3, 5)$; after pass 1 $(3, 9, 2)$; pass 2 $(3, 81, 1)$; pass 3 $(243, 6561, 0)$. Returns $243 = 3^5$, and each state has $r \cdot x^k = 243$ ($3 \cdot 9^2$, $3 \cdot 81$, $243$).

</details>

19\. Prove that the set of all finite subsets of $\mathbb{N}$ is countably infinite.

<details class="solution" markdown>
<summary>Hint</summary>

Send a finite set $S$ to the number $\sum_{s \in S} 2^s$ (binary notation: which bits are on). To show two different sets give different numbers, look at the largest element on which they differ.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

Countability by an injection into $\mathbb{N}$. Injectivity is proved by comparing the two sums at the largest element where the sets differ, and the symmetry of the claim makes WLOG legitimate.

*Proof.* Let $\mathcal{F}$ be the set of finite subsets of $\mathbb{N}$. Define $f \colon \mathcal{F} \to \mathbb{N}$ by $f(S) = \sum_{s \in S} 2^s$, with $f(\emptyset) = 0$.

The map $f$ is injective. Let $S \ne T$ be finite sets. Their symmetric difference is non-empty and finite, so it has a largest element $m$. The statement "$f(S) \ne f(T)$" is unchanged if $S$ and $T$ are swapped, so we may assume without loss of generality that $m \in S$ and $m \notin T$. Above $m$, the sets $S$ and $T$ have the same elements, so those terms cancel in $f(S) - f(T)$. Then

$$
f(S) - f(T) = 2^m + \sum_{s \in S,\, s < m} 2^s - \sum_{t \in T,\, t < m} 2^t \ge 2^m - \sum_{t=0}^{m-1} 2^t = 2^m - (2^m - 1) = 1 > 0.
$$

So $f(S) \ne f(T)$.

An injection into $\mathbb{N}$ makes $\mathcal{F}$ countable. It is infinite, because the sets $\{0\}, \{1\}, \{2\}, \dots$ are all different elements of $\mathcal{F}$. An infinite set that injects into $\mathbb{N}$ is countably infinite. $\blacksquare$

Check: the sets with elements in $\{0, 1, 2, 3\}$ are sent to $0, 1, \dots, 15$ exactly once each, for example $\{0, 2\} \mapsto 5$ and $\{1, 3\} \mapsto 10$.

</details>

20\. Prove that if 11 distinct integers are chosen from $\{1, 2, \dots, 20\}$, then one of the chosen numbers divides another.

<details class="solution" markdown>
<summary>Hint</summary>

Every positive integer can be written as $2^i \cdot m$ with $m$ odd. How many possible values of $m$ are there below 20? Think of them as boxes.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

The pigeonhole principle, once the right boxes are found. The boxes come from the odd part of a number.

*Proof.* Write each chosen number as $2^i m$, where $i \ge 0$ and $m$ is odd. Because the number is at most 20, $m$ is one of the 10 odd numbers $1, 3, 5, \dots, 19$. These are the boxes. There are 11 chosen numbers and 10 boxes, so two different chosen numbers have the same odd part $m$: say $2^i m$ and $2^j m$. They are different numbers, so $i \ne j$, and we may assume $i < j$ (the statement "one divides the other" is symmetric in the two). Then $2^j m = 2^{j - i} \cdot 2^i m$ with $j - i \ge 1$ an integer, so $2^i m$ divides $2^j m$. $\blacksquare$

Check: ten numbers can avoid it, for example $11, 12, \dots, 20$ (none divides another, since the larger of two is less than twice the smaller). Adding any number from $1$ to $10$ creates a pair, because it has a multiple among $11, \dots, 20$; adding $5$ gives $5 \mid 15$.

</details>

21\. Let $S$ be a finite set with $n \ge 1$ elements. Prove that $S$ has as many subsets of even size as subsets of odd size.

<details class="solution" markdown>
<summary>Hint</summary>

Fix one element $x_0$ of $S$. Build a function from the even-sized subsets to the odd-sized subsets by adding or removing $x_0$.

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A counting argument by bijection: two sets have the same size if a bijection joins them.

*Proof.* Let $E$ be the set of subsets of $S$ of even size and $O$ the set of subsets of odd size. Fix an element $x_0 \in S$ (possible since $n \ge 1$). For a subset $T \subseteq S$, define $\varphi(T) = T \setminus \{x_0\}$ if $x_0 \in T$, and $\varphi(T) = T \cup \{x_0\}$ if $x_0 \notin T$.

In either case $\varphi(T)$ has exactly one element more or one fewer than $T$, so its size has the opposite parity. So $\varphi$ sends $E$ into $O$ and $O$ into $E$. Applying $\varphi$ twice adds and then removes $x_0$ (or the reverse), which returns $T$, so $\varphi(\varphi(T)) = T$. Hence the restriction $\varphi \colon E \to O$ has the inverse $\varphi \colon O \to E$, and it is a bijection. So $\lvert E \rvert = \lvert O \rvert$. $\blacksquare$

Check: $S = \{1, 2, 3\}$. Even-sized: $\emptyset$, $\{1,2\}$, $\{1,3\}$, $\{2,3\}$, which is 4. Odd-sized: $\{1\}$, $\{2\}$, $\{3\}$, $\{1,2,3\}$, which is 4. With $x_0 = 1$, $\varphi(\emptyset) = \{1\}$ and $\varphi(\{2,3\}) = \{1,2,3\}$. Each is half of $2^3 = 8$.

</details>

22\. Let $c_n$ be the number of binary strings of length $n$ with no two consecutive 1s. Prove that $c_n = F_{n+2}$ for every $n \ge 1$, where $F_1 = F_2 = 1$ and $F_k = F_{k-1} + F_{k-2}$ for $k \ge 3$.

<details class="solution" markdown>
<summary>Hint</summary>

Sort the valid strings of length $n$ by their last bit. What can precede a final 1? What can precede a final 0?

</details>

<details class="solution" markdown>
<summary>Solution</summary>

A counting argument that produces a recurrence, followed by strong induction to match it with the Fibonacci numbers.

*Proof.* First, the recurrence. Let $n \ge 3$. A valid string of length $n$ ends in 0 or in 1.

If it ends in 0, the first $n - 1$ bits can be any valid string of length $n - 1$, and every valid string of length $n - 1$ followed by 0 is valid. That gives $c_{n-1}$ strings.

If it ends in 1, the bit before it must be 0, and the first $n - 2$ bits can be any valid string of length $n - 2$. Every valid string of length $n - 2$ followed by $01$ is valid. That gives $c_{n-2}$ strings.

The two kinds are different, so $c_n = c_{n-1} + c_{n-2}$ for $n \ge 3$.

Now the induction. Base cases: the valid strings of length 1 are $0$ and $1$, so $c_1 = 2 = F_3$. Those of length 2 are $00$, $01$ and $10$, so $c_2 = 3 = F_4$. Step: let $n \ge 3$ and suppose $c_{n-1} = F_{n+1}$ and $c_{n-2} = F_n$. Then $c_n = c_{n-1} + c_{n-2} = F_{n+1} + F_n = F_{n+2}$. By strong induction, $c_n = F_{n+2}$ for every $n \ge 1$. $\blacksquare$

Check: $c_3 = c_2 + c_1 = 5$, and the valid strings of length 3 are $000, 001, 010, 100, 101$, five of them, with $F_5 = 5$. Also $c_5 = 13 = F_7$.

</details>

## Where this shows up

- Discrete math and algorithms problem sets are built from these shapes: an induction, a loop invariant, a counting argument, a set or function proof. The loop invariant in problem 18 is the model for correctness proofs in invariants and algorithm correctness<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->, and problem 20 is a first use of the counting tools in inclusion-exclusion and the pigeonhole principle<!-- link: ../../06-cs-math/03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md -->.
- In linear algebra, the proofs are the same shapes: a bijection is a proof by definition (problem 6), a kernel is a set whose equality needs two inclusions (linear transformations, kernel and image<!-- link: ../../05-university-core/06-linear-algebra/05-linear-transformations-kernel-and-image.md -->), and "exactly one solution" is existence and uniqueness (problem 10).
- In the theory of computation, countability and diagonal arguments (problem 19 and [cardinality and countability](../06-relations-and-functions/06-cardinality-and-countability.md)) lead to decidability and the halting problem<!-- link: ../../06-cs-math/06-theory-of-computation/05-decidability-and-the-halting-problem.md -->.
- Return to [common proof mistakes](01-common-proof-mistakes.md) to check your own answers against the list.
