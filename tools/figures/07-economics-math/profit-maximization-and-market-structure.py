"""Figures for docs/07-economics-math/03-firms-and-consumers/03-profit-maximization-and-market-structure.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/profit-maximization-and-market-structure.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "profit-maximization-and-market-structure"
ARROW = dict(arrowstyle="-", color=fs.GRAY)


def grid(ax):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def competition():
    """A price-taking firm with a U-shaped marginal cost."""
    fig, ax = fs.figure(6.0, 4.2)
    grid(ax)
    q = np.linspace(1.2, 26, 600)
    mc = 15 - 1.2 * q + 0.06 * q**2
    avc = 15 - 0.6 * q + 0.02 * q**2
    ac = avc + 80 / q
    ax.plot(q, ac, color=fs.GREEN, lw=2.2)
    ax.plot(q, avc, color=fs.BLUE, lw=2.2)
    ax.plot(q, mc, color=fs.GRAY, lw=1.6)
    qs = q[q >= 15]
    ax.plot(qs, 15 - 1.2 * qs + 0.06 * qs**2, color=fs.RED, lw=3.4, zorder=4)
    ax.axhline(12, color=fs.ORANGE, lw=1.4, ls="--")
    r = 10 + 5 * np.sqrt(2)
    l = 10 - 5 * np.sqrt(2)
    ax.plot([r], [12], "o", color=fs.RED, ms=6.5, zorder=6)
    ax.plot([l], [12], "o", color=fs.GRAY, ms=6.5, zorder=6)
    ax.plot([15], [10.5], "o", color=fs.BLUE, ms=6.5, zorder=6)
    ax.plot([20], [15], "o", color=fs.GREEN, ms=6.5, zorder=6)
    ax.text(0.3, 11.0, "p = 12", color=fs.ORANGE, fontsize=9.5, ha="left", va="top")
    ax.text(25.8, 17.2, "AC", color=fs.GREEN, fontsize=11, ha="right")
    ax.text(25.8, 10.6, "AVC", color=fs.BLUE, fontsize=11, ha="right")
    ax.text(24.9, 23.4, "MC", color=fs.RED, fontsize=11, ha="right")
    ax.annotate("shutdown point\nq = 15, price 10.5", (15, 10.5), (6.5, 5.3), color=fs.BLUE, fontsize=9, arrowprops=ARROW)
    ax.annotate("break-even point\nq = 20, price 15", (20, 15), (11.2, 21.6), color=fs.GREEN, fontsize=9, arrowprops=ARROW)
    ax.annotate("q = 17.07: best\n(MC rising)", (r, 12), (17.6, 5.8), color=fs.RED, fontsize=9, arrowprops=ARROW)
    ax.annotate("q = 2.93: MC = p\nbut the worst", (l, 12), (3.0, 16.5), color=fs.DARK, fontsize=9, arrowprops=ARROW)
    ax.set_xlabel("output q", fontsize=10)
    ax.set_ylabel("dollars per unit", fontsize=10)
    ax.set_xlim(0, 26)
    ax.set_ylim(0, 25)
    fs.save(fig, FOLDER, f"{SLUG}-competition")


def monopoly():
    """A monopolist with linear demand and rising marginal cost."""
    fig, ax = fs.figure(6.0, 4.2)
    grid(ax)
    q = np.linspace(0, 100, 200)
    ax.fill([36, 36, 60], [64, 28, 40], color=fs.RED, alpha=0.22, lw=0, zorder=2)
    ax.plot(q, 100 - q, color=fs.GREEN, lw=2.4)
    qm = np.linspace(0, 52, 100)
    ax.plot(qm, 100 - 2 * qm, color=fs.BLUE, lw=2.2)
    ax.plot(q, 10 + 0.5 * q, color=fs.RED, lw=2.2)
    ax.plot([36, 36], [0, 64], color=fs.GRAY, lw=1.1, ls="--")
    ax.plot([0, 36], [64, 64], color=fs.GRAY, lw=1.1, ls="--")
    ax.plot([36], [28], "o", color=fs.RED, ms=6.5, zorder=6)
    ax.plot([36], [64], "o", color=fs.GREEN, ms=6.5, zorder=6)
    ax.plot([60], [40], "o", color=fs.DARK, ms=6.5, zorder=6)
    ax.axhline(0, color=fs.DARK, lw=0.8)
    ax.text(88, 17, "demand", color=fs.GREEN, fontsize=11, ha="center")
    ax.text(12, 65, "price p = 64", color=fs.DARK, fontsize=9.5, ha="left", va="bottom")
    ax.text(4.5, 72, "MR", color=fs.BLUE, fontsize=11, ha="center")
    ax.text(90, 55.5, "MC", color=fs.RED, fontsize=11, ha="center")
    ax.annotate("MR = MC = 28\nat q = 36", (36, 28), (40.5, 12), color=fs.RED, fontsize=9, arrowprops=ARROW)
    ax.annotate("competitive point\nq = 60, p = 40", (60, 40), (66, 66), color=fs.DARK, fontsize=9, arrowprops=ARROW)
    ax.annotate("deadweight loss = 432", (46, 45.5), (60, 82), color=fs.RED, fontsize=9.5, arrowprops=ARROW)
    ax.set_xlabel("quantity q", fontsize=10)
    ax.set_ylabel("dollars per unit", fontsize=10)
    ax.set_xlim(0, 100)
    ax.set_ylim(-6, 102)
    fs.save(fig, FOLDER, f"{SLUG}-monopoly")


if __name__ == "__main__":
    competition()
    monopoly()
