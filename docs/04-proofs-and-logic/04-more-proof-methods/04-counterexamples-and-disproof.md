# Counterexamples and disproof

After this lesson you can say what it takes to disprove each shape of statement, find a counterexample by checking edge cases and small cases (by hand or by a short program), check that a counterexample satisfies every hypothesis, and decide whether a "prove or disprove" claim is true.

Before this: [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md), [quantifiers](../02-logic-and-sets/04-quantifiers.md) and [proofs about sets](03-proofs-about-sets.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Disprove the claim "for every integer $n$, $n^2 > n$".
2. Which of these are counterexamples to "if a positive integer $n$ is divisible by 6, then $n$ is divisible by 12"? (a) $n = 18$. (b) $n = 12$. (c) $n = 8$.
3. Does the single example $x = 1$ disprove the claim "there is an integer $x$ with $x^2 = 2$"?

<details class="solution" markdown>
<summary>Answers</summary>

1. Take $n = 1$: $n^2 = 1$, which is not greater than $n = 1$. (The value $n = 0$ also works.) One case where the claim fails disproves a "for every" claim.
2. Only (a). For $n = 18$, $6 \mid 18$ and $12 \nmid 18$. For $n = 12$ the conclusion is true, so it is not a counterexample. For $n = 8$ the hypothesis is false ($6 \nmid 8$), so it says nothing about the claim.
3. No. The claim says some integer has square 2, and showing that one integer fails does not rule out the others. To disprove it you must show that $x^2 \ne 2$ for every integer $x$, for example because $x^2$ is $0, 1$ or at least $4$.

</details>

## The idea

A bug report is most useful when it contains an input that makes the program fail. "The sort function is wrong" starts an argument, and "`sort([2, 1, 2])` returns `[1, 2]`" ends it, because anyone can run the input and look. A counterexample plays the same role for a mathematical claim. It is a failing test case that you have checked by hand, and once it is on the page, nobody can argue with it.

The strength of a counterexample is that it works against a "for every" claim with a single case. The cost is that it must be a proper case: it has to satisfy every hypothesis, and the conclusion has to fail. Most wrong counterexamples are cases that only look like they break the claim. Software tools make the same distinction. A property-based testing tool such as the Python library Hypothesis generates many inputs, finds one that violates a property, and then shrinks it to a minimal failing case. The programs you write in this lesson do a small version of that search.

Disproof has a second job: it tells you what to fix. When a claim is nearly true, the counterexample shows which hypothesis was missing. "If $a$ divides $bc$, then $a$ divides $b$ or $a$ divides $c$" is false, and the smallest counterexample has $a = 4$, which points straight at the hypothesis that makes it true: $a$ prime.

## Definitions

A **counterexample** to a statement "for every $x$ in $D$, if $P(x)$ then $Q(x)$" is an element $x$ of $D$ for which $P(x)$ is true and $Q(x)$ is false. In plain words, it is a case that meets all the conditions of the claim and still fails the conclusion. A statement with no hypothesis, such as "for every $n$, $n^2 > n$", has the same definition with $P$ always true.

To **disprove** a statement is to prove that it is false, which is the same as proving its negation. This is why the negation rules from [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md) come first: you can only prove the negation once you have written it out. A counterexample is one kind of disproof, the one that suits a "for every" claim.

An **edge case** is a value at the boundary of what a claim allows, or one that behaves differently from its neighbours: $0$, $1$, negative numbers, equal values, the empty set. Claims that were proved or guessed from typical cases tend to fail at edge cases first.

What a disproof must show depends on the shape of the statement. The negations come from the table in the negation lesson.

| Statement | Its negation | To disprove it, show |
|---|---|---|
| for every $x$, $P(x)$ | there exists $x$ with not $P(x)$ | one $x$ where $P$ fails |
| for every $x$, if $P(x)$ then $Q(x)$ | there exists $x$ with $P(x)$ and not $Q(x)$ | one $x$ with $P$ true and $Q$ false |
| there exists $x$ with $P(x)$ | for every $x$, not $P(x)$ | a proof that $P$ fails for all $x$ |
| for every $x$ there exists $y$ with $P(x, y)$ | there exists $x$ such that for every $y$, not $P(x, y)$ | one $x$, and a proof that every $y$ fails for it |
| there exists $x$ such that for every $y$, $P(x, y)$ | for every $x$ there exists $y$ with not $P(x, y)$ | for an arbitrary $x$, a $y$ (that may depend on $x$) that breaks it |
| $P$ and $Q$ | not $P$ or not $Q$ | that one of them is false |
| $P$ or $Q$ | not $P$ and not $Q$ | that both are false |
| $P$ if and only if $Q$ | $P$ and not $Q$, or $Q$ and not $P$ | a case where exactly one of them holds |
| there is exactly one $x$ with $P(x)$ | none, or at least two | a proof that none works, or two different ones that do |
| $A \subseteq B$ (sets) | some element of $A$ is not in $B$ | one element of $A$ that is not in $B$ |
| $A = B$ (sets) | some element is in one set and not in the other | one such element |

The third row is the one that surprises people. A single example can't disprove an existence claim. Disproving "there is a real number $x$ with $x^2 + 2x + 2 = 0$" takes a proof that no real number works.

## How to do it

### Disproving a claim

1. Write the claim in full: the domain, the hypotheses and the conclusion, with the quantifiers in order.
2. Negate it. Push the negation in until it sits on the conclusion, so you know the exact shape of what you need.
3. Say in words what a witness looks like. For "if $P(x)$ then $Q(x)$", it is "an $x$ with $P(x)$ true and $Q(x)$ false".
4. Search for the witness. Try the edge cases in the table below first, then small values in order, then a computer search. If you get stuck, try to prove the claim and see where the proof fails.
5. Verify the witness twice: check that every hypothesis holds, and check that the conclusion fails. Show the computation for both.
6. Write the disproof as a sentence: "Take $x = \dots$. Then ... holds but ... fails, so the claim is false."

### Where to look

| Kind of object | Try first |
|---|---|
| integers | $0$, $1$, $-1$, $2$ (the only even prime), a small prime, a small composite, a perfect square |
| two or more numbers | equal values ($a = b$), one of them $0$ or $1$, opposite signs |
| real numbers | a fraction between 0 and 1 (such as $\frac{1}{2}$), a negative number, a very large or very small number |
| sets | $\emptyset$, a one-element set, equal sets, disjoint sets, a set that contains another |
| functions and sequences | a constant, the empty list, a one-element list, a list with repeats |
| graphs | no edges, one vertex, a complete graph, a tree |

Edge cases come first because that is where claims break. A claim that seems to be about "typical" numbers often gets its first failure at $0$ or at equal values.

### Using a computer

For a claim about integers, a loop over a range finds a counterexample if a small one exists. The pattern is always the same: iterate over the domain, test the hypothesis, test the conclusion, and report the first case where the hypothesis is true and the conclusion is false. The In code section has a short function for this. Three cautions.

- A search that finds nothing proves nothing. It says only that there is no counterexample in the range you tried. The Pólya conjecture below holds for every number below 906,150,257 and is still false.
- Check the result by hand. A counterexample found by a program still goes through Step 5, and you write the arithmetic out.
- The program tests the claim you coded, not the one you meant. If the hypothesis or the domain is coded wrong, the answer is for a different statement.

### Why a counterexample must satisfy every hypothesis

The claim "if $n$ is even, then $n^2$ is divisible by 4" is true. Someone offers $n = 3$ as a counterexample: $3^2 = 9$ is not divisible by 4. But $n = 3$ is not even, so the hypothesis fails, and the claim says nothing about $n = 3$. A conditional is false only in the case where its hypothesis is true and its conclusion is false. The other three rows of the truth table, with a false hypothesis or with a true conclusion, leave the conditional true.

### Prove or disprove

Some problems give a claim and ask whether it is true. The method:

1. Test two or three cases, including edge cases. A failure ends the search: you have a counterexample.
2. If every test passes, try to prove the claim. Choose the method from the shape of the claim.
3. If the proof gets stuck, look at where. The stuck point often shows what a counterexample must look like, or which hypothesis is missing.
4. Write whichever you found: a proof, or a counterexample with its two checks.

If a claim is false but nearly true, you can often repair it by adding a hypothesis, and then prove the repaired claim. Examples 1 and 4 do this.

### Famous false conjectures

Patterns that hold for a long time can still be false. Four well-known cases.

The polynomial $n^2 + n + 41$ gives a prime for $n = 0, 1, \dots, 39$, and $n = 40$ gives $1681 = 41^2$ ([what is a proof](../01-language-and-notation/01-what-is-a-proof.md#the-idea)).

Fermat noticed that $2^{2^n} + 1$ is prime for $n = 0, 1, 2, 3, 4$ (the values $3, 5, 17, 257, 65537$) and guessed it is prime for every $n$. Euler showed in 1732 that $n = 5$ fails: $2^{32} + 1 = 4294967297 = 641 \times 6700417$.

Euler conjectured that a sum of fewer than $k$ positive $k$-th powers can't be a $k$-th power. For $k = 3$ the conjecture is true (it contains Fermat's last theorem for exponent 3). For $k = 5$, Lander and Parkin found by computer search in 1966 that

$$
27^5 + 84^5 + 110^5 + 133^5 = 144^5,
$$

a sum of four fifth powers that is a fifth power. For $k = 4$, Elkies found a counterexample in 1986, and Frye found the smallest, $95800^4 + 217519^4 + 414560^4 = 422481^4$ (1988). Practice problem 7 asks you to verify the fifth-power case.

Pólya conjectured in 1919 that, for every $n > 1$, at least half of the integers from 1 to $n$ have an odd number of prime factors (counted with multiplicity). It holds for every $n$ below $906{,}150{,}257$. Haselgrove proved in 1958 that it must fail somewhere, and the smallest counterexample, $n = 906{,}150{,}257$, was found by Tanaka in 1980. (Sources: the Wikipedia articles on the Pólya conjecture and on Euler's sum of powers conjecture.)

The moral is the one from the first proof lesson. A pattern, even a pattern checked up to enormous numbers, is a reason to look for a proof and not a proof. And a false claim has a counterexample, which may be very large.

## Worked examples

<div class="example" markdown>

### Example 1: divides a product, divides a factor

*Claim.* For all integers $a$, $b$ and $c$, if $a \mid bc$, then $a \mid b$ or $a \mid c$.

Step 1: the domain is the integers; the hypothesis is $a \mid bc$; the conclusion is "$a \mid b$ or $a \mid c$". Step 2: the negation is "there are integers $a$, $b$, $c$ with $a \mid bc$, $a \nmid b$ and $a \nmid c$" (the negation of "or" is "and not"). Step 3: so a witness is a triple where $a$ divides the product but divides neither factor.

What we know: the definition of divides. What we want: such a triple. The plan: search by size of $a$. The value $a = 1$ divides everything, so it can't work. For $a = 2$, a product $bc$ is even only if $b$ or $c$ is even, so $2 \mid b$ or $2 \mid c$, and the conclusion holds. The same reasoning works for $a = 3$ and for every prime. So we need $a$ composite, and the smallest is $a = 4$. For 4 to divide $bc$ without dividing either factor, split the factor 2 twice: $b = 2$ and $c = 2$.

*Disproof.* Take $a = 4$, $b = 2$ and $c = 2$ (the result of Step 4). Step 5, the two checks. The hypothesis holds: $bc = 4 = 4 \cdot 1$, so $4 \mid bc$. The conclusion fails: $2 = 4k$ has no integer solution, since it would force $k = \frac{1}{2}$, so $4 \nmid 2$, and the same for $c$. Hence the claim is false. $\blacksquare$

Look back: the counterexample has $b = c$, an edge case worth trying early. It also tells you the repair. The claim is true when $a$ is prime (Euclid's lemma, proved in the number theory chapter), and the search above explains why: for a prime there is no way to split the factors. Another counterexample with different numbers is $a = 6$, $b = 2$ and $c = 3$, where $bc = 6$.

Check: a short search over $1 \le a, b, c \le 10$ lists $(4, 2, 2)$ first, which agrees.

</div>

<div class="example" markdown>

### Example 2: a claim about sets

*Claim.* For all sets $A$, $B$ and $C$, if $A \cap B \subseteq C$, then $A \subseteq C$ or $B \subseteq C$.

Negation: there are sets $A$, $B$, $C$ with $A \cap B \subseteq C$, $A \not\subseteq C$ and $B \not\subseteq C$. The set edge cases (empty, disjoint) are the natural place to look: if $A$ and $B$ are disjoint, then $A \cap B = \emptyset$, which is a subset of every set, so the hypothesis holds for free.

*Disproof.* Take $A = \{1\}$, $B = \{2\}$ and $C = \emptyset$. The hypothesis holds: $A \cap B = \emptyset \subseteq C$ (the empty set is a subset of every set). The conclusion fails: $1 \in A$ and $1 \notin C$, so $A \not\subseteq C$; and $2 \in B$ and $2 \notin C$, so $B \not\subseteq C$. Hence the claim is false. $\blacksquare$

Look back: this is a counterexample that uses two edge cases at once, disjoint sets and an empty set. A drawing of overlapping circles would never have suggested it. Check: disjoint sets are not needed. The overlapping sets $A = \{1, 2\}$, $B = \{2, 3\}$ and $C = \{2\}$ are also a counterexample: $A \cap B = \{2\} \subseteq C$, while $1 \in A$ is not in $C$ and $3 \in B$ is not in $C$.

</div>

<div class="example" markdown>

### Example 3: disproving an existence claim and a biconditional

(a) *Claim.* There is a real number $x$ with $x^2 + 2x + 2 = 0$.

The negation is "for every real $x$, $x^2 + 2x + 2 \ne 0$". A counterexample isn't available for this shape; we need a proof about all $x$. Complete the square: $x^2 + 2x + 2 = (x + 1)^2 + 1$. A square is at least 0, so $(x + 1)^2 + 1 \ge 1 > 0$ for every real $x$. Hence no real $x$ solves the equation, and the claim is false. $\blacksquare$

(b) *Claim.* For every integer $n$, $4 \mid n^2$ if and only if $4 \mid n$.

A biconditional is disproved by a case where exactly one side holds. Test the direction ($\Rightarrow$): the hypothesis is $4 \mid n^2$ and the conclusion is $4 \mid n$. Take $n = 2$. Then $n^2 = 4$ and $4 \mid 4$, so the hypothesis holds. But $4 \nmid 2$, so the conclusion fails. The claim is false. $\blacksquare$

Look back: only one direction failed. The other direction is true: if $n = 4k$ then $n^2 = 16k^2 = 4(4k^2)$. This is the situation of [if and only if proofs](01-if-and-only-if-proofs.md): a biconditional needs both halves, and one bad half sinks it. The true statement with a similar look is "$2 \mid n^2$ if and only if $2 \mid n$".

Check: $n = 2$ gives $4 \mid 4$ and $4 \nmid 2$. And in (a), the value of the expression at $x = -1$ is $1 - 2 + 2 = 1$, the smallest it gets.

</div>

<div class="example" markdown>

### Example 4: prove or disprove

Decide each claim for integers or real numbers as stated.

(a) For every integer $n$, $n^2 + n + 1$ is odd.

Test: $n = 0$ gives 1, $n = 1$ gives 3, $n = 2$ gives 7, $n = -1$ gives 1. All odd, so try a proof. Since $n^2 + n = n(n + 1)$, we show that $n(n + 1)$ is even. If $n$ is even, $n = 2k$ and $n(n + 1) = 2(k(n + 1))$. If $n$ is odd, $n + 1 = 2k$ and $n(n + 1) = 2(kn)$. In both cases $n^2 + n = 2m$ for an integer $m$, so $n^2 + n + 1 = 2m + 1$ is odd. $\blacksquare$ The claim is true.

(b) For all real numbers $x$ and $y$, if $x < y$ then $x^2 < y^2$.

Test with a negative number: $x = -3$ and $y = 2$. The hypothesis holds, since $-3 < 2$. The conclusion fails: $x^2 = 9$ and $y^2 = 4$, and $9 < 4$ is false. So the claim is false. $\blacksquare$

(c) Repair (b): for real numbers with $0 \le x < y$, we have $x^2 < y^2$. This is true, and it is Practice problem 7 of [if and only if proofs](01-if-and-only-if-proofs.md#practice) in different clothes. Here is a direct proof. Since $x \ge 0$ and $y > x \ge 0$, multiplying $x < y$ by $y > 0$ gives $xy < y^2$, and multiplying $x < y$ by $x \ge 0$ gives $x^2 \le xy$. So $x^2 \le xy < y^2$. $\blacksquare$

Check: for (a), $n = 5$ gives $31$, odd; $n = -4$ gives $13$, odd. For (b), the counterexample has $x < 0$, which is why (c) adds $x \ge 0$.

</div>

<div class="example" markdown>

### Example 5: a polynomial that is prime for a while (finish it yourself)

*Claim.* For every positive integer $n$, $n^2 + n + 17$ is prime.

Step 1 and 2: the negation is "there is a positive integer $n$ for which $n^2 + n + 17$ is composite". A search by hand starts $n = 1, 2, 3, \dots$ and gives $19, 23, 29, 37, 47, 59, 73, 89, 107, 127, \dots$, all prime so far. A better move than brute force: by analogy with $n^2 + n + 41$, ask which $n$ makes every term a multiple of 17. If $17 \mid n$, then $n = 17k$ and $n^2 + n + 17 = 17(17k^2 + k + 1)$.

Now finish: pick the smallest such $n$, compute the value, and show it is composite. Then say what the smallest counterexample of all is.

<details class="solution" markdown>
<summary>Finish</summary>

Take $n = 17$: $17^2 + 17 + 17 = 289 + 34 = 323 = 17 \times 19$. This is composite (17 divides it, and $17 \ne 1$ and $17 \ne 323$), so the claim is false. $\blacksquare$

The smallest counterexample is smaller: $n = 16$ gives $256 + 16 + 17 = 289 = 17^2$. A loop over $n = 1, \dots, 16$ shows the first 15 values are prime and the 16th is $289$.

Check: $17 \times 19 = 323$ and $17^2 = 289$, and $16^2 + 16 + 17 = 289$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for a "counterexample" that breaks a hypothesis. The claim "if $n$ is even, then $n^2$ is even" is true, and $n = 3$ ($3^2 = 9$ is odd) is not a counterexample, because $n = 3$ is not even. Always check the hypothesis first, in writing. A real counterexample has two checks: the hypothesis is true, and the conclusion is false.

</div>

<div class="warning" markdown>

Watch out for disproving the wrong statement. The converse of a true claim may be false, and a counterexample to the converse says nothing about the original. "If $n$ is divisible by 4, then $n$ is even" is true. The case $n = 2$ is even and not divisible by 4, which refutes the converse only.

</div>

<div class="warning" markdown>

Watch out for using examples to "disprove" an existence claim. Checking that $x = 1, 2, 3$ don't solve $x^2 = 2$ does not show that no integer does. For a claim of the form "there exists", the disproof is a proof of "for every, not", which needs an argument about all cases.

</div>

<div class="warning" markdown>

Watch out for the domain. "For every natural number $n$, $n^2 \ge n$" is true: $n^2 - n = n(n - 1) \ge 0$ for $n = 0, 1, 2, \dots$. The same sentence for real numbers is false, with the counterexample $x = \frac{1}{2}$: $\frac{1}{4} < \frac{1}{2}$. Read the domain before you search.

</div>

<div class="warning" markdown>

Watch out for treating a failed search as a proof, and a failed proof as a disproof. A computer search with no hit means only that no small counterexample exists. A proof attempt that stalls means only that you haven't found the proof. Neither is a conclusion. The conclusions are a proof or a checked counterexample.

</div>

<div class="warning" markdown>

Watch out for a counterexample that is not checked. Writing "$a = 6$, $b = 4$, $c = 3$" for Example 1 without computing $bc = 12$ and $6 \mid 12$ invites an error. Write out the hypothesis check and the conclusion check as separate lines.

</div>

A counterexample is allowed to be unnatural. Equal values, zero, an empty set and a very small set are all legal, so long as they satisfy the hypotheses, and they are the first things to try.

## Tricks and shortcuts

Negate first. Writing the negation out in full tells you what a witness looks like, and it prevents the commonest error, which is looking for the wrong kind of example.

Make the hypothesis barely true and the conclusion barely false. For "if $P$ then $Q$" this means choosing the object with the least room: the smallest number, the smallest set, a value on a boundary.

When a claim fails, look for the smallest counterexample, not just any. The smallest one is easiest to check by hand, and it often shows which hypothesis you were missing.

Let a stalled proof guide the search. In Example 1, the attempt to prove the claim for $a = 2$ and $a = 3$ goes through, and the reason it breaks for $a = 4$ is the counterexample.

For a claim about two numbers, try the case where they are equal, and then the case where one of them is zero or one. Many wrong claims survive "generic" pairs but fail on these.

## In code

A short function finds the first counterexample to a conditional claim over a range. The same function finds nothing for a true claim, which is evidence and not proof. The last lines show that a search to 100,000 would not have found the Pólya counterexample: the claim holds there, and fails first near 906 million.

<details class="code" markdown>
<summary>In code</summary>

```python
from itertools import product

def first_counterexample(domain, hypothesis, conclusion):
    for x in domain:
        if hypothesis(x) and not conclusion(x):
            return x
    return None

# if n is divisible by 6, then n is divisible by 12
print(first_counterexample(range(1, 100), lambda n: n % 6 == 0, lambda n: n % 12 == 0))   # 6

# if n^2 is divisible by 4, then n is divisible by 4
print(first_counterexample(range(1, 100), lambda n: n * n % 4 == 0, lambda n: n % 4 == 0))   # 2

# n^2 + n + 17 is prime for every positive integer n
def is_prime(m):
    return m > 1 and all(m % d for d in range(2, int(m ** 0.5) + 1))

print(first_counterexample(range(1, 100), lambda n: True, lambda n: is_prime(n * n + n + 17)))   # 16

# if a | bc, then a | b or a | c  (triples)
triples = product(range(1, 11), repeat=3)
print(first_counterexample(triples, lambda t: (t[1] * t[2]) % t[0] == 0,
                           lambda t: t[1] % t[0] == 0 or t[2] % t[0] == 0))   # (4, 2, 2)

# a true claim: if n is odd then n^2 - 1 is divisible by 8
print(first_counterexample(range(-200, 201), lambda n: n % 2 == 1, lambda n: (n * n - 1) % 8 == 0))   # None

# Polya: L(n) = (number of k <= n with an even number of prime factors) - (odd) stays <= 0 for n > 1
N = 100000
spf = list(range(N + 1))
for i in range(2, int(N ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i

def big_omega(n):
    count = 0
    while n > 1:
        n //= spf[n]
        count += 1
    return count

L, worst = 0, -N
for n in range(1, N + 1):
    L += -1 if big_omega(n) % 2 else 1
    if n > 1:
        worst = max(worst, L)
print(worst)                                                     # 0: never positive up to 100000
```

The first four searches return the counterexamples used in this lesson, and the fifth returns `None` because the claim is true. The last block finds no counterexample to the Pólya conjecture in the first 100,000 numbers, and the conjecture is false anyway: a search needs a proof behind it.

</details>

## FAQ

### How many counterexamples do I need?

One. A single case that satisfies the hypotheses and fails the conclusion disproves a "for every" claim, and a second one adds nothing. A second counterexample can still help the reader see the pattern, and it is a good check on your own reasoning.

### What if I can't find a counterexample but also can't prove it?

Keep both ideas alive. Change the question: try a smaller or more special version of the claim, try to prove it with an extra hypothesis, and test more cases. If you are stuck on a problem from a course, a likely explanation is that the claim is true and needs a proof method you haven't tried, such as contrapositive or cases. Look at the shape of the claim: the first lines of a proof come from it, as in [direct proof](../03-core-proof-methods/01-direct-proof.md).

### Can a counterexample use numbers that look strange, like zero or a negative?

Yes, when the domain allows them. The domain of the claim sets the rules. If a claim is about all integers, then $0$ and $-3$ are fair; if it is about positive integers, they are not.

### Does a disproof have to give a counterexample?

Not always. A claim of the form "for every $x$, $P(x)$" can be disproved by proving "there exists $x$ with not $P(x)$" without naming one (for example by contradiction or counting). A counterexample is the clearest version, since the reader can check it directly, and non-constructive disproofs are rare in a first course.

## Practice

### Warm-up

1\. Write the negation of each claim and give a counterexample. (a) Every prime number is odd. (b) For every real number $x$, $x^2 \ge x$. (c) If $n$ is an odd integer, then $n^2 - 1$ is divisible by 16.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Negation: some prime number is even. Counterexample: $2$, which is prime and even.
- (b) Negation: there is a real number $x$ with $x^2 < x$. Counterexample: $x = \frac{1}{2}$, with $x^2 = \frac{1}{4} < \frac{1}{2}$.
- (c) Negation: there is an odd integer $n$ for which $16 \nmid n^2 - 1$. Counterexample: $n = 3$, which is odd, and $n^2 - 1 = 8$, which is not divisible by 16.

Check: $2$ has no divisor other than 1 and 2; $\frac{1}{4} < \frac{1}{2}$; $8 = 16 \cdot \frac{1}{2}$ is not an integer multiple. (Some odd $n$ do give multiples of 16: $n = 7$ gives $48 = 16 \times 3$. One failure is enough.)

</details>

2\. Which of these are counterexamples to "if a positive integer $n$ is divisible by 6, then $n$ is divisible by 12"? (a) $n = 18$. (b) $n = 12$. (c) $n = 8$. (d) $n = 6$. Explain each.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Yes. $6 \mid 18$ and $12 \nmid 18$ ($18 = 12 + 6$).
- (b) No. The hypothesis holds, but the conclusion is true as well ($12 \mid 12$).
- (c) No. The hypothesis fails ($6 \nmid 8$), so the claim says nothing about 8.
- (d) Yes. $6 \mid 6$ and $12 \nmid 6$.

Check: a counterexample needs "divisible by 6" true and "divisible by 12" false, and only $18$ and $6$ give that pair of values.

</details>

3\. What would a disproof of each claim have to show? (a) There is a real $x$ with $x^4 < 0$. (b) For every real $x$ there is a real $y$ with $y^2 = x$. (c) Two sets $A$ and $B$ are equal. (d) There is exactly one real $x$ with $x^2 = 4$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) A proof that $x^4 \ge 0$ for every real $x$ (an example is not enough for an existence claim).
- (b) One real $x$, together with a proof that no real $y$ has $y^2 = x$. The value $x = -1$ works, because $y^2 \ge 0 > -1$ for every real $y$.
- (c) One element that is in one set and not in the other.
- (d) Two different real numbers whose squares are 4, for example $2$ and $-2$. (Or a proof that none exists, but here two exist.)

Check: the negations are (a) for every $x$, $x^4 \ge 0$; (b) there is $x$ such that for every $y$, $y^2 \ne x$; (c) some element is in exactly one of the sets; (d) there are none, or at least two.

</details>

### Standard

4\. Prove or disprove: for all integers $a$, $b$ and $c$, if $a \mid c$ and $b \mid c$, then $ab \mid c$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the definition of divides. We test equal values first. Take $a = b = 2$ and $c = 2$. The hypothesis holds: $2 \mid 2$ and $2 \mid 2$. The conclusion fails: $ab = 4$ and $4 \nmid 2$. So the claim is false.

*Disproof.* Take $a = 2$, $b = 2$ and $c = 2$. Then $a \mid c$ and $b \mid c$ hold, and $ab = 4 \nmid 2$. $\blacksquare$

Look back: another counterexample is $a = 2$, $b = 4$, $c = 4$, where $ab = 8 \nmid 4$. The claim becomes true if $a$ and $b$ have no common factor other than 1, which is a theorem about GCDs. Check: $2 = 2 \cdot 1$, and $2 = 4k$ has no integer solution.

</details>

5\. Find the flaw in this disproof. Claim: "If $n^2$ is even, then $n$ is even." "Disproof. Take $n = 3$. Then $n$ is odd, and $n^2 = 9$ is odd, so the claim fails." Is the claim true?

<details class="solution" markdown>
<summary>Solution</summary>

The flaw is that $n = 3$ does not satisfy the hypothesis. The claim is a conditional with hypothesis "$n^2$ is even", and $3^2 = 9$ is odd, so the hypothesis is false. A conditional with a false hypothesis is true, so $n = 3$ says nothing against the claim. A counterexample would need $n^2$ even and $n$ odd.

The claim is true. It is the contrapositive of "if $n$ is odd, then $n^2$ is odd", which is the forward half of Theorem 1 in [if and only if proofs](01-if-and-only-if-proofs.md#worked-examples).

Check: $n = 4$ has $n^2 = 16$ even and $n = 4$ even; $n = 5$ has $25$ odd. No integer has an even square and is odd.

</details>

6\. Prove or disprove each claim for integers. (a) $n^2 + n$ is even. (b) If $a + b$ is even, then $a$ and $b$ are both even. (c) If $ab$ is odd, then $a$ and $b$ are both odd.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) True. Write $n^2 + n = n(n + 1)$. If $n$ is even, $n = 2k$ and the product is $2k(n + 1)$. If $n$ is odd, $n + 1 = 2k$ and the product is $2kn$. Either way it is twice an integer.
- (b) False. Take $a = 1$ and $b = 3$: $a + b = 4$ is even, and $a$ and $b$ are odd. (Another is $a = b = 1$.)
- (c) True, by the contrapositive. If $a$ is even or $b$ is even, say $a = 2k$, then $ab = 2(kb)$ is even (and the case $b$ even is the same with the names swapped, since $ab = ba$). So if $ab$ is odd, neither factor is even, and both are odd.

Check: (a) $n = 3$ gives $12$ and $n = -2$ gives $2$. (b) $1 + 3 = 4$. (c) $3 \cdot 5 = 15$ and $3 \cdot 4 = 12$, which is even.

</details>

### Challenge

7\. Euler conjectured that a sum of fewer than five positive fifth powers is never a fifth power. Verify that $27^5 + 84^5 + 110^5 + 133^5 = 144^5$, and say exactly what this disproves.

<details class="solution" markdown>
<summary>Solution</summary>

Compute each power: $27^5 = 14{,}348{,}907$, $84^5 = 4{,}182{,}119{,}424$, $110^5 = 16{,}105{,}100{,}000$ and $133^5 = 41{,}615{,}795{,}893$. Their sum is $61{,}917{,}364{,}224$. Also $144^5 = 61{,}917{,}364{,}224$. The two sides are equal.

A quick partial check by last digits: the fifth powers end in $7, 4, 0, 3$ (the fifth power of a number ends in the same digit as the number itself), and $7 + 4 + 0 + 3 = 14$ ends in 4, which is the last digit of $144^5$. A last-digit match doesn't prove the equation, but a mismatch would have disproved it.

What it disproves: the conjecture says that if a sum of $k$ positive fifth powers is a fifth power, then $k \ge 5$. Here $k = 4$ and all four numbers are positive, so the hypothesis holds and the conclusion fails. It does not disprove the claim for sums of five or more fifth powers, and it says nothing about other exponents.

Check: the equality was computed in Python as integers, with no rounding.

</details>

8\. (Reviews [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md).) Write the negation of each claim, and use it to decide which claims are true and to prove your answer. (a) For every real number $x$ there is a real number $y$ with $y^2 = x$. (b) There is a real number $y$ such that for every real number $x$, $y \ge x$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Negation: there is a real $x$ such that for every real $y$, $y^2 \ne x$. This is true: take $x = -1$. For every real $y$, $y^2 \ge 0 > -1$, so $y^2 \ne -1$. So the original claim is false.

(b) Negation: for every real $y$ there is a real $x$ with $x > y$. This is true: given $y$, take $x = y + 1$. So the original claim is false.

Look back: in (a) the disproof needs an $x$ and then a proof about every $y$, which is the "one case plus a proof" shape of the table. In (b) the witness $x$ depends on $y$, as the order of the quantifiers allows. Check: for (a), $x = 4$ would not work as a witness for the negation, since $y = 2$ has $y^2 = 4$.

</details>

## Where this shows up

- The next chapter starts with [mathematical induction](../05-induction/01-mathematical-induction.md). The idea of a smallest counterexample, used in Example 5 and in the tricks above, is the engine of the well-ordering proofs in [strong induction and well-ordering](../05-induction/02-strong-induction-and-well-ordering.md). [Mixed proof practice](../07-putting-it-together/02-mixed-proof-practice.md) asks you to decide, for each claim, whether to prove or disprove it.
- In CS, a failing test or a fuzzing crash is a counterexample, and a model checker (a tool that verifies a design) returns a counterexample trace when a property fails. In the theory of computation, the pumping lemma in [Regular expressions and the pumping lemma](../../06-cs-math/06-theory-of-computation/02-regular-expressions-and-pumping-lemma.md) is used to show a language is not regular, and the argument is organized around finding a string that breaks a property.
- In economics, a theorem's assumptions are tested by counterexamples: a market with a missing assumption (a monopolist, a missing price) can show that the conclusion fails, which tells you which assumption the result depends on.
