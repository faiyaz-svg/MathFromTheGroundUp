# Counting: permutations and combinations

After this lesson you can count outcomes with the sum and product rules, count ordered and unordered selections with $P(n, k)$ and $\binom{n}{k}$, count arrangements with repeated letters, handle restrictions by counting the complement, and use counts to find probabilities such as the odds in Lotto 6/49.

Before this: [basic probability](../../02-middle-school/07-statistics-and-probability/02-basic-probability.md), [real numbers, axioms and set notation](../01-algebra-foundations/01-real-numbers-axioms-and-set-notation.md) and [summation notation and series](02-summation-notation-and-series.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A menu has 4 mains, 3 sides and 2 drinks. How many meals have one of each?
2. A club of 8 people elects a president, a vice-president and a treasurer (three different people). In how many ways can it do this? In how many ways can it instead choose a committee of 3?
3. A 4-digit PIN uses the digits 0 to 9, and repeats are allowed. What is the probability that a random PIN has four different digits?

<details class="solution" markdown>
<summary>Answers</summary>

1. Choose a main, then a side, then a drink: $4 \cdot 3 \cdot 2 = 24$ meals.
2. For the three offices there are 8 choices for the president, then 7 for the vice-president, then 6 for the treasurer: $8 \cdot 7 \cdot 6 = 336$. A committee has no offices, so each group of 3 was counted $3 \cdot 2 \cdot 1 = 6$ times above: $336 \div 6 = 56$.
3. There are $10^4 = 10{,}000$ PINs. With four different digits there are $10 \cdot 9 \cdot 8 \cdot 7 = 5040$ of them, so the probability is $\frac{5040}{10000} = 0.504$.

</details>

## The idea

How many 4-digit PINs are there? Nobody lists them. A PIN is built in four stages, and each stage is a free choice of one of 10 digits, so there are $10 \cdot 10 \cdot 10 \cdot 10 = 10{,}000$. That is the main idea of counting: split the thing you are building into stages, and multiply the number of choices at each stage. The second idea is the opposite one. If the task can be done in two different ways with nothing in common, you add the two counts.

The Lotto 6/49 draw asks a different question. You pick 6 numbers from 1 to 49, and the order you write them in doesn't matter: a ticket with 3, 17, 22, 30, 41, 48 is the same ticket however you list those numbers. Building the ticket in stages gives $49 \cdot 48 \cdot 47 \cdot 46 \cdot 45 \cdot 44$ lists, but every ticket appears in many lists, once for each order of its six numbers. The count of tickets is the count of lists divided by the number of orders. The whole lesson comes back to one question: does order matter? If it does, you count lists. If it doesn't, you count lists and divide out the orders.

## Definitions

For a finite set $A$, the number of elements in $A$ is written $\lvert A \rvert$. So $\lvert \{a, b, c\} \rvert = 3$.

**The sum rule.** If $A_1, A_2, \dots, A_m$ are finite sets with no element in more than one of them, then the number of elements in the union is the sum of the sizes:

$$
\lvert A_1 \cup A_2 \cup \cdots \cup A_m \rvert = \lvert A_1 \rvert + \lvert A_2 \rvert + \cdots + \lvert A_m \rvert.
$$

In plain words, if a task can be done in one of several ways, and no outcome comes from two of the ways, add the counts. A student who picks one elective from 6 CS courses or from 4 economics courses has $6 + 4 = 10$ choices, as long as no course is on both lists. If the lists overlap, the overlap is counted twice and has to be subtracted, which is the subject of [inclusion-exclusion and the pigeonhole principle](../../06-cs-math/03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md).

**The product rule.** Suppose a procedure has $k$ stages, and stage $i$ can be done in $n_i$ ways, whatever happened at the earlier stages. Then the whole procedure can be done in

$$
n_1 \cdot n_2 \cdots n_k
$$

ways. In plain words, "and" means multiply. The wording "whatever happened earlier" matters: the options available at stage 2 may depend on what you chose at stage 1, but their number must not. The set version is $\lvert A_1 \times \cdots \times A_k \rvert = \lvert A_1 \rvert \cdots \lvert A_k \rvert$.

Two consequences come up constantly. A list of length $k$ made from $n$ symbols, with repeats allowed, can be built in $k$ stages with $n$ choices each, so there are $n^k$ such lists. And a set with $n$ elements has $2^n$ subsets, because each element is either in the subset or out of it: $2 \cdot 2 \cdots 2$ with $n$ factors. For $n = 3$ the eight subsets of $\{a, b, c\}$ are the empty set, three single elements, three pairs and the whole set.

The **factorial** of a whole number $n \ge 1$ is the product of the whole numbers from 1 to $n$, and $0!$ is defined to be 1:

$$
n! = n(n-1)(n-2) \cdots 2 \cdot 1, \qquad 0! = 1.
$$

In plain words, $n!$ is the number of ways to line up $n$ different things (see below), and $5! = 120$. It satisfies the recurrence $n! = n \cdot (n-1)!$ for $n \ge 1$, which is how the convention $0! = 1$ is forced: $1! = 1 \cdot 0!$ only works if $0! = 1$. It also matches the empty product from [summation notation and series](02-summation-notation-and-series.md), a product with no factors being 1.

A **permutation** of $k$ items chosen from $n$ different items is an ordered list of $k$ different items from the $n$. The number of them is written $P(n, k)$, for integers $0 \le k \le n$. Some books write $_nP_k$. A permutation of all $n$ items is an arrangement, an ordering, of the whole set. In plain words, permutations count selections where the order matters, such as gold, silver and bronze in a race.

A **combination** of $k$ items chosen from $n$ different items is a subset with $k$ elements, so the order is ignored. The number of them is the **binomial coefficient** $\binom{n}{k}$, read "$n$ choose $k$" (also written $C(n, k)$ or $_nC_k$). By convention $\binom{n}{k} = 0$ when $k > n$, since there is no way to choose more items than exist. In plain words, a combination is a selection where the order doesn't matter, such as the members of a committee.

## How to do it

### Choosing the tool

1. Say what you are counting in a sentence, and what one outcome looks like ("a list of 3 different people", "a set of 6 numbers").
2. Does order matter? If swapping two of the chosen items gives a different outcome (a PIN, a race result), order matters. If it gives the same outcome (a committee, a ticket), it doesn't.
3. Can items repeat? A PIN can use the digit 7 twice. A committee can't use the same person twice.
4. Pick the count from the table, or split the task into stages (multiply) or cases (add).
5. If the condition is awkward ("at least one", "not next to each other"), count all outcomes and subtract the ones that break the condition, or count the complement.
6. Check: test the method on a tiny version you can list by hand, or compare with a second way of counting.

| Order matters? | Repeats allowed? | Count | Example |
|---|---|---|---|
| yes | yes | $n^k$ | PINs, bit strings |
| yes | no | $P(n, k) = \frac{n!}{(n-k)!}$ | race results, officers |
| no | no | $\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$ | committees, lottery tickets |
| no | yes | $\binom{n+k-1}{k}$ | scoops of ice cream |

The fourth row is stated without proof here; it is the "stars and bars" count of [counting rules](../../06-cs-math/03-counting-and-discrete-probability/01-counting-rules.md). For example, 3 scoops chosen from 5 flavours, repeats allowed and order ignored, can be done in $\binom{7}{3} = 35$ ways.

### Permutations

*Theorem.* For integers $0 \le k \le n$,

$$
P(n, k) = n(n-1)(n-2)\cdots(n-k+1) = \frac{n!}{(n-k)!}.
$$

We know the product rule. We want the number of ordered lists of $k$ different items from $n$. The plan is to build the list one position at a time.

*Proof.* The first position can hold any of the $n$ items. Once it is filled, $n - 1$ items remain for the second position, then $n - 2$ for the third, and the position numbered $k$ has $n - k + 1$ choices. Which items remain depends on what was chosen, but how many remain doesn't, so the product rule gives $n(n-1)\cdots(n-k+1)$. Multiplying the top and bottom by $(n-k)!$ turns this into $\frac{n!}{(n-k)!}$, because $(n-k)! = (n-k)(n-k-1)\cdots 1$ is the part of $n!$ that is missing. $\blacksquare$

Look back: with $k = n$ this says that $n$ items can be lined up in $P(n, n) = n!$ ways, which is the plain-words claim about factorials above. With $k = 0$ it says $P(n, 0) = 1$: there is exactly one list of no items, the empty list.

### Combinations

*Theorem.* For integers $0 \le k \le n$,

$$
\binom{n}{k} = \frac{n!}{k!\,(n-k)!} = \frac{P(n, k)}{k!}.
$$

We know $P(n, k)$ and that $k$ items can be ordered in $k!$ ways. We want the number of subsets of size $k$. The plan is to count the ordered lists of $k$ items in two ways, and compare.

*Proof.* Let $L$ be the set of ordered lists of $k$ different items from the $n$ items. By the previous theorem, $\lvert L \rvert = P(n, k)$.

Count $L$ a second way. First choose which $k$ items appear, which is a $k$-element subset: $\binom{n}{k}$ ways. Then put those $k$ items in some order: $k!$ ways, by the previous theorem with $n = k$. Different choices of subset or order give different lists, and every list arises this way. By the product rule, $\lvert L \rvert = \binom{n}{k} \cdot k!$.

The two counts are equal: $P(n, k) = \binom{n}{k} \cdot k!$. Dividing by $k!$ gives $\binom{n}{k} = \frac{P(n, k)}{k!} = \frac{n!}{k!\,(n-k)!}$. $\blacksquare$

Look back: this is why "divide by $k!$" removes the order. Each subset appears in the list of ordered selections exactly $k!$ times, once for each way of arranging its members, so dividing the number of lists by $k!$ counts each subset once. The same argument counts anything where every outcome is counted the same number of times too often.

Two facts follow at once from the formula and are worth knowing by heart. First, $\binom{n}{0} = \binom{n}{n} = 1$ and $\binom{n}{1} = n$. Second, the symmetry $\binom{n}{k} = \binom{n}{n-k}$: the formula is unchanged when $k$ and $n - k$ swap places, and in words, choosing the $k$ items to take is the same as choosing the $n - k$ items to leave. The symmetry lets you swap a large $k$ for a small one, so $\binom{100}{98} = \binom{100}{2} = 4950$ is far easier to compute than it looks.

### Arrangements with repeated letters

*Theorem.* A word of $n$ letters in which the first kind of letter appears $n_1$ times, the second $n_2$ times, and so on up to $n_m$ times, with $n_1 + \cdots + n_m = n$, can be rearranged into

$$
\frac{n!}{n_1!\, n_2! \cdots n_m!}
$$

different words.

We know that $n$ different items can be lined up in $n!$ ways. We want to count the words when some letters are copies of each other. The plan is to pretend the copies are different, and then correct for the pretence.

*Proof.* Give the copies of each repeated letter subscripts, as in $\text{A}_1, \text{A}_2, \text{A}_3$, so that all $n$ letters are different. There are $n!$ arrangements of the labelled letters. Take one actual word, say BANANA. Its labelled versions come from putting the subscripts back on, and the three A's can be labelled in $3!$ orders, the two N's in $2!$ orders, and the single B in $1!$ order. By the product rule, each word has $n_1!\, n_2! \cdots n_m!$ labelled versions, and each labelled arrangement gives exactly one word. So $n! = N \cdot n_1!\, n_2! \cdots n_m!$, where $N$ is the number of words, and dividing gives the formula. $\blacksquare$

Look back: this is the same "count too many, then divide" argument as for combinations. In fact $\binom{n}{k}$ is the case with two kinds of letter: a word of $k$ ones and $n - k$ zeros is a subset of size $k$ (the positions of the ones), and the theorem gives $\frac{n!}{k!\,(n-k)!}$ again.

### Restrictions and the complement

Many problems have a condition that makes direct counting messy. Three tools handle most of them.

1. Subtract the complement. The number of outcomes with a property is the total number of outcomes minus the number without it. "At least one" is the standard case: the complement of "at least one" is "none".
2. Fill the restricted position first. To count 3-digit even numbers with all digits different, choose the last digit first (it must be one of 0, 2, 4, 6, 8) and then the others, taking care of 0 in the leading position.
3. Glue items that must be together. If two people must sit next to each other, treat them as one block, arrange the blocks, and multiply by the orders inside the block.

### Passwords, PINs and bits

A secret chosen uniformly at random from $N$ equally likely possibilities has $\log_2 N$ **bits of entropy**: each bit doubles the number of guesses an attacker needs. A random 4-digit PIN has $N = 10^4$ and about 13.3 bits. A random 6-letter lowercase password has $26^6 = 308{,}915{,}776$ possibilities and about 28.2 bits, and a random 8-character password from the 62 letters and digits has $62^8 = 218{,}340{,}105{,}584{,}896$ possibilities, about $2.18 \times 10^{14}$, and 47.6 bits. These numbers assume every possibility is equally likely, which is true of passwords from a generator and false of passwords people choose, since people pick a few popular PINs and words far more often than the rest. The lesson on [logarithms](../07-exponentials-and-logarithms/02-logarithms.md) explains $\log_2$, and [bits and information](../../06-cs-math/01-number-representation/02-bits-and-information.md) gives entropy a precise meaning.

### Counting and probability

When all the outcomes of an experiment are equally likely, the probability of an event is a ratio of two counts, as in [basic probability](../../02-middle-school/07-statistics-and-probability/02-basic-probability.md):

$$
P(A) = \frac{\lvert A \rvert}{\lvert S \rvert}.
$$

This lesson supplies the tools to find $\lvert A \rvert$ and $\lvert S \rvert$ when they are too big to list. The step to check is that both counts use the same view of the outcomes. If $S$ counts ordered lists, then $A$ must count ordered lists too, and if $S$ counts subsets, $A$ must count subsets. Mixing the two is a common source of wrong answers.

## Worked examples

<div class="example" markdown>

### Example 1: a podium and a team

Eight runners are in a race. (a) In how many ways can gold, silver and bronze be awarded? (b) In how many ways can the three medallists be chosen as a group, ignoring who got which medal?

Step 1: one outcome in (a) is a list of three different runners, with the first getting gold. In (b) it is a set of three runners.

Step 2: in (a) order matters, because swapping gold and silver changes the result. In (b) it doesn't.

Step 3: runners can't repeat, since one runner can't win two medals.

Step 4 and 5: (a) uses $P(8, 3)$. The count is $8 \cdot 7 \cdot 6 = 336$: 8 runners for gold, 7 left for silver, 6 left for bronze. (b) uses $\binom{8}{3} = \frac{P(8, 3)}{3!} = \frac{336}{6} = 56$.

Step 6: check that the two answers fit together. Every group of 3 medallists can be ordered in $3! = 6$ ways, so the number of podiums should be 6 times the number of groups, and $6 \cdot 56 = 336$. The factorial formula agrees: $\frac{8!}{3!\,5!} = \frac{40320}{6 \cdot 120} = 56$.

</div>

<div class="example" markdown>

### Example 2: a committee with a condition

A committee of 4 is chosen from 10 students, 6 in CS and 4 in economics. How many committees are there (a) in total, (b) with at least one economics student, (c) with exactly two from each program? (d) If the committee is chosen at random, what is the probability that it has at least one economics student?

The committee is a set, so order doesn't matter, and nobody repeats: combinations.

(a) $\binom{10}{4} = \frac{10 \cdot 9 \cdot 8 \cdot 7}{4 \cdot 3 \cdot 2 \cdot 1} = 210$.

(b) The complement of "at least one economics student" is "all four are CS students": $\binom{6}{4} = \binom{6}{2} = 15$. So the answer is $210 - 15 = 195$.

(c) Choose two of the 6 CS students and two of the 4 economics students, and multiply: $\binom{6}{2}\binom{4}{2} = 15 \cdot 6 = 90$.

(d) All 210 committees are equally likely, so the probability is $\frac{195}{210} = \frac{13}{14} \approx 0.929$.

Check by adding the cases for the number of economics students: 0 gives $\binom{6}{4} = 15$, 1 gives $\binom{4}{1}\binom{6}{3} = 4 \cdot 20 = 80$, 2 gives 90, 3 gives $\binom{4}{3}\binom{6}{1} = 24$, and 4 gives 1. These add up to $15 + 80 + 90 + 24 + 1 = 210$, the total in (a), and the cases with at least one economics student add up to $80 + 90 + 24 + 1 = 195$, matching (b).

</div>

<div class="example" markdown>

### Example 3: repeated letters, and people who must sit together

(a) How many different words can be made from all the letters of BANANA? (b) How many of them start with B? (c) Five people stand in a row. Ana and Ben insist on standing next to each other. How many ways are there, and how many ways with Ana and Ben not next to each other?

(a) The word has 6 letters: three A's, two N's and one B. By the repeated-letters formula, $\frac{6!}{3!\,2!\,1!} = \frac{720}{12} = 60$.

(b) Put B first. The other five letters, AANAN, have three A's and two N's: $\frac{5!}{3!\,2!} = 10$.

(c) Glue Ana and Ben into one block. Now there are 4 objects (the block and three other people), which can be lined up in $4! = 24$ ways. Inside the block Ana and Ben can swap, a factor of 2, so $4! \cdot 2 = 48$ ways. Without any condition there are $5! = 120$ lines, so the number with Ana and Ben apart is the complement, $120 - 48 = 72$.

Check (a) and (c) with the smaller cases that can be listed by hand. For the word AAB the formula gives $\frac{3!}{2!\,1!} = 3$ words: AAB, ABA, BAA. For three people with Ana and Ben together, the block method gives $2! \cdot 2 = 4$, and listing confirms it: ABC, BAC, CAB, CBA, where C is the third person.

</div>

<div class="example" markdown>

### Example 4: Lotto 6/49 (finish it yourself)

In Lotto 6/49 the draw picks 6 numbers from 1 to 49. According to OLG's [lottery odds page](https://www.playsmart.ca/lottery-instant-games/lottery/odds/) (checked October 2026), the odds of winning the classic jackpot with one play are 1 in 13,983,816. Check that figure, and find the probability that a ticket matches exactly 3 of the 6 drawn numbers. (The lottery also has a bonus number and a separate Gold Ball draw, which affect other prizes; ignore them here.)

A ticket is a set of 6 numbers, so order doesn't matter, and the numbers are different: combinations. The number of possible tickets is

$$
\binom{49}{6} = \frac{49 \cdot 48 \cdot 47 \cdot 46 \cdot 45 \cdot 44}{6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1}.
$$

Cancel before multiplying: $48 \div 6 = 8$, $45 \div 5 = 9$, $44 \div 4 = 11$, then $9 \div 3 = 3$ and $46 \div 2 = 23$. Everything in the denominator is used up, and the numerator is $49 \cdot 8 \cdot 47 \cdot 23 \cdot 3 \cdot 11$. Multiply it out. Then, for the second question, count the tickets with exactly 3 matches: choose which 3 of the 6 drawn numbers the ticket holds, $\binom{6}{3}$ ways, and choose the other 3 numbers of the ticket from the 43 numbers that were not drawn, $\binom{43}{3}$ ways. Divide the product by the total number of tickets.

<details class="solution" markdown>
<summary>Finish</summary>

$49 \cdot 8 = 392$, then $392 \cdot 47 = 18{,}424$, then $18{,}424 \cdot 23 = 423{,}752$, then $423{,}752 \cdot 3 = 1{,}271{,}256$, then $1{,}271{,}256 \cdot 11 = 13{,}983{,}816$. So $\binom{49}{6} = 13{,}983{,}816$ and the jackpot probability is $\frac{1}{13{,}983{,}816}$, matching the published odds.

For exactly 3 matches: $\binom{6}{3} = 20$ and $\binom{43}{3} = \frac{43 \cdot 42 \cdot 41}{6} = 12{,}341$, so there are $20 \cdot 12{,}341 = 246{,}820$ such tickets. The probability is $\frac{246{,}820}{13{,}983{,}816} \approx 0.01765$, about 1 in 56.7.

Check: matching $j$ of the 6 numbers can happen in $\binom{6}{j}\binom{43}{6-j}$ ways for $j = 0, \dots, 6$, and the seven counts must add up to all tickets. Python gives $\sum_{j=0}^{6} \binom{6}{j}\binom{43}{6-j} = 13{,}983{,}816$, which equals $\binom{49}{6}$.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out for using the wrong tool. A committee is not a podium. Choosing 3 of 8 people for a committee is $\binom{8}{3} = 56$, not $P(8, 3) = 336$. Ask "if I swap two of the chosen items, is it a different outcome?" before you choose a formula. Using $P$ when order doesn't matter overcounts by exactly $k!$.

</div>

<div class="warning" markdown>

Watch out for counting a case twice. A committee of 3 is chosen from 6 people, and it must include at least one of Ana and Ben. A tempting count is "pick Ana or Ben first (2 ways), then choose the other 2 members from the remaining 5": $2 \cdot \binom{5}{2} = 20$. But a committee with both Ana and Ben is counted twice, once for each way of calling one of them "first". There are $\binom{4}{1} = 4$ such committees, and $20 - 4 = 16$ is right. The complement agrees: $\binom{6}{3} - \binom{4}{3} = 20 - 4 = 16$.

</div>

<div class="warning" markdown>

Watch out: add for "or" and multiply for "and", but only when the cases are separate. Choosing a CS elective or an economics elective is $6 + 4$. Choosing a CS elective and an economics elective is $6 \cdot 4$. If a course is on both lists, the sum rule double-counts it.

</div>

Some small cases are easy to get wrong. $0! = 1$, not 0, and $\binom{n}{0} = 1$: there is one way to choose nothing. $\binom{n}{n} = 1$ too. $P(n, k)$ and $\binom{n}{k}$ are 0 when $k > n$, since you can't pick 5 distinct people from a group of 3, and the factorial formula is not defined there because $(n-k)!$ would need a negative number. Finally, every formula in this lesson assumes the $n$ items are different from each other. When some are copies, as in BANANA, use the repeated-letters formula.

## Tricks and shortcuts

Cancel before you multiply. Writing $\binom{n}{k}$ as a product of $k$ numbers going down from $n$, over $k!$, keeps the numbers small: $\binom{52}{5} = \frac{52 \cdot 51 \cdot 50 \cdot 49 \cdot 48}{5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = 2{,}598{,}960$, and no step needs $52!$.

Use the symmetry to keep $k$ small: $\binom{100}{98} = \binom{100}{2} = \frac{100 \cdot 99}{2} = 4950$.

A problem about "at least one" or "at most" is usually shorter by the complement. "At least 1 of 10 items is defective" is the total minus "none is defective".

When you set up stages, fill the position with the most restrictions first. A rule such as "the first digit can't be 0" is easiest to apply at the first position, and the later positions then have simple counts.

For powers of ten, remember $2^{10} = 1024 \approx 10^3$. Then $2^{20} \approx 10^6$ and $2^{32} \approx 4 \times 10^9$. The estimates are near enough to size up a count: the number of subsets of a 30-element set is about a billion.

## In code

Python's `math` module has `perm`, `comb` and `factorial`, and `itertools` lists the objects themselves, so you can check a formula by brute force on a small case.

<details class="code" markdown>
<summary>In code</summary>

```python
import math
from itertools import combinations, permutations, product

print(math.perm(8, 3), math.comb(8, 3))                  # 336 56
print(len(list(permutations(range(8), 3))),
      len(list(combinations(range(8), 3))))              # 336 56
print(math.comb(49, 6))                                  # 13983816
print(len(set(permutations("BANANA"))),
      math.factorial(6) // (math.factorial(3) * math.factorial(2)))   # 60 60
print(len(list(product("abc", repeat=4))), 3**4)         # 81 81
print(math.comb(10, 4) - math.comb(6, 4))                # 195
print(round(math.log2(10**4), 2), round(math.log2(62**8), 1))   # 13.29 47.6

# the probability that 23 people all have different birthdays (365 days)
p = 1.0
for i in range(23):
    p *= (365 - i) / 365
print(round(1 - p, 4))                                   # 0.5073
```

Brute force over every subset of a 49-number pool would be slow, which is the point of the formula: `math.comb(49, 6)` returns at once, while listing all 13,983,816 tickets would take much longer. The last lines compute the birthday problem from Practice problem 7 as a running product, the same product as $\frac{P(365, 23)}{365^{23}}$.

</details>

## FAQ

### Why is $0! = 1$?

Three reasons agree. The number of ways to line up zero items is 1, the single empty arrangement. The recurrence $n! = n \cdot (n-1)!$ would break at $n = 1$ if $0!$ were anything else, since $1! = 1 \cdot 0!$. And the formula $\binom{n}{n} = \frac{n!}{n!\,0!}$ has to equal 1, because there is one way to choose all $n$ items. Setting $0! = 1$ keeps every formula in the lesson true at the edges.

### Why divide by $k!$ and not by something else?

Because each subset shows up exactly $k!$ times among the ordered lists, once for every ordering of its $k$ members. The proof of the combinations theorem counts the lists two ways to show it. If you divided by anything else, some subsets would be counted more than once or less than once.

### Is a combination lock a combination?

No, by the definition here. Opening a lock with the code 3-17-22 and with 22-17-3 are different, so order matters, and the number of codes is a permutation count (or $n^k$ when numbers can repeat). Despite its name, a "combination lock" counts ordered lists.

### What if the items are not all different?

The formulas assume all $n$ items can be told apart. If some are copies (three identical red marbles and two blue ones), count by letters-with-repeats, or count by cases. For instance, the number of ways to choose 2 marbles to take from three red and two blue ones depends on how many of each colour the selection has, so work through the cases: red-red, red-blue, blue-blue.

## Practice

### Warm-up

1\. Compute (a) $\binom{8}{3}$, (b) $\binom{8}{5}$, (c) $\binom{20}{2}$, (d) $\binom{100}{99}$, (e) $\binom{7}{0}$ and (f) $P(10, 3)$.

<details class="solution" markdown>
<summary>Solution</summary>

- (a) $\frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56$.
- (b) By symmetry $\binom{8}{5} = \binom{8}{3} = 56$.
- (c) $\frac{20 \cdot 19}{2} = 190$.
- (d) $\binom{100}{99} = \binom{100}{1} = 100$: choose the one item to leave out.
- (e) 1: there is one way to choose nothing.
- (f) $10 \cdot 9 \cdot 8 = 720$.

Check (f) against $\binom{10}{3}$: $720 \div 3! = 120$, and $\binom{10}{3} = \frac{10 \cdot 9 \cdot 8}{6} = 120$.

</details>

2\. A username is 2 lowercase letters followed by 3 digits. How many are there (a) if repeats are allowed, and (b) if no letter and no digit may repeat?

<details class="solution" markdown>
<summary>Solution</summary>

(a) There are 26 choices for each letter and 10 for each digit: $26 \cdot 26 \cdot 10 \cdot 10 \cdot 10 = 676{,}000$.

(b) The letters can't repeat, so $26 \cdot 25 = 650$; the digits can't repeat, so $10 \cdot 9 \cdot 8 = 720$. The total is $650 \cdot 720 = 468{,}000$.

Check: (b) must be smaller than (a), and it is. The ratio $\frac{468{,}000}{676{,}000} \approx 0.69$ says that about 69% of the usernames in (a) have no repeats.

</details>

3\. A conference schedules 5 talks, one after another, chosen from 9 submitted talks. How many different schedules are there? If instead only the set of 5 talks matters and not the order, how many sets are there?

<details class="solution" markdown>
<summary>Solution</summary>

Order matters for the schedule: $P(9, 5) = 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 = 15{,}120$. For the set of 5 talks, order doesn't matter: $\binom{9}{5} = \frac{15120}{5!} = \frac{15120}{120} = 126$.

Check: $126 \cdot 5! = 126 \cdot 120 = 15{,}120$, so each set of 5 talks gives 120 schedules. Also $\binom{9}{5} = \binom{9}{4} = \frac{9 \cdot 8 \cdot 7 \cdot 6}{24} = 126$.

</details>

### Standard

4\. How many distinct arrangements are there of the letters of STATISTICS? How many of them start with S?

<details class="solution" markdown>
<summary>Solution</summary>

The word has 10 letters: S appears 3 times, T 3 times, I 2 times, A once and C once. So there are $\frac{10!}{3!\,3!\,2!\,1!\,1!} = \frac{3{,}628{,}800}{6 \cdot 6 \cdot 2} = \frac{3{,}628{,}800}{72} = 50{,}400$ arrangements.

If an S comes first, the other 9 letters are S twice, T three times, I twice, A and C once: $\frac{9!}{2!\,3!\,2!} = \frac{362{,}880}{24} = 15{,}120$.

Check: the fraction of arrangements that start with S should be the fraction of the letters that are S, $\frac{3}{10}$, and $\frac{15{,}120}{50{,}400} = 0.3$.

</details>

5\. A project team of 4 is chosen from 7 CS students and 5 economics students. Count the teams (a) with no restriction, (b) with exactly 2 economics students, (c) with at least 1 economics student, (d) with at most 1 CS student.

<details class="solution" markdown>
<summary>Solution</summary>

(a) $\binom{12}{4} = \frac{12 \cdot 11 \cdot 10 \cdot 9}{24} = 495$.

(b) Two from each program: $\binom{5}{2}\binom{7}{2} = 10 \cdot 21 = 210$.

(c) The complement is a team of CS students only: $\binom{7}{4} = 35$. So the answer is $495 - 35 = 460$.

(d) At most one CS student means 0 or 1 CS students. The cases are separate, so add: 0 CS students, 4 economics, gives $\binom{5}{4} = 5$; 1 CS and 3 economics gives $7 \cdot \binom{5}{3} = 70$. The total is 75.

Check (a) by adding the cases by number of economics students: $\binom{7}{4} + 5\binom{7}{3} + 210 + \binom{5}{3}\cdot 7 + \binom{5}{4} = 35 + 175 + 210 + 70 + 5 = 495$.

</details>

6\. (Reviews [basic probability](../../02-middle-school/07-statistics-and-probability/02-basic-probability.md).) A random 8-bit string is chosen, so each of the $2^8$ strings is equally likely. What is the probability that it has (a) exactly 3 ones, (b) at least one 1, (c) an equal number of ones and zeros?

<details class="solution" markdown>
<summary>Solution</summary>

There are $2^8 = 256$ strings.

(a) A string with three ones is determined by the positions of the ones, a 3-element subset of the 8 positions: $\binom{8}{3} = 56$. The probability is $\frac{56}{256} = \frac{7}{32} \approx 0.219$.

(b) The complement of "at least one 1" is the single string of all zeros, so the probability is $1 - \frac{1}{256} = \frac{255}{256} \approx 0.996$.

(c) Four ones and four zeros: $\binom{8}{4} = 70$ strings, so the probability is $\frac{70}{256} = \frac{35}{128} \approx 0.273$.

Check: the counts $\binom{8}{k}$ for $k = 0, \dots, 8$ are $1, 8, 28, 56, 70, 56, 28, 8, 1$, and they add up to 256.

</details>

### Challenge

7\. In a group of 23 people, what is the probability that at least two share a birthday? Assume 365 equally likely birthdays and ignore leap days.

<details class="solution" markdown>
<summary>Solution</summary>

The complement of "at least two share a birthday" is "all 23 birthdays are different". The sample space is the ordered lists of 23 birthdays, one per person, so $\lvert S \rvert = 365^{23}$ (repeats allowed). The lists with all different entries number $P(365, 23) = 365 \cdot 364 \cdots 343$. So

$$
P(\text{all different}) = \frac{365}{365} \cdot \frac{364}{365} \cdots \frac{343}{365} \approx 0.4927,
$$

and the probability of at least one shared birthday is $1 - 0.4927 \approx 0.5073$, just over 50%.

Check: both counts treat the birthdays as ordered lists, one entry per person, so the ratio is a valid probability. The smaller case of 2 people gives $1 - \frac{364}{365} = \frac{1}{365}$, as it should: the second person has to match the first person's one day.

</details>

8\. Prove that $k\binom{n}{k} = n\binom{n-1}{k-1}$ for $1 \le k \le n$ by counting the same thing in two ways. Then use it to check the identity with $n = 7$, $k = 3$.

<details class="solution" markdown>
<summary>Solution</summary>

We want to show that two expressions count the same set. The set: ways to choose a committee of $k$ people from $n$ people and then name one of its members as the chair.

Count it by choosing the committee first: $\binom{n}{k}$ ways, and then the chair from among its $k$ members: $k$ ways. That gives $k\binom{n}{k}$.

Count it by choosing the chair first: any of the $n$ people. Then choose the other $k - 1$ members of the committee from the remaining $n - 1$ people: $\binom{n-1}{k-1}$ ways. That gives $n\binom{n-1}{k-1}$.

Both counts are the number of (committee, chair) pairs, so they are equal. $\blacksquare$

Check with $n = 7$ and $k = 3$: $3\binom{7}{3} = 3 \cdot 35 = 105$ and $7\binom{6}{2} = 7 \cdot 15 = 105$. The algebra agrees: $k\frac{n!}{k!\,(n-k)!} = \frac{n!}{(k-1)!\,(n-k)!} = n\frac{(n-1)!}{(k-1)!\,(n-k)!}$.

</details>

## Where this shows up

- The next lesson, the [binomial theorem](04-binomial-theorem.md), shows that $\binom{n}{k}$ is also the coefficient of $a^{n-k}b^k$ in $(a+b)^n$. Counting and discrete probability in the CS math folder ([counting rules](../../06-cs-math/03-counting-and-discrete-probability/01-counting-rules.md), [inclusion-exclusion and the pigeonhole principle](../../06-cs-math/03-counting-and-discrete-probability/04-inclusion-exclusion-and-pigeonhole.md)) extends these rules, and [discrete probability](../../06-cs-math/03-counting-and-discrete-probability/05-discrete-probability.md) uses them to find probabilities.
- In computing, $2^n$ counts bit strings and subsets, $n!$ counts the orderings a brute-force search must try (the number of possible tours in the travelling-salesman problem on $n$ cities grows like $n!$), and $\binom{n}{k}$ counts the ways to pick $k$ items, which is why the cost of checking all subsets of a given size grows so fast.
- In probability courses, the binomial distribution (met in [discrete random variables](../../05-university-core/07-probability/03-discrete-random-variables.md)) counts the ways to get $k$ successes in $n$ trials. In finance, the number of paths that lead to each node of a binomial price tree is a binomial coefficient.
