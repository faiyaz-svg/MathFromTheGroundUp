# Statistics

Summarizing data, saying how far a sample can be trusted, testing claims, and fitting lines: the tools for reading studies and for econometrics.

1. [Descriptive statistics and study design](01-descriptive-statistics-and-study-design.md)
2. [Confidence intervals](02-confidence-intervals.md)
3. [Hypothesis testing](03-hypothesis-testing.md)
4. [Correlation and linear regression](04-correlation-and-linear-regression.md)
5. [Chi-square tests](05-chi-square-tests.md)
6. [The bootstrap and permutation tests](06-bootstrap-and-permutation-tests.md)
7. [Multiple testing and p-hacking](07-multiple-testing-and-p-hacking.md)

## Cheat sheet

### Descriptive statistics and study design

A parameter describes a population ($\mu$, $\sigma$, $p$) and a statistic describes a sample ($\bar{x}$, $s$, $\hat{p}$). The sample variance divides by $n - 1$ because the deviations from $\bar{x}$ add to 0 and $\bar{x}$ sits closer to the data than $\mu$ does:

$$
s^2 = \frac{1}{n - 1}\sum (x_i - \bar{x})^2, \qquad E[s^2] = \sigma^2, \qquad z = \frac{x - \bar{x}}{s}.
$$

| Summary | Robust? | Breakdown point |
|---|---|---|
| mean, standard deviation | no | 0 |
| median | yes | $\frac{1}{2}$ |
| IQR | yes | $\frac{1}{4}$ |

Report the median and IQR for skewed data or outliers, and the mean and $s$ for symmetric data. A sample of $n$ values can't have $\lvert z \rvert$ above $\frac{n - 1}{\sqrt{n}}$, so use the IQR fences to find outliers in small samples.

Study design: random sampling lets you generalize to the population, and random assignment lets you claim a cause. An observational study can't separate the treatment from a confounder (a variable tied to both the group and the outcome). Randomization makes groups alike on every variable, recorded or not.

Main mistakes:

- Trusting a large sample that was chosen badly (Literary Digest, 1936). More data doesn't remove bias.
- Studying only what survived (survivorship bias).
- Comparing combined rates when the groups have different mixes (Simpson's paradox). Compare within groups.
- Treating a volunteer or self-selected group as a random sample.

### Confidence intervals

Every interval has the form estimate $\pm$ critical value $\times$ SE. The standard error is the standard deviation of the estimate over repeated samples, and it shrinks like $\frac{1}{\sqrt{n}}$.

| Parameter | Standard error | Interval | Critical value |
|---|---|---|---|
| mean, $\sigma$ known | $\frac{\sigma}{\sqrt{n}}$ | $\bar{x} \pm z^*\frac{\sigma}{\sqrt{n}}$ | $z^*$ |
| mean, $\sigma$ unknown | $\frac{s}{\sqrt{n}}$ | $\bar{x} \pm t^*\frac{s}{\sqrt{n}}$ | $t^*$, $n - 1$ df |
| proportion | $\sqrt{\frac{\hat{p}(1 - \hat{p})}{n}}$ | $\hat{p} \pm z^* \cdot \text{SE}$ | $z^*$ |
| difference of means | $\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$ | $(\bar{x}_1 - \bar{x}_2) \pm t^* \cdot \text{SE}$ | $t^*$, Welch df |
| slope | $\frac{s_e}{s_x\sqrt{n - 1}}$ | $b \pm t^* \cdot \text{SE}$ | $t^*$, $n - 2$ df |

Normal critical values: $z^* = 1.645, 1.960, 2.576$ for 90%, 95%, 99%. The 95% $t^*$ is 2.776 (4 df), 2.262 (9 df), 2.131 (15 df), 2.045 (29 df), approaching 1.960. Sample size for margin $E$: $n = \left(\frac{z^*\sigma}{E}\right)^2$ for a mean and $n = \left(\frac{z^*}{E}\right)^2 p(1 - p)$ for a proportion, with $p = 0.5$ as the worst case. A 95% poll of 1000 has margin about $\pm 3.1$ points, and halving the margin takes four times the sample.

The bootstrap: resample the data with replacement many times, compute the statistic each time, and take the 2.5th and 97.5th percentiles for a 95% interval. It works for medians and other awkward statistics.

Main mistakes:

- Saying "95% probability the true value is in this interval". The 95% describes the method: about 95% of intervals built this way capture the true value.
- Reading an interval for the mean as a range for individual values.
- Using $z^*$ instead of $t^*$ for a small sample with $s$.
- Forgetting that the margin of error covers only random sampling error, not bias.

### Hypothesis testing

Steps: state $H_0$ and $H_a$, choose $\alpha$, check conditions, compute the statistic, find the p-value, decide, and report the estimate with an interval. The p-value is $P(\text{result at least this extreme} \mid H_0)$. Reject when $p \le \alpha$.

| Test | Statistic | Distribution under $H_0$ |
|---|---|---|
| one mean | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ | t, $n - 1$ df |
| two means (Welch) | $t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}}$ | t, Welch df |
| paired | one-sample $t$ on the differences | t, $n - 1$ df |
| one proportion | $z = \frac{\hat{p} - p_0}{\sqrt{p_0(1 - p_0)/n}}$ | standard normal |
| two proportions | $z = \frac{\hat{p}_2 - \hat{p}_1}{\sqrt{\hat{p}(1 - \hat{p})(\frac{1}{n_1} + \frac{1}{n_2})}}$ | standard normal |
| slope | $t = \frac{b}{\text{SE}(b)}$ | t, $n - 2$ df |

| | $H_0$ true | $H_0$ false |
|---|---|---|
| reject | type I error, probability $\alpha$ | power $1 - \beta$ |
| fail to reject | correct | type II error, probability $\beta$ |

A two-sided test at level $\alpha$ rejects $\theta_0$ exactly when $\theta_0$ is outside the $(1 - \alpha)$ interval. Power rises with the effect size and $n$ and falls with variability. Sample size per group for two proportions: $n = \frac{(z_{\alpha/2} + z_\beta)^2(p_1q_1 + p_2q_2)}{(p_2 - p_1)^2}$. Among $m$ independent true-null tests, the chance of at least one false positive is $1 - (1 - \alpha)^m$, so use Bonferroni ($\frac{\alpha}{m}$) or Holm.

Main mistakes:

- Reading $p$ as the probability that $H_0$ is true, or that the result was "due to chance".
- Treating "fail to reject" as "no effect", when the test may have low power.
- Reporting the one-tail area as if it were a two-sided p-value (a two-sided p-value is twice it).
- Testing many things and reporting the one that worked (p-hacking).
- Mistaking a tiny p-value for an important effect.

### Correlation and linear regression

With centred data vectors $\mathbf{u}$ and $\mathbf{v}$, the correlation is the cosine of the angle between them, and the line is a projection:

$$
r = \frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}} = \cos\theta, \qquad b = \frac{S_{xy}}{S_{xx}} = r\frac{s_y}{s_x}, \qquad a = \bar{y} - b\bar{x}, \qquad R^2 = r^2 = 1 - \frac{\text{SSE}}{\text{SST}}.
$$

The line passes through $(\bar{x}, \bar{y})$, the residuals add to 0, and $\text{SST} = \text{SSR} + \text{SSE}$. In z-scores the line is $\hat{z}_y = r\,z_x$, which gives regression to the mean. The residual standard error is $s_e = \sqrt{\frac{\text{SSE}}{n - 2}}$. The slope is read as a difference in $y$ per unit difference in $x$ among the individuals studied.

For the slope, $\text{SE}(b) = \frac{s_e}{s_x\sqrt{n - 1}}$ and $t = \frac{b}{\text{SE}(b)}$ with $n - 2$ degrees of freedom. Multiple regression solves $A^TA\mathbf{b} = A^T\mathbf{y}$ with a column per variable. Each coefficient is the slope on what the other variables leave over, and leaving out a confounder biases a slope by (its coefficient) $\times$ (its slope on $x$).

Main mistakes:

- Reading correlation as causation, or a slope as the effect of changing $x$.
- Trusting $r$ without a plot: Anscombe's four data sets share $r = 0.816$.
- Extrapolating outside the range of $x$.
- Ignoring a high-leverage point that holds the line in place.
- Inverting the line of $y$ on $x$ to predict $x$ (the slopes multiply to $r^2$, not 1).
- Calling a drop after an extreme score a real change, when it is regression to the mean.

### Chi-square tests

The chi-square distribution with $\nu$ degrees of freedom is the distribution of $Z_1^2 + \dots + Z_\nu^2$ for independent standard normals, with mean $\nu$ and variance $2\nu$. The statistic compares observed counts $O$ with expected counts $E$, and only the upper tail counts:

$$
\chi^2 = \sum \frac{(O - E)^2}{E}.
$$

| Test | Expected count | Degrees of freedom |
|---|---|---|
| goodness of fit, $k$ categories | $E_i = np_i$ | $k - 1$ |
| independence or homogeneity, $r \times c$ table | $\frac{(\text{row total})(\text{column total})}{n}$ | $(r - 1)(c - 1)$ |

The 5% critical values are 3.841, 5.991, 7.815, 9.488 and 11.070 for 1 to 5 degrees of freedom. Conditions: counts of independent individuals, each counted once, and every expected count at least 5. With 1 degree of freedom, $\chi^2 = z^2$ for the pooled two-proportion test, and for a 2 by 2 table $\chi^2 = \frac{N(ad - bc)^2}{(a + b)(c + d)(a + c)(b + d)}$. After a rejection, look at each cell's share $\frac{(O - E)^2}{E}$ and at Cramér's V, $\sqrt{\frac{\chi^2}{n(\min(r, c) - 1)}}$, for the strength.

Main mistakes:

- Using percentages instead of counts.
- Ignoring expected counts below 5 (merge categories or use Fisher's exact test).
- Reading "significant" as "strong" or as "caused by".
- Counting one individual many times.
- Doubling the p-value, as for a two-sided z test.

### The bootstrap and permutation tests

Bootstrap: draw $n$ values with replacement from the data, recompute the statistic, repeat $B$ times, and take the 2.5th and 97.5th percentiles for a 95% interval. The bootstrap standard error of a mean is exactly $\frac{\hat{\sigma}}{\sqrt{n}}$, with $\hat{\sigma}^2$ the variance divided by $n$. Permutation test: shuffle the group labels, recompute the statistic, and use

$$
p = \frac{1 + k}{B + 1},
$$

where $k$ is the number of shuffles at least as extreme as the real split. With groups of sizes $n_1$ and $n_2$ there are $\binom{n_1 + n_2}{n_1}$ splits, which can all be listed when they are few. The p-value is valid when the splits are equally likely under $H_0$, as with random assignment. Bootstrap intervals say how big an effect is, and permutation tests say whether groups differ at all.

A resample leaves out a given value with probability $\left(1 - \frac{1}{n}\right)^n \to e^{-1} \approx 0.368$.

Main mistakes:

- Trusting the bootstrap for a maximum, a minimum or a high percentile (the resample can't go beyond the sample).
- Resampling single values from dependent data or clusters (use blocks, or resample users).
- Expecting it to rescue a tiny or biased sample.
- Reading a permutation test of means as a test of equal means when the spreads differ.
- Reporting a p-value of 0.

### Multiple testing and p-hacking

With $m$ independent true nulls at level $\alpha$, the chance of at least one false positive is $1 - (1 - \alpha)^m$ and the expected number is $m\alpha$.

| Procedure | Rule | Controls |
|---|---|---|
| Bonferroni | reject $p_i \le \frac{\alpha}{m}$ | family-wise error rate, any dependence |
| Holm | sorted; reject while $p_{(i)} \le \frac{\alpha}{m - i + 1}$, stop at the first failure | family-wise error rate |
| Benjamini-Hochberg | sorted; find the largest $k$ with $p_{(k)} \le \frac{k}{m}q$, reject ranks $1, \dots, k$ | false discovery rate, $E\left[\frac{V}{\max(R, 1)}\right] \le q$ |

BH never rejects fewer than Holm at $q = \alpha$, and Holm never rejects fewer than Bonferroni. Peeking at a running test and stopping at the first $p < 0.05$ inflates the false-positive rate (about 22% for 14 daily looks of an A/A test). Fix the sample size in advance, or use group sequential or always-valid methods. The family is everything you could have reported: outcomes, subgroups, analyses, looks and models scored on the test set. Preregistration and sample splitting reduce the number of forks.

Main mistakes:

- Counting only the tests you reported.
- Stopping at the first failure in BH.
- Reading an FDR of 5% as a 5% chance for each discovery.
- Choosing the family after the result.
- Reusing the test set to pick a model.
