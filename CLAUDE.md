# Math From the Ground Up

A self-study math textbook for one reader: a 4th-year CS student (economics minor, Ontario) filling gaps in their math base, from grade 1 arithmetic to university math, proofs, CS math, economics math and Canadian personal finance. The Markdown in `docs/` is published to https://faiyaz-svg.github.io/MathFromTheGroundUp/ and also read directly in VS Code.

## Rules to follow

- Writing: `STYLE.md`. Every page must follow it, including the list of AI-writing patterns to avoid. Em dashes are the most common slip.
- Lesson structure: `LESSON_TEMPLATE.md`.
- Site look: `DESIGN.md`.
- Don't make decisions the reader hasn't agreed to. Ask first when a change goes beyond what was requested.

## Layout

- `docs/00-start-here` to `docs/08-financial-math`: the book, in reading order. `docs/reference`: glossary, symbols, common mistakes, formula index.
- Each folder has `index.md` (overview and cheat sheet) and `diagnostic.md`. Each chapter subfolder has an `index.md` cheat sheet.
- Lesson files are numbered: `docs/02-middle-school/02-ratios-rates-percents/03-percents.md`.
- `mkdocs.yml` holds the site config and the `nav`. A new page must be added to `nav` and to `docs/progress.md`.
- `anki/cards/<folder>.tsv` -> `anki/build_decks.py` -> `docs/downloads/anki/<folder>.apkg`.
- `tools/figures/` holds the scripts that draw SVG figures into `docs/assets/figures/`.

## Commands (Windows, Git Bash)

```bash
py -m venv .venv
.venv/Scripts/python -m pip install -r requirements-dev.txt
.venv/Scripts/zensical serve        # preview at http://127.0.0.1:8000/MathFromTheGroundUp/
.venv/Scripts/zensical build --clean
.venv/Scripts/python anki/build_decks.py
```

## Before committing a page

1. Run the self-check in `STYLE.md` (search for em dashes, curly quotes, banned words and patterns).
2. Recompute every answer and table value in Python, and run every "In code" snippet.
3. `zensical build --clean` must report no issues.

## Git

- Work on `main`. Many small commits, one per logical piece ("add percents lesson"). Short, plain messages.
- No Co-Authored-By or any other attribution lines in commits.
