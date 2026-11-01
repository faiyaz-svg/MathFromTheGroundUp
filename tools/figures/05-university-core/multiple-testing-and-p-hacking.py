"""Figures for docs/05-university-core/08-statistics/07-multiple-testing-and-p-hacking.md.

Run from the repo root:

    .venv/Scripts/python tools/figures/05-university-core/multiple-testing-and-p-hacking.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

import figstyle as fs  # noqa: E402

FOLDER = "05-university-core"
SLUG = "multiple-testing-and-p-hacking"


def style(ax, grid="y"):
    ax.tick_params(labelsize=9, length=3)
    ax.grid(True, axis=grid)
    ax.set_axisbelow(True)


def benjamini_hochberg():
    """The 12 sorted p-values of Example 1 against the Bonferroni, BH and 0.05 cutoffs."""
    p = np.array([0.001, 0.004, 0.0048, 0.011, 0.019, 0.027, 0.034, 0.042, 0.11, 0.31, 0.58, 0.83])
    m = len(p)
    k = np.arange(1, m + 1)
    fig, ax = plt.subplots(figsize=(7.2, 3.8))
    style(ax)
    ax.axhline(0.05, color=fs.GRAY, lw=1.4, ls="--", zorder=2)
    ax.text(12.6, 0.0515, "0.05, no correction", color="#5a5f68", ha="right", va="bottom", fontsize=9.5)
    ax.axhline(0.05 / m, color=fs.RED, lw=1.6, zorder=2)
    ax.text(12.6, 0.05 / m + 0.0015, "Bonferroni, 0.05 / 12 = 0.0042", color=fs.RED, ha="right", va="bottom", fontsize=9.5)
    ax.plot([0, 13], [0, 0.05 * 13 / m], color=fs.BLUE, lw=1.8, zorder=2)
    ax.text(10.2, 0.0275, "Benjamini-Hochberg line,\n0.05 x rank / 12", color=fs.BLUE, ha="left", va="center", fontsize=9.5)
    rejected = k <= 5
    ax.scatter(k[~rejected & (p < 0.12)], p[~rejected & (p < 0.12)], s=48, color=fs.GRAY, zorder=4)
    ax.scatter(k[rejected], p[rejected], s=58, color=fs.GREEN, zorder=5)
    # rank 3 (p = 0.0048) is the one that Holm rejects and Bonferroni does not
    ax.text(5.35, 0.019, "BH rejects ranks 1 to 5", color="#027a50", ha="left", va="center", fontsize=9.5)
    ax.text(12.6, 0.108, "ranks 10 to 12 have p = 0.31, 0.58, 0.83\n(above the top of the chart)", color="#5a5f68",
            ha="right", va="top", fontsize=9)
    ax.set_xlim(0, 12.8)
    ax.set_ylim(0, 0.115)
    ax.set_xticks(range(1, 13))
    ax.set_xlabel("rank of the p-value, smallest first", fontsize=10)
    ax.set_ylabel("p-value", fontsize=10)
    fig.tight_layout()
    fs.save(fig, FOLDER, f"{SLUG}-bh")


def peeking():
    """Left: z paths of A/A tests checked daily. Right: the chance of a false positive after d daily looks."""
    rng = np.random.default_rng(11)
    reps, days, per_day = 20_000, 14, 1000
    xa = rng.binomial(per_day, 0.05, (reps, days)).cumsum(axis=1)
    xb = rng.binomial(per_day, 0.05, (reps, days)).cumsum(axis=1)
    n = per_day * np.arange(1, days + 1)
    pool = (xa + xb) / (2 * n)
    z = (xb / n - xa / n) / np.sqrt(pool * (1 - pool) * 2 / n)
    sig = np.abs(z) > 1.96
    ever = sig.any(axis=1)
    print("at day 14 only", sig[:, -1].mean(), "days 7 and 14", sig[:, [6, 13]].any(axis=1).mean(), "daily", ever.mean())

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.6), gridspec_kw={"width_ratios": [1.15, 1]})
    style(ax1)
    d = np.arange(1, days + 1)
    shown = 40
    for i in range(shown):
        if not ever[i]:
            ax1.plot(d, z[i], color=fs.GRAY, lw=1.0, alpha=0.6, zorder=2)
    for i in range(shown):
        if ever[i]:
            ax1.plot(d, z[i], color=fs.RED, lw=1.3, alpha=0.85, zorder=3)
            first = int(np.argmax(sig[i]))
            ax1.scatter([d[first]], [z[i, first]], s=22, color=fs.RED, zorder=4)
    for level in (1.96, -1.96):
        ax1.hlines(level, 1, 14, color=fs.DARK, lw=1.2, ls="--", zorder=5)
    ax1.text(14.2, 1.96, "1.96", fontsize=9, va="center", ha="left")
    ax1.text(14.2, -1.96, "-1.96", fontsize=9, va="center", ha="left")
    ax1.text(4.3, 3.9, f"red: {int(ever[:shown].sum())} of {shown} A/A tests that\nshow p < 0.05 on some day", color=fs.RED,
             fontsize=9.5, ha="left", va="top")
    ax1.set_xlim(1, 15.2)
    ax1.set_ylim(-4, 4)
    ax1.set_xticks([1, 4, 7, 10, 14])
    ax1.set_xlabel("day of the test", fontsize=10)
    ax1.set_ylabel("z statistic of A against B (no real difference)", fontsize=10)

    style(ax2)
    rate = [sig[:, :j].any(axis=1).mean() * 100 for j in d]
    ax2.plot(d, rate, color=fs.RED, lw=2, marker="o", ms=4.5, zorder=3)
    ax2.axhline(5, color=fs.DARK, lw=1.3, ls="--", zorder=2)
    ax2.text(14, 6.2, "5% promised", ha="right", fontsize=9.5)
    labels = {1: (1.2, rate[0] - 2.4, "left"), 2: (1.8, rate[1] + 1.4, "right"), 5: (4.7, rate[4] + 1.4, "right"),
              14: (14.2, rate[13] + 1.4, "right")}
    for j, (x, y, ha) in labels.items():
        ax2.text(x, y, f"{rate[j - 1]:.1f}%", color=fs.RED, fontsize=9.5, ha=ha)
    ax2.set_xlim(0.5, 14.5)
    ax2.set_ylim(0, 27)
    ax2.set_xticks([1, 2, 5, 7, 10, 14])
    ax2.set_xlabel("number of daily looks, stopping at the first p < 0.05", fontsize=10)
    ax2.set_ylabel("A/A tests declared a winner (%)", fontsize=10)
    fig.tight_layout(w_pad=1.5)
    fs.save(fig, FOLDER, f"{SLUG}-peeking")


if __name__ == "__main__":
    benjamini_hochberg()
    peeking()
