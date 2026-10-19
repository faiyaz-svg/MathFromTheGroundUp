"""Figures for docs/03-high-school/02-linear-functions-and-systems/02-systems-of-linear-equations.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/systems-of-linear-equations.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "systems-of-linear-equations"
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


def elimination():
    """Four lines through (5, -1): the two equations, and the two lines elimination produces."""
    fig, ax = fs.figure(5.6, 4.4)
    plane(ax, -2, 8, -5, 4)
    xs = [-2.5, 8.5]
    ax.plot(xs, [(7 - 2 * x) / 3 for x in xs], color=fs.GREEN, zorder=3)
    ax.plot(xs, [(x - 9) / 4 for x in xs], color=fs.BLUE, zorder=3)
    ax.plot([5, 5], [-5.4, 4.6], color=fs.ORANGE, ls=(0, (5, 3)), zorder=3)
    ax.plot(xs, [-1, -1], color=fs.RED, ls=(0, (5, 3)), zorder=3)
    ax.plot(5, -1, "o", color=fs.DARK, zorder=5)
    ax.text(5.25, -1.3, "(5, " + M + "1)", ha="left", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.text(1.2, 3.3, "2x + 3y = 7", ha="left", va="bottom", fontsize=10, color=fs.GREEN,
            style="italic", bbox=BOX, zorder=6)
    ax.text(0.7, -3.2, "x " + M + " 4y = 9", ha="left", va="top", fontsize=10, color=fs.BLUE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(5.15, 3.9, "x = 5", ha="left", va="top", fontsize=10, color=fs.ORANGE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(-2.3, -1.3, "y = " + M + "1", ha="left", va="top", fontsize=10, color=fs.RED,
            style="italic", bbox=BOX, zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-elimination")


def supply_demand():
    """Demand and supply lines, with price on the vertical axis, before and after a demand shift."""
    fig, ax = fs.figure(5.4, 4.0)
    ax.set_xlim(0, 180)
    ax.set_ylim(0, 18)
    ax.set_xticks(range(0, 181, 30))
    ax.set_yticks(range(0, 19, 3))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.plot([0, 150], [15, 0], color=fs.BLUE, zorder=3)
    ax.plot([0, 180], [18, 0], color=fs.BLUE, ls=(0, (5, 3)), zorder=3)
    ax.plot([30, 180], [0, 7.5], color=fs.GREEN, zorder=3)
    ax.plot([110, 130], [4, 5], "o", color=fs.DARK, zorder=5)
    ax.text(108, 3.6, "(110, 4)", ha="right", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.annotate("(130, 5)", xy=(130, 5), xytext=(140, 9.0), ha="left", va="center", fontsize=10,
                arrowprops=dict(arrowstyle="-", color=fs.GRAY, lw=0.8), zorder=6)
    ax.text(2, 14.6, "demand", ha="left", va="top", fontsize=10, color=fs.BLUE, style="italic",
            bbox=BOX, zorder=6)
    ax.text(28, 16.6, "demand after the shift", ha="left", va="bottom", fontsize=10, color=fs.BLUE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(160, 5.4, "supply", ha="left", va="top", fontsize=10, color=fs.GREEN, style="italic",
            bbox=BOX, zorder=6)
    ax.set_xlabel("quantity, Q (dozens per week)")
    ax.set_ylabel("price, P (dollars per dozen)")
    fs.save(fig, FOLDER, f"{SLUG}-supply-demand")


if __name__ == "__main__":
    elimination()
    supply_demand()
