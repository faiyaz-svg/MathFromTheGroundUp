"""Figures for docs/07-economics-math/03-firms-and-consumers/04-utility-and-indifference-curves.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/utility-and-indifference-curves.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "utility-and-indifference-curves"
ARROW = dict(arrowstyle="-", color=fs.GRAY)


def grid(ax):
    ax.tick_params(labelsize=8.5, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def three_cases():
    fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.8))

    a = axs[0]
    grid(a)
    x = np.linspace(2, 30, 400)
    a.plot([0, 30], [45, 0], color=fs.DARK, lw=2.0)
    for u, col in [(6000, fs.GRAY), (9000, fs.GREEN), (12000, fs.GRAY)]:
        a.plot(x, np.sqrt(u / x), color=col, lw=2.2 if u == 9000 else 1.5)
    a.plot([10], [30], "o", color=fs.RED, ms=7, zorder=5)
    a.annotate("best bundle (10, 30):\nthe curve touches\nthe budget line", (10, 30), (13.5, 37.5), color=fs.RED, fontsize=8.5, arrowprops=ARROW)
    a.text(24, 8.2, "budget line\n3x + 2y = 90", color=fs.DARK, fontsize=8.5, ha="center")
    a.text(30.5, 16.2, "U = 6000", color=fs.GRAY, fontsize=8.5, ha="right")
    a.text(30.5, 19.6, "U = 9000", color=fs.GREEN, fontsize=8.5, ha="right")
    a.text(30.5, 22.6, "U = 12000", color=fs.GRAY, fontsize=8.5, ha="right")
    a.set_xlim(0, 31)
    a.set_ylim(0, 48)
    a.set_xlabel("x", fontsize=10)
    a.set_ylabel("y", fontsize=10)
    a.set_title("")

    b = axs[1]
    grid(b)
    b.plot([0, 60], [20, 0], color=fs.DARK, lw=2.0)
    for u, col in [(40, fs.GRAY), (60, fs.GREEN), (80, fs.GRAY)]:
        b.plot([0, u], [u / 2, 0], color=col, lw=2.2 if u == 60 else 1.5)
    b.plot([60], [0], "o", color=fs.RED, ms=7, zorder=5)
    b.annotate("corner (60, 0)", (60, 0), (64, 2.2), color=fs.RED, fontsize=8.5, arrowprops=ARROW)
    b.text(8, 2.6, "budget line x + 3y = 60", color=fs.DARK, fontsize=8.5, ha="left")
    b.text(1.2, 20.9, "U = 40", color=fs.GRAY, fontsize=8.5)
    b.text(1.2, 30.9, "U = 60", color=fs.GREEN, fontsize=8.5)
    b.text(1.2, 40.9, "U = 80", color=fs.GRAY, fontsize=8.5)
    b.text(79, 36.0, "indifference curves\nare straight lines", color=fs.GRAY, fontsize=8.5, ha="right", va="top")
    b.set_xlim(0, 82)
    b.set_ylim(0, 42)
    b.set_xlabel("x", fontsize=10)
    b.set_ylabel("y", fontsize=10)

    c = axs[2]
    grid(c)
    xs = np.linspace(0, 30, 100)
    c.plot(xs, (60 - 4 * xs) / 2, color=fs.DARK, lw=2.0)
    for u, col in [(5, fs.GRAY), (10, fs.GREEN), (15, fs.GRAY)]:
        c.plot([u, u, 30], [30, u, u], color=col, lw=2.2 if u == 10 else 1.5)
    c.plot([10], [10], "o", color=fs.RED, ms=7, zorder=5)
    c.annotate("kink (10, 10):\nno tangent line", (10, 10), (14, 17.5), color=fs.RED, fontsize=8.5, arrowprops=ARROW)
    c.text(16.5, 2.0, "budget line 4x + 2y = 60", color=fs.DARK, fontsize=8.5, ha="left")
    c.text(29.6, 5.5, "U = 5", color=fs.GRAY, fontsize=8.5, ha="right")
    c.text(29.6, 10.5, "U = 10", color=fs.GREEN, fontsize=8.5, ha="right")
    c.text(29.6, 15.5, "U = 15", color=fs.GRAY, fontsize=8.5, ha="right")
    c.set_xlim(0, 30)
    c.set_ylim(0, 31)
    c.set_xlabel("x", fontsize=10)
    c.set_ylabel("y", fontsize=10)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-three-cases")


if __name__ == "__main__":
    three_cases()
