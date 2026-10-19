"""Figures for docs/02-middle-school/05-linear-relationships-and-functions/04-systems-of-linear-equations.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/02-middle-school/systems-of-linear-equations.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
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


def phone_plans():
    fig, ax = fs.figure(5.2, 3.8)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 85)
    ax.set_xticks(range(0, 11))
    ax.set_yticks(range(0, 81, 10))
    ax.set_yticks(range(0, 86, 5), minor=True)
    ax.grid(True, which="major")
    ax.grid(True, which="minor", lw=0.35, color="#e6e8ea")
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    xs = [0, 10]
    ax.plot(xs, [30 + 5 * x for x in xs], color=fs.GREEN, zorder=3, clip_on=False)
    ax.plot(xs, [45 + 2 * x for x in xs], color=fs.BLUE, zorder=3, clip_on=False)
    ax.plot(5, 55, "o", color=fs.DARK, zorder=5)
    ax.text(4.85, 57, "(5, 55)", ha="right", va="bottom", fontsize=10, bbox=BOX, zorder=6)
    ax.text(8.3, 74.5, r"plan A: \$30 + \$5 per GB", ha="right", va="bottom", fontsize=10,
            color=fs.GREEN, bbox=BOX, zorder=6)
    ax.text(9.9, 54, r"plan B: \$45 + \$2 per GB", ha="right", va="top", fontsize=10,
            color=fs.BLUE, bbox=BOX, zorder=6)
    ax.set_xlabel("data used in a month (GB)")
    ax.set_ylabel("monthly cost (dollars)")
    fs.save(fig, FOLDER, f"{SLUG}-phone-plans")


def three_cases():
    fig, axes = plt.subplots(1, 3, figsize=(7.5, 3.0))
    lo, hi = -4.5, 4.5
    cases = [
        ("one solution:\nthe lines cross once",
         [(lambda x: x + 1, fs.GREEN, "-"), (lambda x: -2 * x + 4, fs.BLUE, "-")], (1, 2)),
        ("no solution:\nparallel lines",
         [(lambda x: 0.5 * x + 2, fs.GREEN, "-"), (lambda x: 0.5 * x - 2, fs.BLUE, "-")], None),
        ("infinitely many:\nthe same line",
         [(lambda x: -x + 1, fs.GREEN, "-"), (lambda x: -x + 1, fs.BLUE, (0, (3, 3)))], None),
    ]
    for ax, (text, lines, point) in zip(axes, cases):
        plane(ax, -4, 4, -4, 4, every=2, size=8)
        for i, (f, colour, ls) in enumerate(lines):
            width = 5.0 if (i == 0 and point is None and ls == "-" and text.startswith("inf")) else 2.0
            ax.plot([lo, hi], [f(lo), f(hi)], color=colour, ls=ls, lw=width, zorder=3 + i)
        if point:
            ax.plot(*point, "o", color=fs.DARK, zorder=5)
        ax.text(0.5, -0.03, text, transform=ax.transAxes, ha="center", va="top", fontsize=11)
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-three-cases")


def break_even():
    fig, ax = fs.figure(5.2, 3.8)
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 1600)
    ax.set_xticks(range(0, 81, 10))
    ax.set_yticks(range(0, 1601, 200))
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    xs = [0, 40, 80]
    cost = [600 + 4 * x for x in xs]
    revenue = [19 * x for x in xs]
    ax.fill_between(xs[:2], revenue[:2], cost[:2], color=fs.RED, alpha=0.10, lw=0)
    ax.fill_between(xs[1:], cost[1:], revenue[1:], color=fs.GREEN, alpha=0.12, lw=0)
    ax.plot(xs, cost, color=fs.BLUE, zorder=3, clip_on=False)
    ax.plot(xs, revenue, color=fs.GREEN, zorder=3, clip_on=False)
    ax.plot(40, 760, "o", color=fs.DARK, zorder=5)
    ax.text(41.5, 730, "break-even\n(40, 760)", ha="left", va="top", fontsize=10, bbox=BOX, zorder=6)
    ax.text(20, 560, "loss", ha="center", va="center", fontsize=11, color=fs.RED)
    ax.text(68, 1080, "profit", ha="center", va="center", fontsize=11, color=fs.GREEN)
    ax.text(78, 790, "cost y = 600 + 4x", ha="right", va="top", fontsize=10, color=fs.BLUE,
            style="italic", bbox=BOX, zorder=6)
    ax.text(62, 1420, "revenue y = 19x", ha="right", va="bottom", fontsize=10, color=fs.GREEN,
            style="italic", bbox=BOX, zorder=6)
    ax.set_xlabel("phone cases made and sold")
    ax.set_ylabel("dollars")
    fs.save(fig, FOLDER, f"{SLUG}-break-even")


if __name__ == "__main__":
    phone_plans()
    three_cases()
    break_even()
