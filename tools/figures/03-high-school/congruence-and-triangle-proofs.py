"""Figures for docs/03-high-school/08-geometry-and-proof/02-congruence-and-triangle-proofs.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/congruence-and-triangle-proofs.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402
import geomhelp as g  # noqa: E402

SLUG = "congruence-and-triangle-proofs"


def polar(r, deg, c=(0, 0)):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))


def tests():
    """Six panels: the five congruence tests and the failed SSA."""
    fig, axes = fs.plt.subplots(2, 3, figsize=(8.4, 5.0))
    shapes = {
        "SSS": ((0, 0), (3.0, 0), (1.0, 2.0), {"AB", "BC", "CA"}, set()),
        "SAS": ((0, 0), (3.0, 0), (1.0, 2.0), {"AB", "CA"}, {"A"}),
        "ASA": ((0, 0), (3.0, 0), (1.0, 2.0), {"AB"}, {"A", "B"}),
        "AAS": ((0, 0), (3.0, 0), (1.0, 2.0), {"BC"}, {"A", "B"}),
        "HL": ((0, 0), (3.0, 0), (3.0, 2.0), {"AB", "CA"}, {"B"}),
        "SSA": ((0, 0), (3.0, 0), (1.0, 2.0), {"CA", "BC"}, {"A"}),
    }
    notes = {
        "SSS": "three sides",
        "SAS": "two sides and the\nangle between them",
        "ASA": "two angles and the\nside between them",
        "AAS": "two angles and a side\nnot between them",
        "HL": "right angle, hypotenuse\nand one leg",
        "SSA": "two sides and an angle\nnot between them",
    }
    for ax, (key, (A, B, C, sides, angs)) in zip(axes.flat, shapes.items()):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-0.8, 3.8)
        ax.set_ylim(-1.5, 2.4)
        g.poly(ax, [A, B, C], fs.GREEN if key != "SSA" else fs.RED, edge=fs.GRAY, alpha=0.08, lw=1.6)
        col = fs.GREEN if key != "SSA" else fs.RED
        sd = {"AB": (A, B), "BC": (B, C), "CA": (C, A)}
        n = 0
        for k, (p, q) in sd.items():
            if k in sides:
                n += 1
                g.seg(ax, p, q, col, 2.8)
                g.tick(ax, p, q, n if key == "SSS" else 1, col)
        for v, (p1, p2) in {"A": (B, C), "B": (A, C), "C": (A, B)}.items():
            P = {"A": A, "B": B, "C": C}[v]
            if v in angs:
                if key == "HL":
                    g.right_angle(ax, P, p1, p2, 0.22, col)
                else:
                    g.arc(ax, P, p1, p2, 0.4, 1, col)
        for P, t, o in [(A, "A", (-0.2, -0.15)), (B, "B", (0.2, -0.15)), (C, "C", (0.0, 0.22) if key != "HL" else (0.2, 0.12))]:
            g.name(ax, P, t, o, size=11)
        title = key + (" fails" if key == "SSA" else "")
        ax.text(1.5, -0.6, title, ha="center", va="center", fontsize=12, weight="bold",
                color=col)
        ax.text(1.5, -1.1, notes[key], ha="center", va="center", fontsize=8.6, color=fs.DARK)
    fig.subplots_adjust(hspace=0.02, wspace=0.02)
    g.save(fig, SLUG, "tests")


def ssa():
    """Angle 30 degrees, AC = 8 and BC = 5 fit two different triangles."""
    fig, ax = g.canvas(6.2, 3.1, (-0.8, 11.0), (-1.1, 4.9))
    A = (0, 0)
    C = polar(8, 30)
    r = math.sqrt(25 - 16)
    B1, B2 = (C[0] - r, 0), (C[0] + r, 0)
    g.seg(ax, A, (10.6, 0), fs.GRAY, 1.6)
    g.poly(ax, [A, B1, C], fs.GREEN, edge=fs.GREEN, alpha=0.1, lw=2.2)
    g.poly(ax, [A, B2, C], fs.RED, edge=fs.RED, alpha=0.06, lw=2.2)
    g.arc(ax, A, B2, C, 1.3, 1, fs.DARK, text="30\N{DEGREE SIGN}", text_r=1.95, size=10.5)
    g.tick(ax, C, B1, 1, fs.GREEN)
    g.tick(ax, C, B2, 1, fs.RED)
    g.label(ax, (C[0] - 1.15, 1.7), "5", color=fs.GREEN, box=False, size=11)
    g.label(ax, (C[0] + 1.75, 2.2), "5", color=fs.RED, box=False, size=11)
    g.label(ax, (2.9, 2.4), "8", box=False, size=11)
    for P, t, o in [(A, "A", (-0.25, -0.2)), (C, "C", (0.0, 0.3)), (B1, "B", (0.0, -0.4)), (B2, "B'", (0.1, -0.4))]:
        g.dot(ax, P)
        g.name(ax, P, t, o)
    g.save(fig, SLUG, "ssa")


def isosceles():
    """Isosceles triangle ABC with the bisector AD of the vertex angle."""
    fig, ax = g.canvas(4.2, 3.4, (-3.0, 3.0), (-0.7, 3.6))
    A, B, C, D = (0, 3.0), (-2.4, 0), (2.4, 0), (0, 0)
    g.poly(ax, [A, B, C], fs.GREEN, alpha=0.08)
    g.seg(ax, A, D, fs.GRAY, 1.8, ls=(0, (5, 3)))
    g.tick(ax, A, B, 1)
    g.tick(ax, A, C, 1)
    g.arc(ax, A, B, D, 0.7, 1, fs.BLUE)
    g.arc(ax, A, D, C, 0.7, 1, fs.BLUE)
    g.arc(ax, B, A, C, 0.55, 2, fs.GREEN)
    g.arc(ax, C, A, B, 0.55, 2, fs.GREEN)
    for P, t, o in [(A, "A", (0, 0.28)), (B, "B", (-0.25, -0.2)), (C, "C", (0.25, -0.2)), (D, "D", (0, -0.28))]:
        g.dot(ax, P)
        g.name(ax, P, t, o)
    g.save(fig, SLUG, "isosceles")


def perpbis():
    """P on the perpendicular bisector of AB."""
    fig, ax = g.canvas(4.6, 3.6, (-3.2, 3.2), (-1.0, 3.7))
    A, B, M, P = (-2.6, 0), (2.6, 0), (0, 0), (0, 3.0)
    g.seg(ax, (0, -0.7), (0, 3.4), fs.GRAY, 1.5, ls=(0, (5, 3)))
    g.seg(ax, A, B)
    g.seg(ax, P, A, fs.GREEN, 2.2)
    g.seg(ax, P, B, fs.GREEN, 2.2)
    g.seg(ax, P, M, fs.BLUE, 1.8)
    g.tick(ax, A, M, 1)
    g.tick(ax, M, B, 1)
    g.tick(ax, P, A, 2, fs.GREEN)
    g.tick(ax, P, B, 2, fs.GREEN)
    g.right_angle(ax, M, B, P, 0.25)
    for Q, t, o in [(A, "A", (-0.25, -0.2)), (B, "B", (0.25, -0.2)), (M, "M", (0.3, -0.25)), (P, "P", (0.3, 0.1))]:
        g.dot(ax, Q)
        g.name(ax, Q, t, o)
    g.label(ax, (0.55, 3.45), "perpendicular bisector of AB", ha="left", box=False, size=9.5, color=fs.GRAY)
    g.save(fig, SLUG, "perpendicular-bisector")


def anglebis():
    """P on the bisector of angle BAC, with its distances PD and PE to the two sides."""
    fig, ax = g.canvas(5.0, 3.6, (-0.6, 5.6), (-0.7, 4.4))
    A = (0, 0)
    Bp, Cp = polar(5.2, 0), polar(5.2, 50)
    P = polar(3.8, 25)
    D = (P[0], 0)
    t = 3.8 * math.cos(math.radians(25))
    E = polar(t, 50)
    g.seg(ax, A, Bp)
    g.seg(ax, A, Cp)
    g.seg(ax, A, polar(4.6, 25), fs.GRAY, 1.8, ls=(0, (5, 3)))
    g.seg(ax, P, D, fs.GREEN, 2.2)
    g.seg(ax, P, E, fs.GREEN, 2.2)
    g.tick(ax, P, D, 1, fs.GREEN)
    g.tick(ax, P, E, 1, fs.GREEN)
    g.arc(ax, A, Bp, P, 1.0, 1, fs.BLUE, text="x", text_r=1.4, size=11)
    g.arc(ax, A, P, Cp, 1.0, 1, fs.BLUE, text="x", text_r=1.4, size=11)
    g.right_angle(ax, D, A, P, 0.22)
    g.right_angle(ax, E, A, P, 0.22)
    for Q, tx, o in [(A, "A", (-0.25, -0.2)), (P, "P", (0.25, 0.12)), (D, "D", (0.0, -0.3)), (E, "E", (-0.25, 0.15)),
                     (Bp, "B", (0.25, 0.0)), (Cp, "C", (0.15, 0.25))]:
        g.dot(ax, Q)
        g.name(ax, Q, tx, o)
    g.save(fig, SLUG, "angle-bisector")


def overlap():
    """Overlapping triangles ABC and DCB sharing the side BC."""
    fig, ax = g.canvas(5.0, 3.4, (-0.7, 5.7), (-0.7, 3.6))
    B, C, A, D = (0, 0), (5, 0), (1, 3), (4, 3)
    E = (2.5, 1.875)
    g.poly(ax, [A, B, C], fs.GREEN, edge=fs.GREEN, alpha=0.1, lw=2.0)
    g.poly(ax, [D, C, B], fs.BLUE, edge=fs.BLUE, alpha=0.1, lw=2.0)
    g.seg(ax, A, D, fs.GRAY, 1.4, ls=(0, (5, 3)))
    g.tick(ax, A, B, 1, fs.GREEN)
    g.tick(ax, D, C, 1, fs.BLUE)
    g.arc(ax, B, A, C, 0.6, 1, fs.DARK)
    g.arc(ax, C, D, B, 0.6, 1, fs.DARK)
    for Q, t, o in [(A, "A", (-0.1, 0.28)), (D, "D", (0.1, 0.28)), (B, "B", (-0.25, -0.2)), (C, "C", (0.25, -0.2)),
                    (E, "E", (0.0, -0.3))]:
        g.dot(ax, Q)
        g.name(ax, Q, t, o)
    g.save(fig, SLUG, "overlap")


def crossing():
    """Segments AB and CD bisect each other at M; AC is parallel to BD."""
    fig, ax = g.canvas(5.0, 3.2, (-3.6, 3.6), (-2.4, 2.4))
    M = (0, 0)
    A, B, C, D = (-3, 1.2), (3, -1.2), (-2, -1.8), (2, 1.8)
    g.seg(ax, A, B)
    g.seg(ax, C, D)
    g.seg(ax, A, C, fs.BLUE, 2.0, ls=(0, (5, 3)))
    g.seg(ax, B, D, fs.BLUE, 2.0, ls=(0, (5, 3)))
    g.tick(ax, A, M, 1)
    g.tick(ax, M, B, 1)
    g.tick(ax, C, M, 2)
    g.tick(ax, M, D, 2)
    g.arc(ax, M, A, C, 0.5, 1, fs.GREEN)
    g.arc(ax, M, B, D, 0.5, 1, fs.GREEN)
    for Q, t, o in [(A, "A", (-0.25, 0.15)), (B, "B", (0.25, -0.15)), (C, "C", (-0.1, -0.3)), (D, "D", (0.1, 0.3)),
                    (M, "M", (0.05, -0.34))]:
        g.dot(ax, Q)
        g.name(ax, Q, t, o)
    g.save(fig, SLUG, "crossing")


if __name__ == "__main__":
    tests()
    ssa()
    isosceles()
    perpbis()
    anglebis()
    overlap()
    crossing()
