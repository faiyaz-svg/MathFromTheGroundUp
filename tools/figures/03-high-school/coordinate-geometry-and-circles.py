"""Figures for docs/03-high-school/08-geometry-and-proof/04-coordinate-geometry-and-circles.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/coordinate-geometry-and-circles.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402
from matplotlib.patches import Circle  # noqa: E402

import figstyle as fs  # noqa: E402
import geomhelp as g  # noqa: E402

SLUG = "coordinate-geometry-and-circles"
M = "\N{MINUS SIGN}"


def num(v):
    return f"{v:g}".replace("-", M)


def plane(ax, xmin, xmax, ymin, ymax, every=1, size=9, grid=True):
    ax.set_xlim(xmin - 0.6, xmax + 0.7)
    ax.set_ylim(ymin - 0.6, ymax + 0.7)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks(range(xmin, xmax + 1))
    ax.set_yticks(range(ymin, ymax + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    if grid:
        ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for t in range(xmin, xmax + 1):
        if t != 0 and t % every == 0:
            ax.text(t, -0.2, num(t), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
    for t in range(ymin, ymax + 1):
        if t != 0 and t % every == 0:
            ax.text(-0.2, t, num(t), ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)
    ax.text(xmax + 0.7, 0.3, "x", ha="right", va="bottom", style="italic", fontsize=12)
    ax.text(0.3, ymax + 0.7, "y", ha="left", va="top", style="italic", fontsize=12)


def parallelogram():
    """Parallelogram with vertices O, A, B, C and both diagonals meeting at their midpoint."""
    fig, ax = g.canvas(5.4, 3.3, (-0.9, 7.2), (-0.9, 3.4))
    a, b, c = 4.0, 2.0, 2.5
    O, A, B, C = (0, 0), (a, 0), (a + b, c), (b, c)
    Mid = ((a + b) / 2, c / 2)
    g.poly(ax, [O, A, B, C], fs.GREEN, alpha=0.08)
    g.seg(ax, O, B, fs.BLUE, 2.0, ls=(0, (5, 3)))
    g.seg(ax, A, C, fs.BLUE, 2.0, ls=(0, (5, 3)))
    for X, t, o in [(O, "O(0, 0)", (-0.15, -0.4)), (A, "A(a, 0)", (0.1, -0.4)), (B, "B(a + b, c)", (0.3, 0.38)),
                    (C, "C(b, c)", (-0.2, 0.38))]:
        g.dot(ax, X)
        g.name(ax, X, t, o, size=10.5)
    g.dot(ax, Mid, fs.RED)
    g.name(ax, Mid, "M", (0.0, 0.33), color=fs.RED, size=11.5, box=True)
    g.label(ax, (5.8, 1.0), "M = ((a + b)/2, c/2)", ha="left", box=False, size=9.5, color=fs.RED)
    g.save(fig, SLUG, "parallelogram")


def hypotenuse():
    """The midpoint of the hypotenuse is the centre of the circle through the three vertices."""
    fig, ax = g.canvas(4.8, 3.7, (-1.6, 6.4), (-1.4, 5.0))
    a, b = 2.4, 1.6
    O, A, B = (0, 0), (2 * a, 0), (0, 2 * b)
    Mid = (a, b)
    r = math.hypot(a, b)
    ax.add_patch(Circle(Mid, r, fill=False, edgecolor=fs.GRAY, lw=1.6, ls=(0, (5, 3)), zorder=2))
    g.poly(ax, [O, A, B], fs.GREEN, alpha=0.1)
    g.seg(ax, O, Mid, fs.RED, 2.0)
    g.right_angle(ax, O, A, B, 0.3)
    for X, t, o in [(O, "O(0, 0)", (-0.6, -0.35)), (A, "A(2a, 0)", (0.1, -0.55)), (B, "B(0, 2b)", (-0.15, 0.4))]:
        g.dot(ax, X)
        g.name(ax, X, t, o, size=10.5)
    g.dot(ax, Mid, fs.RED)
    g.name(ax, Mid, "M(a, b)", (0.75, 0.3), color=fs.RED, size=10.5, box=True)
    g.save(fig, SLUG, "hypotenuse")


def circle():
    """The circle (x - 3)^2 + (y + 2)^2 = 25 with its centre and radius."""
    fig, ax = fs.figure(4.8, 4.6)
    plane(ax, -3, 9, -8, 4, every=2)
    h, k, r = 3, -2, 5
    t = np.linspace(0, 2 * math.pi, 400)
    ax.plot(h + r * np.cos(t), k + r * np.sin(t), color=fs.GREEN, zorder=3)
    P = (7, 1)
    ax.plot([h, P[0]], [k, P[1]], color=fs.RED, lw=2, zorder=4)
    ax.plot([h, P[0], P[0]], [k, k, P[1]], color=fs.GRAY, lw=1.4, ls=(0, (4, 3)), zorder=3)
    for X, c in [((h, k), fs.DARK), (P, fs.DARK)]:
        ax.plot(*X, "o", color=c, zorder=6)
    ax.text(h - 0.25, k - 0.35, "(3, " + M + "2)", ha="right", va="top", fontsize=10, bbox=g.BOX, zorder=7)
    ax.text(P[0] + 0.25, P[1] + 0.1, "(7, 1)", ha="left", va="bottom", fontsize=10, bbox=g.BOX, zorder=7)
    ax.text(4.5, 0.0, "r = 5", ha="right", va="bottom", fontsize=10.5, color=fs.RED, bbox=g.BOX, zorder=7)
    ax.text(5.0, k + 0.2, "4", ha="center", va="bottom", fontsize=10, color=fs.DARK)
    ax.text(P[0] + 0.2, -0.5, "3", ha="left", va="center", fontsize=10, color=fs.DARK)
    fs.save(fig, g.FOLDER, f"{SLUG}-circle")


def tangent():
    """A tangent line cannot be slanted against the radius: the point Q would be a second point on the circle."""
    fig, ax = g.canvas(4.4, 4.5, (-4.6, 3.6), (-3.4, 4.8))
    O = np.array((0.0, 0.0))
    r = 3.0
    ang = math.radians(100)
    P = np.array((r * math.cos(ang), r * math.sin(ang)))
    d = np.array((math.cos(math.radians(40)), math.sin(math.radians(40))))
    d /= np.linalg.norm(d)
    # foot of the perpendicular from O onto the line through P with direction d
    F = P - np.dot(P, d) * d + np.dot(P, d) * d  # placeholder, replaced below
    t0 = -np.dot(P - O, d)
    F = P + t0 * d
    Q = 2 * F - P
    ax.add_patch(Circle((0, 0), r, fill=False, edgecolor=fs.GRAY, lw=1.6, zorder=2))
    ends = (Q - 1.0 * d, P + 1.8 * d)
    g.seg(ax, tuple(ends[0]), tuple(ends[1]), fs.DARK, 2.0)
    g.seg(ax, tuple(O), tuple(P), fs.GREEN, 2.0)
    g.seg(ax, tuple(O), tuple(F), fs.RED, 2.0)
    g.seg(ax, tuple(O), tuple(Q), fs.GREEN, 2.0)
    g.right_angle(ax, tuple(F), tuple(O), tuple(P), 0.22, fs.RED)
    g.tick(ax, tuple(P), tuple(F), 1, fs.BLUE)
    g.tick(ax, tuple(F), tuple(Q), 1, fs.BLUE)
    g.tick(ax, tuple(O), tuple(P), 2, fs.GREEN)
    g.tick(ax, tuple(O), tuple(Q), 2, fs.GREEN)
    for X, tx, o in [(O, "O", (-0.05, -0.32)), (P, "P", (0.3, 0.12)), (F, "F", (-0.3, 0.25)), (Q, "Q", (-0.32, -0.12))]:
        g.dot(ax, tuple(X))
        g.name(ax, tuple(X), tx, o)
    g.label(ax, (ends[1][0] + 0.55, ends[1][1] + 0.1), "line ℓ", box=False, size=11, ha="center")
    g.save(fig, SLUG, "tangent")
    print("check", np.linalg.norm(Q), np.linalg.norm(P), np.dot(F - O, d))


def line_circle():
    """The lines 3x + 4y = c against the circle x^2 + y^2 = 25: two points, one point, none."""
    fig, axes = fs.plt.subplots(1, 3, figsize=(9.2, 3.9))
    t = np.linspace(0, 2 * math.pi, 400)
    cases = [(10, "secant: 2 points", [(-2, 4), (6, -2)]),
             (25, "tangent: 1 point", [(3, 4)]),
             (35, "miss: no points", [])]
    for ax, (cc, title, pts) in zip(axes, cases):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-6.5, 11)
        ax.set_ylim(-10.0, 9.4)
        ax.plot(5 * np.cos(t), 5 * np.sin(t), color=fs.GREEN, lw=2.0)
        ax.plot([-6, 11], [0, 0], color=fs.GRAY, lw=0.8)
        ax.plot([0, 0], [-6.5, 9.0], color=fs.GRAY, lw=0.8)
        xs = np.array([-6.0, 11.0])
        ax.plot(xs, (cc - 3 * xs) / 4, color=fs.BLUE, lw=2.0)
        if cc == 10:
            for x in ((10 - 4 * y) / 3 for y in []):
                pass
            # intersections of 3x + 4y = 10 with x^2 + y^2 = 25
            a, b, c = 25, -60, 100 - 400
            disc = b * b - 4 * a * c
            for s in (1, -1):
                x = (-b + s * math.sqrt(disc)) / (2 * a)
                ax.plot(x, (10 - 3 * x) / 4, "o", color=fs.DARK, zorder=5)
        elif cc == 25:
            ax.plot(3, 4, "o", color=fs.DARK, zorder=5)
            ax.plot([0, 3], [0, 4], color=fs.RED, lw=1.6)
            g.right_angle(ax, (3, 4), (0, 0), (3 + 4, 4 - 3), 0.7)
        ax.text(2.5, -7.4, f"3x + 4y = {cc}", ha="center", va="center", fontsize=10, color=fs.BLUE)
        ax.text(2.5, -9.2, title, ha="center", va="center", fontsize=11, color=fs.DARK)
    fig.subplots_adjust(wspace=0.02)
    g.save(fig, SLUG, "line-circle")


if __name__ == "__main__":
    parallelogram()
    hypotenuse()
    circle()
    tangent()
    line_circle()
