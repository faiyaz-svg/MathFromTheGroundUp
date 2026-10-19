"""Figures for docs/03-high-school/05-quadratics-and-complex-numbers/03-complex-numbers.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/03-high-school/complex-numbers.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "03-high-school"
SLUG = "complex-numbers"
M = "−"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def num(v):
    return f"{v:g}".replace("-", M)


def plane(ax, xmin, xmax, ymin, ymax, size=9, imag=False, equal=True):
    """Axes through the origin with arrows, a light grid and tick labels."""
    ax.set_xlim(xmin - 0.5, xmax + 0.8)
    ax.set_ylim(ymin - 0.5, ymax + 0.8)
    if equal:
        ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks(range(xmin, xmax + 1))
    ax.set_yticks(range(ymin, ymax + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.tick_params(length=3)
    ax.grid(True, zorder=0)
    ax.set_axisbelow(True)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for t in range(xmin, xmax + 1):
        if t != 0:
            ax.text(t, -0.18, num(t), ha="center", va="top", fontsize=size, zorder=4, bbox=box)
    for t in range(ymin, ymax + 1):
        if t != 0:
            label = num(t) + ("i" if imag else "")
            ax.text(-0.18, t, label, ha="right", va="center", fontsize=size, zorder=4, bbox=box)
    ax.plot(1, 0, ">", color=fs.DARK, transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^", color=fs.DARK, transform=ax.get_xaxis_transform(), clip_on=False, ms=5)


def arrow(ax, p, q, colour, rad=0.0, lw=1.8):
    ax.add_patch(
        FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=13, color=colour, lw=lw,
                        connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0, zorder=4)
    )


def plane_figure():
    fig, ax = fs.figure(5.4, 4.2)
    plane(ax, -1, 5, -3, 3, imag=True)
    ax.plot([3, 3], [0, 2], color=fs.GRAY, ls=(0, (3, 3)), lw=1.2, zorder=2)
    ax.plot([0, 3], [2, 2], color=fs.GRAY, ls=(0, (3, 3)), lw=1.2, zorder=2)
    ax.plot([3, 3], [0, -2], color=fs.GRAY, ls=(0, (3, 3)), lw=1.2, zorder=2)
    arrow(ax, (0, 0), (3, 2), fs.GREEN)
    arrow(ax, (0, 0), (3, -2), fs.BLUE)
    ax.plot([3], [2], "o", color=fs.GREEN, zorder=6)
    ax.plot([3], [-2], "o", color=fs.BLUE, zorder=6)
    ax.text(3.15, 2.15, "$z = 3 + 2i$", ha="left", va="bottom", fontsize=11, color=fs.GREEN, bbox=BOX, zorder=6)
    ax.text(3.15, -2.15, "$\\overline{z} = 3 - 2i$", ha="left", va="top", fontsize=11, color=fs.BLUE, bbox=BOX, zorder=6)
    ax.text(1.7, 1.0, "$|z| = \\sqrt{13}$", ha="center", va="top", fontsize=10.5, color=fs.GREEN,
            rotation=33.7, rotation_mode="anchor", zorder=6)
    ax.text(5.9, 0.15, "real axis", ha="right", va="bottom", fontsize=10)
    ax.text(0.15, 3.75, "imaginary axis", ha="left", va="top", fontsize=10)
    fs.save(fig, FOLDER, f"{SLUG}-plane")


def rotation():
    fig, ax = fs.figure(5.0, 4.8)
    plane(ax, -4, 4, -4, 4, imag=True, size=8)
    r = np.sqrt(13)
    th = np.linspace(0, 2 * np.pi, 300)
    ax.plot(r * np.cos(th), r * np.sin(th), color=fs.GRAY, lw=1.0, ls=(0, (3, 3)), zorder=2)
    pts = [(3, 2), (-2, 3), (-3, -2), (2, -3)]
    labels = ["$z = 3 + 2i$", "$iz = -2 + 3i$", "$i^2 z = -3 - 2i$", "$i^3 z = 2 - 3i$"]
    colours = [fs.GREEN, fs.BLUE, fs.RED, fs.ORANGE]
    aligns = [("left", "bottom", (0.2, 0.15)), ("right", "bottom", (-0.2, 0.15)),
              ("right", "top", (-0.2, -0.15)), ("left", "top", (0.2, -0.15))]
    for p, lab, col, (ha, va, off) in zip(pts, labels, colours, aligns):
        ax.plot(*p, "o", color=col, zorder=6)
        ax.text(p[0] + off[0], p[1] + off[1], lab, ha=ha, va=va, fontsize=10.5, color=col, bbox=BOX, zorder=6)
    for i in range(4):
        p, q = pts[i], pts[(i + 1) % 4]
        a0 = np.arctan2(p[1], p[0])
        a1 = a0 + np.pi / 2
        s = np.linspace(a0 + 0.12, a1 - 0.12, 30)
        ax.plot(r * 0.82 * np.cos(s), r * 0.82 * np.sin(s), color=colours[(i + 1) % 4], lw=1.6, zorder=3)
        ax.annotate("", xy=(r * 0.82 * np.cos(a1 - 0.05), r * 0.82 * np.sin(a1 - 0.05)),
                    xytext=(r * 0.82 * np.cos(a1 - 0.3), r * 0.82 * np.sin(a1 - 0.3)),
                    arrowprops=dict(arrowstyle="-|>", color=colours[(i + 1) % 4], lw=1.6, mutation_scale=12))
    fs.save(fig, FOLDER, f"{SLUG}-rotation")


def roots():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.2, 3.8), gridspec_kw={"width_ratios": [1.1, 1]})
    # left: the parabola y = x^2 + 2x + 5 never reaches the x-axis
    ax1.set_xlim(-4.2, 2.4)
    ax1.set_ylim(-1.2, 10.5)
    ax1.spines["left"].set_position("zero")
    ax1.spines["bottom"].set_position("zero")
    ax1.set_xticks(range(-4, 3))
    ax1.set_yticks(range(0, 11, 2))
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.grid(True, zorder=0)
    ax1.set_axisbelow(True)
    ax1.tick_params(length=3)
    box = dict(facecolor="white", edgecolor="none", pad=0.2)
    for t in range(-4, 3):
        if t != 0:
            ax1.text(t, -0.35, num(t), ha="center", va="top", fontsize=8.5, bbox=box, zorder=4)
    for t in range(2, 11, 2):
        ax1.text(0.12, t, num(t), ha="left", va="center", fontsize=8.5, bbox=box, zorder=4)
    xs = np.linspace(-3.6, 1.6, 300)
    ax1.plot(xs, xs**2 + 2 * xs + 5, color=fs.GREEN, zorder=3)
    ax1.plot(-1, 4, "o", color=fs.RED, zorder=6)
    ax1.text(-1.0, 3.4, "vertex $(-1, 4)$", ha="center", va="top", fontsize=10, color=fs.RED, bbox=BOX, zorder=6)
    ax1.text(1.9, 9.8, "$y = x^2 + 2x + 5$", ha="right", va="top", fontsize=10.5, color=fs.GREEN, bbox=BOX)
    ax1.text(0.5, -0.17, "no real solutions: the graph misses the $x$-axis", transform=ax1.transAxes,
             ha="center", va="top", fontsize=10)
    # right: the two solutions in the complex plane
    plane(ax2, -3, 2, -3, 3, imag=True, size=8.5)
    ax2.plot([-1, -1], [-3.3, 3.3], color=fs.BLUE, ls=(0, (5, 3)), lw=1.4, zorder=2)
    ax2.plot([-1, -1], [2, -2], "o", color=fs.RED, zorder=6)
    ax2.text(-1.2, 2.0, "$-1 + 2i$", ha="right", va="center", fontsize=10.5, color=fs.RED, bbox=BOX, zorder=6)
    ax2.text(-1.2, -2.0, "$-1 - 2i$", ha="right", va="center", fontsize=10.5, color=fs.RED, bbox=BOX, zorder=6)
    ax2.text(-1.2, 3.25, "real part $-1$ is\nthe axis $x = -1$", ha="right", va="center", fontsize=9, color=fs.BLUE, bbox=BOX, zorder=6)
    ax2.text(0.5, -0.17, "the two solutions in the complex plane", transform=ax2.transAxes,
             ha="center", va="top", fontsize=10)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-roots")


if __name__ == "__main__":
    plane_figure()
    rotation()
    roots()
