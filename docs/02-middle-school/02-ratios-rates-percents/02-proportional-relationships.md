# Proportional relationships

After this lesson you can solve a proportion, tell from a table, a graph or an equation whether two quantities are proportional, find and use the constant of proportionality, and work with scale drawings and map scales.

Before this: [ratios and unit rates](01-ratios-and-unit-rates.md), and the cross-multiplication test in [fractions and equivalent fractions](../../01-elementary/09-fractions-and-equivalent-fractions.md#comparing-two-fractions).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $\frac{x}{18} = \frac{5}{12}$.
2. When $x$ is 2, 5 and 8, the matching values of $y$ are 7, 17.5 and 28. Is $y$ proportional to $x$? If so, find the constant of proportionality.
3. A map has a scale of $1:50{,}000$. Two towns are 7.4 cm apart on the map. How far apart are they, in kilometres?

<details class="solution" markdown>
<summary>Answers</summary>

1. Cross-multiply: $12x = 5 \times 18 = 90$, so $x = 90 \div 12 = 7.5$.
2. Yes. Each quotient $y \div x$ is 3.5, since $7 \div 2$, $17.5 \div 5$ and $28 \div 8$ all equal 3.5. So $y = 3.5x$, and the constant is 3.5.
3. On the ground the distance is $7.4 \times 50{,}000 = 370{,}000$ cm. A kilometre is 100,000 cm, so that is 3.7 km.

</details>

## The idea

At a gas pump, two numbers climb together: the litres and the dollars. If gas costs \$1.50 a litre, here are some of the pairs the pump shows:

| Litres | Cost (dollars) |
|---|---|
| 0 | 0.00 |
| 10 | 15.00 |
| 20 | 30.00 |
| 30 | 45.00 |
| 45 | 67.50 |

Double the litres and the cost doubles; pump nothing and you pay nothing. Every row has the same ratio of dollars to litres, 1.50, which is the price per litre. Two quantities that behave like this are proportional, and one equation describes every row: the cost is 1.5 times the litres.

Now take a taxi that charges \$4.50 when you get in, plus \$2.00 per kilometre. A 5 km ride costs \$14.50, but a 10 km ride costs \$24.50, not twice as much, because you pay the \$4.50 only once. The fare rises steadily with the distance, but it is not proportional to it. This lesson shows how to tell the two kinds apart, and how to solve problems about the first kind quickly.

## Definitions

A **proportion** is an equation stating that two ratios are equal:

$$
\frac{a}{b} = \frac{c}{d}, \qquad \text{where } b \ne 0 \text{ and } d \ne 0.
$$

It is read "$a$ is to $b$ as $c$ is to $d$", and it is sometimes written $a:b = c:d$. In plain words, a proportion says that two ratios make the same comparison, such as 27 L of gas for 360 km and 37.5 L for 500 km.

Two quantities $x$ and $y$ are **proportional** (or directly proportional) when there is a nonzero number $k$ such that

$$
y = kx
$$

for every pair of matching values. The number $k$ is the **constant of proportionality**. Elsewhere in this book $k$ usually names an integer, but in $y = kx$ it can be any nonzero number (see the [letter table](../../reference/symbols-and-notation.md#one-letter-one-meaning-in-this-book)).

In plain words, $y$ is always the same multiple of $x$. Dividing both sides by $x$ gives $k = \frac{y}{x}$ for every pair with $x \ne 0$, so $k$ is the unit rate: the amount of $y$ for one unit of $x$. For the gas pump, write $x$ for the litres and $y$ for the cost in dollars. Then $k = 1.5$ dollars per litre, and $y = 1.5x$.

A **scale drawing** is a drawing of an object in which every length is the same multiple of the matching real length. Its **scale** is the ratio of a length in the drawing to the matching real length. A map scale of $1:50{,}000$ means that 1 cm on the map stands for 50,000 cm on the ground, and 1 mm for 50,000 mm; a scale with no units uses the same unit on both sides. A scale can also be written with two units, such as 1 cm : 0.5 km, which says the same thing. Either way, the lengths in the drawing are proportional to the real lengths.

## How to do it

### Solving a proportion

1. Set up the proportion with the same kind of quantity in the same place on both sides: if litres are on top on the left, litres go on top on the right.
2. Cross-multiply: from $\frac{a}{b} = \frac{c}{d}$, write $a \times d = b \times c$.
3. Divide both sides by the number that multiplies the unknown.
4. Check by putting the answer back and comparing the two ratios as decimals, or with an estimate.

Instead of Steps 2 and 3, you can find the unit rate first and multiply. It is the same arithmetic in a different order, and Example 1 does it both ways.

### Why cross-multiplication works

We know that $\frac{a}{b} = \frac{c}{d}$, where $b$ and $d$ are not 0. We want to show that $ad = bc$. The plan is to multiply both sides by $bd$, which clears both denominators.

Multiplying both sides of an equation by the same number keeps them equal, so

$$
\frac{a}{b} \times bd = \frac{c}{d} \times bd.
$$

On the left the $b$ cancels, leaving $a \times d$. On the right the $d$ cancels, leaving $c \times b$. So $ad = bc$.

Looking back, the steps also run backwards: if $ad = bc$, dividing both sides by $bd$, which is not 0, gives $\frac{a}{b} = \frac{c}{d}$. So the cross-multiplied equation has exactly the same solutions as the proportion. The two products are the ones you compare in the cross-multiplication test for fractions, and solving equations by doing the same thing to both sides gets its own lesson in [one- and two-step equations](../03-expressions-equations-inequalities/03-one-and-two-step-equations.md).

### Testing whether two quantities are proportional

1. From a table: divide $y$ by $x$ in every row where $x \ne 0$. If every quotient is the same number, $y$ is proportional to $x$, and that number is $k$. A row with $x = 0$ must have $y = 0$.
2. From a graph: plot each pair as a point, with $x$ across and $y$ up, as in [the coordinate plane](../05-linear-relationships-and-functions/01-coordinate-plane.md). The quantities are proportional exactly when the points lie on a straight line through the origin, the point $(0, 0)$ where the axes cross. A straight line that misses the origin, or a curve, means they are not.
3. From an equation: the relationship is proportional when it has the form $y = kx$, with nothing added on. The taxi fare, $y = 2x + 4.5$, has 4.5 added, so it is not.

The graph of $y = kx$ passes through the origin because $x = 0$ gives $y = k \times 0 = 0$. It is straight because each step of 1 to the right adds the same amount, $k$, to $y$. That steady climb is the slope of the line, the subject of [slope and linear equations](../05-linear-relationships-and-functions/02-slope-and-linear-equations.md).

### Scale drawings and map scales

1. Write the scale as drawing length to real length. If it has no units, such as $1:50{,}000$, measure in any unit and keep that unit on both sides.
2. To go from the drawing to real life, multiply by the second term of the scale. To go from real life to the drawing, divide by it.
3. Convert the answer to a sensible unit at the end. On maps, 100,000 cm is 1 km.
4. Check that the size makes sense.

On a hiking map at $1:50{,}000$, a trail that measures 12.6 cm is $12.6 \times 50{,}000 = 630{,}000$ cm long, which is 6.3 km. In the other direction, a 2 km trail is 200,000 cm, so the map draws it $200{,}000 \div 50{,}000 = 4$ cm long.

## Worked examples

<div class="example" markdown>

### Example 1: gas for a longer trip

Your car used 27 L of gas to drive 360 km. At the same rate, how many litres will it use for 500 km?

Step 1: let $x$ be the litres for 500 km. Put litres on top and kilometres on the bottom on both sides:

$$
\frac{27}{360} = \frac{x}{500}.
$$

<div class="warning" markdown>

Watch out at Step 1: flipping one side, as in $\frac{27}{360} = \frac{500}{x}$, mixes litres per kilometre with kilometres per litre. It gives $x = 6666.7$ L, more than a hundred tankfuls. If an answer is far from your estimate, check that both sides of the proportion have their units in the same places.

</div>

Step 2: cross-multiply:

$$
360 \times x = 27 \times 500, \quad \text{that is,} \quad 360x = 13{,}500.
$$

Step 3: divide both sides by 360, the number that multiplies $x$: $x = 13{,}500 \div 360 = 37.5$. The car will use 37.5 L.

Step 4: check the ratios. On the left, $27 \div 360 = 0.075$, and on the right, $37.5 \div 500 = 0.075$. For an estimate, 500 km is a little less than $1.5 \times 360 = 540$ km, so the gas should be a little less than $1.5 \times 27 = 40.5$ L, and 37.5 L is.

The unit-rate route gives the same answer. The constant of proportionality is $k = 27 \div 360 = 0.075$ litres per kilometre, so a trip of $d$ km uses $0.075d$ litres, and $0.075 \times 500 = 37.5$.

</div>

<div class="example" markdown>

### Example 2: finding the constant from a table

A tutor charges \$48 for 1.5 hours, \$64 for 2 hours and \$112 for 3.5 hours. Is the cost proportional to the time? If it is, what do 5 hours cost, and how long can you book for \$200?

Divide each cost by its time: $48 \div 1.5 = 32$, $64 \div 2 = 32$ and $112 \div 3.5 = 32$. Every quotient is 32, so the cost is proportional to the time, with $k = 32$ dollars per hour. For $x$ hours the cost is $y = 32x$ dollars.

Five hours cost $32 \times 5 = 160$ dollars. For \$200, solve $32x = 200$ by dividing by 32: $x = 6.25$ hours, which is 6 hours 15 minutes.

Check: $32 \times 6.25 = 200$, and 6.25 h is between 3.5 h and twice 3.5 h, as \$200 is between \$112 and twice \$112.

</div>

<div class="example" markdown>

### Example 3: a taxi fare is not proportional

The taxi from [The idea](#the-idea) charges \$4.50 plus \$2.00 per kilometre. Is the fare proportional to the distance?

Make a table and divide the fare by the distance:

| Distance (km) | Fare (dollars) | Fare per km |
|---|---|---|
| 2 | 8.50 | 4.25 |
| 5 | 14.50 | 2.90 |
| 10 | 24.50 | 2.45 |

The quotients are not equal, so the fare is not proportional to the distance. Plotted, the points do lie on a straight line, but the line crosses the vertical axis at 4.50 instead of 0: a ride of 0 km, where you get in and straight back out, still costs \$4.50. The relationship is linear but not proportional.

A proportion gives the wrong answer here. From $\frac{14.50}{5} = \frac{x}{10}$, cross-multiplying gives $5x = 145$, so $x = 29.00$. That is \$4.50 too much, because it charges the base fare twice. The right fare for 10 km is $4.50 + 2.00 \times 10 = 24.50$ dollars.

What stays constant in this table is the change: each extra kilometre adds \$2.00. Only the part of the fare above the base charge is proportional to the distance, since $24.50 - 4.50 = 20 = 2 \times 10$.

</div>

<div class="example" markdown>

### Example 4: a floor plan (finish it yourself)

A floor plan is drawn at a scale of $1:50$. A bedroom on the plan measures 9.2 cm by 7 cm. What are the real length, width and floor area of the room?

Steps 1 and 2: multiply each length on the plan by 50 to get the real length: $9.2 \times 50 = 460$ cm and $7 \times 50 = 350$ cm.

Step 3: in metres, the room is 4.6 m by 3.5 m.

Now find the floor area, and check it against the area of the rectangle on the plan.

<details class="solution" markdown>
<summary>Finish</summary>

The floor area is $4.6 \times 3.5 = 16.1\ \text{m}^2$.

Check: on the plan the room covers $9.2 \times 7 = 64.4\ \text{cm}^2$. Each length was multiplied by 50, so the area was multiplied by $50 \times 50 = 2500$. That gives $64.4 \times 2500 = 161{,}000\ \text{cm}^2$, and since $1\ \text{m}^2 = 10{,}000\ \text{cm}^2$, this is $16.1\ \text{m}^2$. Multiplying the plan area by only 50 would give $3220\ \text{cm}^2$, about a third of a square metre, which is far too small for a bedroom.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for a fixed amount. A proportion only works when zero of one quantity goes with zero of the other. A base fare, a delivery fee, a sign-up charge or a flat monthly fee breaks this, as in Example 3. Before you set up a proportion, ask "would zero of this cost zero?"

</div>

<div class="warning" markdown>

Watch out for the units in a scale. A map at $1:50{,}000$ does not mean 1 cm to 50,000 m or 50,000 km. Both sides are in the same unit, so 1 cm stands for 50,000 cm, which is 500 m, or 0.5 km.

</div>

<div class="warning" markdown>

Watch out: areas don't scale by the scale factor. At $1:50$, lengths are multiplied by 50 but areas by $50^2 = 2500$, and volumes by $50^3 = 125{,}000$. This is the same reason that a square metre is $10{,}000\ \text{cm}^2$ ([measurement and unit conversion](../../01-elementary/15-measurement-and-unit-conversion.md#edge-cases-and-common-mistakes)).

</div>

<div class="warning" markdown>

Watch out: one pair of values can't show proportionality, since every single pair has a ratio. Check every row of a table, and check that $x = 0$ gives $y = 0$. In a table with the rows $(2, 6)$, $(4, 12)$ and $(5, 16)$, the first two rows give 3 and the third gives 3.2, so $y$ is not proportional to $x$.

</div>

The constant $k$ can be a fraction or a small decimal. Going from the ground to the map at $1:50{,}000$, the constant is $\frac{1}{50{,}000}$. It can even be negative, as in $y = -2x$, whose line through the origin goes down from left to right ([negative numbers and absolute value](../01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md)). This book keeps $k$ positive in this chapter. The value $k = 0$ is left out of the definition, because $y = 0x$ would make $y$ always 0.

A proportion can't have 0 in a denominator, for the same reason a fraction can't. If setting up a proportion puts a 0 on the bottom, the question is not about a ratio of that quantity.

## Tricks and shortcuts

Look for a whole-number factor before you cross-multiply. In $\frac{x}{12} = \frac{15}{36}$, the denominator 36 becomes 12 by dividing by 3, so the numerator does too: $x = 15 \div 3 = 5$. You can also simplify one side first, since $\frac{15}{36} = \frac{5}{12}$, and then read off $x = 5$.

For map scales, $1:100{,}000$ means 1 cm stands for 1 km. In general, at $1:n$, 1 cm on the map is $n \div 100{,}000$ km on the ground. So at $1:50{,}000$ a centimetre is 0.5 km, and at $1:250{,}000$ it is 2.5 km.

Two fast tests catch most non-proportional relationships. The zero test asks whether 0 of $x$ gives 0 of $y$. The doubling test asks whether twice $x$ gives twice $y$. The taxi fare fails both: 0 km costs \$4.50, and doubling 5 km to 10 km takes the fare from \$14.50 to \$24.50, not \$29.00.

## In code

Testing a table for a constant ratio is a natural loop. Python's `Fraction` type does the division exactly, which matters because floats can make equal ratios look different.

<details class="code" markdown>
<summary>In code</summary>

```python
from fractions import Fraction

def constant_of_proportionality(xs, ys):
    """Return k if y = kx for every pair in the table, otherwise None."""
    ratios = set()
    for x, y in zip(xs, ys):
        x, y = Fraction(x), Fraction(y)
        if x == 0:
            if y != 0:
                return None   # a point (0, y) with y not 0 is on no line y = kx
            continue
        ratios.add(y / x)
    return ratios.pop() if len(ratios) == 1 else None

print(constant_of_proportionality(["1.5", "2", "3.5"], ["48", "64", "112"]))      # tutor: 32
print(constant_of_proportionality(["2", "5", "10"], ["8.50", "14.50", "24.50"]))  # taxi: None
print(constant_of_proportionality(["0.1", "0.3"], ["0.3", "0.9"]))                # 3

print(0.3 / 0.1, 0.9 / 0.3)   # 2.9999999999999996 3.0
```

The last line shows the problem the function avoids. With floats, $0.3 \div 0.1$ and $0.9 \div 0.3$ come out different, so a float version would wrongly report the third table as not proportional. Passing the values as strings lets `Fraction` store 0.1 exactly as $\frac{1}{10}$. Floating-point basics<!-- link: ../../06-cs-math/01-number-representation/04-floating-point-basics.md --> explains why floats can't.

</details>

## FAQ

### Why can't I cross-multiply to add fractions?

Cross-multiplying comes from an equation: you multiply both sides by $bd$. A sum such as $\frac{1}{2} + \frac{1}{3}$ is not an equation, so there are no two sides to multiply. Adding fractions needs a common denominator, as in [adding and subtracting fractions](../../01-elementary/10-adding-and-subtracting-fractions.md), and multiplying them goes straight across, numerator times numerator.

### What is inverse proportion?

Two quantities are inversely proportional when their product is constant, so $y = \frac{k}{x}$. On a 240 km drive, the time is $\frac{240}{\text{speed}}$: at 60 km/h it takes 4 h, at 80 km/h 3 h, and at 120 km/h 2 h. Doubling the speed halves the time, and the graph is a curve, not a line. When a book says "proportional" with no other word, it means direct proportion, $y = kx$.

### Is every straight-line graph a proportional relationship?

No. Every proportional relationship has a straight-line graph through the origin, but the taxi fare is a straight line that misses the origin. Straight-line relationships in general are linear, with equations of the form $y = mx + b$, where $m$ is the slope and $b$ is where the line crosses the vertical axis ([slope and linear equations](../05-linear-relationships-and-functions/02-slope-and-linear-equations.md)). A proportional relationship is the linear case with $b = 0$.

## Practice

### Warm-up

1\. Solve each proportion: (a) $\frac{x}{15} = \frac{4}{6}$, (b) $\frac{9}{x} = \frac{21}{35}$, (c) $\frac{2.5}{4} = \frac{x}{10}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Cross-multiply: $6x = 4 \times 15 = 60$, so $x = 10$.
- (b) Cross-multiply: $21x = 9 \times 35 = 315$, so $x = 315 \div 21 = 15$.
- (c) Cross-multiply: $4x = 2.5 \times 10 = 25$, so $x = 6.25$.

Check by comparing the ratios: $\frac{10}{15} = 0.666\ldots = \frac{4}{6}$, $\frac{9}{15} = 0.6 = \frac{21}{35}$, and $\frac{2.5}{4} = 0.625 = \frac{6.25}{10}$.

</details>

2\. Is $y$ proportional to $x$? If it is, give $k$ and the equation. (a) When $x$ is 3, 6 and 10, $y$ is 4.5, 9 and 15. (b) When $x$ is 1, 2 and 4, $y$ is 5, 8 and 14. (c) When $x$ is 0, 4 and 6, $y$ is 0, 10 and 15.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $4.5 \div 3 = 1.5$, $9 \div 6 = 1.5$ and $15 \div 10 = 1.5$. Proportional, with $k = 1.5$ and $y = 1.5x$.
- (b) $5 \div 1 = 5$, $8 \div 2 = 4$ and $14 \div 4 = 3.5$. The quotients differ, so it is not proportional. (Each step of 1 in $x$ adds 3 to $y$, starting from 2 at $x = 0$, so $y = 3x + 2$.)
- (c) The row $x = 0$ has $y = 0$, as it must. The other rows give $10 \div 4 = 2.5$ and $15 \div 6 = 2.5$. Proportional, with $k = 2.5$ and $y = 2.5x$.

Check (b) with the doubling test: doubling $x$ from 2 to 4 takes $y$ from 8 to 14, not 16.

</details>

3\. A road map has a scale of $1:250{,}000$. (a) Two towns are 6.8 cm apart on the map. How far apart are they? (b) How long is a 30 km road on the map?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Multiply by 250,000: $6.8 \times 250{,}000 = 1{,}700{,}000$ cm. Divide by 100,000 to get kilometres: 17 km.

(b) At this scale 1 cm stands for $250{,}000 \div 100{,}000 = 2.5$ km, so 30 km is drawn $30 \div 2.5 = 12$ cm long.

Check: $12 \times 2.5 = 30$ and $6.8 \times 2.5 = 17$.

</details>

### Standard

4\. Your pay is proportional to the hours you work, and 12 hours earn \$222. (a) Find $k$ and write the equation. (b) What do 30 hours earn? (c) How many hours do you need to work to earn \$500?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $k = 222 \div 12 = 18.5$ dollars per hour. For $x$ hours the pay is $y = 18.5x$ dollars.

(b) $18.5 \times 30 = 555$, so \$555.

(c) Solve $18.5x = 500$: $x = 500 \div 18.5 = 27.027\ldots$, about 27 hours. Working exactly 27 hours earns $18.5 \times 27 = 499.50$ dollars, 50 cents short, so you need a little over 27 hours.

Check: 30 hours is 2.5 times 12 hours, and $2.5 \times 222 = 555$.

</details>

5\. A courier charges \$7 plus \$1.20 per kilometre. (a) What do deliveries of 5 km and 10 km cost? (b) Is the cost proportional to the distance? (c) A friend says, "5 km costs \$13, so 15 km costs three times as much, \$39." What is the right cost, and what went wrong?

<details class="solution" markdown>
<summary>Solution</summary>

(a) For 5 km, $7 + 1.20 \times 5 = 13$ dollars. For 10 km, $7 + 1.20 \times 10 = 19$ dollars.

(b) No. The cost per kilometre is $13 \div 5 = 2.60$ for 5 km and $19 \div 10 = 1.90$ for 10 km, which are different. The doubling test fails too: twice the distance costs \$19, not \$26.

(c) The right cost is $7 + 1.20 \times 15 = 25$ dollars. Tripling \$13 also triples the \$7 fee, which you only pay once, so the friend's answer is $2 \times 7 = 14$ dollars too high.

Check: $39 - 25 = 14$.

</details>

6\. A model car is built at a scale of $1:24$. (a) The model is 19 cm long. How long is the real car? (b) The real car is 1.8 m wide. How wide is the model?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Multiply by 24: $19 \times 24 = 456$ cm, which is 4.56 m.

(b) Write the width in centimetres, 180 cm, and divide by 24: $180 \div 24 = 7.5$ cm.

Check the size: 4.56 m is a normal length for a car. And the model's shape matches the real one: $\frac{19}{7.5} = 2.533\ldots$ and $\frac{456}{180} = 2.533\ldots$

</details>

### Challenge

7\. A photo is 10 cm by 15 cm. You enlarge it, keeping it in proportion, so that the short side is 25 cm. (a) How long is the long side? (b) How many times bigger is the area?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The short side goes from 10 cm to 25 cm, a factor of $25 \div 10 = 2.5$. Keeping the photo in proportion multiplies the long side by 2.5 as well: $15 \times 2.5 = 37.5$ cm. As a proportion, $\frac{10}{15} = \frac{25}{x}$ gives $10x = 375$ and $x = 37.5$.

(b) Both lengths were multiplied by 2.5, so the area is multiplied by $2.5 \times 2.5 = 6.25$. The new area is 6.25 times the old.

Check: the old area is $10 \times 15 = 150\ \text{cm}^2$ and the new one is $25 \times 37.5 = 937.5\ \text{cm}^2$, and $937.5 \div 150 = 6.25$.

</details>

8\. (Reviews [measurement and unit conversion](../../01-elementary/15-measurement-and-unit-conversion.md).) A download runs at a steady 40 Mbit/s (megabits per second), so the data downloaded is proportional to the time. A byte is 8 bits. (a) Write the equation for the megabytes $y$ downloaded in $x$ seconds. (b) How long does a 3 GB file take, where 1 GB is 1000 MB?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Convert the rate to megabytes per second, with bits cancelling:

$$
40\ \frac{\text{Mbit}}{\text{s}} \times \frac{1\ \text{MB}}{8\ \text{Mbit}} = 5\ \frac{\text{MB}}{\text{s}}.
$$

So $k = 5$ MB per second, and $y = 5x$.

(b) The file is 3000 MB. Solve $5x = 3000$: $x = 600$ seconds, which is 10 minutes.

Check: in 10 minutes, $600 \times 40 = 24{,}000$ megabits arrive, and $24{,}000 \div 8 = 3000$ MB. Forgetting the factor of 8 would give 75 seconds, a common slip.

</details>

## Where this shows up

- The constant $k$ is the slope of the line $y = kx$ ([slope and linear equations](../05-linear-relationships-and-functions/02-slope-and-linear-equations.md)), and the [percents](03-percents.md) lesson writes $\frac{\text{part}}{\text{whole}} = \frac{x}{100}$ as a proportion. Scale drawings lead to similar shapes in transformations, congruence and similarity<!-- link: ../06-geometry/05-transformations-congruence-similarity.md -->.
- In economics, a cost that is the same for every unit makes total cost proportional to output, and a fixed cost makes it linear but not proportional, like the taxi's base fare (production and cost functions<!-- link: ../../07-economics-math/03-firms-and-consumers/02-production-and-cost-functions.md -->).
- An algorithm that does the same amount of work per item runs in time roughly proportional to the size of its input, so doubling the input about doubles the time. Asymptotic notation<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md --> makes "roughly" precise.
