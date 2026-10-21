"""Figures for docs/05-university-core/04-integrals/06-applications-of-integrals.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/applications-of-integrals.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Ellipse  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "applications-of-integrals"


def style(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def between():
    """Area between y = x and y = x^2, and between sin x and cos x."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.5))
    # left panel
    style(ax1)
    x = np.linspace(0, 1, 300)
    ax1.fill_between(x, x**2, x, color=fs.GREEN, alpha=0.3, zorder=2)
    ax1.plot(x, x, color=fs.BLUE, lw=2.0, zorder=4)
    ax1.plot(x, x**2, color=fs.ORANGE, lw=2.0, zorder=4)
    x0 = 0.6
    ax1.plot([x0, x0], [x0**2, x0], color=fs.DARK, lw=1.6, zorder=5)
    ax1.set_xlim(-0.05, 1.3)
    ax1.set_ylim(-0.05, 1.12)
    ax1.set_xticks([0, 0.5, 1])
    ax1.set_yticks([0, 0.5, 1])
    ax1.text(1.03, 1.0, "y = x", color=fs.BLUE, fontsize=10, ha="left", va="center")
    ax1.text(1.03, 0.82, "y = x²", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax1.text(x0 + 0.03, 0.47, "x − x²", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax1.text(0.28, 0.62, "area = 1/6", color=fs.GREEN, fontsize=10.5, ha="center", va="center")
    # right panel
    style(ax2)
    t = np.linspace(0, 2 * math.pi, 500)
    a, b = math.pi / 4, 5 * math.pi / 4
    m = (t >= a) & (t <= b)
    ax2.fill_between(t[m], np.cos(t[m]), np.sin(t[m]), color=fs.GREEN, alpha=0.3, zorder=2)
    ax2.plot(t, np.sin(t), color=fs.BLUE, lw=2.0, zorder=4)
    ax2.plot(t, np.cos(t), color=fs.ORANGE, lw=2.0, zorder=4)
    ax2.axhline(0, color=fs.DARK, lw=0.8, zorder=3)
    ax2.set_xlim(-0.2, 2 * math.pi + 0.3)
    ax2.set_ylim(-1.45, 1.45)
    ax2.set_xticks([0, math.pi / 4, math.pi, 5 * math.pi / 4, 2 * math.pi])
    ax2.set_xticklabels(["0", "π/4", "π", "5π/4", "2π"])
    ax2.set_yticks([-1, 0, 1])
    ax2.text(3.7, 0.95, "y = sin x", color=fs.BLUE, fontsize=10, ha="left", va="center")
    ax2.text(5.2, -0.35, "y = cos x", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax2.text(2.2, 0.22, "area = 2√2", color=fs.GREEN, fontsize=9.5, ha="center", va="center")
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-between")


def revolve():
    """The curve y = sqrt(x) turned about the x-axis: a disc of radius sqrt(x) and thickness dx."""
    fig, ax = fs.figure(6.0, 3.6)
    style(ax)
    ax.set_aspect("equal")
    x = np.linspace(0, 4, 300)
    ax.fill_between(x, -np.sqrt(x), np.sqrt(x), color=fs.GREEN, alpha=0.18, zorder=1)
    ax.plot(x, np.sqrt(x), color=fs.DARK, lw=2.2, zorder=4)
    ax.plot(x, -np.sqrt(x), color=fs.DARK, lw=1.4, ls="--", zorder=3)
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
    # a representative disc
    x0, dx = 2.4, 0.22
    r = math.sqrt(x0)
    ax.fill_between([x0, x0 + dx], [-r, -r], [r, r], color=fs.ORANGE, alpha=0.5, zorder=3)
    ax.add_patch(Ellipse((x0, 0), 0.32, 2 * r, fill=False, ec=fs.ORANGE, lw=1.6, zorder=5))
    ax.plot([x0, x0], [0, r], color=fs.RED, lw=1.8, zorder=6)
    ax.add_patch(Ellipse((4, 0), 0.4, 4, fill=False, ec=fs.DARK, lw=1.2, zorder=3))
    ax.set_xlim(-0.3, 5.3)
    ax.set_ylim(-2.6, 2.7)
    ax.set_xticks([1, 2, 3, 4])
    ax.set_yticks([-2, -1, 1, 2])
    ax.text(0.15, 2.25, "y = √x", color=fs.DARK, fontsize=10.5, ha="left", va="center")
    ax.annotate("thin disc: radius √x,\nvolume πx dx", xy=(x0 + dx / 2, -r * 0.7), xytext=(0.1, -2.25),
                color=fs.ORANGE, fontsize=10, ha="left", va="center",
                arrowprops=dict(arrowstyle="->", color=fs.ORANGE, lw=1.2))
    ax.text(x0 - 0.28, r * 0.5, "r", color=fs.RED, fontsize=10, ha="right", va="center")
    ax.text(4.35, 0, "total\n8π", color=fs.GREEN, fontsize=11, ha="left", va="center")
    fs.save(fig, FOLDER, f"{SLUG}-revolve")


def surplus():
    """Consumer and producer surplus for D(q) = 100 - 2q and S(q) = 20 + 0.1 q^2."""
    fig, ax = fs.figure(5.8, 3.9)
    style(ax)
    q = np.linspace(0, 30, 400)
    D = 100 - 2 * q
    S = 20 + 0.1 * q**2
    qs = np.linspace(0, 20, 300)
    ax.fill_between(qs, 60, 100 - 2 * qs, color=fs.BLUE, alpha=0.25, zorder=2)
    ax.fill_between(qs, 20 + 0.1 * qs**2, 60, color=fs.ORANGE, alpha=0.3, zorder=2)
    ax.plot(q[D >= 0], D[D >= 0], color=fs.BLUE, lw=2.2, zorder=4)
    ax.plot(q, S, color=fs.ORANGE, lw=2.2, zorder=4)
    ax.plot([0, 20], [60, 60], color=fs.DARK, lw=1.2, ls="--", zorder=3)
    ax.plot([20, 20], [0, 60], color=fs.DARK, lw=1.2, ls="--", zorder=3)
    ax.plot([20], [60], "o", color=fs.DARK, ms=6, zorder=6)
    ax.set_xlim(0, 31)
    ax.set_ylim(0, 108)
    ax.set_xticks([0, 10, 20, 30])
    ax.set_yticks([20, 60, 100])
    ax.text(4.2, 76, "consumer surplus\n= 400", color=fs.BLUE, fontsize=10, ha="center", va="center")
    ax.text(11, 42, "producer surplus\n≈ 533.3", color=fs.ORANGE, fontsize=10, ha="center", va="center")
    ax.text(21.0, 66, "equilibrium\nq = 20, p = 60", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax.text(0.7, 103, "demand", color=fs.BLUE, fontsize=10.5, ha="left", va="center")
    ax.text(25, 85, "supply", color=fs.ORANGE, fontsize=10.5, ha="left", va="center")
    ax.set_xlabel("quantity q (thousands of units)", fontsize=9.5)
    ax.set_ylabel("price p (dollars)", fontsize=9.5)
    fs.save(fig, FOLDER, f"{SLUG}-surplus")


def lorenz():
    """A Lorenz curve L(x) = x^2 and the line of equality."""
    fig, ax = fs.figure(4.8, 4.6)
    style(ax)
    ax.set_aspect("equal")
    x = np.linspace(0, 1, 300)
    ax.fill_between(x, x**2, x, color=fs.RED, alpha=0.22, zorder=2)
    ax.fill_between(x, 0, x**2, color=fs.BLUE, alpha=0.18, zorder=2)
    ax.plot(x, x, color=fs.DARK, lw=1.6, ls="--", zorder=3)
    ax.plot(x, x**2, color=fs.BLUE, lw=2.2, zorder=4)
    ax.set_xlim(-0.03, 1.08)
    ax.set_ylim(-0.03, 1.08)
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks([0, 0.5, 1])
    ax.set_xlabel("share of population, poorest first", fontsize=9.5)
    ax.set_ylabel("share of total income", fontsize=9.5)
    ax.text(0.30, 0.55, "A", color=fs.RED, fontsize=12, ha="center", va="center")
    ax.text(0.72, 0.28, "B", color=fs.BLUE, fontsize=12, ha="center", va="center")
    ax.text(0.03, 1.0, "line of equality, L(x) = x", color=fs.DARK, fontsize=9.5, ha="left", va="center", rotation=0)
    ax.text(0.84, 0.5, "L(x) = x²", color=fs.BLUE, fontsize=10, ha="center", va="center")
    ax.plot([0.5, 0.5], [0, 0.25], color=fs.BLUE, lw=1.2, ls=":", zorder=3)
    ax.plot([0, 0.5], [0.25, 0.25], color=fs.BLUE, lw=1.2, ls=":", zorder=3)
    fs.save(fig, FOLDER, f"{SLUG}-lorenz")


if __name__ == "__main__":
    between()
    revolve()
    surplus()
    lorenz()
