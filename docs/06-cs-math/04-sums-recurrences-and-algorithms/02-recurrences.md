# Recurrences

After this lesson you can write the recurrence for the cost of a recursive function, solve it by unrolling, solve a linear recurrence with constant coefficients through its characteristic equation (distinct or repeated roots), find the closed form of the Fibonacci numbers, and handle a nonhomogeneous recurrence by adding a particular solution.

Before this: [sequences and recursion](../../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md), [sums and closed forms](01-sums-and-closed-forms.md) and [mathematical induction](../../04-proofs-and-logic/05-induction/01-mathematical-induction.md). [Complex numbers](../../03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md) are needed only for a remark.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A sequence has $T(0) = 2$ and $T(n) = T(n-1) + 3$ for $n \ge 1$. Find a formula for $T(n)$.
2. Solve $a_n = 5a_{n-1} - 6a_{n-2}$ with $a_0 = 1$ and $a_1 = 0$.
3. Write a recurrence for the number of times `step()` is called by this function, counting $n$ as the input size.

    ```python
    def f(n):
        if n <= 1:
            return
        f(n // 2)
        f(n // 2)
        for i in range(n):
            step()
    ```

<details class="solution" markdown>
<summary>Answers</summary>

1. Each step adds 3, so after $n$ steps the value is $2 + 3n$.
2. Try $a_n = r^n$. Then $r^2 = 5r - 6$, so $(r - 2)(r - 3) = 0$ and $a_n = A\,2^n + B\,3^n$. From $a_0 = 1$: $A + B = 1$. From $a_1 = 0$: $2A + 3B = 0$. So $B = -2$, $A = 3$, and $a_n = 3 \cdot 2^n - 2 \cdot 3^n$. Check: $a_2 = 5 \cdot 0 - 6 \cdot 1 = -6$ and $12 - 18 = -6$.
3. The function makes two calls on inputs of about half the size and then runs a loop of $n$ steps, so $T(n) = 2T(n/2) + n$, with $T(1) = 0$.

</details>

## The idea

Most of the algorithms in a data structures course are recursive, and the cost of a recursive function is described by the function itself. To search a sorted list of $n$ items by binary search, you look at the middle item and then search half the list: the cost $T(n)$ equals the cost of one comparison plus $T(n/2)$. To sort by merge sort, you sort two halves and then merge them: $T(n) = 2T(n/2) + n$. To move $n$ disks in the Towers of Hanoi, you move $n - 1$ disks twice and one disk once: $T(n) = 2T(n-1) + 1$.

Each of these is a **recurrence**: an equation that gives a quantity in terms of the same quantity on smaller inputs. A recurrence says what the cost is made of, but not how large it is. To find out whether the Hanoi solution is practical, or whether merge sort is faster than the simple quadratic sorts, you solve the recurrence: you find a formula or at least a growth rate.

This lesson builds a toolbox for solving recurrences. Unrolling works for the simplest ones. Guessing and checking by induction works when you can see the pattern. For a large family, linear recurrences with constant coefficients such as Fibonacci's, a general method gives the exact formula every time. Recurrences with a division in them, like $T(n) = 2T(n/2) + n$, are handled by their own theorem in [divide and conquer and the master theorem](05-divide-and-conquer-and-master-theorem.md), and unrolling gets us started here.

## Definitions

A **recurrence relation** for a sequence $(a_n)$ is an equation that gives $a_n$ in terms of earlier terms, valid for every $n$ from some starting index on. A recurrence together with enough **initial conditions** (the first few terms) determines the sequence. A **solution** is a formula that gives $a_n$ directly, or any sequence that satisfies both the recurrence and the initial conditions. These were defined in [sequences and recursion](../../03-high-school/11-sequences-series-and-counting/01-sequences-and-recursion.md); this lesson is about solving them.

In plain words, the recurrence is the rule for one step, and solving it means finding the formula that jumps straight to step $n$.

A recurrence has **order** $k$ if $a_n$ depends on the previous $k$ terms, $a_{n-1}, \dots, a_{n-k}$. A **linear homogeneous recurrence with constant coefficients** of order $k$ has the form

$$
a_n = c_1 a_{n-1} + c_2 a_{n-2} + \cdots + c_k a_{n-k}, \qquad c_k \ne 0,
$$

where $c_1, \dots, c_k$ are constants. The Fibonacci recurrence $F_n = F_{n-1} + F_{n-2}$ is one, with $c_1 = c_2 = 1$. In plain words, "linear" means the earlier terms are only multiplied by numbers and added, with no squares or products of terms, and "homogeneous" means there is nothing else added, so the zero sequence is a solution. "Constant coefficients" means the multipliers don't depend on $n$.

A recurrence is **nonhomogeneous** if an extra term $g(n)$ is added: $a_n = c_1 a_{n-1} + \cdots + c_k a_{n-k} + g(n)$. The Hanoi recurrence $h_n = 2h_{n-1} + 1$ is nonhomogeneous, with $g(n) = 1$.

The **characteristic equation** of the homogeneous recurrence above is

$$
r^k = c_1 r^{k-1} + c_2 r^{k-2} + \cdots + c_k.
$$

For order 2 it is $r^2 = c_1 r + c_2$, or $r^2 - c_1 r - c_2 = 0$. Its roots are the **characteristic roots**. In plain words, the characteristic equation is what you get by trying $a_n = r^n$ in the recurrence and dividing by the smallest power of $r$. The roots are the values of $r$ for which that guess works.

A **particular solution** of a nonhomogeneous recurrence is any one sequence $p_n$ that satisfies the recurrence, ignoring the initial conditions. In plain words, it is one answer you found by guessing, and you don't need it to match the starting values.

## How to do it

### From code to a recurrence

1. Decide what $n$ measures, the input size that shrinks: the length of a list, the number of disks, the number of digits.
2. Find the base case, the input size where the function stops calling itself, and count its cost.
3. For the recursive case, count the work done outside the recursive calls, as a function of $n$, and count the number of recursive calls and the size of each.
4. Write $T(n)$ as the sum of the costs of the recursive calls plus the outside work.
5. Check by running the code for small $n$ with a counter, or by hand.

In step 3, a division such as $n/2$ is shorthand: a real list of 7 items splits into pieces of 3 and 4. Until the master theorem lesson, solve for $n$ that are powers of 2, where the halves are exact. The result describes the other $n$ as well, and the master theorem lesson says why.

### Unrolling

**Unrolling** (also called iteration or repeated substitution) means substituting the recurrence into itself until the pattern is visible.

1. Write $T(n)$ in terms of $T(n-1)$, or $T(n/2)$. Substitute the recurrence again into the smaller term. Do this three or four times without simplifying too much.
2. Name the pattern after $i$ substitutions: $T(n) = (\text{what has accumulated}) + (\text{the remaining } T)$.
3. Choose $i$ so that the remaining $T$ is the base case. For $T(n-1)$ that is $i = n$ (or $n - 1$); for $T(n/2)$ with $n = 2^t$ it is $i = t$.
4. Evaluate the accumulated part, usually a sum or a geometric series.
5. The pattern was a guess, so check it for small $n$, and prove it by induction if the answer matters.

For example, $T(n) = T(n-1) + n$ with $T(0) = 0$ unrolls to $T(n) = n + (n-1) + T(n-2) = n + (n-1) + (n-2) + T(n-3) = \cdots$, so after reaching the base case $T(n) = n + (n-1) + \cdots + 1 = \frac{n(n+1)}{2}$. The pattern is a sum from [sums and closed forms](01-sums-and-closed-forms.md), which is why that lesson comes first.

### Guess and verify

When unrolling gets messy, compute the first values, guess a formula and prove it by induction. The earlier lesson used this on the Hanoi numbers: the values $0, 1, 3, 7, 15$ suggest $2^n - 1$, and induction confirms it. For a sequence whose differences are polynomials, the guess can be a polynomial. If $T(n) = T(n-1) + n^2$, the values $0, 1, 5, 14, 30$ have first differences $1, 4, 9, 16$, second differences $3, 5, 7$ and constant third differences $2, 2$, which says $T$ is a cubic. A cubic is determined by four values, and fitting them gives $T(n) = \frac{n(n+1)(2n+1)}{6}$, the sum of squares. The verification is the induction step: $\frac{n(n+1)(2n+1)}{6} + (n+1)^2 = \frac{(n+1)(n+2)(2n+3)}{6}$.

### Linear homogeneous recurrences: the characteristic equation

*Theorem.* Let $c_1$ and $c_2$ be numbers with $c_2 \ne 0$, and let $(a_n)$ satisfy $a_n = c_1 a_{n-1} + c_2 a_{n-2}$ for every $n \ge 2$. Let $r_1$ and $r_2$ be the two roots of $r^2 = c_1 r + c_2$.

- (a) If $r_1 \ne r_2$, then there are numbers $A$ and $B$ with $a_n = A\,r_1^n + B\,r_2^n$ for every $n \ge 0$, and the initial values $a_0, a_1$ determine $A$ and $B$ uniquely.
- (b) If $r_1 = r_2 = r$, then there are numbers $A$ and $B$ with $a_n = (A + Bn)\,r^n$ for every $n \ge 0$.

We know the recurrence and two initial values, and that the quadratic formula gives the roots. We want a formula for all $n$. The plan has four parts: show that $r^n$ solves the recurrence exactly when $r$ is a root, show that combinations of solutions are solutions, show that a combination can be fitted to any initial values, and note that the recurrence leaves no freedom after that.

*Proof of (a).* First, a geometric sequence $r^n$ satisfies the recurrence when $r^n = c_1 r^{n-1} + c_2 r^{n-2}$. We have $r \ne 0$, since $r = 0$ would give $0 = c_2$. Dividing by $r^{n-2}$ gives $r^2 = c_1 r + c_2$, which is true for $r = r_1$ and $r = r_2$. So $r_1^n$ and $r_2^n$ are solutions.

Second, if $(x_n)$ and $(y_n)$ both satisfy the recurrence, so does $A x_n + B y_n$, because the recurrence is linear and homogeneous:

$$
A x_n + B y_n = A(c_1 x_{n-1} + c_2 x_{n-2}) + B(c_1 y_{n-1} + c_2 y_{n-2}) = c_1 (A x_{n-1} + B y_{n-1}) + c_2 (A x_{n-2} + B y_{n-2}).
$$

So $A\,r_1^n + B\,r_2^n$ is a solution for all numbers $A$ and $B$.

Third, choose $A$ and $B$ to match the initial values: $A + B = a_0$ and $A r_1 + B r_2 = a_1$. Subtracting $r_1$ times the first equation from the second gives $B(r_2 - r_1) = a_1 - r_1 a_0$. Since $r_2 \ne r_1$, there is exactly one solution, $B = \frac{a_1 - r_1 a_0}{r_2 - r_1}$ and $A = a_0 - B$.

Fourth, the recurrence gives each term from the two before it, so the sequence is determined by $a_0$ and $a_1$. The formula with the fitted $A$ and $B$ satisfies the recurrence and the same two initial values, so it is the sequence. $\blacksquare$

*Proof of (b).* A double root means the discriminant $c_1^2 + 4c_2$ is 0, so $r = \frac{c_1}{2}$ and $c_2 = -r^2$. By part (a)'s first step, $r^n$ is a solution. We check that $n\,r^n$ is one too. The recurrence asks for $n r^n = c_1 (n-1) r^{n-1} + c_2 (n-2) r^{n-2}$. Divide by $r^{n-2}$ and substitute $c_1 = 2r$ and $c_2 = -r^2$:

$$
n r^2 \overset{?}{=} 2r(n-1)r - r^2(n-2) = 2nr^2 - 2r^2 - nr^2 + 2r^2 = n r^2.
$$

So $n\,r^n$ is a solution, and by the second step above so is $(A + Bn)r^n$. To match the initial values, put $A = a_0$ and then solve $(A + B) r = a_1$ for $B = \frac{a_1}{r} - a_0$, which works because $r \ne 0$. The fourth step is the same as before. $\blacksquare$

Look back: the idea is to find enough simple solutions to fit the starting values. A recurrence of order 2 has two free starting values, so it needs two independent solutions. A double root gives only one of the form $r^n$, and the extra factor $n$ supplies the second. For order $k$ the same pattern holds: a root of multiplicity $m$ contributes $r^n, n\,r^n, \dots, n^{m-1} r^n$, and the $k$ constants are fitted to the $k$ initial values. This book states that general version without proof.

<div class="note" markdown>

If $c_1^2 + 4c_2 < 0$ the roots are complex numbers, $r = \rho(\cos\theta \pm i \sin\theta)$, and part (a) still holds with complex $A$ and $B$. For real starting values the answer is real, and it has the form $\rho^n(A' \cos n\theta + B' \sin n\theta)$. For example, $a_n = 2a_{n-1} - 2a_{n-2}$ has roots $1 \pm i = \sqrt{2}\left(\cos\frac{\pi}{4} \pm i\sin\frac{\pi}{4}\right)$, and with $a_0 = 0$ and $a_1 = 1$ the solution is $a_n = (\sqrt{2})^n \sin\frac{n\pi}{4}$: the values $0, 1, 2, 2, 0, -4, -8, -8, 0, 16$ swing in sign and grow. Costs of algorithms rarely do this, so we don't pursue it.

</div>

### The Fibonacci numbers

The characteristic equation of $F_n = F_{n-1} + F_{n-2}$ is $r^2 = r + 1$, with roots

$$
\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618, \qquad \psi = \frac{1 - \sqrt{5}}{2} \approx -0.618.
$$

By part (a), $F_n = A\varphi^n + B\psi^n$. The conditions $F_0 = 0$ and $F_1 = 1$ give $A + B = 0$ and $A\varphi + B\psi = 1$, so $A(\varphi - \psi) = 1$. Since $\varphi - \psi = \sqrt{5}$, we get $A = \frac{1}{\sqrt{5}}$ and $B = -\frac{1}{\sqrt{5}}$:

$$
F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}.
$$

The formula is named after Binet. It is a closed form with irrational numbers whose irrational parts cancel to give whole numbers every time. Because $\lvert\psi\rvert < 1$, the term $\frac{\psi^n}{\sqrt{5}}$ has absolute value below $\frac{1}{\sqrt{5}} < \frac{1}{2}$ for every $n \ge 0$, so $F_n$ is the integer nearest to $\frac{\varphi^n}{\sqrt{5}}$.

| $n$ | $F_n$ | $\varphi^n / \sqrt{5}$ |
|---|---|---|
| 5 | 5 | 4.9597 |
| 10 | 55 | 55.0036 |
| 20 | 6765 | 6765.00003 |
| 30 | 832040 | 832040.0000002 |

This also gives the growth rate: $F_n$ grows like $\varphi^n$, and the ratio $\frac{F_{n+1}}{F_n}$ tends to $\varphi$. Each Fibonacci number is about 1.618 times the one before, so the number of calls made by the plain recursive `fib_rec` in the earlier lesson, which is of the same size, grows exponentially. Example 4 makes that exact.

### Nonhomogeneous recurrences: a particular solution

*Theorem.* Let $(p_n)$ be a particular solution of $a_n = c_1 a_{n-1} + c_2 a_{n-2} + g(n)$. Then every solution of the recurrence has the form $a_n = p_n + h_n$, where $(h_n)$ is a solution of the homogeneous recurrence $h_n = c_1 h_{n-1} + c_2 h_{n-2}$.

We know one solution $p_n$. We want all of them. The plan is to subtract: if two sequences both satisfy the recurrence, their difference satisfies the homogeneous version.

*Proof.* If $a_n$ is any solution, put $h_n = a_n - p_n$. Subtracting the equations for $a_n$ and $p_n$, the terms $g(n)$ cancel and $h_n = c_1 h_{n-1} + c_2 h_{n-2}$. So $a_n = p_n + h_n$. Conversely, $p_n + h_n$ satisfies the recurrence, since the $h$ parts satisfy the homogeneous equation and the $p$ part supplies $g(n)$. $\blacksquare$

The method is to find $h_n$ from the characteristic equation, guess $p_n$ in the same shape as $g(n)$, and fit the constants last.

1. Solve the homogeneous part. Write $h_n$ with unknown constants $A$ and $B$.
2. Guess a particular solution from the table, with undetermined coefficients. Substitute it into the full recurrence and match coefficients to find them.
3. Write $a_n = p_n + h_n$. Now use the initial conditions to find $A$ and $B$, in the full formula.
4. Check the first few terms against the recurrence.

| If $g(n)$ is | Try $p_n =$ | If that fails |
|---|---|---|
| a constant $d$ | $C$ | $Cn$, when 1 is a characteristic root |
| a polynomial of degree $m$ | a polynomial of degree $m$ in $n$ | multiply by $n$ for each time 1 is a root |
| $s^n$ | $C\,s^n$ | $C\,n\,s^n$ when $s$ is a root, $C\,n^2 s^n$ when $s$ is a double root |

The guess fails when it is already a solution of the homogeneous equation: then plugging it in gives $0$ on the left and $g(n)$ on the right, and the equation can't be satisfied. Multiplying by $n$ avoids this.

<div class="warning" markdown>

Watch out at step 3: the initial conditions apply to the whole solution $p_n + h_n$, not to $h_n$ alone. If you fit $A$ and $B$ to $a_0$ and $a_1$ before adding the particular solution, the formula is wrong from $n = 0$.

</div>

## Worked examples

<div class="example" markdown>

### Example 1: distinct roots

Solve $a_n = a_{n-1} + 6a_{n-2}$ with $a_0 = 2$ and $a_1 = 1$.

Following the method for homogeneous recurrences, the first step is the characteristic equation: $r^2 = r + 6$, so $r^2 - r - 6 = (r - 3)(r + 2) = 0$ and the roots are $r_1 = 3$ and $r_2 = -2$. They are distinct, so by part (a)

$$
a_n = A \cdot 3^n + B \cdot (-2)^n.
$$

Next fit the initial values. From $a_0 = 2$ we get $A + B = 2$, and from $a_1 = 1$ we get $3A - 2B = 1$. Multiply the first equation by 2 and add: $5A = 5$, so $A = 1$ and $B = 1$. The solution is

$$
a_n = 3^n + (-2)^n.
$$

Check: the recurrence gives $a_2 = 1 + 6 \cdot 2 = 13$, $a_3 = 13 + 6 = 19$ and $a_4 = 19 + 78 = 97$. The formula gives $3^2 + 4 = 13$, $27 - 8 = 19$ and $81 + 16 = 97$. Note that $a_n$ is a sum of two exponentials, and for large $n$ the $3^n$ term dominates, so $a_n$ grows like $3^n$.

</div>

<div class="example" markdown>

### Example 2: a repeated root

Solve $a_n = 6a_{n-1} - 9a_{n-2}$ with $a_0 = 1$ and $a_1 = 9$.

The characteristic equation is $r^2 - 6r + 9 = (r - 3)^2 = 0$, with the double root $r = 3$. By part (b), $a_n = (A + Bn)3^n$. From $a_0 = 1$ we get $A = 1$. From $a_1 = 9$ we get $(1 + B) \cdot 3 = 9$, so $B = 2$:

$$
a_n = (1 + 2n)\,3^n.
$$

Check: the recurrence gives $a_2 = 6 \cdot 9 - 9 \cdot 1 = 45$ and $a_3 = 6 \cdot 45 - 9 \cdot 9 = 189$. The formula gives $5 \cdot 9 = 45$ and $7 \cdot 27 = 189$.

If you had used only $A\,3^n$, you could match one initial value and not the other. The factor $n$ is what makes the second condition solvable.

</div>

<div class="example" markdown>

### Example 3: a particular solution

Solve $a_n = 2a_{n-1} + 3n$ with $a_0 = 1$.

Step 1: the homogeneous part is $h_n = 2h_{n-1}$, so $h_n = A \cdot 2^n$.

Step 2: $g(n) = 3n$ is a polynomial of degree 1, and 1 is not a root of $r = 2$, so try $p_n = Cn + D$. Substituting into the recurrence:

$$
Cn + D = 2\bigl(C(n-1) + D\bigr) + 3n = (2C + 3)n + (2D - 2C).
$$

Matching the coefficients of $n$ gives $C = 2C + 3$, so $C = -3$. Matching the constant terms gives $D = 2D - 2C$, so $D = 2C = -6$. The particular solution is $p_n = -3n - 6$.

Step 3: $a_n = A \cdot 2^n - 3n - 6$. From $a_0 = 1$ we get $A - 6 = 1$, so $A = 7$:

$$
a_n = 7 \cdot 2^n - 3n - 6.
$$

Step 4, the check: the recurrence gives $a_1 = 2 \cdot 1 + 3 = 5$, $a_2 = 10 + 6 = 16$ and $a_3 = 32 + 9 = 41$. The formula gives $14 - 3 - 6 = 5$, $28 - 6 - 6 = 16$ and $56 - 9 - 6 = 41$.

</div>

<div class="example" markdown>

### Example 4: counting the calls of the recursive Fibonacci

The plain recursive function from the sequences lesson calls itself twice. Let $C(n)$ be the number of calls to `fib_rec(n)`, including the first one. For $n \le 1$ there is one call, so $C(0) = C(1) = 1$. For $n \ge 2$ there is the call itself plus the calls made by `fib_rec(n - 1)` and `fib_rec(n - 2)`:

$$
C(n) = C(n-1) + C(n-2) + 1.
$$

This is nonhomogeneous with $g(n) = 1$. The homogeneous part is the Fibonacci recurrence. Since $g$ is a constant and 1 is not a root of $r^2 = r + 1$, try $p_n = C_0$ (a constant): $C_0 = 2C_0 + 1$ gives $C_0 = -1$. So $C(n) = -1 + A\varphi^n + B\psi^n$.

Rather than solve for $A$ and $B$ again, use the fact that $C(n) + 1$ satisfies the Fibonacci recurrence (the $-1$ and the $+1$ cancel), and its first two values are $C(0) + 1 = 2$ and $C(1) + 1 = 2$. Fibonacci-type sequences are determined by their first two terms, and $2F_1 = 2$, $2F_2 = 2$, so $C(n) + 1 = 2F_{n+1}$:

$$
C(n) = 2F_{n+1} - 1.
$$

Check: for $n = 20$, $F_{21} = 10946$, so $C(20) = 21{,}891$, the number reported in the earlier lesson. For $n = 2$ the function calls itself on 1 and 0, so $C(2) = 3$, and the formula gives $2F_3 - 1 = 3$. The count grows like $\varphi^n$, which is exponential.

</div>

<div class="example" markdown>

### Example 5: when the guess is already a solution (finish it yourself)

Solve $a_n = 3a_{n-1} - 2a_{n-2} + 2^n$ with $a_0 = 0$ and $a_1 = 1$.

The characteristic equation is $r^2 - 3r + 2 = (r - 1)(r - 2) = 0$, so $h_n = A + B \cdot 2^n$. Since $2$ is a root, the guess $C \cdot 2^n$ would be a solution of the homogeneous part and could not produce the $2^n$ on the right. By the table, try $p_n = C\,n\,2^n$. Substituting and dividing by $2^n$:

$$
Cn = \frac{3}{2}C(n-1) - \frac{1}{2}C(n-2) + 1 = Cn - \frac{C}{2} + 1.
$$

So $C = 2$ and $p_n = n\,2^{n+1}$. Now finish: write the general solution, fit $A$ and $B$ to $a_0 = 0$ and $a_1 = 1$, and check $a_2$ and $a_3$.

<details class="solution" markdown>
<summary>Finish</summary>

The general solution is $a_n = A + B \cdot 2^n + n\,2^{n+1}$. From $a_0 = 0$: $A + B = 0$. From $a_1 = 1$: $A + 2B + 4 = 1$, so $A + 2B = -3$. Subtracting, $B = -3$ and $A = 3$:

$$
a_n = 3 - 3 \cdot 2^n + n\,2^{n+1}.
$$

Check: the recurrence gives $a_2 = 3 \cdot 1 - 0 + 4 = 7$ and $a_3 = 21 - 2 + 8 = 27$. The formula gives $3 - 12 + 16 = 7$ and $3 - 24 + 48 = 27$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for the sign in the characteristic equation. The recurrence $a_n = c_1 a_{n-1} + c_2 a_{n-2}$ gives $r^2 - c_1 r - c_2 = 0$. A common slip is to write $r^2 + c_1 r + c_2$, which solves the wrong recurrence. For $a_n = a_{n-1} + 6a_{n-2}$ the equation is $r^2 - r - 6 = 0$, not $r^2 + r + 6 = 0$ (that one has complex roots, and no connection to this sequence).

</div>

<div class="warning" markdown>

Watch out for a repeated root with no extra factor. If the characteristic equation is $(r - 3)^2 = 0$, then $A\,3^n + B\,3^n = (A + B)\,3^n$ is only one free constant, and it can't match two initial values. The solution needs $(A + Bn)\,3^n$.

</div>

<div class="warning" markdown>

Watch out for fitting the initial conditions too early in a nonhomogeneous problem. The constants in $a_n = A\,2^n + p_n$ are found after adding $p_n$, from $a_0$ and not from $h_0$. With Example 3, using $h_0 = a_0 = 1$ would give $A = 1$, and the formula $2^n - 3n - 6$ would give $-5$ at $n = 0$, not 1.

</div>

<div class="warning" markdown>

Watch out when the guess for $p_n$ is already a solution of the homogeneous recurrence. Then the substitution gives a contradiction such as $0 = 2^n$, which is not a sign of an algebra error but of the wrong guess. Multiply by $n$ (Example 5).

</div>

A recurrence like $T(n) = 2T(n/2) + n$ is not of this form, because the index $n/2$ is not $n - 1$ or $n - 2$, and the coefficient pattern doesn't fit. Don't force the characteristic equation on it. Either unroll it, or use the master theorem lesson. A recurrence with a coefficient that depends on $n$, such as $a_n = n\,a_{n-1}$ (which gives $n!$), is not "constant coefficient" either, and unrolling handles it.

If $c_k = 0$ the order is lower than it looks. The recurrence $a_n = 4a_{n-1} + 0 \cdot a_{n-2}$ is of order 1, and its characteristic equation $r^2 = 4r$ has the extra root 0, which contributes nothing. Always check that the formula matches the first four or five terms, because a sign slip in the roots is easy to make and easy to catch.

## Tricks and shortcuts

- For order 2 the sum of the roots is $c_1$ and the product is $-c_2$. Check your roots against both: for $a_n = a_{n-1} + 6a_{n-2}$, the roots $3$ and $-2$ have sum $1 = c_1$ and product $-6 = -c_2$.
- If the coefficients add up to 1, then $r = 1$ is a root, because $r = 1$ turns $r^2 = c_1 r + c_2$ into $1 = c_1 + c_2$. For $a_n = 3a_{n-1} - 2a_{n-2}$ the coefficients add to $3 - 2 = 1$, so 1 is a root, and the other root is 2.
- The largest characteristic root, in absolute value, decides the growth. In Example 1 the roots $3$ and $-2$ give growth like $3^n$. In Fibonacci, $\varphi \approx 1.618$ decides, and $\psi$ fades away.
- A recurrence with $n/2$ becomes a plain recurrence if you set $n = 2^t$ and $S(t) = T(2^t)$. Then $T(n) = 2T(n/2) + n$ turns into $S(t) = 2S(t-1) + 2^t$, which is nonhomogeneous with a resonant right side (the root 2 and $g(t) = 2^t$), so the particular solution is $C\,t\,2^t$, which is $n \lg n$ in the original variable.
- To test a closed form quickly, compute 5 terms from the recurrence and from the formula. If they agree, an error would have to be a coincidence of five numbers.

## In code

The code computes a recurrence term by term and compares it with the closed forms from this lesson, counts the calls of the recursive Fibonacci, and shows where the floating-point version of Binet's formula stops being exact.

<details class="code" markdown>
<summary>In code</summary>

```python
def terms(c, init, count):
    """First `count` terms of a_n = c[0]*a_(n-1) + c[1]*a_(n-2) + ..."""
    a = list(init)
    while len(a) < count:
        a.append(sum(ci * a[-1 - i] for i, ci in enumerate(c)))
    return a

a = terms([1, 6], [2, 1], 10)                 # Example 1
print(a)                                      # [2, 1, 13, 19, 97, 211, 793, 2059, 6817, 19171]
print(all(a[n] == 3**n + (-2)**n for n in range(10)))      # True

b = terms([6, -9], [1, 9], 10)                # Example 2
print(all(b[n] == (1 + 2 * n) * 3**n for n in range(10)))  # True

c = [1]                                       # Example 3: a_n = 2 a_(n-1) + 3n
for n in range(1, 10):
    c.append(2 * c[-1] + 3 * n)
print(all(c[n] == 7 * 2**n - 3 * n - 6 for n in range(10)))  # True

calls = 0
def fib_rec(n):
    global calls
    calls += 1
    return n if n < 2 else fib_rec(n - 1) + fib_rec(n - 2)

fib_rec(20)
fib = terms([1, 1], [0, 1], 100)
print(calls, 2 * fib[21] - 1)                 # 21891 21891

phi = (1 + 5**0.5) / 2                        # Binet's formula in floating point
first_bad = next(n for n in range(100) if round(phi**n / 5**0.5) != fib[n])
print(first_bad)                              # 71
```

The last line is a warning, not a flaw in the formula. A double-precision number keeps about 16 digits, and $F_{71}$ has 15 digits, so by $n = 71$ the rounding in $\varphi^n$ is bigger than the $\frac{1}{2}$ that the rounding step can absorb. With exact integers, or a loop, there is no problem.

</details>

## FAQ

### Why do we try $a_n = r^n$ in the first place?

Because shifting a geometric sequence by one place gives a constant multiple of itself: $r^{n-1} = \frac{1}{r}\,r^n$. So plugging $r^n$ into a recurrence with constant coefficients turns every term into a multiple of $r^n$, and the equation becomes a polynomial equation in $r$. No other simple shape has this property. The rest of the theorem shows that these solutions are enough.

### Why does a repeated root need the extra factor $n$?

A recurrence of order 2 has two free starting values, so its solutions form a two-parameter family. A double root gives only one geometric solution, $r^n$. The sequence $n\,r^n$ is a second solution (the proof in part (b) checks it), and it is not a multiple of the first, so together they fit any two starting values.

### What if the roots are irrational, as in Fibonacci?

Nothing changes. The roots are still numbers, the fitting of $A$ and $B$ still works, and the irrational parts cancel when you add up to get whole numbers. For a check, compute a few terms from the formula with a calculator, or work in exact arithmetic with $\sqrt{5}$.

### Why can't I use the characteristic equation for merge sort's $T(n) = 2T(n/2) + n$?

The method needs each term to depend on the terms one, two, ..., $k$ places back, with $k$ fixed. In $T(n) = 2T(n/2) + n$, the term $T(n)$ depends on $T(n/2)$, which is a different kind of step: the number of places back grows with $n$. You can convert the problem with $n = 2^t$, as in Tricks, or use the master theorem, which solves this whole family at once.

## Practice

### Warm-up

1\. Unroll to find a formula: (a) $T(n) = T(n-1) + 4$ with $T(0) = 7$, and (b) $T(n) = 3T(n-1)$ with $T(0) = 2$. Evaluate each at $n = 10$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $T(n) = T(n-1) + 4 = T(n-2) + 8 = \cdots = T(0) + 4n = 7 + 4n$. So $T(10) = 47$.

(b) $T(n) = 3T(n-1) = 3^2 T(n-2) = \cdots = 3^n T(0) = 2 \cdot 3^n$. So $T(10) = 2 \cdot 59049 = 118{,}098$.

Check: (a) $T(1) = 11$ and $7 + 4 = 11$, and (b) $T(2) = 3 \cdot 6 = 18$ and $2 \cdot 9 = 18$.

</details>

2\. Write the characteristic equation and its roots, and the general solution, for (a) $a_n = a_{n-1} + 2a_{n-2}$, (b) $a_n = 6a_{n-1} - 9a_{n-2}$ and (c) $a_n = 4a_{n-2}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $r^2 - r - 2 = (r - 2)(r + 1) = 0$, with roots $2$ and $-1$. General solution: $a_n = A\,2^n + B(-1)^n$.

(b) $r^2 - 6r + 9 = (r - 3)^2 = 0$, with the double root 3. General solution: $a_n = (A + Bn)\,3^n$.

(c) Here $c_1 = 0$ and $c_2 = 4$, so $r^2 = 4$, with roots $2$ and $-2$. General solution: $a_n = A\,2^n + B(-2)^n$.

Check (a): the roots add to $1 = c_1$ and multiply to $-2 = -c_2$. For (c), $a_n = 2^n$ gives $a_n = 2^n$ and $4a_{n-2} = 4 \cdot 2^{n-2} = 2^n$.

</details>

3\. Write the recurrence for the number of values printed by this function, and solve it.

```python
def g(n):
    if n == 0:
        return
    for i in range(n):
        print(i)
    g(n - 1)
```

<details class="solution" markdown>
<summary>Solution</summary>

The base case prints nothing, so $T(0) = 0$. For $n \ge 1$ the loop prints $n$ values and then the call $g(n-1)$ prints $T(n-1)$ more, so $T(n) = T(n-1) + n$. Unrolling gives $T(n) = n + (n-1) + \cdots + 1 = \frac{n(n+1)}{2}$.

Check: $g(3)$ prints $3 + 2 + 1 = 6$ values, and $\frac{3 \cdot 4}{2} = 6$.

</details>

### Standard

4\. Solve $a_n = 4a_{n-1} - 4a_{n-2}$ with $a_0 = 1$ and $a_1 = 0$.

<details class="solution" markdown>
<summary>Solution</summary>

The characteristic equation $r^2 - 4r + 4 = (r - 2)^2 = 0$ has the double root 2, so $a_n = (A + Bn)2^n$. From $a_0 = 1$: $A = 1$. From $a_1 = 0$: $(1 + B) \cdot 2 = 0$, so $B = -1$. The solution is $a_n = (1 - n)\,2^n$.

Check: the recurrence gives $a_2 = 0 - 4 = -4$ and $a_3 = -16 - 0 = -16$. The formula gives $(-1) \cdot 4 = -4$ and $(-2) \cdot 8 = -16$.

</details>

5\. Solve $a_n = 3a_{n-1} + 2^n$ with $a_0 = 1$.

<details class="solution" markdown>
<summary>Solution</summary>

The homogeneous part is $h_n = A \cdot 3^n$. The root is 3, not 2, so the guess $p_n = C \cdot 2^n$ is allowed. Substituting: $C\,2^n = 3C\,2^{n-1} + 2^n$, and dividing by $2^{n-1}$ gives $2C = 3C + 2$, so $C = -2$. Then $a_n = A \cdot 3^n - 2 \cdot 2^n$. From $a_0 = 1$: $A - 2 = 1$, so $A = 3$:

$$
a_n = 3^{n+1} - 2^{n+1}.
$$

Check: the recurrence gives $a_1 = 3 + 2 = 5$, $a_2 = 15 + 4 = 19$ and $a_3 = 57 + 8 = 65$. The formula gives $9 - 4 = 5$, $27 - 8 = 19$ and $81 - 16 = 65$.

</details>

6\. Let $s_n$ be the number of binary strings of length $n$ with no two 1s next to each other. Find a recurrence for $s_n$, solve it, and give $s_{10}$.

<details class="solution" markdown>
<summary>Solution</summary>

There is one empty string and two strings of length 1, so $s_0 = 1$ and $s_1 = 2$. For $n \ge 2$, a valid string of length $n$ ends in 0 or in 1. If it ends in 0, what comes before is any valid string of length $n - 1$, which gives $s_{n-1}$ strings. If it ends in 1, the bit before must be 0, and what comes before that is any valid string of length $n - 2$, which gives $s_{n-2}$ strings. So $s_n = s_{n-1} + s_{n-2}$.

This is the Fibonacci recurrence with starting values $s_0 = 1 = F_2$ and $s_1 = 2 = F_3$, so $s_n = F_{n+2}$. Using the closed form, $s_n = \frac{\varphi^{n+2} - \psi^{n+2}}{\sqrt{5}}$. Then $s_{10} = F_{12} = 144$.

Check: for $n = 3$ the valid strings are 000, 001, 010, 100, 101, which is $5 = F_5$.

</details>

### Challenge

7\. Use Binet's formula to prove Cassini's identity: $F_{n+1}F_{n-1} - F_n^2 = (-1)^n$ for every $n \ge 1$. (Hint: $\varphi\psi = -1$ and $\varphi - \psi = \sqrt{5}$.)

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}$, $\varphi\psi = -1$ (the product of the roots is $-c_2 = -1$) and $(\varphi - \psi)^2 = 5$. What we want: the identity. The plan: expand $5\bigl(F_{n+1}F_{n-1} - F_n^2\bigr)$ and see what is left.

$$
\begin{aligned}
5F_{n+1}F_{n-1} &= (\varphi^{n+1} - \psi^{n+1})(\varphi^{n-1} - \psi^{n-1}) = \varphi^{2n} - \varphi^{n+1}\psi^{n-1} - \psi^{n+1}\varphi^{n-1} + \psi^{2n}, \\
5F_n^2 &= \varphi^{2n} - 2\varphi^n\psi^n + \psi^{2n}.
\end{aligned}
$$

Subtract. The terms $\varphi^{2n}$ and $\psi^{2n}$ cancel:

$$
5\bigl(F_{n+1}F_{n-1} - F_n^2\bigr) = -\varphi^{n-1}\psi^{n-1}\bigl(\varphi^2 + \psi^2 - 2\varphi\psi\bigr) = -(\varphi\psi)^{n-1}(\varphi - \psi)^2 = -(-1)^{n-1} \cdot 5.
$$

Dividing by 5, $F_{n+1}F_{n-1} - F_n^2 = -(-1)^{n-1} = (-1)^n$. $\blacksquare$

Check: $n = 1$ gives $F_2F_0 - F_1^2 = 0 - 1 = -1$. $n = 5$ gives $F_6F_4 - F_5^2 = 8 \cdot 3 - 25 = -1$. $n = 6$ gives $F_7F_5 - F_6^2 = 13 \cdot 5 - 64 = 1$.

</details>

8\. (Reviews [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md).) A loan balance satisfies $B_{n+1} = (1 + r)B_n - \text{PMT}$ with $B_0$ given and $r \ne 0$. Solve it as a nonhomogeneous recurrence, and compare with the geometric-series formula from that lesson.

<details class="solution" markdown>
<summary>Solution</summary>

The homogeneous part is $h_n = A(1 + r)^n$. Since $g$ is a constant and 1 is not a root unless $r = 0$, try a constant $p_n = C$: $C = (1 + r)C - \text{PMT}$ gives $rC = \text{PMT}$, so $C = \frac{\text{PMT}}{r}$. The general solution is $B_n = A(1 + r)^n + \frac{\text{PMT}}{r}$. From $n = 0$: $A = B_0 - \frac{\text{PMT}}{r}$. So

$$
B_n = (1 + r)^n B_0 - \text{PMT}\cdot\frac{(1 + r)^n - 1}{r}.
$$

This is the formula the geometric series gave in the summation lesson, now found without guessing it first.

Check with the loan of \$1,000 at 1% a month and \$100 payments: $B_4 = 1.01^4 \cdot 1000 - 100 \cdot \frac{1.01^4 - 1}{0.01} = 1040.60 - 406.04 = 634.56$, which matches the table in the sequences lesson.

</details>

## Where this shows up

- The next lessons use recurrences without naming them. [Asymptotic notation](04-asymptotic-notation.md) says how fast a solution grows, and [divide and conquer and the master theorem](05-divide-and-conquer-and-master-theorem.md) solves the whole family $T(n) = aT(n/b) + f(n)$.
- Dynamic programming is recurrences turned into loops: the cost of computing Fibonacci numbers, the longest common subsequence or the number of paths in a grid are all recurrences with memory. The number of calls in Example 4 is the reason for memoization.
- Linear recurrences are everywhere outside algorithms too: the loan balance of this lesson is the finance lesson on [the loan amortization formula](../../08-financial-math/03-time-value-of-money/03-loan-amortization-formula.md), and discrete models of populations and of dynamic economic systems use the same characteristic equation.
