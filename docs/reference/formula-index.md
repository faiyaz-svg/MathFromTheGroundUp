# Formula index

Each chapter's `index.md` page is its cheat sheet: the rules, formulas and tricks of that chapter on one page, without the explanations. The elementary folder has no chapters, so its cheat sheet is the folder page itself. Cheat sheets are written together with their lessons, so they fill in as the book grows.

## Cheat sheets by folder

| Folder | What its cheat sheets cover |
|---|---|
| [Elementary](../01-elementary/index.md) | Times tables, divisibility rules, long division, fractions, decimals, unit conversion, area and volume |
| [Middle school](../02-middle-school/index.md) | Sign rules, order of operations, percents, solving equations, exponent rules, slope, geometry formulas, mean, median and mode |
| [High school](../03-high-school/index.md) | Interval notation, function transformations, factoring, the quadratic formula, logarithm rules, trigonometry, series and counting |
| [Proofs and logic](../04-proofs-and-logic/index.md) | Which proof method fits which shape of statement, negation rules, logical equivalences, induction |
| [University core](../05-university-core/index.md) | Limit laws, derivative and integral rules, series tests, matrix facts, probability rules, statistics formulas |
| [CS math](../06-cs-math/index.md) | Base conversion, two's complement, modular arithmetic, counting formulas, sums and recurrences, asymptotic notation |
| [Economics math](../07-economics-math/index.md) | Growth rates, index numbers, GDP and inflation, elasticity, marginal analysis, present value |
| [Financial math](../08-financial-math/index.md) | Interest, present and future value, annuities and loan payments, mortgage compounding, tax brackets |

Each folder page links to its chapters, and a chapter's cheat sheet is the first page of that chapter.

## Most-used formulas

Each formula below names the lesson that explains it and the cheat sheet that collects it. Letters follow the conventions in [symbols and notation](symbols-and-notation.md#one-letter-one-meaning-in-this-book).

### Division with remainder

Dividing $n$ by $d$ gives a quotient $q$ and a remainder $r$:

$$
n = qd + r, \qquad 0 \le r < d
$$

Taught in [long division](../01-elementary/07-long-division.md); collected on the [elementary folder page](../01-elementary/index.md).

### Area and volume

$$
\begin{aligned}
\text{rectangle: } & A = lw \\
\text{triangle: } & A = \tfrac{1}{2}bh \\
\text{circle: } & A = \pi r^2, \quad C = 2\pi r \\
\text{rectangular box: } & V = lwh \\
\text{cylinder: } & V = \pi r^2 h \\
\text{right triangle: } & a^2 + b^2 = c^2
\end{aligned}
$$

Here $l$, $w$ and $h$ are the length, width and height, $b$ is the base of the triangle, $r$ is the radius, $C$ is the circumference, and $c$ is the hypotenuse, the side opposite the right angle. Taught in [geometry basics: area, perimeter and volume](../01-elementary/16-geometry-basics-area-perimeter-volume.md), [area and circles](../02-middle-school/06-geometry/02-area-and-circles.md), [volume and surface area](../02-middle-school/06-geometry/03-volume-and-surface-area.md) and [the Pythagorean theorem](../02-middle-school/06-geometry/04-pythagorean-theorem.md); collected on the [elementary folder page](../01-elementary/index.md) and in the [middle school geometry cheat sheet](../02-middle-school/06-geometry/index.md).

### Percents

$$
\text{part} = \text{percent} \times \text{whole}, \qquad \text{percent change} = \frac{\text{new} - \text{old}}{\text{old}} \times 100\%
$$

Write the percent as a decimal first, so 15% of 80 is $0.15 \times 80 = 12$. A price with 13% HST added is $1.13 \times \text{price}$. Taught in [percents](../02-middle-school/02-ratios-rates-percents/03-percents.md) and [percent change and applications](../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md); collected in the [ratios, rates and percents cheat sheet](../02-middle-school/02-ratios-rates-percents/index.md).

### Exponent rules

$$
\begin{aligned}
a^m a^n &= a^{m+n} & \qquad \frac{a^m}{a^n} &= a^{m-n} \\
(a^m)^n &= a^{mn} & (ab)^n &= a^n b^n \\
a^0 &= 1 & a^{-n} &= \frac{1}{a^n} \\
a^{1/n} &= \sqrt[n]{a} & a^{m/n} &= \left(\sqrt[n]{a}\right)^m
\end{aligned}
$$

The first three rows hold for $a, b \ne 0$ and integer exponents $m$ and $n$. The last row needs $a > 0$ and $n \ge 1$. Taught in [exponent rules](../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md) and [radicals and rational exponents](../03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md); collected in the [powers, roots and real numbers cheat sheet](../02-middle-school/04-powers-roots-and-real-numbers/index.md).

### Quadratic formula

The solutions of $ax^2 + bx + c = 0$, where $a \ne 0$, are:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

The discriminant $b^2 - 4ac$ says how many real solutions there are: two if it is positive, one if it is zero, and none if it is negative. Taught in [solving quadratic equations](../03-high-school/05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md); collected in the [quadratics and complex numbers cheat sheet](../03-high-school/05-quadratics-and-complex-numbers/index.md).

### Slope and lines

The slope of the line through $(x_1, y_1)$ and $(x_2, y_2)$, where $x_1 \ne x_2$, and the slope-intercept form of the line are:

$$
m = \frac{y_2 - y_1}{x_2 - x_1}, \qquad y = mx + b
$$

Here $b$ is the $y$-intercept. The line through $(1, 2)$ and $(4, 8)$ has slope $\frac{8 - 2}{4 - 1} = 2$. Taught in [slope and linear equations](../02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md) and [forms of linear equations](../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md); collected in the [linear relationships and functions cheat sheet](../02-middle-school/05-linear-relationships-and-functions/index.md).

### Distance between two points

The distance between $(x_1, y_1)$ and $(x_2, y_2)$ is:

$$
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

It is the Pythagorean theorem applied to the horizontal and vertical gaps. The distance from $(1, 2)$ to $(4, 6)$ is $\sqrt{9 + 16} = 5$. Taught in [coordinate geometry and circles](../03-high-school/08-geometry-and-proof/04-coordinate-geometry-and-circles.md); collected in the [geometry and proof cheat sheet](../03-high-school/08-geometry-and-proof/index.md).

### Logarithm rules

The logarithm $\log_b x$ is the exponent $y$ with $b^y = x$. For $x, y > 0$, a base $b > 0$ with $b \ne 1$, and every real number $c$:

$$
\begin{aligned}
\log_b(xy) &= \log_b x + \log_b y & \qquad \log_b\!\left(\frac{x}{y}\right) &= \log_b x - \log_b y \\
\log_b(x^c) &= c \log_b x & \log_b x &= \frac{\ln x}{\ln b} \\
b^{\log_b x} &= x & \log_b(b^c) &= c
\end{aligned}
$$

There is no rule for $\log_b(x + y)$. Taught in [logarithms](../03-high-school/07-exponentials-and-logarithms/02-logarithms.md) and [logarithm properties](../03-high-school/07-exponentials-and-logarithms/03-logarithm-properties.md); collected in the [exponentials and logarithms cheat sheet](../03-high-school/07-exponentials-and-logarithms/index.md).

### Arithmetic and geometric series

$$
\begin{aligned}
1 + 2 + \dots + n &= \frac{n(n + 1)}{2} \\
a_1 + a_2 + \dots + a_n &= \frac{n(a_1 + a_n)}{2} && \text{(arithmetic: equal steps)} \\
a + ar + ar^2 + \dots + ar^{n-1} &= \frac{a(1 - r^n)}{1 - r} && (r \ne 1) \\
a + ar + ar^2 + \dots &= \frac{a}{1 - r} && (\lvert r \rvert < 1)
\end{aligned}
$$

In the geometric series, $a$ is the first term and $r$ is the common ratio. For example, $2 + 5 + 8 + 11 + 14 = \frac{5(2 + 14)}{2} = 40$, and $1 + \frac{1}{2} + \frac{1}{4} + \dots = \frac{1}{1 - 1/2} = 2$. Taught in [summation notation and series](../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md) and [infinite series basics](../05-university-core/05-sequences-and-series/02-infinite-series-basics.md); collected in the [sequences, series and counting cheat sheet](../03-high-school/11-sequences-series-and-counting/index.md).

### Binomial coefficient

The number of ways to choose $k$ items from $n$ when order doesn't matter, for $0 \le k \le n$, is:

$$
\binom{n}{k} = \frac{n!}{k!\,(n - k)!}
$$

When order matters, the count is $\frac{n!}{(n - k)!}$ instead. Choosing 2 people from 5 gives $\binom{5}{2} = 10$ pairs, and $\frac{5!}{3!} = 20$ ordered pairs. Taught in [counting: permutations and combinations](../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md); collected in the [sequences, series and counting cheat sheet](../03-high-school/11-sequences-series-and-counting/index.md).

### Compound interest

An amount $\text{PV}$ invested now at an interest rate $r$ per compounding period grows after $n$ periods to:

$$
\text{FV} = \text{PV}\,(1 + r)^n, \qquad \text{so} \qquad \text{PV} = \frac{\text{FV}}{(1 + r)^n}
$$

At 6% a year compounded monthly for 5 years, $r = \frac{0.06}{12} = 0.005$ and $n = 60$, so \$1,000 grows to about \$1,348.85. With continuous compounding at an annual rate $r$ for $t$ years, $\text{FV} = \text{PV}\,e^{rt}$. Ontario high school textbooks often write the first formula as $A = P(1 + i)^n$. Taught in compound interest<!-- link: ../08-financial-math/02-interest-and-growth/02-compound-interest.md -->, continuous compounding and e<!-- link: ../08-financial-math/02-interest-and-growth/04-continuous-compounding-and-e.md --> and present and future value<!-- link: ../08-financial-math/03-time-value-of-money/01-present-and-future-value.md -->; collected in the interest and growth cheat sheet<!-- link: ../08-financial-math/02-interest-and-growth/index.md -->.

### Loan payment

A loan of $\text{PV}$, repaid in $n$ equal payments at an interest rate $r$ per payment period, has the payment:

$$
\text{PMT} = \frac{\text{PV} \cdot r}{1 - (1 + r)^{-n}}
$$

A \$20,000 car loan at 6% a year, paid monthly over 5 years, has $r = 0.005$ and $n = 60$, so the payment is about \$386.66 a month. Canadian mortgages compound differently, and the mortgage lessons adjust $r$ for that. Taught in the loan amortization formula<!-- link: ../08-financial-math/03-time-value-of-money/03-loan-amortization-formula.md -->; collected in the time value of money cheat sheet<!-- link: ../08-financial-math/03-time-value-of-money/index.md -->.

### Derivative rules

$$
\begin{aligned}
\frac{d}{dx} x^n &= n x^{n-1} & \qquad \frac{d}{dx} e^x &= e^x & \qquad \frac{d}{dx} \ln x &= \frac{1}{x} \\
(f + g)' &= f' + g' & (cf)' &= c f' \\
(fg)' &= f'g + fg' & \left(\frac{f}{g}\right)' &= \frac{f'g - fg'}{g^2} \\
(f \circ g)'(x) &= f'(g(x))\, g'(x)
\end{aligned}
$$

The power rule also holds for every real exponent when $x > 0$, the quotient rule needs $g \ne 0$, and $c$ is a constant. The last line is the chain rule. Taught in [differentiation rules](../05-university-core/02-derivatives/02-differentiation-rules.md) and [the chain rule](../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md); collected in the [derivatives cheat sheet](../05-university-core/02-derivatives/index.md).

### Mean and variance

For data $x_1, \dots, x_n$, the sample mean and sample variance are given on the first line below. For a discrete random variable $X$, the expected value and variance are on the second.

$$
\begin{aligned}
\bar{x} &= \frac{1}{n} \sum_{i=1}^{n} x_i & \qquad s^2 &= \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2 \\
E[X] &= \sum_x x \, P(X = x) & \operatorname{Var}(X) &= E[X^2] - (E[X])^2
\end{aligned}
$$

When the data are a whole population rather than a sample, divide by $n$ instead of $n - 1$. The standard deviation is the square root of the variance. For the data 2, 4 and 9, $\bar{x} = 5$ and $s^2 = \frac{9 + 1 + 16}{2} = 13$. Taught in [describing data](../02-middle-school/07-statistics-and-probability/01-describing-data.md), [descriptive statistics and study design](../05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md) and [discrete random variables](../05-university-core/07-probability/03-discrete-random-variables.md); collected in the [probability](../05-university-core/07-probability/index.md) and [statistics](../05-university-core/08-statistics/index.md) cheat sheets.
