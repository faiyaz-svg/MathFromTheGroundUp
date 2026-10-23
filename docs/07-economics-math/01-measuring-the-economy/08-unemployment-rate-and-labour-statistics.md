# Unemployment rate and labour statistics

After this lesson you can classify a person as employed, unemployed or not in the labour force by the Labour Force Survey rules, compute the unemployment, participation and employment rates and show how they are related, explain how the unemployment rate can fall for a bad reason, and use a simple flows model of unemployment.

Before this: [percent change vs percentage points](02-percent-change-vs-percentage-points.md), [how economists use math and graphs](01-how-economists-use-math-and-graphs.md) (stocks and flows) and [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A survey population aged 15 and over is 10,000 people, of whom 6,000 are employed and 400 are unemployed. Find the labour force, the unemployment rate, the participation rate and the employment rate.
2. A person without a job wants one but stopped searching because they believe none is available. Are they unemployed, by the survey's rules?
3. If an unemployed person gives up searching and leaves the labour force, what happens to the unemployment rate?

<details class="solution" markdown>
<summary>Answers</summary>

1. The labour force is $6000 + 400 = 6400$. The unemployment rate is $\frac{400}{6400} = 6.25\%$, the participation rate is $\frac{6400}{10000} = 64\%$ and the employment rate is $\frac{6000}{10000} = 60\%$.
2. No. They are not searching, so they are classified as not in the labour force (a discouraged searcher).
3. It falls, because the unemployed count falls and so does the labour force, and the number of employed doesn't change.

</details>

## The idea

Every month, Statistics Canada asks a sample of households a fixed set of questions about last week: did you work, did you look for work, could you have started a job? From the answers it sorts everyone aged 15 and over into three groups, employed, unemployed and not in the labour force, and reports the sizes of the groups and a few ratios. These statistics, from the Labour Force Survey (LFS), are the main monthly measure of the Canadian job market.

The headline number is the unemployment rate, and it is easy to misread. In September 2026 it was 6.5% for Canada and 7.0% for Ontario (Statistics Canada, Table 14-10-0287-01, seasonally adjusted). A year earlier the figures were 7.1% and 7.9%. That looks like good news, and in Ontario it mostly is. In Canada, the fall comes with a drop in the share of people in the labour force. Telling the two apart needs the algebra relating the rates, which this lesson develops.

## Definitions

The **population** $N$ here is the survey population: people aged 15 and over, excluding people living on reserves, full-time members of the regular Armed Forces and people living in institutions such as hospitals and prisons (Statistics Canada, [Guide to the Labour Force Survey, 2025](https://www150.statcan.gc.ca/n1/pub/71-543-g/71-543-g2025001-eng.htm)). Each person is in exactly one of three groups.

A person is **employed** ($E$) if, during the reference week, they did any work at all at a job or business (paid work or self-employment), or had a job but were absent from it (illness, vacation, family reasons and so on). A person is **unemployed** ($U$) if, during the reference week, they were without work, were available for work, and either had looked for work in the past four weeks, or were on temporary layoff with an expected recall, or had a job to start within four weeks. A person is **not in the labour force** ($M$ for "marginally attached or out") if they are neither employed nor unemployed, such as students not looking for work, retirees and people caring for family. The same reference gives these definitions.

The **labour force** $L$ is the number of people who are employed or unemployed:

$$
L = E + U.
$$

In plain words, the labour force is everyone who has a job or is available and looking for one. The population then splits as $N = L + M = E + U + M$.

The three rates are:

$$
u = \frac{U}{L}, \qquad p = \frac{L}{N}, \qquad e = \frac{E}{N}.
$$

The **unemployment rate** $u$ is the share of the labour force that is unemployed. The **participation rate** $p$ is the share of the population that is in the labour force. The **employment rate** $e$ (also called the employment-to-population ratio) is the share of the population that is employed. In plain words, $u$ is "of those who want work, how many don't have it", $p$ is "how many want work", and $e$ is "how many have it". Note that $u$ has a different denominator from the other two: $u$ divides by the labour force, and $p$ and $e$ divide by the population.

A **discouraged searcher** is a person who wanted work and was available, but didn't look because they believed no suitable work was available. By the LFS rules a discouraged searcher is not in the labour force, so they are not counted as unemployed.

A **flow** between labour market states is the number of people who move from one state to another in a period, for example from unemployed to employed in a month. The numbers $E$, $U$ and $M$ are stocks; the flows change them, as in [the first lesson](01-how-economists-use-math-and-graphs.md#stocks-and-flows).

## How to do it

### Computing the three rates

1. Find $E$, $U$ and the population $N$ (aged 15 and over) in the same units and the same month.
2. Compute the labour force $L = E + U$.
3. Compute $u = \frac{U}{L}$, with the labour force on the bottom.
4. Compute $p = \frac{L}{N}$ and $e = \frac{E}{N}$, with the population on the bottom.
5. Check the identity from the next section: $e = p(1 - u)$.
6. Convert to percents and round at the end. Statistics Canada publishes the rates to one decimal place, and the levels in thousands of people.

### How the rates are related

*Theorem.* For $L > 0$ and $N > 0$, $e = p\,(1 - u)$ and equivalently $u = 1 - \frac{e}{p}$.

What we know: $L = E + U$, $u = \frac{U}{L}$, $p = \frac{L}{N}$ and $e = \frac{E}{N}$. What we want: $e$ in terms of $p$ and $u$. The plan is to write $E$ as the part of the labour force that is not unemployed.

Proof. Since $L = E + U$, we have $E = L - U = L(1 - u)$, because $U = uL$. Divide by $N$:

$$
e = \frac{E}{N} = \frac{L}{N}(1 - u) = p(1 - u).
$$

Solving for $u$ gives $1 - u = \frac{e}{p}$, so $u = 1 - \frac{e}{p}$, valid when $p > 0$. $\blacksquare$

Looking back: the employment rate is the participation rate times the share of the labour force that is employed, $1 - u$. So the unemployment rate can fall for two very different reasons. Either the employment rate $e$ rises, which is good news, or the participation rate $p$ falls with $e$ unchanged, so that fewer people are counted as looking. The formula $u = 1 - \frac{e}{p}$ makes both visible at once.

### Changes in counts

When the survey is compared across two dates, the counts satisfy $\Delta U = \Delta L - \Delta E$, since $U = L - E$. A fall in the number of unemployed is the growth of the labour force minus the growth of employment, with the sign reversed. If employment grows by 95 thousand and the labour force shrinks by 26 thousand, unemployment falls by $95 + 26 = 121$ thousand. About three quarters of that comes from more jobs and about a quarter from fewer people in the labour force.

To see what would have happened under different participation, hold participation fixed. If the participation rate had stayed at $p_0$, the labour force this year would have been $p_0 N_1$, where $N_1$ is this year's population, and with the actual number of employed, the unemployment rate would be $\frac{p_0 N_1 - E_1}{p_0 N_1}$. Example 2 does this with real data.

### Why the unemployment rate can fall for bad reasons

The unemployment rate counts only people who are searching, so it can fall without anyone finding work:

- People leave the labour force. Discouraged workers stop searching, people retire early, and people return to school. The labour force shrinks, and $u$ falls.
- The population is aging. A larger share of retirees lowers the participation rate, and with it the employment rate, even when the people who want work find it.
- Employment can rise at the same time as the participation rate falls, and then $u$ falls twice over.

The unemployment rate can also rise for good reasons, for example when a strong job market draws people into the labour force who were not searching before, and some of them have not yet found work. That is why economists read the unemployment rate together with the participation rate and the employment rate.

### Flows between states

The three groups are connected by monthly flows. In a simple two-state model, each month a fraction $s$ of employed workers lose their jobs (the separation rate) and a fraction $f$ of unemployed workers find one (the job-finding rate), with the labour force fixed. Let $E$ and $U$ be the stocks.

*Theorem.* If $E$ and $U$ are constant over time (a steady state) with $E + U = L$, then the unemployment rate is

$$
u^* = \frac{s}{s + f}.
$$

What we know: each month $sE$ people move from employed to unemployed and $fU$ move from unemployed to employed. What we want: the steady-state ratio $\frac{U}{L}$. The plan is to set the two flows equal, because the stocks don't change, and substitute $E = L - U$.

Proof. In a steady state $sE = fU$. Substituting $E = L - U$ gives $s(L - U) = fU$, so $sL = (s + f)U$, and dividing by $(s + f)L$ gives $\frac{U}{L} = \frac{s}{s + f}$. $\blacksquare$

Looking back: the unemployment rate in the model depends only on the ratio of the separation rate to the sum of the two rates. A fall in the job-finding rate $f$ raises $u^*$, and so does a rise in the separation rate $s$. The model leaves out the flow in and out of the labour force, and real flows are large, but it gives the right picture of why unemployment is a balance of inflows and outflows.

## Worked examples

<div class="example" markdown>

### Example 1: the rates from the counts, Canada, September 2026

Statistics Canada reports for September 2026 (Table 14-10-0287-01, seasonally adjusted, thousands of persons aged 15 and over): population 34,854.9, employment 21,104.8 and unemployment 1,474.9. Find $L$, $u$, $p$ and $e$.

Step 1: the three counts are in the same units (thousands) and the same month.

Step 2: $L = 21{,}104.8 + 1{,}474.9 = 22{,}579.7$, which agrees with the published labour force.

Step 3: $u = \frac{1{,}474.9}{22{,}579.7} = 0.06532$, so 6.5%.

Step 4: $p = \frac{22{,}579.7}{34{,}854.9} = 0.64782$, so 64.8%, and $e = \frac{21{,}104.8}{34{,}854.9} = 0.60550$, so 60.6%.

Step 5: check the identity: $p(1 - u) = 0.64782 \times 0.93468 = 0.60550$, which equals $e$. The numbers not in the labour force are $34{,}854.9 - 22{,}579.7 = 12{,}275.2$ thousand, about 35.2% of the population.

The published rates are 6.5%, 64.8% and 60.6%, which agree with these.

Watch out at Step 3: the unemployment rate divides by the labour force. Dividing by the population gives $\frac{1{,}474.9}{34{,}854.9} = 4.2\%$, which is not the unemployment rate.

</div>

<div class="example" markdown>

### Example 2: did the unemployment rate fall for a good reason?

The LFS (Table 14-10-0287-01, seasonally adjusted, September of each year, thousands) gives for Canada: in 2025, $N = 34{,}671.9$, $L = 22{,}606.0$, $E = 21{,}009.9$, $U = 1{,}596.1$, and in 2026 the values in Example 1. The published unemployment rates are 7.1% and 6.5%. What drove the fall?

Step 1: unrounded rates: $u_{2025} = \frac{1{,}596.1}{22{,}606.0} = 7.06\%$ and $u_{2026} = 6.53\%$, a fall of 0.53 points (the published, rounded figures differ by 0.6). Participation fell from $\frac{22{,}606.0}{34{,}671.9} = 65.20\%$ to 64.78%. The employment rate went from 60.60% to 60.55%.

Step 2: the changes in counts are $\Delta E = 21{,}104.8 - 21{,}009.9 = +94.9$, $\Delta L = 22{,}579.7 - 22{,}606.0 = -26.3$ and $\Delta U = -121.2$, which equals $\Delta L - \Delta E = -26.3 - 94.9$.

Step 3: employment grew, but the population grew faster (by 183.0 thousand, or 0.53%), so the employment rate was flat. The unemployed count fell by 121.2 thousand, of which 94.9 (78%) is explained by employment growth and 26.3 (22%) by the shrinking labour force.

Step 4: counterfactual. If the participation rate had stayed at 65.20%, the labour force would have been $0.6520 \times 34{,}854.9 = 22{,}725$ thousand. With the same employment of 21,104.8 thousand, unemployment would have been $22{,}725 - 21{,}104.8 = 1{,}620$ thousand, a rate of $\frac{1{,}620}{22{,}725} = 7.13\%$.

So the whole fall in the unemployment rate lines up with the drop in participation. With participation constant, the rate would have been about 7.1%, the same as a year earlier. The survey does not say why participation fell (an aging population, fewer immigrants entering the labour force, discouragement), so this is a statement about the arithmetic and not about the cause.

Check: $e = p(1 - u)$ in both years: $0.6520 \times 0.9294 = 0.6060$ and $0.6478 \times 0.9347 = 0.6055$.

</div>

<div class="example" markdown>

### Example 3: Ontario, a fall driven by employment

Ontario, September 2025 and September 2026 (Table 14-10-0287-01, seasonally adjusted, thousands): 2025 has $N = 13{,}732.8$, $L = 8{,}903.0$, $E = 8{,}200.2$ and $U = 702.9$. In 2026, $N = 13{,}798.4$, $L = 8{,}910.6$, $E = 8{,}286.5$ and $U = 624.1$. The published unemployment rates are 7.9% and 7.0%.

Unrounded, $u_{2025} = \frac{702.9}{8{,}903.0} = 7.90\%$ and $u_{2026} = \frac{624.1}{8{,}910.6} = 7.00\%$, a fall of 0.89 points, or 11.3% relative to the old rate. The count of unemployed fell by 78.8 thousand while employment rose by 86.3 thousand and the labour force rose by 7.6 thousand. Employment growth is more than all of the fall in $U$ (the labour force even grew slightly).

Participation fell a little, from 64.83% to 64.58%. Holding it at 64.83% would give a labour force of 8,946 thousand and an unemployment rate of $\frac{8{,}946 - 8{,}286.5}{8{,}946} = 7.37\%$, so a fall from 7.90% would remain even then. In Ontario, the fall in the unemployment rate has more of a "more people at work" explanation than in Canada as a whole, although the employment rate rose by only 0.34 points, from 59.71% to 60.05%.

Check: $\Delta L - \Delta E = 7.6 - 86.3 = -78.7$, against the reported $\Delta U = -78.8$. The 0.1 gap is rounding in the published levels (2025's $E + U = 8{,}903.1$ against $L = 8{,}903.0$).

</div>

<div class="example" markdown>

### Example 4: a steady-state rate from flows

These flow rates are made up. Each month 1.5% of employed workers lose their jobs, and 25% of unemployed workers find one. What is the steady-state unemployment rate, and what happens if the job-finding rate falls to 15%?

Step 1: $s = 0.015$ and $f = 0.25$.

Step 2: $u^* = \frac{0.015}{0.015 + 0.25} = \frac{0.015}{0.265} = 0.0566$, so 5.7%.

Step 3: with $f = 0.15$, $u^* = \frac{0.015}{0.165} = 0.0909$, so 9.1%.

Check: with 100 people in the labour force at $u^* = 5.66$, 5.66 are unemployed and 94.34 employed. Flows are $0.015 \times 94.34 = 1.415$ into unemployment and $0.25 \times 5.66 = 1.415$ out, equal as they should be in a steady state.

</div>

<div class="example" markdown>

### Example 5: a discouraged worker (finish it yourself)

These numbers are made up. A town has 1,000 people aged 15 and over: 600 employed, 60 unemployed and 340 not in the labour force. Find $u$, $p$ and $e$. Then 20 of the unemployed give up searching and leave the labour force, with no change in employment. Find the new rates.

Before: $L = 660$, $u = \frac{60}{660} = 9.09\%$, $p = 66\%$ and $e = 60\%$.

Now compute the rates after the 20 people leave, and say which rates changed.

<details class="solution" markdown>
<summary>Finish</summary>

After: $U = 40$, $L = 640$, so $u = \frac{40}{640} = 6.25\%$, $p = \frac{640}{1000} = 64\%$ and $e = \frac{600}{1000} = 60\%$ (unchanged, since nobody found a job).

The unemployment rate fell by 2.84 points, and the participation rate fell by 2 points, and the employment rate didn't move. Nobody got a job, and the unemployment rate still fell by almost a third.

Check: $e = p(1 - u) = 0.64 \times 0.9375 = 0.60$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the unemployment rate divides by the labour force, not the population. In Example 1, 1,474.9 divided by the population gives 4.2%, while the unemployment rate is 6.5%.

</div>

<div class="warning" markdown>

Watch out: "not working" is not "unemployed". A retiree, a full-time student not looking for work and a discouraged searcher are not in the labour force, so they are in none of the unemployment figures. Only people who are available and searching (or on temporary layoff, or about to start a job) are unemployed.

</div>

<div class="warning" markdown>

Watch out: a falling unemployment rate is not the same as more people working. Check the employment rate and the participation rate. In Example 2, the unemployment rate fell, and the employment rate stayed flat.

</div>

<div class="warning" markdown>

Watch out: changes in the rates are in percentage points. A rate going from 7.1% to 6.5% fell 0.6 percentage points (a relative fall of 8.5%), as in [percent change vs percentage points](02-percent-change-vs-percentage-points.md).

</div>

Seasonally adjusted figures are used for month-to-month comparisons, because employment has a regular yearly pattern (summer jobs, holiday hiring). The LFS levels are estimates from a sample, so each figure has a margin of error, and small changes (a few tenths of a point, or a few tens of thousands of people) are often not statistically distinguishable from no change. Statistics Canada's releases say so in their wording, for example "little changed".

Part-time work counts as employment, so a person who works one hour a week is employed. That is one reason economists look at other measures such as the share working part-time involuntarily, and at the employment rate. A person who works at a job and is also looking for another is employed, not unemployed.

The unemployment rate is not a measure of hardship. It leaves out the employed with low pay and too few hours, and it leaves out discouraged people. Broader measures exist, but they are different statistics with their own definitions.

## Tricks and shortcuts

Use $u = 1 - \frac{e}{p}$ to check a report. If the employment rate is 60.6% and the participation rate is 64.8%, then $u = 1 - \frac{60.6}{64.8} = 6.5\%$, which matches the published rate. A quick estimate of the unemployment rate is the gap between the participation and employment rates divided by the participation rate: $\frac{64.8 - 60.6}{64.8}$.

To see whether a fall in $u$ is "real", compare the change in the employment rate with the change in participation. A falling $u$ with flat $e$ and a falling $p$ is the pattern of Example 2.

For a steady-state check from flows, the unemployment rate is the separation rate over the sum of the two: with $s$ small compared with $f$, $u^* \approx \frac{s}{f}$ (for $s = 1.5\%$ and $f = 25\%$, that is 6%, against the exact 5.7%).

When you have counts, subtract: $\Delta U = \Delta L - \Delta E$. The fall in the number of unemployed is employment growth minus labour force growth.

## In code

The code computes the rates for Canada in September 2026, checks $e = p(1 - u)$, decomposes the change in the number of unemployed, and finds the steady-state rate.

<details class="code" markdown>
<summary>In code</summary>

```python
# Thousands of persons aged 15 and over, Canada, seasonally adjusted (Table 14-10-0287-01)
n26, e26, u26 = 34_854.9, 21_104.8, 1_474.9
n25, e25, u25 = 34_671.9, 21_009.9, 1_596.1

def rates(n, e, u):
    labour_force = e + u
    return u / labour_force, labour_force / n, e / n

ur, pr, er = rates(n26, e26, u26)
print(round(ur * 100, 2), round(pr * 100, 2), round(er * 100, 2))  # 6.53 64.78 60.55
print(abs(er - pr * (1 - ur)) < 1e-12)                             # True

# Why did the unemployed count fall? dU = dL - dE
dE = e26 - e25
dL = (e26 + u26) - (e25 + u25)
print(round(dE, 1), round(dL, 1), round(u26 - u25, 1))  # 94.9 -26.3 -121.2

# Unemployment rate if participation had stayed at its 2025 level
p25 = (e25 + u25) / n25
labour_force_cf = p25 * n26
print(round((labour_force_cf - e26) / labour_force_cf * 100, 2))  # 7.13

# Steady-state unemployment from flow rates
def steady_state(s, f):
    return s / (s + f)

print(round(steady_state(0.015, 0.25) * 100, 2))  # 5.66
```

</details>

## FAQ

### Why aren't discouraged workers counted as unemployed?

The survey definition requires that a person looked for work (or be on temporary layoff or have a job to start). The definition follows international standards and keeps the measure checkable: searching is something a respondent can report. Discouraged searchers are counted in a separate category, and broader measures of labour underutilization include them.

### What is a "normal" unemployment rate?

There is no single number. Some unemployment is always present because people change jobs and new workers enter. The flows model shows that even with a low separation rate, $u^*$ is positive. What counts as normal depends on the economy and changes over time.

### Why does Statistics Canada survey households and not count unemployment insurance claims?

Not everyone who is unemployed receives or claims benefits, and some people claim who are not searching. A survey with fixed definitions applies the same test to everyone. The cost is sampling error, because only a sample of households is asked.

### Does a falling participation rate mean the economy is weak?

Not necessarily. An aging population lowers it as more people retire, even in a strong economy. A drop that happens in people of prime working age (25 to 54) points more to weak demand or discouragement. The survey reports participation by age group.

## Practice

### Warm-up

1\. A survey population of 20,000 people aged 15 and over has 12,000 employed and 900 unemployed. Find $L$, $u$, $p$ and $e$.

<details class="solution" markdown>
<summary>Solution</summary>

$L = 12{,}000 + 900 = 12{,}900$. $u = \frac{900}{12900} = 6.98\%$. $p = \frac{12900}{20000} = 64.5\%$. $e = \frac{12000}{20000} = 60\%$.

Check: $e = p(1 - u) = 0.645 \times 0.9302 = 0.60$.

</details>

2\. Classify each person as employed, unemployed or not in the labour force: (a) a student who worked 5 hours last week at a café, (b) someone laid off 3 months ago who has applied to 10 jobs this month, (c) a retiree who isn't looking for work, (d) someone on vacation from their job, (e) someone who wants a job but stopped searching 6 months ago because there are none.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Employed (any work at all counts). (b) Unemployed (without work, available, looked in the past four weeks). (c) Not in the labour force. (d) Employed (has a job and is absent). (e) Not in the labour force (a discouraged searcher).

Check: none of the five is in two groups, since each person falls in exactly one of the three.

</details>

3\. The participation rate is 65% and the unemployment rate is 6%. Find the employment rate.

<details class="solution" markdown>
<summary>Solution</summary>

$e = p(1 - u) = 0.65 \times 0.94 = 0.611$, so 61.1%.

Check: $u = 1 - \frac{0.611}{0.65} = 6\%$.

</details>

### Standard

4\. Ontario in September 2026 (Table 14-10-0287-01, thousands, seasonally adjusted): population 13,798.4, labour force 8,910.6 and employment 8,286.5. Find the number unemployed and the three rates.

<details class="solution" markdown>
<summary>Solution</summary>

$U = L - E = 8{,}910.6 - 8{,}286.5 = 624.1$. Then $u = \frac{624.1}{8{,}910.6} = 7.0\%$, $p = \frac{8{,}910.6}{13{,}798.4} = 64.6\%$ and $e = \frac{8{,}286.5}{13{,}798.4} = 60.1\%$.

Check: $0.6458 \times (1 - 0.0700) = 0.6005$, which is $e$. These agree with the published 7.0%, 64.6% and 60.1%.

</details>

5\. A town has 1,000 people aged 15 and over, with 600 employed and 60 unemployed. Then 30 of the unemployed stop searching. Find $u$, $p$ and $e$ before and after.

<details class="solution" markdown>
<summary>Solution</summary>

Before: $L = 660$, $u = 9.09\%$, $p = 66\%$, $e = 60\%$. After: $U = 30$, $L = 630$, $u = \frac{30}{630} = 4.76\%$, $p = 63\%$, $e = 60\%$.

The unemployment rate halves, and the employment rate stays at 60%.

Check: $0.63 \times (1 - 0.0476) = 0.60$.

</details>

6\. In the flows model, the separation rate is 2% a month and the job-finding rate is 30%. Find the steady-state unemployment rate. What if the job-finding rate falls to 20%?

<details class="solution" markdown>
<summary>Solution</summary>

$u^* = \frac{0.02}{0.02 + 0.30} = 6.25\%$. With $f = 0.20$, $u^* = \frac{0.02}{0.22} = 9.09\%$.

Check: at 6.25%, with 100 workers, 6.25 unemployed and 93.75 employed give flows $0.02 \times 93.75 = 1.875$ and $0.30 \times 6.25 = 1.875$.

</details>

### Challenge

7\. Canada, September 2025 and September 2026 (thousands, seasonally adjusted): population 34,671.9 then 34,854.9; employment 21,009.9 then 21,104.8; labour force 22,606.0 then 22,579.7. (a) Find the change in the unemployment rate in points (unrounded). (b) Find what it would have been in 2026 with the 2025 participation rate. (c) What part of the change is accounted for by participation?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $u_{2025} = \frac{22{,}606.0 - 21{,}009.9}{22{,}606.0} = 7.06\%$ and $u_{2026} = \frac{22{,}579.7 - 21{,}104.8}{22{,}579.7} = 6.53\%$, so $-0.53$ points.

(b) $p_{2025} = \frac{22{,}606.0}{34{,}671.9} = 65.20\%$, so the 2026 labour force would be $0.6520 \times 34{,}854.9 = 22{,}725$ and $u = \frac{22{,}725 - 21{,}104.8}{22{,}725} = 7.13\%$.

(c) With participation held fixed, the rate would have been 7.13%, which is 0.07 points above the 2025 rate of 7.06%. So the whole fall, and a little more, is accounted for by the lower participation: $7.13 - 6.53 = 0.60$ points of the rate is the effect of participation falling from 65.20% to 64.78%.

Check: with $p$ held fixed, $e = 0.6520 \times (1 - 0.0713) = 0.6055$, equal to the actual 2026 employment rate, which shows why the counterfactual is consistent.

</details>

8\. (Reviews [percent change vs percentage points](02-percent-change-vs-percentage-points.md).) Ontario's unemployment rate was 7.9% in September 2025 and 7.0% in September 2026. Give the change in percentage points and in basis points, and the relative change.

<details class="solution" markdown>
<summary>Solution</summary>

The change is $7.0 - 7.9 = -0.9$ percentage points, or $-90$ basis points. The relative change is $\frac{-0.9}{7.9} = -0.114$, a fall of 11.4% in the rate (11.3% with the unrounded rates of Example 3).

Check: $7.9 \times (1 - 0.114) = 7.0$.

</details>

## Where this shows up

- This lesson ends the chapter on measuring the economy. The next chapter starts with opportunity cost and the PPC<!-- link: ../02-markets/01-opportunity-cost-and-the-ppc.md -->, and [regression and econometrics intuition](../04-more-tools/03-regression-and-econometrics-intuition.md) uses labour statistics as examples of data where causes are hard to separate.
- In macroeconomics, the unemployment rate and the inflation rate (from [CPI and inflation](07-cpi-and-inflation.md)) are the two numbers most often watched together, in the Phillips curve and in central bank decisions.
- In data work, the lesson of Example 2 is general: a rate has a numerator and a denominator, and the rate can change because either part changed. The first step with any ratio statistic is to ask what moved.
