# Exponential and logarithmic equations

After this lesson you can solve equations with the unknown in an exponent by taking logarithms, solve logarithmic equations and throw out extraneous solutions by checking the domain, and answer "how long until..." questions about compound interest, doubling, half-life, population and inflation.

Before this: [exponential functions and growth](01-exponential-functions-and-growth.md), [logarithms](02-logarithms.md) and [logarithm properties](03-logarithm-properties.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $3 \cdot 2^x = 45$. Give the exact answer and a decimal.
2. Solve $\log_2 x + \log_2(x - 2) = 3$.
3. By the rule of 72, about how many years does money take to double at 6% a year?

<details class="solution" markdown>
<summary>Answers</summary>

1. Divide by 3: $2^x = 15$. So $x = \log_2 15 = \frac{\ln 15}{\ln 2} \approx 3.907$.
2. Condense to $\log_2\left(x(x - 2)\right) = 3$, so $x(x - 2) = 8$ and $x^2 - 2x - 8 = 0$, which gives $x = 4$ or $x = -2$. The logarithms need $x > 2$, so only $x = 4$ works.
3. $\frac{72}{6} = 12$ years.

</details>

## The idea

You have \$5,000 in an account that pays 4% a year. How long until it is \$10,000? The balance after $t$ years is $5000 \cdot 1.04^t$, so you want the $t$ with $5000 \cdot 1.04^t = 10000$, which is $1.04^t = 2$. Try a few years: $1.04^{17} = 1.948$ and $1.04^{18} = 2.026$, so the answer is between 17 and 18 years. Guessing narrows it down, but it can't give the exact number, because the unknown is in the exponent and ordinary algebra can't reach it.

A logarithm can. Taking the logarithm undoes the exponent: $t = \log_{1.04} 2 = \frac{\ln 2}{\ln 1.04} = 17.67$ years. This lesson makes that into a method. The pattern is the same for every equation here: get the exponential part alone, take a logarithm of both sides, and use the power rule to bring the unknown down to where you can solve for it. For logarithmic equations the move runs the other way, and you turn the logarithm back into a power. The one new danger is that a logarithm only accepts positive inputs, so you must check your answers against the domain.

## Definitions

An **exponential equation** is an equation in which the unknown appears in an exponent, such as $3 \cdot 2^x = 45$. A **logarithmic equation** is an equation in which the unknown appears inside a logarithm, such as $\log_2 x + \log_2(x - 2) = 3$.

Two facts do the work. Because $b^x$ is one-to-one (for $b > 0$ and $b \ne 1$), and so is $\log_b x$:

$$
b^m = b^n \implies m = n, \qquad \log_b M = \log_b N \implies M = N \ (M, N > 0).
$$

In plain words, if two powers of the same base are equal, their exponents are equal, and if two logarithms with the same base are equal, their arguments are equal. A related fact justifies the main move below: if two positive numbers are equal, their logarithms are equal. That is true because a logarithm is a function, so equal inputs give equal outputs.

An **extraneous solution** is a number that comes out of the algebra but does not satisfy the original equation. In logarithmic equations the usual cause is that a step (such as condensing two logarithms into one) accepts inputs that the original logarithms could not take. The remedy is to check every candidate in the original equation.

## How to do it

### Solving an exponential equation

1. Isolate the exponential expression: divide by any coefficient and move any added or subtracted number to the other side. The goal is one power on one side, as in $b^{(\text{stuff})} = c$.
2. If both sides can be written as powers of the same base, write them that way and set the exponents equal. For example $2^{x+1} = 32 = 2^5$ gives $x + 1 = 5$.
3. Otherwise, take a logarithm of both sides. Natural logs are convenient since every calculator has them, but any base gives the same answer.
4. Use the power rule to bring the exponent down: $\ln\left(b^{(\text{stuff})}\right) = (\text{stuff})\ln b$.
5. Solve the resulting equation for the unknown. Divide by $\ln b$; don't subtract it.
6. Keep an exact answer as a quotient of logarithms, and round only at the end when a decimal is requested.
7. Check by putting the answer back into the original equation.

The key point is Step 1: isolate before you take the log. The rules of logarithms cover products and powers but not sums, so $2^x + 3 = 11$ must become $2^x = 8$ first. The edge cases below show what goes wrong otherwise.

An equation $b^x = c$ with $c > 0$ always has exactly one solution, $x = \log_b c$. If $c \le 0$ it has no real solution, since every power of a positive base is positive.

### Unknown in more than one exponent

When $x$ appears in two different exponents, as in $3^{2x-1} = 5^x$, the bases differ and can't be matched. Take the log of both sides and bring both exponents down. You get a linear equation in $x$ with logarithms as its coefficients. Gather the terms with $x$ on one side, factor out the $x$, and divide.

### Equations that are quadratic in form

An equation like $e^{2x} - 5e^x + 6 = 0$ has the same exponential twice, once squared. Since $e^{2x} = \left(e^x\right)^2$, substitute $u = e^x$ to get an ordinary quadratic, $u^2 - 5u + 6 = 0$, with solutions $u = 2$ and $u = 3$ ([solving quadratic equations](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md)). Then solve $e^x = u$ for each. A solution $u \le 0$ would be discarded, because $e^x$ is always positive.

### Solving a logarithmic equation

1. Write the domain: every expression inside a logarithm must be positive. Keep this as a list of conditions on $x$.
2. Combine the logarithms into one using the product and quotient rules, so the equation has the form $\log_b(\text{stuff}) = c$ or $\log_b(\text{stuff}) = \log_b(\text{other})$.
3. Remove the logarithm. Either rewrite it in exponent form, $\text{stuff} = b^c$, or, when both sides are logarithms of the same base, set the arguments equal.
4. Solve the resulting equation. It may be linear or quadratic.
5. Check every candidate against the domain from Step 1. Throw out any that make an argument zero or negative.
6. Check the survivors in the original equation.

### Solving for time in compound interest

Compound interest puts the unknown in an exponent, so this is an exponential equation. From the last lesson, a present value $\text{PV}$ at the annual rate $r$ compounded $m$ times a year becomes

$$
\text{FV} = \text{PV}\left(1 + \frac{r}{m}\right)^{mt}.
$$

To find $t$, divide by $\text{PV}$, take the logarithm of both sides and divide:

$$
t = \frac{\ln\left(\text{FV}/\text{PV}\right)}{m \ln\left(1 + \frac{r}{m}\right)}.
$$

With continuous compounding, $\text{FV} = \text{PV}\,e^{rt}$ and the natural log undoes $e$ exactly: $t = \dfrac{\ln\left(\text{FV}/\text{PV}\right)}{r}$. For doubling, $\frac{\text{FV}}{\text{PV}} = 2$ and the numerator is $\ln 2 = 0.6931$.

This table shows the time for money to double at 4% a year under the three kinds of compounding. The time falls only slightly as compounding gets more frequent.

| Compounding | Doubling time (years) |
|---|---|
| annually ($m = 1$) | $\dfrac{\ln 2}{\ln 1.04} = 17.67$ |
| monthly ($m = 12$) | $\dfrac{\ln 2}{12\ln\left(1 + 0.04/12\right)} = 17.36$ |
| continuously | $\dfrac{\ln 2}{0.04} = 17.33$ |

The finance chapter uses the same method in [doubling time, the rule of 72 and logs](../../08-financial-math/02-interest-and-growth/05-doubling-time-rule-of-72-and-logs.md).

### The rule of 72

Finding a doubling time exactly needs a logarithm. The **rule of 72** gives it in your head: money growing at $R\%$ per period, compounded each period, takes about $\frac{72}{R}$ periods to double.

Here is how well it works. The exact doubling time at $R\%$ per period is $\dfrac{\ln 2}{\ln(1 + R/100)}$.

| Rate $R\%$ | Exact doubling time | $72 \div R$ | Rule is off by |
|---|---|---|---|
| 1 | 69.66 | 72.00 | 3.4% too high |
| 2 | 35.00 | 36.00 | 2.9% too high |
| 4 | 17.67 | 18.00 | 1.9% too high |
| 6 | 11.90 | 12.00 | 0.9% too high |
| 8 | 9.01 | 9.00 | 0.1% too low |
| 12 | 6.12 | 6.00 | 1.9% too low |
| 18 | 4.19 | 4.00 | 4.5% too low |
| 36 | 2.25 | 2.00 | 11.3% too low |

The rule is closest near 8% and stays within about 2% from 4% to 12%. It gets worse at the extremes: for very low rates 70 works better (at 1%, $\frac{70}{1} = 70$ against the exact 69.66), and for rates above about 20% the error is more than 5%.

The reason comes from the logarithm. For a small rate $r$ written as a decimal, $\ln(1 + r) \approx r - \frac{r^2}{2}$, which is a little less than $r$. So the exact time is about $\frac{\ln 2}{r}\left(1 + \frac{r}{2}\right) = \frac{69.3}{R}\left(1 + \frac{r}{2}\right)$. For $r = 0.08$ the factor is 1.04, and $69.3 \cdot 1.04 = 72.07$. So 72 is the number that fits best around 8%. It is also handy because 72 divides evenly by 1, 2, 3, 4, 6, 8, 9 and 12, the rates that come up most.

### Half-life problems

A quantity with half-life $T$ follows $A(t) = A_0 \cdot \left(\frac{1}{2}\right)^{t/T}$. To find the time at which a given fraction remains, set $A(t)$ equal to that amount and solve:

$$
\left(\tfrac{1}{2}\right)^{t/T} = \frac{A}{A_0} \implies \frac{t}{T}\ln\tfrac{1}{2} = \ln\frac{A}{A_0} \implies t = T\cdot\frac{\ln(A/A_0)}{\ln(1/2)} = T\log_2\frac{A_0}{A}.
$$

The last form says the time is the half-life times the number of halvings, $\log_2\frac{A_0}{A}$. For example, carbon-14 has a half-life of about 5,730 years (Britannica gives 5,730 plus or minus 40 years, and other tables round it a little differently; see [Britannica, carbon-14](https://www.britannica.com/science/carbon-14), checked 2026). A sample that still has 30% of the carbon-14 of living tissue is about $5730 \cdot \log_2\frac{1}{0.30} = 5730 \cdot 1.737 = 9{,}953$ years old, about 10,000 years.

### Population and inflation

Both are exponential growth at a percent rate, so both use the same equation, $\text{final} = \text{start} \cdot (1 + r)^t$. Take a town of 120,000 people that grows 1.8% a year (an assumed rate). It reaches 150,000 when $1.018^t = 1.25$, so $t = \frac{\ln 1.25}{\ln 1.018} = 12.5$ years.

Inflation raises prices by a percent each year, so prices multiply by $(1 + r)^t$. The Bank of Canada's inflation target is 2% a year ([Bank of Canada, inflation](https://www.bankofcanada.ca/core-functions/monetary-policy/inflation/), checked 2026). At a steady 2% a year, prices double after $\frac{\ln 2}{\ln 1.02} = 35.0$ years, the same as the rule of 72 predicts with $\frac{72}{2} = 36$. They rise by half after $\frac{\ln 1.5}{\ln 1.02} = 20.5$ years. Another way to say it: a dollar buys about half as much after 35 years of 2% inflation. The 2% is a target, and actual inflation in a given year has been higher and lower ([CPI and inflation](../../07-economics-math/01-measuring-the-economy/07-cpi-and-inflation.md)).

## Worked examples

<div class="example" markdown>

### Example 1: when does \$5,000 double at 4% compounded monthly?

Find the number of years for \$5,000 to become \$10,000 at 4% a year compounded monthly.

Step 1: the equation is $5000\left(1 + \frac{0.04}{12}\right)^{12t} = 10000$. Isolate the power by dividing by 5000:

$$
\left(1 + \frac{0.04}{12}\right)^{12t} = 2.
$$

Step 2: the base $1.003333\ldots$ and the number 2 are not powers of a common base, so go to Step 3.

Step 3: take the natural log of both sides. Step 4: the power rule brings $12t$ down:

$$
12t \cdot \ln\left(1.003333\ldots\right) = \ln 2.
$$

Step 5: divide by $12\ln(1.003333\ldots)$. With $\ln(1.003333\ldots) = 0.0033278$ and $\ln 2 = 0.693147$,

$$
t = \frac{\ln 2}{12 \cdot 0.0033278} = \frac{0.693147}{0.039934} = 17.36.
$$

So it takes about 17.36 years, which is 17 years and about 4 months. The exact answer is $t = \dfrac{\ln 2}{12\ln\left(1 + 0.04/12\right)}$.

Step 7: check by putting the answer back. With the unrounded $t$, $12t = 208.29$ and $5000 \cdot (1.003333\ldots)^{208.29} = 10{,}000$; with the rounded $t = 17.36$ the balance is \$10,000.98. A real account adds interest once a month, so look at whole months: after 208 months the balance is \$9,990.34 and after 209 months it is \$10,023.64. The balance first passes \$10,000 at month 209, which is 17 years and 5 months.

Compare: annual compounding takes 17.67 years and the rule of 72 says $\frac{72}{4} = 18$ years. The estimate is a little high, as the table above showed for 4%.

<div class="warning" markdown>

Watch out at Step 5: the exponent was $12t$, not $t$. Dividing $\ln 2$ by $\ln 1.003333$ alone gives 208.3, which is the value of $12t$, the number of months. Reading it as years is the mistake.

</div>

</div>

<div class="example" markdown>

### Example 2: same base, and two different bases

(a) Solve $2^{x+1} = 32$. (b) Solve $3^{2x-1} = 5^x$.

(a) Step 2 applies: $32 = 2^5$, so $2^{x+1} = 2^5$ and $x + 1 = 5$, giving $x = 4$. Check: $2^{4+1} = 32$.

(b) The bases 3 and 5 differ, so use logs. Take $\ln$ of both sides and bring the exponents down:

$$
(2x - 1)\ln 3 = x\ln 5.
$$

Distribute, gather the $x$ terms on one side and factor:

$$
2x\ln 3 - \ln 3 = x\ln 5 \implies x\left(2\ln 3 - \ln 5\right) = \ln 3 \implies x = \frac{\ln 3}{2\ln 3 - \ln 5}.
$$

Numerically, $\ln 3 = 1.098612$, $\ln 5 = 1.609438$, so the bottom is $0.587787$ and $x = 1.8691$.

Check: $3^{2x-1} = 3^{2.7381} = 20.25$ and $5^{1.8691} = 20.25$. Both sides agree.

</div>

<div class="example" markdown>

### Example 3: a logarithmic equation with an extraneous solution

Solve $\log_2 x + \log_2(x - 2) = 3$.

Step 1: the domain needs $x > 0$ and $x - 2 > 0$, so $x > 2$.

Step 2: the product rule combines the logs: $\log_2\left(x(x - 2)\right) = 3$.

Step 3: rewrite in exponent form: $x(x - 2) = 2^3 = 8$.

Step 4: this is a quadratic, and $x^2 - 2x - 8 = 0$ factors as $(x - 4)(x + 2) = 0$, so the candidates are $x = 4$ and $x = -2$.

Step 5: the domain requires $x > 2$. The candidate $x = 4$ is fine, and $x = -2$ is not. Putting $-2$ into the original gives $\log_2(-2)$, which doesn't exist. So $x = -2$ is an extraneous solution, and it appeared because condensing created a product $x(x - 2)$ that is positive for $x = -2$ even though neither factor's logarithm is defined.

Step 6: check $x = 4$: $\log_2 4 + \log_2 2 = 2 + 1 = 3$. The answer is $x = 4$.

</div>

<div class="example" markdown>

### Example 4: when does the drug fall to 15 mg? (finish it yourself)

A 200 mg dose has a half-life of 6 hours, so $A(t) = 200\left(\frac{1}{2}\right)^{t/6}$ milligrams after $t$ hours. When does the amount reach 15 mg?

Step 1: set $200\left(\frac{1}{2}\right)^{t/6} = 15$ and divide by 200: $\left(\frac{1}{2}\right)^{t/6} = 0.075$.

Step 3 and Step 4: take $\ln$ of both sides and bring the exponent down: $\frac{t}{6}\ln\frac{1}{2} = \ln 0.075$.

Now do Step 5, find $t$, and check by substituting it back.

<details class="solution" markdown>
<summary>Finish</summary>

Step 5: $\ln 0.075 = -2.5903$ and $\ln\frac{1}{2} = -0.6931$, so $\frac{t}{6} = \frac{-2.5903}{-0.6931} = 3.737$ and $t = 6 \cdot 3.737 = 22.42$ hours. Equivalently, $t = 6\log_2\frac{200}{15}$, since 200 mg must halve $\log_2 13.33 = 3.737$ times.

Check: $200\left(\frac{1}{2}\right)^{22.42/6} = 200 \cdot 0.075 = 15$. It is between 3 half-lives (18 hours, 25 mg) and 4 half-lives (24 hours, 12.5 mg), and 22.4 hours is between 18 and 24.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: take the logarithm of the whole side, not of each term. To solve $2^x + 3 = 11$, writing "$x\ln 2 + \ln 3 = \ln 11$" is wrong because $\ln(2^x + 3) \ne \ln 2^x + \ln 3$. Isolate first: $2^x = 8$, so $x = 3$. A product on the side is fine: $5 \cdot 2^x = 40$ can be logged directly as $\ln 5 + x\ln 2 = \ln 40$, though dividing by 5 first is shorter.

</div>

<div class="warning" markdown>

Watch out: $x = \dfrac{\ln 15}{\ln 2}$ is a quotient of logarithms, and it is not $\ln 15 - \ln 2$. The first is $\log_2 15 = 3.907$. The second is $\ln 7.5 = 2.015$. After the power rule you have $x\ln 2 = \ln 15$, and you divide by $\ln 2$.

</div>

<div class="warning" markdown>

Watch out: rounding the logarithms early can shift the answer a lot. In Example 1 the factor $12\ln(1.003333\ldots)$ is small, so rounding $\ln 1.003333$ to $0.003$ would give $t = 19.25$ years instead of 17.36. Keep six digits or more in the middle of a calculation, or keep the exact quotient until the last step.

</div>

<div class="warning" markdown>

Watch out: keep the units of the rate and the time together. If the rate is per month, $t$ counts months, and if $t$ is in years with a monthly rate you need the exponent $12t$, as in Example 1.

</div>

Some exponential equations have no solution. The equation $2^x = -4$ has none, because $2^x$ is always positive, and $2^x = 0$ has none either. A calculator will show an error for $\ln(-4)$, which is the hint. In the same way $\log_2 x = -3$ does have a solution, $x = \frac{1}{8}$, since a logarithm can be any real number.

Solutions can be negative or untidy, and both are fine. The equation $2^x = \frac{1}{8}$ gives $x = -3$, a time before the start. An answer such as $x = \log_2 15$ is exact, while $3.907$ is its approximation, so write the exact form when a question asks for exact.

Be careful about losing a solution. The equation $\ln\left(x^2\right) = 4$ has two solutions: $x^2 = e^4$ gives $x = e^2$ and $x = -e^2$, since $\ln\left((-e^2)^2\right) = \ln e^4 = 4$. If you first rewrote it as $2\ln x = 4$, you would find only $x = e^2$, because that form needs $x > 0$. Example 3 of [logarithm properties](03-logarithm-properties.md#worked-examples) explains why the power rule changes the domain.

## Tricks and shortcuts

Try to write both sides as powers of one base before reaching for logarithms. Numbers like 4, 8, 16, 32 are powers of 2, and 9, 27, 81 are powers of 3. Then $4^{x} = 8^{x-1}$ becomes $2^{2x} = 2^{3(x-1)}$, so $2x = 3x - 3$ and $x = 3$.

Bracket your answer before you calculate. For $2^x = 15$, since $2^3 = 8$ and $2^4 = 16$, the answer is a little under 4. If your calculator says 3.907, it is right, and if it says 7.5, you divided when you should have taken a logarithm.

Use the rule of 72 as an estimate and a check. If a calculation says money doubles in 3 years at 4%, the rule says 18 years, so something is wrong. For growth by any factor $F$, the time is about $\frac{100\ln F}{R}$ periods, a little more at higher rates. The factor $F = 2$ gives 69.3, and $F = 3$ gives 109.9, which becomes about 114 at 8% after the same correction that turns 69.3 into 72.

## In code

The code solves the equations of this lesson with `math.log`, finds the doubling month by direct search, and checks the rule of 72.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

# 3 * 2**x = 45
x = math.log(45 / 3, 2)
print(round(x, 4))                                   # 3.9069

# 3**(2x - 1) = 5**x
x = math.log(3) / (2 * math.log(3) - math.log(5))
print(round(x, 4), round(3 ** (2 * x - 1), 3), round(5**x, 3))  # 1.8691 20.25 20.25

# Doubling time for 4% a year: annual, monthly, continuous
annual = math.log(2) / math.log(1.04)
monthly = math.log(2) / (12 * math.log(1 + 0.04 / 12))
continuous = math.log(2) / 0.04
print(round(annual, 2), round(monthly, 2), round(continuous, 2))  # 17.67 17.36 17.33

# The first whole month with at least 10,000 in the account
balance, months = 5000.0, 0
while balance < 10000:
    balance *= 1 + 0.04 / 12
    months += 1
print(months, round(balance, 2))                     # 209 10023.64

# Rule of 72 against the exact doubling time
for rate in (1, 4, 8, 12, 36):
    exact = math.log(2) / math.log(1 + rate / 100)
    print(rate, round(exact, 2), 72 / rate)
# 1 69.66 72.0
# 4 17.67 18.0
# 8 9.01 9.0
# 12 6.12 6.0
# 36 2.25 2.0

# The extraneous root in log2(x) + log2(x - 2) = 3
for candidate in (4, -2):
    ok = candidate > 2
    print(candidate, ok, math.log2(candidate) + math.log2(candidate - 2) if ok else "not in the domain")
# 4 True 3.0
# -2 False not in the domain
```

</details>

## FAQ

### Why am I allowed to take the logarithm of both sides?

Because a logarithm is a function: if two positive numbers are equal, their logarithms are equal. You are applying the same operation to both sides, like adding 5 to both sides. It is also reversible, because $\log_b$ is one-to-one, so no solutions are lost or invented. The only requirement is that both sides are positive, which is why $2^x = -4$ can't be logged.

### Does the choice of logarithm base matter?

No. The logarithms $\ln$, $\log_{10}$ and $\log_2$ all give the same $x$, because each base's logarithms differ by a constant factor that cancels in the quotient: $\frac{\ln 15}{\ln 2} = \frac{\log_{10} 15}{\log_{10} 2}$. Use whichever your calculator has, and use the same one in the numerator and denominator.

### Why do extraneous solutions appear at all?

Some steps enlarge the set of numbers the equation accepts. Condensing $\log_2 x + \log_2(x - 2)$ into $\log_2\left(x(x - 2)\right)$ accepts $x = -2$, because the product is positive there. Squaring both sides of an equation does the same, as in radical equations ([rational and radical equations](../06-rational-expressions-and-equations/03-rational-and-radical-equations.md)). Such a step is fine as long as every candidate is checked in the original equation.

### Why does the rule of 72 use 72 and not 69.3?

The number 69.3 is $100\ln 2$, the exact doubling time in the limit of a tiny rate. For rates people actually earn the exact time is a bit larger, about 72 at 8%, as the derivation showed. Also 72 divides by many numbers, so it is easy to use in your head.

## Practice

### Warm-up

1\. Solve $2^x = 64$ and $5^{x-1} = \frac{1}{25}$.

<details class="solution" markdown>
<summary>Solution</summary>

Write each side as a power of the same base. Since $2^x = 64 = 2^6$, we get $x = 6$. And $5^{x-1} = \frac{1}{25} = 5^{-2}$ gives $x - 1 = -2$, so $x = -1$.

Check: $2^6 = 64$ and $5^{-1-1} = 5^{-2} = \frac{1}{25}$.

</details>

2\. Solve (a) $4 \cdot 3^x = 108$ exactly and (b) $7^x = 20$ to three decimal places.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Isolate the power: $3^x = 27 = 3^3$, so $x = 3$.

(b) Take $\ln$ of both sides: $x\ln 7 = \ln 20$, so $x = \dfrac{\ln 20}{\ln 7} = \dfrac{2.995732}{1.945910} = 1.540$.

Check: $4 \cdot 3^3 = 108$, and $7^{1.5395} = 20.0$. The answer is between 1 and 2, as it should be, since $7^1 = 7$ and $7^2 = 49$.

</details>

3\. Solve $\ln x = 3$ and $\log_3(x + 1) = 2$.

<details class="solution" markdown>
<summary>Solution</summary>

In exponent form, $\ln x = 3$ gives $x = e^3 = 20.086$. And $\log_3(x + 1) = 2$ gives $x + 1 = 3^2 = 9$, so $x = 8$.

Check: $\ln(e^3) = 3$, and $\log_3(8 + 1) = \log_3 9 = 2$. Both answers are in the domains ($x > 0$ and $x > -1$).

</details>

### Standard

4\. How long until \$2,000 grows to \$3,000 at 5% a year, (a) compounded annually and (b) compounded monthly?

<details class="solution" markdown>
<summary>Solution</summary>

The ratio is $\frac{3000}{2000} = 1.5$.

(a) $1.05^t = 1.5$, so $t = \dfrac{\ln 1.5}{\ln 1.05} = \dfrac{0.405465}{0.048790} = 8.31$ years.

(b) $\left(1 + \frac{0.05}{12}\right)^{12t} = 1.5$, so $t = \dfrac{\ln 1.5}{12\ln\left(1 + 0.05/12\right)} = \dfrac{0.405465}{12 \cdot 0.0041580} = 8.13$ years.

Check: $2000 \cdot 1.05^{8.31} = 3000$ and $2000\left(1 + \frac{0.05}{12}\right)^{97.5} = 3000$. Monthly compounding is a little faster, as expected.

</details>

5\. Solve $2^{x+3} = 5^x$ exactly, then to three decimals.

<details class="solution" markdown>
<summary>Solution</summary>

Take $\ln$ of both sides: $(x + 3)\ln 2 = x\ln 5$. Expand and gather: $x\ln 2 + 3\ln 2 = x\ln 5$, so $3\ln 2 = x\left(\ln 5 - \ln 2\right)$ and

$$
x = \frac{3\ln 2}{\ln 5 - \ln 2} = \frac{3\ln 2}{\ln 2.5} = \frac{2.0794}{0.9163} = 2.269.
$$

Check: $2^{x+3} = 2^{5.269} = 38.57$ and $5^{2.269} = 38.57$.

</details>

6\. Solve $\log_2(x + 6) + \log_2 x = 4$ and state which candidates are extraneous.

<details class="solution" markdown>
<summary>Solution</summary>

The domain needs $x + 6 > 0$ and $x > 0$, so $x > 0$. Condense: $\log_2\left(x(x + 6)\right) = 4$, so $x^2 + 6x = 16$ and $x^2 + 6x - 16 = 0$, which factors as $(x + 8)(x - 2) = 0$. The candidates are $x = -8$ and $x = 2$.

Since the domain needs $x > 0$, the candidate $x = -8$ is extraneous, and $x = 2$ is the solution.

Check: $\log_2 8 + \log_2 2 = 3 + 1 = 4$. And $x = -8$ would need $\log_2(-8)$, which doesn't exist.

</details>

### Challenge

7\. A bone has 20% of the carbon-14 that living tissue has. Using a half-life of 5,730 years, how old is it? How much remains after 20,000 years?

<details class="solution" markdown>
<summary>Solution</summary>

The fraction remaining after $t$ years is $\left(\frac{1}{2}\right)^{t/5730}$. Setting it equal to 0.20 gives $\frac{t}{5730}\ln\frac{1}{2} = \ln 0.2$, so $t = 5730 \cdot \dfrac{\ln 0.2}{\ln 0.5} = 5730 \cdot 2.3219 = 13{,}305$ years. In other words, the sample went through $\log_2 5 = 2.32$ half-lives.

After 20,000 years: $\left(\frac{1}{2}\right)^{20000/5730} = \left(\frac{1}{2}\right)^{3.49} = 0.0890$, about 8.9%.

Check: $0.5^{13305/5730} = 0.5^{2.322} = 0.2$. Also 13,305 years is between 2 half-lives (11,460 years, 25% left) and 3 half-lives (17,190 years, 12.5% left).

</details>

8\. (Reviews [solving quadratic equations](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md).) Solve $e^{2x} - 5e^x + 6 = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

Let $u = e^x$. Since $e^{2x} = \left(e^x\right)^2 = u^2$, the equation is $u^2 - 5u + 6 = 0$, which factors as $(u - 2)(u - 3) = 0$. So $u = 2$ or $u = 3$.

Both are positive, so both are allowed. Solve $e^x = 2$ and $e^x = 3$: $x = \ln 2 = 0.693$ or $x = \ln 3 = 1.099$.

Check: for $x = \ln 2$, $e^{2x} = 4$ and $e^x = 2$, so $4 - 10 + 6 = 0$. For $x = \ln 3$, $e^{2x} = 9$ and $e^x = 3$, so $9 - 15 + 6 = 0$.

</details>

## Where this shows up

- In finance, "how long until my investment reaches a goal?" and "what rate do I need?" are these equations. The finance chapter builds on them in [compound interest](../../08-financial-math/02-interest-and-growth/02-compound-interest.md) and [inflation and real returns](../../08-financial-math/02-interest-and-growth/06-inflation-and-real-returns.md).
- In algorithm analysis, "how large an input can I handle in a budget of steps?" is an equation such as $2^n = 10^9$, with answer $n = \log_2 10^9 \approx 29.9$. Counting the levels of a recursion with [recurrences](../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md) also uses logarithms.
- In calculus, the same methods solve for the point where an exponential model reaches a value ([the derivative definition](../../05-university-core/02-derivatives/01-the-derivative-definition.md)), and in statistics, maximum-likelihood equations are solved after taking logarithms.
