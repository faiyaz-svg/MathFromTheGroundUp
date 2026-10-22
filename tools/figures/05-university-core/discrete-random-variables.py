"""Figures for docs/05-university-core/07-probability/03-discrete-random-variables.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/discrete-random-variables.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "discrete-random-variables"


def style(ax):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True, axis="y")
    ax.set_axisbelow(True)


def dice():
    """PMF and CDF of the sum of two dice."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.3))
    xs = np.arange(2, 13)
    ways = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
    pmf = ways / 36
    style(ax1)
    ax1.bar(xs, pmf, color=fs.GREEN, alpha=0.75, width=0.7, zorder=3)
    ax1.axvline(7, color=fs.DARK, lw=1.2, ls="--", zorder=4)
    ax1.text(7.2, 0.178, "mean 7", fontsize=9.5, color=fs.DARK, ha="left", va="center")
    ax1.set_xticks(xs)
    ax1.set_ylim(0, 0.2)
    ax1.set_xlabel("sum of two dice, x", fontsize=10)
    ax1.set_ylabel("P(X = x)", fontsize=10)
    cdf = np.cumsum(pmf)
    style(ax2)
    ax2.grid(True, axis="x")
    edges = np.concatenate([[1], xs, [13.5]])
    vals = np.concatenate([[0], cdf])
    for i in range(len(vals)):
        ax2.hlines(vals[i], edges[i], edges[i + 1], color=fs.BLUE, lw=2.2, zorder=4)
    ax2.plot(xs, cdf, "o", color=fs.BLUE, zorder=5, ms=5)
    ax2.plot(xs, np.concatenate([[0], cdf[:-1]]), "o", mfc="white", mec=fs.BLUE, zorder=5, ms=5)
    ax2.set_xticks(xs)
    ax2.set_ylim(-0.03, 1.08)
    ax2.set_xlim(1, 13.5)
    ax2.set_xlabel("x", fontsize=10)
    ax2.set_ylabel("P(X ≤ x)", fontsize=10)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-dice")


def families():
    """Binomial, geometric and Poisson PMFs."""
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 3.2))
    # binomial n = 10, p = 0.3
    ax = axes[0]
    style(ax)
    k = np.arange(0, 11)
    pmf = [math.comb(10, i) * 0.3**i * 0.7 ** (10 - i) for i in k]
    ax.bar(k, pmf, color=fs.BLUE, alpha=0.75, width=0.7, zorder=3)
    ax.axvline(3, color=fs.DARK, lw=1.2, ls="--", zorder=4)
    ax.text(3.3, 0.285, "mean 3", fontsize=9.5, ha="left", va="center")
    ax.set_xticks(range(0, 11, 2))
    ax.set_ylim(0, 0.32)
    ax.set_xlabel("binomial, n = 10, p = 0.3\nk = number of successes", fontsize=9.5, color=fs.BLUE)
    ax.set_ylabel("P(X = k)", fontsize=10)
    # geometric p = 0.2
    ax = axes[1]
    style(ax)
    k = np.arange(1, 16)
    pmf = 0.2 * 0.8 ** (k - 1)
    ax.bar(k, pmf, color=fs.GREEN, alpha=0.75, width=0.7, zorder=3)
    ax.axvline(5, color=fs.DARK, lw=1.2, ls="--", zorder=4)
    ax.text(5.4, 0.15, "mean 5", fontsize=9.5, ha="left", va="center")
    ax.set_xticks([1, 3, 5, 7, 9, 11, 13, 15])
    ax.set_ylim(0, 0.23)
    ax.set_xlabel("geometric, p = 0.2\nk = trial of the first success", fontsize=9.5, color=fs.GREEN)
    # Poisson lambda = 3
    ax = axes[2]
    style(ax)
    k = np.arange(0, 13)
    pmf = [math.exp(-3) * 3**i / math.factorial(i) for i in k]
    ax.bar(k, pmf, color=fs.ORANGE, alpha=0.75, width=0.7, zorder=3)
    ax.axvline(3, color=fs.DARK, lw=1.2, ls="--", zorder=4)
    ax.text(3.4, 0.21, "mean 3", fontsize=9.5, ha="left", va="center")
    ax.set_xticks(range(0, 13, 2))
    ax.set_ylim(0, 0.255)
    ax.set_xlabel("Poisson, λ = 3\nk = number of events", fontsize=9.5, color=fs.ORANGE)
    fig.tight_layout(w_pad=1.2)
    fs.save(fig, FOLDER, f"{SLUG}-families")


if __name__ == "__main__":
    dice()
    families()
