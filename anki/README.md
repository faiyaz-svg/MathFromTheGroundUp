# Anki decks

Each book folder has one card file, `anki/cards/<folder>.tsv`. The build turns it into one Anki deck, `docs/downloads/anki/<folder>.apkg`, which the website offers as a download. All decks sit under a parent deck called "Math From the Ground Up", for example "Math From the Ground Up::06 CS math".

## Card file format

A card file is UTF-8 text with one card per line and the columns separated by tabs. The first line is the header:

```text
id	front	back	tags
```

Every line has exactly these 4 columns, even when the tags column is empty (end the line with a tab).

- `id` is a short lowercase slug, unique within the file, such as `bases-hex-digit-values`. It is the card's identity in Anki, so don't change it after the deck is published. A new id makes a new card, and the old one stays in the reader's collection.
- `front` is the question and `back` is the answer. Neither can be empty.
- `tags` is a space-separated list, such as `number-bases hex conversion`. Use letters, digits, `-` and `_`, with `::` for nested tags. The folder name (`06-cs-math`) is added to every card as a tag.

A field can't contain a tab or a line break. Write `<br>` where you want a new line; you can't put a tab inside a field. Other HTML also works outside math, such as `<code>0x1F</code>`. Quotes are ordinary characters and need no escaping. Blank lines and lines starting with `#` are skipped, so you can group cards under comment lines.

Write math the same way as in the book (see `STYLE.md`):

- inline math is `$x^2$`, and display math is `$$...$$` inside the field;
- a dollar sign for money is `\$12.50`;
- inside math, write `<`, `>` and `&` directly, for example `$a < b$`. The build escapes them for HTML. Outside math, write `<` as `&lt;`.

Anki shows math with MathJax, which uses `\(...\)` and `\[...\]`, so the build converts `$...$` to `\(...\)` and `$$...$$` to `\[...\]`, and turns `\$` back into `$`.

## Adding cards

1. Open the folder's `.tsv` file in an editor that keeps tabs (VS Code does). If the folder has no file yet, create one with the header line above.
2. Add one line per card with a new id.
3. Recompute every numeric answer in Python, as for lesson pages, and run the self-check from `STYLE.md` on the text.
4. Build the decks and commit the `.tsv` file together with the new `.apkg`.

## Building

From the repo root:

```bash
.venv/Scripts/python anki/build_decks.py
```

The script reads every `anki/cards/*.tsv` and prints one line per deck with the number of cards and the output path. It checks all files before writing anything. Duplicate ids, empty fields, a wrong number of columns, unbalanced `$` and bad HTML are reported as `file:line: message`, and then the script stops with exit code 1 without writing a deck.

A deck whose cards didn't change is left as it is (the line ends with "(unchanged)"), so rebuilding doesn't create a new file to commit. A deck whose cards changed gets the current time, which is what tells Anki the file is newer.

The tests:

```bash
.venv/Scripts/python anki/test_build_decks.py
```

## Importing into Anki

On a computer, download the `.apkg` file and open it with Anki, or use File > Import in Anki and choose the file.

On Android (AnkiDroid), download the file, then open it from the browser's downloads or a file manager and choose AnkiDroid. You can also use Import in the menu on AnkiDroid's deck list and pick the file.

On iPhone or iPad (AnkiMobile), download the file in Safari, open it from the downloads list or the Files app, and use the share button to send it to Anki.

If you sync with AnkiWeb, you only need to import on one device. The cards reach the others at the next sync.

## Updating a deck

Import the new `.apkg` the same way. Anki recognises cards it has seen before by their id, so it updates their text in place and keeps your review history; only new cards are added. This works with Anki's default import option for updating notes ("if newer").

A card deleted from the `.tsv` file is not deleted from your collection. Delete it in Anki's browser if you no longer want it.
