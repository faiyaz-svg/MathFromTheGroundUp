"""Figure for docs/07-economics-math/02-markets/04-surplus-and-market-interventions.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/surplus-and-market-interventions.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon, Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "surplus-and-market-interventions"


def style(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def poly(ax, pts, color, alpha, z=2):
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, alpha=alpha, edgecolor="none", zorder=z))


def note(ax, text, xy, xytext, color, ha="left"):
    ax.annotate(text, xy=xy, xytext=xytext, color=color, fontsize=9.5, ha=ha, va="center",
                arrowprops=dict(arrowstyle="->", color=color, lw=1.1))


def surplus():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.2))
    q = np.linspace(0, 80, 200)
    # Left: consumer and producer surplus at the equilibrium (40, 4)
    style(ax1)
    poly(ax1, [(0, 6), (0, 4), (40, 4)], fs.BLUE, 0.28)
    poly(ax1, [(0, 0), (0, 4), (40, 4)], fs.ORANGE, 0.30)
    ax1.plot(q, 6 - q / 20, color=fs.BLUE, lw=2.3, zorder=4)
    ax1.plot(q, q / 10, color=fs.ORANGE, lw=2.3, zorder=4)
    ax1.plot([0, 40], [4, 4], color=fs.DARK, lw=1.1, ls="--", zorder=3)
    ax1.plot([40, 40], [0, 4], color=fs.DARK, lw=1.1, ls="--", zorder=3)
    ax1.plot([40], [4], "o", color=fs.DARK, ms=7, zorder=6)
    note(ax1, "consumer surplus = 40", (12, 4.6), (30, 6.9), fs.BLUE)
    note(ax1, "producer surplus = 80", (14, 2.0), (36, 0.8), fs.ORANGE)
    ax1.text(43, 3.4, "(40, 4)", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax1.text(58, 2.0, "demand", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax1.text(52, 6.4, "supply", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    ax1.set_xlim(0, 80)
    ax1.set_ylim(0, 8)
    ax1.set_xticks([0, 20, 40, 60, 80])
    ax1.set_yticks([0, 2, 4, 6, 8])
    ax1.set_xlabel("quantity Q (cups per day)", fontsize=9.5)
    ax1.set_ylabel("price P (dollars)", fontsize=9.5)
    ax1.set_title("Surplus with no tax", fontsize=10.5, color=fs.DARK, loc="left")

    # Right: a $3 per-unit tax; buyers pay 5, sellers keep 2, quantity 20
    style(ax2)
    ax2.add_patch(Rectangle((0, 2), 20, 3, facecolor=fs.GREEN, alpha=0.30, edgecolor="none", zorder=2))
    poly(ax2, [(20, 5), (20, 2), (40, 4)], fs.RED, 0.35)
    poly(ax2, [(0, 6), (0, 5), (20, 5)], fs.BLUE, 0.28)
    poly(ax2, [(0, 0), (0, 2), (20, 2)], fs.ORANGE, 0.30)
    ax2.plot(q, 6 - q / 20, color=fs.BLUE, lw=2.3, zorder=4)
    ax2.plot(q, q / 10, color=fs.ORANGE, lw=2.3, zorder=4)
    ax2.plot(q, q / 10 + 3, color=fs.ORANGE, lw=1.8, ls="--", zorder=3)
    ax2.plot([20, 20], [0, 5], color=fs.DARK, lw=1.1, ls="--", zorder=3)
    ax2.plot([0, 20], [5, 5], color=fs.DARK, lw=1.1, ls=":", zorder=3)
    ax2.plot([0, 20], [2, 2], color=fs.DARK, lw=1.1, ls=":", zorder=3)
    ax2.plot([20, 20, 40], [5, 2, 4], "o", color=fs.DARK, ms=6, zorder=6, linestyle="none")
    ax2.text(8, 2.9, "tax revenue\n= 60", color=fs.DARK, fontsize=9.5, ha="center", va="center")
    note(ax2, "consumer surplus = 10", (6, 5.4), (2, 7.2), fs.BLUE)
    note(ax2, "producer surplus = 20", (10, 1.4), (30, 0.7), fs.ORANGE)
    note(ax2, "deadweight loss = 30", (28, 3.7), (46, 1.5), fs.RED)
    ax2.text(22, 8.4, "supply + \\$3 tax", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    ax2.text(66, 5.3, "supply", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    ax2.text(62, 3.55, "demand", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax2.set_xlim(0, 80)
    ax2.set_ylim(0, 9)
    ax2.set_xticks([0, 20, 40, 60, 80])
    ax2.set_yticks([0, 2, 4, 5, 6, 8])
    ax2.set_xlabel("quantity Q (cups per day)", fontsize=9.5)
    ax2.set_ylabel("price P (dollars)", fontsize=9.5)
    ax2.set_title("A \\$3 per-unit tax", fontsize=10.5, color=fs.DARK, loc="left")
    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-surplus")


if __name__ == "__main__":
    surplus()
