"""Figures for docs/03-high-school/08-geometry-and-proof/03-similarity.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/similarity.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402
import geomhelp as g  # noqa: E402

SLUG = "similarity"


def par_mark(ax, p, q, color=fs.DARK, size=0.13, n=1):
    """A chevron (arrow mark) on segment pq, the usual sign for parallel lines."""
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    for i in range(n):
        cx, cy = mx + ux * 0.1 * (i - (n - 1) / 2) * 2, my + uy * 0.1 * (i - (n - 1) / 2) * 2
        tip = (cx + ux * size, cy + uy * size)
        for s in (1, -1):
            ax.plot([cx - ux * size * 0.2 + s * nx * size * 0.8, tip[0]],
                    [cy - uy * size * 0.2 + s * ny * size * 0.8, tip[1]],
                    color=color, lw=1.5, zorder=6)


def construction():
    """The proof of SAS similarity: cut a copy of triangle DEF out of triangle ABC."""
    fig, ax = g.canvas(7.0, 3.0, (-0.8, 10.8), (-0.8, 3.6))
    A, B, C = (0, 0), (5, 0), (1.4, 3.2)
    P = (3, 0)
    Q = (0.6 * C[0], 0.6 * C[1])
    D, E, F = (7.5, 0), (10.5, 0), (7.5 + 0.6 * C[0], 0.6 * C[1])
    g.poly(ax, [A, B, C], fs.GREEN, alpha=0.08)
    g.poly(ax, [A, P, Q], fs.GREEN, edge=fs.GREEN, alpha=0.18, lw=2.4)
    g.seg(ax, P, Q, fs.GREEN, 2.4)
    g.poly(ax, [D, E, F], fs.BLUE, edge=fs.BLUE, alpha=0.18, lw=2.4)
    par_mark(ax, P, Q, fs.GREEN)
    par_mark(ax, C, B, fs.GREEN)
    g.tick(ax, A, P, 1, fs.GREEN)
    g.tick(ax, D, E, 1, fs.BLUE)
    g.arc(ax, A, B, C, 0.6, 1, fs.DARK)
    g.arc(ax, D, E, F, 0.6, 1, fs.DARK)
    for X, t, o in [(A, "A", (-0.25, -0.2)), (B, "B", (0.25, -0.2)), (C, "C", (0.0, 0.28)), (P, "P", (0.0, -0.3)),
                    (Q, "Q", (-0.28, 0.0)), (D, "D", (-0.25, -0.2)), (E, "E", (0.25, -0.2)), (F, "F", (0.0, 0.28))]:
        g.dot(ax, X)
        g.name(ax, X, t, o)
    g.save(fig, SLUG, "construction")


def splitter():
    """DE parallel to BC cuts AB and AC in proportion."""
    fig, ax = g.canvas(4.8, 3.6, (-0.8, 5.8), (-0.7, 3.7))
    A, B, C = (2.0, 3.2), (0, 0), (5, 0)
    D = (A[0] + 0.6 * (B[0] - A[0]), A[1] + 0.6 * (B[1] - A[1]))
    E = (A[0] + 0.6 * (C[0] - A[0]), A[1] + 0.6 * (C[1] - A[1]))
    g.poly(ax, [A, B, C], fs.GREEN, alpha=0.06)
    g.poly(ax, [A, D, E], fs.GREEN, alpha=0.16, edge=fs.GREEN, lw=2.2)
    par_mark(ax, D, E, fs.GREEN)
    par_mark(ax, B, C)
    for X, t, o in [(A, "A", (0, 0.28)), (B, "B", (-0.25, -0.2)), (C, "C", (0.25, -0.2)), (D, "D", (-0.25, 0.0)),
                    (E, "E", (0.25, 0.0))]:
        g.dot(ax, X)
        g.name(ax, X, t, o)
    g.label(ax, (0.55, 2.55), "AD", ha="center", box=False, size=10.5, color=fs.GREEN)
    g.label(ax, (0.0 - 0.1 + 0.2, 0.65), "DB", ha="center", box=False, size=10.5, color=fs.BLUE)
    g.label(ax, (3.55, 2.55), "AE", box=False, size=10.5, color=fs.GREEN)
    g.label(ax, (4.75, 0.65), "EC", box=False, size=10.5, color=fs.BLUE)
    g.save(fig, SLUG, "splitter")


RIGHT = dict(A=(0, 0), B=(13, 0), C=(4, 6), D=(4, 0))


def altitude():
    """The altitude to the hypotenuse, with all the lengths named."""
    fig, ax = g.canvas(5.6, 3.5, (-1.2, 14.0), (-1.8, 7.2))
    A, B, C, D = RIGHT["A"], RIGHT["B"], RIGHT["C"], RIGHT["D"]
    g.poly(ax, [A, B, C], fs.GREEN, alpha=0.06)
    g.seg(ax, C, D, fs.RED, 2.2)
    g.right_angle(ax, C, A, B, 0.6)
    g.right_angle(ax, D, A, C, 0.5)
    for X, t, o in [(A, "A", (-0.5, -0.4)), (B, "B", (0.5, -0.4)), (C, "C", (0.0, 0.55)), (D, "D", (0.0, -0.6))]:
        g.dot(ax, X)
        g.name(ax, X, t, o)
    g.label(ax, (2.0, -1.2), "p", color=fs.GREEN, box=False, size=11.5, style="italic")
    g.label(ax, (8.5, -1.2), "q", color=fs.BLUE, box=False, size=11.5, style="italic")
    g.label(ax, (4.55, 3.0), "h", color=fs.RED, box=False, size=11.5, style="italic")
    g.label(ax, (1.6, 3.6), "b", box=False, size=11.5, style="italic")
    g.label(ax, (9.1, 3.5), "a", box=False, size=11.5, style="italic")
    g.save(fig, SLUG, "altitude")


def three():
    """The three similar triangles of an altitude, side by side."""
    fig, axes = fs.plt.subplots(1, 3, figsize=(9.0, 2.9))
    A, B, C, D = RIGHT["A"], RIGHT["B"], RIGHT["C"], RIGHT["D"]
    alpha = math.degrees(math.atan2(6, 4))
    cases = [
        ("whole triangle", [A, B, C], "ABC"),
        ("left piece", [A, D, C], "ACD"),
        ("right piece", [D, B, C], "CBD"),
    ]
    for ax, (title, tri, nm) in zip(axes, cases):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-1.0, 14.0)
        ax.set_ylim(-1.8, 7.6)
        g.poly(ax, [A, B, C], None, edge=fs.GRAY, lw=1.4)
        g.seg(ax, C, D, fs.GRAY, 1.4)
        g.poly(ax, tri, fs.GREEN, edge=fs.GREEN, alpha=0.18, lw=2.4)
        for X, t, o in [(A, "A", (-0.6, -0.4)), (B, "B", (0.6, -0.4)), (C, "C", (0.0, 0.6)), (D, "D", (0.0, -0.7))]:
            g.name(ax, X, t, o, size=11)
        ax.text(6.5, -1.4, title, ha="center", va="center", fontsize=10.5, color=fs.DARK)
    # marks: alpha at A and beta at B in the whole; alpha at A, beta at C in the left; alpha at C, beta at B in the right
    ax0, ax1, ax2 = axes
    g.right_angle(ax0, C, A, B, 0.9)
    g.arc(ax0, A, B, C, 1.6, 1, fs.GREEN, text="\N{GREEK SMALL LETTER ALPHA}", text_r=2.4, size=11)
    g.arc(ax0, B, A, C, 1.6, 1, fs.BLUE, text="\N{GREEK SMALL LETTER BETA}", text_r=2.4, size=11)
    g.right_angle(ax1, D, A, C, 0.8)
    g.arc(ax1, A, D, C, 1.6, 1, fs.GREEN, text="\N{GREEK SMALL LETTER ALPHA}", text_r=2.4, size=11)
    g.arc(ax1, C, A, D, 1.6, 1, fs.BLUE, text="\N{GREEK SMALL LETTER BETA}", text_r=2.4, size=11)
    g.right_angle(ax2, D, B, C, 0.8)
    g.arc(ax2, C, D, B, 1.6, 1, fs.GREEN, text="\N{GREEK SMALL LETTER ALPHA}", text_r=2.4, size=11)
    g.arc(ax2, B, C, D, 1.6, 1, fs.BLUE, text="\N{GREEK SMALL LETTER BETA}", text_r=2.4, size=11)
    fig.subplots_adjust(wspace=0.02)
    g.save(fig, SLUG, "three-triangles")
    print("alpha", alpha)


def mirror():
    """Measuring a building with a mirror on the ground."""
    fig, ax = g.canvas(6.4, 3.6, (-1.5, 22.0), (-2.2, 13.8))
    eye, M, base, top = (0, 1.6), (2.4, 0), (20.4, 0), (20.4, 12)
    g.seg(ax, (-1.2, 0), (21.6, 0), fs.GRAY, 1.6)
    g.seg(ax, (0, 0), eye, fs.DARK, 3.2)
    g.seg(ax, base, top, fs.DARK, 3.2)
    g.dot(ax, eye)
    g.seg(ax, eye, M, fs.GREEN, 1.6, ls=(0, (5, 3)))
    g.seg(ax, M, top, fs.GREEN, 1.6, ls=(0, (5, 3)))
    ax.plot([M[0] - 0.5, M[0] + 0.5], [0, 0], color=fs.BLUE, lw=4, zorder=5, solid_capstyle="round")
    g.arc(ax, M, (3.4, 0), top, 1.3, 1, fs.GREEN)
    g.arc(ax, M, (1.4, 0), eye, 1.3, 1, fs.GREEN)
    g.label(ax, (-0.5, 0.8), "1.6 m", ha="right", box=False, size=9.5)
    g.label(ax, (1.2, -0.9), "2.4 m", box=False, size=9.5)
    g.label(ax, (11.4, -0.9), "18 m", box=False, size=9.5)
    g.label(ax, (21.0, 6.0), "h", ha="left", box=False, size=11.5, style="italic")
    g.label(ax, (12.0, 1.6), "equal angles at the mirror", box=False, size=9, color=fs.GREEN)
    g.label(ax, (2.4, -1.8), "mirror", box=False, size=9, color=fs.BLUE)
    g.right_angle(ax, base, (19.4, 0), top, 0.7)
    g.save(fig, SLUG, "mirror")


if __name__ == "__main__":
    construction()
    splitter()
    altitude()
    three()
    mirror()
