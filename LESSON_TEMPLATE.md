# Lesson template

Copy the skeleton below into a new lesson file and fill it in. Read `STYLE.md` first; every rule there applies.

## Two sizes

**Full lessons** (middle school and up) use every section below.

**Compact lessons** (most of `01-elementary`, and anything the reader likely half-knows) drop the faded example, "In code" and "FAQ", keep the explanations short, and have about 5 practice problems instead of 8.

## Section rules

| Section | What goes in it |
|---|---|
| Title and goal | Title in sentence case. One line: "After this lesson you can ...". Then prerequisite links. |
| Quick check | 3 problems that test the whole lesson. Answers in one collapsible box. "All three right? Skip to Practice." |
| The idea | A concrete situation first, a picture if it helps, then the idea in plain words. No formal definitions yet. |
| Definitions | Each term in bold once, stated formally, then restated in plain words or with a tiny example. |
| How to do it | Numbered steps (a method) or a theorem with its proof framed as: what we know, what we want, plan, proof, look back. |
| Worked examples | Example 1 explained at every step, ending with a check. Examples 2 and 3 with less commentary: one variation, one edge case. In full lessons, one more example leaves the last step or two for the reader. |
| Edge cases and common mistakes | Zero, negatives, empty cases, division by zero, untidy answers. Each mistake shown next to the step where it happens. |
| Tricks and shortcuts | Mental math, memory aids, quick checks. Only real ones. |
| In code | Optional. Short Python, only when the idea maps naturally to code. Every snippet must run. |
| FAQ | Real "why" and "what if" questions a learner asks. 2 to 5 of them. |
| Practice | About 8 problems: 3 warm-up, 3 standard, 2 challenge (one of them reviews an earlier lesson). Each problem has its own collapsible solution with full steps, ending with a check. |
| Where this shows up | 1 to 3 short lines on where the idea is used later: later lessons, CS courses, economics, money. |

There is no summary at the end of a lesson. The chapter's `index.md` cheat sheet collects the rules and formulas.

## Links to lessons that don't exist yet

Only link to pages that already exist. When you mention a planned lesson that hasn't been written, write its name in plain text and put the planned path in an HTML comment right after it, so the link can be added later with a search:

```markdown
You will use this again in modular arithmetic<!-- link: ../06-cs-math/02-number-theory/01-divisibility-and-modular-arithmetic.md -->.
```

## Skeleton

````markdown
# Lesson title

After this lesson you can do one specific, concrete thing.

Before this: [prerequisite lesson](../path/to/lesson.md).

## Quick check

Try these first. If you get all three right, skip to [Practice](#practice).

1. First problem.
2. Second problem.
3. Third problem.

<details class="solution" markdown>
<summary>Answers</summary>

1. Answer, with one line of working.
2. Answer.
3. Answer.

</details>

## The idea

A concrete situation the reader can picture. Then the idea in plain words.

## Definitions

A **term** is the formal definition, in standard wording.

In plain words: the same idea said simply, or a tiny example.

## How to do it

1. First step.
2. Second step.
3. Check the answer.

## Worked examples

<div class="example" markdown>

### Example 1: what it shows

Every step explained, using the step numbers above.

Check: substitute back or estimate.

</div>

<div class="example" markdown>

### Example 2: a variation

Less commentary than Example 1.

</div>

<div class="example" markdown>

### Example 3: an edge case

The unusual case, worked out.

</div>

<div class="example" markdown>

### Example 4: finish it yourself

The first steps are done. The last step is left for you.

<details class="solution" markdown>
<summary>Finish</summary>

The last step, and the check.

</details>

</div>

## Edge cases and common mistakes

<div class="warning" markdown>

Watch out: the mistake, why it is wrong, and the fix.

</div>

## Tricks and shortcuts

A real shortcut, with one example of it.

## In code

One line on what the code shows.

<details class="code" markdown>
<summary>In code</summary>

```python
print("every snippet must run")
```

</details>

## FAQ

### A real question a learner asks?

The answer, in a few sentences.

## Practice

### Warm-up

1. Problem.

<details class="solution" markdown>
<summary>Solution</summary>

Full steps, then the check.

</details>

### Standard

4. Problem.

<details class="solution" markdown>
<summary>Solution</summary>

Full steps, then the check.

</details>

### Challenge

7. Problem.

<details class="solution" markdown>
<summary>Solution</summary>

Full steps, then the check.

</details>

## Where this shows up

- One later use, linked if the page exists.
````
