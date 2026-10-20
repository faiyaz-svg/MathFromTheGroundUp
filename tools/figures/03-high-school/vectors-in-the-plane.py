"""Figures for docs/03-high-school/10-vectors-and-matrices/01-vectors-in-the-plane.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/vectors-in-the-plane.py
"""

import math
import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Arc

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "vectors-in-the-plane"
DASH = (0, (4, 3))


def arrow(ax, tail, tip, color, lw=2.2, ls="-", z=5):
    ax.annotate("", xy=tip, xytext=tail, zorder=z,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, ls=ls,
                                shrinkA=0, shrinkB=0, mutation_scale=14))


def grid(ax, xmin, xmax, ymin, ymax, ticks=True):
    ax.set_xlim(xmin - 0.4, xmax + 0.4)
    ax.set_ylim(ymin - 0.4, ymax + 0.4)
    ax.set_xticks([t for t in range(xmin, xmax + 1) if t != 0] if ticks else [])
    ax.set_yticks([t for t in range(ymin, ymax + 1) if t != 0] if ticks else [])
    ax.tick_params(labelsize=9)
    ax.grid(True)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")


def blank(ax):
    ax.set_aspect("equal")
    ax.axis("off")


def label(ax, x, y, text, color=fs.DARK, ha="center", va="center", size=11, **kw):
    ax.text(x, y, text, color=color, ha=ha, va=va, fontsize=size, zorder=8, **kw)


def point(ax, p, color=fs.DARK):
    ax.plot(*p, "o", color=color, ms=5, zorder=7)


def right_mark(ax, p, u, v, s=0.22, color=fs.DARK):
    p, u, v = (np.array(a, float) for a in (p, u, v))
    u, v = u / np.linalg.norm(u), v / np.linalg.norm(v)
    ax.plot(*zip(p + s * u, p + s * (u + v), p + s * v), color=color, lw=1.1, zorder=6)


def displacement():
    fig, ax = fs.figure(5.2, 3.9)
    grid(ax, 0, 8, 0, 6)
    ax.plot([3, 3], [0, 4], color=fs.GRAY, lw=1.3, ls=DASH, zorder=3)
    ax.plot([0, 3], [0, 0], color=fs.GRAY, lw=1.3, ls=DASH, zorder=3)
    arrow(ax, (0, 0), (3, 4), fs.GREEN)
    arrow(ax, (4, 1), (7, 5), fs.BLUE)
    point(ax, (0, 0))
    label(ax, 1.5, 0.3, "3 right", fs.GRAY)
    label(ax, 3.55, 2.0, "4 up", fs.GRAY, ha="left")
    label(ax, 1.05, 2.45, "length 5", fs.GREEN, ha="right", rotation=53.13)
    label(ax, 5.15, 3.35, "the same vector,\nstarted at (4, 1)", fs.BLUE, ha="left")
    label(ax, 0.1, 5.5, r"$\mathbf{v} = (3, 4)$", fs.GREEN, ha="left", size=12)
    fs.save(fig, FOLDER, f"{SLUG}-displacement")


def addition():
    fig, ax = fs.figure(5.2, 3.7)
    grid(ax, 0, 5, 0, 4)
    u, v = (3, 1), (1, 2)
    s = (4, 3)
    ax.plot([v[0], s[0]], [v[1], s[1]], color=fs.BLUE, lw=1.3, ls=DASH, zorder=3)
    ax.plot([0, v[0]], [0, v[1]], color=fs.BLUE, lw=1.3, ls=DASH, zorder=3)
    ax.plot([u[0], s[0]], [u[1], s[1]], color=fs.BLUE, lw=1.3, ls=DASH, zorder=3)
    arrow(ax, (0, 0), u, fs.GREEN)
    arrow(ax, u, s, fs.BLUE)
    arrow(ax, (0, 0), s, fs.RED, lw=2.6)
    point(ax, (0, 0))
    label(ax, 2.2, 0.25, r"$\mathbf{u} = (3, 1)$", fs.GREEN)
    label(ax, 3.75, 1.9, r"$\mathbf{v} = (1, 2)$", fs.BLUE, ha="left")
    label(ax, 3.9, 3.5, r"$\mathbf{u} + \mathbf{v} = (4, 3)$", fs.RED, ha="right")
    fs.save(fig, FOLDER, f"{SLUG}-addition")


def scalar_multiples():
    fig, ax = fs.figure(5.0, 3.6)
    blank(ax)
    ax.set_xlim(-0.6, 5.8)
    ax.set_ylim(-2.2, 5.6)
    arrow(ax, (0, 3.0), (4, 5.0 - 0.0), fs.ORANGE)
    arrow(ax, (0, 1.6), (2, 2.6), fs.GREEN)
    arrow(ax, (0, 0.6), (1, 1.1), fs.BLUE)
    arrow(ax, (4, -0.2), (2, -1.2), fs.RED)
    label(ax, 4.15, 4.95, r"$2\mathbf{v}$", fs.ORANGE, ha="left")
    label(ax, 2.15, 2.5, r"$\mathbf{v} = (2, 1)$", fs.GREEN, ha="left")
    label(ax, 1.15, 1.0, r"$\frac{1}{2}\mathbf{v}$", fs.BLUE, ha="left")
    label(ax, 4.15, -0.3, r"$-\mathbf{v}$", fs.RED, ha="left")
    fs.save(fig, FOLDER, f"{SLUG}-scalar-multiples")


def subtraction():
    fig, ax = fs.figure(5.2, 3.6)
    grid(ax, 0, 5, -2, 4)
    u, v = (4, 1), (1, 3)
    arrow(ax, (0, 0), u, fs.GREEN)
    arrow(ax, (0, 0), v, fs.BLUE)
    arrow(ax, v, u, fs.RED, lw=2.6)
    point(ax, (0, 0))
    label(ax, 2.5, 0.28, r"$\mathbf{u}$", fs.GREEN)
    label(ax, 0.5, 2.3, r"$\mathbf{v}$", fs.BLUE)
    label(ax, 4.6, 3.3, r"$\mathbf{u} - \mathbf{v} = (3, -2)$", fs.RED, ha="right")
    fs.save(fig, FOLDER, f"{SLUG}-subtraction")


def ij():
    fig, ax = fs.figure(4.8, 3.4)
    grid(ax, 0, 4, 0, 3)
    arrow(ax, (0, 0), (3, 0), fs.GREEN)
    arrow(ax, (3, 0), (3, 2), fs.BLUE)
    arrow(ax, (0, 0), (3, 2), fs.RED, lw=2.6)
    arrow(ax, (0, 0), (1, 0), fs.DARK, lw=3.0, z=6)
    arrow(ax, (0, 0), (0, 1), fs.DARK, lw=3.0, z=6)
    label(ax, 0.5, -0.3, r"$\mathbf{i}$", fs.DARK)
    label(ax, -0.28, 0.5, r"$\mathbf{j}$", fs.DARK)
    label(ax, 2.0, 0.28, r"$3\mathbf{i}$", fs.GREEN)
    label(ax, 3.3, 1.0, r"$2\mathbf{j}$", fs.BLUE, ha="left")
    label(ax, 1.4, 1.5, r"$\mathbf{v} = 3\mathbf{i} + 2\mathbf{j}$", fs.RED, ha="right")
    fs.save(fig, FOLDER, f"{SLUG}-ij")


def angle_arc(ax, r, start, end, color=fs.DARK):
    ax.add_patch(Arc((0, 0), 2 * r, 2 * r, theta1=start, theta2=end, color=color, lw=1.3, zorder=4))


def direction():
    fig, (a1, a2) = fs.plt.subplots(1, 2, figsize=(8.6, 3.5))
    # Left: a vector in the first quadrant, with its components.
    grid(a1, 0, 5, 0, 4)
    v = (4, 3)
    a1.plot([4, 4], [0, 3], color=fs.GRAY, lw=1.3, ls=DASH, zorder=3)
    arrow(a1, (0, 0), v, fs.GREEN)
    angle_arc(a1, 1.0, 0, 36.87)
    label(a1, 1.45, 0.3, r"$\theta$", fs.DARK)
    label(a1, 2.7, 0.3,r"$\|\mathbf{v}\|\cos\theta = 4$", fs.GRAY, size=10)
    label(a1, 4.2, 1.5, r"$\|\mathbf{v}\|\sin\theta = 3$", fs.GRAY, ha="left", size=10)
    label(a1, 1.7, 2.35, r"$\|\mathbf{v}\| = 5$", fs.GREEN, ha="right", rotation=36.87)
    # Right: arctan of the ratio lands in the wrong quadrant.
    grid(a2, -4, 4, -4, 4)
    arrow(a2, (0, 0), (-3, -3), fs.RED)
    arrow(a2, (0, 0), (3, 3), fs.GRAY, lw=1.6, ls=DASH, z=4)
    angle_arc(a2, 1.1, 0, 225, fs.RED)
    label(a2, 2.2, 3.55, r"$\arctan(1) = 45^\circ$", fs.GRAY, ha="center", size=10)
    label(a2, -1.0, -3.55, r"$\mathbf{v} = (-3, -3)$", fs.RED, ha="center", size=10)
    label(a2, 1.7, -0.9,r"$225^\circ$", fs.RED, size=10)
    a2.set_xticks([])
    a2.set_yticks([])
    fs.plt.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-direction")


def dot_triangle():
    fig, ax = fs.figure(5.0, 3.6)
    blank(ax)
    u, v = np.array([5.0, 1.0]), np.array([2.0, 4.0])
    th = math.degrees(math.acos(u @ v / (np.linalg.norm(u) * np.linalg.norm(v))))
    ax.set_xlim(-0.8, 5.9)
    ax.set_ylim(-0.7, 4.6)
    arrow(ax, (0, 0), tuple(u), fs.GREEN)
    arrow(ax, (0, 0), tuple(v), fs.BLUE)
    arrow(ax, tuple(v), tuple(u), fs.RED, lw=2.6)
    point(ax, (0, 0))
    ang1 = math.degrees(math.atan2(1, 5))
    ang2 = math.degrees(math.atan2(4, 2))
    ax.add_patch(Arc((0, 0), 2.0, 2.0, theta1=ang1, theta2=ang2, color=fs.DARK, lw=1.3, zorder=4))
    label(ax, 1.55, 0.9, r"$\theta$", fs.DARK)
    label(ax, 2.8, -0.3, r"$\|\mathbf{u}\|$", fs.GREEN)
    label(ax, 0.5, 2.3, r"$\|\mathbf{v}\|$", fs.BLUE, ha="right")
    label(ax, 4.2, 3.0, r"$\|\mathbf{u} - \mathbf{v}\|$", fs.RED, ha="left")
    print("theta", th)
    fs.save(fig, FOLDER, f"{SLUG}-dot-triangle")


def dot_sign():
    plt = fs.plt
    fig, axes = plt.subplots(1, 3, figsize=(8.8, 2.7))
    cases = [((2, 2), "acute angle", r"$\mathbf{u}\cdot\mathbf{v} = 6 > 0$"),
             ((0, 2), "right angle", r"$\mathbf{u}\cdot\mathbf{v} = 0$"),
             ((-2, 2), "obtuse angle", r"$\mathbf{u}\cdot\mathbf{v} = -6 < 0$")]
    for ax, (v, name, dot) in zip(axes, cases):
        blank(ax)
        ax.set_xlim(-2.8, 3.8)
        ax.set_ylim(-1.3, 3.3)
        arrow(ax, (0, 0), (3, 0), fs.GREEN)
        arrow(ax, (0, 0), v, fs.BLUE)
        point(ax, (0, 0))
        a2 = math.degrees(math.atan2(v[1], v[0]))
        ax.add_patch(Arc((0, 0), 1.2, 1.2, theta1=0, theta2=a2, color=fs.DARK, lw=1.2, zorder=4))
        label(ax, 3.0, -0.3, r"$\mathbf{u} = (3, 0)$", fs.GREEN, ha="right", size=10)
        label(ax, v[0] * 0.5 + (0.45 if v[0] >= 0 else -0.45), v[1] * 0.5 + 0.2,
              r"$\mathbf{v}$", fs.BLUE, size=11)
        label(ax, 0.5, -0.95, name, fs.DARK, size=10, ha="left")
        label(ax, 0.5, -1.25 - 0.0, "", fs.DARK)
        ax.set_title(dot, fontsize=10, color=fs.DARK, pad=2)
    fs.plt.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-dot-sign")


def wind():
    fig, ax = fs.figure(4.2, 4.6)
    blank(ax)
    ax.set_xlim(-2.4, 8.2)
    ax.set_ylim(-1.2, 27)
    # 1 unit = 10 km/h
    arrow(ax, (0, 0), (0, 24), fs.GREEN)
    arrow(ax, (0, 24), (5, 24), fs.BLUE)
    arrow(ax, (0, 0), (5, 24), fs.RED, lw=2.6)
    point(ax, (0, 0))
    ax.plot([0, 0], [24, 26.2], color=fs.GRAY, lw=1.1, ls=DASH, zorder=3)
    label(ax, -0.3, 12, "plane, 240 km/h\nheading north", fs.GREEN, ha="right")
    label(ax, 2.5, 25.0, "wind, 50 km/h", fs.BLUE, va="bottom")
    label(ax, 3.3, 8.5, "ground velocity\n(50, 240)", fs.RED, ha="left")
    ax.add_patch(Arc((0, 0), 36, 36, theta1=math.degrees(math.atan2(24, 5)), theta2=90,
                     color=fs.DARK, lw=1.2, zorder=4))
    label(ax, 1.7, 19.7, r"$11.8^\circ$", fs.DARK, size=10)
    fs.save(fig, FOLDER, f"{SLUG}-wind")


if __name__ == "__main__":
    displacement()
    addition()
    scalar_multiples()
    subtraction()
    ij()
    direction()
    dot_triangle()
    dot_sign()
    wind()
