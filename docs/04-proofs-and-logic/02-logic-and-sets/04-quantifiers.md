# Quantifiers

After this lesson you can read and write statements with "for every" ($\forall$) and "there exists" ($\exists$), decide how the domain changes a truth value, say why $\forall x\, \exists y$ and $\exists y\, \forall x$ differ, and name the right way to prove or disprove each kind of quantified statement.

Before this: [statements and connectives](01-statements-and-connectives.md) (open sentences are not statements), [conditionals and biconditionals](02-conditionals-and-biconditionals.md) and [real numbers, axioms and set notation](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) (sets and number systems).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Decide whether "for every $x$, $x^2 \ge x$" is true when $x$ ranges over (a) the natural numbers $\mathbb{N}$ and (b) the real numbers $\mathbb{R}$.
2. Write in symbols: "For every integer there is a larger integer." Is it true? Then write "There is an integer larger than every integer" and say whether it is true.
3. Is "for every real $x$, $x^2 > 0$" true? Is "there is a natural number $n$ with $n^2 = 49$" true? How would you justify each answer?

<details class="solution" markdown>
<summary>Answers</summary>

1. (a) True. For $x = 0$ and $x = 1$ we get $0 \ge 0$ and $1 \ge 1$, and for $x \ge 2$ we have $x \cdot x \ge 2x \ge x$. (b) False: $x = \frac{1}{2}$ gives $\frac{1}{4} \ge \frac{1}{2}$, which is false.
2. $\forall n \in \mathbb{Z},\ \exists m \in \mathbb{Z},\ m > n$ is true: take $m = n + 1$. The second is $\exists m \in \mathbb{Z},\ \forall n \in \mathbb{Z},\ m > n$, and it is false: for each candidate $m$, the choice $n = m$ gives $m > m$, which fails.
3. The first is false, and one counterexample justifies it: $x = 0$ has $x^2 = 0$, which is not greater than 0. The second is true, and one example justifies it: $n = 7$ gives $49$.

</details>

## The idea

Two sentences about locks and keys differ by a few words. "Every lock has a key" is true of every hardware store. "One key opens every lock" is true only of a master key, which is a very different object. Both sentences use the same ingredients, locks, keys and "opens", but they say different things because the order of "every" and "one" changed.

Last lesson ended with a gap: a sentence like "$x > 2$" is not a statement, because it has a free variable. Two things can fix this. You can give $x$ a value, which turns it into a statement about one number. Or you can say how many values are meant: "for every $x$" or "for some $x$". Those two phrases are the quantifiers, and they are what most theorems are made of. "Vertical angles are equal" means "for every pair of vertical angles, the angles are equal". "The equation $x^2 = 2$ has a real solution" means "there is a real number whose square is 2".

Quantifiers also explain why proofs look the way they do. To show that something holds for every number, you can't test all the numbers, so you take an arbitrary one and argue about it. To show that something exists, you only need to produce one example. To show that "for every" fails, one counterexample is enough. The rest of the lesson makes these rules exact.

## Definitions

### Open sentences and domains

An **open sentence** (or **predicate**) is a sentence $P(x)$ that contains a variable $x$ and becomes a statement when $x$ is replaced by an element of some set. That set is the **domain** (or universe of discourse), the collection of values the variable is allowed to take. For example, "$x$ is even" is an open sentence with domain $\mathbb{Z}$: $P(6)$ is true and $P(7)$ is false. A sentence can have two or more variables, as in $Q(x, y)$: "$x + y = 10$".

In plain words, an open sentence is a statement with a hole in it, and the domain says what can go in the hole. The same sentence can be true on one domain and false on another, so a statement with a quantifier always comes with a domain, spelled out or clear from context.

### The two quantifiers

The **universal statement** $\forall x \in D,\ P(x)$ (read "for every $x$ in $D$, $P(x)$") is true when $P(a)$ is true for every element $a$ of $D$, and false when $P(a)$ is false for at least one element $a$ of $D$.

The **existential statement** $\exists x \in D,\ P(x)$ (read "there exists an $x$ in $D$ such that $P(x)$") is true when $P(a)$ is true for at least one element $a$ of $D$, and false when $P(a)$ is false for every element $a$ of $D$.

In plain words, $\forall$ asks whether the property holds everywhere in the domain, and $\exists$ asks whether it holds somewhere. The symbol $\forall$ is an upside-down A (for "all") and $\exists$ is a backward E (for "exists"). A comma or a colon often follows the quantifier, and brackets can show how far the quantifier reaches: $\forall x\,(P(x) \Rightarrow Q(x))$.

Here are four statements on the domain $\mathbb{Z}$, to get the feel. The statement $\forall x \in \mathbb{Z},\ x^2 \ge 0$ is true. The statement $\exists x \in \mathbb{Z},\ x^2 = 49$ is true (take $x = 7$, or $-7$). The statement $\forall x \in \mathbb{Z},\ x > 0$ is false (take $x = -3$). The statement $\exists x \in \mathbb{Z},\ x^2 = 2$ is false, since $1^2 = 1$ and $2^2 = 4$ and larger squares only grow.

A variable that a quantifier governs is **bound**. A variable that no quantifier governs is **free**, and a sentence with a free variable is still not a statement. Bound variables are placeholders: $\forall x\,P(x)$ and $\forall y\,P(y)$ say the same thing, just as $\sum_{i=1}^{3} i$ and $\sum_{k=1}^{3} k$ are the same number.

### The domain matters

The same sentence can change truth value when the domain changes.

| Statement | Domain | Truth value |
|---|---|---|
| $\forall x,\ x^2 \ge x$ | $\mathbb{N}$ | true |
| $\forall x,\ x^2 \ge x$ | $\mathbb{R}$ | false ($x = \frac{1}{2}$) |
| $\exists x,\ x^2 = 2$ | $\mathbb{Q}$ | false ($\sqrt{2}$ is irrational) |
| $\exists x,\ x^2 = 2$ | $\mathbb{R}$ | true ($x = \sqrt{2}$) |
| $\exists x,\ 3x = 1$ | $\mathbb{Z}$ | false |
| $\exists x,\ 3x = 1$ | $\mathbb{Q}$ | true ($x = \frac{1}{3}$) |

Writing "$\forall x \in D$" and "$\exists x \in D$" makes the domain visible. When the domain is stated once for the whole passage ("throughout, $x$ and $y$ are real numbers"), authors drop it from each statement, and you should reinsert it mentally.

A restriction such as "for every $x > 0$" is shorthand with a conditional inside: $\forall x \in \mathbb{R},\ (x > 0 \Rightarrow P(x))$. And "there exists $x > 0$" is shorthand with an "and": $\exists x \in \mathbb{R},\ (x > 0 \wedge P(x))$. This pairing, $\forall$ with $\Rightarrow$ and $\exists$ with $\wedge$, matters in the common mistakes below.

If the domain is empty, $\forall x\,P(x)$ is true and $\exists x\,P(x)$ is false. This is vacuous truth again: with no elements, no element can fail $P$, and no element can satisfy it.

### Nested quantifiers

A statement can have several quantifiers, and their order matters. Take $P(x, y)$: "$y > x$", with $x$ and $y$ real numbers.

$$
\forall x\, \exists y\ (y > x) \qquad \text{versus} \qquad \exists y\, \forall x\ (y > x).
$$

The first says: "for every real $x$ there is a real $y$ bigger than it." It is true, with $y = x + 1$. The second says: "there is a real $y$ bigger than every real $x$." It is false, because $x = y$ makes $y > x$ fail. The sentences use the same $P$, the same variables and the same domain, and have opposite truth values.

In plain words, in $\forall x\, \exists y$ the choice of $y$ comes after $x$ is given, so $y$ may depend on $x$. In $\exists y\, \forall x$ the $y$ comes first, and one $y$ must work for every $x$. In the locks example, "every lock has a key" is $\forall L\, \exists K$, and "one key opens every lock" is $\exists K\, \forall L$.

Two quantifiers of the same kind can be swapped freely: $\forall x\, \forall y\, P(x, y)$ says the same as $\forall y\, \forall x\, P(x, y)$, and the same holds for two $\exists$. Mixed quantifiers cannot be swapped in general. One direction of swapping is always safe, and it is the first theorem of this lesson.

*Theorem 1.* Let $P(x, y)$ be an open sentence with $x$ in a domain $A$ and $y$ in a domain $B$. If $\exists y \in B,\ \forall x \in A,\ P(x, y)$ is true, then $\forall x \in A,\ \exists y \in B,\ P(x, y)$ is true.

What we know: there is some element $y_0$ of $B$ such that $P(x, y_0)$ holds for every $x$ in $A$. What we want: for each $x$ in $A$, some $y$ in $B$ with $P(x, y)$. The plan is to take an arbitrary $x$ and use the $y_0$ we already have.

*Proof.* Let $y_0 \in B$ be an element such that $P(x, y_0)$ holds for every $x \in A$. Let $x$ be an arbitrary element of $A$. Then $P(x, y_0)$ holds, so $y = y_0$ is an element of $B$ with $P(x, y)$. Since $x$ was arbitrary, $\forall x \in A,\ \exists y \in B,\ P(x, y)$. $\blacksquare$

Look back: the argument used the same $y_0$ for every $x$, which is more than $\forall x\,\exists y$ asks for. That surplus is why the reverse fails: "every lock has a key" does not give a master key.

## How to do it

### Proving and disproving quantified statements

There are four tasks, and each has a standard method.

| To show | Method | Starts like |
|---|---|---|
| $\forall x \in D,\ P(x)$ is true | Take an arbitrary element, and prove $P$ for it | "Let $x \in D$ be arbitrary." |
| $\exists x \in D,\ P(x)$ is true | Exhibit one element and check that $P$ holds | "Take $x = \dots$." |
| $\forall x \in D,\ P(x)$ is false | Find one counterexample: an element where $P$ fails | "Take $x = \dots$. Then $P(x)$ is false because ..." |
| $\exists x \in D,\ P(x)$ is false | Prove $P$ fails for every element: take an arbitrary one | "Let $x \in D$ be arbitrary. Then $P(x)$ fails because ..." |

The two middle rows are the cheap ones: one example. The first and last rows need an argument that covers the whole domain, and that argument can only use facts true of every element. The word "arbitrary" is the promise to use nothing special about $x$. If you start "Let $x = 3$", you have proved a statement about 3.

### Steps for a nested statement

1. Read the quantifiers from left to right. The first one is the outermost, and later variables may depend on earlier ones.
2. Handle the first quantifier by the table above. For $\forall x$, say "let $x$ be arbitrary", and from then on $x$ is a fixed but unknown element. For $\exists y$, you must name a $y$.
3. If an $\exists y$ comes after a $\forall x$, the $y$ you name may be a formula in $x$ (as in $y = x + 1$).
4. If an $\exists y$ comes before a $\forall x$, the $y$ you name cannot mention $x$, since $x$ doesn't exist yet. Then check that this one $y$ works for an arbitrary $x$.
5. Finish by checking that the property you needed holds.

## Worked examples

<div class="example" markdown>

### Example 1: the domain changes the answer

Decide whether each is true: (a) $\forall x \in \{1, 2, 3, 4\},\ x^2 > 8$. (b) $\exists x \in \{1, 2, 3, 4\},\ x^2 > 8$. (c) $\forall x \in \mathbb{N},\ x^2 \ge x$. (d) $\forall x \in \mathbb{R},\ x^2 \ge x$.

For (a), a universal statement over a finite domain is true only if every element passes. Test them: $1^2 = 1$ is not above 8, so (a) is false, and $x = 1$ is a counterexample.

For (b), one element is enough. The squares of 1, 2 and 3 are 1, 4 and 9, and $3^2 = 9 > 8$. So (b) is true, with the witness $x = 3$.

For (c), the domain is infinite, so testing isn't enough, and we need an argument for an arbitrary $x$. Let $x \in \mathbb{N}$. If $x = 0$, then $x^2 = 0 \ge 0 = x$. If $x \ge 1$, multiply the inequality $x \ge 1$ by $x$ (which is positive) to get $x^2 \ge x$. In both cases $x^2 \ge x$, so (c) is true.

For (d), the same inequality can fail between 0 and 1: $x = \frac{1}{2}$ gives $x^2 = \frac{1}{4}$, and $\frac{1}{4} \ge \frac{1}{2}$ is false. So (d) is false.

Check: (c) and (d) have the same sentence and different domains and opposite truth values. The natural numbers contain none of the numbers between 0 and 1 where the sentence fails.

</div>

<div class="example" markdown>

### Example 2: order of quantifiers

Let the domain of $x$ and $y$ be $\{1, 2, 3\}$ and let $P(x, y)$ be "$x + y = 4$". Decide the truth of (a) $\forall x\, \exists y\ P(x, y)$ and (b) $\exists y\, \forall x\ P(x, y)$. Then decide the same two statements for "$y > x$" with $x, y \in \mathbb{R}$.

For (a), follow Step 2 and Step 3: take $x$ and name a $y$ that depends on it. For $x = 1$ take $y = 3$, for $x = 2$ take $y = 2$, and for $x = 3$ take $y = 1$. In general $y = 4 - x$ works. So (a) is true.

For (b), by Step 4 we need one $y$ that works for all $x$. Try each: $y = 1$ needs $x = 3$ and fails for $x = 1$. The value $y = 2$ needs $x = 2$, and $y = 3$ needs $x = 1$. No single $y$ makes $x + y = 4$ for all three values of $x$, so (b) is false.

For "$y > x$" on $\mathbb{R}$: $\forall x\, \exists y\ (y > x)$ is true with $y = x + 1$, and $\exists y\, \forall x\ (y > x)$ is false because $x = y$ breaks it.

Check: Theorem 1 says that (b) true would force (a) true, and here (a) is true and (b) is false, which is allowed. The reverse direction is the one that doesn't hold.

</div>

<div class="example" markdown>

### Example 3: a universal proof and an existential disproof

(a) Prove that for every integer $n$, the number $n^2 + n$ is even. (b) Prove that "$\exists x \in \mathbb{R},\ x^2 + 1 = 0$" is false.

(a) What we know: $n$ is an integer, and an even number is $2k$ for an integer $k$. What we want: $n^2 + n = 2m$ for some integer $m$. The plan is to let $n$ be arbitrary and split into the two kinds of integer, even and odd.

*Proof.* Let $n$ be an arbitrary integer. If $n$ is even, write $n = 2k$. Then $n^2 + n = 4k^2 + 2k = 2(2k^2 + k)$, and $2k^2 + k$ is an integer. If $n$ is odd, write $n = 2k + 1$. Then $n^2 + n = (4k^2 + 4k + 1) + (2k + 1) = 4k^2 + 6k + 2 = 2(2k^2 + 3k + 1)$, and $2k^2 + 3k + 1$ is an integer. In both cases $n^2 + n$ is even. Since $n$ was arbitrary, the claim holds for every integer. $\blacksquare$

Check with numbers: $n = 5$ gives $30$, $n = -4$ gives $12$, and $n = 0$ gives $0$. All are even.

(b) To disprove an existential statement, show that the property fails for every real $x$. Let $x$ be an arbitrary real number. Then $x^2 \ge 0$, so $x^2 + 1 \ge 1 > 0$, and $x^2 + 1 \ne 0$. Since $x$ was arbitrary, no real number satisfies the equation. $\blacksquare$ Check: $x = 0$ gives 1, $x = 2$ gives 5, and no value gives 0.

</div>

<div class="example" markdown>

### Example 4: a nested proof (finish it yourself)

Prove that $\forall x \in \mathbb{R},\ \exists y \in \mathbb{R},\ x + y = 5$.

By Step 2, begin with "Let $x$ be an arbitrary real number." Now we need a $y$. By Step 3, $y$ may depend on $x$. Find a formula for $y$, and check that $x + y = 5$. Then say what changes if the statement is $\exists y\, \forall x\ (x + y = 5)$.

<details class="solution" markdown>
<summary>Finish</summary>

Take $y = 5 - x$. It is a real number, because the reals are closed under subtraction. Then $x + y = x + (5 - x) = 5$. Since $x$ was arbitrary, the statement holds for every real $x$. $\blacksquare$

For the swapped statement $\exists y\, \forall x\ (x + y = 5)$, the $y$ must be chosen before $x$ and cannot mention it. Try to find such a $y$: $x = 0$ forces $y = 5$, and $x = 1$ forces $y = 4$, so no single $y$ works, and the swapped statement is false.

Check: $x = 2$ gives $y = 3$, and $2 + 3 = 5$. $x = -7$ gives $y = 12$, and $-7 + 12 = 5$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: examples do not prove a universal statement. You can't show "$\forall n \in \mathbb{N},\ n^2 + n + 41$ is prime" by checking 40 cases. It holds for $n = 0$ to $39$ and fails at $n = 40$, where the value is $41^2$ (see the code box in [definitions, postulates and proof](../../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#in-code)). A universal statement needs an argument about an arbitrary element.

</div>

<div class="warning" markdown>

Watch out: one failure does not disprove an existential statement. That $x = 1$ doesn't satisfy $x^2 = 4$ says nothing about whether some $x$ does. To show an $\exists$ is false you must show failure for every element of the domain.

</div>

<div class="warning" markdown>

Watch out for pairing the wrong connective with the quantifier. "Some student in the class is a CS major who likes math" is $\exists x\,(C(x) \wedge M(x))$. Writing $\exists x\,(C(x) \Rightarrow M(x))$ is almost always wrong: it is true as soon as there is one student who isn't a CS major, since then $C(x)$ is false and the conditional holds vacuously. In the same way, "every CS major likes math" is $\forall x\,(C(x) \Rightarrow M(x))$, and writing $\forall x\,(C(x) \wedge M(x))$ would claim that everybody is a CS major.

</div>

<div class="warning" markdown>

Watch out for the order of quantifiers. The form $\forall x\, \exists y$ lets $y$ depend on $x$, and $\exists y\, \forall x$ doesn't. When you translate English, read the order from the sentence: "everyone has someone they trust" is $\forall \exists$, and "there is someone everyone trusts" is $\exists \forall$.

</div>

<div class="warning" markdown>

Watch out for choosing the arbitrary element. "Let $x$ be an arbitrary integer. Say $x = 2k$" assumes without saying so that $x$ is even. If the argument only works for even $x$, the proof covers only even $x$. Either split into cases, as in Example 3, or find an argument that covers every $x$ at once.

</div>

A quantifier reaches only as far as its brackets. The statements $\forall x\,(P(x) \vee Q(x))$ and $(\forall x\,P(x)) \vee (\forall x\,Q(x))$ are different statements. The first says each $x$ has at least one of the properties, and the second says that one of the properties is shared by all. On the integers with $P$ meaning "even" and $Q$ meaning "odd", the first is true and the second is false.

## Tricks and shortcuts

Think of $\forall$ as a long "and" and $\exists$ as a long "or". On the domain $\{1, 2, 3\}$, the statement $\forall x\,P(x)$ is $P(1) \wedge P(2) \wedge P(3)$, and $\exists x\,P(x)$ is $P(1) \vee P(2) \vee P(3)$. This explains why one counterexample kills a $\forall$ (one false part ruins an "and"), why one witness proves an $\exists$ (one true part rescues an "or"), and, next lesson, why negating a quantifier works like De Morgan's laws.

To test a nested statement quickly, make a small table. Put the values of $x$ in rows and the values of $y$ in columns, and fill each cell with the truth value of $P(x, y)$. Then $\forall x\, \exists y$ asks that every row has a T, and $\exists y\, \forall x$ asks that some column is all T. In Example 2 (a), the table for "$x + y = 4$" has one T in each row (on the anti-diagonal) and no all-T column.

When you prove $\forall x\, \exists y$, find $y$ by solving for it. In Example 4, "I want $x + y = 5$" gives $y = 5 - x$ at once. Work out the formula on scratch paper, and then write the proof in the order a reader needs: "let $x$ be arbitrary; take $y = 5 - x$; check".

## In code

A quantifier over a finite set is a loop. `all(...)` is $\forall$, `any(...)` is $\exists$, and nesting them in the order of the quantifiers gives the nested statements. This can only test a finite domain, so it can find counterexamples but can't prove a statement about all integers.

<details class="code" markdown>
<summary>In code</summary>

```python
D = [1, 2, 3]

print(all(x * x >= x for x in D))            # True: for all x in D, x*x >= x
print(any(x * x == 4 for x in D))            # True: x = 2 is a witness

# nested: for all x there is a y, versus there is a y for all x
print(all(any(x + y == 4 for y in D) for x in D))    # True
print(any(all(x + y == 4 for x in D) for y in D))    # False

# find a counterexample, or return None
print(next((x for x in range(-5, 6) if not x * x >= x), None))   # None: no integer counterexample
print(next((x / 2 for x in range(-5, 6) if not (x / 2) ** 2 >= x / 2), None))   # 0.5

# an empty domain: "for all" is true, "there exists" is false
print(all(x > 100 for x in []), any(x > 100 for x in []))   # True False

# the same nested check as an explicit double loop
ok = True
for x in D:
    found = False
    for y in D:
        if x + y == 4:
            found = True
    if not found:
        ok = False
print(ok)   # True
```

The first two lines test a universal and an existential statement. The two nested lines are the pair from Example 2, and the order of `all` and `any` is the order of the quantifiers. The `next(...)` lines search for a counterexample: the first is over integers and finds none (so it prints `None`), because $x^2 \ge x$ holds for every integer, and the second tries halves and finds $\frac{1}{2}$. The empty-domain line shows vacuous truth. A search that finds nothing is evidence and not a proof, as in the earlier lesson's search for a prime-generating formula.

</details>

## FAQ

### Why is a "for all" statement over an empty set true?

Because it can only fail if some element fails, and there are no elements. "Every unicorn in this room is purple" can't be refuted, since you can't point at an unpurple unicorn. It is the same fact as the empty set being a subset of every set. If "for all" over an empty set were false, "every element of $A$ is in $B$" would stop being the same as $A \subseteq B$ when $A$ is empty, and the definition of a subset would need a special case.

### Does the letter I use for the variable matter?

No. The statements $\forall x\,P(x)$, $\forall t\,P(t)$ and $\forall \clubsuit\,P(\clubsuit)$ all say the same thing. What matters is that two different variables stay different, and that you don't reuse a letter that is already in use: $\forall x\, \exists x\ (\dots)$ is confusing, because it is unclear which $x$ is meant inside.

### Can I swap two quantifiers?

Two of the same kind, yes: $\forall x\, \forall y$ is the same as $\forall y\, \forall x$, and $\exists x\, \exists y$ is the same as $\exists y\, \exists x$. For a mixed pair, only the direction in Theorem 1 holds: $\exists y\, \forall x$ implies $\forall x\, \exists y$. The converse fails, as shown by the numbers in Example 2.

### Why can the $y$ depend on $x$ in $\forall x\, \exists y$?

Because the statement is read left to right as a game. You are handed an arbitrary $x$ (by an opponent who wants to break the claim), and then you must produce a $y$. You see $x$ before you choose, so your $y$ can use it. In $\exists y\, \forall x$ the order is reversed: you commit to $y$, and then the opponent picks the worst $x$ for it.

## Practice

### Warm-up

1\. Let the domain be $\{-2, -1, 0, 1, 2\}$. Decide whether each is true. (a) $\forall x,\ x^2 \le 4$. (b) $\exists x,\ x^2 = 1$. (c) $\forall x,\ x \le 1$. (d) $\exists x,\ 2x = 3$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) True: the squares are $4, 1, 0, 1, 4$, and all are at most 4.
- (b) True: $x = 1$ (or $-1$) is a witness.
- (c) False: $x = 2$ is a counterexample.
- (d) False: $2x = 3$ needs $x = 1.5$, which is not in the domain, and none of the five values works ($-4, -2, 0, 2, 4$).

Check (a) and (c) against the "big and" view: (a) is five true facts joined by "and", and (c) has a false fact among the five.

</details>

2\. Translate into symbols, with the domain and the predicates stated. (a) "Every even integer is divisible by 2." (b) "Some prime number is even." (c) "No integer is both even and odd."

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $\forall n \in \mathbb{Z},\ (n \text{ is even} \Rightarrow 2 \mid n)$. A restricted "for every" uses an arrow.
- (b) $\exists p \in \mathbb{Z},\ (p \text{ is prime} \wedge p \text{ is even})$. A restricted "there exists" uses "and". It is true, with $p = 2$.
- (c) $\forall n \in \mathbb{Z},\ \neg(n \text{ is even} \wedge n \text{ is odd})$.

Check (a) and (b) against the common mistakes: writing (b) with an arrow would make it true because of a single odd number, which isn't what the sentence says.

</details>

3\. On the domain $\mathbb{R}$, decide whether each is true. (a) $\forall x\, \exists y\ (y = 2x)$. (b) $\exists y\, \forall x\ (y = 2x)$. (c) $\forall x\, \exists y\ (y^2 = x)$. (d) $\forall x\, \exists y\ (y^3 = x)$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) True: take $y = 2x$.
- (b) False: one $y$ would need to equal $2x$ for all $x$, but $x = 0$ forces $y = 0$ and $x = 1$ forces $y = 2$.
- (c) False: $x = -1$ has no real $y$ with $y^2 = -1$, since squares are not negative.
- (d) True: every real number has a real cube root, $y = \sqrt[3]{x}$, including negative $x$ (for $x = -8$, $y = -2$).

Check (c) and (d): $(-2)^2 = 4$ is positive, and $(-2)^3 = -8$ is negative, so cubes reach all the reals and squares do not.

</details>

### Standard

4\. Prove or disprove. (a) $\forall n \in \mathbb{Z},\ n^2 \ge n$. (b) $\exists x \in \mathbb{R},\ \forall y \in \mathbb{R},\ xy = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) True. What we know: $n$ is an arbitrary integer. We want $n^2 \ge n$. The plan is cases on the sign of $n$.

*Proof.* Let $n$ be an arbitrary integer. If $n \ge 1$, multiplying $n \ge 1$ by the positive number $n$ gives $n^2 \ge n$. If $n = 0$, then $n^2 = 0 = n$. If $n \le -1$, then $n^2 \ge 0 > n$, since a square is not negative and $n$ is. In every case $n^2 \ge n$. $\blacksquare$

(b) True. The statement has $\exists$ first, so we must name an $x$ that doesn't depend on $y$. Take $x = 0$. Let $y$ be an arbitrary real number. Then $xy = 0 \cdot y = 0$. $\blacksquare$

Check: (a) at $n = -3$ gives $9 \ge -3$, at $n = 1$ gives $1 \ge 1$. (b) $0 \cdot 7 = 0$ and $0 \cdot (-2.5) = 0$. The domain matters: (a) fails over the reals at $n = \frac{1}{2}$.

</details>

5\. Show that $\forall x \in \mathbb{R},\ \exists y \in \mathbb{R},\ xy = 1$ is false, and that it becomes true when the domain for $x$ and $y$ is $\mathbb{R} \setminus \{0\}$.

<details class="solution" markdown>
<summary>Solution</summary>

To disprove a $\forall$, we need a counterexample: a real $x$ for which no $y$ works. Take $x = 0$. For every real $y$, $0 \cdot y = 0 \ne 1$ (a product with 0 is 0, as proved in the [axioms lesson](../../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#proving-facts-from-the-axioms)). So no $y$ works for $x = 0$, and the statement is false.

On $\mathbb{R} \setminus \{0\}$, let $x$ be an arbitrary nonzero real number. Take $y = \frac{1}{x}$. It is a nonzero real number, so it is in the domain, and $xy = x \cdot \frac{1}{x} = 1$. So the statement is true on that domain. $\blacksquare$

Check: $x = 4$ has $y = \frac{1}{4}$, and $4 \cdot \frac{1}{4} = 1$. $x = -0.5$ has $y = -2$, and the product is $1$.

</details>

6\. Let the domain be all people, and let $M(x, y)$ mean "$x$ is the mother of $y$". Write each in symbols and say whether it is true in the real world. (a) Everyone has a mother. (b) Someone is everyone's mother. (c) No one is their own mother.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $\forall y\, \exists x\ M(x, y)$. True: each person has (or had) a mother, and the mother can differ from person to person.
- (b) $\exists x\, \forall y\ M(x, y)$. False: it would need one person who is the mother of every person, including herself.
- (c) $\forall x\ \neg M(x, x)$. True.

Check (a) against (b): the two have the same predicate and the same domain, and the quantifiers in the opposite order make one true and the other false. In (a) the mother depends on the child.

</details>

### Challenge

7\. Prove that for every real number $x > 0$ there is a real number $y$ with $0 < y < x$. Then explain why "there is a real number $y$ such that for every $x > 0$, $0 < y < x$" is false.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $x$ is an arbitrary positive real. We want a $y$ strictly between 0 and $x$. The plan is to name $y$ as a formula in $x$: half of $x$.

*Proof.* Let $x > 0$ be arbitrary and take $y = \frac{x}{2}$. Since $x > 0$, we have $\frac{x}{2} > 0$. Also $x - \frac{x}{2} = \frac{x}{2} > 0$, so $\frac{x}{2} < x$. Thus $0 < y < x$. Since $x$ was arbitrary, the statement holds for every $x > 0$. $\blacksquare$

The swapped statement is $\exists y\, \forall x > 0\ (0 < y < x)$. Suppose such a $y$ existed. It would be positive, so $x = y$ is an allowed value, but then $y < x$ reads $y < y$, which is false. Or take $x = \frac{y}{2}$, which is positive and smaller than $y$. So no $y$ works for every $x$.

Check: for $x = 0.001$ the proof gives $y = 0.0005$, and $0 < 0.0005 < 0.001$. There is no smallest positive real number: whatever $y$ you propose, $\frac{y}{2}$ is smaller. This "for every small number there is a smaller one" pattern appears in limit proofs.

</details>

8\. (Reviews [conditionals and biconditionals](02-conditionals-and-biconditionals.md).) Write the statement "if $x > 2$, then $x^2 > 4$" for real $x$ as a quantified statement. Then write its converse as a quantified statement and decide whether it is true.

<details class="solution" markdown>
<summary>Solution</summary>

A theorem of this shape has a hidden "for every". The statement is $\forall x \in \mathbb{R},\ (x > 2 \Rightarrow x^2 > 4)$. It is true: if $x > 2$ then $x$ is positive, and $x \cdot x > 2 \cdot 2$.

The converse swaps the two parts inside the brackets: $\forall x \in \mathbb{R},\ (x^2 > 4 \Rightarrow x > 2)$. It is false, and one counterexample shows it: $x = -3$ has $x^2 = 9 > 4$ and $x = -3$ is not greater than 2.

Check: at $x = -3$ the converse's hypothesis is true and its conclusion is false, which is the one false row of the conditional's table. The quantifier $\forall$ stayed in front in both statements, and only the conditional inside was flipped.

</details>

## Where this shows up

- The next lesson, [negation and translating English](05-negation-and-translating-english.md), shows how to negate a quantified statement and how to translate English sentences with hidden quantifiers. The proof methods in the next chapters ([direct proof](../03-core-proof-methods/01-direct-proof.md), [existence and uniqueness proofs](../04-more-proof-methods/02-existence-and-uniqueness-proofs.md), [counterexamples and disproof](../04-more-proof-methods/04-counterexamples-and-disproof.md)) are the four tasks in the table above, developed one at a time.
- The definition of a limit has the shape $\forall \varepsilon\, \exists \delta\, \forall x$, so the order of quantifiers is its whole content (the epsilon-delta definition<!-- link: ../../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md -->). A sequence converges when "for every tolerance, from some point on the terms stay within it". In algorithms courses, "for every input of size $n$, the algorithm uses at most $cn \log n$ steps" is a quantified statement, and a lower-bound argument produces the worst-case input, which is the witness for a $\exists$.
- In economics, "for every price there is a quantity demanded" is $\forall \exists$, and market equilibrium is $\exists p\ (Q_d(p) = Q_s(p))$, an existence claim that needs a proof, as in supply and demand equilibrium algebra<!-- link: ../../07-economics-math/02-markets/03-supply-and-demand-equilibrium-algebra.md -->.
