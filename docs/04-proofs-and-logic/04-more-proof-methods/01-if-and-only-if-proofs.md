# If and only if proofs

After this lesson you can prove a statement of the form "$P$ if and only if $Q$" by proving two implications, run a chain of equivalences and spot the step that is not reversible, and show that several statements are all equivalent with one cycle of implications.

Before this: [conditionals and biconditionals](../02-logic-and-sets/02-conditionals-and-biconditionals.md), [direct proof](../03-core-proof-methods/01-direct-proof.md) and [contrapositive proof](../03-core-proof-methods/05-contrapositive-proof.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Write the two statements you must prove in order to prove "an integer $n$ is even if and only if $n + 1$ is odd".
2. A solution chain says: $x^2 = 4 \Leftrightarrow x = 2$. Which direction is wrong, and what value shows it?
3. You want to show that four statements $P_1, P_2, P_3, P_4$ are all equivalent. How many implications does a single cycle need, and how many would you need if you proved every pair in both directions?

<details class="solution" markdown>
<summary>Answers</summary>

1. If $n$ is even, then $n + 1$ is odd. And if $n + 1$ is odd, then $n$ is even.
2. The direction "$x^2 = 4 \Rightarrow x = 2$" is wrong. The value $x = -2$ has $x^2 = 4$ and $x \ne 2$. The other direction, $x = 2 \Rightarrow x^2 = 4$, is fine.
3. A cycle $P_1 \Rightarrow P_2 \Rightarrow P_3 \Rightarrow P_4 \Rightarrow P_1$ needs 4 implications. Proving every ordered pair separately needs $4 \times 3 = 12$.

</details>

## The idea

Suppose you refactor a function and replace the condition `n % 2 == 1` with `n * n % 2 == 1`. To trust the change you need the two conditions to agree on every integer: whenever the first is true so is the second, and whenever the second is true so is the first. Checking one of those is half a job. If you only know that the first implies the second, the new code might fire on inputs where the old code did not.

A statement "$P$ if and only if $Q$" is a guarantee of exactly that kind. It says that $P$ and $Q$ are true together and false together, so either one can stand in for the other. Theorems of this shape are called characterizations, and they are among the most useful results in mathematics, because they let you swap a condition that is hard to use for one that is easy to check. A graph is bipartite if and only if it has no cycle of odd length. A square matrix is invertible if and only if the only solution of $Ax = 0$ is $x = 0$. A natural number is divisible by 3 if and only if its digit sum is. In each case you can test whichever side is easier and read off the other.

The cost is that the proof has two halves, and each half has its own hypothesis. The conditionals lesson showed why: $P \Leftrightarrow Q$ is the same as $(P \Rightarrow Q) \wedge (Q \Rightarrow P)$, so it is true only when both implications are. This lesson is about writing those two halves, keeping them apart, and doing the bookkeeping for longer chains.

## Definitions

A **biconditional** is a statement "$P$ if and only if $Q$", written $P \Leftrightarrow Q$, which is true exactly when $P$ and $Q$ have the same truth value. A **proof of a biconditional** consists of a proof of $P \Rightarrow Q$ and a proof of $Q \Rightarrow P$.

In plain words, you prove two theorems. The forward direction, labelled ($\Rightarrow$), starts from $P$ and ends at $Q$. The backward direction, labelled ($\Leftarrow$), starts from $Q$ and ends at $P$. Which side you call "forward" is a choice, so say which one you mean in the proof.

The English has several disguises, and the proof has to match each one.

| The sentence | The half "if $P$, then $Q$" | The half "if $Q$, then $P$" |
|---|---|---|
| $P$ if and only if $Q$ | the "only if" half | the "if" half |
| $P$ iff $Q$ | the same | the same |
| $P$ is necessary and sufficient for $Q$ | the "sufficient" half | the "necessary" half |
| $P$ if $Q$, and $P$ only if $Q$ | the "only if" half | the "if" half |
| $P$ exactly when $Q$ | one half | the other half |

Watch the third row. "$P$ is sufficient for $Q$" means $P \Rightarrow Q$, and "$P$ is necessary for $Q$" means $Q \Rightarrow P$. The two words name the same two implications as "if" and "only if", so a sentence that uses them still asks for both halves.

Several statements $P_1, P_2, \dots, P_n$ are **equivalent** (or "the following are equivalent") when every one of them is equivalent to every other. A theorem that lists three or four conditions this way is saying that the conditions are interchangeable.

A step in a calculation is **reversible** when the new line implies the old line as well as the other way round. A chain of reversible steps $A \Leftrightarrow B \Leftrightarrow C$ proves $A \Leftrightarrow C$, because each arrow is a proved biconditional and a biconditional can be chained: if $A \Leftrightarrow B$ and $B \Leftrightarrow C$, then $A \Leftrightarrow C$.

## How to do it

### Two directions

1. Write the statement as "$P$ if and only if $Q$", and write both implications out in full, with the objects named. Put each in its own paragraph, headed ($\Rightarrow$) and ($\Leftarrow$).
2. Prove ($\Rightarrow$). Start by assuming $P$ and nothing about $Q$. Use any method that works: direct proof, contrapositive, cases.
3. Prove ($\Leftarrow$). Now assume $Q$ and nothing about $P$. Choose its method separately; the two halves are often different in difficulty and in style.
4. Keep the hypotheses apart. In the ($\Leftarrow$) half you may not use $P$, because it is the thing you are trying to reach.
5. Close with a sentence that names both: "Since both implications hold, $P$ if and only if $Q$."

A reliable pattern: one half is a direct proof that unpacks a definition, and the other half is a contrapositive, because the direct route starts from a fact that is awkward to unpack. Example 1 shows it.

### Chains of equivalences

When both sides of the statement can be rewritten step by step, you can prove a biconditional in one chain instead of two halves. Each line is equivalent to the one before it, with the reason beside it:

$$
\begin{aligned}
3x + 5 = 20 &\Leftrightarrow 3x = 15 && \text{(add } -5 \text{ to both sides; adding } 5 \text{ undoes it)} \\
&\Leftrightarrow x = 5 && \text{(multiply both sides by } \tfrac{1}{3} \text{; multiplying by } 3 \text{ undoes it)}
\end{aligned}
$$

The test for each arrow is the same: can I read this step upward? That works when the move has an inverse. The table lists the usual moves.

| Move on an equation or inequality | Reversible? | Why |
|---|---|---|
| add or subtract the same number on both sides | yes | the opposite operation undoes it |
| multiply or divide both sides by a number known to be nonzero | yes | the reciprocal undoes it |
| apply a function with an inverse on the numbers in play ($2^x$, $x^3$, $\ln$ on positive numbers) | yes | the inverse function undoes it |
| multiply both sides by an expression that might be 0 | no | the new equation gains the roots of that expression |
| divide both sides by an expression that might be 0 | no | the roots of that expression are lost |
| square both sides | no, unless both sides are known to be nonnegative | $x^2 = y^2$ also allows $x = -y$ |
| multiply both sides of an inequality by a negative number | yes, if you flip the sign | the flipped inequality undoes it |

If any step is only one-way, a chain proves only that direction. The standard repair is to prove the chain in one direction, and then check the other direction separately (or check each candidate in the original statement). Example 4 does this for an equation with a square root.

### Several equivalent statements

To prove that $P_1, P_2, \dots, P_n$ are equivalent, you do not need to prove every pair. Prove a cycle of implications:

$$
P_1 \Rightarrow P_2 \Rightarrow P_3 \Rightarrow \cdots \Rightarrow P_n \Rightarrow P_1.
$$

Then every statement implies every other one by following the arrows around: $P_3 \Rightarrow P_2$, for example, follows from $P_3 \Rightarrow \cdots \Rightarrow P_n \Rightarrow P_1 \Rightarrow P_2$. The cycle uses $n$ implications where the pair-by-pair approach uses $n(n-1)$.

1. Choose an order in which each arrow looks easy. Any order gives a valid proof, so pick the one that makes the arrows short. Putting the hard arrow where a strong hypothesis can carry it often helps.
2. Prove each arrow with its own method and its own "Suppose $P_i$".
3. Say at the end that the cycle closes, so all of the statements are equivalent.

Example 3 proves a cycle of three.

## Worked examples

<div class="example" markdown>

### Example 1: an integer is odd if and only if its square is odd

*Theorem 1.* Let $n$ be an integer. Then $n$ is odd if and only if $n^2$ is odd.

We follow the steps of "Two directions".

Step 1: the two implications. ($\Rightarrow$): if $n$ is odd, then $n^2$ is odd. ($\Leftarrow$): if $n^2$ is odd, then $n$ is odd.

Step 2, the forward half. What we know: $n$ is odd, so $n = 2k + 1$ for some integer $k$. What we want: $n^2 = 2l + 1$ for some integer $l$. The plan: square and gather.

*Proof of ($\Rightarrow$).* Suppose $n$ is odd. Then $n = 2k + 1$ for some integer $k$, so

$$
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.
$$

The number $2k^2 + 2k$ is an integer, so $n^2$ is odd.

Step 3, the backward half. What we know: $n^2$ is odd. A direct attack gets stuck: from $n^2 = 2l + 1$ there is no way to unpack $n$ itself. What we want: $n$ is odd. The plan: use the contrapositive. If $n$ is not odd, then $n$ is even, because every integer is even or odd, and we show that $n^2$ is then not odd.

*Proof of ($\Leftarrow$).* We prove the contrapositive: if $n$ is not odd, then $n^2$ is not odd. Suppose $n$ is not odd. Then $n$ is even, so $n = 2k$ for some integer $k$, and $n^2 = 4k^2 = 2(2k^2)$ is even. An even integer is not odd, so $n^2$ is not odd.

Step 4: the backward half used only "$n^2$ is odd" through its contrapositive, and never the assumption that $n$ is odd.

Step 5: since both implications hold, $n$ is odd if and only if $n^2$ is odd. $\blacksquare$

Look back: the two halves used different methods, as predicted. The step "an even integer is not odd" uses the fact that no integer is both; the division algorithm gives it for divisor 2, and [existence and uniqueness proofs](02-existence-and-uniqueness-proofs.md#practice) proves it in Practice problem 8.

Check: $n = 7$ is odd and $49$ is odd. $n = 6$ is even and $36$ is even. And $n = -5$ gives $25$, odd.

</div>

<div class="example" markdown>

### Example 2: two integers that divide each other

*Theorem 2.* Let $a$ and $b$ be nonzero integers. Then $a \mid b$ and $b \mid a$ if and only if $a = b$ or $a = -b$.

What we know: the definition of divides, $a \mid b$ when $b = ak$ for some integer $k$. What we want: two implications. The plan: for ($\Rightarrow$), turn both divisibilities into equations and combine them; for ($\Leftarrow$), give the witnesses.

*Proof.* ($\Rightarrow$) Suppose $a \mid b$ and $b \mid a$. Then $b = ak$ and $a = bl$ for some integers $k$ and $l$. Substituting the first into the second gives $a = (ak)l = a(kl)$. Since $a \ne 0$, we can cancel $a$ (multiply by $a^{-1}$) to get $kl = 1$. Both $k$ and $l$ are nonzero integers, because their product is 1, so each has absolute value at least 1. If $\lvert k \rvert \ge 2$ then $\lvert kl \rvert \ge 2$, which is false, so $\lvert k \rvert = 1$ and $k = 1$ or $k = -1$. Hence $b = ak = a$ or $b = -a$, that is, $a = b$ or $a = -b$.

($\Leftarrow$) Suppose $a = b$ or $a = -b$. If $a = b$, then $b = a \cdot 1$ and $a = b \cdot 1$, so $a \mid b$ and $b \mid a$. If $a = -b$, then $b = a \cdot (-1)$ and $a = b \cdot (-1)$, so again $a \mid b$ and $b \mid a$. $\blacksquare$

Look back: the hypothesis "nonzero" was used when we cancelled $a$. The theorem is still true when a number is 0, because $0 \mid b$ forces $b = 0$, but the reason is different and the proof above would not cover it. One consequence: for positive integers, $a \mid b$ and $b \mid a$ force $a = b$. Divisibility never runs both ways between two different positive integers.

Check: $a = 6$ and $b = -6$ give $-6 = 6(-1)$ and $6 = (-6)(-1)$. For $a = 4$ and $b = 8$, both sides are false: $4 \mid 8$ but $8 \nmid 4$, and $4 \ne \pm 8$.

</div>

<div class="example" markdown>

### Example 3: three equivalent conditions on one integer

*Theorem 3.* For an integer $n$, the following are equivalent:

- (a) $n$ is odd;
- (b) $n^2$ is odd;
- (c) $8 \mid n^2 - 1$.

Plan: prove (a) $\Rightarrow$ (c) $\Rightarrow$ (b) $\Rightarrow$ (a). We choose this order because (b) $\Rightarrow$ (a) is the backward half of Theorem 1, already proved, and the other two arrows are short.

*Proof.* (a) $\Rightarrow$ (c). Suppose $n$ is odd, so $n = 2k + 1$ for an integer $k$. Then

$$
n^2 - 1 = 4k^2 + 4k = 4k(k + 1).
$$

We claim that $k(k + 1)$ is even. Either $k$ is even, so $k = 2j$ and $k(k + 1) = 2j(k + 1)$; or $k$ is odd, so $k + 1 = 2j$ for an integer $j$ and $k(k + 1) = 2jk$. In both cases $k(k + 1) = 2m$ for an integer $m$, so $n^2 - 1 = 8m$ and $8 \mid n^2 - 1$.

(c) $\Rightarrow$ (b). Suppose $8 \mid n^2 - 1$, so $n^2 - 1 = 8t$ for an integer $t$. Then $n^2 = 2(4t) + 1$, which is odd.

(b) $\Rightarrow$ (a). This is the ($\Leftarrow$) half of Theorem 1.

The three arrows form a cycle, so each statement implies the other two. $\blacksquare$

Look back: the cycle gave six implications for the price of three. For example, (a) $\Rightarrow$ (b) was never proved on its own: it follows from (a) $\Rightarrow$ (c) and (c) $\Rightarrow$ (b). The most useful reading is (a) $\Rightarrow$ (c): the square of every odd number is one more than a multiple of 8.

Check: $n = 5$ gives $24 = 8 \times 3$. $n = 7$ gives $48 = 8 \times 6$. $n = 1$ gives $0 = 8 \times 0$. For the even number $n = 6$, $n^2 - 1 = 35$, not a multiple of 8.

</div>

<div class="example" markdown>

### Example 4: a chain that is not reversible

Solve $\sqrt{2x + 3} = x$ for real $x$.

The tempting chain is

$$
\sqrt{2x + 3} = x \;\Rightarrow\; 2x + 3 = x^2 \;\Leftrightarrow\; x^2 - 2x - 3 = 0 \;\Leftrightarrow\; (x - 3)(x + 1) = 0 \;\Leftrightarrow\; x = 3 \text{ or } x = -1.
$$

The first arrow is only one-way: squaring turns $\sqrt{2x + 3} = x$ into $2x + 3 = x^2$, and $2x + 3 = x^2$ also allows $x = -\sqrt{2x + 3}$. So the chain shows that any solution is $3$ or $-1$, and nothing more. Candidates must be tested in the original equation.

For $x = 3$: $\sqrt{2 \cdot 3 + 3} = \sqrt{9} = 3$. This works. For $x = -1$: $\sqrt{2(-1) + 3} = \sqrt{1} = 1$, which is not $-1$. This fails.

A chain that is reversible all the way keeps track of the sign condition. The root symbol is never negative, so $x$ has to be at least 0:

$$
\sqrt{2x + 3} = x \;\Leftrightarrow\; x \ge 0 \text{ and } 2x + 3 = x^2 \;\Leftrightarrow\; x \ge 0 \text{ and } (x = 3 \text{ or } x = -1) \;\Leftrightarrow\; x = 3.
$$

Each arrow is now an equivalence, because squaring two nonnegative numbers is reversible (that is Practice problem 7). The only solution is $x = 3$.

Check: $x = 3$ is the only value in the list $-5, -4, \dots, 5$ that satisfies the original equation.

</div>

<div class="example" markdown>

### Example 5: divisible by 3 if and only if the square is (finish it yourself)

*Theorem 4.* Let $n$ be an integer. Then $3 \mid n$ if and only if $3 \mid n^2$.

($\Rightarrow$) Suppose $3 \mid n$, so $n = 3k$ for an integer $k$. Then $n^2 = 9k^2 = 3(3k^2)$, and $3k^2$ is an integer, so $3 \mid n^2$.

($\Leftarrow$) Like Theorem 1, this half is easier by the contrapositive: if $3 \nmid n$, then $3 \nmid n^2$. Suppose $3 \nmid n$. By the division algorithm, $n = 3k + 1$ or $n = 3k + 2$ for an integer $k$.

Now finish the proof: square each form, write the result as a multiple of 3 plus a leftover, and say why 3 does not divide it.

<details class="solution" markdown>
<summary>Finish</summary>

If $n = 3k + 1$, then $n^2 = 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1$. If $n = 3k + 2$, then $n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$. In both cases $n^2 = 3m + 1$ for an integer $m$. If $3$ divided $3m + 1$, it would divide the difference $(3m + 1) - 3m = 1$, which is false. So $3 \nmid n^2$. This proves the contrapositive, and the theorem. $\blacksquare$

Check: $n = 4$ gives $16 = 3 \times 5 + 1$, and $n = 5$ gives $25 = 3 \times 8 + 1$. The squares of numbers not divisible by 3 leave remainder 1.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for proving only one direction. A proof that begins "Suppose $n$ is odd" and ends at "$n^2$ is odd" has proved the forward half and nothing else. The statement "if $n^2$ is odd then $n$ is odd" is a different statement (the converse), and in general it can be false even when the forward half is true: every multiple of 4 is even, but not every even number is a multiple of 4.

</div>

<div class="warning" markdown>

Watch out for proving the same implication twice, in disguise. The contrapositive of the forward half ("if $n^2$ is not odd, then $n$ is not odd") is not the backward half. It says the same thing as the forward half. The contrapositive of the backward half is "if $n$ is not odd, then $n^2$ is not odd", which is what Example 1 proved. To check which one you wrote, ask what the first line assumes and what the last line concludes, and compare with the two implications you listed in Step 1.

</div>

<div class="warning" markdown>

Watch out for an irreversible step in a chain. Squaring both sides, multiplying by an expression that can be 0, and dividing by a variable are the three usual ones. Dividing $x^2 = x$ by $x$ gives $x = 1$ and loses the solution $x = 0$. Squaring $x = 2$ gives $x^2 = 4$ and adds the solution $x = -2$. The fix is either to prove the chain in both directions, or to check every candidate in the original equation.

</div>

<div class="warning" markdown>

Watch out for using the other half's hypothesis. In ($\Leftarrow$), writing "since $n$ is odd" assumes the very thing you are trying to prove. The first sentence of each half should be a "Suppose" that names a different statement from the other half's.

</div>

<div class="warning" markdown>

Watch out for the one-way "if" in a theorem. A theorem that says "$n$ is even if $n = 4k$" proves one direction only. A definition's "if" means "if and only if", but a theorem's "if" does not, so read the exact wording before assuming a characterization.

</div>

Zero and negative integers need a look in every characterization. In Theorem 1, $0$ is even and $0^2 = 0$ is even, so the two sides still agree, and a negative $n$ works the same way as a positive one. In Theorem 2 the hypothesis that $a$ and $b$ are nonzero is what keeps $0$ out, because the proof cancels $a$.

## Tricks and shortcuts

Write the two headings ($\Rightarrow$) and ($\Leftarrow$) before anything else, and under each write the statement you are about to prove in a complete sentence. Half the errors in biconditional proofs are a half that proves the wrong statement, and the sentence makes that visible.

When one half is a "for every" statement over a definition ("$n$ is even"), the direct proof goes through the witness. When the other half starts from a negative or squared object, try the contrapositive. Theorems 1 and 4 both follow this split.

For a theorem with $n$ equivalent conditions, order the cycle so that the arrows go from stronger conditions to ones that unpack easily. If you already know a good implication between two of the statements, make it one arrow of the cycle.

A quick test for a chain: read it from the bottom up. If a line does not imply the line above it, the arrow between them should have been a plain $\Rightarrow$.

## In code

A biconditional is `==` on two Booleans. A brute-force check over a finite range tests a characterization, though only the proof covers every integer. The last lines show why squaring is not reversible.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

R = range(-100, 101)

def odd(n):
    return n % 2 == 1

def divides(a, b):
    return b == 0 if a == 0 else b % a == 0

print(all(odd(n) == odd(n * n) for n in R))                        # True: Theorem 1 on 201 values
print(all((divides(a, b) and divides(b, a)) == (a == b or a == -b)
          for a in R for b in R))                                  # True: Theorem 2 on 40,401 pairs (zeros included)
print(all(odd(n) == odd(n * n) == ((n * n - 1) % 8 == 0) for n in R))   # True: Theorem 3

print([x for x in R if x == 2])                                    # [2]
print([x for x in R if x * x == 4])                                # [-2, 2]: squaring adds a solution

candidates = [x for x in R if x * x == 2 * x + 3]
print(candidates)                                                  # [-1, 3]
print([x for x in candidates if 2 * x + 3 >= 0 and math.isqrt(2 * x + 3) == x])   # [3]
```

The last two lines are Example 4: the squared equation has two solutions, and only one survives in the original equation. Python agrees with the table: `x * x == 4` has more solutions than `x == 2` because squaring is not reversible.

</details>

## FAQ

### Do I really have to prove both directions, even when one looks obvious?

Yes, and write it down. A direction that looks obvious is usually short, so the cost is a line or two. A direction you skip is a place where the statement could be false. The theorem "$a \mid b$ and $b \mid a$ if and only if $a = \pm b$" has a one-line ($\Leftarrow$) half and a longer ($\Rightarrow$) half, and the longer one is where the hypothesis $a \ne 0$ is used.

### Is $\Leftrightarrow$ the same as $=$ or as $\equiv$?

They live at different levels. The symbol $=$ joins two numbers or sets. The symbol $\Leftrightarrow$ joins two statements and produces a statement, which may be true or false. The symbol $\equiv$ makes a claim that a biconditional is true in every case, as in [truth tables and logical equivalence](../02-logic-and-sets/03-truth-tables-and-logical-equivalence.md). In a chain of equations, writing $\Leftrightarrow$ between lines says that the lines have the same set of solutions.

### Why do textbooks say "TFAE" and list three or four conditions?

"TFAE" is short for "the following are equivalent". It is the cycle method packaged as a theorem: the book proves a cycle of implications once, and every later proof gets to choose whichever of the conditions is easiest to verify or to use. Linear algebra is full of them.

### Can a chain of "if and only if" steps hide a wrong step?

Yes. Writing $\Leftrightarrow$ between two lines is a claim, and a wrong claim looks the same as a right one. That is why the reversibility table is worth memorizing: each move in it either has an inverse or does not, and the chain is only as strong as its weakest arrow.

## Practice

### Warm-up

1\. For each statement, write the two implications that must be proved. (a) An integer $n$ is even if and only if $n + 1$ is odd. (b) For real $x$, $x > 3$ if and only if $x - 3 > 0$. (c) For integers $a$ and $b$, $a \mid b$ if and only if $a \mid -b$. In (a), say which half is "only if".

<details class="solution" markdown>
<summary>Solution</summary>

- (a) ($\Rightarrow$) If $n$ is even, then $n + 1$ is odd. ($\Leftarrow$) If $n + 1$ is odd, then $n$ is even. The "only if" half is ($\Rightarrow$): "$n$ is even only if $n + 1$ is odd" means "if $n$ is even, then $n + 1$ is odd".
- (b) ($\Rightarrow$) If $x > 3$, then $x - 3 > 0$. ($\Leftarrow$) If $x - 3 > 0$, then $x > 3$.
- (c) ($\Rightarrow$) If $a \mid b$, then $a \mid -b$. ($\Leftarrow$) If $a \mid -b$, then $a \mid b$.

Check: in each part the two implications swap hypothesis and conclusion, which is what makes the second one the converse of the first.

</details>

2\. Each step below changes an equation. Say whether it is reversible. If not, say which direction fails and give a value that shows it. (a) $x + 4 = 7$ to $x = 3$. (b) $x^2 = 9$ to $x = 3$. (c) $x(x - 2) = x$ to $x - 2 = 1$. (d) $2^x = 8$ to $x = 3$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Reversible: add 4 or subtract 4.
- (b) Not reversible. From $x = 3$ we get $x^2 = 9$, but from $x^2 = 9$ we do not get $x = 3$: the value $x = -3$ is a solution of the first and not the second.
- (c) Not reversible. Dividing by $x$ loses the solution $x = 0$, which has $0 \cdot (-2) = 0$. The step $x - 2 = 1 \Rightarrow x(x - 2) = x$ is fine, but the other direction fails at $x = 0$.
- (d) Reversible. The function $2^x$ is increasing, so it takes the value 8 only once, at $x = 3$.

Check: in (b) substitute $x = -3$, which gives $9 = 9$. In (c) substitute $x = 0$, which gives $0 = 0$.

</details>

3\. Prove that an integer $n$ is odd if and only if $n + 2$ is odd.

<details class="solution" markdown>
<summary>Solution</summary>

What we know and want: each half unpacks "odd" on one side and builds it on the other. The plan: add 2 or subtract 2 inside the definition.

*Proof.* ($\Rightarrow$) Suppose $n$ is odd, so $n = 2k + 1$ for an integer $k$. Then $n + 2 = 2(k + 1) + 1$, and $k + 1$ is an integer, so $n + 2$ is odd.

($\Leftarrow$) Suppose $n + 2$ is odd, so $n + 2 = 2k + 1$ for an integer $k$. Then $n = 2k - 1 = 2(k - 1) + 1$, and $k - 1$ is an integer, so $n$ is odd. $\blacksquare$

Check: $n = 5$ and $n + 2 = 7$ are both odd; $n = -4$ and $n + 2 = -2$ are both even.

</details>

### Standard

4\. Prove that for integers $m$ and $n$, the product $mn$ is odd if and only if $m$ and $n$ are both odd.

<details class="solution" markdown>
<summary>Solution</summary>

What we know and want: one half builds a product from odd integers, which is Theorem 4 of [proof language](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#worked-examples). The other half starts from a product, which is awkward, so we use the contrapositive.

*Proof.* ($\Leftarrow$) Suppose $m$ and $n$ are both odd, so $m = 2j + 1$ and $n = 2k + 1$ for integers $j$ and $k$. Then $mn = 2(2jk + j + k) + 1$, which is odd.

($\Rightarrow$) We prove the contrapositive: if $m$ or $n$ is even, then $mn$ is even. Suppose $m$ is even (the case where $n$ is even is the same with the names swapped, since $mn = nm$). Then $m = 2k$, so $mn = 2(kn)$ is even. A number that is even is not odd, so if $mn$ is odd then $m$ and $n$ are both odd. $\blacksquare$

Check: $m = 3$ and $n = 5$ give $15$, odd. $m = 3$ and $n = 4$ give $12$, even.

</details>

5\. Find the flaw in this solution and give the correct answer. "Solve $\sqrt{x + 2} = x$. Squaring both sides, $x + 2 = x^2$, so $x^2 - x - 2 = 0$, which factors as $(x - 2)(x + 1) = 0$. Every step is an equivalence, so the solutions are $x = 2$ and $x = -1$."

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is in the claim that every step is an equivalence. Squaring is only one-way. The equation $x + 2 = x^2$ is also satisfied by values where $x = -\sqrt{x + 2}$.

Test both values in the original equation. For $x = 2$: $\sqrt{4} = 2$, true. For $x = -1$: $\sqrt{1} = 1$, which is not $-1$, so $x = -1$ is rejected. The only solution is $x = 2$.

Check: the corrected chain is $\sqrt{x + 2} = x \Leftrightarrow x \ge 0$ and $x + 2 = x^2$, and the only root of $x^2 - x - 2$ that is at least 0 is $x = 2$.

</details>

6\. Prove that for integers $a$, $b$ and $c$ with $c \ne 0$, we have $a \mid b$ if and only if $ca \mid cb$. Then show by example that the hypothesis $c \ne 0$ is needed.

<details class="solution" markdown>
<summary>Solution</summary>

What we know and want: both halves unpack the definition of divides. The plan: ($\Rightarrow$) multiply by $c$; ($\Leftarrow$) cancel $c$, which is the only place where $c \ne 0$ matters.

*Proof.* ($\Rightarrow$) Suppose $a \mid b$, so $b = ak$ for an integer $k$. Then $cb = c(ak) = (ca)k$, so $ca \mid cb$.

($\Leftarrow$) Suppose $ca \mid cb$, so $cb = (ca)k$ for an integer $k$. Then $cb = c(ak)$. Since $c \ne 0$, we can cancel $c$ (multiply by $c^{-1}$) to get $b = ak$, so $a \mid b$. $\blacksquare$

The hypothesis is needed: take $c = 0$, $a = 2$ and $b = 1$. Then $ca = 0$ and $cb = 0$, and $0 \mid 0$ is true, but $2 \mid 1$ is false. So the ($\Leftarrow$) half fails.

Check: $a = 3$, $b = 12$, $c = -5$: $3 \mid 12$, and $-15 \mid -60$ because $-60 = (-15)(4)$.

</details>

### Challenge

7\. Prove that for real numbers $a, b \ge 0$, we have $a \le b$ if and only if $a^2 \le b^2$. Then give an example showing that the statement can fail if $a$ and $b$ may be negative.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $a \ge 0$ and $b \ge 0$, and the order axioms (a product of nonnegative numbers is nonnegative, and multiplying an inequality by a nonnegative number keeps it). What we want: two implications. The plan: ($\Rightarrow$) multiply twice; ($\Leftarrow$) the contrapositive, because from $a^2 \le b^2$ there is nothing to take square roots of.

*Proof.* ($\Rightarrow$) Suppose $a \le b$. Multiplying by $a \ge 0$ gives $a^2 \le ab$. Multiplying by $b \ge 0$ gives $ab \le b^2$. So $a^2 \le b^2$.

($\Leftarrow$) We prove the contrapositive: if $a > b$ then $a^2 > b^2$. Suppose $a > b$. Since $b \ge 0$, we have $a > 0$. Multiplying $a > b$ by $a > 0$ gives $a^2 > ab$. Multiplying $a > b$ by $b \ge 0$ gives $ab \ge b^2$. So $a^2 > ab \ge b^2$, and $a^2 > b^2$. $\blacksquare$

For negative numbers: $a = -3$ and $b = 2$ have $a^2 = 9$ and $b^2 = 4$. Here $a \le b$ is true and $a^2 \le b^2$ is false, so ($\Rightarrow$) fails.

Look back: this is the fact that makes squaring reversible when both sides are nonnegative, the repair used in Example 4. Check: $a = 1.5$, $b = 2$ give $2.25 \le 4$, and $a = 4$, $b = 3$ give $16 > 9$.

</details>

8\. (Reviews [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md).) Let $a$, $b$ and $c$ be integers. Prove that $a \mid b$ if and only if $a \mid b + ac$. Use Theorem 3 and Corollary 4 from that lesson.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: if $a \mid x$ and $a \mid y$, then $a \mid x + y$ and $a \mid x - y$ (Corollary 4); and $a \mid ac$ for every $c$ (Lemma 2 with $b = a$, or directly $ac = a \cdot c$). What we want: two implications. The plan: add $ac$ in one direction, subtract it in the other.

*Proof.* ($\Rightarrow$) Suppose $a \mid b$. Since $a \mid ac$, Corollary 4 gives $a \mid b + ac$.

($\Leftarrow$) Suppose $a \mid b + ac$. Since $a \mid ac$, Corollary 4 gives $a \mid (b + ac) - ac$, and $(b + ac) - ac = b$. So $a \mid b$. $\blacksquare$

Look back: the idea is the same as in the Euclidean algorithm: replacing $b$ by $b + ac$ does not change which numbers divide it together with $a$. Check: $a = 4$, $b = 6$, $c = 5$ gives $b + ac = 26$; $4 \nmid 6$ and $4 \nmid 26$. And $a = 4$, $b = 8$, $c = 5$ gives $28$, with $4 \mid 8$ and $4 \mid 28$.

</details>

## Where this shows up

- The next lesson, [existence and uniqueness proofs](02-existence-and-uniqueness-proofs.md), adds the "exactly one" statement, which is itself a pair of claims. [Proofs about sets](03-proofs-about-sets.md) uses two inclusions the way this lesson uses two implications.
- In discrete math and algorithms, characterizations are everywhere: a graph is bipartite if and only if it has no odd cycle (Bipartite graphs, coloring and planar graphs<!-- link: ../../06-cs-math/05-graphs/03-bipartite-coloring-and-planar-graphs.md -->), and a statement of the form "language $L$ is regular if and only if some finite automaton accepts it" needs both halves. The reversibility table is the reason "solve the equation, then check the answer" is a proof step and not just a habit.
- In linear algebra, the theorem listing equivalent conditions for a square matrix (invertible, only the zero solution to $Ax = 0$, columns independent, nonzero determinant) is proved by a cycle, as in Example 3. You will meet it in [matrix algebra and inverses](../../05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md).
