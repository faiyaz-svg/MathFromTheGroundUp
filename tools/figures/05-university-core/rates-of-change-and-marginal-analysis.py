"""Figures for docs/05-university-core/03-applications-of-derivatives/01-rates-of-change-and-marginal-analysis.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/rates-of-change-and-marginal-analysis.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Polygon  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "rates-of-change-and-marginal-analysis"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def related_rates():
    """A 13 m ladder against a wall, and a lamp-post shadow."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(8.6, 3.6), gridspec_kw={"width_ratios": [1, 1.25]})

    # Ladder
    a.set_aspect("equal")
    a.axis("off")
    a.plot([0, 0], [0, 13.5], color=fs.DARK, lw=3)
    a.plot([-0.5, 9], [0, 0], color=fs.DARK, lw=3)
    a.plot([5, 0], [0, 12], color=fs.GREEN, lw=3.2, solid_capstyle="round")
    a.plot([5], [0], "o", color=fs.RED, ms=7, zorder=5)
    a.plot([0], [12], "o", color=fs.BLUE, ms=7, zorder=5)
    a.annotate("", xy=(8.4, 0.9), xytext=(6.2, 0.9), arrowprops=dict(arrowstyle="->", color=fs.RED, lw=1.8))
    a.text(7.3, 1.5, "foot: 0.6 m/s", color=fs.RED, fontsize=9.5, ha="center", va="bottom")
    a.annotate("", xy=(0.9, 10.2), xytext=(0.9, 12.0), arrowprops=dict(arrowstyle="->", color=fs.BLUE, lw=1.8))
    a.text(1.3, 10.0, "top slides down", color=fs.BLUE, fontsize=9.5, ha="left", va="top")
    a.text(3.4, 6.9, "13 m", color=fs.GREEN, fontsize=10.5, ha="center", va="center", rotation=-67, bbox=BOX)
    a.text(2.5, -0.8, "x = 5 m", color=fs.RED, fontsize=10, ha="center", va="top")
    a.text(-0.5, 6, "y = 12 m", color=fs.BLUE, fontsize=10, ha="right", va="center")
    a.set_xlim(-3.2, 9.4)
    a.set_ylim(-2, 14)

    # Shadow
    b.set_aspect("equal")
    b.axis("off")
    x = 4.0
    tip = 1.5625 * x
    b.plot([-0.5, 8.2], [0, 0], color=fs.DARK, lw=3)
    b.plot([0, 0], [0, 5], color=fs.DARK, lw=4)
    b.plot([0], [5.0], "o", color=fs.ORANGE, ms=9, zorder=5)
    b.plot([0, tip], [5, 0], color=fs.ORANGE, lw=1.6, ls="--")
    b.plot([x, x], [0, 1.8], color=fs.BLUE, lw=4, solid_capstyle="round")
    b.plot([tip], [0], "o", color=fs.RED, ms=7, zorder=5)
    b.plot([x, tip], [-0.35, -0.35], color=fs.RED, lw=1.6)
    b.text((x + tip) / 2, -0.7, "shadow s", color=fs.RED, fontsize=10, ha="center", va="top")
    b.plot([0, x], [-0.35, -0.35], color=fs.BLUE, lw=1.6)
    b.text(x / 2, -0.7, "distance x", color=fs.BLUE, fontsize=10, ha="center", va="top")
    b.text(0.25, 5.1, "lamp, 5 m", color=fs.ORANGE, fontsize=10, ha="left", va="bottom")
    b.text(x + 0.2, 1.9, "person, 1.8 m", color=fs.BLUE, fontsize=10, ha="left", va="bottom")
    b.text(tip, 0.45, "tip", color=fs.RED, fontsize=10, ha="center", va="bottom")
    b.set_xlim(-0.8, 8.4)
    b.set_ylim(-2, 6.2)
    fs.save(fig, FOLDER, f"{SLUG}-ladder-and-shadow")


def cone():
    """A conical tank, point down, with water at depth h."""
    fig, ax = fs.figure(4.2, 3.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Polygon([[-2, 4], [2, 4], [0, 0]], closed=True, fill=False, ec=fs.DARK, lw=2.4))
    h = 3.0
    r = h / 2
    ax.add_patch(Polygon([[-r, h], [r, h], [0, 0]], closed=True, fc="#cfe6f6", ec=fs.BLUE, lw=1.8))
    ax.plot([-r, r], [h, h], color=fs.BLUE, lw=2.2)
    ax.plot([0, r], [h, h], color=fs.RED, lw=2.6)
    ax.text(r / 2, h + 0.12, "r", color=fs.RED, fontsize=11, ha="center", va="bottom")
    ax.plot([0, 0], [0, h], color=fs.GREEN, lw=2.6)
    ax.text(-0.12, h / 2, "h", color=fs.GREEN, fontsize=11, ha="right", va="center")
    ax.annotate("", xy=(2.6, 4), xytext=(2.6, 0), arrowprops=dict(arrowstyle="<->", color=fs.DARK, lw=1.2))
    ax.text(2.75, 2, "4 m", color=fs.DARK, fontsize=10, ha="left", va="center")
    ax.annotate("", xy=(-2, 4.45), xytext=(2, 4.45), arrowprops=dict(arrowstyle="<->", color=fs.DARK, lw=1.2))
    ax.text(0, 4.6, "4 m across", color=fs.DARK, fontsize=10, ha="center", va="bottom")
    ax.text(0, -0.55, "draining at 0.5 m³/min", color=fs.BLUE, fontsize=10, ha="center", va="top")
    ax.set_xlim(-2.6, 3.8)
    ax.set_ylim(-1.3, 5.3)
    fs.save(fig, FOLDER, f"{SLUG}-cone")


def average_and_marginal():
    """Average cost and marginal cost for C(q) = 1000 + 10q + 0.05q^2."""
    fig, ax = fs.figure(5.6, 3.8)
    ax.grid(True)
    ax.set_axisbelow(True)
    q = np.linspace(28, 300, 400)
    avg = 1000 / q + 10 + 0.05 * q
    mc = 10 + 0.1 * q
    ax.plot(q, avg, color=fs.GREEN, lw=2.4)
    ax.plot(q, mc, color=fs.RED, lw=2.4)
    q0 = 20000 ** 0.5
    y0 = 10 + 0.1 * q0
    ax.plot([q0, q0], [0, y0], color=fs.GRAY, lw=1.2, ls="--")
    ax.plot([q0], [y0], "o", color=fs.DARK, ms=7, zorder=5)
    ax.text(q0 + 6, 8, "q ≈ 141.4", color=fs.DARK, fontsize=10, ha="left", va="bottom")
    ax.text(q0 + 8, y0 - 5.5, "MC = AC ≈ \\$24.14", color=fs.DARK, fontsize=10, ha="left", va="top")
    ax.text(40, 41, "average cost AC(q)", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax.text(212, 35.5, "marginal cost MC(q)", color=fs.RED, fontsize=10.5, ha="right", va="bottom")
    ax.set_xlim(0, 310)
    ax.set_ylim(0, 50)
    ax.set_xlabel("quantity q (widgets)")
    ax.set_ylabel("dollars per widget")
    fs.save(fig, FOLDER, f"{SLUG}-average-and-marginal")


if __name__ == "__main__":
    related_rates()
    cone()
    average_and_marginal()
