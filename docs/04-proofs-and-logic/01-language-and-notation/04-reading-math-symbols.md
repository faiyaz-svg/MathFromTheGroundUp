# Reading math symbols

After this lesson you can read a dense symbolic sentence aloud, translate it into English and back, and decide whether a written proof should use a symbol or a word.

Before this: [proof language: let, suppose, WLOG](03-proof-language-let-suppose-wlog.md), and the set notation in [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md). The full symbol list is the [symbols and notation](../../reference/symbols-and-notation.md) reference page; this lesson teaches you how to read what is on it.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Read aloud and translate into a plain English sentence: $\forall x \in \mathbb{R},\ x^2 \ge 0$. Is it true?
2. Evaluate $\lfloor -2.5 \rfloor$, $\sum_{i=1}^{4} i^2$ and $\prod_{i=1}^{3} 2i$.
3. Write in symbols: "there is an integer $k$ with $n = 3k$". What shorter symbol says the same thing?

<details class="solution" markdown>
<summary>Answers</summary>

1. "For every real number $x$, $x$ squared is at least 0." It is true.
2. The floor rounds down, so $\lfloor -2.5 \rfloor = -3$. The sum is $1 + 4 + 9 + 16 = 30$. The product is $2 \cdot 4 \cdot 6 = 48$.
3. $\exists k \in \mathbb{Z},\ n = 3k$. The shorter form is $3 \mid n$.

</details>

## The idea

A line of symbols is a sentence with the words squeezed out. It looks harder than it is, because the grammar of the symbols is small and regular. Almost every symbol plays one of four roles, and knowing the role tells you how to read it.

Some expressions name an object: $3$, $x^2$, $\mathbb{R}$, $A \cup B$, $\sum_{i=1}^{n} i$. These are the nouns. Some symbols are relations that glue two objects into a statement: $=$, $<$, $\in$, $\subseteq$, $\mid$. A statement is the thing that is true or false, and it is the verb phrase of the sentence. Connectives such as $\wedge$ ("and"), $\vee$ ("or"), $\neg$ ("not") and $\Rightarrow$ ("implies") join statements into bigger statements. And quantifiers, $\forall$ and $\exists$, say how many objects a statement is about.

The first test for any expression is whether it is an object or a statement, as the reference page says in "How to read a symbol you don't know". The expression $12 / 3$ is an object, the number 4. The expression $3 \mid 12$ is a statement, and a true one. A line such as "$3 \mid 12 = 4$" mixes the two kinds, like a program that adds a boolean to a string. Most symbol errors in proofs are of this type.

## Definitions

An **operation symbol** takes objects and builds a new object: $+$, $\cup$, $\circ$, $\sum$, $\lfloor \cdot \rfloor$. A **relation symbol** takes objects and makes a statement: $=$, $\le$, $\in$, $\subseteq$, $\mid$, $\equiv$. In plain words, an operation gives you a thing, and a relation gives you a claim about things.

A **bound variable** is a letter that exists only inside the expression that introduces it, such as $i$ in $\sum_{i=1}^{n} i$ or $x$ in "for every $x$". A **free variable** is a letter whose meaning comes from outside, such as $n$ in the same sum. In plain words, a bound variable is like a loop counter or a function parameter: it has no value outside, and renaming it changes nothing. So $\sum_{i=1}^{n} i$ and $\sum_{j=1}^{n} j$ are the same number, and "for every $x$, $x^2 \ge 0$" says the same as "for every $y$, $y^2 \ge 0$". Using a bound letter outside its expression is the same mistake as using a variable after its scope has ended.

## How to do it

### Reading a dense sentence

1. Find the main relation or connective. It is the symbol at the outermost level, not inside a bracket or after a quantifier.
2. Read the quantifiers from left to right, each with its set: "for every $x$ in $\mathbb{R}$, there is a $y$ in $\mathbb{R}$ such that ...". The order carries meaning.
3. Read the remaining piece as a statement, using the "say it" column below.
4. Smooth the words into a plain sentence, but keep every condition.
5. Test it. Is it true? Try a small example. If you can't say what a symbol means, look it up in the [reference](../../reference/symbols-and-notation.md) before going on.

### Translating English into symbols

1. Find the objects and say what set each lives in: integers, reals, sets.
2. Find the quantity words ("every", "some", "exactly one", "no") and write the quantifiers in the order the sentence uses them.
3. Write the condition, using relations and connectives.
4. Add brackets so that the grouping is clear: write $\forall x\,(P(x) \Rightarrow Q(x))$ and not $\forall x\ P(x) \Rightarrow Q(x)$.
5. Read your symbols back aloud. If the sentence you hear isn't the one you started with, fix the symbols.

### A reading guide

The tables list what to say and what to watch for. They do not repeat the LaTeX or the lesson where each symbol is taught: the [reference page](../../reference/symbols-and-notation.md) has both.

Quantifiers and logic:

| Symbol | Say it | Watch for |
|---|---|---|
| $\forall x \in A,\ P(x)$ | for every $x$ in $A$, $P$ of $x$ | The set matters. If $A$ is empty the statement is true, because there is nothing to fail. |
| $\exists x \in A,\ P(x)$ | there exists an $x$ in $A$ such that $P$ of $x$ | "At least one". It does not say "exactly one". |
| $\exists!\, x \in A,\ P(x)$ | there exists exactly one $x$ in $A$ such that $P$ of $x$ | Two claims in one: existence and uniqueness. |
| $\neg P$ | not $P$ | The negation of a "for every" statement is a "there exists" statement. |
| $P \wedge Q$, $P \vee Q$ | $P$ and $Q$; $P$ or $Q$ | Math's "or" is inclusive: it is true when both hold. |
| $P \Rightarrow Q$ | $P$ implies $Q$; if $P$ then $Q$ | False only when $P$ is true and $Q$ is false. It is a statement, not a step. |
| $P \Leftrightarrow Q$ | $P$ if and only if $Q$ | Both directions: $P \Rightarrow Q$ and $Q \Rightarrow P$. |
| $P \equiv Q$ | $P$ is logically equivalent to $Q$ | The two have the same truth value in every case. In other places $\equiv$ means congruence or "identically equal". |
| $:=$ | is defined to be | $f(x) := x^2 + 1$ gives a name. It isn't an equation to solve. |
| $\therefore$ | therefore | Words are better in a proof: "so", "thus". |

Sets and number systems:

| Symbol | Say it | Watch for |
|---|---|---|
| $x \in A$, $x \notin A$ | $x$ is in $A$; $x$ is not in $A$ | The left side is an element and the right side is a set. |
| $A \subseteq B$ | $A$ is a subset of $B$ | The left side is a set. $1 \subseteq \{1, 2\}$ is not even a statement. |
| $\{x \in A : P(x)\}$ | the set of $x$ in $A$ such that $P$ of $x$ | The colon (or a bar) means "such that". Name the ground set $A$ before it. |
| $\{2k : k \in \mathbb{Z}\}$ | the set of all $2k$ with $k$ an integer | The expression comes first and the range of the letter after. |
| $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ | the natural numbers, integers, rationals, reals | This book's $\mathbb{N}$ starts at 0. Check other books. |
| $\emptyset$ | the empty set | $\emptyset$ has no elements, and $\{\emptyset\}$ has one. |
| $a \mid b$, $a \nmid b$ | $a$ divides $b$; $a$ does not divide $b$ | A statement. The multiple is on the right. $3 \mid 12$ is true and $12 \mid 3$ is false. |
| $a \equiv b \pmod{n}$ | $a$ is congruent to $b$ mod $n$ | It means $n \mid a - b$. |

Sums, functions and indices:

| Symbol | Say it | Watch for |
|---|---|---|
| $\sum_{i=1}^{n} a_i$ | the sum of $a$ sub $i$, for $i$ from 1 to $n$ | The letter $i$ is bound. A sum with no terms is 0. |
| $\prod_{i=1}^{n} a_i$ | the product of $a$ sub $i$, for $i$ from 1 to $n$ | A product with no terms is 1. |
| $f \colon A \to B$ | $f$ is a function from $A$ to $B$ | $A$ is the domain, $B$ the codomain. The outputs may fill only part of $B$. |
| $x \mapsto x^2$ | $x$ maps to $x$ squared | The rule of a function for one input. The arrow is different from the one in $f \colon A \to B$. |
| $f \circ g$ | $f$ composed with $g$; $f$ after $g$ | Apply $g$ first: $(f \circ g)(x) = f(g(x))$. |
| $\lfloor x \rfloor$ | the floor of $x$ | Round down: $\lfloor 3.7 \rfloor = 3$ and $\lfloor -3.7 \rfloor = -4$. |
| $a_i$, $x_{i,j}$ | $a$ sub $i$; $x$ sub $i$ comma $j$ | A subscript is an index, a label that picks one item from a list. It is not an exponent. |

Subscripts and superscripts are easy to confuse. In $x_2$ the 2 picks the second entry of a list; in $x^2$ it squares. The notation $f^{-1}$ is the inverse function and not $\frac{1}{f}$, and $f^{(n)}$ is sometimes the $n$-th derivative and sometimes $n$ repeated compositions, so look for the author's note.

### Symbols or words in a written proof

This book's rule is to write the logic in words and to keep symbols for formulas. A proof is prose that a person reads. The words "for every", "there exists", "implies" and "therefore" carry the flow of the argument, and symbols in their place make the paragraph read like a list of codes. The quantifier and implication symbols appear when the symbols themselves are the subject, as in this lesson and the logic lessons, and in your own scratch work.

| Symbols in prose | Words in prose |
|---|---|
| $\forall n \in \mathbb{Z},\ \exists k \in \mathbb{Z}$ s.t. $n = 2k \Rightarrow n$ even | If an integer $n$ equals $2k$ for some integer $k$, then $n$ is even. |
| $m, n$ even $\therefore m + n$ even | Since $m$ and $n$ are even, $m + n$ is even. |
| $x \in A \wedge x \in B$ | The element $x$ is in both $A$ and $B$. |

Formulas, equations and set expressions stay as symbols, because that is what they are for. Never begin a sentence with a symbol, and put a word between two displayed formulas. In a proof, $\in$ and $\subseteq$ work well inside a formula ("$x \in A \cup B$"), and "belongs to" is also fine in prose.

## Worked examples

<div class="example" markdown>

### Example 1: reading a symbolic theorem

Read and translate:

$$
\forall a, b, c \in \mathbb{Z},\ \bigl( (a \mid b \wedge a \mid c) \Rightarrow a \mid (b + c) \bigr).
$$

Step 1: the main structure is a quantifier on the outside, so the sentence begins "for every". The main connective inside the brackets is $\Rightarrow$, with $\wedge$ in its hypothesis.

Step 2: the quantifiers are $\forall a, b, c \in \mathbb{Z}$, which reads "for all integers $a$, $b$ and $c$".

Step 3: the statement inside says "if ($a$ divides $b$ and $a$ divides $c$), then $a$ divides $b + c$".

Step 4: smoothed out, "if an integer divides two integers, then it divides their sum". This is part of Corollary 4 in [definitions, theorems, lemmas and corollaries](02-definitions-theorems-lemmas-corollaries.md#building-on-lemmas).

Step 5: test it with $a = 3$, $b = 12$ and $c = 21$: $3 \mid 12$ and $3 \mid 21$, and $3 \mid 33$.

Now unpack "divides" with the definition. The statement says: for all integers $a$, $b$, $c$, if (there is an integer $j$ with $b = aj$) and (there is an integer $k$ with $c = ak$), then there is an integer $l$ with $b + c = al$. The letters $j$, $k$ and $l$ are bound variables. The proof of the corollary names them freely, and renaming them changes nothing.

</div>

<div class="example" markdown>

### Example 2: the order of quantifiers

Compare two sentences that differ in the order of the quantifiers:

$$
\text{(A) } \forall x \in \mathbb{R}\ \exists y \in \mathbb{R},\ y > x
\qquad\qquad
\text{(B) } \exists y \in \mathbb{R}\ \forall x \in \mathbb{R},\ y > x.
$$

Read left to right. Sentence (A): "for every real number $x$, there is a real number $y$ bigger than $x$." Sentence (B): "there is a real number $y$ that is bigger than every real number $x$."

(A) is true. *Proof.* Let $x$ be a real number. Take $y = x + 1$. Then $y > x$. $\blacksquare$

(B) is false. *Proof.* Suppose, to get a contradiction, that such a $y$ exists. Apply the statement "for every $x$, $y > x$" to the particular real number $x = y$. It says $y > y$, which is false. So no such $y$ exists. $\blacksquare$

Look back: in (A) the number $y$ is allowed to depend on $x$, as in $y = x + 1$. In (B) one $y$ has to work for all $x$ at once. Swapping two quantifiers changes the meaning, which is why quantifiers are read in order. Check with numbers: for $x = 7$, (A) gives $y = 8$; no single number beats both 7 and 8 and 9 and so on.

</div>

<div class="example" markdown>

### Example 3: from English to symbols and back

Write each sentence in symbols, then read it back.

- (a) "Every multiple of 6 is a multiple of 3." In symbols: $\forall n \in \mathbb{Z},\ (6 \mid n \Rightarrow 3 \mid n)$.
- (b) "The set of even integers." Two correct forms: $\{n \in \mathbb{Z} : \exists k \in \mathbb{Z},\ n = 2k\}$ and $\{2k : k \in \mathbb{Z}\}$.
- (c) "There is exactly one real number $x$ with $x + 3 = 5$." In symbols: $\exists!\, x \in \mathbb{R},\ x + 3 = 5$.

Reading (a) back: "for every integer $n$, if 6 divides $n$ then 3 divides $n$." The sentence says "multiple of 6" and "6 divides n" is the same thing. Sentence (a) is true, and here is the proof.

*Proof of (a).* Let $n$ be an integer with $6 \mid n$. Then $n = 6k$ for some integer $k$, so $n = 3(2k)$, and $2k$ is an integer. Hence $3 \mid n$. $\blacksquare$

Reading (c) back: the unique solution is $x = 2$. Check by substitution: $2 + 3 = 5$. For uniqueness, if $x + 3 = 5$, then subtracting 3 gives $x = 2$. The symbol $\exists!$ promises both parts.

</div>

<div class="example" markdown>

### Example 4: a double sum (finish it yourself)

Evaluate

$$
\sum_{i=1}^{3} \sum_{j=1}^{2} i \cdot j.
$$

Read it from the inside out. The inner sum has $i$ as a free variable and $j$ as its bound variable: $\sum_{j=1}^{2} i \cdot j = i \cdot 1 + i \cdot 2 = 3i$. So the outer sum is $\sum_{i=1}^{3} 3i$.

Finish the evaluation, and find a second way to get the same number.

<details class="solution" markdown>
<summary>Finish</summary>

The outer sum is $3 \cdot 1 + 3 \cdot 2 + 3 \cdot 3 = 18$.

A second way: the double sum is the sum of all products $i \cdot j$ with $i \in \{1, 2, 3\}$ and $j \in \{1, 2\}$, which factors as $(1 + 2 + 3)(1 + 2) = 6 \times 3 = 18$.

Check: the six products are $1, 2, 2, 4, 3, 6$, and they add to 18.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: $\Rightarrow$ is not the same as "therefore". The expression $P \Rightarrow Q$ is one statement, and it can be false. A chain such as "$x^2 = 9 \Rightarrow x = 3 \Rightarrow x + 1 = 4$" claims each step follows from the one before it, and the first step is wrong: $x^2 = 9$ also allows $x = -3$. When you mean "so", write "so" or "therefore" in words. Use $\Rightarrow$ for a claim you want to be checked, and use $\Leftrightarrow$ only when both directions hold.

</div>

<div class="warning" markdown>

Watch out for symbols with more than one meaning. The bar means "divides" in $a \mid b$, "such that" in some books' set-builder notation, and absolute value in $\lvert x \rvert$; the symbol $\lvert A \rvert$ is the size of a set. The symbol $\equiv$ is logical equivalence, congruence and "identically equal". The symbol $\subset$ means $\subseteq$ in some books and "proper subset" in others, which is why this book avoids it. Read the notation section of each book before you rely on a symbol.

</div>

<div class="warning" markdown>

Watch out for unbracketed quantifiers. The line $\forall x\ P(x) \Rightarrow Q(x)$ can mean "for every $x$, if $P(x)$ then $Q(x)$" or "if $P(x)$ holds for every $x$, then $Q(x)$". Write the brackets: $\forall x\,(P(x) \Rightarrow Q(x))$.

</div>

<div class="warning" markdown>

Watch out for using a bound variable outside its expression. After writing $\sum_{i=1}^{4} i = 10$, the letter $i$ has no meaning, so "$10 \cdot i$" on the next line is an error. Either the letter is introduced again, or the formula should not refer to it.

</div>

Empty cases are part of the notation. A sum with no terms, such as $\sum_{i=1}^{0} a_i$, equals 0, and a product with no terms equals 1. A statement $\forall x \in \emptyset,\ P(x)$ is true, and $\exists x \in \emptyset,\ P(x)$ is false. These follow from the definitions, as the lesson on [sets and set operations](../02-logic-and-sets/06-sets-and-set-operations.md) shows.

## Tricks and shortcuts

Say every symbol aloud before you try to understand the sentence. If you can read it aloud as English, you can usually reason about it. If a symbol won't turn into words, look it up.

Keep a "mirror" in mind: a statement beginning with $\forall$ is a promise about all objects, so one counterexample breaks it. A statement beginning with $\exists$ is a promise that something exists, so one example proves it. This is the table from [what is a proof](01-what-is-a-proof.md#definitions), in symbols. The next lessons develop it: the negation of "for every $x$, $P(x)$" is "there exists an $x$ where $P(x)$ fails", as covered in [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md).

When you meet a long formula, bracket it from the inside out and name each piece: "this is the sum of the first $n$ odd numbers, this is a set of divisors". A name for each piece turns an unreadable line into three short statements.

## In code

Python's comprehension syntax is close to set-builder notation, and `sum`, `prod`, `all`, `any` are $\sum$, $\prod$, $\forall$ and $\exists$ over a finite range. The last two lines show a limit of this: a finite range can make a false statement about all integers look true.

<details class="code" markdown>
<summary>In code</summary>

```python
from math import floor, prod

print(sorted({n for n in range(-10, 11) if n * n < 20}))        # {n in Z : n^2 < 20}: -4, -3, ..., 4
print(sum(i * i for i in range(1, 5)), prod(2 * i for i in range(1, 4)))   # 30 48
print(floor(-3.7), floor(3.7))                                  # -4 3
print(sum(i * j for i in range(1, 4) for j in range(1, 3)))     # 18
print(sum(i for i in range(1, 1)), prod(i for i in range(1, 1)))          # 0 1: empty sum, empty product

f = lambda x: x * x
g = lambda x: x + 1
compose = lambda f, g: lambda x: f(g(x))
print(compose(f, g)(2), compose(g, f)(2))                       # 9 5: f after g is not g after f

X, Y = range(-10, 11), range(-20, 21)
print(all(any(y > x for y in Y) for x in X))                    # True: for every x there is a y > x
print(any(all(y > x for x in X) for y in Y))                    # True here, but false over the integers
```

The last line is True because the range `Y` includes numbers bigger than everything in `X`, such as 11. Over all the integers, Example 2 proves that no such $y$ exists. A check on a finite range can mislead, which is why the proof is needed.

</details>

## FAQ

### Is $\Rightarrow$ the same as "therefore"?

No. The symbol $P \Rightarrow Q$ is a single statement, "if $P$ then $Q$", which can be true or false. "Therefore" announces that $Q$ has been established because $P$ was. In a proof, you write "since $P$, we have $Q$" in words. The lesson [conditionals and biconditionals](../02-logic-and-sets/02-conditionals-and-biconditionals.md) works out when $P \Rightarrow Q$ is true.

### Why are there several symbols for the same idea?

Different fields settled on different conventions. Logic books write $\to$ for implication, many math books write $\Rightarrow$, and some write $\supset$. A set difference can be $A \setminus B$ or $A - B$. The lessons in this book use one symbol per idea, and the reference page lists the common alternatives, so you can read other books.

### Do I need to memorize the LaTeX commands?

No. You need to recognize the symbols and know what they say. If you ever have to type one, the reference page lists the command, and a tool such as Detexify finds it from a drawing.

### Why not write everything in symbols, since they are more exact?

Symbols are exact about the formula but silent about the argument. The word "since" tells the reader a reason follows, and the word "suppose" tells them an assumption starts. A page of $\forall$ and $\Rightarrow$ takes those signals away and is slower to check. That is why this book keeps the logic in words and the formulas in symbols.

## Practice

### Warm-up

1\. Read each expression aloud as a plain English sentence, and say whether it is true. (a) $\exists n \in \mathbb{N},\ n^2 = 49$ (b) $A \subseteq B$ where $A = \{1, 2\}$ and $B = \{1, 2, 3\}$ (c) $\{x \in \mathbb{Z} : 2 \mid x\}$ (d) $f \colon \mathbb{R} \to \mathbb{R}$ given by $x \mapsto 3x - 1$, evaluated at 2.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) "There is a natural number whose square is 49." True, with $n = 7$.
- (b) "$A$ is a subset of $B$." True: 1 and 2 are both in $B$.
- (c) "The set of integers $x$ such that 2 divides $x$." This is the set of even integers. It is a set and not a statement, so it is neither true nor false.
- (d) "The function $f$ from the reals to the reals sends $x$ to $3x - 1$." At 2 it gives $3 \cdot 2 - 1 = 5$.

Check (a): $7^2 = 49$. Check (d): $f(2) = 5$.

</details>

2\. Evaluate: (a) $\lfloor -0.2 \rfloor$ and $\lceil -0.2 \rceil$, (b) $\sum_{k=0}^{4} 2^k$, (c) $\prod_{k=1}^{4} k$, (d) $(f \circ g)(3)$ for $f(x) = 2x$ and $g(x) = x - 5$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The floor rounds down, so $\lfloor -0.2 \rfloor = -1$. The ceiling rounds up, so $\lceil -0.2 \rceil = 0$.
- (b) $1 + 2 + 4 + 8 + 16 = 31$.
- (c) $1 \cdot 2 \cdot 3 \cdot 4 = 24$, which is $4!$.
- (d) Apply $g$ first: $g(3) = -2$, then $f(-2) = -4$.

Check (b): the sum of powers of 2 from $2^0$ to $2^4$ is one less than $2^5 = 32$. Check (d): $(f \circ g)(x) = 2(x - 5)$, and $2(3 - 5) = -4$.

</details>

3\. Write in symbols: (a) every natural number is an integer, (b) some real number has square 2, (c) there is exactly one real number $x$ with $2x = 6$, (d) $n$ is a multiple of 5.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $\forall n \in \mathbb{N},\ n \in \mathbb{Z}$, or more briefly $\mathbb{N} \subseteq \mathbb{Z}$.
- (b) $\exists x \in \mathbb{R},\ x^2 = 2$.
- (c) $\exists!\, x \in \mathbb{R},\ 2x = 6$.
- (d) $5 \mid n$, or $\exists k \in \mathbb{Z},\ n = 5k$.

Check by reading back: (c) says "there is exactly one real $x$ with $2x = 6$", and that $x$ is 3.

</details>

### Standard

4\. Translate each sentence, decide whether it is true, and prove your answer. (a) $\forall x \in \mathbb{Z}\ \exists y \in \mathbb{Z},\ x + y = 0$. (b) $\exists y \in \mathbb{Z}\ \forall x \in \mathbb{Z},\ x + y = 0$. (c) $\forall x \in \mathbb{R}\ \exists y \in \mathbb{R},\ y^2 = x$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) "For every integer $x$ there is an integer $y$ with $x + y = 0$." True. *Proof.* Let $x$ be an integer and take $y = -x$, which is an integer. Then $x + y = 0$. $\blacksquare$

(b) "There is an integer $y$ with $x + y = 0$ for every integer $x$." False. *Proof.* Suppose such a $y$ exists. Apply the statement to $x = 1 - y$, which is an integer. It gives $(1 - y) + y = 0$, that is, $1 = 0$, which is false. So no such $y$ exists. $\blacksquare$

(c) "Every real number is the square of a real number." False. *Proof.* Take $x = -1$. The square of a real number is never negative (Theorem 4 in the axioms lesson), so no real $y$ has $y^2 = -1$. $\blacksquare$

Check: (a) with $x = 5$ gives $y = -5$. For (b), if $y = 3$ then $x = -2$ gives $-2 + 3 = 1 \ne 0$.

</details>

5\. Find the error in each line. (a) "Solve $x^2 = 9$. Then $x^2 = 9 \Rightarrow x = 3$, so the only solution is 3." (b) "The statement $3 \mid 12 = 4$ is true because $12 \div 3 = 4$."

<details class="solution" markdown>
<summary>Solution</summary>

(a) The implication $x^2 = 9 \Rightarrow x = 3$ is false, because $x = -3$ also satisfies $x^2 = 9$. The correct chain is $x^2 = 9 \Leftrightarrow (x = 3 \vee x = -3)$. Both directions hold: $(-3)^2 = 9$. The solutions are 3 and $-3$.

(b) The expression mixes two kinds of object. The symbol $3 \mid 12$ is a statement (true), and "$= 4$" compares it to a number. The two true facts are "$3 \mid 12$" and "$12 \div 3 = 4$", and they should be written separately.

Check (a): $3^2 = 9$ and $(-3)^2 = 9$.

</details>

6\. Prove that the two ways of writing the set of odd integers describe the same set: $\{n \in \mathbb{Z} : \exists k \in \mathbb{Z},\ n = 2k + 1\} = \{2k + 1 : k \in \mathbb{Z}\}$.

<details class="solution" markdown>
<summary>Solution</summary>

Call the left set $L$ and the right set $R$. To show $L = R$, prove $L \subseteq R$ and $R \subseteq L$.

*Proof.* ($L \subseteq R$) Let $n \in L$. Then $n$ is an integer and $n = 2k + 1$ for some integer $k$. So $n$ is of the form $2k + 1$ with $k \in \mathbb{Z}$, which is the description of $R$. Hence $n \in R$.

($R \subseteq L$) Let $n \in R$. Then $n = 2k + 1$ for some integer $k$. Since $2k + 1$ is an integer, $n \in \mathbb{Z}$, and it has the property $\exists k \in \mathbb{Z},\ n = 2k + 1$. Hence $n \in L$.

Since each set is a subset of the other, $L = R$. $\blacksquare$

Check: both sets contain $-3$ (with $k = -2$) and 7 (with $k = 3$), and neither contains 4.

</details>

### Challenge

7\. A student claims: "$\forall a, b \in \mathbb{Z},\ (a \mid b \wedge b \mid a) \Rightarrow a = b$." Show that it is false, find the true statement, and prove it.

<details class="solution" markdown>
<summary>Solution</summary>

*Counterexample.* Take $a = 3$ and $b = -3$. Then $3 \mid -3$ since $-3 = 3 \times (-1)$, and $-3 \mid 3$ since $3 = (-3) \times (-1)$. But $a \ne b$.

*The true statement:* for all integers $a$ and $b$, if $a \mid b$ and $b \mid a$, then $a = b$ or $a = -b$.

What we know: $b = ak$ and $a = bl$ for integers $k$ and $l$. What we want: $a = \pm b$. The plan: substitute one equation into the other and look at the product $kl$.

*Proof.* Let $a \mid b$ and $b \mid a$. Then $b = ak$ and $a = bl$ for integers $k$ and $l$, so $a = (ak)l = a(kl)$. If $a = 0$, then $b = 0 \cdot k = 0$, so $a = b$. Suppose $a \ne 0$. Dividing by $a$ gives $kl = 1$. The integers $k$ and $l$ are nonzero, so $\lvert k \rvert \ge 1$ and $\lvert l \rvert \ge 1$, and $\lvert k \rvert \lvert l \rvert = 1$ forces $\lvert k \rvert = 1$. So $k = 1$ or $k = -1$, which gives $b = a$ or $b = -a$. $\blacksquare$

Look back: the extra case $b = -a$ appears because the definition of divides allows negative $k$. Check: $a = 5$ and $b = 5$ work, as do $a = 5$ and $b = -5$, and a program that searches all pairs from $-6$ to 6 finds only pairs with $a = \pm b$.

</details>

8\. (Reviews [composition and inverse functions](../../03-high-school/03-functions/05-composition-and-inverse-functions.md).) Let $f(x) = 2x + 3$ and $g(x) = x^2$. Compute $(f \circ g)(x)$ and $(g \circ f)(x)$, and prove that $f \circ g \ne g \circ f$ by finding an input where they differ.

<details class="solution" markdown>
<summary>Solution</summary>

By definition $(f \circ g)(x) = f(g(x)) = 2x^2 + 3$, and $(g \circ f)(x) = g(f(x)) = (2x + 3)^2 = 4x^2 + 12x + 9$.

*Proof that they differ.* Take $x = 1$. Then $(f \circ g)(1) = 2 + 3 = 5$ and $(g \circ f)(1) = 5^2 = 25$. Since $5 \ne 25$, the functions $f \circ g$ and $g \circ f$ are not equal. $\blacksquare$

Look back: two functions are equal exactly when they agree on every input, so a single input where they differ is enough to show they are different. Read $f \circ g$ as "$f$ after $g$": the right function acts first. Check: $2(1)^2 + 3 = 5$ and $4 + 12 + 9 = 25$.

</details>

## Where this shows up

- The logic chapter turns the symbols of this lesson into a calculation: [statements and connectives](../02-logic-and-sets/01-statements-and-connectives.md), then [quantifiers](../02-logic-and-sets/04-quantifiers.md) and [negation and translating English](../02-logic-and-sets/05-negation-and-translating-english.md), which practises the translation steps above. Relations and functions use the arrow notation of $f \colon A \to B$ in [functions and well-definedness](../06-relations-and-functions/04-functions-and-well-definedness.md).
- CS definitions are strings of quantifiers. The statement "$f(n)$ is $O(g(n))$" means: there exist $c > 0$ and $n_0$ such that for every $n \ge n_0$, $f(n) \le c\,g(n)$. That is $\exists\,\forall$ in this order, and [asymptotic notation](../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md) reads it the way this lesson does. Program specifications and loop invariants are quantified statements too.
- In economics, the assumptions on preferences are quantified: "for all bundles $x$ and $y$, $x$ is at least as good as $y$ or $y$ is at least as good as $x$" is the completeness assumption ([utility and indifference curves](../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md)).
