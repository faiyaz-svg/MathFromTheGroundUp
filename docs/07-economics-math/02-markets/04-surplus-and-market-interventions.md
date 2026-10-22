# Surplus and market interventions

After this lesson you can compute consumer and producer surplus as triangle areas (and as integrals for curved demand and supply), show that total surplus is largest at equilibrium, work out the effects of a price ceiling or floor, and find who pays a per-unit tax, how much revenue it raises and how large the deadweight loss is.

Before this: [supply and demand equilibrium algebra](03-supply-and-demand-equilibrium-algebra.md) and [area and circles](../../02-middle-school/06-geometry/02-area-and-circles.md) (for the triangle area). Curved demand and supply use [applications of integrals](../../05-university-core/04-integrals/06-applications-of-integrals.md#definitions), which already has a worked example of surplus, so this lesson doesn't repeat it.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Inverse demand is $P = 10 - \frac{Q}{2}$ and the market price is \$4. Find the quantity bought and the consumer surplus.
2. In the market $Q_d = 120 - 20P$, $Q_s = 10P$ (equilibrium \$4 and 40 units), the government sets a maximum price of \$3. Is it binding? What is the shortage?
3. A \$2 per-unit tax on a good whose equilibrium is 100 units cuts the quantity to 80 units. Find the tax revenue and the deadweight loss.

<details class="solution" markdown>
<summary>Answers</summary>

1. At \$4, $4 = 10 - \frac{Q}{2}$ gives $Q = 12$. The surplus is the triangle between the demand curve and the price: $\frac{1}{2} \cdot 12 \cdot (10 - 4) = 36$ dollars.
2. The ceiling is below the equilibrium price of \$4, so it binds. At \$3, buyers want $120 - 60 = 60$ and sellers offer $30$, a shortage of 30 units.
3. Revenue is the tax times the quantity sold, $2 \times 80 = 160$ dollars. The deadweight loss is the triangle with height \$2 (the tax) and base $100 - 80 = 20$ (the lost trades): $\frac{1}{2} \cdot 2 \cdot 20 = 20$ dollars.

</details>

## The idea

A buyer who would have paid \$6 for a bubble tea and pays \$4 comes out \$2 ahead. A seller who would have sold at \$1 and gets \$4 comes out \$3 ahead. Add up these gains over everyone who trades, and you have the surplus of the market: how much better off the trades leave people than not trading. The surplus is the number that lets you compare market arrangements, such as a price cap or a tax, on one scale.

The picture is simple. The demand curve is a staircase of what each buyer would pay (smoothed into a line when there are many buyers), and the market price is a horizontal line. The gap between them, summed over the units sold, is the buyers' surplus, and it is a triangle for a straight demand curve. The same holds for sellers, between the price and the supply curve.

![Left: with demand P = 6 minus Q over 20 and supply P = Q over 10, the equilibrium is (40, 4). The triangle between the demand line and the price line is consumer surplus, equal to 40, and the triangle between the price line and the supply line is producer surplus, equal to 80. Right: with a 3 dollar per-unit tax the quantity falls to 20, buyers pay 5 and sellers keep 2. The rectangle between prices 2 and 5 is tax revenue, 60. Consumer surplus falls to 10, producer surplus to 20, and the triangle between 20 and 40 units is the deadweight loss, 30.](../../assets/figures/07-economics-math/surplus-and-market-interventions-surplus.svg)

The lesson then asks what happens when the government interferes with the price or with the quantity. A price ceiling and a price floor stop the price from reaching equilibrium. A tax puts a gap between what buyers pay and what sellers keep. Each one moves surplus from one group to another and also destroys some of it, and the destroyed part is the deadweight loss.

## Definitions

The **consumer surplus** (CS) in a market is the total amount by which buyers' willingness to pay for the units they buy exceeds the price they pay. The **producer surplus** (PS) is the total amount by which the price sellers receive exceeds their minimum acceptable prices for the units they sell. In plain words, each is a gain from trade, measured in dollars: buyers' value minus price, and price minus sellers' cost.

Let $P_d(Q)$ and $P_s(Q)$ be the inverse demand and inverse supply functions, let $Q$ be the quantity traded and let $P$ be the price (buyers pay it and sellers receive it, until a tax comes in). Then the surpluses are

$$
\text{CS} = \int_0^{Q}\bigl(P_d(x) - P\bigr)\,dx, \qquad \text{PS} = \int_0^{Q}\bigl(P - P_s(x)\bigr)\,dx.
$$

In plain words, they are the areas between the price line and the two curves, out to the quantity traded. For straight lines these areas are triangles. The **total surplus** is $\text{TS} = \text{CS} + \text{PS}$, and, when the quantity is $Q$ and units are exchanged between the willing, $\text{TS}(Q) = \int_0^{Q}\bigl(P_d(x) - P_s(x)\bigr)\,dx$, the value to buyers minus the cost to sellers of each unit up to $Q$.

A **price ceiling** is a legal maximum price. A **price floor** is a legal minimum price. A ceiling or floor is **binding** if it changes the price from the equilibrium, which happens when a ceiling is below $P^*$ or a floor is above it, and **non-binding** otherwise. Under a binding ceiling there is a shortage ($Q_d > Q_s$), and under a binding floor there is a surplus of goods ($Q_s > Q_d$): "surplus" here means unsold goods, and it is a different thing from consumer and producer surplus.

A **per-unit tax** of $t$ dollars is an amount paid to the government on each unit sold. A **per-unit subsidy** of $s$ dollars is an amount the government pays on each unit sold. With a tax there are two prices: $P_b$, what buyers pay, and $P_k$, what sellers keep, with $P_b - P_k = t$. That difference is the **tax wedge**. The **tax revenue** is $t \times Q$, where $Q$ is the quantity actually traded. The **tax incidence** is the split of the tax burden between buyers and sellers: buyers bear $P_b - P^*$ per unit, and sellers bear $P^* - P_k$ per unit. The **deadweight loss** (DWL) is the total surplus that disappears and goes to nobody: the surplus before the intervention minus the sum of the surpluses (and tax revenue, less subsidy cost) after it.

## How to do it

### Surplus for straight lines

1. Find the equilibrium (or the price and quantity the problem gives).
2. Find the intercepts: the choke price $P_d(0)$, where demand reaches zero, and the lowest supply price $P_s(0)$.
3. Consumer surplus is $\frac{1}{2} \times Q \times (P_d(0) - P)$. Producer surplus is $\frac{1}{2} \times Q \times (P - P_s(0))$.
4. For a curved line, integrate as in the definition, using the earlier [applications of integrals](../../05-university-core/04-integrals/06-applications-of-integrals.md#how-to-do-it) lesson, or split into pieces whose areas you know.
5. Check that the surpluses are positive and that CS plus PS is the area between the two curves up to $Q$.

*Theorem 1 (total surplus is largest at equilibrium).* Let $P_d$ be decreasing, $P_s$ be increasing, and both continuous, with $P_d(Q^*) = P_s(Q^*)$. Then $\text{TS}(Q) = \int_0^{Q}(P_d - P_s)\,dx$ is largest at $Q = Q^*$.

What we know: the fundamental theorem of calculus gives the derivative of an integral with a variable upper limit, and the curves are monotone. What we want: the quantity that maximizes TS. The plan is to find where $\text{TS}$ increases and where it decreases.

*Proof.* By the fundamental theorem, $\text{TS}'(Q) = P_d(Q) - P_s(Q)$. For $Q < Q^*$, since $P_d$ is decreasing and $P_s$ is increasing, $P_d(Q) > P_d(Q^*) = P_s(Q^*) > P_s(Q)$, so $\text{TS}' > 0$ and TS is increasing. For $Q > Q^*$ the same argument reverses the inequalities, so $\text{TS}' < 0$ and TS is decreasing. A function that increases up to $Q^*$ and then decreases has its largest value at $Q^*$. $\blacksquare$

Look back: the derivative says that the $Q$-th unit adds $P_d(Q) - P_s(Q)$ to total surplus, the value to the buyer minus the cost to the seller. Units before $Q^*$ are worth more to a buyer than they cost a seller, so making them adds surplus, and units after $Q^*$ cost more than they are worth, so making them subtracts. Every intervention that moves the quantity away from $Q^*$ loses the triangle between the curves on that stretch, which is the deadweight loss.

### Ceilings and floors

1. Find the equilibrium $(P^*, Q^*)$.
2. Compare the controlled price with $P^*$. A ceiling above $P^*$, or a floor below it, is non-binding: nothing changes.
3. If it binds, compute $Q_d$ and $Q_s$ at the controlled price. The quantity traded is the smaller of the two, because nobody can be forced to buy or sell more than they want.
4. The shortage (ceiling) or surplus of goods (floor) is $\lvert Q_d - Q_s \rvert$.
5. Compute the surpluses for the quantity traded. The answer depends on who gets the scarce units: assume, as an upper bound, that the units go to the buyers who value them most (under a ceiling) or are sold by the sellers with the lowest cost (under a floor). If they don't, the surplus is smaller.
6. The deadweight loss is the part of $\text{TS}(Q^*)$ that is gone.

### A per-unit tax

With a tax $t$ on sellers, buyers pay $P_b$ and sellers keep $P_k = P_b - t$, and the market clears when $Q_d(P_b) = Q_s(P_k)$.

1. Write the equation $Q_d(P_b) = Q_s(P_b - t)$ and solve for $P_b$.
2. Find $P_k = P_b - t$ and the quantity $Q$.
3. Tax revenue is $tQ$. The buyers' burden is $P_b - P^*$ per unit and the sellers' is $P^* - P_k$.
4. CS is the triangle above $P_b$ and under demand. PS is the triangle below $P_k$ and above supply.
5. The deadweight loss is the triangle with height $t$ and base $Q^* - Q$.
6. Check: $\text{CS} + \text{PS} + \text{revenue} + \text{DWL}$ equals the surplus before the tax.

A tax on buyers gives the same prices and quantity. That is because the market only sees the wedge: when the buyer pays the tax, the buyer's net price is $P + t$ and demand reads $Q_d(P + t)$, which is the same equation with $P = P_k$.

*Theorem 2 (incidence in the linear model).* For $Q_d = d_0 - d_1 P$ and $Q_s = s_0 + s_1 P$, with a per-unit tax $t$ small enough that trade continues, the equilibrium prices and quantity are

$$
P_b = P^* + \frac{s_1}{d_1 + s_1}\,t, \qquad P_k = P^* - \frac{d_1}{d_1 + s_1}\,t, \qquad Q = Q^* - \frac{d_1 s_1}{d_1 + s_1}\,t.
$$

So buyers bear the fraction $\frac{s_1}{d_1 + s_1}$ of the tax and sellers bear $\frac{d_1}{d_1 + s_1}$, the fractions add to 1, and the deadweight loss is $\frac{1}{2}\,t\,(Q^* - Q) = \frac{d_1 s_1}{2(d_1 + s_1)}\,t^2$.

What we know: the market clears when $d_0 - d_1 P_b = s_0 + s_1 (P_b - t)$, and the untaxed equilibrium satisfies $d_0 - s_0 = (d_1 + s_1)P^*$ (Theorem 1 of the [previous lesson](03-supply-and-demand-equilibrium-algebra.md#solving-for-the-equilibrium)). What we want: $P_b$, $P_k$ and $Q$. The plan is to solve the equation for $P_b$, then subtract $P^*$.

*Proof.* Collecting the terms in $P_b$ gives $d_0 - s_0 + s_1 t = (d_1 + s_1)P_b$, so $P_b = \frac{d_0 - s_0}{d_1 + s_1} + \frac{s_1}{d_1 + s_1}t = P^* + \frac{s_1}{d_1 + s_1}t$. Then $P_k = P_b - t = P^* - \frac{d_1}{d_1 + s_1}t$, because $\frac{s_1}{d_1 + s_1} - 1 = -\frac{d_1}{d_1 + s_1}$. The quantity is $Q = d_0 - d_1 P_b = Q^* - \frac{d_1 s_1}{d_1 + s_1}t$. The lost trades are $Q^* - Q = \frac{d_1 s_1}{d_1 + s_1}t$, and the deadweight loss is a triangle with base $Q^* - Q$ and height $t$, which gives the last formula. $\blacksquare$

Look back: the share of the tax that falls on buyers is $\frac{s_1}{d_1 + s_1}$, so it is larger when sellers respond more to price (large $s_1$) and smaller when buyers do (large $d_1$). The side that is less able to walk away bears more of the tax, and the law gives no say in this: it doesn't matter whether the law puts the tax on buyers or sellers. Also the deadweight loss is proportional to $t^2$: doubling the tax quadruples the loss, but doubles the revenue only at first, as the later remark shows.

For a **subsidy** of $s$, set $t = -s$: the formulas give a quantity above $Q^*$, buyers paying less than $P^*$ and sellers receiving more. The government pays $sQ$, and the deadweight loss is again a triangle, the lost surplus on units whose cost exceeds their value.

## Worked examples

<div class="example" markdown>

### Example 1: surplus and a \$3 tax

A made-up market for bubble tea has $Q_d = 120 - 20P$ and $Q_s = 10P$ (cups a day, dollars). Find the surpluses. Then the government puts a \$3 per-unit tax on sellers: find the prices, the quantity, the tax revenue, the incidence, and the deadweight loss.

Step 1: the equilibrium is $P^* = 4$, $Q^* = 40$ (from the previous lesson).

Step 2: the inverse demand is $P = 6 - \frac{Q}{20}$ with choke price 6. The inverse supply is $P = \frac{Q}{10}$ with $P_s(0) = 0$.

Step 3: $\text{CS} = \frac{1}{2} \cdot 40 \cdot (6 - 4) = 40$ and $\text{PS} = \frac{1}{2} \cdot 40 \cdot (4 - 0) = 80$, so $\text{TS} = 120$ dollars a day.

Now the tax. The market clears when $120 - 20P_b = 10(P_b - 3)$, so $150 = 30P_b$ and $P_b = 5$. Sellers keep $P_k = 5 - 3 = 2$, and the quantity is $120 - 100 = 20$.

Revenue is $3 \times 20 = 60$. Buyers pay \$1 more than before and sellers receive \$2 less, so buyers bear $\frac{1}{3}$ of the tax and sellers $\frac{2}{3}$, as Theorem 2 predicts: $\frac{s_1}{d_1 + s_1} = \frac{10}{30}$.

The surpluses after the tax: $\text{CS} = \frac{1}{2} \cdot 20 \cdot (6 - 5) = 10$ and $\text{PS} = \frac{1}{2} \cdot 20 \cdot (2 - 0) = 20$. So buyers lose $40 - 10 = 30$, sellers lose $80 - 20 = 60$, and the government gains 60. The net loss is $30 + 60 - 60 = 30$.

The deadweight loss from the triangle is $\frac{1}{2} \cdot 3 \cdot (40 - 20) = 30$, and Theorem 2 gives $\frac{20 \cdot 10}{2 \cdot 30}\,3^2 = 30$.

Check: $10 + 20 + 60 + 30 = 120$, the surplus before the tax. If the tax is put on buyers instead, buyers pay $P + 3$ and the market clears when $120 - 20(P + 3) = 10P$, so $P = 2$: sellers keep \$2 and buyers pay \$5, the same as before.

</div>

<div class="example" markdown>

### Example 2: a ceiling and a floor

In the same market ($P^* = 4$, $Q^* = 40$), find the effects of (a) a ceiling of \$3, (b) a floor of \$5, and (c) a ceiling of \$5.

(a) The ceiling is below \$4, so it binds. At \$3 buyers want $120 - 60 = 60$ and sellers offer $30$. Trade is the short side, 30 units, and the shortage is 30. If the 30 units go to the buyers who value them most, the buyers' willingness to pay runs from \$6 down to $P_d(30) = 4.5$, so $\text{CS} = \int_0^{30}\left(6 - \frac{x}{20} - 3\right)dx = 90 - 22.5 = 67.5$ and $\text{PS} = \int_0^{30}\left(3 - \frac{x}{10}\right)dx = 90 - 45 = 45$. Total surplus is 112.5, down from 120, so $\text{DWL} = 7.5$. Buyers who get a unit gain (CS rises from 40 to 67.5, at the best) and sellers lose (PS falls from 80 to 45).

(b) The floor is above \$4, so it binds. At \$5 buyers want 20 and sellers offer 50. Trade is again the short side, 20 units, and there are 30 unsold units. With the lowest-cost sellers selling, $\text{CS} = \frac{1}{2} \cdot 20 \cdot (6 - 5) = 10$ and $\text{PS} = 5 \cdot 20 - \int_0^{20}\frac{x}{10}\,dx = 100 - 20 = 80$. The total is 90 and $\text{DWL} = 30$.

(c) A ceiling of \$5 is above \$4, so it doesn't bind. Nothing changes: the price stays at \$4 and the quantity at 40.

Check: the DWL in (a) is the triangle with vertices $(30, 4.5)$, $(30, 3)$ and $(40, 4)$: base 1.5, height 10, area $\frac{1}{2} \cdot 1.5 \cdot 10 = 7.5$. In (b), the triangle with vertices $(20, 5)$, $(20, 2)$ and $(40, 4)$ has area $\frac{1}{2} \cdot 3 \cdot 20 = 30$, as in the tax example, because the quantity is the same, 20.

</div>

<div class="example" markdown>

### Example 3: a subsidy

In the same market, the government pays sellers \$3 for each cup sold. Find the prices, the quantity, the cost and the deadweight loss.

Sellers receive $P_k = P_b + 3$. The market clears when $120 - 20P_b = 10(P_b + 3)$, so $90 = 30P_b$ and $P_b = 3$. Sellers receive \$6, and the quantity is $120 - 60 = 60$. The cost to the government is $3 \times 60 = 180$.

Buyers gain $\text{CS} = \frac{1}{2} \cdot 60 \cdot (6 - 3) = 90$, up 50 from 40. Sellers have $\text{PS} = \frac{1}{2} \cdot 60 \cdot (6 - 0) = 180$, up 100 from 80. The gains are 150 and the cost is 180, so the net loss is $180 - 150 = 30$, the same as the deadweight loss in the formula, $\frac{1}{2} \cdot 3 \cdot (60 - 40) = 30$.

Check: the subsidy is shared in the same proportions as the tax was: buyers' price falls \$1 (a third of \$3) and sellers' price rises \$2 (two thirds). The totals add up: $90 + 180 - 180 = 90 = 120 - 30$.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Inverse demand is $P = 20 - Q$ and inverse supply is $P = Q + 4$ (made up). Find the equilibrium, the surpluses, and the effect of a \$2 per-unit tax on sellers: the two prices, the quantity, the revenue, and the deadweight loss.

Step 1: $20 - Q = Q + 4$ gives $Q^* = 8$ and $P^* = 12$.

Step 2: the choke price is 20 and the lowest supply price is 4. $\text{CS} = \frac{1}{2} \cdot 8 \cdot (20 - 12) = 32$ and $\text{PS} = \frac{1}{2} \cdot 8 \cdot (12 - 4) = 32$.

Now find the market with the tax: let buyers pay $P_b$ and sellers keep $P_b - 2$, and set the two quantities equal.

<details class="solution" markdown>
<summary>Finish</summary>

In quantity form, $Q_d = 20 - P_b$ and $Q_s = P_k - 4 = P_b - 6$. Setting them equal, $20 - P_b = P_b - 6$ gives $P_b = 13$, so $P_k = 11$ and $Q = 7$. Revenue is $2 \times 7 = 14$. The buyers bear \$1 and the sellers bear \$1, an even split since the lines have the same steepness. The deadweight loss is $\frac{1}{2} \cdot 2 \cdot (8 - 7) = 1$.

Check: $\text{CS} = \frac{1}{2} \cdot 7 \cdot (20 - 13) = 24.5$ and $\text{PS} = \frac{1}{2} \cdot 7 \cdot (11 - 4) = 24.5$. Then $24.5 + 24.5 + 14 + 1 = 64$, the surplus before the tax.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a ceiling or floor only matters on the side of the equilibrium price where it binds. A ceiling above $P^*$ or a floor below it does nothing. Compare the controlled price with $P^*$ before you compute anything.

</div>

<div class="warning" markdown>

Watch out: the quantity under a binding ceiling or floor is the smaller of $Q_d$ and $Q_s$, not the larger and not their average. At a ceiling of \$3, buyers want 60 and sellers offer 30, and only 30 trade.

</div>

<div class="warning" markdown>

Watch out: the tax triangle has height $t$, not the price change of one side, and base $Q^* - Q$, the lost units. Tax revenue is the rectangle with the same height $t$ and the base $Q$, the units still sold. Using $Q^*$ for the revenue overstates it ($3 \times 40 = 120$ instead of 60 in Example 1).

</div>

<div class="warning" markdown>

Watch out: the legal burden of a tax is not the economic burden. If the law makes sellers pay the \$3, sellers still do not bear all of it: buyers pay \$1 more per cup. Incidence follows the slopes, not who writes the cheque.

</div>

Two edge cases are worth knowing. A tax at least as large as the gap between the choke price and the lowest supply price ends all trade, because no buyer is willing to pay more than a seller needs: here that is $6 - 0 = 6$, and at $t = 6$ the formula gives $Q = 40 - \frac{200}{30} \cdot 6 = 0$. Above that the formulas are not valid, since the quantity can't be negative. Second, the surplus calculations for ceilings and floors depend on who gets the goods. If the scarce units under a ceiling go to buyers by queue or luck and not to those with the highest willingness to pay, the consumer surplus is lower than the 67.5 above, and the deadweight loss is higher than 7.5. The efficient allocation is the best case for the ceiling.

A percent tax such as HST works the same way as a per-unit tax, with a wedge between the buyer's and the seller's price, but the wedge is a share of the price and not a fixed dollar amount. The algebra in this lesson covers the per-unit case.

## Tricks and shortcuts

For straight lines, skip the integrals: $\text{CS} = \frac{1}{2}Q(P_d(0) - P)$ and $\text{PS} = \frac{1}{2}Q(P - P_s(0))$. A tax triangle is always $\frac{1}{2} \times t \times (\text{lost units})$, so you only need the quantity before and after.

To get the incidence quickly, compare the two coefficients: the buyers' share is $\frac{s_1}{d_1 + s_1}$ and the sellers' is $\frac{d_1}{d_1 + s_1}$. In Example 1, $d_1 = 20$ and $s_1 = 10$, so buyers bear $\frac{1}{3}$. The next lesson writes the same shares with elasticities.

A tax raises revenue $R(t) = t\,Q(t) = t\left(Q^* - kt\right)$, with $k = \frac{d_1 s_1}{d_1 + s_1}$. This is a downward-opening parabola in $t$, which is $0$ at $t = 0$ and again at $t = \frac{Q^*}{k}$, so revenue is largest at $t = \frac{Q^*}{2k}$, halfway between. In Example 1, $k = \frac{200}{30}$ and $Q^* = 40$, so $\frac{40}{2k} = 3$: the \$3 tax is the one that raises the most revenue, \$60. A higher tax raises less. Challenge problem 8 asks you to check this.

## In code

One function can price any linear market with a tax, subsidy or no intervention. It uses the formulas of Theorem 2 and the triangle areas, and it checks that the pieces add up to the original surplus.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction as F

def market(d0, d1, s0, s1, t=0):
    """Qd = d0 - d1*P, Qs = s0 + s1*P, a per-unit tax t (negative for a subsidy)."""
    pb = F(d0 - s0 + s1 * t, d1 + s1)      # price buyers pay
    ps = pb - t                            # price sellers keep
    q = d0 - d1 * pb
    cs = F(1, 2) * q * (F(d0, d1) - pb)    # triangle under inverse demand
    ps_surplus = F(1, 2) * q * (ps + F(s0, s1))  # triangle above inverse supply
    revenue = t * q
    return dict(pb=pb, ps=ps, q=q, cs=cs, producer=ps_surplus, revenue=revenue,
                total=cs + ps_surplus + revenue)

base = market(120, 20, 0, 10)
taxed = market(120, 20, 0, 10, t=3)
print(base["pb"], base["q"], base["cs"], base["producer"])
# 4 40 40 80
print(taxed["pb"], taxed["ps"], taxed["q"], taxed["revenue"])
# 5 2 20 60
print("deadweight loss", base["total"] - taxed["total"])
# deadweight loss 30

# A subsidy is a negative tax. The government's cost is -revenue.
sub = market(120, 20, 0, 10, t=-3)
print(sub["pb"], sub["ps"], sub["q"], "cost", -sub["revenue"], "deadweight loss", base["total"] - sub["total"])
# 3 6 60 cost 180 deadweight loss 30
```

</details>

## FAQ

### Why is the deadweight loss a triangle?

Each lost unit would have created a gain of $P_d(Q) - P_s(Q)$, the buyer's value minus the seller's cost. For straight lines, this gap shrinks linearly from $t$ at the tax quantity $Q$ down to 0 at $Q^*$, so the total of the gaps is a triangle with height $t$ and base $Q^* - Q$. The gap at $Q$ equals the tax: at 20 units buyers value the next cup at \$5 and it costs sellers \$2 to make, a gap of \$3 that the tax stops from being traded.

### Does a price ceiling help buyers?

It helps the buyers who get the good, because they pay less. It hurts those who don't, since the shortage means some buyers who would have paid \$4 can't buy at all. The total surplus falls, and what the buyers who get the good gain is less than what sellers lose. Whether the policy is worth it depends on goals that the model doesn't judge.

### Why can the tax be on sellers or on buyers with the same result?

Because the market only sees the wedge. The buyers' price minus the sellers' price equals $t$ either way, and the two prices have to clear the market. Whoever sends the money to the government, the equation to solve is the same.

### What about a real price floor?

Ontario's general minimum wage is \$17.95 an hour from October 1, 2026 (source: the Ontario government's [minimum wage page](https://www.ontario.ca/document/your-guide-employment-standards-act-0/minimum-wage), which says the rate applies until September 30, 2027). A wage is the price of labour, so a minimum wage is a price floor. In the simple model, if the wage that would clear a market is below the floor, the floor binds and more people want the work than there are jobs, as in Practice problem 5. If the market-clearing wage is above \$17.95, the floor is non-binding. Real labour markets have other features that the two-line model leaves out, so the model is a way to see the mechanism, not a forecast.

## Practice

### Warm-up

1\. Inverse demand is $P = 20 - Q$ and inverse supply is $P = Q + 4$. Find the equilibrium, the consumer surplus, the producer surplus and the total surplus.

<details class="solution" markdown>
<summary>Solution</summary>

$20 - Q = Q + 4$ gives $Q^* = 8$ and $P^* = 12$. $\text{CS} = \frac{1}{2} \cdot 8 \cdot (20 - 12) = 32$ and $\text{PS} = \frac{1}{2} \cdot 8 \cdot (12 - 4) = 32$, so $\text{TS} = 64$.

Check: the total surplus is the triangle between the curves out to $Q^* = 8$, with height $20 - 4 = 16$ at $Q = 0$: $\frac{1}{2} \cdot 8 \cdot 16 = 64$.

</details>

2\. In the market of Problem 1 (so $Q_d = 20 - P$ and $Q_s = P - 4$), decide whether each control binds, and give the shortage or surplus of goods: (a) a ceiling of \$15, (b) a ceiling of \$9, (c) a floor of \$10, (d) a floor of \$14.

<details class="solution" markdown>
<summary>Solution</summary>

The equilibrium price is \$12. (a) A ceiling of \$15 is above it: non-binding. (b) A ceiling of \$9 binds: $Q_d = 11$, $Q_s = 5$, a shortage of 6, and 5 units trade. (c) A floor of \$10 is below \$12: non-binding. (d) A floor of \$14 binds: $Q_d = 6$, $Q_s = 10$, a surplus of 4 goods, and 6 units trade.

Check: in each binding case the quantity traded is the smaller of $Q_d$ and $Q_s$, and it is below $Q^* = 8$, so trade falls.

</details>

3\. In the market of Problem 1, a \$2 per-unit tax is put on sellers. Find the prices buyers pay and sellers keep, the quantity, the revenue and the deadweight loss. Who bears the tax?

<details class="solution" markdown>
<summary>Solution</summary>

Buyers pay $P_b$ and sellers keep $P_b - 2$. Then $20 - P_b = (P_b - 2) - 4$, so $P_b = 13$, $P_k = 11$ and $Q = 7$. Revenue is $2 \times 7 = 14$. Buyers pay \$1 more than \$12 and sellers get \$1 less, so each side bears half. The deadweight loss is $\frac{1}{2} \cdot 2 \cdot (8 - 7) = 1$.

Check: the slopes are equal ($d_1 = s_1 = 1$), so Theorem 2 gives an even split. $\text{CS} + \text{PS} = 24.5 + 24.5 = 49$, and $49 + 14 + 1 = 64$.

</details>

### Standard

4\. In the same market, the government instead pays a \$2 per-unit subsidy to sellers. Find the prices, the quantity, the cost and the deadweight loss, and show that the totals add up.

<details class="solution" markdown>
<summary>Solution</summary>

Sellers receive $P_b + 2$, so $20 - P_b = (P_b + 2) - 4$, which gives $2P_b = 22$, $P_b = 11$, $P_k = 13$ and $Q = 9$. The cost is $2 \times 9 = 18$. The deadweight loss is $\frac{1}{2} \cdot 2 \cdot (9 - 8) = 1$.

Check: $\text{CS} = \frac{1}{2} \cdot 9 \cdot (20 - 11) = 40.5$ and $\text{PS} = \frac{1}{2} \cdot 9 \cdot (13 - 4) = 40.5$. These total 81, less the cost 18 gives 63, which is $64 - 1$.

</details>

5\. A made-up local market for part-time labour has demand $L_d = 480 - 20w$ and supply $L_s = 10w$, with $w$ the hourly wage in dollars and $L$ in thousands of hours a week. (a) Find the equilibrium wage and hours. (b) Ontario's general minimum wage is \$17.95 an hour from October 1, 2026 (Ontario government, ontario.ca). Is it binding in this market? (c) Find the hours worked and the surplus of labour. (d) Find the weekly wage bill (in thousands of dollars) before and after the floor.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $480 - 20w = 10w$ gives $w = 16$ and $L = 160$.

(b) The floor, \$17.95, is above \$16, so it binds in this made-up market. (A market with a higher clearing wage would not be affected.)

(c) At \$17.95, employers want $480 - 20(17.95) = 121$ and workers supply $10(17.95) = 179.5$. Hours worked are the smaller, 121 thousand, and the surplus of labour is $179.5 - 121 = 58.5$ thousand hours.

(d) Before: $16 \times 160 = 2560$ thousand dollars. After: $17.95 \times 121 = 2171.95$ thousand dollars. The wage bill falls, because in this market labour demand is elastic at the floor: the percent drop in hours is bigger than the percent rise in the wage. With a less elastic demand it would rise.

Check: $480 - 359 = 121$ and $17.95 \times 10 = 179.5$. The next lesson explains the wage-bill result with elasticity.

</details>

6\. Use Theorem 2 for the bubble tea market ($d_1 = 20$, $s_1 = 10$, $P^* = 4$, $Q^* = 40$) with a tax of $t = 2$. Find $P_b$, $P_k$, $Q$, the revenue and the deadweight loss, and compare the deadweight loss with the one for $t = 3$.

<details class="solution" markdown>
<summary>Solution</summary>

$P_b = 4 + \frac{10}{30}\cdot 2 = 4.667$ and $P_k = 4 - \frac{20}{30}\cdot 2 = 2.667$. The quantity is $40 - \frac{200}{30}\cdot 2 = 26.67$. Revenue is $2 \times 26.67 = 53.33$. The deadweight loss is $\frac{1}{2}\cdot\frac{200}{30}\cdot 4 = 13.33$.

For $t = 3$ the deadweight loss was 30. The ratio is $\frac{30}{13.33} = 2.25 = \left(\frac{3}{2}\right)^2$: the deadweight loss grows as the square of the tax.

Check: $P_b - P_k = 4.667 - 2.667 = 2$, the tax, and $120 - 20(4.667) = 26.67 = 10(2.667)$.

</details>

### Challenge

7\. Inverse demand is $P = 36 - q^2$ and inverse supply is $P = 12 + 2q$ (made up; $q$ in thousands, $P$ in dollars). (a) Find the equilibrium. (b) Find CS and PS by integration. (c) Find $\text{TS}(q)$ and show it is largest at $q^*$ by comparing with $q = 3$ and $q = 5$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $36 - q^2 = 12 + 2q$ gives $q^2 + 2q - 24 = 0$, so $(q + 6)(q - 4) = 0$. The positive root is $q^* = 4$ and $p^* = 20$.

(b) $\text{CS} = \int_0^4\left(36 - q^2 - 20\right)dq = \left[16q - \frac{q^3}{3}\right]_0^4 = 64 - \frac{64}{3} = \frac{128}{3} \approx 42.67$. $\text{PS} = \int_0^4(20 - 12 - 2q)\,dq = \left[8q - q^2\right]_0^4 = 32 - 16 = 16$.

(c) $\text{TS}(q) = \int_0^q\left(24 - x^2 - 2x\right)dx = 24q - \frac{q^3}{3} - q^2$. Then $\text{TS}(4) = 96 - \frac{64}{3} - 16 = \frac{176}{3} \approx 58.67$, $\text{TS}(3) = 72 - 9 - 9 = 54$ and $\text{TS}(5) = 120 - \frac{125}{3} - 25 = \frac{160}{3} \approx 53.33$. Both neighbours are smaller.

Check: $\frac{128}{3} + 16 = \frac{176}{3}$, which is $\text{TS}(4)$. Also $\text{TS}'(q) = 24 - q^2 - 2q$ is $P_d - P_s$ and it is 0 at $q = 4$.

</details>

8\. (Reviews [quadratic functions and graphs](../../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md).) In the linear model, the tax revenue is $R(t) = t(Q^* - kt)$ with $k = \frac{d_1 s_1}{d_1 + s_1}$. (a) Find the tax $t$ that maximizes revenue and the maximum revenue. (b) Check it for the bubble tea market. (c) What tax ends all trade?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $R(t) = Q^*t - kt^2$ is a parabola opening downward, with its vertex at $t = \frac{Q^*}{2k}$. The maximum is $R = Q^*\cdot\frac{Q^*}{2k} - k\cdot\frac{Q^{*2}}{4k^2} = \frac{Q^{*2}}{4k}$.

(b) Here $k = \frac{200}{30} = \frac{20}{3}$ and $Q^* = 40$, so $t = \frac{40}{40/3} = 3$ and $R = \frac{1600}{80/3} = 60$.

(c) Trade ends when $Q = Q^* - kt = 0$, so $t = \frac{Q^*}{k} = 6$ for the bubble tea market. Revenue is 0 there, and the vertex is halfway between the two zeros of the parabola, at $t = 3$.

Check: $R(2) = 53.33$ and $R(4) = 4(40 - 26.67) = 53.33$, both below $R(3) = 60$, and symmetric around 3.

</details>

## Where this shows up

- The next lesson, [elasticity](05-elasticity.md), shows that the tax shares are the elasticities of supply and demand, and why a tax on a good with few substitutes raises more revenue per unit of lost trade.
- Later, [profit maximization and market structure](../03-firms-and-consumers/03-profit-maximization-and-market-structure.md) uses the same surplus triangles to compare market structures, and the HST on a purchase is a percent tax that you can compute in tips, discounts and HST<!-- link: ../../08-financial-math/01-everyday-money/01-tips-discounts-and-hst.md -->.
- In CS, a rate limit or a cap on a shared resource, such as a fixed number of API calls, is a ceiling on the price in effect, and the shortage shows up as a queue or as rejected requests.
