# Continuous compounding and e

After this lesson you can explain why compounding more and more often approaches $A = Pe^{rt}$, prove that $\left(1 + \frac{r}{n}\right)^n \to e^r$, measure how close daily compounding gets, and convert between a continuous rate and an effective annual rate.

Before this: [compound interest](02-compound-interest.md), [APR, APY and the effective annual rate](03-apr-apy-and-effective-annual-rate.md), [logarithms](../../03-high-school/07-exponentials-and-logarithms/02-logarithms.md) and [limits: intuition and limit laws](../../05-university-core/01-limits-and-continuity/01-limits-intuition-and-limit-laws.md). The proof also uses the derivative of $\ln x$ from [the chain rule, implicit and inverse derivatives](../../05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find $1000e^{0.05 \times 10}$.
2. What is the effective annual rate of a continuous rate of 6%?
3. What continuous rate gives an effective annual rate of 5%?

<details class="solution" markdown>
<summary>Answers</summary>

1. $1000e^{0.5} = 1648.72\ldots$, so \$1,648.72.
2. $e^{0.06} - 1 = 0.061837$, that is, 6.1837%.
3. Solve $e^{\delta} = 1.05$, so $\delta = \ln 1.05 = 0.048790$, that is, 4.879%.

</details>

## The idea

The [exponential functions lesson](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md) showed a table: \$1 at 100% a year, compounded more and more often, grows to 2.00, 2.25, 2.61, 2.71 and so on, and the numbers settle near 2.71828. That was accepted from the table. This lesson explains why the same thing happens at any rate, and what it means for money.

Take \$1,000 at a nominal 5% for 10 years. Annual compounding gives \$1,628.89 and monthly gives \$1,647.01. Daily gives \$1,648.66, and compounding every hour gives \$1,648.72. Every minute gives \$1,648.72 again, to the cent. The amounts stop moving, and what they approach is $1000e^{0.5} = 1648.72$. This is continuous compounding: interest added at every instant, as the limit of adding it more and more often.

Nobody's bank account adds interest every instant. The model matters because the formula is simple, the algebra is easier than with $\left(1 + \frac{r}{n}\right)^{nt}$, and it is the form that finance theory and the calculus of growth use.

## Definitions

The number $e$, **Euler's number**, is the limit

$$
e = \lim_{n \to \infty}\left(1 + \frac{1}{n}\right)^n \approx 2.718281828\ldots
$$

In plain words, $e$ is the amount \$1 grows to in one year at 100% interest compounded continuously. It is also the base of the natural logarithm, so $\ln e = 1$.

**Continuous compounding** at the nominal annual rate $r$, also called the continuously compounded rate or the force of interest, means that the amount after $t$ years is

$$
A = Pe^{rt}.
$$

In plain words, the principal is multiplied by $e^r$ each year. Here $r$ is a rate that is meant to be used in this formula, so a "5% continuous rate" means $e^{0.05}$ per year, not $1.05$.

The **continuous rate equivalent to an effective annual rate** $r_{\text{eff}}$ is the $\delta$ with $e^{\delta} = 1 + r_{\text{eff}}$, which is

$$
\delta = \ln(1 + r_{\text{eff}}), \qquad r_{\text{eff}} = e^{\delta} - 1.
$$

In plain words, the effective annual rate is the growth factor $e^\delta$ minus 1, and the continuous rate is the natural log of the growth factor.

## How to do it

### Why the limit is $e^r$

Each period of ordinary compounding multiplies by $1 + \frac{r}{n}$. We want to know where $\left(1 + \frac{r}{n}\right)^n$ goes as $n$ grows, and the answer is the following theorem.

**Theorem.** For every real number $r$,

$$
\lim_{n \to \infty}\left(1 + \frac{r}{n}\right)^n = e^r.
$$

*Know:* $e$ is the base of $\ln$, and $\ln$ has derivative $\frac{1}{x}$, so the derivative of $\ln x$ at $x = 1$ is 1. The function $e^x$ is continuous.

*Want:* the limit of $\left(1 + \frac{r}{n}\right)^n$.

*Plan:* an exponent is hard to handle, so take a logarithm. Then $n\ln\left(1 + \frac{r}{n}\right)$ turns into a difference quotient for $\ln$ at 1, whose limit is the derivative. Then undo the logarithm with $e^x$.

*Proof.* If $r = 0$ every term is $1$ and the limit is $1 = e^0$. For $r \ne 0$, write $h = \frac{r}{n}$, which goes to 0 as $n \to \infty$. Then

$$
n\ln\left(1 + \frac{r}{n}\right) = r \cdot \frac{\ln(1 + h) - \ln 1}{h}.
$$

The fraction is the difference quotient of $\ln$ at 1, and its limit as $h \to 0$ is the derivative $\frac{d}{dx}\ln x\big|_{x=1} = \frac{1}{1} = 1$. So $n\ln\left(1 + \frac{r}{n}\right) \to r \cdot 1 = r$. Since $e^x$ is continuous, a limit can be moved inside it, so

$$
\left(1 + \frac{r}{n}\right)^n = e^{\,n\ln(1 + r/n)} \longrightarrow e^r. \quad \blacksquare
$$

*Look back:* the proof used no value of $r$ other than that it is a number, which is why one formula covers every rate. Putting $r = 1$ gives the definition of $e$ again, which is a consistency check. Replacing $n$ by $nt$ in the exponent and $r$ by $rt$ gives $\left(1 + \frac{r}{n}\right)^{nt} \to e^{rt}$ as $n \to \infty$, the formula for continuous compounding.

### How close daily compounding gets

Use the logarithm again, now with the series $\ln(1 + x) = x - \frac{x^2}{2} + \cdots$ from [power series and Taylor series](../../05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md). Then

$$
nt\ln\left(1 + \frac{r}{n}\right) = nt\left(\frac{r}{n} - \frac{r^2}{2n^2} + \cdots\right) = rt - \frac{r^2t}{2n} + \cdots
$$

so the compound amount is about $Pe^{rt}$ times $e^{-r^2t/(2n)}$, which is about $1 - \frac{r^2t}{2n}$. The relative shortfall is $\frac{r^2 t}{2n}$. It shrinks like $\frac{1}{n}$: ten times as many periods cut the gap by a factor of 10.

For \$1,000 at 5% for 10 years, the continuous amount is \$1,648.72:

| Compounded | $n$ | Amount | Shortfall | Estimate $\frac{r^2t}{2n}\cdot Pe^{rt}$ |
|---|---|---|---|---|
| annually | 1 | \$1,628.89 | \$19.83 | \$20.61 |
| semi-annually | 2 | \$1,638.62 | \$10.10 | \$10.30 |
| monthly | 12 | \$1,647.01 | \$1.71 | \$1.72 |
| weekly | 52 | \$1,648.33 | \$0.40 | \$0.40 |
| daily | 365 | \$1,648.66 | \$0.06 | \$0.06 |
| hourly | 8,760 | \$1,648.72 | \$0.00 | \$0.00 |

For daily compounding, the estimate is $\frac{0.05^2 \times 10}{2 \times 365} = 3.4 \times 10^{-5}$ of the amount, which is 6 cents. Daily compounding is so close to continuous that the two can't be told apart on a statement, which is why people say "continuous" when they mean "very frequent".

### Continuous rates and effective rates

To convert, use $\delta = \ln(1 + r_{\text{eff}})$ and $r_{\text{eff}} = e^\delta - 1$:

| Effective annual rate | Equivalent continuous rate |
|---|---|
| 3% | 2.956% |
| 5% | 4.879% |
| 8% | 7.696% |
| 10% | 9.531% |

The continuous rate is a little below the effective rate, because continuous compounding does a little more of the work. A continuous rate of 100% is an effective rate of $e - 1 = 171.8\%$.

Continuous rates have one convenient property. Growth factors multiply across periods, and logarithms turn multiplying into adding, so continuous rates add. If an investment grows by 8% in one year and 3% in the next, the total factor is $1.08 \times 1.03 = 1.1124$, and the continuous rates are $\ln 1.08 + \ln 1.03 = 0.07696 + 0.02956 = 0.10652$, which is $\ln 1.1124$. This is why finance, economics and statistics often describe returns by their logs, as in the section on log differences in [growth rates and CAGR](../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md).

### Solving with continuous compounding

The algebra is shorter. Taking the natural log of $A = Pe^{rt}$ gives $\ln\frac{A}{P} = rt$, so

$$
t = \frac{\ln(A/P)}{r}, \qquad r = \frac{\ln(A/P)}{t}, \qquad P = Ae^{-rt}.
$$

There is no $n$ to carry around, and the natural log undoes $e^{rt}$ with no extra factor.

## Worked examples

<div class="example" markdown>

### Example 1: a continuous amount

How much is \$5,000 worth after 6 years at a continuous rate of 3.2% (an example rate)?

Step 1: $P = 5000$, $r = 0.032$ and $t = 6$, so $rt = 0.192$.

Step 2: $A = 5000e^{0.192} = 5000 \times 1.211670 = 6058.35$, so \$6,058.35.

Check: the same money at 3.2% compounded annually would be $5000 \times 1.032^6 = 6040.16$ and the continuous answer is above it. For small $rt$, $e^{rt} \approx 1 + rt + \frac{(rt)^2}{2} = 1 + 0.192 + 0.0184 = 1.2104$, close to $1.2117$.

</div>

<div class="example" markdown>

### Example 2: continuous equivalent of a monthly rate

A nominal 6% compounded monthly is equivalent to what continuous rate?

The yearly growth factor is $1.005^{12} = 1.061678$. Take the natural log: $\delta = \ln 1.061678 = 12\ln 1.005 = 0.059850$. So the equivalent continuous rate is 5.985%.

Check: $e^{0.05985} = 1.061678$. The continuous rate is a little below the nominal 6%, as expected. The EAR is 6.1678%.

</div>

<div class="example" markdown>

### Example 3: how long to grow by half

How many years does it take \$2,000 to become \$3,000 at a continuous rate of 4%?

$t = \dfrac{\ln(3000/2000)}{0.04} = \dfrac{\ln 1.5}{0.04} = \dfrac{0.405465}{0.04} = 10.14$ years.

Check: $2000e^{0.04 \times 10.1366} = 2000 \times 1.5 = 3000$. Annual compounding at 4% would take $\frac{\ln 1.5}{\ln 1.04} = 10.34$ years, a little longer.

</div>

<div class="example" markdown>

### Example 4: log returns (finish it yourself)

A stock rises 10% in one year and falls 10% in the next. (a) Find the continuous (log) return of each year. (b) Add them and turn the sum into an overall change.

Step 1: the growth factors are 1.10 and 0.90.

Step 2: $\ln 1.10 = 0.09531$ and $\ln 0.90 = -0.10536$.

Finish: add them and convert back.

<details class="solution" markdown>
<summary>Finish</summary>

The sum is $0.09531 - 0.10536 = -0.01005$, and $e^{-0.01005} = 0.99$, so the stock lost 1% overall. The log returns add, and the percent changes do not: $+10\%$ and $-10\%$ do not cancel.

Check: $1.10 \times 0.90 = 0.99$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: treating $e^{r}$ as $1 + r$. A continuous rate of 5% gives \$1.0513 after one year, not \$1.05, because $e^{0.05} = 1.051271$. If a problem quotes a continuous rate, the effective rate is $e^{r} - 1$.

</div>

<div class="warning" markdown>

Watch out: mixing up a continuous rate with a nominal rate. "5% continuously compounded" and "5% compounded daily" are almost the same, \$1,648.72 against \$1,648.66 over 10 years on \$1,000, but "5% compounded annually" is not: \$1,628.89.

</div>

<div class="warning" markdown>

Watch out: using $\log$ for $\ln$. On a calculator, "log" often means base 10. The formula $t = \frac{\ln(A/P)}{r}$ needs the natural log. In Python, `math.log` is the natural log and `math.log10` is base 10.

</div>

A negative continuous rate gives decay: $e^{-rt}$ is below 1 and the balance shrinks. This is how real value falls in the [inflation lesson](06-inflation-and-real-returns.md). A zero rate gives $e^0 = 1$ and no change.

## Tricks and shortcuts

For small $x$, $e^x \approx 1 + x + \frac{x^2}{2}$. Over a short time $t$, continuous compounding is close to simple interest, $1 + rt$, with a small extra $\frac{(rt)^2}{2}$. At 5% for 2 years, $e^{0.1} = 1.10517$ against $1 + 0.1 = 1.1$ and $1 + 0.1 + 0.005 = 1.105$.

To convert quickly, a continuous rate of $\delta$ is an effective rate of about $\delta + \frac{\delta^2}{2}$. For 5%, that is $0.05 + 0.00125 = 5.125\%$, against the exact 5.127%.

## In code

The code watches $\left(1 + \frac{r}{n}\right)^{nt}$ approach $e^{rt}$, and checks the shortfall estimate.

<details class="code" markdown>
<summary>In code</summary>

```python
from math import exp, log

P, r, t = 1000, 0.05, 10
cont = P * exp(r * t)
print(round(cont, 2))                                   # 1648.72

for n in [1, 2, 12, 365, 8760]:
    a = P * (1 + r / n) ** (n * t)
    est = cont * r**2 * t / (2 * n)
    print(n, round(a, 2), round(cont - a, 2), round(est, 2))
    # 1 1628.89 19.83 20.61, then 2 1638.62 10.1 10.3, then 12 1647.01 1.71 1.72,
    # then 365 1648.66 0.06 0.06, then 8760 1648.72 0.0 0.0

print(round(100 * log(1.05), 3))                        # 4.879, continuous rate for a 5% EAR
print(round(12 * log(1.005), 5))                        # 0.05985
print(round(log(1.10) + log(0.90), 5))                  # -0.01005
```

</details>

## FAQ

### Why is there a number $e$ at all?

It is the base for which growth at rate $r$ per year is exactly $e^{rt}$, with no leftover constant. Any other base $b$ gives $b^{t} = e^{t\ln b}$, so every exponential can be written with $e$. The derivative of $e^{rt}$ is $re^{rt}$, which says that the balance grows at a rate proportional to itself, which is what continuous compounding means.

### Does any bank really compound continuously?

Most consumer accounts add interest daily or monthly, and some pay at maturity. Continuous compounding is mostly a model: it is used in finance theory, for example in option pricing and in discounting a stream of payments by a smooth curve. Because daily compounding is so close to it, the model gives answers that match real accounts to within a few cents.

### Is a bigger $n$ always better for a saver?

More frequent compounding never lowers the amount, but the gain flattens out and stops at $Pe^{rt}$. At 5% for 10 years the best any frequency can do on \$1,000 is \$1,648.72. Choosing a higher rate is worth far more than choosing a higher frequency.

## Practice

### Warm-up

1\. How much does \$2,500 become after 3 years at a continuous rate of 4%?

<details class="solution" markdown>
<summary>Solution</summary>

$A = 2500e^{0.04 \times 3} = 2500e^{0.12} = 2500 \times 1.127497 = 2818.74$, so \$2,818.74.

Check: simple interest would give $2500 \times 1.12 = 2800$, and continuous compounding gives a little more.

</details>

2\. How much must you invest now at a continuous rate of 5% to have \$5,000 in 8 years?

<details class="solution" markdown>
<summary>Solution</summary>

$P = Ae^{-rt} = 5000e^{-0.4} = 5000 \times 0.670320 = 3351.60$, so \$3,351.60.

Check: $3351.60 \times e^{0.4} = 3351.60 \times 1.491825 = 5000.00$.

</details>

3\. How long does money take to double, and to triple, at a continuous rate of 5%?

<details class="solution" markdown>
<summary>Solution</summary>

Doubling: $t = \frac{\ln 2}{0.05} = 13.86$ years. Tripling: $t = \frac{\ln 3}{0.05} = 21.97$ years.

Check: $e^{0.05 \times 13.8629} = e^{0.693147} = 2$.

</details>

### Standard

4\. A \$1,200 deposit grows to \$1,800 in 5 years under continuous compounding. What is the continuous rate, and what is the effective annual rate?

<details class="solution" markdown>
<summary>Solution</summary>

$r = \frac{\ln(1800/1200)}{5} = \frac{\ln 1.5}{5} = 0.0811$, that is, 8.11%. The effective annual rate is $e^{0.0811} - 1 = 1.5^{1/5} - 1 = 0.0845$, about 8.45%.

Check: $1200e^{0.0811 \times 5} = 1200 \times 1.5 = 1800$.

</details>

5\. Which is bigger on \$3,000 for 2 years: 4.5% compounded continuously, or 4.5% compounded monthly, and by how much?

<details class="solution" markdown>
<summary>Solution</summary>

Continuous: $3000e^{0.09} = 3282.52$. Monthly: $3000\left(1 + \frac{0.045}{12}\right)^{24} = 3281.97$. Continuous is bigger by \$0.55.

Check: the estimate of the shortfall is $\frac{r^2t}{2n} \times 3282.52 = \frac{0.045^2 \times 2}{24} \times 3282.52 = 0.55$.

</details>

6\. A nominal rate of 6% is compounded continuously. (a) What is the effective annual rate? (b) What nominal rate compounded annually is equivalent?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $e^{0.06} - 1 = 0.061837$, so 6.1837%.

(b) The equivalent annually compounded rate is the effective rate itself, 6.1837%, because annual compounding with rate $i$ has EAR $i$.

Check: $1.061837 = e^{0.06}$.

</details>

### Challenge

7\. Using the shortfall estimate $\frac{r^2t}{2n}$, how many compounding periods a year are needed to get within one cent of continuous compounding on \$1,000 at 5% for 10 years? Check with the exact formula.

<details class="solution" markdown>
<summary>Solution</summary>

The shortfall in dollars is about $1648.72 \times \frac{0.05^2 \times 10}{2n} = \frac{20.609}{n}$. We need it under 0.01, so $n > 2061$. Using hourly compounding, $n = 8760$, the exact shortfall is about \$0.0024, under a cent, and with $n = 2061$ the estimate is \$0.0100.

Check with $n = 8760$: exact amount \$1,648.7189 against \$1,648.7213, a difference of \$0.0024, and the estimate $\frac{20.609}{8760} = 0.0024$.

</details>

8\. (Reviews [exponential and logarithmic equations](../../03-high-school/07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md).) Solve $1000e^{0.05t} = 2500$ for $t$, and then compare with the answer for annual compounding at 5%.

<details class="solution" markdown>
<summary>Solution</summary>

Divide by 1000: $e^{0.05t} = 2.5$. Take the natural log: $0.05t = \ln 2.5 = 0.916291$, so $t = 18.33$ years. For annual compounding, $1.05^t = 2.5$ gives $t = \frac{\ln 2.5}{\ln 1.05} = \frac{0.916291}{0.048790} = 18.78$ years, about 0.45 years longer.

Check: $1000e^{0.05 \times 18.3258} = 2500$ and $1000 \times 1.05^{18.78} = 2500$.

</details>

## Where this shows up

- The [next lesson](05-doubling-time-rule-of-72-and-logs.md) uses logarithms for doubling times, and continuous compounding makes the exact rule simple: doubling takes $\frac{\ln 2}{r} = \frac{69.3}{R}$ years. The same $e^{rt}$ is the discount factor in [present value and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md).
- Computing and science: $e^{kt}$ models anything whose growth is proportional to its size, from populations to radioactive decay to a queue of work.
- Finance: continuous rates add across time, which makes log returns the standard way to describe a series of returns.
