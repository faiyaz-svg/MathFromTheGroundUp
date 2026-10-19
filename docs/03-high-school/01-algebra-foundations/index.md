# Algebra foundations

The rules arithmetic is built on, solving equations and formulas, and describing solution sets with intervals and absolute value.

1. [Real numbers, axioms and set notation](01-real-numbers-axioms-and-set-notation.md)
2. [Linear and literal equations](02-linear-and-literal-equations.md)
3. [Compound inequalities and interval notation](03-compound-inequalities-and-interval-notation.md)
4. [Absolute value equations and inequalities](04-absolute-value-equations-and-inequalities.md)

## Cheat sheet

### Real numbers, axioms and set notation

| Notation | Meaning | Example |
|---|---|---|
| $x \in A$, $x \notin A$ | element of, not an element of | $3 \in \{1, 2, 3\}$ |
| $\{2, 4, 6\}$ | roster: list the elements | order and repeats don't matter |
| $\{x \in A : \dots\}$ | set-builder: name the ground set, then the condition | $\{x \in \mathbb{Z} : x^2 = 4\} = \{-2, 2\}$ |
| $A \subseteq B$ | every element of $A$ is in $B$ | $\{1\} \subseteq \{1, 2\}$ |
| $\emptyset$ | no elements; a subset of every set | $\{x \in \mathbb{R} : x^2 = -1\}$ |

The chain is $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}$, all proper, and this book's $\mathbb{N}$ starts at 0.

The field axioms, for all real $a$, $b$, $c$:

| Name | Addition | Multiplication |
|---|---|---|
| closure | $a + b \in \mathbb{R}$ | $ab \in \mathbb{R}$ |
| commutative | $a + b = b + a$ | $ab = ba$ |
| associative | $(a + b) + c = a + (b + c)$ | $(ab)c = a(bc)$ |
| identity | $a + 0 = a$ | $a \cdot 1 = a$, with $1 \ne 0$ |
| inverse | $a + (-a) = 0$ | $a \cdot a^{-1} = 1$ for $a \ne 0$ |

Also the distributive property $a(b + c) = ab + ac$. Subtraction is $a + (-b)$ and division is $a \cdot b^{-1}$, so they have no axioms of their own. The order axioms: the positives are closed under $+$ and $\cdot$, and each $a$ is positive, zero or has $-a$ positive; $a < b$ means $b - a$ is positive. Completeness (every bounded nonempty set has a least upper bound) separates $\mathbb{R}$ from $\mathbb{Q}$.

Proved from the axioms: $a + c = b + c$ implies $a = b$; the opposite is unique; $a \cdot 0 = 0$; $ab = 0$ implies $a = 0$ or $b = 0$; $a \ne 0$ implies $a^2 > 0$, so $1 > 0$.

Main mistakes:

- Writing $2 \subseteq \{1, 2\}$ or $\{2\} \in \{1, 2\}$. Elements go with $\in$, sets with $\subseteq$.
- Cancelling a factor without knowing it is not 0: $0 \cdot 3 = 0 \cdot 5$.
- Treating subtraction or division as commutative or associative.
- Leaving out the ground set in set-builder notation.

### Linear and literal equations

Steps for a linear equation: clear fractions, expand, combine, gather the variable on one side, divide by its coefficient, check. For $ax + b = cx + d$:

| Case | Result |
|---|---|
| $a \ne c$ | one solution, $x = \frac{d - b}{a - c}$ |
| $a = c$, $b \ne d$ | no solution |
| $a = c$, $b = d$ | every number |

To solve a formula for a letter, treat the other letters as numbers. If the target appears once, undo the operations in reverse order. If it appears in several terms, gather them, factor it out and divide. State the restriction: the coefficient is not 0.

| Formula | Solved | Restriction |
|---|---|---|
| $A = P(1 + rt)$ | $t = \frac{A - P}{Pr}$ | $P \ne 0$, $r \ne 0$ |
| $A = P(1 + rt)$ | $P = \frac{A}{1 + rt}$ | $1 + rt \ne 0$ |
| $C = \frac{5}{9}(F - 32)$ | $F = \frac{9}{5}C + 32$ | none |
| $y = mx + b$ | $x = \frac{y - b}{m}$ | $m \ne 0$ |
| $a - bp = c + dp$ | $p = \frac{a - c}{b + d}$ | $b + d \ne 0$ |

Check with numbers, and check the units: $\frac{A - P}{Pr}$ is dollars over dollars per year, which is years.

Main mistakes:

- Dividing only one term: $t = \frac{A - P}{r}$ is off by a factor of $P$.
- Undoing in the wrong order: $F = \frac{9}{5}(C + 32)$.
- Cancelling across a sum: $\frac{A - P}{P}$ is $\frac{A}{P} - 1$, not $A - 1$.
- Leaving the target on both sides.
- Dividing by a letter that could be 0 without saying so.

### Compound inequalities and interval notation

"And" is the intersection $\cap$ of the solution sets, and "or" is the union $\cup$. The math "or" includes both.

| Interval | Inequality |
|---|---|
| $(a, b)$ | $a < x < b$ |
| $[a, b]$ | $a \le x \le b$ |
| $[a, b)$, $(a, b]$ | one end included |
| $(a, \infty)$, $[a, \infty)$ | $x > a$, $x \ge a$ |
| $(-\infty, b)$, $(-\infty, b]$ | $x < b$, $x \le b$ |
| $(-\infty, \infty)$ | all of $\mathbb{R}$ |

- A bracket includes an endpoint and a parenthesis excludes it. $\infty$ always gets a parenthesis. The smaller endpoint goes first.
- Solve each part, graph both, take the overlap for "and" and everything shaded for "or". A chain such as $-3 \le 2x + 1 < 7$ gets the same operation on all three parts, and both symbols reverse when you divide by a negative.
- Special answers: $x < 1$ and $x > 3$ is $\emptyset$; $x \le 2$ and $x \ge 2$ is $\{2\}$; $x < 2$ or $x > 2$ is $(-\infty, 2) \cup (2, \infty)$; $x < 3$ or $x > 1$ is $\mathbb{R}$.
- Not between $a$ and $b$ means $x \le a$ or $x \ge b$.
- Endpoints: for "and", included only if every piece includes it; for "or", included if any piece does.
- Test one number from each piece cut by the boundary numbers, and each boundary number.

Main mistakes:

- A bracket at $\infty$.
- $\cup$ for "and": $(1, \infty) \cup (-\infty, 3)$ is all of $\mathbb{R}$, not $(1, 3)$.
- Writing "or" as a chain.
- Endpoints in the wrong order, such as $[4, -3)$.
- Listing overlapping pieces separately.

### Absolute value equations and inequalities

The distance from $x$ to $a$ is $\lvert x - a \rvert$. For $r > 0$:

| Statement | Solution |
|---|---|
| $\lvert x - a \rvert = r$ | $x = a - r$ or $x = a + r$ |
| $\lvert x - a \rvert < r$ | $a - r < x < a + r$, the interval with centre $a$ and radius $r$ |
| $\lvert x - a \rvert > r$ | $x < a - r$ or $x > a + r$ |

Less than means between (and), greater than means outside (or). With $\le$ and $\ge$ the endpoints are included.

For $\lvert u \rvert$ compared with $c$: if $c < 0$, an equation or a $<$ or $\le$ has no solution, and a $>$ or $\ge$ holds for every $u$. If $c = 0$, $\lvert u \rvert = 0$ means $u = 0$, $\lvert u \rvert \ge 0$ always holds, and $\lvert u \rvert > 0$ holds except at $u = 0$.

Steps: isolate the absolute value first, look at the sign of the other side, split into two cases, solve, and check. An equation with the variable on both sides, such as $\lvert x - 3 \rvert = 2x$, needs the check, because a case can produce an extraneous solution.

- Tolerance $a \pm t$ means $\lvert x - a \rvert \le t$, the interval $[a - t, a + t]$. A 5% tolerance on 330 is $t = 16.5$.
- $\lvert ax + b \rvert = \lvert a \rvert \lvert x + \frac{b}{a} \rvert$, so factor the coefficient out.
- An interval from $p$ to $q$ has centre $\frac{p + q}{2}$ and radius $\frac{q - p}{2}$.
- $\lvert u \rvert = \lvert v \rvert$ means $u = v$ or $u = -v$.
- Float tolerance tests need slack or exact decimals: $\lvert 25.05 - 25 \rvert \le 0.05$ is false in floating point.

Main mistakes:

- Splitting before isolating: $\lvert x - 1 \rvert + 3 = 7$ is $\lvert x - 1 \rvert = 4$.
- Mixing up "and" and "or". Test the centre.
- Treating $\lvert a + b \rvert$ as $\lvert a \rvert + \lvert b \rvert$.
- Solving $\lvert x \rvert = -4$ as $x = \pm 4$.
- Dropping the $a$ when turning $-r < x - a < r$ into an interval.
