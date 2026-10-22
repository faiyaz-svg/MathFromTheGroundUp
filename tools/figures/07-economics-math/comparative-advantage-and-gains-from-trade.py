"""Figure for docs/07-economics-math/02-markets/02-comparative-advantage-and-gains-from-trade.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/comparative-advantage-and-gains-from-trade.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "comparative-advantage-and-gains-from-trade"


def style(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def panel(ax, name, xmax, ymax, before, spec, after, x0, y0):
    """PPC from (xmax, 0) to (0, ymax); trade line of slope -0.75 through the specialization point."""
    style(ax)
    x = np.array([0, xmax])
    ax.fill_between(x, 0, ymax * (1 - x / xmax), color=fs.GREEN, alpha=0.10, zorder=1)
    ax.plot(x, ymax * (1 - x / xmax), color=fs.GREEN, lw=2.4, zorder=4)
    # trade line through the specialization point with slope -0.75 (cloth per wheat)
    xs = np.array([0, 640])
    ax.plot(xs, spec[1] - 0.75 * (xs - spec[0]), color=fs.BLUE, lw=1.8, ls="--", zorder=3)
    ax.plot(*before, "o", color=fs.ORANGE, ms=8, zorder=6)
    ax.plot(*spec, "s", color=fs.DARK, ms=7, zorder=6)
    ax.plot(*after, "o", color=fs.BLUE, ms=8, zorder=6)
    ax.set_xlim(0, 730)
    ax.set_ylim(0, 520)
    ax.set_xticks([0, 200, 400, 600])
    ax.set_yticks([0, 100, 200, 300, 400])
    ax.set_xlabel("wheat (bushels)", fontsize=9.5)
    ax.set_ylabel("cloth (bolts)", fontsize=9.5)
    ax.set_title(name, fontsize=10.5, color=fs.DARK, loc="left")


def trade():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.1))
    # A: PPC (600, 0) to (0, 300); before (300, 150); specialize (600, 0); after (360, 180)
    panel(ax1, "Northland", 600, 300, (300, 150), (600, 0), (360, 180), 600, 0)
    ax1.text(290, 128, "no trade\n(300, 150)", color=fs.ORANGE, fontsize=9.5, ha="right", va="top")
    ax1.text(372, 196, "with trade\n(360, 180)", color=fs.BLUE, fontsize=9.5, ha="left", va="bottom")
    ax1.text(615, 35, "specialize\n(600, 0)", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax1.text(60, 285, "PPC", color=fs.GREEN, fontsize=10, ha="left", va="bottom")
    ax1.text(300, 400, "trade line,\nslope −3/4", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    # B: PPC (400, 0) to (0, 400); before (200, 200); specialize (0, 400); after (240, 220)
    panel(ax2, "Southland", 400, 400, (200, 200), (0, 400), (240, 220), 0, 400)
    ax2.text(190, 184, "no trade\n(200, 200)", color=fs.ORANGE, fontsize=9.5, ha="right", va="top")
    ax2.text(252, 228, "with trade\n(240, 220)", color=fs.BLUE, fontsize=9.5, ha="left", va="bottom")
    ax2.text(20, 425, "specialize\n(0, 400)", color=fs.DARK, fontsize=9.5, ha="left", va="bottom")
    ax2.text(60, 60, "PPC", color=fs.GREEN, fontsize=10, ha="left", va="bottom")
    ax2.text(430, 120, "trade line,\nslope −3/4", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-trade")


if __name__ == "__main__":
    trade()
