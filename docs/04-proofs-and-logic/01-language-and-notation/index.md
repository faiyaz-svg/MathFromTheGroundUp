# Language and notation

What a proof is, the vocabulary of a math text, the phrases a proof is written in, and how to read the symbols.

1. [What is a proof](01-what-is-a-proof.md)
2. [Definitions, theorems, lemmas and corollaries](02-definitions-theorems-lemmas-corollaries.md)
3. [Proof language: let, suppose, WLOG](03-proof-language-let-suppose-wlog.md)
4. [Reading math symbols](04-reading-math-symbols.md)

## Cheat sheet

### What is a proof

A proof is a finite sequence of statements ending in the claim, where each statement is a hypothesis, a definition or axiom, or follows from earlier ones by a step the reader accepts. It must be checkable line by line by a classmate who knows the course.

| Kind of claim | One example | One counterexample |
|---|---|---|
| universal ("for every ...") | supports it, proves nothing | disproves it |
| existential ("there is ...") | proves it, if checked | disproves nothing |

- Patterns break. The expression $n^2 + n + 41$ is prime for $n = 0, \dots, 39$ and equals $41^2 = 1681$ at $n = 40$. The regions cut by chords of $n$ points on a circle go $1, 2, 4, 8, 16, 31$.
- Checking every case is a proof only when the set of cases is finite and you really run through all of it.
- A proof is rigorous when each step rests on a definition, an axiom or an earlier result, never on a picture or a feeling.

Method for "if $P$, then $Q$":

1. Write the claim as "if $P$, then $Q$" and test a small case.
2. Name the objects with letters and give their types.
3. Unpack every definition in the hypothesis.
4. Say what you must show for the conclusion, by unpacking its definition.
5. Connect the two with justified steps.
6. State why the last line matches the definition, then end.
7. Reread each line as your classmate would.

Model proof: if $m = 2j$ and $n = 2k$, then $m + n = 2(j + k)$, and $j + k$ is an integer, so $m + n$ is even.

Main mistakes:

- Proving a claim from examples, or from a test run of any size.
- Reusing one letter for two integers: $m = 2k$ and $n = 2k$ forces $m = n$.
- Starting at the conclusion.
- Proving a special case ("Let $m = 4$").

### Definitions, theorems, lemmas and corollaries

| Word | Meaning |
|---|---|
| definition | an agreement about what a word means; neither true nor false |
| axiom, postulate | accepted without proof as a starting rule |
| theorem | a proved main result |
| proposition | a proved result, usually smaller |
| lemma | a proved result used to prove a bigger one |
| corollary | a result that follows quickly from one just proved |
| conjecture | believed but unproved (Goldbach's: every even integer above 2 is a sum of two primes) |
| claim | a statement proved inside a proof |
| remark, example | commentary and illustration; neither proves anything |

The working definitions. Given one, you get the witness (an integer $k$, say); to prove one, you produce it.

| Word | Definition |
|---|---|
| $n$ even | $n = 2k$ for some integer $k$ |
| $n$ odd | $n = 2k + 1$ for some integer $k$ |
| $a \mid b$ | $b = ak$ for some integer $k$ |
| $p$ prime | $p > 1$, and the only positive divisors of $p$ are 1 and $p$ |
| $r$ rational | $r = \frac{a}{b}$ with integers $a$, $b$ and $b \ne 0$ |

- In a definition, "if" means "if and only if". In a theorem, "if" is one-way.
- The first move of nearly every proof is to write the definitions down with fresh letters.
- Edge cases: $0$ is even, $a \mid 0$ for every $a$, $0 \mid b$ only for $b = 0$, $1$ is not prime, $-7$ is odd and not prime.
- Divisibility chain: if $a \mid b$ then $a \mid bm$ (lemma); if $a \mid b$ and $a \mid c$ then $a \mid bx + cy$ (theorem); so $a \mid b + c$ and $a \mid b - c$ (corollary). Also, if $a \mid b$ and $b \mid c$ then $a \mid c$.
- The sum and product of two rationals are rational, and so is $\frac{1}{r}$ for a rational $r \ne 0$.

Main mistakes:

- Using a half-remembered definition, for example dropping $p > 1$ or $b \ne 0$.
- Letting the witness $k$ be a non-integer ($3 = 2 \times 1.5$ does not make 3 even).
- Reading $a \mid b$ backwards: $3 \mid 12$ is true and $12 \mid 3$ is false.
- Citing a result that comes later and depends on the claim.

### Proof language: let, suppose, WLOG

| Phrase | What it does |
|---|---|
| let, fix | introduces an object, with its type |
| suppose, assume | opens an assumption (hypothesis, case, contradiction) |
| then, so, thus, hence, therefore | draws a conclusion from lines already on the page |
| by definition | unpacks a named definition |
| there exists, for some | gives a witness, or asks for one |
| for every, for each | says something holds for all members of a set |
| such that | attaches a property to a new object |
| without loss of generality | narrows to one case by symmetry |
| as required, $\blacksquare$ | the last line is the claim |

Moves with quantifiers:

| Statement | To prove it | When it is given |
|---|---|---|
| for every $x$ in $S$, $P(x)$ | let $x$ be arbitrary in $S$; prove $P(x)$ | pick any element you like |
| there exists $x$ with $P(x)$ | produce a witness; check $P(x)$ | name such an $x$; use only $P(x)$ |

- "Let $n$ be an integer" is arbitrary and covers every integer. "Let $n = 3$" is one value.
- Name an object before you use it. Different objects get different letters. A letter obtained inside a case belongs to that case.
- First line by shape of claim: "for every $x$" starts with "Let $x$ be ..."; "if $P$ then $Q$" starts with "Suppose $P$"; "there exists" starts with a choice.
- WLOG needs the claim to be unchanged when the objects are swapped (symmetric). Say the reason. Prove the one case completely.
- The words "clearly", "obviously" and "it is easy to see" mean "the author skipped a routine step". Supply the step when you read, and don't use them when you write.

Main mistakes:

- WLOG on a claim that isn't symmetric, such as "if $ab$ is even, then $a$ is even" (false: $a = 3$, $b = 2$).
- Swapping the order of "for every" and "there exists": every $x$ has a bigger $y$, but no $y$ is bigger than every $x$.
- A "thus" with nothing before it to follow from.
- Carrying a case's assumption into another case.

### Reading math symbols

Every expression is an object (a number, a set) or a statement (true or false). Operations build objects. Relations build statements. Mixing them, as in $3 \mid 12 = 4$, is a type error.

| Symbol | Say it |
|---|---|
| $\forall x \in A$ | for every $x$ in $A$ |
| $\exists x \in A$ | there exists an $x$ in $A$ |
| $\exists!\, x$ | there exists exactly one $x$ |
| $\neg P$, $P \wedge Q$, $P \vee Q$ | not $P$; $P$ and $Q$; $P$ or $Q$ (inclusive) |
| $P \Rightarrow Q$, $P \Leftrightarrow Q$ | $P$ implies $Q$; $P$ if and only if $Q$ |
| $x \in A$, $A \subseteq B$ | $x$ is in $A$; $A$ is a subset of $B$ |
| $\{x \in A : P(x)\}$ | the set of $x$ in $A$ such that $P(x)$ |
| $a \mid b$, $a \nmid b$ | $a$ divides $b$; $a$ does not divide $b$ |
| $\sum_{i=1}^{n} a_i$, $\prod_{i=1}^{n} a_i$ | the sum, the product, of $a$ sub $i$ for $i$ from 1 to $n$ |
| $f \colon A \to B$, $x \mapsto f(x)$ | $f$ is a function from $A$ to $B$; $x$ maps to $f(x)$ |
| $f \circ g$ | $f$ after $g$: apply $g$ first |
| $\lfloor x \rfloor$ | the floor of $x$: round down ($\lfloor -3.7 \rfloor = -4$) |
| $:=$, $\equiv$ | is defined to be; is logically equivalent to |

- Read quantifiers left to right. $\forall x\ \exists y\ (y > x)$ is true over $\mathbb{R}$, and $\exists y\ \forall x\ (y > x)$ is false.
- The index of a sum and the letter after $\forall$ are bound variables: they exist only inside the expression, and renaming them changes nothing.
- A sum with no terms is 0, and a product with no terms is 1. A "for every" over the empty set is true, and a "there exists" over it is false.
- To translate English into symbols: find the objects, find the quantifier words in order, write the condition, bracket it, then read it back.
- Book rule: write the logic in words and keep symbols for formulas. Never start a sentence with a symbol.

Main mistakes:

- Treating $\Rightarrow$ as "therefore". It is a statement, and it can be false.
- Using a bound letter outside its expression.
- Writing $\forall x\ P(x) \Rightarrow Q(x)$ without brackets.
- Mixing up $\in$ (element) and $\subseteq$ (subset), or $x_2$ (index) and $x^2$ (square).
- Trusting a symbol's meaning across books: $\mathbb{N}$, $\subset$, $\equiv$ and the bar all vary.
