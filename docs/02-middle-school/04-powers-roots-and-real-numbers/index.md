# Powers, roots and real numbers

The rules for exponents, numbers written as powers of ten, square and cube roots, the sets of numbers from $\mathbb{N}$ to $\mathbb{R}$, and quick ways to estimate and check an answer.

1. [Exponent rules](01-exponent-rules.md)
2. [Scientific notation](02-scientific-notation.md)
3. [Roots, irrational numbers and types of numbers](03-roots-irrationals-and-types-of-numbers.md)
4. [Estimation and sanity checks](04-estimation-and-sanity-checks.md)

## Cheat sheet

### Exponent rules

For nonzero $a$ and $b$ and integers $m$ and $n$:

| Rule | Identity | Example |
|---|---|---|
| product | $a^m \cdot a^n = a^{m+n}$ | $2^3 \cdot 2^4 = 2^7$ |
| quotient | $\dfrac{a^m}{a^n} = a^{m-n}$ | $\dfrac{3^6}{3^2} = 3^4$ |
| power of a power | $(a^m)^n = a^{mn}$ | $(5^2)^3 = 5^6$ |
| power of a product | $(ab)^n = a^n b^n$ | $(2x)^3 = 8x^3$ |
| power of a quotient | $\left(\dfrac{a}{b}\right)^n = \dfrac{a^n}{b^n}$ | $\left(\dfrac{2}{3}\right)^2 = \dfrac{4}{9}$ |
| zero exponent | $a^0 = 1$ | $(-7)^0 = 1$ |
| negative exponent | $a^{-n} = \dfrac{1}{a^n}$ | $2^{-3} = \dfrac{1}{8}$ |

- The first three rules need the same base; the next two need the same exponent.
- A negative exponent on a fraction flips it: $\left(\frac{2}{5}\right)^{-2} = \left(\frac{5}{2}\right)^2 = \frac{25}{4}$.
- To move a factor across a fraction bar, change the sign of its exponent: $\frac{x^{-3}}{y^{-2}} = \frac{y^2}{x^3}$.
- $0^0$ is undefined in arithmetic; counting and Python use $0^0 = 1$. $0^{-n}$ is undefined.
- $2^{10} = 1024 \approx 10^3$, so $2^{20} \approx 10^6$, $2^{30} \approx 10^9$ and $2^{32} \approx 4.3 \times 10^9$. One more bit doubles the count: $2^{n+1} = 2 \cdot 2^n$.
- Growth by a rate $r$ for $n$ periods multiplies by $(1 + r)^n$; going back $n$ periods multiplies by $(1 + r)^{-n}$.

Main mistakes:

- $(a + b)^2 \ne a^2 + b^2$: $(3 + 4)^2 = 49$, but $9 + 16 = 25$.
- $a^m \cdot a^n \ne a^{mn}$: $2^3 \cdot 2^4 = 2^7$, not $2^{12}$.
- $-2^4 = -16$, while $(-2)^4 = 16$.
- $2^3 \cdot 3^2 = 72$ doesn't combine into one power. $2^3 \cdot 3^3 = 6^3$ does.
- $(2x^3)^4 = 16x^{12}$: the 2 is raised to the power 4 too.
- $2^{-1} + 3^{-1} = \frac{5}{6}$, not $5^{-1}$. Sums of powers don't combine.
- A negative exponent doesn't make a number negative: $5^{-2} = \frac{1}{25}$.

### Scientific notation

A number in scientific notation is $a \times 10^n$, with $1 \le \lvert a \rvert < 10$ and $n$ an integer. The order of magnitude is $n$.

| Task | Method | Example |
|---|---|---|
| convert | point after the first nonzero digit; count the places it moved | $0.00052 = 5.2 \times 10^{-4}$ |
| multiply | multiply coefficients, add exponents, normalize | $(6 \times 10^4)(5 \times 10^{-7}) = 3 \times 10^{-2}$ |
| divide | divide coefficients, subtract exponents, normalize | $\frac{1.496 \times 10^{11}}{2.998 \times 10^8} \approx 4.99 \times 10^2$ |
| add or subtract | match the exponents first | $4.5 \times 10^6 + 0.032 \times 10^6 = 4.532 \times 10^6$ |
| E notation | e means "times ten to the" | `1.5e-3` is $1.5 \times 10^{-3}$ |

SI prefixes, each a factor of $10^3$ apart:

| nano (n) | micro ($\mu$) | milli (m) | kilo (k) | mega (M) | giga (G) | tera (T) |
|---|---|---|---|---|---|---|
| $10^{-9}$ | $10^{-6}$ | $10^{-3}$ | $10^{3}$ | $10^{6}$ | $10^{9}$ | $10^{12}$ |

- Binary units: 1 KiB $= 2^{10}$ bytes, 1 MiB $= 2^{20}$, 1 GiB $= 2^{30}$, 1 TiB $= 2^{40}$. They are 2.4%, 4.9%, 7.4% and 10.0% bigger than kB, MB, GB and TB.
- A 1 TB drive holds $10^{12} \div 2^{30} \approx 931$ GiB, which many systems label "931 GB".
- A whole number with $d$ digits has exponent $d - 1$.
- Network speeds are in bits; file sizes are in bytes; 1 byte is 8 bits.

Main mistakes:

- Counting the zeros instead of the places: $93{,}000{,}000 = 9.3 \times 10^7$, not $10^6$.
- Adding exponents in a sum: $2 \times 10^3 + 3 \times 10^3 = 5 \times 10^3$.
- Leaving $45 \times 10^3$ unnormalized; it is $4.5 \times 10^4$.
- Reading $10^{-4}$ as negative. It is 0.0001.
- Typing `10^3` in Python, where `^` is XOR. Write `1e3` or `10**3`.

### Roots, irrational numbers and types of numbers

For $a \ge 0$, $\sqrt{a}$ is the non-negative number whose square is $a$. Every real number has one real cube root: $\sqrt[3]{-8} = -2$.

| Fact | Example |
|---|---|
| $\sqrt{a^2} = \lvert a \rvert$ for every real $a$ | $\sqrt{(-5)^2} = 5$ |
| $\sqrt{ab} = \sqrt{a}\sqrt{b}$ for $a, b \ge 0$ | $\sqrt{72} = \sqrt{36}\sqrt{2} = 6\sqrt{2}$ |
| $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$ for $a \ge 0$, $b > 0$ | $\sqrt{\frac{9}{64}} = \frac{3}{8}$ |
| like radicals add | $\sqrt{12} + \sqrt{27} = 2\sqrt{3} + 3\sqrt{3} = 5\sqrt{3}$ |
| estimate | $\sqrt{n^2 + d} \approx n + \frac{d}{2n}$, a little high: $\sqrt{40} \approx 6.33$ |

- To simplify, pull out the largest perfect square factor, then check that none is left.
- A real number is rational exactly when its decimal terminates or repeats. $\sqrt{2}$ and $\pi$ are irrational; $3.14$ and $\frac{22}{7}$ only approximate $\pi$.
- $\sqrt{n}$ for a natural number $n$ is irrational unless $n$ is a perfect square.
- The proof that $\sqrt{2}$ is irrational is by contradiction: from $\sqrt{2} = \frac{a}{b}$ in simplest form, $a^2 = 2b^2$ forces $a$ and $b$ both even.
- Rational plus irrational is irrational; irrational plus irrational can be rational ($\sqrt{2} + (-\sqrt{2}) = 0$).
- A perfect square ends in 0, 1, 4, 5, 6 or 9.

The sets nest: $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}$.

| Set | Contains | Examples |
|---|---|---|
| $\mathbb{N}$ | $0, 1, 2, \ldots$ (this book includes 0) | $0$, $7$, $\sqrt{9}$ |
| $\mathbb{Z}$ | natural numbers and their opposites | $-3$, $-12$ |
| $\mathbb{Q}$ | fractions $\frac{a}{b}$ of integers, $b \ne 0$ | $0.5$, $-\frac{2}{3}$, $0.\overline{3}$ |
| $\mathbb{R}$ | every point on the number line | $\sqrt{2}$, $\pi$, $-\sqrt{5}$ |

Main mistakes:

- $\sqrt{a + b} \ne \sqrt{a} + \sqrt{b}$: $\sqrt{9 + 16} = 5$, not 7.
- $\sqrt{9} = 3$, not $\pm 3$; the equation $x^2 = 9$ has the two solutions $\pm 3$.
- $\sqrt{x^2} = x$ fails for negative $x$.
- Stopping at $2\sqrt{45}$ instead of $6\sqrt{5}$.
- $2\sqrt{3} = \sqrt{12}$, not $\sqrt{6}$.
- In Python, `(-8) ** (1/3)` is complex; use `math.cbrt(-8)`.

### Estimation and sanity checks

| Method | How | Example |
|---|---|---|
| one significant figure | keep the first nonzero digit, rounded | $\frac{387 \times 5.2}{0.49} \approx \frac{400 \times 5}{0.5} = 4000$ |
| front-end | leading digits first, then adjust | $4{,}385 + 2{,}917 + 1{,}602 \approx 7{,}000 + 1{,}900$ |
| compatible numbers | nearby numbers that work together | $3{,}592 \div 6.2 \approx 3{,}600 \div 6 = 600$ |
| Fermi estimate | write the unknown as a product of guessable factors | $4 \times 10^7$ people times 200 bytes is about $8 \times 10^9$ bytes |

Handy facts: 86,400 seconds in a day; about $\pi \times 10^7$ seconds in a year; about $10^4$ hours in a year; about 2,000 full-time work hours in a year; $2^{10} \approx 10^3$; light goes $3 \times 10^8$ m/s; Canada has about $4 \times 10^7$ people (2026).

The checklist for any answer:

1. Units: the answer has the units the question asks for.
2. Sign: positive or negative as expected.
3. Size: close to an estimate, with a sensible order of magnitude.
4. Special cases: a formula gives the known answer at 0, 1 or an extreme.
5. Reverse operation: undo the calculation and get back the data.
6. A second method: a different route gives the same answer.

- Round one factor up and another down so the errors cancel: $48 \times 53 \approx 50 \times 50$.
- For a Fermi range, the middle of 100 and 10,000 is 1,000 (multiply, don't add).
- A product's last digit comes from the last digits of the factors. The nines check (digit sums) catches most multiplication slips.
- An error by a factor of exactly 10, 100 or 1000 is usually a decimal point or a prefix; a factor of 8 is bits and bytes; 60 or 3,600 is minutes or hours.

Main mistakes:

- Rounding 0.0416 to 0.4 instead of 0.04.
- Rounding every factor the same way when the factors sit near a boundary: $149^3$ is not about $10^6$.
- Checking by redoing the same steps, which repeats the same error.
- Estimating a difference of nearly equal numbers by rounding both to the same value.
