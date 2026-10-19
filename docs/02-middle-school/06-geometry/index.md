# Geometry

Angles, triangles and polygons, area and volume, the Pythagorean theorem, and moving and scaling shapes, with a proof for each main fact.

1. [Angles and triangles](01-angles-and-triangles.md)
2. [Area and circles](02-area-and-circles.md)
3. [Volume and surface area](03-volume-and-surface-area.md)
4. [The Pythagorean theorem](04-pythagorean-theorem.md)
5. [Transformations, congruence and similarity](05-transformations-congruence-similarity.md)

## Cheat sheet

### Angles and triangles

| Fact | Rule |
|---|---|
| complementary, supplementary | add to $90^\circ$, add to $180^\circ$ |
| linear pair, angles around a point | add to $180^\circ$, add to $360^\circ$ |
| vertical angles | equal |
| parallel lines: corresponding, alternate interior | equal |
| parallel lines: co-interior | add to $180^\circ$ |
| triangle angle sum | $180^\circ$ |
| exterior angle of a triangle | the sum of the two remote interior angles |
| interior angles of an $n$-gon | $(n - 2) \times 180^\circ$ |
| exterior angles of a convex polygon | $360^\circ$ |
| each angle of a regular $n$-gon | exterior $360^\circ \div n$, interior $180^\circ$ minus that |

- Triangle inequality: three lengths form a triangle exactly when the two shorter ones add to more than the longest. Given sides 5 and 8, the third side is between 3 and 13.
- Isosceles triangles have equal base angles, and the longest side of a triangle is opposite its largest angle.
- Proofs: vertical angles are both "$180^\circ$ minus the angle between them"; the triangle sum draws a line through one vertex parallel to the opposite side.
- A transversal of parallel lines makes only two sizes of angle, one acute and one obtuse, adding to $180^\circ$.

Main mistakes:

- Setting co-interior angles equal. They add to $180^\circ$.
- Using parallel-line facts on lines that aren't marked parallel.
- Writing $n \times 180^\circ$ for the interior sum. A square's angles add to $360^\circ$.
- Testing the triangle inequality on the wrong pair: 2, 3, 10 fails because $2 + 3 < 10$.

### Area and circles

| Shape | Area | Perimeter or length |
|---|---|---|
| parallelogram | $bh$ | add the sides |
| triangle | $\frac{1}{2}bh$ | add the sides |
| trapezoid | $\frac{1}{2}(b_1 + b_2)h$ | add the sides |
| circle | $\pi r^2$ | $C = 2\pi r = \pi d$ |
| sector with angle $\theta$ | $\frac{\theta}{360} \times \pi r^2$ | arc $\frac{\theta}{360} \times 2\pi r$, plus $2r$ for the perimeter |

- The height is perpendicular to the base. Each formula comes from cutting and rearranging into a rectangle or parallelogram; the circle's from thin sectors laid into a near-parallelogram $\pi r$ long and $r$ tall.
- $\pi = \frac{C}{d} \approx 3.14159$, irrational. Keep $\pi$ as a symbol for exact answers and round once at the end.
- Composite shapes: add pieces, or subtract cut-outs from an outer shape. Check against the rectangle around it.
- Estimates: a circle's area is a bit more than $3r^2$, and it fills about 79% of the square around it.

Main mistakes:

- Using the diameter as the radius.
- Computing $(\pi r)^2$ instead of $\pi r^2$.
- Mixing up circumference (cm) and area ($\text{cm}^2$).
- Forgetting the two radii in a sector's perimeter, or counting inside edges in a composite perimeter.

### Volume and surface area

| Solid | Volume | Surface area |
|---|---|---|
| prism | $Bh$ | $2B$ plus the lateral faces |
| box | $lwh$ | $2(lw + lh + wh)$ |
| cylinder | $\pi r^2 h$ | $2\pi r^2 + 2\pi rh$ |
| pyramid | $\frac{1}{3}Bh$ | $B$ plus the triangles |
| cone | $\frac{1}{3}\pi r^2 h$ | $\pi r^2 + \pi r\ell$ |
| sphere | $\frac{4}{3}\pi r^3$ | $4\pi r^2$ |

- $B$ is the base area and $h$ the perpendicular height; $\ell$ is a cone's slant height, $\sqrt{r^2 + h^2}$.
- A cube splits into three identical pyramids, which is why pyramids and cones are a third.
- $1\ \text{mL} = 1\ \text{cm}^3$, $1\ \text{L} = 1000\ \text{cm}^3$, $1\ \text{m}^3 = 1000\ \text{L}$.
- Scaling lengths by $k$ multiplies areas by $k^2$ and volumes by $k^3$.
- Cone, hemisphere and cylinder with radius $r$ and height $r$: volumes in the ratio $1 : 2 : 3$.

Main mistakes:

- Using the slant height in a volume formula.
- Mixing units: put every length in the same unit first.
- Doubling the volume when every length doubles. It grows 8 times.

### The Pythagorean theorem

In a right triangle with legs $a$ and $b$ and hypotenuse $c$ (opposite the right angle, the longest side), $a^2 + b^2 = c^2$.

| Task | Method | Example |
|---|---|---|
| hypotenuse | $c = \sqrt{a^2 + b^2}$ | legs 9, 12: $c = 15$ |
| a leg | $b = \sqrt{c^2 - a^2}$ | ladder 6 m, foot 1.5 m out: $\sqrt{33.75} \approx 5.81$ m |
| right angle? | compare $a^2 + b^2$ with $c^2$ (longest side) | 7, 24, 25: $49 + 576 = 625$, right |
| distance | $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ | $(-3, 2)$ to $(5, -4)$: 10 |
| box diagonal | $\sqrt{l^2 + w^2 + h^2}$ | 80, 60, 70 cm: about 122.1 cm |

- Proof: a square of side $a + b$ holds four copies of the triangle and either a tilted square $c^2$ or the two squares $a^2$ and $b^2$.
- If $a^2 + b^2 > c^2$ the triangle is acute; if less, obtuse.
- Triples: 3, 4, 5; 5, 12, 13; 8, 15, 17; 7, 24, 25; 20, 21, 29, and their multiples. A square's diagonal is $s\sqrt{2}$.

Main mistakes:

- Using it on a triangle with no right angle.
- Adding the squares when the hypotenuse is given. Subtract to find a leg.
- Writing $\sqrt{a^2 + b^2} = a + b$: legs 3 and 4 give 5, not 7.
- Forgetting the final square root.

### Transformations, congruence and similarity

| Transformation | Rule |
|---|---|
| translation by $(a, b)$ | $(x, y) \to (x + a, y + b)$ |
| reflection in the $x$-axis, $y$-axis, line $y = x$ | $(x, -y)$, $(-x, y)$, $(y, x)$ |
| rotation $90^\circ$ counterclockwise, $180^\circ$, $90^\circ$ clockwise | $(-y, x)$, $(-x, -y)$, $(y, -x)$ |
| dilation, scale factor $k$, centre the origin | $(kx, ky)$ |

- Rigid motions (translations, reflections, rotations) keep lengths and angles. Dilations keep angles and multiply lengths by $k$.
- Congruent: rigid motions carry one figure onto the other (tests SSS, SAS, ASA). Similar: rigid motions and a dilation (tests AA, SSS similarity).
- $\triangle ABC \sim \triangle DEF$ matches $A$ with $D$, $B$ with $E$, $C$ with $F$.
- Similar-triangle problems: show AA, match vertices, find $k$ or set up a proportion with the same triangle on top, solve, check a ratio within each triangle.
- Scale factor $k$: lengths times $k$, areas times $k^2$, volumes times $k^3$.

Main mistakes:

- Rotating the wrong way. Test the rule on $(1, 0)$.
- Using a piece of a side in nested triangles ($DB$ instead of $AB$).
- Scaling an area by $k$ instead of $k^2$: a map at $1:25{,}000$ scales areas by $625{,}000{,}000$.
- Writing the letters of a similarity statement in the wrong order.
