"""Figures for docs/05-university-core/06-linear-algebra/03-matrix-algebra-and-inverses.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/matrix-algebra-and-inverses.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "matrix-algebra-and-inverses"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)

F_SHAPE = np.array(
    [(0, 0), (1, 0), (1, 1.5), (2, 1.5), (2, 2.2), (1, 2.2), (1, 3), (3, 3), (3, 4), (0, 4)], float
)


def grid2d(ax, xlim, ylim):
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.axhline(0, color=fs.DARK, lw=1.0)
    ax.axvline(0, color=fs.DARK, lw=1.0)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(labelsize=9, length=0)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)


def draw(ax, pts, color, fill=0.25):
    ax.fill(pts[:, 0], pts[:, 1], color=color, alpha=fill, lw=0)
    closed = np.vstack([pts, pts[:1]])
    ax.plot(closed[:, 0], closed[:, 1], color=color, lw=2.0)


def inverse_and_singular():
    """An invertible matrix moves the F and the inverse moves it back; a singular one flattens it."""
    A = np.array([[2.0, 1.0], [1.0, 1.0]])
    S = np.array([[1.0, 2.0], [1.0, 2.0]])
    P = np.array([2.0, 0.0])
    Q = np.array([0.0, 1.0])
    fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.9))

    a = axs[0]
    grid2d(a, (-1, 5), (-1, 5))
    draw(a, F_SHAPE, fs.GREEN)
    a.plot(*P, "o", color=fs.BLUE, ms=7, zorder=5)
    a.plot(*Q, "o", color=fs.RED, ms=7, zorder=5)
    a.text(2.15, -0.15, "P = (2, 0)", color=fs.BLUE, fontsize=9.5, ha="left", va="top")
    a.text(0.15, 1.0, "Q", color=fs.RED, fontsize=9.5, ha="left", va="center", bbox=BOX)
    a.text(2.0, -0.85, "the shape", color=fs.DARK, fontsize=10.5, ha="center", va="center")

    b = axs[1]
    grid2d(b, (-1, 11), (-1, 9))
    draw(b, F_SHAPE @ A.T, fs.GREEN)
    b.plot(*(A @ P), "o", color=fs.BLUE, ms=7, zorder=5)
    b.plot(*(A @ Q), "o", color=fs.RED, ms=7, zorder=5)
    b.text(4.2, 1.9, "A P", color=fs.BLUE, fontsize=9.5, ha="left", va="top")
    b.text(1.25, 0.8, "A Q", color=fs.RED, fontsize=9.5, ha="left", va="top")
    b.text(5.0, -0.8, "after A: A⁻¹ moves it back", color=fs.DARK, fontsize=10.5, ha="center", va="center")

    c = axs[2]
    grid2d(c, (-1, 15), (-1, 15))
    SF = F_SHAPE @ S.T
    xs = np.array([0.0, 14.0])
    c.plot(xs, xs, color=fs.GREEN, lw=4.0, alpha=0.5)
    c.plot(*(S @ P), "o", color=fs.BLUE, ms=8, zorder=5)
    c.plot(*(S @ Q), "o", color=fs.RED, ms=5, zorder=6)
    c.text(2.5, 1.4, "SP = SQ = (2, 2)", color=fs.DARK, fontsize=9.5, ha="left", va="top")
    c.text(7.0, -2.0, "after S: flat, no way back", color=fs.DARK, fontsize=10.5, ha="center", va="center")
    c.set_ylim(-3.2, 15)
    _ = SF
    fig.subplots_adjust(wspace=0.12)
    fs.save(fig, FOLDER, f"{SLUG}-inverse")


def rotate_about_point():
    """Rotate a triangle by 90 degrees about (1, 1): translate, rotate, translate back."""
    tri = np.array([(2.0, 1.0), (4.0, 1.0), (2.0, 2.0)])
    c = np.array([1.0, 1.0])
    rot = np.array([[0.0, -1.0], [1.0, 0.0]])
    after = (tri - c) @ rot.T + c
    fig, ax = fs.figure(5.0, 4.4)
    grid2d(ax, (-0.8, 5.0), (-0.6, 5.0))
    draw(ax, tri, fs.GREEN)
    draw(ax, after, fs.BLUE)
    ax.plot(*c, "o", color=fs.RED, ms=7, zorder=5)
    ax.text(1.15, 0.6, "centre (1, 1)", color=fs.RED, fontsize=10, ha="left", va="top")
    ax.text(3.6, 0.55, "before", color=fs.GREEN, fontsize=10.5, ha="center", va="top")
    ax.text(0.5, 4.2, "after", color=fs.BLUE, fontsize=10.5, ha="center", va="bottom")
    for p, q in zip(tri, after):
        ax.annotate(
            "",
            xy=q,
            xytext=p,
            arrowprops=dict(arrowstyle="-|>", color=fs.GRAY, lw=1.0, connectionstyle="arc3,rad=0.28", shrinkA=3, shrinkB=3),
            zorder=3,
        )
    fs.save(fig, FOLDER, f"{SLUG}-rotate-about-point")


if __name__ == "__main__":
    inverse_and_singular()
    rotate_about_point()
