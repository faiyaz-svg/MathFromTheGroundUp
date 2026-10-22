# Invariants and algorithm correctness

After this lesson you can write a specification for an algorithm, prove a loop correct with an invariant (initialization, maintenance, termination), prove that a loop ends by finding a decreasing measure, and use an invariant of a state machine to show that a puzzle position can never be reached.

Before this: [mathematical induction](../../04-proofs-and-logic/05-induction/01-mathematical-induction.md) and [strong induction and well-ordering](../../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md). The sums in the examples use [sums and closed forms](01-sums-and-closed-forms.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. In the loop below, what is true of `total` and `i` at the start of every pass, and what does that say about `total` when the loop stops?

    ```python
    i, total = 0, 0
    while i < 5:
        i += 1
        total += i
    ```

2. Find a whole-number quantity that decreases on every pass of `while b != 0: a, b = b, a % b` and never goes below 0.
3. A puzzle starts with a counter at 0, and every allowed move changes the counter by 0 or by 2. Can the counter ever be 7?

<details class="solution" markdown>
<summary>Answers</summary>

1. At the start of every pass, $\text{total} = 0 + 1 + \cdots + i = \frac{i(i+1)}{2}$. It holds at the start ($0 = 0$) and each pass keeps it true, since $\frac{i(i+1)}{2} + (i+1) = \frac{(i+1)(i+2)}{2}$. When the loop stops, $i = 5$, so $\text{total} = 15$.
2. The value of `b`. After a pass the new `b` is $a \bmod b$, which is less than the old `b` and at least 0.
3. No. The counter starts even, and each move keeps it even, so it is even in every reachable position, and 7 is odd.

</details>

## The idea

Testing shows that a program works on the inputs you tried. A proof shows that it works on all inputs the program is meant for. For a loop, the proof has a standard shape: find something that is true each time around the loop, show that one pass can't spoil it, and show that when the loop stops, what is true is exactly what you wanted.

Think of a loop as a machine that repeats one step. Before the first step the machine is in some state, and each step moves it to a new state. A property that holds in the starting state, and that every step preserves, holds forever, however many steps are taken. That is induction on the number of steps, with the starting state as the base case. Such a property is called an invariant, and it is the whole idea of this lesson.

The same idea proves that some things are impossible. A puzzle is a state machine too: the states are positions and the steps are the legal moves. A property of positions that the starting position has, and that no move changes, is true of every position you can reach. If a target position fails the property, it can never be reached, and no amount of searching is needed to know it.

## Definitions

A **specification** of an algorithm has two parts. The **precondition** is what must be true of the inputs before the algorithm runs, and the **postcondition** is what the algorithm promises about its output, whenever the precondition held. In plain words, the precondition is "what the caller must supply" and the postcondition is "what you get back". For binary search the precondition is that the list is sorted, and the postcondition says where the value is.

An algorithm is **partially correct** if, for every input satisfying the precondition, whenever the algorithm stops, the postcondition holds. It is **totally correct** (or just correct) if it is partially correct and also stops on every such input. In plain words, partial correctness says "if it finishes, the answer is right", and termination says "it does finish".

A **loop invariant** for a loop `while G: B` (guard $G$, body $B$) is a statement $I$ about the program variables with two properties:

- (initialization) $I$ is true just before the first test of $G$, and
- (maintenance) if $I$ and $G$ are both true before the body $B$ runs, then $I$ is true after $B$ has run.

In plain words, the invariant is true when you arrive at the loop and each pass that starts with it true ends with it true. A `for` loop is a `while` loop with a counter, so the same definition applies. The invariant is claimed at one place only: at the top of the loop, at the moment the guard is tested. In the middle of the body it may be briefly false.

A **loop variant** (or ranking function) for the loop is an expression $V$ in the program variables whose value is a natural number whenever the guard is true, and that is strictly smaller after each pass than before. In plain words, the variant is a countdown that can't go on forever.

A **state machine** is a set of **states**, a start state, and a set of allowed **transitions** from one state to another. A state is **reachable** if some sequence of transitions leads to it from the start state. An **invariant of a state machine** is a statement $P$ about states such that $P$ is true of the start state, and for every transition from a state $s$ to a state $s'$, if $P$ is true of $s$ then $P$ is true of $s'$. In plain words, it is a property that the start has and every move preserves. A loop is a state machine whose states are the values of its variables and whose transition is one pass of the body, and the loop invariant is the same idea.

## How to do it

### The invariant theorem

*Theorem.* Suppose a loop `while G: B` has an invariant $I$. Then $I$ is true at every test of the guard, including the last one. So if the loop stops, then $I$ and the negation of $G$ are both true when it stops.

We know the two properties in the definition of an invariant. We want $I$ true at every test. The plan is induction on the number of tests: the first test is the base case and each pass is the step.

*Proof.* Let $P(k)$ be the statement "if the guard is tested at least $k$ times, then $I$ is true at the $k$-th test". The first test comes before any pass of the body, so $P(1)$ is the initialization property. Suppose $P(k)$ holds and the guard is tested a $(k+1)$-th time. Then the body ran once after the $k$-th test, so $G$ was true at the $k$-th test. By $P(k)$, $I$ was also true then. By maintenance, $I$ is true after the body, which is the state at the $(k+1)$-th test. So $P(k+1)$ holds, and by induction $P(k)$ holds for every $k \ge 1$. If the loop stops, it stops at a test where $G$ is false, and $I$ is true at that test. $\blacksquare$

Look back: the proof is the two-part induction from [mathematical induction](../../04-proofs-and-logic/05-induction/01-mathematical-induction.md), with "number of passes" playing the role of $n$. The result "$I$ and not $G$" is the only thing the loop gives you, so the invariant has to be chosen so that it implies the postcondition when combined with "not $G$".

### Proving a loop correct

1. Write the precondition and the postcondition.
2. Choose an invariant. A good first try is the postcondition with the final value replaced by the loop's progress: if the loop is meant to compute a result over the whole list, say what the variable holds over the part of the list processed so far.
3. Initialization: show the invariant is true before the first test of the guard.
4. Maintenance: assume the invariant and the guard, run the body, and show the invariant is true again.
5. Termination: find a variant, a natural number that strictly decreases on each pass, so the loop stops.
6. Conclusion: when the loop stops, the invariant and the negation of the guard give the postcondition. Show that.

Steps 3 to 5 are the three standard checks, often called initialization, maintenance and termination. Step 6 is where you find out whether the invariant was strong enough.

<div class="warning" markdown>

Watch out at step 2: an invariant can be true and useless. For `total += i`, "$\text{total} \ge 0$" is preserved by every pass, but when the loop stops it says nothing about the sum. Test an invariant by doing step 6 first: does the invariant together with "not $G$" give the postcondition? If not, strengthen it.

</div>

### Termination: the variant

*Theorem.* Let $V$ be an expression in the variables of the loop `while G: B`. Suppose that whenever $G$ is true $V$ is a whole number, and that each pass of the body makes $V$ smaller by at least 1. Then the loop stops after at most $V_0$ passes, where $V_0$ is the value of $V$ at the first test.

*Proof.* After $k$ passes the value of $V$ is at most $V_0 - k$. While the loop is running, $V$ is at least 0, so $V_0 - k \ge 0$ and $k \le V_0$. So the loop can't make more than $V_0$ passes. $\blacksquare$

In plain words: a countdown from a whole number that goes down by at least 1 each time must reach the end. This is the well-ordering principle from [strong induction and well-ordering](../../04-proofs-and-logic/05-induction/02-strong-induction-and-well-ordering.md), put to work.

The variant is often the distance to the end of the loop: $n - i$ for a counter, or $\text{hi} - \text{lo}$ for a shrinking range. If you can't find one, be suspicious. The loop `while n != 1: n = n // 2 if n % 2 == 0 else 3 * n + 1` has no known variant. Whether it stops for every positive $n$ is the Collatz conjecture, which no one has proved. A guard being false at the end is easy to wish for and hard to prove.

### State machines and the invariant principle

*Theorem (the invariant principle).* If $P$ is an invariant of a state machine, then $P$ is true of every reachable state.

*Proof.* Take a reachable state $s$, reached by $k$ transitions from the start state. We prove by induction on $k$ that $P$ holds. If $k = 0$, $s$ is the start state, and $P$ holds there by the definition of an invariant. If $s$ is reached in $k + 1$ transitions, the last one comes from a state $s'$ reached in $k$ transitions, where $P$ holds by the inductive hypothesis, and the definition of an invariant says that $P$ holds after the transition. $\blacksquare$

The principle proves that a state can't be reached: if $P$ is an invariant and the target state fails $P$, the target is unreachable. It does not prove the opposite. A state that satisfies the invariant might still be unreachable, because some other obstacle exists. To show a state is reachable, exhibit the moves.

### The 15-puzzle

The 15-puzzle has 15 numbered tiles in a $4 \times 4$ frame with one blank square. A move slides a tile next to the blank into the blank. Read the tiles in order, left to right along each row and top to bottom, skipping the blank. An **inversion** is a pair of tiles in which the larger number comes first. Let $I$ be the number of inversions in a position, and let $R$ be the row of the blank, counted from the top as $1, 2, 3, 4$.

*Theorem.* In every position reachable from the solved position (tiles $1, \dots, 15$ in order with the blank at the bottom right), the number $I + R$ is even.

We know the solved position has $I = 0$ and $R = 4$, so $I + R = 4$ is even. We want $I + R$ to stay even after a move. The plan is to show that each kind of move leaves the parity of $I + R$ alone, so that "$I + R$ is even" is an invariant.

*Proof.* The start state is the solved position, where $I + R = 4$. For a move, there are two cases.

A sideways move slides a tile along its row. The blank stays in the same row, so $R$ doesn't change, and the reading order of the tiles doesn't change either, since the blank is skipped. So $I$ is unchanged.

An up or down move slides a tile from the row above (or below) into the blank's position. In the reading order, the tile jumps over the three squares between its old and new positions, and none of them is the blank, so it passes exactly three tiles. For each of those three tiles the pair (the moving tile, the tile it passes) flips between inversion and not an inversion, so each pair changes $I$ by $+1$ or $-1$. Three changes of $\pm 1$ add up to an odd number, so $I$ changes parity. The blank moves to the next row, so $R$ changes by exactly 1, which changes the parity of $R$ too. The two changes cancel: $I + R$ keeps its parity.

So "$I + R$ is even" is true at the start and preserved by every move. By the invariant principle it holds in every reachable position. $\blacksquare$

Look back: the position with the tiles 14 and 15 swapped and everything else in place, the blank at the bottom right, has $I = 1$ and $R = 4$, so $I + R = 5$ is odd. It can never be reached from the solved position, and no one needs to try. The converse is also true (every position with $I + R$ even can be reached), but that needs a longer argument and is not proved here (Johnson and Story, 1879). It means exactly half of the $16!$ arrangements are reachable, which is $10{,}461{,}394{,}944{,}000$ positions.

For the $3 \times 3$ version, the 8-puzzle, an up or down move jumps over two tiles, which changes $I$ by an even number, so the parity of $I$ alone is the invariant. Practice problem 7 is about it.

## Worked examples

<div class="example" markdown>

### Example 1: the largest item of a list

```python
def list_max(a):
    m = a[0]
    i = 1
    while i < len(a):
        if a[i] > m:
            m = a[i]
        i += 1
    return m
```

Step 1: the precondition is that `a` is a list with at least one item (otherwise `a[0]` fails). The postcondition is that the result is an item of `a` and is at least as large as every item of `a`.

Step 2: the postcondition talks about the whole list. Replace "the whole list" by "the part seen so far", which is `a[0:i]`. The invariant $I$ is: $1 \le i \le \text{len}(a)$, and `m` is an item of `a[0:i]` that is at least as large as every item of `a[0:i]`.

Step 3, initialization: before the first test, $i = 1$ and `m` is `a[0]`. The list `a[0:1]` has the one item `a[0]`, and `m` is that item, so $I$ holds. (The condition $1 \le \text{len}(a)$ is the precondition.)

Step 4, maintenance: assume $I$ and $i < \text{len}(a)$. If `a[i] > m`, the body sets `m` to `a[i]`, which is larger than every item of `a[0:i]` (since it is larger than `m`, which was at least as large as all of them), and is an item of `a[0:i+1]`. Otherwise `a[i] <= m` and `m` stays as it was, still at least as large as every item of `a[0:i+1]`. In both cases, after `i += 1`, `m` is the largest item of `a[0:i]` with the new `i`, and $i \le \text{len}(a)$ since $i < \text{len}(a)$ held before the increase.

Step 5, termination: the variant is $\text{len}(a) - i$. It is a natural number while $i < \text{len}(a)$ and it decreases by 1 on each pass.

Step 6, conclusion: the loop stops when $i < \text{len}(a)$ is false, and with $i \le \text{len}(a)$ that means $i = \text{len}(a)$. Then $I$ says `m` is the largest item of `a[0:len(a)]`, the whole list, which is the postcondition.

Check: for `a = [3, 9, 2]`, the values of `m` at the tests are 3, 9, 9, with $i = 1, 2, 3$, and the answer is 9. For `a = [5]` the loop doesn't run, $i = 1 = \text{len}(a)$, and the answer is 5.

</div>

<div class="example" markdown>

### Example 2: insertion sort

```python
def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
```

The precondition is that `a` is a list of items that can be compared. The postcondition is that `a` holds the same items as before (the same multiset), in nondecreasing order.

The outer invariant, for the test with the counter value $i$: `a[0:i]` holds the items that were originally in `a[0:i]`, in nondecreasing order, and `a[i:]` has not been touched. Initially $i = 1$, and a list with one item is sorted, so the invariant holds.

For maintenance, take a pass with a given $i$, and call the original sorted items $s_0 \le s_1 \le \dots \le s_{i-1}$. The pass is itself a loop, so it has its own invariant, for the test of the inner guard with the value $j$: the items `a[0:j+1]` are $s_0, \dots, s_j$ (untouched), the items `a[j+2:i+1]` are $s_{j+1}, \dots, s_{i-1}$ and each of them is greater than `key`, and `a[j+1]` is a spare square whose contents are a stale copy. At the first test, $j = i - 1$: `a[0:i]` is $s_0, \dots, s_{i-1}$, there are no items in `a[i+1:i+1]`, and `a[i]` is the spare (its old content is saved in `key`). One pass of the inner body, when $j \ge 0$ and `a[j] > key`, copies $s_j$ into the spare square `a[j+1]` and lowers $j$, so the old square $j$ is now the spare and $s_j > \text{key}$ joins the shifted block. The invariant holds again, and $j$ is the variant (together with $j \ge -1$), so the inner loop stops.

When the inner loop stops, either $j = -1$ or `a[j] <= key`. The items $s_0, \dots, s_j$ are all at most `key` (they are sorted and the last of them is at most `key`, or there are none). Putting `key` into `a[j+1]` therefore gives, in order: $s_0, \dots, s_j$, then `key`, then $s_{j+1}, \dots, s_{i-1}$, which are all greater than `key`. That is `a[0:i+1]` in nondecreasing order, holding the original items of `a[0:i+1]`, and `a[i+1:]` is untouched. This is the outer invariant for $i + 1$.

The `for` loop runs $\text{len}(a) - 1$ times, so it stops. At the end, $i$ has reached $\text{len}(a)$ and the invariant says all of `a` is sorted and holds the original items. This is the postcondition.

Check: sorting `[3, 1, 2]`. At $i = 1$ the key is 1, the 3 shifts right, and `a` is `[1, 3, 2]`. At $i = 2$ the key is 2, the 3 shifts, the 1 stays, and `a` is `[1, 2, 3]`. Using `>` and not `>=` in the guard means equal items are never moved past each other, so the sort is stable.

</div>

<div class="example" markdown>

### Example 3: binary search, and a bug the invariant catches

This version finds the first position where `x` could be inserted, searching the half-open range `a[lo:hi]`.

```python
def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

The precondition is that `a` is sorted in nondecreasing order. The postcondition is that the result $p$ is the smallest index in $0, \dots, \text{len}(a)$ such that every item before position $p$ is less than `x` and every item from position $p$ on is at least `x`. In particular, `x` is in `a` exactly when $p < \text{len}(a)$ and `a[p] == x`.

Invariant: $0 \le \text{lo} \le \text{hi} \le \text{len}(a)$, every item of `a[0:lo]` is less than `x`, and every item of `a[hi:]` is at least `x`.

Initialization: $\text{lo} = 0$ and $\text{hi} = \text{len}(a)$, and both parts `a[0:0]` and `a[len(a):]` are empty, so the statements about them hold with nothing to check.

Maintenance: suppose the invariant holds and $\text{lo} < \text{hi}$. Then $\text{lo} \le \text{mid} < \text{hi}$, since the midpoint of two different whole numbers rounds down to something that is at least `lo` and below `hi`. If `a[mid] < x`, sortedness gives that every item of `a[0:mid+1]` is less than `x`, so `lo = mid + 1` keeps the left statement true, and $\text{lo} \le \text{hi}$ still holds. Otherwise `a[mid] >= x`, sortedness gives that every item from position `mid` on is at least `x`, so `hi = mid` keeps the right statement true.

Termination: the variant is $\text{hi} - \text{lo}$. In the first case it becomes $\text{hi} - \text{mid} - 1$, and since $\text{mid} \ge \text{lo}$ this is smaller than $\text{hi} - \text{lo}$. In the second case it becomes $\text{mid} - \text{lo}$, smaller because $\text{mid} < \text{hi}$. It is at least 1 when the guard is true, and it shrinks by at least 1 each pass.

Conclusion: at the end $\text{lo} = \text{hi}$, so every item before position `lo` is less than `x` and every item from position `lo` on is at least `x`, which is the postcondition.

The off-by-one traps are the places where one of these checks fails. Here is a common variant that searches the closed range `a[lo..hi]`.

```python
def buggy(a, x):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1
```

Its natural invariant is "if `x` is in `a`, then it is in `a[lo..hi]`". Initialization and maintenance both work. The conclusion fails: when the loop stops, $\text{lo} \ge \text{hi}$, which includes $\text{lo} = \text{hi}$, and that is a range with one candidate left that has never been looked at. The loop exits before it checks it. For `buggy([5], 5)` the range is `a[0..0]`, the loop doesn't run, and the function returns $-1$ though 5 is in the list. For `buggy([1, 3], 3)`, `mid` is 0, `lo` becomes 1, and the loop stops with the 3 never examined. The cure is to test the last candidate with `while lo <= hi`, and then the invariant, when the loop stops with $\text{lo} > \text{hi}$, says the range is empty. But then `hi = mid - 1` and `lo = mid + 1` are needed so the variant shrinks. With `lo = mid` the loop can repeat forever on a range of two items.

Check: for `a = [2, 3, 5, 7, 11, 13]` and `x = 7`, the tuples (lo, hi, mid) are $(0, 6, 3)$, $(0, 3, 1)$ and $(2, 3, 2)$, and the function returns 3, where `a[3] == 7`. A brute-force test on every sorted list of up to 6 items from $\{0, 1, 2, 3\}$ agrees with Python's `bisect_left`.

<div class="warning" markdown>

Watch out for a second, different trap: `mid = (lo + hi) // 2`. In Python the sum is exact, but in a language with fixed-width integers, `lo + hi` can exceed the largest value and wrap around to a negative number when the list has more than about a billion items (for 32-bit integers). The safe form is `lo + (hi - lo) // 2`. Joshua Bloch reported this in the standard Java library's binary search in "Extra, Extra - Read All About It: Nearly All Binary Searches and Mergesorts are Broken", Google Research Blog, 2 June 2006. The invariant proof above assumes `lo + hi` doesn't overflow, which is a precondition that the proof makes visible.

</div>

</div>

<div class="example" markdown>

### Example 4: Euclid's algorithm

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

The precondition is that $a$ and $b$ are whole numbers at least 0, not both 0. The postcondition is that the result is the greatest common divisor of the two original values, $\gcd(a_0, b_0)$.

Invariant: $a$ and $b$ are whole numbers at least 0, not both 0, and $\gcd(a, b) = \gcd(a_0, b_0)$.

Initialization: this is the precondition, with $a = a_0$ and $b = b_0$.

Maintenance: the body replaces $(a, b)$ by $(b, a \bmod b)$ when $b \ne 0$. The key fact is that the two pairs have the same common divisors. Write $a = qb + r$ with $r = a \bmod b$. If $d$ divides both $a$ and $b$, it divides $a - qb = r$, so $d$ divides $b$ and $r$. If $d$ divides both $b$ and $r$, it divides $qb + r = a$, so it divides $a$ and $b$. The two pairs share all their common divisors, so they share the greatest one. The new pair is not both 0 since $b \ne 0$.

Termination: the variant is $b$. The new $b$ is $a \bmod b$, which is a whole number less than the old $b$, so $b$ strictly decreases and stays at least 0. The loop stops.

Conclusion: at the end $b = 0$, and the invariant says $\gcd(a, 0) = \gcd(a_0, b_0)$. Every number divides 0, so the common divisors of $a$ and 0 are the divisors of $a$, and the greatest is $a$ (this uses $a \ne 0$, from "not both 0"). So the function returns $\gcd(a_0, b_0)$.

Check: for $(252, 105)$ the pairs are $(252, 105) \to (105, 42) \to (42, 21) \to (21, 0)$, and the answer is 21. The gcd is 21 at every stage: $\gcd(105, 42) = 21$ and $\gcd(42, 21) = 21$.

How many passes? If $a \ge b > 0$, then $a \bmod b < \frac{a}{2}$: either $b \le \frac{a}{2}$, and then the remainder is below $b$, or $b > \frac{a}{2}$, and then the remainder is $a - b < \frac{a}{2}$. After two passes the larger number has fallen below half of what it was, so the loop runs at most about $2\lg a$ times. The worst case is consecutive Fibonacci numbers: $\gcd(F_{20}, F_{19})$ takes 18 passes. The lesson on [GCD and Euclid's algorithm](../02-number-theory/02-gcd-and-euclids-algorithm.md) goes further.

</div>

<div class="example" markdown>

### Example 5: a jug puzzle, by an invariant

You have a 6-litre jug and a 9-litre jug, both empty, and a tap. A move fills a jug from the tap, empties a jug onto the ground, or pours one jug into the other until the first is empty or the second is full. Can you ever have exactly 4 litres in one jug?

A state is the pair $(x, y)$ of amounts in the 6-litre and the 9-litre jug. The start state is $(0, 0)$. Claim: in every reachable state, both $x$ and $y$ are multiples of 3.

The start $(0, 0)$ satisfies the claim. Check each kind of move from a state where $x$ and $y$ are multiples of 3. Filling gives 6 or 9 in one jug, a multiple of 3, and the other jug is unchanged. Emptying gives 0 and the other jug is unchanged. A pour moves $p = \min(x, 9 - y)$ litres from the first jug to the second (or $\min(y, 6 - x)$ the other way), and each of $x$, $y$, $9$ and $6$ is a multiple of 3, so $p$ is a multiple of 3, and so are the two new amounts.

By the invariant principle, every reachable state has both amounts multiples of 3. The number 4 is not one, so 4 litres can never be in either jug.

Check: a computer search of all reachable states finds exactly ten of them, $(0,0)$, $(0,3)$, $(0,6)$, $(0,9)$, $(3,0)$, $(3,9)$, $(6,0)$, $(6,3)$, $(6,6)$ and $(6,9)$, and all have both coordinates divisible by 3. The number 3 is $\gcd(6, 9)$, which is the general rule for two jugs.

</div>

<div class="example" markdown>

### Example 6: fast exponentiation (finish it yourself)

```python
def power(x, n):
    result, base, e = 1, x, n
    while e > 0:
        if e % 2 == 1:
            result *= base
        base *= base
        e //= 2
    return result
```

The precondition is that $n$ is a whole number at least 0, and the postcondition is that the result equals $x^n$. The invariant is $\text{result} \cdot \text{base}^{e} = x^n$ with $e \ge 0$.

Initialization: $1 \cdot x^n = x^n$. Maintenance, the odd case: $e$ is odd, so the body multiplies `result` by `base`, squares `base` and replaces $e$ by $\lfloor e/2 \rfloor = \frac{e-1}{2}$. Check that the product is unchanged: new result times new base to the new $e$ is $(\text{result} \cdot \text{base}) \cdot (\text{base}^2)^{(e-1)/2} = \text{result} \cdot \text{base}^{1 + (e - 1)} = \text{result} \cdot \text{base}^{e}$.

Now do the even case, find a variant, and conclude what the function returns when the loop stops. Then trace $x = 3$, $n = 13$.

<details class="solution" markdown>
<summary>Finish</summary>

Maintenance, the even case: `result` is unchanged, `base` is squared and $e$ becomes $\frac{e}{2}$. The product is $\text{result} \cdot (\text{base}^2)^{e/2} = \text{result} \cdot \text{base}^{e}$, unchanged.

Termination: the variant is $e$. It is a natural number, and $\lfloor e/2 \rfloor < e$ when $e > 0$, so it strictly decreases.

Conclusion: the loop stops with $e = 0$ (the guard is false and $e \ge 0$). The invariant gives $\text{result} \cdot \text{base}^0 = \text{result} = x^n$.

Trace for $x = 3$, $n = 13$ (binary $1101$), listing (result, base, e) at each test: $(1, 3, 13)$, $(3, 9, 6)$, $(3, 81, 3)$, $(243, 6561, 1)$, and after the last pass `result` is $243 \cdot 6561 = 1{,}594{,}323$ with $e = 0$.

Check: each triple satisfies the invariant, for example $243 \cdot 6561^1 = 1{,}594{,}323 = 3^{13}$ and $3 \cdot 81^3 = 3 \cdot 531441 = 1{,}594{,}323$. The loop ran 4 times, once for each bit of 13, which is why this method takes about $\lg n$ multiplications. It is the first step of Fermat, Euler and [Fermat, Euler and fast exponentiation](../02-number-theory/05-fermat-euler-and-fast-exponentiation.md).

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for claiming the invariant in the middle of the body. In the insertion sort, between `a[j + 1] = a[j]` and `j -= 1`, the stated invariant is false for a moment: one item is stored twice. The invariant is a claim about the state at the guard test, not at every line.

</div>

<div class="warning" markdown>

Watch out for an invariant that is too specific. "The list `a[0:i]` is unchanged" is not preserved by insertion sort, because each pass moves items. What stays true is that `a[0:i]` holds the same items as the original `a[0:i]`, in sorted order. If maintenance fails because the body changes something, the invariant is probably too specific about what the body is allowed to change.

</div>

<div class="warning" markdown>

Watch out for forgetting termination. A proof of initialization, maintenance and conclusion shows only partial correctness: if the loop stops, the answer is right. The loop `while True: pass` is partially correct for every specification, since it never stops. Always find a variant, or say that the loop might not stop, as for the Collatz loop.

</div>

<div class="warning" markdown>

Watch out for off-by-one errors in ranges. `range(1, n)` stops at $n - 1$, `a[0:i]` has $i$ items and stops at index $i - 1$, and a half-open range like `a[lo:hi]` has $\text{hi} - \text{lo}$ items. In a proof, write the range in the same convention as the code, and test the first and the last pass by hand. The binary search bugs in Example 3 are exactly these.

</div>

Smaller cases to test every time. The empty input: `insertion_sort([])` does nothing, correctly, because `range(1, 0)` is empty, while `list_max([])` fails at `a[0]`, which is why its precondition says at least one item. A single item: `buggy([5], 5)` fails, and `lower_bound([5], 5)` returns 0. Repeated values: the sort and the search should still be right. Negative inputs: Euclid's algorithm needs $a, b \ge 0$, because in some languages `%` of a negative number is negative, and the variant argument breaks.

## Tricks and shortcuts

- Choose the invariant by generalising the postcondition. If the postcondition is "total is the sum of the whole list", the invariant is "total is the sum of the part of the list seen so far".
- Draw the array as zones: a bar split into "done", "being worked on" and "untouched". Each zone gets a sentence, and the sentences are the invariant. For binary search the zones are "less than `x`", "unknown" and "at least `x`".
- Put `assert` statements for the invariant at the top of the loop while testing. They check the invariant on every run, and a failing assert tells you which line broke it. Remove them or keep them in debug builds.
- The first and last pass catch most bugs. Hand-trace the loop for a list of 0, 1 and 2 items.
- For a variant, take the gap between the counter and its limit, or the size of the range still to search.

## In code

The code tests the invariants with `assert` while the algorithms run, which is evidence for small cases and not a proof, and then compares the correct and the buggy binary search on every sorted list of up to 5 items. The last part checks the 15-puzzle invariant along a long random walk and counts the reachable positions of the 8-puzzle.

<details class="code" markdown>
<summary>In code</summary>

```python
import itertools
import math
import random
from bisect import bisect_left
from collections import deque

def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        assert 0 <= lo <= hi <= len(a)                     # the invariant, at each test
        assert all(a[k] < x for k in range(lo))
        assert all(a[k] >= x for k in range(hi, len(a)))
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def buggy(a, x):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1

lists = [list(c) for n in range(6) for c in itertools.combinations_with_replacement(range(4), n)]
print(all(lower_bound(a, x) == bisect_left(a, x) for a in lists for x in range(-1, 5)))   # True
misses = [(a, x) for a in lists if len(set(a)) == len(a) for x in a if buggy(a, x) == -1]
print(len(misses), misses[0])                    # 20 ([0], 0)

def gcd(a, b):
    g = math.gcd(a, b)
    while b != 0:
        assert math.gcd(a, b) == g               # gcd(a, b) never changes
        a, b = b, a % b
    return a

print(gcd(252, 105))                             # 21

def inversions(state):
    tiles = [v for v in state if v != 0]
    return sum(tiles[i] > tiles[j] for i in range(len(tiles)) for j in range(i + 1, len(tiles)))

def parity15(state):                             # I + R mod 2, rows counted from 1
    return (inversions(state) + state.index(0) // 4 + 1) % 2

def moves(state, width):
    z = state.index(0)
    r, c = divmod(z, width)
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= r + dr < width and 0 <= c + dc < width:
            s = list(state)
            y = (r + dr) * width + c + dc
            s[z], s[y] = s[y], s[z]
            yield tuple(s)

random.seed(1)
state = tuple(list(range(1, 16)) + [0])
start = parity15(state)
for _ in range(100_000):
    state = random.choice(list(moves(state, 4)))
    assert parity15(state) == start              # the invariant survives 100,000 moves
print(start, parity15(tuple(list(range(1, 14)) + [15, 14, 0])))   # 0 1

start8 = tuple(list(range(1, 9)) + [0])
seen, queue = {start8}, deque([start8])
while queue:
    for t in moves(queue.popleft(), 3):
        if t not in seen:
            seen.add(t)
            queue.append(t)
print(len(seen), math.factorial(9) // 2)         # 181440 181440
```

The checked search agrees with `bisect_left` on every small sorted list, and the asserts never fire. The buggy search misses an item that is in the list: `misses` holds 20 such (list, item) pairs among the short lists with no repeated items, and the first is the one-item list `[0]`. The reachable 8-puzzle positions are exactly half of the $9!$ arrangements, as the invariant and its converse predict, and the Loyd position has the other parity.

</details>

## FAQ

### If I test a function on a hundred inputs, why do I need a proof?

Because tests show that a bug is there, not that no bug is. The buggy binary search above finds an item that happens to sit at a midpoint, and fails on every one-item list and on the last item of a two-item list. A proof covers every input at once, including the ones you didn't think of. In practice you do both: tests find mistakes quickly, and the invariant is what tells you why the code is right and what to fix when it isn't.

### How do I find the invariant?

Start from the postcondition and from the shape of the loop. Ask what the variables hold after $k$ passes, in terms of the first $k$ items (or the first $k$ steps of the process). Write that as a sentence, test it against the first two passes by hand, and then check that "invariant and not guard" gives the postcondition. If the check at the end fails, the invariant is too weak and needs another clause. If maintenance fails, it may be too strong or the body may have a bug.

### Do I have to write all this for every loop?

No. For a simple loop a line of comment is enough. The habit that matters is asking "what is true each time round?" for every loop that is not obvious, and writing out the checks for the ones that matter: loops that search, sort, or maintain a data structure, and anything with an off-by-one risk.

### What about recursive functions?

The same idea, with induction on the size of the input. The precondition and the postcondition are the claim $P(n)$, the base case is the case where the function returns without calling itself, and the step uses the claim for the smaller inputs of the recursive calls, which is strong induction when the sizes are not $n - 1$. The termination argument is again a measure that decreases, the input size.

## Practice

### Warm-up

1\. Prove that this loop computes $n!$ for each whole number $n \ge 0$.

```python
result, i = 1, 1
while i <= n:
    result *= i
    i += 1
```

<details class="solution" markdown>
<summary>Solution</summary>

Invariant: $1 \le i \le n + 1$ and $\text{result} = (i-1)!$.

Initialization: $i = 1$ and $\text{result} = 1 = 0!$. Also $1 \le n + 1$ since $n \ge 0$.

Maintenance: if $i \le n$, the body sets $\text{result}$ to $(i-1)! \cdot i = i!$ and $i$ to $i + 1$, so $\text{result} = (i_{\text{new}} - 1)!$, and $i_{\text{new}} \le n + 1$.

Termination: the variant is $n + 1 - i$, which decreases by 1 each pass and is at least 1 while the guard is true.

Conclusion: the guard $i \le n$ is false and $i \le n + 1$, so $i = n + 1$ and $\text{result} = n!$. For $n = 0$ the loop doesn't run and the result is $1 = 0!$.

Check: for $n = 4$ the values of (i, result) at the tests are $(1, 1)$, $(2, 1)$, $(3, 2)$, $(4, 6)$, $(5, 24)$, and $4! = 24$.

</details>

2\. Find a variant for each loop, or explain why none exists. Say how many passes each makes for $n = 10$. (a) `i = 0` and `while i < n: i += 3`. (b) `while n > 0: n //= 2`. (c) `x = 4` and `while x != 1: x -= 2`.

<details class="solution" markdown>
<summary>Solution</summary>

(a) The variant is $n - i$, which is positive while the guard is true and drops by 3 each pass. For $n = 10$ the values of $i$ at the passes are $0, 3, 6, 9$, so 4 passes ($\lceil 10/3 \rceil$).

(b) The variant is $n$ itself. It is a whole number and $\lfloor n/2 \rfloor < n$ when $n > 0$. For $n = 10$ the values are $10, 5, 2, 1$, then 0, so 4 passes ($\lfloor \lg 10 \rfloor + 1$).

(c) There is no variant, and the loop doesn't stop. The values of $x$ are $4, 2, 0, -2, \dots$, and they step over 1 without landing on it. The condition $x \ne 1$ stays true forever. Testing the guard with `!=` instead of `>` is the mistake.

Check: running (a) and (b) by hand gives 4 passes each, as counted.

</details>

3\. Trace `lower_bound([2, 3, 5, 7, 11, 13], x)` from Example 3 for $x = 7$ and for $x = 4$. Give (lo, hi, mid) at each test and the return value.

<details class="solution" markdown>
<summary>Solution</summary>

For $x = 7$: $(0, 6, 3)$ with `a[3] = 7`, which is not less than 7, so `hi = 3`. Then $(0, 3, 1)$ with `a[1] = 3 < 7`, so `lo = 2`. Then $(2, 3, 2)$ with `a[2] = 5 < 7`, so `lo = 3`. Now $\text{lo} = \text{hi} = 3$ and the function returns 3, and `a[3]` is 7.

For $x = 4$ the first two tests are the same, giving `hi = 3` and `lo = 2`. At $(2, 3, 2)$, `a[2] = 5` is not less than 4, so `hi = 2`. The function returns 2. Position 2 holds 5, the first item that is at least 4, and 4 is not in the list.

Check: for $x = 4$, the items before position 2 (the 2 and the 3) are less than 4 and the items from position 2 on are at least 4, which is the postcondition.

</details>

### Standard

4\. Write a specification and prove this function correct.

```python
def find(a, x):
    i = 0
    while i < len(a):
        if a[i] == x:
            return i
        i += 1
    return -1
```

<details class="solution" markdown>
<summary>Solution</summary>

Specification: there is no precondition beyond `a` being a list. The postcondition is that the result is the smallest index $k$ with `a[k] == x`, or $-1$ if there is none.

Invariant: $0 \le i \le \text{len}(a)$ and `x` is not in `a[0:i]`.

Initialization: $i = 0$, the part `a[0:0]` is empty, and `x` is not in an empty list.

Maintenance: suppose the invariant holds and $i < \text{len}(a)$. If `a[i] == x`, the function returns (see below). Otherwise `a[i] != x`, so `x` is not in `a[0:i+1]`, and after `i += 1` the invariant holds.

Termination: the variant is $\text{len}(a) - i$, which decreases by 1 each pass.

Conclusion: if the function returns $i$ inside the loop, the invariant says `x` is not in `a[0:i]`, and `a[i] == x`, so $i$ is the smallest index. If the loop ends, $i = \text{len}(a)$, so `x` is not in `a[0:len(a)]`, which is the whole list, and $-1$ is correct.

Check: `find([4, 7, 7], 7)` returns 1, the first of the two 7s, and `find([4, 7, 7], 5)` returns $-1$.

</details>

5\. (Reviews [summation notation and series](../../03-high-school/11-sequences-series-and-counting/02-summation-notation-and-series.md).) Prove that the loop below ends with $s = n^2$, for each whole number $n \ge 0$.

```python
s, i = 0, 0
while i < n:
    s += 2 * i + 1
    i += 1
```

<details class="solution" markdown>
<summary>Solution</summary>

Invariant: $0 \le i \le n$ and $s = i^2$.

Initialization: $s = 0 = 0^2$ and $i = 0 \le n$.

Maintenance: if $i < n$, the body sets $s$ to $i^2 + 2i + 1 = (i + 1)^2$ and $i$ to $i + 1 \le n$, so $s = i_{\text{new}}^2$.

Termination: the variant is $n - i$.

Conclusion: the loop stops when $i < n$ is false, so $i = n$ and $s = n^2$.

Check: this is the sum of the first $n$ odd numbers, $1 + 3 + \cdots + (2n - 1) = n^2$. For $n = 5$: $1 + 3 + 5 + 7 + 9 = 25$.

</details>

6\. A 4-litre jug and a 10-litre jug start empty and can be filled, emptied and poured into each other as in Example 5. Prove that exactly 7 litres can never be in either jug, and say which amounts you expect to be possible.

<details class="solution" markdown>
<summary>Solution</summary>

A state is $(x, y)$, the amounts in the two jugs. Claim: in every reachable state both $x$ and $y$ are even. It holds at the start $(0, 0)$. Filling gives 4 or 10, emptying gives 0, and a pour moves $\min(x, 10 - y)$ or $\min(y, 4 - x)$ litres, which is even whenever $x$, $y$, 10 and 4 are even, so both new amounts are even. By the invariant principle, every reachable amount is even, and 7 is odd.

Since $\gcd(4, 10) = 2$, every even amount that fits in a jug is expected to be possible, which are $0, 2, 4, 6, 8, 10$. (A search over the states confirms that all six occur.)

Check: from $(0, 0)$, fill the 10-litre jug and pour into the 4-litre one to get $(4, 6)$, so 6 litres is possible, and emptying the small jug and pouring again gives $(4, 2)$, so 2 is possible.

</details>

### Challenge

7\. Show that the 8-puzzle position with tiles 1 to 6 in place, then 8 and 7 in the second-to-last and last tile squares, and the blank at the bottom right (read as $1, 2, 3, 4, 5, 6, 8, 7, \text{blank}$) can't be reached from the solved position. (Hint: the invariant is the parity of the number of inversions.)

<details class="solution" markdown>
<summary>Solution</summary>

Let $I$ be the number of inversions of the tiles read in order, skipping the blank. We show that $I$ is even in every reachable position of the $3 \times 3$ puzzle.

At the start (the solved position) $I = 0$. A sideways move doesn't change the reading order of the tiles, so $I$ is unchanged. An up or down move slides a tile past exactly two tiles in the reading order (the width is 3, and the two squares between the old and new positions don't hold the blank). Each of the two pairs flips between inversion and non-inversion, so $I$ changes by $\pm 1 \pm 1$, which is $-2$, $0$ or $2$. So $I$ keeps its parity, and "$I$ is even" is an invariant.

The position $1, 2, 3, 4, 5, 6, 8, 7$ has exactly one inversion, the pair $(8, 7)$. That is odd, so by the invariant principle the position is unreachable.

Check: a breadth-first search from the solved position finds $181{,}440 = \frac{9!}{2}$ reachable positions, and the target is not one of them.

</details>

8\. Prove that this integer square root function returns the largest whole number $r$ with $r^2 \le n$, for each whole number $n \ge 0$.

```python
def isqrt(n):
    lo, hi = 0, n + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid
    return lo
```

<details class="solution" markdown>
<summary>Solution</summary>

Invariant: $0 \le \text{lo} < \text{hi}$, $\text{lo}^2 \le n$ and $n < \text{hi}^2$.

Initialization: $\text{lo} = 0$ and $\text{hi} = n + 1$. Then $0 \le n$, and $n < (n+1)^2$ since $(n + 1)^2 \ge n + 1$. Also $0 < n + 1$.

Maintenance: the guard says $\text{hi} - \text{lo} \ge 2$, so $\text{lo} < \text{mid} < \text{hi}$ ($\text{mid}$ is the rounded-down average of two numbers at least 2 apart). If $\text{mid}^2 \le n$, setting $\text{lo} = \text{mid}$ keeps $\text{lo}^2 \le n$, and $n < \text{hi}^2$ is unchanged. Otherwise $\text{mid}^2 > n$ and setting $\text{hi} = \text{mid}$ keeps $n < \text{hi}^2$. In both cases $\text{lo} < \text{hi}$ still holds.

Termination: the variant is $\text{hi} - \text{lo} - 1$. It is at least 1 while the guard is true. Since $\text{lo} < \text{mid} < \text{hi}$, the new gap is smaller than the old one in either case.

Conclusion: the loop stops when $\text{hi} - \text{lo} \le 1$, and with $\text{lo} < \text{hi}$ this means $\text{hi} = \text{lo} + 1$. The invariant gives $\text{lo}^2 \le n < (\text{lo} + 1)^2$, so $\text{lo}$ is the largest whole number whose square is at most $n$.

Check: for $n = 50$ the pairs (lo, hi) at the tests are $(0, 51)$, $(0, 25)$, $(0, 12)$, $(6, 12)$, $(6, 9)$, $(7, 9)$ and $(7, 8)$. Each satisfies $\text{lo}^2 \le 50 < \text{hi}^2$, the loop stops at $(7, 8)$, and the answer is 7, where $49 \le 50 < 64$.

</details>

## Where this shows up

- Every algorithms course proves its greedy and graph algorithms with invariants, and the data structures themselves are defined by them: the heap property, the binary search tree property and the balance conditions of a red-black tree are invariants that every operation must preserve. The next lesson, [asymptotic notation](04-asymptotic-notation.md), asks how many passes a loop makes, and this lesson's variants are the first step.
- Number theory uses the same two algorithms as above: [GCD and Euclid's algorithm](../02-number-theory/02-gcd-and-euclids-algorithm.md) extends the proof, and [Fermat, Euler and fast exponentiation](../02-number-theory/05-fermat-euler-and-fast-exponentiation.md) is Example 6 with a remainder at each step.
- State machines return in the lesson Finite automata: DFA and NFA<!-- link: ../06-theory-of-computation/01-finite-automata-dfa-and-nfa.md -->, where an invariant on the states proves what a machine accepts. Formal verification tools check invariants like these automatically for real programs.
