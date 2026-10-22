# Markets

The algebra behind introductory microeconomics: opportunity cost, gains from trade, supply and demand, surplus, taxes and price controls, and elasticity.

1. [Opportunity cost and the PPC](01-opportunity-cost-and-the-ppc.md)
2. [Comparative advantage and gains from trade](02-comparative-advantage-and-gains-from-trade.md)
3. [Supply and demand equilibrium algebra](03-supply-and-demand-equilibrium-algebra.md)
4. [Surplus and market interventions](04-surplus-and-market-interventions.md)
5. [Elasticity](05-elasticity.md)

## Cheat sheet

### Opportunity cost and the PPC

The opportunity cost of one more unit of $X$ is the units of $Y$ given up per unit of $X$ gained. It is a ratio in the other good, not in dollars. The slope of a PPC is minus the opportunity cost of the horizontal good.

| Situation | Opportunity cost of $x$ | Example |
|---|---|---|
| straight PPC, intercepts $X_{\max}$ and $Y_{\max}$ | $\frac{Y_{\max}}{X_{\max}}$, constant | 120 loaves or 240 buns: a loaf costs 2 buns |
| curved PPC $y = f(x)$ | $-f'(x)$ | $w^2 + c^2 = 100$: wheat costs $\frac{w}{c}$ canola |
| hours table | $\frac{\text{hours per } x}{\text{hours per } y}$ | $\frac{1/15}{1/30} = 2$ |

- The cost of $y$ is the reciprocal of the cost of $x$ on a straight PPC.
- Bowed outward means $f'' < 0$, which means the cost rises as you make more of $x$.
- A point is efficient on the curve, inefficient inside it and unattainable outside it. For $g(x, y) \le 0$, substitute and compare with 0.
- Growth moves the curve out. Better technology for one good pivots it about the other intercept.

Main mistakes:

- Flipping the ratio: the slope $-2$ is the cost of a loaf in buns, and a bun costs $\frac{1}{2}$ loaf.
- Counting only money, or counting a cost you pay either way.
- Calling every point on the curve the best one. Efficient does not mean preferred.
- Treating a move along the curve as growth.

### Comparative advantage and gains from trade

Absolute advantage means more output per input. Comparative advantage means a lower opportunity cost. A producer can have the first in both goods, never the second.

| Table | Opportunity cost of $X$ in $Y$ |
|---|---|
| output table | $\frac{\text{output of } Y}{\text{output of } X}$ |
| input table (hours per unit) | $\frac{\text{input per } X}{\text{input per } Y}$ |

- With costs $a < b$ for $X$, a price $p$ (units of $Y$ per unit of $X$) helps both sides exactly when $a < p < b$. The gain per unit traded is $b - a$, shared by the price: the seller gets $p - a$ and the buyer $b - p$.
- To compute gains: find comparative advantages, specialize, pick a price in range, then compare each final bundle with the no-trade bundle, good by good. The bundles must add to what was made.
- Quick test for $X$: compare $\frac{\text{output of } X}{\text{output of } Y}$, and the larger ratio wins.
- Equal opportunity costs mean no gains. Advantage depends on the partner.

Main mistakes:

- Reading "needs fewer hours" as comparative advantage. That is absolute advantage.
- Inverting the fraction from an input table.
- Quoting the price in the wrong direction (bolts per bushel against bushels per bolt).
- Thinking a price at an end of the range helps both sides.

### Supply and demand equilibrium algebra

With $Q_d = d_0 - d_1P$ and $Q_s = s_0 + s_1P$ (both slopes positive in this form):

$$
P^* = \frac{d_0 - s_0}{d_1 + s_1}, \qquad Q^* = \frac{d_0 s_1 + d_1 s_0}{d_1 + s_1}.
$$

| Change | Effect on $P^*$ | Effect on $Q^*$ |
|---|---|---|
| demand up by $\Delta d_0$ | $+\frac{\Delta d_0}{d_1 + s_1}$ | $+\frac{s_1 \Delta d_0}{d_1 + s_1}$ |
| supply up by $\Delta s_0$ | $-\frac{\Delta s_0}{d_1 + s_1}$ | $+\frac{d_1 \Delta s_0}{d_1 + s_1}$ |
| both up | direction unclear | up |

- Inverse forms: $P = \frac{d_0 - Q}{d_1}$ and $P = \frac{Q - s_0}{s_1}$. The drawn slopes are $-\frac{1}{d_1}$ and $\frac{1}{s_1}$.
- A change in the good's own price moves you along a curve. Anything else (income, related prices, tastes, costs, technology) shifts it.
- Above $P^*$ there is a surplus of goods and below it a shortage. $Q_d - Q_s = (d_0 - s_0) - (d_1 + s_1)P$.
- Market demand adds quantities at each price (horizontally). Each buyer is $\max(0, a_i - b_iP)$, and the sum has a kink where a buyer drops out. After solving, check that the price lies in the region you used.
- A negative $P^*$ (when $d_0 < s_0$) means no trade at a positive price.

Main mistakes:

- Confusing "demand falls" with "quantity demanded falls".
- Reading the drawn slope as $d_1$.
- Adding demands vertically.
- Using a region's formula at a price outside that region.

### Surplus and market interventions

For straight lines, $\text{CS} = \frac{1}{2}Q(P_d(0) - P)$ and $\text{PS} = \frac{1}{2}Q(P - P_s(0))$. For curves, $\text{CS} = \int_0^Q (P_d - P)\,dx$ and $\text{PS} = \int_0^Q (P - P_s)\,dx$ ([applications of integrals](../../05-university-core/04-integrals/06-applications-of-integrals.md#definitions)). Total surplus is largest at the equilibrium quantity.

| Intervention | Binding when | Quantity traded |
|---|---|---|
| price ceiling | below $P^*$ | $\min(Q_d, Q_s) = Q_s$, with a shortage |
| price floor | above $P^*$ | $\min(Q_d, Q_s) = Q_d$, with unsold goods |
| per-unit tax $t$ | always | where $Q_d(P_b) = Q_s(P_b - t)$ |

- For a tax, $P_b - P_k = t$. Buyers' share is $\frac{s_1}{d_1 + s_1}$, sellers' share is $\frac{d_1}{d_1 + s_1}$, whoever the law taxes.
- Revenue is $tQ$ (units sold after the tax). Deadweight loss is $\frac{1}{2}t(Q^* - Q) = \frac{d_1 s_1}{2(d_1 + s_1)}t^2$. A subsidy is a negative tax.
- Revenue $t(Q^* - kt)$, with $k = \frac{d_1 s_1}{d_1 + s_1}$, peaks at $t = \frac{Q^*}{2k}$ and is zero at $t = \frac{Q^*}{k}$.
- Check: $\text{CS} + \text{PS} + \text{revenue} + \text{DWL}$ equals the surplus before.

Main mistakes:

- Computing the effect of a non-binding control.
- Using $Q^*$ in the revenue instead of the smaller quantity.
- Thinking that the person the law taxes bears all of it.
- Forgetting that surplus under a ceiling or floor assumes the best allocation.

### Elasticity

$$
E = \frac{dQ}{dP}\cdot\frac{P}{Q}, \qquad E_{\text{arc}} = \frac{(Q_2 - Q_1)/\bar{Q}}{(P_2 - P_1)/\bar{P}}, \qquad \bar{Q} = \frac{Q_1 + Q_2}{2}, \ \bar{P} = \frac{P_1 + P_2}{2}.
$$

| $\lvert E \rvert$ | Name | Price rise makes revenue |
|---|---|---|
| above 1 | elastic | fall |
| equal to 1 | unit elastic | stay the same (a peak) |
| below 1 | inelastic | rise |

- On $Q = d_0 - d_1P$, $E = -\frac{d_1P}{d_0 - d_1P}$, and $\lvert E \rvert = \frac{Q_{\max} - Q}{Q}$. It is 1 at $P = \frac{d_0}{2d_1}$, elastic above and inelastic below.
- $\frac{dR}{dP} = Q(1 + E)$ and $\text{MR} = P\left(1 + \frac{1}{E}\right)$, so $\text{MR} > 0$ exactly when demand is elastic.
- $Q = AP^{-\eta}$ has $E = -\eta$ everywhere and revenue $AP^{1-\eta}$. Its log-log graph is a line of slope $-\eta$.
- Income elasticity: positive means normal ($> 1$ luxury, between 0 and 1 necessity), negative means inferior. Cross-price: positive means substitutes, negative means complements. Supply: $E_s \ge 0$, and $E_s = 1$ for a line through the origin.
- Buyers' share of a tax is $\frac{E_s}{E_s + \lvert E_d \rvert}$.

Main mistakes:

- Treating elasticity as slope.
- Using the start of the move as the base for the percent changes.
- Saying a price rise always lowers revenue.
- Comparing $E = -2$ with 1 and calling it inelastic.
