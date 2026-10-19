# Common mistakes

Each entry names a classic mistake, shows the wrong and the right version, says why the right one is right, and points to the lesson that teaches the idea. Most of them have a quick test: put in a small number, or work out both sides, and the wrong version gives a different answer. The lessons also flag each mistake at the step where it happens; this page collects them in one place.

## Arithmetic and order of operations

### Squaring a negative number without brackets

Wrong: $-3^2 = 9$

Right: $-3^2 = -9$, and $(-3)^2 = 9$

Exponents come before negation, so $-3^2$ means $-(3^2)$. To square the negative number, put it in brackets. Calculators and Python follow the same rule: `-3**2` is `-9`.

Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md).

### Dividing from right to left

Wrong: $24 \div 4 \div 2 = 24 \div 2 = 12$

Right: $24 \div 4 \div 2 = 6 \div 2 = 3$

Multiplication and division have the same rank, so they are done from left to right, and the same goes for addition and subtraction. The "DM" in BEDMAS doesn't put division first, and the "MD" in PEMDAS doesn't put multiplication first: $8 \div 2 \times 4 = 4 \times 4 = 16$, not $8 \div 8 = 1$. Division isn't associative, so moving the brackets changes the answer.

Taught in [exponents and order of operations](../02-middle-school/01-integers-and-rational-numbers/04-exponents-and-order-of-operations.md) and [properties of operations](../01-elementary/04-properties-of-operations.md).

### Leaving out a zero in the quotient

Wrong: $612 \div 6 = 12$

Right: $612 \div 6 = 102$

After $6$ goes into $6$ once, the next digit brought down is $1$, which is smaller than $6$. That step still needs a digit in the quotient, so write $0$ there and bring down the $2$. The check catches the mistake: $12 \times 6 = 72$, far from $612$, while $102 \times 6 = 612$.

Taught in [long division](../01-elementary/07-long-division.md).

## Fractions, decimals and percents

### Adding the numerators and the denominators

Wrong: $\frac{1}{2} + \frac{1}{3} = \frac{2}{5}$

Right: $\frac{1}{2} + \frac{1}{3} = \frac{3}{6} + \frac{2}{6} = \frac{5}{6}$

Fractions can be added directly only when they count pieces of the same size, so rewrite them over a common denominator first. A size check shows the wrong answer can't be right: $\frac{2}{5}$ is less than $\frac{1}{2}$, but adding $\frac{1}{3}$ to $\frac{1}{2}$ has to give more than $\frac{1}{2}$.

Taught in [adding and subtracting fractions](../01-elementary/10-adding-and-subtracting-fractions.md).

### Reading half a percent as one half

Wrong: $0.5\% = 0.5$

Right: $0.5\% = \frac{0.5}{100} = 0.005$, and $0.5 = 50\%$

Percent means "divide by 100", so going between a percent and a decimal moves the point two places. A 0.5% fee on \$2,000 is \$10; read as 50%, it would be \$1,000.

Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md).

### Taking tax off by subtracting 13 percent

Wrong: a total of \$113.00 that includes 13% HST came from a price of $113 - 0.13 \times 113 = 98.31$

Right: the price before tax was $113 \div 1.13 = 100$, that is, \$100.00

The 13% was taken of the price before tax, not of the total, so the total is 113% of the price. Divide by $1.13$ to undo multiplying by $1.13$. Adding the tax back on shows the error: $1.13 \times 98.31 = 111.09$, which is not the total.

Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md) and [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).

### Adding percent changes

Wrong: a 10% rise followed by a 10% fall leaves a price where it started

Right: $100 \times 1.10 \times 0.90 = 99$, so the price ends 1% lower

Each change is a percent of a different whole: on a \$100 price, the rise is 10% of \$100 and the fall is 10% of \$110. Percent changes combine by multiplying their factors, $1.10 \times 0.90 = 0.99$, and adding the percents skips that step.

Taught in [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).

### Confusing percent change with percentage points

Wrong: an interest rate that goes from 4% to 5% has gone up by 1%

Right: it has gone up by 1 percentage point, which is a 25% increase, since $\frac{5 - 4}{4} = 0.25$

A percentage point is the plain difference between two percents. A percent change compares that difference to the starting value. News reports and economics papers use both, so check which one a sentence means.

Taught in percent change vs percentage points<!-- link: ../07-economics-math/01-measuring-the-economy/02-percent-change-vs-percentage-points.md -->.

## Exponents and roots

### Multiplying the bases when multiplying powers

Wrong: $2^3 \cdot 2^4 = 4^7$

Right: $2^3 \cdot 2^4 = 2^{3+4} = 2^7 = 128$

The product is three 2s times four 2s, which is seven 2s, so the base stays $2$ and the exponents add. The wrong answer, $4^7 = 16{,}384$, is far too big. Powers with different bases and the same exponent combine the other way: $2^3 \cdot 5^3 = 10^3$.

Taught in exponent rules<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md -->.

### Treating a negative exponent as a negative number

Wrong: $2^{-1} = -2$

Right: $2^{-1} = \frac{1}{2}$

A negative exponent means a reciprocal: $a^{-n} = \frac{1}{a^n}$ for $a \ne 0$. The pattern $2^2 = 4$, $2^1 = 2$, $2^0 = 1$ halves at each step, so the next value is $2^{-1} = \frac{1}{2}$. Every power of a positive base is positive.

Taught in exponent rules<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md -->.

### Splitting a square root over a sum

Wrong: $\sqrt{a + b} = \sqrt{a} + \sqrt{b}$

Right: $\sqrt{a + b}$ doesn't simplify in general. Products do split: $\sqrt{ab} = \sqrt{a}\,\sqrt{b}$ for $a, b \ge 0$.

Test with numbers: $\sqrt{9 + 16} = \sqrt{25} = 5$, while $\sqrt{9} + \sqrt{16} = 3 + 4 = 7$. A root, like a power, works with multiplication and not with addition.

Taught in radicals and rational exponents<!-- link: ../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md -->.

### Writing the square root of x squared as x

Wrong: $\sqrt{x^2} = x$

Right: $\sqrt{x^2} = \lvert x \rvert$

A square root is never negative, so it can't give back $x$ when $x$ is negative. With $x = -3$, the left side is $\sqrt{(-3)^2} = \sqrt{9} = 3$, which is $\lvert -3 \rvert$ and not $-3$. Watch for this step in any proof that takes the square root of both sides.

Taught in radicals and rational exponents<!-- link: ../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md -->.

### Mixing up a square root with the solutions of a square

Wrong: $\sqrt{9} = \pm 3$, or $x^2 = 9$ means $x = 3$

Right: $\sqrt{9} = 3$, and $x^2 = 9$ means $x = 3$ or $x = -3$

The symbol $\sqrt{9}$ names one number, the non-negative one. The equation $x^2 = 9$ asks for every number whose square is $9$, and there are two of them. When you solve, write $x = \pm\sqrt{9} = \pm 3$.

Taught in roots, irrationals and types of numbers<!-- link: ../02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md --> and solving quadratic equations<!-- link: ../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md -->.

## Algebra

### Squaring a sum term by term

Wrong: $(a + b)^2 = a^2 + b^2$

Right: $(a + b)^2 = a^2 + 2ab + b^2$

Squaring means multiplying $(a + b)(a + b)$, and the two cross products $ab$ and $ba$ make the middle term. Test with $a = b = 1$: the left side is $2^2 = 4$, but $a^2 + b^2 = 2$.

Taught in polynomial arithmetic<!-- link: ../03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md -->.

### Cancelling terms instead of factors

Wrong: $\frac{x + 3}{x} = 3$, by crossing out the $x$ on top and the $x$ on the bottom

Right: $\frac{x + 3}{x} = \frac{x}{x} + \frac{3}{x} = 1 + \frac{3}{x}$, for $x \ne 0$

Cancelling divides the numerator and the denominator by the same number, so it works only on a factor of the whole numerator. Here $x$ is a term of the numerator, not a factor of it. Test with $x = 1$: $\frac{1 + 3}{1} = 4$, not $3$. By contrast, $\frac{3x}{x} = 3$ for $x \ne 0$, because $x$ is a factor of $3x$.

Taught in rational expressions<!-- link: ../03-high-school/06-rational-expressions-and-equations/01-rational-expressions.md -->.

### Subtracting only the first term in brackets

Wrong: $5 - (x + 2) = 5 - x + 2$

Right: $5 - (x + 2) = 5 - x - 2 = 3 - x$

The minus sign in front of the brackets multiplies every term inside by $-1$. Test with $x = 0$: the original is $5 - 2 = 3$, the right version gives $3 - 0 = 3$, and the wrong version gives $5 - 0 + 2 = 7$.

Taught in [equivalent expressions](../02-middle-school/03-expressions-equations-inequalities/02-equivalent-expressions.md).

## Equations and inequalities

### Not flipping an inequality after multiplying by a negative

Wrong: $-2x < 6$, so $x < -3$

Right: $-2x < 6$, so $x > -3$

Multiplying or dividing both sides by a negative number reverses the order, just as $2 < 3$ but $-2 > -3$. Check with a number from the right answer: $x = 0$ satisfies $0 > -3$, and $-2 \cdot 0 = 0 < 6$ is true.

Taught in [inequalities](../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md).

### Dividing both sides by a variable that might be zero

Wrong: $x^2 = 3x$, and dividing by $x$ gives $x = 3$

Right: $x^2 - 3x = 0$, so $x(x - 3) = 0$, and $x = 0$ or $x = 3$

Dividing by $x$ is allowed only when $x \ne 0$, so it throws away the solution $x = 0$. Move every term to one side and factor instead. Both answers check: $0^2 = 3 \cdot 0$ and $3^2 = 3 \cdot 3$.

Taught in solving quadratic equations<!-- link: ../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md -->.

### Keeping every solution after squaring both sides

Wrong: $\sqrt{x + 2} = x$ has the solutions $x = 2$ and $x = -1$

Right: only $x = 2$ is a solution

Squaring gives $x + 2 = x^2$, so $x^2 - x - 2 = 0$ and $(x - 2)(x + 1) = 0$. Squaring can add solutions, because $a = b$ and $a = -b$ both turn into $a^2 = b^2$, so check each candidate in the original equation. For $x = -1$ the left side is $\sqrt{1} = 1$ and the right side is $-1$, so $-1$ is an extraneous root.

Taught in rational and radical equations<!-- link: ../03-high-school/06-rational-expressions-and-equations/03-rational-and-radical-equations.md -->.

### Multiplying an inequality by an expression of unknown sign

Wrong: $\frac{1}{x} < 2$, so $1 < 2x$, so $x > \frac{1}{2}$

Right: $\frac{1}{x} < 2$ exactly when $x < 0$ or $x > \frac{1}{2}$

Multiplying by $x$ keeps the order only when $x > 0$. For $x < 0$ the order flips and gives $1 > 2x$, which every negative $x$ satisfies. Test $x = -1$: $\frac{1}{-1} = -1 < 2$, so it is a solution the wrong method lost. Split into cases by sign, or move every term to one side and use a sign chart.

Taught in polynomial and rational inequalities<!-- link: ../03-high-school/06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md -->.

## Functions and graphs

### Reading the inverse function as a reciprocal

Wrong: $f^{-1}(x) = \frac{1}{f(x)}$

Right: $f^{-1}$ undoes $f$, so $f^{-1}(y) = x$ exactly when $f(x) = y$

For $f(x) = 2x$ the inverse is $f^{-1}(x) = \frac{x}{2}$, so $f^{-1}(4) = 2$, while $\frac{1}{f(4)} = \frac{1}{8}$. The notation invites the mix-up, because $\sin^2 x$ means $(\sin x)^2$ but $\sin^{-1} x$ means the inverse function $\arcsin x$. When you mean the reciprocal, write $\frac{1}{f(x)}$ or $(f(x))^{-1}$.

Taught in composition and inverse functions<!-- link: ../03-high-school/03-functions/05-composition-and-inverse-functions.md -->.

### Adding h outside the function

Wrong: $f(x + h) = f(x) + h$

Right: replace every $x$ in the rule with $(x + h)$. For $f(x) = x^2$, that gives $f(x + h) = (x + h)^2 = x^2 + 2xh + h^2$.

Test with $x = 3$ and $h = 1$: $f(4) = 16$, while $f(3) + 1 = 10$. The input has changed, so the whole rule applies to the new input. This substitution is the first step of every derivative worked from the definition.

Taught in what is a function<!-- link: ../03-high-school/03-functions/01-what-is-a-function.md --> and the derivative definition<!-- link: ../05-university-core/02-derivatives/01-the-derivative-definition.md -->.

### Shifting a graph the wrong way

Wrong: the graph of $y = (x - 2)^2$ is the graph of $y = x^2$ moved 2 units left

Right: it is moved 2 units right

The new graph reaches each height when $x - 2$ equals the old input, which happens 2 units further right. The lowest point of $y = (x - 2)^2$ is at $x = 2$, where $x - 2 = 0$. Subtracting inside the function moves the graph right; subtracting outside, as in $y = x^2 - 2$, moves it down.

Taught in transformations of functions<!-- link: ../03-high-school/03-functions/04-transformations-of-functions.md -->.

## Logarithms

### Splitting a logarithm over a sum

Wrong: $\log(a + b) = \log a + \log b$

Right: $\log(ab) = \log a + \log b$, and $\log(a + b)$ doesn't simplify

A logarithm turns multiplication into addition, because exponents add when you multiply powers of the same base. Test with base-10 logarithms: $\log(10 + 10) = \log 20 \approx 1.301$, while $\log 10 + \log 10 = 2$, which is $\log 100$.

Taught in logarithm properties<!-- link: ../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md -->.

### Treating a quotient of logarithms as one logarithm

Wrong: $\frac{\log 8}{\log 2} = \log 4$

Right: $\frac{\log 8}{\log 2} = \log_2 8 = 3$

A quotient of two logarithms is the change-of-base formula, $\log_b x = \frac{\log x}{\log b}$. The rule $\log \frac{x}{y} = \log x - \log y$ is about the logarithm of a quotient, which is a different thing. Check: $\log 4 \approx 0.602$ in base 10, but $\frac{\log 8}{\log 2} = 3$ in every base, since $2^3 = 8$.

Taught in logarithm properties<!-- link: ../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md -->.

## Logic and proofs

### Confusing a statement with its converse

Wrong: "if $n$ is divisible by 4, then $n$ is even" is true, so "if $n$ is even, then $n$ is divisible by 4" is true

Right: the converse is a different statement and needs its own proof. Here it is false, since $6$ is even but not divisible by $4$.

The converse of "if P, then Q" is "if Q, then P", and knowing one tells you nothing about the other. Only the contrapositive, "if not Q, then not P", is equivalent to the original.

Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md -->.

### Using the inverse in place of the contrapositive

Wrong: "if $x > 2$, then $x^2 > 4$" is equivalent to "if $x \le 2$, then $x^2 \le 4$"

Right: it is equivalent to its contrapositive, "if $x^2 \le 4$, then $x \le 2$"

The statement in the wrong line is the inverse, and it fails at $x = -3$, where $x \le 2$ but $(-3)^2 = 9 > 4$. The contrapositive negates both parts and swaps them; the inverse negates them without swapping. A proof by contrapositive has to start from "not Q".

Taught in conditionals and biconditionals<!-- link: ../04-proofs-and-logic/02-logic-and-sets/02-conditionals-and-biconditionals.md --> and contrapositive proof<!-- link: ../04-proofs-and-logic/03-core-proof-methods/05-contrapositive-proof.md -->.

### Negating a statement about every case

Wrong: the negation of "every student passed" is "no student passed"

Right: the negation is "some student did not pass"

A statement about every case is false as soon as one case fails, so its negation says that a failing case exists. In symbols, $\neg(\forall x\ P(x)) \equiv \exists x\ \neg P(x)$, and $\neg(\exists x\ P(x)) \equiv \forall x\ \neg P(x)$. The sentence "no student passed" claims much more than the negation does, and it is usually false as well.

Taught in negation and translating English<!-- link: ../04-proofs-and-logic/02-logic-and-sets/05-negation-and-translating-english.md -->.

### Proving a general claim with examples

Wrong: $n^2 + n + 41$ is prime for $n = 0, 1, 2, 3, 4$, so it is prime for every natural number $n$

Right: examples can't prove a claim about every $n$. This claim is false: for $n = 40$, $40^2 + 40 + 41 = 1681 = 41^2$.

The formula gives a prime for every $n$ from $0$ to $39$ and still fails at $40$. To prove a claim for every $n$, take an arbitrary $n$ and argue from the definitions. Examples do settle the opposite question, since one counterexample disproves a claim about every case.

Taught in common proof mistakes<!-- link: ../04-proofs-and-logic/07-putting-it-together/01-common-proof-mistakes.md --> and counterexamples and disproof<!-- link: ../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md -->.

### Assuming what you want to prove

Wrong: to prove $a^2 + b^2 \ge 2ab$, start from it, subtract $2ab$ to get $a^2 - 2ab + b^2 \ge 0$, reach $(a - b)^2 \ge 0$, and stop because that is true

Right: start from a known fact, $(a - b)^2 \ge 0$, expand it to $a^2 - 2ab + b^2 \ge 0$, and add $2ab$ to both sides to reach $a^2 + b^2 \ge 2ab$

Reaching a true statement from the claim proves nothing, because a false claim can lead to a true one: $-1 = 1$ is false, but squaring both sides gives $1 = 1$. Working backward is fine as scratch work for finding the steps. The written proof has to run forward from known facts, with each step following from the ones before it.

Taught in scratch work and proof strategies<!-- link: ../04-proofs-and-logic/03-core-proof-methods/03-scratch-work-and-proof-strategies.md -->.

### Skipping the base case in induction

Wrong: every natural number $n$ satisfies $n > n + 1$, because if $k > k + 1$, then adding 1 to both sides gives $k + 1 > k + 2$

Right: that inductive step is valid, but the claim is false, because the base case fails: $0 > 1$ is false

Induction needs both parts. The inductive step only says that each case passes its truth on to the next one, and the base case is what starts the chain. Without it, the argument above would prove a statement that is false for every $n$.

Taught in mathematical induction<!-- link: ../04-proofs-and-logic/05-induction/01-mathematical-induction.md -->.

## Counting and probability

### Multiplying probabilities of events that are not independent

Wrong: $P(A \cap B) = P(A)\,P(B)$ for every pair of events

Right: $P(A \cap B) = P(A)\,P(B \mid A)$ always, and $P(A \cap B) = P(A)\,P(B)$ only when $A$ and $B$ are independent

Roll one die, and let $A$ be "even" and $B$ be "at least 4". Then $A \cap B = \{4, 6\}$, so $P(A \cap B) = \frac{2}{6} = \frac{1}{3}$, while $P(A)\,P(B) = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$. Knowing the roll is even makes "at least 4" more likely ($\frac{2}{3}$ instead of $\frac{1}{2}$), so the events are not independent.

Taught in conditional probability and Bayes' theorem<!-- link: ../05-university-core/07-probability/02-conditional-probability-and-bayes.md -->.

### Swapping the two sides of a conditional probability

Wrong: $P(A \mid B) = P(B \mid A)$

Right: $P(A \mid B) = \frac{P(B \mid A)\,P(A)}{P(B)}$, which is Bayes' theorem, and the two sides are usually different

Draw one card from a standard deck. The probability that it is a king, given that it is a face card, is $\frac{4}{12} = \frac{1}{3}$; the probability that it is a face card, given that it is a king, is $1$. The same mistake misleads people about medical tests: a test that catches most sick people can still give mostly false alarms when the disease is rare.

Taught in conditional probability and Bayes' theorem<!-- link: ../05-university-core/07-probability/02-conditional-probability-and-bayes.md -->.

### Counting ordered choices when order doesn't matter

Wrong: the number of 2-person committees you can form from 5 people is $5 \times 4 = 20$

Right: it is $\binom{5}{2} = \frac{5 \times 4}{2} = 10$

The count $5 \times 4$ lists each committee twice, once as (Ana, Ben) and once as (Ben, Ana). Ask whether swapping two choices gives a different outcome. If it does, as with choosing a president and a vice-president, order matters and $20$ is right; if not, divide out the orderings.

Taught in counting: permutations and combinations<!-- link: ../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md -->.

### Counting the integers in a range off by one

Wrong: there are $10 - 3 = 7$ integers from 3 to 10, inclusive

Right: there are $10 - 3 + 1 = 8$

Subtracting counts the gaps between the numbers, and there is one more number than there are gaps, just as a fence with 7 gaps needs 8 posts. In general there are $b - a + 1$ integers from $a$ to $b$, inclusive. Python's `range(3, 11)` has 8 elements because it leaves out its upper end.

Taught in counting rules<!-- link: ../06-cs-math/03-counting-and-discrete-probability/01-counting-rules.md -->.

## Calculus

### Giving up on a limit that gives zero over zero

Wrong: $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$ doesn't exist, because putting in $x = 2$ gives $\frac{0}{0}$

Right: factor first. For $x \ne 2$, $\frac{x^2 - 4}{x - 2} = \frac{(x - 2)(x + 2)}{x - 2} = x + 2$, so the limit is $4$.

The form $\frac{0}{0}$ only says that substitution failed to give an answer. A limit depends on the values near $2$ and never on the value at $2$, so cancelling the factor $x - 2$, which is nonzero near $2$, is allowed.

Taught in limits: intuition and limit laws<!-- link: ../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md -->.

### Multiplying derivatives for the derivative of a product

Wrong: $\frac{d}{dx}(fg) = f'g'$

Right: $\frac{d}{dx}(fg) = f'g + fg'$

Test with $f(x) = g(x) = x$: the product is $x^2$, whose derivative is $2x$, but $f'g' = 1 \cdot 1 = 1$. The product rule gives $1 \cdot x + x \cdot 1 = 2x$. Quotients have their own rule as well, and $\left(\frac{f}{g}\right)'$ is not $\frac{f'}{g'}$.

Taught in differentiation rules<!-- link: ../05-university-core/02-derivatives/02-differentiation-rules.md -->.

### Forgetting the chain rule

Wrong: $\frac{d}{dx} \sin(3x) = \cos(3x)$

Right: $\frac{d}{dx} \sin(3x) = 3\cos(3x)$

When a function is applied to something other than plain $x$, multiply by the derivative of the inside: $\frac{d}{dx} f(g(x)) = f'(g(x))\,g'(x)$. The inside here is $3x$, with derivative $3$. In the same way, $\frac{d}{dx}(x^2 + 1)^5 = 5(x^2 + 1)^4 \cdot 2x$.

Taught in the chain rule<!-- link: ../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md -->.

### Forgetting the constant of integration

Wrong: $\int 2x\,dx = x^2$

Right: $\int 2x\,dx = x^2 + C$, where $C$ stands for an arbitrary constant

Every function $x^2 + C$ has derivative $2x$ (for example $x^2 + 7$), so the indefinite integral is the whole family. The constant matters when a condition fixes it: if $F'(x) = 2x$ and $F(0) = 5$, then $F(x) = x^2 + 5$. A definite integral has no $+C$, because it cancels in $F(b) - F(a)$.

Taught in the fundamental theorem of calculus<!-- link: ../05-university-core/04-integrals/02-fundamental-theorem-of-calculus.md -->.

## Number bases

### Reading binary remainders from the top down

Wrong: dividing 13 by 2 again and again gives the remainders 1, 0, 1, 1, so $13 = 1011_2$

Right: read the remainders from the bottom up, so $13 = 1101_2$

The first remainder is the ones digit, so it goes on the right. Check by expanding: $1101_2 = 8 + 4 + 1 = 13$, while $1011_2 = 8 + 2 + 1 = 11$.

Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).

### Numbering the places from 1 instead of 0

Wrong: $1101_2 = 2^4 + 2^3 + 2^1 = 26$

Right: $1101_2 = 2^3 + 2^2 + 2^0 = 13$

The rightmost place is $2^0 = 1$, so the exponent of each place is its position counted from $0$ at the right. A size check catches the slip: four bits hold at most $1111_2 = 15$, so 26 is too big.

Taught in [number bases and conversions](../06-cs-math/01-number-representation/01-number-bases-and-conversions.md).
