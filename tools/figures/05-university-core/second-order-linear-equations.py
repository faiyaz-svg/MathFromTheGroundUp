"""Figures for docs/05-university-core/10-differential-equations-light/02-second-order-linear-equations.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/second-order-linear-equations.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "second-order-linear-equations"
BOX = dict(facecolor="white", edgecolor="none", pad=0.4, alpha=0.9)


def damping():
    """Under-, critically and over-damped motion of a spring from x(0) = 1, x'(0) = 0."""
    fig, ax = fs.figure(7.0, 3.8)
    t = np.linspace(0, 6, 600)
    under = np.exp(-t) * (np.cos(2 * t) + 0.5 * np.sin(2 * t))
    crit = (1 + t) * np.exp(-t)
    over = (4 * np.exp(-t) - np.exp(-4 * t)) / 3
    R = np.sqrt(1.25)
    ax.plot(t, R * np.exp(-t), color=fs.GRAY, lw=1.2, ls="--")
    ax.plot(t, -R * np.exp(-t), color=fs.GRAY, lw=1.2, ls="--")
    ax.plot(t, under, color=fs.GREEN, lw=2.4)
    ax.plot(t, crit, color=fs.RED, lw=2.4)
    ax.plot(t, over, color=fs.BLUE, lw=2.4)
    ax.axhline(0, color=fs.DARK, lw=0.8)
    ax.text(2.0, -0.32, "underdamped (γ = 2, k = 5): roots −1 ± 2i", color=fs.GREEN, fontsize=9.5,
            ha="left", va="center", bbox=BOX)
    ax.text(0.5, 1.12, "critically damped (γ = 2, k = 1): root −1 twice", color=fs.RED, fontsize=9.5, ha="left",
            va="bottom")
    ax.text(1.9, 0.64, "overdamped (γ = 5, k = 4): roots −1 and −4", color=fs.BLUE, fontsize=9.5, ha="left",
            va="center", bbox=BOX)
    ax.text(3.0, -0.52, "dashed: the envelope ±1.118 e^(−t)", color=fs.GRAY, fontsize=9.5, ha="left", va="center")
    ax.set_xlim(0, 6)
    ax.set_ylim(-0.75, 1.5)
    ax.set_xlabel("time t")
    ax.set_ylabel("displacement x")
    ax.tick_params(labelsize=9)
    ax.grid(True)
    ax.set_axisbelow(True)
    fs.save(fig, FOLDER, f"{SLUG}-damping")


def saddle():
    """Phase portrait of x' = Ax with A = [[1, 2], [3, 0]]: eigenvalues 3 and -2."""
    fig, ax = fs.figure(5.6, 5.0)
    X, Y = np.meshgrid(np.linspace(-4, 4, 200), np.linspace(-4, 4, 200))
    U = X + 2 * Y
    V = 3 * X
    ax.streamplot(X, Y, U, V, color="#b9bdc2", linewidth=1.0, density=1.2, arrowsize=1.0)
    s = np.linspace(-4, 4, 10)
    ax.plot(s, s, color=fs.RED, lw=2.4, label="λ = 3, eigenvector (1, 1): solutions move away")
    ax.plot(s, -1.5 * s, color=fs.GREEN, lw=2.4, label="λ = −2, eigenvector (2, −3): solutions move toward 0")
    t = np.linspace(-0.5, 0.5, 200)
    px = np.exp(3 * t) + np.exp(-2 * t)
    py = np.exp(3 * t) - 1.5 * np.exp(-2 * t)
    ax.plot(px, py, color=fs.DARK, lw=2.4, label="the solution that starts at (2, −0.5)")
    ax.plot([2], [-0.5], "o", color=fs.DARK, ms=7, zorder=5)
    ax.plot([0], [0], "o", color=fs.DARK, ms=5)
    ax.set_aspect("equal")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_xlabel("x₁")
    ax.set_ylabel("x₂")
    ax.tick_params(labelsize=9)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.14), fontsize=9)
    fs.save(fig, FOLDER, f"{SLUG}-saddle")


if __name__ == "__main__":
    damping()
    saddle()
