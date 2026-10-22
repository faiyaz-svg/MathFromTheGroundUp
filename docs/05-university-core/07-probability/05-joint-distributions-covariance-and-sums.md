# Joint distributions, covariance and sums

After this lesson you can read a joint PMF and find its marginals, test two random variables for independence, compute covariance and correlation, find the variance of a sum, explain why zero covariance does not mean independence, and use these ideas to see why diversification reduces risk.

Before this: [discrete random variables](03-discrete-random-variables.md) and [continuous random variables and the normal distribution](04-continuous-random-variables-and-the-normal.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A pair $(X, Y)$ has joint probabilities $p(0,0) = 0.2$, $p(0,1) = 0.3$, $p(1,0) = 0.2$ and $p(1,1) = 0.3$. Find the marginal PMFs of $X$ and $Y$, and decide whether $X$ and $Y$ are independent.
2. Random variables $X$ and $Y$ have $\operatorname{Var}(X) = 4$, $\operatorname{Var}(Y) = 9$ and $\operatorname{Cov}(X, Y) = -3$. Find $\operatorname{Var}(X + Y)$ and $\operatorname{Var}(X - Y)$.
3. Let $X$ be equally likely to be $-1$, $0$ or $1$, and let $Y = X^2$. Find $\operatorname{Cov}(X, Y)$. Are $X$ and $Y$ independent?

<details class="solution" markdown>
<summary>Answers</summary>

1. Add across rows and down columns: $P(X = 0) = 0.5$, $P(X = 1) = 0.5$, $P(Y = 0) = 0.4$ and $P(Y = 1) = 0.6$. Each cell equals the product of its marginals: $0.5 \cdot 0.4 = 0.2$ and $0.5 \cdot 0.6 = 0.3$. So the variables are independent.
2. $\operatorname{Var}(X + Y) = 4 + 9 + 2(-3) = 7$. $\operatorname{Var}(X - Y) = 4 + 9 - 2(-3) = 19$.
3. $E[X] = 0$, $E[Y] = \frac{2}{3}$ and $E[XY] = E[X^3] = \frac{(-1) + 0 + 1}{3} = 0$, so $\operatorname{Cov}(X, Y) = 0 - 0 = 0$. But $Y$ is a function of $X$, so they are not independent: for example $P(X = 0, Y = 1) = 0$, while $P(X = 0)P(Y = 1) = \frac{1}{3}\cdot\frac{2}{3} \ne 0$.

</details>

## The idea

A server logs the number of errors in a day and the number of customer complaints. Each count has its own distribution, but the interesting question is how the two go together: do days with many errors tend to have many complaints? The two distributions on their own can't tell you. What does is the **joint** distribution, which gives the probability of each pair of values together. From it you can recover each variable's own distribution (the marginals), tell whether knowing one variable helps you guess the other, and measure how strongly they move together.

The measure is covariance. If $X$ and $Y$ tend to be above their means at the same time, and below at the same time, the products $(X - \mu_X)(Y - \mu_Y)$ are mostly positive, and the average of these products is positive. If one tends to be high when the other is low, the average is negative. If there is no tendency, it is near zero. Dividing by the two standard deviations makes the measure unitless, between $-1$ and $1$: correlation, the number that scatter plots in the [earlier statistics lesson](../../02-middle-school/07-statistics-and-probability/03-scatter-plots-and-two-way-tables.md) were already hinting at.

Why bother with this in a lesson on probability? Because the mean and variance of a sum, which is what a total, an average or a portfolio is, depend on the covariances. Means add no matter what. Variances add only when the pieces don't move together, and when they do move together the variance of the sum is larger, and when they move in opposite directions it is smaller. That one fact explains why insurance works, why diversification works, and why the average of many measurements is more precise than one.

## Definitions

For two discrete random variables $X$ and $Y$ on the same sample space, the **joint PMF** is

$$
p(x, y) = P(X = x \text{ and } Y = y).
$$

In plain words, it lists the probability of each pair of values, usually as a table with the values of $X$ down the side and the values of $Y$ across the top. The entries are non-negative and sum to 1. The **marginal PMFs** come from adding along the rows or the columns:

$$
p_X(x) = \sum_y p(x, y), \qquad p_Y(y) = \sum_x p(x, y).
$$

The name comes from writing the sums in the margins of the table. The reason it works is the law of total probability: the events $\{Y = y\}$ partition the sample space, so $P(X = x) = \sum_y P(X = x, Y = y)$. The expected value of a function of both variables is $E[g(X, Y)] = \sum_{x, y} g(x, y)\,p(x, y)$, by the same grouping argument as in Lemma 1 of [the discrete lesson](03-discrete-random-variables.md#definitions).

Two random variables $X$ and $Y$ are **independent** if for all values $x$ and $y$,

$$
p(x, y) = p_X(x)\,p_Y(y).
$$

In plain words, the joint table is the product of its margins, so knowing the value of one variable gives no information about the other. If a single cell fails the test, they are dependent. For continuous variables the same idea uses a joint density $f(x, y)$, probabilities are double integrals over regions, the marginals are integrals of $f$ over the other variable, and independence means $f(x, y) = f_X(x)f_Y(y)$ (double integrals<!-- link: ../09-multivariable-calculus-light/04-double-integrals.md -->). The rest of this lesson is written for discrete variables, but the formulas for covariance and variance hold for both.

The **covariance** of $X$ and $Y$ is

$$
\operatorname{Cov}(X, Y) = E\bigl[(X - \mu_X)(Y - \mu_Y)\bigr].
$$

In plain words, it is the average product of the two deviations from the means. It has the units of $X$ times the units of $Y$. A positive covariance means the variables tend to be above or below their means together, and a negative one means they tend to be on opposite sides. The **correlation** is the unitless version, defined when both standard deviations are positive:

$$
\rho(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sigma_X\,\sigma_Y}.
$$

The variables are called **uncorrelated** when the covariance is 0.

## How to do it

### Working with a joint table

1. Check that the entries are non-negative and add to 1.
2. Add along rows and columns to get the marginals $p_X$ and $p_Y$.
3. Test independence: compare each cell with the product of its two marginals. One cell that fails is enough to show dependence, and a cell with probability 0 whose margins are both positive fails at once.
4. Find $E[X]$ and $E[Y]$ from the marginals, and $E[XY] = \sum xy\,p(x, y)$ from the table.
5. Find $\operatorname{Cov}(X, Y) = E[XY] - E[X]E[Y]$, then the variances (from the marginals) and $\rho$.
6. Check that $\lvert\rho\rvert \le 1$, and that the sign agrees with the pattern in the table: heavy cells on the diagonal give positive covariance.

### Rules for covariance and variance of sums

*Theorem 1 (covariance rules).* For random variables with finite variances and constants $a, b, c, d$:

- $\operatorname{Cov}(X, Y) = E[XY] - E[X]E[Y]$,
- $\operatorname{Cov}(X, Y) = \operatorname{Cov}(Y, X)$ and $\operatorname{Cov}(X, X) = \operatorname{Var}(X)$,
- $\operatorname{Cov}(aX + b,\ cY + d) = ac\,\operatorname{Cov}(X, Y)$.

We know linearity of expectation. We want three identities. The plan is to expand products and use linearity each time.

*Proof.* Expand $(X - \mu_X)(Y - \mu_Y) = XY - \mu_YX - \mu_XY + \mu_X\mu_Y$. Taking expectations term by term, $E[XY] - \mu_Y\mu_X - \mu_X\mu_Y + \mu_X\mu_Y = E[XY] - \mu_X\mu_Y$. The symmetry follows from the definition, since the product of the deviations doesn't depend on their order, and the definition with $Y = X$ is the variance. For the last rule, $aX + b$ has mean $a\mu_X + b$, so its deviation is $a(X - \mu_X)$, and likewise $c(Y - \mu_Y)$ for the second. The product of the deviations is $ac(X - \mu_X)(Y - \mu_Y)$. $\blacksquare$

Look back: the first identity is the covariance version of $\operatorname{Var}(X) = E[X^2] - \mu^2$ and is the one used in calculations. The third shows that shifting a variable doesn't change the covariance, and rescaling multiplies it by the scale factors. That is why the correlation, which divides the factors back out, is unchanged by changing units: Celsius to Fahrenheit makes no difference (if the scale factor $ac$ is positive).

*Theorem 2 (independent variables).* If $X$ and $Y$ are independent, then $E[XY] = E[X]E[Y]$, and so $\operatorname{Cov}(X, Y) = 0$.

We know the definition of independence. We want $E[XY]$ as a product of two means. The plan is to factor the double sum.

*Proof.* Take discrete variables with expected values that exist. Then

$$
E[XY] = \sum_{x, y}xy\,p(x, y) = \sum_{x, y}xy\,p_X(x)p_Y(y) = \Bigl(\sum_x x\,p_X(x)\Bigr)\Bigl(\sum_y y\,p_Y(y)\Bigr) = E[X]E[Y].
$$

By the first rule of Theorem 1, the covariance is 0. $\blacksquare$

Look back: independence implies zero covariance. The converse is false, and Example 2 shows it. The general statement is that independence is about the whole joint table and covariance is about one number computed from it, which only catches linear patterns.

*Theorem 3 (variance of a sum).* For random variables with finite variances,

$$
\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X, Y).
$$

We know the definition of variance and the covariance rules. We want the spread of a sum. The plan is to square out the deviation of the sum.

*Proof.* The mean of $X + Y$ is $\mu_X + \mu_Y$, so its deviation is $(X - \mu_X) + (Y - \mu_Y)$. Squaring and taking expectations,

$$
\operatorname{Var}(X + Y) = E\bigl[(X - \mu_X)^2\bigr] + 2E\bigl[(X - \mu_X)(Y - \mu_Y)\bigr] + E\bigl[(Y - \mu_Y)^2\bigr]. \qquad \blacksquare
$$

Look back: three consequences follow. If $X$ and $Y$ are independent (or just uncorrelated), $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$, and so does $\operatorname{Var}(X - Y)$: the variance of a difference is the sum of the variances. Applying Theorem 1 to $-Y$ gives $\operatorname{Var}(X - Y) = \operatorname{Var}(X) + \operatorname{Var}(Y) - 2\operatorname{Cov}(X, Y)$. For $n$ variables, $\operatorname{Var}\left(\sum_i X_i\right) = \sum_i\operatorname{Var}(X_i) + 2\sum_{i < j}\operatorname{Cov}(X_i, X_j)$, which follows by induction. And for independent variables the standard deviations don't add: $\sigma_{X+Y} = \sqrt{\sigma_X^2 + \sigma_Y^2}$, like the hypotenuse of a right triangle. The same formula gives a second proof that a binomial variable has variance $npq$, the result of the last lesson: the indicators of the $n$ trials are independent, each has variance $pq$, and they add.

*Theorem 4 (correlation is between $-1$ and $1$).* If $\sigma_X > 0$ and $\sigma_Y > 0$, then $-1 \le \rho(X, Y) \le 1$.

We know Theorem 3 and that a variance is never negative. We want bounds on $\rho$. The plan is to standardize both variables and look at the variance of their sum and their difference.

*Proof.* Let $U = \frac{X - \mu_X}{\sigma_X}$ and $V = \frac{Y - \mu_Y}{\sigma_Y}$. Then $E[U] = E[V] = 0$, $\operatorname{Var}(U) = \operatorname{Var}(V) = 1$, and by Theorem 1, $\operatorname{Cov}(U, V) = \frac{\operatorname{Cov}(X, Y)}{\sigma_X\sigma_Y} = \rho$. By Theorem 3, $0 \le \operatorname{Var}(U + V) = 1 + 1 + 2\rho$, so $\rho \ge -1$. Also $0 \le \operatorname{Var}(U - V) = 1 + 1 - 2\rho$, so $\rho \le 1$. $\blacksquare$

Look back: the extreme values $\pm 1$ happen exactly when $Y$ is a linear function of $X$ (Practice problem 7 proves the "if" direction of the statement for $+1$). So $\rho$ measures how close the pair is to lying on a straight line, and nothing else. A value near 0 says there is no linear tendency, and it can hide a strong curved relationship, as in Example 2.

The figure shows what three samples look like. The first has correlation close to 0.8, the second is a pair of independent variables, and the third is $Y = X^2$, where $Y$ is completely determined by $X$ and the correlation is still close to 0.

![Three scatter plots of 150 points. The first is a rising cloud with sample correlation 0.79. The second is a round cloud with sample correlation near zero, labelled independent. The third lies exactly on a parabola opening upward, labelled Y equals X squared, with sample correlation near zero.](../../assets/figures/05-university-core/joint-distributions-covariance-and-sums-scatter.svg)

## Worked examples

<div class="example" markdown>

### Example 1: a joint table

A server's day is classified by the number of errors $X$ and the number of complaints $Y$, each 0, 1 or 2 (hypothetical numbers). The joint probabilities are

| | $Y = 0$ | $Y = 1$ | $Y = 2$ | $p_X$ |
|---|---|---|---|---|
| $X = 0$ | 0.30 | 0.10 | 0.00 | 0.40 |
| $X = 1$ | 0.10 | 0.20 | 0.10 | 0.40 |
| $X = 2$ | 0.00 | 0.05 | 0.15 | 0.20 |
| $p_Y$ | 0.40 | 0.35 | 0.25 | 1 |

Find the covariance and correlation, and decide whether $X$ and $Y$ are independent.

Step 1: the entries are non-negative and add to 1. Step 2: the marginals are in the last row and column, from adding the rows and columns. Step 3: the cell $(0, 2)$ has probability 0, but $p_X(0)\,p_Y(2) = 0.4 \cdot 0.25 = 0.10$. One failing cell is enough: $X$ and $Y$ are dependent.

Step 4: $E[X] = 0.4 + 2(0.2) = 0.8$ and $E[Y] = 0.35 + 2(0.25) = 0.85$. For the product, only the cells with $x, y \ge 1$ count: $E[XY] = 1 \cdot 1(0.20) + 1 \cdot 2(0.10) + 2 \cdot 1(0.05) + 2 \cdot 2(0.15) = 0.20 + 0.20 + 0.10 + 0.60 = 1.10$.

Step 5: $\operatorname{Cov}(X, Y) = 1.10 - 0.8 \cdot 0.85 = 1.10 - 0.68 = 0.42$. The variances are $E[X^2] - 0.8^2 = (0.4 + 0.8) - 0.64 = 0.56$ and $E[Y^2] - 0.85^2 = (0.35 + 1.00) - 0.7225 = 0.6275$. So

$$
\rho = \frac{0.42}{\sqrt{0.56 \cdot 0.6275}} = \frac{0.42}{0.5928} \approx 0.709.
$$

Step 6: $\rho$ is between $-1$ and 1 and positive, as the table suggests: the heavy cells lie along the diagonal, with errors and complaints rising together. The variance of the total is $\operatorname{Var}(X + Y) = 0.56 + 0.6275 + 2(0.42) = 2.0275$, and a direct computation from the distribution of $X + Y$ (values 0 to 4 with probabilities 0.30, 0.20, 0.20, 0.15, 0.15) gives the same number: $E[(X + Y)^2] = 4.75$ and $4.75 - 1.65^2 = 2.0275$.

Note that the marginals alone could not have told you any of this: a table with the same margins but each cell equal to the product would have covariance 0.

</div>

<div class="example" markdown>

### Example 2: zero covariance without independence

Let $X$ be equally likely to be $-1$, $0$ or $1$, and let $Y = X^2$. Show that $\operatorname{Cov}(X, Y) = 0$ although $Y$ is determined by $X$. Then explain the same effect for a point chosen uniformly in the unit disc.

The joint distribution has three cells, each with probability $\frac{1}{3}$: $(-1, 1)$, $(0, 0)$ and $(1, 1)$. Then $E[X] = 0$, $E[Y] = \frac{2}{3}$ and $E[XY] = \frac{(-1)(1) + 0 + (1)(1)}{3} = 0$. So $\operatorname{Cov}(X, Y) = 0 - 0 \cdot \frac{2}{3} = 0$. The variables are uncorrelated. They are not independent: $P(X = 0, Y = 1) = 0$, while $P(X = 0)\,P(Y = 1) = \frac{1}{3}\cdot\frac{2}{3} = \frac{2}{9}$.

The reason: the relation $Y = X^2$ is symmetric about $X = 0$. When $X$ is positive, $Y$ is high, and when $X$ is negative, $Y$ is high as well, so the positive and negative deviations of $X$ cancel in the average of $(X - \mu_X)(Y - \mu_Y)$. Covariance detects the tendency to rise together or fall together along a line, and this relation is a parabola.

The same cancellation happens for a point $(X, Y)$ chosen uniformly in the unit disc. The map $(x, y) \mapsto (x, -y)$ keeps the disc, and flips the sign of $xy$, so $E[XY] = 0$, and likewise $E[X] = E[Y] = 0$, giving covariance 0. But the variables are dependent: $P(X > 0.9, Y > 0.9) = 0$, since the point $(0.9, 0.9)$ is outside the disc, while each of $P(X > 0.9)$ and $P(Y > 0.9)$ is positive. A simulation of 20,000 points gives a sample correlation of 0.001.

Check: the third panel of the figure above is Example 2's parabola, with sample correlation $-0.07$ for 150 random points, close to 0.

</div>

<div class="example" markdown>

### Example 3: a two-asset portfolio

Asset A has an expected annual return of 8% and a standard deviation of 20%. Asset B has an expected return of 6% and a standard deviation of 15%. (These numbers are hypothetical.) You put half your money in each. The returns have correlation $\rho$. Find the expected return and standard deviation of the portfolio for $\rho = 1$, $0.3$, $0$ and $-0.5$.

Step 1: the portfolio return is $R = \frac{1}{2}A + \frac{1}{2}B$. Step 2: by linearity, $E[R] = \frac{1}{2}(8\%) + \frac{1}{2}(6\%) = 7\%$ for every $\rho$.

Step 3: by Theorem 3 and the covariance rules, for a weight $w$ in A,

$$
\operatorname{Var}(R) = w^2\sigma_A^2 + (1 - w)^2\sigma_B^2 + 2w(1 - w)\rho\,\sigma_A\sigma_B.
$$

With $w = \frac{1}{2}$, $\sigma_A = 0.20$ and $\sigma_B = 0.15$, this is $0.01 + 0.005625 + 0.015\rho = 0.015625 + 0.015\rho$. So:

| $\rho$ | $\operatorname{Var}(R)$ | $\sigma_R$ |
|---|---|---|
| 1 | 0.030625 | 17.5% |
| 0.3 | 0.020125 | 14.2% |
| 0 | 0.015625 | 12.5% |
| $-0.5$ | 0.008125 | 9.0% |

For $\rho = 1$ the standard deviation is the plain average of 20% and 15%: no gain. Each lower correlation gives a lower risk for the same expected return of 7%, and with $\rho = -0.5$ the portfolio is less risky than either asset alone, which has $\sigma = 15\%$ at the least.

Step 4: the weights can be chosen. For $\rho = 0.3$, the variance is smallest at $w = \frac{\sigma_B^2 - \rho\sigma_A\sigma_B}{\sigma_A^2 + \sigma_B^2 - 2\rho\sigma_A\sigma_B} = \frac{0.0135}{0.0445} \approx 0.303$, where $\sigma_R \approx 13.6\%$ and the expected return is about 6.6%. Compared with the 50/50 mix (14.2% risk, 7% return), this gives up about 0.4 points of return for 0.6 points less risk, and the figure shows the whole curve.

![Portfolio standard deviation against the share in asset A, from 0 to 1, for four correlations. At rho equal to 1 it is a straight line from 15 to 20 percent. For rho equal to 0.3 and 0 the curves dip below 15 percent in the middle, and for rho equal to minus 0.5 the dip is deep, to about 8.5 percent near a share of 0.4.](../../assets/figures/05-university-core/joint-distributions-covariance-and-sums-portfolio.svg)

The effect goes further with many assets. Take $n$ assets that each have variance $\sigma^2$ and pairwise covariance $\rho\sigma^2$, in equal shares of $\frac{1}{n}$. By the variance-of-a-sum formula, $\operatorname{Var}(R) = n \cdot \frac{\sigma^2}{n^2} + n(n - 1)\cdot\frac{\rho\sigma^2}{n^2} = \sigma^2\left(\frac{1}{n} + \left(1 - \frac{1}{n}\right)\rho\right)$. With $\sigma = 20\%$ and $\rho = 0.3$, the standard deviation is 20% for $n = 1$, 16.1% for $n = 2$, 12.2% for $n = 10$ and 11.1% for $n = 100$. It falls toward $\sqrt{\rho}\,\sigma = 10.95\%$ and no lower: diversification removes the risk that is specific to each asset, and leaves the risk that the assets share.

Check: at $\rho = 1$ the formula gives $\sigma$ for every $n$, as it should when the assets move in lockstep. At $\rho = 0$ it gives $\frac{\sigma}{\sqrt{n}}$, the standard deviation of an average of independent variables. The real-world version of this idea is in investing returns and risk<!-- link: ../../08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk.md -->.

</div>

<div class="example" markdown>

### Example 4: sums of independent normals (finish it yourself)

A commute has two parts, a bus ride and a walk, with independent times in minutes (hypothetical): the ride is $N(25, 4^2)$ and the walk is $N(10, 3^2)$. What is the probability that the whole trip takes more than 45 minutes?

Step 1: the total is $T = R + W$. By linearity, $E[T] = 25 + 10 = 35$. Step 2: the times are independent, so by Theorem 3 the variances add: $\operatorname{Var}(T) = 16 + 9 = 25$, so $\sigma_T = 5$ minutes. The standard deviations $4$ and $3$ do not add to 7. Step 3: a sum of independent normal variables is itself normal, a fact stated here without proof, so $T \sim N(35, 5^2)$.

Now standardize $T$ at 45 and find the probability. Then find the trip time that is exceeded only 5% of the time.

<details class="solution" markdown>
<summary>Finish</summary>

The z-score of 45 is $\frac{45 - 35}{5} = 2$, so $P(T > 45) = 1 - \Phi(2) = 1 - 0.9772 = 0.0228$, about 2.3%. For the 5% point, $z = 1.645$ and $t = 35 + 1.645 \cdot 5 = 43.2$ minutes: the trip takes more than 43.2 minutes on 5% of days.

Check: a simulation of 200,000 trips gives a mean of 35.00, a standard deviation of 4.99 and $P(T > 45) = 0.0227$. Adding the standard deviations by mistake would give $\sigma = 7$, $z = 1.43$ and a probability of 7.6%, more than three times too large.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the variance of a difference is the sum of the variances, not the difference. For independent $X$ and $Y$, $\operatorname{Var}(X - Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$. The spread of a difference is at least as big as the spread of each part, because both sources of randomness feed into it. Subtracting two noisy measurements doesn't cancel the noise.

</div>

<div class="warning" markdown>

Watch out: standard deviations don't add. For independent variables with standard deviations 4 and 3, the sum has standard deviation 5, not 7. Add variances, then take the square root. The standard deviations add only when the correlation is 1.

</div>

<div class="warning" markdown>

Watch out: zero covariance does not mean independent. Example 2 has a variable that is a function of the other with covariance 0. Zero covariance rules out a linear trend and nothing else. The converse of Theorem 2 holds for one important family: if $(X, Y)$ is bivariate normal (a joint distribution built from normal variables), then uncorrelated does imply independent. That is a property of the family and not a general rule.

</div>

<div class="warning" markdown>

Watch out: correlation is not causation. Suppose temperature drives both ice-cream sales and the number of people who go swimming, and so also drownings (hypothetical model, simulated in [In code](#in-code)). Sales and drownings then have a correlation of about 0.55 in the simulation, although neither affects the other. The correlation comes from the shared cause. Taking out the part of each that temperature explains leaves residuals with correlation about 0. Correlation, even a strong one, can't tell you which way the effect goes, or whether there is one, without extra information such as a randomized experiment.

</div>

Correlation is undefined when a variable is constant, since $\sigma = 0$ puts a zero in the denominator. It also depends on the range of the data: restricting to a narrow range of $X$ (for example only the top students) usually lowers the correlation, even if the relationship is the same. And a correlation only tells you how tightly the points follow a line, not the slope: two lines with very different slopes can both have $\rho = 0.9$.

Finally, the joint table determines the marginals, but the marginals don't determine the joint table. Example 1 and the independent table with the same margins have different covariances. When a problem gives only marginals and asks for something about the pair, check whether it says the variables are independent.

## Tricks and shortcuts

To find a variance of a sum, write the covariance terms in a table. For three variables, $\operatorname{Var}(X + Y + Z)$ has three variance terms and three covariance terms, each covariance counted twice. For independent variables all the covariance terms vanish.

To find a covariance by hand, use $E[XY] - E[X]E[Y]$, not the definition. Scan the table first for zero cells and symmetric structure: cancellation like that in Example 2 often shows a covariance of 0 at a glance.

A scale-free check of correlation: a $\rho$ of $0.7$ means that $\rho^2 = 0.49$, about half of the variance of $Y$, is explained by a linear fit on $X$ (this is the coefficient of determination of the later regression lesson). So a correlation of 0.7 is a moderate relationship, and 0.3 explains under 10% of the variance.

For a portfolio, the 50/50 case with equal variances is quick: $\operatorname{Var}(R) = \frac{\sigma^2}{2}(1 + \rho)$. The risk is $\sigma\sqrt{\frac{1 + \rho}{2}}$, which is $\sigma$ at $\rho = 1$, $\frac{\sigma}{\sqrt{2}}$ at $\rho = 0$ and 0 at $\rho = -1$.

## In code

A joint table fits in a dictionary, and a few lines give the marginals, the covariance and the correlation. The code reproduces Examples 1 and 2, simulates the hidden common cause from the warning above, tabulates the portfolio of Example 3, and checks the rule for a sum of independent normals from Example 4.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import random
from statistics import correlation, mean, pstdev

# A joint PMF as a dictionary: (x, y) -> probability.
joint = {(0, 0): 0.30, (0, 1): 0.10, (0, 2): 0.00,
         (1, 0): 0.10, (1, 1): 0.20, (1, 2): 0.10,
         (2, 0): 0.00, (2, 1): 0.05, (2, 2): 0.15}
px = {x: sum(p for (a, b), p in joint.items() if a == x) for x in range(3)}
py = {y: sum(p for (a, b), p in joint.items() if b == y) for y in range(3)}
ex = sum(x * p for x, p in px.items())
ey = sum(y * p for y, p in py.items())
exy = sum(x * y * p for (x, y), p in joint.items())
varx = sum(x * x * p for x, p in px.items()) - ex**2
vary = sum(y * y * p for y, p in py.items()) - ey**2
cov = exy - ex * ey
print(round(ex, 2), round(ey, 2), round(exy, 2), round(cov, 2))      # 0.8 0.85 1.1 0.42
print(round(cov / math.sqrt(varx * vary), 4))                        # 0.7085
print(round(varx + vary + 2 * cov, 4))                               # 2.0275

# Zero covariance without independence: X uniform on {-1, 0, 1}, Y = X^2.
pairs = [(x, x * x) for x in (-1, 0, 1)]
e_x = sum(x for x, _ in pairs) / 3
e_y = sum(y for _, y in pairs) / 3
print(sum(x * y for x, y in pairs) / 3 - e_x * e_y)                  # 0.0

# A hidden common cause: temperature drives both sales and drownings (hypothetical model).
random.seed(2026)
temp = [random.gauss(20, 5) for _ in range(1000)]
sales = [10 * t + random.gauss(0, 30) for t in temp]
drown = [0.5 * t + random.gauss(0, 3) for t in temp]
print(round(correlation(sales, drown), 3))                           # 0.553

# Two-asset portfolio: standard deviation for a weight w in A.
def portfolio_sd(w, rho, sa=0.20, sb=0.15):
    return math.sqrt(w**2 * sa**2 + (1 - w) ** 2 * sb**2 + 2 * w * (1 - w) * rho * sa * sb)

for rho in (1, 0.3, 0, -0.5):
    print(rho, round(portfolio_sd(0.5, rho), 4))
# 1 0.175
# 0.3 0.1419
# 0 0.125
# -0.5 0.0901

# A sum of independent normals: bus ride N(25, 4^2) plus walk N(10, 3^2) minutes.
total = [random.gauss(25, 4) + random.gauss(10, 3) for _ in range(200_000)]
print(round(mean(total), 2), round(pstdev(total), 2), round(sum(t > 45 for t in total) / len(total), 4))
# 35.0 4.99 0.0227
```

The correlation of 0.553 between the two simulated series comes entirely from their dependence on `temp`: there is no term in the formula for `drown` that involves `sales`. The simulated standard deviation of the commute, 4.99, is close to $\sqrt{16 + 9} = 5$, not 7.

</details>

## FAQ

### Why does covariance use the product of deviations?

The product $(X - \mu_X)(Y - \mu_Y)$ is positive when both deviations have the same sign and negative when they have opposite signs, so its average records whether the variables lean the same way. The sum formula shows that this average is exactly the missing term in the variance of $X + Y$, which gives it a reason to exist beyond measuring association.

### Is a correlation of 0.5 "half as strong" as 1?

No, correlation is not a proportion. A better reading is $\rho^2$, the share of the variance of one variable that a straight-line fit on the other accounts for. For $\rho = 0.5$ this is 25%. For $\rho = 0.9$ it is 81%. The lesson on correlation and linear regression<!-- link: ../08-statistics/04-correlation-and-linear-regression.md --> develops this.

### Why does diversification not remove all the risk?

Because assets share a common risk, which shows up as positive covariance. Averaging $n$ assets divides the variance of each asset's own risk by $n$, but the covariance terms don't shrink with $n$. In the formula $\sigma^2\left(\frac{1}{n} + \left(1 - \frac{1}{n}\right)\rho\right)$ the first term goes to 0 and the second tends to $\rho\sigma^2$. Only assets with low or negative correlation with the rest reduce the floor.

### What about sums of dependent variables that aren't normal?

The mean of a sum is always the sum of the means, and the variance formula with covariances is always true. What changes is the shape: the sum of independent normals is exactly normal, and for other distributions the sum has its own distribution. For many independent pieces, the next lesson shows that the sum is close to normal anyway.

## Practice

### Warm-up

1\. A pair $(X, Y)$ has joint probabilities $p(0, 0) = 0.1$, $p(0, 1) = 0.4$, $p(1, 0) = 0.3$ and $p(1, 1) = 0.2$. Find the marginals and decide whether the variables are independent.

<details class="solution" markdown>
<summary>Solution</summary>

The marginals are $P(X = 0) = 0.5$, $P(X = 1) = 0.5$, $P(Y = 0) = 0.4$ and $P(Y = 1) = 0.6$. The cell $(0, 0)$ would need $0.5 \cdot 0.4 = 0.2$ for independence, but it has 0.1. So the variables are dependent.

Check: the entries add to $0.1 + 0.4 + 0.3 + 0.2 = 1$, and the marginals do too. In this table $Y = 1$ is more likely when $X = 0$ ($\frac{0.4}{0.5} = 0.8$) than when $X = 1$ ($\frac{0.2}{0.5} = 0.4$), which is the dependence in words.

</details>

2\. Let $\operatorname{Var}(X) = 1$, $\operatorname{Var}(Y) = 4$ and $\operatorname{Cov}(X, Y) = 0.5$. Find $\operatorname{Var}(2X - 3Y + 1)$.

<details class="solution" markdown>
<summary>Solution</summary>

The constant 1 doesn't change the variance. For the rest, $\operatorname{Var}(2X - 3Y) = 2^2\operatorname{Var}(X) + (-3)^2\operatorname{Var}(Y) + 2(2)(-3)\operatorname{Cov}(X, Y) = 4 + 36 - 6 = 34$.

Check: with a covariance of 0 the result would be 40, and the positive covariance reduces it, since $X$ and $Y$ enter with opposite signs and partly cancel.

</details>

3\. Flip a fair coin twice. Let $X$ be the number of heads and $Y$ the number of tails. Find $\operatorname{Cov}(X, Y)$ and $\rho(X, Y)$.

<details class="solution" markdown>
<summary>Solution</summary>

Since $Y = 2 - X$, the variable $Y$ is a linear function of $X$ with slope $-1$. $\operatorname{Var}(X) = 2 \cdot \frac{1}{4} = 0.5$ for the binomial with $n = 2$ and $p = \frac{1}{2}$. By Theorem 1, $\operatorname{Cov}(X, 2 - X) = -\operatorname{Var}(X) = -0.5$. Also $\operatorname{Var}(Y) = 0.5$, so $\rho = \frac{-0.5}{\sqrt{0.5 \cdot 0.5}} = -1$.

Check: a perfect linear relation with a negative slope must give $\rho = -1$, the lower bound of Theorem 4. And $X + Y = 2$ is constant, so $\operatorname{Var}(X + Y) = 0 = 0.5 + 0.5 + 2(-0.5)$.

</details>

### Standard

4\. Using the joint table of Example 1, find $P(Y = 2 \mid X = 2)$, and verify $\operatorname{Var}(X + Y) = 2.0275$ by finding the distribution of $X + Y$ directly.

<details class="solution" markdown>
<summary>Solution</summary>

$P(Y = 2 \mid X = 2) = \frac{p(2, 2)}{p_X(2)} = \frac{0.15}{0.20} = 0.75$.

For the sum, collect the cells by the value of $X + Y$: the value 0 has $p(0, 0) = 0.30$; the value 1 has $p(0, 1) + p(1, 0) = 0.20$; the value 2 has $p(1, 1) + p(0, 2) + p(2, 0) = 0.20$; the value 3 has $p(1, 2) + p(2, 1) = 0.15$; the value 4 has $p(2, 2) = 0.15$. The mean is $0.20 + 0.40 + 0.45 + 0.60 = 1.65$, which is $0.8 + 0.85$. Then $E[(X + Y)^2] = 0.20 + 0.80 + 1.35 + 2.40 = 4.75$ and the variance is $4.75 - 1.65^2 = 4.75 - 2.7225 = 2.0275$.

Check: this agrees with $0.56 + 0.6275 + 2(0.42) = 2.0275$ from Theorem 3.

</details>

5\. For the assets of Example 3 with $\rho = 0.3$, a portfolio puts a weight $w$ in A and $1 - w$ in B. Find the weight with the smallest variance, by setting the derivative of $\operatorname{Var}(R)$ to 0, and find its standard deviation and expected return.

<details class="solution" markdown>
<summary>Solution</summary>

With $\sigma_A = 0.20$, $\sigma_B = 0.15$ and $\rho\sigma_A\sigma_B = 0.009$,

$$
\operatorname{Var}(R) = 0.04w^2 + 0.0225(1 - w)^2 + 0.018w(1 - w).
$$

The derivative is $0.08w - 0.045(1 - w) + 0.018(1 - 2w) = (0.08 + 0.045 - 0.036)w - 0.045 + 0.018 = 0.089w - 0.027$. Setting it to 0 gives $w = \frac{0.027}{0.089} \approx 0.303$. The second derivative $0.089$ is positive, so this is a minimum. The variance there is $0.018404$ and $\sigma \approx 13.57\%$. The expected return is $0.303(8\%) + 0.697(6\%) \approx 6.61\%$.

Check: this matches the formula $w = \frac{\sigma_B^2 - \rho\sigma_A\sigma_B}{\sigma_A^2 + \sigma_B^2 - 2\rho\sigma_A\sigma_B} = \frac{0.0135}{0.0445}$ quoted in Example 3. The minimum-risk portfolio has lower risk than either asset alone (15% and 20%), by using both.

</details>

6\. Two students' scores on a test are modelled as independent, $X \sim N(100, 15^2)$ and $Y \sim N(110, 20^2)$ (hypothetical numbers). Find the probability that $X > Y$.

<details class="solution" markdown>
<summary>Solution</summary>

The difference $D = X - Y$ is normal, with mean $100 - 110 = -10$ and variance $15^2 + 20^2 = 625$, so $\sigma_D = 25$. Then $P(X > Y) = P(D > 0) = 1 - \Phi\!\left(\frac{0 - (-10)}{25}\right) = 1 - \Phi(0.4) = 1 - 0.6554 = 0.3446$.

Check: the probability is below $\frac{1}{2}$, as it should be, since $Y$ has the higher mean. A simulation with 200,000 pairs gives 0.345. Subtracting the variances by mistake would give $\sigma^2 = 225 - 400 < 0$, which is impossible, a quick sign that variances of differences add.

</details>

### Challenge

7\. Show that if $\rho(X, Y) = 1$, then $Y = aX + b$ with probability 1, for some $a > 0$ and some $b$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: with $U$ and $V$ the standardized variables, $\operatorname{Var}(U - V) = 2 - 2\rho$, which is 0 when $\rho = 1$. What we want: $V = U$ with probability 1. The plan is to show that a variable with variance 0 is constant, and then translate back.

Let $W = U - V$. It has $E[W] = 0$ and $\operatorname{Var}(W) = E[W^2] = \sum_w w^2 P(W = w) = 0$ (for a discrete variable). Every term is non-negative, so each term is 0, and $P(W = w) = 0$ unless $w = 0$. So $W = 0$ with probability 1, meaning $V = U$. Then $\frac{Y - \mu_Y}{\sigma_Y} = \frac{X - \mu_X}{\sigma_X}$, that is, $Y = \frac{\sigma_Y}{\sigma_X}X + \left(\mu_Y - \frac{\sigma_Y}{\sigma_X}\mu_X\right)$. This is $aX + b$ with $a = \frac{\sigma_Y}{\sigma_X} > 0$. $\blacksquare$

Check with the table of Practice problem 3's variables, which have $\rho = -1$: the same argument with $U + V$ gives $V = -U$, that is, $Y = -X + 2$, and indeed $Y = 2 - X$.

</details>

8\. (Reviews [discrete random variables](03-discrete-random-variables.md).) Shuffle $n \ge 2$ items and let $X$ be the number in their original position, so that $X = I_1 + \cdots + I_n$ for indicators $I_i$. Show that $\operatorname{Cov}(I_i, I_j) = \frac{1}{n^2(n - 1)}$ for $i \ne j$, and use it to show that $\operatorname{Var}(X) = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $E[I_i] = \frac{1}{n}$ from the last lesson, and Theorem 3 for $n$ variables. What we want: the covariance of two indicators and the sum. The plan is to find $E[I_iI_j]$ by counting.

For $i \ne j$, $I_iI_j = 1$ exactly when items $i$ and $j$ are both fixed, and there are $(n - 2)!$ orders of the others, so $E[I_iI_j] = \frac{(n - 2)!}{n!} = \frac{1}{n(n - 1)}$. Then $\operatorname{Cov}(I_i, I_j) = \frac{1}{n(n - 1)} - \frac{1}{n^2} = \frac{n - (n - 1)}{n^2(n - 1)} = \frac{1}{n^2(n - 1)}$.

Each $I_i$ is a Bernoulli variable with $p = \frac{1}{n}$, so $\operatorname{Var}(I_i) = \frac{1}{n}\left(1 - \frac{1}{n}\right) = \frac{n - 1}{n^2}$. There are $n$ variances and $n(n - 1)$ ordered pairs, and so

$$
\operatorname{Var}(X) = n \cdot \frac{n - 1}{n^2} + n(n - 1)\cdot\frac{1}{n^2(n - 1)} = \frac{n - 1}{n} + \frac{1}{n} = 1.
$$

Check with $n = 4$, where the distribution of $X$ is 0, 1, 2, 4 with probabilities $\frac{9}{24}$, $\frac{8}{24}$, $\frac{6}{24}$, $\frac{1}{24}$: $E[X^2] = \frac{0 + 8 + 24 + 16}{24} = 2$ and $\operatorname{Var}(X) = 2 - 1 = 1$. The mean and the variance of the number of fixed points are both 1.

</details>

## Where this shows up

- The next lesson, [the law of large numbers and the CLT](06-law-of-large-numbers-and-clt.md), uses the variance of a sum of independent variables to show that an average of $n$ of them has variance $\frac{\sigma^2}{n}$. Correlation and the line of best fit are developed in correlation and linear regression<!-- link: ../08-statistics/04-correlation-and-linear-regression.md -->, and in regression and econometrics intuition<!-- link: ../../07-economics-math/04-more-tools/03-regression-and-econometrics-intuition.md -->, where the confounding warning above becomes the main practical problem.
- In CS and data science, the covariance matrix of many variables is a symmetric matrix whose eigenvectors give the directions of greatest variance, the basis of principal component analysis ([eigenvalues and eigenvectors](../06-linear-algebra/08-eigenvalues-and-eigenvectors.md)). Independence of random bits and hash values is the assumption behind most randomized algorithms (discrete probability<!-- link: ../../06-cs-math/03-counting-and-discrete-probability/05-discrete-probability.md -->).
- In finance, the variance-of-a-sum formula with covariances is the mathematics of diversification and of the mean-variance model of portfolios (investing returns and risk<!-- link: ../../08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk.md -->). Insurance works because the claims of many unrelated policyholders have low covariance (insurance and expected value<!-- link: ../../08-financial-math/07-taxes-insurance-and-planning/02-insurance-and-expected-value.md -->).
