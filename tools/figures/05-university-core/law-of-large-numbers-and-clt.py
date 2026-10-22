"""Figures for docs/05-university-core/07-probability/06-law-of-large-numbers-and-clt.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/law-of-large-numbers-and-clt.py
"""

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "law-of-large-numbers-and-clt"


def style(ax):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True)
    ax.set_axisbelow(True)


def lln():
    """Running averages of die rolls, with the band 3.5 plus or minus 2 sigma / sqrt(n)."""
    rng = np.random.default_rng(2026)
    n = np.arange(1, 5001)
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    style(ax)
    sigma = math.sqrt(35 / 12)
    ax.fill_between(n, 3.5 - 2 * sigma / np.sqrt(n), 3.5 + 2 * sigma / np.sqrt(n),
                    color=fs.GRAY, alpha=0.2, zorder=1)
    for col in [fs.GREEN, fs.BLUE, fs.ORANGE, fs.RED]:
        rolls = rng.integers(1, 7, size=5000)
        ax.plot(n, np.cumsum(rolls) / n, color=col, lw=1.5, zorder=3)
    ax.axhline(3.5, color=fs.DARK, lw=1.0, ls="--", zorder=2)
    ax.set_xscale("log")
    ax.set_xlim(1, 5000)
    ax.set_ylim(1, 6)
    ax.set_xlabel("number of rolls n", fontsize=10)
    ax.set_ylabel("average of the first n rolls", fontsize=10)
    ax.text(1.3, 3.65, "mean 3.5", fontsize=9.5, ha="left", va="bottom", color=fs.DARK)
    ax.text(40, 5.5, "gray band: 3.5 ± 2σ/√n", fontsize=9.5, ha="left", va="center",
            color=fs.DARK)
    fs.save(fig, FOLDER, f"{SLUG}-running-average")


def clt():
    """Standardized averages of dice (top) and of exponentials (bottom) against the normal curve."""
    rng = np.random.default_rng(7)
    fig, axes = plt.subplots(2, 4, figsize=(9.6, 4.6))
    z = np.linspace(-4, 4, 300)
    phi = np.exp(-z**2 / 2) / math.sqrt(2 * math.pi)
    reps = 40000
    rows = [
        ("dice", [1, 2, 5, 30], 3.5, math.sqrt(35 / 12), fs.GREEN,
         lambda n: rng.integers(1, 7, size=(reps, n)).mean(axis=1)),
        ("exponential", [1, 2, 10, 50], 1.0, 1.0, fs.BLUE,
         lambda n: rng.exponential(1.0, size=(reps, n)).mean(axis=1)),
    ]
    for r, (name, ns, mu, sd, col, draw) in enumerate(rows):
        for c, n in enumerate(ns):
            ax = axes[r][c]
            style(ax)
            xbar = draw(n)
            zs = (xbar - mu) / (sd / math.sqrt(n))
            if name == "dice":
                step = 1 / (sd * math.sqrt(n))
                lo = (1 - mu) / (sd / math.sqrt(n)) - step / 2
                bins = lo + step * np.arange(0, 5 * n + 2)
                ax.hist(zs, bins=bins, density=True, color=col, alpha=0.55, zorder=2)
            else:
                ax.hist(zs, bins=40, range=(-4, 4), density=True, color=col, alpha=0.55, zorder=2)
            ax.plot(z, phi, color=fs.DARK, lw=1.5, zorder=4)
            ax.set_xlim(-4, 4)
            ax.set_ylim(0, 0.75 if (name == "exponential" and n == 1) else 0.62)
            ax.set_yticks([])
            ax.set_xticks([-3, 0, 3])
            ax.set_xlabel(f"{name}, n = {n}", fontsize=9.5, color=col)
    fig.tight_layout(h_pad=1.0, w_pad=0.8)
    fs.save(fig, FOLDER, f"{SLUG}-clt")


def monte_carlo():
    """Average error of the hit-or-miss estimate of pi against n, on log-log axes."""
    rng = np.random.default_rng(11)
    p = math.pi / 4
    ns = np.array([10**k for k in range(2, 8)])
    errs = []
    for n in ns:
        hits = rng.binomial(n, p, size=400)
        errs.append(np.mean(np.abs(4 * hits / n - math.pi)))
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    style(ax)
    ref = 4 * math.sqrt(p * (1 - p)) * math.sqrt(2 / math.pi) / np.sqrt(ns)
    ax.loglog(ns, ref, color=fs.GRAY, lw=1.6, ls="--", zorder=2)
    ax.loglog(ns, errs, "o-", color=fs.GREEN, lw=2.0, zorder=4)
    ax.text(2e2, 0.009, "gray: 1/√n shape", fontsize=9.5, color=fs.DARK, ha="left", va="center")
    ax.text(1e4, 0.5, "green: simulated average error", fontsize=9.5, color=fs.GREEN,
            ha="left", va="center")
    ax.set_xlabel("number of random points n", fontsize=10)
    ax.set_ylabel("average error of the estimate of π", fontsize=10)
    ax.set_ylim(3e-4, 0.8)
    fs.save(fig, FOLDER, f"{SLUG}-monte-carlo")


if __name__ == "__main__":
    lln()
    clt()
    monte_carlo()
