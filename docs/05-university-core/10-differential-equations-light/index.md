# Differential equations (light)

Equations that give a rate of change: how to read them with slope fields, solve the common first-order types, step them with Euler's method, and handle the second-order linear case that describes springs and oscillations. Lesson 2 is optional.

1. [First-order differential equations](01-first-order-differential-equations.md)
2. [Second-order linear equations](02-second-order-linear-equations.md) (optional)

## Cheat sheet

### First-order differential equations

| Type | Form | Solution |
|---|---|---|
| exponential growth or decay | $y' = ky$ | $y = y_0e^{kt}$; doubling time $\frac{\ln 2}{k}$ if $k > 0$, half-life $\frac{\ln 2}{\lvert k \rvert}$ if $k < 0$ |
| cooling, price adjustment | $y' = -k(y - c)$ | $y = c + (y_0 - c)e^{-kt}$ |
| separable | $y' = g(t)h(y)$ | $\int\frac{dy}{h(y)} = \int g\,dt + C$; keep the equilibria $h(y) = 0$ |
| linear | $y' + p(t)y = q(t)$ | multiply by $\mu = e^{\int p\,dt}$: $(\mu y)' = \mu q$ |
| logistic | $P' = rP\left(1 - \frac{P}{K}\right)$ | $P = \dfrac{K}{1 + Ae^{-rt}}$, $A = \dfrac{K - P_0}{P_0}$ |

Vocabulary: order is the highest derivative, an initial value problem adds $y(t_0) = y_0$, and an equilibrium is a constant solution with $f = 0$. An equilibrium of $y' = f(y)$ is stable if $f' < 0$ there and unstable if $f' > 0$. Solutions of $y' = f(t, y)$ never cross.

Logistic facts: equilibria $0$ (unstable) and $K$ (stable), fastest growth $\frac{rK}{4}$ at $P = \frac{K}{2}$, reached at $t = \frac{\ln A}{r}$. Compounding: continuous growth at rate $r$ multiplies by $e^r$ a year, against $1 + r$ for yearly compounding. Steady deposits $d$ at rate $r$ from $A(0) = 0$ give $A = \frac{d}{r}(e^{rt} - 1)$.

Existence and uniqueness: if $f$ and $\frac{\partial f}{\partial y}$ are continuous near $(t_0, y_0)$, the initial value problem has exactly one solution nearby. Failures: $y' = 3y^{2/3}$ from $0$ has two solutions ($0$ and $t^3$), and $y' = y^2$ from $1$ blows up at $t = 1$.

Euler's method: $y_{n+1} = y_n + h\,f(t_n, y_n)$. The error is proportional to $h$ (for $y' = y$, $h = 0.1$ gives $2.5937$ against $e = 2.7183$). On $y' = -\lambda y$ it needs $h < \frac{2}{\lambda}$, which is the learning-rate limit of gradient descent, since gradient descent is Euler's method for $w' = -f'(w)$.

Economics: a price with $p' = k(D - S)$ approaches the equilibrium exponentially, and Solow's $k' = sk^{\alpha} - \delta k$ becomes linear in $u = k^{1 - \alpha}$ with steady state $k^* = \left(\frac{s}{\delta}\right)^{1/(1 - \alpha)}$.

Worked reminders: \$1,000 at 5% compounded continuously is worth $1000e^{0.5} \approx \$1{,}648.72$ after 10 years. Coffee at $90^\circ\text{C}$ in a $20^\circ\text{C}$ room that reaches $70^\circ\text{C}$ after 10 minutes has $k = \frac{\ln(7/5)}{10} \approx 0.0336$ and reaches $40^\circ\text{C}$ at $t \approx 37.2$ minutes. For $y' + 2y = 6$ the integrating factor is $e^{2t}$ and $y = 3 + Ce^{-2t}$. With the logistic numbers $K = 10^6$, $r = 0.5$, $P_0 = 1000$ the curve reaches half capacity at $t = \frac{\ln 999}{0.5} \approx 13.8$ months.

The main mistakes: forgetting the constant, losing equilibria when dividing, separating an equation that is not separable (such as $y' = t + y$), a wrong sign in a decay or cooling exponent, and an Euler step that is too large.

### Second-order linear equations

| Roots of $r^2 + br + c = 0$ | General solution of $y'' + by' + cy = 0$ |
|---|---|
| distinct real $r_1, r_2$ | $C_1e^{r_1t} + C_2e^{r_2t}$ |
| repeated real $r$ | $(C_1 + C_2t)e^{rt}$ |
| complex $\alpha \pm i\beta$ | $e^{\alpha t}(C_1\cos\beta t + C_2\sin\beta t)$ |

Try $y = e^{rt}$ to get the characteristic equation. The two constants come from $y(0)$ and $y'(0)$. The roots add to $-b$ and multiply to $c$. For a pair $\alpha \pm i\beta$ the real part is $-\frac{b}{2}$, the frequency is $\beta = \sqrt{c - \frac{b^2}{4}}$ and the period is $\frac{2\pi}{\beta}$.

Spring $mx'' + \gamma x' + kx = 0$: underdamped if $\gamma^2 < 4mk$ (oscillates inside the envelope $e^{-\gamma t/(2m)}$), critically damped if $\gamma^2 = 4mk$ (no oscillation), overdamped if $\gamma^2 > 4mk$. Example with $x(0) = 1$, $x'(0) = 0$, $m = 1$: $\gamma = 2$, $k = 5$ gives $e^{-t}(\cos 2t + 0.5\sin 2t)$; $\gamma = 2$, $k = 1$ gives $(1 + t)e^{-t}$; $\gamma = 5$, $k = 4$ gives $\frac{4e^{-t} - e^{-4t}}{3}$.

Forcing: the solution is a particular solution plus the homogeneous solution. Try a constant for a constant $g$ and $A\cos\omega t + B\sin\omega t$ for $\cos\omega t$ (for $y'' + 3y' + 2y = 10\cos t$ it is $\cos t + 3\sin t$). Forcing at the natural frequency of an undamped system gives resonance, growth like $t\sin\omega_0t$.

Systems: $\mathbf{x}' = A\mathbf{x}$ has the solution $c_1e^{\lambda_1t}\mathbf{v}_1 + c_2e^{\lambda_2t}\mathbf{v}_2$. The equation $y'' + by' + cy = 0$ is the system with $A = \begin{pmatrix} 0 & 1 \\ -c & -b \end{pmatrix}$, whose characteristic polynomial is $\lambda^2 + b\lambda + c$. Recurrences use $r^n$ with the same polynomial.

| Eigenvalues | Behaviour |
|---|---|
| both real, negative | decay to $\mathbf{0}$ (stable) |
| both real, positive | growth (unstable) |
| real, opposite signs | saddle |
| complex, real part $< 0$ | spiral in (stable) |
| complex, real part $> 0$ | spiral out (unstable) |
| complex, real part $= 0$ | closed loops |

With $b, c > 0$ every solution of $y'' + by' + cy = 0$ tends to $0$.

Worked reminders: $y'' - y' - 6y = 0$ has roots $3$ and $-2$. $y'' + 6y' + 9y = 0$ has the double root $-3$ and solutions $(C_1 + C_2t)e^{-3t}$. $y'' + 2y' + 5y = 0$ has roots $-1 \pm 2i$, so solutions oscillate with period $\pi$ inside the envelope $e^{-t}$. The system $\mathbf{x}' = A\mathbf{x}$ with $A = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$ has eigenvalues $3$ and $-2$, a saddle.

The main mistakes: using one constant or one initial condition, writing $(C_1 + C_2)e^{rt}$ for a double root, dropping the $e^{\alpha t}$ factor in the complex case, a wrong sign in the characteristic equation, and fitting initial conditions before adding the particular solution.
