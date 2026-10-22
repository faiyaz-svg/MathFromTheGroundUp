# Existence and uniqueness proofs

After this lesson you can prove that an object exists by naming it or by a counting or continuity argument, prove that it is unique by assuming two and showing they are equal, and write a complete "there exists exactly one" proof, including the existence and uniqueness of the quotient and remainder.

Before this: [quantifiers](../02-logic-and-sets/04-quantifiers.md), [proof by contradiction](../03-core-proof-methods/06-proof-by-contradiction.md) and [if and only if proofs](01-if-and-only-if-proofs.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Prove that there is an integer $x$ with $x^2 + x = 56$.
2. How many real solutions does each equation have? (a) $3x + 1 = 10$. (b) $x^2 = 9$. (c) $x^2 = -1$.
3. Find the quotient $q$ and remainder $r$ when $-17$ is divided by $5$, so that $-17 = 5q + r$ and $0 \le r < 5$.

<details class="solution" markdown>
<summary>Answers</summary>

1. Take $x = 7$: $49 + 7 = 56$. One checked example proves an existence claim. (The value $x = -8$ also works: $64 - 8 = 56$.)
2. (a) One solution, $x = 3$. (b) Two solutions, $x = 3$ and $x = -3$. (c) None, because a real square is never negative.
3. $q = -4$ and $r = 3$, because $5(-4) + 3 = -17$ and $0 \le 3 < 5$. The pair $q = -3$, $r = -2$ also satisfies the equation, but $r = -2$ is negative, so it is not the remainder.

</details>

## The idea

A specification for a function says what it must return. Two questions come before you write any code. Is there always a correct answer for each valid input? And is there only one? If the answer to the first is no, no implementation can meet the specification on every input. If the answer to the second is no, two correct implementations can disagree, and "the" answer is not well defined. The standard library function `divmod(n, d)` is possible because for every integer $n$ and every positive integer $d$ there is a correct quotient and remainder, and there is exactly one.

Mathematics asks the same two questions about equations, numbers and structures. Does a solution exist? Is it the only one? These are different questions with different proofs. The equation $x^2 = 9$ has solutions, but two of them. The equation $x^2 = -1$ has none among the reals. The equation $3x + 1 = 10$ has exactly one. A theorem that says "there is exactly one" is stronger than "there is at least one", and it earns the word "the": the identity element, the inverse, the quotient.

This lesson gives a method for each question. To show that something exists, you either produce it, or you show by an argument that it must be there. To show that it is unique, you assume there are two, call them by different names, and show they are the same. Each method is a short, fixed pattern, and the examples apply it.

## Definitions

A **constructive proof** of an existence claim names an object (a witness) and checks that it has the required property. A **non-constructive proof** shows that an object must exist without saying which one it is. In plain words, a constructive proof hands you the object, and a non-constructive proof hands you a guarantee. Both are valid proofs of "there exists".

The statement **there exists exactly one** $x$ in $D$ such that $P(x)$, written $\exists!\, x \in D,\ P(x)$, means two things at once:

- existence: there is some $x$ in $D$ with $P(x)$;
- uniqueness: for all $x$ and $y$ in $D$, if $P(x)$ and $P(y)$, then $x = y$.

In plain words, at least one, and at most one. The word "unique" on its own means only the second part: at most one. A statement like "the largest integer is unique" is true as a statement about uniqueness and says nothing about whether a largest integer exists (none does).

The domain $D$ is part of the claim. The equation $x^2 = 9$ has exactly one solution among the positive reals ($x = 3$) and two among all reals. Always name the set the object lives in.

| Situation | Number of objects | What a proof must show |
|---|---|---|
| existence only | at least one | a witness, or an argument that one is there |
| uniqueness only | at most one | any two such objects are equal |
| exactly one | one | both of the above |
| none | zero | the property can't hold; this is a "for every" claim, a proof, not an example |

## How to do it

### Proving existence

1. Write the claim in full: for which objects (the domain), and what property. If the claim is "for every $x$, there is a $y$ with ...", introduce $x$ first, since the witness $y$ may depend on it (Example 2 in [proof language](../01-language-and-notation/03-proof-language-let-suppose-wlog.md#worked-examples) shows this).
2. Do scratch work to find a candidate. Solve for the unknown, try small values, or build the object from the given ones (a midpoint, a sum, a product plus 1).
3. State the witness: "Take $x = \dots$" or "Put $m = \dots$". The lesson [scratch work and proof strategies](../03-core-proof-methods/03-scratch-work-and-proof-strategies.md) explains why scratch work stays off the final page.
4. Check that the witness lies in the domain, and that it has every part of the property.
5. Conclude in the words of the claim.

### Existence without naming the object

Three arguments give existence with no explicit witness. Each is short, and each is worth knowing by name.

Contradiction. Suppose no such object exists, and derive something false. This is the form of the proof in Example 2.

Counting, or the pigeonhole principle. If more than $k$ objects are placed into $k$ boxes, then some box holds at least two of them. The proof is the contrapositive: if every box held at most one object, there would be at most $k$ objects. The principle says that some box is crowded but not which one. The lesson on [inclusion-exclusion and the pigeonhole principle](../../06-cs-math/03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md) develops it. Here is a first use.

*Proposition 1.* Among any five integers, there are two whose difference is divisible by 4.

*Proof.* Put each integer into the box named by its remainder when divided by 4 (every integer has one, by Theorem 1 below). There are four boxes, with remainders $0, 1, 2, 3$, and five integers, so some box holds two integers $x$ and $y$ with the same remainder $r$. Then $x = 4s + r$ and $y = 4t + r$ for integers $s$ and $t$, so $x - y = 4(s - t)$, which is divisible by 4. $\blacksquare$

Nothing in the proof says which two integers will collide. It says that two must.

Continuity. A continuous function cannot jump over a value. This is the intermediate value theorem, stated here and proved in a calculus or analysis course: if $f$ is continuous on $[a, b]$ and $f(a)$ and $f(b)$ have opposite signs, then $f(c) = 0$ for some $c$ between $a$ and $b$. You can use it as a reason in a proof, like any proved theorem.

*Proposition 2.* The equation $x^3 + x - 1 = 0$ has a real solution between 0 and 1.

*Proof.* Let $f(x) = x^3 + x - 1$. It is continuous, with $f(0) = -1 < 0$ and $f(1) = 1 > 0$. By the intermediate value theorem, there is $c$ with $0 < c < 1$ and $f(c) = 0$. $\blacksquare$

The proof gives no formula for $c$. It still points to a method: halve the interval, keep the half where the sign changes, and repeat. After a few dozen halvings this finds $c \approx 0.6823$, and the proof is what tells you the search will succeed. The intermediate value theorem is proved from the completeness axiom in [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#the-completeness-axiom); [the lesson on continuity and the IVT](../../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md) uses it.

### Proving uniqueness

1. State what two objects must satisfy: "Suppose $x$ and $y$ both have property $P$." Use two different letters.
2. Write down what each one satisfies, as separate equations or facts.
3. Combine them to reach $x = y$. Typical moves: substitute one equation into another, subtract, or cancel a nonzero factor.
4. Conclude: any two objects with the property are equal, so there is at most one.

Do not begin by solving for $x$ and then declaring that $y$ "is also" that value. Uniqueness is a claim about every pair, and the proof must treat the pair symmetrically.

### Exactly one

Write two labelled parts. Under "Existence" prove that there is an object, usually by a witness. Under "Uniqueness" assume two and show they are equal. Close by saying that the two parts together give exactly one. The parts are independent: uniqueness does not need existence, and existence does not need uniqueness. When the claim is an equation, a chain of reversible steps from "$P(x)$" to "$x = \dots$" proves both parts at once (the reversibility table in [if and only if proofs](01-if-and-only-if-proofs.md#chains-of-equivalences) says when a chain can be trusted).

### The division algorithm

The lesson on [long division](../../01-elementary/07-long-division.md) stated the division algorithm and proved it for $n \ge 0$ by walking up the multiples of $d$. Here is the version for every integer $n$, with a proof that has an existence half and a uniqueness half. The existence half uses the well-ordering principle: every nonempty set of nonnegative integers has a least element. We accept it as part of the integers, and a later lesson, [strong induction and well-ordering](../05-induction/02-strong-induction-and-well-ordering.md), examines it.

*Theorem 1 (division algorithm).* Let $n$ and $d$ be integers with $d > 0$. Then there exists exactly one pair of integers $q$ and $r$ such that

$$
n = qd + r \quad \text{and} \quad 0 \le r < d.
$$

What we know: $d \ge 1$, and the well-ordering principle. What we want: existence of a pair, then uniqueness. The plan for existence: among all the nonnegative numbers of the form $n - kd$ (that is, what is left of $n$ after taking away $k$ copies of $d$), take the smallest; call it $r$. It must be less than $d$, or we could take away one more $d$. The plan for uniqueness: subtract two pairs and use the size of $r$.

*Proof.* Existence. Let $S = \{\, n - kd : k \in \mathbb{Z} \text{ and } n - kd \ge 0 \,\}$. The set $S$ is nonempty: take $k = -\lvert n \rvert$, which gives $n + \lvert n \rvert d \ge n + \lvert n \rvert \ge 0$ (using $d \ge 1$). By well-ordering, $S$ has a least element $r$, and $r = n - qd$ for some integer $q$. So $n = qd + r$ and $r \ge 0$. Suppose $r \ge d$. Then $r - d = n - (q + 1)d \ge 0$, so $r - d$ is in $S$, and it is smaller than $r$ because $d > 0$. That contradicts the choice of $r$. So $r < d$, and the pair $q$, $r$ has both required properties.

Uniqueness. Suppose $n = qd + r = q'd + r'$ with $0 \le r < d$ and $0 \le r' < d$. Subtracting, $(q - q')d = r' - r$. Because $r$ and $r'$ both lie in $\{0, 1, \dots, d - 1\}$, the difference satisfies $-d < r' - r < d$. So $\lvert q - q' \rvert \, d < d$, which gives $\lvert q - q' \rvert < 1$. An integer with absolute value less than 1 is $0$, so $q = q'$. Then $r = n - qd = n - q'd = r'$. $\blacksquare$

Look back: the proof is non-constructive in a mild way (it takes "the least element" of a set) but it is easy to turn into a method: keep subtracting $d$ from $n$ until the result is below $d$. That is what long division does for positive $n$. The condition $0 \le r < d$ is what makes the pair unique, as the long-division lesson noted for $47 = 8 \cdot 5 + 7$. The proof also works for negative $n$: for $n = -17$ and $d = 5$, the set $S$ starts $3, 8, 13, \dots$, and its least element is $r = 3$ with $q = -4$.

## Worked examples

<div class="example" markdown>

### Example 1: a rational number between two rational numbers

*Theorem 2.* For all rational numbers $r$ and $s$ with $r < s$, there exists a rational number $t$ with $r < t < s$.

This has the form "for every $r$ and $s$, there exists $t$", so by the steps for existence we introduce $r$ and $s$ first (Step 1), and the witness may depend on them.

What we know: $r = \frac{a}{b}$ and $s = \frac{c}{d}$ for integers $a, b, c, d$ with $b, d \ne 0$, and $r < s$. What we want: a rational $t$ strictly between. The plan (Step 2): the midpoint of two numbers is between them, and fractions can be added and halved without leaving the rationals.

*Proof.* Let $r$ and $s$ be rational numbers with $r < s$. Put $t = \frac{r + s}{2}$ (Step 3). Since $r < s$, adding $r$ to both sides gives $2r < r + s$, so $r < \frac{r + s}{2} = t$. Adding $s$ to both sides of $r < s$ gives $r + s < 2s$, so $t < s$. For rationality, write

$$
t = \frac{1}{2}\left(\frac{a}{b} + \frac{c}{d}\right) = \frac{ad + bc}{2bd}.
$$

The numerator $ad + bc$ is an integer, and the denominator $2bd$ is a nonzero integer, because $b \ne 0$ and $d \ne 0$. So $t$ is rational (Step 4). Hence there is a rational number strictly between $r$ and $s$. $\blacksquare$

Look back: the witness is a formula in $r$ and $s$, which is why those two had to be introduced before $t$. The theorem repeats itself: apply it to $r$ and $t$ to get another rational, and so on, so between two rationals there are infinitely many. In particular there is no smallest positive rational, since $\frac{s}{2}$ is positive and smaller than $s$.

Check: $r = \frac{1}{3}$ and $s = \frac{3}{4}$ give $t = \frac{13}{24}$ from the formula $\frac{ad + bc}{2bd} = \frac{4 + 9}{24}$. Indeed $\frac{8}{24} < \frac{13}{24} < \frac{18}{24}$.

</div>

<div class="example" markdown>

### Example 2: an irrational power that is rational

*Theorem 3.* There exist irrational numbers $a$ and $b$ such that $a^b$ is rational.

This is a non-constructive proof: we don't know which pair works, but we know that one of two pairs does. We use that $\sqrt{2}$ is irrational, proved in [roots, irrational numbers and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#proving-that-the-square-root-of-2-is-irrational).

What we know: $\sqrt{2}$ is irrational. What we want: some pair of irrational numbers whose power is rational. The plan: look at the number $x = \sqrt{2}^{\sqrt{2}}$, and split into the two cases "rational" and "irrational".

*Proof.* Let $x = \sqrt{2}^{\sqrt{2}}$. Either $x$ is rational or $x$ is irrational.

Case 1: $x$ is rational. Take $a = b = \sqrt{2}$. Both are irrational, and $a^b = x$ is rational.

Case 2: $x$ is irrational. Take $a = x$ and $b = \sqrt{2}$. Both are irrational, and

$$
a^b = \left(\sqrt{2}^{\sqrt{2}}\right)^{\sqrt{2}} = \sqrt{2}^{\,\sqrt{2} \cdot \sqrt{2}} = \sqrt{2}^{\,2} = 2,
$$

which is rational. In both cases there are irrational numbers $a$ and $b$ with $a^b$ rational. $\blacksquare$

Look back: the proof never decides which case is true. (A later theorem of Gelfond and Schneider shows that $\sqrt{2}^{\sqrt{2}}$ is irrational, so Case 2 is the real one, but the proof above doesn't need it.) A constructive proof also exists: take $a = \sqrt{2}$ and $b = \log_2 9$. Then $a^b = 2^{\frac{1}{2}\log_2 9} = 2^{\log_2 3} = 3$. The number $b$ is irrational, because if $\log_2 9 = \frac{p}{q}$ with positive integers $p$ and $q$, then $2^p = 9^q$, which is impossible: the left side is even and the right side is odd.

Check: in floating point, `(2 ** 0.5) ** (2 * math.log2(3))` is `3.0000000000000004`, which is 3 up to rounding.

</div>

<div class="example" markdown>

### Example 3: the zero and the opposite are unique

The real number axioms say there is a number $0$ with $a + 0 = a$ for every $a$ (A4), and for each $a$ a number $-a$ with $a + (-a) = 0$ (A5). They say "there is", not "there is exactly one". Uniqueness follows, and it is what lets us say "the zero" and "the opposite of $a$". Here $a$, $b$, $c$ and $z$ are real numbers, and we cite the axioms from [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#the-field-axioms).

*Theorem 4.* (a) If $z$ satisfies $a + z = a$ for every real number $a$, then $z = 0$. (b) If $a + b = 0$ and $a + c = 0$, then $b = c$.

*Proof.* (a) Suppose $z$ has the property. Apply the property with $a = 0$: $0 + z = 0$. By commutativity (A2) and the identity axiom (A4), $0 + z = z + 0 = z$. So $z = 0$.

(b) Suppose $a + b = 0$ and $a + c = 0$. Then

$$
b = b + 0 = b + (a + c) = (b + a) + c = (a + b) + c = 0 + c = c.
$$

The steps use, in order, A4, the hypothesis $a + c = 0$, A3, A2, the hypothesis $a + b = 0$, and A2 with A4 (since $0 + c = c + 0 = c$). $\blacksquare$

Look back: the proofs never solve for anything. They assume two objects with the same property, and a chain of equalities connects them. The earlier proof of the opposite's uniqueness (Theorem 1 part 2 in the axioms lesson) cancelled a summand; this one avoids cancellation. Both are fine. Check with numbers: if $a = 7$, $b = -7$ and $c = -7$, the chain reads $-7 = -7 + 0 = -7 + (7 + (-7)) = (-7 + 7) + (-7) = 0 + (-7) = -7$.

</div>

<div class="example" markdown>

### Example 4: the equation $ax = b$

*Theorem 5.* Let $a$ and $b$ be real numbers with $a \ne 0$. Then there is exactly one real number $x$ such that $ax = b$.

What we know: the field axioms, and in particular that $a \ne 0$ gives a reciprocal $a^{-1}$ with $a a^{-1} = 1$ (M5). What we want: existence and uniqueness. The plan: the reciprocal gives the candidate $x = a^{-1}b$; for uniqueness, multiply an equation by $a^{-1}$.

*Proof.* Existence. Put $x = a^{-1}b$. Then $ax = a(a^{-1}b) = (aa^{-1})b = 1 \cdot b = b$, by M3, M5 and M4.

Uniqueness. Suppose $ax = b$ and $ay = b$. Then $ax = ay$. Multiply both sides by $a^{-1}$: $a^{-1}(ax) = a^{-1}(ay)$, so $(a^{-1}a)x = (a^{-1}a)y$, that is, $1 \cdot x = 1 \cdot y$, so $x = y$.

So there is exactly one solution, $x = a^{-1}b = \frac{b}{a}$. $\blacksquare$

Look back: the hypothesis $a \ne 0$ is used twice, to get $a^{-1}$ in each half. If $a = 0$ the equation is $0 \cdot x = b$. For $b \ne 0$ there is no solution, and for $b = 0$ every $x$ is a solution. So the failure is not "two solutions": the count goes from one to none or to infinitely many. The same thing happens for linear systems, as in [systems of linear equations](../../03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md): one solution, none, or infinitely many.

Check: $a = -2$ and $b = 3$ give $x = -\frac{3}{2}$, and $(-2)(-\frac{3}{2}) = 3$. For $a = 5$, $b = 7$: $x = \frac{7}{5}$, and $5 \cdot \frac{7}{5} = 7$.

</div>

<div class="example" markdown>

### Example 5: the reciprocal is unique (finish it yourself)

*Theorem 6.* Let $a$ be a real number. If $ab = 1$ and $ac = 1$, then $b = c$.

What we know: both $b$ and $c$ are reciprocals of $a$, so $ab = 1$ and $ac = 1$. What we want: $b = c$. The plan: mimic Theorem 4(b), with 1 and multiplication in place of 0 and addition. Start from $b = b \cdot 1$ and replace the 1 using $ac = 1$.

Now write the chain of equalities from $b$ to $c$, and name the axiom for each step.

<details class="solution" markdown>
<summary>Finish</summary>

$b = b \cdot 1 = b(ac) = (ba)c = (ab)c = 1 \cdot c = c$.

The steps use M4 (identity), the hypothesis $ac = 1$, M3 (associative), M2 (commutative), the hypothesis $ab = 1$, and M4 with M2 for $1 \cdot c = c$. $\blacksquare$

Check: $a = 4$ and $b = c = \frac{1}{4}$ give $\frac{1}{4} = \frac{1}{4} \cdot 1 = \frac{1}{4}(4 \cdot \frac{1}{4}) = (\frac{1}{4} \cdot 4)\frac{1}{4} = 1 \cdot \frac{1}{4} = \frac{1}{4}$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for a uniqueness proof that is taken for an existence proof. "Let $N$ be the largest integer. If $M$ is also the largest integer, then $M \le N$ and $N \le M$, so $M = N$" is a valid argument that there is at most one largest integer. It does not show that one exists, and none does. Uniqueness only talks about objects that you are given. If the problem asks for exactly one, the existence half is a separate piece of work.

</div>

<div class="warning" markdown>

Watch out for a witness that is not in the domain, or that satisfies only part of the property. For "there is an integer $x$ with $2x = 5$", the value $x = \frac{5}{2}$ solves the equation and is not an integer, so it proves nothing about integers. For "there is a prime $p$ such that $p + 2$ and $p + 6$ are both prime", the value $p = 3$ gives $5$ and $9$, and 9 fails, so you need to check every condition.

</div>

<div class="warning" markdown>

Watch out for the order of quantifiers. "For every $x$ there exists $y$ with $y > x$" lets $y$ depend on $x$. "There exists $y$ such that for every $x$, $y > x$" asks for one $y$ that works for all $x$, and it is false for the integers. In an existence proof of the first kind, introduce $x$ before the witness; a witness written before $x$ can't mention $x$.

</div>

<div class="warning" markdown>

Watch out for solving first and calling it uniqueness. The "proof" "Let $x$ and $y$ be solutions of $x^2 = 4$. Then $x = 2$ and $y = 2$, so $x = y$" skipped the root $-2$ in the step "then $x = 2$". Uniqueness has to follow from the equations for $x$ and $y$ without choosing which root they are. Here it cannot, because the claim is false: $2$ and $-2$ are both solutions. A real uniqueness proof reaches $x = y$ through steps that are each forced by the two equations.

</div>

<div class="warning" markdown>

Watch out for the sign of the remainder. The remainder in the division algorithm is never negative, and the divisor is positive. For $n = -17$ and $d = 5$ the answer is $q = -4$ and $r = 3$, not $q = -3$ and $r = -2$. Python's `divmod(-17, 5)` returns `(-4, 3)`, matching the theorem. Some other languages (C, Java) truncate toward zero and return $-2$ for the remainder, which is a different convention.

</div>

Uniqueness shows that two objects are equal; it does not show that they are different. The word "unique" never means "different from the others".

## Tricks and shortcuts

To find a witness, work backwards from what it must satisfy. If you need $x$ with $x^2 + x = 56$, treat the equation as one to solve, find $x = 7$, and then write the proof forwards: "Take $x = 7$. Then $49 + 7 = 56$."

To prove uniqueness of a solution to an equation, subtract the two equations. If $ax = b$ and $ay = b$, then $a(x - y) = 0$, and when $a \ne 0$ this gives $x = y$ in one step.

If you can solve an equation by a chain of reversible steps that ends in "$x = \dots$", you have proved existence and uniqueness together. The chain shows that the solutions are exactly that one value.

When you need a witness that is hard to build, ask whether counting, continuity or contradiction gives a guarantee instead. The cost is that you lose the explicit object; the gain is a proof that fits on three lines.

## In code

A program can look for a witness, and can test existence and uniqueness over a finite range. It can't prove either for all integers. The code below finds a witness, checks that the division algorithm has exactly one answer for each input in a box, and compares with `divmod`.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

# existence by search: an integer x with x^2 + x = 56
print([x for x in range(-20, 21) if x * x + x == 56])        # [-8, 7]: existence, and not uniqueness

# exactly one pair (q, r) with n = q*d + r and 0 <= r < d
def pairs(n, d):
    return [(q, n - q * d) for q in range(-100, 101) if 0 <= n - q * d < d]

print(pairs(-17, 5))                                          # [(-4, 3)]
print(all(len(pairs(n, d)) == 1 for n in range(-50, 51) for d in range(1, 13)))   # True
print(all(pairs(n, d)[0] == divmod(n, d) for n in range(-50, 51) for d in range(1, 13)))   # True

# consecutive composites: n! + 2, ..., n! + n are n - 1 consecutive composite numbers
def is_prime(m):
    return m > 1 and all(m % k for k in range(2, math.isqrt(m) + 1))

print([math.factorial(5) + k for k in range(2, 6)])           # [122, 123, 124, 125]
print([is_prime(math.factorial(5) + k) for k in range(2, 6)]) # [False, False, False, False]

# bisection: the "unnamed" root of x^3 + x - 1 between 0 and 1
lo, hi = 0.0, 1.0
for _ in range(50):
    mid = (lo + hi) / 2
    if mid ** 3 + mid - 1 < 0:
        lo = mid
    else:
        hi = mid
print(round(lo, 4))                                           # 0.6823
```

The first search finds two witnesses, so that equation has existence without uniqueness among the integers. The test on 1,212 pairs $(n, d)$ supports Theorem 1, and the proof covers every integer. The bisection loop is the intermediate value theorem turned into a method.

</details>

## FAQ

### Is a non-constructive proof really a proof?

Yes. It proves the claim "there exists" as firmly as a witness does. What it does not give is a way to find the object. If you need the object, for example inside a program, then you want a constructive proof, and a non-constructive one is a reason to go looking for an algorithm. For many theorems both kinds exist.

### Does "unique" mean "exactly one" or "at most one"?

In everyday math writing, "there is a unique $x$ such that..." means exactly one, existence and uniqueness together. On its own, "$x$ is unique" is usually read as "at most one". Whenever it matters, say "exactly one" or "at most one".

### Why can we say "the identity" and "the quotient"?

Because uniqueness has been proved. The word "the" promises that there is exactly one object that fits. Before the proof, you may only say "an identity" or "a quotient and remainder pair". This is also the reason a function must be well defined: if two different outputs were allowed for one input, "the output" would be ambiguous.

### Can I prove uniqueness by contradiction?

Yes. Suppose $x \ne y$ both have the property, derive a contradiction, and conclude $x = y$. It is the same proof in different words. The direct version, which ends at $x = y$, is usually shorter.

## Practice

### Warm-up

1\. Prove each existence claim by naming a witness and checking it. (a) There is an integer $x$ with $x^2 - 5x + 6 = 0$. (b) There are integers $a$ and $b$ with $6a + 10b = 2$. (c) There is a prime $p$ such that $p + 2$ and $p + 6$ are both prime.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Take $x = 2$: $4 - 10 + 6 = 0$. (So does $x = 3$.)
- (b) Take $a = 2$ and $b = -1$: $12 - 10 = 2$.
- (c) Take $p = 5$: it is prime, $5 + 2 = 7$ is prime and $5 + 6 = 11$ is prime.

Check: the arithmetic in each line is complete, and each witness is an integer (a prime for (c)). Each claim is existential, so one verified witness is a proof.

</details>

2\. For each claim, say whether there is none, exactly one, or more than one such object. (a) A real $x$ with $3x + 1 = 10$. (b) An integer $x$ with $x^2 = 9$. (c) A real $x$ with $x^2 = -1$. (d) A natural number $n$ with $n + n = n$. (e) An integer $x$ with $2 < x < 3$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Exactly one: $x = 3$.
- (b) More than one: $x = 3$ and $x = -3$.
- (c) None: a real square is never negative.
- (d) Exactly one: $n + n = n$ gives $n = 0$.
- (e) None: no integer lies strictly between 2 and 3.

Check: substitute (a) $3 \cdot 3 + 1 = 10$, (b) $(-3)^2 = 9$, (d) $0 + 0 = 0$.

</details>

3\. Find the quotient and remainder, as in Theorem 1. (a) $n = 100$, $d = 8$. (b) $n = -23$, $d = 6$. (c) $n = 0$, $d = 5$. (d) $n = -5$, $d = 5$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $100 = 12 \cdot 8 + 4$, so $q = 12$ and $r = 4$.
- (b) $-23 = (-4) \cdot 6 + 1$, so $q = -4$ and $r = 1$. The choice $q = -3$ would leave $r = -5$, which is negative.
- (c) $0 = 0 \cdot 5 + 0$, so $q = 0$ and $r = 0$.
- (d) $-5 = (-1) \cdot 5 + 0$, so $q = -1$ and $r = 0$.

Check: $12 \cdot 8 + 4 = 100$; $-24 + 1 = -23$; $0 + 0 = 0$; $-5 + 0 = -5$. Each remainder is at least 0 and less than $d$.

</details>

### Standard

4\. Prove that for every real number $x$ there is exactly one real number $y$ with $3y - 2x = 5$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $x$ is a given real number. What we want: existence and uniqueness of $y$. The plan: solve for $y$, then check, and show any two solutions agree.

*Proof.* Let $x$ be a real number. Existence. Put $y = \frac{5 + 2x}{3}$. Then $3y - 2x = 5 + 2x - 2x = 5$.

Uniqueness. Suppose $3y - 2x = 5$ and $3y' - 2x = 5$. Subtracting, $3y - 3y' = 0$, so $3(y - y') = 0$, and since $3 \ne 0$, $y = y'$. $\blacksquare$

Check: $x = 2$ gives $y = 3$ and $3 \cdot 3 - 4 = 5$. For $x = -1$: $y = 1$ and $3 - (-2) = 5$.

</details>

5\. Prove that any set of 11 integers chosen from $\{1, 2, \dots, 20\}$ contains two consecutive integers. Then show that 11 can't be replaced by 10.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the boxes $\{1, 2\}, \{3, 4\}, \dots, \{19, 20\}$. What we want: two chosen numbers that are consecutive. The plan: pigeonhole with 10 boxes.

*Proof.* Split $\{1, \dots, 20\}$ into the 10 pairs $\{1, 2\}, \{3, 4\}, \dots, \{19, 20\}$. Eleven chosen numbers go into 10 pairs, so some pair holds two of them. The two members of a pair are consecutive. $\blacksquare$

The bound is tight: the 10 numbers $1, 3, 5, \dots, 19$ contain no two consecutive integers.

Check: add any eleventh number to $\{1, 3, 5, \dots, 19\}$ and a consecutive pair appears. Adding 4 gives $3, 4$, and adding 20 gives $19, 20$.

</details>

6\. Find the flaw. Claim: "the equation $x^2 = x$ has exactly one real solution. Proof. Existence: $x = 1$ works, since $1^2 = 1$. Uniqueness: if $x^2 = x$, divide by $x$ to get $x = 1$. So any solution equals 1." Say whether the claim is true.

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is in the uniqueness half. Dividing by $x$ is allowed only when $x \ne 0$, and the proof never rules out $x = 0$. The value $x = 0$ satisfies $0^2 = 0$, so it is a second solution and the claim is false: there are exactly two real solutions, 0 and 1.

A correct uniqueness argument for the claim would have to survive the case $x = 0$ and can't. The correct statement is "there is exactly one nonzero real solution", and its uniqueness proof first assumes $x \ne 0$.

Check: $0^2 = 0$ and $1^2 = 1$. The factorization $x^2 - x = x(x - 1) = 0$ shows the two roots at once.

</details>

### Challenge

7\. Prove that for every positive integer $n$ there exist $n$ consecutive composite positive integers. (Hint: look at $(n + 1)! + 2$, $(n + 1)! + 3$, and so on.)

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $(n + 1)! = 1 \cdot 2 \cdots (n + 1)$ is divisible by every integer $k$ from 2 to $n + 1$. What we want: $n$ consecutive integers, each with a divisor other than 1 and itself. The plan: the numbers $(n + 1)! + k$ for $k = 2, \dots, n + 1$ are $n$ consecutive integers, and each is divisible by $k$.

*Proof.* Let $n$ be a positive integer, and for each integer $k$ with $2 \le k \le n + 1$ let $m_k = (n + 1)! + k$. These are $n$ consecutive integers. Since $k$ divides $(n + 1)!$ and $k$ divides $k$, Corollary 4 of [definitions, theorems, lemmas and corollaries](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md) gives $k \mid m_k$. Also $k \ge 2$, and $k < m_k$ because $(n + 1)! \ge 1$. So $m_k$ has the divisor $k$, which is neither 1 nor $m_k$, and $m_k$ is composite. $\blacksquare$

Look back: this is a constructive existence proof whose witness depends on $n$. It shows that gaps between primes can be as long as you like. Check: $n = 4$ gives $5! = 120$ and the numbers $122, 123, 124, 125$, which are divisible by $2, 3, 4, 5$ in turn. For $n = 3$: $26, 27, 28$.

</details>

8\. (Reviews [long division](../../01-elementary/07-long-division.md).) Use Theorem 1 with $d = 2$ to prove that every integer is even or odd, and that no integer is both.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Theorem 1 with $d = 2$. For each integer $n$ there is exactly one pair $q$, $r$ with $n = 2q + r$ and $0 \le r < 2$, so $r$ is 0 or 1. What we want: $n$ is even or odd, and not both. The plan: existence gives "even or odd", uniqueness gives "not both".

*Proof.* Let $n$ be an integer. By the existence half of Theorem 1, $n = 2q + r$ with $r = 0$ or $r = 1$. If $r = 0$ then $n = 2q$, and $n$ is even. If $r = 1$ then $n = 2q + 1$, and $n$ is odd. So $n$ is even or odd.

Suppose $n$ were both even and odd: $n = 2k$ and $n = 2j + 1$ for integers $k$ and $j$. Then $n = 2k + 0 = 2j + 1$ are two representations of the form $2q + r$ with $0 \le r < 2$, with remainders 0 and 1. That contradicts the uniqueness half of Theorem 1. So no integer is both. $\blacksquare$

Check: $n = -7$ has $q = -4$ and $r = 1$ ($-8 + 1$), so it is odd, and there is no integer $k$ with $2k = -7$. This justifies the step "an even integer is not odd" used in [if and only if proofs](01-if-and-only-if-proofs.md).

</details>

## Where this shows up

- The next lessons use these patterns: [proofs about sets](03-proofs-about-sets.md) proves that a set is unique when it has a given membership test, and [counterexamples and disproof](04-counterexamples-and-disproof.md) shows how to disprove an existence claim, which is harder than disproving a "for every" claim. The division algorithm is the starting point of [divisibility and modular arithmetic](../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md) and of [GCD and Euclid's algorithm](../../06-cs-math/02-number-theory/02-gcd-and-euclids-algorithm.md).
- In CS, existence arguments appear as pigeonhole bounds and as the existence of a fixed point, and uniqueness is the reason an algorithm's output is well defined. A hash table with more keys than buckets must have a collision, by the pigeonhole principle. Unique decoding in a code is a uniqueness theorem.
- In economics, an equilibrium theorem says that a solution exists and, with more assumptions, that it is unique. Existence usually comes from a continuity argument like the intermediate value theorem, and uniqueness from monotonicity: if the supply minus demand curve is strictly increasing in price, it crosses zero at most once.
