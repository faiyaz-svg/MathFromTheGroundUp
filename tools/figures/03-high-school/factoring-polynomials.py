"""Figures for docs/03-high-school/04-radicals-and-polynomials/03-factoring-polynomials.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/factoring-polynomials.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "factoring-polynomials"


def block(ax, x0, y0, w, h, colour, label, size=13, rotation=0):
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=colour, alpha=0.22, edgecolor="none", zorder=1))
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor="none", edgecolor=fs.DARK, lw=1.4, zorder=3))
    ax.text(x0 + w / 2, y0 + h / 2, label, ha="center", va="center", fontsize=size, zorder=4, rotation=rotation)


def difference_of_squares():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.8, 3.5), gridspec_kw={"width_ratios": [5.6, 7.6]})
    a, b = 5.0, 2.0
    # Left: a square of side a with a b-by-b corner removed.
    ax1.set_xlim(-1.0, a + 0.8)
    ax1.set_ylim(-1.0, a + 1.1)
    ax1.set_aspect("equal")
    ax1.axis("off")
    block(ax1, 0, 0, a, a - b, fs.GREEN, r"$A$")
    block(ax1, 0, a - b, a - b, b, fs.BLUE, r"$B$")
    ax1.add_patch(Rectangle((a - b, a - b), b, b, facecolor="none", edgecolor=fs.GRAY, lw=1.3, ls=(0, (4, 3)), zorder=3))
    ax1.text(a - b / 2, a - b / 2, r"$b^2$", ha="center", va="center", fontsize=12, color=fs.GRAY)
    ax1.text(a / 2, -0.4, r"$a$", ha="center", va="top", fontsize=12)
    ax1.text(-0.35, (a - b) / 2, r"$a - b$", ha="right", va="center", fontsize=11)
    ax1.text(-0.35, a - b / 2, r"$b$", ha="right", va="center", fontsize=11)
    ax1.text(a / 2, a + 0.3, r"$a^2 - b^2$", ha="center", va="bottom", fontsize=13)

    # Right: B turned on its side and moved to the right of A.
    ax2.set_xlim(-1.0, a + b + 0.8)
    ax2.set_ylim(-1.0, a + 1.1)
    ax2.set_aspect("equal")
    ax2.axis("off")
    block(ax2, 0, 0, a, a - b, fs.GREEN, r"$A$")
    block(ax2, a, 0, b, a - b, fs.BLUE, r"$B$")
    ax2.text(a / 2, -0.4, r"$a$", ha="center", va="top", fontsize=12)
    ax2.text(a + b / 2, -0.4, r"$b$", ha="center", va="top", fontsize=12)
    ax2.text(-0.35, (a - b) / 2, r"$a - b$", ha="right", va="center", fontsize=11)
    ax2.text((a + b) / 2, a - b + 0.6, r"$(a + b)(a - b)$", ha="center", va="bottom", fontsize=13)
    ax2.text((a + b) / 2, -1.0, r"$a + b$", ha="center", va="top", fontsize=12)

    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-difference-of-squares")


if __name__ == "__main__":
    difference_of_squares()
