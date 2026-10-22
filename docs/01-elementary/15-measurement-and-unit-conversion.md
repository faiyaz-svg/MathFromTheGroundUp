# Measurement and unit conversion

After this lesson you can convert between metric units, change the units of a rate such as km/h to m/s by cancelling units, work with hours, minutes and seconds, convert the imperial units and Fahrenheit temperatures that Canadians still meet, and use units to check an answer.

Before this: [powers of ten](14-powers-of-ten.md) and [multiplying and dividing fractions](11-multiplying-and-dividing-fractions.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Convert 2.4 km to metres, and $3\ \text{m}^2$ to square centimetres.
2. Convert 90 km/h to metres per second.
3. It is 25°C in Toronto. What is that in degrees Fahrenheit?

<details class="solution" markdown>
<summary>Answers</summary>

1. 2,400 m, since 1 km = 1000 m. And $30{,}000\ \text{cm}^2$, since $1\ \text{m}^2 = 100\ \text{cm} \times 100\ \text{cm} = 10{,}000\ \text{cm}^2$.
2. 25 m/s. An hour is 3600 s, so $90 \times 1000 \div 3600 = 25$.
3. 77°F, since $\frac{9}{5} \times 25 + 32 = 45 + 32 = 77$.

</details>

## The idea

A speed limit sign on an Ontario highway says 100, in kilometres per hour. Drive across the border into Michigan and the freeway signs say 70, in miles per hour. Which limit is higher? You can't compare 100 with 70 directly, because they count different units. First you need both speeds in the same unit.

A measurement is a number and a unit together, and the unit is part of its meaning: "100 km/h" is 100 of the unit "kilometre per hour". Changing the unit changes the number but not the speed. A smaller unit needs a bigger number: a metre is a thousandth of a kilometre, so 3 km is 3000 m.

Every conversion in this lesson multiplies by 1. A fraction such as $\frac{1000\ \text{m}}{1\ \text{km}}$ has the same length on top and on the bottom, so it equals 1, and multiplying by it changes the units without changing the amount. Example 2 uses one to settle the Michigan question.

## Definitions

A **unit** is a fixed amount of a quantity that other amounts are measured against, such as the metre for length. A **measurement** is a number times a unit: 3 km means $3 \times (1\ \text{km})$.

Canada uses the **metric system**, whose modern form is the International System of Units (SI). Each kind of quantity has one main unit, and bigger and smaller units are made from it with the prefixes from [powers of ten](14-powers-of-ten.md#metric-prefixes).

| Quantity | What it measures | Main unit | Other common units |
|---|---|---|---|
| Length | distance | metre (m) | km, cm, mm |
| Mass | amount of matter, what everyday speech calls weight | gram (g) | kg, mg, and the tonne (t), which is 1000 kg |
| Capacity | how much a container holds | litre (L) | mL |
| Time | how long something lasts | second (s) | minute (min), hour (h), day |

Volume is the amount of space an object takes up, and **capacity** is the volume a container can hold. Volume is measured in cubic units, such as the cubic centimetre, $\text{cm}^3$, which is the space inside a cube 1 cm on each side. The two kinds of unit match exactly: $1\ \text{mL} = 1\ \text{cm}^3$, so $1\ \text{L} = 1000\ \text{cm}^3$. A litre of water has a mass of about 1 kg.

A **conversion factor** is a fraction whose numerator and denominator are the same amount written in different units, so the fraction equals 1. The fact 1 km = 1000 m gives two of them:

$$
\frac{1000\ \text{m}}{1\ \text{km}} = 1 \qquad \text{and} \qquad \frac{1\ \text{km}}{1000\ \text{m}} = 1.
$$

**Dimensional analysis** (also called the factor-label method) converts units by multiplying by conversion factors and cancelling each unit that appears in both a numerator and a denominator, the way a common factor cancels in a fraction. In plain words, you treat units like numbers that can cancel, and you pick each factor so that the unit you don't want cancels out.

## How to do it

### Metric to metric: move the decimal point

1. Find the factor between the two units from their prefixes: 1 km = 1000 m, 1 m = 100 cm, 1 g = 1000 mg.
2. Going from a bigger unit to a smaller one, multiply by the factor. Going from a smaller unit to a bigger one, divide.
3. Move the decimal point as in [powers of ten](14-powers-of-ten.md#how-to-do-it), then check that the smaller unit has the bigger number.

For example, 450 mg is $450 \div 1000 = 0.45$ g, and 1.8 L is $1.8 \times 1000 = 1{,}800$ mL.

### Other units: multiply by conversion factors

1. Write the quantity with its units. Write a rate as a fraction, so km/h becomes $\frac{\text{km}}{\text{h}}$.
2. For each unit you want to change, write a conversion factor with that unit on the opposite side: a unit in the numerator needs a factor with it in the denominator, and the other way round.
3. Multiply, and cancel each unit that appears both on top and on the bottom.
4. Work out the numbers.
5. Check that the units left are the ones you want, and that the size makes sense.

If a unit you wanted to get rid of is still there at Step 5, or shows up squared, one of the factors from Step 2 is upside down.

### Time

Time units don't go up in powers of ten. A minute is 60 s, an hour is 60 min or 3600 s, and a day is 24 h. Minutes and seconds count in base 60, so a decimal number of hours is not hours and minutes: 1.5 h is 1 h 30 min, because half of 60 minutes is 30. To convert, use conversion factors, or divide by 60 and keep the remainder, as in Practice problem 5 of [long division](07-long-division.md#challenge).

### Imperial units

Canada uses metric units, but the older imperial units are still common for heights, body weights, and anything from the United States. The values in this table are exact definitions, not roundings:

| Unit | Exact value | Rough value |
|---|---|---|
| 1 inch (in) | 2.54 cm | 2.5 cm |
| 1 foot (ft) | 12 in = 30.48 cm | 30 cm |
| 1 yard (yd) | 3 ft = 0.9144 m | 0.9 m |
| 1 mile (mi) | 5280 ft = 1.609344 km | 1.6 km |
| 1 pound (lb) | 0.45359237 kg | 0.45 kg, so 1 kg is about 2.2 lb |

Use the exact value when the answer has to be precise, and the rough value for a quick estimate.

### Temperature

Weather forecasts in the United States give temperatures in degrees Fahrenheit. The conversion is a formula, not a single factor:

$$
\text{Fahrenheit} = \frac{9}{5} \times \text{Celsius} + 32, \qquad \text{Celsius} = \frac{5}{9} \times (\text{Fahrenheit} - 32).
$$

Lengths convert by multiplying because both units start from the same zero: 0 m and 0 ft are the same length. The two temperature scales put their zeros in different places. Water freezes at 0°C, which is 32°F, and boils at 100°C (at sea level), which is 212°F. Between those two points there are 100 Celsius degrees and $212 - 32 = 180$ Fahrenheit degrees, so one Celsius degree is as big as $\frac{180}{100} = \frac{9}{5}$ Fahrenheit degrees. The formula multiplies by $\frac{9}{5}$ to change the size of the degree, then adds 32 to line up the zeros.

Because of the shift, a ratio of temperatures doesn't survive a conversion. Doubling a Celsius temperature does not double the Fahrenheit one: 10°C is 50°F, but 20°C is 68°F, not 100°F.

### Area and volume units

A square 1 m on each side has an area of $1\ \text{m}^2$, one square metre. Each of its sides is 100 cm long, so it holds 100 rows of 100 squares that are 1 cm on each side:

$$
1\ \text{m}^2 = 100\ \text{cm} \times 100\ \text{cm} = 10{,}000\ \text{cm}^2.
$$

Area units scale by the square of the length factor, and volume units by its cube: $1\ \text{m}^3 = 100^3\ \text{cm}^3 = 1{,}000{,}000\ \text{cm}^3$, which is 1000 L. With conversion factors, use the length factor twice for an area and three times for a volume, so that every metre cancels. Area and volume themselves are the subject of [geometry basics](16-geometry-basics-area-perimeter-volume.md).

## Worked examples

<div class="example" markdown>

### Example 1: kilometres per hour to metres per second

Convert 72 km/h to m/s.

Step 1: write the rate as a fraction, $72\ \frac{\text{km}}{\text{h}}$.

Step 2: kilometres are on top, so the first factor needs kilometres on the bottom: $\frac{1000\ \text{m}}{1\ \text{km}}$. Hours are on the bottom, so the second factor needs hours on top: $\frac{1\ \text{h}}{3600\ \text{s}}$.

Step 3: multiply, and cancel the units that appear above and below:

$$
72\ \frac{\cancel{\text{km}}}{\cancel{\text{h}}} \times \frac{1000\ \text{m}}{1\ \cancel{\text{km}}} \times \frac{1\ \cancel{\text{h}}}{3600\ \text{s}} = \frac{72 \times 1000}{3600}\ \frac{\text{m}}{\text{s}}.
$$

Step 4: $72 \times 1000 = 72{,}000$, and $72{,}000 \div 3600 = 20$. So 72 km/h is 20 m/s.

Step 5: the units left are metres on top and seconds below, which is what we wanted. For the size, go back the other way: at 20 m/s, one hour covers $20 \times 3600 = 72{,}000$ m, which is 72 km.

<div class="warning" markdown>

Watch out at Step 2: flipping a factor gives a wrong answer with strange units. With $\frac{1\ \text{km}}{1000\ \text{m}}$ instead, the kilometres no longer cancel, and the result is in $\frac{\text{km}^2}{\text{m} \cdot \text{s}}$, which is not a speed. If the units at the end aren't the ones you want, look for the upside-down factor.

</div>

</div>

<div class="example" markdown>

### Example 2: the Michigan speed limit

Convert 70 mph (miles per hour) to km/h. Only the miles need to change, so one factor is enough, with miles on the bottom:

$$
70\ \frac{\cancel{\text{mi}}}{\text{h}} \times \frac{1.609344\ \text{km}}{1\ \cancel{\text{mi}}} = 112.65408\ \frac{\text{km}}{\text{h}}.
$$

That is about 113 km/h, so the Michigan limit is higher than Ontario's 100 km/h. Check with the rough value: $70 \times 1.6 = 112$.

</div>

<div class="example" markdown>

### Example 3: decimal hours

(a) Write 3 h 40 min in hours. (b) Write 2.35 h in hours and minutes.

(a) Forty minutes is $\frac{40}{60} = \frac{2}{3}$ of an hour, so 3 h 40 min is $3\frac{2}{3}$ h, which is $3.666\ldots$ h, about 3.67 h.

<div class="warning" markdown>

Watch out: 3 h 40 min is not 3.40 h. The 0.40 in 3.40 h means 40 hundredths of an hour, which is $0.4 \times 60 = 24$ minutes. Minutes are sixtieths of an hour, not hundredths.

</div>

(b) Keep the 2 hours and convert the 0.35 h: $0.35 \times 60 = 21$ minutes. So 2.35 h is 2 h 21 min. Check: $\frac{21}{60} = 0.35$.

</div>

<div class="example" markdown>

### Example 4: a Fahrenheit forecast

A forecast for Buffalo says 50°F. What is that in Celsius?

Subtract 32 first, then multiply by $\frac{5}{9}$:

$$
\frac{5}{9} \times (50 - 32) = \frac{5}{9} \times 18 = 10.
$$

So 50°F is 10°C. Check with the other formula: $\frac{9}{5} \times 10 + 32 = 18 + 32 = 50$.

Multiplying 50 by $\frac{5}{9}$ without subtracting 32 gives about 27.8, and 27.8°C is a warm summer day, far from the cool 10°C. The 32 lines up the two zeros, so it can't be skipped.

</div>

<div class="example" markdown>

### Example 5: square feet to square metres

Condo listings in Ontario often give the floor area in square feet. Convert $650\ \text{ft}^2$ to square metres.

Since 1 ft = 0.3048 m, use that factor twice, once for each foot in $\text{ft}^2 = \text{ft} \times \text{ft}$:

$$
650\ \text{ft}^2 \times \frac{0.3048\ \text{m}}{1\ \text{ft}} \times \frac{0.3048\ \text{m}}{1\ \text{ft}} = 650 \times 0.09290304\ \text{m}^2 = 60.38697\ldots\ \text{m}^2.
$$

The condo is about $60.4\ \text{m}^2$. Check with rough values: a foot is about 0.3 m, so a square foot is about $0.3 \times 0.3 = 0.09\ \text{m}^2$, and $650 \times 0.09 = 58.5$, close to 60.4.

Using the factor only once gives $650 \times 0.3048 = 198.12$, and its units are $\text{ft} \cdot \text{m}$, which is neither square feet nor square metres. The units show that a factor is missing.

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the direction. Converting 450 mg to grams, it is tempting to multiply by 1000 and get 450,000 g, which is 450 kg. A gram is the bigger unit, so the number has to get smaller: $450 \div 1000 = 0.45$ g.

</div>

<div class="warning" markdown>

Watch out: a square metre is $10{,}000\ \text{cm}^2$, not $100\ \text{cm}^2$. A square that is 100 cm on each side holds 100 rows of 100 small squares. In the same way, $1\ \text{cm}^2 = 100\ \text{mm}^2$ and $1\ \text{m}^3 = 1{,}000{,}000\ \text{cm}^3$.

</div>

<div class="warning" markdown>

Watch out: convert before you add. A shelf 1.2 m long plus a 35 cm extension is not $1.2 + 35 = 36.2$ of anything. Write 35 cm as 0.35 m, and the total is $1.2 + 0.35 = 1.55$ m.

</div>

A change in temperature converts without the 32. If the temperature rises by 10 Celsius degrees, it rises by $\frac{9}{5} \times 10 = 18$ Fahrenheit degrees, whatever it started at. The 32 lines up the zeros of the scales, and a difference between two temperatures doesn't depend on where zero is. For example, 10°C to 20°C is 50°F to 68°F, a rise of 18.

Mass and capacity are different quantities. A litre of water has a mass of about 1 kg, but a litre of cooking oil is lighter, about 0.92 kg, so "1 L = 1 kg" holds only for water.

## Tricks and shortcuts

To change km/h to m/s, divide by 3.6, and to change m/s to km/h, multiply by 3.6. This is Example 1 in one step, since $\frac{1000}{3600} = \frac{1}{3.6}$. For instance, 90 km/h is $90 \div 3.6 = 25$ m/s.

For weather, a rough Celsius-to-Fahrenheit conversion is "double it and add 30": 25°C gives about 80°F (the exact value is 77°F). To go back, subtract 30 and halve: 50°F gives 10°C. The estimate drifts further off at very hot and very cold temperatures, so use the formula when it matters.

Keep the units on every line of a calculation, and check that the answer comes out in the units the question asks for. A speed must come out in a distance per time. If you divide 3 h by 240 km, you get $0.0125\ \frac{\text{h}}{\text{km}}$, a time per distance, so the division is upside down: the speed is $240 \div 3 = 80$ km/h. The [problem-solving playbook](../00-start-here/problem-solving-playbook.md#check-units-and-size) uses the same check on a download time.

A few everyday sizes help you spot an answer that is far off:

| Unit | Roughly |
|---|---|
| 1 mm | the thickness of a dime |
| 1 cm | the width of a fingernail |
| 1 m | a bit more than the height of a kitchen counter |
| 1 km | the distance you walk in 12 minutes |
| 1 g | the mass of a paper clip |
| 1 kg | the mass of a litre of water |

## Practice

### Warm-up

1\. Convert (a) 3.5 kg to grams, (b) 820 mm to metres, (c) 1.25 L to millilitres and (d) 45 cm to metres.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) 1 kg = 1000 g, and the gram is smaller, so multiply: $3.5 \times 1000 = 3{,}500$ g.
- (b) 1 m = 1000 mm, and the metre is bigger, so divide: $820 \div 1000 = 0.82$ m.
- (c) 1 L = 1000 mL, so multiply: $1.25 \times 1000 = 1{,}250$ mL.
- (d) 1 m = 100 cm, so divide: $45 \div 100 = 0.45$ m.

Check: in each answer the smaller unit has the bigger number. For (b), 0.82 m is a bit under a metre, and 820 mm is a bit under 1000 mm.

</details>

2\. (a) Write 2 h 15 min in minutes, and then in hours. (b) Write 200 min in hours and minutes. (c) Write 0.4 h in minutes.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Two hours are 120 min, so the time is $120 + 15 = 135$ min. In hours, 15 min is $\frac{15}{60} = 0.25$ h, so the time is 2.25 h.

(b) Divide by 60: 200 is 3 sixties with 20 left over, since $3 \times 60 = 180$. So 200 min is 3 h 20 min.

(c) Multiply by 60: $0.4 \times 60 = 24$ min.

Check: $2.25 \times 60 = 135$, and $3 \times 60 + 20 = 200$.

</details>

### Standard

3\. A form asks for your height in centimetres and your weight in kilograms. You know them as 5 ft 9 in and 154 lb. Convert both, to the nearest whole unit.

<details class="solution" markdown>
<summary>Solution</summary>

Height: first change everything to inches, $5 \times 12 + 9 = 69$ in. Then multiply by the exact factor:

$$
69\ \cancel{\text{in}} \times \frac{2.54\ \text{cm}}{1\ \cancel{\text{in}}} = 175.26\ \text{cm},
$$

which is about 175 cm.

Weight: $154 \times 0.45359237 = 69.853\ldots$, so about 70 kg.

Check with rough values: $69 \times 2.5 = 172.5$, close to 175, and $154 \div 2.2 = 70$.

</details>

4\. Square floor tiles are 20 cm on each side, so each one covers $400\ \text{cm}^2$. How many tiles cover a floor of $6\ \text{m}^2$?

<details class="solution" markdown>
<summary>Solution</summary>

Convert the floor to square centimetres. Since $1\ \text{m}^2 = 10{,}000\ \text{cm}^2$, the floor is $6 \times 10{,}000 = 60{,}000\ \text{cm}^2$. Then $60{,}000 \div 400 = 150$ tiles.

Check another way: 20 cm is 0.2 m, so a tile covers $0.2 \times 0.2 = 0.04\ \text{m}^2$, and $6 \div 0.04 = 150$. Using $1\ \text{m}^2 = 100\ \text{cm}^2$ by mistake gives 1.5 tiles for a whole floor, which fails the size check.

</details>

### Challenge

5\. The forecast says 59°F in Buffalo and 14°C in Toronto. (a) Which city will be warmer, and by how many Celsius degrees? (b) A friend converts 59°F by multiplying by $\frac{5}{9}$ and gets about 32.8°C. What went wrong, and how could a size check have caught it?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Convert Buffalo's temperature: $\frac{5}{9} \times (59 - 32) = \frac{5}{9} \times 27 = 15$, so 59°F is 15°C. Buffalo will be warmer by $15 - 14 = 1$ Celsius degree.

(b) The friend skipped subtracting 32, which lines up the zeros of the two scales. The rough rule from [Tricks and shortcuts](#tricks-and-shortcuts) catches it: 59 minus 30, halved, is about 15°C, nowhere near 32.8°C, which would be a heat wave.

Check: $\frac{9}{5} \times 15 + 32 = 27 + 32 = 59$.

</details>

6\. This one reviews [multiplying and dividing decimals](13-multiplying-and-dividing-decimals.md). A marathon is 42.195 km. A runner finishes in 3 h 30 min. Find (a) the average speed in km/h, (b) the average speed in m/s and (c) the average pace, in minutes and seconds per kilometre.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The time is 3.5 h, since 30 min is half an hour. Speed is distance divided by time: $42.195 \div 3.5 = 12.0557\ldots$, about 12.06 km/h.

(b) Divide by 3.6: $12.0557 \div 3.6 = 3.3488\ldots$, about 3.35 m/s. With factors instead, $42{,}195\ \text{m} \div 12{,}600\ \text{s}$ gives the same, since 3.5 h is $3.5 \times 3600 = 12{,}600$ s.

(c) Pace is time divided by distance, the units the other way up: $210\ \text{min} \div 42.195\ \text{km} = 4.9769\ldots$ minutes per kilometre. The 0.9769 min is $0.9769 \times 60 = 58.6$ s, so the pace is about 4 min 59 s per km.

Check: at 12.06 km/h, 3.5 h covers $12.06 \times 3.5 = 42.21$ km, close to 42.195 (the small gap is from rounding). And a pace of 5 min per km over 42.195 km takes about $5 \times 42.195 = 211$ min, just over the actual 210.

</details>

## Where this shows up

- A rate such as km/h is a ratio of two quantities with different units, the subject of [ratios and unit rates](../02-middle-school/02-ratios-rates-percents/01-ratios-and-unit-rates.md). Grocery shelf labels give prices per 100 g, a rate in dollars per gram, and comparing them is the subject of [unit price and comparison shopping](../08-financial-math/01-everyday-money/02-unit-price-and-comparison-shopping.md).
- In computing, data sizes and speeds mix bits, bytes and prefixes, and dimensional analysis keeps them straight: a byte is 8 bits, so 100 Mbit/s is 12.5 MB/s.
- An elasticity in economics is a ratio of two percent changes, so its units cancel completely. That is why it can compare markets measured in litres, kilograms or hours ([elasticity](../07-economics-math/02-markets/05-elasticity.md)).
