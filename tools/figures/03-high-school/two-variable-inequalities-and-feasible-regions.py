"""Figures for docs/03-high-school/02-linear-functions-and-systems/03-two-variable-inequalities-and-feasible-regions.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/two-variable-inequalities-and-feasible-regions.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "two-variable-inequalities-and-feasible-regions"
M = "\u2212"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)
SHADE = dict(facecolor=fs.GREEN, alpha=0.16, edgecolor="none", zorder=1)


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


def real_axes(ax, xmax, ymax, xstep, ystep, xlabel, ylabel):
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, ymax)
    ax.set_xticks(range(0, xmax + 1, xstep))
    ax.set_yticks(range(0, ymax + 1, ystep))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)


def half_planes():
    """3x - 2y > 6 (dashed) and 2x + 3y <= 12 (solid), each with its test point."""
    fig, axes = plt.subplots(1, 2, figsize=(7.8, 3.9))
    lo, hi = -3.5, 7.5
    # (a) 3x - 2y > 6: below the line y = 1.5x - 3
    ax = axes[0]
    plane(ax, -3, 7, -5, 6, every=2, size=8)
    xs = [lo, hi]
    ys = [1.5 * x - 3 for x in xs]
    fine = [lo + i * (hi - lo) / 200 for i in range(201)]
    ax.fill_between(fine, -6, [1.5 * x - 3 for x in fine], **SHADE)
    ax.plot(xs, ys, color=fs.GREEN, ls=(0, (5, 3)), zorder=3)
    ax.plot(0, 0, "o", mfc="white", mec=fs.DARK, zorder=5)
    ax.text(-0.35, 0.5, "(0, 0): 0 > 6 false", ha="right", va="bottom", fontsize=8.5, bbox=BOX, zorder=6)
    ax.plot(4, 0, "o", color=fs.DARK, zorder=5, ms=4)
    ax.text(7.4, 1.0, "(4, 0): 12 > 6 true", ha="right", va="bottom", fontsize=8.5, bbox=BOX, zorder=6)
    ax.text(0.5, -0.03, "3x " + M + " 2y > 6, dashed", transform=ax.transAxes, ha="center", va="top",
            fontsize=10)
    # (b) 2x + 3y <= 12: below the line y = (12 - 2x)/3
    ax = axes[1]
    plane(ax, -3, 7, -5, 6, every=2, size=8)
    ys = [(12 - 2 * x) / 3 for x in xs]
    ax.fill_between(fine, -6, [(12 - 2 * x) / 3 for x in fine], **SHADE)
    ax.plot(xs, ys, color=fs.GREEN, zorder=3)
    ax.plot(0, 0, "o", color=fs.DARK, zorder=5, ms=4)
    ax.text(0.3, -0.25, "(0, 0): 0 \u2264 12 true", ha="left", va="top", fontsize=8.5, bbox=BOX, zorder=6)
    ax.text(0.5, -0.03, "2x + 3y \u2264 12, solid", transform=ax.transAxes, ha="center", va="top",
            fontsize=10)
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-half-planes")


def corners():
    """x >= 0, y >= 0, x + y <= 6, x + 3y <= 12 with its four corners."""
    fig, ax = fs.figure(5.4, 4.2)
    plane(ax, -1, 8, -1, 6)
    pts = [(0, 0), (6, 0), (3, 3), (0, 4)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=fs.GREEN, alpha=0.16, edgecolor="none", zorder=1))
    xs = [-0.8, 8.2]
    ax.plot(xs, [6 - x for x in xs], color=fs.BLUE, zorder=3)
    ax.plot(xs, [(12 - x) / 3 for x in xs], color=fs.ORANGE, zorder=3)
    for px, py in pts:
        ax.plot(px, py, "o", color=fs.DARK, zorder=5)
    ax.text(0.2, -0.25, "(0, 0)", ha="left", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.text(6.15, 0.25, "(6, 0)", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(3.15, 3.2, "(3, 3)", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(0.25, 4.25, "(0, 4)", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(1.0, 5.6, "x + y = 6", ha="left", va="bottom", fontsize=10, color=fs.BLUE, style="italic",
            bbox=BOX, zorder=6)
    ax.text(5.2, 2.35, "x + 3y = 12", ha="left", va="bottom", fontsize=10, color=fs.ORANGE, style="italic",
            bbox=BOX, zorder=6)
    ax.text(1.2, 1.3, "feasible\nregion", ha="center", va="center", fontsize=10, color=fs.GREEN)
    fs.save(fig, FOLDER, f"{SLUG}-corners")


BAKERY = [(0, 0), (30, 0), (20, 20), (10, 30), (0, 30)]


def bakery_axes(ax):
    real_axes(ax, 45, 45, 5, 5, "trays of muffins per week, x", "trays of scones per week, y")
    ax.add_patch(Polygon(BAKERY, closed=True, facecolor=fs.GREEN, alpha=0.16, edgecolor="none", zorder=1))


def bakery():
    """The bakery feasible region with its five corners."""
    fig, ax = fs.figure(5.6, 4.6)
    bakery_axes(ax)
    ax.plot([0, 40], [40, 0], color=fs.BLUE, zorder=3)
    ax.plot([0, 30], [60, 0], color=fs.ORANGE, zorder=3)
    ax.plot([0, 45], [30, 30], color=fs.RED, zorder=3)
    for px, py in BAKERY:
        ax.plot(px, py, "o", color=fs.DARK, zorder=5, clip_on=False)
    ax.text(0.8, 0.8, "(0, 0)", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(30.8, 1.0, "(30, 0)", ha="left", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(21.0, 17.8, "(20, 20)", ha="left", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.text(10.3, 26.2, "(10, 30)", ha="left", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.text(0.8, 27.0, "(0, 30)", ha="left", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.text(36.0, 14.0, "labour\nx + y = 40", ha="left", va="center", fontsize=10, color=fs.BLUE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(14.5, 36.0, "oven\n2x + y = 60", ha="left", va="center", fontsize=10, color=fs.ORANGE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(44.5, 31.0, "scone demand y = 30", ha="right", va="bottom", fontsize=10, color=fs.RED,
            style="italic", bbox=BOX, zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-bakery")


def level_lines():
    """Lines of equal profit P = 30x + 20y slide across the region and last touch the corner (20, 20)."""
    fig, ax = fs.figure(5.6, 4.6)
    bakery_axes(ax)
    levels = [(600, fs.GRAY), (1000, fs.GREEN), (1200, fs.RED)]
    for p, colour in levels:
        xs = [0, p / 30]
        ys = [p / 20, 0]
        ax.plot(xs, ys, color=colour, ls=(0, (5, 3)), lw=1.8, zorder=3)
    ax.plot(20, 20, "o", color=fs.DARK, zorder=5)
    ax.annotate("best corner (20, 20),\nP = 1000", xy=(20, 20), xytext=(28.5, 23.5), ha="left", va="center",
                fontsize=10, arrowprops=dict(arrowstyle="-", color=fs.GRAY, lw=0.8), zorder=6)
    ax.text(1.0, 30.6, "P = 600", ha="left", va="bottom", fontsize=10, color=fs.GRAY, bbox=BOX, zorder=6)
    ax.text(3.0, 43.5, "P = 1000", ha="left", va="top", fontsize=10, color=fs.GREEN, bbox=BOX, zorder=6)
    ax.text(30.5, 44.0, "P = 1200\nmisses the region", ha="left", va="top", fontsize=10, color=fs.RED,
            bbox=BOX, zorder=6)
    ax.text(7.0, 14.0, "feasible\nregion", ha="center", va="center", fontsize=10, color=fs.GREEN)
    fs.save(fig, FOLDER, f"{SLUG}-level-lines")


def budget():
    """12x + 4y <= 60: tickets and snacks."""
    fig, ax = fs.figure(5.4, 4.0)
    real_axes(ax, 7, 17, 1, 2, "movie tickets, x", "snacks, y")
    ax.add_patch(Polygon([(0, 0), (5, 0), (0, 15)], closed=True, facecolor=fs.GREEN, alpha=0.16,
                         edgecolor="none", zorder=1))
    ax.plot([0, 5.5], [15, -1.5], color=fs.GREEN, zorder=3, clip_on=True)
    for px, py, colour in [(2, 5, fs.DARK), (3, 6, fs.DARK), (4, 4, fs.RED), (5, 0, fs.DARK), (0, 15, fs.DARK)]:
        ax.plot(px, py, "o", color=colour, zorder=5, clip_on=False)
    ax.text(1.85, 5.4, "(2, 5)\ncosts \\$44", ha="right", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(3.15, 6.2, "(3, 6): costs \\$60,\non the line", ha="left", va="bottom", fontsize=9.5, bbox=BOX,
            zorder=6)
    ax.text(4.15, 3.6, "(4, 4): costs \\$64,\nover budget", ha="left", va="top", fontsize=9.5, color=fs.RED,
            bbox=BOX, zorder=6)
    ax.text(0.25, 15.3, "(0, 15)", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(5.15, 0.6, "(5, 0)", ha="left", va="bottom", fontsize=9.5, bbox=BOX, zorder=6)
    ax.text(1.0, 2.0, "affordable", ha="left", va="center", fontsize=10, color=fs.GREEN)
    ax.text(6.5, 15.4, "12x + 4y = 60", ha="right", va="bottom", fontsize=10, color=fs.GREEN, style="italic",
            bbox=BOX, zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-budget")


def budget_changes():
    """Income rises from 60 to 84 (parallel shift); the ticket price rises from 12 to 15 (pivot)."""
    fig, axes = plt.subplots(1, 2, figsize=(7.8, 3.7))
    ax = axes[0]
    real_axes(ax, 9, 24, 1, 4, "tickets, x", "snacks, y")
    ax.plot([0, 5], [15, 0], color=fs.GREEN, zorder=3)
    ax.plot([0, 7], [21, 0], color=fs.BLUE, zorder=3)
    for px, py in [(5, 0), (7, 0), (0, 15), (0, 21)]:
        ax.plot(px, py, "o", color=fs.DARK, zorder=5, ms=4, clip_on=False)
    ax.text(5.1, 1.0, "5", ha="left", va="bottom", fontsize=9.5, color=fs.GREEN, zorder=6)
    ax.text(7.1, 1.0, "7", ha="left", va="bottom", fontsize=9.5, color=fs.BLUE, zorder=6)
    ax.text(0.3, 15.7, "15", ha="left", va="bottom", fontsize=9.5, color=fs.GREEN, zorder=6)
    ax.text(0.3, 21.7, "21", ha="left", va="bottom", fontsize=9.5, color=fs.BLUE, zorder=6)
    ax.text(5.6, 10.0, "budget \\$84", ha="left", va="center", fontsize=9.5, color=fs.BLUE, style="italic",
            bbox=BOX, zorder=6)
    ax.text(0.3, 5.0, "budget \\$60", ha="left", va="center", fontsize=9.5, color=fs.GREEN, style="italic",
            bbox=BOX, zorder=6)
    ax.text(0.5, -0.17, "income rises: parallel shift", transform=ax.transAxes, ha="center", va="top",
            fontsize=10)
    ax = axes[1]
    real_axes(ax, 9, 24, 1, 4, "tickets, x", "snacks, y")
    ax.plot([0, 5], [15, 0], color=fs.GREEN, zorder=3)
    ax.plot([0, 4], [15, 0], color=fs.RED, zorder=3)
    for px, py in [(5, 0), (4, 0), (0, 15)]:
        ax.plot(px, py, "o", color=fs.DARK, zorder=5, ms=4, clip_on=False)
    ax.text(5.1, 1.0, "5", ha="left", va="bottom", fontsize=9.5, color=fs.GREEN, zorder=6)
    ax.text(0.3, 15.7, "15", ha="left", va="bottom", fontsize=9.5, color=fs.DARK, zorder=6)
    ax.text(3.6, 9.6, "tickets \\$12", ha="left", va="center", fontsize=9.5, color=fs.GREEN, style="italic",
            bbox=BOX, zorder=6)
    ax.text(0.3, 2.5, "tickets \\$15", ha="left", va="center", fontsize=9.5, color=fs.RED, style="italic",
            bbox=BOX, zorder=6)
    ax.text(0.5, -0.17, "ticket price rises: pivot", transform=ax.transAxes, ha="center", va="top",
            fontsize=10)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-budget-changes")


if __name__ == "__main__":
    half_planes()
    corners()
    bakery()
    level_lines()
    budget()
    budget_changes()
