"""Figures for docs/02-middle-school/04-powers-roots-and-real-numbers/03-roots-irrationals-and-types-of-numbers.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/roots-irrationals-and-types-of-numbers.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from matplotlib.patches import Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "roots-irrationals-and-types-of-numbers"


def box(ax, x, y, w, h, colour, fill_alpha):
    """A set drawn as a rectangle: a pale fill and a solid outline."""
    ax.add_patch(Rectangle((x, y), w, h, facecolor=colour, alpha=fill_alpha, edgecolor="none"))
    ax.add_patch(Rectangle((x, y), w, h, facecolor="none", edgecolor=colour, linewidth=2))


def label(ax, x, y, symbol, words, colour):
    ax.text(x, y, symbol, fontsize=15, fontweight="bold", color=colour, va="top", ha="left")
    ax.text(x + 0.55, y - 0.05, words, fontsize=11, color=fs.DARK, va="top", ha="left")


def member(ax, x, y, text):
    """One example number, centred on (x, y)."""
    ax.text(x, y, text, fontsize=14, color=fs.DARK, va="center", ha="center")


def number_sets():
    fig, ax = fs.figure(6.4, 4.4)
    ax.set_xlim(0, 12.8)
    ax.set_ylim(0, 8.8)
    ax.set_aspect("equal")
    ax.axis("off")

    # R, the real numbers: the whole picture.
    box(ax, 0.1, 0.1, 12.6, 8.6, fs.DARK, 0.04)
    label(ax, 0.35, 8.45, "ℝ", "real numbers", fs.DARK)

    # Q, the rational numbers, inside R on the left.
    box(ax, 0.5, 0.5, 8.6, 7.2, fs.BLUE, 0.07)
    label(ax, 0.75, 7.45, "ℚ", "rational numbers", fs.BLUE)
    for y, t in [(6.0, r"$0.5$"), (4.6, r"$-\dfrac{2}{3}$"), (3.2, r"$0.\!\overline{3}$"), (1.8, r"$\dfrac{22}{7}$")]:
        member(ax, 7.75, y, t)

    # Z, the integers, inside Q.
    box(ax, 0.9, 0.9, 5.7, 5.6, fs.ORANGE, 0.10)
    label(ax, 1.15, 6.25, "ℤ", "integers", fs.ORANGE)
    member(ax, 2.4, 4.9, r"$-3$")
    member(ax, 4.6, 4.9, r"$-12$")

    # N, the natural numbers, inside Z.
    box(ax, 1.3, 1.3, 4.9, 2.7, fs.GREEN, 0.14)
    label(ax, 1.55, 3.75, "ℕ", "natural numbers", fs.GREEN)
    member(ax, 2.2, 2.2, r"$0$")
    member(ax, 3.5, 2.2, r"$7$")
    member(ax, 4.9, 2.2, r"$\sqrt{9}$")

    # The irrational numbers: the part of R outside Q.
    ax.text(9.45, 7.45, "irrational\nnumbers", fontsize=11, color=fs.DARK, va="top", ha="left", linespacing=1.2)
    for y, t in [(5.3, r"$\sqrt{2}$"), (3.9, r"$\pi$"), (2.5, r"$-\sqrt{5}$")]:
        member(ax, 10.6, y, t)

    fs.save(fig, FOLDER, f"{SLUG}-number-sets")


if __name__ == "__main__":
    number_sets()
