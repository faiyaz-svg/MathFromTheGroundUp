"""Figures for docs/05-university-core/06-linear-algebra/02-systems-and-gaussian-elimination.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/systems-and-gaussian-elimination.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "systems-and-gaussian-elimination"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def arrow(ax, tail, tip, color, lw=2.2, z=4):
    ax.annotate(
        "",
        xy=tip,
        xytext=tail,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=14),
        zorder=z,
    )


def grid2d(ax, xlim, ylim):
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.axhline(0, color=fs.DARK, lw=1.0)
    ax.axvline(0, color=fs.DARK, lw=1.0)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(labelsize=9, length=0)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)


def three_cases():
    """Two lines in the plane: one point, no point, a whole line."""
    fig, axs = plt.subplots(1, 3, figsize=(10.2, 3.5))
    xs = np.array([-1.5, 5.0])
    lim = ((-1, 4.6), (-2.0, 4.9))

    a = axs[0]
    grid2d(a, *lim)
    a.plot(xs, 3 - xs, color=fs.GREEN, lw=2.2)
    a.plot(xs, xs - 1, color=fs.BLUE, lw=2.2)
    a.plot([2], [1], "o", color=fs.RED, ms=7, zorder=5)
    a.text(0.25, 3.35, "x + y = 3", color=fs.GREEN, fontsize=10, ha="left", va="bottom")
    a.text(3.6, 3.0, "x − y = 1", color=fs.BLUE, fontsize=10, ha="center", va="bottom")
    a.text(2.2, 0.7, "(2, 1)", color=fs.RED, fontsize=10, ha="left", va="top")
    a.text(1.8, -1.6, "one solution", color=fs.DARK, fontsize=10.5, ha="center", va="center")

    b = axs[1]
    grid2d(b, *lim)
    b.plot(xs, 3 - xs, color=fs.GREEN, lw=2.2)
    b.plot(xs, 1 - xs, color=fs.BLUE, lw=2.2)
    b.text(3.3, 0.45, "x + y = 3", color=fs.GREEN, fontsize=10, ha="left", va="bottom")
    b.text(1.6, -0.85, "x + y = 1", color=fs.BLUE, fontsize=10, ha="left", va="center")
    b.text(1.8, -1.6, "no solution", color=fs.DARK, fontsize=10.5, ha="center", va="center")

    c = axs[2]
    grid2d(c, *lim)
    c.plot(xs, 3 - xs, color=fs.GREEN, lw=4.6)
    c.plot(xs, 3 - xs, color=fs.BLUE, lw=1.6, ls=(0, (4, 4)))
    c.text(1.0, 3.5, "x + y = 3 and\n2x + 2y = 6", color=fs.GREEN, fontsize=10, ha="left", va="bottom")
    c.text(1.8, -1.6, "infinitely many solutions", color=fs.DARK, fontsize=10.5, ha="center", va="center")
    fig.subplots_adjust(wspace=0.12)
    fs.save(fig, FOLDER, f"{SLUG}-three-cases")


def row_and_column():
    """The same system 2x + y = 5, x - y = 1 as two lines and as a combination of columns."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 3.9))
    grid2d(a, (-1, 4.2), (-2.9, 5.4))
    xs = np.array([-1.0, 4.2])
    a.plot(xs, 5 - 2 * xs, color=fs.GREEN, lw=2.2)
    a.plot(xs, xs - 1, color=fs.BLUE, lw=2.2)
    a.plot([2], [1], "o", color=fs.RED, ms=7, zorder=5)
    a.text(0.5, 4.3, "2x + y = 5", color=fs.GREEN, fontsize=10, ha="left", va="center")
    a.text(3.3, 2.7, "x − y = 1", color=fs.BLUE, fontsize=10, ha="left", va="center")
    a.text(2.15, 0.8, "(2, 1)", color=fs.RED, fontsize=10, ha="left", va="top")
    a.text(1.6, -2.5, "rows: two lines meet at (2, 1)", color=fs.DARK, fontsize=10, ha="center", va="center")

    grid2d(b, (-1.4, 6.2), (-2.9, 3.4))
    a1 = np.array([2.0, 1.0])
    a2 = np.array([1.0, -1.0])
    bb = np.array([5.0, 1.0])
    arrow(b, (0, 0), tuple(a1), fs.GREEN, lw=1.6)
    arrow(b, tuple(a1), tuple(2 * a1), fs.GREEN, lw=1.6)
    arrow(b, tuple(2 * a1), tuple(2 * a1 + a2), fs.BLUE, lw=2.2)
    arrow(b, (0, 0), tuple(a2), fs.BLUE, lw=1.6)
    arrow(b, (0, 0), tuple(bb), fs.RED, lw=2.6)
    b.text(0.05, 1.5, "col 1 = (2, 1)", color=fs.GREEN, fontsize=9.5, ha="left", va="bottom")
    b.text(1.05, -1.25, "col 2 = (1, −1)", color=fs.BLUE, fontsize=9.5, ha="left", va="top")
    b.text(5.15, 1.0, "b = (5, 1)", color=fs.RED, fontsize=10, ha="left", va="center")
    b.text(4.35, 2.2, "1 × col 2", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    b.text(2.4, 0.35, "2 × col 1", color=fs.GREEN, fontsize=9.5, ha="left", va="center", bbox=BOX)
    b.text(2.1, -2.5, "columns: b = 2 × col 1 + 1 × col 2", color=fs.DARK, fontsize=10, ha="center", va="center")
    fig.subplots_adjust(wspace=0.08)
    fs.save(fig, FOLDER, f"{SLUG}-row-and-column")


if __name__ == "__main__":
    three_cases()
    row_and_column()
