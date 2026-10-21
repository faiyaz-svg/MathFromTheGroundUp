# Mathematical induction

After this lesson you can prove a statement about every integer $n \ge n_0$ by induction: state $P(n)$ exactly, prove a base case, carry out the inductive step with the algebra written out, and spot the errors that make an induction proof worthless.

Before this: [direct proof](../03-core-proof-methods/01-direct-proof.md), [quantifiers](../02-logic-and-sets/04-quantifiers.md), [conditionals and biconditionals](../02-logic-and-sets/02-conditionals-and-biconditionals.md), [sequences and recursion](../../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md) and [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For the claim "for every integer $n \ge 1$, $1 + 3 + 5 + \cdots + (2n - 1) = n^2$", write the base case, the statement $P(k)$ and the statement $P(k + 1)$. Which of the two do you get to assume in the inductive step?
2. Let $P(n)$ be the statement "$n = n + 1$". A student proves that for every $k \ge 0$, if $P(k)$ is true then $P(k + 1)$ is true. Can the student conclude that $P(7)$ is true?
3. Compute $2^n$ and $n^2$ for $n = 0, 1, \dots, 6$. For which of these $n$ is $2^n > n^2$?

<details class="solution" markdown>
<summary>Answers</summary>

1. Base case ($n = 1$): $1 = 1^2$. The statement $P(k)$ is $1 + 3 + \cdots + (2k - 1) = k^2$, and $P(k + 1)$ is $1 + 3 + \cdots + (2k - 1) + (2k + 1) = (k + 1)^2$. You assume $P(k)$ and must prove $P(k + 1)$.
2. No. The step is true (add 1 to both sides of $k = k + 1$), but there is no base case, and $P(7)$ says $7 = 8$, which is false. A correct step with nothing to start from proves nothing.
3. The pairs $(2^n, n^2)$ are $(1, 0)$, $(2, 1)$, $(4, 4)$, $(8, 9)$, $(16, 16)$, $(32, 25)$ and $(64, 36)$. So $2^n > n^2$ for $n = 0, 1, 5, 6$ and fails for $n = 2, 3, 4$.

</details>

## The idea

The sequences lessons proved that $a_n = a_0 + nd$ and $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$, and each proof ended with the words "and so on for every $n$". Those words hide an infinite claim. A careful reader should ask what makes the "and so on" legitimate, and induction is the answer. It turns "and so on" into two finite checks.

Picture an endless row of dominoes, numbered $0, 1, 2, \dots$. You can't push each one. But two facts about the row are enough to knock them all down. First, domino 0 falls. Second, the dominoes are spaced so that whenever domino $k$ falls, it knocks over domino $k + 1$. The second fact is a rule about all the dominoes at once, and you check it once, in general, without waiting for any domino to fall.

```mermaid
flowchart LR
    B["P(0) is true<br/>(base case)"] -->|"step: P(0) implies P(1)"| P1["P(1) is true"]
    P1 -->|"step: P(1) implies P(2)"| P2["P(2) is true"]
    P2 -->|"step: P(2) implies P(3)"| P3["P(3) is true"]
    P3 -->|"and so on"| D["..."]
```

Now replace "domino $n$ falls" by "the statement $P(n)$ is true". The first fact becomes the **base case**, a check that $P(0)$ (or $P(1)$, or wherever the claim starts) is true. The second becomes the **inductive step**, a proof that for every $k$, if $P(k)$ is true then $P(k + 1)$ is true. In the step you do not prove that $P(k)$ is true. You prove the implication, so you are allowed to assume $P(k)$ while you prove $P(k + 1)$. That is not circular, for the same reason that proving "if it rains, the street gets wet" doesn't need rain: the implication is the thing proved.

### Why this is valid

There are three ways to see that the two facts really give $P(n)$ for every $n$, and each one is worth knowing.

The first is a chain. The base case gives $P(0)$. The step with $k = 0$ gives "if $P(0)$ then $P(1)$", so $P(1)$ is true. The step with $k = 1$ gives $P(2)$, and so on. For any particular $n$, such as 1,000,000, the chain reaches $P(n)$ after exactly $n$ steps. No single $n$ is out of reach, and every natural number is some finite number of steps from 0.

The second is a smallest counterexample. Suppose $P(n)$ fails for some $n$, and let $m$ be the smallest such $n$. It can't be 0, because the base case holds. So $m - 1$ is a natural number below $m$, and $P(m - 1)$ is true because $m$ is the smallest failure. But the step says $P(m - 1)$ implies $P(m)$, so $P(m)$ is true, a contradiction. This argument uses the fact that every nonempty set of natural numbers has a smallest member, the well-ordering principle of the [next lesson](02-strong-induction-and-well-ordering.md).

The third is that induction is part of what the natural numbers are. The set $\mathbb{N}$ is, by definition, the numbers you can reach from 0 by adding 1 finitely many times, and induction says that a property that holds at 0 and survives adding 1 holds for all of them. Most courses treat the principle as an axiom for this reason. You don't need to choose one view: they agree, and the first is the one to keep in your head when writing a proof.

## Definitions

Let $n_0$ be an integer, and let $P(n)$ be a statement that is true or false for each integer $n \ge n_0$ (an open sentence in $n$, as in the lesson on [quantifiers](../02-logic-and-sets/04-quantifiers.md)). The **principle of mathematical induction** says: if

- $P(n_0)$ is true, and
- for every integer $k \ge n_0$, the implication $P(k) \Rightarrow P(k + 1)$ is true,

then $P(n)$ is true for every integer $n \ge n_0$. When $n_0 = 0$ and the variables range over $\mathbb{N}$, the principle is the logical statement

$$
\bigl[P(0) \wedge \forall k\,\bigl(P(k) \Rightarrow P(k + 1)\bigr)\bigr] \Rightarrow \forall n\,P(n).
$$

In plain words: if the first domino falls, and each domino that falls knocks over the next, then every domino falls. The left side is two things to prove, and the right side is what you get for free.

The **base case** is the proof that $P(n_0)$ is true, for the first value $n_0$ in the claim. In plain words, it is the push that starts the chain.

The **inductive step** is the proof that $P(k) \Rightarrow P(k + 1)$ for an arbitrary integer $k \ge n_0$. The assumption that $P(k)$ is true is the **inductive hypothesis**. In plain words, the step is the spacing between dominoes, and the hypothesis is "domino $k$ has fallen".

The letter $k$ in the step and the letter $n$ in the claim have different jobs. The claim is about all $n$. The step fixes one arbitrary $k$ and talks about it and its successor. If you assumed $P(k)$ for every $k$, you would be assuming the conclusion.

## How to do it

### The six steps

1. State $P(n)$ in full, with the starting value $n_0$ and the kind of number $n$ is. "For every integer $n \ge 1$, $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$" is a statement. "The formula works" is not.
2. Prove the base case. Write out both sides of $P(n_0)$ with $n_0$ put in, and show they agree.
3. Write the inductive hypothesis: "Let $k \ge n_0$ and suppose $P(k)$." Write $P(k)$ out in full, on its own line, so you can point at it later.
4. Write the target. Write $P(k + 1)$ in full, on its own line, replacing every $n$ by $k + 1$ with brackets. This line is what you are aiming for, and it tells you which expression to build.
5. Prove the target. Start from one side of $P(k + 1)$, rewrite it until the expression in $P(k)$ appears, replace that expression using the hypothesis, and do the algebra until you reach the other side. Say where you use the hypothesis.
6. Conclude: "By induction, $P(n)$ holds for every integer $n \ge n_0$."

Here is the shape of the finished proof. Learn it well enough that you can write it from memory.

```text
Claim. For every integer n >= n0, P(n).

Proof. By induction on n.

Base case. For n = n0: [check P(n0)].

Inductive step. Let k >= n0 and suppose P(k): [write P(k)].
We must show P(k+1): [write P(k+1)].
[Rewrite so that P(k) appears, use the hypothesis, finish the algebra.]
So P(k+1) holds.

By induction, P(n) holds for every integer n >= n0.  []
```

### Finding where the hypothesis goes

Step 5 is where proofs are won or lost, and the question is always the same: where does $P(k)$ hide inside $P(k + 1)$? The table lists the usual answers.

| Kind of claim | What $P(k + 1)$ looks like | How to expose $P(k)$ |
|---|---|---|
| a sum up to $n$ | the same sum with one more term | peel off the last term: $\sum_{i=1}^{k+1} a_i = \sum_{i=1}^{k} a_i + a_{k+1}$ |
| divisibility, $d \mid f(n)$ | $f(k + 1)$ | write $f(k + 1) = c \cdot f(k) + (\text{something divisible by } d)$ |
| inequality, $f(n) > g(n)$ | $f(k + 1) > g(k + 1)$ | chain: $f(k + 1) = (\text{multiple of } f(k)) > \dots \ge g(k + 1)$ |
| a recurrence formula | $a_{k+1}$ in closed form | use the recurrence to write $a_{k+1}$ with $a_k$, then use the hypothesis for $a_k$ |

The next four examples use each row in turn.

## Worked examples

<div class="example" markdown>

### Example 1: the sum of the first $n$ integers

*Theorem 1.* For every integer $n \ge 1$,

$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}.
$$

What we know: the definition of $\sum$ as a running total, so that adding one more term to a sum is allowed. What we want: the formula for all $n \ge 1$. The plan: show it for $n = 1$, then show that adding the next integer to the right side of the formula for $k$ gives the right side of the formula for $k + 1$. The earlier lesson proved this by pairing the terms. Induction gives a second proof that needs no trick.

Step 1: $P(n)$ is the statement "$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$", and $n_0 = 1$.

*Proof.* Step 2, base case. For $n = 1$ the left side is $1$ and the right side is $\frac{1 \cdot 2}{2} = 1$. They agree.

Step 3, inductive hypothesis. Let $k \ge 1$ and suppose

$$
\sum_{i=1}^{k} i = \frac{k(k+1)}{2}.
$$

Step 4, target. We must show

$$
\sum_{i=1}^{k+1} i = \frac{(k+1)(k+2)}{2}.
$$

Step 5. Peel off the last term of the left side, use the hypothesis on the rest, and put everything over 2:

$$
\begin{aligned}
\sum_{i=1}^{k+1} i &= \sum_{i=1}^{k} i + (k + 1) \\
&= \frac{k(k+1)}{2} + (k + 1) \qquad \text{(hypothesis)} \\
&= \frac{k(k+1) + 2(k+1)}{2} \\
&= \frac{(k+1)(k+2)}{2}.
\end{aligned}
$$

The last line factors out the common $(k + 1)$. This is the target.

Step 6. By induction, the formula holds for every integer $n \ge 1$. $\blacksquare$

Look back: the hypothesis was used once, on the second line, and nothing else about $k$ was needed. Check with numbers: for $k = 4$ the hypothesis says $1 + 2 + 3 + 4 = 10 = \frac{4 \cdot 5}{2}$. Adding $k + 1 = 5$ gives 15, and the target says $\frac{5 \cdot 6}{2} = 15$.

</div>

<div class="example" markdown>

### Example 2: the sum of the first $n$ squares

*Theorem 2.* For every integer $n \ge 1$,

$$
\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}.
$$

The telescoping proof in the earlier lesson had to be invented. With induction you only need the formula, which can come from a guess, a table or a textbook. Proof strategy: the same as Example 1, with more algebra.

*Proof.* Base case ($n = 1$): the left side is $1^2 = 1$ and the right side is $\frac{1 \cdot 2 \cdot 3}{6} = 1$.

Inductive hypothesis: let $k \ge 1$ and suppose $\sum_{i=1}^{k} i^2 = \frac{k(k+1)(2k+1)}{6}$.

Target: $\sum_{i=1}^{k+1} i^2 = \frac{(k+1)(k+2)(2k+3)}{6}$. (Replace $n$ by $k + 1$ everywhere: $n + 1$ becomes $k + 2$, and $2n + 1$ becomes $2(k + 1) + 1 = 2k + 3$.)

Peel off the last term and use the hypothesis:

$$
\sum_{i=1}^{k+1} i^2 = \sum_{i=1}^{k} i^2 + (k+1)^2 = \frac{k(k+1)(2k+1)}{6} + (k+1)^2.
$$

Both terms contain the factor $k + 1$. Factor it out, with a common denominator of 6:

$$
\frac{k(k+1)(2k+1)}{6} + (k+1)^2 = \frac{(k+1)\bigl[k(2k+1) + 6(k+1)\bigr]}{6}.
$$

Expand the bracket: $k(2k + 1) + 6(k + 1) = 2k^2 + k + 6k + 6 = 2k^2 + 7k + 6$. This factors as $(k + 2)(2k + 3)$, which you can confirm by multiplying: $(k + 2)(2k + 3) = 2k^2 + 3k + 4k + 6 = 2k^2 + 7k + 6$. So

$$
\sum_{i=1}^{k+1} i^2 = \frac{(k+1)(k+2)(2k+3)}{6},
$$

which is the target. By induction, the formula holds for every $n \ge 1$. $\blacksquare$

Look back: the trick is to factor out the common $(k + 1)$ and not to multiply everything out. Because the target is known in advance, you can aim at it: the bracket has to become $(k + 2)(2k + 3)$, and you check by multiplying. Check: for $k = 3$, the hypothesis gives $1 + 4 + 9 = 14 = \frac{3 \cdot 4 \cdot 7}{6}$, and adding $16$ gives $30 = \frac{4 \cdot 5 \cdot 9}{6}$.

</div>

<div class="example" markdown>

### Example 3: a geometric sum

*Theorem 3.* For every real number $r \ne 1$ and every integer $n \ge 0$,

$$
\sum_{i=0}^{n} r^i = \frac{r^{n+1} - 1}{r - 1}.
$$

This is the geometric series formula with $n + 1$ terms, $1, r, \dots, r^n$. The earlier lesson found it by multiplying by $r$ and subtracting. Here we check it.

*Proof.* Base case ($n = 0$): the left side is $r^0 = 1$, and the right side is $\frac{r - 1}{r - 1} = 1$, which uses $r \ne 1$.

Inductive hypothesis: let $k \ge 0$ and suppose $\sum_{i=0}^{k} r^i = \frac{r^{k+1} - 1}{r - 1}$. Target: $\sum_{i=0}^{k+1} r^i = \frac{r^{k+2} - 1}{r - 1}$.

Peel off the last term and use the hypothesis. Then write $r^{k+1}$ over the common denominator $r - 1$:

$$
\begin{aligned}
\sum_{i=0}^{k+1} r^i &= \sum_{i=0}^{k} r^i + r^{k+1} \\
&= \frac{r^{k+1} - 1}{r - 1} + \frac{r^{k+1}(r - 1)}{r - 1} \\
&= \frac{r^{k+1} - 1 + r^{k+2} - r^{k+1}}{r - 1} = \frac{r^{k+2} - 1}{r - 1}.
\end{aligned}
$$

The terms $r^{k+1}$ and $-r^{k+1}$ cancel, which leaves the target. By induction, the formula holds for every $n \ge 0$. $\blacksquare$

Check: for $r = 3$ and $k = 2$, the hypothesis gives $1 + 3 + 9 = 13 = \frac{27 - 1}{2}$. Adding $3^3 = 27$ gives $40 = \frac{81 - 1}{2}$. The proof breaks at $r = 1$, where the denominator is 0, and the formula for that case is $n + 1$.

</div>

<div class="example" markdown>

### Example 4: divisibility, $3 \mid n^3 - n$

*Theorem 4.* For every integer $n \ge 0$, the number $n^3 - n$ is divisible by 3.

Divisibility claims have a different shape: there is no equation to continue, so the hypothesis has to be turned into one. By the definition of divides, "$3 \mid k^3 - k$" means $k^3 - k = 3m$ for some integer $m$. Naming that witness $m$ is the first move.

*Proof.* Base case ($n = 0$): $0^3 - 0 = 0 = 3 \cdot 0$.

Inductive hypothesis: let $k \ge 0$ and suppose $3 \mid k^3 - k$, so $k^3 - k = 3m$ for some integer $m$. Target: $3 \mid (k+1)^3 - (k+1)$.

Expand $(k + 1)^3 = k^3 + 3k^2 + 3k + 1$, and regroup so that $k^3 - k$ appears:

$$
\begin{aligned}
(k+1)^3 - (k+1) &= k^3 + 3k^2 + 3k + 1 - k - 1 \\
&= (k^3 - k) + 3k^2 + 3k \\
&= 3m + 3(k^2 + k) \qquad \text{(hypothesis)} \\
&= 3(m + k^2 + k).
\end{aligned}
$$

The number $m + k^2 + k$ is an integer, so $(k+1)^3 - (k+1)$ is 3 times an integer. By induction, $3 \mid n^3 - n$ for every $n \ge 0$. $\blacksquare$

Check: $k = 3$ gives $27 - 3 = 24 = 3 \cdot 8$, so $m = 8$. Then $(k+1)^3 - (k+1) = 64 - 4 = 60$, and the proof says $3(8 + 9 + 3) = 60$.

</div>

<div class="example" markdown>

### Example 5: an inequality with the base case at 5

*Theorem 5.* For every integer $n \ge 5$, $2^n > n^2$.

In Quick check 3 you saw that the inequality fails at $n = 2, 3, 4$, so the claim can't start at 0. It starts at $n_0 = 5$, and the base case is $n = 5$.

What we know: $2^{k+1} = 2 \cdot 2^k$, so the hypothesis can be doubled. What we want: $2^{k+1} > (k+1)^2$. The plan: double the hypothesis to get $2^{k+1} > 2k^2$, then show $2k^2 \ge (k+1)^2$ when $k \ge 5$.

*Proof.* Base case ($n = 5$): $2^5 = 32 > 25 = 5^2$.

Inductive hypothesis: let $k \ge 5$ and suppose $2^k > k^2$. Target: $2^{k+1} > (k+1)^2$.

Doubling both sides of the hypothesis (multiplying by 2 keeps the inequality, since $2 > 0$):

$$
2^{k+1} = 2 \cdot 2^k > 2k^2.
$$

It remains to show $2k^2 \ge (k+1)^2$. The difference is

$$
2k^2 - (k+1)^2 = k^2 - 2k - 1 = k(k - 2) - 1.
$$

For $k \ge 5$ we have $k(k - 2) \ge 5 \cdot 3 = 15$, so the difference is at least 14 and certainly positive. So $2k^2 > (k+1)^2$, and chaining the two inequalities,

$$
2^{k+1} > 2k^2 > (k+1)^2.
$$

By induction, $2^n > n^2$ for every $n \ge 5$. $\blacksquare$

Look back: the inequality $2k^2 \ge (k+1)^2$ is true from $k = 3$ on, because $k^2 - 2k - 1$ is $2$ at $k = 3$. So why can't the base case be 3? Because $P(3)$ and $P(4)$ are false, and a step that starts from a false statement tells you nothing. The base case has to be a true statement that the step can reach from, and 5 is the first one.

Check: $k = 5$ gives $2^6 = 64 > 36 = 6^2$, and $2^6 = 2 \cdot 32 > 2 \cdot 25 = 50 > 36$, the chain in the proof.

</div>

<div class="example" markdown>

### Example 6: $6 \mid 7^n - 1$ (finish it yourself)

*Theorem 6.* For every integer $n \ge 0$, $7^n - 1$ is divisible by 6.

Step 1: $P(n)$ is "$6 \mid 7^n - 1$", and $n_0 = 0$.

Step 2, base case: $7^0 - 1 = 0 = 6 \cdot 0$.

Step 3, hypothesis: let $k \ge 0$ and suppose $7^k - 1 = 6m$ for some integer $m$.

Step 4, target: $7^{k+1} - 1$ is 6 times an integer.

Now do Step 5. Write $7^{k+1} - 1$ as $7 \cdot (7^k - 1)$ plus a leftover that is visibly a multiple of 6, use the hypothesis, and finish.

<details class="solution" markdown>
<summary>Finish</summary>

Step 5: $7^{k+1} - 1 = 7 \cdot 7^k - 1 = 7(7^k - 1) + 7 - 1 = 7(7^k - 1) + 6$. By the hypothesis, this is $7 \cdot 6m + 6 = 6(7m + 1)$, and $7m + 1$ is an integer.

Step 6: by induction, $6 \mid 7^n - 1$ for every $n \ge 0$. $\blacksquare$

Check: $k = 1$ gives $7 - 1 = 6$, so $m = 1$, and $7^2 - 1 = 48 = 6(7 \cdot 1 + 1) = 6 \cdot 8$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for proving the step backward. A student writes: "Assume the formula for $k + 1$: $\sum_{i=1}^{k+1} i = \frac{(k+1)(k+2)}{2}$. Subtract $k + 1$ from both sides and the formula for $k$ appears. So it's true." This starts from the target and reaches the hypothesis. That proves $P(k + 1) \Rightarrow P(k)$, the converse of what the step needs. Going down from a statement that nobody has shown to be true establishes nothing. Always start from $P(k)$, or start from one side of $P(k + 1)$ and use $P(k)$ to get to the other side.

</div>

<div class="warning" markdown>

Watch out for a missing base case. Let $P(n)$ be "$4^n + 1$ is divisible by 3". The step is correct: if $4^k + 1 = 3m$, then $4^{k+1} + 1 = 4(4^k + 1) - 3 = 12m - 3 = 3(4m - 1)$. But $4^n + 1$ leaves remainder 2 on division by 3 for every $n$ (the values are 2, 5, 17, 65, ...), so the claim is false for all $n$. A proof of "if $P(k)$ then $P(k+1)$" says nothing about whether $P$ is ever true. The base case is the only place where the proof touches a real fact.

</div>

<div class="warning" markdown>

Watch out for a base case that doesn't support the step. The step must work for every $k$ from the base case on, starting with $k = n_0$ itself. In Example 5, the step is valid from $k = 3$, but the base case is $n = 5$ because $P(3)$ and $P(4)$ are false. The opposite slip is worse: a step that secretly needs $k \ge 2$, attached to a base case at $n = 1$, leaves the jump from 1 to 2 unproved. Practice problem 7 (the horses) is a famous false proof with exactly this gap.

</div>

<div class="warning" markdown>

Watch out for writing $P(k + 1)$ carelessly. Substitute $k + 1$ for $n$ everywhere, in brackets. For $\frac{n(n+1)}{2}$ the target is $\frac{(k+1)(k+2)}{2}$, and a common slip is to write $\frac{k+1(k+2)}{2}$ or to forget that the upper limit of the sum also changes. Write the target on its own line before doing any algebra.

</div>

<div class="warning" markdown>

Watch out for treating examples as a step. Checking that $P(1), P(2), P(3), P(4)$ are true is evidence, and not a proof of $P(k) \Rightarrow P(k+1)$ for general $k$. The expression $n^2 + n + 41$ from [what is a proof](../01-language-and-notation/01-what-is-a-proof.md) is prime for 40 consecutive values and then fails. The step has to be an argument about an arbitrary $k$.

</div>

Some smaller points. A sum up to $n = 0$ is the empty sum, which is 0, so Theorems 1 and 2 are also true for $n = 0$, and a proof may start there instead of at 1. A claim about two variables, such as "$m^n \ge n$ for all $m \ge 1$ and $n \ge 0$", is proved by fixing one variable and doing induction on the other. A claim about all integers, negative included, needs a second induction downwards or a different method, because the principle only starts at a base and goes up. And a hypothesis that is used zero times, as when the algebra proves $P(k+1)$ without it, is a warning: either the claim doesn't need induction, or an error has crept in.

## Tricks and shortcuts

For a sum, the step is a check that the formula grows by exactly the new term. Subtract the formula at $k$ from the formula at $k + 1$ and see whether the difference is the term $a_{k+1}$. For $\frac{n(n+1)}{2}$ this is $\frac{(k+1)(k+2)}{2} - \frac{k(k+1)}{2} = \frac{(k+1)\cdot 2}{2} = k + 1$. If the difference is wrong, the formula is wrong, and you find out before writing the proof.

For divisibility, the identity $a^{k+1} - 1 = a(a^k - 1) + (a - 1)$ handles every claim of the form $(a - 1) \mid a^n - 1$. For a divisor $d$ and an expression with several terms, write $f(k+1) = c \cdot f(k) + d \cdot (\text{something})$. In Example 4 the constant was $c = 1$, and in Practice problem 5 it is $c = 4$.

For an inequality, find where the claim becomes true by computing a table, as in Quick check 3. The first $n$ after the last failure is your base case. Then in the step, "double the hypothesis and compare" works for $2^n$, and "multiply the hypothesis by $k + 1$" works for factorials.

When you are stuck in Step 5, write $P(k)$ and $P(k+1)$ one under the other. Ask what was added on the left (a new term, a new factor, one more power) and what the right side did in response. The step is the explanation of that response.

## In code

A **loop invariant** is a statement about the variables of a loop that is true before the loop starts and stays true after every pass. Proving it is an induction on the number of passes: the base case is "true before the first pass", the step is "if true before a pass, then true after it", and the conclusion, when the loop stops, is the invariant together with the stopping condition. The `assert` lines below test the invariant on particular inputs, which is evidence. The comments say what the three-line induction proves for every `n`.

<details class="code" markdown>
<summary>In code</summary>

```python
def sum_to(n):
    total, i = 0, 0
    # invariant: total == i * (i + 1) // 2
    # base case: i = 0 and total = 0, and 0 == 0 * 1 // 2
    while i < n:
        assert total == i * (i + 1) // 2      # true before each pass
        i += 1
        total += i                            # step: i(i+1)/2 + (i+1) == (i+1)(i+2)/2
    assert total == i * (i + 1) // 2          # still true when the loop stops, and i == n
    return total

print(sum_to(0), sum_to(1), sum_to(100))      # 0 1 5050

print(all(sum(i * i for i in range(1, n + 1)) == n * (n + 1) * (2 * n + 1) // 6
          for n in range(0, 1000)))           # True: evidence for 1000 values, not a proof
print([n for n in range(0, 12) if 2 ** n > n * n])    # [0, 1, 5, 6, 7, 8, 9, 10, 11]
print([(4 ** n + 1) % 3 for n in range(8)])           # [2, 2, 2, 2, 2, 2, 2, 2]
```

The third line shows the table behind Example 5: the inequality fails at 2, 3 and 4 and holds from 5 on. The last line shows why the base case matters: the step for "$3 \mid 4^n + 1$" is correct, and the claim is false at every $n$.

</details>

## FAQ

### Isn't it circular to assume $P(k)$ when we are proving $P(n)$?

No. The step proves an implication, "if $P(k)$ then $P(k+1)$", and to prove an implication you assume the hypothesis and derive the conclusion. You are not claiming $P(k)$ is true. The truth of any particular $P(n)$ comes from chaining the implications to the base case. Compare with proving "if $x$ is even then $x + 2$ is even": you assume $x$ is even there too.

### If the step is true for every $k$, why do I need the base case?

Because a true step only says that truth passes along, and something has to be true to pass. The "$4^n + 1$ divisible by 3" example has a valid step and no true statement anywhere. The base case is the only point where the proof compares the claim with a real number.

### Do I have to start at 0 or 1?

No. Start at the first value for which the claim is true and the step works. For "for all $n \ge 5$" the base case is $n = 5$, and the conclusion says "for every $n \ge 5$". Starting at 0 would be wrong for $2^n > n^2$, and starting at 4 would give a false base case.

### Why is it called induction if it is a deduction?

The name comes from older usage, where "induction" meant moving from particular cases to a general rule. Mathematical induction is a deductive proof: the two checks logically force the conclusion. Do not confuse it with the scientific habit of generalizing from examples, which proves nothing in math.

## Practice

### Warm-up

1\. For each claim, write the base case (with both sides computed), the statement $P(k)$ and the statement $P(k+1)$. You need not prove the step. (a) $\sum_{i=1}^{n} i^3 = \left(\frac{n(n+1)}{2}\right)^2$ for $n \ge 1$. (b) $5 \mid 6^n - 1$ for $n \ge 0$. (c) $n! > 2^n$ for $n \ge 4$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Base case $n = 1$: left side $1^3 = 1$, right side $\left(\frac{1 \cdot 2}{2}\right)^2 = 1$. $P(k)$: $\sum_{i=1}^{k} i^3 = \left(\frac{k(k+1)}{2}\right)^2$. $P(k+1)$: $\sum_{i=1}^{k+1} i^3 = \left(\frac{(k+1)(k+2)}{2}\right)^2$.
- (b) Base case $n = 0$: $6^0 - 1 = 0 = 5 \cdot 0$. $P(k)$: $5 \mid 6^k - 1$. $P(k+1)$: $5 \mid 6^{k+1} - 1$.
- (c) Base case $n = 4$: $4! = 24 > 16 = 2^4$. $P(k)$: $k! > 2^k$. $P(k+1)$: $(k+1)! > 2^{k+1}$.

Check: in each case $P(k+1)$ is $P(k)$ with every $k$ replaced by $k + 1$, in brackets, including the upper limit of the sum in (a). In (c), $n = 3$ is not a valid base because $3! = 6 < 8 = 2^3$.

</details>

2\. Find the smallest integer $n_0$ such that $2^n > n^3$ for every $n \ge n_0$, by computing a table. Then check that the inequality $2k^3 \ge (k+1)^3$ holds for $k = 4$ but not for $k = 3$, and say what that means for the base case.

<details class="solution" markdown>
<summary>Solution</summary>

The pairs $(n, 2^n, n^3)$ for $n = 0, 1, \dots, 12$ are $(0, 1, 0)$, $(1, 2, 1)$, $(2, 4, 8)$, $(3, 8, 27)$, $(4, 16, 64)$, $(5, 32, 125)$, $(6, 64, 216)$, $(7, 128, 343)$, $(8, 256, 512)$, $(9, 512, 729)$, $(10, 1024, 1000)$, $(11, 2048, 1331)$, $(12, 4096, 1728)$. The inequality is true at 0 and 1, false at 2 through 9, and true from 10 on in this table, so $n_0 = 10$.

For the step we need $2k^3 \ge (k+1)^3$. At $k = 4$: $2 \cdot 64 = 128 \ge 125$. At $k = 3$: $2 \cdot 27 = 54 < 64$. So the step works from $k = 4$ on, but the base case must still be $n = 10$ because the statements for $n = 4, \dots, 9$ are false.

Check: $2^{10} = 1024 > 1000$, and $2^{11} = 2 \cdot 1024 > 2 \cdot 1000 = 2000 \ge 1331$.

</details>

3\. A student begins the inductive step for $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ in three different ways. Which openings are acceptable? (a) "Start from $\sum_{i=1}^{k} i = \frac{k(k+1)}{2}$ and add $k + 1$ to both sides." (b) "Assume $\sum_{i=1}^{k+1} i = \frac{(k+1)(k+2)}{2}$ and subtract $k + 1$ from both sides." (c) "Assume the formula holds for every $k \ge 1$, and show it for $k + 1$."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Acceptable. It starts from the hypothesis $P(k)$ and applies a legal operation, adding the same number to both sides. The result is $\sum_{i=1}^{k+1} i = \frac{k(k+1)}{2} + (k + 1)$, and the algebra finishes the step.
- (b) Not acceptable. It assumes the target $P(k+1)$ and derives $P(k)$, which proves the converse of the step.
- (c) Not acceptable. Assuming the formula for every $k$ assumes the conclusion of the whole theorem. The step may assume only $P(k)$ for one arbitrary $k$. (Assuming $P(j)$ for all $j \le k$ is legitimate in strong induction, which the [next lesson](02-strong-induction-and-well-ordering.md) covers, but only with the base cases handled correctly.)

Check: in (a), for $k = 4$ the line gives $10 + 5 = 15$, and the target at $k + 1 = 5$ is $\frac{5 \cdot 6}{2} = 15$.

</details>

### Standard

4\. Prove by induction that for every integer $n \ge 1$,

$$
\sum_{i=1}^{n} i(i+1) = \frac{n(n+1)(n+2)}{3}.
$$

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the sum splits off its last term. What we want: the formula for all $n \ge 1$. The plan: add the next term $(k+1)(k+2)$ to the formula for $k$ and factor.

*Proof.* Base case ($n = 1$): the left side is $1 \cdot 2 = 2$, and the right side is $\frac{1 \cdot 2 \cdot 3}{3} = 2$.

Inductive hypothesis: let $k \ge 1$ and suppose $\sum_{i=1}^{k} i(i+1) = \frac{k(k+1)(k+2)}{3}$. Target: $\sum_{i=1}^{k+1} i(i+1) = \frac{(k+1)(k+2)(k+3)}{3}$.

$$
\begin{aligned}
\sum_{i=1}^{k+1} i(i+1) &= \sum_{i=1}^{k} i(i+1) + (k+1)(k+2) \\
&= \frac{k(k+1)(k+2)}{3} + (k+1)(k+2) \qquad \text{(hypothesis)} \\
&= (k+1)(k+2)\left(\frac{k}{3} + 1\right) \\
&= \frac{(k+1)(k+2)(k+3)}{3}.
\end{aligned}
$$

By induction, the formula holds for every $n \ge 1$. $\blacksquare$

Check: $n = 3$ gives $2 + 6 + 12 = 20 = \frac{3 \cdot 4 \cdot 5}{3}$, and $n = 4$ adds $4 \cdot 5 = 20$ to give $40 = \frac{4 \cdot 5 \cdot 6}{3}$.

</details>

5\. Prove by induction that $9 \mid 4^n + 15n - 1$ for every integer $n \ge 0$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: if $4^k + 15k - 1 = 9m$ then we can rewrite $4^{k+1}$ in terms of $4^k$. What we want: $4^{k+1} + 15(k+1) - 1$ is 9 times an integer. The plan: write it as $4$ times the hypothesis expression plus a leftover, and show the leftover is a multiple of 9.

*Proof.* Base case ($n = 0$): $4^0 + 0 - 1 = 0 = 9 \cdot 0$.

Inductive hypothesis: let $k \ge 0$ and suppose $4^k + 15k - 1 = 9m$ for some integer $m$. Target: $4^{k+1} + 15(k+1) - 1$ is a multiple of 9.

Since $4^{k+1} = 4 \cdot 4^k$ and $15(k+1) - 1 = 15k + 14$,

$$
\begin{aligned}
4^{k+1} + 15(k+1) - 1 &= 4 \cdot 4^k + 15k + 14 \\
&= 4\bigl(4^k + 15k - 1\bigr) - 60k + 4 + 15k + 14 \\
&= 4 \cdot 9m - 45k + 18 \qquad \text{(hypothesis)} \\
&= 9(4m - 5k + 2).
\end{aligned}
$$

The number $4m - 5k + 2$ is an integer, so the expression is a multiple of 9. By induction, the claim holds for every $n \ge 0$. $\blacksquare$

Check: $k = 1$ gives $4 + 15 - 1 = 18 = 9 \cdot 2$, so $m = 2$. Then $4^2 + 30 - 1 = 45$, and the proof says $9(8 - 5 + 2) = 45$.

</details>

6\. Prove by induction that $n! > 2^n$ for every integer $n \ge 4$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $(k+1)! = (k+1) \cdot k!$. What we want: $(k+1)! > 2^{k+1}$. The plan: multiply the hypothesis by $k + 1$, then compare $k + 1$ with 2.

*Proof.* Base case ($n = 4$): $4! = 24 > 16 = 2^4$.

Inductive hypothesis: let $k \ge 4$ and suppose $k! > 2^k$. Target: $(k+1)! > 2^{k+1}$.

Multiply both sides of the hypothesis by $k + 1$, which is positive:

$$
(k+1)! = (k+1) \cdot k! > (k+1) \cdot 2^k.
$$

Since $k \ge 4$, we have $k + 1 \ge 5 > 2$, so $(k+1) \cdot 2^k > 2 \cdot 2^k = 2^{k+1}$. Chaining, $(k+1)! > 2^{k+1}$. By induction, the claim holds for every $n \ge 4$. $\blacksquare$

Check: $5! = 120 > 32$, and $120 = 5 \cdot 24 > 5 \cdot 16 = 80 > 2 \cdot 16 = 32$.

</details>

### Challenge

7\. Find the flaw in this "proof" that all horses have the same colour.

*Claim.* In every set of $n \ge 1$ horses, all the horses have the same colour.

"*Proof.* By induction on $n$. Base case: in a set of 1 horse, all horses have the same colour. Inductive step: suppose every set of $k$ horses is all one colour, and take a set $H$ of $k + 1$ horses, $h_1, \dots, h_{k+1}$. Remove $h_{k+1}$: the remaining $k$ horses $h_1, \dots, h_k$ are one colour by the hypothesis. Remove $h_1$ instead: the horses $h_2, \dots, h_{k+1}$ are one colour. These two groups share the horses $h_2, \dots, h_k$, so all colours agree, and all $k + 1$ horses have one colour."

<details class="solution" markdown>
<summary>Solution</summary>

The base case is fine, and the step is correct for $k \ge 2$. It fails for $k = 1$, the step from one horse to two. With $k = 1$ the set is $\{h_1, h_2\}$. The first group is $\{h_1\}$ and the second group is $\{h_2\}$, and the "shared horses $h_2, \dots, h_k$" are the horses from $h_2$ to $h_1$, which is no horses at all. The two groups don't overlap, so nothing forces their colours to agree.

So the proof contains a true base case $P(1)$, a true step for every $k \ge 2$, and a false step for $k = 1$. The chain from $P(1)$ to $P(2)$ is broken, and $P(2)$ is false: a brown horse and a white horse are a set of two horses of different colours. Everything after $P(2)$ was never reached.

The step has to hold for every $k$ from the base case on, including the smallest one. Proofs like this one hide an assumption (here, that the two groups share a horse) that is true for large $k$ and false at the start. When you finish a step, test it on the first value of $k$ by writing out the case $k = n_0$ in full.

Check: for $k = 2$ the groups are $\{h_1, h_2\}$ and $\{h_2, h_3\}$, which do share $h_2$, so the step is valid there. The failure is only at $k = 1$.

</details>

8\. (Reviews [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md).) A loan balance satisfies $B_{n+1} = (1 + r)B_n - \text{PMT}$, with $r \ne 0$. The earlier lesson claimed that $B_n = (1+r)^n B_0 - \text{PMT} \cdot \frac{(1+r)^n - 1}{r}$ and said it "can be checked by induction". Prove it by induction on $n \ge 0$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the recurrence gives $B_{k+1}$ from $B_k$, and the hypothesis gives $B_k$ in closed form. What we want: the closed form for $B_{k+1}$. The plan: substitute the hypothesis into the recurrence and simplify.

Write $q = 1 + r$ to shorten the algebra, so that $r = q - 1$.

*Proof.* Base case ($n = 0$): the formula gives $q^0 B_0 - \text{PMT} \cdot \frac{q^0 - 1}{r} = B_0 - 0 = B_0$, which is the starting balance.

Inductive hypothesis: let $k \ge 0$ and suppose $B_k = q^k B_0 - \text{PMT} \cdot \frac{q^k - 1}{r}$. Target: $B_{k+1} = q^{k+1} B_0 - \text{PMT} \cdot \frac{q^{k+1} - 1}{r}$.

By the recurrence and the hypothesis,

$$
\begin{aligned}
B_{k+1} &= qB_k - \text{PMT} \\
&= q^{k+1} B_0 - \text{PMT} \cdot \frac{q(q^k - 1)}{r} - \text{PMT} \\
&= q^{k+1} B_0 - \text{PMT}\left[\frac{q^{k+1} - q}{r} + \frac{r}{r}\right].
\end{aligned}
$$

Since $-q + r = -(1 + r) + r = -1$, the bracket is $\frac{q^{k+1} - 1}{r}$, and the target follows. By induction, the formula holds for every $n \ge 0$. $\blacksquare$

Check with the \$1,000 loan at 1% a month and \$100 payments: $B_4 = 1.01^4 \cdot 1000 - 100 \cdot \frac{1.01^4 - 1}{0.01} = 1040.60401 - 406.0401 = 634.56391$, which matches the table in the [sequences lesson](../../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md) (\$634.56).

</details>

## Where this shows up

- The next lesson, [strong induction and well-ordering](02-strong-induction-and-well-ordering.md), lets the hypothesis use every earlier case and not just $k$. After that, [recursive definitions and structural induction](03-recursive-definitions-and-structural-induction.md) applies the same two-part pattern to trees, strings and expressions. A famous false proof like the horses is the first thing to look for in [common proof mistakes](../07-putting-it-together/01-common-proof-mistakes.md).
- Every correctness proof for a loop is an induction on the number of passes, as in the invariant above (invariants and algorithm correctness<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->). Closed forms for sums and recurrences are guessed or derived and then confirmed by induction (sums and closed forms<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md --> and recurrences<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md -->).
- In finance, the annuity and loan formulas are proved by induction, as in problem 8 (annuities and geometric series<!-- link: ../../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md -->).
