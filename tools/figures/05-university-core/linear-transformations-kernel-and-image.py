"""Figures for docs/05-university-core/06-linear-algebra/05-linear-transformations-kernel-and-image.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/linear-transformations-kernel-and-image.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "linear-transformations-kernel-and-image"

# An F shape inside the unit square shows orientation (a reflection flips it).
F = np.array(
    [(0.2, 0.1), (0.4, 0.1), (0.4, 0.4), (0.7, 0.4), (0.7, 0.55), (0.4, 0.55), (0.4, 0.7), (0.85, 0.7), (0.85, 0.9), (0.2, 0.9)]
).T
SQUARE = np.array([(0, 0), (1, 0), (1, 1), (0, 1)]).T


def panel(ax, M, name, detail):
    M = np.array(M, dtype=float)
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=8, length=2)
    ax.set_xticks(range(-1, 4))
    ax.set_yticks(range(-1, 4))
    ax.axhline(0, color=fs.DARK, lw=0.8)
    ax.axvline(0, color=fs.DARK, lw=0.8)
    # the original square, dashed
    ax.add_patch(Polygon(SQUARE.T, closed=True, fill=False, ec=fs.GRAY, lw=1.1, ls="--"))
    img = M @ SQUARE
    ax.add_patch(Polygon(img.T, closed=True, fc="#e3f5ee", ec=fs.GREEN, lw=1.8))
    ax.add_patch(Polygon((M @ F).T, closed=True, fc=fs.GREEN, ec="none", alpha=0.75))
    for vec, col, lab in [(M[:, 0], fs.BLUE, "$A\\mathbf{i}$"), (M[:, 1], fs.RED, "$A\\mathbf{j}$")]:
        if np.linalg.norm(vec) > 1e-9:
            ax.annotate("", xy=vec, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=col, lw=2.0, shrinkA=0, shrinkB=0))
    ax.set_xlim(-1.5, 3.3)
    ax.set_ylim(-1.3, 2.6)
    ax.text(-1.4, 2.45, name, fontsize=10, color=fs.DARK, ha="left", va="top", weight="bold")
    ax.text(-1.4, -1.2, detail, fontsize=8.5, color=fs.DARK, ha="left", va="bottom")


def labels(ax, M, ix, jx):
    M = np.array(M, dtype=float)
    for vec, col, lab, off in [(M[:, 0], fs.BLUE, "$A\\mathbf{i}$", ix), (M[:, 1], fs.RED, "$A\\mathbf{j}$", jx)]:
        if np.linalg.norm(vec) > 1e-9:
            ax.text(vec[0] + off[0], vec[1] + off[1], lab, color=col, fontsize=10, ha="center", va="center")


def gallery():
    c, s = np.cos(np.pi / 6), np.sin(np.pi / 6)
    items = [
        ([[c, -s], [s, c]], "rotation by $30^\\circ$", "columns (0.87, 0.5), (-0.5, 0.87)", (0.25, -0.12), (-0.25, 0.1)),
        ([[0, 1], [1, 0]], "reflection in $y = x$", "columns (0, 1), (1, 0)", (-0.2, 0.18), (0.2, -0.18)),
        ([[2, 0], [0, 0.5]], "stretch", "columns (2, 0), (0, 0.5)", (0, -0.2), (-0.28, 0.12)),
        ([[1, 1], [0, 1]], "shear", "columns (1, 0), (1, 1)", (0, -0.2), (0.28, 0.12)),
        ([[0.5, 0.5], [0.5, 0.5]], "projection onto $y = x$", "columns (0.5, 0.5), (0.5, 0.5)", (0.45, 0.05), (-0.1, 0.45)),
        ([[1, -1], [1, 1]], "rotation by $45^\\circ$ and scaling by $\\sqrt{2}$", "columns (1, 1), (-1, 1)", (0.3, 0.05), (-0.3, 0.12)),
    ]
    fig, axes = plt.subplots(2, 3, figsize=(10.2, 6.1))
    for ax, (M, name, detail, ix, jx) in zip(axes.ravel(), items):
        panel(ax, M, name, detail)
        labels(ax, M, ix, jx)
    # the long name in the last panel needs a smaller font
    axes[1, 2].texts[0].set_fontsize(8.2)
    fig.tight_layout(w_pad=1.0, h_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-gallery")


def kernel_image():
    """The map (x, y) -> (x + 2y)(1, 2): every line x + 2y = c lands on one point."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.2))
    for ax in (a, b):
        ax.set_aspect("equal")
        ax.grid(True)
        ax.set_axisbelow(True)
        ax.tick_params(labelsize=8, length=2)
        ax.axhline(0, color=fs.DARK, lw=0.8)
        ax.axvline(0, color=fs.DARK, lw=0.8)
    xs = np.array([-4.0, 4.0])
    a.set_xlim(-4, 4)
    a.set_ylim(-3, 3.2)
    cs = [-2, -1, 0, 1, 2]
    for c in cs:
        y = (c - xs) / 2
        if c == 0:
            a.plot(xs, y, color=fs.RED, lw=2.6)
        else:
            a.plot(xs, y, color=fs.GRAY, lw=1.2)
    a.text(-3.9, -2.75, "red: the kernel, $x + 2y = 0$", color=fs.RED, fontsize=10, ha="left", va="bottom")
    a.text(-3.9, -2.2, "gray: the line $x + 2y = c$", color=fs.DARK, fontsize=9, ha="left", va="bottom")
    for c in cs:
        a.text(3.85, (c - 3.85) / 2 + 0.08, f"$c = {c}$", color=fs.DARK, fontsize=8.5, ha="right", va="bottom")
    a.set_xlabel("domain $\\mathbb{R}^2$")

    b.set_xlim(-2.4, 3.9)
    b.set_ylim(-4.4, 4.4)
    t = np.array([-2.2, 2.2])
    b.plot(t, 2 * t, color=fs.GREEN, lw=2.6)
    for c in cs:
        b.plot([c], [2 * c], "o", color=fs.DARK, ms=5.5, zorder=5)
        if c != 0:
            b.text(c + 0.18, 2 * c - 0.1, f"$c = {c}$", fontsize=9, ha="left", va="top" if c > 0 else "bottom")
    b.plot([0], [0], "o", color=fs.RED, ms=8, zorder=6)
    b.text(0.2, -0.45, "all of the kernel lands here", color=fs.RED, fontsize=9, ha="left", va="top")
    b.text(0.4, -3.2, "green: the image,\nthe line $y = 2x$", color=fs.GREEN, fontsize=10, ha="left", va="top")
    b.set_xlabel("codomain $\\mathbb{R}^2$")
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-kernel-image")


if __name__ == "__main__":
    gallery()
    kernel_image()
