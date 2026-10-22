"""Figures for docs/07-economics-math/04-more-tools/02-multipliers-and-the-ad-as-model.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/07-economics-math/multipliers-and-the-ad-as-model.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "07-economics-math"
SLUG = "multipliers-and-the-ad-as-model"


def style(ax):
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, length=3)


def cross():
    """Keynesian cross: planned spending against income, with a rise in G of 100."""
    fig, ax = fs.figure(6.2, 4.2)
    style(ax)
    lo, hi = 3600, 6300
    y = np.linspace(lo, hi, 100)
    ax.plot(y, y, color=fs.GRAY, lw=1.6)
    ax.plot(y, 1000 + 0.8 * y, color=fs.GREEN, lw=2.2)
    ax.plot(y, 1100 + 0.8 * y, color=fs.ORANGE, lw=2.2)
    for yy, col in ((5000, fs.GREEN), (5500, fs.ORANGE)):
        ax.plot([yy, yy], [lo, yy], color=col, lw=1.0, ls="--")
        ax.plot([yy], [yy], "o", color=col, zorder=5)
    ax.annotate("", xy=(5500, 3800), xytext=(5000, 3800), arrowprops=dict(arrowstyle="->", color=fs.DARK, lw=1.4))
    ax.text(5250, 3860, "+500", ha="center", color=fs.DARK, fontsize=10)
    ax.text(5000 - 40, 5120, "A", ha="right", color=fs.GREEN, fontsize=10.5)
    ax.text(5500 - 40, 5620, "B", ha="right", color=fs.ORANGE, fontsize=10.5)
    ax.annotate("spending = income", xy=(4300, 4300), xytext=(3700, 5000), color=fs.GRAY, fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=fs.GRAY, lw=0.8))
    ax.text(6330, 5990, "1000 + 0.8Y", color=fs.GREEN, fontsize=9.5, ha="left", va="center")
    ax.text(6330, 6200, "1100 + 0.8Y (G up)", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    ax.set_xlim(lo, 7300)
    ax.set_ylim(lo, 6400)
    ax.set_xticks([3600, 4000, 4500, 5000, 5500, 6000])
    ax.set_xlabel("income Y")
    ax.set_ylabel("planned spending")
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-cross")


def adas():
    """AD-AS: AD shifts right by 500, short-run and long-run results."""
    fig, ax = fs.figure(5.8, 4.2)
    style(ax)
    yy = np.linspace(3900, 6800, 100)
    ax.plot(yy, (7000 - yy) / 20, color=fs.BLUE, lw=2.2)
    ax.plot(yy, (7500 - yy) / 20, color=fs.BLUE, lw=2.2, ls="--")
    ax.plot(yy, 0.02 * yy, color=fs.RED, lw=2.2)
    ax.axvline(5000, color=fs.DARK, lw=1.8)
    ys = 7500 / 1.4
    for x, p, col, lab, dx, dy in (
        (5000, 100, fs.DARK, "A", 60, -3.0),
        (ys, 0.02 * ys, fs.ORANGE, "B", 60, -3.0),
        (5000, 125, fs.GREEN, "C", 60, 1.0),
    ):
        ax.plot([x], [p], "o", color=col, zorder=5)
        ax.text(x + dx, p + dy, lab, color=col, fontsize=10.5, ha="left", va="center")
    ax.text(5300, 88, "AD", color=fs.BLUE, fontsize=9, ha="left", va="center")
    ax.text(5800, 88, "AD (G up)", color=fs.BLUE, fontsize=9, ha="left", va="center")
    ax.text(6850, 136, "short-run AS", color=fs.RED, fontsize=9.5, ha="left", va="center")
    ax.text(5030, 138, "long-run AS", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax.set_xlim(3500, 7500)
    ax.set_ylim(84, 140)
    ax.set_xlabel("real output Y")
    ax.set_ylabel("price level P")
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-adas")


if __name__ == "__main__":
    cross()
    adas()
