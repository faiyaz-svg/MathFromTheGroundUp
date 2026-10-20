"""Figures for docs/03-high-school/06-rational-expressions-and-equations/02-rational-functions-and-asymptotes.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/rational-functions-and-asymptotes.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "rational-functions-and-asymptotes"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def setup(ax, xlim, ylim, xticks, yticks, size=9, origin=True):
    """Axes through the origin with tick labels drawn by hand, as in the polynomial lesson."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="none", edgecolor="none")
    dy = (ylim[1] - ylim[0]) * 0.02
    dx = (xlim[1] - xlim[0]) * 0.012
    for t in xticks:
        if t != 0:
            ax.text(t, -dy, num(t), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
    for t in yticks:
        if t != 0:
            ax.text(-dx, t, num(t), ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def hole(ax, x, y, color=fs.GREEN):
    ax.plot(x, y, "o", mfc="white", mec=color, mew=1.8, ms=7, zorder=6)


def reciprocal():
    fig, (a, b) = plt.subplots(1, 2, figsize=(8.4, 3.8))
    # left: y = 1/x
    setup(a, (-4.4, 4.4), (-4.4, 4.4), [-4, -2, 2, 4], [-4, -2, 2, 4])
    xs = np.linspace(0.23, 4.4, 300)
    a.plot(xs, 1 / xs, color=fs.GREEN, zorder=3)
    a.plot(-xs, -1 / xs, color=fs.GREEN, zorder=3)
    a.text(1.0, 1.3, "$y = 1/x$", color=fs.GREEN, fontsize=10.5, ha="left", va="bottom", bbox=BOX, zorder=6)
    a.text(0.12, 4.25, "$y$", ha="left", va="top", style="italic", fontsize=11)
    a.text(4.35, 0.15, "$x$", ha="right", va="bottom", style="italic", fontsize=11)
    a.text(-0.15, 3.3, "$x = 0$", ha="right", va="center", fontsize=9, color=fs.GRAY)
    a.text(-4.3, 0.15, "$y = 0$", ha="left", va="bottom", fontsize=9, color=fs.GRAY)
    # right: y = 2/(x-3) + 1
    setup(b, (-2.4, 8.4), (-6.4, 8.4), [-2, 2, 4, 6, 8], [-6, -4, -2, 2, 4, 6, 8])
    b.axvline(3, color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    b.axhline(1, color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    xs1 = np.linspace(3.18, 8.4, 300)
    xs2 = np.linspace(-2.4, 2.82, 300)
    b.plot(xs1, 2 / (xs1 - 3) + 1, color=fs.GREEN, zorder=3)
    b.plot(xs2, 2 / (xs2 - 3) + 1, color=fs.GREEN, zorder=3)
    b.text(3.15, -5.9, "$x = 3$", ha="left", va="center", fontsize=9, color=fs.GRAY)
    b.text(-2.3, 1.25, "$y = 1$", ha="left", va="bottom", fontsize=9, color=fs.GRAY)
    b.text(4.6, 4.2, "$y = \\dfrac{2}{x - 3} + 1$", color=fs.GREEN, fontsize=10.5, ha="left", va="bottom", bbox=BOX, zorder=6)
    b.text(0.12, 8.3, "$y$", ha="left", va="top", style="italic", fontsize=11)
    b.text(8.35, 0.2, "$x$", ha="right", va="bottom", style="italic", fontsize=11)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.04, wspace=0.08)
    fs.save(fig, FOLDER, f"{SLUG}-reciprocal")


def hole_sketch():
    fig, ax = fs.figure(5.8, 4.2)
    setup(ax, (-7, 9.5), (-9, 11), [-6, -4, -2, 2, 4, 6, 8], [-8, -4, 4, 8])
    f = lambda x: 2 * (x - 2) / (x - 3)
    ax.axvline(3, color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    ax.axhline(2, color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    left = np.linspace(-7, 2.8, 400)
    right = np.linspace(3.12, 9.5, 400)
    ax.plot(left, f(left), color=fs.GREEN, zorder=3)
    ax.plot(right, f(right), color=fs.GREEN, zorder=3)
    hole(ax, -2, f(-2))
    ax.plot([2, 0], [0, f(0)], "o", color=fs.DARK, zorder=5, ms=5)
    ax.annotate("hole at $(-2, \\frac{8}{5})$", xy=(-2, f(-2)), xytext=(-6.6, -3.8), fontsize=9.5, color=fs.GREEN, ha="left", va="center", arrowprops=dict(arrowstyle="-", color=fs.GREEN, lw=1.0), zorder=6)
    ax.text(3.2, -8.6, "$x = 3$", ha="left", va="center", fontsize=9.5, color=fs.GRAY)
    ax.text(-6.9, 2.3, "$y = 2$", ha="left", va="bottom", fontsize=9.5, color=fs.GRAY)
    ax.text(2.1, -0.5, "$2$", ha="left", va="top", fontsize=9, alpha=0)
    ax.text(0.25, f(0) + 0.4, "$(0, \\frac{4}{3})$", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(6.0, 4.9, "$f(x) = \\dfrac{2x^2 - 8}{x^2 - x - 6}$", fontsize=10.5, color=fs.GREEN, ha="left", va="bottom", bbox=BOX, zorder=6)
    ax.text(0.2, 10.8, "$y$", ha="left", va="top", style="italic", fontsize=12)
    ax.text(9.4, 0.3, "$x$", ha="right", va="bottom", style="italic", fontsize=12)
    fs.save(fig, FOLDER, f"{SLUG}-hole-sketch")


def slant_sketch():
    fig, ax = fs.figure(5.8, 4.2)
    setup(ax, (-5, 9), (-9, 9), [-4, -2, 2, 4, 6, 8], [-8, -4, 4, 8])
    f = lambda x: (x**2 - 3 * x - 4) / (x - 2)
    ax.axvline(2, color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    xs = np.linspace(-5, 9, 200)
    ax.plot(xs, xs - 1, color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    left = np.linspace(-5, 1.6, 400)
    right = np.linspace(2.4, 9, 400)
    ax.plot(left, f(left), color=fs.GREEN, zorder=3)
    ax.plot(right, f(right), color=fs.GREEN, zorder=3)
    ax.plot([-1, 4, 0], [0, 0, 2], "o", color=fs.DARK, zorder=5, ms=5)
    ax.text(2.15, -8.6, "$x = 2$", ha="left", va="center", fontsize=9.5, color=fs.GRAY)
    ax.text(6.9, 4.4, "$y = x - 1$", ha="left", va="top", fontsize=9.5, color=fs.GRAY, rotation=0)
    ax.text(0.25, 2.3, "$(0, 2)$", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(-4.8, -5.3, "$f(x) = \\dfrac{x^2 - 3x - 4}{x - 2}$", fontsize=10.5, color=fs.GREEN, ha="left", va="top", bbox=BOX, zorder=6)
    ax.text(0.2, 8.8, "$y$", ha="left", va="top", style="italic", fontsize=12)
    ax.text(8.9, 0.3, "$x$", ha="right", va="bottom", style="italic", fontsize=12)
    fs.save(fig, FOLDER, f"{SLUG}-slant-sketch")


def average_cost():
    fig, ax = fs.figure(5.8, 3.8)
    setup(ax, (-300, 5300), (-6, 72), [1000, 2000, 3000, 4000, 5000], [12, 20, 40, 60])
    qs = np.linspace(72, 5300, 500)
    ax.axhline(12, color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    ax.plot(qs, 5000 / qs + 12, color=fs.GREEN, zorder=3)
    pts = [(100, 62), (500, 22), (1000, 17)]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], "o", color=fs.DARK, zorder=5, ms=5)
    ax.text(130, 63, "$(100, 62)$", ha="left", va="center", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(560, 26, "$(500, 22)$", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(1060, 20, "$(1000, 17)$", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(1500, 10.0, "marginal cost, $y = 12$", ha="left", va="top", fontsize=9.5, color=fs.GRAY)
    ax.text(2300, 40, "$\\overline{C}(q) = \\dfrac{5000}{q} + 12$", fontsize=11, color=fs.GREEN, ha="left", va="bottom", bbox=BOX, zorder=6)
    ax.text(5250, 1.5, "$q$ (units)", ha="right", va="bottom", style="italic", fontsize=11)
    ax.text(350, 71, "dollars per unit", ha="left", va="top", fontsize=9.5)
    fs.save(fig, FOLDER, f"{SLUG}-average-cost")


if __name__ == "__main__":
    reciprocal()
    hole_sketch()
    slant_sketch()
    average_cost()
