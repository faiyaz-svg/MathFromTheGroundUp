# Symbols and notation

This page lists the symbols used in the book, grouped by area. Each row gives the symbol, the LaTeX that produces it, how to say it aloud, what it means, a small example and the lesson that teaches it. Lessons that are not written yet are named without a link.

## How to read a symbol you don't know

1. Decide what kind of thing the expression is: a number, a set, a function or a statement (something that is true or false). The expression $12/3$ is a number, $4$, while $3 \mid 12$ is a statement, and a true one. Many errors in proofs come from mixing the kinds, such as writing $3 \mid 12 = 4$.
2. Look at where the symbol sits. A symbol between two things is either an operation, which builds a new object ($A \cup B$ is a set), or a relation, which makes a statement ($A \subseteq B$ is true or false). A symbol in front acts on what follows, as in $\neg P$ or $\sum$, and a pair of symbols around something acts on what is inside, as in $\lvert x \rvert$ or $\lfloor x \rfloor$.
3. Say it aloud with the "How to say it" column. A formula read aloud should sound like a sentence: $\forall x \in \mathbb{R},\ x^2 \ge 0$ reads "for every real number $x$, $x$ squared is at least $0$".
4. Check the author's own notation section before this page. Books redefine symbols (the rows for $\mathbb{N}$, $\subset$ and $\lg$ below show three that differ between books), and the author's definition is the one that counts.
5. Try the definition on a small example before you read on.

If a symbol isn't on this page, draw it in [Detexify](https://detexify.kirelabs.org/classify.html), which tells you its LaTeX command. Searching for the command's name usually finds what it means.

## Numbers and arithmetic

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $\times$ | `\times` | times | Multiplication. Algebra replaces it with $\cdot$ or writes letters side by side, so it can't be confused with $x$. | $3 \times 4 = 12$ | [Multiplication and times tables](../01-elementary/03-multiplication-and-times-tables.md) |
| $\cdot$ | `\cdot` | times | Multiplication, in algebra. Writing $3x$ means $3 \cdot x$. | $2 \cdot 5 = 10$ | [Variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md) |
| $\div$ | `\div` | divided by | Division. After middle school a fraction bar or a slash replaces it. | $12 \div 4 = 3$ | [Division facts and remainders](../01-elementary/06-division-facts-and-remainders.md) |
| $/$, $\frac{a}{b}$ | `/`, `\frac{a}{b}` | a over b, a divided by b | Division, or the fraction with numerator $a$ and denominator $b$ | $7/2 = \frac{7}{2} = 3.5$ | [Fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md) |
| $\pm$ | `\pm` | plus or minus | Two values at once, one with $+$ and one with $-$ | $3 \pm 2$ means $5$ or $1$ | [Solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md) |
| $\approx$ | `\approx` | is approximately equal to | Close in value but not exactly equal | $\pi \approx 3.14$ | [Place value and rounding](../01-elementary/01-place-value-and-rounding.md) |
| $\ne$ | `\ne` or `\neq` | is not equal to | The two sides have different values | $2 + 2 \ne 5$ | [Inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md) |
| $<$, $\le$ | `<`, `\le` or `\leq` | is less than; is less than or equal to | Order on the number line. The line under $\le$ allows the two sides to be equal. | $3 \le 3$ is true, $3 < 3$ is false | [Inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md) |
| $>$, $\ge$ | `>`, `\ge` or `\geq` | is greater than; is greater than or equal to | The same order, read from the other side | $x \ge 0$ means $x$ is $0$ or positive | [Inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md) |
| $a \mid b$ | `a \mid b` | a divides b | There is an integer $k$ with $b = ka$. This is a statement (true or false), not a number. | $3 \mid 12$ is true; $5 \nmid 12$ (typed `\nmid`) | Divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md --> |
| $a \bmod n$ | `a \bmod n` | a mod n | The remainder when $a$ is divided by $n$. Python writes `a % n`. | $17 \bmod 5 = 2$ | Divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md --> |
| $n!$ | `n!` | n factorial | The product $1 \cdot 2 \cdot 3 \cdots n$, with $0! = 1$ | $5! = 120$ | [Counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md) |
| $a^n$ | `a^n`, `a^{10}` | a to the n-th power; a squared when $n = 2$; a cubed when $n = 3$ | The base $a$ multiplied by itself $n$ times, where $n$ is the exponent. Braces group an exponent longer than one character. | $2^5 = 32$ | [Exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md) |
| $\sqrt{x}$, $\sqrt[n]{x}$ | `\sqrt{x}`, `\sqrt[n]{x}` | the square root of x; the n-th root of x | For $x \ge 0$, the non-negative number whose square is $x$. The $n$-th root is the number whose $n$-th power is $x$ (the non-negative one when $n$ is even). | $\sqrt{49} = 7$, $\sqrt[3]{8} = 2$ | [Roots, irrationals and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md) |
| $\lvert x \rvert$ | `\lvert x \rvert` | the absolute value of x | The distance from $x$ to $0$ on the number line, so never negative | $\lvert -4 \rvert = 4$ | [Negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md) |
| $\lfloor x \rfloor$ | `\lfloor x \rfloor` | the floor of x | The greatest integer less than or equal to $x$ (round down) | $\lfloor 3.7 \rfloor = 3$, $\lfloor -3.7 \rfloor = -4$ | [Piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md) |
| $\lceil x \rceil$ | `\lceil x \rceil` | the ceiling of x | The least integer greater than or equal to $x$ (round up) | $\lceil 3.2 \rceil = 4$, $\lceil -3.2 \rceil = -3$ | [Piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md) |
| $\%$ | `\%` | percent | Per hundred: $x\%$ means $\frac{x}{100}$ | $15\% = 0.15$ | [Percents](../02-middle-school/02-ratios-rates-percents/03-percents.md) |

Inside math, a bare `%` starts a LaTeX comment and hides the rest of the line, so write `\%`. Absolute value can also be typed with the bar key, as `|x|`. This book writes `\lvert x \rvert` because a bare bar ends a cell in a Markdown table.

## Number sets

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $\mathbb{N}$ | `\mathbb{N}` | N, the natural numbers | In this book, $\{0, 1, 2, 3, \dots\}$. Many books start at $1$ instead, so check the book you are reading. | $0 \in \mathbb{N}$, $-1 \notin \mathbb{N}$ | [Roots, irrationals and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md) |
| $\mathbb{Z}$ | `\mathbb{Z}` | Z, the integers | The whole numbers and their negatives, $\{\dots, -2, -1, 0, 1, 2, \dots\}$ | $-7 \in \mathbb{Z}$ | [Roots, irrationals and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md) |
| $\mathbb{Q}$ | `\mathbb{Q}` | Q, the rational numbers | Fractions $\frac{a}{b}$ with $a$ and $b$ integers and $b \ne 0$ | $-\frac{3}{4} \in \mathbb{Q}$, $0.25 \in \mathbb{Q}$ | [Roots, irrationals and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md) |
| $\mathbb{R}$ | `\mathbb{R}` | R, the real numbers | Every point on the number line, rational or irrational | $\sqrt{2} \in \mathbb{R}$ but $\sqrt{2} \notin \mathbb{Q}$ | [Roots, irrationals and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md) |
| $\mathbb{C}$ | `\mathbb{C}` | C, the complex numbers | Numbers $a + bi$ with $a$ and $b$ real and $i^2 = -1$ | $3 - 2i \in \mathbb{C}$ | [Complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md) |
| $\mathbb{Z}^+$ | `\mathbb{Z}^+` | Z plus, the positive integers | $\{1, 2, 3, \dots\}$. In the same way, $\mathbb{R}^+$ is the positive reals. Some books write $\mathbb{Z}_{>0}$. | $1 \in \mathbb{Z}^+$, $0 \notin \mathbb{Z}^+$ | [Real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) |
| $\mathbb{R}^n$ | `\mathbb{R}^n` | R n, or R to the n | Ordered lists $(x_1, \dots, x_n)$ of $n$ real numbers | $(1, -2, 0.5) \in \mathbb{R}^3$ | [Vectors, dot product and span](../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md) |

When the start of $\mathbb{N}$ matters, the clearest choice is to avoid it and write $\mathbb{Z}^+$ for $\{1, 2, 3, \dots\}$ or $\mathbb{Z}_{\ge 0}$ for $\{0, 1, 2, \dots\}$.

## Sets

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $\in$ | `\in` | is an element of, is in | Membership. The left side is an element and the right side is a set. | $3 \in \{1, 2, 3\}$ | [Real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) |
| $\notin$ | `\notin` | is not an element of | Not a member | $4 \notin \{1, 2, 3\}$ | [Real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) |
| $\{1, 2, 3\}$ | `\{ 1, 2, 3 \}` | the set containing 1, 2 and 3 | A set given by listing its elements. Order and repeats don't matter. | $\{1, 2\} = \{2, 1, 1\}$ | [Real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) |
| $\{x \in A : \dots\}$ | `\{ x \in \mathbb{Z} : x > 0 \}` | the set of x in Z such that x is greater than 0 | Set-builder notation: the elements of $A$ that satisfy the condition after the colon | $\{x \in \mathbb{Z} : x^2 = 4\} = \{-2, 2\}$ | [Real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) |
| $\{x \in A \mid \dots\}$ | `\{ x \in \mathbb{Z} \mid x > 0 \}` | the set of x in Z such that x is greater than 0 | The same as the colon form; each book picks one. Type the bar as `\mid`. | $\{n \in \mathbb{N} \mid n < 3\} = \{0, 1, 2\}$ | [Real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) |
| $\subseteq$ | `\subseteq` | is a subset of | Every element of the left set is also in the right set. Every set is a subset of itself. | $\{1, 2\} \subseteq \{1, 2, 3\}$ and $A \subseteq A$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $\subsetneq$ | `\subsetneq` | is a proper subset of | A subset that is not the whole set: $A \subseteq B$ and $A \ne B$ | $\{1\} \subsetneq \{1, 2\}$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $\subset$ | `\subset` | is a subset of, or is a proper subset of | Books differ: some use $\subset$ to mean $\subseteq$, others to mean $\subsetneq$. This book writes $\subseteq$ or $\subsetneq$ and avoids $\subset$. | $\{1\} \subset \{1, 2\}$ is true under both readings | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $\cup$ | `\cup` | union | The elements in $A$, in $B$, or in both | $\{1, 2\} \cup \{2, 3\} = \{1, 2, 3\}$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $\cap$ | `\cap` | intersection | The elements in both sets | $\{1, 2\} \cap \{2, 3\} = \{2\}$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $\setminus$ | `\setminus` | minus, set difference | The elements of $A$ that are not in $B$. Some books write $A - B$. | $\{1, 2, 3\} \setminus \{2\} = \{1, 3\}$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $A^c$, $\overline{A}$ | `A^c`, `\overline{A}` | the complement of A | The elements of the universal set $U$ that are not in $A$. Some books write $A'$. | If $U = \{1, \dots, 5\}$ and $A = \{1, 2\}$, then $A^c = \{3, 4, 5\}$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $\emptyset$ | `\emptyset` or `\varnothing` | the empty set | The set with no elements, $\{\}$. It is a subset of every set. | $\{1\} \cap \{2\} = \emptyset$, and $\emptyset \ne \{\emptyset\}$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $A \times B$ | `A \times B` | A cross B, the Cartesian product | All ordered pairs $(a, b)$ with $a \in A$ and $b \in B$ | $\{1, 2\} \times \{0\} = \{(1, 0), (2, 0)\}$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $\mathcal{P}(A)$ | `\mathcal{P}(A)` | the power set of A | The set of all subsets of $A$. Some books write $2^A$. | $\mathcal{P}(\{1, 2\}) = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |
| $\lvert A \rvert$ | `\lvert A \rvert` | the cardinality of A, the size of A | The number of elements of $A$. Some books write $\#A$ or $n(A)$. | $\lvert \{a, b, c\} \rvert = 3$, $\lvert \emptyset \rvert = 0$ | [Sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md) |

## Logic

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $\neg P$ | `\neg P` | not P | True exactly when $P$ is false. Also written $\sim P$, and `not P` or `!P` in code. | $\neg(2 > 3)$ is true | [Statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md) |
| $P \land Q$ | `P \land Q` or `P \wedge Q` | P and Q | True when both are true | $(2 < 3) \land (3 < 4)$ is true | [Statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md) |
| $P \lor Q$ | `P \lor Q` or `P \vee Q` | P or Q | True when at least one is true. Math's "or" includes the case where both are true. | $(2 > 3) \lor (3 < 4)$ is true | [Statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md) |
| $P \Rightarrow Q$ | `P \Rightarrow Q` or `P \implies Q` | P implies Q; if P, then Q | False only when $P$ is true and $Q$ is false. Logic books often write $P \to Q$. | $x = 2 \Rightarrow x^2 = 4$ | [Conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md) |
| $P \Leftrightarrow Q$ | `P \Leftrightarrow Q` or `P \iff Q` | P if and only if Q | Both $P \Rightarrow Q$ and $Q \Rightarrow P$, so the two are true together or false together. Also written $P \leftrightarrow Q$. | $x^2 = 4 \iff (x = 2 \lor x = -2)$ | [Conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md) |
| $\forall$ | `\forall` | for every, for all | The statement after it holds for each element of the given set | $\forall x \in \mathbb{R},\ x^2 \ge 0$ | [Quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md) |
| $\exists$ | `\exists` | there exists, there is | At least one element of the given set makes the statement true | $\exists x \in \mathbb{R},\ x^2 = 2$ | [Quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md) |
| $\exists!$ | `\exists!` | there exists a unique | Exactly one element makes the statement true | $\exists! x \in \mathbb{R},\ x + 3 = 5$ | [Existence and uniqueness proofs](../04-proofs-and-logic/04-more-proof-methods/02-existence-and-uniqueness-proofs.md) |
| $\therefore$ | `\therefore` | therefore | Marks a conclusion. University writing usually uses the word instead. | $x + 1 = 3$, $\therefore x = 2$ | [Reading math symbols](../04-proofs-and-logic/01-language-and-notation/04-reading-math-symbols.md) |
| $\blacksquare$, $\square$ | `\blacksquare`, `\square` | end of proof, QED | Marks the end of a proof. QED abbreviates the Latin for "which was to be shown". | "... so $n^2$ is odd. $\blacksquare$" | [What is a proof](../04-proofs-and-logic/01-language-and-notation/01-what-is-a-proof.md) |
| $:=$ | `:=` or `\coloneqq` | is defined as | Gives a new name to the right side. It is a definition, not an equation to solve. | $f(x) := x^2 + 1$ | [Definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md) |
| $\equiv$ | `\equiv` | is logically equivalent to | In logic, the two statements have the same truth value in every case. Elsewhere $\equiv$ means "is identically equal to", or congruence (see the CS table). | $\neg(P \land Q) \equiv \neg P \lor \neg Q$ | [Truth tables and logical equivalence](../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md) |

## Functions

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $f \colon A \to B$ | `f \colon A \to B` | f is a function from A to B | Each element of the domain $A$ goes to exactly one element of the codomain $B$ | $f \colon \mathbb{R} \to \mathbb{R}$ | [What is a function](../03-high-school/03-functions/01-what-is-a-function.md) |
| $\mapsto$ | `\mapsto` | maps to | Gives the rule of a function, one element at a time | $x \mapsto x^2$ is the squaring function | [What is a function](../03-high-school/03-functions/01-what-is-a-function.md) |
| $f(x)$ | `f(x)` | f of x | The output of $f$ at the input $x$ | If $f(x) = x^2$, then $f(3) = 9$ | [Introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md) |
| $f^{-1}$ | `f^{-1}` | f inverse | The inverse function: $f^{-1}(y) = x$ exactly when $f(x) = y$. It exists only when $f$ is a bijection, and it is not $\frac{1}{f}$. | If $f(x) = 2x$, then $f^{-1}(x) = \frac{x}{2}$ | [Composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md) |
| $f \circ g$ | `f \circ g` | f composed with g, f circle g | Apply $g$ first, then $f$: $(f \circ g)(x) = f(g(x))$ | With $f(x) = x^2$ and $g(x) = x + 1$, $(f \circ g)(2) = f(3) = 9$ | [Composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md) |
| $f(A)$ | `f(A)` | the image of A under f | For a set $A$ of inputs, the set of outputs $\{f(a) : a \in A\}$ | If $f(x) = x^2$, then $f(\{-1, 1, 2\}) = \{1, 4\}$ | [Functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md) |
| $f^{-1}(B)$ | `f^{-1}(B)` | the preimage of B under f | The set of inputs whose output is in $B$: $\{a : f(a) \in B\}$. Defined for every function, even one with no inverse. | If $f(x) = x^2$, then $f^{-1}(\{4\}) = \{-2, 2\}$ | [Functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md) |

## Sums and products

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $\sum_{i=1}^{n} a_i$ | `\sum_{i=1}^{n} a_i` | the sum of a sub i, for i from 1 to n | Add up $a_1 + a_2 + \dots + a_n$. The letter $i$ is the index, and the numbers below and above are the bounds. | $\sum_{i=1}^{4} i = 1 + 2 + 3 + 4 = 10$ | [Summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md) |
| $\prod_{i=1}^{n} a_i$ | `\prod_{i=1}^{n} a_i` | the product of a sub i, for i from 1 to n | Multiply $a_1 a_2 \cdots a_n$ | $\prod_{i=1}^{4} i = 24 = 4!$ | [Summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md) |

A sum with no terms, such as one whose upper bound is below its lower bound, equals $0$. A product with no terms equals $1$, which is one way to see why $0! = 1$.

## Calculus

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $\lim_{x \to a} f(x)$ | `\lim_{x \to a} f(x)` | the limit of f of x as x approaches a | The value $f(x)$ gets close to as $x$ gets close to $a$, whether or not $f(a)$ exists | $\lim_{x \to 2} (3x + 1) = 7$ | [Limits: intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md) |
| $\to$ | `\to` | approaches, goes to | In a limit, "gets close to"; $x \to 0^+$ means from the right. In $f \colon A \to B$ it points from the domain to the codomain. | $\frac{1}{x} \to 0$ as $x \to \infty$ | [Limits: intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md) |
| $\frac{dy}{dx}$ | `\frac{dy}{dx}` | d y d x, the derivative of y with respect to x | The rate of change of $y$ as $x$ changes, which is the slope of the tangent line | If $y = x^3$, then $\frac{dy}{dx} = 3x^2$ | [The derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md) |
| $f'(x)$ | `f'(x)` | f prime of x | The derivative of $f$ at $x$; $f''(x)$ is the second derivative | If $f(x) = x^3$, then $f'(x) = 3x^2$ | [The derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md) |
| $\frac{\partial f}{\partial x}$ | `\frac{\partial f}{\partial x}` | partial f partial x | The partial derivative: the derivative in $x$ with every other variable held fixed | If $f(x, y) = x^2 y$, then $\frac{\partial f}{\partial x} = 2xy$ | Partial derivatives and the gradient<!-- link: ../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md --> |
| $\int_a^b f(x)\,dx$ | `\int_a^b f(x)\,dx` | the integral from a to b of f of x d x | The signed area between the graph of $f$ and the $x$-axis from $a$ to $b$. Without bounds, $\int f(x)\,dx$ means the antiderivatives of $f$. | $\int_0^1 x^2\,dx = \frac{1}{3}$ | [Riemann sums and the definite integral](../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md) |
| $\infty$ | `\infty` | infinity | Not a real number. Writing $x \to \infty$ means $x$ grows without bound. | $\lim_{x \to \infty} \frac{1}{x} = 0$ | [Limits: intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md) |
| $\ln x$ | `\ln x` | the natural log of x | The logarithm with base $e \approx 2.718$ | $\ln e = 1$, $\ln 1 = 0$ | [Logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md) |

## Linear algebra

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $\mathbf{v}$, $\vec{v}$ | `\mathbf{v}`, `\vec{v}` | vector v | A vector. Print uses bold; handwriting uses an arrow, since bold is hard to write by hand. | $\mathbf{v} = (3, 4)$ | [Vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md) |
| $\lVert \mathbf{v} \rVert$ | `\lVert \mathbf{v} \rVert` | the norm of v, the length of v | The length $\sqrt{v_1^2 + \dots + v_n^2}$ | $\lVert (3, 4) \rVert = 5$ | [Vectors, dot product and span](../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md) |
| $\mathbf{u} \cdot \mathbf{v}$ | `\mathbf{u} \cdot \mathbf{v}` | u dot v | The dot product $u_1 v_1 + \dots + u_n v_n$, which is a number | $(1, 2) \cdot (3, 4) = 11$ | [Vectors, dot product and span](../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md) |
| $I$, $I_n$ | `I`, `I_n` | the identity matrix | The $n \times n$ matrix with ones on the diagonal and zeros elsewhere, so $AI = IA = A$ | $I_2$ has rows $(1, 0)$ and $(0, 1)$ | [Matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md) |
| $A^T$ | `A^T` or `A^{\mathsf{T}}` | A transpose | Rows and columns swapped: entry $(i, j)$ of $A^T$ is entry $(j, i)$ of $A$. Also written $A^{\top}$ or $A'$. | If $A$ is $2 \times 3$, then $A^T$ is $3 \times 2$ | [Matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md) |
| $A^{-1}$ | `A^{-1}` | A inverse | The matrix with $AA^{-1} = A^{-1}A = I$. It exists only for a square matrix with $\det(A) \ne 0$. | $(2I)^{-1} = \frac{1}{2}I$ | [Matrix algebra and inverses](../05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md) |
| $\det(A)$ | `\det(A)` | the determinant of A | A number computed from a square matrix. It is $0$ exactly when $A$ has no inverse. Also written $\lvert A \rvert$. | If $A$ has rows $(a, b)$ and $(c, d)$, then $\det(A) = ad - bc$ | [Determinants](../05-university-core/06-linear-algebra/06-determinants.md) |
| $\operatorname{rank}(A)$ | `\operatorname{rank}(A)` | the rank of A | The number of linearly independent columns, which always equals the number of linearly independent rows | $\operatorname{rank}(I_3) = 3$ | [Linear independence, basis and dimension](../05-university-core/06-linear-algebra/04-linear-independence-basis-and-dimension.md) |

## Probability and statistics

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $P(A)$ | `P(A)` | the probability of A, P of A | A number from $0$ to $1$ that says how likely the event $A$ is. Also written $\Pr(A)$. | For a fair die, $P(\text{even}) = \frac{1}{2}$ | [Basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md) |
| $P(A \mid B)$ | `P(A \mid B)` | the probability of A given B | The probability of $A$ once you know $B$ happened: $\frac{P(A \cap B)}{P(B)}$, for $P(B) > 0$ | For a fair die, $P(6 \mid \text{even}) = \frac{1}{3}$ | [Conditional probability and Bayes' theorem](../05-university-core/07-probability/02-conditional-probability-and-bayes.md) |
| $E[X]$ | `E[X]` or `\mathbb{E}[X]` | the expected value of X, E of X | The long-run average value of the random variable $X$ | For one roll $X$ of a fair die, $E[X] = 3.5$ | [Discrete random variables](../05-university-core/07-probability/03-discrete-random-variables.md) |
| $\operatorname{Var}(X)$ | `\operatorname{Var}(X)` | the variance of X | The expected squared distance from the mean, $E[(X - \mu)^2]$ | For one roll of a fair die, $\operatorname{Var}(X) = \frac{35}{12}$ | [Discrete random variables](../05-university-core/07-probability/03-discrete-random-variables.md) |
| $\sigma$ | `\sigma` | sigma | The standard deviation, $\sqrt{\operatorname{Var}(X)}$, so $\sigma^2$ is the variance | For one roll of a fair die, $\sigma \approx 1.71$ | Descriptive statistics and study design<!-- link: ../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md --> |
| $\mu$ | `\mu` | mu | The mean of a population or of a random variable, so $\mu = E[X]$ | For one roll of a fair die, $\mu = 3.5$ | Descriptive statistics and study design<!-- link: ../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md --> |
| $\bar{x}$ | `\bar{x}` | x bar | The sample mean $\frac{x_1 + \dots + x_n}{n}$ | For the data $2, 4, 9$, the mean is $\bar{x} = 5$ | [Describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md) |
| $\binom{n}{k}$ | `\binom{n}{k}` | n choose k | The number of ways to choose $k$ items from $n$ when order doesn't matter, $\frac{n!}{k!(n-k)!}$. Also written $C(n, k)$ or ${}_nC_k$. | $\binom{5}{2} = 10$ | [Counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md) |

## CS notation

| Symbol | LaTeX | How to say it | Meaning | Example | Taught in |
|---|---|---|---|---|---|
| $O(g(n))$ | `O(g(n))` | big O of g of n | Grows no faster than a constant times $g(n)$, for large $n$ (an upper bound) | $3n^2 + 5n = O(n^2)$ | Asymptotic notation<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md --> |
| $\Omega(g(n))$ | `\Omega(g(n))` | big omega of g of n | Grows at least as fast as a constant times $g(n)$, for large $n$ (a lower bound) | $n^2 = \Omega(n)$ | Asymptotic notation<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md --> |
| $\Theta(g(n))$ | `\Theta(g(n))` | big theta of g of n | Both $O(g(n))$ and $\Omega(g(n))$ (a tight bound) | $3n^2 + 5n = \Theta(n^2)$ | Asymptotic notation<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md --> |
| $\log_2 n$ | `\log_2 n` | log base 2 of n | The power you raise $2$ to in order to get $n$ | $\log_2 1024 = 10$ | [Logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md) |
| $\lg n$ | `\lg n` | lg n, log n | Log base 2 in most CS books (Knuth, CLRS). The ISO standard and some science books use $\lg$ for base 10. A bare $\log$ is base 10 in high school and base $e$ in most pure math; in big O the base doesn't matter, because changing it only multiplies by a constant. | $\lg 8 = 3$ | [Logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md) |
| $a \oplus b$ | `a \oplus b` | a XOR b, exclusive or | True (1) when exactly one of $a$ and $b$ is true (1). On binary numbers it works bit by bit. Python writes `a ^ b`. | $1 \oplus 1 = 0$; $0110 \oplus 0101 = 0011$ | Bitwise operations and masks<!-- link: ../06-cs-math/01-number-representation/05-bitwise-operations-and-masks.md --> |
| $a \equiv b \pmod{n}$ | `a \equiv b \pmod{n}` | a is congruent to b mod n | The modulus $n$ divides $a - b$. In other words, $a$ and $b$ leave the same remainder when divided by $n$. | $17 \equiv 2 \pmod{5}$ | Divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md --> |
| $1011_2$ | `1011_2` | one zero one one, base two | A numeral in base 2; the subscript names the base, written in decimal. Python writes `0b1011` for binary and `0xFF` for hexadecimal. | $1011_2 = 11$, $\mathrm{FF}_{16} = 255$ | [Number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md) |

## Greek alphabet

Thirteen of the capital Greek letters look the same as Latin capitals (A, B, E, Z, H, I, K, M, N, O, P, T and X). LaTeX has no command for those, so you type the Latin letter.

| Lowercase | Uppercase | Name | LaTeX | Common uses |
|---|---|---|---|---|
| $\alpha$ | $\mathrm{A}$ | alpha | `\alpha` | The significance level of a hypothesis test; angles; the learning rate in machine learning |
| $\beta$ | $\mathrm{B}$ | beta | `\beta` | Regression coefficients $\beta_0, \beta_1$; the probability of a Type II error; a stock's beta in finance |
| $\gamma$ | $\Gamma$ | gamma | `\gamma`, `\Gamma` | Angles; the gamma function $\Gamma$, which extends factorials: $\Gamma(n) = (n - 1)!$ for positive integers $n$ |
| $\delta$ | $\Delta$ | delta | `\delta`, `\Delta` | $\delta$ is a small positive number in limit proofs, and the transition function of an automaton; $\Delta$ means "change in", as in $\Delta x$ |
| $\varepsilon$, $\epsilon$ | $\mathrm{E}$ | epsilon | `\varepsilon`, `\epsilon` | A small positive number in limit proofs; the empty string in automata theory; the error term in a regression |
| $\zeta$ | $\mathrm{Z}$ | zeta | `\zeta` | The Riemann zeta function; rare in this book |
| $\eta$ | $\mathrm{H}$ | eta | `\eta` | The learning rate in machine learning; elasticity in some economics books |
| $\theta$ | $\Theta$ | theta | `\theta`, `\Theta` | Angles; an unknown parameter in statistics; $\Theta$ is big theta in algorithm analysis |
| $\iota$ | $\mathrm{I}$ | iota | `\iota` | Rarely used |
| $\kappa$ | $\mathrm{K}$ | kappa | `\kappa` | Curvature; the condition number of a matrix |
| $\lambda$ | $\Lambda$ | lambda | `\lambda`, `\Lambda` | An eigenvalue; a Lagrange multiplier; the rate of a Poisson or exponential distribution; an unnamed function in code (`lambda` in Python) |
| $\mu$ | $\mathrm{M}$ | mu | `\mu` | A mean; the prefix micro, as in $\mu\text{s}$ for a microsecond |
| $\nu$ | $\mathrm{N}$ | nu | `\nu` | Degrees of freedom; frequency. It is easy to misread as $v$. |
| $\xi$ | $\Xi$ | xi | `\xi`, `\Xi` | An unknown point in some theorems, such as the mean value theorem in older books; rare |
| $o$ | $\mathrm{O}$ | omicron | `o` | Not used, since it looks like the Latin o. Big O notation is typeset with the Latin letter O. |
| $\pi$ | $\Pi$ | pi | `\pi`, `\Pi` | The number $\pi \approx 3.14159$; $\Pi$ is a product; in economics $\pi$ often stands for profit or for inflation |
| $\rho$ | $\mathrm{P}$ | rho | `\rho` | The correlation coefficient of a population; density |
| $\sigma$ | $\Sigma$ | sigma | `\sigma`, `\Sigma` | $\sigma$ is a standard deviation; $\Sigma$ is a sum, the alphabet of an automaton, or a covariance matrix |
| $\tau$ | $\mathrm{T}$ | tau | `\tau` | Time; a tax rate in economics models |
| $\upsilon$ | $\Upsilon$ | upsilon | `\upsilon`, `\Upsilon` | Rarely used |
| $\phi$, $\varphi$ | $\Phi$ | phi | `\phi`, `\varphi`, `\Phi` | Euler's totient function $\varphi(n)$; the golden ratio $\varphi \approx 1.618$; angles; $\Phi$ is the cumulative distribution function of the standard normal distribution |
| $\chi$ | $\mathrm{X}$ | chi | `\chi` | The chi-squared distribution $\chi^2$; the chromatic number $\chi(G)$ of a graph |
| $\psi$ | $\Psi$ | psi | `\psi`, `\Psi` | Rarely used in this book |
| $\omega$ | $\Omega$ | omega | `\omega`, `\Omega` | $\omega$ is one outcome of an experiment, or an angular speed; $\Omega$ is the sample space in probability, and big omega in algorithm analysis |

## One letter, one meaning in this book

Each letter below has a default meaning across the book. Some letters also have uses that every textbook shares, such as $b$ in $ax^2 + bx + c$; those are listed in the last column, and a lesson that uses one of them says so when it does. Use the same letters in your own solutions and they will be easier to check against the lessons.

| Letter | Default meaning | Standard other uses |
|---|---|---|
| $n$, $m$ | Natural numbers and counts: how many items, the size of an input | $m$ is the slope in $y = mx + b$ |
| $i$, $j$, $k$ | Integer indices in sums, sequences and loops. The letter $k$ is also the integer in a definition such as "$b = ka$ for some integer $k$". | $i$ is the imaginary unit, $i^2 = -1$, in the complex numbers lessons |
| $q$, $r$ | Quotient and remainder in $n = qd + r$, where $0 \le r < d$ | $r$ is also a radius, the interest rate per period in finance, the common ratio of a geometric series, and the correlation coefficient of a sample |
| $d$ | Divisor | The digits $d_i$ of a numeral in positional notation; a distance; the $d$ in $dx$, which is part of the notation and not a number |
| $b$ | A base: of a number system ($b = 2$ for binary), of a power $b^x$, or of a logarithm $\log_b x$ | One of the fixed numbers $a$, $b$, $c$ below; the $y$-intercept in $y = mx + b$; the base of a triangle in $A = \frac{1}{2}bh$ |
| $a$, $b$, $c$ | Fixed numbers: constants and coefficients, as in $ax^2 + bx + c$, and the integers in $a \mid b$ | |
| $x$, $y$, $z$ | Real variables and unknowns | Data values $x_1, \dots, x_n$ in statistics |
| $t$ | Time | |
| $f$, $g$, $h$ | Functions | $h$ is the small step in $\frac{f(x+h) - f(x)}{h}$, and a height in geometry |
| $A$, $B$, $C$ | Sets, including events in probability (an event is a set of outcomes) | Matrices in linear algebra; an area in geometry |
| $U$ | The universal set | |
| $P$, $Q$, $R$ | Statements, which are true or false, as in $P \Rightarrow Q$; $P(x)$ is a statement about $x$ | $P(A)$ is the probability of the event $A$ |
| $p$ | A prime number | The probability of success in one trial; a $p$-value in statistics |
| $e$ | Euler's number, $e \approx 2.71828$; never a variable | $E$ is an edge set in graphs, and $E[X]$ an expected value |
| $\mathbf{u}$, $\mathbf{v}$, $\mathbf{w}$ | Vectors | |
| $X$, $Y$ | Random variables, with lowercase $x$ and $y$ for the values they take | |
| $\mu$, $\sigma$ | Mean and standard deviation | |
| $\varepsilon$, $\delta$ | Small positive numbers in limit definitions | $\varepsilon$ is the empty string and $\delta$ the transition function in theory of computation |
| $\lambda$ | An eigenvalue | A Lagrange multiplier in optimization |
| $G$ | A graph, with vertex set $V$ and edge set $E$ | |
| $\text{PV}$, $\text{FV}$, $\text{PMT}$ | Present value, future value and payment per period in finance formulas. Each is one name, not a product of letters. | |
