# How to use this book

This book rebuilds the math that university courses take for granted, from grade 1 arithmetic up to proofs, calculus, linear algebra, CS math, economics math and Canadian personal finance. It is written for a CS student with an economics minor who can already do a lot of math, but keeps hitting missing basics and unfamiliar terms in proof-heavy courses. The aim is a solid base and good problem-solving habits, without reading every page.

You don't have to start at the beginning. Every folder opens with a quiz that shows which lessons you can skip, and every lesson opens with three questions that let you skip most of it.

## Read these first

- [How to read math](how-to-read-math.md) shows how to read a definition, a theorem, a line of notation and a worked example.
- [How to study](how-to-study.md) explains the study habits this book is built around, and the research behind them.
- [Problem-solving playbook](problem-solving-playbook.md) gives Polya's four steps and ten moves to try when you don't know how to start.

## The folders, in reading order

Proofs come right after high school because every later folder uses them.

| Folder | What it covers |
|---|---|
| [01-elementary](../01-elementary/index.md) | Place value, the four operations, long division, primes, fractions, decimals, units, area. Short lessons. |
| [02-middle-school](../02-middle-school/index.md) | Integers, ratios and percents, equations and inequalities, exponents, linear functions, geometry, basic probability. |
| [03-high-school](../03-high-school/index.md) | Set notation, functions, polynomials, logarithms, geometry proofs, trigonometry, sequences, sums and counting. |
| [04-proofs-and-logic](../04-proofs-and-logic/index.md) | Proof language, logic and sets, proof methods, induction, relations and functions, countability. |
| [05-university-core](../05-university-core/index.md) | Calculus, series, linear algebra, probability, statistics, and a little multivariable calculus and differential equations. |
| [06-cs-math](../06-cs-math/index.md) | Number bases and bits, number theory, counting, recurrences and asymptotics, graphs, theory of computation. |
| [07-economics-math](../07-economics-math/index.md) | GDP, inflation and growth rates, supply and demand, marginal analysis, present value, game theory. |
| [08-financial-math](../08-financial-math/index.md) | Interest, loans, mortgages, investing, RRSP, TFSA and FHSA, income tax, with Ontario rules. |
| [reference](../reference/index.md) | Glossary, symbols and notation, common mistakes, formula index. |

## How each folder works

Every folder has two pages in front of its lessons.

The index page (`index.md`) is the overview. It lists the lessons in order, marks the fast path and the optional lessons, and links the folder's Anki deck. In 01-elementary it also holds the cheat sheet, the rules and tricks from every lesson on one page. In the other folders, each chapter's index page has its own cheat sheet.

The diagnostic (`diagnostic.md`) is a short quiz on the whole folder, and each question names the lesson it tests. Take it without notes and mark each answer right, wrong or guessed. Then do only the lessons behind the wrong and guessed questions. A lucky guess still counts as wrong.

## How a lesson is laid out

Each lesson opens with a one-line goal ("After this lesson you can ...") and links to the lessons it builds on. The sections then come in the same order every time:

| Section | What it gives you |
|---|---|
| Quick check | Three problems covering the whole lesson, answers hidden. All three right means you skip to Practice. |
| The idea | A concrete situation, then the idea in plain words. |
| Definitions | Each term stated formally, then again in plain words. |
| How to do it | The method as numbered steps, or a theorem with its proof. |
| Worked examples | Example 1 explained at every step; later ones lighter; one leaves its last step for you. |
| Edge cases and common mistakes | Zero, negatives, empty cases, and each mistake at the step where it happens. |
| Tricks and shortcuts | Mental math and memory aids, where real ones exist. |
| In code, FAQ | In some lessons: short Python, and "why" and "what if" questions. |
| Practice | About eight problems in three tiers: warm-up, standard, challenge. One challenge problem reviews an earlier lesson. |
| Where this shows up | Where the idea comes back: later lessons, CS, economics, money. |

The 01-elementary lessons are shorter, with about five practice problems. Solutions sit in boxes that stay closed until you click them. Try each problem before you open its box ([how to study](how-to-study.md) explains why).

## Fast paths and optional lessons

A folder's index page marks a fast path (the lessons that later folders lean on most) once that folder is written; the proofs folder already has one. If you are short on time, do the fast path first and come back for the rest when a course needs it. Optional lessons, such as conic sections, can wait until a course uses them.

## Tracking your progress

The [progress page](../progress.md) lists every lesson with a checkbox. On the site, click a box to tick it. Ticks are saved in your browser, so each browser on each device keeps its own list, and clearing the browser's data for the site clears them. In VS Code, tick a lesson by changing `[ ]` to `[x]` in the file.

## Anki decks

Anki is a free flashcard app that schedules reviews for you: a card you know comes back after a longer gap each time, and a card you miss comes back soon. Each folder gets a deck once its lessons are written.

1. Download the folder's `.apkg` file from its index page.
2. Import it. In Anki desktop, choose File, then Import. On Android, open the file with AnkiDroid (free); on an iPhone or iPad, open it with AnkiMobile (paid).
3. Review for a few minutes every day. Short daily reviews beat one long weekly session, for the reasons in [space it out](how-to-study.md#space-it-out).

A free AnkiWeb account keeps your reviews in sync across devices. When a deck gets new cards, import it again: Anki updates the cards you have and adds the new ones.

## Reading in VS Code

Open the book's folder in VS Code, open a lesson and press Ctrl+Shift+V. The preview shows the math typeset and the solution boxes working. Ctrl+K and then V opens the preview beside the source. Mermaid diagrams also need the Markdown Preview Mermaid Support extension.

With Claude Code open in VS Code, you can ask about the page in front of you:

- "Explain step 3 of Example 2 in this lesson another way."
- "Give me three more problems like practice problem 5, with hidden solutions."
- "Here is my working for problem 7. Which line is wrong?"

Paste your whole working, so the mistake can be found at the line where it happens. The repo's `CLAUDE.md` tells Claude to follow `STYLE.md`, so anything it adds matches the book.

## A fast route for a CS student

1. Read [how to read math](how-to-read-math.md) and the [problem-solving playbook](problem-solving-playbook.md). Skim [how to study](how-to-study.md) and set up Anki.
2. Take the diagnostics for [01-elementary](../01-elementary/diagnostic.md), [02-middle-school](../02-middle-school/diagnostic.md) and [03-high-school](../03-high-school/diagnostic.md). Do only the lessons you miss, and use each lesson's quick check to skip what you know.
3. Do [04-proofs-and-logic](../04-proofs-and-logic/index.md) in full, in order. Discrete math, algorithms, theory of computation and linear algebra all ask you to read and write proofs, and this is the folder that teaches it.
4. Take the diagnostics for 05-university-core<!-- link: ../05-university-core/diagnostic.md --> and 06-cs-math<!-- link: ../06-cs-math/diagnostic.md -->, and do the lessons you miss, starting with the chapters your current courses use.
5. Use 07-economics-math and 08-financial-math when an economics course or a money decision (a car loan, a mortgage, a TFSA) needs them.

When a course needs a topic you haven't reached, go straight to that lesson. Its quick check and prerequisite links show which earlier gaps to fill first.
