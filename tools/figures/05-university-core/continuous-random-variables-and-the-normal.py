"""Figures for docs/05-university-core/07-probability/04-continuous-random-variables-and-the-normal.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/continuous-random-variables-and-the-normal.py
"""

import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "continuous-random-variables-and-the-normal"


def style(ax):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def density_and_cdf():
    """Exponential density with P(1 < X < 3) shaded, and its CDF."""
    lam = 0.5
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.4))
    x = np.linspace(0, 8, 400)
    f = lam * np.exp(-lam * x)
    F = 1 - np.exp(-lam * x)
    style(ax1)
    m = (x >= 1) & (x <= 3)
    ax1.fill_between(x[m], 0, f[m], color=fs.GREEN, alpha=0.35, zorder=2)
    ax1.plot(x, f, color=fs.GREEN, lw=2.2, zorder=4)
    ax1.set_xlim(0, 8)
    ax1.set_ylim(0, 0.56)
    ax1.set_xlabel("x (seconds)", fontsize=10)
    ax1.set_ylabel("density f(x)", fontsize=10)
    ax1.annotate("shaded area = P(1 < X < 3) = 0.3834", xy=(2.0, 0.12), xytext=(3.4, 0.24),
                 fontsize=9.5, color=fs.DARK, ha="left", va="center",
                 arrowprops=dict(arrowstyle="-", color=fs.DARK, lw=0.8))
    ax1.text(4.0, 0.42, "f(x) = 0.5 e^(−0.5x)", ha="left", va="center", fontsize=10,
             color=fs.GREEN)
    style(ax2)
    ax2.plot(x, F, color=fs.BLUE, lw=2.2, zorder=4)
    F1, F3 = 1 - math.exp(-0.5), 1 - math.exp(-1.5)
    ax2.plot([1, 3], [F1, F3], "o", color=fs.BLUE, zorder=5)
    ax2.hlines([F1, F3], 0, [1, 3], color=fs.GRAY, lw=1.0, ls="--", zorder=3)
    ax2.vlines([1, 3], 0, [F1, F3], color=fs.GRAY, lw=1.0, ls="--", zorder=3)
    ax2.text(1.15, F1 - 0.05, "F(1) = 0.3935", fontsize=9.5, ha="left", va="center")
    ax2.text(3.15, F3 - 0.05, "F(3) = 0.7769", fontsize=9.5, ha="left", va="center")
    ax2.text(4.6, 0.40, "P(1 < X < 3) =\nF(3) − F(1) = 0.3834", fontsize=9.5, ha="left",
             va="center", color=fs.DARK)
    ax2.set_xlim(0, 8)
    ax2.set_ylim(0, 1.05)
    ax2.set_xlabel("x (seconds)", fontsize=10)
    ax2.set_ylabel("F(x) = P(X ≤ x)", fontsize=10)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-density-cdf")


def normal_rule():
    """Normal curves with different mean and spread, and the 68-95-99.7 rule."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.4))
    x = np.linspace(-5, 6, 600)

    def pdf(x, mu, s):
        return np.exp(-((x - mu) ** 2) / (2 * s**2)) / (s * math.sqrt(2 * math.pi))

    style(ax1)
    ax1.plot(x, pdf(x, 0, 1), color=fs.GREEN, lw=2.2)
    ax1.plot(x, pdf(x, 2, 1), color=fs.BLUE, lw=2.2)
    ax1.plot(x, pdf(x, 0, 2), color=fs.ORANGE, lw=2.2)
    ax1.text(-0.3, 0.42, "μ = 0, σ = 1", color=fs.GREEN, fontsize=9.5, ha="right", va="center")
    ax1.text(3.2, 0.36, "μ = 2, σ = 1", color=fs.BLUE, fontsize=9.5, ha="left", va="center")
    ax1.text(-5.0, 0.15, "μ = 0, σ = 2", color=fs.ORANGE, fontsize=9.5, ha="left", va="center")
    ax1.set_xlim(-5.2, 6)
    ax1.set_ylim(0, 0.46)
    ax1.set_xlabel("x", fontsize=10)
    ax1.set_ylabel("density", fontsize=10)

    style(ax2)
    z = np.linspace(-4, 4, 600)
    y = pdf(z, 0, 1)
    cols = [(3, fs.GRAY, 0.3), (2, fs.BLUE, 0.35), (1, fs.GREEN, 0.45)]
    for k, c, a in cols:
        m = np.abs(z) <= k
        ax2.fill_between(z[m], 0, y[m], color=c, alpha=a, zorder=2)
    ax2.plot(z, y, color=fs.DARK, lw=1.8, zorder=4)
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(0, 0.52)
    ax2.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax2.set_xlabel("z, standard deviations from the mean", fontsize=10)
    ax2.text(0, 0.455, "68.3% within 1", ha="center", va="center", fontsize=9.5, color=fs.GREEN)
    ax2.text(0, 0.495, "95.4% within 2", ha="center", va="center", fontsize=9.5, color=fs.BLUE)
    ax2.text(3.9, 0.42, "99.7% within 3", ha="right", va="center", fontsize=9.5, color=fs.DARK)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-normal")


def sums():
    """Histograms of sums of n uniform(0, 1) variables, with the matching normal curve."""
    rng = random.Random(2026)
    fig, axes = plt.subplots(1, 4, figsize=(9.6, 2.9), sharey=False)
    for ax, n in zip(axes, [1, 2, 3, 12]):
        data = [sum(rng.random() for _ in range(n)) for _ in range(40000)]
        style(ax)
        ax.hist(data, bins=40, density=True, color=fs.GREEN, alpha=0.55, zorder=2)
        mu, s = n / 2, math.sqrt(n / 12)
        xs = np.linspace(mu - 4 * s, mu + 4 * s, 300)
        ax.plot(xs, np.exp(-((xs - mu) ** 2) / (2 * s**2)) / (s * math.sqrt(2 * math.pi)),
                color=fs.DARK, lw=1.6, zorder=4)
        ax.set_xlabel(f"sum of {n}" if n == 1 else f"sum of {n}", fontsize=10)
        ax.set_xlim(0, n if n < 12 else 12)
        if n == 12:
            ax.set_xlim(2.5, 9.5)
        ax.set_yticks([])
    fig.tight_layout(w_pad=1.0)
    fs.save(fig, FOLDER, f"{SLUG}-sums")


if __name__ == "__main__":
    density_and_cdf()
    normal_rule()
    sums()
