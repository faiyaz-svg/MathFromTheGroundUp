# Core proof methods

How to prove "if $P$, then $Q$" directly, read a proof, find one, split into cases, use the contrapositive, argue by contradiction, and write the result so a classmate can check it.

1. [Direct proof](01-direct-proof.md)
2. [How to read a proof](02-how-to-read-a-proof.md)
3. [Scratch work and proof strategies](03-scratch-work-and-proof-strategies.md)
4. [Proof by cases and WLOG](04-proof-by-cases-and-wlog.md)
5. [Contrapositive proof](05-contrapositive-proof.md)
6. [Proof by contradiction](06-proof-by-contradiction.md)
7. [How to write a proof](07-how-to-write-a-proof.md)

## Cheat sheet

### Proof strategy by statement shape

| The claim has the shape | Usual first move |
|---|---|
| for every $x$ in $S$, $P(x)$ | Let $x$ be arbitrary in $S$; prove $P(x)$. |
| there exists $x$ with $P(x)$ | Find a witness and check it. |
| if $P$, then $Q$ | Suppose $P$; derive $Q$. If $P$ is hard to use, try the contrapositive. |
| negative claim ("not", "irrational", "no", "infinitely many") | Assume the opposite; look for a contradiction. |
| $P$ or $Q$ | Assume not $P$ and prove $Q$, or split into cases. |
| $P$ and $Q$ | Prove each. |
| $P$ if and only if $Q$ | Prove both directions. |
| exactly one $x$ | Prove existence; assume two and show they are equal. |
| false claim | Find one counterexample. |
| the hypothesis has a defined word | Unpack it with fresh letters. |

### Direct proof

Assume $P$, walk to $Q$. Each line is a hypothesis, a definition, an earlier result or a consequence of earlier lines.

- Six moves: put the claim in if-then form; write the first line (objects and hypothesis); write the target (conclusion unpacked); unpack the hypothesis; connect; write forward and end in the words of the claim.
- Found backward, written forward. Each scratch arrow must point towards $Q$. Multiplying by a positive number is reversible; squaring is not.
- Cite a result by name, match its letters, and check its hypotheses.
- AM-GM: for $a, b \ge 0$, $\frac{a+b}{2} \ge \sqrt{ab}$, from $(\sqrt{a} - \sqrt{b})^2 \ge 0$; equality exactly when $a = b$.
- Euclid's step: if $a = bq + r$, then $(a, b)$ and $(b, r)$ have the same common divisors.
- Products: if $a \mid b$ and $c \mid d$, then $ac \mid bd$. If $n$ is odd, $8 \mid n^2 - 1$.

Main mistakes: starting at the conclusion; an unused hypothesis; dividing by a negative or unknown sign; citing a result whose hypotheses are not met.

### How to read a proof

Eight questions: the claim's shape; the method and the last line; every letter's origin; a reason for each line (H, D, R, L, A); fill the "clearly" steps; test on an example; where each hypothesis is used and what breaks without it; a one-sentence summary compared with the claim.

| Phrase in a text | What you do |
|---|---|
| clearly, obviously, it is easy to see | write the step out yourself |
| similarly, by symmetry | check the second case really is a copy |
| one checks, a routine calculation | do the computation |
| by the lemma | find it and check its hypotheses |

- Euclid's proof hides a lemma: every integer greater than 1 has a prime divisor. The number $p_1 \cdots p_n + 1$ need not be prime ($2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 59 \times 509$).
- "If $a \mid bc$, then $a \mid b$ or $a \mid c$" is false for composite $a$ ($6 \mid 2 \cdot 3$).

Main mistakes: reading to agree; checking lines but not the whole (a proof of the converse); trusting a theorem because it is true; confusing "I followed it" with "I understand it".

### Scratch work and proof strategies

- Scratch work is for you; the proof is for the reader. Never hand in a backward argument unless every step is an equivalence.
- Moves: unpack definitions; small cases; picture or table; work backward; work forward; choose by shape.
- Givens and goal: keep two lists and update them until they meet.
- When stuck: reread; write the definitions; test an example; prove a special case; change the problem; change the method; work from both ends; rest.
- Equality cases point to the square: if $x + \frac{4}{x} \ge 4$ is tight at $x = 2$, look for $(x-2)^2$.
- Examples: $n^3 - n = (n-1)n(n+1)$ is divisible by 6; $n^5 - n$ is divisible by 5; $x^2 + xy + y^2 = \left(x + \frac{y}{2}\right)^2 + \frac{3y^2}{4} \ge 0$.

Main mistakes: a backward proof ($-1 = 1$, so $1 = 1$); proving a pattern from small cases; hunting for a trick before unpacking definitions; working on a false claim.

### Proof by cases and WLOG

1. Choose a split that makes the definitions concrete.
2. Show the cases cover everything, and say why.
3. Prove each case under its own assumption.
4. Conclude for all.

| In the claim | Split |
|---|---|
| parity | $2k$ or $2k + 1$ |
| divisibility by $m$ | $n = mq + r$, $0 \le r < m$ |
| $\lvert x \rvert$ | $x \ge 0$ or $x < 0$ |
| $\max$, $\min$ | $a \ge b$ or $a < b$ |

- Squares leave remainder 0 or 1 modulo 3 (and modulo 4). If $3 \nmid n$, then $n^2 = 3k + 1$.
- Triangle inequality: $\lvert a + b \rvert \le \lvert a \rvert + \lvert b \rvert$, by sign cases; the mixed case uses WLOG.
- $\max(a,b) + \min(a,b) = a + b$, $\max \cdot \min = ab$, $\max(a,b) = \frac{a + b + \lvert a - b \rvert}{2}$.
- WLOG needs a true symmetry (swapping the names gives the same claim) and a stated reason. It may also use $x \mapsto -x$.

Main mistakes: a case missing (the claim "$x^2 \ge x$ for all $x$" fails on $0 < x < 1$); "similarly" for a case that is not a copy; WLOG on "if $ab$ is even, then $a$ is even"; using a case's assumption outside the case.

### Contrapositive proof

"If $P$, then $Q$" is equivalent to "if not $Q$, then not $P$". Assume not $Q$, derive not $P$.

| Statement | Contrapositive | Converse |
|---|---|---|
| if $P$ then $Q$ | if not $Q$ then not $P$ (same truth value) | if $Q$ then $P$ (can differ) |

| Statement | Negation |
|---|---|
| $n$ even (integer) | $n$ odd |
| $x$ rational | $x$ irrational |
| $P$ or $Q$ | not $P$ and not $Q$ |
| for every $x$, $P(x)$ | some $x$ with not $P(x)$ |

- Choose it when the conclusion is negative or an "or", or the hypothesis is negative or about a function of the variable ($n^2$ even).
- Opening line: "We prove the contrapositive: if (not $Q$), then (not $P$)."
- Examples: if $n^2$ is even then $n$ is even; if $xy$ is irrational then $x$ or $y$ is irrational; if $a^2 + b^2 = c^2$ then $a$ or $b$ is even.

Main mistakes: proving the converse or the inverse; a wrong negation; treating "not even" as "odd" for a non-integer.

### Proof by contradiction

Assume the claim is false (for "if $P$, then $Q$": assume $P$ and not $Q$), derive a statement that cannot be true, conclude the claim.

1. Write the exact negation.
2. Announce: "Suppose, for contradiction, that ...".
3. Unpack; derive.
4. Name both halves of the contradiction.
5. Conclude.

- $\sqrt{2}$ is irrational: write it in lowest terms $\frac{a}{b}$; then $a^2 = 2b^2$; $a$ and $b$ are both even; this contradicts lowest terms. Lemmas: every rational has a lowest-terms form; an even square has an even root.
- Infinitely many primes: for a finite list, $N = p_1 \cdots p_n + 1$ has a prime divisor outside the list, because a listed prime would divide 1.
- Contrapositive aims at a known target; contradiction aims at any falsehood.
- Halting problem: a decider $H$ lets you build $D$ that does the opposite of $H$ on its own code; either answer is wrong.

Main mistakes: "a contradiction" that is only a consequence; a wrong negation (a weaker claim proved); a direct proof dressed as contradiction; circular support.

### How to write a proof

Seven rules: state the claim and the method; introduce every letter; one idea per sentence; sentences with formulas inside; justify what needs it; keep forward order; end in the words of the claim.

| Method | Opening | Closing |
|---|---|---|
| direct | Let $x$ be ... | So ..., as claimed. |
| contrapositive | We prove the contrapositive: ... | This is the contrapositive, so the claim holds. |
| contradiction | Suppose, for contradiction, ... | This contradicts ...; so the claim holds. |
| cases | There are $k$ cases covering ... | In every case ..., so in general. |

- Circular reasoning uses the claim as a reason. Symbol soup uses arrows instead of words; an arrow is a statement.
- The "blah" test: replace each formula by "blah" and read the proof aloud.
- Typing: `$...$`, `\mid`, `\lvert x \rvert`, `$\blacksquare$`; in LaTeX use `amsthm` with the `theorem` and `proof` environments.

Main mistakes: too little or too much detail for the audience; scratch work left in; no ending; an object used before it is introduced.
