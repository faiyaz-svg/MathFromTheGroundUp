# Trigonometry

Triangle ratios, the unit circle and radians, the sine wave, identities and inverse functions, and (optionally) the laws for triangles without a right angle.

1. [Right triangle trigonometry](01-right-triangle-trigonometry.md)
2. [Radians and the unit circle](02-radians-and-the-unit-circle.md)
3. [Graphs of trig functions](03-graphs-of-trig-functions.md)
4. [Trig identities and inverse trig](04-trig-identities-and-inverse-trig.md)
5. [Law of sines and law of cosines](05-law-of-sines-and-cosines.md) (optional)

## Cheat sheet

### Right triangle trigonometry

For an acute angle $\theta$ in a right triangle, SOH CAH TOA:

$$
\sin\theta = \frac{\text{opp}}{\text{hyp}}, \qquad \cos\theta = \frac{\text{adj}}{\text{hyp}}, \qquad \tan\theta = \frac{\text{opp}}{\text{adj}}.
$$

The ratios depend only on $\theta$, because right triangles with the same acute angle are similar. Also $\sin\theta = \cos(90^\circ - \theta)$.

| $\theta$ | $\sin\theta$ | $\cos\theta$ | $\tan\theta$ |
|---|---|---|---|
| $30^\circ$ | $\frac{1}{2}$ | $\frac{\sqrt{3}}{2}$ | $\frac{\sqrt{3}}{3}$ |
| $45^\circ$ | $\frac{\sqrt{2}}{2}$ | $\frac{\sqrt{2}}{2}$ | $1$ |
| $60^\circ$ | $\frac{\sqrt{3}}{2}$ | $\frac{1}{2}$ | $\sqrt{3}$ |

- To find a side: pick the ratio that holds the known side and the wanted side. An unknown in the denominator needs a division, as in $x = \frac{50}{\tan 20^\circ}$.
- To find an angle: $\theta = \sin^{-1}(\text{ratio})$, or the matching inverse. The other acute angle is $90^\circ - \theta$.
- Angles of elevation and depression are measured from the horizontal. The two are equal along one line of sight (alternate angles). Add the eye height.
- Special triangles: sides $1 : 1 : \sqrt{2}$ and $1 : \sqrt{3} : 2$.

Main mistakes:

- Calculator in the wrong mode. Test $\sin 30 = 0.5$.
- Reading $\sin^{-1}$ as $\frac{1}{\sin}$.
- Naming opposite and adjacent from the wrong angle.
- Rounding in the middle.

### Radians and the unit circle

An angle in radians is arc length divided by radius, $\theta = \frac{s}{r}$. A full turn is $2\pi$ radians.

| Task | Rule | Example |
|---|---|---|
| degrees to radians | multiply by $\frac{\pi}{180}$ | $150^\circ = \frac{5\pi}{6}$ |
| radians to degrees | multiply by $\frac{180}{\pi}$ | $1 \text{ rad} \approx 57.3^\circ$ |
| arc length | $s = r\theta$ | $r = 6$, $\theta = \frac{5\pi}{6}$ gives $5\pi$ |
| sector area | $A = \frac{1}{2}r^2\theta$ | the same sector has area $15\pi$ |
| point at angle $\theta$, radius $r$ | $(r\cos\theta, r\sin\theta)$ | on the unit circle, $r = 1$ |

- On the unit circle, $\cos\theta$ is the $x$-coordinate, $\sin\theta$ is the $y$-coordinate and $\tan\theta = \frac{\sin\theta}{\cos\theta}$ (undefined where $\cos\theta = 0$).
- Evaluate any angle by reducing it to $[0, 2\pi)$, naming the quadrant, finding the reference angle and attaching the sign. All Students Take Calculus: all positive in I, sine in II, tangent in III, cosine in IV.
- Pythagorean identity: $\sin^2\theta + \cos^2\theta = 1$. Given one of sine and cosine and the quadrant, find the other.
- Radians keep $s = r\theta$ clean, make $\frac{\sin\theta}{\theta} \to 1$ as $\theta \to 0$ and make $\frac{d}{dx}\sin x = \cos x$. Every programming language's `sin` takes radians.

Main mistakes:

- Using $s = r\theta$ or $\frac{1}{2}r^2\theta$ with degrees.
- Taking the calculator's inverse answer as the angle without checking the quadrant.
- Writing $\sin 2\theta = 2\sin\theta$.
- Using the angle itself where the reference angle belongs.

### Graphs of trig functions

Sine and cosine have domain $\mathbb{R}$, range $[-1, 1]$ and period $2\pi$. Tangent has period $\pi$, range $\mathbb{R}$ and vertical asymptotes at $x = \frac{\pi}{2} + k\pi$.

$$
y = A\sin\bigl(B(x - C)\bigr) + D
$$

| Feature | Value |
|---|---|
| amplitude | $\lvert A \rvert$ |
| period | $\frac{2\pi}{\lvert B \rvert}$ (for tangent, $\frac{\pi}{\lvert B \rvert}$) |
| midline | $y = D$ |
| phase shift | $C$, to the right if positive |
| maximum and minimum | $D \pm \lvert A \rvert$ |

- Sketch: draw the midline, mark the maximum and minimum, find the period, plot five key points a quarter period apart, and join them smoothly.
- From a graph or data: $A = \frac{\max - \min}{2}$, $D = \frac{\max + \min}{2}$, $B = \frac{2\pi}{\text{period}}$. Use cosine if you know where a maximum is.
- Cosine is sine shifted left by $\frac{\pi}{2}$: $\cos x = \sin\left(x + \frac{\pi}{2}\right)$.
- Tangent: each branch is centred midway between two asymptotes, and passes through heights $D \pm A$ halfway to each asymptote.
- A sinusoid is a good first model of periodic data (daylight hours, tides), and not an exact one.

Main mistakes:

- Reading the shift before factoring: $\sin(2x - \pi)$ has shift $\frac{\pi}{2}$.
- Using $2\pi B$ for the period.
- Calling the amplitude negative, or giving tangent an amplitude.
- Joining the branches of a tangent graph.

### Trig identities and inverse trig

| Group | Identities |
|---|---|
| Reciprocal | $\csc\theta = \frac{1}{\sin\theta}$, $\sec\theta = \frac{1}{\cos\theta}$, $\cot\theta = \frac{1}{\tan\theta}$ |
| Quotient | $\tan\theta = \frac{\sin\theta}{\cos\theta}$, $\cot\theta = \frac{\cos\theta}{\sin\theta}$ |
| Pythagorean | $\sin^2\theta + \cos^2\theta = 1$, $1 + \tan^2\theta = \sec^2\theta$, $1 + \cot^2\theta = \csc^2\theta$ |
| Sum and difference | $\sin(a \pm b) = \sin a\cos b \pm \cos a\sin b$, $\cos(a \pm b) = \cos a\cos b \mp \sin a\sin b$ |
| Double angle | $\sin 2\theta = 2\sin\theta\cos\theta$, $\cos 2\theta = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$ |

- Prove an identity by working on one side only: rewrite in sine and cosine, combine fractions, factor, use a Pythagorean substitution. Never start from the claim and operate on both sides, because squaring $-1 = 1$ gives a true statement.
- Inverse functions: $\sin^{-1}$ has range $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, $\cos^{-1}$ has range $[0, \pi]$ and $\tan^{-1}$ has range $\left(-\frac{\pi}{2}, \frac{\pi}{2}\right)$. Also $\sin^{-1}(\sin x) = x$ only on that range.
- Solving: isolate a trig function (factor, never divide by one), find the angles in one period from the unit circle, then add $2\pi k$ (or $\pi k$ for tangent) or list those inside the interval.

| Equation | General solution ($k$ an integer) |
|---|---|
| $\sin x = c$ | $x = \alpha + 2\pi k$ or $x = \pi - \alpha + 2\pi k$, $\alpha = \sin^{-1} c$ |
| $\cos x = c$ | $x = \pm\alpha + 2\pi k$, $\alpha = \cos^{-1} c$ |
| $\tan x = c$ | $x = \alpha + \pi k$, $\alpha = \tan^{-1} c$ |

- For $\cos 2x = c$ on $[0, 2\pi)$, solve for $2x$ on $[0, 4\pi)$ and then halve: twice as many solutions.

Main mistakes:

- $\sin(a + b) = \sin a + \sin b$.
- Dividing by $\sin x$ and losing the solutions where it is 0.
- Keeping only the calculator's angle and missing the second one in the period.
- Keeping an answer that squaring introduced and the original equation rejects.

### Law of sines and law of cosines (optional)

In a triangle with sides $a$, $b$, $c$ opposite the angles $A$, $B$, $C$:

$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}, \qquad c^2 = a^2 + b^2 - 2ab\cos C, \qquad \text{area} = \frac{1}{2}ab\sin C.
$$

| Given | Use |
|---|---|
| ASA or AAS | law of sines |
| SAS | law of cosines for the third side |
| SSS | law of cosines for an angle (largest first) |
| SSA | law of sines, and check for two triangles |

- For $C = 90^\circ$ the law of cosines is the Pythagorean theorem. The sign of $c^2 - a^2 - b^2$ shows whether $C$ is acute, right or obtuse.
- SSA with acute $A$ and $h = b\sin A$: no triangle if $a < h$, one right triangle if $a = h$, two if $h < a < b$ and one if $a \ge b$.

Main mistakes:

- Missing the obtuse second angle from the inverse sine.
- Pairing a side with the wrong angle in the law of cosines.
- Rounding the intermediate values.
