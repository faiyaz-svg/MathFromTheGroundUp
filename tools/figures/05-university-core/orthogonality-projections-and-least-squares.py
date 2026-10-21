"""Figures for docs/05-university-core/06-linear-algebra/07-orthogonality-projections-and-least-squares.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/orthogonality-projections-and-least-squares.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "orthogonality-projections-and-least-squares"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)


def arrow(ax, tail, tip, color, lw=2.2, ls="-"):
    ax.annotate(
        "", xy=tip, xytext=tail,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, shrinkA=0, shrinkB=0, linestyle=ls),
    )


def right_angle(ax, corner, d1, d2, size=0.18):
    d1 = np.array(d1, float) / np.linalg.norm(d1)
    d2 = np.array(d2, float) / np.linalg.norm(d2)
    c = np.array(corner, float)
    pts = [c + size * d1, c + size * (d1 + d2), c + size * d2]
    ax.plot([p[0] for p in pts], [p[1] for p in pts], color=fs.DARK, lw=1.0)


def grid(ax):
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=8, length=2)
    ax.axhline(0, color=fs.DARK, lw=0.8)
    ax.axvline(0, color=fs.DARK, lw=0.8)


def projection_and_gram_schmidt():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.2))

    # left: projection of v = (1, 3) onto the line through u = (2, 1)
    grid(a)
    u = np.array([2.0, 1.0])
    v = np.array([1.0, 3.0])
    p = (v @ u) / (u @ u) * u
    t = np.array([-0.6, 3.2])
    a.plot(t * u[0], t * u[1], color=fs.GRAY, lw=1.3)
    arrow(a, (0, 0), v, fs.DARK)
    arrow(a, (0, 0), p, fs.GREEN, lw=2.8)
    arrow(a, p, v, fs.RED, lw=2.2)
    right_angle(a, p, -u, v - p)
    a.text(0.45, 2.85, "$\\mathbf{v}$", color=fs.DARK, fontsize=12, ha="center")
    a.text(1.0, 0.1, "$\\mathrm{proj}_{\\mathbf{u}}\\,\\mathbf{v}$", color=fs.GREEN, fontsize=11, ha="center", va="top", bbox=BOX)
    a.text(1.6, 2.55,"$\\mathbf{v} - \\mathrm{proj}_{\\mathbf{u}}\\,\\mathbf{v}$", color=fs.RED, fontsize=10.5, ha="left", va="center", bbox=BOX)
    a.text(4.05, 2.15, "line of $\\mathbf{u} = (2, 1)$", color=fs.GRAY, fontsize=9, ha="right", va="bottom", rotation=0)
    a.set_xlim(-0.8, 4.1)
    a.set_ylim(-0.8, 3.7)

    # right: Gram-Schmidt step in the plane
    grid(b)
    v1 = np.array([3.0, 1.0])
    v2 = np.array([2.0, 2.0])
    pr = (v2 @ v1) / (v1 @ v1) * v1
    u2 = v2 - pr
    arrow(b, (0, 0), v1, fs.BLUE)
    arrow(b, (0, 0), v2, fs.DARK)
    arrow(b, (0, 0), pr, fs.GREEN, lw=2.6)
    arrow(b, pr, v2, fs.RED, lw=2.2)
    arrow(b, (0, 0), u2, fs.RED, lw=2.6)
    b.plot([u2[0], v2[0]], [u2[1], v2[1]], color=fs.RED, lw=1.0, ls="--")
    right_angle(b, (0, 0), v1, u2, size=0.22)
    b.text(3.15, 0.85, "$\\mathbf{u}_1 = \\mathbf{v}_1$", color=fs.BLUE, fontsize=11, ha="left", va="center")
    b.text(2.1, 2.2, "$\\mathbf{v}_2$", color=fs.DARK, fontsize=11, ha="left", va="bottom")
    b.text(-0.35, 1.45, "$\\mathbf{u}_2$", color=fs.RED, fontsize=11.5, ha="right", va="center")
    b.text(1.2, 0.1, "$\\mathrm{proj}$", color=fs.GREEN, fontsize=10, ha="center", va="top", bbox=BOX)
    b.set_xlim(-1.0, 4.3)
    b.set_ylim(-0.8, 2.9)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-projection")


def oblique(p):
    x, y, z = p
    return np.array([x + 0.5 * y, 0.45 * y + z])


def least_squares_geometry():
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.set_aspect("equal")
    ax.axis("off")
    corners = [(-0.5, -0.4, 0), (4.2, -0.4, 0), (4.2, 3.0, 0), (-0.5, 3.0, 0)]
    ax.add_patch(Polygon([oblique(c) for c in corners], closed=True, fc="#e3f5ee", ec=fs.GREEN, lw=1.6))
    foot3 = np.array([1.6, 1.0, 0.0])
    b3 = np.array([1.6, 1.0, 2.4])
    other3 = np.array([3.4, 2.0, 0.0])
    foot, bt, other = oblique(foot3), oblique(b3), oblique(other3)
    o = oblique((0, 0, 0))
    arrow(ax, o, bt, fs.DARK, lw=2.2)
    arrow(ax, o, foot, fs.GREEN, lw=2.6)
    ax.plot([foot[0], bt[0]], [foot[1], bt[1]], color=fs.RED, lw=2.4)
    ax.plot([other[0], bt[0]], [other[1], bt[1]], color=fs.GRAY, lw=1.4, ls="--")
    ax.plot([foot[0], other[0]], [foot[1], other[1]], color=fs.GRAY, lw=1.4, ls="--")
    ax.plot(*o, "o", color=fs.DARK, ms=5)
    ax.plot(*foot, "o", color=fs.GREEN, ms=6, zorder=6)
    ax.plot(*other, "o", color=fs.GRAY, ms=6, zorder=6)
    ax.plot(*bt, "o", color=fs.DARK, ms=6, zorder=6)
    # right angle marker at the foot
    d_along = oblique((0.35, 0, 0))
    d_up = oblique((0, 0, 0.35))
    ax.plot(
        [foot[0] + d_along[0], foot[0] + d_along[0] + d_up[0], foot[0] + d_up[0]],
        [foot[1] + d_along[1], foot[1] + d_along[1] + d_up[1], foot[1] + d_up[1]],
        color=fs.DARK, lw=1.0,
    )
    ax.text(bt[0] - 0.12, bt[1] + 0.05, "$\\mathbf{b}$", color=fs.DARK, fontsize=13, ha="right", va="center")
    ax.text(foot[0] - 0.14, foot[1] - 0.18, "$\\hat{\\mathbf{b}} = A\\hat{\\mathbf{x}}$", color=fs.GREEN, fontsize=12, ha="right", va="top")
    ax.text(foot[0] + 0.12, (foot[1] + bt[1]) / 2 + 0.05, "$\\mathbf{b} - A\\hat{\\mathbf{x}}$", color=fs.RED, fontsize=11, ha="left", va="center", bbox=BOX)
    ax.text(other[0] + 0.12, other[1] - 0.05, "$A\\mathbf{x}$", color=fs.GRAY, fontsize=11, ha="left", va="center")
    ax.text(0.3, 2.62, "$\\mathrm{Col}\\,A$", color=fs.GREEN, fontsize=12, ha="center", va="center")
    ax.text(5.2, 2.7, "any other $A\\mathbf{x}$\nis farther from $\\mathbf{b}$", color=fs.DARK, fontsize=9.5, ha="center", va="center")
    ax.set_xlim(-1.4, 6.6)
    ax.set_ylim(-0.7, 3.6)
    fs.save(fig, FOLDER, f"{SLUG}-geometry")


def demand_fit():
    price = np.array([2, 3, 4, 5, 6], float)
    qty = np.array([95, 82, 70, 61, 48], float)
    a0, b0 = 117.2, -11.5
    fig, ax = fs.figure(5.6, 4.4)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, length=3)
    xs = np.array([1.5, 6.5])
    ax.plot(xs, a0 + b0 * xs, color=fs.GREEN, lw=2.4)
    for x, y in zip(price, qty):
        ax.plot([x, x], [y, a0 + b0 * x], color=fs.RED, lw=3.4, zorder=6)
    ax.plot(price, qty, "o", color=fs.DARK, ms=4.5, zorder=5)
    ax.set_xlabel("price (dollars)")
    ax.set_ylabel("quantity per week (units)")
    ax.text(3.35, 97, "$\\hat{q} = 117.2 - 11.5\\,p$", color=fs.GREEN, fontsize=11, ha="left", va="center")
    ax.text(4.5, 75.5, "red: the residuals,\neach under 1.4 units", color=fs.RED, fontsize=9.5, ha="left", va="center")
    ax.set_xlim(1.5, 6.5)
    ax.set_ylim(44, 102)
    fs.save(fig, FOLDER, f"{SLUG}-demand-fit")


if __name__ == "__main__":
    projection_and_gram_schmidt()
    least_squares_geometry()
    demand_fit()
