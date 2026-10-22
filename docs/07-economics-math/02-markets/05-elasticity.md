# Elasticity

After this lesson you can compute the price elasticity of demand with the midpoint formula and with a derivative, classify demand as elastic, inelastic or unit elastic, prove how elasticity varies along a straight demand line, connect elasticity to revenue and marginal revenue, work with constant-elasticity demand, and use income, cross-price and supply elasticities, including to split a tax between buyers and sellers.

Before this: [supply and demand equilibrium algebra](03-supply-and-demand-equilibrium-algebra.md), [surplus and market interventions](04-surplus-and-market-interventions.md) and [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md). The derivative parts use [rates of change and marginal analysis](../../05-university-core/03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md#elasticity-and-revenue), which previews the main formula.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. When the price of a good rises from \$5 to \$6, the quantity demanded falls from 50 to 40. Use the midpoint formula to find the elasticity of demand.
2. Demand is $Q = 100 - 4P$. Find the point elasticity at $P = 10$, say whether demand is elastic or inelastic there, and say what a small price rise does to revenue.
3. Demand has constant elasticity $-2$. The price rises by 1%. About how does the quantity demanded change?

<details class="solution" markdown>
<summary>Answers</summary>

1. The change in quantity is $-10$ on the average quantity 45, which is $-22.2\%$. The change in price is $+1$ on the average price 5.5, which is $+18.2\%$. The elasticity is $\frac{-10/45}{1/5.5} = -\frac{11}{9} \approx -1.22$.
2. At $P = 10$ we have $Q = 60$, so $E = \frac{dQ}{dP}\cdot\frac{P}{Q} = -4 \cdot \frac{10}{60} = -\frac{2}{3}$. Since $\lvert E \rvert < 1$, demand is inelastic, and a small price rise raises revenue.
3. The quantity falls by about 2%, because elasticity is the percent change in quantity per 1% change in price.

</details>

## The idea

A price rise of \$1 is a big change for a \$2 coffee and a small change for a \$200 concert ticket, and a drop of 10 cups is a big change for a kiosk that sells 20 and a small one for a kiosk that sells 2,000. The slope $\frac{dQ}{dP}$ of a demand curve mixes these units together. It changes if you count in cups or in dozens, or in dollars or in cents. To compare how responsive buyers are for different goods, economists use percent changes, which have no units.

The price elasticity of demand is the percent change in quantity demanded per 1% change in price. If it is $-2$, a 1% rise in price cuts the quantity by about 2%. If it is $-0.3$, the same rise cuts the quantity by only about 0.3%. The first buyers are sensitive to price, and the second are not.

The number matters for a practical reason. A seller who raises the price earns more on each unit but sells fewer units. Which effect wins depends on the elasticity, and this gives the lesson's main result about revenue. The same number also decides who pays a tax, since the side that can walk away more easily bears less of it.

![Left: the demand line P = 6 minus Q over 20 with the absolute elasticity marked at five points: 5 at a price of 5 dollars, 2 at 4, 1 at 3, 0.5 at 2 and 0.2 at 1 dollar. The part above a price of 3 is red (elastic) and the part below is blue (inelastic). Right: revenue R = Q times (6 minus Q over 20) rises to a maximum of 180 at Q = 60, where the elasticity is 1 in absolute value, and falls after that.](../../assets/figures/07-economics-math/elasticity-linear.svg)

## Definitions

The **price elasticity of demand** is the ratio of the percent change in the quantity demanded to the percent change in the price:

$$
E_d = \frac{\%\Delta Q_d}{\%\Delta P}.
$$

In plain words, it says how many percent the quantity demanded changes for a 1% change in price. Because demand slopes down, $E_d$ is negative. Many books quote its absolute value $\lvert E_d \rvert$ and drop the sign, but this lesson keeps the sign in formulas and says "in absolute value" when it drops it.

For a demand function $Q = D(P)$ with a derivative, the **point elasticity** at a price $P$ is

$$
E = \frac{dQ}{dP}\cdot\frac{P}{Q}.
$$

In plain words, it is the slope of the demand curve times the ratio of price to quantity at that point: the limit of the percent change formula as the change shrinks to 0. (The percent change in $Q$ is $\frac{dQ}{Q}$ and in $P$ is $\frac{dP}{P}$, and their ratio is $\frac{dQ}{dP}\cdot\frac{P}{Q}$.)

For a move between two points $(P_1, Q_1)$ and $(P_2, Q_2)$, the **midpoint (arc) elasticity** measures each percent change against the average of the two endpoints:

$$
E_{\text{arc}} = \frac{(Q_2 - Q_1)\big/\tfrac{Q_1 + Q_2}{2}}{(P_2 - P_1)\big/\tfrac{P_1 + P_2}{2}}.
$$

In plain words, it is the percent change formula with the averages as the base, so it gives the same answer whichever point you start from.

Demand is **elastic** at a point if $\lvert E \rvert > 1$ (quantity responds by a larger percent than price), **inelastic** if $\lvert E \rvert < 1$, and **unit elastic** if $\lvert E \rvert = 1$. It is **perfectly inelastic** if $E = 0$ (a vertical demand curve: quantity doesn't respond) and **perfectly elastic** if $\lvert E \rvert$ is unbounded (a horizontal demand curve: any price above the going price loses every buyer).

The **total revenue** of a seller is $R = P \times Q$, and the **marginal revenue** is the extra revenue from selling one more unit, $\text{MR} = \frac{dR}{dQ}$ when the price is lowered as needed to sell it.

Three more elasticities use the same form. The **income elasticity of demand** is $E_I = \frac{dQ}{dI}\cdot\frac{I}{Q}$, where $I$ is income: a good is **normal** if $E_I > 0$ and **inferior** if $E_I < 0$, and a normal good is a **luxury** if $E_I > 1$ and a **necessity** if $0 < E_I < 1$. The **cross-price elasticity** of the demand for good $X$ with respect to the price $P_Y$ of good $Y$ is $E_{XY} = \frac{dQ_X}{dP_Y}\cdot\frac{P_Y}{Q_X}$: the goods are **substitutes** if it is positive and **complements** if it is negative. The **price elasticity of supply** is $E_s = \frac{dQ_s}{dP}\cdot\frac{P}{Q_s}$, which is positive for an upward-sloping supply.

## How to do it

### Computing an elasticity

1. Decide whether you have two points (use the midpoint formula) or a function and a price (use the derivative).
2. For two points, compute the change in $Q$ over the average $Q$, and the change in $P$ over the average $P$, and divide. Use the same direction for both changes.
3. For a function, differentiate $Q$ with respect to $P$, multiply by $\frac{P}{Q}$, and evaluate at the price.
4. Classify by $\lvert E \rvert$: above 1 is elastic, below 1 is inelastic.
5. Check the sign (negative for demand) and the size against the picture: a flat curve far from the axes is elastic.

### Elasticity along a straight demand line

*Theorem 1 (a straight demand line has different elasticities at different points).* For $Q = d_0 - d_1 P$ with $d_1 > 0$ and $0 < P < \frac{d_0}{d_1}$,

$$
E = -\frac{d_1 P}{d_0 - d_1 P}.
$$

In absolute value it increases from 0 (as $P \to 0$) without bound (as $P \to \frac{d_0}{d_1}$), and $\lvert E \rvert = 1$ exactly at the midpoint price $P = \frac{d_0}{2d_1}$. Demand is elastic above that price and inelastic below it.

What we know: the slope of the line is the constant $-d_1$, and $E = \frac{dQ}{dP}\cdot\frac{P}{Q}$. What we want: how $E$ depends on the point. The plan is to substitute and then compare $\lvert E \rvert$ with 1 by an inequality.

*Proof.* The derivative is $\frac{dQ}{dP} = -d_1$, so $E = -d_1 \cdot \frac{P}{d_0 - d_1 P}$. For $0 < P < \frac{d_0}{d_1}$ the denominator $d_0 - d_1 P$ is positive and shrinks as $P$ rises while the numerator $d_1 P$ grows, so $\lvert E \rvert = \frac{d_1 P}{d_0 - d_1 P}$ increases from 0 toward infinity. Also $\lvert E \rvert < 1$ exactly when $d_1 P < d_0 - d_1 P$, which is $2d_1 P < d_0$, that is, $P < \frac{d_0}{2d_1}$. The case $\lvert E \rvert > 1$ is the same with the inequality reversed, and equality gives $\lvert E \rvert = 1$. $\blacksquare$

Look back: the slope of a straight line is the same everywhere, yet the elasticity changes from point to point, because $\frac{P}{Q}$ changes: at a high price and a small quantity the ratio is large. A straight line is therefore not "constant elasticity". For the line in the figure ($Q = 120 - 20P$), $\lvert E \rvert = 1$ at $P = \frac{120}{40} = 3$. Another way to see the result is geometric: $\lvert E \rvert = \frac{Q_{\max} - Q}{Q}$, where $Q_{\max} = d_0$ is the quantity at price 0. At $Q = 20$ this is $\frac{100}{20} = 5$.

### Revenue and elasticity

*Theorem 2 (revenue and elasticity).* Let $Q = D(P)$ be differentiable with $Q > 0$. Then

$$
\frac{dR}{dP} = Q\,(1 + E), \qquad \text{so revenue rises with price when } E > -1 \text{ and falls when } E < -1.
$$

In terms of quantity, with the inverse demand $P(Q)$, the marginal revenue is $\text{MR} = P\left(1 + \frac{1}{E}\right)$, so it is positive when demand is elastic, zero when it is unit elastic, and negative when it is inelastic.

What we know: $R = P \cdot Q(P)$, and the product rule. What we want: the sign of the change in revenue. The plan is to differentiate and factor out $Q$.

*Proof.* By the product rule, $\frac{dR}{dP} = Q + P\frac{dQ}{dP} = Q\left(1 + \frac{dQ}{dP}\cdot\frac{P}{Q}\right) = Q(1 + E)$. Since $Q > 0$, the sign is the sign of $1 + E$, which is positive when $E > -1$ (inelastic) and negative when $E < -1$ (elastic). For the marginal revenue, write $R = P(Q) \cdot Q$ so that $\text{MR} = P + Q\frac{dP}{dQ} = P\left(1 + \frac{Q}{P}\cdot\frac{dP}{dQ}\right)$. The inverse function rule says $\frac{dP}{dQ} = \frac{1}{dQ/dP}$, so $\frac{Q}{P}\cdot\frac{dP}{dQ} = \frac{1}{E}$, and $\text{MR} = P\left(1 + \frac{1}{E}\right)$. This is positive when $\frac{1}{E} > -1$, that is, when $E < -1$ (elastic), since $E$ is negative. $\blacksquare$

Look back: raising the price has two effects, a gain of $Q\,dP$ on the units still sold and a loss of $P\,dQ$ from the units that are lost. The elasticity compares them: when the percent loss in quantity is smaller than the percent gain in price, the gain wins. For the straight line $Q = 120 - 20P$, revenue $R = 120P - 20P^2$ has $\frac{dR}{dP} = 120 - 40P$, which is 0 at $P = 3$ where $\lvert E \rvert = 1$, matching Theorem 1. In the figure, revenue peaks at $Q = 60$, $P = 3$, with $R = 180$.

### Constant elasticity

*Theorem 3 (constant-elasticity demand).* The demand function $Q = A P^{-\eta}$, with $A > 0$ and $\eta > 0$, has $E = -\eta$ at every price. Its revenue is $R = AP^{1-\eta}$, which falls with price if $\eta > 1$, is constant if $\eta = 1$ and rises with price if $\eta < 1$. Conversely, if $E = -\eta$ at every price then $Q = AP^{-\eta}$ for some $A$.

What we know: the power rule and the definition of $E$. What we want: the elasticity of this family and its revenue. The plan is to differentiate, simplify, and use the laws of exponents for the revenue.

*Proof.* The derivative is $\frac{dQ}{dP} = -\eta A P^{-\eta - 1}$, so $E = -\eta A P^{-\eta - 1}\cdot\frac{P}{AP^{-\eta}} = -\eta$. The revenue is $P \cdot AP^{-\eta} = AP^{1-\eta}$. If $\eta > 1$ the exponent is negative and $R$ falls as $P$ rises, if $\eta = 1$ then $R = A$ is constant, and if $\eta < 1$ the exponent is positive and $R$ rises. For the converse, $E = -\eta$ says $\frac{dQ}{Q} = -\eta\frac{dP}{P}$. Integrating both sides gives $\ln Q = -\eta\ln P + C$, so $Q = e^C P^{-\eta}$. $\blacksquare$

Look back: on a graph with both axes on log scales, $\ln Q = \ln A - \eta\ln P$ is a straight line of slope $-\eta$. This is why economists fit demand by regressing $\ln Q$ on $\ln P$ (see [regression and econometrics intuition](../04-more-tools/03-regression-and-econometrics-intuition.md)): the slope is the elasticity. A constant-elasticity curve never touches the axes, so it describes a range of prices and not all of them.

### Other elasticities and tax incidence

For supply, $E_s = \frac{dQ_s}{dP}\cdot\frac{P}{Q_s}$. For a line $Q_s = s_0 + s_1 P$ this is $\frac{s_1 P}{s_0 + s_1 P}$, which is 1 at every price if $s_0 = 0$ (a line through the origin), less than 1 if $s_0 > 0$ and more than 1 if $s_0 < 0$.

*Theorem 4 (tax incidence by elasticities).* In the linear market of the [previous lesson](04-surplus-and-market-interventions.md#a-per-unit-tax), evaluate the elasticities at the untaxed equilibrium $(P^*, Q^*)$. Then the share of a per-unit tax paid by buyers is $\frac{E_s}{E_s + \lvert E_d \rvert}$ and the share paid by sellers is $\frac{\lvert E_d \rvert}{E_s + \lvert E_d \rvert}$.

*Proof.* At equilibrium, $\lvert E_d \rvert = \frac{d_1 P^*}{Q^*}$ and $E_s = \frac{s_1 P^*}{Q^*}$. So $\frac{E_s}{E_s + \lvert E_d \rvert} = \frac{s_1 P^*/Q^*}{(s_1 + d_1)P^*/Q^*} = \frac{s_1}{d_1 + s_1}$, which is the buyers' share in Theorem 2 of the previous lesson. The sellers' share follows because the two shares add to 1. $\blacksquare$

Look back: the side with the smaller elasticity, the one less able to respond to a price change, bears more of the tax. For other shapes of curve the same formula is a good approximation for small taxes, because the curves are close to their tangent lines near the equilibrium.

## Worked examples

<div class="example" markdown>

### Example 1: midpoint against the endpoint

Demand is $Q = 120 - 20P$ (a made-up market for bubble tea). Find the elasticity when the price moves from \$3 to \$4, using the midpoint formula, and compare with the endpoint percent changes and the point elasticity at \$3.50.

Step 1: we have two points, $(3, 60)$ and $(4, 40)$, so use the midpoint formula.

Step 2: the change in quantity is $-20$ on the average quantity 50, which is $-40\%$. The change in price is $+1$ on the average price 3.5, which is $+28.57\%$. So

$$
E_{\text{arc}} = \frac{-20/50}{1/3.5} = -1.4.
$$

Step 3: $\lvert E \rvert = 1.4 > 1$, so demand is elastic over this range.

Now the endpoint versions. Starting at \$3 and going to \$4, the price rises by $\frac{1}{3} = 33.3\%$ and the quantity falls by $\frac{20}{60} = 33.3\%$, which gives $-1.0$. Starting at \$4 and going to \$3, the price falls by $\frac{1}{4} = 25\%$ and the quantity rises by $\frac{20}{40} = 50\%$, which gives $-2.0$. The same two points give $-1$ or $-2$ depending on the direction, and the midpoint formula gives one answer, $-1.4$.

The point elasticity at $P = 3.5$, where $Q = 50$, is $-20 \cdot \frac{3.5}{50} = -1.4$.

Check: the midpoint elasticity of a straight line equals the point elasticity at the midpoint, as Practice problem 7 proves. The revenue also agrees with elastic demand: raising the price from \$3 to \$4 changes revenue from $3 \cdot 60 = 180$ to $4 \cdot 40 = 160$, a fall.

</div>

<div class="example" markdown>

### Example 2: elasticity and revenue along a line

For $Q = 120 - 20P$, find the elasticity and the revenue at $P = 1, 2, 3, 4, 5$, and say where revenue is largest.

By Theorem 1, $E = -\frac{20P}{120 - 20P}$. Putting in each price:

| $P$ | $Q$ | $E$ | $\lvert E \rvert$ is | $R = PQ$ |
|---|---|---|---|---|
| \$1 | 100 | $-0.2$ | inelastic | \$100 |
| \$2 | 80 | $-0.5$ | inelastic | \$160 |
| \$3 | 60 | $-1$ | unit elastic | \$180 |
| \$4 | 40 | $-2$ | elastic | \$160 |
| \$5 | 20 | $-5$ | elastic | \$100 |

Revenue rises while demand is inelastic (price up from \$1 to \$3) and falls once it is elastic (from \$3 to \$5), with the maximum of \$180 at the unit-elastic price, \$3.

Check: Theorem 2 gives $\frac{dR}{dP} = Q(1 + E)$. At $P = 2$ this is $80 \cdot 0.5 = 40 > 0$ and at $P = 4$ it is $40 \cdot (1 - 2) = -40 < 0$. The direct derivative $120 - 40P$ gives $40$ and $-40$ as well.

</div>

<div class="example" markdown>

### Example 3: constant elasticity

Demand is $Q = 200P^{-2}$ (made up). Find the elasticity, and compare the effect of raising the price from \$5 by 1% and by 10%.

By Theorem 3, $E = -2$ at every price. At $P = 5$, $Q = \frac{200}{25} = 8$ and $R = 40$.

A 1% rise to \$5.05 gives $Q = \frac{200}{25.5025} = 7.8424$, a fall of 1.97%, close to the predicted 2%. A 10% rise to \$5.50 gives $Q = \frac{200}{30.25} = 6.6116$, a fall of 17.4%, not 20%: the elasticity is exact only for small changes. The revenue falls from \$40 to $5.5 \cdot 6.6116 = 36.36$, in line with $R = \frac{200}{P}$ and $\eta = 2 > 1$.

Check: $R = AP^{1-\eta} = 200P^{-1}$ gives $\frac{200}{5} = 40$ and $\frac{200}{5.5} = 36.36$. Doubling the price to \$10 halves the revenue to \$20.

</div>

<div class="example" markdown>

### Example 4: elasticities and a tax (finish it yourself)

Demand is $Q_d = 90 - 6P$ and supply is $Q_s = -10 + 4P$ (from the previous lesson, where the equilibrium was $P^* = 10$ and $Q^* = 30$). Find $E_d$ and $E_s$ at the equilibrium, then the share of a per-unit tax paid by buyers, and say how a price rise affects revenue.

Step 1: $E_d = \frac{dQ_d}{dP}\cdot\frac{P}{Q} = -6 \cdot \frac{10}{30}$.

Now compute $E_d$ and $E_s$, use Theorem 4, and compare with the share $\frac{s_1}{d_1 + s_1}$.

<details class="solution" markdown>
<summary>Finish</summary>

$E_d = -6 \cdot \frac{10}{30} = -2$ and $E_s = 4 \cdot \frac{10}{30} = \frac{4}{3}$. The buyers' share is $\frac{4/3}{4/3 + 2} = \frac{4/3}{10/3} = \frac{2}{5} = 0.4$, and the sellers' share is 0.6. Direct check: $\frac{s_1}{d_1 + s_1} = \frac{4}{10} = 0.4$.

Demand is elastic ($\lvert E_d \rvert = 2 > 1$), so a price rise would lower revenue: $\frac{dR}{dP} = Q(1 + E) = 30 \cdot (1 - 2) = -30$ per dollar.

Check: with a \$1 tax, $P_b = 10 + 0.4 = 10.4$, and buyers pay 40 cents of the dollar.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: elasticity is not the slope. A steeper demand curve is not always less elastic, and two curves with the same slope can have different elasticities at the same price. Along one straight line the slope is constant and the elasticity changes from 0 to unbounded (Theorem 1). Compare elasticities, not slopes.

</div>

<div class="warning" markdown>

Watch out: use the same base for both percent changes. The percent change from 3 to 4 is 33.3% and from 4 to 3 is $-25\%$, so using the start of the move gives different answers in each direction (Example 1). The midpoint formula uses the average as the base for both, so the answer doesn't depend on direction. For why the base matters, see [percent change and applications](../../02-middle-school/02-ratios-rates-percents/04-percent-change-and-applications.md).

</div>

<div class="warning" markdown>

Watch out: a price rise does not always lower revenue. It lowers revenue only when demand is elastic. If demand is inelastic, the quantity falls by a smaller percent than the price rises, and revenue goes up. Check the sign of $1 + E$.

</div>

<div class="warning" markdown>

Watch out for the sign. Demand elasticity is negative, and the rule is "elastic if $E < -1$", not "$E > 1$". If you compare $E = -2$ with 1 you will call elastic demand inelastic. Say "in absolute value" when you drop the sign.

</div>

A few edge cases. At a quantity of 0 (the choke price on a straight line) the elasticity is not defined, because $\frac{P}{Q}$ has a zero denominator, and it grows without bound as the price approaches that value. A vertical demand curve has $E = 0$ and a horizontal one has unbounded $\lvert E \rvert$. And because elasticity is local, for a large change you should use the midpoint formula over the whole range, or integrate.

## Tricks and shortcuts

On a straight demand line, $\lvert E \rvert = \frac{Q_{\max} - Q}{Q}$, the distance from the point to the quantity axis divided by the quantity. It is also $\frac{P}{P_{\max} - P}$, where $P_{\max}$ is the choke price. The midpoint of the line is unit elastic, the upper half is elastic and the lower half is inelastic. For $P_{\max} = 6$ and $P = 5$: $\frac{5}{6 - 5} = 5$.

The total-revenue test checks elasticity without a derivative: if a price rise raises revenue, demand is inelastic over that range, and if it lowers revenue, demand is elastic. In Example 2, revenue goes from \$160 to \$180 when the price goes from \$2 to \$3, so demand is inelastic over that stretch.

For constant elasticity, the percent change in quantity is about $E$ times the percent change in price for small changes, and the exact change is $\left(1 + \frac{\%\Delta P}{100}\right)^{-\eta} - 1$. For $\eta = 2$ and a 10% rise this is $1.1^{-2} - 1 = -17.4\%$.

## In code

The midpoint and point formulas are one line each. A derivative from a small step gives the point elasticity of any demand function, and a table checks Theorem 1 and Theorem 3.

<details class="code" markdown>
<summary>In code</summary>

```python
def arc_elasticity(p1, q1, p2, q2):
    """Midpoint (arc) elasticity between two points on a demand curve."""
    pct_q = (q2 - q1) / ((q1 + q2) / 2)
    pct_p = (p2 - p1) / ((p1 + p2) / 2)
    return pct_q / pct_p

def point_elasticity(demand, p, h=1e-6):
    """(dQ/dP) * (P/Q), with the derivative from a small step."""
    dq = (demand(p + h) - demand(p - h)) / (2 * h)
    return dq * p / demand(p)

linear = lambda p: 120 - 20 * p
print(round(arc_elasticity(3, 60, 4, 40), 4), round(point_elasticity(linear, 3.5), 4))
# -1.4 -1.4

for p in (1, 2, 3, 4, 5):
    q = linear(p)
    print(p, q, round(point_elasticity(linear, p), 2), p * q)
# 1 100 -0.2 100
# 2 80 -0.5 160
# 3 60 -1.0 180
# 4 40 -2.0 160
# 5 20 -5.0 100

constant = lambda p: 200 / p**2
print([round(point_elasticity(constant, p), 4) for p in (1, 5, 20)])
# [-2.0, -2.0, -2.0]
```

</details>

## FAQ

### Why use the midpoint formula?

Because the plain percent change depends on where you start. A move from 3 to 4 is a 33.3% rise, and the reverse move is a 25% fall, so the elasticity of the same pair of points changes with the direction. Using the average of the endpoints as the base for both percent changes removes the dependence.

### Why is demand for some goods inelastic?

Demand tends to be inelastic when there are no close substitutes, when the good is a small part of the budget, and when buyers have little time to adjust. These are tendencies, and each good needs its own data. The elasticity is estimated from data on prices and quantities, with the regression of $\ln Q$ on $\ln P$ as the simplest method.

### Is the unit-elastic point the best price for a seller?

It is the price that maximizes revenue on a straight line (Example 2). A seller who also has costs cares about profit, not revenue, and since selling more costs something, the profit-maximizing price is on the elastic part of the demand curve, where $\text{MR}$ is positive. Challenge problem 8 shows the rule for constant elasticity.

### Can elasticity be positive for demand?

For ordinary goods, no: a higher price lowers quantity demanded, so $E < 0$. The signs in the other elasticities carry meaning (positive cross-price for substitutes, negative income elasticity for inferior goods), but the own-price elasticity of demand is negative.

## Practice

### Warm-up

1\. The price of a good rises from \$5 to \$6 and the quantity demanded falls from 50 to 40. Find the midpoint elasticity and say whether demand is elastic.

<details class="solution" markdown>
<summary>Solution</summary>

The change in quantity is $-10$ on the average 45. The change in price is $+1$ on the average 5.5. So $E = \frac{-10/45}{1/5.5} = -\frac{11}{9} \approx -1.22$. The absolute value is above 1, so demand is elastic.

Check: revenue goes from $5 \cdot 50 = 250$ to $6 \cdot 40 = 240$, a fall, as elastic demand predicts.

</details>

2\. For each absolute elasticity (0.3, 1, 2.5), say whether demand is elastic, inelastic or unit elastic, and what a price rise does to revenue.

<details class="solution" markdown>
<summary>Solution</summary>

0.3 is inelastic: a price rise raises revenue. 1 is unit elastic: a small price rise leaves revenue unchanged (it is at a peak on a straight line). 2.5 is elastic: a price rise lowers revenue.

Check: by Theorem 2, $\frac{dR}{dP} = Q(1 + E)$ is $0.7Q > 0$, $0$ and $-1.5Q < 0$ for $E = -0.3, -1, -2.5$.

</details>

3\. Demand is $Q = 100 - 4P$. Find the point elasticity at $P = 10$ and say what a price rise does to revenue there.

<details class="solution" markdown>
<summary>Solution</summary>

At $P = 10$, $Q = 60$ and $\frac{dQ}{dP} = -4$, so $E = -4 \cdot \frac{10}{60} = -\frac{2}{3}$. It is inelastic, so a price rise raises revenue.

Check: $R = 100P - 4P^2$ and $\frac{dR}{dP} = 100 - 8P = 20$ at $P = 10$, positive, and $Q(1 + E) = 60 \cdot \frac{1}{3} = 20$.

</details>

### Standard

4\. For $Q = 120 - 20P$, find the price at which $\lvert E \rvert = 1$, and check that revenue at \$2.50, \$3 and \$3.50 is highest at \$3.

<details class="solution" markdown>
<summary>Solution</summary>

By Theorem 1 the unit-elastic price is $\frac{d_0}{2d_1} = \frac{120}{40} = 3$. The revenues are $2.5 \cdot 70 = 175$, $3 \cdot 60 = 180$ and $3.5 \cdot 50 = 175$, so \$3 gives the most.

Check: $E(3) = -\frac{20 \cdot 3}{120 - 60} = -1$, and $\frac{dR}{dP} = 120 - 40 \cdot 3 = 0$.

</details>

5\. Demand is $Q = 200P^{-2}$. (a) What is $E$? (b) The price rises from \$5 to \$5.50. Find the exact percent change in quantity and compare with the prediction from $E$. (c) What happens to revenue?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $E = -2$ at every price, by Theorem 3.

(b) At \$5, $Q = 8$. At \$5.50, $Q = \frac{200}{30.25} = 6.612$. The exact change is $\frac{6.612}{8} - 1 = -17.4\%$. The elasticity predicts $-2 \times 10\% = -20\%$. The two differ because the elasticity is exact only for very small changes.

(c) Revenue goes from $5 \cdot 8 = 40$ to $5.5 \cdot 6.612 = 36.36$, a fall, since $\eta = 2 > 1$.

Check: $R = \frac{200}{P}$ gives 40 and $\frac{200}{5.5} = 36.36$.

</details>

6\. A coffee shop's demand is $Q = 200 + 0.02I + 5P_t - 20P$, where $I$ is average monthly income in dollars, $P_t$ is the price of tea and $P$ is the price of coffee (made up). At $I = 2000$, $P_t = 4$ and $P = 4$, find $Q$, then the income elasticity, the cross-price elasticity with tea and the own-price elasticity. Classify each.

<details class="solution" markdown>
<summary>Solution</summary>

$Q = 200 + 40 + 20 - 80 = 180$.

Income: $E_I = 0.02 \cdot \frac{2000}{180} = \frac{2}{9} \approx 0.22$. It is positive and below 1: coffee is a normal good and a necessity.

Cross-price: $E_{XY} = 5 \cdot \frac{4}{180} = \frac{1}{9} \approx 0.11$. It is positive: tea is a substitute for coffee.

Own price: $E = -20 \cdot \frac{4}{180} = -\frac{4}{9} \approx -0.44$. Demand is inelastic here.

Check: the three terms $0.02I$, $5P_t$ and $-20P$ are 40, 20 and $-80$, and each elasticity is the term over $Q$: $\frac{40}{180}$, $\frac{20}{180}$ and $-\frac{80}{180}$.

</details>

### Challenge

7\. Show that for a straight-line demand curve the midpoint elasticity between two prices $P_1$ and $P_2$ equals the point elasticity at the midpoint $\bar{P} = \frac{P_1 + P_2}{2}$. Check it for $Q = 120 - 20P$ between \$3 and \$4.

<details class="solution" markdown>
<summary>Solution</summary>

Let $Q = d_0 - d_1 P$. Then $Q_2 - Q_1 = -d_1(P_2 - P_1)$, and the average quantity is $\bar{Q} = \frac{Q_1 + Q_2}{2} = d_0 - d_1\bar{P}$, the quantity at the midpoint price. The midpoint elasticity is

$$
\frac{-d_1(P_2 - P_1)/\bar{Q}}{(P_2 - P_1)/\bar{P}} = -d_1\,\frac{\bar{P}}{\bar{Q}},
$$

which is $\frac{dQ}{dP}\cdot\frac{P}{Q}$ at $(\bar{P}, \bar{Q})$.

For \$3 and \$4: $\bar{P} = 3.5$ and $\bar{Q} = 50$, so $-20 \cdot \frac{3.5}{50} = -1.4$, the value from Example 1.

Check: this works only because the line has the same slope everywhere. For a curved demand the two can differ slightly.

</details>

8\. (Reviews [rates of change and marginal analysis](../../05-university-core/03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md).) A firm faces constant-elasticity demand $Q = AP^{-3}$ and has a constant marginal cost of \$2 per unit. (a) Use $\text{MR} = P\left(1 + \frac{1}{E}\right)$ to find the price where marginal revenue equals marginal cost. (b) Check by maximizing profit $(P - 2)AP^{-3}$ directly. (c) What goes wrong if the elasticity were $-1$ or $-0.5$?

<details class="solution" markdown>
<summary>Solution</summary>

(a) With $E = -3$, $\text{MR} = P\left(1 - \frac{1}{3}\right) = \frac{2P}{3}$. Setting it equal to 2 gives $P = 3$.

(b) The profit is $\pi(P) = A\left(P^{-2} - 2P^{-3}\right)$, and $\pi'(P) = A\left(-2P^{-3} + 6P^{-4}\right) = 0$ gives $P = 3$. The sign of $\pi'$ is positive for $P < 3$ and negative for $P > 3$, so $P = 3$ is the maximum.

(c) For $E = -1$, $\text{MR} = P(1 - 1) = 0$, which never equals the cost 2. For $E = -0.5$, $\text{MR} = P(1 - 2) = -P < 0$. There is no price where $\text{MR} = \text{MC}$, and profit keeps rising with price, because demand is not elastic enough. A seller with positive marginal cost always sets the price in the elastic range, where $\text{MR} > 0$.

Check: at $P = 3$ the markup $\frac{P}{\text{MC}} = \frac{3}{2} = \frac{\eta}{\eta - 1}$ for $\eta = 3$.

</details>

## Where this shows up

- The firms and consumers chapter puts elasticity to work in [profit maximization and market structure](../03-firms-and-consumers/03-profit-maximization-and-market-structure.md), where the markup of price over marginal cost depends on the elasticity, as Challenge problem 8 shows for constant elasticity.
- In economics generally, demand curves are estimated by regressing $\ln Q$ on $\ln P$, so the fitted slope is an elasticity: see [regression and econometrics intuition](../04-more-tools/03-regression-and-econometrics-intuition.md). Growth rates measure the same kind of percent response over time: [growth rates and CAGR](../01-measuring-the-economy/03-growth-rates-and-cagr.md).
- In CS, the same percent-over-percent ratio appears wherever a change is relative: how much a system's response time changes per 1% more load, and how sensitive a model's output is to a 1% change in an input (a log-log slope).
