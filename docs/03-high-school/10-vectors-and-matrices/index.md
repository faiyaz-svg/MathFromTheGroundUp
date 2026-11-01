# Vectors and matrices

Quantities with a direction, and tables of numbers that combine and transform them: the bridge from high school algebra to linear algebra.

1. [Vectors in the plane](01-vectors-in-the-plane.md)
2. [Matrix basics](02-matrix-basics.md)
3. [Vectors in 3D and the cross product](03-vectors-in-3d-and-the-cross-product.md)
4. [Lines and planes in 3D](04-lines-and-planes-in-3d.md)

## Cheat sheet

### Vectors in the plane

A vector is a move: $\mathbf{v} = (a, b)$ means $a$ right and $b$ up. Where the arrow is drawn doesn't matter, only its components. The vector from $P = (x_1, y_1)$ to $Q = (x_2, y_2)$ is "end minus start", $(x_2 - x_1,\; y_2 - y_1)$.

| Operation | Formula | Picture or example |
|---|---|---|
| sum | $(u_1 + v_1,\; u_2 + v_2)$ | tip to tail, or the diagonal of a parallelogram |
| difference | $\mathbf{u} - \mathbf{v} = (u_1 - v_1,\; u_2 - v_2)$ | the arrow from the tip of $\mathbf{v}$ to the tip of $\mathbf{u}$ |
| scalar multiple | $c\mathbf{v} = (ca,\; cb)$ | same direction if $c > 0$, opposite if $c < 0$, length times $\lvert c \rvert$ |
| length | $\lVert \mathbf{v} \rVert = \sqrt{a^2 + b^2}$ | $\lVert (5, -12) \rVert = 13$ |
| unit vector | $\hat{\mathbf{v}} = \mathbf{v} \div \lVert \mathbf{v} \rVert$ | $(3, 4)$ gives $(0.6, 0.8)$ |
| from length and angle | $\mathbf{v} = \lVert \mathbf{v} \rVert\,(\cos\theta,\; \sin\theta)$ | 60 N at $30^\circ$ is about $(51.96,\; 30)$ |
| dot product | $\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2$ | a number, not a vector |

- Standard unit vectors: $\mathbf{i} = (1, 0)$ and $\mathbf{j} = (0, 1)$, so $(a, b) = a\mathbf{i} + b\mathbf{j}$.
- Direction angle from the positive $x$-axis, counterclockwise: $\arctan\frac{b}{a}$ when $a > 0$ (add $360^\circ$ if negative), $\arctan\frac{b}{a} + 180^\circ$ when $a < 0$, and $90^\circ$ or $270^\circ$ when $a = 0$. Bearings are clockwise from north, so draw first.
- Angle between nonzero vectors, from $0^\circ$ to $180^\circ$:

$$
\mathbf{u} \cdot \mathbf{v} = \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos\theta, \qquad \cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert}.
$$

The proof expands $\lVert \mathbf{u} - \mathbf{v} \rVert^2$ twice, once by the law of cosines and once in components.

- The sign of the dot product tells the angle type: positive is acute, zero is a right angle (perpendicular), negative is obtuse.
- Rules: $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$, the dot product distributes over addition, and $\mathbf{u} \cdot \mathbf{u} = \lVert \mathbf{u} \rVert^2$.
- Perpendicular to $(a, b)$: $(-b, a)$. Parallel to $\mathbf{u}$: any scalar multiple $c\mathbf{u}$.
- Velocity and force problems: write each vector in components, add, then find the length and the angle. Work is $\mathbf{F} \cdot \mathbf{d}$. A total cost is prices dot quantities.

Main mistakes:

- Adding lengths: $\lVert \mathbf{u} + \mathbf{v} \rVert \le \lVert \mathbf{u} \rVert + \lVert \mathbf{v} \rVert$, with equality only for the same direction. For $(3, 0) + (0, 4)$ the lengths give 5, not 7.
- Using $\arctan\frac{b}{a}$ without checking the quadrant. For $(-3, -3)$ the angle is $225^\circ$, not $45^\circ$.
- Treating the dot product as a vector, or cancelling: $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{w}$ doesn't give $\mathbf{v} = \mathbf{w}$.
- Subtracting in the wrong order. $\overrightarrow{PQ}$ is $Q - P$, "end minus start".
- Asking for the direction, the unit vector or the angle of the zero vector, which has no direction.
- Confusing perpendicular (dot product 0) with parallel (scalar multiple).

### Matrix basics

A matrix with $m$ rows and $n$ columns is $m \times n$ (rows first). The entry $a_{ij}$ is in row $i$ and column $j$. Sum and scalar multiple work entry by entry, and the sum needs equal sizes.

| Item | Rule | Example |
|---|---|---|
| product size | $(m \times n)(n \times p)$ gives $m \times p$; the middle numbers must match | $(2 \times 3)(3 \times 4)$ is $2 \times 4$ |
| product entry | $(AB)_{ij}$ is row $i$ of $A$ dotted with column $j$ of $B$ | $(1, 2, 0)$ with $(2, 0, 3)$ gives 2 |
| matrix times vector | rows dotted with $\mathbf{x}$, or $x$ times column 1 plus $y$ times column 2 | rows $(2, 1)$ and $(-1, 3)$ times $(4, -2)$ give $(6, -10)$ |
| identity | $AI = IA = A$ | $I_2$ has rows $(1, 0)$ and $(0, 1)$ |
| transpose | swap rows and columns; $\mathbf{u} \cdot \mathbf{v} = \mathbf{u}^T\mathbf{v}$ | a $2 \times 3$ matrix has a $3 \times 2$ transpose |
| determinant | $\det(A) = ad - bc$ for $A$ with rows $(a, b)$ and $(c, d)$ | rows $(3, 1)$ and $(5, 2)$ give 1 |
| $2 \times 2$ inverse | swap $a$ and $d$, negate $b$ and $c$, divide by $ad - bc$ | rows $(3, 1)$, $(5, 2)$ have inverse rows $(2, -1)$, $(-5, 3)$ |

- $AB$ means "do $B$ first, then $A$", because $(AB)\mathbf{x} = A(B\mathbf{x})$. The product is defined as it is so that multiplying matrices composes substitutions.
- Rules that hold: $(AB)C = A(BC)$, $A(B + C) = AB + AC$, $(A + B)C = AC + BC$, $(AB)^{-1} = B^{-1}A^{-1}$.
- Rules that fail: $AB = BA$ (swapping the columns of $A$ is $AS$ and swapping rows is $SA$), and cancelling: $AB = 0$ doesn't give $A = 0$ or $B = 0$.
- A system $a_1 x + b_1 y = c_1$, $a_2 x + b_2 y = c_2$ is $A\mathbf{x} = \mathbf{b}$ with $A$ the coefficient matrix. If $\det A \ne 0$ then $\mathbf{x} = A^{-1}\mathbf{b}$, multiplying on the left. If $\det A = 0$ the system has no solution or infinitely many.
- Acting on the plane: the columns of $A$ are where $\mathbf{i}$ and $\mathbf{j}$ go. Rotation by $90^\circ$ has columns $(0, 1)$ and $(-1, 0)$. Reflection in $y = x$ swaps the coordinates. A stretch is a diagonal matrix.
- $\lvert \det A \rvert$ is the factor by which areas scale, and a negative determinant flips the plane. If $\det A = 0$ the plane collapses onto a line, so there is no inverse.
- In NumPy, `A @ B` is the matrix product, `A * B` is entry by entry, and `np.linalg.solve(A, b)` solves a system without computing the inverse. An adjacency matrix $G$ has $(G^k)_{ij}$ equal to the number of walks of length $k$ from $i$ to $j$.

Main mistakes:

- Multiplying entry by entry instead of rows by columns.
- Assuming $AB = BA$, or that a product with a zero factor must be zero.
- Multiplying matrices whose sizes don't match, or forgetting that $AB$ can exist while $BA$ doesn't.
- Taking the inverse entry by entry, as the reciprocals of the entries.
- Multiplying by the inverse on the wrong side when solving $A\mathbf{x} = \mathbf{b}$.
- Swapping the order in a composition: for "reflect, then rotate" the matrix is $RF$, with the reflection written next to the point.

### Vectors in 3D and the cross product

Points and vectors in space have three components, and the axes are right-handed: $\mathbf{i} \times \mathbf{j} = \mathbf{k}$. Length, unit vector and dot product get a third term.

| Item | Formula | Example |
|---|---|---|
| length | $\lVert \mathbf{v} \rVert = \sqrt{a^2 + b^2 + c^2}$ | $\lVert (3, 4, 2) \rVert = \sqrt{29}$ |
| dot product and angle | $\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 = \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \cos\theta$ | $(1, 2, 2)$ and $(2, 3, 6)$: $\cos\theta = \frac{20}{21}$ |
| cross product | $(u_2 v_3 - u_3 v_2,\; u_3 v_1 - u_1 v_3,\; u_1 v_2 - u_2 v_1)$ | $(1, 2, 3) \times (4, 5, 6) = (-3, 6, -3)$ |
| parallelogram area | $\lVert \mathbf{u} \times \mathbf{v} \rVert = \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert \sin\theta$ | triangle: half of it |
| triple product | $\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})$, the $3 \times 3$ determinant of the rows | box volume $\lvert \cdot \rvert$, tetrahedron one sixth |

- Cover-a-column pattern: cover column 1 for the first component, column 2 (and change the sign) for the second, column 3 for the third, taking the $2 \times 2$ determinant of what is left. Check by dotting the result with both factors: both must be 0.
- $\mathbf{u} \times \mathbf{v}$ is perpendicular to both vectors, and the right-hand rule gives its direction. $\mathbf{v} \times \mathbf{u} = -(\mathbf{u} \times \mathbf{v})$, $\mathbf{u} \times \mathbf{u} = \mathbf{0}$, and $\mathbf{u} \times \mathbf{v} = \mathbf{0}$ exactly when the vectors are parallel (or one is zero). It distributes over addition.
- $\mathbf{i} \times \mathbf{j} = \mathbf{k}$, $\mathbf{j} \times \mathbf{k} = \mathbf{i}$, $\mathbf{k} \times \mathbf{i} = \mathbf{j}$; the reverse order gives a minus sign.
- Three points are collinear when $\overrightarrow{AB} \times \overrightarrow{AC} = \mathbf{0}$, and four points are coplanar when the triple product is 0.
- Graphics: the normal of triangle $ABC$ is $\overrightarrow{AB} \times \overrightarrow{AC}$. It faces a camera at $E$ when $\mathbf{n} \cdot \overrightarrow{AE} > 0$ (back-face culling needs only the sign), and its diffuse brightness is $\max(0, \hat{\mathbf{n}} \cdot \hat{\mathbf{l}})$ with unit vectors.
- Whole-number lengths: $(1, 2, 2)$ has length 3, $(2, 3, 6)$ has length 7, $(2, 6, 9)$ has length 11.

Main mistakes:

- Swapping the order, or the sign of the middle component, which should be $u_3 v_1 - u_1 v_3$.
- Mixing the products: the dot product is a number (0 for perpendicular), the cross product is a vector ($\mathbf{0}$ for parallel).
- Assuming the cross product is associative or can be cancelled: $\mathbf{u} \times \mathbf{v} = \mathbf{u} \times \mathbf{w}$ does not give $\mathbf{v} = \mathbf{w}$.
- Using it on two-component vectors without a third component 0.

### Lines and planes in 3D

| Object | Forms |
|---|---|
| line through $P_0$ with direction $\mathbf{m} = (a, b, c)$ | vector $\mathbf{r} = \mathbf{r}_0 + t\mathbf{m}$; parametric $x = x_0 + at$, and so on; symmetric $\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}$ (no zero components) |
| plane through $P_0$ with normal $\mathbf{n} = (a, b, c)$ | scalar $ax + by + cz = d$ with $d = \mathbf{n} \cdot \mathbf{r}_0$; vector $\mathbf{r} = \mathbf{r}_0 + s\mathbf{u} + t\mathbf{v}$ with $\mathbf{n} = \mathbf{u} \times \mathbf{v}$ |
| plane through three points | $\mathbf{n} = \overrightarrow{AB} \times \overrightarrow{AC}$, then $d = \mathbf{n} \cdot A$ |

| Question | Test |
|---|---|
| two lines | parallel if $\mathbf{m}_1 \times \mathbf{m}_2 = \mathbf{0}$. Otherwise they meet if $(\mathbf{r}_2 - \mathbf{r}_1) \cdot (\mathbf{m}_1 \times \mathbf{m}_2) = 0$ and are skew if not. Use two parameters, $s$ and $t$ |
| line and plane | $t = \frac{d - \mathbf{n} \cdot \mathbf{r}_0}{\mathbf{n} \cdot \mathbf{m}}$ if $\mathbf{n} \cdot \mathbf{m} \ne 0$ (one point). If $\mathbf{n} \cdot \mathbf{m} = 0$: in the plane when $\mathbf{n} \cdot \mathbf{r}_0 = d$, else no point |
| two planes | parallel if $\mathbf{n}_1 \times \mathbf{n}_2 = \mathbf{0}$. Otherwise a line with direction $\mathbf{n}_1 \times \mathbf{n}_2$ |
| three planes | triple product of the normals not 0: one point. If 0: a line (consistent) or none (inconsistent) |
| point $Q$ to plane | $\frac{\lvert \mathbf{n} \cdot Q - d \rvert}{\lVert \mathbf{n} \rVert}$ |
| skew lines | $\frac{\lvert (\mathbf{r}_2 - \mathbf{r}_1) \cdot (\mathbf{m}_1 \times \mathbf{m}_2) \rvert}{\lVert \mathbf{m}_1 \times \mathbf{m}_2 \rVert}$ |

- One linear equation in space is a plane. A line needs two equations or a parameter.
- The angle between planes is the angle between the normals: $\cos\theta = \frac{\lvert \mathbf{n}_1 \cdot \mathbf{n}_2 \rvert}{\lVert \mathbf{n}_1 \rVert \lVert \mathbf{n}_2 \rVert}$. A line is parallel to a plane when $\mathbf{m} \cdot \mathbf{n} = 0$ and perpendicular to it when $\mathbf{m}$ is a multiple of $\mathbf{n}$.
- The plane through $(p, 0, 0)$, $(0, q, 0)$ and $(0, 0, r)$ is $\frac{x}{p} + \frac{y}{q} + \frac{z}{r} = 1$.

Main mistakes:

- Using one parameter for both lines, which tests a collision and not a crossing.
- Thinking two non-parallel lines in space must meet. They can be skew.
- Writing $x + y = 3$ as a line in space. It is a plane.
- Getting the sign of $d$ wrong, or leaving out the absolute value in the distance formula.
- Mixing up parallel to a plane ($\mathbf{m} \cdot \mathbf{n} = 0$) and perpendicular to it.
