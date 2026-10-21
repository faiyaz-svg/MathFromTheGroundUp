"""Figures for docs/05-university-core/02-derivatives/01-the-derivative-definition.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/the-derivative-definition.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "the-derivative-definition"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def axes_through_zero(ax, size=9):
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def secants():
    """Secant lines through (1, 1) on y = x^2 turning into the tangent line."""
    fig, ax = fs.figure(5.4, 4.6)
    axes_through_zero(ax)
    ax.set_xlim(-1.1, 4.9)
    ax.set_ylim(-3.4, 10.4)
    ax.set_xticks([1, 2, 3])
    ax.set_yticks([2, 4, 6, 8])
    xs = np.linspace(-1.0, 3.05, 300)
    ax.plot(xs, xs**2, color=fs.DARK, lw=2.2, zorder=3)
    ax.text(-0.95, 1.9, "y = x²", color=fs.DARK, fontsize=10, ha="left", va="center", bbox=BOX)
    lx = np.array([0.0, 3.0])
    specs = [(2.0, fs.RED, 4.0), (1.0, fs.ORANGE, 3.0), (0.5, fs.BLUE, 2.5)]
    for h, colour, slope in specs:
        ax.plot(lx, 1 + slope * (lx - 1), color=colour, lw=1.6, zorder=2)
        ax.plot([1 + h], [(1 + h) ** 2], "o", color=colour, ms=5.5, zorder=5)
    ax.plot(lx, 1 + 2 * (lx - 1), color=fs.GREEN, lw=2.4, zorder=4)
    ax.plot([1], [1], "o", color=fs.DARK, ms=7, zorder=6)
    labels = [
        (9.0, "h = 2, slope 4", fs.RED),
        (7.0, "h = 1, slope 3", fs.ORANGE),
        (6.0, "h = 0.5, slope 2.5", fs.BLUE),
        (5.0, "tangent, slope 2", fs.GREEN),
    ]
    for y, text, colour in labels:
        ax.text(3.1, y, text, color=colour, fontsize=9.5, ha="left", va="center")
    ax.text(0.85, 1.55, "(1, 1)", color=fs.DARK, fontsize=9.5, ha="right", va="bottom")
    fs.save(fig, FOLDER, f"{SLUG}-secants")


def failures():
    """Four ways a derivative can fail to exist at x = 0."""
    fig, axs = plt.subplots(2, 2, figsize=(6.6, 5.4))
    x = np.linspace(-1, 1, 801)
    panels = [
        (axs[0, 0], np.abs(x), r"corner: $|x|$", (-1.1, 1.1), (-0.25, 1.25)),
        (axs[0, 1], np.abs(x) ** (2 / 3), r"cusp: $x^{2/3}$", (-1.1, 1.1), (-0.25, 1.25)),
        (axs[1, 0], np.cbrt(x), r"vertical tangent: $x^{1/3}$", (-1.1, 1.1), (-1.25, 1.25)),
    ]
    for ax, y, label, xl, yl in panels:
        axes_through_zero(ax, size=8)
        ax.set_xlim(*xl)
        ax.set_ylim(*yl)
        ax.set_xticks([-1, 1])
        ax.set_yticks([v for v in (-1, 1) if yl[0] < v < yl[1]])
        ax.plot(x, y, color=fs.GREEN, zorder=4)
        ax.plot([0], [0], "o", color=fs.RED, ms=6, zorder=6)
        ax.text(-1.05, yl[1] - 0.02, label, color=fs.DARK, fontsize=9.5, ha="left", va="top")
    axs[1, 0].plot([0, 0], [-1.25, 1.25], color=fs.RED, lw=1.3, ls="--", zorder=3)
    ax = axs[1, 1]
    axes_through_zero(ax, size=8)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-0.25, 1.25)
    ax.set_xticks([-1, 1])
    ax.set_yticks([1])
    ax.plot([-1, 0], [0, 0], color=fs.GREEN, zorder=4)
    ax.plot([0, 1], [1, 1], color=fs.GREEN, zorder=4)
    ax.plot([0], [0], "o", mfc="white", mec=fs.GREEN, ms=6, zorder=6)
    ax.plot([0], [1], "o", color=fs.RED, ms=6, zorder=6)
    ax.text(-1.05, 1.23, "jump: a step", color=fs.DARK, fontsize=9.5, ha="left", va="top")
    fig.tight_layout(h_pad=2.2, w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-failures")


def numerical():
    """Error of two difference quotients for the derivative of exp at x = 1."""
    fig, ax = fs.figure(5.4, 4.0)
    h = 10.0 ** np.linspace(-16, 0, 400)
    true = math.e
    fwd = np.abs((np.exp(1 + h) - np.exp(1)) / h - true)
    cen = np.abs((np.exp(1 + h) - np.exp(1 - h)) / (2 * h) - true)
    ax.loglog(h, fwd, color=fs.ORANGE, lw=1.6)
    ax.loglog(h, cen, color=fs.BLUE, lw=1.6)
    ax.set_xlim(1e-16, 1)
    ax.set_ylim(1e-12, 10)
    ax.set_xlabel("step size h")
    ax.set_ylabel(r"error in the derivative of $e^x$ at $x = 1$")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.text(1e-5, 3e-2, "forward difference", color=fs.ORANGE, fontsize=10, ha="center", va="bottom")
    ax.text(3e-3, 1e-9, "central difference", color=fs.BLUE, fontsize=10, ha="center", va="top")
    ax.annotate("rounding error\ntakes over", xy=(1e-13, 4.6e-4), xytext=(1e-15, 1e-9),
                color=fs.RED, fontsize=9.5, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=fs.RED, lw=1.2))
    ax.annotate("best forward h is near 1e-8", xy=(1e-8, 6.6e-9), xytext=(2e-13, 3e-12),
                color=fs.ORANGE, fontsize=9.5, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=fs.ORANGE, lw=1.2))
    fs.save(fig, FOLDER, f"{SLUG}-numerical")


if __name__ == "__main__":
    secants()
    failures()
    numerical()
