"""Figures for docs/05-university-core/02-derivatives/02-differentiation-rules.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/differentiation-rules.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "differentiation-rules"
PI = math.pi
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def sine_and_slope():
    """sin x with tangent segments, above cos x, the slope of those tangents."""
    fig, (top, bot) = plt.subplots(2, 1, figsize=(6.2, 5.2), sharex=True)
    xs = np.linspace(-0.25, 2 * PI + 0.25, 600)
    marks = [0, PI / 2, PI, 3 * PI / 2, 2 * PI]
    ticks = [0, PI / 2, PI, 3 * PI / 2, 2 * PI]
    labels = ["0", r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"]
    for ax in (top, bot):
        ax.axhline(0, color=fs.DARK, lw=1.0, zorder=2)
        ax.grid(True)
        ax.set_axisbelow(True)
        ax.set_ylim(-1.45, 1.45)
        ax.set_yticks([-1, 1])
        ax.tick_params(labelsize=9, length=3)
        for m in marks:
            ax.axvline(m, color=fs.GRAY, lw=0.8, ls=":", zorder=1)
    bot.set_xticks(ticks)
    bot.set_xticklabels(labels, fontsize=11)
    top.tick_params(labelbottom=False)
    top.plot(xs, np.sin(xs), color=fs.GREEN, zorder=3)
    for m in marks:
        slope = math.cos(m)
        dx = 0.62
        top.plot([m - dx, m + dx], [math.sin(m) - slope * dx, math.sin(m) + slope * dx],
                 color=fs.ORANGE, lw=2.0, zorder=4)
        top.plot([m], [math.sin(m)], "o", color=fs.ORANGE, ms=5.5, zorder=5)
    bot.plot(xs, np.cos(xs), color=fs.BLUE, zorder=3)
    for m in marks:
        bot.plot([m], [math.cos(m)], "o", color=fs.ORANGE, ms=5.5, zorder=5)
    top.text(0.45, 1.3, "y = sin x, with tangent lines", color=fs.GREEN, fontsize=10, ha="left", va="center")
    bot.text(1.9, 1.3, "y = cos x, the slope of those tangent lines", color=fs.BLUE, fontsize=10,
             ha="left", va="center")
    # slope labels on the lower panel, next to the dots
    offs = [(0.18, -0.3, "left", "slope 1"), (0.12, 0.2, "left", "slope 0"),
            (0.12, 0.15, "left", "slope −1"), (0.12, -0.2, "left", "slope 0"),
            (-0.12, -0.2, "right", "slope 1")]
    for m, (ox, oy, ha, text) in zip(marks, offs):
        bot.text(m + ox, math.cos(m) + oy, text, color=fs.DARK, fontsize=8.5, ha=ha, va="center", bbox=BOX)
    top.set_xlim(-0.35, 2 * PI + 0.45)
    fig.tight_layout(h_pad=0.6)
    fs.save(fig, FOLDER, f"{SLUG}-sine-and-slope")


def product_rectangle():
    """A rectangle u by v whose sides grow by du and dv."""
    fig, ax = fs.figure(4.8, 3.9)
    u, v, du, dv = 4.0, 3.0, 0.7, 0.55
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-0.9, u + du + 1.5)
    ax.set_ylim(-0.9, v + dv + 0.9)
    ax.add_patch(Rectangle((0, 0), u, v, fc=fs.LIGHT, ec=fs.DARK, lw=1.4))
    ax.add_patch(Rectangle((u, 0), du, v, fc="#b7e6d3", ec=fs.DARK, lw=1.0))
    ax.add_patch(Rectangle((0, v), u, dv, fc="#b9d3ea", ec=fs.DARK, lw=1.0))
    ax.add_patch(Rectangle((u, v), du, dv, fc="#f3b5b8", ec=fs.DARK, lw=1.0))
    ax.text(u / 2, v / 2, "u v", color=fs.DARK, fontsize=14, ha="center", va="center")
    ax.text(u + du / 2, v / 2, r"$v\,\Delta u$", color=fs.DARK, fontsize=9.5, ha="center", va="center",
            rotation=90)
    ax.text(u / 2, v + dv / 2, r"$u\,\Delta v$", color=fs.DARK, fontsize=10, ha="center", va="center")
    ax.annotate(r"$\Delta u\,\Delta v$", xy=(u + du / 2, v + dv / 2), xytext=(u + du + 0.35, v + dv + 0.55),
                color=fs.RED, fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=fs.RED, lw=1.1))
    ax.text(u / 2, -0.3, "u", color=fs.DARK, fontsize=11, ha="center", va="top")
    ax.text(u + du / 2, -0.3, r"$\Delta u$", color=fs.DARK, fontsize=10, ha="center", va="top")
    ax.text(-0.2, v / 2, "v", color=fs.DARK, fontsize=11, ha="right", va="center")
    ax.text(-0.2, v + dv / 2, r"$\Delta v$", color=fs.DARK, fontsize=10, ha="right", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-product-rectangle")


if __name__ == "__main__":
    sine_and_slope()
    product_rectangle()
