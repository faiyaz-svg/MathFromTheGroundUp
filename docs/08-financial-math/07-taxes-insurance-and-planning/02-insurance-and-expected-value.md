# Insurance and expected value

After this lesson you can compute the expected loss and the loading of an insurance policy, explain with concave utility why a risk-averse person can rationally pay more than the expected loss, compare deductibles by expected cost, test an extended warranty, and size a term life policy as the present value of the income it replaces.

Before this: [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md) and [annuities and geometric series](../03-time-value-of-money/02-annuities-and-geometric-series.md).

All probabilities, prices and premiums in this lesson are made up for practice. They are not quotes from any insurer, and the lesson explains the math. It does not tell you what to buy.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A policy covers a \$5,000 loss that happens with probability 0.02 a year. The premium is \$140. What is the expected loss, and by what percent does the premium exceed it?
2. A policy with a \$500 deductible pays the loss above \$500. The loss is \$0 with probability 0.9 and \$2,000 with probability 0.1. What is the expected payout?
3. An extended warranty costs \$90. With probability 0.1 the item fails and the warranty pays a \$400 repair. What is the expected net gain from buying it?

<details class="solution" markdown>
<summary>Answers</summary>

1. The expected loss is $0.02 \times 5000 = 100$, that is, \$100. The premium exceeds it by $\frac{140 - 100}{100} = 40\%$.
2. The payout is \$0 with probability 0.9 and $2000 - 500 = 1500$ with probability 0.1, so the expected payout is $0.1 \times 1500 = 150$, that is, \$150.
3. The expected payout is $0.1 \times 400 = 40$ dollars and the price is \$90, so the expected net gain is $40 - 90 = -50$, a loss of \$50.

</details>

## The idea

You own a phone worth \$900. In any year there is a small chance, say 8%, that you lose or break it. You will not know in advance whether this is your year. An insurance company offers to replace the phone for a premium of \$110 a year. If it insures thousands of people like you, it can predict how many phones will be lost in a year quite accurately even though it cannot predict which ones, and it can set the premium above what it expects to pay out.

So for the average buyer insurance has a negative expected value: they pay \$110 and expect \$72 back. The question for this lesson is why anyone buys it. Part of the answer is that the premium also pays the insurer's costs and profit, and the expected value is not the whole story. A loss that is rare but would wreck your finances is worse than its average suggests, because the first dollars of your wealth matter more to you than the last ones. A \$900 phone is a small loss for most people, so insurance on it is a poor deal. A \$400,000 house fire is a loss no one can absorb, so insurance on it can be worth paying more than the expected loss for.

Expected value from the probability lesson is the tool. Then a second tool, concave utility, explains the gap between "negative expected value" and "worth buying".

## Definitions

A **loss** is a random variable $L \ge 0$: the dollar amount you lose in a year (it is 0 in a year when nothing happens). The **expected loss** is $E[L]$. A **premium** is the price $P$ of the insurance. In plain words, the premium is what you pay for sure, and the expected loss is what you would lose on average with no insurance.

A policy is **actuarially fair** when the premium equals the expected payout. The **loading** of a policy with premium $P$ and expected payout $E$ is

$$
\lambda = \frac{P - E}{E},
$$

the percent by which the premium exceeds the expected payout. The **loss ratio** is $\frac{E}{P}$, the share of premium dollars that come back as claims on average. For example, a premium of \$110 and an expected payout of \$72 give a loading of $\frac{110 - 72}{72} = 52.8\%$ and a loss ratio of 65.5%.

A **deductible** $D$ is the part of each loss that you pay yourself. A policy with a deductible pays $\max(L - D, 0)$.

A **utility function** $u(w)$ gives the value to you of having wealth $w$. A person is **risk averse** when $u$ is strictly concave: each extra dollar adds less value than the one before. Concave is the same word as in [concavity and curve sketching](../../05-university-core/03-applications-of-derivatives/04-concavity-and-curve-sketching.md): the graph bends downward, and a chord between two points lies below the graph. In symbols, for $0 < q < 1$ and $a \ne b$,

$$
u\bigl(q\,a + (1-q)\,b\bigr) > q\,u(a) + (1-q)\,u(b).
$$

The **certainty equivalent** of a risky wealth $W$ is the sure amount $c$ with $u(c) = E[u(W)]$. The **risk premium** is $E[W] - c$. In plain words, the certainty equivalent is the guaranteed wealth that feels exactly as good as the gamble, and the risk premium is how much average wealth the person gives up to avoid the risk. The logarithm $u(w) = \ln w$ is a standard example of a concave utility ([logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md)), and economics uses it throughout ([utility and indifference curves](../../07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md)).

## How to do it

### Why insurers make money on average

*Theorem 1 (the insurer's average profit).* An insurer sells $n$ independent policies, each with premium $P$ and a payout $X_i$ with mean $E$ and standard deviation $s$. The total profit before costs is $nP - \sum X_i$. Its mean is $n(P - E)$ and its standard deviation is $s\sqrt{n}$, so the profit per policy has mean $P - E$ and standard deviation $\frac{s}{\sqrt{n}}$.

We know the rules for the mean and variance of a sum of independent random variables ([discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md)). We want the mean and spread of the insurer's profit. The plan is to use linearity for the mean and the fact that independent variances add.

*Proof.* By linearity of expectation, $E\bigl[nP - \sum X_i\bigr] = nP - nE = n(P - E)$. The variables are independent, so the variances add: $\operatorname{Var}\bigl(\sum X_i\bigr) = n s^2$, and the standard deviation of the total is $s\sqrt{n}$. Subtracting from a constant doesn't change the standard deviation. Dividing both by $n$ gives the profit per policy: mean $P - E$, standard deviation $\frac{s\sqrt{n}}{n} = \frac{s}{\sqrt{n}}$. $\blacksquare$

Look back: the mean grows like $n$, but the standard deviation grows only like $\sqrt{n}$, so the relative risk falls as the portfolio grows. This is the law of large numbers at work ([law of large numbers and CLT](../../05-university-core/07-probability/06-law-of-large-numbers-and-clt.md)). One person faces the full risk of one policy, and an insurer faces a small relative risk. The assumption of independence matters: a flood or a pandemic hits many policies at once, and then the $\sqrt{n}$ argument fails.

### Why a risk-averse person can still buy it

*Theorem 2 (a fair premium is always preferred).* Let $u$ be strictly concave and let wealth be $W - L$, where $W$ is the starting wealth and $L$ is a non-constant random loss. Then $E[u(W - L)] < u(W - E[L])$. So a risk-averse person strictly prefers full insurance at the actuarially fair premium $E[L]$ to no insurance. By continuity of $u$, they would also pay a little more than $E[L]$.

We know that $u$ is concave, so $u$ lies above its chords. We want a comparison of the expected utility of a gamble with the utility of its mean. The plan is to prove it for a loss with two values, which is the case this lesson uses, from the definition of concavity.

*Proof.* Suppose the loss is $\ell_1$ with probability $q$ and $\ell_2$ with probability $1 - q$, where $\ell_1 \ne \ell_2$ and $0 < q < 1$. Put $a = W - \ell_1$ and $b = W - \ell_2$. Then $a \ne b$, and $W - E[L] = q a + (1-q) b$. The definition of strict concavity says $u(q a + (1-q)b) > q\,u(a) + (1-q)\,u(b)$. The left side is $u(W - E[L])$ and the right side is $E[u(W - L)]$. $\blacksquare$

Look back: nothing in the proof used the log function, only the bend of the graph. The opposite holds for a convex utility, and people with a linear utility ($u(w) = w$) are indifferent at a fair premium and refuse any positive loading. Real people buy insurance for big losses and rarely for small ones, which fits the picture: the curve is steepest, and bends most, where wealth is low.

### The steps

1. Write down the loss distribution: each possible loss and its probability. Say where the numbers come from (here they are made up).
2. Compute the expected payout of the policy, with the deductible and any limit applied.
3. Compare it with the premium: loading $= \frac{P - E}{E}$. A positive loading is the normal case.
4. Ask whether you could afford the worst loss out of pocket. If yes, a large loading is hard to justify. If no, compute a utility comparison, or at least the size of the loss against your savings.
5. For a deductible, compare expected total cost $=$ premium $+$ expected amount you pay yourself, and compare the worst year too.
6. For life insurance, find the income to be replaced and its present value (an annuity), then subtract assets and add debts.
7. Check every probability sums to 1 and every expected value lies between the smallest and largest payout.

## Worked examples

<div class="example" markdown>

### Example 1: phone insurance and the insurer's side

A phone is worth \$900 and is lost or broken with probability 0.08 in a year (made up). The insurer charges \$110.

Step 1: the loss is \$900 with probability 0.08 and \$0 with probability 0.92.

Step 2: the policy pays the full loss, so the expected payout is $E = 0.08 \times 900 = 72$ dollars.

Step 3: the loading is $\frac{110 - 72}{72} = 0.5278$, which is 52.8%, and the loss ratio is $72 \div 110 = 65.5\%$. For you the expected value of the policy is $72 - 110 = -38$ dollars a year.

Step 4: could you afford a \$900 loss? For many people yes, so the loading of 52.8% is what you pay for convenience.

Now the insurer's side. One policy's payout has standard deviation $s = 900\sqrt{0.08 \times 0.92} = 244.16$. With $n = 10{,}000$ independent policies, Theorem 1 gives an expected profit of $10000 \times 38 = 380{,}000$ dollars before costs, and a standard deviation of $244.16 \times \sqrt{10000} = 24{,}416$ dollars. The premiums total \$1,100,000 and the expected claims are \$720,000, which is $\frac{380000}{24416} = 15.6$ standard deviations below the premium total. Claims above the premiums are not a realistic risk. A simulation in the code below agrees: over 200 simulated years the largest claim total was \$782,100.

Check: the expected claims $10000 \times 72 = 720{,}000$ match $10000 \times 0.08 \times 900$. The \$380,000 is before the insurer's costs such as staff, advertising and claims handling, which is where part of the 52.8% loading goes.

</div>

<div class="example" markdown>

### Example 2: why insure a big loss (log utility)

Your wealth is \$60,000. With probability 0.05 you suffer a \$20,000 loss (made up). Use $u(w) = \ln w$.

Without insurance the expected loss is $0.05 \times 20000 = 1000$ dollars. The expected utility is

$$
E[u] = 0.95 \ln 60000 + 0.05 \ln 40000 = 10.98183.
$$

The certainty equivalent is $c = e^{10.98183} = 58{,}795.85$. So the risky situation feels as good as a sure wealth of \$58,795.85, which is \$1,204.15 below the starting \$60,000. That is the most you would pay for full insurance: a premium of $P$ leaves sure wealth $60000 - P$, and $\ln(60000 - P) \ge 10.98183$ exactly when $P \le 1204.15$.

The expected loss is only \$1,000, so you would pay up to \$204.15 above it, a loading of up to $\frac{1204.15 - 1000}{1000} = 20.4\%$. Theorem 2 guarantees this number is positive. A premium of \$1,200 would be worth buying and one of \$1,300 would not. Check: $\ln(60000 - 1200) = 10.98190$, which is just above $10.98183$, and $\ln(60000 - 1300) = 10.98020$, which is below.

Wealth matters. Someone with \$200,000 facing the same gamble would pay at most \$1,050.83, a loading of only 5.1%, because the loss is smaller relative to what they have. This is why people with more savings tend to insure less.

</div>

<div class="example" markdown>

### Example 3: choosing a deductible

A car's yearly collision loss is made up as follows: \$0 with probability 0.90, \$500 with probability 0.05, \$2,000 with probability 0.03 and \$8,000 with probability 0.02. The insurer charges 1.4 times the expected payout (a loading of 40%).

With deductible $D$, the policy pays $\max(L - D, 0)$ and you pay $\min(L, D)$. For $D = 1000$ the expected payout is $0.03 \times 1000 + 0.02 \times 7000 = 170$, the premium is $1.4 \times 170 = 238$, and you expect to pay $0.05 \times 500 + 0.03 \times 1000 + 0.02 \times 1000 = 75$ yourself. The other rows are computed the same way:

| Deductible | Expected payout | Premium | Expected own cost | Expected total | Premium plus deductible |
|---|---|---|---|---|---|
| \$0 | \$245 | \$343 | \$0 | \$343 | \$343 |
| \$500 | \$195 | \$273 | \$50 | \$323 | \$773 |
| \$1,000 | \$170 | \$238 | \$75 | \$313 | \$1,238 |
| \$2,000 | \$120 | \$168 | \$125 | \$293 | \$2,168 |

On average the higher deductible is cheaper: the expected total falls from \$343 to \$293. The last column is the cost of a year with a big loss, since the loss is at least the deductible: it climbs from \$343 to \$2,168. So the trade-off is a lower expected cost against a bigger bill in a bad year. The expected total is always $E[L] + 0.4 \times$ (expected payout) $= 245 + 0.4 \times 120 = 293$ for $D = 2000$, because every dollar of payout carries the 40% loading (Practice 7 proves this).

Check: the expected loss is $0.05 \times 500 + 0.03 \times 2000 + 0.02 \times 8000 = 245$, matching the $D = 0$ row, and payout plus own cost is 245 in every row ($195 + 50$, $170 + 75$, $120 + 125$).

</div>

<div class="example" markdown>

### Example 4: an extended warranty

A laptop costs \$1,200. An extended warranty costs \$180 for three years. Suppose (made up) the chance of a covered failure in that time is 10%, and the repair is worth \$600.

The expected payout is $0.10 \times 600 = 60$ dollars. The expected net gain is $60 - 180 = -120$, so the warranty returns on average 33 cents per dollar paid and has a loading of $\frac{180 - 60}{60} = 200\%$. To break even the failure probability would have to be $\frac{180}{600} = 30\%$. Unless you think this laptop is three times as likely to fail as the made-up 10%, or a \$600 repair would be a real hardship, the warranty has a large negative expected value.

Check: $0.30 \times 600 = 180$. Compared with the phone policy (loading 52.8%), the warranty's 200% loading is far higher, which is what the numbers show: the seller keeps most of what you pay.

</div>

<div class="example" markdown>

### Example 5: how much term life insurance (finish it yourself)

Suppose (made up) a family would need \$50,000 a year for 15 years if the earner died, with the money received at the end of each year. Use a real rate of 3%, meaning a rate after inflation ([inflation and real returns](../02-interest-and-growth/06-inflation-and-real-returns.md)). They have \$40,000 of savings and \$25,000 of debts that would have to be paid off. How large should the policy be?

Step 1: the income need is an ordinary annuity of \$50,000 for 15 years at 3%.

Step 2: its present value is

$$
PV = 50000 \cdot \frac{1 - 1.03^{-15}}{0.03}.
$$

Now compute it, add the debts, subtract the savings, and check the result.

<details class="solution" markdown>
<summary>Finish</summary>

Step 2 continued: $1.03^{-15} = 0.64186$, so $\frac{1 - 0.64186}{0.03} = 11.9379$ and $PV = 50000 \times 11.9379 = 596{,}896.75$ dollars.

Step 3: the policy should cover the income need plus the debts, minus the savings: $596896.75 + 25000 - 40000 = 581896.75$, so a policy of about \$580,000. The exact figure depends on the made-up rate, the length and the amounts, so round it and treat it as an estimate.

Check: run the money forward. Starting from \$596,896.75, grow the balance by 3% and then pay out \$50,000, fifteen times. The balance ends at \$0 (to the cent). The code at the end of the lesson also adds the 15 discounted payments and gets the same \$596,896.75.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: "negative expected value" does not mean "never buy". Expected value treats every dollar the same. A loss that would force you to sell your home hurts more than its probability-weighted average, and Example 2 shows that a risk-averse person would rationally pay a loading of 20% for it. The same logic fails for small losses: a \$900 phone is not a loss that changes your life, so paying 52.8% extra for it is expensive.

</div>

<div class="warning" markdown>

Watch out: do not compare premiums alone when deductibles differ. A \$273 premium with a \$500 deductible and a \$343 premium with no deductible are different products. Compare expected total cost, premium plus what you expect to pay yourself, and also the bill in a bad year, as in Example 3.

</div>

<div class="warning" markdown>

Watch out: the probabilities in an insurance example are not facts about you. They are estimates for a group. If you know you are riskier than the group (adverse selection), insurance looks better to you than to the insurer, and if you take more risks because you are insured (moral hazard), the insurer's numbers are wrong. Both effects are why real premiums are not simple averages.

</div>

Insurance can also fail the independence assumption. A disaster that hits many policies at the same time makes the insurer's total claims vary far more than the $\sqrt{n}$ rule says, which is why insurers use reinsurance and why some risks are hard to insure.

Two edge cases for the formulas: if the expected payout is 0 the loading is undefined (a policy that never pays has an infinite loading), and a deductible larger than every possible loss makes the payout 0 for all of them.

## Tricks and shortcuts

For any policy, loss ratio and loading are two views of one number: loading $= \frac{1}{\text{loss ratio}} - 1$. A loss ratio of 65.5% means a loading of $\frac{1}{0.655} - 1 = 52.7\%$.

For a deductible with loading $\lambda$ on the expected payout, the expected total cost is $E[L] + \lambda\,E[\text{payout}]$. You only need the expected payout under each deductible, not the expected own cost.

For a warranty, divide the price by the repair cost. That gives the break-even probability of a failure: \$180 over \$600 is 30%. If you think the true chance is well below it, skip the warranty.

To estimate a term life need, multiply the yearly income to be replaced by a factor from the annuity formula. At a real rate of 3% the factor is about 12 for 15 years and about 14.9 for 20 years.

## In code

The code computes the loading, simulates an insurer's portfolio (with a fixed seed), solves the log-utility example, tabulates the deductibles and discounts the term life need.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import random

# 1. expected loss and loading (made-up phone insurance)
p, loss, premium = 0.08, 900, 110
expected_loss = p * loss
print(expected_loss, round(premium / expected_loss - 1, 4))     # 72.0 0.5278

# 2. an insurer with 10,000 such policies, simulated for 200 years
random.seed(1)
n_policies = 10_000
totals = []
for year in range(200):
    claims = sum(random.random() < p for _ in range(n_policies))
    totals.append(claims * loss)
print(max(totals) < n_policies * premium, max(totals), n_policies * premium)
print(round(sum(totals) / len(totals) / n_policies, 2))        # average payout per policy

# 3. log utility: the most you would pay to remove a 5% chance of a $20,000 loss
W, L, q = 60_000, 20_000, 0.05
expected_utility = (1 - q) * math.log(W) + q * math.log(W - L)
certainty_equivalent = math.exp(expected_utility)
print(round(W - certainty_equivalent, 2))                      # 1204.15 (expected loss is only 1000)

# 4. deductibles: premium is 1.4 times the expected payout
dist = [(0, 0.90), (500, 0.05), (2000, 0.03), (8000, 0.02)]
for d in (0, 500, 1000, 2000):
    payout = sum(pr * max(x - d, 0) for x, pr in dist)
    own = sum(pr * min(x, d) for x, pr in dist)
    print(d, round(payout, 2), round(1.4 * payout, 2), round(1.4 * payout + own, 2))

# 5. term life: present value of 15 years of $50,000 at a real rate of 3%
pv = sum(50_000 / 1.03 ** t for t in range(1, 16))
print(round(pv, 2))                                            # 596896.75
```

The output is `72.0 0.5278`, then `True 782100 1100000` and `71.99`, then `1204.15`, then the four deductible rows `0 245.0 343.0 343.0`, `500 195.0 273.0 323.0`, `1000 170.0 238.0 313.0` and `2000 120.0 168.0 293.0`, then `596896.75`. The simulated average payout of \$71.99 per policy is close to the exact \$72 (it is a simulation, so it varies with the seed). The loop over policies is slow on purpose, to show the idea; `numpy` would draw all claims at once.

</details>

## FAQ

### If insurance has a negative expected value, why is it legal and common?

The negative expected value is the price of moving risk to a company that can spread it over many people. You give up a small sure amount to avoid a small chance of a large loss, and Theorem 2 shows that a risk-averse person values that trade. The loading pays for the insurer's costs, its profit and the capital it must hold to pay claims in a bad year.

### Why use $\ln w$ for utility?

It is a convenient concave function with a useful property: a loss of 10% of your wealth costs the same utility whatever your wealth is. Other concave functions give the same type of result, with different numbers. The conclusion that a risk-averse person pays more than the expected loss uses only concavity, and the log is chosen to get numbers.

### Does a high deductible mean I should always take it?

Not always. The expected cost falls as the deductible rises, as in Example 3, because each dollar you take on yourself no longer carries the loading. But the bill in a bad year rises. The right deductible is the highest one whose worst case you can pay from savings without trouble. This is the same "could I afford the loss" test from the steps.

### How is the term life amount different from the premium comparison?

For a phone or a warranty you compare the premium with the expected payout. For life insurance for dependants the main question is the size of the need: how much money replaces the income. That is a present value, so it is a time-value problem and not an expected-value one. You compare premiums afterwards, between policies that cover the same need.

## Practice

### Warm-up

1\. A policy covers a \$3,000 loss that happens with probability 0.04 in a year. (a) What is the actuarially fair premium? (b) The premium is \$150. What is the loading?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The fair premium equals the expected payout: $0.04 \times 3000 = 120$, so \$120.

(b) The loading is $\frac{150 - 120}{120} = 0.25$, that is, 25%.

Check: $120 \times 1.25 = 150$.

</details>

2\. A policy with a \$1,000 deductible pays the loss above \$1,000. The yearly loss is \$0 with probability 0.80, \$1,500 with probability 0.15 and \$6,000 with probability 0.05. Find the expected payout, and the premium if the loading is 30%.

<details class="solution" markdown>
<summary>Solution</summary>

The payout is $1500 - 1000 = 500$ in the second case and $6000 - 1000 = 5000$ in the third. The expected payout is $0.15 \times 500 + 0.05 \times 5000 = 75 + 250 = 325$, so \$325. With a loading of 30% the premium is $1.3 \times 325 = 422.50$, that is, \$422.50.

Check: the probabilities add up, $0.80 + 0.15 + 0.05 = 1$, and the expected payout is between 0 and the largest payout, \$5,000.

</details>

3\. An extended warranty costs \$120. The item fails with probability 0.15 within the term and the repair is worth \$500. Find the expected net gain, and the failure probability at which the warranty breaks even.

<details class="solution" markdown>
<summary>Solution</summary>

The expected payout is $0.15 \times 500 = 75$, so the expected net gain is $75 - 120 = -45$, a loss of \$45. It breaks even when $p \times 500 = 120$, so $p = \frac{120}{500} = 0.24$, that is, 24%.

Check: at $p = 0.24$ the expected payout is $0.24 \times 500 = 120$, equal to the price.

</details>

### Standard

4\. An insurer sells 5,000 independent policies. Each pays \$10,000 with probability 0.02 and nothing otherwise, and the premium is \$280. Find the expected claims, the premiums collected, the expected profit before costs and the standard deviation of the total claims. How many standard deviations is the expected profit?

<details class="solution" markdown>
<summary>Solution</summary>

Expected claims: $5000 \times 0.02 \times 10000 = 1{,}000{,}000$ dollars. Premiums: $5000 \times 280 = 1{,}400{,}000$ dollars. Expected profit: $400{,}000$ dollars.

One policy's payout has variance $10000^2 \times 0.02 \times 0.98$, so for 5,000 independent policies the standard deviation of the total is $10000\sqrt{5000 \times 0.02 \times 0.98} = 10000 \times 9.8995 = 98{,}995$ dollars. The expected profit is $\frac{400000}{98995} = 4.04$ standard deviations.

Check: $5000 \times 0.02 = 100$ claims expected, and $100 \times 10000 = 1{,}000{,}000$. The profit being 4 standard deviations means a loss would need an unusually bad year, but the number is not infinite: the insurer can still lose money in a rare year.

</details>

5\. Your wealth is \$100,000 and with probability 0.10 you lose \$40,000 (made up). Using $u(w) = \ln w$, find the most you would pay for full insurance, and compare it with the expected loss.

<details class="solution" markdown>
<summary>Solution</summary>

The expected utility is $0.9\ln 100000 + 0.1\ln 60000 = 0.9 \times 11.51293 + 0.1 \times 11.00210 = 11.46185$. The certainty equivalent is $e^{11.46185} = 95{,}020.02$. The most you would pay is $100000 - 95020.02 = 4979.98$, about \$4,979.98. The expected loss is $0.10 \times 40000 = 4000$, so the risk premium is \$979.98, which is 24.5% above the expected loss.

Check: $\ln(100000 - 4979.98) = \ln 95020.02 = 11.46185$, equal to the expected utility.

</details>

6\. A family would need \$40,000 a year for 20 years, paid at the end of each year, at a real rate of 3%. They have \$30,000 of savings and no debts. How large should the policy be?

<details class="solution" markdown>
<summary>Solution</summary>

The present value of the income need is $40000 \cdot \frac{1 - 1.03^{-20}}{0.03} = 40000 \times 14.87747 = 595{,}098.99$ dollars. Subtracting the savings gives $595098.99 - 30000 = 565098.99$, so about \$565,000.

Check: 20 years of \$40,000 add to \$800,000 undiscounted, and the present value is lower, \$595,099, as discounting makes it. The ratio $\frac{595099}{40000} = 14.88$ matches the annuity factor.

</details>

### Challenge

7\. A policy has premium $(1 + \lambda)\,E[(L - D)^+]$, where $(L - D)^+ = \max(L - D, 0)$ is the payout with deductible $D$. Show that your expected total cost, premium plus expected own cost, equals $E[L] + \lambda\,E[(L - D)^+]$. Why does a higher deductible always lower the expected total cost when $\lambda > 0$? Check it against the row $D = 1000$ of Example 3.

<details class="solution" markdown>
<summary>Solution</summary>

Each loss is split between you and the insurer: $L = \min(L, D) + (L - D)^+$. Taking expectations, $E[\min(L, D)] + E[(L - D)^+] = E[L]$. Your expected total cost is the premium plus your expected own cost:

$$
(1 + \lambda)E[(L - D)^+] + E[\min(L, D)] = E[(L - D)^+] + E[\min(L, D)] + \lambda E[(L - D)^+] = E[L] + \lambda E[(L - D)^+].
$$

Raising $D$ can only lower the payout $(L - D)^+$, since $\max(L - D, 0)$ doesn't increase when $D$ increases. So $E[(L - D)^+]$ doesn't increase, and with $\lambda > 0$ the total cost doesn't increase. It goes down strictly whenever the higher deductible really cuts the expected payout.

Check with Example 3 at $D = 1000$: $E[L] = 245$, the expected payout is 170 and $\lambda = 0.4$, so the cost is $245 + 0.4 \times 170 = 313$. That matches the table.

</details>

8\. (Reviews [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md).) A game costs \$2 to play. You roll a fair die and win \$10 if it shows a 6, and nothing otherwise. Find the expected net winnings and the standard deviation of the net winnings. Is it an actuarially fair game?

<details class="solution" markdown>
<summary>Solution</summary>

The net winnings $X$ are $10 - 2 = 8$ with probability $\frac{1}{6}$ and $-2$ with probability $\frac{5}{6}$. So $E[X] = 8 \cdot \frac{1}{6} + (-2) \cdot \frac{5}{6} = \frac{8 - 10}{6} = -\frac{1}{3}$, about $-\$0.33$ per game. Next, $E[X^2] = 64 \cdot \frac{1}{6} + 4 \cdot \frac{5}{6} = \frac{84}{6} = 14$, so $\operatorname{Var}(X) = 14 - \frac{1}{9} = 13.8889$ and the standard deviation is $\sqrt{13.8889} = 3.727$.

The game is not fair, since the expected net winnings are not 0. It would be fair at a price of $\frac{10}{6} = 1.67$ dollars. At \$2 the "loading" on the expected payout of \$1.67 is $\frac{2 - 1.667}{1.667} = 20\%$.

Check: the probabilities add up, $\frac{1}{6} + \frac{5}{6} = 1$, and the expected payout is $\frac{10}{6} = 1.667$, so $1.667 - 2 = -0.333$.

</details>

## Where this shows up

- The capstone in [spreadsheet finance functions and a capstone plan](03-spreadsheet-finance-functions-and-capstone.md) uses an emergency fund as self-insurance. The previous lesson, [income tax brackets: marginal vs effective](01-income-tax-brackets-marginal-vs-effective.md), is where the "compare after tax" habit comes from.
- Economics: adverse selection, moral hazard and risk aversion are core topics in microeconomics and in [Game theory and Nash equilibrium](../../07-economics-math/04-more-tools/04-game-theory-and-nash-equilibrium.md).
- Computing: expected value drives algorithm analysis, and the same "pay a small known cost against a rare large one" trade-off appears in backups, redundancy and fault tolerance. Actuarial science is a whole field built on the loading and loss-ratio ideas here.
