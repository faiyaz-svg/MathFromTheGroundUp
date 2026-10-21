"""Figures for docs/05-university-core/05-sequences-and-series/02-infinite-series-basics.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/infinite-series-basics.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "infinite-series-basics"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def grid(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def partial_sums():
    """Partial sums of 1/2 + 1/4 + ... (settle at 1) and of 1 + 1/2 + 1/3 + ... (keep growing)."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.8))
    grid(a)
    n = np.arange(1, 11)
    s = 1 - 0.5**n
    a.axhline(1, color=fs.DARK, lw=1.2, ls="--")
    a.plot(n, s, "o-", color=fs.GREEN, lw=1.6, ms=6)
    a.text(10.3, 1.0, "S = 1", color=fs.DARK, fontsize=10, ha="left", va="center")
    a.text(1.2, 0.46, "S₁ = 1/2", color=fs.GREEN, fontsize=9.5, ha="left", va="top")
    a.text(2.2, 0.70, "S₂ = 3/4", color=fs.GREEN, fontsize=9.5, ha="left", va="top")
    a.text(5.2, 0.45, "Sₙ = 1 − 1/2ⁿ\nconverges to 1", color=fs.GREEN, fontsize=10, ha="left", va="center")
    a.set_xlim(0, 12.5)
    a.set_ylim(0, 1.2)
    a.set_xticks(range(0, 11, 2))
    a.set_xlabel("n")

    grid(b)
    m = np.arange(1, 101)
    h = np.cumsum(1.0 / m)
    b.step(m, h, where="post", color=fs.RED, lw=2.0)
    b.axhline(5, color=fs.DARK, lw=1.0, ls="--")
    b.plot([83], [5.0021], "o", color=fs.DARK, ms=5.5, zorder=5)
    b.text(80, 4.7, "Hₙ passes 5 at n = 83", color=fs.DARK, fontsize=9.5, ha="right", va="top")
    b.text(40, 2.0, "Hₙ = 1 + 1/2 + … + 1/n\nkeeps growing, with no limit", color=fs.RED, fontsize=10, ha="left", va="center")
    b.set_xlim(0, 100)
    b.set_ylim(0, 6)
    b.set_xlabel("n")
    fs.save(fig, FOLDER, f"{SLUG}-partial-sums")


def harmonic_grouping():
    """Bars of height 1/k for k = 1..16, grouped so each group adds to more than 1/2."""
    fig, ax = fs.figure(6.4, 3.9)
    grid(ax)
    groups = [(1, 1, fs.DARK), (2, 2, fs.BLUE), (3, 4, fs.GREEN), (5, 8, fs.ORANGE), (9, 16, fs.RED)]
    for lo, hi, col in groups:
        ks = np.arange(lo, hi + 1)
        ax.bar(ks, 1.0 / ks, width=0.82, color=col, alpha=0.85, zorder=3)
    ax.plot([1.5, 16.5], [0, 0], color=fs.DARK, lw=0.8)
    ax.text(1, 1.06, "1", color=fs.DARK, fontsize=9.5, ha="center", va="bottom")
    ax.text(2, 0.56, "1/2", color=fs.BLUE, fontsize=9.5, ha="center", va="bottom")
    ax.text(2.8, 0.78, "1/3 + 1/4 > 1/2", color=fs.GREEN, fontsize=9.5, ha="left", va="bottom")
    ax.text(4.8, 0.52, "1/5 + … + 1/8 > 1/2", color=fs.ORANGE, fontsize=9.5, ha="left", va="bottom")
    ax.text(8.8, 0.30, "1/9 + … + 1/16 > 1/2", color=fs.RED, fontsize=9.5, ha="left", va="bottom")
    ax.set_xlim(0.2, 16.8)
    ax.set_ylim(0, 1.25)
    ax.set_xticks(range(1, 17))
    ax.set_xlabel("k   (bar height is 1/k)")
    fs.save(fig, FOLDER, f"{SLUG}-harmonic-grouping")


def geometric_square():
    """The unit square cut into 1/2, 1/4, 1/8, ... pieces."""
    fig, ax = fs.figure(4.4, 4.4)
    ax.set_aspect("equal")
    ax.axis("off")
    cols = [fs.GREEN, fs.BLUE, fs.ORANGE, fs.RED, fs.DARK]
    x0, y0, w, h = 0.0, 0.0, 1.0, 1.0
    vertical = True
    labels = ["1/2", "1/4", "1/8", "1/16", "1/32"]
    for i in range(5):
        if vertical:
            piece = (x0, y0, w / 2, h)
            x0 += w / 2
            w /= 2
        else:
            piece = (x0, y0, w, h / 2)
            y0 += h / 2
            h /= 2
        ax.add_patch(Rectangle(piece[:2], piece[2], piece[3], facecolor=cols[i], alpha=0.35, edgecolor=fs.DARK, lw=1.2))
        if i < 4:
            ax.text(piece[0] + piece[2] / 2, piece[1] + piece[3] / 2, labels[i], ha="center", va="center", fontsize=12 - i, color=fs.DARK)
        vertical = not vertical
    ax.text(x0 + w / 2, y0 + h / 2, "…", ha="center", va="center", fontsize=11, color=fs.DARK)
    ax.add_patch(Rectangle((0, 0), 1, 1, fill=False, edgecolor=fs.DARK, lw=2.0))
    ax.text(0.5, -0.07, "area 1 in total", ha="center", va="top", fontsize=10.5, color=fs.DARK)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.15, 1.05)
    fs.save(fig, FOLDER, f"{SLUG}-geometric-square")


if __name__ == "__main__":
    partial_sums()
    harmonic_grouping()
    geometric_square()
