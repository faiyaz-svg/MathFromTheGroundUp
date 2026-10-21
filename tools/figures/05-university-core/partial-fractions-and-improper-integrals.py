"""Figure for docs/05-university-core/04-integrals/05-partial-fractions-and-improper-integrals.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/partial-fractions-and-improper-integrals.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "partial-fractions-and-improper-integrals"


def p_test():
    """Areas under 1/x^2 (finite) and 1/x (growing without bound) from x = 1 to the right."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.2, 3.4), sharey=True)
    xs = np.linspace(1, 9.5, 400)
    for ax in (ax1, ax2):
        ax.tick_params(labelsize=9, length=3)
        ax.grid(True)
        ax.set_axisbelow(True)
        ax.set_xlim(0.6, 10.3)
        ax.set_ylim(0, 1.15)
        ax.set_xticks([1, 2, 4, 6, 8, 10])
        ax.set_yticks([0.5, 1])
    ax1.fill_between(xs, 0, 1 / xs**2, color=fs.GREEN, alpha=0.3, zorder=2)
    ax1.plot(xs, 1 / xs**2, color=fs.GREEN, lw=2.2, zorder=4)
    ax1.text(1.3, 1.07, "y = 1/x²", color=fs.GREEN, fontsize=11, ha="left", va="center")
    ax1.text(4.2, 0.55, "area from 1 to b is 1 − 1/b\nand tends to 1", color=fs.GREEN,
             fontsize=10, ha="left", va="center")
    ax2.fill_between(xs, 0, 1 / xs, color=fs.RED, alpha=0.25, zorder=2)
    ax2.plot(xs, 1 / xs, color=fs.RED, lw=2.2, zorder=4)
    ax2.text(1.3, 1.07, "y = 1/x", color=fs.RED, fontsize=11, ha="left", va="center")
    ax2.text(4.2, 0.6, "area from 1 to b is ln b\nand grows without bound", color=fs.RED,
             fontsize=10, ha="left", va="center")
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-p-test")


if __name__ == "__main__":
    p_test()
