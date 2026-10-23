# University core

Calculus, linear algebra, probability and statistics, with a light pass of multivariable calculus and differential equations.

Before this folder: High school, and the proofs and logic folder for the proof-based lessons.

## How to use this folder

Take the [diagnostic](diagnostic.md) first, with a calculator but without notes. It asks two questions on each of the 42 core lessons and one on each of the 3 optional ones, 87 in all, and its answer table names the lesson to study for each one you miss, so you can do only those lessons and skip the rest. The optional lessons are 09/01 (parametric, polar and 3D coordinates), 09/04 (double integrals) and 10/02 (second-order linear equations). Each chapter has its own cheat sheet (the links are below), and each lesson starts with a quick check, so you can test yourself before reading it.

The [Anki deck for this folder](../downloads/anki/05-university-core.apkg) holds the definitions, theorem statements with their hypotheses, derivative and integral rules, convergence tests, Taylor series, the standard distributions, the test statistics and the pairs that are easy to confuse, such as a convergent sequence and a convergent series, rank and nullity, $P(A \mid B)$ and $P(B \mid A)$, and a standard deviation and a standard error. In Anki desktop choose File, then Import, and [Anki decks](../00-start-here/index.md#anki-decks) covers phones.

## Fast path for a CS student

If you are short on time, these lessons carry the most weight in the later folders, in algorithms, machine learning, theory of computation and econometrics. They are listed in reading order, so each one only needs the ones above it.

| Lesson | Where it comes back |
|---|---|
| [The derivative definition](02-derivatives/01-the-derivative-definition.md) | marginal analysis in economics, and the gradient in machine learning |
| [Chain rule, implicit and inverse derivatives](02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md) | backpropagation, which is the chain rule applied layer by layer |
| [Optimization](03-applications-of-derivatives/05-optimization.md) | training a model, and [profit maximization and market structure](../07-economics-math/03-firms-and-consumers/03-profit-maximization-and-market-structure.md) |
| [The fundamental theorem of calculus](04-integrals/02-fundamental-theorem-of-calculus.md) | probabilities from densities, and consumer surplus |
| [Infinite series basics](05-sequences-and-series/02-infinite-series-basics.md) | the geometric series in [sums and closed forms](../06-cs-math/04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md), and [annuities and geometric series](../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md) |
| [Vectors, dot product and span](06-linear-algebra/01-vectors-dot-product-and-span.md) | embeddings, cosine similarity and every model that takes a feature vector |
| [Systems and Gaussian elimination](06-linear-algebra/02-systems-and-gaussian-elimination.md) | solving linear systems, and the $n^3$ cost that algorithm courses count |
| [Matrix algebra and inverses](06-linear-algebra/03-matrix-algebra-and-inverses.md) | [graph basics](../06-cs-math/05-graphs/01-graph-basics.md), where powers of the adjacency matrix count walks, and graphics transformations |
| [Linear independence, basis and dimension](06-linear-algebra/04-linear-independence-basis-and-dimension.md) | rank in machine learning, and when a model has redundant features |
| [Orthogonality, projections and least squares](06-linear-algebra/07-orthogonality-projections-and-least-squares.md) | linear regression, and [regression and econometrics intuition](../07-economics-math/04-more-tools/03-regression-and-econometrics-intuition.md) |
| [Eigenvalues and eigenvectors](06-linear-algebra/08-eigenvalues-and-eigenvectors.md) | PageRank, Markov chains, and [recurrences](../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md) solved by eigenvalues |
| [Conditional probability and Bayes' theorem](07-probability/02-conditional-probability-and-bayes.md) | spam filters, naive Bayes, and [discrete probability](../06-cs-math/03-counting-and-discrete-probability/05-discrete-probability.md) |
| [Discrete random variables](07-probability/03-discrete-random-variables.md) | the expected running time of randomized algorithms, and [insurance and expected value](../08-financial-math/07-taxes-insurance-and-planning/02-insurance-and-expected-value.md) |
| [Joint distributions, covariance and sums](07-probability/05-joint-distributions-covariance-and-sums.md) | [investing returns and risk](../08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk.md), and principal component analysis |
| [The law of large numbers and the CLT](07-probability/06-law-of-large-numbers-and-clt.md) | Monte Carlo methods, A/B tests and every confidence interval |
| [Confidence intervals](08-statistics/02-confidence-intervals.md) | reporting an estimate with its uncertainty, in econometrics and in model evaluation |
| [Hypothesis testing](08-statistics/03-hypothesis-testing.md) | A/B tests, and reading the p-values in a regression table |
| [Correlation and linear regression](08-statistics/04-correlation-and-linear-regression.md) | econometrics, and the first model of machine learning |
| [Partial derivatives and the gradient](09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md) | gradient descent, and marginal utility in economics |
| [Multivariable optimization and Lagrange multipliers](09-multivariable-calculus-light/03-multivariable-optimization-and-lagrange-multipliers.md) | the best bundle and the cheapest inputs, in [Lagrange multipliers, utility and cost minimization](../07-economics-math/03-firms-and-consumers/05-lagrange-multipliers-utility-and-cost-minimization.md) |

The lessons not in the table can wait. Skim the first chapter on limits if you remember the basics from high school, since later chapters mostly use the ideas and not the epsilon-delta proofs. Come back to the convergence tests when you meet the integral test or the ratio test in a course, to determinants before eigenvalues, to the integration techniques when a density needs them, and to the differential equations chapter when you reach growth models in economics or the link between Euler's method and gradient descent.

## Cheat sheet

Each chapter has a cheat sheet with the rules, tables and common mistakes of its lessons. This is the map.

- [Limits and continuity](01-limits-and-continuity/index.md#cheat-sheet) covers limit laws and the standard moves for $\frac{0}{0}$, the epsilon-delta recipe, continuity, asymptotes and the intermediate value theorem.
- [Derivatives](02-derivatives/index.md#cheat-sheet) covers the limit definition, the product, quotient and chain rules, implicit and inverse derivatives, and the table of derivatives.
- [Applications of derivatives](03-applications-of-derivatives/index.md#cheat-sheet) covers marginal analysis, linearization and L'Hopital's rule, the mean value theorem, the second derivative test and optimization.
- [Integrals](04-integrals/index.md#cheat-sheet) covers Riemann sums, the fundamental theorem, substitution, parts, partial fractions, improper integrals and the antiderivative table.
- [Sequences and series](05-sequences-and-series/index.md#cheat-sheet) covers limits of sequences, geometric and telescoping series, the convergence tests, and power and Taylor series.
- [Linear algebra](06-linear-algebra/index.md#cheat-sheet) covers dot products, elimination, matrix algebra, bases and dimension, kernel and image, determinants, least squares and eigenvalues.
- [Probability](07-probability/index.md#cheat-sheet) covers the axioms, Bayes' theorem, random variables, the normal distribution, covariance, the law of large numbers and the table of standard distributions.
- [Statistics](08-statistics/index.md#cheat-sheet) covers parameters and statistics, study design, confidence intervals, tests and their errors, and correlation and regression.
- [Multivariable calculus (light)](09-multivariable-calculus-light/index.md#cheat-sheet) covers parametric and polar curves, the gradient, the second derivative test, Lagrange multipliers and double integrals.
- [Differential equations (light)](10-differential-equations-light/index.md#cheat-sheet) covers separable, linear and logistic equations, Euler's method, and second-order equations with systems.

The results used most often in later folders are below in short form.

| Topic | The result to keep |
|---|---|
| derivative | $f'(a) = \lim_{h \to 0}\frac{f(a + h) - f(a)}{h}$, and $(f \circ g)' = f'(g)\,g'$ |
| fundamental theorem | $\int_a^b f\,dx = F(b) - F(a)$ when $F' = f$ and $f$ is continuous |
| geometric series | $\sum_{k=0}^{\infty} ar^k = \frac{a}{1 - r}$ for $\lvert r \rvert < 1$ |
| least squares | $A^TA\hat{\mathbf{x}} = A^T\mathbf{b}$ |
| eigenvalues | $\det(A - \lambda I) = 0$ |
| Bayes | $P(H \mid E) = \frac{P(E \mid H)P(H)}{P(E)}$ |
| sample mean | mean $\mu$, standard error $\frac{\sigma}{\sqrt{n}}$ |
| interval | estimate $\pm$ critical value $\times$ standard error |
| Lagrange | $\nabla f = \lambda\nabla g$ together with $g = c$ |

<!-- lessons:start -->
## Lessons

### 1. [Limits and continuity](01-limits-and-continuity/index.md)

1. [Limits, intuition and limit laws](01-limits-and-continuity/01-limits-intuition-and-limit-laws.md)
2. [The epsilon-delta definition](01-limits-and-continuity/02-epsilon-delta-definition.md)
3. [Continuity, asymptotes and the IVT](01-limits-and-continuity/03-continuity-asymptotes-and-ivt.md)

### 2. [Derivatives](02-derivatives/index.md)

1. [The derivative definition](02-derivatives/01-the-derivative-definition.md)
2. [Differentiation rules](02-derivatives/02-differentiation-rules.md)
3. [Chain rule, implicit and inverse derivatives](02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md)

### 3. [Applications of derivatives](03-applications-of-derivatives/index.md)

1. [Rates of change and marginal analysis](03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md)
2. [Linear approximation and L'Hopital's rule](03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md)
3. [The mean value theorem and extrema](03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md)
4. [Concavity and curve sketching](03-applications-of-derivatives/04-concavity-and-curve-sketching.md)
5. [Optimization](03-applications-of-derivatives/05-optimization.md)

### 4. [Integrals](04-integrals/index.md)

1. [Riemann sums and the definite integral](04-integrals/01-riemann-sums-and-the-definite-integral.md)
2. [The fundamental theorem of calculus](04-integrals/02-fundamental-theorem-of-calculus.md)
3. [U-substitution](04-integrals/03-u-substitution.md)
4. [Integration by parts and trig integrals](04-integrals/04-integration-by-parts-and-trig-integrals.md)
5. [Partial fractions and improper integrals](04-integrals/05-partial-fractions-and-improper-integrals.md)
6. [Applications of integrals](04-integrals/06-applications-of-integrals.md)

### 5. [Sequences and series](05-sequences-and-series/index.md)

1. [Sequences and their limits](05-sequences-and-series/01-sequences-and-their-limits.md)
2. [Infinite series basics](05-sequences-and-series/02-infinite-series-basics.md)
3. [Convergence tests](05-sequences-and-series/03-convergence-tests.md)
4. [Power series and Taylor series](05-sequences-and-series/04-power-series-and-taylor-series.md)

### 6. [Linear algebra](06-linear-algebra/index.md)

1. [Vectors, dot product and span](06-linear-algebra/01-vectors-dot-product-and-span.md)
2. [Systems and Gaussian elimination](06-linear-algebra/02-systems-and-gaussian-elimination.md)
3. [Matrix algebra and inverses](06-linear-algebra/03-matrix-algebra-and-inverses.md)
4. [Linear independence, basis and dimension](06-linear-algebra/04-linear-independence-basis-and-dimension.md)
5. [Linear transformations, kernel and image](06-linear-algebra/05-linear-transformations-kernel-and-image.md)
6. [Determinants](06-linear-algebra/06-determinants.md)
7. [Orthogonality, projections and least squares](06-linear-algebra/07-orthogonality-projections-and-least-squares.md)
8. [Eigenvalues and eigenvectors](06-linear-algebra/08-eigenvalues-and-eigenvectors.md)

### 7. [Probability](07-probability/index.md)

1. [Sample spaces, events and axioms](07-probability/01-sample-spaces-events-and-axioms.md)
2. [Conditional probability and Bayes' theorem](07-probability/02-conditional-probability-and-bayes.md)
3. [Discrete random variables](07-probability/03-discrete-random-variables.md)
4. [Continuous random variables and the normal distribution](07-probability/04-continuous-random-variables-and-the-normal.md)
5. [Joint distributions, covariance and sums](07-probability/05-joint-distributions-covariance-and-sums.md)
6. [The law of large numbers and the CLT](07-probability/06-law-of-large-numbers-and-clt.md)

### 8. [Statistics](08-statistics/index.md)

1. [Descriptive statistics and study design](08-statistics/01-descriptive-statistics-and-study-design.md)
2. [Confidence intervals](08-statistics/02-confidence-intervals.md)
3. [Hypothesis testing](08-statistics/03-hypothesis-testing.md)
4. [Correlation and linear regression](08-statistics/04-correlation-and-linear-regression.md)

### 9. [Multivariable calculus (light)](09-multivariable-calculus-light/index.md)

1. [Parametric, polar and 3D coordinates](09-multivariable-calculus-light/01-parametric-polar-and-3d-coordinates.md) (optional)
2. [Partial derivatives and the gradient](09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md)
3. [Multivariable optimization and Lagrange multipliers](09-multivariable-calculus-light/03-multivariable-optimization-and-lagrange-multipliers.md)
4. [Double integrals](09-multivariable-calculus-light/04-double-integrals.md) (optional)

### 10. [Differential equations (light)](10-differential-equations-light/index.md)

1. [First-order differential equations](10-differential-equations-light/01-first-order-differential-equations.md)
2. [Second-order linear equations](10-differential-equations-light/02-second-order-linear-equations.md) (optional)

<!-- lessons:end -->
