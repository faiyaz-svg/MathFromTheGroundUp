# Regression and econometrics intuition

After this lesson you can read a regression equation and a regression table, interpret coefficients in levels, logs and dummy variables, predict the direction of omitted variable bias from the bias formula, and explain why a regression slope is not automatically a causal effect.

Before this: [correlation and linear regression](../../05-university-core/08-statistics/04-correlation-and-linear-regression.md) (least squares, $R^2$ and the standard error of a slope are taught there and not re-derived here), [hypothesis testing](../../05-university-core/08-statistics/03-hypothesis-testing.md), and [chain rule, implicit and inverse derivatives](../../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md) (the derivative of $\ln x$).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A regression of hourly wage (dollars) on years of schooling gives $\widehat{\text{wage}} = 4.00 + 1.50 \times \text{schooling}$. What does 1.50 mean, and what wage does the line predict for 14 years?
2. A regression of $\ln(\text{wage})$ on years of schooling has slope 0.08. About what percent higher is the wage for one more year of schooling?
3. A coefficient is 0.045 with a standard error of 0.015. What is its t-statistic, and is it statistically significant at the 5% level?

<details class="solution" markdown>
<summary>Answers</summary>

1. Among workers in the data, one more year of schooling goes with \$1.50 more in hourly wage. For 14 years, $4.00 + 1.50 \times 14 = 25.00$, so \$25.00 an hour.
2. About 8%. In a log-linear model, the slope times 100 is the approximate percent change in the outcome per unit of the explanatory variable (the exact figure is $e^{0.08} - 1 \approx 8.3\%$).
3. $t = \frac{0.045}{0.015} = 3$. The cutoff is about 2 for a 5% test, so yes, it is significant.

</details>

## The idea

An economist asks: how much more do people earn for each extra year of school? You could look at a scatter plot of wages against schooling and fit a line, as in the earlier lesson on regression. The slope is a number, say 12% more per year. But a number is not an answer until you know what it measures. People who stay in school longer also tend to differ in ability, family background and where they live, and each of those could raise wages by itself. A line through the raw data blends the effect of schooling with the effect of everything that travels with schooling.

Econometrics is the set of methods for using regression to learn about cause and effect, and most of it deals with that blending. Two tools do most of the work. The first is adding the other variables to the regression as extra columns, so that the coefficient on schooling compares people who are alike in the other measured ways. The second is knowing, when a variable is left out, which way and how far the coefficient is pushed. This lesson covers those two, how to read the coefficient when variables are in logs or are yes/no dummies, and how to read a regression table.

All the data in this lesson are simulated, so the true effects are known and you can see how far each regression lands from the truth.

## Definitions

A **regression model** says that an outcome $y$ is a linear function of an explanatory variable $x$ plus an error:

$$
y = \beta_0 + \beta_1 x + u.
$$

The numbers $\beta_0$ and $\beta_1$ are the unknown **coefficients** (the intercept and the slope) of the population. The **error** $u$ holds everything else that affects $y$: other variables, luck and measurement noise. In plain words, $\beta_1$ is how much $y$ changes, on average, when $x$ rises by one unit, and $u$ is the part of $y$ the model leaves unexplained.

The estimates computed from a sample are written $b_0$ and $b_1$ (the least-squares line of the earlier lesson). The model is **causal** when $\beta_1$ is the effect on $y$ of changing $x$ with everything else held fixed. For that, the error must be unrelated to $x$: $E[u \mid x] = 0$, called **exogeneity** (the average error is 0 whatever the value of $x$). If this fails, the least-squares slope is a biased estimate of $\beta_1$: it misses on average, even with unlimited data.

**Ceteris paribus** is Latin for "other things equal". In a regression with several variables, $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + u$, each coefficient is read ceteris paribus: $\beta_1$ is the change in $y$ per unit change in $x_1$ with $x_2, \dots$ fixed. It is a partial derivative, $\beta_1 = \frac{\partial y}{\partial x_1}$ (see [partial derivatives and the gradient](../../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md)).

A **dummy variable** (indicator variable) is a variable $D$ that equals 1 for one group and 0 for the other, such as $\text{female} = 1$ for women and 0 for men. In plain words, its coefficient is the average difference between the groups, holding the other variables fixed.

A **log-linear** model has $\ln y$ on the left and $x$ on the right, $\ln y = \beta_0 + \beta_1 x + u$. A **log-log** model has $\ln y = \beta_0 + \beta_1 \ln x + u$. A **level-log** model has $y = \beta_0 + \beta_1 \ln x + u$. Here $\ln$ is the natural logarithm.

An **omitted variable** is a variable that belongs in the model, because it affects $y$, but is not included. **Omitted variable bias** is the difference between the expected value of the estimated slope and the true $\beta_1$ that results.

A **regression table** reports, for each coefficient, its estimate, **standard error** (the typical size of the sampling error of the estimate), and the **t-statistic** $t = \frac{b_j}{\text{SE}(b_j)}$ for the null hypothesis $\beta_j = 0$. Under the conditions of the earlier lesson, a 95% confidence interval is $b_j \pm t^* \cdot \text{SE}(b_j)$ with $t^* \approx 1.96$ in a large sample. The table also gives $R^2$, the share of the variation in $y$ that the model accounts for, and the number of observations $n$.

## How to do it

### Reading a coefficient

1. Note the units of $y$ and of $x$, and whether either is in logs. The units decide the reading.
2. Level-level ($y$ on $x$): $b_1$ is the change in $y$ units per unit of $x$.
3. Log-linear ($\ln y$ on $x$): $100\,b_1$ is the approximate percent change in $y$ per unit of $x$. For a larger change, use $e^{b_1 \Delta x} - 1$.
4. Log-log: $b_1$ is the elasticity, the percent change in $y$ for a 1% change in $x$.
5. Level-log ($y$ on $\ln x$): $\frac{b_1}{100}$ is the change in $y$ units per 1% change in $x$.
6. Dummy: $b_1$ is the average difference between the group coded 1 and the group coded 0 (in a log model, the difference is about $100\,b_1$ percent).
7. Add "other variables in the model held fixed" for every coefficient in a multiple regression, and ask whether the variable you most worry about is in the model.

### Why the log readings work

*Theorem 1.* Suppose $y > 0$ and $x > 0$ where logs are taken.

- (a) If $\ln y = \beta_0 + \beta_1 x$, then $\frac{dy}{dx} \cdot \frac{1}{y} = \beta_1$, so a unit rise in $x$ changes $y$ by the exact factor $e^{\beta_1}$, which is a percent change of $e^{\beta_1} - 1 \approx \beta_1$ when $\beta_1$ is small.
- (b) If $\ln y = \beta_0 + \beta_1 \ln x$, then the elasticity $\frac{dy}{dx} \cdot \frac{x}{y}$ equals $\beta_1$ at every point.
- (c) If $y = \beta_0 + \beta_1 \ln x$, then $\frac{dy}{dx} = \frac{\beta_1}{x}$, so a 1% rise in $x$ changes $y$ by about $\frac{\beta_1}{100}$.

We know the derivative rules $\frac{d}{dx}\ln x = \frac{1}{x}$ and the chain rule. We want to turn each model into a statement about percent changes. The plan is to solve each model for $y$, differentiate, and compare $\frac{dy}{y}$ with $dx$ or $\frac{dx}{x}$.

*Proof.* (a) Solving gives $y = e^{\beta_0 + \beta_1 x}$. Then $\frac{dy}{dx} = \beta_1 e^{\beta_0 + \beta_1 x} = \beta_1 y$, so $\frac{1}{y}\frac{dy}{dx} = \beta_1$. For a whole unit of $x$, the ratio of the new $y$ to the old is $\frac{e^{\beta_0 + \beta_1 (x+1)}}{e^{\beta_0 + \beta_1 x}} = e^{\beta_1}$.

(b) Solving gives $y = e^{\beta_0} x^{\beta_1}$. Then $\frac{dy}{dx} = \beta_1 e^{\beta_0} x^{\beta_1 - 1} = \beta_1 \frac{y}{x}$, so $\frac{dy}{dx} \cdot \frac{x}{y} = \beta_1$.

(c) Differentiating directly, $\frac{dy}{dx} = \frac{\beta_1}{x}$. A 1% rise in $x$ is $dx = 0.01x$, so $dy = \frac{\beta_1}{x} \cdot 0.01x = \frac{\beta_1}{100}$. $\blacksquare$

Look back: in all three cases, the log turns a percent change into a plain difference, because $d(\ln x) = \frac{dx}{x}$ is the fractional change of $x$. That is why economists like logs: wages, prices and GDP change in percent terms, not in dollars. The readings with "about" are linear approximations (see [linear approximation](../../05-university-core/03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md)). They are good for small coefficients and poor for large ones: $e^{0.05} - 1 = 5.1\%$, but $e^{0.5} - 1 = 64.9\%$, not 50%. The elasticity of part (b) is the same elasticity as in [elasticity](../02-markets/05-elasticity.md), and a log-log regression of quantity on price estimates it directly.

### Omitted variable bias

Suppose the true model has two variables,

$$
y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + u,
$$

but you regress $y$ on $x_1$ alone, because $x_2$ is not measured or you didn't think of it. Let $\tilde{b}_1$ be the slope of this short regression, and let $\delta_1$ be the slope from regressing $x_2$ on $x_1$, which measures how much $x_2$ tends to be higher when $x_1$ is higher.

*Theorem 2 (omitted variable bias).* Let $b_1$ and $b_2$ be the coefficients from the least-squares regression of $y$ on both $x_1$ and $x_2$, in the same sample. Then exactly

$$
\tilde{b}_1 = b_1 + b_2\,\delta_1,
\qquad \delta_1 = \frac{S_{12}}{S_{11}},
$$

where $S_{11} = \sum (x_{1i} - \bar{x}_1)^2$ and $S_{12} = \sum (x_{1i} - \bar{x}_1)(x_{2i} - \bar{x}_2)$. In large samples $b_1 \to \beta_1$ and $b_2 \to \beta_2$, so the short regression estimates $\beta_1 + \beta_2\,\delta_1$, and the bias is $\beta_2\,\delta_1$.

We know that the least-squares residuals add to 0 and are uncorrelated with each explanatory variable (the residual is perpendicular to every column, from the earlier lesson), and that the simple slope is $\tilde{b}_1 = \frac{S_{1y}}{S_{11}}$. We want to link the short slope to the long ones. The plan is to write each $y_i$ using the long regression and take the sum of products with the deviations of $x_1$.

*Proof.* The long regression fits $y_i = b_0 + b_1 x_{1i} + b_2 x_{2i} + e_i$. Subtract the means, using the fact that the fitted plane passes through the point of means: $y_i - \bar{y} = b_1 (x_{1i} - \bar{x}_1) + b_2 (x_{2i} - \bar{x}_2) + e_i$. Multiply by $(x_{1i} - \bar{x}_1)$ and add over all $i$:

$$
S_{1y} = b_1 S_{11} + b_2 S_{12} + \sum (x_{1i} - \bar{x}_1)\,e_i.
$$

The last sum is 0, because the residuals are uncorrelated with $x_1$ and add to 0. Dividing by $S_{11}$ gives $\tilde{b}_1 = b_1 + b_2 \frac{S_{12}}{S_{11}}$. $\blacksquare$

Look back: the formula says that the short regression gives you the direct effect of $x_1$ plus the effect of $x_2$ that $x_1$ picks up because the two move together. The sign of the bias is the product of two signs:

| | $x_1$ and $x_2$ positively related ($\delta_1 > 0$) | $x_1$ and $x_2$ negatively related ($\delta_1 < 0$) |
|---|---|---|
| $x_2$ raises $y$ ($\beta_2 > 0$) | upward bias: the slope is too big | downward bias: the slope is too small |
| $x_2$ lowers $y$ ($\beta_2 < 0$) | downward bias: the slope is too small | upward bias: the slope is too big |

There is no bias if $\beta_2 = 0$ (the omitted variable doesn't matter) or $\delta_1 = 0$ (it is unrelated to $x_1$). Adding a variable that is unrelated to $x_1$ doesn't change the slope of $x_1$, which is why a randomised experiment, where $x_1$ is assigned at random and so unrelated to everything else, needs no controls to be causal. Bias doesn't shrink as the sample grows. It is a flaw in the question the regression answers, not a lack of data.

## Worked examples

<div class="example" markdown>

### Example 1: reading a regression table

A simulated sample of 2,000 workers (made-up data) has the hourly wage, years of education, years of experience and a dummy that is 1 for women. A regression of $\ln(\text{wage})$ on these gives:

| Variable | Coefficient | Standard error | t-statistic |
|---|---|---|---|
| intercept | 0.677 | 0.0457 | 14.8 |
| education (years) | 0.1186 | 0.0033 | 35.5 |
| experience (years) | 0.0206 | 0.0012 | 16.6 |
| female (1 or 0) | $-0.0863$ | 0.0142 | $-6.1$ |

The sample has $n = 2000$ and $R^2 = 0.443$. Interpret each coefficient and say which are significant.

Step 1: the outcome is in logs, and education and experience are in years, so the model is log-linear for those two variables.

Step 3 (log-linear): each extra year of education goes with a wage that is about 11.9% higher, holding experience and sex fixed. The exact percent is $e^{0.1186} - 1 = 12.6\%$. Experience: each extra year goes with about 2.1% higher wages ($e^{0.0206} - 1 = 2.08\%$), holding education and sex fixed.

Step 6 (dummy): women earn about 8.6% less than men, holding education and experience fixed. The exact figure is $e^{-0.0863} - 1 = -8.3\%$. The coefficient is the difference between two groups of workers who are alike in education and experience, and not a statement about why the gap exists.

All the t-statistics have absolute value far above 2, so each coefficient is statistically significant at the 5% level. A 95% confidence interval for the education coefficient is $0.1186 \pm 1.96 \times 0.0033$, which is $(0.112, 0.125)$. The intercept, 0.677, is the predicted log wage for a man with 0 education and 0 experience. It is outside the data, so it has no use on its own.

The $R^2$ says the three variables account for 44.3% of the variation in log wages; the other 55.7% is left to the error, which holds everything that wasn't measured.

Check: $t = \frac{b}{\text{SE}}$ matches the table, for example $\frac{0.0206}{0.0012} \approx 17$ (the table says 16.6, because the printed numbers are rounded). Everything in this table comes from a seeded simulation in the In code section.

</div>

<div class="example" markdown>

### Example 2: a log-log demand regression

A simulated data set (made-up numbers) has the price and quantity sold of a product in 400 stores. The true demand is $q = 1000\,p^{-1.5}$ times random noise, so the true elasticity is $-1.5$. A regression of $\ln q$ on $\ln p$ gives a slope of $-1.538$ with a standard error of 0.039, and $R^2 = 0.794$.

By Theorem 1(b), the slope is the estimated price elasticity of demand: a 1% rise in price goes with a 1.54% fall in the quantity sold. Since the magnitude exceeds 1, demand is elastic (see [elasticity](../02-markets/05-elasticity.md)), and a price rise lowers total revenue.

A 95% interval is $-1.538 \pm 1.96 \times 0.039$, which is $(-1.614, -1.462)$. It contains the true value $-1.5$. To test whether demand is unit elastic, $H_0 \colon \beta_1 = -1$, use $t = \frac{-1.538 - (-1)}{0.039} = -13.8$, so unit elasticity is firmly rejected.

For a 10% price rise, the "elasticity times 10%" rule gives $-15.4\%$, but the exact prediction is $1.10^{-1.538} - 1 = -13.6\%$. A 10% change is large enough that the approximation is off by almost 2 points, so use the exact formula for big changes.

Check: on a log-log scale the data are close to a straight line with slope about $-1.5$, and the exact change for a 1% rise is $1.01^{-1.538} - 1 = -1.52\%$, close to the slope.

</div>

<div class="example" markdown>

### Example 3: omitted variable bias, with the numbers

Return to the wage data of Example 1. In the simulation, each worker has an "ability" that raises wages and also raises years of education. A researcher can't observe ability. The regression in Example 1 left it out, and gave 0.1186 for education. With ability in the model (possible only in a simulation), the coefficients are 0.0806 on education and 0.1134 on ability.

The bias formula needs $\delta_1$, the slope from regressing ability on education, experience and sex in the same sample: it is 0.3351. So

$$
\tilde{b}_1 = b_1 + b_2\,\delta_1 = 0.0806 + 0.1134 \times 0.3351 = 0.0806 + 0.0380 = 0.1186.
$$

The short regression gives exactly the number the formula predicts. The bias is $+0.038$, nearly half again as big as the true effect of about 0.08: leaving out ability makes education look 47% more powerful than it is.

Both signs are positive: ability raises wages ($\beta_2 > 0$) and is higher among the more educated ($\delta_1 > 0$), so the bias is upward, the top-left cell of the table.

Check: the true coefficient used to build the data was 0.08, and the regression with ability found 0.0806. The bias predicted in large samples is $0.10 \times 0.333 = 0.033$, because the true $\delta_1 = \frac{1.5}{1.5^2 + 1.5^2} = \frac{1}{3}$ in the way the data were made, and the sample's $0.038$ is close to it.

The fix is not always available. Ability is not in any survey, and the researcher can't add it. Economists then look for variation in education that is unrelated to ability, such as a change in the school leaving age, as a natural experiment. That is the subject of a full econometrics course.

</div>

<div class="example" markdown>

### Example 4: finish it yourself (police and crime)

A city study regresses the crime rate (crimes per 1,000 residents) on the number of police officers per 1,000 residents, across neighbourhoods, and finds a positive slope. The made-up truth is $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + u$ with $\beta_1 = -3$ (more police reduce crime) and $\beta_2 = 8$, where $x_2$ is an unmeasured "danger index" of the neighbourhood. Dangerous neighbourhoods get more police: regressing $x_2$ on $x_1$ gives $\delta_1 = 2$.

Use Theorem 2 to find the slope the short regression estimates, and say what a reader who ignored the omitted variable would conclude.

<details class="solution" markdown>
<summary>Finish</summary>

The short regression estimates $\beta_1 + \beta_2\,\delta_1 = -3 + 8 \times 2 = 13$. The bias is $+16$, and it is large enough to flip the sign: the regression shows crime rising by 13 per 1,000 for each additional officer per 1,000, although the true effect of police is a reduction of 3.

A reader who ignored the omitted variable would conclude that police cause crime. The correct reading is that police are sent where the danger is, so the police variable is standing in for danger.

Check against the sign table: $\beta_2 > 0$ and $\delta_1 > 0$ gives an upward bias, as found. Reverse causality (crime attracts police) works the same way here, and a regression can't separate it from the effect of police without extra information.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a coefficient is a statement about differences, not about changes. "People with one more year of education earn 12.6% more" compares different people. It says that changing one person's schooling would raise their wage by 12.6% only if the model is causal, which needs the error to be unrelated to schooling. Correlation can't tell which, and the phrase "associated with" is the safe wording until you have argued for causation.

</div>

<div class="warning" markdown>

Watch out: significant does not mean important. With 2,000 observations, even a tiny coefficient can have a large t-statistic. A slope of 0.001 with a standard error of 0.0002 is statistically significant ($t = 5$), but one extra year of education would change wages by only 0.1%. Read the size of the coefficient in the units of the problem, and use the standard error to see how precisely it is estimated. Don't read the size from the t-statistic.

</div>

<div class="warning" markdown>

Watch out for the percent-change reading of a dummy in a log model. A dummy coefficient of $-0.0863$ means about $-8.6\%$ only as an approximation, and the exact figure is $e^{-0.0863} - 1 = -8.3\%$. For a coefficient of $-0.5$, the approximation says 50% lower, and the exact answer is $e^{-0.5} - 1 = -39.3\%$. Use the exact formula when $\lvert b \rvert$ is more than about 0.1.

</div>

<div class="warning" markdown>

Watch out for the dummy variable trap. If you include a dummy for women and a dummy for men and also an intercept, the two dummies add to the column of ones, so one column is a combination of the others, and least squares has no unique answer. Include one fewer dummy than the number of groups. The group left out is the baseline, and each included dummy's coefficient is the difference from it.

</div>

<div class="warning" markdown>

Watch out: adding variables is not always good. Adding a variable that is a result of the one you study (for example, adding occupation when studying the effect of education on wages, when education leads to better occupations) can remove part of the effect you want to measure. And $R^2$ never falls when a variable is added, so $R^2$ can't tell you whether to include it. The choice of controls comes from an argument about the causal story, not from the fit.

</div>

Other limits. If the explanatory variable is measured with random error, the slope is pulled toward 0 (attenuation), because the noise makes $x$ look less related to $y$ than it is. Reverse causality, as in Example 4, gives a bias like omitted variable bias. Logs need positive values: $\ln 0$ is undefined, so zero wages or zero sales can't be logged directly. And a regression describes the range of the data: predicting for 40 years of experience when no worker has more than 20 is extrapolation, as in the earlier lesson.

## Tricks and shortcuts

For the bias direction, multiply two signs: the sign of the omitted variable's effect on $y$, and the sign of its relation to the variable you studied. Plus times plus is upward, minus times minus is upward, and mixed signs give downward.

When units change, coefficients change in the opposite direction. If you measure education in months instead of years, $x$ is 12 times larger, so the slope is $\frac{1}{12}$ as large, and its standard error shrinks by the same factor, so the t-statistic is unchanged. The t-statistic, $R^2$ and predictions don't depend on units.

A quick significance rule: for $n$ above 30, $\lvert t \rvert > 2$ means significant at the 5% level, and the interval is about the coefficient plus or minus twice the standard error.

For percent readings, remember two reference points: $e^{0.1} - 1 = 10.5\%$ and $e^{-0.1} - 1 = -9.5\%$. Between 0.1 and $-0.1$, the coefficient times 100 is accurate to within half a percentage point.

## In code

The code simulates the wage data (seeded), runs least squares with standard errors and $R^2$ in NumPy, shows the omitted variable bias identity from Theorem 2, and fits the log-log demand regression.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

def ols(columns, y):
    """Least squares with an intercept. Returns coefficients, standard errors, R squared."""
    X = np.column_stack([np.ones(len(y))] + list(columns))
    xtx_inv = np.linalg.inv(X.T @ X)
    b = xtx_inv @ X.T @ y
    e = y - X @ b
    s2 = e @ e / (len(y) - X.shape[1])
    se = np.sqrt(np.diag(s2 * xtx_inv))
    r2 = 1 - e @ e / ((y - y.mean()) @ (y - y.mean()))
    return b, se, r2

# Simulated workers: ability raises both education and wages.
rng = np.random.default_rng(42)
n = 2000
ability = rng.normal(0, 1, n)
educ = 13 + 1.5 * ability + rng.normal(0, 1.5, n)
exper = rng.uniform(0, 20, n)
female = (rng.random(n) < 0.5).astype(float)
u = rng.normal(0, 0.3, n)
lnw = 1.2 + 0.08 * educ + 0.02 * exper - 0.10 * female + 0.10 * ability + u

# Short regression: what a researcher without an ability measure would run.
b_s, se_s, r2_s = ols([educ, exper, female], lnw)
print([round(float(v), 4) for v in b_s])            # [0.677, 0.1186, 0.0206, -0.0863]
print([round(float(v), 4) for v in se_s])           # [0.0457, 0.0033, 0.0012, 0.0142]
print([round(float(v), 1) for v in b_s / se_s])     # [14.8, 35.5, 16.6, -6.1]
print(round(r2_s, 3))                        # 0.443

# Long regression, with ability (only possible in a simulation).
b_l, se_l, r2_l = ols([educ, exper, female, ability], lnw)
print([round(float(v), 4) for v in b_l])            # [1.1758, 0.0806, 0.0203, -0.083, 0.1134]
print(round(r2_l, 3))                        # 0.478

# Omitted variable bias identity: short slope = long slope + b_ability * delta.
d, _, _ = ols([educ, exper, female], ability)
print(round(d[1], 4))                                    # 0.3351
print(round(b_s[1], 4), round(b_l[1] + b_l[4] * d[1], 4))   # 0.1186 0.1186

# Log-log demand: the slope is the price elasticity.
rng2 = np.random.default_rng(7)
lnp = rng2.normal(np.log(10), 0.2, 400)
lnq = np.log(1000) - 1.5 * lnp + rng2.normal(0, 0.15, 400)
b, se, r2 = ols([lnp], lnq)
print([round(float(v), 3) for v in b], [round(float(v), 3) for v in se], round(r2, 3))
# [6.979, -1.538] [0.09, 0.039] 0.794
print(round(1.10 ** b[1] - 1, 3))            # -0.136
```

The identity holds to the last decimal because it is algebra, not a statistical claim. The coefficient on ability (0.1134) differs a little from the 0.10 used to make the data because of sampling noise. In practice, packages such as `statsmodels` print this table (and p-values) for you: `statsmodels.api.OLS(y, X).fit().summary()`.

</details>

## FAQ

### Why not just include every variable I can think of?

Extra variables cost precision and can do harm. They raise the standard errors when they are strongly related to the variable of interest, and a variable that is itself caused by $x_1$ (a mediator) removes part of the effect you are trying to measure. The aim is to include the variables that affect $y$ and are related to $x_1$ (the confounders), and leave out the consequences of $x_1$.

### How do economists get causal effects, if regression has these problems?

By finding variation in $x$ that is as good as random. A randomised experiment is the cleanest, and in the simulation of Example 3 it would make $\delta_1 = 0$ and remove the bias. Economists also use natural experiments, in which a rule or accident changes $x$ for reasons unrelated to $y$, and comparisons of the same units before and after a change. Those are the topics of a full econometrics course, and each is a way of getting variation that is unrelated to the omitted variables.

### Why use logs for wages and prices?

Because these variables change in proportions, and are skewed: a few very high values stretch the right tail. Taking logs makes percent effects the natural unit, often makes the relationship closer to a straight line, and makes the spread of the errors more even. The cost is that you must read the coefficients as percents and can't take the log of zero.

### What does the intercept mean?

It is the predicted value of $y$ when every explanatory variable is 0. It is meaningful only if 0 is a sensible value for all of them. In Example 1 it describes a man with no education and no experience, which doesn't exist in the data, so the intercept only anchors the line. It is still needed, because dropping it forces the line through the origin and biases the other coefficients.

## Practice

### Warm-up

1\. A regression of weekly hours worked on the number of children gives $\widehat{\text{hours}} = 32.0 - 1.2 \times \text{children}$ (made-up). Interpret the slope and predict the hours for a person with 2 children.

<details class="solution" markdown>
<summary>Solution</summary>

Among the people in the data, each additional child goes with 1.2 fewer hours worked per week. For 2 children, $32.0 - 1.2 \times 2 = 29.6$ hours.

Check: the prediction is below the intercept 32.0, since the slope is negative, and the drop is $2 \times 1.2 = 2.4$ hours.

</details>

2\. A regression of $\ln(\text{price})$ of houses (price in dollars) on floor area in square feet gives a slope of 0.0004. (a) About what percent is the price higher for 100 more square feet? (b) What is the exact figure?

<details class="solution" markdown>
<summary>Solution</summary>

(a) 100 square feet changes $\ln(\text{price})$ by $0.0004 \times 100 = 0.04$, so about 4%.

(b) The exact change is $e^{0.04} - 1 = 0.0408$, or 4.08%.

Check: the coefficient is small, so the approximation is close: 4% against 4.08%.

</details>

3\. In a log-log regression of quantity demanded on price, the slope is $-1.2$. (a) What is the elasticity, and is demand elastic? (b) About what happens to the quantity when the price rises by 5%? (c) What is the exact change?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The slope is the elasticity: $-1.2$. Its magnitude is above 1, so demand is elastic.

(b) About $-1.2 \times 5\% = -6\%$.

(c) $1.05^{-1.2} - 1 = -0.0569$, a fall of 5.69%.

Check: the exact and approximate values are close, because 5% is a small change.

</details>

### Standard

4\. For each omitted variable, say whether the bias on the coefficient of the named variable is upward or downward, and give the reasoning. (a) Wages on years of education, omitting family connections (which raise wages, and are more common among the more educated). (b) Health on the number of hospital visits, omitting how ill the person is. (c) Wages on years of work experience, omitting years of education, in a sample where older workers have less schooling.

<details class="solution" markdown>
<summary>Solution</summary>

Use the sign table: the bias is the sign of $\beta_2$ times the sign of $\delta_1$.

(a) Connections raise wages ($\beta_2 > 0$) and go with more education ($\delta_1 > 0$), so the bias is upward: education looks like it pays more than it does.

(b) Illness lowers health ($\beta_2 < 0$) and goes with more hospital visits ($\delta_1 > 0$), so the bias is downward. Hospital visits can look harmful when sick people are the ones who go.

(c) Education raises wages ($\beta_2 > 0$) and is negatively related to experience in this sample ($\delta_1 < 0$), so the bias is downward: the experience slope is too small.

Check: in (a) and (b), the product of signs is plus and minus respectively, and in (c) plus times minus gives minus.

</details>

5\. The true model is $y = 10 + 2x_1 + 3x_2 + u$. In a sample, the regression of $x_2$ on $x_1$ has slope 0.4. (a) What slope does the regression of $y$ on $x_1$ alone estimate? (b) What is the bias, and in which direction? (c) What would the slope be if the slope of $x_2$ on $x_1$ were $-0.4$?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\beta_1 + \beta_2\,\delta_1 = 2 + 3 \times 0.4 = 3.2$.

(b) The bias is $3 \times 0.4 = 1.2$, upward (both $\beta_2$ and $\delta_1$ are positive).

(c) With $\delta_1 = -0.4$, the estimate is $2 + 3 \times (-0.4) = 0.8$, a downward bias of 1.2.

Check: both estimates differ from the true 2 by $\pm 1.2$, with the sign of $\delta_1$.

</details>

6\. A regression table reports a coefficient of 0.045 on a training-program dummy in a log wage regression, with a standard error of 0.015. (a) Find the t-statistic and a 95% interval. (b) What is the exact percent effect on wages? (c) Is the effect statistically significant? Does that show the program caused it?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $t = \frac{0.045}{0.015} = 3$, and the interval is $0.045 \pm 1.96 \times 0.015 = (0.0156, 0.0744)$.

(b) $e^{0.045} - 1 = 0.0460$, so 4.6% higher wages for participants.

(c) Yes, $t = 3$ is above 2 and the interval excludes 0. It doesn't show that the program caused the difference: if people who joined were more motivated, motivation is an omitted variable, and the estimate could be biased upward. It depends on whether participants were assigned at random.

Check: the interval is centred on 0.045 and runs about 0.03 either side, twice the standard error.

</details>

### Challenge

7\. (a) Prove that in $\ln y = \beta_0 + \beta_1 x + u$, an increase of $\Delta x$ units in $x$ changes the predicted $y$ by the exact factor $e^{\beta_1 \Delta x}$. (b) For $\beta_1 = 0.5$ and $\Delta x = 1$, compare the exact percent change with the approximation $100\beta_1$. (c) Do the same for $\beta_1 = 0.05$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Solving for the predicted $y$ (ignoring the error term) gives $y = e^{\beta_0 + \beta_1 x}$. Then $\frac{y(x + \Delta x)}{y(x)} = \frac{e^{\beta_0 + \beta_1 x + \beta_1 \Delta x}}{e^{\beta_0 + \beta_1 x}} = e^{\beta_1 \Delta x}$, which does not depend on $x$.

(b) $e^{0.5} - 1 = 0.6487$, a 64.9% increase, against the approximation of 50%. The approximation is off by 15 points.

(c) $e^{0.05} - 1 = 0.0513$, a 5.13% increase, against 5%. The error is 0.13 points.

Check: the exact percent exceeds the approximation for every positive $\beta_1$, because $e^t > 1 + t$ for $t \ne 0$, and the gap grows with $\beta_1$.

</details>

8\. (Reviews [correlation and linear regression](../../05-university-core/08-statistics/04-correlation-and-linear-regression.md).) For the points $(1, 2)$, $(2, 3)$, $(3, 5)$, $(4, 6)$ the least-squares line is $\hat{y} = 0.5 + 1.4x$. Find the residuals, the residual standard error, the standard error of the slope, the t-statistic and a 95% confidence interval for the slope (use $t^* = 4.303$ for 2 degrees of freedom).

<details class="solution" markdown>
<summary>Solution</summary>

The fitted values are $1.9, 3.3, 4.7, 6.1$, so the residuals are $0.1, -0.3, 0.3, -0.1$, and $\text{SSE} = 0.01 + 0.09 + 0.09 + 0.01 = 0.2$. The residual standard error is $s_e = \sqrt{\frac{0.2}{4 - 2}} = 0.3162$.

With $S_{xx} = 5$, the standard error of the slope is $\frac{s_e}{\sqrt{S_{xx}}} = \frac{0.3162}{2.236} = 0.1414$. The t-statistic is $\frac{1.4}{0.1414} = 9.90$. The 95% interval is $1.4 \pm 4.303 \times 0.1414 = (0.79, 2.01)$.

Check: the interval is centred at 1.4, and excludes 0, matching the large t-statistic. With only 4 points, it is wide, since $t^* = 4.3$ is far above 1.96.

</details>

## Where this shows up

- The next lesson, [game theory and Nash equilibrium](04-game-theory-and-nash-equilibrium.md), is about strategic behaviour, which is one reason regressions on economic data are hard: people respond to each other, so $x$ and $u$ often move together.
- In economics, almost every empirical paper is a regression with a story about why the coefficient is causal. Estimates of the return to education, demand elasticities ([elasticity](../02-markets/05-elasticity.md)) and the effects of policy all use the tools here. Multipliers like the one in [the last lesson](02-multipliers-and-the-ad-as-model.md) are estimated this way, and are hard to pin down because spending and output affect each other. In finance, the slope of a stock's returns on the market's is its beta (investing returns and risk<!-- link: ../../08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk.md -->).
- In CS, the same model is the first one in machine learning. Omitted variable bias has a twin in data science, where a model trained on observational data picks up confounders, and in A/B testing, where random assignment is used precisely to make $\delta_1 = 0$ ([hypothesis testing](../../05-university-core/08-statistics/03-hypothesis-testing.md)).
