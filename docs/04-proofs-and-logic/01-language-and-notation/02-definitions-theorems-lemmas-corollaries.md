# Definitions, theorems, lemmas and corollaries

After this lesson you can name each kind of statement in a math text, unpack a definition (even, odd, divides, prime, rational) inside a proof, and use an earlier lemma to prove a bigger result.

Before this: [what is a proof](01-what-is-a-proof.md), and the definitions, postulates and theorems of [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Which word fits each description: a statement accepted without proof; a result proved mainly to help prove a bigger one; a result that follows quickly from a theorem just proved; a statement believed to be true but not yet proved?
2. Write "$6 \mid n$" as an equation using the definition of divides. Is $6 \mid 0$ true? Is $0 \mid 6$ true?
3. A definition says "an integer $n$ is prime if $n > 1$ and the only positive divisors of $n$ are 1 and $n$". Is 1 prime? Is $-7$ prime? Is 0 prime?

<details class="solution" markdown>
<summary>Answers</summary>

1. An axiom (or postulate), a lemma, a corollary, and a conjecture.
2. It means $n = 6k$ for some integer $k$. The statement $6 \mid 0$ is true, because $0 = 6 \times 0$. The statement $0 \mid 6$ is false, because $6 = 0 \times k$ has no solution.
3. None of them. The number 1 fails $n > 1$, the numbers $-7$ and 0 fail it too.

</details>

## The idea

Think of a textbook section as a small codebase. Definitions are the type declarations: they say what a name means. Lemmas are helper functions, written once and called from several places. The theorem is the public function the section exists to provide, and a corollary is a thin wrapper around it. The analogy breaks in one place: you can't run a proof to see whether it works, so the reading order matters more than in code. A lemma has to come before the proof that uses it, and everything depends on the definitions at the top.

That is why the most common mistake in a first proof course is a half-remembered definition. Take the sentence "Let $p$ be a prime." The word "prime" looks like a label, but all of its content is in the definition. A proof about $p$ can use only what the definition says, so if you don't have it in front of you, you have nothing to work with. The first move in almost every proof is to write the definitions down, and this lesson practises that move.

## Definitions

A mathematical text is made of a small number of kinds of statements. Each kind has a name, and the name tells you how to read the statement and what you may do with it.

| Word | What it is | How you use it |
|---|---|---|
| **definition** | An agreement about what a word or symbol means. | It is not true or false. It is a rule you may unpack any time the word appears. |
| **axiom** (also **postulate**) | A statement accepted without proof, as part of the starting rules. | You may cite it as a reason. Examples: the field axioms, "two points lie on exactly one line". |
| **theorem** | A statement that has been proved, and that the author considers a main result. | You may cite it as a reason. Its proof is the part you read or write. |
| **proposition** | A proved statement, usually a smaller or more specific result than a theorem. | The same as a theorem. The choice of word is the author's. |
| **lemma** | A proved statement whose main purpose is to help prove a larger result. | Read it as a tool. Ask which later proof will call it. |
| **corollary** | A proved statement that follows quickly from a theorem or proposition just before it. | Its proof is usually one or two lines that cite that result. |
| **conjecture** | A statement that someone believes is true but that has not been proved. | Don't cite it as a reason. Goldbach's conjecture says that every even integer greater than 2 is a sum of two primes; nobody has proved it. |
| **claim** | A statement made inside a proof, which the author then proves before continuing. | It is a stepping stone in the argument, proved on the spot. |
| **remark** | A comment: a warning, a history note or a link to another idea. | It carries no proof. Read it for orientation. |
| **example** | A specific case that illustrates a definition or a theorem. | Use it to test your understanding. An example never proves a universal claim. |

Proved statements are all equally true. A lemma isn't a weaker kind of fact than a theorem; it is named for its job in the text. Some lemmas are more famous than the theorems they were written to help. The words also vary by author and by book, so treat them as signposts and not as rules.

A hypothesis is a condition a statement assumes, and the conclusion is what it promises, as in [conditional statements](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements). Every theorem has both, even when the wording hides them ("The sum of two even integers is even" means "if $m$ and $n$ are even integers, then $m + n$ is even").

### Five working definitions

These five words carry most of the proofs in the next few chapters. In all of them, a letter such as $k$ stands for an integer.

An integer $n$ is **even** if $n = 2k$ for some integer $k$, and **odd** if $n = 2k + 1$ for some integer $k$. In plain words, even numbers are the multiples of 2, and odd numbers are one more than a multiple of 2. So $10 = 2 \times 5$ is even, $-7 = 2 \times (-4) + 1$ is odd, and $0 = 2 \times 0$ is even.

For integers $a$ and $b$, we say that $a$ **divides** $b$, and write $a \mid b$, if $b = ak$ for some integer $k$. In plain words, $b$ is a multiple of $a$, so dividing $b$ by $a$ leaves no remainder. We also say that $a$ is a divisor (or factor) of $b$, and write $a \nmid b$ when $a$ does not divide $b$. So $3 \mid 12$ since $12 = 3 \times 4$, and $5 \nmid 12$. By this definition, every $a$ divides 0 (since $0 = a \times 0$), and 0 divides only 0.

An integer $p$ is **prime** if $p > 1$ and the only positive divisors of $p$ are 1 and $p$. In plain words, a prime is a whole number bigger than 1 that can't be split into a product of two smaller positive integers. So 13 is prime, since $13 = 1 \times 13$ is its only factorization into positive integers, and 15 is not, since $3 \mid 15$.

A real number $r$ is **rational** if $r = \frac{a}{b}$ for some integers $a$ and $b$ with $b \ne 0$. In plain words, a rational number is a fraction of integers. So $0.75 = \frac{3}{4}$ is rational, and so is $-5 = \frac{-5}{1}$. The same number has many such fractions ($\frac{3}{4} = \frac{6}{8}$), and the definition asks only that at least one exists.

Each of these definitions has the same shape: a defined word, followed by an equation or a condition with a "for some". The shape tells you what to do with it. The table shows both directions.

| Word | If you are given it, you get | To prove it, you must produce |
|---|---|---|
| $n$ is even | an integer $k$ with $n = 2k$ | an integer $k$ with $n = 2k$ |
| $n$ is odd | an integer $k$ with $n = 2k + 1$ | an integer $k$ with $n = 2k + 1$ |
| $a \mid b$ | an integer $k$ with $b = ak$ | an integer $k$ with $b = ak$ |
| $p$ is prime | $p > 1$, and the fact that every positive divisor of $p$ is 1 or $p$ | $p > 1$, and a proof that any positive divisor of $p$ is 1 or $p$ |
| $r$ is rational | integers $a$ and $b$ with $b \ne 0$ and $r = \frac{a}{b}$ | integers $a$ and $b$ with $b \ne 0$ and $r = \frac{a}{b}$ |

The first four rows are the same on both sides: the definition is a "for some" statement, so being given it means you get a witness, and proving it means you must provide one. The row for primes is different because it has a "for every" inside it, which you meet again in the lesson on [quantifiers](../02-logic-and-sets/04-quantifiers.md).

### "If" in a definition means "if and only if"

Definitions are written with "if": "an integer $n$ is even if $n = 2k$ for some integer $k$". Read strictly, "if" gives only one direction: whenever $n = 2k$, the number is even. It says nothing about the other numbers. So it could still be that 7 is even for some other reason.

Everyone reads a definition as saying more than it says. In a definition, "if" means "if and only if": $n$ is even exactly when $n = 2k$ for some integer $k$. That is the only way a definition can do its job, since it has to sort every integer into "even" or "not even". The number 7 is not even because there is no integer $k$ with $7 = 2k$. In a theorem, by contrast, "if" keeps its one-way meaning, as [how to read math](../../00-start-here/how-to-read-math.md#reading-a-definition) notes. The lesson [conditionals and biconditionals](../02-logic-and-sets/02-conditionals-and-biconditionals.md) treats both directions carefully.

Because definitions work in both directions, different books can use different but equivalent wording. Here is a small example.

*Proposition 1.* An integer $n$ is even if and only if $2 \mid n$.

*Proof.* By the definition of divides, $2 \mid n$ means that $n = 2k$ for some integer $k$. By the definition of even, that is exactly what it means for $n$ to be even. So the two statements say the same thing. $\blacksquare$

The proof is short because the two definitions are the same sentence in different words. It is worth having anyway: you can now switch freely between "even" and "divisible by 2".

## How to do it

### Unpacking a definition

1. Find the defined words in the hypothesis and in the conclusion. Underline them.
2. For each defined word in the hypothesis, write down its definition with fresh letters for any "for some". Don't reuse a letter that already names something else.
3. For each defined word in the conclusion, write down what you would have to show. Leave the witness blank (an unknown $l$ with $m + n = 2l$) if you don't know it yet.
4. Connect the two with algebra or with earlier results, and fill in the witness.
5. Close by saying which definition the last line matches.

Step 2 is where the first proof lesson started, and the same steps work for every definition above.

### Building on lemmas

A longer result is usually proved in layers. The definitions let you prove a lemma, the lemma helps with a theorem, and the theorem gives corollaries almost for free. Here is a chain of three about divisibility. In each, $a$, $b$ and $c$ are integers.

*Lemma 2.* If $a \mid b$, then $a \mid bm$ for every integer $m$.

What we know: $b = ak$ for some integer $k$. What we want: $bm = al$ for some integer $l$. The plan: multiply the first equation by $m$.

*Proof.* Let $a \mid b$, so $b = ak$ for an integer $k$. Let $m$ be an integer. Then $bm = (ak)m = a(km)$. Since $km$ is an integer, $a \mid bm$. $\blacksquare$

*Theorem 3.* If $a \mid b$ and $a \mid c$, then $a \mid bx + cy$ for all integers $x$ and $y$.

What we know: $a \mid b$ and $a \mid c$, and the lemma. What we want: $a$ divides $bx + cy$. The plan: the lemma says $a$ divides each of the two terms, so write each as a multiple of $a$ and add.

*Proof.* Let $x$ and $y$ be integers. By the lemma, $a \mid bx$ and $a \mid cy$, so $bx = aj$ and $cy = ak$ for integers $j$ and $k$. Then $bx + cy = aj + ak = a(j + k)$, and $j + k$ is an integer. So $a \mid bx + cy$. $\blacksquare$

*Corollary 4.* If $a \mid b$ and $a \mid c$, then $a \mid b + c$ and $a \mid b - c$.

*Proof.* Apply Theorem 3 with $x = 1$ and $y = 1$ for the sum, and with $x = 1$ and $y = -1$ for the difference. $\blacksquare$

Look back: the corollary has a one-line proof because the work was done in the lemma and the theorem. Notice the order: a corollary can't come before the result it depends on. As a check with numbers, $3 \mid 12$ and $3 \mid 21$, so $3 \mid 12 \cdot 5 + 21 \cdot (-2) = 18$, and $3 \mid 33$ and $3 \mid -9$.

### Reading a textbook section

A section written in this style repeats a pattern: definition, example, lemma, theorem with proof, corollary, remark. Here is a small one, with each part annotated below.

*Definition.* An integer $n$ is a perfect square if $n = k^2$ for some integer $k$.

*Example.* The integers $0$, $1$, $49$ are perfect squares. The integer $50$ is not.

*Theorem.* If $m$ and $n$ are perfect squares, then $mn$ is a perfect square.

*Proof.* Write $m = j^2$ and $n = k^2$. Then $mn = j^2k^2 = (jk)^2$, and $jk$ is an integer. $\blacksquare$

*Corollary.* If $n$ is a perfect square, then $n^2$ is a perfect square.

*Remark.* The sum of two perfect squares need not be a perfect square: $1 + 1 = 2$.

| Part | What to do with it |
|---|---|
| Definition | Stop and unpack it: what must a perfect square look like? Test it on $9$, $0$ and $-4$. |
| Example | Check that the claims are right. Why is $50$ not a perfect square? (No integer squares to $50$, since $7^2 = 49$ and $8^2 = 64$.) |
| Theorem | Split it into hypothesis ($m$ and $n$ are perfect squares) and conclusion ($mn$ is one). Test it with $4 \times 9 = 36 = 6^2$. |
| Proof | Cover it and try to prove the theorem yourself using the definition. Then compare. |
| Corollary | Ask which result it comes from. Here, take $m = n$ in the theorem. |
| Remark | Read it as a warning about what is not true, and check it. |

The reading routine in [how to read math](../../00-start-here/how-to-read-math.md) applies line by line, with one habit added: for every term you meet, find where it was defined. When you can't, go back until you can.

## Worked examples

<div class="example" markdown>

### Example 1: divisibility is transitive

*Proposition 5.* If $a \mid b$ and $b \mid c$, then $a \mid c$.

Step 1: the defined word is "divides", in the hypothesis (twice) and in the conclusion. We write the hypothesis as "$a \mid b$ and $b \mid c$" and the conclusion as "$a \mid c$". Test it: $3 \mid 6$ and $6 \mid 30$, and $3 \mid 30$.

Step 2: unpack the hypothesis with a fresh letter for each "for some". From $a \mid b$ there is an integer $j$ with $b = aj$. From $b \mid c$ there is an integer $k$ with $c = bk$. The two letters are different because the two statements are separate facts.

Step 3: to prove $a \mid c$ we need an integer $l$ with $c = al$.

Step 4: substitute the first equation into the second:

$$
c = bk = (aj)k = a(jk).
$$

Step 5: the product $jk$ is an integer, so $c = al$ with $l = jk$. That is the definition of $a \mid c$. $\blacksquare$

Check: $a = 3$, $b = 6$ and $c = 30$ give $j = 2$ and $k = 5$, so $l = 10$ and $3 \times 10 = 30$.

</div>

<div class="example" markdown>

### Example 2: using a chain of results

Show that if $5 \mid n$ and $5 \mid m$, then $5 \mid 3n - 7m$.

We could unpack the definitions again. The earlier results do it faster, and using them is the point of having proved them. Theorem 3 says that if $a \mid b$ and $a \mid c$, then $a \mid bx + cy$ for all integers $x$ and $y$. Take $a = 5$, $b = n$, $c = m$, $x = 3$ and $y = -7$. The hypotheses of the theorem are exactly our hypotheses, and its conclusion is $5 \mid 3n + (-7)m = 3n - 7m$.

Check with numbers: $n = 15$ and $m = 20$ give $3n - 7m = 45 - 140 = -95 = 5 \times (-19)$.

</div>

<div class="example" markdown>

### Example 3: the sum of two rationals

*Proposition 6.* If $r$ and $s$ are rational numbers, then $r + s$ is rational.

Unpack the hypothesis. There are integers $a$, $b$, $c$ and $d$ with $b \ne 0$ and $d \ne 0$, such that $r = \frac{a}{b}$ and $s = \frac{c}{d}$. To prove $r + s$ rational we need integers $p$ and $q$ with $q \ne 0$ and $r + s = \frac{p}{q}$.

Add the fractions with a common denominator:

$$
r + s = \frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}.
$$

Let $p = ad + bc$ and $q = bd$. Both are integers, because sums and products of integers are integers. The definition also asks for $q \ne 0$, and this needs a reason: $b \ne 0$ and $d \ne 0$, and a product of two nonzero numbers is nonzero by the zero-product property (Theorem 3 in [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#proving-facts-from-the-axioms)). So $r + s = \frac{p}{q}$ with $q \ne 0$, and $r + s$ is rational. $\blacksquare$

Check: $r = \frac{1}{2}$ and $s = \frac{3}{4}$ give $\frac{1 \cdot 4 + 2 \cdot 3}{2 \cdot 4} = \frac{10}{8} = \frac{5}{4}$, and $\frac{1}{2} + \frac{3}{4} = \frac{5}{4}$.

The step that is easy to skip is the check that $q \ne 0$. The definition has two conditions on the denominator, and a proof has to meet both.

</div>

<div class="example" markdown>

### Example 4: a divisor of a square (finish it yourself)

*Proposition 7.* If $a \mid b$, then $a \mid b^2$.

Steps 1 to 3: the hypothesis is "$a \mid b$" and the conclusion is "$a \mid b^2$". By the definition of divides, there is an integer $k$ with $b = ak$. To prove the conclusion we need an integer $l$ with $b^2 = al$.

Now finish the proof in two different ways: first directly, using $b = ak$, and then with a single call to Lemma 2.

<details class="solution" markdown>
<summary>Finish</summary>

Directly: $b^2 = b \cdot b = (ak)b = a(kb)$, and $kb$ is an integer, so $a \mid b^2$.

With the lemma: Lemma 2 says that if $a \mid b$, then $a \mid bm$ for every integer $m$. Taking $m = b$ gives $a \mid b \cdot b = b^2$. $\blacksquare$

Check: $a = 4$ and $b = 12$ give $k = 3$, and $b^2 = 144 = 4 \times 36$ with $36 = kb$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the integer $k$ in a definition must be an integer. The equation $3 = 2k$ has a solution, $k = \frac{3}{2}$, but it isn't an integer, so 3 is not even. A proof that produces a witness has to say why the witness is an integer, as Example 3 and the proofs above do ("$km$ is an integer").

</div>

<div class="warning" markdown>

Watch out for reversing divides. The statement $a \mid b$ means $b$ is a multiple of $a$, so $3 \mid 12$ is true and $12 \mid 3$ is false. The symbol $\mid$ is also not a division: $a \mid b$ is a statement that is true or false, while $\frac{b}{a}$ is a number. Writing "$3 \mid 12 = 4$" mixes the two.

</div>

<div class="warning" markdown>

Watch out for dropping one condition of a definition. Prime requires $p > 1$ as well as having no other divisors, and rational requires $b \ne 0$ as well as $r = \frac{a}{b}$. The number 1 has no positive divisors other than 1 and itself, so without $p > 1$ it would be prime. The reason for excluding it appears in the FAQ.

</div>

<div class="warning" markdown>

Watch out for using a result before it is proved. Proposition 5 uses only the definition of divides. If you tried to prove it by citing Corollary 4, which comes later and relies on other results, you could end up in a circle. Check each cited result: has it been proved, and does its proof avoid the claim you are proving?

</div>

Some edge cases follow from the definitions, and they are not exceptions to them. The number 0 is even, because $0 = 2 \times 0$. Every integer divides 0, and 0 divides only 0, so $0 \mid 0$ is true even though $\frac{0}{0}$ is undefined. A negative integer can be odd ($-7 = 2 \times (-4) + 1$) or even ($-6 = 2 \times (-3)$), and can have divisors ($-4 \mid 12$ because $12 = (-4) \times (-3)$). No negative integer is prime in this book, because primes must be greater than 1. The same rational number can be written many ways, and a proof about "a rational $r$" can pick any one of them.

## Tricks and shortcuts

Keep a one-page list of the definitions you have met, written from memory and checked against the text. Nearly every proof in this folder begins by pulling one of them off that page.

When a hypothesis contains a defined word, write the unpacked version on the first line of your scratch work before you think about anything else. When a conclusion does, write the target version on the last line. The proof is the path from the first line to the last, and with both ends fixed the middle is usually algebra.

When you read a lemma, ask where it will be called. If the next theorem's proof has a gap you can fill with the lemma, you understand both. If you can't see any use for the lemma, reread the theorem's statement; the lemma and the theorem usually share a pattern.

## In code

A definition with a "for some" in it becomes a function that finds the witness. The code below follows the definitions word for word. The last test is a computer check of Corollary 4 over a box of integers. It supports the corollary and doesn't prove it.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction

def even_witness(n):
    """Return k with n == 2*k, or None if no such integer exists."""
    return n // 2 if n % 2 == 0 else None

def divides(a, b):
    """a | b means b == a*k for some integer k."""
    return b == 0 if a == 0 else b % a == 0

def is_prime(n):
    """n > 1, and the only positive divisors of n are 1 and n."""
    return n > 1 and [d for d in range(1, n + 1) if divides(d, n)] == [1, n]

print(even_witness(10), even_witness(7), even_witness(-6), even_witness(0))   # 5 None -3 0
print(divides(3, 12), divides(5, 12), divides(6, 0), divides(0, 6), divides(0, 0))
# True False True False True
print([n for n in range(-3, 20) if is_prime(n)])      # [2, 3, 5, 7, 11, 13, 17, 19]
print(Fraction(2, 4) == Fraction(1, 2), Fraction(1, 2) + Fraction(3, 4))      # True 5/4

R = range(-30, 31)
print(all(divides(a, b + c) and divides(a, b - c)
          for a in R for b in R for c in R
          if divides(a, b) and divides(a, c)))        # True
```

The function `divides(0, 0)` returns `True` and `divides(0, 6)` returns `False`, matching the edge cases above. Python's `%` gives remainder 0 for negative divisors too, so `divides(-4, 12)` works. The last test tries all 226,981 triples $(a, b, c)$ in the box and finds no failure, while the proof of Corollary 4 covers all integers.

</details>

## FAQ

### Why do texts use so many words for "something we proved"?

They are signposts for the reader. A theorem is the result you should remember, a lemma is a tool for a specific proof, a corollary is a near-free consequence, and a proposition sits in between. All four are proved statements and equally true. The sorting is the author's judgment, and two books can label the same result differently, so don't read anything into the label except its role.

### Why does a definition not need a proof?

A definition is a decision about how to use a word, not a claim about the world, so nothing in it can be true or false. What does need checking is that a definition makes sense. For instance, a definition that says "the number $x$ such that $x^2 = 4$" is faulty, because there are two such numbers, 2 and $-2$. A definition that picks a single object has to show that one exists and that only one does, which is the topic of [existence and uniqueness proofs](../04-more-proof-methods/02-existence-and-uniqueness-proofs.md).

### Why is 1 not prime?

Because of what primes are used for. Every integer greater than 1 factors into primes in exactly one way (apart from the order), and this fact, covered in [primes and unique factorization](../../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md), is used constantly. If 1 were prime, then $6 = 2 \times 3 = 1 \times 2 \times 3 = 1 \times 1 \times 2 \times 3$ would be different factorizations, and every theorem would need the extra words "other than 1". Mathematicians chose a definition that avoids that.

### What if two books define a word differently?

First check whether the definitions are equivalent, meaning each implies the other. Proposition 1 shows that "even" defined as $n = 2k$ and as $2 \mid n$ are equivalent. If they really differ, as the natural numbers do (some books start at 1, this one at 0), follow the book you are reading, and check its notation page before you rely on a result.

## Practice

### Warm-up

1\. Name each statement as an axiom, a definition, a conjecture, a lemma or a theorem, and give a reason. (a) "An integer $n$ is odd if $n = 2k + 1$ for some integer $k$." (b) "Every even integer greater than 2 is the sum of two primes." (c) "If two lines cross, the vertical angles are equal." (d) "Any two real numbers $a$ and $b$ satisfy $a + b = b + a$."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) A definition. It fixes the meaning of "odd".
- (b) A conjecture. It is Goldbach's conjecture, believed true but not proved.
- (c) A theorem. It was proved in [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#a-first-proof-vertical-angles-are-equal) from the linear pair postulate.
- (d) An axiom, the commutative property of addition (A2) in the field axioms.

Check: only (c) comes with a proof from earlier statements, and only (b) is open.

</details>

2\. Write each statement with the definitions unpacked, producing the witness. (a) "$9 \mid 63$." (b) "$0.75$ is rational." (c) "$-7$ is odd." (d) "13 is prime."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $63 = 9 \times 7$, so the witness is $k = 7$.
- (b) $0.75 = \frac{3}{4}$ with $a = 3$ and $b = 4 \ne 0$.
- (c) $-7 = 2 \times (-4) + 1$, so $k = -4$.
- (d) We have $13 > 1$. A positive divisor of 13 can't be bigger than 13, and none of $2, 3, \dots, 12$ divides 13: dividing 13 by $2, 3, \dots, 12$ leaves the remainders $1, 1, 1, 3, 1, 6, 5, 4, 3, 2, 1$. So the only positive divisors are 1 and 13.

Check: $9 \times 7 = 63$, $3 \div 4 = 0.75$, $2 \times (-4) + 1 = -7$, and a program listing the divisors of 13 gives $[1, 13]$.

</details>

3\. Decide whether each statement is true, using only the definitions: (a) $0$ is even, (b) $0 \mid 0$, (c) $0 \mid 5$, (d) $5 \mid -15$, (e) $1$ is prime, (f) $\frac{0}{7}$ is rational.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) True: $0 = 2 \times 0$.
- (b) True: $0 = 0 \times k$ holds for every integer $k$, for instance $k = 1$.
- (c) False: $5 = 0 \times k$ has no solution, since $0 \times k = 0$.
- (d) True: $-15 = 5 \times (-3)$.
- (e) False: prime requires $p > 1$, and $1 > 1$ is false.
- (f) True: $\frac{0}{7}$ has integer numerator 0 and denominator $7 \ne 0$. It equals the number 0.

Check (d): $5 \times (-3) = -15$. Check (b) against (c): the definition allows $0 \mid 0$ but not $0 \mid 5$, which matches "0 divides only 0".

</details>

### Standard

4\. Prove that if $n$ is an odd integer, then $n^2$ is odd.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $n = 2k + 1$ for some integer $k$. What we want: $n^2 = 2l + 1$ for some integer $l$. The plan: square, and pull a factor of 2 out of every term except the last.

*Proof.* Let $n$ be an odd integer. By the definition of odd, $n = 2k + 1$ for some integer $k$. Then

$$
n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1.
$$

The number $2k^2 + 2k$ is an integer, because $k$ is. So $n^2$ has the form $2l + 1$ with $l = 2k^2 + 2k$, and $n^2$ is odd. $\blacksquare$

Check: $n = 7$ has $k = 3$, $l = 2 \cdot 9 + 6 = 24$, and $2 \times 24 + 1 = 49 = 7^2$.

</details>

5\. Find the error in this proof, and say whether the claim is true. Claim: if $a \mid c$ and $b \mid c$, then $ab \mid c$. "Proof. Let $c = ak$ and $c = bl$ for integers $k$ and $l$. Multiplying the two equations, $c^2 = (ak)(bl) = ab(kl)$. So $ab \mid c^2$, and therefore $ab \mid c$."

<details class="solution" markdown>
<summary>Solution</summary>

The proof is correct up to "$ab \mid c^2$". The last step, "therefore $ab \mid c$", doesn't follow: knowing that a number divides $c^2$ does not mean it divides $c$. For example, $4 \mid 36 = 6^2$, but $4 \nmid 6$.

The claim itself is false. Take $a = 2$, $b = 4$ and $c = 12$. Then $2 \mid 12$ and $4 \mid 12$, but $ab = 8$ and $8 \nmid 12$, since $12 = 8 \times 1 + 4$. The statement does hold when $a$ and $b$ have no common factor other than 1, but that needs more tools than these definitions, and it is proved in [GCD and Euclid's algorithm](../../06-cs-math/02-number-theory/02-gcd-and-euclids-algorithm.md).

Check: $12 \div 2 = 6$, $12 \div 4 = 3$, and $12 \div 8 = 1.5$, which is not an integer.

</details>

6\. Prove that if $a \mid b$ and $a \mid c$, then $a \mid b^2 - c^2$. Cite the lemma, theorem or corollary from this lesson each time you use one.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $a \mid b$ and $a \mid c$. What we want: $a \mid b^2 - c^2$. The plan: show that $a$ divides each square with Proposition 7, then subtract with Corollary 4.

*Proof.* Let $a \mid b$ and $a \mid c$. By Proposition 7, $a \mid b^2$ and $a \mid c^2$. By Corollary 4, applied to $b^2$ and $c^2$, $a \mid b^2 - c^2$. $\blacksquare$

Check: $a = 3$, $b = 12$ and $c = 21$ give $b^2 - c^2 = 144 - 441 = -297 = 3 \times (-99)$.

</details>

### Challenge

7\. Prove that if $r$ and $s$ are rational, then $rs$ is rational, and that if $r$ is rational and $r \ne 0$, then $\frac{1}{r}$ is rational.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $r = \frac{a}{b}$ and $s = \frac{c}{d}$ with integers $a$, $b$, $c$, $d$ and $b \ne 0$, $d \ne 0$. What we want: a fraction of integers with nonzero denominator for each of $rs$ and $\frac{1}{r}$. The plan: multiply the fractions, and flip the fraction, checking the denominators each time.

*Proof of the first claim.* Let $r = \frac{a}{b}$ and $s = \frac{c}{d}$ as above. Then $rs = \frac{ac}{bd}$. The numerator $ac$ and the denominator $bd$ are integers. Since $b \ne 0$ and $d \ne 0$, the zero-product property gives $bd \ne 0$. So $rs$ is rational.

*Proof of the second claim.* Let $r = \frac{a}{b}$ with $b \ne 0$, and suppose $r \ne 0$. If $a$ were 0, then $r = \frac{0}{b} = 0$, so $a \ne 0$. Then $\frac{1}{r} = \frac{b}{a}$, where $b$ and $a$ are integers and $a \ne 0$. So $\frac{1}{r}$ is rational. $\blacksquare$

Look back: the condition $r \ne 0$ is used in a single place, to make the new denominator nonzero. Without it the claim is meaningless, since $\frac{1}{0}$ is undefined. Check: $r = \frac{3}{4}$ and $s = -\frac{2}{5}$ give $rs = \frac{-6}{20} = -\frac{3}{10}$ and $\frac{1}{r} = \frac{4}{3}$.

</details>

8\. (Reviews [factors, multiples and primes](../../01-elementary/08-factors-multiples-and-primes.md).) Prove that 2 is the only even prime.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: the definition of prime, and the definition of even. We want two things: 2 is prime, and every even prime equals 2. The plan: check 2 against the definition, then take an arbitrary even prime and show that it must be 2.

*Proof.* The number 2 is greater than 1, and its positive divisors are 1 and 2, since a positive divisor of 2 can't exceed 2. So 2 is prime, and 2 is even because $2 = 2 \times 1$.

Now let $p$ be an even prime. Since $p$ is even, $p = 2k$ for some integer $k$, so $2 \mid p$, and 2 is a positive divisor of $p$. Since $p$ is prime, its only positive divisors are 1 and $p$. So $2 = 1$ or $2 = p$. The first is false, so $p = 2$. $\blacksquare$

Check: the even numbers 4, 6, 8, 10 are all composite ($4 = 2 \times 2$, $6 = 2 \times 3$, and so on). A computer search of the evens up to 1,000 finds no even prime other than 2.

</details>

## Where this shows up

- The next lesson, [proof language: let, suppose, WLOG](03-proof-language-let-suppose-wlog.md), lists the phrases that connect these definitions and results in a written proof. Divisibility returns in [divisibility and modular arithmetic](../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md), where Theorem 3 above is the first tool.
- Every CS theory course begins with definitions that work like the ones here. A DFA, a language, a Turing machine and the class P are all defined with a list of conditions, and proofs about them start by unpacking the definition (finite automata: DFA and NFA<!-- link: ../../06-cs-math/06-theory-of-computation/01-finite-automata-dfa-and-nfa.md -->).
- In economics, the assumptions on a consumer's preferences, such as completeness and transitivity, play the part of axioms, and the results about demand are theorems proved from them ([utility and indifference curves](../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md)).
