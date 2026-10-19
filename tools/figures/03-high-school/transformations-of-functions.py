"""Figures for docs/03-high-school/03-functions/04-transformations-of-functions.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/transformations-of-functions.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "transformations-of-functions"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def frange(a, b, n=400):
    return [a + (b - a) * i / n for i in range(n + 1)]


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


def dot(ax, x, y, color, filled=True):
    if filled:
        ax.plot([x], [y], "o", color=color, ms=6, zorder=6)
    else:
        ax.plot([x], [y], "o", mfc="white", mec=color, ms=6, mew=1.5, zorder=6)


def shifts():
    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.8))
    ax = axes[0]
    through_zero(ax, (-3.6, 3.6), (-4.2, 7.6), [-3, -2, -1, 1, 2, 3], [-4, -2, 2, 4, 6])
    xs = frange(-2.6, 2.6)
    ax.plot(xs, [t * t for t in xs], color=fs.GRAY, lw=1.6, zorder=3)
    ax.plot(xs, [t * t + 2 for t in xs], color=fs.GREEN, zorder=4)
    ax.plot(xs, [t * t - 3 for t in xs], color=fs.ORANGE, zorder=4)
    ax.text(0, 4.6, "x² + 2", color=fs.GREEN, fontsize=10, ha="center", va="center", bbox=BOX)
    ax.text(2.0, 1.0, "x²", color=fs.GRAY, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(0.5, -3.6, f"x² {M} 3", color=fs.ORANGE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(-3.4, 7.0, "vertical shifts: f(x) + k", fontsize=9.5, ha="left", va="center")
    ax = axes[1]
    through_zero(ax, (-5.6, 5.6), (-1.4, 8.2), [-4, -2, 2, 4], [2, 4, 6])
    xs = frange(-2.8, 2.8)
    ax.plot([t for t in xs], [t * t for t in xs], color=fs.GRAY, lw=1.6, zorder=3)
    xr = frange(-0.8, 4.8)
    ax.plot(xr, [(t - 2) ** 2 for t in xr], color=fs.GREEN, zorder=4)
    xl = frange(-5.2, 0.8)
    ax.plot(xl, [(t + 3) ** 2 for t in xl], color=fs.ORANGE, zorder=4)
    ax.text(3.4, 1.2, f"(x {M} 2)²", color=fs.GREEN, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(-5.3, 7.3, "(x + 3)²", color=fs.ORANGE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(1.3, 6.3, "x²", color=fs.GRAY, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(-5.4, -0.95, "horizontal shifts: f(x − h)", fontsize=9.5, ha="left", va="center")
    for px, col in ((2, fs.GREEN), (-3, fs.ORANGE)):
        dot(ax, px, 0, col)
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-shifts")


def scaling():
    def f(x):
        return x**3 - 3 * x

    fig, axes = plt.subplots(1, 2, figsize=(7.4, 3.9))
    ax = axes[0]
    through_zero(ax, (-4.7, 4.7), (-6.6, 6.6), [-4, -2, 2, 4], [-6, -4, -2, 2, 4, 6])
    xs = frange(-2, 2)
    ax.plot(xs, [f(t) for t in xs], color=fs.GRAY, lw=1.6, zorder=3)
    ax.plot(xs, [2 * f(t) for t in xs], color=fs.GREEN, zorder=4)
    ax.plot(xs, [0.5 * f(t) for t in xs], color=fs.ORANGE, zorder=4)
    ax.text(-1.1, 4.5, "2f(x)", color=fs.GREEN, fontsize=10, ha="right", va="center", bbox=BOX)
    ax.text(-1.0, 2.2, "f(x)", color=fs.GRAY, fontsize=10, ha="center", va="bottom")
    ax.text(2.15, 1.0, "½f(x)", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax.text(-4.5, 6.0, "vertical stretch and compression", fontsize=9.5, ha="left", va="center")
    ax = axes[1]
    through_zero(ax, (-4.7, 4.7), (-3.6, 3.6), [-4, -2, 2, 4], [-3, -2, -1, 1, 2, 3])
    xs = frange(-2, 2)
    ax.plot(xs, [f(t) for t in xs], color=fs.GRAY, lw=1.6, zorder=3)
    xc = frange(-1, 1)
    ax.plot(xc, [f(2 * t) for t in xc], color=fs.GREEN, zorder=4)
    xw = frange(-4, 4)
    ax.plot(xw, [f(t / 2) for t in xw], color=fs.ORANGE, zorder=4)
    ax.text(-0.85, 2.9, "f(2x)", color=fs.GREEN, fontsize=10, ha="right", va="center", bbox=BOX)
    ax.text(2.1, 1.0, "f(x)", color=fs.GRAY, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(3.3, -1.5, "f(x/2)", color=fs.ORANGE, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(-4.5, 3.25, "horizontal compression and stretch", fontsize=9.5, ha="left", va="center")
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-scaling")


def reflections():
    fig, ax = fs.figure(5.0, 4.2)
    through_zero(ax, (-5.4, 5.4), (-4.4, 4.4), [-4, -2, 2, 4], [-4, -2, 2, 4])
    xs = frange(0, 4.6)
    r = [math.sqrt(t) for t in xs]
    ax.plot(xs, r, color=fs.GREEN, zorder=4)
    ax.plot(xs, [-v for v in r], color=fs.BLUE, zorder=4)
    ax.plot([-t for t in xs], r, color=fs.ORANGE, zorder=4)
    ax.plot([-t for t in xs], [-v for v in r], color=fs.RED, zorder=4)
    ax.text(3.2, 2.6, "√x", color=fs.GREEN, fontsize=10.5, ha="left", va="center", bbox=BOX)
    ax.text(3.2, -2.6, "−√x", color=fs.BLUE, fontsize=10.5, ha="left", va="center", bbox=BOX)
    ax.text(-3.2, 2.6, "√(−x)", color=fs.ORANGE, fontsize=10.5, ha="right", va="center", bbox=BOX)
    ax.text(-3.2, -2.6, "−√(−x)", color=fs.RED, fontsize=10.5, ha="right", va="center", bbox=BOX)
    for px, py in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        dot(ax, px, py, fs.DARK)
    fs.save(fig, FOLDER, f"{SLUG}-reflections")


def steps():
    """g(x) = -2 sqrt(x + 3) + 1 built from key points of sqrt(x)."""
    fig, ax = fs.figure(6.0, 4.3)
    through_zero(ax, (-4.6, 10.4), (-6.8, 4.2), [-4, -2, 2, 4, 6, 8, 10], [-6, -4, -2, 2, 4])
    xs = frange(0, 10)
    ax.plot(xs, [math.sqrt(t) for t in xs], color=fs.GRAY, lw=1.6, ls="--", zorder=3)
    xg = frange(-3, 7)
    ax.plot(xg, [-2 * math.sqrt(t + 3) + 1 for t in xg], color=fs.GREEN, zorder=4)
    parent = [(0, 0), (1, 1), (4, 2), (9, 3)]
    image = [(-3, 1), (-2, -1), (1, -3), (6, -5)]
    for (px, py), (qx, qy) in zip(parent, image):
        dot(ax, px, py, fs.GRAY)
        dot(ax, qx, qy, fs.GREEN)
        ax.annotate("", xy=(qx, qy), xytext=(px, py),
                    arrowprops=dict(arrowstyle="-|>", color=fs.GRAY, lw=0.9, shrinkA=4, shrinkB=4, alpha=0.8))
    ax.text(9.0, 3.6, "√x", color=fs.GRAY, fontsize=10.5, ha="center", va="center")
    ax.text(6.3, -3.6, f"{M}2√(x + 3) + 1", color=fs.GREEN, fontsize=10.5, ha="left", va="center", bbox=BOX)
    ax.text(-3.0, 1.6, f"({M}3, 1)", fontsize=9, ha="left", va="bottom")
    ax.text(-2.0, -1.5, f"({M}2, {M}1)", fontsize=9, ha="right", va="top")
    ax.text(0.75, -3.0, f"(1, {M}3)", fontsize=9, ha="right", va="center")
    ax.text(6.0, -5.5, f"(6, {M}5)", fontsize=9, ha="center", va="top")
    fs.save(fig, FOLDER, f"{SLUG}-steps")


def order():
    """Reflect then shift, versus shift then reflect, for sqrt(x)."""
    fig, ax = fs.figure(6.0, 3.6)
    through_zero(ax, (-8.4, 8.4), (-0.9, 3.6), [-8, -6, -4, -2, 2, 4, 6, 8], [1, 2, 3])
    xs = frange(0, 8)
    ax.plot(xs, [math.sqrt(t) for t in xs], color=fs.GRAY, lw=1.6, ls="--", zorder=3)
    xa = frange(-6, 2)
    ax.plot(xa, [math.sqrt(2 - t) for t in xa], color=fs.GREEN, zorder=4)
    xb = frange(-8.2, -2)
    ax.plot(xb, [math.sqrt(-t - 2) for t in xb], color=fs.ORANGE, zorder=4)
    dot(ax, 0, 0, fs.GRAY)
    dot(ax, 2, 0, fs.GREEN)
    dot(ax, -2, 0, fs.ORANGE)
    ax.text(6.4, 1.8, "√x", color=fs.GRAY, fontsize=10.5, ha="left", va="center")
    ax.text(-1.5, 2.3, "√(2 − x)", color=fs.GREEN, fontsize=10.5, ha="left", va="center", bbox=BOX)
    ax.text(-8.2, 2.9, "√(−x − 2)", color=fs.ORANGE, fontsize=10.5, ha="left", va="center", bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-order")


if __name__ == "__main__":
    shifts()
    scaling()
    reflections()
    steps()
    order()
