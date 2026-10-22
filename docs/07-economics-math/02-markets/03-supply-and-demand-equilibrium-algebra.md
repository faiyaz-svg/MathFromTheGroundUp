# Supply and demand equilibrium algebra

After this lesson you can write demand and supply as functions and as inverse functions, solve for the equilibrium price and quantity, tell a shift of a curve from a movement along it, work out how the equilibrium changes when a parameter changes, and add buyers' demands horizontally, including the kink when a buyer drops out.

Before this: [systems of linear equations](../../03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md#applications) (which has a first market example), [composition and inverse functions](../../03-high-school/03-functions/05-composition-and-inverse-functions.md) and [opportunity cost and the PPC](01-opportunity-cost-and-the-ppc.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Demand is $Q_d = 120 - 20P$ and supply is $Q_s = 10P$, with $P$ in dollars and $Q$ in cups a day. Find the equilibrium. Then write the inverse demand function $P(Q)$.
2. Say whether each event shifts the demand curve, shifts the supply curve, or moves along a curve: (a) the price of tea falls, and tea is a substitute for coffee; (b) a coffee shop cuts its coffee price.
3. Demand rises so that $Q_d = 150 - 20P$, with the same supply. Find the new equilibrium and say what happened to the price and the quantity.

<details class="solution" markdown>
<summary>Answers</summary>

1. Set $120 - 20P = 10P$, so $30P = 120$ and $P = 4$, and then $Q = 10 \cdot 4 = 40$. Solving $Q = 120 - 20P$ for $P$ gives $P = 6 - \frac{Q}{20}$.
2. (a) A fall in the price of a substitute shifts the demand for coffee to the left. (b) A change in the good's own price moves along the demand curve, a change in the quantity demanded.
3. Set $150 - 20P = 10P$, so $P = 5$ and $Q = 50$. Both the price and the quantity rose.

</details>

## The idea

A campus kiosk sells bubble tea. If the price is \$2, a lot of students will buy one, and if it is \$6 almost nobody will. At a high price the kiosk would love to sell more, and at a low price it would rather sell fewer. A table of "price, cups wanted, cups offered" shows two lists that move in opposite directions. At one price they meet, and that price is the equilibrium.

The math is two lines and a crossing point, which you met in [systems of linear equations](../../03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md). What this lesson adds is the economics reading of the algebra: which way the lines must slope and why, what moves a line and what moves you along it, and a formula that says how the crossing point moves when something changes. Economists call that exercise comparative statics, comparing two equilibria without asking how the market got from one to the other.

One more habit is worth getting straight at the start. The demand equation gives quantity as a function of price, $Q = 120 - 20P$, but the graph puts price on the vertical axis. So the line you draw is the inverse function, $P = 6 - \frac{Q}{20}$. The next section says why.

![Left: the demand line P = 6 minus Q over 20 and the supply line P = Q over 10 cross at (40, 4). A dashed demand line after a shift crosses supply at (50, 5). Right: the demand lines of two buyers, and their horizontal sum, which has a kink at (6, 5) where buyer 1 drops out, crossing the supply line at (5, 5.5).](../../assets/figures/07-economics-math/supply-and-demand-equilibrium-algebra-equilibrium.svg)

## Definitions

The **quantity demanded** of a good, $Q_d$, is the amount buyers are willing and able to buy at a given price, and the **demand function** gives it for every price. The **quantity supplied**, $Q_s$, is the amount sellers are willing to sell at a given price, and the **supply function** gives it for every price. For a linear model, in the notation of the earlier lesson,

$$
Q_d = d_0 - d_1 P, \qquad Q_s = s_0 + s_1 P, \qquad d_1 > 0, \ s_1 > 0.
$$

In plain words, $d_1$ and $s_1$ say how many units the quantity changes per dollar of price. The signs are the **law of demand** (a higher price means a lower quantity demanded) and the **law of supply** (a higher price means a higher quantity supplied). They are assumptions that hold for most goods, not theorems.

The **inverse demand function** $P_d(Q)$ is the price at which buyers would take exactly $Q$ units, and the **inverse supply function** $P_s(Q)$ is the price at which sellers would offer exactly $Q$ units. For the linear model,

$$
P_d(Q) = \frac{d_0 - Q}{d_1}, \qquad P_s(Q) = \frac{Q - s_0}{s_1}.
$$

In plain words, inverse demand is the highest price at which the $Q$-th unit still sells, which is the buyers' willingness to pay for that unit, and inverse supply is the lowest price at which the $Q$-th unit is worth producing. Both are the inverse functions of [the earlier lesson](../../03-high-school/03-functions/05-composition-and-inverse-functions.md), and they exist because each curve passes the horizontal line test.

A **market equilibrium** is a price $P^*$ at which the quantity demanded equals the quantity supplied, $Q_d(P^*) = Q_s(P^*)$, and the common quantity $Q^*$ is the equilibrium quantity. At a price above $P^*$ there is a **surplus**, with $Q_s > Q_d$. At a price below it there is a **shortage**, with $Q_d > Q_s$.

A change in the good's own price causes a **movement along** a curve: the quantity demanded or supplied changes and the curve stays put. A change in anything else (income, tastes, the price of a related good, the number of buyers, input costs, technology) changes $d_0$ or $s_0$ or the slopes, and the curve itself moves: a **shift** of the curve. In plain words, price moves you along the curve, and everything else moves the curve.

The **market demand** is the sum of all the individual buyers' demands: at each price, add the quantities. In plain words, it is a sum in the horizontal direction.

## How to do it

### Why price goes on the vertical axis

If $Q$ is a function of $P$, the usual rule would put $P$ on the horizontal axis. Economics draws it the other way. The reason is use: the inverse functions $P_d(Q)$ and $P_s(Q)$ answer "what is the $Q$-th unit worth to a buyer or cost a seller?", and the areas between them and a price line are surpluses, in dollars, as the [next lesson](04-surplus-and-market-interventions.md) shows. The consequence for reading graphs is that the slope of the drawn line is $\frac{dP}{dQ}$, the reciprocal of the coefficient in the equation. For $Q_d = 120 - 20P$ the drawn slope is $-\frac{1}{20}$, not $-20$. A drawn line that looks flat is a quantity that responds a lot to price.

### Solving for the equilibrium

1. Write the demand and supply functions, with units. Check the signs against the laws of demand and supply.
2. Set $Q_d = Q_s$ and solve for $P^*$.
3. Put $P^*$ in either function to get $Q^*$.
4. Check by putting $P^*$ in both functions. They must give the same $Q$.
5. Check one price on each side: above $P^*$ there should be a surplus and below it a shortage.
6. For piecewise curves, check that $P^*$ lies in the region whose formula you used.

*Theorem 1 (linear equilibrium).* If $d_1 + s_1 > 0$, the linear model has exactly one equilibrium,

$$
P^* = \frac{d_0 - s_0}{d_1 + s_1}, \qquad Q^* = \frac{d_0 s_1 + d_1 s_0}{d_1 + s_1}.
$$

It has a positive price exactly when $d_0 > s_0$.

What we know: the two equations, and that setting them equal gives one linear equation in $P$. What we want: $P^*$ and $Q^*$ in terms of the four parameters. The plan is to solve for $P$, then substitute.

*Proof.* Setting $d_0 - d_1 P = s_0 + s_1 P$ and collecting the $P$ terms gives $d_0 - s_0 = (d_1 + s_1)P$, so $P^* = \frac{d_0 - s_0}{d_1 + s_1}$, the only solution because $d_1 + s_1 \ne 0$. Then

$$
Q^* = d_0 - d_1 P^* = \frac{d_0(d_1 + s_1) - d_1(d_0 - s_0)}{d_1 + s_1} = \frac{d_0 s_1 + d_1 s_0}{d_1 + s_1}.
$$

The price is positive exactly when the numerator is, since the denominator is. $\blacksquare$

Look back: the numerator $d_0 - s_0$ is the gap between what buyers would want and what sellers would offer at a price of zero, and the denominator $d_1 + s_1$ is how fast that gap closes as the price rises. A big gap makes a high price, and a fast-closing gap makes a low one. Example 1 puts numbers into the formula.

### Comparative statics

A parameter shift changes the equilibrium by a computable amount. Differentiate the formulas of Theorem 1.

*Theorem 2 (comparative statics, linear model).*

$$
\frac{\partial P^*}{\partial d_0} = \frac{1}{d_1 + s_1} > 0, \qquad \frac{\partial Q^*}{\partial d_0} = \frac{s_1}{d_1 + s_1} \in (0, 1),
$$

$$
\frac{\partial P^*}{\partial s_0} = -\frac{1}{d_1 + s_1} < 0, \qquad \frac{\partial Q^*}{\partial s_0} = \frac{d_1}{d_1 + s_1} \in (0, 1).
$$

In words: when demand rises (larger $d_0$), the equilibrium price and quantity both rise. When supply rises (larger $s_0$), the price falls and the quantity rises. Because the model is linear, the formulas are exact for any size of change: a change $\Delta d_0$ changes the price by $\frac{\Delta d_0}{d_1 + s_1}$ and the quantity by $\frac{s_1 \Delta d_0}{d_1 + s_1}$.

What we know: the explicit formulas of Theorem 1, which are quotients of linear functions of each parameter. What we want: the signs and sizes of the effects. The plan is to differentiate each formula with respect to one parameter, holding the others fixed (a partial derivative, written $\partial$; see [partial derivatives](../../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md)).

*Proof.* In $P^* = \frac{d_0 - s_0}{d_1 + s_1}$ the denominator doesn't contain $d_0$ or $s_0$, so $\frac{\partial P^*}{\partial d_0} = \frac{1}{d_1 + s_1}$ and $\frac{\partial P^*}{\partial s_0} = -\frac{1}{d_1 + s_1}$. In $Q^* = \frac{d_0 s_1 + d_1 s_0}{d_1 + s_1}$ the numerator has $d_0$ with coefficient $s_1$ and $s_0$ with coefficient $d_1$, so $\frac{\partial Q^*}{\partial d_0} = \frac{s_1}{d_1 + s_1}$ and $\frac{\partial Q^*}{\partial s_0} = \frac{d_1}{d_1 + s_1}$. Since $d_1, s_1 > 0$, each fraction is positive, and $\frac{s_1}{d_1 + s_1} < 1$ and $\frac{d_1}{d_1 + s_1} < 1$. $\blacksquare$

Look back: the market doesn't pass the whole shift of $d_0$ into quantity. Part of it is absorbed by a higher price, which pushes buyers back along the new demand curve ($d_1$ of it) and pulls sellers forward ($s_1$ of it). If supply is fixed, $s_1 = 0$ (a concert with a set number of seats), then $\frac{\partial Q^*}{\partial d_0} = 0$ and all of the demand shift goes into price. In the other direction, when sellers respond a lot ($s_1$ large), most of a demand shift goes into quantity and little into price. The next lesson's elasticities say this in percent.

When both curves shift, add the two effects. The quantity change, $\frac{s_1 \Delta d_0 + d_1 \Delta s_0}{d_1 + s_1}$, is positive if both $\Delta d_0$ and $\Delta s_0$ are. The price change, $\frac{\Delta d_0 - \Delta s_0}{d_1 + s_1}$, can go either way, and is zero if the two shifts are equal. A shift of both curves in the same direction determines the change in quantity but not that of the price.

### Adding demands horizontally

Market demand is the sum of the buyers' quantities at each price, so the algebra adds the functions $Q_i(P)$, and the graph adds the curves horizontally. Adding inverse demands $P_i(Q)$ would be a mistake: it would add prices at the same quantity, which is a different thing (it is how public goods work, and it is not the market for a private good).

A buyer who is priced out buys nothing, so the formula for that buyer's demand is $Q_i = \max(0, a_i - b_i P)$: it is the line for prices up to the buyer's highest willing price and zero above. When you add, the sum changes formula at each price where a buyer drops out, and the market demand curve has a kink there.

1. Write each buyer's demand, with its zero above the price where it reaches 0 (the choke price, $P = \frac{a_i}{b_i}$).
2. List the choke prices in increasing order. They cut the price axis into regions.
3. In each region add the demands of the buyers who are still in.
4. For the equilibrium, solve $Q_d = Q_s$ in each region, and keep the answer whose price lies in that region.

## Worked examples

<div class="example" markdown>

### Example 1: the bubble tea market

A made-up market for bubble tea at a campus kiosk has demand $Q_d = 120 - 20P$ and supply $Q_s = 10P$, with $P$ in dollars and $Q$ in cups a day. Find the equilibrium and the inverse functions, and describe the market at \$3 and at \$5.

Step 1: the signs are right: demand falls with price and supply rises.

Steps 2 and 3: $120 - 20P = 10P$ gives $30P = 120$, so $P^* = 4$ and $Q^* = 10 \cdot 4 = 40$. Theorem 1 agrees: $\frac{120 - 0}{20 + 10} = 4$ and $\frac{120 \cdot 10 + 0}{30} = 40$.

Step 4: demand at \$4 is $120 - 80 = 40$ and supply is $10 \cdot 4 = 40$.

Step 5: at \$3, demand is $120 - 60 = 60$ and supply is $30$, a shortage of 30 cups. At \$5, demand is $120 - 100 = 20$ and supply is 50, a surplus of 30 cups.

The inverse functions are $P_d(Q) = \frac{120 - Q}{20} = 6 - \frac{Q}{20}$ and $P_s(Q) = \frac{Q}{10}$. The drawn slopes are $-\frac{1}{20}$ and $\frac{1}{10}$, and they cross at $Q = 40$: $6 - 2 = 4 = \frac{40}{10}$.

Check: this is the pair of solid lines in the left graph of the figure. Buyers' highest willing price is $P_d(0) = \$6$ (the choke price), and no seller will offer anything below $P_s(0) = \$0$.

</div>

<div class="example" markdown>

### Example 2: comparative statics

Start from Example 1 ($d_0 = 120$, $d_1 = 20$, $s_0 = 0$, $s_1 = 10$). (a) Income rises, and demand becomes $Q_d = 150 - 20P$. (b) Instead, a cheaper machine raises supply to $Q_s = 30 + 10P$. (c) Both happen. Find each new equilibrium.

(a) A shift of $\Delta d_0 = 30$ changes the price by $\frac{30}{30} = 1$ and the quantity by $\frac{10 \cdot 30}{30} = 10$. The new equilibrium is $(P, Q) = (5, 50)$. Direct check: $150 - 20P = 10P$ gives $P = 5$, and $10 \cdot 5 = 50$. This is the dashed line in the left graph.

(b) A shift $\Delta s_0 = 30$ changes the price by $-\frac{30}{30} = -1$ and the quantity by $\frac{20 \cdot 30}{30} = 20$. The new equilibrium is $(3, 60)$. Direct check: $120 - 20P = 30 + 10P$ gives $P = 3$, and $120 - 60 = 60$.

(c) With both shifts, the price changes by $\frac{30 - 30}{30} = 0$ and the quantity by $\frac{10 \cdot 30 + 20 \cdot 30}{30} = 30$. The new equilibrium is $(4, 70)$. Direct check: $150 - 20P = 30 + 10P$ gives $P = 4$, and $150 - 80 = 70$.

Check: the quantity rose in all three cases, and the price moved in the direction the theorem says (up, down, unchanged). The sizes agree with the direct solutions.

</div>

<div class="example" markdown>

### Example 3: a buyer drops out

Two buyers have demands $Q_1 = 10 - 2P$ (for prices up to \$5, and 0 above) and $Q_2 = 16 - 2P$ (up to \$8). Supply is $Q_s = 2P - 6$ (up to the price \$3 below which nothing is offered, so $Q_s = 0$ below that). Find the market demand and the equilibrium.

Step 1: the choke prices are 5 and 8. They cut prices into $0 \le P \le 5$, $5 < P \le 8$ and $P > 8$.

Step 2: for $P \le 5$ both buy: $Q_d = (10 - 2P) + (16 - 2P) = 26 - 4P$. For $5 < P \le 8$ only buyer 2 buys: $Q_d = 16 - 2P$. For $P > 8$, $Q_d = 0$. At $P = 5$ both formulas give 6, so the curve is continuous, with a kink at $(Q, P) = (6, 5)$ that is the right graph of the figure.

Step 3: try the upper region first: $16 - 2P = 2P - 6$ gives $P = 5.5$, and $5 < 5.5 \le 8$, so it is in the region. Then $Q = 16 - 11 = 5$. In the lower region: $26 - 4P = 2P - 6$ gives $P = \frac{16}{3} \approx 5.33$, which is not in $P \le 5$, so it is not an equilibrium.

Check: at $P = 5.5$, buyer 1 wants $10 - 11 < 0$, so 0, buyer 2 wants $16 - 11 = 5$, and supply is $11 - 6 = 5$. Buyer 1 is priced out, which is why the answer comes from the upper formula.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

Demand is $Q_d = 90 - 6P$ and supply is $Q_s = -10 + 4P$ (no supply below \$2.50). Find the equilibrium. Then income rises so that $d_0$ goes up by 20, and find the new equilibrium using Theorem 2 and then directly.

Step 1: set $90 - 6P = -10 + 4P$.

Do Step 2 and Step 3 yourself, check, and then do the shift.

<details class="solution" markdown>
<summary>Finish</summary>

$100 = 10P$, so $P^* = 10$ and $Q^* = 90 - 60 = 30$. Check: $-10 + 40 = 30$.

For the shift, $d_1 + s_1 = 10$, so the price rises by $\frac{20}{10} = 2$ and the quantity by $\frac{4 \cdot 20}{10} = 8$. The new equilibrium is $(12, 38)$. Directly: $110 - 6P = -10 + 4P$ gives $P = 12$, and $110 - 72 = 38$ and $-10 + 48 = 38$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the difference between a change in quantity demanded and a change in demand. When the price of a good falls, buyers buy more of it: that is a movement along the demand curve, and economists call it an increase in the quantity demanded. "Demand increased" means the whole curve moved, because of something other than the good's own price. Write down what changed before you decide which curve moves.

</div>

<div class="warning" markdown>

Watch out: the slope on the graph is not the coefficient in the equation. For $Q_d = 120 - 20P$ the line on the graph has slope $-\frac{1}{20}$. Comparing slopes of two drawn curves compares the reciprocals of the $d_1$ and $s_1$ values, so the steeper drawn curve is the one that responds less to price.

</div>

<div class="warning" markdown>

Watch out: don't add demands vertically. At each price, the market demand adds quantities. Adding $\frac{10 - Q}{2}$ and $\frac{16 - Q}{2}$ gives a number that is not the price that anybody pays. If you want the market demand as a function of quantity, add the quantity formulas first and invert.

</div>

<div class="warning" markdown>

Watch out for the region check. If you solve $Q_d = Q_s$ with a formula that doesn't apply at the price you get, the answer is not an equilibrium. In Example 3 the lower formula gave $P = 5.33$, which is outside the range where it holds. Always substitute the price back into each buyer's $\max(0, \cdot)$.

</div>

A negative equilibrium price, which Theorem 1 gives when $d_0 < s_0$, means that buyers value the good at less than the lowest price at which any seller would sell: there is no trade at a positive price, and the market does not exist. Also the formulas assume positive quantities. A line such as $Q_s = -10 + 4P$ is meant only for $P \ge 2.5$, where it is non-negative.

## Tricks and shortcuts

For a linear model, skip the substitution and use the formula: $P^* = \frac{d_0 - s_0}{d_1 + s_1}$. A quick check on any answer: the shortage $Q_d - Q_s$ at a price $P$ is $(d_0 - s_0) - (d_1 + s_1)P$, which is positive below $P^*$, zero at $P^*$ and negative (a surplus) above it.

For a shift in the inverse form, a demand shift of $\Delta d_0$ in quantity at each price is a shift of $\frac{\Delta d_0}{d_1}$ in price at each quantity. In Example 2(a), the quantity shift of 30 is a price shift of $\frac{30}{20} = 1.5$ upward, from $P = 6 - \frac{Q}{20}$ to $P = 7.5 - \frac{Q}{20}$. The price of the equilibrium rises by less than that, $\frac{20}{30}$ of it, because the supply curve slopes upward.

To check the direction of a comparative-statics answer without algebra, sketch the shift: demand right means a higher price and a higher quantity, and supply right means a lower price and a higher quantity. If the algebra says otherwise, recheck it.

## In code

The equilibrium formula, the three shifts of Example 2, and the piecewise market demand of Example 3 are a few lines. Fractions keep the answers exact.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction as F

def equilibrium(d0, d1, s0, s1):
    """Qd = d0 - d1*P and Qs = s0 + s1*P. Returns (P*, Q*)."""
    p = F(d0 - s0, d1 + s1)
    return p, d0 - d1 * p

print(equilibrium(120, 20, 0, 10))
# (Fraction(4, 1), Fraction(40, 1))

# Comparative statics: a demand shift of +30, then a supply shift of +30, then both
base = equilibrium(120, 20, 0, 10)
for name, args in [("demand +30", (150, 20, 0, 10)),
                   ("supply +30", (120, 20, 30, 10)),
                   ("both +30", (150, 20, 30, 10))]:
    p, q = equilibrium(*args)
    print(name, "price change", p - base[0], "quantity change", q - base[1])
# demand +30 price change 1 quantity change 10
# supply +30 price change -1 quantity change 20
# both +30 price change 0 quantity change 30

# Market demand: add the quantities of two buyers at each price
def market_demand(p):
    q1 = max(0, 10 - 2 * p)
    q2 = max(0, 16 - 2 * p)
    return q1 + q2

def supply(p):
    return max(0, 2 * p - 6)

# Find the price where market demand equals supply by checking a fine grid of prices
best = min((abs(market_demand(F(k, 100)) - supply(F(k, 100))), F(k, 100)) for k in range(0, 1000))
print(best[1], market_demand(best[1]))
# 11/2 5
```

</details>

## FAQ

### Why does price go on the vertical axis when it is the input?

Because the graph is meant to show prices as heights: the height of the demand curve at $Q$ is what the $Q$-th buyer will pay, and the height of the supply curve is what the $Q$-th seller needs. That reading makes surpluses areas in dollars. The cost is that the drawn curve is the inverse function, and its slope is the reciprocal of what the equation shows.

### Does the market really get to the equilibrium?

The model says that at a price above $P^*$ there is a surplus, so sellers with unsold goods have a reason to cut the price, and at a price below $P^*$ there is a shortage, so buyers have a reason to bid it up. In this story the price moves toward $P^*$. Real markets can be slow, and some prices are set by rules, which the [next lesson](04-surplus-and-market-interventions.md) studies. The equilibrium is where the pressure to change disappears, not a promise about what happens.

### Can a shift and a movement happen together?

Yes, and they do. If income rises, the demand curve shifts right. The old price now has a shortage, so the price rises, and the equilibrium moves up along the supply curve (a movement: sellers offer more) while buyers move up along the new demand curve (also a movement: they buy less than they wanted at the old price). One shift is followed by two movements. Keep track of which curve each thing moves.

### What if the demand and supply lines never cross for a positive price?

That happens when $d_0 \le s_0$. At a price of zero, sellers would already offer at least as much as buyers want, so no price above zero clears the market. For a good with a positive price in reality, the parameters must satisfy $d_0 > s_0$.

## Practice

### Warm-up

1\. Demand is $Q_d = 80 - 5P$ and supply is $Q_s = 3P$. Find the equilibrium and the inverse demand function.

<details class="solution" markdown>
<summary>Solution</summary>

Set $80 - 5P = 3P$, so $8P = 80$ and $P^* = 10$, and $Q^* = 30$. The inverse demand is $P = \frac{80 - Q}{5} = 16 - \frac{Q}{5}$.

Check: demand at \$10 is $80 - 50 = 30$ and supply is $30$. Also $P_d(30) = 16 - 6 = 10$.

</details>

2\. For each event in the coffee market, say whether it shifts demand, shifts supply, or moves along a curve, and which way: (a) the price of coffee falls; (b) incomes rise, and coffee is a normal good (more is bought when income rises); (c) a frost raises the cost of growing beans; (d) the price of tea, a substitute, rises.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Movement along the demand curve: the quantity demanded rises. (b) Demand shifts right. (c) Supply shifts left, because at each price sellers offer less. (d) Demand for coffee shifts right, because some tea drinkers switch.

Check: only (a) is caused by the price of coffee itself, and only that one is a movement. The others change something besides that price.

</details>

3\. Demand is $Q_d = 120 - 20P$ and supply is $Q_s = 4P - 8$. Write both inverse functions, and find where the supply line crosses the price axis.

<details class="solution" markdown>
<summary>Solution</summary>

Demand: $P = 6 - \frac{Q}{20}$. Supply: $4P = Q + 8$, so $P = 2 + \frac{Q}{4}$. The supply line crosses the price axis at $Q = 0$, where $P = 2$: nothing is offered below \$2. Equilibrium: $120 - 20P = 4P - 8$ gives $128 = 24P$, so $P^* = \frac{16}{3} \approx 5.33$ and $Q^* = 120 - \frac{320}{3} = \frac{40}{3} \approx 13.33$.

Check: $4 \cdot \frac{16}{3} - 8 = \frac{40}{3}$. Also $6 - \frac{40/3}{20} = 6 - \frac{2}{3} = \frac{16}{3}$ and $2 + \frac{40/3}{4} = \frac{16}{3}$, so both inverse functions agree at the equilibrium.

</details>

### Standard

4\. Demand is $Q_d = 100 - 4P$ and supply is $Q_s = 10 + P$. (a) Find the equilibrium. (b) Demand rises by 15 units at every price. Use Theorem 2 to find the new price and quantity, and check directly.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $100 - 4P = 10 + P$ gives $90 = 5P$, so $P^* = 18$ and $Q^* = 100 - 72 = 28$. Check: $10 + 18 = 28$.

(b) Here $d_1 + s_1 = 5$. The price rises by $\frac{15}{5} = 3$ and the quantity by $\frac{1 \cdot 15}{5} = 3$, to $(21, 31)$. Directly: $115 - 4P = 10 + P$ gives $P = 21$, and $115 - 84 = 31 = 10 + 21$.

</details>

5\. Buyer A has demand $Q_A = 12 - 3P$ for prices up to \$4, and buyer B has $Q_B = 20 - 2P$ for prices up to \$10. Supply is $Q_s = 3P - 4$. (a) Write the market demand in two regions. (b) Where is the kink? (c) Find the equilibrium.

<details class="solution" markdown>
<summary>Solution</summary>

(a) For $0 \le P \le 4$ both buy, $Q_d = 32 - 5P$. For $4 < P \le 10$ only B buys, $Q_d = 20 - 2P$.

(b) At $P = 4$ both formulas give 12 ($32 - 20 = 12$ and $20 - 8 = 12$), so the kink is at $(Q, P) = (12, 4)$.

(c) Lower region: $32 - 5P = 3P - 4$ gives $P = 4.5$, which is not $\le 4$, so it is not an equilibrium. Upper region: $20 - 2P = 3P - 4$ gives $P = 4.8$, which is in $(4, 10]$, so $Q = 20 - 9.6 = 10.4$.

Check: at \$4.80, A wants $12 - 14.4 < 0$, so 0, B wants 10.4, and supply is $14.4 - 4 = 10.4$.

</details>

6\. In the market $Q_d = 120 - 20P$, $Q_s = 10P$, a poor harvest cuts supply to $Q_s = -30 + 10P$. (a) Use Theorem 2 to find the changes in price and quantity. (b) Show that in the inverse form the supply curve shifts up by 3 dollars.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Here $\Delta s_0 = -30$ and $d_1 + s_1 = 30$. The price changes by $-\frac{-30}{30} = +1$, and the quantity by $\frac{20 \cdot (-30)}{30} = -20$. The new equilibrium is $(5, 20)$. Check: $120 - 100 = 20$ and $-30 + 50 = 20$.

(b) The old inverse supply is $P = \frac{Q}{10}$ and the new one is $P = \frac{Q + 30}{10} = \frac{Q}{10} + 3$, a shift up of \$3, which is $\frac{30}{s_1} = \frac{30}{10}$.

Check: the price of the equilibrium rose by \$1, a third of the \$3 shift, because demand slopes downward and buyers pull back.

</details>

### Challenge

7\. In the linear model, a demand shift of $\Delta d_0$ moves the inverse demand curve up by $\frac{\Delta d_0}{d_1}$ at every quantity. Show that the equilibrium price rises by the fraction $\frac{d_1}{d_1 + s_1}$ of that vertical shift, and check it for $d_1 = 20$, $s_1 = 10$ and $\Delta d_0 = 30$.

<details class="solution" markdown>
<summary>Solution</summary>

By Theorem 2 the price rises by $\frac{\Delta d_0}{d_1 + s_1}$. The vertical shift is $\frac{\Delta d_0}{d_1}$. The ratio is

$$
\frac{\Delta d_0 / (d_1 + s_1)}{\Delta d_0 / d_1} = \frac{d_1}{d_1 + s_1},
$$

which is less than 1 because $s_1 > 0$.

For the numbers: the vertical shift is $\frac{30}{20} = 1.5$, the price rises by $\frac{30}{30} = 1$, and $\frac{1}{1.5} = \frac{2}{3} = \frac{20}{30}$.

Check: this agrees with Example 2(a), where the line moved from $P = 6 - \frac{Q}{20}$ to $P = 7.5 - \frac{Q}{20}$ (up 1.5), and the equilibrium price went from 4 to 5. If supply were fixed ($s_1 = 0$) the fraction would be 1: the price would rise by the whole vertical shift.

</details>

8\. (Reviews [composition and inverse functions](../../03-high-school/03-functions/05-composition-and-inverse-functions.md).) Demand is not always linear. Suppose $Q_d = \frac{100}{P^2}$ for $P > 0$ and $Q_s = 5P$. (a) Find the inverse demand function. (b) Find the equilibrium. (c) Why does the inverse exist?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Solve $Q = \frac{100}{P^2}$ for $P$: $P^2 = \frac{100}{Q}$, and since $P > 0$, $P = \frac{10}{\sqrt{Q}}$.

(b) Set $\frac{100}{P^2} = 5P$, so $P^3 = 20$ and $P^* = 20^{1/3} \approx 2.714$. Then $Q^* = 5P^* \approx 13.57$.

(c) For $P > 0$ the function $\frac{100}{P^2}$ is strictly decreasing, so each quantity comes from only one price, and it passes the horizontal line test. (Without $P > 0$, the prices $P$ and $-P$ would give the same quantity.)

Check: $\frac{100}{2.714^2} = \frac{100}{7.368} = 13.57$, and $P_d(13.57) = \frac{10}{\sqrt{13.57}} = \frac{10}{3.684} = 2.714$.

</details>

## Where this shows up

- The next lesson, [surplus and market interventions](04-surplus-and-market-interventions.md), measures the areas between these curves and a price line, and the lesson after, [elasticity](05-elasticity.md), turns $d_1$ and $s_1$ into percent responses.
- Firms' supply curves come from their costs, which [marginal analysis with derivatives](../03-firms-and-consumers/01-marginal-analysis-with-derivatives.md) and [profit maximization and market structure](../03-firms-and-consumers/03-profit-maximization-and-market-structure.md) derive.
- In CS, the same two-curves idea sets prices in auctions and in dynamic pricing (surge pricing for rides is a price that rises when the quantity demanded passes the quantity supplied), and a load balancer that adds servers when demand rises is a supply shift.
