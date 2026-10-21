# Sequences and series

Limits of sequences, sums of infinitely many terms, the tests that decide convergence, and power series as polynomials that never stop.

1. [Sequences and their limits](01-sequences-and-their-limits.md)
2. [Infinite series basics](02-infinite-series-basics.md)
3. [Convergence tests](03-convergence-tests.md)
4. [Power series and Taylor series](04-power-series-and-taylor-series.md)

## Cheat sheet

### Sequences and their limits

$a_n \to L$ means: for every $\varepsilon > 0$ there is an $N$ such that $\lvert a_n - L \rvert < \varepsilon$ for every $n \ge N$. To prove it, simplify $\lvert a_n - L \rvert$, bound it by something like $\frac{c}{n}$, and solve for $n$. A sequence diverges to $\infty$ if it passes every ceiling for good, and oscillates if it has two different values that each recur forever, like $(-1)^n$.

Tools: the limit laws (sum, product, quotient with a nonzero limit, continuous functions), the squeeze theorem ($a_n \le b_n \le c_n$ with outer limits equal), and $f(n) \to L$ whenever $f(x) \to L$. A convergent sequence is bounded. The monotone convergence theorem says a bounded monotone sequence converges, and it fails over the rationals, so completeness of $\mathbb{R}$ is the reason.

Recursive sequence $a_{n+1} = g(a_n)$: guess, prove bounded and monotone by induction, conclude convergence, then solve $L = g(L)$ and discard roots the bounds forbid. Newton's iteration $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$ is such a sequence, and its error is roughly squared at each step.

Growth orders, for $p > 0$ and $b > 1$: $\ln n \ll n^p \ll b^n \ll n! \ll n^n$. Also $r^n \to 0$ for $\lvert r \rvert < 1$.

Main mistakes:

- Solving $L = g(L)$ before proving the limit exists.
- Thinking $a_{n+1} - a_n \to 0$ makes $(a_n)$ converge ($\sqrt{n}$ does not).
- Calling a bounded sequence convergent ($(-1)^n$), or a monotone one convergent ($n$).
- Using L'Hopital's rule on a sequence instead of on $f(x)$.

### Infinite series basics

$\sum a_k = S$ means the partial sums $S_n = a_1 + \cdots + a_n$ tend to $S$. Convergence of a series is convergence of the sequence $(S_n)$. Sums and constant multiples of convergent series are convergent, and changing finitely many terms changes the sum but not convergence.

| Series | Converges when | Sum |
|---|---|---|
| geometric $\sum_{k=0}^{\infty} a r^k$ | $\lvert r \rvert < 1$ | $\dfrac{a}{1 - r}$ (first term over one minus ratio) |
| telescoping $\sum (b_k - b_{k+1})$ | $b_k$ has a limit $B$ | $b_1 - B$ |
| harmonic $\sum \frac{1}{k}$ | never | $H_{2^m} \ge 1 + \frac{m}{2}$ |

The $n$-th term test: if $a_k \not\to 0$ the series diverges. The converse is false (harmonic series). Applications: a retry loop with success probability $p$ takes $\frac{1}{p}$ attempts on average, a perpetuity paying $C$ per year at rate $r$ is worth $\frac{C}{r}$, and a deposit $D$ with reserve ratio $\rho$ multiplies to $\frac{D}{\rho}$ in the textbook model.

Rearranging a conditionally convergent series can change its sum to any value (Riemann), so only rearrange absolutely convergent series.

Main mistakes:

- Using $\frac{a}{1 - r}$ with $\lvert r \rvert \ge 1$, or with the wrong first term.
- Believing terms tending to 0 forces convergence.
- Splitting $\sum (a_k + b_k)$ when the pieces diverge, or regrouping a divergent series.

### Convergence tests

For non-negative terms, convergence is the same as bounded partial sums. The standard tests:

| Test | Statement | Use when |
|---|---|---|
| $n$-th term | $a_k \not\to 0$ implies divergence | always check first |
| $p$-series | $\sum k^{-p}$ converges iff $p > 1$ | yardstick for comparison |
| comparison | $0 \le a_k \le b_k$: $\sum b_k$ converges implies $\sum a_k$ converges; $\sum a_k$ diverges implies $\sum b_k$ diverges | an obvious bigger or smaller series |
| limit comparison | $\frac{a_k}{b_k} \to c \in (0, \infty)$: same behaviour | rational or algebraic terms |
| integral | $f$ positive, decreasing, $a_k = f(k)$: series and $\int_1^\infty f$ converge together | terms like $\frac{1}{k\ln k}$ |
| ratio | $\lvert a_{k+1}/a_k \rvert \to L$: $L < 1$ converges, $L > 1$ diverges, $L = 1$ no information | factorials, exponentials |
| root | $\lvert a_k \rvert^{1/k} \to L$: same thresholds | $k$-th powers |
| alternating | $b_k$ decreasing to 0: $\sum (-1)^{k-1} b_k$ converges, error at most $b_{n+1}$ | alternating signs |

Absolutely convergent ($\sum \lvert a_k \rvert$ converges) implies convergent. Conditionally convergent means $\sum a_k$ converges but $\sum \lvert a_k \rvert$ does not. The integral test gives $\int_{n+1}^{\infty} f \le R_n \le \int_n^{\infty} f$. Harmonic numbers satisfy $\ln(n + 1) \le H_n \le 1 + \ln n$ and $H_n - \ln n \to \gamma \approx 0.5772$.

Order of attack: terms tend to 0? Geometric or $p$-series? Comparison for rational terms, ratio or root for factorials, exponentials and powers, integral if the function is easy to integrate, alternating test for sign changes.

Main mistakes:

- Drawing a conclusion from the ratio test when $L = 1$.
- Comparing in the wrong direction (a bigger divergent series, or a smaller convergent one, says nothing).
- Using the integral test without checking decreasing and positive.
- Applying the alternating test when $b_k$ does not tend to 0 or is not decreasing.

### Power series and Taylor series

A power series $\sum c_k (x - a)^k$ has a radius $R$: absolute convergence for $\lvert x - a \rvert < R$, divergence for $\lvert x - a \rvert > R$. If $\left\lvert\frac{c_{k+1}}{c_k}\right\rvert \to \rho$ then $R = \frac{1}{\rho}$. Check both endpoints separately.

Taylor polynomial: $T_n(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x - a)^k$, which matches $f$ and its first $n$ derivatives at $a$. $T_1$ is the linearization. Lagrange remainder: $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$ for some $c$ between $a$ and $x$, so $\lvert R_n \rvert \le \frac{M\lvert x - a \rvert^{n+1}}{(n+1)!}$ with $M$ a bound for $\lvert f^{(n+1)} \rvert$ on the interval.

| Function | Series at 0 | Interval |
|---|---|---|
| $e^x$ | $\sum \frac{x^k}{k!}$ | all $x$ |
| $\sin x$ | $\sum \frac{(-1)^k x^{2k+1}}{(2k+1)!}$ | all $x$ |
| $\cos x$ | $\sum \frac{(-1)^k x^{2k}}{(2k)!}$ | all $x$ |
| $\frac{1}{1 - x}$ | $\sum x^k$ | $(-1, 1)$ |
| $\ln(1 + x)$ | $\sum_{k \ge 1} \frac{(-1)^{k-1} x^k}{k}$ | $(-1, 1]$ |
| $\arctan x$ | $\sum \frac{(-1)^k x^{2k+1}}{2k+1}$ | $[-1, 1]$ |

Inside the radius, a power series can be differentiated and integrated term by term, with the same radius. New series come from substitution, such as $e^{-x^2}$ from $e^t$. Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ comes from putting $x = i\theta$ in the series for $e^x$. Libraries reduce the argument ($e^x = 2^m e^r$ with $\lvert r \rvert \le \frac{\ln 2}{2}$) and then evaluate a short polynomial.

Main mistakes:

- Forgetting the $k!$ in the coefficients.
- Bounding the next derivative at one end instead of over the whole interval.
- Using a series outside its interval of convergence ($\ln 3$ from the series for $\ln(1 + x)$ at $x = 2$).
- Assuming a convergent Taylor series equals the function (it does only when $R_n \to 0$).
