# Vectors and matrices

Quantities with a direction, and tables of numbers that combine and transform them: the bridge from high school algebra to linear algebra.

1. [Vectors in the plane](01-vectors-in-the-plane.md)
2. [Matrix basics](02-matrix-basics.md)

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
