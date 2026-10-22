# Counting and discrete probability

Counting finite sets without listing them, proving identities by counting, and turning counts into probabilities and expected values.

1. [Counting rules](01-counting-rules.md)
2. [Permutations and combinations](02-permutations-and-combinations.md)
3. [The binomial theorem and combinatorial proofs](03-binomial-theorem-and-combinatorial-proofs.md)
4. [Inclusion-exclusion and the pigeonhole principle](04-inclusion-exclusion-and-pigeonhole.md)
5. [Discrete probability](05-discrete-probability.md)

## Cheat sheet

### Counting rules

| Rule | Statement | Use |
|---|---|---|
| Sum | disjoint $A_1, \dots, A_m$: $\lvert \bigcup A_i \rvert = \sum \lvert A_i \rvert$ | cases that don't overlap |
| Product | $\lvert A \times B \rvert = \lvert A \rvert \lvert B \rvert$; stages with $n_i$ choices each give $n_1 \cdots n_k$ | "and", building in stages |
| Bijection | a bijection $A \to B$ gives $\lvert A \rvert = \lvert B \rvert$ | match a hard set with an easy one |
| Division | a $k$-to-1 function $A \to B$ gives $\lvert B \rvert = \lvert A \rvert / k$ | each object counted $k$ times |
| Complement | $\lvert A \rvert = \lvert U \rvert - \lvert A^c \rvert$ | "at least one" |

- Functions from $A$ to $B$: $\lvert B \rvert^{\lvert A \rvert}$. Subsets of an $n$-set: $2^n$, by matching subsets with bit strings. Even-weight bit strings of length $n$: $2^{n-1}$.
- A tree diagram counts leaves. The product rule needs the same number of choices at each stage whatever came before.

Main mistakes: adding overlapping cases, multiplying when the number of choices depends on earlier choices, forgetting to divide when an order is counted, and taking the complement in the wrong universe.

### Permutations and combinations

| Order matters? | Repetition? | Count |
|---|---|---|
| yes | yes | $n^k$ |
| yes | no | $P(n, k) = \frac{n!}{(n-k)!}$ |
| no | no | $\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$ |
| no | yes | $\binom{n+k-1}{k}$ |

- Multinomial: $\frac{n!}{n_1! \cdots n_m!}$ counts words with repeated letters and splits into labelled groups. Unlabelled groups of equal size: divide by $r!$ for $r$ equal groups.
- Stars and bars: $x_1 + \cdots + x_k = n$ has $\binom{n+k-1}{k-1}$ solutions in non-negative integers, and $\binom{n-1}{k-1}$ if every $x_i \ge 1$. Use $k - 1$ bars.
- Circular arrangements of $n$ different items: $(n-1)!$, or $\frac{(n-1)!}{2}$ if flips count as the same ($n \ge 3$). Numbered seats give $n!$.
- Non-adjacent items: arrange the others, then choose gaps.

Main mistakes: $\binom{n}{k}$ for repetition without order, $k$ bars instead of $k - 1$, $n!$ for a round table, and dividing by $2!$ for groups of different sizes.

### The binomial theorem and combinatorial proofs

- $(a+b)^n = \sum_k \binom{n}{k}a^{n-k}b^k$: choose $a$ or $b$ from each factor, a bit string with $k$ ones.
- Pascal: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ (does the subset contain one chosen element?). Lattice paths to $(a, b)$: $\binom{a+b}{a}$.

| Identity | Story |
|---|---|
| $\sum_k \binom{n}{k} = 2^n$ | subsets sorted by size |
| $\sum_k (-1)^k\binom{n}{k} = 0$ for $n \ge 1$ | toggle one element |
| $\sum_k k\binom{n}{k} = n2^{n-1}$ | committee with a chair |
| $\sum_k \binom{m}{k}\binom{n}{r-k} = \binom{m+n}{r}$ | committee from two groups |
| $\sum_k \binom{n}{k}^2 = \binom{2n}{n}$ | Vandermonde with $m = r = n$ |
| $\sum_{i=r}^{n}\binom{i}{r} = \binom{n+1}{r+1}$ | sort by the largest element |
| $\sum_k \binom{n}{k}2^k = 3^n$ | words over three letters |

- Combinatorial proof: name one set $S$, count it two ways, conclude. Cases must cover $S$ without overlap.
- Multinomial theorem: coefficient of $x_1^{n_1}\cdots x_m^{n_m}$ in $(x_1 + \cdots + x_m)^n$ is $\frac{n!}{n_1!\cdots n_m!}$.

Main mistakes: counting two different sets, overlapping cases, off-by-one in the hockey stick ($\binom{n+1}{r+1}$), and treating a numerical check as a proof.

### Inclusion-exclusion and the pigeonhole principle

- $\lvert A_1 \cup \cdots \cup A_n \rvert = s_1 - s_2 + s_3 - \cdots$, where $s_j$ adds the sizes of all $j$-fold intersections. Proof: an element in $t \ge 1$ sets is counted $\sum_{j \ge 1}(-1)^{j+1}\binom{t}{j} = 1$ times.
- In none of the sets: $\lvert U \rvert - s_1 + s_2 - \cdots$. For multiples, use floors of $N$ over the least common multiple.
- Derangements: $D_n = n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}$, the nearest integer to $\frac{n!}{e}$; $D_n/n! \to \frac{1}{e} \approx 0.3679$. Values: 0, 1, 2, 9, 44, 265, 1854.
- Onto functions: $\sum_{k=0}^{n}(-1)^k\binom{n}{k}(n-k)^m$; for $4 \to 3$ it is 36.
- Pigeonhole: more than $k$ objects in $k$ boxes means some box has two. Generalized: some box has at least $\lceil N/k \rceil$.
- Among $n$ integers some block of consecutive terms has sum divisible by $n$ (prefix sums, $n + 1$ totals, $n$ remainders). Any $n^2 + 1$ distinct numbers have a monotone subsequence of length $n + 1$ (label by $(u_i, d_i)$).

Main mistakes: stopping the alternating sum early, using the product of sizes for an intersection, needing one more object than boxes, and using the floor instead of the ceiling.

### Discrete probability

- Uniform sample space: $P(A) = \lvert A \rvert / \lvert \Omega \rvert$, with both counts using the same view of an outcome.
- Indicator $I_A$: $E[I_A] = P(A)$. Linearity: $E[\sum X_i] = \sum E[X_i]$, with no independence needed.

| Quantity | Result |
|---|---|
| fixed points of a random permutation of $n$ | mean 1, variance 1, distribution tends to Poisson(1) |
| inversions of a random ordering | $\frac{n(n-1)}{4}$ |
| empty slots, $n$ items into $n$ slots | $n(1 - \frac{1}{n})^n \approx \frac{n}{e}$ |
| coupon collector, $n$ kinds | $nH_n \approx n\ln n + 0.577n$ (6: 14.7; 52: 235.98) |
| birthday, $k$ people, $n$ days | $1 - e^{-k(k-1)/(2n)} \le P \le \frac{k(k-1)}{2n}$ |

- Birthday: 50% at about $1.18\sqrt{n}$ (23 for 365 days, 302 for $2^{16}$, 77,164 for $2^{32}$).
- Union bound: $P(\bigcup A_i) \le \sum P(A_i)$. Coupon tail: $P(T > n\ln n + cn) \le e^{-c}$. A table of size $n^2$ has no collision among $n$ keys with probability at least $\frac{1}{2}$.

Main mistakes: assuming equally likely outcomes for unordered results, reading an expected count as a probability, using the union bound as an estimate when it exceeds 1, and assuming linearity for variances.
