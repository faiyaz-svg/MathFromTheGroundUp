"""Figures for docs/05-university-core/05-sequences-and-series/04-power-series-and-taylor-series.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/power-series-and-taylor-series.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "power-series-and-taylor-series"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def grid(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def exp_polynomials():
    """e^x and its Taylor polynomials of degree 1 to 4 at 0."""
    fig, ax = fs.figure(6.0, 4.2)
    grid(ax)
    x = np.linspace(-3, 3, 400)
    ax.plot(x, np.exp(x), color=fs.DARK, lw=2.8, zorder=6)
    cols = [fs.RED, fs.ORANGE, fs.BLUE, fs.GREEN]
    for n, c in zip(range(1, 5), cols):
        t = sum(x**k / math.factorial(k) for k in range(n + 1))
        ax.plot(x, t, color=c, lw=1.6, zorder=3)
    ax.text(3.08, 20.1, "eˣ", color=fs.DARK, fontsize=10.5, ha="left", va="center")
    ax.text(3.08, 4.0, "T₁", color=fs.RED, fontsize=10, ha="left", va="center")
    ax.text(3.08, 8.5, "T₂", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax.text(3.08, 13.0, "T₃", color=fs.BLUE, fontsize=10, ha="left", va="center")
    ax.text(3.08, 16.4, "T₄", color=fs.GREEN, fontsize=10, ha="left", va="center")
    ax.text(-2.9, -6.2, "T₁ = 1 + x\nT₂ = 1 + x + x²/2, and so on", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    ax.set_xlim(-3, 3.6)
    ax.set_ylim(-9, 21)
    ax.set_xlabel("x")
    fs.save(fig, FOLDER, f"{SLUG}-exp-polynomials")


def sin_polynomials():
    """sin x and Taylor polynomials of degree 1, 3, 5, 7, 9."""
    fig, ax = fs.figure(7.0, 4.0)
    grid(ax)
    x = np.linspace(-2 * math.pi, 2 * math.pi, 600)
    ax.plot(x, np.sin(x), color=fs.DARK, lw=2.8, zorder=6)
    cols = [fs.RED, fs.ORANGE, fs.BLUE, fs.GREEN, fs.GRAY]
    for n, c in zip((1, 3, 5, 7, 9), cols):
        t = sum((-1) ** ((k - 1) // 2) * x**k / math.factorial(k) for k in range(1, n + 1, 2))
        ax.plot(x, t, color=c, lw=1.6, zorder=3)
    ax.text(-6.2, 3.05, "sin x", color=fs.DARK, fontsize=10.5, ha="left", va="center", fontweight="bold")
    ax.text(-5.0, 3.05, "Taylor polynomials:", color=fs.DARK, fontsize=9.5, ha="left", va="center")
    for xx, lab, col in [(-1.7, "T₁", fs.RED), (-0.7, "T₃", fs.ORANGE), (0.3, "T₅", fs.BLUE), (1.3, "T₇", fs.GREEN), (2.3, "T₉", fs.GRAY)]:
        ax.text(xx, 3.05, lab, color=col, fontsize=10.5, ha="left", va="center")
    ax.set_xlim(-2 * math.pi, 2 * math.pi)
    ax.set_ylim(-2.6, 3.4)
    ax.set_xticks([-2 * math.pi, -math.pi, 0, math.pi, 2 * math.pi])
    ax.set_xticklabels(["−2π", "−π", "0", "π", "2π"])
    ax.set_xlabel("x")
    fs.save(fig, FOLDER, f"{SLUG}-sin-polynomials")


def geometric_radius():
    """1/(1 - x) and partial sums of 1 + x + x^2 + ...; they follow the curve only for |x| < 1."""
    fig, ax = fs.figure(6.0, 4.2)
    grid(ax)
    ax.spines["bottom"].set_position("zero")
    x = np.linspace(-1.9, 0.93, 500)
    ax.plot(x, 1 / (1 - x), color=fs.DARK, lw=2.8, zorder=6)
    cols = {2: fs.RED, 4: fs.ORANGE, 8: fs.BLUE}
    for n, c in cols.items():
        t = sum(x**k for k in range(n + 1))
        ax.plot(x, t, color=c, lw=1.6, zorder=3)
    ax.axvspan(-1, 1, color=fs.GREEN, alpha=0.12, lw=0)
    ax.text(-0.97, 5.6, "radius R = 1:\nseries converges\nfor −1 < x < 1", color=fs.GREEN, fontsize=9.5, ha="left", va="center")
    ax.text(0.7, 3.4, "y = 1/(1 − x)", color=fs.DARK, fontsize=10, ha="right", va="center", bbox=BOX, zorder=8)
    ax.text(-1.85, 1.2, "T₂", color=fs.RED, fontsize=10, ha="left", va="center")
    ax.text(-1.85, 3.3, "T₄", color=fs.ORANGE, fontsize=10, ha="left", va="center")
    ax.text(-1.5, 8.0, "T₈", color=fs.BLUE, fontsize=10, ha="left", va="center")
    ax.set_xlim(-1.9, 1.1)
    ax.set_ylim(-1.5, 8.5)
    ax.set_xlabel("x")
    fs.save(fig, FOLDER, f"{SLUG}-geometric-radius")


if __name__ == "__main__":
    exp_polynomials()
    sin_polynomials()
    geometric_radius()
