"""Figures for docs/03-high-school/02-linear-functions-and-systems/01-forms-of-linear-equations.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/forms-of-linear-equations.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from matplotlib.patches import Polygon  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "forms-of-linear-equations"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def plane(ax, xmin, xmax, ymin, ymax, every=1, size=9):
    """Axes through the origin with arrows, a light grid and equal units."""
    ax.set_xlim(xmin - 0.5, xmax + 0.6)
    ax.set_ylim(ymin - 0.5, ymax + 0.6)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks(range(xmin, xmax + 1))
    ax.set_yticks(range(ymin, ymax + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for t in range(xmin, xmax + 1):
        if t != 0 and t % every == 0:
            ax.text(t, -0.18, num(t), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
    for t in range(ymin, ymax + 1):
        if t != 0 and t % every == 0:
            ax.text(-0.18, t, num(t), ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)
    ax.text(xmax + 0.6, 0.3, "x", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.3, ymax + 0.6, "y", ha="left", va="top", style="italic", fontsize=12)


def one_line():
    """The line 2x + 3y = 12 with its intercepts and a slope triangle."""
    fig, ax = fs.figure(5.4, 4.2)
    plane(ax, -2, 8, -2, 6, every=2)
    xs = [-2.5, 8]
    ax.plot(xs, [(12 - 2 * x) / 3 for x in xs], color=fs.GREEN, zorder=3)
    # slope triangle from (0, 4) to (3, 2)
    ax.plot([0, 3, 3], [4, 4, 2], color=fs.GRAY, lw=1.4, ls=(0, (4, 3)), zorder=3)
    ax.text(1.5, 4.18, "run 3", ha="center", va="bottom", fontsize=10, color=fs.DARK)
    ax.text(3.2, 3.0, "rise " + M + "2", ha="left", va="center", fontsize=10, color=fs.DARK)
    for px, py in [(0, 4), (6, 0), (3, 2)]:
        ax.plot(px, py, "o", color=fs.DARK, zorder=5)
    ax.text(-0.3, 4.1, "y-intercept (0, 4)", ha="right", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(6.0, 0.35, "x-intercept (6, 0)", ha="center", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(3.35, 1.55, "(3, 2)", ha="left", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.text(6.4, 3.0, "2x + 3y = 12", ha="left", va="center", fontsize=11, color=fs.GREEN,
            style="italic", bbox=BOX, zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-one-line")


def perpendicular():
    """A quarter turn about O sends the line y = (2/3)x to the line y = -(3/2)x."""
    fig, ax = fs.figure(5.2, 4.4)
    plane(ax, -4, 5, -3, 5)
    # original triangle O, (3, 0), P and its quarter-turn image O, (0, 3), P'
    ax.add_patch(Polygon([(0, 0), (3, 0), (3, 2)], closed=True, facecolor=fs.GREEN, alpha=0.14,
                         edgecolor=fs.GREEN, lw=1.2, zorder=2))
    ax.add_patch(Polygon([(0, 0), (0, 3), (-2, 3)], closed=True, facecolor=fs.BLUE, alpha=0.14,
                         edgecolor=fs.BLUE, lw=1.2, zorder=2))
    ax.plot([-3.2, 4.8], [-3.2 * 2 / 3, 4.8 * 2 / 3], color=fs.GREEN, zorder=3)
    ax.plot([-2.6, 2.2], [-2.6 * -1.5, 2.2 * -1.5], color=fs.BLUE, zorder=3)
    ax.plot([3, -2], [2, 3], "o", color=fs.DARK, zorder=5)
    ax.plot(0, 0, "o", color=fs.DARK, zorder=5, ms=4)
    ax.text(3.2, 2.2, "P (3, 2)", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(-2.2, 3.2, "P′ (" + M + "2, 3)", ha="right", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(4.8, 3.55, "slope 2/3", ha="right", va="bottom", fontsize=10, color=fs.GREEN,
            style="italic", bbox=BOX, zorder=6)
    ax.text(-2.5, 4.35, "slope " + M + "3/2", ha="right", va="bottom", fontsize=10, color=fs.BLUE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(1.5, -0.1, "3", ha="center", va="top", fontsize=9, color=fs.GREEN, zorder=6)
    ax.text(3.15, 1.0, "2", ha="left", va="center", fontsize=9, color=fs.GREEN, zorder=6)
    ax.text(-0.15, 1.5, "3", ha="right", va="center", fontsize=9, color=fs.BLUE, zorder=6)
    ax.text(-1.0, 3.15, "2", ha="center", va="bottom", fontsize=9, color=fs.BLUE, zorder=6)
    # right-angle mark at O between the two lines
    s = 0.35
    d1 = (3 / 13 ** 0.5, 2 / 13 ** 0.5)
    d2 = (-2 / 13 ** 0.5, 3 / 13 ** 0.5)
    pts = [(s * d1[0], s * d1[1]), (s * (d1[0] + d2[0]), s * (d1[1] + d2[1])), (s * d2[0], s * d2[1])]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=fs.DARK, lw=1.0, zorder=4)
    fs.save(fig, FOLDER, f"{SLUG}-perpendicular")


def depreciation():
    """A laptop worth 1200 dollars loses 240 dollars a year."""
    fig, ax = fs.figure(5.2, 3.8)
    ax.set_xlim(0, 6.5)
    ax.set_ylim(0, 1400)
    ax.set_xticks(range(0, 7))
    ax.set_yticks(range(0, 1401, 200))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.plot([0, 5], [1200, 0], color=fs.GREEN, zorder=3, clip_on=False)
    for px, py in [(0, 1200), (5, 0), (3.5, 360)]:
        ax.plot(px, py, "o", color=fs.DARK, zorder=5, clip_on=False)
    ax.text(0.2, 1210, "bought at \\$1,200", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(5.15, 60, "worth \\$0\nat t = 5", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(3.65, 420, "(3.5, 360)", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(0.3, 520, "V = 1200 " + M + " 240t", ha="left", va="center", fontsize=11, color=fs.GREEN,
            style="italic", bbox=BOX, zorder=6)
    ax.set_xlabel("years since purchase, t")
    ax.set_ylabel("value in dollars, V")
    fs.save(fig, FOLDER, f"{SLUG}-depreciation")


def parallel_perpendicular():
    """Through (-1, 4): the line parallel to 3x - 2y = 5 and the one perpendicular to it."""
    fig, ax = fs.figure(5.2, 5.0)
    plane(ax, -6, 7, -4, 8, every=2)
    xs = [-6.5, 6.5]
    ax.plot(xs, [(3 * x - 5) / 2 for x in xs], color=fs.BLUE, zorder=3)
    ax.plot(xs, [(3 * x + 11) / 2 for x in xs], color=fs.GREEN, zorder=3)
    ax.plot(xs, [(10 - 2 * x) / 3 for x in xs], color=fs.ORANGE, zorder=3)
    ax.plot(-1, 4, "o", color=fs.DARK, zorder=5)
    ax.text(-1.7, 3.5, "(" + M + "1, 4)", ha="right", va="center", fontsize=10, bbox=BOX, zorder=6)
    ax.text(6.4, 5.9, "3x " + M + " 2y = 5", ha="right", va="top", fontsize=10, color=fs.BLUE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(0.6, 7.5, "3x " + M + " 2y = " + M + "11", ha="left", va="center", fontsize=10, color=fs.GREEN,
            style="italic", bbox=BOX, zorder=6)
    ax.text(5.0, 1.7, "2x + 3y = 10", ha="center", va="bottom", fontsize=10, color=fs.ORANGE,
            style="italic", bbox=BOX, zorder=6)
    # right-angle mark at (-1, 4) between the green and orange lines
    s = 0.55
    n1 = 13 ** 0.5
    d1 = (2 / n1, 3 / n1)
    d2 = (3 / n1, -2 / n1)
    pts = [(-1 + s * d1[0], 4 + s * d1[1]), (-1 + s * (d1[0] + d2[0]), 4 + s * (d1[1] + d2[1])),
           (-1 + s * d2[0], 4 + s * d2[1])]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=fs.DARK, lw=1.0, zorder=4)
    fs.save(fig, FOLDER, f"{SLUG}-parallel-perpendicular")


if __name__ == "__main__":
    one_line()
    perpendicular()
    depreciation()
    parallel_perpendicular()
