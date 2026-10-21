"""Figures for docs/05-university-core/03-applications-of-derivatives/04-concavity-and-curve-sketching.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/concavity-and-curve-sketching.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "concavity-and-curve-sketching"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def grid(ax, size=9):
    ax.tick_params(labelsize=size, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def tangent(ax, f, fp, c, half, color, lw=1.6):
    lx = np.array([c - half, c + half])
    ax.plot(lx, f(c) + fp(c) * (lx - c), color=color, lw=lw, zorder=2)
    ax.plot([c], [f(c)], "o", color=color, ms=5.5, zorder=5)


def concavity():
    """Concave up, concave down and an inflection point."""
    fig, axs = plt.subplots(1, 3, figsize=(10.0, 3.4))
    x = np.linspace(-2, 2, 300)

    a = axs[0]
    grid(a, 8)
    a.plot(x, x**2, color=fs.GREEN, lw=2.4, zorder=3)
    for c, col in [(-1.2, fs.RED), (0, fs.ORANGE), (1.2, fs.BLUE)]:
        tangent(a, lambda t: t**2, lambda t: 2 * t, c, 0.8, col)
    a.text(0, 3.5, "concave up", color=fs.DARK, fontsize=10.5, ha="center", va="center")
    a.text(0, 2.9, "slopes −2.4, 0, 2.4\nincrease", color=fs.DARK, fontsize=9, ha="center", va="center")
    a.set_xlim(-2.1, 2.1)
    a.set_ylim(-1.2, 4.3)

    b = axs[1]
    grid(b, 8)
    b.plot(x, -(x**2), color=fs.GREEN, lw=2.4, zorder=3)
    for c, col in [(-1.2, fs.RED), (0, fs.ORANGE), (1.2, fs.BLUE)]:
        tangent(b, lambda t: -(t**2), lambda t: -2 * t, c, 0.8, col)
    b.text(0, -3.5, "concave down", color=fs.DARK, fontsize=10.5, ha="center", va="center")
    b.text(0, -2.45, "slopes 2.4, 0, −2.4\ndecrease", color=fs.DARK, fontsize=9, ha="center", va="center")
    b.set_xlim(-2.1, 2.1)
    b.set_ylim(-4.3, 1.2)

    c_ax = axs[2]
    grid(c_ax, 8)
    f = lambda t: t**3
    c_ax.plot(x, f(x), color=fs.GREEN, lw=2.4, zorder=3)
    tangent(c_ax, f, lambda t: 3 * t**2, 0, 1.2, fs.RED, lw=1.8)
    c_ax.text(0.1, -3.4, "inflection at 0:\nthe tangent crosses\nthe curve", color=fs.RED, fontsize=9, ha="left", va="center")
    c_ax.text(-1.9, 6.4, "concave down, then up", color=fs.DARK, fontsize=10.5, ha="left", va="center")
    c_ax.set_xlim(-2.1, 2.1)
    c_ax.set_ylim(-8.8, 8.8)
    fs.save(fig, FOLDER, f"{SLUG}-concavity")


def mark(ax, px, py, text, color, dx, dy, ha="left", va="center", size=9.5):
    ax.plot([px], [py], "o", color=color, ms=6.5, zorder=6)
    ax.text(px + dx, py + dy, text, color=color, fontsize=size, ha=ha, va=va, bbox=BOX, zorder=7)


def quartic():
    """y = x^4 - 4x^3."""
    fig, ax = fs.figure(5.8, 4.2)
    grid(ax)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    x = np.linspace(-1.2, 4.35, 400)
    ax.plot(x, x**4 - 4 * x**3, color=fs.GREEN, lw=2.4, zorder=3)
    mark(ax, 0, 0, "(0, 0) inflection,\nflat tangent", fs.BLUE, 0.15, 5.5, va="bottom")
    mark(ax, 2, -16, "(2, −16) inflection", fs.BLUE, 0.15, 3.5, va="bottom")
    mark(ax, 3, -27, "(3, −27) minimum", fs.RED, -0.1, -2.6, ha="center", va="top")
    mark(ax, 4, 0, "(4, 0)", fs.DARK, 0.0, 4.5, ha="center", va="bottom")
    ax.text(1.2, 24, "y = x⁴ − 4x³", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax.set_xlim(-1.3, 4.6)
    ax.set_ylim(-34, 30)
    ax.set_xticks([-1, 1, 2, 3, 4])
    ax.set_yticks([-20, -10, 10, 20])
    fs.save(fig, FOLDER, f"{SLUG}-quartic")


def rational():
    """y = x^2 / (x - 1) with its asymptotes."""
    fig, ax = fs.figure(6.0, 4.4)
    grid(ax)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    xl = np.linspace(-4.2, 0.82, 300)
    xr = np.linspace(1.18, 5.4, 300)
    f = lambda t: t**2 / (t - 1)
    ax.plot(xl, f(xl), color=fs.GREEN, lw=2.4, zorder=3)
    ax.plot(xr, f(xr), color=fs.GREEN, lw=2.4, zorder=3)
    xs = np.linspace(-4.3, 5.5, 10)
    ax.plot(xs, xs + 1, color=fs.GRAY, lw=1.3, ls="--")
    ax.plot([1, 1], [-12, 14], color=fs.GRAY, lw=1.3, ls="--")
    ax.plot([0], [0], "o", color=fs.RED, ms=6.5, zorder=6)
    ax.annotate("(0, 0) local max", xy=(0, 0), xytext=(-2.6, 4.2), color=fs.RED, fontsize=9.5, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color=fs.RED, lw=1.0), bbox=BOX, zorder=7)
    mark(ax, 2, 4, "(2, 4) local min", fs.RED, 0.2, -1.4, ha="left", va="top")
    ax.text(1.12, 11.8, "x = 1", color=fs.GRAY, fontsize=9.5, ha="left", va="center")
    ax.text(4.9, 3.6, "y = x + 1", color=fs.GRAY, fontsize=9.5, ha="right", va="center", rotation=0)
    ax.text(-4.1, -8.0, "y = x²/(x − 1)", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax.set_xlim(-4.4, 5.6)
    ax.set_ylim(-10, 13)
    ax.set_xticks([-4, -2, 2, 4])
    ax.set_yticks([-8, -4, 4, 8, 12])
    fs.save(fig, FOLDER, f"{SLUG}-rational")


def xexp():
    """y = x e^(-x)."""
    fig, ax = fs.figure(6.0, 3.8)
    grid(ax)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    x = np.linspace(-1.6, 7, 500)
    ax.plot(x, x * np.exp(-x), color=fs.GREEN, lw=2.4, zorder=3)
    ax.plot([-1.6, 7], [0, 0], color=fs.GRAY, lw=1.0, ls="--")
    mark(ax, 1, 1 / np.e, "(1, 1/e) maximum", fs.RED, -0.15, 0.17, ha="right", va="bottom")
    mark(ax, 2, 2 * np.exp(-2), "(2, 2/e²) inflection", fs.BLUE, 0.2, 0.55, va="bottom")
    ax.text(6.9, 0.1, "y → 0 as x → ∞", color=fs.GRAY, fontsize=9.5, ha="right", va="bottom")
    ax.text(2.5, -0.7, "y = x e⁻ˣ", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    ax.set_xlim(-1.8, 7.2)
    ax.set_ylim(-1.2, 1.1)
    ax.set_xticks([-1, 1, 2, 3, 4, 5, 6, 7])
    ax.set_yticks([-1, -0.5, 0.5, 1])
    fs.save(fig, FOLDER, f"{SLUG}-x-exp")


def diminishing():
    """Q = 20 sqrt(L), and its marginal product."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.0, 3.6))
    L = np.linspace(0.01, 30, 400)
    grid(a)
    a.plot(L, 20 * np.sqrt(L), color=fs.GREEN, lw=2.4, zorder=3)
    for c, col in [(4, fs.RED), (16, fs.BLUE)]:
        mp = 10 / np.sqrt(c)
        lx = np.array([c - 5, c + 5])
        a.plot(lx, 20 * np.sqrt(c) + mp * (lx - c), color=col, lw=1.6, zorder=2)
        a.plot([c], [20 * np.sqrt(c)], "o", color=col, ms=6, zorder=5)
    a.text(4.6, 28, "slope 5 at L = 4", color=fs.RED, fontsize=9.5, ha="left", va="center")
    a.text(16.6, 68, "slope 2.5 at L = 16", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    a.text(1, 104, "Q = 20√L: concave", color=fs.GREEN, fontsize=10.5, ha="left", va="center")
    a.set_xlim(0, 30)
    a.set_ylim(0, 115)
    a.set_xlabel("workers L")
    a.set_ylabel("output Q")
    grid(b)
    b.plot(L[L > 0.5], 10 / np.sqrt(L[L > 0.5]), color=fs.RED, lw=2.4)
    b.text(10, 11.5, "marginal product 10/√L falls", color=fs.RED, fontsize=10.5, ha="left", va="center")
    b.set_xlim(0, 30)
    b.set_ylim(0, 14)
    b.set_xlabel("workers L")
    b.set_ylabel("output per extra worker")
    fs.save(fig, FOLDER, f"{SLUG}-diminishing-returns")


if __name__ == "__main__":
    concavity()
    quartic()
    rational()
    xexp()
    diminishing()
