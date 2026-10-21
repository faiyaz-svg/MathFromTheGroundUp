"""Figures for docs/05-university-core/06-linear-algebra/06-determinants.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/determinants.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "determinants"

F = np.array(
    [(0.2, 0.1), (0.4, 0.1), (0.4, 0.4), (0.7, 0.4), (0.7, 0.55), (0.4, 0.55), (0.4, 0.7), (0.85, 0.7), (0.85, 0.9), (0.2, 0.9)]
).T
SQUARE = np.array([(0, 0), (1, 0), (1, 1), (0, 1)]).T


def signed_area():
    """The unit square under two matrices with determinants +5 and -5."""
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.3))
    items = [
        ([[3, 1], [1, 2]], "$\\det = 3 \\cdot 2 - 1 \\cdot 1 = 5$", (3.0, 0.75), (0.4, 2.35)),
        ([[1, 3], [2, 1]], "$\\det = 1 \\cdot 1 - 3 \\cdot 2 = -5$", (0.6, 2.35), (3.1, 1.0)),
    ]
    for ax, (M, label, ipos, jpos) in zip(axes, items):
        M = np.array(M, dtype=float)
        ax.set_aspect("equal")
        ax.grid(True)
        ax.set_axisbelow(True)
        ax.tick_params(labelsize=8, length=2)
        ax.axhline(0, color=fs.DARK, lw=0.8)
        ax.axvline(0, color=fs.DARK, lw=0.8)
        ax.add_patch(Polygon(SQUARE.T, closed=True, fill=False, ec=fs.GRAY, lw=1.1, ls="--"))
        ax.add_patch(Polygon((M @ SQUARE).T, closed=True, fc="#e3f5ee", ec=fs.GREEN, lw=1.8))
        ax.add_patch(Polygon((M @ F).T, closed=True, fc=fs.GREEN, ec="none", alpha=0.75))
        for vec, col in [(M[:, 0], fs.BLUE), (M[:, 1], fs.RED)]:
            ax.annotate("", xy=vec, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2.0, shrinkA=0, shrinkB=0))
        ax.text(ipos[0], ipos[1], "$A\\mathbf{i}$", color=fs.BLUE, fontsize=11, ha="center", va="center")
        ax.text(jpos[0], jpos[1], "$A\\mathbf{j}$", color=fs.RED, fontsize=11, ha="center", va="center")
        ax.text(2.2, -0.3, "area 5", color=fs.GREEN, fontsize=10, ha="center", va="center", weight="bold")
        ax.text(-0.9, -0.85, label, fontsize=10.5, color=fs.DARK, ha="left", va="center")
        ax.set_xlim(-1.0, 4.3)
        ax.set_ylim(-1.3, 3.2)
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-signed-area")


def box():
    """A parallelepiped with edge vectors (3,0,0), (1,2,0), (1,1,2): volume 12."""
    u, v, w = np.array([3, 0, 0.0]), np.array([1, 2, 0.0]), np.array([1, 1, 2.0])

    # oblique projection: x to the right, y up-right, z up
    def pr(p):
        x, y, z = p
        return np.array([x + 0.5 * y, 0.45 * y + z])

    fig, ax = plt.subplots(figsize=(6.0, 3.9))
    ax.set_aspect("equal")
    ax.axis("off")
    o = np.zeros(3)
    verts = {
        "0": o, "u": u, "v": v, "w": w, "uv": u + v, "uw": u + w, "vw": v + w, "uvw": u + v + w,
    }
    faces = [
        (["0", "u", "uv", "v"], "#e3f5ee"),
        (["w", "uw", "uvw", "vw"], "#e3f5ee"),
        (["0", "u", "uw", "w"], "#f1f2f3"),
        (["u", "uv", "uvw", "uw"], "#f1f2f3"),
        (["v", "uv", "uvw", "vw"], "#f1f2f3"),
    ]
    for keys, col in faces[2:]:
        ax.add_patch(Polygon([pr(verts[k]) for k in keys], closed=True, fc=col, ec=fs.DARK, lw=1.0, alpha=0.9))
    ax.add_patch(Polygon([pr(verts[k]) for k in faces[0][0]], closed=True, fc="#cdeee0", ec=fs.GREEN, lw=1.8))
    ax.add_patch(Polygon([pr(verts[k]) for k in faces[1][0]], closed=True, fc="#f9fdfb", ec=fs.DARK, lw=1.0))
    for vec, col, lab, off in [(u, fs.BLUE, "$\\mathbf{a}_1$", (0, -0.28)), (v, fs.RED, "$\\mathbf{a}_2$", (0.3, 0.22)), (w, fs.ORANGE, "$\\mathbf{a}_3$", (-0.3, 0.0))]:
        end = pr(vec)
        ax.annotate("", xy=end, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2.2, shrinkA=0, shrinkB=0))
        ax.text(end[0] + off[0], end[1] + off[1], lab, color=col, fontsize=12, ha="center", va="center")
    c = (pr(verts["0"]) + pr(verts["uv"])) / 2
    ax.text(c[0] + 0.0, c[1] - 0.05, "base area 6", color=fs.GREEN, fontsize=10, ha="center", va="center", weight="bold")
    foot, tip = pr(np.array([1.0, 1.0, 0.0])), pr(w)
    ax.plot([foot[0], tip[0]], [foot[1], tip[1]], color=fs.DARK, lw=1.2, ls="--", zorder=6)
    ax.text(foot[0] + 0.12, foot[1] + 0.62 * (tip[1] - foot[1]), "height 2", color=fs.DARK, fontsize=10, ha="left", va="center", bbox=dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9), zorder=7)
    ax.text(5.5, 2.4, "volume $6 \\cdot 2 = 12$", color=fs.DARK, fontsize=10, ha="left", va="center")
    ax.set_xlim(-0.6, 7.6)
    ax.set_ylim(-0.7, 3.6)
    fs.save(fig, FOLDER, f"{SLUG}-box")


def cost():
    n = np.arange(2, 21)
    fact = np.array([math.factorial(int(k)) for k in n], dtype=float)
    cub = n.astype(float) ** 3
    fig, ax = fs.figure(5.6, 3.7)
    ax.semilogy(n, fact, color=fs.RED, lw=2.4)
    ax.semilogy(n, cub, color=fs.GREEN, lw=2.4)
    ax.grid(True, which="major")
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, length=3)
    ax.set_xlabel("size $n$ of the matrix")
    ax.set_ylabel("operations (log scale)")
    ax.set_xticks(range(2, 21, 2))
    ax.text(14.2, 4e10, "cofactor expansion, about $n!$", color=fs.RED, fontsize=10, ha="right", va="bottom", rotation=0)
    ax.text(20.3, 40, "elimination, about $n^3$", color=fs.GREEN, fontsize=10, ha="right", va="top")
    ax.plot([20], [fact[-1]], "o", color=fs.RED, ms=6)
    ax.plot([20], [cub[-1]], "o", color=fs.GREEN, ms=6)
    ax.text(19.6, fact[-1] / 12, "$20! \\approx 2.4 \\times 10^{18}$", color=fs.RED, fontsize=9, ha="right", va="top")
    ax.text(19.6, cub[-1] * 1.8, "$20^3 = 8000$", color=fs.GREEN, fontsize=9, ha="right", va="bottom")
    ax.set_xlim(1.5, 20.6)
    fs.save(fig, FOLDER, f"{SLUG}-cost")


if __name__ == "__main__":
    signed_area()
    box()
    cost()
