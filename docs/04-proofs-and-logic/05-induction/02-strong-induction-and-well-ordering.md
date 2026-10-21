# Strong induction and well-ordering

After this lesson you can choose between ordinary and strong induction, prove a claim whose step needs several earlier cases (with the right number of base cases), prove a claim by taking a smallest counterexample, and see recursive functions as strong induction in code.

Before this: [mathematical induction](01-mathematical-induction.md) and [proof by contradiction](../03-core-proof-methods/06-proof-by-contradiction.md). The recurrence examples use [sequences and recursion](../../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. To prove "every integer $n \ge 2$ is a product of primes" by induction, a student writes $60 = 6 \cdot 10$. Which earlier cases does the proof of $P(60)$ need?
2. Which amounts of postage from 1 to 15 cents can't be made with 4-cent and 5-cent stamps?
3. The Fibonacci numbers satisfy $F_{n+2} = F_{n+1} + F_n$. Why can't ordinary induction, which assumes only $P(k)$, prove a bound on $F_{k+1}$?

<details class="solution" markdown>
<summary>Answers</summary>

1. It needs $P(6)$ and $P(10)$, not $P(59)$. Both 6 and 10 are smaller than 60, and neither is 59.
2. Check each amount: 1, 2, 3, 6, 7 and 11 can't be made. The others can: $4, 5, 8 = 4 + 4, 9 = 4 + 5, 10, 12 = 4 \cdot 3, 13 = 4 \cdot 2 + 5, 14 = 4 + 10, 15$.
3. Because $F_{k+1} = F_k + F_{k-1}$ involves two earlier terms. The hypothesis $P(k)$ says something about $F_k$ only, and nothing about $F_{k-1}$.

</details>

## The idea

Ordinary induction has the domino picture: domino $k$ knocks over domino $k + 1$. Some claims don't fit it. To show that 60 is a product of primes, you write $60 = 6 \cdot 10$ and factor 6 and 10 separately. The number 59 never comes up, and the numbers you need are far below 60 and not next to it.

Strong induction fits these claims. The picture changes from "the previous domino pushes this one" to "this domino falls once all of the dominoes before it have fallen". The extra hypothesis costs nothing, because by the time you reach $k + 1$ the earlier cases have all been proved anyway. You are allowed to use any of them, and you use whichever the argument needs.

The price is a new decision about base cases. If the step for $P(k+1)$ looks back at $P(k)$ and $P(k-1)$, then at the start there is no $P(-1)$ to look back at, and you must prove the first two cases by hand. The postage example below shows how to count the base cases you need.

## Definitions

Let $n_0$ be an integer and $P(n)$ a statement for each integer $n \ge n_0$. The principle of **strong induction** says: if, for every integer $k \ge n_0$, the implication

$$
\bigl[P(n_0) \wedge P(n_0 + 1) \wedge \cdots \wedge P(k)\bigr] \Rightarrow P(k + 1)
$$

is true, together with the base case(s) that the step can't cover, then $P(n)$ is true for every integer $n \ge n_0$. The assumption in the bracket is the **strong inductive hypothesis**.

In plain words: to prove the statement for $k + 1$, you may assume it for every smaller case, not just for $k$. A neat way to write the whole principle for $\mathbb{N}$ is

$$
\forall n\,\bigl[(\forall j < n\; P(j)) \Rightarrow P(n)\bigr] \;\Rightarrow\; \forall n\,P(n).
$$

For $n = 0$ the hypothesis "for all $j < 0$" is vacuously true, so this single step also covers the base case. In practice you still treat the small cases separately, because the general argument usually breaks for them.

The **well-ordering principle** says that every nonempty set of natural numbers has a least element. In plain words, if you pick any collection of natural numbers (as long as it isn't empty), one of them is the smallest. This fails for the integers (no smallest negative number) and for the positive real numbers (no smallest positive real), so it is a real property of $\mathbb{N}$.

A **smallest counterexample** argument uses well-ordering. To prove $P(n)$ for all $n \ge n_0$, suppose some $n$ makes $P(n)$ false. The set of such $n$ is nonempty, so it has a least element $m$. You then show that $m$ can't exist.

## How to do it

### Strong induction in six steps

1. State $P(n)$ and the starting value $n_0$.
2. Look at the step before proving anything. Write down which earlier cases $P(k+1)$ will use (for example $P(k)$ and $P(k-1)$, or $P(k+1-4)$, or $P$ of two factors). This tells you how many base cases you need.
3. Prove the base cases. They are the smallest values of $n$ for which the step would reach back below $n_0$. If the step uses $P(k-1)$ and $P(k)$, you need two base cases. If it uses $P(k + 1 - 4)$ and you want $n_0 = 12$, you need four, namely $12, 13, 14, 15$.
4. State the strong inductive hypothesis: "Let $k \ge$ (the last base case) and suppose $P(j)$ for every $j$ with $n_0 \le j \le k$."
5. Prove $P(k+1)$, saying which of the earlier cases you use and checking that each one lies in the range $n_0 \le j \le k$.
6. Conclude: "By strong induction, $P(n)$ holds for every integer $n \ge n_0$."

Step 5 hides the most common failure. A reference to an earlier case such as $P(k - 3)$ is legal only when $k - 3 \ge n_0$. The base cases exist so that this holds for every $k$ the step covers.

### A smallest counterexample argument

1. Suppose the claim is false. Let $S$ be the set of integers $n \ge n_0$ for which $P(n)$ fails. Assume $S$ is nonempty.
2. By the well-ordering principle, $S$ has a least element $m$.
3. Show $m$ is not one of the base cases, by checking them directly.
4. Because $m$ is the least element, $P(j)$ is true for every $j$ with $n_0 \le j < m$. Use that to show that $P(m)$ is true, or that a smaller counterexample exists.
5. This contradicts the choice of $m$, so $S$ is empty and the claim holds for every $n \ge n_0$.

### Why the principles agree

Ordinary induction, strong induction and the well-ordering principle are equivalent: each one can be proved from either of the others (using the basic facts of arithmetic). Here are the three arguments, each short.

Ordinary induction follows from well-ordering by the smallest counterexample argument at the start of the [previous lesson](01-mathematical-induction.md#why-this-is-valid). Strong induction follows from ordinary induction. Given a strong induction proof of $P$, define $Q(n)$ as "$P(j)$ holds for every $j$ with $n_0 \le j \le n$". Then $Q(n_0)$ is the base case $P(n_0)$. And $Q(k) \Rightarrow Q(k+1)$ holds because $Q(k)$ is exactly the strong hypothesis, which gives $P(k+1)$, and $Q(k)$ together with $P(k+1)$ is $Q(k+1)$. Ordinary induction on $Q$ then gives $Q(n)$ for every $n$, so $P(n)$ for every $n$.

Well-ordering follows from strong induction. Let $S$ be a set of natural numbers with no least element, and let $P(n)$ be "$n \notin S$". Suppose $P(j)$ for every $j < n$. If $n$ were in $S$, then it would be the least element, because everything below it is outside $S$. So $n \notin S$, which is $P(n)$. By strong induction, no natural number is in $S$, so $S$ is empty. Hence a nonempty set must have a least element.

The three principles form a circle, so you may use whichever is easiest. Strong induction is the most flexible; ordinary induction is the one to use when only $P(k)$ is needed, because it needs the fewest base cases.

## Worked examples

<div class="example" markdown>

### Example 1: every integer $n \ge 2$ is a product of primes

A **prime** is an integer $p > 1$ whose only positive divisors are 1 and $p$. A product of primes may have a single factor, so a prime counts as a product of one prime.

*Theorem 1.* Every integer $n \ge 2$ can be written as a product of primes.

What we know: if $n$ is not prime, it has a divisor $a$ with $1 < a < n$, so $n = ab$ with $1 < a, b < n$. What we want: $n$ is a product of primes. The plan: use strong induction. Split a non-prime $n$ into two smaller factors, and apply the hypothesis to both factors, whatever they are.

Step 1: $P(n)$ is "$n$ is a product of primes", and $n_0 = 2$.

Step 2: the step uses the hypothesis for two unknown smaller numbers $a$ and $b$ between 2 and $n - 1$. Those aren't $n - 1$, so ordinary induction can't do it. No other base case is needed, since the step starts at $n = 3$ and its factors lie between 2 and $n - 1$.

*Proof.* Step 3, base case. $n = 2$ is prime, so it is a product of one prime.

Step 4, strong inductive hypothesis. Let $k \ge 2$ and suppose every integer $j$ with $2 \le j \le k$ is a product of primes.

Step 5. Consider $k + 1$. If $k + 1$ is prime, it is a product of one prime. Otherwise $k + 1 = ab$ with $1 < a < k + 1$ and $1 < b < k + 1$. Then $2 \le a \le k$ and $2 \le b \le k$, so by the hypothesis, $a = p_1 \cdots p_s$ and $b = q_1 \cdots q_t$ for primes $p_i$ and $q_j$. Hence $k + 1 = p_1 \cdots p_s q_1 \cdots q_t$ is a product of primes.

Step 6. By strong induction, every integer $n \ge 2$ is a product of primes. $\blacksquare$

Look back: the proof says that factorizations exist, and nothing about their uniqueness. Uniqueness is a separate theorem, proved in primes and unique factorization<!-- link: ../../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md -->. Check: $60 = 6 \cdot 10$, then $6 = 2 \cdot 3$ and $10 = 2 \cdot 5$, so $60 = 2 \cdot 3 \cdot 2 \cdot 5$. The proof's recursion on the factors is exactly how a factoring program works.

</div>

<div class="example" markdown>

### Example 2: postage with 4-cent and 5-cent stamps

*Theorem 2.* Every amount of $n \ge 12$ cents can be made with 4-cent and 5-cent stamps.

What we know: Quick check 2 shows that 11 is the largest amount that can't be made. What we want: every $n \ge 12$ can. The plan: to make $n$, make $n - 4$ and add a 4-cent stamp.

Step 1: $P(n)$ is "$n$ cents can be made with 4-cent and 5-cent stamps", and $n_0 = 12$.

Step 2: the step for $P(k + 1)$ uses $P(k + 1 - 4) = P(k - 3)$. That case is in range only when $k - 3 \ge 12$, that is, $k \ge 15$. So the step covers $k + 1 \ge 16$, and the base cases are the four amounts 12, 13, 14 and 15.

*Proof.* Step 3, base cases. $12 = 4 + 4 + 4$, $13 = 4 + 4 + 5$, $14 = 4 + 5 + 5$ and $15 = 5 + 5 + 5$.

Step 4: let $k \ge 15$ and suppose $P(j)$ for every $j$ with $12 \le j \le k$.

Step 5: consider $k + 1 \ge 16$. Then $k + 1 - 4 = k - 3$ satisfies $12 \le k - 3 \le k$, so by the hypothesis $k - 3$ cents can be made. Add one 4-cent stamp to get $k + 1$ cents.

Step 6: by strong induction, every $n \ge 12$ can be made. $\blacksquare$

Look back: ordinary induction can't do this, since $P(k)$ doesn't tell you how to make $k - 3$. The four base cases are forced by the "4": a step that reaches back four places needs four starting values. Check: $16 = 12 + 4$ and $12 = 4 + 4 + 4$, so $16$ is four 4-cent stamps. For $n = 23$, $23 - 4 = 19$, $19 - 4 = 15$ and $15 = 5 + 5 + 5$, so $23 = 4 + 4 + 5 + 5 + 5$.

</div>

<div class="example" markdown>

### Example 3: an upper bound for Fibonacci numbers

Recall that $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$.

*Theorem 3.* For every integer $n \ge 0$, $F_n < 2^n$.

Step 1: $P(n)$ is "$F_n < 2^n$", and $n_0 = 0$. Step 2: the step uses $P(k)$ and $P(k-1)$, which are in range when $k - 1 \ge 0$, so $k \ge 1$ and the step covers $k + 1 \ge 2$. We need two base cases, $n = 0$ and $n = 1$.

*Proof.* Base cases: $F_0 = 0 < 1 = 2^0$ and $F_1 = 1 < 2 = 2^1$.

Let $k \ge 1$ and suppose $P(j)$ for every $j \le k$. Consider $F_{k+1}$. By the recurrence and then the hypothesis for $j = k$ and $j = k - 1$,

$$
F_{k+1} = F_k + F_{k-1} < 2^k + 2^{k-1} < 2^k + 2^k = 2^{k+1}.
$$

The second inequality holds because $2^{k-1} < 2^k$. By strong induction, $F_n < 2^n$ for every $n \ge 0$. $\blacksquare$

Check: $F_{12} = 144 < 4096 = 2^{12}$. The bound is far from tight, which Practice problem 7 improves.

</div>

<div class="example" markdown>

### Example 4: a smallest counterexample

*Theorem 4.* Every positive integer $n$ can be written as $n = 2^a m$ with $a \ge 0$ an integer and $m$ an odd positive integer.

The plan: suppose the claim fails, take the least counterexample $c$, and show that it can be written in the required form after all.

*Proof.* Suppose some positive integer fails, and let $c$ be the least one. If $c$ is odd, then $c = 2^0 \cdot c$ is of the required form, a contradiction. So $c$ is even, $c = 2d$ for a positive integer $d$ with $d < c$. By the choice of $c$, the number $d$ is not a counterexample, so $d = 2^a m$ with $m$ odd. Then $c = 2d = 2^{a+1} m$ is of the required form, again a contradiction. So there is no counterexample. $\blacksquare$

Look back: the argument has the same skeleton as strong induction (the claim for $c$ follows from the claim for a smaller number), written as a contradiction. Check: $40 = 2^3 \cdot 5$, $96 = 2^5 \cdot 3$ and $7 = 2^0 \cdot 7$.

</div>

<div class="example" markdown>

### Example 5: postage with 3-cent and 5-cent stamps (finish it yourself)

*Theorem 5.* Every amount of $n \ge 8$ cents can be made with 3-cent and 5-cent stamps.

Step 1: $P(n)$ is "$n$ cents can be made with 3-cent and 5-cent stamps", and $n_0 = 8$.

Step 2: the step makes $k + 1$ cents from $k + 1 - 3 = k - 2$ cents by adding a 3-cent stamp. It needs $k - 2 \ge 8$, so $k \ge 10$ and $k + 1 \ge 11$.

Now do Steps 3 to 6: find the base cases, state the hypothesis, prove the step and conclude.

<details class="solution" markdown>
<summary>Finish</summary>

Step 3: the base cases are $8 = 3 + 5$, $9 = 3 + 3 + 3$ and $10 = 5 + 5$.

Step 4: let $k \ge 10$ and suppose $P(j)$ for every $j$ with $8 \le j \le k$.

Step 5: for $k + 1 \ge 11$, the number $k - 2$ satisfies $8 \le k - 2 \le k$, so $k - 2$ cents can be made. Add a 3-cent stamp.

Step 6: by strong induction, every $n \ge 8$ can be made. $\blacksquare$

Check: the amounts that can't be made are 1, 2, 4 and 7, and $8, 9, 10, 11 = 3 + 3 + 5, 12, 13$ all work.

</details>

</div>

## Recursion as the CS mirror

A recursive function that calls itself on smaller inputs is proved correct by induction, and the form of its recursion tells you which induction. The code and the proof have the same parts.

| In the proof | In the function |
|---|---|
| base case | the `if` branch that returns without a recursive call |
| strong inductive hypothesis | "the recursive calls return the right answer for every smaller input" |
| inductive step | the code that combines the answers of the recursive calls |
| the step uses $P(\lfloor n/2 \rfloor)$ | a call on `n // 2`, which is far below `n - 1` |

Here is a function that computes $x^n$ by repeated squaring, and the proof that it works.

```python
def fast_pow(x, n):
    if n == 0:
        return 1
    half = fast_pow(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x
```

*Claim.* For every integer $n \ge 0$, `fast_pow(x, n)` returns $x^n$.

*Proof.* Base case: for $n = 0$ the function returns 1, which is $x^0$. Let $k \ge 0$ and suppose the call returns $x^j$ for every $j$ with $0 \le j \le k$. Consider $n = k + 1 \ge 1$. The recursive call is on $\lfloor n/2 \rfloor \le k$, so by the hypothesis `half` is $x^{\lfloor n/2 \rfloor}$. If $n$ is even, then $n = 2\lfloor n/2 \rfloor$ and `half * half` is $x^{2\lfloor n/2 \rfloor} = x^n$. If $n$ is odd, then $n = 2\lfloor n/2 \rfloor + 1$ and `half * half * x` is $x^n$. $\blacksquare$

Strong induction is needed because the call is on $\lfloor n/2 \rfloor$, not on $n - 1$. This also explains why divide-and-conquer algorithms are analyzed with strong induction: merge sort calls itself on both halves of its input, and the proof of correctness assumes both calls work. The cost of such a function follows a recurrence (recurrences<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md --> and divide and conquer and the master theorem<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/05-divide-and-conquer-and-master-theorem.md -->). For `fast_pow`, the number of calls is the number of times you can halve $n$ before reaching 0, plus one, so computing $x^{100}$ makes 8 calls.

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for too few base cases. Suppose someone "proves" that every $n \ge 8$ can be made with 4-cent and 5-cent stamps, with base cases 8, 9 and 10 and the same step as Example 2. For $n = 11$ the step wants 7 cents, which is below the starting value 8 and isn't covered. And $11$ can't be made. The number of base cases comes from how far back the step reaches, and a step that reaches back four places needs four base cases (Practice problem 6).

</div>

<div class="warning" markdown>

Watch out for a reference outside the range. In a strong induction step, every earlier case you cite must satisfy $n_0 \le j \le k$. Writing "by the hypothesis for $k - 3$" is only legitimate when $k - 3 \ge n_0$. If you can't say why, your base cases are too few.

</div>

<div class="warning" markdown>

Watch out for using strong induction when you only need ordinary induction, and for claiming the opposite. They prove exactly the same statements. A proof that uses only $P(k)$ needs just one base case and is cleaner as ordinary induction. A proof that needs $P(k-1)$ or other earlier cases must say it is strong induction, because the hypothesis in the first lesson ("suppose $P(k)$") does not allow it.

</div>

<div class="warning" markdown>

Watch out for a "smallest counterexample" with no minimality used. If the proof never uses that the counterexample is the least one, the argument isn't doing what it says. The point of taking the least is that all smaller cases are true, as in Example 4, where $P(d)$ for $d < c$ was used.

</div>

Well-ordering needs a nonempty set of natural numbers. For the positive reals, or for the set of all integers, the least element can fail to exist, and arguments that "take the smallest" are not valid there. Strong induction also has no problem with a step that doesn't use all of the earlier cases. It only permits it.

## Tricks and shortcuts

To count the base cases, find the smallest $k + 1$ for which every case you cite is at least $n_0$. In Example 2 the step cites $k + 1 - 4$, which is at least 12 when $k + 1 \ge 16$, so the four values 12 to 15 are base cases. In Example 3 the step cites $k$ and $k - 1$, so two base cases.

For postage problems with stamps $a$ and $b$ (with no common factor), the largest amount that can't be made is $ab - a - b$. For 4 and 5 that is $20 - 9 = 11$, for 3 and 5 it is $15 - 8 = 7$, and for 3 and 7 it is $21 - 10 = 11$. So the claim starts at $ab - a - b + 1$, and the base cases are the next $a$ values (take $a$ to be the smaller stamp). This is a formula to guess the claim with, and the induction proves it.

When a recursion calls itself on `n // 2`, `n - 1` or both halves of a list, the argument that it terminates and the argument that it is correct are the same induction. The size of the input decreases, and the strong hypothesis covers every smaller size.

## In code

Strong induction is the proof that matches recursion on more than one smaller input. The code below checks the three results of this lesson on finite ranges (evidence, not proof) and prints the sequence of recursive calls for `fast_pow`.

<details class="code" markdown>
<summary>In code</summary>

```python
def makeable(n, a, b):
    return any(n - a * i >= 0 and (n - a * i) % b == 0 for i in range(n // a + 1))

print([n for n in range(20) if not makeable(n, 4, 5)])   # [1, 2, 3, 6, 7, 11]
print(all(makeable(n, 4, 5) for n in range(12, 500)))    # True

F = [0, 1]
for i in range(2, 100):
    F.append(F[-1] + F[-2])
print(all(F[n] < 2 ** n for n in range(100)))            # True

calls = []

def fast_pow(x, n):
    calls.append(n)
    if n == 0:
        return 1
    half = fast_pow(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x

print(fast_pow(2, 100) == 2 ** 100, calls)    # True [100, 50, 25, 12, 6, 3, 1, 0]
```

The list of calls shows the sizes $100, 50, 25, \dots$: each is far below the previous one minus 1, which is why the hypothesis must cover every smaller case.

</details>

## FAQ

### How do I know whether to use ordinary or strong induction?

Look at the step. If $P(k+1)$ follows from $P(k)$ alone (a sum plus one more term, a power times one more factor), use ordinary induction. If it needs a number that is not $k$ (a factor, a half, two terms back), use strong induction. When in doubt, use strong induction: it never hurts, and the hypothesis is only larger.

### Why doesn't strong induction need more work for the base case?

It sometimes does, as Example 2 showed. The "strong" part only enlarges the hypothesis. The base cases depend on how far back the step reaches, and not on the kind of induction. If the step reaches back one place, one base case is enough.

### Is well-ordering a theorem or an assumption?

Either, depending on the course. If you start from the axiom of ordinary induction, well-ordering is a theorem, and the circle of three principles shows that any one of them can be taken as the axiom. In a first proofs course it is usually stated and used without proof.

### Does a smallest counterexample proof have to be written as a contradiction?

It is a proof by contradiction, since you assume a counterexample exists and reach a conflict. But the content is the same as a strong induction: the claim at $m$ follows from the claim at smaller numbers. Many authors prefer the strong induction form because the structure is easier to check.

## Practice

### Warm-up

1\. Find all amounts that can't be made with 3-cent and 7-cent stamps, find the smallest $n_0$ such that every $n \ge n_0$ can be made, and give the base cases and the step for a strong induction proof.

<details class="solution" markdown>
<summary>Solution</summary>

Checking each amount, the ones that can't be made are 1, 2, 4, 5, 8 and 11. The next amounts are $12 = 3 \cdot 4$, $13 = 3 \cdot 2 + 7$, $14 = 7 \cdot 2$ and $15 = 3 \cdot 5$, so $n_0 = 12$.

The step makes $k + 1$ cents from $k + 1 - 3 = k - 2$ cents by adding a 3-cent stamp. It needs $k - 2 \ge 12$, so $k + 1 \ge 15$, and the base cases are $12, 13, 14$. The step: for $k + 1 \ge 15$, the amount $k - 2$ satisfies $12 \le k - 2 \le k$, so by the hypothesis it can be made, and adding a 3-cent stamp gives $k + 1$.

Check: the formula $3 \cdot 7 - 3 - 7 = 11$ is the largest amount that can't be made, and $15 = 12 + 3$ with $12 = 3 \cdot 4$.

</details>

2\. For each recurrence, say which earlier terms the step uses and how many base cases are needed. (a) $a_n = a_{n-1} + a_{n-2}$. (b) $a_n = a_{n-3} + 1$. (c) $a_n = a_{\lfloor n/2 \rfloor} + 1$ for $n \ge 2$. (d) $a_n = a_{n-1} + a_{n-2} + a_{n-3}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Uses $a_{n-1}$ and $a_{n-2}$, so two base cases, $a_0$ and $a_1$.
- (b) Uses $a_{n-3}$, so three base cases, $a_0, a_1, a_2$.
- (c) Uses $a_{\lfloor n/2 \rfloor}$. For $n \ge 2$ we have $1 \le \lfloor n/2 \rfloor < n$, so one base case, $a_1$, is enough.
- (d) Uses three earlier terms, so three base cases.

Check: in (c), $n = 2$ uses $a_1$ and $n = 3$ uses $a_1$, and $n = 4$ uses $a_2$, which is defined by then.

</details>

3\. Which method fits each claim best: ordinary induction, strong induction, or a smallest counterexample? (a) $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$. (b) Every integer $n \ge 2$ has a prime divisor. (c) Among the positive integers of the form $12a + 18b$ with integers $a, b$ there is a smallest one. (d) $F_n \le 2^{n-1}$ for $n \ge 1$. (e) $3^n > n^3$ for $n \ge 4$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Ordinary induction: the step adds one term and uses only $P(k)$.
- (b) Strong induction: a composite $n = ab$ has a divisor chain through smaller numbers, not through $n - 1$. (A smallest counterexample works too.)
- (c) Well-ordering directly: the set of positive numbers of that form is nonempty, so it has a least element. No induction is needed.
- (d) Strong induction with two base cases, because $F_{k+1}$ uses $F_k$ and $F_{k-1}$.
- (e) Ordinary induction: multiply the hypothesis $3^k > k^3$ by 3 and compare $3k^3$ with $(k+1)^3$.

Check: in (e), $3^4 = 81 > 64 = 4^3$, and $3k^3 \ge (k+1)^3$ at $k = 4$ is $192 \ge 125$.

</details>

### Standard

4\. Use the well-ordering principle to prove that for integers $a \ge 0$ and $b > 0$ there exist integers $q \ge 0$ and $r$ with $a = bq + r$ and $0 \le r < b$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: every nonempty set of natural numbers has a least element. What we want: a quotient and a remainder. The plan: collect all the nonnegative numbers of the form $a - bq$, take the least, and show it is less than $b$.

*Proof.* Let $S = \{a - bq : q \in \mathbb{N} \text{ and } a - bq \ge 0\}$. The set $S$ is nonempty, because $q = 0$ gives $a \ge 0$. By well-ordering, $S$ has a least element $r = a - bq$ for some $q \in \mathbb{N}$. Then $a = bq + r$ and $r \ge 0$.

Suppose $r \ge b$. Then $r - b = a - b(q + 1) \ge 0$, so $r - b$ is in $S$, and $r - b < r$ because $b > 0$. That contradicts $r$ being least. So $r < b$. $\blacksquare$

Check: $a = 47$ and $b = 6$ give $S = \{47, 41, 35, 29, 23, 17, 11, 5\}$, the least element is $5$ with $q = 7$, and $47 = 6 \cdot 7 + 5$.

</details>

5\. A sequence has $a_0 = 1$, $a_1 = 3$ and $a_n = 3a_{n-1} - 2a_{n-2}$ for $n \ge 2$. Prove by strong induction that $a_n = 2^{n+1} - 1$ for every $n \ge 0$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the recurrence reaches back two places, so we need two base cases. What we want: $a_n = 2^{n+1} - 1$. The plan: substitute the hypothesis for the two earlier terms and simplify.

*Proof.* Base cases: $a_0 = 1 = 2^1 - 1$ and $a_1 = 3 = 2^2 - 1$.

Let $k \ge 1$ and suppose $a_j = 2^{j+1} - 1$ for every $j$ with $0 \le j \le k$. For $a_{k+1}$ the recurrence applies, since $k + 1 \ge 2$, and uses $a_k$ and $a_{k-1}$, both in range:

$$
a_{k+1} = 3\bigl(2^{k+1} - 1\bigr) - 2\bigl(2^k - 1\bigr) = 3 \cdot 2^{k+1} - 3 - 2^{k+1} + 2 = 2 \cdot 2^{k+1} - 1 = 2^{k+2} - 1.
$$

Here $2 \cdot 2^k = 2^{k+1}$ was used to combine the powers. By strong induction, the formula holds for every $n \ge 0$. $\blacksquare$

Check: the sequence is $1, 3, 7, 15, 31, \dots$, and $a_4 = 3 \cdot 15 - 2 \cdot 7 = 31 = 2^5 - 1$.

</details>

6\. Find the flaw. Claim: every amount $n \ge 8$ cents can be made with 4-cent and 5-cent stamps. "Proof. Base cases: $8 = 4 + 4$, $9 = 4 + 5$, $10 = 5 + 5$. Let $k \ge 10$ and suppose every amount from 8 to $k$ can be made. For $k + 1 \ge 11$, the amount $k + 1 - 4 = k - 3$ can be made by the hypothesis. Add a 4-cent stamp."

<details class="solution" markdown>
<summary>Solution</summary>

The step cites $k - 3$ and says it lies in the range 8 to $k$. That holds only when $k - 3 \ge 8$, that is, $k \ge 11$. For $k = 10$ (proving $n = 11$) the citation is $7$, which is outside the range, and 7 can't be made. In fact 11 can't be made either. The step reaches back four places, so it needs four base cases: $8, 9, 10$ and $11$. But 11 is not true, so the claim itself starts at 12 (Example 2).

Check: $11 - 4 = 7$ and $11 - 5 = 6$, neither of which can be made, so 11 cannot be made.

</details>

### Challenge

7\. Prove that $F_n \ge \left(\frac{3}{2}\right)^{n-2}$ for every integer $n \ge 2$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $F_{k+1} = F_k + F_{k-1}$. What we want: the bound for $k + 1$. The plan: use the hypothesis for $k$ and $k - 1$, factor out the lower power, and compare.

*Proof.* Base cases ($n = 2$ and $n = 3$): $F_2 = 1 \ge \left(\frac{3}{2}\right)^0 = 1$ and $F_3 = 2 \ge \frac{3}{2}$.

Let $k \ge 3$ and suppose the bound holds for every $j$ with $2 \le j \le k$. Then $k$ and $k - 1$ are both in range, so

$$
F_{k+1} = F_k + F_{k-1} \ge \left(\tfrac{3}{2}\right)^{k-2} + \left(\tfrac{3}{2}\right)^{k-3} = \left(\tfrac{3}{2}\right)^{k-3}\left(\tfrac{3}{2} + 1\right) = \left(\tfrac{3}{2}\right)^{k-3} \cdot \tfrac{5}{2}.
$$

Since $\frac{5}{2} = \frac{10}{4} \ge \frac{9}{4} = \left(\frac{3}{2}\right)^2$, this is at least $\left(\frac{3}{2}\right)^{k-3} \left(\frac{3}{2}\right)^2 = \left(\frac{3}{2}\right)^{k-1}$, which is the bound for $k + 1$. By strong induction, the bound holds for every $n \ge 2$. $\blacksquare$

Check: $F_8 = 21 \ge \left(\frac{3}{2}\right)^6 = 11.39$. With Example 3, the Fibonacci numbers grow exponentially: between $1.5^{n-2}$ and $2^n$.

</details>

8\. (Reviews [number bases and conversions](../../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).) Prove by strong induction that every positive integer $n$ is a sum of distinct powers of 2. (This is the existence of binary representations.)

<details class="solution" markdown>
<summary>Solution</summary>

What we know: for $n \ge 2$ there is a largest power $2^m \le n$, so $2^m \le n < 2^{m+1}$. What we want: $n$ is a sum of distinct powers of 2. The plan: take away $2^m$, and apply the hypothesis to what is left, which is smaller than $2^m$.

*Proof.* Base case: $1 = 2^0$.

Let $k \ge 1$ and suppose every $j$ with $1 \le j \le k$ is a sum of distinct powers of 2. Consider $n = k + 1 \ge 2$ and let $2^m$ be the largest power of 2 with $2^m \le n$. If $n = 2^m$, we are done. Otherwise $j = n - 2^m$ satisfies $1 \le j \le k$, so $j$ is a sum of distinct powers of 2. Each of those powers is at most $j$, and $j = n - 2^m < 2^{m+1} - 2^m = 2^m$, so every power in the sum is smaller than $2^m$. Adding $2^m$ gives $n$ as a sum of distinct powers of 2. By strong induction, the claim holds for every $n \ge 1$. $\blacksquare$

Check: $45 = 32 + 13 = 32 + 8 + 5 = 32 + 8 + 4 + 1$, the binary number $101101$. The algorithm in the proof is the usual conversion from decimal to binary.

</details>

## Where this shows up

- The next lesson, [recursive definitions and structural induction](03-recursive-definitions-and-structural-induction.md), proves facts about trees and strings by an induction built from their definitions. After the induction chapter, [relations and their properties](../06-relations-and-functions/01-relations-and-their-properties.md) starts the next topic.
- Recursive algorithms, from `fast_pow` to merge sort and Euclid's algorithm (GCD and Euclid's algorithm<!-- link: ../../06-cs-math/02-number-theory/02-gcd-and-euclids-algorithm.md -->), are proved correct by strong induction on the size of the input, as in invariants and algorithm correctness<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->.
- The well-ordering principle is behind the division algorithm of Practice problem 4, which underlies divisibility and modular arithmetic<!-- link: ../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.
