# Theory of computation

What machines of different strength can compute: finite automata, grammars, Turing machines, the limits of computation, and the cost of computing.

1. [Finite automata: DFA and NFA](01-finite-automata-dfa-and-nfa.md)
2. [Regular expressions and the pumping lemma](02-regular-expressions-and-pumping-lemma.md)
3. [Context-free grammars and pushdown automata](03-context-free-grammars-and-pushdown-automata.md)
4. [Turing machines and the Church-Turing thesis](04-turing-machines-and-church-turing-thesis.md)
5. [Decidability and the halting problem](05-decidability-and-the-halting-problem.md)
6. [Reductions and undecidability](06-reductions-and-undecidability.md)
7. [P, NP and NP-completeness](07-p-np-and-np-completeness.md)

## Cheat sheet

### Finite automata: DFA and NFA

A string is a finite sequence of symbols from an alphabet $\Sigma$; $\Sigma^*$ is all strings, $\varepsilon$ is the empty string, and a language is a subset of $\Sigma^*$.

| Model | Definition | Accepts $w$ when |
|---|---|---|
| DFA | $(Q, \Sigma, \delta, q_0, F)$ with $\delta \colon Q \times \Sigma \to Q$ | $\delta^*(q_0, w) \in F$ |
| NFA | same, with $\delta \colon Q \times \Sigma_\varepsilon \to \mathcal{P}(Q)$ | some path reading $w$ ends in $F$ |

- Extended transition function: $\delta^*(q, \varepsilon) = q$ and $\delta^*(q, wa) = \delta(\delta^*(q, w), a)$.
- Designing a DFA: one state per thing to remember, start state for $\varepsilon$, an arrow for every state and symbol. For remainders in binary, $\delta(r, b) = (2r + b) \bmod m$.
- Subset construction: start $E(\{q_0\})$, $\delta'(R, a) = \bigcup_{r \in R} E(\delta(r, a))$, accept if the set contains an accepting state. Up to $2^{\lvert Q \rvert}$ states; "$n$-th symbol from the end is 1" needs $2^n$.
- Regular languages are closed under union, concatenation, star, complement (swap accepting states of a DFA) and intersection (product DFA).

Main mistakes:

- Leaving out the dead state, so a DFA has missing arrows.
- Making the old start state accepting in the star construction. Use a new start state.
- Complementing an NFA by swapping accepting states. Convert to a DFA first.
- Forgetting the $\varepsilon$-closure of the start state in the subset construction.

### Regular expressions and the pumping lemma

Regular expressions: symbols, $\varepsilon$, $\emptyset$, $R_1 \cup R_2$, $R_1 R_2$, $R^*$. Precedence is star, then concatenation, then union. $\emptyset^* = \{\varepsilon\}$. A language is regular exactly when a regular expression describes it. Expression to NFA by structural induction; DFA to expression by state elimination.

Pumping lemma: if $A$ is regular, there is $p$ such that every $s \in A$ with $\lvert s \rvert \ge p$ splits as $s = xyz$ with

1. $xy^i z \in A$ for all $i \ge 0$,
2. $\lvert y \rvert > 0$,
3. $\lvert xy \rvert \le p$.

| Step | Who | What |
|---|---|---|
| 1 | adversary | picks $p$ |
| 2 | you | pick $s \in A$ with $\lvert s \rvert \ge p$, written with $p$ |
| 3 | adversary | picks any valid split |
| 4 | you | pick $i$ and show $xy^i z \notin A$ for every split |

- $\{0^n 1^n\}$: $s = 0^p 1^p$, $i = 2$. $\{ww\}$: $s = 0^p 1 0^p 1$. $\{1^{n^2}\}$: $s = 1^{p^2}$, $i = 2$. "More than": pump down with $i = 0$.
- Myhill-Nerode: $m$ pairwise distinguishable strings force $m$ states. The closure trick: intersect with $0^* 1^*$ to reduce to $\{0^n 1^n\}$.

Main mistakes:

- Choosing $s$ that the adversary can pump (such as $0^{2p}$ for $\{ww\}$), or a fixed $s$ that doesn't depend on $p$.
- Checking one split instead of all.
- Using the lemma to prove a language is regular. The converse is false.

### Context-free grammars and pushdown automata

A CFG is $(V, \Sigma, R, S)$ with rules $A \to w$. The language is $\{w \in \Sigma^* : S \Rightarrow^* w\}$. A grammar is ambiguous if some string has two parse trees.

- $\{0^n 1^n\}$: $S \to 0S1 \mid \varepsilon$. Balanced parentheses: $S \to (S)S \mid \varepsilon$. $\{0^i 1^j : i \le j\}$: $S \to 0S1 \mid S1 \mid \varepsilon$.
- Remove ambiguity in expressions by layering: $E \to E + T \mid T$, $T \to T \times F \mid F$, $F \to (E) \mid a$.
- Chomsky normal form: rules $A \to BC$ and $A \to a$ only (and $S_0 \to \varepsilon$). Steps: new start, remove $\varepsilon$-rules, remove unit rules, split long rules. Derivations of a string of length $n \ge 1$ take $2n - 1$ steps.
- PDA: an NFA with a stack, $\delta \colon Q \times \Sigma_\varepsilon \times \Gamma_\varepsilon \to \mathcal{P}(Q \times \Gamma_\varepsilon)$. CFGs and PDAs describe the same languages. Nondeterminism is needed ($\{ww^R\}$).
- Pumping lemma for CFLs: $s = uvxyz$ with $uv^i x y^i z \in A$, $\lvert vy \rvert > 0$, $\lvert vxy \rvert \le p$. For $\{a^n b^n c^n\}$ take $s = a^p b^p c^p$: the window misses a letter, so $i = 2$ breaks the counts.

Main mistakes:

- Assuming a grammar is right after testing a few strings. Prove both inclusions.
- Pumping only one of $v$ and $y$.
- Believing CFLs are closed under intersection or complement. They are not.

### Turing machines and the Church-Turing thesis

A TM is $(Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$ with $\delta \colon Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$ and a blank $\sqcup \in \Gamma \setminus \Sigma$. A configuration $u\,q\,v$ has the head on the first symbol of $v$. Three outcomes: accept, reject, loop.

| Term | Meaning |
|---|---|
| recognizes $A$ | accepts exactly the strings of $A$; may loop otherwise |
| decides $A$ | recognizes $A$ and halts on every input |
| decidable | some decider exists |

- Decidable implies recognizable, and the complement of a decidable language is decidable.
- Multitape and nondeterministic machines recognize the same languages (single tape with $\#$ and dotted heads; breadth-first search of the computation tree).
- $\langle O \rangle$ is a string encoding of an object, so machines can take machines as input.
- Church-Turing thesis: algorithms in the informal sense are exactly what Turing machines compute. It is a thesis, supported by evidence, and cannot be proved.

Main mistakes:

- Treating "does not accept" as "rejects". A recognizer may loop.
- Forgetting that the head cannot see the left end of the tape.
- Calling the Church-Turing thesis a theorem.

### Decidability and the halting problem

| Language | Status |
|---|---|
| $A_{\text{DFA}}$, $E_{\text{DFA}}$, $EQ_{\text{DFA}}$, $A_{\text{CFG}}$ | decidable |
| $A_{\text{TM}}$, $HALT_{\text{TM}}$ | recognizable, not decidable |
| $\overline{A_{\text{TM}}}$, $\overline{HALT_{\text{TM}}}$ | not recognizable |

- Counting: countably many machines, uncountably many languages, so some language is not recognizable.
- $A_{\text{TM}}$ is undecidable: if $H$ decides it, $D$ on $\langle M \rangle$ does the opposite of $H$ on $\langle M, \langle M \rangle \rangle$, and $D$ on $\langle D \rangle$ contradicts itself. The table of machines against descriptions has $D$ as the flipped diagonal.
- $A$ is decidable if and only if $A$ and $\overline{A}$ are both recognizable (run both in parallel).
- $E_{\text{DFA}}$: mark reachable states. $EQ_{\text{DFA}}$: test the symmetric difference for emptiness.

Main mistakes:

- Confusing undecidable with unrecognizable.
- Reading the theorem as "no program can ever tell whether a program halts". It says no single algorithm is right on all inputs.
- Simulating a machine without a bound inside a decider.

### Reductions and undecidability

$A \le_m B$ if a computable $f$ has $w \in A \iff f(w) \in B$. If $A \le_m B$ and $B$ is decidable, so is $A$. So to prove $B$ undecidable, reduce a known undecidable $A$ to $B$.

| Problem | Reduction from $A_{\text{TM}}$: the machine $M'$ built from $\langle M, w \rangle$ |
|---|---|
| $HALT_{\text{TM}}$ | runs $M$ on its input; loops if $M$ rejects |
| $E_{\text{TM}}$ (to the complement) | accepts only $w$, and only if $M$ accepts $w$ |
| $REGULAR_{\text{TM}}$ | accepts $0^n 1^n$, otherwise runs $M$ on $w$ |
| $EQ_{\text{TM}}$ | pair $\langle M, \text{reject-all} \rangle$, reducing from $E_{\text{TM}}$ |

- The reduction only writes down $M'$. It never runs $M$.
- Rice's theorem: a property of $L(M)$ that is nontrivial and depends only on the language is undecidable. It does not cover properties of the description (number of states), bounded runs, or behaviour such as "halts on every input".

Main mistakes:

- Reducing in the wrong direction.
- Handling only one direction of "if and only if".
- Applying Rice's theorem to a property of the machine instead of its language.

### P, NP and NP-completeness

| Class | Definition |
|---|---|
| P | decided in time $O(n^k)$ for some $k$ |
| NP | has a polynomial-time verifier: a short certificate for each yes-instance |
| NP-hard | every NP language reduces to it by a polynomial-time mapping reduction $\le_P$ |
| NP-complete | NP-hard and in NP |

- $\mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{EXPTIME}$. NP also means decided by a nondeterministic machine in polynomial time.
- Certificates: SAT, an assignment; CLIQUE, the vertices; HAMPATH, the path; COMPOSITES, a factor. PATH is in P by breadth-first search.
- Cook-Levin: SAT is NP-complete, and so is 3SAT. To prove a new problem NP-complete: show it is in NP, reduce a known NP-complete problem to it in polynomial time, prove both directions.
- 3SAT to CLIQUE: a vertex for each literal in each clause; join literals from different clauses unless they contradict; $k$ = number of clauses.
- If one NP-complete problem is in P, then $\mathrm{P} = \mathrm{NP}$. The question is open.
- In practice: expect no fast exact algorithm for all instances. Use solvers, approximation, heuristics, special cases or small inputs.

Main mistakes:

- Reading NP as "not polynomial", or as "hard".
- Reducing the new problem to a known one instead of the other way round.
- Counting an exponentially long or slow-to-check certificate as a proof of membership in NP.
- Measuring the size of a number by its value and not its number of bits.
