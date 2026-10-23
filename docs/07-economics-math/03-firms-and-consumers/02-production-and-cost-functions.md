# Production and cost functions

After this lesson you can find marginal and average product from a production function, prove the returns to scale of a Cobb-Douglas function from the sum of its exponents, compute and interpret the marginal rate of technical substitution, and derive a firm's short-run cost curves from its production function.

Before this: [marginal analysis with derivatives](01-marginal-analysis-with-derivatives.md) and [partial derivatives and the gradient](../../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md), which introduced marginal products and the Cobb-Douglas function.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A firm has $Q = 5K^{0.6}L^{0.6}$. If it triples both inputs, by what factor does output change?
2. With capital fixed, $Q = 4\sqrt{L}$. At $L = 25$, find the marginal product and the average product of labour. Is the average product rising or falling?
3. A firm's total cost is $C(Q) = 50 + 4Q^2$. Find marginal cost, average cost and average variable cost at $Q = 5$.

<details class="solution" markdown>
<summary>Answers</summary>

1. Output is multiplied by $3^{0.6 + 0.6} = 3^{1.2} \approx 3.74$, more than triple.
2. $MP_L = \frac{2}{\sqrt{L}} = 0.4$ and $AP_L = \frac{4\sqrt{L}}{L} = 0.8$. The marginal product is below the average, so the average is falling.
3. $MC = 8Q = 40$, $AC = \frac{50}{5} + 4 \cdot 5 = 30$ and $AVC = 4Q = 20$ dollars per unit.

</details>

## The idea

A bakery has one oven and hires bakers. The first baker can do little: someone has to mix, shape, bake and sell. The second and third let the work be divided, so each adds more than the one before. Eventually the kitchen is crowded, bakers wait for the oven, and the tenth adds almost nothing. That curve, output against workers with the oven fixed, is a production function, and its shape explains the shape of the bakery's cost curves.

The link is one line of algebra. If an extra hour of labour adds $MP$ loaves and costs the wage $w$, then an extra loaf costs $\frac{w}{MP}$ in wages. So when the marginal product of labour is high, the marginal cost of output is low, and when crowding makes it fall, the marginal cost rises. The textbook U-shaped cost curves are the production function turned upside down.

The word "run" matters. In the short run some input, usually capital (the oven, the building), can't be changed, so that part of the bill is fixed. In the long run every input can be changed. The long-run question has a second part: when the firm gets bigger, does output grow faster or slower than inputs? That is returns to scale, and for the Cobb-Douglas function it is read off one number.

## Definitions

A **production function** $Q = f(K, L)$ gives the largest output $Q$ that a firm can make from $K$ units of capital and $L$ hours of labour. In the **short run**, at least one input (here $K = \bar{K}$) is fixed. In the **long run**, all inputs can be changed.

The **marginal product** of labour is $MP_L = \frac{\partial Q}{\partial L}$, the extra output from one more hour with capital held fixed, and $MP_K = \frac{\partial Q}{\partial K}$ is defined the same way. The **average product** of labour is $AP_L = \frac{Q}{L}$. In plain words, marginal product is the output of the last worker and average product is the output per worker.

**Diminishing marginal returns** means that the marginal product of an input falls as that input rises while the others are held fixed: $\frac{\partial^2 Q}{\partial L^2} < 0$. In plain words, the tenth worker in the same kitchen adds less than the ninth.

An **isoquant** is a level curve of the production function, the set of input pairs $(K, L)$ that make the same output. The **marginal rate of technical substitution** is

$$
MRTS = -\frac{dK}{dL}\bigg|_{Q \text{ fixed}} = \frac{MP_L}{MP_K},
$$

the amount of capital the firm can give up for one more hour of labour at the same output. In plain words, it is the slope of the isoquant, made positive.

**Returns to scale** describe what happens when every input is multiplied by $s > 1$. They are increasing if $f(sK, sL) > s\,f(K, L)$ for every such $s$, constant if the two are equal, and decreasing if the left side is smaller. A **Cobb-Douglas** production function is $Q = AK^{a}L^{b}$ with constants $A > 0$, $a > 0$ and $b > 0$. (The exponents are $\alpha$ and $\beta$ in the university core lessons, and are written $a$ and $b$ here to match the utility function in [utility and indifference curves](04-utility-and-indifference-curves.md).)

The cost terms follow from lesson 1. The **total cost** is $TC(Q) = FC + VC(Q)$, with the **fixed cost** $FC$ independent of output and the **variable cost** $VC(Q)$ the cost of the inputs that change. The averages are $AFC = \frac{FC}{Q}$, $AVC = \frac{VC}{Q}$ and $AC = \frac{TC}{Q} = AFC + AVC$ (the average total cost), and $MC = \frac{dTC}{dQ}$.

## How to do it

### Marginal and average product

1. Differentiate the production function in the one input that varies, holding the other fixed: $MP_L = \frac{dQ}{dL}$.
2. Compute $AP_L = \frac{Q}{L}$.
3. Compare them. By [Theorem 2 of the last lesson](01-marginal-analysis-with-derivatives.md#average-against-marginal) with $T = Q(L)$, we have $AP_L' = \frac{MP_L - AP_L}{L}$. So $AP_L$ rises while $MP_L > AP_L$ and falls while $MP_L < AP_L$, and the two are equal where $AP_L$ is at a peak.

The marginal product usually has three stages. At first it rises, because workers can specialize. Then it falls (diminishing marginal returns) but stays positive. Finally it may reach zero, where more labour adds nothing. Example 1 has all three.

### Cobb-Douglas: returns to scale and marginal products

*Theorem 1.* For $Q = AK^aL^b$ and every $s > 0$,

$$
f(sK, sL) = s^{a+b}f(K, L).
$$

So returns to scale are increasing if $a + b > 1$, constant if $a + b = 1$ and decreasing if $a + b < 1$. The marginal products are $MP_K = a\frac{Q}{K}$ and $MP_L = b\frac{Q}{L}$, and

$$
K\cdot MP_K + L\cdot MP_L = (a + b)\,Q.
$$

What we know: the exponent laws $(sx)^a = s^ax^a$ and $s^as^b = s^{a+b}$. What we want: output after scaling, as a multiple of the original output. The plan is to pull the $s$ out of each power.

*Proof.* $f(sK, sL) = A(sK)^a(sL)^b = As^aK^as^bL^b = s^{a+b}AK^aL^b = s^{a+b}f(K, L)$. If $a + b > 1$ and $s > 1$ then $s^{a+b} > s$, so output grows by more than the factor $s$; if $a + b = 1$ it grows by exactly $s$; if $a + b < 1$ by less. For the marginal products, $\frac{\partial Q}{\partial K} = aAK^{a-1}L^b = a\frac{Q}{K}$, and likewise $\frac{\partial Q}{\partial L} = b\frac{Q}{L}$. Then $K\cdot MP_K + L\cdot MP_L = aQ + bQ = (a + b)Q$. $\blacksquare$

Look back: the exponent $a$ is also the output elasticity of capital, since $\frac{K}{Q}MP_K = a$: a 1% rise in capital raises output by about $a$%. Diminishing marginal returns and returns to scale are different questions. Marginal returns change one input; returns to scale change all of them together. With $a = b = 0.6$ each marginal product falls as its own input grows (because $0.6 < 1$), yet scaling both inputs gives increasing returns to scale, since $a + b = 1.2$. The last identity has a use too: if returns to scale are constant, paying each input its marginal product uses up the whole output, $K\,MP_K + L\,MP_L = Q$.

### The isoquant and the MRTS

*Theorem 2.* For $Q = AK^aL^b$, along an isoquant

$$
MRTS = \frac{b}{a}\cdot\frac{K}{L},
$$

and it falls as one moves along the isoquant towards more labour and less capital. So the isoquants are convex.

What we know: along an isoquant $Q(K, L) = \bar{Q}$ stays constant, so by the chain rule $MP_K\,dK + MP_L\,dL = 0$. What we want: $-\frac{dK}{dL}$. The plan is to solve for it and substitute the Cobb-Douglas marginal products.

*Proof.* From $MP_K\,dK + MP_L\,dL = 0$ we get $-\frac{dK}{dL} = \frac{MP_L}{MP_K}$, which is the definition of the MRTS. For Cobb-Douglas, $\frac{MP_L}{MP_K} = \frac{bQ/L}{aQ/K} = \frac{b}{a}\cdot\frac{K}{L}$. Along the isoquant, moving to more labour and less capital lowers $K$ and raises $L$, so $\frac{K}{L}$ falls and the MRTS falls. $\blacksquare$

Look back: a falling MRTS means that the more labour the firm already uses, the less capital one more hour of labour can replace. This is the same shape as the indifference curves in lesson 4, and it is the reason that the cost-minimizing input mix is a tangency.

### From a short-run production function to cost curves

Let capital be fixed at $\bar{K}$, so $Q = f(\bar{K}, L)$ is a function of $L$ alone, increasing over the range we use. Let the wage be $w$ and the cost of the fixed capital be $FC$ (the rent on $\bar{K}$).

*Theorem 3.* Suppose $Q = g(L)$ is differentiable and strictly increasing, so that it has an inverse $L = g^{-1}(Q)$. Then $VC(Q) = w\,g^{-1}(Q)$, $TC(Q) = FC + VC(Q)$ and

$$
MC = \frac{w}{MP_L}, \qquad AVC = \frac{w}{AP_L}.
$$

What we know: the firm's only variable cost is the wage bill $wL$, and to make $Q$ it needs $L = g^{-1}(Q)$ hours. What we want: $\frac{dVC}{dQ}$ and $\frac{VC}{Q}$. The plan is to use the derivative of an inverse function.

*Proof.* $VC = wL$ with $L = g^{-1}(Q)$, so $MC = \frac{dVC}{dQ} = w\frac{dL}{dQ}$. The derivative of the inverse is the reciprocal of the derivative, $\frac{dL}{dQ} = \frac{1}{dQ/dL} = \frac{1}{MP_L}$, so $MC = \frac{w}{MP_L}$. Also $AVC = \frac{wL}{Q} = \frac{w}{Q/L} = \frac{w}{AP_L}$. $\blacksquare$

Look back at what the formulas say. Marginal cost is lowest where marginal product is highest, and rises once marginal product falls: the law of diminishing returns is the reason MC is eventually upward-sloping. The average variable cost is lowest where $AP_L$ is highest, and at that point $MP_L = AP_L$, so $MC = AVC$: the marginal cost curve cuts the AVC curve at its minimum, as the average-versus-marginal theorem says. Where $MP_L$ reaches 0, the marginal cost is unbounded: that is capacity. The fixed cost only adds $AFC$, a curve that falls as $Q$ grows, to AVC, so $AC$ has its minimum to the right of the minimum of $AVC$.

### Short run against long run

In the long run the firm chooses both inputs. To make $Q$ at the least cost with input prices $r$ for capital and $w$ for labour, it picks the point of the isoquant where the MRTS equals the price ratio, $\frac{MP_L}{MP_K} = \frac{w}{r}$. (The derivation with a Lagrange multiplier is in [Lagrange multipliers, utility and cost minimization](05-lagrange-multipliers-utility-and-cost-minimization.md).) Any short-run plan with capital fixed at some $\bar{K}$ is also a possible long-run plan, so

$$
TC_{\text{short run}}(Q; \bar{K}) \ge TC_{\text{long run}}(Q)
$$

for every $Q$, with equality at the output for which $\bar{K}$ happens to be the cost-minimizing capital. Each short-run cost curve therefore lies on or above the long-run cost curve and touches it at one point (Example 4 and the second figure).

*Theorem 4.* Suppose $f(tK, tL) = t^\gamma f(K, L)$ for all $t > 0$, with $\gamma > 0$. If $C(Q)$ is the least cost of producing the output $Q$, then

$$
C(Q) = C(1)\,Q^{1/\gamma} \qquad\text{and}\qquad \frac{C(Q)}{Q} = C(1)\,Q^{\frac{1}{\gamma} - 1}.
$$

So long-run average cost falls with output if $\gamma > 1$, is constant if $\gamma = 1$ and rises if $\gamma < 1$.

What we know: $f$ scales by $t^\gamma$ when the inputs scale by $t$, and the cost of an input bundle scales by $t$ when the bundle scales by $t$. What we want: the cheapest bundle for $Q$ from the cheapest bundle for $1$. The plan is to scale the cheap bundle for output 1 up to output $Q$, then show that nothing cheaper exists by scaling any other bundle back down.

*Proof.* Let $x_1$ be a cheapest bundle for output 1, with cost $C(1)$, and let $t = Q^{1/\gamma}$. The bundle $tx_1$ gives output $t^\gamma\cdot 1 = Q$ at cost $t\,C(1)$. Now let $y$ be any bundle with output $Q$. Then $\frac{y}{t}$ has output $\frac{Q}{t^\gamma} = 1$, so its cost is at least $C(1)$, which means the cost of $y$ is at least $t\,C(1)$. So $C(Q) = t\,C(1) = C(1)Q^{1/\gamma}$. Dividing by $Q$ gives the average, and $Q^{\frac{1}{\gamma} - 1}$ is decreasing, constant or increasing as $\frac{1}{\gamma} - 1$ is negative, zero or positive, that is, as $\gamma$ is above, equal to or below 1. $\blacksquare$

Look back: for Cobb-Douglas, $\gamma = a + b$, so the sum of the exponents decides everything. With constant returns the long-run cost is a straight line through the origin, $C = C(1)\,Q$, and average cost equals marginal cost at every output. Increasing returns give "economies of scale" (falling long-run average cost) and decreasing returns give "diseconomies of scale".

## Worked examples

<div class="example" markdown>

### Example 1: the three stages of labour

A bakery's output with one oven is $Q(L) = 0.6L^2 - 0.02L^3$ loaves in a shift of $L$ labour hours (made up; it is the function behind the first figure). Find the marginal and average product, and describe the stages.

Step 1: differentiate, $MP_L = 1.2L - 0.06L^2$.

Step 2: divide, $AP_L = 0.6L - 0.02L^2$.

Step 3: compare, by the table:

| $L$ | $Q$ | $MP_L$ | $AP_L$ |
|---|---|---|---|
| 5 | 12.5 | 4.5 | 2.5 |
| 10 | 40 | 6 | 4 |
| 15 | 67.5 | 4.5 | 4.5 |
| 18 | 77.76 | 2.16 | 4.32 |
| 20 | 80 | 0 | 4 |

The marginal product rises until $MP_L' = 1.2 - 0.12L = 0$, that is until $L = 10$, where it peaks at 6. From there it falls, so the diminishing returns start after 10 hours. The average product peaks where it equals the marginal product, $1.2L - 0.06L^2 = 0.6L - 0.02L^2$, which gives $0.6L = 0.04L^2$ and $L = 15$, with $MP_L = AP_L = 4.5$. At $L = 20$ the marginal product is zero, and output is at its maximum of 80, the capacity of the oven.

Check: $AP_L' = 0.6 - 0.04L = 0$ at $L = 15$ agrees, and $AP_L$ falls after it ($4.32$ at 18, $4$ at 20) while $MP_L$ is below it, as the identity $AP_L' = \frac{MP_L - AP_L}{L}$ predicts.

</div>

<div class="example" markdown>

### Example 2: increasing returns with diminishing marginal products

A firm has $Q = 2K^{0.6}L^{0.6}$ (made up). Check the returns to scale and find the marginal products and the MRTS at $K = L = 10$.

By Theorem 1, $a + b = 1.2 > 1$: increasing returns. Doubling both inputs multiplies output by $2^{1.2} \approx 2.30$.

At $K = L = 10$ the output is $Q = 2 \cdot 10^{1.2} \approx 31.70$. Then $MP_K = 0.6\frac{Q}{K} \approx 1.902$ and $MP_L = 0.6\frac{Q}{L} \approx 1.902$, so the MRTS is $\frac{MP_L}{MP_K} = 1$, in agreement with $\frac{b}{a}\frac{K}{L} = 1$.

Each marginal product diminishes: $\frac{\partial^2 Q}{\partial K^2} = 0.6(-0.4)\frac{Q}{K^2} < 0$. So this firm has diminishing marginal returns to each input and increasing returns to scale at the same time.

Check: the real gain from one more unit of capital is $Q(11, 10) - Q(10, 10) \approx 1.866$, slightly under $MP_K = 1.902$, as diminishing returns predict. Doubling gives $Q(20, 20) = 2 \cdot 20^{1.2} \approx 72.82 = 2.2974 \cdot 31.70$.

</div>

<div class="example" markdown>

### Example 3: the cost curves from the bakery

Use the bakery function of Example 1, a wage of \$18 an hour and a fixed cost of \$300 a shift (the oven; made up). Find the cost curves at several points.

By Theorem 3, $MC = \frac{18}{MP_L}$ and $AVC = \frac{18}{AP_L}$. The fixed cost gives $AFC = \frac{300}{Q}$, and $AC = AVC + AFC$.

| $L$ | $Q$ | $MC$ | $AVC$ | $AFC$ | $AC$ |
|---|---|---|---|---|---|
| 5 | 12.5 | 4.00 | 7.20 | 24.00 | 31.20 |
| 10 | 40 | 3.00 | 4.50 | 7.50 | 12.00 |
| 15 | 67.5 | 4.00 | 4.00 | 4.44 | 8.44 |
| 18 | 77.76 | 8.33 | 4.17 | 3.86 | 8.02 |

The first figure draws the whole picture. The marginal cost is lowest at $Q = 40$ (where $MP_L$ peaks), at \$3. The average variable cost is lowest at $Q = 67.5$, at \$4, which is where the marginal cost passes through it. The average cost is lowest further right, at $Q \approx 77.6$ and about \$8.02, because the falling $AFC$ keeps pulling it down after AVC has started to rise. Past 80 loaves the oven can't make more at any price.

![Two panels. On the left, the marginal product of labour (red) rises to 6 at L equal to 10, then falls to 0 at L equal to 20; the average product (blue) peaks at 4.5 at L equal to 15, where the red curve crosses it. On the right, cost curves against output: marginal cost in red is lowest at 3 when Q is 40 and rises steeply towards capacity at Q equal to 80, average variable cost in blue is lowest at 4 when Q is 67.5 where the red curve crosses it, average fixed cost in grey falls throughout, and average cost in green is lowest at about 8.02 at Q equal to 77.6.](../../assets/figures/07-economics-math/production-and-cost-functions-cost-curves.svg)

Check: the point $L = 15$ gives $MC = AVC = 4$ exactly, because $MP_L = AP_L = 4.5$ there. And $AC = 8.44$ at $Q = 67.5$ is the sum $4 + 4.44$. A direct search over $L$ puts the minimum of $AC$ at $L \approx 17.91$, $Q \approx 77.57$, where $MC \approx AC \approx 8.02$.

</div>

<div class="example" markdown>

### Example 4: a worked cost function, short run and long run

A firm makes $Q = \sqrt{KL}$ with capital at \$2 a unit and labour at \$8 an hour (made up). Find its long-run cost function, then its short-run cost with $\bar{K} = 20$.

Long run. The MRTS is $\frac{b}{a}\frac{K}{L} = \frac{K}{L}$, and cost minimization needs $\frac{K}{L} = \frac{w}{r} = 4$, so $K = 4L$. Then $Q = \sqrt{4L^2} = 2L$, so $L = \frac{Q}{2}$ and $K = 2Q$. The cost is $2 \cdot 2Q + 8 \cdot \frac{Q}{2} = 4Q + 4Q = 8Q$. This is constant returns ($a + b = 1$), so by Theorem 4 the long-run cost is a straight line with $MC = AC = 8$.

Short run with $\bar{K} = 20$. Output is $Q = \sqrt{20L}$, so $L = \frac{Q^2}{20}$. The fixed cost is $2 \cdot 20 = 40$ and $VC = 8 \cdot \frac{Q^2}{20} = 0.4Q^2$, so

$$
TC = 40 + 0.4Q^2, \qquad MC = 0.8Q, \qquad AC = \frac{40}{Q} + 0.4Q.
$$

Average cost is smallest where $MC = AC$: $0.8Q = \frac{40}{Q} + 0.4Q$ gives $Q^2 = 100$ and $Q = 10$, where $AC = 4 + 4 = 8$. The short-run curve touches the long-run line at $Q = 10$, because the capital 20 is the cost-minimizing capital for that output ($K = 2Q = 20$).

![Total cost against output. The long-run cost line C equals 8Q in green, and three short-run cost curves for capital fixed at 5, 20 and 45 units. Each short-run curve is a parabola above the green line that touches it at one point: Q equal to 2.5, 10 and 22.5 respectively.](../../assets/figures/07-economics-math/production-and-cost-functions-short-and-long-run.svg)

Check: at $Q = 10$ the short-run cost is $40 + 40 = 80$ and the long-run cost is $8 \cdot 10 = 80$. At other outputs the short run is dearer: $Q = 5$ costs $50$ against $40$, and $Q = 20$ costs $200$ against $160$. The same happens for $\bar{K} = 5$ (touching at $Q = 2.5$, $TC = 20$) and $\bar{K} = 45$ (touching at $Q = 22.5$, $TC = 180$).

</div>

<div class="example" markdown>

### Example 5: costs from a square-root production function (finish it yourself)

With capital fixed, a firm has $Q = 4\sqrt{L}$. The wage is \$12 an hour and the fixed cost is \$100 (made up). Use Theorem 3 to find $VC$, $MC$ and $AC$ as functions of $Q$, then find the output that minimizes average cost.

<details class="solution" markdown>
<summary>Finish</summary>

From $Q = 4\sqrt{L}$ we get $L = \frac{Q^2}{16}$, so $VC = 12 \cdot \frac{Q^2}{16} = 0.75Q^2$ and $TC = 100 + 0.75Q^2$. Then $MC = 1.5Q$ and $AC = \frac{100}{Q} + 0.75Q$.

Setting $MC = AC$: $1.5Q = \frac{100}{Q} + 0.75Q$ gives $0.75Q^2 = 100$, so $Q^2 = \frac{400}{3}$ and $Q \approx 11.55$, where $AC = 10\sqrt{3} \approx 17.32$ and $MC = 1.5Q = 17.32$.

Check by the formula of Theorem 3: $MP_L = \frac{2}{\sqrt{L}}$ and $\sqrt{L} = \frac{Q}{4}$, so $MP_L = \frac{8}{Q}$ and $\frac{w}{MP_L} = \frac{12Q}{8} = 1.5Q$, in agreement.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: mixing up diminishing marginal returns with decreasing returns to scale. The first changes one input and holds the others fixed (a second derivative in $L$). The second changes all inputs by the same factor (the sum $a + b$). Example 2 has the first and the opposite of the second.

</div>

<div class="warning" markdown>

Watch out: reading the marginal product as the average. The output of the last worker is $MP_L$, and the output per worker is $AP_L = \frac{Q}{L}$. They are equal only where the average product peaks. In Example 1 the tenth hour adds 6 loaves while each hour averages 4.

</div>

<div class="warning" markdown>

Watch out: putting fixed cost into marginal cost, or treating "fixed" as "cannot be avoided in the long run". A cost is fixed with respect to output in the short run. In the long run the firm can exit and avoid it. In the example of the oven, the \$300 is fixed only while the firm owns the oven.

</div>

<div class="warning" markdown>

Watch out: inverting the MRTS. The slope of the isoquant for labour on the horizontal axis is $\frac{MP_L}{MP_K}$, labour over capital. Writing $\frac{MP_K}{MP_L}$ gives the MRTS of capital for labour, the reciprocal, with the axes swapped. State which axis is which before computing.

</div>

<div class="warning" markdown>

Watch out: assuming that every production function has $a + b = 1$. Many textbooks use $K^{0.3}L^{0.7}$ because it is easy, but estimated functions often have a sum above or below 1, and then the long-run cost is not a straight line (Theorem 4).

</div>

Two edge cases are worth knowing. At $L = 0$ the average product $\frac{Q}{L}$ is not defined, and the cost curves are drawn for $Q > 0$ only. And the cost curve ends at capacity: when $MP_L = 0$ there is no way to make more output with this plant, so $MC$ is not finite. Real cost curves are often drawn up to capacity.

## Tricks and shortcuts

For Cobb-Douglas, skip the power rule: $MP_K = a\frac{Q}{K}$ and $MP_L = b\frac{Q}{L}$, so the MRTS is $\frac{b}{a}\frac{K}{L}$ immediately. If capital and labour are in the ratio $\frac{K}{L}$, the cost-minimizing ratio is $\frac{K}{L} = \frac{a}{b}\cdot\frac{w}{r}$.

To read returns to scale from a formula, add up the exponents of all the inputs. It works for any function that is a product of powers, and for a sum of such terms of the same degree.

To get a cost curve quickly from $Q = g(L)$, invert it to $L(Q)$ and multiply by the wage. Then $MC$ and $AVC$ come by differentiating and dividing, and the reciprocals $\frac{w}{MP}$ and $\frac{w}{AP}$ give a check.

The short-run cost at any output is at least the long-run cost. If you compute a short-run figure that is below the long-run one, one of them has a mistake.

## In code

Sympy checks the scaling law, the MRTS and the cost curves of the bakery. The last block finds the minimum of average cost.

<details class="code" markdown>
<summary>In code</summary>

```python
import sympy as sp

K, L, A, a, b, s = sp.symbols("K L A a b s", positive=True)
f = A * K**a * L**b

print(sp.simplify(f.subs({K: s * K, L: s * L}, simultaneous=True) / f))
# s**(a + b)
print(sp.simplify(sp.diff(f, L) / sp.diff(f, K)))
# K*b/(L*a)

# The bakery: Q(L), marginal and average product, wage 18, fixed cost 300
Q = sp.Rational(3, 5) * L**2 - sp.Rational(1, 50) * L**3
MP = sp.diff(Q, L)
AP = sp.simplify(Q / L)
print(sp.solve(sp.diff(MP, L), L), sp.solve(sp.diff(AP, L), L))
# [10] [15]
print(18 / MP.subs(L, 15), 18 / AP.subs(L, 15))
# 4 4

mc = 18 / MP
ac = (300 + 18 * L) / Q
L_star = sp.nsolve(sp.Eq(mc, ac), L, 16.5)
print(round(float(L_star), 2), round(float(Q.subs(L, L_star)), 2), round(float(ac.subs(L, L_star)), 3))
# 17.91 77.57 8.024
```

The first two lines are Theorem 1 and the MRTS formula. The peaks of $MP_L$ and $AP_L$ are at 10 and 15, and at 15 both $MC$ and $AVC$ equal 4. The last line is the minimum of average cost, in labour, output and dollars per unit.

</details>

## FAQ

### Why does marginal cost eventually rise?

Because of diminishing marginal returns. With the plant fixed, each added worker has less to work with, so the marginal product falls, and each extra loaf needs more worker-hours. By Theorem 3, $MC = \frac{w}{MP_L}$ rises when $MP_L$ falls. In the long run, when all inputs can grow, the firm can build a second oven, and the rise can go away: with constant returns to scale the long-run $MC$ is flat.

### Is Cobb-Douglas realistic?

It is a convenient model more than a law. It has diminishing returns, convex isoquants and a one-line formula for everything, and it fits aggregate data tolerably well, with $a$ near the capital share of income. But it forces the MRTS to depend only on the ratio $\frac{K}{L}$ and the substitution between inputs to be fixed, which real technologies don't have. [Regression and econometrics intuition](../04-more-tools/03-regression-and-econometrics-intuition.md) shows how the exponents are estimated by taking logs.

### Why must a short-run cost curve lie above the long-run one?

In the short run the firm is stuck with the capital it has, and in the long run it is free to choose anything, including that same capital. A firm that can choose can't do worse than a firm that can't. The two are equal only where the fixed capital happens to be the best choice, as at $Q = 10$ for $\bar{K} = 20$ in Example 4.

### Can returns to scale be decreasing while marginal products are constant?

Yes. $Q = K + L$ has constant marginal products and constant returns to scale, but $Q = \sqrt{K + L}$ has decreasing marginal products and decreasing returns. The two properties are independent; Example 2 shows one more combination.

## Practice

### Warm-up

1\. With capital fixed, $Q = 20\sqrt{L}$. At $L = 25$, find $MP_L$ and $AP_L$. Is the average product rising or falling?

<details class="solution" markdown>
<summary>Solution</summary>

$Q(25) = 100$. $MP_L = \frac{10}{\sqrt{L}} = 2$ and $AP_L = \frac{100}{25} = 4$. Since $MP_L < AP_L$, the average product is falling.

Check: $AP_L = \frac{20}{\sqrt{L}}$ is decreasing for all $L$, and $MP_L$ is always half of $AP_L$.

</details>

2\. A firm has $TC(Q) = 200 + 6Q + 0.5Q^2$. At $Q = 10$ find $FC$, $VC$, $AFC$, $AVC$, $AC$ and $MC$.

<details class="solution" markdown>
<summary>Solution</summary>

$FC = 200$. $VC = 60 + 50 = 110$. $AFC = \frac{200}{10} = 20$, $AVC = \frac{110}{10} = 11$, $AC = 20 + 11 = 31$. $MC = 6 + Q = 16$.

Check: $TC(10) = 310$, and $\frac{310}{10} = 31$. Since $MC = 16 < AC = 31$, the average cost is falling at $Q = 10$.

</details>

3\. Classify the returns to scale of (a) $Q = 3K^{0.3}L^{0.5}$ and (b) $Q = K^{0.7}L^{0.7}$. By what factor does output change when both inputs double?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $a + b = 0.8 < 1$: decreasing returns to scale. Doubling multiplies output by $2^{0.8} \approx 1.74$.

(b) $a + b = 1.4 > 1$: increasing returns. Doubling multiplies output by $2^{1.4} \approx 2.64$.

Check: the factor is below 2 in (a) and above 2 in (b), as it should be.

</details>

### Standard

4\. For $Q = K^{0.4}L^{0.6}$, find the MRTS as a function of $K$ and $L$. (a) Find it at $K = 20$, $L = 30$. (b) If $w = r = 10$, is this input mix cost-minimizing? (c) At $K = 30$, $L = 20$, which input should the firm use more of?

<details class="solution" markdown>
<summary>Solution</summary>

$MRTS = \frac{b}{a}\frac{K}{L} = 1.5\frac{K}{L}$.

(a) At $K = 20$, $L = 30$: $1.5 \cdot \frac{20}{30} = 1$.

(b) The price ratio is $\frac{w}{r} = 1$, so the MRTS equals it: this is the cost-minimizing mix for the output $Q = 20^{0.4}30^{0.6}$.

(c) At $K = 30$, $L = 20$ the MRTS is $1.5 \cdot 1.5 = 2.25 > 1$. The extra output per dollar is higher for labour, $\frac{MP_L}{w} > \frac{MP_K}{r}$, so the firm should hire more labour and use less capital.

Check: moving along the isoquant from $(30, 20)$ towards more labour lowers the MRTS, and it reaches 1 where $\frac{K}{L} = \frac{2}{3}$, the same ratio as the mix in (a).

</details>

5\. With capital fixed, $Q = 6\sqrt{L}$, the wage is \$9 and $FC = 90$. Find $VC$, $MC$ and $AC$ as functions of $Q$, and the output and the value at which $AC$ is smallest.

<details class="solution" markdown>
<summary>Solution</summary>

$L = \frac{Q^2}{36}$, so $VC = \frac{9Q^2}{36} = \frac{Q^2}{4}$, $MC = \frac{Q}{2}$ and $AC = \frac{90}{Q} + \frac{Q}{4}$. Setting $MC = AC$: $\frac{Q}{4} = \frac{90}{Q}$, so $Q^2 = 360$ and $Q = 6\sqrt{10} \approx 18.97$. There $AC = \frac{Q}{2} \approx 9.49$.

Check: $MP_L = \frac{3}{\sqrt{L}} = \frac{18}{Q}$, so $\frac{w}{MP_L} = \frac{9Q}{18} = \frac{Q}{2}$, matching $MC$.

</details>

6\. For $Q = \sqrt{KL}$ with $r = 2$ and $w = 8$ as in Example 4, take $\bar{K} = 5$. Find the short-run cost function, and show that it touches the long-run cost $8Q$ at $Q = 2.5$. Compare the two at $Q = 10$.

<details class="solution" markdown>
<summary>Solution</summary>

$L = \frac{Q^2}{5}$, so $TC = 2 \cdot 5 + 8 \cdot \frac{Q^2}{5} = 10 + 1.6Q^2$. At $Q = 2.5$: $10 + 1.6 \cdot 6.25 = 20 = 8 \cdot 2.5$. At $Q = 10$: $10 + 160 = 170$ against $80$.

Check: the long-run capital for $Q = 2.5$ is $K = 2Q = 5$, which is $\bar{K}$, so the touching point is where it should be. Also $TC_{SR} - 8Q = 1.6Q^2 - 8Q + 10 = 1.6(Q - 2.5)^2 \ge 0$.

</details>

### Challenge

7\. (a) Prove that if $f(tK, tL) = t^\gamma f(K, L)$ then long-run average cost is $C(1)Q^{\frac{1}{\gamma} - 1}$. (b) For $\gamma = 0.5$ and $C(1) = 5$, find $C(4)$, $AC(4)$ and $MC(4)$ and say what kind of scale effects these costs show.

<details class="solution" markdown>
<summary>Solution</summary>

(a) This is Theorem 4: scale the cheapest bundle for $Q = 1$ by $t = Q^{1/\gamma}$ to get output $Q$ at cost $t\,C(1)$, and no bundle is cheaper, since scaling any bundle $y$ with output $Q$ by $\frac{1}{t}$ gives output 1. Then $\frac{C(Q)}{Q} = C(1)Q^{\frac{1}{\gamma} - 1}$.

(b) With $\gamma = 0.5$, $\frac{1}{\gamma} = 2$, so $C(Q) = 5Q^2$. Then $C(4) = 80$, $AC(4) = 20$ and $MC(Q) = 10Q$ gives $MC(4) = 40$. Average cost $5Q$ rises with output and marginal cost is twice the average: decreasing returns to scale, so diseconomies of scale.

Check: $MC = \frac{dC}{dQ} = \frac{1}{\gamma}\cdot\frac{C}{Q}$ in general, which is $2 \cdot 20 = 40$ here.

</details>

8\. (Reviews [partial derivatives and the gradient](../../05-university-core/09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md).) For $Q = 2K^{0.6}L^{0.6}$ at $K = L = 10$: (a) find $MP_K$ using $a\frac{Q}{K}$. (b) Check it with a small step $\Delta K = 0.01$. (c) Use the gradient to estimate the output change if capital rises by 0.5 and labour falls by 0.5.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $Q = 2 \cdot 10^{1.2} \approx 31.698$, so $MP_K = 0.6 \cdot \frac{31.698}{10} \approx 1.902$.

(b) $Q(10.01, 10) - Q(10, 10) \approx 0.01901$, so the rate is about $1.901$, matching.

(c) $\Delta Q \approx MP_K\,\Delta K + MP_L\,\Delta L = 1.902(0.5) + 1.902(-0.5) = 0$. The output is unchanged to first order, because the MRTS is 1 and the move is along the isoquant.

Check: exactly, $Q(10.5, 9.5) = 2(10.5 \cdot 9.5)^{0.6} \approx 31.650$ against $31.698$, a very small drop of 0.05 (second-order, from the convexity of the isoquant).

</details>

## Where this shows up

- The next lesson, [profit maximization and market structure](03-profit-maximization-and-market-structure.md), takes the cost curves of this lesson and finds the output where marginal revenue meets marginal cost, the shutdown price at the minimum of AVC and the long-run price at the minimum of average cost. [Lagrange multipliers, utility and cost minimization](05-lagrange-multipliers-utility-and-cost-minimization.md) derives the long-run cost-minimizing inputs with a multiplier.
- Economics: growth models use Cobb-Douglas functions for the whole economy, and the exponent $a$ is read as the capital share of income. Economies of scale (Theorem 4) are the main reason for large firms, and diseconomies of scale explain why firms stop growing.
- CS: adding servers or engineers to a fixed system has diminishing marginal returns, and speedups of parallel programs have the same shape as the marginal product curve (Amdahl's law is a diminishing-returns result). Cloud costs have a fixed part and a per-unit part in the same way.
