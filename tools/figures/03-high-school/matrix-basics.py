"""Figures for docs/03-high-school/10-vectors-and-matrices/02-matrix-basics.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/matrix-basics.py
"""

import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Polygon

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "matrix-basics"
DASH = (0, (4, 3))

# An L shape, so that a turn or a flip is visible (a square would look the same).
L = np.array([(0, 0), (2, 0), (2, 1), (1, 1), (1, 3), (0, 3)], float)

ROT = np.array([[0, -1], [1, 0]], float)      # rotate 90 degrees counterclockwise
FLIPX = np.array([[1, 0], [0, -1]], float)    # reflect in the x-axis
STRETCH = np.array([[2, 0], [0, 1]], float)
SWAP = np.array([[0, 1], [1, 0]], float)      # reflect in y = x
SHEAR = np.array([[1, 1], [0, 1]], float)


def apply(m, pts):
    return pts @ m.T


def arrow(ax, tail, tip, color, lw=2.2, z=6):
    ax.annotate("", xy=tip, xytext=tail, zorder=z,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=13))


def grid(ax, xmin, xmax, ymin, ymax):
    ax.set_xlim(xmin - 0.4, xmax + 0.4)
    ax.set_ylim(ymin - 0.4, ymax + 0.4)
    ax.set_xticks([t for t in range(xmin, xmax + 1) if t != 0])
    ax.set_yticks([t for t in range(ymin, ymax + 1) if t != 0])
    ax.tick_params(labelsize=8)
    ax.grid(True)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")


def shape(ax, pts, color, alpha=0.28, ls="-", z=3):
    ax.add_patch(Polygon(pts, closed=True, facecolor=color, alpha=alpha, edgecolor="none", zorder=z))
    ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor=color, lw=1.8, ls=ls, zorder=z + 1))


def text(ax, x, y, s, color=fs.DARK, ha="center", va="center", size=10):
    ax.text(x, y, s, color=color, ha=ha, va=va, fontsize=size, zorder=8)


def gallery():
    fig, axes = fs.plt.subplots(2, 2, figsize=(7.4, 4.9))
    panels = [
        (ROT, "rotate $90^\\circ$", (-3.2, 3.6), (-2.2, 2.3)),
        (STRETCH, "stretch $x$ by 2", (3.0, 3.6), (1.0, 3.2)),
        (SWAP, "reflect in $y = x$", (3.0, 3.6), (1.0, 3.2)),
        (SHEAR, "shear", (3.0, 3.6), (1.0, 3.2)),
    ]
    for ax, (m, name, _, _) in zip(axes.flat, panels):
        grid(ax, -4, 5, -1, 4)
        shape(ax, L, fs.GREEN)
        shape(ax, apply(m, L), fs.BLUE)
        text(ax, 3.2, 4.0, name, fs.DARK, size=11)
    # Labels for the first panel only, next to the shapes.
    ax0 = axes[0, 0]
    text(ax0, 0.5, 3.5, "L", fs.GREEN, size=11)
    text(ax0, -1.4, 0.4, "image", fs.BLUE, size=11)
    fs.plt.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-gallery")


def columns():
    fig, ax = fs.figure(4.8, 3.9)
    grid(ax, -1, 4, -1, 4)
    A = np.array([[2, 1], [1, 2]], float)
    square = np.array([(0, 0), (1, 0), (1, 1), (0, 1)], float)
    shape(ax, square, fs.GREEN, alpha=0.3)
    shape(ax, apply(A, square), fs.BLUE, alpha=0.18)
    arrow(ax, (0, 0), (1, 0), fs.GREEN, lw=2.6)
    arrow(ax, (0, 0), (0, 1), fs.ORANGE, lw=2.6)
    arrow(ax, (0, 0), (2, 1), fs.GREEN, lw=2.6)
    arrow(ax, (0, 0), (1, 2), fs.ORANGE, lw=2.6)
    text(ax, 0.55, -0.35, r"$\mathbf{i}$", fs.GREEN, size=11)
    text(ax, -0.3, 0.55, r"$\mathbf{j}$", fs.ORANGE, size=11)
    text(ax, 2.95, 0.45, "$A\\mathbf{i} = (2, 1)$", fs.GREEN, ha="right", size=10)
    text(ax, 0.2, 2.35, "$A\\mathbf{j} = (1, 2)$", fs.ORANGE, ha="right", size=10)
    text(ax, 1.5, 1.5, "area 3", fs.BLUE, size=11)
    fs.save(fig, FOLDER, f"{SLUG}-columns")


def order():
    fig, axes = fs.plt.subplots(1, 2, figsize=(8.4, 4.0))
    cases = [
        (FLIPX, ROT, "reflect, then rotate", "RF"),
        (ROT, FLIPX, "rotate, then reflect", "FR"),
    ]
    for ax, (first, second, name, _) in zip(axes, cases):
        grid(ax, -4, 4, -4, 4)
        mid = apply(first, L)
        end = apply(second, mid)
        shape(ax, L, fs.GREEN)
        shape(ax, mid, fs.ORANGE, alpha=0.12, ls=DASH)
        shape(ax, end, fs.BLUE, alpha=0.3)
        text(ax, 0.5, 3.55, "start", fs.GREEN, size=9)
        text(ax, -2.0, 3.7, name, fs.DARK, size=10)
    text(axes[0], 3.1, 1.6, "end", fs.BLUE, size=9, ha="left")
    text(axes[1], -1.5, -2.5, "end", fs.BLUE, size=9)
    text(axes[0], 2.6, -1.8, "after step 1", fs.ORANGE, size=9)
    text(axes[1], -2.0, 2.5, "after step 1", fs.ORANGE, size=9)
    fs.plt.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-order")


if __name__ == "__main__":
    gallery()
    columns()
    order()
