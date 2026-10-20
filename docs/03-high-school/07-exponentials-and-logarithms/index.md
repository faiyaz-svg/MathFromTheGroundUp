# Exponentials and logarithms

Growth and decay by a constant factor, the logarithm as the inverse that finds the exponent, its rules, and how to solve for time.

1. [Exponential functions and growth](01-exponential-functions-and-growth.md)
2. [Logarithms](02-logarithms.md)
3. [Logarithm properties](03-logarithm-properties.md)
4. [Exponential and logarithmic equations](04-exponential-and-logarithmic-equations.md)

## Cheat sheet

### Exponential functions and growth

An exponential function is $f(x) = a \cdot b^x$ with $a \ne 0$, $b > 0$ and $b \ne 1$. Each step of 1 in $x$ multiplies the output by $b$, and $f(x+h)/f(x) = b^h$ for every $x$. The starting value is $f(0) = a$.

| Base | Type | Percent form |
|---|---|---|
| $b > 1$ | growth | $b = 1 + r$, a rise of $r$ per step |
| $0 < b < 1$ | decay | $b = 1 - r$, a fall of $r$ per step |

- For $a > 0$ the domain is all reals, the range is $y > 0$, the $y$-intercept is $(0, a)$, and $y = 0$ is a horizontal asymptote.
- From two points, $b = \left(\frac{y_2}{y_1}\right)^{1/(x_2 - x_1)}$, then find $a$.
- Doubling time $T_d$: $A(t) = A_0 \cdot 2^{t/T_d}$. Half-life $T_h$: $A(t) = A_0 \cdot \left(\frac{1}{2}\right)^{t/T_h}$.
- Compound interest: $\text{FV} = \text{PV}(1 + r)^n$, or $\text{PV}\left(1 + \frac{r}{m}\right)^{mt}$ with $m$ periods a year. Continuous: $\text{PV}\,e^{rt}$.
- $e = \lim_{m \to \infty}\left(1 + \frac{1}{m}\right)^m \approx 2.71828$. Any $b^x$ equals $e^{kx}$ with $k = \ln b$.
- Linear growth adds the same amount per step, and exponential growth multiplies by the same factor. At 7% a year, \$1,000 passes the account that adds \$100 a year just before year 11.

Main mistakes:

- Treating growth as linear: 8% a year for 10 years is $1.08^{10} = 2.159$, a rise of 115.9%, not 80%.
- Reading $3 \cdot 2^x$ as $(3 \cdot 2)^x$.
- Using $b = r$ or $b = 1 + r$ for a decrease. A 15% fall has $b = 0.85$.
- Mixing units: a monthly rate needs $t$ in months, or the exponent $12t$.

### Logarithms

For $b > 0$, $b \ne 1$ and $x > 0$: $\log_b x = y$ exactly when $b^y = x$. The logarithm is the exponent. It is the inverse of $b^x$, so $\log_b b^x = x$ and $b^{\log_b x} = x$.

| Name | Notation | Base |
|---|---|---|
| common | $\log_{10} x$ | 10 |
| natural | $\ln x$ | $e$ |
| binary | $\log_2 x$ or $\lg x$ | 2 |

- Special values: $\log_b 1 = 0$, $\log_b b = 1$, $\log_2 \frac{1}{8} = -3$, $\log_4 32 = \frac{5}{2}$.
- To evaluate, write the argument as a power of the base, or write both as powers of a common base. Otherwise use $\log_b x = \frac{\ln x}{\ln b}$.
- Graph: the reflection of $b^x$ in $y = x$. Domain $x > 0$, range all reals, vertical asymptote $x = 0$, passes through $(1, 0)$ and $(b, 1)$. The graph of $\log_b(x - h) + k$ has domain $x > h$.
- Digits: $n$ has $\lfloor \log_{10} n \rfloor + 1$ digits, and $\lfloor \log_2 n \rfloor + 1$ bits.
- Binary search on $n$ items takes at most $\lfloor \log_2 n \rfloor + 1$ steps: 20 for a million items and 30 for a billion. $n$ distinct IDs need $\lceil \log_2 n \rceil$ bits.
- Powers of 2: $2^{10} = 1024 \approx 10^3$, so each factor of 1,000 costs about 10 bits.

Main mistakes:

- Taking the log of 0 or a negative number. There is no real answer.
- Swapping the roles when converting: $\log_5 125 = 3$ means $5^3 = 125$, not $3^5 = 125$.
- Python's `math.log(x)` is $\ln x$. Use `math.log10` and `math.log2` for the others.
- Forgetting that the domain of $\log_b(x - h)$ starts at $h$.

### Logarithm properties

For $M, N > 0$ and any real $p$, each rule comes from an exponent rule.

| Rule | Identity |
|---|---|
| product | $\log_b(MN) = \log_b M + \log_b N$ |
| quotient | $\log_b\frac{M}{N} = \log_b M - \log_b N$ |
| power | $\log_b M^p = p\log_b M$ |
| change of base | $\log_b M = \frac{\log_c M}{\log_c b}$ |

- Also $\log_b\frac{1}{N} = -\log_b N$, $\log_b\sqrt[n]{M} = \frac{1}{n}\log_b M$, $\log_b a = \frac{1}{\log_a b}$ and $\log_{b^k} M = \frac{1}{k}\log_b M$.
- Expand: roots to powers, quotient, product, then power. Condense: coefficients up as powers, sums to products, differences to quotients. Keep one base throughout.
- Condensing can add values to the domain: $\ln x^2 = 2\ln\lvert x \rvert$, and $\ln(x-1) + \ln(x-3)$ needs $x > 3$.
- Log scales: decibels $L = 10\log_{10}\frac{I}{I_0}$ (double the intensity is $+3$ dB, ten times is $+10$ dB); magnitude scales (each whole step is 10 times the amplitude and about 32 times the energy); $\text{pH} = -\log_{10}[\text{H}^+]$. On a log axis, a straight line means constant percent growth.
- A logarithm turns multiplication into addition, which is how slide rules work and why programs add log probabilities: a product of 1,000 probabilities of 0.01 underflows to 0, but $1000\ln 0.01 = -4605.17$.

Main mistakes:

- $\log(a + b) \ne \log a + \log b$. The sum of logs is $\log(ab)$.
- $\frac{\log a}{\log b} \ne \log a - \log b$. The quotient of logs is $\log_b a$, and the difference is $\log\frac{a}{b}$.
- $(\log x)^p \ne p\log x$, and $2\log x$ is $\log x^2$, not $\log 2x$.
- Combining logs with different bases.

### Exponential and logarithmic equations

To solve an exponential equation: isolate the power, then either write both sides with the same base and equate exponents, or take a log of both sides, use the power rule, and solve. Always isolate before logging: $2^x + 3 = 11$ becomes $2^x = 8$.

| Equation | Method | Answer |
|---|---|---|
| $2^{x+1} = 32$ | same base | $x = 4$ |
| $3 \cdot 2^x = 45$ | isolate, then log | $x = \log_2 15 = 3.907$ |
| $3^{2x-1} = 5^x$ | log both sides, gather $x$ | $x = \frac{\ln 3}{2\ln 3 - \ln 5} = 1.869$ |
| $e^{2x} - 5e^x + 6 = 0$ | $u = e^x$, then a quadratic | $x = \ln 2$ or $\ln 3$ |
| $\log_2 x + \log_2(x-2) = 3$ | condense, exponent form, check | $x = 4$ ($-2$ is extraneous) |

- Logarithmic equations: write the domain first, condense to one log, rewrite as a power (or equate arguments), solve, then check every candidate. Reject any that make an argument zero or negative.
- Time in compound interest: $t = \dfrac{\ln(\text{FV}/\text{PV})}{m\ln(1 + r/m)}$, and $t = \dfrac{\ln(\text{FV}/\text{PV})}{r}$ for continuous compounding. \$5,000 doubles in 17.67 years at 4% annually, 17.36 monthly and 17.33 continuously.
- Rule of 72: doubling takes about $\frac{72}{R}$ periods at $R\%$ per period. It is within 2% from 4% to 12% and exact near 8%. At 1% use 70.
- Half-life: $t = T\log_2\frac{A_0}{A}$. Carbon-14 (half-life about 5,730 years) at 30% remaining is about 9,953 years.
- Prices at 2% inflation double in 35.0 years and rise by half in 20.5 years.
- An equation $b^x = c$ has exactly one solution when $c > 0$ and none when $c \le 0$.

Main mistakes:

- Logging each term: $\ln(2^x + 3) \ne x\ln 2 + \ln 3$.
- Writing $\frac{\ln 15}{\ln 2}$ as $\ln 15 - \ln 2$.
- Skipping the domain check, which keeps extraneous solutions like $x = -2$ in the answer.
- Rounding a logarithm early: $\ln 1.003333$ rounded to $0.003$ turns 17.36 years into 19.25.
- Losing a solution: $\ln x^2 = 4$ has two, $\pm e^2$, but $2\ln x = 4$ has one.
