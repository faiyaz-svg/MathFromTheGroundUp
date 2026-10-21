"""Figures for docs/05-university-core/06-linear-algebra/08-eigenvalues-and-eigenvectors.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/eigenvalues-and-eigenvectors.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "eigenvalues-and-eigenvectors"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)


def arrow(ax, tail, tip, color, lw=2.2):
    ax.annotate("", xy=tip, xytext=tail, arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, shrinkA=0, shrinkB=0))


def circle_to_ellipse():
    A = np.array([[2.0, 1.0], [1.0, 2.0]])
    fig, ax = plt.subplots(figsize=(5.6, 5.2))
    ax.set_aspect("equal")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=8, length=2)
    ax.axhline(0, color=fs.DARK, lw=0.8)
    ax.axvline(0, color=fs.DARK, lw=0.8)
    t = np.linspace(0, 2 * np.pi, 400)
    circle = np.vstack([np.cos(t), np.sin(t)])
    ellipse = A @ circle
    ax.plot(circle[0], circle[1], color=fs.GRAY, lw=1.4, ls="--")
    ax.plot(ellipse[0], ellipse[1], color=fs.DARK, lw=1.6)
    s = 1 / np.sqrt(2)
    v1, v2 = np.array([s, s]), np.array([s, -s])
    # the two eigen-directions as long thin lines
    for d, c in [(v1, fs.GREEN), (v2, fs.BLUE)]:
        ax.plot([-3.6 * d[0], 3.6 * d[0]], [-3.6 * d[1], 3.6 * d[1]], color=c, lw=0.9, alpha=0.5)
    arrow(ax, (0, 0), v1, fs.GREEN, 2.6)
    arrow(ax, (0, 0), A @ v1, fs.GREEN, 2.6)
    arrow(ax, (0, 0), v2, fs.BLUE, 2.6)
    # a vector that is not an eigenvector: i goes to (2, 1), which points elsewhere
    arrow(ax, (0, 0), (1, 0), fs.RED, 2.0)
    arrow(ax, (0, 0), A @ np.array([1.0, 0.0]), fs.RED, 2.0)
    ax.text(0.55, 0.88, "$\\mathbf{v}_1$", color=fs.GREEN, fontsize=11, ha="right", va="bottom", bbox=BOX)
    ax.text(*(A @ v1 + np.array([0.12, 0.05])), "$A\\mathbf{v}_1 = 3\\mathbf{v}_1$", color=fs.GREEN, fontsize=10.5, ha="left", va="bottom")
    ax.text(v2[0] + 0.1, v2[1] - 0.12, "$\\mathbf{v}_2 = A\\mathbf{v}_2$", color=fs.BLUE, fontsize=10.5, ha="left", va="top")
    ax.text(1.0, -0.08, "$\\mathbf{i}$", color=fs.RED, fontsize=11, ha="left", va="top")
    ax.text(2.05, 1.0, "$A\\mathbf{i} = (2, 1)$", color=fs.RED, fontsize=10.5, ha="left", va="center")
    ax.text(-2.9, -2.55, "dashed: the unit circle\nsolid: its image under $A$", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax.set_xlim(-3.4, 3.9)
    ax.set_ylim(-3.2, 3.4)
    fs.save(fig, FOLDER, f"{SLUG}-circle")


def markov():
    k = np.arange(0, 11)
    sunny_start = 2 / 3 + (1 / 3) * 0.4**k
    rainy_start = 2 / 3 - (2 / 3) * 0.4**k
    fig, ax = fs.figure(5.6, 3.6)
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9, length=3)
    ax.axhline(2 / 3, color=fs.GRAY, lw=1.2, ls="--")
    ax.plot(k, sunny_start, "o-", color=fs.GREEN, ms=4.5)
    ax.plot(k, rainy_start, "o-", color=fs.BLUE, ms=4.5)
    ax.text(10.2, 2 / 3 - 0.012, "steady state 2/3", color=fs.DARK, fontsize=10, ha="right", va="top")
    ax.text(1.25, 0.9, "starts sunny", color=fs.GREEN, fontsize=10, ha="left", va="center")
    ax.text(1.25, 0.34, "starts rainy", color=fs.BLUE, fontsize=10, ha="left", va="center")
    ax.set_xlabel("day $k$")
    ax.set_ylabel("probability of sun")
    ax.set_xlim(-0.3, 10.4)
    ax.set_ylim(-0.03, 1.05)
    fs.save(fig, FOLDER, f"{SLUG}-markov")


if __name__ == "__main__":
    circle_to_ellipse()
    markov()
