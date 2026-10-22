"""Figure for docs/06-cs-math/04-sums-recurrences-and-algorithms/01-sums-and-closed-forms.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/06-cs-math/sums-and-closed-forms.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "06-cs-math"
SLUG = "sums-and-closed-forms"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)


def harmonic():
    """Upper and lower rectangles for 1/x on [1, 8]."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 3.6), sharey=True)
    x = np.linspace(1, 8, 400)
    n = 7
    for ax in (a, b):
        ax.plot(x, 1 / x, color=fs.DARK, lw=2.0, zorder=4)
        ax.grid(True)
        ax.set_axisbelow(True)
        ax.tick_params(labelsize=9, length=3)
        ax.set_xlim(0.8, 8.4)
        ax.set_ylim(0, 1.12)
        ax.set_xticks(range(1, 9))
        ax.set_xlabel("x")
    for k in range(1, n + 1):
        a.bar(k, 1 / k, width=1, align="edge", color=fs.GREEN, alpha=0.35, edgecolor=fs.GREEN, lw=1.0, zorder=2)
        b.bar(k, 1 / (k + 1), width=1, align="edge", color=fs.BLUE, alpha=0.35, edgecolor=fs.BLUE, lw=1.0, zorder=2)
    a.set_ylabel("1/x")
    a.text(4.6, 0.82, "heights 1/k:\ntotal area H$_7$\nis more than ln 8", color=fs.GREEN, fontsize=10.5, ha="left", va="center", bbox=BOX, zorder=6)
    b.text(4.6, 0.82, "heights 1/(k+1):\ntotal area H$_8$ − 1\nis less than ln 8", color=fs.BLUE, fontsize=10.5, ha="left", va="center", bbox=BOX, zorder=6)
    a.text(7.9, 0.2, "y = 1/x", color=fs.DARK, fontsize=10, ha="right", va="bottom", bbox=BOX, zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-harmonic")


if __name__ == "__main__":
    harmonic()
