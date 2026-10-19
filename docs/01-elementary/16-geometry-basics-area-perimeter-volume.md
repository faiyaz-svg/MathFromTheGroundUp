# Geometry basics: area, perimeter and volume

After this lesson you can name the basic shapes and angles, find the perimeter of a polygon, find the area of a rectangle, square, triangle or parallelogram and the volume of a rectangular box, and give each answer in the right units.

Before this: [multiplication and times tables](03-multiplication-and-times-tables.md) and [measurement and unit conversion](15-measurement-and-unit-conversion.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A rectangle is 8 cm long and 5 cm wide. Find its perimeter and its area.
2. A triangle has a base of 10 m and a height of 6 m. Find its area.
3. A box is 20 cm long, 10 cm wide and 15 cm tall. Find its volume in cubic centimetres and in litres.

<details class="solution" markdown>
<summary>Answers</summary>

1. The perimeter is $8 + 5 + 8 + 5 = 26$ cm, and the area is $8 \times 5 = 40\ \text{cm}^2$.
2. Half of base times height: $\frac{1}{2} \times 10 \times 6 = 30\ \text{m}^2$.
3. Length times width times height: $20 \times 10 \times 15 = 3{,}000\ \text{cm}^3$, which is 3 L, since $1\ \text{L} = 1000\ \text{cm}^3$.

</details>

## The idea

You are redoing a bedroom floor that is 4 m long and 3 m wide, and two questions come up at the hardware store. How much baseboard trim goes around the edge of the room? And how much flooring covers it?

The trim runs along the four walls, so you add their lengths: $4 + 3 + 4 + 3 = 14$ m. That is the perimeter. It is a length, measured in metres.

The flooring covers the surface. Picture the floor divided into squares 1 m on each side. There are 3 rows of 4 squares:

$$
\begin{array}{|c|c|c|c|}
\hline
1 & 2 & 3 & 4 \\
\hline
5 & 6 & 7 & 8 \\
\hline
9 & 10 & 11 & 12 \\
\hline
\end{array}
$$

That is $3 \times 4 = 12$ squares, so the room needs 12 square metres of flooring. This is the area. It counts squares instead of lengths, and its unit is the square metre, $\text{m}^2$.

So one room has a perimeter of 14 m and an area of $12\ \text{m}^2$: two different numbers with different units, and knowing one doesn't tell you the other ([Edge cases](#edge-cases-and-common-mistakes) shows why). A third measure, volume, counts cubes instead of squares, such as how much a box holds.

## Definitions

### Points, lines and angles

In geometry, capital letters name points. These four objects are the starting point for everything else:

| Object | Written | What it is |
|---|---|---|
| **point** | $P$ | an exact location, with no length, width or thickness |
| **line** | $\overleftrightarrow{PQ}$ | a straight path with no thickness that goes on forever in both directions; through two points there is exactly one |
| **line segment** | $\overline{PQ}$ | the part of a line between two endpoints, here $P$ and $Q$; its length is the distance between them |
| **ray** | $\overrightarrow{PQ}$ | the part of a line that starts at an endpoint $P$ and goes on forever through $Q$, like a beam of light |

An **angle** is a pair of rays with the same endpoint, called the **vertex** of the angle. The angle made by the rays $\overrightarrow{QP}$ and $\overrightarrow{QR}$ is written $\angle PQR$, with the vertex in the middle. Its size, how far one ray is turned from the other, is measured in **degrees**: a full turn is $360^\circ$, so one degree is $\frac{1}{360}$ of a full turn.

| Angle | Size | Example |
|---|---|---|
| **acute angle** | less than $90^\circ$ | the tip of a slice of pizza |
| **right angle** | exactly $90^\circ$ | the corner of a sheet of paper |
| **obtuse angle** | more than $90^\circ$ and less than $180^\circ$ | an open laptop tilted back |
| **straight angle** | exactly $180^\circ$ | two rays pointing in opposite directions, which together make a line |

Drawings mark a right angle with a small square in its corner. Two lines that meet at a right angle are **perpendicular**, and two lines in the same flat surface that never meet are **parallel**.

### Polygons

A **polygon** is a closed flat shape made of straight line segments, called its **sides**, that meet only at their endpoints. Each corner where two sides meet is a vertex (the plural is vertices). A circle is not a polygon, because it has no straight sides, and neither is a shape with a gap in its boundary.

| Sides | Name | Example |
|---|---|---|
| 3 | triangle | a yield sign |
| 4 | quadrilateral | a sheet of paper |
| 5 | pentagon | home plate on a baseball field |
| 6 | hexagon | one cell of a honeycomb |
| 8 | octagon | a stop sign |

A **regular polygon** has all its sides the same length and all its angles the same size. A stop sign is a regular octagon.

Three kinds of quadrilateral come up all the time. A **rectangle** has four right angles, and its opposite sides are equal and parallel. A **square** is a rectangle whose four sides are all the same length. A **parallelogram** has two pairs of parallel sides; it looks like a rectangle pushed over sideways. Every square is a rectangle and every rectangle is a parallelogram, but not the other way round.

### Perimeter, area and volume

The **perimeter** of a polygon is the total length of its sides, the distance once around the boundary. It is a length, so its units are cm, m and so on.

The **area** of a flat shape is the number of unit squares that cover it exactly, with no gaps and no overlaps. A unit square is a square whose sides are 1 unit long, so area is measured in square units such as $\text{cm}^2$ (square centimetres) and $\text{m}^2$. Parts of squares count too: two halves make one.

The **volume** of a solid is the number of unit cubes that fill it, again with no gaps and no overlaps. It is measured in cubic units such as $\text{cm}^3$ and $\text{m}^3$. A **rectangular box** is a solid with six rectangular faces, like a shoebox; geometry books call it a rectangular prism.

### Base and height

The area of a triangle or parallelogram uses two measurements. The **base** is a side you choose to measure from, usually the one drawn at the bottom. The **height** is the perpendicular distance from the base to the opposite vertex of a triangle, or to the opposite side of a parallelogram. In plain words, the height is how tall the shape stands above its base, measured straight up at a right angle to it, not along a slanted side.

## How to do it

1. Decide what the question asks for: a distance around (perimeter), a surface covered (area), or a space filled (volume). The units tell you which: cm for perimeter, $\text{cm}^2$ for area, $\text{cm}^3$ for volume.
2. Put every length in the same unit, converting first if you need to ([measurement and unit conversion](15-measurement-and-unit-conversion.md)).
3. Use the formula for the shape, from the table below. For a shape made of pieces, split it into rectangles and triangles and add the pieces.
4. Write the answer with its units.
5. Check: estimate, count squares on a sketch, or compare with a simpler shape.

| Shape | Perimeter | Area or volume |
|---|---|---|
| rectangle, length $l$, width $w$ | $2l + 2w$ | $A = lw$ |
| square, side $s$ | $4s$ | $A = s^2$ |
| triangle, base $b$, height $h$ | add the three sides | $A = \frac{1}{2}bh$ |
| parallelogram, base $b$, height $h$ | add the four sides | $A = bh$ |
| rectangular box, length $l$, width $w$, height $h$ | | $V = lwh$ |

Here $A$ is the area and $V$ the volume, and letters written side by side are multiplied, so $lw$ means $l \times w$.

### Why the formulas work

A rectangle $l$ units long and $w$ units wide holds $w$ rows of $l$ unit squares, which is $l \times w$ squares in all, as in the bedroom. The same holds when the lengths aren't whole numbers. A rectangle 2.5 m by 2 m has 2 rows, each with 2 whole squares and a half square, so its area is $2 \times 2.5 = 5\ \text{m}^2$. A square is a rectangle with $l = w = s$, so its area is $s \times s = s^2$. That is where the name "$s$ squared" for a second power comes from ([powers of ten](14-powers-of-ten.md#definitions)).

For a parallelogram, cut and rearrange. Picture one with a horizontal base $b$ and height $h$, leaning to the right. Cut straight down from its top left corner to the base, at a right angle, which cuts off a right triangle on the left. Slide that triangle to the right end, where its slanted side fits exactly against the parallelogram's right side. The pieces now form a rectangle $b$ long and $h$ tall, and nothing was added or thrown away, so the area of the parallelogram is $bh$.

For a triangle, take two copies of it and turn one upside down. The two fit together into a parallelogram with the same base and height, so one triangle is half of it: $A = \frac{1}{2}bh$. Both arguments get a full treatment, with pictures, in area and circles<!-- link: ../02-middle-school/06-geometry/02-area-and-circles.md -->.

For a box, a single layer of unit cubes on the bottom has $l \times w$ cubes, and there are $h$ layers stacked up, so the box holds $l \times w \times h$ cubes. A cube with edges of length $s$ has volume $s^3$, "$s$ cubed".

### Shapes on a grid

The **coordinate plane** is a flat grid with a horizontal number line, the $x$-axis, and a vertical one, the $y$-axis, which cross at their zeros. The crossing point is the **origin**. Each point has **coordinates** $(x, y)$, written in that order: start at the origin, go $x$ units right, then $y$ units up. The point $(3, 2)$ is 3 right and 2 up. In this lesson every coordinate is 0 or positive, so the points lie in the top right part of the plane, called the **first quadrant**; the whole plane comes in [the coordinate plane](../02-middle-school/05-linear-relationships-and-functions/01-coordinate-plane.md).

On the grid, the length of a horizontal or vertical segment is a subtraction. From $(1, 1)$ to $(5, 1)$ the $x$-coordinate goes from 1 to 5, so the segment is $5 - 1 = 4$ units long. The rectangle with corners $(1, 1)$, $(5, 1)$, $(5, 4)$ and $(1, 4)$ is therefore 4 units wide and $4 - 1 = 3$ units tall, with an area of 12 square units: the bedroom floor, drawn on a grid.

## Worked examples

<div class="example" markdown>

### Example 1: fencing and soil for a garden

A rectangular garden is 6.5 m long and 4 m wide. How much fence goes around it, and how much ground does it cover?

Step 1: the fence runs around the edge, so it is the perimeter. The ground covered is the area.

Step 2: both lengths are in metres already.

Step 3: the perimeter of a rectangle is $2l + 2w$, and its area is $lw$:

$$
\begin{aligned}
2l + 2w &= 2 \times 6.5 + 2 \times 4 = 13 + 8 = 21, \\
lw &= 6.5 \times 4 = 26.
\end{aligned}
$$

Step 4: the fence is 21 m long, and the garden covers $26\ \text{m}^2$.

Step 5: check the area by counting squares. The garden has 4 rows, and each row has 6 whole squares and a half square, so it holds $4 \times 6 = 24$ whole squares and 4 halves, which make 2 more: $24 + 2 = 26$.

</div>

<div class="example" markdown>

### Example 2: a parallelogram and a slanted side

A parallelogram has a base of 8 cm, slanted sides of 5 cm, and a height of 4 cm. Find its perimeter and its area, and the area of the triangle you get by cutting it along a diagonal.

The perimeter uses the sides: $8 + 5 + 8 + 5 = 26$ cm. The area uses the base and the height: $A = bh = 8 \times 4 = 32\ \text{cm}^2$.

A diagonal cuts the parallelogram into two identical triangles, each with base 8 cm and height 4 cm, so each has area $\frac{1}{2} \times 8 \times 4 = 16\ \text{cm}^2$. Check: $16 + 16 = 32$.

<div class="warning" markdown>

Watch out: the slanted side is not the height. Using it gives $8 \times 5 = 40\ \text{cm}^2$, which is too big. The height is the straight-up distance, and a slanted path from the base to the top is always longer than the straight one. A parallelogram's side equals its height only when the parallelogram is a rectangle.

</div>

</div>

<div class="example" markdown>

### Example 3: the volume of a moving box

A moving box is 60 cm long, 40 cm wide and 50 cm tall. Find its volume in cubic centimetres, litres and cubic metres.

Use $V = lwh$: $60 \times 40 \times 50 = 120{,}000\ \text{cm}^3$. Since $1\ \text{L} = 1000\ \text{cm}^3$, that is 120 L. Since $1\ \text{m}^3 = 1{,}000{,}000\ \text{cm}^3$, it is also $0.12\ \text{m}^3$.

Check in metres from the start: $0.6 \times 0.4 \times 0.5 = 0.12\ \text{m}^3$.

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the same perimeter can enclose different areas. Every rectangle below has a perimeter of 20 cm, since its length and width add to 10:

| Length | Width | Perimeter | Area |
|---|---|---|---|
| 9 cm | 1 cm | 20 cm | $9\ \text{cm}^2$ |
| 8 cm | 2 cm | 20 cm | $16\ \text{cm}^2$ |
| 7 cm | 3 cm | 20 cm | $21\ \text{cm}^2$ |
| 6 cm | 4 cm | 20 cm | $24\ \text{cm}^2$ |
| 5 cm | 5 cm | 20 cm | $25\ \text{cm}^2$ |

The long thin rectangle has the least area and the square has the most. In fact, of all the rectangles with a given perimeter, the square always encloses the most; optimization<!-- link: ../05-university-core/03-applications-of-derivatives/05-optimization.md --> proves it with calculus. It works the other way too: rectangles with an area of $12\ \text{cm}^2$ can be 1 by 12, 2 by 6 or 3 by 4 (in cm), with perimeters of 26, 16 and 14 cm. Neither number tells you the other; each needs the side lengths and its own formula.

</div>

<div class="warning" markdown>

Watch out for the units. Perimeter is in cm, area in $\text{cm}^2$, volume in $\text{cm}^3$. Writing "the area is 40 cm" mixes up a length and an area. Mixed units give wrong numbers too: a rug 2 m by 50 cm is not $2 \times 50 = 100$ of anything. Convert first, $2 \times 0.5 = 1\ \text{m}^2$, or $200 \times 50 = 10{,}000\ \text{cm}^2$, which is the same area.

</div>

<div class="warning" markdown>

Watch out: the perimeter of a rectangle needs all four sides. Adding the length and the width once goes only halfway around, so for an 8 cm by 5 cm rectangle, 13 cm is half of the right answer, 26 cm.

</div>

In a triangle with an obtuse angle at the base, the height falls outside the triangle. If the top vertex sits out past the end of the base, the height is measured from that vertex straight down to the line of the base, extended past its end. The formula $\frac{1}{2}bh$ still holds, with that height.

Scaling changes area and volume more than length. Double each side of a rectangle and its area becomes $2 \times 2 = 4$ times as big; double each edge of a box and its volume becomes $2 \times 2 \times 2 = 8$ times as big. This is the same squaring and cubing that makes $1\ \text{m}^2 = 10{,}000\ \text{cm}^2$ in [measurement and unit conversion](15-measurement-and-unit-conversion.md#area-and-volume-units).

## Tricks and shortcuts

For the perimeter of a rectangle, add the length and the width, then double: $2(l + w)$. For an 8 by 5 rectangle, $8 + 5 = 13$ and $2 \times 13 = 26$.

For a shape with only right-angle corners, such as an L-shaped room, there are two ways to get the area: split it into rectangles and add, or take the rectangle around it and subtract the missing piece. Doing both is a built-in check. Practice problem 3 has one.

To check an area quickly, sketch the shape on squared paper and count: whole squares, plus halves paired up into wholes.

## Practice

### Warm-up

1\. (a) Say whether each angle is acute, right, obtuse or straight: $35^\circ$, $90^\circ$, $120^\circ$, $180^\circ$. (b) Name the polygons with 5, 6 and 8 sides.

<details class="solution" markdown>
<summary>Solution</summary>

(a) An angle of $35^\circ$ is less than $90^\circ$, so it is acute. Exactly $90^\circ$ is a right angle. The angle of $120^\circ$ is between $90^\circ$ and $180^\circ$, so it is obtuse, and $180^\circ$ is a straight angle.

(b) Pentagon, hexagon and octagon.

</details>

2\. A rectangle is 7 m long and 2.5 m wide. Find its perimeter and its area.

<details class="solution" markdown>
<summary>Solution</summary>

Perimeter: $2(7 + 2.5) = 2 \times 9.5 = 19$ m. Area: $7 \times 2.5 = 17.5\ \text{m}^2$. The area is not a whole number, and that is fine.

Check: the rectangle has 2 rows of 7 whole squares and a row of 7 half squares, so the area is $14 + 3.5 = 17.5$.

</details>

### Standard

3\. An L-shaped room is a 6 m by 4 m rectangle with a 2 m by 1.5 m rectangle missing from one corner. Find its area and its perimeter.

<details class="solution" markdown>
<summary>Solution</summary>

Area, by subtracting: the full rectangle is $6 \times 4 = 24\ \text{m}^2$ and the missing corner is $2 \times 1.5 = 3\ \text{m}^2$, so the room is $24 - 3 = 21\ \text{m}^2$.

Perimeter: put the missing piece at the top right and walk around from the bottom left corner. The walls are 6 m along the bottom, 2.5 m up the right side, 2 m left into the notch, 1.5 m up, 4 m back along the top and 4 m down the left side:

$$
6 + 2.5 + 2 + 1.5 + 4 + 4 = 20\ \text{m}.
$$

That is the same as the perimeter of the full 6 by 4 rectangle, $2(6 + 4) = 20$ m. The notch moves two walls inward without changing their total length.

Check the area by splitting instead: a bottom strip 6 m by 2.5 m is $15\ \text{m}^2$, and the part above it on the left is 4 m by 1.5 m, which is $6\ \text{m}^2$, so the total is $15 + 6 = 21\ \text{m}^2$.

</details>

4\. On the coordinate plane, (a) find the perimeter and area of the rectangle with corners $(2, 1)$, $(7, 1)$, $(7, 4)$ and $(2, 4)$, and (b) find the area of the triangle with corners $(2, 1)$, $(7, 1)$ and $(2, 4)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The width is $7 - 2 = 5$ units and the height is $4 - 1 = 3$ units. The perimeter is $2(5 + 3) = 16$ units, and the area is $5 \times 3 = 15$ square units.

(b) The triangle has a right angle at $(2, 1)$. Take the bottom side as the base, $7 - 2 = 5$ units, and the left side as the height, $4 - 1 = 3$ units, since the two sides are perpendicular. The area is $\frac{1}{2} \times 5 \times 3 = 7.5$ square units.

Check: the triangle is half of the rectangle from (a), cut along the diagonal from $(7, 1)$ to $(2, 4)$, and half of 15 is 7.5.

</details>

### Challenge

5\. You have 24 m of fence for a rectangular garden, and each side has to be a whole number of metres. List every possible shape. Which gives the most area, and which the least?

<details class="solution" markdown>
<summary>Solution</summary>

The perimeter is $2(l + w) = 24$, so $l + w = 12$. List the pairs, with the length at least as big as the width:

| Length | Width | Area |
|---|---|---|
| 11 m | 1 m | $11\ \text{m}^2$ |
| 10 m | 2 m | $20\ \text{m}^2$ |
| 9 m | 3 m | $27\ \text{m}^2$ |
| 8 m | 4 m | $32\ \text{m}^2$ |
| 7 m | 5 m | $35\ \text{m}^2$ |
| 6 m | 6 m | $36\ \text{m}^2$ |

The 6 m by 6 m square gives the most area, $36\ \text{m}^2$, and the 11 m by 1 m strip gives the least, $11\ \text{m}^2$.

Check: every row uses all the fence, for example $2(7 + 5) = 24$. The areas grow as the shape gets closer to a square, as in the Edge cases table.

</details>

6\. This one reviews [measurement and unit conversion](15-measurement-and-unit-conversion.md). An aquarium is 60 cm long, 30 cm wide and 35 cm tall. (a) Find its volume in cubic centimetres and in litres. (b) You fill it with water to 5 cm below the top. About what mass of water is that?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The volume is $V = 60 \times 30 \times 35 = 63{,}000\ \text{cm}^3$. Since $1\ \text{L} = 1000\ \text{cm}^3$, that is 63 L.

(b) The water is $35 - 5 = 30$ cm deep, so it fills a box 60 cm by 30 cm by 30 cm: $60 \times 30 \times 30 = 54{,}000\ \text{cm}^3$, which is 54 L. A litre of water has a mass of about 1 kg, so the water is about 54 kg.

Check: the empty 5 cm at the top is $60 \times 30 \times 5 = 9{,}000\ \text{cm}^3$, or 9 L, and $54 + 9 = 63$ L, the full volume.

</details>

## Where this shows up

- Middle school geometry continues with angles and triangles<!-- link: ../02-middle-school/06-geometry/01-angles-and-triangles.md -->, area and circles<!-- link: ../02-middle-school/06-geometry/02-area-and-circles.md --> and volume and surface area<!-- link: ../02-middle-school/06-geometry/03-volume-and-surface-area.md -->.
- In calculus, the area under a curve is found by adding up the areas of thin rectangles, each one base times height: Riemann sums and the definite integral<!-- link: ../05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md -->.
- On a supply and demand graph, a firm's revenue (price times quantity) is the area of a rectangle, and consumer surplus is the area of a triangle: surplus and market interventions<!-- link: ../07-economics-math/02-markets/04-surplus-and-market-interventions.md -->.
