# Integers and rational numbers

Negative numbers, the integers and the rational numbers, the rules for their signs, and the order in which an expression is worked out.

1. [Negative numbers and absolute value](01-negative-numbers-and-absolute-value.md)
2. [Integer arithmetic and sign rules](02-integer-arithmetic-and-sign-rules.md)
3. [Rational number arithmetic](03-rational-number-arithmetic.md)
4. [Exponents and order of operations](04-exponents-and-order-of-operations.md)

## Cheat sheet

### Negative numbers and absolute value

| Notation | Meaning | Example |
|---|---|---|
| $\mathbb{Z}$ | the integers, $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$ | $-7 \in \mathbb{Z}$, $2.5 \notin \mathbb{Z}$ |
| $a < b$ | $a$ is to the left of $b$ on the number line | $-9 < -4$ |
| $-a$ | the opposite of $a$: same distance from 0, other side | $-(-7) = 7$ |
| $\lvert x \rvert$ | the distance from $x$ to 0, never negative | $\lvert -6 \rvert = \lvert 6 \rvert = 6$ |
| $\lvert a - b \rvert$ | the distance between $a$ and $b$ | $\lvert 3 - 8 \rvert = 5$ |

The definition of absolute value by cases:

$$
\lvert x \rvert = \begin{cases} x & \text{if } x \ge 0, \\ -x & \text{if } x < 0. \end{cases}
$$

- Zero is neither positive nor negative. "Non-negative" means positive or 0.
- To compare two negative numbers, compare their absolute values and reverse: the bigger absolute value is the smaller number.
- Taking opposites reverses order: if $a < b$, then $-a > -b$.
- Distance by counting: if the numbers have the same sign, subtract the absolute values; if their signs are opposite, add them.
- For $d > 0$, the equation $\lvert x \rvert = d$ has two solutions, $d$ and $-d$. The equation $\lvert x \rvert = 0$ has only $x = 0$, and $\lvert x \rvert = -2$ has none.
- Truncating a negative number moves it toward 0, which makes it bigger: truncating $-3.7$ gives $-3$.

Main mistakes: reading $-27$ as bigger than $-4$; working out $\lvert 3 \rvert - \lvert 8 \rvert$ when the question is $\lvert 3 - 8 \rvert$; assuming $-x$ is negative (it is 6 when $x = -6$).

### Integer arithmetic and sign rules

| Operation | Rule | Example |
|---|---|---|
| add, same signs | add the absolute values, keep the sign | $-8 + (-5) = -13$ |
| add, different signs | subtract the absolute values, take the sign of the larger one | $-8 + 5 = -3$ |
| subtract | add the opposite: $a - b = a + (-b)$ | $6 - (-9) = 15$ |
| multiply or divide, same signs | positive | $(-6) \times (-7) = 42$ |
| multiply or divide, different signs | negative | $(-56) \div 8 = -7$ |
| many factors | even number of negatives: positive; odd: negative | $(-2)(-3)(-5) = -30$ |

- Additive inverse: $a + (-a) = 0$.
- Change is new minus old: from $-14$ to $-2$ is a change of $-2 - (-14) = 12$. Swapping the order flips the sign.
- $a - b > 0$ exactly when $a > b$.
- $(-1) \times a = -a$, so a minus sign in front of brackets can be multiplied in like a factor.
- A factor of 0 makes the product 0. Division by 0 is undefined; $0 \div (-5) = 0$.
- Division algorithm with negative $n$: $n = qd + r$ with $0 \le r < d$, so $-17 = 5 \times (-4) + 3$. Python's `divmod(-17, 5)` gives `(-4, 3)`; C and Java round the quotient toward 0 instead.

A negative times a negative is positive because of the distributive property. With the zero property it gives $a \times b + a \times (-b) = a \times (b + (-b)) = a \times 0 = 0$, so $a \times (-b) = -(a \times b)$. Using that twice gives $(-a) \times (-b) = a \times b$. Defining $(-1) \times (-1) = -1$ would make $(-1) \times (1 + (-1))$ equal both 0 and $-2$.

Main mistakes: $-3 + (-5) = 8$ (the "two negatives" rule is for multiplication and division only); $6 - (-9) = -3$ (both signs must change); old minus new for a change.

### Rational number arithmetic

- A rational number is $\frac{a}{b}$ with $a$ and $b$ integers and $b \ne 0$. The set is $\mathbb{Q}$, and every integer is in it: $-7 = \frac{-7}{1}$.
- Signs in a fraction: $-\frac{a}{b} = \frac{-a}{b} = \frac{a}{-b}$ and $\frac{-a}{-b} = \frac{a}{b}$. Simplest form has a positive denominator.
- A negative mixed number negates both parts: $-2\frac{1}{4} = -\left(2 + \frac{1}{4}\right) = -\frac{9}{4}$.
- Signed arithmetic: decide the sign with the sign rules, then use the fraction or decimal methods on the absolute values. For sums, put the signs in the numerators over a common denominator.

The denominator decides whether a fraction's decimal terminates:

| Denominator in simplest form | Decimal | Example |
|---|---|---|
| only the primes 2 and 5: $2^m \times 5^n$ | terminates after the larger of $m$ and $n$ places | $-\frac{13}{80} = -0.1625$, since $80 = 2^4 \times 5$ |
| another prime appears | repeats | $\frac{7}{30} = 0.2\overline{3}$ |

Cancel before you test: $\frac{21}{56} = \frac{3}{8} = 0.375$, even though $56$ has a factor 7.

To turn a repeating decimal into a fraction:

1. Call the number $x$.
2. If digits come before the block, multiply by a power of 10 that moves them in front of the point.
3. Multiply by $10^k$ more, where $k$ is the length of the block.
4. Subtract the two lines so the endless tails cancel, then solve for $x$ and simplify.

- $0.\overline{36}$: $100x - x = 36$, so $x = \frac{36}{99} = \frac{4}{11}$.
- $1.2\overline{7}$: $100x - 10x = 127.\overline{7} - 12.\overline{7} = 115$, so $x = \frac{115}{90} = \frac{23}{18}$.
- Nines shortcut: $0.\overline{d_1 \ldots d_k}$ is the block over $k$ nines, so $0.\overline{7} = \frac{7}{9}$ and $\frac{n}{11} = \frac{9n}{99}$, as in $\frac{4}{11} = 0.\overline{36}$.
- $0.999\ldots = 1$: $10x - x = 9$, so $9x = 9$. Every terminating decimal also has a form ending in 9s: $0.5 = 0.4\overline{9}$.
- Between two rational numbers $p < q$ lies their average $\frac{p + q}{2}$, which is rational too.
- A decimal that neither stops nor repeats is not rational: $0.1010010001\ldots$, $\sqrt{2}$, $\pi$.

Main mistakes: spreading a minus sign over a whole numerator, $-\frac{10}{12} + \frac{9}{12} \ne -\frac{19}{12}$; reading $-2\frac{1}{4}$ as $-2 + \frac{1}{4}$; treating $0.36$ as $0.\overline{36}$ (they differ by $\frac{1}{275}$); shifting by the wrong power of 10.

### Exponents and order of operations

The order of operations (BEDMAS in Canada, PEMDAS in the United States):

1. Grouping symbols, innermost first: brackets, fraction bars, absolute value bars, square roots.
2. Exponents.
3. Multiplication and division, left to right.
4. Addition and subtraction, left to right.

| Expression | Value | Why |
|---|---|---|
| $-3^2$ | $-9$ | the exponent belongs to the 3; the minus comes after |
| $(-3)^2$ | $9$ | the bracket makes $-3$ the base |
| $(-2)^5$ | $-32$ | odd power of a negative number |
| $2 \times 3^2$ | $18$ | only the 3 is squared |
| $8 \div 4 \div 2$ | $1$ | left to right, not $8 \div 2 = 4$ |
| $10 - 4 + 3$ | $9$ | left to right, not $10 - 7 = 3$ |
| $8 \div 2 \times 4$ | $16$ | division and multiplication have equal rank |
| $2^{3^2}$ | $512$ | stacked exponents from the top: $2^9$ |
| $\frac{12 + 6}{3 + 6}$ | $2$ | the bar groups; type `(12 + 6) / (3 + 6)` |

- $b^0 = 1$ for $b \ne 0$, so $(-7)^0 = 1$ but $-7^0 = -1$.
- Even powers of a negative number are positive and odd powers are negative; $(-1)^n$ alternates between 1 and $-1$.
- Exponents don't split over sums: $(3 + 4)^2 = 49$, but $3^2 + 4^2 = 25$. They do split over products: $(2 \times 3)^2 = 2^2 \times 3^2$.
- $\left(\frac{2}{3}\right)^2 = \frac{4}{9}$, while $\frac{2^2}{3} = \frac{4}{3}$.
- Squaring a number between $-1$ and 1 makes its absolute value smaller: $0.5^2 = 0.25$.
- Squares of numbers ending in 5: $35^2$ is $3 \times 4 = 12$ followed by 25, so 1225.
- Powers of 2 to know: $2^8 = 256$ and $2^{10} = 1024$.

Tools differ at a minus sign in front of a power. Python gives `-3**2 == -9` and `2**3**2 == 512`; Excel gives `=-3^2` as 9; JavaScript rejects `-3 ** 2` as a syntax error. Brackets make every tool agree.

Main mistakes: $-3^2 = 9$; multiplying before dividing in $8 \div 2 \times 4$; $(a + b)^2 = a^2 + b^2$; typing a fraction on one line without brackets.
