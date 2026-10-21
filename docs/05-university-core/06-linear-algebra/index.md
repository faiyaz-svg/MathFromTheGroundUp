# Linear algebra

Vectors and systems, matrices and their inverses, bases and dimension, linear maps, determinants, orthogonality and least squares, and eigenvalues.

1. [Vectors, dot product and span](01-vectors-dot-product-and-span.md)
2. [Systems and Gaussian elimination](02-systems-and-gaussian-elimination.md)
3. [Matrix algebra and inverses](03-matrix-algebra-and-inverses.md)
4. [Linear independence, basis and dimension](04-linear-independence-basis-and-dimension.md)
5. [Linear transformations, kernel and image](05-linear-transformations-kernel-and-image.md)
6. [Determinants](06-determinants.md)
7. [Orthogonality, projections and least squares](07-orthogonality-projections-and-least-squares.md)
8. [Eigenvalues and eigenvectors](08-eigenvalues-and-eigenvectors.md)

## Cheat sheet

### Vectors, dot product and span

| Idea | Rule |
|---|---|
| vector in $\mathbb{R}^n$ | $(x_1, \dots, x_n)$, a column in matrix products; add and scale one component at a time |
| linear combination | $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k$ |
| span | all linear combinations; always contains $\mathbf{0}$ |
| dot product | $\mathbf{u} \cdot \mathbf{v} = \sum u_iv_i$, a number; symmetric and linear |
| norm and distance | $\lVert \mathbf{v} \rVert = \sqrt{\mathbf{v} \cdot \mathbf{v}}$, distance $\lVert \mathbf{u} - \mathbf{v} \rVert$ |
| orthogonal | $\mathbf{u} \cdot \mathbf{v} = 0$ |
| angle | $\cos\theta = \dfrac{\mathbf{u} \cdot \mathbf{v}}{\lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert}$ |

Cauchy-Schwarz: $\lvert \mathbf{u} \cdot \mathbf{v} \rvert \le \lVert \mathbf{u} \rVert \lVert \mathbf{v} \rVert$, with equality exactly when one vector is a scalar multiple of the other. The proof expands $0 \le \lVert \mathbf{u} - t\mathbf{v} \rVert^2$ with $t = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}}$. Triangle inequality: $\lVert \mathbf{u} + \mathbf{v} \rVert \le \lVert \mathbf{u} \rVert + \lVert \mathbf{v} \rVert$. Pythagoras: $\lVert \mathbf{u} + \mathbf{v} \rVert^2 = \lVert \mathbf{u} \rVert^2 + \lVert \mathbf{v} \rVert^2$ exactly when $\mathbf{u} \perp \mathbf{v}$.

The span of one nonzero vector is a line through the origin, and of two non-parallel vectors in $\mathbb{R}^3$ a plane through the origin. A vector already in the span adds nothing. To test whether $\mathbf{b}$ is in a span, solve $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k = \mathbf{b}$; in $\mathbb{R}^3$ with two vectors, find $\mathbf{n}$ orthogonal to both and test $\mathbf{n} \cdot \mathbf{b} = 0$.

As data: a row of features is a vector, cosine similarity ignores length, spending is $\mathbf{p} \cdot \mathbf{q}$, and the budget line $\mathbf{p} \cdot \mathbf{q} = m$ is orthogonal to $\mathbf{p}$.

Main mistakes:

- Cancelling $\mathbf{u}$ in $\mathbf{u} \cdot \mathbf{v} = \mathbf{u} \cdot \mathbf{w}$.
- Taking an angle with $\mathbf{0}$.
- Treating the triangle inequality as an equality.

### Systems and Gaussian elimination

| Idea | Rule |
|---|---|
| system as a matrix equation | $A\mathbf{x} = \mathbf{b}$, with augmented matrix $[A \mid \mathbf{b}]$ |
| row operations | swap two rows; multiply a row by $c \ne 0$; add a multiple of another row |
| REF | zero rows last; leading entries step right and down |
| RREF | also every pivot is $1$ with zeros above and below; it is unique |
| basic and free variables | the column has a pivot, or not |

Row operations don't change the solution set, because each one can be undone. The algorithm: pick a pivot, clear below it, move down and right (REF); look for a row $(0 \cdots 0 \mid c)$ with $c \ne 0$; scale pivots to $1$ and clear above them (RREF); read off the solutions; check.

| RREF of $[A \mid \mathbf{b}]$ | Solutions |
|---|---|
| a row $(0 \cdots 0 \mid 1)$ | none |
| a pivot in every column of $A$, no such row | exactly one |
| a free variable, no such row | infinitely many, one parameter per free variable |

A system never has exactly two solutions: if $\mathbf{p} \ne \mathbf{q}$ are solutions, so is every $\mathbf{p} + t(\mathbf{q} - \mathbf{p})$. A homogeneous system with more unknowns than equations has a nontrivial solution. The solutions of $A\mathbf{x} = \mathbf{b}$ are one particular solution plus every solution of $A\mathbf{x} = \mathbf{0}$, written in parametric vector form $\mathbf{x} = \mathbf{p} + s\mathbf{u} + t\mathbf{w}$. Forward elimination costs $\frac{n(n-1)(2n+5)}{6} \approx \frac{n^3}{3}$ operations, so doubling $n$ gives about 8 times the work. In floating point, swap rows to use a large pivot.

Main mistakes:

- Using $R_i \to R_i + cR_i$ as a row operation.
- Forgetting to apply an operation to the right-hand side.
- Reading a zero row $(0 \cdots 0 \mid 0)$ as a contradiction.
- Assigning free variables to rows instead of columns.

### Matrix algebra and inverses

| Rule | Statement |
|---|---|
| product | $(AB)_{ij} = \sum_k a_{ik}b_{kj}$, defined when the columns of $A$ match the rows of $B$ |
| three readings | entries; columns $A\mathbf{b}_j$; rows (row of $A$)$B$ |
| holds | associative, distributive, $IA = AI = A$ |
| fails | commutative; cancellation; "a zero product has a zero factor" |
| transpose | $(AB)^T = B^TA^T$ |
| inverse | $(AB)^{-1} = B^{-1}A^{-1}$, $(A^T)^{-1} = (A^{-1})^T$; unique if it exists |

To find $A^{-1}$, row reduce $[A \mid I]$ to $[I \mid A^{-1}]$; fewer than $n$ pivots means $A$ is singular. For $2 \times 2$, $A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$. A row operation is left multiplication by an elementary matrix, which is invertible.

Invertible matrix theorem, first part. For an $n \times n$ matrix these are equivalent: $A$ is invertible; the RREF is $I$; there are $n$ pivots; $A\mathbf{x} = \mathbf{0}$ has only the trivial solution; $A\mathbf{x} = \mathbf{b}$ is solvable (uniquely) for every $\mathbf{b}$; $A^T$ is invertible; $A$ is a product of elementary matrices. For square matrices, $AB = I$ implies $BA = I$.

Applications: in graphics, homogeneous coordinates, and a rotation about a point is $TRT^{-1}$ read right to left. In a graph, $(A^k)_{ij}$ counts walks of length $k$, and $\operatorname{tr}A^3$ is 6 times the number of triangles. In the Leontief model, $\mathbf{x} = C\mathbf{x} + \mathbf{d}$ gives $\mathbf{x} = (I - C)^{-1}\mathbf{d}$.

Main mistakes:

- Writing $(AB)^{-1} = A^{-1}B^{-1}$.
- Taking the matrix of reciprocals as the inverse.
- "Dividing" by a matrix without saying on which side.

### Linear independence, basis and dimension

| Idea | Definition or test |
|---|---|
| independent | $\sum c_i\mathbf{v}_i = \mathbf{0}$ only with all $c_i = 0$; columns are independent exactly when every column is a pivot column |
| subspace | contains $\mathbf{0}$; closed under $+$ and scalar multiples |
| $N(A)$, $\operatorname{col}(A)$ | $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\}$ in $\mathbb{R}^n$; the span of the columns, in $\mathbb{R}^m$ |
| basis | independent and spanning; unique coordinates $[\mathbf{v}]_{\mathcal{B}} = B^{-1}\mathbf{v}$ |
| dimension, rank, nullity | the size of a basis; $\dim \operatorname{col}(A)$; $\dim N(A)$ |

Redundancy lemma: a list is dependent exactly when some vector is a combination of the others. A vector outside the span keeps an independent list independent.

Exchange lemma: more than $m$ vectors in the span of $m$ vectors are dependent, by the homogeneous system with more unknowns than equations. So all bases of a subspace have the same size. Consequences: $\dim \mathbb{R}^n = n$; in a $d$-dimensional space, $d$ independent vectors or $d$ spanning vectors are a basis; more than $n$ vectors in $\mathbb{R}^n$ are dependent; $W \subseteq V$ gives $\dim W \le \dim V$, with equality only if $W = V$.

Bases from pivots: the pivot columns of $A$ (not of the RREF) for $\operatorname{col}(A)$, and one vector per free variable for $N(A)$. So $\operatorname{rank}(A) + \dim N(A) = n$ and $\operatorname{rank}(A) = \operatorname{rank}(A^T)$. A set defined by homogeneous linear equations is a null space, so it is a subspace, of dimension $n$ minus the number of pivots. The invertible matrix theorem adds: independent columns, spanning columns, columns a basis, rank $n$, $N(A) = \{\mathbf{0}\}$, rows a basis.

Main mistakes:

- Treating pairwise independence as independence.
- Taking basis columns from the RREF.
- Confusing the dimension of a subspace with that of the space around it.
- Forgetting that a subspace must contain $\mathbf{0}$.

### Linear transformations, kernel and image

A map $T \colon \mathbb{R}^n \to \mathbb{R}^m$ is linear if $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ and $T(c\mathbf{v}) = cT(\mathbf{v})$. Then $T(\mathbf{0}) = \mathbf{0}$, so a translation is not linear. Every linear map is $\mathbf{x} \mapsto A\mathbf{x}$, where column $j$ of $A$ is $T(\mathbf{e}_j)$.

| Map | Matrix |
|---|---|
| rotation by $\theta$ | $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ |
| reflection in the $x$-axis | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ |
| reflection in $y = x$ | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ |
| scaling | $\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}$ |
| shear | $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ |
| projection onto the $x$-axis | $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ |

The kernel $\ker T = \{\mathbf{x} \mid T(\mathbf{x}) = \mathbf{0}\}$ and the image $\operatorname{im} T$ are subspaces. For a matrix, $\ker = N(A)$ and $\operatorname{im} = \operatorname{col}(A)$. The map is injective if and only if $\ker T = \{\mathbf{0}\}$, and surjective if and only if the rank is $m$.

Rank-nullity: $\dim\ker T + \dim\operatorname{im} T = n$, the number of columns. For a square matrix, injective, surjective and invertible all mean the same thing. The composition of maps is the product of matrices, and $BA$ means "do $A$ first". An affine map $A\mathbf{x} + \mathbf{b}$ is not linear; the trick of writing $(x, y, 1)$ turns a translation into a matrix.

Main mistakes:

- Writing the images of the basis vectors as rows.
- Putting a kernel vector in the output space.
- Counting rows instead of columns in rank-nullity.

### Determinants

The determinant is the signed factor by which a matrix scales area (2D) or volume (3D). The sign says whether orientation is kept. Formulas:

$$
\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc, \qquad \det A = \sum_{j=1}^{n}(-1)^{1+j}a_{1j}\det(M_{1j}).
$$

Expansion works along any row or column, with checkerboard signs. For a $3 \times 3$ matrix, $\det = a(ei - fh) - b(di - fg) + c(dh - eg)$.

| Operation on the rows | Effect on $\det$ |
|---|---|
| swap two rows | multiplies by $-1$ |
| scale a row by $c$ | multiplies by $c$ |
| add a multiple of a row to another | no change |

Also: $\det(A^T) = \det A$, $\det(AB) = \det A\det B$, $\det(A^{-1}) = \frac{1}{\det A}$, $\det(cA) = c^n\det A$, and for a triangular matrix the determinant is the product of the diagonal. A square matrix is invertible if and only if $\det A \ne 0$. Cramer's rule: $x_i = \frac{\det A_i}{\det A}$, where $A_i$ has column $i$ replaced by $\mathbf{b}$.

Computing: by row reduction to triangular form, $\det A = (-1)^s \cdot (\text{product of the pivots})$, with $s$ the number of swaps. Cofactor expansion costs about $n!$ operations and elimination about $\frac{n^3}{3}$, so $n = 20$ is out of reach for one and trivial for the other.

Main mistakes:

- Writing $\det(A + B) = \det A + \det B$.
- Using $c\det A$ for $\det(cA)$.
- Applying the diagonal-product rule to a non-triangular matrix.
- Using the rule of Sarrus beyond $3 \times 3$.

### Orthogonality, projections and least squares

Vectors are orthogonal when $\mathbf{u} \cdot \mathbf{v} = 0$. An orthogonal set of nonzero vectors is independent. In an orthogonal basis $\mathbf{u}_1, \dots, \mathbf{u}_k$, the coordinates of $\mathbf{y}$ are $\frac{\mathbf{y} \cdot \mathbf{u}_j}{\mathbf{u}_j \cdot \mathbf{u}_j}$. A matrix $Q$ with orthonormal columns has $Q^TQ = I$.

$$
\operatorname{proj}_{\mathbf{u}}\mathbf{v} = \frac{\mathbf{v} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}}\,\mathbf{u}, \qquad \hat{\mathbf{y}} = \operatorname{proj}_W\mathbf{y} = \sum_j \operatorname{proj}_{\mathbf{u}_j}\mathbf{y} \text{ for an orthogonal basis of } W.
$$

Orthogonal decomposition: $\mathbf{y} = \hat{\mathbf{y}} + \mathbf{z}$ in exactly one way, with $\hat{\mathbf{y}}$ in $W$ and $\mathbf{z}$ in $W^\perp$. The projection $\hat{\mathbf{y}}$ is the closest point of $W$ to $\mathbf{y}$ (Pythagoras).

Gram-Schmidt: $\mathbf{u}_1 = \mathbf{v}_1$ and $\mathbf{u}_j = \mathbf{v}_j - \sum_{i<j}\operatorname{proj}_{\mathbf{u}_i}\mathbf{v}_j$. Divide by the lengths for an orthonormal basis. Scaling a $\mathbf{u}_j$ before the next step is allowed.

Least squares: the best answer to an inconsistent $A\mathbf{x} = \mathbf{b}$ solves the normal equations $A^TA\hat{\mathbf{x}} = A^T\mathbf{b}$, which say the residual is perpendicular to every column. The solution is unique when the columns are independent, and then $\hat{\mathbf{b}} = A(A^TA)^{-1}A^T\mathbf{b}$. To fit $y = a + bx$, use the columns $(1, \dots, 1)$ and $(x_1, \dots, x_m)$; the residuals add to 0, and the line passes through $(\bar{x}, \bar{y})$. In practice use `numpy.linalg.lstsq` or QR, not an explicit inverse.

Main mistakes:

- Summing projections onto a non-orthogonal basis.
- Leaving out the column of ones.
- Mixing up orthogonal and orthonormal.

### Eigenvalues and eigenvectors

An eigenvector satisfies $A\mathbf{v} = \lambda\mathbf{v}$ with $\mathbf{v} \ne \mathbf{0}$. The eigenvalues are the roots of $\det(A - \lambda I) = 0$, and the eigenspace for $\lambda$ is $N(A - \lambda I)$. For a $2 \times 2$ matrix, $\lambda^2 - (\operatorname{tr}A)\lambda + \det A = 0$. In general the eigenvalues add to the trace and multiply to the determinant. The eigenvalues of a triangular matrix are its diagonal entries, and $0$ is an eigenvalue exactly when $A$ is not invertible.

Eigenvectors for different eigenvalues are independent. A matrix is diagonalizable, $A = PDP^{-1}$, exactly when it has $n$ independent eigenvectors (so $n$ different eigenvalues is enough). Then $A^k = PD^kP^{-1}$. A repeated eigenvalue can fail: $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has one eigenvector.

| Topic | Result |
|---|---|
| Markov chain $\mathbf{x}_{k+1} = M\mathbf{x}_k$ | columns of $M$ add to 1, so 1 is an eigenvalue; the steady state is its eigenvector with entries adding to 1; other eigenvalues below 1 in absolute value give convergence |
| Fibonacci | eigenvalues $\varphi = \frac{1 + \sqrt{5}}{2}$ and $\psi = \frac{1 - \sqrt{5}}{2}$ give $F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}$ |
| rotation by $\theta$ | eigenvalues $e^{\pm i\theta}$, no real eigenvector unless $\theta$ is $0^\circ$ or $180^\circ$ |
| PageRank | the eigenvector of eigenvalue 1 of the surfer's stochastic matrix, found by power iteration |
| symmetric matrix | real eigenvalues, orthogonal eigenvectors for different eigenvalues, $A = QDQ^T$ |

Main mistakes:

- Calling $\mathbf{0}$ an eigenvector.
- Reading eigenvalues off a row-reduced matrix.
- Assuming a repeated eigenvalue gives enough eigenvectors.
- Putting the columns of $P$ and the entries of $D$ in different orders.
