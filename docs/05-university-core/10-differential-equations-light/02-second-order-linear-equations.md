# Second-order linear equations

This lesson is optional. It is for readers who want to see oscillation and damping, or who want the link between differential equations and the eigenvalues and recurrences of other chapters.

After this lesson you can solve $y'' + by' + cy = 0$ with the characteristic equation in each of its three cases, classify a spring-mass system as underdamped, critically damped or overdamped, solve a forced equation with a steady forcing term, solve a two-variable system $\mathbf{x}' = A\mathbf{x}$ with eigenvalues, and read stability from the roots.

Before this: [first-order differential equations](01-first-order-differential-equations.md), [eigenvalues and eigenvectors](../06-linear-algebra/08-eigenvalues-and-eigenvectors.md) and [complex numbers](../../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $y'' - 5y' + 6y = 0$.
2. Find the roots of the characteristic equation of $y'' + 4y' + 4y = 0$.
3. Find the roots of the characteristic equation of $y'' + 2y' + 5y = 0$.

<details class="solution" markdown>
<summary>Answers</summary>

1. The characteristic equation $r^2 - 5r + 6 = (r - 2)(r - 3) = 0$ has roots $2$ and $3$, so $y = C_1e^{2t} + C_2e^{3t}$.
2. $r^2 + 4r + 4 = (r + 2)^2 = 0$, so $r = -2$ twice.
3. $r = \frac{-2 \pm \sqrt{4 - 20}}{2} = -1 \pm 2i$.

</details>

## The idea

A mass hangs on a spring. Pull it down and let go, and it bobs up and down. Newton's second law says that mass times acceleration equals the total force. The spring pulls back with a force proportional to the displacement, $-kx$, and friction in the air or a shock absorber opposes the velocity, $-\gamma x'$. So

$$
mx'' = -kx - \gamma x', \qquad\text{that is,}\qquad mx'' + \gamma x' + kx = 0.
$$

This is a **second-order** equation, because it has the second derivative. The motion depends on how strong the friction is. With none the mass oscillates forever. With a little, it oscillates with shrinking swings, like a car on worn shocks. With a lot it creeps back to rest without crossing it, like a door with a hydraulic closer.

Whether the motion oscillates comes down to a quadratic equation. Try $x = e^{rt}$. The derivatives are $re^{rt}$ and $r^2e^{rt}$, and the equation becomes $(mr^2 + \gamma r + k)e^{rt} = 0$, an ordinary quadratic in $r$. Real roots give exponentials. Complex roots give oscillations, through Euler's formula $e^{i\beta t} = \cos\beta t + i\sin\beta t$. So the three cases of the quadratic formula (two real roots, one repeated root, a complex pair) are the three kinds of motion, and the figure below shows them.

![Displacement against time for three springs started at x = 1 with zero velocity. The green underdamped curve oscillates, crossing zero near t = 1.02, dipping to about minus 0.2 near t = 1.6 and then settling, inside dashed envelope curves plus and minus 1.118 e to the minus t. The red critically damped curve falls smoothly with no oscillation. The blue overdamped curve also falls smoothly and without crossing zero.](../../assets/figures/05-university-core/second-order-linear-equations-damping.svg)

## Definitions

A **second-order linear differential equation with constant coefficients** is

$$
y'' + by' + cy = g(t),
$$

where $b$ and $c$ are constants and $g$ is a given function. It is **homogeneous** if $g = 0$. Dividing the spring equation by $m$ puts it in this form with $b = \frac{\gamma}{m}$ and $c = \frac{k}{m}$. In plain words, the equation is linear because $y$, $y'$ and $y''$ appear only to the first power and are only multiplied by constants.

The **characteristic equation** of the homogeneous equation $y'' + by' + cy = 0$ is

$$
r^2 + br + c = 0.
$$

In plain words, it is what you get by putting $y = e^{rt}$ into the equation and dividing by $e^{rt}$.

The **general solution** is a family of solutions with two arbitrary constants, such as $C_1y_1 + C_2y_2$. An **initial value problem** for a second-order equation gives two conditions, the position and the velocity, $y(t_0) = a$ and $y'(t_0) = a'$, which fix the two constants. Two solutions are **independent** if neither is a constant multiple of the other.

For the spring $x'' + bx' + cx = 0$ with $b, c > 0$, the motion is **underdamped** if $b^2 - 4c < 0$, **critically damped** if $b^2 - 4c = 0$ and **overdamped** if $b^2 - 4c > 0$. In plain words, the sign of the discriminant of the characteristic equation tells you whether the friction is weak, just right or strong.

## How to do it

### Solving the homogeneous equation

1. Write the characteristic equation $r^2 + br + c = 0$ and find its roots with the quadratic formula.
2. Choose the form of the solution from the roots, using the table.
3. Use the two initial conditions $y(0)$ and $y'(0)$ to find $C_1$ and $C_2$: differentiate the general solution, put in $t = 0$ and solve the two linear equations.
4. Check that the answer satisfies the equation (or at least both initial conditions).

| Roots of $r^2 + br + c = 0$ | General solution |
|---|---|
| distinct real $r_1 \ne r_2$ | $C_1e^{r_1t} + C_2e^{r_2t}$ |
| one repeated real root $r$ | $(C_1 + C_2t)e^{rt}$ |
| complex pair $\alpha \pm i\beta$ with $\beta > 0$ | $e^{\alpha t}\left(C_1\cos\beta t + C_2\sin\beta t\right)$ |

### Why the table is right

*Theorem 1 (superposition).* If $y_1$ and $y_2$ solve the homogeneous equation, so does $C_1y_1 + C_2y_2$ for all constants $C_1, C_2$.

*Proof.* Write $L[y] = y'' + by' + cy$. Derivatives are linear, so $L[C_1y_1 + C_2y_2] = C_1L[y_1] + C_2L[y_2] = 0$. $\blacksquare$

*Theorem 2 (the characteristic equation).* The function $e^{rt}$ solves $y'' + by' + cy = 0$ if and only if $r^2 + br + c = 0$.

*Proof.* With $y = e^{rt}$, $L[y] = (r^2 + br + c)e^{rt}$, and $e^{rt} \ne 0$. $\blacksquare$

What remains is to show that the table lists all the solutions. We use one fact, stated without proof: for each $a$ and $a'$ the initial value problem $y(0) = a$, $y'(0) = a'$ has exactly one solution, on the whole line. So it is enough to show that the formulas in the table can match any $a$ and $a'$.

*Distinct real roots.* By Theorem 2 both exponentials are solutions, and by Theorem 1 so is $y = C_1e^{r_1t} + C_2e^{r_2t}$. The conditions are $C_1 + C_2 = a$ and $r_1C_1 + r_2C_2 = a'$, a linear system whose determinant is $r_2 - r_1 \ne 0$. By the [determinants lesson](../06-linear-algebra/06-determinants.md) it has exactly one solution for every $a$ and $a'$.

*A repeated root.* Here $r = -\frac{b}{2}$ and $c = \frac{b^2}{4}$. Theorem 2 gives $e^{rt}$. To check that $te^{rt}$ is a solution, compute $y' = (1 + rt)e^{rt}$ and $y'' = (2r + r^2t)e^{rt}$. Then

$$
y'' + by' + cy = e^{rt}\left[t(r^2 + br + c) + (2r + b)\right] = 0,
$$

because $r^2 + br + c = 0$ and $2r + b = 0$ for the double root. The conditions are $C_1 = a$ and $rC_1 + C_2 = a'$, which can always be solved.

*Complex roots.* The complex function $e^{(\alpha + i\beta)t} = e^{\alpha t}(\cos\beta t + i\sin\beta t)$ solves the equation (Theorem 2 holds for complex $r$). Write it as $u + iv$ with $u = e^{\alpha t}\cos\beta t$ and $v = e^{\alpha t}\sin\beta t$. Since $b$ and $c$ are real, $L[u + iv] = L[u] + iL[v] = 0$ with $L[u]$ and $L[v]$ real, so both are zero: $u$ and $v$ are real solutions. The conditions are $C_1 = a$ and $\alpha C_1 + \beta C_2 = a'$, solvable because $\beta \ne 0$. $\blacksquare$

Look back: the three cases are the three cases of the quadratic formula, and each was shown to match every starting position and velocity, so nothing is missing. In the complex case, $C_1\cos\beta t + C_2\sin\beta t = R\cos(\beta t - \varphi)$ with $R = \sqrt{C_1^2 + C_2^2}$, a wave of angular frequency $\beta$ (period $\frac{2\pi}{\beta}$) inside the envelope $\pm Re^{\alpha t}$.

### The link to eigenvalues and recurrences

Put $\mathbf{x} = \begin{pmatrix} y \\ y' \end{pmatrix}$. Then $y'' = -cy - by'$ turns the equation into the system

$$
\mathbf{x}' = A\mathbf{x}, \qquad A = \begin{pmatrix} 0 & 1 \\ -c & -b \end{pmatrix}.
$$

The characteristic polynomial of $A$ is $\det(A - \lambda I) = \lambda(\lambda + b) + c = \lambda^2 + b\lambda + c$, the same polynomial. The roots of the characteristic equation are the eigenvalues of this matrix. This is the idea of the next section, and the reason the eigenvalue lesson mentioned this one.

The same polynomial appears for recurrences. The recurrence $a_{n+2} + ba_{n+1} + ca_n = 0$ has the solutions $a_n = r^n$, where $r^2 + br + c = 0$, and the same three cases. Recurrences<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md --> solves the Fibonacci numbers this way, and Binet's formula of the eigenvalue lesson is the same answer. The differential equation uses $e^{rt}$ where the recurrence uses $r^n$: continuous time against steps.

### Forcing

If the right side is not $0$, $y'' + by' + cy = g(t)$, the general solution is the sum of one particular solution $y_p$ and the general solution of the homogeneous equation. The reason: if $y_p$ is any solution, then $y - y_p$ solves the homogeneous equation. To find $y_p$ for a simple $g$, guess a function of the same type (the method of undetermined coefficients): a constant for a constant $g$, and $A\cos\omega t + B\sin\omega t$ for $g = \cos\omega t$.

For a stable system the homogeneous part dies out (it is the transient), and what remains is $y_p$, the steady state. If the forcing has the same frequency as the system's natural oscillation, there is **resonance**. For the undamped equation $y'' + \omega_0^2y = \cos\omega_0t$, the solution $y_p = \frac{t}{2\omega_0}\sin\omega_0t$ grows without bound: a small push at the right rhythm builds a large swing. (Check: $y_p'' = \cos\omega_0t - \frac{\omega_0t}{2}\sin\omega_0t$, so $y_p'' + \omega_0^2y_p = \cos\omega_0t$.)

### Systems and stability

*Theorem 3.* If $A$ is a $2 \times 2$ matrix with eigenvalues $\lambda_1 \ne \lambda_2$ and eigenvectors $\mathbf{v}_1$, $\mathbf{v}_2$, then $\mathbf{x}(t) = c_1e^{\lambda_1t}\mathbf{v}_1 + c_2e^{\lambda_2t}\mathbf{v}_2$ solves $\mathbf{x}' = A\mathbf{x}$, and the constants can be chosen to match any $\mathbf{x}(0)$.

*Proof.* Differentiating, $\mathbf{x}' = c_1\lambda_1e^{\lambda_1t}\mathbf{v}_1 + c_2\lambda_2e^{\lambda_2t}\mathbf{v}_2$, and $A\mathbf{x} = c_1e^{\lambda_1t}A\mathbf{v}_1 + c_2e^{\lambda_2t}A\mathbf{v}_2$, which is the same because $A\mathbf{v}_i = \lambda_i\mathbf{v}_i$. At $t = 0$, $\mathbf{x}(0) = c_1\mathbf{v}_1 + c_2\mathbf{v}_2$, and since the eigenvectors are independent (Theorem 3 of the eigenvalue lesson) every starting vector is such a combination. $\blacksquare$

Look back: the eigenvector directions are the special solutions that stay on a line: each is multiplied by $e^{\lambda t}$ as time passes. For a real pair of eigenvalues this is the picture of the figure below. For complex eigenvalues $\alpha \pm i\beta$ the solutions rotate while growing or shrinking by $e^{\alpha t}$.

The signs of the eigenvalues (or of the roots in the second-order case) say what the system does in the long run.

| Eigenvalues | Long-run behaviour |
|---|---|
| both real and negative | every solution decays to $\mathbf{0}$ (stable) |
| both real and positive | every solution grows (unstable) |
| real, one positive and one negative | a saddle: a solution decays only if it starts on the eigenvector of the negative one, and otherwise it grows |
| complex $\alpha \pm i\beta$ with $\alpha < 0$ | spirals in toward $\mathbf{0}$ (stable) |
| complex with $\alpha > 0$ | spirals out (unstable) |
| complex with $\alpha = 0$ | circles forever |

For the equation $y'' + by' + cy = 0$ with $b, c > 0$ both roots (or both real parts) are negative, so every solution decays. That is why friction makes a spring settle (Practice problem 7 proves it).

![A phase portrait in the (x1, x2) plane for the system with matrix rows (1, 2) and (3, 0): grey flow lines curving around the origin in a saddle pattern. A red line along (1, 1) marks the eigenvalue 3, along which solutions move away from the origin. A green line along (2, minus 3) marks the eigenvalue minus 2, along which solutions move toward the origin. A dark curve through (2, minus 0.5) comes in close to the green line and then leaves along the red line.](../../assets/figures/05-university-core/second-order-linear-equations-saddle.svg)

## Worked examples

<div class="example" markdown>

### Example 1: distinct real roots

Solve $y'' - y' - 6y = 0$ with $y(0) = 1$ and $y'(0) = 2$.

Step 1: the characteristic equation is $r^2 - r - 6 = (r - 3)(r + 2) = 0$, so $r = 3$ and $r = -2$. Step 2: the roots are real and distinct, so $y = C_1e^{3t} + C_2e^{-2t}$.

Step 3: $y' = 3C_1e^{3t} - 2C_2e^{-2t}$, so the conditions are $C_1 + C_2 = 1$ and $3C_1 - 2C_2 = 2$. Adding twice the first to the second gives $5C_1 = 4$, so $C_1 = 0.8$ and $C_2 = 0.2$. The solution is $y = 0.8e^{3t} + 0.2e^{-2t}$.

Step 4, the check: $y' = 2.4e^{3t} - 0.4e^{-2t}$, which is $2.4 - 0.4 = 2$ at $t = 0$. Also $y'' = 7.2e^{3t} + 0.8e^{-2t}$, and $y'' - y' - 6y = (7.2 - 2.4 - 4.8)e^{3t} + (0.8 + 0.4 - 1.2)e^{-2t} = 0$. The growing root $3$ wins in the long run, so this solution blows up.

</div>

<div class="example" markdown>

### Example 2: a repeated root

Solve $y'' + 6y' + 9y = 0$ with $y(0) = 2$ and $y'(0) = -1$.

The characteristic equation is $(r + 3)^2 = 0$, so $r = -3$ twice and $y = (C_1 + C_2t)e^{-3t}$. Then $y' = \left(C_2 - 3C_1 - 3C_2t\right)e^{-3t}$. The conditions are $C_1 = 2$ and $C_2 - 3C_1 = -1$, so $C_2 = 5$. The solution is $y = (2 + 5t)e^{-3t}$.

Check: $y' = (5 - 6 - 15t)e^{-3t} = (-1 - 15t)e^{-3t}$, which is $-1$ at $t = 0$ and negative for all $t \ge 0$. So the solution falls steadily from 2 toward $0$, never crossing it.

</div>

<div class="example" markdown>

### Example 3: three springs, one mass

A mass of 1 kg is pulled to $x = 1$ and released from rest, so $x(0) = 1$ and $x'(0) = 0$. Solve $x'' + \gamma x' + kx = 0$ for (a) $\gamma = 2$, $k = 5$, (b) $\gamma = 2$, $k = 1$ and (c) $\gamma = 5$, $k = 4$.

(a) The characteristic equation $r^2 + 2r + 5 = 0$ has the discriminant $4 - 20 = -16 < 0$, so it is underdamped, with $r = -1 \pm 2i$. Then $x = e^{-t}(C_1\cos 2t + C_2\sin 2t)$, and the conditions give $C_1 = 1$ and $-C_1 + 2C_2 = 0$, so $C_2 = 0.5$:

$$
x = e^{-t}\left(\cos 2t + 0.5\sin 2t\right).
$$

The mass crosses $x = 0$ at $t \approx 1.017$ (where $\tan 2t = -2$), swings to about $-0.21$ (at $t = \frac{\pi}{2}$) and settles. The period of the oscillation is $\frac{2\pi}{2} = \pi \approx 3.14$, and the swings are inside the envelope $\sqrt{1.25}\,e^{-t} = 1.118e^{-t}$.

(b) $r^2 + 2r + 1 = (r + 1)^2$, so it is critically damped, with $r = -1$ twice. Then $x = (C_1 + C_2t)e^{-t}$, with $C_1 = 1$ and $-C_1 + C_2 = 0$, so $x = (1 + t)e^{-t}$. It never crosses zero.

(c) $r^2 + 5r + 4 = (r + 1)(r + 4)$, so it is overdamped, with $r = -1$ and $r = -4$. Then $x = C_1e^{-t} + C_2e^{-4t}$, with $C_1 + C_2 = 1$ and $-C_1 - 4C_2 = 0$, so $C_1 = \frac{4}{3}$ and $C_2 = -\frac{1}{3}$:

$$
x = \frac{4e^{-t} - e^{-4t}}{3}.
$$

Check: at $t = 1$ the three formulas give $0.0142$, $0.7358$ and $0.4844$, and a numerical solution of the equations (in the "In code" section) gives the same values. With no friction at all ($\gamma = 0$) and $k = 4$, the motion would be $\cos 2t$ forever.

</div>

<div class="example" markdown>

### Example 4: a forced equation

Solve $y'' + 3y' + 2y = 10\cos t$ with $y(0) = 0$ and $y'(0) = 0$.

The homogeneous equation has $r^2 + 3r + 2 = (r + 1)(r + 2)$, so $y_h = C_1e^{-t} + C_2e^{-2t}$. For a particular solution try $y_p = A\cos t + B\sin t$. Then $y_p' = -A\sin t + B\cos t$ and $y_p'' = -A\cos t - B\sin t$, and

$$
y_p'' + 3y_p' + 2y_p = (A + 3B)\cos t + (B - 3A)\sin t.
$$

Matching $10\cos t$ gives $A + 3B = 10$ and $B - 3A = 0$. So $B = 3A$, $10A = 10$, $A = 1$ and $B = 3$: $y_p = \cos t + 3\sin t$.

The general solution is $y = \cos t + 3\sin t + C_1e^{-t} + C_2e^{-2t}$. The conditions are $y(0) = 1 + C_1 + C_2 = 0$ and $y'(0) = 3 - C_1 - 2C_2 = 0$. Adding them, $4 - C_2 = 0$, so $C_2 = 4$ and $C_1 = -5$:

$$
y = \cos t + 3\sin t - 5e^{-t} + 4e^{-2t}.
$$

Check: $y(0) = 1 - 5 + 4 = 0$ and $y'(0) = 3 + 5 - 8 = 0$. The exponential terms die away, so $y$ settles into the steady oscillation $\cos t + 3\sin t$, with amplitude $\sqrt{10} \approx 3.16$. At $t = 2$ the formula gives $1.7083$, and a numerical solution agrees (below).

</div>

<div class="example" markdown>

### Example 5: a system with a saddle

Solve $\mathbf{x}' = A\mathbf{x}$ with $A = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$ and $\mathbf{x}(0) = (2, -0.5)$.

The trace is $1$ and the determinant is $-6$, so $\lambda^2 - \lambda - 6 = (\lambda - 3)(\lambda + 2)$ and the eigenvalues are $3$ and $-2$. For $\lambda = 3$: $A - 3I = \begin{pmatrix} -2 & 2 \\ 3 & -3 \end{pmatrix}$ gives $\mathbf{v}_1 = (1, 1)$. For $\lambda = -2$: $A + 2I = \begin{pmatrix} 3 & 2 \\ 3 & 2 \end{pmatrix}$ gives $\mathbf{v}_2 = (2, -3)$, or $(1, -1.5)$.

Write $(2, -0.5) = c_1(1, 1) + c_2(1, -1.5)$. Then $c_1 + c_2 = 2$ and $c_1 - 1.5c_2 = -0.5$, so $2.5c_2 = 2.5$, $c_2 = 1$ and $c_1 = 1$. Therefore

$$
\mathbf{x}(t) = e^{3t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + e^{-2t}\begin{pmatrix} 1 \\ -1.5 \end{pmatrix}.
$$

Check: $A(1, -1.5) = (1 - 3, 3) = (-2, 3) = -2(1, -1.5)$ and $A(1, 1) = (3, 3)$. At $t = 0$ the sum is $(2, -0.5)$. The eigenvalues have opposite signs, so the origin is a saddle (the figure): the solution first approaches the line of $\mathbf{v}_2$, and then the growing $e^{3t}$ term takes over and it leaves along $(1, 1)$. Only a start exactly on the line of $\mathbf{v}_2$ goes to the origin.

</div>

<div class="example" markdown>

### Example 6: an oscillating economy (finish it yourself)

In a hypothetical model, the gap of output from its trend obeys $y'' + 0.4y' + 1.04y = 0$ (time in years), with $y(0) = 1$ and $y'(0) = 0$. Find $y(t)$, the period of the cycle, and how long the amplitude takes to halve.

The roots are $r = \frac{-0.4 \pm \sqrt{0.16 - 4.16}}{2} = -0.2 \pm i$, so $y = e^{-0.2t}(C_1\cos t + C_2\sin t)$.

<details class="solution" markdown>
<summary>Finish</summary>

The conditions give $C_1 = 1$ and $-0.2C_1 + C_2 = 0$, so $C_2 = 0.2$: $y = e^{-0.2t}(\cos t + 0.2\sin t)$. The angular frequency is $1$, so the period is $2\pi \approx 6.28$ years. The amplitude shrinks like $e^{-0.2t}$, and it halves when $e^{-0.2t} = \frac{1}{2}$, at $t = \frac{\ln 2}{0.2} \approx 3.47$ years.

Check: $y' = e^{-0.2t}\left(-0.2\cos t - 0.04\sin t - \sin t + 0.2\cos t\right) = -1.04\,e^{-0.2t}\sin t$, which is $0$ at $t = 0$. The cycle fades but returns: at $t = \pi$, $y = -e^{-0.2\pi} = -0.5335$, so the economy swings from above trend to about half as far below trend. The numbers are made up to show the method.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: using only one constant, or solving for the constants from one condition. A second-order equation needs two initial conditions, and the solution has two constants. With $y(0)$ alone, a whole family of solutions fits.

</div>

<div class="warning" markdown>

Watch out: the repeated root has the factor $t$. For a double root $r$ the solutions are $e^{rt}$ and $te^{rt}$, and writing $(C_1 + C_2)e^{rt}$ is a single constant in disguise. It can't match two initial conditions.

</div>

<div class="warning" markdown>

Watch out: dropping the real part in the complex case. For $r = -1 \pm 2i$ the solution is $e^{-t}(C_1\cos 2t + C_2\sin 2t)$, with the factor $e^{-t}$ from the real part. The imaginary part is the frequency and the real part is the growth or decay. Writing $C_1\cos 2t + C_2\sin 2t$ gives an oscillation that never fades.

</div>

<div class="warning" markdown>

Watch out: the sign of $b$ in the characteristic equation. For $y'' + by' + cy = 0$ it is $r^2 + br + c$, with plus signs, and for $y'' - 5y' + 6y = 0$ it is $r^2 - 5r + 6$. A common slip is $r^2 + 5r + 6$, which has the roots $-2$ and $-3$ instead of $2$ and $3$.

</div>

<div class="warning" markdown>

Watch out: the particular solution must be added to the general solution of the homogeneous equation, and the constants are found at the end. If you fit $y(0)$ and $y'(0)$ to $y_h$ alone, then add $y_p$, the conditions fail (in Example 4, $y_p(0) = 1$ is not $0$).

</div>

<div class="warning" markdown>

Watch out: guessing a particular solution that is already a solution of the homogeneous equation. If $g = e^{-t}$ in Example 4, the guess $Ae^{-t}$ gives $0$ on the left side and can't work. Multiply the guess by $t$, as with the repeated root and resonance.

</div>

## Tricks and shortcuts

For $y'' + by' + cy = 0$ the roots add to $-b$ and multiply to $c$, so you can often find them by inspection: for $r^2 - 5r + 6$, look for two numbers with sum $5$ and product $6$. A quick test of the discriminant $b^2 - 4c$ decides the case before you solve anything.

For a complex pair, the real part is $-\frac{b}{2}$ and the frequency is $\beta = \sqrt{c - \frac{b^2}{4}}$. In Example 3(a), $-\frac{b}{2} = -1$ and $\beta = \sqrt{5 - 1} = 2$.

A system or equation is stable exactly when all the roots or eigenvalues have negative real part. For $y'' + by' + cy = 0$ this holds exactly when $b > 0$ and $c > 0$ (Practice problem 7). So you can read stability from the signs of the coefficients, without solving.

A constant forcing $g = K$ has the particular solution $y_p = \frac{K}{c}$ when $c \ne 0$, the equilibrium: put $y' = y'' = 0$ into the equation.

## In code

A numerical solver (fourth-order Runge-Kutta, a more accurate relative of Euler's method) checks the three springs of Example 3, the forced solution of Example 4 and the system of Example 5. NumPy finds the roots and eigenvalues.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
import numpy as np

# Characteristic roots of x'' + g x' + k x = 0 for three dampings (mass 1).
for name, g, k in [("under", 2, 5), ("critical", 2, 1), ("over", 5, 4)]:
    print(name, np.round(np.roots([1, g, k]), 4), g * g - 4 * k)
# under [-1.+2.j -1.-2.j] -16
# critical [-1. -1.] 0
# over [-4. -1.] 9

def rk4(f, y, t_end, h):
    """Fourth-order Runge-Kutta for a system y' = f(t, y), y a NumPy vector."""
    t = 0.0
    for _ in range(round(t_end / h)):
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h / 2 * k1)
        k3 = f(t + h / 2, y + h / 2 * k2)
        k4 = f(t + h, y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return y

def spring(g, k):
    return lambda t, y: np.array([y[1], -k * y[0] - g * y[1]])   # y = (x, x')

exact = {
    "under": lambda t: math.exp(-t) * (math.cos(2 * t) + 0.5 * math.sin(2 * t)),
    "critical": lambda t: (1 + t) * math.exp(-t),
    "over": lambda t: (4 * math.exp(-t) - math.exp(-4 * t)) / 3,
}
for name, g, k in [("under", 2, 5), ("critical", 2, 1), ("over", 5, 4)]:
    num = rk4(spring(g, k), np.array([1.0, 0.0]), 1.0, 0.001)[0]
    print(name, round(num, 5), round(exact[name](1.0), 5))
# under 0.01416 0.01416
# critical 0.73576 0.73576
# over 0.4844 0.4844

# Forced equation y'' + 3y' + 2y = 10 cos t, y(0) = y'(0) = 0, against the formula of Example 4.
forced = lambda t, y: np.array([y[1], 10 * math.cos(t) - 3 * y[1] - 2 * y[0]])
y2 = rk4(forced, np.array([0.0, 0.0]), 2.0, 0.001)[0]
formula = lambda t: math.cos(t) + 3 * math.sin(t) - 5 * math.exp(-t) + 4 * math.exp(-2 * t)
print(round(y2, 5), round(formula(2.0), 5))
# 1.70833 1.70833

# The system x' = A x with A = [[1, 2], [3, 0]] and x(0) = (2, -0.5), solved at t = 1.
A = np.array([[1.0, 2.0], [3.0, 0.0]])
print(np.round(np.sort(np.linalg.eigvals(A).real), 4))
# [-2.  3.]
x1 = rk4(lambda t, x: A @ x, np.array([2.0, -0.5]), 1.0, 0.0001)
print(np.round(x1, 3), np.round(math.exp(3) * np.array([1, 1]) + math.exp(-2) * np.array([1, -1.5]), 3))
# [20.221 19.883] [20.221 19.883]
```

The roots of the characteristic polynomial are the same numbers as the eigenvalues of the matrix $A = \begin{pmatrix} 0 & 1 \\ -c & -b \end{pmatrix}$, which you can check with `np.linalg.eigvals`.

</details>

## FAQ

### Why try $e^{rt}$?

Because the derivative of an exponential is a multiple of itself, so substituting it turns the differential equation into an algebraic one with the factor $e^{rt}$ cancelled. It is the same idea as in the first-order case, where $y' = ky$ has the solution $e^{kt}$. For a constant-coefficient linear equation the exponentials are the natural building blocks, and the characteristic equation finds the exponents.

### Why do complex roots give sines and cosines?

Because $e^{i\beta t} = \cos\beta t + i\sin\beta t$ (Euler's formula), so a complex exponent is a rotation. The solution $e^{(\alpha + i\beta)t}$ is a number of size $e^{\alpha t}$ that rotates at rate $\beta$. The real equation has real solutions, which are the real and imaginary parts, $e^{\alpha t}\cos\beta t$ and $e^{\alpha t}\sin\beta t$.

### What about equations with $y'''$ or variable coefficients?

The characteristic method extends to higher orders: a constant-coefficient equation of order $n$ has an $n$-th degree characteristic polynomial, and each root gives a solution in the same way. Equations with variable coefficients, such as $y'' + ty = 0$, usually have no formula, and are solved numerically or with series, which is a second course.

### Is a repeated root a rare case?

It is a boundary between the other two: it happens only when the discriminant is exactly $0$. In a real system the parameters are never exact, which is why critical damping is a design target (a door closer is tuned toward it) rather than something you find by chance.

## Practice

### Warm-up

1\. Solve $y'' - 5y' + 6y = 0$ with $y(0) = 1$ and $y'(0) = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

The roots are $2$ and $3$, so $y = C_1e^{2t} + C_2e^{3t}$. The conditions are $C_1 + C_2 = 1$ and $2C_1 + 3C_2 = 0$. So $C_2 = -2$ and $C_1 = 3$, and $y = 3e^{2t} - 2e^{3t}$.

Check: $y'(0) = 6 - 6 = 0$ and $y(0) = 3 - 2 = 1$.

</details>

2\. Solve $y'' + 4y = 0$ with $y(0) = 3$ and $y'(0) = 4$. Give the amplitude and the period.

<details class="solution" markdown>
<summary>Solution</summary>

The roots are $r = \pm 2i$, so $\alpha = 0$ and $\beta = 2$, and $y = C_1\cos 2t + C_2\sin 2t$. Then $y(0) = C_1 = 3$ and $y'(0) = 2C_2 = 4$, so $C_2 = 2$ and $y = 3\cos 2t + 2\sin 2t$. The amplitude is $\sqrt{9 + 4} = \sqrt{13} \approx 3.606$ and the period is $\frac{2\pi}{2} = \pi$.

Check: $y'' = -4y$, so $y'' + 4y = 0$, and the largest value of $3\cos 2t + 2\sin 2t$ is $\sqrt{13}$.

</details>

3\. Solve $y'' - 6y' + 9y = 0$ with $y(0) = 1$ and $y'(0) = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

$(r - 3)^2 = 0$, so $r = 3$ twice and $y = (C_1 + C_2t)e^{3t}$. Then $y' = (C_2 + 3C_1 + 3C_2t)e^{3t}$, so $C_1 = 1$ and $C_2 + 3C_1 = 0$, which gives $C_2 = -3$. The solution is $y = (1 - 3t)e^{3t}$.

Check: $y(0) = 1$ and $y'(0) = (-3 + 3)\cdot 1 = 0$. The solution crosses $0$ at $t = \frac{1}{3}$ and then grows in the negative direction, which the factor $t$ allows.

</details>

### Standard

4\. A 1 kg mass on a spring has the equation $x'' + x' + 4x = 0$. (a) Is it underdamped, critically damped or overdamped? (b) Find the period of the oscillation and the time for the envelope to halve. (c) What value of the friction coefficient $\gamma$ (in place of the 1) makes it critically damped?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The discriminant is $1 - 16 = -15 < 0$, so it is underdamped. (b) The roots are $r = \frac{-1 \pm i\sqrt{15}}{2} = -0.5 \pm 1.936i$, so $\beta = 1.936$ and the period is $\frac{2\pi}{1.936} \approx 3.245$. The envelope is $e^{-0.5t}$, which halves when $t = \frac{\ln 2}{0.5} \approx 1.386$. (c) The equation $x'' + \gamma x' + 4x = 0$ has discriminant $\gamma^2 - 16$, which is $0$ for $\gamma = 4$.

Check: $\sqrt{4 - \frac{1}{4}} = \sqrt{3.75} = 1.936$, as found.

</details>

5\. Solve $y'' + 3y' + 2y = 6$ with $y(0) = 0$ and $y'(0) = 0$. What does $y$ approach?

<details class="solution" markdown>
<summary>Solution</summary>

For a constant right side, try $y_p = K$: then $2K = 6$ and $y_p = 3$. The homogeneous part is $C_1e^{-t} + C_2e^{-2t}$, so $y = 3 + C_1e^{-t} + C_2e^{-2t}$. The conditions are $3 + C_1 + C_2 = 0$ and $-C_1 - 2C_2 = 0$. So $C_1 = -2C_2$ and $3 - 2C_2 + C_2 = 0$, giving $C_2 = 3$ and $C_1 = -6$, and $y = 3 - 6e^{-t} + 3e^{-2t}$. As $t \to \infty$ it approaches $3$.

Check: $y(0) = 3 - 6 + 3 = 0$ and $y'(0) = 6 - 6 = 0$.

</details>

6\. Solve $\mathbf{x}' = A\mathbf{x}$ for $A = \begin{pmatrix} -1 & 2 \\ 2 & -1 \end{pmatrix}$ with $\mathbf{x}(0) = (3, 1)$, and classify the origin.

<details class="solution" markdown>
<summary>Solution</summary>

The trace is $-2$ and the determinant is $1 - 4 = -3$, so $\lambda^2 + 2\lambda - 3 = (\lambda + 3)(\lambda - 1)$, with eigenvalues $1$ and $-3$. For $\lambda = 1$: $A - I = \begin{pmatrix} -2 & 2 \\ 2 & -2 \end{pmatrix}$ gives $(1, 1)$. For $\lambda = -3$: $A + 3I = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$ gives $(1, -1)$. Writing $(3, 1) = c_1(1, 1) + c_2(1, -1)$ gives $c_1 = 2$ and $c_2 = 1$, so

$$
\mathbf{x}(t) = 2e^{t}\begin{pmatrix} 1 \\ 1 \end{pmatrix} + e^{-3t}\begin{pmatrix} 1 \\ -1 \end{pmatrix}.
$$

The eigenvalues have opposite signs, so the origin is a saddle.

Check: $A(1, 1) = (1, 1)$ and $A(1, -1) = (-3, 3) = -3(1, -1)$, and $\mathbf{x}(0) = (2 + 1, 2 - 1) = (3, 1)$.

</details>

### Challenge

7\. Show that when $b > 0$ and $c > 0$, every solution of $y'' + by' + cy = 0$ tends to $0$ as $t \to \infty$. What happens if $c < 0$? If $b < 0$ and $c > 0$?

<details class="solution" markdown>
<summary>Solution</summary>

Let the roots be $r = \frac{-b \pm \sqrt{b^2 - 4c}}{2}$. If $b^2 - 4c < 0$, the roots are $-\frac{b}{2} \pm i\beta$, with real part $-\frac{b}{2} < 0$, so every term has the factor $e^{-bt/2} \to 0$ (times a bounded oscillation). If $b^2 - 4c \ge 0$, then since $c > 0$ we have $\sqrt{b^2 - 4c} < b$, so both roots $\frac{-b \pm \sqrt{b^2 - 4c}}{2}$ are negative, and the solutions are combinations of $e^{r_1t}$ and $e^{r_2t}$ (and $te^{rt}$ for a double root), all tending to $0$.

If $c < 0$, then $\sqrt{b^2 - 4c} > \lvert b \rvert$, so one root is positive and one is negative, and almost every solution grows (a saddle in the system form). If $b < 0$ and $c > 0$, both roots (or the real part $-\frac{b}{2}$) are positive, so solutions grow: negative friction adds energy.

Check with $y'' + 2y' + 5y = 0$: $b = 2 > 0$ and $c = 5 > 0$, and the roots $-1 \pm 2i$ have negative real part. With $y'' - y' - 6y = 0$ ($c < 0$) the roots are $3$ and $-2$.

</details>

8\. (Reviews [eigenvalues and eigenvectors](../06-linear-algebra/08-eigenvalues-and-eigenvectors.md).) Write $y'' + 3y' + 2y = 0$ as a system $\mathbf{x}' = A\mathbf{x}$ with $\mathbf{x} = (y, y')$, find the eigenvalues and eigenvectors of $A$, and use them to solve it for $y(0) = 1$ and $y'(0) = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

With $y'' = -2y - 3y'$ the system is $\mathbf{x}' = A\mathbf{x}$ with $A = \begin{pmatrix} 0 & 1 \\ -2 & -3 \end{pmatrix}$. The trace is $-3$ and the determinant is $2$, so $\lambda^2 + 3\lambda + 2 = (\lambda + 1)(\lambda + 2)$ and the eigenvalues are $-1$ and $-2$, the roots of the characteristic equation. An eigenvector for $\lambda$ is $(1, \lambda)$, since $A(1, \lambda) = (\lambda, -2 - 3\lambda) = \lambda(1, \lambda)$ when $\lambda^2 + 3\lambda + 2 = 0$. So $\mathbf{v}_1 = (1, -1)$ and $\mathbf{v}_2 = (1, -2)$.

The starting vector is $(1, 0) = c_1(1, -1) + c_2(1, -2)$, so $c_1 + c_2 = 1$ and $-c_1 - 2c_2 = 0$, giving $c_2 = -1$ and $c_1 = 2$. The first component of $\mathbf{x}(t) = 2e^{-t}(1, -1) - e^{-2t}(1, -2)$ is $y = 2e^{-t} - e^{-2t}$.

Check: $y(0) = 1$ and $y'(0) = -2 + 2 = 0$.

</details>

## Where this shows up

- In the rest of the book, the characteristic equation returns in recurrences<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md -->, where $a_n = r^n$ replaces $e^{rt}$. The stability table is the same condition on eigenvalues that decides whether an iteration $\mathbf{x}_{k+1} = A\mathbf{x}_k$ converges, in the [eigenvalue lesson](../06-linear-algebra/08-eigenvalues-and-eigenvectors.md).
- In CS, second-order systems model control loops (a thermostat, a drone, a PID controller), signal filters and the physics in games and simulations. Momentum in gradient descent behaves like a heavy ball rolling with friction, which is a damped oscillator.
- In economics, second-order differential equations model business-cycle oscillations and adjustment with overshoot, and linear systems $\mathbf{x}' = A\mathbf{x}$ model several interacting markets. A saddle is the shape of the stable path in growth models such as Ramsey's.
