"""Figures for docs/03-high-school/04-radicals-and-polynomials/05-polynomial-functions-and-graphs.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/polynomial-functions-and-graphs.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "polynomial-functions-and-graphs"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def axes_through_origin(ax, xlim, ylim, xticks, yticks, size=9):
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
    box = dict(facecolor="white", edgecolor="none", pad=0.15)
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


def box_volume():
    fig, ax = fs.figure(5.8, 3.8)
    axes_through_origin(ax, (-1, 16.5), (-500, 1400), [5, 10, 15], [-400, 400, 800, 1200], size=9)
    xs = np.linspace(-0.6, 16, 400)
    v = 4 * xs**3 - 100 * xs**2 + 600 * xs
    ax.axvspan(0, 10, color=fs.GREEN, alpha=0.10, lw=0, zorder=1)
    ax.plot(xs, v, color=fs.GREEN, zorder=3)
    ax.plot([0, 10, 15], [0, 0, 0], "o", color=fs.DARK, zorder=5, ms=5)
    ax.plot(3.92, 1056.3, "o", color=fs.RED, zorder=5, ms=5)
    ax.text(4.6, 1180, "largest volume, about 1056 cm$^3$\nat $x \\approx 3.9$ cm", ha="left", va="bottom", fontsize=9.5, color=fs.RED, bbox=BOX, zorder=6)
    ax.text(5, -420, "box exists for $0 < x < 10$", ha="center", va="center", fontsize=9.5, color=fs.GREEN)
    ax.text(16.3, 70, "$x$", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.5, 1380, "$V$", ha="left", va="top", style="italic", fontsize=12)
    ax.text(15.3, 120, "15", ha="left", va="bottom", fontsize=9, alpha=0)
    fs.save(fig, FOLDER, f"{SLUG}-box-volume")


def end_behaviour():
    fig, axes = plt.subplots(1, 4, figsize=(8.4, 2.6))
    xs = np.linspace(-2.6, 2.6, 300)
    cases = [
        (0.25 * xs**4 - xs**2, "even degree,\nleading coefficient $> 0$:\nup on both ends"),
        (-(0.25 * xs**4 - xs**2), "even degree,\nleading coefficient $< 0$:\ndown on both ends"),
        (0.35 * xs**3 - 1.2 * xs, "odd degree,\nleading coefficient $> 0$:\ndown left, up right"),
        (-(0.35 * xs**3 - 1.2 * xs), "odd degree,\nleading coefficient $< 0$:\nup left, down right"),
    ]
    for ax, (ys, text) in zip(axes, cases):
        ax.set_xlim(-2.8, 2.8)
        ax.set_ylim(-5, 5)
        ax.axis("off")
        ax.plot([-2.8, 2.8], [0, 0], color=fs.DARK, lw=1.0)
        ax.plot([0, 0], [-4.6, 4.6], color=fs.DARK, lw=1.0)
        ax.plot(xs, ys, color=fs.GREEN, zorder=3)
        ax.text(0, -5.4, text, ha="center", va="top", fontsize=8.5)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.30, wspace=0.08)
    fs.save(fig, FOLDER, f"{SLUG}-end-behaviour")


def multiplicity():
    fig, axes = plt.subplots(1, 3, figsize=(7.8, 3.0))
    xs = np.linspace(-0.4, 2.4, 300)
    cases = [
        (xs - 1, "multiplicity 1\ncrosses, straight through", "$y = (x - 1)$"),
        ((xs - 1) ** 2, "multiplicity 2\ntouches and turns back", "$y = (x - 1)^2$"),
        ((xs - 1) ** 3, "multiplicity 3\ncrosses, flattening", "$y = (x - 1)^3$"),
    ]
    for ax, (ys, text, label) in zip(axes, cases):
        ax.set_xlim(-0.6, 2.6)
        ax.set_ylim(-1.8, 1.8)
        ax.axis("off")
        ax.plot([-0.6, 2.6], [0, 0], color=fs.DARK, lw=1.0)
        ax.plot(xs, ys, color=fs.BLUE, zorder=3)
        ax.plot(1, 0, "o", color=fs.DARK, zorder=5, ms=5)
        ax.text(1, -0.28, "1", ha="center", va="top", fontsize=9)
        ax.text(1, -1.95, label + "\n" + text, ha="center", va="top", fontsize=9)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.32, wspace=0.05)
    fs.save(fig, FOLDER, f"{SLUG}-multiplicity")


def sketch():
    fig, ax = fs.figure(5.8, 4.0)
    axes_through_origin(ax, (-3.2, 4.2), (-20, 26), [-3, -2, -1, 1, 2, 3, 4], [-10, 10, 20], size=9)
    xs = np.linspace(-3, 3.9, 400)
    ys = (xs + 2) * (xs - 1) ** 2 * (xs - 3)
    ax.plot(xs, ys, color=fs.GREEN, zorder=3)
    ax.plot([-2, 1, 3], [0, 0, 0], "o", color=fs.DARK, zorder=5, ms=5)
    ax.plot(0, -6, "o", color=fs.RED, zorder=5, ms=5)
    ax.text(0.15, -6.8, "$(0, -6)$", ha="left", va="top", fontsize=9.5, color=fs.RED, bbox=BOX, zorder=6)
    ax.text(-1.9, 2.6, "$-2$: crosses", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(1.0, 2.2, "$1$: touches", ha="center", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(2.9, 2.2, "$3$: crosses", ha="right", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(3.95, -19.4, "$x$", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.2, 25.5, "$y$", ha="left", va="top", style="italic", fontsize=12)
    fs.save(fig, FOLDER, f"{SLUG}-sketch")


def fitting():
    fig, ax = fs.figure(5.6, 3.8)
    xs = [0, 1, 2, 3, 4, 5]
    ys = [1.0, 2.2, 2.9, 4.4, 4.7, 6.1]
    line = np.polyfit(xs, ys, 1)
    quint = np.polyfit(xs, ys, 5)
    t = np.linspace(-0.2, 5.8, 400)
    ax.set_xlim(-0.3, 5.9)
    ax.set_ylim(-3, 12)
    ax.set_xticks(range(0, 6))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.plot(t, np.polyval(line, t), color=fs.BLUE, zorder=3)
    ax.plot(t, np.polyval(quint, t), color=fs.RED, zorder=3)
    ax.plot(xs, ys, "o", color=fs.DARK, zorder=5)
    ax.text(0.0, 8.8, "degree 5 through all six points", ha="left", va="center", fontsize=10, color=fs.RED, bbox=BOX, zorder=6)
    ax.text(2.2, 0.0, "degree 1: a line near the points", ha="left", va="center", fontsize=10, color=fs.BLUE, bbox=BOX, zorder=6)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    fs.save(fig, FOLDER, f"{SLUG}-fitting")


if __name__ == "__main__":
    box_volume()
    end_behaviour()
    multiplicity()
    sketch()
    fitting()
