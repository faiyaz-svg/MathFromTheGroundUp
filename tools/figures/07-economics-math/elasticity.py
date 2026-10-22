"""Figure for docs/07-economics-math/02-markets/05-elasticity.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/elasticity.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "elasticity"


def style(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def linear():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.1))
    # Left: P = 6 - Q/20 with elastic part (P > 3) and inelastic part (P < 3)
    style(ax1)
    qe = np.linspace(0, 60, 50)
    qi = np.linspace(60, 120, 50)
    ax1.plot(qe, 6 - qe / 20, color=fs.RED, lw=2.6, zorder=4)
    ax1.plot(qi, 6 - qi / 20, color=fs.BLUE, lw=2.6, zorder=4)
    for p in (5, 4, 3, 2, 1):
        qq = 120 - 20 * p
        e = 20 * p / qq
        ax1.plot([qq], [p], "o", color=fs.DARK, ms=6, zorder=6)
        label = f"|E| = {e:g}"
        ax1.text(qq + 3, p + 0.28, label, color=fs.DARK, fontsize=9, ha="left", va="center")
    ax1.text(45, 5.75, "elastic: |E| > 1", color=fs.RED, fontsize=9.5, ha="left", va="center")
    ax1.text(76, 0.35, "inelastic: |E| < 1", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax1.set_xlim(0, 130)
    ax1.set_ylim(0, 6.6)
    ax1.set_xticks([0, 20, 40, 60, 80, 100, 120])
    ax1.set_yticks([0, 1, 2, 3, 4, 5, 6])
    ax1.set_xlabel("quantity Q (cups per day)", fontsize=9.5)
    ax1.set_ylabel("price P (dollars)", fontsize=9.5)
    ax1.set_title("Demand P = 6 − Q/20", fontsize=10.5, color=fs.DARK, loc="left")

    # Right: revenue R = Q (6 - Q/20), maximum at Q = 60
    style(ax2)
    q = np.linspace(0, 120, 200)
    r = q * (6 - q / 20)
    ax2.plot(q[q <= 60], r[q <= 60], color=fs.RED, lw=2.6, zorder=4)
    ax2.plot(q[q >= 60], r[q >= 60], color=fs.BLUE, lw=2.6, zorder=4)
    ax2.plot([60], [180], "o", color=fs.DARK, ms=7, zorder=6)
    ax2.plot([60, 60], [0, 180], color=fs.DARK, lw=1, ls=":", zorder=3)
    ax2.text(63, 186, "maximum: Q = 60, P = 3,\nR = 180, |E| = 1", color=fs.DARK, fontsize=9.5, ha="left", va="bottom")
    ax2.text(30, 50, "R rises as Q rises:\nMR > 0", color=fs.RED, fontsize=9.5, ha="left", va="center")
    ax2.text(90, 30, "R falls as Q rises:\nMR < 0", color=fs.BLUE, fontsize=9.5, ha="center", va="center")
    ax2.set_xlim(0, 130)
    ax2.set_ylim(0, 230)
    ax2.set_xticks([0, 20, 40, 60, 80, 100, 120])
    ax2.set_yticks([0, 60, 120, 180])
    ax2.set_xlabel("quantity Q (cups per day)", fontsize=9.5)
    ax2.set_ylabel("revenue R = PQ (dollars)", fontsize=9.5)
    ax2.set_title("Revenue along that demand curve", fontsize=10.5, color=fs.DARK, loc="left")
    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-linear")


if __name__ == "__main__":
    linear()
