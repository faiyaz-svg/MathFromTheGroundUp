# Real numbers, axioms and set notation

After this lesson you can describe a set in roster or set-builder notation, use $\in$, $\notin$, $\subseteq$ and $\emptyset$ correctly, name the axiom behind each step of an algebra calculation, and prove simple facts such as $a \cdot 0 = 0$ from the axioms.

Before this: [roots, irrational numbers and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md), [integer arithmetic and sign rules](../../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md) and [properties of operations](../../01-elementary/04-properties-of-operations.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. List the elements of $\{n \in \mathbb{N} : n^2 < 20\}$, and write "the integers strictly between $-3$ and 2" in set-builder notation.
2. True or false: (a) $\sqrt{2} \in \mathbb{Q}$, (b) $\{1, 2\} \subseteq \{1, 2, 3\}$, (c) $\emptyset \subseteq \mathbb{Z}$, (d) $-3 \notin \mathbb{N}$.
3. Name the property that justifies each equation: (a) $7 + (3 + x) = (7 + 3) + x$, (b) $5(x + 2) = 5x + 10$, (c) $x + (-x) = 0$.

<details class="solution" markdown>
<summary>Answers</summary>

1. The squares $0, 1, 4, 9, 16$ are below 20 and $5^2 = 25$ is not, so the set is $\{0, 1, 2, 3, 4\}$. The second set is $\{n \in \mathbb{Z} : -3 < n < 2\}$, which is $\{-2, -1, 0, 1\}$.
2. (a) False: $\sqrt{2}$ is irrational. (b) True: both elements of the left set are in the right set. (c) True: the empty set has no element that could fail to be in $\mathbb{Z}$. (d) True: $-3$ is not a natural number.
3. (a) The associative property of addition. (b) The distributive property. (c) The additive inverse property.

</details>

## The idea

Simplify $3(x + 4) - 3x$. The answer is 12, and you probably wrote it without a pause. But every move in that calculation was one of a few rules, and each can be named:

$$
\begin{aligned}
3(x + 4) - 3x &= (3x + 12) + (-3x) && \text{distributive property; subtracting is adding the opposite} \\
&= (12 + 3x) + (-3x) && \text{commutative property of addition} \\
&= 12 + \bigl(3x + (-3x)\bigr) && \text{associative property of addition} \\
&= 12 + 0 && \text{an opposite cancels its number} \\
&= 12 && \text{adding 0 changes nothing}
\end{aligned}
$$

The rules are the ones from [properties of operations](../../01-elementary/04-properties-of-operations.md), now called by their university names. A short list of rules like this, accepted without proof, is enough to prove every other fact about the arithmetic of real numbers. A statement accepted without proof as a starting point is an axiom, and this lesson gathers the list in one place.

Two things make the list worth knowing. First, a proof in a university course cites a reason for every line, and these axioms are the first reasons you get. Second, many number systems you will meet obey only some of the rules. Matrices break the commutative property of multiplication, computer floating-point numbers break the associative property of addition, and arithmetic with remainders breaks the rule that a product is 0 only when a factor is 0. Knowing the list tells you which algebra moves are safe in each system.

To state the rules for "all real numbers" we also need a way to name collections of numbers. That is set notation, and it comes first.

## Definitions

### Sets and set notation

A **set** is a collection of objects, and the objects are its **elements**. We write $x \in A$ ("$x$ is an element of $A$") when $x$ is in the set $A$, and $x \notin A$ when it is not. So $3 \in \{1, 2, 3\}$ and $4 \notin \{1, 2, 3\}$.

In plain words, a set is a bag that either has an object in it or doesn't. Two things don't matter: the order the elements are listed in, and how many times an element is listed. So $\{1, 2\} = \{2, 1\} = \{1, 1, 2\}$.

**Roster notation** lists the elements between braces, with dots when the pattern is clear: $\{2, 4, 6, 8\}$ and $\{0, 1, 2, 3, \dots\}$. **Set-builder notation** describes the elements by a condition instead:

$$
\{x \in A : \text{condition on } x\}.
$$

Read it as "the set of all $x$ in $A$ such that the condition holds". The set $A$ named first is the ground set, the collection the elements are picked from, and the condition then filters it. For example, $\{x \in \mathbb{Z} : x^2 = 4\} = \{-2, 2\}$. Some books write a vertical bar instead of the colon, as in $\{x \in \mathbb{Z} \mid x^2 = 4\}$, and the two forms mean the same.

Set-builder notation can also put an expression in front of the colon: $\{n^2 : n \in \{-2, -1, 0, 1, 2\}\}$ is "all numbers of the form $n^2$, where $n$ is one of those five". Listing the five squares gives $0, 1, 4, 1, 0$ as a roster, and removing the repeats leaves $\{0, 1, 4\}$.

The **empty set**, written $\emptyset$ or $\{\}$, is the set with no elements. For example, $\{x \in \mathbb{R} : x^2 = -1\} = \emptyset$, because no real number squares to $-1$.

A set $A$ is a **subset** of a set $B$, written $A \subseteq B$, when every element of $A$ is also an element of $B$. In plain words, nothing in $A$ falls outside $B$. So $\{1, 2\} \subseteq \{1, 2, 3\}$, and every set is a subset of itself. Two sets are equal exactly when each is a subset of the other: $A = B$ means $A \subseteq B$ and $B \subseteq A$. A **proper subset**, written $A \subsetneq B$, is a subset with $A \ne B$. This book avoids the symbol $\subset$, because some books use it for $\subseteq$ and others for $\subsetneq$.

The symbols $\in$ and $\subseteq$ are different. The symbol $\in$ connects an element to a set, and $\subseteq$ connects two sets. Here $1 \in \{1, 2\}$ is true, and $\{1\} \subseteq \{1, 2\}$ is true, but $1 \subseteq \{1, 2\}$ is not even a statement, because $1$ is a number and not a set.

### The number systems

The natural numbers are $\mathbb{N} = \{0, 1, 2, 3, \dots\}$ in this book, the integers are $\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$, and the rational numbers are the fractions of integers:

$$
\mathbb{Q} = \left\{ \frac{a}{b} : a \in \mathbb{Z},\ b \in \mathbb{Z},\ b \ne 0 \right\}.
$$

The real numbers $\mathbb{R}$ are all the points of the number line, rational or not, as in [roots, irrational numbers and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#the-real-numbers-and-their-subsets). Each set sits inside the next:

$$
\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}.
$$

All three inclusions are proper. The number $-1$ is in $\mathbb{Z}$ but not $\mathbb{N}$, the number $\frac{1}{2}$ is in $\mathbb{Q}$ but not $\mathbb{Z}$, and $\sqrt{2}$ is in $\mathbb{R}$ but not $\mathbb{Q}$. Each inclusion holds because an element of the smaller set can be written as an element of the larger one: an integer $n$ equals the fraction $\frac{n}{1}$. The figure in the roots lesson draws the four sets inside each other.

Two more names are handy. The positive integers are $\mathbb{Z}^+ = \{1, 2, 3, \dots\}$ and the positive reals are $\mathbb{R}^+ = \{x \in \mathbb{R} : x > 0\}$. When the start of $\mathbb{N}$ matters, writing $\mathbb{Z}^+$ or $\mathbb{Z}_{\ge 0}$ avoids the question, as noted in [symbols and notation](../../reference/symbols-and-notation.md#number-sets).

Each set in the chain was built to repair a gap. In $\mathbb{N}$ you can't always subtract, since $2 - 5$ is not a natural number, and $\mathbb{Z}$ fixes that. In $\mathbb{Z}$ you can't always divide, since $1 \div 2$ is not an integer, and $\mathbb{Q}$ fixes that. In $\mathbb{Q}$ some lengths are missing, since no fraction has square 2, and $\mathbb{R}$ fixes that. The axioms below make the gaps precise.

### The field axioms

In this section $a$, $b$ and $c$ stand for any real numbers. The **field axioms** are these eleven statements about addition and multiplication.

| Name | For addition | For multiplication |
|---|---|---|
| A1, M1: **closure** | $a + b$ is a real number | $a \cdot b$ is a real number |
| A2, M2: **commutative** | $a + b = b + a$ | $a \cdot b = b \cdot a$ |
| A3, M3: **associative** | $(a + b) + c = a + (b + c)$ | $(a \cdot b) \cdot c = a \cdot (b \cdot c)$ |
| A4, M4: **identity** | there is a number $0$ with $a + 0 = a$ | there is a number $1$, with $1 \ne 0$, and $a \cdot 1 = a$ |
| A5, M5: **inverse** | for each $a$ there is a number $-a$ with $a + (-a) = 0$ | for each $a \ne 0$ there is a number $a^{-1}$ with $a \cdot a^{-1} = 1$ |

The eleventh axiom, labelled D, links the two operations. It is the **distributive property**: $a \cdot (b + c) = a \cdot b + a \cdot c$.

In plain words: you can add or multiply any two real numbers and stay inside $\mathbb{R}$; you can swap and regroup in a sum or a product; adding 0 and multiplying by 1 change nothing; every number has an opposite for addition, and every number except 0 has a reciprocal for multiplication; and multiplication distributes over addition. The reciprocal $a^{-1}$ is the number written $\frac{1}{a}$.

Subtraction and division have no axioms of their own. They are defined from the inverses: $a - b$ means $a + (-b)$, and for $b \ne 0$, $\frac{a}{b}$ means $a \cdot b^{-1}$. That is why subtraction and division are not commutative or associative, as the table in [properties of operations](../../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division) showed: the axioms were never stated for them.

A set with an addition and a multiplication that satisfy all eleven axioms is a **field**. The sets $\mathbb{Q}$ and $\mathbb{R}$ are fields, and the next table shows what the smaller sets are missing.

| Set | A1, M1 (closure) | A2 to A4, M2 to M4, D | A5 (opposites) | M5 (reciprocals) |
|---|---|---|---|---|
| $\mathbb{N}$ | holds | holds | fails: $1$ has no opposite in $\mathbb{N}$ | fails: $2$ has no reciprocal in $\mathbb{N}$ |
| $\mathbb{Z}$ | holds | holds | holds | fails: $2$ has no reciprocal in $\mathbb{Z}$ |
| $\mathbb{Q}$ | holds | holds | holds | holds |
| $\mathbb{R}$ | holds | holds | holds | holds |

Each row matches the story above: $\mathbb{Z}$ repairs the missing opposites, and $\mathbb{Q}$ repairs the missing reciprocals. The set of irrational numbers is not a field, because it isn't closed: $\sqrt{2} \cdot \sqrt{2} = 2$ and $\sqrt{2} + (-\sqrt{2}) = 0$ are both rational.

### The order axioms

The field axioms say nothing about "less than". Let $P$ be a set of real numbers, called the positive numbers, with two properties.

- O1 (closure of the positives): if $a \in P$ and $b \in P$, then $a + b \in P$ and $a \cdot b \in P$.
- O2 (trichotomy): for each real number $a$, exactly one of these holds: $a \in P$, $a = 0$, or $-a \in P$.

Then the order is defined from $P$. The statement $a < b$ means $b - a \in P$, and $a > b$ means $b < a$. The statement $a \le b$ means $a < b$ or $a = b$. In plain words, $a < b$ says that $b - a$ is positive, which is how [inequalities](../../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#definitions) defined it, and O1 and O2 say that positive numbers can be added and multiplied and that each number is positive, zero or minus a positive number. A field with such a set $P$ is an **ordered field**. Both $\mathbb{Q}$ and $\mathbb{R}$ are ordered fields.

### The completeness axiom

Only one more axiom is needed to tell $\mathbb{R}$ from $\mathbb{Q}$. An **upper bound** of a set $S$ of real numbers is a number $u$ with $s \le u$ for every $s \in S$. A **least upper bound** of $S$ is an upper bound that is less than or equal to every other upper bound. The completeness axiom says that every nonempty set of real numbers that has an upper bound has a least upper bound.

In plain words, the real line has no gaps. The set $\{x \in \mathbb{R} : x^2 < 2\}$ has upper bounds such as 1.5 and 1.42, and its least upper bound is $\sqrt{2}$. The same description inside $\mathbb{Q}$, the set $\{x \in \mathbb{Q} : x^2 < 2\}$, has rational upper bounds but no least rational one, because the least would have to be $\sqrt{2}$, which is not rational. A real analysis course proves that last claim and builds calculus on the axiom; the intermediate value theorem in [continuity, asymptotes and the IVT](../../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md) depends on it. This lesson only names it.

## How to do it

### Working with sets

1. Decide whether to list or to describe. A short finite set is easiest to list. A set with a pattern or infinitely many elements usually needs dots or set-builder notation.
2. In set-builder notation, name the ground set before the colon. The description $\{x : x > 0\}$ is ambiguous, since it changes meaning between $\mathbb{Z}$ and $\mathbb{R}$ (for the first, 0.5 isn't an element; for the second it is).
3. To test whether $x \in \{y \in A : \text{condition}\}$, check two things: that $x \in A$, and that the condition is true for $x$.
4. To show that $A \subseteq B$, take an arbitrary element $x \in A$ and show that $x \in B$. To show $A = B$, prove both inclusions.
5. To show that $A \not\subseteq B$ (not a subset), find one element of $A$ that is not in $B$.

### Naming the axiom behind a step

1. Look at what the step changes. Swapping two terms or two factors is the commutative property. Moving brackets is the associative property.
2. Handing a multiplier over a sum, or pulling one out, is the distributive property.
3. Inserting or deleting $+ 0$ or $\cdot 1$ is the identity property. Cancelling a number with its opposite, or with its reciprocal, is the inverse property.
4. Write the name beside the line. If no axiom fits, the step needs an earlier theorem (a result already proved) or isn't allowed.

Step 4 catches a common habit. "Move the 5 to the other side" is not an axiom. It is a shorthand for adding $-5$ to both sides, and the next section shows why that is allowed.

### Proving facts from the axioms

The first theorem is the rule behind "add the same number to both sides". The second says that the opposite of a number is unique.

*Theorem 1.* Let $a$, $b$ and $c$ be real numbers.

1. If $a + c = b + c$, then $a = b$.
2. If $a + b = 0$, then $b = -a$.

We know the axioms A1 to A5. We want to remove $c$ from both sides in part 1, and to show that no number other than $-a$ can be added to $a$ to get 0 in part 2. The plan for part 1 is to add $-c$ to both sides and cancel. Part 2 is then a short application of part 1.

*Proof of part 1.*

$$
\begin{aligned}
a &= a + 0 && \text{A4} \\
&= a + \bigl(c + (-c)\bigr) && \text{A5} \\
&= (a + c) + (-c) && \text{A3} \\
&= (b + c) + (-c) && \text{the hypothesis } a + c = b + c \\
&= b + \bigl(c + (-c)\bigr) && \text{A3} \\
&= b + 0 && \text{A5} \\
&= b && \text{A4}
\end{aligned}
$$

*Proof of part 2.* By A5, $a + (-a) = 0$, so $a + b = a + (-a)$. By A2 this says $b + a = (-a) + a$. Part 1, with $c = a$, gives $b = -a$.

Look back: the proof of part 1 uses only the axioms, never a particular number, so it holds in every field. Part 2 says that a number has only one opposite. It also gives $-(-a) = a$: since $(-a) + a = 0$ by A5 and A2, part 2 applied to $-a$ says that $a$ is the opposite of $-a$. The sign-rules lesson used this fact in its proofs and checked it in [Practice problem 7](../../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#practice), by a different route.

*Theorem 2.* For every real number $a$, $a \cdot 0 = 0$.

We know A4, D and Theorem 1. We want to show that multiplying by 0 gives 0, and no axiom says so directly. The plan is to write $0$ as $0 + 0$, distribute, and cancel.

*Proof.*

$$
\begin{aligned}
a \cdot 0 + a \cdot 0 &= a \cdot (0 + 0) && \text{D} \\
&= a \cdot 0 && \text{A4, since } 0 + 0 = 0 \\
&= 0 + a \cdot 0 && \text{A4 and A2}
\end{aligned}
$$

So $(a \cdot 0) + (a \cdot 0) = 0 + (a \cdot 0)$. Theorem 1, part 1, with $c = a \cdot 0$ gives $a \cdot 0 = 0$.

Look back: [Practice problem 5 of properties of operations](../../01-elementary/04-properties-of-operations.md#practice) proved the same fact by assuming that $x + x = x$ forces $x = 0$. Cancellation is where that assumption comes from: $x + x = x + 0$ gives $x = 0$. A consequence is that 0 has no reciprocal. If $0 \cdot x = 1$ for some $x$, Theorem 2 would give $0 = 1$, which M4 forbids. So "division by 0 is undefined" is not a convention someone chose: no number could play the part of $\frac{1}{0}$.

*Theorem 3 (the zero-product property).* Let $a$ and $b$ be real numbers. If $a \cdot b = 0$, then $a = 0$ or $b = 0$.

We know M3, M4, M5 and Theorem 2. We want to show that at least one factor is 0. The plan is a proof by cases: either $a = 0$, and we are done, or $a \ne 0$, and we show $b = 0$ by multiplying by the reciprocal of $a$.

*Proof.* If $a = 0$, the statement holds. Suppose $a \ne 0$. By M5, $a^{-1}$ exists, and

$$
\begin{aligned}
b &= 1 \cdot b && \text{M4 and M2} \\
&= (a^{-1} \cdot a) \cdot b && \text{M5 and M2} \\
&= a^{-1} \cdot (a \cdot b) && \text{M3} \\
&= a^{-1} \cdot 0 && \text{the hypothesis } ab = 0 \\
&= 0 && \text{Theorem 2 and M2}
\end{aligned}
$$

So $b = 0$. In both cases at least one of $a$ and $b$ is 0. $\blacksquare$

Look back: the "or" is inclusive, since $a$ and $b$ can both be 0. The proof needed M5, and that is where the property can fail in other systems. It is the reason that solving $(x - 2)(x - 3) = 0$ by writing $x - 2 = 0$ or $x - 3 = 0$ is legal for real numbers. The next theorem shows the order axioms at work.

*Theorem 4.* For every real number $a \ne 0$, $a \cdot a > 0$. In particular, $1 > 0$.

We know O1, O2, M4 and the sign-rules theorem $(-a)(-a) = a \cdot a$, proved in [integer arithmetic and sign rules](../../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#why-a-negative-times-a-negative-is-positive) from these same axioms. We want $a \cdot a \in P$. The plan is to split on the two ways a nonzero number can be positive-or-negative, which O2 provides.

*Proof.* Since $a \ne 0$, O2 says that $a \in P$ or $-a \in P$. If $a \in P$, then $a \cdot a \in P$ by O1. If $-a \in P$, then $(-a)(-a) \in P$ by O1, and $(-a)(-a) = a \cdot a$, so again $a \cdot a \in P$. In both cases $a \cdot a - 0 = a \cdot a$ is in $P$, which means $a \cdot a > 0$. For the last claim, $1 \ne 0$ by M4, and $1 = 1 \cdot 1$, so $1 > 0$. $\blacksquare$

Look back: with Theorem 2 this says that $a^2 \ge 0$ for every real $a$, with equality only for $a = 0$. So $x^2 + 1 \ge 1$ for every real $x$, and the equation $x^2 = -1$ has no real solution. That is the gap that [complex numbers](../05-quadratics-and-complex-numbers/03-complex-numbers.md) are built to fill.

## Worked examples

<div class="example" markdown>

### Example 1: justifying every step of an equation

Solve $3x + 5 = 20$, and name the axiom or theorem behind each step.

The first move is "subtract 5 from both sides", which is adding $-5$ to both sides. Equal numbers stay equal when you add the same number to each, so

$$
(3x + 5) + (-5) = 20 + (-5).
$$

Now name the changes on the left (Steps 1 to 3 of naming the axiom). Moving the brackets is the associative property A3, giving $3x + \bigl(5 + (-5)\bigr)$. Cancelling $5$ with $-5$ is the inverse property A5, giving $3x + 0$, and dropping the $+ 0$ is the identity property A4, giving $3x$. On the right, $20 + (-5) = 15$ is arithmetic on two specific numbers. The equation is now $3x = 15$.

The second move is "divide both sides by 3", which is multiplying both sides by $3^{-1} = \frac{1}{3}$:

$$
3^{-1} \cdot (3x) = 3^{-1} \cdot 15.
$$

On the left, M3 regroups the product as $(3^{-1} \cdot 3) \cdot x$, M5 turns $3^{-1} \cdot 3$ into 1, and M4 turns $1 \cdot x$ into $x$. On the right, $\frac{1}{3} \cdot 15 = 5$. So $x = 5$.

Check: $3 \cdot 5 + 5 = 20$.

The axioms are why each of those quick steps is allowed. They also show what to watch for: M5 needs a nonzero number, so you may divide both sides only by a number you know is not 0.

</div>

<div class="example" markdown>

### Example 2: three sets inside each other

Let $A = \{x \in \mathbb{Z} : x^2 \le 10\}$, $B = \{x \in \mathbb{N} : x^2 \le 10\}$ and $C = \{x \in \mathbb{R} : x^2 \le 10\}$. List $A$ and $B$, describe $C$, and put the three sets in order with $\subseteq$.

The integers with $x^2 \le 10$ are the ones with $\lvert x \rvert \le 3$, because $3^2 = 9$ and $4^2 = 16$. So $A = \{-3, -2, -1, 0, 1, 2, 3\}$. The set $B$ keeps only the natural numbers among them, so $B = \{0, 1, 2, 3\}$.

The set $C$ is infinite, with elements such as $0.5$, $-2.9$ and $\sqrt{10} \approx 3.162$. It contains $3.1$, since $3.1^2 = 9.61 \le 10$, and it doesn't contain $3.5$, since $3.5^2 = 12.25$.

Every element of $B$ is in $A$, and every element of $A$ is a real number with $x^2 \le 10$, so

$$
B \subseteq A \subseteq C.
$$

Both inclusions are proper: $-1 \in A$ but $-1 \notin B$, and $0.5 \in C$ but $0.5 \notin A$. Check by counting: $A$ has 7 elements, $B$ has 4, and $B$ is what is left of $A$ after dropping the 3 negative integers.

</div>

<div class="example" markdown>

### Example 3: the empty set and other edge cases

(a) The set $\{x \in \mathbb{R} : x^2 = -1\}$ is empty, because squares of real numbers are never negative (Theorem 4).

(b) Is $\emptyset \subseteq \{1, 2\}$? By the definition, we need every element of $\emptyset$ to be in $\{1, 2\}$. The empty set has no element that could fail, so the statement is true. In fact $\emptyset \subseteq A$ for every set $A$.

(c) The sets $\emptyset$, $\{\emptyset\}$ and $\{0\}$ are three different sets. The first has no elements, the second has one element (the empty set), and the third has one element (the number 0).

(d) Compare three statements about $\{1, 2\}$: $1 \in \{1, 2\}$ is true, $\{1\} \subseteq \{1, 2\}$ is true, and $\{1\} \in \{1, 2\}$ is false, since the elements of $\{1, 2\}$ are numbers and $\{1\}$ is a set.

Check (c) by counting elements: write $\lvert S \rvert$ for the number of elements of $S$. Then $\lvert \emptyset \rvert = 0$, $\lvert \{\emptyset\} \rvert = 1$ and $\lvert \{0\} \rvert = 1$, and the last two differ in what their one element is.

</div>

<div class="example" markdown>

### Example 4: the opposite of a sum (finish it yourself)

Prove that $-(a + b) = (-a) + (-b)$ for all real numbers $a$ and $b$.

We know Theorem 1, part 2: if $x + y = 0$, then $y = -x$. We want to show that $(-a) + (-b)$ is the opposite of $a + b$. By the theorem it is enough to show that

$$
(a + b) + \bigl((-a) + (-b)\bigr) = 0.
$$

Regroup and reorder with A2 and A3:

$$
(a + b) + \bigl((-a) + (-b)\bigr) = \bigl(a + (-a)\bigr) + \bigl(b + (-b)\bigr).
$$

Now finish the argument, and say which axioms you used.

<details class="solution" markdown>
<summary>Finish</summary>

By A5, $a + (-a) = 0$ and $b + (-b) = 0$, so the right side is $0 + 0$, which is 0 by A4. So $(a + b) + \bigl((-a) + (-b)\bigr) = 0$. Theorem 1, part 2, with $x = a + b$ and $y = (-a) + (-b)$, gives $(-a) + (-b) = -(a + b)$.

Check with numbers: for $a = 3$ and $b = -8$, $-(3 + (-8)) = -(-5) = 5$ and $(-3) + 8 = 5$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: $\in$ and $\subseteq$ are not interchangeable. The number 2 is an element of $\{1, 2, 3\}$, so $2 \in \{1, 2, 3\}$, and the set $\{2\}$ is a subset, so $\{2\} \subseteq \{1, 2, 3\}$. Writing $2 \subseteq \{1, 2, 3\}$ or $\{2\} \in \{1, 2, 3\}$ is a type error: an element belongs to a set, and a set is contained in a set. If you can't tell which symbol you need, ask whether the left side is a single object or a collection.

</div>

<div class="warning" markdown>

Watch out: the empty set is not the same as the set containing 0, or as nothing at all. The set $\{0\}$ has one element. The set $\emptyset$ has none, and $\{\emptyset\}$ has one element, which is itself a set. A solution set that comes out empty is a complete answer: "no real number works" is written $\emptyset$.

</div>

<div class="warning" markdown>

Watch out: you can't cancel a factor without knowing it is not 0. From $0 \cdot 3 = 0 \cdot 5$ cancelling the 0 would give $3 = 5$. Multiplicative cancellation says: if $a \ne 0$ and $ab = ac$, then $b = c$. Additive cancellation (Theorem 1) needs no such condition, because every number has an opposite and only 0 lacks a reciprocal.

</div>

<div class="warning" markdown>

Watch out: don't treat subtraction and division as if they had the commutative and associative properties. Subtraction is $a + (-b)$ and division is $a \cdot b^{-1}$, and the axioms are about addition and multiplication. For example, $(10 - 5) - 2 = 3$ but $10 - (5 - 2) = 7$. The fix is to rewrite as an addition first: $10 + (-5) + (-2)$ can be regrouped freely.

</div>

Writing "by algebra" as the reason for a step doesn't count as a reason in a proof. Each line should cite an axiom, a definition or a proved theorem, as the proofs above do, until you have enough practice to skip the easy ones.

Subtle point: M4 says $1 \ne 0$. Without it, the one-element set $\{0\}$ would satisfy the other ten axioms, with $0 + 0 = 0$ and $0 \cdot 0 = 0$, and every theorem would be about a system with only one number.

## Tricks and shortcuts

To disprove a "for all" rule, find one counterexample, and try the numbers 0, 1 and $-1$ first. They break most false rules. The proposed rule $a + a = a \cdot a$ holds for 0 and 2 but fails for 1, so it isn't a rule.

To show two sets are equal, prove two inclusions. To show $A = \{x \in \mathbb{Z} : x \text{ is even}\}$ equals $B = \{2k : k \in \mathbb{Z}\}$, show that every even number has the form $2k$ and that every $2k$ is even.

Read set-builder notation aloud as a sentence: "the set of all $n$ in $\mathbb{N}$ such that $n^2 < 20$". If the sentence sounds wrong, the notation usually is too.

When you need an inverse, define it by its job. The opposite of $a$ is "the number that adds to $a$ to give 0", and the reciprocal is "the number that multiplies $a$ to give 1". Uniqueness (Theorem 1, part 2) then lets you prove that something is the opposite by showing that it adds to $a$ to give 0, as in Example 4.

## In code

Floating-point numbers look like real numbers but don't satisfy every axiom. Exact fractions do. Python's built-in sets follow the notation of this lesson.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction

# A float sum can depend on how it is grouped, so A3 fails for floats.
print((0.1 + 0.2) + 0.3)             # 0.6000000000000001
print(0.1 + (0.2 + 0.3))             # 0.6
a = 1e16
print((a + 1) + 1 == a + (1 + 1))    # False

# Exact fractions are a field, so the grouping never matters.
f = [Fraction(1, 10), Fraction(2, 10), Fraction(3, 10)]
print((f[0] + f[1]) + f[2] == f[0] + (f[1] + f[2]))   # True

# Sets: roster, set-builder (a set comprehension), subset and element tests.
A = {x for x in range(-10, 11) if x * x <= 10}
B = {x for x in range(0, 11) if x * x <= 10}
print(sorted(A), sorted(B))          # [-3, -2, -1, 0, 1, 2, 3] [0, 1, 2, 3]
print(B <= A, A <= B, 3 in A)        # True False True
print(set() <= A)                    # True: the empty set is a subset of every set
print(sorted({n * n for n in range(-2, 3)}))   # [0, 1, 4]
```

In the first line, `0.1 + 0.2` is stored as slightly more than 0.3, and adding 0.3 gives a different last digit than adding in the other order. The 1e16 line shows the same failure from rounding: adding 1 to $10^{16}$ one step at a time is lost twice, while adding 2 in one step is not. [Floating point basics](../../06-cs-math/01-number-representation/04-floating-point-basics.md) explains the format. The expression `B <= A` is Python's $\subseteq$, and `{... for ... if ...}` is set-builder notation with the ground set written as `range(...)`.

</details>

## FAQ

### If these rules are obvious, why list them?

They are obvious for real numbers, and the list matters because it is short. Everything else about real-number arithmetic can be proved from eleven statements, so a doubtful claim can be settled by a proof instead of an appeal to habit. The list also travels: a mathematician can ask of any new system whether it satisfies the axioms. Matrix multiplication fails M2. Arithmetic with remainders, as in clocks, satisfies M2 and D but fails M5 unless the modulus is prime, which is why prime moduli matter in cryptography.

### Why does 0 have no reciprocal?

Theorem 2 says that $0 \cdot x = 0$ for every $x$, so no number $x$ satisfies $0 \cdot x = 1$. Suppose someone defines a number called $\frac{1}{0}$ anyway, with $0 \cdot \frac{1}{0} = 1$. Then Theorem 2 gives $0 = 1$, and M4 says $1 \ne 0$, so the new number would break the axioms. The same conflict is behind the false proof that $2 = 1$ in the [multi-step equations FAQ](../../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#where-does-the-proof-that-2-equals-1-go-wrong), which hides a division by 0.

### Why does the complex number system have no order?

It does satisfy all eleven field axioms, so it is a field, but it is not an ordered field. The number $i$ with $i^2 = -1$ is not 0, so in an ordered field Theorem 4 would give $i^2 > 0$, that is, $-1 > 0$. But $1 > 0$ says that $1 \in P$, and by O2 the number $-1$ can't be in $P$ as well. So no choice of $P$ works for the complex numbers.

### Why is the empty set a subset of every set?

To fail to be a subset of $A$, a set would need an element that is not in $A$. The empty set has no elements at all, so it can't fail. A statement of the form "every element of $\emptyset$ satisfies something" is true for the same reason that "every unicorn in this room is purple" can't be shown false by pointing at a unicorn. Logicians call this vacuous truth, and the proofs and logic folder returns to it in [sets and set operations](../../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md).

## Practice

### Warm-up

1\. (a) List the elements of $\{x \in \mathbb{Z} : -2 \le x < 3\}$. (b) Write $\{2, 4, 6, 8, 10\}$ in set-builder notation. (c) List the elements of $\{n^2 : n \in \{-2, -1, 0, 1, 2\}\}$. (d) What is $\{x \in \mathbb{R} : x^2 = -4\}$?

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The integers from $-2$ up to but not including 3: $\{-2, -1, 0, 1, 2\}$.
- (b) One answer is $\{n \in \mathbb{Z}^+ : n \text{ is even and } n < 12\}$. Another is $\{2k : k \in \mathbb{Z},\ 1 \le k \le 5\}$.
- (c) The squares are $4, 1, 0, 1, 4$, and removing repeats gives $\{0, 1, 4\}$.
- (d) The empty set, $\emptyset$, since no real number has a negative square.

Check (b) by listing: $k = 1, \dots, 5$ gives $2, 4, 6, 8, 10$, and the positive even integers below 12 are the same five numbers.

</details>

2\. True or false: (a) $0 \in \mathbb{N}$, (b) $\frac{3}{4} \in \mathbb{Z}$, (c) $\mathbb{Z} \subseteq \mathbb{Q}$, (d) $\{2, 3\} \subseteq \{1, 2\}$, (e) $\emptyset \subseteq \{1, 2\}$, (f) $\{1\} \in \{1, 2\}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) True, because this book's $\mathbb{N}$ starts at 0.
- (b) False: $\frac{3}{4}$ has a fractional part.
- (c) True: each integer $n$ equals $\frac{n}{1}$.
- (d) False: $3 \in \{2, 3\}$ but $3 \notin \{1, 2\}$.
- (e) True: the empty set is a subset of every set.
- (f) False: the elements of $\{1, 2\}$ are the numbers 1 and 2, not the set $\{1\}$.

Check (c) with an example: $-4 = \frac{-4}{1}$, which is a quotient of integers with denominator not 0.

</details>

3\. Name the axiom that justifies each equation: (a) $8 + 5 = 5 + 8$, (b) $2 \cdot (3 \cdot x) = (2 \cdot 3) \cdot x$, (c) $\frac{1}{7} \cdot 7 = 1$, (d) $4(x + 9) = 4x + 36$, (e) $y + 0 = y$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The commutative property of addition (A2).
- (b) The associative property of multiplication (M3).
- (c) The multiplicative inverse property (M5), with $7^{-1} = \frac{1}{7}$.
- (d) The distributive property (D) gives $4x + 4 \cdot 9$, and $4 \cdot 9 = 36$ is arithmetic.
- (e) The additive identity property (A4).

Check each by substituting numbers: (a) $13 = 13$, (b) both sides are $6x$ for any $x$, such as 12 when $x = 2$, (c) $1 = 1$, (d) at $x = 1$ both sides are 40, (e) at $y = 9$ both sides are 9.

</details>

### Standard

4\. For each set and operation, say whether the set is closed under the operation. If it is, give a reason. If not, give a counterexample. (a) $\mathbb{N}$ under subtraction. (b) The odd integers under addition. (c) The irrational numbers under multiplication. (d) The even integers under addition. (e) $\mathbb{R}$ under division.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Not closed: $2 - 5 = -3$, which is not in $\mathbb{N}$.
- (b) Not closed: $1 + 3 = 4$, which is even.
- (c) Not closed: $\sqrt{2} \cdot \sqrt{2} = 2$, which is rational.
- (d) Closed. If $m$ and $n$ are integers, then $2m + 2n = 2(m + n)$ by D, and $m + n$ is an integer, so the sum is even.
- (e) Not closed: $1 \div 0$ is not a real number, since 0 has no reciprocal. Removing 0 from the divisor makes it closed: $a \cdot b^{-1}$ is real when $b \ne 0$.

Check (d) with numbers: $6 + 10 = 16$, which is even. Check (c) twice: $\sqrt{2} \cdot \sqrt{2} = 2$ and $2$ is rational, so the product of the two irrational numbers is not irrational.

</details>

5\. Prove multiplicative cancellation: if $a \ne 0$ and $ab = ac$, then $b = c$. Then show with an example that the condition $a \ne 0$ is needed.

<details class="solution" markdown>
<summary>Solution</summary>

We know M3, M4, M5, and that $ab = ac$. We want $b = c$. The plan is to multiply both sides by $a^{-1}$, which exists because $a \ne 0$.

$$
\begin{aligned}
b &= 1 \cdot b && \text{M4 and M2} \\
&= (a^{-1} \cdot a) \cdot b && \text{M5 and M2} \\
&= a^{-1} \cdot (a \cdot b) && \text{M3} \\
&= a^{-1} \cdot (a \cdot c) && \text{the hypothesis} \\
&= (a^{-1} \cdot a) \cdot c && \text{M3} \\
&= 1 \cdot c && \text{M5 and M2} \\
&= c && \text{M4 and M2}
\end{aligned}
$$

Without the condition, $0 \cdot 3 = 0 \cdot 5$ (both are 0 by Theorem 2), but $3 \ne 5$.

Check with $a = 4$: from $4b = 4 \cdot 7 = 28$, the proof says $b = 7$, and indeed $4 \cdot 7 = 28$.

</details>

6\. Use the order axioms. (a) Prove that if $a < b$ and $b < c$, then $a < c$. (b) Prove that if $a < b$, then $-b < -a$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) We know $b - a \in P$ and $c - b \in P$, and we want $c - a \in P$. The plan is to show that $c - a$ is the sum of those two numbers, and use O1.

$$
\begin{aligned}
(c - b) + (b - a) &= \bigl(c + (-b)\bigr) + \bigl(b + (-a)\bigr) && \text{definition of subtraction} \\
&= c + \Bigl((-b) + \bigl(b + (-a)\bigr)\Bigr) && \text{A3} \\
&= c + \Bigl(\bigl((-b) + b\bigr) + (-a)\Bigr) && \text{A3} \\
&= c + \bigl(0 + (-a)\bigr) && \text{A5 and A2} \\
&= c + (-a) = c - a && \text{A4}
\end{aligned}
$$

By O1 the sum of two elements of $P$ is in $P$, so $c - a \in P$, which says $a < c$.

(b) We want $(-a) - (-b) \in P$. By definition, $(-a) - (-b) = (-a) + \bigl(-(-b)\bigr)$, and $-(-b) = b$ from Theorem 1. So the expression is $(-a) + b = b + (-a) = b - a$ by A2, which is in $P$ because $a < b$. Hence $-b < -a$.

Check with numbers: $2 < 5$ and $5 < 9$ give $2 < 9$, and $2 < 5$ gives $-5 < -2$.

</details>

### Challenge

7\. Arithmetic mod $n$ means adding and multiplying as usual and keeping only the remainder after dividing by $n$ (the remainders from [long division](../../01-elementary/07-long-division.md)). (a) In arithmetic mod 6, find all pairs $a \le b$ from $\{1, 2, 3, 4, 5\}$ with $ab \equiv 0$, that is, with $ab$ leaving remainder 0 when divided by 6. (b) Explain why Theorem 3 shows that arithmetic mod 6 can't satisfy all the field axioms, and say which one fails. (c) Find the reciprocal of each of $1, 2, 3, 4$ in arithmetic mod 5, and check that no product of two of them is 0.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The products $ab$ for $a \le b$ in $\{1, \dots, 5\}$ that are multiples of 6 are $2 \cdot 3 = 6$ and $3 \cdot 4 = 12$. So the pairs are $(2, 3)$ and $(3, 4)$.

(b) Theorem 3 says that in a system satisfying the field axioms, $ab = 0$ forces $a = 0$ or $b = 0$. Here $2 \cdot 3 = 0$ with $2 \ne 0$ and $3 \ne 0$, so some axiom in the proof must fail. The proof used M3, M4, M5 and Theorem 2, and the one that fails is M5. The number 2 has no reciprocal mod 6: the products $2 \cdot k$ leave the remainders $0, 2, 4, 0, 2$ for $k = 1, \dots, 5$, never 1.

(c) Mod 5: $1 \cdot 1 = 1$, $2 \cdot 3 = 6 \equiv 1$, $3 \cdot 2 \equiv 1$ and $4 \cdot 4 = 16 \equiv 1$. So the reciprocals of $1, 2, 3, 4$ are $1, 3, 2, 4$. Every product of two of them is $1, 2, 3, 4, 6, 8, 9, 12$ or $16$ before reducing, and none of these is a multiple of 5.

Check (a) and (c) with a computer: the pairs with $ab \bmod 6 = 0$ are exactly $(2, 3)$ and $(3, 4)$, and all of $1, \dots, 4$ have a reciprocal mod 5. This is the first example of the pattern that arithmetic mod $n$ is a field exactly when $n$ is prime.

</details>

8\. This one reviews [roots, irrational numbers and types of numbers](../../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md). (a) Prove that if $r$ is rational and $s$ is irrational, then $r + s$ is irrational. (b) Prove that if $r$ is rational and not 0, and $s$ is irrational, then $rs$ is irrational. (c) Show that the sum of two irrational numbers can be rational.

<details class="solution" markdown>
<summary>Solution</summary>

(a) We know that $\mathbb{Q}$ is a field, so it is closed under subtraction. We want to show $r + s \notin \mathbb{Q}$. The plan is a proof by contradiction. Suppose $r + s = q$ with $q$ rational. Then $s = q - r$, which is a difference of two rationals, so $s \in \mathbb{Q}$ by closure. That contradicts $s$ being irrational, so $r + s$ is irrational.

(b) Suppose $rs = q$ with $q$ rational. Since $r \ne 0$ is rational, $r^{-1}$ is rational too (if $r = \frac{a}{b}$ with $a \ne 0$, then $r^{-1} = \frac{b}{a}$). Then $s = r^{-1} \cdot q$ is a product of two rationals, so $s \in \mathbb{Q}$ by closure, a contradiction.

(c) $\sqrt{2} + (-\sqrt{2}) = 0$, and both $\sqrt{2}$ and $-\sqrt{2}$ are irrational (by part (b) with $r = -1$). Another example is $(1 + \sqrt{2}) + (1 - \sqrt{2}) = 2$, with both summands irrational by part (a).

Look back: this is why part (b) needs $r \ne 0$: for $r = 0$ the product is 0, which is rational. Check numerically: $\frac{1}{2} + \sqrt{2} \approx 1.914$, and $3\sqrt{2} \approx 4.243$, neither of which has a terminating or repeating decimal.

</details>

## Where this shows up

- The rest of this chapter uses these rules without naming them: [linear and literal equations](02-linear-and-literal-equations.md) adds the same number to both sides and divides by nonzero expressions, and [compound inequalities and interval notation](03-compound-inequalities-and-interval-notation.md) writes solution sets with the notation of this lesson.
- Every proof lesson in the proofs folder cites reasons the way Theorems 1 to 4 do, and [sets and set operations](../../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) continues with unions, intersections and proofs about sets. Linear algebra defines a vector space over a field, and Gaussian elimination divides by pivots, which needs M5 ([systems and Gaussian elimination](../../05-university-core/06-linear-algebra/02-systems-and-gaussian-elimination.md)).
- In computing, arithmetic mod a prime is a field, which is what makes [divisibility and modular arithmetic](../../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md) and later RSA work, and floats break the associative property, which is why the order of a sum changes its last digits. In economics, a consumer's preference "bundle $A$ is at least as good as bundle $B$" is assumed to be an order like $\le$, in utility and indifference curves<!-- link: ../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md -->.
