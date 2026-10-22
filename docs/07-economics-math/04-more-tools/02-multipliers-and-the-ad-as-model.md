# Multipliers and the AD-AS model

After this lesson you can find equilibrium output in the Keynesian cross, derive the spending multiplier $\frac{1}{1 - b}$ by algebra and by a geometric series, compute tax and balanced-budget multipliers, show how taxes and imports shrink the multiplier, and read the AD-AS diagram for a demand shock.

Before this: [infinite series basics](../../05-university-core/05-sequences-and-series/02-infinite-series-basics.md) (the geometric series), [systems of linear equations](../../03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md), and [GDP and the circular flow](../01-measuring-the-economy/05-gdp-and-the-circular-flow.md) (spending and income). The previous lesson, [present value, NPV and bond prices](01-present-value-npv-and-bond-prices.md), uses the same series.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. People spend 75 cents of each extra dollar of income. By how much does output eventually rise if the government spends an extra \$50 million?
2. In an economy, $C = 100 + 0.9Y$, $I = 50$ and $G = 50$ (all in billions of dollars), and output equals spending: $Y = C + I + G$. Find $Y$.
3. In question 1's economy (spending 75 cents of each extra dollar of income), a lump-sum tax rises by \$40 million. How much does output change?

<details class="solution" markdown>
<summary>Answers</summary>

1. The multiplier is $\frac{1}{1 - 0.75} = 4$, so output rises by $4 \times 50 = 200$ million dollars.
2. $Y = 100 + 0.9Y + 50 + 50$, so $0.1Y = 200$ and $Y = 2000$ billion dollars.
3. The tax multiplier is $-\frac{b}{1 - b} = -\frac{0.75}{0.25} = -3$, so output falls by $3 \times 40 = 120$ million dollars.

</details>

## The idea

Suppose a province spends \$100 million on a new transit line. The money goes to construction firms as income. They pay workers and suppliers, and those people spend part of what they receive, say 80 cents of each dollar, at restaurants, shops and landlords. The owners of those businesses receive \$80 million in income, and they spend 80% of that, \$64 million. Each round of spending creates income, and part of the income is spent again. The rounds are \$100 million, \$80 million, \$64 million, \$51.2 million, and so on.

The total is a geometric series: $100 + 80 + 64 + \cdots = \frac{100}{1 - 0.8} = 500$ million dollars. A \$100 million injection has raised total spending, and so output, by \$500 million. The ratio 5 is the spending multiplier.

This is the logic of the Keynesian cross, the simplest model of how total spending determines output when there is spare capacity. It was built to explain the Great Depression: if factories and workers sit idle, then a fall in spending makes output fall, and a rise in spending can bring it back. It says nothing about prices, and the second half of the lesson adds them with the AD-AS model. The multiplier is an upper bound in most real economies, for reasons listed at the end.

![Planned spending against income. The 45-degree line shows spending equal to income. The green line, 1000 plus 0.8 Y, crosses it at point A where income is 5000. After government spending rises by 100, the orange line, 1100 plus 0.8 Y, crosses it at point B where income is 5500, an arrow marking the rise of 500.](../../assets/figures/07-economics-math/multipliers-and-the-ad-as-model-cross.svg)

## Definitions

In the simplest model, an economy has no foreign trade. **Output** $Y$ is total production, which equals total income, as in the circular flow. **Planned spending** (aggregate expenditure) is the sum of four parts: consumption $C$, investment $I$, government purchases $G$, and net exports $NX$. This lesson first sets $NX = 0$.

The **consumption function** is the rule $C = a + bY$, where $a \ge 0$ is **autonomous consumption** (what households spend even at zero income) and $b$ is the **marginal propensity to consume** (MPC). In plain words, $b$ is the number of extra dollars spent when income rises by one dollar. We assume $0 \le b < 1$. The **marginal propensity to save** is $1 - b$, the part of an extra dollar not spent.

Investment $I$ and government purchases $G$ are treated as given numbers, so they are **autonomous spending** too. The **Keynesian cross** equilibrium is the output $Y$ at which planned spending equals output:

$$
Y = C + I + G = a + bY + I + G.
$$

The **spending multiplier** is the ratio $\frac{\Delta Y}{\Delta G}$ of the change in equilibrium output to the change in autonomous spending that caused it. In plain words, it says how many dollars of output each extra dollar of spending creates in the end. The same factor applies to a change in $I$ or in $a$.

A **lump-sum tax** $T$ is a tax of a fixed amount, and **disposable income** is $Y - T$. With taxes, consumption is $C = a + b(Y - T)$. A **proportional tax** takes the fraction $\tau$ of income (the Greek letter tau), so disposable income is $(1 - \tau)Y$. **Imports** are modelled as $M = mY$, where $m$ is the **marginal propensity to import**. A **leakage** is any use of an extra dollar of income that does not become spending on domestic output: saving, taxes and imports.

The **AD curve** (aggregate demand) shows the output demanded at each price level $P$. The **short-run AS curve** (aggregate supply) shows the output firms supply at each price level when some prices and wages are slow to change, and it slopes up. The **long-run AS curve** is vertical at **potential output**, the level the economy produces when all resources are normally employed. A **demand shock** moves the AD curve and a **supply shock** moves the AS curve.

## How to do it

### Finding equilibrium output

1. Write the consumption function, including any taxes: $C = a + b(Y - T)$.
2. Write the equilibrium condition $Y = C + I + G$ and substitute $C$.
3. Collect the terms in $Y$ on the left. For the basic model this gives $(1 - b)Y = a + I + G$.
4. Divide by $1 - b$ to solve for $Y$.
5. Find consumption, and check that $C + I + G$ equals $Y$.

### The spending multiplier, two ways

*Theorem 1.* In the Keynesian cross with $C = a + bY$ and $0 \le b < 1$, equilibrium output is

$$
Y^* = \frac{a + I + G}{1 - b},
$$

and a change $\Delta G$ in government purchases changes it by $\Delta Y = \frac{1}{1 - b}\,\Delta G$. Equivalently, the rounds of spending $\Delta G,\ b\,\Delta G,\ b^2\,\Delta G, \dots$ add up to $\frac{\Delta G}{1 - b}$.

We know the equilibrium condition $Y = a + bY + I + G$ and the infinite geometric series. We want a formula for $Y^*$ and the effect of $\Delta G$. The plan is to solve the equation once, and then, as a second method, add up the rounds of spending as a series and see that the two answers agree.

*Proof (algebra).* Subtract $bY$ from both sides of the equilibrium condition to get $(1 - b)Y = a + I + G$. Since $b < 1$, we can divide by $1 - b$, which gives $Y^*$. If $G$ rises by $\Delta G$, the new equilibrium is $\frac{a + I + G + \Delta G}{1 - b}$, and subtracting the old one leaves $\frac{\Delta G}{1 - b}$.

*Proof (rounds of spending).* The first round is the extra purchases themselves, $\Delta G$, which are income to someone. Households spend the fraction $b$ of that income, so round 2 is $b\,\Delta G$, which is again income to someone, who spends $b$ times it. Round $k + 1$ is $b^k\,\Delta G$. The total over all rounds is

$$
\Delta G\,(1 + b + b^2 + \cdots) = \frac{\Delta G}{1 - b},
$$

by the geometric series, which converges because $\lvert b \rvert < 1$. $\blacksquare$

Look back: the two proofs say the same thing in two ways. The algebra looks only at the end state, where the extra income $\Delta Y$ is the original injection plus the extra consumption it triggers, $\Delta Y = \Delta G + b\,\Delta Y$. The series follows the money round by round, and the algebra is what you get by adding all the rounds at once. The condition $b < 1$ is needed in both: if $b = 1$ the algebra divides by zero and the series $1 + 1 + 1 + \cdots$ diverges, since every extra dollar would be spent again and the process never settles. The multiplier $\frac{1}{1 - b}$ is the reciprocal of the marginal propensity to save.

### Taxes: the tax and balanced-budget multipliers

*Theorem 2.* Let consumption be $C = a + b(Y - T)$ with a lump-sum tax $T$. Then equilibrium output is

$$
Y^* = \frac{a - bT + I + G}{1 - b}.
$$

A rise $\Delta T$ in taxes changes output by $-\frac{b}{1 - b}\,\Delta T$ (the tax multiplier is $-\frac{b}{1 - b}$). If the government raises $G$ and $T$ by the same amount, $\Delta G = \Delta T$, output changes by exactly that amount: the balanced-budget multiplier is 1.

We know the multiplier from Theorem 1. We want the effect of a tax. The plan is to solve the new equilibrium equation in the same way, then add the two effects.

*Proof.* The condition $Y = a + b(Y - T) + I + G$ gives $(1 - b)Y = a - bT + I + G$, so $Y^*$ is as stated. A change $\Delta T$ changes the numerator by $-b\,\Delta T$, so $\Delta Y = \frac{-b}{1 - b}\,\Delta T$. For the combination, add the two effects: $\Delta Y = \frac{1}{1 - b}\Delta G - \frac{b}{1 - b}\Delta T$. With $\Delta G = \Delta T$ this is $\frac{1 - b}{1 - b}\,\Delta G = \Delta G$. $\blacksquare$

Look back: a tax cut has a smaller effect than the same amount of government spending, by the factor $b$. The reason is that the first round of a tax cut is not spent in full: households save the fraction $1 - b$ of the tax cut, and only $b\,\Delta T$ enters the spending rounds. Government spending counts for the whole $\Delta G$ in round 1. In the balanced-budget case, the whole amount is spent in round 1 by the government, and only $b$ of it is taken back out of spending through taxes, with the later rounds netting out to exactly one.

### Leakages shrink the multiplier

*Theorem 3.* Suppose consumption is $C = a + b(1 - \tau)Y$ with a proportional tax rate $\tau$, imports are $M = mY$, and net exports are $NX = X - mY$ for fixed exports $X$. Then equilibrium output is

$$
Y^* = \frac{a + I + G + X}{1 - b(1 - \tau) + m},
$$

and the spending multiplier is $\frac{1}{1 - b(1 - \tau) + m}$.

We know how to solve the equilibrium condition. We want the multiplier when taxes and imports take a share of each extra dollar. The plan is to write the condition with all four spending parts, collect the $Y$ terms, and divide.

*Proof.* The condition $Y = C + I + G + NX$ becomes $Y = a + b(1 - \tau)Y + I + G + X - mY$. Moving every term with $Y$ to the left gives $\bigl(1 - b(1 - \tau) + m\bigr)Y = a + I + G + X$. The coefficient is positive, because $b(1 - \tau) < 1$ and $m \ge 0$, so we can divide. A change in $G$ changes the numerator by $\Delta G$, and the multiplier follows. $\blacksquare$

Look back: the quantity $b(1 - \tau) - m$ is the fraction of each extra dollar of income that is spent on domestically produced goods, which is the ratio of the geometric series of rounds. With no taxes or imports it is $b$. Each leakage lowers the ratio, so the series adds up to less. The model is consistent with the rounds picture: the rounds are $\Delta G,\ q\,\Delta G,\ q^2\,\Delta G, \dots$ with $q = b(1 - \tau) - m$, and the total is $\frac{\Delta G}{1 - q}$.

### The AD-AS picture

The Keynesian cross holds the price level fixed. The AD-AS model lets prices move. The AD curve slopes down: at a higher price level, households' wealth buys less, interest rates tend to rise, and exports become more expensive, so less output is demanded. The multiplier tells you how far the AD curve moves to the right when autonomous spending rises: at each price level, the amount demanded rises by $\frac{1}{1 - b}\,\Delta G$ (or the leaky version).

The short-run AS curve slopes up because some prices and wages are slow to adjust, so firms produce more when prices rise. The long-run AS curve is vertical at potential output $Y_p$, because in the long run all prices and wages adjust, and the economy can't produce more than its resources allow, whatever the price level.

![A downward-sloping AD curve crossing an upward-sloping short-run AS curve and a vertical long-run AS line at 5000, with a second dashed AD curve to the right. Point A, the start, is at output 5000 and price level 100. Point B, the short-run result, is where the dashed AD crosses short-run AS, at output about 5357 and price level 107. Point C, the long-run result, is where the dashed AD crosses the vertical line, at output 5000 and price level 125.](../../assets/figures/07-economics-math/multipliers-and-the-ad-as-model-adas.svg)

A demand shock then plays out in two stages, as in the figure. Take a toy economy (made-up numbers) with AD: $Y = 7000 - 20P$, short-run AS: $P = 0.02Y$, and potential output $Y_p = 5000$. Solving the two lines gives point A, $Y = 5000$ and $P = 100$, with output at potential. Now $G$ rises by 100 with $b = 0.8$, so the AD curve moves right by $5 \times 100 = 500$ and becomes $Y = 7500 - 20P$. In the short run the economy moves along the AS curve to point B, where $Y = \frac{7500}{1.4} \approx 5357$ and $P \approx 107$. Output rises by 357, not by the multiplier's 500, because the price level rose and pulled the economy back up along the AD curve. In the long run, wages and prices rise until output is back at 5000, which is point C, with $P = \frac{7500 - 5000}{20} = 125$. If the economy begins below potential, with spare capacity, the same push raises output by more and prices by less, which is the case the Keynesian cross describes.

## Worked examples

<div class="example" markdown>

### Example 1: equilibrium and a rise in government spending

An economy (made-up numbers, in billions of dollars) has $C = 200 + 0.8Y$, $I = 300$ and $G = 500$. Find equilibrium output and consumption. Then find the effect of raising $G$ by 100.

Step 1: the consumption function is $C = 200 + 0.8Y$, with no taxes.

Step 2: the equilibrium condition is $Y = 200 + 0.8Y + 300 + 500$.

Step 3: collecting terms, $0.2Y = 1000$.

Step 4: $Y = \frac{1000}{0.2} = 5000$.

Step 5: consumption is $C = 200 + 0.8 \times 5000 = 4200$. Check: $C + I + G = 4200 + 300 + 500 = 5000 = Y$.

For the rise in $G$, the multiplier is $\frac{1}{1 - 0.8} = 5$, so output rises by $5 \times 100 = 500$ to $Y = 5500$. Check by solving again: $Y = \frac{200 + 300 + 600}{0.2} = 5500$. The rounds of spending are 100, 80, 64, 51.2, 40.96, and so on; the first five add to 336.16, and 200 rounds add to 500.00.

The same \$100 billion rise in $I$ would give the same result. In the figure above, this is the shift from the green line to the orange one and the move from point A to point B.

</div>

<div class="example" markdown>

### Example 2: tax multiplier and the balanced budget

The same economy now has a lump-sum tax $T = 100$ and consumption $C = 200 + 0.8(Y - T)$, with $I = 300$ and $G = 500$. Find $Y$. Then find the effect of (a) a tax rise of 100, and (b) raising both $G$ and $T$ by 100.

By Theorem 2, $Y = \frac{200 - 0.8 \times 100 + 300 + 500}{0.2} = \frac{920}{0.2} = 4600$. Consumption is $200 + 0.8 \times 4500 = 3800$, and $3800 + 300 + 500 = 4600$ confirms it.

(a) The tax multiplier is $-\frac{0.8}{0.2} = -4$, so a tax rise of 100 lowers output by 400, to 4200. Check: $\frac{200 - 0.8 \times 200 + 800}{0.2} = \frac{840}{0.2} = 4200$.

(b) Raising $G$ by 100 adds $5 \times 100 = 500$, and raising $T$ by 100 subtracts 400, so output rises by 100, to 4700. The change equals the change in $G$, the balanced-budget multiplier of 1. Check: $\frac{200 - 0.8 \times 200 + 300 + 600}{0.2} = \frac{940}{0.2} = 4700$.

The tax cut is the weaker tool: \$100 billion of tax cuts raises output by 400, while \$100 billion of spending raises it by 500, a ratio of $b = 0.8$.

</div>

<div class="example" markdown>

### Example 3: how leakages cut the multiplier

Take $b = 0.8$, as before, but now add an income tax of $\tau = 25\%$ and imports with $m = 0.1$. What is the multiplier, and how much does a \$100 billion rise in $G$ raise output?

The share of an extra dollar of income that is spent on domestic goods is $b(1 - \tau) - m = 0.8 \times 0.75 - 0.1 = 0.5$. By Theorem 3, the multiplier is $\frac{1}{1 - 0.6 + 0.1} = \frac{1}{0.5} = 2$, so a \$100 billion rise in $G$ raises output by only \$200 billion, against \$500 billion with no leakages.

In rounds: the first round is 100, the second is 50, the third 25, and so on, a series with ratio 0.5 that adds to $\frac{100}{1 - 0.5} = 200$.

Check: follow one extra dollar of income. Tax takes 25 cents. Of the remaining 75 cents, households spend 80%, which is 60 cents, and save 15 cents. Imports are 10 cents per dollar of income, so 10 of the 60 cents spent goes abroad and 50 cents is spent on domestic goods. The leakages are $25 + 15 + 10 = 50$ cents, and the 50 cents that stay in the circle match the ratio 0.5.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

In the Example 1 economy the central bank's economists estimate that output is 400 below potential. With $b = 0.8$, $\tau = 0.25$ and $m = 0.1$, how large a rise in government purchases closes the gap, and how large would you have estimated it with the simple multiplier?

The leaky multiplier is 2 (Example 3). Set $\text{multiplier} \times \Delta G = 400$ and solve for $\Delta G$. Then repeat with the simple multiplier $\frac{1}{1 - b}$.

<details class="solution" markdown>
<summary>Finish</summary>

With the leaky multiplier, $2\,\Delta G = 400$, so $\Delta G = 200$. With the simple multiplier, $5\,\Delta G = 400$, so $\Delta G = 80$.

Using the simple multiplier would have understated the needed spending by $200 - 80 = 120$, and the economy would have been left short of potential.

Check: spending 80 with the leaky multiplier raises output by only $2 \times 80 = 160$, which is 40% of the gap. Spending 200 raises it by $2 \times 200 = 400$, the whole gap.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the multiplier is not a promise. It needs $b < 1$, spare capacity, and fixed prices and interest rates. If the economy is already at potential output, extra spending raises prices, as the move from point B to point C shows, and the long-run multiplier is close to zero.

</div>

<div class="warning" markdown>

Watch out for confusing $Y$ with disposable income. In $C = a + bY$ there are no taxes. When taxes exist, the MPC applies to $Y - T$, and the tax multiplier is $-\frac{b}{1 - b}$, not $-\frac{1}{1 - b}$. Forgetting the factor $b$ overstates the effect of a tax cut by 25% when $b = 0.8$: \$100 of tax cut raises output by \$400, not \$500.

</div>

<div class="warning" markdown>

Watch out: the MPC is a marginal number, not an average one. If a household earns \$60,000 and spends \$54,000, its average propensity to consume is 0.9. The MPC is about the next dollar, and can be well below or above the average. Using the average spending share as $b$ gives a wrong multiplier.

</div>

<div class="warning" markdown>

Watch out for reading the multiplier as instant. The rounds happen over months and years, and the full \$500 million of Example 1 is only reached in the limit. After 5 rounds, the economy has gone through $336.16$ of the $500$, about two thirds.

</div>

Edge cases. If $b = 0$ (nothing is spent out of extra income) the multiplier is 1, and output moves one for one with autonomous spending. If $b \ge 1$ the model has no sensible equilibrium: the partial sums of the rounds grow without bound, which is the divergence case of the geometric series. A negative change, such as a cut in $G$, is multiplied in the same way: a cut of 100 lowers $Y$ by 500 in Example 1.

## Tricks and shortcuts

Memorise two multipliers. Spending: $\frac{1}{1 - b}$, which is 5 for $b = 0.8$, 10 for $b = 0.9$, 4 for $b = 0.75$ and 2 for $b = 0.5$. Taxes: the spending multiplier times $-b$, which is one less in magnitude, $-4$ for $b = 0.8$. The tax multiplier is always exactly one less in magnitude than the spending multiplier, since $\frac{1}{1 - b} - \frac{b}{1 - b} = 1$, which is the balanced-budget result.

To find the multiplier from a table of leakages, add up the fractions of each extra dollar that do not return to domestic spending, called the leakage rate $\ell = 1 - b(1 - \tau) + m$, and invert: multiplier $= \frac{1}{\ell}$. In Example 3, $\ell = 0.5$ and the multiplier is 2.

To double-check any equilibrium, plug $Y$ back in: $C + I + G$ must equal $Y$. To double-check a multiplier, add the first few rounds and see that they head toward the formula.

## In code

The code solves the equilibrium for the economy of Examples 1 to 3, adds up the rounds of spending, and solves the toy AD-AS economy.

<details class="code" markdown>
<summary>In code</summary>

```python
def equilibrium(a, b, I, G, T=0.0, tau=0.0, m=0.0, X=0.0):
    """Y = a + b*((1 - tau)*Y - T) + I + G + X - m*Y, solved for Y."""
    return (a - b * T + I + G + X) / (1 - b * (1 - tau) + m)

print(round(equilibrium(200, 0.8, 300, 500), 2))             # 5000.0
print(round(equilibrium(200, 0.8, 300, 600), 2))             # 5500.0
print(round(equilibrium(200, 0.8, 300, 500, T=100), 2))      # 4600.0
print(round(equilibrium(200, 0.8, 300, 500, T=200), 2))      # 4200.0
print(round(equilibrium(200, 0.8, 300, 600, T=200), 2))      # 4700.0

# Multiplier with an income tax of 25% and imports of 10% of income.
base = equilibrium(200, 0.8, 300, 500, tau=0.25, m=0.1)
more = equilibrium(200, 0.8, 300, 600, tau=0.25, m=0.1)
print(round(more - base, 2))                                 # 200.0

# Rounds of spending after an extra 100 of G, with b = 0.8.
total, spend = 0.0, 100.0
for k in range(1, 6):
    total += spend
    print(k, round(spend, 2), round(total, 2))
    spend *= 0.8
# 1 100.0 100.0
# 2 80.0 180.0
# 3 64.0 244.0
# 4 51.2 295.2
# 5 40.96 336.16

# Toy AD-AS: AD is Y = 7000 + shift - 20 P, short-run AS is P = 0.02 Y.
def short_run(shift):
    y = (7000 + shift) / (1 + 20 * 0.02)
    return y, 0.02 * y

print([round(v, 2) for v in short_run(0)])                   # [5000.0, 100.0]
print([round(v, 2) for v in short_run(500)])                 # [5357.14, 107.14]
print((7500 - 5000) / 20)                                    # 125.0, the long-run price level
```

The step `y = (7000 + shift) / (1 + 20 * 0.02)` is the algebra of two lines crossing: substituting $P = 0.02Y$ into the AD equation gives $Y = 7000 + \text{shift} - 0.4Y$. Linear solvers such as `numpy.linalg.solve` do the same for a system with many equations, which is how large macro models are solved.

</details>

## FAQ

### Why does the multiplier have to be bigger than 1?

Because each round creates income for someone else. With $0 \le b < 1$ the rounds add to $\frac{1}{1 - b}$, which is at least 1: the first round alone is 1, and every later round is positive. Only if the first round were the whole story ($b = 0$) would the multiplier equal 1. The balanced-budget multiplier of exactly 1 is a different case: the tax takes back the later rounds.

### Does a bigger multiplier mean the economy is better off?

No. A bigger multiplier means output is more sensitive to changes in spending, in both directions. A high $b$ (people spend most of each extra dollar) also means a downturn in spending is amplified. The multiplier says how much a given push moves output, and says nothing about whether the level of output is good.

### Why does the real-world multiplier look smaller than 1 divided by the saving rate?

Real economies have many leakages and offsetting effects. Taxes and imports take part of each dollar (Theorem 3). If the central bank raises interest rates in response to the stimulus, private investment falls, which is called crowding out. If households expect higher taxes later to pay for the spending, they may save the extra income. And if the economy is near capacity, extra demand raises prices more than output. Estimates of the multiplier for government spending are debated, and they vary with the state of the economy. This lesson's numbers are for practice and are not estimates.

### Why is the AD curve downward sloping if the multiplier says spending creates its own income?

The multiplier moves the AD curve to the right. It is silent about the slope, which comes from the price level: a higher price level reduces the real value of money holdings, tends to raise interest rates and makes exports less competitive, so less is demanded. The two ideas answer different questions. The multiplier says how far the curve moves when autonomous spending changes, and the slope says how demand responds to prices.

## Practice

### Warm-up

1\. Find the spending multiplier when (a) $b = 0.9$ and (b) $b = 0.6$. In case (a), by how much does output change when $G$ rises by \$20 billion?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\frac{1}{1 - 0.9} = 10$. A rise of \$20 billion changes output by $10 \times 20 = 200$ billion dollars.

(b) $\frac{1}{1 - 0.6} = 2.5$.

Check: the series $1 + 0.9 + 0.81 + \cdots$ adds up to $\frac{1}{0.1} = 10$, and a larger MPC gives a larger multiplier.

</details>

2\. An economy has $C = 150 + 0.6Y$, $I = 200$ and $G = 250$ (billions of dollars). Find equilibrium output and consumption, and check your answer.

<details class="solution" markdown>
<summary>Solution</summary>

$Y = 150 + 0.6Y + 200 + 250$, so $0.4Y = 600$ and $Y = 1500$. Consumption is $150 + 0.6 \times 1500 = 1050$.

Check: $C + I + G = 1050 + 200 + 250 = 1500 = Y$.

</details>

3\. The government raises purchases by \$60 billion, and $b = 0.75$. List the first four rounds of spending, add them, and compare with the full effect.

<details class="solution" markdown>
<summary>Solution</summary>

The rounds are $60,\ 45,\ 33.75,\ 25.3125$. They add to $164.0625$. The full effect is $\frac{60}{1 - 0.75} = 240$, so four rounds deliver $\frac{164.0625}{240} \approx 68.4\%$ of it.

Check: the ratio of consecutive rounds is $0.75$ each time, and the sum $60\,(1 + 0.75 + 0.5625 + 0.421875) = 60 \times 2.734375 = 164.0625$.

</details>

### Standard

4\. An economy has $C = 100 + 0.8(Y - T)$, $T = 200$, $I = 150$ and $G = 200$. Find equilibrium output. Then find the new output if (a) $T$ rises to 250, and (b) $G$ rises to 250 with $T$ unchanged.

<details class="solution" markdown>
<summary>Solution</summary>

$Y = \frac{100 - 0.8 \times 200 + 150 + 200}{0.2} = \frac{290}{0.2} = 1450$. Consumption is $100 + 0.8 \times 1250 = 1100$, and $1100 + 150 + 200 = 1450$, as it should.

(a) The tax multiplier is $-\frac{0.8}{0.2} = -4$, so a rise of 50 lowers output by 200, to 1250.

(b) The spending multiplier is 5, so a rise of 50 adds 250, giving 1700.

Check: resolving (a) gives $\frac{100 - 200 + 350}{0.2} = 1250$, and resolving (b) gives $\frac{100 - 160 + 400}{0.2} = 1700$.

</details>

5\. Show with the formulas that raising $G$ and $T$ by \$50 billion each, with $b = 0.8$, raises output by exactly \$50 billion. Why isn't the answer 0?

<details class="solution" markdown>
<summary>Solution</summary>

The spending effect is $\frac{1}{0.2} \times 50 = 250$. The tax effect is $-\frac{0.8}{0.2} \times 50 = -200$. The total is $250 - 200 = 50$.

The answer isn't 0 because the tax takes only the fraction $b = 0.8$ out of spending: households would have saved 20% of the \$50 billion, so the tax removes \$40 billion of spending, while the government spends the whole \$50 billion. The net first round is \$10 billion, and the multiplier turns that into \$50 billion.

Check: $\frac{1 - b}{1 - b} = 1$, so the balanced-budget multiplier is 1 for every $b$.

</details>

6\. Suppose $b = 0.9$, the income tax rate is $\tau = 20\%$ and the marginal propensity to import is $m = 0.12$. Find the multiplier, and compare it with the multiplier $\frac{1}{1 - b}$ with no leakages.

<details class="solution" markdown>
<summary>Solution</summary>

The leakage rate is $1 - 0.9 \times 0.8 + 0.12 = 1 - 0.72 + 0.12 = 0.40$, so the multiplier is $\frac{1}{0.40} = 2.5$. With no taxes or imports the multiplier would be $\frac{1}{1 - 0.9} = 10$, four times as large.

Check: the rounds have ratio $0.9 \times 0.8 - 0.12 = 0.60$, and $\frac{1}{1 - 0.6} = 2.5$.

</details>

### Challenge

7\. (a) Use the model of Theorem 3 to show that the multiplier is $\frac{1}{1 - b(1 - \tau) + m}$ again, but this time for a rise in autonomous consumption $a$ rather than $G$. (b) In the economy of Example 3, how large a fall in exports $X$ makes output fall by \$300 billion?

<details class="solution" markdown>
<summary>Solution</summary>

(a) In $Y^* = \frac{a + I + G + X}{1 - b(1 - \tau) + m}$, the variable $a$ enters the numerator exactly as $G$ does, with coefficient 1. So $\Delta Y = \frac{\Delta a}{1 - b(1 - \tau) + m}$, the same multiplier. The same is true of $I$ and $X$.

(b) The multiplier is 2, so $2\,\Delta X = -300$ and $\Delta X = -150$: exports must fall by \$150 billion.

Check: with the base numbers $Y = \frac{1000}{0.5} = 2000$, and with exports lower by 150, $Y = \frac{850}{0.5} = 1700$, a fall of 300.

</details>

8\. (Reviews [infinite series basics](../../05-university-core/05-sequences-and-series/02-infinite-series-basics.md).) Suppose $b = 1$. Write the first four partial sums of the rounds of spending after an extra \$100, say what the series does, and explain what happens to the algebraic solution $Y = \frac{a + I + G}{1 - b}$.

<details class="solution" markdown>
<summary>Solution</summary>

Every round is 100, so the partial sums are $100, 200, 300, 400$, and in general $100n$. They grow without bound, so the series diverges. The ratio $b = 1$ is not below 1 in absolute value, so the geometric series formula does not apply.

The algebraic solution divides by $1 - b = 0$, which is undefined, matching the divergence. Economically, if every extra dollar is spent again in full, the equation $\Delta Y = \Delta G + \Delta Y$ has no solution unless $\Delta G = 0$: any injection pushes spending up round after round and never reaches a resting point.

Check: with $b = 0.99$ the multiplier is 100, and with $b = 0.999$ it is 1000, growing without bound as $b \to 1$.

</details>

## Where this shows up

- The next lesson, [regression and econometrics intuition](03-regression-and-econometrics-intuition.md), is how economists estimate quantities like the MPC from data. Estimating a multiplier is hard because spending and output affect each other, which is the causation problem in that lesson.
- In finance, the geometric series behind the multiplier is the one behind the present value of a perpetuity ([present value, NPV and bond prices](01-present-value-npv-and-bond-prices.md)). The money multiplier in banking, where banks lend out all but a reserve fraction of each deposit, is the same series with ratio $1 - \text{reserve ratio}$ ([infinite series basics](../../05-university-core/05-sequences-and-series/02-infinite-series-basics.md#worked-examples)).
- In CS, an amplification factor $\frac{1}{1 - q}$ appears wherever feedback loops repeat with a fraction $q$ carried over: the expected number of retries of a process that succeeds with probability $1 - q$, and the geometric decay of a signal in a filter. Large macro models are systems of many linear equations like the one solved here, and are solved with linear algebra ([systems and Gaussian elimination](../../05-university-core/06-linear-algebra/02-systems-and-gaussian-elimination.md)).
