# Common proof mistakes

After this lesson you can recognise nineteen common mistakes in proofs, say exactly what is wrong in each, and repair the proof.

Before this: the whole folder, but especially [how to write a proof](../03-core-proof-methods/07-how-to-write-a-proof.md), [mathematical induction](../05-induction/01-mathematical-induction.md) and [injective, surjective and bijective](../06-relations-and-functions/05-injective-surjective-bijective.md). Each mistake below links to the lesson that teaches the idea it breaks.

## Quick check

Each of these short proofs has a flaw. Find it before you open the answers. If you find all three, skip to [Practice](#practice).

1. Claim: for every integer $n \ge 0$, the number $4^n + 1$ is divisible by 3. Proof: suppose $4^k + 1 = 3m$ for some integer $m$. Then $4^{k+1} + 1 = 4(4^k + 1) - 3 = 12m - 3 = 3(4m - 1)$, which is divisible by 3. By induction, the claim holds for every $n \ge 0$.
2. Claim: the function $f \colon \mathbb{R} \to \mathbb{R}$ given by $f(x) = x^2$ is injective. Proof: suppose $a = a'$. Then $a^2 = a'^2$, so $f(a) = f(a')$. Hence $f$ is injective.
3. Claim: for every integer $n$, the number $n^2 + n$ is even. Proof: clearly $n(n + 1)$ is even.

<details class="solution" markdown>
<summary>Answers</summary>

1. There is no base case. The step is valid, but nothing starts the chain: for $n = 0$ the number $4^0 + 1 = 2$ is not divisible by 3, and in fact $4^n + 1$ leaves remainder 2 for every $n$. The claim is false.
2. The proof starts from the wrong equation. "$a = a'$ implies $f(a) = f(a')$" is true for every function, so it proves nothing about injectivity. Injectivity needs the reverse: suppose $f(a) = f(a')$ and show $a = a'$. Here that fails, since $f(-2) = f(2) = 4$, so the claim is false.
3. The word "clearly" hides the reason. The reason is that $n$ and $n + 1$ are consecutive integers, so one of them is even, and a product with an even factor is even. A reader should not have to supply it.

</details>

## The idea

A grader reads dozens of proofs of the same statement, and the mistakes repeat. Most wrong proofs fail in one of a small number of ways, and most of those ways are the ones this folder has already named: a converse proved in place of the claim, a case left out, a base case forgotten. Once you can name the mistake, you can both avoid it in your own work and find it in a classmate's.

You already do this with code. A failing test has a handful of usual causes (off-by-one, a null, a mutated argument), and an experienced programmer checks those first. A proof has the same kind of checklist. This lesson is that checklist, with an example of each mistake and its repair. The mistakes are grouped by where they happen: in the logic, in the method, in induction, in sets and functions, and in the writing.

## Definitions

A **flawed proof** is an argument written as a proof that a careful reader would not accept. There are three kinds of trouble, and the repair depends on which one you have.

- The claim is false. No proof can be repaired, and the fix is a counterexample (see [counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md)).
- A step is invalid. The step does not follow from the lines before it, for example because it proves the converse or divides by zero. The fix is a different step.
- The proof has a **gap**, a step that is true but unjustified, or a case that is missing. The fix is to supply it.

In plain words: first ask whether the claim is true, then whether each step follows, then whether anything is missing. A flawed proof of a true claim is common, and a flawed proof of a false claim is the sign that the claim needs testing before anyone argues about the proof.

## How to do it

Use this order to check any proof, yours or someone else's. It is the reading routine from [how to read a proof](../03-core-proof-methods/02-how-to-read-a-proof.md), tuned for finding flaws.

1. Test the claim on a small case and an awkward case ($0$, a negative number, equal values, the empty set). If it fails, stop: the claim is false.
2. Read the first line. Does it assume exactly the hypothesis, and introduce each letter with its type?
3. Read the last line. Is it exactly the claim, in the right direction?
4. Check each line for a reason. A line with no reason, or with "clearly", is a place to look.
5. Check the logic of each step: the direction of each implication, each negation, each division, and the order of quantifiers.
6. Check coverage. Do the cases cover everything? Is there a base case? Are both inclusions proved?
7. Find where each hypothesis is used. A hypothesis that is never used usually means the proof proves something else.
8. Run the proof on one concrete example, including a bad one. If the proof "works" on an example where the claim fails, the proof is wrong.

The catalogue below is organised by the step that fails.

## The catalogue

### Mistakes in the logic

#### Proving the converse

> Claim: if $n^2$ is divisible by 4, then $n$ is even. Proof: let $n$ be even, so $n = 2k$. Then $n^2 = 4k^2$, which is divisible by 4.

The proof assumes "$n$ is even" and derives "$4 \mid n^2$". That is the converse of the claim. The claim assumes "$4 \mid n^2$" and must derive "$n$ is even", and the two directions are not equivalent in general (see [conditionals and biconditionals](../02-logic-and-sets/02-conditionals-and-biconditionals.md)). Here the converse happens to be true as well, which hides the error.

Repair: prove the contrapositive. Suppose $n$ is odd, $n = 2k + 1$. Then $n^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1$, which leaves remainder 1 when divided by 4, so $4 \nmid n^2$. Taught in [contrapositive proof](../03-core-proof-methods/05-contrapositive-proof.md).

#### Assuming the conclusion

> Claim: if $n^2$ is odd, then $n$ is odd. Proof: since $n^2$ is odd, $n$ is odd, because the square root of an odd number is odd.

The reason given for the last step is the claim itself, so the argument is circular. A proof may use earlier results, and "the square root of an odd number is odd" is a result that has not been proved yet.

Repair: prove it from the definitions. Suppose $n$ is even, $n = 2k$. Then $n^2 = 2(2k^2)$ is even, so by the contrapositive, an odd $n^2$ forces an odd $n$. Taught in [direct proof](../03-core-proof-methods/01-direct-proof.md) (starting at the conclusion) and [how to write a proof](../03-core-proof-methods/07-how-to-write-a-proof.md) (circular reasoning).

#### A wrong negation

> Claim: if $ab$ is even, then $a$ is even or $b$ is even. Proof by contrapositive: suppose $a$ is odd or $b$ is odd. Then $ab$ is odd.

The negation of "$a$ is even or $b$ is even" is "$a$ is odd and $b$ is odd", by De Morgan's law. The proof negated "or" as "or", and its "contrapositive" is false: $a = 3$ and $b = 2$ give an even product.

Repair: suppose $a$ and $b$ are both odd, $a = 2j + 1$ and $b = 2k + 1$. Then $ab = 4jk + 2j + 2k + 1 = 2(2jk + j + k) + 1$ is odd. Taught in [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md).

#### Swapping the order of quantifiers

> Claim: there is a natural number $N$ such that $n \le N$ for every natural number $n$. Proof: let $n$ be a natural number. Take $N = n + 1$. Then $n \le N$.

The statement says "there exists $N$, for every $n$": one $N$ must work for all $n$. The proof picked $N$ after $n$, so $N$ depends on $n$, and it proved "for every $n$ there exists $N$", which is a different statement. The claim itself is false, since $N + 1$ is bigger than any proposed $N$.

Repair: the true statement is "for every natural number $n$ there is a natural number $N$ with $n \le N$", and the proof above is correct for it. Taught in [quantifiers](../02-logic-and-sets/04-quantifiers.md).

### Mistakes in the method

#### Examples as a proof of a universal claim

> Claim: for every real number $x$, $x^2 \ge x$. Proof: $x = 2$ gives $4 \ge 2$, $x = 5$ gives $25 \ge 5$, and $x = -3$ gives $9 \ge -3$.

Examples can make a "for every" claim believable, but they can never prove it. They can only disprove it. The claim is false: $x = \frac{1}{2}$ gives $\frac{1}{4} < \frac{1}{2}$.

Repair: change the claim to one that is true, such as "for every integer $n$, $n^2 \ge n$", and prove it for an arbitrary $n$. If $n \ge 1$, then $n > 0$ and $n - 1 \ge 0$, so $n(n - 1) \ge 0$. If $n \le 0$, then $n - 1 < 0$ as well, so again $n(n - 1) \ge 0$. In both cases $n^2 - n \ge 0$. Taught in [what is a proof](../01-language-and-notation/01-what-is-a-proof.md) and [counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md).

#### WLOG without a symmetry

> Claim: if $ab$ is even, then $a$ is even. Proof: since $ab$ is even, one of $a$ and $b$ is even. Without loss of generality it is $a$.

"Without loss of generality" is allowed only when swapping the names gives the same claim. This claim treats $a$ and $b$ differently, so the swap changes it, and the case that was dropped ($a$ odd, $b$ even) is exactly where the claim fails: $a = 3$, $b = 2$.

Repair: state the symmetric claim that is true, "if $ab$ is even, then $a$ is even or $b$ is even", and prove it as in the wrong-negation entry. Taught in [proof language: let, suppose, WLOG](../01-language-and-notation/03-proof-language-let-suppose-wlog.md) and [proof by cases and WLOG](../03-core-proof-methods/04-proof-by-cases-and-wlog.md).

#### A case that is missing

> Claim: for every integer $n$, the remainder of $n^2$ on division by 3 is 0 or 1. Proof: if $n = 3k$, then $n^2 = 9k^2$ has remainder 0. If $n = 3k + 1$, then $n^2 = 9k^2 + 6k + 1$ has remainder 1.

An integer can also be $3k + 2$. The proof covers two of the three possible remainders and says nothing about the third.

Repair: add the case. If $n = 3k + 2$, then $n^2 = 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1$, which has remainder 1. State at the start why three cases are enough: every integer has remainder 0, 1 or 2 when divided by 3. Taught in [proof by cases and WLOG](../03-core-proof-methods/04-proof-by-cases-and-wlog.md).

#### Contradiction with no contradiction

> Claim: there are infinitely many primes. Proof: suppose there are only finitely many, $p_1, \dots, p_n$. Let $N = p_1 p_2 \cdots p_n + 1$. Then $N$ is larger than every $p_i$, so $N$ is not on the list, and so $N$ is not prime. Contradiction.

The proof reaches "$N$ is not prime", and that is not a contradiction with anything. A number can be composite. For example, $2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \times 509$. A contradiction is a statement and its negation, both derived.

Repair: $N > 1$ has a prime divisor $q$. The prime $q$ is on the list, so $q \mid p_1 \cdots p_n$. Also $q \mid N$. Then $q \mid N - p_1 \cdots p_n = 1$, which is impossible for a prime. Taught in [proof by contradiction](../03-core-proof-methods/06-proof-by-contradiction.md).

### Mistakes in induction

#### No base case

> Claim: for every integer $n \ge 1$, $1 + 2 + \cdots + n = \frac{n(n+1)}{2} + 1$. Proof: suppose it holds for $k$. Then $1 + \cdots + k + (k + 1) = \frac{k(k+1)}{2} + 1 + (k + 1) = \frac{(k+1)(k+2)}{2} + 1$.

The step is correct algebra, and the claim is false: for $n = 1$ the left side is 1 and the right side is 2. A correct step plus a failed base case proves nothing, because the chain never starts.

Repair: there is nothing to repair in the claim except to drop the $+1$. For $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ the base case $1 = \frac{1 \cdot 2}{2}$ holds and the same step works. Always check the base case first; it is the quickest test of the claim. Taught in [mathematical induction](../05-induction/01-mathematical-induction.md).

#### A step that fails at the first few values

> Claim: every integer $n \ge 8$ is a sum of 3s and 5s. Proof by strong induction: base case $n = 8 = 3 + 5$. Step: for $n \ge 9$, the number $n - 3$ is a sum of 3s and 5s by the hypothesis, so $n = (n - 3) + 3$ is too.

For $n = 9$ the proof calls on $n - 3 = 6$, and for $n = 10$ on $7$. Both are below the starting value 8, so the hypothesis says nothing about them. The step cites cases outside the range it is allowed to assume, and the gap is real: $7$ is not a sum of 3s and 5s, yet the step for $n = 10$ leans on it.

Repair: use three base cases, $8 = 3 + 5$, $9 = 3 + 3 + 3$ and $10 = 5 + 5$. Then for $n \ge 11$ the number $n - 3 \ge 8$ is covered. Count base cases by finding the smallest $n$ where every cited case is at least the starting value. Taught in [strong induction and well-ordering](../05-induction/02-strong-induction-and-well-ordering.md).

#### Proving the step backward

> Claim: for every integer $n \ge 1$, $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$. Step: suppose the formula holds for $k + 1$: $\sum_{i=1}^{k+1} i = \frac{(k+1)(k+2)}{2}$. Subtract $k + 1$ from both sides. The left side becomes $\sum_{i=1}^{k} i$ and the right side becomes $\frac{k(k+1)}{2}$, which is the formula for $k$.

This shows "$P(k + 1)$ implies $P(k)$". Induction needs "$P(k)$ implies $P(k + 1)$". The proof assumes the statement it is supposed to reach.

Repair: start from $P(k)$ and add the new term. Suppose $\sum_{i=1}^{k} i = \frac{k(k+1)}{2}$. Then $\sum_{i=1}^{k+1} i = \frac{k(k+1)}{2} + (k + 1) = \frac{(k+1)(k+2)}{2}$. Taught in [mathematical induction](../05-induction/01-mathematical-induction.md).

### Mistakes with sets and functions

#### An element where a subset belongs

> Claim: if $A \in B$ and $B \subseteq C$, then $A \subseteq C$. Proof: every element of $A$ is in $B$, and $B \subseteq C$, so every element of $A$ is in $C$.

The hypothesis "$A \in B$" says that $A$ is one element of $B$. It does not say that the elements of $A$ are in $B$. A counterexample: $A = \{1\}$, $B = \{\{1\}\}$, $C = \{\{1\}, 2\}$. Here $A \in B$ and $B \subseteq C$, but $1 \notin C$, so $A \not\subseteq C$.

Repair: the true conclusion is "$A \in C$": since $A \in B$ and every element of $B$ is in $C$, we get $A \in C$. Taught in [sets and set operations](../02-logic-and-sets/06-sets-and-set-operations.md) and [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md).

#### One inclusion only

> Claim: if $A \subseteq B$, then $A \cap B = A$. Proof: let $x \in A \cap B$. Then $x \in A$ and $x \in B$, so $x \in A$.

This proves $A \cap B \subseteq A$. That inclusion is true for all sets, and the hypothesis $A \subseteq B$ was never used. A set equality needs two inclusions, and the unused hypothesis is the sign that one is missing.

Repair: add $A \subseteq A \cap B$. Let $x \in A$. Since $A \subseteq B$, also $x \in B$, so $x \in A \cap B$. Both inclusions together give $A \cap B = A$. Taught in [proofs about sets](../04-more-proof-methods/03-proofs-about-sets.md).

#### Injectivity started from equal inputs

> Claim: $f \colon \mathbb{R} \to \mathbb{R}$, $f(x) = 5x - 2$, is injective. Proof: suppose $a = a'$. Then $5a - 2 = 5a' - 2$, so $f(a) = f(a')$.

The proof goes from equal inputs to equal outputs, which holds for every function by the definition of a function. Injective means the reverse: equal outputs force equal inputs. The claim is true, but this argument does not show it. (The Quick check used $x^2$, where the same argument "proves" a false claim.)

Repair: suppose $f(a) = f(a')$. Then $5a - 2 = 5a' - 2$, so $5a = 5a'$, and dividing by $5$ gives $a = a'$. Taught in [injective, surjective and bijective](../06-relations-and-functions/05-injective-surjective-bijective.md).

#### A rule that is not a function

> Define $f \colon \mathbb{R} \to \mathbb{R}$ by $f(x) = x + 1$ if $x \ge 0$ and $f(x) = x - 1$ if $x \le 0$. Then $f$ is a function.

At $x = 0$ both rules apply, and they disagree: $f(0) = 1$ and $f(0) = -1$. A function must give exactly one output for each input.

Repair: make the cases disjoint, for example $x + 1$ for $x \ge 0$ and $x - 1$ for $x < 0$. Then every real number falls in exactly one case, and the rule is a function. Taught in [functions and well-definedness](../06-relations-and-functions/04-functions-and-well-definedness.md).

### Mistakes in the writing

#### A letter used before it is introduced

> Claim: the sum of an even integer and an odd integer is odd. Proof: since $n = 2k$ and $m = 2j + 1$, we get $n + m = 2(k + j) + 1$, which is odd.

The proof never says what $n$, $m$, $k$ and $j$ are. A reader cannot tell whether $n$ is a given even integer or a particular one, or whether $k$ is an integer.

Repair: "Let $n$ be an even integer and $m$ an odd integer. Then $n = 2k$ for some integer $k$ and $m = 2j + 1$ for some integer $j$. So $n + m = 2(k + j) + 1$, and $k + j$ is an integer, so $n + m$ is odd." Every letter now has an origin and a type. Taught in [proof language: let, suppose, WLOG](../01-language-and-notation/03-proof-language-let-suppose-wlog.md).

#### Symbol soup

> Proof: $n$ even $\Rightarrow$ $n = 2k$ $\Rightarrow$ $n^2 = 4k^2$ $\Rightarrow$ $2(2k^2)$ $\Rightarrow$ even.

An arrow connects two statements. Here it joins an equation to a bare expression, "$2(2k^2)$", which is not a statement at all. The chain never says what is being proved, and each arrow could mean "implies", "therefore" or "becomes".

Repair: use sentences. "Let $n$ be even, so $n = 2k$ for an integer $k$. Then $n^2 = 4k^2 = 2(2k^2)$, and $2k^2$ is an integer, so $n^2$ is even." Test any proof with the "blah" test: replace each formula by "blah" and read it aloud. Taught in [how to write a proof](../03-core-proof-methods/07-how-to-write-a-proof.md) and [reading math symbols](../01-language-and-notation/04-reading-math-symbols.md).

#### "Clearly" and other unjustified steps

> Claim: for every integer $n$, $n^3 - n$ is divisible by 6. Proof: $n^3 - n = (n - 1)n(n + 1)$, and clearly this is divisible by 6.

The factoring is right. "Clearly" replaces the whole argument: why is a product of three consecutive integers divisible by 6? In a textbook the word means the author skipped a routine step, and in a graded proof it means the grader will not give credit for it.

Repair: say why. Among three consecutive integers one is even, so the product is even. Among them one is also a multiple of 3 (one of $n - 1$, $n$, $n + 1$ has remainder 0 when divided by 3). So the product is divisible by 2 and by 3. Since $\gcd(2, 3) = 1$, it is divisible by 6 ([scratch work and proof strategies](../03-core-proof-methods/03-scratch-work-and-proof-strategies.md#worked-examples) writes this out in full, including the combining step). Taught in [how to read a proof](../03-core-proof-methods/02-how-to-read-a-proof.md).

#### Dividing by something that might be zero

> Claim: if $ab = ac$, then $b = c$. Proof: divide both sides by $a$.

If $a = 0$, then $ab = ac$ is true for every $b$ and $c$, and the conclusion fails: $0 \cdot 1 = 0 \cdot 2$ but $1 \ne 2$. Dividing by an expression that can be 0 also loses solutions: it turns $x^2 = x$ into $x = 1$ and drops $x = 0$.

Repair: add the hypothesis the argument needs, "if $ab = ac$ and $a \ne 0$, then $b = c$", and say where it is used. Or keep the claim general and factor: $a(b - c) = 0$, so $a = 0$ or $b = c$. Taught in [if and only if proofs](../04-more-proof-methods/01-if-and-only-if-proofs.md) (reversible steps).

## Worked examples

<div class="example" markdown>

### Example 1: a proof written the wrong way round

Claim: for every real number $x > 0$, $x + \frac{1}{x} \ge 2$.

A flawed proof: "Suppose $x + \frac{1}{x} \ge 2$. Multiply by $x$: $x^2 + 1 \ge 2x$. Then $x^2 - 2x + 1 \ge 0$, which is $(x - 1)^2 \ge 0$. This is true, so the claim holds."

Step 1 of the checking routine: the claim is true (try $x = 1$: $2 \ge 2$; $x = 3$: $3.33 \ge 2$). Steps 2 and 3: the proof begins with the conclusion as an assumption and ends with a true statement. The logic runs from the claim to "$(x-1)^2 \ge 0$", and what the proof needs is the opposite direction. That is the mistake of assuming the conclusion. From a true statement you can reach the claim only if each step can be reversed.

In this case every step can be reversed, because we multiplied by $x > 0$ and rearranged. That is why the flawed proof is repairable, and why a "backward proof" is sometimes acceptable if it says so. A better habit is to write it forward.

What we know: $x > 0$, and a square is never negative. What we want: $x + \frac{1}{x} \ge 2$. The plan: start from $(x - 1)^2 \ge 0$ and divide by $x$.

*Proof.* Let $x > 0$. A square is at least 0, so $(x - 1)^2 \ge 0$, that is, $x^2 - 2x + 1 \ge 0$. Dividing by $x$, which is positive, keeps the direction of the inequality and gives $x - 2 + \frac{1}{x} \ge 0$. Adding 2 to both sides gives $x + \frac{1}{x} \ge 2$. $\blacksquare$

Look back: the hypothesis $x > 0$ is used once, in the division. Without it the claim fails ($x = -1$ gives $-2$). Check: $x = 4$ gives $4.25 \ge 2$.

</div>

<div class="example" markdown>

### Example 2: a missing case

Claim: for every real number $x$, $\lvert x - 1 \rvert + \lvert x - 2 \rvert \ge 1$.

A flawed proof: "Case 1: $x < 1$. Then both $x - 1$ and $x - 2$ are negative, so the sum is $(1 - x) + (2 - x) = 3 - 2x > 1$. Case 2: $x > 2$. Then both are positive, so the sum is $(x - 1) + (x - 2) = 2x - 3 > 1$. In both cases the sum is more than 1, so the claim holds."

Two things are wrong. The cases $x < 1$ and $x > 2$ leave out every $x$ with $1 \le x \le 2$, and that is the interesting range, because the expression takes its smallest value there. The proof also shows "more than 1", which suggests that the claim is never tight. Running the proof on an example catches it: at $x = 1.5$ the sum is $0.5 + 0.5 = 1$, which neither case covers.

Repair: split the real line into three pieces that cover everything, and use $\le$ so that the boundaries are included.

*Proof.* Let $x$ be a real number. Every real number satisfies exactly one of $x < 1$, $1 \le x \le 2$ and $x > 2$.

If $x < 1$, then $x - 1 < 0$ and $x - 2 < 0$, so the sum is $(1 - x) + (2 - x) = 3 - 2x$. Since $x < 1$, we have $3 - 2x > 1$.

If $1 \le x \le 2$, then $x - 1 \ge 0$ and $x - 2 \le 0$, so the sum is $(x - 1) + (2 - x) = 1$.

If $x > 2$, then both terms are positive and the sum is $(x - 1) + (x - 2) = 2x - 3 > 1$.

In every case the sum is at least 1. $\blacksquare$

Check: $x = 0$ gives $1 + 2 = 3$, $x = 1.5$ gives $1$, and $x = 4$ gives $3 + 2 = 5$. The value 1 is reached on the whole middle interval.

</div>

<div class="example" markdown>

### Example 3: a step that does not work for small values

Claim: $n^2 < 2^n$ for every integer $n \ge 1$.

A flawed proof: "Base case: $1^2 = 1 < 2 = 2^1$. Step: suppose $k^2 < 2^k$. Then $(k + 1)^2 = k^2 + 2k + 1 < 2^k + 2k + 1 \le 2^k + 2^k = 2^{k+1}$, using $2k + 1 \le 2^k$."

The last inequality, $2k + 1 \le 2^k$, is stated without proof, and it is false for small $k$: at $k = 1$ it says $3 \le 2$, and at $k = 2$ it says $5 \le 4$. It first holds at $k = 3$, where $7 \le 8$. So the step fails for $k = 1$ and $k = 2$. The claim is false too: $n = 2$ gives $4 < 4$, $n = 3$ gives $9 < 8$ and $n = 4$ gives $16 < 16$, all false.

Repair: restart the claim where the step works, at $n = 5$, and prove the inequality that the step needs.

Claim: $n^2 < 2^n$ for every integer $n \ge 5$.

What we know: $5^2 = 25 < 32 = 2^5$. For the step we need a bound for $2k + 1$ that holds from $k = 5$ on. What we want: $(k+1)^2 < 2^{k+1}$. The plan: bound $2k + 1$ by $k^2$, then use the hypothesis twice.

*Proof.* By induction on $n$.

Base case, $n = 5$: $25 < 32$.

Inductive step. Let $k \ge 5$ and suppose $k^2 < 2^k$. For $k \ge 3$ we have $k^2 - 2k - 1 = k(k - 2) - 1 \ge 3 - 1 > 0$, so $2k + 1 \le k^2$. Then

$$
(k + 1)^2 = k^2 + (2k + 1) \le k^2 + k^2 = 2k^2 < 2 \cdot 2^k = 2^{k+1},
$$

where the last inequality is the hypothesis. By induction, the claim holds for every $n \ge 5$. $\blacksquare$

Look back: the proof now says where $k \ge 3$ is used, and the base case matches the start of the claim. Check: $n = 6$ gives $36 < 64$ and $n = 10$ gives $100 < 1024$.

</div>

<div class="example" markdown>

### Example 4: a function that is not well defined (finish it yourself)

Claim: there is a function $f \colon \mathbb{Z}_4 \to \mathbb{Z}_6$ given by $f([a]_4) = [a]_6$. Here $[a]_n$ is the class of $a$ modulo $n$.

A flawed proof: "Every element of $\mathbb{Z}_4$ has the form $[a]_4$ for some integer $a$, and $[a]_6$ is a class in $\mathbb{Z}_6$. So the rule assigns an output to each input, and $f$ is a function."

The rule is written using a representative $a$ of the class. The same class has many representatives, and a function must give one output however the input is named. Test with two names for one class: $[1]_4 = [5]_4$, because $4 \mid 5 - 1$. The rule gives $[1]_6$ from the name $1$ and $[5]_6$ from the name $5$, and $[1]_6 \ne [5]_6$, since $6 \nmid 4$. So the rule is not a function. Compare the rule $[a]_6 \mapsto [a]_3$, which is well defined because $6 \mid a - a'$ gives $3 \mid a - a'$ (see [functions and well-definedness](../06-relations-and-functions/04-functions-and-well-definedness.md)).

Now write the repaired statement and its proof: show that $g \colon \mathbb{Z}_{12} \to \mathbb{Z}_4$ given by $g([a]_{12}) = [a]_4$ is well defined.

<details class="solution" markdown>
<summary>Finish</summary>

*Proof.* Suppose $[a]_{12} = [a']_{12}$. Then $12 \mid a' - a$, so $a' - a = 12j$ for some integer $j$. Then $a' - a = 4(3j)$ with $3j$ an integer, so $4 \mid a' - a$ and $[a']_4 = [a]_4$. The output does not depend on the representative, so $g$ is well defined. $\blacksquare$

The general rule is that $[a]_m \mapsto [a]_n$ is well defined exactly when $n \mid m$. The proof above is the "if" half. For the "only if" half, $[0]_m = [m]_m$ forces $[0]_n = [m]_n$, that is, $n \mid m$, which is the test that failed for $m = 4$ and $n = 6$.

Check: $[5]_{12} = [17]_{12}$, and $g$ gives $[5]_4 = [1]_4$ and $[17]_4 = [1]_4$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for "fixing" a proof of a false claim. If step 1 of the routine shows the claim fails, every repair of the argument will fail too. Change the claim (add a hypothesis, weaken the conclusion) or disprove it, as in Example 3.

</div>

<div class="warning" markdown>

Watch out for a flaw that is also a true statement. In the entry on proving the converse, the converse was true, which is why the flawed proof looks fine. A proof is judged on the implication it proves, not on whether its last line is true.

</div>

<div class="warning" markdown>

Watch out for correcting the wrong thing. When a step is wrong, the fix is a new step or a new hypothesis, not a reworded old step. Replacing "clearly" with "obviously", or "therefore" with an arrow, leaves the gap where it was.

</div>

## Tricks and shortcuts

Run your own proof on a bad example. Pick an input that is awkward for the claim (zero, a negative number, equal values, the empty set, a one-element set, $a$ with $a \mid b$ and $b \mid a$) and follow your lines on it. A step that breaks on the example is the flawed one.

Check the unused hypothesis. List the hypotheses and tick off where each is used. A proof that never uses one has either proved a stronger claim (rare, and worth a second look) or skipped a step (usual). In "one inclusion only" the unused hypothesis $A \subseteq B$ pointed straight at the missing half.

Read the quantifiers aloud in order. "There exists $N$ such that for every $n$" and "for every $n$ there exists $N$" differ by a swap, and saying them left to right makes the dependence audible.

## In code

A short search finds a counterexample to a false claim in seconds and finds none for a true one. The script tests the claims from this lesson over a small range. It supports nothing as a proof, and it quickly kills the false ones.

<details class="code" markdown>
<summary>In code</summary>

```python
def first_failure(claim, values):
    """Return the first value where the claim fails, or None."""
    for v in values:
        if not claim(v):
            return v
    return None

print(first_failure(lambda n: (4**n + 1) % 3 == 0, range(10)))        # 0
print(first_failure(lambda x: x * x >= x, [i / 2 for i in range(-10, 11)]))  # 0.5
print(first_failure(lambda n: n * n < 2**n, range(1, 20)))            # 2
print(first_failure(lambda n: n * n < 2**n, range(5, 200)))           # None
print(first_failure(lambda n: (n**3 - n) % 6 == 0, range(-100, 100))) # None
```

The first three claims fail at once, at $n = 0$, $x = 0.5$ and $n = 2$. The last two print `None`: they supply evidence and no proof.

</details>

## FAQ

### How do I know whether my own proof has one of these mistakes?

Use the routine in "How to do it", and in particular steps 1 and 8, which test the claim and the proof on examples. Most of the mistakes above show up the moment you substitute a concrete bad input. The rest (circular reasoning, symbol soup) show up when you read the proof aloud to someone who does not know the answer.

### If the claim is true and I made one small flawed step, is the proof nearly right?

A grader may give partial credit for the idea, but the step is still marked wrong. A proof is a chain, and a chain with one broken link does not hold. Fix the link, and then reread the line after it, because the fix often changes what comes next.

### Why does a correct but unneeded detail count as a flaw?

It usually doesn't. Extra true detail costs readability and nothing else. What counts as a flaw is a missing reason, a wrong direction or a missing case, because those make the proof unacceptable to a careful reader.

## Practice

### Warm-up

1\. Find and fix the flaw. Claim: the sum of two odd integers is even. Proof: let $m$ and $n$ be odd. Then $m = 2k + 1$ and $n = 2k + 1$, so $m + n = 4k + 2 = 2(2k + 1)$, which is even.

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is that one letter, $k$, is used for two different integers. Writing $m = 2k + 1$ and $n = 2k + 1$ forces $m = n$, so the proof covers only equal pairs. It does not cover $m = 3$, $n = 5$.

Fixed proof. Let $m$ and $n$ be odd integers. Then $m = 2j + 1$ and $n = 2k + 1$ for integers $j$ and $k$. So $m + n = 2j + 2k + 2 = 2(j + k + 1)$, and $j + k + 1$ is an integer, so $m + n$ is even. $\blacksquare$

Check: $m = 3$ ($j = 1$) and $n = 5$ ($k = 2$) give $8 = 2(1 + 2 + 1)$.

</details>

2\. Find and fix the flaw. Claim: for every positive integer $n$, the number $n^2 - n + 11$ is prime. Proof: for $n = 1, 2, \dots, 10$ the values are $11, 13, 17, 23, 31, 41, 53, 67, 83, 101$, and all are prime. So the claim holds.

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is that ten examples are offered as a proof of a "for every" claim. The claim is false: $n = 11$ gives $121 - 11 + 11 = 121 = 11^2$, which is not prime.

Fixed version: the statement "$n^2 - n + 11$ is prime for $n = 1, \dots, 10$" is true and is proved by the ten checks. For all $n$ the correct answer is the counterexample $n = 11$.

Check: $11 \cdot 11 = 121$.

</details>

3\. Find and fix the flaw. Claim: if $A \subseteq B$, then $\mathcal{P}(A) \subseteq \mathcal{P}(B)$. Proof: let $x \in \mathcal{P}(A)$. Then $x \in A$. Since $A \subseteq B$, $x \in B$, so $x \in \mathcal{P}(B)$.

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is the second sentence. The elements of $\mathcal{P}(A)$ are subsets of $A$, so "$x \in \mathcal{P}(A)$" means $x \subseteq A$, not $x \in A$. The proof mixes up an element and a subset.

Fixed proof. Let $x \in \mathcal{P}(A)$. Then $x \subseteq A$. Since $A \subseteq B$, every element of $x$ is in $A$ and hence in $B$, so $x \subseteq B$. Therefore $x \in \mathcal{P}(B)$. $\blacksquare$

Check: $A = \{1\}$, $B = \{1, 2\}$. Then $\mathcal{P}(A) = \{\emptyset, \{1\}\}$, and both are subsets of $B$, so both are in $\mathcal{P}(B)$.

</details>

### Standard

4\. Find and fix the flaw. Claim: $A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C)$ for all sets $A$, $B$, $C$. Proof: let $x \in A \setminus (B \cap C)$. Then $x \in A$ and $x \notin B \cap C$, so $x \notin B$ or $x \notin C$. So $x \in A \setminus B$ or $x \in A \setminus C$, which means $x \in (A \setminus B) \cup (A \setminus C)$.

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is that only one inclusion is proved, $\subseteq$. Equality needs the other one too.

Fixed proof, second half. Let $x \in (A \setminus B) \cup (A \setminus C)$. Then $x \in A \setminus B$ or $x \in A \setminus C$. In both cases $x \in A$. In the first case $x \notin B$, in the second $x \notin C$, so in either case $x \notin B \cap C$ (a member of $B \cap C$ would be in both $B$ and $C$). So $x \in A \setminus (B \cap C)$. Together with the first half, the sets are equal. $\blacksquare$

Check: $A = \{1, 2, 3\}$, $B = \{1, 2\}$, $C = \{2, 3\}$. Then $B \cap C = \{2\}$ and the left side is $\{1, 3\}$. The right side is $\{3\} \cup \{1\} = \{1, 3\}$.

</details>

5\. Find and fix the flaw. Claim: the equation $x^2 = 3x$ has exactly one real solution, $x = 3$. Proof: divide both sides by $x$ to get $x = 3$. Check: $3^2 = 9 = 3 \cdot 3$.

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is dividing by $x$ when $x$ might be 0. The division is reversible only for $x \ne 0$, so it loses the solution $x = 0$, and the claim "exactly one solution" is false.

Fixed proof of the correct claim. The equation is equivalent to $x^2 - 3x = 0$, that is, $x(x - 3) = 0$. A product of two real numbers is 0 only if one of them is 0, so $x = 0$ or $x = 3$. Both satisfy the equation, so the solutions are exactly $0$ and $3$. $\blacksquare$

Check: $0^2 = 0 = 3 \cdot 0$ and $3^2 = 9 = 3 \cdot 3$.

</details>

6\. (Reviews [sequences and recursion](../../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md).) Find and fix the flaw. Define $a_0 = 2$, $a_1 = 3$ and $a_n = 3a_{n-1} - 2a_{n-2}$ for $n \ge 2$. Claim: $a_n = 2^n + 1$ for every $n \ge 0$. Proof: base case $a_0 = 2 = 2^0 + 1$. Step: suppose $a_k = 2^k + 1$ and $a_{k-1} = 2^{k-1} + 1$. Then $a_{k+1} = 3(2^k + 1) - 2(2^{k-1} + 1) = 2^{k+1} + 1$.

<details class="solution" markdown>
<summary>Solution</summary>

The step uses two earlier cases, $k$ and $k - 1$, and the proof has one base case. For $k = 0$ the step needs $a_{-1}$, which does not exist, so the proof never reaches $a_1$, and everything after it hangs on $a_1$. The claim is true, and the proof has a gap.

Fixed proof. Strong induction with two base cases. Base cases: $a_0 = 2 = 2^0 + 1$ and $a_1 = 3 = 2^1 + 1$. Step: let $k \ge 1$ and suppose the formula holds for $k$ and $k - 1$ (both are at least 0). Then

$$
a_{k+1} = 3(2^k + 1) - 2(2^{k-1} + 1) = 3 \cdot 2^k - 2^k + 3 - 2 = 2 \cdot 2^k + 1 = 2^{k+1} + 1.
$$

By induction the formula holds for every $n \ge 0$. $\blacksquare$

Check: $a_2 = 3 \cdot 3 - 2 \cdot 2 = 5 = 2^2 + 1$ and $a_3 = 3 \cdot 5 - 2 \cdot 3 = 9 = 2^3 + 1$.

</details>

### Challenge

7\. Find and fix the flaw. Claim: for integers $a$ and $b$, if $a^2 + b^2$ is odd, then $a$ is odd. Proof: the parity of $a^2 + b^2$ is odd, so exactly one of $a^2$ and $b^2$ is odd, and a square has the same parity as its root, so exactly one of $a$ and $b$ is odd. Without loss of generality, it is $a$.

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is the use of "without loss of generality". The claim is not symmetric: it says $a$ is odd, not "one of them is odd". Swapping $a$ and $b$ gives "if $a^2 + b^2$ is odd then $b$ is odd", a different claim. In fact the claim is false: $a = 2$, $b = 1$ give $a^2 + b^2 = 5$, which is odd, while $a$ is even.

Fixed claim: $a^2 + b^2$ is odd exactly when one of $a$ and $b$ is odd and the other is even. The symmetric statement is where WLOG is allowed.

*Proof.* A square has the same parity as its root: if $n = 2k$, then $n^2 = 2(2k^2)$ is even; if $n = 2k + 1$, then $n^2 = 2(2k^2 + 2k) + 1$ is odd. So $a^2 + b^2$ has the parity of $a + b$. A sum of two integers is odd exactly when they have different parities. So $a^2 + b^2$ is odd exactly when one of $a$ and $b$ is odd and the other is even. $\blacksquare$

This claim does not change when $a$ and $b$ are swapped, so a proof that handled the case "$a$ odd, $b$ even" could cover "$a$ even, $b$ odd" by WLOG.

Check: $(a, b) = (2, 1)$ gives $5$, odd, with $a$ even and $b$ odd, and $(3, 3)$ gives $18$, even, with both odd.

</details>

8\. Find and fix the flaw. Claim: $\sqrt{3}$ is irrational. Proof: suppose $\sqrt{3} = \frac{a}{b}$ for integers $a$ and $b \ne 0$. Then $a^2 = 3b^2$, so $3 \mid a^2$, so $3 \mid a$. Write $a = 3c$. Then $9c^2 = 3b^2$, so $b^2 = 3c^2$, and $3 \mid b$. So $3$ divides both $a$ and $b$. Contradiction.

<details class="solution" markdown>
<summary>Solution</summary>

Two flaws. First, "3 divides both $a$ and $b$" is not a contradiction unless $\frac{a}{b}$ was in lowest terms, and the proof never assumed that. Second, "$3 \mid a^2$, so $3 \mid a$" is used without a reason, and it needs one: the same move is false for a composite divisor ($4 \mid 2^2$ and $4 \nmid 2$).

Fixed proof. Lemma: if $3 \mid n^2$, then $3 \mid n$. By the contrapositive: if $3 \nmid n$, then $n = 3q + 1$ or $n = 3q + 2$, so $n^2 = 3(3q^2 + 2q) + 1$ or $n^2 = 3(3q^2 + 4q + 1) + 1$, and in both cases $3 \nmid n^2$.

Now suppose, for contradiction, that $\sqrt{3}$ is rational. Then $\sqrt{3} = \frac{a}{b}$ with integers $a$, $b \ne 0$ in lowest terms, that is, $\gcd(a, b) = 1$. Then $a^2 = 3b^2$, so $3 \mid a^2$, so $3 \mid a$ by the lemma. Write $a = 3c$. Then $9c^2 = 3b^2$, so $b^2 = 3c^2$, and by the lemma $3 \mid b$. So $3 \mid \gcd(a, b) = 1$, which is false. This contradicts lowest terms, so $\sqrt{3}$ is irrational. $\blacksquare$

Check: the lemma on $n = 4$ gives $16 = 3 \cdot 5 + 1$, and on $n = 5$ gives $25 = 3 \cdot 8 + 1$.

</details>

## Where this shows up

- The next lesson, [mixed proof practice](02-mixed-proof-practice.md), asks you to choose a method yourself, and the mistakes above are the ones to check for in your own answers.
- In discrete math and in algorithms courses, graders check for the same things: the base case of an induction, the cases of a case analysis, the direction of an implication.
- In the theory of computation, the same mistakes appear in pumping-lemma proofs ([regular expressions and the pumping lemma](../../06-cs-math/06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md)), where the quantifier order is the usual trap, and in reduction proofs ([reductions and undecidability](../../06-cs-math/06-theory-of-computation/06-reductions-and-undecidability.md)), where reducing in the wrong direction is the usual one.
