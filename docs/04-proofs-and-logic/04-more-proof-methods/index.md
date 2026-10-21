# More proof methods

Proving two-way statements, proving that something exists or is unique, working with sets, and disproving false claims.

1. [If and only if proofs](01-if-and-only-if-proofs.md)
2. [Existence and uniqueness proofs](02-existence-and-uniqueness-proofs.md)
3. [Proofs about sets](03-proofs-about-sets.md)
4. [Counterexamples and disproof](04-counterexamples-and-disproof.md)

## Cheat sheet

### If and only if proofs

To prove $P \Leftrightarrow Q$, prove two implications under their own headings, each starting from its own hypothesis:

| Half | Assume | Show |
|---|---|---|
| ($\Rightarrow$), the "only if" half | $P$ | $Q$ |
| ($\Leftarrow$), the "if" half | $Q$ | $P$ |

- Choose the method for each half separately. A common split: one half direct (unpack a definition), the other by the contrapositive.
- "$P$ is necessary and sufficient for $Q$", "$P$ exactly when $Q$" and "$P$ iff $Q$" all ask for both halves.
- A chain $A \Leftrightarrow B \Leftrightarrow C$ proves a biconditional only if every arrow is reversible.

| Move | Reversible? |
|---|---|
| add or subtract the same number | yes |
| multiply or divide by a nonzero number | yes |
| apply a function with an inverse ($2^x$, $x^3$) | yes |
| square both sides | no, unless both sides are nonnegative |
| multiply or divide by an expression that can be 0 | no |

- To show $P_1, \dots, P_n$ are equivalent, prove a cycle $P_1 \Rightarrow P_2 \Rightarrow \cdots \Rightarrow P_n \Rightarrow P_1$: $n$ implications instead of $n(n-1)$.
- Model results: $n$ is odd iff $n^2$ is odd; for nonzero integers, $a \mid b$ and $b \mid a$ iff $a = \pm b$; $3 \mid n$ iff $3 \mid n^2$; for $c \ne 0$, $a \mid b$ iff $ca \mid cb$.

Main mistakes:

- Proving one direction and stopping.
- Proving the contrapositive of the same direction twice and calling it the second half.
- Using the other half's hypothesis ("since $n$ is odd" inside ($\Leftarrow$)).
- Trusting a chain with a squaring step: $\sqrt{2x+3} = x$ gives $x = 3$ and $x = -1$ after squaring, and only $3$ survives.
- Dividing $x^2 = x$ by $x$ and losing $x = 0$.

### Existence and uniqueness proofs

| Claim | Proof |
|---|---|
| there exists $x$ with $P(x)$ | constructive: name the witness, check it is in the domain and has every property |
| (same) | non-constructive: contradiction, pigeonhole, or the intermediate value theorem |
| $x$ is unique | assume $x$ and $y$ both work, show $x = y$ |
| there exists exactly one $x$ | an "Existence" part and a "Uniqueness" part |

- Pigeonhole: more than $k$ objects in $k$ boxes puts two in one box. Among any 5 integers, two differ by a multiple of 4.
- Intermediate value theorem: a continuous $f$ with $f(a) < 0 < f(b)$ has a root between $a$ and $b$. For $x^3 + x - 1$, $f(0) = -1$ and $f(1) = 1$, so a root lies in $(0, 1)$; bisection finds $0.6823\ldots$.
- A witness may depend on objects introduced earlier: for rationals $r < s$, the midpoint $\frac{r+s}{2}$ is rational and lies between them. It may not depend on objects introduced later.
- Non-constructive example: $\sqrt{2}^{\sqrt{2}}$ is rational or irrational; either way there are irrational $a$, $b$ with $a^b$ rational. A constructive pair: $a = \sqrt{2}$, $b = \log_2 9$, with $a^b = 3$.
- Uniqueness of 0 and of the opposite: if $a + b = 0$ and $a + c = 0$, then $b = b + (a + c) = (b + a) + c = c$.
- If $a \ne 0$, the equation $ax = b$ has exactly one solution, $x = a^{-1}b$. If $a = 0$ there is none or infinitely many.

Division algorithm. For integers $n$ and $d > 0$ there is exactly one pair $q$, $r$ with $n = qd + r$ and $0 \le r < d$.

| $n$ | $d$ | $q$ | $r$ |
|---|---|---|---|
| 100 | 8 | 12 | 4 |
| $-17$ | 5 | $-4$ | 3 |
| $-23$ | 6 | $-4$ | 1 |

- Existence: the least nonnegative number of the form $n - kd$ is less than $d$ (well-ordering). Uniqueness: subtract two pairs, so $(q - q')d = r' - r$ with $\lvert r' - r \rvert < d$, which forces $q = q'$.
- Python's `divmod` follows this for $d > 0$. C and Java truncate toward zero and give $-17 \% 5 = -2$.

Main mistakes:

- A uniqueness proof taken for existence ("the largest integer is unique" proves nothing about existence).
- A witness outside the domain: $x = \frac{5}{2}$ for "an integer with $2x = 5$".
- "Solving" first, then saying $y$ is "also" that value.
- A negative remainder.

### Proofs about sets

| Set | Membership test |
|---|---|
| $A \cap B$ | $x \in A$ and $x \in B$ |
| $A \cup B$ | $x \in A$ or $x \in B$ |
| $A \setminus B$ | $x \in A$ and $x \notin B$ |
| $A^c$ | $x \in U$ and $x \notin A$ |
| $S \in \mathcal{P}(A)$ | $S \subseteq A$ |
| $(a, b) \in A \times B$ | $a \in A$ and $b \in B$ |

- To show $A \subseteq B$: "Let $x \in A$", unpack, reach "$x \in B$".
- To show $A = B$: prove $A \subseteq B$ and $B \subseteq A$, or use a chain where every step is an equivalence.
- A set identity is a logical equivalence: with $p$, $q$, $r$ for "$x \in A$", "$x \in B$", "$x \in C$", the distributive law is $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$. The 8 rows of the truth table are the 8 regions of a three-set Venn diagram.
- Laws proved here: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$; $(A \cup B)^c = A^c \cap B^c$; $A \setminus B = A \cap B^c$; $\mathcal{P}(A) \cap \mathcal{P}(B) = \mathcal{P}(A \cap B)$; $A \times (B \cup C) = (A \times B) \cup (A \times C)$; $A \subseteq B$ iff $A \cap B = A$ iff $A \cup B = B$.
- $\emptyset \subseteq A$ for every $A$ (vacuous truth). The sets $\emptyset$, $\{\emptyset\}$ and $\{0\}$ are three different sets. A set with $n$ elements has $2^n$ subsets.
- False: $\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)$ (take $A = \{1\}$, $B = \{2\}$), and $A \cup (B \setminus C) = (A \cup B) \setminus C$ (take $A = C = \{1\}$, $B = \emptyset$).

Main mistakes:

- Proving a set identity from a Venn diagram.
- Proving one inclusion and calling it equality.
- Starting from "Let $x \in B$" to prove $A \subseteq B$.
- Mixing up $\in$ and $\subseteq$: $1 \in \{1, 2\}$, $\{1\} \subseteq \{1, 2\}$, and $\emptyset \in \{1\}$ is false.

### Counterexamples and disproof

To disprove a statement, negate it first, then prove the negation.

| Statement | To disprove it, show |
|---|---|
| for every $x$, $P(x)$ | one $x$ where $P$ fails |
| for every $x$, if $P(x)$ then $Q(x)$ | one $x$ with $P$ true and $Q$ false |
| there exists $x$ with $P(x)$ | a proof that $P$ fails for every $x$ (examples are not enough) |
| $P$ iff $Q$ | a case where exactly one of them holds |
| there is exactly one $x$ | none, or two different ones |
| $A \subseteq B$ or $A = B$ | one element in $A$ and not in $B$ (or in only one of the sets) |

Steps: write the claim in full, negate it, say what a witness looks like, search, verify the hypothesis and the failed conclusion separately, and state the disproof.

- Search edge cases first: $0$, $1$, $-1$, $2$, equal values, $\frac{1}{2}$, $\emptyset$, a one-element set, disjoint sets, a constant, the empty list.
- A short loop finds the first counterexample over a range. Finding none proves nothing.
- Examples: $a = 4$, $b = c = 2$ breaks "if $a \mid bc$ then $a \mid b$ or $a \mid c$" (true for prime $a$). $n = 2$ breaks "$4 \mid n^2$ implies $4 \mid n$". $x = -3$, $y = 2$ breaks "$x < y$ implies $x^2 < y^2$" (true for $0 \le x < y$).
- Famous false patterns: $n^2 + n + 41$ is composite at $n = 40$; $n^2 + n + 17$ at $n = 16$ ($289$); $2^{2^n} + 1$ is composite at $n = 5$ ($641 \times 6700417$); $27^5 + 84^5 + 110^5 + 133^5 = 144^5$ breaks Euler's sum of powers conjecture; the Pólya conjecture first fails at $n = 906{,}150{,}257$.
- A prove-or-disprove problem: test cases first, then try a proof, and read the point where the proof sticks.

Main mistakes:

- A counterexample that breaks a hypothesis: $n = 3$ does not refute "if $n$ is even then $n^2$ is divisible by 4".
- Refuting the converse and calling it the claim.
- Checking examples to "disprove" an existence claim.
- Searching the wrong domain: $n^2 \ge n$ is true for naturals and false at $x = \frac{1}{2}$ for reals.
- Counting a failed computer search as a proof.
