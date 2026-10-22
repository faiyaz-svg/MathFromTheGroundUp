"""Figures for docs/07-economics-math/02-markets/01-opportunity-cost-and-the-ppc.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/opportunity-cost-and-the-ppc.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "opportunity-cost-and-the-ppc"


def style(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def ppc():
    """Left: the linear bakery PPC. Right: the bowed-out wheat and canola PPC."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 4.0))

    # Left panel: B = 240 - 2L
    style(ax1)
    L = np.array([0, 120])
    ax1.fill_between(L, 0, 240 - 2 * L, color=fs.GREEN, alpha=0.12, zorder=1)
    ax1.plot(L, 240 - 2 * L, color=fs.GREEN, lw=2.4, zorder=4)
    ax1.plot([60], [120], "o", color=fs.GREEN, ms=7, zorder=6)
    ax1.plot([30], [90], "o", color=fs.ORANGE, ms=7, zorder=6)
    ax1.plot([90], [150], "o", color=fs.RED, ms=7, zorder=6)
    ax1.text(63, 126, "A: efficient", color=fs.GREEN, fontsize=9.5, ha="left", va="bottom")
    ax1.text(33, 84, "B: inefficient", color=fs.ORANGE, fontsize=9.5, ha="left", va="top")
    ax1.text(87, 156, "C: unattainable", color=fs.RED, fontsize=9.5, ha="right", va="bottom")
    ax1.text(60, 220,"slope = −2 everywhere:\n1 loaf costs 2 buns", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax1.set_xlim(0, 130)
    ax1.set_ylim(0, 260)
    ax1.set_xticks([0, 30, 60, 90, 120])
    ax1.set_yticks([0, 60, 120, 180, 240])
    ax1.set_xlabel("loaves per day", fontsize=9.5)
    ax1.set_ylabel("buns per day", fontsize=9.5)

    # Right panel: w^2 + c^2 = 100 and 144
    style(ax2)
    ax2.set_aspect("equal")
    th = np.linspace(0, np.pi / 2, 300)
    ax2.fill_between(10 * np.cos(th), 0, 10 * np.sin(th), color=fs.GREEN, alpha=0.12, zorder=1)
    ax2.plot(10 * np.cos(th), 10 * np.sin(th), color=fs.GREEN, lw=2.4, zorder=4)
    ax2.plot(12 * np.cos(th), 12 * np.sin(th), color=fs.BLUE, lw=1.8, ls="--", zorder=3)
    # tangent lines at (6,8) and (8,6)
    for (x0, y0, slope, col) in [(6, 8, -0.75, fs.DARK), (8, 6, -4 / 3, fs.DARK)]:
        xs = np.array([x0 - 0.9, x0 + 0.9])
        ax2.plot(xs, y0 + slope * (xs - x0), color=col, lw=1.3, zorder=5)
    ax2.plot([6, 8], [8, 6], "o", color=fs.GREEN, ms=7, zorder=6)
    ax2.plot([4], [5], "o", color=fs.ORANGE, ms=7, zorder=6)
    ax2.plot([9], [9], "o", color=fs.RED, ms=7, zorder=6)
    ax2.text(5.0, 7.7, "slope −3/4", color=fs.DARK, fontsize=9, ha="right", va="center")
    ax2.text(7.0, 4.3, "slope −4/3", color=fs.DARK, fontsize=9, ha="center", va="center")
    ax2.text(3.7, 4.6, "inefficient", color=fs.ORANGE, fontsize=9.5, ha="right", va="top")
    ax2.text(9.3, 9.0, "unattainable", color=fs.RED, fontsize=9.5, ha="left", va="center")
    ax2.text(1.0, 12.4, "after growth", color=fs.BLUE, fontsize=9.5, ha="left", va="bottom")
    ax2.text(1.0, 10.4, "today's PPC", color=fs.GREEN, fontsize=9.5, ha="left", va="bottom")
    ax2.set_xlim(0, 14.5)
    ax2.set_ylim(0, 13.5)
    ax2.set_xticks([0, 4, 8, 12])
    ax2.set_yticks([0, 4, 8, 12])
    ax2.set_xlabel("wheat (thousand tonnes)", fontsize=9.5)
    ax2.set_ylabel("canola (thousand tonnes)", fontsize=9.5)
    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-ppc")


if __name__ == "__main__":
    ppc()
