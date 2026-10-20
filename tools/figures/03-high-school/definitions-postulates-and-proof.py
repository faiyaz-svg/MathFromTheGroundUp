"""Figures for docs/03-high-school/08-geometry-and-proof/01-definitions-postulates-and-proof.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/definitions-postulates-and-proof.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import figstyle as fs  # noqa: E402
import geomhelp as g  # noqa: E402

SLUG = "definitions-postulates-and-proof"


def polar(r, deg, c=(0, 0)):
    return (c[0] + r * math.cos(math.radians(deg)), c[1] + r * math.sin(math.radians(deg)))


def vertical():
    """Two lines AB and CD crossing at E, with the four angles numbered."""
    fig, ax = g.canvas(5.0, 3.9, (-2.9, 2.9), (-2.3, 2.3))
    E = (0, 0)
    A, B, C, D = polar(2.6, 200), polar(2.6, 20), polar(2.1, 70), polar(2.1, 250)
    g.seg(ax, A, B)
    g.seg(ax, C, D)
    for p1, p2, col in [(A, C, fs.GREEN), (C, B, fs.BLUE), (B, D, fs.GREEN), (D, A, fs.BLUE)]:
        g.shade_angle(ax, E, p1, p2, 1.25, col)
    g.arc(ax, E, A, C, 0.55, color=fs.GREEN, text="1", text_r=0.95)
    g.arc(ax, E, C, B, 0.42, color=fs.BLUE, text="2", text_r=0.85)
    g.arc(ax, E, B, D, 0.55, color=fs.GREEN, text="3", text_r=0.95)
    g.arc(ax, E, D, A, 0.42, color=fs.BLUE, text="4", text_r=0.85)
    for p, t, o in [(A, "A", (-0.22, -0.12)), (B, "B", (0.22, 0.12)), (C, "C", (0.1, 0.2)), (D, "D", (-0.1, -0.2))]:
        g.dot(ax, p)
        g.name(ax, p, t, o)
    g.dot(ax, E)
    g.name(ax, E, "E", (0.0, -0.2), box=True)
    g.save(fig, SLUG, "vertical")


def bisectors():
    """The bisectors of a linear pair meet at a right angle."""
    fig, ax = g.canvas(5.0, 3.5, (-2.9, 2.9), (-0.5, 2.9))
    E = (0, 0)
    A, B = (-2.6, 0), (2.6, 0)
    C = polar(2.4, 65)
    F = polar(2.4, 180 - 57.5)
    G = polar(2.4, 32.5)
    g.seg(ax, A, B)
    g.seg(ax, E, C)
    g.seg(ax, E, F, fs.GREEN)
    g.seg(ax, E, G, fs.BLUE)
    g.arc(ax, E, A, F, 1.0, 1, fs.GREEN, text="a", text_r=0.7, size=12)
    g.arc(ax, E, F, C, 1.0, 1, fs.GREEN, text="a", text_r=0.7, size=12)
    g.arc(ax, E, C, G, 1.3, 1, fs.BLUE, text="b", text_r=1.0, size=12)
    g.arc(ax, E, G, B, 1.3, 1, fs.BLUE, text="b", text_r=1.0, size=12)
    g.right_angle(ax, E, F, G, 0.3, fs.RED)
    g.label(ax, polar(0.55, 77), "?", color=fs.RED, size=12, box=False)
    for p, t, o in [(A, "A", (-0.2, 0.0)), (B, "B", (0.2, 0.0)), (C, "C", (0.12, 0.18)),
                    (F, "F", (-0.2, 0.1)), (G, "G", (0.2, 0.08)), (E, "E", (0.0, -0.25))]:
        g.dot(ax, p)
        g.name(ax, p, t, o)
    g.save(fig, SLUG, "bisectors")


if __name__ == "__main__":
    vertical()
    bisectors()
