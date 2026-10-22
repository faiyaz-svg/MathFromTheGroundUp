# Compound inequalities and interval notation

After this lesson you can solve compound inequalities joined by "and" or "or", write any solution set in interval notation (including the empty set and all of $\mathbb{R}$), and read a set off a number-line graph.

Before this: [inequalities](../../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md), [negative numbers and absolute value](../../02-middle-school/01-integers-and-rational-numbers/01-negative-numbers-and-absolute-value.md) and [real numbers, axioms and set notation](01-real-numbers-axioms-and-set-notation.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Solve $-3 \le 2x + 1 < 7$ and write the answer in interval notation.
2. Solve "$3x - 1 < -7$ or $2x + 5 \ge 9$" and write the answer in interval notation.
3. Write the solution of "$x \ge 5$ and $x < 2$", and of "$x < 3$ or $x > 1$", in interval notation.

<details class="solution" markdown>
<summary>Answers</summary>

1. $[-2, 3)$. Subtract 1 from all three parts to get $-4 \le 2x < 6$, then divide by 2 to get $-2 \le x < 3$.
2. $(-\infty, -2) \cup [2, \infty)$. The first inequality gives $x < -2$, and the second gives $x \ge 2$. "Or" keeps both pieces.
3. The first is $\emptyset$: no number is both at least 5 and less than 2. The second is $(-\infty, \infty)$, all of $\mathbb{R}$: every number is below 3 or above 1, since the two pieces overlap between 1 and 3.

</details>

## The idea

A thermostat is set to keep the room between 19°C and 22°C, ends included. A temperature $T$ is acceptable when $19 \le T$ and $T \le 22$. Both conditions must hold at once, so the acceptable temperatures are the ones that satisfy the first and the second. A transit fare works the other way: a discount applies to riders under 13 or 65 and over. A rider qualifies by meeting either condition, so the discount group is made of everyone who satisfies the first or the second.

These are the two kinds of compound inequality. With "and", a number is a solution only if it solves both inequalities, so the solution set is the overlap of the two solution sets. With "or", a number is a solution if it solves at least one, so the solution set is everything covered by either. In the thermostat example the overlap is a single stretch of the number line. In the fare example the answer is two separate pieces, one on each side.

Writing these sets with inequalities gets clumsy. "The temperatures from 19 up to and including 22" has the short form $[19, 22]$, and "under 13 or 65 and over" has the short form $(-\infty, 13) \cup [65, \infty)$. This lesson is about getting from the words or the inequalities to that short form, and back, without mistakes.

## Definitions

A **compound inequality** is two inequalities joined by "and" or "or", as previewed in [inequalities](../../02-middle-school/03-expressions-equations-inequalities/05-inequalities.md#compound-inequalities-a-preview). The statement $-2 < x \le 5$ is a chain, a shorthand for "$-2 < x$ and $x \le 5$". A chain needs both symbols to point the same way. An "or" statement can't be written as a chain, since the two pieces are not connected.

Two operations on sets turn the solution sets of the pieces into the solution set of the whole. The **intersection** $A \cap B$ is the set of elements that are in both $A$ and $B$, and the **union** $A \cup B$ is the set of elements that are in $A$, in $B$, or in both. For example, $\{1, 2, 3\} \cap \{2, 3, 4\} = \{2, 3\}$ and $\{1, 2, 3\} \cup \{2, 3, 4\} = \{1, 2, 3, 4\}$. The **set difference** $A \setminus B$ is the set of elements of $A$ that are not in $B$, so $\mathbb{R} \setminus \{0\}$ is every real number except 0.

In plain words, "and" means intersection and "or" means union. If $S_1$ and $S_2$ are the solution sets of two inequalities, then "first and second" has solution set $S_1 \cap S_2$ and "first or second" has solution set $S_1 \cup S_2$. The math "or" is inclusive: a number that satisfies both pieces is a solution, and is listed once.

An **interval** is a set of real numbers that contains every number between two endpoints, where each endpoint may or may not belong to the set, or the set runs on forever in one or both directions. **Interval notation** writes an interval with the smaller endpoint first, then the larger, with a bracket where an endpoint is included and a parenthesis where it is not.

| Interval | Set-builder form | In words |
|---|---|---|
| $(a, b)$ | $\{x \in \mathbb{R} : a < x < b\}$ | between $a$ and $b$, neither included |
| $[a, b]$ | $\{x \in \mathbb{R} : a \le x \le b\}$ | from $a$ to $b$, both included |
| $[a, b)$ | $\{x \in \mathbb{R} : a \le x < b\}$ | $a$ included, $b$ not |
| $(a, b]$ | $\{x \in \mathbb{R} : a < x \le b\}$ | $b$ included, $a$ not |
| $(a, \infty)$ | $\{x \in \mathbb{R} : x > a\}$ | everything above $a$ |
| $[a, \infty)$ | $\{x \in \mathbb{R} : x \ge a\}$ | $a$ and everything above |
| $(-\infty, b)$ | $\{x \in \mathbb{R} : x < b\}$ | everything below $b$ |
| $(-\infty, b]$ | $\{x \in \mathbb{R} : x \le b\}$ | $b$ and everything below |
| $(-\infty, \infty)$ | $\mathbb{R}$ | every real number |

The symbol $\infty$ ("infinity") is not a number. It only says that the interval has no end in that direction. Since there is no largest real number to include, an infinite end always gets a parenthesis: $[3, \infty)$ is correct, and $[3, \infty]$ is not.

A number-line graph shows the same information. An **open dot** at an endpoint means that the endpoint is not included, which goes with a parenthesis or a strict inequality. A **closed dot** means it is included, which goes with a bracket or $\le$, $\ge$. A solution set that runs off the line has an arrow. In the figure, each row has the inequality on the left, its graph, and its interval notation on the right.

![Six number lines. Row 1 shades the numbers between -1 and 3 with open dots at both ends, labelled -1 < x < 3 and (-1, 3). Row 2 has closed dots at both ends, labelled [-1, 3]. Row 3 has a closed dot at -1 and an open dot at 3, labelled [-1, 3). Row 4 has an open dot at -1 and a closed dot at 3, labelled (-1, 3]. Row 5 shades everything to the right of an open dot at 1, labelled x > 1 and (1, infinity). Row 6 shades everything to the left of a closed dot at 2, labelled x <= 2 and (-infinity, 2].](../../assets/figures/03-high-school/compound-inequalities-and-interval-notation-interval-types.svg)

Some intervals are tiny or empty. The interval $[a, a]$ contains the single number $a$, so $[a, a] = \{a\}$. The intervals $(a, a)$ and $[a, a)$ contain no numbers, so they are $\emptyset$, and an interval written with its endpoints in the wrong order, such as $[5, 2]$, is not allowed. The symbol $(3, 4)$ also means the point with coordinates 3 and 4 on the coordinate plane. The context tells you which one is meant: a point is in a plane, and an interval is on a line.

## How to do it

### Solving an "and" inequality

1. Solve each inequality on its own, with the rules from the inequalities lesson. Reverse the symbol when you multiply or divide by a negative number.
2. Graph each solution set on its own number line, one above the other, with the numbers lined up.
3. Keep the overlap: the numbers shaded on both lines. An endpoint is in the overlap only if both sets contain it.
4. Write the overlap in interval notation, with the smaller endpoint first. If nothing overlaps, write $\emptyset$.
5. Check one number inside the answer, one in each part outside it, and each endpoint in the original inequalities.

A chain such as $-3 \le 2x + 1 < 7$ is two inequalities with the middle shared, so it can be solved in one go. Do the same operation to all three parts: here subtract 1, then divide by 2. Both symbols reverse when you multiply or divide by a negative number, and then you rewrite the result with the smaller number on the left, so $4 > x \ge -3$ becomes $-3 \le x < 4$.

### Solving an "or" inequality

1. Solve each inequality on its own.
2. Graph each solution set on its own number line.
3. Keep everything that is shaded on at least one line.
4. If two pieces overlap or touch, merge them into one. For example, "$x \le 2$ or $x > 2$" covers the whole line, but "$x < 2$ or $x > 2$" leaves out the point 2.
5. Write the result with $\cup$, left piece first: $(-\infty, -2) \cup [2, \infty)$.
6. Check one number in each piece, one in the gap between the pieces, and each endpoint.

### The numbers that are not between two others

Statements such as "$x$ is not between 1 and 5" turn up when solving absolute value inequalities in the next lesson. This theorem says that they split into two outside pieces.

*Theorem.* Let $a$ and $b$ be real numbers with $a < b$, and let $x$ be a real number. Then $x \notin (a, b)$ exactly when $x \le a$ or $x \ge b$.

We know the definition $x \in (a, b)$ means "$a < x$ and $x < b$", and that for any two numbers exactly one of $<$, $=$, $>$ holds (the order axiom O2 in [real numbers, axioms and set notation](01-real-numbers-axioms-and-set-notation.md#the-order-axioms), applied to the difference of the two numbers). We want the exact opposite of "and". The plan is to use the fact that "$P$ and $Q$" is false exactly when $P$ is false or $Q$ is false, and to say what "not $<$" means.

*Proof.* The statement $x \notin (a, b)$ says that "$a < x$ and $x < b$" is false. That happens exactly when "$a < x$" is false or "$x < b$" is false. If $a < x$ is false, then $x = a$ or $x < a$ by trichotomy, which is $x \le a$. If $x < b$ is false, then $x \ge b$ in the same way. So $x \notin (a, b)$ exactly when $x \le a$ or $x \ge b$. $\blacksquare$

Look back: the "and" turned into an "or", and each strict inequality turned into a non-strict one, so the outside pieces include the endpoints. In interval notation the theorem says that the complement of $(a, b)$ in $\mathbb{R}$ is $(-\infty, a] \cup [b, \infty)$. The same argument shows that the complement of $[a, b]$ is $(-\infty, a) \cup (b, \infty)$. With $a = 1$ and $b = 5$, the number 5 is not in $(1, 5)$, and indeed $5 \ge 5$.

## Worked examples

<div class="example" markdown>

### Example 1: an "and" inequality

Solve "$2x + 3 > -1$ and $5 - x \ge 1$", graph the answer, and write it in interval notation.

Step 1: solve each inequality. For the first, subtract 3 to get $2x > -4$, then divide by 2: $x > -2$. For the second, subtract 5 to get $-x \ge -4$, then divide by $-1$ and reverse the symbol: $x \le 4$.

Step 2: graph both, and Step 3: keep the overlap. The first set is everything to the right of $-2$ (not including $-2$), and the second is everything to the left of 4 (including 4). The third line shows the numbers on both:

![Three number lines from -4 to 6. The first shades everything to the right of an open dot at -2 and is labelled x > -2. The second shades everything to the left of a closed dot at 4 and is labelled x <= 4. The third shades only the stretch between them, with an open dot at -2 and a closed dot at 4, labelled both and (-2, 4]. Dashed vertical lines at -2 and 4 connect the three lines.](../../assets/figures/03-high-school/compound-inequalities-and-interval-notation-intersection.svg)

Step 4: the overlap has $-2$ excluded and 4 included, so it is $(-2, 4]$. In set-builder form, $\{x \in \mathbb{R} : -2 < x \le 4\}$.

<div class="warning" markdown>

Watch out: the number 4 is in the overlap because both sets contain it, but $-2$ is not, because the first set leaves it out. The endpoint rule for "and" is that an endpoint is included only if every piece includes it.

</div>

Step 5: check. At the endpoint 4, the first inequality gives $2 \cdot 4 + 3 = 11 > -1$, which is true, and the second gives $5 - 4 = 1 \ge 1$, which is true, so 4 belongs. At $-2$, the first gives $-1 > -1$, which is false, so $-2$ does not belong. At the test number 0, both are true. At 5 the second gives $0 \ge 1$, which is false, and at $-3$ the first is false, so neither outside number belongs.

</div>

<div class="example" markdown>

### Example 2: an "or" inequality

Solve "$3x - 1 < -7$ or $2x + 5 \ge 9$", graph the answer, and write it in interval notation.

Step 1: solve each inequality. For the first, add 1 to get $3x < -6$, then divide by 3: $x < -2$. For the second, subtract 5 to get $2x \ge 4$, then divide by 2: $x \ge 2$.

Steps 2 and 3: graph both and keep everything shaded on at least one line:

![Three number lines from -5 to 5. The first shades everything to the left of an open dot at -2 and is labelled x < -2. The second shades everything to the right of a closed dot at 2 and is labelled x >= 2. The third shows both pieces shaded, with an open dot at -2 and a closed dot at 2, labelled either and (-infinity, -2) union [2, infinity). Dashed vertical lines at -2 and 2 connect the three lines.](../../assets/figures/03-high-school/compound-inequalities-and-interval-notation-union.svg)

The pieces don't overlap, so no merging is needed. Step 5: the answer is $(-\infty, -2) \cup [2, \infty)$.

Step 6: check. At $-2$ the first inequality gives $3(-2) - 1 = -7 < -7$, which is false, and the second gives $2(-2) + 5 = 1 \ge 9$, which is false, so $-2$ is out. At 2 the second gives $4 + 5 = 9 \ge 9$, which is true, so 2 is in. A number from the gap between the pieces, such as 0, fails both: $-1 < -7$ and $5 \ge 9$ are false. A number from each piece works, for instance $-5$ in the first ($-16 < -7$) and 4 in the second ($13 \ge 9$).

</div>

<div class="example" markdown>

### Example 3: empty, one point, and everything

Solve each statement, and write the answer in interval notation.

- (a) $x < 1$ and $x > 3$. No number is both below 1 and above 3, so the answer is $\emptyset$.
- (b) $x \le 2$ and $x \ge 2$. Only 2 satisfies both, so the answer is the single number $\{2\}$, which is the interval $[2, 2]$.
- (c) $x < 2$ or $x > 2$. Every number except 2 satisfies one of them, so the answer is $(-\infty, 2) \cup (2, \infty)$, which can also be written $\mathbb{R} \setminus \{2\}$ or "$x \ne 2$".
- (d) $x < 3$ or $x > 1$. A number that isn't below 3 is at least 3, so it is above 1. So every number satisfies at least one, and the answer is $(-\infty, \infty)$, which is $\mathbb{R}$.

![Four number lines from 0 to 5, each with the statement on the left and its answer on the right. The first, x < 1 and x > 3, has nothing shaded and is labelled the empty set. The second, x <= 2 and x >= 2, has a single closed dot at 2 and is labelled {2}. The third, x < 2 or x > 2, has the whole line shaded with an open dot at 2. The fourth, x < 3 or x > 1, has the whole line shaded and is labelled (-infinity, infinity).](../../assets/figures/03-high-school/compound-inequalities-and-interval-notation-special-cases.svg)

Check (a) and (d) with a test number. At 2, "$x < 1$ and $x > 3$" says "false and false", so 2 is not in the set, and "$x < 3$ or $x > 1$" says "true or true", so 2 is in it. Check (c) at 2, the only number that fails both pieces.

</div>

<div class="example" markdown>

### Example 4: a chain with a negative coefficient (finish it yourself)

Solve $-7 < 1 - 4x \le 9$ and write the answer in interval notation.

Do the same thing to all three parts. Subtract 1 from each part:

$$
-8 < -4x \le 8.
$$

Now finish: divide all three parts by $-4$, say what happens to the symbols, write the answer with the smaller number on the left, and check both endpoints in the original.

<details class="solution" markdown>
<summary>Finish</summary>

Dividing by $-4$, a negative number, reverses both symbols:

$$
2 > x \ge -2.
$$

Written with the smaller number on the left, this is $-2 \le x < 2$, which is the interval $[-2, 2)$.

Check: at $x = -2$ the middle part is $1 - 4(-2) = 9$, and $-7 < 9 \le 9$ is true, so $-2$ belongs. At $x = 2$ it is $1 - 8 = -7$, and $-7 < -7$ is false, so 2 does not. At the test number 0 it is 1, and $-7 < 1 \le 9$ is true.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: an infinite end never takes a bracket. Writing $(3, \infty]$ or $[-\infty, 5)$ treats $\infty$ as a number that could be included. The correct forms are $(3, \infty)$ and $(-\infty, 5)$, even when the finite end is included, as in $[3, \infty)$.

</div>

<div class="warning" markdown>

Watch out: don't use $\cup$ for "and". The statement "$x > 1$ and $x < 3$" is the overlap, $(1, 3)$. Writing $(1, \infty) \cup (-\infty, 3)$ gives every real number, since 5 is in the first piece and $-2$ is in the second. Test one number that should be outside, like 5: it is above 1 but not below 3, so "and" rejects it.

</div>

<div class="warning" markdown>

Watch out: an "or" statement is not a chain. Writing "$-2 > x \ge 2$" for "$x < -2$ or $x \ge 2$" says $x < -2$ and $x \ge 2$, which no number satisfies. A chain always means "and". Write an "or" answer as two pieces joined by "or" or by $\cup$.

</div>

<div class="warning" markdown>

Watch out: the smaller endpoint goes first. After dividing a chain by a negative number you get $4 > x \ge -3$, and the interval is $[-3, 4)$, not $[4, -3)$. Rewrite the chain with the smaller number on the left before you write the interval.

</div>

Overlapping pieces are merged, not listed twice. For "$x < 5$ or $x < 8$", the answer is $(-\infty, 8)$, not $(-\infty, 5) \cup (-\infty, 8)$. In the same way, $(1, 5) \cup (3, 8) = (1, 8)$.

Checking the endpoints alone is not enough. An endpoint test tells you whether the endpoint belongs, but not whether you shaded the correct side. Always try one number from inside the answer too, as in Example 1.

A single point can be a complete answer: "$x \le 2$ and $x \ge 2$" is $\{2\}$. And $\emptyset$ is also a complete answer, written as $\emptyset$, not as "$0$" or "none of them".

## Tricks and shortcuts

Remember "between means and, outside means or". A number between 2 and 8 is above 2 and below 8. A number outside the interval is below 2 or above 8. Absolute value inequalities in the next lesson come in exactly these two kinds.

To choose test points, mark the boundary numbers on the line. They cut the line into pieces, and every number in one piece behaves the same way. Test one number from each piece, plus each boundary number, and the whole answer is decided. For Example 2 the boundary numbers are $-2$ and 2, so the tests are $-5$, $-2$, $0$, $2$ and $4$.

Endpoints follow a simple rule. For "and", an endpoint is included only if every piece includes it. For "or", an endpoint is included if any piece includes it. That is why $(-\infty, 2) \cup [2, \infty) = \mathbb{R}$ while $(-\infty, 2) \cup (2, \infty)$ misses the single point 2.

Programmers meet half-open intervals daily. Python's `range(0, 5)` is the interval $[0, 5)$ restricted to integers, and slices such as `a[2:6]` include index 2 and exclude index 6. Adjacent half-open intervals, $[0, 5)$ and $[5, 10)$, share no point and leave no gap, which is why they are the usual choice for bins in a histogram.

## In code

Sympy represents intervals, and its `intersect` and `union` methods apply the rules above. A plain Python chain tests membership.

<details class="code" markdown>
<summary>In code</summary>

```python
from sympy import Interval, oo

A = Interval.open(-2, oo)               # x > -2
B = Interval(-oo, 4)                    # x <= 4
print(A.intersect(B))                   # Interval.Lopen(-2, 4)

C = Interval.open(-oo, -2)              # x < -2
D = Interval(2, oo)                     # x >= 2
print(C.union(D))                       # Union(Interval.open(-oo, -2), Interval(2, oo))

print(Interval.open(-oo, 2).union(Interval.open(2, oo)))   # Union(Interval.open(-oo, 2), Interval.open(2, oo))
print(Interval(-oo, 3).union(Interval(1, oo)))             # Interval(-oo, oo)
print(Interval.open(-oo, 1).intersect(Interval.open(3, oo)))   # EmptySet

# Plain Python: a chain is "and", and "or" is spelled out.
print([x for x in range(-6, 7) if -3 <= 2 * x + 1 < 7])          # the integers in [-2, 3): [-2, -1, 0, 1, 2]
print([x for x in range(-6, 7) if 3 * x - 1 < -7 or 2 * x + 5 >= 9])   # [-6, -5, -4, -3, 2, 3, 4, 5, 6]
```

In sympy's output, `Interval.Lopen(-2, 4)` means the left end is open and the right end is closed, which is $(-2, 4]$, and `oo` is infinity. The plain-Python lines test integers only, so they show the pattern but not the whole interval: the integers in $[-2, 3)$ are $-2$ to 2, and the integers that satisfy the "or" statement skip $-2$ to 1, the gap in Example 2.

</details>

## FAQ

### Why is the math "or" inclusive, when "or" in English often means one or the other?

"Soup or salad" usually means one of the two. In mathematics "P or Q" is true when at least one of them is, including both at once. This choice makes the union of two sets contain everything in either one, with the common part counted once, and it keeps rules such as "not (P and Q) means (not P) or (not Q)" simple, as in the theorem above. If you want the exclusive meaning, you say "exactly one of".

### Can a solution set of an "or" inequality ever be a single interval?

Yes, when the pieces overlap or touch. "$x < 5$ or $x \ge 3$" is all of $\mathbb{R}$, and "$x < 3$ or $x < 8$" is the single interval $(-\infty, 8)$. In the common case where the pieces point away from each other, as in $x < -2$ or $x \ge 2$, you get two separate pieces.

### Is $(-\infty, \infty)$ the same as $\mathbb{R}$?

Yes. Both name the set of all real numbers. The interval form is useful in a list of answers, as in "the solution set is $(-\infty, \infty)$", and $\mathbb{R}$ is the usual name when the set is a ground set, as in $\{x \in \mathbb{R} : \dots\}$.

### Why do we need interval notation when inequalities already describe the set?

Inequalities describe one piece well, but the notation is clumsy for unions, and it hides the endpoints inside symbols. Interval notation makes the endpoints visible, works with $\cup$ and $\cap$, and is what calculus and statistics use when they say "on the interval $[0, 1]$" or "the domain is $(0, \infty)$". It is also shorter to type.

## Practice

### Warm-up

1\. Write each set in interval notation: (a) $-1 \le x < 5$, (b) $x > 2$, (c) $x \le -3$, (d) all real numbers. Then write each interval as an inequality: (e) $[-4, 0)$, (f) $(-\infty, 7)$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $-1$ is included and 5 is not: $[-1, 5)$.
- (b) No upper end, and 2 is not included: $(2, \infty)$.
- (c) No lower end, and $-3$ is included: $(-\infty, -3]$.
- (d) $(-\infty, \infty)$.
- (e) $-4 \le x < 0$.
- (f) $x < 7$.

Check (a) by testing: $-1$ should be in the set ($-1 \le -1$), and 5 should not be ($5 < 5$ is false).

</details>

2\. Solve "$x - 3 < 2$ and $x + 1 > -2$", and write the answer in interval notation.

<details class="solution" markdown>
<summary>Solution</summary>

The first inequality gives $x < 5$, and the second gives $x > -3$. The overlap is the numbers between $-3$ and 5, with both ends excluded: $(-3, 5)$.

Check at the test number 0: $-3 < 2$ and $1 > -2$ are both true. At 5, the first is $2 < 2$, which is false, and at $-3$ the second is $-2 > -2$, which is false, so both ends are correctly excluded.

</details>

3\. Solve "$2x \le -6$ or $x - 1 > 4$", and write the answer in interval notation.

<details class="solution" markdown>
<summary>Solution</summary>

The first inequality gives $x \le -3$, and the second gives $x > 5$. The pieces don't overlap, so the answer is $(-\infty, -3] \cup (5, \infty)$.

Check: at $-3$, $2(-3) = -6 \le -6$ is true, so $-3$ is in. At 5, $5 - 1 = 4 > 4$ is false and $10 \le -6$ is false, so 5 is out. The gap number 0 fails both, as it should.

</details>

### Standard

4\. Solve $-4 \le 3x - 1 \le 11$, and write the answer in interval notation.

<details class="solution" markdown>
<summary>Solution</summary>

Add 1 to all three parts: $-3 \le 3x \le 12$. Divide all three parts by 3, which is positive, so the symbols stay: $-1 \le x \le 4$. The interval is $[-1, 4]$.

Check the ends: at $x = -1$, $3(-1) - 1 = -4$, and $-4 \le -4$ is true. At $x = 4$, $3 \cdot 4 - 1 = 11$, and $11 \le 11$ is true. At the test number 0, the middle part is $-1$, between $-4$ and 11.

</details>

5\. A courier charges \$12 plus \$0.80 per kilogram. You have a budget of at least \$20 and at most \$32. What weights $w$ (in kilograms) can you ship? Write the answer in interval notation.

<details class="solution" markdown>
<summary>Solution</summary>

The cost is $12 + 0.80w$, and the budget says $20 \le 12 + 0.80w \le 32$. Subtract 12 from all three parts: $8 \le 0.80w \le 20$. Divide by 0.80: $10 \le w \le 25$. The weights are $[10, 25]$ kilograms.

Check the ends: a 10 kg parcel costs $12 + 8 = 20$ dollars, and a 25 kg parcel costs $12 + 20 = 32$ dollars. A 26 kg parcel costs \$32.80, which is over the budget.

</details>

6\. For each statement, say whether the answer is the empty set, a single number, one interval, two pieces or all of $\mathbb{R}$, and write it in interval notation. (a) $x < 2$ and $x > 5$, (b) $x \le 5$ or $x > 2$, (c) $x \le -1$ and $x \ge -1$, (d) $x < 3$ or $x > 3$, (e) $x > 1$ and $x \ge 4$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) No number is below 2 and above 5: the empty set, $\emptyset$.
- (b) A number that isn't at most 5 is above 5, so it is above 2. Every number works: $(-\infty, \infty)$.
- (c) Only $-1$ is both at most and at least $-1$: a single number, $\{-1\}$.
- (d) Every number except 3: two pieces, $(-\infty, 3) \cup (3, \infty)$.
- (e) A number at least 4 is also above 1, so the second condition decides: one interval, $[4, \infty)$.

Check with test numbers: for (e), $x = 4$ satisfies both, and $x = 3$ satisfies the first but not the second, so 3 is out. For (b), $x = 0$ is at most 5, so it is in.

</details>

### Challenge

7\. (a) For which values of $k$ does "$x > 2$ and $x < k$" have at least one solution? Write the solution set in each case. (b) Answer the same question for "$x \ge 2$ and $x \le k$".

<details class="solution" markdown>
<summary>Solution</summary>

(a) The solutions are the numbers strictly between 2 and $k$. There are some exactly when $2 < k$, and then the set is $(2, k)$. If $k \le 2$, nothing is above 2 and below $k$, so the set is $\emptyset$.

(b) The solutions are the numbers from 2 to $k$, ends included. There are some exactly when $2 \le k$. For $k > 2$ the set is $[2, k]$, and for $k = 2$ it is the single number $\{2\}$. For $k < 2$ it is $\emptyset$.

The difference between (a) and (b) is at $k = 2$: with strict symbols the set is empty, and with non-strict symbols it is one point.

Check with numbers: for $k = 5$, (a) has $3$ as a solution, and for $k = 2$, (a) has none while (b) has 2.

</details>

8\. This one reviews [percents](../../02-middle-school/02-ratios-rates-percents/03-percents.md). A store takes 20% off the regular price $p$ and then adds 13% HST. You want to pay at least \$40 and at most \$60. What regular prices $p$ work? Write the answer in interval notation, rounding each end to the cent in the direction that keeps the payment inside the budget.

<details class="solution" markdown>
<summary>Solution</summary>

The payment is $0.80 \times 1.13 \times p = 0.904p$. The budget says $40 \le 0.904p \le 60$. Divide all three parts by 0.904, which is positive:

$$
\frac{40}{0.904} \le p \le \frac{60}{0.904}, \quad \text{that is,} \quad 44.2477\ldots \le p \le 66.3716\ldots
$$

Prices are in cents. The smallest price that keeps the payment at \$40 or more is the lower end rounded up, \$44.25, and the largest price that keeps it at \$60 or less is the upper end rounded down, \$66.37. The set is $[44.25, 66.37]$.

Check: $0.904 \times 44.25 = 40.002$, which is at least 40, while $0.904 \times 44.24 = 39.993$ falls short. And $0.904 \times 66.37 = 59.998$ is at most 60, while $0.904 \times 66.38 = 60.008$ is over.

</details>

## Where this shows up

- The next lesson, [absolute value equations and inequalities](04-absolute-value-equations-and-inequalities.md), turns "$x$ is within 2 of 5" into "$-2 < x - 5 < 2$", a chain from this lesson, and "$x$ is more than 2 from 5" into an "or". [Two-variable inequalities and feasible regions](../02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md) shades the plane where several inequalities hold at once, which is the "and" of this lesson in two dimensions.
- [Polynomial and rational inequalities](../06-rational-expressions-and-equations/04-polynomial-and-rational-inequalities.md) produce answers such as $(-\infty, -1) \cup (2, 5]$, and calculus states domains, closed intervals and limits in this notation. [Continuous random variables and the normal distribution](../../05-university-core/07-probability/04-continuous-random-variables-and-the-normal.md) asks for $P(a \le X \le b)$, the probability of an interval.
- In economics, a price floor and a price ceiling define an interval of allowed prices, and a budget is a set of affordable bundles (surplus and market interventions<!-- link: ../../07-economics-math/02-markets/04-surplus-and-market-interventions.md -->). In code, bounds checks such as `lo <= i < hi` are interval membership, and half-open intervals are why `range(n)` stops at $n - 1$.
