# Glossary

Plain definitions of the terms used across the book, in alphabetical order. Each entry ends with the lesson that teaches the term. Where a term has a formal definition, the entry gives the plain version and the lesson gives the formal one. The glossary grows as new folders are written.

Jump to a letter: [A](#a), [B](#b), [C](#c), [D](#d), [E](#e), [F](#f), [G](#g), [H](#h), [I](#i), [K](#k), [L](#l), [M](#m), [N](#n), [O](#o), [P](#p), [Q](#q), [R](#r), [S](#s), [T](#t), [U](#u), [V](#v), [W](#w), [Z](#z).


## A

An **absolute maximum** of $f$ is a value $f(c)$ that is at least as large as the value at every input in the domain. An absolute minimum is the smallest value. Together they are called extrema. Taught in [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions).

The **absolute value** of a number $x$, written $\lvert x \rvert$, is its distance from 0 on the number line, so it is never negative: $\lvert -6 \rvert = \lvert 6 \rvert = 6$. The distance between two numbers $a$ and $b$ is $\lvert a - b \rvert$. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions) and [absolute value equations and inequalities](../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md#definitions). The two-branch definition ($x$ if $x \ge 0$, $-x$ if $x < 0$) is used to split into cases in [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md#definitions).

An **absolute value inequality** such as $\lvert x - a \rvert < r$ asks for the numbers within distance $r$ of $a$, which means $a - r < x < a + r$. The inequality $\lvert x - a \rvert > r$ asks for the numbers farther away, which means $x < a - r$ or $x > a + r$. Taught in [absolute value equations and inequalities](../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md#definitions).

The **acceleration** of an object moving on a line is the rate of change of its velocity, $a(t) = v'(t) = s''(t)$, the second derivative of the position $s(t)$. Its units are metres per second squared. Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#definitions).

**Active reading** of a proof means reading with pencil and paper and answering questions about the claim, the method, the letters and the reason for each line, so that no line is taken on trust. Taught in [how to read a proof](../04-proofs-and-logic/03-core-proof-methods/02-how-to-read-a-proof.md#definitions).

In $a + b = c$, the numbers $a$ and $b$ are the **addends** and $c$ is their sum. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions).

The **additive inverse** of a number $a$ is its opposite $-a$, the number that adds to $a$ to give 0: $7 + (-7) = 0$. Subtracting a number is the same as adding its additive inverse, $a - b = a + (-b)$. Taught in [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#definitions).

An **algorithm** is a finite list of exact steps that solves a problem and always stops with an answer. Long division is the first algorithm in this book. Taught in [long division](../01-elementary/07-long-division.md) and invariants and algorithm correctness<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->.

**Alternate interior angles** lie between two lines on opposite sides of a transversal. When the lines are parallel, they are equal. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#a-line-crossing-two-lines).

An **altitude** of a triangle is a segment from a vertex perpendicular to the line containing the opposite side. Its length is the height used in the area formula. Taught in [congruence and triangle proofs](../03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md#parts-of-a-triangle-used-in-proofs).

The **AM-GM inequality** for two numbers says that if $a \ge 0$ and $b \ge 0$, then the arithmetic mean is at least the geometric mean, $\frac{a + b}{2} \ge \sqrt{ab}$, with equality exactly when $a = b$. For $a = 4$ and $b = 9$ the two means are $6.5$ and $6$. Taught in [direct proof](../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md#definitions).

The **ambiguous case** of solving a triangle is the case of two sides and an angle not between them (SSA), where the data can fit no triangle, one triangle or two. Test the second angle $180^\circ - B$ as well as $B$. Taught in [law of sines and law of cosines](../03-high-school/09-trigonometry/05-law-of-sines-and-cosines.md#the-ambiguous-case-ssa).

The **amplitude** of a sinusoidal function is half the distance from its highest value to its lowest, $\lvert A \rvert$ in $A\sin(B(x - C)) + D$. Taught in [graphs of trig functions](../03-high-school/09-trigonometry/03-graphs-of-trig-functions.md#definitions).

An **angle** is a pair of rays with a shared endpoint, called the vertex. Its size is measured in degrees, and a full turn is $360^\circ$. An angle is acute if it is less than $90^\circ$, right if it is exactly $90^\circ$, obtuse if it is between $90^\circ$ and $180^\circ$, and straight if it is exactly $180^\circ$. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#points-lines-and-angles) and [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md).

An **antichain** in a partially ordered set is a subset in which no two different elements are comparable. Among the divisors of 12 under divisibility, $\{4, 6\}$ is an antichain. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#minimal-maximal-least-and-greatest).

A relation is **antisymmetric** when the only way for both $a \mathrel{R} b$ and $b \mathrel{R} a$ to hold is $a = b$, so two different elements are never related in both directions. It does not mean "not symmetric": equality is both symmetric and antisymmetric. Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#the-four-properties).

In a proof, an **arbitrary** element is one you pick with no assumptions beyond the stated ones, so whatever you prove about it holds for every element. "Let $n$ be an arbitrary integer" starts most proofs of statements about every integer. Taught in [proof language: let, suppose, WLOG](../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md).

An **arc** is the part of a circle between two points on it. For a central angle $\theta$ in degrees, the arc length is $\frac{\theta}{360} \cdot 2\pi r$. Taught in [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md#arcs-and-sectors).

The **area** of a flat shape is the number of unit squares that cover it with no gaps and no overlaps, measured in square units such as $\text{cm}^2$. A rectangle has area length times width, a parallelogram base times height, and a triangle half of base times height. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#perimeter-area-and-volume) and [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md).

The **arithmetic mean** of two numbers $a$ and $b$ is $\frac{a + b}{2}$, the usual average. For non-negative numbers it is compared with the geometric mean $\sqrt{ab}$. Taught in [direct proof](../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md#definitions).

An **arithmetic sequence** adds the same number, the common difference $d$, at every step, so $a_n = a_0 + nd$ when the first term has index 0. Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#definitions).

An **arithmetic series** is the sum of the terms of an arithmetic sequence. It equals the number of terms times the average of the first and last terms. Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#definitions).

Two variables have an **association** when knowing one tells you something about the other. It is positive when both tend to rise together and negative when one rises as the other falls. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

The **associative property** says that the grouping of a repeated operation doesn't matter: $(a + b) + c = a + (b + c)$ and $(a \times b) \times c = a \times (b \times c)$ for all numbers $a$, $b$ and $c$. Subtraction and division are not associative, since $(10 - 5) - 2 = 3$ but $10 - (5 - 2) = 7$. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#associative-properties).

A statement is **atomic** when it has no smaller statement inside it. "7 is prime" is atomic, and "7 is prime and 8 is even" is built from two atomic statements. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#statements).

The **audience** of a proof is the reader it is written for. The best target is a classmate who knows the definitions and earlier results but has not seen your argument. Taught in [what is a proof](../04-proofs-and-logic/01-language-and-notation/01-what-is-a-proof.md#definitions).

The **augmented matrix** of a system is its coefficient matrix with one more column for the constants. Taught in [systems of linear equations](../03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md#definitions).

The **average rate of change** of $f$ from $a$ to $b$ is $\frac{f(b) - f(a)}{b - a}$, the slope of the secant line. It is 0 over an interval where the function ends where it started, even if it moved in between. Taught in [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions).

The **axes** of the coordinate plane are the two number lines that cross at right angles: the horizontal $x$-axis, positive to the right, and the vertical $y$-axis, positive upward. Taught in [the coordinate plane](../02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md#definitions).

An **axiom** is a statement accepted without proof as a starting point for a theory. In a university course, rules of arithmetic such as $a + b = b + a$ are axioms for the real numbers. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#the-field-axioms), [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#postulates-and-theorems) and [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md).

The **axis of symmetry** of a parabola is the vertical line through its vertex, $x = h$. The two halves of the parabola are mirror images across it. Taught in [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#definitions).

## B

The **base** has three meanings. In a power $b^n$, the base is the number being multiplied, $b$; a logarithm $\log_b x$ has a base in the same sense. In a number system, the base is the number of digits and the factor between neighbouring places: base 10 for decimal, base 2 for binary. In a triangle or a parallelogram, the base is the side you choose to measure the height from, usually the one drawn at the bottom. Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#definitions), [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md), [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md) and [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#base-and-height).

The **base case** of an induction proof is the check that the statement is true for the first value, usually $n = 0$ or $n = 1$. It is the push that starts the chain, and a correct inductive step proves nothing without it. Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#definitions).

A **basis** of a vector space is a set of vectors that are linearly independent and span the space, so every vector in the space is a linear combination of them in exactly one way. The vectors $(1, 0)$ and $(0, 1)$ form a basis of $\mathbb{R}^2$. The formal definition is in linear independence, basis and dimension<!-- link: ../05-university-core/06-linear-algebra/04-linear-independence-basis-and-dimension.md -->. In a recursive definition of a set, the basis is the list of elements named outright, such as $0$ in "$0 \in E$, and if $x \in E$ then $x + 2 \in E$". Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#definitions).

A **biconditional** is the statement "$P$ if and only if $Q$", which says that "if $P$, then $Q$" and its converse are both true. A definition is a biconditional. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements), [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md#the-biconditional) and [if and only if proofs](../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md#definitions).

A function is **bijective**, or a bijection, when it is both injective and surjective: every element of the codomain is the output of exactly one input. A bijection pairs up the domain and the codomain one to one, so it has an inverse. Taught in [injective, surjective and bijective](../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md).

**Binary** is base 2: numbers written with only the digits 0 and 1, where the places are worth $1, 2, 4, 8, \dots$ from the right. Computers store all data in binary. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

The **binary logarithm** is the logarithm in base 2, written $\log_2 x$. It counts how many times $x$ can be halved, which is why it appears in the running times of binary search and other halving algorithms. Taught in [logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md#definitions).

A **binary prefix** is a prefix for a power of 2 rather than a power of 10: KiB, MiB, GiB and TiB stand for $2^{10}$, $2^{20}$, $2^{30}$ and $2^{40}$ bytes. The decimal prefixes kB, MB and GB stand for $10^3$, $10^6$ and $10^9$ bytes, so a GiB is about 7% bigger than a GB. Taught in [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md#kb-or-kib).

A **binomial coefficient** $\binom{n}{k}$, read "$n$ choose $k$", is the number of $k$-element subsets of an $n$-element set, $\frac{n!}{k!\,(n-k)!}$. It is also the entry in position $k$ of row $n$ of Pascal's triangle. Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md#definitions).

The **binomial theorem** says that $(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$ for a whole number $n$. The expansion has $n + 1$ terms, and $(a + b)^n$ is not $a^n + b^n$. Taught in [the binomial theorem](../03-high-school/11-sequences-series-and-counting/04-binomial-theorem.md#definitions).

The **bisection method** finds a zero of a continuous function by halving an interval whose ends give opposite signs and keeping the half that still has a sign change. After $k$ steps the interval has width $\frac{b - a}{2^k}$. Taught in [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#finding-the-root-by-bisection) and, for polynomials, [polynomial functions and graphs](../03-high-school/04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#finding-a-zero-by-bisection).

A **bit** is a binary digit, 0 or 1. It is the smallest unit of information, the answer to one yes-or-no question. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md) and bits and information<!-- link: ../06-cs-math/01-number-representation/02-bits-and-information.md -->.

A **block** of a partition is one of the non-empty subsets that the set is cut into, so that every element lies in exactly one block. The blocks of the integers under "same remainder mod 3" are the three remainder classes. Taught in [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#partitions).

A **bound variable** is a letter that exists only inside the expression that introduces it, such as $i$ in $\sum_{i=1}^{n} i$ or $x$ in "for every $x$". A variable that no quantifier or operator governs is free, and its meaning comes from outside. Renaming a bound variable changes nothing. Taught in [reading math symbols](../04-proofs-and-logic/01-language-and-notation/04-reading-math-symbols.md#definitions) and [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#the-two-quantifiers).

A **box plot** draws a box from $Q_1$ to $Q_3$ with a line at the median, and whiskers out to the most extreme values that are not outliers. Each quarter of the data lies in one of the four sections. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

A **budget line** is the equation $p_x x + p_y y = I$ of the goods bundles that use up an income $I$ at prices $p_x$ and $p_y$. Its slope $-\frac{p_x}{p_y}$ is the opportunity cost of $x$. Taught in [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#a-budget-constraint).

A **byte** is 8 bits, enough for $2^8 = 256$ different values, from 0 to 255. Taught in bits and information<!-- link: ../06-cs-math/01-number-representation/02-bits-and-information.md -->.

## C

**Cantor's theorem** says that for every set $A$, no function from $A$ to its power set $\mathcal{P}(A)$ is surjective, so $\lvert A \rvert < \lvert \mathcal{P}(A) \rvert$. The proof builds the set of elements that are not in their own image. Taught in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#uncountable-sets).

The **cardinality** of a set is the number of elements in it, written $\lvert A \rvert$, as counted in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#three-sets-and-counting). For infinite sets it is defined by comparing sets with bijections; the formal version is in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md).

The **Cartesian product** $A \times B$ of two sets is the set of all ordered pairs $(a, b)$ with $a$ in $A$ and $b$ in $B$. A function from $A$ to $B$ is a subset of $A \times B$ in which each $a$ appears exactly once. Taught in [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#definitions) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#ordered-pairs-and-cartesian-products).

**Casting out nines** checks a multiplication with remainders on division by 9. Reduce each factor to one digit by taking digit sums again and again, multiply those two digits and reduce the result, and compare it with your answer reduced the same way. Different digits mean the answer is wrong, but matching digits don't prove it right, since a mistake that changes the answer by a multiple of 9 passes. Taught in [multi-digit multiplication](../01-elementary/05-multi-digit-multiplication.md#casting-out-nines).

A **categorical variable** sorts individuals into groups, such as an operating system or a province. Averaging its values makes no sense. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

**Cavalieri's principle** says that two solids with the same height and equal cross-section areas at every level have equal volumes. It explains why a slanted prism has the same volume as a straight one. Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#why-prisms-and-cylinders-are-base-times-height).

The **ceiling** of a number $x$, written $\lceil x \rceil$, is the least integer greater than or equal to $x$. So $\lceil 3.2 \rceil = 4$, and an integer is its own ceiling. Taught in [piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md#definitions).

A **chain** in a partially ordered set is a subset in which every two elements are comparable, like a path going up a Hasse diagram. Among the divisors of 12 under divisibility, $\{1, 2, 4, 12\}$ is a chain. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#minimal-maximal-least-and-greatest).

The **chain rule** says that if $g$ is differentiable at $x$ and $f$ is differentiable at $g(x)$, then $(f \circ g)'(x) = f'(g(x))\,g'(x)$: the derivative of the outer function at the inner value, times the derivative of the inner function. So $\frac{d}{dx}\sin(3x) = 3\cos(3x)$. Taught in [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md#definitions).

The **change of base** formula is $\log_b x = \frac{\log_c x}{\log_c b}$ for any valid base $c$. It lets a calculator that only has $\ln$ compute a logarithm in any base. Taught in [logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md#change-of-base).

A **circle** is the set of all points in a plane at a fixed distance, the radius, from a point called the centre. A segment through the centre with both ends on the circle is a diameter, twice the radius in length. The area of a circle is $\pi r^2$. Taught in [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md#circles).

**Circular reasoning** is an argument that uses the claim itself, or something equivalent to it, as one of its reasons. "The sum of two rationals is rational because rationals are closed under addition" is circular, since "closed under addition" is the claim. Taught in [how to write a proof](../04-proofs-and-logic/03-core-proof-methods/07-how-to-write-a-proof.md#definitions).

The **circumference** of a circle is the distance once around it, $C = 2\pi r = \pi d$. Taught in [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md#circles).

**Clearing fractions** means multiplying both sides of an equation by a common denominator of all its fractions, usually the least common denominator, so that no fractions remain. Every term gets multiplied, including the ones with no fraction. Taught in [multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#definitions).

The **closure clause** of a recursive definition says that nothing else is in the set: its elements are exactly those obtained from the basis by finitely many uses of the recursive clauses. Without it, "$0 \in E$, and if $x \in E$ then $x + 2 \in E$" would not rule out odd numbers in $E$. Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#definitions).

**Co-interior angles** lie between two lines on the same side of a transversal. When the lines are parallel, they add to $180^\circ$, and they are not equal. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#a-line-crossing-two-lines).

The **codomain** of a function $f \colon A \to B$ is the set $B$ that its outputs are allowed to land in. It can be bigger than the range, which is the set of outputs that actually occur. Two functions are equal only when their domains and codomains match as well as their outputs. Taught in [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#definitions) and [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#functions-as-sets-of-pairs).

A **coefficient** is a number that multiplies a variable in a term. In $3x^2 - 5x$, the coefficients are $3$ and $-5$. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md) and [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md#definitions).

A **combination** of $k$ items chosen from $n$ different items is a selection in which order is ignored, such as a committee. The number of them is $\binom{n}{k}$, which is $P(n, k)$ divided by $k!$. Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md#definitions).

A **common denominator** of two or more fractions is a common multiple of their denominators. The least common denominator (LCD) is their least common multiple: for $\frac{3}{4}$ and $\frac{5}{6}$ it is 12. Taught in [adding and subtracting fractions](../01-elementary/10-adding-and-subtracting-fractions.md#definitions). The version for polynomials is in [rational expressions](../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md#definitions).

The **commutative property** says that order doesn't matter in a sum or a product: $a + b = b + a$ and $a \times b = b \times a$ for all numbers $a$ and $b$. Subtraction and division are not commutative, since $10 - 3 = 7$ but $3 - 10 = -7$. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#commutative-properties).

Two elements $a$ and $b$ of a partially ordered set are **comparable** when $a \preceq b$ or $b \preceq a$, and incomparable otherwise. Under divisibility, 2 and 6 are comparable, and 2 and 3 are incomparable. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#partial-orders).

The **complement** of an event $A$ is the event "not $A$", written $A^c$, and $P(A^c) = 1 - P(A)$. It is the quick route to "at least one" problems. For sets, the complement $A^c$ is the set of elements of the universe that are not in $A$, so it has no meaning until the universe is stated; see [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#the-four-operations). Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#definitions).

Two angles are **complementary** when their measures add to $90^\circ$. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#pairs-of-angles).

**Completing the square** rewrites $ax^2 + bx + c$ in vertex form by adding and subtracting the square needed to make a perfect-square trinomial. When $a \ne 1$, whatever you subtract inside the bracket is multiplied by $a$ outside. Taught in [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#definitions).

A **complex number** is a number $a + bi$ with $a$ and $b$ real, where $a$ is the real part and $b$ is the imaginary part (itself a real number). The numbers $\mathbb{C}$ contain the real numbers, as the case $b = 0$. Every polynomial equation has a solution in $\mathbb{C}$, which is the fundamental theorem of algebra. Taught in [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#definitions).

The **complex plane** is the plane in which $a + bi$ is drawn as the point $(a, b)$, with the real axis horizontal and the imaginary axis vertical. Multiplying by $i$ turns a point a quarter turn counterclockwise about the origin. Taught in [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#definitions).

A **composite** number is an integer greater than 1 that is not prime, so it has a factor other than 1 and itself. The number 12 is composite, since $12 = 3 \times 4$, and the number 1 is neither prime nor composite. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md).

The **composition** of two functions is $(f \circ g)(x) = f(g(x))$: apply $g$ first, then $f$. Order matters, since $f \circ g$ and $g \circ f$ are usually different. Taught in [composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md#definitions) and [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#identity-and-composition).

A **compound inequality** is two inequalities joined by "and" or "or". The statement $-2 < x \le 5$ means "$-2 < x$ and $x \le 5$", the numbers between $-2$ and 5 with 5 included. Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#compound-inequalities-a-preview) and [compound inequalities and interval notation](../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md).

**Compound interest** is interest that is added to the balance and then earns interest itself. After $n$ periods at rate $r$ per period, the future value is $\text{FV} = \text{PV}(1 + r)^n$. Taught in [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#compound-interest-as-a-preview) and compound interest<!-- link: ../08-financial-math/02-interest-and-growth/02-compound-interest.md -->.

A **compound statement** is built from atomic statements with connectives, such as $(P \vee Q) \wedge \neg R$. Its truth table has $2^n$ rows when it involves $n$ atomic statements. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#compound-statements-and-precedence).

The **conclusion** of "if P, then Q" is Q, the part that is claimed to follow, also called the consequent. In a theorem, the conclusion is what the proof has to reach. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements) and [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md).

A **conditional statement** is a statement of the form "if $P$, then $Q$". The part after "if" is the hypothesis and the part after "then" is the conclusion. It is false only when the hypothesis is true and the conclusion is false, so it is true whenever the hypothesis is false. In symbols it is written $P \Rightarrow Q$. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements) and [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md#the-conditional).

A **cone** is like a pyramid with a circle for its base. Its volume is $\frac{1}{3}\pi r^2 h$. Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#definitions).

A **confounding variable** is a third variable that influences both of the two variables being studied, so it can create an association that isn't causal. Towns with more libraries also have more car accidents, because both grow with population. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

Two figures are **congruent** when one can be carried onto the other by rigid motions, so they have the same shape and size. For triangles, all three pairs of corresponding sides and angles are equal. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#congruence-and-similarity) and [congruence and triangle proofs](../03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md#definitions).

A **conic section** is a curve obtained by cutting a double cone with a plane: a circle, an ellipse, a parabola or a hyperbola. Taught in [conic sections](../03-high-school/08-geometry-and-proof/05-conic-sections.md#definitions).

A **conjecture** is a statement that people believe is true but that nobody has proved yet. Goldbach's conjecture, that every even integer greater than 2 is the sum of two primes, is a famous one that is still open. Taught in [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md).

The **conjugate** of a binomial is the same two terms with the sign between them flipped. The conjugate of $2 + \sqrt{3}$ is $2 - \sqrt{3}$, and the conjugate of the complex number $a + bi$ is $a - bi$. A number times its conjugate is free of the radical or of $i$, as in $(2 + \sqrt{3})(2 - \sqrt{3}) = 1$. Taught in [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md#definitions) and [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#definitions).

The **conjunction** $P \wedge Q$ ("$P$ and $Q$") is true exactly when both $P$ and $Q$ are true. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#the-connectives).

A **connective** builds a new statement from one or two old ones, and the truth value of the new statement depends only on the truth values of the old ones. The first four are not, and, or and exclusive or; the conditional and biconditional follow. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#the-connectives).

A system is **consistent** when it has at least one solution, and inconsistent when it has none, as with two parallel lines. Taught in [systems of linear equations](../02-middle-school/05-linear-relationships-and-functions/04-systems-of-linear-equations.md#definitions).

When $y = kx$, the number $k$ is the **constant of proportionality**. It is the unit rate $\frac{y}{x}$: gas at \$1.50 per litre costs $y = 1.5x$ dollars for $x$ litres. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#definitions).

A **constant term** is a term with no variable, such as the 7 in $4x^2 - x + 7$. Its value stays the same whatever the variable is. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#definitions).

A **constructive proof** of an existence claim names an object, called a witness, and checks that it has the required property. A non-constructive proof shows that an object must exist without saying which one. Both are valid proofs of "there exists". Taught in [existence and uniqueness proofs](../04-proofs-and-logic/04-more-proof-methods/02-existence-and-uniqueness-proofs.md#definitions).

A function $f$ is **continuous at** a number $a$ when $f(a)$ is defined, $\lim_{x \to a} f(x)$ exists, and the limit equals $f(a)$. In plain words, there is no hole, jump or blow-up at $a$. It is right-continuous at $a$ if only $\lim_{x \to a^+} f(x) = f(a)$ holds, and left-continuous for the left side; an endpoint of a closed interval is tested from the one side that exists. Taught in [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#definitions).

A **contradiction** is a statement that cannot be true: either one of the form "$R$ and not $R$", or one that clashes with a hypothesis, a definition or a proved result. In a truth table it is a compound statement that is false in every row. Deriving one from an assumption shows that the assumption is false. Taught in [proof by contradiction](../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md#definitions) and [truth tables and logical equivalence](../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md#tautologies-and-contradictions).

The **contrapositive** of "if P, then Q" is "if not Q, then not P". It is logically equivalent to the original, so proving one proves the other. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements) and [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md) and [contrapositive proof](../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md).

A series **converges** when its partial sums approach a limit, and it diverges otherwise. An infinite geometric series converges to $\frac{a}{1 - r}$ exactly when $\lvert r \rvert < 1$, which is why $0.999\ldots = 1$. A sequence converges to $L$ when its terms eventually stay as close to $L$ as you like, and the exact version is previewed in [the epsilon-delta definition](../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md#the-sequence-version-as-a-preview). Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#the-infinite-geometric-series) and [infinite series basics](../05-university-core/05-sequences-and-series/02-infinite-series-basics.md).

The **converse** of "if P, then Q" is "if Q, then P". It is a different statement: "if a number is divisible by 4, then it is even" is true, but its converse is false. (The converse of a relation $R$ is a different thing: the relation $R^{-1}$ that reverses every pair, taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#relations).) Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements) and [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md).

A **conversion factor** is a fraction whose numerator and denominator are the same amount written in two units, such as $\frac{1000\ \text{m}}{1\ \text{km}}$, so the fraction equals 1. Multiplying by it changes the units without changing the amount. Taught in [measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#definitions).

The **coordinate plane** is a flat grid made by two number lines, the horizontal $x$-axis and the vertical $y$-axis, which cross at their zeros, a point called the origin. Each point has coordinates $(x, y)$, written in that order: the point $(3, 2)$ is 3 units right of the origin and 2 units up. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#shapes-on-a-grid) and [the coordinate plane](../02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md).

A **coordinate proof** proves a geometric statement by placing the figure on the coordinate plane, usually with a vertex at the origin and a side on an axis, and calculating with distances, slopes and midpoints. Taught in [coordinate geometry and circles](../03-high-school/08-geometry-and-proof/04-coordinate-geometry-and-circles.md#coordinate-proofs).

A **corner** of a graph is a point where the two one-sided slopes are different finite numbers, as for $\lvert x \rvert$ at 0. The derivative does not exist there. Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#where-a-derivative-does-not-exist).

A **corner point** of a feasible region is a crossing of two boundary lines that satisfies every other constraint too. Not every crossing of two boundary lines is a corner. Taught in [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#definitions).

A **corollary** is a result that follows quickly from a theorem that was just proved. Taught in [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md).

**Correlation** measures how strong a linear association is. University statistics gives it as a number $r$ from $-1$ to 1. Correlation is not causation. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

The **cosine** of an acute angle in a right triangle is the adjacent side divided by the hypotenuse. For any angle $\theta$, it is the $x$-coordinate of the point at angle $\theta$ on the unit circle. Taught in [right triangle trigonometry](../03-high-school/09-trigonometry/01-right-triangle-trigonometry.md#definitions) and [radians and the unit circle](../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md#definitions).

A set is **countable** when its elements can be listed in a sequence $a_0, a_1, a_2, \dots$, which may be finite. The integers and the rational numbers are countable, and the real numbers are not. Some books use "countable" only for infinite sets; the formal definition is in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md).

A set is **countably infinite** when it can be paired off with $\mathbb{N}$ by a bijection. A set that is finite or countably infinite is countable. Taught in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#finite-infinite-countable).

A **counterexample** is one case that makes a statement about every case false. The number 2 is a counterexample to "every prime is odd", and $3 - 10 \ne 10 - 3$ is a counterexample to "subtraction is commutative". For a claim with a hypothesis, a counterexample must satisfy the hypothesis and fail the conclusion. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements), [properties of operations](../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division) and [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md).

**CPCTC** stands for "corresponding parts of congruent triangles are congruent". It is the definition of congruent triangles read in the other direction, and it can be cited only after the triangles are proved congruent. Taught in [congruence and triangle proofs](../03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md#definitions).

A **critical number** of a polynomial or rational inequality is a zero of the numerator or of the denominator after everything is combined into one factored fraction. The critical numbers cut the number line into the intervals on which the sign is constant. Taught in [polynomial and rational inequalities](../03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md#definitions).

The **cube** of a number $b$ is $b^3 = b \times b \times b$, read "$b$ cubed", after the volume of a cube. A perfect cube is the cube of an integer, and unlike a perfect square it can be negative: $(-2)^3 = -8$. Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#definitions).

A **cube root** of $a$ is the number whose cube is $a$, written $\sqrt[3]{a}$. Unlike a square root, it exists for every real number, and there is only one: $\sqrt[3]{-8} = -2$. Taught in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#square-roots-and-cube-roots).

A **cusp** is a sharp point of a graph where the one-sided slopes go off to infinity with opposite signs, as for $x^{2/3}$ at 0. The derivative does not exist there. Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#where-a-derivative-does-not-exist).

A **cylinder** is like a prism with circles for bases. Its volume is $\pi r^2 h$ and its surface area is $2\pi r^2 + 2\pi r h$. Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#definitions).

## D

A **decibel** is a logarithmic unit for the ratio of two intensities: $L = 10\log_{10}\frac{I}{I_0}$. Adding 10 decibels multiplies the intensity by 10. Taught in [logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md#log-scales).

A **decimal** is a number written in base 10 with a decimal point, where the digits after the point stand for tenths, hundredths, thousandths and so on. Those digits are its decimal places, so 24.375 has three decimal places and stands for $24 + \frac{3}{10} + \frac{7}{100} + \frac{5}{1000}$. Taught in [decimals: place value, adding and subtracting](../01-elementary/12-decimals-place-value-and-adding.md#definitions).

A **decision problem** asks a yes-or-no question about each input string, such as "is this number prime". It is determined by the set of strings whose answer is yes, so the set of all decision problems is the power set of the set of all strings. Taught in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#why-some-problems-have-no-program).

A **definition** gives the exact meaning of a term. A definition worded with "if" is read as "if and only if": "an integer $n$ is even if $n = 2k$ for some integer $k$" also tells you that every even integer has that form. Taught in [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md).

The **degree** of a nonzero polynomial is the largest exponent that has a nonzero coefficient. The zero polynomial has no degree. The **leading coefficient** is the coefficient of the term of that degree. Taught in [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md#definitions).

**De Morgan's laws** say that a negation passes through "and" and "or" by swapping them and negating each part: $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$ and $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$. For sets, $(A \cap B)^c = A^c \cup B^c$ and $(A \cup B)^c = A^c \cap B^c$. Taught in [truth tables and logical equivalence](../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md#three-theorems-with-proofs) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#set-identities).

The **denominator** of a fraction $\frac{a}{b}$ is the number on the bottom, $b$, which says how many equal parts the whole is cut into. It can't be 0. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md).

The **derivative** of a function at a point is its instantaneous rate of change there, which is the slope of the tangent line. It is defined as the limit $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$; the formal treatment is in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#definitions), which also shows that a differentiable function is continuous.

The **determinant** of a $2 \times 2$ matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is $ad - bc$. The matrix has an inverse exactly when its determinant is not 0. Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#definitions).

The **diagonal argument** shows that a set cannot be listed. Assume a list of all its elements, then build a new element that differs from the $n$-th listed element at place $n$, so it is on no row of the list. It proves that the set of infinite sequences of 0s and 1s is uncountable, and so is $\mathbb{R}$. Taught in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#uncountable-sets).

The **difference** $a - b$ is the number you add to $b$ to get $a$, so $52 - 18 = 34$ because $18 + 34 = 52$. For integers it is the same as adding the opposite: $3 - 7 = 3 + (-7) = -4$. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions) and [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#definitions).

A **difference of squares** $a^2 - b^2$ factors as $(a + b)(a - b)$. A sum of squares such as $x^2 + 9$ is prime over the real numbers. Taught in [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#the-factoring-identities).

The **difference quotient** of $f$ at $a$ is $\frac{f(a + h) - f(a)}{h}$ for $h \ne 0$, the slope of the secant line through $(a, f(a))$ and $(a + h, f(a + h))$. Its limit as $h \to 0$ is the derivative. Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#definitions).

A function is **differentiable** at $a$ when the limit of the difference quotient as $h \to 0$ exists as a real number. Differentiable implies continuous, and the converse is false: $\lvert x \rvert$ is continuous at 0 and not differentiable there. Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#differentiable-implies-continuous).

A **digit** is one of the ten symbols 0 to 9 that write numbers in base 10. Other bases use other digits: binary uses only 0 and 1. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

A **digraph**, or directed graph, draws a relation with one vertex for each element and an arrow from $a$ to $b$ whenever $a$ is related to $b$. A pair $(a, a)$ is an arrow from a vertex to itself, called a loop. Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#ways-to-show-a-relation).

A **dilation** stretches or shrinks a figure from a centre by a scale factor $k$, so with the origin as the centre $(x, y)$ goes to $(kx, ky)$. Distances change by the factor $k$ and angles don't change. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#the-four-transformations).

**Dimensional analysis** converts units by multiplying by conversion factors and cancelling each unit that appears in both a numerator and a denominator. For example, $90\ \frac{\text{km}}{\text{h}} \times \frac{1000\ \text{m}}{1\ \text{km}} \times \frac{1\ \text{h}}{3600\ \text{s}} = 25\ \frac{\text{m}}{\text{s}}$. Taught in [measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#definitions).

A **direct proof** of "if $P$, then $Q$" assumes $P$ and derives $Q$ through a chain of statements, each of which is a hypothesis, a definition, a result already proved, or a consequence of earlier lines. Taught in [direct proof](../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md#definitions).

**Direct substitution** finds a limit by putting $x = a$ into the formula. It works for a polynomial, and for a rational function whose denominator is not 0 at $a$. Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#definitions).

A **discontinuity** of a function is a point where it is not continuous. It is removable if the limit exists but the value is missing or different, a jump if the one-sided limits exist and differ, and infinite if a one-sided limit is $\infty$ or $-\infty$. Taught in [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#definitions).

The **discriminant** of $ax^2 + bx + c$ is $D = b^2 - 4ac$, the number under the root in the quadratic formula. If $D > 0$ there are two real solutions, if $D = 0$ there is one, and if $D < 0$ there are none. The single solution when $D = 0$ is a repeated root: the graph touches the $x$-axis there and turns back. Taught in [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md#definitions).

Two sets are **disjoint** when they have no element in common, $A \cap B = \emptyset$. Taught in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#sets-equality-and-subsets).

The **disjunction** $P \vee Q$ ("$P$ or $Q$") is true exactly when at least one of $P$ and $Q$ is true, so it is true when both are. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#the-connectives).

To **disprove** a statement is to prove that it is false, which is the same as proving its negation. A counterexample is the disproof that suits a "for every" claim. Taught in [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md#definitions).

The **distance formula** gives the distance between $(x_1, y_1)$ and $(x_2, y_2)$ as $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$. It is the Pythagorean theorem applied to the horizontal and vertical differences. Taught in [coordinate geometry and circles](../03-high-school/08-geometry-and-proof/04-coordinate-geometry-and-circles.md#definitions) and [the Pythagorean theorem](../02-middle-school/06-geometry/04-pythagorean-theorem.md#definitions).

The **distributive property** says that $a \times (b + c) = a \times b + a \times c$ for all numbers $a$, $b$ and $c$: to multiply a sum, multiply each term and add the results. It holds over subtraction too, and read from right to left it pulls out a common factor. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#distributive-property) and [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#the-properties-behind-each-step).

The **dividend** is the number being divided: in $n \div d$, it is $n$. Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and [long division](../01-elementary/07-long-division.md).

A whole number $n$ is **divisible** by a nonzero whole number $d$ when $n \div d$ leaves remainder 0, that is, when $n = kd$ for some whole number $k$. So 24 is divisible by 4, and 26 is not. The same fact is written $d \mid n$ and read "$d$ divides $n$". Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->. In proofs, "$d$ divides $n$" is defined by $n = dk$ for some integer $k$, so every integer divides 0 and 0 divides only 0; see [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#five-working-definitions).

The **division algorithm** is the theorem that for integers $n$ and $d$ with $d > 0$, there are unique integers $q$ and $r$ with $n = qd + r$ and $0 \le r < d$. Despite its name it is a theorem, not a method; long division is one method for finding $q$ and $r$. Taught in [long division](../01-elementary/07-long-division.md#definitions) and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->. The version for polynomials is in [polynomial division and the remainder theorem](../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md#definitions). The proof for every integer $n$, with existence and uniqueness shown separately, is in [existence and uniqueness proofs](../04-proofs-and-logic/04-more-proof-methods/02-existence-and-uniqueness-proofs.md#the-division-algorithm).

The **divisor** in $n \div d$ is $d$, the number you divide by. In number theory, a divisor of $n$ is an integer $d$ with $d \mid n$, so there the word means the same as "factor". Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions), [long division](../01-elementary/07-long-division.md) and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

The **domain** of a function is its set of allowed inputs, the set $A$ in $f \colon A \to B$. When a formula such as $\frac{1}{x}$ comes with no stated domain, the domain is taken to be every real number the formula works for, here every $x \ne 0$. In logic, the domain of a quantifier is the set of values its variable may take. Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#definitions), [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#definitions), [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#functions-as-sets-of-pairs) and [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#open-sentences-and-domains).

The **dot product** of $\mathbf{u} = (u_1, u_2)$ and $\mathbf{v} = (v_1, v_2)$ is the number $u_1 v_1 + u_2 v_2$. It also equals $\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos\theta$, where $\theta$ is the angle between them, so for nonzero vectors a dot product of 0 means they are perpendicular. Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md#definitions) and vectors, dot product and span<!-- link: ../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md -->.

The **doubling time** of a growing quantity is the time it takes to double, so the quantity is $A_0 \cdot 2^{t/T}$ for a doubling time $T$. Taught in [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#doubling-time-and-half-life) and [exponential and logarithmic equations](../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md#the-rule-of-72).

## E

An **edge case** is a value at the boundary of what a claim allows, or one that behaves differently from its neighbours: 0, 1, negative numbers, equal values, the empty set. Claims proved or guessed from typical cases tend to fail there first. Taught in [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md#definitions).

A number $\lambda$ is an **eigenvalue** of a square matrix $A$ when $A\mathbf{v} = \lambda\mathbf{v}$ for some nonzero vector $\mathbf{v}$, which is called an eigenvector. In plain words, $A$ only stretches that vector, by the factor $\lambda$. Taught in eigenvalues and eigenvectors<!-- link: ../05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md -->.

An **element** of a set is one of the objects in it. Writing $x \in A$ says that $x$ is an element of $A$. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#sets-and-set-notation) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md).

**Elimination** solves a system by adding multiples of the equations to cancel one unknown. Each step keeps the solutions, so the answer to the last equation is the answer to the original system. Taught in [systems of linear equations](../02-middle-school/05-linear-relationships-and-functions/04-systems-of-linear-equations.md#solving-by-elimination).

An **ellipse** is the set of points for which the distances to two fixed points, the foci, add to a constant. A circle is the case where the two foci coincide. Taught in [conic sections](../03-high-school/08-geometry-and-proof/05-conic-sections.md#definitions).

The **empty set**, written $\emptyset$, is the set with no elements. It is a subset of every set, and its cardinality is 0. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#sets-and-set-notation) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md).

The **empty sum** is a sum with no terms, and it is defined to be 0, as the total of a loop that runs zero times. The empty product is 1. Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#definitions).

The **end behaviour** of a polynomial function describes what $f(x)$ does as $x$ grows large in either direction. It is decided by the leading term. Taught in [polynomial functions and graphs](../03-high-school/04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#end-behaviour).

The **epsilon-delta definition** of a limit says that $\lim_{x \to a} f(x) = L$ when for every $\varepsilon > 0$ there is a $\delta > 0$ such that for every $x$, if $0 < \lvert x - a \rvert < \delta$ then $\lvert f(x) - L \rvert < \varepsilon$. The tolerance $\delta$ may depend on $\varepsilon$ but not on $x$. Taught in [the epsilon-delta definition](../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md#definitions).

An **equation** is a statement that two expressions are equal, such as $2x + 1 = 7$. Solving it means finding every value of the variable that makes it true. Taught in [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md).

In a market, the **equilibrium** is the price at which the quantity demanded equals the quantity supplied. To find it, set the two quantities equal, not the two prices. Taught in [systems of linear equations](../03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md#applications).

The **equivalence class** of $a$ under an equivalence relation $\sim$ is the set $[a]$ of everything equivalent to $a$. Under congruence mod 3, $[1] = [4]$, so $[a] = [b]$ does not mean $a = b$. Taught in [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#equivalence-classes).

An **equivalence relation** on a set is a relation that is reflexive, symmetric and transitive. It sorts the set into equivalence classes that form a partition. Taught in [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#equivalence-relations).

The word **equivalent** has a precise meaning for each kind of object. Two fractions are equivalent when they are equal as numbers, as $\frac{1}{4}$ and $\frac{2}{8}$ are, and two ratios are equivalent when one is the other with every term multiplied by the same nonzero number, as with $1:3$ and $2:6$. Two expressions are equivalent when they have the same value for every value of their variables. Two equations, or two inequalities, are equivalent when they have the same solution set. Two statements of logic are equivalent when they have the same truth value in every row of their truth table. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions), [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions), [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#definitions) and [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#definitions). For statements, see [truth tables and logical equivalence](../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md#logical-equivalence).

An **estimate** is an approximate answer, usually worked out from rounded numbers: $389 + 412 \approx 400 + 400 = 800$, where $\approx$ means "is approximately equal to". Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions) and [estimation and sanity checks](../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md).

**Euler's number** $e \approx 2.71828$ is the limit of $\left(1 + \frac{1}{m}\right)^m$ as $m$ grows. It is the base for which continuous growth is simplest to write. Taught in [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#the-number-e) and continuous compounding and e<!-- link: ../08-financial-math/02-interest-and-growth/04-continuous-compounding-and-e.md -->.

To **evaluate** an expression is to replace each variable with a given number and work out the value. Evaluating $5 + 0.40t$ at $t = 20$ gives 13. Replacing a variable with a number, or with another expression, is called substitution. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#definitions).

A function is **even** when $f(-x) = f(x)$ for every $x$ in its domain, so its graph is symmetric about the $y$-axis. An integer $n$ is even when $n = 2k$ for some integer $k$, so 0 and $-6$ are even. Taught in [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions) and [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#five-working-definitions).

An **event** is a set of outcomes, a subset of the sample space. "The die shows an even number" is the event $\{2, 4, 6\}$. Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#definitions).

An **excluded value** of a rational expression is a number that makes a denominator 0. List it from the original expression, before any cancelling, and keep it excluded after. Taught in [rational expressions](../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md#definitions).

The **exclusive or** $P \oplus Q$ is true exactly when one of $P$, $Q$ is true and the other is false. It differs from the ordinary "or" of mathematics, which is also true when both hold. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#the-connectives).

Cases are **exhaustive** when at least one of them holds in every situation the claim covers, and mutually exclusive when at most one does. A proof by cases needs the first property and not the second. Taught in [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md#definitions).

An **existential statement** $\exists x \in D,\ P(x)$ ("there exists an $x$ in $D$ with $P(x)$") is true when $P(a)$ is true for at least one element $a$ of $D$, and false when it fails for every element of $D$. To prove one, produce a witness. Taught in [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#the-two-quantifiers).

To **expand** a product is to multiply it out into a sum of terms with the distributive property, as in $3(x + 4) = 3x + 12$. Factoring goes the other way. Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#definitions).

The **expanded form** of a number writes it as the sum of the values of its digits: $4{,}072 = 4{,}000 + 70 + 2$. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

The **expected value** $E[X]$ of a random variable is its long-run average: each value weighted by its probability, $\sum x \, P(X = x)$. One roll of a fair die has expected value 3.5, even though no roll shows 3.5. Taught in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md -->.

An **explicit formula**, or closed form, gives the $n$-th term of a sequence directly from $n$, such as $a_n = 100 \cdot 1.02^n$. Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#definitions).

The **exponent** in $b^n$ is $n$, the number of times the base is used as a factor. Negative and fractional exponents extend the idea, so that $b^{-1} = \frac{1}{b}$ and $b^{1/2} = \sqrt{b}$. Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#definitions), [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md) and [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).

An **exponential function** has the form $f(x) = ab^x$ with $a \ne 0$, $b > 0$ and $b \ne 1$. The variable is in the exponent, so equal steps in $x$ multiply the output by the same factor. Taught in [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#definitions).

An **expression** is a combination of numbers, variables and operations with no equals sign, such as $3x^2 - 5x$. An expression has a value, while an equation is true or false. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md).

An **exterior angle** of a polygon is the angle between one side and the extension of the next side. The exterior angle of a triangle equals the sum of the two interior angles not next to it, and the exterior angles of any convex polygon add to $360^\circ$. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#polygon-angles).

An **extraneous solution** is a number that comes out of the solving steps but fails the original equation. Squaring both sides, multiplying by an expression that can be zero, and taking logarithms of both sides can all create one, so every candidate gets checked in the original. Taught in [absolute value equations and inequalities](../03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md#definitions), [rational and radical equations](../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md#definitions) and [exponential and logarithmic equations](../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md#definitions).

**Extrapolation** is using a fitted line to predict outside the range of the data, which is much less reliable. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

The **extreme value theorem** says that a function continuous on a closed interval $[a, b]$ has a maximum and a minimum there. Both conditions matter: $\frac{1}{x}$ on $(0, 1]$ is continuous but has no maximum. Taught in [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#the-extreme-value-theorem).

## F

A **fact family** is the set of four facts made from three related numbers, such as $5 + 7 = 12$, $7 + 5 = 12$, $12 - 7 = 5$ and $12 - 5 = 7$. Multiplication and division have fact families too: $3 \times 8 = 24$ gives $24 \div 3 = 8$ and $24 \div 8 = 3$. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions) and [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions).

A **factor** of an integer is an integer that divides it with no remainder: the positive factors of 12 are 1, 2, 3, 4, 6 and 12. More generally, the factors of a product are the numbers multiplied together, such as 4 and 6 in $4 \times 6 = 24$, or $x - 2$ in $(x - 2)(x + 3)$. As a verb, to factor an expression is to write it as a product, as in $3x + 12 = 3(x + 4)$. Taught in [multiplication and times tables](../01-elementary/03-multiplication-and-times-tables.md#definitions), [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md) , [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#definitions) and [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#definitions).

The **factor theorem** says that $x - c$ is a factor of $p(x)$ exactly when $p(c) = 0$. Taught in [polynomial division and the remainder theorem](../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md#definitions).

The **factorial** of a whole number $n \ge 1$ is $n! = n(n-1)\cdots 2 \cdot 1$, and $0! = 1$. It is the number of ways to line up $n$ different things. Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md#definitions).

A **family of sets** $\{A_i : i \in I\}$ has one set $A_i$ for each index $i$ in an index set $I$. Its union is the set of elements that lie in at least one $A_i$, and its intersection is the set of elements that lie in every $A_i$. Taught in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#indexed-families).

The **feasible region** of a system of linear inequalities is the set of points that satisfy every constraint. It can be bounded (it fits inside a circle), unbounded, or empty, in which case the problem is infeasible. Taught in [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#definitions).

A **Fermi estimate** writes an unknown quantity as a product of factors that can each be guessed, aiming for the right order of magnitude rather than the right digits. Taught in [estimation and sanity checks](../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md#definitions).

The **Fibonacci sequence** is defined by $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$, so it runs $0, 1, 1, 2, 3, 5, 8, 13, \dots$ Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#definitions).

A **field** is a set with addition and multiplication that satisfy all eleven field axioms. The rationals, the reals and the complex numbers are fields, and the integers are not, because most integers have no reciprocal in the integers. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#the-field-axioms).

The **field axioms** are the eleven rules for addition and multiplication that the real numbers satisfy: closure, associativity and commutativity of each operation, the identities 0 and 1 with $0 \ne 1$, additive inverses, reciprocals of nonzero numbers, and the distributive law. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#the-field-axioms).

A set is **finite** if it can be paired off with $\{1, 2, \dots, n\}$ for some $n \in \mathbb{N}$, and then its cardinality is $n$. A set is infinite if it is not finite, and an infinite set such as $\mathbb{N}$ can have the same size as a proper part of itself. Taught in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#finite-infinite-countable).

The **five-number summary** of a data set is its minimum, $Q_1$, median, $Q_3$ and maximum. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

A **flawed proof** is an argument written as a proof that a careful reader would not accept. The trouble is of one of three kinds: the claim is false, a step is invalid, or there is a gap, meaning a true but unjustified step or a missing case. Taught in [common proof mistakes](../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md#definitions).

The **floor** of a number $x$, written $\lfloor x \rfloor$, is the greatest integer less than or equal to $x$. So $\lfloor 3.7 \rfloor = 3$ and $\lfloor -3.7 \rfloor = -4$. Taught in [piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md#definitions).

The **forward-backward method** alternates working forward from the givens with working backward from the goal, asking "what would be enough to prove it?", until the two meet. A backward step can be written into the proof only when it is reversible. Taught in [scratch work and proof strategies](../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md#definitions).

For whole numbers $a$ and $b$ with $b \ne 0$, the **fraction** $\frac{a}{b}$ is the number $a \div b$. The denominator $b$ says how many equal parts the whole is cut into, and the numerator $a$ says how many of those parts you have. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions).

A **free variable** is a letter whose meaning comes from outside the expression, such as $n$ in $\sum_{i=1}^{n} i$. A sentence with a free variable, such as "$x > 3$", is not a statement until $x$ is given a value or a quantifier. Taught in [reading math symbols](../04-proofs-and-logic/01-language-and-notation/04-reading-math-symbols.md#definitions) and [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#the-two-quantifiers).

A **full binary tree** is defined recursively: a single node, called a leaf, is one, and a new node (the root) with two full binary trees as its left and right subtrees is one. Every node has 0 or 2 children, and a node with children is internal. Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#definitions).

A **function** from a set $A$ to a set $B$ assigns to each element of $A$ exactly one element of $B$. A rule such as $f(x) = x^2$ is one way to give a function. Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#definitions) and [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#definitions); the formal definition, as a set of ordered pairs, is in [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md).

The **fundamental theorem of algebra** says that every polynomial of degree at least 1 has a zero among the complex numbers, so a polynomial of degree $n$ has $n$ complex zeros when they are counted with multiplicity. Taught in [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#why-complex-numbers-are-worth-having).

The **fundamental theorem of arithmetic** says that every whole number greater than 1 can be written as a product of primes in exactly one way, apart from the order of the factors, as in $360 = 2^3 \times 3^2 \times 5$. It is the reason 1 is not called prime. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions) and primes and unique factorization<!-- link: ../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md -->.

## G

A **gap** in a proof is a step whose justification is not on the page and that the reader cannot fill in at once. Routine gaps are filled in silently by the audience, but a gap that hides the whole difficulty means the proof is not yet a proof. Taught in [how to read a proof](../04-proofs-and-logic/03-core-proof-methods/02-how-to-read-a-proof.md#definitions).

The **geometric mean** of $x$ and $y$ is the number $g$ with $\frac{x}{g} = \frac{g}{y}$, so $g = \sqrt{xy}$. The altitude to the hypotenuse of a right triangle is the geometric mean of the two pieces it cuts the hypotenuse into. Taught in [similarity](../03-high-school/08-geometry-and-proof/03-similarity.md#the-altitude-to-the-hypotenuse) and [direct proof](../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md#definitions), where $\sqrt{ab}$ is compared with the arithmetic mean.

A **geometric sequence** multiplies by the same number, the common ratio $r$, at every step, so $a_n = a_0 r^n$ when the first term has index 0. Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#definitions).

A **geometric series** is the sum of the terms of a geometric sequence. With $n$ terms, the sum is $a\,\frac{1 - r^n}{1 - r}$ for $r \ne 1$, where $a$ is the first term. Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#definitions).

The **givens** of a proof are the statements you may use: the hypotheses, the definitions and the results already proved. The goal is the statement you must reach. Taught in [scratch work and proof strategies](../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md#definitions).

The **graph of a function** $f$ is the set of all points $(x, f(x))$ for $x$ in the domain. Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#definitions) and [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#definitions).

The **greatest common factor** (GCF) of two whole numbers is the largest number that is a factor of both. It is also called the greatest common divisor and written $\gcd(a, b)$, so $\gcd(12, 18) = 6$. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions) and GCD and Euclid's algorithm<!-- link: ../06-cs-math/02-number-theory/02-gcd-and-euclids-algorithm.md -->.

The **growth factor** of an exponential function is its base $b$ when $b > 1$: each step of 1 in $x$ multiplies the output by $b$. A 5% yearly increase has growth factor 1.05. Taught in [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#definitions).

## H

The **half-life** of a decaying quantity is the time it takes to halve, so the quantity is $A_0 \left(\frac{1}{2}\right)^{t/T}$ for a half-life $T$. Taught in [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#doubling-time-and-half-life).

A **Hasse diagram** draws a finite partially ordered set as dots, with $b$ drawn above $a$ and joined to it by a line whenever $b$ covers $a$, that is, $a \prec b$ with nothing strictly between. Then $a \preceq b$ exactly when a path goes upward from $a$ to $b$, or $a = b$. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#hasse-diagrams).

The **height** of a triangle or a parallelogram is the perpendicular distance from the base to the opposite vertex or side. It is measured at a right angle to the base, not along a slanted side. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#base-and-height).

A **heuristic** is a rule of thumb that often helps and carries no guarantee, such as trying small cases or working backward from the goal. Taught in [scratch work and proof strategies](../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md#definitions).

**Hexadecimal**, or hex, is base 16, with the digits 0 to 9 and then A to F for the values 10 to 15. Each hex digit stands for exactly 4 bits, which is why programmers use it: $\mathrm{FF}_{16} = 1111\,1111_2 = 255$. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

A **histogram** groups numerical data into equal-width bins and draws a bar for each bin, with the bars touching, so that the height shows the count. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

A **hole** in a graph is a single missing point at a place where a factor cancelled from numerator and denominator. The function is undefined there, but the graph approaches a finite height. Taught in [rational functions and asymptotes](../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md#definitions).

A **horizontal asymptote** is a horizontal line $y = L$ that a graph approaches as $x$ grows large in either direction. For a rational function it is $y = 0$ when the numerator has the smaller degree and the ratio of the leading coefficients when the degrees are equal. A graph can cross a horizontal asymptote at a finite $x$. In limit notation, $y = L$ is a horizontal asymptote when $\lim_{x \to \infty} f(x) = L$ or $\lim_{x \to -\infty} f(x) = L$. Taught in [rational functions and asymptotes](../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md#definitions), [exponential functions and growth](../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md#definitions) and [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#definitions).

The **horizontal line test** says that a function is one-to-one, and so has an inverse function, exactly when every horizontal line meets its graph at most once. Taught in [composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md#definitions).

A **horizontal shift** replaces $f(x)$ with $f(x - h)$ and moves the graph right by $h$, or left when $h$ is negative. Taught in [transformations of functions](../03-high-school/03-functions/04-transformations-of-functions.md#definitions).

**Horner's method** evaluates a polynomial by nested factoring, as in $2x^3 - 5x^2 + 4x - 7 = ((2x - 5)x + 4)x - 7$. A polynomial of degree $n$ then takes $n$ multiplications. Taught in [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md#evaluating-a-polynomial-with-horners-method).

A **hyperbola** is the set of points for which the distances to two fixed points, the foci, differ by a constant. Its two branches approach lines called asymptotes. Taught in [conic sections](../03-high-school/08-geometry-and-proof/05-conic-sections.md#definitions).

The **hypotenuse** is the side of a right triangle opposite the right angle, always the longest side. The other two sides are the legs. Taught in [the Pythagorean theorem](../02-middle-school/06-geometry/04-pythagorean-theorem.md#definitions) and [right triangle trigonometry](../03-high-school/09-trigonometry/01-right-triangle-trigonometry.md#definitions).

The **hypothesis** of "if P, then Q" is P, the part that is assumed, also called the antecedent. The hypotheses of a theorem are what its proof may use. In statistics, a hypothesis is instead a claim to be tested. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#conditional-statements) and [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md).

## I

An **identity** is an equation that is true for every value of its variables, such as $(a + b)^2 = a^2 + 2ab + b^2$. The word also names something that changes nothing: $0$ for addition and $1$ for multiplication (the identity properties $a + 0 = a$ and $a \times 1 = a$), the identity matrix $I$ and the identity function $x \mapsto x$. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#identity-properties) and [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md) and, for trigonometric identities, [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#definitions).

The **identity function** on a set $A$ is $\text{id}_A \colon A \to A$ with $\text{id}_A(x) = x$. Composing a function with an identity function leaves it unchanged. Taught in [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#identity-and-composition).

The **identity matrix** $I$ is the square matrix with 1 on the diagonal from top left to bottom right and 0 elsewhere. It satisfies $AI = IA = A$, so it plays the role of the number 1. Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#definitions).

**Iff** is short for "if and only if". "P iff Q" means that P and Q imply each other, so they are true together or false together. A proof of an iff statement usually has two parts, one for each direction. Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md) and [if and only if proofs](../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md).

The **image** of a figure under a transformation is the figure it is moved to. For a function $f$, the image of a set $S$ of inputs is the set $f(S)$ of their outputs, and the image of the whole domain is the range. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#definitions), [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#definitions) and [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#image-and-preimage-of-a-set).

The **imaginary unit** $i$ is a number defined by $i^2 = -1$. Its powers repeat in a cycle of four: $i, -1, -i, 1$. Taught in [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#definitions).

**Implicit differentiation** differentiates both sides of an equation relating $x$ and $y$ with respect to $x$, treating $y$ as an unknown function of $x$, and then solves for $\frac{dy}{dx}$. Every term with $y$ gets a factor $\frac{dy}{dx}$ from the chain rule, so the derivative of $y^3$ is $3y^2\frac{dy}{dx}$. Taught in [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md#implicit-differentiation).

**Implied multiplication** is a product written side by side with no sign: $3x$ means $3 \cdot x$, and $2(x + 1)$ means $2 \cdot (x + 1)$. A sign comes back once numbers replace the letters, since $3 \cdot 4$ is 12 while $34$ is thirty-four. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#how-multiplication-is-written).

An **improper fraction** has a numerator at least as big as its denominator, so it is 1 or more, as $\frac{11}{4}$ and $\frac{4}{4}$ are. A proper fraction, such as $\frac{3}{8}$, has a numerator smaller than its denominator and is less than 1. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions).

The **inclusive or** is the ordinary "or" of mathematics: "$P$ or $Q$" is true when at least one of them is true, and also when both are. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#the-connectives).

A function is **increasing** on an interval when larger inputs in the interval give larger outputs, and **decreasing** when larger inputs give smaller outputs. Intervals are stated in terms of $x$, not of heights. Taught in [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions).

Two events are **independent** when knowing that one happened doesn't change the probability of the other, which means $P(A \text{ and } B) = P(A)\,P(B)$. Successive coin flips are independent, and draws without replacement are not. Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#definitions).

The **independent variable** of a function is the input, usually $x$, whose value you choose. The output $y = f(x)$ is the dependent variable, because its value depends on the input. Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#definitions).

**Induction**, or mathematical induction, proves a statement for every natural number in two parts. The base case proves it for the first value, usually $n = 0$ or $n = 1$, and the inductive step shows that the statement for $k$ implies the statement for $k + 1$. Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md).

In an induction proof, the **inductive hypothesis** is the assumption that $P(k)$ is true. Assuming it is not circular, because the step proves only the implication from $P(k)$ to $P(k + 1)$. Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#definitions).

The **inductive step** is the proof that $P(k)$ implies $P(k + 1)$ for an arbitrary integer $k$ from the first value on. In plain words, it is the spacing between dominoes. Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#definitions).

An **inequality** compares two expressions with $<$, $\le$, $>$ or $\ge$, such as $2x + 1 < 7$. Its solution is usually a whole interval of numbers rather than a single value. Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md) and [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#definitions).

An **infinite limit**, written $\lim_{x \to a} f(x) = \infty$, means that $f(x)$ becomes larger than any number you name as $x$ gets close to $a$. It describes how a limit fails to exist, and the line $x = a$ is then a vertical asymptote. Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#definitions).

A function is **injective**, or one-to-one, when different inputs always give different outputs: $f(a_1) = f(a_2)$ implies $a_1 = a_2$. The squaring function on $\mathbb{R}$ is not injective, since $(-2)^2 = 2^2$. Taught in [composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md#definitions) (as one-to-one) and [injective, surjective and bijective](../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md).

The **instantaneous rate of change** of $f$ at $a$ is the derivative $f'(a)$, in units of $f(x)$ per unit of $x$. If $s(t)$ is a position in metres and $t$ is in seconds, then $s'(t)$ is a velocity in metres per second. Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#definitions).

An **integer** is a whole number or the opposite of one: $\dots, -2, -1, 0, 1, 2, \dots$. The set of integers is $\mathbb{Z}$. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions) and [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).

The definite **integral** $\int_a^b f(x)\,dx$ is the signed area between the graph of $f$ and the $x$-axis from $a$ to $b$, defined as a limit of sums of thin rectangles. The indefinite integral $\int f(x)\,dx$ is the family of antiderivatives of $f$. The formal definition is in [Riemann sums and the definite integral](../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md).

An **intercept** is a point where a graph crosses an axis. The $y$-intercept of a line is $(0, b)$ and the $x$-intercept is $(a, 0)$. The $x$-intercepts of a function's graph are its zeros. Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#definitions) and [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions).

The **intermediate value theorem** says that a continuous function, such as a polynomial, that has opposite signs at $a$ and $b$ has a zero between $a$ and $b$. A polynomial can have an even number of zeros between two points where it has the same sign. For any function continuous on $[a, b]$, the theorem says it takes every value between $f(a)$ and $f(b)$. Taught in [polynomial functions and graphs](../03-high-school/04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#what-the-graph-must-do) and [continuity, asymptotes and the IVT](../05-university-core/01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md#the-intermediate-value-theorem).

**Interpolation** is using a fitted line to predict inside the range of the data. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

The **interquartile range** (IQR) is $Q_3 - Q_1$, the width of the middle half of the data. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

The **intersection** $A \cap B$ of two sets is the set of elements that are in both. In a solution set, "and" means intersection. Taught in [compound inequalities and interval notation](../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md#definitions) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#the-four-operations).

An **interval** is the set of all real numbers between two endpoints, with each endpoint included or left out. Taught in [compound inequalities and interval notation](../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md#definitions).

**Interval notation** writes an interval with its endpoints: $(a, b)$ leaves both out, $[a, b]$ includes both, and $\infty$ always gets a parenthesis, as in $[3, \infty)$, because it is not a number. A closed dot on a number line marks an included endpoint and an open dot an excluded one. Taught in [compound inequalities and interval notation](../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md#definitions).

An **invariant** is a property that stays true at every step of a process, such as every pass through a loop. It is the standard tool for proving an algorithm correct: show it holds at the start, show each step keeps it true, and see what it says when the process stops. A loop invariant is proved by induction on the number of passes. Taught in invariants and algorithm correctness<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md --> and [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#in-code).

The **inverse** of a function $f$ is the function $g$ with $g(f(x)) = x$ for every $x$ in the domain of $f$ and $f(g(y)) = y$ for every $y$ in the domain of $g$, written $f^{-1}$. It undoes $f$, and it is not the reciprocal $\frac{1}{f}$. In logic, the inverse of "if $P$, then $Q$" is "if not $P$, then not $Q$", which is equivalent to the converse and not to the original. Taught in [composition and inverse functions](../03-high-school/03-functions/05-composition-and-inverse-functions.md#definitions), [injective, surjective and bijective](../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md#proving-bijective-and-the-inverse) and [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md#converse-inverse-and-contrapositive).

The **inverse function rule** says that if $f$ is continuous and one-to-one near $a$ and differentiable at $a$ with $f'(a) \ne 0$, then its inverse is differentiable at $b = f(a)$ and $\left(f^{-1}\right)'(b) = \frac{1}{f'(a)}$. The slope of $f$ is taken at the matching point $a$, not at $b$. Taught in [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md#the-derivative-of-an-inverse-function).

The **inverse matrix** of a square matrix $A$ is a matrix $A^{-1}$ with $AA^{-1} = A^{-1}A = I$, and a matrix with an inverse is invertible. It is not the matrix of entrywise reciprocals. The system $A\mathbf{x} = \mathbf{b}$ then has the solution $\mathbf{x} = A^{-1}\mathbf{b}$. Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#definitions).

Two operations are **inverse operations** when each one undoes the other: subtracting 5 undoes adding 5, and dividing by $c$ undoes multiplying by $c$, for $c \ne 0$. Solving an equation means applying inverse operations to both sides. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions), [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#definitions).

An **inverse trig function** is the inverse of a trigonometric function restricted to a domain where it is one-to-one. This is why $\sin^{-1}(\sin x) = x$ only for $x$ from $-\frac{\pi}{2}$ to $\frac{\pi}{2}$. Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#definitions).

Two quantities are **inversely proportional** when their product is constant, so $y = \frac{k}{x}$, and doubling one halves the other. On a 240 km drive the time is $\frac{240}{\text{speed}}$: 4 h at 60 km/h, and 2 h at 120 km/h. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#what-is-inverse-proportion).

An **irrational** number is a real number that is not rational, so it can't be written as a fraction of two integers. Its decimal expansion never ends and never repeats. Two examples are $\sqrt{2}$ and $\pi$. Taught in [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#not-every-number-is-rational) and [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).

A relation is **irreflexive** if no element is related to itself, so no vertex of its digraph has a loop. This is stronger than "not reflexive", which says only that some element fails. The relation $<$ is irreflexive. Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#the-four-properties).

An **isosceles triangle** has at least two equal sides. The angles opposite the equal sides, the base angles, are equal. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#triangles) and [congruence and triangle proofs](../03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md#definitions).

## K

The **kernel** of a function $f$ is the relation "$a \sim a'$ when $f(a) = f(a')$" on its domain. It is an equivalence relation, and its classes are the sets of inputs that $f$ cannot tell apart. A hash function sorts keys into buckets in this way. Taught in [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#the-kernel-of-a-function).

## L

The **law of cosines** says that $c^2 = a^2 + b^2 - 2ab\cos C$, where $C$ is the angle between sides $a$ and $b$. When $C = 90^\circ$ it becomes the Pythagorean theorem. Taught in [law of sines and law of cosines](../03-high-school/09-trigonometry/05-law-of-sines-and-cosines.md#definitions).

The **law of sines** says that in a triangle with sides $a$, $b$, $c$ opposite angles $A$, $B$, $C$, $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$. Taught in [law of sines and law of cosines](../03-high-school/09-trigonometry/05-law-of-sines-and-cosines.md#definitions).

The **laws of exponents** are the identities $a^m a^n = a^{m+n}$, $\frac{a^m}{a^n} = a^{m-n}$, $(a^m)^n = a^{mn}$, $(ab)^n = a^n b^n$ and $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$. They hold for all whole-number exponents, and the zero and negative exponent rules extend them to every integer. Taught in [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md#definitions).

The **laws of logarithms** are $\log_b(xy) = \log_b x + \log_b y$, $\log_b \frac{x}{y} = \log_b x - \log_b y$ and $\log_b x^p = p \log_b x$, for positive $x$ and $y$. There is no rule for $\log_b(x + y)$. Taught in [logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md#definitions).

The **least common multiple** (LCM) of two positive integers is the smallest positive number that is a multiple of both, written $\operatorname{lcm}(a, b)$, so $\operatorname{lcm}(12, 18) = 36$. The product of the two numbers is always a common multiple, but it is the least one only when their greatest common factor is 1. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions).

A **least element** of a subset $S$ of a partially ordered set is an $m \in S$ with $m \preceq x$ for every $x \in S$, and a greatest element is the same with the order reversed. A minimal element has nothing below it, while a least element is below everything, so there can be several minimal elements and no least one. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#minimal-maximal-least-and-greatest).

An upper bound of a set $S$ of real numbers is a number $u$ with $s \le u$ for every $s$ in $S$. A **least upper bound** of $S$ is an upper bound that is less than or equal to every other upper bound. The completeness axiom says that every nonempty set of real numbers with an upper bound has one, and that is what distinguishes $\mathbb{R}$ from $\mathbb{Q}$. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#the-completeness-axiom).

A **lemma** is a smaller result, proved mainly as a step toward a theorem. A few lemmas are important in their own right, such as the pumping lemma in theory of computation. Taught in [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md).

The **lexicographic order** on strings is the order of a dictionary: a string $u$ comes before $v$ when $u$ is a prefix of $v$, or when at the first position where they differ the letter of $u$ is below the letter of $v$. Every two different strings are comparable, so it is a total order. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#examples).

**Like terms** have the same variables, each raised to the same power, so only their coefficients differ: $3x^2$ and $-5x^2$ are like terms, but $3x^2$ and $3x$ are not. Only like terms combine into one term, as in $3x + 5x = 8x$. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#definitions) and [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#the-properties-behind-each-step).

The **limit** of $f(x)$ as $x$ approaches $a$ is the value that $f(x)$ gets as close as you like to when $x$ is close enough to $a$, whatever happens at $a$ itself. The intuition is in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md), and the formal version is in [the epsilon-delta definition](../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md).

A **limit at infinity**, $\lim_{x \to \infty} f(x) = L$, means that $f(x)$ can be made as close to $L$ as we like by taking $x$ large enough. When $L$ is a real number, the line $y = L$ is a horizontal asymptote. Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#definitions).

The **limit laws** say that when $\lim f(x) = L$ and $\lim g(x) = M$ both exist as real numbers, the limit of a sum, difference, constant multiple, product, power or root is the same combination of the limits, and so is the limit of a quotient when $M \ne 0$. They say nothing when a piece has no limit. Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#definitions).

A **line of best fit** is a line drawn through the middle of a scatter plot that models a linear trend. Its slope is the predicted change in $y$ for each extra unit of $x$. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

A **line segment** is the part of a line between two endpoints, written $\overline{PQ}$ for the endpoints $P$ and $Q$, and its length is the distance between them. A line $\overleftrightarrow{PQ}$ goes on forever in both directions, and a ray $\overrightarrow{PQ}$ starts at $P$ and goes on forever through $Q$. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#points-lines-and-angles).

A **linear combination** of vectors $\mathbf{v}_1, \dots, \mathbf{v}_n$ is a sum $c_1\mathbf{v}_1 + \dots + c_n\mathbf{v}_n$, where the weights $c_1, \dots, c_n$ are numbers. For example, $2(1, 0) + 3(0, 1) = (2, 3)$. For integers $b$ and $c$, a linear combination of $b$ and $c$ is a number $bx + cy$ with integers $x$ and $y$, and a common divisor of $b$ and $c$ divides every one of them; see [direct proof](../04-proofs-and-logic/03-core-proof-methods/01-direct-proof.md#definitions). Taught in vectors, dot product and span<!-- link: ../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md -->.

A **linear equation** in one variable is an equation that can be rearranged into the form $ax = b$ by expanding, combining like terms and doing the same operation to both sides. Once the brackets are expanded, the variable appears only to the first power: $3(x - 1) = 5x + \frac{x}{2}$ is linear, while $x^2 = 3x$ is not. Taught in [multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#definitions). The version with two variables, whose graph is a line, is in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#definitions) and [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md#definitions).

A **linear extension** of a finite partially ordered set is a list of all its elements, each once, in which $x_i \preceq x_j$ implies $i \le j$. In plain words, it is a total order that agrees with the partial order. Producing one from a set of dependencies is called topological sorting. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#topological-sorting).

A **linear function** is a function of the form $f(x) = mx + b$, whose graph is a straight line. Any other function is nonlinear. Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#definitions).

A **linear program** is the problem of maximizing or minimizing a linear objective function over a region defined by linear constraints. On a bounded feasible region the best value occurs at a corner point. Taught in [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#definitions).

A **literal equation** is an equation whose quantities are all letters, such as the formula $A = P + Prt$. To solve it for a target letter, apply inverse operations as you would with numbers, and note any restriction on the other letters, such as $m \ne 0$, under which the solved form is equivalent to the original. Taught in [linear and literal equations](../03-high-school/01-algebra-foundations/02-linear-and-literal-equations.md#definitions).

A **local maximum** of $f$ at $c$ is a value $f(c)$ that is at least as large as the values at all nearby inputs. A local minimum is defined the same way with "at most". Taught in [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions).

The **logarithm** $\log_b x$ is the exponent $y$ for which $b^y = x$, defined for a base $b > 0$ with $b \ne 1$ and for $x > 0$. So $\log_5 125 = 3$, because $5^3 = 125$. Logarithms undo exponentials, and the logarithm of 0 or of a negative number is undefined in the real numbers. The function $f(x) = \log_b x$ is the inverse of $b^x$, and base 10 gives the common logarithm, written $\log x$. Taught in [logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md#definitions).

A **logarithmic axis** is an axis on which equal distances stand for equal ratios, not equal differences. A graph of exponential growth on a logarithmic axis is a straight line. Taught in [logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md#log-scales).

**Logarithmic differentiation** differentiates a function with variables in both the base and the exponent, or a long product or quotient, by taking the natural logarithm of both sides first and then differentiating implicitly. Taught in [chain rule, implicit and inverse derivatives](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md#logarithmic-differentiation).

Two statements are **logically equivalent**, written $A \equiv B$, when they have the same truth value in every row of the truth table. For example, $P \Rightarrow Q$ is equivalent to $\neg P \vee Q$ and to its contrapositive. A single row where they differ shows they are not equivalent. Taught in [truth tables and logical equivalence](../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md#logical-equivalence).

A **loop invariant** is a statement about the variables of a loop that is true before the loop starts and stays true after every pass. Proving it is an induction on the number of passes. Taught in [mathematical induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md#in-code).

## M

The **magnitude**, or length, of a vector $\mathbf{v} = (a, b)$ is $\lVert \mathbf{v} \rVert = \sqrt{a^2 + b^2}$. The length of a sum of vectors is at most the sum of their lengths, with equality only when they point the same way. Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md#definitions).

A store's **margin**, or gross margin, is its profit written as a percent of the selling price. An item bought for \$40 and sold for \$50 makes \$10 of profit, a margin of $\frac{10}{50} = 20\%$. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions).

The **marginal cost** $C'(q)$ is the derivative of the cost $C(q)$ of producing $q$ units: the cost of producing one more unit at output $q$, to a good approximation, in dollars per unit. Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#definitions).

A **marginal rate** is the rate that applies to the next dollar of income, as opposed to the average rate, which is the total tax divided by the total income. Taught in [piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md#definitions).

The **marginal revenue** $R'(q)$ is the derivative of the revenue $R(q)$ from selling $q$ units: the extra revenue from selling one more unit at output $q$, to a good approximation. Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#definitions).

A **markup** is the amount a store adds to its cost to get the selling price, usually written as a percent of the cost. The item bought for \$40 and sold for \$50 has a markup of $\frac{10}{40} = 25\%$, while its margin is 20%, because the margin divides the same profit by the bigger price. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions).

A **matrix** is a rectangular grid of numbers. One with $m$ rows and $n$ columns is an $m \times n$ matrix. A matrix can hold the coefficients of a system of equations, or describe a linear transformation. Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md).

The **matrix product** $AB$ of an $m \times n$ matrix $A$ and an $n \times p$ matrix $B$ is the $m \times p$ matrix whose entry in row $i$ and column $j$ is the dot product of row $i$ of $A$ with column $j$ of $B$. It is defined only when the number of columns of $A$ equals the number of rows of $B$, and in general $AB \ne BA$. Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#definitions).

A **maximal element** of a subset $S$ of a partially ordered set is an element with nothing in $S$ strictly above it. It is not the same as a greatest element, which is above everything in $S$, because several elements can be maximal at once. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#minimal-maximal-least-and-greatest).

The **mean** of a list of numbers is their sum divided by how many there are, the ordinary average. The mean of 2, 4 and 9 is $\frac{15}{3} = 5$. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md).

The **mean absolute deviation** (MAD) is the average distance from the values to their mean. Absolute values are needed because the plain deviations from the mean always add to 0. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

The **median** is the middle value of a list sorted in order, or the mean of the two middle values when the list has an even number of entries. Extreme values move it less than they move the mean: the median of 2, 4 and 90 is 4, while the mean is 32. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md).

A **median of a triangle** is a segment from a vertex to the midpoint of the opposite side. A median in statistics is a different thing. Taught in [congruence and triangle proofs](../03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md#parts-of-a-triangle-used-in-proofs).

A **metric prefix** is a word put in front of a unit to multiply it by a power of ten: kilo is $10^3$, centi is $10^{-2}$ and milli is $10^{-3}$, so a kilometre is 1000 m. The symbols are case-sensitive, since M is mega ($10^6$) and m is milli. Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#metric-prefixes) and [measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#definitions).

The **midpoint** of a segment is the point halfway between its endpoints. In the plane, the midpoint of the segment from $(x_1, y_1)$ to $(x_2, y_2)$ is $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#definitions) and [coordinate geometry and circles](../03-high-school/08-geometry-and-proof/04-coordinate-geometry-and-circles.md#definitions).

A **midsegment** of a triangle is a segment joining the midpoints of two sides. It is parallel to the third side and half as long. Taught in [similarity](../03-high-school/08-geometry-and-proof/03-similarity.md#the-triangle-proportionality-theorem).

A **minimal element** of a subset $S$ of a partially ordered set is an $m \in S$ with no $x \in S$ strictly below it. Several elements can be minimal at once, and then there is no least element. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#minimal-maximal-least-and-greatest).

A **mixed number** is a whole number followed by a proper fraction, and it means their sum: $2\frac{3}{4} = 2 + \frac{3}{4} = \frac{11}{4}$. A negative mixed number is the opposite of the whole thing, so $-2\frac{1}{4} = -\frac{9}{4}$. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions) and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#where-the-minus-sign-goes).

**Mod**, short for modulo, has two related uses. As an operation, $a \bmod n$ is the remainder when $a$ is divided by $n$, so $17 \bmod 5 = 2$. As a relation, $a \equiv b \pmod{n}$ says that $a$ and $b$ leave the same remainder, and $n$ is called the **modulus**. (The modulus of a complex number is something else, its distance from 0, taught in [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#definitions).) Taught in divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

The **mode** is the value that occurs most often in a list. A list can have more than one mode. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md).

The **modulus** of a complex number, $\lvert a + bi \rvert = \sqrt{a^2 + b^2}$, is its distance from 0 in the complex plane, not $a + b$. Taught in [complex numbers](../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md#definitions).

A **multiple** of an integer $n$ is $n$ times some integer, so the multiples of 4 are $\dots, -8, -4, 0, 4, 8, \dots$. Saying that $b$ is a multiple of $a$ is the same as saying that $a$ is a factor of $b$. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md).

The **multiplicity** of a zero $c$ is the largest $k$ for which $(x - c)^k$ is a factor of the polynomial. The graph crosses the axis at a zero of odd multiplicity and touches it and turns back at a zero of even multiplicity. Taught in [polynomial functions and graphs](../03-high-school/04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#definitions).

The **multiplier** of a percent change, also called the growth factor, is $1 + r$, where $r$ is the rate written as a decimal, so that $\text{new} = (1 + r) \times \text{old}$. A 7.5% increase has multiplier 1.075, and a 30% decrease has multiplier 0.70. Changes in a row combine by multiplying their multipliers. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions).

Two events are **mutually exclusive** when they can't both happen. For such events $P(A \text{ or } B) = P(A) + P(B)$. Two events with positive probabilities that are mutually exclusive are never independent. In a proof by cases, the cases are mutually exclusive when at most one of them holds. Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#definitions) and [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md#definitions).

## N

An **$n$-th root** of a number $a$ is a number $b$ with $b^n = a$. The principal $n$-th root, written $\sqrt[n]{a}$, is the real root when $n$ is odd and the non-negative root when $n$ is even and $a \ge 0$. The integer $n$ is the index of the root. Taught in [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md#definitions).

The **natural domain** of a formula is the set of all real numbers for which the formula gives a real number. For $\frac{1}{\sqrt{x - 2}}$ it is $x > 2$. Taught in [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#definitions).

The **natural logarithm** is the logarithm in base $e$, written $\ln x$. Python's `math.log` is the natural logarithm, not base 10. Taught in [logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md#definitions).

A **natural number** is a counting number. In this book the natural numbers are $\mathbb{N} = \{0, 1, 2, \dots\}$, but many books start at 1, so check the definition in whatever you are reading. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions) and [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).

A condition Q is **necessary** for P when P can't happen without Q, which is the statement "if P, then Q". Being even is necessary for being divisible by 4. Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md).

The **negation** $\neg P$ ("not $P$") of a statement is true exactly when $P$ is false. To negate a longer statement, push the "not" inward: "and" swaps with "or", "for every" swaps with "there exists", and the negation of "if $P$, then $Q$" is "$P$ and not $Q$". Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#the-connectives) and [negation and translating English](../04-proofs-and-logic/02-logic-and-sets/05-negation-and-translating-english.md#the-negation-rules).

A **negative exponent** means a reciprocal: $a^{-n} = \frac{1}{a^n}$ for $a \ne 0$. So $2^{-1} = \frac{1}{2}$ and $10^{-2} = 0.01$, and the result is not a negative number. Taught in [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md#definitions).

A **negative number** is a number less than 0, and a positive number is one greater than 0. Zero is neither, and a number that is positive or 0 is called non-negative. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions).

A **non-constructive proof** of an existence claim shows that an object must exist without saying which one. It hands you a guarantee instead of the object. Taught in [existence and uniqueness proofs](../04-proofs-and-logic/04-more-proof-methods/02-existence-and-uniqueness-proofs.md#definitions).

A negation is in **normal form** when the "not" has been pushed inward as far as it goes, so that it sits only on the smallest pieces, such as a single comparison. Taught in [negation and translating English](../04-proofs-and-logic/02-logic-and-sets/05-negation-and-translating-english.md#the-negation-rules).

The **number line** is a straight line with one point marked 0, on which each number is a point: a positive number $x$ lies $x$ units to the right of 0, and $-x$ lies $x$ units to the left. Of two numbers, the one further left is smaller, so $-27 < -4$. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions).

The **numerator** of a fraction $\frac{a}{b}$ is the number on top, $a$, which says how many of the equal parts you have. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md).

## O

An **objective function** is the linear quantity to be made as large or as small as possible, such as profit. Taught in [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#definitions).

A function is **odd** when $f(-x) = -f(x)$ for every $x$ in its domain, so its graph is unchanged by a half-turn about the origin. An integer $n$ is odd when $n = 2k + 1$ for some integer $k$, so $-7 = 2 \times (-4) + 1$ is odd. Taught in [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions) and [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#five-working-definitions).

The **one-sided limits** of $f$ at $a$ are the left-hand limit $\lim_{x \to a^-} f(x)$, which uses only inputs with $x < a$, and the right-hand limit $\lim_{x \to a^+} f(x)$, which uses only inputs with $x > a$. The two-sided limit exists exactly when both exist and are equal. Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#definitions).

An **open sentence**, or predicate, is a sentence $P(x)$ with a variable $x$ that becomes a statement when $x$ is replaced by an element of its domain. "$x$ is even" is an open sentence over $\mathbb{Z}$: $P(6)$ is true and $P(7)$ is false. Taught in [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#open-sentences-and-domains).

An **operation symbol** takes objects and builds a new object, such as $+$, $\cup$ or $\sum$, while a **relation symbol** takes objects and makes a statement, such as $=$, $\le$, $\in$ or $\mid$. In plain words, an operation gives you a thing, and a relation gives you a claim about things. Taught in [reading math symbols](../04-proofs-and-logic/01-language-and-notation/04-reading-math-symbols.md#definitions).

The **opportunity cost** of something is what you give up to get it. Along a budget line, it is the number of units of $y$ given up for each extra unit of $x$. Taught in [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#a-budget-constraint).

The **opposite** of a number $a$, written $-a$, is the number at the same distance from 0 on the other side of 0. The opposite of $-7$ is 7, so $-a$ is not always negative. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions).

The **order of magnitude** of a number is the power of ten in its scientific notation, so 93,000,000 is of order $10^7$. Comparing orders of magnitude tells you roughly how many times bigger one quantity is than another. Taught in [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md#definitions).

The **order of operations** is the convention for which operation comes first: grouping symbols, then exponents, then multiplication and division from left to right, then addition and subtraction from left to right. The memory aid is BEDMAS in Canada and PEMDAS in the United States, and in both the two letters of a pair have equal rank. Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#definitions).

An **ordered field** is a field together with a set $P$ of positive elements that is closed under addition and multiplication and such that, for each $a$, exactly one of $a \in P$, $a = 0$ and $-a \in P$ holds. The rationals and reals are ordered fields, and the complex numbers are not. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#the-order-axioms).

An **ordered pair** $(a, b)$ is a pair of numbers in which order counts, so $(2, 5) \ne (5, 2)$. A point in the plane is described by its coordinates, an ordered pair whose first number is the signed distance right of the $y$-axis and whose second is the signed distance above the $x$-axis. As a set-theory object, $(3, 3)$ is a pair while $\{3, 3\}$ is just the set $\{3\}$. Taught in [the coordinate plane](../02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md#definitions) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#ordered-pairs-and-cartesian-products).

An **outlier** is a value far from the rest of the data. By the rule used in this book, it is a value below $Q_1 - 1.5\,\text{IQR}$ or above $Q_3 + 1.5\,\text{IQR}$. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

## P

A **parabola** is the graph of a quadratic function, a smooth U-shaped curve that opens up when $a > 0$ and down when $a < 0$. It can also be defined as the set of points equally far from a fixed point, the focus, and a fixed line, the directrix. Taught in [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#definitions) and [conic sections](../03-high-school/08-geometry-and-proof/05-conic-sections.md#definitions).

Two lines are **parallel** when they lie in the same flat surface and never meet. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#points-lines-and-angles), [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#a-line-crossing-two-lines) and [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#definitions).

A **parallelogram** is a four-sided shape with two pairs of parallel sides, like a rectangle pushed over sideways. Every square is a rectangle, and every rectangle is a parallelogram. Its area is base times height. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#polygons).

A **parent function** is the basic function, such as $x^2$ or $\lvert x \rvert$, from which $g(x) = a f(b(x - h)) + k$ is built by shifting, stretching and reflecting. Taught in [transformations of functions](../03-high-school/03-functions/04-transformations-of-functions.md#definitions).

A **partial function** from $A$ to $B$ is a relation in which each $a \in A$ has at most one output, so it satisfies uniqueness and may fail existence. Division is a partial function on $\mathbb{R} \times \mathbb{R}$, with no output when the divisor is 0. Taught in [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#partial-functions).

A **partial order** on a set is a relation $\preceq$ that is reflexive, antisymmetric and transitive, and a set with a partial order is a partially ordered set, or poset. It may leave some pairs incomparable: under divisibility, 2 and 3 are incomparable. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#partial-orders).

A **partial product** is one piece of a product whose factors are split by place value, such as $47 \times 30 = 1{,}410$ in $47 \times 36$. The product is the sum of its partial products. The area model draws them as the boxes of a rectangle, and the column method writes one row for each digit of the bottom factor. Taught in [multi-digit multiplication](../01-elementary/05-multi-digit-multiplication.md#definitions).

A **partition** of a set is a collection of non-empty, pairwise disjoint subsets, called its blocks, whose union is the whole set, so that every element is in exactly one block. Every equivalence relation gives a partition into its classes, and every partition gives an equivalence relation. Taught in [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#partitions).

**Pascal's rule** says that $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$, which is the rule for building each row of Pascal's triangle from the one above. Taught in [the binomial theorem](../03-high-school/11-sequences-series-and-counting/04-binomial-theorem.md#pascals-rule).

**Pascal's triangle** is the triangular array whose row $n$ lists $\binom{n}{0}, \binom{n}{1}, \dots, \binom{n}{n}$. It has 1s down both sides, and each other entry is the sum of the two above it. Rows and positions both start at 0. Taught in [the binomial theorem](../03-high-school/11-sequences-series-and-counting/04-binomial-theorem.md#definitions).

A **percent** is a ratio written per hundred: $x\%$ means $\frac{x}{100}$. So 35% is $0.35$, and 113% is $1.13$. In "the part is $x\%$ of the whole", the whole is the amount that counts as 100%, usually the noun right after "of", and $\text{part} = \frac{x}{100} \times \text{whole}$. Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md#definitions).

The **percent change** from an old value to a new one is $\frac{\text{new} - \text{old}}{\text{old}} \times 100\%$, the change measured against where you started. From \$1,600 to \$1,720 it is $\frac{120}{1600} = 7.5\%$. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions).

A **percentage point** is the unit for the plain difference between two percents. A rate that goes from 4% to 5% has risen by 1 percentage point, which is a percent change of 25%. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#percent-change-or-percentage-points) and percent change vs percentage points<!-- link: ../07-economics-math/01-measuring-the-economy/02-percent-change-vs-percentage-points.md -->.

A **perfect-square trinomial** has the form $a^2 \pm 2ab + b^2$ and factors as $(a \pm b)^2$. Taught in [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#the-factoring-identities).

The **perimeter** of a polygon is the total length of its sides, the distance once around it. A rectangle of length $l$ and width $w$ has perimeter $2l + 2w$. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#perimeter-area-and-volume).

A function is **periodic** when $f(x + p) = f(x)$ for every $x$, and the smallest such positive $p$ is its period. The period of $\sin(Bx)$ is $\frac{2\pi}{B}$. Taught in [graphs of trig functions](../03-high-school/09-trigonometry/03-graphs-of-trig-functions.md#definitions).

A **permutation** of $k$ items chosen from $n$ different items is an ordered list of $k$ of them, and there are $P(n, k) = \frac{n!}{(n-k)!}$ of them. Order matters, as in the gold, silver and bronze places of a race. Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md#definitions).

Two lines are **perpendicular** when they meet at a right angle, $90^\circ$. In the coordinate plane, two non-vertical lines are perpendicular exactly when their slopes multiply to $-1$. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#points-lines-and-angles) and [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md#definitions).

The **pH** of a solution is $-\log_{10}[\text{H}^+]$, where $[\text{H}^+]$ is the concentration of hydrogen ions in moles per litre. A drop of one pH unit means ten times the concentration. Taught in [logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md#log-scales).

The **phase shift** of a sinusoidal function is the horizontal shift of the curve. Factor out $B$ first: $\sin(2x - \pi)$ is shifted by $\frac{\pi}{2}$, not by $\pi$. Taught in [graphs of trig functions](../03-high-school/09-trigonometry/03-graphs-of-trig-functions.md#definitions).

The number **pi**, written $\pi$, is the circumference of a circle divided by its diameter. It is the same for every circle, about 3.14159, and it is irrational. Taught in [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md#circles).

A **piecewise function** uses different formulas on different, non-overlapping pieces of its domain. Exactly one piece owns each break point, where one piece ends and the next begins. Taught in [piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md#definitions).

The **pigeonhole principle** says that if more than $n$ objects are placed in $n$ boxes, some box holds two. Equivalently, if $A$ and $B$ are finite sets with $\lvert A \rvert > \lvert B \rvert$, no function from $A$ to $B$ is injective. Taught in [injective, surjective and bijective](../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md#theorems).

The **place value** of a position in a number is what one unit in that position is worth. In base 10 the places are worth 1, 10, 100 and so on from the right, each 10 times the place to its right, and after the decimal point they are worth tenths, hundredths and so on. A digit's value is the digit times its place value, so the 4 in 2,436 is worth 400. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions) and [decimals: place value, adding and subtracting](../01-elementary/12-decimals-place-value-and-adding.md#definitions).

The **point-slope form** of the line through $(x_1, y_1)$ with slope $m$ is $y - y_1 = m(x - x_1)$. Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#point-slope-form) and [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md#definitions).

A **polygon** is a closed flat shape made of straight line segments, called its sides, that meet only at their endpoints. A regular polygon has all its sides the same length and all its angles the same size, as a stop sign does. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#polygons).

A **polynomial** is a sum of monomials. The monomials are its terms, and it is in standard form when like terms are combined and the terms run from the highest power to the lowest. Taught in [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md#definitions).

A **postulate** is a statement in geometry accepted without proof, the same thing as an axiom. A theorem is then proved from definitions, postulates and earlier theorems. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#postulates-and-theorems).

A **power** of a number $b$ is $b^n$, the product of $n$ copies of the base $b$, read "$b$ to the power $n$". The powers of ten are $10^1 = 10$, $10^2 = 100$ and so on, and the pattern continues down to $10^0 = 1$ and $10^{-1} = 0.1$. Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#definitions) and [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).

The **power rule** says that $\frac{d}{dx}\left(x^n\right) = n x^{n-1}$. It is proved for positive integers $n$ with the binomial theorem, and it also holds for negative integers and then for every real exponent. Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#the-power-rule).

The **power set** $\mathcal{P}(A)$ of a set $A$ is the set of all subsets of $A$, including $\emptyset$ and $A$ itself. A set with $n$ elements has $2^n$ subsets, and for $A = \{1, 2\}$ the power set is $\{\emptyset, \{1\}, \{2\}, \{1, 2\}\}$. Taught in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#power-sets) and [proofs about sets](../04-proofs-and-logic/04-more-proof-methods/03-proofs-about-sets.md#definitions).

The **preimage** of a set $T \subseteq B$ under a function $f \colon A \to B$ is the set of inputs whose output lands in $T$. It always exists, even when $f$ has no inverse function: for $f(x) = x^2$ on $\mathbb{R}$, the preimage of $\{4\}$ is $\{-2, 2\}$. Taught in [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#image-and-preimage-of-a-set).

A **preorder** is a relation that is reflexive and transitive but not necessarily antisymmetric, so two different elements can each be below the other, as with "grows at most as fast as" for functions. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#what-if-the-relation-is-reflexive-and-transitive-but-not-antisymmetric).

A **prime** number is an integer greater than 1 whose only positive factors are 1 and itself, such as $2, 3, 5, 7$ and $11$. The number 1 is not prime, and proofs state "$p > 1$" as part of the definition. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md), [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#five-working-definitions) and primes and unique factorization<!-- link: ../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md -->.

A **prime factorization** of a number writes it as a product of primes, with repeated factors grouped by exponents: $360 = 2^3 \times 3^2 \times 5$. By the fundamental theorem of arithmetic, every whole number greater than 1 has exactly one, apart from the order. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions).

A **prism** is a solid with two parallel, congruent polygons as bases and flat rectangular or parallelogram sides. Its volume is the base area times the height, $V = Bh$. Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#definitions).

The **probability** of an event $A$, written $P(A)$, is a number from 0 to 1 that measures how likely $A$ is. For equally likely outcomes it is the number of outcomes in $A$ divided by the number in the sample space. Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#definitions).

The **product rule** says that if a procedure has $k$ stages and stage $i$ can be done in $n_i$ ways whatever happened earlier, the whole procedure can be done in $n_1 n_2 \cdots n_k$ ways. A set with $n$ elements has $2^n$ subsets. In calculus, the product rule for derivatives is $(fg)' = f'g + fg'$, which is not $f'g'$. Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md#definitions) and, for derivatives, [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#the-product-rule).

A **progressive tax** charges a higher rate on each higher bracket of income. Taught in [piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md#definitions).

A **proof** is an argument that shows a statement is true, where each step follows from definitions, axioms, the hypotheses or results proved earlier. Checking many examples is not a proof. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#two-column-and-paragraph-proofs) and [what is a proof](../04-proofs-and-logic/01-language-and-notation/01-what-is-a-proof.md).

A **proof by cases** of a statement $Q$ chooses cases $C_1, \dots, C_k$, shows that at least one of them must hold, and shows that each one gives $Q$. The cases must be exhaustive, and it helps if they don't overlap. Taught in [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md#definitions).

A **proof by contradiction** of a statement $S$ assumes that $S$ is false and derives a contradiction, then concludes that $S$ is true. For a conditional "if $P$, then $Q$", the proof assumes $P$ and not $Q$. Taught in [proof by contradiction](../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md#definitions).

A **proof by contrapositive** of "if $P$, then $Q$" is a direct proof of "if not $Q$, then not $P$": it starts from "$Q$ is false" and walks to "$P$ is false". Its first line must negate the conclusion. Taught in [contrapositive proof](../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md#definitions).

A **proper subset** of $B$ is a subset $A$ of $B$ that is not equal to $B$, written $A \subsetneq B$. This book avoids the symbol $\subset$, because books disagree on whether it means $\subseteq$ or $\subsetneq$. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#sets-and-set-notation).

A **proportion** is an equation stating that two ratios are equal, $\frac{a}{b} = \frac{c}{d}$ with $b \ne 0$ and $d \ne 0$, read "$a$ is to $b$ as $c$ is to $d$". Cross-multiplying turns it into $ad = bc$. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#definitions).

Two quantities $x$ and $y$ are **proportional**, or directly proportional, when $y = kx$ for a nonzero constant $k$. Then $y$ is always the same multiple of $x$, and zero of one goes with zero of the other, so a taxi fare with a fixed base charge is not proportional to the distance. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#definitions).

A **proposition** is, in logic, a statement that is either true or false but not both. In a text it is a proved result, usually smaller or more specific than a theorem. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#statements) and [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#definitions).

A **pyramid** is a solid with a polygon for its base and triangular faces that meet at a point called the apex. Its volume is $\frac{1}{3}Bh$. Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#definitions).

The **Pythagorean identity** is $\sin^2\theta + \cos^2\theta = 1$, true for every angle $\theta$. It is the equation of the unit circle. Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#definitions).

The **Pythagorean theorem** says that in a right triangle with legs $a$ and $b$ and hypotenuse $c$, $a^2 + b^2 = c^2$. The converse also holds: if $a^2 + b^2 = c^2$, the angle opposite $c$ is a right angle. Taught in [the Pythagorean theorem](../02-middle-school/06-geometry/04-pythagorean-theorem.md#definitions).

A **Pythagorean triple** is a set of three positive integers with $a^2 + b^2 = c^2$, such as 3, 4, 5 and 5, 12, 13. Taught in [the Pythagorean theorem](../02-middle-school/06-geometry/04-pythagorean-theorem.md#definitions).

## Q

The four **quadrants** are the regions the axes cut the plane into, numbered I to IV counterclockwise from the top right. A point on an axis is in no quadrant. Taught in [the coordinate plane](../02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md#definitions).

A **quadratic equation** is an equation that can be written $ax^2 + bx + c = 0$ with $a \ne 0$. It is solved by factoring, by taking square roots, by completing the square or by the quadratic formula. Taught in [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md#definitions).

The **quadratic formula** gives the solutions of $ax^2 + bx + c = 0$ as $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$. Taught in [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md#definitions).

A **quadratic function** is a function $f(x) = ax^2 + bx + c$ with $a \ne 0$. Its graph is a parabola. Taught in [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#definitions).

A **quantifier** says how many elements a statement is about. "For every" ($\forall$) claims the statement for each element of a set, and "there exists" ($\exists$) claims it for at least one. Taught in [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md).

The **quartiles** of a sorted data set are the medians of its lower and upper halves, written $Q_1$ and $Q_3$, with the overall median left out of both halves when the number of values is odd. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

The **quotient** is the result of a division. In division with a remainder, $n = qd + r$, it is the whole number $q$ of times that $d$ fits into $n$. Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and [long division](../01-elementary/07-long-division.md).

The **quotient rule** says that $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$ when $g(x) \ne 0$: the derivative of the top times the bottom, minus the top times the derivative of the bottom, over the bottom squared. Swapping the order in the numerator flips the sign. Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#the-reciprocal-and-quotient-rules).

## R

A **radian** is the angle at the centre of a circle that cuts off an arc equal in length to the radius. A half turn is $\pi$ radians, so $180^\circ = \pi$ rad, and an arc of angle $\theta$ radians has length $r\theta$. Taught in [radians and the unit circle](../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md#definitions).

A **radical equation** is an equation with the unknown under a root. Isolate the radical, raise both sides to the index, and check every answer in the original equation. Taught in [rational and radical equations](../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md#definitions).

A **random variable** is a number whose value depends on the outcome of a random experiment, such as the total of two dice. Formally it is a function from the sample space to $\mathbb{R}$; the details are in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md -->.

The **range** of a function is the set of outputs that actually occur, $\{f(a) : a \in A\}$, also called the image. Some books use "range" to mean the codomain, so check which one is meant. In statistics, the range of a data set is its largest value minus its smallest. Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#definitions), [what is a function](../03-high-school/03-functions/01-what-is-a-function.md#definitions) and [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md#functions-as-sets-of-pairs).

A **rate** is a ratio of two quantities with different units, such as 90 km per hour or \$18 per hour. A unit rate gives the amount for one unit of the second quantity, and a unit price is the price for a fixed amount, such as per kilogram or per 100 g. Taught in [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions).

A **rate of change** is a slope with units: units of $y$ per unit of $x$, such as \$2.50 per kilometre for a taxi fare. Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#definitions).

A **ratio** compares two quantities by division. A recipe with 2 cups of flour for every 3 cups of milk has a flour-to-milk ratio of $2 : 3$, which is the fraction $\frac{2}{3}$. The numbers 2 and 3 are the terms of the ratio, and their order matters. That ratio is part-to-part, since it compares two parts of the mix; the part-to-whole ratio of flour to mix is $2 : 5$, so flour is $\frac{2}{5}$ of the mix. Taught in [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions).

A **rational** number is one that can be written as a fraction $\frac{a}{b}$ of integers with $b \ne 0$, such as $-\frac{9}{20}$ or $7 = \frac{7}{1}$. The set of rational numbers is $\mathbb{Q}$. Every decimal that ends or repeats is rational: $0.75 = \frac{3}{4}$ and $0.333\ldots = \frac{1}{3}$. In a proof, $r$ is rational when $r = \frac{a}{b}$ for some integers $a$ and $b$ with $b \ne 0$, and one such fraction is enough. Formally, a rational number is an equivalence class of fractions. Taught in [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#definitions), [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md), [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md#five-working-definitions) and [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#the-rational-numbers-as-classes-of-fractions).

A **rational equation** is an equation with the unknown in a denominator. Multiply every term by the least common denominator, solve, and reject any answer that is an excluded value. Taught in [rational and radical equations](../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md#definitions).

A **rational exponent** is a fractional exponent: $a^{m/n} = \left(\sqrt[n]{a}\right)^m$ for $a > 0$. So $8^{2/3} = 2^2 = 4$, and the denominator of the exponent is the index of the root. Taught in [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md#definitions).

A **rational expression** is a fraction $\frac{p(x)}{q(x)}$ of two polynomials, with $q$ not the zero polynomial. Taught in [rational expressions](../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md#definitions).

A **rational function** is a function $f(x) = \frac{p(x)}{q(x)}$ given by a rational expression, with domain every $x$ where $q(x) \ne 0$. Taught in [rational functions and asymptotes](../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md#definitions).

The **rational root theorem** says that if a polynomial with integer coefficients has a rational zero $\frac{r}{s}$ in lowest terms, then $r$ divides the constant term and $s$ divides the leading coefficient. It lists candidates; each one still has to be tested. Taught in [polynomial division and the remainder theorem](../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md#the-rational-root-theorem).

**Rationalizing the denominator** means multiplying the top and bottom of a fraction by a factor that removes the radical from the denominator: $\frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}$. A denominator such as $2 + \sqrt{3}$ is cleared by multiplying by its conjugate. Taught in [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md#definitions).

A **real number** is a point on the number line, rational or irrational. The set of real numbers is $\mathbb{R}$. Its formal properties are in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md).

The **reciprocal** of a nonzero number $a$ is $\frac{1}{a}$, the number you multiply $a$ by to get 1. It is also called the multiplicative inverse. The reciprocal of $\frac{2}{3}$ is $\frac{3}{2}$, and 0 has no reciprocal. Taught in [multiplying and dividing fractions](../01-elementary/11-multiplying-and-dividing-fractions.md#definitions).

The **reciprocal rule** says that if $g$ is differentiable at $x$ and $g(x) \ne 0$, then $\left(\frac{1}{g}\right)' = -\frac{g'}{g^2}$. With the product rule it gives the quotient rule, and with $g = x^n$ it extends the power rule to negative integers. Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#the-reciprocal-and-quotient-rules).

The **reciprocal trig functions** are cosecant, $\csc\theta = \frac{1}{\sin\theta}$, secant, $\sec\theta = \frac{1}{\cos\theta}$, and cotangent, $\cot\theta = \frac{1}{\tan\theta}$. Taught in [trig identities and inverse trig](../03-high-school/09-trigonometry/04-trig-identities-and-inverse-trig.md#definitions).

A **recurrence relation** gives each term of a sequence from earlier ones, and it comes with initial conditions that fix the starting terms: $a_0 = 100$ and $a_{n+1} = 1.02\,a_n$. A rule that looks back two terms needs two initial conditions. Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md#definitions).

**Recursion** defines something in terms of smaller versions of itself, together with a starting case. The factorial is defined recursively: $0! = 1$, and $n! = n \cdot (n - 1)!$ for $n \ge 1$. Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md) and [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md).

A **recursive definition** of a set has three parts: a basis that names some elements outright, recursive clauses that build new elements from elements already in the set, and a closure clause that says nothing else is in the set. Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#definitions).

The **reference angle** of an angle is the acute angle between its terminal side and the $x$-axis. The trigonometric ratios of the angle equal those of its reference angle, up to sign. Taught in [radians and the unit circle](../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md#definitions).

A **reflection** is a mirror image across a line: each point goes to the point the same distance on the other side of the line, along a path at right angles to it. Reflecting in the $x$-axis sends $(x, y)$ to $(x, -y)$. Taught in [the coordinate plane](../02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md#definitions), [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#the-four-transformations) and [transformations of functions](../03-high-school/03-functions/04-transformations-of-functions.md#definitions).

A relation $R$ on a set $A$ is **reflexive** if $a \mathrel{R} a$ for every $a \in A$, so every element is related to itself and every vertex of the digraph has a loop. Whether a rule is reflexive depends on the set: "$xy \ge 0$" is reflexive on $\mathbb{R}$, while "$xy > 0$" fails at $x = 0$. Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#the-four-properties).

**Regrouping** is the step in column arithmetic that changes how a number is split among its places without changing the number, as in 52 = 5 tens + 2 ones = 4 tens + 12 ones. In addition it is called carrying, when a column adds up to 10 or more, and in subtraction it is called borrowing, when a top digit is too small. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions).

A **relation** from a set $A$ to a set $B$ is a subset $R$ of $A \times B$, and a relation on $A$ is a subset of $A \times A$. We write $a \mathrel{R} b$ when $(a, b) \in R$. A function is a relation in which every input has exactly one output. Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#relations).

A **relative frequency** is a count divided by a total. A row relative frequency divides each cell by its row total, and a column relative frequency divides by its column total, so the two answer different questions. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

Two integers are **relatively prime**, or coprime, when their greatest common factor is 1. The numbers 8 and 15 are relatively prime even though neither one is prime. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions).

The **remainder** is what is left over when a division doesn't come out even. In $n = qd + r$ it is $r$, and it always satisfies $0 \le r < d$. Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and [long division](../01-elementary/07-long-division.md).

The **remainder theorem** says that dividing a polynomial $p(x)$ by $x - c$ leaves the remainder $p(c)$. Taught in [polynomial division and the remainder theorem](../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md#definitions).

A **repeating decimal** has a block of one or more digits that, from some place on, repeats forever. The block is written once with a bar over it: $\frac{1}{3} = 0.\overline{3}$ and $\frac{7}{12} = 0.58\overline{3}$. The decimal of every fraction either terminates or repeats. Taught in [multiplying and dividing decimals](../01-elementary/13-multiplying-and-dividing-decimals.md#definitions) and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#terminating-and-repeating-decimals).

A **representative** of an equivalence class is an element chosen to name the class. A class has many representatives: if $[a] = [b]$, either one can name it. Taught in [equivalence relations and partitions](../04-proofs-and-logic/06-relations-and-functions/02-equivalence-relations-and-partitions.md#equivalence-classes).

A step in a calculation is **reversible** when the new line implies the old line as well as the other way round. A chain of reversible steps proves an if-and-only-if statement, and squaring both sides is not reversible. Taught in [if and only if proofs](../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md#definitions) and [scratch work and proof strategies](../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md#definitions).

A **rigid motion**, or isometry, is a transformation that preserves distances and angles: a translation, a rotation, a reflection, or a combination of them. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#definitions).

A proof is **rigorous** when every step can be justified by a definition, an axiom or a result already established, with no step resting on a picture, a pattern or a feeling that it must be true. Taught in [what is a proof](../04-proofs-and-logic/01-language-and-notation/01-what-is-a-proof.md#definitions).

A **rotation** turns every point through the same angle about a fixed point. A $90^\circ$ counterclockwise turn about the origin sends $(x, y)$ to $(-y, x)$. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#the-four-transformations).

To **round** a number to a given place is to replace it with the nearest number that has only zeros to the right of that place, so 2,436 rounded to the nearest hundred is 2,400. This book rounds an exact half up. Python's `round` uses round half to even instead, also called banker's rounding, so it sends 2,450 to 2,400 and 2,550 to 2,600. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

The **rule of 72** says that a quantity growing at $R$ percent per period doubles in about $\frac{72}{R}$ periods. At 6% per year, money doubles in about 12 years. Taught in [exponential and logarithmic equations](../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md#the-rule-of-72) and doubling time, the rule of 72 and logs<!-- link: ../08-financial-math/02-interest-and-growth/05-doubling-time-rule-of-72-and-logs.md -->.

## S

The **sample space** of an experiment is the set of all its possible outcomes, written $S$ in school books and $\Omega$ in university ones. An outcome is one result of the experiment. Taught in [basic probability](../02-middle-school/07-statistics-and-probability/02-basic-probability.md#definitions).

A **sanity check** is a quick test of whether an answer is plausible, by looking at its units, its sign and its size. A negative length or a speed of 5,000 km/h for a car fails it. Taught in [estimation and sanity checks](../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md#definitions).

A compound statement is **satisfiable** if at least one row of its truth table makes it true. Tautologies are satisfiable, and contradictions are not. Taught in [truth tables and logical equivalence](../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md#satisfiability-briefly).

A **scalar** is a plain number, used to scale a vector or a matrix. The scalar multiple $c\mathbf{v}$ of $\mathbf{v} = (a, b)$ is $(ca, cb)$, which points the same way when $c > 0$ and the opposite way when $c < 0$. Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md#definitions).

A **scale drawing** is a drawing in which every length is the same multiple of the matching real length, and its scale is the ratio of a length in the drawing to the real length. A map scale of $1:50{,}000$ means that 1 cm on the map stands for 50,000 cm, or 0.5 km, on the ground. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#definitions).

A **scale factor** is the number by which every length is multiplied in a dilation, a scale drawing or a pair of similar figures. Areas change by $k^2$ and volumes by $k^3$. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#definitions) and [similarity](../03-high-school/08-geometry-and-proof/03-similarity.md#definitions).

A **scatter plot** draws pairs of values as points, with the explanatory variable on the horizontal axis and the response variable on the vertical axis. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

A number is in **scientific notation** when it is written as $a \times 10^n$ with $1 \le \lvert a \rvert < 10$ and $n$ an integer, as in $93{,}000{,}000 = 9.3 \times 10^7$. Programs write the same thing as `9.3e7`, which is called E notation. In engineering notation the exponent is a multiple of 3, to match the metric prefixes. Taught in [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md#definitions).

**Scratch work** is the informal work done to find a proof: examples, pictures, false starts and shorthand. It is for you and can be messy, and it is not the proof. Taught in [scratch work and proof strategies](../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md#definitions).

A **secant line** is a line through two points of a graph. Its slope is the average rate of change between them. Taught in [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions).

The **second derivative** of $f$ is the derivative of the derivative, written $f''(x)$ or $\frac{d^2 y}{dx^2}$: the rate of change of the rate of change. The $n$-th derivative $f^{(n)}$ is found by differentiating $n$ times. Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#definitions).

A **sector** is the region of a circle between two radii and the arc they cut off. Its area is $\frac{\theta}{360} \cdot \pi r^2$. Taught in [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md#arcs-and-sectors).

A **sequence** is an ordered list of numbers $a_1, a_2, a_3, \dots$, finite or infinite. Formally it is a function whose domain is a set of natural numbers. Taught in [sequences and recursion](../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md).

A **series** is the sum of the terms of a sequence, such as $1 + \frac{1}{2} + \frac{1}{4} + \dots$. An infinite series has a value only when its partial sums approach a limit, and this one approaches 2. Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md) and [infinite series basics](../05-university-core/05-sequences-and-series/02-infinite-series-basics.md).

A **set** is a collection of distinct objects, called its elements, in which order and repeats don't matter. Most of university math is built on sets. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#sets-and-set-notation) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md).

The **set difference** $A \setminus B$ is the set of elements of $A$ that are not in $B$. It is not symmetric: $A \setminus B$ and $B \setminus A$ are usually different. Taught in [compound inequalities and interval notation](../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md#definitions) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#the-four-operations).

**Set-builder notation** describes a set by a condition: $\{x \in \mathbb{Z} : x^2 = 4\}$ is "the set of all integers $x$ such that $x^2 = 4$", which is $\{-2, 2\}$. Some books write a vertical bar instead of the colon. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#sets-and-set-notation).

The **sieve of Eratosthenes** finds every prime up to a limit. Write the numbers from 2 up to the limit, then again and again circle the first number that is not yet circled or crossed out, and cross out its multiples, starting from its square. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#the-sieve-of-eratosthenes).

A **sign chart** is a number line marked at the critical numbers, showing the sign of each factor, and so of the whole expression, on each interval. Taught in [polynomial and rational inequalities](../03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md#definitions).

The **sign rules** give the sign of a product or quotient of two nonzero numbers: the same signs give a positive answer, and different signs give a negative one. So $(-3) \times (-4) = 12$ and $(-12) \div 4 = -3$. They are rules for multiplication and division only, and $-3 + (-5)$ is $-8$. Taught in [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#definitions).

The **significant figures** of a measurement are the digits of its coefficient in scientific notation. They show how precisely the value is known: $4.50 \times 10^{-3}$ has three significant figures, and $4.5 \times 10^{-3}$ has two. Taught in [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md#definitions).

Two figures are **similar** when one can be carried onto the other by rigid motions and a dilation, so they have the same shape and possibly different sizes. Corresponding angles are equal and corresponding sides are in the same ratio. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#congruence-and-similarity) and [similarity](../03-high-school/08-geometry-and-proof/03-similarity.md#definitions).

**Simple interest** is interest paid only on the amount first borrowed or saved, called the principal. A principal $P$ at an annual rate $r$ for $t$ years earns $I = Prt$, so \$2,000 at 4% earns \$80 a year. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions) and simple interest<!-- link: ../08-financial-math/02-interest-and-growth/01-simple-interest.md -->.

A fraction is in **simplest form**, or lowest terms, when its numerator and denominator have no common factor other than 1, as in $\frac{3}{4}$. A ratio is in simplest form when its terms are whole numbers with no common factor other than 1, as in $2:5$. For a negative rational number, simplest form keeps the denominator positive: $-\frac{3}{4}$, not $\frac{3}{-4}$. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions), [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions) and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#where-the-minus-sign-goes).

A radical is in **simplest radical form** when no factor of the radicand is a perfect power of the index and no root is left in a denominator. So $\sqrt{180} = 6\sqrt{5}$, since $180 = 36 \times 5$. Taught in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#rules-for-products-and-quotients) and [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md#definitions).

To **simplify** an expression is to rewrite it as an equivalent expression with no brackets left to expand and no like terms left to combine: $3(x + 4) - 2x$ simplifies to $x + 12$. Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#definitions).

The **sine** of an acute angle in a right triangle is the opposite side divided by the hypotenuse. For any angle $\theta$, it is the $y$-coordinate of the point at angle $\theta$ on the unit circle. Taught in [right triangle trigonometry](../03-high-school/09-trigonometry/01-right-triangle-trigonometry.md#definitions) and [radians and the unit circle](../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md#definitions).

A **sinusoidal function** is a sine or cosine curve that has been shifted and stretched, $y = A\sin(B(x - C)) + D$. Its midline is $y = D$, its amplitude is $\lvert A \rvert$, its phase shift is $C$ and its frequency is $\frac{B}{2\pi}$ cycles per unit of $x$. Taught in [graphs of trig functions](../03-high-school/09-trigonometry/03-graphs-of-trig-functions.md#definitions).

The **skeleton** of a proof is its claim, its method, its assumptions and its final line, with the middle left out. For Euclid's proof it is "assume the opposite, build a number $N$, show $N$ has a prime divisor, derive that it divides 1". Taught in [how to read a proof](../04-proofs-and-logic/03-core-proof-methods/02-how-to-read-a-proof.md#definitions).

A data set is **skewed** right when it has a long tail of large values, as incomes do, and skewed left when the long tail is on the small side. In a right-skewed set the mean is usually larger than the median. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

A **slant asymptote** is a line $y = mx + b$ with $m \ne 0$ that a graph approaches. A rational function has one when the numerator's degree is exactly one more than the denominator's, and polynomial division finds it. Taught in [rational functions and asymptotes](../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md#definitions).

The **slant height** of a cone or a pyramid is the distance from the apex down a side face to the edge of the base. It is used for surface area, and the volume uses the perpendicular height instead. Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#definitions).

The **slope** of a line through $(x_1, y_1)$ and $(x_2, y_2)$ is $\frac{y_2 - y_1}{x_2 - x_1}$, the rise over the run. Horizontal lines have slope 0, and vertical lines have no slope, because the run is 0. Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#definitions).

The **slope-intercept form** of a line is $y = mx + b$, where $m$ is the slope and $b$ is the $y$-intercept. Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md#definitions).

A **smallest counterexample** argument uses the well-ordering principle: suppose some $n$ makes $P(n)$ false, take the least such $m$, and show that $m$ cannot exist. Taught in [strong induction and well-ordering](../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md#definitions).

A **solution** of an equation or inequality in one variable is a value of the variable that makes it true. The solution set is the set of all solutions, and to solve is to find all of them: $3x + 2 = 14$ has the solution set $\{4\}$. Taught in [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#definitions) and [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#definitions).

The **span** of a set of vectors is the set of all their linear combinations. Two vectors in $\mathbb{R}^3$ that don't lie on the same line through the origin span a plane through the origin. Taught in vectors, dot product and span<!-- link: ../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md -->.

The **special products** are the identities $(a + b)^2 = a^2 + 2ab + b^2$, $(a - b)^2 = a^2 - 2ab + b^2$ and $(a + b)(a - b) = a^2 - b^2$. Read from right to left, they are factoring patterns. Taught in [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md#definitions).

A **sphere** is the set of all points in space at a fixed distance $r$ from a centre. Its volume is $\frac{4}{3}\pi r^3$ and its surface area is $4\pi r^2$. Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#definitions).

The **square** of a number $b$ is $b^2 = b \times b$, read "$b$ squared", after the area of a square. A perfect square, or square number, is the square of an integer, such as $49 = 7^2$, and it is never negative. As a shape, a square is a rectangle whose four sides are all the same length. Taught in [multiplication and times tables](../01-elementary/03-multiplication-and-times-tables.md#definitions), [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#definitions) and [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#polygons).

A **square root** of a number $a$ is a number whose square is $a$. For $a \ge 0$, the symbol $\sqrt{a}$ means the principal square root, the non-negative one, so $\sqrt{9} = 3$, while the equation $x^2 = 9$ has the two solutions $3$ and $-3$. Taught in [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md#square-roots-and-cube-roots).

The **squeeze theorem** says that if $g(x) \le f(x) \le h(x)$ near $a$, and $g$ and $h$ have the same limit $L$ at $a$, then $f$ has limit $L$ too. It is used to show that $\lim_{x \to 0} \frac{\sin x}{x} = 1$. Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#definitions).

The **SSS, SAS and ASA** postulates are the three tests accepted without proof for congruent triangles: three sides, two sides and the included angle, or two angles and the included side. AAS and HL are proved from them. SSA is not a test, because a circle can meet a ray twice. Taught in [congruence and triangle proofs](../03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md#the-postulates).

The **standard form** of a linear equation is $Ax + By = C$, with integer coefficients that have no common factor and $A \ge 0$. A polynomial is in standard form when its like terms are combined and its terms run from the highest power down, and a quadratic function in standard form is $ax^2 + bx + c$. Taught in [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md#definitions), [polynomial arithmetic](../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md#definitions) and [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#definitions).

An angle is in **standard position** when its vertex is at the origin and its initial side is on the positive $x$-axis. Angles with the same terminal side are coterminal and differ by whole turns. Taught in [radians and the unit circle](../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md#definitions).

A **statement**, or proposition, is a sentence that is either true or false. "7 is prime" is a statement, while "$x > 3$" is not one until you know $x$. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md).

A **step function** is a piecewise function that is constant on each of its pieces, so its graph looks like stairs. Floor, ceiling and parking tariffs are examples. Taught in [piecewise, absolute value and step functions](../03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md#definitions).

A **strict inequality** uses $<$ or $>$, so equality is left out: $5 < 5$ is false, while $5 \le 5$ is true. On a number line, the boundary of a strict inequality is drawn as an open dot, and the boundary of a non-strict one, with $\le$ or $\ge$, as a closed dot. Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#definitions).

The **strict order** that goes with a partial order $\preceq$ is $a \prec b$, meaning $a \preceq b$ and $a \ne b$, like $<$ for $\le$. A strict order is irreflexive and transitive. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#strict-orders).

A **string** over an alphabet $\Sigma$, a finite set of symbols, is built recursively: the empty string $\varepsilon$ is a string, and if $w$ is a string and $a$ is a symbol then $wa$ is a string. The length is $\lvert \varepsilon \rvert = 0$ and $\lvert wa \rvert = \lvert w \rvert + 1$. Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#definitions).

**Strong induction** proves $P(n)$ for every integer $n$ from the first value on by assuming $P$ for all earlier cases back to the first value and proving it for the next. It proves the same statements as ordinary induction, and it needs as many base cases as the step reaches back. Taught in [strong induction and well-ordering](../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md#definitions).

**Structural induction** proves a property of every element of a recursively defined set: prove it for the basis elements, then prove that each recursive clause preserves it, assuming it for the parts and proving it for the new object. Taught in [recursive definitions and structural induction](../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md#definitions).

A set $A$ is a **subset** of a set $B$, written $A \subseteq B$, when every element of $A$ is also in $B$. Every set is a subset of itself, and $\emptyset$ is a subset of every set. Taught in [real numbers, axioms and set notation](../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md#sets-and-set-notation), [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#sets-equality-and-subsets) and [proofs about sets](../04-proofs-and-logic/04-more-proof-methods/03-proofs-about-sets.md#definitions), where $A = B$ is proved as $A \subseteq B$ and $B \subseteq A$.

**Substitution** solves a system by solving one equation for one unknown and putting that expression into the other equation. Taught in [systems of linear equations](../02-middle-school/05-linear-relationships-and-functions/04-systems-of-linear-equations.md#solving-by-substitution).

A condition P is **sufficient** for Q when P guarantees Q, which is the statement "if P, then Q". Being divisible by 4 is sufficient for being even. Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md).

The **sum rule** says that if a task can be done in one of several ways and no outcome comes from two of the ways, the number of outcomes is the sum of the counts for each way. In calculus, the sum rule for derivatives is $(f \pm g)' = f' \pm g'$. Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md#definitions).

**Summation** notation writes a long sum compactly: $\sum_{i=1}^{n} a_i$ means $a_1 + a_2 + \dots + a_n$. Also called sigma notation. Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#definitions).

Two angles are **supplementary** when their measures add to $180^\circ$. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#pairs-of-angles).

The **surface area** of a solid is the total area of its outer faces, measured in square units. Taught in [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md#definitions).

A function $f \colon A \to B$ is **surjective**, or onto, when every element of $B$ is the output of at least one input, so the range equals the codomain. The squaring function from $\mathbb{R}$ to $\mathbb{R}$ is not surjective, since no real number squares to $-1$. Taught in [injective, surjective and bijective](../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md).

**Symbol soup** is a string of formulas joined by arrows or equals signs, with few or no words, so that the reader must guess how each formula follows from the last. The arrow $\Rightarrow$ means "implies", not "and then". Taught in [how to write a proof](../04-proofs-and-logic/03-core-proof-methods/07-how-to-write-a-proof.md#definitions).

A relation is **symmetric** if $b \mathrel{R} a$ whenever $a \mathrel{R} b$, so every arrow of its digraph has an arrow coming back. A statement about $a$ and $b$ is also called symmetric in $a$ and $b$ when swapping the names gives the same statement, which is what WLOG needs. Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#the-four-properties) and [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md#definitions).

**Synthetic division** divides a polynomial by $x - c$ using only its coefficients, and it is the same arithmetic as Horner's method. The number to use is $c$, so dividing by $x + 2$ uses $c = -2$. Taught in [polynomial division and the remainder theorem](../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md#how-to-do-it).

A **system of linear equations** is two or more linear equations in the same unknowns, solved together. A solution is a set of values that makes every equation true at once; with two unknowns it is a point on both lines. Taught in [systems of linear equations](../02-middle-school/05-linear-relationships-and-functions/04-systems-of-linear-equations.md#definitions) and [systems of linear equations](../03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md#definitions).

## T

The **tangent** of an angle is $\frac{\sin\theta}{\cos\theta}$. In a right triangle it is the opposite side divided by the adjacent side, which is the slope of the hypotenuse. The memory aid SOH CAH TOA covers all three ratios. Taught in [right triangle trigonometry](../03-high-school/09-trigonometry/01-right-triangle-trigonometry.md#definitions).

A **tangent line** to a circle is a line that meets the circle at exactly one point, and it is perpendicular to the radius drawn to that point. A secant is a line that meets the circle at two points. In calculus, the tangent line to the graph of $f$ at $(a, f(a))$ is the line through that point with slope $f'(a)$. The idea of touching at only one point works for circles and not in general: the line $y = 0$ crosses $y = x^3$ at the origin and is still its tangent there. Taught in [coordinate geometry and circles](../03-high-school/08-geometry-and-proof/04-coordinate-geometry-and-circles.md#circles) and [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#definitions).

A **tautology** is a compound statement that is true in every row of its truth table, whatever the truth values of its parts, such as $P \vee \neg P$. A statement that is true in some rows and false in others is called contingent. Taught in [truth tables and logical equivalence](../04-proofs-and-logic/02-logic-and-sets/03-truth-tables-and-logical-equivalence.md#tautologies-and-contradictions).

A **telescoping sum** is a sum in which consecutive terms cancel, leaving only the first and last pieces, as in $\sum_{k=1}^{n}\left(\frac{1}{k} - \frac{1}{k+1}\right) = 1 - \frac{1}{n+1}$. Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md#telescoping-and-the-sum-of-squares).

A **term** is one of the pieces added together in an expression: $3x^2 - 5x + 2$ has the three terms $3x^2$, $-5x$ and $2$. A term of a sequence is one of its entries. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md).

A **terminating decimal** has a finite number of decimal places, such as $\frac{7}{8} = 0.875$. A fraction in simplest form terminates exactly when its denominator has no prime factors other than 2 and 5. Taught in [multiplying and dividing decimals](../01-elementary/13-multiplying-and-dividing-decimals.md#definitions) and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#terminating-and-repeating-decimals).

A **test point** is a single point off the boundary line that you substitute into the inequality to find which side to shade. The origin is the usual choice, unless the line passes through it. Taught in [two-variable inequalities and feasible regions](../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#definitions).

**TFAE** is short for "the following are equivalent". A theorem that lists several conditions this way says that each one is equivalent to every other, so the conditions are interchangeable. Taught in [if and only if proofs](../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md#several-equivalent-statements).

A **theorem** is a statement that has been proved, usually one important enough to be named or used often. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#postulates-and-theorems) and [definitions, theorems, lemmas and corollaries](../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md).

The statement **there exists exactly one** $x$ in $D$ with $P(x)$, written $\exists!\, x \in D,\ P(x)$, claims two things at once: such an $x$ exists, and any two such elements are equal. Taught in [existence and uniqueness proofs](../04-proofs-and-logic/04-more-proof-methods/02-existence-and-uniqueness-proofs.md#exactly-one).

**Topological sorting** produces a linear extension of a finite partially ordered set from its dependencies: a list in which, whenever $a$ must come before $b$, it does. A schedule of tasks with prerequisites is an example. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#topological-sorting).

A partial order is a **total order** if every two elements are comparable, so it lines all the elements up in a single row. The relation $\le$ on $\mathbb{R}$ is total, and "divides" on the positive integers is not. Taught in [partial orders](../04-proofs-and-logic/06-relations-and-functions/03-partial-orders.md#partial-orders).

A **transformation** is a rule that moves every point of the plane to a new point. The new figure is called the image. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#definitions).

A relation is **transitive** if $a \mathrel{R} c$ whenever $a \mathrel{R} b$ and $b \mathrel{R} c$, so every two-step path has a shortcut. A relation with no two-step paths, such as $\{(1, 2), (3, 4)\}$, is transitive. Taught in [relations and their properties](../04-proofs-and-logic/06-relations-and-functions/01-relations-and-their-properties.md#the-four-properties).

A **translation** slides every point the same distance in the same direction. Taught in [transformations, congruence and similarity](../02-middle-school/06-geometry/05-transformations-congruence-similarity.md#the-four-transformations).

The **transpose** $A^T$ of a matrix swaps its rows and columns, so entry $(i, j)$ of $A^T$ is entry $(j, i)$ of $A$. A $2 \times 3$ matrix has a $3 \times 2$ transpose. Taught in [matrix basics](../03-high-school/10-vectors-and-matrices/02-matrix-basics.md#definitions).

A **transversal** is a line that crosses two other lines at two different points. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#a-line-crossing-two-lines).

A **trapezoid** is a quadrilateral with at least one pair of parallel sides, called its bases. Its area is $\frac{1}{2}(b_1 + b_2)h$. Taught in [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md#trapezoids).

The **triangle inequality** says that each side of a triangle is less than the sum of the other two. Sides of 4, 7 and 12 can't form a triangle, since $4 + 7 < 12$. For real numbers, the triangle inequality is $\lvert a + b \rvert \le \lvert a \rvert + \lvert b \rvert$, which is proved by cases. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#the-triangle-inequality) and [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md#worked-examples).

To **truncate** a number at a given place is to replace every digit to the right of that place with 0, without looking at what those digits are. Truncating 2,996 to the tens gives 2,990, while rounding gives 3,000. For a whole number this is the same as always rounding down. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

A **truth table** lists every combination of truth values of the atomic parts of a statement, one row each, and gives the truth value of the whole in each row. A table for $n$ atomic statements has $2^n$ rows. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#the-connectives).

The **truth value** of a statement is T if it is true and F if it is false. Taught in [statements and connectives](../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md#statements).

A **turning point** of a graph is a place where it switches between rising and falling. A polynomial of degree $n$ has at most $n - 1$ of them. Taught in [polynomial functions and graphs](../03-high-school/04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md#definitions).

A **two-column proof** lists numbered statements in one column and the reason for each in the other. A paragraph proof gives the same steps in sentences. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#two-column-and-paragraph-proofs).

A **two-way table** shows the counts for two categorical variables, with one variable's categories down the side and the other's across the top. Taught in [scatter plots and two-way tables](../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md#definitions).

## U

A set is **uncountable** if it is not countable, that is, if it is infinite and cannot be paired off with $\mathbb{N}$. The real numbers and the power set of $\mathbb{N}$ are uncountable, by the diagonal argument. Taught in [cardinality and countability](../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#finite-infinite-countable).

An expression is **undefined** when the rules of arithmetic give it no value, as with division by 0. No number $q$ satisfies $q \times 0 = 5$, so $5 \div 0$ is undefined. The case $0 \div 0$ fails the other way: every $q$ satisfies $q \times 0 = 0$, so there is no single answer. Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#edge-cases-and-common-mistakes).

**Undefined terms** are the starting words of geometry, point, line and plane, which are described rather than defined, since any definition would need other words. Taught in [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#undefined-terms).

**Underflow** happens when a nonzero value is too small for the computer to store and is rounded to 0. A product of many small probabilities underflows, and the sum of their logarithms does not. Taught in [logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md#why-a-logarithm-turns-multiplication-into-addition).

The **union** $A \cup B$ of two sets is the set of elements that are in at least one of them. In a solution set, "or" means union. Taught in [compound inequalities and interval notation](../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md#definitions) and [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#the-four-operations).

The **unit circle** is the circle of radius 1 centred at the origin. The point at angle $\theta$ from the positive $x$-axis is $(\cos\theta, \sin\theta)$. Taught in [radians and the unit circle](../03-high-school/09-trigonometry/02-radians-and-the-unit-circle.md#definitions).

A **unit fraction** is a fraction with numerator 1, such as $\frac{1}{8}$. Every fraction counts unit fractions: $\frac{3}{8}$ is three copies of $\frac{1}{8}$. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions).

A **unit vector** is a vector of length 1. Dividing a nonzero vector by its length, called normalizing it, gives the unit vector in its direction. Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md#definitions).

A **universal statement** $\forall x \in D,\ P(x)$ ("for every $x$ in $D$, $P(x)$") is true when $P(a)$ is true for every element $a$ of $D$, and false when it fails for at least one. A universal statement over an empty domain is true. Taught in [quantifiers](../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md#the-two-quantifiers).

The **universe** $U$ is the one fixed set of which every set in a discussion is a subset, and complements are taken inside it. It is part of the problem and has to be stated. Taught in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#sets-equality-and-subsets).

## V

A statement "if P, then Q" is **vacuously true** when P is false, because there is no case in which it could fail. For the same reason, "every element of $\emptyset$ is even" is true. Taught in [conditionals and biconditionals](../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md).

A **variable** is a symbol, usually a letter, that stands for a number. The number may be one unknown value that we want to find, or it may range over a set of values. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#definitions).

The **variance** measures how spread out values are: it is the average squared distance from the mean. For a random variable, $\operatorname{Var}(X) = E[(X - \mu)^2]$, and its square root is the standard deviation. Taught in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md --> and descriptive statistics and study design<!-- link: ../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md -->.

A **vector** is a quantity with a size and a direction, written as a list of numbers such as $(3, 4)$. The numbers in the list are its components. In linear algebra the word covers every element of a vector space. Taught in [vectors in the plane](../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md).

If $s(t)$ is the position of an object on a line at time $t$, its **velocity** is $v(t) = s'(t)$. The sign of the velocity gives the direction of motion. Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md#definitions).

A **Venn diagram** draws a box for the universe and a circle for each set, with a point inside a circle standing for an element of that set. It helps find an answer, but it shows only one arrangement of the sets, so it is not a proof. Taught in [sets and set operations](../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md#sets-equality-and-subsets).

The **vertex** of a parabola is its turning point: the lowest point when it opens up and the highest when it opens down. For $f(x) = ax^2 + bx + c$ it is at $x = -\frac{b}{2a}$. The vertex of an angle is a different thing, the point where its two rays meet. Taught in [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#definitions).

The **vertex form** of a quadratic function is $f(x) = a(x - h)^2 + k$, where $(h, k)$ is the vertex. The point is $(h, k)$, not $(-h, k)$, because $x - h$ is zero at $x = h$. Taught in [quadratic functions and graphs](../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#definitions).

**Vertical angles** are the angles opposite each other where two lines cross. They are equal. Taught in [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md#pairs-of-angles) and [definitions, postulates and proof](../03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md#postulates-and-theorems).

A **vertical asymptote** is a vertical line $x = a$ that the graph of a function approaches while its values grow without bound. For a rational function in lowest terms it sits at each zero of the denominator, and the graph never crosses it. In limit notation, $x = a$ is a vertical asymptote when a one-sided limit at $a$ is $\infty$ or $-\infty$. Taught in [rational functions and asymptotes](../03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md#definitions), [graphs of trig functions](../03-high-school/09-trigonometry/03-graphs-of-trig-functions.md#definitions) and [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#definitions).

The **vertical line test** says that a graph is the graph of a function of $x$ exactly when every vertical line meets it at most once. Taught in [introduction to functions](../02-middle-school/05-linear-relationships-and-functions/03-intro-to-functions.md#the-vertical-line-test).

A **vertical stretch** replaces $f(x)$ with $a f(x)$ for $a > 1$, pulling the graph away from the $x$-axis by the factor $a$. When $0 < a < 1$ it is a compression. Replacing $x$ by $bx$ stretches or compresses horizontally by the factor $\frac{1}{b}$. Taught in [transformations of functions](../03-high-school/03-functions/04-transformations-of-functions.md#definitions).

A **vertical tangent** is a point where the curve is smooth but the tangent line is vertical, as the $y$-axis is for $x^{1/3}$ at 0. The derivative does not exist there, because the difference quotient tends to $\infty$. Taught in [the derivative definition](../05-university-core/02-derivatives/01-the-derivative-definition.md#where-a-derivative-does-not-exist).

The **volume** of a solid is the number of unit cubes that fill it, measured in cubic units such as $\text{cm}^3$. A rectangular box has volume length times width times height. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#perimeter-area-and-volume) and [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md).

## W

A **weighted mean** gives each value $x_i$ a weight $w_i$ and divides by the total weight: $\frac{\sum w_i x_i}{\sum w_i}$. A course grade with components worth different percents is a weighted mean. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md#definitions).

A definition is **well-defined** when it gives exactly one result and doesn't depend on choices that shouldn't matter. The rule "send the fraction $\frac{a}{b}$ to $a$" is not well-defined, because $\frac{1}{2} = \frac{2}{4}$ would be sent to both 1 and 2. The formal treatment is in [functions and well-definedness](../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md).

The **well-ordering principle** says that every nonempty set of natural numbers has a least element. It fails for the integers, which have no smallest element, and for the positive real numbers. Taught in [strong induction and well-ordering](../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md#definitions).

The **whole numbers** are 0, 1, 2, 3 and so on: the counting numbers together with zero. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

A **witness** is an object that shows an existence claim is true. In "$n$ is even if $n = 2k$ for some integer $k$", the integer $k$ is the witness: proving that $n$ is even means producing one, and using the fact that $n$ is even means receiving one. Taught in [proof language: let, suppose, WLOG](../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md#definitions).

**WLOG** is short for "without loss of generality". It means the proof handles one case because the other cases work the same way, often after renaming: "WLOG, assume $a \le b$". Taught in [proof language: let, suppose, WLOG](../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md) and [proof by cases and WLOG](../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md).

## Z

A **0/0 form** is a limit whose formula gives $\frac{0}{0}$ when $x = a$ is substituted. It carries no information by itself: the formula has to be rewritten, for example by factoring and cancelling, before the limit can be found. Taught in [limits, intuition and limit laws](../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md#finding-a-limit).

The **zero exponent** rule says that $a^0 = 1$ for every $a \ne 0$. The pattern $2^3 = 8$, $2^2 = 4$, $2^1 = 2$, $2^0 = 1$ halves at each step, so the next value has to be 1. The expression $0^0$ is left undefined in arithmetic, though counting formulas and Python treat it as 1. Taught in [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md#definitions).

A **zero of a function** $f$ is a number $c$ with $f(c) = 0$. It is where the graph meets the $x$-axis. Taught in [reading function graphs](../03-high-school/03-functions/02-reading-function-graphs.md#definitions).

A **zero of a polynomial**, also called a root, is a number $c$ with $p(c) = 0$. By the factor theorem it corresponds to a factor $x - c$. Taught in [polynomial division and the remainder theorem](../03-high-school/04-radicals-and-polynomials/04-polynomial-division-and-remainder-theorem.md#definitions).

The **zero property of multiplication** says that $a \times 0 = 0$ for every number $a$. Compare it with the identity property of addition: adding 0 leaves a number alone, but multiplying by 0 gives 0. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#zero-property).

The **zero-product property** says that if $ab = 0$, then $a = 0$ or $b = 0$. It is why you factor an equation with $0$ on one side, and it fails when the right side is anything else: $x(x - 3) = 10$ does not mean $x = 10$. Taught in [factoring polynomials](../03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md#zero-product-property) and [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md#definitions).
