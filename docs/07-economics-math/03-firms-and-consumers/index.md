# Firms and consumers

The calculus of micro: marginal analysis, production and cost, profit maximization in competition, monopoly and duopoly, and the consumer's utility problem with Lagrange multipliers.

1. [Marginal analysis with derivatives](01-marginal-analysis-with-derivatives.md)
2. [Production and cost functions](02-production-and-cost-functions.md)
3. [Profit maximization and market structure](03-profit-maximization-and-market-structure.md)
4. [Utility and indifference curves](04-utility-and-indifference-curves.md)
5. [Lagrange multipliers, utility and cost minimization](05-lagrange-multipliers-utility-and-cost-minimization.md)

## Cheat sheet

### Marginal analysis with derivatives

The marginal cost is $MC = C'(q)$, the slope of the cost curve. The real cost of the $n$-th unit is $C(n) - C(n-1)$, which for a quadratic cost equals $C'\left(n - \frac{1}{2}\right)$.

| Idea | Formula | Example |
|---|---|---|
| Best quantity | $MB = MC$, with $B'' < C''$ | $\frac{600}{1 + h} = 40$ gives $h = 14$ |
| Average against marginal | $a' = \frac{T' - a}{q}$; at a flat point $a'' = \frac{T''}{q}$ | $AC$ is lowest where $MC = AC$ and $MC$ is rising |
| Marginal revenue | $MR = p + q\,p'$ | $p = a - bq$ gives $MR = a - 2bq$ |
| Elasticity form | $MR = p\left(1 + \frac{1}{E}\right)$ | $p = 40$, $E = -2$ gives $MR = 20$ |

- Fixed and sunk costs drop out of every margin.
- $MR > 0$ when demand is elastic ($E < -1$), $MR = 0$ at $E = -1$, and $MR < 0$ when it is inelastic.
- For linear demand, $MR$ has the same intercept and twice the slope, and the point of unit elasticity is the midpoint of the demand line.

Main mistakes:

- Treating average cost as the cost of the next unit.
- Setting $MR = p$ for a seller whose price falls as it sells more. That holds only for a price taker.
- Stopping at $MB = MC$ without checking that marginal cost is rising there.
- Using $C'(n)$ for the $n$-th unit when units are large.
- Dropping the sign of $E$: use $1 + \frac{1}{E}$ with $E < 0$, or $1 - \frac{1}{\lvert E \rvert}$.

### Production and cost functions

| Term | Definition | Cobb-Douglas $Q = AK^aL^b$ |
|---|---|---|
| marginal product | $MP_L = \frac{\partial Q}{\partial L}$ | $MP_L = b\frac{Q}{L}$, $MP_K = a\frac{Q}{K}$ |
| average product | $AP_L = \frac{Q}{L}$ | $MP$ cuts $AP$ at the peak of $AP$ |
| MRTS | $\frac{MP_L}{MP_K} = -\frac{dK}{dL}$ | $\frac{b}{a}\frac{K}{L}$, falling along an isoquant |
| returns to scale | $f(sK, sL)$ against $s\,f(K, L)$ | $s^{a+b}$: increasing if $a + b > 1$, decreasing if below |

- From a short-run production function: $MC = \frac{w}{MP_L}$ and $AVC = \frac{w}{AP_L}$. $MC$ is lowest where $MP$ is highest, and $MC = AVC$ at the minimum of $AVC$.
- $AC = AFC + AVC$, and the minimum of $AC$ is to the right of the minimum of $AVC$.
- Long run: choose inputs with $MRTS = \frac{w}{r}$. Short-run cost is at least long-run cost, with equality where the fixed input is the best one.
- If $f(tK, tL) = t^\gamma f(K, L)$ then $C(Q) = C(1)Q^{1/\gamma}$, so average cost falls if $\gamma > 1$, is flat if $\gamma = 1$ and rises if $\gamma < 1$.

Main mistakes:

- Mixing up diminishing marginal returns (one input) with decreasing returns to scale (all inputs).
- Reading $MP$ as $AP$.
- Putting the fixed cost into $MC$.
- Inverting the MRTS, or forgetting which input is on which axis.
- Assuming $a + b = 1$.

### Profit maximization and market structure

| Market | Condition | Rule |
|---|---|---|
| price taker | $p = MC$, with $MC' > 0$ | supply is $MC$ above the minimum of $AVC$ |
| shutdown | $p < AVC$ | produce nothing and lose only $FC$ |
| long run, competitive | free entry | $p = AC_{\min}$, zero profit, $n = \frac{Q_D}{q}$ |
| monopoly | $MR = MC$ | $\frac{p - MC}{p} = \frac{1}{\lvert E \rvert}$, with $\lvert E \rvert > 1$ |
| Cournot duopoly | best responses | $q_i = \frac{a - c}{3b}$, $P = \frac{a + 2c}{3}$ |

- Deadweight loss of a monopoly: the area between demand and $MC$ from the monopoly quantity to the competitive quantity. For linear demand and constant $MC$ it is $\frac{(a - c)^2}{8b}$, half of the profit $\frac{(a - c)^2}{4b}$.
- Linear demand and constant $MC$: monopoly sells half the competitive quantity, at price $\frac{a + c}{2}$.
- With $n$ Cournot firms, each makes $\frac{a - c}{(n + 1)b}$.

Main mistakes:

- Setting $p = MC$ for a monopolist.
- Using $AC$ in the shutdown rule.
- Taking the first root of $p = MC$ when marginal cost is U-shaped.
- Taking the deadweight loss against $MR$ instead of $MC$.
- Substituting $q_2 = q_1$ before differentiating in Cournot.

### Utility and indifference curves

| Idea | Formula |
|---|---|
| Ordinal utility | $g(U)$ with $g$ increasing represents the same preferences |
| MRS | $-\frac{dy}{dx} = \frac{U_x}{U_y}$, unchanged by relabelling |
| Cobb-Douglas $U = x^ay^b$ | $MRS = \frac{a}{b}\frac{y}{x}$, curves are convex |
| Budget line | $p_xx + p_yy = m$, slope $-\frac{p_x}{p_y}$, intercepts $\frac{m}{p_x}$ and $\frac{m}{p_y}$ |
| Interior optimum | $MRS = \frac{p_x}{p_y}$ and the budget |
| Perfect substitutes $ax + by$ | all of the good with more utility per dollar; any bundle if tied |
| Perfect complements $\min(x, y)$ | $x = y = \frac{m}{p_x + p_y}$, at the kink |

- Compare utility per dollar: $\frac{U_x}{p_x}$ against $\frac{U_y}{p_y}$.
- Diminishing MRS is not the same as diminishing marginal utility.

Main mistakes:

- Reading utility numbers as amounts of happiness.
- Inverting the MRS or the price ratio.
- Using the tangency at a corner or a kink.
- Trusting a tangency when preferences aren't convex.

### Lagrange multipliers, utility and cost minimization

| Result | Formula |
|---|---|
| Cobb-Douglas demand | $x = \frac{a}{a + b}\frac{m}{p_x}$, $y = \frac{b}{a + b}\frac{m}{p_y}$ |
| Multiplier | $\lambda = \frac{(a + b)U}{m} = \frac{U_x}{p_x}$, the marginal utility of income |
| Envelope theorem | $\frac{dV}{d\theta} = \frac{\partial\mathcal{L}}{\partial\theta}$: $\frac{\partial V}{\partial m} = \lambda$, $\frac{\partial V}{\partial p_x} = -\lambda x$ |
| Hicksian demand | $h_x = \bar{u}^{\frac{1}{a+b}}\left(\frac{a\,p_y}{b\,p_x}\right)^{\frac{b}{a+b}}$ |
| Duality | $e\bigl(p, V(p, m)\bigr) = m$ |
| Firm: conditional demands | $K = Q^{\frac{1}{\alpha+\beta}}\left(\frac{\alpha w}{\beta r}\right)^{\frac{\beta}{\alpha+\beta}}$, and $\lambda$ is the marginal cost |
| Slutsky | $\frac{\partial x}{\partial p_x} = \frac{\partial h_x}{\partial p_x} - x\frac{\partial x}{\partial m}$ |

- Substitution effect: $h_x(p^{new}, u_0) - x_0$. Income effect: $x_1 - h_x$. With $U = \sqrt{xy}$, $m = 100$ and $p_x$ from 1 to 4, the effects are $-25$ and $-12.5$.
- The multiplier depends on how utility is labelled, and demand doesn't.
- Check the answer: if a quantity is negative, the best bundle is a corner.

Main mistakes:

- Reading $\lambda$ as an observable number.
- Skipping the sign check on the solution.
- Using the share $a$ when $a + b \ne 1$: the share is $\frac{a}{a + b}$.
- Mixing up Marshallian and Hicksian demand.
- Flipping the constraint's sign and then the sign of the multiplier.
