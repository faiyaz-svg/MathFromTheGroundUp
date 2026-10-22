# Problem-solving playbook

After this page you have a routine for problems you don't know how to start, and a list of moves to try when you are stuck.

A practice problem at the end of a lesson tells you its method, because it comes right after the method. Problems in courses, on exams and in proofs usually don't. George Polya's book *How to Solve It* (Princeton University Press, 1945) describes what to do then, as four steps and a set of questions to ask yourself. This page gives the four steps in plain words, then ten moves with a small example each, then six puzzles to practise on.

## Polya's four steps

1. Understand the problem.
2. Make a plan.
3. Carry out the plan.
4. Look back.

### Understand the problem

Before you calculate anything, answer Polya's three questions. What is the unknown, the thing you have to find or prove? What are the data, the things you are given? What is the condition that connects them? Then restate the problem in your own words, draw a figure if there is anything to draw, and give names to the quantities. If you can't say what a correct answer would look like, you aren't ready to start.

### Make a plan

Ask whether you have seen a related problem, especially one with the same unknown, and whether its method or its result helps here. If nothing comes to mind, pick a move from the list below. A plan can be rough: "find the width first, then the area" is enough.

### Carry out the plan

Do each step and check it as you go. Polya's question here is whether you can see that the step is correct, and whether you could prove it. If the plan stops working, go back to step 2 with what you learned. A plan that fails usually tells you something about the problem.

### Look back

Check the answer by substituting it back, estimating it, or checking its units. Then ask whether you could get it another way, and whether the method would solve other problems. This is the easiest step to skip once you have an answer, and it is the step that builds intuition, because each problem you look back on adds a method to the ones you know.

<div class="example" markdown>

### Example 1: the four steps on one problem

A rectangle has a perimeter of $30$ cm, and its length is twice its width. Find its area.

Step 1: the unknown is the area. The data are the perimeter, $30$ cm, and the condition that the length is twice the width. The answer is an area, so it will be in square centimetres.

Step 2: call the width $w$, so the length is $2w$. The perimeter gives an equation for $w$, and then the area is length times width.

Step 3: the perimeter is $2(w + 2w) = 6w$, so $6w = 30$ and $w = 5$. The width is $5$ cm, the length is $10$ cm, and the area is $5 \times 10 = 50 \text{ cm}^2$.

Step 4: check the conditions. The perimeter is $2(5 + 10) = 30$ cm, and $10$ is twice $5$. Looking back at the method, the width always comes out as one sixth of the perimeter, so the same steps solve every problem of this shape.

</div>

## Moves to try

Each move below comes with a small example. When you are stuck, go down the list and give each move a couple of minutes.

### Try small cases and look for a pattern

When a problem is about a general $n$, work out $n = 1, 2, 3, 4$ by hand, put the answers in a row, and look for a pattern. Then explain why the pattern holds, because a pattern from a few cases is only a guess.

<div class="example" markdown>

How many diagonals does a polygon with $n$ sides have? A diagonal joins two corners that are not next to each other.

| Sides | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| Diagonals | 0 | 2 | 5 | 9 |

The gaps between the counts are $2$, $3$ and $4$, which suggests a formula with $n^2$ in it, and $\frac{n(n-3)}{2}$ fits all four columns. Here is why it works. Each of the $n$ corners joins to $n - 3$ others by a diagonal (every corner except itself and its two neighbours), which gives $n(n - 3)$. That counts each diagonal twice, once from each end, so divide by $2$.

Check: an octagon has $\frac{8 \times 5}{2} = 20$ diagonals.

</div>

<div class="warning" markdown>

Watch out: patterns can fool you. Put $n$ points on a circle, join every pair with a straight line, and place the points so that no three lines cross at one point. For $n = 1$ to $5$ the lines cut the circle into $1$, $2$, $4$, $8$ and $16$ regions. The pattern says $32$ for $n = 6$, but the answer is $31$.

</div>

### Draw a picture or make a table

A table or a sketch shows you what actually happens, instead of what you assume happens.

<div class="example" markdown>

A snail at the bottom of a $10$ m well climbs $3$ m each day and slides back $2$ m each night. On which day does it get out?

The quick answer, "it gains $1$ m a day, so $10$ days", is wrong. A table shows why:

| Day | Height at start of day | Height at end of day | Height after the night |
|---|---|---|---|
| 1 | 0 m | 3 m | 1 m |
| 2 | 1 m | 4 m | 2 m |
| 3 | 2 m | 5 m | 3 m |
| ... | ... | ... | ... |
| 7 | 6 m | 9 m | 7 m |
| 8 | 7 m | 10 m | out |

On day $k$ the snail starts at $k - 1$ metres and climbs to $k + 2$ metres. It reaches the top when $k + 2 = 10$, so on day $8$, and it doesn't slide back that night. The quick answer forgot that the last climb is a full $3$ m.

</div>

### Name things and choose good notation

Give every quantity a name, and choose names that carry information. Many wrong proofs come from giving two different things the same name.

<div class="example" markdown>

Show that the sum of two odd integers is even.

An odd integer has the form $2k + 1$, where $k$ is an integer. Two odd integers need two different letters, so call them $2a + 1$ and $2b + 1$. Their sum is

$$
(2a + 1) + (2b + 1) = 2a + 2b + 2 = 2(a + b + 1),
$$

which is $2$ times an integer, so it is even.

Check: $3 + 7 = 10$. Here $a = 1$ and $b = 3$, and $2(1 + 3 + 1) = 10$.

</div>

<div class="warning" markdown>

Watch out: if you write both odd integers as $2k + 1$, you have only proved the claim for an odd number added to itself.

</div>

### Work backwards from the goal

Start from what you want, and ask what would give you that. Then ask what would give you that, and keep going until you reach something you know is true. In a proof, do this on scratch paper, then write the final proof forwards.

<div class="example" markdown>

Show that $x^2 + 1 \ge 2x$ for every real number $x$.

Backwards: the inequality holds if $x^2 - 2x + 1 \ge 0$, which is the same inequality with $2x$ subtracted from both sides. The left side is $(x - 1)^2$, and the square of a real number is never negative. That is something we know.

Forwards, as you would write it: for every real number $x$, we know $(x - 1)^2 \ge 0$. Multiplying out gives $x^2 - 2x + 1 \ge 0$, and adding $2x$ to both sides gives $x^2 + 1 \ge 2x$.

Check: $x = 3$ gives $10 \ge 6$, and $x = 1$ gives $2 \ge 2$, which is the case where the two sides are equal.

</div>

### Solve a simpler or special version first

If the problem is too big, shrink it: fewer objects, smaller numbers, one dimension instead of two. The small version often shows you the method for the big one.

<div class="example" markdown>

How many squares of all sizes are on an $8 \times 8$ chessboard?

Start smaller. A $2 \times 2$ board has four $1 \times 1$ squares and one $2 \times 2$ square, so $5$ in all. A $3 \times 3$ board has $9 + 4 + 1 = 14$. The counts are sums of perfect squares, and the reason is this: on an $n \times n$ board, a $k \times k$ square can start in $n - k + 1$ positions across and $n - k + 1$ positions down, so there are $(n - k + 1)^2$ of them. For the $8 \times 8$ board:

$$
64 + 49 + 36 + 25 + 16 + 9 + 4 + 1 = 204
$$

Check: the same rule gives $4 + 1 = 5$ for the $2 \times 2$ board and $14$ for the $3 \times 3$ board, which match the counts by hand.

</div>

### Check extreme and edge cases

Push a quantity to an extreme, such as $0$, $1$, a very large value or the empty case, and see whether the answer still makes sense. This catches wrong formulas fast. In code, it means testing an empty list, a list of one item and the largest input; in proofs, it means checking $n = 0$ or the empty set.

<div class="example" markdown>

You drive to a town at $60$ km/h and come back along the same road at $40$ km/h. Is your average speed $50$ km/h?

Try an extreme: suppose you come back at $1$ km/h. The way back then takes $60$ times as long as the way out, so the average speed for the whole trip is just under $2$ km/h, nowhere near the $30.5$ km/h you get by averaging $60$ and $1$. So averaging the two speeds is the wrong method.

Average speed is total distance divided by total time. Say the town is $120$ km away. The way out takes $2$ hours and the way back takes $3$ hours, so you drive $240$ km in $5$ hours, and the average speed is $48$ km/h.

Check: the distance doesn't matter. With $240$ km each way, the trip takes $4 + 6 = 10$ hours for $480$ km, which is again $48$ km/h.

</div>

### Use symmetry

If two things play the same role in a problem, they must have the same answer. Seeing that can save most of a calculation.

<div class="example" markdown>

Roll two fair dice, a red one and a blue one. What is the probability that the red die shows a higher number than the blue one?

The two dice play the same role, so the probability that red is higher equals the probability that blue is higher. Of the $36$ equally likely outcomes, $6$ are ties. The other $30$ split evenly between "red higher" and "blue higher", so $15$ have red higher, and the probability is $\frac{15}{36} = \frac{5}{12}$.

Check by counting directly: a red $2$ beats one blue value, a red $3$ beats two, and so on up to a red $6$, which beats five. That gives $1 + 2 + 3 + 4 + 5 = 15$ outcomes.

</div>

### Look for an invariant

An **invariant** is a quantity that stays the same no matter which allowed move you make. In plain words, it is something the moves can't change. If the invariant has one value at the start and a different value at the goal, the goal can't be reached.

<div class="example" markdown>

The numbers $1$ to $10$ are written on a board. A move is: erase two numbers and write their difference, the larger minus the smaller. After nine moves one number is left. Can it be $0$?

Look at the parity of the total, whether it is odd or even. At the start the total is $1 + 2 + \cdots + 10 = 55$, which is odd. A move removes two numbers $a$ and $b$, where $a \ge b$, and adds $a - b$, so the total goes down by

$$
a + b - (a - b) = 2b,
$$

which is even. Taking away an even number doesn't change parity, so the total stays odd after every move. The last number is the final total, so it is odd, and it can't be $0$.

Check on a smaller board: with $1$, $2$ and $3$ the total is $6$, which is even, and $0$ is reachable. The move $3 - 2 = 1$ leaves $1$ and $1$, and then $1 - 1 = 0$.

</div>

Algorithms courses use the same idea to prove that a loop is correct: a loop invariant<!-- link: ../06-cs-math/04-sums-recurrences-and-algorithms/03-invariants-and-algorithm-correctness.md --> is a statement that is true before the loop starts and stays true after every pass.

### Check units and size

Write units next to every number and carry them through the calculation. A wrong unit at the end means a wrong step somewhere. Then make a rough estimate and see whether your exact answer is close to it.

<div class="example" markdown>

How long does a $4$ GB file take to download at $100$ Mbit/s?

The units don't match: GB is gigabytes, Mbit/s is megabits per second, and a byte is $8$ bits. So $4$ GB is $4 \times 10^9$ bytes, which is $32 \times 10^9$ bits. Then

$$
\frac{32 \times 10^9 \text{ bits}}{100 \times 10^6 \text{ bits/s}} = 320 \text{ s},
$$

which is about $5$ minutes. The usual wrong answer is $40$ seconds, which comes from dividing gigabytes by megabits and forgetting the factor of $8$.

Check the size another way: $100$ Mbit/s is $12.5$ megabytes per second, and $4000$ MB divided by $12.5$ MB/s is $320$ s.

</div>

Here GB means $10^9$ bytes. The difference between GB and GiB comes up in [scientific notation](../02-middle-school/04-powers-roots-and-real-numbers/02-scientific-notation.md), and estimation gets its own lesson in [estimation and sanity checks](../02-middle-school/04-powers-roots-and-real-numbers/04-estimation-and-sanity-checks.md).

### Ask whether you have used all the information

In a homework or exam problem, every given fact is usually there for a reason. If your solution never used one of them, check it: either that fact really isn't needed, or your solution has a gap.

<div class="example" markdown>

Show that if $n$ is odd, then $n^2 - 1$ is divisible by $8$.

Factoring gives $n^2 - 1 = (n - 1)(n + 1)$. If you stop there, you haven't used "$n$ is odd", and the claim is false without it: for $n = 2$, the number $n^2 - 1 = 3$ is not divisible by $8$.

So use it. Write $n = 2k + 1$ for an integer $k$. Then

$$
n^2 - 1 = (2k + 1)^2 - 1 = 4k^2 + 4k = 4k(k + 1).
$$

One of $k$ and $k + 1$ is even, so $k(k + 1)$ is even, and $4$ times an even number is divisible by $8$.

Check: $n = 3$, $5$ and $7$ give $8$, $24$ and $48$, which are all multiples of $8$.

</div>

## When you are stuck

1. Reread the problem. Write down, in symbols, what you are given and what you want.
2. Write out the definition of every term in the problem. In a proof, the definitions often give you the first and last lines: "$n$ is even" becomes "$n = 2k$ for some integer $k$".
3. Try one specific case with small numbers, even if the problem is general.
4. Go down the list of moves above and give each one two minutes.
5. Change the problem. Drop a condition, solve a special case, or work backwards from the goal and see how far you get.
6. Take a break and come back later. A problem often looks different the next day.
7. If you still need help, open the solution, read only its first line, and close it again. Then carry on yourself.
8. Afterwards, write one line about what made the problem work: which move, which idea. That line is the part worth keeping.

In self-study, give a hard problem about 20 to 30 minutes of real effort before you reach step 7.

## Practice puzzles

The puzzles are roughly in order of difficulty. Each solution names the moves it uses, and most puzzles can be solved in more than one way.

### Puzzle 1: odd numbers

Find a formula for the sum of the first $n$ odd numbers, $1 + 3 + 5 + \cdots + (2n - 1)$, and explain why it works.

<details class="solution" markdown>
<summary>Solution</summary>

Try small cases: the sums for $n = 1, 2, 3, 4$ are $1$, $4$, $9$ and $16$. These are perfect squares, so guess that the sum is $n^2$.

Draw a picture to see why. Take a $4 \times 4$ square of dots. The dot in the top-left corner is $1$. The L-shaped layer around it adds $3$ dots and makes a $2 \times 2$ square, the next L-shaped layer adds $5$ and makes a $3 \times 3$ square, and the last adds $7$. Going from an $(n - 1) \times (n - 1)$ square to an $n \times n$ square always adds $n + (n - 1) = 2n - 1$ dots, which is the $n$-th odd number.

Check: for $n = 5$, the sum $1 + 3 + 5 + 7 + 9$ is $25 = 5^2$.

Moves used: small cases and a picture. [A proof by induction](../04-proofs-and-logic/05-induction/01-mathematical-induction.md) turns the picture into a formal argument.

</details>

### Puzzle 2: handshakes

In a room of $n$ people, each person shakes hands exactly once with each other person. How many handshakes are there? How many for $30$ people?

<details class="solution" markdown>
<summary>Solution</summary>

Small cases first: $2$ people make $1$ handshake, $3$ people make $3$, and $4$ people make $6$.

Now count by naming. Each of the $n$ people shakes $n - 1$ hands, which gives $n(n - 1)$. But every handshake involves two people, so that counts each handshake twice. The number of handshakes is

$$
\frac{n(n - 1)}{2}.
$$

For $30$ people that is $\frac{30 \times 29}{2} = 435$.

Check: for $4$ people the formula gives $\frac{4 \times 3}{2} = 6$, which matches the small case.

Look back: this is the number of ways to choose $2$ people out of $n$, written $\binom{n}{2}$. It also matches the diagonals example above. Joining every pair of corners of a polygon uses the $n$ sides plus the diagonals, and $n + \frac{n(n - 3)}{2} = \frac{n(n - 1)}{2}$.

Moves used: small cases, naming and counting each handshake twice, and looking back.

</details>

### Puzzle 3: three stores

At each of three stores, you spend half of the money you have plus another \$2. You leave the third store with \$1. How much did you start with?

<details class="solution" markdown>
<summary>Solution</summary>

Work backwards and undo one store at a time. Leaving a store, you have half of what you walked in with, minus \$2. So to undo a store, add \$2 and then double.

- After store 3 you have \$1, so before it you had $2 \times (1 + 2) = 6$ dollars.
- Before store 2 you had $2 \times (6 + 2) = 16$ dollars.
- Before store 1 you had $2 \times (16 + 2) = 36$ dollars.

You started with \$36.

Check forwards: at store 1 you spend \$18 plus \$2, leaving \$16. At store 2 you spend \$8 plus \$2, leaving \$6. At store 3 you spend \$3 plus \$2, leaving \$1.

Moves used: work backwards from the goal.

</details>

### Puzzle 4: will it finish

A program runs a double loop that does about $n^2$ simple operations, with $n = 10^5$. The computer does about $10^8$ simple operations per second. Will the program finish within a second? How long would an algorithm that does about $n \log_2 n$ operations take?

<details class="solution" markdown>
<summary>Solution</summary>

The double loop does $(10^5)^2 = 10^{10}$ operations. Dividing operations by operations per second gives seconds:

$$
\frac{10^{10}}{10^8 \text{ per second}} = 100 \text{ s},
$$

so no. It takes more than a minute and a half.

For the second algorithm, estimate $\log_2 10^5$. Since $2^{16} = 65{,}536$ and $2^{17} = 131{,}072$, the value is between $16$ and $17$, so use $17$. That gives about $10^5 \times 17 = 1.7 \times 10^6$ operations, which take about $0.017$ seconds.

Check the units: operations divided by operations per second leaves seconds, in both parts.

Moves used: check units and size, and estimate. This is the reason [asymptotic notation](../06-cs-math/04-sums-recurrences-and-algorithms/04-asymptotic-notation.md) matters in an algorithms course.

</details>

### Puzzle 5: a prime pattern

Is $n^2 + n + 41$ prime for every integer $n \ge 0$?

<details class="solution" markdown>
<summary>Solution</summary>

Small cases look convincing. The values for $n = 0, 1, 2, 3$ are $41$, $43$, $47$ and $53$, all prime, and the values stay prime all the way up to $n = 39$.

But a pattern isn't a proof, so look at the structure for a special case. Every term can share the factor $41$ if $n$ is a multiple of $41$. For $n = 41$:

$$
41^2 + 41 + 41 = 41 \times (41 + 1 + 1) = 41 \times 43,
$$

which is not prime. An even earlier case works too: for $n = 40$, the value is $40 \times 41 + 41 = 41 \times 41 = 1681$.

So the answer is no. One counterexample is enough to disprove a statement that begins "for every".

Check: $41 \times 43 = 1763$, and $41^2 + 82 = 1681 + 82 = 1763$.

Moves used: small cases (which mislead here), and a special case chosen from the structure. The lesson on [counterexamples and disproof](../04-proofs-and-logic/04-more-proof-methods/04-counterexamples-and-disproof.md) comes back to this.

</details>

### Puzzle 6: dominoes on a chessboard

Remove two opposite corner squares from an $8 \times 8$ chessboard, which leaves $62$ squares. Can you cover those $62$ squares exactly with $31$ dominoes, each covering two squares that share a side?

<details class="solution" markdown>
<summary>Solution</summary>

No. Look at the colours. Two squares that share a side always have different colours, so each domino covers one dark square and one light square, and $31$ dominoes cover $31$ of each.

Opposite corners have the same colour (on a standard board, both are dark). The full board has $32$ dark and $32$ light squares, so removing both corners leaves $30$ dark and $32$ light. The two counts are not equal, so no covering exists.

Check with a simpler version: remove two opposite corners of a $2 \times 2$ board. The two squares left are the same colour and only touch at a corner, so no domino fits.

Moves used: look for an invariant (each domino covers one square of each colour), draw a picture, and solve a simpler version to check.

</details>
