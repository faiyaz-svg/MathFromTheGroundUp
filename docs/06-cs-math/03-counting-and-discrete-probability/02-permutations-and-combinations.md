# Permutations and combinations

After this lesson you can derive the counts for ordered and unordered selections from the product and division rules, count arrangements with repeated items, count selections with repetition by stars and bars, count circular arrangements, and pick the right count from a table that asks whether order matters and whether repetition is allowed.

Before this: [counting rules](01-counting-rules.md). The high school lesson, [counting: permutations and combinations](../../03-high-school/11-sequences-series-and-counting/03-counting-permutations-combinations.md), covers the first three tools at a quick pace. This lesson proves them from the division rule and adds repetition, groups and circles.

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. In poker you are dealt 5 cards from a standard 52-card deck. How many hands are a full house, three cards of one rank and two cards of another?
2. How many ways are there to put 10 identical donuts into 4 different boxes, if a box may be empty?
3. Six different people sit at a round table, and two seatings are the same if one is a rotation of the other. How many seatings are there?

<details class="solution" markdown>
<summary>Answers</summary>

1. Choose the rank of the triple (13 ways) and which 3 of its 4 suits ($\binom{4}{3} = 4$), then a different rank for the pair (12 ways) and 2 of its 4 suits ($\binom{4}{2} = 6$): $13 \cdot 4 \cdot 12 \cdot 6 = 3{,}744$.
2. Write 10 stars and 3 bars in a row, the bars separating the boxes. Choosing the places of the 3 bars among the 13 symbols gives $\binom{13}{3} = 286$.
3. The 720 orderings of the 6 people fall into groups of 6 rotations each, so there are $\frac{720}{6} = 120$ seatings.

</details>

## The idea

Questions about choosing things look alike and have different answers. Picking a president, a vice-president and a treasurer from a club is different from picking a committee of three, and picking three scoops of ice cream from five flavours is different again if you may repeat a flavour. Two questions sort out almost all of them. Does the order of the chosen items matter? Can an item be chosen more than once?

Each of the four combinations has a count, and each comes from the rules of the previous lesson. Order matters and repeats are allowed: build the list in stages and multiply. Order matters and repeats are not allowed: the same, with fewer choices at each stage. Order doesn't matter: build the ordered version and divide by the number of orders. The last case, no order and repeats allowed, is the one the high school lesson only stated. It has a clever proof, in which a selection is turned into a row of stars and bars.

The lesson then uses the same two moves, stage-by-stage products and division by a fixed number of repeats, for items that are alike, for groups that are labelled or not, and for seats around a table where rotations don't count.

## Definitions

A **$k$-permutation** of $n$ different items is an ordered list of $k$ different items chosen from them. The number of them is $P(n, k) = n(n-1)\cdots(n-k+1)$, for $0 \le k \le n$. In plain words, it counts the ways to fill $k$ ranked places, such as gold, silver and bronze, from $n$ candidates.

A **$k$-combination** of an $n$-element set is a subset with $k$ elements, and the number of them is the **binomial coefficient** $\binom{n}{k}$, read "$n$ choose $k$". In plain words, it counts the ways to choose $k$ items when only the group matters and not the order.

A **multiset** is a collection of items in which an item can appear more than once, and the order is ignored. A multiset of size $k$ from $n$ types is a list of how many of each type, such as two vanilla and one mango. In plain words, it is a selection with repeats allowed and order ignored.

The **multinomial coefficient** for numbers $n_1, \dots, n_m$ with $n_1 + \cdots + n_m = n$ is

$$
\binom{n}{n_1, n_2, \dots, n_m} = \frac{n!}{n_1!\, n_2! \cdots n_m!}.
$$

In plain words, it counts the ways to split $n$ different items into $m$ labelled groups of sizes $n_1, \dots, n_m$, and it also counts the words that can be made from $n_1$ copies of one letter, $n_2$ of another, and so on. With $m = 2$ it is $\binom{n}{n_1}$.

A **circular arrangement** of $n$ items is an arrangement around a circle in which two lists count as the same if one is a rotation of the other. In plain words, only who sits next to whom, and on which side, matters, and not which seat anyone started in.

## How to do it

### Choosing the count

1. Say what one outcome looks like, and what you are counting.
2. Ask whether swapping two chosen items gives a different outcome. If yes, order matters.
3. Ask whether an item can be chosen twice. A PIN can repeat a digit, and a committee can't repeat a person.
4. Read the count off the table, or split the problem into stages and cases.
5. Check on a tiny case that you can list.

| Order matters? | Repetition allowed? | Count | Example with $n = 5$, $k = 3$ |
|---|---|---|---|
| yes | yes | $n^k$ | 3-letter strings from 5 letters: 125 |
| yes | no | $P(n, k) = \frac{n!}{(n-k)!}$ | gold, silver, bronze from 5 runners: 60 |
| no | no | $\binom{n}{k}$ | a committee of 3 from 5 people: 10 |
| no | yes | $\binom{n+k-1}{k}$ | 3 scoops from 5 flavours: 35 |

The same ideas answer questions about putting $n$ objects into $k$ boxes:

| Objects | Boxes | Count |
|---|---|---|
| different | labelled, any size | $k^n$ |
| alike | labelled, any size | $\binom{n+k-1}{k-1}$ |
| different | labelled, sizes $n_1, \dots, n_k$ fixed | $\frac{n!}{n_1! \cdots n_k!}$ |

### Permutations and combinations from the rules

*Theorem 1.* For $0 \le k \le n$, the number of $k$-permutations of $n$ different items is $P(n, k) = \frac{n!}{(n-k)!}$, and the number of $k$-combinations is $\binom{n}{k} = \frac{P(n, k)}{k!} = \frac{n!}{k!\,(n-k)!}$.

We know the product rule and the division rule. We want both counts. The plan is to build the lists in stages, and then forget the order with a $k!$-to-1 map.

*Proof.* A list of $k$ different items has $n$ choices for the first place, then $n - 1$ for the second, and so on down to $n - k + 1$ for the $k$-th, whichever items were chosen before. By the product rule, $P(n, k) = n(n-1)\cdots(n-k+1)$, and multiplying the top and bottom by $(n-k)!$ gives $\frac{n!}{(n-k)!}$.

Let $L$ be the set of these lists, and $C$ the set of $k$-element subsets. The function $g \colon L \to C$ that forgets the order, sending a list to the set of its entries, is $k!$-to-1: a subset with $k$ elements comes from exactly the $k!$ lists that arrange its elements, by the first half of the proof with $n = k$. By the division rule, $\lvert C \rvert = \frac{\lvert L \rvert}{k!}$. $\blacksquare$

Look back: the division rule explains the formula without any algebra. "Divide by $k!$" is the number of times each group appears among the lists. The symmetry $\binom{n}{k} = \binom{n}{n-k}$ also has a one-line counting proof: choosing the $k$ items to take matches choosing the $n - k$ items to leave, a bijection.

### Splitting into groups

*Theorem 2.* The number of ways to split $n$ different items into labelled groups of sizes $n_1, \dots, n_m$, with $n_1 + \cdots + n_m = n$, is $\frac{n!}{n_1!\, n_2! \cdots n_m!}$.

We know combinations and the product rule. We want a count for several groups at once. The plan is to fill the groups one at a time.

*Proof.* Choose the first group's members from the $n$ items: $\binom{n}{n_1}$ ways. Choose the second group from the $n - n_1$ that remain: $\binom{n - n_1}{n_2}$ ways, and so on. Whatever was chosen earlier, the number of ways at each stage is the same, so by the product rule the total is

$$
\binom{n}{n_1}\binom{n-n_1}{n_2}\cdots\binom{n_m}{n_m} = \frac{n!}{n_1!\,(n-n_1)!}\cdot\frac{(n-n_1)!}{n_2!\,(n-n_1-n_2)!}\cdots\frac{n_m!}{n_m!\,0!}.
$$

Each numerator after the first cancels the denominator before it, and what is left is $\frac{n!}{n_1!\, n_2! \cdots n_m!}$, since the last $0! = 1$. $\blacksquare$

Look back: the same number counts words with repeated letters. Replace the groups by letters: the $n_1$ places that hold the first letter, the $n_2$ places for the second, and so on. A word is a split of the $n$ positions into groups, one group for each letter, so the words match the splits. The words that can be made from the letters of MISSISSIPPI (one M, four I, four S, two P) number $\frac{11!}{1!\,4!\,4!\,2!} = 34{,}650$. You can also get the formula by the division rule: lining up the 11 letters as if they were different gives $11!$ lists, and each word comes from $1! \cdot 4! \cdot 4! \cdot 2!$ of them.

When the groups are not labelled, there is a further division. Splitting 8 people into two teams of 4 gives $\binom{8}{4} = 70$ ways if the teams are called Red and Blue. If the teams have no names, swapping the two teams gives the same split, so each split is counted twice and the answer is $\frac{70}{2} = 35$. In general, divide by $r!$ for each set of $r$ groups of the same size, since only groups of equal size can swap.

### Stars and bars

*Theorem 3 (stars and bars).* For integers $n \ge 0$ and $k \ge 1$, the number of solutions of

$$
x_1 + x_2 + \cdots + x_k = n
$$

in non-negative integers is $\binom{n+k-1}{k-1}$. This is also the number of multisets of size $n$ from $k$ types, and the number of ways to put $n$ identical objects into $k$ different boxes.

We know the bijection rule and combinations. We want to count solutions of an equation, and the equation has no obvious stages. The plan is to turn each solution into a string of stars and bars, and count the strings.

*Proof.* Take a solution $(x_1, \dots, x_k)$. Write $x_1$ stars, then a bar, then $x_2$ stars, then a bar, and so on, ending with $x_k$ stars with no bar after it. The string has $n$ stars and $k - 1$ bars, so its length is $n + k - 1$. For example, with $n = 5$ and $k = 4$ the solution $(2, 0, 3, 0)$ gives

```
**||***|
```

Every string of $n$ stars and $k - 1$ bars comes from exactly one solution, by reading $x_i$ as the number of stars between the $(i-1)$-th and $i$-th bar. So solutions match strings, by the bijection rule. A string is determined by the positions of its bars among the $n + k - 1$ positions, which can be chosen in $\binom{n+k-1}{k-1}$ ways. Since $\binom{n+k-1}{k-1} = \binom{n+k-1}{n}$, the count can also be read as choosing the places for the stars. $\blacksquare$

Look back: nothing in the proof depends on the stars being donuts. The bijection is the idea. Solutions also match multisets, because $x_i$ is the number of copies of type $i$ chosen, and match ways of filling boxes, because $x_i$ is the number of objects in box $i$.

Three variations come from changing the variables so that the equation looks like the one in the theorem.

1. Each $x_i \ge 1$. Put $y_i = x_i - 1 \ge 0$. Then $y_1 + \cdots + y_k = n - k$, which has $\binom{n-1}{k-1}$ solutions, and $x_i \mapsto y_i$ is a bijection between the two sets of solutions.
2. A bigger lower bound, such as $x_1 \ge 3$. Put $y_1 = x_1 - 3$ and leave the others, to get a total of $n - 3$.
3. $x_1 + \cdots + x_k \le n$. Add a slack variable $s = n - (x_1 + \cdots + x_k) \ge 0$. Then $x_1 + \cdots + x_k + s = n$ has $k + 1$ unknowns, so there are $\binom{n+k}{k}$ solutions.

Upper bounds, such as $x_i \le 3$, don't fit this method directly. They are handled with [inclusion-exclusion](04-inclusion-exclusion-and-pigeonhole.md).

### Circular arrangements

*Theorem 4.* For $n \ge 1$, the number of circular arrangements of $n$ different items is $(n-1)!$. If a flip of the circle also counts as the same arrangement, there are $\frac{(n-1)!}{2}$ of them for $n \ge 3$.

We know the division rule. We want to count arrangements up to rotation. The plan is to map lists to circular arrangements, show the map is $n$-to-1, and divide.

*Proof.* Let $L$ be the set of $n!$ lists of the items. Map each list to the circular arrangement it makes, which is its class of rotations. A list has $n$ rotations (shift by $0, 1, \dots, n-1$ places), and they are $n$ different lists because the items are different. So each circular arrangement comes from exactly $n$ lists, the map is $n$-to-1, and the number of arrangements is $\frac{n!}{n} = (n-1)!$.

If flips count too, each class of rotations is paired with its mirror image, and for $n \ge 3$ the mirror image is a different class (the neighbours of some item swap sides), so each arrangement comes from $2n$ lists and the count is $\frac{n!}{2n}$. $\blacksquare$

Look back: another way to see $(n-1)!$ is to fix one item in a seat, which uses up the rotations, and arrange the other $n - 1$ freely. For $n = 1$ and $n = 2$ the formula gives 1, and a flip changes nothing, so the second count starts at $n = 3$. If the seats are labelled, say numbered chairs, then a rotation is a different seating and the count is $n!$.

## Worked examples

<div class="example" markdown>

### Example 1: poker hands

A 5-card hand from a 52-card deck is a 5-element subset, so there are $\binom{52}{5} = 2{,}598{,}960$ hands. Count the hands that are (a) a full house and (b) two pair, meaning two cards of one rank, two of another rank and one card of a third rank.

Step 1: a full house is a set of 5 cards. Step 2 and 3: the order doesn't matter and cards can't repeat, so build the hand from choices of ranks and suits, and let each choice be a combination. Step 4: the stages for a full house are the rank of the triple (13), its 3 suits ($\binom{4}{3} = 4$), the rank of the pair (12 ranks left), and its 2 suits ($\binom{4}{2} = 6$):

$$
13 \cdot 4 \cdot 12 \cdot 6 = 3{,}744.
$$

The roles matter here: a triple of kings and a pair of fives is a different hand from a triple of fives and a pair of kings, which is why the two ranks are chosen one after the other and not as a pair of ranks. For (b), the two ranks of the pairs are interchangeable, so they are chosen as a set: $\binom{13}{2}$ ways. Each pair has $\binom{4}{2}$ suit choices, and the fifth card is any of the $52 - 8 = 44$ cards of the other 11 ranks:

$$
\binom{13}{2}\binom{4}{2}^2 \cdot 44 = 78 \cdot 36 \cdot 44 = 123{,}552.
$$

Step 5, the check: a program that goes through all 2,598,960 hands and sorts them by the pattern of their rank counts finds 3,744 full houses and 123,552 two-pair hands. The chance of a full house is $\frac{3744}{2598960} \approx 0.00144$, about 1 in 694.

</div>

<div class="example" markdown>

### Example 2: donuts in boxes

(a) In how many ways can 10 identical donuts go into 4 labelled boxes? (b) If every box must get at least one? (c) If box 1 must get at least 3?

(a) This is the number of non-negative solutions of $x_1 + x_2 + x_3 + x_4 = 10$, so $n = 10$ and $k = 4$, and Theorem 3 gives $\binom{13}{3} = 286$.

(b) Put $y_i = x_i - 1$, so $y_1 + \cdots + y_4 = 6$ with $y_i \ge 0$. That has $\binom{6+3}{3} = \binom{9}{3} = 84$ solutions.

(c) Put $y_1 = x_1 - 3$, so $y_1 + x_2 + x_3 + x_4 = 7$, which has $\binom{7+3}{3} = \binom{10}{3} = 120$ solutions.

Check: listing all solutions of the equation by brute force gives 286, 84 and 120. For (c), the solutions that break the condition have $x_1 \in \{0, 1, 2\}$, and the other three variables then add to 10, 9 or 8, which gives $\binom{12}{2} + \binom{11}{2} + \binom{10}{2} = 66 + 55 + 45 = 166$ of them. Then $286 - 166 = 120$, as before.

</div>

<div class="example" markdown>

### Example 3: MISSISSIPPI

(a) How many different words can be made from all the letters of MISSISSIPPI? (b) How many have no two I's next to each other?

(a) The word has 11 letters: one M, four I, four S and two P. By Theorem 2, $\frac{11!}{1!\,4!\,4!\,2!} = \frac{39{,}916{,}800}{1152} = 34{,}650$.

(b) Place the 7 letters that are not I first: M, four S and two P can be arranged in $\frac{7!}{1!\,4!\,2!} = 105$ ways. These 7 letters leave 8 gaps, counting the two ends, and no two I's are adjacent exactly when the four I's go into four different gaps. Choose the gaps: $\binom{8}{4} = 70$ ways, and the I's are alike, so nothing else is chosen. By the product rule, $105 \cdot 70 = 7{,}350$.

Check: a program that generates all 34,650 words and removes those containing II finds 7,350. Also, the words that start with M number $\frac{10!}{4!\,4!\,2!} = 3{,}150$, and $\frac{3150}{34650} = \frac{1}{11}$ is the fraction of the letters that are M, as symmetry says it should be.

</div>

<div class="example" markdown>

### Example 4: a round table

Six different people sit at a round table, with rotations counted as the same. (a) How many seatings? (b) How many have Ana and Ben not next to each other? (c) How many if reflections also count as the same?

(a) By Theorem 4, $(6-1)! = 120$.

(b) Count the complement. Glue Ana and Ben into one block. The block and the other 4 people make 5 objects around the table, which gives $(5-1)! = 24$ circular arrangements, and Ana and Ben can swap inside the block, a factor of 2: $48$ seatings with them adjacent. So $120 - 48 = 72$ have them apart.

(c) With reflections also identified, $\frac{120}{2} = 60$.

Check: a program that generates all 720 lists and keeps one list from each class of rotations finds 120 classes, 72 of them with Ana and Ben apart, and 60 classes when mirror images are merged too.

</div>

<div class="example" markdown>

### Example 5: finish it yourself

Ten people are split into two teams of 5, and then into groups of sizes 3, 3 and 4. The teams and groups have no names. How many ways are there for each split?

The labelled counts are $\frac{10!}{5!\,5!} = 252$ for the two teams, and $\frac{10!}{3!\,3!\,4!} = 4{,}200$ for the three groups, by Theorem 2. Now correct for the groups having no labels.

<details class="solution" markdown>
<summary>Finish</summary>

For the two teams, swapping the labels gives the same split, so the map from labelled splits to unlabelled splits is 2-to-1: $\frac{252}{2} = 126$.

For the groups of 3, 3 and 4, only the two groups of size 3 can swap, so the map is 2-to-1 and the answer is $\frac{4200}{2} = 2{,}100$. The group of 4 can't swap with anything, so it needs no division.

Check on a smaller case: 8 people into two unlabelled teams of 4 gives $\frac{70}{2} = 35$, and listing all splits of $\{1, \dots, 8\}$ into two sets of 4 by brute force also gives 35.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out at step 3: repetition with no order is not $\binom{n}{k}$. Three scoops from 5 flavours, with repeats allowed, is $\binom{5+3-1}{3} = 35$, and $\binom{5}{3} = 10$ counts only the choices with three different flavours. If an outcome can have two scoops of the same flavour, use stars and bars.

</div>

<div class="warning" markdown>

Watch out when you use stars and bars: the number of bars is one less than the number of boxes. Ten donuts in 4 boxes has $10$ stars and $3$ bars in $13$ places, giving $\binom{13}{3} = 286$. Using 4 bars, one per box, gives $\binom{14}{4} = 1001$, which is wrong.

</div>

<div class="warning" markdown>

Watch out when the groups are not labelled: after the multinomial count, divide by $r!$ for each set of $r$ groups of equal size, and by nothing for a group of a size of its own. Forgetting the division counts each split twice, and dividing by $2!$ when the sizes are 3 and 4 divides too much.

</div>

<div class="warning" markdown>

Watch out for circles: $(n-1)!$ assumes that only the neighbours matter. At a table with numbered chairs, or when one seat is the head, a rotation is a different seating and the count is $n!$. Use the reflection count $\frac{(n-1)!}{2}$ only when a flip of the circle is meant to count as the same, as for beads on a bracelet, which can be turned over.

</div>

Some small cases. $\binom{n}{0} = 1$ and $P(n, 0) = 1$, the one empty selection. Stars and bars with $n = 0$ has the one solution of all zeros, and with $k = 1$ it has one solution, $x_1 = n$. A selection of more items than exist, $k > n$ without repeats, has 0 choices, but with repeats allowed it is fine: 7 scoops from 2 flavours is $\binom{8}{7} = 8$. A circular arrangement of 1 item is 1 seating.

## Tricks and shortcuts

When some items must be kept apart, place the free items first and put the restricted ones into the gaps. Five men and four women in a row, no two women adjacent: arrange the 5 men ($5!$), which leaves 6 gaps, and choose and order the places for the women ($P(6, 4)$). When items must be together, glue them into one block, count the blocks, and multiply by the orders inside.

Label first, divide after. If objects that are alike are counted as if they were different, the count is too big by the number of ways to relabel the alike ones, which is the same for every outcome. This is how the multinomial and circular counts arise, and it works for any problem in which every outcome appears equally often.

To check a stars-and-bars number, count the string positions: $n$ stars plus $k - 1$ bars, and choose the $k - 1$ bar positions. A quick test is $n = 1$: one object in $k$ boxes has $k$ ways, and $\binom{k}{k-1} = k$.

Compute $\binom{n}{k}$ without large factorials by cancelling, $\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!}$, and use $\binom{n}{k} = \binom{n}{n-k}$ to keep $k$ small.

## In code

Python's `math.perm` and `math.comb` give the counts, and `itertools` lists the objects so that each formula can be checked by brute force.

<details class="code" markdown>
<summary>In code</summary>

```python
from collections import Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, factorial, perm

n, k = 5, 3
print(n**k, perm(n, k), comb(n, k), comb(n + k - 1, k))        # 125 60 10 35
print(len(list(product(range(n), repeat=k))),
      len(list(permutations(range(n), k))),
      len(list(combinations(range(n), k))),
      len(list(combinations_with_replacement(range(n), k))))   # 125 60 10 35

# Stars and bars: solutions of x1 + x2 + x3 + x4 = 10.
sols = [x for x in product(range(11), repeat=4) if sum(x) == 10]
print(len(sols), comb(13, 3))                                  # 286 286
print(sum(1 for x in sols if min(x) >= 1), comb(9, 3))         # 84 84
print(sum(1 for x in sols if x[0] >= 3), comb(10, 3))          # 120 120

# Arrangements of MISSISSIPPI, with and without adjacent I's.
def arrangements(counts):
    if sum(counts.values()) == 0:
        yield ""
        return
    for ch in list(counts):
        if counts[ch] > 0:
            counts[ch] -= 1
            for rest in arrangements(counts):
                yield ch + rest
            counts[ch] += 1

words = list(arrangements(Counter("MISSISSIPPI")))
print(len(words), factorial(11) // (factorial(4) * factorial(4) * factorial(2)))   # 34650 34650
print(sum(1 for w in words if "II" not in w),
      factorial(7) // (factorial(4) * factorial(2)) * comb(8, 4))                  # 7350 7350

# Round table of 6 people, labelled 0 to 5: rotations the same.
def rotate_first(p):
    i = p.index(0)
    return p[i:] + p[:i]

tables = {rotate_first(p) for p in permutations(range(6))}
print(len(tables), factorial(5))                                                   # 120 120
def neighbours(p, a, b):
    i = p.index(a)
    return p[(i + 1) % 6] == b or p[(i - 1) % 6] == b
print(sum(1 for t in tables if not neighbours(t, 0, 1)), factorial(5) - 2 * factorial(4))   # 72 72

# Full houses and two pairs among all 5-card hands (13 ranks, 4 suits).
deck = [(r, s) for r in range(13) for s in range(4)]
patterns = Counter(tuple(sorted(Counter(r for r, s in h).values(), reverse=True))
                   for h in combinations(deck, 5))
print(patterns[(3, 2)], 13 * 4 * 12 * 6)                                           # 3744 3744
print(patterns[(2, 2, 1)], comb(13, 2) * comb(4, 2) ** 2 * 44)                     # 123552 123552
```

The last block goes through 2,598,960 hands and takes a few seconds. Each pair of numbers is the count from the list followed by the count from the formula, and they agree.

</details>

## FAQ

### Why is the number of bars $k - 1$ and not $k$?

Bars are dividers between boxes, and $k$ boxes in a row have $k - 1$ walls between neighbours. The stars before the first bar are box 1, the stars after the last bar are box $k$. With 2 boxes, one bar splits the stars into two groups.

### Why divide by $n$ for a round table, and not by something else?

The division rule needs every circular arrangement to come from the same number of lists, and a list of $n$ different items has $n$ different rotations, whichever list it is. That fixed number is $n$. If some items were alike, a list could equal one of its own rotations, and the number of lists per arrangement would no longer be the same for every arrangement, so the simple division would fail. Counting beads of two colours around a ring needs a different method.

### Why do the labelled groups need no extra division but unlabelled groups do?

Labelled groups are told apart by their names, so swapping the contents of two groups gives a different outcome, and the multinomial count already treats it as one. Unlabelled groups of the same size can swap contents without changing the split, and each split then appears once for each way of permuting the equal groups.

### How can I tell whether order matters?

Write down one outcome, swap two of the chosen items, and ask whether you have the same outcome. A committee with Ana and Ben is the same as one with Ben and Ana, and a podium with Ana first and Ben second is not the same as the reverse. When unsure, a two-element version of the problem is small enough to list.

## Practice

### Warm-up

1\. Compute (a) $P(9, 4)$, (b) $\binom{9}{4}$, (c) the number of multisets of size 4 from 9 types, and (d) the number of 4-letter strings from 9 letters, repeats allowed.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $9 \cdot 8 \cdot 7 \cdot 6 = 3{,}024$. (b) $\frac{3024}{24} = 126$. (c) $\binom{9+4-1}{4} = \binom{12}{4} = 495$. (d) $9^4 = 6{,}561$.

Check: ignoring the order of 4 different items divides by $4! = 24$, and $\frac{3024}{24} = 126$. Allowing order or repeats can only add outcomes, so $126$ is the smallest of the four and $6{,}561$ the largest.

</details>

2\. How many different words can be made from the letters of COMMITTEE?

<details class="solution" markdown>
<summary>Solution</summary>

The word has 9 letters: C, O, I once each, and M, T, E twice each. By Theorem 2, $\frac{9!}{2!\,2!\,2!} = \frac{362{,}880}{8} = 45{,}360$.

Check: for the smaller word MOON, the formula gives $\frac{4!}{2!} = 12$, and listing the words gives 12.

</details>

3\. How many non-negative integer solutions does $x_1 + x_2 + x_3 = 7$ have? How many have every $x_i \ge 1$?

<details class="solution" markdown>
<summary>Solution</summary>

With $n = 7$ and $k = 3$, there are $\binom{9}{2} = 36$ solutions. For $x_i \ge 1$, put $y_i = x_i - 1$ so that $y_1 + y_2 + y_3 = 4$, which has $\binom{6}{2} = 15$ solutions.

Check by listing the positive solutions by the value of $x_1$: for $x_1 = 1, 2, 3, 4, 5$ the other two add to $6, 5, 4, 3, 2$ and have $5, 4, 3, 2, 1$ solutions, and $5 + 4 + 3 + 2 + 1 = 15$.

</details>

### Standard

4\. How many 5-card hands have three of a kind, that is, three cards of one rank and two cards of two other different ranks?

<details class="solution" markdown>
<summary>Solution</summary>

Choose the rank of the triple (13) and its suits ($\binom{4}{3} = 4$). Choose the two other ranks as a set, since their roles are the same: $\binom{12}{2} = 66$. Each of those two ranks contributes one card, with 4 suit choices each: $4 \cdot 4 = 16$. The total is $13 \cdot 4 \cdot 66 \cdot 16 = 54{,}912$.

Check: the pattern count over all hands, as in the code block above, gives 54,912 for the rank pattern $(3, 1, 1)$.

</details>

5\. A school has 8 identical laptops to share among 3 labs, and every lab must get at least 2. In how many ways can it do this?

<details class="solution" markdown>
<summary>Solution</summary>

Let $x_i \ge 2$ be the number for lab $i$, with $x_1 + x_2 + x_3 = 8$. Put $y_i = x_i - 2 \ge 0$, so that $y_1 + y_2 + y_3 = 2$. By stars and bars there are $\binom{2+2}{2} = 6$ solutions.

Check by listing: the numbers are $2, 2, 4$ in 3 orders and $2, 3, 3$ in 3 orders, which is 6 in all.

</details>

6\. Five men and four women stand in a row. In how many ways can they stand so that no two women are next to each other?

<details class="solution" markdown>
<summary>Solution</summary>

Line up the 5 men first, in $5! = 120$ ways. They leave 6 gaps, including the two ends. The four women go into 4 different gaps, and since the women are different and the order of the women matters, the number of ways is $P(6, 4) = 6 \cdot 5 \cdot 4 \cdot 3 = 360$. By the product rule, $120 \cdot 360 = 43{,}200$.

Check: brute force over all $9! = 362{,}880$ rows, counting those with no two women adjacent, gives 43,200.

</details>

### Challenge

7\. Prove directly that the number of multisets of size $k$ from the types $1, 2, \dots, n$ is $\binom{n+k-1}{k}$, with a bijection to the $k$-element subsets of $\{1, 2, \dots, n+k-1\}$.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: a multiset of size $k$ can be listed in non-decreasing order, $a_1 \le a_2 \le \cdots \le a_k$, with each $a_i \in \{1, \dots, n\}$. What we want: a matching with subsets. The plan is to add $0, 1, 2, \dots$ to the entries to make them all different.

*Proof.* Map $a_1 \le \cdots \le a_k$ to the set $\{a_1, a_2 + 1, a_3 + 2, \dots, a_k + (k - 1)\}$. The entries are strictly increasing, because $a_{i+1} + i \ge a_i + i > a_i + (i - 1)$, so the set has $k$ different elements, and the largest is at most $n + k - 1$. The map has an inverse: list a $k$-element subset of $\{1, \dots, n + k - 1\}$ in increasing order as $b_1 < \cdots < b_k$ and subtract $0, 1, \dots, k-1$, giving $b_i - (i - 1)$, which is non-decreasing and lies between 1 and $n$. So the map is a bijection, and the number of multisets is $\binom{n+k-1}{k}$. $\blacksquare$

Check with $n = 3$ and $k = 2$: the multisets $11, 12, 13, 22, 23, 33$ map to $\{1, 2\}, \{1, 3\}, \{1, 4\}, \{2, 3\}, \{2, 4\}, \{3, 4\}$, the six 2-element subsets of $\{1, 2, 3, 4\}$, and $\binom{4}{2} = 6$.

</details>

8\. (Reviews [counting rules](01-counting-rules.md).) Six people are split into 3 pairs, with the pairs unlabelled. (a) Count the splits by choosing the pairs one after another and dividing. (b) Count them again by pairing the first person first. (c) Explain why the two answers agree.

<details class="solution" markdown>
<summary>Solution</summary>

(a) Labelled pairs: $\frac{6!}{2!\,2!\,2!} = 90$. The three pairs all have the same size, so swapping them gives the same split, and the map from labelled to unlabelled splits is $3!$-to-1: $\frac{90}{6} = 15$.

(b) Person 1 has 5 possible partners. Of the 4 people left, the lowest-numbered one has 3 possible partners, and the last two form a pair: $5 \cdot 3 \cdot 1 = 15$.

(c) Method (b) breaks the symmetry, by always pairing the lowest-numbered person who is still free, so each split is built in exactly one order, and the product rule gives the count with no division. Method (a) builds each split in $3!$ orders, and the division rule removes them.

Check: for 4 people the same two methods give $\frac{4!}{2!\,2!\,2!} = 3$ and $3 \cdot 1 = 3$, and the splits of $\{1, 2, 3, 4\}$ are $12|34$, $13|24$ and $14|23$.

</details>

## Where this shows up

- The next lesson, [the binomial theorem and combinatorial proofs](03-binomial-theorem-and-combinatorial-proofs.md), proves identities by counting one set in two ways, using these counts as the two sides. The multinomial coefficient of Theorem 2 gives the multinomial theorem there.
- In machine learning and algebra, the number of monomials of degree $d$ in $n$ variables is the number of multisets of size $d$ from $n$ types, $\binom{n+d-1}{d}$. In algorithms, $\binom{n}{k}$ is the number of subsets a brute-force search tries, and the stars-and-bars count is the number of ways to split a total workload into $k$ parts.
- In economics, the number of different baskets of $n$ units spread over $k$ goods is $\binom{n+k-1}{k-1}$, so a small budget over a few goods already has many baskets. In probability, a lottery or a card hand is a ratio of two such counts ([discrete probability](05-discrete-probability.md)).
