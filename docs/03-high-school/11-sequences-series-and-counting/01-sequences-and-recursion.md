# Sequences and recursion

After this lesson you can describe a sequence by an explicit formula or by a recurrence, write the formula for an arithmetic or a geometric sequence, find a formula for a recurrence by spotting a pattern (and say why the pattern is not yet a proof), turn a recurrence into a recursive function and a loop, and model a loan balance as a recurrence.

Before this: [what is a function](../03-functions/01-what-is-a-function.md) and [exponent rules](../../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A sequence has $a_0 = 5$ and $a_{n+1} = 2a_n - 3$ for every $n \ge 0$. List $a_0$ to $a_4$.
2. An arithmetic sequence has $a_0 = 4$ and $a_5 = 19$. Find the common difference and $a_{20}$.
3. A geometric sequence has $a_0 = 6$ and common ratio $\frac{1}{2}$. Find $a_4$.

<details class="solution" markdown>
<summary>Answers</summary>

1. Apply the rule four times: $a_1 = 2 \cdot 5 - 3 = 7$, $a_2 = 2 \cdot 7 - 3 = 11$, $a_3 = 19$, $a_4 = 35$.
2. Five steps add up to $19 - 4 = 15$, so $d = 3$. Then $a_{20} = 4 + 20 \cdot 3 = 64$.
3. $a_4 = 6 \cdot \left(\frac{1}{2}\right)^4 = \frac{6}{16} = \frac{3}{8}$.

</details>

## The idea

A savings account holds \$100 and pays 2% interest once a year. After one year it holds $100 \times 1.02 = 102$ dollars, after two years $102 \times 1.02 = 104.04$, after three $104.04 \times 1.02 = 106.1208$ (so \$106.12). The list of balances $100, 102, 104.04, 106.1208, \dots$ is a sequence.

There are two natural ways to describe it. The first is a rule for getting from one balance to the next: "start at 100, and each balance is 1.02 times the one before". That is a recursive definition, and it is how a loop in a program works: update the balance, repeat. The second is a rule that goes straight from the year to the balance: "after $n$ years the balance is $100 \times 1.02^n$". That is an explicit formula. To find the balance after 30 years, the first rule needs 30 steps and the second needs one calculation. Both give \$181.14, since they describe the same list.

Most of this lesson is about moving between the two descriptions. Going from an explicit formula to the next term is easy. Going from a recurrence to a formula is harder, and for a few important families (adding the same amount each time, multiplying by the same number each time) there is a formula that is always available. A computer scientist needs both views, because algorithms are described by recurrences, and their cost is understood from formulas.

## Definitions

A **sequence** is a function $a$ whose domain is the set $\mathbb{N} = \{0, 1, 2, \dots\}$ (or the positive integers, or any set of consecutive integers $\{m, m+1, m+2, \dots\}$) and whose outputs are numbers. It is customary to write $a_n$ instead of $a(n)$. The input $n$ is the **index**, and the output $a_n$ is the **term** with index $n$. The whole sequence is written $(a_n)$, or as a list $a_0, a_1, a_2, \dots$.

In plain words, a sequence is a list of numbers that goes on forever, with each place in the list numbered. The number in place $n$ is $a_n$. Unlike a set, a sequence cares about order and repeats: the sequences $1, 2, 3$ and $3, 2, 1$ are different, and $1, 1, 1, \dots$ is a perfectly good sequence. A **finite sequence** has a domain such as $\{0, 1, \dots, N\}$ and stops at $a_N$.

This book starts sequences at index 0 unless a lesson says otherwise, in line with $0 \in \mathbb{N}$ in [symbols and notation](../../reference/symbols-and-notation.md). Then the formulas below have no $n - 1$ in them. Many other books start at index 1, so their formulas read $a_1 + (n-1)d$, and the two conventions describe the same lists. A list that starts at index 0 and has $N$ terms ends at $a_{N-1}$, which is the source of many off-by-one mistakes.

An **explicit formula** (also called a closed form) gives $a_n$ directly in terms of $n$, such as $a_n = 100 \cdot 1.02^n$ or $a_n = n^2 + 1$.

A **recursive definition** (also called a recurrence relation) has two parts: the **initial conditions**, which give the first term or terms, and a **recurrence**, a rule that gives each later term using earlier ones. For example,

$$
a_0 = 100, \qquad a_{n+1} = 1.02\,a_n \quad \text{for every } n \ge 0.
$$

In plain words, the recurrence is the recipe for one step, and the initial conditions say where to start. Both parts are needed. A rule that looks back one term needs one initial condition, and a rule that looks back two terms needs two.

A sequence is **arithmetic** if the difference between consecutive terms is a constant $d$, the **common difference**:

$$
a_{n+1} - a_n = d \quad \text{for every } n \ge 0.
$$

A sequence is **geometric** if each term is a constant $r$ times the one before, where $r$ is the **common ratio**:

$$
a_{n+1} = r\,a_n \quad \text{for every } n \ge 0.
$$

When the terms are not 0, the ratio is $r = \frac{a_{n+1}}{a_n}$. In plain words, an arithmetic sequence adds the same amount at every step, like a savings plan that deposits \$50 a month, and a geometric sequence multiplies by the same number at every step, like the 2% interest above. Every arithmetic sequence is a linear function of $n$ and every geometric sequence is an exponential function of $n$, which the next section shows.

The **Fibonacci sequence** is the standard example of a recurrence that looks back two terms:

$$
F_0 = 0, \quad F_1 = 1, \quad F_{n+2} = F_{n+1} + F_n \quad \text{for every } n \ge 0.
$$

It begins $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, \dots$, and each term after the first two is the sum of the two before it. The rule needs both initial conditions: with only $F_0$ given, nothing says what $F_1$ is.

## How to do it

### The formulas for arithmetic and geometric sequences

*Theorem.* Let $a_0$, $d$ and $r$ be numbers.

- (a) If $a_{n+1} = a_n + d$ for every $n \ge 0$, then $a_n = a_0 + nd$ for every $n \ge 0$.
- (b) If $a_{n+1} = r\,a_n$ for every $n \ge 0$, then $a_n = a_0 r^n$ for every $n \ge 0$.

We know the initial term and the one-step rule. We want a formula for the term with any index $n$. The plan is to prove the formula for $n = 0$, and then show that if the formula holds for one index, it holds for the next. The first fact gets the argument started, and the second one passes it along, like dominoes.

*Proof of (a).* Call the claim "$a_n = a_0 + nd$" the statement for $n$.

For $n = 0$ the claim says $a_0 = a_0 + 0 \cdot d$, which is true.

Now suppose the claim holds for some index $n \ge 0$. Then

$$
a_{n+1} = a_n + d = (a_0 + nd) + d = a_0 + (n+1)d,
$$

which is the claim for $n + 1$. So the claim holds for $n = 0$, and whenever it holds for $n$ it holds for $n + 1$. It therefore holds for $n = 1$, then for $n = 2$, and so on for every $n$.

*Proof of (b).* The base case is $a_0 = a_0 r^0$, which is true because $r^0 = 1$. For the step, suppose $a_n = a_0 r^n$. Then

$$
a_{n+1} = r\,a_n = r \cdot a_0 r^n = a_0 r^{n+1},
$$

where the last step is the exponent rule $r \cdot r^n = r^{n+1}$. So the claim passes from $n$ to $n + 1$, and (b) follows in the same way.

Look back: the "and so on" at the end of each proof is the part a careful reader should question, and the technique that makes it rigorous is called mathematical induction<!-- link: ../../04-proofs-and-logic/05-induction/01-mathematical-induction.md -->. The two checks (the claim holds at the start, and it passes from $n$ to $n + 1$) are exactly what induction asks for, and you will see the same two-part pattern in every proof about recurrences. The theorem also shows that an arithmetic sequence is a linear function of $n$ with slope $d$ and intercept $a_0$, and a geometric sequence is an exponential function with base $r$ and starting value $a_0$ ([exponential functions and growth](../07-exponentials-and-logarithms/01-exponential-functions-and-growth.md)).

### Finding the formula for an arithmetic or geometric sequence

1. Decide the type. Subtract consecutive terms: if the differences are all equal, the sequence is arithmetic. Divide consecutive terms: if the ratios are all equal, it is geometric. Check at least three terms, not two, because any two terms fit both types.
2. Find $a_0$ and $d$ (or $r$). If you are given two terms $a_m$ and $a_n$ with $m < n$ instead, use $d = \frac{a_n - a_m}{n - m}$ for an arithmetic sequence, and $r^{n-m} = \frac{a_n}{a_m}$ for a geometric one. For a geometric sequence, take the $(n-m)$-th root, and watch for two answers when $n - m$ is even.
3. Substitute into $a_n = a_0 + nd$ or $a_n = a_0 r^n$. If you know a term $a_m$ rather than $a_0$, find $a_0$ first from $a_0 = a_m - md$ or $a_0 = a_m / r^m$.
4. Check the formula on a term you were given and did not use to build it.

### Turning a recurrence into a formula by pattern

For recurrences that are neither arithmetic nor geometric, the standard first attempt is to compute terms and look for a pattern.

1. Compute the first six or so terms from the recurrence. Don't simplify too much: $2 \cdot 3 + 1$ shows more structure than 7.
2. Look at how the terms relate to something familiar: powers of 2, squares, a constant plus a power, differences from a fixed number.
3. Guess a formula, and test it on terms you did not use to find it.
4. Prove it. A formula that fits six terms is a conjecture, not a fact (see [Edge cases](#edge-cases-and-common-mistakes)). The proof is the same two-part induction as above: the formula holds for $n = 0$, and if it holds for $n$ then the recurrence makes it hold for $n + 1$.

### Modelling a balance as a recurrence

A balance that changes by a rule each period is a recurrence. Here is the method for a loan, where interest is added and then a payment is made.

1. Choose the period (a month) and the rate per period. A loan at 12% a year with monthly interest charges $\frac{12\%}{12} = 1\%$ per month, so $r = 0.01$.
2. Let $B_n$ be the balance after $n$ payments, so $B_0$ is the amount borrowed.
3. Describe one period. The balance first grows by interest, $B_n + rB_n = (1 + r)B_n$, and then the payment $\text{PMT}$ is subtracted.
4. Write the rule and the initial condition:

$$
B_0 = \text{amount borrowed}, \qquad B_{n+1} = (1 + r)B_n - \text{PMT}.
$$

5. Check the rule against a hand calculation for one period.

The recurrence is "geometric growth with a withdrawal at each step". It is neither arithmetic nor geometric, but the next lesson uses sums of geometric sequences to find a formula for $B_n$, and that formula is the one behind the loan amortization formula<!-- link: ../../08-financial-math/03-time-value-of-money/03-loan-amortization-formula.md -->. Savings plans have the same shape with the sign of the payment flipped.

## Worked examples

<div class="example" markdown>

### Example 1: towers of Hanoi, from a recurrence to a formula

In the Towers of Hanoi puzzle you move $n$ disks from one peg to another, one at a time, never putting a larger disk on a smaller one. Let $h_n$ be the fewest moves needed for $n$ disks. With no disks, no moves are needed, so $h_0 = 0$. To move $n + 1$ disks you must move the top $n$ disks to a spare peg ($h_n$ moves), move the largest disk (1 move), and move the $n$ disks back on top of it ($h_n$ moves). So

$$
h_0 = 0, \qquad h_{n+1} = 2h_n + 1.
$$

Find an explicit formula for $h_n$.

Step 1: compute terms, leaving the structure visible: $h_1 = 2 \cdot 0 + 1 = 1$, $h_2 = 2 \cdot 1 + 1 = 3$, $h_3 = 2 \cdot 3 + 1 = 7$, $h_4 = 15$, $h_5 = 31$, $h_6 = 63$.

Step 2: look for something familiar. The numbers $1, 3, 7, 15, 31, 63$ are each one less than a power of 2: $2, 4, 8, 16, 32, 64$.

Step 3: guess $h_n = 2^n - 1$. It fits $h_0 = 2^0 - 1 = 0$. Test on a term past the ones that suggested it: the recurrence gives $h_7 = 2 \cdot 63 + 1 = 127$, and the formula gives $2^7 - 1 = 127$.

Step 4: prove it. The formula holds for $n = 0$, as just checked. Suppose $h_n = 2^n - 1$ for some $n$. Then

$$
h_{n+1} = 2h_n + 1 = 2(2^n - 1) + 1 = 2^{n+1} - 2 + 1 = 2^{n+1} - 1,
$$

which is the formula for $n + 1$. So the formula holds for every $n$.

Check: the recurrence and the formula agree for $n$ from 0 to 7. For 64 disks the formula gives $2^{64} - 1$ moves, about $1.8 \times 10^{19}$, which is why the recursive solution is easy to write and impossible to finish.

</div>

<div class="example" markdown>

### Example 2: an arithmetic sequence from two terms

An arithmetic sequence has $a_3 = 17$ and $a_8 = 42$. Find a formula for $a_n$, and find the index of the term equal to 302.

Step 1: the type is given. Step 2: five steps lead from index 3 to index 8, and they add up to $42 - 17 = 25$, so $d = \frac{25}{5} = 5$.

Step 3: find $a_0$ by going back three steps from $a_3$: $a_0 = 17 - 3 \cdot 5 = 2$. So $a_n = 2 + 5n$.

Step 4: check against both given terms. $a_3 = 2 + 15 = 17$ and $a_8 = 2 + 40 = 42$.

For the second question, solve $2 + 5n = 302$, which gives $n = 60$. The term with index 60 is 302, and the check is $2 + 5 \cdot 60 = 302$.

</div>

<div class="example" markdown>

### Example 3: a geometric sequence with two answers

A geometric sequence has $a_2 = 12$ and $a_4 = 48$. Find the possible formulas, and decide which one fits if every term is positive.

Two steps lead from index 2 to index 4, so $r^2 = \frac{48}{12} = 4$. Then $r = 2$ or $r = -2$, and both work: a negative ratio is allowed, and the terms alternate in sign.

Find $a_0$ from $a_0 = \frac{a_2}{r^2} = \frac{12}{4} = 3$ in both cases. The two sequences are

$$
a_n = 3 \cdot 2^n: \quad 3, 6, 12, 24, 48, \dots \qquad \text{and} \qquad a_n = 3 \cdot (-2)^n: \quad 3, -6, 12, -24, 48, \dots
$$

Both have $a_2 = 12$ and $a_4 = 48$, so the information given doesn't tell them apart. If every term is positive, the ratio can't be negative, and only $r = 2$ remains.

Check: $3 \cdot 2^2 = 12$, $3 \cdot 2^4 = 48$, $3 \cdot (-2)^2 = 12$ and $3 \cdot (-2)^4 = 48$.

</div>

<div class="example" markdown>

### Example 4: a loan balance (finish it yourself)

You borrow \$1,000 at 12% a year, charged monthly, and pay \$100 at the end of each month. Using the steps for modelling a balance, the rate per month is $r = 0.01$, and

$$
B_0 = 1000, \qquad B_{n+1} = 1.01\,B_n - 100.
$$

The first payment gives $B_1 = 1.01 \cdot 1000 - 100 = 910$. The second gives $B_2 = 1.01 \cdot 910 - 100 = 919.10 - 100 = 819.10$. Find $B_3$ and $B_4$, and check that the payments are doing something sensible.

<details class="solution" markdown>
<summary>Finish</summary>

$B_3 = 1.01 \cdot 819.10 - 100 = 827.291 - 100 = 727.291$, which is \$727.29 to the cent. Then $B_4 = 1.01 \cdot 727.291 - 100 = 734.56391 - 100 = 634.56391$, which is \$634.56. (Keep the unrounded balance between steps and round only what you report.)

Check: the first month's interest is \$10.00 and the payment is \$100, so the balance falls by \$90. In month two the interest is \$9.10 and the balance falls by \$90.90, so the balance falls faster as the interest shrinks. The drops in the sequence $1000, 910, 819.10, 727.29, 634.56$ are $90, 90.90, 91.81, 92.73$, and they do grow.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: a pattern is not a proof. Put $n$ points on a circle, join every pair with a chord, and count the regions inside, assuming no three chords meet at one point. For $n = 1, 2, 3, 4, 5$ the counts are $1, 2, 4, 8, 16$, which looks like $2^{n-1}$ and predicts 32 for six points. The real count for six points is 31. The correct formula, $\binom{n}{4} + \binom{n}{2} + 1$, uses the counting notation of [a later lesson](03-counting-permutations-combinations.md), and its proof is not one you could guess from five values. A guessed formula needs a proof, and the proof is usually induction.

</div>

<div class="warning" markdown>

Watch out for off-by-one errors in indexing. With index 0 as the first term, $a_{10}$ is the eleventh term in the list, and a list of 10 terms ends at $a_9$. A word problem that says "the third term" means the term with index 2 in this book's convention. If you prefer to number from 1, write $b_1, b_2, b_3, \dots$ and use $b_n = b_1 + (n-1)d$. Decide the starting index before you write a formula, and check the formula on the first term.

</div>

<div class="warning" markdown>

Watch out when you mix up the two families. The sequence $2, 4, 8, \dots$ is geometric (ratio 2) and $2, 4, 6, \dots$ is arithmetic (difference 2). The formulas $2n$ and $2^n$ differ at $n = 3$: 6 against 8. Compute both the differences and the ratios of consecutive terms before choosing a formula.

</div>

<div class="warning" markdown>

Watch out: a recurrence without its initial conditions does not define one sequence. The rule $a_{n+1} = 2a_n$ is satisfied by $1, 2, 4, 8, \dots$ and also by $5, 10, 20, 40, \dots$ and by $0, 0, 0, \dots$. Fibonacci's rule looks back two terms, so it needs two starting values, and giving only one leaves the sequence undetermined.

</div>

Some degenerate cases are legal. If $r = 1$ the geometric sequence is constant, and if $d = 0$ so is the arithmetic one. If $r = 0$ then $a_n = a_0 \cdot 0^n$ is $a_0, 0, 0, \dots$, where the convention $0^0 = 1$ (see [exponent rules](../../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md)) makes $a_0 r^0 = a_0$ hold. If $r$ is negative the terms alternate in sign, as in Example 3. If $0 < \lvert r \rvert < 1$ the terms shrink toward 0.

## Tricks and shortcuts

To count the terms from $a_m$ to $a_n$ in a list, use $n - m + 1$, not $n - m$. The terms $a_3, a_4, \dots, a_8$ are 6 terms, but only 5 steps. The same fence-post count matters in the next lesson, where it decides how many terms a sum has.

You can test a guessed explicit formula against a recurrence without computing many terms. Check the initial condition, then substitute the formula into both sides of the recurrence and see that they match. That is the induction step in disguise, and it is quicker than comparing lists.

A rough size check separates the two families. An arithmetic sequence grows by the same amount each step, so its terms stay near a straight line. A geometric sequence with $r > 1$ doubles, triples, and eventually outruns any arithmetic sequence: $2^n$ passes $2n$ for good at $n = 3$, and passes $1000n$ by $n = 14$.

## In code

A recurrence is a recipe for a loop, and it can also be written as a function that calls itself. The two Fibonacci versions below give the same numbers, but the recursive one repeats work: computing $F_{20}$ makes 21,891 calls, because it recomputes the same small values again and again.

<details class="code" markdown>
<summary>In code</summary>

```python
from functools import cache

calls = 0

def fib_rec(n):
    global calls
    calls += 1
    if n < 2:               # the two initial conditions
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)   # the recurrence

def fib_loop(n):
    a, b = 0, 1             # F(0) and F(1)
    for _ in range(n):
        a, b = b, a + b     # slide the pair along one place
    return a

@cache
def fib_memo(n):            # recursion that remembers its answers
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

print(fib_rec(20), calls)           # 6765 21891
print(fib_loop(20), fib_memo(20))   # 6765 6765

def balance(b0, rate, pmt, n):
    b = b0
    for _ in range(n):
        b = (1 + rate) * b - pmt    # B(n+1) = (1 + r) B(n) - PMT
    return b

print([round(balance(1000, 0.01, 100, n), 2) for n in range(11)])
# [1000, 910.0, 819.1, 727.29, 634.56, 540.91, 446.32, 350.78, 254.29, 156.83, 58.4]
print(round(balance(1000, 0.01, 100, 10) * 1.01, 2))   # 58.98, the last payment
```

The loop version does about $n$ additions. The plain recursive version makes a number of calls that grows like the Fibonacci numbers themselves, which is exponential, and the memoized version remembers each answer so every value is computed once. The loan table shows ten full payments of \$100, leaving \$58.40, so an eleventh payment of \$58.98 (the balance plus a month of interest) clears the loan.

</details>

## FAQ

### Why start at index 0 and not 1?

It makes the formulas shorter: $a_0 + nd$ and $a_0 r^n$ instead of $a_1 + (n-1)d$ and $a_1 r^{n-1}$. It also matches how programmers index arrays and loops, where the first item is item 0. Neither choice changes the mathematics. When you read another book, check where its sequences start before you copy a formula.

### Does every recurrence have an explicit formula?

For many it does. The Fibonacci numbers have one, which involves the golden ratio and a square root, and Recurrences<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md --> gives a method for the common kind that adds up earlier terms with constant multipliers. Other recurrences have no formula anyone can write, and the recurrence is the best description available. It is still a complete definition, and a loop computes the terms.

### If the recursive function is so slow, why use recursion at all?

Because it often matches the problem. The recursive solution to the Tower of Hanoi is three lines and mirrors the argument for $h_{n+1}$. The slowness of `fib_rec` comes from repeated work, and storing answers (as `fib_memo` does) or switching to a loop removes it. Writing the recurrence first and then deciding how to compute it is a normal way to design an algorithm.

### How is this different from a function $f(x)$ I graph?

A sequence is a function on the integers, so its graph is a set of separate points and not a curve. A formula such as $a_n = 100 \cdot 1.02^n$ looks like the exponential function $f(x) = 100 \cdot 1.02^x$, and the sequence is that function evaluated only at $x = 0, 1, 2, \dots$. A sequence with a recurrence, like Fibonacci, has no single curve through its points.

## Practice

### Warm-up

1\. Write the first five terms (indices 0 to 4) of each sequence: (a) $a_n = 3n^2 - 2$, (b) $a_0 = 2$ and $a_{n+1} = a_n + 7$, (c) $a_0 = 80$ and $a_{n+1} = \frac{1}{2}a_n$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) Substitute $n = 0, 1, 2, 3, 4$: $-2, 1, 10, 25, 46$.
- (b) Add 7 each time: $2, 9, 16, 23, 30$. The sequence is arithmetic with $d = 7$.
- (c) Halve each time: $80, 40, 20, 10, 5$. The sequence is geometric with $r = \frac{1}{2}$.

Check (a) at $n = 4$: $3 \cdot 16 - 2 = 46$. Check (b) with the formula $2 + 7n$ at $n = 4$: $30$. Check (c) with $80 \cdot \left(\frac{1}{2}\right)^4 = 5$.

</details>

2\. Is each sequence arithmetic, geometric or neither? Give the formula when it is one of the two. (a) $11, 8, 5, 2, \dots$ (b) $3, 6, 12, 24, \dots$ (c) $1, 4, 9, 16, \dots$ (d) $5, 5, 5, 5, \dots$

<details class="solution" markdown>
<summary>Solution</summary>

- (a) The differences are $-3, -3, -3$, so it is arithmetic with $d = -3$ and $a_n = 11 - 3n$.
- (b) The ratios are $2, 2, 2$, so it is geometric with $a_n = 3 \cdot 2^n$.
- (c) The differences $3, 5, 7$ are not equal and the ratios $4, \frac{9}{4}, \frac{16}{9}$ are not equal, so it is neither. (The formula is $(n+1)^2$.)
- (d) The differences are all 0 and the ratios are all 1, so it is both: arithmetic with $d = 0$ and geometric with $r = 1$. The formula is $a_n = 5$.

Check (a) with $a_3 = 11 - 9 = 2$ and (b) with $a_3 = 3 \cdot 8 = 24$.

</details>

3\. Write the Fibonacci numbers $F_0$ to $F_{12}$, and check that $F_{12} = 144$.

<details class="solution" markdown>
<summary>Solution</summary>

Each term is the sum of the two before it:

$$
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
$$

So $F_{10} = 55$, $F_{11} = 89$ and $F_{12} = 55 + 89 = 144$.

Check: there are 13 terms, from index 0 to index 12, and each one after the first two equals the sum of the two before it: $34 + 55 = 89$ and $55 + 89 = 144$.

</details>

### Standard

4\. A streaming service charges \$9.99 for the first month and its price rises by \$0.50 every 6 months. Treat the price paid in each 6-month block as the sequence $p_0, p_1, p_2, \dots$. (a) Write a formula for $p_n$. (b) What is the price in block 7, and in which block does the price first exceed \$15?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The price rises by the same amount each block, so the sequence is arithmetic with $p_0 = 9.99$ and $d = 0.50$: $p_n = 9.99 + 0.50n$.

(b) Block 7 is $p_7 = 9.99 + 3.50 = 13.49$, so \$13.49. For the price to exceed 15 we need $9.99 + 0.50n > 15$, so $0.50n > 5.01$ and $n > 10.02$. The first whole index is $n = 11$, with $p_{11} = 9.99 + 5.50 = 15.49$.

Check: $p_{10} = 9.99 + 5.00 = 14.99$, which is not above 15, and $p_{11} = 15.49$ is. Block 11 is the twelfth block in the list, after eleven increases.

</details>

5\. A bacteria culture has 800 cells at noon and the count multiplies by 1.5 every hour. (a) Write a recurrence and an explicit formula. (b) How many cells are there after 6 hours, rounded to a whole number? (c) A second culture starts with 5,000 cells and loses 10% each hour. After how many hours is it first smaller than the first culture?

<details class="solution" markdown>
<summary>Solution</summary>

(a) The count is geometric: $c_0 = 800$ and $c_{n+1} = 1.5\,c_n$, with explicit formula $c_n = 800 \cdot 1.5^n$.

(b) $c_6 = 800 \cdot 1.5^6 = 800 \cdot 11.390625 = 9112.5$, which is about 9,113 cells.

(c) The second culture has $s_n = 5000 \cdot 0.9^n$. Compare the values hour by hour. At $n = 3$: $c_3 = 2700$ and $s_3 = 3645$. At $n = 4$: $c_4 = 4050$ and $s_4 = 3280.5$. So the second culture is first smaller after 4 hours.

Check: at $n = 3$ the second culture is still bigger ($3645 > 2700$) and at $n = 4$ it is smaller ($3280.5 < 4050$). The sign flips between hours 3 and 4, so hour 4 is the answer.

</details>

6\. The sequence $a_0 = 1$, $a_{n+1} = a_n + 2n + 1$ starts $1, 2, 5, 10, 17, \dots$. (a) Compute $a_5$ and $a_6$. (b) Guess a formula for $a_n$ and test it on $a_6$. (c) Prove the guess by induction.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $a_5 = 17 + 2 \cdot 4 + 1 = 26$ and $a_6 = 26 + 2 \cdot 5 + 1 = 37$.

(b) The terms $1, 2, 5, 10, 17, 26, 37$ are each one more than a square: $0, 1, 4, 9, 16, 25, 36$. Guess $a_n = n^2 + 1$. At $n = 6$ it gives 37, which matches.

(c) For $n = 0$ the formula gives $0^2 + 1 = 1 = a_0$. Suppose $a_n = n^2 + 1$. Then

$$
a_{n+1} = a_n + 2n + 1 = n^2 + 1 + 2n + 1 = (n^2 + 2n + 1) + 1 = (n+1)^2 + 1.
$$

That is the formula for $n + 1$, so it holds for every $n$.

Check: the formula gives $a_0, \dots, a_4 = 1, 2, 5, 10, 17$, as listed.

</details>

### Challenge

7\. (Reviews [exponent rules](../../02-middle-school/04-powers-roots-and-real-numbers/01-exponent-rules.md).) A sequence is defined by $x_0 = 3$ and $x_{n+1} = x_n^2$. (a) List $x_0$ to $x_4$. (b) Find and prove an explicit formula. (c) How many digits does $x_{10}$ have?

<details class="solution" markdown>
<summary>Solution</summary>

(a) $3, 9, 81, 6561, 43046721$. Each term is the square of the one before.

(b) Write the terms as powers of 3: $3^1, 3^2, 3^4, 3^8, 3^{16}$. The exponents double each time, so guess $x_n = 3^{2^n}$. For $n = 0$ this is $3^1 = 3$. If $x_n = 3^{2^n}$, then by the power-of-a-power rule

$$
x_{n+1} = x_n^2 = \left(3^{2^n}\right)^2 = 3^{2^n \cdot 2} = 3^{2^{n+1}},
$$

which is the formula for $n + 1$.

(c) $x_{10} = 3^{1024}$. The number of digits of a positive integer $N$ is $\lfloor \log_{10} N \rfloor + 1$ ([logarithms](../07-exponentials-and-logarithms/02-logarithms.md)). Here $\log_{10} 3^{1024} = 1024 \log_{10} 3 \approx 1024 \times 0.47712 = 488.57$, so $x_{10}$ has 489 digits.

Check: $x_3 = 3^8 = 6561$ and $x_4 = 3^{16} = 43{,}046{,}721$ match the list, and 489 agrees with Python's `len(str(3**1024))`.

</details>

8\. A loan of \$5,000 has a monthly interest rate $r = 0.005$ (6% a year, charged monthly) and monthly payment \$300. Let $B_n$ be the balance after $n$ payments. (a) Write the recurrence. (b) Find $B_1$, $B_2$ and $B_3$. (c) Show that the payment must be bigger than $rB_0$ or the balance never falls, and find the smallest whole-dollar payment that makes $B_1 < B_0$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $B_0 = 5000$ and $B_{n+1} = 1.005\,B_n - 300$.

(b) $B_1 = 1.005 \cdot 5000 - 300 = 5025 - 300 = 4725$. $B_2 = 1.005 \cdot 4725 - 300 = 4748.625 - 300 = 4448.625$, about \$4,448.63. $B_3 = 1.005 \cdot 4448.625 - 300 = 4470.868\ldots - 300 = 4170.868\ldots$, about \$4,170.87.

(c) The balance falls when $B_{n+1} < B_n$, that is, when $(1 + r)B_n - \text{PMT} < B_n$, which simplifies to $\text{PMT} > rB_n$. The right side is the interest for the month. At the start it is $0.005 \cdot 5000 = 25$, so any payment above \$25 makes $B_1 < B_0$, and the smallest whole-dollar payment is \$26. A payment of exactly \$25 leaves the balance at \$5,000 forever, because it pays only the interest.

Check: with PMT $= 26$, $B_1 = 5025 - 26 = 4999 < 5000$. With PMT $= 25$, $B_1 = 5025 - 25 = 5000$.

</details>

## Where this shows up

- The next lesson, [summation notation and series](02-summation-notation-and-series.md), adds up the terms of arithmetic and geometric sequences, which gives the closed form of the loan balance above. The finance folder uses it in compound interest<!-- link: ../../08-financial-math/02-interest-and-growth/02-compound-interest.md --> and annuities and geometric series<!-- link: ../../08-financial-math/03-time-value-of-money/02-annuities-and-geometric-series.md -->.
- Algorithms are described by recurrences: the cost of a recursive function, such as binary search or merge sort, satisfies one. Recurrences<!-- link: ../../06-cs-math/04-sums-recurrences-and-algorithms/02-recurrences.md --> solves them, and recursive definitions and structural induction<!-- link: ../../04-proofs-and-logic/05-induction/03-recursive-definitions-and-structural-induction.md --> proves facts about them.
- In calculus, sequences and their limits<!-- link: ../../05-university-core/05-sequences-and-series/01-sequences-and-their-limits.md --> asks what happens to $a_n$ as $n$ grows, which is how the infinite sums of the next lesson get their meaning.
