"""Figures for docs/07-economics-math/01-measuring-the-economy/01-how-economists-use-math-and-graphs.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/how-economists-use-math-and-graphs.py
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"


def demand_shift():
    """Demand Q = 100 - 2P + 0.5Y, drawn with price on the vertical axis."""
    fig, ax = fs.figure(5.2, 3.8)
    ax.grid(True, zorder=0)
    q = np.array([40, 120])
    ax.plot(q, 60 - q / 2, color=fs.BLUE, zorder=2)
    ax.plot(q, 62.5 - q / 2 + 0, color=fs.GREEN, zorder=2)
    # Income 40: P = 60 - Q/2. Income 50: P = 62.5 - Q/2.
    ax.plot([100], [10], "o", color=fs.BLUE, zorder=3)
    ax.plot([105], [10], "o", color=fs.GREEN, zorder=3)
    ax.plot([100], [12.5], "o", color=fs.GREEN, zorder=3)
    ax.plot([100, 100], [0, 10], color=fs.GRAY, linestyle=":", linewidth=1.3, zorder=1)
    ax.plot([0, 100], [10, 10], color=fs.GRAY, linestyle=":", linewidth=1.3, zorder=1)
    ax.text(38, 44.5, "income 50", color=fs.GREEN, ha="right", va="center")
    ax.text(38, 38.0, "income 40", color=fs.BLUE, ha="right", va="center")
    ax.text(97, 7.2, "(100, 10)", color=fs.BLUE, ha="right", va="top")
    ax.text(108, 10, "(105, 10)", color=fs.GREEN, ha="left", va="center")
    ax.text(103, 13.8, "(100, 12.5)", color=fs.GREEN, ha="left", va="bottom")
    ax.set_xlim(0, 125)
    ax.set_ylim(0, 50)
    ax.set_xlabel("Quantity of coffee per week (thousands of cups)")
    ax.set_ylabel("Price (dollars per cup)")
    return fig, "how-economists-use-math-and-graphs-demand-shift"


def linear_vs_log():
    """The same two series on a linear axis and on a log axis."""
    t = np.arange(0, 41)
    lin = 1000 + 100 * t
    exp = 1000 * 1.07**t
    fig, (a, b) = fs.plt.subplots(1, 2, figsize=(7.2, 3.6))
    for ax in (a, b):
        ax.grid(True, zorder=0)
        ax.plot(t, lin, color=fs.BLUE, zorder=2)
        ax.plot(t, exp, color=fs.GREEN, zorder=2)
        ax.set_xlabel("Year")
    a.set_ylabel("Balance (dollars)")
    a.set_title("Linear axis", color=fs.DARK, fontsize=11)
    b.set_title("Log axis", color=fs.DARK, fontsize=11)
    b.set_yscale("log")
    b.set_yticks([1000, 2000, 5000, 10000])
    b.set_yticklabels(["1,000", "2,000", "5,000", "10,000"])
    b.minorticks_off()
    a.text(17, 2500, r"+$100 a year", color=fs.BLUE, ha="left", va="top")
    a.text(30, 9500, "+7% a year", color=fs.GREEN, ha="right", va="bottom")
    b.text(30, 2800, r"+$100 a year", color=fs.BLUE, ha="center", va="top")
    b.text(1, 5200, "+7% a year", color=fs.GREEN, ha="left", va="bottom")
    return fig, "how-economists-use-math-and-graphs-log-axis"


if __name__ == "__main__":
    for make in (demand_shift, linear_vs_log):
        fig, name = make()
        fs.save(fig, FOLDER, name)
