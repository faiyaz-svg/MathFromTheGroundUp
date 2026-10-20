# Geometry and proof

Your first full course in proof: postulates, two-column and paragraph proofs, congruence and similarity, and geometry done with coordinates.

1. [Definitions, postulates and proof](01-definitions-postulates-and-proof.md)
2. [Congruence and triangle proofs](02-congruence-and-triangle-proofs.md)
3. [Similarity](03-similarity.md)
4. [Coordinate geometry and circles](04-coordinate-geometry-and-circles.md)
5. [Conic sections](05-conic-sections.md) (optional)

## Cheat sheet

### Definitions, postulates and proof

Undefined terms (point, line, plane) are described, not defined. Postulates are accepted without proof. Theorems are proved from definitions, postulates and earlier theorems.

| Reason | Statement |
|---|---|
| Segment addition | $B$ between $A$ and $C$ gives $AB + BC = AC$ |
| Angle addition | ray $EC$ inside $\angle AEB$ gives $\angle AEC + \angle CEB = \angle AEB$ |
| Linear pair | a linear pair adds to $180^\circ$ |
| Corresponding angles | parallel lines: equal; equal corresponding angles: parallel |
| Properties of equality | reflexive, symmetric, transitive, substitution, add, subtract, multiply, divide |

- Conditional "if $P$, then $Q$": $P$ is the hypothesis, $Q$ is the conclusion. The converse "if $Q$, then $P$" can be false. The contrapositive "if not $Q$, then not $P$" is true exactly when the original is.
- A proof is Given, Prove, then numbered statements with a reason each: Given, a definition, a postulate or an earlier theorem. Write it first in two columns, then as a paragraph.
- Plan by working backward from the Prove and forward from the Given until they meet. Mark the figure first.
- A counterexample (hypothesis true, conclusion false) disproves a claim. Examples never prove it.
- From a figure you may read order (between, inside), never sizes (right angle, equal sides, parallel).

Main mistakes:

- Proving the converse instead of the statement.
- Circular reasoning: using the claim as a step.
- Reading sizes from the drawing.
- A step with no reason, or the reason "obvious".

### Congruence and triangle proofs

| Test | Needs |
|---|---|
| SSS | three sides |
| SAS | two sides and the angle between them |
| ASA | two angles and the side between them |
| AAS | two angles and a side not between them (theorem, from ASA) |
| HL | right triangles: hypotenuse and a leg (theorem, from Pythagoras and SSS) |

SSA and AAA do not prove congruence. CPCTC (corresponding parts of congruent triangles are congruent) comes after the congruence is proved.

Method: mark the figure, find two triangles containing the parts you want, list three equal pairs (Given, shared side, vertical angles, parallel-line angles, midpoints, bisectors), name the test with the letters in matching order, then use CPCTC. Redraw overlapping triangles apart.

| Theorem | Statement |
|---|---|
| isosceles triangle | $AB = AC$ gives $\angle B = \angle C$ (draw the bisector of $\angle A$, SAS) |
| converse | $\angle B = \angle C$ gives $AB = AC$ (same bisector, AAS) |
| equilateral | three equal sides if and only if three equal angles, each $60^\circ$ |
| perpendicular bisector | $P$ is on the perpendicular bisector of $AB$ if and only if $PA = PB$ |
| angle bisector | $P$ is on the bisector of an angle if and only if it is equally far from the two sides (HL for the converse) |

In an isosceles triangle, the bisector of the vertex angle is also the median and the altitude to the base.

Main mistakes:

- Citing SSA, or SAS when the angle is not between the sides.
- Writing the congruence with the letters in the wrong order.
- Using CPCTC to prove the triangles congruent.

### Similarity

$\triangle ABC \sim \triangle DEF$ means equal angles and $\frac{AB}{DE} = \frac{BC}{EF} = \frac{CA}{FD} = k$.

| Test | Needs |
|---|---|
| AA | two pairs of equal angles |
| SAS similarity | one equal angle and the sides including it in proportion |
| SSS similarity | all three pairs of sides in proportion |

- Triangle proportionality: $DE \parallel BC$ gives $\frac{AD}{DB} = \frac{AE}{EC}$ and $\frac{AD}{AB} = \frac{DE}{BC}$. The converse proves lines parallel.
- Midsegment: joins two midpoints, is parallel to the third side and half as long.
- Altitude $h$ to the hypotenuse $c = p + q$ of a right triangle with legs $a$, $b$: $h^2 = pq$, $b^2 = pc$, $a^2 = qc$. Adding the leg equations gives $a^2 + b^2 = c^2$.
- Similar figures with scale factor $k$: lengths $\times k$, areas $\times k^2$.
- Indirect measurement: find an AA pair, match vertices, write heights over bases on both sides, solve, check the ratio inside one triangle.

Main mistakes:

- Matching sides in the wrong order.
- Writing $\frac{AD}{DB} = \frac{DE}{BC}$ (part to part against part to whole).
- Testing two out of three ratios, or adding the same amount to each side.

### Coordinate geometry and circles

| Formula | For $(x_1, y_1)$ and $(x_2, y_2)$ |
|---|---|
| distance | $\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ |
| midpoint | $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$ |
| slope | $\frac{y_2 - y_1}{x_2 - x_1}$; parallel: equal; perpendicular: product $-1$ |
| circle | $(x - h)^2 + (y - k)^2 = r^2$, centre $(h, k)$ |

- Coordinate proof: put a vertex at the origin and a side on the $x$-axis, name the other coordinates with letters (use $2a$, $2b$ near midpoints), compute, compare. Numbers prove one figure only.
- Proved: diagonals of a parallelogram bisect each other (both midpoints are $\left(\frac{a + b}{2}, \frac{c}{2}\right)$); the midpoint of a right triangle's hypotenuse is equally far from all three vertices; diagonals of a rectangle are equal.
- Completing the square: divide by the common coefficient, group $x$ and $y$ terms, add the squares of the halves to both sides, read the centre (opposite signs) and radius. Right side positive: circle. Zero: a point. Negative: no graph.
- A tangent is perpendicular to the radius at the point of contact. Tangent at $(x_0, y_0)$: $(x_0 - h)(x - h) + (y_0 - k)(y - k) = r^2$.
- Line and circle: substitute, solve the quadratic. Two roots: secant. One (discriminant 0): tangent. None: miss.

Main mistakes:

- Reading the centre of $(x + 2)^2 + \ldots$ as $(2, \ldots)$.
- Adding squares on the left only, or not dividing out a leading coefficient.
- Using the slope test with a vertical line.
- $\sqrt{a^2 + b^2} = a + b$.

### Conic sections (optional)

| Conic | Definition | Standard equation | Key facts |
|---|---|---|---|
| parabola | equally far from focus and directrix | $x^2 = 4py$ or $y^2 = 4px$ | focus $(0, p)$ or $(p, 0)$; directrix $y = -p$ or $x = -p$ |
| ellipse | distances to two foci add to $2a$ | $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, $a > b$ | $c^2 = a^2 - b^2$, foci $(\pm c, 0)$, vertices $(\pm a, 0)$ |
| hyperbola | distances to two foci differ by $2a$ | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$ | $c^2 = a^2 + b^2$, asymptotes $y = \pm\frac{b}{a}x$ |

- Slices of a double cone: horizontal gives a circle, tilted an ellipse, parallel to a side a parabola, steep a hyperbola.
- Reading an equation: one squared variable is a parabola; two squares with the same sign an ellipse; opposite signs a hyperbola. Divide so the right side is 1. For an ellipse, $a^2$ is the larger denominator; for a hyperbola, the one under the positive term.
- Centre at $(h, k)$: replace $x$ by $x - h$ and $y$ by $y - k$ after completing the square.
- A ray parallel to a parabola's axis reflects through the focus (dishes, headlights).

Main mistakes:

- Using $c^2 = a^2 - b^2$ for a hyperbola, or $a^2 + b^2$ for an ellipse.
- Reading the number in $y^2 = 12x$ as $p$ (it is $4p$).
- Putting $a$ on the shorter axis of an ellipse.
