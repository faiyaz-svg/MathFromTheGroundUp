"""Figures for docs/05-university-core/09-multivariable-calculus-light/03-multivariable-optimization-and-lagrange-multipliers.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/multivariable-optimization-and-lagrange-multipliers.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "multivariable-optimization-and-lagrange-multipliers"
BOX = dict(facecolor="white", edgecolor="none", pad=0.5, alpha=0.9)


def critical():
    """Contours of f = x^3 + y^3 - 3xy with a saddle at (0, 0) and a minimum at (1, 1)."""
    fig, ax = fs.figure(5.6, 4.6)
    X, Y = np.meshgrid(np.linspace(-1.7, 2.2, 400), np.linspace(-1.7, 2.2, 400))
    Z = X**3 + Y**3 - 3 * X * Y
    ax.contour(X, Y, Z, levels=[-0.9, -0.5, 0.5, 1, 2, 4, 8], colors=fs.GRAY, linewidths=1.0)
    ax.contour(X, Y, Z, levels=[0], colors=fs.BLUE, linewidths=2.0)
    ax.plot([0], [0], "s", color=fs.RED, ms=7, zorder=5)
    ax.plot([1], [1], "o", color=fs.GREEN, ms=8, zorder=5)
    ax.text(0.1, -0.12, "(0, 0) saddle, f = 0", color=fs.RED, fontsize=10, ha="left", va="top", bbox=BOX)
    ax.annotate("(1, 1) minimum, f = −1", xy=(1, 1), xytext=(0.75, -0.7), color=fs.GREEN, fontsize=10, ha="left", va="center", bbox=BOX, arrowprops=dict(arrowstyle="-", color=fs.GREEN, lw=1.2))
    ax.text(-1.6, 2.1, "blue: the level curve f = 0", fontsize=9.5, va="top", color=fs.BLUE)
    ax.set_aspect("equal")
    ax.set_xlim(-1.7, 2.2)
    ax.set_ylim(-1.7, 2.2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-critical")


def lagrange():
    """Left: f = x + 2y on the circle x^2 + y^2 = 5. Right: utility maximization on a budget line."""
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 4.0), gridspec_kw={"width_ratios": [1, 1.05]})
    th = np.linspace(0, 2 * np.pi, 400)
    r5 = 5**0.5
    a.plot(r5 * np.cos(th), r5 * np.sin(th), color=fs.DARK, lw=2.4)
    xs = np.linspace(-3.6, 3.6, 10)
    for c, col, lw in [(-3, fs.GRAY, 1.2), (0, fs.GRAY, 1.2), (3, fs.GRAY, 1.2), (5, fs.RED, 2.2)]:
        a.plot(xs, (c - xs) / 2, color=col, lw=lw)
    a.text(3.55, 0.85, "x + 2y = 5", color=fs.RED, fontsize=9.5, ha="right", va="bottom", rotation=-26)
    a.annotate("", xy=(1 + 0.9, 2 + 1.8), xytext=(1, 2), arrowprops=dict(arrowstyle="-|>", color=fs.BLUE, lw=2.2))
    a.annotate("", xy=(1 + 0.5, 2 + 1.0), xytext=(1, 2), arrowprops=dict(arrowstyle="-|>", color=fs.GREEN, lw=2.2))
    a.text(1.55, 3.95, "∇g = (2, 4)", color=fs.BLUE, fontsize=10, ha="left", va="center")
    a.text(1.75, 3.0, "∇f = (1, 2)", color=fs.GREEN, fontsize=10, ha="left", va="center")
    a.plot([1, -1], [2, -2], "o", color=fs.DARK, ms=6, zorder=5)
    a.text(2.35, 2.05, "(1, 2): max 5", fontsize=10, ha="left", va="center")
    a.text(0.1, -2.75, "(−1, −2): min −5", fontsize=9.5, ha="left", va="center")
    a.text(-3.6, -2.95, "circle: x² + y² = 5", fontsize=10, va="center")
    a.set_aspect("equal")
    a.set_xlim(-3.7, 3.7)
    a.set_ylim(-3.2, 4.4)
    a.axhline(0, color=fs.GRAY, lw=0.6)
    a.axvline(0, color=fs.GRAY, lw=0.6)
    a.set_xlabel("x")
    a.set_ylabel("y")
    a.tick_params(labelsize=9)

    x = np.linspace(2, 80, 400)
    for c, col in [(15, fs.GRAY), (24, fs.GREEN), (33, fs.GRAY)]:
        y = (c / x**0.4) ** (1 / 0.6)
        b.plot(x, y, color=col, lw=2.2 if col == fs.GREEN else 1.3)
    b.plot([0, 60], [40, 0], color=fs.RED, lw=2.4)
    b.plot([24], [24], "o", color=fs.DARK, ms=7, zorder=5)
    b.text(26.5, 25.5, "best bundle (24, 24)", fontsize=10, ha="left", va="bottom")
    b.text(4, 4, "budget line\n2x + 3y = 120", color=fs.RED, fontsize=10, ha="left", va="bottom")
    b.text(64, 12.5, "U = 24", color=fs.GREEN, fontsize=10, ha="left", va="center")
    b.text(64, 3.0, "U = 15", color=fs.GRAY, fontsize=9.5, ha="left", va="center")
    b.text(10.5, 52, "U = 33", color=fs.GRAY, fontsize=9.5, ha="left", va="center")
    b.set_xlim(0, 80)
    b.set_ylim(0, 56)
    b.set_xlabel("good x")
    b.set_ylabel("good y")
    b.grid(True)
    b.set_axisbelow(True)
    b.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-lagrange")


def cost():
    """The isoquant K^0.3 L^0.7 = 100 and isocost lines 3K + 7L = C."""
    fig, ax = fs.figure(5.8, 4.2)
    K = np.linspace(20, 300, 400)
    L = (100 / K**0.3) ** (1 / 0.7)
    ax.plot(K, L, color=fs.GREEN, lw=2.6)
    for C, col in [(800, fs.GRAY), (1000, fs.RED), (1300, fs.GRAY)]:
        ax.plot([0, C / 3], [C / 7, 0], color=col, lw=2.2 if col == fs.RED else 1.3)
    ax.plot([100], [100], "o", color=fs.DARK, ms=7, zorder=5)
    ax.text(107, 108, "cheapest way: K = L = 100", fontsize=10, ha="left", va="bottom")
    ax.text(300, 70, "isoquant Q = 100", color=fs.GREEN, fontsize=10, ha="right", va="bottom")
    ax.text(4, 190, "cost 1300", color=fs.GRAY, fontsize=9.5, ha="left", va="bottom")
    ax.text(4, 147, "cost 1000: touches the isoquant", color=fs.RED, fontsize=9.5, ha="left", va="bottom")
    ax.text(4, 118, "cost 800", color=fs.GRAY, fontsize=9.5, ha="left", va="bottom")
    ax.set_xlim(0, 330)
    ax.set_ylim(0, 200)
    ax.set_xlabel("capital K")
    ax.set_ylabel("labour L")
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.tick_params(labelsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-cost")


if __name__ == "__main__":
    critical()
    lagrange()
    cost()
