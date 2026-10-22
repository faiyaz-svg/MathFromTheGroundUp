# First-order differential equations

After this lesson you can read a slope field, solve separable and first-order linear equations, model growth, decay, cooling and the logistic curve, run Euler's method and judge its error, and set up a simple price-adjustment or growth model in economics.

Before this: [the chain rule](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md), [u-substitution](../04-integrals/03-u-substitution.md), [partial fractions](../04-integrals/05-partial-fractions-and-improper-integrals.md) and [exponential functions and growth](../../03-high-school/07-exponentials-and-logarithms/01-exponential-functions-and-growth.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Check that $y = 3e^{2t}$ solves $y' = 2y$.
2. Solve $y' = ty$ with $y(0) = 2$.
3. A population grows continuously at 3% a year, so $P' = 0.03P$. How long does it take to double?

<details class="solution" markdown>
<summary>Answers</summary>

1. The derivative of $3e^{2t}$ is $6e^{2t}$, and $2y = 2 \cdot 3e^{2t} = 6e^{2t}$. They are equal, so it is a solution.
2. Separate: $\frac{dy}{y} = t\,dt$, so $\ln\lvert y \rvert = \frac{t^2}{2} + C$ and $y = Ae^{t^2/2}$. The condition $y(0) = 2$ gives $A = 2$, so $y = 2e^{t^2/2}$.
3. $P = P_0e^{0.03t}$ doubles when $e^{0.03t} = 2$, so $t = \frac{\ln 2}{0.03} \approx 23.1$ years.

</details>

## The idea

A bank account earns interest at 5% a year, paid continuously. The bigger the balance, the faster it grows: the rate of growth is proportional to the balance. In symbols, if $A(t)$ is the balance, $A'(t) = 0.05A(t)$. This is not a formula for $A$. It is a statement about how $A$ changes, and the job is to recover $A$ from it. A **differential equation** is an equation that contains a function and its derivatives. Solving it means finding the functions that satisfy it.

Differential equations are the language of anything that changes by a rule. The rate at which a hot drink cools depends on how much hotter it is than the room. The rate at which a drug leaves the blood depends on how much is left. The rate at which a price moves depends on the gap between demand and supply. In each case the rule gives the derivative in terms of the current state, and the future follows from the present.

There is a picture for this. At each point $(t, y)$ of the plane, the rule says what the slope of a solution through that point must be. Draw a short segment with that slope at many points, and a solution is a curve that follows the segments, the way a leaf follows the current of a stream. This picture, a slope field, is the first tool. The figure shows it for the logistic equation of this lesson, which models growth that levels off.

![A slope field for the equation N' = 0.5 N (1 minus N): short grey segments, flat along N = 0 and N = 1 and steepest near N = 0.5. Four solution curves: one from 0.001 that creeps along the bottom, then rises in an S shape and approaches 1 by t = 16; one from 0.2 that rises to 1; one from 0.6 that rises to 1; and one from 1.3 above the dashed line N = 1 that falls toward 1. The horizontal dashed line N = 1 is marked as the capacity.](../../assets/figures/05-university-core/first-order-differential-equations-slope-field.svg)

## Definitions

A **differential equation** (DE) is an equation involving an unknown function $y(t)$ and its derivatives. Its **order** is the highest derivative that appears, so $y' = 2y$ is first order and $y'' + y = 0$ is second order. A **solution** is a function that makes the equation true on an interval. In plain words, put $y$ and its derivatives into the equation and you get a true statement for every $t$ in the interval.

A first-order equation in standard form is $y' = f(t, y)$. A **general solution** is a family of solutions with an arbitrary constant, such as $y = Ce^{2t}$. An **initial value problem** (IVP) is the equation together with a starting condition $y(t_0) = y_0$, which picks one solution from the family. In plain words, the equation gives the rule and the initial condition gives the starting point.

An equation is **autonomous** if $f$ doesn't depend on $t$, so $y' = f(y)$. An **equilibrium solution** of such an equation is a constant solution $y = c$, where $f(c) = 0$. An equilibrium is **stable** if solutions that start nearby move toward it, and **unstable** if they move away.

A **slope field** (or direction field) is the picture of $y' = f(t, y)$ made by drawing, at many points $(t, y)$, a short segment of slope $f(t, y)$.

A first-order equation is **separable** if it can be written $y' = g(t)h(y)$, a product of a function of $t$ and a function of $y$. It is **linear** if it can be written $y' + p(t)y = q(t)$, where $p$ and $q$ are given functions of $t$.

**Euler's method** with step size $h$ approximates the solution of $y' = f(t, y)$, $y(t_0) = y_0$ by the sequence $y_{n+1} = y_n + h\,f(t_n, y_n)$ with $t_{n+1} = t_n + h$. In plain words, walk along the tangent line for a short step, then recompute the slope.

## How to do it

### Checking a solution

Substitute. Compute $y'$ from the claimed formula, put both into the equation and simplify. To check an initial condition, put in $t_0$. This is also the check for every method below, and it takes a minute.

### Reading a slope field and finding equilibria

1. For an autonomous equation $y' = f(y)$, solve $f(y) = 0$. The solutions are the equilibria, drawn as horizontal lines.
2. Between two equilibria, the sign of $f$ is fixed: positive means solutions rise, negative means they fall.
3. An equilibrium is stable if $f$ is positive just below it and negative just above it (solutions move toward it), and unstable if the signs are the other way round. If $f'$ exists at the equilibrium $c$, then $f'(c) < 0$ means stable and $f'(c) > 0$ means unstable.
4. Solution curves never cross, because a point has one slope. So a solution that starts between two equilibria stays between them.

### Separable equations

1. Check that $y' = g(t)h(y)$. Write $y' = \frac{dy}{dt}$.
2. If $h(y) = 0$ for some constant $y = c$, then $y = c$ is a solution (an equilibrium). Set these aside.
3. Otherwise separate the variables: $\frac{dy}{h(y)} = g(t)\,dt$.
4. Integrate both sides, with one constant: $\int\frac{dy}{h(y)} = \int g(t)\,dt + C$.
5. Solve for $y$ if you can, use the initial condition to find $C$, and add back any equilibria set aside in Step 2 that the formula missed.
6. Check by substituting into the equation and the initial condition.

The separation looks like algebra with differentials and needs a reason. If $H(y)$ is an antiderivative of $\frac{1}{h(y)}$ and $G(t)$ one of $g(t)$, then the equation $H(y(t)) = G(t) + C$, differentiated with the chain rule, gives $H'(y)y' = G'(t)$, that is $\frac{y'}{h(y)} = g(t)$, the original equation. So solutions of the integrated equation solve the DE.

### Exponential growth and decay

*Theorem 1.* If $y' = ky$ for a constant $k$ on an interval containing $t_0$, then $y(t) = y(t_0)e^{k(t - t_0)}$.

What we know: $y' = ky$. What we want: a formula for $y$. The plan: instead of dividing by $y$ (which could be zero), show that the combination $y\,e^{-kt}$ has derivative zero.

*Proof.* Let $u(t) = y(t)e^{-kt}$. By the product rule, $u'(t) = y'e^{-kt} - ky\,e^{-kt} = (y' - ky)e^{-kt} = 0$. A function with derivative $0$ on an interval is constant (a consequence of the mean value theorem), so $u(t) = u(t_0)$ for all $t$, that is, $y(t)e^{-kt} = y(t_0)e^{-kt_0}$. Multiplying by $e^{kt}$ gives the formula. $\blacksquare$

Look back: the proof also shows that there is no other solution, which a "divide by $y$ and integrate" argument can't claim without extra care. If $k > 0$ it is growth, if $k < 0$ it is decay, and $\lvert k \rvert$ is the rate per unit time.

Three standard uses:

- *Continuous compounding.* A balance with interest rate $r$ compounded continuously satisfies $A' = rA$, so $A(t) = A_0e^{rt}$. It doubles after $\frac{\ln 2}{r}$ years. Continuous compounding and e<!-- link: ../../08-financial-math/02-interest-and-growth/04-continuous-compounding-and-e.md --> compares it with yearly and monthly compounding.
- *Radioactive decay.* A sample decays at a rate proportional to the amount present, $N' = -kN$, so $N(t) = N_0e^{-kt}$. The **half-life** is the time for half to decay, $t_{1/2} = \frac{\ln 2}{k}$, the same at every starting amount.
- *Newton's law of cooling.* An object at temperature $T$ in a room at $T_r$ changes at a rate proportional to the difference: $T' = -k(T - T_r)$ with $k > 0$. Put $u = T - T_r$. Then $u' = T' = -ku$, so $u = u_0e^{-kt}$ and $T(t) = T_r + (T_0 - T_r)e^{-kt}$. The temperature moves toward the room's temperature, fast at first and then more slowly.

### The logistic equation

Unlimited exponential growth can't last, because resources run out. The **logistic equation** is

$$
P' = rP\left(1 - \frac{P}{K}\right),
$$

where $r > 0$ is the growth rate when $P$ is small and $K > 0$ is the carrying capacity. In plain words, the growth rate per unit $\frac{P'}{P} = r\left(1 - \frac{P}{K}\right)$ falls from $r$ down to $0$ as $P$ rises to $K$. The equilibria are $P = 0$ (unstable, since $f'(0) = r > 0$) and $P = K$ (stable, since $f'(K) = -r < 0$). The growth rate $P'$ is largest at $P = \frac{K}{2}$, where it equals $\frac{rK}{4}$.

To solve it, put $N = \frac{P}{K}$, so that $N' = rN(1 - N)$. This is separable. By partial fractions, $\frac{1}{N(1 - N)} = \frac{1}{N} + \frac{1}{1 - N}$, so

$$
\ln\left\lvert\frac{N}{1 - N}\right\rvert = rt + C, \qquad\text{which gives}\qquad N(t) = \frac{1}{1 + Ae^{-rt}}, \quad A = \frac{1 - N_0}{N_0}.
$$

In terms of $P$, $P(t) = \frac{K}{1 + Ae^{-rt}}$ with $A = \frac{K - P_0}{P_0}$. The curve is S-shaped: slow growth at first, fastest at $P = \frac{K}{2}$, then levelling off at $K$.

### Linear equations and the integrating factor

*Theorem 2.* If $p$ and $q$ are continuous on an interval, then all solutions of $y' + p(t)y = q(t)$ are

$$
y(t) = e^{-P(t)}\left(\int e^{P(t)}q(t)\,dt + C\right), \qquad P(t) = \int p(t)\,dt.
$$

What we know: the equation. What we want: $y$. The plan: multiply the equation by a function $\mu(t)$ chosen so that the left side becomes the derivative of a product, $(\mu y)'$, which can be integrated.

*Proof.* Let $\mu(t) = e^{P(t)}$, so that $\mu' = p\mu$ by the chain rule. Multiply the equation by $\mu$: $\mu y' + p\mu y = \mu q$. The left side is $\mu y' + \mu' y = (\mu y)'$ by the product rule, so $(\mu y)' = \mu q$. Integrating, $\mu y = \int\mu q\,dt + C$, and dividing by $\mu$ gives the formula. Every step is reversible, so each such $y$ is a solution. $\blacksquare$

Look back: the function $\mu$ is the integrating factor, and the constant in $P$ doesn't matter, because it multiplies $\mu$ by a constant that cancels. For $p$ constant the integrating factor is $e^{pt}$, and the solution has the form $y = \frac{q}{p} + Ce^{-pt}$ when $q$ is also constant: it moves toward the equilibrium $\frac{q}{p}$.

### Existence and uniqueness

*Theorem (stated without proof).* If $f(t, y)$ and $\frac{\partial f}{\partial y}$ are continuous near the point $(t_0, y_0)$, then the initial value problem $y' = f(t, y)$, $y(t_0) = y_0$ has a solution on some interval around $t_0$, and there is only one.

Two examples show why the conditions matter. The equation $y' = 3y^{2/3}$ with $y(0) = 0$ has the solutions $y = 0$ and $y = t^3$ (check: $3(t^3)^{2/3} = 3t^2$), and many more, because $\frac{\partial f}{\partial y} = 2y^{-1/3}$ is not continuous at $y = 0$. And $y' = y^2$ with $y(0) = 1$ has the solution $y = \frac{1}{1 - t}$, which goes to infinity at $t = 1$: a solution can exist only on a short interval, even for a harmless-looking equation.

### Euler's method

When an equation can't be solved by a formula, Euler's method steps along the slope field.

1. Pick a step size $h$ and set $t_0$, $y_0$.
2. Compute the slope $f(t_n, y_n)$.
3. Step: $y_{n+1} = y_n + h\,f(t_n, y_n)$ and $t_{n+1} = t_n + h$.
4. Repeat until you reach the end time. Check by halving $h$ and seeing how much the answer changes.

For $y' = y$, $y(0) = 1$, the method gives $y_{n+1} = (1 + h)y_n$, so after reaching $t = 1$ with $n = \frac{1}{h}$ steps the estimate is $(1 + h)^{1/h}$, to be compared with the exact answer $e = 2.71828\ldots$.

| Step size $h$ | Estimate of $y(1)$ | Error $e - y$ | Error $\div\,h$ |
|---|---|---|---|
| 0.5 | 2.2500 | 0.4683 | 0.94 |
| 0.1 | 2.5937 | 0.1245 | 1.25 |
| 0.05 | 2.6533 | 0.0650 | 1.30 |
| 0.01 | 2.7048 | 0.0135 | 1.35 |

The error is proportional to $h$: it is cut by about $10$ when $h$ is cut by $10$, and the last column settles near $1.36 = \frac{e}{2}$. Euler's method is a first-order method. The reason is that each step makes an error of order $h^2$ (the tangent line departs from the curve by about $\frac{1}{2}y''h^2$) and there are $\frac{1}{h}$ steps. Better methods (Runge-Kutta) have errors proportional to $h^4$ and are what software uses.

![The curve y = e to the t from t = 0 to 1 in dark grey, ending at 2.718, and three Euler approximations, each a chain of straight steps starting at (0, 1) that stays below the curve. With step 0.5 (red, two steps) it ends at 2.250, with step 0.25 (orange, four steps) at 2.441, and with step 0.1 (blue, ten steps) at 2.594.](../../assets/figures/05-university-core/first-order-differential-equations-euler.svg)

The method can also fail. For $y' = -\lambda y$ with $\lambda > 0$, the exact solution decays, and Euler's method gives $y_{n+1} = (1 - \lambda h)y_n$. This decays only if $\lvert 1 - \lambda h \rvert < 1$, that is, $h < \frac{2}{\lambda}$. For a larger step the numbers oscillate and grow. This is the same arithmetic as gradient descent on a parabola from the [optimization lesson](../03-applications-of-derivatives/05-optimization.md#gradient-descent-in-one-variable), and for a reason: gradient descent $w \leftarrow w - \eta f'(w)$ is Euler's method with step $\eta$ for the equation $w' = -f'(w)$, the "gradient flow" that rolls downhill.

### Two models from economics

*A price adjusting toward equilibrium.* A common model says that the price rises when demand exceeds supply, and falls when supply exceeds demand, at a rate proportional to the gap: $p' = k\bigl(D(p) - S(p)\bigr)$ with $k > 0$. For hypothetical numbers, take demand $D = 100 - 2p$, supply $S = 10 + 4p$ and $k = 0.05$. Then $p' = 0.05(90 - 6p) = -0.3(p - 15)$. The equilibrium is $p^* = 15$ (where $D = S = 70$), and with $u = p - 15$ the equation $u' = -0.3u$ gives

$$
p(t) = 15 + (p_0 - 15)e^{-0.3t}.
$$

From $p_0 = 25$ the gap of 10 halves every $\frac{\ln 2}{0.3} \approx 2.31$ time units, and the price is within 1 of equilibrium when $10e^{-0.3t} = 1$, at $t = \frac{\ln 10}{0.3} \approx 7.68$. The equilibrium is stable because the slope of $D - S$ is negative.

*Capital accumulation.* In the Solow growth model, the capital per worker $k$ changes by savings minus depreciation: $k' = sk^{\alpha} - \delta k$, where $s$ is the savings rate and $\delta$ the depreciation rate, and $0 < \alpha < 1$. The equation is not linear, but the substitution $u = k^{1 - \alpha}$ gives $u' = (1 - \alpha)k^{-\alpha}k' = (1 - \alpha)(s - \delta u)$, which is linear. Its solution is

$$
u(t) = \frac{s}{\delta} + \left(u_0 - \frac{s}{\delta}\right)e^{-(1 - \alpha)\delta t}.
$$

The steady state is $u^* = \frac{s}{\delta}$, that is $k^* = \left(\frac{s}{\delta}\right)^{1/(1 - \alpha)}$. With the hypothetical numbers $\alpha = 0.3$, $s = 0.2$, $\delta = 0.05$ and $k_0 = 1$, the steady state is $k^* = 4^{1/0.7} \approx 7.25$, and the gap closes at the rate $(1 - \alpha)\delta = 0.035$ per year: $k$ reaches $3.72$ after 20 years. The half-life of the gap in $u$ is $\frac{\ln 2}{0.035} \approx 19.8$ years. The numbers are made up to show the method, and not estimates of any economy.

## Worked examples

<div class="example" markdown>

### Example 1: a separable equation with an initial condition

Solve $\frac{dy}{dx} = \frac{x}{y}$ with $y(0) = 2$.

Step 1: the right side is $g(x)h(y)$ with $g(x) = x$ and $h(y) = \frac{1}{y}$. Step 2: $h$ is never $0$, so there are no equilibria to set aside (the value $y = 0$ isn't allowed in $\frac{x}{y}$ anyway).

Step 3: separating, $y\,dy = x\,dx$. Step 4: integrating, $\frac{y^2}{2} = \frac{x^2}{2} + C$, that is, $y^2 = x^2 + 2C$. Step 5: the condition $y(0) = 2$ gives $4 = 2C$, so $y^2 = x^2 + 4$. Since $y(0) = 2 > 0$ and $y$ can't pass through $0$ (the equation breaks there), the solution is the positive root $y = \sqrt{x^2 + 4}$, defined for all $x$.

Step 6, the check: $y' = \frac{x}{\sqrt{x^2 + 4}} = \frac{x}{y}$, and $y(0) = 2$. The curves $y^2 - x^2 = C$ are hyperbolas, which is what the slope field of $\frac{x}{y}$ shows.

</div>

<div class="example" markdown>

### Example 2: continuous compounding and decay

(a) How much is \$1,000 worth after 10 years at 5% compounded continuously, and when does it double? (b) A hypothetical sample has a half-life of 12 hours. What fraction remains after 36 hours, and when is 10% left?

(a) $A' = 0.05A$ gives $A = 1000e^{0.05t}$. At $t = 10$, $A = 1000e^{0.5} = \$1{,}648.72$. It doubles when $e^{0.05t} = 2$, at $t = \frac{\ln 2}{0.05} \approx 13.86$ years. For comparison, yearly compounding gives $1000(1.05)^{10} = \$1{,}628.89$, a little less.

(b) The half-life gives $k = \frac{\ln 2}{12} \approx 0.05776$ per hour. After 36 hours, which is three half-lives, the fraction is $\left(\frac{1}{2}\right)^3 = \frac{1}{8}$. The sample is at 10% when $e^{-kt} = 0.1$, so $t = \frac{\ln 10}{k} = 12\log_2 10 \approx 39.86$ hours.

Check: $1648.72 = 1000e^{0.5}$ and $e^{0.5} = 1.6487$. For (b), $e^{-0.05776 \cdot 36} = e^{-2.079} = 0.125$.

</div>

<div class="example" markdown>

### Example 3: a cooling cup of coffee

Coffee at $90^\circ\text{C}$ is left in a $20^\circ\text{C}$ room. After 10 minutes it is at $70^\circ\text{C}$. When will it reach $40^\circ\text{C}$?

The model is $T = 20 + 70e^{-kt}$. At $t = 10$ it is $70$, so $e^{-10k} = \frac{50}{70} = \frac{5}{7}$ and $k = \frac{\ln(7/5)}{10} \approx 0.03365$ per minute. The temperature is $40$ when $70e^{-kt} = 20$, so $e^{-kt} = \frac{2}{7}$ and $t = \frac{\ln 3.5}{k} \approx 37.23$ minutes.

Check: after another 10 minutes the gap is $50 \cdot \frac{5}{7} = 35.7$, so the temperature is $55.7^\circ\text{C}$, and the gap shrinks by the same factor, $\frac{5}{7}$, every 10 minutes. The cooling is fastest at the start: the slope at $t = 0$ is $-70k = -2.36^\circ\text{C}$ per minute, and at $t = 37.2$ it is $-20k = -0.67$. The figure shows the curve with the three points.

![Left, the temperature of the coffee falling from 90 degrees Celsius toward the room temperature of 20 degrees, a curve that bends and flattens; the points (0, 90), (10, 70) and (37.2, 40) are marked. Right, a price that starts at 25 falls toward the equilibrium of 15 and a price that starts at 5 rises toward 15, both flattening out as they approach the dashed line.](../../assets/figures/05-university-core/first-order-differential-equations-cooling-price.svg)

</div>

<div class="example" markdown>

### Example 4: a logistic model of an app's users

In a hypothetical model, the number of users $P$ of an app follows $P' = 0.5P\left(1 - \frac{P}{10^6}\right)$ per month, starting from $P_0 = 1000$. Find $P(t)$, when the app reaches half its capacity, and the fastest growth.

Here $K = 10^6$, $r = 0.5$ and $A = \frac{10^6 - 1000}{1000} = 999$, so $P(t) = \frac{10^6}{1 + 999e^{-0.5t}}$. Half capacity is $P = 500{,}000$, where $999e^{-0.5t} = 1$, so $t = \frac{\ln 999}{0.5} \approx 13.81$ months. At that moment the growth is fastest, $\frac{rK}{4} = 125{,}000$ users a month.

Check: $P(0) = \frac{10^6}{1 + 999} = 1000$. At $t = 6$, $P = \frac{10^6}{1 + 999e^{-3}} = \frac{10^6}{50.74} \approx 19{,}709$, and the equation then gives a growth of $0.5 \cdot 19{,}709\left(1 - 0.0197\right) \approx 9{,}660$ users a month. Early on, $P' \approx 0.5P$, so the growth looks exponential, with a doubling time of $\frac{\ln 2}{0.5} = 1.39$ months. The numerical Euler run below gives $19{,}695$ for $P(6)$, close to the exact value.

</div>

<div class="example" markdown>

### Example 5: a linear equation, and savings with deposits

(a) Solve $y' + 2y = 6$ with $y(0) = 0$. (b) An account earns 4% compounded continuously and receives deposits at a steady \$6,000 a year, so $A' = 0.04A + 6000$. Starting from $A(0) = 0$, how much is there after 10 years?

(a) Here $p = 2$ and $q = 6$, so the integrating factor is $e^{2t}$. Then $(e^{2t}y)' = 6e^{2t}$, so $e^{2t}y = 3e^{2t} + C$ and $y = 3 + Ce^{-2t}$. The condition $y(0) = 0$ gives $C = -3$, so $y = 3(1 - e^{-2t})$, which approaches the equilibrium $3 = \frac{q}{p}$.

(b) Write it as $A' - 0.04A = 6000$, so $p = -0.04$ and the integrating factor is $e^{-0.04t}$. Then $(e^{-0.04t}A)' = 6000e^{-0.04t}$, so $e^{-0.04t}A = -150{,}000e^{-0.04t} + C$ and $A = -150{,}000 + Ce^{0.04t}$. The condition $A(0) = 0$ gives $C = 150{,}000$, so

$$
A(t) = 150{,}000\left(e^{0.04t} - 1\right).
$$

At $t = 10$, $A = 150{,}000(e^{0.4} - 1) \approx \$73{,}773.70$. The deposits alone total \$60,000, so the interest is about \$13,774.

Check: (a) $y' = 6e^{-2t}$ and $2y = 6 - 6e^{-2t}$, which add to 6. (b) $A' = 6000e^{0.04t}$ and $0.04A + 6000 = 6000(e^{0.04t} - 1) + 6000 = 6000e^{0.04t}$. Annual deposits with annual compounding would be the geometric series of annuities and geometric series<!-- link: ../../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md -->, and continuous deposits are its limit.

</div>

<div class="example" markdown>

### Example 6: Euler's method by hand

Use Euler's method to estimate $y(1)$ for $y' = t - y$, $y(0) = 1$, with $h = 0.5$ and with $h = 0.25$. The exact solution is $y = t - 1 + 2e^{-t}$.

With $h = 0.5$: $y_1 = 1 + 0.5(0 - 1) = 0.5$ at $t = 0.5$, then $y_2 = 0.5 + 0.5(0.5 - 0.5) = 0.5$ at $t = 1$. With $h = 0.25$: the values at $t = 0.25, 0.5, 0.75, 1$ are

$$
y_1 = 1 + 0.25(0 - 1) = 0.75, \quad y_2 = 0.75 + 0.25(0.25 - 0.75) = 0.625,
$$

$$
y_3 = 0.625 + 0.25(0.5 - 0.625) = 0.59375, \quad y_4 = 0.59375 + 0.25(0.75 - 0.59375) = 0.6328.
$$

The exact value is $y(1) = 2e^{-1} \approx 0.7358$. The errors are $0.236$ for $h = 0.5$ and $0.103$ for $h = 0.25$.

Check: the error went down by a factor of $2.3$ when the step was halved, a little more than the factor $2$ of a first-order method, and it keeps tending to $2$ for smaller steps. Also, $y = t - 1 + 2e^{-t}$ satisfies $y' = 1 - 2e^{-t} = t - y$ and $y(0) = 0 + 2 - 1 = 1$.

</div>

<div class="example" markdown>

### Example 7: a cold drink (finish it yourself)

A drink at $5^\circ\text{C}$ is left in a room at $25^\circ\text{C}$, with $T' = -0.05(T - 25)$. Find $T(t)$, the temperature after 20 minutes, and the time to reach $20^\circ\text{C}$.

The room temperature is $T_r = 25$, so $u = T - 25$ obeys $u' = -0.05u$ with $u(0) = -20$. So $T(t) = 25 - 20e^{-0.05t}$.

<details class="solution" markdown>
<summary>Finish</summary>

At $t = 20$: $T = 25 - 20e^{-1} \approx 25 - 7.36 = 17.64^\circ\text{C}$. The drink reaches $20^\circ\text{C}$ when $20e^{-0.05t} = 5$, so $e^{-0.05t} = \frac{1}{4}$ and $t = \frac{\ln 4}{0.05} \approx 27.73$ minutes.

Check: $T' = 20 \cdot 0.05e^{-0.05t} = e^{-0.05t}$, and $-0.05(T - 25) = -0.05(-20e^{-0.05t}) = e^{-0.05t}$. Also $T(0) = 25 - 20 = 5$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: forgetting the constant. After integrating, the constant $C$ gives a whole family of solutions, and an initial condition picks one. Writing $y = e^{t}$ for $y' = y$ misses $y = 3e^{t}$, $y = -e^{t}$ and all the others.

</div>

<div class="warning" markdown>

Watch out: losing solutions when you divide. Separating $y' = y(1 - y)$ requires dividing by $y(1 - y)$, which is $0$ at the equilibria $y = 0$ and $y = 1$. These are solutions that the formula $y = \frac{1}{1 + Ae^{-t}}$ never gives for $y = 0$ (it would need $A$ infinite), and gives for $y = 1$ only if you allow $A = 0$, which the separation steps don't produce. List the equilibria before you separate.

</div>

<div class="warning" markdown>

Watch out: separating an equation that isn't separable. The equation $y' = t + y$ can't be written as a product of a function of $t$ and a function of $y$, so integrating "both sides" is wrong. It is linear: write it as $y' - y = t$ and use the integrating factor $e^{-t}$.

</div>

<div class="warning" markdown>

Watch out: signs in the exponent. For $y' = -ky$ with $k > 0$ the solution is $e^{-kt}$ and decays. In cooling, $T' = -k(T - T_r)$, the sign makes the gap shrink. If you write $T' = k(T - T_r)$ by mistake, the solution grows away from the room's temperature.

</div>

<div class="warning" markdown>

Watch out: a step size that is too large. Euler's method doesn't announce failure: the numbers just go wrong. For $y' = -10y$ the steps $h = 0.1$, $0.2$ and $0.25$ give factors $0$, $-1$ and $-1.5$ per step. Halve $h$ and see whether the answer changes much.

</div>

<div class="warning" markdown>

Watch out: believing a model beyond its range. The exponential model $P' = kP$ predicts unlimited growth, and the logistic model with a carrying capacity does better but still assumes a constant $K$ and $r$. A solution of a model is a statement about the model.

</div>

## Tricks and shortcuts

For $y' = k(y - c)$ (cooling, price adjustment, a balance with steady deposits), skip the work: $y = c + (y_0 - c)e^{kt}$. The equilibrium is $c$ and the gap from it grows or decays at rate $k$. Example 3 and the price model are of this kind.

The half-life or doubling time gives the rate without a calculator: $k = \frac{\ln 2}{t_{1/2}}$, and the fraction left after $n$ half-lives is $2^{-n}$. A growth rate of $x\%$ a year doubles in about $\frac{70}{x}$ years, since $\ln 2 \approx 0.69$: at 5% about $14$ years.

A fast check of the logistic curve: the S is symmetric about its midpoint $P = \frac{K}{2}$, which is reached at $t = \frac{\ln A}{r}$.

For a slope field by hand, compute the slope along the lines where it is constant (the isoclines, $f(t, y) = c$), and draw segments of slope $c$ along each.

## In code

Euler's method as a short function, tested against the exact answers of this lesson: $y' = y$, the cooling coffee, the logistic model and the Solow equation.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def euler(f, t0, y0, t_end, h):
    """Euler's method for y' = f(t, y): repeat y <- y + h f(t, y)."""
    n = round((t_end - t0) / h)
    t, y = t0, y0
    for _ in range(n):
        y += h * f(t, y)
        t += h
    return y

# y' = y, y(0) = 1: the exact value at t = 1 is e.
for h in (0.5, 0.1, 0.05, 0.01):
    y = euler(lambda t, y: y, 0, 1.0, 1, h)
    print(h, round(y, 4), round(math.e - y, 4))
# 0.5 2.25 0.4683
# 0.1 2.5937 0.1245
# 0.05 2.6533 0.065
# 0.01 2.7048 0.0135

# Newton cooling T' = -k (T - 20), T(0) = 90, T(10) = 70.
k = math.log(70 / 50) / 10
print(round(k, 5), round(math.log(70 / 20) / k, 2))
# 0.03365 37.23
print(round(euler(lambda t, T: -k * (T - 20), 0, 90.0, 10, 0.001), 3))
# 70.0

# Logistic growth: P' = 0.5 P (1 - P / 1e6), P(0) = 1000, exact solution K / (1 + A e^(-r t)).
K, r, P0 = 1e6, 0.5, 1000
A = (K - P0) / P0
exact = lambda t: K / (1 + A * math.exp(-r * t))
print(round(exact(6)), round(math.log(A) / r, 2))
# 19709 13.81
print(round(euler(lambda t, P: r * P * (1 - P / K), 0, P0, 6, 0.001)))
# 19695

# Solow: k' = s k^0.3 - d k with s = 0.2, d = 0.05, starting from k = 1.
s, d, a = 0.2, 0.05, 0.3
print(round((s / d) ** (1 / (1 - a)), 3))
# 7.246
print(round(euler(lambda t, k: s * k**a - d * k, 0, 1.0, 20, 0.001), 3), round((4 - 3 * math.exp(-0.7)) ** (1 / 0.7), 3))
# 3.724 3.724
```

The error column for $y' = y$ is proportional to $h$, which is the first-order behaviour. The Euler estimates for the nonlinear models agree with the formulas to three or four digits at $h = 0.001$.

</details>

## FAQ

### Why does $y' = ky$ give an exponential?

Because the exponential is the function whose derivative is proportional to itself, and Theorem 1 shows it is the only one. A quantity that grows (or shrinks) by a fixed fraction of itself in each short interval, however short, is exponential. This is why compound growth, decay and cooling all look alike.

### What is the difference between continuous and yearly compounding?

Yearly compounding multiplies the balance by $1 + r$ each year, while continuous compounding multiplies it by $e^{r}$ each year. For $r = 0.05$ these are $1.05$ and $1.0513$. As the number of compounding periods per year grows, $\left(1 + \frac{r}{n}\right)^n \to e^r$, and the differential equation $A' = rA$ is the limit of "add a fraction of the balance in each tiny period".

### What if I can't solve the equation?

Most real equations have no formula for the solution. Then you use the slope field to see the shape, find equilibria and their stability by hand, and run a numerical method such as Euler's (or a better one from a library). The theorem on existence and uniqueness says that a solution exists even when you can't write it down.

### Why does uniqueness matter?

Because a model that allows two futures from the same present, as $y' = 3y^{2/3}$ does from $y = 0$, can't predict anything. A unique solution means that the present state determines the whole future of the model, which is why simulation works.

## Practice

### Warm-up

1\. Show that $y = Ce^{-3t} + 2$ solves $y' + 3y = 6$ for every constant $C$, and find $C$ so that $y(0) = 5$.

<details class="solution" markdown>
<summary>Solution</summary>

$y' = -3Ce^{-3t}$ and $3y = 3Ce^{-3t} + 6$, so $y' + 3y = 6$ for every $C$. The condition $y(0) = C + 2 = 5$ gives $C = 3$.

Check: $y = 3e^{-3t} + 2$ has $y(0) = 5$ and as $t \to \infty$ it tends to $2 = \frac{6}{3}$, the equilibrium of the equation.

</details>

2\. Solve $y' = 4x^3y$ with $y(0) = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

The equilibrium $y = 0$ doesn't meet the initial condition. Separating, $\frac{dy}{y} = 4x^3\,dx$, so $\ln\lvert y \rvert = x^4 + C$ and $y = Ae^{x^4}$. The condition gives $A = 1$, so $y = e^{x^4}$.

Check: $y' = 4x^3e^{x^4} = 4x^3y$ and $y(0) = e^0 = 1$.

</details>

3\. A hypothetical sample has a half-life of 8 days. Find the decay rate $k$, and the fraction left after 20 days.

<details class="solution" markdown>
<summary>Solution</summary>

$k = \frac{\ln 2}{8} \approx 0.08664$ per day. After 20 days, the fraction is $e^{-20k} = 2^{-20/8} = 2^{-2.5} \approx 0.1768$.

Check: after 16 days (two half-lives) the fraction is $\frac{1}{4}$ and after 24 days $\frac{1}{8}$, and $0.1768$ is between $0.25$ and $0.125$.

</details>

### Standard

4\. A town of 50,000 grows continuously at 2% a year. (a) Find $P(t)$ and the time to reach 75,000. (b) What is the equivalent yearly growth rate?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $P' = 0.02P$ gives $P(t) = 50{,}000e^{0.02t}$. It reaches $75{,}000$ when $e^{0.02t} = 1.5$, so $t = \frac{\ln 1.5}{0.02} \approx 20.27$ years. (b) In one year the population is multiplied by $e^{0.02} = 1.0202$, so the equivalent yearly rate is $2.02\%$.

Check: $50{,}000e^{0.02 \cdot 20.27} = 50{,}000e^{0.4055} = 50{,}000 \cdot 1.5 = 75{,}000$.

</details>

5\. Solve $y' + \frac{1}{x}y = 3x$ for $x > 0$ with $y(1) = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

Here $p = \frac{1}{x}$, so $P = \ln x$ and the integrating factor is $e^{\ln x} = x$. Then $(xy)' = 3x^2$, so $xy = x^3 + C$ and $y = x^2 + \frac{C}{x}$. The condition $y(1) = 1 + C = 1$ gives $C = 0$, so $y = x^2$.

Check: $y' = 2x$ and $\frac{y}{x} = x$, so $y' + \frac{y}{x} = 3x$. Also $y(1) = 1$.

</details>

6\. A fish population in a lake follows $N' = 0.4N\left(1 - \frac{N}{500}\right)$ (hypothetical numbers). (a) Find the equilibria and say which is stable. (b) How fast is the population growing when $N = 100$, and what is the fastest growth? (c) Find $N(10)$ if $N(0) = 50$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $N' = 0$ at $N = 0$ and $N = 500$. The slope of $f(N) = 0.4N(1 - \frac{N}{500})$ is $f'(N) = 0.4 - \frac{0.8N}{500}$, which is $0.4 > 0$ at $0$ (unstable) and $-0.4 < 0$ at $500$ (stable).

(b) At $N = 100$, $N' = 0.4 \cdot 100 \cdot 0.8 = 32$ fish per unit time. The fastest growth is at $N = 250$: $\frac{rK}{4} = \frac{0.4 \cdot 500}{4} = 50$.

(c) With $K = 500$, $r = 0.4$ and $A = \frac{500 - 50}{50} = 9$, $N(t) = \frac{500}{1 + 9e^{-0.4t}}$, so $N(10) = \frac{500}{1 + 9e^{-4}} = \frac{500}{1.1648} \approx 429.2$.

Check: $N(0) = \frac{500}{10} = 50$, and $429.2$ is below the capacity $500$ and above the midpoint $250$, which the population passes at $t = \frac{\ln 9}{0.4} \approx 5.5$.

</details>

### Challenge

7\. Apply Euler's method to $y' = -10y$, $y(0) = 1$, with steps $h = 0.1$, $0.2$ and $0.25$. For each, give the factor by which $y$ is multiplied at every step and describe what happens. For which $h$ does the method decay like the true solution? Connect this to gradient descent on $f(y) = 5y^2$.

<details class="solution" markdown>
<summary>Solution</summary>

Euler's method gives $y_{n+1} = y_n + h(-10y_n) = (1 - 10h)y_n$. For $h = 0.1$ the factor is $0$, so $y_1 = 0$ and it stays there, much faster than the true solution $e^{-10t}$ (which is $0.37$ at $t = 0.1$). For $h = 0.2$ the factor is $-1$, so $y$ alternates between $1$ and $-1$ forever, and for $h = 0.25$ the factor is $-1.5$, so $\lvert y \rvert$ grows by half at each step. The method decays only if $\lvert 1 - 10h \rvert < 1$, that is $0 < h < 0.2$.

For $f(y) = 5y^2$ we have $f'(y) = 10y$, and gradient descent $y \leftarrow y - \eta f'(y)$ is the same recursion with $\eta = h$. The limit $\eta < \frac{2}{f''} = \frac{2}{10} = 0.2$ is the rule from the optimization lesson.

Check: with $h = 0.01$ the factor is $0.9$ and $y_{10} = 0.9^{10} = 0.349$, close to the exact $e^{-1} = 0.368$ at $t = 0.1$.

</details>

8\. (Reviews [u-substitution](../04-integrals/03-u-substitution.md).) Solve $\frac{dy}{dx} = \frac{x^2y}{1 + x^3}$ with $y(0) = 2$.

<details class="solution" markdown>
<summary>Solution</summary>

The equilibrium $y = 0$ doesn't meet the initial condition. Separating, $\frac{dy}{y} = \frac{x^2}{1 + x^3}\,dx$. With $u = 1 + x^3$, $du = 3x^2\,dx$, the right side integrates to $\frac{1}{3}\ln\lvert 1 + x^3 \rvert$, so $\ln y = \frac{1}{3}\ln(1 + x^3) + C$ and $y = A(1 + x^3)^{1/3}$ for $x > -1$. The condition $y(0) = A = 2$ gives $y = 2(1 + x^3)^{1/3}$.

Check: $y' = 2 \cdot \frac{1}{3}(1 + x^3)^{-2/3} \cdot 3x^2 = 2x^2(1 + x^3)^{-2/3}$, and $\frac{x^2y}{1 + x^3} = \frac{2x^2(1 + x^3)^{1/3}}{1 + x^3} = 2x^2(1 + x^3)^{-2/3}$.

</details>

## Where this shows up

- The next lesson, [second-order linear equations](02-second-order-linear-equations.md), handles equations with $y''$, where the exponential $e^{rt}$ of Theorem 1 is tried as a solution. The same methods, with a vector $\mathbf{y}$ and a matrix, solve systems of equations. [Recurrences](../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md) are the discrete counterpart of differential equations: $a_{n+1} = ra_n$ plays the role of $y' = ky$.
- In CS, simulation of physical systems, games and animation run numerical methods like Euler's, and the learning-rate limit of gradient descent is the stability limit of Euler's method. Queues, caches and epidemics are modelled by logistic and exponential equations.
- In economics, continuous-time models of growth (Solow), price adjustment, debt and savings are first-order equations. [Present value, NPV and bond prices](../../07-economics-math/04-more-tools/01-present-value-npv-and-bond-prices.md) discounts with $e^{-rt}$, and [multipliers and the AD-AS model](../../07-economics-math/04-more-tools/02-multipliers-and-the-ad-as-model.md) studies how an economy adjusts toward equilibrium.
