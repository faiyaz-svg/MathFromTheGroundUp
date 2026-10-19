"""Figures for docs/03-high-school/04-radicals-and-polynomials/02-polynomial-arithmetic.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/polynomial-arithmetic.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "polynomial-arithmetic"
BOX = dict(facecolor="white", edgecolor="none", pad=0.6, alpha=0.9)


def block(ax, x0, y0, w, h, colour, label, size=12, alpha=0.22):
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=colour, alpha=alpha, edgecolor="none", zorder=1))
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor="none", edgecolor=fs.DARK, lw=1.4, zorder=3))
    ax.text(x0 + w / 2, y0 + h / 2, label, ha="center", va="center", fontsize=size, zorder=4)


def brace_text(ax, x, y, text, ha="center", va="center", size=11):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, zorder=5)


def garden():
    """The rectangle (x + 5) by (x + 3), cut into four pieces."""
    fig, ax = plt.subplots(figsize=(5.2, 3.9))
    x = 4.0  # drawn length of x
    ax.set_xlim(-2.3, x + 5.3)
    ax.set_ylim(-1.2, x + 3.9)
    ax.set_aspect("equal")
    ax.axis("off")
    # bottom-left: x by x; left strip: 3 by x (width x, height 3) above; right strip: 5 wide, x tall.
    block(ax, 0, 0, x, x, fs.GREEN, r"$x^2$", size=14)
    block(ax, x, 0, 5, x, fs.BLUE, r"$5x$", size=14)
    block(ax, 0, x, x, 3, fs.BLUE, r"$3x$", size=14)
    block(ax, x, x, 5, 3, fs.ORANGE, r"$15$", size=14)
    # unit grid lines inside the 5 by x and 3 by x and 5 by 3 blocks
    for i in range(1, 5):
        ax.plot([x + i, x + i], [x, x + 3], color=fs.DARK, lw=0.6, zorder=2)
    for j in range(1, 3):
        ax.plot([x, x + 5], [x + j, x + j], color=fs.DARK, lw=0.6, zorder=2)
    # side labels
    brace_text(ax, x / 2, -0.55, r"$x$")
    brace_text(ax, x + 2.5, -0.55, r"$5$")
    brace_text(ax, x + 2.5, -1.15, r"$x + 5$", size=12)
    ax.text(-0.55, x / 2, r"$x$", ha="right", va="center", fontsize=11)
    ax.text(-0.55, x + 1.5, r"$3$", ha="right", va="center", fontsize=11)
    ax.text(-1.5, (x + 3) / 2, r"$x + 3$", ha="right", va="center", fontsize=12, rotation=90)
    fs.save(fig, FOLDER, f"{SLUG}-area-model")


def binomial_square():
    """A square of side a + b, cut into a^2, two ab rectangles and b^2."""
    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    a, b = 5.0, 3.0
    ax.set_xlim(-1.3, a + b + 1.2)
    ax.set_ylim(-1.6, a + b + 0.8)
    ax.set_aspect("equal")
    ax.axis("off")
    block(ax, 0, 0, a, a, fs.GREEN, r"$a^2$", size=15)
    block(ax, a, 0, b, a, fs.BLUE, r"$ab$", size=14)
    block(ax, 0, a, a, b, fs.BLUE, r"$ab$", size=14)
    block(ax, a, a, b, b, fs.ORANGE, r"$b^2$", size=14)
    ax.text(a / 2, -0.55, r"$a$", ha="center", va="center", fontsize=12)
    ax.text(a + b / 2, -0.55, r"$b$", ha="center", va="center", fontsize=12)
    ax.text(a + b / 2, -1.3, r"$a + b$", ha="center", va="center", fontsize=12)
    ax.text(-0.55, a / 2, r"$a$", ha="right", va="center", fontsize=12)
    ax.text(-0.55, a + b / 2, r"$b$", ha="right", va="center", fontsize=12)
    ax.text(-1.2, (a + b) / 2, r"$a + b$", ha="right", va="center", fontsize=12, rotation=90)
    fs.save(fig, FOLDER, f"{SLUG}-binomial-square")


if __name__ == "__main__":
    garden()
    binomial_square()
