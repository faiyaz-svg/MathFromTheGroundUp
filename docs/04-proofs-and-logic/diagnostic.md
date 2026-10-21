# Proofs and logic diagnostic

This quiz covers the 32 lessons of the proofs and logic folder: two questions on each of the first 31 lessons and one on the mixed proof practice lesson, 63 questions in all. Take it without notes, and write every answer down before you look at the answers. Most questions take a minute or two, and none asks for a full proof: you name a method, write a first line, find a flaw, give a counterexample or decide true or false with a reason. Plan on three or four sittings rather than one. In this book $\mathbb{N}$ includes 0.

Mark each answer right, wrong or guessed. A guess counts as wrong, even when it turns out right. Then do only the lessons behind the questions you marked wrong or guessed; the answer table names the lesson for each one. Several questions ask for a reason, and an answer without its reason counts as wrong.

## Language and notation

1\. The expression $n^2 + n + 41$ is prime for $n = 0, 1, \dots, 39$. Does that prove it is prime for every $n \in \mathbb{N}$? Give a value of $n$ that settles it.

2\. A proof begins "Let $m = 2k$ and $n = 2k$ be two even integers." What is wrong with this opening?

3\. Which of $0$, $1$ and $-7$ are prime? Which are even?

4\. True or false, with a reason: $12 \mid 3$, $3 \mid 0$ and $0 \mid 0$.

5\. Write the first line of a proof of "for every integer $n$, the number $n^2 + n$ is even", and the first line of a proof of "there exists an integer $n$ with $n^2 = 49$".

6\. Can you write "without loss of generality, $a$ is the even one" at the start of a proof of "if $ab$ is even, then $a$ is even"? Why or why not?

7\. Evaluate $\lfloor -3.7 \rfloor$, the empty sum $\sum_{i=1}^{0} i$ and the empty product $\prod_{i=1}^{0} i$.

8\. Let $f(x) = x + 1$ and $g(x) = 2x$. Find $(f \circ g)(3)$ and $(g \circ f)(3)$.

## Logic and sets

9\. Which of these are statements: "$x > 2$", "Is 7 prime?", "7 is prime", "$2 + 2 = 5$"? Give the truth value of each statement.

10\. Write "neither $P$ nor $Q$" and "not both $P$ and $Q$" in symbols.

11\. Is $P \Rightarrow Q$ true or false when $P$ is false and $Q$ is true? When both are false?

12\. Write "You may enter only if you have a ticket" as an if-then statement, and write its converse.

13\. How many rows does the truth table of $(P \wedge Q) \Rightarrow R$ have? In how many of them is the statement false?

14\. Is $\neg(P \vee Q)$ equivalent to $\neg P \vee \neg Q$? If not, give a row where they differ.

15\. Over $\mathbb{N}$, is $\forall x\ \exists y\ (y > x)$ true? Is $\exists y\ \forall x\ (y > x)$ true?

16\. Is "for every real $x$, $x^2 \ge x$" true? Is it true over $\mathbb{N}$?

17\. Negate "for every $n \in \mathbb{N}$, if $n$ is prime, then $n$ is odd". Which of the two statements is true?

18\. Translate into symbols, using $B(x)$ for "$x$ is a bird", $M(x)$ for "$x$ is a mammal", $V(x)$ for "$x$ may vote" and $C(x)$ for "$x$ is a club member": "No bird is a mammal", and "Only club members may vote".

19\. Let $S = \{\{1\}, 2\}$. Which of these are true: $1 \in S$, $\{1\} \in S$, $\{1\} \subseteq S$, $\{\{1\}\} \subseteq S$?

20\. Let $A = \{a, b, c, d\}$. How many elements does $\mathcal{P}(A)$ have? If $\lvert X \rvert = 10$, $\lvert Y \rvert = 7$ and $\lvert X \cap Y \rvert = 3$, what is $\lvert X \cup Y \rvert$?

## Core proof methods

21\. Write the first line and the target of a direct proof of "if $a \mid b$ and $b \mid c$, then $a \mid c$".

22\. True or false: if $n$ is odd, then $8 \mid n^2 - 1$. Give the identity that proves it, or a counterexample.

23\. A proof says "Let $p_1, \dots, p_n$ be all the primes. Then $N = p_1 p_2 \cdots p_n + 1$ is prime, which is a contradiction." Find the flaw, with a number that shows it.

24\. A text says "if $a \mid bc$, then $a \mid b$ or $a \mid c$" and uses it with $a = 6$. Is that allowed? When is the statement true?

25\. For $x > 0$, the inequality $x + \frac{4}{x} \ge 4$ is tight at $x = 2$. Which square does that point to, and what identity does it give?

26\. A student writes: "Start with $-1 = 1$. Square both sides: $1 = 1$. This is true, so $-1 = 1$." What is wrong?

27\. What are the possible remainders of a perfect square when divided by 3? By 4?

28\. A proof of "$x^2 \ge x$ for every real $x$" has two cases: $x \ge 1$ and $x \le 0$. Which $x$ are missing, and is the claim true there?

29\. State the contrapositive and the converse of "if $xy$ is irrational, then $x$ or $y$ is irrational". Which one is true?

30\. In a proof by the contrapositive, what is the negation of "$x$ is rational", and of "$P$ or $Q$"?

31\. Write the first line of a proof by contradiction that $\sqrt{2}$ is irrational, and name the contradiction it reaches.

32\. To prove "if $n$ is an integer and $3 \mid n^2$, then $3 \mid n$" by contradiction, exactly what do you assume?

33\. A proof of "if $n$ is even, then $n^2$ is even" writes $n = 2k$ and $n^2 = 4k^2$, then ends "so $n^2$ is even". Which justification is missing?

34\. A proof of $x^2 + y^2 \ge 2xy$ begins "Since $x^2 + y^2 \ge 2xy$, we have $(x - y)^2 \ge 0$." What kind of flaw is this, and how is it repaired?

## More proof methods

35\. To prove "$n$ is odd if and only if $n^2$ is odd", what do you assume and show in each half? Which half suits the contrapositive?

36\. Squaring $\sqrt{2x + 3} = x$ gives $x^2 - 2x - 3 = 0$. Which of its solutions solve the original equation?

37\. Find the quotient $q$ and the remainder $r$ with $-17 = 5q + r$ and $0 \le r < 5$.

38\. Why must two of any 5 integers differ by a multiple of 4? Name the principle and the boxes.

39\. True or false: $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$. If it is false, give sets $A$ and $B$ that show it.

40\. Write the first line of a proof that $A \subseteq B$, and the first line of a proof that $A = B$.

41\. Give a counterexample to "if $4 \mid n^2$, then $4 \mid n$".

42\. Is $n = 3$ a counterexample to "if $n$ is even, then $4 \mid n^2$"? Why or why not?

## Induction

43\. For $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$, check the base case and write the hypothesis and the goal of the inductive step.

44\. For which $n \in \mathbb{N}$ is $2^n > n^2$ true? Where does an induction proof of "$2^n > n^2$ for all large $n$" have to start?

45\. An inductive step proves $P(k+1)$ from $P(k)$ and $P(k-1)$, as for the Fibonacci numbers. How many base cases are needed, and why?

46\. With only 4-cent and 5-cent stamps, from which amount on is every postage possible? How many base cases does the step "add a 4-cent stamp" need?

47\. The set $B$ of balanced strings is defined by $\varepsilon \in B$, $x \in B$ gives $(x) \in B$, and $x, y \in B$ gives $xy \in B$. Is the string `)(` in $B$? Does it have equal numbers of "(" and ")"?

48\. A full binary tree with $i$ internal nodes has how many leaves? Write the key line of the structural induction step.

## Relations and functions

49\. Let $R = \{(1, 2), (2, 1)\}$ on $\{1, 2, 3\}$. Which of reflexive, symmetric, antisymmetric and transitive does $R$ have?

50\. Is divisibility antisymmetric on $\mathbb{Z}$? On the positive integers?

51\. Define $x \sim y$ on $\mathbb{R}$ to mean $\lvert x - y \rvert < 1$. Is $\sim$ an equivalence relation? If not, which property fails and why?

52\. Congruence modulo 3 is an equivalence relation on $\mathbb{Z}$. How many classes does it have, and which class contains $-7$?

53\. Order $\{2, 3, 4, 6\}$ by divisibility. List the minimal elements and say whether there is a least element.

54\. Is $\subseteq$ on $\mathcal{P}(\{1, 2\})$ a total order? Give two incomparable elements, or explain why none exist.

55\. A rule on the rationals says $f\!\left(\frac{a}{b}\right) = a + b$. Is it well defined?

56\. How many functions are there from $\{1, 2, 3\}$ to $\{a, b\}$, and from $\{a, b\}$ to $\{1, 2, 3\}$?

57\. Let $f \colon \mathbb{R} \to \mathbb{R}$ be $f(x) = x^2$. Is it injective? Surjective? Is it surjective as a map onto $[0, \infty)$?

58\. Write the first line of a proof that $f(x) = 3x - 7$ is injective and the first two lines of a proof that it is surjective from $\mathbb{R}$ to $\mathbb{R}$.

59\. Which of these sets are countable: $\mathbb{Z}$, $\mathbb{Q}$, the set of infinite binary sequences, the set of finite subsets of $\mathbb{N}$?

60\. In Cantor's diagonal argument, how is the new sequence built from a list $s^{(1)}, s^{(2)}, \dots$, and why is it missing from the list?

## Putting it together

61\. A proof of "if $n^2$ is even, then $n$ is even" begins "Suppose $n$ is even, so $n = 2k$, and then $n^2 = 4k^2$ is even." Which mistake is this?

62\. A student proves "$3 \mid 4^n + 1$ for every $n \in \mathbb{N}$" by showing that $3 \mid 4^k + 1$ implies $3 \mid 4^{k+1} + 1$. Is the step valid? Is the claim true?

63\. Name the method, and write the first line, for each claim: (a) $\log_2 3$ is irrational; (b) every integer $n \ge 12$ equals $4a + 5b$ with integers $a, b \ge 0$; (c) if $g \circ f$ is surjective, then $g$ is surjective.

## Answers

<details class="solution" markdown>
<summary>Answers</summary>

| Question | Answer | Working | Study |
|---|---|---|---|
| 1 | No; $n = 40$ | At $n = 40$ the value is $1681 = 41^2$. Forty true cases do not prove a "for every" claim. | [What is a proof](01-language-and-notation/01-what-is-a-proof.md) |
| 2 | It forces $m = n$ | One letter names one number, so the proof covers only equal even integers. Use $m = 2j$ and $n = 2k$. | [What is a proof](01-language-and-notation/01-what-is-a-proof.md) |
| 3 | None is prime; only 0 is even | A prime is greater than 1. And $0 = 2 \cdot 0$, while $-7 = 2(-4) + 1$. | [Definitions, theorems, lemmas and corollaries](01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md) |
| 4 | False, true, true | No integer $k$ gives $3 = 12k$. But $0 = 3 \cdot 0$ and $0 = 0 \cdot 1$. | [Definitions, theorems, lemmas and corollaries](01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md) |
| 5 | "Let $n$ be an integer."; "Take $n = 7$." | A "for every" claim starts with an arbitrary object; a "there exists" claim starts with a witness, then a check that $7^2 = 49$. | [Proof language: let, suppose, WLOG](01-language-and-notation/03-proof-language-let-suppose-wlog.md) |
| 6 | No | WLOG needs a symmetry, and the claim is not symmetric in $a$ and $b$. It is even false: $a = 3$, $b = 2$. | [Proof language: let, suppose, WLOG](01-language-and-notation/03-proof-language-let-suppose-wlog.md) |
| 7 | $-4$, 0, 1 | Floor rounds down. An empty sum is 0 and an empty product is 1. | [Reading math symbols](01-language-and-notation/04-reading-math-symbols.md) |
| 8 | 7 and 8 | Composition applies $g$ first: $f(6) = 7$. In the other order, $g(f(3)) = g(4) = 8$. | [Reading math symbols](01-language-and-notation/04-reading-math-symbols.md) |
| 9 | "7 is prime" (true) and "$2 + 2 = 5$" (false) | "$x > 2$" is an open sentence and "Is 7 prime?" is a question. | [Statements and connectives](02-logic-and-sets/01-statements-and-connectives.md) |
| 10 | $\neg P \wedge \neg Q$; $\neg(P \wedge Q)$ | "Neither" rules out both. "Not both" allows one of them to hold. | [Statements and connectives](02-logic-and-sets/01-statements-and-connectives.md) |
| 11 | True; true | A conditional is false only when $P$ is true and $Q$ is false. | [Conditionals and biconditionals](02-logic-and-sets/02-conditionals-and-biconditionals.md) |
| 12 | If you may enter, then you have a ticket; converse: if you have a ticket, you may enter | "$P$ only if $Q$" is $P \Rightarrow Q$ with $P$ = "you may enter". The converse is a different statement. | [Conditionals and biconditionals](02-logic-and-sets/02-conditionals-and-biconditionals.md) |
| 13 | 8 rows; false in 1 | The statement is false only when $P$ and $Q$ are true and $R$ is false. | [Truth tables and logical equivalence](02-logic-and-sets/03-truth-tables-and-logical-equivalence.md) |
| 14 | No; $P$ true and $Q$ false | The left side is false and the right side is true. The correct law is $\neg P \wedge \neg Q$. | [Truth tables and logical equivalence](02-logic-and-sets/03-truth-tables-and-logical-equivalence.md) |
| 15 | True; false | Take $y = x + 1$. For the second, $y > y$ fails at $x = y$. | [Quantifiers](02-logic-and-sets/04-quantifiers.md) |
| 16 | False over $\mathbb{R}$; true over $\mathbb{N}$ | At $x = \frac{1}{2}$, $\frac{1}{4} < \frac{1}{2}$. For $x \in \mathbb{N}$, either $x = 0$ or $x \ge 1$, and both give $x^2 \ge x$. | [Quantifiers](02-logic-and-sets/04-quantifiers.md) |
| 17 | There is a prime $n$ that is even; the negation is true | $n = 2$ is a counterexample to the original. The negation of an if-then is "and". | [Negation and translating English](02-logic-and-sets/05-negation-and-translating-english.md) |
| 18 | $\forall x\,(B(x) \Rightarrow \neg M(x))$; $\forall x\,(V(x) \Rightarrow C(x))$ | "No" is "for every, not". "Only club members" puts the membership condition after the arrow. | [Negation and translating English](02-logic-and-sets/05-negation-and-translating-english.md) |
| 19 | False, true, false, true | The elements of $S$ are $\{1\}$ and $2$. So $\{1\} \subseteq S$ would need $1 \in S$. | [Sets and set operations](02-logic-and-sets/06-sets-and-set-operations.md) |
| 20 | 16; 14 | A set with $n$ elements has $2^n$ subsets. And $10 + 7 - 3$. | [Sets and set operations](02-logic-and-sets/06-sets-and-set-operations.md) |
| 21 | Suppose $a \mid b$ and $b \mid c$, so $b = aj$ and $c = bk$ for integers $j$, $k$. Target: $c = am$ for an integer $m$. | Then $c = (aj)k = a(jk)$, and $jk$ is an integer. | [Direct proof](03-core-proof-methods/01-direct-proof.md) |
| 22 | True | For $n = 2k + 1$, $n^2 - 1 = 4k(k + 1)$, and $k(k + 1)$ is even. | [Direct proof](03-core-proof-methods/01-direct-proof.md) |
| 23 | $N$ need not be prime | For the first six primes, $N = 30031 = 59 \cdot 509$. In general $N$ has a prime divisor outside the list. | [How to read a proof](03-core-proof-methods/02-how-to-read-a-proof.md) |
| 24 | No; it holds for all $b$ and $c$ when $a$ is prime | Here $6 \mid 2 \cdot 3$, but $6 \nmid 2$ and $6 \nmid 3$. | [How to read a proof](03-core-proof-methods/02-how-to-read-a-proof.md) |
| 25 | $(x - 2)^2$; $x + \frac{4}{x} - 4 = \frac{(x-2)^2}{x}$ | The right side is nonnegative for $x > 0$, with equality only at $x = 2$. | [Scratch work and proof strategies](03-core-proof-methods/03-scratch-work-and-proof-strategies.md) |
| 26 | Squaring is not reversible | From $1 = 1$ you cannot get back to $-1 = 1$. The argument starts from the conclusion. | [Scratch work and proof strategies](03-core-proof-methods/03-scratch-work-and-proof-strategies.md) |
| 27 | 0 or 1 in both cases | Modulo 3, $n = 3q + r$ with $r = 0, 1, 2$ gives squares $\equiv 0, 1, 1$. Modulo 4 the squares are $\equiv 0, 1, 0, 1$. | [Proof by cases and WLOG](03-core-proof-methods/04-proof-by-cases-and-wlog.md) |
| 28 | $0 < x < 1$; the claim is false there | At $x = \frac{1}{2}$, $\frac{1}{4} < \frac{1}{2}$. | [Proof by cases and WLOG](03-core-proof-methods/04-proof-by-cases-and-wlog.md) |
| 29 | Contrapositive: if $x$ and $y$ are both rational, then $xy$ is rational (true). Converse: if $x$ or $y$ is irrational, then $xy$ is irrational (false). | The converse fails at $x = \sqrt{2}$, $y = 0$. | [Contrapositive proof](03-core-proof-methods/05-contrapositive-proof.md) |
| 30 | "$x$ is irrational"; "not $P$ and not $Q$" | De Morgan turns "or" into "and". | [Contrapositive proof](03-core-proof-methods/05-contrapositive-proof.md) |
| 31 | Suppose, for contradiction, that $\sqrt{2} = \frac{a}{b}$ in lowest terms. | Then $a^2 = 2b^2$, so $a$ and $b$ are both even, which contradicts lowest terms. | [Proof by contradiction](03-core-proof-methods/06-proof-by-contradiction.md) |
| 32 | $3 \mid n^2$ and $3 \nmid n$ | The negation of "if $P$, then $Q$" is "$P$ and not $Q$". | [Proof by contradiction](03-core-proof-methods/06-proof-by-contradiction.md) |
| 33 | $4k^2 = 2(2k^2)$ and $2k^2$ is an integer | An even number is $2m$ for an integer $m$, so the witness must be named and shown to be an integer. | [How to write a proof](03-core-proof-methods/07-how-to-write-a-proof.md) |
| 34 | Circular reasoning | The claim is used as a reason. Start from $(x - y)^2 \ge 0$ and expand to get $x^2 + y^2 \ge 2xy$. | [How to write a proof](03-core-proof-methods/07-how-to-write-a-proof.md) |
| 35 | ($\Rightarrow$) Assume $n$ is odd, show $n^2$ is odd. ($\Leftarrow$) Assume $n^2$ is odd, show $n$ is odd; the contrapositive suits this half. | Each half starts from its own hypothesis. | [If and only if proofs](04-more-proof-methods/01-if-and-only-if-proofs.md) |
| 36 | Only $x = 3$ | At $x = -1$ the left side is $\sqrt{1} = 1 \ne -1$. Squaring is not reversible. | [If and only if proofs](04-more-proof-methods/01-if-and-only-if-proofs.md) |
| 37 | $q = -4$, $r = 3$ | Check: $5(-4) + 3 = -17$. The remainder is never negative. | [Existence and uniqueness proofs](04-more-proof-methods/02-existence-and-uniqueness-proofs.md) |
| 38 | Pigeonhole; the 4 remainders modulo 4 | Five integers go into 4 boxes, so two share a remainder and their difference is a multiple of 4. | [Existence and uniqueness proofs](04-more-proof-methods/02-existence-and-uniqueness-proofs.md) |
| 39 | False; $A = \{1\}$, $B = \{2\}$ | The set $\{1, 2\}$ is in $\mathcal{P}(A \cup B)$, but it is a subset of neither $A$ nor $B$. | [Proofs about sets](04-more-proof-methods/03-proofs-about-sets.md) |
| 40 | "Let $x \in A$."; "We show $A \subseteq B$ and $B \subseteq A$." | For equality, prove both inclusions. | [Proofs about sets](04-more-proof-methods/03-proofs-about-sets.md) |
| 41 | $n = 2$ | Here $4 \mid 4$ but $4 \nmid 2$. | [Counterexamples and disproof](04-more-proof-methods/04-counterexamples-and-disproof.md) |
| 42 | No | A counterexample needs the hypothesis true and the conclusion false. The number 3 is not even. | [Counterexamples and disproof](04-more-proof-methods/04-counterexamples-and-disproof.md) |
| 43 | Base: $1 = \frac{1 \cdot 2}{2}$. Hypothesis: $\sum_{i=1}^{k} i = \frac{k(k+1)}{2}$. Goal: $\sum_{i=1}^{k+1} i = \frac{(k+1)(k+2)}{2}$. | The hypothesis is for one arbitrary $k$, and the goal has $k + 1$ in brackets. | [Mathematical induction](05-induction/01-mathematical-induction.md) |
| 44 | $n = 0, 1$ and all $n \ge 5$; start at $n = 5$ | At $n = 2, 3, 4$ the pairs $(2^n, n^2)$ are $(4, 4)$, $(8, 9)$ and $(16, 16)$. At $n = 5$, $32 > 25$. | [Mathematical induction](05-induction/01-mathematical-induction.md) |
| 45 | 2 | The step cites $P(k-1)$, which needs $k - 1 \ge n_0$, so the first two cases are checked by hand. | [Strong induction and well-ordering](05-induction/02-strong-induction-and-well-ordering.md) |
| 46 | From 12; 4 base cases | The largest unreachable amount is $4 \cdot 5 - 4 - 5 = 11$. The step cites $P(k+1-4)$, so 12, 13, 14, 15 are checked. | [Strong induction and well-ordering](05-induction/02-strong-induction-and-well-ordering.md) |
| 47 | No; yes | The string `)(` has one of each but no clause builds it. Equal counts do not make a string balanced. | [Recursive definitions and structural induction](05-induction/03-recursive-definitions-and-structural-induction.md) |
| 48 | $i + 1$ leaves; $\ell = \ell_1 + \ell_2 = (i_1 + 1) + (i_2 + 1) = i + 1$ | The new root is internal, so $i = i_1 + i_2 + 1$. | [Recursive definitions and structural induction](05-induction/03-recursive-definitions-and-structural-induction.md) |
| 49 | Symmetric only | The pair $(1, 1)$ is missing, so it is not reflexive. Both $(1,2)$ and $(2,1)$ with $1 \ne 2$, so not antisymmetric. Those two pairs need $(1,1)$ for transitivity. | [Relations and their properties](06-relations-and-functions/01-relations-and-their-properties.md) |
| 50 | No on $\mathbb{Z}$; yes on the positive integers | Here $2 \mid -2$ and $-2 \mid 2$ with $2 \ne -2$. For positive numbers, $a \mid b$ and $b \mid a$ force $a = b$. | [Relations and their properties](06-relations-and-functions/01-relations-and-their-properties.md) |
| 51 | No; transitivity fails | Here $0 \sim 0.6$ and $0.6 \sim 1.2$, but $\lvert 0 - 1.2 \rvert \ge 1$. | [Equivalence relations and partitions](06-relations-and-functions/02-equivalence-relations-and-partitions.md) |
| 52 | 3 classes; $-7 \in [2]$ | Since $-7 = 3(-3) + 2$, the remainder is 2. | [Equivalence relations and partitions](06-relations-and-functions/02-equivalence-relations-and-partitions.md) |
| 53 | Minimal: 2 and 3; no least element | Nothing in the set divides 2 or 3 other than themselves. No element divides all of the others. | [Partial orders](06-relations-and-functions/03-partial-orders.md) |
| 54 | No; $\{1\}$ and $\{2\}$ | Neither is a subset of the other. | [Partial orders](06-relations-and-functions/03-partial-orders.md) |
| 55 | No | Since $\frac{1}{2} = \frac{2}{4}$, the two names should agree, but the rule gives 3 and 6. | [Functions and well-definedness](06-relations-and-functions/04-functions-and-well-definedness.md) |
| 56 | $2^3 = 8$; $3^2 = 9$ | Each input chooses an output: $\lvert B \rvert^{\lvert A \rvert}$ functions. | [Functions and well-definedness](06-relations-and-functions/04-functions-and-well-definedness.md) |
| 57 | Neither; yes | Here $f(2) = f(-2)$, and $-1$ has no square root. The codomain is part of the question. | [Injective, surjective and bijective](06-relations-and-functions/05-injective-surjective-bijective.md) |
| 58 | "Suppose $f(a) = f(a')$."; "Let $b \in \mathbb{R}$. Take $a = \frac{b + 7}{3}$." | Then $f(a) = b + 7 - 7 = b$, and $a$ is real. Starting injectivity from $a = a'$ proves nothing. | [Injective, surjective and bijective](06-relations-and-functions/05-injective-surjective-bijective.md) |
| 59 | $\mathbb{Z}$, $\mathbb{Q}$ and the finite subsets of $\mathbb{N}$; not the binary sequences | The first three can be listed. The sequences are uncountable by the diagonal argument. | [Cardinality and countability](06-relations-and-functions/06-cardinality-and-countability.md) |
| 60 | $d_n = 1 - s^{(n)}_n$; it differs from row $n$ at position $n$ | So the new sequence equals no row. Adding $d$ to the list does not help, since the new list has a new diagonal. | [Cardinality and countability](06-relations-and-functions/06-cardinality-and-countability.md) |
| 61 | Proving the converse | It assumes the conclusion ($n$ even) and derives the hypothesis. | [Common proof mistakes](07-putting-it-together/01-common-proof-mistakes.md) |
| 62 | The step is valid; the claim is false | Since $4^{k+1} + 1 = 4(4^k + 1) - 3$, the step works. With no base case, $n = 0$ gives $2$, which 3 does not divide. | [Common proof mistakes](07-putting-it-together/01-common-proof-mistakes.md) |
| 63 | (a) contradiction: "Suppose $\log_2 3 = \frac{p}{q}$ with positive integers $p$, $q$." (b) strong induction: base cases 12, 13, 14, 15. (c) direct: "Let $c \in C$." | A negative claim suggests contradiction. The step "add a 4" cites $k - 3$. Surjectivity starts with an arbitrary element of the codomain. | [Mixed proof practice](07-putting-it-together/02-mixed-proof-practice.md) |

</details>

## What to do next

List the lessons behind every question you marked wrong or guessed, and do them in order, since later lessons build on earlier ones. Start each lesson with its quick check: if you get all three right, go straight to its practice problems. Use the chapter cheat sheets to review, such as [logic and sets](02-logic-and-sets/index.md#cheat-sheet), [core proof methods](03-core-proof-methods/index.md#cheat-sheet) or [induction](05-induction/index.md#cheat-sheet), and take this diagnostic again a few weeks after you finish the lessons, as [how to study](../00-start-here/how-to-study.md#use-the-diagnostics-well) recommends. When you can do the mixed proof practice without looking at the strategy table, or if you missed nothing, go on to the [university core](../05-university-core/index.md).
