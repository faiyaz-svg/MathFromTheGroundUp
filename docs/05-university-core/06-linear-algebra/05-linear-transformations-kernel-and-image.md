# Linear transformations, kernel and image

After this lesson you can decide whether a map $\mathbb{R}^n \to \mathbb{R}^m$ is linear, write down its matrix, describe what a $2 \times 2$ matrix does to the plane, find and prove facts about its kernel and image, and use the rank-nullity theorem.

Before this: [vectors, dot product and span](01-vectors-dot-product-and-span.md), [matrix algebra and inverses](03-matrix-algebra-and-inverses.md), [linear independence, basis and dimension](04-linear-independence-basis-and-dimension.md) and [injective, surjective and bijective](../../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md). The $2 \times 2$ pictures start from [matrix basics](../../03-high-school/10-vectors-and-matrices/02-matrix-basics.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Is $T(x, y) = (x + 1, y)$ a linear map? Give a reason.
2. Find the matrix of $T(x, y, z) = (x + 2y,\; 3z - y)$.
3. Find the kernel of $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ and say whether $\mathbf{x} \mapsto A\mathbf{x}$ is injective.

<details class="solution" markdown>
<summary>Answers</summary>

1. No. A linear map sends $\mathbf{0}$ to $\mathbf{0}$, and $T(0, 0) = (1, 0)$. It is a translation.
2. The columns are $T(\mathbf{e}_1) = (1, 0)$, $T(\mathbf{e}_2) = (2, -1)$ and $T(\mathbf{e}_3) = (0, 3)$, so $A = \begin{pmatrix} 1 & 2 & 0 \\ 0 & -1 & 3 \end{pmatrix}$.
3. Solve $x + 2y = 0$ (the second equation is twice the first): $\mathbf{x} = t\begin{pmatrix} -2 \\ 1 \end{pmatrix}$. The kernel is that line, not just $\{\mathbf{0}\}$, so the map is not injective.

</details>

## The idea

Matrix basics showed that a $2 \times 2$ matrix does something to the whole plane. It takes every point to another point, and it turns the unit square into a parallelogram. The map keeps the grid lines straight and evenly spaced, and keeps the origin where it is. That is all a matrix can do, and the property has a name: the map is linear.

Why does it follow that the whole map is decided by two columns? Every point of the plane is $x\mathbf{i} + y\mathbf{j}$, a combination of two arrows. If the map keeps combinations (straight, evenly spaced grid lines are exactly that), then the image of the point is $x$ times the image of $\mathbf{i}$ plus $y$ times the image of $\mathbf{j}$. Two images, four numbers, and those numbers are the matrix.

This lesson does three things with that picture. First it makes "keeps combinations" precise and proves that every linear map from $\mathbb{R}^n$ to $\mathbb{R}^m$ is a matrix, so the two words describe the same thing. Second it asks the two questions you can ask of any function, in linear form: what gets sent to $\mathbf{0}$ (the kernel), and what is hit (the image). Third it connects them with the rank-nullity theorem, which says that whatever the map squashes, it squashes by exactly the number of dimensions it loses.

![Six panels, each showing the dashed unit square and the letter F inside it, and the green image of the square and F under one matrix, with the images A i in blue and A j in red. Rotation by 30 degrees turns the square. Reflection in y = x flips the F. The stretch makes the square 2 wide and 0.5 tall. The shear slants it into a parallelogram. The projection onto y = x collapses the square onto a segment. The last panel rotates by 45 degrees and scales by root 2.](../../assets/figures/05-university-core/linear-transformations-kernel-and-image-gallery.svg)

## Definitions

A function $T \colon \mathbb{R}^n \to \mathbb{R}^m$ is a **linear map** (also called a **linear transformation**) if for all vectors $\mathbf{u}, \mathbf{v}$ in $\mathbb{R}^n$ and every scalar $c$,

$$
T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) \qquad \text{and} \qquad T(c\mathbf{v}) = c\,T(\mathbf{v}).
$$

In plain words, it makes no difference whether you add (or scale) first and then apply $T$, or apply $T$ first and then add (or scale). The two rules together say that $T$ keeps linear combinations: $T(a\mathbf{u} + b\mathbf{v}) = a\,T(\mathbf{u}) + b\,T(\mathbf{v})$, and by repeating the rule the same holds for a combination of any number of vectors.

Two quick consequences. Taking $c = 0$ gives $T(\mathbf{0}) = T(0\cdot\mathbf{0}) = 0\cdot T(\mathbf{0}) = \mathbf{0}$, so a linear map fixes the origin. And a map that fails either rule is not linear. The map $(x, y) \mapsto (x + 1, y)$ fails because it moves the origin. The map $(x, y) \mapsto (xy, y)$ fails the scaling rule: doubling the input quadruples the first output.

The **standard basis** of $\mathbb{R}^n$ is the list $\mathbf{e}_1, \dots, \mathbf{e}_n$, where $\mathbf{e}_j$ has a 1 in position $j$ and 0 elsewhere. In the plane, $\mathbf{e}_1 = \mathbf{i} = (1, 0)$ and $\mathbf{e}_2 = \mathbf{j} = (0, 1)$. Every vector is $\mathbf{x} = x_1\mathbf{e}_1 + \dots + x_n\mathbf{e}_n$. In plain words, the entries of a vector are the weights in the combination of the standard basis vectors that makes it.

The **standard matrix** of a linear map $T \colon \mathbb{R}^n \to \mathbb{R}^m$ is the $m \times n$ matrix

$$
A = \begin{pmatrix} T(\mathbf{e}_1) & T(\mathbf{e}_2) & \cdots & T(\mathbf{e}_n) \end{pmatrix}
$$

whose columns are the images of the standard basis vectors. In plain words, to build the matrix, ask where each basis vector goes and write the answers as columns. Conversely, a matrix $A$ gives the map $T_A(\mathbf{x}) = A\mathbf{x}$. This map is linear, since $A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}$ and $A(c\mathbf{v}) = c\,A\mathbf{v}$ are rules of matrix algebra.

The **kernel** of a linear map $T \colon \mathbb{R}^n \to \mathbb{R}^m$ is the set of inputs that go to zero,

$$
\ker T = \{\mathbf{x} \in \mathbb{R}^n \mid T(\mathbf{x}) = \mathbf{0}\}.
$$

The **image** of $T$ is the set of outputs,

$$
\operatorname{im} T = \{T(\mathbf{x}) \mid \mathbf{x} \in \mathbb{R}^n\} \subseteq \mathbb{R}^m.
$$

In plain words, the kernel is everything the map flattens to the origin, and the image is everything the map reaches. The **rank** of $T$ is $\dim(\operatorname{im} T)$ and the **nullity** of $T$ is $\dim(\ker T)$. For $T = T_A$ these are the sets from the earlier lessons: $\ker T_A = N(A)$ is the solution set of $A\mathbf{x} = \mathbf{0}$, and $\operatorname{im} T_A = \operatorname{col}(A)$ is the span of the columns, because $A\mathbf{x} = x_1\mathbf{a}_1 + \dots + x_n\mathbf{a}_n$ is a combination of the columns $\mathbf{a}_j$ of $A$. So the rank of $T_A$ is the rank of $A$.

Recall that a subspace of $\mathbb{R}^k$ is a set that contains $\mathbf{0}$ and is closed under addition and scalar multiplication. In the plane the subspaces are the origin alone, the lines through the origin and the whole plane.

## How to do it

### Every linear map is a matrix

*Theorem 1.* Let $T \colon \mathbb{R}^n \to \mathbb{R}^m$ be linear and let $A$ be its standard matrix. Then $T(\mathbf{x}) = A\mathbf{x}$ for every $\mathbf{x}$ in $\mathbb{R}^n$, and $A$ is the only matrix with this property.

We know that $T$ keeps linear combinations, and that $A\mathbf{x}$ is the combination of the columns of $A$ with the entries of $\mathbf{x}$ as weights. We want to show that $T(\mathbf{x})$ and $A\mathbf{x}$ are the same combination. The plan is to write $\mathbf{x}$ in the standard basis, push $T$ through the sum, and compare.

*Proof.* Write $\mathbf{x} = x_1\mathbf{e}_1 + \dots + x_n\mathbf{e}_n$. Since $T$ is linear,

$$
T(\mathbf{x}) = x_1 T(\mathbf{e}_1) + \dots + x_n T(\mathbf{e}_n).
$$

The right side is the combination of the columns $T(\mathbf{e}_1), \dots, T(\mathbf{e}_n)$ of $A$ with weights $x_1, \dots, x_n$, which is $A\mathbf{x}$. For uniqueness, suppose $T(\mathbf{x}) = B\mathbf{x}$ for all $\mathbf{x}$ for some matrix $B$. Then column $j$ of $B$ is $B\mathbf{e}_j = T(\mathbf{e}_j)$, which is column $j$ of $A$, so $B = A$. $\blacksquare$

Look back: the proof needed only the two rules of linearity and the standard basis. The theorem says that "linear map $\mathbb{R}^n \to \mathbb{R}^m$" and "$m \times n$ matrix" are two names for one object, and that is why $A\mathbf{x}$ was the right way to multiply a matrix by a vector. It also gives the method for finding a matrix.

### The matrix of a map

1. Check that the map is linear: it sends $\mathbf{0}$ to $\mathbf{0}$ and each output entry is a combination of the input entries with no constants, products or powers. (A single counterexample to either rule shows that it is not.)
2. Apply the map to each standard basis vector $\mathbf{e}_1, \dots, \mathbf{e}_n$.
3. Write the $n$ answers as the columns of an $m \times n$ matrix.
4. Check: apply the matrix to one test vector and compare with the map.

### The $2 \times 2$ maps you should recognize

Following the method, a few families of matrices cover most of what you will meet in the plane. Each is found by asking where $\mathbf{i}$ and $\mathbf{j}$ go. The gallery above shows several of them.

| Map | Matrix | What it does |
|---|---|---|
| rotation by $\theta$ (counterclockwise) | $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ | $\mathbf{i} \to (\cos\theta, \sin\theta)$, $\mathbf{j} \to (-\sin\theta, \cos\theta)$; lengths and angles kept |
| reflection in the $x$-axis | $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | flips the sign of $y$ |
| reflection in the line $y = x$ | $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | swaps the two coordinates |
| scaling | $\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}$ | stretches $x$ by $a$ and $y$ by $b$ |
| horizontal shear | $\begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$ | slides each point sideways by $k$ times its height |
| projection onto the $x$-axis | $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ | drops the $y$ part; the plane collapses onto a line |

The first four are invertible: you can undo them (rotate back, reflect again, stretch by $\frac{1}{a}$ and $\frac{1}{b}$, shear by $-k$). The projection is not. It flattens the plane onto a line, so many inputs share one output, and no map can undo that. This is the geometric content of a zero determinant, which the [next lesson](06-determinants.md) measures: the area of the image square is the number $\lvert ad - bc \rvert$, and it is zero when the square is flattened.

### Kernel and image are subspaces

*Theorem 2.* For a linear map $T \colon \mathbb{R}^n \to \mathbb{R}^m$, the kernel $\ker T$ is a subspace of $\mathbb{R}^n$ and the image $\operatorname{im} T$ is a subspace of $\mathbb{R}^m$.

We know the definitions of the kernel and image and the three conditions for a subspace (it contains $\mathbf{0}$, and it is closed under addition and scalar multiplication). We want to check the three conditions for each set. The plan is to take two members, apply the rules of linearity, and see that the result still has the defining property.

*Proof.* Kernel. Since $T(\mathbf{0}) = \mathbf{0}$, the zero vector is in $\ker T$. If $\mathbf{u}$ and $\mathbf{v}$ are in $\ker T$ then $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v}) = \mathbf{0} + \mathbf{0} = \mathbf{0}$, so $\mathbf{u} + \mathbf{v}$ is in $\ker T$. If also $c$ is a scalar then $T(c\mathbf{u}) = c\,T(\mathbf{u}) = c\,\mathbf{0} = \mathbf{0}$, so $c\mathbf{u}$ is in $\ker T$.

Image. The zero vector is $T(\mathbf{0})$, so it is in $\operatorname{im} T$. Take two members $\mathbf{p} = T(\mathbf{u})$ and $\mathbf{q} = T(\mathbf{v})$ of the image. Then $\mathbf{p} + \mathbf{q} = T(\mathbf{u}) + T(\mathbf{v}) = T(\mathbf{u} + \mathbf{v})$ is an output, and $c\mathbf{p} = c\,T(\mathbf{u}) = T(c\mathbf{u})$ is an output. $\blacksquare$

Look back: each line of the proof was one use of a linearity rule, and the zero vector comes from $T(\mathbf{0}) = \mathbf{0}$. For the translation $(x, y) \mapsto (x + 1, y)$ the set of inputs that go to $\mathbf{0}$ is the single point $(-1, 0)$, which does not contain $\mathbf{0}$, so it is not a subspace. That is another sign that the map is not linear.

The next picture shows both sets for $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$. Each output is $A\begin{pmatrix} x \\ y \end{pmatrix} = (x + 2y)\begin{pmatrix} 1 \\ 2 \end{pmatrix}$, a multiple of one vector. All the points on the line $x + 2y = c$ land on the one point $c\,(1, 2)$. The line with $c = 0$ is the kernel. The image is the line through the origin and $(1, 2)$.

![Left: the plane with the red kernel line x + 2y = 0 and gray parallel lines x + 2y = c for c from minus 2 to 2. Right: the plane with the green image line y = 2x, with a dot at c times (1, 2) for each c, and the red dot at the origin where the whole kernel lands.](../../assets/figures/05-university-core/linear-transformations-kernel-and-image-kernel-image.svg)

The gray lines are the fibres of the map: the sets of inputs with a given output. Each fibre is the kernel slid sideways, and the kernel tells you exactly how much information the map throws away. The next theorem makes that precise.

### Injective if and only if the kernel is zero

*Theorem 3.* A linear map $T \colon \mathbb{R}^n \to \mathbb{R}^m$ is injective if and only if $\ker T = \{\mathbf{0}\}$.

We know that injective means $T(\mathbf{u}) = T(\mathbf{v}) \Rightarrow \mathbf{u} = \mathbf{v}$ (the definition in the [injective and surjective lesson](../../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md)). We want a statement that needs only one test vector, $\mathbf{0}$, instead of every pair. The plan is to turn a pair $\mathbf{u}, \mathbf{v}$ into the single vector $\mathbf{u} - \mathbf{v}$ by linearity.

*Proof.* Suppose $T$ is injective and $\mathbf{x}$ is in $\ker T$. Then $T(\mathbf{x}) = \mathbf{0} = T(\mathbf{0})$, so injectivity gives $\mathbf{x} = \mathbf{0}$. So the kernel is $\{\mathbf{0}\}$.

Conversely, suppose $\ker T = \{\mathbf{0}\}$ and $T(\mathbf{u}) = T(\mathbf{v})$. Then $T(\mathbf{u} - \mathbf{v}) = T(\mathbf{u}) - T(\mathbf{v}) = \mathbf{0}$, so $\mathbf{u} - \mathbf{v}$ is in the kernel. It must be $\mathbf{0}$, so $\mathbf{u} = \mathbf{v}$. $\blacksquare$

Look back: for a general function you must compare all pairs of inputs. Linearity reduces that to one question, "which vectors go to zero?", which is a system of equations $A\mathbf{x} = \mathbf{0}$ you already know how to solve. The kernel is $\{\mathbf{0}\}$ exactly when every column of the reduced matrix has a pivot, that is, when the columns of $A$ are linearly independent.

Surjectivity is the matching question about the image. The map is surjective when $\operatorname{im} T = \mathbb{R}^m$, that is, when its rank is $m$.

### The rank-nullity theorem

*Theorem 4 (rank-nullity).* For a linear map $T \colon \mathbb{R}^n \to \mathbb{R}^m$,

$$
\dim(\ker T) + \dim(\operatorname{im} T) = n.
$$

In terms of a matrix $A$ with $n$ columns: $\dim N(A) + \operatorname{rank} A = n$.

In plain words, the $n$ dimensions of the input split into the ones the map flattens (the nullity) and the ones that survive as the image (the rank).

We know the facts from the last lesson that every subspace has a basis, that the number of vectors in a basis is the dimension, and that a linearly independent list in $\mathbb{R}^n$ can be extended to a basis of $\mathbb{R}^n$. We want to count dimensions. The plan is to take a basis of the kernel, extend it to a basis of the whole input space, and show that the images of the added vectors form a basis of the image.

*Proof.* Let $\mathbf{v}_1, \dots, \mathbf{v}_k$ be a basis of $\ker T$, so $k$ is the nullity. Extend it to a basis $\mathbf{v}_1, \dots, \mathbf{v}_k, \mathbf{w}_1, \dots, \mathbf{w}_r$ of $\mathbb{R}^n$, so $k + r = n$. We claim that $T(\mathbf{w}_1), \dots, T(\mathbf{w}_r)$ is a basis of $\operatorname{im} T$. That gives rank $= r$ and finishes the proof.

They span the image. Any vector in the image is $T(\mathbf{x})$ for some $\mathbf{x}$, and $\mathbf{x} = a_1\mathbf{v}_1 + \dots + a_k\mathbf{v}_k + b_1\mathbf{w}_1 + \dots + b_r\mathbf{w}_r$. Each $T(\mathbf{v}_i)$ is $\mathbf{0}$, so $T(\mathbf{x}) = b_1 T(\mathbf{w}_1) + \dots + b_r T(\mathbf{w}_r)$.

They are linearly independent. Suppose $b_1 T(\mathbf{w}_1) + \dots + b_r T(\mathbf{w}_r) = \mathbf{0}$. By linearity $T(b_1\mathbf{w}_1 + \dots + b_r\mathbf{w}_r) = \mathbf{0}$, so the vector $\mathbf{z} = b_1\mathbf{w}_1 + \dots + b_r\mathbf{w}_r$ is in the kernel, and $\mathbf{z} = a_1\mathbf{v}_1 + \dots + a_k\mathbf{v}_k$ for some $a_i$. Then $a_1\mathbf{v}_1 + \dots + a_k\mathbf{v}_k - b_1\mathbf{w}_1 - \dots - b_r\mathbf{w}_r = \mathbf{0}$. The vectors $\mathbf{v}_i, \mathbf{w}_j$ form a basis, so they are independent, and every coefficient is 0. In particular every $b_j = 0$. $\blacksquare$

Look back: the proof shows where the image's basis comes from: the part of the input that the kernel doesn't swallow. There is a second reading in terms of [row reduction](02-systems-and-gaussian-elimination.md). In the reduced form of $A$ the rank is the number of pivot columns, the nullity is the number of free columns (each free column gives one basis vector of the kernel), and every column is one or the other, so the two numbers add to $n$.

Rank-nullity has quick consequences, each by arithmetic:

- If $n > m$, the nullity is at least $n - m > 0$, because the rank is at most $m$. So no linear map from a bigger space to a smaller one is injective: some nonzero vector is flattened.
- If $n < m$, the rank is at most $n < m$, so no linear map from a smaller space to a bigger one is surjective.
- If $n = m$ (a square matrix), injective means nullity 0, which means rank $n$, which means surjective, and the other way around. So for a square matrix, injective, surjective and bijective all mean the same thing, and they all say that $A$ is invertible. This is a new line in the invertible matrix theorem of [matrix algebra and inverses](03-matrix-algebra-and-inverses.md).

### Composition is the matrix product

*Theorem 5.* If $T \colon \mathbb{R}^n \to \mathbb{R}^m$ and $S \colon \mathbb{R}^m \to \mathbb{R}^p$ are linear with standard matrices $A$ and $B$, then $S \circ T$ is linear and its standard matrix is $BA$.

*Proof.* For every $\mathbf{x}$, $(S \circ T)(\mathbf{x}) = S(T(\mathbf{x})) = B(A\mathbf{x}) = (BA)\mathbf{x}$, by associativity of matrix multiplication. A map of the form $\mathbf{x} \mapsto M\mathbf{x}$ is linear, and by the uniqueness in Theorem 1, $BA$ is its standard matrix. $\blacksquare$

Look back: this is the reason matrix multiplication is defined the way it is, and why the product $BA$ means "do $A$ first". It also explains why $AB \ne BA$ in general: reflecting and then rotating is a different map from rotating and then reflecting (Example 2). A bijective linear map also has an inverse map that is linear. By Theorem 5 the composite of the two is the identity map, so the matrix of the inverse map is $A^{-1}$. For linearity of the inverse: if $T(\mathbf{p}) = \mathbf{u}$ and $T(\mathbf{q}) = \mathbf{v}$, then $T(c\mathbf{p} + d\mathbf{q}) = c\mathbf{u} + d\mathbf{v}$, so $T^{-1}(c\mathbf{u} + d\mathbf{v}) = cT^{-1}(\mathbf{u}) + dT^{-1}(\mathbf{v})$.

## Worked examples

<div class="example" markdown>

### Example 1: the matrix of a map from $\mathbb{R}^3$ to $\mathbb{R}^2$

Let $T(x, y, z) = (x - y + 2z,\; 3y + z)$. Find its matrix, then use it to compute $T(1, 2, -1)$.

Step 1: the map is linear, because each output is a combination of $x$, $y$, $z$ with constant coefficients and no constant term.

Step 2: apply $T$ to the standard basis. $T(\mathbf{e}_1) = T(1, 0, 0) = (1, 0)$, $T(\mathbf{e}_2) = T(0, 1, 0) = (-1, 3)$ and $T(\mathbf{e}_3) = T(0, 0, 1) = (2, 1)$.

Step 3: write the answers as columns. The map has 3 inputs and 2 outputs, so the matrix is $2 \times 3$:

$$
A = \begin{pmatrix} 1 & -1 & 2 \\ 0 & 3 & 1 \end{pmatrix}.
$$

Step 4, the check: $A\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 - 2 - 2 \\ 0 + 6 - 1 \end{pmatrix} = \begin{pmatrix} -3 \\ 5 \end{pmatrix}$, and the formula gives $T(1, 2, -1) = (1 - 2 - 2,\; 6 - 1) = (-3, 5)$. The matrix reads off the coefficients of the formula, row by row.

</div>

<div class="example" markdown>

### Example 2: reflect then rotate, or rotate then reflect

Let $F = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (reflection in the $x$-axis) and $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ (rotation by $90^\circ$). Find the matrix of "reflect, then rotate", and of "rotate, then reflect".

By Theorem 5 the map "first $F$, then $R$" has matrix $RF$, with the first map on the right:

$$
RF = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},
$$

which is the reflection in the line $y = x$. In the other order,

$$
FR = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix},
$$

the reflection in the line $y = -x$.

Check with the point $(3, 1)$. Reflect to get $(3, -1)$ and rotate to get $(1, 3)$, and indeed $RF$ swaps the coordinates of $(3, 1)$. Rotate first to get $(-1, 3)$, then reflect to get $(-1, -3)$, and $FR\begin{pmatrix} 3 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ -3 \end{pmatrix}$. The two orders give different answers.

</div>

<div class="example" markdown>

### Example 3: kernel, image and rank-nullity for a $3 \times 3$ matrix

Find the kernel and the image of $M = \begin{pmatrix} 1 & 2 & 1 \\ 2 & 4 & 0 \\ 3 & 6 & 1 \end{pmatrix}$, and decide whether $\mathbf{x} \mapsto M\mathbf{x}$ is injective or surjective.

Kernel: solve $M\mathbf{x} = \mathbf{0}$. The second equation is $2x + 4y = 0$, so $x = -2y$. The first is $x + 2y + z = 0$, which then gives $z = 0$. The third, $3x + 6y + z = 0$, is satisfied. The solutions are $\mathbf{x} = y\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}$, so $\ker M$ is the line spanned by $(-2, 1, 0)$ and the nullity is 1.

Image: the columns are $\mathbf{a}_1 = (1, 2, 3)$, $\mathbf{a}_2 = (2, 4, 6) = 2\mathbf{a}_1$ and $\mathbf{a}_3 = (1, 0, 1)$. The second column adds nothing (that is the kernel vector at work: $-2\mathbf{a}_1 + \mathbf{a}_2 = \mathbf{0}$), so the image is the span of $\mathbf{a}_1$ and $\mathbf{a}_3$, a plane. A normal vector to the plane is $\mathbf{a}_1 \times \mathbf{a}_3 = (2, 2, -2)$, so the plane is $x + y - z = 0$. The rank is 2.

Rank-nullity: $1 + 2 = 3$, the number of columns. The kernel is not $\{\mathbf{0}\}$, so $M$ is not injective, and the rank is less than 3, so it is not surjective. As a square matrix, it is not invertible.

Check: $M(-2, 1, 0) = (-2 + 2,\; -4 + 4,\; -6 + 6) = \mathbf{0}$. Also each column satisfies $x + y - z = 0$: $1 + 2 - 3 = 0$, $2 + 4 - 6 = 0$ and $1 + 0 - 1 = 0$.

</div>

<div class="example" markdown>

### Example 4: an economy as a linear map

A hypothetical economy has two sectors, farms and factories. To produce one unit of output, farms use 0.2 units of their own output and 0.4 of factory output, and factories use 0.3 units of farm output and 0.1 of their own. The matrix $C = \begin{pmatrix} 0.2 & 0.3 \\ 0.4 & 0.1 \end{pmatrix}$ has the "inputs per unit of output" as columns (farm column first). If the gross outputs are $\mathbf{x} = (x_1, x_2)$, the sectors use $C\mathbf{x}$ in production, and what is left for consumers is the net output $\mathbf{d} = \mathbf{x} - C\mathbf{x} = (I - C)\mathbf{x}$. The map $\mathbf{x} \mapsto (I - C)\mathbf{x}$ is linear, because it is a matrix.

For gross outputs $\mathbf{x} = (100, 200)$: $C\mathbf{x} = (20 + 60,\; 40 + 20) = (80, 60)$ and $\mathbf{d} = (20, 140)$.

Now the inverse question: which gross output produces the net output $\mathbf{d} = (60, 30)$? Here $I - C = \begin{pmatrix} 0.8 & -0.3 \\ -0.4 & 0.9 \end{pmatrix}$ has determinant $0.72 - 0.12 = 0.6 \ne 0$, so it is injective and surjective, with inverse $(I - C)^{-1} = \begin{pmatrix} 1.5 & 0.5 \\ \frac{2}{3} & \frac{4}{3} \end{pmatrix}$. Then $\mathbf{x} = (I - C)^{-1}\mathbf{d} = (90 + 15,\; 40 + 40) = (105, 80)$.

Check: $C\mathbf{x} = (21 + 24,\; 42 + 8) = (45, 50)$, and $\mathbf{x} - C\mathbf{x} = (60, 30)$. This is the Leontief input-output model from [matrix algebra and inverses](03-matrix-algebra-and-inverses.md), seen as a linear map, and the inverse is called the Leontief inverse. The numbers here are made up for the example.

</div>

<div class="example" markdown>

### Example 5: projection onto a line (finish it yourself)

Let $P$ send each point of the plane to the nearest point on the line $y = x$. The image of $\mathbf{i} = (1, 0)$ is $\left(\frac{1}{2}, \frac{1}{2}\right)$, the foot of the perpendicular from $(1, 0)$ to the line, and by symmetry the image of $\mathbf{j}$ is the same point.

Write the matrix of $P$. Find its kernel and image, check rank-nullity, and decide whether $P$ is injective. Then compute $P^2$ and say what it means.

<details class="solution" markdown>
<summary>Finish</summary>

The columns are the images of $\mathbf{i}$ and $\mathbf{j}$, so $P = \begin{pmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & \frac{1}{2} \end{pmatrix}$. The equations for the kernel are $\frac{1}{2}(x + y) = 0$ twice, so the kernel is the line $y = -x$, spanned by $(1, -1)$: the points that the perpendicular drops onto the origin. The image is the line $y = x$, spanned by $(1, 1)$. The nullity is 1 and the rank is 1, and $1 + 1 = 2 = n$. The kernel is not $\{\mathbf{0}\}$, so $P$ is not injective.

Squaring, $P^2 = \begin{pmatrix} \frac{1}{4} + \frac{1}{4} & \frac{1}{4} + \frac{1}{4} \\ \frac{1}{4} + \frac{1}{4} & \frac{1}{4} + \frac{1}{4} \end{pmatrix} = P$. Projecting twice is the same as projecting once, because the first projection already lands on the line.

Check: $P(3, 1) = (2, 2)$, the midpoint of the coordinates, and $P(2, 2) = (2, 2)$. Also $P(1, -1) = \mathbf{0}$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a map with a constant added is not linear. The map $\mathbf{x} \mapsto A\mathbf{x} + \mathbf{b}$ with $\mathbf{b} \ne \mathbf{0}$ sends $\mathbf{0}$ to $\mathbf{b}$, so it breaks both rules. It is called an affine map. In a neural network the layer $W\mathbf{x} + \mathbf{b}$ is affine, and in graphics a translation is affine. The fix in graphics is shown under [Tricks and shortcuts](#tricks-and-shortcuts).

</div>

<div class="warning" markdown>

Watch out: the kernel lives in the input space and the image lives in the output space. For a $3 \times 2$ matrix the kernel is a subset of $\mathbb{R}^2$ and the image is a subset of $\mathbb{R}^3$. A kernel vector has as many entries as the matrix has columns, and an image vector has as many entries as the matrix has rows. Writing a kernel vector with three entries for a $3 \times 2$ matrix is a sign that the sets got swapped.

</div>

<div class="warning" markdown>

Watch out: the images of the basis vectors are the columns of the matrix, not the rows. For $T(x, y) = (x + 2y, 3x)$, the images are $T(\mathbf{e}_1) = (1, 3)$ and $T(\mathbf{e}_2) = (2, 0)$, so the matrix is $\begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$. Writing the images as rows gives the transpose $\begin{pmatrix} 1 & 3 \\ 2 & 0 \end{pmatrix}$, which is a different map. The test is the first column: it must be $T(\mathbf{e}_1)$.

</div>

<div class="warning" markdown>

Watch out: rank-nullity counts the columns, not the rows. For a $4 \times 6$ matrix of rank 3 the nullity is $6 - 3 = 3$. It is not $4 - 3 = 1$. The input space has dimension 6.

</div>

<div class="warning" markdown>

Watch out: the order of composition. In "reflect, then rotate" the matrix is $RF$ with the reflection on the right, because $RF\mathbf{x}$ means $R(F\mathbf{x})$ and $F$ touches $\mathbf{x}$ first. Reading the product left to right as "first $R$, then $F$" reverses the order.

</div>

## Tricks and shortcuts

To guess a map's matrix, track just the two (or three) basis vectors. For the rotation by $90^\circ$, $\mathbf{i}$ turns into $\mathbf{j}$ and $\mathbf{j}$ turns into $-\mathbf{i}$, so the columns are $(0, 1)$ and $(-1, 0)$. A $2 \times 2$ rotation also satisfies $R_\alpha R_\beta = R_{\alpha + \beta}$, because rotating by $\beta$ and then by $\alpha$ is rotating by $\alpha + \beta$; multiplying out the matrices gives the angle-addition formulas for sine and cosine in the entries.

For the question "is this map injective?" count the pivots: the columns of $A$ are independent exactly when there is a pivot in every column. And "is it surjective?" asks for a pivot in every row.

Translations become matrix products if you add a coordinate. Write the point $(x, y)$ as $(x, y, 1)$. Then the $3 \times 3$ matrix $\begin{pmatrix} 1 & 0 & a \\ 0 & 1 & b \\ 0 & 0 & 1 \end{pmatrix}$ sends $(x, y, 1)$ to $(x + a, y + b, 1)$. These are called homogeneous coordinates, and graphics code uses them to write a rotation followed by a translation followed by a scaling as one matrix product.

## In code

The code builds a matrix from a map by applying it to the standard basis, finds the rank and a kernel vector with the singular value decomposition (which the book doesn't cover; here it is used as a black box that returns the null directions), and checks composition, the homogeneous-coordinates trick and the collapse of two stacked linear layers.

<details class="code" markdown>
<summary>In code</summary>

```python
import numpy as np

def T(v):
    x, y, z = v
    return np.array([x - y + 2 * z, 3 * y + z])

# The matrix of a linear map: its columns are the images of the standard basis.
A = np.column_stack([T(e) for e in np.eye(3)])
print(A)
# [[ 1. -1.  2.]
#  [ 0.  3.  1.]]
v = np.array([1.0, 2.0, -1.0])
print(T(v), A @ v)
# [-3.  5.] [-3.  5.]

# Rank, nullity and a kernel vector from the SVD.
M = np.array([[1, 2, 1], [2, 4, 0], [3, 6, 1]], dtype=float)
u, s, vt = np.linalg.svd(M)
rank = int(np.sum(s > 1e-10))
print(rank, M.shape[1] - rank)
# 2 1
kernel = vt[rank:].T          # columns span the kernel
print(np.round(kernel[:, 0] / kernel[1, 0], 6) + 0.0, np.allclose(M @ kernel, 0))
# [-2.  1.  0.] True

# Composition is the matrix product: reflect in the x-axis first, then rotate by 90 degrees.
F = np.array([[1, 0], [0, -1]])
R = np.array([[0, -1], [1, 0]])
p = np.array([3, 1])
print(R @ (F @ p), (R @ F) @ p)
# [1 3] [1 3]
print(R @ F)
# [[0 1]
#  [1 0]]

# Translation is not linear, but a 3 by 3 matrix can translate a point written as (x, y, 1).
Tr = np.array([[1, 0, 5], [0, 1, -2], [0, 0, 1]])
print(Tr @ np.array([3, 1, 1]))
# [ 8 -1  1]

# Two linear layers with no nonlinearity in between collapse into one matrix.
rng = np.random.default_rng(0)
W1, W2 = rng.normal(size=(4, 3)), rng.normal(size=(2, 4))
x = rng.normal(size=3)
print(np.allclose(W2 @ (W1 @ x), (W2 @ W1) @ x))
# True
```

</details>

## FAQ

### Why must a linear map send the zero vector to the zero vector?

Because scaling by 0 is one of the two rules. The vector $0 \cdot \mathbf{v}$ is $\mathbf{0}$ for every $\mathbf{v}$, so $T(\mathbf{0}) = T(0 \cdot \mathbf{v}) = 0 \cdot T(\mathbf{v}) = \mathbf{0}$. Geometrically, the grid lines stay straight and evenly spaced, so the one point where all the lines through the origin cross has nowhere to go. A map that slides the origin, such as a translation, is not linear, even though it keeps lines straight.

### Is the matrix the same thing as the map?

For maps $\mathbb{R}^n \to \mathbb{R}^m$ and the standard basis, yes, by Theorem 1. In general vector spaces, or if you choose another basis for $\mathbb{R}^n$, the same map has different matrices. The [eigenvalues lesson](08-eigenvalues-and-eigenvectors.md) is about picking a basis that makes the matrix simple. This book keeps to the standard basis except there.

### Why is the kernel called the "null" space for matrices and the "kernel" for maps?

They are the same set in two vocabularies: $\ker T_A = N(A)$ and $\operatorname{im} T_A = \operatorname{col}(A)$. Textbooks that start with matrices say null space and column space, and textbooks that start with maps say kernel and image. A first course uses whichever its text does, and exam questions often use both words, so know both.

### Does rank-nullity say something for functions that aren't linear?

No. The kernel isn't a subspace and the image needn't have a dimension. The square map $x \mapsto x^2$ on $\mathbb{R}$ flattens the two inputs $\pm a$ onto one output and misses all negative numbers, and nothing like "the dimensions add up" holds. Linearity is what makes the flattened directions and the reached directions two subspaces whose dimensions add up to $n$.

## Practice

### Warm-up

1\. Decide whether each map is linear. If it is, give a one-line reason; if not, give a counterexample. (a) $T(x, y) = (2x - y,\; x + 3y)$. (b) $T(x, y) = (x + y,\; xy)$. (c) $T(x, y) = (x + 1,\; y)$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Linear: each output is a combination of $x$ and $y$ with constant coefficients, and the map is $\mathbf{x} \mapsto \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}\mathbf{x}$.

(b) Not linear. With $\mathbf{v} = (1, 1)$ we get $T(\mathbf{v}) = (2, 1)$, and $T(2\mathbf{v}) = T(2, 2) = (4, 4)$, which is not $2\,T(\mathbf{v}) = (4, 2)$.

(c) Not linear: $T(\mathbf{0}) = (1, 0) \ne \mathbf{0}$.

Check (a) at $\mathbf{u} = (1, 0)$, $\mathbf{v} = (0, 1)$: $T(\mathbf{u} + \mathbf{v}) = T(1, 1) = (1, 4)$ and $T(\mathbf{u}) + T(\mathbf{v}) = (2, 1) + (-1, 3) = (1, 4)$.

</details>

2\. Find the standard matrix of $T \colon \mathbb{R}^2 \to \mathbb{R}^3$ with $T(x, y) = (x + y,\; 2x,\; -y)$ and use it to compute $T(3, -2)$.

<details class="solution" markdown>
<summary>Solution</summary>

$T(\mathbf{e}_1) = (1, 2, 0)$ and $T(\mathbf{e}_2) = (1, 0, -1)$ are the columns, so $A = \begin{pmatrix} 1 & 1 \\ 2 & 0 \\ 0 & -1 \end{pmatrix}$, a $3 \times 2$ matrix. Then $A\begin{pmatrix} 3 \\ -2 \end{pmatrix} = \begin{pmatrix} 3 - 2 \\ 6 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 \\ 6 \\ 2 \end{pmatrix}$.

Check: the formula gives $T(3, -2) = (3 - 2,\; 6,\; 2) = (1, 6, 2)$.

</details>

3\. Find the kernel and the image of $A = \begin{pmatrix} 1 & -1 \\ 2 & -2 \end{pmatrix}$ and say whether $\mathbf{x} \mapsto A\mathbf{x}$ is injective.

<details class="solution" markdown>
<summary>Solution</summary>

$A\mathbf{x} = \mathbf{0}$ means $x - y = 0$ (twice, as the second row is twice the first), so the kernel is $\{t(1, 1)\}$, the line $y = x$. Both columns are multiples of $(1, 2)$, since $(-1, -2) = -1 \cdot (1, 2)$, so the image is the line spanned by $(1, 2)$. The kernel is not $\{\mathbf{0}\}$, so the map is not injective.

Check: $A(1, 1) = (0, 0)$, and rank-nullity gives $1 + 1 = 2$ columns.

</details>

### Standard

4\. Find the matrix of the map "shear $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ first, then reflect in the $x$-axis", and of the map "reflect first, then shear". Are they equal?

<details class="solution" markdown>
<summary>Solution</summary>

With $F = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, "shear then reflect" is $FS = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix}$. "Reflect then shear" is $SF = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 0 & -1 \end{pmatrix}$. They differ in the top right entry, so the two orders are different maps.

Check with $\mathbf{x} = (0, 1)$: shear gives $(1, 1)$ and reflection gives $(1, -1)$, and $FS\mathbf{x}$ is the second column $(1, -1)$. Reflection first gives $(0, -1)$ and the shear gives $(-1, -1)$, the second column of $SF$.

</details>

5\. (a) A linear map $T \colon \mathbb{R}^5 \to \mathbb{R}^3$ is surjective. Find its nullity. (b) A $4 \times 6$ matrix has rank 3. Find the dimensions of its kernel and image, and say whether $\mathbf{x} \mapsto A\mathbf{x}$ is injective, surjective, both or neither. (c) Can a linear map $\mathbb{R}^2 \to \mathbb{R}^3$ be surjective?

<details class="solution" markdown>
<summary>Solution</summary>

(a) Surjective means the image is all of $\mathbb{R}^3$, so the rank is 3, and the nullity is $5 - 3 = 2$.

(b) The kernel is in $\mathbb{R}^6$ and has dimension $6 - 3 = 3$; the image is in $\mathbb{R}^4$ and has dimension 3. The nullity is not 0, so the map is not injective, and the rank is $3 < 4$, so it is not surjective. Neither.

(c) No. The rank is at most the number of inputs, $2$, and surjective needs rank 3.

Check (a): the nullity plus the rank is $2 + 3 = 5$. Check (b): $3 + 3 = 6$ columns.

</details>

6\. Let $T$ be an injective linear map and let $\mathbf{v}_1, \dots, \mathbf{v}_k$ be linearly independent. Prove that $T(\mathbf{v}_1), \dots, T(\mathbf{v}_k)$ are linearly independent.

<details class="solution" markdown>
<summary>Solution</summary>

We know $T$ is injective (so its kernel is $\{\mathbf{0}\}$ by Theorem 3) and the $\mathbf{v}_i$ are independent. We want to show that the only solution of $c_1 T(\mathbf{v}_1) + \dots + c_k T(\mathbf{v}_k) = \mathbf{0}$ is $c_1 = \dots = c_k = 0$. The plan is to pull $T$ out by linearity.

Suppose $c_1 T(\mathbf{v}_1) + \dots + c_k T(\mathbf{v}_k) = \mathbf{0}$. By linearity, $T(c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k) = \mathbf{0}$, so $c_1\mathbf{v}_1 + \dots + c_k\mathbf{v}_k$ is in the kernel, so it equals $\mathbf{0}$. The $\mathbf{v}_i$ are independent, so every $c_i = 0$. $\blacksquare$

Check with a map that isn't injective: $T(x, y) = x$ sends the independent vectors $(1, 0)$ and $(1, 1)$ to $1$ and $1$, which are dependent. The hypothesis is needed.

</details>

### Challenge

7\. Let $T \colon \mathbb{R}^n \to \mathbb{R}^m$ and $S \colon \mathbb{R}^m \to \mathbb{R}^p$ be linear. (a) Prove that $\ker T \subseteq \ker(S \circ T)$. (b) Prove that if $S \circ T$ is injective then $T$ is injective. (c) Give an example in which $S \circ T$ is injective and $S$ is not.

<details class="solution" markdown>
<summary>Solution</summary>

(a) If $\mathbf{x}$ is in $\ker T$ then $(S \circ T)(\mathbf{x}) = S(\mathbf{0}) = \mathbf{0}$, so $\mathbf{x}$ is in $\ker(S \circ T)$.

(b) If $S \circ T$ is injective, its kernel is $\{\mathbf{0}\}$ (Theorem 3), and by (a) $\ker T$ sits inside it, so $\ker T = \{\mathbf{0}\}$ and $T$ is injective.

(c) Let $T \colon \mathbb{R} \to \mathbb{R}^2$ with $T(x) = (x, 0)$ and $S \colon \mathbb{R}^2 \to \mathbb{R}$ with $S(x, y) = x$. Then $S \circ T$ is the identity on $\mathbb{R}$, which is injective, while $S(0, 1) = 0$ puts a nonzero vector in $\ker S$.

Check (c): the matrices are $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \end{pmatrix}$, and the product $\begin{pmatrix} 1 & 0 \end{pmatrix}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = (1)$.

</details>

8\. (Reviews [injective, surjective and bijective](../../04-proofs-and-logic/06-relations-and-functions/05-injective-surjective-bijective.md).) Let $T(x, y) = (x, y, x + y)$ from $\mathbb{R}^2$ to $\mathbb{R}^3$. (a) Prove that $T$ is injective using the template from that lesson (assume $T(\mathbf{a}) = T(\mathbf{a}')$ and show $\mathbf{a} = \mathbf{a}'$). (b) Show that $T$ is not surjective by exhibiting a vector with no input. (c) Describe the image as a plane and check rank-nullity.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Suppose $T(a_1, a_2) = T(a_1', a_2')$, so $(a_1, a_2, a_1 + a_2) = (a_1', a_2', a_1' + a_2')$. Comparing the first two entries gives $a_1 = a_1'$ and $a_2 = a_2'$, so the inputs are equal.

(b) The vector $(0, 0, 1)$ has no input: it would need $x = 0$, $y = 0$ and $x + y = 1$.

(c) The outputs are $(x, y, x + y)$, which satisfy $z = x + y$, so the image is the plane $x + y - z = 0$. It has dimension 2 and is spanned by the columns $(1, 0, 1)$ and $(0, 1, 1)$. The kernel is $\{\mathbf{0}\}$, with dimension 0, and $0 + 2 = 2$ inputs.

Check: $(0, 0, 1)$ is not on the plane, since $0 + 0 - 1 \ne 0$, which agrees with (b).

</details>

## Where this shows up

- The next lesson, [determinants](06-determinants.md), measures how much a square matrix scales area, and the lessons after it use the kernel (the eigenvectors of eigenvalue 0 are the kernel) and the image (least squares projects onto the image of $A$) in [orthogonality, projections and least squares](07-orthogonality-projections-and-least-squares.md) and [eigenvalues and eigenvectors](08-eigenvalues-and-eigenvectors.md).
- In calculus, the derivative of a function of several variables is a linear map, the one that best approximates the function near a point, the many-variable version of [linear approximation](../03-applications-of-derivatives/02-linear-approximation-and-lhopitals-rule.md). See Partial derivatives and the gradient<!-- link: ../09-multivariable-calculus-light/02-partial-derivatives-and-the-gradient.md -->.
- In CS, graphics pipelines are products of linear and homogeneous-coordinate matrices, and a neural network layer is a linear map followed by a translation and a nonlinear function. Without the nonlinear functions, stacked layers collapse to a single matrix, as the code above shows.
- In economics, input-output tables are linear maps from gross output to net output, and the Leontief inverse in Example 4 says how much total output a unit of final demand needs.
