# Discrete probability

After this lesson you can compute probabilities by counting, use indicator variables and linearity of expectation to find expected values without independence, solve the birthday and coupon collector problems, and use the union bound to analyze hashing.

Before this: [counting rules](01-counting-rules.md), [inclusion-exclusion and the pigeonhole principle](04-inclusion-exclusion-and-pigeonhole.md), [sample spaces, events and axioms](../../05-university-core/07-probability/01-sample-spaces-events-and-axioms.md) and [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md). Those lessons teach the axioms, random variables and the named distributions. This lesson is the discrete-math view: counting, indicators and a few classic problems from algorithms.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A random 8-bit string is chosen, all $2^8$ strings equally likely. What is the probability that it has exactly 3 ones?
2. A fair die is rolled 12 times. What is the expected number of sixes?
3. A fair die is rolled until the first six appears. What is the expected number of rolls?

<details class="solution" markdown>
<summary>Answers</summary>

1. There are $\binom{8}{3} = 56$ strings with three ones, so the probability is $\frac{56}{256} = \frac{7}{32} \approx 0.219$.
2. Each roll is a six with probability $\frac{1}{6}$, so by linearity the expected number is $12 \cdot \frac{1}{6} = 2$.
3. The number of rolls is geometric with $p = \frac{1}{6}$, so the mean is $\frac{1}{p} = 6$.

</details>

## The idea

When all outcomes are equally likely, probability is counting: the probability of an event is the number of outcomes in it divided by the number of outcomes. Everything in the first four lessons of this chapter is a tool for finding those two numbers. The harder questions ask for an average instead of a probability, such as how many people get their own hat back, how many empty slots a hash table has, or how many random draws it takes to see every card in a deck.

A direct attack on those averages needs the whole distribution, and the distributions are messy. The trick of this lesson is to write the count as a sum of yes-or-no variables, one per item, and add up the expected values. The expected value of a yes-or-no variable is just the probability of yes, and the expected value of a sum is the sum of the expected values, even when the variables depend on each other. A question that looked like it needed the distribution of a complicated count turns into a sum of simple probabilities.

The same few ideas answer the central questions about hashing: how many items fit before a collision is likely (the birthday problem), how many random probes cover every slot (the coupon collector problem), and how large a table must be to avoid collisions with good probability (the union bound).

## Definitions

An experiment has a **uniform** sample space $\Omega$ if $\Omega$ is finite and every outcome has the same probability. Then for each event $A \subseteq \Omega$,

$$
P(A) = \frac{\lvert A \rvert}{\lvert \Omega \rvert}.
$$

In plain words, count the outcomes you want and divide by the count of all outcomes. The rule is valid only when the outcomes really are equally likely, so the sample space must be chosen so that they are, as the [sample spaces lesson](../../05-university-core/07-probability/01-sample-spaces-events-and-axioms.md) stresses.

A **random variable** $X$ is a function from $\Omega$ to the real numbers, and its **expected value** is $E[X] = \sum_{\omega \in \Omega}X(\omega)P(\{\omega\})$, the average of $X$ weighted by probability. The **indicator variable** of an event $A$ is the random variable $I_A$ with $I_A(\omega) = 1$ if $\omega \in A$ and $0$ otherwise. In plain words, an indicator is a switch that is on when the event happens, and a count of how many events happen is a sum of switches.

Since $I_A$ takes the value 1 on the outcomes in $A$ and 0 elsewhere,

$$
E[I_A] = 1 \cdot P(A) + 0 \cdot P(A^c) = P(A).
$$

A **geometric waiting time** with success probability $p$ is the number of independent trials up to and including the first success. Its mean is $\frac{1}{p}$, from [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md).

## How to do it

### Probability by counting

1. Describe an outcome, and choose a sample space whose outcomes are equally likely.
2. Count $\lvert \Omega \rvert$ and $\lvert A \rvert$ with the same view of an outcome. If $\Omega$ counts ordered lists, so must $A$.
3. Divide. For "at least one", count the complement.
4. Check that the answer is between 0 and 1, and test the method on a tiny case.

### Expected values by indicators

1. Write the count you want as $X = I_1 + I_2 + \cdots + I_m$, one indicator for each item that might count.
2. Find $P(I_i = 1)$ for each $i$, usually a ratio of two counts.
3. Add: $E[X] = \sum_i P(I_i = 1)$. No independence is needed.
4. Check with a small case by brute force.

*Theorem 1 (linearity of expectation).* For random variables $X$ and $Y$ on the same finite sample space, and constants $a$ and $b$, $E[aX + bY] = aE[X] + bE[Y]$. By induction the same holds for a sum of any finite number of variables, whether or not they are independent.

We know the definition of expected value as a sum over outcomes. We want to split the expected value of a sum. The plan is to expand the sum and regroup it.

*Proof.* The variable $aX + bY$ has the value $aX(\omega) + bY(\omega)$ at the outcome $\omega$, so

$$
E[aX + bY] = \sum_{\omega}\bigl(aX(\omega) + bY(\omega)\bigr)P(\{\omega\}) = a\sum_{\omega}X(\omega)P(\{\omega\}) + b\sum_{\omega}Y(\omega)P(\{\omega\}) = aE[X] + bE[Y]. \qquad \blacksquare
$$

Look back: the proof never mentions how $X$ and $Y$ relate to each other, which is the point. The sum is over outcomes, and each outcome carries its own values of $X$ and $Y$, so what one variable does has no bearing on the other's contribution. Two dice that are glued together, so that the second always shows the first's value, still have $E[X + Y] = 2E[X]$.

*Theorem 2 (fixed points of a random permutation).* Let $X$ be the number of fixed points of a uniformly random permutation of $n$ items. Then $E[X] = 1$ for every $n \ge 1$, and for $n \ge 2$, $\operatorname{Var}(X) = 1$. Also, for $0 \le k \le n$,

$$
P(X = k) = \frac{1}{k!}\sum_{j=0}^{n-k}\frac{(-1)^j}{j!},
$$

which tends to $\frac{e^{-1}}{k!}$ as $n \to \infty$.

We know indicators, linearity, and the derangement count $D_m = m!\sum_{j=0}^{m}\frac{(-1)^j}{j!}$. We want the mean, the variance and the distribution. The plan is to use one indicator for each item, find the variance through $E[X(X-1)]$, and count the permutations with exactly $k$ fixed points through derangements.

*Proof.* Let $I_i$ be the indicator that item $i$ is fixed, so $X = I_1 + \cdots + I_n$. The permutations that fix item $i$ number $(n-1)!$ out of $n!$, so $E[I_i] = \frac{1}{n}$ and, by linearity, $E[X] = n \cdot \frac{1}{n} = 1$.

For the variance, $X(X - 1) = \sum_{i \ne j}I_iI_j$, a sum over ordered pairs of different items, since $X^2 = \sum_{i,j}I_iI_j$ and the terms with $i = j$ add up to $\sum_i I_i^2 = X$. The product $I_iI_j$ is 1 when both items are fixed, which happens in $(n-2)!$ of the $n!$ permutations. So $E[I_iI_j] = \frac{1}{n(n-1)}$ and

$$
E[X(X-1)] = n(n-1)\cdot\frac{1}{n(n-1)} = 1.
$$

Then $E[X^2] = E[X(X-1)] + E[X] = 2$, and $\operatorname{Var}(X) = E[X^2] - E[X]^2 = 2 - 1 = 1$.

For the distribution, a permutation with exactly $k$ fixed points is built by choosing the $k$ fixed items, $\binom{n}{k}$ ways, and arranging the other $n - k$ items with no fixed point, $D_{n-k}$ ways. So

$$
P(X = k) = \frac{\binom{n}{k}D_{n-k}}{n!} = \frac{n!}{k!\,(n-k)!}\cdot\frac{(n-k)!}{n!}\sum_{j=0}^{n-k}\frac{(-1)^j}{j!} = \frac{1}{k!}\sum_{j=0}^{n-k}\frac{(-1)^j}{j!}.
$$

As $n \to \infty$ the sum tends to $e^{-1}$. $\blacksquare$

Look back: the indicators are not independent. If $n - 1$ items are fixed, the last one is too, and the proof didn't need independence. The mean and the variance of the count are both 1, and the probabilities approach $\frac{e^{-1}}{k!}$, which are the probabilities of a Poisson variable with mean 1. For $n = 10$ the probabilities of 0, 1, 2, 3 fixed points are $0.3679, 0.3679, 0.1839, 0.0613$, and the Poisson values are $0.3679, 0.3679, 0.1839, 0.0613$, equal to four places. The count is a sum of many unlikely and nearly independent events, which is when the Poisson shape appears.

### The birthday problem

There are $k$ people, and each birthday is uniform on $n$ days and independent of the others. The outcomes are the $n^k$ lists of birthdays, all equally likely, and "no two people share a birthday" is the set of lists with no repeat, of size $n(n-1)\cdots(n-k+1)$ by the product rule. So

$$
P(\text{all different}) = \prod_{i=0}^{k-1}\left(1 - \frac{i}{n}\right), \qquad P(\text{some match}) = 1 - \prod_{i=0}^{k-1}\left(1 - \frac{i}{n}\right).
$$

*Theorem 3.* Let $x = \frac{k(k-1)}{2n}$. Then

$$
1 - e^{-x} \le P(\text{some match}) \le x.
$$

We know $1 - t \le e^{-t}$ for every real $t$, and the union bound. We want to bound the product. The plan is to bound each factor by an exponential, and add the exponents.

*Proof.* Each factor satisfies $1 - \frac{i}{n} \le e^{-i/n}$, and all factors are non-negative for $k \le n$, so the product is at most $e^{-\sum_i i/n} = e^{-k(k-1)/(2n)} = e^{-x}$. That gives the lower bound on $P(\text{some match})$. For the upper bound, there are $\binom{k}{2}$ pairs of people, each pair matches with probability $\frac{1}{n}$, and the union bound says that the probability of some match is at most $\binom{k}{2}\cdot\frac{1}{n} = x$. $\blacksquare$

Look back: the lower bound is also an excellent approximation, because $1 - t \approx e^{-t}$ for small $t$, so the formula $1 - e^{-k(k-1)/(2n)}$ is the one to use. The exponent counts pairs: $\binom{k}{2}$ pairs, each a $\frac{1}{n}$ chance, so the expected number of matching pairs is $x$, and the probability of at least one match is about $1 - e^{-x}$. Setting $1 - e^{-x} = \frac{1}{2}$ gives $x = \ln 2$, so about $k \approx \sqrt{2\ln 2 \cdot n} \approx 1.18\sqrt{n}$ people give a 50% chance of a match.

![A curve rising from 0 at k equal to 0 to nearly 1 at k equal to 70, for the probability of a shared birthday among k people with 365 days. The exact curve and the curve 1 minus exp of minus k(k-1) over 2n nearly coincide. A dashed line, the union bound k(k-1) over 2n, lies above them and reaches 1 at about k equal to 28. A point marks k equal to 23 with probability 0.507.](../../assets/figures/06-cs-math/discrete-probability-birthday.svg)

| $k$ | exact | $1 - e^{-k(k-1)/730}$ | union bound $\frac{k(k-1)}{730}$ |
|---|---|---|---|
| 10 | 0.1169 | 0.1160 | 0.1233 |
| 23 | 0.5073 | 0.5000 | 0.6932 |
| 30 | 0.7063 | 0.6963 | 1.1918 |
| 40 | 0.8912 | 0.8820 | 2.1370 |
| 57 | 0.9901 | 0.9874 | 4.3726 |

The union bound is accurate only while the probability is small. At $k = 23$ the approximation $0.5000$ is within $0.01$ of the exact $0.5073$, and 23 is the smallest group with probability above one half.

For a hash function into $n = 2^b$ equally likely values, the same formula says that about $1.18 \cdot 2^{b/2}$ random inputs give a 50% chance of a collision. For $b = 16$ that is 302 inputs, for $b = 32$ it is 77,164 and for $b = 64$ about $5.06 \times 10^9$. This is why a hash of $b$ bits offers only about $\frac{b}{2}$ bits of resistance against finding two inputs that collide.

### The coupon collector problem

*Theorem 4 (coupon collector).* There are $n$ kinds of coupon, and each draw is one of them with probability $\frac{1}{n}$, independently. Let $T$ be the number of draws until every kind has appeared. Then

$$
E[T] = n\left(1 + \frac{1}{2} + \cdots + \frac{1}{n}\right) = nH_n,
$$

where $H_n$ is the $n$-th harmonic number.

We know that a geometric waiting time with success probability $p$ has mean $\frac{1}{p}$, and linearity. We want the mean of a waiting time with $n$ stages. The plan is to cut the process into phases, one per new kind, and add the phases' mean lengths.

*Proof.* Let $T_i$ be the number of draws needed, after $i - 1$ different kinds have been seen, to see the $i$-th new kind, for $i = 1, \dots, n$. Then $T = T_1 + \cdots + T_n$. During phase $i$ there are $n - i + 1$ unseen kinds, so each draw is a new kind with probability $p_i = \frac{n-i+1}{n}$, independently of the others. Phase $i$ ends at the first such success, so $T_i$ is a geometric waiting time with mean $\frac{1}{p_i} = \frac{n}{n-i+1}$. By linearity,

$$
E[T] = \sum_{i=1}^{n}\frac{n}{n-i+1} = n\left(\frac{1}{n} + \frac{1}{n-1} + \cdots + \frac{1}{1}\right) = nH_n. \qquad \blacksquare
$$

Look back: the first phase takes one draw, and the last takes $n$ draws on average, so most of the work is finding the last few kinds. For large $n$, $H_n \approx \ln n + 0.5772$ ([convergence tests](../../05-university-core/05-sequences-and-series/03-convergence-tests.md) bound $H_n$ by $\ln n$), so $E[T] \approx n\ln n + 0.577n$. The phases $T_i$ are independent here, but linearity needed only that each has the right mean.

| $n$ | $E[T] = nH_n$ |
|---|---|
| 6 | 14.70 |
| 10 | 29.29 |
| 52 | 235.98 |
| 100 | 518.74 |
| 365 | 2364.65 |

So a die needs 14.7 rolls on average to show every face, and a deck of 52 types needs about 236 random draws with replacement.

### The union bound

*Theorem 5 (union bound).* For events $A_1, \dots, A_m$, $P(A_1 \cup \cdots \cup A_m) \le P(A_1) + \cdots + P(A_m)$.

This is Theorem 5 of [sample spaces, events and axioms](../../05-university-core/07-probability/01-sample-spaces-events-and-axioms.md), and it is the first partial sum of inclusion-exclusion. In plain words, the chance that at least one bad thing happens is at most the sum of the chances of each bad thing, however the bad things are connected. It is useful when each $P(A_i)$ is tiny and you want a guarantee about all of them at once.

The coupon collector's tail shows a typical use. After $t$ draws, the kind $j$ is missing with probability $\left(1 - \frac{1}{n}\right)^t \le e^{-t/n}$. The event that some kind is missing is the union of $n$ such events, so

$$
P(T > t) \le n\left(1 - \frac{1}{n}\right)^t \le n\,e^{-t/n}.
$$

With $t = n\ln n + cn$ the bound is $n\,e^{-\ln n - c} = e^{-c}$. In plain words, after $n\ln n + cn$ draws, the chance that a kind is still missing is at most $e^{-c}$, so the waiting time is not much more than its mean $n\ln n + 0.58n$ with high probability. For $n = 52$ and $c = 2$ we have $t = 310$ and the bound is $0.126$.

## Worked examples

<div class="example" markdown>

### Example 1: a union bound for a hash table

A table has $m = 10^6$ slots, and a hash function sends each of $n = 1000$ keys to a uniformly random slot, independently. Bound the probability of any collision, and find how large $m$ must be to make that bound at most $\frac{1}{2}$ for $n = 1000$.

Step 1: an outcome is the list of slots chosen by the keys, uniform on $m^n$ lists. For keys $i < j$, let $A_{ij}$ be the event that they collide. Step 2: $P(A_{ij}) = \frac{1}{m}$, since key $j$ lands in the slot of key $i$ with probability $\frac{1}{m}$. Step 3: there are $\binom{n}{2} = 499{,}500$ pairs. By the union bound,

$$
P(\text{collision}) \le \binom{n}{2}\frac{1}{m} = \frac{499{,}500}{1{,}000{,}000} \approx 0.4995.
$$

The exact value from the birthday product is $0.3933$, so the bound is crude here, since the overlaps matter.

For the second question, we need $\frac{n(n-1)}{2m} \le \frac{1}{2}$, which holds when $m \ge n(n-1) = 999{,}000$. So a table with about $n^2$ slots has no collision with probability at least $\frac{1}{2}$, and this is the starting point for perfect hashing, where $n$ keys get a table of size $n^2$ and a few random tries find a function with no collision.

Check: with $m = 999{,}000$ the exact probability of no collision is $0.6064$, above the guaranteed $\frac{1}{2}$.

</div>

<div class="example" markdown>

### Example 2: expected empty slots

$n$ items are thrown into $n$ slots, each landing in a uniformly random slot, independently. What is the expected number of empty slots?

Step 1: let $I_s$ be the indicator that slot $s$ is empty, so the count is $X = \sum_s I_s$. Step 2: slot $s$ is empty when all $n$ items miss it, each with probability $1 - \frac{1}{n}$, so $P(I_s = 1) = \left(1 - \frac{1}{n}\right)^n$. The indicators are dependent, since slots can't all be empty, and Theorem 1 doesn't care. Step 3:

$$
E[X] = n\left(1 - \frac{1}{n}\right)^n \approx \frac{n}{e}.
$$

So about 37% of the slots are empty. For $n = 100$ the exact value is $36.60$ and $\frac{100}{e} = 36.79$.

Check: with $n = 2$ the formula gives $2 \cdot \frac{1}{4} = \frac{1}{2}$. The four equally likely outcomes put both items in slot 1 or both in slot 2 (one empty slot each, two outcomes), or one in each slot (no empty slot, two outcomes), and the average is $\frac{2 \cdot 1 + 2 \cdot 0}{4} = \frac{1}{2}$.

</div>

<div class="example" markdown>

### Example 3: inversions of a random permutation

An inversion in a list is a pair of positions $i < j$ with the entry at $i$ larger than the entry at $j$. Insertion sort makes one swap per inversion. What is the expected number of inversions in a uniformly random ordering of $n$ different numbers?

For each pair $i < j$, let $I_{ij}$ be the indicator of an inversion. The two entries are equally likely to be in either order, so $P(I_{ij} = 1) = \frac{1}{2}$. There are $\binom{n}{2}$ pairs, so

$$
E[\text{inversions}] = \binom{n}{2}\cdot\frac{1}{2} = \frac{n(n-1)}{4}.
$$

For $n = 5$ this is $5$. Check: averaging the number of inversions over all $5! = 120$ orderings, by brute force, gives exactly $5$. So insertion sort on random input takes about $\frac{n^2}{4}$ swaps, which is quadratic: [asymptotic notation](../04-sums-recurrences-and-algorithms/04-asymptotic-notation.md) names this growth.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

A 365-day year, $k = 40$ people. Use Theorem 3 to estimate the probability that two share a birthday, find the expected number of matching pairs, and compare with the exact value $0.8912$.

The exponent is $x = \frac{k(k-1)}{2n}$. Work out $x$, then $1 - e^{-x}$, and then $x$ itself as the expected number of matching pairs.

<details class="solution" markdown>
<summary>Finish</summary>

$x = \frac{40 \cdot 39}{730} = \frac{1560}{730} = 2.137$. Then $e^{-2.137} = 0.1180$, so $1 - e^{-x} = 0.8820$, a lower bound for the true probability and within $0.01$ of it.

The expected number of matching pairs is $x = 2.137$, by linearity over the $\binom{40}{2} = 780$ pairs with probability $\frac{1}{365}$ each. The union bound $x = 2.137$ is useless as a probability, since it is above 1, but it is the right expected count.

Check: the approximation $0.8820$ is below the exact $0.8912$, as Theorem 3 says it must be.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out at step 2 of probability by counting: both counts must use the same sample space. The probability that two dice sum to 7 is $\frac{6}{36}$, counting ordered pairs. Counting the unordered outcomes $\{1, 6\}, \{2, 5\}, \{3, 4\}$ out of the 21 unordered outcomes gives $\frac{3}{21}$, which is wrong because the 21 unordered outcomes are not equally likely: a double has one ordering and a non-double two.

</div>

<div class="warning" markdown>

Watch out: the expected value of a count is not the probability of at least one. In a group of 23 the expected number of matching pairs is $\frac{253}{365} = 0.69$ and the probability of at least one match is $0.507$. They answer different questions, and the expected count is at least the probability, since a count of 2 or more adds to the mean but still counts once as "at least one".

</div>

<div class="warning" markdown>

Watch out at step 3 of the indicator method: linearity holds for expected values and not for probabilities, variances or products. $E[X + Y] = E[X] + E[Y]$ always, while $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ needs the variables to be uncorrelated, and $E[XY] = E[X]E[Y]$ needs independence. In Theorem 2 the variance needed the pair probability $E[I_iI_j]$ separately.

</div>

<div class="warning" markdown>

Watch out: the union bound is an upper bound only. It can exceed 1, as in the table at $k = 30$, and then it says nothing. Use it when each term is small, or to show that a probability is small, and don't read it as an estimate when the events overlap a lot.

</div>

Some small cases. For $k = 1$ person the birthday product is empty and equals 1, so no match, probability 0. For $k > n$ the product contains the factor $1 - \frac{n}{n} = 0$, so a match is certain, which is the pigeonhole principle. The coupon collector with $n = 1$ takes 1 draw, $1 \cdot H_1 = 1$. The expected number of fixed points of a permutation of one item is 1, since the item always stays.

## Tricks and shortcuts

To estimate a product of many factors close to 1, use $\prod(1 - a_i) \approx e^{-\sum a_i}$. It turns a long product into one sum, as in the birthday formula.

For "how many of these happen", write the count as a sum of indicators and add the probabilities. Look for a symmetry that makes all the probabilities equal, so that the sum is the number of indicators times one probability: $n \cdot \frac{1}{n}$ for fixed points, $\binom{n}{2}\frac{1}{2}$ for inversions.

For waiting times, split the wait into phases with constant success probability and add the means $\frac{1}{p}$.

The rule of thumb for random hashing is the square root: $\sqrt{n}$ items give a collision in a table of $n$ slots with probability about $\frac{1}{2}$, and about $n$ items are needed before most slots are used.

## In code

The program computes the probabilities exactly with fractions, simulates the expected values with a fixed seed, and checks each formula in the lesson against brute force or simulation.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import random
from fractions import Fraction
from itertools import permutations

# Exact distribution of fixed points for n = 5, then mean and variance.
n = 5
counts = {}
for p in permutations(range(n)):
    k = sum(1 for i, v in enumerate(p) if i == v)
    counts[k] = counts.get(k, 0) + 1
total = math.factorial(n)
mean = Fraction(sum(k * c for k, c in counts.items()), total)
var = Fraction(sum(k * k * c for k, c in counts.items()), total) - mean**2
print(sorted(counts.items()), mean, var)    # [(0, 44), (1, 45), (2, 20), (3, 10), (5, 1)] 1 1

# Expected inversions for n = 5.
inv = Fraction(sum(sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
                   for p in permutations(range(n))), total)
print(inv, Fraction(n * (n - 1), 4))        # 5 5

# Birthday: exact, approximation, union bound.
def no_match(k, n):
    prob = 1.0
    for i in range(k):
        prob *= (n - i) / n
    return prob

for k in (10, 23, 30, 40, 57):
    x = k * (k - 1) / (2 * 365)
    print(k, round(1 - no_match(k, 365), 4), round(1 - math.exp(-x), 4), round(x, 4))
# 10 0.1169 0.116 0.1233
# 23 0.5073 0.5 0.6932
# 30 0.7063 0.6963 1.1918
# 40 0.8912 0.882 2.137
# 57 0.9901 0.9874 4.3726

def smallest_k(n):
    k, s = 1, 0.0                           # s = log of the probability of no match
    while True:
        s += math.log1p(-k / n)             # factor for the (k + 1)-th person
        k += 1
        if 1 - math.exp(s) >= 0.5:
            return k
print(smallest_k(365), smallest_k(2**16), smallest_k(2**32))   # 23 302 77164
print(math.sqrt(2 * math.log(2) * 2**64))                      # 5056937540.686587

# Coupon collector: formula and simulation.
def collect(n):
    seen, draws = set(), 0
    while len(seen) < n:
        seen.add(random.randrange(n))
        draws += 1
    return draws

random.seed(11)
expected = lambda n: n * sum(1 / i for i in range(1, n + 1))
print(round(expected(6), 2), round(expected(52), 2), round(expected(365), 2))   # 14.7 235.98 2364.65
print(sum(collect(6) for _ in range(20000)) / 20000)                            # 14.68235

# Union bound tail for n = 52 coupons, t = n ln n + 2n.
t = math.ceil(52 * math.log(52) + 2 * 52)
print(t, round(52 * (1 - 1 / 52) ** t, 4), round(math.exp(-2), 4))              # 310 0.1264 0.1353

# Empty slots when n items go into n slots.
for size in (10, 100, 1000):
    print(size, round(size * (1 - 1 / size) ** size, 2), round(size / math.e, 2))
# 10 3.49 3.68 / 100 36.6 36.79 / 1000 367.7 367.88
```

The simulated coupon average, 14.68, is near the exact 14.7, and the formulas for the other quantities were checked by listing outcomes where that was possible.

</details>

## FAQ

### Why does linearity of expectation work without independence?

Expected value is an average over outcomes, and an average of a sum of values is the sum of the averages, outcome by outcome. Independence is about whether knowing one variable tells you something about another, which can change probabilities of joint events but not the average of each variable alone. It matters for variances and products, which depend on how the variables move together.

### Is the birthday problem about birthdays?

No, it is about collisions among random choices from a fixed set, and birthdays are the familiar example. It applies to hash values, random identifiers, random seeds and any case where $k$ random draws from $n$ values might repeat. The point is that collisions arrive when $k$ is about $\sqrt{n}$, much sooner than a naive guess of $\frac{n}{2}$, because the number of pairs grows like $k^2$.

### Does the coupon collector take about $n$ draws?

It takes about $n\ln n$, a little more than $n$ times a logarithm. Getting most coupons is quick, and the last few take the time: the last phase alone has mean $n$. For 52 types the mean is 236 draws, more than four times the 52 needed if every draw were new.

### When should I use the union bound and when inclusion-exclusion?

Use the union bound when you want a guarantee and the individual probabilities are small, so that the bound is close and needs no information about overlaps. Use inclusion-exclusion when you need the exact probability and can compute the probabilities of the intersections.

## Practice

### Warm-up

1\. Two fair dice are rolled. Find the probability that the sum is 8, and the expected value of the sum.

<details class="solution" markdown>
<summary>Solution</summary>

Of the 36 equally likely ordered pairs, five have sum 8: $(2,6), (3,5), (4,4), (5,3), (6,2)$. So the probability is $\frac{5}{36}$. The expected sum is $3.5 + 3.5 = 7$ by linearity.

Check: the sums 2 to 12 occur in $1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1$ of the 36 pairs, and these add to 36.

</details>

2\. A random 10-bit string is chosen. Find the probability that it has exactly 5 ones, and the expected number of ones.

<details class="solution" markdown>
<summary>Solution</summary>

There are $\binom{10}{5} = 252$ strings with five ones out of $2^{10} = 1024$, so the probability is $\frac{252}{1024} \approx 0.246$. Each bit is 1 with probability $\frac{1}{2}$, so the expected number of ones is $10 \cdot \frac{1}{2} = 5$.

Check: the counts $\binom{10}{k}$ add to 1024, and the weighted average $\frac{\sum k\binom{10}{k}}{1024} = \frac{10 \cdot 2^9}{1024} = 5$.

</details>

3\. A hash function sends 5 keys to 10 slots uniformly and independently. What is the probability that all 5 land in different slots?

<details class="solution" markdown>
<summary>Solution</summary>

There are $10^5$ equally likely lists of slots, and $10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 = 30{,}240$ with no repeat, so the probability is $\frac{30240}{100000} = 0.3024$.

Check: the union bound gives a collision probability of at most $\binom{5}{2}\cdot\frac{1}{10} = 1$, and the exact collision probability is $1 - 0.3024 = 0.6976$, below the bound.

</details>

### Standard

4\. A class of 30 students (365 equally likely birthdays) is chosen. Find the expected number of pairs with the same birthday, the exact probability that at least one pair matches, and the approximation $1 - e^{-x}$.

<details class="solution" markdown>
<summary>Solution</summary>

There are $\binom{30}{2} = 435$ pairs, each matching with probability $\frac{1}{365}$, so the expected count is $\frac{435}{365} = 1.192$. The exact probability is $1 - \prod_{i=0}^{29}\frac{365 - i}{365} = 0.7063$. The approximation is $1 - e^{-1.192} = 0.6963$.

Check: $0.6963 \le 0.7063$, as Theorem 3 says, and the union bound $1.192$ exceeds 1.

</details>

5\. A fair six-sided die is rolled until all six faces have appeared. Find the expected number of rolls, and a union-bound estimate of the probability that it takes more than 30 rolls.

<details class="solution" markdown>
<summary>Solution</summary>

By Theorem 4, $E[T] = 6H_6 = 6 \cdot \frac{49}{20} = 14.7$. For the tail, a given face is missing after 30 rolls with probability $\left(\frac{5}{6}\right)^{30} = 0.00421$, and by the union bound $P(T > 30) \le 6 \cdot 0.00421 = 0.0253$.

Check: the exact probability that all faces have appeared after 30 rolls, by inclusion-exclusion, is $\sum_k(-1)^k\binom{6}{k}\left(1 - \frac{k}{6}\right)^{30}$, which gives a tail $P(T > 30)$ of $0.0252$, just under the bound $0.0253$.

</details>

6\. Prove that the expected number of items that end up in a position one place to the right of where they began, in a random permutation of $n$ items, is $\frac{n-1}{n}$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: indicators and linearity. What we want: the mean of a count. The plan is one indicator per item that has a right neighbour position.

*Proof.* Items $1, \dots, n-1$ have a position to their right. Let $I_i$ be the indicator that item $i$ ends in position $i + 1$. Of the $n!$ permutations, $(n-1)!$ put item $i$ in a given position, so $E[I_i] = \frac{1}{n}$. By linearity the expected count is $(n-1)\cdot\frac{1}{n} = \frac{n-1}{n}$. $\blacksquare$

Check with $n = 3$, writing each permutation as the list of items in positions 1, 2, 3. The counts of items that sit one place to the right of their start are 0 for 123, 1 for 132 (item 2), 1 for 213 (item 1), 0 for 231, 2 for 312 (items 1 and 2) and 0 for 321. The total is 4, so the mean is $\frac{4}{6} = \frac{2}{3}$, matching $\frac{n-1}{n}$.

</details>

### Challenge

7\. Show that $n$ people can have a 50% chance of a shared birthday with about $1.18\sqrt{n}$ people, by solving $1 - e^{-k(k-1)/(2n)} = \frac{1}{2}$, and use it to find the number of random 48-bit values that give a 50% chance of a collision.

<details class="solution" markdown>
<summary>Solution</summary>

Setting $e^{-x} = \frac{1}{2}$ gives $x = \ln 2$, so $k(k-1) = 2n\ln 2$. For large $k$, $k(k-1) \approx k^2$, so $k \approx \sqrt{2\ln 2}\sqrt{n} = 1.1774\sqrt{n}$. For 48-bit values $n = 2^{48}$ and $\sqrt{n} = 2^{24} = 16{,}777{,}216$, so $k \approx 1.1774 \cdot 16{,}777{,}216 \approx 19.75$ million.

Check against the 365-day case: $1.1774\sqrt{365} = 22.5$, and the true smallest group is 23.

</details>

8\. (Reviews [inclusion-exclusion and the pigeonhole principle](04-inclusion-exclusion-and-pigeonhole.md).) A secret-Santa draw gives each of 8 people a random other person's name, with every permutation of the names equally likely. What is the probability that nobody draws their own name, and how does it compare with $\frac{1}{e}$? What is the probability that exactly one person draws their own name?

<details class="solution" markdown>
<summary>Solution</summary>

Nobody draws their own name exactly for the derangements, so the probability is $\frac{D_8}{8!} = \frac{14833}{40320} = 0.36788$. That is within $\frac{1}{9!} = 0.0000028$ of $\frac{1}{e} = 0.367879$.

Exactly one fixed point: by Theorem 2 with $n = 8$ and $k = 1$, $P = \frac{8D_7}{8!} = \frac{8 \cdot 1854}{40320} = 0.36786$.

Check: the probabilities of 0, 1, 2, 3 fixed points, $0.3679, 0.3679, 0.1839, 0.0613$, are close to the Poisson values with mean 1, and the mean number of fixed points is 1.

</details>

## Where this shows up

- In algorithms, the randomized analysis of quicksort, hash tables and Bloom filters is built from indicators, linearity and the union bound, and the coupon collector explains why random probing needs about $n\ln n$ tries. The expected-cost arguments continue in [divide and conquer](../04-sums-recurrences-and-algorithms/05-divide-and-conquer-and-master-theorem.md).
- In security, the birthday bound is why a hash of $b$ bits gives about $\frac{b}{2}$ bits of collision resistance, and random identifiers need to be long enough that $k^2 \ll 2^b$.
- In economics and statistics, expected values by indicators give the mean of any count of events, such as the number of defaults in a portfolio of loans, and the Poisson shape of the fixed-point count is the pattern for rare events. Averages of many such counts are treated by [the law of large numbers and the CLT](../../05-university-core/07-probability/06-law-of-large-numbers-and-clt.md).
