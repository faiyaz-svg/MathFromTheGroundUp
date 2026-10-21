"""Figures for docs/05-university-core/02-derivatives/03-chain-rule-implicit-and-inverse-derivatives.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/chain-rule-implicit-and-inverse-derivatives.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "chain-rule-implicit-and-inverse-derivatives"
E = math.e
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def through_zero(ax, xlim, ylim, xticks, yticks, size=9):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xticks([t for t in xticks if t != 0])
    ax.set_yticks([t for t in yticks if t != 0])
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=size, length=3)


def dot(ax, x, y, colour):
    ax.plot([x], [y], "o", color=colour, ms=6, zorder=6)


def inverse_reflection():
    """e^x and ln x, mirror images in y = x, with tangent lines at (1, e) and (e, 1)."""
    fig, ax = fs.figure(5.0, 4.9)
    through_zero(ax, (-1.6, 4.6), (-1.6, 4.6), [-1, 1, 2, 3, 4], [-1, 1, 2, 3, 4])
    ax.plot([-1.6, 4.6], [-1.6, 4.6], color=fs.GRAY, lw=1.2, ls="--", zorder=2)
    xs = np.linspace(-1.6, 1.52, 300)
    ax.plot(xs, np.exp(xs), color=fs.GREEN, zorder=4)
    xl = np.linspace(0.2, 4.6, 300)
    ax.plot(xl, np.log(xl), color=fs.BLUE, zorder=4)
    # tangent lines: y = e x at (1, e), and y = x / e at (e, 1); both pass through the origin
    tx = np.array([0.0, 1.6])
    ax.plot(tx, E * tx, color=fs.GREEN, lw=1.4, ls="-", alpha=0.65, zorder=3)
    ty = np.array([0.0, 4.4])
    ax.plot(ty, ty / E, color=fs.BLUE, lw=1.4, alpha=0.65, zorder=3)
    dot(ax, 1, E, fs.GREEN)
    dot(ax, E, 1, fs.BLUE)
    ax.text(0.9, E + 0.12, "(1, e)", color=fs.GREEN, fontsize=9.5, ha="right", va="bottom")
    ax.text(E + 0.1, 0.85, "(e, 1)", color=fs.BLUE, fontsize=9.5, ha="left", va="top")
    ax.text(1.85, 4.25, "slope e", color=fs.GREEN, fontsize=9.5, ha="left", va="center")
    ax.text(4.0, 1.9, "slope 1/e", color=fs.BLUE, fontsize=9.5, ha="center", va="center")
    ax.text(-1.45, 1.5, "y = eˣ", color=fs.GREEN, fontsize=10, ha="left", va="center", bbox=BOX)
    ax.text(3.2, -0.55, "y = ln x", color=fs.BLUE, fontsize=10, ha="center", va="center", bbox=BOX)
    ax.text(1.9, 2.6, "y = x", color=fs.GRAY, fontsize=9.5, ha="center", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-inverse")


def implicit_curves():
    fig, axs = plt.subplots(1, 2, figsize=(7.6, 3.9))
    # circle
    ax = axs[0]
    through_zero(ax, (-6.2, 7.6), (-6.2, 6.4), [-5, 5], [-5, 5])
    th = np.linspace(0, 2 * math.pi, 400)
    ax.plot(5 * np.cos(th), 5 * np.sin(th), color=fs.GREEN, zorder=4)
    tx = np.array([0.2, 7.2])
    ax.plot(tx, 4 - 0.75 * (tx - 3), color=fs.ORANGE, lw=1.8, zorder=5)
    ax.plot([0, 3], [0, 4], color=fs.GRAY, lw=1.2, ls="--", zorder=3)
    dot(ax, 3, 4, fs.ORANGE)
    ax.text(2.2, 4.8, "(3, 4)", color=fs.DARK, fontsize=9.5, ha="right", va="bottom")
    ax.text(7.5, -0.9, "slope $-\\frac{3}{4}$", color=fs.ORANGE, fontsize=9.5, ha="right", va="center")
    ax.text(1.0, 2.9, "radius,\nslope $\\frac{4}{3}$", color=fs.GRAY, fontsize=8.5, ha="right", va="center")
    ax.text(-4.2, -4.9, "$x^2 + y^2 = 25$", color=fs.GREEN, fontsize=10, ha="center", va="center")
    # folium of Descartes
    ax = axs[1]
    through_zero(ax, (-4.0, 6.4), (-4.0, 5.4), [-3, 3], [-3, 3])
    t1 = np.linspace(0.0, 60, 6000)
    t2 = np.linspace(-0.97, -0.0001, 3000)
    t3 = np.linspace(-60, -1.03, 6000)
    for tt in (t1, t2, t3):
        xx = 6 * tt / (1 + tt**3)
        yy = 6 * tt**2 / (1 + tt**3)
        mask = (xx > -4.5) & (xx < 6) & (yy > -4.5) & (yy < 6)
        xx = np.where(mask, xx, np.nan)
        yy = np.where(mask, yy, np.nan)
        ax.plot(xx, yy, color=fs.GREEN, zorder=4)
    tx = np.array([1.2, 5.2])
    ax.plot(tx, 6 - tx, color=fs.ORANGE, lw=1.8, zorder=5)
    p = 2 ** (4 / 3)
    q = 2 ** (5 / 3)
    ax.plot([0.8, 4.4], [q, q], color=fs.BLUE, lw=1.3, ls="--", zorder=3)
    ax.plot([q, q], [0.8, 4.4], color=fs.RED, lw=1.3, ls="--", zorder=3)
    dot(ax, 3, 3, fs.ORANGE)
    dot(ax, p, q, fs.BLUE)
    dot(ax, q, p, fs.RED)
    ax.text(4.5, 2.2, "slope $-1$", color=fs.ORANGE, fontsize=9, ha="left", va="bottom")
    ax.text(2.9, 3.3, "(3, 3)", color=fs.DARK, fontsize=9, ha="left", va="bottom")
    ax.text(0.1, q + 0.3, "horizontal\ntangent", color=fs.BLUE, fontsize=8.5, ha="left", va="bottom")
    ax.text(q + 0.12, 0.95, "vertical\ntangent", color=fs.RED, fontsize=8.5, ha="left", va="center")
    ax.text(-3.8, -3.55, "$x^3 + y^3 = 6xy$", color=fs.GREEN, fontsize=10, ha="left", va="center")
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-implicit")


if __name__ == "__main__":
    inverse_reflection()
    implicit_curves()
