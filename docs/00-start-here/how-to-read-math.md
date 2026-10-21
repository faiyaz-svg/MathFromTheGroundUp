# How to read math

After this page you can read a definition, a theorem, a line of notation and a worked example actively, and you know what to do when one line stops you.

A page of math holds more than a page of almost anything else you read. Every word of a definition matters, a theorem can depend on a condition stated once at the top, and one line of notation can stand for a whole sentence. If you read it like a novel, at a steady speed from top to bottom, you finish with the feeling of having understood and very little you can use. The routines below slow you down in the places that need it.

## Reading a definition

A definition gives a name to everything that meets a list of conditions. Many mistakes in proofs start with a definition that was only half remembered, so read each one with a pencil in hand:

1. Read it once, slowly, all the way through.
2. Find each condition and write it on its own line. Watch the small words: "and", "or", "for every", "there exists", "unique", "positive".
3. Build an example: something that meets every condition. Check the conditions one at a time.
4. Build a non-example: something that fails exactly one condition. If you can, find one for each condition, because each one shows you why that condition is there.
5. Say the definition in your own words. Then compare your version with the original and check that you haven't dropped a condition.

<div class="example" markdown>

### Example 1: the definition of a prime

Definition: an integer $n$ is prime if $n > 1$ and the only positive divisors of $n$ are $1$ and $n$.

Step 2: there are three conditions.

- (a) The number $n$ is an integer.
- (b) It is greater than $1$.
- (c) Its only positive divisors are $1$ and $n$.

Step 3: the number $7$ is an integer, it is greater than $1$, and its positive divisors are $1$ and $7$. All three conditions hold, so $7$ is prime.

Step 4: one non-example for each condition.

| Candidate | Condition it fails | Why |
|---|---|---|
| $7.5$ | (a) | It is not an integer. |
| $1$ | (b) | The statement $1 > 1$ is false. |
| $9$ | (c) | The number $3$ is also a positive divisor of $9$. |

Step 5: "a prime is a whole number bigger than $1$ that has no positive divisors except $1$ and itself." Compare with the original: "whole number" covers (a) and "bigger than $1$" covers (b). Condition (b) is the one people drop. Without it, $1$ would count as prime, because its only positive divisor is $1$ itself.

</div>

<div class="note" markdown>

In a definition, "if" means "exactly when". The definition above also tells you that a number failing even one of the conditions is not prime. In a theorem, "if" keeps its usual one-way meaning.

</div>

## Reading a theorem

A theorem says that when certain conditions hold, something else must follow. The **hypotheses** of a theorem are the conditions it assumes. In plain words, they are what you are given. The **conclusion** is the statement that follows from the hypotheses: what the theorem promises you.

1. Split the statement into hypotheses and conclusion. Look for "if ... then", "let", "suppose" and "for every", and for conditions set up earlier on the page. A line such as "Let $G$ be a connected graph" is a hypothesis too.
2. Test it on a small case where you can work out both sides.
3. Test an edge case: equality, zero, the smallest value allowed.
4. Drop one hypothesis at a time and look for a case where the conclusion fails. That case shows what the hypothesis is for.
5. Ask whether the converse holds. The **converse** of "if $P$, then $Q$" is the statement "if $Q$, then $P$". In plain words, it swaps the hypothesis and the conclusion. It is a different statement, and it is often false.

<div class="example" markdown>

### Example 2: a theorem about two averages

Theorem: if $a$ and $b$ are nonnegative real numbers, then

$$
\sqrt{ab} \le \frac{a + b}{2}.
$$

Step 1: the hypotheses are that $a$ and $b$ are real numbers and that both are nonnegative. The conclusion is the inequality: the square root of the product is at most the ordinary average.

Step 2: take $a = 4$ and $b = 9$. The left side is $\sqrt{36} = 6$ and the right side is $\frac{13}{2} = 6.5$, and $6 \le 6.5$ holds.

Step 3: take $a = b = 5$. Both sides equal $5$, so the inequality can be an equality.

Step 4: drop "nonnegative" and take $a = b = -1$. The left side is $\sqrt{1} = 1$, the right side is $-1$, and $1 \le -1$ is false. So the theorem needs that hypothesis.

Step 5: this theorem has no natural converse to test, so here is a smaller one. "If $n$ is divisible by $4$, then $n$ is even" is true. Its converse, "if $n$ is even, then $n$ is divisible by $4$", is false: the number $6$ is even and $6 \div 4$ leaves remainder $2$.

</div>

A proof is read the same way, one line at a time, with one more question at each line: which hypothesis or earlier result does this line use? The lesson [how to read a proof](../04-proofs-and-logic/03-core-proof-methods/02-how-to-read-a-proof.md) in 04-proofs-and-logic practises this.

## Reading notation

Notation squeezes a sentence into a few symbols. To read it:

1. Say each symbol out loud as words. If you can't say a symbol, look it up before you go on.
2. Unpack nested notation from the inside out: first the innermost expression, then whatever acts on it.
3. Write out the first few terms or members, and the last one if there is one.

These are the symbols you will meet most often in the first university courses:

| Symbol | Say it |
|---|---|
| $x \in A$ | $x$ is an element of $A$, or $x$ is in $A$ |
| $A \subseteq B$ | $A$ is a subset of $B$ |
| $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ | the natural numbers, the integers, the rational numbers, the real numbers |
| $\{x \in A : \ldots\}$ | the set of $x$ in $A$ such that ... |
| $\sum_{i=1}^{n}$ | the sum, for $i$ from $1$ to $n$, of ... |
| $a \mid b$ | $a$ divides $b$ |
| $\forall$, $\exists$ | for every, there exists |
| $\Rightarrow$, $\iff$ | implies, if and only if |
| $f : A \to B$ | $f$ is a function from $A$ to $B$ |

Watch out for $\mathbb{N}$: some books include $0$ in the natural numbers and some don't, so check the convention at the start of the book or course. The full list, with the Greek alphabet, is on the [symbols and notation](../reference/symbols-and-notation.md) page.

<div class="example" markdown>

### Example 3: unpacking a sum

Read this expression:

$$
\sum_{i=1}^{n} (2i - 1)
$$

Step 1: say it as "the sum, for $i$ from $1$ to $n$, of $2i - 1$". The letter $i$ is the index, a counter that takes each whole-number value from $1$ to $n$ in turn.

Step 2: start inside. The formula $2i - 1$ gives $1$ when $i = 1$, then $3$ when $i = 2$, then $5$ when $i = 3$, so it produces the odd numbers. The $\Sigma$ outside adds them all up.

Step 3: write out the terms, including the last one, where $i = n$:

$$
\sum_{i=1}^{n} (2i - 1) = 1 + 3 + 5 + \cdots + (2n - 1)
$$

So the expression is the sum of the first $n$ odd numbers. For $n = 4$ it is $1 + 3 + 5 + 7 = 16$. Check: there are four terms, and the last is $2 \times 4 - 1 = 7$. The first [practice puzzle](problem-solving-playbook.md#practice-puzzles) in the playbook finds a formula for this sum.

</div>

<div class="example" markdown>

### Example 4: unpacking a set

Read this set:

$$
\{x \in \mathbb{Z} : x^2 < 10\}
$$

Step 1: say it as "the set of integers $x$ such that $x^2$ is less than $10$". The colon is read "such that". Some books use a vertical bar instead.

Step 2: start inside, with the condition $x^2 < 10$. The part before the colon says where $x$ comes from: the integers, so negative values count too.

Step 3: the squares $0$, $1$, $4$ and $9$ are less than $10$, and $16$ is not. The set is $\{-3, -2, -1, 0, 1, 2, 3\}$.

Check the ends: the member $-3$ has square $9$, which is less than $10$, and the next integer out, $-4$, has square $16$, which is not.

</div>

<div class="warning" markdown>

Watch out: the common wrong answer here is $\{0, 1, 2, 3\}$, which forgets the negative integers. The set before the colon matters. With $\mathbb{R}$ in place of $\mathbb{Z}$, the set is every real number strictly between $-\sqrt{10}$ and $\sqrt{10}$.

</div>

## Reading a worked example

A worked example teaches the most when you treat it as a problem first.

1. Read the problem, then stop. Try the first step yourself, or the whole problem if you can.
2. Cover the solution with a sheet of paper. Uncover one line at a time, and predict each line before you see it.
3. For each line, say what changed from the line before and which rule allows it. If you can't name the rule, that is the line to study. This is self-explanation, described in [how to study](how-to-study.md#explain-each-step-to-yourself).
4. At the end, close the example and solve the problem again on a blank page. Then do a practice problem of the same type.

A wrong prediction in step 2 is useful. It shows you exactly where your idea of the method differs from the book's.

## How fast to read

Math reads slowly. On hard material, a page an hour is a normal pace, and a short proof can take longer than the page around it. Keep paper beside you, and when the text says "so", "therefore" or "hence", work out the step yourself before you accept it.

You can speed up where you already know the material, and the quick check at the top of each lesson tells you where that is. Two signs that you are going too fast: you can't say what the last definition required, or you can't start the next example on your own.

## When you are stuck on a line

1. Find the exact line. Copy it and the line before it, one under the other.
2. Ask what changed between them: which terms moved, which were combined, which disappeared.
3. Look up every term and symbol in the line. Often the problem is a definition you have half forgotten.
4. Put a small number into both lines. If they give the same value, the step is right and you only need to find the rule. If they don't, you have misread something or the book has a typo.
5. Write in the missing steps. Authors skip steps they think of as routine, and filling them in is how you learn the routine.
6. If you are still stuck, mark the line and read on for a paragraph or two. The next lines often explain the step. Then come back.
7. Ask someone: a TA, a classmate, or Claude in VS Code. Bring the exact line and what you have tried.

<div class="example" markdown>

### Example 5: filling in a skipped step

This line comes from a proof by induction:

$$
\frac{n(n+1)}{2} + (n+1) = \frac{(n+1)(n+2)}{2}
$$

Step 4: put in $n = 3$. The left side is $6 + 4 = 10$ and the right side is $\frac{4 \times 5}{2} = 10$. They agree, so the step is right, and we only need to find the rule.

Step 5: write $n + 1$ as a fraction over $2$, add the fractions, then take out the common factor $n + 1$:

$$
\begin{aligned}
\frac{n(n+1)}{2} + (n+1) &= \frac{n(n+1)}{2} + \frac{2(n+1)}{2} \\
&= \frac{n(n+1) + 2(n+1)}{2} \\
&= \frac{(n+1)(n+2)}{2}
\end{aligned}
$$

Check: in the last line, multiplying out gives $(n+1)(n+2) = n(n+1) + 2(n+1)$, which matches the line above it.

</div>

## Exercises

### Exercise 1: a definition

A set $S$ of integers is closed under addition if for every $a$ and $b$ in $S$, the sum $a + b$ is also in $S$. List the conditions in this definition, then give two examples and one non-example. Is the empty set closed under addition?

<details class="solution" markdown>
<summary>Solution</summary>

The conditions are that $S$ is a set of integers, and that for every choice of $a$ and $b$ in $S$, the sum $a + b$ is in $S$. The choice $a = b$ is allowed, which is easy to miss.

Examples: the even integers, because $2j + 2k = 2(j + k)$ is even. The set $\{0\}$, because $0 + 0 = 0$. The set $\mathbb{Z}$ of all integers also works.

Non-example: the odd integers, because $1 + 1 = 2$ is not odd. A smaller one is $\{0, 1\}$, because $1 + 1 = 2$ is not in the set.

The empty set is closed under addition. It has no elements, so there is no pair $a$, $b$ that could fail the condition. A statement of the form "for every element of $S$, ..." is true when $S$ is empty; this is called vacuous truth, and it comes back in the [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md) lesson.

</details>

### Exercise 2: two sets

Rewrite each set in words, then list its members.

- (a) $\{n \in \mathbb{N} : n \mid 12\}$
- (b) $\{2k + 1 : k \in \mathbb{Z} \text{ and } 0 \le k \le 4\}$

<details class="solution" markdown>
<summary>Solution</summary>

(a) "The set of natural numbers $n$ such that $n$ divides $12$." The members are $1$, $2$, $3$, $4$, $6$ and $12$. Whether $\mathbb{N}$ includes $0$ doesn't matter here, because $0$ does not divide $12$: no integer $k$ gives $12 = 0 \times k$. Notice that the bar means "divides" here, which is one reason this book writes set-builder notation with a colon.

(b) "The set of numbers $2k + 1$, where $k$ is an integer from $0$ to $4$." This set is written differently: the expression before the colon is the form of each member, and the part after it says which values of $k$ to use. Putting in $k = 0, 1, 2, 3, 4$ gives $\{1, 3, 5, 7, 9\}$, the first five odd numbers.

Check: $k$ takes five values and the set has five members.

</details>

### Exercise 3: two sums

Unpack each sum from the inside out, then work it out.

- (a) $\sum_{k=0}^{3} 2^k$
- (b) $\sum_{i=1}^{3} \sum_{j=1}^{i} j$

<details class="solution" markdown>
<summary>Solution</summary>

(a) The index starts at $0$, so there are four terms: $2^0 + 2^1 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15$. Check: a sum of powers of $2$ starting at $1$ is one less than the next power, and $2^4 - 1 = 15$.

(b) Start with the inner sum. For a fixed $i$, the expression $\sum_{j=1}^{i} j$ means $1 + 2 + \cdots + i$. That gives $1$ for $i = 1$, then $3$ for $i = 2$, then $6$ for $i = 3$. The outer sum adds these: $1 + 3 + 6 = 10$.

Check: list every pair $(i, j)$ with $1 \le j \le i \le 3$. They are $(1,1)$, $(2,1)$, $(2,2)$, $(3,1)$, $(3,2)$ and $(3,3)$, and their $j$ values add to $1 + 1 + 2 + 1 + 2 + 3 = 10$.

</details>

### Exercise 4: a theorem

Theorem: if $n$ is a prime number and $n > 2$, then $n$ is odd. Find the hypotheses and the conclusion, test small cases, drop each hypothesis in turn, and decide whether the converse is true.

<details class="solution" markdown>
<summary>Solution</summary>

The hypotheses are that $n$ is prime and that $n > 2$. The conclusion is that $n$ is odd.

Small cases: the primes $3$, $5$, $7$ and $11$ are all odd.

Drop "$n > 2$": the number $2$ is prime and even, so the conclusion fails. Drop "prime": the number $4$ is greater than $2$ and even, so the conclusion fails again. Both hypotheses are needed.

The converse is "if $n$ is odd, then $n$ is prime and $n > 2$". It is false: the number $9$ is odd, but $9 = 3 \times 3$ is not prime.

Check: $9 \div 3 = 3$ with remainder $0$, so $3$ divides $9$.

</details>
