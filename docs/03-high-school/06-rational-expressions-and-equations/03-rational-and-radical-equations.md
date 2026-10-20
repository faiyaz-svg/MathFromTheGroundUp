# Rational and radical equations

After this lesson you can solve equations that have the unknown in a denominator, under a root or in a rational exponent, throw out the extra solutions that these methods create, and set up work, current and average speed problems.

Before this: [rational expressions](01-rational-expressions.md), [radicals and rational exponents](../04-radicals-and-polynomials/01-radicals-and-rational-exponents.md) and [solving quadratic equations](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $\dfrac{x}{x - 4} = \dfrac{4}{x - 4} + 2$.
2. Solve $\sqrt{x + 6} = x$.
3. One printer prints a batch in 12 minutes and a second printer prints the same batch in 20 minutes. How long do they take working together?

<details class="solution" markdown>
<summary>Answers</summary>

1. Multiply by $x - 4$: $x = 4 + 2(x - 4)$, so $x = 2x - 4$ and $x = 4$. But $x = 4$ makes a denominator 0, so it is excluded. There is no solution.
2. Square both sides: $x + 6 = x^2$, so $x^2 - x - 6 = (x - 3)(x + 2) = 0$ and $x = 3$ or $x = -2$. Check: $\sqrt{9} = 3$ works, but $\sqrt{4} = 2 \ne -2$. The only solution is $x = 3$.
3. The printers' rates add: $\frac{1}{12} + \frac{1}{20} = \frac{8}{60} = \frac{2}{15}$ of a batch per minute, so one batch takes $\frac{15}{2} = 7.5$ minutes.

</details>

## The idea

To solve $\frac{1}{x} + \frac{1}{2} = 1$ you would like to get rid of the fractions. Multiply both sides by $2x$, the common denominator, and you get $2 + x = 2x$, which is easy: $x = 2$. Clearing the fractions turned a hard-looking equation into a linear one. In the same way, an equation with a square root becomes a polynomial equation if you square both sides.

Both tricks have a price. When you multiply both sides by an expression that can be 0, or square both sides, you create a new equation that has every solution of the old one and possibly more. The extra numbers are not mistakes in arithmetic. They come from the step itself. Take $x = 3$: squaring both sides gives $x^2 = 9$, which has the solutions 3 and $-3$. The new equation does not know that you only wanted the positive one.

So the method for these equations always has two halves: clear the fractions or the roots, solve what is left, and then decide which of the answers belong to the original. The checking is part of the method, not an optional extra.

## Definitions

A **rational equation** is an equation in which the unknown appears in the denominator of a rational expression, such as $\frac{x}{x - 3} = \frac{18}{x^2 - 9}$. A **radical equation** is an equation in which the unknown appears under a root sign, such as $\sqrt{2x + 3} = x$. An equation with a rational exponent, such as $x^{2/3} = 4$, is a radical equation in other clothes, since $x^{2/3}$ means $\left(\sqrt[3]{x}\right)^2$.

Two equations are **equivalent** when they have exactly the same solutions. A solving step is safe when it turns an equation into an equivalent one. An **extraneous solution** (the term from [absolute value equations](../01-algebra-foundations/04-absolute-value-equations-and-inequalities.md#definitions)) is a number that comes out of the solving steps but does not satisfy the original equation. In plain words, an extraneous solution is a false positive created by a step that allows more than the original equation did.

Steps that keep the solutions the same are adding or subtracting the same expression on both sides, and multiplying or dividing both sides by a nonzero number. Two steps are not safe. Multiplying both sides by an expression $c(x)$ keeps all old solutions but can add the zeros of $c(x)$, because at such a number the new equation reads $0 = 0$. Squaring both sides also keeps all old solutions and can add new ones. The next result says exactly which ones.

*Theorem (squaring).* For real numbers $A$ and $B$, $A^2 = B^2$ if and only if $A = B$ or $A = -B$.

We know the difference of squares and the zero-product property ([factoring polynomials](../04-radicals-and-polynomials/03-factoring-polynomials.md#zero-product-property)). We want to describe every pair $A, B$ with equal squares. The plan is to move everything to one side and factor.

*Proof.* The equation $A^2 = B^2$ is equivalent to $A^2 - B^2 = 0$, which factors as $(A - B)(A + B) = 0$. A product is 0 exactly when one factor is 0, so $A - B = 0$ or $A + B = 0$. Each step can be reversed, so this is an "if and only if". $\blacksquare$

Look back: squaring $A = B$ gives $A^2 = B^2$, but the squared equation also allows $A = -B$. So the extraneous solutions of a squaring step are exactly the solutions of the "wrong sign" equation. For $\sqrt{2x + 3} = x$, the extra number is a solution of $\sqrt{2x + 3} = -x$. Odd powers have no such problem: $A^3 = B^3$ holds only when $A = B$, since the cube is one-to-one, so cubing a cube-root equation creates no false solutions.

## How to do it

### Solving a rational equation

1. Factor every denominator, and write the excluded values: the numbers that make any denominator 0.
2. Find the LCD of all the denominators ([rational expressions](01-rational-expressions.md#definitions)).
3. Multiply every term on both sides by the LCD, and cancel. Each term, including terms that are whole numbers, gets multiplied. No denominators should remain.
4. Solve the equation that is left. It is usually linear or quadratic (use [factoring](../04-radicals-and-polynomials/03-factoring-polynomials.md) or the [quadratic formula](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md)).
5. Reject any solution that is an excluded value from Step 1.
6. Check the other solutions in the original equation.

When each side is a single fraction, $\frac{A}{B} = \frac{C}{D}$, you can cross-multiply to $AD = BC$ instead. That is the same as multiplying by $BD$. It does not apply when a side has a sum of fractions.

### Solving a radical equation

1. Isolate one radical on one side of the equation. Move every other term to the other side.
2. Raise both sides to the power equal to the index of that radical. For a square root, square both sides, and square the whole side, not each term: $(a + b)^2 = a^2 + 2ab + b^2$.
3. If a radical is still there, isolate it and raise both sides to a power again.
4. Solve the polynomial equation you get.
5. Check every solution in the original equation. For an even index this step cannot be skipped.

A quick filter saves work. In $\sqrt{\ldots} = E$, the principal root is never negative, so any solution must make $E \ge 0$. In $\sqrt{2x + 3} = x$ this says $x \ge 0$, which rules out $-1$ before you check anything.

### Equations with rational exponents

1. Isolate the power $x^{m/n}$ (or the expression raised to $\frac{m}{n}$), with $\frac{m}{n}$ in lowest terms.
2. Undo the numerator first by taking the $m$-th root of both sides. If $m$ is even, there are two possibilities, $+$ and $-$ (and none if the right side is negative). If $m$ is odd, there is one.
3. Undo the root by raising both sides to the power $n$.
4. Check, remembering that for even $n$ the base must be at least 0.

For an equation of quadratic type such as $x^{2/3} - x^{1/3} - 6 = 0$, substitute $u = x^{1/3}$ so that $x^{2/3} = u^2$, solve for $u$, and then go back to $x = u^3$.

### Work problems

If a job takes $a$ hours, the worker finishes $\frac{1}{a}$ of it per hour: that is the rate. When people or machines work together, their rates add. Since (rate) $\times$ (time) = (fraction of the job done),

$$
\left(\frac{1}{a} + \frac{1}{b}\right) t = 1.
$$

1. Let the whole job be 1. Write each worker's rate as $\frac{1}{\text{time alone}}$.
2. Add the rates of those who work together.
3. Set (total rate) $\times$ (time) equal to 1, or to the fraction of the job that gets done.
4. Solve, which is a rational equation, and reject answers that don't make sense (a negative time).
5. Check by computing the fraction each worker does.

Solving for $t$ gives $t = \frac{ab}{a + b}$, product over sum. The combined time is always shorter than either time alone. The pattern $\frac{1}{t} = \frac{1}{a} + \frac{1}{b}$ is the same as for two resistors in parallel in physics.

### Rate, distance and time with a current

Distance equals speed times time, so the time is distance divided by speed. A boat with still-water speed $v$ in a current $c$ goes at $v + c$ downstream and $v - c$ upstream. A trip of $d$ kilometres each way takes $\frac{d}{v + c} + \frac{d}{v - c}$ hours. Setting that equal to the total time gives a rational equation. The speed $v - c$ has to be positive, or the boat never gets upstream, which is a built-in excluded value.

### The harmonic mean

If you drive the same distance twice, at speed $a$ and then at speed $b$, the average speed is not $\frac{a + b}{2}$. The average speed is the total distance divided by the total time.

*Theorem (average speed).* If a trip covers a distance $d$ at speed $a$ and then the same distance $d$ at speed $b$, with $a, b > 0$, the average speed for the whole trip is

$$
\frac{2ab}{a + b},
$$

the harmonic mean of $a$ and $b$. It is never more than the arithmetic mean $\frac{a + b}{2}$, and it equals it only when $a = b$.

We know that average speed is total distance over total time. We want a formula in $a$ and $b$ alone. The plan is to compute the two times, add them, and divide.

*Proof.* The first leg takes $\frac{d}{a}$ and the second takes $\frac{d}{b}$, so the total time is $\frac{d}{a} + \frac{d}{b} = \frac{d(a + b)}{ab}$. The total distance is $2d$, so the average speed is $2d \div \frac{d(a + b)}{ab} = \frac{2ab}{a + b}$. The difference from the arithmetic mean is

$$
\frac{a + b}{2} - \frac{2ab}{a + b} = \frac{(a + b)^2 - 4ab}{2(a + b)} = \frac{(a - b)^2}{2(a + b)} \ge 0,
$$

which is 0 only when $a = b$. $\blacksquare$

Look back: the distance $d$ cancelled, so the answer doesn't depend on how long the trip is. The harmonic mean is smaller than the arithmetic mean because you spend more time at the slow speed, so the slow speed counts for more. Going 60 km/h out and 40 km/h back gives $\frac{2 \cdot 60 \cdot 40}{100} = 48$ km/h, not 50.

## Worked examples

<div class="example" markdown>

### Example 1: a rational equation with an extraneous solution

Solve $\dfrac{x}{x - 3} = \dfrac{18}{x^2 - 9}$.

Step 1: $x^2 - 9 = (x - 3)(x + 3)$. The excluded values are $x = 3$ and $x = -3$.

Step 2: the LCD is $(x - 3)(x + 3)$.

Step 3: multiply both sides by it. On the left, the $x - 3$ cancels and leaves $x(x + 3)$. On the right, everything cancels except the 18:

$$
x(x + 3) = 18.
$$

Step 4: expand and move everything to one side, $x^2 + 3x - 18 = 0$. Factor: the numbers 6 and $-3$ have product $-18$ and sum 3, so $(x + 6)(x - 3) = 0$, and $x = -6$ or $x = 3$.

Step 5: $x = 3$ is an excluded value, so it is extraneous. At $x = 3$ both sides of the original equation have a zero denominator. The new equation $x(x + 3) = 18$ accepted it because we multiplied by $x - 3$, which is 0 there.

Step 6: check $x = -6$. The left side is $\frac{-6}{-9} = \frac{2}{3}$, and the right side is $\frac{18}{36 - 9} = \frac{18}{27} = \frac{2}{3}$. The solution is $x = -6$.

<div class="warning" markdown>

Watch out at Step 3: multiply every term. If the equation were $\frac{x}{x - 3} + 1 = \ldots$, the 1 would also become $(x - 3)(x + 3)$. Forgetting to multiply a whole-number term is the most common slip.

</div>

</div>

<div class="example" markdown>

### Example 2: isolate the radical first

Solve $\sqrt{3x + 1} - 1 = x$.

Step 1: isolate the radical by adding 1: $\sqrt{3x + 1} = x + 1$. Squaring the original form directly would be a mistake, because $(\sqrt{3x + 1} - 1)^2$ still contains a radical.

Step 2: square both sides. The right side is a sum, so square the whole of it: $3x + 1 = (x + 1)^2 = x^2 + 2x + 1$.

Step 4: simplify to $0 = x^2 - x$, so $x(x - 1) = 0$ and $x = 0$ or $x = 1$.

Step 5: check each in the original equation. At $x = 0$: $\sqrt{1} - 1 = 0$, which equals $x$. At $x = 1$: $\sqrt{4} - 1 = 1$, which equals $x$. Both solutions work. The filter agrees: both give $x + 1 \ge 0$.

It is fine that nothing was extraneous. Squaring allows extra solutions but does not force them. Any extra solution here would solve $\sqrt{3x + 1} = -(x + 1)$, which needs $x + 1 \le 0$ and also $x \ge -\frac{1}{3}$ so that the root exists. No number does both, so there are none. Step 3 was not needed, because no radical was left after squaring.

</div>

<div class="example" markdown>

### Example 3: rational exponents

Solve $x^{2/3} - x^{1/3} - 6 = 0$.

The equation is quadratic in $x^{1/3}$. Let $u = x^{1/3}$, so $x^{2/3} = u^2$ and the equation is $u^2 - u - 6 = 0$. Factor: $(u - 3)(u + 2) = 0$, so $u = 3$ or $u = -2$.

Go back to $x$ by cubing: $x = 3^3 = 27$ or $x = (-2)^3 = -8$. The denominator of the exponent is 3, which is odd, so negative $x$ is allowed.

Check $x = 27$: $27^{2/3} = 9$ and $27^{1/3} = 3$, so $9 - 3 - 6 = 0$. Check $x = -8$: $(-8)^{2/3} = (-2)^2 = 4$ and $(-8)^{1/3} = -2$, so $4 + 2 - 6 = 0$. Both solutions are valid.

A single-power version shows the $\pm$. For $x^{2/3} = 4$, take the square root of both sides, $x^{1/3} = \pm 2$, then cube: $x = 8$ or $x = -8$. And for $x^{3/2} = 27$, take the cube root, $x^{1/2} = 3$, and square: $x = 9$. Here only $x \ge 0$ is allowed, because the denominator 2 is even.

</div>

<div class="example" markdown>

### Example 4: two machines (finish it yourself)

Machine A takes 3 hours longer than machine B to do a job alone. Together they finish it in 2 hours. How long does each take alone?

Step 1: let machine B take $x$ hours alone, so machine A takes $x + 3$ hours. The rates are $\frac{1}{x}$ and $\frac{1}{x + 3}$ jobs per hour.

Step 2 and 3: together for 2 hours they do the whole job:

$$
\left(\frac{1}{x} + \frac{1}{x + 3}\right) \cdot 2 = 1, \qquad\text{that is}\qquad \frac{1}{x} + \frac{1}{x + 3} = \frac{1}{2}.
$$

The excluded values are $x = 0$ and $x = -3$. The LCD is $2x(x + 3)$. Multiply every term and solve the quadratic you get. Then reject any answer that is not a sensible time, and give both machines' times.

<details class="solution" markdown>
<summary>Finish</summary>

Multiplying by $2x(x + 3)$: $2(x + 3) + 2x = x(x + 3)$, so $4x + 6 = x^2 + 3x$ and $x^2 - x - 6 = 0$. Factor: $(x - 3)(x + 2) = 0$, so $x = 3$ or $x = -2$.

A negative time makes no sense, so $x = -2$ is rejected. Machine B takes 3 hours alone and machine A takes 6 hours.

Check: the rates are $\frac{1}{3} + \frac{1}{6} = \frac{1}{2}$ of the job per hour, so the job takes 2 hours. The shortcut also works: $\frac{3 \cdot 6}{3 + 6} = 2$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for skipping the check. For a radical equation the check is not optional. In $\sqrt{x + 6} = x$ the candidate $x = -2$ looks fine after squaring, but the left side is $\sqrt{4} = 2$ and the right side is $-2$. The square root symbol means the non-negative root, and squaring forgot that.

</div>

<div class="warning" markdown>

Watch out: squaring a sum term by term. $\left(\sqrt{x + 7} + 2\right)^2$ is not $x + 7 + 4$. It is $x + 7 + 4\sqrt{x + 7} + 4$, and the middle term is a radical that stays. After this step you isolate that radical and square again, as in Practice problem 4.

</div>

<div class="warning" markdown>

Watch out: dividing by a variable expression loses solutions. In $x(x - 3) = 2(x - 3)$, dividing both sides by $x - 3$ leaves $x = 2$ and loses the solution $x = 3$. Move everything to one side and factor instead: $(x - 3)(x - 2) = 0$. In a rational equation, a solution lost this way might have been an excluded value, but you will not know unless you factor.

</div>

<div class="warning" markdown>

Watch out: the average of two speeds. If you drive 60 km/h out and 40 km/h back, the average speed is 48 km/h, not 50. The arithmetic mean of the speeds is right only when you spend the same time at each speed. When you cover the same distance, the harmonic mean is the right one.

</div>

An equation with no solutions is a legitimate answer: the empty set. It happens in the Quick check, when the only candidate is an excluded value, and in $\sqrt{x - 2} = -3$, where a square root cannot equal a negative number. Squaring gives $x - 2 = 9$ and the candidate $x = 11$, which fails: $\sqrt{9} = 3$, not $-3$. You can see the problem before squaring, since the left side is never negative.

Answers can be untidy. The equation $\frac{1}{x - 1} + \frac{1}{x + 1} = 1$ clears to $2x = x^2 - 1$, so $x^2 - 2x - 1 = 0$ and $x = 1 \pm \sqrt{2}$. Both are valid, since neither is $\pm 1$. A decimal answer such as $x \approx 2.414$ is fine in a real-world problem, but give the exact form when the problem is only algebra.

## Tricks and shortcuts

For a work problem with two workers, use product over sum, $t = \frac{ab}{a + b}$. The printers in the Quick check give $\frac{12 \cdot 20}{32} = 7.5$ minutes. If three workers are involved, add three rates.

To check a rational equation quickly, plug each candidate into both sides of the original on a calculator. A candidate that satisfies the cleared equation but not the original shows up at once: one side gives an error, or the two sides differ.

For a work or current problem, a sensible-answer test often rejects the second root without a check. A time must be positive, and a boat speed must be bigger than the current. In Practice problem 5 the other root is $-\frac{2}{5}$.

## In code

Python can solve the equations exactly with SymPy, and a short filter shows the extraneous solution of a squaring step directly. The last lines compute the harmonic mean in two ways.

<details class="code" markdown>
<summary>In code</summary>

```python
import statistics
from math import isclose
from sympy import symbols, solve, Eq, sqrt, Rational

x = symbols("x")

# Squaring creates a candidate that the check rejects.
candidates = solve(Eq(2*x + 3, x**2), x)
print(candidates)                       # [-1, 3]
valid = [c for c in candidates if isclose(float(sqrt(2*c + 3)), float(c))]
print(valid)                            # [3]

# A rational equation: x = 3 is excluded, so only -6 remains.
print(solve(Eq(x/(x - 3), 18/(x**2 - 9)), x))                      # [-6]

# Two machines, one 3 hours slower than the other, 2 hours together.
print(solve(Eq(1/x + 1/(x + 3), Rational(1, 2)), x))               # [-2, 3]

# Harmonic mean: 60 km/h out and 40 km/h back.
print(2*60*40/(60 + 40), statistics.harmonic_mean([60, 40]))       # 48.0 48.0
```

The first `solve` returns both candidates from the squared equation, and the filter keeps only the one that satisfies the original. The third `solve` returns $-2$ as well as 3; the code does not know that a time cannot be negative, so rejecting $-2$ is still your job.

</details>

## FAQ

### Why does squaring add solutions but never remove them?

If $A = B$, then $A^2 = B^2$, so every solution of the original is a solution of the squared equation. The reverse fails because $A^2 = B^2$ also allows $A = -B$, as the theorem above shows. Squaring is a step in only one direction, which is why the check is needed. Taking an odd power, such as cubing, is reversible, and then no check is needed.

### Do I have to check a rational equation, or is comparing with the excluded values enough?

If every step was an algebra step you trust, comparing with the excluded values is enough: the only danger of multiplying by the LCD is the zeros of the LCD, and those are exactly the excluded values. A check in the original equation also catches arithmetic slips, so it is worth doing when it takes little time.

### Why do rates add but times don't?

Rates measure how much of the job gets done per hour, and two workers in the same hour do the two amounts together, so the amounts add. Times are the other way round, the reciprocal of a rate. Two printers that each take 12 minutes do not take 24 minutes together. They take 6, since together they do twice as much per minute.

### Why is the harmonic mean the right average for speeds, but not for everything?

An average is a total divided by a count of something. For a speed, the total is the distance and the count is the time. When you drive equal distances, the times are different, and the harmonic mean accounts for it. When you drive for equal times, the distances differ and the arithmetic mean is right: an hour at 60 and an hour at 40 cover 100 km in 2 hours, an average of 50.

## Practice

### Warm-up

1\. Solve and check: (a) $\dfrac{2}{x} + \dfrac{1}{3} = \dfrac{5}{6}$, (b) $\dfrac{3}{x - 2} = \dfrac{4}{x + 1}$, (c) $\dfrac{x}{x - 5} = \dfrac{5}{x - 5}$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The excluded value is $x = 0$ and the LCD is $6x$. Multiplying every term: $12 + 2x = 5x$, so $x = 4$. Check: $\frac{2}{4} + \frac{1}{3} = \frac{5}{6}$.
- (b) The excluded values are $2$ and $-1$. Cross-multiplying: $3(x + 1) = 4(x - 2)$, so $3x + 3 = 4x - 8$ and $x = 11$. Check: $\frac{3}{9} = \frac{1}{3}$ and $\frac{4}{12} = \frac{1}{3}$.
- (c) Multiplying by $x - 5$ gives $x = 5$, which is an excluded value. There is no solution.

</details>

2\. Solve (a) $\sqrt{x + 4} = 3$ and (b) $\sqrt{x - 2} = -3$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Square both sides: $x + 4 = 9$, so $x = 5$. Check: $\sqrt{9} = 3$.

(b) A principal square root is never negative, so there is no solution. If you square anyway you get $x - 2 = 9$ and $x = 11$, but the check fails: $\sqrt{11 - 2} = 3 \ne -3$.

</details>

3\. Solve (a) $x^{3/2} = 8$ and (b) $x^{2/3} = 9$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Take the cube root of both sides: $x^{1/2} = 2$, and square: $x = 4$. Check: $4^{3/2} = 2^3 = 8$.

(b) Take the square root of both sides: $x^{1/3} = \pm 3$, and cube: $x = 27$ or $x = -27$. Check: $27^{2/3} = 3^2 = 9$ and $(-27)^{2/3} = (-3)^2 = 9$. Both work, since the denominator 3 is odd.

</details>

### Standard

4\. Solve $\sqrt{x + 7} - \sqrt{x - 1} = 2$.

<details class="solution" markdown>
<summary>Solution</summary>

Isolate one radical: $\sqrt{x + 7} = 2 + \sqrt{x - 1}$. Square both sides, squaring the whole right side:

$$
x + 7 = 4 + 4\sqrt{x - 1} + (x - 1) = x + 3 + 4\sqrt{x - 1}.
$$

Subtract $x + 3$: $4 = 4\sqrt{x - 1}$, so $\sqrt{x - 1} = 1$. Square again: $x - 1 = 1$, so $x = 2$.

Check: $\sqrt{9} - \sqrt{1} = 3 - 1 = 2$.

</details>

5\. A boat travels 24 km upstream and 24 km back, and the round trip takes 5 hours. The current is 2 km/h. What is the speed of the boat in still water?

<details class="solution" markdown>
<summary>Solution</summary>

Let $v$ be the still-water speed in km/h. The speeds are $v - 2$ upstream and $v + 2$ downstream, and $v > 2$. The times add to 5:

$$
\frac{24}{v - 2} + \frac{24}{v + 2} = 5.
$$

Multiply by $(v - 2)(v + 2)$: $24(v + 2) + 24(v - 2) = 5(v^2 - 4)$, so $48v = 5v^2 - 20$ and $5v^2 - 48v - 20 = 0$. Factor: $(5v + 2)(v - 10) = 0$, so $v = -\frac{2}{5}$ or $v = 10$. A speed must exceed 2, so $v = 10$ km/h.

Check: upstream $\frac{24}{8} = 3$ hours, downstream $\frac{24}{12} = 2$ hours, total 5 hours.

</details>

6\. Printer A takes 4 hours longer than printer B to do a print run alone. Together they finish in 1.5 hours. How long does each take alone?

<details class="solution" markdown>
<summary>Solution</summary>

Let B take $x$ hours, so A takes $x + 4$. The rates add up to $\frac{1}{1.5} = \frac{2}{3}$ of a run per hour:

$$
\frac{1}{x} + \frac{1}{x + 4} = \frac{2}{3}.
$$

Multiply by $3x(x + 4)$: $3(x + 4) + 3x = 2x(x + 4)$, so $6x + 12 = 2x^2 + 8x$ and $2x^2 + 2x - 12 = 0$. Divide by 2: $x^2 + x - 6 = (x + 3)(x - 2) = 0$. The time is positive, so $x = 2$: printer B takes 2 hours and printer A takes 6 hours.

Check: $\frac{1}{2} + \frac{1}{6} = \frac{2}{3}$ of a run per hour, and the product-over-sum shortcut agrees: $\frac{2 \cdot 6}{2 + 6} = 1.5$ hours.

</details>

### Challenge

7\. You drive 90 km out at 60 km/h and drive back at a speed $v$. (a) What must $v$ be for the average speed of the round trip to be 45 km/h? (b) Can you average 120 km/h for the round trip, whatever speed you drive back at?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The average speed is the harmonic mean, $\frac{2 \cdot 60 \cdot v}{60 + v} = 45$. Multiply by $60 + v$: $120v = 2700 + 45v$, so $75v = 2700$ and $v = 36$ km/h.

Check: the out leg takes $\frac{90}{60} = 1.5$ hours and the return takes $\frac{90}{36} = 2.5$ hours. The total distance is 180 km and the total time is 4 hours, so the average speed is $\frac{180}{4} = 45$ km/h.

(b) Set $\frac{120v}{60 + v} = 120$. Multiply: $120v = 7200 + 120v$, which gives $0 = 7200$, so there is no solution. In words: 180 km at an average of 120 km/h takes 1.5 hours, but the out leg alone already took 1.5 hours, so there is no time left for the return, however fast you drive.

</details>

8\. (Reviews [solving quadratic equations](../05-quadratics-and-complex-numbers/02-solving-quadratic-equations.md).) Solve $\dfrac{1}{x - 1} + \dfrac{1}{x + 1} = 1$. Give exact answers and decimals.

<details class="solution" markdown>
<summary>Solution</summary>

The excluded values are $x = 1$ and $x = -1$. Multiply every term by $(x - 1)(x + 1)$: $(x + 1) + (x - 1) = (x - 1)(x + 1)$, so $2x = x^2 - 1$ and $x^2 - 2x - 1 = 0$.

The quadratic formula gives $x = \frac{2 \pm \sqrt{4 + 4}}{2} = 1 \pm \sqrt{2}$, which is about $2.414$ and $-0.414$. Neither is 1 or $-1$, so both are valid.

Check $x = 1 + \sqrt{2}$: $\frac{1}{\sqrt{2}} + \frac{1}{2 + \sqrt{2}} \approx 0.7071 + 0.2929 = 1.0000$. Check $x = 1 - \sqrt{2} \approx -0.4142$: $\frac{1}{-1.4142} + \frac{1}{0.5858} \approx -0.7071 + 1.7071 = 1.0000$.

</details>

## Where this shows up

- The next lesson, [polynomial and rational inequalities](04-polynomial-and-rational-inequalities.md), asks where a rational expression is positive or negative instead of equal to a number. Its warning is the cousin of this lesson's: multiplying an inequality by an expression of unknown sign is as unsafe as multiplying an equation by one that might be 0.
- Rational equations appear in computer science as Amdahl's law: a program that is 90% parallel runs $S = \frac{1}{0.1 + 0.9/n}$ times faster on $n$ processors, and setting $S = 5$ gives $n = 9$ processors. The harmonic mean is how the F1 score of a classifier combines precision and recall: for precision 0.9 and recall 0.5, it is $\frac{2 \cdot 0.9 \cdot 0.5}{1.4} \approx 0.64$, lower than the average 0.7 because the weak number counts for more.
- In finance, buying the same dollar amount of a stock at two different prices gives an average price that is the harmonic mean of the prices. Buying \$100 at \$20 and \$100 at \$25 gets $5 + 4 = 9$ shares for \$200, an average of about \$22.22, below \$22.50. [Exponential and logarithmic equations](../07-exponentials-and-logarithms/04-exponential-and-logarithmic-equations.md) has its own extraneous solutions, found by the same check.
