# Decidability and the halting problem

After this lesson you can show that a problem is decidable by describing an algorithm that always halts, explain by counting why some languages can't even be recognized, prove with a diagonal argument that $A_{\text{TM}}$ and the halting problem are undecidable, and prove that a language is decidable exactly when it and its complement are recognizable.

Before this: [Turing machines and the Church-Turing thesis](04-turing-machines-and-church-turing-thesis.md), [cardinality and countability](../../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md) (the diagonal argument and the countability of strings), and [proof by contradiction](../../04-proofs-and-logic/03-core-proof-methods/06-proof-by-contradiction.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. Describe how a Turing machine could decide, given a DFA $B$ and a string $w$, whether $B$ accepts $w$. Why does it always halt?
2. There are countably many Turing machines and uncountably many languages over $\{0, 1\}$. What follows?
3. You have a machine $M_1$ that recognizes $A$ and a machine $M_2$ that recognizes $\overline{A}$. How could you decide $A$?

<details class="solution" markdown>
<summary>Answers</summary>

1. Simulate $B$ on $w$: start in the start state, follow one transition per symbol of $w$, and accept if the final state is accepting. It reads $\lvert w \rvert$ symbols and stops, so it halts.
2. Each machine recognizes one language, so only countably many languages are recognized by some machine. There are uncountably many languages, so some language is recognized by no Turing machine.
3. Run $M_1$ and $M_2$ on the input, alternating one step of each. Every string is in $A$ or in $\overline{A}$, so one of the two machines accepts after finitely many steps. If $M_1$ accepts, accept. If $M_2$ accepts, reject.

</details>

## The idea

Every program you write is a finite piece of text, and so is its input. So a program can take another program as its input. A compiler does it, a debugger does it, and a virus scanner does it. This opens a natural question: can a program answer questions about other programs? Does this code ever crash? Does it ever stop? Does it do the same thing as that other code?

Some questions of this kind have algorithms. Whether a DFA accepts a given string can be settled by running it. Whether a DFA accepts anything at all can be settled by looking at its transition graph. For Turing machines it is different. The question "does this program stop on this input?" looks as if it should be answerable by running the program and watching. If it stops, you know. If it hasn't stopped after a million steps, you don't know whether to wait longer. The theorem of this lesson says that no cleverness can remove that uncertainty: there is no algorithm that answers the question correctly for every program and input.

The proof is the diagonal argument you have seen, applied to programs. Suppose a program $H$ decides whether programs halt. Then build a program that does the opposite of what $H$ predicts about it, and run that program on itself. Whatever $H$ says, it is wrong.

## Definitions

### Problems as languages

A decision problem about objects becomes a language by encoding the objects as strings ($\langle O \rangle$ from the [previous lesson](04-turing-machines-and-church-turing-thesis.md#encodings)). Deciding the problem means deciding whether a string belongs to the language. The languages of this lesson are:

$$
\begin{aligned}
A_{\text{DFA}} &= \{\langle B, w \rangle : B \text{ is a DFA that accepts the string } w\} \\
E_{\text{DFA}} &= \{\langle B \rangle : B \text{ is a DFA and } L(B) = \emptyset\} \\
EQ_{\text{DFA}} &= \{\langle B, C \rangle : B \text{ and } C \text{ are DFAs and } L(B) = L(C)\} \\
A_{\text{TM}} &= \{\langle M, w \rangle : M \text{ is a Turing machine that accepts } w\} \\
HALT_{\text{TM}} &= \{\langle M, w \rangle : M \text{ is a Turing machine that halts on } w\}
\end{aligned}
$$

In plain words: $A_{\text{DFA}}$ is the question "does this DFA accept this input", $E_{\text{DFA}}$ is "does this DFA accept nothing", $EQ_{\text{DFA}}$ is "do these two DFAs agree", and $A_{\text{TM}}$ and $HALT_{\text{TM}}$ ask the first and the "does it stop" question for Turing machines. The last is the **halting problem**. Strings that are not valid encodings are simply not in the language.

### Co-recognizable

A language is **co-Turing-recognizable**, or co-recognizable for short, if its complement is Turing-recognizable. In plain words: there is a machine that confirms membership of every string that is not in the language. A language that is recognizable can confirm its members. A language that is co-recognizable can confirm its non-members.

### The universal machine

*Theorem 1.* There is a Turing machine $U$ that recognizes $A_{\text{TM}}$.

*Proof.* On input $\langle M, w \rangle$, the machine $U$ checks that the input is a valid encoding. If not, it rejects. Otherwise it simulates $M$ on $w$ step by step, keeping $M$'s tape, state and head position on its own tape, and looking up each move in the description $\langle M \rangle$. If the simulation enters $q_{\text{accept}}$, $U$ accepts. If it enters $q_{\text{reject}}$, $U$ rejects. $\blacksquare$

Look back: $U$ accepts $\langle M, w \rangle$ exactly when $M$ accepts $w$, so $L(U) = A_{\text{TM}}$. If $M$ loops on $w$, then $U$ loops too, so $U$ is not a decider. It is a **universal Turing machine**: one fixed machine that can run any machine, given as data. Real computers are universal in the same sense, and a Python interpreter written in Python is an example. The In code section of the previous lesson had a small one.

## How to do it

### Showing that a language is decidable

1. Write down an algorithm that takes the encoded input and produces an answer. It may use any subroutine you have already shown to be a decider.
2. Check that the input is a valid encoding, and reject if not.
3. Argue that the algorithm halts on every input, by saying what is finite or what grows or shrinks at every step.
4. Argue that the answer is right: accept exactly when the input is in the language.
5. By the Church-Turing thesis, a Turing machine exists for the algorithm.

Step 3 is the one that has to be shown, not assumed. Simulating a machine that may loop doesn't halt, so a decider must never simulate a general TM without a bound.

### Showing that a language is undecidable by diagonalization

1. Suppose, for contradiction, that a decider $H$ exists.
2. Build a new machine $D$ that uses $H$ as a subroutine and does the opposite on the input that describes $D$ itself.
3. Run $D$ on its own description and show that $D$ accepts if and only if $D$ doesn't accept.
4. Conclude that $H$ can't exist.

## Theorems and proofs

*Theorem 2.* The languages $A_{\text{DFA}}$, $E_{\text{DFA}}$ and $EQ_{\text{DFA}}$ are decidable.

What we know: DFAs are finite objects and their computations stop. What we want: an algorithm for each language that always halts. The plan: simulation for the first, graph search for the second, and a reduction to the second (using the product construction from [finite automata](01-finite-automata-dfa-and-nfa.md#theorems)) for the third.

*Proof.* $A_{\text{DFA}}$: on input $\langle B, w \rangle$, simulate $B$ on $w$ as in the quick check. It does $\lvert w \rvert$ steps and halts, and it accepts exactly when $B$ does.

$E_{\text{DFA}}$: a DFA accepts some string exactly when an accepting state can be reached from the start state. On input $\langle B \rangle$, mark the start state. Repeat: mark every state that has an arrow from a marked state. Stop when no new state is marked. This happens after at most $\lvert Q \rvert$ rounds, since each round marks a new state or ends. Accept if no accepting state is marked, and reject if one is.

$EQ_{\text{DFA}}$: given $\langle B, C \rangle$, build the DFA $T$ for the symmetric difference

$$
L(T) = \bigl(L(B) \cap \overline{L(C)}\bigr) \cup \bigl(\overline{L(B)} \cap L(C)\bigr),
$$

the strings that exactly one of $B$ and $C$ accepts. The closure constructions of the first lesson (complement, intersection, union) produce $T$ from $B$ and $C$, and the whole construction is a finite computation. Then run the decider for $E_{\text{DFA}}$ on $\langle T \rangle$ and give its answer. We have $L(T) = \emptyset$ exactly when no string separates $B$ and $C$, that is, when $L(B) = L(C)$. $\blacksquare$

Look back: the third proof uses the second as a subroutine. This pattern, solving a new problem by transforming it into one already solved, is the idea of the next lesson, used in the other direction. Check: a computer test on 400 random pairs of DFAs with up to three states agrees with a brute-force comparison on all strings of length up to $\lvert Q_B \rvert \lvert Q_C \rvert + 1$.

Other decidable problems: $A_{\text{NFA}}$ and $A_{\text{REX}}$ (convert to a DFA first) and $A_{\text{CFG}}$, the question whether a grammar generates a given string. For $A_{\text{CFG}}$, convert the grammar to Chomsky normal form and try every derivation with exactly $2n - 1$ steps for a string of length $n \ge 1$, by [Theorem 3 of the grammar lesson](03-context-free-grammars-and-pushdown-automata.md#converting-a-grammar-to-chomsky-normal-form); there are finitely many of them, so the search halts. Together these show that every context-free language is decidable.

*Theorem 3.* Some languages are not Turing-recognizable.

What we know: the set of Turing machines is countable (Practice 8 of the previous lesson), and the set of languages over $\{0, 1\}$ is uncountable ([Theorem 8 of the cardinality lesson](../../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#why-some-problems-have-no-program)). What we want: a language that no machine recognizes. The plan: compare the two sizes.

*Proof.* Each Turing machine $M$ recognizes exactly one language, $L(M)$. So the set of recognizable languages is the image of the countable set of machines under $M \mapsto L(M)$, and the image of a countable set is countable (a surjection from a countable set gives a countable set, Practice 8 of the cardinality lesson). The set of all languages over $\{0, 1\}$ is $\mathcal{P}(\{0, 1\}^*)$, which is uncountable. A countable set can't be all of an uncountable one, so some language is not recognizable. $\blacksquare$

Look back: this proves that unrecognizable languages exist and gives none. In fact, most languages are unrecognizable, since the recognizable ones are a countable part of an uncountable whole. The next theorem finds a specific undecidable language.

*Theorem 4.* The language $A_{\text{TM}}$ is undecidable.

What we know: $A_{\text{TM}}$ is recognizable (Theorem 1). What we want: no decider exists. The plan: proof by contradiction, with a machine $D$ that does the opposite of what the supposed decider predicts about $D$ on its own description. We use the fact from the previous lesson that a machine can be given to another machine as a string.

*Proof.* Suppose, for contradiction, that a Turing machine $H$ decides $A_{\text{TM}}$. So on input $\langle M, w \rangle$, $H$ halts, accepting if $M$ accepts $w$ and rejecting if $M$ doesn't accept $w$ (rejects or loops). Define a machine $D$:

> On input $\langle M \rangle$, where $M$ is a Turing machine, run $H$ on $\langle M, \langle M \rangle \rangle$. If $H$ accepts, reject. If $H$ rejects, accept.

(On inputs that aren't descriptions of machines, $D$ rejects.) The machine $D$ halts on every input, since $H$ is a decider, so $D$ is itself a Turing machine and has a description $\langle D \rangle$. Run $D$ on $\langle D \rangle$. By the definition of $D$:

$$
D \text{ accepts } \langle D \rangle \iff H \text{ rejects } \langle D, \langle D \rangle \rangle \iff D \text{ does not accept } \langle D \rangle.
$$

The first equivalence is the definition of $D$, and the second is that $H$ decides $A_{\text{TM}}$. A statement equivalent to its own negation is a contradiction. So $H$ doesn't exist. $\blacksquare$

Look back: the proof is Cantor's diagonal argument. Make a table with a row for each machine $M_i$ and a column for each description $\langle M_j \rangle$, with the entry A if $M_i$ accepts $\langle M_j \rangle$ and R if it rejects or loops. The decider $H$ would compute every entry. The machine $D$ is built to disagree with row $i$ at the diagonal entry $(i, i)$, for every $i$. Here is an example with four machines and the diagonal in bold; $D$ is the flipped diagonal.

| | $\langle M_1 \rangle$ | $\langle M_2 \rangle$ | $\langle M_3 \rangle$ | $\langle M_4 \rangle$ | $\langle D \rangle$ |
|---|---|---|---|---|---|
| $M_1$ | **A** | R | A | R | $\dots$ |
| $M_2$ | A | **A** | A | A | $\dots$ |
| $M_3$ | R | R | **R** | R | $\dots$ |
| $M_4$ | R | A | R | **A** | $\dots$ |
| $D$ | R | R | A | R | **?** |

The row of $D$ differs from every other row at the diagonal. But $D$ is a machine too, so it is in the table, and its own diagonal entry is the entry that must be the opposite of itself. That is the contradiction. The only assumption that made the table fillable was that $H$ exists.

*Theorem 5 (the halting problem).* The language $HALT_{\text{TM}}$ is undecidable.

What we know: Theorem 4. What we want: no decider for $HALT_{\text{TM}}$. The plan: if there were one, we could decide $A_{\text{TM}}$: halting is most of the work, and the rest is a simulation that is now safe.

*Proof.* Suppose $R$ decides $HALT_{\text{TM}}$. Define a machine $S$:

> On input $\langle M, w \rangle$, run $R$ on it. If $R$ rejects, then $M$ loops on $w$, so reject. If $R$ accepts, then $M$ halts on $w$, so simulate $M$ on $w$ until it halts. If $M$ accepts, accept, and if $M$ rejects, reject.

The simulation in the last step stops, because $R$ said $M$ halts. So $S$ halts on every input and accepts exactly the pairs where $M$ accepts $w$: $S$ decides $A_{\text{TM}}$. This contradicts Theorem 4, so $R$ doesn't exist. $\blacksquare$

Look back: halting is the part that can't be known in advance. If you could tell when a run will stop, accepting would be a matter of waiting. Check with $M$ = a machine that loops on every input: $\langle M, w \rangle \notin HALT_{\text{TM}}$, and $S$ rejects it at once, which is right because $M$ doesn't accept $w$. The previous remark also shows that $HALT_{\text{TM}}$ is recognizable: simulate $M$ on $w$, and accept if the simulation halts.

*Theorem 6.* A language $A$ is decidable if and only if $A$ is recognizable and co-recognizable.

What we know: the definitions. What we want: both directions. The plan: a decider is a recognizer for both $A$ and its complement; conversely, run the two recognizers side by side.

*Proof.* ($\Rightarrow$) Let $M$ decide $A$. Then $M$ recognizes $A$. Swapping the accepting and rejecting states gives a decider for $\overline{A}$ (the previous lesson, Theorem 1), which recognizes $\overline{A}$. So $A$ is recognizable and co-recognizable.

($\Leftarrow$) Let $M_1$ recognize $A$ and $M_2$ recognize $\overline{A}$. On input $w$, run $M_1$ and $M_2$ in parallel: one step of $M_1$, then one step of $M_2$, and so on (using two tapes, or one by the multitape theorem). Every string $w$ is in $A$ or in $\overline{A}$, so $M_1$ accepts $w$ or $M_2$ accepts $w$, after finitely many steps. If $M_1$ accepts, accept. If $M_2$ accepts, reject. This halts on every input, and it accepts exactly the strings in $A$ (a string in $A$ is never accepted by $M_2$). So it decides $A$. $\blacksquare$

*Corollary 7.* The complement $\overline{A_{\text{TM}}}$ is not Turing-recognizable.

*Proof.* The language $A_{\text{TM}}$ is recognizable (Theorem 1). If $\overline{A_{\text{TM}}}$ were recognizable too, then $A_{\text{TM}}$ would be recognizable and co-recognizable, hence decidable by Theorem 6, which contradicts Theorem 4. $\blacksquare$

Look back: this is the first specific unrecognizable language, and it is the complement of a recognizable one. It shows that "recognizable" is not closed under complement. Intuitively, you can confirm that a machine accepts by running it and watching, but you can't confirm that it doesn't by watching: if it hasn't accepted yet, it may be about to.

## Worked examples

<div class="example" markdown>

### Example 1: deciding $E_{\text{DFA}}$

The DFA $B$ has states $a, b, c, d$ over $\{0, 1\}$, start state $a$, accepting state $d$, and transitions $a \xrightarrow{0} b$, $a \xrightarrow{1} a$, $b \xrightarrow{0} b$, $b \xrightarrow{1} a$, $c \xrightarrow{0,1} d$, $d \xrightarrow{0,1} d$. Is $\langle B \rangle \in E_{\text{DFA}}$?

Step 1 of the marking algorithm marks the start state: $\{a\}$. Round 1: the arrows out of $a$ lead to $b$ and $a$, so mark $b$: $\{a, b\}$. Round 2: the arrows out of $a$ and $b$ lead only to $a$ and $b$. Nothing new, so stop.

The accepting state $d$ is not marked. No path from the start reaches it, so $B$ accepts nothing and $\langle B \rangle \in E_{\text{DFA}}$. The state $c$ has an arrow to $d$, but nothing leads to $c$, so $c$ is unreachable too.

Check: a computer test of all strings up to length 12 finds that $B$ accepts none of them. The algorithm halts after 2 rounds, and in general after at most $\lvert Q \rvert$ rounds.

</div>

<div class="example" markdown>

### Example 2: why a time limit doesn't decide halting

Here is a tempting algorithm for $HALT_{\text{TM}}$: simulate $M$ on $w$ for $10^6$ steps; if it halts in that time, say yes; otherwise say no. It halts on every input, so it is a decider for some language, but not for $HALT_{\text{TM}}$.

Take the machine $M_0$ that counts to $2 \cdot 10^6$ on its tape and then halts. It halts, so $\langle M_0, \varepsilon \rangle \in HALT_{\text{TM}}$. The time-limited algorithm answers no. It is wrong on this input.

No other fixed limit works either: for each limit $t$ there is a machine that halts after $t + 1$ steps. And no limit that grows with the input works, since machines can count to any function that a machine can compute. Theorem 5 says that the problem is not fixable by choosing a better limit.

Check: the same argument applies to every bound that can be computed from $\langle M, w \rangle$: a machine that first computes the bound and then runs for one more step defeats it.

</div>

<div class="example" markdown>

### Example 3: the diagonal program, in code

Replace Turing machines by Python functions that take a function as input. Suppose a function `halts(f, x)` claims to say whether `f(x)` halts. Build the troublemaker from it:

```python
def make_trouble(halts):
    def trouble(f):
        if halts(f, f):      # the checker says f(f) halts...
            while True: pass # ...so loop forever
        return "stopped"     # the checker says f(f) loops, so stop
    return trouble
```

Run `trouble(trouble)`. If `halts(trouble, trouble)` returns True, then `trouble(trouble)` loops forever, so the checker was wrong. If it returns False, then `trouble(trouble)` returns at once, so the checker was wrong again. For every checker we can write down a case where it fails. The In code section runs this against three candidate checkers (replacing "loop forever" by an exception so that the program ends).

Check: the argument doesn't depend on how `halts` works. It could run the function for a year, analyse the source code, or ask an oracle. `trouble` is built from `halts` itself, so it knows what `halts` will say about it.

</div>

<div class="example" markdown>

### Example 4: finish the table (finish it yourself)

Three machines were run on the descriptions of the three machines, and the results (A for accept, R for reject or loop) are:

| | $\langle M_1 \rangle$ | $\langle M_2 \rangle$ | $\langle M_3 \rangle$ |
|---|---|---|---|
| $M_1$ | A | R | A |
| $M_2$ | R | R | A |
| $M_3$ | A | A | R |

Write the row of $D$ on the three descriptions, where $D$ does the opposite of $M_i$ on $\langle M_i \rangle$. Then say at which input $D$ differs from each of the three machines.

<details class="solution" markdown>
<summary>Finish</summary>

The diagonal entries are A (for $M_1$ on $\langle M_1 \rangle$), R (for $M_2$ on $\langle M_2 \rangle$) and R (for $M_3$ on $\langle M_3 \rangle$). $D$ does the opposite, so its row is R, A, A on $\langle M_1 \rangle$, $\langle M_2 \rangle$, $\langle M_3 \rangle$.

$D$ differs from $M_1$ at $\langle M_1 \rangle$ (R against A), from $M_2$ at $\langle M_2 \rangle$ (A against R), and from $M_3$ at $\langle M_3 \rangle$ (A against R). So $D$ is none of the three machines. With all machines in the table, the same construction gives a row that differs from every row.

Check: $D$'s row R, A, A matches none of the rows A, R, A and R, R, A and A, A, R of the table.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: "undecidable" does not mean "unsolvable in every case". It means that no single algorithm is correct on all inputs. Tools that check programs for termination or for bugs exist and are useful; each of them is wrong, or silent, or runs forever on some programs. A termination checker for loops that count down from a given number is easy. The theorem rules out a checker for all programs.

</div>

<div class="warning" markdown>

Watch out: do not confuse undecidable with unrecognizable. $A_{\text{TM}}$ and $HALT_{\text{TM}}$ are undecidable and recognizable: you can confirm "yes" by running the machine. Their complements are not even recognizable (Corollary 7 for $A_{\text{TM}}$), because a "no" has no finite certificate in general. When you are asked what class a language is in, there are three answers: decidable, recognizable but not decidable, and not recognizable.

</div>

<div class="warning" markdown>

Watch out: in the diagonal proof, the machine $D$ must be a legal Turing machine that halts when $H$ does, or its description can't be fed to $H$. $D$ uses $H$ as a subroutine, and $H$ is assumed to be a decider, so $D$ halts. This is where the assumption is used. The proof doesn't claim that $D$ exists in a world without $H$.

</div>

<div class="warning" markdown>

Watch out: the proof works on a machine run on its own description. This is not a trick: any program can be run on any string, including its own source code, and `cat` on its own file is an example. Nothing in the definitions forbids it, and a theorem about all inputs must cover it.

</div>

<div class="note" markdown>

Simple special cases are decidable. If the programs are restricted so that every loop is bounded by a known number, or if the machine has finitely many configurations (as for a DFA, or a program with a fixed amount of memory), halting can be decided by looking for a repeated configuration. The undecidability needs unbounded memory and unbounded loops, which is what a Turing machine has and what makes it a good model of a program.

</div>

## Tricks and shortcuts

- To decide a problem about DFAs, NFAs or regular expressions, convert to the form that makes the question a graph search: reachability for emptiness, and the symmetric difference for equality.
- When a proof needs "run $M$ on $w$" for a machine that may loop, never run it alone and wait. Run it alongside something that is certain to end, or bound the steps. The parallel run of Theorem 6 is the standard way, sometimes called dovetailing.
- To place a language in one of the three classes, ask first whether you can confirm "yes" by running something (recognizable), then whether you can confirm "no" the same way (co-recognizable). If both, it is decidable by Theorem 6.
- To prove undecidability in practice, you won't repeat the diagonal argument. You reduce a known undecidable problem to the new one, as in the next lesson. The diagonal argument is used once, for $A_{\text{TM}}$.

## In code

The first block decides $E_{\text{DFA}}$ and $EQ_{\text{DFA}}$ by the algorithms above and checks them against brute force on random DFAs. The second block runs the diagonal program of Example 3 against three candidate halting checkers, with `WouldLoop` standing for "runs forever" so that the program ends.

<details class="code" markdown>
<summary>In code</summary>

```python
import random
from itertools import product

def strings(alphabet, max_len):
    for n in range(max_len + 1):
        for t in product(alphabet, repeat=n):
            yield "".join(t)

# A DFA is (delta, start, accepting) with delta[(state, symbol)] = state.
def accepts(dfa, w):
    delta, q, accepting = dfa
    for a in w:
        q = delta[(q, a)]
    return q in accepting

def is_empty(dfa, alphabet="01"):
    """E_DFA: mark the states reachable from the start, then look for an accepting one."""
    delta, start, accepting = dfa
    marked, todo = {start}, [start]
    while todo:
        q = todo.pop()
        for a in alphabet:
            if delta[(q, a)] not in marked:
                marked.add(delta[(q, a)])
                todo.append(delta[(q, a)])
    return not (marked & accepting)

def symmetric_difference(d1, d2, alphabet="01"):
    (t1, s1, f1), (t2, s2, f2) = d1, d2
    states1 = {q for q, _ in t1}
    states2 = {q for q, _ in t2}
    delta = {((p, q), a): (t1[(p, a)], t2[(q, a)])
             for p in states1 for q in states2 for a in alphabet}
    accepting = {(p, q) for p in states1 for q in states2 if (p in f1) != (q in f2)}
    return delta, (s1, s2), accepting

def equivalent(d1, d2):
    """EQ_DFA: the machines agree iff their symmetric difference is empty."""
    return is_empty(symmetric_difference(d1, d2))

def random_dfa(n, rng):
    delta = {(q, a): rng.randrange(n) for q in range(n) for a in "01"}
    return delta, 0, {q for q in range(n) if rng.random() < 0.4}

rng = random.Random(7)
agree = equal_pairs = 0
for _ in range(400):
    d1, d2 = random_dfa(rng.randint(1, 3), rng), random_dfa(rng.randint(1, 3), rng)
    brute = all(accepts(d1, w) == accepts(d2, w) for w in strings("01", 10))
    agree += equivalent(d1, d2) == brute
    equal_pairs += brute
print(agree, equal_pairs)          # 400 112

# The diagonal program against some candidate halting checkers.
class WouldLoop(Exception):
    """Stands for 'runs forever'."""

def make_trouble(halts):
    def trouble(f):
        if halts(f, f):
            raise WouldLoop        # the checker said it halts, so loop forever
        return "stopped"           # the checker said it loops, so stop at once
    return trouble

def really_halts(f, x):
    try:
        f(x)
        return True
    except WouldLoop:
        return False

candidates = {"always yes": lambda f, x: True,
              "always no": lambda f, x: False,
              "odd name length": lambda f, x: len(f.__name__) % 2 == 1}
for name, halts in candidates.items():
    trouble = make_trouble(halts)
    print(name, halts(trouble, trouble), really_halts(trouble, trouble))
# always yes True False
# always no False True
# odd name length True False
```

</details>

## FAQ

### Isn't the halting problem just a trick with self-reference?

The self-reference is the proof technique, and the result is not about the trick. Once $HALT_{\text{TM}}$ is known to be undecidable, other undecidable problems are shown by reduction (the next lesson), with no self-reference. These include questions about real programs, such as whether two programs do the same thing. The self-reference only supplies the first undecidable problem.

### Does this mean we can never tell if a program halts?

We can for many programs, and tools do it every day. The theorem says that no algorithm gets every program right. For any fixed tool, there are programs on which it gives the wrong answer or no answer. Programmers use termination proofs, such as a quantity that gets smaller at every step of a loop, one program at a time.

### Why does the proof use $D$ on its own description and not on some other machine?

Because the table of machines against descriptions has to be completed by $D$ itself. $D$ is defined to disagree with each $M$ on the description of $M$. For $M = D$ the definition asks $D$ to disagree with itself on $\langle D \rangle$. Using a different input would leave open a place where $D$ could agree with some machine.

### What is the difference between "recognizable" and "decidable" for a student who thinks of programs?

A recognizer is like a program that prints "yes" when the answer is yes and may run forever otherwise. A decider is like a program that always prints "yes" or "no" and then stops. A program that searches for a solution to a puzzle is a recognizer: it finds an answer when there is one and may search forever when there isn't. Checking whether a given answer is correct is a decider.

## Practice

### Warm-up

1\. Use the decider for $A_{\text{DFA}}$ on $\langle B, 1101 \rangle$, where $B$ is the DFA for "ends in 01" with states $q_0, q_1, q_2$ (start $q_0$, accepting $q_2$, transitions $q_0 \xrightarrow{0} q_1$, $q_0 \xrightarrow{1} q_0$, $q_1 \xrightarrow{0} q_1$, $q_1 \xrightarrow{1} q_2$, $q_2 \xrightarrow{0} q_1$, $q_2 \xrightarrow{1} q_0$). What does it answer, and how many steps does the simulation take?

<details class="solution" markdown>
<summary>Solution</summary>

The simulation follows $q_0 \xrightarrow{1} q_0 \xrightarrow{1} q_0 \xrightarrow{0} q_1 \xrightarrow{1} q_2$. It takes 4 steps, one per symbol, ends in the accepting state $q_2$ and accepts.

Check: $1101$ ends in 01.

</details>

2\. Say for each language whether it is decidable, recognizable but not decidable, or not recognizable: $A_{\text{DFA}}$, $A_{\text{TM}}$, $\overline{A_{\text{TM}}}$, $HALT_{\text{TM}}$.

<details class="solution" markdown>
<summary>Solution</summary>

$A_{\text{DFA}}$ is decidable (Theorem 2). $A_{\text{TM}}$ is recognizable (Theorem 1) and not decidable (Theorem 4). $\overline{A_{\text{TM}}}$ is not recognizable (Corollary 7). $HALT_{\text{TM}}$ is recognizable (simulate $M$ on $w$ and accept when the simulation halts) and not decidable (Theorem 5).

Check: if $HALT_{\text{TM}}$ were co-recognizable as well, Theorem 6 would make it decidable, which Theorem 5 forbids. So its complement is also unrecognizable.

</details>

3\. A decider $H$ for $A_{\text{TM}}$ is supposed to exist, and $D$ is built as in Theorem 4. What does $D$ do on $\langle M \rangle$ if $M$ accepts its own description? What if $M$ loops on it?

<details class="solution" markdown>
<summary>Solution</summary>

If $M$ accepts $\langle M \rangle$, then $H$ accepts $\langle M, \langle M \rangle \rangle$, so $D$ rejects $\langle M \rangle$. If $M$ loops on $\langle M \rangle$, then $H$ rejects $\langle M, \langle M \rangle \rangle$ (it halts and says no, since $M$ doesn't accept), so $D$ accepts $\langle M \rangle$.

In both cases $D$ does the opposite of $M$ on $\langle M \rangle$, so $D$ is not equal to $M$ in what it accepts.

Check: a looping $M$ and an accepting $M$ both give a row of the table that disagrees with $D$ at the diagonal.

</details>

### Standard

4\. Decide whether $\langle B \rangle \in E_{\text{DFA}}$ for the DFA with states $p, q, r$ over $\{0, 1\}$, start state $p$, accepting state $r$, and transitions $p \xrightarrow{0} q$, $p \xrightarrow{1} p$, $q \xrightarrow{0} q$, $q \xrightarrow{1} r$, $r \xrightarrow{0,1} r$. Show the marking rounds.

<details class="solution" markdown>
<summary>Solution</summary>

Mark $p$. Round 1: from $p$ the arrows lead to $q$ and $p$, so mark $q$. Round 2: from $q$ the arrows lead to $q$ and $r$, so mark $r$. Round 3: nothing new. The accepting state $r$ is marked, so $B$ accepts something and $\langle B \rangle \notin E_{\text{DFA}}$.

A string that reaches $r$ is $01$: $p \xrightarrow{0} q \xrightarrow{1} r$.

Check: simulating $01$ on $B$ ends in $r$.

</details>

5\. Let $ALL_{\text{DFA}} = \{\langle B \rangle : B \text{ is a DFA and } L(B) = \Sigma^*\}$. Prove it is decidable.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: $E_{\text{DFA}}$ is decidable (Theorem 2), and swapping the accepting states of a DFA gives a DFA for the complement. What we want: a decider. The plan: reduce to emptiness of the complement.

*Proof.* On input $\langle B \rangle$, build the DFA $B'$ from $B$ by swapping accepting and non-accepting states, so $L(B') = \overline{L(B)}$. Run the decider for $E_{\text{DFA}}$ on $\langle B' \rangle$ and give its answer. Then $L(B) = \Sigma^*$ exactly when $L(B') = \emptyset$. The construction is finite and the decider halts, so this halts. $\blacksquare$

Check: for the DFA of "ends in 01", $B'$ accepts the strings that don't end in 01, such as $\varepsilon$, so $L(B') \ne \emptyset$ and the answer is no.

</details>

6\. Someone proposes: "To decide whether $M$ halts on $w$, simulate it, and also check whether the configuration has repeated; if it has, say it loops." Why is this not a decider for $HALT_{\text{TM}}$?

<details class="solution" markdown>
<summary>Solution</summary>

A repeated configuration does prove that the machine loops, so that check is correct when it fires. But a Turing machine can run forever without repeating a configuration, for example by writing a longer and longer string of 1s and moving right each time. The tape gets bigger, so each configuration is new. For such a machine the simulation never finds a repeat and never halts, so the proposed procedure doesn't halt either.

A repeated configuration works as a complete test only for machines with a bounded tape, which have finitely many configurations.

Check: the machine that moves right forever, writing 1 on every cell, has a new configuration at every step, since the head position is different each time.

</details>

### Challenge

7\. Prove that $HALT_{\text{TM}}$ is Turing-recognizable, and deduce that $\overline{HALT_{\text{TM}}}$ is not.

<details class="solution" markdown>
<summary>Solution</summary>

*Recognizable.* On input $\langle M, w \rangle$ (reject if it is not a valid encoding), simulate $M$ on $w$. If the simulation reaches $q_{\text{accept}}$ or $q_{\text{reject}}$, accept. This accepts exactly the pairs where $M$ halts on $w$. If $M$ loops on $w$, the simulation loops, and so the recognizer doesn't accept.

*Complement.* Suppose $\overline{HALT_{\text{TM}}}$ were recognizable. Then $HALT_{\text{TM}}$ would be recognizable and co-recognizable, hence decidable by Theorem 6. This contradicts Theorem 5. So $\overline{HALT_{\text{TM}}}$ is not recognizable. $\blacksquare$

Check: the same shape as Corollary 7. The pattern is general: a recognizable language that is not decidable has a complement that isn't recognizable.

</details>

8\. (Reviews [cardinality and countability](../../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md).) Let $w_1, w_2, w_3, \dots$ list all strings over $\{0, 1\}$, and let $L_1, L_2, L_3, \dots$ be any list of languages over $\{0, 1\}$. Define $D = \{w_i : w_i \notin L_i\}$. Show that $D$ is not on the list, and explain how this gives Theorem 3.

<details class="solution" markdown>
<summary>Solution</summary>

Suppose $D = L_k$ for some $k$. Is $w_k \in D$? If $w_k \in D$, then by the definition of $D$, $w_k \notin L_k = D$, a contradiction. If $w_k \notin D$, then $w_k \notin L_k$, so $w_k$ meets the definition of $D$ and $w_k \in D$, a contradiction. So $D \ne L_k$ for every $k$, and $D$ is not on the list.

This holds for every list of languages, so no list contains all languages: the set of languages is uncountable. The recognizable languages can be listed (list the Turing machines, which are countably many, and take $L(M)$ for each), so some language is not on that list, and so it is not recognizable. This is Theorem 3, and also the proof of Theorem 4 in disguise, with $L_i = L(M_i)$.

Check: with $L_1 = \{0\}$, $L_2 = \{\varepsilon\}$ and $L_3 = \emptyset$ listed against $w_1 = \varepsilon$, $w_2 = 0$, $w_3 = 1$: $w_1 \notin L_1$, so $\varepsilon \in D$. $w_2 = 0 \notin L_2$, so $0 \in D$. $w_3 = 1 \notin L_3$, so $1 \in D$. Then $D$ contains $\varepsilon$, which $L_1$ doesn't, and $0$, which $L_2$ doesn't, and $1$, which $L_3$ doesn't.

</details>

## Where this shows up

- The next lesson, [reductions and undecidability](06-reductions-and-undecidability.md), uses $A_{\text{TM}}$ as the first undecidable problem and spreads undecidability to others by reduction. The proof technique is a direct generalization of Theorem 5.
- In software, the halting problem is why static analysers, type checkers for expressive languages and compilers' optimizers can't be both sound and complete about program behaviour. A checker for a property of what a program does, as opposed to its text, must give up one of correctness, termination and generality. Rice's theorem, in the next lesson, makes this precise.
- The diagonal argument itself is the one from [cardinality and countability](../../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md#uncountable-sets), and it comes back in complexity theory as the time hierarchy theorem. The decidable problems for DFAs are also what finite-state model checkers rely on.
