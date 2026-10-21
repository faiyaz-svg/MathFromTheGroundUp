"""Figures for docs/05-university-core/05-sequences-and-series/03-convergence-tests.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/convergence-tests.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "convergence-tests"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def grid(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def integral_test():
    """Rectangles under and over y = 1/x on [1, 7]."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.8), sharey=True)
    x = np.linspace(1, 7, 300)
    for ax in (a, b):
        grid(ax)
        ax.plot(x, 1 / x, color=fs.DARK, lw=2.2, zorder=4)
        ax.set_xlim(0.7, 7.5)
        ax.set_ylim(0, 1.15)
        ax.set_xticks(range(1, 8))
        ax.set_xlabel("x")
    for k in range(1, 7):
        a.add_patch(Rectangle((k, 0), 1, 1 / (k + 1), facecolor=fs.GREEN, alpha=0.4, edgecolor=fs.GREEN, lw=1.0, zorder=3))
        b.add_patch(Rectangle((k, 0), 1, 1 / k, facecolor=fs.RED, alpha=0.3, edgecolor=fs.RED, lw=1.0, zorder=3))
    a.text(2.7, 0.95, "rectangles below the curve:\n1/2 + 1/3 + … + 1/7 ≤ ∫₁⁷ dx/x", color=fs.GREEN, fontsize=9.5, ha="left", va="center")
    b.text(2.4, 0.95,"rectangles above the curve:\n∫₁⁷ dx/x ≤ 1 + 1/2 + … + 1/6", color=fs.RED, fontsize=9.5, ha="left", va="center", bbox=BOX)
    a.set_ylabel("y")
    fs.save(fig, FOLDER, f"{SLUG}-integral-test")


def alternating():
    """Partial sums of 1 - 1/2 + 1/3 - ... zigzag around ln 2."""
    fig, ax = fs.figure(6.2, 3.8)
    grid(ax)
    n = np.arange(1, 13)
    s = np.cumsum([(-1) ** (k - 1) / k for k in n])
    ax.axhline(math.log(2), color=fs.DARK, lw=1.2, ls="--")
    ax.plot(n, s, "-", color=fs.GRAY, lw=1.0, zorder=2)
    ax.plot(n[::2], s[::2], "o", color=fs.RED, ms=6.5, zorder=4)
    ax.plot(n[1::2], s[1::2], "o", color=fs.BLUE, ms=6.5, zorder=4)
    ax.text(15.3, math.log(2) + 0.015, "ln 2 ≈ 0.693", color=fs.DARK, fontsize=10, ha="right", va="bottom")
    ax.text(1.15, 0.97, "S₁ = 1", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax.text(2.0, 0.34, "S₂ = 0.5", color=fs.RED, fontsize=9.5, ha="center", va="top")
    ax.text(5.5, 0.97, "odd partial sums sit above ln 2,\neven partial sums sit below it", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax.set_xlim(0, 15.5)
    ax.set_ylim(0.3, 1.1)
    ax.set_xticks(range(0, 13, 2))
    ax.set_xlabel("n")
    fs.save(fig, FOLDER, f"{SLUG}-alternating")


def harmonic_bounds():
    """H_n squeezed between ln(n+1) and 1 + ln n."""
    fig, ax = fs.figure(6.2, 3.9)
    grid(ax)
    n = np.arange(1, 31)
    h = np.cumsum(1.0 / n)
    t = np.linspace(1, 30, 300)
    ax.fill_between(t, np.log(t + 1), 1 + np.log(t), color=fs.GREEN, alpha=0.15, lw=0)
    ax.plot(t, np.log(t + 1), color=fs.BLUE, lw=1.6)
    ax.plot(t, 1 + np.log(t), color=fs.ORANGE, lw=1.6)
    ax.plot(n, h, "o", color=fs.RED, ms=4.5, zorder=5)
    ax.text(30.4, 1 + math.log(30), "1 + ln n", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax.text(30.4, math.log(31) - 0.05, "ln(n + 1)", color=fs.BLUE, fontsize=10, ha="left", va="center")
    ax.text(30.4, h[-1] + 0.05, "Hₙ", color=fs.RED, fontsize=10, ha="left", va="center")
    ax.set_xlim(0, 36)
    ax.set_ylim(0, 4.8)
    ax.set_xlabel("n")
    fs.save(fig, FOLDER, f"{SLUG}-harmonic-bounds")


if __name__ == "__main__":
    integral_test()
    alternating()
    harmonic_bounds()
