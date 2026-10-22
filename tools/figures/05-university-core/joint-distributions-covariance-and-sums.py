"""Figures for docs/05-university-core/07-probability/05-joint-distributions-covariance-and-sums.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/joint-distributions-covariance-and-sums.py
"""

import random
import sys
from pathlib import Path
from statistics import correlation

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "joint-distributions-covariance-and-sums"


def style(ax):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def scatter():
    """Three scatter plots: correlated, independent, and uncorrelated but dependent."""
    rng = random.Random(2026)
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 3.2))
    n = 150
    # panel 1: correlation about 0.8
    xs, ys = [], []
    for _ in range(n):
        x = rng.gauss(0, 1)
        y = 0.8 * x + 0.6 * rng.gauss(0, 1)
        xs.append(x)
        ys.append(y)
    # panel 2: independent
    x2 = [rng.gauss(0, 1) for _ in range(n)]
    y2 = [rng.gauss(0, 1) for _ in range(n)]
    # panel 3: y = x^2 with x uniform on [-1, 1]
    x3 = [rng.uniform(-1, 1) for _ in range(n)]
    y3 = [x * x for x in x3]
    data = [(xs, ys, fs.GREEN), (x2, y2, fs.BLUE), (x3, y3, fs.ORANGE)]
    names = ["positive correlation", "independent", "Y = X², fully dependent"]
    for ax, (x, y, c), name in zip(axes, data, names):
        style(ax)
        ax.plot(x, y, "o", color=c, alpha=0.65, ms=4.5, zorder=3)
        r = correlation(x, y)
        ax.set_xlabel(f"{name}\nsample correlation r = {r:.2f}", fontsize=9.5, color=c)
        ax.set_xticks([])
        ax.set_yticks([])
    axes[0].set_xlim(-3, 3)
    axes[0].set_ylim(-3, 3)
    axes[1].set_xlim(-3, 3)
    axes[1].set_ylim(-3, 3)
    axes[2].set_xlim(-1.2, 1.2)
    axes[2].set_ylim(-0.15, 1.15)
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-scatter")


def portfolio():
    """Standard deviation of a two-asset portfolio against the weight in asset A."""
    sa, sb = 0.20, 0.15
    w = np.linspace(0, 1, 300)
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    style(ax)
    for rho, col in [(1.0, fs.RED), (0.3, fs.ORANGE), (0.0, fs.BLUE), (-0.5, fs.GREEN)]:
        var = w**2 * sa**2 + (1 - w) ** 2 * sb**2 + 2 * w * (1 - w) * rho * sa * sb
        ax.plot(w, 100 * np.sqrt(var), color=col, lw=2.2)
    for y, rho, col in [(7.0, "ρ = 1", fs.RED), (5.2, "ρ = 0.3", fs.ORANGE),
                        (3.4, "ρ = 0", fs.BLUE), (1.6, "ρ = −0.5", fs.GREEN)]:
        ax.plot([0.66, 0.74], [y, y], color=col, lw=2.2)
        ax.text(0.76, y, rho, color=col, fontsize=10, ha="left", va="center")
    ax.axvline(0.5, color=fs.GRAY, lw=1.0, ls="--")
    ax.text(0.51, 21.2, "50/50 mix", fontsize=9.5, ha="left", va="center", color=fs.DARK)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 22.5)
    ax.set_xlabel("share of the portfolio in asset A (σ = 20%); the rest is in B (σ = 15%)",
                  fontsize=9.5)
    ax.set_ylabel("portfolio standard deviation (%)", fontsize=10)
    fs.save(fig, FOLDER, f"{SLUG}-portfolio")


if __name__ == "__main__":
    scatter()
    portfolio()
