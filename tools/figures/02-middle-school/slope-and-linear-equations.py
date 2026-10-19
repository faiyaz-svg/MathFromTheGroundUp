"""Figures for docs/02-middle-school/05-linear-relationships-and-functions/02-slope-and-linear-equations.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/slope-and-linear-equations.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "slope-and-linear-equations"
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


def taxi():
    fig, ax = fs.figure(5.2, 3.8)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 26)
    ax.set_xticks(range(0, 11))
    ax.set_yticks(range(0, 27, 2))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    xs = [0, 10]
    ax.plot(xs, [2 * x + 4.5 for x in xs], color=fs.GREEN, zorder=3, clip_on=False)
    # Slope triangle from (2, 8.5): run 3 km, rise 6 dollars.
    ax.plot([2, 5], [8.5, 8.5], color=fs.BLUE, lw=1.6, zorder=4)
    ax.plot([5, 5], [8.5, 14.5], color=fs.RED, lw=1.6, zorder=4)
    ax.text(3.5, 8.1, "run = 3 km", ha="center", va="top", fontsize=10, color=fs.BLUE, bbox=BOX)
    ax.text(5.15, 11.5, r"rise = \$6", ha="left", va="center", fontsize=10, color=fs.RED, bbox=BOX)
    ax.plot([2, 5], [8.5, 14.5], "o", color=fs.GREEN, zorder=5, ms=5)
    ax.plot(0, 4.5, "o", color=fs.GREEN, zorder=5, ms=6, clip_on=False)
    ax.text(0.25, 4.0, r"starts at \$4.50", ha="left", va="top", fontsize=10, color=fs.DARK, bbox=BOX)
    ax.text(7.3, 21.2, "y = 2x + 4.5", ha="right", va="bottom", fontsize=11, color=fs.GREEN,
            style="italic", bbox=BOX)
    ax.set_xlabel("distance (km)")
    ax.set_ylabel("fare (dollars)")
    fs.save(fig, FOLDER, f"{SLUG}-taxi")


def four_slopes():
    fig, axes = plt.subplots(2, 2, figsize=(6.0, 6.0))
    cases = [
        ("positive slope:\nrises to the right", "right",
         lambda a: a.plot([-11 / 3, 7 / 3], [-4.5, 4.5], color=fs.GREEN)),
        ("negative slope:\nfalls to the right", "left",
         lambda a: a.plot([-7 / 3, 11 / 3], [4.5, -4.5], color=fs.BLUE)),
        ("zero slope:\nhorizontal", "right", lambda a: a.axhline(3, color=fs.ORANGE, lw=2)),
        ("undefined slope:\nvertical", "right", lambda a: a.axvline(-3, color=fs.RED, lw=2)),
    ]
    for ax, (text, side, draw) in zip(axes.flat, cases):
        plane(ax, -4, 4, -4, 4, every=2, size=9)
        draw(ax)
        x = 4.5 if side == "right" else -4.4
        ax.text(x, -3.6, text, ha=side, va="bottom", fontsize=11, bbox=BOX, zorder=6)
    fig.tight_layout(w_pad=1.2, h_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-four-slopes")


def two_points():
    fig, ax = fs.figure(4.6, 5.2)
    plane(ax, -3, 5, -3, 9)
    xs = [-2.0, 4.0]
    ax.plot(xs, [-2 * x + 5 for x in xs], color=fs.GREEN, zorder=3)
    ax.plot([-1, -1], [7, -1], color=fs.RED, lw=1.6, ls="--", zorder=3)
    ax.plot([-1, 3], [-1, -1], color=fs.BLUE, lw=1.6, ls="--", zorder=3)
    ax.text(1.0, -1.3, "run = 4", ha="center", va="top", fontsize=10, color=fs.BLUE, bbox=BOX)
    ax.text(-1.2, 2.5, f"rise = {M}8", ha="right", va="center", fontsize=10, color=fs.RED, bbox=BOX)
    for x, y, text, dx, dy, ha, va in [
        (-1, 7, f"({M}1, 7)", -0.3, 0.0, "right", "center"),
        (3, -1, f"(3, {M}1)", 0.25, 0.0, "left", "center"),
        (0, 5, "(0, 5)", 0.25, 0.0, "left", "center"),
        (2.5, 0, "(2.5, 0)", 0.2, 0.25, "left", "bottom"),
    ]:
        ax.plot(x, y, "o", color=fs.GREEN, zorder=5)
        ax.text(x + dx, y + dy, text, ha=ha, va=va, fontsize=10, bbox=BOX, zorder=6)
    ax.text(1.5, 6.0, f"y = {M}2x + 5", ha="left", va="center", fontsize=11, color=fs.GREEN,
            style="italic", bbox=BOX, zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-two-points")


def parallel():
    fig, ax = fs.figure(5.2, 5.2)
    plane(ax, -7, 9, -8, 8, every=2)
    xs = [-7.5, 9.5]
    ax.plot(xs, [2 / 3 * x + 4 for x in xs], color=fs.GREEN, zorder=3)
    ax.plot(xs, [2 / 3 * x - 5 for x in xs], color=fs.BLUE, zorder=3)
    for b, colour in [(4, fs.GREEN), (-5, fs.BLUE)]:
        x0 = 3 if b == 4 else 0
        y0 = 2 / 3 * x0 + b
        ax.plot([x0, x0 + 3], [y0, y0], color=colour, lw=1.4, ls="--", zorder=3)
        ax.plot([x0 + 3, x0 + 3], [y0, y0 + 2], color=colour, lw=1.4, ls="--", zorder=3)
        ax.text(x0 + 1.5, y0 - 0.3, "3", ha="center", va="top", fontsize=10, color=colour, bbox=BOX)
        ax.text(x0 + 3.25, y0 + 1, "2", ha="left", va="center", fontsize=10, color=colour, bbox=BOX)
    ax.plot(0, 4, "o", color=fs.GREEN, zorder=5)
    ax.plot(6, -1, "o", color=fs.BLUE, zorder=5)
    ax.text(6.3, -1.4, f"(6, {M}1)", ha="left", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.text(-1.0, 6.5, "y = (2/3)x + 4", ha="right", va="center", fontsize=11, color=fs.GREEN,
            style="italic", bbox=BOX, zorder=6)
    ax.text(9.4, 2.4, "y = (2/3)x " + M + " 5", ha="right", va="bottom", fontsize=11, color=fs.BLUE,
            style="italic", bbox=BOX, zorder=6)
    fs.save(fig, FOLDER, f"{SLUG}-parallel")


if __name__ == "__main__":
    taxi()
    four_slopes()
    two_points()
    parallel()
