"""Figures for docs/03-high-school/01-algebra-foundations/03-compound-inequalities-and-interval-notation.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/compound-inequalities-and-interval-notation.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import algebra_numberline as nl  # noqa: E402

fs = nl.fs

FOLDER = "03-high-school"
SLUG = "compound-inequalities-and-interval-notation"


def interval_types():
    """Six interval types: the inequality, the graph and the interval notation."""
    lo, hi = -3.6, 5.6
    rows = [
        (r"$-1 < x < 3$", r"$(-1,\ 3)$", ("seg", -1, 3, False, False)),
        (r"$-1 \leq x \leq 3$", r"$[-1,\ 3]$", ("seg", -1, 3, True, True)),
        (r"$-1 \leq x < 3$", r"$[-1,\ 3)$", ("seg", -1, 3, True, False)),
        (r"$-1 < x \leq 3$", r"$(-1,\ 3]$", ("seg", -1, 3, False, True)),
        (r"$x > 1$", r"$(1,\ \infty)$", ("ray", 1, +1, False)),
        (r"$x \leq 2$", r"$(-\infty,\ 2]$", ("ray", 2, -1, True)),
    ]
    gap = 1.25
    fig, ax = nl.canvas(7.0, 4.3, (-7.6, 9.4), (-(len(rows) - 1) * gap - 0.7, 0.5))
    for i, (left, right, spec) in enumerate(rows):
        y = -i * gap
        nl.axis_line(ax, y, lo, hi, range(-3, 6), size=8, label_gap=0.14)
        if spec[0] == "seg":
            nl.segment(ax, y, spec[1], spec[2], spec[3], spec[4])
        else:
            nl.ray(ax, y, spec[1], spec[2], spec[3], hi, lo)
        ax.text(-7.4, y + 0.1, left, ha="left", va="center", fontsize=11)
        ax.text(6.6, y + 0.1, right, ha="left", va="center", fontsize=11, color=fs.GREEN, fontweight="bold")
    fs.save(fig, FOLDER, f"{SLUG}-interval-types")


def intersection():
    """x > -2 and x <= 4: the overlap is (-2, 4]."""
    lo, hi = -4.6, 6.6
    fig, ax = nl.canvas(6.8, 3.2, (-7.8, 9.6), (-3.6, 0.7))
    ys = [0, -1.3, -2.8]
    for y in ys:
        nl.axis_line(ax, y, lo, hi, range(-4, 7), size=8, label_gap=0.14)
    nl.guide(ax, -2, 0.35, ys[2] - 0.2)
    nl.guide(ax, 4, 0.35, ys[2] - 0.2)
    nl.ray(ax, ys[0], -2, +1, False, hi, lo, colour=fs.BLUE)
    nl.ray(ax, ys[1], 4, -1, True, hi, lo, colour=fs.ORANGE)
    nl.segment(ax, ys[2], -2, 4, False, True, colour=fs.GREEN)
    ax.text(-7.6, ys[0] + 0.1, r"$x > -2$", ha="left", va="center", fontsize=11, color=fs.BLUE)
    ax.text(-7.6, ys[1] + 0.1, r"$x \leq 4$", ha="left", va="center", fontsize=11, color=fs.ORANGE)
    ax.text(-7.6, ys[2] + 0.1, "both", ha="left", va="center", fontsize=11, color=fs.GREEN)
    ax.text(7.1, ys[2] + 0.1, r"$(-2,\ 4]$", ha="left", va="center", fontsize=11, color=fs.GREEN, fontweight="bold")
    fs.save(fig, FOLDER, f"{SLUG}-intersection")


def union():
    """x < -2 or x >= 2: the union is (-inf, -2) U [2, inf)."""
    lo, hi = -5.6, 5.6
    fig, ax = nl.canvas(6.8, 3.2, (-8.8, 10.6), (-3.6, 0.7))
    ys = [0, -1.3, -2.8]
    for y in ys:
        nl.axis_line(ax, y, lo, hi, range(-5, 6), size=8, label_gap=0.14)
    nl.guide(ax, -2, 0.35, ys[2] - 0.2)
    nl.guide(ax, 2, 0.35, ys[2] - 0.2)
    nl.ray(ax, ys[0], -2, -1, False, hi, lo, colour=fs.BLUE)
    nl.ray(ax, ys[1], 2, +1, True, hi, lo, colour=fs.ORANGE)
    nl.ray(ax, ys[2], -2, -1, False, hi, lo, colour=fs.GREEN)
    nl.ray(ax, ys[2], 2, +1, True, hi, lo, colour=fs.GREEN)
    ax.text(-8.6, ys[0] + 0.1, r"$x < -2$", ha="left", va="center", fontsize=11, color=fs.BLUE)
    ax.text(-8.6, ys[1] + 0.1, r"$x \geq 2$", ha="left", va="center", fontsize=11, color=fs.ORANGE)
    ax.text(-8.6, ys[2] + 0.1, "either", ha="left", va="center", fontsize=11, color=fs.GREEN)
    ax.text(
        6.2,
        ys[2] + 0.1,
        r"$(-\infty,\ -2) \cup [2,\ \infty)$",
        ha="left",
        va="center",
        fontsize=11,
        color=fs.GREEN,
        fontweight="bold",
    )
    fs.save(fig, FOLDER, f"{SLUG}-union")


def special_cases():
    """The empty set, a single point, a line with one point missing, and all of R."""
    lo, hi = -0.6, 5.6
    rows = [
        (r"$x < 1$ and $x > 3$", r"$\emptyset$", "empty"),
        (r"$x \leq 2$ and $x \geq 2$", r"$\{2\}$", "point"),
        (r"$x < 2$ or $x > 2$", r"$(-\infty,\ 2) \cup (2,\ \infty)$", "punctured"),
        (r"$x < 3$ or $x > 1$", r"$(-\infty,\ \infty)$", "all"),
    ]
    gap = 1.25
    fig, ax = nl.canvas(7.4, 3.5, (-5.4, 11.0), (-(len(rows) - 1) * gap - 0.7, 0.5))
    for i, (left, right, kind) in enumerate(rows):
        y = -i * gap
        nl.axis_line(ax, y, lo, hi, range(0, 6), size=8, label_gap=0.14)
        if kind == "point":
            nl.dot(ax, 2, y, True)
        elif kind == "punctured":
            nl.whole_line(ax, y, lo, hi)
            nl.dot(ax, 2, y, False)
        elif kind == "all":
            nl.whole_line(ax, y, lo, hi)
        ax.text(-5.2, y + 0.1, left, ha="left", va="center", fontsize=11)
        ax.text(6.1, y + 0.1, right, ha="left", va="center", fontsize=11, color=fs.GREEN, fontweight="bold")
    fs.save(fig, FOLDER, f"{SLUG}-special-cases")


if __name__ == "__main__":
    interval_types()
    intersection()
    union()
    special_cases()
