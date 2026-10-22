# Opportunity cost and the PPC

After this lesson you can compute an opportunity cost as a ratio, read the slope of a production possibilities curve as an opportunity cost, tell efficient, inefficient and unattainable points apart, and explain with a derivative why a bowed-out curve means increasing opportunity cost.

Before this: [forms of linear equations](../../03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md) and [two-variable inequalities and feasible regions](../../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md). The bowed-out curve uses [concavity](../../05-university-core/03-applications-of-derivatives/04-concavity-and-curve-sketching.md). For the graph habits of economics, see [how economists use math and graphs](../01-measuring-the-economy/01-how-economists-use-math-and-graphs.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. In 10 hours a student can write 5 essays (2 hours each) or finish 20 problem sets (half an hour each), and any mix of the two that fills the 10 hours. What does one essay cost in problem sets?
2. A country can make the amounts of wheat $w$ and canola $c$ (thousand tonnes) that satisfy $w^2 + c^2 \le 100$, and its PPC is the curve $w^2 + c^2 = 100$. Is $(7, 7)$ attainable? Is it efficient? What about $(7, 8)$?
3. On the curve $c = \sqrt{100 - w^2}$, what does one more thousand tonnes of wheat cost in canola at $w = 8$, to a good approximation?

<details class="solution" markdown>
<summary>Answers</summary>

1. One essay takes 2 hours, which is the time for 4 problem sets, so an essay costs 4 problem sets.
2. For $(7, 7)$ we get $49 + 49 = 98 \le 100$, so it is attainable, but $98 < 100$ means it is inside the curve, so it is not efficient. For $(7, 8)$ we get $49 + 64 = 113 > 100$, so it is unattainable.
3. The slope of the curve at $w = 8$ is $\frac{dc}{dw} = -\frac{w}{\sqrt{100 - w^2}} = -\frac{8}{6} = -\frac{4}{3}$, so one more thousand tonnes of wheat costs about $\frac{4}{3}$ thousand tonnes of canola.

</details>

## The idea

A small bakery has one oven and 8 hours a day. In an hour the oven bakes 15 loaves or 30 buns. Every hour spent on loaves is an hour not spent on buns, so baking more of one means baking less of the other. If you want 15 more loaves, you give up 30 buns. That give-up is the cost that matters, and it has nothing to do with dollars: it is the best alternative that you no longer get.

Economists call this the opportunity cost, and they draw it. Put loaves on the horizontal axis and buns on the vertical axis, and mark every combination the bakery could make in a day. The outer edge of that set of combinations is a curve, the production possibilities curve (PPC). Points on or under the curve are possible, and points above it are not. Moving along the curve, one good goes up and the other goes down, and the slope tells you how fast.

This is the first picture of economics, and almost every later idea is built on it: why trade helps, why supply curves slope up, why choices have prices. The mathematics is the same you met in the [feasible region lesson](../../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md): a PPC is the outer boundary of a feasible region, and the budget line there was a PPC for a shopper.

![Two graphs. Left: a straight PPC for a bakery, from 240 buns at 0 loaves to 120 loaves at 0 buns, with the efficient point A at (60, 120) on the line, the inefficient point B at (30, 90) below it and the unattainable point C at (90, 150) above it. Right: a bowed-out PPC for wheat and canola with tangent slopes of minus 3/4 at (6, 8) and minus 4/3 at (8, 6), an inefficient point at (4, 5), an unattainable point at (9, 9) and a dashed larger curve showing growth.](../../assets/figures/07-economics-math/opportunity-cost-and-the-ppc-ppc.svg)

## Definitions

The **opportunity cost** of an action is the value of the best alternative you give up by taking it. When there are two goods $X$ and $Y$, the opportunity cost of one more unit of $X$ is the number of units of $Y$ given up to get it:

$$
\text{opportunity cost of } X = \frac{\text{units of } Y \text{ given up}}{\text{units of } X \text{ gained}}.
$$

In plain words, it is a ratio with a "per" in it: buns per loaf. It is measured in the other good, not in dollars, and it changes if you swap which good you call $X$.

A **production possibilities curve** (PPC, also called a production possibilities frontier) shows, for two goods, the largest amount of one good that can be produced for each amount of the other, when all resources are fully used and technology is fixed. The **production possibilities set** is the curve together with everything under it and in the first quadrant.

In plain words, the curve is the edge of what is possible with what you have. The set is a feasible region, as in the [earlier lesson](../../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#definitions), and the amounts can't be negative.

Points are sorted into three kinds:

- A point is **attainable** if it is in the set. A point above the curve is **unattainable**: the resources can't produce it.
- A point on the curve is **efficient** (more exactly, productively efficient): you can't make more of one good without making less of the other.
- A point strictly inside the set is **inefficient**: some resources are idle or badly used, and you could make more of at least one good without making less of the other.

Finally, the opportunity cost is **constant** along a stretch of the curve if the ratio above is the same for every move along it, and **increasing** if it grows as you make more of $X$. An opportunity cost can also be decreasing, but that is unusual for a whole economy.

## How to do it

### The slope is the opportunity cost

Write the PPC as a decreasing function $y = f(x)$, so that $y$ is the most of the second good you can make when you make $x$ of the first. For a small move from $x$ to $x + \Delta x$, you give up $f(x) - f(x + \Delta x) = -\Delta y$ units of $y$ and gain $\Delta x$ units of $x$. So

$$
\text{opportunity cost of } x \approx \frac{-\Delta y}{\Delta x} = -\text{slope}.
$$

In the limit the opportunity cost of $x$ at a point is $-f'(x)$, the slope with its minus sign removed. The slope of a PPC is negative, because making more of one good means less of the other, but an opportunity cost is quoted as a positive number.

*Theorem 1 (straight PPC).* Suppose a PPC is a straight line that meets the axes at $(X_{\max}, 0)$ and $(0, Y_{\max})$. Then the opportunity cost of $x$ is the same everywhere, equal to $\frac{Y_{\max}}{X_{\max}}$, and the opportunity cost of $y$ is its reciprocal $\frac{X_{\max}}{Y_{\max}}$.

What we know: the line passes through two points, so its slope is rise over run. What we want: the opportunity cost along the whole line. The plan is to compute the slope and read it as a ratio.

*Proof.* The slope between $(X_{\max}, 0)$ and $(0, Y_{\max})$ is $\frac{0 - Y_{\max}}{X_{\max} - 0} = -\frac{Y_{\max}}{X_{\max}}$. A line has the same slope everywhere, so every move along it gives up $\frac{Y_{\max}}{X_{\max}}$ units of $y$ per unit of $x$ gained. Moving the other way, a move of $\Delta y$ in $y$ comes with a move of $\Delta x = \frac{X_{\max}}{Y_{\max}}\Delta y$ in the other direction, so each extra unit of $y$ costs $\frac{X_{\max}}{Y_{\max}}$ units of $x$. $\blacksquare$

Look back: for the bakery, $X_{\max} = 120$ loaves and $Y_{\max} = 240$ buns, so a loaf costs 2 buns and a bun costs half a loaf. The two costs are reciprocals, which is why you must say which good is the "cost" and which is the "gain". A straight PPC means that every unit of the resource is equally good at both jobs, as an hour of oven time is.

### Why most PPCs bow outward

Take a country with farmland that is better for wheat in some places and better for canola in others. At first, wheat goes on the best wheat land, so a lot of wheat costs little canola. As wheat expands onto land that suits canola better, each extra tonne of wheat costs more canola. The opportunity cost of wheat rises as wheat output rises, and the curve gets steeper as you move to the right. A curve whose slope gets steeper downward as $x$ grows is bowed outward, which is the shape of the quarter circle in the figure.

The calculus statement is a theorem.

*Theorem 2 (increasing opportunity cost means concave).* Let $y = f(x)$ be a twice differentiable PPC with $f'(x) < 0$ on an interval. If $f''(x) < 0$ on the interval, the opportunity cost $-f'(x)$ is increasing there, and the curve is concave (it bows outward). If $f''(x) = 0$ on the interval, the cost is constant, and if $f''(x) > 0$ it is decreasing.

What we know: the opportunity cost is $-f'(x)$, and the sign of a derivative tells whether a function increases (see [concavity and curve sketching](../../05-university-core/03-applications-of-derivatives/04-concavity-and-curve-sketching.md)). What we want: when $-f'$ is increasing. The plan is to differentiate $-f'$.

*Proof.* The derivative of $-f'(x)$ is $-f''(x)$. A function whose derivative is positive on an interval is increasing there, and one whose derivative is 0 is constant. If $f'' < 0$ then $-f'' > 0$, so $-f'$ is increasing. If $f'' = 0$ then $-f'' = 0$ and $-f'$ is constant. If $f'' > 0$ then $-f'' < 0$ and $-f'$ is decreasing. $\blacksquare$

Look back with the example $c = \sqrt{100 - w^2}$. Here $c' = -\frac{w}{\sqrt{100 - w^2}}$, so the opportunity cost of wheat is $\frac{w}{\sqrt{100 - w^2}}$, which is $\frac{3}{4}$ at $w = 6$ and $\frac{4}{3}$ at $w = 8$. Also $c'' = -\frac{100}{(100 - w^2)^{3/2}} < 0$ for $0 \le w < 10$, so the curve is concave and the cost rises throughout. The theorem also explains why a straight line is the borderline: $f'' = 0$, and the cost is constant.

### Reading a PPC problem

1. Name the two goods and decide which one goes on which axis, with units (loaves per day, thousand tonnes).
2. Find the two intercepts: the most of each good if all resources go to it. For a straight PPC these are all you need.
3. For a straight PPC, the opportunity cost of the horizontal good is $\frac{Y_{\max}}{X_{\max}}$. For a curved PPC, differentiate: it is $-\frac{dy}{dx}$ at the point.
4. To classify a point, compare it with the curve. With the PPC written as $g(x, y) = 0$ and attainable points as $g(x, y) \le 0$, substitute the point: $<0$ is inefficient, $=0$ is efficient, $>0$ is unattainable.
5. For growth, redraw the curve with the new intercepts, and say which good's intercept moved.
6. Check units and signs: opportunity costs are positive, and "units of the other good per unit of this one".

### Economic growth

If the economy gets more resources (more workers, more machines) or better technology, the PPC moves outward, and points that were unattainable become attainable. If the technology improves for one good only, the intercept of that good moves out and the other stays put, so the curve pivots. Growth does not happen by moving along the curve, because that is a different choice with the same resources. A point inside the curve moves to the curve by using idle resources, which is not growth either.

## Worked examples

<div class="example" markdown>

### Example 1: the bakery

The bakery (a made-up one) has 8 hours of oven time a day, and the oven bakes 15 loaves or 30 buns an hour. Find its PPC, the opportunity cost of a loaf and of a bun, and classify the points $(60, 120)$, $(30, 90)$ and $(90, 150)$, with $L$ loaves and $B$ buns a day.

Step 1: the goods are loaves $L$ (horizontal) and buns $B$ (vertical).

Step 2: if all 8 hours go to loaves, $L = 8 \times 15 = 120$. If all go to buns, $B = 8 \times 30 = 240$. The intercepts are $(120, 0)$ and $(0, 240)$.

Step 3: the PPC is the line between them. Its equation comes from the hours: loaves take $\frac{L}{15}$ hours and buns take $\frac{B}{30}$ hours, so full use of the oven means

$$
\frac{L}{15} + \frac{B}{30} = 8, \qquad \text{which simplifies to} \qquad B = 240 - 2L.
$$

The slope is $-2$. By Theorem 1 the opportunity cost of one loaf is $\frac{240}{120} = 2$ buns, and of one bun it is $\frac{1}{2}$ loaf.

Step 4: compute the hours each point needs. For $(60, 120)$: $\frac{60}{15} + \frac{120}{30} = 4 + 4 = 8$ hours, exactly the oven's day, so it is efficient. For $(30, 90)$: $2 + 3 = 5$ hours, so 3 hours of oven time are idle and the point is inefficient. For $(90, 150)$: $6 + 5 = 11$ hours, more than 8, so it is unattainable.

Check: using the equation $B = 240 - 2L$ at $L = 60$ gives $B = 120$, on the line. At $L = 30$ the line gives 180, and 90 is below it. At $L = 90$ the line gives 60, and 150 is above it.

</div>

<div class="example" markdown>

### Example 2: increasing opportunity cost

A country's wheat $w$ and canola $c$, in thousand tonnes, satisfy $w^2 + c^2 = 100$ on the PPC (made-up numbers). Find the opportunity cost of wheat at $w = 6$ and $w = 8$, and the exact cost of raising wheat from 6 to 7 and from 7 to 8.

Solving for $c$ gives $c = \sqrt{100 - w^2}$. Differentiating with the chain rule: $c' = \frac{-2w}{2\sqrt{100 - w^2}} = -\frac{w}{c}$. So the opportunity cost of wheat is $\frac{w}{c}$.

At $w = 6$ we have $c = 8$ and the cost is $\frac{6}{8} = \frac{3}{4}$. At $w = 8$ we have $c = 6$ and the cost is $\frac{8}{6} = \frac{4}{3}$. The cost has almost doubled.

For the exact moves: $c(6) = 8$, $c(7) = \sqrt{51} \approx 7.1414$ and $c(8) = 6$. Raising wheat from 6 to 7 costs $8 - 7.1414 = 0.8586$ canola, and from 7 to 8 costs $7.1414 - 6 = 1.1414$.

Check: the second move costs more than the first, as increasing cost says. Each exact cost also lies between the slopes at its ends: $0.75 < 0.8586 < \frac{7}{\sqrt{51}} \approx 0.980$ and $0.980 < 1.1414 < 1.333$. The total, $0.8586 + 1.1414 = 2$, is the full drop from $c = 8$ to $c = 6$.

</div>

<div class="example" markdown>

### Example 3: improving one good only

The bakery buys a new bun tray, and the oven now bakes 40 buns an hour. Loaves are still 15 an hour. Find the new PPC and say what happened to the opportunity cost of a loaf.

Loaves: $L = 120$ at most, as before. Buns: $B = 8 \times 40 = 320$ at most. The hours equation is $\frac{L}{15} + \frac{B}{40} = 8$, so $B = 320 - \frac{8}{3}L$.

The new slope is $-\frac{8}{3} \approx -2.67$, steeper than $-2$. A loaf now costs $\frac{8}{3}$ buns, and a bun costs $\frac{3}{8}$ of a loaf. Improving the bun tray made buns cheaper in loaves, and loaves dearer in buns. The curve pivots about the loaf intercept $(120, 0)$.

Check: at $L = 60$ the new line gives $B = 320 - 160 = 160$, and the hours are $4 + 4 = 8$. The old point $(60, 120)$ is now inside the curve, since $120 < 160$: with the better tray the bakery could make 40 more buns without giving up any loaves.

</div>

<div class="example" markdown>

### Example 4: a factory (finish it yourself)

A made-up factory, in a week, can make 100 phones or 40 tablets, and any mix of them in proportion (so the PPC is straight). Find the opportunity cost of a tablet, and decide whether the plan of 50 phones and 20 tablets is efficient.

Step 1: put tablets $t$ on the horizontal axis and phones $p$ on the vertical axis.

Step 2: the intercepts are $t = 40$ and $p = 100$.

Now do Step 3, the opportunity cost of a tablet, and then Step 4, classifying $(t, p) = (20, 50)$. Using the equation $\frac{t}{40} + \frac{p}{100} = 1$ for the line, test the point.

<details class="solution" markdown>
<summary>Finish</summary>

Step 3: a tablet costs $\frac{100}{40} = 2.5$ phones, and a phone costs $\frac{40}{100} = 0.4$ tablet.

Step 4: $\frac{20}{40} + \frac{50}{100} = 0.5 + 0.5 = 1$, so the point is on the line, which makes it efficient. A plan of 60 phones and 20 tablets would give $0.5 + 0.6 = 1.1 > 1$, so it would be unattainable.

Check: the PPC is $p = 100 - 2.5t$, and at $t = 20$ it gives $p = 50$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the direction of the ratio. On the bakery graph the slope is $-2$ and the opportunity cost of a loaf is 2 buns. The opportunity cost of a bun is $\frac{1}{2}$ loaf, not 2. The slope of a PPC is the cost of the good on the horizontal axis, in units of the vertical good. To get the cost of the vertical good, flip the fraction.

</div>

<div class="warning" markdown>

Watch out: the money you spend is only part of an opportunity cost. Suppose you go to a 3-hour movie that costs \$15 instead of working a 3-hour shift at \$20 an hour. The cost of the choice is the \$15 ticket plus the \$60 of pay you gave up, \$75 in all, not just \$15. A cost you would pay either way, such as rent that is due whatever you do tonight, is not an opportunity cost of the choice. Count what changes with the choice, and count the best alternative you give up.

</div>

<div class="warning" markdown>

Watch out: efficient does not mean best. Every point on the PPC is efficient, including $(120, 0)$ with no buns at all. Which efficient point is chosen depends on what people want, which the PPC does not show. Also, a point being unattainable is a statement about today's resources and technology, and growth can change it.

</div>

<div class="warning" markdown>

Watch out: an outward shift is not a move along the curve. Making more wheat and less canola moves you along the PPC. Growth moves the curve itself. The same is true of an inefficient point: using idle resources moves the economy from inside the set to the curve, with no change in the curve.

</div>

The PPC is not always smooth. If making goods needs two resources and each is limited, the boundary is made of straight pieces with corners, and the opportunity cost jumps at each corner. Challenge problem 7 works one out, and the cost still rises from piece to piece. Also, the whole story assumes that the amounts of both goods can be any non-negative number. For goods that come in whole units, the PPC is a set of dots, and the line is only a convenient approximation.

## Tricks and shortcuts

For a straight PPC, the opportunity cost of the horizontal good is $\frac{Y_{\max}}{X_{\max}}$: the vertical intercept divided by the horizontal intercept. For an hours table, it is the ratio of hours per unit: if a loaf takes $\frac{1}{15}$ of an hour and a bun $\frac{1}{30}$, a loaf costs $\frac{1/15}{1/30} = 2$ buns. The next lesson uses this to compare producers.

To classify a point for a PPC that is an equation, put it in the "less than or equal" form and substitute, as in Step 4 of the method. For $w^2 + c^2 \le 100$, the points $(6, 8)$, $(4, 5)$ and $(9, 9)$ give $100$, $41$ and $162$.

A curve that bows outward has an opportunity cost that rises as you go right and falls as you go left, so a move that is cheap in one direction is expensive in the other. For a rough check, a drawn PPC is steeper on the right than on the left.

## In code

The opportunity cost along a curve is minus the slope, and a finite difference approximates it. The classification of a point is a comparison.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def canola(w):
    return math.sqrt(100 - w * w)

def opp_cost(w, h=1e-6):
    # minus the slope, from a small step
    return (canola(w) - canola(w + h)) / h

print(round(opp_cost(6), 4), round(opp_cost(8), 4))
# 0.75 1.3333

def classify(w, c):
    g = w * w + c * c
    if g > 100:
        return "unattainable"
    return "efficient" if g == 100 else "inefficient"

print(classify(6, 8), classify(4, 5), classify(9, 9))
# efficient inefficient unattainable
```

The step `h` is small enough that the difference quotient matches the derivative to four decimal places. The exact comparison `g == 100` works here only because the numbers are whole; for measured data you would use a tolerance.

</details>

## FAQ

### Why is the opportunity cost in the other good and not in dollars?

Because the PPC has no prices in it. It shows what the economy can physically make. Dollars come in when you add prices, and then a price ratio plays the same role: on the budget line from the [feasible region lesson](../../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#a-budget-constraint), the slope $-\frac{p_x}{p_y}$ is the opportunity cost in the market of one more unit of $x$.

### Could a PPC bow inward?

Yes, as a mathematical possibility: by Theorem 2, $f'' > 0$ gives a decreasing opportunity cost. It could happen when making more of a good makes a producer better at it, so that the next unit costs less. Intro economics mostly takes increasing cost as normal, because resources are rarely equally good at everything, and draws the curve bowed outward.

### Is the PPC the same as a demand or supply curve?

No. A PPC has two goods on its axes and shows what is physically possible. Demand and supply have a price and one good. The PPC does connect to supply: the opportunity cost of making the next unit of a good is the cost that sits behind a supply curve, which the [supply and demand lesson](03-supply-and-demand-equilibrium-algebra.md) draws.

### What if the opportunity cost is zero?

Then the goods don't compete for the same resources, and that part of the PPC is flat or vertical: making more of one good costs none of the other. It happens at an inefficient point with idle resources, where putting an idle worker to a job gives up nothing.

## Practice

### Warm-up

1\. In 6 hours Maya can make 3 posters or 12 slide decks, in any mix. (a) What does one poster cost in slide decks? (b) What does one slide deck cost in posters?

<details class="solution" markdown>
<summary>Solution</summary>

(a) A poster takes $\frac{6}{3} = 2$ hours and a deck takes $\frac{6}{12} = 0.5$ hour, so a poster costs $\frac{2}{0.5} = 4$ decks. (b) A deck costs the reciprocal, $\frac{1}{4}$ of a poster.

Check: the intercepts are 3 posters and 12 decks, and $\frac{12}{3} = 4$ decks per poster.

</details>

2\. The bakery's PPC is $2L + B = 240$. Classify each point as efficient, inefficient or unattainable: $(50, 130)$, $(70, 100)$, $(100, 60)$ and $(20, 200)$.

<details class="solution" markdown>
<summary>Solution</summary>

Compute $2L + B$ for each. For $(50, 130)$: $100 + 130 = 230 < 240$, inefficient. For $(70, 100)$: $140 + 100 = 240$, efficient. For $(100, 60)$: $200 + 60 = 260 > 240$, unattainable. For $(20, 200)$: $40 + 200 = 240$, efficient.

Check: at $L = 70$ the line gives $B = 240 - 140 = 100$, and at $L = 20$ it gives 200. At $L = 100$ it gives 40, and 60 is above that.

</details>

3\. On the curve $w^2 + c^2 = 100$, how much canola can be made when wheat is 6, and when wheat is 9? Is $(6, 8.5)$ attainable?

<details class="solution" markdown>
<summary>Solution</summary>

At $w = 6$: $c = \sqrt{100 - 36} = 8$. At $w = 9$: $c = \sqrt{100 - 81} = \sqrt{19} \approx 4.359$. For $(6, 8.5)$: $36 + 72.25 = 108.25 > 100$, so it is unattainable.

Check: $6^2 + 8^2 = 100$ and $9^2 + 4.359^2 = 81 + 19.0 = 100$. The point $(6, 8.5)$ is above the curve, because the curve is at 8 when $w = 6$.

</details>

### Standard

4\. For $c = \sqrt{100 - w^2}$, find the opportunity cost of wheat at $w = 3$ and $w = 9$, and explain what the change says about the shape.

<details class="solution" markdown>
<summary>Solution</summary>

The opportunity cost of wheat is $-c'(w) = \frac{w}{\sqrt{100 - w^2}}$. At $w = 3$ it is $\frac{3}{\sqrt{91}} \approx 0.314$ canola per wheat. At $w = 9$ it is $\frac{9}{\sqrt{19}} \approx 2.065$.

The cost has risen by a factor of about 6.6 as wheat went from 3 to 9. A cost that rises with wheat output means the curve is concave, steeper to the right, and bowed outward.

Check: $0.314 < \frac{3}{4} < \frac{4}{3} < 2.065$ matches the earlier values at $w = 6$ and $w = 8$, so the cost increases along the whole curve.

</details>

5\. Every resource grows by 20%, so the PPC becomes $w^2 + c^2 = 144$. (a) How much canola can the country make now when wheat is 6, and how much more is that than before? (b) What is the opportunity cost of wheat at $w = 6$ now?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $c = \sqrt{144 - 36} = \sqrt{108} \approx 10.392$. Before it was 8, so the gain is about 2.392 thousand tonnes of canola at the same wheat output.

(b) The cost is $\frac{w}{c} = \frac{6}{10.392} \approx 0.577$, lower than the old $0.75$ at $w = 6$. At the same wheat output the economy is now at a flatter part of the new curve. At the scaled point $(7.2, 9.6)$, the cost is $\frac{7.2}{9.6} = 0.75$ again, because growing every resource by the same factor scales the picture up without changing its shape.

Check: $6^2 + 10.392^2 = 36 + 108 = 144$, and $7.2^2 + 9.6^2 = 51.84 + 92.16 = 144$.

</details>

6\. The bakery improves its loaf oven so that it bakes 20 loaves an hour; buns stay at 30 an hour. (a) Find the new PPC. (b) Find both opportunity costs. (c) Is the old point $(60, 120)$ still efficient?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The intercepts are $L = 8 \times 20 = 160$ and $B = 240$. The hours equation $\frac{L}{20} + \frac{B}{30} = 8$ gives $B = 240 - 1.5L$.

(b) A loaf costs $\frac{240}{160} = 1.5$ buns, and a bun costs $\frac{2}{3}$ of a loaf.

(c) At $L = 60$ the new line gives $B = 240 - 90 = 150$. The point $(60, 120)$ has $B = 120 < 150$, so it is inside the new curve and inefficient.

Check: the hours for $(60, 120)$ are $3 + 4 = 7 < 8$, an idle hour. The loaf has become cheaper in buns (from 2 to 1.5), and the bun dearer in loaves (from $\frac{1}{2}$ to $\frac{2}{3}$).

</details>

### Challenge

7\. A firm makes phones $p$ and tablets $t$. A phone needs 1 hour of labour and 2 hours of machine time, and a tablet needs 2 hours of labour and 1 hour of machine time. It has 100 hours of labour and 120 hours of machine time a week. (a) Write the two constraints and find the corners of the production possibilities set. (b) Find the opportunity cost of a phone on each piece of the PPC. (c) Is the cost increasing?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Labour: $p + 2t \le 100$. Machines: $2p + t \le 120$. With $p, t \ge 0$. The corners are $(p, t) = (0, 0)$, $(60, 0)$, $(0, 50)$ and the crossing of the two lines. Solving $p + 2t = 100$ and $2p + t = 120$: from the first, $p = 100 - 2t$, so $200 - 4t + t = 120$, giving $t = \frac{80}{3}$ and $p = \frac{140}{3}$. The crossing is $\left(\frac{140}{3}, \frac{80}{3}\right) \approx (46.7, 26.7)$, and it satisfies both constraints.

(b) The PPC runs from $(0, 50)$ to the crossing, then to $(60, 0)$. On the first piece the slope is $\frac{80/3 - 50}{140/3 - 0} = -\frac{70/3}{140/3} = -\frac{1}{2}$, so a phone costs $\frac{1}{2}$ tablet (labour is the limit). On the second piece the slope is $\frac{0 - 80/3}{60 - 140/3} = -\frac{80/3}{40/3} = -2$, so a phone costs 2 tablets (the machines are the limit).

(c) Yes: the cost rises from $\frac{1}{2}$ to 2 as phone output goes up, so the PPC is concave with a corner, even though both constraints are straight lines.

Check: $\frac{140}{3} + 2 \cdot \frac{80}{3} = \frac{300}{3} = 100$ and $2 \cdot \frac{140}{3} + \frac{80}{3} = \frac{360}{3} = 120$. The corner $(60, 0)$ uses all 120 machine hours and 60 labour hours, and $(0, 50)$ uses all 100 labour hours and 50 machine hours.

</details>

8\. (Reviews [budget lines](../../03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md#a-budget-constraint).) A student has \$120 a week to spend on books at \$20 each and coffees at \$4 each. (a) What is the opportunity cost of a book in coffees? (b) The student's allowance rises to \$160 and a coffee now costs \$5. Find the new intercepts and the new opportunity cost of a book. (c) Does the line shift or pivot?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The budget line is $20x + 4y = 120$, with intercepts 6 books and 30 coffees. The slope is $-\frac{20}{4} = -5$, so a book costs 5 coffees.

(b) With \$160 and \$5 coffees the line is $20x + 5y = 160$, with intercepts $\frac{160}{20} = 8$ books and $\frac{160}{5} = 32$ coffees. A book now costs $\frac{20}{5} = 4$ coffees.

(c) The book intercept moved from 6 to 8 and the coffee intercept from 30 to 32, and the slope changed from $-5$ to $-4$. So the line does not just shift in parallel: it moves and rotates, because both income and a price changed.

Check: $20(6) + 4(0) = 120$ and $20(0) + 4(30) = 120$ for the old line; $20(8) = 160$ and $5(32) = 160$ for the new one. The intercept ratios, $\frac{30}{6} = 5$ and $\frac{32}{8} = 4$, match the slopes.

</details>

## Where this shows up

- The next lesson, [comparative advantage and gains from trade](02-comparative-advantage-and-gains-from-trade.md), compares the opportunity costs of two producers, and the supply curve of the [supply and demand lesson](03-supply-and-demand-equilibrium-algebra.md) is built from the opportunity costs of sellers.
- Increasing opportunity cost is the same fact as rising marginal cost, which firms meet in [marginal analysis with derivatives](../03-firms-and-consumers/01-marginal-analysis-with-derivatives.md) and in [production and cost functions](../03-firms-and-consumers/02-production-and-cost-functions.md).
- In CS, a time budget is a PPC: with a fixed number of hours, every feature you add has an opportunity cost in other features or in testing, and a latency and accuracy trade-off for a model is a frontier of efficient points.
