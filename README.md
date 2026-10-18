# Math From the Ground Up

A self-study math textbook from grade 1 arithmetic to university math, with side tracks for proofs, CS math, economics and Canadian personal finance.

Read it online: https://faiyaz-svg.github.io/MathFromTheGroundUp/

The lessons are plain Markdown files in `docs/`, so they can also be read in VS Code: open a file and press Ctrl+Shift+V for the preview with math.

## Run the site locally

```bash
py -m venv .venv
.venv/Scripts/python -m pip install -r requirements-dev.txt
.venv/Scripts/zensical serve
```

Then open http://127.0.0.1:8000/MathFromTheGroundUp/.

## Working on the book

- `STYLE.md`: how pages are written.
- `LESSON_TEMPLATE.md`: the structure of a lesson.
- `DESIGN.md`: how the site looks.
- `tools/lessons.yml`: the full lesson map. After adding a lesson, run `.venv/Scripts/python tools/build_nav.py` to update the menu, the progress page and the folder lesson lists.
- `anki/`: flashcard decks, built with `.venv/Scripts/python anki/build_decks.py`.

Pushing to `main` publishes the site through GitHub Actions.
