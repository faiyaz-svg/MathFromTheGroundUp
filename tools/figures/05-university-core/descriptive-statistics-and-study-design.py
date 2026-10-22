"""Figures for docs/05-university-core/08-statistics/01-descriptive-statistics-and-study-design.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/descriptive-statistics-and-study-design.py
"""

import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "descriptive-statistics-and-study-design"


def style(ax, grid="y"):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True, axis=grid)
    ax.set_axisbelow(True)


def outlier():
    """Ten page load times with the mean and the median marked."""
    times = [120, 135, 128, 142, 131, 125, 138, 129, 133, 410]
    mean = st.mean(times)
    med = st.median(times)
    fig, ax = plt.subplots(figsize=(7.2, 2.7))
    style(ax, "x")
    ordered = sorted(times)
    ys = [0.06 * (i % 4) for i in range(len(ordered))]
    ax.plot(ordered[:-1], ys[:-1], "o", color=fs.DARK, ms=7, zorder=4)
    ax.plot([410], [0], "o", color=fs.RED, ms=8, zorder=5)
    ax.axvline(med, color=fs.GREEN, lw=2, ymax=0.78, zorder=3)
    ax.axvline(mean, color=fs.BLUE, lw=2, ymax=0.78, zorder=3)
    ax.text(med - 6, 0.62, "median 132", color=fs.GREEN, ha="right", va="center", fontsize=10)
    ax.text(mean + 6, 0.62, "mean 159.1", color=fs.BLUE, ha="left", va="center", fontsize=10)
    ax.text(410, 0.12, "410", color=fs.RED, ha="center", fontsize=10)
    ax.set_ylim(-0.12, 0.85)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.set_xlim(100, 430)
    ax.set_xlabel("page load time (ms)", fontsize=10)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-outlier")


def sampling():
    """A skewed population and the distribution of sample means."""
    rng = np.random.default_rng(2026)
    pop = rng.lognormal(mean=4.0, sigma=0.55, size=200_000)
    n = 30
    means = rng.choice(pop, size=(5000, n)).mean(axis=1)
    print("population mean", pop.mean(), "median", np.median(pop), "sd", pop.std())
    print("sample means: mean", means.mean(), "sd", means.std(), "sigma/sqrt(n)", pop.std() / np.sqrt(n))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.3), sharex=True)
    bins = np.linspace(0, 260, 53)
    style(ax1)
    ax1.hist(pop, bins=bins, color=fs.GRAY, alpha=0.75, zorder=3, density=True)
    ax1.axvline(pop.mean(), color=fs.DARK, ls="--", lw=1.2, zorder=4)
    ax1.text(pop.mean() + 5, 0.0125, f"mean {pop.mean():.1f}", fontsize=9.5, ha="left")
    ax1.set_xlabel("population: one value (thousand dollars)", fontsize=10)
    ax1.set_ylabel("density", fontsize=10)
    style(ax2)
    ax2.hist(means, bins=np.linspace(0, 260, 105), color=fs.GREEN, alpha=0.8, zorder=3, density=True)
    ax2.axvline(pop.mean(), color=fs.DARK, ls="--", lw=1.2, zorder=4)
    ax2.set_xlabel(f"5000 sample means, n = {n} (thousand dollars)", fontsize=10)
    ax1.set_xlim(0, 260)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-sampling")


def simpson():
    """Page versions A and B: overall rates against rates by device."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.3), gridspec_kw={"width_ratios": [1, 1.5]})
    style(ax1)
    ax1.bar([0, 1], [4.8, 8.4], color=[fs.GREEN, fs.BLUE], width=0.6, zorder=3)
    for x, v in [(0, 4.8), (1, 8.4)]:
        ax1.text(x, v + 0.25, f"{v}%", ha="center", fontsize=10)
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(["A", "B"], fontsize=10)
    ax1.set_ylim(0, 11)
    ax1.set_ylabel("conversion rate (%)", fontsize=10)
    ax1.set_xlabel("all visitors together", fontsize=10)
    style(ax2)
    w = 0.34
    vals = {"desktop": (12, 10), "mobile": (3, 2)}
    for i, (seg, (a, b)) in enumerate(vals.items()):
        ax2.bar(i - w / 2 - 0.01, a, width=w, color=fs.GREEN, zorder=3)
        ax2.bar(i + w / 2 + 0.01, b, width=w, color=fs.BLUE, zorder=3)
        ax2.text(i - w / 2 - 0.01, a + 0.25, f"A {a}%", ha="center", fontsize=9.5)
        ax2.text(i + w / 2 + 0.01, b + 0.25, f"B {b}%", ha="center", fontsize=9.5)
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(["desktop", "mobile"], fontsize=10)
    ax2.set_ylim(0, 14.5)
    ax2.set_xlabel("split by device", fontsize=10)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-simpson")


if __name__ == "__main__":
    outlier()
    sampling()
    simpson()
