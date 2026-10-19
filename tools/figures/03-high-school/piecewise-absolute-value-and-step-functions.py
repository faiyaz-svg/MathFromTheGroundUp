"""Figures for docs/03-high-school/03-functions/03-piecewise-absolute-value-and-step-functions.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/piecewise-absolute-value-and-step-functions.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "piecewise-absolute-value-and-step-functions"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)


def through_zero(ax, xlim, ylim, xticks, yticks, size=9):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks([t for t in xticks if t != 0])
    ax.set_yticks([t for t in yticks if t != 0])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=size, length=3)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def plain_axes(ax, xlim, ylim, xticks, yticks, size=9):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=size)


def closed(ax, x, y, color):
    ax.plot([x], [y], "o", color=color, ms=7, zorder=6, clip_on=False)


def opened(ax, x, y, color):
    ax.plot([x], [y], "o", mfc="white", mec=color, ms=7, mew=1.7, zorder=6, clip_on=False)


def seg(ax, x0, x1, fn, color, n=2):
    xs = [x0 + (x1 - x0) * i / n for i in range(n + 1)]
    ax.plot(xs, [fn(t) for t in xs], color=color, zorder=4, solid_capstyle="butt")


def piecewise_example():
    """f(x) = 2x + 1 (x < 1), 5 - x (1 <= x <= 3), x - 1 (x > 3)."""
    fig, ax = fs.figure(6.0, 4.2)
    through_zero(ax, (-3.2, 6.7), (-4.2, 6.2), [-3, -2, -1, 1, 2, 3, 4, 5, 6], [-4, -3, -2, -1, 1, 2, 3, 4, 5, 6])
    seg(ax, -2.6, 1, lambda t: 2 * t + 1, fs.BLUE)
    seg(ax, 1, 3, lambda t: 5 - t, fs.GREEN)
    seg(ax, 3, 6.4, lambda t: t - 1, fs.ORANGE)
    opened(ax, 1, 3, fs.BLUE)
    closed(ax, 1, 4, fs.GREEN)
    closed(ax, 3, 2, fs.GREEN)
    ax.text(0.4, -1.5, "y = 2x + 1,  x < 1", color=fs.BLUE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(1.55, 4.55, "y = 5 − x,  1 ≤ x ≤ 3", color=fs.GREEN, fontsize=10, ha="left",
            va="center", bbox=BOX)
    ax.text(4.1, 1.4, "y = x − 1,  x > 3", color=fs.ORANGE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(0.85, 3.0, "(1, 3)", color=fs.BLUE, fontsize=9, ha="right", va="center", bbox=BOX)
    ax.text(0.8, 4.2, "(1, 4)", color=fs.GREEN, fontsize=9, ha="right", va="center", bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-piecewise")


def absolute_value():
    """|x| and g(x) = |x - 3| + |x + 1|, drawn piece by piece."""
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.7))
    ax = axes[0]
    through_zero(ax, (-4.4, 4.7), (-1.0, 4.9), [-4, -3, -2, -1, 1, 2, 3, 4], [1, 2, 3, 4])
    seg(ax, -4, 0, lambda t: -t, fs.BLUE)
    seg(ax, 0, 4, lambda t: t, fs.GREEN)
    closed(ax, 0, 0, fs.GREEN)
    ax.text(-4.2, 1.0, f"y = {M}x\nfor x < 0", color=fs.BLUE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(2.3, 1.0, "y = x\nfor x ≥ 0", color=fs.GREEN, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(0.2, -0.5, "y = |x|", color=fs.DARK, fontsize=10, ha="left", va="center")

    ax = axes[1]
    through_zero(ax, (-4.4, 6.6), (-1.0, 10.4), [-4, -3, -2, -1, 1, 2, 3, 4, 5], [2, 4, 6, 8])
    seg(ax, -3.2, -1, lambda t: -2 * t + 2, fs.BLUE)
    seg(ax, -1, 3, lambda t: 4, fs.GREEN)
    seg(ax, 3, 5.2, lambda t: 2 * t - 2, fs.ORANGE)
    closed(ax, -1, 4, fs.GREEN)
    closed(ax, 3, 4, fs.GREEN)
    ax.text(-4.3, 5.0, f"{M}2x + 2\nfor x < {M}1", color=fs.BLUE, fontsize=9.5, ha="left", va="center", bbox=BOX)
    ax.text(0.2, 2.5, f"4  for  {M}1 ≤ x ≤ 3", color=fs.GREEN, fontsize=9.5, ha="left", va="center", bbox=BOX)
    ax.text(4.1, 4.6, "2x − 2\nfor x > 3", color=fs.ORANGE, fontsize=9.5, ha="left", va="center", bbox=BOX)
    ax.text(-4.3, 9.6, "y = |x − 3| + |x + 1|", color=fs.DARK, fontsize=10, ha="left", va="center")
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-absolute-value")


def floor_ceiling():
    """The floor and ceiling functions on [-3, 3]."""
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.7))
    for ax, kind in zip(axes, ("floor", "ceiling")):
        through_zero(ax, (-3.4, 3.6), (-3.6, 3.7), [-3, -2, -1, 1, 2, 3], [-3, -2, -1, 1, 2, 3])
        ax.set_aspect("equal")
        for n in range(-3, 3):
            if kind == "floor":
                ax.plot([n, n + 1], [n, n], color=fs.GREEN, lw=2.2, zorder=4, solid_capstyle="butt")
                closed(ax, n, n, fs.GREEN)
                opened(ax, n + 1, n, fs.GREEN)
            else:
                ax.plot([n, n + 1], [n + 1, n + 1], color=fs.BLUE, lw=2.2, zorder=4, solid_capstyle="butt")
                opened(ax, n, n + 1, fs.BLUE)
                closed(ax, n + 1, n + 1, fs.BLUE)
        col = fs.GREEN if kind == "floor" else fs.BLUE
        label = "y = ⌊x⌋" if kind == "floor" else "y = ⌈x⌉"
        ax.text(-3.3, 3.0, label, color=col, fontsize=11, ha="left", va="center", bbox=BOX)
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-floor-ceiling")


def parking():
    """C(t) = min(4 * ceil(2t), 22) for 0 < t <= 4, and C(0) = 0."""
    def C(t):
        return 0 if t <= 0 else min(4 * math.ceil(2 * t), 22)

    fig, ax = fs.figure(6.2, 3.7)
    plain_axes(ax, (-0.1, 4.2), (-1, 26), [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4], [0, 4, 8, 12, 16, 20, 22])
    ax.set_xlabel("time parked (hours)")
    ax.set_ylabel("cost (dollars)")
    for k in range(1, 6):  # the k-th step is at 4k for (k - 1) / 2 < t <= k / 2
        lo, hi = (k - 1) / 2, k / 2
        ax.plot([lo, hi], [4 * k, 4 * k], color=fs.GREEN, lw=2.2, zorder=4, solid_capstyle="butt")
        opened(ax, lo, 4 * k, fs.GREEN)
        closed(ax, hi, 4 * k, fs.GREEN)
    ax.plot([2.5, 4.1], [22, 22], color=fs.ORANGE, lw=2.2, zorder=4, solid_capstyle="butt")
    opened(ax, 2.5, 22, fs.ORANGE)
    closed(ax, 0, 0, fs.GREEN)
    opened(ax, 0, 4, fs.GREEN)
    ax.text(3.2, 24.2, "daily maximum $" + "22", color=fs.ORANGE, fontsize=9.5, ha="center", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-parking")


def tax():
    """Hypothetical brackets: 10% to 20,000, 20% to 60,000, 30% above."""
    def T(x):
        if x <= 20000:
            return 0.1 * x
        if x <= 60000:
            return 2000 + 0.2 * (x - 20000)
        return 10000 + 0.3 * (x - 60000)

    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.8))
    ax = axes[0]
    plain_axes(ax, (0, 105000), (0, 25000), [0, 20000, 40000, 60000, 80000, 100000],
               [0, 5000, 10000, 15000, 20000, 25000], size=8.5)
    ax.set_xticklabels(["0", "20", "40", "60", "80", "100"])
    ax.set_yticklabels(["0", "5", "10", "15", "20", "25"])
    ax.set_xlabel("income (thousands of dollars)", fontsize=10)
    ax.set_ylabel("tax owed (thousands of dollars)", fontsize=10)
    xs = [0, 20000, 60000, 100000]
    ax.plot(xs, [T(v) for v in xs], color=fs.BLUE, zorder=4)
    ax.plot([20000, 60000], [T(20000), T(60000)], "o", color=fs.BLUE, zorder=5)
    ax.text(9000, 3800, "slope 0.10", color=fs.BLUE, fontsize=9, ha="center", va="center", rotation=7)
    ax.text(41000, 3400, "slope 0.20", color=fs.BLUE, fontsize=9, ha="center", va="center")
    ax.text(79000, 11500, "slope 0.30", color=fs.BLUE, fontsize=9, ha="center", va="center")
    ax.text(21000, 2300, "(20, 2)", fontsize=8.5, ha="left", va="top")
    ax.text(58500, 10000, "(60, 10)", fontsize=8.5, ha="right", va="bottom")

    ax = axes[1]
    plain_axes(ax, (0, 105000), (0, 0.36), [0, 20000, 40000, 60000, 80000, 100000],
               [0, 0.1, 0.2, 0.3], size=8.5)
    ax.set_xticklabels(["0", "20", "40", "60", "80", "100"])
    ax.set_yticklabels(["0%", "10%", "20%", "30%"])
    ax.set_xlabel("income (thousands of dollars)", fontsize=10)
    ax.set_ylabel("tax rate", fontsize=10)
    for lo, hi, r in ((0, 20000, 0.1), (20000, 60000, 0.2), (60000, 105000, 0.3)):
        ax.plot([lo, hi], [r, r], color=fs.ORANGE, lw=2.2, zorder=4, solid_capstyle="butt")
    ax.plot([20000, 60000], [0.1, 0.2], "o", color=fs.ORANGE, ms=6, zorder=5)
    ax.plot([20000, 60000], [0.2, 0.3], "o", mfc="white", mec=fs.ORANGE, ms=6, mew=1.5, zorder=5)
    xs = [500 + (105000 - 500) * i / 400 for i in range(401)]
    ax.plot(xs, [T(v) / v for v in xs], color=fs.GREEN, zorder=4)
    ax.text(26000, 0.255, "marginal rate (steps)", color=fs.ORANGE, fontsize=9, ha="left", va="center")
    ax.text(48000, 0.075, "average rate\n(tax ÷ income)", color=fs.GREEN, fontsize=9, ha="left", va="center")
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-tax")


if __name__ == "__main__":
    piecewise_example()
    absolute_value()
    floor_ceiling()
    parking()
    tax()
