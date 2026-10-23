# Profit maximization and market structure

After this lesson you can find a firm's profit-maximizing output with the first- and second-order conditions, apply the shutdown rule and build a short-run supply curve, find the long-run zero-profit price, solve a monopoly with the markup rule and its deadweight loss, and solve a Cournot duopoly from the reaction functions.

Before this: [marginal analysis with derivatives](01-marginal-analysis-with-derivatives.md) and [production and cost functions](02-production-and-cost-functions.md). The cost curves of this lesson are the ones built there.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A price-taking firm has $C(q) = 100 + 2q + q^2$ and faces the price \$26. Find its output and its profit.
2. A firm's revenue is \$500, its variable cost is \$600 and its fixed cost is \$200. Should it keep operating or shut down, and what is its loss in each case?
3. A monopolist has marginal cost \$15 and faces demand with elasticity $E = -4$ at the profit-maximizing price. What is the price, and what is the markup $\frac{p - MC}{p}$?

<details class="solution" markdown>
<summary>Answers</summary>

1. $MC = 2 + 2q = 26$ gives $q = 12$. Profit is $26 \cdot 12 - (100 + 24 + 144) = 312 - 268 = 44$ dollars.
2. Operating loses $500 - 600 - 200 = -300$. Shutting down loses only the fixed cost, \$200, so it should shut down. (Revenue is below variable cost, so each unit sold loses money.)
3. $\frac{p - MC}{p} = \frac{1}{\lvert E \rvert} = \frac{1}{4}$, so $p = \frac{MC}{1 - 1/4} = \frac{15}{0.75} = 20$, a markup of 25%.

</details>

## The idea

Every firm in a first micro course is asked the same question: how much should it make? The answer in lesson 1 was to keep going while the extra unit brings in at least as much as it costs. What changes from one market to another is the revenue side. A farmer selling wheat at the world price can sell as much as they like at that price, so each extra bushel brings in the price. A utility with the only power line to a town faces the town's whole demand curve, so each extra kilowatt-hour has to be sold at a lower price to everyone, and brings in less than the price.

That one difference gives the main results of the lesson. The price taker produces where price equals marginal cost, and the cost curves decide when it shuts down and how it supplies. The monopolist produces where marginal revenue equals marginal cost, which is a smaller quantity at a higher price, and the gap between price and marginal cost is tied to the elasticity of demand. Between the two lies oligopoly, where a few firms each affect the price and each must guess the others' outputs. The simplest model of that, Cournot's, is solved here with two firms.

The calculus is the same throughout: a first-order condition, a second-order check, and the usual care with endpoints, because "produce nothing" is always an option.

## Definitions

A firm's **profit** is $\pi(q) = R(q) - C(q)$, revenue minus total cost. A firm is a **price taker** if it can sell any quantity at the market price $p$, so that $R(q) = pq$, and a market is **perfectly competitive** if its firms are price takers (many small sellers, identical goods, free entry and exit). A firm has **market power** if its output changes the price it receives. A **monopoly** is a market with a single seller, which faces the whole market demand.

The **shutdown point** is the output and price at the minimum of the average variable cost curve. The **short-run supply curve** of a price-taking firm is the quantity it chooses at each price when its fixed cost can't be avoided. In the **long run**, with free entry and exit, firms enter while profit is positive and leave while it is negative, so the market settles where profit is zero.

The **markup** of a seller is $\frac{p - MC}{p}$, which is also called the Lerner index. The **deadweight loss** of a monopoly is the total surplus (consumer plus producer) that is lost because it produces less than the competitive quantity. In plain words, it is the value of the trades that would benefit both sides and don't happen.

In a **Cournot duopoly** two firms choose their quantities $q_1$ and $q_2$ at the same time, and the market price is the inverse demand evaluated at $q_1 + q_2$. Firm $i$'s **reaction function** (best response) is the profit-maximizing $q_i$ for each quantity of the other firm. A **Cournot equilibrium** is a pair $(q_1^*, q_2^*)$ in which each quantity is the best response to the other.

## How to do it

### The conditions for a profit maximum

1. Write profit $\pi(q) = R(q) - C(q)$ for the market the firm is in. For a price taker $R = pq$. For a firm with market power, find $R = q\,p(q)$ from the demand curve.
2. Set $\pi'(q) = 0$, which is $MR(q) = MC(q)$. For a price taker this is $p = MC(q)$.
3. Check the second-order condition $\pi''(q) < 0$, which is $MR'(q) < MC'(q)$. For a price taker $MR' = 0$, so it reads $MC'(q) > 0$: marginal cost must be rising.
4. Compare with the endpoint $q = 0$: profit there is $-F$, the fixed cost lost. (This is the shutdown rule, below.)
5. Check by evaluating profit just on either side of the answer.

The second-order condition matters, because $p = MC$ can have two solutions. With a U-shaped marginal cost, a horizontal price line crosses it once on the falling part and once on the rising part. The first is the worst output nearby and the second is the best. Example 1 has numbers.

### The shutdown rule

*Theorem 1.* Let a price-taking firm have fixed cost $F$ that can't be avoided in the short run, and variable cost $VC(q)$. Compared with producing nothing (profit $-F$), producing $q > 0$ is better exactly when

$$
pq - VC(q) \ge 0, \qquad\text{that is,}\qquad p \ge AVC(q).
$$

So the firm produces only if the price is at least the minimum of the average variable cost, and its short-run supply is the part of the marginal cost curve at or above that minimum.

What we know: producing $q$ gives profit $pq - VC(q) - F$ and producing nothing gives $-F$. What we want: the condition under which the first is at least the second, and what it says about the price. The plan is to subtract, divide by $q$, and recall where $MC$ meets $AVC$.

*Proof.* The profit from producing is at least the profit from shutting down when $pq - VC(q) - F \ge -F$, which is $pq \ge VC(q)$. Dividing by $q > 0$ gives $p \ge AVC(q)$. The firm can find such a $q$ only if $p$ is at least the smallest value of $AVC$. By the average-versus-marginal theorem of the last lesson, the minimum of $AVC$ is at the output where $MC = AVC$, so the lowest price at which the firm operates is $p = MC = AVC_{\min}$. Above it, the profit-maximizing output solves $p = MC(q)$ on the rising part of the marginal cost curve, so the supply curve is that part. $\blacksquare$

Look back: the fixed cost left the argument on both sides. That is why the rule uses AVC and not average cost. A firm may lose money at a price between $AVC_{\min}$ and $AC_{\min}$ and still be right to produce, because the revenue above variable cost pays part of a fixed cost it owes anyway.

### Long run: zero profit

In the long run there is free entry. If $p > AC_{\min}$ a firm can make a positive profit at the output where $AC$ is lowest, so new firms enter, supply grows and the price falls. If $p < AC_{\min}$ firms lose money and leave. So the price settles at $p = AC_{\min}$, each firm produces at the bottom of its average cost curve (where $MC = AC$), and the number of firms is $n = \frac{Q_D(p)}{q}$, the market quantity divided by one firm's output.

### Monopoly and the markup rule

A monopolist's revenue is $R(q) = q\,p(q)$, and by lesson 1 its marginal revenue is $MR = p + q\,p'(q)$, below the price.

*Theorem 2 (markup rule).* A profit-maximizing monopolist with differentiable demand sets $MR = MC$ at a point where demand is elastic, $\lvert E \rvert > 1$, and its price satisfies

$$
\frac{p - MC}{p} = \frac{1}{\lvert E \rvert}.
$$

What we know: $MR = p\left(1 + \frac{1}{E}\right)$ from Theorem 4 of lesson 1, and the profit-maximizing condition $MR = MC$. What we want: the markup in terms of $E$. The plan is to substitute and solve for the markup.

*Proof.* At a maximum with $q > 0$, $MR = MC$, so $p\left(1 + \frac{1}{E}\right) = MC$. Since $E < 0$, write $\lvert E \rvert = -E$, so $1 + \frac{1}{E} = 1 - \frac{1}{\lvert E \rvert}$. Then $p - \frac{p}{\lvert E \rvert} = MC$, so $p - MC = \frac{p}{\lvert E \rvert}$, and dividing by $p$ gives the rule. Since $MC > 0$ and $p > 0$, we need $1 - \frac{1}{\lvert E \rvert} > 0$, which is $\lvert E \rvert > 1$. $\blacksquare$

Look back: the less elastic demand is, the bigger the markup. As $\lvert E \rvert \to \infty$ (buyers who switch at any price rise), the markup goes to 0 and the firm acts like a price taker. The rule is an equation in $p$ and $E$ together, because $E$ itself depends on $p$, so it gives a closed form only for special demand curves. For constant elasticity, $p = \frac{MC}{1 - 1/\lvert E \rvert}$ is the full answer. For linear demand, solve $MR = MC$ directly.

The monopolist produces less than a competitive industry with the same costs would, where the price equals the marginal cost. The trades between the two outputs, in which buyers value the good above its marginal cost, don't happen. The area between the demand curve and the marginal cost curve over that range is the deadweight loss: $DWL = \int_{q_m}^{q_c}\bigl(p(q) - MC(q)\bigr)\,dq$, where $q_m$ is the monopoly output and $q_c$ the competitive output at which $p = MC$. The lesson on [surplus and market interventions](../02-markets/04-surplus-and-market-interventions.md) develops this idea of lost surplus for taxes and price controls.

### A Cournot duopoly

Let inverse demand be $P = a - b(q_1 + q_2)$ and let each firm have constant marginal cost $c < a$. Firm 1's profit is $\pi_1 = \bigl(a - b(q_1 + q_2) - c\bigr)q_1$.

*Theorem 3.* Firm 1's best response to $q_2$ is $q_1 = \frac{a - c - bq_2}{2b}$, and by symmetry firm 2's is $q_2 = \frac{a - c - bq_1}{2b}$. The Cournot equilibrium is

$$
q_1^* = q_2^* = \frac{a - c}{3b}, \qquad P^* = \frac{a + 2c}{3}.
$$

What we know: each firm takes the other's quantity as given and maximizes profit by calculus. What we want: the pair of quantities that are best responses to each other. The plan is to find one reaction function, use symmetry and solve.

*Proof.* Differentiate $\pi_1 = (a - c - bq_2)q_1 - bq_1^2$ with respect to $q_1$ (holding $q_2$ fixed): $\frac{\partial\pi_1}{\partial q_1} = a - c - bq_2 - 2bq_1 = 0$, so $q_1 = \frac{a - c - bq_2}{2b}$. The second derivative is $-2b < 0$, so this is the maximum. Firm 2's problem is the same with the roles swapped. In an equilibrium both equations hold. Subtracting them gives $q_1 - q_2 = \frac{1}{2}(q_1 - q_2)$, which forces $q_1 = q_2$. Call it $q$: $q = \frac{a - c - bq}{2b}$, so $2bq + bq = a - c$ and $q = \frac{a - c}{3b}$. The price is $a - b\cdot\frac{2(a - c)}{3b} = \frac{a + 2c}{3}$. $\blacksquare$

Look back at the numbers: each firm produces a third of the competitive quantity $\frac{a - c}{b}$, so the two together produce two thirds of it, more than the monopoly half and less than the competitive whole. The price is between the monopoly and the competitive price too. Each firm's output reduces the other's price, but neither firm counts that cost, so they overproduce compared with a cartel. A Cournot equilibrium is a Nash equilibrium; [game theory and Nash equilibrium](../04-more-tools/04-game-theory-and-nash-equilibrium.md) treats the general idea.

## Worked examples

<div class="example" markdown>

### Example 1: a price taker, with two solutions to p = MC

A firm has $C(q) = 80 + 15q - 0.6q^2 + 0.02q^3$ (the cost of lessons 1 and 2, made up) and the market price is \$12. Find the best output and profit, and decide whether to operate.

Step 1: revenue is $12q$, so $\pi(q) = 12q - C(q)$.

Step 2: $MC = 15 - 1.2q + 0.06q^2$. Setting $MC = 12$ gives $0.06q^2 - 1.2q + 3 = 0$, so $q^2 - 20q + 50 = 0$ and $q = 10 \pm 5\sqrt{2}$, that is, $q \approx 2.93$ or $q \approx 17.07$.

Step 3: the second-order condition is $MC'(q) = -1.2 + 0.12q > 0$. At $q = 2.93$ it is $-0.85$ (marginal cost falling, a minimum of profit) and at $q = 17.07$ it is $+0.85$ (a maximum).

Step 4: the profit at 17.07 is $12 \cdot 17.07 - C(17.07) \approx 204.85 - 260.71 = -55.86$. A loss. Shutting down costs the fixed \$80. Since $p = 12 \ge AVC(17.07) = 15 - 10.24 + 5.83 = 10.59$, producing is better, and the loss shrinks from \$80 to \$55.86. Equivalently, the revenue above variable cost is $pq - VC = 24.14 > 0$, and it pays part of the \$80.

Step 5, the check: $\pi(2.93) \approx -84.14$ (worse than shutting down), $\pi(10) = -70$, $\pi(17.07) \approx -55.86$ and $\pi(20) = -60$. The best is at 17.07. At the price \$10, which is below the minimum of AVC (\$10.50), the best output on the rising part is 14.08 with a loss of \$87.28, worse than \$80, so the firm shuts down.

![Cost curves of a price-taking firm against output: marginal cost in grey and then thick red where it rises above the average variable cost, average variable cost in blue with its lowest point at q equal to 15 and price 10.5 marked as the shutdown point, and average cost in green with its lowest point at q equal to 20 and price 15 marked as the break-even point. A dashed orange line at the price 12 crosses the marginal cost at q equal to 2.93 (labelled the worst) and at q equal to 17.07 (labelled the best, where marginal cost is rising).](../../assets/figures/07-economics-math/profit-maximization-and-market-structure-competition.svg)

</div>

<div class="example" markdown>

### Example 2: the supply curve and the long-run price

For the firm of Example 1, find the short-run supply curve, and then the long-run price and the number of firms if market demand is $Q_D = 1000 - 20p$.

The firm supplies along the rising part of $MC$, from the shutdown point: $MC = 15 - 1.2q + 0.06q^2 = p$. Solving for the larger root,

$$
q(p) = 10 + \frac{\sqrt{0.24p - 2.16}}{0.12}, \qquad p \ge 10.5.
$$

At $p = 10.5$ the square root is $0.6$ and $q = 15$, the minimum of AVC. At $p = 12$, $q \approx 17.07$. At $p = 15$, $\sqrt{1.44} = 1.2$ and $q = 20$. At $p = 18$, $q \approx 22.25$. For $p < 10.5$ the supply is zero.

In the long run, free entry drives the price to the minimum of the average cost, which is at $q = 20$ with $AC = 15$ (setting $MC = AC$ in lesson 1's Example 5 gave the same point). Profit there is $15 \cdot 20 - C(20) = 300 - 300 = 0$. At $p = 15$ the market buys $Q_D = 1000 - 300 = 700$ units, and with each firm making 20 the industry has $\frac{700}{20} = 35$ firms.

Check: $C(20) = 80 + 300 - 240 + 160 = 300$, so profit is zero. At $p = 18$ the firm earns more than zero (it makes 22.25 units at price 18 and average cost about \$15.15, a profit of about \$63), which would attract entrants, and the price falls back to 15. The supply formula also checks: $MC(22.25) = 18.0$.

</div>

<div class="example" markdown>

### Example 3: a monopoly and its deadweight loss

A monopolist (made up) faces $p = 100 - q$ and has $C(q) = 200 + 10q + 0.25q^2$. Find its output, price, profit and the deadweight loss, and check the markup rule.

Step 1: $R = 100q - q^2$, so $MR = 100 - 2q$, and $MC = 10 + 0.5q$.

Step 2: $MR = MC$ gives $100 - 2q = 10 + 0.5q$, so $2.5q = 90$ and $q_m = 36$. The price is $p_m = 64$, and $MC(36) = 28$.

Step 3: the second-order condition is $\pi'' = MR' - MC' = -2 - 0.5 < 0$, a maximum. The profit is $R - C = 2304 - (200 + 360 + 324) = 1420$.

Step 4: a competitive industry with the same marginal cost sets $p = MC$: $100 - q = 10 + 0.5q$, so $q_c = 60$ and $p_c = 40$. The deadweight loss is the triangle between demand and marginal cost from $q = 36$ to $q = 60$, whose height at $q = 36$ is $64 - 28 = 36$:

$$
DWL = \int_{36}^{60}\bigl((100 - q) - (10 + 0.5q)\bigr)\,dq = \frac{1}{2}\cdot 24\cdot 36 = 432.
$$

Step 5, the check: the elasticity at the optimum is $E = \frac{dq}{dp}\frac{p}{q} = -1\cdot\frac{64}{36} = -\frac{16}{9}$, so $\frac{1}{\lvert E \rvert} = \frac{9}{16} = 0.5625$, and the markup is $\frac{64 - 28}{64} = 0.5625$. They match. Also $\lvert E \rvert > 1$, as required.

![Demand in green, marginal revenue in blue and marginal cost in red against quantity. Marginal revenue meets marginal cost at q equal to 36 and marginal cost 28; the monopoly price on the demand curve at that quantity is 64. The demand and marginal cost curves cross at the competitive point q equal to 60, price 40. The triangle between the monopoly quantity and the competitive point, bounded by demand and marginal cost, is shaded and labelled deadweight loss equal to 432.](../../assets/figures/07-economics-math/profit-maximization-and-market-structure-monopoly.svg)

</div>

<div class="example" markdown>

### Example 4: a Cournot duopoly

Two firms (made up) face $P = 100 - (q_1 + q_2)$ with the same constant marginal cost \$10, so $a = 100$, $b = 1$ and $c = 10$. Find the equilibrium.

Firm 1's profit is $(90 - q_1 - q_2)q_1$, and setting the derivative with respect to $q_1$ to zero gives $90 - 2q_1 - q_2 = 0$, so the reaction function is $q_1 = 45 - \frac{q_2}{2}$. By symmetry $q_2 = 45 - \frac{q_1}{2}$. Substituting, $q_1 = 45 - \frac{1}{2}\left(45 - \frac{q_1}{2}\right) = 22.5 + \frac{q_1}{4}$, so $\frac{3}{4}q_1 = 22.5$ and $q_1 = q_2 = 30$.

The price is $P = 100 - 60 = 40$, and each firm's profit is $(40 - 10) \cdot 30 = 900$.

Compare with the monopoly and the competitive outcome for the same demand and cost: a monopolist produces $\frac{a - c}{2b} = 45$ at price 55 and makes a profit of $45 \cdot 45 = 2025$, and a competitive industry produces 90 at price 10. The Cournot total is 60 at price 40.

Check: if firm 2 stays at 30, firm 1's best response is $45 - 15 = 30$, so neither firm wants to change. Deviating to $q_1 = 35$ gives a profit of $(100 - 65 - 10) \cdot 35 = 875 < 900$, and to $q_1 = 25$ gives $(100 - 55 - 10) \cdot 25 = 875$. The two firms together earn 1,800 here, less than the 2,025 of a monopoly: they would gain by cooperating, but each has an incentive to produce more.

</div>

<div class="example" markdown>

### Example 5: a monopoly with constant marginal cost (finish it yourself)

A monopolist faces $p = 90 - 3q$ and has constant marginal cost 18 (made up). Find $q$, $p$ and the profit. Check the markup rule, and find the competitive quantity and the deadweight loss.

<details class="solution" markdown>
<summary>Finish</summary>

$MR = 90 - 6q = 18$ gives $q = 12$ and $p = 54$. The profit (ignoring any fixed cost) is $(54 - 18) \cdot 12 = 432$.

The markup is $\frac{54 - 18}{54} = \frac{2}{3}$. The demand $q = 30 - \frac{p}{3}$ has $\frac{dq}{dp} = -\frac{1}{3}$, so $E = -\frac{1}{3}\cdot\frac{54}{12} = -1.5$ and $\frac{1}{\lvert E \rvert} = \frac{2}{3}$. It matches.

The competitive quantity solves $90 - 3q = 18$, so $q_c = 24$. The deadweight loss is $\frac{1}{2}(24 - 12)(54 - 18) = 216$.

Check: the deadweight loss is half the monopoly profit, $\frac{432}{2} = 216$, as for every linear demand with constant marginal cost (problem 7).

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: setting $p = MC$ for a monopolist. The rule $p = MC$ holds only for a price taker. A firm with market power sets $MR = MC$ and charges the price on the demand curve at that quantity, which is above $MC$. In Example 3, $p = 64$ and $MC = 28$.

</div>

<div class="warning" markdown>

Watch out: using average cost in the shutdown rule. A firm that loses money at a price between $AVC_{\min}$ and $AC_{\min}$ should still produce in the short run, because shutting down loses the whole fixed cost. In Example 1 the firm loses \$55.86 by producing and \$80 by shutting down.

</div>

<div class="warning" markdown>

Watch out: taking the first solution of $p = MC$. When marginal cost is U-shaped, the equation has two roots, and only the one on the rising part is a maximum. At $q = 2.93$ in Example 1 the firm does worse than by closing.

</div>

<div class="warning" markdown>

Watch out: measuring the deadweight loss against the wrong curve. The triangle lies between demand and marginal cost, from the monopoly quantity to the competitive quantity. Using marginal revenue as its lower edge gives a wrong area that doesn't have an economic meaning. Also the monopoly profit rectangle is not part of the loss: it moves from buyers to the seller.

</div>

<div class="warning" markdown>

Watch out: reading the markup rule as a formula for $p$ without noticing that $E$ depends on $p$. For linear demand the elasticity changes along the curve, so the rule is a check at the answer. Solve $MR = MC$ first, and then confirm with $E$ (Example 3).

</div>

<div class="warning" markdown>

Watch out: forgetting that a Cournot firm takes the other's quantity as fixed when it differentiates. The derivative of firm 1's profit is taken with $q_2$ held constant, and then both equations are solved together. Substituting $q_2 = q_1$ before differentiating gives the monopoly answer instead.

</div>

A monopolist does not operate on the inelastic part of its demand curve: there $MR < 0$ and, with $MC > 0$, an extra unit loses money. And the monopoly has no supply curve, since the output depends on the whole demand curve and not on the price alone. It is also a standard error to say that a monopolist can charge any price. It picks the quantity, and the demand curve then gives the price it can get.

## Tricks and shortcuts

For linear demand $p = a - bq$ and constant marginal cost $c$, the monopoly answer is quick: $q_m = \frac{a - c}{2b}$, which is half the competitive quantity $\frac{a - c}{b}$, and $p_m = \frac{a + c}{2}$, halfway between the demand intercept and the marginal cost. The profit is $\frac{(a - c)^2}{4b}$ and the deadweight loss is $\frac{(a - c)^2}{8b}$, half of the profit.

For Cournot with $n$ identical firms, each produces $\frac{a - c}{(n + 1)b}$, so the industry produces $\frac{n}{n + 1}$ of the competitive quantity. With $n = 1$ you get the monopoly and as $n$ grows you approach perfect competition. The price is $\frac{a + nc}{n + 1}$.

To find a supply curve from a cost function, set $MC = p$ on the rising part and add the shutdown condition. The minimum of AVC can be found with $MC = AVC$ (cancel the matching terms).

The three prices to know for a U-shaped cost curve are the shutdown price (minimum of AVC), the long-run price (minimum of AC) and anything in between, where the firm produces at a loss. The ordering is always $AVC_{\min} < AC_{\min}$ when fixed costs are positive.

## In code

Sympy confirms the two roots of $p = MC$, the profit at each, the monopoly solution and the Cournot equilibrium. The last lines let two firms respond to each other, one after the other, to see that the quantities settle at the Cournot equilibrium.

<details class="code" markdown>
<summary>In code</summary>

```python
import sympy as sp

q = sp.symbols("q", positive=True)

# Example 1: p = MC has two roots; only the one on the rising part is a maximum
C = 80 + 15 * q - sp.Rational(3, 5) * q**2 + sp.Rational(1, 50) * q**3
MC = sp.diff(C, q)
for root in sp.solve(sp.Eq(MC, 12), q):
    print(round(float(root), 2), round(float(12 * root - C.subs(q, root)), 2))
# 2.93 -84.14
# 17.07 -55.86

# Example 3: the monopoly
R = q * (100 - q)
Cm = 200 + 10 * q + q**2 / 4
qm = sp.solve(sp.Eq(sp.diff(R, q), sp.diff(Cm, q)), q)[0]
print(qm, 100 - qm, (R - Cm).subs(q, qm))
# 36 64 1420
print(sp.integrate((100 - q) - (10 + q / 2), (q, qm, 60)))
# 432

# Example 4: Cournot, with the firms responding to each other in turn
q1 = q2 = 0.0
for _ in range(40):
    q1 = 45 - q2 / 2
    q2 = 45 - q1 / 2
print(round(q1, 4), round(q2, 4))
# 30.0 30.0
```

The loop is not part of the solution method: it shows that the best responses, applied in turn, converge to the equilibrium, because each reaction function has slope $-\frac{1}{2}$, which is less than 1 in size.

</details>

## FAQ

### Why does a price taker produce where price equals marginal cost?

Because its marginal revenue is the price. By the rule $MR = MC$, it produces up to the point where the next unit would cost as much as it sells for. If $p > MC$ the next unit earns a profit, and if $p < MC$ it loses money. The second-order condition says marginal cost must be rising at that point, which is why only the upward-sloping part of $MC$ is the supply curve.

### If a firm is losing money, why keep producing?

Because the fixed cost is owed whether it produces or not. If the revenue covers the variable cost and some of the fixed cost, producing loses less than shutting down. In the long run there is no fixed cost, since the firm can leave the industry, and it must earn at least zero profit to stay. That is why the short-run rule uses $AVC$ and the long-run rule uses $AC$.

### Is a zero profit a bad thing for the firms?

No. Economic profit counts all costs, including the owner's time and the return on their capital that they could have earned elsewhere. Zero economic profit means they earn exactly what the next-best use of their resources would pay. Accounting profit, which leaves out those costs, can be positive.

### Why would a monopolist make a smaller quantity than a competitive industry?

Because to sell more it has to cut the price on everything it sells, so its marginal revenue is below the price, while a competitive firm gets the full price for each unit. It stops where $MR = MC$, which is at a lower quantity than where $p = MC$. The buyers who would have paid more than the marginal cost but less than the monopoly price are shut out, and that gives the deadweight loss.

### Is Cournot competition realistic?

It is a model with a clear assumption: firms choose quantities, such as capacity or production runs, and the price clears the market. For industries where capacity is the main decision it is a reasonable first model. When firms choose prices instead, the answer is different (the Bertrand model has a price equal to marginal cost with two firms). The first lesson to take is the pattern: more firms means lower prices and larger output.

## Practice

### Warm-up

1\. A price-taking firm has $C(q) = 50 + 10q + q^2$. (a) At the price \$30, find the output and the profit. (b) What is the lowest price at which the firm produces?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $MC = 10 + 2q = 30$ gives $q = 10$, and $MC' = 2 > 0$. The profit is $30 \cdot 10 - (50 + 100 + 100) = 50$ dollars.

(b) $AVC = 10 + q$, which is lowest at $q = 0$ with value 10, so the firm produces for any price above \$10 (supply $q = \frac{p - 10}{2}$).

Check: $\pi(9) = 270 - (50 + 90 + 81) = 49$ and $\pi(11) = 330 - (50 + 110 + 121) = 49$, both below 50.

</details>

2\. A monopolist faces $p = 60 - q$ and has constant marginal cost 12. Find its quantity and price, its profit (ignoring fixed costs), and the competitive quantity and the deadweight loss.

<details class="solution" markdown>
<summary>Solution</summary>

$MR = 60 - 2q = 12$ gives $q = 24$ and $p = 36$. The profit is $(36 - 12) \cdot 24 = 576$. The competitive quantity solves $60 - q = 12$, so $q_c = 48$. The deadweight loss is $\frac{1}{2}(48 - 24)(36 - 12) = 288$.

Check: the formulas $\frac{(a - c)^2}{4b} = \frac{48^2}{4} = 576$ and $\frac{(a - c)^2}{8b} = 288$ agree.

</details>

3\. A seller with $MC = 30$ faces demand with a constant elasticity of $-2.5$. Find its profit-maximizing price.

<details class="solution" markdown>
<summary>Solution</summary>

$\frac{p - 30}{p} = \frac{1}{2.5} = 0.4$, so $0.6p = 30$ and $p = 50$.

Check: $MR = p\left(1 - \frac{1}{2.5}\right) = 50 \cdot 0.6 = 30 = MC$.

</details>

### Standard

4\. For the cost of Example 1 and the price \$12, compute the profit at $q = 0$, $2.93$, $10$, $17.07$ and $20$. Which of them solve $p = MC$, and which is the maximum?

<details class="solution" markdown>
<summary>Solution</summary>

Using $\pi(q) = 12q - C(q)$ with $C(q) = 80 + 15q - 0.6q^2 + 0.02q^3$: $\pi(0) = -80$, $\pi(2.93) \approx -84.14$, $\pi(10) = 120 - 190 = -70$, $\pi(17.07) \approx -55.86$ and $\pi(20) = 240 - 300 = -60$.

The solutions of $p = MC$ are 2.93 and 17.07. The maximum of profit is at 17.07, with a loss of \$55.86. The point 2.93 is a local minimum: profit is lower there than at 0 on one side and 10 on the other.

Check: $\pi'' = -MC' = -(-1.2 + 0.12q)$ is $+0.85$ at 2.93 (minimum) and $-0.85$ at 17.07 (maximum).

</details>

5\. A firm has $C(q) = 100 + 4q + 0.5q^2$. (a) Find its short-run supply curve. (b) At the price \$10, find the output and the profit, and say whether the firm should operate. (c) Find the long-run price.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $MC = 4 + q$ and $AVC = 4 + 0.5q$, whose minimum is 4 at $q = 0$. So the firm supplies $q = p - 4$ for $p > 4$, and nothing below.

(b) At $p = 10$, $q = 6$ and the profit is $60 - (100 + 24 + 18) = -82$. Shutting down loses \$100, so the firm should operate.

(c) $AC = \frac{100}{q} + 4 + 0.5q$ is lowest where $MC = AC$: $q = \frac{100}{q} + 0.5q + 4 - 4$, so $0.5q = \frac{100}{q}$, $q^2 = 200$ and $q = 10\sqrt{2} \approx 14.14$. The price is $AC = 4 + 10\sqrt{2} \approx 18.14$.

Check: $MC(14.14) = 18.14$, the same value, and profit at $p = 18.14$ is $18.14 \cdot 14.14 \approx 256.57$ and $C(14.14) = 100 + 56.57 + 100 = 256.57$, so the profit is zero.

</details>

6\. Two firms with the marginal cost \$10 face $P = 100 - 2(q_1 + q_2)$. Find the Cournot equilibrium and compare it with the monopoly and the competitive outcomes.

<details class="solution" markdown>
<summary>Solution</summary>

Here $a = 100$, $b = 2$, $c = 10$. By Theorem 3, $q_1 = q_2 = \frac{90}{6} = 15$, total 30, and the price is $\frac{100 + 20}{3} = 40$. Each profit is $(40 - 10) \cdot 15 = 450$.

The monopoly produces $\frac{90}{4} = 22.5$ at price $100 - 45 = 55$ with a profit of $45 \cdot 22.5 = 1012.5$. The competitive industry produces $\frac{90}{2} = 45$ at the price 10.

Check: the reaction function $q_1 = \frac{90 - 2q_2}{4} = 22.5 - 0.5q_2$ gives $22.5 - 7.5 = 15$ at $q_2 = 15$. The two firms together earn 900, less than the monopoly's 1012.5.

</details>

### Challenge

7\. Let demand be $p = a - bq$ and marginal cost constant at $c < a$. Show that the deadweight loss of the monopoly is $\frac{(a - c)^2}{8b}$, and that it is half of the monopoly profit (before fixed cost). Apply it to $a = 100$, $b = 1$, $c = 10$.

<details class="solution" markdown>
<summary>Solution</summary>

The monopoly sets $a - 2bq = c$, so $q_m = \frac{a - c}{2b}$, and the competitive output is $q_c = \frac{a - c}{b}$. At $q_m$ the gap between the price and the marginal cost is $p_m - c = a - bq_m - c = \frac{a - c}{2}$. The deadweight loss is the triangle $\frac{1}{2}(q_c - q_m)(p_m - c) = \frac{1}{2}\cdot\frac{a - c}{2b}\cdot\frac{a - c}{2} = \frac{(a - c)^2}{8b}$. The profit is $(p_m - c)\,q_m = \frac{a - c}{2}\cdot\frac{a - c}{2b} = \frac{(a - c)^2}{4b}$, twice the loss.

For $a = 100$, $b = 1$, $c = 10$: $q_m = 45$, profit $= \frac{8100}{4} = 2025$ and the deadweight loss is $\frac{8100}{8} = 1012.5$.

Check by integration: $\int_{45}^{90}(90 - q)\,dq = \left[90q - \frac{q^2}{2}\right]_{45}^{90} = 4050 - (4050 - 1012.5) = 1012.5$.

</details>

8\. (Reviews [quadratic functions and graphs](../../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md).) A firm has revenue $R = 72q - q^2$ and cost $C = 100 + 24q + q^2$. (a) Write the profit as a quadratic and find its maximum with the vertex formula. (b) Confirm with $MR = MC$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\pi = 72q - q^2 - 100 - 24q - q^2 = -2q^2 + 48q - 100$. The vertex is at $q = -\frac{b}{2a} = -\frac{48}{-4} = 12$, and $\pi(12) = -288 + 576 - 100 = 188$.

(b) $MR = 72 - 2q$ and $MC = 24 + 2q$. Setting them equal, $4q = 48$ and $q = 12$.

Check: $\pi(11) = -242 + 528 - 100 = 186$ and $\pi(13) = -338 + 624 - 100 = 186$, both below 188. The parabola opens downward ($-2 < 0$), consistent with $MR' < MC'$.

</details>

## Where this shows up

- The next lessons turn to consumers. [Utility and indifference curves](04-utility-and-indifference-curves.md) sets up the consumer's problem, which has the same structure: choose the best affordable point. [Lagrange multipliers, utility and cost minimization](05-lagrange-multipliers-utility-and-cost-minimization.md) gives the two-input version of the firm's cost problem.
- Economics: the shutdown rule, the supply curve and zero long-run profit are the core of a first course in competitive markets, and the markup rule is the basis for pricing in industrial organization. [Game theory and Nash equilibrium](../04-more-tools/04-game-theory-and-nash-equilibrium.md) generalizes the Cournot idea.
- CS: pricing a platform with network effects, setting a cloud price when several providers compete, and two algorithms that respond to each other's moves in a repeated game all use the best-response structure of the Cournot model.
