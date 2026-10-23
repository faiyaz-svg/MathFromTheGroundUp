# Turing machines and the Church-Turing thesis

After this lesson you can define a Turing machine as a 7-tuple, trace its configurations on an input, design a machine for a simple language, tell recognizable languages from decidable ones, and state the Church-Turing thesis and what it does and doesn't claim.

Before this: [context-free grammars and pushdown automata](03-context-free-grammars-and-pushdown-automata.md) and [finite automata: DFA and NFA](01-finite-automata-dfa-and-nfa.md). The idea of a bijection between strings and numbers is from [cardinality and countability](../../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. A Turing machine is in the configuration $01\,q\,10$ (the head is on the first symbol after $q$) and the transition is $\delta(q, 1) = (r, x, R)$. What is the next configuration?
2. The head is on the leftmost cell and the machine must move left. Where does the head end up?
3. Can a Turing machine run forever on some input? If it does, does it accept or reject?

<details class="solution" markdown>
<summary>Answers</summary>

1. The head reads 1, writes $x$ and moves right, so the configuration is $01x\,r\,0$.
2. It stays on the leftmost cell. The tape has a left end, and a move left from it leaves the head in place.
3. Yes. A machine that runs forever neither accepts nor rejects. It is said to loop, and the input is not accepted.

</details>

## The idea

A finite automaton reads its input once, left to right, with a fixed amount of memory. A pushdown automaton adds a stack. Both fail on easy tasks: no pushdown automaton recognizes $\{a^n b^n c^n\}$, or the strings of the form $ww$.

Think of what a person does with pencil and paper. They read symbols, write symbols, erase, move back and forth, and have as much paper as they need. At each moment they are in some state of mind, and what they write depends only on that and on what they see. Alan Turing took that picture in 1936 and made it a machine: a finite control, a tape that is as long as needed, and a head that reads and writes one cell and moves one cell at a time.

The point of the model is that it is simple enough to prove things about and strong enough to compute everything a computer can. The proofs about what is impossible for this machine will then be proofs about what is impossible for any program, in any language, on any hardware. That is the content of the Church-Turing thesis at the end of the lesson, and of the next two.

## Definitions

### Turing machines

A **Turing machine** (TM) is a 7-tuple $M = (Q, \Sigma, \Gamma, \delta, q_0, q_{\text{accept}}, q_{\text{reject}})$ where

1. $Q$ is a finite set of states,
2. $\Sigma$ is the input alphabet, which does not contain the **blank symbol** $\sqcup$,
3. $\Gamma$ is the tape alphabet, with $\sqcup \in \Gamma$ and $\Sigma \subseteq \Gamma$,
4. $\delta \colon Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$ is the transition function,
5. $q_0 \in Q$ is the start state,
6. $q_{\text{accept}} \in Q$ is the accept state, and
7. $q_{\text{reject}} \in Q$ is the reject state, with $q_{\text{reject}} \ne q_{\text{accept}}$.

In plain words: the tape is a row of cells, infinite to the right, and starts out holding the input followed by blanks. The head starts on the leftmost cell. A transition $\delta(q, a) = (r, b, D)$ says: in state $q$ reading $a$, write $b$ over it, move one cell in direction $D$ (left or right), and go to state $r$. On the leftmost cell, a move left leaves the head where it is. The machine halts as soon as it enters $q_{\text{accept}}$ or $q_{\text{reject}}$, and the transitions out of those two states are never used. When a book leaves a transition out of a table, it means the machine goes to $q_{\text{reject}}$.

### Configurations and computation

A **configuration** records everything about an instant of the computation: the state, the contents of the tape and the head position. We write it $u\,q\,v$, where $q$ is the current state, $uv$ is the tape contents up to the last non-blank cell, and the head is on the first symbol of $v$. Configuration $C_1$ **yields** $C_2$ if the machine can go from $C_1$ to $C_2$ in one step. For example, if $\delta(q_1, b) = (q_2, c, R)$ then $u\,a\,q_1\,b\,v$ yields $u\,a\,c\,q_2\,v$, and if $\delta(q_1, b) = (q_2, c, L)$ then it yields $u\,q_2\,a\,c\,v$.

The **start configuration** on input $w$ is $q_0 w$. An **accepting configuration** has state $q_{\text{accept}}$ and a **rejecting configuration** has state $q_{\text{reject}}$, and both are **halting configurations**. The machine $M$ **accepts** $w$ if a sequence of configurations $C_1, \dots, C_k$ exists with $C_1$ the start configuration, each $C_i$ yielding $C_{i+1}$, and $C_k$ accepting. The set of strings that $M$ accepts is the **language of $M$**, written $L(M)$.

On a given input, a TM has three possible fates: it accepts, it rejects, or it **loops** (it never enters a halting state). This third outcome is new. A DFA always finishes, because it reads a finite input and stops.

### Recognizable and decidable

A language is **Turing-recognizable** if some TM recognizes it, that is, has it as $L(M)$. A TM that recognizes a language accepts every string in it, and on every other string either rejects or loops. A TM is a **decider** if it halts on every input. A language is **Turing-decidable**, or just decidable, if some decider recognizes it.

In plain words: to recognize a language is to confirm membership when the answer is yes, with no promise about what happens when the answer is no. To decide a language is to always give an answer, yes or no. Every decidable language is recognizable, because a decider is a TM. Whether the reverse holds is the question of the next lesson, and the answer is no.

*Theorem 1.* If $A$ is decidable, then its complement $\overline{A}$ is decidable.

What we know: a decider $M$ for $A$. What we want: a decider for $\overline{A}$. The plan: swap the answers.

*Proof.* Build $M'$ from $M$ by exchanging the roles of $q_{\text{accept}}$ and $q_{\text{reject}}$. On every input $M$ halts in one of them, and $M'$ halts in the other, so $M'$ halts on every input and accepts exactly the strings that $M$ rejects, which are those not in $A$. $\blacksquare$

Look back: the proof needs $M$ to halt. If $M$ were only a recognizer, the swap would turn "loops" into "loops", not into "accepts", so complements of recognizable languages are a different matter. That difference is the center of the next lesson.

### Encodings

A Turing machine reads strings. To give it an object such as a graph, a DFA or another Turing machine, we write the object as a string. The **encoding** of an object $O$ is a string $\langle O \rangle$, and $\langle O_1, O_2 \rangle$ is the encoding of a pair. The exact scheme doesn't matter as long as a TM can decode it: a graph can be written as a list of vertices and a list of edges, a DFA as its five parts, and a TM as its transition table. Any such scheme can be turned into a string over $\{0, 1\}$.

In plain words: an input to a program is always text in the end. A language of strings such as $\{\langle G \rangle : G \text{ is a connected graph}\}$ is a problem about graphs. A TM that is given $\langle M \rangle$ for another machine $M$ can read the table of rules and simulate $M$. This is the same idea as a program that reads source code, and it is what makes the arguments in the next two lessons work.

### Variants

A **multitape Turing machine** has $k$ tapes, each with its own head, and a transition reads all $k$ symbols, writes $k$ symbols and moves each head left or right (or lets it stay). A **nondeterministic Turing machine** (NTM) has $\delta \colon Q \times \Gamma \to \mathcal{P}(Q \times \Gamma \times \{L, R\})$, a set of possible moves, and accepts if some branch of the computation reaches $q_{\text{accept}}$.

*Theorem 2.* Every multitape TM has an equivalent single-tape TM. Every NTM has an equivalent deterministic TM.

The machines are equivalent in power: the same languages are recognized. The proofs are sketched in the proofs section below.

### The Church-Turing thesis

The **Church-Turing thesis** says: a function can be computed by an algorithm, in the informal sense of a finite, mechanical procedure, exactly when it can be computed by a Turing machine. Equivalently, the intuitive notion of an algorithm is captured by Turing machines.

It is a thesis and not a theorem, because one side of it, "algorithm" in the informal sense, is not a mathematical object. There is nothing to prove it about. What exists is evidence. Every model of computation proposed since 1936 has turned out to compute the same functions: Church's lambda calculus (from the same years as Turing's machines), recursive functions, register machines, and every programming language that can allocate unbounded memory. No one has found a procedure that people would call an algorithm and that a TM can't carry out. Nor can the thesis be refuted by a theorem; it could only be refuted by finding a new kind of procedure that is mechanical and not simulated by a TM.

## How to do it

### Designing a Turing machine

1. Write the algorithm in words, thinking of the tape as scratch paper: what do you mark, what do you compare, in which order does the head move?
2. Decide on the tape alphabet. Extra symbols are marks: $x$ for "crossed off", or dotted copies of letters to remember a position.
3. Mark the left end if you need to come back to it. The head can't see the left end, so a common trick is to overwrite the first symbol by a blank at the beginning, or by a special symbol, and treat that cell as the marker.
4. Split the algorithm into phases (sweep right, sweep back, compare, accept). Each phase, and each thing the machine must remember within a phase, is a state.
5. Write the transition for every state and every symbol that can occur in it. Leave out the impossible ones, which then reject.
6. Trace the machine on a string in the language, a string not in the language, and the shortest inputs.

TMs are described at three levels. The formal level gives the 7-tuple. The implementation level describes the head movements and the marks in words. The high-level description gives only an algorithm in pseudocode, relying on the thesis that a TM exists for it. Proofs in the later lessons are at the high level; the examples here are at the first two so that you can see what the thesis is hiding.

## Proofs

*Proof of Theorem 2, multitape to single-tape (sketch).* What we know: a $k$-tape machine $M$. What we want: a single-tape machine $S$ with the same language. The plan: store all $k$ tapes on one tape, separated by a new symbol $\#$, and mark each head position with a dotted copy of the symbol it is on.

On input $w = w_1 \cdots w_n$, $S$ first rewrites its tape as $\#\,\dot{w}_1 w_2 \cdots w_n\,\#\,\dot{\sqcup}\,\#\,\dot{\sqcup}\,\#\cdots\#$, which has the input on the first track with its head mark and $k - 1$ empty tapes. To simulate one step of $M$, $S$ scans the whole tape from the left to read the symbols under the $k$ dotted marks, then scans again to write the new symbols and move the dots as the transition of $M$ says. If a head would move onto a $\#$, that tape has run out of room, so $S$ shifts the rest of the tape to the right by one cell and inserts a blank. $S$ accepts exactly when $M$ does. Each step of $M$ takes $S$ a number of moves proportional to the length of the used part of the tape, so a computation of $t$ steps of $M$ takes $S$ roughly $t^2$ steps. $\blacksquare$

*Proof of Theorem 2, NTM to deterministic (sketch).* The computation of an NTM $N$ on an input $w$ is a tree: each configuration has the configurations it can yield as its children, and the tree has a bounded branching number $b$, the largest number of choices in $\delta$. $N$ accepts if some node of the tree is accepting. A deterministic machine $D$ searches the tree breadth-first, by levels. It uses three tapes (equivalent to one, by the first half of the theorem): tape 1 holds the input and is never changed, tape 2 is a working copy for the branch being tried, and tape 3 holds an address, a string over $\{1, \dots, b\}$ that names a node. For each address, in order of length and then alphabetically, $D$ copies the input to tape 2, runs $N$ along the branch the address names, and accepts if it reaches an accepting configuration. If the address is invalid or the branch rejects, $D$ goes to the next address. If $N$ accepts, some accepting node has an address of some finite length, and $D$ reaches it after finitely many addresses. If $N$ never accepts, $D$ never accepts. $\blacksquare$

Look back: the search is breadth-first and not depth-first. A depth-first search could dive into an infinite branch and never get back to the accepting node on another branch. The price of the simulation is time: it can be exponential, and nobody knows whether that is avoidable. That is the subject of the last lesson.

## Worked examples

<div class="example" markdown>

### Example 1: a machine for $\{0^{2^n} : n \ge 0\}$

The language is the strings of 0s whose length is a power of 2: $0, 00, 0000, 00000000, \dots$ (but not $\varepsilon$). The input alphabet is $\{0\}$.

Step 1, the algorithm. Sweep over the tape and cross off every other 0, starting with the first. If a sweep finds exactly one uncrossed 0, accept. If it finds an odd number of uncrossed 0s greater than one, reject. Otherwise the number of uncrossed 0s has been halved, so go back to the left and sweep again. A power of 2 can be halved down to 1 without ever meeting an odd number above 1, and a number that isn't a power of 2 reaches such an odd number.

Steps 2 and 3, the marks. Cross-offs are written $x$. In the first sweep the first 0 is replaced by a blank, which both counts as crossed off and marks the left end, so the head can find it on the way back.

Step 4, the states. The sweeps need to count the uncrossed 0s met so far, only as "none", "one", "even, at least two" or "odd, at least three". State $q_1$ is the start. State $q_2$ is a sweep that has met no uncrossed 0 yet. State $q_3$ has met exactly one (which it crossed off), $q_4$ has met an even number (the last was kept) and $q_5$ an odd number of at least three (the last was crossed off). State $q_6$ is the return trip to the left end.

Step 5, the transitions. "None" means there is no transition, so the machine rejects.

| $\delta$ | 0 | $x$ | $\sqcup$ |
|---|---|---|---|
| $q_1$ | $q_3, \sqcup, R$ | none | none |
| $q_2$ | $q_3, x, R$ | $q_2, x, R$ | none |
| $q_3$ | $q_4, 0, R$ | $q_3, x, R$ | $q_{\text{accept}}, \sqcup, R$ |
| $q_4$ | $q_5, x, R$ | $q_4, x, R$ | $q_6, \sqcup, L$ |
| $q_5$ | $q_4, 0, R$ | $q_5, x, R$ | $q_{\text{reject}}, \sqcup, R$ |
| $q_6$ | $q_6, 0, L$ | $q_6, x, L$ | $q_2, \sqcup, R$ |

Step 6, the trace on $00$, one configuration per row, with the rule used:

| Configuration | Rule used |
|---|---|
| $q_1\,00$ | $\delta(q_1, 0) = (q_3, \sqcup, R)$ |
| $\sqcup\,q_3\,0$ | $\delta(q_3, 0) = (q_4, 0, R)$ |
| $\sqcup 0\,q_4\,\sqcup$ | $\delta(q_4, \sqcup) = (q_6, \sqcup, L)$ |
| $\sqcup\,q_6\,0\sqcup$ | $\delta(q_6, 0) = (q_6, 0, L)$ |
| $q_6\,\sqcup 0\sqcup$ | $\delta(q_6, \sqcup) = (q_2, \sqcup, R)$ |
| $\sqcup\,q_2\,0\sqcup$ | $\delta(q_2, 0) = (q_3, x, R)$ |
| $\sqcup x\,q_3\,\sqcup$ | $\delta(q_3, \sqcup) = (q_{\text{accept}}, \sqcup, R)$ |
| $\sqcup x \sqcup\,q_{\text{accept}}\,\sqcup$ | halts, accepts |

The first sweep blanked the first 0 and kept the second. The second sweep crossed off the one 0 that remained and found it alone, so $00$ is accepted.

Check: a computer simulation of this table on $0^k$ for every $k$ from 0 to 69 accepts exactly $k = 1, 2, 4, 8, 16, 32, 64$, and always halts. The simulation is the same loop that appears in the In code section.

</div>

<div class="example" markdown>

### Example 2: a rejecting run, and a count of the steps

Trace the same machine on $000$, which should be rejected.

$q_1\,000 \to \sqcup\,q_3\,00 \to \sqcup 0\,q_4\,0 \to \sqcup 0x\,q_5\,\sqcup \to \sqcup 0 x \sqcup\,q_{\text{reject}}\,\sqcup$.

The first 0 was blanked ($q_3$ has met one uncrossed 0), the second was kept ($q_4$, even), and the third was crossed off ($q_5$, odd and at least three). At the blank the machine is in $q_5$, so the count was odd and more than one: reject. This takes 4 steps.

The input $0000$ takes 21 steps: the first sweep leaves two uncrossed 0s, the second sweep leaves one, and the third finds it alone. In general each sweep costs about as many steps as the tape is long, and there are about $\log_2 n$ sweeps, so the running time is about $n \log n$.

Check: the simulation reports reject after 4 steps on $000$ and accept after 21 steps on $0000$, matching.

</div>

<div class="example" markdown>

### Example 3: recognizing without deciding

Let $M$ have $\Sigma = \{0, 1\}$ and the transitions $\delta(q_0, 1) = (q_{\text{accept}}, 1, R)$, $\delta(q_0, 0) = (q_0, 0, R)$ and $\delta(q_0, \sqcup) = (q_0, \sqcup, R)$. The machine scans right past 0s and accepts when it meets a 1. On an input that contains a 1 it accepts. On an input with no 1 (a string of 0s, or the empty input) it moves right forever, reading 0s and then blanks, and never halts.

So $L(M)$ is the set of strings that contain a 1, and $M$ recognizes this language. It is not a decider, because it loops on some inputs. But the same language is decidable: a different machine can reject when it reaches the first blank without having seen a 1. Being a decider is a property of a machine, and being decidable is a property of a language.

Check: the simulation, cut off after 1,000 steps, reports accept for $1$, $10$ and $01$, and no halt for $0$ and $\varepsilon$.

</div>

<div class="example" markdown>

### Example 4: finish the trace of $0000$

Here are the first configurations of Example 1's machine on $0000$:

$$
q_1\,0000 \to \sqcup\,q_3\,000 \to \sqcup 0\,q_4\,00 \to \sqcup 0x\,q_5\,0 \to \sqcup 0x0\,q_4\,\sqcup \to \sqcup 0x\,q_6\,0\sqcup.
$$

The first sweep has blanked the first 0, kept the second, crossed off the third and kept the fourth. Continue the trace through the return trip and the second sweep, and decide whether the input is accepted.

<details class="solution" markdown>
<summary>Finish</summary>

The return trip in $q_6$ moves left over $0$, $x$ and $0$ until it reads the blank at the left end, then steps right into $q_2$:

$$
\sqcup 0\,q_6\,x0\sqcup \to \sqcup\,q_6\,0x0\sqcup \to q_6\,\sqcup 0x0\sqcup \to \sqcup\,q_2\,0x0\sqcup.
$$

The second sweep: $q_2$ reads the 0 and crosses it off, moving to $q_3$. State $q_3$ moves over the $x$, reads the last 0, keeps it and moves to $q_4$, and $q_4$ reads the blank and starts the return trip:

$$
\sqcup x\,q_3\,x0\sqcup \to \sqcup xx\,q_3\,0\sqcup \to \sqcup xx0\,q_4\,\sqcup \to \sqcup xx\,q_6\,0\sqcup.
$$

The second return trip, then a third sweep: $q_2$ moves over two $x$s, reads the single uncrossed 0 and crosses it off, and $q_3$ reads the blank and accepts:

$$
\begin{aligned}
&\sqcup x\,q_6\,x0\sqcup \to \sqcup\,q_6\,xx0\sqcup \to q_6\,\sqcup xx0\sqcup \to \sqcup\,q_2\,xx0\sqcup \\
&\to \sqcup x\,q_2\,x0\sqcup \to \sqcup xx\,q_2\,0\sqcup \to \sqcup xxx\,q_3\,\sqcup \to \sqcup xxx\sqcup\,q_{\text{accept}}\,\sqcup.
\end{aligned}
$$

So $0000$ is accepted, after 21 steps in all.

Check: $4 = 2^2$ is a power of 2, and each sweep halved the count of uncrossed 0s: 4, then 2, then 1. The simulation in the In code section counts 21 steps.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: "does not accept" is not "rejects". A TM that recognizes a language may loop on strings outside it, and a loop is not an answer. A decider has to halt on every input. When you are asked to show that a language is decidable, you must argue that your machine halts every time, usually by saying what gets smaller or what is bounded at each step.

</div>

<div class="warning" markdown>

Watch out: the blank $\sqcup$ is a tape symbol and is not an input symbol, so $\sqcup \notin \Sigma$ and $\sqcup \in \Gamma$. It is also not the same as $\varepsilon$. The string $\varepsilon$ means no symbols, and the tape holds blanks everywhere the input isn't. A machine finds the end of its input by reading a blank.

</div>

<div class="warning" markdown>

Watch out: the head cannot see the left end of the tape. A machine that moves left "until it hits the start" will stay on cell 0 forever if it has nothing to detect the end by, and it loops. That is why Example 1 puts a blank over the first 0, and why other machines mark the first cell with a special symbol.

</div>

<div class="warning" markdown>

Watch out: the Church-Turing thesis is not a theorem and can't be proved. A sentence such as "by the Church-Turing thesis there is a TM for this" is a shortcut: it means that the algorithm is described well enough that you are confident of writing the machine. It is only as good as the description. It doesn't say that TMs are fast or that they are a good way to program. It also doesn't say that every problem has an algorithm: the next lesson shows that some don't.

</div>

<div class="note" markdown>

A few conventions. Some books let the head stay put as well as move left or right (a transition to $S$). That changes nothing: a stay can be simulated by a move right followed by a move left. Some books make the tape infinite in both directions, and some give each machine its own accepting set. All the variants recognize the same languages. This book follows Sipser, with one reject state, one accept state and a tape that is infinite to the right.

</div>

## Tricks and shortcuts

- Use marks to turn a comparison into a loop: cross off one symbol on the left, travel to its partner on the right, cross it off, return. Zig-zagging like this is how $\{w\#w\}$ is decided: cross off the first symbol of $w$, then the first uncrossed symbol after the $\#$ if they match, and repeat until the left side is all crossed. Accept if the right side is crossed off too.
- A DFA is a special case: a TM that moves right on every step, never writes, and accepts when it reads the first blank in an accepting state. So every regular language is decidable. Every context-free language is decidable too, because a grammar in Chomsky normal form can be tested by a TM (the next lesson shows how).
- To check a design, trace the shortest strings first: the empty string, one symbol, the smallest string in the language and the smallest not in it. Most bugs show up there.
- To describe a machine in a proof, give the algorithm at the high level and name the data it keeps on the tape. A reader should be able to see how each step would be a few states. Use the formal level only when the details matter, as in the table above.

## In code

A TM is a dictionary and a loop. The program runs the machine of Example 1, stores the table as text, and reads it back, which is the idea of a universal machine: one fixed program that takes the description of another machine as part of its input.

<details class="code" markdown>
<summary>In code</summary>

```python
BLANK = "_"

# The machine of Example 1 as a table: (state, symbol) -> (state, symbol, direction)
TABLE = {
    ("q1", "0"): ("q3", BLANK, "R"),
    ("q2", "0"): ("q3", "x", "R"), ("q2", "x"): ("q2", "x", "R"),
    ("q3", "0"): ("q4", "0", "R"), ("q3", "x"): ("q3", "x", "R"),
    ("q3", BLANK): ("accept", BLANK, "R"),
    ("q4", "0"): ("q5", "x", "R"), ("q4", "x"): ("q4", "x", "R"),
    ("q4", BLANK): ("q6", BLANK, "L"),
    ("q5", "0"): ("q4", "0", "R"), ("q5", "x"): ("q5", "x", "R"),
    ("q5", BLANK): ("reject", BLANK, "R"),
    ("q6", "0"): ("q6", "0", "L"), ("q6", "x"): ("q6", "x", "L"),
    ("q6", BLANK): ("q2", BLANK, "R"),
}

def encode(table):
    """Write a machine as one string: one 'state,symbol,state,symbol,direction' per rule."""
    return ";".join(",".join(key + value) for key, value in sorted(table.items()))

def decode(text):
    table = {}
    for rule in text.split(";"):
        q, a, r, b, d = rule.split(",")
        table[(q, a)] = (r, b, d)
    return table

def run(description, w, start="q1", max_steps=100_000):
    """A universal machine: the description of the machine is data."""
    table = decode(description)
    tape, q, head, steps = list(w) or [BLANK], start, 0, 0
    while q not in ("accept", "reject"):
        if steps == max_steps:
            return "no halt", steps
        if (q, tape[head]) not in table:
            return "reject", steps                  # a missing rule rejects
        q, tape[head], move = table[(q, tape[head])]
        head = head + 1 if move == "R" else max(head - 1, 0)   # no move left of cell 0
        if head == len(tape):
            tape.append(BLANK)
        steps += 1
    return q, steps

desc = encode(TABLE)
print(len(desc), desc[:30])                        # 187 q1,0,q3,_,R;q2,0,q3,x,R;q2,x,q
print(run(desc, "00"), run(desc, "000"), run(desc, "0000"))
# ('accept', 7) ('reject', 4) ('accept', 21)
accepted = [k for k in range(70) if run(desc, "0" * k)[0] == "accept"]
print(accepted)                                    # [1, 2, 4, 8, 16, 32, 64]
```

</details>

## FAQ

### Is a Turing machine a real design for a computer?

No. It is a model made to be easy to reason about, and no one would program in it. The tape is infinite, which no physical machine has. What matters is that a real computer with enough memory computes the same functions, only faster. When a proof says "a TM can't do this", it means no computer can, however much memory you add.

### Why one infinite tape and one head, and not something that looks more like a computer?

Because a simpler model gives shorter proofs of impossibility. The variants (more tapes, random access, nondeterminism for recognition) are shown to recognize the same languages, so nothing is lost. Proving that something is impossible for the simplest model proves it for the stronger ones too.

### Does "halts" mean "accepts"?

No. A TM halts when it enters either the accept state or the reject state. Accepting is one way to halt. A decider always halts, either accepting or rejecting. A recognizer may fail to halt on strings outside its language.

### If the thesis can't be proved, why trust it?

Because of the evidence, and because of what it is used for. Every serious attempt to define "computable" has landed on the same class of functions, and the attempts were made independently with very different ideas. The thesis is used to move from informal algorithms to Turing machines. For impossibility results, it works the other way: a proof that no TM exists is taken as a proof that no algorithm exists, and that is the part the evidence supports most strongly.

## Practice

### Warm-up

1\. A machine is in the configuration $\sqcup 0\,q\,1\,1$ and has the transitions $\delta(q, 1) = (r, 0, L)$ and $\delta(r, 0) = (r, 1, R)$. Write the next two configurations.

<details class="solution" markdown>
<summary>Solution</summary>

The head is on the first 1. The rule writes 0, moves left and enters $r$, so the next configuration is $\sqcup\,r\,0\,0\,1$. Now the head is on the 0 that was in the second cell, and the rule $\delta(r, 0) = (r, 1, R)$ writes 1, moves right and stays in $r$, giving $\sqcup 1\,r\,0\,1$.

Check: the tape went $\sqcup 011$ to $\sqcup 001$ to $\sqcup 101$, and the head moved from cell 2 to cell 1 to cell 2.

</details>

2\. A TM has states $q_0, q_1, q_{\text{accept}}, q_{\text{reject}}$, input alphabet $\{0, 1\}$, and transitions $\delta(q_0, 0) = (q_0, 0, R)$, $\delta(q_0, 1) = (q_1, 1, R)$, $\delta(q_1, 0) = (q_0, 0, R)$, $\delta(q_1, 1) = (q_1, 1, R)$, $\delta(q_1, \sqcup) = (q_{\text{accept}}, \sqcup, R)$ and $\delta(q_0, \sqcup) = (q_{\text{reject}}, \sqcup, R)$. Trace it on $0101$ and on $10$, and describe $L(M)$.

<details class="solution" markdown>
<summary>Solution</summary>

On $0101$: $q_0\,0101 \to 0\,q_0\,101 \to 01\,q_1\,01 \to 010\,q_0\,1 \to 0101\,q_1\,\sqcup \to 0101\sqcup\,q_{\text{accept}}\,\sqcup$. Accepted.

On $10$: $q_0\,10 \to 1\,q_1\,0 \to 10\,q_0\,\sqcup \to 10\sqcup\,q_{\text{reject}}\,\sqcup$. Rejected.

The machine tracks the last symbol read: $q_1$ after a 1 and $q_0$ after a 0. It accepts at the end of the input when the last symbol was 1. So $L(M)$ is the set of strings that end in 1, and the machine is a decider, since it moves right at every step and halts at the first blank.

Check: $\varepsilon$ is rejected (the start state reads a blank in $q_0$), and $1$ is accepted.

</details>

3\. For each statement, say whether it is true: (a) every decidable language is recognizable, (b) a TM that loops on some input is not a decider, (c) if a TM recognizes $A$, the same machine with accept and reject swapped recognizes $\overline{A}$.

<details class="solution" markdown>
<summary>Solution</summary>

(a) True: a decider is a TM that recognizes the language. (b) True: a decider must halt on every input. (c) False in general. Swapping works if the machine is a decider (Theorem 1). A recognizer may loop on strings outside $A$, and the swapped machine still loops on them, so it does not accept all of $\overline{A}$.

Check: Example 3 has a machine that recognizes the strings containing a 1 and loops on the others; swapping its states changes nothing for the looping inputs.

</details>

### Standard

4\. Describe at the implementation level a TM that decides $\{w\#w : w \in \{0, 1\}^*\}$. Trace it on $01\#01$ and on $01\#00$ (in words).

<details class="solution" markdown>
<summary>Solution</summary>

The algorithm zig-zags between the two halves. First check that the input contains exactly one $\#$ (a pass to the right; reject otherwise). Then repeat: move to the leftmost symbol not yet crossed off, remember it (in the state) and replace it by $x$; move right past the $\#$ to the leftmost symbol not yet crossed off after it; if it equals the remembered symbol, replace it by $x$, and otherwise reject; return to the left end. When no uncrossed symbol is left before the $\#$, check that none is left after it either, and accept if so, reject otherwise. The machine halts on every input: each round crosses off two symbols, so there are at most $n/2$ rounds.

On $01\#01$: round 1 crosses off the 0 on each side, round 2 the 1 on each side, nothing is left on either side, so it accepts. On $01\#00$: round 1 matches the 0s, and in round 2 the machine remembers 1 and finds 0 after the $\#$, so it rejects.

Check: the lengths matter too. On $01\#0$, round 2 finds a blank after the $\#$ where it needs a 1, and rejects; on $0\#01$, the left side is used up with symbols left on the right, and the final check rejects.

</details>

5\. Show that every regular language is decidable by a TM, by turning a DFA $D = (Q, \Sigma, \delta_D, q_0, F)$ into a decider.

<details class="solution" markdown>
<summary>Solution</summary>

What we want: a TM $M$ that halts on every input and accepts exactly $L(D)$. The plan: let the states of $M$ be the states of $D$ and have $M$ read the input once, moving right, with the DFA's transition in the TM's.

*Construction.* Use the states $Q$ together with $q_{\text{accept}}$ and $q_{\text{reject}}$, start state $q_0$, and tape alphabet $\Sigma \cup \{\sqcup\}$. For each $q \in Q$ and $a \in \Sigma$, put $\delta(q, a) = (\delta_D(q, a), a, R)$. For each $q \in F$, put $\delta(q, \sqcup) = (q_{\text{accept}}, \sqcup, R)$, and for each $q \notin F$ put $\delta(q, \sqcup) = (q_{\text{reject}}, \sqcup, R)$.

On an input of length $n$, $M$ takes $n$ steps to read the input and one more to reach the first blank, then halts, so it is a decider. After $n$ steps it is in the state $\delta_D^*(q_0, w)$, so it accepts exactly when $D$ does. $\blacksquare$

Check: for the DFA of "ends in 01", the machine accepts $1101$ and rejects $0110$ after reading all four symbols.

</details>

6\. Why does the simulation of an NTM by a deterministic machine search the computation tree breadth-first, and not by depth-first search?

<details class="solution" markdown>
<summary>Solution</summary>

A computation tree can have an infinite branch: a branch where the NTM runs forever. A depth-first search that enters this branch never leaves it, so it never reaches an accepting node on another branch, and the deterministic machine would fail to accept a string that the NTM accepts. Breadth-first search examines every node of depth $d$ before any of depth $d + 1$. An accepting node at some finite depth is found after finitely many nodes.

Check: take an NTM with two branches at the start, one looping and one accepting after 3 steps. Breadth-first search finds the accepting branch in the third level. Depth-first search that tries the looping branch first never does.

</details>

### Challenge

7\. Prove that if $A$ and $B$ are decidable, then $A \cup B$ is decidable. Then prove that if $A$ and $B$ are Turing-recognizable, then $A \cup B$ is recognizable, and explain why the first argument does not work for the second claim.

<details class="solution" markdown>
<summary>Solution</summary>

*Decidable.* Let $M_A$ and $M_B$ be deciders. On input $w$, run $M_A$ on $w$; it halts. If it accepts, accept. Otherwise run $M_B$ on $w$; it halts. Accept if it does, and reject otherwise. This halts on every input and accepts exactly $w \in A \cup B$. $\blacksquare$

*Recognizable.* Let $M_A$ and $M_B$ be recognizers. The machine above fails: if $M_A$ loops on $w$ but $M_B$ accepts it, the first machine never gets to $M_B$. Instead run both at the same time, one step of $M_A$, then one step of $M_B$, and so on (on two tapes, which is allowed by Theorem 2). Accept as soon as either accepts. If $w \in A \cup B$, one of them accepts after finitely many steps, and the combined machine accepts. If $w \notin A \cup B$, neither accepts, so the combined machine does not. $\blacksquare$

Check: $A$ = strings containing a 1 (Example 3's machine, which loops on strings of 0s) and $B$ = all strings ending in 0 (a decider). On $00$, $M_A$ loops, $M_B$ accepts, and the parallel machine accepts in a few steps; running $M_A$ first would never end.

</details>

8\. (Reviews [cardinality and countability](../../04-proofs-and-logic/06-relations-and-functions/06-cardinality-and-countability.md).) Prove that the set of all Turing machines is countable.

<details class="solution" markdown>
<summary>Solution</summary>

What we know: each TM can be written as a finite string $\langle M \rangle$ over a fixed finite alphabet (its states, symbols and transitions, written out with separators), and different machines give different strings. What we want: an injection from the set of TMs into a countable set. The plan: use Lemma 1 and Theorem 8 of the cardinality lesson.

*Proof.* Let $\Sigma_0$ be a finite alphabet in which all machine descriptions are written. The map $M \mapsto \langle M \rangle$ is an injection from the set of Turing machines into $\Sigma_0^*$. The set $\Sigma_0^*$ is countably infinite (list the strings by length, and alphabetically within one length), and an injection into a countable set makes the domain countable (Lemma 1). So there are countably many Turing machines. $\blacksquare$

Check: in the In code section, `encode` turns a machine into a string, and two machines with different tables give different strings, because `decode` recovers the table.

</details>

## Where this shows up

- The next lesson, [decidability and the halting problem](05-decidability-and-the-halting-problem.md), uses everything here: encodings $\langle M, w \rangle$, machines that simulate other machines, and the gap between recognizing and deciding. [Reductions and undecidability](06-reductions-and-undecidability.md) builds machines out of other machines' descriptions.
- Running time is counted in Turing machine steps in [P, NP and NP-completeness](07-p-np-and-np-completeness.md). The $t^2$ cost of the multitape simulation and the exponential cost of the nondeterministic one are the reason that lesson cares which model it uses.
- Unary notation, where $n$ is written as $n$ marks, is the input format for the first examples: the language $\{0^{2^n}\}$ here is a question about numbers in unary, and [number bases and conversions](../01-number-representation/01-number-bases-and-conversions.md) explains why the size of an input depends on the base.
