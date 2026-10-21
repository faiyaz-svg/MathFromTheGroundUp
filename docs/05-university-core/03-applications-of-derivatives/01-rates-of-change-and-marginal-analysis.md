# Rates of change and marginal analysis

After this lesson you can read a derivative as a rate with units, solve related-rates problems (a ladder, a draining cone, a shadow), estimate the cost of the next unit with marginal cost, revenue and profit, and prove why marginal cost crosses average cost at the minimum of average cost.

Before this: [the derivative definition](../02-derivatives/01-the-derivative-definition.md), [differentiation rules](../02-derivatives/02-differentiation-rules.md) and [chain rule, implicit and inverse derivatives](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A spherical balloon has volume $V = \frac{4}{3}\pi r^3$ cm$^3$, and its radius grows at 2 cm/s. How fast is the volume growing when $r = 5$ cm?
2. A firm's cost is $C(q) = 500 + 8q + 0.02q^2$ dollars for $q$ units. Use $C'(50)$ to estimate the cost of the 51st unit, then compute that cost exactly.
3. The side of a square grows at 3 cm/s. How fast is its area growing when the side is 10 cm?

<details class="solution" markdown>
<summary>Answers</summary>

1. By the chain rule, $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt} = 4\pi \cdot 25 \cdot 2 = 200\pi \approx 628.3$ cm$^3$/s.
2. $C'(q) = 8 + 0.04q$, so $C'(50) = 10$ and the 51st unit costs about \$10. Exactly, $C(51) - C(50) = 8 + 0.02(51^2 - 50^2) = 8 + 0.02 \cdot 101 = 10.02$, so the estimate is off by two cents.
3. $A = s^2$, so $\frac{dA}{dt} = 2s \frac{ds}{dt} = 2 \cdot 10 \cdot 3 = 60$ cm$^2$/s.

</details>

## The idea

The derivative was built to answer "how fast is it changing right now?", and the answer always comes with units. If $s(t)$ is a distance in metres and $t$ is in seconds, then $s'(t)$ is in metres per second. If $C(q)$ is a cost in dollars and $q$ counts units, then $C'(q)$ is in dollars per unit. The units are a check on every answer in this lesson: if a rate of change of a volume comes out in square centimetres per second, something went wrong.

Many quantities are tied together. As the foot of a ladder slides away from a wall, the top slides down; as water drains from a tank, its depth falls; as a person walks away from a lamp, the tip of the shadow races ahead of them. In each case one rate is known and another is wanted, and an equation connects the quantities. Differentiating that equation with respect to time, using the chain rule, connects the rates. This is the idea of related rates, and the first half of the lesson is about doing it carefully.

The second half moves the same idea into economics. A firm doesn't only ask what its total cost is, it asks what the next unit costs, and whether the next unit brings in more revenue than it costs. The derivative answers both, to a good approximation, because the cost of one more unit is the change in $C$ over a step of size 1, and for a smooth curve a step of size 1 is nearly the tangent step. Comparing the cost of the next unit with the average cost of all the units so far gives a clean fact about the minimum of average cost, which has a short proof and a picture.

## Definitions

The **rate of change** of a quantity $y$ with respect to $x$ at a point is the derivative $\frac{dy}{dx}$ there. In plain words, it is how many units of $y$ you gain per extra unit of $x$ at that moment, and a negative rate means $y$ is falling. When $x$ is time, we write $\frac{dy}{dt}$ and say "the rate at which $y$ changes".

A **related rates problem** gives an equation connecting two or more quantities that all change with time, together with the rates of all but one of them at a particular instant, and asks for the remaining rate at that instant. In plain words, it is the chain rule applied to a real situation: differentiate the connecting equation with respect to $t$, then substitute the numbers.

For a firm producing $q$ units, the **total cost** is $C(q)$ and the **total revenue** is $R(q)$, both in dollars. If it sells $q$ units at the price $p(q)$ per unit, then $R(q) = q\,p(q)$. The **profit** is $P(q) = R(q) - C(q)$. The **marginal cost** $C'(q)$, the **marginal revenue** $R'(q)$ and the **marginal profit** $P'(q) = R'(q) - C'(q)$ are the derivatives, in dollars per unit. In plain words, each is the amount that the next unit adds to cost, revenue or profit.

The reason the derivative stands in for "the next unit" is the approximation

$$
C(q + 1) - C(q) \approx C'(q).
$$

The left side is the difference quotient with step $h = 1$. The approximation is good when the slope of $C$ barely changes over a step of 1 unit, which is true when $q$ is large compared with 1, or when units are small (thousands of cars, litres of oil). For a quadratic cost curve the error is exactly $\frac{1}{2}C''(q)$, and in general it is close to that number; the next lesson makes this precise.

The **average cost** is $A(q) = \frac{C(q)}{q}$ for $q > 0$, the cost per unit over all $q$ units. Notice that the average cost and the marginal cost are different numbers with the same units. The average cost spreads the whole bill, including the fixed cost, over all units. The marginal cost looks only at the next unit.

The **elasticity of demand** is a way to compare changes in percent instead of in units. If the quantity demanded at the price $p$ is $q = D(p)$, the elasticity at $p$ is

$$
E = \frac{dq}{dp} \cdot \frac{p}{q}.
$$

In plain words, it is approximately the percent change in quantity for a 1% rise in price. It is a preview here, and the full treatment is in elasticity<!-- link: ../../07-economics-math/02-markets/05-elasticity.md -->.

## How to do it

### Reading a derivative as a rate

1. Name the two quantities and their units: $y$ in (units of $y$), $x$ in (units of $x$).
2. The derivative $\frac{dy}{dx}$ has units "units of $y$ per unit of $x$". Say what it means in a sentence: "when $x$ is 100, each extra unit of $x$ adds about $f'(100)$ units of $y$".
3. Read the sign: positive means $y$ rises as $x$ rises, negative means it falls.
4. To estimate a small change, use $\Delta y \approx f'(x)\,\Delta x$.

### Related rates

1. Draw a picture and name every quantity that changes, with units. Use letters for the quantities that vary, and keep numbers for the quantities that stay fixed throughout.
2. Write an equation connecting the varying quantities. Find it from geometry (Pythagoras, similar triangles, volume formulas), and reduce the number of variables if you can. Do not substitute the numbers of the instant yet.
3. Differentiate both sides with respect to $t$, using the chain rule on every varying quantity: $\frac{d}{dt}x^2 = 2x\frac{dx}{dt}$.
4. Now substitute the values at the instant in question, including values of the quantities themselves (found from the equation of Step 2 if needed) and the known rates.
5. Solve for the unknown rate. Give its sign and units.
6. Check: does the sign match the picture, are the units right, and does a small time step on the original equation agree?

Watch out for Step 4. If you substitute the instant's values into the equation before differentiating, a varying quantity turns into a constant, and its derivative disappears. The error is common and the rest of the work looks fine.

### Marginal analysis

1. Write the cost, revenue or profit function in terms of the quantity $q$. If revenue is given through a price, use $R = q\,p(q)$.
2. Differentiate to get the marginal function, and evaluate it at the $q$ of interest.
3. Read it as the approximate amount that the next unit adds, in dollars per unit. For an exact figure, compute $C(q + 1) - C(q)$ directly.
4. Compare: if marginal revenue is above marginal cost at $q$, then the next unit adds profit, and if it is below, the next unit loses money.

### Average cost against marginal cost

The next theorem connects the two ideas. The figure shows the result for the cost function $C(q) = 1000 + 10q + 0.05q^2$ from [the derivative definition](../02-derivatives/01-the-derivative-definition.md), whose marginal cost is $C'(q) = 10 + 0.1q$.

![Average cost and marginal cost for C(q) = 1000 + 10q + 0.05q squared. The green average cost curve falls steeply, reaches a minimum near q equals 141.4, and then rises slowly. The red marginal cost line rises steadily and crosses the green curve exactly at the lowest point of the green curve, where both are about 24.14 dollars. A dashed vertical line marks the quantity 141.4.](../../assets/figures/05-university-core/rates-of-change-and-marginal-analysis-average-and-marginal.svg)

*Theorem.* Let $C$ be differentiable for $q > 0$, and let $A(q) = \frac{C(q)}{q}$. Then

$$
A'(q) = \frac{C'(q) - A(q)}{q}.
$$

So, for $q > 0$:

- $A'(q) < 0$ exactly when $C'(q) < A(q)$, so average cost falls while marginal cost is below it;
- $A'(q) > 0$ exactly when $C'(q) > A(q)$, so average cost rises while marginal cost is above it;
- if $A$ has a local minimum at $q_0 > 0$, then $C'(q_0) = A(q_0)$.

We know that $A$ is the quotient of two differentiable functions, $C(q)$ and $q$, and that the quotient rule applies. We want a formula for $A'$ in terms of $C'$ and $A$. The plan is to differentiate with the quotient rule, then replace $\frac{C}{q}$ by $A$.

*Proof.* The quotient rule with numerator $C$ and denominator $q$ gives

$$
A'(q) = \frac{C'(q) \cdot q - C(q) \cdot 1}{q^2} = \frac{C'(q)}{q} - \frac{C(q)}{q^2} = \frac{C'(q) - A(q)}{q},
$$

where the last step replaces $\frac{C(q)}{q}$ by $A(q)$, so that $\frac{C(q)}{q^2} = \frac{A(q)}{q}$. Since $q > 0$, the sign of $A'(q)$ is the sign of $C'(q) - A(q)$, which proves the first two bullets. For the third, a local minimum of a differentiable function has a zero derivative ([Fermat's theorem](03-mean-value-theorem-and-extrema.md#fermats-theorem)), so $A'(q_0) = 0$, and the formula gives $C'(q_0) - A(q_0) = 0$. $\blacksquare$

Look back at what the proof says. A new unit pulls the average toward its own cost, exactly as a test mark does: a mark below your current average lowers the average, and a mark above raises it. The average stops falling and starts rising at the moment the new units cost the same as the average, which is where the two curves cross. There is also a picture. $A(q)$ is the slope of the line from the origin to the point $(q, C(q))$, and $C'(q)$ is the slope of the tangent there. The average cost is smallest where the ray from the origin just touches the cost curve, so that the ray and the tangent have the same slope.

### Elasticity and revenue

For a demand function $q = D(p)$ the revenue is $R = pq$, and the product rule with respect to $p$ gives

$$
\frac{dR}{dp} = q + p\frac{dq}{dp} = q\left(1 + \frac{dq}{dp}\cdot\frac{p}{q}\right) = q\,(1 + E).
$$

When demand is elastic, $E < -1$, so $1 + E < 0$ and a price rise lowers revenue. When it is inelastic, $-1 < E < 0$, a price rise raises revenue. The same idea in terms of quantity is $R'(q) = p\left(1 + \frac{1}{E}\right)$, found by writing $R = q\,p(q)$, so that $R' = p + q\frac{dp}{dq}$ and $\frac{dp}{dq} = \frac{1}{dq/dp}$.

## Worked examples

<div class="example" markdown>

### Example 1: a sliding ladder

A 13 m ladder leans against a vertical wall. Its foot is 5 m from the wall and is pulled away at 0.6 m/s. How fast is the top sliding down at that moment?

Step 1: draw the picture (the left panel of the figure). Let $x$ be the distance of the foot from the wall and $y$ the height of the top, both in metres. Both change with time, and the ladder's length 13 m stays fixed.

![Two panels. On the left, a 13 m ladder leans on a vertical wall, with the foot 5 m from the wall moving away at 0.6 m per second and the top at height 12 m sliding down. On the right, a 5 m lamp post and a 1.8 m person at distance x from it, with the shadow of length s on the ground reaching to the tip of the shadow.](../../assets/figures/05-university-core/rates-of-change-and-marginal-analysis-ladder-and-shadow.svg)

Step 2: Pythagoras gives $x^2 + y^2 = 169$. We keep it as it is, without the numbers 5 and 12.

Step 3: differentiate with respect to $t$. The chain rule gives $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$, so

$$
\frac{dy}{dt} = -\frac{x}{y}\frac{dx}{dt}.
$$

Step 4: at the moment in question $x = 5$, so $y = \sqrt{169 - 25} = 12$, and $\frac{dx}{dt} = 0.6$. Then $\frac{dy}{dt} = -\frac{5}{12} \cdot 0.6 = -0.25$.

Step 5: the top slides down at 0.25 m/s. The negative sign means $y$ is decreasing, which matches the picture, and the units are metres per second.

Check: the position of the top after a short time $t$ is $y(t) = \sqrt{169 - (5 + 0.6t)^2}$. At $t = 0.01$ this is $11.99750\ldots$, so the change over 0.01 s is about $-0.0025$ m, a rate of $-0.25$ m/s. As the foot gets closer to 13 m from the wall, $y \to 0$ and the formula's rate grows without bound: at $x = 12$, $y = 5$ and the top falls at $\frac{12}{5} \cdot 0.6 = 1.44$ m/s. A real ladder would have left the wall long before that, so the model has limits.

</div>

<div class="example" markdown>

### Example 2: a draining cone

A conical tank is 4 m across the top and 4 m deep, with its point at the bottom, so that the tank is a cone with radius 2 m and height 4 m. It drains at 0.5 m$^3$/min. How fast is the water level falling when the water is 3 m deep?

Draw the cone (the figure) and let $h$ be the depth and $r$ the radius of the water surface. Similar triangles give $\frac{r}{h} = \frac{2}{4}$, so $r = \frac{h}{2}$, which removes one variable before differentiating. The volume of the water is

$$
V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi\left(\frac{h}{2}\right)^2 h = \frac{\pi}{12}h^3.
$$

![A conical tank with its point at the bottom, 4 m across the top and 4 m deep. Water fills the lower part to depth h, with the surface radius r marked as a red segment and the depth h as a green segment. A label says the tank is draining at 0.5 cubic metres per minute.](../../assets/figures/05-university-core/rates-of-change-and-marginal-analysis-cone.svg)

Differentiate with respect to $t$: $\frac{dV}{dt} = \frac{\pi}{4}h^2\frac{dh}{dt}$. Now substitute $\frac{dV}{dt} = -0.5$ (the volume is falling) and $h = 3$:

$$
-0.5 = \frac{\pi}{4} \cdot 9 \cdot \frac{dh}{dt}, \qquad \frac{dh}{dt} = -\frac{2}{9\pi} \approx -0.0707 \text{ m/min}.
$$

The level falls at about 7 cm per minute. Check: the units are $\frac{\text{m}^3/\text{min}}{\text{m}^2}$, which is m/min. Also, at depth 3 m the water surface has area $\pi r^2 = \pi \cdot 1.5^2 \approx 7.07$ m$^2$, and draining 0.5 m$^3$ from a surface of that area lowers it by $\frac{0.5}{7.07} \approx 0.0707$ m each minute. That is the same calculation in words: the rate of the volume divided by the area of the surface.

</div>

<div class="example" markdown>

### Example 3: a shadow

A lamp is 5 m above the ground. A person 1.8 m tall walks away from the lamp post at 1.2 m/s. How fast is the tip of the shadow moving, and how fast is the shadow lengthening?

In the right panel of the figure, let $x$ be the person's distance from the post and $s$ the length of the shadow. The lamp, the top of the person's head and the tip of the shadow are on one line, so the triangles formed by the post and by the person are similar:

$$
\frac{s}{1.8} = \frac{x + s}{5}, \quad\text{so}\quad 5s = 1.8x + 1.8s, \quad\text{so}\quad s = \frac{1.8}{3.2}x = \frac{9}{16}x.
$$

The shadow is $\frac{9}{16}$ of the distance from the post, which gives $\frac{ds}{dt} = \frac{9}{16} \cdot 1.2 = 0.675$ m/s. The tip is at distance $x + s = \frac{25}{16}x$ from the post, so it moves at $\frac{25}{16} \cdot 1.2 = 1.875$ m/s.

There was no instant in this problem: the answer is the same wherever the person is, because the connecting equation is linear. When the relation is linear and the given rate is constant, the answer never depends on the position.

Check: the tip moves faster than the person, which is right, since it is ahead of the person. And the tip's speed is the person's speed plus the shadow's: $1.2 + 0.675 = 1.875$.

</div>

<div class="example" markdown>

### Example 4: marginal revenue, cost and profit

A seller faces the price $p(q) = 100 - 2q$ dollars, as in [differentiation rules](../02-derivatives/02-differentiation-rules.md), and the cost $C(q) = 200 + 20q + 2q^2$ dollars. Find the marginal functions, and say what happens to profit as the seller makes more.

The revenue is $R(q) = q(100 - 2q) = 100q - 2q^2$, so $R'(q) = 100 - 4q$. The marginal cost is $C'(q) = 20 + 4q$. The marginal profit is $P'(q) = R'(q) - C'(q) = 80 - 8q$.

| $q$ | Marginal revenue | Marginal cost | Marginal profit | Profit $P(q)$ |
|---|---|---|---|---|
| 5 | \$80 | \$40 | \$40 | \$100 |
| 8 | \$68 | \$52 | \$16 | \$184 |
| 10 | \$60 | \$60 | \$0 | \$200 |
| 12 | \$52 | \$68 | loss of \$16 | \$184 |

Up to $q = 10$ each unit brings in more than it costs, so profit rises. At $q = 10$ the marginal revenue equals the marginal cost, and beyond it each unit costs more than it brings in, so profit falls. The best output is where the profit stops rising, $P'(q) = 0$, so at $q = 10$. This is the rule "marginal revenue equals marginal cost", and [optimization](05-optimization.md) develops it into a method.

Check: $P(q) = -4q^2 + 80q - 200$, and the table's profits are $P(5) = 100$, $P(8) = 184$, $P(10) = 200$ and $P(12) = 184$. The exact profit gain from the 6th unit is $P(6) - P(5) = 136 - 100 = 36$, against the marginal profit \$40 at $q = 5$. The estimate overshoots by \$4. The slope of $P$ falls by 8 for each unit, so over a step of 1 the average slope is lower than the starting slope: the actual change is $P'(5) + \frac{1}{2}P''(5) = 40 - 4 = 36$.

</div>

<div class="example" markdown>

### Example 5: where average cost is smallest (finish it yourself)

A workshop's cost is $C(q) = 900 + 4q + 0.25q^2$ dollars for $q$ units. The average cost is $A(q) = \frac{900}{q} + 4 + 0.25q$, and the marginal cost is $C'(q) = 4 + 0.5q$.

Use the theorem to find the output that minimizes average cost, and the value of the average cost there.

<details class="solution" markdown>
<summary>Finish</summary>

At a minimum, $C'(q) = A(q)$, so $4 + 0.5q = \frac{900}{q} + 4 + 0.25q$. Subtract 4 and $0.25q$ from both sides: $0.25q = \frac{900}{q}$, so $q^2 = 3600$ and $q = 60$ (the negative root is not an output).

Then $A(60) = 15 + 4 + 15 = 34$ and $C'(60) = 4 + 30 = 34$. The average cost is smallest at 60 units, at \$34 per unit.

Check: $A(50) = 18 + 4 + 12.5 = 34.5$ and $A(70) = 12.857 + 4 + 17.5 = 34.357$, both above \$34. Also $A'(q) = -\frac{900}{q^2} + 0.25$ is negative for $q < 60$ and positive for $q > 60$, so 60 is a minimum.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: substituting the instant's numbers before differentiating. In the ladder, writing $5^2 + y^2 = 169$ and differentiating gives $2y\frac{dy}{dt} = 0$, so the top "doesn't move". The foot's position $x$ varies, so it must stay a letter until after the derivative.

</div>

<div class="warning" markdown>

Watch out: the signs of the rates. A quantity that is falling has a negative rate, so a tank draining at 0.5 m$^3$/min has $\frac{dV}{dt} = -0.5$. If the answer for a falling level comes out positive, a sign was lost.

</div>

<div class="warning" markdown>

Watch out: mixing units, such as a speed in km/h with a distance in metres, or minutes with seconds. Convert everything to one system before the derivative, and check that the answer's units match the question.

</div>

<div class="warning" markdown>

Watch out: using the average cost as the cost of the next unit. In the cost function above, the average cost at 100 units is \$25, but the next unit costs about \$20. The two are equal only at the minimum of the average cost.

</div>

<div class="warning" markdown>

Watch out: $C'(q)$ is an estimate of the next unit's cost, and not an exact value. It is a good one when the slope of $C$ changes little over one unit. If one unit is a big step (a factory, a flight), use $C(q + 1) - C(q)$.

</div>

<div class="warning" markdown>

Watch out: "$C'(q) = A(q)$" is a condition at a minimum, but it doesn't always produce one. If $C(q) = 50 + 10q$, marginal cost is always \$10 and always below the average cost, so $A$ falls forever and has no minimum. The theorem says what must hold at a minimum, not that a minimum exists.

</div>

## Tricks and shortcuts

Units are a free check. A rate that should be a speed must be a length over a time. In Example 2 the units $\text{m}^3/\text{min}$ divided by $\text{m}^2$ gave m/min, which could only be a speed of the level.

For linear connecting equations, such as shadows, the rates are proportional to each other and there is no need to pick an instant.

For a quadratic cost or profit, the derivative at the midpoint of a step gives the exact change over the step: $P(6) - P(5) = 36 = P'(5.5)$, and $P(9) - P(8) = 12 = P'(8.5)$. For other smooth functions the midpoint estimate is also much better than the left-end estimate.

Near the minimum of average cost, the average cost is flat. At $q = 141.4$, a 10% error in the output (at $q = 127$ or $q = 156$) changes the average cost by under 1%. This is why the exact minimizing quantity matters less than its neighbourhood, a fact about every minimum that [optimization](05-optimization.md) uses.

## In code

The first part checks that the marginal cost estimates the next unit's cost better as $q$ grows. The second finds the integer output with the least average cost by a direct search, and compares it with $q = \sqrt{20000} \approx 141.42$. The third checks the ladder with a difference quotient.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def C(q):
    return 1000 + 10 * q + 0.05 * q**2

def MC(q):
    return 10 + 0.1 * q

# Cost of the next unit against marginal cost, for growing q.
for q in (1, 10, 100, 1000):
    print(q, round(C(q + 1) - C(q), 2), MC(q))
# 1 10.15 10.1
# 10 11.05 11.0
# 100 20.05 20.0
# 1000 110.05 110.0

# Integer output with the smallest average cost.
best = min(range(1, 1001), key=lambda q: C(q) / q)
print(best, round(C(best) / best, 4), round(MC(best), 4))
# 141 24.1422 24.1

# The ladder: top height as the foot moves out at 0.6 m/s.
def y(t):
    return math.sqrt(169 - (5 + 0.6 * t) ** 2)

h = 1e-6
print(round((y(h) - y(0)) / h, 4))
# -0.25
```

The first table shows the error staying at 5 cents however large $q$ gets, so the relative error shrinks. The average cost at 141 is within \$0.001 of the true minimum $10 + 10\sqrt{2} \approx 24.1421$, and the marginal cost at 141 is close to it, as the theorem predicts.

</details>

## FAQ

### Why do economists use a derivative for "the cost of the next unit" when the next unit is a step of 1?

A derivative is a cleaner object: it exists for every $q$, it follows from the rules, and it gives formulas such as $P'(q) = 0$ for the best output. The step of 1 is also arbitrary: the next 0.1 kilograms or the next 1,000 units would have different step costs. The derivative is the limit that doesn't depend on the step. For a firm that makes thousands of units, the two agree to a fraction of a percent. For a firm that makes five aircraft a year, use differences.

### If marginal cost equals average cost, is the average cost always at its minimum?

Not always. The equation $C'(q) = A(q)$ means $A'(q) = 0$, which is a critical point. A critical point can be a minimum, a maximum or neither, and you check which by seeing how $A'$ changes sign. In Example 5, $A'$ goes from negative to positive at $q = 60$, so it is a minimum. [Concavity and curve sketching](04-concavity-and-curve-sketching.md) has the tests.

### Why does the ladder's top speed up so much as it nears the floor?

Because $\frac{dy}{dt} = -\frac{x}{y}\frac{dx}{dt}$ has $y$ in the denominator. When the ladder is nearly flat, a tiny horizontal slide of the foot produces a large vertical drop of the top. The model assumes the ladder stays on the wall, and it doesn't: a real ladder leaves the wall before the top reaches the floor, so the formula's growth to infinity is not a real speed.

## Practice

### Warm-up

1\. A firm's cost is $C(q) = 2000 + 30q + 0.01q^2$ dollars. Find the marginal cost at $q = 400$, use it to estimate the cost of the 401st unit, and compute the exact cost of that unit.

<details class="solution" markdown>
<summary>Solution</summary>

$C'(q) = 30 + 0.02q$, so $C'(400) = 38$. The 401st unit costs about \$38. Exactly, $C(401) - C(400) = 30 + 0.01(401^2 - 400^2) = 30 + 0.01 \cdot 801 = 38.01$.

Check: the error is one cent, which is $\frac{1}{2}C''(400) = \frac{1}{2} \cdot 0.02 = 0.01$.

</details>

2\. An oil slick is a circle whose radius grows at 3 m/min. How fast is its area growing when the radius is 10 m?

<details class="solution" markdown>
<summary>Solution</summary>

$A = \pi r^2$, so $\frac{dA}{dt} = 2\pi r\frac{dr}{dt} = 2\pi \cdot 10 \cdot 3 = 60\pi \approx 188.5$ m$^2$/min.

Check: the units are m$^2$/min. Also the circumference at $r = 10$ is $20\pi$, and a ring of width 3 m has area about $20\pi \cdot 3 = 60\pi$.

</details>

3\. The edge of a cube shrinks at 2 cm/min. How fast is its volume changing when the edge is 6 cm?

<details class="solution" markdown>
<summary>Solution</summary>

$V = s^3$, so $\frac{dV}{dt} = 3s^2\frac{ds}{dt} = 3 \cdot 36 \cdot (-2) = -216$ cm$^3$/min. The volume is falling at 216 cm$^3$/min.

Check: the sign is negative because the edge is shrinking, and the units are cm$^3$/min.

</details>

### Standard

4\. Car A leaves an intersection heading east at 60 km/h, and car B leaves the same intersection at the same moment heading north at 80 km/h. How fast is the distance between them increasing 2 hours later?

<details class="solution" markdown>
<summary>Solution</summary>

Let $x$ and $y$ be the distances of A and B from the intersection and $D$ the distance between them, so $D^2 = x^2 + y^2$. Differentiating, $2D\frac{dD}{dt} = 2x\frac{dx}{dt} + 2y\frac{dy}{dt}$, so $\frac{dD}{dt} = \frac{x \cdot 60 + y \cdot 80}{D}$.

After 2 hours $x = 120$, $y = 160$ and $D = \sqrt{14400 + 25600} = 200$. Then $\frac{dD}{dt} = \frac{7200 + 12800}{200} = 100$ km/h.

Check: the separation speed is 100 km/h at every time, because $D = 100t$: the cars' distance is $\sqrt{(60t)^2 + (80t)^2} = 100t$. The 3-4-5 triangle scaled by $20t$ makes this exact.

</details>

5\. A kite flies 40 m above the ground, carried horizontally by the wind at 3 m/s. How fast is the string being let out when 50 m of string is out? Assume the string is straight.

<details class="solution" markdown>
<summary>Solution</summary>

Let $x$ be the horizontal distance of the kite from the person and $s$ the length of the string, so $s^2 = x^2 + 40^2$, where the height 40 is fixed. Differentiating, $2s\frac{ds}{dt} = 2x\frac{dx}{dt}$, so $\frac{ds}{dt} = \frac{x}{s}\frac{dx}{dt}$.

When $s = 50$, $x = \sqrt{2500 - 1600} = 30$. Then $\frac{ds}{dt} = \frac{30}{50} \cdot 3 = 1.8$ m/s.

Check: the string is let out more slowly than the kite moves horizontally, because the string is longer than the horizontal distance and only part of the kite's motion lengthens it: $1.8 < 3$.

</details>

6\. A firm sells $q$ units at the price $p(q) = 120 - 3q$ dollars, and its cost is $C(q) = 300 + 24q + q^2$ dollars. (a) Find $R'(q)$, $C'(q)$ and $P'(q)$. (b) Find the output $q$ where $R'(q) = C'(q)$. (c) Check that profit there beats profit one unit above and below.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $R(q) = 120q - 3q^2$, so $R'(q) = 120 - 6q$. Also $C'(q) = 24 + 2q$, so $P'(q) = 96 - 8q$.

(b) Set $120 - 6q = 24 + 2q$, so $8q = 96$ and $q = 12$.

(c) $P(q) = 120q - 3q^2 - 300 - 24q - q^2 = -4q^2 + 96q - 300$. Then $P(12) = -576 + 1152 - 300 = 276$, $P(11) = -484 + 1056 - 300 = 272$ and $P(13) = -676 + 1248 - 300 = 272$.

Check: both neighbours are lower, and the price at 12 units is $120 - 36 = 84$ dollars, which is above the marginal cost $24 + 24 = 48$ dollars, so the seller makes a margin on every unit.

</details>

### Challenge

7\. For the cost function $C(q) = F + vq + aq^2$ with $F, v, a > 0$, show that the average cost is smallest at $q = \sqrt{F/a}$, and that the minimum average cost is $v + 2\sqrt{aF}$. Then apply the result to $F = 1000$, $v = 10$, $a = 0.05$.

<details class="solution" markdown>
<summary>Solution</summary>

Here $A(q) = \frac{F}{q} + v + aq$ and $C'(q) = v + 2aq$. At a minimum, $C'(q) = A(q)$, so $v + 2aq = \frac{F}{q} + v + aq$, so $aq = \frac{F}{q}$, so $q^2 = \frac{F}{a}$ and $q = \sqrt{F/a}$.

To see it is a minimum, $A'(q) = \frac{C'(q) - A(q)}{q} = \frac{aq - F/q}{q} = \frac{aq^2 - F}{q^2}$, which is negative for $q < \sqrt{F/a}$ and positive after. At the minimum, $A = \frac{F}{q} + v + aq$ with $\frac{F}{q} = aq = \sqrt{aF}$, so $A = v + 2\sqrt{aF}$.

For $F = 1000$, $v = 10$, $a = 0.05$: $q = \sqrt{20000} \approx 141.42$ and $A = 10 + 2\sqrt{50} = 10 + 10\sqrt{2} \approx 24.14$.

Check: this agrees with the figure, and with the table of values at $q = 100$ (average \$25) and $q = 200$ (average \$25), both above \$24.14.

</details>

8\. (Reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md).) Demand for a product is $q = 200 - 4p$ units at the price $p$ dollars. (a) Find the elasticity at $p = 20$. (b) Check it by computing the percent change in quantity when the price rises 1%. (c) Is it elastic or inelastic, and what does it say about revenue?

<details class="solution" markdown>
<summary>Solution</summary>

(a) At $p = 20$, $q = 120$ and $\frac{dq}{dp} = -4$, so $E = -4 \cdot \frac{20}{120} = -\frac{2}{3} \approx -0.667$.

(b) A 1% rise makes $p = 20.20$ and $q = 200 - 80.80 = 119.2$. The change in quantity is $\frac{119.2 - 120}{120} = -0.00667$, which is $-0.667\%$. The ratio of percent changes is $\frac{-0.667\%}{1\%} = -0.667$, which matches $E$.

(c) $\lvert E \rvert < 1$, so demand is inelastic: a price rise reduces quantity by a smaller percent than it raises the price, so revenue rises. By the formula $\frac{dR}{dp} = q(1 + E) = 120 \cdot \frac{1}{3} = 40$ dollars per dollar of price.

Check: $R = pq = 200p - 4p^2$ has $R'(p) = 200 - 8p = 40$ at $p = 20$. Directly, $R(20) = 2400$ and $R(20.20) = 20.20 \cdot 119.2 = 2407.84$, a gain of about \$7.84, close to $0.2 \cdot 40 = 8$.

</details>

## Where this shows up

- The next lesson, [linear approximation and L'Hopital's rule](02-linear-approximation-and-lhopitals-rule.md), turns "the next unit costs about $C'(q)$" into the approximation $\Delta y \approx f'(x)\,\Delta x$, with an error estimate. [Optimization](05-optimization.md) uses marginal revenue equals marginal cost to find the best output, and [the mean value theorem and extrema](03-mean-value-theorem-and-extrema.md) says why the critical points found there are the right places to look.
- In economics, marginal cost, marginal revenue, average cost and elasticity are the first tools of a microeconomics course (marginal analysis with derivatives<!-- link: ../../07-economics-math/03-firms-and-consumers/01-marginal-analysis-with-derivatives.md -->, production and cost functions<!-- link: ../../07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md -->, elasticity<!-- link: ../../07-economics-math/02-markets/05-elasticity.md -->).
- In CS, a derivative is a sensitivity: how fast a model's loss changes when one parameter changes, or how fast the running time of a program changes as the input grows. Related rates reappear in simulations, where several quantities are updated together at each time step.
