# Probability

Probability as a set function with three axioms, conditioning and Bayes' theorem, random variables discrete and continuous, covariance, and the two theorems that explain why averages behave.

1. [Sample spaces, events and axioms](01-sample-spaces-events-and-axioms.md)
2. [Conditional probability and Bayes' theorem](02-conditional-probability-and-bayes.md)
3. [Discrete random variables](03-discrete-random-variables.md)
4. [Continuous random variables and the normal distribution](04-continuous-random-variables-and-the-normal.md)
5. [Joint distributions, covariance and sums](05-joint-distributions-covariance-and-sums.md)
6. [The law of large numbers and the CLT](06-law-of-large-numbers-and-clt.md)

## Cheat sheet

### Sample spaces, events and axioms

A probability measure $P$ on a sample space $\Omega$ satisfies: $P(A) \ge 0$, $P(\Omega) = 1$, and $P\left(\bigcup_i A_i\right) = \sum_i P(A_i)$ for pairwise disjoint events. Events are sets, so $\cup$ is "or", $\cap$ is "and" and $A^c$ is "not".

| Rule | Statement |
|---|---|
| empty event | $P(\emptyset) = 0$ |
| complement | $P(A^c) = 1 - P(A)$ |
| monotone | $A \subseteq B$ gives $P(A) \le P(B)$ |
| two events | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| union bound | $P(A_1 \cup \cdots \cup A_n) \le \sum_i P(A_i)$ |
| equally likely | $P(A) = \frac{\lvert A \rvert}{\lvert \Omega \rvert}$ |
| uniform point in a region | $P(A) = \frac{\operatorname{area}(A)}{\operatorname{area}(\Omega)}$ |

Probability 0 does not mean impossible once $\Omega$ is infinite: each single point of a square has probability 0. Main mistakes: assuming the outcomes are equally likely without a reason (sums of two dice, two coins), adding probabilities of overlapping events, and treating "random" as one measure when the model has to say which (Bertrand's chords).

### Conditional probability and Bayes' theorem

$$
P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(A \cap B) = P(A \mid B)\,P(B), \qquad P(A) = \sum_i P(A \mid B_i)\,P(B_i).
$$

$$
P(H \mid E) = \frac{P(E \mid H)\,P(H)}{P(E \mid H)\,P(H) + P(E \mid H^c)\,P(H^c)}, \qquad \text{posterior odds} = \text{prior odds} \times \text{likelihood ratio}.
$$

Events are independent when $P(A \cap B) = P(A)\,P(B)$. Disjoint events with positive probability are dependent. Three events need all four product conditions, and pairwise independence is not enough. A medical test with 90% sensitivity and 95% specificity on a 1% condition gives $P(\text{sick} \mid \text{positive}) = \frac{2}{13} \approx 15\%$ (hypothetical numbers). Check any Bayes answer with natural frequencies: count people out of 10,000.

Main mistakes: reading $P(A \mid B)$ as $P(B \mid A)$, ignoring the base rate, dropping the denominator, and forgetting that the answer depends on how the information was obtained (Monty Hall with a host who knows gives $\frac{2}{3}$ for switching, and a blind host gives $\frac{1}{2}$).

### Discrete random variables

A random variable is a function $X \colon \Omega \to \mathbb{R}$. PMF $p_X(x) = P(X = x)$, CDF $F_X(x) = P(X \le x)$.

$$
E[X] = \sum_x x\,p_X(x), \qquad E[g(X)] = \sum_x g(x)\,p_X(x), \qquad \operatorname{Var}(X) = E[X^2] - \mu^2, \qquad \sigma = \sqrt{\operatorname{Var}(X)}.
$$

Linearity: $E[aX + bY] = aE[X] + bE[Y]$ always, with no independence needed. Indicator of an event: $E[I_A] = P(A)$. A count is a sum of indicators, so its mean is the sum of the probabilities (the expected number of fixed points of a random permutation is 1). Scaling: $\operatorname{Var}(aX + b) = a^2\operatorname{Var}(X)$.

Main mistakes: $E[X^2] \ne (E[X])^2$, using the binomial for draws without replacement, and expecting the mean to be a possible value (a die has mean 3.5).

### Continuous random variables and the normal distribution

A density $f \ge 0$ with total area 1 gives $P(a \le X \le b) = \int_a^b f$. Then $F(x) = \int_{-\infty}^x f$ and $F' = f$. Every single value has probability 0, and $f(x)$ can exceed 1. Mean $\int x f(x)\,dx$, variance $\int (x - \mu)^2 f(x)\,dx$.

Standardizing: if $X \sim N(\mu, \sigma^2)$ then $Z = \frac{X - \mu}{\sigma}$ is standard normal, and $P(X \le x) = \Phi\left(\frac{x - \mu}{\sigma}\right)$.

| $z$ | 1 | 1.645 | 1.96 | 2 | 2.576 | 3 |
|---|---|---|---|---|---|---|
| $\Phi(z)$ | 0.8413 | 0.9500 | 0.9750 | 0.9772 | 0.9950 | 0.9987 |

Within 1, 2 and 3 standard deviations of the mean: 68.3%, 95.4% and 99.7%. The exponential is memoryless: $P(X > s + t \mid X > s) = P(X > t)$, and $P(X > t) = e^{-\lambda t}$. In Python, `NormalDist(mu, sigma).cdf(x)` takes $\sigma$, not the variance.

Main mistakes: treating a density as a probability, using the variance where $\sigma$ is needed, and forgetting that a table gives the area to the left. The Cauchy density $\frac{1}{\pi(1 + x^2)}$ has no mean.

### Joint distributions, covariance and sums

Joint PMF $p(x, y)$, marginals by adding rows and columns. Independent exactly when every cell is the product of its margins.

$$
\operatorname{Cov}(X, Y) = E[XY] - E[X]E[Y], \qquad \rho = \frac{\operatorname{Cov}(X, Y)}{\sigma_X\sigma_Y} \in [-1, 1].
$$

$$
\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y).
$$

Independent variables have covariance 0 and variances that add (also for a difference). Standard deviations do not add. Two assets with returns of standard deviations $\sigma_A$ and $\sigma_B$, weights $w$ and $1 - w$, have variance $w^2\sigma_A^2 + (1 - w)^2\sigma_B^2 + 2w(1 - w)\rho\sigma_A\sigma_B$. A sum of independent normals is normal, with the means added and the variances added.

Main mistakes: concluding independence from zero covariance ($Y = X^2$), reading correlation as causation, and subtracting variances for a difference.

### The law of large numbers and the CLT

For i.i.d. $X_i$ with mean $\mu$ and variance $\sigma^2$: $E[\bar{X}_n] = \mu$ and $\operatorname{Var}(\bar{X}_n) = \frac{\sigma^2}{n}$, so the standard error is $\frac{\sigma}{\sqrt{n}}$.

| Result | Statement |
|---|---|
| Markov ($X \ge 0$) | $P(X \ge a) \le \frac{E[X]}{a}$ |
| Chebyshev | $P(\lvert X - \mu \rvert \ge k\sigma) \le \frac{1}{k^2}$ |
| weak law | $P(\lvert \bar{X}_n - \mu \rvert \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2} \to 0$ |
| CLT | $\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}}$ is approximately $N(0, 1)$ for large $n$ |
| binomial | $\text{Bin}(n, p) \approx N(np, npq)$, with a continuity correction of $\frac{1}{2}$ |

Error of an average is about $\frac{2\sigma}{\sqrt{n}}$ at 95%: one more digit of accuracy takes 100 times the samples. A poll of about 1,068 people gives a margin of $\pm 3$ points at worst.

Main mistakes: the gambler's fallacy (the next flip is still fair), reading the law as "counts even out" (the gap grows like $\sqrt{n}$), thinking the data become normal (only the average does), and applying the CLT to heavy-tailed variables without a finite variance.

### Standard distributions

| Distribution | Values | PMF or PDF | Mean | Variance |
|---|---|---|---|---|
| Bernoulli($p$) | $0, 1$ | $p^x q^{1-x}$ | $p$ | $pq$ |
| Binomial($n$, $p$) | $0, \dots, n$ | $\binom{n}{k}p^k q^{n-k}$ | $np$ | $npq$ |
| Geometric($p$) | $1, 2, \dots$ | $q^{k-1}p$ | $\frac{1}{p}$ | $\frac{q}{p^2}$ |
| Poisson($\lambda$) | $0, 1, \dots$ | $\frac{e^{-\lambda}\lambda^k}{k!}$ | $\lambda$ | $\lambda$ |
| Uniform($a$, $b$) | $[a, b]$ | $\frac{1}{b - a}$ | $\frac{a + b}{2}$ | $\frac{(b - a)^2}{12}$ |
| Exponential($\lambda$) | $[0, \infty)$ | $\lambda e^{-\lambda x}$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| Normal($\mu$, $\sigma^2$) | $(-\infty, \infty)$ | $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x - \mu)^2/(2\sigma^2)}$ | $\mu$ | $\sigma^2$ |

Here $q = 1 - p$. The binomial is a count of successes in $n$ independent trials, the geometric counts trials until the first success, and the Poisson counts rare events (it is the limit of $\text{Bin}(n, \frac{\lambda}{n})$). The exponential is the waiting time between Poisson events.
