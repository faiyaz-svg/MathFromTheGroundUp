# Comparative advantage and gains from trade

After this lesson you can compute each producer's opportunity costs from an output table or an input table, find who has the comparative advantage in each good, give the range of trade prices that make both sides better off, and compute the gains from trade.

Before this: [opportunity cost and the PPC](01-opportunity-cost-and-the-ppc.md) and [ratios and unit rates](../../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. In one day Ana can make 8 mugs or 4 bowls, and Ben can make 6 mugs or 6 bowls. What is each person's opportunity cost of a mug, in bowls? Who has the comparative advantage in mugs?
2. The hours needed to make one unit are: Country X, 3 hours for a bushel of wheat and 6 hours for a bolt of cloth; Country Y, 4 hours for wheat and 12 hours for cloth. Who has the comparative advantage in wheat?
3. Ana and Ben trade mugs for bowls. Which of these prices, in bowls per mug, makes both better off: 0.4, 0.8, 1.2?

<details class="solution" markdown>
<summary>Answers</summary>

1. Ana gives up 4 bowls for 8 mugs, so a mug costs her $\frac{4}{8} = \frac{1}{2}$ bowl. Ben gives up 6 bowls for 6 mugs, so a mug costs him 1 bowl. Ana's cost is lower, so she has the comparative advantage in mugs.
2. A bushel of wheat costs X $\frac{3}{6} = \frac{1}{2}$ bolt of cloth and costs Y $\frac{4}{12} = \frac{1}{3}$ bolt. Y has the lower cost, so Y has the comparative advantage in wheat, although X needs fewer hours for both goods.
3. The price must lie strictly between the two opportunity costs, $\frac{1}{2}$ and 1, so only 0.8 works. At 0.4 Ana would be paid less than a mug costs her, and at 1.2 Ben would pay more than a mug costs him.

</details>

## The idea

Suppose you are better than your friend at everything. You code faster, and you also cook faster. Is there any reason for you to let your friend cook? Yes, if cooking takes more of your coding time than it takes of theirs. Your hour is worth the same whichever job you do, and what matters is what each job costs in the other job.

Say you can write a program in 1 hour or cook a meal in 1 hour, and your friend needs 4 hours for the program and 2 for a meal. You are better at both. But a meal costs you 1 program, and it costs your friend only half a program. If your friend cooks and you code, there is more of both. This is the idea of comparative advantage, and it is one of the few results in economics with a proof you can carry in your head.

The previous lesson gave the tool: opportunity cost is a ratio, and the slope of a PPC. Here we compare the ratios of two producers. The one with the smaller ratio for a good should make that good, and the two trade at a price that lies between the two ratios. Both end up with more than they could make alone.

![Two graphs, Northland and Southland, each with a straight PPC for wheat and cloth. Northland's PPC runs from 300 bolts of cloth to 600 bushels of wheat, with the no-trade point (300, 150), the specialization point (600, 0) and the with-trade point (360, 180) on a dashed trade line of slope minus 3/4 that lies above the PPC. Southland's PPC runs from 400 bolts of cloth to 400 bushels of wheat, with the no-trade point (200, 200), the specialization point (0, 400) and the with-trade point (240, 220) on the same dashed trade line, above the PPC.](../../assets/figures/07-economics-math/comparative-advantage-and-gains-from-trade-trade.svg)

## Definitions

A producer has an **absolute advantage** in a good if it can make more of it from the same inputs, or equivalently if it needs fewer inputs per unit. In plain words, it is simply better at the job: faster, cheaper in hours, higher output.

A producer has a **comparative advantage** in a good if its opportunity cost of making it is lower than another producer's. In plain words, it gives up less of the other good to make this one.

A producer **specializes** in a good if it puts all its resources into that good. A **trade** is an exchange of the goods between producers, and the **terms of trade** are the price at which they exchange, written as units of one good per unit of the other, such as 0.75 bolts of cloth per bushel of wheat. The **gains from trade** are the extra amounts of goods that each side can consume after trading compared with what it could make alone.

Two ways to read an opportunity cost come from the two ways a table can be written. An **output table** gives what each producer can make in the same amount of input: for example, in a day. An **input table** gives the input needed for one unit of each good: for example, hours per unit. The opportunity cost of a unit of good $X$, in units of good $Y$, is

$$
\text{from outputs:} \quad \frac{\text{output of } Y}{\text{output of } X}, \qquad\qquad \text{from inputs:} \quad \frac{\text{input per unit of } X}{\text{input per unit of } Y}.
$$

The two formulas agree because output per hour is one over hours per unit, so the fractions flip. In the input version the good you are costing goes on top.

## How to do it

### Finding comparative advantage

1. Write each producer's opportunity cost of good $X$ in units of $Y$, using the formula that fits the table (output table or input table).
2. The producer with the lower cost of $X$ has the comparative advantage in $X$.
3. The other producer has the comparative advantage in $Y$ (Theorem 1 below shows that this must be so).
4. Check by computing the opportunity cost of $Y$ for each, which should be the reciprocals and should point to the other producer.

*Theorem 1 (someone always has a comparative advantage in each good).* Let producers A and B have opportunity costs $a_X$ and $b_X$ for good $X$ in units of $Y$, and $a_Y$ and $b_Y$ for $Y$ in units of $X$. Then $a_Y = \frac{1}{a_X}$ and $b_Y = \frac{1}{b_X}$. If $a_X < b_X$ then $b_Y < a_Y$: A has the comparative advantage in $X$ and B in $Y$. If $a_X = b_X$ nobody has a comparative advantage.

What we know: an opportunity cost of $X$ is the units of $Y$ given up per unit of $X$ (Theorem 1 of [the PPC lesson](01-opportunity-cost-and-the-ppc.md#the-slope-is-the-opportunity-cost) gave the reciprocal rule for a straight PPC). What we want: that the two producers can't both be cheaper in the same good. The plan is to take reciprocals of an inequality between positive numbers.

*Proof.* Giving up $a_X$ units of $Y$ to get one unit of $X$ means that one unit of $Y$ is worth $\frac{1}{a_X}$ units of $X$, so $a_Y = \frac{1}{a_X}$, and likewise for B. Now suppose $0 < a_X < b_X$. Taking reciprocals of positive numbers reverses an inequality, so $\frac{1}{a_X} > \frac{1}{b_X}$, that is, $a_Y > b_Y$. So B's cost of $Y$ is lower. If $a_X = b_X$, the reciprocals are equal too. $\blacksquare$

Look back: absolute advantage doesn't appear anywhere in the proof. Even if A can make more of both goods, A's cost of one good is higher in terms of the other than B's, whichever way the ratios fall. It is the ratio of the two productivities that counts: A's advantage is larger in one good than in the other, and the larger one is the comparative advantage.

### The two table types

Here is how the formulas work on the same producers written both ways. In a day, a producer makes 8 mugs or 4 bowls. In hours, if a day is 8 hours, a mug takes 1 hour and a bowl takes 2 hours. The cost of a mug in bowls is $\frac{4}{8} = \frac{1}{2}$ from the outputs, and $\frac{1}{2}$ from the inputs ($\frac{1 \text{ hour per mug}}{2 \text{ hours per bowl}}$). Same answer.

The classic trap is to put the fraction upside down. In an input table, a producer who needs more hours for a good is worse at it, and a tempting rule is "the one who needs fewer hours has the advantage". That rule is the test for absolute advantage. Comparative advantage compares the two hours-per-unit numbers for the same producer, with each other, and then compares producers. Example 2 shows a case where the producer that needs fewer hours for both goods is not the one with the comparative advantage in both.

### Terms of trade

Suppose A has the lower cost of $X$, so $a_X < b_X$, and imagine A sells $X$ to B in exchange for $Y$ at the price $p$ units of $Y$ per unit of $X$.

*Theorem 2 (the trade price lies between the two opportunity costs).* With constant opportunity costs, A gains from each unit of $X$ it makes and sells exactly when $p > a_X$, and B gains from each unit of $X$ it buys exactly when $p < b_X$. So both gain exactly when $a_X < p < b_X$. The two together gain $b_X - a_X$ units of $Y$ per unit traded, whatever the price in this range.

What we know: A can turn $a_X$ units of $Y$ into one unit of $X$ by shifting resources, and B can do the same at the rate $b_X$. What we want: the prices at which each side prefers trading to making the goods itself. The plan is to compare the price to each side's cost of the same unit.

*Proof.* For A, making one more unit of $X$ means making $a_X$ fewer units of $Y$. Selling that unit of $X$ brings in $p$ units of $Y$. So A's net change in $Y$ is $p - a_X$, which is positive exactly when $p > a_X$. For B, getting a unit of $X$ without trade means giving up $b_X$ units of $Y$ (B makes it itself), while buying it costs $p$ units of $Y$. So B saves $b_X - p$ units of $Y$, which is positive exactly when $p < b_X$. Both are positive exactly when $a_X < p < b_X$. The two net amounts add to $(p - a_X) + (b_X - p) = b_X - a_X$, which does not depend on $p$. $\blacksquare$

Look back: the price decides how the total gain $b_X - a_X$ is shared. A price near $a_X$ gives most of it to B, and a price near $b_X$ gives most of it to A. At the ends one side gets nothing, which is why the inequality is strict. The proof also says the cost for the trade is quoted in a direction: if the price is in $Y$ per $X$ it must lie between the two costs of $X$ in $Y$. In the other direction (units of $X$ per unit of $Y$) it lies between $\frac{1}{b_X}$ and $\frac{1}{a_X}$, the reciprocals.

### Computing the gains

1. Find the comparative advantages and each producer's PPC.
2. Compute the no-trade bundle for each: the point on its PPC that it would choose by itself (the lesson gives it).
3. Have each specialize in the good where it has the comparative advantage, and compute the total output of each good.
4. Choose a price strictly between the two opportunity costs, and an amount to trade.
5. Subtract what is sold and add what is bought to find each side's bundle after trade, and compare with its no-trade bundle, good by good.
6. Check that the total of each good after trade is the total made, and that the gains in step 5 are positive for both goods and both sides.

## Worked examples

<div class="example" markdown>

### Example 1: Northland and Southland

Northland has 10 worker-days of labour a month and Southland has 20 (all numbers made up). In one worker-day Northland makes 60 bushels of wheat or 30 bolts of cloth, and Southland makes 20 bushels or 20 bolts. Each country, with no trade, puts half its days into each good. Show that trade can leave both better off in both goods.

Step 1: the opportunity cost of a bushel of wheat, in cloth, from the output table: Northland $\frac{30}{60} = \frac{1}{2}$ bolt, Southland $\frac{20}{20} = 1$ bolt.

Step 2: Northland has the lower cost of wheat, so it has the comparative advantage in wheat. By Theorem 1, Southland has it in cloth: a bolt costs Northland $\frac{60}{30} = 2$ bushels and Southland $\frac{20}{20} = 1$ bushel. Northland has the absolute advantage in both goods (60 against 20 and 30 against 20), and that doesn't change the answer.

Step 3: the PPCs. Northland's runs from $(600, 0)$ to $(0, 300)$ in (wheat, cloth), and Southland's from $(400, 0)$ to $(0, 400)$. Without trade, half the days to each good gives Northland $(300, 150)$ and Southland $(200, 200)$. The world has 500 bushels and 350 bolts.

Step 4: if each specializes, Northland makes 600 bushels and Southland makes 400 bolts. The world now has 600 bushels and 400 bolts, more of both. This is the extra output that trade can share.

Step 5: by Theorem 2, a price between $\frac{1}{2}$ and 1 bolt per bushel works for both. Choose the middle, $p = \frac{3}{4}$ bolt per bushel, and let Northland sell 240 bushels for $\frac{3}{4} \times 240 = 180$ bolts.

Step 6: Northland ends with $600 - 240 = 360$ bushels and 180 bolts. Compared with $(300, 150)$, it has 60 more bushels and 30 more bolts. Southland ends with 240 bushels and $400 - 180 = 220$ bolts, against $(200, 200)$: 40 more bushels and 20 more bolts. Both are better off in both goods.

Check: the totals still add up, since $360 + 240 = 600$ bushels and $180 + 220 = 400$ bolts. The gain in cloth terms agrees with Theorem 2: Northland gains $60 \times \frac{1}{2} + 30 = 60$ bolts' worth and Southland gains $40 \times 1 + 20 = 60$, and together that is $120 = 240 \times \left(1 - \frac{1}{2}\right)$.

</div>

<div class="example" markdown>

### Example 2: an input table, and the trap

Country X needs 3 hours to make a bushel of wheat and 6 hours to make a bolt of cloth. Country Y needs 4 hours for wheat and 12 hours for cloth. Who has the comparative advantage in each good?

X needs fewer hours for both goods, so X has the absolute advantage in both. Now the opportunity costs from the input formula, with the costed good on top: a bushel of wheat costs X $\frac{3}{6} = \frac{1}{2}$ bolt and costs Y $\frac{4}{12} = \frac{1}{3}$ bolt. Y's cost of wheat is lower, so Y has the comparative advantage in wheat, and by Theorem 1 X has it in cloth.

Check by the other good: a bolt of cloth costs X $\frac{6}{3} = 2$ bushels and Y $\frac{12}{4} = 3$ bushels, so X's cost is lower, and X has the comparative advantage in cloth. Also check by converting to outputs per 12-hour day: X makes 4 bushels or 2 bolts and Y makes 3 bushels or 1 bolt, and $\frac{2}{4} = \frac{1}{2}$ and $\frac{1}{3}$ agree with the costs above.

<div class="warning" markdown>

Watch out: putting the fraction upside down gives X the cost 2 and Y the cost 3 for wheat, and the wrong conclusion that X is better at wheat. The costed good goes on top in an input table. The check by the second good catches it, because the two answers disagree.

</div>

</div>

<div class="example" markdown>

### Example 3: no gain from trade

Country P makes 6 bushels or 6 bolts per worker-day, and Country Q makes 12 bushels or 12 bolts. Is there a price at which trade helps both?

Each country's cost of a bushel is 1 bolt: $\frac{6}{6} = 1$ and $\frac{12}{12} = 1$. Theorem 2 needs a price strictly between the two costs, and here they are equal, so there is none. At the price 1 bolt per bushel nobody gains: a country that sells a bushel receives 1 bolt, exactly what the bushel cost it in bolts. At any other price one side loses.

Check: Q is twice as productive in both goods, so it has the absolute advantage in both, but because the advantage is the same size in both goods, there are no gains. The bundle after specializing and trading at price 1 is on the same line as the PPC: for P, $b + w = 6$ per worker-day whichever way it trades, and trade doesn't take it outside.

</div>

<div class="example" markdown>

### Example 4: Ana and Ben (finish it yourself)

Use Ana (8 mugs or 4 bowls a day) and Ben (6 mugs or 6 bowls a day) from the quick check. Each works 5 days, and with no trade each splits the days equally between the goods. Ana has the comparative advantage in mugs (cost $\frac{1}{2}$ bowl against Ben's 1), so Ben has it in bowls.

Step 1: the PPCs. Ana makes up to 40 mugs or 20 bowls, and Ben up to 30 mugs or 30 bowls.

Step 2: the no-trade bundles in (mugs, bowls) are Ana $(20, 10)$ and Ben $(15, 15)$.

Now specialize (Ana in mugs, Ben in bowls), trade 16 mugs for 12 bowls (a price of 0.75 bowl per mug, between $\frac{1}{2}$ and 1), and find both final bundles. Compare them with the no-trade bundles.

<details class="solution" markdown>
<summary>Finish</summary>

Ana makes 40 mugs and Ben makes 30 bowls. Ana sells 16 mugs and receives 12 bowls, so she ends with $(40 - 16, 12) = (24, 12)$. Ben ends with $(16, 30 - 12) = (16, 18)$.

Against the no-trade bundles, Ana has 4 more mugs and 2 more bowls, and Ben has 1 more mug and 3 more bowls. Both gain in both goods.

Check: $24 + 16 = 40$ mugs and $12 + 18 = 30$ bowls are the totals made. The price is in range: $\frac{12}{16} = 0.75$, and $0.5 < 0.75 < 1$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: absolute advantage does not decide who should make what. A country can be better at everything and still gain from trade, as Northland did. If you read the input table and say "the one with the smaller number is better, so it should make both", you have found the absolute advantage and answered a different question. Look at the ratio.

</div>

<div class="warning" markdown>

Watch out: the price must be quoted the same way as the costs. If the costs are in bolts per bushel, the price is too. A price of 2 bushels per bolt means $\frac{1}{2}$ bolt per bushel, and that is a different price than 2 bolts per bushel. Convert before you compare.

</div>

<div class="warning" markdown>

Watch out: a price at either end of the range helps only one side. At $p = a_X$ the producer with the comparative advantage gets back exactly what the unit cost it, and at $p = b_X$ the buyer pays exactly what it would pay at home. A correct answer to "can they trade at $p = \frac{1}{2}$?" is "yes, but only B gains".

</div>

<div class="warning" markdown>

Watch out: comparative advantage is relative to a partner. A producer who has the comparative advantage in a good against one partner can have the disadvantage against another. Challenge problem 8 shows Ben switching sides.

</div>

The model has constant costs, and with them total specialization is the end of the story. When the PPC is bowed out, each producer's cost rises as it makes more of a good, and trade stops short of full specialization, at the point where its cost of the good equals the price. The model also leaves out the costs of moving workers and shipping goods, and it does not say who within a country gains or loses. It says that the total available grows, not that every person gains.

## Tricks and shortcuts

To find who has the comparative advantage in $X$ from an output table, compare the ratios $\frac{\text{output of } X}{\text{output of } Y}$ for the two producers. The one with the larger ratio has it. For Ana and Ben this is $\frac{8}{4} = 2$ against $\frac{6}{6} = 1$, so Ana. For an input table, compare $\frac{\text{input per } X}{\text{input per } Y}$ and pick the smaller.

The gain per unit traded is $b_X - a_X$. For 16 mugs traded between Ana and Ben this is $16 \times \left(1 - \frac{1}{2}\right) = 8$ bowls' worth, shared by the price. At the price 0.75 bowls per mug, Ana's share is $16 \times (0.75 - 0.5) = 4$ and Ben's is $16 \times (1 - 0.75) = 4$.

## In code

A function from the two tables to opportunity costs, and the check of the mutually beneficial range, takes only a few lines. It uses exact fractions so that $\frac{1}{3}$ stays $\frac{1}{3}$.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction as F

def opp_costs_from_output(x_out, y_out):
    """Opportunity cost of one X in Y, and of one Y in X, from output per unit of input."""
    return F(y_out, x_out), F(x_out, y_out)

def opp_costs_from_input(x_in, y_in):
    """Same, from input needed per unit of output."""
    return F(x_in, y_in), F(y_in, x_in)

# Ana and Ben: output per day (mugs, bowls)
ana = opp_costs_from_output(8, 4)
ben = opp_costs_from_output(6, 6)
print("OC of a mug in bowls: Ana", ana[0], "Ben", ben[0])
# OC of a mug in bowls: Ana 1/2 Ben 1
lo, hi = sorted([ana[0], ben[0]])
print("mutually beneficial prices (bowls per mug) lie strictly between", lo, "and", hi)
# mutually beneficial prices (bowls per mug) lie strictly between 1/2 and 1

# Hours per unit (wheat, cloth): the classic trap
x = opp_costs_from_input(3, 6)
y = opp_costs_from_input(4, 12)
print("OC of wheat in cloth: X", x[0], "Y", y[0])
# OC of wheat in cloth: X 1/2 Y 1/3
print("comparative advantage in wheat:", "X" if x[0] < y[0] else "Y")
# comparative advantage in wheat: Y

# Gains from the Ana and Ben trade: 16 mugs for 12 bowls
ana_after = (40 - 16, 12)
ben_after = (16, 30 - 12)
print(ana_after, ben_after)
# (24, 12) (16, 18)
```

</details>

## FAQ

### If I am better at everything, why not do it all myself?

Because you have only so many hours. Every hour you spend on the job that costs you more is an hour not spent on the job where you are most ahead. If your friend does that job, you give up less than you gain. The saving is real as long as your friend's cost of that job in the other job is lower than yours, even if your friend is slower at everything.

### What if the two opportunity costs are equal?

Then there are no gains from specializing, as in Example 3. The PPCs are parallel (same slope), and no price makes both sides better off.

### Does this work with more than two goods or two countries?

The idea extends: each good goes to the producers with the lowest opportunity cost, and prices settle between the costs. The bookkeeping gets longer, with a ratio for each pair of goods, and it is the subject of an international trade course. This lesson keeps to two and two, where the algebra is complete.

### Why do real producers not specialize completely?

The model assumes a straight PPC. With increasing opportunity cost (the bowed curve), the cost of the next unit of the specialized good keeps rising, and at some point it reaches the price, so producing more no longer pays. Shipping costs and other limits also matter. The straight-line model gives the clearest statement of the principle.

## Practice

### Warm-up

1\. In one hour Dev can write 6 functions or 3 test files, and Eli can write 2 functions or 2 test files. (a) Find each person's opportunity cost of a function, in test files. (b) Who has the comparative advantage in functions, and who in test files? (c) Who has the absolute advantage?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Dev: $\frac{3}{6} = \frac{1}{2}$ test file per function. Eli: $\frac{2}{2} = 1$ test file per function.

(b) Dev's cost of a function is lower, so Dev has the comparative advantage in functions. By Theorem 1, Eli has it in test files: a test file costs Dev 2 functions and Eli 1 function.

(c) Dev has the absolute advantage in both (6 against 2 functions, and 3 against 2 test files).

Check: the costs of a test file, 2 and 1, are the reciprocals of $\frac{1}{2}$ and 1.

</details>

2\. Farm F needs 2 hours for a tonne of potatoes and 8 hours for a tonne of corn. Farm G needs 3 hours and 10 hours. (a) Find the opportunity cost of a tonne of potatoes, in corn, for each farm. (b) Who has the comparative advantage in each crop? (c) Which farm has the absolute advantage?

<details class="solution" markdown>
<summary>Solution</summary>

(a) From the input formula with potatoes on top: F, $\frac{2}{8} = \frac{1}{4}$ tonne of corn. G, $\frac{3}{10} = 0.3$ tonne of corn.

(b) F has the lower cost of potatoes ($0.25 < 0.3$), so F has the comparative advantage in potatoes and G in corn. Check with corn: a tonne of corn costs F $\frac{8}{2} = 4$ tonnes of potatoes and G $\frac{10}{3} \approx 3.33$, so G's is lower.

(c) F needs fewer hours for both ($2 < 3$ and $8 < 10$), so F has the absolute advantage in both.

</details>

3\. Using Ana (cost of a mug $\frac{1}{2}$ bowl) and Ben (1 bowl), decide for each price in bowls per mug whether both gain: 0.4, 0.5, 0.8, 1, 1.25. If only one side gains, say which.

<details class="solution" markdown>
<summary>Solution</summary>

Both gain only strictly between $\frac{1}{2}$ and 1, so only 0.8.

At 0.4, Ana receives 0.4 bowl for a mug that costs her 0.5, so she loses, and Ben gains. At 0.5, Ana gains nothing and Ben gains $1 - 0.5 = 0.5$ bowl per mug. At 1, Ben gains nothing and Ana gains 0.5. At 1.25, Ben pays 1.25 for a mug that costs him 1, so he loses, and Ana gains.

Check: the gain per mug is $1 - \frac{1}{2} = \frac{1}{2}$ bowl in total when $\frac{1}{2} \le p \le 1$. At 0.8, Ana gains 0.3 and Ben 0.2, and $0.3 + 0.2 = 0.5$.

</details>

### Standard

4\. Country P has 10 worker-days and makes 12 shirts or 4 jackets per worker-day. Country Q has 20 worker-days and makes 5 shirts or 5 jackets per worker-day. With no trade each splits its days equally. (a) Who has the comparative advantage in each good? (b) Find each country's no-trade bundle and the world totals. (c) With specialization, what are the world totals? (d) P sells 54 shirts to Q for 36 jackets. Find both final bundles and the gains.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The cost of a shirt, in jackets: P, $\frac{4}{12} = \frac{1}{3}$. Q, $\frac{5}{5} = 1$. P has the comparative advantage in shirts, Q in jackets (a jacket costs P 3 shirts and Q 1 shirt).

(b) P's PPC runs to 120 shirts or 40 jackets. Half the days gives $(60, 20)$ in (shirts, jackets). Q can make 100 shirts or 100 jackets, and half the days gives $(50, 50)$. The world has 110 shirts and 70 jackets.

(c) P specializes in shirts, 120, and Q in jackets, 100. The world has 120 shirts and 100 jackets.

(d) The price is $\frac{36}{54} = \frac{2}{3}$ jacket per shirt, between $\frac{1}{3}$ and 1. P ends with $(120 - 54, 36) = (66, 36)$, which is 6 more shirts and 16 more jackets than $(60, 20)$. Q ends with $(54, 100 - 36) = (54, 64)$, which is 4 more shirts and 14 more jackets than $(50, 50)$.

Check: $66 + 54 = 120$ and $36 + 64 = 100$. The total gain is $54 \times \left(1 - \frac{1}{3}\right) = 36$ jackets' worth: P gains $6 \times \frac{1}{3} + 16 = 18$ and Q gains $4 \times 1 + 14 = 18$.

</details>

5\. In Problem 4, a trader offers to exchange 2 shirts for each jacket. (a) Convert this to a price in jackets per shirt and say if both countries gain. (b) What about 4 shirts per jacket? (c) State the range of prices that work, in shirts per jacket.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Two shirts per jacket is $\frac{1}{2}$ jacket per shirt, which lies between $\frac{1}{3}$ and 1. Both gain.

(b) Four shirts per jacket is $\frac{1}{4}$ jacket per shirt, below $\frac{1}{3}$. P, who sells shirts, would get a quarter jacket for a shirt that costs it a third of a jacket, so P loses. Equivalently P could make a jacket itself with 3 shirts, and the trade asks for 4.

(c) The range in jackets per shirt is $\frac{1}{3} < p < 1$. In shirts per jacket take reciprocals, which reverses the inequality: $1 < \frac{1}{p} < 3$.

Check: the endpoints are the two costs of a jacket in shirts, 1 for Q and 3 for P, and $2$ and $1.5 = \frac{1}{2/3}$ both lie inside $(1, 3)$.

</details>

6\. Country A needs 2 hours for a tonne of wheat and 4 hours for a bolt of cloth. Country B needs 5 hours for wheat and 8 hours for cloth. (a) Find who has the comparative advantage in each good. (b) Give the range of prices, in bolts per tonne of wheat, at which both gain. (c) What conclusion would you wrongly draw by inverting the fractions?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The cost of a tonne of wheat in cloth: A, $\frac{2}{4} = 0.5$ bolt. B, $\frac{5}{8} = 0.625$ bolt. A's is lower, so A has the comparative advantage in wheat and B in cloth (a bolt costs A 2 tonnes and B $1.6$ tonnes).

(b) The price must lie strictly between 0.5 and 0.625 bolts per tonne.

(c) Inverted, the fractions give A $\frac{4}{2} = 2$ and B $\frac{8}{5} = 1.6$, and "B has the lower cost of wheat" is the wrong conclusion. Those are the costs of cloth in wheat.

Check: $\frac{1}{0.5} = 2$ and $\frac{1}{0.625} = 1.6$, the costs of cloth, which are in the opposite order, as Theorem 1 says.

</details>

### Challenge

7\. In general, a producer with the comparative advantage in $X$ has cost $a_X$ and its partner has cost $b_X$ with $a_X < b_X$. They trade $n$ units of $X$ at price $p$ with $a_X < p < b_X$. Show that the seller's gain is $n(p - a_X)$ and the buyer's gain is $n(b_X - p)$, both in units of $Y$, and that the total does not depend on $p$. Check it with Ana and Ben, who traded 16 mugs at 0.75.

<details class="solution" markdown>
<summary>Solution</summary>

By Theorem 2 each unit gives the seller $p - a_X$ and the buyer $b_X - p$. For $n$ units, multiply: $n(p - a_X)$ and $n(b_X - p)$. Their sum is $n(b_X - a_X)$, with no $p$ in it.

For Ana and Ben, $n = 16$, $a_X = \frac{1}{2}$, $b_X = 1$ and $p = 0.75$. Ana gains $16 \times 0.25 = 4$ bowls' worth and Ben gains $16 \times 0.25 = 4$. In Example 4, Ana gained 4 mugs and 2 bowls, which is $4 \times \frac{1}{2} + 2 = 4$ bowls' worth, and Ben gained 1 mug and 3 bowls, which is $1 \times 1 + 3 = 4$.

Check: the total is $16 \times \frac{1}{2} = 8$, and $4 + 4 = 8$.

</details>

8\. (Reviews [ratios and unit rates](../../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md) and the previous lesson.) A third trader, Chen, makes 5 mugs or 10 bowls a day. Compare Chen with Ana (8 mugs or 4 bowls) and with Ben (6 mugs or 6 bowls). (a) Find Chen's cost of a mug. (b) With Chen as partner, who has the comparative advantage in mugs: Ana or Chen? Ben or Chen? (c) What does this say about Ben?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Chen gives up 10 bowls for 5 mugs, so a mug costs 2 bowls.

(b) Ana's cost is $\frac{1}{2}$ bowl against Chen's 2, so Ana has the comparative advantage in mugs. Ben's cost is 1 against Chen's 2, so Ben has the comparative advantage in mugs, and Chen has it in bowls.

(c) Against Ana, Ben has the comparative advantage in bowls (cost of a bowl 1 mug against Ana's 2 mugs). Against Chen, Ben has it in mugs. Comparative advantage depends on the partner.

Check: the costs of a mug in bowls are $\frac{1}{2}$ (Ana), 1 (Ben) and 2 (Chen), so Ben is in the middle: higher than Ana and lower than Chen. A mug trade between Ben and Chen could be at any price in $(1, 2)$.

</details>

## Where this shows up

- The next lesson, [supply and demand equilibrium algebra](03-supply-and-demand-equilibrium-algebra.md), has the prices that markets settle on, and [surplus and market interventions](04-surplus-and-market-interventions.md) measures the gains to buyers and sellers, which is the same idea as the gains from trade.
- In CS, assigning tasks to machines or people by the ratio of their speeds follows the same logic: give each job to whoever loses least by taking it. Scheduling on machines with different speeds uses this reasoning.
- International trade courses, and Canada's trade debates, begin from this model, and then add what it leaves out, such as costs of moving and who within a country gains or loses.
