"""Figures for docs/03-high-school/01-algebra-foundations/04-absolute-value-equations-and-inequalities.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/absolute-value-equations-and-inequalities.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np  # noqa: E402

import algebra_numberline as nl  # noqa: E402

fs = nl.fs
plt = fs.plt

FOLDER = "03-high-school"
SLUG = "absolute-value-equations-and-inequalities"
M = nl.MINUS
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def distance():
    """|x - 3| = 2, < 2 and > 2: points, the middle and the outside."""
    lo, hi = -0.6, 6.6
    gap = 1.55
    rows = [
        (r"$|x - 3| = 2$", r"$x = 1$ or $x = 5$"),
        (r"$|x - 3| < 2$", r"$(1,\ 5)$"),
        (r"$|x - 3| > 2$", r"$(-\infty,\ 1) \cup (5,\ \infty)$"),
    ]
    fig, ax = nl.canvas(7.2, 3.9, (-5.2, 11.6), (-(len(rows) - 1) * gap - 0.7, 1.0))
    for i, (left, right) in enumerate(rows):
        y = -i * gap
        nl.axis_line(ax, y, lo, hi, range(0, 7), size=8, label_gap=0.14)
        ax.text(-5.0, y + 0.1, left, ha="left", va="center", fontsize=11)
        ax.text(7.2, y + 0.1, right, ha="left", va="center", fontsize=11, color=fs.GREEN, fontweight="bold")
    # Row 1: two points, each at distance 2 from the centre 3.
    y = 0
    nl.dot(ax, 1, y, True)
    nl.dot(ax, 5, y, True)
    nl.dot(ax, 3, y, True, colour=fs.DARK, size=5)
    for a, b in [(1, 3), (3, 5)]:
        ax.annotate(
            "",
            xy=(a, y + 0.55),
            xytext=(b, y + 0.55),
            arrowprops=dict(arrowstyle="<->", color=fs.DARK, lw=1.0, shrinkA=0, shrinkB=0),
        )
        ax.text((a + b) / 2, y + 0.65, "2", ha="center", va="bottom", fontsize=10)
    ax.text(3, y - 0.55, "", fontsize=9)
    # Row 2: the middle.
    nl.segment(ax, -gap, 1, 5, False, False)
    # Row 3: the outside.
    nl.ray(ax, -2 * gap, 1, -1, False, hi, lo)
    nl.ray(ax, -2 * gap, 5, +1, False, hi, lo)
    fs.save(fig, FOLDER, f"{SLUG}-distance")


def tolerance():
    """A shaft machined to 25 +/- 0.05 mm: the accepted interval and four measured parts."""
    lo, hi = 24.895, 25.105
    fig, ax = nl.canvas(7.2, 3.1, (24.80, 25.215), (-2.45, 1.05))
    y = 0
    ticks = [24.90, 24.95, 25.00, 25.05, 25.10]
    nl.axis_line(ax, y, lo, hi, ticks, decimals=2, size=9, tick_h=0.07, label_gap=0.14)
    nl.segment(ax, y, 24.95, 25.05, True, True)
    for a, b in [(24.95, 25.00), (25.00, 25.05)]:
        ax.annotate(
            "",
            xy=(a, y + 0.5),
            xytext=(b, y + 0.5),
            arrowprops=dict(arrowstyle="<->", color=fs.DARK, lw=1.0, shrinkA=0, shrinkB=0),
        )
        ax.text((a + b) / 2, y + 0.58, "0.05", ha="center", va="bottom", fontsize=9)
    ax.text(25.1065, y + 0.1, "mm", ha="left", va="center", fontsize=9)
    ax.text(24.803, y + 0.1, "accepted", ha="left", va="center", fontsize=11, color=fs.GREEN)
    # Four measured parts, each at its length on a second line.
    y2 = -1.45
    nl.axis_line(ax, y2, lo, hi, ticks, decimals=2, size=9, tick_h=0.07, label_gap=0.14, show_labels=False)
    for v, ok, below in [(24.94, False, False), (25.02, True, False), (25.05, True, True), (25.07, False, False)]:
        colour = fs.GREEN if ok else fs.RED
        nl.dot(ax, v, y2, ok, colour=colour, size=8)
        if below:
            ax.text(v, y2 - 0.3, f"{v:.2f}", ha="center", va="top", fontsize=9, color=colour)
        else:
            ax.text(v, y2 + 0.3, f"{v:.2f}", ha="center", va="bottom", fontsize=9, color=colour)
    ax.text(24.803, y2 + 0.1, "measured", ha="left", va="center", fontsize=11, color=fs.DARK)
    for v in ticks:
        nl.guide(ax, v, y2 + 0.07, y2 - 0.07, colour=fs.DARK)
    fs.save(fig, FOLDER, f"{SLUG}-tolerance")


def axes_zero(ax, xmin, xmax, ymin, ymax):
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks(range(int(np.ceil(xmin)) + 1, int(xmax)))
    ax.set_yticks(range(int(np.ceil(ymin)) + 1, int(ymax)))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    for t in range(int(np.ceil(xmin)) + 1, int(xmax)):
        if t != 0:
            ax.text(t, -0.45, f"{t}".replace("-", M), ha="center", va="top", fontsize=8.5, zorder=4, bbox=BOX)
    for t in range(int(np.ceil(ymin)) + 1, int(ymax)):
        if t != 0 and t % 2 == 0:
            ax.text(-0.15, t, f"{t}".replace("-", M), ha="right", va="center", fontsize=8.5, zorder=4, bbox=BOX)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def cases_graph():
    """y = |2x - 3| against y = 7, y = 0 and y = -2: two solutions, one and none."""
    fig, ax = fs.figure(6.2, 4.2)
    axes_zero(ax, -4.5, 7.8, -3.4, 10.4)
    x = np.linspace(-3.3, 6.3, 400)
    ax.plot(x, np.abs(2 * x - 3), color=fs.DARK, lw=2.2, zorder=3)
    ax.text(5.9, 8.9, r"$y = |2x - 3|$", ha="right", va="center", fontsize=11, color=fs.DARK, bbox=BOX)
    for c, colour, label in [(7, fs.GREEN, "c = 7"), (0, fs.ORANGE, "c = 0"), (-2, fs.RED, f"c = {M}2")]:
        ax.plot([-4.2, 7.0], [c, c], color=colour, lw=1.6, ls=(0, (5, 3)), zorder=2)
        ax.text(7.1, c + (0.55 if c == 0 else 0), label, ha="left", va="center", fontsize=10.5, color=colour, bbox=BOX, zorder=7)
    for px, py, colour in [(-2, 7, fs.GREEN), (5, 7, fs.GREEN), (1.5, 0, fs.ORANGE)]:
        ax.plot([px], [py], "o", ms=7, mfc=colour, mec="white", mew=1.2, zorder=6)
    ax.text(-2.4, 6.5, f"x = {M}2", ha="right", va="top", fontsize=10, color=fs.GREEN, bbox=BOX)
    ax.text(5.4, 6.5, "x = 5", ha="left", va="top", fontsize=10, color=fs.GREEN, bbox=BOX)
    ax.text(1.5, 0.75, "x = 1.5", ha="center", va="bottom", fontsize=10, color=fs.ORANGE, bbox=BOX)
    ax.text(-4.3, -1.0, "no solution", ha="left", va="top", fontsize=10, color=fs.RED)
    fs.save(fig, FOLDER, f"{SLUG}-cases-graph")


def extraneous():
    """|x - 3| = 2x: one real solution, x = 1; the candidate x = -3 fails."""
    fig, ax = fs.figure(6.0, 4.0)
    axes_zero(ax, -4.6, 6.8, -8.4, 8.4)
    x = np.linspace(-4.2, 6.4, 400)
    ax.plot(x, np.abs(x - 3), color=fs.BLUE, lw=2.2, zorder=3)
    ax.plot(x, 2 * x, color=fs.ORANGE, lw=2.2, zorder=3)
    ax.text(6.7, 5.2, r"$y = |x - 3|$", ha="right", va="bottom", fontsize=11, color=fs.BLUE, bbox=BOX)
    ax.text(3.6, 8.0, r"$y = 2x$", ha="left", va="top", fontsize=11, color=fs.ORANGE, bbox=BOX)
    ax.plot([1], [2], "o", ms=8, mfc=fs.GREEN, mec="white", mew=1.2, zorder=6)
    ax.text(1.35, 3.0, "x = 1", ha="left", va="bottom", fontsize=10.5, color=fs.GREEN, bbox=BOX)
    # The failed candidate: the two graphs are 12 apart at x = -3.
    ax.plot([-3, -3], [-6, 6], color=fs.RED, lw=1.4, ls=(0, (3, 3)), zorder=2)
    ax.plot([-3], [6], "o", ms=7, mfc=fs.BLUE, mec="white", mew=1.2, zorder=6)
    ax.plot([-3], [-6], "o", ms=7, mfc=fs.ORANGE, mec="white", mew=1.2, zorder=6)
    ax.text(-2.7, 6.9, f"({M}3, 6)", ha="left", va="center", fontsize=10, color=fs.BLUE, bbox=BOX)
    ax.text(-2.7, -6.9, f"({M}3, {M}6)", ha="left", va="center", fontsize=10, color=fs.ORANGE, bbox=BOX)
    ax.text(-3.2, 0.9, "not equal", ha="right", va="bottom", fontsize=10, color=fs.RED, bbox=BOX)
    fs.save(fig, FOLDER, f"{SLUG}-extraneous")


if __name__ == "__main__":
    distance()
    tolerance()
    cases_graph()
    extraneous()
