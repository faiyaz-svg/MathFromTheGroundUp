# Marginal analysis with derivatives

After this lesson you can say when a marginal quantity is a derivative and when it is the cost of one more lump, derive the rule "marginal benefit equals marginal cost" with its second-order check, prove why marginal cost crosses average cost at the minimum of average cost, and get marginal revenue from a demand curve, including the elasticity form $MR = p\left(1 + \frac{1}{E}\right)$.

Before this: [rates of change and marginal analysis](../../05-university-core/03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md) and [optimization](../../05-university-core/03-applications-of-derivatives/05-optimization.md). Those lessons introduced marginal cost, marginal revenue and the rule $R' = C'$; this one asks why the rule works, where it breaks, and what it says about demand.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. The marginal benefit of the $q$-th unit is $MB(q) = 80 - 2q$ dollars and the marginal cost is $MC(q) = 20 + q$ dollars. At which $q$ do they meet, and what happens to net benefit just before and just after?
2. Inverse demand is $p = 50 - 0.25q$. Find the marginal revenue at $q = 40$ and compare it with the price there.
3. At the price \$40 the elasticity of demand is $E = -2$. What is the marginal revenue?

<details class="solution" markdown>
<summary>Answers</summary>

1. Set $80 - 2q = 20 + q$, so $3q = 60$ and $q = 20$. Before 20, $MB > MC$ and net benefit rises; after 20, $MB < MC$ and net benefit falls.
2. $R(q) = 50q - 0.25q^2$, so $MR = 50 - 0.5q = 30$ at $q = 40$. The price is $50 - 10 = 40$, so the marginal revenue is \$10 below the price.
3. $MR = p\left(1 + \frac{1}{E}\right) = 40\left(1 - \frac{1}{2}\right) = 20$, that is, \$20.

</details>

## The idea

A café owner wonders whether to stay open one more hour in the evening. The hour costs wages and electricity, and it brings in some sales. She doesn't need the café's total profit for the year to decide; she needs two numbers about that one hour. If the extra sales are more than the extra cost, open. If not, close. Economists call the extra amount from one more step the marginal amount, and almost all of microeconomics is that one comparison made carefully.

There are two ways to measure "one more". You can take the actual difference, $C(q+1) - C(q)$, the cost of the next lump. Or you can take the derivative $C'(q)$, the slope of the cost curve at $q$. The derivative is a limit of tiny steps, so it is an idealization, and it is a good one when a unit is small next to the total. It is a poor one when the step is a whole oven, a flight or a server rack. Both are called "marginal" in textbooks, and part of being fluent is knowing which one a problem means.

The derivative earns its place because it turns a search into algebra. Instead of testing $q = 1, 2, 3, \ldots$ one at a time, you solve one equation. The same machinery gives three facts that every intermediate micro course uses: the best output sits where marginal benefit equals marginal cost, marginal cost cuts average cost at its lowest point, and a seller with a downward-sloping demand curve gets less extra revenue from a unit than the price it sells at. The last one is the root of monopoly pricing in [profit maximization and market structure](03-profit-maximization-and-market-structure.md).

## Definitions

For a total cost function $C(q)$ of the quantity $q$, the **marginal cost** is the derivative $MC(q) = C'(q)$, in dollars per unit. In plain words, it is the slope of the cost curve: what the next small amount of output adds to cost. The **discrete marginal cost** of the $n$-th unit is $C(n) - C(n-1)$, the real extra cost of going from $n - 1$ units to $n$ units.

For a total benefit function $B(q)$, which could be a firm's revenue, a consumer's willingness to pay or any gain that depends on the quantity, the **marginal benefit** is $MB(q) = B'(q)$. When the benefit is the firm's sales revenue $R(q) = q\,p(q)$, it is called the **marginal revenue**, $MR(q) = R'(q)$, where $p(q)$ is the price at which exactly $q$ units sell (the inverse demand function). The **net benefit** is $N(q) = B(q) - C(q)$, and for a firm with $B = R$ it is the profit.

The **average cost** is $AC(q) = \frac{C(q)}{q}$ for $q > 0$. Costs split into the **fixed cost** $F = C(0)$, which doesn't change with output, and the **variable cost** $VC(q) = C(q) - F$. The **average variable cost** is $AVC(q) = \frac{VC(q)}{q}$. Since $F$ is a constant, $C'(q) = VC'(q)$: fixed costs never appear in marginal cost.

The **elasticity of demand** at a point on the demand function $q = D(p)$ is

$$
E = \frac{dq}{dp}\cdot\frac{p}{q}.
$$

In plain words, it is about the percent change in the quantity demanded for a 1% rise in price. It is negative for a downward-sloping demand curve, and the full treatment is in [elasticity](../02-markets/05-elasticity.md). Demand is elastic where $E < -1$ and inelastic where $-1 < E < 0$.

## How to do it

### Which kind of marginal?

1. Ask how big one unit is compared with the quantity. For 400 loaves, one loaf is small and the derivative is fine. For 3 aircraft, one aircraft is a large step, so use $C(n) - C(n-1)$.
2. For a smooth cost function, remember that the cost of the $n$-th unit is a difference over the interval from $n - 1$ to $n$. By the mean value theorem it equals $C'(c)$ for some $c$ in that interval. For a quadratic, $c$ is exactly the midpoint, so $C(n) - C(n-1) = C'\left(n - \tfrac{1}{2}\right)$ (Example 1).
3. If the cost function jumps (a new oven at every 60th loaf), there is no derivative at the jump. Compare lumps with lumps: the extra revenue from the whole batch against the extra cost of the whole batch (Example 3).

### The rule MB = MC

The next theorem says why firms and people choose where the two margins meet. Net benefit $N(q)$ rises while $MB > MC$ and falls when $MB < MC$, so the top is where they cross.

*Theorem 1.* Let $B$ and $C$ be twice differentiable on $q \ge 0$, and let $N(q) = B(q) - C(q)$.

- If $N$ has its maximum over $q \ge 0$ at some $q^* > 0$, then $B'(q^*) = C'(q^*)$ and $B''(q^*) \le C''(q^*)$.
- Conversely, if $B'(q^*) = C'(q^*)$ and $B''(q^*) < C''(q^*)$, then $q^*$ is a strict local maximum of $N$.
- If the maximum is at $q^* = 0$, then $B'(0) \le C'(0)$.

What we know: $N$ is differentiable, and a maximum at an interior point is a critical point ([the mean value theorem and extrema](../../05-university-core/03-applications-of-derivatives/03-mean-value-theorem-and-extrema.md)). What we want: to translate "$N' = 0$ and $N'' \le 0$" into statements about $B$ and $C$. The plan is to differentiate $N = B - C$ once and twice.

*Proof.* Since $N' = B' - C'$ and $N'' = B'' - C''$, the conditions $N'(q^*) = 0$ and $N''(q^*) \le 0$ are exactly $B'(q^*) = C'(q^*)$ and $B''(q^*) \le C''(q^*)$. The first is Fermat's theorem for an interior maximum, and the second is the second derivative condition for a maximum. For the converse, $N'(q^*) = 0$ and $N''(q^*) < 0$ is the second derivative test for a strict local maximum. For $q^* = 0$ the maximum is at an endpoint of $[0, \infty)$, so $N$ can't be increasing there, and $N'(0) \le 0$ says $B'(0) \le C'(0)$. $\blacksquare$

Look back at what the second condition means. The slope of $C'$ must exceed the slope of $B'$ at $q^*$: past the optimum, the marginal cost climbs faster than the marginal benefit, or the marginal benefit drops faster than the marginal cost. If instead the marginal cost were falling faster, the point where the two curves cross would be the worst output nearby, not the best. Lesson 3 shows this with a cubic cost curve, where $P = MC$ is solved by two outputs and only one is a profit maximum.

Two consequences follow without any more calculus. First, $F$ is a constant, so it drops out of $N'$: fixed costs don't change where the optimum is, only how high the net benefit is there. Second, a cost already paid and unrecoverable (a sunk cost) is like $F$ and belongs to no decision about the next unit.

### Average against marginal

The theorem in the university core lesson proved that $AC' = \frac{C' - AC}{q}$ for a cost function. The same proof works for any total, and the general version also says which critical points are minima.

*Theorem 2.* Let $T(q)$ be twice differentiable for $q > 0$ and let $a(q) = \frac{T(q)}{q}$ be its average. Then

$$
a'(q) = \frac{T'(q) - a(q)}{q}.
$$

If $a'(q_0) = 0$ at some $q_0 > 0$, then $T'(q_0) = a(q_0)$ and $a''(q_0) = \frac{T''(q_0)}{q_0}$. So $a$ has a local minimum at $q_0$ if $T''(q_0) > 0$ and a local maximum if $T''(q_0) < 0$.

What we know: the quotient rule. What we want: the formula for $a'$, then the sign of $a''$ at a flat spot. The plan is to differentiate $a$ once to get the formula, then differentiate the formula and evaluate where both $a'$ and $T' - a$ vanish.

*Proof.* By the quotient rule, $a' = \frac{T'q - T}{q^2} = \frac{T' - a}{q}$, where the last step uses $\frac{T}{q} = a$. Now write $a' = \frac{T' - a}{q}$ and differentiate again with the quotient rule:

$$
a'' = \frac{(T'' - a')\,q - (T' - a)}{q^2} = \frac{T'' - a'}{q} - \frac{T' - a}{q^2}.
$$

At $q_0$ we have $a'(q_0) = 0$, which by the first formula means $T'(q_0) = a(q_0)$, so both $a'$ and $T' - a$ are $0$ there. The formula becomes $a''(q_0) = \frac{T''(q_0)}{q_0}$. Since $q_0 > 0$, the sign of $a''(q_0)$ is the sign of $T''(q_0)$, and the second derivative test finishes the proof. $\blacksquare$

Look back at the two halves. The first says that the average falls when the margin is below it and rises when the margin is above it, as a new exam mark moves your course average. The second is new: a flat point of the average cost is a minimum exactly when marginal cost is rising there, $C''(q_0) > 0$. That is why the textbook picture has MC crossing AC from below at the lowest point of AC. The same theorem applied to the total product gives the crossing of marginal and average product in [production and cost functions](02-production-and-cost-functions.md).

### Marginal revenue from demand

A seller that can't pick the price separately for each unit has to lower the price on all units to sell one more. That is the whole reason marginal revenue is below the price.

*Theorem 3.* If inverse demand is $p(q)$, differentiable, then revenue is $R(q) = q\,p(q)$ and

$$
MR(q) = p(q) + q\,p'(q).
$$

For linear inverse demand $p(q) = a - bq$ with $a, b > 0$, this is $MR(q) = a - 2bq$. The marginal revenue curve has the same intercept $a$ as the demand curve and twice the slope, and it reaches $0$ at $q = \frac{a}{2b}$, half the quantity at which demand reaches $0$.

*Proof.* The product rule gives $R' = p + q\,p'$. With $p = a - bq$ we have $p' = -b$, so $MR = (a - bq) + q(-b) = a - 2bq$. Setting $a - 2bq = 0$ gives $q = \frac{a}{2b}$, while $p = 0$ at $q = \frac{a}{b}$, twice as far. $\blacksquare$

Look back at the formula $p + q\,p'$. The first term is the price you get on the new unit. The second term, $q\,p'$, is negative for a downward-sloping demand curve: it is the revenue lost on the $q$ units you already sell, because their price fell by $p'$ each. A price taker faces a flat demand curve at the market price, so $p' = 0$ and $MR = p$.

### The elasticity form

*Theorem 4.* Let inverse demand $p(q)$ be differentiable with $p'(q) \ne 0$, and let $E = \frac{dq}{dp}\cdot\frac{p}{q}$ be the elasticity at the point $(q, p)$. Then

$$
MR = p\left(1 + \frac{1}{E}\right).
$$

So $MR > 0$ exactly when $E < -1$ (elastic demand), $MR = 0$ when $E = -1$, and $MR < 0$ when $-1 < E < 0$.

What we know: $MR = p + q\,p'$ from Theorem 3, and the demand function and its inverse have derivatives that are reciprocals. What we want: $q\,p'$ in terms of $p$ and $E$. The plan is to write $\frac{dp}{dq} = \frac{1}{dq/dp}$ and compare with the definition of $E$.

*Proof.* On a demand curve with $\frac{dq}{dp} \ne 0$, the derivative of the inverse function is $p'(q) = \frac{dp}{dq} = \frac{1}{dq/dp}$. By the definition of $E$, $\frac{dq}{dp} = E\,\frac{q}{p}$, so $p'(q) = \frac{p}{E\,q}$. Then $q\,p'(q) = \frac{p}{E}$, and $MR = p + \frac{p}{E} = p\left(1 + \frac{1}{E}\right)$. For the signs: $E < 0$, so $1 + \frac{1}{E} > 0$ exactly when $\frac{1}{E} > -1$, that is, $\lvert E \rvert > 1$. $\blacksquare$

Look back: this is the reason a seller never operates where demand is inelastic. If $\lvert E \rvert < 1$, the extra unit would lose revenue, and with a positive marginal cost it would lose even more. It also lets you compute $MR$ from a measured elasticity without knowing the whole demand curve, which is how the markup rule in the next lesson is derived.

## Worked examples

<div class="example" markdown>

### Example 1: the cost of the next unit, two ways

A print shop's cost for a run of $q$ posters (made-up numbers) is $C(q) = 400 + 12q + 0.5q^2$ dollars. Find the cost of the 5th poster in two ways, and the cost of the 401st.

Step 1: the unit size matters. At $q = 4$, one poster is a quarter of the run, so the derivative may not be close to the real difference. At $q = 400$, one poster is a quarter of a percent.

Step 2: the derivative is $C'(q) = 12 + q$, so $C'(4) = 16$ and $C'(5) = 17$.

Step 3: the real extra cost of the 5th poster is $C(5) - C(4) = (400 + 60 + 12.5) - (400 + 48 + 8) = 472.5 - 456 = 16.5$. That is not $C'(4) = 16$, and not $C'(5) = 17$. It is $C'(4.5) = 12 + 4.5 = 16.5$, the midpoint, as promised for a quadratic.

Step 4: for the 401st poster, $C(401) - C(400) = 12 + 0.5(401^2 - 400^2) = 12 + 0.5 \cdot 801 = 412.5$, against $C'(400) = 412$. The gap is 50 cents on \$412, about 0.12%, so for large runs the derivative is a fine stand-in.

Check: the average cost of the first four posters is $\frac{C(4)}{4} = \frac{456}{4} = 114$ dollars, far above the marginal cost of \$16.50 for the fifth. Average cost is falling there because the fixed \$400 is spread over more posters.

</div>

<div class="example" markdown>

### Example 2: how many hours of testing

A software team (made-up numbers) estimates that $h$ hours of testing before a release avoids $B(h) = 600\ln(1 + h)$ dollars of bug-fixing later, with diminishing returns. Testing costs \$40 an hour plus a \$100 setup, so $C(h) = 100 + 40h$. How many hours maximize the net benefit?

Step 1: the marginal benefit is $B'(h) = \frac{600}{1 + h}$ and the marginal cost is $C'(h) = 40$. The setup cost disappears.

Step 2: set $MB = MC$:

$$
\frac{600}{1 + h} = 40 \quad\Rightarrow\quad 1 + h = 15 \quad\Rightarrow\quad h = 14.
$$

Step 3: apply the second-order condition of Theorem 1. $B''(h) = -\frac{600}{(1 + h)^2}$, which is negative, and $C'' = 0$, so $B'' < C''$ everywhere and the point is a maximum.

Step 4: the net benefit is $N(14) = 600\ln 15 - 100 - 560 \approx 1624.83 - 660 = 964.83$ dollars.

Check: $N(13) \approx 963.43$ and $N(15) \approx 963.55$, both lower. The peak is flat: an hour either way costs about \$1.30. Also, the setup cost shifts $N$ down by \$100 without moving the peak: without it the maximum is still at $h = 14$, and the net benefit is \$1,064.83.

</div>

<div class="example" markdown>

### Example 3: when the derivative fails

A bakery bakes loaves in batches of 60. Each batch costs \$45 to run, and ingredients cost \$0.50 a loaf, with a daily fixed cost of \$120. So $C(q) = 120 + 0.5q + 45\lceil q/60 \rceil$ for $q$ loaves (a made-up cost, with $\lceil \cdot \rceil$ rounding up to the next whole number). Loaves sell at \$3 each. Should the bakery bake the 61st loaf?

The cost function jumps at $q = 60$, so it has no derivative there. The real marginal cost of the 61st loaf is $C(61) - C(60) = 0.5 + 45 = 45.50$ dollars, because it starts a second batch. The marginal revenue is \$3. Compared loaf by loaf, the 61st loaf looks like a terrible idea.

That comparison asks the wrong question. Once the oven is running, the second batch can make up to 60 loaves, not one. Compare lumps with lumps: a full batch costs $45 + 0.5 \cdot 60 = 75$ dollars and brings in $3 \cdot 60 = 180$ dollars, so it adds \$105 of profit if all 60 loaves sell. If only 10 more loaves would sell, the batch brings in \$30 against a cost of $45 + 0.5 \cdot 10 = 50$ dollars and loses \$20.

The break-even point comes from the extra profit on $k$ more loaves, $3k - (45 + 0.5k) = 2.5k - 45$, which is zero at $k = 18$. The second batch is worth running if at least 18 more loaves would sell.

Check: at $k = 18$ the revenue is $3 \cdot 18 = 54$ and the cost is $45 + 9 = 54$. The derivative-based rule $MR = MC$ would be silent here: $C'(q) = 0.5$ everywhere except at the jump, and $MR = 3 > 0.5$ would say "always bake more".

</div>

<div class="example" markdown>

### Example 4: marginal revenue from linear demand

Inverse demand for a product is $p = 60 - 0.2q$ (made up). Find $R(q)$ and $MR(q)$, and check $MR$ at $q = 100$ with the elasticity form.

Revenue is $R(q) = q(60 - 0.2q) = 60q - 0.2q^2$, so $MR(q) = 60 - 0.4q$ (Theorem 3). The demand curve has slope $-0.2$ and the marginal revenue curve has slope $-0.4$, twice as steep, from the same intercept 60. Marginal revenue reaches zero at $q = 150$, half of the 300 where the price reaches zero.

At $q = 100$ the price is $p = 60 - 20 = 40$ and $MR = 60 - 40 = 20$.

Check with Theorem 4. In the form $q = 300 - 5p$ we have $\frac{dq}{dp} = -5$, so $E = -5 \cdot \frac{40}{100} = -2$. Then $MR = 40\left(1 + \frac{1}{-2}\right) = 20$, in agreement. Also $q = 150$ gives $p = 30$ and $E = -5 \cdot \frac{30}{150} = -1$: marginal revenue is zero exactly where demand has unit elasticity.

</div>

<div class="example" markdown>

### Example 5: where average cost is lowest

A firm has $C(q) = 80 + 15q - 0.6q^2 + 0.02q^3$ (made up), a U-shaped marginal cost. Find the minimum of average cost and confirm it with Theorem 2.

The average cost is $AC(q) = \frac{80}{q} + 15 - 0.6q + 0.02q^2$, and the marginal cost is $MC(q) = 15 - 1.2q + 0.06q^2$. Setting $MC = AC$ gives

$$
15 - 1.2q + 0.06q^2 = \frac{80}{q} + 15 - 0.6q + 0.02q^2 \quad\Rightarrow\quad 0.04q^2 - 0.6q = \frac{80}{q} \quad\Rightarrow\quad 0.04q^3 - 0.6q^2 - 80 = 0.
$$

Rather than solve a cubic, try $q = 20$: $0.04 \cdot 8000 - 0.6 \cdot 400 - 80 = 320 - 240 - 80 = 0$. Yes. At $q = 20$ both curves equal $15$: $AC(20) = 4 + 15 - 12 + 8 = 15$ and $MC(20) = 15 - 24 + 24 = 15$.

By Theorem 2, $AC''(20) = \frac{C''(20)}{20}$, and $C''(q) = -1.2 + 0.12q$ gives $C''(20) = 1.2 > 0$, so $AC''(20) = 0.06 > 0$ and it is a minimum. Marginal cost is rising at 20, because its own minimum is earlier, at $q = 10$ where $MC = 9$.

Check by differentiating directly: $AC''(q) = \frac{160}{q^3} + 0.04$, which at $q = 20$ is $0.02 + 0.04 = 0.06$. Values on either side are higher, $AC(10) = 19$ and $AC(30) = 17.67$.

</div>

<div class="example" markdown>

### Example 6: marginal revenue and unit elasticity (finish it yourself)

Demand is $q = 200 - 5p$ (made up). Inverse demand is $p = 40 - 0.2q$, so $R(q) = 40q - 0.2q^2$.

Find $MR(q)$, the quantity where $MR = 0$, and the elasticity there. Then check Theorem 4 at $q = 60$.

<details class="solution" markdown>
<summary>Finish</summary>

$MR(q) = 40 - 0.4q$, which is zero at $q = 100$, where $p = 20$. The elasticity is $E = -5 \cdot \frac{20}{100} = -1$, as Theorem 4 predicts for $MR = 0$.

At $q = 60$: $p = 28$ and $MR = 40 - 24 = 16$. The elasticity is $E = -5 \cdot \frac{28}{60} = -\frac{7}{3}$, and $p\left(1 + \frac{1}{E}\right) = 28\left(1 - \frac{3}{7}\right) = 28 \cdot \frac{4}{7} = 16$.

Check: $16 < 28$, so the marginal revenue is below the price, and $\lvert E \rvert = 2.33 > 1$, so it is positive, as it should be on the elastic part of the curve.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: confusing marginal cost with average cost. In Example 1 the fifth poster costs \$16.50 and the average over the first four is \$114. A firm that prices each extra unit at its average cost is charging for the fixed cost over again, and one that treats average cost as the cost of the next unit will turn down good orders.

</div>

<div class="warning" markdown>

Watch out: putting a fixed or sunk cost into a margin. If a company has already paid \$20,000 for a software licence, the next customer's marginal cost has no \$20,000 in it. The cost $F$ is constant, so it disappears when you differentiate. It matters for whether to be in the business at all (see the shutdown rule in the next lesson), but not for how much to produce.

</div>

<div class="warning" markdown>

Watch out: setting $MR = p$ for a seller with market power. The identity $MR = p$ holds only when the demand curve is flat, as for a price taker. For a downward-sloping demand, $MR = p + q\,p' < p$. A common slip is to write $R = pq$, differentiate as if $p$ were constant and get $R' = p$.

</div>

<div class="warning" markdown>

Watch out: halving the wrong thing. The marginal revenue curve for linear demand $p = a - bq$ is $a - 2bq$. It has twice the slope of demand and the same price intercept. It doesn't have half the intercept, and it is not $\frac{a}{2} - bq$. A check: at $q = 0$ the first unit sells at the full price $a$, so $MR(0) = a$.

</div>

<div class="warning" markdown>

Watch out: stopping at $MB = MC$. The equation is a first-order condition, and it holds at minima of net benefit too. With a falling marginal cost, as for a cubic cost curve, the first crossing can be the worst output nearby. Check that $B'' < C''$ at the solution, or compare the net benefit on both sides.

</div>

<div class="warning" markdown>

Watch out: the sign of the elasticity. The number $E = \frac{dq}{dp}\cdot\frac{p}{q}$ is negative for ordinary demand. Writing $MR = p\left(1 - \frac{1}{E}\right)$ with $E = -2$ gives $1.5p$, more than the price, which can't be right. Either keep the sign and use $1 + \frac{1}{E}$, or use $\lvert E \rvert$ and write $1 - \frac{1}{\lvert E \rvert}$.

</div>

<div class="warning" markdown>

Watch out: the cost of the $n$-th unit is $C(n) - C(n-1)$, not $C'(n)$. For a quadratic cost the exact figure is $C'(n - \frac{1}{2})$. With small quantities the difference is large (Example 1: \$16.50 against \$17).

</div>

Two special cases are worth a word. Marginal cost can be zero or constant, as for a software product with no per-copy cost: then $AC = \frac{F}{q} + c$ falls forever and has no minimum, and Theorem 2 correctly says nothing, because $C'' = 0$. And at $q = 0$ the average cost isn't defined, so every statement about $AC$ is for $q > 0$.

## Tricks and shortcuts

For linear demand $p = a - bq$, write marginal revenue straight from the demand curve: same intercept, double the slope, so $MR = a - 2bq$. It reaches zero at half the quantity where demand hits the axis, and the point of unit elasticity is the midpoint of the demand line.

For a quadratic cost, $C(n) - C(n-1) = C'(n - \frac{1}{2})$. The exact cost of a unit is the derivative at the midpoint of the step, which is a better habit than using either end.

For a cost with a fixed part, find the minimum of $AC$ by setting $MC = AC$ and cancelling the terms that match on both sides. In Example 5 the 15 cancelled, and in general the constant term $a$ in $C = F + aq + \ldots$ always does.

To get the sign of $MR$ at a glance, use the elasticity: elastic means positive, unit elastic means zero, inelastic means negative. If you know only that demand is elastic, you know that the extra unit adds revenue.

## In code

Sympy checks a derivative against the real step, finds the minimum of average cost, and confirms that marginal revenue is the product-rule formula. The last lines compute marginal revenue two ways from the elasticity.

<details class="code" markdown>
<summary>In code</summary>

```python
import sympy as sp

q = sp.symbols("q", positive=True)

# Example 1: marginal cost as a derivative against the real step
C = 400 + 12 * q + sp.Rational(1, 2) * q**2
for n in (4, 400):
    print(n, sp.diff(C, q).subs(q, n), C.subs(q, n + 1) - C.subs(q, n))
# 4 16 33/2
# 400 412 825/2

# Example 5: the minimum of average cost
C5 = 80 + 15 * q - sp.Rational(3, 5) * q**2 + sp.Rational(1, 50) * q**3
AC = C5 / q
print(sp.solve(sp.Eq(sp.diff(C5, q), AC), q))
# [20]
print(sp.diff(AC, q, 2).subs(q, 20), sp.diff(C5, q, 2).subs(q, 20) / 20)
# 3/50 3/50

# Example 4: marginal revenue from p = 60 - 0.2 q, and the elasticity form
p = 60 - sp.Rational(1, 5) * q
MR = sp.diff(q * p, q)
E = -5 * p / q
print(MR.subs(q, 100), (p * (1 + 1 / E)).subs(q, 100))
# 20 20
```

The first block shows the gap of half a unit's cost at a small $q$ and at a large one. The second confirms that $AC' = 0$ at $q = 20$, with $AC''$ equal to $C''$ divided by $q$. The third checks Theorem 4 at one point.

</details>

## FAQ

### Why is marginal revenue below the price?

To sell one more unit along a downward-sloping demand curve you have to lower the price, and the lower price applies to every unit, and not just the new one. The new unit adds the price $p$, but the $q$ units you already sell each lose $\lvert p' \rvert$. In Example 4, going from 100 to 101 units drops the price from \$40 to \$39.80: the new unit brings in \$39.80, the 100 old units lose \$20 together, and the net gain is \$19.80, close to $MR = 20$.

### What if marginal cost is constant?

Then $C(q) = F + cq$, $MC = c$ and $AC = \frac{F}{q} + c$, which always falls toward $c$ but never reaches it. There is no minimum of average cost: the more you make, the cheaper each unit gets. This is the cost shape of software, a network or a power line with a huge fixed cost, and it is why such markets tend to have a few big firms.

### Should I use the derivative or the real step in exams?

Use the derivative unless the problem gives a table of costs for whole units or says that units are big. A table is a discrete problem: compare $C(n) - C(n - 1)$ with the benefit of the $n$-th unit and stop when the margin turns negative. Intermediate micro courses usually give you a differentiable function and expect the derivative.

### Does the rule MB = MC work for consumers too?

Yes, and it is the same theorem. A consumer's benefit is the utility $U(q)$ from $q$ units of a good, and the cost is what they pay. They buy until the marginal utility of the next unit, in dollars, equals its price. With several goods and a budget, the comparison becomes the tangency condition in [utility and indifference curves](04-utility-and-indifference-curves.md).

## Practice

### Warm-up

1\. A firm's cost is $C(q) = 1500 + 25q + 0.2q^2$. (a) Find the marginal cost at $q = 100$. (b) Find the exact cost of the 101st unit. (c) Is the average cost rising or falling at $q = 100$?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $C'(q) = 25 + 0.4q$, so $C'(100) = 65$ dollars per unit.

(b) $C(101) - C(100) = 25 + 0.2(101^2 - 100^2) = 25 + 0.2 \cdot 201 = 65.2$ dollars.

(c) $AC(100) = \frac{1500}{100} + 25 + 0.2 \cdot 100 = 60$. Marginal cost (\$65) is above average cost (\$60), so by Theorem 2 the average is rising.

Check: the difference in (b) is $C'(100.5) = 25 + 40.2 = 65.2$, the midpoint derivative. And $AC' = \frac{65 - 60}{100} = 0.05 > 0$; directly, $AC(101) = \frac{1500}{101} + 25 + 20.2 = 60.05$, up by 5 cents.

</details>

2\. Inverse demand is $p = 120 - 0.4q$. Find revenue and marginal revenue as functions of $q$. At $q = 100$, find the price and the marginal revenue. At what quantity is marginal revenue zero?

<details class="solution" markdown>
<summary>Solution</summary>

$R(q) = 120q - 0.4q^2$ and $MR(q) = 120 - 0.8q$. At $q = 100$ the price is $120 - 40 = 80$ and $MR = 120 - 80 = 40$. Setting $120 - 0.8q = 0$ gives $q = 150$.

Check: the slope of $MR$ is $-0.8$, twice the slope $-0.4$ of demand, and 150 is half of the 300 where the price is zero.

</details>

3\. The marginal benefit of the $q$-th unit is $MB(q) = 90 - 3q$ and the marginal cost is $MC(q) = 30 + 2q$, with a fixed cost of \$100. Find the best $q$, and the net benefit there, given $B(q) = 90q - 1.5q^2$ and $C(q) = 100 + 30q + q^2$.

<details class="solution" markdown>
<summary>Solution</summary>

$90 - 3q = 30 + 2q$ gives $5q = 60$ and $q = 12$. The net benefit is $N(q) = 60q - 2.5q^2 - 100$, so $N(12) = 720 - 360 - 100 = 260$.

Check: $B'' = -3 < C'' = 2$, so it is a maximum, and $N(11) = N(13) = 257.5$, both below 260. The fixed cost of \$100 didn't change the answer, only the height.

</details>

### Standard

4\. Demand is $q = 300 - 6p$. (a) At $p = 30$ find the quantity and the elasticity. (b) Use $MR = p\left(1 + \frac{1}{E}\right)$ to find the marginal revenue there. (c) Verify (b) by writing inverse demand and differentiating revenue. (d) At what price is demand unit elastic?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $q = 300 - 180 = 120$, and $\frac{dq}{dp} = -6$, so $E = -6 \cdot \frac{30}{120} = -1.5$.

(b) $MR = 30\left(1 + \frac{1}{-1.5}\right) = 30 \cdot \frac{1}{3} = 10$ dollars.

(c) Inverse demand is $p = 50 - \frac{q}{6}$, so $R = 50q - \frac{q^2}{6}$ and $MR = 50 - \frac{q}{3}$, which is $50 - 40 = 10$ at $q = 120$.

(d) $E = -6 \cdot \frac{p}{300 - 6p} = -1$ gives $6p = 300 - 6p$, so $p = 25$, $q = 150$. There $MR = 50 - 50 = 0$.

Check: demand is elastic for prices above \$25 and inelastic below; at \$30, $\lvert E \rvert = 1.5 > 1$ and $MR > 0$.

</details>

5\. A firm has $C(q) = 270 + 12q - 0.3q^2 + 0.01q^3$. Show that the average cost is minimized at $q = 30$, find the minimum, and check that $MC = AC$ there and that $AC'' > 0$.

<details class="solution" markdown>
<summary>Solution</summary>

$AC(q) = \frac{270}{q} + 12 - 0.3q + 0.01q^2$ and $MC(q) = 12 - 0.6q + 0.03q^2$. At $q = 30$: $AC = 9 + 12 - 9 + 9 = 21$ and $MC = 12 - 18 + 27 = 21$. Equal, so $AC'(30) = 0$.

By Theorem 2, $AC''(30) = \frac{C''(30)}{30}$ with $C''(q) = -0.6 + 0.06q = 1.2$ at $q = 30$, so $AC''(30) = 0.04 > 0$. It is a minimum, and the minimum average cost is \$21.

Check: $AC(20) = 13.5 + 12 - 6 + 4 = 23.5$ and $AC(40) = 6.75 + 12 - 12 + 16 = 22.75$, both above 21.

</details>

6\. With $MB(q) = 90 - 3q$ and $MC(q) = 30 + 2q$ as in problem 3, the government puts a tax of $t$ dollars on each unit, which adds $t$ to the marginal cost. Find the new best quantity as a function of $t$. By how much does a \$5 tax cut the quantity? Is the tax cost for the units that are still produced equal to $5q$?

<details class="solution" markdown>
<summary>Solution</summary>

$90 - 3q = 30 + 2q + t$ gives $q = \frac{60 - t}{5} = 12 - \frac{t}{5}$. A \$5 tax cuts the quantity by 1 unit, from 12 to 11.

The tax collected is $5 \cdot 11 = 55$ dollars, on the 11 units still sold. It is not $5 \cdot 12$, because the twelfth unit is no longer produced.

Check: at $q = 11$, $MB = 90 - 33 = 57$ and $MC + t = 30 + 22 + 5 = 57$. They meet.

</details>

### Challenge

7\. Demand has constant elasticity: $q = Ap^{-2}$ for a constant $A > 0$. (a) Show that $MR = \frac{p}{2}$ at every quantity. (b) A seller with constant marginal cost \$15 and $A = 10{,}000$ sets $MR = MC$. Find its price and quantity.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Here $\frac{dq}{dp} = -2Ap^{-3}$, so $E = -2Ap^{-3}\cdot\frac{p}{Ap^{-2}} = -2$ at every point. Theorem 4 gives $MR = p\left(1 - \frac{1}{2}\right) = \frac{p}{2}$. Directly, $p = \sqrt{A/q}$ and $R = \sqrt{A}\,q^{1/2}$, so $MR = \frac{1}{2}\sqrt{A}\,q^{-1/2} = \frac{p}{2}$.

(b) $\frac{p}{2} = 15$ gives $p = 30$, and $q = \frac{10000}{900} \approx 11.11$ units.

Check: $R = \sqrt{10000}\sqrt{q} = 100\sqrt{q}$, so $MR = \frac{50}{\sqrt{11.11}} = 15$. The second-order condition holds too: $MR$ falls with $q$ while $MC$ is constant, so $B'' < C'' = 0$. The price is exactly twice the marginal cost, because $\lvert E \rvert = 2$.

</details>

8\. (Reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).) A seller raises the price by 5% and the quantity sold falls by 8%. (a) Estimate the elasticity as the ratio of percent changes. (b) By what percent does revenue change? (c) Is this consistent with Theorem 4?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $E \approx \frac{-8\%}{5\%} = -1.6$.

(b) Revenue is price times quantity, so it is multiplied by $1.05 \times 0.92 = 0.966$, a fall of 3.4%.

(c) Yes. $\lvert E \rvert = 1.6 > 1$, so demand is elastic, and by Theorem 4 the marginal revenue is positive. Raising the price moves the seller up the demand curve to a point with less quantity, and on an elastic stretch, the loss of quantity costs more revenue than the higher price earns.

Check: with $E = -1.6$, a 5% price rise predicts a quantity change of $-1.6 \cdot 5\% = -8\%$. The estimate is rough for a 5% step; it agrees with the true derivative only for small changes.

</details>

## Where this shows up

- The next lesson, [production and cost functions](02-production-and-cost-functions.md), builds the cost curves from the technology that makes the output. [Profit maximization and market structure](03-profit-maximization-and-market-structure.md) uses $MR = MC$ with the curves of this lesson, and the markup rule $\frac{p - MC}{p} = \frac{1}{\lvert E \rvert}$ is Theorem 4 solved for the price. [Elasticity](../02-markets/05-elasticity.md) is developed further in the markets chapter.
- Economics: every "margin" in a micro course is this derivative, from the labour supply decision to a firm's hiring. The rule $MB = MC$ is also how cost-benefit analysis decides how much of a public good to provide.
- CS: the same comparison decides how many servers to run, how long to test or how many cache layers to build, when the marginal benefit of the next one falls below its cost. The average-versus-marginal identity $a' = (T' - a)/q$ is also the idea behind amortized analysis, where the average cost of an operation can fall while a single operation is costly.

