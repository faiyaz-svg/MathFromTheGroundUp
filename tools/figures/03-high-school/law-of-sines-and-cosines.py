"""Figures for docs/03-high-school/09-trigonometry/05-law-of-sines-and-cosines.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/law-of-sines-and-cosines.py
"""

import math
import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Arc, Polygon

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "law-of-sines-and-cosines"
DASH = (0, (4, 3))


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def right_mark(ax, p, u, v, s=0.22):
    p, u, v = (np.array(a, float) for a in (p, u, v))
    u, v = u / np.linalg.norm(u), v / np.linalg.norm(v)
    ax.plot(*zip(p + s * u, p + s * (u + v), p + s * v), color=fs.DARK, lw=1.1)


def tri(ax, pts, face=fs.GREEN, alpha=0.15):
    ax.add_patch(Polygon(pts, closed=True, facecolor=face, alpha=alpha, edgecolor="none"))
    ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor=fs.DARK, lw=2))


def altitude():
    """Triangle ABC with the altitude from C, for the proof of the law of sines."""
    fig, ax = fs.figure(5.4, 3.4)
    A, B, C = np.array([0.0, 0]), np.array([7.0, 0]), np.array([2.4, 3.3])
    F = np.array([C[0], 0.0])
    tri(ax, [A, B, C])
    ax.plot([C[0], F[0]], [C[1], F[1]], color=fs.RED, lw=1.8, ls=DASH)
    right_mark(ax, F, (-1, 0), (0, 1))
    for name, p, off, ha, va in (("$A$", A, (-0.2, -0.1), "right", "top"), ("$B$", B, (0.2, -0.1), "left", "top"),
                                 ("$C$", C, (0, 0.2), "center", "bottom")):
        ax.text(p[0] + off[0], p[1] + off[1], name, fontsize=13, ha=ha, va=va)
    ax.text(3.0, -0.2, "$c$", fontsize=12, ha="center", va="top")
    ax.text(0.95, 1.85, "$b$", fontsize=12, ha="right", va="center")
    ax.text(5.0, 1.85, "$a$", fontsize=12, ha="left", va="center")
    ax.text(C[0] - 0.12, 1.55, "$h$", fontsize=12, ha="right", va="center", color=fs.RED)
    ax.add_patch(Arc(A, 1.4, 1.4, theta1=0, theta2=math.degrees(math.atan2(C[1], C[0])), color=fs.BLUE, lw=1.2))
    ax.text(1.0, 0.25, "$A$", fontsize=10.5, color=fs.BLUE, ha="left", va="center")
    ax.add_patch(Arc(B, 1.4, 1.4, theta1=180 - math.degrees(math.atan2(C[1], B[0] - C[0])), theta2=180, color=fs.ORANGE, lw=1.2))
    ax.text(6.1, 0.27, "$B$", fontsize=10.5, color=fs.ORANGE, ha="right", va="center")
    ax.set_xlim(-0.8, 7.8)
    ax.set_ylim(-0.8, 4.0)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-altitude")


def cosine_law():
    """C at the origin, B on the x-axis, A at (b cos C, b sin C)."""
    fig, ax = fs.figure(5.6, 3.6)
    a, b = 5.0, 4.0
    Cang = math.radians(65)
    C, B, A = np.array([0.0, 0]), np.array([a, 0.0]), np.array([b * math.cos(Cang), b * math.sin(Cang)])
    tri(ax, [C, B, A])
    ax.plot([A[0], A[0]], [0, A[1]], color=fs.GRAY, lw=1.0, ls=DASH)
    right_mark(ax, (A[0], 0), (-1, 0), (0, 1), s=0.18)
    ax.add_patch(Arc(C, 1.4, 1.4, theta1=0, theta2=65, color=fs.BLUE, lw=1.3))
    ax.text(1.1, 0.35, "$C$", fontsize=11.5, color=fs.BLUE, ha="left", va="center")
    ax.text(-0.15, -0.1, "$C = (0, 0)$", fontsize=10.5, ha="right", va="top")
    ax.text(a + 0.12, -0.1, "$B = (a, 0)$", fontsize=10.5, ha="left", va="top")
    ax.text(A[0] - 0.1, A[1] + 0.15, r"$A = (b\cos C,\ b\sin C)$", fontsize=10.5, ha="right", va="bottom")
    ax.text(2.5, -0.2, "$a$", fontsize=12, ha="center", va="top")
    ax.text(0.65, 2.0, "$b$", fontsize=12, ha="right", va="center")
    ax.text(3.6, 2.0, "$c$", fontsize=12, ha="left", va="center", color=fs.RED)
    ax.plot([A[0], B[0]], [A[1], B[1]], color=fs.RED, lw=2.4)
    ax.set_xlim(-2.6, 7.6)
    ax.set_ylim(-0.8, 4.4)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-cosine-law")


def ambiguous():
    """A = 30 degrees, b = 10, a = 6: two triangles."""
    fig, ax = fs.figure(6.2, 3.2)
    A = np.array([0.0, 0])
    C = np.array([10 * math.cos(math.radians(30)), 5.0])
    r = 6.0
    dx = math.sqrt(r * r - C[1] ** 2)
    B1, B2 = np.array([C[0] - dx, 0.0]), np.array([C[0] + dx, 0.0])
    ax.plot([-0.5, 14.2], [0, 0], color=fs.DARK, lw=1.5)
    ax.plot([A[0], C[0]], [A[1], C[1]], color=fs.DARK, lw=2)
    ax.plot([C[0], B1[0]], [C[1], B1[1]], color=fs.GREEN, lw=2.4)
    ax.plot([C[0], B2[0]], [C[1], B2[1]], color=fs.ORANGE, lw=2.4)
    ax.plot([C[0], C[0]], [0, C[1]], color=fs.GRAY, lw=1.0, ls=DASH)
    t = np.linspace(math.radians(250), math.radians(335), 80)
    ax.plot(C[0] + r * np.cos(t), C[1] + r * np.sin(t), color=fs.GRAY, lw=1.0, ls=(0, (1, 2)))
    ax.add_patch(Arc(A, 2.4, 2.4, theta1=0, theta2=30, color=fs.BLUE, lw=1.2))
    ax.text(1.7, 0.4, r"$30^\circ$", fontsize=10.5, color=fs.BLUE, ha="left", va="center")
    for p, name, col in ((A, "$A$", fs.DARK), (C, "$C$", fs.DARK), (B1, "$B_1$", fs.GREEN), (B2, "$B_2$", fs.ORANGE)):
        ax.plot(*p, "o", color=col, ms=5, zorder=5)
    ax.text(-0.15, -0.2, "$A$", fontsize=12, ha="right", va="top")
    ax.text(C[0] - 0.1, C[1] + 0.2, "$C$", fontsize=12, ha="right", va="bottom")
    ax.text(B1[0], -0.2, "$B_1$", fontsize=12, ha="center", va="top", color=fs.GREEN)
    ax.text(B2[0], -0.2, "$B_2$", fontsize=12, ha="center", va="top", color=fs.ORANGE)
    ax.text(4.0, 3.0, "$b = 10$", fontsize=11, ha="right", va="center", rotation=30, rotation_mode="anchor")
    ax.text(C[0] + 0.15, 1.3, "$h = 5$", fontsize=10.5, ha="left", va="center", color=fs.GRAY)
    ax.text(7.0, 2.4, "$a = 6$", fontsize=11, ha="right", va="center", color=fs.GREEN)
    ax.text(11.5, 2.4, "$a = 6$", fontsize=11, ha="left", va="center", color=fs.ORANGE)
    ax.set_xlim(-1.2, 14.6)
    ax.set_ylim(-1.1, 6.4)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-ambiguous")


if __name__ == "__main__":
    altitude()
    cosine_law()
    ambiguous()
