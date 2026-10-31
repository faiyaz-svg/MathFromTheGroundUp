"""Write docs/reference/tricks-and-shortcuts.md from the lessons' trick sections.

Walks tools/lessons.yml in reading order (through build_nav.load_folders) and
pulls each written lesson's "## Tricks and shortcuts" section. The page gets
one line per lesson: the lesson title, linked to that section, and a summary.
The summary is the first sentence of the section, unless
tools/tricks_overrides.yml holds a hand-written one for that lesson.

Run from the repo root:  .venv/Scripts/python tools/build_tricks.py
With --tracked, only pages committed to git count, as in build_nav.py.
"""

from __future__ import annotations

import re
import sys

import yaml

import build_nav as bn

OUT = bn.DOCS / "reference" / "tricks-and-shortcuts.md"
OVERRIDES = bn.ROOT / "tools" / "tricks_overrides.yml"
MENTAL_MATH = "02-middle-school/08-mental-math/index.md"
ANCHOR = "tricks-and-shortcuts"
MAX_WORDS = 30


def tricks_section(text: str) -> str | None:
    m = re.search(r"^## Tricks and shortcuts[ \t]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else None


def first_sentence(section: str) -> str:
    """The first sentence of the first paragraph (or first list item) of a section."""
    for block in re.split(r"\n\s*\n", section):
        block = block.strip()
        if not block or block.startswith(("#", "|", "```", "$$", "<", "!")):
            continue
        block = re.sub(r"^([-*]|\d+\.) ", "", block).split("\n- ")[0]
        block = " ".join(block.split())
        sentence = re.split(r"(?<=[.!?])\s+(?=[A-Z$])", block)[0]
        return clean(sentence)
    return ""


def clean(sentence: str) -> str:
    sentence = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", sentence)  # links to plain text
    sentence = re.sub(r"<!--.*?-->", "", sentence)
    sentence = re.sub(r"\s*\((?:see )?(?:Example|Practice|Quick check|Lemma|Theorem)[^)]*\)", "", sentence)
    if sentence.endswith(":"):
        sentence = sentence[:-1] + "."
    return sentence.strip()


def math_balanced(text: str) -> bool:
    return text.replace("\\$", "").count("$") % 2 == 0


def build(folders: list[bn.Folder], overrides: dict[str, str]) -> tuple[str, list[str]]:
    mental = (
        "[Mental math](../" + MENTAL_MATH + ")"
        if bn.exists(MENTAL_MATH)
        else "Mental math"
    )
    lines = [
        "# Tricks and shortcuts",
        "",
        "Every lesson has a section called \"Tricks and shortcuts\": mental math, memory aids "
        "and quick checks that save time once you understand the method. This page lists them "
        "in reading order, one line per lesson, and each line links to the full section. "
        f"To practise calculating in your head, start with the {mental} chapter.",
        "",
    ]
    problems = []
    for f in folders:
        written = [les for les in f.all_lessons() if les.exists]
        if not written:
            continue
        lines += [f"## {f.title}", ""]
        for chapter in f.chapters:
            entries = []
            for les in chapter.lessons:
                if not les.exists:
                    continue
                section = tricks_section((bn.DOCS / les.path).read_text(encoding="utf-8"))
                if section is None:
                    continue
                summary = overrides.get(les.path) or first_sentence(section)
                if not summary or not math_balanced(summary):
                    problems.append(f"{les.path}: no usable first sentence; add an override")
                    continue
                if les.path not in overrides and len(summary.split()) > MAX_WORDS:
                    problems.append(f"{les.path}: summary has {len(summary.split())} words")
                entries.append(f"- [{les.title}](../{les.path}#{ANCHOR}): {summary}")
            if not entries:
                continue
            if chapter.title:
                lines += [f"### {chapter.title}", ""]
            lines += entries + [""]
    return "\n".join(lines).rstrip("\n") + "\n", problems


def main() -> None:
    if "--tracked" in sys.argv:
        bn.TRACKED = bn.tracked_paths()
    overrides = {}
    if OVERRIDES.is_file():
        overrides = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8")) or {}
    page, problems = build(bn.load_folders(), overrides)
    OUT.write_text(page, encoding="utf-8", newline="\n")
    count = page.count(f"#{ANCHOR})")
    print(f"{count} lessons listed in {OUT.relative_to(bn.ROOT).as_posix()}")
    for p in problems:
        print("  " + p)


if __name__ == "__main__":
    main()
