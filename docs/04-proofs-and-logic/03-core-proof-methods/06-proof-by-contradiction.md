# Proof by contradiction

After this lesson you can prove a statement by assuming it is false and reaching an impossibility, announce the method before you start, write the proofs that $\sqrt{2}$ is irrational and that there are infinitely many primes, choose between contradiction and contrapositive, and spot the three usual errors.

Before this: [contrapositive proof](05-contrapositive-proof.md), [direct proof](01-direct-proof.md), and [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md). The middle-school lesson [roots, irrationals and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#proving-that-the-square-root-of-2-is-irrational) gave a gentle version of the first proof, and [how to read a proof](02-how-to-read-a-proof.md) read the second line by line.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. To prove "there is no largest integer" by contradiction, what do you assume in the first line?
2. A proof assumes $\sqrt{2} = \frac{a}{b}$ and reaches $a^2 = 2b^2$, then writes "which is a contradiction." Is that a contradiction?
3. A student proves "all primes greater than 2 are odd" by assuming "all primes greater than 2 are even" and noting that 3 is a prime that is not even. What did the student actually prove?

<details class="solution" markdown>
<summary>Answers</summary>

1. "Suppose, for contradiction, that there is a largest integer $M$", so that $n \le M$ for every integer $n$.
2. No. The equation $a^2 = 2b^2$ is not false; it is a consequence of the assumption. The proof must go on until it reaches a statement that is false or that clashes with something known (the proof of Example 1 below finds that $a$ and $b$ have a common factor, against the way they were chosen).
3. Only that "not all primes greater than 2 are even". That is much weaker than the claim. The correct assumption is the negation of the claim: "some prime greater than 2 is even".

</details>

## The idea

A detective's argument goes: "Suppose the butler did it. Then he was in the library at nine. But the camera shows him in the kitchen at nine. So he didn't do it." The structure is the same every time. You assume what you want to rule out, follow the consequences, and meet a fact that can't be true. The only thing that can be wrong is the assumption, so the assumption goes.

In mathematics the same move proves statements that have no good direct route. Take "$\sqrt{2}$ is irrational". A direct proof would need to show that no fraction of integers has square 2, and there are infinitely many fractions to rule out. Turn it around: suppose some fraction does have square 2. Now we hold a particular fraction in our hands, and we can compute with it. The computation shows that the fraction could be simplified forever, which is impossible.

Contradiction is especially natural for statements of the form "there is no ...", "there are infinitely many ...", and "this number is not ...". Each of these denies something or says something is unlimited. Their negations ("there is one", "there are only finitely many", "this number is ...") give a concrete object or a finite list to work with.

It also has a famous use in computer science. A program that decides whether other programs halt can't exist, and the proof is a contradiction: assume it exists, feed it a program built to defeat it, and watch it be wrong either way. A sketch comes at the end of this lesson.

## Definitions

A **contradiction** is a statement that cannot be true: either a statement of the form "$R$ and not $R$", or a statement that clashes with a hypothesis, a definition or a result you have proved. In plain words, it is two claims that can't both hold, such as "$a$ and $b$ have no common factor" and "$2$ is a common factor of $a$ and $b$".

A **proof by contradiction** of a statement $S$ assumes that $S$ is false and derives a contradiction, then concludes that $S$ is true. In plain words, you show that the opposite of what you want leads somewhere impossible. For a conditional "if $P$, then $Q$", the false case is "$P$ is true and $Q$ is false", so the proof assumes $P$ and not $Q$.

Why the method is valid: suppose "not $S$" leads to a contradiction. A true statement can't imply a false one, so "not $S$" can't be true, and $S$ is true. In the logic of [truth tables and logical equivalence](../02-logic-and-sets/03-truth-tables-and-logical-equivalence.md), the statement "if not $S$ then (some statement and its negation)" is equivalent to $S$.

## How to do it

### Proof by contradiction in six steps

1. Write the claim $S$ exactly, and write its negation exactly. Use the negation rules: "not (for every)" is "there exists ... not", "not ($P$ or $Q$)" is "not $P$ and not $Q$". For "if $P$, then $Q$", the negation is "$P$ and not $Q$".
2. Announce the method in the first line: "Suppose, for contradiction, that [the negation]." The reader should know from the first sentence where the proof is going and what its last line must be.
3. Unpack the assumption. Introduce letters for the objects it provides, and add any choice you can justify (see the lemma on lowest terms below).
4. Derive consequences by ordinary steps, aiming at something false. Keep every step justified, because a contradiction built on an unjustified step proves nothing.
5. State the contradiction explicitly: "This contradicts the choice of $a$ and $b$", "but $p > 1$".
6. Conclude: "Therefore the assumption is false, and $S$ is true."

Do not write the assumption as if it were a fact. After the conclusion, the assumption is gone. Nothing derived under it can be used later.

### Two lemmas the proofs below need

The proofs of Examples 1 and 2 each use a fact that textbooks tend to state without proof. Both are short contradiction proofs, and they use the well-ordering principle: every nonempty set of positive integers has a smallest member (proved and used further in [strong induction and well-ordering](../05-induction/02-strong-induction-and-well-ordering.md)).

*Lemma 1.* Every rational number $r$ can be written $r = \frac{a}{b}$ with integers $a$ and $b$, $b > 0$, and no common divisor of $a$ and $b$ greater than 1 (lowest terms).

*Proof.* Let $r$ be rational. The set of positive integers $b$ for which $r = \frac{a}{b}$ for some integer $a$ is nonempty, because $r$ has some fraction with a nonzero denominator, and changing the signs of numerator and denominator if necessary makes the denominator positive. Let $b$ be the smallest member of this set, and $a$ an integer with $r = \frac{a}{b}$. Suppose, for contradiction, that $d > 1$ is a common divisor of $a$ and $b$. Then $a = da'$ and $b = db'$ for integers $a'$ and $b'$, with $b' > 0$ and $r = \frac{a'}{b'}$, and $b' < b$. That contradicts the choice of $b$ as the smallest. So no such $d$ exists. $\blacksquare$

*Lemma 2.* Every integer $N > 1$ has a prime divisor.

*Proof.* Let $N > 1$. The set of divisors of $N$ that are greater than 1 is nonempty (it contains $N$), so it has a smallest member $d$. Suppose, for contradiction, that $d$ is not prime. Then $d$ has a divisor $e$ with $1 < e < d$. Since $e \mid d$ and $d \mid N$, we have $e \mid N$ (divisibility is transitive, [Proposition 5](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#worked-examples)), so $e$ is a divisor of $N$ greater than 1 and smaller than $d$. That contradicts the choice of $d$. So $d$ is prime. $\blacksquare$

### Contradiction or contrapositive?

The two methods start alike and differ in what they aim at. A contrapositive proof assumes "not $Q$" and aims at a specific target, "not $P$". A contradiction proof assumes "$P$ and not $Q$" and aims at anything false. Every contrapositive proof is a contradiction proof where the contradiction is "not $P$" against the hypothesis $P$. But when the target is known in advance, the contrapositive version is cleaner and says so up front.

| Contrapositive | Contradiction |
|---|---|
| for a claim "if $P$, then $Q$" | for any claim, including those with no hypothesis ("$\sqrt{2}$ is irrational") |
| assumes "not $Q$" only | assumes the negation of the whole claim |
| the last line is "not $P$", known at the start | the last line is some contradiction, found along the way |
| use when negating $Q$ gives something concrete and "not $P$" is the natural end | use when the claim is a flat denial or an unlimited statement, or no target is in sight |

Here is one claim, "if $n^2$ is even, then $n$ is even", proved both ways. By contradiction: suppose $n^2$ is even and $n$ is odd; then $n = 2k + 1$, so $n^2 = 2(2k^2 + 2k) + 1$ is odd, which contradicts $n^2$ being even. By contrapositive: suppose $n$ is odd; then $n^2 = 2(2k^2 + 2k) + 1$ is odd. The computation is identical, and the contrapositive says what it is doing without the extra assumption. For "$\sqrt{2}$ is irrational", there is no hypothesis to turn into a target, so contradiction is the natural choice.

## Worked examples

<div class="example" markdown>

### Example 1: the square root of 2 is irrational

*Theorem 1.* The number $\sqrt{2}$ is irrational.

What we know: "irrational" means "not rational", so the negation of the claim is "$\sqrt{2}$ is rational". We have Lemma 1 (lowest terms) and Theorem 2 of [contrapositive proof](05-contrapositive-proof.md#worked-examples): if $n^2$ is even, then $n$ is even. What we want: a contradiction. The plan: assume $\sqrt{2} = \frac{a}{b}$ in lowest terms, show that both $a$ and $b$ must be even, and note that this clashes with lowest terms.

Step 1 and 2: the negation of "irrational" is "rational", so we begin by announcing the assumption.

*Proof.* Suppose, for contradiction, that $\sqrt{2}$ is rational.

Step 3. By Lemma 1, $\sqrt{2} = \frac{a}{b}$ for integers $a$ and $b$ with $b > 0$ that have no common divisor greater than 1.

Step 4. Squaring both sides gives $2 = \frac{a^2}{b^2}$, so $a^2 = 2b^2$. Hence $a^2$ is even, and by Theorem 2 of the previous lesson, $a$ is even. Write $a = 2k$ for an integer $k$. Substituting, $4k^2 = 2b^2$, so $b^2 = 2k^2$. Hence $b^2$ is even, and by the same theorem, $b$ is even.

Step 5. Now 2 divides both $a$ and $b$, and $2 > 1$. This contradicts the choice of $a$ and $b$ with no common divisor greater than 1.

Step 6. So the assumption was false, and $\sqrt{2}$ is irrational. $\blacksquare$

Look back: the proof is a chain. The assumption gave a fraction, the fraction gave $a^2 = 2b^2$, and the evenness of squares pushed the factor 2 into both $a$ and $b$. The number 2 matters: the same steps for $\sqrt{4}$ give $a^2 = 4b^2$ and $a = 2k$ yields $b^2 = k^2$, with no clash (the test from [how to read a proof](02-how-to-read-a-proof.md#practice)). Lowest terms matters too: without it, "both even" is no contradiction. Check: the equation $a^2 = 2b^2$ has no solution in positive integers. For $b = 5$, $2b^2 = 50$ is not a square, and for $b = 12$, $2b^2 = 288$, which lies between $16^2 = 256$ and $17^2 = 289$.

</div>

<div class="example" markdown>

### Example 2: infinitely many primes

*Theorem 2 (Euclid).* There are infinitely many primes.

What we know: Lemma 2 (every integer greater than 1 has a prime divisor), and the linear combination theorem ([Theorem 3](../01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#building-on-lemmas)). What we want: a contradiction from "finitely many". The plan: given a finite list of all primes, build a number whose prime divisors are all outside the list.

*Proof.* Suppose, for contradiction, that there are only finitely many primes, and list all of them: $p_1, p_2, \dots, p_n$. Let

$$
N = p_1 p_2 \cdots p_n + 1.
$$

Each $p_k \ge 2$, so $N \ge 3 > 1$. By Lemma 2, $N$ has a prime divisor $p$. Since the list contains every prime, $p = p_i$ for some $i$. Then $p \mid p_1 p_2 \cdots p_n$, because $p$ is one of the factors, and $p \mid N$. By the linear combination theorem, $p$ divides $N - p_1 p_2 \cdots p_n = 1$. A prime is greater than 1, and no integer greater than 1 divides 1 (if $1 = pk$ with $k$ an integer, then $k > 0$ and $pk \ge p > 1$). This is a contradiction. So the list can't contain every prime, and there are infinitely many primes. $\blacksquare$

Look back: the proof does not claim that $N$ is prime, only that $N$ has a prime divisor outside the list. For the first six primes, $N = 30031 = 59 \times 509$ is composite, and its prime divisors 59 and 509 are new. The assumption "the list contains every prime" is used in one line, to say $p = p_i$. Check: with the list $2, 3, 5$ we get $N = 31$, a prime outside the list, and with $2, 3, 5, 7, 11, 13$ we get $N = 30031$, whose divisor 59 is outside the list.

</div>

<div class="example" markdown>

### Example 3: a pigeonhole argument

*Theorem 3.* If 100 balls are put into 9 boxes, some box contains at least 12 balls.

Step 1 and 2: the claim says "some box has at least 12". Its negation is "every box has at most 11", which is a bound we can add up.

*Proof.* Suppose, for contradiction, that every box contains at most 11 balls. Then the total number of balls is at most $9 \times 11 = 99$. But there are 100 balls. This is a contradiction, so some box contains at least 12 balls. $\blacksquare$

Look back: the proof finds no box. It shows that one exists, which is all the claim asks. The same argument shows that $n$ items in $k$ boxes force a box with at least $\lceil \frac{n}{k} \rceil$ items, the pigeonhole principle, taught in inclusion-exclusion and the pigeonhole principle<!-- link: ../../06-cs-math/03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md -->. Check: $9 \times 11 = 99 < 100$, and with 99 balls the claim would fail (11 in each box).

</div>

<div class="example" markdown>

### Example 4: a rational plus an irrational (finish it yourself)

*Theorem 4.* If $r$ is rational and $x$ is irrational, then $r + x$ is irrational.

Steps 1 and 2: the claim is "if $P$, then $Q$" with $P$ = "$r$ is rational and $x$ is irrational" and $Q$ = "$r + x$ is irrational". The negation is "$P$ and not $Q$". Suppose, for contradiction, that $r$ is rational, $x$ is irrational, and $r + x$ is rational. Write $r + x = q$ with $q$ rational.

Now finish: express $x$ in terms of $q$ and $r$, say why that is rational, and name the contradiction.

<details class="solution" markdown>
<summary>Finish</summary>

From $r + x = q$ we get $x = q - r$. The difference of two rational numbers is rational (the sum of rationals is rational, and so is the negative of a rational, which has the fraction $\frac{-a}{b}$). So $x$ is rational. This contradicts the hypothesis that $x$ is irrational. Hence $r + x$ is irrational. $\blacksquare$

Check: $r = \frac{1}{2}$ and $x = \sqrt{2}$: if $\frac{1}{2} + \sqrt{2}$ were rational, say $q$, then $\sqrt{2} = q - \frac{1}{2}$ would be rational, which Example 1 rules out.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for "a contradiction" that isn't one. After "$a^2 = 2b^2$" a proof says "this is a contradiction". It isn't: the equation is a fine statement that follows from the assumption. A contradiction clashes with something already established. If you can't name both halves of the clash ("$a$ and $b$ have no common factor" against "2 is a common factor"), you haven't reached one.

</div>

<div class="warning" markdown>

Watch out for a wrong negation, which proves something weaker. To prove "all primes greater than 2 are odd", assuming "all primes greater than 2 are even" and refuting it with the prime 3 proves only that not all are even. The negation of "all are odd" is "some prime greater than 2 is even". Write the negation as a full sentence, and check it with the table in [contrapositive proof](05-contrapositive-proof.md#negating-the-words-you-meet-in-proofs).

</div>

<div class="warning" markdown>

Watch out for contradiction where a direct proof is shorter. *Claim:* if $m$ and $n$ are even integers, then $m + n$ is even. A student writes: "Suppose, for contradiction, that $m$ and $n$ are even and $m + n$ is odd. Then $m = 2j$ and $n = 2k$, so $m + n = 2(j + k)$ is even. This contradicts $m + n$ odd." The assumption "$m + n$ is odd" was never used until the last line, and then only to be contradicted by the conclusion we wanted. Delete the first assumption and the last sentence, and what remains is the direct proof. If your contradiction proof ends by contradicting your own assumption, with no use of that assumption in between, rewrite it directly.

</div>

<div class="warning" markdown>

Watch out for circular support. A contradiction needs a false statement derived from the assumption by valid steps. If one of the steps quotes a result whose proof depends on the claim you are proving, the argument goes in a circle. For Example 2, Lemma 2 must not be proved using the infinitude of primes.

</div>

The assumption is local. Once the proof concludes, "the number $N$" and "the fraction $\frac{a}{b}$" don't exist in the world of the theorem. They were the characters in a hypothetical.

## Tricks and shortcuts

A claim that says "no", "not", "never", "irrational", "infinitely many" or "there is no largest" is a candidate. Write the negation first and see whether it gives you a concrete object (a fraction, a largest element, a finite list).

State what you will contradict as soon as you can. In Example 1 you know from the start that the contradiction will be about lowest terms; in Example 2, about a prime dividing 1. Keeping the target in mind stops you from wandering.

If a contradiction proof's last line contradicts the hypothesis of the theorem, the proof can usually be rewritten as a contrapositive. If it contradicts the assumption you just made, rewrite it directly. If it contradicts something else (a choice such as lowest terms, or a known fact), you have a real contradiction proof.

## In code

A computer can't prove that $\sqrt{2}$ is irrational, but it can show that the equation at the centre of the proof, $a^2 = 2b^2$, has no small solutions, and it can run the construction from Euclid's proof. The last block builds the diagonal program of the halting problem against two candidate deciders. The strings `"halts"` and `"loops forever"` stand in for the behaviour of a program, since actually looping forever would stop the demonstration.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import isprime, primerange

# no solutions of a^2 = 2 b^2 in positive integers up to 2000
print([(a, b) for b in range(1, 2001) for a in range(1, 2829) if a * a == 2 * b * b])   # []

# Euclid's construction: N = product of the first k primes + 1 has a prime factor outside the list
def smallest_prime_factor(n):
    return next(p for p in primerange(2, n + 1) if n % p == 0)

for k, ps in enumerate([[2, 3, 5], [2, 3, 5, 7, 11, 13]], start=1):
    N = 1
    for p in ps:
        N *= p
    N += 1
    p = smallest_prime_factor(N)
    print(N, isprime(N), p, p in ps)
# 31 True 31 False
# 30031 False 59 False

# pigeonhole: 99 balls can fill 9 boxes with 11 each, but 100 cannot
print(9 * 11, 9 * 11 < 100)    # 99 True

# the diagonal program of the halting problem, against two candidate deciders
def make_diagonal(halts):
    def D(program):
        if halts(program, program):
            return "loops forever"       # stands for: while True: pass
        return "halts"                   # stands for: return
    return D

for name, h in [("always_yes", lambda p, x: True), ("always_no", lambda p, x: False)]:
    D = make_diagonal(h)
    print(name, "claims D(D) halts:", h(D, D), "| D(D) actually", D(D))
# always_yes claims D(D) halts: True | D(D) actually loops forever
# always_no claims D(D) halts: False | D(D) actually halts
```

In the last block, whatever a candidate decider says about $D(D)$, the program $D$ does the opposite. A real proof does this for every possible decider at once.

</details>

## FAQ

### Why does assuming something false let me prove something true?

You aren't proving the true thing from the false one. You are showing that the assumption cannot be true, because it leads to a statement that can't be true either. Since the claim and its negation can't both fail, ruling out the negation leaves the claim. The false assumption is a hypothetical, discarded as soon as the contradiction is reached.

### Is it cheating to assume what I want to prove is false?

No, because you aren't assuming it and keeping it. You assume the opposite temporarily and show it collapses. The thing that would be cheating is assuming the claim itself and deriving a true statement from it; that is the backward argument warned against in [direct proof](01-direct-proof.md#edge-cases-and-common-mistakes).

### How do I know when I have a contradiction?

You have one when two statements on the page can't both be true, and you can point to both. They may be a statement and its negation, a result and a hypothesis, or a value and a definition (such as "$p$ divides 1" against "$p > 1$"). If you can't point to both, keep going.

### What is the halting problem proof, in a few lines?

Suppose a program $H$ could decide, for every program $p$ and input $x$, whether $p$ halts on $x$. Build a program $D$: given a program $p$, ask $H$ whether $p$ halts when run on its own code; if $H$ says yes, loop forever, and if $H$ says no, halt. Now run $D$ on its own code. If $H$ says $D(D)$ halts, then $D$ loops, so $H$ was wrong. If $H$ says $D(D)$ doesn't halt, then $D$ halts, so $H$ was wrong. Either way $H$ fails, so no such $H$ exists. The full argument, with careful definitions, is in decidability and the halting problem<!-- link: ../../06-cs-math/06-theory-of-computation/05-decidability-and-the-halting-problem.md -->.

## Practice

### Warm-up

1\. Write the first line (the assumption) of a proof by contradiction for each claim. (a) There is no largest integer. (b) $\sqrt{3}$ is irrational. (c) Every integer greater than 1 has a prime divisor. (d) No integer is both even and odd.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) "Suppose, for contradiction, that $M$ is the largest integer", so every integer $n$ satisfies $n \le M$.
- (b) "Suppose, for contradiction, that $\sqrt{3}$ is rational", so $\sqrt{3} = \frac{a}{b}$ in lowest terms.
- (c) "Suppose, for contradiction, that some integer $N > 1$ has no prime divisor." (The negation of "every" is "some ... not".)
- (d) "Suppose, for contradiction, that some integer $n$ is both even and odd", so $n = 2j$ and $n = 2k + 1$.

Check: in each case the assumption is the full negation of the claim, with its quantifier changed where needed.

</details>

2\. Decide whether each statement is a real contradiction. (a) Assume $\sqrt{2} = \frac{a}{b}$. Then $a^2 = 2b^2$. (b) Assume $x$ is the smallest positive real number. Then $\frac{x}{2}$ is a positive real number smaller than $x$. (c) Assume $n^2$ is even and $n$ is odd. Then $n^2 = 2m + 1$ for an integer $m$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Not a contradiction. $a^2 = 2b^2$ is a consequence of the assumption and clashes with nothing. The proof must continue.
- (b) A real contradiction. $\frac{x}{2}$ is positive and smaller than $x$, but $x$ was assumed smallest. Both halves can be named.
- (c) Not yet a contradiction. The step "$n^2 = 2m + 1$" shows $n^2$ is odd, and the hypothesis says it is even. The contradiction is the two statements "$n^2$ is odd" and "$n^2$ is even" together, and it needs the fact that no integer is both. Once that is said, it is a contradiction.

Check: in (b), $x = 0.001$ gives $0.0005$, smaller and positive.

</details>

3\. A student proves "every prime greater than 2 is odd" like this: "Suppose, for contradiction, that every prime greater than 2 is even. The prime 3 is greater than 2 and is not even. This is a contradiction." What was proved, and what is a correct proof?

<details class="solution" markdown>
<summary>Solution</summary>

The negation of "every prime greater than 2 is odd" is "some prime greater than 2 is not odd", that is, even. The student assumed the stronger statement "every prime greater than 2 is even", and refuting it proves only "not every prime greater than 2 is even", which is a weaker statement than the claim.

A correct proof: suppose, for contradiction, that $p$ is a prime greater than 2 and $p$ is even. Then $p = 2k$ for an integer $k$, so $2 \mid p$. Since $p$ is prime, its positive divisors are only 1 and $p$, so $2 = 1$ or $2 = p$. Neither holds, since $2 \ne 1$ and $p > 2$. This is a contradiction, so $p$ is odd. $\blacksquare$

Check: the primes 3, 5, 7, 11 are odd, and the only even prime is 2.

</details>

### Standard

4\. Prove by contradiction that no integer is both even and odd.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the definitions of even and odd. What we want: a contradiction from an integer being both. The plan: equate the two forms and get an integer equal to $\frac{1}{2}$.

*Proof.* Suppose, for contradiction, that some integer $n$ is both even and odd. Then $n = 2j$ and $n = 2k + 1$ for integers $j$ and $k$. So $2j = 2k + 1$, which gives $2(j - k) = 1$. Hence $j - k = \frac{1}{2}$. But $j - k$ is an integer, and $\frac{1}{2}$ is not (it lies strictly between the integers 0 and 1). This is a contradiction. $\blacksquare$

Look back: the contradiction is between "an integer" and "$\frac{1}{2}$", and both can be named. Check: $2 \cdot 3 = 6$ is even and $2 \cdot 3 + 1 = 7$ is odd, and the two never meet.

</details>

5\. Prove that $\sqrt{3}$ is irrational. You may use the result of problem 6 in [contrapositive proof](05-contrapositive-proof.md#practice): if $3 \mid n^2$, then $3 \mid n$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: Lemma 1 (lowest terms), and if $3 \mid n^2$ then $3 \mid n$. What we want: a contradiction from $\sqrt{3}$ rational. The plan: copy the structure of Example 1, with 3 in place of 2.

*Proof.* Suppose, for contradiction, that $\sqrt{3}$ is rational. By Lemma 1, $\sqrt{3} = \frac{a}{b}$ with $b > 0$ and no common divisor of $a$ and $b$ greater than 1. Squaring, $a^2 = 3b^2$, so $3 \mid a^2$, and so $3 \mid a$. Write $a = 3k$. Then $9k^2 = 3b^2$, so $b^2 = 3k^2$, and $3 \mid b^2$, so $3 \mid b$. Now 3 is a common divisor of $a$ and $b$, and $3 > 1$. This contradicts the choice of $a$ and $b$. $\blacksquare$

Look back: the proof needs "3 divides a square, so 3 divides the number", which holds for primes and fails for 4 ($4 \mid 2^2$ and $4 \nmid 2$); that is why the same argument can't show $\sqrt{4}$ is irrational (it isn't). Check: $a^2 = 3b^2$ has no small solutions: $b = 4$ gives $48$, between $6^2 = 36$ and $7^2 = 49$.

</details>

6\. Rewrite as a direct proof, and say what was unnecessary. *Claim:* if $a$ is odd, then $a + 1$ is even. "Proof. Suppose, for contradiction, that $a$ is odd and $a + 1$ is odd. Then $a = 2j + 1$, so $a + 1 = 2j + 2 = 2(j + 1)$, which is even. This contradicts $a + 1$ being odd."

<details class="solution" markdown>
<summary>Solution</summary>

*Direct proof.* Let $a$ be odd, so $a = 2j + 1$ for some integer $j$. Then $a + 1 = 2j + 2 = 2(j + 1)$, and $j + 1$ is an integer, so $a + 1$ is even. $\blacksquare$

The unnecessary parts are the assumption "$a + 1$ is odd" and the final sentence. The assumption was never used in any step, and the last line contradicted it only by reaching the claim itself.

Check: $a = 7$ gives $a + 1 = 8 = 2 \cdot 4$ with $j = 3$.

</details>

### Challenge

7\. Prove that if $a$, $b$ and $c$ are odd integers, then the equation $ax^2 + bx + c = 0$ has no rational solution.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $a$, $b$, $c$ are odd. What we want: no rational $x$ satisfies the equation. The plan: assume a rational root in lowest terms $\frac{p}{q}$, clear denominators, and look at the parity of each term in the four cases for $p$ and $q$.

*Proof.* Suppose, for contradiction, that $x = \frac{p}{q}$ is a rational solution, written in lowest terms with $q > 0$ (Lemma 1). Substituting and multiplying by $q^2$ gives

$$
ap^2 + bpq + cq^2 = 0.
$$

By lowest terms, $p$ and $q$ are not both even. There are three cases.

- $p$ even and $q$ odd: $ap^2$ and $bpq$ are even, and $cq^2$ is odd (odd times odd times odd). The sum is odd, not 0.
- $p$ odd and $q$ even: $bpq$ and $cq^2$ are even, and $ap^2$ is odd. The sum is odd, not 0.
- $p$ and $q$ both odd: each of the three terms is odd, and the sum of three odd integers is odd, not 0.

In every case the left side is odd, but it equals 0, which is even. This is a contradiction. $\blacksquare$

Look back: a root would force an odd number to equal 0. The cases cover all possibilities because "not both even" leaves exactly these three. Check: $x^2 + x + 1 = 0$ has no real roots at all, and $3x^2 + 5x + 1$ has the roots $\frac{-5 \pm \sqrt{13}}{6}$, which are irrational. A search over odd coefficients up to 9 and fractions $\frac{p}{q}$ with $\lvert p \rvert, q \le 30$ finds no root.

</details>

8\. (Reviews [roots, irrationals and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).) Prove that $3 + 2\sqrt{2}$ is irrational.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $\sqrt{2}$ is irrational (Example 1), and a rational plus an irrational is irrational (Example 4). What we want: $3 + 2\sqrt{2}$ is irrational. The plan: show $2\sqrt{2}$ is irrational by contradiction, then add 3.

*Proof.* First, $2\sqrt{2}$ is irrational. Suppose, for contradiction, that $2\sqrt{2} = q$ with $q$ rational. Then $\sqrt{2} = \frac{q}{2}$, and $\frac{q}{2}$ is rational (a product of the rationals $q$ and $\frac{1}{2}$). That contradicts Example 1.

Now $3$ is rational and $2\sqrt{2}$ is irrational, so by Example 4, $3 + 2\sqrt{2}$ is irrational. $\blacksquare$

Look back: the same pattern shows $a + b\sqrt{2}$ is irrational whenever $a$ and $b$ are rational and $b \ne 0$. Check: $3 + 2\sqrt{2} \approx 5.8284$, and no small fraction matches it: $\frac{35}{6} = 5.8333$ and $\frac{17}{3} = 5.6667$ are off.

</details>

## Where this shows up

- This closes the core methods. The next chapter adds [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md), [existence and uniqueness proofs](../04-more-proof-methods/02-existence-and-uniqueness-proofs.md) (where "suppose there are two" is a contradiction in miniature) and [counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md). The lesson [how to write a proof](07-how-to-write-a-proof.md) shows how to announce and end a contradiction proof cleanly.
- In CS, contradiction is how you show impossibility: the halting problem, and the lower bound that a comparison sort needs at least $\log_2(n!)$ comparisons in the worst case. It appears in decidability and the halting problem<!-- link: ../../06-cs-math/06-theory-of-computation/05-decidability-and-the-halting-problem.md --> and in primes and unique factorization<!-- link: ../../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md -->.
- In economics, no-arbitrage arguments have the same shape: suppose two prices differ, then buying low and selling high is a risk-free profit, which cannot persist in equilibrium, so the prices are equal (present value, NPV and bond prices<!-- link: ../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md -->).
