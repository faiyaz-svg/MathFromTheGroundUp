# Writing style

These rules apply to every page in `docs/`. The reader is a capable adult (a university CS student with an economics minor) who has gaps in their math base. Don't talk down to them, and don't assume they already know the background.

The goal of each page is that the reader can do something new by the end of it, and understands why it works.

## Voice

- Talk to the reader as "you" in instructions ("Write the 1 above the 9"). Use "we" when working through something together ("We want to show that...").
- Explanations are plain and direct. Definitions and theorems are stated precisely, in the standard wording a university course would use, so the reader also learns to read real textbooks.
- Active voice, present tense, plain verbs: "divide", not "perform a division"; "use", not "utilize".
- Be modest. Don't praise the material ("this beautiful result") and don't hype it.
- Use Canadian spelling: colour, centre, labour, practise (the verb) and practice (the noun). Keep the original spelling in names and titles ("National Center for Education Research").

## How to explain

1. Start with something concrete: a real situation or a small example, then a picture if one helps, then plain words, then the formal definition. At university level keep the concrete part short.
2. The first time a symbol appears, say what it means in words: "$\Sigma$ means add up all the terms".
3. Start from what the reader already knows, and say where an analogy stops working.
4. Give the method as numbered steps, then refer to the step numbers in the examples ("Step 3: bring down the next digit").
5. Explain Example 1 fully. Later examples get less commentary, and one example leaves the last step (or the last two) for the reader.
6. End every worked solution with a check: substitute back, estimate, or multiply out.
7. Name a common mistake at the step where it happens, not only in a separate list.
8. Include untidy answers on purpose (fractions, negatives, remainders) and say that they are fine.
9. State each definition twice, once formally and once in plain words or with an example.
10. Frame each proof: what we know, what we want, the plan, the proof, a look back. If a proof uses contradiction, say so before it starts.
11. Never write "clearly", "obviously", "it is easy to see" or "trivially" (except in the proofs lesson that explains what those words mean in textbooks). Show the step instead.
12. Keep one idea per paragraph, in 2 to 5 sentences.
13. Aim for about 20 words per sentence on average, never more than about 40, and vary the length. A short sentence after a long one is fine. A page of identical short sentences reads like a machine wrote it.
14. Put labels next to what they label: beside the equation line or inside the diagram, not "see the figure above".
15. Leave out decoration. No fun facts, history asides or images that don't teach the idea.

## Writing math in sentences

These come from Knuth, Larrabee and Roberts, *Mathematical Writing*, and Halmos, *How to Write Mathematics*.

- Put words between separate formulas. Not "Consider $S_q$, $q < p$" but "Consider $S_q$, where $q < p$".
- Don't start a sentence with a symbol. Not "$x$ is even" but "The number $x$ is even".
- In prose, write "for every", "there exists", "implies" and "therefore" as words. The symbols $\forall$, $\exists$, $\Rightarrow$ and $\therefore$ appear only in the logic lessons, where the symbols are the subject.
- The sentence before a displayed formula is either complete or ends with a colon.
- The "blah" test: the sentence should still read well if each formula is replaced by "blah".
- Connect steps with words ("Subtract 7 from both sides:"). Don't list formulas one after another like homework.
- One letter keeps one meaning across the whole book. Check `docs/reference/symbols-and-notation.md` before choosing a letter.
- One term per concept. If the book says "numerator", it never also says "top number" or "upper term" for the same thing, except once when introducing the term ("the numerator, the number on top").
- Use "each" or "every" instead of "any" when you mean all of them.

## Markdown that works on the site and in VS Code

The same files are read in VS Code's preview (KaTeX) and built into the website (Zensical + KaTeX). These rules keep both working.

### Math

- Inline math: `$x^2$`. No space just inside the dollar signs.
- Display math: `$$` on its own line, with a blank line before and after the block, and no blank lines inside it.
- Multi-line work: `$$\begin{aligned} ... \end{aligned}$$`.
- Never use `\(...\)` or `\[...\]` in the source.
- Don't put a letter or digit right after a closing `$`: write `$n$-th`, not `$n$th`.
- Inside a table, write absolute value as `\lvert x \rvert` and "divides" as `\mid`, because a plain `|` ends the table cell.
- Minus signs belong inside math: write `$-3$`, never a hyphen or dash on its own.

### Money

Always escape the dollar sign in money amounts: `\$12.50`. An unescaped `$` can turn the text after it into math.

### Boxes

Use HTML containers with the `markdown` attribute. Leave a blank line after the opening tag and a blank line before the closing tag, or the content inside won't be processed.

Worked example (gray box):

```html
<div class="example" markdown>

### Example 1: dividing 91 by 7

...

</div>
```

Note (pale yellow) and warning (pale red):

```html
<div class="note" markdown>

...

</div>

<div class="warning" markdown>

...

</div>
```

Collapsible solution, and collapsible code:

```html
<details class="solution" markdown>
<summary>Solution</summary>

...

</details>

<details class="code" markdown>
<summary>In code</summary>

...

</details>
```

Don't use `!!!`, `???` or `===` blocks. They need indented content, which VS Code shows as a raw code block.

### Links, headings and diagrams

- Link between pages with relative paths to the `.md` file: `[long division](../01-elementary/07-long-division.md)`.
- Keep math and punctuation out of headings that other pages link to, so the anchor stays stable.
- Mermaid code blocks for trees, graphs, flowcharts and automata. Generated SVG files (from `tools/figures/`) for geometry and function plots.

## Patterns to avoid

These are signs of AI-generated text, collected from Wikipedia's "Signs of AI writing" page (including its 2026 updates) and from studies of words that language models overuse (Kobak et al. 2024; Juzek and Ward 2025; Liang et al. 2024). One or two of them can appear by chance in human writing; the problem is when they pile up. Treat them as hard rules here anyway, because the whole book is drafted with AI help and would otherwise drift toward them.

### Words: never use

delve, tapestry, testament, pivotal, underscore (as a verb), intricate, intricacies, meticulous, meticulously, showcase, garner, bolster, interplay, vibrant, multifaceted, realm, groundbreaking, renowned, nestled, seamless, seamlessly, commendable, noteworthy, invaluable, transformative, unparalleled, unveil, harness, elucidate, burgeoning, foster, leverage (as a verb), quietly, deep dive, boasts, "key role", "key factor", "key takeaway", "key insight", "key concept".

Technical senses are allowed: the underscore character, robust statistics, financial leverage, a primary key or encryption key, steady state, critical point, statistical significance, spanning tree, "the inequality holds".

### Words: use rarely

crucial, vital, essential, comprehensive, notably, additionally, moreover, furthermore, consequently, ultimately, enhance, valuable, insights, practical, remarkable, nuanced, significant (outside statistics), robust (outside statistics). Prefer a plain word: "needed", "also", "so", "big".

### Phrases and patterns: never use

- "serves as", "stands as", "functions as" where "is" works. Write "The remainder is the amount left over", not "The remainder serves as...".
- Inflated importance: "plays a crucial role", "is a testament to", "is a cornerstone of", "sets the stage for", "marks a shift".
- A trailing "-ing" clause that adds vague commentary: "..., highlighting the importance of place value", "..., underscoring...", "..., showcasing...".
- Disclaimers: "It's important to note that", "It's worth noting", "It is worth mentioning". State the warning directly instead: "Watch out: ...".
- Summary endings: a closing paragraph starting "In summary", "In conclusion", "To sum up" or "Overall,". Pages end with practice and "Where this shows up", not a recap.
- Chatbot lines: "Great question", "Certainly!", "Let's dive in", "Let's unpack this", "I hope this helps", "Let me know". Plain "Let's check the answer" is fine.
- Vague attribution: "mathematicians agree", "experts say", "it is widely believed". Name the source or drop the claim.
- Negative parallelism: "not only X but also Y", "it's not X, it's Y", "no X, no Y, just Z". The one exception is correcting a specific mistake: "$-3^2$ is $-9$, not $9$".
- False ranges: "from X to Y" where X and Y are not two ends of one scale ("from counting sheep to designing algorithms"). Real ranges are fine: "from 0 to 1", "from left to right".
- Groups of three used for rhythm ("clear, simple, and powerful"). A real list of three things is fine.
- Hedging about sources: "while details are limited", "based on available information".

### Punctuation and characters

- Em dashes (—) almost never: at most one per 500 words, and never with spaces around them. Studies cited on Wikipedia found Claude uses em dashes more than professional writers do, so this takes active effort. Use a comma, a colon, parentheses or a new sentence instead.
- En dashes (–) only in numeric ranges ("pages 10–12"), or write "10 to 12".
- Straight quotes and apostrophes only (`"` and `'`). Curly ones also break math like `f'(x)`.
- No emoji, and no unicode bullets (•). Use Markdown `-` lists.
- Few exclamation marks in prose. (In math, $n!$ is a factorial and is fine.)

### Formatting

- Headings are in sentence case: "How to do it", not "How To Do It". Proper nouns keep their capitals: Pythagorean theorem, Bayes' theorem, Euclid's algorithm, Ontario.
- A term is bold once, where it is defined, and nowhere else. Don't use bold for emphasis.
- Don't write bullet lists where every item starts with a bold label and a colon. Use a sentence, a table or a real subheading.
- Each page has one H1 (the title). Don't skip heading levels (H2 straight to H4).
- Don't put `---` lines between sections.
- Use a list for real steps or real collections of items. If prose reads fine, use prose.
- Use tables for real tables of values (place value, times tables, amortization schedules, symbol lists). A two-row table that should be a sentence should be a sentence.

### Don't over-correct

Wikipedia now also flags the opposite extreme: text that never uses a dash or a semicolon, uses only commas and periods, and keeps every sentence between 8 and 20 words. Write like a person explaining at a whiteboard: plain "is" and "has" sentences, a colon or semicolon or parentheses where they fit, an occasional "usually" or "often", and sentences of different lengths.

## Changing numbers (finance and economics)

Tax brackets, HST, contribution limits, CMHC premiums, land transfer tax rates and similar figures change every year. Each lesson that uses one:

- takes it from an official source (canada.ca, ontario.ca, cmhc-schl.gc.ca, statcan.gc.ca),
- states the year ("2026 federal brackets"),
- links the source at the point of use.

## Self-check before a page is committed

1. Search the file for `—`, `“`, `”`, `‘`, `’`, emoji, and every word in "never use".
2. Search for "serves as", "stands as", "important to note", "worth noting", "In summary", "In conclusion", "Overall,", "not only", "Let's dive".
3. Check headings for Title Case and lists for bold "Label:" items.
4. Recompute every answer, worked example and table value in Python.
5. Run every code block in "In code" boxes.
6. Read the page once from top to bottom for rhythm. If several sentences in a row have the same length and shape, rewrite some of them.
