# Induction

How to prove a statement about every natural number, every string or every tree from a base case and a step, with the three forms of induction and the well-ordering principle.

1. [Mathematical induction](01-mathematical-induction.md)
2. [Strong induction and well-ordering](02-strong-induction-and-well-ordering.md)
3. [Recursive definitions and structural induction](03-recursive-definitions-and-structural-induction.md)

## Cheat sheet

### Mathematical induction

To prove $P(n)$ for every integer $n \ge n_0$: prove $P(n_0)$ (base case), and prove that for every $k \ge n_0$, $P(k)$ implies $P(k+1)$ (inductive step). In symbols, $[P(0) \wedge \forall k\,(P(k) \Rightarrow P(k+1))] \Rightarrow \forall n\,P(n)$.

Proof template:

```text
Claim. For every integer n >= n0, P(n).
Proof. By induction on n.
Base case. For n = n0: [check both sides].
Inductive step. Let k >= n0 and suppose P(k): [write it out].
We must show P(k+1): [write it out, k+1 in brackets].
[Rewrite so P(k) appears, use the hypothesis, finish the algebra.]
By induction, P(n) holds for every integer n >= n0.
```

| Kind of claim | How to expose $P(k)$ in $P(k+1)$ |
|---|---|
| sum | peel off the last term: $\sum_{i=1}^{k+1} a_i = \sum_{i=1}^{k} a_i + a_{k+1}$ |
| divisibility $d \mid f(n)$ | name the witness, $f(k) = dm$, and write $f(k+1) = c\,f(k) + d(\dots)$ |
| inequality | chain: $f(k+1) = (\text{multiple of } f(k)) > \dots \ge g(k+1)$ |
| recurrence formula | use the recurrence for $a_{k+1}$, then the hypothesis for $a_k$ |

Standard results proved by induction:

| Claim | Starts at |
|---|---|
| $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ | $n = 1$ |
| $\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$ | $n = 1$ |
| $\sum_{i=0}^{n} r^i = \frac{r^{n+1} - 1}{r - 1}$, $r \ne 1$ | $n = 0$ |
| $3 \mid n^3 - n$, $\ 6 \mid 7^n - 1$ | $n = 0$ |
| $2^n > n^2$ | $n = 5$ (false at 2, 3, 4) |
| $n! > 2^n$ | $n = 4$ |

- Always write $P(k)$ and $P(k+1)$ on their own lines. The hypothesis is $P(k)$ for one arbitrary $k$, never for all $k$.
- Check the step for the smallest $k$. A step that needs $k \ge 2$ with a base case at 1 leaves a gap (the horses).
- The sum formula grows by exactly the new term: test $\text{formula}(k+1) - \text{formula}(k)$ before writing the proof.
- Loop invariants: true before the loop (base case), kept by each pass (step), and useful when the loop stops.

Main mistakes: proving the step backward (from $P(k+1)$ to $P(k)$); no base case (the step for "$3 \mid 4^n + 1$" is valid and the claim is false); a base case that can't reach the claim; careless substitution of $k+1$; calling a list of checked cases a step.

### Strong induction and well-ordering

Strong induction: assume $P(j)$ for every $j$ with $n_0 \le j \le k$, then prove $P(k+1)$.

| The step uses | Base cases needed |
|---|---|
| $P(k)$ only | 1 (ordinary induction) |
| $P(k)$ and $P(k-1)$ (Fibonacci) | 2 |
| $P(k+1-a)$ (postage with a stamp of $a$ cents) | $a$ |
| $P(a)$, $P(b)$ for factors $a, b < n$ (primes) | 1 |
| $P(\lfloor n/2 \rfloor)$ (halving) | 1 |

- Count base cases by finding the smallest $k+1$ where every cited case is at least $n_0$.
- Postage with coprime stamps $a < b$: the largest unreachable amount is $ab - a - b$, so the claim starts at $ab - a - b + 1$ with $a$ base cases ($4, 5$: from 12; $3, 5$: from 8; $3, 7$: from 12).
- Well-ordering: every nonempty set of natural numbers has a least element. A smallest counterexample proof: suppose the set of failures is nonempty, take the least $m$, show it isn't a base case, use the truth of everything below $m$ to get a contradiction.
- The three principles (ordinary, strong, well-ordering) are equivalent. Use strong induction when the step needs a case that isn't $k$.
- A recursive function is proved correct by strong induction: base branch is the base case, recursive calls on smaller inputs are the hypothesis, the return is the step.

Main mistakes: too few base cases; citing an earlier case outside $n_0 \le j \le k$; a smallest counterexample that never uses minimality; using well-ordering on sets without a least element (negative integers, positive reals).

### Recursive definitions and structural induction

A recursive definition has a basis, recursive clauses, and an unwritten "nothing else" clause.

| Set | Definition |
|---|---|
| strings $\Sigma^*$ | $\varepsilon \in \Sigma^*$; $w \in \Sigma^*$, $a \in \Sigma$ gives $wa \in \Sigma^*$ |
| balanced parentheses $B$ | $\varepsilon \in B$; $x \in B$ gives $(x) \in B$; $x, y \in B$ gives $xy \in B$ |
| full binary trees | a leaf; two trees $T_1$, $T_2$ under a new root |
| expressions $X$ | numbers and variables; $e, f \in X$ gives $(e + f)$, $(e \times f)$ |

Structural induction: prove $P$ for each basis element, and for each clause prove that $P$ for the parts gives $P$ for the new object.

| Theorem | Proof idea |
|---|---|
| balanced strings have equal counts of "(" and ")" | counts add under $(x)$ and $xy$ |
| full binary tree with $n$ internal nodes has $n+1$ leaves | $\ell = \ell_1 + \ell_2 = (i_1 + 1) + (i_2 + 1) = i + 1$ |
| $\text{rev}(\text{rev}(w)) = w$ | lemma $\text{rev}(uv) = \text{rev}(v)\,\text{rev}(u)$, then induction on length |
| an expression has one more operand than operators | $n = n_1 + n_2 = (o_1 + 1) + (o_2 + 1) = o + 1$ |

- Handle every clause. Assume $P$ for the parts, never for the new object.
- Functions defined by recursion need each object to have one construction (unique readability). With $xy$ in $B$, a function like $f(xy) = 2f(x) + f(y)$ is not well defined.
- Recursive function proofs: induction on the size of the input; check that each call is on a smaller input.

Main mistakes: forgetting a clause (the claim "every nonempty balanced string is $(y)$" fails at $()()$); equal counts do not make a string balanced ($)($); dropping "full" (a one-child node breaks $\ell = i + 1$).
