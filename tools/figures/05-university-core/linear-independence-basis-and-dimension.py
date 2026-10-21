"""Figures for docs/05-university-core/06-linear-algebra/04-linear-independence-basis-and-dimension.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/linear-independence-basis-and-dimension.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "linear-independence-basis-and-dimension"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def arrow(ax, tail, tip, color, lw=2.2, z=4):
    ax.annotate(
        "",
        xy=tip,
        xytext=tail,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=14),
        zorder=z,
    )


def grid2d(ax, xlim, ylim, grid=True):
    ax.set_aspect("equal")
    if grid:
        ax.grid(True)
    ax.set_axisbelow(True)
    ax.axhline(0, color=fs.DARK, lw=1.0)
    ax.axvline(0, color=fs.DARK, lw=1.0)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(labelsize=9, length=0)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)


def redundancy():
    """Two independent vectors reach every point; a third vector in the plane is redundant."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 4.0))
    u = np.array([2.0, 1.0])
    w = np.array([-1.0, 2.0])

    grid2d(a, (-3.2, 4.2), (-1.0, 5.2))
    arrow(a, (0, 0), tuple(u), fs.GREEN)
    arrow(a, (0, 0), tuple(w), fs.BLUE)
    p = 1.5 * u + 1.0 * w
    a.plot(*p, "o", color=fs.RED, ms=7, zorder=5)
    a.plot([0, 1.5 * u[0], p[0]], [0, 1.5 * u[1], p[1]], color=fs.RED, lw=1.2, ls="--", zorder=3)
    a.text(2.2, 0.55, "u", color=fs.GREEN, fontsize=11, ha="left", va="top")
    a.text(-1.2, 2.1, "w", color=fs.BLUE, fontsize=11, ha="right", va="center")
    a.text(2.2, 3.3, "1.5u + 1w", color=fs.RED, fontsize=10, ha="left", va="center")
    a.text(0.5, -0.7, "independent: each point has one pair of weights", color=fs.DARK, fontsize=9.5, ha="center", va="center")

    grid2d(b, (-3.2, 4.2), (-1.0, 5.2))
    arrow(b, (0, 0), tuple(u), fs.GREEN)
    arrow(b, (0, 0), tuple(w), fs.BLUE)
    arrow(b, (0, 0), tuple(u + w), fs.RED, lw=2.4)
    b.plot([u[0], u[0] + w[0]], [u[1], u[1] + w[1]], color=fs.BLUE, lw=1.1, ls="--", zorder=3)
    b.plot([w[0], u[0] + w[0]], [w[1], u[1] + w[1]], color=fs.GREEN, lw=1.1, ls="--", zorder=3)
    b.text(2.2, 0.55, "u", color=fs.GREEN, fontsize=11, ha="left", va="top")
    b.text(-1.2, 2.1, "w", color=fs.BLUE, fontsize=11, ha="right", va="center")
    b.text(1.25, 3.55, "u + w", color=fs.RED, fontsize=11, ha="left", va="bottom")
    b.text(0.5, -0.7, "dependent: u + w adds nothing to the span", color=fs.DARK, fontsize=9.5, ha="center", va="center")
    fig.subplots_adjust(wspace=0.08)
    fs.save(fig, FOLDER, f"{SLUG}-redundancy")


def coordinates():
    """Coordinates of v = (4, 7) relative to the basis (2, 1), (1, 3)."""
    b1 = np.array([2.0, 1.0])
    b2 = np.array([1.0, 3.0])
    v = 1 * b1 + 2 * b2
    fig, ax = fs.figure(5.6, 5.0)
    grid2d(ax, (-2.2, 8.0), (-1.4, 9.2), grid=False)
    rng = range(-1, 4)
    for c in rng:
        t = np.array([-1.0, 3.5])
        pts = c * b1[None, :] + t[:, None] * b2[None, :]
        ax.plot(pts[:, 0], pts[:, 1], color=fs.GRAY, lw=0.8, alpha=0.7, zorder=1)
        pts = c * b2[None, :] + t[:, None] * b1[None, :]
        ax.plot(pts[:, 0], pts[:, 1], color=fs.GRAY, lw=0.8, alpha=0.7, zorder=1)
    arrow(ax, (0, 0), tuple(b1), fs.GREEN, lw=2.6)
    arrow(ax, (0, 0), tuple(b2), fs.BLUE, lw=2.6)
    arrow(ax, tuple(b1), tuple(b1 + b2), fs.BLUE, lw=1.4)
    arrow(ax, tuple(b1 + b2), tuple(v), fs.BLUE, lw=1.4)
    arrow(ax, (0, 0), tuple(v), fs.RED, lw=2.6)
    ax.text(2.15, 0.35, "b₁ = (2, 1)", color=fs.GREEN, fontsize=10.5, ha="left", va="top")
    ax.text(0.55, 3.1, "b₂ = (1, 3)", color=fs.BLUE, fontsize=10.5, ha="right", va="center")
    ax.text(7.9, 8.3, "v = (4, 7) = 1·b₁ + 2·b₂", color=fs.RED, fontsize=10.5, ha="right", va="bottom")
    ax.text(3.0, -0.9, "coordinates of v in this basis: (1, 2)", color=fs.DARK, fontsize=10, ha="center", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-coordinates")


def subspaces():
    """One subspace of the plane and three sets that fail the test."""
    fig, axs = plt.subplots(1, 4, figsize=(11.0, 3.2))
    lim = ((-2.6, 2.6), (-2.6, 2.6))
    xs = np.array([-2.6, 2.6])

    a = axs[0]
    grid2d(a, *lim)
    a.plot(xs, 0.5 * xs, color=fs.GREEN, lw=2.6)
    a.plot([0], [0], "o", color=fs.DARK, ms=5, zorder=5)
    a.text(-2.5, 2.35, "y = x/2", color=fs.GREEN, fontsize=10, ha="left", va="center")
    a.text(0, -2.2, "a subspace", color=fs.DARK, fontsize=10.5, ha="center", va="center")

    b = axs[1]
    grid2d(b, *lim)
    b.plot(xs, 0.5 * xs + 1, color=fs.RED, lw=2.6)
    b.plot([0], [0], "o", color=fs.DARK, ms=5, zorder=5)
    b.text(-2.5, 2.35, "y = x/2 + 1", color=fs.RED, fontsize=10, ha="left", va="center")
    b.text(0.15, -0.35, "0", color=fs.DARK, fontsize=9.5, ha="left", va="top")
    b.text(0, -2.2, "misses the origin", color=fs.DARK, fontsize=10.5, ha="center", va="center")

    c = axs[2]
    grid2d(c, *lim)
    c.fill([0, 2.6, 2.6, 0], [0, 0, 2.6, 2.6], color=fs.RED, alpha=0.3, lw=0)
    c.plot([1, -1], [1, -1], "o-", color=fs.DARK, lw=1.0, ms=5, zorder=5)
    c.text(1.15, 1.0, "(1, 1)", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    c.text(-0.9, -1.25, "−(1, 1)", color=fs.DARK, fontsize=9.5, ha="left", va="center", bbox=BOX)
    c.text(0, -2.2, "not closed under ×(−1)", color=fs.DARK, fontsize=10.5, ha="center", va="center")

    d = axs[3]
    grid2d(d, *lim)
    d.plot(xs, 0 * xs, color=fs.RED, lw=2.6)
    d.plot(0 * xs, xs, color=fs.RED, lw=2.6)
    d.plot([1, 0, 1], [0, 1, 1], "o", color=fs.DARK, ms=5, zorder=5)
    d.plot([1, 1], [0, 1], color=fs.DARK, lw=0.9, ls=":")
    d.plot([0, 1], [1, 1], color=fs.DARK, lw=0.9, ls=":")
    d.text(1.12, 0.12, "(1, 0)", color=fs.DARK, fontsize=9.5, ha="left", va="bottom")
    d.text(-0.12, 1.0, "(0, 1)", color=fs.DARK, fontsize=9.5, ha="right", va="center")
    d.text(1.12, 1.0, "(1, 1)", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    d.text(0, -2.2, "not closed under +", color=fs.DARK, fontsize=10.5, ha="center", va="center")
    fig.subplots_adjust(wspace=0.1)
    fs.save(fig, FOLDER, f"{SLUG}-subspaces")


if __name__ == "__main__":
    redundancy()
    coordinates()
    subspaces()
