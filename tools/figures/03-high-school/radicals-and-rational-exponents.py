"""Figures for docs/03-high-school/04-radicals-and-polynomials/01-radicals-and-rational-exponents.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/radicals-and-rational-exponents.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "radicals-and-rational-exponents"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def plane(ax, lo, hi, step=1, size=9):
    """Axes through the origin with a light grid and equal units."""
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ticks = list(range(int(lo), int(hi) + 1))
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for t in ticks:
        if t != 0 and t % step == 0:
            ax.text(t, -0.2, num(t), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
            ax.text(-0.2, t, num(t), ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)
    ax.text(hi, 0.25, "x", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.25, hi, "y", ha="left", va="top", style="italic", fontsize=12)


def roots_and_powers():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.6, 3.9))

    # Left: squares and square roots, for x >= 0 only.
    plane(ax1, -1, 5, step=1, size=8)
    t = np.linspace(0, 2.2, 200)
    ax1.plot(t, t**2, color=fs.BLUE, zorder=3)
    s = np.linspace(0, 5, 300)
    ax1.plot(s, np.sqrt(s), color=fs.GREEN, zorder=3)
    ax1.plot([-1, 5], [-1, 5], color=fs.GRAY, lw=1.2, ls=(0, (4, 3)), zorder=2)
    for p in [(1, 1), (2, 4), (4, 2)]:
        ax1.plot(*p, "o", color=fs.DARK, zorder=5, ms=4)
    ax1.text(2.35, 4.3, r"$y = x^2$", color=fs.BLUE, fontsize=10, ha="left", va="center", bbox=BOX, zorder=6)
    ax1.text(4.2, 2.05, r"$y = x^{1/2}$", color=fs.GREEN, fontsize=10, ha="left", va="bottom", bbox=BOX, zorder=6)
    ax1.text(3.0, 3.35, r"$y = x$", color=fs.GRAY, fontsize=9, ha="left", va="top", rotation=0, bbox=BOX, zorder=6)
    ax1.text(0.5, -0.02, "even index: only $x \\geq 0$", transform=ax1.transAxes, ha="center", va="top", fontsize=10)

    # Right: cubes and cube roots, for all x.
    plane(ax2, -4, 4, step=1, size=8)
    t = np.linspace(-1.58, 1.58, 300)
    ax2.plot(t, t**3, color=fs.BLUE, zorder=3)
    s = np.linspace(-4, 4, 400)
    ax2.plot(s, np.cbrt(s), color=fs.GREEN, zorder=3)
    ax2.plot([-4, 4], [-4, 4], color=fs.GRAY, lw=1.2, ls=(0, (4, 3)), zorder=2)
    ax2.plot([1, -1], [1, -1], "o", color=fs.DARK, zorder=5, ms=4)
    ax2.text(1.75, 3.4, r"$y = x^3$", color=fs.BLUE, fontsize=10, ha="left", va="center", bbox=BOX, zorder=6)
    ax2.text(-3.9, -1.75, r"$y = x^{1/3}$", color=fs.GREEN, fontsize=10, ha="left", va="top", bbox=BOX, zorder=6)
    ax2.text(2.2, 2.7, r"$y = x$", color=fs.GRAY, fontsize=9, ha="left", va="top", bbox=BOX, zorder=6)
    ax2.text(0.5, -0.02, "odd index: every $x$", transform=ax2.transAxes, ha="center", va="top", fontsize=10)

    fig.tight_layout(w_pad=2.0)
    fs.save(fig, FOLDER, f"{SLUG}-roots-and-powers")


if __name__ == "__main__":
    roots_and_powers()
