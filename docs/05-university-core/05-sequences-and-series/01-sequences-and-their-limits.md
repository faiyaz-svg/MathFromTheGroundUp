# Sequences and their limits

After this lesson you can state the epsilon-N definition of a limit and prove a sequence converges, find limits with the limit laws and the squeeze theorem, decide convergence of a monotone or recursive sequence, and rank $\ln n$, $n^p$, $b^n$ and $n!$ by growth.

Before this: [epsilon-delta definition](../01-limits-and-continuity/02-epsilon-delta-definition.md), [limits, intuition and limit laws](../01-limits-and-continuity/01-limits-intuition-and-limit-laws.md), [sequences and recursion](../../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md) and [linear approximation and L'Hopital's rule](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md). Induction ([mathematical induction](../../04-proofs-and-logic/05-induction/01-mathematical-induction.md)) is used for the recursive sequences.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. For $a_n = \frac{1}{n}$, find the smallest whole number $N$ such that $\lvert a_n \rvert < 0.01$ for every $n \ge N$.
2. Find $\displaystyle\lim_{n \to \infty} \frac{3n^2 + 1}{n^2 + n}$.
3. Does the sequence $a_n = (-1)^n$ converge?

<details class="solution" markdown>
<summary>Answers</summary>

1. We need $\frac{1}{n} < 0.01$, which means $n > 100$. So $N = 101$ is the smallest: $\frac{1}{100} = 0.01$ is not below 0.01, and $\frac{1}{101} \approx 0.0099$ is.
2. Divide the top and bottom by $n^2$: $\frac{3 + 1/n^2}{1 + 1/n} \to \frac{3}{1} = 3$.
3. No. The terms alternate $-1, 1, -1, 1, \dots$ forever, so they do not settle near one number.

</details>

## The idea

A savings account earns interest and you add \$50 each month. The balance after $n$ months is a list of numbers $a_1, a_2, a_3, \dots$, and the question that matters is where the list ends up. Does the balance grow without bound, or does it level off? A computer asks the same question about an iteration: Newton's method produces guesses $x_0, x_1, x_2, \dots$ for $\sqrt{2}$, and we want to know that the guesses approach $\sqrt{2}$ and how fast.

A **sequence** is a list with a first term, a second term, and so on forever. You met sequences in high school as lists with a formula or a recurrence. The new question is what a list does as $n$ gets large, and the answer is the same idea as a limit at infinity of a function, but with the input restricted to whole numbers.

The figure shows the idea for $a_n = \frac{2n + 1}{n + 3}$, whose terms climb toward 2. Draw a band of half-width $\varepsilon = 0.5$ around 2. The first seven terms fall outside the band, but from the eighth term on every term is inside. If you shrink the band, more terms fall outside, but there is always a point after which all the rest are in. That "always a point after which" is the whole definition.

![The terms of the sequence a sub n equals (2n plus 1) over (n plus 3) plotted as dots for n from 1 to 20. A green horizontal band runs from 1.5 to 2.5 around the dashed line at 2. The first seven dots, in red, lie below the band. A vertical red line between n equals 7 and n equals 8 marks N equals 8, and every dot from n equals 8 on, in green, lies inside the band.](../../assets/figures/05-university-core/sequences-and-their-limits-epsilon-n.svg)

The rest of the lesson makes this precise, proves the basic facts, and then asks which sequences converge without being told the limit in advance. Two tools do that: a bounded increasing sequence always converges (because the real line has no gaps), and a recursion can often be solved for its limit once convergence is known. The last part ranks how fast sequences grow, which is the vocabulary of algorithm analysis.

## Definitions

A **sequence** of real numbers is a function from the natural numbers (or from the natural numbers from some starting index on) to $\mathbb{R}$. We write $a_n$ for the value at $n$ and $(a_n)$ for the whole sequence. In plain words, it is an infinite list, and $a_n$ is the entry in position $n$. The book's $\mathbb{N}$ includes 0, but a sequence may start at 0, 1 or any index that is convenient.

Let $(a_n)$ be a sequence and $L$ a real number. The statement $\lim_{n \to \infty} a_n = L$ means that

$$
\forall \varepsilon > 0\ \exists N \in \mathbb{N}\ \forall n \ge N\ \bigl(\lvert a_n - L \rvert < \varepsilon\bigr).
$$

In words: for every $\varepsilon > 0$ there is a number $N$ such that every term from position $N$ on is within $\varepsilon$ of $L$. This is the **epsilon-N definition**. We also write $a_n \to L$. The sequence **converges** if there is some $L$ with $a_n \to L$, and **diverges** otherwise. In plain words, you name a tolerance $\varepsilon$, and I answer with a position $N$ after which the sequence never leaves the band $(L - \varepsilon, L + \varepsilon)$.

This is the [epsilon-delta definition](../01-limits-and-continuity/02-epsilon-delta-definition.md#definitions) of $\lim_{x \to \infty} f(x) = L$ with the half-line $x > M$ replaced by the half-line $n \ge N$, and the same game applies. The order of the quantifiers matters in the same way: $N$ comes after $\varepsilon$, so it may depend on $\varepsilon$, and a smaller $\varepsilon$ usually needs a larger $N$. The number $N$ is not unique, since any larger number also works.

Two kinds of divergence deserve names. The sequence **diverges to infinity**, written $a_n \to \infty$, if for every real number $M$ there is an $N$ such that $a_n > M$ for all $n \ge N$. Replacing $>$ by $<$ gives $a_n \to -\infty$. A sequence that diverges without going to $\pm\infty$ is said to oscillate, as $(-1)^n$ does. In plain words, "diverges to infinity" means the sequence eventually passes every ceiling and stays above it.

A sequence is **bounded** if there is a number $B$ with $\lvert a_n \rvert \le B$ for every $n$. It is **increasing** if $a_n \le a_{n+1}$ for every $n$, **decreasing** if $a_n \ge a_{n+1}$ for every $n$, and **monotone** if it is one or the other. In plain words, a monotone sequence only ever moves in one direction. (Some books write "non-decreasing" for $\le$ and reserve "increasing" for $<$. Here "increasing" allows ties.)

The last definition is the one place where the reals differ from the rationals. The **completeness axiom** says every nonempty set of real numbers with an upper bound has a least upper bound. It was introduced in [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#the-completeness-axiom), and it is exactly what makes the monotone convergence theorem below true. We also use the fact that no real number is larger than every natural number: for each real $x$ there is a whole number $N > x$.

## How to do it

### Proving a limit from the definition

A proof that $a_n \to L$ has the same two parts as an epsilon-delta proof: a search for $N$ done on scratch paper, and a clean proof written forwards.

1. State what you must prove: for every $\varepsilon > 0$ there is an $N$ such that $n \ge N$ implies $\lvert a_n - L \rvert < \varepsilon$.
2. Scratch work: simplify $\lvert a_n - L \rvert$ until it is a simple expression in $n$, usually a constant divided by something that grows.
3. If the expression is messy, replace it by something larger and simpler (drop positive terms from a denominator, for instance). The simpler expression must still be an upper bound.
4. Solve "simple expression $< \varepsilon$" for $n$. The answer has the form $n > $ (something depending on $\varepsilon$). Take $N$ to be a whole number at least that large.
5. Write the proof forwards: "Let $\varepsilon > 0$. Take $N > \dots$. If $n \ge N$, then $\lvert a_n - L \rvert \le \dots < \varepsilon$."
6. Check with numbers: pick one $\varepsilon$, compute $N$ and test terms at and beyond it.

*Theorem 1.* $\displaystyle\lim_{n \to \infty} \frac{1}{n} = 0$.

We know the definition, and that some whole number exceeds any real number. We want an $N$ for each $\varepsilon$. The plan is to solve $\frac{1}{n} < \varepsilon$ for $n$.

*Proof.* Let $\varepsilon > 0$. Choose a whole number $N > \frac{1}{\varepsilon}$. If $n \ge N$, then $n > \frac{1}{\varepsilon}$, so $\frac{1}{n} < \varepsilon$, that is, $\left\lvert \frac{1}{n} - 0 \right\rvert < \varepsilon$. $\blacksquare$

Look back: the recipe for $N$ is "just above $\frac{1}{\varepsilon}$". For $\varepsilon = 0.01$ that is 100, and the quick check used 101 because the inequality is strict. For $\varepsilon = 0.0001$ it is 10,000: a ten-times smaller band costs a ten-times longer wait.

*Theorem 2.* $\displaystyle\lim_{n \to \infty} \frac{2n + 1}{n + 3} = 2$.

We know the definition. We want an $N$ for each $\varepsilon$. The plan follows Steps 2 to 4: simplify the distance to 2, bound it by a multiple of $\frac{1}{n}$, and solve.

*Scratch work.* $\left\lvert \frac{2n + 1}{n + 3} - 2 \right\rvert = \left\lvert \frac{2n + 1 - 2n - 6}{n + 3} \right\rvert = \frac{5}{n + 3} < \frac{5}{n}$, and $\frac{5}{n} < \varepsilon$ when $n > \frac{5}{\varepsilon}$.

*Proof.* Let $\varepsilon > 0$ and choose a whole number $N > \frac{5}{\varepsilon}$. If $n \ge N$ then $n > \frac{5}{\varepsilon}$, so

$$
\left\lvert \frac{2n + 1}{n + 3} - 2 \right\rvert = \frac{5}{n + 3} < \frac{5}{n} < \varepsilon. \qquad \blacksquare
$$

Look back: the figure used $\varepsilon = 0.5$. The formula gives $N > 10$, so $N = 11$ works, but the picture shows the true threshold is $N = 8$. As with $\delta$, the proof only has to find some $N$, and usually finds a larger one than necessary.

*Theorem 3.* If $\lvert r \rvert < 1$, then $r^n \to 0$.

We know $0 < \lvert r \rvert < 1$ (the case $r = 0$ is trivial) and Bernoulli's inequality $(1 + h)^n \ge 1 + nh$ for $h \ge 0$, proved in the [binomial theorem lesson](../../03-high-school/11-sequences-series-and-counting/04-binomial-theorem.md#why-powers-of-a-small-ratio-shrink). We want an $N$ for each $\varepsilon$. The plan is to write $\lvert r \rvert = \frac{1}{1 + h}$ and use Bernoulli to bound $\lvert r \rvert^n$ by a multiple of $\frac{1}{n}$.

*Proof.* Put $h = \frac{1}{\lvert r \rvert} - 1$, which is positive, so $\lvert r \rvert = \frac{1}{1 + h}$. By Bernoulli's inequality $(1 + h)^n \ge 1 + nh > nh$, so

$$
\lvert r^n - 0 \rvert = \frac{1}{(1 + h)^n} < \frac{1}{nh}.
$$

Given $\varepsilon > 0$, choose a whole number $N > \frac{1}{h\varepsilon}$. If $n \ge N$, then $\frac{1}{nh} < \varepsilon$. $\blacksquare$

Look back: for $r = 0.9$, $h = \frac{1}{9}$, and the proof gives $N > \frac{9}{\varepsilon}$. For $\varepsilon = 0.001$ that is $N = 9{,}001$, far more than needed (in fact $0.9^{66} < 0.001$). The bound is crude but it is a proof, and it shows the key structure: a geometric sequence shrinks faster than $\frac{1}{n}$. This is the fact the next lesson uses for the geometric series.

### Divergence

To show a sequence diverges, negate the definition: for every candidate $L$ there is an $\varepsilon > 0$ such that for every $N$ some $n \ge N$ has $\lvert a_n - L \rvert \ge \varepsilon$.

*Theorem 4.* The sequence $a_n = (-1)^n$ diverges.

We know the terms alternate between $1$ and $-1$. We want to show no $L$ works. The proof is by contradiction: suppose $a_n \to L$, use $\varepsilon = 1$, and compare two neighbouring terms.

*Proof.* Suppose $(-1)^n \to L$. Take $\varepsilon = 1$. There is an $N$ such that $\lvert (-1)^n - L \rvert < 1$ for every $n \ge N$. Apply this to two consecutive indices $n$ and $n + 1$ with $n \ge N$: one of the terms is $1$ and the other is $-1$. So $\lvert 1 - L \rvert < 1$ and $\lvert -1 - L \rvert < 1$. By the triangle inequality,

$$
2 = \lvert 1 - (-1) \rvert \le \lvert 1 - L \rvert + \lvert L - (-1) \rvert < 1 + 1 = 2,
$$

which says $2 < 2$, a contradiction. $\blacksquare$

Look back: the same argument shows that any sequence with two different values that each appear infinitely often must diverge, because a band narrower than half the gap between the values can't hold both. Notice that $(-1)^n$ is bounded. Bounded is necessary for convergence (Theorem 5 below) but not sufficient.

### The limit laws and the squeeze theorem

Proving every limit from the definition would be slow, so the laws from [limits, intuition and limit laws](../01-limits-and-continuity/01-limits-intuition-and-limit-laws.md) are used instead. They hold for sequences with the same proofs as for functions, replacing "$0 < \lvert x - a \rvert < \delta$" by "$n \ge N$" and the minimum of two values of $\delta$ by the maximum of two values of $N$.

*Theorem 5 (limit laws).* Let $a_n \to L$ and $b_n \to M$, and let $c$ be a constant. Then

- $a_n + b_n \to L + M$ and $a_n - b_n \to L - M$,
- $c\,a_n \to cL$,
- $a_n b_n \to LM$,
- $\frac{a_n}{b_n} \to \frac{L}{M}$ if $M \ne 0$ (and $b_n \ne 0$ for every $n$),
- $\lvert a_n \rvert \to \lvert L \rvert$, and more generally $g(a_n) \to g(L)$ for each function $g$ that is continuous at $L$.

A convergent sequence is also bounded. We know $a_n \to L$. We want a single bound $B$. The plan is to use $\varepsilon = 1$: past some $N$ the terms are within 1 of $L$, and only finitely many terms remain before that.

*Proof that a convergent sequence is bounded.* Take $\varepsilon = 1$ and the matching $N$. For $n \ge N$, $\lvert a_n \rvert \le \lvert L \rvert + 1$. Let $B$ be the largest of $\lvert a_1 \rvert, \dots, \lvert a_{N-1} \rvert$ and $\lvert L \rvert + 1$. Then $\lvert a_n \rvert \le B$ for every $n$. $\blacksquare$

The sum law is proved for functions in the epsilon-delta lesson; the sequence version splits $\varepsilon$ in half in the same way. Here is the squeeze theorem, which has a short proof.

*Theorem 6 (squeeze theorem).* If $a_n \le b_n \le c_n$ for every $n \ge n_0$, and $a_n \to L$ and $c_n \to L$, then $b_n \to L$.

We know the two outer sequences squeeze the middle one. We want $b_n$ inside every band around $L$ eventually. The plan is to take a position past which both outer sequences are in the band, and the middle one is trapped between them.

*Proof.* Let $\varepsilon > 0$. There are $N_1$ and $N_2$ with $L - \varepsilon < a_n$ for $n \ge N_1$ and $c_n < L + \varepsilon$ for $n \ge N_2$. Let $N = \max(n_0, N_1, N_2)$. For $n \ge N$,

$$
L - \varepsilon < a_n \le b_n \le c_n < L + \varepsilon,
$$

so $\lvert b_n - L \rvert < \varepsilon$. $\blacksquare$

One more tool links sequences back to functions: if $f(x) \to L$ as $x \to \infty$ and $a_n = f(n)$, then $a_n \to L$. Given $\varepsilon$, the function definition gives a number $M$ with $\lvert f(x) - L \rvert < \varepsilon$ for $x > M$, and any whole number $N > M$ works. This lets L'Hopital's rule, which needs a differentiable function, be applied to $f(x)$ and then carried over to the sequence $f(n)$. The rule can't be applied to the sequence itself.

### Monotone sequences

Most convergence questions have no formula for the limit. The monotone convergence theorem answers "does a limit exist?" without finding it.

*Theorem 7 (monotone convergence theorem).* A bounded monotone sequence converges. If $(a_n)$ is increasing and bounded above, then $a_n \to \sup\{a_n\}$, the least upper bound of its terms. If it is decreasing and bounded below, it converges to the greatest lower bound.

We know the sequence is increasing and bounded above. We want a limit $L$ and an $N$ for each $\varepsilon$. The plan is to take $L$ to be the least upper bound of the set of terms, which exists by completeness, and then use the fact that $L - \varepsilon$ is not an upper bound.

*Proof.* The set $\{a_n\}$ is nonempty and bounded above, so by the completeness axiom it has a least upper bound $L$. Let $\varepsilon > 0$. Since $L - \varepsilon < L$, the number $L - \varepsilon$ is not an upper bound, so some term has $a_N > L - \varepsilon$. For $n \ge N$ the sequence is increasing, so $a_n \ge a_N > L - \varepsilon$, and $a_n \le L$ because $L$ is an upper bound. Hence $\lvert a_n - L \rvert < \varepsilon$ for every $n \ge N$. The decreasing case is the same after replacing $a_n$ by $-a_n$. $\blacksquare$

Look back: completeness is used in exactly one place, to know that $L$ exists. Over the rationals the theorem is false: the decimal truncations $1, 1.4, 1.41, 1.414, \dots$ of $\sqrt{2}$ are an increasing bounded sequence of rational numbers with no rational limit. A sequence of guesses can approach something that isn't on the number line you started with, unless the line has no gaps.

### Recursive sequences

A recursive sequence has the form $a_{n+1} = g(a_n)$ with a starting value $a_0$. If it converges to $L$ and $g$ is continuous, then taking the limit of both sides of $a_{n+1} = g(a_n)$ gives $L = g(L)$. A number with $g(L) = L$ is called a **fixed point** of $g$. In plain words, if the iteration settles down, it settles at a point that the rule leaves unchanged. The steps for a recursive sequence are:

1. Compute a few terms and guess whether the sequence is monotone and where it might go.
2. Prove, by induction, that the sequence is bounded in the direction that matters (above for increasing, below for decreasing).
3. Prove, by induction, that it is monotone. A direct comparison of $a_{n+1}$ and $a_n$ often reduces to a sign check.
4. Conclude convergence from the monotone convergence theorem.
5. Take the limit of both sides of the recursion to get an equation for $L$, solve it, and discard solutions that the bounds rule out.

Step 5 comes after Step 4, never before. The fixed-point equation only says where a convergent sequence could end up. For $a_{n+1} = 2a_n$ with $a_0 = 1$ the equation $L = 2L$ gives $L = 0$, but the sequence $1, 2, 4, \dots$ goes to infinity.

Newton's method from the [linear approximation lesson](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md) is a recursive sequence $x_{n+1} = g(x_n)$ with $g(x) = x - \frac{f(x)}{f'(x)}$. A fixed point of $g$ is a point with $f(x) = 0$, which is why a convergent Newton sequence ends at a root.

### Growth orders

For sequences we write $a_n \ll b_n$ ("$a_n$ is eventually much smaller than $b_n$") when $\frac{a_n}{b_n} \to 0$.

*Theorem 8.* For every real $p > 0$ and every $b > 1$,

$$
\ln n \ll n^p \ll b^n \ll n! \ll n^n.
$$

We know the function version $\ln x \ll x^p \ll b^x$ from the L'Hopital lesson, and the fact that $f(x) \to L$ implies $f(n) \to L$. We want the sequence version, plus the two new comparisons $b^n \ll n!$ and $n! \ll n^n$. The plan is to carry the first two over from functions, and for factorials to show that the ratio of consecutive terms is eventually at most $\frac{1}{2}$, so the terms shrink at least as fast as a geometric sequence.

*Proof.* The first two comparisons are the function limits $\frac{\ln x}{x^p} \to 0$ and $\frac{x^p}{b^x} \to 0$, evaluated at $x = n$. For $b^n \ll n!$, fix $b > 1$ and choose a whole number $m \ge 2b$. For $n > m$,

$$
\frac{b^n}{n!} = \frac{b^m}{m!} \cdot \prod_{k=m+1}^{n} \frac{b}{k} \le \frac{b^m}{m!}\left(\frac{1}{2}\right)^{n-m},
$$

because each factor $\frac{b}{k}$ with $k > m \ge 2b$ is below $\frac{1}{2}$. The right side is a constant times $\left(\frac{1}{2}\right)^n$, which tends to 0 by Theorem 3, so the squeeze theorem gives $\frac{b^n}{n!} \to 0$. For $n! \ll n^n$, write $\frac{n!}{n^n} = \frac{1}{n} \cdot \frac{2}{n} \cdots \frac{n}{n} \le \frac{1}{n}$, since every factor after the first is at most 1, and squeeze again. $\blacksquare$

Look back: the three-line argument for factorials is the model for the ratio test in [convergence tests](03-convergence-tests.md): compare consecutive terms with a ratio below 1 and let a geometric sequence do the work.

The following table shows what "eventually much smaller" looks like in numbers. The order only wins in the long run.

| $n$ | $\ln n$ | $n^2$ | $2^n$ | $n!$ |
|---|---|---|---|---|
| 5 | 1.61 | 25 | 32 | 120 |
| 10 | 2.30 | 100 | 1,024 | 3,628,800 |
| 20 | 3.00 | 400 | 1,048,576 | about $2.4 \times 10^{18}$ |
| 30 | 3.40 | 900 | about $1.1 \times 10^{9}$ | about $2.7 \times 10^{32}$ |

![Four sequences plotted for n from 1 to 20 on a logarithmic vertical axis. The natural log of n in green stays below 3. The curve n squared in blue rises slowly. The curve 2 to the n in orange rises steeply to about a million. The factorial n! in red rises fastest, reaching about 2 times 10 to the 18 at n equal to 20.](../../assets/figures/05-university-core/sequences-and-their-limits-growth.svg)

On a logarithmic axis, $n^p$ bends toward flat, $b^n$ is a straight line (because $\ln b^n = n\ln b$) and $n!$ bends upward. This ranking is the working vocabulary of [asymptotic notation](../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md). An algorithm that takes $2^n$ steps is hopeless for large $n$ and one that takes $n^2$ steps is not, and the ranking says that no choice of constants can reverse the order for large enough $n$.

## Worked examples

<div class="example" markdown>

### Example 1: a limit from the definition

Prove that $\displaystyle\lim_{n \to \infty} \frac{5n - 2}{2n + 1} = \frac{5}{2}$.

Step 1: for every $\varepsilon > 0$ we need an $N$ such that $n \ge N$ gives $\left\lvert \frac{5n - 2}{2n + 1} - \frac{5}{2} \right\rvert < \varepsilon$.

Step 2, scratch work: put the difference over a common denominator.

$$
\frac{5n - 2}{2n + 1} - \frac{5}{2} = \frac{2(5n - 2) - 5(2n + 1)}{2(2n + 1)} = \frac{-9}{2(2n + 1)}.
$$

So the distance is $\frac{9}{2(2n + 1)} = \frac{9}{4n + 2}$.

Step 3: drop the $+2$ in the denominator. A smaller denominator makes a bigger fraction, so $\frac{9}{4n + 2} < \frac{9}{4n}$.

Step 4: $\frac{9}{4n} < \varepsilon$ exactly when $n > \frac{9}{4\varepsilon}$. Take $N$ to be a whole number larger than $\frac{9}{4\varepsilon}$.

Step 5, the proof: let $\varepsilon > 0$ and choose a whole number $N > \frac{9}{4\varepsilon}$. If $n \ge N$, then $\left\lvert \frac{5n - 2}{2n + 1} - \frac{5}{2} \right\rvert = \frac{9}{4n + 2} < \frac{9}{4n} < \varepsilon$.

Step 6, check: for $\varepsilon = 0.01$ we get $N > 225$, so take $N = 226$. At $n = 226$ the distance is $\frac{9}{4 \cdot 226 + 2} = \frac{9}{906} \approx 0.00993 < 0.01$. Watch out for dropping a term in the wrong direction: $\frac{9}{4n + 2} < \frac{9}{4n}$ is true, but $\frac{9}{4n + 2} < \frac{9}{4n + 4}$ is false.

</div>

<div class="example" markdown>

### Example 2: limit laws

Find $\displaystyle\lim_{n \to \infty} \frac{4n^2 - n + 7}{2n^2 + 3}$.

The top and bottom both tend to infinity, so the quotient law doesn't apply yet. Divide the top and bottom by the highest power of $n$ in the denominator, $n^2$:

$$
\frac{4n^2 - n + 7}{2n^2 + 3} = \frac{4 - \frac{1}{n} + \frac{7}{n^2}}{2 + \frac{3}{n^2}}.
$$

Now $\frac{1}{n} \to 0$ and $\frac{1}{n^2} = \frac{1}{n}\cdot\frac{1}{n} \to 0$ by the product law. By the sum and constant-multiple laws the top tends to 4 and the bottom to 2. The bottom's limit is not 0, so the quotient law gives $\frac{4}{2} = 2$.

Check: at $n = 100$ the value is $\frac{39{,}907}{20{,}003} \approx 1.995$.

</div>

<div class="example" markdown>

### Example 3: the squeeze theorem

Find $\displaystyle\lim_{n \to \infty} \frac{n!}{n^n}$.

Write $\frac{n!}{n^n} = \frac{1}{n}\cdot\frac{2}{n}\cdot\frac{3}{n}\cdots\frac{n}{n}$. The first factor is $\frac{1}{n}$ and every other factor is at most 1, so $0 \le \frac{n!}{n^n} \le \frac{1}{n}$. The outer sequences tend to 0, so the squeeze theorem gives limit 0.

Check: at $n = 10$ the value is $\frac{3{,}628{,}800}{10^{10}} \approx 0.00036$, which is below $\frac{1}{10}$, and in fact it is far below, so the bound is crude but enough.

</div>

<div class="example" markdown>

### Example 4: a recursive sequence by monotone convergence

Let $a_1 = \sqrt{2}$ and $a_{n+1} = \sqrt{2 + a_n}$. Show that $(a_n)$ converges and find the limit. (The terms are $\sqrt{2}$, $\sqrt{2 + \sqrt{2}}$, $\sqrt{2 + \sqrt{2 + \sqrt{2}}}$, and so on.)

Step 1: the first terms are $1.4142, 1.8478, 1.9616, 1.9904, 1.9976$. They look increasing and look as if they stop below 2. The figure shows the terms on the left and a cobweb on the right: start at $a_1$ on the horizontal axis, go up to the curve $y = \sqrt{2 + x}$ to read off $a_2$, go across to the line $y = x$ to turn that output into the next input, and repeat. The staircase climbs to the point $(2, 2)$ where the curve crosses the line.

![Left: the terms of the recursive sequence, plotted as dots for n from 0 to 9, climbing from 0 toward the dashed line at 2. Right: a cobweb diagram. A green curve y equals the square root of (2 plus x) and a blue line y equals x cross at the point (2, 2). A red staircase between the curve and the line climbs toward that point.](../../assets/figures/05-university-core/sequences-and-their-limits-recursive.svg)

Step 2, bounded above by 2: we show $a_n < 2$ for every $n$ by induction. For $n = 1$, $\sqrt{2} < 2$. If $a_n < 2$ then $a_{n+1} = \sqrt{2 + a_n} < \sqrt{4} = 2$.

Step 3, increasing: we show $a_n < a_{n+1}$ by induction. For $n = 1$, $1.414 < 1.848$. Suppose $a_{n-1} < a_n$. Then $2 + a_{n-1} < 2 + a_n$, and taking square roots, $a_n < a_{n+1}$.

Step 4: the sequence is increasing and bounded above, so it converges by the monotone convergence theorem. Call the limit $L$.

Step 5: the limit of $a_{n+1}$ is also $L$ (the same sequence shifted by one place), and the square root is continuous, so $L = \sqrt{2 + L}$. Square both sides: $L^2 = 2 + L$, so $L^2 - L - 2 = (L - 2)(L + 1) = 0$. The roots are 2 and $-1$. All terms are positive, so $L \ge 0$, and therefore $L = 2$.

Check: the eighth term is $1.99996$, within $0.00004$ of 2. Squaring created the extra root $L = -1$, and the sign of the terms removed it. Without Steps 2 to 4, solving $L = \sqrt{2 + L}$ would only tell us where a limit would have to be.

</div>

<div class="example" markdown>

### Example 5: Newton's iteration as a sequence

Newton's method for $x^2 - 2 = 0$ gives $x_{n+1} = x_n - \frac{x_n^2 - 2}{2x_n} = \frac{1}{2}\left(x_n + \frac{2}{x_n}\right)$. Starting from $x_0 = 2$, the terms are $2,\ 1.5,\ 1.416667,\ 1.4142157,\ 1.41421356237469,\ 1.414213562373095$. The fixed-point equation $L = \frac{1}{2}\left(L + \frac{2}{L}\right)$ gives $\frac{L}{2} = \frac{1}{L}$, so $L^2 = 2$ and the limit, if it exists, is $\sqrt{2}$.

The number of correct digits roughly doubles each step. The errors $e_n = x_n - \sqrt{2}$ are $0.0858,\ 0.00245,\ 2.1 \times 10^{-6},\ 1.6 \times 10^{-12}$, and each is roughly a third of the square of the one before it (the ratio $\frac{e_{n+1}}{e_n^2}$ is $0.25,\ 0.333,\ 0.353$ and settles near $0.354$). For example, $0.353 \cdot (0.00245)^2 \approx 2.1 \times 10^{-6}$. This squaring of the error is why Newton's method is so fast, and it is quantified in practice problem 6.

Check: the last term in the list agrees with $\sqrt{2} = 1.4142135623730951$ to double precision.

</div>

<div class="example" markdown>

### Example 6: finish it yourself

Let $a_0 = 0$ and $a_{n+1} = \frac{1}{2}a_n + 3$. Compute $a_1, \dots, a_4$. Then show the sequence is bounded above by 6 and increasing, and find its limit.

The first terms are $a_1 = 3,\ a_2 = 4.5,\ a_3 = 5.25,\ a_4 = 5.625$. For the bound, if $a_n < 6$ then $a_{n+1} < 3 + 3 = 6$, and $a_0 = 0 < 6$. For monotonicity, $a_{n+1} - a_n = 3 - \frac{1}{2}a_n > 0$ when $a_n < 6$, which holds for every $n$ by the bound.

<details class="solution" markdown>
<summary>Finish</summary>

By the monotone convergence theorem the sequence converges, to some $L$. Taking the limit of both sides of $a_{n+1} = \frac{1}{2}a_n + 3$ gives $L = \frac{1}{2}L + 3$, so $\frac{1}{2}L = 3$ and $L = 6$.

Check: the terms $5.625, 5.8125, 5.90625$ move toward 6, and the gap to 6 halves each step. The gap is $6 - a_n = 6\left(\frac{1}{2}\right)^n$, which tends to 0.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: solving the fixed-point equation does not prove convergence. For $a_{n+1} = a_n^2$ the equation $L = L^2$ gives $L = 0$ or $L = 1$. Starting from $a_0 = \frac{1}{2}$ the sequence $\frac{1}{4}, \frac{1}{16}, \dots$ goes to 0, from $a_0 = 1$ it is constant at 1, and from $a_0 = 2$ it goes to infinity. First prove the limit exists (Steps 2 to 4), then solve for it.

</div>

<div class="warning" markdown>

Watch out: $a_{n+1} - a_n \to 0$ does not make $(a_n)$ converge. The terms $\sqrt{n}$ have $\sqrt{n + 1} - \sqrt{n} = \frac{1}{\sqrt{n + 1} + \sqrt{n}} \to 0$, but $\sqrt{n} \to \infty$. Consecutive terms getting close does not mean the sequence is settling on a value, since the small steps can add up forever.

</div>

<div class="warning" markdown>

Watch out: bounded is not convergent, and monotone is not convergent. The sequence $(-1)^n$ is bounded but oscillates, and $n$ is monotone but unbounded. The theorem needs both properties together.

</div>

<div class="warning" markdown>

Watch out: a limit can equal a term of the sequence. The constant sequence $5, 5, 5, \dots$ converges to 5, and the sequence $0, \frac{1}{2}, 0, \frac{1}{3}, 0, \frac{1}{4}, \dots$ converges to 0 and hits 0 infinitely often. "Gets close" means within $\varepsilon$, not "never reaches".

</div>

<div class="warning" markdown>

Watch out: don't use L'Hopital's rule on $a_n$ as if it were a function of a real variable. Define $f(x)$ with $f(n) = a_n$, apply the rule to $f$ as $x \to \infty$, and then conclude about the sequence. A sequence defined only by a recursion has no formula $f(x)$ to differentiate, and the rule is unavailable.

</div>

<div class="warning" markdown>

Watch out: the limit laws for quotients, products and sums need each limit to exist as a finite number first. For $a_n = n$ and $b_n = n$, the "difference of limits" $\infty - \infty$ is meaningless, and in fact $a_n - b_n = 0 \to 0$, while for $a_n = n^2$ and $b_n = n$ the difference goes to infinity. Rewrite the expression instead, as in Example 2.

</div>

## Tricks and shortcuts

To find the limit of a ratio of polynomials in $n$, divide the top and bottom by the highest power of $n$ present. The limit is the ratio of the leading coefficients if the degrees match, 0 if the top has lower degree, and infinite if the top has higher degree. For example, $\frac{3n^2 + 1}{n^2 + n} \to 3$ and $\frac{n}{n^2 + 1} \to 0$.

For a limit with $n$-th roots, squeeze between the largest term and a constant times it: $3^n \le 2^n + 3^n \le 2 \cdot 3^n$ gives $3 \le (2^n + 3^n)^{1/n} \le 2^{1/n}\cdot 3$, and $2^{1/n} \to 1$, so the limit is 3. This works for the root of any finite sum of exponentials.

To guess a limit of a recursive sequence before proving anything, solve $L = g(L)$. Then check the guess against the first few terms. If the terms move toward one of the roots, that root is the candidate, and Steps 2 to 4 turn the guess into a proof.

## In code

The code runs the recursions from this lesson and finds where $n^{10}$ is overtaken by $2^n$, which shows how late "eventually" can be.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

# Example 4: a_{n+1} = sqrt(2 + a_n), starting at sqrt(2).
a = math.sqrt(2)
for n in range(1, 9):
    print(n, round(a, 6))
    a = math.sqrt(2 + a)
# 1 1.414214
# 2 1.847759
# 3 1.961571
# 4 1.990369
# 5 1.997591
# 6 1.999398
# 7 1.999849
# 8 1.999962

# Example 5: Newton's iteration for sqrt(2), and the ratio e_{n+1} / e_n^2.
x = 2.0
errors = []
for n in range(4):
    errors.append(x - math.sqrt(2))
    x = (x + 2 / x) / 2
for e0, e1 in zip(errors, errors[1:]):
    print(round(e1 / e0**2, 3))
# 0.25
# 0.333
# 0.353

# When does 2^n overtake n^10, and 2^n overtake n^2 for good?
print(next(n for n in range(2, 200) if 2**n > n**10))
print(next(n for n in range(5, 200) if 2**n > n**2))
# 59
# 5
```

</details>

## FAQ

### Why does the definition need $\varepsilon$ at all? Can't I say "the terms get closer and closer to $L$"?

That phrase is true of numbers that are not the limit. The terms $\frac{1}{n}$ get closer and closer to $-1$ in the sense that each term is nearer to $-1$ than the one before: the distance is $1 + \frac{1}{n}$, which keeps shrinking. But the limit is 0, and the distance to $-1$ never drops below 1. "Closer and closer" only says each distance is smaller than the last. The $\varepsilon$ version demands that the distances go below every positive tolerance, and that picks out the limit uniquely.

### What if $N$ depends on $\varepsilon$ in a way I can't find?

Then you are probably trying to solve the inequality exactly. You don't have to. Replace $\lvert a_n - L \rvert$ by a larger, simpler expression (Step 3) and make that smaller than $\varepsilon$. Any $N$ that works is fine, and it is normal for it to be much bigger than the true threshold.

### Is a sequence just a function?

Yes, a function whose domain is the natural numbers, so its graph is a set of separate dots. That is why a function limit at infinity gives a sequence limit (the dots lie on the curve), but not the other way around: $\sin(\pi n) = 0$ for every whole $n$, so the sequence tends to 0, while the function $\sin(\pi x)$ has no limit as $x \to \infty$.

### Does every bounded sequence have a limit?

No, but it does have a convergent subsequence (the Bolzano-Weierstrass theorem, proved in a real analysis course). For $(-1)^n$, taking every second term gives the constant sequence $1, 1, 1, \dots$. The monotone convergence theorem is the special case where the whole sequence behaves.

## Practice

### Warm-up

1\. For $a_n = \frac{1}{n^2}$, find the smallest whole number $N$ such that $a_n < 0.001$ for every $n \ge N$.

<details class="solution" markdown>
<summary>Solution</summary>

We need $\frac{1}{n^2} < 0.001$, so $n^2 > 1000$. Since $31^2 = 961$ and $32^2 = 1024$, the condition holds from $n = 32$ on, so $N = 32$.

Check: $\frac{1}{31^2} = 0.00104$, which is not below 0.001, and $\frac{1}{32^2} = 0.000977$, which is. Every later term is smaller.

</details>

2\. Find $\displaystyle\lim_{n \to \infty} \frac{5n^2 + 3n}{2n^2 - 1}$.

<details class="solution" markdown>
<summary>Solution</summary>

Divide the top and bottom by $n^2$: $\frac{5 + \frac{3}{n}}{2 - \frac{1}{n^2}} \to \frac{5}{2}$.

Check: at $n = 1000$ the value is $\frac{5{,}003{,}000}{1{,}999{,}999} \approx 2.5015$.

</details>

3\. Say whether each sequence converges, diverges to infinity, or oscillates: (a) $a_n = n^2$, (b) $a_n = (-1)^n$, (c) $a_n = \frac{2n}{n + 1}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) It passes every ceiling, so it diverges to infinity. (b) It alternates between $1$ and $-1$, so it oscillates (Theorem 4). (c) Dividing top and bottom by $n$ gives $\frac{2}{1 + 1/n} \to 2$, so it converges to 2.

Check: the terms of (c) are $1, 1.33, 1.5, 1.6, \dots$ and at $n = 99$ the term is $1.98$.

</details>

### Standard

4\. Prove from the definition that $\displaystyle\lim_{n \to \infty} \frac{3n + 1}{n + 2} = 3$. Find the $N$ that your proof gives for $\varepsilon = 0.1$.

<details class="solution" markdown>
<summary>Solution</summary>

Scratch work: $\frac{3n + 1}{n + 2} - 3 = \frac{3n + 1 - 3n - 6}{n + 2} = \frac{-5}{n + 2}$, so the distance is $\frac{5}{n + 2} < \frac{5}{n}$, and $\frac{5}{n} < \varepsilon$ when $n > \frac{5}{\varepsilon}$.

Proof: let $\varepsilon > 0$ and choose a whole number $N > \frac{5}{\varepsilon}$. For $n \ge N$, $\left\lvert \frac{3n + 1}{n + 2} - 3 \right\rvert = \frac{5}{n + 2} < \frac{5}{n} < \varepsilon$.

For $\varepsilon = 0.1$ we need $N > 50$, so $N = 51$.

Check: at $n = 51$ the distance is $\frac{5}{53} \approx 0.0943 < 0.1$.

</details>

5\. Find $\displaystyle\lim_{n \to \infty} (2^n + 3^n)^{1/n}$, justifying each step.

<details class="solution" markdown>
<summary>Solution</summary>

Since $3^n \le 2^n + 3^n \le 3^n + 3^n = 2\cdot 3^n$, taking $n$-th roots (an increasing operation on positive numbers) gives $3 \le (2^n + 3^n)^{1/n} \le 2^{1/n}\cdot 3$. The function $t \mapsto 2^t$ is continuous at 0 and $\frac{1}{n} \to 0$, so $2^{1/n} \to 2^0 = 1$ and the right side tends to 3. The left side is the constant 3. By the squeeze theorem the limit is 3.

Check: $(2^{20} + 3^{20})^{1/20} = 3\left(1 + \left(\frac{2}{3}\right)^{20}\right)^{1/20} \approx 3.00004$.

</details>

6\. Newton's method for $x^2 - 5 = 0$ gives $x_{n+1} = \frac{1}{2}\left(x_n + \frac{5}{x_n}\right)$. Starting from $x_0 = 2$, find $x_1$ and $x_2$ as fractions and decimals, and compare with $\sqrt{5} \approx 2.2360680$.

<details class="solution" markdown>
<summary>Solution</summary>

$x_1 = \frac{1}{2}\left(2 + \frac{5}{2}\right) = \frac{9}{4} = 2.25$. Then $x_2 = \frac{1}{2}\left(\frac{9}{4} + \frac{20}{9}\right) = \frac{1}{2}\cdot\frac{81 + 80}{36} = \frac{161}{72} \approx 2.2361111$.

The errors are $x_1 - \sqrt{5} \approx 0.0139$ and $x_2 - \sqrt{5} \approx 4.3 \times 10^{-5}$. The second is about $0.22$ times the square of the first, so the error is roughly squared at each step.

Check: $\left(\frac{161}{72}\right)^2 = \frac{25921}{5184} \approx 5.000193$, close to 5.

</details>

### Challenge

7\. For $a_{n+1} = a_n^2$, find the fixed points. Then prove that for $a_0 = \frac{1}{2}$ the sequence converges to 0, and prove that for $a_0 = 2$ it diverges to infinity.

<details class="solution" markdown>
<summary>Solution</summary>

Fixed points: $L = L^2$ gives $L = 0$ or $L = 1$.

For $a_0 = \frac{1}{2}$: by induction $0 < a_n < 1$ (if $0 < a_n < 1$ then $0 < a_n^2 < a_n < 1$). The same line shows $a_{n+1} = a_n^2 < a_n$, so the sequence is decreasing and bounded below by 0. By monotone convergence it converges to some $L$ with $L = L^2$ and $L \le a_0 = \frac{1}{2}$. The root $L = 1$ is excluded, so $L = 0$.

For $a_0 = 2$: by induction $a_n \ge 2$, and then $a_{n+1} = a_n^2 \ge 2a_n$, so $a_n \ge 2^{n+1}$ by induction. Given $M$, choose $N$ with $2^{N+1} > M$. For $n \ge N$ we have $a_n \ge 2^{n+1} > M$.

Check: from $a_0 = 2$ the terms are $2, 4, 16, 256$, matching $a_n = 2^{2^n}$, which is far above $2^{n+1}$.

</details>

8\. (Reviews [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md).) A saver keeps a balance $a_n$ that loses 10% to spending and then receives a deposit of \$50 each month: $a_{n+1} = 0.9a_n + 50$ with $a_0 = 0$. Use the geometric sum formula to find $a_n$ in closed form, then find the limit.

<details class="solution" markdown>
<summary>Solution</summary>

Unrolling the recursion, $a_1 = 50$, $a_2 = 50(1 + 0.9)$, and in general $a_n = 50\left(1 + 0.9 + \cdots + 0.9^{n-1}\right)$. The geometric sum formula gives $a_n = 50\cdot\frac{1 - 0.9^n}{1 - 0.9} = 500\left(1 - 0.9^n\right)$. Since $0.9^n \to 0$ (Theorem 3), $a_n \to 500$.

Check with the fixed-point equation: $L = 0.9L + 50$ gives $0.1L = 50$ and $L = 500$. Also $a_2 = 0.9 \cdot 50 + 50 = 95$ and $500(1 - 0.81) = 95$.

</details>

## Where this shows up

- The infinite series in the next lesson are limits of one particular sequence, the partial sums ([infinite series basics](02-infinite-series-basics.md)).
- In CS, the ranking $\ln n \ll n^p \ll b^n \ll n!$ is the base of [asymptotic notation](../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md) and of [recurrences](../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md). Iterations such as Newton's method, gradient descent and fixed-point solvers are recursive sequences, and their analysis is the question of this lesson: does it converge, and how fast?
- In economics, an adjustment process such as a price that moves toward equilibrium each period is a recursive sequence $p_{n+1} = g(p_n)$, and its equilibrium is a fixed point (multipliers and the AD-AS model<!-- link: ../../07-economics-math/04-more-tools/02-multipliers-and-the-ad-as-model.md -->).
