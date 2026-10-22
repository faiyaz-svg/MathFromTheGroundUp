# Inclusion-exclusion and the pigeonhole principle

After this lesson you can count a union of overlapping sets with inclusion-exclusion and prove the formula, count derangements and onto functions, and use the pigeonhole principle, in its basic and generalized forms, to prove that a repeat or a long subsequence must exist.

Before this: [counting rules](01-counting-rules.md), [the binomial theorem and combinatorial proofs](03-binomial-theorem-and-combinatorial-proofs.md) (the alternating row sum) and [sets and set operations](../../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md), which counts two and three sets with overlaps.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. How many integers from 1 to 100 are divisible by 2 or by 3?
2. Among 13 people, must two have birthdays in the same month? Why?
3. Three letters are written in order, ABC. In how many of the $3! = 6$ orderings does no letter stay in its original place?

<details class="solution" markdown>
<summary>Answers</summary>

1. There are 50 multiples of 2 and 33 of 3, and the 16 multiples of 6 are in both lists, so $50 + 33 - 16 = 67$.
2. Yes. There are 12 months, and 13 people, so if each month held at most one birthday there would be at most 12 people. Some month holds two or more.
3. The orderings are ABC, ACB, BAC, BCA, CAB and CBA. Only BCA and CAB move every letter, so the answer is 2.

</details>

## The idea

Adding the sizes of two sets counts the elements in both sets twice. The fix, from the sets lesson, is to subtract the overlap once. With three sets the same fix overcorrects: subtracting all three pairwise overlaps removes the elements that are in all three sets once too often, so they have to be added back. The pattern is to add the singles, subtract the pairs, add the triples, and keep alternating. This is **inclusion-exclusion**, and the first half of this lesson proves that it works for any number of sets and uses it for two famous counts, derangements and onto functions.

The second half is about the opposite situation. Instead of counting overlaps, you prove that an overlap must exist. If 13 people have birthdays in 12 months, two share a month, and nobody needs to know the birthdays. This is the **pigeonhole principle**, and it gives surprising results with almost no calculation: any sequence of $n$ integers has a block of consecutive terms whose sum is divisible by $n$, and any long enough sequence of distinct numbers has a long increasing or decreasing subsequence. The two halves belong together because both are about collisions, one by counting them and one by showing that they can't be avoided.

## Definitions

For finite sets $A_1, \dots, A_n$ and each $j$ from 1 to $n$, let $s_j$ be the sum of the sizes of all the intersections of $j$ of the sets:

$$
s_j = \sum_{1 \le i_1 < i_2 < \cdots < i_j \le n} \lvert A_{i_1} \cap A_{i_2} \cap \cdots \cap A_{i_j} \rvert.
$$

In plain words, $s_1$ is the sum of the sizes of the sets, $s_2$ is the sum over all pairs of the size of the overlap, $s_3$ is the same for triples, and so on. For three sets, $s_1 = \lvert A \rvert + \lvert B \rvert + \lvert C \rvert$, $s_2 = \lvert A \cap B \rvert + \lvert A \cap C \rvert + \lvert B \cap C \rvert$ and $s_3 = \lvert A \cap B \cap C \rvert$. The condition $i_1 < \cdots < i_j$ makes each group of $j$ sets appear once.

A **derangement** of $n$ items is a permutation in which no item is in its original position, a permutation with no fixed point. The number of derangements is $D_n$. In plain words, it counts the ways to shuffle $n$ things so that every one moves, such as $n$ people each taking a hat that is not their own. By convention $D_0 = 1$, and $D_1 = 0$, $D_2 = 1$, $D_3 = 2$.

A function $f \colon A \to B$ is **onto**, or surjective, if every element of $B$ is an output, as in [injective, surjective and bijective](../../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md). Write $\text{Onto}(m, n)$ for the number of onto functions from an $m$-element set to an $n$-element set.

The **ceiling** $\lceil x \rceil$ of a real number $x$ is the smallest integer that is at least $x$, so $\lceil 4.3 \rceil = 5$ and $\lceil 4 \rceil = 4$. The [step functions lesson](../../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md) covers floors and ceilings.

The **pigeonhole principle** says that if $N$ objects are put into $k$ boxes and $N > k$, some box has at least 2 objects. In plain words, if there are more pigeons than holes, two pigeons share a hole. The **generalized pigeonhole principle** says that some box has at least $\lceil N/k \rceil$ objects.

## How to do it

### Inclusion-exclusion

1. Name the sets $A_1, \dots, A_n$ and the universe $U$. Say what each set is a set of.
2. Compute the size of every intersection of $j$ of the sets, for $j = 1, \dots, n$. Often all the intersections of the same number of sets have equal size, and then $s_j = \binom{n}{j}$ times that size.
3. For the size of the union, alternate: $s_1 - s_2 + s_3 - \cdots$. For the number of elements in none of the sets, start from the universe: $\lvert U \rvert - s_1 + s_2 - s_3 + \cdots$.
4. Check with a case small enough to list, or compute the result a second way.

*Theorem 1 (inclusion-exclusion).* For finite sets $A_1, \dots, A_n$,

$$
\lvert A_1 \cup A_2 \cup \cdots \cup A_n \rvert = s_1 - s_2 + s_3 - \cdots + (-1)^{n+1}s_n = \sum_{j=1}^{n}(-1)^{j+1}s_j.
$$

For $n = 2$ and $n = 3$ this reads

$$
\begin{aligned}
\lvert A \cup B \rvert &= \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert, \\
\lvert A \cup B \cup C \rvert &= \lvert A \rvert + \lvert B \rvert + \lvert C \rvert - \lvert A \cap B \rvert - \lvert A \cap C \rvert - \lvert B \cap C \rvert + \lvert A \cap B \cap C \rvert.
\end{aligned}
$$

We know the sum rule and that $\sum_{j=0}^{t}(-1)^j\binom{t}{j} = 0$ for $t \ge 1$. We want the size of the union. The plan is to find how many times each element is counted on the right side, and show that it is once for an element of the union and zero times for any other.

*Proof.* Take an element $x$ and let $t$ be the number of the sets $A_i$ that contain $x$. If $t = 0$, then $x$ is in no intersection and contributes 0 to the right side, and $x$ is not in the union. Suppose $t \ge 1$, so that $x$ is in the union. For each $j$, the element $x$ lies in an intersection of $j$ of the sets exactly when all $j$ sets are among the $t$ sets that contain $x$, so $x$ is counted in $\binom{t}{j}$ of the intersections in $s_j$ (this is zero if $j > t$). So the right side counts $x$ a total of

$$
\sum_{j=1}^{t}(-1)^{j+1}\binom{t}{j} = 1 - \sum_{j=0}^{t}(-1)^j\binom{t}{j} = 1 - 0 = 1
$$

times, by the alternating row sum of the previous lesson. Each element of the union is counted once and every other element not at all, so the right side is the size of the union. $\blacksquare$

Look back: the proof doesn't track the sets, only one element at a time. An element in all $n$ sets is counted $n$ times in $s_1$, then removed $\binom{n}{2}$ times, added back $\binom{n}{3}$ times, and so on, and the alternating sum of the row leaves exactly one. For three sets, an element in all three is counted $3 - 3 + 1 = 1$ times.

Since the union and its complement partition the universe, the number of elements in none of the sets is

$$
\lvert U \rvert - \lvert A_1 \cup \cdots \cup A_n \rvert = \sum_{j=0}^{n}(-1)^j s_j, \qquad s_0 = \lvert U \rvert.
$$

In plain words, count everything, subtract the elements that break rule 1, rule 2 and so on, then add back what was subtracted twice.

### Derangements

*Theorem 2.* For $n \ge 0$,

$$
D_n = n!\sum_{k=0}^{n}\frac{(-1)^k}{k!} = n!\left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \cdots + \frac{(-1)^n}{n!}\right).
$$

We know inclusion-exclusion in its complement form. We want the permutations with no fixed point. The plan is to let $A_i$ be the permutations that fix the item $i$, and count the permutations in none of the $A_i$.

*Proof.* Let $U$ be the set of all $n!$ permutations of $\{1, \dots, n\}$, and let $A_i$ be the set of those with $\pi(i) = i$. A derangement is a permutation in none of the $A_i$. The permutations in $A_{i_1} \cap \cdots \cap A_{i_j}$ fix $j$ chosen items, and the other $n - j$ items can be arranged in any order, so the intersection has $(n-j)!$ elements, whichever $j$ items were chosen. There are $\binom{n}{j}$ such intersections, so $s_j = \binom{n}{j}(n-j)! = \frac{n!}{j!}$. By inclusion-exclusion, $D_n = \sum_{j=0}^{n}(-1)^j\frac{n!}{j!}$. $\blacksquare$

Look back: for $n = 3$, $D_3 = 6 - 6 + 3 - 1 = 2$, which matches the two orderings BCA and CAB of the quick check.

The fraction of permutations that are derangements is $\frac{D_n}{n!} = \sum_{k=0}^{n}\frac{(-1)^k}{k!}$, a partial sum of the series for $e^{-1}$. The series $e^{x} = \sum_k\frac{x^k}{k!}$ is from [power series and Taylor series](../../05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md), and $x = -1$ gives $e^{-1} = \sum_{k \ge 0}\frac{(-1)^k}{k!}$. This is an alternating series whose terms decrease to 0, so the error of a partial sum is smaller than the first term left out ([convergence tests](../../05-university-core/05-sequences-and-series/03-convergence-tests.md)):

$$
\left\lvert \frac{D_n}{n!} - \frac{1}{e} \right\rvert < \frac{1}{(n+1)!}.
$$

So $\frac{D_n}{n!} \to \frac{1}{e} \approx 0.367879$, and the convergence is very fast.

| $n$ | $D_n$ | $\frac{D_n}{n!}$ |
|---|---|---|
| 1 | 0 | 0.000000 |
| 2 | 1 | 0.500000 |
| 3 | 2 | 0.333333 |
| 4 | 9 | 0.375000 |
| 5 | 44 | 0.366667 |
| 6 | 265 | 0.368056 |
| 7 | 1,854 | 0.367857 |
| 8 | 14,833 | 0.367882 |
| 9 | 133,496 | 0.367879 |
| 10 | 1,334,961 | 0.367879 |

Multiplying the bound by $n!$ gives $\lvert D_n - \frac{n!}{e} \rvert < \frac{1}{n+1} \le \frac{1}{2}$ for $n \ge 1$, so $D_n$ is the integer nearest to $\frac{n!}{e}$. For $n = 10$, $\frac{10!}{e} = 1{,}334{,}960.9\ldots$, and the nearest integer is $1{,}334{,}961$. In words: a random shuffle leaves nothing in place about 37% of the time, whether there are 5 items or 5 million.

### Onto functions

*Theorem 3.* For $m, n \ge 1$,

$$
\text{Onto}(m, n) = \sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)^m.
$$

We know inclusion-exclusion in its complement form. We want the functions that hit every output. The plan is to count the functions that miss at least one output, and use the same method as for derangements.

*Proof.* Let $U$ be the set of all functions from $\{1, \dots, m\}$ to $\{1, \dots, n\}$, so $\lvert U \rvert = n^m$. Let $A_i$ be the set of functions that never output $i$. A function is onto exactly when it is in none of the $A_i$. A function in $A_{i_1} \cap \cdots \cap A_{i_k}$ avoids $k$ chosen outputs, so it is a function into the other $n - k$ values, and there are $(n-k)^m$ of those. There are $\binom{n}{k}$ choices of $k$ outputs, so $s_k = \binom{n}{k}(n-k)^m$, and inclusion-exclusion gives $\sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)^m$. $\blacksquare$

Look back: for $m < n$ the sum is 0, since no function can hit more outputs than it has inputs. For $m = n$ it gives $n!$, the number of bijections. The numbers are also $n!$ times the Stirling numbers of the second kind, which count the ways to split $m$ items into $n$ non-empty unlabelled groups.

| $m \to n$ | all functions $n^m$ | onto |
|---|---|---|
| $4 \to 3$ | 81 | 36 |
| $5 \to 3$ | 243 | 150 |
| $5 \to 2$ | 32 | 30 |
| $6 \to 3$ | 729 | 540 |
| $4 \to 4$ | 256 | 24 |

### The pigeonhole principle

*Theorem 4 (pigeonhole principle).* If $A$ and $B$ are finite sets with $\lvert A \rvert > \lvert B \rvert$, and $f \colon A \to B$ is a function, then $f(a) = f(a')$ for some different $a, a' \in A$.

We know the bijection rule. We want to show that a function from a bigger set to a smaller set repeats an output. The plan is to suppose it doesn't and count.

*Proof.* Suppose that no two different elements of $A$ have the same output. Then $f$ is injective, so $f$ is a bijection from $A$ onto its set of outputs $f(A) \subseteq B$, and $\lvert A \rvert = \lvert f(A) \rvert \le \lvert B \rvert$, contradicting $\lvert A \rvert > \lvert B \rvert$. $\blacksquare$

Look back: the objects are $A$ and the boxes are $B$, and $f$ says which box each object goes in. The principle says nothing about which box holds two objects or how to find them, only that one does.

*Theorem 5 (generalized pigeonhole principle).* If $N$ objects are put into $k$ boxes, some box contains at least $\lceil N/k \rceil$ objects.

We know the ceiling is the smallest integer that is at least $\frac{N}{k}$. We want a box with that many objects. The plan is to suppose every box has fewer and count the total.

*Proof.* Suppose every box has at most $\lceil N/k \rceil - 1$ objects. Since $\lceil x \rceil - 1 < x$ for every real $x$, each box has fewer than $\frac{N}{k}$ objects, so the $k$ boxes together hold fewer than $k \cdot \frac{N}{k} = N$ objects. That contradicts the fact that all $N$ objects are in the boxes. $\blacksquare$

Look back: with $N > k$ we have $\frac{N}{k} > 1$, so the ceiling is at least 2, and the first theorem is the case $\lceil N/k \rceil \ge 2$. The bound can be reached: $N = 28$ objects in $k = 7$ boxes can have exactly 4 in each box, and $\lceil \frac{28}{7} \rceil = 4$. The ceiling matters, because with 30 objects in 7 boxes the average is $4.29$ and some box must have 5.

### Classic uses

The method is the same each time. Choose the boxes, which is where the creativity goes, put each object in a box, and count.

*Theorem 6.* Every sequence $a_1, a_2, \dots, a_n$ of $n$ integers has a block of consecutive terms $a_{i+1}, \dots, a_j$ whose sum is divisible by $n$.

We know the pigeonhole principle. We want a block with sum divisible by $n$. The plan is to look at the running totals, which are $n + 1$ numbers, and sort them by their remainder mod $n$, of which there are only $n$.

*Proof.* Let $p_0 = 0$ and $p_k = a_1 + \cdots + a_k$ for $k = 1, \dots, n$. These are $n + 1$ integers. Each has a remainder on division by $n$ from $\{0, 1, \dots, n-1\}$, so there are $n$ boxes, and two of the totals, $p_i$ and $p_j$ with $i < j$, have the same remainder. Then $p_j - p_i = a_{i+1} + \cdots + a_j$ is divisible by $n$. $\blacksquare$

Look back: the empty total $p_0 = 0$ is what makes the number of objects $n + 1$, one more than the number of boxes. It also covers blocks that start at the first term: if some $p_j$ is itself divisible by $n$, it matches $p_0$ and the block is $a_1, \dots, a_j$. The integers can be negative, and the block can be a single term or the whole sequence. For $n = 5$ and the sequence 4, 7, 1, 8, 3, the totals are 0, 4, 11, 12, 20, 23, with remainders 0, 4, 1, 2, 0, 3. The remainder 0 appears twice, for $p_0$ and $p_4$, so the block $4 + 7 + 1 + 8 = 20$ is divisible by 5.

*Theorem 7 (Erdős-Szekeres).* Every sequence of $n^2 + 1$ distinct real numbers contains an increasing subsequence of length $n + 1$ or a decreasing subsequence of length $n + 1$.

We know the pigeonhole principle. We want a long monotone subsequence. The plan is to label each term with two numbers, the lengths of the longest increasing and decreasing subsequences that end there, and show the labels can't all fit in the available boxes.

*Proof.* Let the sequence be $a_1, \dots, a_{n^2+1}$. For each position $i$, let $u_i$ be the length of the longest increasing subsequence that ends at $a_i$, and $d_i$ the length of the longest decreasing one. Both are at least 1. Suppose for contradiction that no monotone subsequence has length $n + 1$. Then $1 \le u_i \le n$ and $1 \le d_i \le n$, so each pair $(u_i, d_i)$ is one of $n \cdot n = n^2$ boxes. There are $n^2 + 1$ positions, so two positions $i < j$ have the same pair. Since the terms are different, either $a_i < a_j$ or $a_i > a_j$. If $a_i < a_j$, appending $a_j$ to a longest increasing subsequence that ends at $a_i$ gives an increasing subsequence of length $u_i + 1$ that ends at $a_j$, so $u_j \ge u_i + 1$. If $a_i > a_j$, then in the same way $d_j \ge d_i + 1$. Either way the pairs differ, a contradiction. $\blacksquare$

Look back: the proof uses the boxes $(u_i, d_i)$, and nobody would think of them without trying. The result can't be improved. For $n = 2$ the sequence 2, 1, 4, 3 has 4 terms and no monotone subsequence of length 3, and for $n = 3$ the sequence 3, 2, 1, 6, 5, 4, 9, 8, 7 has 9 terms and none of length 4. For the sequence 3, 1, 4, 2, 5 ($n = 2$, so 5 terms), the pairs $(u_i, d_i)$ are $(1,1), (1,2), (2,1), (2,2), (3,1)$, all different, and $u_5 = 3$ gives the increasing subsequence 1, 2, 5.

## Worked examples

<div class="example" markdown>

### Example 1: numbers divisible by none of 2, 3 and 5

How many integers from 1 to 1,000 are divisible by none of 2, 3 and 5?

Step 1: let $U = \{1, \dots, 1000\}$, and let $A$, $B$ and $C$ be the multiples of 2, 3 and 5. We want the number of elements in none of the three sets.

Step 2: the number of multiples of $d$ in $U$ is $\lfloor \frac{1000}{d} \rfloor$, and a number is a multiple of two of them exactly when it is a multiple of their least common multiple. So $\lvert A \rvert = 500$, $\lvert B \rvert = 333$, $\lvert C \rvert = 200$, then $\lvert A \cap B \rvert = \lfloor \frac{1000}{6} \rfloor = 166$, $\lvert A \cap C \rvert = 100$, $\lvert B \cap C \rvert = 66$ and $\lvert A \cap B \cap C \rvert = \lfloor \frac{1000}{30} \rfloor = 33$.

Step 3: the sums are $s_1 = 500 + 333 + 200 = 1033$, $s_2 = 166 + 100 + 66 = 332$ and $s_3 = 33$. The number in none of the sets is

$$
1000 - 1033 + 332 - 33 = 266.
$$

Step 4, the check: a loop over 1 to 1,000 that counts the numbers not divisible by 2, 3 or 5 finds 266. Another check is the density: the fraction of integers not divisible by any of 2, 3, 5 is $\frac{1}{2} \cdot \frac{2}{3} \cdot \frac{4}{5} = \frac{4}{15}$, and $\frac{4}{15} \cdot 1000 = 266.7$. The same method counts the integers up to $N$ that have no factor in common with $N$, which is [Euler's function in the number theory chapter](../02-number-theory/05-fermat-euler-and-fast-exponentiation.md).

</div>

<div class="example" markdown>

### Example 2: three overlapping groups

In a class of 40 students (hypothetical numbers), 25 take CS, 18 take economics and 12 take math. Of these, 10 take CS and economics, 8 take CS and math, 5 take economics and math, and 3 take all three. How many take none of the three?

The union has $25 + 18 + 12 - 10 - 8 - 5 + 3 = 35$ students, so $40 - 35 = 5$ take none.

Check by filling in the regions of the Venn diagram from the middle out. All three: 3. CS and economics only: $10 - 3 = 7$. CS and math only: $8 - 3 = 5$. Economics and math only: $5 - 3 = 2$. CS only: $25 - 7 - 5 - 3 = 10$. Economics only: $18 - 7 - 2 - 3 = 6$. Math only: $12 - 5 - 2 - 3 = 2$. The seven regions are $3, 7, 5, 2, 10, 6, 2$, all at least 0, and they add to 35. If one of them had come out negative, the data would be impossible.

</div>

<div class="example" markdown>

### Example 3: the hat-check problem

Five people check their hats, and the hats are returned in a random order. How many of the $5! = 120$ orders return no one's own hat, and what is the probability?

By Theorem 2 with $s_j = \frac{5!}{j!}$, the terms are $120, 120, 60, 20, 5, 1$ for $j = 0, \dots, 5$, and

$$
D_5 = 120 - 120 + 60 - 20 + 5 - 1 = 44.
$$

The probability is $\frac{44}{120} = \frac{11}{30} \approx 0.3667$, compared with $\frac{1}{e} \approx 0.3679$. The error $0.0012$ is below the bound $\frac{1}{6!} = 0.0014$.

Check: a brute-force count over all 120 orders gives 44. Also, $\left\lvert 44 - \frac{120}{e} \right\rvert = \lvert 44 - 44.145 \rvert = 0.145$, less than $\frac{1}{2}$, so 44 is the integer nearest to $\frac{5!}{e}$.

</div>

<div class="example" markdown>

### Example 4: assigning tasks so that every server is used

Five different tasks go to 3 servers, and every server must get at least one task. How many assignments are there?

An assignment is a function from the 5 tasks to the 3 servers, and every server is used exactly when the function is onto. By Theorem 3, with $m = 5$ and $n = 3$:

$$
\text{Onto}(5, 3) = 3^5 - 3\cdot 2^5 + 3\cdot 1^5 - 0 = 243 - 96 + 3 = 150.
$$

The terms mean: all assignments, minus those that leave a given server idle (3 choices of server, $2^5$ assignments each), plus those that leave two servers idle (counted twice in the subtraction), and the term for 3 idle servers is 0.

Check: brute force over all $3^5 = 243$ assignments finds 150 onto functions. Another check is by cases on the sizes of the groups: sizes $3, 1, 1$ give $\binom{5}{3} \cdot 2 \cdot 3 = 60$ assignments (choose the three tasks for one server, then split the remaining 2 between the other servers, and choose which server takes the big group: $10 \cdot 2 \cdot 3 = 60$), and sizes $2, 2, 1$ give $\binom{5}{1}\binom{4}{2} \cdot 3 = 90$, and $60 + 90 = 150$.

</div>

<div class="example" markdown>

### Example 5: finish it yourself

Show that among any 30 people, some 5 of them were born on the same day of the week. Then find the smallest number of people that guarantees 5 born on the same day.

The boxes are the 7 days of the week and the objects are the 30 people. By the generalized pigeonhole principle, some day has at least $\lceil \frac{30}{7} \rceil$ people. Work out the ceiling, and then ask how many people would be needed to be sure of 5 on one day, by finding the largest group of people that could have at most 4 on each day.

<details class="solution" markdown>
<summary>Finish</summary>

$\frac{30}{7} = 4.29$, so $\lceil \frac{30}{7} \rceil = 5$, and some day has at least 5 people.

For the second question, a group in which each day has at most 4 people has at most $7 \cdot 4 = 28$ people, and such a group exists (4 for each day). So 28 people don't guarantee 5. With 29 people, the generalized principle gives $\lceil \frac{29}{7} \rceil = \lceil 4.14 \rceil = 5$. So 29 is the smallest number.

Check: 29 people can't have at most 4 on each day, since $7 \cdot 4 = 28 < 29$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out at step 3: the signs alternate, and the first term, $s_1$, is added. A common slip is to stop after subtracting the pairs, which overcounts or undercounts when three sets overlap. Stopping early is fine only as an estimate: the partial sums $s_1$, $s_1 - s_2$, $s_1 - s_2 + s_3$ and so on alternate between an upper bound and a lower bound for the union, and $s_1$ is the union bound of probability.

</div>

<div class="warning" markdown>

Watch out at step 2: the intersections must be counted for every group of $j$ sets, and the size of an intersection of two sets is not the product of their sizes. For multiples, the intersection of "multiples of 4" and "multiples of 6" is the multiples of 12, the least common multiple, and not of 24. The two sets overlap in $\lfloor \frac{1000}{12} \rfloor = 83$ numbers.

</div>

<div class="warning" markdown>

Watch out: the pigeonhole principle needs more objects than boxes, and the off-by-one is a classic error. Among 5 integers, two need not differ by a multiple of 5: 0, 1, 2, 3, 4 have different remainders. Six integers are needed, one more than the number of remainders. In Theorem 6 the extra object is the running total 0.

</div>

<div class="warning" markdown>

Watch out: the generalized principle gives the guaranteed minimum for some box, not for every box and not the number in a particular box. With 30 people and 7 days, one day has at least 5, but other days may have none. Also take the ceiling and not the floor: $\lfloor \frac{30}{7} \rfloor = 4$ would give a bound that is true and weaker.

</div>

Some small cases. Inclusion-exclusion with one set says that the union has the size of the set, and with disjoint sets all of $s_2, s_3, \dots$ are 0, which is the sum rule. $D_0 = 1$ because the empty permutation has no fixed point, and $D_1 = 0$. The formula for onto functions with $n = 1$ gives $1^m - 0 = 1$, the single constant function. The pigeonhole principle with an empty set of objects says nothing, since $0 > k$ is false.

## Tricks and shortcuts

For "divisible by" problems on $1, \dots, N$, every size is a floor of $N$ divided by a least common multiple, and the sets often have symmetric sizes, so $s_j$ is a sum over groups of $j$ primes. To avoid sign errors, write out the terms in a table by $j$ and add the column.

When the intersections of $j$ sets all have the same size $c_j$, then $s_j = \binom{n}{j}c_j$. Derangements ($c_j = (n-j)!$) and onto functions ($c_j = (n-j)^m$) are both of this kind, and so is any problem about "no item is in a forbidden position" when the forbidden positions don't interfere.

For a pigeonhole problem, say what the objects and the boxes are, and check the numbers: objects greater than boxes. If the claim is about a sum or a difference, the boxes are usually remainders. If it is about pairs, the boxes are often groups of numbers that make a bad pair, such as $\{1, 8\}, \{2, 7\}, \{3, 6\}, \{4, 5\}$ for sum 9. If the objects can be labelled in two ways, use pairs of labels as boxes, as in Erdős-Szekeres.

Estimate the answer to a derangement problem by $\frac{n!}{e}$, which is within $\frac{1}{2}$ of the exact count for $n \ge 1$: for $n = 8$, $\frac{40320}{2.71828} = 14{,}832.9$, and $D_8 = 14{,}833$.

## In code

The program checks inclusion-exclusion against brute force, the derangement formula and its limit, the onto-function formula, and the pigeonhole results.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import random
from bisect import bisect_left
from itertools import combinations, permutations, product
from math import comb, factorial

# Example 1: integers 1..1000 divisible by none of 2, 3, 5.
N = 1000
brute = sum(1 for x in range(1, N + 1) if x % 2 and x % 3 and x % 5)
ie = N - (N // 2 + N // 3 + N // 5) + (N // 6 + N // 10 + N // 15) - N // 30
print(brute, ie)                                           # 266 266

# Inclusion-exclusion on random sets (4 sets).
random.seed(1)
sets = [set(random.sample(range(30), 12)) for _ in range(4)]
union = len(set().union(*sets))
total = sum((-1) ** (j + 1) * len(set.intersection(*group))
            for j in range(1, 5) for group in combinations(sets, j))
print(union, total)                                        # 25 25

# Derangements: formula against brute force, and the limit 1/e.
def derangements(n):
    return sum((-1) ** k * factorial(n) // factorial(k) for k in range(n + 1))
for n in range(1, 9):
    brute = sum(1 for p in permutations(range(n)) if all(p[i] != i for i in range(n)))
    assert brute == derangements(n) == round(factorial(n) / math.e)
print([derangements(n) for n in range(1, 11)])
# [0, 1, 2, 9, 44, 265, 1854, 14833, 133496, 1334961]
print(round(derangements(10) / factorial(10), 6), round(1 / math.e, 6))   # 0.367879 0.367879

# Onto functions: formula against brute force.
def onto(m, n):
    return sum((-1) ** k * comb(n, k) * (n - k) ** m for k in range(n + 1))
for m, n in [(4, 3), (5, 3), (5, 2), (6, 3), (4, 4), (3, 4)]:
    brute = sum(1 for f in product(range(n), repeat=m) if len(set(f)) == n)
    print(m, n, onto(m, n), brute)
# 4 3 36 36 / 5 3 150 150 / 5 2 30 30 / 6 3 540 540 / 4 4 24 24 / 3 4 0 0

# Theorem 6: a block with sum divisible by n, in 20,000 random sequences.
random.seed(5)
for _ in range(20000):
    n = random.randint(1, 9)
    a = [random.randint(-50, 50) for _ in range(n)]
    assert any(sum(a[i:j]) % n == 0 for i in range(n) for j in range(i + 1, n + 1))
print("every sequence had a block")                        # every sequence had a block

# Theorem 7: monotone subsequences. Only the relative order matters, so use permutations.
def longest_increasing(seq):
    tails = []
    for x in seq:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
def longest_decreasing(seq):
    return longest_increasing([-x for x in seq])

for n in (2, 3):
    ok = all(max(longest_increasing(p), longest_decreasing(p)) >= n + 1
             for p in permutations(range(n * n + 1)))
    print(n, n * n + 1, ok)                                # 2 5 True / 3 10 True
tight = (3, 2, 1, 6, 5, 4, 9, 8, 7)
print(longest_increasing(tight), longest_decreasing(tight))   # 3 3
```

The Erdős-Szekeres check for $n = 3$ goes through all $10! = 3{,}628{,}800$ orders and takes a few seconds.

</details>

## FAQ

### Why do the signs alternate?

Each term corrects the one before. Adding the sizes counts an element in two sets twice, so subtracting the pairs fixes that, but it subtracts an element in three sets three times after adding it three times, leaving it at zero, so the triples are added back, and so on. The proof shows that the alternating signs are exactly what makes every element count once.

### Does the pigeonhole principle say which box has two objects?

No. It proves that some box does, and gives no way to find it. In Theorem 6 the proof does tell you where to look, since the two totals with the same remainder mark the block. In the 13 people and 12 months example, you would have to look at the birthdays to find the pair. Results of this kind are called existence proofs.

### Why is the answer to the hat-check problem about $\frac{1}{e}$ for every large $n$?

Because the exact answer is a partial sum of the series for $e^{-1}$, and the terms of that series shrink so fast that the partial sums are almost equal to the total after 5 or 6 terms. The number $e$ enters because the exact answer is a sum of reciprocals of factorials. The next lesson finds the same number as the probability of zero fixed points of a random permutation.

### Is $D_n$ the same as $\frac{n!}{e}$?

It is the nearest integer to it for $n \ge 1$, but $\frac{n!}{e}$ is not an integer, so the two can't be equal. To count derangements exactly, use the sum or the recurrence $D_n = (n-1)(D_{n-1} + D_{n-2})$, which gives $D_6 = 5(44 + 9) = 265$.

## Practice

### Warm-up

1\. In a group of 60 people, 30 speak French, 25 speak Spanish and 10 speak both. How many speak at least one of the two? How many speak neither?

<details class="solution" markdown>
<summary>Solution</summary>

By inclusion-exclusion, $30 + 25 - 10 = 45$ speak at least one. The other $60 - 45 = 15$ speak neither.

Check: French only is $30 - 10 = 20$, Spanish only is $25 - 10 = 15$, both is 10, and $20 + 15 + 10 = 45$.

</details>

2\. How many integers from 1 to 60 are divisible by 2, 3 or 5? How many are not?

<details class="solution" markdown>
<summary>Solution</summary>

The sizes are $\lvert A \rvert = 30$, $\lvert B \rvert = 20$, $\lvert C \rvert = 12$, then $\lvert A \cap B \rvert = 10$, $\lvert A \cap C \rvert = 6$, $\lvert B \cap C \rvert = 4$ and $\lvert A \cap B \cap C \rvert = 2$. The union is $30 + 20 + 12 - 10 - 6 - 4 + 2 = 44$. So $60 - 44 = 16$ are not divisible by any of them.

Check by listing the 16: 1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59.

</details>

3\. How many cards from a standard 52-card deck must you draw to be sure of (a) two cards of the same suit, (b) three cards of the same suit?

<details class="solution" markdown>
<summary>Solution</summary>

The boxes are the 4 suits. (a) With 5 cards, $\lceil \frac{5}{4} \rceil = 2$, and 4 cards can have all different suits, so 5 cards are needed. (b) With 9 cards, $\lceil \frac{9}{4} \rceil = 3$, and 8 cards can have two of each suit, so 9 are needed.

Check: $4 \cdot 2 = 8$ cards with at most two per suit exist, and 9 cannot, since $4 \cdot 2 < 9$.

</details>

### Standard

4\. Find $D_6$, and the number of permutations of 6 items that have exactly one fixed point.

<details class="solution" markdown>
<summary>Solution</summary>

By Theorem 2, $D_6 = 720 - 720 + 360 - 120 + 30 - 6 + 1 = 265$.

For exactly one fixed point: choose the fixed item (6 ways), and arrange the other 5 with no fixed point ($D_5 = 44$ ways), so $6 \cdot 44 = 264$.

Check: the probabilities of 0 and of exactly 1 fixed point are $\frac{265}{720} = 0.3681$ and $\frac{264}{720} = 0.3667$, both close to $\frac{1}{e}$. A brute-force count over the 720 permutations gives 265 and 264.

</details>

5\. Six different jobs are given to 4 workers, and every worker must get at least one job. How many assignments are there?

<details class="solution" markdown>
<summary>Solution</summary>

By Theorem 3 with $m = 6$ and $n = 4$:

$$
\text{Onto}(6, 4) = 4^6 - 4\cdot 3^6 + 6\cdot 2^6 - 4\cdot 1^6 = 4096 - 2916 + 384 - 4 = 1{,}560.
$$

Check: a brute-force count over all 4,096 assignments gives 1,560. As a second check, split by the sizes of the groups of jobs. Sizes $3, 1, 1, 1$: choose the worker with 3 jobs (4 ways), their 3 jobs ($\binom{6}{3} = 20$ ways), and give the other 3 jobs to the 3 other workers in $3! = 6$ ways, which is $4 \cdot 20 \cdot 6 = 480$. Sizes $2, 2, 1, 1$: choose the two workers with 2 jobs ($\binom{4}{2} = 6$ ways) and split the jobs into labelled groups of sizes $2, 2, 1, 1$ in $\frac{6!}{2!\,2!} = 180$ ways, which is $6 \cdot 180 = 1080$. Then $480 + 1080 = 1560$.

</details>

6\. (a) Show that among any 6 integers there are two whose difference is divisible by 5. (b) Show that if you choose 5 numbers from $\{1, 2, \dots, 8\}$, two of them add to 9.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The boxes are the remainders $0, 1, 2, 3, 4$ on division by 5. There are 6 integers and 5 boxes, so two integers have the same remainder, and their difference is a multiple of 5.

(b) The boxes are the four pairs $\{1, 8\}, \{2, 7\}, \{3, 6\}, \{4, 5\}$, each with sum 9. Five chosen numbers go into 4 boxes, so two are in the same pair, and they are the two numbers of that pair, which add to 9.

Check: five numbers are needed. The four numbers 1, 2, 3, 4 have no pair with sum 9. A program over all 56 five-element subsets of $\{1, \dots, 8\}$ finds a pair summing to 9 in each.

</details>

### Challenge

7\. Show that in any group of 6 people, there are 3 who all know each other or 3 who are all strangers to each other (knowing is mutual). Show that 5 people are not enough.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the generalized pigeonhole principle. What we want: three mutual acquaintances or three mutual strangers. The plan is to fix one person and look at how they relate to the other five.

*Proof.* Fix a person $P$. Each of the other 5 people either knows $P$ or doesn't, so these are 2 boxes, and some box holds at least $\lceil \frac{5}{2} \rceil = 3$ people. Suppose 3 people know $P$ (the other case is the same with "know" and "don't know" exchanged). If two of those three know each other, they and $P$ are three mutual acquaintances. If no two of them know each other, the three are mutual strangers. Either way we have the triple. $\blacksquare$

For 5 people, seat them in a circle and let each person know exactly their two neighbours. Any three people include two who are not neighbours, so no three are mutual acquaintances, and any three include two who are neighbours, so no three are mutual strangers.

Check: of the $2^{15}$ ways to mark each of the 15 pairs among 6 people as "know" or "don't", a program finds that every one has a triple of one kind, and for 5 people, 12 of the $2^{10}$ markings have none, all of them circles of acquaintance like the one above.

</details>

8\. (Reviews [counting rules](01-counting-rules.md).) How many bit strings of length 8 start with 1, or end with 00, or have 1 as the third bit?

<details class="solution" markdown>
<summary>Solution</summary>

Let $A$ be the strings that start with 1, $B$ those that end with 00, and $C$ those with third bit 1. Fixing $d$ bits leaves $2^{8-d}$ strings. So $\lvert A \rvert = 2^7 = 128$, $\lvert B \rvert = 2^6 = 64$ and $\lvert C \rvert = 128$, giving $s_1 = 320$. The pairs: $A \cap B$ fixes 3 bits, so 32; $A \cap C$ fixes 2 bits, so 64; $B \cap C$ fixes 3 bits, so 32; $s_2 = 128$. For the triple, 4 bits are fixed, so $s_3 = 16$. By inclusion-exclusion,

$$
320 - 128 + 16 = 208.
$$

Check: the complement is the strings that start with 0, don't end with 00 and have third bit 0. That is the strings with bits 1 and 3 equal to 0 (64 strings) and with the last two bits not 00 (three of four patterns, so $64 \cdot \frac{3}{4} = 48$), and $256 - 48 = 208$. A program that lists all 256 strings gives 208 too.

</details>

## Where this shows up

- The next lesson, [discrete probability](05-discrete-probability.md), turns these counts into probabilities: the chance that a random shuffle has no fixed point is $\frac{D_n}{n!}$, the first term of inclusion-exclusion is the union bound, and the birthday problem is a pigeonhole question with a probability attached.
- In CS, the pigeonhole principle proves that no lossless compression program can shrink every file (there are $2^L$ bit strings of length $L$ and only $2^L - 1$ shorter ones), that every hash function on unbounded inputs has collisions, and that a deterministic machine with a finite number of states must repeat a state on a long input, which is the [pumping lemma](../06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md). Inclusion-exclusion counts the cases of a program that satisfy at least one of several conditions.
- In number theory, inclusion-exclusion gives the formula for Euler's totient function (Example 1 is a case), which [RSA cryptography](../02-number-theory/06-rsa-cryptography.md) relies on. In surveys and economics data, the number of respondents with at least one of several overlapping traits is a union, and inclusion-exclusion is how the overlaps are corrected.
