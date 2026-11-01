# Chi-square tests

After this lesson you can test whether counts in categories match a claimed split (goodness of fit) and whether two categorical variables are related (independence), compute expected counts and degrees of freedom, check the conditions, read an A/B/C test, and explain why a chi-square test with one degree of freedom is the square of the two-proportion z test.

Before this: [hypothesis testing](03-hypothesis-testing.md) (p-values and the two-proportion test), [continuous random variables and the normal distribution](../07-probability/04-continuous-random-variables-and-the-normal.md) (standard normal variables) and [conditional probability and Bayes' theorem](../07-probability/02-conditional-probability-and-bayes.md) (independence).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A die is rolled 60 times, and faces 1 to 6 come up 5, 8, 9, 8, 10 and 20 times. Find the chi-square statistic for the claim that the die is fair, and say whether it is beyond the 5% critical value 11.07 for 5 degrees of freedom.
2. A table of 100 users has 60 on the Basic plan and 40 on the Pro plan, and 70 stayed while 30 cancelled. If plan and cancelling were independent, how many Basic users would you expect to stay? How many degrees of freedom does a test on this table have?
3. The A/B test of [hypothesis testing](03-hypothesis-testing.md#example-3-an-ab-test-with-two-proportions) had $z = 1.928$ and a two-sided p-value of 0.0538. What chi-square statistic and p-value does the same test give on the 2 by 2 table of sign-ups?

<details class="solution" markdown>
<summary>Answers</summary>

1. A fair die gives an expected count of $60 \div 6 = 10$ per face, so $\chi^2 = \frac{25 + 4 + 1 + 4 + 0 + 100}{10} = 13.4$. That is above 11.07, so the claim is rejected at the 5% level (the p-value is about 0.020). The 20 sixes alone add 10 to the total.
2. Expected count $= \frac{60 \times 70}{100} = 42$. A 2 by 2 table has $(2 - 1)(2 - 1) = 1$ degree of freedom.
3. $z^2 = 1.928^2 \approx 3.72$ with 1 degree of freedom, and the p-value is the same 0.0538. This is the fact that the lesson proves.

</details>

## The idea

A support team believes that Mondays are the worst. Over four weeks they log 500 tickets: 132 on Mondays, 104 on Tuesdays, 88 on Wednesdays, 90 on Thursdays and 86 on Fridays (hypothetical numbers). If tickets arrived evenly, each weekday would get 100. Monday is 32 above that, and the other days are within 14 of it. Is the pattern more than chance?

The tests so far compare one proportion, or two. Here five counts have to be judged together. One z test per weekday would be five tests, with the multiple-testing problem that comes with them. We want one number for the whole pattern. For each weekday, take the gap between the observed count and the expected one, square it so that a shortfall counts as much as an excess, and divide by the expected count so that gaps are on one scale (a gap of 10 means more when you expected 20 than when you expected 2000). Add the five results. For the tickets the total is 14.8.

A total near 0 means the counts match the claim, and a large total means they don't. How large is large? If the claim is true, the total has a known distribution, the chi-square distribution, and the p-value is the area beyond 14.8. The same arithmetic tests a table: the expected counts come from the row and column totals, and the question becomes whether the two variables of the table are related.

![Left: chi-square curves for 1, 2, 4 and 9 degrees of freedom, all skewed to the right, with the 1 df curve shooting up at 0 and the 9 df curve peaking near 7. Right: a histogram of 10,000 simulated chi-square statistics from weeks with no weekday effect, following the 4 df curve, with the observed 14.8 far out in the right tail where the area is 0.0051](../../assets/figures/05-university-core/chi-square-tests-distribution.svg)

In the right panel, 10,000 weeks of 500 tickets were simulated with every weekday equally likely. Only 51 of them reach a statistic of 14.8 or more, which matches the curve's area of 0.0051, about 1 in 200.

## Definitions

The **chi-square distribution** with $\nu$ degrees of freedom, written $\chi^2_\nu$, is the distribution of $Z_1^2 + Z_2^2 + \dots + Z_\nu^2$, where $Z_1, \dots, Z_\nu$ are independent standard normal random variables. The letter $\nu$ is the Greek nu, as in Welch's degrees of freedom in [hypothesis testing](03-hypothesis-testing.md). In plain words: draw $\nu$ standard normal numbers, square each, and add them up. The result is never negative and is skewed to the right, as the left panel above shows.

Its mean is $\nu$ and its variance is $2\nu$. For one squared standard normal, $E[Z^2] = \operatorname{Var}(Z) = 1$, and $\operatorname{Var}(Z^2) = E[Z^4] - 1 = 3 - 1 = 2$, using the fact that $E[Z^4] = 3$. Independent terms add their means and their variances. So a statistic with 4 degrees of freedom is typically near 4, give or take $\sqrt{8} \approx 2.8$. The 5% critical values, the points with 5% of the area to their right, come from software or a table:

| Degrees of freedom $\nu$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 9 |
|---|---|---|---|---|---|---|---|---|
| 5% critical value | 3.841 | 5.991 | 7.815 | 9.488 | 11.070 | 12.592 | 14.067 | 16.919 |

The first value is $1.96^2$, because $Z_1^2$ is beyond $3.841$ exactly when $\lvert Z_1 \rvert$ is beyond 1.96.

A **categorical variable** puts each individual into one of a few categories, such as weekday, plan or browser. The **observed count** $O$ of a category is how many individuals in the sample fall in it. The **expected count** $E$ is how many would fall in it, on average, if the null hypothesis were true. It is usually not a whole number, and you don't round it.

The **chi-square statistic** is

$$
\chi^2 = \sum \frac{(O - E)^2}{E},
$$

summed over all categories (or all cells of a table). In plain words, each category adds its squared gap in units of its expected count. The statistic is 0 when every observed count equals its expected count, and it grows as the gaps grow.

A **goodness-of-fit test** asks whether one categorical variable with $k$ categories has a claimed distribution. The null hypothesis $H_0$ gives the probability $p_i$ of each category $i$, the expected count is $E_i = np_i$, and the test has $\nu = k - 1$ degrees of freedom. The alternative is that at least one probability differs.

A **test of independence** asks whether two categorical variables are independent, using a table of counts with $r$ rows (the categories of one variable) and $c$ columns (the categories of the other). Independence means that every row has the same split across the columns. Under $H_0$ the expected count in the cell in row $i$ and column $j$ is

$$
E_{ij} = \frac{(\text{total of row } i)(\text{total of column } j)}{n},
$$

and the test has $\nu = (r - 1)(c - 1)$ degrees of freedom. The reason for the formula: if the variables are independent, $P(\text{row } i \text{ and column } j) = P(\text{row } i)\,P(\text{column } j)$, each probability is estimated by its share of the total, and $n$ times the product gives $E_{ij}$. In plain words, the expected table has the same row and column totals as the real one and no relationship between rows and columns.

When the groups are fixed in advance, as in an A/B/C test where each version is shown to its own 10,000 visitors, the same computation is called a **test of homogeneity**: each row is a sample, and $H_0$ says the rows share one split across the columns. The arithmetic is identical, and only the wording of $H_0$ changes.

Three conditions make the chi-square curve a good model for the statistic. The data are counts of individuals, each counted once. The individuals are a random sample or were randomly assigned, and are independent of one another. And every expected count is at least 5. The last rule is the same idea as the 10 successes and 10 failures needed for a proportion: each cell's count has to be large enough to behave like a normal variable.

## How to do it

### Where the statistic comes from

With two categories the statistic is something you already know.

*Theorem 1 (two categories).* In $n$ independent trials, each a success with probability $p$, let $X$ be the number of successes. The chi-square statistic for the counts $X$ and $n - X$, with expected counts $np$ and $n(1 - p)$, equals $z^2$, where $z = \frac{X - np}{\sqrt{np(1 - p)}}$ is the usual standardized count.

We know the two observed counts add to $n$, and so do the expected counts. We want to compare $\sum \frac{(O - E)^2}{E}$ with $z^2$. The plan is to show that both gaps are the same number up to sign.

*Proof.* Let $d = X - np$. The gap for failures is $(n - X) - n(1 - p) = -d$, so both gaps square to $d^2$ and

$$
\chi^2 = \frac{d^2}{np} + \frac{d^2}{n(1 - p)} = d^2 \cdot \frac{1}{n}\left(\frac{1}{p} + \frac{1}{1 - p}\right) = \frac{d^2}{np(1 - p)} = z^2. \qquad \blacksquare
$$

Look back: for large $n$, $z$ is close to a standard normal, so $z^2$ is close to $\chi^2_1$, and that is where the chi-square distribution comes from. With $k$ categories there are $k$ standardized gaps $\frac{O - E}{\sqrt{E}}$, each close to a standard normal. They are not independent, because the gaps add to 0 (the observed counts and the expected counts both add to $n$). Once $k - 1$ gaps are known, the last one is fixed, and that costs one degree of freedom: the sum of squares behaves like $\chi^2_{k-1}$. This is the reason for $k - 1$, though the full proof is beyond this lesson.

The same accounting gives $(r - 1)(c - 1)$ for a table. The counts must match the row totals and the column totals, so only $r - 1$ rows and $c - 1$ columns are free, and the remaining cells follow. If you have to estimate $m$ parameters from the data to get the expected counts (the mean of a Poisson distribution, say), subtract $m$ more degrees of freedom.

*Theorem 2 (chi-square is $z^2$ for two proportions).* For a 2 by 2 table with $x_1$ successes among $n_1$ in group 1 and $x_2$ among $n_2$ in group 2, the chi-square statistic for independence equals the square of the pooled two-proportion $z$ statistic from [hypothesis testing](03-hypothesis-testing.md).

We know the expected counts under $H_0$, which says both groups share one rate: with $N = n_1 + n_2$ and the pooled proportion $\hat{p} = \frac{x_1 + x_2}{N}$, they are $n_1\hat{p}$ and $n_1(1 - \hat{p})$ for group 1, and $n_2\hat{p}$ and $n_2(1 - \hat{p})$ for group 2. We want to show that $\chi^2 = \frac{d^2}{\hat{p}(1 - \hat{p})\left(\frac{1}{n_1} + \frac{1}{n_2}\right)}$, where $d = \hat{p}_1 - \hat{p}_2$ is the difference of the sample proportions. The plan is to handle each group as in Theorem 1 and then express the gaps through $d$.

*Proof.* In group 1 the gap for successes is $x_1 - n_1\hat{p} = n_1(\hat{p}_1 - \hat{p})$, and the gap for failures is its negative. As in Theorem 1, group 1 contributes

$$
n_1^2(\hat{p}_1 - \hat{p})^2\left(\frac{1}{n_1\hat{p}} + \frac{1}{n_1(1 - \hat{p})}\right) = \frac{n_1(\hat{p}_1 - \hat{p})^2}{\hat{p}(1 - \hat{p})},
$$

and group 2 contributes $\frac{n_2(\hat{p}_2 - \hat{p})^2}{\hat{p}(1 - \hat{p})}$. Because $\hat{p} = \frac{n_1\hat{p}_1 + n_2\hat{p}_2}{N}$, we get $\hat{p}_1 - \hat{p} = \frac{n_2}{N}d$ and $\hat{p}_2 - \hat{p} = -\frac{n_1}{N}d$. Adding the two contributions gives

$$
\chi^2 = \frac{1}{\hat{p}(1 - \hat{p})}\left(n_1\frac{n_2^2}{N^2} + n_2\frac{n_1^2}{N^2}\right)d^2 = \frac{n_1 n_2}{N}\cdot\frac{d^2}{\hat{p}(1 - \hat{p})}.
$$

Since $\frac{n_1 n_2}{N} = \frac{1}{\frac{1}{n_1} + \frac{1}{n_2}}$, this is $z^2$. $\blacksquare$

Look back: the z test and the chi-square test on a 2 by 2 table are one test in two forms, with the same p-value. The chi-square form loses the sign of the difference and gains the ability to handle more than two groups or more than two categories. The check with real numbers is in the examples and in the code below.

### The steps of a goodness-of-fit test

1. State $H_0$ as the probability of each category, and $H_a$ as "at least one is different". Choose $\alpha$.
2. Compute the expected counts $E_i = np_i$. Check that every one is at least 5 and that the data are counts of independent individuals.
3. Compute $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$.
4. The degrees of freedom are $k - 1$. Find the p-value as the area to the right of the statistic under $\chi^2_{k-1}$. It is the upper tail only, with no doubling.
5. Decide: reject $H_0$ if $p \le \alpha$.
6. If you reject, find where the gap is. Look at each category's share $\frac{(O - E)^2}{E}$ of the total and at the sign of $O - E$.

### The steps of a test of independence

1. State $H_0$: the two variables are independent, which means the split across columns is the same in every row. $H_a$ says they are associated. Choose $\alpha$.
2. Find the row totals, the column totals and $n$. Compute $E_{ij} = \frac{(\text{row } i)(\text{column } j)}{n}$ for every cell and check that all are at least 5.
3. Compute $\chi^2 = \sum \frac{(O - E)^2}{E}$ over all cells.
4. The degrees of freedom are $(r - 1)(c - 1)$. Find the upper-tail p-value and decide.
5. Describe the association with the percentages within each row, and look at the cells that add the most to the total.

## Worked examples

<div class="example" markdown>

### Example 1: support tickets by weekday

A support team logs 500 tickets over four weeks, 132 on Mondays, 104 on Tuesdays, 88 on Wednesdays, 90 on Thursdays and 86 on Fridays (hypothetical numbers). Test at the 5% level whether tickets are spread evenly over the five weekdays.

Step 1: $H_0$ says that each weekday has probability $\frac{1}{5}$, and $H_a$ says that at least one weekday differs. $\alpha = 0.05$.

Step 2: the expected count is $500 \times \frac{1}{5} = 100$ for every weekday, well above 5. The data are counts of separate tickets, so we treat them as independent.

Step 3:

$$
\chi^2 = \frac{(132 - 100)^2}{100} + \frac{(104 - 100)^2}{100} + \frac{(88 - 100)^2}{100} + \frac{(90 - 100)^2}{100} + \frac{(86 - 100)^2}{100} = \frac{1024 + 16 + 144 + 100 + 196}{100} = 14.8.
$$

Step 4: there are $5 - 1 = 4$ degrees of freedom. The 5% critical value is 9.488, and the p-value is $P(\chi^2_4 \ge 14.8) \approx 0.0051$, the shaded area in the first figure.

<div class="warning" markdown>

Watch out at Step 4: a large statistic is the evidence, so only the right tail counts. Don't double the area as you would for a two-sided z test.

</div>

Step 5: $14.8 > 9.488$ and $0.0051 < 0.05$, so reject $H_0$. The tickets are not spread evenly over the weekdays.

Step 6: the figure shows each day's share of the 14.8. Monday adds 10.24, about 69% of the total, and its count is 32% above the expected 100. The other four days add 4.56 between them, and none is far from 100.

![Bars of support tickets by weekday against a dashed line at the expected 100: Monday 132 in red, Tuesday 104, Wednesday 88, Thursday 90 and Friday 86 in gray, with the share each day adds to the chi-square statistic written inside each bar: 10.24, 0.16, 1.44, 1.00 and 1.96](../../assets/figures/05-university-core/chi-square-tests-tickets.svg)

Check: the observed counts and the expected counts both add to 500, and the five shares add to $10.24 + 0.16 + 1.44 + 1.00 + 1.96 = 14.80$. The statistic, 14.8, is well above the typical value 4 for four degrees of freedom.

</div>

<div class="example" markdown>

### Example 2: plan and cancelling

A subscription app records, for 800 users, their plan and whether they cancelled within 90 days (hypothetical numbers). Of 300 Free users, 90 cancelled. Of 300 Basic users, 60 cancelled. Of 200 Pro users, 30 cancelled. Test whether plan and cancelling are associated.

Step 1: $H_0$ says that plan and cancelling are independent, so every plan has the same cancel rate. $H_a$ says they are associated. $\alpha = 0.05$.

Step 2: in total 180 users cancelled and 620 stayed. The expected counts are $E = \frac{(\text{row})(\text{column})}{800}$:

| Plan | Cancelled: observed (expected) | Stayed: observed (expected) | Row total |
|---|---|---|---|
| Free | 90 (67.5) | 210 (232.5) | 300 |
| Basic | 60 (67.5) | 240 (232.5) | 300 |
| Pro | 30 (45) | 170 (155) | 200 |
| Column total | 180 | 620 | 800 |

For example, the Free and cancelled cell has $\frac{300 \times 180}{800} = 67.5$. All six expected counts are at least 45, so the condition holds.

Step 3: the six cells add

$$
\frac{22.5^2}{67.5} + \frac{22.5^2}{232.5} + \frac{7.5^2}{67.5} + \frac{7.5^2}{232.5} + \frac{15^2}{45} + \frac{15^2}{155} = 7.50 + 2.18 + 0.83 + 0.24 + 5.00 + 1.45 = 17.20.
$$

Step 4: $\nu = (3 - 1)(2 - 1) = 2$. The critical value is 5.991, and the p-value is about 0.00018. Reject $H_0$.

Step 5: the cancel rates are 30% for Free, 20% for Basic and 15% for Pro, against 22.5% overall. Free users cancel more than independence predicts (90 against 67.5) and Pro users cancel less (30 against 45). Those two cancelled cells add 12.5 of the 17.2.

The test says that plan and cancelling are associated. It doesn't say that the plan causes the cancelling. Heavy users may choose Pro and also be the ones who stay, which is confounding, as in [study design](01-descriptive-statistics-and-study-design.md#judge-a-study).

Check: each row of expected counts adds to its row total ($67.5 + 232.5 = 300$, and $45 + 155 = 200$), and each column adds to its column total ($67.5 + 67.5 + 45 = 180$).

</div>

<div class="example" markdown>

### Example 3: an A/B/C test

The A/B test of [hypothesis testing](03-hypothesis-testing.md) gave 480 sign-ups from 10,000 visitors for version A and 540 for version B. Add version C, with 590 sign-ups from 10,000 visitors (hypothetical). Do the three versions have the same sign-up rate?

The table has three rows and two columns, with 1,610 sign-ups among 30,000 visitors, an overall rate of 5.37%. Under $H_0$ each version expects $10{,}000 \times 0.05367 = 536.67$ sign-ups and $9463.33$ non-sign-ups. The sign-up cells of A, B and C add $\frac{(480 - 536.67)^2}{536.67} + \frac{(540 - 536.67)^2}{536.67} + \frac{(590 - 536.67)^2}{536.67} = 5.983 + 0.021 + 5.300$. The three non-sign-up cells add $0.339 + 0.001 + 0.301$, so

$$
\chi^2 = 5.983 + 0.021 + 5.300 + 0.339 + 0.001 + 0.301 \approx 11.95.
$$

There are $(3 - 1)(2 - 1) = 2$ degrees of freedom, so the p-value is $P(\chi^2_2 \ge 11.95) \approx 0.0025$, and we reject: the three rates are not all equal.

That is all the test says. It doesn't say which version differs. A and B alone gave $p = 0.0538$. Pairwise z tests (which by Theorem 2 are chi-square tests on 2 by 2 tables) give $p = 0.0538$ for A against B, $p = 0.00055$ for A against C and $p = 0.126$ for B against C. With three comparisons, Bonferroni's cutoff is $\frac{0.05}{3} = 0.0167$, and only A against C passes. The follow-up comparisons are a multiple-testing problem of their own, the subject of [Multiple testing and p-hacking](07-multiple-testing-and-p-hacking.md).

The result is also small. The 95% interval for C minus A is $0.011 \pm 1.96 \times 0.00318$, about 0.5 to 1.7 percentage points. The test is significant because $n = 30{,}000$ is large, not because the difference is big.

Check: the three expected sign-up counts add to $3 \times 536.67 = 1610$, the observed total, and the six terms add to 11.95.

</div>

<div class="example" markdown>

### Example 4: when the expected counts are too small

A team compares two release processes with 20 deployments each (hypothetical). With the new process, 2 of the 20 deployments were rolled back, and with the old one, 6 of 20. Is the rollback rate different?

There are 8 rollbacks and 32 clean deployments among 40, so each process expects $20 \times \frac{8}{40} = 4$ rollbacks. That is below 5, so the condition fails. If we ignore the rule, $\chi^2 = 2.5$ and the p-value is 0.114, with $\nu = 1$.

Fisher's exact test doesn't use the chi-square curve. With the row and column totals held fixed, it counts how likely every possible table is, and adds up the probabilities of the tables at least as unusual as this one. Its p-value is 0.235, about twice the chi-square value. The uncorrected statistic made the evidence look twice as strong as it is. Software also offers Yates's continuity correction, which shrinks each gap $\lvert O - E \rvert$ by 0.5 and gives $\chi^2 = 1.41$ and $p = 0.236$, close to the exact answer.

Either way, 2 rollbacks against 6 is not convincing evidence with 20 deployments each.

Check: $\frac{20 \times 8}{40} = 4$ for each rollback cell and $\frac{20 \times 32}{40} = 16$ for each clean cell, and the smallest of the four is 4.

</div>

<div class="example" markdown>

### Example 5: does a hash function spread keys evenly? (finish it yourself)

A hash function sends 800 keys into 8 buckets (hypothetical run). The bucket counts are 112, 95, 104, 88, 99, 107, 93 and 102. $H_0$ says every bucket has probability $\frac{1}{8}$. The expected count is $800 \times \frac{1}{8} = 100$ per bucket, well above 5, and $\nu = 8 - 1 = 7$. The 5% critical value for 7 degrees of freedom is 14.067.

Compute the statistic and decide.

<details class="solution" markdown>
<summary>Finish</summary>

The gaps $O - E$ are $12, -5, 4, -12, -1, 7, -7, 2$, and the squares divided by 100 are $1.44, 0.25, 0.16, 1.44, 0.01, 0.49, 0.49, 0.04$. They add to $\chi^2 = 4.32$. Since $4.32 < 14.067$, we fail to reject $H_0$ (the p-value is about 0.74). The counts are as even as a fair spread would usually be: the typical statistic for 7 degrees of freedom is 7, and 4.32 is below it.

This doesn't prove that the hash function is perfect, only that this run shows no sign of uneven spreading.

Check: the counts add to $112 + 95 + 104 + 88 + 99 + 107 + 93 + 102 = 800$, and the gaps add to 0.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: use counts, not percentages or proportions. The formula needs the real counts because the statistic grows with $n$. If you put the weekday tickets in as percentages (26.4, 20.8, 17.6, 18.0 and 17.2 against an expected 20), you get $\chi^2 = 2.96$ instead of 14.8, and a p-value of 0.56 instead of 0.0051. The percentages carry the same pattern with the sample size thrown away.

</div>

<div class="warning" markdown>

Watch out: expected counts below 5. The chi-square curve is an approximation, and it is poor when cells are small, as Example 4 showed. Merge categories that make sense together (a rare category with its nearest neighbour), use Fisher's exact test for a 2 by 2 table, or use a simulation, which is the idea of the next lesson, [The bootstrap and permutation tests](06-bootstrap-and-permutation-tests.md). Check the expected counts, not the observed ones. A table can have large observed counts and still have small expected ones.

</div>

<div class="warning" markdown>

Watch out: "significant" doesn't say where, or how strongly. A significant statistic says that the counts are not what $H_0$ predicts, with no word on which cells are off or how large the association is. Look at each cell's share of the total, and at the percentages within rows. For strength, use Cramér's V (in the tricks below). In Example 3 the p-value was 0.0025 and the association was tiny.

</div>

<div class="warning" markdown>

Watch out: an association is not a cause, and a combined table can reverse the story. The combined table of [Example 3 of study design](01-descriptive-statistics-and-study-design.md#example-3-simpsons-paradox-in-an-ab-test), 48 of 1000 against 84 of 1000, gives $\chi^2 = 10.5$ and $p = 0.0012$ in favour of B, while A converts better on both desktop and mobile. A chi-square test on the combined table answers a question about the combined table. It can't repair a confounder that the table leaves out.

</div>

<div class="warning" markdown>

Watch out: the observations must be independent, and each individual counted once. If the 500 tickets came from 40 customers who write many tickets each, the tickets are not independent, and the p-value is too small. The same goes for counting one user's ten clicks as ten observations. Count users, or use a method built for repeated measurements.

</div>

Two smaller points. The test has no direction: squaring removes the sign, so a significant 2 by 2 table doesn't say which group is higher, and you read that from the percentages (or use the z form of Theorem 2, which keeps the sign). And a statistic far below its degrees of freedom is also unusual. A $\chi^2$ near 0 means that the counts match the claim more closely than chance usually allows, which is worth a look at how the counts were produced, though the test is only built to find mismatches.

## Tricks and shortcuts

To find an expected count, multiply the row total by the column total and divide by $n$. A cheap check on the whole expected table is that each row and each column of it adds up to the same total as the observed table.

In a 2 by 2 table all four gaps $\lvert O - E \rvert$ are the same number, so the statistic needs only one of them. With the cells $a, b$ in the first row and $c, d$ in the second, and $N = a + b + c + d$,

$$
\chi^2 = \frac{N(ad - bc)^2}{(a + b)(c + d)(a + c)(b + d)}.
$$

For the A/B table with $a = 480$, $b = 9520$, $c = 540$ and $d = 9460$, this gives $\frac{20000 \times (-600000)^2}{10000 \times 10000 \times 1020 \times 18980} = 3.719$. Practice problem 7 derives the formula.

Compare the statistic with its degrees of freedom first. The mean of $\chi^2_\nu$ is $\nu$ and its standard deviation is $\sqrt{2\nu}$. A statistic near $\nu$ shows nothing, and one several $\sqrt{2\nu}$ above $\nu$ is a signal. For 4 degrees of freedom, 14.8 is $\frac{14.8 - 4}{2.83} \approx 3.8$ standard deviations above the mean.

To find the cells behind a rejection, compute the standardized gap $\frac{O - E}{\sqrt{E}}$ for each. As a rough guide, a gap beyond about 2 in size marks a cell worth a look. In Example 1, Monday's is $\frac{32}{10} = 3.2$ and no other day is beyond 1.4.

For the strength of an association, use Cramér's V, $V = \sqrt{\frac{\chi^2}{n\,(\min(r, c) - 1)}}$. It runs from 0 to 1 and doesn't grow with $n$. For a 2 by 2 table it is the absolute value of the correlation between the two variables coded 0 and 1, as in [correlation and linear regression](04-correlation-and-linear-regression.md). In Example 2, $V = \sqrt{\frac{17.2}{800}} \approx 0.15$, a modest association. In Example 3, $V \approx 0.02$, a tiny one, despite $p = 0.0025$.

## In code

SciPy has the whole procedure (install it once with `pip install scipy`). `stats.chisquare` does a goodness-of-fit test, and `stats.chi2_contingency` does the test of independence and returns the expected counts. For 2 by 2 tables, `chi2_contingency` applies Yates's correction by default, so use `correction=False` when you compare it with the z test.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
from scipy import stats            # pip install scipy

# 1. Goodness of fit: 500 support tickets over five weekdays, expected 100 each.
tickets = [132, 104, 88, 90, 86]
stat, p = stats.chisquare(tickets)
print(round(stat, 2), round(p, 4))
# 14.8 0.0051

# 2. Independence: plan (rows: Free, Basic, Pro) by outcome (columns: cancelled, stayed).
plans = np.array([[90, 210], [60, 240], [30, 170]])
stat, p, dof, expected = stats.chi2_contingency(plans)
print(round(stat, 2), dof, round(p, 5))
print(expected)
# 17.2 2 0.00018
# [[ 67.5 232.5]
#  [ 67.5 232.5]
#  [ 45.  155. ]]

# 3. An A/B/C test: sign-ups out of 10,000 visitors per version.
abc = np.array([[480, 9520], [540, 9460], [590, 9410]])
stat, p, dof, expected = stats.chi2_contingency(abc)
print(round(stat, 2), dof, round(p, 4))
# 11.95 2 0.0025

# 4. With one degree of freedom, chi-square is z squared (correction=False turns off Yates' correction).
x, n = np.array([480, 540]), np.array([10_000, 10_000])
pooled = x.sum() / n.sum()
z = (x[1] / n[1] - x[0] / n[0]) / np.sqrt(pooled * (1 - pooled) * (1 / n[0] + 1 / n[1]))
stat, p, dof, expected = stats.chi2_contingency([[480, 9520], [540, 9460]], correction=False)
print(round(z**2, 4), round(stat, 4))
print(round(2 * stats.norm.sf(abs(z)), 4), round(p, 4))
# 3.7191 3.7191
# 0.0538 0.0538

# 5. Small expected counts: the chi-square p-value is too small, Fisher's exact test is safe.
rollbacks = np.array([[2, 18], [6, 14]])
stat, p, dof, expected = stats.chi2_contingency(rollbacks, correction=False)
print(round(stat, 2), round(p, 3), expected.min())
print(round(stats.fisher_exact(rollbacks).pvalue, 3))
# 2.5 0.114 4.0
# 0.235

# 6. The chi-square distribution as a sum of squared standard normals.
rng = np.random.default_rng(0)
squares = (rng.standard_normal((100_000, 4)) ** 2).sum(axis=1)
print(round(squares.mean(), 2), round(squares.var(), 2), round((squares > 9.488).mean(), 3))
# 4.01 8.04 0.05
```

The z test and the chi-square test give the same p-value, 0.0538, as Theorem 2 says. In the simulation the mean is close to 4 and the variance close to 8, which are $\nu$ and $2\nu$ for 4 degrees of freedom, and 5% of the values are beyond the critical value 9.488. If the test has estimated parameters, `stats.chisquare` takes `ddof` to remove the extra degrees of freedom.

</details>

## FAQ

### Why divide by the expected count?

Because a count's natural wobble grows with its size. For a count with expected value $E$ in a large sample, the standard deviation is about $\sqrt{E}$, so $\frac{O - E}{\sqrt{E}}$ is close to a standard normal. Squaring and adding gives the sum of squared standard normals that defines the chi-square distribution. Dividing by $E$ is what puts every cell on that one scale. Without it a gap of 10 would count the same in a cell expecting 20 and a cell expecting 2000.

### Why is only the upper tail used?

Squaring turns every gap, positive or negative, into a positive contribution, so any mismatch pushes the statistic up. A small statistic means the counts fit the claim well, and there is nothing to test there. The chi-square test is therefore a one-tailed test that detects any kind of departure from $H_0$, in any direction, at once.

### What if my expected counts are too small?

Merge categories that belong together, use Fisher's exact test if the table is 2 by 2, or simulate the null distribution, which works for any table. Example 4 shows how far off the chi-square p-value can be.

### When should I use the z test and when the chi-square test?

For a 2 by 2 table they have the same p-value. The z form keeps the sign and gives a confidence interval for the difference, so it says which group is higher and by how much. The chi-square form is the one that extends to three or more groups or categories, as in the A/B/C test.

## Practice

### Warm-up

1\. A survey of 200 students records year of study (first, second, third and fourth: 60, 50, 50 and 40 students) and the operating system of their laptop (Windows 90, macOS 70, Linux 40). Find the expected count for first-year students with macOS, and the degrees of freedom of the test of independence.

<details class="solution" markdown>
<summary>Solution</summary>

The expected count is $\frac{60 \times 70}{200} = 21$. The table has 4 rows and 3 columns, so $\nu = (4 - 1)(3 - 1) = 6$.

Check: the first-year row of expected counts is $27, 21, 12$, from $\frac{60 \times 90}{200}$, $\frac{60 \times 70}{200}$ and $\frac{60 \times 40}{200}$, and it adds to 60, the first-year total.

</details>

2\. A die is rolled 120 times, and faces 1 to 6 come up 18, 22, 25, 14, 21 and 20 times. Test at the 5% level whether the die is fair. The critical value for 5 degrees of freedom is 11.07.

<details class="solution" markdown>
<summary>Solution</summary>

The expected count is 20 per face. The shares $\frac{(O - E)^2}{20}$ are $0.2, 0.2, 1.25, 1.8, 0.05$ and $0$, so $\chi^2 = 3.5$ with $\nu = 5$. Since $3.5 < 11.07$, we fail to reject $H_0$ (the p-value is about 0.62). The counts are consistent with a fair die.

Check: the counts add to 120, and 3.5 is below the mean 5 of $\chi^2_5$, so nothing is unusual.

</details>

3\. Which of these meet the condition that every expected count is at least 5? (a) A goodness-of-fit test with 30 observations and 4 equally likely categories. (b) A 2 by 2 table with row totals 50 and 10, column totals 54 and 6, and $n = 60$. (c) 60 observations in 3 categories with claimed probabilities 0.5, 0.45 and 0.05.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Each expected count is $\frac{30}{4} = 7.5$, so it meets the condition. (b) The smallest expected count is $\frac{10 \times 6}{60} = 1$, so it fails. (c) The expected counts are $30$, $27$ and $60 \times 0.05 = 3$, so the third fails. Merge the third category into another, or use an exact test.

Check: in (b), the other three cells are $\frac{50 \times 54}{60} = 45$, $\frac{50 \times 6}{60} = 5$ and $\frac{10 \times 54}{60} = 9$, and the four add to 60.

</details>

### Standard

4\. Of 400 mobile users, 130 opened a promotional email, and of 200 desktop users, 90 did (hypothetical). Test at the 5% level whether device and opening are independent. Then check the answer against the pooled two-proportion z test.

<details class="solution" markdown>
<summary>Solution</summary>

Of 600 users, 220 opened the email. The expected counts for opening are $\frac{400 \times 220}{600} = 146.67$ on mobile and $\frac{200 \times 220}{600} = 73.33$ on desktop, and for not opening $253.33$ and $126.67$. All are above 5. Every gap has size $16.67$ (130 against 146.67, and so on), so

$$
\chi^2 = 16.67^2\left(\frac{1}{146.67} + \frac{1}{73.33} + \frac{1}{253.33} + \frac{1}{126.67}\right) = 277.8 \times 0.03230 \approx 8.97.
$$

With $\nu = 1$ the critical value is 3.841 and the p-value is about 0.0027, so reject $H_0$. The open rates are 32.5% on mobile and 45% on desktop.

Check: the pooled z statistic is $\frac{0.45 - 0.325}{\sqrt{0.3667 \times 0.6333 \times \left(\frac{1}{400} + \frac{1}{200}\right)}} = 2.995$, and $2.995^2 = 8.97$. The shortcut formula gives $\frac{600 \times (130 \times 110 - 270 \times 90)^2}{400 \times 200 \times 220 \times 380} = 8.97$ as well.

</details>

5\. A bug tracker expects reports to split 50%, 30%, 15% and 5% across the severities low, medium, high and critical. A month of 400 reports has 188, 134, 58 and 20. Test at the 5% level whether the split has changed. The critical value for 3 degrees of freedom is 7.815.

<details class="solution" markdown>
<summary>Solution</summary>

The expected counts are $400 \times (0.5, 0.3, 0.15, 0.05) = 200, 120, 60, 20$, all at least 5. The shares are $\frac{12^2}{200} = 0.72$, $\frac{14^2}{120} = 1.633$, $\frac{2^2}{60} = 0.067$ and $0$, so $\chi^2 = 2.42$ with $\nu = 3$. Since $2.42 < 7.815$, we fail to reject $H_0$ (the p-value is about 0.49). The month's split is consistent with the expected one.

Check: both sets of counts add to 400, and the largest share, 1.633, comes from the medium reports, which are 14 above the expected 120.

</details>

6\. Three email subject lines are each sent to 500 people, and 100, 120 and 140 open the email (hypothetical). (a) Test at the 5% level whether the three open rates are equal. (b) Run the three pairwise z tests, using Bonferroni's cutoff $\frac{0.05}{3}$, and say which pairs differ.

<details class="solution" markdown>
<summary>Solution</summary>

(a) In total 360 of 1500 opened, a rate of 0.24, so each line expects 120 opens and 380 non-opens. The statistic is $\frac{20^2}{120} + \frac{0^2}{120} + \frac{20^2}{120} + \frac{20^2}{380} + \frac{0^2}{380} + \frac{20^2}{380} = 6.667 + 2.105 = 8.77$ with $\nu = 2$. The critical value is 5.991 and the p-value is about 0.0125, so reject $H_0$.

(b) The pairwise z statistics and p-values are 1.53 and 0.127 for 100 against 120, 2.96 and 0.0031 for 100 against 140, and 1.44 and 0.149 for 120 against 140. Only the pair 100 against 140 has $p < 0.0167$. The two subject lines at the ends differ, and the middle one can't be separated from either.

Check: the expected opens add to $3 \times 120 = 360$, the observed total.

</details>

### Challenge

7\. For a 2 by 2 table with cells $a, b$ in the first row and $c, d$ in the second, and $N = a + b + c + d$, show that every gap $O - E$ has absolute value $\frac{\lvert ad - bc \rvert}{N}$ and that $\chi^2 = \frac{N(ad - bc)^2}{(a + b)(c + d)(a + c)(b + d)}$.

<details class="solution" markdown>
<summary>Solution</summary>

Write $R_1 = a + b$, $R_2 = c + d$, $C_1 = a + c$ and $C_2 = b + d$. The expected count in the first cell is $\frac{R_1 C_1}{N}$, so

$$
a - E_{11} = \frac{aN - R_1 C_1}{N} = \frac{a(a + b + c + d) - (a + b)(a + c)}{N} = \frac{ad - bc}{N}.
$$

The observed and expected counts have the same row totals and column totals, so each row and each column of the table of gaps adds to 0. The first row is $(a - E_{11}) + (b - E_{12}) = 0$, so $b - E_{12} = -(a - E_{11})$, and the same argument gives the other two cells. All four gaps have absolute value $D = \frac{\lvert ad - bc \rvert}{N}$.

Then $\chi^2 = D^2\left(\frac{1}{E_{11}} + \frac{1}{E_{12}} + \frac{1}{E_{21}} + \frac{1}{E_{22}}\right)$, and since $\frac{1}{E_{ij}} = \frac{N}{R_i C_j}$, the sum factors as $N\left(\frac{1}{R_1} + \frac{1}{R_2}\right)\left(\frac{1}{C_1} + \frac{1}{C_2}\right) = N \cdot \frac{N}{R_1 R_2} \cdot \frac{N}{C_1 C_2}$. Therefore

$$
\chi^2 = \frac{(ad - bc)^2}{N^2} \cdot \frac{N^3}{R_1 R_2 C_1 C_2} = \frac{N(ad - bc)^2}{R_1 R_2 C_1 C_2}.
$$

Check: for $a = 130$, $b = 270$, $c = 90$ and $d = 110$ (problem 4), $D = \frac{10000}{600} = 16.67$, which is the gap found there, and the formula gives 8.97.

</details>

8\. (Reviews [hypothesis testing](03-hypothesis-testing.md).) A chi-square test on a 2 by 2 table gives $\chi^2 = 6.0$. (a) What is the size of the matching z statistic, and what is the two-sided p-value? (b) Every count in the table is multiplied by 4, so the proportions stay the same. What happens to $\chi^2$, to $z$ and to the p-value, and which idea from the power discussion does this show?

<details class="solution" markdown>
<summary>Solution</summary>

(a) By Theorem 2, $\lvert z \rvert = \sqrt{6.0} \approx 2.449$, and the two-sided p-value is $2 \times P(Z \ge 2.449) \approx 0.0143$. This equals $P(\chi^2_1 \ge 6.0)$.

(b) In the formula of Theorem 2, $\frac{n_1 n_2}{N}$ is multiplied by 4 while the proportions stay fixed, so $\chi^2 = 24.0$, and $z = \sqrt{24} \approx 4.90$, which is double the old value. The p-value drops to about $10^{-6}$ (9.6 in ten million). The same difference in proportions becomes much easier to detect with four times the data: the standard error halves, and the statistic doubles. This is the rule that power grows with $n$, and that halving the standard error takes four times the sample.

Check: $2 \times 2.449 = 4.899$, and $4.899^2 = 24.0$.

</details>

## Where this shows up

- In this chapter, [The bootstrap and permutation tests](06-bootstrap-and-permutation-tests.md) give a way to test a table when the expected counts are too small for the chi-square curve, and [Multiple testing and p-hacking](07-multiple-testing-and-p-hacking.md) covers what to do with the pairwise follow-ups after an A/B/C test.
- In CS, checking that a hash function or a random number generator spreads values evenly over buckets is a goodness-of-fit test, as in Example 5. A/B/C and multi-variant tests on conversion counts use the test of homogeneity, and scikit-learn's `feature_selection.chi2` scores count features against class labels with the chi-square statistic. The probability behind the distribution is in [the law of large numbers and the CLT](../07-probability/06-law-of-large-numbers-and-clt.md) and [discrete probability](../../06-cs-math/03-counting-and-discrete-probability/05-discrete-probability.md).
- In economics, survey tables, such as employment status by education level, are the data a test of independence is built for ([unemployment rate and labour statistics](../../07-economics-math/01-measuring-the-economy/08-unemployment-rate-and-labour-statistics.md)), and association alone never settles cause ([regression and econometrics intuition](../../07-economics-math/04-more-tools/03-regression-and-econometrics-intuition.md)).
