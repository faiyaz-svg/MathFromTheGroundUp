"""Figures for docs/02-middle-school/06-geometry/04-pythagorean-theorem.md."""

import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Polygon

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "02-middle-school"
SLUG = "pythagorean-theorem"
DASH = (0, (4, 3))


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def shape(ax, pts, face="none", alpha=0.25, edge=fs.DARK, lw=1.8, ls="-"):
    if face != "none":
        ax.add_patch(Polygon(pts, closed=True, facecolor=face, alpha=alpha, edgecolor="none"))
    ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor=edge, lw=lw, ls=ls))


def right_mark(ax, p, u, v, s=0.2, color=fs.DARK):
    p, u, v = (np.array(a, float) for a in (p, u, v))
    u, v = u / np.linalg.norm(u), v / np.linalg.norm(v)
    ax.plot(*zip(p + s * u, p + s * (u + v), p + s * v), color=color, lw=1.2)


def label(ax, p, q, text, off=0.18, color=fs.DARK, size=13):
    """Put text beside the middle of segment pq, on its left as you go from p to q."""
    p, q = np.array(p, float), np.array(q, float)
    m = (p + q) / 2
    d = (q - p) / np.linalg.norm(q - p)
    n = np.array([-d[1], d[0]])
    ax.text(*(m + off * n), text, ha="center", va="center", fontsize=size, color=color)


def squares_on_sides():
    fig, ax = fs.figure(4.2, 4.2)
    a, b = 1.8, 2.4  # legs: a up the left side, b along the bottom
    C, B, A = np.array([0, 0.0]), np.array([b, 0.0]), np.array([0, a])
    shape(ax, [C, B, A], face=fs.GREEN, alpha=0.3, lw=2)
    right_mark(ax, C, (1, 0), (0, 1))
    shape(ax, [C, B, B + (0, -b), C + (0, -b)], face=fs.BLUE, alpha=0.15, lw=1.3)
    shape(ax, [C, A, A + (-a, 0), C + (-a, 0)], face=fs.ORANGE, alpha=0.18, lw=1.3)
    d = (B - A) / np.linalg.norm(B - A)
    n = np.array([d[1], -d[0]]) * -1  # outward from the triangle
    c = np.linalg.norm(B - A)
    shape(ax, [A, B, B + c * np.array([d[1], -d[0]]) * -1, A + c * np.array([d[1], -d[0]]) * -1],
          face=fs.RED, alpha=0.12, lw=1.3)
    ax.text(b / 2, -b / 2, "$b^2$", ha="center", va="center", fontsize=14, color=fs.BLUE)
    ax.text(-a / 2, a / 2, "$a^2$", ha="center", va="center", fontsize=14, color=fs.ORANGE)
    mid = (A + B) / 2 + n * c / 2
    ax.text(*mid, "$c^2$", ha="center", va="center", fontsize=14, color=fs.RED)
    # Each side's length, written on the outer edge of its square.
    ax.text(-a - 0.12, a / 2, "$a$", ha="right", va="center", fontsize=13)
    ax.text(b / 2, -b - 0.12, "$b$", ha="center", va="top", fontsize=13)
    out = -np.array([d[1], -d[0]])
    label(ax, A + c * out, B + c * out, "$c$", off=0.2)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-squares")


def proof():
    fig, (ax1, ax2) = fs.plt.subplots(1, 2, figsize=(6.4, 3.2))
    a, b = 1.0, 2.0
    s = a + b
    P1, P2, P3, P4 = (a, 0), (s, a), (b, s), (0, b)
    corners = [(0, 0), (s, 0), (s, s), (0, s)]
    tris = [[(0, 0), P1, P4], [(s, 0), P2, P1], [(s, s), P3, P2], [(0, s), P4, P3]]
    shape(ax1, [P1, P2, P3, P4], face=fs.RED, alpha=0.14, lw=1.4)
    for t in tris:
        shape(ax1, t, face=fs.GREEN, alpha=0.3, lw=1.4)
    shape(ax1, corners, lw=2)
    ax1.text(s / 2, s / 2, "$c^2$", ha="center", va="center", fontsize=15, color=fs.RED)
    # Side labels around the outside: bottom a then b, right a then b, top b then a, left b then a.
    for (p, q, t) in [((0, 0), (a, 0), "$a$"), ((a, 0), (s, 0), "$b$"),
                      ((s, 0), (s, a), "$a$"), ((s, a), (s, s), "$b$"),
                      ((s, s), (b, s), "$a$"), ((b, s), (0, s), "$b$"),
                      ((0, s), (0, b), "$a$"), ((0, b), (0, 0), "$b$")]:
        label(ax1, p, q, t, off=-0.17)
    label(ax1, P1, P2, "$c$", off=0.2, color=fs.RED)
    ax1.set_xlim(-0.4, s + 0.4)
    ax1.set_ylim(-0.4, s + 0.4)
    blank(ax1)

    shape(ax2, [(0, 0), (a, 0), (a, a), (0, a)], face=fs.ORANGE, alpha=0.25, lw=1.4)
    shape(ax2, [(a, a), (s, a), (s, s), (a, s)], face=fs.BLUE, alpha=0.18, lw=1.4)
    for t in ([(a, 0), (s, 0), (s, a)], [(a, 0), (s, a), (a, a)],
              [(0, a), (a, a), (a, s)], [(0, a), (a, s), (0, s)]):
        shape(ax2, t, face=fs.GREEN, alpha=0.3, lw=1.4)
    shape(ax2, [(0, 0), (s, 0), (s, s), (0, s)], lw=2)
    ax2.text(a / 2, a / 2, "$a^2$", ha="center", va="center", fontsize=14, color=fs.ORANGE)
    ax2.text(a + b / 2, a + b / 2, "$b^2$", ha="center", va="center", fontsize=15, color=fs.BLUE)
    for (p, q, t) in [((0, 0), (a, 0), "$a$"), ((a, 0), (s, 0), "$b$"),
                      ((s, 0), (s, a), "$a$"), ((s, a), (s, s), "$b$"),
                      ((s, s), (a, s), "$b$"), ((a, s), (0, s), "$a$"),
                      ((0, s), (0, a), "$b$"), ((0, a), (0, 0), "$a$")]:
        label(ax2, p, q, t, off=-0.17)
    ax2.set_xlim(-0.4, s + 0.4)
    ax2.set_ylim(-0.4, s + 0.4)
    blank(ax2)
    fs.save(fig, FOLDER, f"{SLUG}-proof")


def distance():
    fig, ax = fs.figure(4.2, 3.4)
    x1, y1, x2, y2 = 1, 1, 5, 4
    ax.set_xlim(-0.3, 7.4)
    ax.set_ylim(-0.3, 5.3)
    ax.set_xticks(range(1, 8))
    ax.set_yticks(range(1, 6))
    ax.grid(True)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.plot([x1, x2], [y1, y1], color=fs.BLUE, lw=2)
    ax.plot([x2, x2], [y1, y2], color=fs.ORANGE, lw=2)
    ax.plot([x1, x2], [y1, y2], color=fs.GREEN, lw=2.5)
    right_mark(ax, (x2, y1), (-1, 0), (0, 1), s=0.25)
    for (x, y, t, ha, va) in ((x1, y1, "$(1, 1)$", "right", "bottom"), (x2, y2, "$(5, 4)$", "left", "bottom")):
        ax.plot(x, y, "o", color=fs.DARK, ms=6, zorder=5)
        ax.text(x + (0.12 if ha == "left" else -0.12), y + 0.1, t, ha=ha, va=va, fontsize=12)
    ax.text((x1 + x2) / 2, y1 - 0.12, "$5 - 1 = 4$", color=fs.BLUE, ha="center", va="top", fontsize=12)
    ax.text(x2 + 0.15, (y1 + y2) / 2, "$4 - 1 = 3$", color=fs.ORANGE, ha="left", va="center", fontsize=12)
    ax.text((x1 + x2) / 2 - 0.2, (y1 + y2) / 2 + 0.2, "$d$", color=fs.GREEN, ha="right", va="bottom", fontsize=14)
    fs.save(fig, FOLDER, f"{SLUG}-distance")


def space_diagonal():
    fig, ax = fs.figure(4.2, 3.0)
    K, ANG = 0.55, np.radians(35)

    def P(x, y, z):
        return np.array([x + K * np.cos(ANG) * y, z + K * np.sin(ANG) * y])

    l, w, h = 3.0, 2.0, 1.6
    V = {(i, j, k): P(i * l, j * w, k * h) for i in (0, 1) for j in (0, 1) for k in (0, 1)}
    edges = [((0, 0, 0), (1, 0, 0)), ((1, 0, 0), (1, 1, 0)), ((1, 1, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 0)),
             ((0, 0, 1), (1, 0, 1)), ((1, 0, 1), (1, 1, 1)), ((1, 1, 1), (0, 1, 1)), ((0, 1, 1), (0, 0, 1)),
             ((0, 0, 0), (0, 0, 1)), ((1, 0, 0), (1, 0, 1)), ((1, 1, 0), (1, 1, 1)), ((0, 1, 0), (0, 1, 1))]
    hidden = {((1, 1, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 0)), ((0, 1, 0), (0, 1, 1))}
    for a_, b_ in edges:
        hid = (a_, b_) in hidden
        ax.plot(*zip(V[a_], V[b_]), color=fs.DARK, lw=1.2 if hid else 1.8, ls=DASH if hid else "-")
    A, F, G = V[(0, 0, 0)], V[(1, 1, 0)], V[(1, 1, 1)]
    ax.plot(*zip(A, F), color=fs.BLUE, lw=2, ls=(0, (6, 2)))
    ax.plot(*zip(A, G), color=fs.RED, lw=2.4)
    ax.plot(*zip(F, G), color=fs.DARK, lw=2)
    ax.text(*(V[(0, 0, 0)] + V[(1, 0, 0)]) / 2 + np.array([0, -0.12]), "$l$", ha="center", va="top", fontsize=13)
    ax.text(*(V[(1, 0, 0)] + V[(1, 1, 0)]) / 2 + np.array([0.12, -0.05]), "$w$", ha="left", va="top", fontsize=13)
    ax.text(*(V[(1, 1, 0)] + V[(1, 1, 1)]) / 2 + np.array([0.12, 0]), "$h$", ha="left", va="center", fontsize=13)
    m = A + 0.55 * (F - A)
    ax.text(m[0] + 0.05, m[1] - 0.12, "floor diagonal", color=fs.BLUE, ha="left", va="top", fontsize=10,
            rotation=np.degrees(np.arctan2(*(F - A)[::-1])), rotation_mode="anchor")
    m = (A + G) / 2
    ax.text(m[0] - 0.15, m[1] + 0.1, "$d$", color=fs.RED, ha="right", va="bottom", fontsize=14)
    right_mark(ax, F, A - F, G - F, s=0.18)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-space-diagonal")


def ladder():
    fig, ax = fs.figure(3.2, 3.6)
    base, top = 1.5, np.sqrt(36 - 1.5**2)
    ax.plot([-0.3, 2.6], [0, 0], color=fs.DARK, lw=2)
    ax.plot([0, 0], [0, 6.5], color=fs.DARK, lw=3)
    ax.plot([base, 0], [0, top], color=fs.GREEN, lw=3)
    right_mark(ax, (0, 0), (1, 0), (0, 1), s=0.3)
    ax.text(base / 2, -0.15, "1.5 m", ha="center", va="top", fontsize=12)
    ax.text(0.95, top / 2 + 0.3, "6 m", color=fs.GREEN, ha="left", va="center", fontsize=12)
    ax.text(-0.4, top / 2, "?", ha="right", va="center", fontsize=14)
    ax.plot([-0.35, -0.35], [0, top], color=fs.DARK, lw=1)
    blank(ax)
    fs.save(fig, FOLDER, f"{SLUG}-ladder")


squares_on_sides()
proof()
distance()
space_diagonal()
ladder()
