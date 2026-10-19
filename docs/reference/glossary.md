# Glossary

Plain definitions of the terms used across the book, in alphabetical order. Each entry ends with the lesson that teaches the term. Where a term has a formal definition, the entry gives the plain version and the lesson gives the formal one. The glossary grows as new folders are written.

Jump to a letter: [A](#a), [B](#b), [C](#c), [D](#d), [E](#e), [F](#f), [G](#g), [H](#h), [I](#i), [L](#l), [M](#m), [N](#n), [O](#o), [P](#p), [Q](#q), [R](#r), [S](#s), [T](#t), [U](#u), [V](#v), [W](#w), [Z](#z).

## A

The **absolute value** of a number $x$, written $\lvert x \rvert$, is its distance from 0 on the number line, so it is never negative: $\lvert -6 \rvert = \lvert 6 \rvert = 6$. The distance between two numbers $a$ and $b$ is $\lvert a - b \rvert$. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions).

In $a + b = c$, the numbers $a$ and $b$ are the **addends** and $c$ is their sum. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions).

The **additive inverse** of a number $a$ is its opposite $-a$, the number that adds to $a$ to give 0: $7 + (-7) = 0$. Subtracting a number is the same as adding its additive inverse, $a - b = a + (-b)$. Taught in [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#definitions).

An **algorithm** is a finite list of exact steps that solves a problem and always stops with an answer. Long division is the first algorithm in this book. Taught in [long division](../01-elementary/07-long-division.md) and invariants and algorithm correctness<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->.

An **angle** is a pair of rays with a shared endpoint, called the vertex. Its size is measured in degrees, and a full turn is $360^\circ$. An angle is acute if it is less than $90^\circ$, right if it is exactly $90^\circ$, obtuse if it is between $90^\circ$ and $180^\circ$, and straight if it is exactly $180^\circ$. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#points-lines-and-angles) and [angles and triangles](../02-middle-school/06-geometry/01-angles-and-triangles.md).

In a proof, an **arbitrary** element is one you pick with no assumptions beyond the stated ones, so whatever you prove about it holds for every element. "Let $n$ be an arbitrary integer" starts most proofs of statements about every integer. Taught in proof language: let, suppose, WLOG<!-- link: ../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md -->.

The **area** of a flat shape is the number of unit squares that cover it with no gaps and no overlaps, measured in square units such as $\text{cm}^2$. A rectangle has area length times width, a parallelogram base times height, and a triangle half of base times height. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#perimeter-area-and-volume) and [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md).

The **associative property** says that the grouping of a repeated operation doesn't matter: $(a + b) + c = a + (b + c)$ and $(a \times b) \times c = a \times (b \times c)$ for all numbers $a$, $b$ and $c$. Subtraction and division are not associative, since $(10 - 5) - 2 = 3$ but $10 - (5 - 2) = 7$. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#associative-properties).

An **axiom** is a statement accepted without proof as a starting point for a theory. In a university course, rules of arithmetic such as $a + b = b + a$ are axioms for the real numbers. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

## B

The **base** has three meanings. In a power $b^n$, the base is the number being multiplied, $b$; a logarithm $\log_b x$ has a base in the same sense. In a number system, the base is the number of digits and the factor between neighbouring places: base 10 for decimal, base 2 for binary. In a triangle or a parallelogram, the base is the side you choose to measure the height from, usually the one drawn at the bottom. Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#definitions), [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md), [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md) and [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#base-and-height).

A **basis** of a vector space is a set of vectors that are linearly independent and span the space, so every vector in the space is a linear combination of them in exactly one way. The vectors $(1, 0)$ and $(0, 1)$ form a basis of $\mathbb{R}^2$. The formal definition is in linear independence, basis and dimension<!-- link: ../05-university-core/06-linear-algebra/04-linear-independence-basis-and-dimension.md -->.

A function is **bijective**, or a bijection, when it is both injective and surjective: every element of the codomain is the output of exactly one input. A bijection pairs up the domain and the codomain one to one, so it has an inverse. Taught in injective, surjective and bijective<!-- link: ../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md -->.

**Binary** is base 2: numbers written with only the digits 0 and 1, where the places are worth $1, 2, 4, 8, \dots$ from the right. Computers store all data in binary. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

A **bit** is a binary digit, 0 or 1. It is the smallest unit of information, the answer to one yes-or-no question. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md) and bits and information<!-- link: ../06-cs-math/01-number-representation/02-bits-and-information.md -->.

A **byte** is 8 bits, enough for $2^8 = 256$ different values, from 0 to 255. Taught in bits and information<!-- link: ../06-cs-math/01-number-representation/02-bits-and-information.md -->.

## C

The **cardinality** of a set is the number of elements in it, written $\lvert A \rvert$. For infinite sets it is defined by comparing sets with bijections; the formal version is in cardinality and countability<!-- link: ../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md -->.

**Casting out nines** checks a multiplication with remainders on division by 9. Reduce each factor to one digit by taking digit sums again and again, multiply those two digits and reduce the result, and compare it with your answer reduced the same way. Different digits mean the answer is wrong, but matching digits don't prove it right, since a mistake that changes the answer by a multiple of 9 passes. Taught in [multi-digit multiplication](../01-elementary/05-multi-digit-multiplication.md#casting-out-nines).

**Clearing fractions** means multiplying both sides of an equation by a common denominator of all its fractions, usually the least common denominator, so that no fractions remain. Every term gets multiplied, including the ones with no fraction. Taught in [multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#definitions).

The **codomain** of a function $f \colon A \to B$ is the set $B$ that its outputs are allowed to land in. It can be bigger than the range, which is the set of outputs that actually occur. Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md -->.

A **coefficient** is a number that multiplies a variable in a term. In $3x^2 - 5x$, the coefficients are $3$ and $-5$. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md).

A **common denominator** of two or more fractions is a common multiple of their denominators. The least common denominator (LCD) is their least common multiple: for $\frac{3}{4}$ and $\frac{5}{6}$ it is 12. Taught in [adding and subtracting fractions](../01-elementary/10-adding-and-subtracting-fractions.md#definitions).

The **commutative property** says that order doesn't matter in a sum or a product: $a + b = b + a$ and $a \times b = b \times a$ for all numbers $a$ and $b$. Subtraction and division are not commutative, since $10 - 3 = 7$ but $3 - 10 = -7$. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#commutative-properties).

A **composite** number is an integer greater than 1 that is not prime, so it has a factor other than 1 and itself. The number 12 is composite, since $12 = 3 \times 4$, and the number 1 is neither prime nor composite. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md).

A **compound inequality** is two inequalities joined by "and" or "or". The statement $-2 < x \le 5$ means "$-2 < x$ and $x \le 5$", the numbers between $-2$ and 5 with 5 included. Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#compound-inequalities-a-preview) and compound inequalities and interval notation<!-- link: ../03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md -->.

The **conclusion** of "if P, then Q" is Q, the part that is claimed to follow. In a theorem, the conclusion is what the proof has to reach. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

A **conjecture** is a statement that people believe is true but that nobody has proved yet. Goldbach's conjecture, that every even integer greater than 2 is the sum of two primes, is a famous one that is still open. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

When $y = kx$, the number $k$ is the **constant of proportionality**. It is the unit rate $\frac{y}{x}$: gas at \$1.50 per litre costs $y = 1.5x$ dollars for $x$ litres. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#definitions).

A **constant term** is a term with no variable, such as the 7 in $4x^2 - x + 7$. Its value stays the same whatever the variable is. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#definitions).

The **contrapositive** of "if P, then Q" is "if not Q, then not P". It is logically equivalent to the original, so proving one proves the other. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md --> and contrapositive proof<!-- link: ../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md -->.

The **converse** of "if P, then Q" is "if Q, then P". It is a different statement: "if a number is divisible by 4, then it is even" is true, but its converse is false. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

A **conversion factor** is a fraction whose numerator and denominator are the same amount written in two units, such as $\frac{1000\ \text{m}}{1\ \text{km}}$, so the fraction equals 1. Multiplying by it changes the units without changing the amount. Taught in [measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#definitions).

The **coordinate plane** is a flat grid made by two number lines, the horizontal $x$-axis and the vertical $y$-axis, which cross at their zeros, a point called the origin. Each point has coordinates $(x, y)$, written in that order: the point $(3, 2)$ is 3 units right of the origin and 2 units up. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#shapes-on-a-grid) and [the coordinate plane](../02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md).

A **corollary** is a result that follows quickly from a theorem that was just proved. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

A set is **countable** when its elements can be listed in a sequence $a_0, a_1, a_2, \dots$, which may be finite. The integers and the rational numbers are countable, and the real numbers are not. Some books use "countable" only for infinite sets; the formal definition is in cardinality and countability<!-- link: ../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md -->.

A **counterexample** is one case that makes a statement about every case false. The number 2 is a counterexample to "every prime is odd", and $3 - 10 \ne 10 - 3$ is a counterexample to "subtraction is commutative". Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#what-fails-for-subtraction-and-division) and counterexamples and disproof<!-- link: ../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md -->.

The **cube** of a number $b$ is $b^3 = b \times b \times b$, read "$b$ cubed", after the volume of a cube. A perfect cube is the cube of an integer, and unlike a perfect square it can be negative: $(-2)^3 = -8$. Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#definitions).

## D

A **decimal** is a number written in base 10 with a decimal point, where the digits after the point stand for tenths, hundredths, thousandths and so on. Those digits are its decimal places, so 24.375 has three decimal places and stands for $24 + \frac{3}{10} + \frac{7}{100} + \frac{5}{1000}$. Taught in [decimals: place value, adding and subtracting](../01-elementary/12-decimals-place-value-and-adding.md#definitions).

A **definition** gives the exact meaning of a term. A definition worded with "if" is read as "if and only if": "an integer $n$ is even if $n = 2k$ for some integer $k$" also tells you that every even integer has that form. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

The **denominator** of a fraction $\frac{a}{b}$ is the number on the bottom, $b$, which says how many equal parts the whole is cut into. It can't be 0. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md).

The **derivative** of a function at a point is its instantaneous rate of change there, which is the slope of the tangent line. It is defined as the limit $f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$; the formal treatment is in the derivative definition<!-- link: ../05-university-core/02-derivatives/01-the-derivative-definition.md -->.

The **difference** $a - b$ is the number you add to $b$ to get $a$, so $52 - 18 = 34$ because $18 + 34 = 52$. For integers it is the same as adding the opposite: $3 - 7 = 3 + (-7) = -4$. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions) and [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#definitions).

A **digit** is one of the ten symbols 0 to 9 that write numbers in base 10. Other bases use other digits: binary uses only 0 and 1. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

**Dimensional analysis** converts units by multiplying by conversion factors and cancelling each unit that appears in both a numerator and a denominator. For example, $90\ \frac{\text{km}}{\text{h}} \times \frac{1000\ \text{m}}{1\ \text{km}} \times \frac{1\ \text{h}}{3600\ \text{s}} = 25\ \frac{\text{m}}{\text{s}}$. Taught in [measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#definitions).

The **distributive property** says that $a \times (b + c) = a \times b + a \times c$ for all numbers $a$, $b$ and $c$: to multiply a sum, multiply each term and add the results. It holds over subtraction too, and read from right to left it pulls out a common factor. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#distributive-property) and [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#the-properties-behind-each-step).

The **dividend** is the number being divided: in $n \div d$, it is $n$. Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and [long division](../01-elementary/07-long-division.md).

A whole number $n$ is **divisible** by a nonzero whole number $d$ when $n \div d$ leaves remainder 0, that is, when $n = kd$ for some whole number $k$. So 24 is divisible by 4, and 26 is not. The same fact is written $d \mid n$ and read "$d$ divides $n$". Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

The **division algorithm** is the theorem that for integers $n$ and $d$ with $d > 0$, there are unique integers $q$ and $r$ with $n = qd + r$ and $0 \le r < d$. Despite its name it is a theorem, not a method; long division is one method for finding $q$ and $r$. Taught in [long division](../01-elementary/07-long-division.md#definitions) and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

The **divisor** in $n \div d$ is $d$, the number you divide by. In number theory, a divisor of $n$ is an integer $d$ with $d \mid n$, so there the word means the same as "factor". Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions), [long division](../01-elementary/07-long-division.md) and divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

The **domain** of a function is its set of allowed inputs, the set $A$ in $f \colon A \to B$. When a formula such as $\frac{1}{x}$ comes with no stated domain, the domain is taken to be every real number the formula works for, here every $x \ne 0$. Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md -->.

## E

A number $\lambda$ is an **eigenvalue** of a square matrix $A$ when $A\mathbf{v} = \lambda\mathbf{v}$ for some nonzero vector $\mathbf{v}$, which is called an eigenvector. In plain words, $A$ only stretches that vector, by the factor $\lambda$. Taught in eigenvalues and eigenvectors<!-- link: ../05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md -->.

An **element** of a set is one of the objects in it. Writing $x \in A$ says that $x$ is an element of $A$. Taught in sets and set operations<!-- link: ../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md -->.

The **empty set**, written $\emptyset$, is the set with no elements. It is a subset of every set, and its cardinality is 0. Taught in sets and set operations<!-- link: ../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md -->.

An **equation** is a statement that two expressions are equal, such as $2x + 1 = 7$. Solving it means finding every value of the variable that makes it true. Taught in [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md).

The word **equivalent** has a precise meaning for each kind of object. Two fractions are equivalent when they are equal as numbers, as $\frac{1}{4}$ and $\frac{2}{8}$ are, and two ratios are equivalent when one is the other with every term multiplied by the same nonzero number, as with $1:3$ and $2:6$. Two expressions are equivalent when they have the same value for every value of their variables. Two equations, or two inequalities, are equivalent when they have the same solution set. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions), [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions), [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#definitions) and [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#definitions).

An **estimate** is an approximate answer, usually worked out from rounded numbers: $389 + 412 \approx 400 + 400 = 800$, where $\approx$ means "is approximately equal to". Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions) and [estimation and sanity checks](../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md).

To **evaluate** an expression is to replace each variable with a given number and work out the value. Evaluating $5 + 0.40t$ at $t = 20$ gives 13. Replacing a variable with a number, or with another expression, is called substitution. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#definitions).

To **expand** a product is to multiply it out into a sum of terms with the distributive property, as in $3(x + 4) = 3x + 12$. Factoring goes the other way. Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#definitions).

The **expanded form** of a number writes it as the sum of the values of its digits: $4{,}072 = 4{,}000 + 70 + 2$. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

The **expected value** $E[X]$ of a random variable is its long-run average: each value weighted by its probability, $\sum x \, P(X = x)$. One roll of a fair die has expected value 3.5, even though no roll shows 3.5. Taught in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md -->.

The **exponent** in $b^n$ is $n$, the number of times the base is used as a factor. Negative and fractional exponents extend the idea, so that $b^{-1} = \frac{1}{b}$ and $b^{1/2} = \sqrt{b}$. Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#definitions), [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md) and [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).

An **expression** is a combination of numbers, variables and operations with no equals sign, such as $3x^2 - 5x$. An expression has a value, while an equation is true or false. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md).

## F

A **fact family** is the set of four facts made from three related numbers, such as $5 + 7 = 12$, $7 + 5 = 12$, $12 - 7 = 5$ and $12 - 5 = 7$. Multiplication and division have fact families too: $3 \times 8 = 24$ gives $24 \div 3 = 8$ and $24 \div 8 = 3$. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions) and [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions).

A **factor** of an integer is an integer that divides it with no remainder: the positive factors of 12 are 1, 2, 3, 4, 6 and 12. More generally, the factors of a product are the numbers multiplied together, such as 4 and 6 in $4 \times 6 = 24$, or $x - 2$ in $(x - 2)(x + 3)$. As a verb, to factor an expression is to write it as a product, as in $3x + 12 = 3(x + 4)$. Taught in [multiplication and times tables](../01-elementary/03-multiplication-and-times-tables.md#definitions), [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md) and [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#definitions).

For whole numbers $a$ and $b$ with $b \ne 0$, the **fraction** $\frac{a}{b}$ is the number $a \div b$. The denominator $b$ says how many equal parts the whole is cut into, and the numerator $a$ says how many of those parts you have. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions).

A **function** from a set $A$ to a set $B$ assigns to each element of $A$ exactly one element of $B$. A rule such as $f(x) = x^2$ is one way to give a function. Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md -->; the formal definition, as a set of ordered pairs, is in functions and well-definedness<!-- link: ../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md -->.

The **fundamental theorem of arithmetic** says that every whole number greater than 1 can be written as a product of primes in exactly one way, apart from the order of the factors, as in $360 = 2^3 \times 3^2 \times 5$. It is the reason 1 is not called prime. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions) and primes and unique factorization<!-- link: ../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md -->.

## G

The **greatest common factor** (GCF) of two whole numbers is the largest number that is a factor of both. It is also called the greatest common divisor and written $\gcd(a, b)$, so $\gcd(12, 18) = 6$. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions) and GCD and Euclid's algorithm<!-- link: ../06-cs-math/02-number-theory/02-gcd-and-euclids-algorithm.md -->.

## H

The **height** of a triangle or a parallelogram is the perpendicular distance from the base to the opposite vertex or side. It is measured at a right angle to the base, not along a slanted side. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#base-and-height).

**Hexadecimal**, or hex, is base 16, with the digits 0 to 9 and then A to F for the values 10 to 15. Each hex digit stands for exactly 4 bits, which is why programmers use it: $\mathrm{FF}_{16} = 1111\,1111_2 = 255$. Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

The **hypothesis** of "if P, then Q" is P, the part that is assumed. The hypotheses of a theorem are what its proof may use. In statistics, a hypothesis is instead a claim to be tested. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

## I

An **identity** is an equation that is true for every value of its variables, such as $(a + b)^2 = a^2 + 2ab + b^2$. The word also names something that changes nothing: $0$ for addition and $1$ for multiplication (the identity properties $a + 0 = a$ and $a \times 1 = a$), the identity matrix $I$ and the identity function $x \mapsto x$. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#identity-properties) and [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md).

**Iff** is short for "if and only if". "P iff Q" means that P and Q imply each other, so they are true together or false together. A proof of an iff statement usually has two parts, one for each direction. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md --> and if and only if proofs<!-- link: ../04-proofs-and-logic/04-more-proof-methods/01-if-and-only-if-proofs.md -->.

**Implied multiplication** is a product written side by side with no sign: $3x$ means $3 \cdot x$, and $2(x + 1)$ means $2 \cdot (x + 1)$. A sign comes back once numbers replace the letters, since $3 \cdot 4$ is 12 while $34$ is thirty-four. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#how-multiplication-is-written).

An **improper fraction** has a numerator at least as big as its denominator, so it is 1 or more, as $\frac{11}{4}$ and $\frac{4}{4}$ are. A proper fraction, such as $\frac{3}{8}$, has a numerator smaller than its denominator and is less than 1. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions).

**Induction**, or mathematical induction, proves a statement for every natural number in two parts. The base case proves it for the first value, usually $n = 0$ or $n = 1$, and the inductive step shows that the statement for $k$ implies the statement for $k + 1$. Taught in mathematical induction<!-- link: ../04-proofs-and-logic/05-induction/01-mathematical-induction.md -->.

An **inequality** compares two expressions with $<$, $\le$, $>$ or $\ge$, such as $2x + 1 < 7$. Its solution is usually a whole interval of numbers rather than a single value. Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md).

A function is **injective**, or one-to-one, when different inputs always give different outputs: $f(a_1) = f(a_2)$ implies $a_1 = a_2$. The squaring function on $\mathbb{R}$ is not injective, since $(-2)^2 = 2^2$. Taught in injective, surjective and bijective<!-- link: ../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md -->.

An **integer** is a whole number or the opposite of one: $\dots, -2, -1, 0, 1, 2, \dots$. The set of integers is $\mathbb{Z}$. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions) and [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).

The definite **integral** $\int_a^b f(x)\,dx$ is the signed area between the graph of $f$ and the $x$-axis from $a$ to $b$, defined as a limit of sums of thin rectangles. The indefinite integral $\int f(x)\,dx$ is the family of antiderivatives of $f$. The formal definition is in Riemann sums and the definite integral<!-- link: ../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md -->.

An **invariant** is a property that stays true at every step of a process, such as every pass through a loop. It is the standard tool for proving an algorithm correct: show it holds at the start, show each step keeps it true, and see what it says when the process stops. Taught in invariants and algorithm correctness<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md -->.

Two operations are **inverse operations** when each one undoes the other: subtracting 5 undoes adding 5, and dividing by $c$ undoes multiplying by $c$, for $c \ne 0$. Solving an equation means applying inverse operations to both sides. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions), [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#definitions).

Two quantities are **inversely proportional** when their product is constant, so $y = \frac{k}{x}$, and doubling one halves the other. On a 240 km drive the time is $\frac{240}{\text{speed}}$: 4 h at 60 km/h, and 2 h at 120 km/h. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#what-is-inverse-proportion).

An **irrational** number is a real number that is not rational, so it can't be written as a fraction of two integers. Its decimal expansion never ends and never repeats. Two examples are $\sqrt{2}$ and $\pi$. Taught in [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#not-every-number-is-rational) and [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).

## L

The **least common multiple** (LCM) of two positive integers is the smallest positive number that is a multiple of both, written $\operatorname{lcm}(a, b)$, so $\operatorname{lcm}(12, 18) = 36$. The product of the two numbers is always a common multiple, but it is the least one only when their greatest common factor is 1. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions).

A **lemma** is a smaller result, proved mainly as a step toward a theorem. A few lemmas are important in their own right, such as the pumping lemma in theory of computation. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

**Like terms** have the same variables, each raised to the same power, so only their coefficients differ: $3x^2$ and $-5x^2$ are like terms, but $3x^2$ and $3x$ are not. Only like terms combine into one term, as in $3x + 5x = 8x$. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#definitions) and [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#the-properties-behind-each-step).

The **limit** of $f(x)$ as $x$ approaches $a$ is the value that $f(x)$ gets as close as you like to when $x$ is close enough to $a$, whatever happens at $a$ itself. The intuition is in limits, intuition and limit laws<!-- link: ../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md -->, and the formal version is in the epsilon-delta definition<!-- link: ../05-university-core/01-limits-and-continuity/02-epsilon-delta-definition.md -->.

A **line segment** is the part of a line between two endpoints, written $\overline{PQ}$ for the endpoints $P$ and $Q$, and its length is the distance between them. A line $\overleftrightarrow{PQ}$ goes on forever in both directions, and a ray $\overrightarrow{PQ}$ starts at $P$ and goes on forever through $Q$. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#points-lines-and-angles).

A **linear combination** of vectors $\mathbf{v}_1, \dots, \mathbf{v}_n$ is a sum $c_1\mathbf{v}_1 + \dots + c_n\mathbf{v}_n$, where the weights $c_1, \dots, c_n$ are numbers. For example, $2(1, 0) + 3(0, 1) = (2, 3)$. Taught in vectors, dot product and span<!-- link: ../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md -->.

A **linear equation** in one variable is an equation that can be rearranged into the form $ax = b$ by expanding, combining like terms and doing the same operation to both sides. Once the brackets are expanded, the variable appears only to the first power: $3(x - 1) = 5x + \frac{x}{2}$ is linear, while $x^2 = 3x$ is not. Taught in [multi-step equations](../02-middle-school/03-expressions-equations-inequalities/04-multi-step-equations.md#definitions).

## M

A store's **margin**, or gross margin, is its profit written as a percent of the selling price. An item bought for \$40 and sold for \$50 makes \$10 of profit, a margin of $\frac{10}{50} = 20\%$. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions).

A **markup** is the amount a store adds to its cost to get the selling price, usually written as a percent of the cost. The item bought for \$40 and sold for \$50 has a markup of $\frac{10}{40} = 25\%$, while its margin is 20%, because the margin divides the same profit by the bigger price. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions).

A **matrix** is a rectangular grid of numbers. One with $m$ rows and $n$ columns is an $m \times n$ matrix. A matrix can hold the coefficients of a system of equations, or describe a linear transformation. Taught in matrix basics<!-- link: ../03-high-school/10-vectors-and-matrices/02-matrix-basics.md -->.

The **mean** of a list of numbers is their sum divided by how many there are, the ordinary average. The mean of 2, 4 and 9 is $\frac{15}{3} = 5$. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md).

The **median** is the middle value of a list sorted in order, or the mean of the two middle values when the list has an even number of entries. Extreme values move it less than they move the mean: the median of 2, 4 and 90 is 4, while the mean is 32. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md).

A **metric prefix** is a word put in front of a unit to multiply it by a power of ten: kilo is $10^3$, centi is $10^{-2}$ and milli is $10^{-3}$, so a kilometre is 1000 m. The symbols are case-sensitive, since M is mega ($10^6$) and m is milli. Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#metric-prefixes) and [measurement and unit conversion](../01-elementary/15-measurement-and-unit-conversion.md#definitions).

A **mixed number** is a whole number followed by a proper fraction, and it means their sum: $2\frac{3}{4} = 2 + \frac{3}{4} = \frac{11}{4}$. A negative mixed number is the opposite of the whole thing, so $-2\frac{1}{4} = -\frac{9}{4}$. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions) and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#where-the-minus-sign-goes).

**Mod**, short for modulo, has two related uses. As an operation, $a \bmod n$ is the remainder when $a$ is divided by $n$, so $17 \bmod 5 = 2$. As a relation, $a \equiv b \pmod{n}$ says that $a$ and $b$ leave the same remainder, and $n$ is called the **modulus**. (The modulus of a complex number is something else, its absolute value.) Taught in divisibility and modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.

The **mode** is the value that occurs most often in a list. A list can have more than one mode. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md).

A **multiple** of an integer $n$ is $n$ times some integer, so the multiples of 4 are $\dots, -8, -4, 0, 4, 8, \dots$. Saying that $b$ is a multiple of $a$ is the same as saying that $a$ is a factor of $b$. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md).

The **multiplier** of a percent change, also called the growth factor, is $1 + r$, where $r$ is the rate written as a decimal, so that $\text{new} = (1 + r) \times \text{old}$. A 7.5% increase has multiplier 1.075, and a 30% decrease has multiplier 0.70. Changes in a row combine by multiplying their multipliers. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions).

## N

A **natural number** is a counting number. In this book the natural numbers are $\mathbb{N} = \{0, 1, 2, \dots\}$, but many books start at 1, so check the definition in whatever you are reading. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions) and [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).

A condition Q is **necessary** for P when P can't happen without Q, which is the statement "if P, then Q". Being even is necessary for being divisible by 4. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

A **negative number** is a number less than 0, and a positive number is one greater than 0. Zero is neither, and a number that is positive or 0 is called non-negative. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions).

The **number line** is a straight line with one point marked 0, on which each number is a point: a positive number $x$ lies $x$ units to the right of 0, and $-x$ lies $x$ units to the left. Of two numbers, the one further left is smaller, so $-27 < -4$. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions).

The **numerator** of a fraction $\frac{a}{b}$ is the number on top, $a$, which says how many of the equal parts you have. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md).

## O

The **opposite** of a number $a$, written $-a$, is the number at the same distance from 0 on the other side of 0. The opposite of $-7$ is 7, so $-a$ is not always negative. Taught in [negative numbers and absolute value](../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md#definitions).

The **order of operations** is the convention for which operation comes first: grouping symbols, then exponents, then multiplication and division from left to right, then addition and subtraction from left to right. The memory aid is BEDMAS in Canada and PEMDAS in the United States, and in both the two letters of a pair have equal rank. Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#definitions).

## P

Two lines are **parallel** when they lie in the same flat surface and never meet. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#points-lines-and-angles).

A **parallelogram** is a four-sided shape with two pairs of parallel sides, like a rectangle pushed over sideways. Every square is a rectangle, and every rectangle is a parallelogram. Its area is base times height. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#polygons).

A **partial product** is one piece of a product whose factors are split by place value, such as $47 \times 30 = 1{,}410$ in $47 \times 36$. The product is the sum of its partial products. The area model draws them as the boxes of a rectangle, and the column method writes one row for each digit of the bottom factor. Taught in [multi-digit multiplication](../01-elementary/05-multi-digit-multiplication.md#definitions).

A **percent** is a ratio written per hundred: $x\%$ means $\frac{x}{100}$. So 35% is $0.35$, and 113% is $1.13$. In "the part is $x\%$ of the whole", the whole is the amount that counts as 100%, usually the noun right after "of", and $\text{part} = \frac{x}{100} \times \text{whole}$. Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md#definitions).

The **percent change** from an old value to a new one is $\frac{\text{new} - \text{old}}{\text{old}} \times 100\%$, the change measured against where you started. From \$1,600 to \$1,720 it is $\frac{120}{1600} = 7.5\%$. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions).

A **percentage point** is the unit for the plain difference between two percents. A rate that goes from 4% to 5% has risen by 1 percentage point, which is a percent change of 25%. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#percent-change-or-percentage-points) and percent change vs percentage points<!-- link: ../07-economics-math/01-measuring-the-economy/02-percent-change-vs-percentage-points.md -->.

The **perimeter** of a polygon is the total length of its sides, the distance once around it. A rectangle of length $l$ and width $w$ has perimeter $2l + 2w$. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#perimeter-area-and-volume).

Two lines are **perpendicular** when they meet at a right angle, $90^\circ$. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#points-lines-and-angles).

The **place value** of a position in a number is what one unit in that position is worth. In base 10 the places are worth 1, 10, 100 and so on from the right, each 10 times the place to its right, and after the decimal point they are worth tenths, hundredths and so on. A digit's value is the digit times its place value, so the 4 in 2,436 is worth 400. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions) and [decimals: place value, adding and subtracting](../01-elementary/12-decimals-place-value-and-adding.md#definitions).

A **polygon** is a closed flat shape made of straight line segments, called its sides, that meet only at their endpoints. A regular polygon has all its sides the same length and all its angles the same size, as a stop sign does. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#polygons).

A **power** of a number $b$ is $b^n$, the product of $n$ copies of the base $b$, read "$b$ to the power $n$". The powers of ten are $10^1 = 10$, $10^2 = 100$ and so on, and the pattern continues down to $10^0 = 1$ and $10^{-1} = 0.1$. Taught in [powers of ten](../01-elementary/14-powers-of-ten.md#definitions) and [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).

A **prime** number is an integer greater than 1 whose only positive factors are 1 and itself, such as $2, 3, 5, 7$ and $11$. The number 1 is not prime. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md) and primes and unique factorization<!-- link: ../06-cs-math/02-number-theory/03-primes-and-unique-factorization.md -->.

A **prime factorization** of a number writes it as a product of primes, with repeated factors grouped by exponents: $360 = 2^3 \times 3^2 \times 5$. By the fundamental theorem of arithmetic, every whole number greater than 1 has exactly one, apart from the order. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions).

A **proof** is an argument that shows a statement is true, where each step follows from definitions, axioms, the hypotheses or results proved earlier. Checking many examples is not a proof. Taught in what is a proof<!-- link: ../04-proofs-and-logic/01-language-and-notation/01-what-is-a-proof.md -->.

A **proportion** is an equation stating that two ratios are equal, $\frac{a}{b} = \frac{c}{d}$ with $b \ne 0$ and $d \ne 0$, read "$a$ is to $b$ as $c$ is to $d$". Cross-multiplying turns it into $ad = bc$. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#definitions).

Two quantities $x$ and $y$ are **proportional**, or directly proportional, when $y = kx$ for a nonzero constant $k$. Then $y$ is always the same multiple of $x$, and zero of one goes with zero of the other, so a taxi fare with a fixed base charge is not proportional to the distance. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#definitions).

## Q

A **quantifier** says how many elements a statement is about. "For every" ($\forall$) claims the statement for each element of a set, and "there exists" ($\exists$) claims it for at least one. Taught in quantifiers<!-- link: ../04-proofs-and-logic/02-logic-and-sets/04-quantifiers.md -->.

The **quotient** is the result of a division. In division with a remainder, $n = qd + r$, it is the whole number $q$ of times that $d$ fits into $n$. Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and [long division](../01-elementary/07-long-division.md).

## R

A **random variable** is a number whose value depends on the outcome of a random experiment, such as the total of two dice. Formally it is a function from the sample space to $\mathbb{R}$; the details are in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md -->.

The **range** of a function is the set of outputs that actually occur, $\{f(a) : a \in A\}$, also called the image. Some books use "range" to mean the codomain, so check which one is meant. In statistics, the range of a data set is its largest value minus its smallest. Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md -->.

A **rate** is a ratio of two quantities with different units, such as 90 km per hour or \$18 per hour. A unit rate gives the amount for one unit of the second quantity, and a unit price is the price for a fixed amount, such as per kilogram or per 100 g. Taught in [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions).

A **ratio** compares two quantities by division. A recipe with 2 cups of flour for every 3 cups of milk has a flour-to-milk ratio of $2 : 3$, which is the fraction $\frac{2}{3}$. The numbers 2 and 3 are the terms of the ratio, and their order matters. That ratio is part-to-part, since it compares two parts of the mix; the part-to-whole ratio of flour to mix is $2 : 5$, so flour is $\frac{2}{5}$ of the mix. Taught in [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions).

A **rational** number is one that can be written as a fraction $\frac{a}{b}$ of integers with $b \ne 0$, such as $-\frac{9}{20}$ or $7 = \frac{7}{1}$. The set of rational numbers is $\mathbb{Q}$. Every decimal that ends or repeats is rational: $0.75 = \frac{3}{4}$ and $0.333\ldots = \frac{1}{3}$. Taught in [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#definitions) and [roots, irrational numbers and types of numbers](../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md).

A **real number** is a point on the number line, rational or irrational. The set of real numbers is $\mathbb{R}$. Its formal properties are in real numbers, axioms and set notation<!-- link: ../03-high-school/01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md -->.

The **reciprocal** of a nonzero number $a$ is $\frac{1}{a}$, the number you multiply $a$ by to get 1. It is also called the multiplicative inverse. The reciprocal of $\frac{2}{3}$ is $\frac{3}{2}$, and 0 has no reciprocal. Taught in [multiplying and dividing fractions](../01-elementary/11-multiplying-and-dividing-fractions.md#definitions).

**Recursion** defines something in terms of smaller versions of itself, together with a starting case. The factorial is defined recursively: $0! = 1$, and $n! = n \cdot (n - 1)!$ for $n \ge 1$. Taught in sequences and recursion<!-- link: ../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md --> and recursive definitions and structural induction<!-- link: ../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md -->.

**Regrouping** is the step in column arithmetic that changes how a number is split among its places without changing the number, as in 52 = 5 tens + 2 ones = 4 tens + 12 ones. In addition it is called carrying, when a column adds up to 10 or more, and in subtraction it is called borrowing, when a top digit is too small. Taught in [addition and subtraction](../01-elementary/02-addition-and-subtraction.md#definitions).

Two integers are **relatively prime**, or coprime, when their greatest common factor is 1. The numbers 8 and 15 are relatively prime even though neither one is prime. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#definitions).

The **remainder** is what is left over when a division doesn't come out even. In $n = qd + r$ it is $r$, and it always satisfies $0 \le r < d$. Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#definitions) and [long division](../01-elementary/07-long-division.md).

A **repeating decimal** has a block of one or more digits that, from some place on, repeats forever. The block is written once with a bar over it: $\frac{1}{3} = 0.\overline{3}$ and $\frac{7}{12} = 0.58\overline{3}$. The decimal of every fraction either terminates or repeats. Taught in [multiplying and dividing decimals](../01-elementary/13-multiplying-and-dividing-decimals.md#definitions) and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#terminating-and-repeating-decimals).

To **round** a number to a given place is to replace it with the nearest number that has only zeros to the right of that place, so 2,436 rounded to the nearest hundred is 2,400. This book rounds an exact half up. Python's `round` uses round half to even instead, also called banker's rounding, so it sends 2,450 to 2,400 and 2,550 to 2,600. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

## S

A **scale drawing** is a drawing in which every length is the same multiple of the matching real length, and its scale is the ratio of a length in the drawing to the real length. A map scale of $1:50{,}000$ means that 1 cm on the map stands for 50,000 cm, or 0.5 km, on the ground. Taught in [proportional relationships](../02-middle-school/02-ratios-rates-percents/02-proportional-relationships.md#definitions).

A **sequence** is an ordered list of numbers $a_1, a_2, a_3, \dots$, finite or infinite. Formally it is a function whose domain is a set of natural numbers. Taught in sequences and recursion<!-- link: ../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md -->.

A **series** is the sum of the terms of a sequence, such as $1 + \frac{1}{2} + \frac{1}{4} + \dots$. An infinite series has a value only when its partial sums approach a limit, and this one approaches 2. Taught in summation notation and series<!-- link: ../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md --> and infinite series basics<!-- link: ../05-university-core/05-sequences-and-series/02-infinite-series-basics.md -->.

A **set** is a collection of distinct objects, called its elements, in which order and repeats don't matter. Most of university math is built on sets. Taught in sets and set operations<!-- link: ../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md -->.

The **sieve of Eratosthenes** finds every prime up to a limit. Write the numbers from 2 up to the limit, then again and again circle the first number that is not yet circled or crossed out, and cross out its multiples, starting from its square. Taught in [factors, multiples and primes](../01-elementary/08-factors-multiples-and-primes.md#the-sieve-of-eratosthenes).

The **sign rules** give the sign of a product or quotient of two nonzero numbers: the same signs give a positive answer, and different signs give a negative one. So $(-3) \times (-4) = 12$ and $(-12) \div 4 = -3$. They are rules for multiplication and division only, and $-3 + (-5)$ is $-8$. Taught in [integer arithmetic and sign rules](../02-middle-school/01-integers-and-rational-numbers/02-integer-arithmetic-and-sign-rules.md#definitions).

**Simple interest** is interest paid only on the amount first borrowed or saved, called the principal. A principal $P$ at an annual rate $r$ for $t$ years earns $I = Prt$, so \$2,000 at 4% earns \$80 a year. Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md#definitions) and simple interest<!-- link: ../08-financial-math/02-interest-and-growth/01-simple-interest.md -->.

A fraction is in **simplest form**, or lowest terms, when its numerator and denominator have no common factor other than 1, as in $\frac{3}{4}$. A ratio is in simplest form when its terms are whole numbers with no common factor other than 1, as in $2:5$. For a negative rational number, simplest form keeps the denominator positive: $-\frac{3}{4}$, not $\frac{3}{-4}$. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions), [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md#definitions) and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#where-the-minus-sign-goes).

To **simplify** an expression is to rewrite it as an equivalent expression with no brackets left to expand and no like terms left to combine: $3(x + 4) - 2x$ simplifies to $x + 12$. Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md#definitions).

A **solution** of an equation or inequality in one variable is a value of the variable that makes it true. The solution set is the set of all solutions, and to solve is to find all of them: $3x + 2 = 14$ has the solution set $\{4\}$. Taught in [one- and two-step equations](../02-middle-school/03-expressions-equations-inequalities/03-one-and-two-step-equations.md#definitions) and [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#definitions).

The **span** of a set of vectors is the set of all their linear combinations. Two vectors in $\mathbb{R}^3$ that don't lie on the same line through the origin span a plane through the origin. Taught in vectors, dot product and span<!-- link: ../05-university-core/06-linear-algebra/01-vectors-dot-product-and-span.md -->.

The **square** of a number $b$ is $b^2 = b \times b$, read "$b$ squared", after the area of a square. A perfect square, or square number, is the square of an integer, such as $49 = 7^2$, and it is never negative. As a shape, a square is a rectangle whose four sides are all the same length. Taught in [multiplication and times tables](../01-elementary/03-multiplication-and-times-tables.md#definitions), [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md#definitions) and [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#polygons).

A **statement**, or proposition, is a sentence that is either true or false. "7 is prime" is a statement, while "$x > 3$" is not one until you know $x$. Taught in statements and connectives<!-- link: ../04-proofs-and-logic/02-logic-and-sets/01-statements-and-connectives.md -->.

A **strict inequality** uses $<$ or $>$, so equality is left out: $5 < 5$ is false, while $5 \le 5$ is true. On a number line, the boundary of a strict inequality is drawn as an open dot, and the boundary of a non-strict one, with $\le$ or $\ge$, as a closed dot. Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#definitions).

A set $A$ is a **subset** of a set $B$, written $A \subseteq B$, when every element of $A$ is also in $B$. Every set is a subset of itself, and $\emptyset$ is a subset of every set. Taught in sets and set operations<!-- link: ../04-proofs-and-logic/02-logic-and-sets/06-sets-and-set-operations.md -->.

A condition P is **sufficient** for Q when P guarantees Q, which is the statement "if P, then Q". Being divisible by 4 is sufficient for being even. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

**Summation** notation writes a long sum compactly: $\sum_{i=1}^{n} a_i$ means $a_1 + a_2 + \dots + a_n$. Taught in summation notation and series<!-- link: ../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md -->.

A function $f \colon A \to B$ is **surjective**, or onto, when every element of $B$ is the output of at least one input, so the range equals the codomain. The squaring function from $\mathbb{R}$ to $\mathbb{R}$ is not surjective, since no real number squares to $-1$. Taught in injective, surjective and bijective<!-- link: ../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md -->.

## T

A **term** is one of the pieces added together in an expression: $3x^2 - 5x + 2$ has the three terms $3x^2$, $-5x$ and $2$. A term of a sequence is one of its entries. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md).

A **terminating decimal** has a finite number of decimal places, such as $\frac{7}{8} = 0.875$. A fraction in simplest form terminates exactly when its denominator has no prime factors other than 2 and 5. Taught in [multiplying and dividing decimals](../01-elementary/13-multiplying-and-dividing-decimals.md#definitions) and [rational number arithmetic](../02-middle-school/01-integers-and-rational-numbers/03-rational-number-arithmetic.md#terminating-and-repeating-decimals).

A **theorem** is a statement that has been proved, usually one important enough to be named or used often. Taught in definitions, theorems, lemmas and corollaries<!-- link: ../04-proofs-and-logic/01-language-and-notation/02-definitions-theorems-lemmas-corollaries.md -->.

To **truncate** a number at a given place is to replace every digit to the right of that place with 0, without looking at what those digits are. Truncating 2,996 to the tens gives 2,990, while rounding gives 3,000. For a whole number this is the same as always rounding down. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

## U

An expression is **undefined** when the rules of arithmetic give it no value, as with division by 0. No number $q$ satisfies $q \times 0 = 5$, so $5 \div 0$ is undefined. The case $0 \div 0$ fails the other way: every $q$ satisfies $q \times 0 = 0$, so there is no single answer. Taught in [division facts and remainders](../01-elementary/06-division-facts-and-remainders.md#edge-cases-and-common-mistakes).

A **unit fraction** is a fraction with numerator 1, such as $\frac{1}{8}$. Every fraction counts unit fractions: $\frac{3}{8}$ is three copies of $\frac{1}{8}$. Taught in [fractions and equivalent fractions](../01-elementary/09-fractions-and-equivalent-fractions.md#definitions).

## V

A statement "if P, then Q" is **vacuously true** when P is false, because there is no case in which it could fail. For the same reason, "every element of $\emptyset$ is even" is true. Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

A **variable** is a symbol, usually a letter, that stands for a number. The number may be one unknown value that we want to find, or it may range over a set of values. Taught in [variables and expressions](../02-middle-school/03-expressions-equations-inequalities/01-variables-and-expressions.md#definitions).

The **variance** measures how spread out values are: it is the average squared distance from the mean. For a random variable, $\operatorname{Var}(X) = E[(X - \mu)^2]$, and its square root is the standard deviation. Taught in discrete random variables<!-- link: ../05-university-core/07-probability/03-discrete-random-variables.md --> and descriptive statistics and study design<!-- link: ../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md -->.

A **vector** is a quantity with a size and a direction, written as a list of numbers such as $(3, 4)$. In linear algebra the word covers every element of a vector space. Taught in vectors in the plane<!-- link: ../03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md -->.

The **volume** of a solid is the number of unit cubes that fill it, measured in cubic units such as $\text{cm}^3$. A rectangular box has volume length times width times height. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md#perimeter-area-and-volume) and [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md).

## W

A definition is **well-defined** when it gives exactly one result and doesn't depend on choices that shouldn't matter. The rule "send the fraction $\frac{a}{b}$ to $a$" is not well-defined, because $\frac{1}{2} = \frac{2}{4}$ would be sent to both 1 and 2. The formal treatment is in functions and well-definedness<!-- link: ../04-proofs-and-logic/06-relations-and-functions/04-functions-and-well-definedness.md -->.

The **whole numbers** are 0, 1, 2, 3 and so on: the counting numbers together with zero. Taught in [place value and rounding](../01-elementary/01-place-value-and-rounding.md#definitions).

**WLOG** is short for "without loss of generality". It means the proof handles one case because the other cases work the same way, often after renaming: "WLOG, assume $a \le b$". Taught in proof language: let, suppose, WLOG<!-- link: ../04-proofs-and-logic/01-language-and-notation/03-proof-language-let-suppose-wlog.md --> and proof by cases and WLOG<!-- link: ../04-proofs-and-logic/03-core-proof-methods/04-proof-by-cases-and-wlog.md -->.

## Z

The **zero property of multiplication** says that $a \times 0 = 0$ for every number $a$. Compare it with the identity property of addition: adding 0 leaves a number alone, but multiplying by 0 gives 0. Taught in [properties of operations](../01-elementary/04-properties-of-operations.md#zero-property).
