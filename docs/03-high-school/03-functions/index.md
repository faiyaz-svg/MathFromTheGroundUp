# Functions

The precise definition of a function, how to read its graph, functions defined by cases, transformations of graphs, and composition and inverses.

1. [What is a function](01-what-is-a-function.md)
2. [Reading function graphs](02-reading-function-graphs.md)
3. [Piecewise, absolute value and step functions](03-piecewise-absolute-value-and-step-functions.md)
4. [Transformations of functions](04-transformations-of-functions.md)
5. [Composition and inverse functions](05-composition-and-inverse-functions.md)

## Cheat sheet

### What is a function

A function $f \colon A \to B$ assigns to each element of the domain $A$ exactly one element of the codomain $B$. The range (image) is the set of outputs that actually occur, $f(A) = \{f(a) : a \in A\}$, and it is a subset of $B$.

| Idea | Statement | Example |
|---|---|---|
| set of pairs | $G \subseteq A \times B$ is a function when each $a$ starts exactly one pair | $\{(1, 4), (2, 5), (3, 4)\}$ |
| arrows | $\to$ between sets, $\mapsto$ between elements | $f \colon \mathbb{R} \to \mathbb{R}$, $x \mapsto x^2$ |
| equal functions | same domain, same codomain, same output for every input | $2(x + 1)$ and $2x + 2$ |
| natural domain | every real number the formula accepts | $\frac{\sqrt{x + 1}}{x - 3}$ gives $[-1, 3) \cup (3, \infty)$ |

- Natural domain: remove inputs that make a denominator 0 or put a negative number under an even root, then intersect the conditions. A root in a denominator needs a strictly positive radicand.
- The range depends on the domain: $x^2 + 1$ has range $[1, \infty)$ on $\mathbb{R}$ and $[1, 10]$ on $[-2, 3]$.
- In code, a type signature is a domain and a codomain, a pure function is a function, and a partial function (one that raises an error on some inputs) is not total.
- A function from an $m$-element set to an $n$-element set: there are $n^m$ of them.

Main mistakes:

- Calling the codomain the range.
- Cancelling a factor and forgetting the excluded input: $\frac{x^2 - 4}{x - 2}$ is not the same function as $x + 2$.
- Testing a set of pairs without naming the domain.
- Treating $\sqrt{x^2}$ as $x$. It is $\lvert x \rvert$.

### Reading function graphs

| Feature | How to read it |
|---|---|
| value $f(a)$ | go up or down from $a$ to the curve, then across |
| solve $f(x) = c$ | go across from $c$ and read the $x$-values of every hit |
| zero, $x$-intercept | $f(c) = 0$, the point $(c, 0)$ |
| $y$-intercept | $(0, f(0))$, at most one |
| increasing on $I$ | $x_1 < x_2$ in $I$ gives $f(x_1) < f(x_2)$ |
| local maximum at $c$ | $f(c) \ge f(x)$ for all $x$ in an open interval around $c$ |
| absolute maximum at $c$ | $f(c) \ge f(x)$ for every $x$ in the domain |
| average rate of change | $\dfrac{f(b) - f(a)}{b - a}$, the slope of the secant line |
| even | $f(-x) = f(x)$, mirror image in the $y$-axis |
| odd | $f(-x) = -f(x)$, unchanged by a half turn about the origin |

- Intervals of increase and decrease are intervals of $x$, written left to right.
- An odd function with 0 in its domain has $f(0) = 0$. The domain must be symmetric for even or odd to make sense.
- Polynomials: all even powers means even, all odd powers means odd, a mix means neither. Even times odd is odd, and odd times odd is even.
- Units of a rate: output units per input unit.

Main mistakes:

- Giving heights as the interval of increase.
- Mixing up local and absolute maximums.
- Reading an average rate of change of 0 as "nothing happened": $x^2$ from $-1$ to 1.
- Confusing average cost with average rate of change.
- Confusing $f(-x)$ with $-f(x)$.

### Piecewise, absolute value and step functions

A piecewise function uses a different formula on each piece of its domain. The pieces cover the domain and don't overlap, unless the formulas agree where they share an input.

| Function | Definition | Example |
|---|---|---|
| absolute value | $\lvert x \rvert = x$ for $x \ge 0$, and $-x$ for $x < 0$ | $\lvert 2x - 6 \rvert$ breaks at $x = 3$ |
| floor $\lfloor x \rfloor$ | greatest integer $\le x$ | $\lfloor -3.7 \rfloor = -4$ |
| ceiling $\lceil x \rceil$ | least integer $\ge x$ | $\lceil -3.7 \rceil = -3$ |

- Graphing: solid dot where the condition has $\le$ or $\ge$, open circle where it has $<$ or $>$, and never two solid dots at one input.
- To solve $f(x) = c$, solve in each piece and keep only the solutions that satisfy that piece's condition.
- $\lceil x \rceil = -\lfloor -x \rfloor$. For integers $n \ge 0$ and $k \ge 1$, $\lceil n/k \rceil = \lfloor (n + k - 1)/k \rfloor$, which is the number of pages for $n$ items with $k$ per page. Python's `//` is the floor.
- A cap is a minimum, $\min(\text{charge}, \text{cap})$, and $\lvert x \rvert = \max(x, -x)$.
- A progressive tax is piecewise linear: the tax at the start of a bracket plus its rate times the income above the start. The slopes are the marginal rates, and the average rate is tax divided by income. The brackets in the lesson are hypothetical.

Main mistakes:

- Using the wrong piece at a break point.
- Reading $\lfloor -3.7 \rfloor$ as $-3$ (that is the ceiling, or truncation).
- Taking $\lceil 5 \rceil$ as 6.
- Taxing all income at the top bracket's rate.
- Writing $\lvert x + 3 \rvert$ as $\lvert x \rvert + 3$.

### Transformations of functions

The general form is $g(x) = a\,f(b(x - h)) + k$. A point $(u, v)$ of the graph of $f$ goes to $\left(h + \frac{u}{b},\ av + k\right)$.

| Change | Effect |
|---|---|
| $f(x) + k$ | up $k$ |
| $f(x - h)$ | right $h$ |
| $a\,f(x)$, $a > 0$ | vertical stretch by $a$ |
| $f(bx)$, $b > 0$ | horizontal compression by $b$ |
| $-f(x)$ | reflection in the $x$-axis |
| $f(-x)$ | reflection in the $y$-axis |

- Inside changes act backwards because the graph undoes what the formula does to $x$, in the opposite order: divide by $b$, then add $h$. Outside changes act as written.
- Factor out $b$ first: $f(2x - 6) = f(2(x - 3))$ shifts right 3, not 6.
- Horizontal and vertical changes don't interfere. Within one direction, the order matters: $2f(x) + 3 \ne 2(f(x) + 3)$.
- Vertex forms: $a(x - h)^2 + k$ has vertex $(h, k)$, and $a\lvert x - h \rvert + k$ has its corner there. For $a\sqrt{b(x - h)} + k$ the domain is $x \ge h$ if $b > 0$ and $x \le h$ if $b < 0$.
- Domain and range follow: the horizontal rule acts on the domain, the vertical rule on the range.

Main mistakes:

- Shifting $f(x + 2)$ to the right.
- Calling $f(2x)$ a stretch. It is a compression.
- Mixing up $-f(x)$ and $f(-x)$.
- Reading the shift off the unfactored bracket.
- Doing a reflection and a shift in the wrong order: for $\sqrt{x}$, "reflect then shift right 2" is $\sqrt{2 - x}$ and "shift then reflect" is $\sqrt{-x - 2}$.

### Composition and inverse functions

The composition is $(f \circ g)(x) = f(g(x))$, with $g$ applied first. Its domain is the set of $x$ in the domain of $g$ with $g(x)$ in the domain of $f$.

| Idea | Statement |
|---|---|
| not commutative | $f \circ g \ne g \circ f$ in general |
| associative | $(f \circ g) \circ h = f \circ (g \circ h)$ |
| inverse | $f^{-1}(f(x)) = x$ and $f(f^{-1}(y)) = y$ |
| inverse of a composition | $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$ |
| graph | $f^{-1}$ is the reflection of $f$ in $y = x$; $(a, b) \to (b, a)$ |
| domain and range | domain of $f^{-1}$ is the range of $f$, and the reverse |

- A function has an inverse exactly when it is one-to-one: the horizontal line test, or $f(x_1) = f(x_2)$ forces $x_1 = x_2$. An invertible function is always one-to-one, and the inverse is unique.
- To find an inverse: check one-to-one, write $y = f(x)$, solve for $x$, rename, state the domain and range, and check both compositions.
- Restrict the domain to get an inverse: $x^2$ on $x \ge 0$ has the inverse $\sqrt{x}$.
- Undo a chain of steps in reverse order. For $f(x) = mx + b$, $f^{-1}(x) = \frac{x - b}{m}$.
- Examples: $F = 1.8C + 32$ gives $C = \frac{F - 32}{1.8}$, and removing 13% HST is dividing by 1.13.

Main mistakes:

- Reading $f^{-1}(x)$ as $\frac{1}{f(x)}$.
- Simplifying a composition and losing its domain: $(\sqrt{x})^2 - 9$ is $x - 9$ only for $x \ge 0$.
- Calling $\sqrt{x}$ the inverse of $x^2$ on all of $\mathbb{R}$.
- Undoing the steps in the original order instead of the reverse order.
- Expecting composition to commute when one step adds a fixed amount.
