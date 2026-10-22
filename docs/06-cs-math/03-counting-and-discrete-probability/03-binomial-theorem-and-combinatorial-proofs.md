# The binomial theorem and combinatorial proofs

After this lesson you can prove identities about binomial coefficients by counting one set in two ways, including Pascal's rule, the row sums, Vandermonde's identity and the hockey stick identity, and you can write such a proof in the standard form and check it numerically.

Before this: [counting rules](01-counting-rules.md), [permutations and combinations](02-permutations-and-combinations.md) and the high school [binomial theorem](../../03-high-school/11-sequences-series-and-counting/04-binomial-theorem.md), which expands powers of $(a+b)$ and proves Pascal's rule and the row sum. This lesson recasts those results as counting arguments and proves identities that the high school lesson doesn't reach.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find $\sum_{k=0}^{10} \binom{10}{k}$.
2. Find $\binom{10}{4} + \binom{10}{5}$ as a single binomial coefficient.
3. Without expanding, find the coefficient of $x^3$ in $(1+x)^5(1+x)^4$.

<details class="solution" markdown>
<summary>Answers</summary>

1. The sum of a row of Pascal's triangle is $2^{10} = 1{,}024$.
2. By Pascal's rule, $\binom{10}{4} + \binom{10}{5} = \binom{11}{5} = 462$. Check: $210 + 252 = 462$.
3. The product is $(1+x)^9$, and the coefficient of $x^3$ in it is $\binom{9}{3} = 84$.

</details>

## The idea

An identity such as $\binom{n}{k} = \binom{n}{n-k}$ can be proved by writing both sides with factorials. The proof is correct and shows nothing about why it is true. A different proof asks what each side counts. The left side counts the ways to choose the $k$ items you take, the right side the ways to choose the $n - k$ items you leave, and these are the same choice seen from the two ends. The identity stops being a coincidence of factorials.

That is a **combinatorial proof**: pick one set, count it in two different ways, and conclude that the two counts are equal. Each side of the identity is a count of the same set, arrived at by a different route, and a sum on one side usually comes from splitting the set into cases. The method works because a finite set has one size, whichever way you count it.

The method proves a great deal with very little algebra. The sum of a row of Pascal's triangle is the number of subsets of a set, sorted by size. Vandermonde's identity is a committee chosen from two groups, sorted by how many members came from the first group. The hockey stick identity sorts subsets by their largest element. Along the way the binomial theorem itself turns out to be a statement about bit strings.

## Definitions

An **identity** is an equation that holds for all values of the variables in a stated range, such as all integers $n \ge 0$ and $0 \le k \le n$. In plain words, it is a formula that is true every time, and a check on a few values is evidence and not proof.

A **combinatorial proof** of an identity $A = B$ of non-negative whole numbers is an argument that describes a finite set $S$ and shows that $\lvert S \rvert = A$ by one way of counting and $\lvert S \rvert = B$ by another. In plain words, you tell a counting story with two correct endings. A **bijective proof** is the variant that gives a bijection between a set counted by $A$ and a set counted by $B$, and then uses the bijection rule. Proving the same count two ways is also called **double counting**.

A **lattice path** from $(0, 0)$ to $(a, b)$ is a route along grid lines that uses only steps of 1 to the right and 1 up. In plain words, it is a shortest route through a city grid. It has exactly $a$ right steps and $b$ up steps, in some order.

The **binomial coefficient** $\binom{n}{k}$, for integers $0 \le k \le n$, is the number of $k$-element subsets of an $n$-element set, and $\binom{n}{k} = 0$ when $k > n$. The facts used from the earlier lessons are the product and division rules, the formula $\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$ and the symmetry $\binom{n}{k} = \binom{n}{n-k}$.

## How to do it

### Writing a combinatorial proof

1. Read each side as a count. A sum is cases, and a product is stages or a choice of two things. A binomial coefficient is a choice of a subset. A power $m^n$ is a list of $n$ items with $m$ choices each.
2. Find one story whose answer could be either side. Plug in small numbers to see it. On the left, ask what is being chosen. On the right, ask how the choice could be split into cases that give the terms of the sum.
3. Count the set the first way and say why the count is the left side. Then count the same set the second way. If you split into cases, say that the cases cover everything and don't overlap, so the sum rule applies.
4. State the conclusion: the two counts are of the same set, so they are equal.
5. Check the identity for a small case, and check that you counted the same set twice and not two different sets.

### The binomial theorem as a count

*Theorem 1 (binomial theorem).* For every integer $n \ge 0$ and all numbers $a$ and $b$,

$$
(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}\,a^{n-k}b^k.
$$

We know the distributive law and the product rule. We want the coefficient of $a^{n-k}b^k$. The plan is to turn each term of the expansion into a bit string and count the strings by their number of ones.

*Proof.* Multiplying out $(a+b)(a+b)\cdots(a+b)$, with $n$ brackets, means choosing $a$ or $b$ from each bracket, multiplying the choices, and adding up the $2^n$ products. Record a choice as a bit string of length $n$: the $i$-th bit is 1 if $b$ was taken from bracket $i$ and 0 if $a$ was. Different choices give different strings, and each string comes from one choice. A string with $k$ ones gives the product $a^{n-k}b^k$. The strings with exactly $k$ ones match the $k$-element subsets of the $n$ positions, the positions of the ones, so there are $\binom{n}{k}$ of them. So the term $a^{n-k}b^k$ appears $\binom{n}{k}$ times, and adding the groups over $k = 0, \dots, n$ gives the theorem. $\blacksquare$

Look back: this is the proof in the high school lesson with the choice written as a bit string, and the count of strings by their number of ones is the main fact used below. It also explains the name: the strings of length $n$, sorted by the number of ones, are exactly the rows of Pascal's triangle.

### Pascal's rule, two ways and a picture

*Theorem 2 (Pascal's rule).* For integers $n \ge 1$ and $1 \le k \le n$, $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.

*Proof by double counting.* Let $S$ be the set of $k$-element subsets of $\{1, \dots, n\}$, so $\lvert S \rvert = \binom{n}{k}$. Split $S$ by whether the subset contains the element $n$. The subsets that contain $n$ match the $(k-1)$-element subsets of $\{1, \dots, n-1\}$, by removing $n$: $\binom{n-1}{k-1}$ of them. The subsets that don't contain $n$ are the $k$-element subsets of $\{1, \dots, n-1\}$: $\binom{n-1}{k}$. The cases don't overlap and cover $S$, so $\lvert S \rvert = \binom{n-1}{k-1} + \binom{n-1}{k}$. $\blacksquare$

*Proof by algebra.* Write the right side with factorials over the common denominator $k!\,(n-k)!$. Since $\frac{(n-1)!}{(k-1)!\,(n-k)!} = \frac{k\,(n-1)!}{k!\,(n-k)!}$ and $\frac{(n-1)!}{k!\,(n-1-k)!} = \frac{(n-k)\,(n-1)!}{k!\,(n-k)!}$, the sum is $\frac{(k + n - k)\,(n-1)!}{k!\,(n-k)!} = \frac{n!}{k!\,(n-k)!}$. $\blacksquare$

The third proof is a picture. The number of lattice paths from $(0, 0)$ to $(a, b)$ is $\binom{a+b}{a}$, because a path is a string of $a$ right steps and $b$ up steps, and it is determined by which $a$ of its $a + b$ steps are right. Every path to $(a, b)$ ends with either a right step from $(a-1, b)$ or an up step from $(a, b-1)$, and these cases don't overlap. So the number of paths to a point is the sum of the numbers for the point to its left and the point below it, which is Pascal's rule. The figure shows the number of paths to each point of a grid, which is Pascal's triangle turned on its side.

![A grid of points from (0, 0) to (4, 3). Each point shows the number of lattice paths to it from (0, 0): the bottom row and left column are all 1, and each other number is the sum of the number to its left and the number below it. The point (4, 3) shows 35, the sum of 20 from the point to its left and 15 from the point below it.](../../assets/figures/06-cs-math/binomial-theorem-and-combinatorial-proofs-lattice.svg)

Look back: the algebraic proof says that the rule is true, the counting proof says why, and the grid shows the rule at work, since filling in the grid adds numbers and nothing else. The point $(4, 3)$ shows $\binom{7}{3} = 35 = \binom{6}{2} + \binom{6}{3} = 15 + 20$.

### Row sums

*Theorem 3.* For $n \ge 0$, $\sum_{k=0}^{n}\binom{n}{k} = 2^n$. For $n \ge 1$, $\sum_{k=0}^{n}(-1)^k\binom{n}{k} = 0$.

We know that a set with $n$ elements has $2^n$ subsets, and that $\binom{n}{k}$ counts the subsets of size $k$. We want both sums. The plan is to count subsets by size for the first, and to pair up the subsets for the second.

*Proof.* Let $S$ be the set of all subsets of $\{1, \dots, n\}$. Counting them with Theorem 2 of [counting rules](01-counting-rules.md) gives $2^n$. Counting them by size gives $\binom{n}{k}$ subsets of size $k$ for each $k$ from 0 to $n$, and the sizes cover everything with no overlap, so the sum is $\lvert S \rvert$. That proves the first sum.

For the second sum, define $T$ to be the subset obtained from a subset $S$ of $\{1, \dots, n\}$ by toggling the element 1, adding it if it is absent and removing it if it is present. Toggling changes the size by exactly 1, so it turns an even-sized subset into an odd-sized one and the other way round, and toggling twice gives back $S$. So toggling is a bijection from the even-sized subsets to the odd-sized ones, and the two groups have the same size. The second sum is the number of even-sized subsets minus the number of odd-sized ones, which is 0. This needs the element 1 to exist, so $n \ge 1$. $\blacksquare$

Look back: the first proof is the same as setting $a = b = 1$ in the binomial theorem, and the second explains why $a = 1$ and $b = -1$ gives 0: the even-sized and odd-sized subsets cancel in pairs. A pairing that reverses the sign, like toggling, is the standard way to prove an identity with minus signs by counting. For $n = 0$ the second sum is $\binom{0}{0} = 1$, not 0, and the toggling proof fails because there is no element 1.

### Committee identities

Three more identities come from stories about committees.

*Theorem 4.* For $n \ge 1$, $\sum_{k=0}^{n} k\binom{n}{k} = n\,2^{n-1}$. For $0 \le j \le k \le n$, $\binom{n}{k}\binom{k}{j} = \binom{n}{j}\binom{n-j}{k-j}$.

*Proof.* For the first identity, let $S$ be the set of pairs (committee, chair), where the committee is any subset of $n$ people and the chair is a member of it. Counting by the size of the committee: for each $k$ there are $\binom{n}{k}$ committees and $k$ choices of chair, so $\lvert S \rvert = \sum_k k\binom{n}{k}$. Counting by the chair first: there are $n$ choices of chair, and then each of the other $n - 1$ people is in or out of the committee, which gives $2^{n-1}$ committees. So $\lvert S \rvert = n\,2^{n-1}$.

For the second, let $S$ be the set of pairs (committee of $k$ people, subcommittee of $j$ of them). Choosing the committee first and then its subcommittee gives $\binom{n}{k}\binom{k}{j}$. Choosing the subcommittee first, from all $n$ people, and then adding the other $k - j$ members of the committee from the $n - j$ people left gives $\binom{n}{j}\binom{n-j}{k-j}$. $\blacksquare$

Look back: the idea that a sum with a weight $k$ is a pair, a committee with a chosen member, repeats in many proofs. It is the identity $k\binom{n}{k} = n\binom{n-1}{k-1}$ of the high school lesson, summed over $k$: the right sides add to $n\sum_k\binom{n-1}{k-1} = n\,2^{n-1}$.

### Vandermonde's identity

*Theorem 5 (Vandermonde's identity).* For integers $m, n, r \ge 0$,

$$
\sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}.
$$

We know that a binomial coefficient counts committees, and the product rule. We want a story for both sides. The plan is to choose $r$ people from a group of $m$ men and $n$ women, and sort the committees by how many men they hold.

*Proof.* Let $S$ be the set of committees of $r$ people chosen from $m$ men and $n$ women together. The group has $m + n$ people, so $\lvert S \rvert = \binom{m+n}{r}$. Now count by the number $k$ of men on the committee, which can be $0, 1, \dots, r$. A committee with $k$ men is built by choosing the men from the $m$ men, $\binom{m}{k}$ ways, and the women, $r - k$ of them, from the $n$ women, $\binom{n}{r-k}$ ways. By the product rule there are $\binom{m}{k}\binom{n}{r-k}$ committees with exactly $k$ men. Every committee has some number of men, and no committee has two, so the sum rule gives $\lvert S \rvert = \sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k}$. $\blacksquare$

Look back: terms with $k > m$ or $r - k > n$ are 0, so the sum can run over all $k$ from 0 to $r$ without worrying. Algebra gives a second proof. The coefficient of $x^r$ in $(1+x)^m(1+x)^n$ is $\sum_k\binom{m}{k}\binom{n}{r-k}$ (take $x^k$ from the first factor and $x^{r-k}$ from the second), and the product is $(1+x)^{m+n}$, whose coefficient of $x^r$ is $\binom{m+n}{r}$. That is Quick check 3.

A special case with $m = n = r$ is useful. Since $\binom{n}{r-k}$ with $r = n$ equals $\binom{n}{k}$ by symmetry,

$$
\sum_{k=0}^{n}\binom{n}{k}^2 = \binom{2n}{n}.
$$

For $n = 4$: $1 + 16 + 36 + 16 + 1 = 70 = \binom{8}{4}$.

### The hockey stick identity

*Theorem 6 (hockey stick identity).* For integers $0 \le r \le n$,

$$
\sum_{i=r}^{n}\binom{i}{r} = \binom{r}{r} + \binom{r+1}{r} + \cdots + \binom{n}{r} = \binom{n+1}{r+1}.
$$

We know that $\binom{n+1}{r+1}$ counts the subsets of size $r + 1$ of $\{1, \dots, n+1\}$. We want to split those subsets so that the pieces are the terms of the sum. The plan is to sort them by their largest element.

*Proof.* Let $S$ be the set of $(r+1)$-element subsets of $\{1, 2, \dots, n+1\}$, so $\lvert S \rvert = \binom{n+1}{r+1}$. Sort the subsets by their largest element, which can be $r + 1, r + 2, \dots, n + 1$ (a subset of size $r + 1$ needs at least $r + 1$ elements). If the largest element is $i + 1$, the other $r$ elements are any $r$-element subset of $\{1, \dots, i\}$, which gives $\binom{i}{r}$ subsets. Summing over $i = r, \dots, n$ gives $\sum_{i=r}^{n}\binom{i}{r}$. The cases cover every subset exactly once. $\blacksquare$

Look back: the name comes from Pascal's triangle. The entries $\binom{r}{r}, \binom{r+1}{r}, \dots, \binom{n}{r}$ run down a diagonal, like the shaft of a hockey stick, and their sum is the entry just below and to the side, the blade. A second proof is by repeated use of Pascal's rule: $\binom{n+1}{r+1} = \binom{n}{r} + \binom{n}{r+1}$, then $\binom{n}{r+1} = \binom{n-1}{r} + \binom{n-1}{r+1}$, and so on until the last term is $\binom{r+1}{r+1} = \binom{r}{r}$.

With $r = 1$ the identity says $1 + 2 + \cdots + n = \binom{n+1}{2}$, the formula for the sum of the first $n$ integers. Since $i^2 = 2\binom{i}{2} + i$ for every integer $i$, summing the identity for $r = 2$ and $r = 1$ gives the sum of squares: $\sum_{i=1}^{n} i^2 = 2\binom{n+1}{3} + \binom{n+1}{2} = \frac{n(n+1)(2n+1)}{6}$. [Sums and closed forms](../04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md) uses this method to find sums of polynomials.

### The multinomial theorem

*Theorem 7 (multinomial theorem).* For $m \ge 1$ and $n \ge 0$,

$$
(x_1 + x_2 + \cdots + x_m)^n = \sum \frac{n!}{n_1!\,n_2!\cdots n_m!}\,x_1^{n_1}x_2^{n_2}\cdots x_m^{n_m},
$$

where the sum is over all lists of non-negative integers $(n_1, \dots, n_m)$ with $n_1 + \cdots + n_m = n$.

*Proof.* As in Theorem 1, multiplying out $n$ brackets means choosing one of $x_1, \dots, x_m$ from each bracket, so each term is a word of length $n$ over the letters $x_1, \dots, x_m$. A word with $n_i$ copies of $x_i$ gives the product $x_1^{n_1}\cdots x_m^{n_m}$, and by the previous lesson there are $\frac{n!}{n_1!\cdots n_m!}$ such words. Adding over all lists $(n_1, \dots, n_m)$ gives the theorem. $\blacksquare$

Look back: with $x_1 = \cdots = x_m = 1$ the theorem says that the multinomial coefficients add up to $m^n$, the number of words of length $n$ over $m$ letters, grouped by how many times each letter occurs. With $m = 2$ it is the binomial theorem.

## Worked examples

<div class="example" markdown>

### Example 1: a story for a weighted sum

Prove that $\sum_{k=0}^{6} k\binom{6}{k} = 6 \cdot 2^5 = 192$, by the method of Theorem 4, and say why the steps work.

Step 1: the left side is a sum over $k$ of a product, so it counts pairs, with $\binom{6}{k}$ ways to choose a group of $k$ and $k$ ways to pick one of its members. The right side is $6$ choices times $2^5$ choices, which looks like "choose one person, then decide yes or no for each of the other five".

Step 2: the story is committees of any size from 6 people, with a chair chosen from the committee. A pair (committee, chair) is one outcome, and no outcome is counted twice.

Step 3: count by committee size: $\sum_k k\binom{6}{k}$. Count by chair first: 6 chairs, and for each of the other 5 people, in or out, which is $2^5 = 32$ committees. So $6 \cdot 32 = 192$.

Step 4: the two counts are of the same set, so they are equal.

Step 5, the check: the terms $k\binom{6}{k}$ for $k = 0, \dots, 6$ are $0, 6, 30, 60, 60, 30, 6$, and $6 + 30 + 60 + 60 + 30 + 6 = 192$. The empty committee has no chair, so it is not in the set at all, and the $k = 0$ term of the sum is 0.

</div>

<div class="example" markdown>

### Example 2: Vandermonde with numbers

A committee of 3 is chosen from 5 men and 4 women. Show how the identity splits the count.

All committees of 3 from 9 people: $\binom{9}{3} = 84$. By the number of men on the committee:

| Men | Women | Count |
|---|---|---|
| 0 | 3 | $\binom{5}{0}\binom{4}{3} = 4$ |
| 1 | 2 | $\binom{5}{1}\binom{4}{2} = 30$ |
| 2 | 1 | $\binom{5}{2}\binom{4}{1} = 40$ |
| 3 | 0 | $\binom{5}{3}\binom{4}{0} = 10$ |

The four counts add to $4 + 30 + 40 + 10 = 84$, as Theorem 5 says. Check by listing: a program that generates all 84 committees and counts the men in each finds the same four counts.

</div>

<div class="example" markdown>

### Example 3: the hockey stick

Find $\binom{2}{2} + \binom{3}{2} + \binom{4}{2} + \binom{5}{2} + \binom{6}{2} + \binom{7}{2}$.

This is the hockey stick sum with $r = 2$ and $n = 7$, so the total is $\binom{8}{3} = 56$. In the proof, the sets are the 3-element subsets of $\{1, \dots, 8\}$, grouped by their largest element $3, 4, \dots, 8$, and the group with largest element $i + 1$ has $\binom{i}{2}$ members.

Check by adding: $1 + 3 + 6 + 10 + 15 + 21 = 56$.

</div>

<div class="example" markdown>

### Example 4: a sum with a power, and three colours

Prove that $\sum_{k=0}^{n}\binom{n}{k}2^k = 3^n$ by a counting argument.

Let $S$ be the set of words of length $n$ over the letters $\{a, b, c\}$. There are $3^n$ of them, since each position has 3 choices. Now count by the number $k$ of positions that don't hold $c$. Choose which $k$ positions: $\binom{n}{k}$ ways. Each of those positions holds $a$ or $b$, $2^k$ ways, and the other positions hold $c$. The cases for $k = 0, \dots, n$ cover every word once. So $\lvert S \rvert = \sum_k\binom{n}{k}2^k$ as well.

Check with $n = 4$: the terms are $\binom{4}{k}2^k = 1, 8, 24, 32, 16$, and their sum is $81 = 3^4$. This is also the binomial theorem with $a = 1$ and $b = 2$.

</div>

<div class="example" markdown>

### Example 5: finish it yourself

Prove the second identity of Theorem 4, $\binom{n}{k}\binom{k}{j} = \binom{n}{j}\binom{n-j}{k-j}$, for $n = 7$, $k = 4$, $j = 2$, and check it numerically.

The left side is done in the theorem: choose a committee of 4 from 7 people, and then a subcommittee of 2 from it, so $\binom{7}{4}\binom{4}{2}$. Count the same pairs (committee, subcommittee) by choosing the subcommittee first.

<details class="solution" markdown>
<summary>Finish</summary>

Choose the subcommittee of 2 from all 7 people: $\binom{7}{2} = 21$ ways. Then add the other $4 - 2 = 2$ members of the committee from the $7 - 2 = 5$ people who are not in the subcommittee: $\binom{5}{2} = 10$ ways. A pair (committee, subcommittee) is determined by these two choices, and each pair arises once, so the count is $21 \cdot 10 = 210$.

Check: $\binom{7}{4}\binom{4}{2} = 35 \cdot 6 = 210$, which agrees.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out at step 5: both counts must be of the same set. A story in which the left side counts committees and the right side counts committees with a chair has not proved anything about either. Write the set $S$ down in one sentence, and make each count start from that sentence.

</div>

<div class="warning" markdown>

Watch out at step 3: cases must cover the set without overlap. In Vandermonde's identity the cases are labelled by the number of men, and each committee has one such number. Sorting a hand of cards by "contains an ace" and "contains a king" would overlap, since a hand can have both, and the sum rule would not apply.

</div>

<div class="warning" markdown>

Watch out: checking an identity for several values of $n$ is not a proof. The identities in this lesson are true for every $n$, and a numerical check is the way to catch a slip in the statement, such as a missing term or the wrong upper limit. The proof is the counting argument.

</div>

<div class="warning" markdown>

Watch out for the numbers in the hockey stick: the right side has $n + 1$ and $r + 1$, one more than the end of the sum and one more than the lower index, in both places. So $\sum_{i=2}^{7}\binom{i}{2} = \binom{8}{3}$, not $\binom{7}{3}$ or $\binom{7}{2}$. The sum starts at $i = r$ because the terms with $i < r$ are 0, and starting earlier gives the same total.

</div>

Some small cases. For $n = 0$ the row sum is $\binom{0}{0} = 1 = 2^0$, and the alternating sum is 1, not 0. A weighted sum such as $\sum_k k\binom{n}{k}$ has a zero term at $k = 0$. Vandermonde with $r > m + n$ has all terms 0 on both sides, and with $r = 0$ it says $1 = 1$. Identities with a subtraction, such as the alternating sum, cannot be proved by adding up cases, and need a pairing that reverses the sign, like toggling an element.

## Tricks and shortcuts

To find the story for an identity, put in small numbers and list what each side counts. For $n = 3$, a sum like $\sum_k\binom{3}{k}2^k = 27$ can be matched with the 27 words over three letters.

A product of two binomial coefficients is two successive choices, so Vandermonde-type sums come from choosing from two groups. A sum over an upper index, like the hockey stick, comes from conditioning on a largest or smallest element. A factor $k$ inside a sum comes from naming a member.

Algebra is a check on a combinatorial proof, not the other way round. The identities of this lesson all follow from $(1+x)^{m}(1+x)^{n} = (1+x)^{m+n}$ and its relatives, by comparing coefficients, and trying the algebra often shows which story is hiding.

A binomial coefficient in a sum of probabilities, such as a probability of $k$ heads in $n$ flips, is a count of strings, so row sums say that the probabilities of a fair coin add to 1: $\frac{1}{2^n}\sum_k\binom{n}{k} = 1$.

## In code

The program checks every identity of the lesson for small values, and counts the sets from the proofs by brute force. A check is not a proof, but it catches a wrong statement at once.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import combinations, product
from math import comb, factorial

# Identities for n = 0, ..., 12.
for n in range(13):
    assert sum(comb(n, k) for k in range(n + 1)) == 2**n
    if n >= 1:
        assert sum((-1) ** k * comb(n, k) for k in range(n + 1)) == 0
        assert sum(k * comb(n, k) for k in range(n + 1)) == n * 2 ** (n - 1)
    assert sum(comb(n, k) ** 2 for k in range(n + 1)) == comb(2 * n, n)
    assert sum(comb(n, k) * 2**k for k in range(n + 1)) == 3**n
    for r in range(n + 1):
        assert sum(comb(i, r) for i in range(r, n + 1)) == comb(n + 1, r + 1)
    for m in range(8):
        for r in range(8):
            assert sum(comb(m, k) * comb(n, r - k) for k in range(r + 1)) == comb(m + n, r)
print("all identities hold")                                   # all identities hold

# Example 1: (committee, chair) pairs for 6 people.
people = range(6)
pairs = [(c, chair) for r in range(7) for c in combinations(people, r) for chair in c]
print(len(pairs), 6 * 2**5)                                    # 192 192

# Example 2: committees of 3 from 5 men (0 to 4) and 4 women (5 to 8), by number of men.
committees = list(combinations(range(9), 3))
by_men = [sum(1 for c in committees if sum(1 for p in c if p < 5) == k) for k in range(4)]
print(len(committees), by_men)                                 # 84 [4, 30, 40, 10]

# Lattice paths by recursion: paths(a, b) = paths(a - 1, b) + paths(a, b - 1).
def paths(a, b):
    if a == 0 or b == 0:
        return 1
    return paths(a - 1, b) + paths(a, b - 1)
print(paths(4, 3), comb(7, 3))                                 # 35 35

# Example 4: words over {a, b, c} by the number of positions that are not c.
n = 4
print(3**n, [comb(n, k) * 2**k for k in range(n + 1)])         # 81 [1, 8, 24, 32, 16]

# Multinomial theorem: the coefficients of (x + y + z)^3 add to 3^3.
coeffs = [factorial(3) // (factorial(i) * factorial(j) * factorial(3 - i - j))
          for i in range(4) for j in range(4 - i)]
print(sum(coeffs), 3**3)                                       # 27 27
```

The `assert` lines raise an error if an identity fails, so reaching the first print means every one held for the ranges tested.

</details>

## FAQ

### Why bother with combinatorial proofs when algebra works?

Algebra proves that an identity is true, and a counting story shows why. A story also tells you what to do with the identity: the hockey stick identity is a statement about largest elements, and that is how you recognize it in a new problem. Some identities are much shorter by counting, and others are much shorter by algebra. A good habit is to know both and to use one as a check on the other.

### Can every identity be proved by counting?

Not by the simple method here. A counting proof needs both sides to be sizes of sets, so an identity with a minus sign or a fraction needs more care. A minus sign can be handled by a pairing that reverses the sign, as for the alternating sum. A fraction usually becomes a division rule, as in $\binom{n}{k} = \frac{P(n, k)}{k!}$. When neither works, an algebraic or induction proof is the right tool.

### Is the hockey stick the same as Pascal's rule?

It follows from it. Applying Pascal's rule repeatedly splits $\binom{n+1}{r+1}$ into a sum of the terms along the diagonal, which is the second proof above. The counting proof, sorting by the largest element, is a separate argument and has the same result.

### What does Pascal's rule say at the edges, when $k = 0$ or $k = n$?

With the conventions $\binom{n}{k} = 0$ for $k > n$ and for $k < 0$, the rule holds for those values too: $\binom{n}{0} = \binom{n-1}{-1} + \binom{n-1}{0} = 0 + 1$, and $\binom{n}{n} = \binom{n-1}{n-1} + \binom{n-1}{n} = 1 + 0$. That is why the rule builds a whole row of the triangle, the 1s at the ends included, from the row above padded with zeros.

## Practice

### Warm-up

1\. Check Pascal's rule for $n = 10$ and $k = 4$, and check Vandermonde's identity with $m = 6$, $n = 5$ and $r = 4$ by listing the terms.

<details class="solution" markdown>
<summary>Solution</summary>

Pascal: $\binom{10}{4} = 210$, and $\binom{9}{3} + \binom{9}{4} = 84 + 126 = 210$.

Vandermonde: the right side is $\binom{11}{4} = 330$. The terms $\binom{6}{k}\binom{5}{4-k}$ for $k = 0, 1, 2, 3, 4$ are $1 \cdot 5 = 5$, $6 \cdot 10 = 60$, $15 \cdot 10 = 150$, $20 \cdot 5 = 100$ and $15 \cdot 1 = 15$. They add to $5 + 60 + 150 + 100 + 15 = 330$.

Check: the terms are the numbers of committees of 4 from 6 men and 5 women with $k$ men, and they cover every committee once.

</details>

2\. For $n = 12$, find (a) $\sum_{k}\binom{12}{k}$, (b) the sum over even $k$ only, and (c) $\sum_k k\binom{12}{k}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $2^{12} = 4{,}096$. (b) The alternating sum is 0, so the even-$k$ terms and odd-$k$ terms are equal and each is $\frac{4096}{2} = 2{,}048$. (c) $12 \cdot 2^{11} = 12 \cdot 2048 = 24{,}576$.

Check (c) by the story: choose a chair among 12 people (12 ways) and let each of the other 11 be in or out ($2^{11}$ ways).

</details>

3\. Find $\binom{3}{3} + \binom{4}{3} + \cdots + \binom{10}{3}$.

<details class="solution" markdown>
<summary>Solution</summary>

This is the hockey stick sum with $r = 3$ and $n = 10$, so it equals $\binom{11}{4} = 330$.

Check by adding: $1 + 4 + 10 + 20 + 35 + 56 + 84 + 120 = 330$.

</details>

### Standard

4\. Prove $\sum_{k=0}^{n}\binom{n}{k}^2 = \binom{2n}{n}$ by counting, using Vandermonde's identity, and check it for $n = 5$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Vandermonde's identity and the symmetry $\binom{n}{k} = \binom{n}{n-k}$. What we want: the sum of squares. The plan is to set $m = n$ and $r = n$ in the identity.

*Proof.* A committee of $n$ people is chosen from $n$ men and $n$ women, so there are $\binom{2n}{n}$ committees. By the number $k$ of men there are $\binom{n}{k}\binom{n}{n-k}$ committees with $k$ men, and $\binom{n}{n-k} = \binom{n}{k}$ by symmetry. So $\binom{2n}{n} = \sum_k\binom{n}{k}^2$. $\blacksquare$

Check with $n = 5$: the squares of the row $1, 5, 10, 10, 5, 1$ are $1, 25, 100, 100, 25, 1$, and they add to $252 = \binom{10}{5}$.

</details>

5\. Use the hockey stick identity to prove that $1^2 + 2^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$, and check it for $n = 10$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $i^2 = 2\binom{i}{2} + i$, because $2\binom{i}{2} = i(i-1)$ and $i(i-1) + i = i^2$. What we want: the sum of the squares. The plan is to sum both parts with the hockey stick.

*Proof.* Summing $i^2 = 2\binom{i}{2} + i$ over $i = 1, \dots, n$ gives $2\sum_{i=1}^{n}\binom{i}{2} + \sum_{i=1}^{n}\binom{i}{1}$. The hockey stick identity gives $\sum_{i=2}^{n}\binom{i}{2} = \binom{n+1}{3}$ (the term $i = 1$ is 0) and $\sum_{i=1}^{n}\binom{i}{1} = \binom{n+1}{2}$. So the sum is $2\binom{n+1}{3} + \binom{n+1}{2} = \frac{(n+1)n(n-1)}{3} + \frac{(n+1)n}{2} = \frac{n(n+1)\bigl(2(n-1) + 3\bigr)}{6} = \frac{n(n+1)(2n+1)}{6}$. $\blacksquare$

Check with $n = 10$: $2\binom{11}{3} + \binom{11}{2} = 2 \cdot 165 + 55 = 385$, and $\frac{10 \cdot 11 \cdot 21}{6} = 385$, which is $1 + 4 + 9 + \cdots + 100$.

</details>

6\. Find the coefficient of $x^2y^3z$ in $(x + y + z)^6$, and say what the sum of all coefficients of $(x + y + z)^6$ is.

<details class="solution" markdown>
<summary>Solution</summary>

By the multinomial theorem, the coefficient is $\frac{6!}{2!\,3!\,1!} = \frac{720}{12} = 60$. All the coefficients add up to the value at $x = y = z = 1$, which is $3^6 = 729$.

Check: the coefficient counts the words of length 6 with two x's, three y's and one z. Choose the places of the x's ($\binom{6}{2} = 15$), then of the y's among the 4 left ($\binom{4}{3} = 4$), and the z goes in the last place: $15 \cdot 4 = 60$.

</details>

### Challenge

7\. Prove by counting that $\sum_{k=0}^{n}k^2\binom{n}{k} = n(n+1)\,2^{n-2}$ for $n \ge 2$. Check it for $n = 4$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the committee-and-chair method. What we want: a story for $k^2$. The plan is to count committees with a president and a secretary, who may be the same person.

*Proof.* Let $S$ be the set of triples (committee, president, secretary) from $n$ people, where the president and the secretary are members of the committee and may be the same person. Counting by the committee size $k$: there are $\binom{n}{k}$ committees, $k$ choices of president and $k$ of secretary, so $\lvert S \rvert = \sum_k k^2\binom{n}{k}$.

Counting by cases on whether the two offices are held by the same person. If they are, choose that person ($n$ ways), and each of the other $n - 1$ people is in or out, $2^{n-1}$ ways: $n\,2^{n-1}$. If they are held by different people, choose them in order ($n(n-1)$ ways), and each of the other $n - 2$ people is in or out: $n(n-1)\,2^{n-2}$. The cases don't overlap, so $\lvert S \rvert = n\,2^{n-1} + n(n-1)\,2^{n-2} = n\,2^{n-2}\bigl(2 + n - 1\bigr) = n(n+1)\,2^{n-2}$. $\blacksquare$

Check with $n = 4$: $\sum_k k^2\binom{4}{k} = 4 + 24 + 36 + 16 = 80$, and $4 \cdot 5 \cdot 2^2 = 80$.

</details>

8\. (Reviews [mathematical induction](../../04-proofs-and-logic/05-induction/01-mathematical-induction.md).) Prove by induction on $m$ that $\sum_{k=0}^{m}(-1)^k\binom{n}{k} = (-1)^m\binom{n-1}{m}$ for fixed $n \ge 1$ and $0 \le m \le n - 1$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Pascal's rule, $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$. What we want: the partial alternating sum. The plan is to induct on $m$, fixing $n$.

*Proof.* Base case, $m = 0$: the left side is $\binom{n}{0} = 1$ and the right side is $\binom{n-1}{0} = 1$.

Step: suppose the statement holds for some $m$ with $m + 1 \le n - 1$. Then

$$
\sum_{k=0}^{m+1}(-1)^k\binom{n}{k} = (-1)^m\binom{n-1}{m} + (-1)^{m+1}\binom{n}{m+1}.
$$

By Pascal's rule, $\binom{n}{m+1} = \binom{n-1}{m} + \binom{n-1}{m+1}$, so the right side is $(-1)^m\binom{n-1}{m} - (-1)^m\binom{n-1}{m} + (-1)^{m+1}\binom{n-1}{m+1} = (-1)^{m+1}\binom{n-1}{m+1}$. That is the statement for $m + 1$. $\blacksquare$

Check with $n = 6$ and $m = 3$: $1 - 6 + 15 - 20 = -10$, and $(-1)^3\binom{5}{3} = -10$. With $m = n$ the formula would need $\binom{n-1}{n} = 0$, which agrees with the full alternating sum being 0.

</details>

## Where this shows up

- The next lesson, [inclusion-exclusion and the pigeonhole principle](04-inclusion-exclusion-and-pigeonhole.md), uses the alternating sum of Theorem 3 to prove inclusion-exclusion, and the multinomial coefficients return in counting surjections. [Discrete probability](05-discrete-probability.md) uses row sums to check that probabilities add to 1.
- In algorithms, Pascal's rule is the dynamic programming recurrence for computing $\binom{n}{k}$ without large factorials, and the count of lattice paths is the count of routes in a grid. The hockey stick identity turns the cost of nested loops, such as the number of pairs $i < j$ or triples $i < j < k$, into closed forms. Vandermonde's identity shows that the sum of independent binomial random variables with the same $p$ is binomial, as in [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md).
- In finance, the number of paths to each node of a binomial price tree is a lattice-path count, and the row sums of Pascal's triangle check that the probabilities of the nodes at each level add to 1. In statistics, $\binom{n}{k}$ is the number of ways to assign $n$ subjects to a treatment group of size $k$ and a control group, the count behind randomization tests.
