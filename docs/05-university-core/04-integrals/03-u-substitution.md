# U-substitution

After this lesson you can recognise an integrand of the form $f(g(x))\,g'(x)$, evaluate indefinite and definite integrals by substitution (changing the limits for definite ones), prove the substitution rule from the chain rule, and tell when substitution will not work.

Before this: [the fundamental theorem of calculus](02-fundamental-theorem-of-calculus.md) and [the chain rule](../02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Find $\displaystyle\int 2x\cos\left(x^2\right)dx$.
2. Evaluate $\displaystyle\int_0^1 x\left(1 + x^2\right)^3\,dx$.
3. Find $\displaystyle\int e^{3x}\,dx$.

<details class="solution" markdown>
<summary>Answers</summary>

1. The inner function is $x^2$ and its derivative $2x$ is sitting in front, so the integral is $\sin\left(x^2\right) + C$. Check: the chain rule gives $\cos\left(x^2\right) \cdot 2x$.
2. Let $u = 1 + x^2$, so $du = 2x\,dx$ and $x\,dx = \frac{1}{2}\,du$. The limits become $u = 1$ and $u = 2$, so the integral is $\frac{1}{2}\int_1^2 u^3\,du = \frac{1}{2}\cdot\frac{16 - 1}{4} = \frac{15}{8}$.
3. The inside is linear, so $\frac{e^{3x}}{3} + C$.

</details>

## The idea

The chain rule says $\frac{d}{dx}\sin\left(x^2\right) = \cos\left(x^2\right) \cdot 2x$. Read from right to left, that is an integration fact:

$$
\int \cos\left(x^2\right) \cdot 2x\,dx = \sin\left(x^2\right) + C.
$$

The integrand has two parts, an outer function $\cos$ applied to an inner function $x^2$, and the derivative $2x$ of the inner function. That second part is what makes the integral possible: the derivative of the inside is the factor the chain rule leaves behind. Substitution is the method of spotting that pattern and using a new letter for the inside, so that the integral looks like one from the table.

The new letter makes the pattern easy to see. Write $u = x^2$, so that $\cos\left(x^2\right)$ becomes $\cos u$, and the leftover $2x\,dx$ becomes $du$. The integral turns into $\int \cos u\,du = \sin u + C$, and putting $x^2$ back for $u$ gives the answer. The method is not a trick with symbols. It is the chain rule, run backward, and the symbol $du = g'(x)\,dx$ is bookkeeping that the proof below justifies.

Not every integral has the pattern. The integral $\int x\cos x\,dx$ has no inner function whose derivative appears, and $\int e^{x^2}\,dx$ is missing the factor $x$ that made the example above work. It has no elementary antiderivative at all. Part of using substitution well is knowing when to stop.

## Definitions

The **substitution rule** is the statement that, if $u = g(x)$, then

$$
\int f\bigl(g(x)\bigr)\,g'(x)\,dx = \int f(u)\,du \quad \text{with } u = g(x),
$$

and for a definite integral

$$
\int_a^b f\bigl(g(x)\bigr)\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du.
$$

In plain words, replace the inside function by a new variable $u$, replace $g'(x)\,dx$ by $du$, and for a definite integral replace the limits by the values of $u$ at the old limits.

The function $g$ is the **substitution** and $u = g(x)$ is the new variable. The **differential** of $u$ is $du = g'(x)\,dx$. In plain words, $du$ is the derivative of the inside, times $dx$. For $u = 1 + x^2$ the differential is $du = 2x\,dx$.

Two reminders from earlier lessons. The integral $\int f(u)\,du$ means an antiderivative of $f$, so it is a family of functions with $+C$. And the symbol $dx$ in $\int f(x)\,dx$ names the variable of integration, so that when you change the variable you must change it everywhere in the integrand and in $dx$.

## How to do it

### The method

1. Look for an inner function $g(x)$, for example the expression inside a power, root, exponential, logarithm or trig function, or a denominator, such that $g'(x)$ (or a constant multiple of it) is also in the integrand. Call it $u$.
2. Compute $du = g'(x)\,dx$. If the integrand has $g'(x)$ times a constant $k$, solve for the part you have: for $du = 2x\,dx$ and an integrand with $x\,dx$, write $x\,dx = \frac{1}{2}\,du$.
3. Rewrite the entire integral in terms of $u$. No $x$ may remain. If one does, you may be able to solve $u = g(x)$ for $x$ and replace it, as in Example 4. If not, the substitution is not working.
4. Integrate with respect to $u$, using the table.
5. For an indefinite integral, replace $u$ by $g(x)$. For a definite integral, either replace the limits at Step 3 by $g(a)$ and $g(b)$ and evaluate in $u$, or return to $x$ and use the old limits. Never mix the two.
6. Check by differentiating the answer. For a definite integral, check the size against a trapezoid sum.

### The proof of the rule

*Theorem (substitution rule).* Let $g$ have a continuous derivative on $[a, b]$ and let $f$ be continuous on an interval that contains every value $g(x)$ for $x$ in $[a, b]$. Then

$$
\int_a^b f\bigl(g(x)\bigr)\,g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du,
$$

and if $F$ is an antiderivative of $f$, then $F\bigl(g(x)\bigr)$ is an antiderivative of $f\bigl(g(x)\bigr)g'(x)$.

We know the chain rule and both parts of the fundamental theorem of calculus. We want to show that two integrals are equal. The plan is to find an antiderivative of the integrand on the left by using the chain rule, and then evaluate both sides with part 2.

*Proof.* Since $f$ is continuous, part 1 of the fundamental theorem says that $f$ has an antiderivative $F$ on that interval, with $F' = f$. By the chain rule,

$$
\frac{d}{dx}F\bigl(g(x)\bigr) = F'\bigl(g(x)\bigr)\,g'(x) = f\bigl(g(x)\bigr)\,g'(x).
$$

So $F\circ g$ is an antiderivative of the integrand $f\bigl(g(x)\bigr)g'(x)$, which is continuous because $f$, $g$ and $g'$ are. By part 2 of the fundamental theorem,

$$
\int_a^b f\bigl(g(x)\bigr)\,g'(x)\,dx = F\bigl(g(b)\bigr) - F\bigl(g(a)\bigr).
$$

Part 2 applied to $f$ on the interval from $g(a)$ to $g(b)$ says that the right side is $\int_{g(a)}^{g(b)} f(u)\,du$. $\blacksquare$

Look back: the proof is two lines because the work was done by the chain rule. It shows why the limits change. The old limits $a$ and $b$ are values of $x$, and the new integral is over $u$, so the endpoints are the values of $u$ there. It also shows that $g$ doesn't need to be one-to-one: if $g$ goes up and then back down, the signed areas in $u$ cancel as they should (Example 3). And $du = g'(x)\,dx$ is safe to use as a rule for rewriting, because the rule is proved for exactly that rewriting. Don't read more into it than that, since $du$ is not a separate object in this book.

### Choosing $u$

A good $u$ is the inside of the most complicated part of the integrand whose derivative is also present. These patterns cover most cases.

| The integrand contains | Try $u$ equal to | Because |
|---|---|---|
| $\bigl(\text{expression}\bigr)^n$ and the derivative of the expression | the expression | the integral becomes $\int u^n\,du$ |
| $e^{\text{expression}}$ and its derivative | the exponent | the integral becomes $\int e^u\,du$ |
| $\sin$, $\cos$ or another trig function of an expression and its derivative | the expression inside | the integral becomes a table entry in $u$ |
| a fraction with the derivative of the denominator on top | the denominator | the integral becomes $\int \frac{du}{u} = \ln\lvert u \rvert + C$ |
| $\ln x$ and $\frac{1}{x}$ | $\ln x$ | $d(\ln x) = \frac{dx}{x}$ |
| a root of a linear expression times $x$ | the linear expression, solving for $x$ | the leftover $x$ is rewritten in $u$ |

When two choices seem possible, take the one that makes the rest simpler, and if the first choice leaves an $x$ that can't be removed, try the other. A wrong choice costs a few lines, not a mistake in the answer.

## Worked examples

<div class="example" markdown>

### Example 1: an exponential with a square

Find $\int x\,e^{x^2}\,dx$.

Step 1: the exponent $x^2$ is an inner function, and its derivative $2x$ is nearly the leftover factor $x$. Let $u = x^2$.

Step 2: $du = 2x\,dx$, and since the integrand has $x\,dx$ and not $2x\,dx$, write $x\,dx = \frac{1}{2}\,du$.

Step 3: the integral becomes $\int e^u \cdot \frac{1}{2}\,du$, and no $x$ remains.

Step 4: $\frac{1}{2}\int e^u\,du = \frac{1}{2}e^u + C$.

Step 5: put back $u = x^2$: $\int x\,e^{x^2}\,dx = \frac{1}{2}e^{x^2} + C$.

Step 6, the check: $\frac{d}{dx}\left[\frac{1}{2}e^{x^2}\right] = \frac{1}{2}e^{x^2} \cdot 2x = x\,e^{x^2}$. A common slip is to drop the factor $\frac{1}{2}$ and write $e^{x^2} + C$, whose derivative is $2x\,e^{x^2}$, twice the integrand.

</div>

<div class="example" markdown>

### Example 2: the integral of the tangent

Find $\int \tan x\,dx$.

Write $\tan x = \frac{\sin x}{\cos x}$. The denominator is $\cos x$, and its derivative $-\sin x$ is, up to a sign, the numerator. Let $u = \cos x$, so $du = -\sin x\,dx$ and $\sin x\,dx = -du$. Then

$$
\int \frac{\sin x}{\cos x}\,dx = \int \frac{-du}{u} = -\ln\lvert u \rvert + C = -\ln\lvert \cos x \rvert + C.
$$

Since $-\ln\lvert \cos x \rvert = \ln\left\lvert \frac{1}{\cos x} \right\rvert$, this is the same as $\ln\lvert \sec x \rvert + C$. The same method with $u = \sin x$ gives $\int \cot x\,dx = \ln\lvert \sin x \rvert + C$.

Check: $\frac{d}{dx}\left[-\ln\lvert \cos x \rvert\right] = -\frac{-\sin x}{\cos x} = \tan x$, using $\frac{d}{dx}\ln\lvert u \rvert = \frac{u'}{u}$. The absolute value matters: $\cos x$ is negative on half of each period, and $\ln$ of a negative number is undefined. The answer is valid on any interval where $\cos x \ne 0$.

</div>

<div class="example" markdown>

### Example 3: a definite integral, with new limits

Evaluate $\int_0^1 \frac{x}{1 + x^4}\,dx$.

The denominator contains $x^4 = \left(x^2\right)^2$, and the numerator contains $x$, which is half the derivative of $x^2$. Let $u = x^2$, so $du = 2x\,dx$ and $x\,dx = \frac{1}{2}\,du$, and $1 + x^4 = 1 + u^2$. The limits change: when $x = 0$, $u = 0$, and when $x = 1$, $u = 1$. So

$$
\int_0^1 \frac{x}{1 + x^4}\,dx = \frac{1}{2}\int_0^1 \frac{du}{1 + u^2} = \frac{1}{2}\bigl[\arctan u\bigr]_0^1 = \frac{1}{2}\left(\frac{\pi}{4} - 0\right) = \frac{\pi}{8}.
$$

Check: the integrand is 0 at $x = 0$, rises to a peak of about $0.57$ near $x = 0.76$, and is $0.5$ at $x = 1$, so the area over a width of 1 should be well under $0.57$, and $\frac{\pi}{8} = 0.3927$ fits. A trapezoid sum with $n = 1000$ gives $0.3927$. An alternative check is to return to $x$: the antiderivative is $\frac{1}{2}\arctan\left(x^2\right)$, and evaluating at 1 and 0 gives the same $\frac{\pi}{8}$.

Another case worth seeing is a substitution that is not one-to-one. For $\int_{-1}^{1} 2x\,e^{x^2}\,dx$, let $u = x^2$. The limits are $u = 1$ at $x = -1$ and $u = 1$ at $x = 1$, so the new integral is $\int_1^1 e^u\,du = 0$. That agrees with the picture: the integrand is odd, so the area on the left of 0 cancels the area on the right.

</div>

<div class="example" markdown>

### Example 4: a leftover $x$

Find $\int x\sqrt{x - 1}\,dx$.

Try $u = x - 1$, the inside of the root. Then $du = dx$ and, solving for $x$, $x = u + 1$. The leftover $x$ is rewritten in terms of $u$:

$$
\int (u + 1)\,u^{1/2}\,du = \int \left(u^{3/2} + u^{1/2}\right)du = \frac{2}{5}u^{5/2} + \frac{2}{3}u^{3/2} + C.
$$

Back in $x$: $\frac{2}{5}(x - 1)^{5/2} + \frac{2}{3}(x - 1)^{3/2} + C$.

Check: differentiating gives $(x - 1)^{3/2} + (x - 1)^{1/2} = (x - 1)^{1/2}\bigl((x - 1) + 1\bigr) = x\sqrt{x - 1}$. The method worked because the substitution was linear, so $x$ could be solved for. For $\int x\sqrt{x^2 - 1}\,dx$ the better choice is $u = x^2 - 1$, which absorbs the $x$ into $du$.

</div>

<div class="example" markdown>

### Example 5: a logarithm inside a fraction (finish it yourself)

Evaluate $\int_e^{e^2}\frac{dx}{x\ln x}$. The integrand is $\frac{1}{\ln x} \cdot \frac{1}{x}$, and $\frac{1}{x}$ is the derivative of $\ln x$. Take $u = \ln x$, so $du = \frac{dx}{x}$, and find the new limits. Then integrate in $u$ and check.

<details class="solution" markdown>
<summary>Finish</summary>

When $x = e$, $u = \ln e = 1$, and when $x = e^2$, $u = 2$. So the integral is $\int_1^2 \frac{du}{u} = \bigl[\ln\lvert u \rvert\bigr]_1^2 = \ln 2 - \ln 1 = \ln 2 \approx 0.6931$.

Check: the antiderivative in $x$ is $\ln\lvert\ln x\rvert$, whose derivative is $\frac{1}{\ln x} \cdot \frac{1}{x}$, and at the limits it gives $\ln(\ln e^2) - \ln(\ln e) = \ln 2 - \ln 1$. Also, the integrand is $\frac{1}{e} = 0.37$ at $x = e$ and $\frac{1}{2e^2} = 0.07$ at $x = e^2$, over a width of $e^2 - e = 4.67$, so an area near $0.7$ is plausible.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: change every part of the integrand, including $dx$. Writing $\int x\,e^{x^2}\,dx = \int x\,e^u\,du$ leaves an $x$ behind, so the integral is neither in $x$ nor in $u$. The fix is to turn $x\,dx$ into $\frac{1}{2}\,du$ together. If an $x$ is left that can't be rewritten in terms of $u$, the substitution isn't working.

</div>

<div class="warning" markdown>

Watch out: a constant factor can come out of an integral, but a variable factor can't. In $\int e^{x^2}\,dx$ with $u = x^2$ you would need a factor of $2x$ and so $\frac{1}{2x}$ would have to come out. That is not allowed, because it depends on $x$. This is the reason that $\int e^{x^2}\,dx$ can't be done by substitution, while $\int x\,e^{x^2}\,dx$ can.

</div>

<div class="warning" markdown>

Watch out: for a definite integral, the limits belong to the variable. Using $u$ in the integrand with the old limits $x = 0$ and $x = 1$ is wrong. In Example 3 the limits happen to be the same ($0$ and $1$) before and after, which hides the mistake. Try $\int_0^2 x\left(1 + x^2\right)^3dx$: with $u = 1 + x^2$ the limits become 1 and 5, and the integral is $\frac{1}{2}\int_1^5 u^3\,du = \frac{1}{2} \cdot \frac{625 - 1}{4} = 78$. Keeping the limits 0 and 2 would give $\frac{1}{2}\cdot\frac{16}{4} = 2$.

</div>

<div class="warning" markdown>

Watch out: don't forget the absolute value in $\int \frac{du}{u} = \ln\lvert u \rvert + C$, and don't forget $+C$. Dropping the absolute value gives an answer that is wrong where $u < 0$. For a definite integral with no zero of $u$ between the limits, it often doesn't matter, but check that $u$ doesn't change sign.

</div>

If $g'(x) = 0$ somewhere on the interval, the substitution still holds, because the proof only needs $g'$ to be continuous. The danger is the other hypothesis: $f\bigl(g(x)\bigr)g'(x)$ must be continuous on the whole interval. Without that, a formal substitution can produce nonsense. Take $u = -\frac{1}{x}$ in $\int_{-1}^{1}\frac{dx}{x^2}$. Then $du = \frac{dx}{x^2}$, the limits become $u = 1$ and $u = -1$, and the integral looks like $\int_1^{-1}du = -2$. This is the same wrong answer as in Example 4 of the last lesson, and it is wrong for the same reason: the integrand is not continuous at $x = 0$, so the rule does not apply.

## Tricks and shortcuts

A linear inside function doesn't need a $u$. If $\int f(u)\,du = F(u) + C$, then $\int f(ax + b)\,dx = \frac{1}{a}F(ax + b) + C$. This handles $\int (3x + 1)^5\,dx = \frac{(3x + 1)^6}{18} + C$ and $\int \cos(5x - 1)\,dx = \frac{1}{5}\sin(5x - 1) + C$ in one step.

When the numerator is the derivative of the denominator, the integral is a logarithm: $\int \frac{h'(x)}{h(x)}\,dx = \ln\lvert h(x) \rvert + C$. So $\int \frac{2x + 3}{x^2 + 3x + 5}\,dx = \ln\left(x^2 + 3x + 5\right) + C$, with no absolute value because the quadratic has no real roots and is always positive. If the numerator is only a constant multiple of the derivative, adjust: $\int \frac{x}{x^2 + 4}\,dx = \frac{1}{2}\ln\left(x^2 + 4\right) + C$.

Complete the square to reach an inverse tangent. For $\int \frac{dx}{x^2 + 2x + 3}$, write $x^2 + 2x + 3 = (x + 1)^2 + 2$ (see [completing the square](../../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#completing-the-square-to-get-vertex-form)) and let $u = x + 1$, which gives $\int \frac{du}{u^2 + 2} = \frac{1}{\sqrt{2}}\arctan\frac{u}{\sqrt{2}} + C$, using $\int \frac{du}{u^2 + a^2} = \frac{1}{a}\arctan\frac{u}{a} + C$.

If the integral has a power of a function times the function's derivative, $\int f(x)^n f'(x)\,dx$, the answer is always $\frac{f(x)^{n+1}}{n+1}$ for $n \ne -1$. So $\int \sin^4 x\cos x\,dx = \frac{\sin^5 x}{5} + C$.

## In code

The first lines check the substitution rule numerically for $\int_0^1 x\,e^{x^2}\,dx$: the integral in $x$ equals one half the integral of $e^u$ over the new limits $0$ to $1$, and both equal $\frac{e - 1}{2}$. The last lines check an indefinite answer by differentiating it, which is Step 6 of the method.

<details class="code" markdown>
<summary>In code</summary>

```python
import math

def midpoint(f, a, b, n=100000):
    dx = (b - a) / n
    return dx * sum(f(a + (k + 0.5) * dx) for k in range(n))

# u = x^2 turns x e^(x^2) dx into (1/2) e^u du, and the limits 0..1 stay 0..1.
in_x = midpoint(lambda x: x * math.exp(x * x), 0, 1)
in_u = 0.5 * midpoint(math.exp, 0, 1)
print(round(in_x, 6), round(in_u, 6), round((math.e - 1) / 2, 6))
# 0.859141 0.859141 0.859141

# Check an antiderivative by differentiating it: F(x) = e^(x^2) / 2.
F = lambda x: math.exp(x * x) / 2
h = 1e-6
for x in (0.5, 1.2):
    print(round((F(x + h) - F(x - h)) / (2 * h), 5), round(x * math.exp(x * x), 5))
# 0.64201 0.64201
# 5.06483 5.06483

# The wrong answer from dropping the factor 1/2 shows up at once.
G = lambda x: math.exp(x * x)
print(round((G(1.2 + h) - G(1.2 - h)) / (2 * h), 5), round(1.2 * math.exp(1.44), 5))
# 10.12967 5.06483
```

</details>

## FAQ

### Why do the limits change, and do I have to change them?

The limits $a$ and $b$ are values of $x$. Once the integrand is written in $u$, the integral runs over $u$, so the limits must be the values of $u$ at $x = a$ and $x = b$. You can avoid changing them by finding the antiderivative in $x$ first (substitute back) and then using the old limits. Both ways give the same number. The mistake is to mix them: $u$ in the integrand with $x$-limits.

### Why can two correct methods give different-looking answers?

Because antiderivatives differ by a constant, and two correct answers can differ by one. For $\int \sin x\cos x\,dx$, the choice $u = \sin x$ gives $\frac{\sin^2 x}{2} + C$ and the choice $u = \cos x$ gives $-\frac{\cos^2 x}{2} + C$. These differ by $\frac{1}{2}$, since $\frac{\sin^2 x}{2} - \left(-\frac{\cos^2 x}{2}\right) = \frac{\sin^2 x + \cos^2 x}{2} = \frac{1}{2}$. Differentiating either one returns $\sin x\cos x$, which is the real test.

### Why does $\int e^{x^2}\,dx$ have no answer in terms of familiar functions?

It has an antiderivative, by part 1 of the fundamental theorem, but this antiderivative can't be written with finitely many powers, exponentials, logarithms, trig functions and their inverses. A theorem of Liouville proves this for $e^{x^2}$, and its proof is well beyond this book. The function $\int_0^x e^{-t^2}\,dt$ is important enough to have a name: times $\frac{2}{\sqrt{\pi}}$, it is the error function. It measures area under the bell curve of the normal distribution. Probability tables are numerical values of it.

### How do I know which $u$ to pick?

Look for the inside function whose derivative is also in the integrand, and use the table above. If the first guess leaves an $x$ that can't be removed, try another. With practice you will see the pattern in a few seconds. If nothing works, the integral may need another technique, such as parts, or may have no closed form.

## Practice

### Warm-up

1\. Find (a) $\int (3x + 1)^5\,dx$, (b) $\int x\cos\left(x^2\right)dx$ and (c) $\int \sin^4 x\cos x\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The inside is linear with slope 3, so the answer is $\frac{(3x + 1)^6}{6 \cdot 3} + C = \frac{(3x + 1)^6}{18} + C$.

(b) Let $u = x^2$, so $x\,dx = \frac{1}{2}\,du$, and the integral is $\frac{1}{2}\int\cos u\,du = \frac{1}{2}\sin\left(x^2\right) + C$.

(c) Let $u = \sin x$, so $du = \cos x\,dx$, and the integral is $\int u^4\,du = \frac{u^5}{5} + C = \frac{\sin^5 x}{5} + C$.

Check by differentiating: (a) gives $\frac{6(3x + 1)^5 \cdot 3}{18} = (3x + 1)^5$. (b) gives $\frac{1}{2}\cos\left(x^2\right) \cdot 2x = x\cos\left(x^2\right)$. (c) gives $\sin^4 x\cos x$.

</details>

2\. Evaluate (a) $\int_0^2 x\left(x^2 + 1\right)^3\,dx$ and (b) $\int_0^{\pi/2}\sin x\cos^2 x\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Let $u = x^2 + 1$, so $x\,dx = \frac{1}{2}\,du$. The limits become $u = 1$ and $u = 5$. The integral is $\frac{1}{2}\int_1^5 u^3\,du = \frac{1}{2}\cdot\frac{5^4 - 1}{4} = \frac{624}{8} = 78$.

(b) Let $u = \cos x$, so $du = -\sin x\,dx$. The limits become $u = \cos 0 = 1$ and $u = \cos\frac{\pi}{2} = 0$. The integral is $\int_1^0 u^2\,(-du) = \int_0^1 u^2\,du = \frac{1}{3}$.

Check: (a) the integrand is 0 at 0 and $2 \cdot 125 = 250$ at 2 and grows quickly, so an area of 78 over a width of 2 is plausible, and a trapezoid sum gives $78.0$. (b) is a positive integrand with maximum below $0.385$ on a width of about 1.57, and $\frac{1}{3}$ fits.

</details>

3\. Find (a) $\int \frac{e^x}{1 + e^x}\,dx$, (b) $\int \cot x\,dx$ and (c) $\int \frac{(\ln x)^3}{x}\,dx$ for $x > 0$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The numerator is the derivative of the denominator. Let $u = 1 + e^x$, so $du = e^x\,dx$, and the integral is $\int \frac{du}{u} = \ln u + C = \ln\left(1 + e^x\right) + C$. No absolute value is needed, because $1 + e^x > 0$.

(b) Write $\cot x = \frac{\cos x}{\sin x}$ and let $u = \sin x$, so $du = \cos x\,dx$. The answer is $\ln\lvert \sin x \rvert + C$.

(c) Let $u = \ln x$, so $du = \frac{dx}{x}$, and the integral is $\int u^3\,du = \frac{u^4}{4} + C = \frac{(\ln x)^4}{4} + C$.

Check: the derivative of (a) is $\frac{e^x}{1 + e^x}$. The derivative of (b) is $\frac{\cos x}{\sin x}$. The derivative of (c) is $\frac{4(\ln x)^3}{4}\cdot\frac{1}{x}$.

</details>

### Standard

4\. Evaluate $\int_0^1 x^2\sqrt{1 + x^3}\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

Let $u = 1 + x^3$, so $du = 3x^2\,dx$ and $x^2\,dx = \frac{1}{3}\,du$. The limits become $u = 1$ and $u = 2$. Then

$$
\frac{1}{3}\int_1^2 u^{1/2}\,du = \frac{1}{3}\cdot\frac{2}{3}\bigl[u^{3/2}\bigr]_1^2 = \frac{2}{9}\left(2\sqrt{2} - 1\right) \approx 0.4063.
$$

Check: the integrand is 0 at $x = 0$ and $\sqrt{2} = 1.41$ at $x = 1$, and it starts flat, so an area around 0.4 over a width of 1 is plausible. A trapezoid sum with $n = 1000$ gives $0.4063$.

</details>

5\. Find $\int \frac{x^3}{\sqrt{1 - x^2}}\,dx$ on $-1 < x < 1$.

<details class="solution" markdown>
<summary>Solution</summary>

Let $u = 1 - x^2$, so $du = -2x\,dx$, $x\,dx = -\frac{1}{2}\,du$ and $x^2 = 1 - u$. Split the numerator as $x^3\,dx = x^2 \cdot x\,dx$:

$$
\int \frac{(1 - u)}{u^{1/2}}\left(-\frac{1}{2}\right)du = -\frac{1}{2}\int\left(u^{-1/2} - u^{1/2}\right)du = -\frac{1}{2}\left(2u^{1/2} - \frac{2}{3}u^{3/2}\right) + C = -\sqrt{u} + \frac{1}{3}u^{3/2} + C.
$$

Back in $x$: $-\sqrt{1 - x^2} + \frac{1}{3}\left(1 - x^2\right)^{3/2} + C$.

Check: the derivative of $-\left(1 - x^2\right)^{1/2}$ is $\frac{x}{\sqrt{1 - x^2}}$, and the derivative of $\frac{1}{3}\left(1 - x^2\right)^{3/2}$ is $-x\sqrt{1 - x^2}$. Their sum is $\frac{x - x\left(1 - x^2\right)}{\sqrt{1 - x^2}} = \frac{x^3}{\sqrt{1 - x^2}}$.

</details>

6\. (Reviews [completing the square](../../03-high-school/05-quadratics-and-complex-numbers/01-quadratic-functions-and-graphs.md#completing-the-square-to-get-vertex-form).) Find $\int \frac{dx}{x^2 + 2x + 3}$ and check by differentiating.

<details class="solution" markdown>
<summary>Solution</summary>

Complete the square: $x^2 + 2x + 3 = (x + 1)^2 + 2$. Let $u = x + 1$, so $du = dx$. Then $\int\frac{du}{u^2 + 2}$. With $a = \sqrt{2}$, the formula $\int\frac{du}{u^2 + a^2} = \frac{1}{a}\arctan\frac{u}{a}$ gives $\frac{1}{\sqrt{2}}\arctan\frac{x + 1}{\sqrt{2}} + C$.

Check: the derivative of $\arctan\frac{x + 1}{\sqrt{2}}$ is $\frac{1}{1 + \frac{(x + 1)^2}{2}}\cdot\frac{1}{\sqrt{2}}$, and multiplying by $\frac{1}{\sqrt{2}}$ gives $\frac{1}{2 + (x + 1)^2}$, which is $\frac{1}{x^2 + 2x + 3}$.

</details>

### Challenge

7\. Show that $\int \sec x\,dx = \ln\lvert \sec x + \tan x \rvert + C$ by multiplying the integrand by $\frac{\sec x + \tan x}{\sec x + \tan x}$ and then substituting.

<details class="solution" markdown>
<summary>Solution</summary>

Multiplying gives $\frac{\sec^2 x + \sec x\tan x}{\sec x + \tan x}$. Let $u = \sec x + \tan x$. Then $du = \left(\sec x\tan x + \sec^2 x\right)dx$, which is exactly the numerator. So the integral is $\int\frac{du}{u} = \ln\lvert u \rvert + C = \ln\lvert\sec x + \tan x\rvert + C$.

Check: differentiate. $\frac{d}{dx}\ln\lvert\sec x + \tan x\rvert = \frac{\sec x\tan x + \sec^2 x}{\sec x + \tan x} = \frac{\sec x(\tan x + \sec x)}{\sec x + \tan x} = \sec x$.

</details>

8\. For $f$ continuous on $[0, a]$, use the substitution $u = a - x$ to show that $\int_0^a f(x)\,dx = \int_0^a f(a - x)\,dx$. Then use this with the identity $\sin\left(\frac{\pi}{2} - x\right) = \cos x$ to evaluate $I = \int_0^{\pi/2}\frac{\sin x}{\sin x + \cos x}\,dx$.

<details class="solution" markdown>
<summary>Solution</summary>

Let $u = a - x$, so $du = -dx$. When $x = 0$, $u = a$, and when $x = a$, $u = 0$. Then $\int_0^a f(a - x)\,dx = \int_a^0 f(u)(-du) = \int_0^a f(u)\,du$, which is the same as $\int_0^a f(x)\,dx$ with the name of the variable changed.

For $I$, take $a = \frac{\pi}{2}$. Replacing $x$ by $\frac{\pi}{2} - x$ turns $\sin x$ into $\cos x$ and $\cos x$ into $\sin x$, so $I = \int_0^{\pi/2}\frac{\cos x}{\cos x + \sin x}\,dx$. Add the two expressions for $I$:

$$
2I = \int_0^{\pi/2}\frac{\sin x + \cos x}{\sin x + \cos x}\,dx = \int_0^{\pi/2}1\,dx = \frac{\pi}{2},
$$

so $I = \frac{\pi}{4}$.

Check: a midpoint sum of the original integrand with 100,000 rectangles gives $0.785398$, and $\frac{\pi}{4} = 0.785398$. This also makes sense by symmetry, since the integrand goes from 0 to 1 and is $\frac{1}{2}$ at $x = \frac{\pi}{4}$, so its average over the interval is about $\frac{1}{2}$, and $\frac{1}{2}\cdot\frac{\pi}{2} = \frac{\pi}{4}$.

</details>

## Where this shows up

- The next lesson, [integration by parts and trig integrals](04-integration-by-parts-and-trig-integrals.md), uses substitution inside most of its examples, and its trigonometric substitution is a substitution with $x = \sin\theta$. [Partial fractions and improper integrals](05-partial-fractions-and-improper-integrals.md) ends most of its integrals with $\int\frac{du}{u}$.
- In probability, changing a variable in a density is a substitution: if $Y = g(X)$ then the density of $Y$ comes from the same $du = g'(x)\,dx$ (continuous random variables and the normal distribution<!-- link: ../07-probability/04-continuous-random-variables-and-the-normal.md -->). In CS, comparing a sum to an integral bounds quantities such as the harmonic sum $1 + \frac{1}{2} + \cdots + \frac{1}{n}$ by $\ln n$ ([convergence tests](../05-sequences-and-series/03-convergence-tests.md)).
- In economics, discounting a continuous flow with $e^{-rt}$ is an integral that substitution solves in one step, and elasticity and growth rates use $\int\frac{du}{u} = \ln\lvert u \rvert$ (growth rates and CAGR<!-- link: ../../07-economics-math/01-measuring-the-economy/03-growth-rates-and-cagr.md -->).
