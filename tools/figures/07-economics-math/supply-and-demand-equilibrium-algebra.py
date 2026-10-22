"""Figure for docs/07-economics-math/02-markets/03-supply-and-demand-equilibrium-algebra.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/supply-and-demand-equilibrium-algebra.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "supply-and-demand-equilibrium-algebra"


def style(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def equilibrium():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.4, 4.0))
    # Left: Qd = 120 - 20P (P = 6 - Q/20), Qs = 10P (P = Q/10), demand shift Qd = 150 - 20P (P = 7.5 - Q/20)
    style(ax1)
    q = np.linspace(0, 120, 200)
    ax1.plot(q, 6 - q / 20, color=fs.BLUE, lw=2.3, zorder=4)
    ax1.plot(q, 7.5 - q / 20, color=fs.BLUE, lw=1.8, ls="--", zorder=3)
    ax1.plot(q, q / 10, color=fs.ORANGE, lw=2.3, zorder=4)
    ax1.plot([40, 40], [0, 4], color=fs.DARK, lw=1, ls=":", zorder=2)
    ax1.plot([0, 40], [4, 4], color=fs.DARK, lw=1, ls=":", zorder=2)
    ax1.plot([50, 50], [0, 5], color=fs.DARK, lw=1, ls=":", zorder=2)
    ax1.plot([0, 50], [5, 5], color=fs.DARK, lw=1, ls=":", zorder=2)
    ax1.plot([40], [4], "o", color=fs.DARK, ms=7, zorder=6)
    ax1.plot([50], [5], "o", color=fs.DARK, ms=7, zorder=6)
    ax1.annotate("", xy=(48.6, 5.0), xytext=(41.4, 4.1), arrowprops=dict(arrowstyle="->", color=fs.DARK, lw=1.2))
    ax1.text(42, 1.9,"old equilibrium\n(40, 4)", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax1.text(53, 5.35, "new equilibrium\n(50, 5)", color=fs.DARK, fontsize=9.5, ha="left", va="bottom")
    ax1.text(62, 0.5, "demand P = 6 − Q/20", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax1.text(3, 7.9, "demand after shift", color=fs.BLUE, fontsize=9.5, ha="left", va="bottom")
    ax1.text(96, 7.6, "supply\nP = Q/10", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    ax1.set_xlim(0, 125)
    ax1.set_ylim(0, 10.5)
    ax1.set_xticks([0, 40, 50, 80, 120])
    ax1.set_yticks([0, 2, 4, 5, 6, 8, 10])
    ax1.set_xlabel("quantity Q (cups per day)", fontsize=9.5)
    ax1.set_ylabel("price P (dollars)", fontsize=9.5)
    ax1.set_title("A shift of demand", fontsize=10.5, color=fs.DARK, loc="left")

    # Right: kinked market demand and supply Qs = 2P - 6 (P = (Q + 6)/2)
    style(ax2)
    q1 = np.linspace(0, 6, 50)
    ax2.plot(np.linspace(0, 5, 20), 5 - 0.5 * np.linspace(0, 5, 20) * 0, color="none")
    # buyer 1: P = 5 - Q/2 for Q in [0, 10]; buyer 2: P = 8 - Q/2 for Q in [0, 16]
    b1 = np.linspace(0, 10, 50)
    b2 = np.linspace(0, 16, 50)
    ax2.plot(b1, 5 - b1 / 2, color=fs.GRAY, lw=1.4, zorder=3)
    ax2.plot(b2, 8 - b2 / 2, color=fs.GRAY, lw=1.4, zorder=3)
    qa = np.linspace(0, 6, 50)
    qb = np.linspace(6, 26, 50)
    ax2.plot(qa, (16 - qa) / 2, color=fs.BLUE, lw=2.6, zorder=5)
    ax2.plot(qb, (26 - qb) / 4, color=fs.BLUE, lw=2.6, zorder=5)
    qs = np.linspace(0, 20, 50)
    ax2.plot(qs, (qs + 6) / 2, color=fs.ORANGE, lw=2.3, zorder=4)
    ax2.plot([6], [5], "o", color=fs.BLUE, ms=7, zorder=6)
    ax2.plot([5], [5.5], "o", color=fs.DARK, ms=7, zorder=7)
    ax2.annotate("kink (6, 5)", xy=(6.1, 5.1), xytext=(9.5, 6.3), color=fs.BLUE, fontsize=9.5,
                 ha="left", va="center", arrowprops=dict(arrowstyle="->", color=fs.BLUE, lw=1.1))
    ax2.annotate("equilibrium (5, 5.5)", xy=(5, 5.5), xytext=(1.0, 8.5), color=fs.DARK, fontsize=9.5,
                 ha="left", va="center", arrowprops=dict(arrowstyle="->", color=fs.DARK, lw=1.1))
    ax2.text(16.2, 7.6, "buyer 2", color=fs.GRAY, fontsize=9.5, ha="left", va="center")
    ax2.text(10.2, 0.3, "buyer 1", color=fs.GRAY, fontsize=9.5, ha="left", va="center")
    ax2.text(20.5, 6.0, "supply", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    ax2.text(15, 4.7, "market demand\n(sum of the two)", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax2.set_xlim(0, 28)
    ax2.set_ylim(0, 9)
    ax2.set_xticks([0, 5, 10, 15, 20, 25])
    ax2.set_yticks([0, 2, 4, 5, 6, 8])
    ax2.set_xlabel("quantity Q", fontsize=9.5)
    ax2.set_ylabel("price P", fontsize=9.5)
    ax2.set_title("Adding two buyers horizontally", fontsize=10.5, color=fs.DARK, loc="left")
    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-equilibrium")


if __name__ == "__main__":
    equilibrium()
