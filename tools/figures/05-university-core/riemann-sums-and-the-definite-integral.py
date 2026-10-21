"""Figures for docs/05-university-core/04-integrals/01-riemann-sums-and-the-definite-integral.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/riemann-sums-and-the-definite-integral.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "riemann-sums-and-the-definite-integral"


def axes_through_zero(ax, size=9):
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def rules():
    """Left, right and midpoint sums for y = x^2 on [0, 1] with four rectangles."""
    fig, axs = plt.subplots(1, 3, figsize=(8.4, 3.0), sharey=True)
    xs = np.linspace(0, 1, 200)
    n = 4
    h = 1 / n
    titles = [
        ("left sum", 0.0, fs.BLUE, "0.2188"),
        ("right sum", 1.0, fs.ORANGE, "0.4688"),
        ("midpoint sum", 0.5, fs.GREEN, "0.3281"),
    ]
    for ax, (title, off, colour, value) in zip(axs, titles):
        axes_through_zero(ax, size=8)
        ax.set_xlim(-0.08, 1.12)
        ax.set_ylim(-0.22, 1.12)
        ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
        ax.set_xticklabels(["0", "", "0.5", "", "1"])
        ax.set_yticks([0.5, 1])
        for k in range(n):
            x0 = k * h
            height = (x0 + off * h) ** 2
            ax.bar(x0, height, width=h, align="edge", color=colour, alpha=0.28,
                   edgecolor=colour, linewidth=1.2, zorder=2)
            ax.plot([x0 + off * h], [height], "o", color=colour, ms=4.5, zorder=5)
        ax.plot(xs, xs**2, color=fs.DARK, lw=2.0, zorder=4)
        ax.text(0.04, 1.08, f"{title} = {value}", color=colour, fontsize=10, ha="left", va="top")
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-rules")


def signed():
    """Velocity v(t) = 3 - t on [0, 5]: positive area above the axis, negative below."""
    fig, ax = fs.figure(5.4, 3.6)
    axes_through_zero(ax)
    ax.set_xlim(-0.3, 5.6)
    ax.set_ylim(-2.6, 3.6)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([-2, -1, 1, 2, 3])
    t = np.linspace(0, 5, 200)
    v = 3 - t
    ax.fill_between(t, 0, v, where=v >= 0, color=fs.GREEN, alpha=0.3, zorder=2)
    ax.fill_between(t, 0, v, where=v <= 0, color=fs.RED, alpha=0.3, zorder=2)
    ax.plot(t, v, color=fs.DARK, lw=2.0, zorder=4)
    ax.text(1.0, 0.75, "area 4.5", color=fs.GREEN, fontsize=10.5, ha="center", va="center")
    ax.text(4.55, -0.85, "area\n−2", color=fs.RED, fontsize=10.5, ha="center", va="center")
    ax.text(0.15, 3.35, "v(t) = 3 − t", color=fs.DARK, fontsize=10, ha="left", va="center")
    ax.text(5.5, 0.2, "t (s)", fontsize=9.5, ha="right", va="bottom", color=fs.DARK)
    fs.save(fig, FOLDER, f"{SLUG}-signed")


def errors():
    """Error of the left, midpoint and trapezoid rules for the integral of 4/(1+x^2) on [0, 1]."""
    f = lambda x: 4 / (1 + x**2)
    ns = np.unique(np.round(10 ** np.linspace(0.6, 4, 40)).astype(int))
    left, mid, trap = [], [], []
    for n in ns:
        h = 1 / n
        k = np.arange(n)
        left.append(abs(h * f(k * h).sum() - math.pi))
        mid.append(abs(h * f((k + 0.5) * h).sum() - math.pi))
        trap.append(abs(h * (f(0) / 2 + f(np.arange(1, n) * h).sum() + f(1) / 2) - math.pi))
    fig, ax = fs.figure(5.4, 4.0)
    ax.loglog(ns, left, color=fs.BLUE, lw=1.8)
    ax.loglog(ns, trap, color=fs.ORANGE, lw=1.8)
    ax.loglog(ns, mid, color=fs.GREEN, lw=1.8, ls="--")
    ax.set_xlim(3, 12000)
    ax.set_ylim(1e-10, 1)
    ax.set_xlabel("number of rectangles n")
    ax.set_ylabel("error in the estimate of pi")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.text(40, 5e-2, "left sum: error shrinks like 1/n", color=fs.BLUE, fontsize=10, ha="left", va="bottom")
    ax.text(3.6, 4e-8, "trapezoid: error shrinks like 1/n²", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax.text(3.6, 4e-9, "midpoint: about half the trapezoid error", color=fs.GREEN, fontsize=10, ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-errors")


if __name__ == "__main__":
    rules()
    signed()
    errors()
