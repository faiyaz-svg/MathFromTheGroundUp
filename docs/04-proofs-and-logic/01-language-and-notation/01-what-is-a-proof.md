# What is a proof

After this lesson you can say what counts as a proof and what doesn't, explain why a list of examples never proves a claim about every case, and read and write a short complete proof such as "the sum of two even integers is even".

Before this: [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md) (conditionals, converses, counterexamples and the two-column layout), [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) (proving facts from axioms) and [how to read math](../../00-start-here/how-to-read-math.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A friend says "the sum of two odd integers is always even" and offers $3 + 5 = 8$, $7 + 9 = 16$ and $11 + 13 = 24$ as the proof. Is that a proof? Why or why not?
2. An integer $n$ is even when $n = 2k$ for some integer $k$. Use this to explain why $n + 2$ is even whenever $n$ is even.
3. Someone claims "for every integer $n$, $n^2 > n$" because it holds for $n = 2, 3, 4, 5$. Find an integer where it fails.

<details class="solution" markdown>
<summary>Answers</summary>

1. No. Three true cases say nothing about the infinitely many other pairs. The claim happens to be true, but the examples don't show it.
2. If $n = 2k$, then $n + 2 = 2k + 2 = 2(k + 1)$, and $k + 1$ is an integer, so $n + 2$ is twice an integer.
3. Take $n = 1$: then $n^2 = 1$ is not greater than $n = 1$. Also $n = 0$ fails, since $0 > 0$ is false.

</details>

## The idea

Suppose you review a teammate's pull request. The function claims to return its input list in sorted order, and your teammate says "I ran it on a thousand random lists and it worked every time." Would you merge it with confidence? Probably not entirely. A thousand lists is a tiny part of all possible inputs, and bugs live in the special cases: the empty list, a list with repeats, a list that is already sorted. What you want instead is an argument that covers every input at once, a reason the code works that doesn't depend on which list you happen to try.

A proof is that kind of argument, for a mathematical claim. It doesn't sample the cases; it explains why no case can go wrong. The next two examples show how far apart those two things can be.

Look at the expression $n^2 + n + 41$. For $n = 0, 1, 2, \dots, 39$ it gives a prime number every time: 41, 43, 47, 53, and so on, forty values in a row (the computer check in the [In code](#in-code) section confirms it). It is natural to guess that the expression always gives a prime. But for $n = 40$ it gives $40^2 + 40 + 41 = 1681 = 41^2$, which is not prime. Forty successes were followed by a failure, and no amount of checking small values would have warned you.

Here is a second pattern. Put $n$ points on a circle and join every pair with a straight line. The lines cut the circle's inside into regions. For $n = 1, 2, 3, 4, 5$ the number of regions is $1, 2, 4, 8, 16$, and the next number looks like 32. For $n = 6$ the count is 31. The formula that gives the correct counts is $\binom{n}{4} + \binom{n}{2} + 1$, and it produces $1, 2, 4, 8, 16, 31, 57$. The doubling pattern held for five cases and then stopped.

Patterns are how mathematics gets started, and they are worth looking for. They are not how it gets finished. A statement of the form "for every ..." can fail in a case you didn't test, so the only way to be sure is an argument about all the cases together.

### Proofs in computer science and economics

You will meet proofs in your CS courses first. The correctness of an algorithm is a claim about every input, so testing can only support it. A typical argument uses an invariant, a fact that is true before the loop starts and stays true after each pass. For a loop that adds up a list:

```python
total = 0
for x in xs:
    total += x
```

the invariant is "before each pass, `total` equals the sum of the entries already visited". It holds before the first pass, because nothing has been visited and the sum of nothing is 0. If it holds before a pass, adding the next entry keeps it true for the next pass. When the loop ends, every entry has been visited, so `total` is the sum of the whole list. That is a proof, written in three sentences, and it works for a list of any length. Invariants and algorithm correctness<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md --> develops the idea, and proving that a reduction works, in the theory of computation, is the same skill with a different claim.

Economics uses proofs to derive a result from assumptions. A model says "suppose demand is linear and the seller sets one price", and the theorem says "then revenue is largest at this price". The proof shows exactly which assumptions the conclusion needs. If a real market breaks an assumption, you know which part of the result to stop trusting. Example 3 below proves a small theorem of this kind.

## Definitions

A **proof** of a claim is a finite sequence of statements that ends with the claim, where each statement is one of the following: something assumed in the claim (a hypothesis), a definition or an axiom, or a consequence of statements earlier in the sequence by a reasoning step the reader accepts.

In plain words, a proof is a convincing argument that starts from facts everybody has agreed on, moves in steps small enough to check one at a time, and arrives at the claim. This is the board game picture from [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md): the agreed facts are the rules, and each step is a move you can point at a rule for.

A **universal claim** says that something holds for every member of a set, such as "for every integer $n$, $n^2 \ge 0$". An **existential claim** says that at least one member has a property, such as "there is a prime between 90 and 100". The two behave very differently under examples:

| Kind of claim | One example | One counterexample |
|---|---|---|
| universal ("for every ...") | supports it but doesn't prove it | disproves it |
| existential ("there is ...") | proves it, if the example is checked | doesn't disprove it |

So "97 is a prime between 90 and 100" is a complete proof of the existential claim, and "$3 + 5 = 8$" is not a proof of the universal claim about sums of odd integers. Most claims in this chapter are universal, and the lesson on [quantifiers](../02-logic-and-sets/04-quantifiers.md) makes the difference exact.

Evidence, intuition and proof are three different things, and each has a job.

| Thing | What it gives you | What it can't do |
|---|---|---|
| intuition | a guess about what is true, and an idea of why | tell you the guess is right |
| evidence (examples, pictures, tests) | confidence that the guess is worth trying to prove, or a counterexample that kills it | cover every case |
| proof | certainty that the claim holds in every case, given the starting facts | find the claim for you |

A good working order is intuition first, then examples, then a proof. The examples are not wasted if the proof comes later. They tell you what a proof should look like, as the first step of the method below shows.

Two more words. A proof is **rigorous** when every step can be justified by a definition, an axiom or a result already established, with no step resting on a picture, a pattern or a feeling that it must be true. Rigour is not a matter of using more symbols. And the **audience** of a proof is the reader it is written for. A proof isn't written for yourself (you know what you meant), and it isn't written for a computer that needs every axiom. The best target is a classmate who has taken the same course: someone who knows the definitions and earlier results but hasn't seen your argument, and who should be able to check every line without asking you what you meant.

## How to do it

### A method for a first proof

Many of the first claims you will prove have the shape "if $P$, then $Q$", where $P$ is the hypothesis and $Q$ the conclusion, as in [conditional statements](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements). The method below handles these. The lesson on [direct proof](../03-core-proof-methods/01-direct-proof.md) gives it a full treatment.

1. Write down the claim in the form "if $P$, then $Q$", and say which part is the hypothesis and which the conclusion. Test it on one or two small cases, to see that it is plausible and to see what the numbers look like.
2. Introduce the objects. Name each thing the hypothesis talks about with a letter, and say what kind of thing it is: "Let $m$ and $n$ be even integers."
3. Unpack the definitions in the hypothesis. Turn each defined word into the equation or condition it stands for. "Even" becomes "equal to $2k$ for some integer $k$".
4. Look at the conclusion and say what you would have to show for it to be true, again by unpacking the definition. For "$m + n$ is even" you would need $m + n = 2 \times (\text{some integer})$.
5. Connect the two with steps you can justify. Usually this is algebra, and each line comes from a definition, an axiom or an earlier result.
6. Finish by saying why the last line is what you wanted, naming the definition it matches.
7. Reread your proof as your classmate would. At each line ask "why does this follow?" and make sure the answer is on the page.

### The first complete proof

*Theorem 1.* If $m$ and $n$ are even integers, then $m + n$ is even.

What we know: $m$ and $n$ are integers, and each is even. An integer is even when it equals $2k$ for some integer $k$, so we know that $m = 2j$ for some integer $j$, and $n = 2k$ for some integer $k$. Nothing else about $m$ and $n$ is given: they could be positive, negative or zero.

What we want: $m + n$ is even, which means $m + n = 2l$ for some integer $l$.

The plan: replace $m$ and $n$ by their definitions, then pull out the common factor 2. What is left over inside the brackets must be an integer, because it is a sum of integers.

*Proof.* Let $m$ and $n$ be even integers. By the definition of even, there are integers $j$ and $k$ with $m = 2j$ and $n = 2k$. Then

$$
m + n = 2j + 2k = 2(j + k).
$$

The sum $j + k$ is an integer, because $j$ and $k$ are integers. So $m + n$ is 2 times an integer, which is what it means for $m + n$ to be even. $\blacksquare$

Look back: the proof never used a specific value, so it covers every pair of even integers at once, including $m = 0$ and negative values. It also used two different letters $j$ and $k$. The two integers $m$ and $n$ may be different, so the integers that halve them may be different too (see the first warning under [Edge cases](#edge-cases-and-common-mistakes)). As a check with numbers, take $m = 6$ and $n = -10$: then $j = 3$, $k = -5$, and $m + n = -4 = 2 \times (-2)$ with $-2 = j + k$.

Here is the same proof taken apart, one sentence at a time. This is the habit to build: for every sentence, ask what it does and why it is allowed.

| Sentence | What it does | Why it is allowed |
|---|---|---|
| "Let $m$ and $n$ be even integers." | Introduces two objects and records the hypothesis. | It is the hypothesis of the theorem. The words "let ... be" name arbitrary objects, not particular numbers. |
| "By the definition of even, there are integers $j$ and $k$ with $m = 2j$ and $n = 2k$." | Unpacks the hypothesis into equations. | Definition of even. The letters $j$ and $k$ are new names for integers that exist because $m$ and $n$ are even. |
| "Then $m + n = 2j + 2k$." | Replaces $m$ and $n$ by what they equal. | Substitution. |
| "$2j + 2k = 2(j + k)$." | Pulls out the common factor. | Distributive property. |
| "The sum $j + k$ is an integer." | Checks that the number in brackets has the right type. | The sum of two integers is an integer. |
| "So $m + n$ is 2 times an integer, which is what it means for $m + n$ to be even." | Matches the last line with the definition of even. | Definition of even, used in the other direction. |
| $\blacksquare$ | Marks the end. | Convention. |

Every line either states a hypothesis, unpacks or applies a definition, or does algebra with a named rule. There is no sentence where the reader has to take your word for it.

## Worked examples

<div class="example" markdown>

### Example 1: an even integer plus an odd integer

*Theorem 2.* If $m$ is an even integer and $n$ is an odd integer, then $m + n$ is odd.

An integer $n$ is odd when $n = 2k + 1$ for some integer $k$. We follow the steps from the method.

Step 1: the hypothesis is "$m$ is even and $n$ is odd", and the conclusion is "$m + n$ is odd". Test it: $4 + 7 = 11$ is odd, and $-2 + 5 = 3$ is odd.

Step 2: let $m$ be an even integer and $n$ an odd integer.

Step 3: unpack the hypothesis. There are integers $j$ and $k$ with $m = 2j$ and $n = 2k + 1$.

Step 4: to show that $m + n$ is odd, we need an integer $l$ with $m + n = 2l + 1$.

Step 5: substitute, then group the terms so that one factor of 2 appears:

$$
m + n = 2j + (2k + 1) = 2(j + k) + 1.
$$

Step 6: the number $j + k$ is an integer, so $m + n$ has the form $2l + 1$ with $l = j + k$. That is the definition of odd. $\blacksquare$

Check: $m = 4$ and $n = 7$ give $j = 2$ and $k = 3$, so $l = 5$ and $2 \times 5 + 1 = 11 = 4 + 7$.

</div>

<div class="example" markdown>

### Example 2: when the pattern breaks

Claim: "the number $n^2 + n + 41$ is prime for every integer $n \ge 0$." We found 40 values that agree. To disprove a universal claim, one counterexample is enough, and it must be a case where the hypothesis holds and the conclusion fails.

Try $n = 40$:

$$
40^2 + 40 + 41 = 1600 + 81 = 1681 = 41 \times 41.
$$

The number 1681 has the divisor 41, which is neither 1 nor 1681, so it is not prime. The claim is false.

There is a reason this had to happen at or before $n = 41$. For $n = 41$ the expression is $41^2 + 41 + 41 = 41 \times 43 = 1763$, so it is a multiple of 41. In general, $n^2 + n + 41$ is a multiple of 41 whenever $n$ is a multiple of 41, because every term is. Finding this reason is a small proof, and it shows that the failure was not bad luck. (A known theorem says more: no nonconstant polynomial with integer coefficients is prime at every integer, so some failure was certain.)

Check: the divisors of 1681 are 1, 41 and 1681, so $1681 = 41^2$. In Python, `1681 % 41` is 0.

</div>

<div class="example" markdown>

### Example 3: revenue from a linear demand curve

A seller faces the demand $q = a - bp$, where $p$ is the price, $q$ the quantity sold, and $a$ and $b$ are positive constants. Revenue is price times quantity, $R(p) = p(a - bp)$. The seller wants the price with the largest revenue.

*Theorem 3.* Let $a > 0$ and $b > 0$. For every real number $p$,

$$
R(p) \le \frac{a^2}{4b},
$$

and equality holds exactly when $p = \frac{a}{2b}$.

What we know: $R(p) = p(a - bp)$ and $b > 0$. We also know that the square of a real number is never negative (Theorems 2 and 4 in [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#proving-facts-from-the-axioms)).

What we want: the gap $\frac{a^2}{4b} - R(p)$ is never negative, and it is 0 only at $p = \frac{a}{2b}$.

The plan: the gap should be a positive constant times a square. Compute it and see.

*Proof.* Expand $R(p) = ap - bp^2$. Then

$$
\frac{a^2}{4b} - R(p) = bp^2 - ap + \frac{a^2}{4b} = b\left(p - \frac{a}{2b}\right)^2.
$$

(The last equality is checked by expanding the right side: $b\left(p^2 - \frac{a}{b}p + \frac{a^2}{4b^2}\right) = bp^2 - ap + \frac{a^2}{4b}$.) Since $b > 0$ and a square is never negative, the gap is at least 0, so $R(p) \le \frac{a^2}{4b}$. The gap is 0 exactly when the square is 0, that is, when $p = \frac{a}{2b}$. $\blacksquare$

Look back: the proof used $b > 0$ at one step, to say that $b$ times a square is nonnegative. If $b < 0$ the inequality turns around, and the point $p = \frac{a}{2b}$ gives the smallest revenue, not the largest. This is the kind of information a proof carries: it tells you which assumption the result stands on.

Check with numbers: for $a = 120$ and $b = 4$ the best price is $\frac{120}{8} = 15$ and the revenue is $15 \times (120 - 60) = 900$, which equals $\frac{120^2}{16} = 900$. A price of 14 gives $14 \times 64 = 896$, and 16 gives $16 \times 56 = 896$, both below 900.

</div>

<div class="example" markdown>

### Example 4: three times an even integer (finish it yourself)

*Theorem 4.* If $n$ is an even integer, then $3n$ is even.

Steps 1 and 2: the hypothesis is "$n$ is even" and the conclusion is "$3n$ is even". Let $n$ be an even integer.

Step 3: by the definition of even, there is an integer $k$ with $n = 2k$.

Step 4: to show that $3n$ is even, we need an integer $l$ with $3n = 2l$.

Now do Steps 5 and 6: write $3n$ in terms of $k$, find $l$, and finish the proof.

<details class="solution" markdown>
<summary>Finish</summary>

Step 5: $3n = 3(2k) = 6k = 2(3k)$, using the associative property for the regrouping.

Step 6: the number $3k$ is an integer, because $k$ is, so $3n = 2l$ with $l = 3k$. That is the definition of even. $\blacksquare$

Check: $n = 8$ gives $k = 4$, and $3n = 24 = 2 \times 12$ with $12 = 3k$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for reusing a letter. If you write "$m = 2k$ and $n = 2k$", you have forced $m = n$, and the proof only covers equal numbers. Two different integers need two different letters, as in Theorem 1. The find-the-error problem in the practice section shows a whole false proof built on this slip.

</div>

<div class="warning" markdown>

Watch out for proving a special case. Writing "Let $m = 4$ and $n = 6$. Then $m + n = 10 = 2 \times 5$, which is even" proves a fact about 4 and 6, and nothing else. The first line of a proof should say "Let $m$ and $n$ be even integers", with letters, so that the argument holds for every choice. The lesson [proof language: let, suppose, WLOG](03-proof-language-let-suppose-wlog.md) explains the difference between "let $n$ be an integer" and "let $n = 3$".

</div>

<div class="warning" markdown>

Watch out for assuming what you want to show. A proof of Theorem 1 that starts "Suppose $m + n = 2l$" has begun at the conclusion. That is a different argument, and it proves the converse direction, if it proves anything. Start from the hypothesis and arrive at the conclusion.

</div>

<div class="warning" markdown>

Watch out for treating a picture or a check as a proof. A diagram of a few cases, or a program that tests ten thousand inputs, can show you that a claim is probably right or that it is wrong. A claim about infinitely many cases is proved only by an argument about all of them. One exception is worth knowing: if the set of cases is finite and small enough, checking every one is a proof (see the FAQ).

</div>

Zero and negative numbers need no special treatment in Theorem 1, and that is a good sign about a proof. Zero is even, because $0 = 2 \times 0$, and a negative even number such as $-6 = 2 \times (-3)$ fits the definition with a negative $k$. If a proof breaks for 0 or for negative values, it was written for positive numbers only, and the hypothesis should say so.

## Tricks and shortcuts

Before writing a proof, test the claim on three inputs: a typical one, a zero or smallest case, and a negative or unusual one. If a test fails, you have a counterexample and no proof to write. If the tests pass, the numbers you used often show which definition to unpack.

A short check for any proof you write: cover everything except one line and ask "what lets me write this?" If the answer is a definition, an axiom, a hypothesis or an earlier line, the line is fine. If the answer is "it seems right", that line is the gap.

Say the proof aloud to an imagined classmate. Each time you say "so" or "therefore", pause and give the reason. A reason you can't state is a step to repair.

## In code

Code can test a claim, but it can't prove a claim about infinitely many cases. These lines show testing next to an argument: a pattern that holds for 40 values and then breaks, a check over a finite box of even integers, and an invariant checked as the loop runs.

<details class="code" markdown>
<summary>In code</summary>

```python
def is_prime(m):
    return m > 1 and all(m % d for d in range(2, int(m ** 0.5) + 1))

print(all(is_prime(n * n + n + 41) for n in range(40)))   # True: 40 cases agree
print(40 * 40 + 40 + 41, is_prime(1681))                  # 1681 False: case 41 breaks it

evens = range(-100, 101, 2)
print(all((m + n) % 2 == 0 for m in evens for n in evens))   # True
print(len(evens) ** 2)                                       # 10201 pairs, but infinitely many remain

xs = [4, 8, 15, 16, 23, 42]
total = 0
for i, x in enumerate(xs):
    assert total == sum(xs[:i])   # invariant: total is the sum of the entries already seen
    total += x
assert total == sum(xs)
print(total)                                                 # 108
```

The first two lines are evidence that fails. The check on 10,201 pairs of even integers supports Theorem 1 but doesn't prove it, and the algebra in the proof does. The `assert` inside the loop tests the invariant on one list; the three-sentence argument above proves it for every list.

</details>

## FAQ

### If a computer checks every case up to a huge number, isn't that a proof?

Not for a claim about all integers, because there are infinitely many integers and the check stops somewhere. The expression $n^2 + n + 41$ survived the first 40 values and failed at the 41st. The check is a proof only when the set of cases is finite and you really run through all of it, such as a claim about every 8-bit input. Some conjectures, such as Goldbach's (every even integer greater than 2 is the sum of two primes), have been checked by computer for extremely large numbers and still have no proof.

### Why prove something that already seems true?

Because the proofs in this chapter are practice on safe ground. "The sum of two even integers is even" is not in doubt. The point is the method: unpack the definition, compute, match the result with a definition. The same method proves claims you can't settle by looking, such as whether an algorithm always terminates or whether a bound holds for all inputs. Also, "it seems true" is how people have ended up believing false statements, such as the prime-producing polynomial after its first 40 values.

### How much detail does a proof need?

Enough for its audience to check each step without help. In this chapter, that means naming the definition or rule behind each line. Later, once the reader knows the laws of algebra by heart, you stop naming them and write "by algebra". The rule is that a step may be skipped when your classmate could fill it in at once, and not otherwise.

### Do I have to prove everything I use?

No. A proof can use the hypotheses, definitions, axioms and any result that has been proved earlier (or that the course lets you cite). Facts such as "the sum of two integers is an integer" are accepted as part of the arithmetic everyone shares. If you are not sure whether you may use a fact, ask whether it is in your course notes or textbook. When it isn't, prove it first, or find a way around it.

## Practice

### Warm-up

1\. Decide whether each argument is a proof of its claim or only evidence. (a) "My sorting function returned a sorted list on 1,000 random inputs, so it is correct." (b) "The number 91 is not prime, because $91 = 7 \times 13$." (c) "The sum of two odd integers is even, because $3 + 5 = 8$." (d) "There is a prime between 90 and 100, because 97 is prime."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Evidence only. The claim is about every input, and 1,000 inputs leave infinitely many unchecked. The empty list, a list of repeats or a list that is already sorted could all behave differently.
- (b) A proof. "Not prime" means "has a divisor other than 1 and itself", so one divisor settles it, and $7 \times 13 = 91$ can be checked by multiplying.
- (c) Evidence only, because the claim is about all pairs of odd integers and one pair doesn't cover them.
- (d) A proof. The claim is existential, so one example that is verified is enough. The number 97 has no divisor from 2 to 9, since 9 is the integer part of $\sqrt{97} \approx 9.85$, so it is prime.

Check: $7 \times 13 = 91$, and $97$ is not divisible by 2, 3, 5 or 7 (the primes up to 9).

</details>

2\. Find a counterexample to the claim "the number $2^n - 1$ is prime for every integer $n \ge 2$".

<details class="solution" markdown>
<summary>Solution</summary>

Try small values. For $n = 2, 3$ the numbers are $3$ and $7$, both prime. For $n = 4$ the number is $2^4 - 1 = 15 = 3 \times 5$, which is not prime. So $n = 4$ is a counterexample, and the claim is false.

Check: $3 \times 5 = 15$. The values $n = 5$ and $n = 7$ give the primes 31 and 127, so the pattern fails after starting well, much like the polynomial in the lesson. Other counterexamples are $n = 6$ (63) and $n = 11$ (2047, which is $23 \times 89$).

</details>

3\. Here is a proof that if $m$ is an even integer and $n$ is any integer, then $mn$ is even. Give the reason for each numbered line.

1. Let $m$ be an even integer and $n$ an integer.
2. There is an integer $k$ with $m = 2k$.
3. Then $mn = (2k)n$.
4. So $mn = 2(kn)$.
5. The product $kn$ is an integer.
6. So $mn$ is 2 times an integer, and $mn$ is even.

<details class="solution" markdown>
<summary>Solution</summary>

1. The hypothesis of the claim (this line introduces $m$ and $n$).
2. The definition of even, applied to $m$.
3. Substitution of $2k$ for $m$.
4. The associative property of multiplication, which regroups $(2k)n$ as $2(kn)$.
5. The product of two integers is an integer.
6. The definition of even, used with the integer $kn$.

Look back: the proof doesn't need $n$ to be even or odd. It is Theorem 4's argument with 3 replaced by any integer. Check: $m = 6$ and $n = -7$ give $k = 3$, and $mn = -42 = 2 \times (-21)$ with $-21 = kn$.

</details>

### Standard

4\. Prove that the sum of two odd integers is even.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $m$ and $n$ are odd, so $m = 2j + 1$ and $n = 2k + 1$ for integers $j$ and $k$. What we want: $m + n = 2l$ for some integer $l$. The plan: add, and gather the two 1s into a 2.

*Proof.* Let $m$ and $n$ be odd integers. By the definition of odd, there are integers $j$ and $k$ with $m = 2j + 1$ and $n = 2k + 1$. Then

$$
m + n = (2j + 1) + (2k + 1) = 2j + 2k + 2 = 2(j + k + 1).
$$

The number $j + k + 1$ is an integer, so $m + n$ is 2 times an integer. That is, $m + n$ is even. $\blacksquare$

Check: $m = 3$ and $n = 5$ give $j = 1$ and $k = 2$, so $j + k + 1 = 4$ and $2 \times 4 = 8 = 3 + 5$. The proof also covers $m = -1$ and $n = 1$: here $j = -1$, $k = 0$, and the sum is $0 = 2 \times 0$ with $j + k + 1 = 0$.

</details>

5\. Find the error in this proof, and say whether the claim is true. Claim: the sum of two even integers is divisible by 4. "Proof. Let $m$ and $n$ be even integers. Then $m = 2k$ and $n = 2k$ for an integer $k$. So $m + n = 2k + 2k = 4k$, which is divisible by 4."

<details class="solution" markdown>
<summary>Solution</summary>

The error is in the second sentence. Writing $m = 2k$ and $n = 2k$ with the same $k$ forces $m = n$. The argument therefore covers only pairs of equal even integers, such as $6 + 6$, and the claim is about all pairs.

The claim is false. A counterexample is $m = 2$ and $n = 4$: the sum is $6$, and $6 \div 4$ leaves remainder 2. (The sum of two even integers is always even, by Theorem 1, but divisible by 4 only sometimes.)

The correct start is $m = 2j$ and $n = 2k$ with two letters, which gives $m + n = 2(j + k)$ and no more. Check: $2 + 4 = 6 = 2 \times 3$, and $3$ is not a multiple of 2, so 6 is not a multiple of 4.

</details>

6\. Prove that the product of two even integers is divisible by 4.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $m = 2j$ and $n = 2k$ for integers $j$ and $k$. What we want: $mn = 4l$ for some integer $l$. The plan: multiply the two definitions.

*Proof.* Let $m$ and $n$ be even integers. Then $m = 2j$ and $n = 2k$ for some integers $j$ and $k$, and

$$
mn = (2j)(2k) = 4jk.
$$

The product $jk$ is an integer, so $mn = 4l$ with $l = jk$. Hence $mn$ is divisible by 4. $\blacksquare$

Check: $m = 6$ and $n = 10$ give $j = 3$ and $k = 5$, and $mn = 60 = 4 \times 15$ with $15 = jk$. Compare with problem 5: sums of even integers need not be multiples of 4, but products always are.

</details>

### Challenge

7\. A seller faces the demand $q = 100 - 2p$ and pays a cost of \$10 per unit, so the profit is $\pi(p) = (p - 10)(100 - 2p)$. Prove that $\pi(p) \le 800$ for every price $p$, with equality only when $p = 30$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $\pi(p) = (p - 10)(100 - 2p)$, and a square is never negative. What we want: $800 - \pi(p) \ge 0$, with equality only at $p = 30$. The plan: multiply out, then complete the square as in Example 3.

*Proof.* Expanding, $\pi(p) = 100p - 2p^2 - 1000 + 20p = -2p^2 + 120p - 1000$. Then

$$
800 - \pi(p) = 2p^2 - 120p + 1800 = 2(p - 30)^2.
$$

(Expanding the right side gives $2(p^2 - 60p + 900) = 2p^2 - 120p + 1800$.) Since $(p - 30)^2 \ge 0$, we have $800 - \pi(p) \ge 0$, so $\pi(p) \le 800$. The gap is 0 exactly when $(p - 30)^2 = 0$, which means $p = 30$. $\blacksquare$

Look back: the assumption doing the work is that the cost per unit is a constant 10 and the demand is linear. A cost that changed with $q$ would change the formula for $\pi$. Check: $\pi(30) = 20 \times 40 = 800$, and $\pi(28) = 18 \times 44 = 792$ and $\pi(32) = 22 \times 36 = 792$, both below 800.

</details>

8\. (Reviews [place value and rounding](../../01-elementary/01-place-value-and-rounding.md).) Prove that if the digits of a three-digit number add up to a multiple of 9, then the number is divisible by 9. Then explain why checking all 900 three-digit numbers with a program would also settle this claim, but would not settle the same claim for all numbers.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the number is $n = 100a + 10b + c$, where $a$, $b$ and $c$ are its digits (place value), and $a + b + c = 9t$ for an integer $t$. What we want: $n = 9l$ for an integer $l$. The plan: split each place value into a multiple of 9 plus a leftover, $100 = 99 + 1$ and $10 = 9 + 1$.

*Proof.* Let $n = 100a + 10b + c$ with digits $a$, $b$ and $c$, and suppose $a + b + c = 9t$ for an integer $t$. Then

$$
n = 99a + 9b + (a + b + c) = 9(11a + b) + 9t = 9(11a + b + t).
$$

The number $11a + b + t$ is an integer, so $n$ is 9 times an integer. $\blacksquare$

A program that loops over $n = 100, \dots, 999$ and tests every one with the digit sum rule examines every case, because the set of cases is finite. That is a proof for three-digit numbers. For "every integer" the set is infinite, so a loop can only test the first part of it, and the algebra above is what generalizes (with more digits, the same trick splits $1000 = 999 + 1$, and so on).

Check: $n = 387$ has digit sum $18 = 9 \times 2$, and $387 = 9 \times 43$. The formula gives $11 \cdot 3 + 8 + 2 = 43$.

</details>

## Where this shows up

- The next lesson, [definitions, theorems, lemmas and corollaries](02-definitions-theorems-lemmas-corollaries.md), names the parts of a mathematical text, and [proof language](03-proof-language-let-suppose-wlog.md) lists the phrases you used in the proofs above. The method of this lesson is developed in [direct proof](../03-core-proof-methods/01-direct-proof.md), and a proof that fails to cover every case is the first thing to look for in common proof mistakes<!-- link: ../07-putting-it-together/01-common-proof-mistakes.md -->.
- In CS courses, invariants and algorithm correctness<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md --> proves that a loop or a recursive function is right for every input, and reductions and undecidability<!-- link: ../../06-cs-math/06-theory-of-computation/06-reductions-and-undecidability.md --> proves that one problem is as hard as another. The loop-invariant argument above is [mathematical induction](../05-induction/01-mathematical-induction.md) in disguise.
- In economics, results are proved from stated assumptions: profit maximization and market structure<!-- link: ../../07-economics-math/03-firms-and-consumers/03-profit-maximization-and-market-structure.md --> derives the best price or quantity, and the proof shows which assumption it depends on.
