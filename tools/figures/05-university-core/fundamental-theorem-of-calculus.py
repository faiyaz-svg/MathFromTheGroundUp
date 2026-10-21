"""Figures for docs/05-university-core/04-integrals/02-fundamental-theorem-of-calculus.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/fundamental-theorem-of-calculus.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "fundamental-theorem-of-calculus"


def style_axes(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def accumulation():
    """f(t) = sin t on top, and its accumulation function F(x) = 1 - cos x below."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5.8, 5.6), sharex=True,
                                   gridspec_kw={"height_ratios": [1, 1], "hspace": 0.12})
    x0 = 2.2
    t = np.linspace(0, 2 * np.pi, 400)
    for ax in (ax1, ax2):
        style_axes(ax)
        ax.set_xlim(-0.2, 2 * np.pi + 0.3)
    ax1.spines["bottom"].set_position("zero")
    ax1.set_ylim(-1.45, 1.45)
    ax1.set_yticks([-1, 1])
    ax1.plot(t, np.sin(t), color=fs.GREEN, lw=2.2, zorder=4)
    mask = t <= x0
    ax1.fill_between(t[mask], 0, np.sin(t[mask]), color=fs.GREEN, alpha=0.3, zorder=2)
    ax1.plot([x0, x0], [0, np.sin(x0)], color=fs.DARK, lw=1.2, ls="--", zorder=3)
    ax1.text(1.2, 0.2, "area = F(x)", color=fs.GREEN, fontsize=9.5, ha="center", va="center")
    ax1.text(5.0, 0.8, "f(t) = sin t", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax1.text(x0 + 0.08, -0.3, "x", color=fs.DARK, fontsize=10, ha="left", va="center")
    ax1.text(4.7, -0.55, "f < 0: F falls", color=fs.RED, fontsize=9.5, ha="center", va="center")
    ax1.text(1.6, 1.22, "f > 0: F rises", color=fs.GREEN, fontsize=9.5, ha="center", va="center")
    ax1.spines["left"].set_position(("data", 0))
    ax1.spines["bottom"].set_position("zero")
    ax2.set_ylim(-0.3, 2.45)
    ax2.set_yticks([0, 1, 2])
    ax2.plot(t, 1 - np.cos(t), color=fs.BLUE, lw=2.2, zorder=4)
    ax2.plot([x0], [1 - np.cos(x0)], "o", color=fs.BLUE, ms=6.5, zorder=6)
    ax2.plot([x0, x0], [0, 1 - np.cos(x0)], color=fs.DARK, lw=1.2, ls="--", zorder=3)
    ax2.text(x0 - 0.12, 1.75, "F(x) = 1.59", color=fs.BLUE, fontsize=10, ha="right", va="center")
    ax2.plot([np.pi], [2], "o", color=fs.RED, ms=6, zorder=6)
    ax2.text(np.pi + 0.12, 2.22, "top of F where f = 0", color=fs.RED, fontsize=9.5, ha="left", va="center")
    ax2.text(5.6, 0.55, "F(x) = 1 − cos x", color=fs.BLUE, fontsize=10.5, ha="center", va="center")
    ax2.set_xticks([0, 1, 2, np.pi, 4, 5, 6])
    ax2.set_xticklabels(["0", "1", "2", "π", "4", "5", "6"])
    ax2.text(2 * np.pi + 0.25, -0.22, "x", fontsize=10, ha="right", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-accumulation")


def strip():
    """The strip of area between x and x + h, squeezed between two rectangles."""
    fig, ax = fs.figure(5.6, 3.7)
    style_axes(ax)
    f = lambda t: 1.2 + 0.7 * np.sin(1.2 * t) + 0.15 * t
    t = np.linspace(0, 4.4, 300)
    x, h = 2.2, 0.55
    ax.plot(t, f(t), color=fs.DARK, lw=2.2, zorder=4)
    m = t <= x
    ax.fill_between(t[m], 0, f(t[m]), color=fs.GREEN, alpha=0.22, zorder=1)
    s = (t >= x) & (t <= x + h)
    ax.fill_between(t[s], 0, f(t[s]), color=fs.ORANGE, alpha=0.4, zorder=2)
    lo = min(f(x), f(x + h))
    hi = max(f(x), f(x + h))
    ax.plot([x, x + h], [hi, hi], color=fs.RED, lw=1.4, ls="--", zorder=3)
    ax.plot([x, x + h], [lo, lo], color=fs.BLUE, lw=1.4, ls="--", zorder=3)
    for v in (x, x + h):
        ax.plot([v, v], [0, f(v)], color=fs.DARK, lw=1.0, zorder=3)
    ax.set_xlim(-0.2, 4.7)
    ax.set_ylim(0, 2.9)
    ax.set_xticks([x, x + h])
    ax.set_xticklabels(["x", "x + h"])
    ax.set_yticks([])
    ax.text(0.9, 0.5, "area F(x)", color=fs.GREEN, fontsize=10.5, ha="center", va="center")
    ax.text(0.15, 2.6, "y = f(t)", color=fs.DARK, fontsize=10.5, ha="left", va="center")
    ax.annotate("new strip: F(x + h) − F(x)", xy=(x + h / 2, lo * 0.55), xytext=(3.0, 0.75),
                color=fs.ORANGE, fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=fs.ORANGE, lw=1.2))
    ax.annotate("highest height, f(c₂)", xy=(x + h, hi), xytext=(3.0, 2.6), color=fs.RED,
                fontsize=9.5, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=fs.RED, lw=1.1))
    ax.annotate("lowest height, f(c₁)", xy=(x + h, lo), xytext=(3.3, 1.8), color=fs.BLUE,
                fontsize=9.5, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=fs.BLUE, lw=1.1))
    fs.save(fig, FOLDER, f"{SLUG}-strip")


if __name__ == "__main__":
    accumulation()
    strip()
