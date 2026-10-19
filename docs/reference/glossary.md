# Glossary

Plain definitions of the terms used across the book, in alphabetical order. Each entry ends with the lesson that teaches the term. Where a term has a formal definition, the entry gives the plain version and the lesson gives the formal one. The glossary grows as new folders are written.

Jump to a letter: [A](#a), [B](#b), [C](#c), [D](#d), [E](#e), [F](#f), [H](#h), [I](#i), [L](#l), [M](#m), [N](#n), [P](#p), [Q](#q), [R](#r), [S](#s), [T](#t), [V](#v), [W](#w).

## A

An **algorithm** is a finite list of exact steps that solves a problem and always stops with an answer. Long division is the first algorithm in this book. Taught in [long division](../01-elementary/07-long-division.md) and invariants and algorithm correctness<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->.

In a proof, an **arbitrary** element is one you pick with no assumptions beyond the stated ones, so whatever you prove about it holds for every element. "Let $n$ be an arbitrary integer" starts most proofs of statements about every integer. Taught in proof language: let, suppose, WLOG<!-- link: ../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md -->.

An **axiom** is a statement accepted without proof as a starting point for a theory. In a university course, rules of arithmetic such as $a + b = b + a$ are axioms for the real numbers. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

## B

The **base** has two meanings. In a power $b^n$, the base is the number being multiplied, $b$; a logarithm $\log_b x$ has a base in the same sense. In a number system, the base is the number of digits and the factor between neighbouring places: base 10 for decimal, base 2 for binary. Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md) and [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

A **basis** of a vector space is a set of vectors that are linearly independent and span the space, so every vector in the space is a linear combination of them in exactly one way. The vectors $(1, 0)$ and $(0, 1)$ form a basis of $\mathbb{R}^2$. The formal definition is in linear independence, basis and dimension<!-- link: ../05-university-core/06-linear-algebra/04-linear-independence-basis-and-dimension.md -->.

A function is **bijective**, or a bijection, when it is both injective and surjective: every element of the codomain is the output of exactly one input. A bijection pairs up the domain and the codomain one to one, so it has an inverse. Taught in injective, surjective and bijective functions<!-- link: ../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md -->.

**Binary** is base 2: numbers written with only the digits 0 and 1, where the places are worth $1, 2, 4, 8, \dots$ from the right. Computers store all data in binary. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

A **bit** is a binary digit, 0 or 1. It is the smallest unit of information, the answer to one yes-or-no question. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md) and bits and information<!-- link: ../06-cs-math/01-number-representation/02-bits-and-information.md -->.

A **byte** is 8 bits, enough for $2^8 = 256$ different values, from 0 to 255. Taught in bits and information<!-- link: ../06-cs-math/01-number-representation/02-bits-and-information.md -->.

## C

The **cardinality** of a set is the number of elements in it, written $\lvert A \rvert$. For infinite sets it is defined by comparing sets with bijections; the formal version is in cardinality and countability<!-- link: ../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md -->.

The **codomain** of a function $f \colon A \to B$ is the set $B$ that its outputs are allowed to land in. It can be bigger than the range, which is the set of outputs that actually occur. Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md -->.

A **coefficient** is a number that multiplies a variable in a term. In $3x^2 - 5x$, the coefficients are $3$ and $-5$. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md).

A **composite** number is an integer greater than 1 that is not prime, so it has a factor other than 1 and itself. The number 12 is composite, since $12 = 3 \times 4$, and the number 1 is neither prime nor composite. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md).

The **conclusion** of "if P, then Q" is Q, the part that is claimed to follow. In a theorem, the conclusion is what the proof has to reach. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

A **conjecture** is a statement that people believe is true but that nobody has proved yet. Goldbach's conjecture, that every even integer greater than 2 is the sum of two primes, is a famous one that is still open. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

The **contrapositive** of "if P, then Q" is "if not Q, then not P". It is logically equivalent to the original, so proving one proves the other. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md --> and contrapositive proof<!-- link: ../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md -->.

The **converse** of "if P, then Q" is "if Q, then P". It is a different statement: "if a number is divisible by 4, then it is even" is true, but its converse is false. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

A **corollary** is a result that follows quickly from a theorem that was just proved. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

A set is **countable** when its elements can be listed in a sequence $a_0, a_1, a_2, \dots$, which may be finite. The integers and the rational numbers are countable, and the real numbers are not. Some books use "countable" only for infinite sets; the formal definition is in cardinality and countability<!-- link: ../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md -->.

A **counterexample** is one case that makes a statement about every case false. The number 2 is a counterexample to "every prime is odd". Taught in counterexamples and disproof<!-- link: ../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md -->.

## D

A **definition** gives the exact meaning of a term. A definition worded with "if" is read as "if and only if": "an integer $n$ is even if $n = 2k$ for some integer $k$" also tells you that every even integer has that form. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

The **denominator** of a fraction $\frac{a}{b}$ is the number on the bottom, $b$, which says how many equal parts the whole is cut into. It can't be 0. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md).

The **derivative** of a function at a point is its instantaneous rate of change there, which is the slope of the tangent line. It is defined as the limit $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$; the formal treatment is in the derivative definition<!-- link: ../05-university-core/02-derivatives/01-the-derivative-definition.md -->.

The **dividend** is the number being divided: in $n \div d$, it is $n$. Taught in [long division](../01-elementary/07-long-division.md).

The **divisor** in $n \div d$ is $d$, the number you divide by. In number theory, a divisor of $n$ is an integer $d$ with $d \mid n$, so there the word means the same as "factor". Taught in [long division](../01-elementary/07-long-division.md) and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

The **domain** of a function is its set of allowed inputs, the set $A$ in $f \colon A \to B$. When a formula such as $\frac{1}{x}$ comes with no stated domain, the domain is taken to be every real number the formula works for, here every $x \ne 0$. Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md -->.

## E

A number $\lambda$ is an **eigenvalue** of a square matrix $A$ when $A\mathbf{v} = \lambda\mathbf{v}$ for some nonzero vector $\mathbf{v}$, which is called an eigenvector. In plain words, $A$ only stretches that vector, by the factor $\lambda$. Taught in eigenvalues and eigenvectors<!-- link: ../05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md -->.

An **element** of a set is one of the objects in it. Writing $x \in A$ says that $x$ is an element of $A$. Taught in sets and set operations<!-- link: ../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md -->.

The **empty set**, written $\emptyset$, is the set with no elements. It is a subset of every set, and its cardinality is 0. Taught in sets and set operations<!-- link: ../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md -->.

An **equation** is a statement that two expressions are equal, such as $2x + 1 = 7$. Solving it means finding every value of the variable that makes it true. Taught in [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md).

The **expected value** $E[X]$ of a random variable is its long-run average: each value weighted by its probability, $\sum x \, P(X = x)$. One roll of a fair die has expected value 3.5, even though no roll shows 3.5. Taught in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md -->.

The **exponent** in $b^n$ is $n$, the number of times the base is used as a factor. Negative and fractional exponents extend the idea, so that $b^{-1} = \frac{1}{b}$ and $b^{1/2} = \sqrt{b}$. Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md) and exponent rules<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md -->.

An **expression** is a combination of numbers, variables and operations with no equals sign, such as $3x^2 - 5x$. An expression has a value, while an equation is true or false. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md).

## F

A **factor** of an integer is an integer that divides it with no remainder: the positive factors of 12 are 1, 2, 3, 4, 6 and 12. In algebra, a factor is one of the pieces multiplied together in a product, such as $x - 2$ in $(x - 2)(x + 3)$. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md).

A **function** from a set $A$ to a set $B$ assigns to each element of $A$ exactly one element of $B$. A rule such as $f(x) = x^2$ is one way to give a function. Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md -->; the formal definition, as a set of ordered pairs, is in functions and well-definedness<!-- link: ../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md -->.

## H

**Hexadecimal**, or hex, is base 16, with the digits 0 to 9 and then A to F for the values 10 to 15. Each hex digit stands for exactly 4 bits, which is why programmers use it: $\mathrm{FF}_{16} = 1111\,1111_2 = 255$. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

The **hypothesis** of "if P, then Q" is P, the part that is assumed. The hypotheses of a theorem are what its proof may use. In statistics, a hypothesis is instead a claim to be tested. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

## I

An **identity** is an equation that is true for every value of its variables, such as $(a + b)^2 = a^2 + 2ab + b^2$. The word also names something that changes nothing: $0$ for addition, $1$ for multiplication, the identity matrix $I$ and the identity function $x \mapsto x$. Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md).

**Iff** is short for "if and only if". "P iff Q" means that P and Q imply each other, so they are true together or false together. A proof of an iff statement usually has two parts, one for each direction. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md --> and if and only if proofs<!-- link: ../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md -->.

**Induction**, or mathematical induction, proves a statement for every natural number in two parts. The base case proves it for the first value, usually $n = 0$ or $n = 1$, and the inductive step shows that the statement for $k$ implies the statement for $k + 1$. Taught in mathematical induction<!-- link: ../04-proofs-and-logic/05-induction/01-mathematical-induction.md -->.

An **inequality** compares two expressions with $<$, $\le$, $>$ or $\ge$, such as $2x + 1 < 7$. Its solution is usually a whole interval of numbers rather than a single value. Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md).

A function is **injective**, or one-to-one, when different inputs always give different outputs: $f(a_1) = f(a_2)$ implies $a_1 = a_2$. The squaring function on $\mathbb{R}$ is not injective, since $(-2)^2 = 2^2$. Taught in injective, surjective and bijective functions<!-- link: ../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md -->.

An **integer** is a whole number or the negative of one: $\dots, -2, -1, 0, 1, 2, \dots$. The set of integers is $\mathbb{Z}$. Taught in roots, irrationals and types of numbers<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md -->.

The definite **integral** $\int_a^b f(x)\,dx$ is the signed area between the graph of $f$ and the $x$-axis from $a$ to $b$, defined as a limit of sums of thin rectangles. The indefinite integral $\int f(x)\,dx$ is the family of antiderivatives of $f$. The formal definition is in Riemann sums and the definite integral<!-- link: ../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md -->.

An **invariant** is a property that stays true at every step of a process, such as every pass through a loop. It is the standard tool for proving an algorithm correct: show it holds at the start, show each step keeps it true, and see what it says when the process stops. Taught in invariants and algorithm correctness<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->.

An **irrational** number is a real number that is not rational, so it can't be written as a fraction of two integers. Its decimal expansion never ends and never repeats. Two examples are $\sqrt{2}$ and $\pi$. Taught in roots, irrationals and types of numbers<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md -->.

## L

A **lemma** is a smaller result, proved mainly as a step toward a theorem. A few lemmas are important in their own right, such as the pumping lemma in theory of computation. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

The **limit** of $f(x)$ as $x$ approaches $a$ is the value that $f(x)$ gets as close as you like to when $x$ is close enough to $a$, whatever happens at $a$ itself. The intuition is in limits: intuition and limit laws<!-- link: ../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md -->, and the formal version is in the epsilon-delta definition<!-- link: ../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md -->.

A **linear combination** of vectors $\mathbf{v}_1, \dots, \mathbf{v}_n$ is a sum $c_1\mathbf{v}_1 + \dots + c_n\mathbf{v}_n$, where the weights $c_1, \dots, c_n$ are numbers. For example, $2(1, 0) + 3(0, 1) = (2, 3)$. Taught in vectors, dot product and span<!-- link: ../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md -->.

## M

A **matrix** is a rectangular grid of numbers. One with $m$ rows and $n$ columns is an $m \times n$ matrix. A matrix can hold the coefficients of a system of equations, or describe a linear transformation. Taught in matrix basics<!-- link: ../03-high-school/10-vectors-and-matrices/02-matrix-basics.md -->.

The **mean** of a list of numbers is their sum divided by how many there are, the ordinary average. The mean of 2, 4 and 9 is $\frac{15}{3} = 5$. Taught in describing data<!-- link: ../02-middle-school/07-statistics-and-probability/01-describing-data.md -->.

The **median** is the middle value of a list sorted in order, or the mean of the two middle values when the list has an even number of entries. Extreme values move it less than they move the mean: the median of 2, 4 and 90 is 4, while the mean is 32. Taught in describing data<!-- link: ../02-middle-school/07-statistics-and-probability/01-describing-data.md -->.

**Mod**, short for modulo, has two related uses. As an operation, $a \bmod n$ is the remainder when $a$ is divided by $n$, so $17 \bmod 5 = 2$. As a relation, $a \equiv b \pmod{n}$ says that $a$ and $b$ leave the same remainder, and $n$ is called the **modulus**. (The modulus of a complex number is something else, its absolute value.) Taught in divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

The **mode** is the value that occurs most often in a list. A list can have more than one mode. Taught in describing data<!-- link: ../02-middle-school/07-statistics-and-probability/01-describing-data.md -->.

A **multiple** of an integer $n$ is $n$ times some integer, so the multiples of 4 are $\dots, -8, -4, 0, 4, 8, \dots$. Saying that $b$ is a multiple of $a$ is the same as saying that $a$ is a factor of $b$. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md).

## N

A **natural number** is a counting number. In this book the natural numbers are $\mathbb{N} = \{0, 1, 2, \dots\}$, but many books start at 1, so check the definition in whatever you are reading. Taught in roots, irrationals and types of numbers<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md -->.

A condition Q is **necessary** for P when P can't happen without Q, which is the statement "if P, then Q". Being even is necessary for being divisible by 4. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

The **numerator** of a fraction $\frac{a}{b}$ is the number on top, $a$, which says how many of the equal parts you have. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md).

## P

A **percent** is a ratio written per hundred: $x\%$ means $\frac{x}{100}$. So 35% is $0.35$, and 113% is $1.13$. Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md).

A **prime** number is an integer greater than 1 whose only positive factors are 1 and itself, such as $2, 3, 5, 7$ and $11$. The number 1 is not prime. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md) and primes and unique factorization<!-- link: ../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md -->.

A **proof** is an argument that shows a statement is true, where each step follows from definitions, axioms, the hypotheses or results proved earlier. Checking many examples is not a proof. Taught in what is a proof<!-- link: ../04-proofs-and-logic/01-language-and-notation/01-what-is-a-proof.md -->.

## Q

A **quantifier** says how many elements a statement is about. "For every" ($\forall$) claims the statement for each element of a set, and "there exists" ($\exists$) claims it for at least one. Taught in quantifiers<!-- link: ../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md -->.

The **quotient** is the result of a division. In division with a remainder, $n = qd + r$, it is the whole number $q$ of times that $d$ fits into $n$. Taught in [long division](../01-elementary/07-long-division.md).

## R

A **random variable** is a number whose value depends on the outcome of a random experiment, such as the total of two dice. Formally it is a function from the sample space to $\mathbb{R}$; the details are in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md -->.

The **range** of a function is the set of outputs that actually occur, $\{f(a) : a \in A\}$, also called the image. Some books use "range" to mean the codomain, so check which one is meant. In statistics, the range of a data set is its largest value minus its smallest. Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md -->.

A **rate** is a ratio of two quantities with different units, such as 90 km per hour or \$18 per hour. A unit rate gives the amount for one unit of the second quantity. Taught in [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md).

A **ratio** compares two quantities by division. A recipe with 2 cups of flour for every 3 cups of milk has a flour-to-milk ratio of $2 : 3$, which is the fraction $\frac{2}{3}$. Taught in [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md).

A **rational** number is one that can be written as a fraction $\frac{a}{b}$ of integers with $b \ne 0$. Every decimal that ends or repeats is rational: $0.75 = \frac{3}{4}$ and $0.333\ldots = \frac{1}{3}$. Taught in roots, irrationals and types of numbers<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md -->.

A **real number** is a point on the number line, rational or irrational. The set of real numbers is $\mathbb{R}$. Its formal properties are in real numbers, axioms and set notation<!-- link: ../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md -->.

The **reciprocal** of a nonzero number $a$ is $\frac{1}{a}$, the number you multiply $a$ by to get 1. The reciprocal of $\frac{2}{3}$ is $\frac{3}{2}$, and 0 has no reciprocal. Taught in [multiplying and dividing fractions](../01-elementary/11-multiplying-and-dividing-fractions.md).

**Recursion** defines something in terms of smaller versions of itself, together with a starting case. The factorial is defined recursively: $0! = 1$, and $n! = n \cdot (n - 1)!$ for $n \ge 1$. Taught in sequences and recursion<!-- link: ../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md --> and recursive definitions and structural induction<!-- link: ../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md -->.

The **remainder** is what is left over when a division doesn't come out even. In $n = qd + r$ it is $r$, and it always satisfies $0 \le r < d$. Taught in [long division](../01-elementary/07-long-division.md).

## S

A **sequence** is an ordered list of numbers $a_1, a_2, a_3, \dots$, finite or infinite. Formally it is a function whose domain is a set of natural numbers. Taught in sequences and recursion<!-- link: ../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md -->.

A **series** is the sum of the terms of a sequence, such as $1 + \frac{1}{2} + \frac{1}{4} + \dots$. An infinite series has a value only when its partial sums approach a limit, and this one approaches 2. Taught in summation notation and series<!-- link: ../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md --> and infinite series basics<!-- link: ../05-university-core/05-sequences-and-series/02-infinite-series-basics.md -->.

A **set** is a collection of distinct objects, called its elements, in which order and repeats don't matter. Most of university math is built on sets. Taught in sets and set operations<!-- link: ../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md -->.

The **span** of a set of vectors is the set of all their linear combinations. Two vectors in $\mathbb{R}^3$ that don't lie on the same line through the origin span a plane through the origin. Taught in vectors, dot product and span<!-- link: ../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md -->.

A **statement**, or proposition, is a sentence that is either true or false. "7 is prime" is a statement, while "$x > 3$" is not one until you know $x$. Taught in statements and connectives<!-- link: ../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md -->.

A set $A$ is a **subset** of a set $B$, written $A \subseteq B$, when every element of $A$ is also in $B$. Every set is a subset of itself, and $\emptyset$ is a subset of every set. Taught in sets and set operations<!-- link: ../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md -->.

A condition P is **sufficient** for Q when P guarantees Q, which is the statement "if P, then Q". Being divisible by 4 is sufficient for being even. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

**Summation** notation writes a long sum compactly: $\sum_{i=1}^{n} a_i$ means $a_1 + a_2 + \dots + a_n$. Taught in summation notation and series<!-- link: ../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md -->.

A function $f \colon A \to B$ is **surjective**, or onto, when every element of $B$ is the output of at least one input, so the range equals the codomain. The squaring function from $\mathbb{R}$ to $\mathbb{R}$ is not surjective, since no real number squares to $-1$. Taught in injective, surjective and bijective functions<!-- link: ../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md -->.

## T

A **term** is one of the pieces added together in an expression: $3x^2 - 5x + 2$ has the three terms $3x^2$, $-5x$ and $2$. A term of a sequence is one of its entries. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md).

A **theorem** is a statement that has been proved, usually one important enough to be named or used often. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

## V

A statement "if P, then Q" is **vacuously true** when P is false, because there is no case in which it could fail. For the same reason, "every element of $\emptyset$ is even" is true. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

The **variance** measures how spread out values are: it is the average squared distance from the mean. For a random variable, $\operatorname{Var}(X) = E[(X - \mu)^2]$, and its square root is the standard deviation. Taught in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md --> and descriptive statistics and study design<!-- link: ../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md -->.

A **vector** is a quantity with a size and a direction, written as a list of numbers such as $(3, 4)$. In linear algebra the word covers every element of a vector space. Taught in vectors in the plane<!-- link: ../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md -->.

## W

A definition is **well-defined** when it gives exactly one result and doesn't depend on choices that shouldn't matter. The rule "send the fraction $\frac{a}{b}$ to $a$" is not well-defined, because $\frac{1}{2} = \frac{2}{4}$ would be sent to both 1 and 2. The formal treatment is in functions and well-definedness<!-- link: ../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md -->.

**WLOG** is short for "without loss of generality". It means the proof handles one case because the other cases work the same way, often after renaming: "WLOG, assume $a \le b$". Taught in proof language: let, suppose, WLOG<!-- link: ../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md --> and proof by cases and WLOG<!-- link: ../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md -->.
