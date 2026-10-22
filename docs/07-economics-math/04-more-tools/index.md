# More tools

Four tools economists use after the basics: discounting and bond prices, spending multipliers and the AD-AS picture, regression and the problem of causation, and games and Nash equilibrium.

1. [Present value, NPV and bond prices](01-present-value-npv-and-bond-prices.md)
2. [Multipliers and the AD-AS model](02-multipliers-and-the-ad-as-model.md)
3. [Regression and econometrics intuition](03-regression-and-econometrics-intuition.md)
4. [Game theory and Nash equilibrium](04-game-theory-and-nash-equilibrium.md)

## Cheat sheet

### Present value, NPV and bond prices

Discounting converts future money into today's money at the discount rate $r$. A payment $C$ received $t$ periods from now is worth $\frac{C}{(1 + r)^t}$ today.

| Quantity | Formula | Example |
|---|---|---|
| present value of one payment | $\frac{C}{(1 + r)^t}$ | \$1,000 in 3 years at 5% is \$863.84 |
| net present value | $\sum_{t=0}^{n} \frac{C_t}{(1 + r)^t}$ | cost \$50,000, NPV at 8% is \$4,018 |
| perpetuity | $\frac{C}{r}$ | \$100 a year at 5% is \$2,000 |
| growing perpetuity | $\frac{C}{r - g}$, for $g < r$ | \$100, growing 2%, at 7% is \$2,000 |
| bond price | $C\,\frac{1 - (1 + y)^{-n}}{y} + \frac{F}{(1 + y)^n}$ | 3-year, 4% coupon, face \$1,000, yield 5% is \$972.77 |

- The NPV rule: do a project if its NPV is positive, and take the highest NPV among projects that exclude each other.
- The IRR is the rate at which NPV is 0. With one outflow followed by inflows it is unique, and "IRR above the discount rate" agrees with the NPV rule. With several sign changes there can be several IRRs, or none.
- The perpetuity formulas are the infinite geometric series $\frac{a}{1 - q}$ with $a = \frac{C}{1 + r}$ and $q = \frac{1 + g}{1 + r}$.
- A bond's price falls when its yield rises, because each fixed payment is discounted more. The price equals the face value exactly when the yield equals the coupon rate, is below it when the yield is higher (a discount), and is above it when the yield is lower (a premium).
- Long bonds move more than short ones: for a 4% coupon and a yield rising from 4% to 5%, a 2-year bond loses 1.9%, a 10-year bond 7.7% and a 30-year bond 15.4%.
- The yield to maturity is the IRR of paying the price and receiving the payments. Find it by bisection, since price is strictly decreasing in the yield.
- Benchmark: the Bank of Canada's 5-year Government of Canada yield was 3.62% on October 20, 2026.

Main mistakes:

- Discounting nominal cash flows at a real rate, or the reverse.
- Forgetting that $\frac{C}{r}$ values the stream one period before the first payment.
- Using a monthly payment with an annual rate. Match the rate to the period.
- Choosing the project with the higher IRR instead of the higher NPV.

### Multipliers and the AD-AS model

In the Keynesian cross, equilibrium output is where planned spending equals output: $Y = C + I + G$, with consumption $C = a + bY$ and marginal propensity to consume $b$, where $0 \le b < 1$.

| Model | Equilibrium or multiplier | Example ($b = 0.8$) |
|---|---|---|
| basic | $Y^* = \frac{a + I + G}{1 - b}$ | multiplier 5 |
| lump-sum tax $T$ | $Y^* = \frac{a - bT + I + G}{1 - b}$ | tax multiplier $-4$ |
| balanced budget | $\Delta G = \Delta T$ gives $\Delta Y = \Delta G$ | multiplier 1 |
| tax rate $\tau$, imports $mY$ | multiplier $\frac{1}{1 - b(1 - \tau) + m}$ | $\tau = 0.25$, $m = 0.1$ gives 2 |

- Two derivations of the spending multiplier: algebra ($\Delta Y = \Delta G + b\,\Delta Y$) and the geometric series of rounds $\Delta G(1 + b + b^2 + \cdots) = \frac{\Delta G}{1 - b}$.
- The multiplier is $\frac{1}{\text{leakage rate}}$. Saving, taxes and imports are leakages.
- A tax change has a smaller effect than a spending change of the same size, by the factor $b$, because part of the tax change comes out of saving.
- AD-AS: the multiplier measures how far AD shifts at a given price level. In the short run the economy moves along the upward-sloping AS curve, so output rises less than the multiplier says and prices rise. In the long run, output returns to potential and only prices stay higher.
- The simple multiplier leaves out prices, interest rate responses, crowding out, expectations and spare capacity, so treat it as an upper bound.

Main mistakes:

- Using $\frac{1}{1 - b}$ for a tax change. It is $-\frac{b}{1 - b}$.
- Using the average share of income spent as $b$. The MPC is about the next dollar.
- Expecting the multiplier effect all at once. The rounds take time.
- Using the formula when $b \ge 1$, which has no equilibrium.

### Regression and econometrics intuition

The model $y = \beta_0 + \beta_1 x + u$ has coefficients $\beta_0, \beta_1$ and an error $u$. A coefficient is read ceteris paribus: other variables in the model held fixed. It is causal only if the error is unrelated to $x$.

| Model | Reading of the slope $b_1$ |
|---|---|
| level-level, $y$ on $x$ | $y$ changes by $b_1$ units per unit of $x$ |
| log-linear, $\ln y$ on $x$ | about $100\,b_1$ percent per unit of $x$; exactly $e^{b_1} - 1$ |
| log-log, $\ln y$ on $\ln x$ | elasticity: $b_1$ percent per 1% |
| level-log, $y$ on $\ln x$ | $\frac{b_1}{100}$ units per 1% |
| dummy variable | average difference between the group coded 1 and the group coded 0 |

- The log readings come from $d(\ln x) = \frac{dx}{x}$: in $\ln y = \beta_0 + \beta_1 \ln x$, the elasticity $\frac{dy}{dx}\cdot\frac{x}{y}$ is $\beta_1$.
- Omitted variable bias: leaving out $x_2$ gives a short slope $\tilde{b}_1 = b_1 + b_2\,\delta_1$, where $\delta_1$ is the slope of $x_2$ on $x_1$. The bias is $\beta_2\,\delta_1$.

| | $\delta_1 > 0$ | $\delta_1 < 0$ |
|---|---|---|
| $\beta_2 > 0$ | upward | downward |
| $\beta_2 < 0$ | downward | upward |

- Reading a table: coefficient, standard error, $t = \frac{b}{\text{SE}}$ (significant at 5% if $\lvert t \rvert$ is above about 2), a 95% interval $b \pm 1.96\,\text{SE}$, $R^2$ and $n$.
- Changing units rescales the coefficient and its standard error together, so $t$ and $R^2$ don't change.
- Randomisation, natural experiments and good controls are the ways to get close to causal effects.

Main mistakes:

- Reading a coefficient as a causal effect when a confounder is missing.
- Confusing statistical significance with importance. Read the size in the units of the problem.
- Using $100\,b_1$ for a large coefficient. Use $e^{b_1} - 1$.
- Including a dummy for every group along with the intercept (the dummy variable trap).
- Adding variables that are consequences of $x$, or choosing controls by $R^2$.

### Game theory and Nash equilibrium

A normal-form game has players, strategies and a payoff matrix with (row, column) payoffs in each cell. A Nash equilibrium is a combination of strategies in which each is a best response to the others.

1. Delete strictly dominated strategies, and repeat. This never removes a Nash equilibrium.
2. Star each player's best responses. A cell with two stars is a pure equilibrium.
3. For a 2 by 2 game with no pure equilibrium (or to find the mixed one), set each player's probability so that the other is indifferent between their two strategies.
4. Sequential game: start at the last move and work back (backward induction).

| Game | Equilibrium | Lesson |
|---|---|---|
| prisoner's dilemma (Example 1) | both choose the dominant strategy, and both are worse off | a shared gain is not an equilibrium |
| coordination (opera or football) | two pure, and a mixed one with $p = \frac{2}{3}$, $q = \frac{1}{3}$ | many equilibria, so one needs a way to pick |
| matching pennies | only mixed, with $p = q = \frac{1}{2}$ | being unpredictable |
| entry game | (Enter, Accommodate) | threats must be credible |

- Mixed strategy: you choose your probabilities to make the other player indifferent, and then every strategy in their mix pays the same.
- Cournot duopoly with $P = a - Q$ and cost $c$: best response $q_i = \frac{a - c - q_j}{2}$, equilibrium $q = \frac{a - c}{3}$ each. With $a = 100$ and $c = 10$ it is 30 each, price \$40 and profit \$900 each, against \$1,012.50 each at half the monopoly output, which each firm would cheat on.
- Repeated play: the grim trigger sustains cooperation when $\delta \ge \frac{\text{cheat} - \text{cooperate}}{\text{cheat} - \text{punish}}$, from a geometric series. For payoffs 130, 100 and 60 this is $\frac{3}{7}$.

Main mistakes:

- Calling an equilibrium efficient or fair. Equilibrium only says no one gains alone.
- Comparing the wrong pair of numbers when marking best responses. The row player compares down a column, the column player along a row.
- Equating your own payoffs instead of the opponent's when finding a mixed strategy.
- Treating an empty threat as part of the solution of a sequential game.
