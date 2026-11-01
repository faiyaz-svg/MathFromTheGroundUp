# Multiple testing and p-hacking

After this lesson you can work out the chance of a false positive across many tests, apply the Bonferroni, Holm and Benjamini-Hochberg procedures, tell the family-wise error rate from the false discovery rate, show how peeking at a running A/B test inflates false positives, and spot forking paths in dashboards and model selection.

Before this: [hypothesis testing](03-hypothesis-testing.md#edge-cases-and-common-mistakes) (the first look at multiple testing and p-hacking), [Chi-square tests](05-chi-square-tests.md) (follow-up comparisons after an A/B/C test) and [The bootstrap and permutation tests](06-bootstrap-and-permutation-tests.md) (simulating a null distribution). The binomial distribution is in [discrete random variables](../07-probability/03-discrete-random-variables.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Two versions of a page are identical, and a team compares them on 10 independent metrics at the 5% level. What is the probability that at least one metric looks significant? What cutoff does the Bonferroni correction use for each metric?
2. Four p-values are 0.003, 0.02, 0.04 and 0.30. Which does the Benjamini-Hochberg procedure reject at $q = 0.05$, using the cutoffs $\frac{k}{4} \times 0.05$ for rank $k$?
3. A team checks a running A/B test every day and stops at the first day with $p < 0.05$. If the two versions are identical, is the chance of declaring a winner below 5%, exactly 5%, or above 5%?

<details class="solution" markdown>
<summary>Answers</summary>

1. $1 - 0.95^{10} = 0.401$, about 40%. Bonferroni tests each metric at $\frac{0.05}{10} = 0.005$.
2. The cutoffs for ranks 1 to 4 are $0.0125$, $0.025$, $0.0375$ and $0.05$. The p-values 0.003 and 0.02 pass theirs, while 0.04 is above $0.0375$ and 0.30 is above 0.05. The largest rank that passes is 2, so BH rejects the first two. Bonferroni, with cutoff $\frac{0.05}{4} = 0.0125$, rejects only 0.003.
3. Above 5%. Each look is another chance for a fluke, and the lesson's simulation puts it at about 22% for 14 daily looks.

</details>

## The idea

A team runs an A/B test and opens a dashboard with 50 metrics: sign-ups, clicks, time on page, error rates, and so on. The two versions are in fact identical, so every null hypothesis is true. Each metric still has a 5% chance of showing $p < 0.05$, so the team should expect $50 \times 0.05 = 2.5$ "significant" metrics, and the chance that at least one appears is $1 - 0.95^{50} = 92\%$. A lone green number on the dashboard tells you very little, because the dashboard was built to produce one.

[Hypothesis testing](03-hypothesis-testing.md#edge-cases-and-common-mistakes) introduced the formula $1 - 0.95^m$, the Bonferroni correction and the idea of p-hacking. This lesson takes them further. It explains why Bonferroni works and what it costs, adds two better procedures (Holm and Benjamini-Hochberg), and then turns to the less obvious sources of the same problem: looking at a running test, trying many analyses, and choosing the best of many models on one test set.

All of these have one shape. You look at many results, keep the best one, and report its p-value as if it were the only one you had. The p-value of the best of many is not the p-value of a single test. It is much smaller than it should be, in the same way that the tallest person in a stadium is taller than a person picked at random.

## Definitions

A **family** of hypotheses is a set of tests that together bear on one decision, such as "do we ship version B?" decided by any of 50 metrics. The number of tests in the family is $m$. How to draw the family is a judgment about the decision, not something the data settle.

The **family-wise error rate** (FWER) is the probability of at least one false rejection in the family, $P(V \ge 1)$, where $V$ is the number of true null hypotheses that were rejected. A procedure **controls the FWER at level $\alpha$** if this probability is at most $\alpha$ whatever the truth. In plain words, FWER control means: with high probability, no false leads at all.

Let $R$ be the number of rejections. The **false discovery proportion** is $\frac{V}{R}$ (taken as 0 when $R = 0$), the share of the rejections that were false. The **false discovery rate** (FDR) is its expected value,

$$
\text{FDR} = E\left[\frac{V}{\max(R, 1)}\right].
$$

In plain words, FDR control means that on average, at most a share $q$ of your list of discoveries is false leads. It allows some false leads in return for finding more real effects.

A p-value is **valid** for a true null hypothesis when $P(p \le t) \le t$ for every $t$ between 0 and 1. Every test in [hypothesis testing](03-hypothesis-testing.md) has this property.

The **Bonferroni correction** rejects hypothesis $i$ when $p_i \le \frac{\alpha}{m}$. **Holm's method** sorts the p-values, $p_{(1)} \le \dots \le p_{(m)}$, and rejects ranks $1, 2, \dots$ in turn as long as $p_{(i)} \le \frac{\alpha}{m - i + 1}$, stopping at the first failure. The **Benjamini-Hochberg procedure** (BH) sorts the p-values, finds the largest rank $k$ with $p_{(k)} \le \frac{k}{m}q$, and rejects ranks $1, \dots, k$. Both Holm and BH are described in steps below.

An **adjusted p-value** for a procedure is the smallest level at which the procedure would reject that hypothesis. You then reject when the adjusted p-value is at most the level you chose.

Three words for the less formal side. **Optional stopping**, or peeking, is deciding when to stop collecting data by looking at the results so far. **P-hacking** is trying analyses, outcomes, subgroups or stopping times until one gives $p < 0.05$, and reporting that one. The **garden of forking paths** is the same trap without bad intent: when the analysis choices were made after seeing the data, the number of tests that matter is the number you might have run, not the number you ran. **Preregistration** is writing down the hypothesis, the outcomes, the exclusion rules, the analysis and the stopping rule before collecting data.

## How to do it

### Why Bonferroni works

*Theorem 1 (Bonferroni).* Run $m$ tests, of which $m_0$ have a true null hypothesis, and reject hypothesis $i$ when $p_i \le \frac{\alpha}{m}$. Whether or not the tests are independent, the probability of at least one false rejection is at most $\alpha$.

We know that each true null has a valid p-value, so it falls at or below $\frac{\alpha}{m}$ with probability at most $\frac{\alpha}{m}$. We want the chance that any of the true nulls does. The plan is to bound the chance of a union of events by the sum of their chances.

*Proof.* Let $A_i$ be the event that true null $i$ is rejected. Then $P(A_i) = P\left(p_i \le \frac{\alpha}{m}\right) \le \frac{\alpha}{m}$. The probability of a union is at most the sum of the probabilities, so

$$
P(\text{at least one false rejection}) = P\left(\bigcup_{i \text{ true}} A_i\right) \le \sum_{i \text{ true}} P(A_i) \le m_0 \cdot \frac{\alpha}{m} \le \alpha. \qquad \blacksquare
$$

Look back: the proof never uses independence, only that a probability of a union is at most the sum. That is why Bonferroni is safe for any set of tests, however they are related. The price is that it is conservative when the tests overlap, since the union bound then counts the same events twice. If the tests are independent, the exact chance is $1 - \left(1 - \frac{\alpha}{m}\right)^m$, which is 0.0488 for every $m$ from 20 to 100, a little below $\alpha$. The other price is power: a two-sided $z$ test at the 5% FWER needs $\lvert z \rvert > 2.81$ for $m = 10$, $3.02$ for $m = 20$, $3.29$ for $m = 50$ and $3.48$ for $m = 100$, against 1.96 for a single test.

### Holm: Bonferroni, improved

Holm's method uses Bonferroni's cutoff for the smallest p-value and relaxes it as hypotheses are rejected, because each rejection leaves fewer hypotheses that could still be true nulls. It has the same guarantee as Bonferroni for any dependence among the tests, and it never rejects fewer: its first cutoff is $\frac{\alpha}{m}$ and the later ones are larger. The proof applies the union bound to the true nulls, and is left out here. Practice problem 7 in [hypothesis testing](03-hypothesis-testing.md#practice) is a worked case.

### The false discovery rate and Benjamini-Hochberg

Sometimes the goal is not "no false leads" but "a short list worth following up, mostly true". A screen of 12 metrics, or 20,000 genes, or 500 candidate features, is followed by more checking, so a few false leads are acceptable. FDR control is built for that. The procedure:

1. Sort the $m$ p-values from smallest to largest: $p_{(1)} \le p_{(2)} \le \dots \le p_{(m)}$.
2. Choose the target $q$ (often 0.05) and compute the cutoff $\frac{k}{m}q$ for each rank $k$.
3. Find the largest $k$ with $p_{(k)} \le \frac{k}{m}q$.
4. Reject the hypotheses with ranks $1, \dots, k$.

Step 3 is "the largest", not "the first to fail". If rank 4 misses its cutoff but rank 5 meets its own, all five are rejected (Example 5).

Benjamini and Hochberg (1995, [Journal of the Royal Statistical Society, Series B](https://doi.org/10.1111/j.2517-6161.1995.tb02031.x)) proved that when the tests are independent, the FDR of this procedure is at most $q$, in fact $q\frac{m_0}{m}$. It is also valid under some kinds of positive dependence between the tests. We use the result without proving it.

The cutoffs $\frac{k}{m}q$ rise with the rank. If many hypotheses are false, many p-values are small, and BH can afford looser cutoffs, since a few false leads are a small share of a long list. Holm and Bonferroni can't, because they guard against any false lead at all. With $q = \alpha$, BH never rejects fewer than Holm: its cutoff at rank $i$ is $\frac{i\alpha}{m}$ and Holm's is $\frac{\alpha}{m - i + 1}$, and $\frac{i}{m} - \frac{1}{m - i + 1} = \frac{(i - 1)(m - i)}{m(m - i + 1)} \ge 0$. The picture below shows the three cutoffs for the 12 p-values of Example 1.

![Twelve sorted p-values plotted against their rank, with a flat red line at the Bonferroni cutoff 0.0042, a sloping blue line for the Benjamini-Hochberg cutoff 0.05 times rank over 12 which rises to 0.05 at rank 12, and a dashed gray line at 0.05. The first five points, in green, are on or below the blue line, and the points for ranks 6 to 9 are above it](../../assets/figures/05-university-core/multiple-testing-and-p-hacking-bh.svg)

### Peeking at a running test

A running A/B test accumulates users, and its $z$ statistic changes every day. If there is no real difference, the statistic wanders around 0 like a random walk, scaled down as the sample grows. A single look at a planned time has a 5% chance of landing beyond $\pm 1.96$. But the statistic gets many chances to wander past the line, and stopping at the first crossing keeps only the lucky path.

The size of the damage depends on the number of looks. It has no tidy formula in this lesson, so it is found by simulation (Example 2). The remedies, from simplest to most refined, are these:

- Decide the sample size in advance from a power calculation, as in [hypothesis testing](03-hypothesis-testing.md#power-and-sample-size), look once, and say that you did.
- Use a Bonferroni cutoff for the number of planned looks. It is valid and wasteful, since looks at accumulating data are strongly correlated.
- Use a method designed for repeated looks: group sequential designs, which use stricter cutoffs at early looks, or always-valid p-values, such as those of Johari, Koomen, Pekelis and Walsh in [Peeking at A/B Tests](https://doi.org/10.1145/3097983.3097992) (KDD 2017), which A/B testing platforms use.

### Forking paths and preregistration

Simmons, Nelson and Simonsohn showed in [False-Positive Psychology](https://doi.org/10.1177/0956797611417632) (*Psychological Science*, 2011), using simulations, that ordinary flexibility in how a study is run and analyzed makes it easy to reach $p < 0.05$ for a hypothesis that is false. The flexibility is in choices such as when to stop, which outcome to report, which covariates to adjust for, and which observations to exclude. Gelman and Loken, in "The garden of forking paths" (2013), pointed out that the problem doesn't need a researcher who tries many analyses on purpose. If the analysis chosen depends on how the data came out, then a different data set would have led to a different analysis, and the p-value doesn't account for that.

Count the forks. Two outcomes, two ways to treat outliers and three subgroups already make $2 \times 2 \times 3 = 12$ analyses that someone could have reported, and the chance of at least one $p < 0.05$ among 12 tests of pure noise is up to $1 - 0.95^{12} = 46\%$ if they were independent (they are not, since they use the same data, which lowers the number, but not to 5%). Two defences work. Preregistration fixes the analysis before the data arrive, so there is one fork. Sample splitting explores on one part of the data and confirms on the rest, or on a fresh experiment, so the confirming test has one fork too.

## Worked examples

<div class="example" markdown>

### Example 1: twelve metrics, four procedures

An experiment compares two versions on 12 metrics and gets these sorted two-sided p-values (hypothetical): 0.001, 0.004, 0.0048, 0.011, 0.019, 0.027, 0.034, 0.042, 0.11, 0.31, 0.58 and 0.83. The team will follow up on any metric that survives. Apply the procedures at the 5% level.

Step 1: with no correction, 8 of the 12 p-values are below 0.05.

Step 2, Bonferroni: the cutoff is $\frac{0.05}{12} = 0.00417$. Only 0.001 and 0.004 pass. That is 2 metrics.

Step 3, Holm: the cutoffs are $\frac{0.05}{12}$, $\frac{0.05}{11}$, $\frac{0.05}{10}$, and so on, which are 0.00417, 0.00455, 0.00500 and 0.00556 for the first four. The first three p-values pass (0.001, 0.004, 0.0048), and 0.011 fails against 0.00556. Holm stops there. That is 3 metrics, one more than Bonferroni, which missed 0.0048 by a hair.

Step 4, Benjamini-Hochberg at $q = 0.05$: the table lists each rank's cutoff $\frac{k}{12} \times 0.05$.

| Rank $k$ | $p_{(k)}$ | Holm cutoff | BH cutoff | BH adjusted p |
|---|---|---|---|---|
| 1 | 0.001 | 0.0042 | 0.0042 | 0.0120 |
| 2 | 0.004 | 0.0045 | 0.0083 | 0.0192 |
| 3 | 0.0048 | 0.0050 | 0.0125 | 0.0192 |
| 4 | 0.011 | 0.0056 | 0.0167 | 0.0330 |
| 5 | 0.019 | 0.0063 | 0.0208 | 0.0456 |
| 6 | 0.027 | 0.0071 | 0.0250 | 0.0540 |
| 7 | 0.034 | 0.0083 | 0.0292 | 0.0583 |
| 8 | 0.042 | 0.0100 | 0.0333 | 0.0630 |
| 9 | 0.11 | 0.0125 | 0.0375 | 0.1467 |
| 10 | 0.31 | 0.0167 | 0.0417 | 0.3720 |
| 11 | 0.58 | 0.0250 | 0.0458 | 0.6327 |
| 12 | 0.83 | 0.0500 | 0.0500 | 0.8300 |

Rank 5 passes (0.019 is at most 0.0208), and ranks 6 to 12 all fail (0.027 is above 0.0250, 0.034 above 0.0292, and so on). The largest passing rank is $k = 5$, so BH rejects the first five metrics.

<div class="warning" markdown>

Watch out at Step 4: the adjusted p-values are not the p-values times $\frac{m}{k}$ for that rank alone. Each adjusted value is the smallest of $p_{(j)}\frac{m}{j}$ over all ranks $j$ at or after $k$. That is why ranks 2 and 3 share the adjusted value 0.0192, which comes from rank 3 ($0.0048 \times 4 = 0.0192$).

</div>

Step 5, reading the results: the procedures reject 2, 3 and 5 metrics, in the order Bonferroni, Holm, BH, and 8 with no correction. Bonferroni and Holm say that the chance of any false lead on their list is at most 5%. BH says that on average at most about 5% of the five metrics on its list are false leads. The extra three metrics that no correction would add (ranks 6 to 8) are the ones with weak evidence, and with 12 tests they are the ones most likely to be luck.

Check: the adjusted p-values agree with the cutoffs. Ranks 1 to 5 have adjusted p-values at most 0.0456, below 0.05, and rank 6 has 0.0540, above it. The code below gives the same adjusted values from SciPy.

</div>

<div class="example" markdown>

### Example 2: peeking at an A/A test

Two arms of an experiment both convert at 5%, so there is no difference to find. Each arm gets 1000 new users a day for 14 days, and a team computes the two-proportion $z$ statistic on the accumulated data after each day. They stop and declare a winner at the first day with $\lvert z \rvert > 1.96$ ($p < 0.05$). How often do they declare a winner?

Simulate 20,000 such experiments. If the team looks once, at day 14, they declare a winner in 4.9% of experiments, which is the 5% the test promises. If they look twice, at days 7 and 14, it is 8.2%. If they look every day, it is 22.3%. Almost a quarter of experiments with no difference at all end with a "winner".

![Left: z statistics of 40 simulated A/A tests over 14 days, mostly gray lines that stay between the dashed lines at plus and minus 1.96 and 6 red lines that cross one of them on some day. Right: the percentage of A/A tests declared a winner rising from 5.2 percent with one daily look to 8.6 percent with two, 14.6 percent with five and 22.3 percent with 14, above a dashed line at 5 percent](../../assets/figures/05-university-core/multiple-testing-and-p-hacking-peeking.svg)

The winners are fragile. Of the experiments that showed $p < 0.05$ on some day, 78% were not significant on day 14. A team that watched the dashboard would have seen a green number, and the next day it would have faded. A Bonferroni cutoff for 14 looks, $\lvert z \rvert > 2.91$ (from $\frac{0.05}{14} = 0.0036$ per look), keeps the overall rate at 2.1%. That is valid, and conservative, because consecutive looks share most of their data, so they are far from independent.

Check: the first look at 1000 users per arm is 5.2% in the simulation, close to 5%, and the rate climbs with each extra look, never falls. The single look at day 14 gives 4.9%, again close to 5%.

</div>

<div class="example" markdown>

### Example 3: twenty comparisons, one hit

An experiment measures 5 outcomes in each of 4 user segments, so 20 comparisons between version A and version B (hypothetical). One of them, session length on mobile, has $p = 0.03$. The other 19 have $p > 0.2$. Should the team conclude that B lengthens mobile sessions?

If every null hypothesis were true, the chance that at least one of the 20 comparisons has $p \le 0.05$ is $1 - 0.95^{20} = 64\%$. A single $p = 0.03$ among 20 is what luck alone usually produces. The Bonferroni-adjusted p-value is $\min(1, 20 \times 0.03) = 0.6$, and the BH-adjusted value is the same here. There is no evidence of an effect after correction.

That doesn't prove B does nothing for mobile sessions. It means that the finding is a hypothesis to test in a new experiment, with that one comparison named in advance. The new experiment has one test, so its p-value means what it says.

Check: the Bonferroni cutoff for 20 tests is $\frac{0.05}{20} = 0.0025$, and $0.03 > 0.0025$, which agrees with the adjusted value 0.6 being above 0.05.

</div>

<div class="example" markdown>

### Example 4: choosing the best model on the test set

A team trains 100 models and evaluates each on the same test set of 1000 labelled examples. To isolate the effect of selection, suppose that every model is a coin flip, with true accuracy 50%. The team keeps the model with the best test accuracy and reports it.

A single model with 540 of 1000 correct has $z = \frac{40}{\sqrt{250}} = 2.53$ and a one-sided p-value of 0.0062, which looks like strong evidence of skill. But the best of 100 models reaches 540 by luck with probability $1 - (1 - 0.0062)^{100} = 46\%$. In a simulation of 2000 such experiments the best model had an average test accuracy of 54.0%, although every model's true accuracy was 50%. On a fresh test set, the selected models averaged 50.0% again.

The reported accuracy is optimistic by a predictable amount that grows with the number of models tried. This is the multiple-testing problem in machine-learning clothes: the family is every model you scored on the test set. The usual fix is to choose among models on a validation set (or by cross-validation) and to touch the test set once, at the end, for the single chosen model. Every extra use of the test set adds to the family.

Check: Bonferroni would multiply the single-model p-value by 100, giving $0.62$ and no evidence of skill, which agrees with the truth that all 100 models guess.

</div>

<div class="example" markdown>

### Example 5: Benjamini-Hochberg with a surprise (finish it yourself)

Six sorted p-values from a screen are 0.003, 0.012, 0.021, 0.034, 0.041 and 0.30. Apply BH at $q = 0.05$, and compare with Bonferroni and Holm.

The BH cutoffs $\frac{k}{6} \times 0.05$ are 0.0083, 0.0167, 0.0250, 0.0333, 0.0417 and 0.0500. Compare each p-value with its cutoff, decide which ranks are rejected, and then do the same with Bonferroni and Holm.

<details class="solution" markdown>
<summary>Finish</summary>

Ranks 1, 2 and 3 pass (0.003 ≤ 0.0083, 0.012 ≤ 0.0167, 0.021 ≤ 0.0250). Rank 4 fails, since 0.034 > 0.0333. Rank 5 passes, since 0.041 ≤ 0.0417, and rank 6 fails. The largest passing rank is 5, so BH rejects ranks 1 to 5, including rank 4, which missed its own cutoff. Stopping at the first failure would have given only 3.

Bonferroni's cutoff is $\frac{0.05}{6} = 0.0083$, so it rejects only 0.003. Holm's cutoffs are 0.0083, 0.0100, 0.0125 and so on: it rejects 0.003 and stops at 0.012 > 0.0100, so it also rejects 1. The three procedures reject 1, 1 and 5.

Check: the BH-adjusted p-values are 0.018, 0.036, 0.042, 0.0492, 0.0492 and 0.30. The first five are at most 0.05 and the last is not, so five rejections, as found.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: counting only the tests you reported. A paper that shows one p-value from a data set where the author tried 12 analyses has a family of 12 (the forks above), not 1. The number that matters is the number you could have run and might have reported if it had come out well. If you decided the one analysis before seeing the data, the family is 1.

</div>

<div class="warning" markdown>

Watch out: stopping at the first failure in Benjamini-Hochberg. That rule belongs to Holm (a step-down method). BH is a step-up method: find the largest rank that passes its cutoff and reject everything up to it, even ranks that failed their own cutoffs. Example 5 shows 5 rejections where the "first failure" rule gives 3.

</div>

<div class="warning" markdown>

Watch out: reading FDR as a promise about each discovery. "FDR 5%" means that on average, over many experiments, about 5% of the items on the list are false. In one experiment the list could hold no false leads or several, and no single item has a "5% chance of being false" by this guarantee. An item's own adjusted p-value is a rule for the list, not a probability for the item.

</div>

<div class="warning" markdown>

Watch out: "just looking" is not free. Looking at a running test and stopping when it looks good, or when it looks hopeless, changes the false-positive rate, as Example 2 shows. Early stopping is fine when the rule was planned, with cutoffs built for repeated looks. What breaks the guarantee is deciding afterwards, from the result, that this was the moment to stop.

</div>

<div class="warning" markdown>

Watch out: choosing the family after the result. If the dashboard has 50 metrics and you then say "we only ever cared about the three that lit up", the family is 50, not 3. Name the primary metric, the secondary metrics and the guardrail metrics before the test, and correct for the family you named.

</div>

Corrections cost power, and that is the price of honesty about how many chances you had, not a reason to skip them. A correct but weak test, as in Example 1 for Bonferroni, can be made stronger with more data, with fewer and better-chosen hypotheses, or with FDR control when false leads are cheap. Also, a correction fixes the error rate of a test, not a flawed design. A significant result in an observational study is still confounded, as in [descriptive statistics and study design](01-descriptive-statistics-and-study-design.md#judge-a-study), however many tests you adjusted for.

## Tricks and shortcuts

The expected number of false positives among $m$ true nulls is $m\alpha$, and this needs no independence, because expectations add. For 50 metrics at 5%, that is 2.5.

The $z$ cutoffs for a 5% family-wise error rate are about 2.8 for 10 tests, 3.0 for 20, 3.3 for 50 and 3.5 for 100. If a result needs fewer standard errors than that and you ran that many tests, be careful with it.

Look at the histogram of all the p-values. If everything is null it is flat, as in the figure of [hypothesis testing](03-hypothesis-testing.md), and if there are real effects the histogram piles up near 0. A pile near 0 plus a flat floor is the picture that FDR methods are built for.

To get BH-adjusted p-values by hand: sort, compute $p_{(k)}\frac{m}{k}$, then work from the largest rank down, replacing each value by the smaller of itself and the one after it, and cap at 1. Reject when the adjusted value is at most $q$. SciPy does this in `scipy.stats.false_discovery_control`.

Plan the test so that fewer corrections are needed: one primary metric at the full $\alpha$, a short list of secondary metrics, and guardrails that only need to be non-inferior. Fix the sample size and the analysis in advance, and write them down.

## In code

The code below runs the formulas and simulations of this lesson. It writes the three procedures from scratch (so you can see how short they are) and checks BH against SciPy, then simulates the A/A test with daily looks, the best of 100 coin-flip models, and the forking paths of 10 analyses on pure noise. Install SciPy once with `pip install scipy`.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np
from scipy import stats            # pip install scipy

# 1. The chance of at least one false positive among m independent tests with every null true.
for m in (1, 5, 20, 50, 100):
    print(m, round(1 - 0.95**m, 3))
# 1 0.05
# 5 0.226
# 20 0.642
# 50 0.923
# 100 0.994

# 2. Bonferroni, Holm and Benjamini-Hochberg on the 12 metrics of Example 1.
p = np.array([0.001, 0.004, 0.0048, 0.011, 0.019, 0.027, 0.034, 0.042, 0.11, 0.31, 0.58, 0.83])

def bonferroni(p, alpha):
    return p <= alpha / len(p)

def holm(p, alpha):
    m, reject = len(p), np.zeros(len(p), bool)
    for rank, i in enumerate(np.argsort(p)):           # rank 0 is the smallest p-value
        if p[i] > alpha / (m - rank):                  # the first failure stops the procedure
            break
        reject[i] = True
    return reject

def benjamini_hochberg(p, alpha):
    m, order = len(p), np.argsort(p)
    passed = p[order] <= alpha * np.arange(1, m + 1) / m
    k = passed.nonzero()[0].max() + 1 if passed.any() else 0     # the LARGEST rank that passes
    reject = np.zeros(m, bool)
    reject[order[:k]] = True
    return reject

print((p < 0.05).sum(), bonferroni(p, 0.05).sum(), holm(p, 0.05).sum(), benjamini_hochberg(p, 0.05).sum())
# 8 2 3 5
print(np.round(stats.false_discovery_control(p), 4).tolist())     # Benjamini-Hochberg adjusted p-values
# [0.012, 0.0192, 0.0192, 0.033, 0.0456, 0.054, 0.0583, 0.063, 0.1467, 0.372, 0.6327, 0.83]

# 3. Peeking: A/A tests (both arms convert at 5%), 1000 users per arm per day, checked every day for 14 days.
rng = np.random.default_rng(11)
reps, days, per_day = 20_000, 14, 1000
xa = rng.binomial(per_day, 0.05, (reps, days)).cumsum(axis=1)     # cumulative sign-ups, arm A
xb = rng.binomial(per_day, 0.05, (reps, days)).cumsum(axis=1)
n = per_day * np.arange(1, days + 1)                              # users per arm after each day
pool = (xa + xb) / (2 * n)
z = (xb / n - xa / n) / np.sqrt(pool * (1 - pool) * 2 / n)
sig = np.abs(z) > 1.96
print(sig[:, -1].mean(), sig[:, [6, 13]].any(axis=1).mean(), sig.any(axis=1).mean())
# 0.0493 0.0824 0.22285
print(round((sig.any(axis=1) & ~sig[:, -1]).sum() / sig.any(axis=1).sum(), 3))
# 0.779
bonf = np.abs(z) > stats.norm.isf(0.05 / (2 * days))             # a Bonferroni cutoff for 14 looks, |z| > 2.91
print(round(stats.norm.isf(0.05 / (2 * days)), 2), bonf.any(axis=1).mean())
# 2.91 0.02145

# 4. Choosing the best of 100 models on a test set of 1000 labels, when every model is a coin flip.
rng = np.random.default_rng(5)
acc = rng.binomial(1000, 0.5, (2000, 100)) / 1000                 # 2000 experiments, 100 models each
best = acc.argmax(axis=1)                                         # the model you would pick on this test set
fresh = rng.binomial(1000, 0.5, (2000, 100)) / 1000               # the same models on a new test set
print(round(acc[:, 0].mean(), 3), round(acc.max(axis=1).mean(), 3), round(fresh[np.arange(2000), best].mean(), 3))
# 0.5 0.54 0.5
tail = stats.binom.sf(539, 1000, 0.5)                             # P(one coin-flip model scores 540 or more)
print(round(tail, 4), round(1 - (1 - tail) ** 100, 3))
# 0.0062 0.464

# 5. Forking paths: 2 outcomes, each tested on everyone and on 4 segments, with no real effect anywhere.
z_seg = rng.standard_normal((reps, 2, 4))                         # z statistic in each segment
z_all = z_seg.sum(axis=2, keepdims=True) / 2                      # everyone: the four segments together
tests = np.concatenate([z_all, z_seg], axis=2)                    # 2 x 5 = 10 analyses
print((np.abs(tests) > 1.96).any(axis=(1, 2)).mean(), round(1 - 0.95**10, 3))
# 0.3631 0.401
```

The simulated rates match the lesson: 4.9% for one look at day 14, 8.2% for two, 22.3% for daily looks, and 2.1% for the Bonferroni cutoff 2.91. The best of 100 coin-flip models scores 54.0% on the test set and 50.0% on a fresh one. Ten analyses of pure noise give at least one $p < 0.05$ in 36% of experiments, a little below the 40.1% that independent tests would give, because the "everyone" test shares its data with the segment tests.

</details>

## FAQ

### I only report one test. Do I still need to correct?

It depends on how you chose it. If you decided on that one test before you saw any data, the family is 1 and there is nothing to correct. If you looked at several results and picked the one to report, the family is everything you looked at, whether or not you show it. A reader can't tell the two cases apart from the paper, which is why preregistration exists.

### Should I use Bonferroni, Holm or Benjamini-Hochberg?

Use Holm over plain Bonferroni, since it has the same guarantee and rejects at least as much. Choose between Holm and BH by the cost of a false lead. If a single false finding is costly, as with a medical claim or a one-way product decision, control the family-wise error rate. If you are screening many candidates for follow-up, such as features, genes or metrics, and a few false leads are cheap, control the false discovery rate.

### Would a stricter cutoff like 0.005 fix this?

It lowers the rate for a single test, and it doesn't touch the cause, which is the number of chances. With a stricter cutoff you can still run 50 metrics, or 14 looks, or 12 analyses, and the chance of a fluke still multiplies. The correction methods work because they tie the cutoff to the number of chances. The cutoff 0.005 is right for 10 tests and wrong for 100.

### Isn't exploring the data the whole point?

Yes, and exploring is fine. The problem is reporting an exploratory finding with a p-value that was computed as if it were planned. Explore freely, label what you found as exploratory, and confirm it with a new experiment or a held-out part of the data, where there is one planned test and its p-value means what it says.

## Practice

### Warm-up

1\. Eight independent tests are run at the 5% level, and every null hypothesis is true. Find (a) the probability of at least one false positive, (b) the Bonferroni cutoff for each test, and (c) the expected number of false positives.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $1 - 0.95^8 = 0.3366$, about 34%. (b) $\frac{0.05}{8} = 0.00625$. (c) $8 \times 0.05 = 0.4$.

Check: with Bonferroni's cutoff, the chance of at least one false positive among the 8 independent tests is $1 - (1 - 0.00625)^8 = 0.0489$, just under 0.05.

</details>

2\. Apply the Bonferroni correction at the 5% level to the four p-values 0.004, 0.011, 0.020 and 0.200. Which are rejected, and what are the adjusted p-values?

<details class="solution" markdown>
<summary>Solution</summary>

The cutoff is $\frac{0.05}{4} = 0.0125$. The p-values 0.004 and 0.011 are below it, so they are rejected, and 0.020 and 0.200 are not. The adjusted p-values are $4p$ capped at 1: $0.016$, $0.044$, $0.08$ and $0.8$.

Check: the adjusted values for the two rejected tests are below 0.05 and the others are above it, which agrees with the cutoff rule.

</details>

3\. Say whether each situation needs a multiple-testing correction, and name the family. (a) A team preregisters one primary metric and tests it once. (b) An experiment tracks 30 metrics, and the team will ship if any one of them improves. (c) A researcher tries five outlier-removal rules and reports the one that gives the smallest p-value.

<details class="solution" markdown>
<summary>Solution</summary>

(a) No. There is one test, so the family has size 1. (b) Yes. Any one metric improving triggers the decision, so the family is all 30 metrics. (c) Yes. The reported test was chosen from five, so the family is at least 5, even though only one p-value is shown.

Check: in (b) and (c) the chance of a spurious "win" is well above 5% without a correction, up to $1 - 0.95^{30} = 78\%$ and $1 - 0.95^5 = 23\%$ for independent tests.

</details>

### Standard

4\. Six sorted p-values are 0.0008, 0.009, 0.013, 0.018, 0.046 and 0.21. Find how many are rejected at the 5% level by Bonferroni, by Holm and by Benjamini-Hochberg with $q = 0.05$.

<details class="solution" markdown>
<summary>Solution</summary>

Bonferroni's cutoff is $\frac{0.05}{6} = 0.00833$, so only 0.0008 is rejected: 1.

Holm's cutoffs are $0.00833, 0.0100, 0.0125, 0.0167, 0.0250$ and $0.0500$. The first two p-values pass (0.0008, 0.009). The third, 0.013, is above 0.0125, so Holm stops: 2.

BH's cutoffs are $0.00833, 0.0167, 0.0250, 0.0333, 0.0417$ and $0.0500$. The first four pass (0.013 ≤ 0.0250, 0.018 ≤ 0.0333). The fifth, 0.046, is above 0.0417, and the sixth fails too. The largest passing rank is 4: 4 rejections.

Check: the counts 1, 2 and 4 rise in the order Bonferroni, Holm, BH, as they must. The BH-adjusted p-values are 0.0048, 0.026, 0.026, 0.027, 0.0552 and 0.21, and four of them are at most 0.05.

</details>

5\. A dashboard compares two identical versions on 50 independent metrics at the 5% level. (a) Find the expected number of significant metrics. (b) Find the probability that 5 or more are significant. (c) What cutoff would Bonferroni use per metric, and what is then the probability that at least one metric is significant?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $50 \times 0.05 = 2.5$. (b) The number of significant metrics is binomial with $n = 50$ and $p = 0.05$, and $P(X \ge 5) = 1 - P(X \le 4) = 0.1036$, about 10%. So five green metrics on a dashboard is not strong evidence of a real difference. (c) The cutoff is $\frac{0.05}{50} = 0.001$, and the chance of at least one significant metric is $1 - 0.999^{50} = 0.0488$.

Check: the expected count 2.5 is the mean of the binomial, $np$, and $P(X \ge 1) = 1 - 0.95^{50} = 0.923$ matches the lesson's 92%.

</details>

6\. A team tries 200 models, each a coin flip with true accuracy 50%, on the same test set of 1000 labels. A single model reaches 540 or more correct with probability 0.0062. Find the expected number of the 200 models that reach 540 or more, and the probability that at least one does. What should the team do instead?

<details class="solution" markdown>
<summary>Solution</summary>

The expected number is $200 \times 0.0062 = 1.24$, and the probability of at least one is $1 - (1 - 0.0062)^{200} = 0.713$ (the exact binomial tail is 0.006222, which gives the same figures). So the "best model" of 200 beats 54% on the test set about 71% of the time, with no skill at all.

Choose among the models on a validation set, or with cross-validation, and use the test set once, for the single model chosen. Or, if the test set must be reused, correct for the number of models tried, as Bonferroni would.

Check: with 100 models the same formula gives 46.4%, the figure in Example 4, and it rises with the number of models.

</details>

### Challenge

7\. (a) Prove that Bonferroni controls the FWER at $\alpha$ when $m_0$ of the $m$ nulls are true, and say how the bound changes when $m_0 < m$. (b) For independent tests, show that the exact FWER of Bonferroni, $1 - \left(1 - \frac{\alpha}{m}\right)^m$, is at most $\alpha$, and evaluate it for $m = 5$, 20 and 100 at $\alpha = 0.05$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) This is Theorem 1: the union bound over the $m_0$ true nulls gives $m_0 \cdot \frac{\alpha}{m}$, which is at most $\alpha$. When $m_0 < m$, the bound $\frac{m_0}{m}\alpha$ is smaller than $\alpha$, so Bonferroni is more conservative the more of the hypotheses are false.

(b) Bernoulli's inequality says $(1 - x)^m \ge 1 - mx$ for $0 \le x \le 1$. With $x = \frac{\alpha}{m}$ we get $\left(1 - \frac{\alpha}{m}\right)^m \ge 1 - \alpha$, so $1 - \left(1 - \frac{\alpha}{m}\right)^m \le \alpha$. For $\alpha = 0.05$ the values are $0.0490$ for $m = 5$, $0.0488$ for $m = 20$ and $0.0488$ for $m = 100$.

Check: the values fall towards $1 - e^{-0.05} = 0.0488$ as $m$ grows, always below 0.05.

</details>

8\. (Reviews [hypothesis testing](03-hypothesis-testing.md#what-a-p-value-is-not).) A lab tests 200 hypotheses, of which 20 are true effects. Each test has power 0.5 and uses $\alpha = 0.05$. (a) How many true effects are found, and how many false positives appear? (b) What share of the significant results are false? (c) What does BH at $q = 0.05$ try to guarantee instead?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The true effects found number $20 \times 0.5 = 10$. The false positives number $180 \times 0.05 = 9$, since 180 hypotheses are true nulls. (b) There are $10 + 9 = 19$ significant results and 9 are false, so $\frac{9}{19} = 47\%$. Nearly half the "discoveries" are false, though every one has $p \le 0.05$.

(c) BH aims to keep the expected share of false discoveries among the rejections at or below $q = 5\%$. With the plain 5% rule, the false share depends on how many hypotheses are true and on the power, and here it is 47%. BH ties its cutoffs to the p-values themselves and would reject fewer of the weak results.

Check: this is the same arithmetic as the 36% in the "What a p-value is not" section of hypothesis testing, with a lower power and a smaller share of true effects.

</details>

## Where this shows up

- In CS, the A/B-testing platforms that you will meet at work run dozens of metrics per experiment and have many people checking results, so guardrail metrics, a single primary metric and sequential tests are standard. In machine learning, every look at the test set, every hyperparameter search scored on it and every leaderboard submission adds to the family of Example 4, which is why train, validation and test sets are kept apart. The regression of [correlation and linear regression](04-correlation-and-linear-regression.md) has the same problem when you add and drop predictors until the coefficients look significant.
- In economics, researchers try many specifications (which controls, which sample, which outcome), and the debate about replication in the field is largely about forking paths ([regression and econometrics intuition](../../07-economics-math/04-more-tools/03-regression-and-econometrics-intuition.md)). In finance, a backtest that tries many strategies on one price history and reports the best is Example 4 again ([investing returns and risk](../../08-financial-math/06-investing-and-retirement/01-investing-returns-and-risk.md)).
- The false discovery rate is the standard tool in fields that test thousands of hypotheses at once, such as genetics, where Benjamini and Hochberg's procedure is used to select genes for follow-up.
